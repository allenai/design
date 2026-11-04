---
name: bump-version
description: Bump the @allenai/design-system version in package.json, open a PR for it, then walk the user step by step through merging it and running the Release workflow in GitHub. Use when the user asks to bump the version, cut or ship a release, or publish a new version of the design system.
---

# Bump the version and cut a release

A release is two separate acts: **bump** the version in `package.json` (Claude does this), then **run the Release workflow** on GitHub (the user does this, with Claude walking them through it). The workflow rebuilds generated files, tags the commit, and creates the GitHub release. That tag is what lets products install a version.

## 1. Pick the bump

Version is `first.middle.last` (for example `0.3.0`). Use the README's rule:

| Change | Bump | Example |
| --- | --- | --- |
| A fix or wording change | last number | 0.3.0 → 0.3.1 |
| Something added (new spec, tokens, assets) | middle number | 0.3.0 → 0.4.0 |
| Something renamed or removed | first number | 0.3.0 → 1.0.0 |

If the user hasn't said which, look at what is going out (`git log <last-tag>..main --oneline`), recommend one bump, and confirm in plain words before editing. Explain the options simply; don't assume they know semver.

## 2. Check what's pending

- `git tag --sort=-v:refname | head -3` for the latest release tag.
- `gh pr list --state open` for open PRs. Ask whether any should merge **before** the bump, since the release only includes what is on `main` when the workflow runs.

## 3. Bump and open a PR

1. `git checkout main && git pull`, then `git checkout -b <user>/bump-<new-version>`.
2. Edit only the `"version"` line in `package.json`. Leave `package-lock.json` alone; it has been out of sync for a long time and is not part of the release.
3. Commit as `Bump version to <new-version>` and push.
4. Open a PR into `main` with `gh pr create`. Say in the body that merging it does not cut the release.

## 4. Walk the user through the release

Do this one step at a time. Give the next step, then wait for the user to say it's done before giving the following one. Don't dump all of it at once. The user may be new to GitHub Actions.

1. **Merge the bump PR.** Open the PR link, click the green **Merge pull request** button, then **Confirm merge**. If any other PRs should ship in this release, merge them first.
2. **Open the Actions tab.** On `github.com/allenai/design`, click **Actions** in the top bar.
3. **Pick the Release workflow.** In the left sidebar under "Workflows", click **Release**. It's the second item, below `.github/workflows/publish.yml`. The Run workflow button doesn't appear on the "All workflows" page.
4. **Open Run workflow.** On the right, above the list of runs, click the **Run workflow** dropdown.
5. **Check the branch.** It must say **main**.
6. **Run it.** Click the green **Run workflow** button.
7. **Watch it.** Refresh after a few seconds; a new "Release" run appears with a yellow dot. It takes about 30 seconds. A green check means it worked.
8. **Verify.** Back on the repo's main page, the right sidebar shows **Releases** with the new version. Or run `git fetch --tags && git tag | tail -3`.

## If something goes wrong

- **Run fails saying the version already has a tag:** the bump PR isn't merged yet, or the version wasn't changed. Check `package.json` on `main`.
- **No Run workflow button:** they're on "All workflows", or lack write access to the repo. Go to the **Release** workflow page; ask a repo admin if the button is still missing.
- **Run fails in the lint or build step:** open the run, click the red step, and read the error. It is usually a `DESIGN.md` problem. Fix it in a PR, then run the workflow again; re-running is harmless.
- **"Not on npm":** that is expected. Publishing to npm needs the `NPM_AUTH_TOKEN` secret, so the workflow only creates the GitHub tag and release for now. Products install with `npm install "github:allenai/design#semver:^<version>"`.

## Don't

- Don't merge PRs or trigger the workflow yourself unless the user explicitly asks and the commands are permitted. Walking them through is the default.
- Don't edit the version in more than `package.json`, or add a git tag by hand. The workflow creates the tag.
