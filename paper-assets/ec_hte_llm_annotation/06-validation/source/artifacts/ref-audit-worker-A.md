# Reference Audit Report — Worker A

**Date**: 2026-05-26
**Auditor**: Worker A (automated verification via WebSearch + tex context check)

## Summary
- Total entries: 71
- Verified OK (bib + usage): 35
- Uncited entries (in bib but never \cite'd in tex): 30
- Issues found: 6
  - HIGH severity: 2
  - MEDIUM severity: 3
  - LOW severity: 1
- High-risk entries checked: 10/10

---

## Issues Found

### [sui2026ppci] — severity: HIGH
- **Problem**: **Citation describes a completely different paper's contribution.** The bib entry correctly points to Sui et al. (2026) "Prediction-Powered Conditional Inference" (arXiv:2603.05575), which is about nonparametric conditional mean estimation at a test point using kernel localization + ML predictions. It has **nothing to do with outcome-side misclassification or causal inference**.
- **Current bib**: Bibliographic data is correct.
- **Citation usage**: The tex files cite this paper in 4 locations (`introduction.tex:22`, `related_work.tex:16`, `method.tex:67`, `experiments.tex:7`, `appendix.tex:527`) all describing it as a method that "extends [PPI/DSL] to outcome-side misclassification." This is **factually wrong**. The acronym "PPCI" in the paper stands for "Prediction-Powered Conditional Inference," not "Post-Prediction Causal Inference" as used in the tex.
- **Possible correct paper**: The authors may have intended to cite Cadei et al. (2025) "Prediction-Powered Causal Inferences" (arXiv:2502.06343) or another paper entirely.
- **Risk**: Reviewer can trivially verify this is the wrong paper — would be flagged as a serious credibility issue.

### [black2000racial] — severity: HIGH
- **Problem**: **Wrong paper cited for a fabricated claim.** The bib entry correctly describes Black, Daniel & Sanders (2002) "The Impact of Economic Conditions on Participation in Disability Programs: Evidence from the Coal Boom and Bust" (AER 92(1):27-50). This paper studies how coal industry booms/busts affect disability program participation — it contains **no analysis of racial misclassification**.
- **Current bib**: Title, authors, journal, volume, pages, year (2002) all verified correct for the actual paper.
- **Citation usage**: `related_work.tex:8` and `appendix.tex:218` both state `\citet{black2000racial} demonstrate that racial misclassification in administrative data biases disparity estimates` — this claim is **not made in this paper**. The citation key itself contains "racial" suggesting confusion with a different paper.
- **Correct value**: The claim about racial misclassification in administrative data more closely matches Knox, Lowe & Mummolo (2020, APSR) which is already cited as `knox2020administrative`. Either replace with the correct citation or remove the claim.
- **Additional issue**: Bib key says `black2000` but year=2002.

### [pangakis2023automated] — severity: MEDIUM
- **Problem**: **Venue is fabricated.** The bib entry claims this appeared in "Findings of the Association for Computational Linguistics: EMNLP 2023" with pages 2284-2296. The paper does **not** appear in ACL Anthology's EMNLP 2023 proceedings. DBLP lists it only as an arXiv preprint (arXiv:2306.00176).
- **Current bib**: `booktitle={Findings of the Association for Computational Linguistics: EMNLP 2023}`, `pages={2284--2296}`
- **Correct value**: Should be `@article` with `journal={arXiv preprint arXiv:2306.00176}`, `year={2023}`, no pages field.
- **Citation usage**: Entry is never cited in any tex file (orphan entry), so this doesn't affect the compiled paper currently.

### [mozer2026ppi] — severity: MEDIUM
- **Problem**: **Citation usage mischaracterizes the paper.** The bib data is correct (Reagan Mozer, arXiv:2603.19160, 2026). However, `introduction.tex:22` cites it as "arm-specific PPI" — the paper is primarily about recognizing that PPI estimators are equivalent to classical survey sampling estimators (difference estimator, GREG). It does not propose an "arm-specific PPI" method.
- **Current bib**: Bibliographic data verified OK.
- **Correct value**: The citation context should be revised to accurately describe the paper's contribution (equivalence between PPI and survey sampling estimators).

### [wood2018challenges] — severity: MEDIUM
- **Problem**: **Wrong page numbers.**
- **Current bib**: `pages={5179--5186}`
- **Correct value**: `pages={4586--4598}` per ACL Anthology (https://aclanthology.org/D18-1488/)
- **Citation usage**: Entry is never cited in any tex file (orphan entry).

### [bu2023forestiv] — severity: LOW
- **Problem**: **Bib key naming mismatch.** Key prefix "bu2023" does not match the actual first author (Yang, Mochen) or publication year (2022). All content fields (title, authors, journal, volume, pages, year, DOI) are correct.
- **Current bib**: Key is `bu2023forestiv`, author is `Yang, Mochen and McFowland III, Edward and Burtch, Gordon and Adomavicius, Gediminas`, year=2022
- **Correct value**: Key should ideally be `yang2022forestiv` for consistency. Content is correct.
- **Citation usage**: OK — correctly described as using "forest-based instrumental variables" in `related_work.tex:16` and `introduction.tex:22`.

---

## Minor Key-Year Mismatches (cosmetic, do not affect rendered output)

- `tornberg2024chatgpt`: Key says 2024, year field = 2025 (journal issue date). First published online Sept 2024. Year field is correct.
- `dorn2022sharp`: Key says 2022, year field = 2023 (JASA publication date). Year field is correct.
- `camuffo2025variance`: arXiv ID prefix "2601" indicates Jan 2026 submission, but original submission Dec 2, 2025. Year=2025 is defensible.

---

## Uncited Entries (30 entries in bib but never \cite'd in any tex file)

These entries exist in `references.bib` but are not referenced by any `\cite`/`\citet`/`\citep` command. They will not appear in the compiled bibliography (assuming standard `\bibliography` workflow). Consider removing before submission.

| # | Key | Notes |
|---|-----|-------|
| 1 | `miao2018identifying` | Proximal causal inference |
| 2 | `cinelli2020making` | Sensitivity analysis |
| 3 | `greenland1980effect` | Misclassification with covariates |
| 4 | `blackwell2017unified` | Measurement error + missing data |
| 5 | `northcutt2021confident` | Confident learning |
| 6 | `athey2019generalized` | Generalized random forests |
| 7 | `kennedy2023dr` | Doubly robust HTE estimation |
| 8 | `kunzel2019metalearners` | Metalearners |
| 9 | `pangakis2023automated` | Also has venue issue (see above) |
| 10 | `fong2021machine` | ML predictions as covariates |
| 11 | `wang2020methods` | Correcting ML-predicted outcomes |
| 12 | `feder2022causal` | Causal inference in NLP |
| 13 | `keith2020text` | Text and causal inference |
| 14 | `semenova2021debiased` | Debiased ML for CATE |
| 15 | `messing2026hidden` | Hidden measurement error in LLM pipelines |
| 16 | `camuffo2025variance` | Variance-aware LLM annotation |
| 17 | `gligoric2025unconfident` | Unconfident LLM annotations |
| 18 | `cheng2024err` | LLM annotation measurement error |
| 19 | `lash2009applying` | Quantitative bias analysis |
| 20 | `dorn2022sharp` | Sensitivity analysis for IPW |
| 21 | `ogburn2012nondifferential` | Nondifferential misclassification |
| 22 | `battistin2014treatment` | Treatment effects + measurement error |
| 23 | `ura2018heterogeneous` | HTE with mismeasured treatment |
| 24 | `knox2022testing` | Causal theories with learned proxies |
| 25 | `natarajan2013learning` | Learning with noisy labels |
| 26 | `patrini2017making` | DNNs robust to label noise |
| 27 | `cheng2020learning` | Instance-dependent label noise |
| 28 | `xia2020part` | Part-dependent label noise |
| 29 | `veitch2020adapting` | Text embeddings for causal inference |
| 30 | `wood2018challenges` | Also has page number issue (see above) |

---

## Verified OK (35 entries — bib data correct + citation usage accurate)

- `borkan2019nuanced`: CivilComments dataset. Cited in experiments.tex, ethics.tex, appendix.tex. ✓
- `bound2001measurement`: Measurement error in surveys. Cited in related_work.tex, appendix.tex. ✓
- `frazis2003estimating`: Mismeasured binary regressors. Cited in related_work.tex, theory.tex, experiments.tex, appendix.tex. ✓
- `mahajan2006identification`: Misclassification identification. Cited in appendix.tex. ✓
- `lewbel2007estimation`: ATE with misclassification. Cited in appendix.tex. ✓
- `fuller1987measurement`: Measurement error models (book). Cited in related_work.tex, appendix.tex. ✓
- `carroll2006measurement`: Nonlinear measurement error (book). Cited in related_work.tex, appendix.tex. ✓
- `gustafson2003measurement`: Bayesian measurement error (book). Cited in appendix.tex. ✓
- `hu2008nonparametric`: IV for nonclassical measurement error. Cited in appendix.tex. ✓
- `dawid1979maximum`: Dawid-Skene model. Cited in appendix.tex. ✓
- `passonneau2014benefits`: Annotation modeling. Cited in appendix.tex. ✓
- `hovy2013learning`: MACE. Cited in appendix.tex. ✓
- `paun2018comparing`: Bayesian annotation models. Cited in appendix.tex. ✓
- `athey2016recursive`: Causal trees. Cited in related_work.tex. ✓
- `wager2018causal`: Causal forests. Cited in related_work.tex, experiments.tex, method.tex. ✓
- `chernozhukov2018dml`: Double ML. Cited in related_work.tex. ✓
- `imai2010causal`: Treatment misclassification. Cited in related_work.tex, appendix.tex. ✓
- `tan2024llm`: LLM annotation survey. Cited in introduction.tex. ✓
- `gilardi2023chatgpt`: ChatGPT outperforms crowd-workers. Cited in introduction.tex. ✓
- `tornberg2024chatgpt`: LLMs outperform expert coders. Cited in introduction.tex. ✓ (minor key-year cosmetic issue)
- `ziems2024nlp`: LLMs for CSS. Cited in introduction.tex. ✓
- `ashwin2025bias`: LLM bias in qualitative analysis. Cited in related_work.tex, introduction.tex. ✓
- `angelopoulos2023ppi`: PPI in Science. Cited in introduction.tex, related_work.tex, experiments.tex, appendix.tex. ✓
- `zrnic2024cross`: Cross-PPI. Cited in appendix.tex. ✓
- `zrnic2024active`: Active statistical inference. Cited in appendix.tex. ✓
- `egami2023dsl`: DSL for LLM surrogates. Cited in introduction.tex, related_work.tex, experiments.tex. ✓
- `grimmer2022text`: Text as Data (book). Cited in appendix.tex. ✓
- `zhang2015character`: AG News dataset source. Cited in appendix_agnews.tex. ✓
- `barbieri2020tweeteval`: TweetEval benchmark. Cited in experiments.tex, appendix_stance.tex. ✓
- `nie2021quasi`: R-learner. Cited in appendix.tex. ✓
- `audinet2025benchmarking`: Debiasing benchmarks. Cited in related_work.tex, appendix.tex. ✓
- `etaiwi2025comparative`: ChatGPT vs DeepSeek NLP evaluation. Cited in appendix_agnews.tex. ✓
- `kennedy2020constructing`: Measuring Hate Speech corpus. Cited in appendix.tex. ✓
- `guo2017calibration`: Neural network calibration. Cited in appendix.tex. ✓
- `knox2020administrative`: Racially biased policing records. Cited in appendix.tex. ✓
- `stewart1990matrix`: Matrix perturbation theory (book). Cited in appendix.tex. ✓
- `blette2024assessing`: HTE with missing effect modifiers. Cited in appendix.tex. ✓
- `mozer2026ppi`: PPI = difference estimator. Bib OK, but citation usage inaccurate (see Issues). ✓ bib / ✗ usage
- `sui2026ppci`: PPCI. Bib OK, but **citation usage completely wrong** (see Issues). ✓ bib / ✗ usage
- `bu2023forestiv`: ForestIV. Content OK, key naming mismatch (see Issues). Usage OK. ✓ content / ✗ key

---

## High-Risk Entries Detail

### mozer2026ppi (arXiv 2026)
- **Existence**: ✓ Confirmed via WebSearch. arXiv:2603.19160 by Reagan Mozer.
- **Title**: ✓ "PPI is the Difference Estimator: Recognizing the Survey Sampling Roots of Prediction-Powered Inference"
- **Authors**: ✓ Reagan Mozer
- **Year**: ✓ 2026
- **Venue**: ✓ arXiv preprint
- **Usage issue**: Cited as "arm-specific PPI" but the paper is about recognizing PPI's equivalence to classical survey estimators.

### sui2026ppci (arXiv 2026)
- **Existence**: ✓ Confirmed via WebSearch. arXiv:2603.05575 by Yang Sui, Jin Zhou, Hua Zhou, Xiaowu Dai.
- **Title**: ✓ "Prediction-Powered Conditional Inference"
- **Authors**: ✓ Yang Sui, Jin Zhou, Hua Zhou, Xiaowu Dai
- **Year**: ✓ 2026
- **Venue**: ✓ arXiv preprint
- **CRITICAL USAGE ERROR**: Paper is about kernel-localized conditional mean estimation. Cited in 4+ tex files as "outcome-side misclassification correction" — **completely wrong content attribution**.

### messing2026hidden (arXiv 2026)
- **Existence**: ✓ Confirmed via WebSearch. arXiv:2604.11581 by Solomon Messing.
- **Title**: ✓ "Hidden Measurement Error in LLM Pipelines Distorts Annotation, Evaluation, and Benchmarking"
- **Authors**: ✓ Solomon Messing
- **Year**: ✓ 2026
- **Venue**: ✓ arXiv preprint
- **Note**: Never cited in any tex file (orphan entry).

### audinet2025benchmarking (EMNLP 2025)
- **Existence**: ✓ Confirmed via ACL Anthology.
- **All fields verified**: ✓ Title, authors, venue (EMNLP 2025), pages (19757-19772).
- **Usage**: ✓ Correctly described as finding debiasing can increase MSE with heterogeneous error.

### ashwin2025bias (2025)
- **Existence**: ✓ Confirmed via SAGE/DOI lookup.
- **All fields verified**: ✓ Title, authors, journal (Sociological Methods & Research), year, DOI.
- **Usage**: ✓ Correctly cited for LLM annotation error rates varying across demographic subgroups.

### camuffo2025variance (arXiv 2025)
- **Existence**: ✓ Confirmed via WebSearch. arXiv:2601.02370.
- **All fields verified**: ✓ Title, authors, year (2025 defensible based on initial submission Dec 2, 2025).
- **Note**: Never cited in any tex file (orphan entry).

### etaiwi2025comparative (arXiv 2025)
- **Existence**: ✓ Confirmed via WebSearch. arXiv:2506.18501. Also published in ScienceDirect.
- **All fields verified**: ✓ Title, authors, year.
- **Usage**: ✓ Correctly cited for empirical LLM accuracy on AG News.

### gligoric2025unconfident (NAACL 2025)
- **Existence**: ✓ Confirmed via ACL Anthology.
- **All fields verified**: ✓ Title, authors, venue (NAACL 2025), pages (3514-3533).
- **Note**: Never cited in any tex file (orphan entry).

### cheng2024err (arXiv 2024)
- **Existence**: ✓ Confirmed via WebSearch. arXiv:2412.14461.
- **All fields verified**: ✓ Title, authors, year.
- **Note**: Never cited in any tex file (orphan entry).

### bu2023forestiv (key mismatch)
- **Existence**: ✓ Confirmed via INFORMS/DOI lookup.
- **All fields verified**: ✓ Title, authors (Yang et al.), journal (INFORMS Journal on Data Science), vol 1(2), pp 138-155, year 2022, DOI.
- **Issue**: Key prefix "bu2023" does not match first author "Yang" or year "2022." Content is correct — only key naming is wrong.
- **Usage**: ✓ Correctly described as forest-based IV method.
