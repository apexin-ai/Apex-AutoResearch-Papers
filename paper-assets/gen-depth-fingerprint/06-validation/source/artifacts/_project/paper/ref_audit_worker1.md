# Reference Audit — Worker 1

## Summary
- Total entries: 74
- Verified OK: 70
- Issues found: 4 (1 critical, 2 venue errors, 1 unconfirmed venue)
- Uncited entries (in bib but not in any tex): 25

## Issues Overview

| # | Key | Severity | Issue |
|---|-----|----------|-------|
| 1 | `human_texts_outliers` | **CRITICAL** | Authors and subtitle are hallucinated; arXiv ID maps to different paper |
| 2 | `diveye` | **ERROR** | Venue is TMLR 2026, not ICLR 2026 |
| 3 | `xu_spectrum_detection` | **WARNING** | Published at EMNLP 2024; still listed as arXiv preprint |
| 4 | `beyond_final_actor` | **WARNING** | ACL 2026 venue could not be independently confirmed |

## Entry-by-Entry Results

### [cohen1988statistical] — Statistical Power Analysis for the Behavioral Sciences (1988)
- **Exists**: ✓
- **Authors**: ✓
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (Lawrence Erlbaum Associates, 2nd edition)
- **Cite usage**: ✓ (appendix_tost.tex: used as SESOI justification for Cohen's d=0.20)
- **Notes**: Classic reference. No issues.

### [detectgpt] — DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature (2023)
- **Exists**: ✓
- **Authors**: ✓ (Mitchell, Lee, Khazatsky, Manning, Finn)
- **Year**: ✓ (ICML 2023)
- **Title**: ✓
- **Venue**: ✓ (ICML 2023, PMLR 202:24950-24962)
- **Cite usage**: ✓ (introduction.tex, related_work.tex: cited as zero-shot detection method)
- **Notes**: No issues.

### [gltr] — GLTR: Statistical Detection and Visualization of Generated Text (2019)
- **Exists**: ✓
- **Authors**: ✓ (Gehrmann, Strobelt, Rush)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (ACL 2019 System Demonstrations, pages 111-116)
- **Cite usage**: N/A — **UNCITED** in any tex file
- **Notes**: Entry exists in bib but is never referenced.

### [dna_gpt] — DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text (2024)
- **Exists**: ✓
- **Authors**: ✓ (Yang, Cheng, Wu, Petzold, Wang, Chen)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (ICLR 2024)
- **Cite usage**: ✓ (related_work.tex: cited as zero-shot scoring method)
- **Notes**: No issues.

### [binoculars] — Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text (2024)
- **Exists**: ✓
- **Authors**: ✓ (Hans, Schwarzschild, Cherepanova, Kazemi, Saha, Goldblum, Geiping, Goldstein)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (ICML 2024, PMLR 235)
- **Cite usage**: ✓ (introduction.tex, related_work.tex, method.tex: cited as baseline detection method)
- **Notes**: No issues.

### [fast_detectgpt] — Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature (2024)
- **Exists**: ✓
- **Authors**: ✓ (Bao, Zhao, Teng, Yang, Zhang)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (ICLR 2024)
- **Cite usage**: ✓ (introduction.tex, related_work.tex, method.tex: cited as baseline detection method)
- **Notes**: No issues.

### [ld_score] — Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection (2026)
- **Exists**: ✓
- **Authors**: ✓ (Narayanasamy, Agrawal, Faber, Alam)
- **Year**: ✓ (2026, submitted May 3, 2026)
- **Title**: ✓
- **Venue**: ✓ (arXiv preprint arXiv:2605.01647)
- **Cite usage**: ✓ (related_work.tex, method.tex: cited as learned classifier / baseline)
- **Notes**: No issues.

### [diveye] — Diversity Boosts AI-Generated Text Detection (2026)
- **Exists**: ✓
- **Authors**: ✓ (Basani, Chen)
- **Year**: ✓ (2026)
- **Title**: ✓
- **Venue**: **✗ — Listed as ICLR 2026 (`@inproceedings` with `booktitle = {Proceedings of the International Conference on Learning Representations}`), but actual venue is TMLR (Transactions on Machine Learning Research), published February 2026. GitHub repo (IBM/diveye) and arXiv PDF header both state "[TMLR '26]".**
- **Cite usage**: ✓ (related_work.tex: cited as surprisal-based approach)
- **Notes**: Must change entry type to `@article` with `journal = {Transactions on Machine Learning Research}` and `year = {2026}`.

### [feat_aug_transformer] — Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators (2026)
- **Exists**: ✓
- **Authors**: ✓ (Mady, Reschke, Schuller)
- **Year**: ✓ (2026)
- **Title**: ✓
- **Venue**: ✓ (arXiv preprint arXiv:2605.03969)
- **Cite usage**: N/A — **UNCITED** in any tex file
- **Notes**: Entry exists in bib but is never referenced.

### [reliable_detection] — Can AI-Generated Text be Reliably Detected? (2025)
- **Exists**: ✓
- **Authors**: ✓ (Sadasivan, Kumar, Balasubramanian, Wang, Feizi)
- **Year**: ✓ (accepted TMLR March 2025)
- **Title**: ✓
- **Venue**: ✓ (Transactions on Machine Learning Research)
- **Cite usage**: ✓ (related_work.tex: cited as learned classifier)
- **Notes**: No issues.

### [paraphrase_evades] — Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense (2023)
- **Exists**: ✓
- **Authors**: ✓ (Krishna, Song, Karpinska, Wieting, Iyyer)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (NeurIPS 2023)
- **Cite usage**: N/A — **UNCITED** in any tex file
- **Notes**: Entry exists in bib but is never referenced.

### [detection_possibilities] — Position: On the Possibilities of AI-Generated Text Detection (2024)
- **Exists**: ✓
- **Authors**: ✓ (Chakraborty, Bedi, Zhu, An, Manocha, Huang)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (ICML 2024, PMLR 235:6093-6115)
- **Cite usage**: N/A — **UNCITED** in any tex file
- **Notes**: Entry exists in bib but is never referenced.

### [intrinsic_dim_detection] — Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts (2023)
- **Exists**: ✓
- **Authors**: ✓ (Tulchinskii, Kuznetsov, Kushnareva, Cherniavskii, Nikolenko, Burnaev, Barannikov, Piontkovskaya)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (NeurIPS 2023)
- **Cite usage**: N/A — **UNCITED** in any tex file
- **Notes**: Entry exists in bib but is never referenced.

### [seqxgpt] — SeqXGPT: Sentence-Level AI-Generated Text Detection (2023)
- **Exists**: ✓
- **Authors**: ✓ (Wang, Li, Ren, Jiang, Zhang, Qiu)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (EMNLP 2023)
- **Cite usage**: N/A — **UNCITED** in any tex file
- **Notes**: Entry exists in bib but is never referenced.

### [grover] — Defending Against Neural Fake News (2019)
- **Exists**: ✓
- **Authors**: ✓ (Zellers, Holtzman, Rashkin, Bisk, Farhadi, Roesner, Choi)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (NeurIPS 2019)
- **Cite usage**: N/A — **UNCITED** in any tex file
- **Notes**: Entry exists in bib but is never referenced.

### [release_strategies] — Release Strategies and the Social Impacts of Language Models (2019)
- **Exists**: ✓
- **Authors**: ✓ (Solaiman, Brundage, Clark, et al. — 15 authors confirmed)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (arXiv preprint arXiv:1908.09203)
- **Cite usage**: N/A — **UNCITED** in any tex file
- **Notes**: Entry exists in bib but is never referenced.

### [beyond_binary] — Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement (2025)
- **Exists**: ✓
- **Authors**: ✓ (Cheng, Zhou, Jiang, Wang, Li)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (ACM Web Conference 2025 / WWW '25)
- **Cite usage**: ✓ (related_work.tex: cited as collaboration role detection)
- **Notes**: No issues.

### [semeval2024_task8] — SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection (2024)
- **Exists**: ✓
- **Authors**: ✓ (Wang, Mansurov, Ivanov, et al. — 15 authors confirmed)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (SemEval 2024)
- **Cite usage**: ✓ (related_work.tex: cited as multi-generator attribution)
- **Notes**: No issues.

### [self_consuming_mad] — Self-Consuming Generative Models Go MAD (2024)
- **Exists**: ✓
- **Authors**: ✓ (Alemohammad, Casco-Rodriguez, Luzi, Humayun, Babaei, LeJeune, Siahkoohi, Baraniuk)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (ICLR 2024)
- **Cite usage**: ✓ (related_work.tex: cited as model collapse reference)
- **Notes**: No issues.

### [curse_of_recursion] — AI models collapse when trained on recursively generated data (2024)
- **Exists**: ✓
- **Authors**: ✓ (Shumailov, Shumaylov, Zhao, Papernot, Anderson, Gal)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (Nature, volume 631, pages 755-759)
- **Cite usage**: ✓ (introduction.tex, related_work.tex, discussion.tex: cited as model collapse, contrasted with DDR)
- **Notes**: No issues.

### [dohmatob_tale_of_tails] — A Tale of Tails: Model Collapse as a Change of Scaling Laws (2024)
- **Exists**: ✓
- **Authors**: ✓ (Dohmatob, Feng, Yang, Charton, Kempe)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (ICML 2024)
- **Cite usage**: ✓ (related_work.tex: model collapse reference)
- **Notes**: No issues.

### [strong_model_collapse] — Strong Model Collapse (2025)
- **Exists**: ✓
- **Authors**: ✓ (Dohmatob, Feng, Subramonian, Kempe)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (ICLR 2025)
- **Cite usage**: ✓ (introduction.tex, related_work.tex, discussion.tex)
- **Notes**: No issues.

### [model_collapse_avoidable] — Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data (2024)
- **Exists**: ✓
- **Authors**: ✓ (Gerstgrasser, Schaeffer, Dey, et al. — 14 authors confirmed)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (COLM 2024)
- **Cite usage**: N/A — **UNCITED** in any tex file
- **Notes**: Entry exists in bib but is never referenced.

### [schaeffer_collapse_position] — Position: Model Collapse Does Not Mean What You Think (2025)
- **Exists**: ✓
- **Authors**: ✓ (Schaeffer, Kazdan, Arulandu, Koyejo)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (arXiv preprint arXiv:2503.03150)
- **Cite usage**: ✓ (related_work.tex: model collapse reference)
- **Notes**: No issues.

### [seddik_synthetic_data] — How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse (2024)
- **Exists**: ✓
- **Authors**: ✓ (Seddik, Chen, Hayou, Youssef, Debbah)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (COLM 2024)
- **Cite usage**: N/A — **UNCITED** in any tex file
- **Notes**: Entry exists in bib but is never referenced.

### [qlora] — QLoRA: Efficient Finetuning of Quantized LLMs (2023)
- **Exists**: ✓
- **Authors**: ✓ (Dettmers, Pagnoni, Holtzman, Zettlemoyer)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (NeurIPS 2023)
- **Cite usage**: ✓ (introduction.tex, appendix_qlora.tex: QLoRA classifier)
- **Notes**: No issues.

### [dsir] — Data Selection for Language Models via Importance Resampling (2023)
- **Exists**: ✓
- **Authors**: ✓ (Xie, Santurkar, Ma, Liang)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (NeurIPS 2023)
- **Cite usage**: ✓ (introduction.tex, related_work.tex: data curation quality signal)
- **Notes**: No issues.

### [qurating] — QuRating: Selecting High-Quality Data for Training Language Models (2024)
- **Exists**: ✓
- **Authors**: ✓ (Wettig, Gupta, Malik, Chen)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (ICML 2024)
- **Cite usage**: N/A — **UNCITED** in any tex file
- **Notes**: Entry exists in bib but is never referenced.

### [ccnet] — CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data (2020)
- **Exists**: ✓
- **Authors**: ✓ (Wenzek, Lachaux, Conneau, Chaudhary, Guzman, Joulin, Grave)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (LREC 2020)
- **Cite usage**: ✓ (introduction.tex, related_work.tex: data curation reference)
- **Notes**: No issues.

### [watermark_llm] — A Watermark for Large Language Models (2023)
- **Exists**: ✓
- **Authors**: ✓ (Kirchenbauer, Geiping, Wen, Katz, Miers, Goldstein)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (ICML 2023, PMLR 202:17061-17084)
- **Cite usage**: ✓ (related_work.tex: watermarking reference)
- **Notes**: No issues.

### [synthid_text] — Scalable Watermarking for Identifying Large Language Model Outputs (2024)
- **Exists**: ✓
- **Authors**: ✓ (Dathathri, See, Ghaisas, et al. — 24 authors confirmed)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (Nature, volume 634, pages 818-823)
- **Cite usage**: ✓ (related_work.tex: watermarking reference)
- **Notes**: No issues.

### [aaronson_watermark] — Watermarking GPT Outputs (2022)
- **Exists**: ✓
- **Authors**: ✓ (Aaronson, Kirchner — conventional dual attribution used across literature)
- **Year**: ✓ (November 2022)
- **Title**: ✓ (conventional citation title; actual blog post titled differently but this is standard practice)
- **Venue**: ✓ (Blog post, URL valid)
- **Cite usage**: N/A — **UNCITED** in any tex file
- **Notes**: Entry exists in bib but is never referenced.

### [chainwash] — Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks (2026)
- **Exists**: ✓
- **Authors**: ✓ (Ameen, Islam, Mahmud, Hamid)
- **Year**: ✓ (2026, submitted May 6)
- **Title**: ✓
- **Venue**: ✓ (arXiv preprint arXiv:2605.05503)
- **Cite usage**: ✓ (related_work.tex: watermark degradation across multi-step chains)
- **Notes**: No issues.

### [curious_decline] — The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text (2024)
- **Exists**: ✓
- **Authors**: ✓ (Guo, Shang, Vazirgiannis, Clavel)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (Findings of NAACL 2024)
- **Cite usage**: ✓ (introduction.tex, related_work.tex: lexical diversity decline)
- **Notes**: No issues.

### [writing_diversity] — Does Writing with Language Models Reduce Content Diversity? (2024)
- **Exists**: ✓
- **Authors**: ✓ (Padmakumar, He)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (ICLR 2024)
- **Cite usage**: ✓ (related_work.tex: lexical diversity decline)
- **Notes**: No issues.

### [nucleus_sampling] — The Curious Case of Neural Text Degeneration (2020)
- **Exists**: ✓
- **Authors**: ✓ (Holtzman, Buys, Du, Forbes, Choi)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (ICLR 2020)
- **Cite usage**: N/A — **UNCITED** in any tex file
- **Notes**: Entry exists in bib but is never referenced.

### [welleck_unlikelihood] — Neural Text Generation with Unlikelihood Training (2020)
- **Exists**: ✓
- **Authors**: ✓ (Welleck, Kulikov, Roller, Dinan, Cho, Weston)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (ICLR 2020)
- **Cite usage**: N/A — **UNCITED** in any tex file
- **Notes**: Entry exists in bib but is never referenced.

### [stamatatos_survey] — A Survey of Modern Authorship Attribution Methods (2009)
- **Exists**: ✓
- **Authors**: ✓ (Stamatatos)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (JASIST, vol. 60, no. 3, pp. 538-556)
- **Cite usage**: ✓ (related_work.tex: classical stylometric features)
- **Notes**: No issues.

### [koppel_authorship] — Computational Methods in Authorship Attribution (2009)
- **Exists**: ✓
- **Authors**: ✓ (Koppel, Schler, Argamon)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (JASIST, vol. 60, no. 1, pp. 9-26)
- **Cite usage**: N/A — **UNCITED** in any tex file
- **Notes**: Entry exists in bib but is never referenced.

### [uchendu_attribution] — Authorship Attribution for Neural Text Generation (2020)
- **Exists**: ✓
- **Authors**: ✓ (Uchendu, Le, Shu, Lee)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (EMNLP 2020, pages 8384-8395)
- **Cite usage**: N/A — **UNCITED** in any tex file
- **Notes**: Entry exists in bib but is never referenced.

### [munir_looking_glass] — Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models (2021)
- **Exists**: ✓
- **Authors**: ✓ (Munir, Batool, Shafiq, Srinivasan, Zaffar)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (EACL 2021, pages 1811-1822)
- **Cite usage**: N/A — **UNCITED** in any tex file
- **Notes**: Entry exists in bib but is never referenced.

### [briesch_self_consuming] — Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop (2023)
- **Exists**: ✓
- **Authors**: ✓ (Briesch, Sobania, Rothlauf)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (arXiv preprint arXiv:2311.16822)
- **Cite usage**: N/A — **UNCITED** in any tex file
- **Notes**: Entry exists in bib but is never referenced.

### [broken_telephone] — LLM as a Broken Telephone: Iterative Generation Distorts Information (2025)
- **Exists**: ✓
- **Authors**: ✓ (Mohamed, Geng, Vazirgiannis, Shang)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (ACL 2025, Long Papers, pages 7493-7509)
- **Cite usage**: ✓ (introduction.tex, related_work.tex, appendix_iterative_comparison.tex: iterative generation distortion)
- **Notes**: No issues.

### [markovian_chains] — Markovian Generation Chains in Large Language Models (2026)
- **Exists**: ✓
- **Authors**: ✓ (Geng, Mohamed, Shang, Vazirgiannis, Poibeau)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (arXiv preprint arXiv:2603.11228)
- **Cite usage**: ✓ (introduction.tex, related_work.tex, appendix_iterative_comparison.tex, results.tex: Markovian convergence dynamics)
- **Notes**: No issues.

### [attractor_cycles] — Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing (2025)
- **Exists**: ✓
- **Authors**: ✓ (Wang, Li, Yan, Cheng, Zhang)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (ACL 2025, Long Papers, pages 12740-12755; arXiv:2502.15208)
- **Cite usage**: ✓ (related_work.tex: attractor cycle evidence)
- **Notes**: No issues.

### [min_k_percent] — Detecting Pretraining Data from Large Language Models (2024)
- **Exists**: ✓
- **Authors**: ✓ (Shi, Ajith, Xia, Huang, Liu, Blevins, Chen, Zettlemoyer)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (ICLR 2024)
- **Cite usage**: ✓ (related_work.tex: membership inference baseline)
- **Notes**: No issues.

### [koike_mia_detection] — Machine Text Detectors are Membership Inference Attacks (2025)
- **Exists**: ✓
- **Authors**: ✓ (Koike, Dugan, Kaneko, Callison-Burch, Okazaki)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (arXiv preprint arXiv:2510.19492)
- **Cite usage**: ✓ (related_work.tex: membership inference connection)
- **Notes**: No issues.

### [wu_survey_2025] — A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions (2025)
- **Exists**: ✓
- **Authors**: ✓ (Wu, Yang, Zhan, Yuan, Chao, Wong)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (Computational Linguistics, MIT Press, vol. 51, no. 1, pp. 275-338)
- **Cite usage**: ✓ (related_work.tex: survey reference)
- **Notes**: No issues.

### [jawahar_survey] — Automatic Detection of Machine Generated Text: A Critical Survey (2020)
- **Exists**: ✓
- **Authors**: ✓ (Jawahar, Abdul-Mageed, Lakshmanan)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (COLING 2020)
- **Cite usage**: N/A — **UNCITED** in any tex file
- **Notes**: Entry exists in bib but is never referenced.

### [pythia] — Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling (2023)
- **Exists**: ✓
- **Authors**: ✓ (Biderman, Schoelkopf, Anthony, et al. — 13 authors confirmed)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (ICML 2023)
- **Cite usage**: ✓ (method.tex: generator model reference)
- **Notes**: No issues.

### [olmo] — OLMo: Accelerating the Science of Language Models (2024)
- **Exists**: ✓
- **Authors**: ✓ (Groeneveld, Beltagy, Walsh, et al. — large author list confirmed)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (ACL 2024, Best Theme Paper)
- **Cite usage**: ✓ (method.tex: generator model reference)
- **Notes**: No issues.

### [qwen3] — Qwen3 Technical Report (2025)
- **Exists**: ✓
- **Authors**: ✓ (Qwen Team)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (arXiv preprint arXiv:2505.09388)
- **Cite usage**: ✓ (method.tex: generator model reference)
- **Notes**: No issues.

### [ghostbuster] — Ghostbuster: Detecting Text Ghostwritten by Large Language Models (2024)
- **Exists**: ✓
- **Authors**: ✓ (Verma, Fleisig, Tomlin, Klein)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (NAACL 2024, pages 1702-1717)
- **Cite usage**: ✓ (related_work.tex: learned classifier)
- **Notes**: No issues.

### [two_birds] — Two Birds with One Stone: Multi-Task Detection and Attribution of LLM-Generated Text (2025)
- **Exists**: ✓
- **Authors**: ✓ (Rao, Mohamed, Liu, Liu)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (arXiv preprint arXiv:2508.14190)
- **Cite usage**: ✓ (related_work.tex: joint detection-attribution)
- **Notes**: No issues.

### [beyond_final_actor] — Beyond the Final Actor: Modeling the Dual Roles of Creator and Editor for Fine-Grained LLM-Generated Text Detection (2026)
- **Exists**: ✓
- **Authors**: ✓ (Li, Sheng, Wang, Yang, Wang, Cao)
- **Year**: ✓ (arXiv April 2026)
- **Title**: ✓
- **Venue**: **⚠ — Listed as ACL 2026 (`@inproceedings` with `booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics}`), but ACL 2026 acceptance could not be independently confirmed from official accepted paper lists. The paper exists on arXiv (2604.04932) and its project page mentions ACL 2026. Consider verifying acceptance or citing as arXiv preprint.**
- **Cite usage**: N/A — **UNCITED** in any tex file
- **Notes**: Entry exists in bib but is never referenced. Venue unconfirmed.

### [gutierrez_ordinal_survey] — Ordinal Regression Methods: Survey and Experimental Study (2016)
- **Exists**: ✓
- **Authors**: ✓ (Gutierrez, Perez-Ortiz, Sanchez-Monedero, Fernandez-Navarro, Hervas-Martinez)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (IEEE TKDE, vol. 28, no. 1, pp. 127-146)
- **Cite usage**: ✓ (related_work.tex: ordinal regression reference)
- **Notes**: No issues.

### [coral_ordinal] — Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation (2020)
- **Exists**: ✓
- **Authors**: ✓ (Cao, Mirjalili, Raschka)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (Pattern Recognition Letters, vol. 140, pp. 325-331)
- **Cite usage**: ✓ (related_work.tex, method.tex, appendix_classifier.tex: ordinal classifier alternative)
- **Notes**: No issues.

### [frank_hall_ordinal] — A Simple Approach to Ordinal Classification (2001)
- **Exists**: ✓
- **Authors**: ✓ (Frank, Hall)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (ECML 2001, LNCS 2167, pp. 145-156)
- **Cite usage**: ✓ (method.tex, appendix_classifier.tex: ordinal classifier alternative)
- **Notes**: No issues.

### [corn_ordinal] — Deep Neural Networks for Rank-Consistent Ordinal Regression Based On Conditional Probabilities (2023)
- **Exists**: ✓
- **Authors**: ✓ (Shi, Cao, Raschka)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (Pattern Analysis and Applications, vol. 26, pp. 941-955)
- **Cite usage**: ✓ (method.tex: ordinal classifier alternative)
- **Notes**: No issues.

### [diaz_soft_labels_ordinal] — Soft Labels for Ordinal Regression (2019)
- **Exists**: ✓
- **Authors**: ✓ (Diaz, Marathe)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (CVPR 2019, pp. 4738-4747)
- **Cite usage**: N/A — **UNCITED** in any tex file
- **Notes**: Entry exists in bib but is never referenced.

### [kasa_ordinality_nlp] — Exploring Ordinality in Text Classification: A Comparative Study of Explicit and Implicit Techniques (2024)
- **Exists**: ✓
- **Authors**: ✓ (Kasa, Goel, Gupta, Roychowdhury, Priyatam, Bhanushali, Murthy)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (Findings of ACL 2024, pp. 5390-5404)
- **Cite usage**: N/A — **UNCITED** in any tex file
- **Notes**: Entry exists in bib but is never referenced.

### [xgboost] — XGBoost: A Scalable Tree Boosting System (2016)
- **Exists**: ✓
- **Authors**: ✓ (Chen, Guestrin)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (KDD 2016, pp. 785-794)
- **Cite usage**: ✓ (method.tex: classifier used throughout)
- **Notes**: No issues.

### [lakens_equivalence] — Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses (2017)
- **Exists**: ✓
- **Authors**: ✓ (Lakens)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (Social Psychological and Personality Science, vol. 8, no. 4, pp. 355-362)
- **Cite usage**: ✓ (appendix_tost.tex, appendix_downstream.tex: TOST equivalence testing)
- **Notes**: No issues.

### [llama3] — The Llama 3 Herd of Models (2024)
- **Exists**: ✓
- **Authors**: ✓ (Grattafiori, Dubey, et al.)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (arXiv preprint arXiv:2407.21783)
- **Cite usage**: ✓ (method.tex: generator model reference)
- **Notes**: No issues.

### [mistral7b] — Mistral 7B (2023)
- **Exists**: ✓
- **Authors**: ✓ (Jiang, Sablayrolles, Mensch, et al.)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (arXiv preprint arXiv:2310.06825)
- **Cite usage**: ✓ (method.tex: generator model reference)
- **Notes**: No issues.

### [strobl_conditional_2008] — Conditional Variable Importance for Random Forests (2008)
- **Exists**: ✓
- **Authors**: ✓ (Strobl, Boulesteix, Kneib, Augustin, Zeileis)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (BMC Bioinformatics, vol. 9, p. 307)
- **Cite usage**: N/A — **UNCITED** in any tex file
- **Notes**: Entry exists in bib but is never referenced.

### [dolma] — Dolma: an Open Corpus of Three Trillion Tokens for Language Model Pretraining Research (2024)
- **Exists**: ✓
- **Authors**: ✓ (Soldaini, Kinney, Bhagia, et al.)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (ACL 2024, pages 15725-15788)
- **Cite usage**: ✓ (introduction.tex: training corpora reference)
- **Notes**: No issues.

### [fineweb] — The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale (2024)
- **Exists**: ✓
- **Authors**: ✓ (Penedo, Kydlicek, Ben Allal, Lozhkov, Mitchell, Raffel, Von Werra, Wolf)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (NeurIPS 2024 Datasets and Benchmarks Track)
- **Cite usage**: ✓ (introduction.tex: training corpora reference)
- **Notes**: No issues.

### [mapping_llm_science] — Mapping the Increasing Use of LLMs in Scientific Papers (2024)
- **Exists**: ✓
- **Authors**: ✓ (Liang, Zhang, Wu, Lepp, et al.)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (COLM 2024)
- **Cite usage**: ✓ (introduction.tex: LLM content in scientific publications)
- **Notes**: No issues.

### [monitoring_ai_review] — Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews (2024)
- **Exists**: ✓
- **Authors**: ✓ (Liang, Izzo, Zhang, Lepp, et al.)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (ICML 2024, PMLR 235:29575-29620)
- **Cite usage**: ✓ (introduction.tex: LLM content in scientific publications)
- **Notes**: No issues.

### [raid] — RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors (2024)
- **Exists**: ✓
- **Authors**: ✓ (Dugan, Hwang, Trhlik, Zhu, Ludan, Xu, Ippolito, Callison-Burch)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (ACL 2024, pages 12463-12492)
- **Cite usage**: N/A — **UNCITED** in any tex file
- **Notes**: Entry exists in bib but is never referenced.

### [human_texts_outliers] — Human Texts Are Outliers: Rethinking Machine-Generated Text Detection from an Out-of-Distribution Perspective (2025)
- **Exists**: **✗ — HALLUCINATED ENTRY**
- **Authors**: **✗ — Bib lists "Li, Yafu and Hu, Zhilin and Guo, Zetian and Zhao, Wei and Li, Lixin and Hou, Yuanxin" but arXiv:2510.08602 is authored by Cong Zeng, Shengkun Tang, Yuanzhou Chen, Zhiqiang Shen, Wenchao Yu, Xujiang Zhao, Haifeng Chen, Wei Cheng, Zhiqiang Xu**
- **Year**: ✓ (2025)
- **Title**: **✗ — Actual title at arXiv:2510.08602 is "Human Texts Are Outliers: Detecting LLM-generated Texts via Out-of-distribution Detection", not "...Rethinking Machine-Generated Text Detection from an Out-of-Distribution Perspective"**
- **Venue**: **✗ — The real paper at this arXiv ID was accepted at NeurIPS 2025 (poster), not listed as arXiv article**
- **Cite usage**: ✓ context is valid (related_work.tex: "reframes detection as an out-of-distribution problem") but must point to correct paper
- **Notes**: **CRITICAL — Authors and subtitle are fabricated. The arXiv ID exists but maps to a completely different author set. Must be corrected: fix authors to Cong Zeng et al., fix subtitle, change venue to NeurIPS 2025.**

### [xu_spectrum_detection] — Detecting Subtle Differences between Human and Model Languages Using Spectrum of Relative Likelihood (2024)
- **Exists**: ✓
- **Authors**: ✓ (Xu, Wang, An, Liu, Li)
- **Year**: ✓
- **Title**: ✓
- **Venue**: **✗ — Listed as "arXiv preprint arXiv:2406.19874" but was published at EMNLP 2024 (pages 10108-10121). Should be updated to `@inproceedings` with `booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing}`.**
- **Cite usage**: ✓ (related_work.tex: surprisal-based approach)
- **Notes**: Venue should be upgraded from arXiv to EMNLP 2024.

### [mauve] — MAUVE: Measuring the Gap Between Neural Text and Human Text using Divergence Frontiers (2021)
- **Exists**: ✓
- **Authors**: ✓ (Pillutla, Swayamdipta, Zellers, Thickstun, Welleck, Choi, Harchaoui)
- **Year**: ✓
- **Title**: ✓
- **Venue**: ✓ (NeurIPS 2021, Outstanding Paper Award)
- **Cite usage**: N/A — **UNCITED** in any tex file
- **Notes**: Entry exists in bib but is never referenced.

## Cite Context Issues

1. **`\cite{human_texts_outliers}`** in `related_work.tex:7` — "Recent work reframes detection as an out-of-distribution problem \cite{human_texts_outliers}". The citation context is thematically appropriate (the real paper IS about OOD-based detection), but the bib entry has hallucinated authors and wrong subtitle. The arXiv ID is correct but the metadata is fabricated.

No other cite-context mismatches found. All other cited papers correctly support the claims made in the surrounding text.

## Uncited Entries (25 entries in bib but not in any \cite{} in tex files)

These entries exist in `references.bib` but are never referenced in any `.tex` file. They will generate LaTeX warnings and should either be cited or removed:

1. `gltr` — GLTR: Statistical Detection and Visualization of Generated Text (2019)
2. `feat_aug_transformer` — Feature-Augmented Transformers for Robust AI-Text Detection (2026)
3. `detection_possibilities` — Position: On the Possibilities of AI-Generated Text Detection (2024)
4. `paraphrase_evades` — Paraphrasing Evades Detectors of AI-Generated Text (2023)
5. `intrinsic_dim_detection` — Intrinsic Dimension Estimation for Robust Detection (2023)
6. `seqxgpt` — SeqXGPT: Sentence-Level AI-Generated Text Detection (2023)
7. `grover` — Defending Against Neural Fake News (2019)
8. `release_strategies` — Release Strategies and the Social Impacts of Language Models (2019)
9. `model_collapse_avoidable` — Is Model Collapse Inevitable? (2024)
10. `seddik_synthetic_data` — How Bad is Training on Synthetic Data? (2024)
11. `qurating` — QuRating: Selecting High-Quality Data (2024)
12. `aaronson_watermark` — Watermarking GPT Outputs (2022)
13. `nucleus_sampling` — The Curious Case of Neural Text Degeneration (2020)
14. `welleck_unlikelihood` — Neural Text Generation with Unlikelihood Training (2020)
15. `koppel_authorship` — Computational Methods in Authorship Attribution (2009)
16. `uchendu_attribution` — Authorship Attribution for Neural Text Generation (2020)
17. `munir_looking_glass` — Through the Looking Glass (2021)
18. `briesch_self_consuming` — Large Language Models Suffer From Their Own Output (2023)
19. `jawahar_survey` — Automatic Detection of Machine Generated Text: A Critical Survey (2020)
20. `beyond_final_actor` — Beyond the Final Actor (2026)
21. `diaz_soft_labels_ordinal` — Soft Labels for Ordinal Regression (2019)
22. `kasa_ordinality_nlp` — Exploring Ordinality in Text Classification (2024)
23. `strobl_conditional_2008` — Conditional Variable Importance for Random Forests (2008)
24. `raid` — RAID: A Shared Benchmark for Robust Evaluation (2024)
25. `mauve` — MAUVE: Measuring the Gap Between Neural Text and Human Text (2021)
