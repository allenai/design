# Release @allenai/design-system

A release is two acts:
1. **Bump** the version, in a merged PR.
2. **Run the Release workflow** on `main`. It:
   - rebuilds the generated files and commits them;
   - lints the specs;
   - tags `v<version>`;
   - creates the GitHub release;
   - publishes to npm when the `NPM_AUTH_TOKEN` secret is set.

The tag is what makes a version installable: `npm install "github:allenai/design#semver:^<version>"`.

## Picking the bump

Versions are `first.middle.last` (e.g. `0.6.0`).

| Change | Bump | Example |
| --- | --- | --- |
| A fix, value tweak or wording change | last number | 0.6.0 → 0.6.1 |
| Something added (token, spec, asset) | middle number | 0.6.0 → 0.7.0 |
| Something renamed or removed | first number | 0.6.0 → 1.0.0 |

Before bumping:
- run `git tag --sort=-v:refname | head -3` to see the latest release;
- run `gh pr list --state open` and ask whether any open PRs should merge first, since the release ships whatever is on `main`.

Bump `package.json`'s `"version"` and the `version:` line of each `DESIGN.md` the change touched. Commit as `Bump version to <new>`.

## Running the release

After the bump PR is merged, ask: "Shall I start the Release workflow on main?" On a yes:

```bash
gh workflow run release.yml --ref main
sleep 5; gh run list --workflow=release.yml --limit 1
gh run watch <run-id> --exit-status
```

Then verify:
- `git fetch --tags && git tag --sort=-v:refname | head -1` shows the new tag;
- `gh release view v<version>` shows the release;
- the run log says whether npm publishing happened or was skipped for want of the token.

Report what you found, including the skip.

### If the user would rather click through it, or `gh` can't run it

Give one step at a time and wait for "done" before the next:

1. **Merge the bump PR:** open the PR, click **Merge pull request**, then **Confirm merge**. Merge any other PRs meant for this release first.
2. **Open the Actions tab:** on `github.com/allenai/design`, click **Actions**.
3. **Choose the workflow:** in the left sidebar under "Workflows", click **Release**. The button doesn't appear on "All workflows".
4. **Open the menu:** click the **Run workflow** dropdown on the right.
5. **Check the branch:** it should say **main**.
6. **Start it:** click the green **Run workflow** button.
7. **Watch it:** refresh after a few seconds. The run shows a yellow dot while running and takes about 30 seconds; a green check means it worked.
8. **Check the release:** the repo's right sidebar should show the new version under **Releases**.

## If something goes wrong

- **403 mentioning SAML SSO on push or `gh`:** the user needs to run `gh auth refresh -h github.com` and approve the allenai organisation in the browser. They can type `! gh auth refresh -h github.com` in the Claude prompt.
- **"Version already has a tag":** the bump isn't merged, or the version didn't change. Check `package.json` on `main`.
- **No Run workflow button:** they're on "All workflows", or they lack write access to the repo. Ask a repo admin.
- **Lint or build step fails:** open the red step and read the error. It's usually a `DESIGN.md` problem. Fix it in a PR and run the workflow again; re-running is harmless.
- **Never create a tag by hand.** The workflow does it.
