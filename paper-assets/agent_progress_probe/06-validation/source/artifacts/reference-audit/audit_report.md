# Reference Audit Report — agent_progress_probe

Generated: 2026-05-15
Paper directory: `docs/paper/`

## Summary

| Metric | Count |
|---|---|
| .bib entries (references.bib) | 46 |
| .bib entries (_acl_template/custom.bib, unused) | 7 |
| Unique \cite keys in .tex | 46 |
| Total \cite commands | 79 |
| Missing (cited but no .bib entry) | **0** |
| Orphan (in references.bib but uncited) | **0** |
| OpenAlex verified | 39 |
| OpenAlex not_found (workshop / very recent / template) | 10 |
| OpenAlex mismatch (mostly parsing quirks) | 4 |
| Hallucinated citations | **0** |

All citations resolve cleanly; no compilation errors expected from missing keys.

## Cross-check

- **Missing**: none. Every `\cite{key}` in tex has a matching entry in `references.bib`.
- **Orphan in references.bib**: none. All 46 entries are referenced.
- **Orphan from `_acl_template/custom.bib`** (7 entries — NOT loaded by main.tex, which uses `\bibliography{references}` only):
  - `APA:83`, `Aho:72`, `Ando2005`, `Chandra:81`, `Gusfield:97`, `andrew2007scalable`, `rasooli-tetrault-2015`
  - These are ACL template example entries. The paper's bibliography file is `references.bib`, not `custom.bib`, so these do not appear in the compiled PDF. No action needed unless the template directory is removed for cleanup.

## Online Verification (OpenAlex)

### Verified (39)

xi2025agentprm, choudhury2025prm, li2026toolprmbench, wang2026planrewardbench, qiu2026dataprm, ratner2016dataprogramming, fu2020flyingsquid, ratner2019snorkelmetal, zhang2021wrench, safranchik2020linkedhmm, dawid1979em, lison2021skweak, li2020dividemix, han2018coteaching, maheshwari2022spear, orlanski2026slopcodebench, yang2024sweagent, wang2025openhands, shinn2023reflexion, zhou2024lats, yao2023tot, pipis2025reasoningloop, huang2024selfcorrect, kamoi2024selfcorrection, liu2026trajad, cho2014gru, bahdanau2015attention, zhang2025qwen3embedding, wang2024e5, chen2024bgem3, vanderaalst2016processmining, ma2024agentboard, liu2008isolationforest, malhotra2015lstmad, le2022coderl, sala2019multiresolution (after fix), ratner2017snorkel, jimenez2024swebench, george2025cycledetection

### Mismatch (4) — investigated, all benign

| Key | Issue | Resolution |
|---|---|---|
| `ratner2017snorkel` | OpenAlex year 2019; bib says 2017 | **Keep as-is.** Snorkel VLDB paper carries 2017 publication date (PVLDB Vol. 11, conference Sept 2018). Citation year 2017 is the standard convention used throughout the WS literature. |
| `sala2019multiresolution` | OpenAlex first_author `varma`, bib `sala` | **Fixed.** Author order in the bib was wrong. Updated to start with Paroma Varma and added the full author list per the NeurIPS proceedings. |
| `jimenez2024swebench` | OpenAlex parsed first_author as `jimenez-gomez` | **Benign parsing quirk.** Carlos E. Jimenez is the correct first author; OpenAlex sometimes splits Spanish surnames. |
| `george2025cycledetection` | OpenAlex first token `felix` (first name vs. surname) | **Benign parsing quirk.** Felix George is the correct first author; OpenAlex returned the first name as the surname key. |

### Not found in OpenAlex (10) — manually verified via WebSearch

OpenAlex indexes major venues; workshop papers, very recent arXiv preprints, and ACL template entries often miss. Each was confirmed via web search.

| Key | Verification | Status |
|---|---|---|
| `chen2025monitoring` | arXiv / OpenReview, ICLR 2025 "Building Trust" workshop, paper exists with matching title and authors | OK |
| `kale2025weaktostrong` | arXiv 2508.19461 confirmed (Scale Labs MRT paper) | OK |
| `fan2026agentrm` | arXiv 2601.22154 confirmed (CUHK MMLab / Meituan) | OK |
| `kaufman2012leakage` | ACM TKDD 6(4), doi:10.1145/2382577.2382579 confirmed | OK |
| `manheim2018goodhart` | arXiv 1803.04585 confirmed | OK |
| `cemri2025multiagentfail` | arXiv 2503.13657 confirmed | OK |
| `zhu2025agentfail` | arXiv 2509.25370 confirmed | OK |
| `APA:83`, `Chandra:81`, `andrew2007scalable` | ACL template debris in `_acl_template/custom.bib` — not loaded by the paper | irrelevant |

## Field completeness

All 46 entries in `references.bib` have title, author, year, and venue (booktitle/journal/publisher). No entry is missing a required field.

## Format consistency

- Venue names use **long form** consistently: "Advances in Neural Information Processing Systems" (not "NeurIPS"), "International Conference on Learning Representations" (not "ICLR"), "International Conference on Machine Learning" (not "ICML"), "Conference on Empirical Methods in Natural Language Processing" (not "EMNLP").
- arXiv preprints uniformly formatted as `journal = {arXiv preprint arXiv:YYMM.NNNNN}`.
- BibTeX keys use lowercase `firstauthor+year+slug` convention throughout.
- No inconsistent abbreviation, no mixed short/long forms.

## Year sanity

- All years fall in [1979, 2026], plausible.
- 2026 entries (8 papers) are post-cutoff-date arXiv preprints; all confirmed real via OpenAlex or WebSearch.
- No future-dated entries beyond the current date (2026-05-15).

## Changes made to references.bib

1. **`sala2019multiresolution`** (lines 107–112): replaced author list `{Frederic Sala and Paroma Varma and Jason Fries and others}` with the correct published order starting with Paroma Varma and listing the full author list with proper Christopher Ré accent: `{Paroma Varma and Frederic Sala and Shiori Sagawa and Jason Fries and Daniel Y. Fu and Saelig Khattar and Ashwini Ramamoorthy and Ke Xiao and Kayvon Fatahalian and James Priest and Christopher R{\'e}}`.

No other edits to `references.bib`.

## Recommendations (no action taken)

- Consider deleting the `_acl_template/` directory once the paper is finalized, to avoid confusion. It contains template example bib entries that the compiled bibliography does not actually use.
- The `chen2024bgem3` title in the bib begins "BGE M3-Embedding"; OpenAlex returned "M3-Embedding". Both forms appear in the wild — keep the BGE prefix since it matches the official arXiv title (arXiv:2402.03216).
