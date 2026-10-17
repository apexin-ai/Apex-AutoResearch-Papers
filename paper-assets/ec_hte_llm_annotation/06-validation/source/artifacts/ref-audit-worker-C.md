# Reference Audit Report — Worker C

**Date**: 2026-05-26
**Auditor**: Worker C (independent verification)
**Bib file**: `docs/paper/references.bib`

## Summary
- Total entries: 71
- Actually cited in tex files: 41
- Uncited entries (in bib but not referenced): 30
- Verified OK: 63
- Issues found: 8
- High-risk entries checked: 10/10

## Issues Found

### [black2000racial] — severity: HIGH
- **Problem**: **Wrong paper in bib.** The bib entry contains "The Impact of Economic Conditions on Participation in Disability Programs: Evidence from the Coal Boom and Bust" (Black, Daniel, Sanders, AER 2002) — a paper about how economic booms/busts affect disability program enrollment. However, the citation key says "racial" and the tex files use it as: `\citet{black2000racial} demonstrate that racial misclassification in administrative data biases disparity estimates` (related_work.tex:8, appendix.tex:218). This paper has nothing to do with racial misclassification or racial disparities. The claim is attributed to the wrong paper entirely.
- **Current bib**: title="The Impact of Economic Conditions on Participation in Disability Programs: Evidence from the Coal Boom and Bust", authors=Black/Daniel/Sanders, journal=AER, year=2002
- **Correct action**: Either (a) replace with the correct paper about racial misclassification (e.g., Knox et al. 2020 which is already cited separately for administrative records masking racial bias), or (b) find the actual Black et al. paper about racial misclassification, or (c) remove the racial misclassification claim from the tex if no supporting reference exists.
- **Citation usage**: INCORRECT — the text attributes a claim about racial misclassification to a paper about disability programs and coal booms.

### [dorn2022sharp] — severity: HIGH
- **Problem**: **Wrong DOI** in bib entry.
- **Current bib**: `doi={10.1080/01621459.2022.2064774}`
- **Correct value**: `doi={10.1080/01621459.2022.2069572}` (Source: [JASA](https://www.tandfonline.com/doi/abs/10.1080/01621459.2022.2069572))
- **Note**: This entry is not currently cited in any tex file, so the wrong DOI would only matter if cited later or if the bib is published as supplementary material. Also, bib key says 2022 but year field correctly says 2023.

### [wood2018challenges] — severity: MEDIUM
- **Problem**: **Incorrect page numbers.**
- **Current bib**: `pages={5179--5186}`
- **Correct value**: `pages={4586--4598}` (Source: [ACL Anthology D18-1488](https://aclanthology.org/D18-1488/))
- **Note**: This entry is not currently cited in any tex file.

### [patrini2017making] — severity: MEDIUM
- **Problem**: **Possibly incorrect page numbers.** Multiple sources report different page numbers for this CVPR 2017 paper.
- **Current bib**: `pages={1944--1952}`
- **Potentially correct**: Pages may be `2233--2241` based on some CVF OpenAccess references, though IEEE proceedings numbering can differ. Needs verification against the official IEEE proceedings.
- **Note**: This entry is not currently cited in any tex file.

### [sui2026ppci] — severity: MEDIUM
- **Problem**: **Potentially inaccurate citation context.** The tex describes this as "PPCI extends this to outcome-side misclassification" (related_work.tex:16) and uses it throughout as a method for "outcome-side error" correction. However, the actual paper "Prediction-Powered Conditional Inference" (Sui et al. 2026, arXiv:2603.05575) is about inference on conditional functionals at fixed test points using kernel-based localization — not specifically about outcome misclassification correction.
- **Current usage**: tex treats PPCI as a method correcting outcome-side prediction error
- **Actual paper content**: Conditional inference framework using ML predictions for conditional means estimation
- **Action needed**: Verify whether the authors' framing is a valid interpretation of how PPCI applies to their setting, or if a different reference should be used for outcome-side misclassification correction.

### [mozer2026ppi] — severity: MEDIUM
- **Problem**: **Potentially inaccurate citation context.** The tex describes this as "arm-specific PPI" (introduction.tex:22). The actual paper "PPI is the Difference Estimator" (Mozer 2026, arXiv:2603.19160) is about recognizing that PPI estimators are algebraically equivalent to classical survey sampling difference estimators — not specifically about arm-specific extensions.
- **Current usage**: tex uses it as evidence for "arm-specific PPI" as a baseline
- **Actual paper content**: Theoretical equivalence between PPI and the difference estimator from survey sampling
- **Action needed**: Verify whether "arm-specific PPI" is discussed in the paper or if a different reference is more appropriate.

### [bu2023forestiv] — severity: LOW
- **Problem**: **Misleading bib key.** The key `bu2023forestiv` suggests author "Bu" and year 2023, but the actual authors are Yang, McFowland III, Burtch, and Adomavicius, and the publication year is 2022 (INFORMS Journal on Data Science, vol 1, no 2). The bib content (authors, title, journal, year) is correct — only the key is misleading.
- **Current bib**: key=bu2023forestiv, author=Yang et al., year=2022 ✓
- **Note**: This is purely cosmetic and does not affect compilation or rendering, but could confuse collaborators.

### [tornberg2024chatgpt] — severity: LOW
- **Problem**: **Minor key-year mismatch.** The key says `2024` but `year={2025}` in the bib. The year field is correct: the paper was published online in 2024 but the official SAGE publication year is 2025 (Social Science Computer Review, vol 43, issue 6, pp 1181-1195).
- **Note**: No action needed; the bib content is correct.

## Verified OK (list)

### Cited entries (41 entries verified)
- `miao2018identifying`: ✓ Biometrika 105(4):987-993, 2018. Authors/title/venue correct. Not cited in tex (uncited but verified).
- `cinelli2020making`: ✓ JRSS-B 82(1):39-67, 2020. Correct. Not cited in tex.
- `borkan2019nuanced`: ✓ WWW 2019 Companion, pp 491-500. Correct. Cited correctly as CivilComments dataset source.
- `bound2001measurement`: ✓ Handbook of Econometrics vol 5, pp 3705-3843, 2001. Correct. Cited accurately for binary misclassification attenuation.
- `greenland1980effect`: ✓ AJE 112(4):564-569, 1980. Correct. Not cited in tex.
- `frazis2003estimating`: ✓ J. Econometrics 117(1):151-178, 2003. Correct. Cited accurately for exact bias formulas with misclassified binary regressors.
- `mahajan2006identification`: ✓ Econometrica 74(3):631-665, 2006. Correct. Cited accurately for IV approach to misclassification.
- `lewbel2007estimation`: ✓ Econometrica 75(2):537-551, 2007. Correct. Cited accurately for IV approach.
- `blackwell2017unified`: ✓ SMR 46(3):303-341, 2017. Correct. Not cited in tex.
- `fuller1987measurement`: ✓ Wiley, 1987. Correct. Cited accurately for foundational measurement error theory.
- `carroll2006measurement`: ✓ Chapman & Hall/CRC, 2nd ed, 2006. Correct. Cited accurately for nonlinear measurement error extension.
- `gustafson2003measurement`: ✓ Chapman & Hall/CRC, 2003. Correct. Cited accurately for Bayesian measurement error.
- `hu2008nonparametric`: ✓ Econometrica 76(1):195-216, 2008. Correct. Cited accurately for nonparametric identification.
- `northcutt2021confident`: ✓ JAIR 70:1373-1411, 2021. Correct. Not cited in tex.
- `dawid1979maximum`: ✓ Applied Statistics 28(1):20-28, 1979. Correct. Cited accurately as foundational annotation model.
- `passonneau2014benefits`: ✓ TACL 2:311-326, 2014. Correct. Cited accurately for item difficulty in annotation.
- `hovy2013learning`: ✓ NAACL-HLT 2013, pp 1120-1130. Correct. Cited accurately for annotator competence.
- `paun2018comparing`: ✓ TACL 6:571-585, 2018. Correct. Cited accurately for hierarchical priors in annotation.
- `athey2016recursive`: ✓ PNAS 113(27):7353-7360, 2016. Correct. Cited accurately for recursive partitioning / HTE.
- `athey2019generalized`: ✓ Annals of Statistics 47(2):1148-1178, 2019. Correct. Not cited in tex.
- `wager2018causal`: ✓ JASA 113(523):1228-1242, 2018. Correct. Cited accurately for causal forests.
- `chernozhukov2018dml`: ✓ Econometrics Journal 21(1):C1-C68, 2018. Correct. Cited accurately for DML.
- `kennedy2023dr`: ✓ EJS 17(2):3008-3049, 2023. Correct. Not cited in tex.
- `kunzel2019metalearners`: ✓ PNAS 116(10):4156-4165, 2019. Correct. Not cited in tex.
- `imai2010causal`: ✓ AJPS 54(2):543-560, 2010. Correct. Cited accurately for treatment misclassification (distinct from effect-modifier misclassification).
- `tan2024llm`: ✓ EMNLP 2024, pp 930-957. Correct. Cited correctly as survey of LLM annotation.
- `gilardi2023chatgpt`: ✓ PNAS 120(30):e2305016120, 2023. Correct. Cited accurately for LLM annotation performance.
- `tornberg2024chatgpt`: ✓ SSCR 43(6):1181-1195, 2025. Title/authors/venue correct. Year field 2025 matches official publication. Cited correctly.
- `ziems2024nlp`: ✓ Computational Linguistics 50(1):237-291, 2024. Correct. Cited correctly.
- `pangakis2023automated`: ✓ Findings of EMNLP 2023, pp 2284-2296. Correct. Not cited in tex.
- `ashwin2025bias`: ✓ SMR 2025, SAGE. Correct. Cited accurately for LLM error rate variation across demographic groups.
- `angelopoulos2023ppi`: ✓ Science 382(6671):669-674, 2023. Correct. Cited accurately for PPI framework.
- `messing2026hidden`: ✓ arXiv:2604.11581, 2026. Correct. Not cited in tex.
- `zrnic2024cross`: ✓ PNAS 121(15):e2322083121, 2024. Correct. Cited accurately for cross-prediction PPI extension.
- `zrnic2024active`: ✓ ICML 2024, PMLR 235. Correct. Cited accurately for active inference budget savings.
- `egami2023dsl`: ✓ NeurIPS 2023, vol 36. Correct. Cited accurately for DSL.
- `mozer2026ppi`: ✓ arXiv:2603.19160, 2026. Paper exists, authors/title correct. Citation context flagged separately.
- `sui2026ppci`: ✓ arXiv:2603.05575, 2026. Paper exists, authors/title correct. Citation context flagged separately.
- `bu2023forestiv`: ✓ INFORMS J. Data Science 1(2):138-155, 2022. Paper content correct. Key naming flagged separately.
- `fong2021machine`: ✓ Political Analysis 29(4):467-484, 2021. Correct. Not cited in tex.
- `grimmer2022text`: ✓ Princeton University Press, 2022. Correct. Cited accurately.
- `audinet2025benchmarking`: ✓ EMNLP 2025, pp 19757-19772. Correct. Cited accurately for benchmarking debiasing methods.
- `zhang2015character`: ✓ NeurIPS 28, 2015. Correct. Cited accurately as AG News dataset source.
- `etaiwi2025comparative`: ✓ arXiv:2506.18501, 2025. Correct. Also published in ScienceDirect. Cited accurately for AG News LLM accuracy levels.
- `barbieri2020tweeteval`: ✓ Findings of EMNLP 2020, pp 1644-1650. Correct. Cited accurately as TweetEval dataset/benchmark.
- `wang2020methods`: ✓ PNAS 117(48):30266-30275, 2020. Correct. Not cited in tex.
- `feder2022causal`: ✓ TACL 10:1138-1158, 2022. Correct. Not cited in tex.
- `keith2020text`: ✓ ACL 2020, pp 5332-5344. Correct. Not cited in tex.
- `semenova2021debiased`: ✓ Econometrics Journal 24(2):264-289, 2021. Correct. Not cited in tex.
- `nie2021quasi`: ✓ Biometrika 108(2):299-319, 2021. Correct. Cited accurately for R-learner.
- `lash2009applying`: ✓ Springer, 2009. Correct. Not cited in tex.
- `ogburn2012nondifferential`: ✓ Epidemiology 23(3):433-439, 2012. Correct. Not cited in tex.
- `battistin2014treatment`: ✓ J. Econometrics 178(2):707-715, 2014. Correct. Not cited in tex.
- `kennedy2020constructing`: ✓ arXiv:2009.10277, 2020. Correct. Cited accurately as UC Berkeley Hate Speech corpus.
- `guo2017calibration`: ✓ ICML 2017, pp 1321-1330. Correct. Cited accurately for temperature/Platt scaling.
- `camuffo2025variance`: ✓ arXiv:2601.02370, 2025. Correct. Not cited in tex.
- `cheng2024err`: ✓ arXiv:2412.14461, 2024. Correct. Not cited in tex.
- `ura2018heterogeneous`: ✓ Quantitative Economics 9(3):1335-1370, 2018. Correct. Not cited in tex.
- `gligoric2025unconfident`: ✓ NAACL 2025, pp 3514-3533. Correct. Not cited in tex.
- `knox2022testing`: ✓ Annual Review of Political Science 25:419-441, 2022. Correct. Not cited in tex.
- `knox2020administrative`: ✓ APSR 114(3):619-637, 2020. Correct. Cited accurately for racial misclassification in administrative records.
- `stewart1990matrix`: ✓ Academic Press, 1990. Correct. Cited accurately for condition number definition.
- `natarajan2013learning`: ✓ NeurIPS 26, 2013. Correct. Not cited in tex.
- `cheng2020learning`: ✓ ICML 2020, pp 1789-1799. Correct. Not cited in tex.
- `xia2020part`: ✓ NeurIPS 33, pp 7597-7610, 2020. Correct. Not cited in tex.
- `blette2024assessing`: ✓ SMMR 33(5):909-927, 2024. Correct. Cited accurately for missing effect modifier data (complementary problem).
- `veitch2020adapting`: ✓ UAI 2020, PMLR 124, pp 919-928. Correct. Not cited in tex.

## High-Risk Entries Detail

### mozer2026ppi (arXiv 2026)
- **Existence**: ✓ Confirmed. arXiv:2603.19160, posted 2026-03-19.
- **Authors**: Reagan Mozer. ✓ Correct.
- **Title**: "PPI is the Difference Estimator: Recognizing the Survey Sampling Roots of Prediction-Powered Inference" ✓ Correct.
- **Venue**: arXiv preprint. ✓ Correct.
- **Citation usage**: Described as "arm-specific PPI" in introduction.tex. ⚠ The paper is about theoretical equivalence of PPI and the difference estimator, not specifically about arm-specific extensions. May be inaccurate.

### sui2026ppci (arXiv 2026)
- **Existence**: ✓ Confirmed. arXiv:2603.05575, posted 2026-03-05.
- **Authors**: Yang Sui, Jin Zhou, Hua Zhou, Xiaowu Dai. ✓ Correct.
- **Title**: "Prediction-Powered Conditional Inference" ✓ Correct.
- **Venue**: arXiv preprint. ✓ Correct.
- **Citation usage**: Described as extending PPI to "outcome-side misclassification" in related_work.tex. ⚠ The paper is about conditional inference at test points using kernel localization. The "outcome-side misclassification" framing may be inaccurate.

### messing2026hidden (arXiv 2026)
- **Existence**: ✓ Confirmed. arXiv:2604.11581, posted 2026-04.
- **Authors**: Solomon Messing (NYU). ✓ Correct.
- **Title**: "Hidden Measurement Error in LLM Pipelines Distorts Annotation, Evaluation, and Benchmarking" ✓ Correct.
- **Venue**: arXiv preprint. ✓ Correct.
- **Citation usage**: Not cited in current tex files.

### audinet2025benchmarking (EMNLP 2025)
- **Existence**: ✓ Confirmed. ACL Anthology: 2025.emnlp-main.1000.
- **Authors**: Nicolas Audinet de Pieuchon, Adel Daoud, Connor Thomas Jerzak, Moa Johansson, Richard Johansson. ✓ Correct.
- **Title**: "Benchmarking Debiasing Methods for LLM-based Parameter Estimates" ✓ Correct.
- **Venue**: EMNLP 2025, pp 19757-19772. ✓ Correct.
- **Citation usage**: Cited accurately for benchmarking DSL/PPI and finding that debiasing can increase MSE with heterogeneous error. ✓

### ashwin2025bias (2025)
- **Existence**: ✓ Confirmed. Published in Sociological Methods & Research, 2025, SAGE.
- **Authors**: Julian Ashwin, Aditya Chhabra, Vijayendra Rao. ✓ Correct.
- **Title**: "Using Large Language Models for Qualitative Analysis can Introduce Serious Bias" ✓ Correct.
- **Venue**: SMR 2025. ✓ Correct.
- **Citation usage**: Cited accurately for documenting error rate variation across demographic groups. ✓

### camuffo2025variance (arXiv 2025)
- **Existence**: ✓ Confirmed. arXiv:2601.02370.
- **Authors**: Arnaldo Camuffo, Alfonso Gambardella, Saeid Kazemi, Jakub Malachowski, Abhinav Pandey. ✓ Correct.
- **Title**: "Variance-Aware LLM Annotation for Strategy Research: Sources, Diagnostics, and a Protocol for Reliable Measurement" ✓ Correct.
- **Venue**: arXiv preprint. ✓ Correct.
- **Citation usage**: Not cited in current tex files.

### etaiwi2025comparative (arXiv 2025)
- **Existence**: ✓ Confirmed. arXiv:2506.18501, submitted June 2025. Also published on ScienceDirect.
- **Authors**: Wael Etaiwi, Bushra Alhijawi. ✓ Correct.
- **Title**: "Comparative Evaluation of ChatGPT and DeepSeek Across Key NLP Tasks: Strengths, Weaknesses, and Domain-Specific Performance" ✓ Correct.
- **Venue**: arXiv preprint (also in journal). ✓ Correct.
- **Citation usage**: Cited accurately for empirical LLM accuracy levels on AG News. ✓

### gligoric2025unconfident (NAACL 2025)
- **Existence**: ✓ Confirmed. ACL Anthology: 2025.naacl-long.179.
- **Authors**: Kristina Gligorić, Tijana Zrnić, Cinoo Lee, Emmanuel Candès, Dan Jurafsky. ✓ Correct.
- **Title**: "Can Unconfident LLM Annotations Be Used for Confident Conclusions?" ✓ Correct.
- **Venue**: NAACL 2025, pp 3514-3533. ✓ Correct.
- **Citation usage**: Not cited in current tex files.

### cheng2024err (arXiv 2024)
- **Existence**: ✓ Confirmed. arXiv:2412.14461.
- **Authors**: Xiang Cheng, Raveesh Mayya, João Sedoc. ✓ Correct (note: bib correctly uses `\~{a}` for João).
- **Title**: "To Err Is Human; To Annotate, SILICON? Reducing Measurement Error in LLM Annotation" ✓ Correct.
- **Venue**: arXiv preprint. ✓ Correct.
- **Citation usage**: Not cited in current tex files.

### bu2023forestiv (key mismatch)
- **Existence**: ✓ Confirmed. INFORMS Journal on Data Science 1(2):138-155, 2022.
- **Authors**: Mochen Yang, Edward McFowland III, Gordon Burtch, Gediminas Adomavicius. ✓ Correct in bib.
- **Title**: "Achieving Reliable Causal Inference with Data-Mined Variables: A Random Forest Approach to the Measurement Error Problem" ✓ Correct.
- **Venue**: INFORMS J. Data Science. ✓ Correct.
- **Year**: 2022 ✓ Correct in bib. Key name `bu2023` is misleading but this is cosmetic only.
- **Citation usage**: Cited as "ForestIV" for forest-based instrumental variables. ✓ Accurate description of the paper.

## Uncited Entries

The following 30 entries exist in the bib but are not referenced in any tex file. They may be intentionally kept for future use or were removed during editing:

1. `miao2018identifying` — Proxy variables / unmeasured confounders
2. `cinelli2020making` — Sensitivity analysis / omitted variable bias
3. `greenland1980effect` — Misclassification with covariates (epidemiology)
4. `blackwell2017unified` — Measurement error + missing data (MI framework)
5. `northcutt2021confident` — Confident learning / noisy labels
6. `athey2019generalized` — Generalized random forests
7. `kennedy2023dr` — Doubly robust HTE estimation
8. `kunzel2019metalearners` — Metalearners / X-learner
9. `pangakis2023automated` — Automated annotation validation
10. `messing2026hidden` — Hidden measurement error in LLM pipelines
11. `fong2021machine` — ML predictions as regression covariates
12. `wang2020methods` — Correcting inference from ML predictions
13. `feder2022causal` — Causal inference in NLP
14. `keith2020text` — Text and causal inference
15. `semenova2021debiased` — Debiased ML of CATE
16. `lash2009applying` — Quantitative bias analysis (epidemiology)
17. `dorn2022sharp` — Sensitivity analysis for IPW (⚠ has wrong DOI)
18. `ogburn2012nondifferential` — Nondifferential misclassification of confounder
19. `battistin2014treatment` — Treatment effect with covariate measurement error
20. `camuffo2025variance` — Variance-aware LLM annotation
21. `cheng2024err` — SILICON method for LLM annotation error
22. `ura2018heterogeneous` — HTE with mismeasured endogenous treatment
23. `gligoric2025unconfident` — Unconfident LLM annotations / confident conclusions
24. `knox2022testing` — Causal theories with learned proxies
25. `natarajan2013learning` — Learning with noisy labels
26. `patrini2017making` — Loss correction for label noise (⚠ possible wrong pages)
27. `cheng2020learning` — Bounded instance-dependent label noise
28. `xia2020part` — Part-dependent label noise
29. `veitch2020adapting` — Text embeddings for causal inference
30. `wood2018challenges` — Text classifiers for causal inference (⚠ wrong pages)

## Notes

1. **No hallucinated papers detected.** All 71 entries correspond to real, verifiable publications.
2. **The most serious issue is `black2000racial`** — the bib contains a completely different paper from what the citation context claims. This must be fixed before submission.
3. **30 uncited entries** should be reviewed: either cite them or remove to keep the bib clean per standard practice. Some (e.g., `messing2026hidden`, `gligoric2025unconfident`, `camuffo2025variance`) are directly relevant to the paper's topic and their omission from the text may be an oversight.
4. **DOI for `dorn2022sharp`** is wrong but the entry is currently uncited.
5. **Page numbers** for `wood2018challenges` and possibly `patrini2017making` are incorrect but both entries are currently uncited.
