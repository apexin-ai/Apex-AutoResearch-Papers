# Reference Audit Report — Worker B

## Summary
- Total entries: 71
- Verified OK: 67
- Issues found: 4
- High-risk entries checked: 10/10

## Issues Found

### [black2000racial] — severity: HIGH
- **Problem**: Citation context mismatch — the bib entry contains a paper about disability programs, but the tex files cite it as demonstrating "racial misclassification in administrative data biases disparity estimates." The cited paper has nothing to do with racial misclassification.
- **Current bib**: Title = "The Impact of Economic Conditions on Participation in Disability Programs: Evidence from the Coal Boom and Bust", Authors = Black, Dan and Daniel, Kermit and Sanders, Seth, Journal = American Economic Review, Year = 2002
- **Citation usage in tex**:
  - `related_work.tex:8` — `\citet{black2000racial} demonstrate that racial misclassification in administrative data biases disparity estimates`
  - `appendix.tex:218` — `\citet{black2000racial} demonstrate that racial misclassification in administrative data can substantially bias estimates of racial disparities`
- **Correct action**: Either (a) replace the bib entry with the actual paper being described (no Black/Daniel/Sanders paper on racial misclassification was found — `knox2020administrative` is already cited separately and covers racially biased policing), or (b) rewrite the citation context to accurately describe the disability-programs paper. This is a factual error that a reviewer would catch.
- **Source**: https://www.aeaweb.org/articles?id=10.1257/000282802760015595

### [wood2018challenges] — severity: MEDIUM
- **Problem**: Wrong page numbers in bib entry.
- **Current bib**: pages = {5179--5186}
- **Correct value**: pages = {4586--4598} (ACL Anthology D18-1488)
- **Citation usage**: Correctly describes the paper's content.
- **Source**: https://aclanthology.org/D18-1488/

### [dorn2022sharp] — severity: MEDIUM
- **Problem**: Wrong DOI in bib entry.
- **Current bib**: doi = {10.1080/01621459.2022.2064774}
- **Correct value**: doi = {10.1080/01621459.2022.2069572}
- **Citation usage**: Not cited in the main tex files (may be in the bib for reference only). Title, authors, journal, volume, pages, year are all correct.
- **Source**: https://www.tandfonline.com/doi/abs/10.1080/01621459.2022.2069572

### [pangakis2023automated] — severity: MEDIUM
- **Problem**: Venue likely incorrect. The bib lists "Findings of the Association for Computational Linguistics: EMNLP 2023" with pages 2284--2296, but the paper does not appear in ACL Anthology's EMNLP 2023 Findings volume, nor in DBLP as a conference paper. DBLP indexes it only as arXiv preprint (journals/corr/abs-2306-00176).
- **Current bib**: booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2023}, pages = {2284--2296}
- **Correct value**: Likely an arXiv preprint only — arXiv:2306.00176. If it was published at a venue, the page numbers and booktitle need verification against ACL Anthology.
- **Citation usage**: Not cited in the main tex files visible in the grep output.
- **Source**: https://arxiv.org/abs/2306.00176

## Additional Notes (LOW severity, not counted as issues)

### [bu2023forestiv] — misleading bib key
- The key "bu2023forestiv" suggests author "Bu" and year 2023, but the actual entry has authors = Yang, McFowland III, Burtch, Adomavicius and year = 2022. Content is correct; key is arbitrary. No action needed unless clarity matters.

### [etaiwi2025comparative] — venue may be updatable
- Listed as "arXiv preprint arXiv:2506.18501" but appears to now be published in a journal (found on ScienceDirect: https://www.sciencedirect.com/science/article/pii/S2590005625001055). Consider updating to the published version for stronger citation.

## Verified OK (list)

- [miao2018identifying]: Miao, Geng, Tchetgen Tchetgen. Biometrika 2018, 105(4):987-993. Confirmed.
- [cinelli2020making]: Cinelli, Hazlett. JRSS-B 2020, 82(1):39-67. Confirmed.
- [borkan2019nuanced]: Borkan et al. WWW 2019, pp. 491-500. Confirmed.
- [bound2001measurement]: Bound, Brown, Mathiowetz. Handbook of Econometrics Vol 5, pp. 3705-3843, 2001. Confirmed.
- [greenland1980effect]: Greenland. AJE 1980, 112(4):564-569. Confirmed.
- [frazis2003estimating]: Frazis, Loewenstein. J. Econometrics 2003, 117(1):151-178. Confirmed.
- [mahajan2006identification]: Mahajan. Econometrica 2006, 74(3):631-665. Confirmed.
- [lewbel2007estimation]: Lewbel. Econometrica 2007, 75(2):537-551. Confirmed.
- [blackwell2017unified]: Blackwell, Honaker, King. Sociological Methods & Research 2017, 46(3):303-341. Confirmed.
- [fuller1987measurement]: Fuller. Measurement Error Models, Wiley 1987. Confirmed.
- [carroll2006measurement]: Carroll, Ruppert, Stefanski, Crainiceanu. 2nd ed., Chapman & Hall/CRC 2006. Confirmed.
- [gustafson2003measurement]: Gustafson. Chapman & Hall/CRC 2003. Confirmed.
- [hu2008nonparametric]: Hu, Schennach. Econometrica 2008, 76(1):195-216. Confirmed.
- [northcutt2021confident]: Northcutt, Jiang, Chuang. JAIR 2021, 70:1373-1411. Confirmed.
- [dawid1979maximum]: Dawid, Skene. Applied Statistics 1979, 28(1):20-28. Confirmed.
- [passonneau2014benefits]: Passonneau, Carpenter. TACL 2014, 2:311-326. Confirmed.
- [hovy2013learning]: Hovy, Berg-Kirkpatrick, Vaswani, Hovy. NAACL-HLT 2013, pp. 1120-1130. Confirmed.
- [paun2018comparing]: Paun et al. TACL 2018, 6:571-585. Confirmed.
- [athey2016recursive]: Athey, Imbens. PNAS 2016, 113(27):7353-7360. Confirmed.
- [athey2019generalized]: Athey, Tibshirani, Wager. Annals of Statistics 2019, 47(2):1148-1178. Confirmed.
- [wager2018causal]: Wager, Athey. JASA 2018, 113(523):1228-1242. Confirmed.
- [chernozhukov2018dml]: Chernozhukov et al. Econometrics Journal 2018, 21(1):C1-C68. Confirmed.
- [kennedy2023dr]: Kennedy. EJS 2023, 17(2):3008-3049. Confirmed.
- [kunzel2019metalearners]: Kunzel et al. PNAS 2019, 116(10):4156-4165. Confirmed.
- [imai2010causal]: Imai, Yamamoto. AJPS 2010, 54(2):543-560. Confirmed.
- [tan2024llm]: Tan et al. EMNLP 2024, pp. 930-957. Confirmed.
- [gilardi2023chatgpt]: Gilardi, Alizadeh, Kubli. PNAS 2023, 120(30):e2305016120. Confirmed.
- [tornberg2024chatgpt]: Tornberg. Social Science Computer Review 2025, 43(6):1181-1195. Confirmed (key says 2024 but year=2025 is correct for the published version).
- [ziems2024nlp]: Ziems et al. Computational Linguistics 2024, 50(1):237-291. Confirmed.
- [ashwin2025bias]: Ashwin, Chhabra, Rao. Sociological Methods & Research 2025. Confirmed.
- [angelopoulos2023ppi]: Angelopoulos et al. Science 2023, 382(6671):669-674. Confirmed.
- [messing2026hidden]: Messing. arXiv:2604.11581, 2026. Confirmed.
- [zrnic2024cross]: Zrnic, Candes. PNAS 2024, 121(15):e2322083121. Confirmed.
- [zrnic2024active]: Zrnic, Candes. ICML 2024, PMLR 235. Confirmed.
- [egami2023dsl]: Egami, Hinck, Stewart, Wei. NeurIPS 2023, vol. 36. Confirmed.
- [mozer2026ppi]: Mozer. arXiv:2603.19160, 2026. Confirmed.
- [sui2026ppci]: Sui, Zhou, Zhou, Dai. arXiv:2603.05575, 2026. Confirmed.
- [bu2023forestiv]: Yang, McFowland III, Burtch, Adomavicius. INFORMS J. Data Sci. 2022, 1(2):138-155. Content confirmed (key is misleading, see notes).
- [fong2021machine]: Fong, Tyler. Political Analysis 2021, 29(4):467-484. Confirmed.
- [grimmer2022text]: Grimmer, Roberts, Stewart. Princeton University Press 2022. Confirmed.
- [audinet2025benchmarking]: Audinet de Pieuchon et al. EMNLP 2025, pp. 19757-19772. Confirmed.
- [zhang2015character]: Zhang, Zhao, LeCun. NeurIPS 2015, vol. 28. Confirmed.
- [etaiwi2025comparative]: Etaiwi, Alhijawi. arXiv:2506.18501, 2025. Confirmed (see notes about journal publication).
- [barbieri2020tweeteval]: Barbieri et al. Findings of EMNLP 2020, pp. 1644-1650. Confirmed.
- [wang2020methods]: Wang, McCormick, Leek. PNAS 2020, 117(48):30266-30275. Confirmed.
- [feder2022causal]: Feder et al. TACL 2022, 10:1138-1158. Confirmed.
- [keith2020text]: Keith, Jensen, O'Connor. ACL 2020, pp. 5332-5344. Confirmed.
- [semenova2021debiased]: Semenova, Chernozhukov. Econometrics Journal 2021, 24(2):264-289. Confirmed.
- [nie2021quasi]: Nie, Wager. Biometrika 2021, 108(2):299-319. Confirmed.
- [lash2009applying]: Lash, Fox, Fink. Springer 2009. Confirmed.
- [dorn2022sharp]: Dorn, Guo. JASA 2023, 118(544):2645-2657. Title/authors/venue/pages confirmed (DOI issue noted above).
- [ogburn2012nondifferential]: Ogburn, VanderWeele. Epidemiology 2012, 23(3):433-439. Confirmed.
- [battistin2014treatment]: Battistin, Chesher. J. Econometrics 2014, 178(2):707-715. Confirmed.
- [kennedy2020constructing]: Kennedy, Bacon, Sahn, von Vacano. arXiv:2009.10277, 2020. Confirmed.
- [guo2017calibration]: Guo, Pleiss, Sun, Weinberger. ICML 2017, pp. 1321-1330. Confirmed.
- [camuffo2025variance]: Camuffo et al. arXiv:2601.02370, 2025. Confirmed.
- [cheng2024err]: Cheng, Mayya, Sedoc. arXiv:2412.14461, 2024. Confirmed.
- [ura2018heterogeneous]: Ura. Quantitative Economics 2018, 9(3):1335-1370. Confirmed.
- [gligoric2025unconfident]: Gligoric et al. NAACL 2025, pp. 3514-3533. Confirmed.
- [knox2022testing]: Knox, Lucas, Cho. Annual Review of Political Science 2022, 25:419-441. Confirmed.
- [knox2020administrative]: Knox, Lowe, Mummolo. APSR 2020, 114(3):619-637. Confirmed.
- [stewart1990matrix]: Stewart, Sun. Academic Press 1990. Confirmed.
- [natarajan2013learning]: Natarajan, Dhillon, Ravikumar, Tewari. NeurIPS 2013, vol. 26. Confirmed.
- [patrini2017making]: Patrini, Rozza, Krishna Menon, Nock, Qu. CVPR 2017, pp. 1944-1952. Confirmed.
- [cheng2020learning]: Cheng, Liu, Ramamohanarao, Tao. ICML 2020, pp. 1789-1799. Confirmed.
- [xia2020part]: Xia et al. NeurIPS 2020, vol. 33, pp. 7597-7610. Confirmed.
- [blette2024assessing]: Blette, Halpern, Li, Harhay. Statistical Methods in Medical Research 2024, 33(5):909-927. Confirmed.
- [veitch2020adapting]: Veitch, Sridhar, Blei. UAI 2020, pp. 919-928. Confirmed.

## High-Risk Entries Detail

### mozer2026ppi
- **Status**: VERIFIED OK
- **Verification**: Found on arXiv (2603.19160). Title: "PPI is the Difference Estimator: Recognizing the Survey Sampling Roots of Prediction-Powered Inference". Author: Reagan Mozer. Year: 2026. All match bib.
- **Citation usage**: Cited in `introduction.tex:22` as "arm-specific PPI" — accurate description of the paper's contribution.

### sui2026ppci
- **Status**: VERIFIED OK
- **Verification**: Found on arXiv (2603.05575). Title: "Prediction-Powered Conditional Inference". Authors: Yang Sui, Jin Zhou, Hua Zhou, Xiaowu Dai. Year: 2026. All match bib.
- **Citation usage**: Cited throughout as PPCI for outcome-side misclassification correction — accurate.

### messing2026hidden
- **Status**: VERIFIED OK
- **Verification**: Found on arXiv (2604.11581). Title: "Hidden Measurement Error in LLM Pipelines Distorts Annotation, Evaluation, and Benchmarking". Author: Solomon Messing. Year: 2026. All match bib.
- **Citation usage**: Not directly cited in the main tex files visible in grep output; in bib for reference.

### audinet2025benchmarking
- **Status**: VERIFIED OK
- **Verification**: Found on ACL Anthology (2025.emnlp-main.1000). Title, authors, venue (EMNLP 2025), pages (19757-19772) all match bib.
- **Citation usage**: Cited in `related_work.tex:17` and `appendix.tex:207` — describes benchmarking DSL/PPI and finding that debiasing can increase MSE with heterogeneous error. Accurate.

### ashwin2025bias
- **Status**: VERIFIED OK
- **Verification**: Found in Sociological Methods & Research, 2025, SAGE. DOI: 10.1177/00491241251338246. Title, authors all match.
- **Citation usage**: Cited in `introduction.tex:17` for error rates varying by demographic groups, and `related_work.tex:24` for error rates varying across subgroups. Accurate.

### camuffo2025variance
- **Status**: VERIFIED OK
- **Verification**: Found on arXiv (2601.02370). Title, authors match. Year 2025. Confirmed.
- **Citation usage**: Not cited in main tex files; in bib for reference.

### etaiwi2025comparative
- **Status**: VERIFIED OK (with note)
- **Verification**: Found on arXiv (2506.18501) and ScienceDirect. Title, authors match. Year 2025.
- **Note**: Now also published in a journal (ScienceDirect). Bib lists as arXiv preprint, which is technically still correct but could be updated.
- **Citation usage**: Cited in `appendix_agnews.tex:5` for LLM accuracy levels on AG News (~80%). Reasonable use.

### cheng2024err
- **Status**: VERIFIED OK
- **Verification**: Found on arXiv (2412.14461). Title: "To Err Is Human; To Annotate, SILICON? Reducing Measurement Error in LLM Annotation". Authors: Xiang Cheng, Raveesh Mayya, Joao Sedoc. Year 2024. All match.
- **Citation usage**: Not cited in main tex files; in bib for reference.

### gligoric2025unconfident
- **Status**: VERIFIED OK
- **Verification**: Found on ACL Anthology (2025.naacl-long.179). Title, authors, venue (NAACL 2025), pages (3514-3533) all match.
- **Citation usage**: Not cited in main tex files; in bib for reference.

### bu2023forestiv
- **Status**: VERIFIED OK (content correct, key misleading)
- **Verification**: Found on INFORMS (doi: 10.1287/ijds.2022.0019). Title: "Achieving Reliable Causal Inference with Data-Mined Variables: A Random Forest Approach to the Measurement Error Problem". Authors: Yang, McFowland III, Burtch, Adomavicius. Journal: INFORMS Journal on Data Science, Vol 1(2), pp. 138-155, 2022. All content matches bib entry.
- **Note**: Bib key "bu2023forestiv" does not match any author name ("bu" ≠ any of the four authors) and year (2023 ≠ 2022). The content fields are correct. Key is an arbitrary identifier so not a strict error, but is confusing.
- **Citation usage**: Cited in `introduction.tex:22` as "ForestIV" and `related_work.tex:16` as forest-based instrumental variables. Accurate description.
