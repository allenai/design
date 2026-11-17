# Source inventory and reuse boundaries

The resource is supporting evaluation material, not a technical specification. Attribution does not
by itself grant reuse rights, and the repository's MIT license does not supersede third-party terms.

| Material                                                                        | Source                                                                                                                                 | Distribution notice or review boundary                                                                                                                                               |
| ------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Consideration FPS clause titles/statements and the cross-cutting privacy clause | [EN 301 549 V3.2.1 (2021-03), clause 4.2](https://www.etsi.org/deliver/etsi_en/301500_301599/301549/03.02.01_60/en_301549v030201p.pdf) | Verify quoted wording/version and applicable ETSI/CEN/CENELEC reuse terms before public distribution. Do not treat original consideration interpretation as normative standard text. |
| Nielsen heuristic names and definitions                                         | [Jakob Nielsen, 10 Usability Heuristics for User Interface Design](https://www.nngroup.com/articles/ten-usability-heuristics/)         | Verify source version and applicable reuse terms before public distribution. Accessibility lenses are supporting interpretations, not an endorsement by Nielsen Norman Group.        |
| Cognitive consideration adaptations                                             | W3C COGA publications listed in the notice                                                                                             | Preserve [cognitive-accessibility-sources.LICENSE.md](../considerations/cognitive-accessibility-sources.LICENSE.md), including both governing licenses and adaptation notices.       |
| WCAG success-criterion reference                                                | [WCAG 2.2 Recommendation](https://www.w3.org/TR/WCAG22/)                                                                               | Preserve [wcag-requirements.LICENSE.md](wcag-requirements.LICENSE.md). Do not distribute the reference as an authoritative specification.                                            |
| Synthetic evaluation fixtures                                                   | Original repository SVG drawings and their PNG renders                                                                                 | Preserve [fixture provenance](../tests/fixtures/images/README.md) and the repository MIT notice.                                                                                     |

The versioned EN publication above is a verification reference, not a claim that a rights review has
been completed. Maintainers must record source-version checks, reuse clearance, and required
additional notices before public release. Do not add copied material with unknown or incompatible
terms. The excluded CC BY-NC-ND cognitive guidebook is not an authorized source for adaptations.

For packaging, paths in [provenance.json](../provenance.json) are relative to the resource root.
Rebase them explicitly if a distribution changes that root, and keep every referenced file.
