# Reference Audit — Worker 2

## Summary
- Total entries: 74
- Actually cited in tex: 48
- Orphaned (in bib but not cited): 25
- Verified OK: 70
- Issues found: 4

## Critical Issues

### 1. [human_texts_outliers] — WRONG AUTHORS, WRONG TITLE, WRONG VENUE
The bib entry attributes arXiv:2510.08602 to **Li, Yafu** et al. with subtitle "Rethinking Machine-Generated Text Detection from an Out-of-Distribution Perspective" as an arXiv preprint. The actual paper at that arXiv ID is:
- **Correct authors**: Zeng, Cong and Tang, Shengkun and Chen, Yuanzhou and Shen, Zhiqiang and Yu, Wenchao and Zhao, Xujiang and Chen, Haifeng and Cheng, Wei and Xu, Zhiqiang
- **Correct title**: "Human Texts Are Outliers: Detecting LLM-generated Texts via Out-of-distribution Detection"
- **Correct venue**: NeurIPS 2025 (not just arXiv preprint)
- **Cite usage**: The citation context in related_work.tex ("Recent work reframes detection as an out-of-distribution problem") IS accurate for the real paper, but the bib metadata is wrong.

### 2. [xu_spectrum_detection] — VENUE OUTDATED
- **Bib says**: `@article`, `journal = {arXiv preprint arXiv:2406.19874}`, year 2024
- **Should be**: `@inproceedings`, `booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing}`, year 2024, pages 10108--10121 (ACL Anthology: 2024.emnlp-main.564)

### 3. [two_birds] — VENUE POSSIBLY OUTDATED
- **Bib says**: `@article`, `journal = {arXiv preprint arXiv:2508.14190}`, year 2025
- **Possible update**: arXiv comments reportedly mention SecureComm 2025 acceptance. Verify and update if confirmed.

### 4. [wu_survey_2025] — MISSING VOLUME/PAGES
- **Bib says**: `@article`, `journal = {Computational Linguistics}`, publisher MIT Press, year 2025
- **Should add**: `volume = {51}`, `number = {1}`, `pages = {275--338}` (published journal article with known volume/pages)

---

## Entry-by-Entry Results

### [cohen1988statistical] — Statistical Power Analysis for the Behavioral Sciences (1988)
- **Exists**: ✓
- **Authors**: ✓ Cohen, Jacob
- **Year**: ✓ 1988
- **Title**: ✓
- **Venue**: ✓ Lawrence Erlbaum Associates, 2nd edition
- **Cite usage**: ✓ Used in appendix_tost.tex for SESOI definition
- **Notes**: Classic reference, no issues.

### [detectgpt] — DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature (2023)
- **Exists**: ✓
- **Authors**: ✓ Mitchell, Lee, Khazatsky, Manning, Finn
- **Year**: ✓ 2023
- **Title**: ✓
- **Venue**: ✓ ICML 2023
- **Cite usage**: ✓ Zero-shot detection baseline in intro/related work
- **Notes**: No issues.

### [gltr] — GLTR: Statistical Detection and Visualization of Generated Text (2019)
- **Exists**: ✓
- **Authors**: ✓ Gehrmann, Strobelt, Rush
- **Year**: ✓ 2019
- **Title**: ✓
- **Venue**: ✓ ACL 2019 System Demonstrations
- **Cite usage**: ✗ NOT CITED in any tex file — orphaned
- **Notes**: Orphaned entry.

### [dna_gpt] — DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text (2024)
- **Exists**: ✓
- **Authors**: ✓ Yang, Cheng, Wu, Petzold, Wang, Chen
- **Year**: ✓ 2024
- **Title**: ✓
- **Venue**: ✓ ICLR 2024
- **Cite usage**: ✓ Zero-shot scoring in related work
- **Notes**: No issues.

### [binoculars] — Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text (2024)
- **Exists**: ✓
- **Authors**: ✓ Hans, Schwarzschild, Cherepanova, Kazemi, Saha, Goldblum, Geiping, Goldstein
- **Year**: ✓ 2024
- **Title**: ✓
- **Venue**: ✓ ICML 2024
- **Cite usage**: ✓ Baseline detector
- **Notes**: No issues.

### [fast_detectgpt] — Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature (2024)
- **Exists**: ✓
- **Authors**: ✓ Bao, Zhao, Teng, Yang, Zhang
- **Year**: ✓ 2024
- **Title**: ✓
- **Venue**: ✓ ICLR 2024
- **Cite usage**: ✓ Baseline detector
- **Notes**: No issues.

### [ld_score] — Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection (2026)
- **Exists**: ✓
- **Authors**: ✓ Narayanasamy, Agrawal, Faber, Alam
- **Year**: ✓ 2026
- **Title**: ✓
- **Venue**: ✓ arXiv:2605.01647
- **Cite usage**: ✓ Baseline detector
- **Notes**: Very recent preprint, no peer-reviewed venue yet.

### [diveye] — Diversity Boosts AI-Generated Text Detection (2026)
- **Exists**: ✓
- **Authors**: ✓ Basani, Advik Raj and Chen, Pin-Yu
- **Year**: ✓ 2026
- **Title**: ✓
- **Venue**: ✓ ICLR 2026 (confirmed via OpenReview: DNgsOhGZBI)
- **Cite usage**: ✓ Surprisal-based approach in related work
- **Notes**: No issues.

### [feat_aug_transformer] — Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators (2026)
- **Exists**: ✓
- **Authors**: ✓ Mady, Reschke, Schuller
- **Year**: ✓ 2026
- **Title**: ✓
- **Venue**: ✓ arXiv:2605.03969
- **Cite usage**: ✗ NOT CITED in any tex file — orphaned
- **Notes**: Orphaned entry.

### [reliable_detection] — Can AI-Generated Text be Reliably Detected? (2025)
- **Exists**: ✓
- **Authors**: ✓ Sadasivan, Kumar, Balasubramanian, Wang, Feizi
- **Year**: ✓ 2025
- **Title**: ✓
- **Venue**: ✓ TMLR 2025
- **Cite usage**: ✓ Learned classifier in related work
- **Notes**: No issues.

### [paraphrase_evades] — Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense (2023)
- **Exists**: ✓
- **Authors**: ✓ Krishna, Song, Karpinska, Wieting, Iyyer
- **Year**: ✓ 2023
- **Title**: ✓
- **Venue**: ✓ NeurIPS 2023
- **Cite usage**: ✗ NOT CITED in any tex file — orphaned
- **Notes**: Orphaned entry.

### [detection_possibilities] — Position: On the Possibilities of AI-Generated Text Detection (2024)
- **Exists**: ✓
- **Authors**: ✓ Chakraborty, Bedi, Zhu, An, Manocha, Huang
- **Year**: ✓ 2024
- **Title**: ✓
- **Venue**: ✓ ICML 2024
- **Cite usage**: ✗ NOT CITED in any tex file — orphaned
- **Notes**: Orphaned entry.

### [intrinsic_dim_detection] — Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts (2023)
- **Exists**: ✓
- **Authors**: ✓ Tulchinskii, Kuznetsov, Kushnareva, Cherniavskii, Nikolenko, Burnaev, Barannikov, Piontkovskaya
- **Year**: ✓ 2023
- **Title**: ✓
- **Venue**: ✓ NeurIPS 2023
- **Cite usage**: ✗ NOT CITED in any tex file — orphaned
- **Notes**: Orphaned entry.

### [seqxgpt] — SeqXGPT: Sentence-Level AI-Generated Text Detection (2023)
- **Exists**: ✓
- **Authors**: ✓ Wang, Li, Ren, Jiang, Zhang, Qiu
- **Year**: ✓ 2023
- **Title**: ✓
- **Venue**: ✓ EMNLP 2023
- **Cite usage**: ✗ NOT CITED in any tex file — orphaned
- **Notes**: Orphaned entry.

### [grover] — Defending Against Neural Fake News (2019)
- **Exists**: ✓
- **Authors**: ✓ Zellers, Holtzman, Rashkin, Bisk, Farhadi, Roesner, Choi
- **Year**: ✓ 2019
- **Title**: ✓
- **Venue**: ✓ NeurIPS 2019
- **Cite usage**: ✗ NOT CITED in any tex file — orphaned
- **Notes**: Orphaned entry.

### [release_strategies] — Release Strategies and the Social Impacts of Language Models (2019)
- **Exists**: ✓
- **Authors**: ✓ Solaiman, Brundage, Clark, et al.
- **Year**: ✓ 2019
- **Title**: ✓
- **Venue**: ✓ arXiv:1908.09203
- **Cite usage**: ✗ NOT CITED in any tex file — orphaned
- **Notes**: Orphaned entry.

### [beyond_binary] — Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement (2025)
- **Exists**: ✓
- **Authors**: ✓ Cheng, Zhou, Jiang, Wang, Li
- **Year**: ✓ 2025
- **Title**: ✓
- **Venue**: ✓ ACM Web Conference 2025
- **Cite usage**: ✓ Collaboration roles in related work
- **Notes**: No issues.

### [semeval2024_task8] — SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection (2024)
- **Exists**: ✓
- **Authors**: ✓ Wang, Mansurov, Ivanov, et al.
- **Year**: ✓ 2024
- **Title**: ✓
- **Venue**: ✓ SemEval 2024
- **Cite usage**: ✓ Multi-generator attribution in related work
- **Notes**: No issues.

### [self_consuming_mad] — Self-Consuming Generative Models Go MAD (2024)
- **Exists**: ✓
- **Authors**: ✓ Alemohammad, Casco-Rodriguez, Luzi, Humayun, Babaei, LeJeune, Siahkoohi, Baraniuk
- **Year**: ✓ 2024
- **Title**: ✓
- **Venue**: ✓ ICLR 2024
- **Cite usage**: ✓ Model collapse in related work
- **Notes**: No issues.

### [curse_of_recursion] — AI models collapse when trained on recursively generated data (2024)
- **Exists**: ✓
- **Authors**: ✓ Shumailov, Shumaylov, Zhao, Papernot, Anderson, Gal
- **Year**: ✓ 2024
- **Title**: ✓
- **Venue**: ✓ Nature vol 631, pp 755-759
- **Cite usage**: ✓ Model collapse throughout paper
- **Notes**: No issues.

### [dohmatob_tale_of_tails] — A Tale of Tails: Model Collapse as a Change of Scaling Laws (2024)
- **Exists**: ✓
- **Authors**: ✓ Dohmatob, Feng, Yang, Charton, Kempe
- **Year**: ✓ 2024
- **Title**: ✓
- **Venue**: ✓ ICML 2024
- **Cite usage**: ✓ Model collapse in related work
- **Notes**: No issues.

### [strong_model_collapse] — Strong Model Collapse (2025)
- **Exists**: ✓
- **Authors**: ✓ Dohmatob, Feng, Subramonian, Kempe
- **Year**: ✓ 2025
- **Title**: ✓
- **Venue**: ✓ ICLR 2025
- **Cite usage**: ✓ Model collapse in intro/related work/discussion
- **Notes**: No issues.

### [model_collapse_avoidable] — Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data (2024)
- **Exists**: ✓
- **Authors**: ✓ Gerstgrasser, Schaeffer, Dey, et al.
- **Year**: ✓ 2024
- **Title**: ✓
- **Venue**: ✓ COLM 2024
- **Cite usage**: ✗ NOT CITED in any tex file — orphaned
- **Notes**: Orphaned entry.

### [schaeffer_collapse_position] — Position: Model Collapse Does Not Mean What You Think (2025)
- **Exists**: ✓
- **Authors**: ✓ Schaeffer, Kazdan, Arulandu, Koyejo
- **Year**: ✓ 2025
- **Title**: ✓
- **Venue**: ✓ arXiv:2503.03150
- **Cite usage**: ✓ Model collapse in related work
- **Notes**: No issues.

### [seddik_synthetic_data] — How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse (2024)
- **Exists**: ✓
- **Authors**: ✓ Seddik, Chen, Hayou, Youssef, Debbah
- **Year**: ✓ 2024
- **Title**: ✓
- **Venue**: ✓ COLM 2024
- **Cite usage**: ✗ NOT CITED in any tex file — orphaned
- **Notes**: Orphaned entry.

### [qlora] — QLoRA: Efficient Finetuning of Quantized LLMs (2023)
- **Exists**: ✓
- **Authors**: ✓ Dettmers, Pagnoni, Holtzman, Zettlemoyer
- **Year**: ✓ 2023
- **Title**: ✓
- **Venue**: ✓ NeurIPS 2023
- **Cite usage**: ✓ QLoRA classifier in intro/method/appendix
- **Notes**: No issues.

### [dsir] — Data Selection for Language Models via Importance Resampling (2023)
- **Exists**: ✓
- **Authors**: ✓ Xie, Santurkar, Ma, Liang
- **Year**: ✓ 2023
- **Title**: ✓
- **Venue**: ✓ NeurIPS 2023
- **Cite usage**: ✓ Data curation in intro/related work
- **Notes**: No issues.

### [qurating] — QuRating: Selecting High-Quality Data for Training Language Models (2024)
- **Exists**: ✓
- **Authors**: ✓ Wettig, Gupta, Malik, Chen
- **Year**: ✓ 2024
- **Title**: ✓
- **Venue**: ✓ ICML 2024
- **Cite usage**: ✗ NOT CITED in any tex file — orphaned
- **Notes**: Orphaned entry.

### [ccnet] — CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data (2020)
- **Exists**: ✓
- **Authors**: ✓ Wenzek, Lachaux, Conneau, Chaudhary, Guzmán, Joulin, Grave
- **Year**: ✓ 2020
- **Title**: ✓
- **Venue**: ✓ LREC 2020
- **Cite usage**: ✓ Data curation in intro/related work
- **Notes**: No issues.

### [watermark_llm] — A Watermark for Large Language Models (2023)
- **Exists**: ✓
- **Authors**: ✓ Kirchenbauer, Geiping, Wen, Katz, Miers, Goldstein
- **Year**: ✓ 2023
- **Title**: ✓
- **Venue**: ✓ ICML 2023
- **Cite usage**: ✓ Watermarking in related work
- **Notes**: No issues.

### [synthid_text] — Scalable Watermarking for Identifying Large Language Model Outputs (2024)
- **Exists**: ✓
- **Authors**: ✓ Dathathri, See, Ghaisas, et al.
- **Year**: ✓ 2024
- **Title**: ✓
- **Venue**: ✓ Nature vol 634, pp 818-823
- **Cite usage**: ✓ Watermarking in related work
- **Notes**: No issues.

### [aaronson_watermark] — Watermarking GPT Outputs (2022)
- **Exists**: ✓
- **Authors**: ✓ Aaronson, Kirchner
- **Year**: ✓ 2022
- **Title**: ✓ (conventional cite title for blog post)
- **Venue**: ✓ Blog post, URL valid
- **Cite usage**: ✗ NOT CITED in any tex file — orphaned
- **Notes**: Orphaned entry.

### [chainwash] — Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks (2026)
- **Exists**: ✓
- **Authors**: ✓ Ameen, Islam, Mahmud, Hamid
- **Year**: ✓ 2026
- **Title**: ✓
- **Venue**: ✓ arXiv:2605.05503
- **Cite usage**: ✓ Watermark degradation in related work
- **Notes**: Very recent preprint.

### [curious_decline] — The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text (2024)
- **Exists**: ✓
- **Authors**: ✓ Guo, Shang, Vazirgiannis, Clavel
- **Year**: ✓ 2024
- **Title**: ✓
- **Venue**: ✓ Findings of NAACL 2024
- **Cite usage**: ✓ Distributional compression in intro/related work
- **Notes**: No issues.

### [writing_diversity] — Does Writing with Language Models Reduce Content Diversity? (2024)
- **Exists**: ✓
- **Authors**: ✓ Padmakumar, He
- **Year**: ✓ 2024
- **Title**: ✓
- **Venue**: ✓ ICLR 2024
- **Cite usage**: ✓ Declining diversity in related work
- **Notes**: No issues.

### [nucleus_sampling] — The Curious Case of Neural Text Degeneration (2020)
- **Exists**: ✓
- **Authors**: ✓ Holtzman, Buys, Du, Forbes, Choi
- **Year**: ✓ 2020
- **Title**: ✓
- **Venue**: ✓ ICLR 2020
- **Cite usage**: ✗ NOT CITED in any tex file — orphaned
- **Notes**: Orphaned entry.

### [welleck_unlikelihood] — Neural Text Generation with Unlikelihood Training (2020)
- **Exists**: ✓
- **Authors**: ✓ Welleck, Kulikov, Roller, Dinan, Cho, Weston
- **Year**: ✓ 2020
- **Title**: ✓
- **Venue**: ✓ ICLR 2020
- **Cite usage**: ✗ NOT CITED in any tex file — orphaned
- **Notes**: Orphaned entry.

### [stamatatos_survey] — A Survey of Modern Authorship Attribution Methods (2009)
- **Exists**: ✓
- **Authors**: ✓ Stamatatos, Efstathios
- **Year**: ✓ 2009
- **Title**: ✓
- **Venue**: ✓ JASIST vol 60, no 3, pp 538-556
- **Cite usage**: ✓ Stylometric features in related work
- **Notes**: No issues.

### [koppel_authorship] — Computational Methods in Authorship Attribution (2009)
- **Exists**: ✓
- **Authors**: ✓ Koppel, Schler, Argamon
- **Year**: ✓ 2009
- **Title**: ✓
- **Venue**: ✓ JASIST vol 60, no 1, pp 9-26
- **Cite usage**: ✗ NOT CITED in any tex file — orphaned
- **Notes**: Orphaned entry.

### [uchendu_attribution] — Authorship Attribution for Neural Text Generation (2020)
- **Exists**: ✓
- **Authors**: ✓ Uchendu, Le, Shu, Lee
- **Year**: ✓ 2020
- **Title**: ✓
- **Venue**: ✓ EMNLP 2020
- **Cite usage**: ✗ NOT CITED in any tex file — orphaned
- **Notes**: Orphaned entry.

### [munir_looking_glass] — Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models (2021)
- **Exists**: ✓
- **Authors**: ✓ Munir, Batool, Shafiq, Srinivasan, Zaffar
- **Year**: ✓ 2021
- **Title**: ✓
- **Venue**: ✓ EACL 2021
- **Cite usage**: ✗ NOT CITED in any tex file — orphaned
- **Notes**: Orphaned entry.

### [briesch_self_consuming] — Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop (2023)
- **Exists**: ✓
- **Authors**: ✓ Briesch, Sobania, Rothlauf
- **Year**: ✓ 2023
- **Title**: ✓
- **Venue**: ✓ arXiv:2311.16822
- **Cite usage**: ✗ NOT CITED in any tex file — orphaned
- **Notes**: Orphaned entry.

### [broken_telephone] — LLM as a Broken Telephone: Iterative Generation Distorts Information (2025)
- **Exists**: ✓
- **Authors**: ✓ Mohamed, Geng, Vazirgiannis, Shang
- **Year**: ✓ 2025
- **Title**: ✓
- **Venue**: ✓ ACL 2025
- **Cite usage**: ✓ Iterative generation in intro/related work/appendix
- **Notes**: No issues.

### [markovian_chains] — Markovian Generation Chains in Large Language Models (2026)
- **Exists**: ✓
- **Authors**: ✓ Geng, Mohamed, Shang, Vazirgiannis, Poibeau
- **Year**: ✓ 2026
- **Title**: ✓
- **Venue**: ✓ arXiv:2603.11228
- **Cite usage**: ✓ Convergence dynamics throughout paper
- **Notes**: No issues.

### [attractor_cycles] — Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing (2025)
- **Exists**: ✓
- **Authors**: ✓ Wang, Li, Yan, Cheng, Zhang
- **Year**: ✓ 2025
- **Title**: ✓
- **Venue**: ✓ ACL 2025, arXiv:2502.15208
- **Cite usage**: ✓ Attractor cycles in related work
- **Notes**: No issues.

### [min_k_percent] — Detecting Pretraining Data from Large Language Models (2024)
- **Exists**: ✓
- **Authors**: ✓ Shi, Ajith, Xia, Huang, Liu, Blevins, Chen, Zettlemoyer
- **Year**: ✓ 2024
- **Title**: ✓
- **Venue**: ✓ ICLR 2024
- **Cite usage**: ✓ Membership inference in related work
- **Notes**: No issues.

### [koike_mia_detection] — Machine Text Detectors are Membership Inference Attacks (2025)
- **Exists**: ✓
- **Authors**: ✓ Koike, Dugan, Kaneko, Callison-Burch, Okazaki
- **Year**: ✓ 2025
- **Title**: ✓
- **Venue**: ✓ arXiv:2510.19492
- **Cite usage**: ✓ Membership inference in related work
- **Notes**: No issues.

### [wu_survey_2025] — A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions (2025)
- **Exists**: ✓
- **Authors**: ✓ Wu, Yang, Zhan, Yuan, Chao, Wong
- **Year**: ✓ 2025
- **Title**: ✓
- **Venue**: ✓ Computational Linguistics (MIT Press)
- **Cite usage**: ✓ Survey reference in related work
- **Notes**: ⚠️ Missing volume=51, number=1, pages=275--338 for completeness.

### [jawahar_survey] — Automatic Detection of Machine Generated Text: A Critical Survey (2020)
- **Exists**: ✓
- **Authors**: ✓ Jawahar, Abdul-Mageed, Lakshmanan
- **Year**: ✓ 2020
- **Title**: ✓
- **Venue**: ✓ COLING 2020
- **Cite usage**: ✗ NOT CITED in any tex file — orphaned
- **Notes**: Orphaned entry.

### [pythia] — Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling (2023)
- **Exists**: ✓
- **Authors**: ✓ Biderman, Schoelkopf, et al.
- **Year**: ✓ 2023
- **Title**: ✓
- **Venue**: ✓ ICML 2023
- **Cite usage**: ✓ Generator model in method
- **Notes**: No issues.

### [olmo] — OLMo: Accelerating the Science of Language Models (2024)
- **Exists**: ✓
- **Authors**: ✓ Groeneveld, Beltagy, et al.
- **Year**: ✓ 2024
- **Title**: ✓
- **Venue**: ✓ ACL 2024
- **Cite usage**: ✓ Generator model in method
- **Notes**: No issues.

### [qwen3] — Qwen3 Technical Report (2025)
- **Exists**: ✓
- **Authors**: ✓ Qwen Team
- **Year**: ✓ 2025
- **Title**: ✓
- **Venue**: ✓ arXiv:2505.09388
- **Cite usage**: ✓ Generator model in method
- **Notes**: No issues.

### [llama3] — The Llama 3 Herd of Models (2024)
- **Exists**: ✓
- **Authors**: ✓ Grattafiori, Dubey, et al.
- **Year**: ✓ 2024
- **Title**: ✓
- **Venue**: ✓ arXiv:2407.21783
- **Cite usage**: ✓ Generator model in method
- **Notes**: No issues.

### [mistral7b] — Mistral 7B (2023)
- **Exists**: ✓
- **Authors**: ✓ Jiang, Sablayrolles, et al.
- **Year**: ✓ 2023
- **Title**: ✓
- **Venue**: ✓ arXiv:2310.06825
- **Cite usage**: ✓ Generator model in method
- **Notes**: No issues.

### [ghostbuster] — Ghostbuster: Detecting Text Ghostwritten by Large Language Models (2024)
- **Exists**: ✓
- **Authors**: ✓ Verma, Fleisig, Tomlin, Klein
- **Year**: ✓ 2024
- **Title**: ✓
- **Venue**: ✓ NAACL 2024
- **Cite usage**: ✓ Learned classifier in related work
- **Notes**: No issues.

### [two_birds] — Two Birds with One Stone: Multi-Task Detection and Attribution of LLM-Generated Text (2025)
- **Exists**: ✓
- **Authors**: ✓ Rao, Mohamed, Liu, Liu
- **Year**: ✓ 2025
- **Title**: ✓
- **Venue**: ⚠️ Bib says arXiv preprint; may have been accepted at SecureComm 2025 (per arXiv comments)
- **Cite usage**: ✓ Joint detection-attribution in related work
- **Notes**: Verify SecureComm 2025 acceptance and update if confirmed.

### [beyond_final_actor] — Beyond the Final Actor: Modeling the Dual Roles of Creator and Editor for Fine-Grained LLM-Generated Text Detection (2026)
- **Exists**: ✓
- **Authors**: ✓ Li, Sheng, Wang, Yang, Wang, Cao
- **Year**: ✓ 2026
- **Title**: ✓
- **Venue**: ✓ ACL 2026 (Oral)
- **Cite usage**: ✗ NOT CITED in any tex file — orphaned
- **Notes**: Orphaned entry.

### [gutierrez_ordinal_survey] — Ordinal Regression Methods: Survey and Experimental Study (2016)
- **Exists**: ✓
- **Authors**: ✓ Gutiérrez, Pérez-Ortiz, Sánchez-Monedero, Fernández-Navarro, Hervás-Martínez
- **Year**: ✓ 2016
- **Title**: ✓
- **Venue**: ✓ IEEE TKDE vol 28, no 1, pp 127-146
- **Cite usage**: ✓ Ordinal classification in related work
- **Notes**: No issues.

### [coral_ordinal] — Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation (2020)
- **Exists**: ✓
- **Authors**: ✓ Cao, Mirjalili, Raschka
- **Year**: ✓ 2020
- **Title**: ✓
- **Venue**: ✓ Pattern Recognition Letters vol 140, pp 325-331
- **Cite usage**: ✓ Ordinal classifier in method/related work/appendix
- **Notes**: No issues.

### [frank_hall_ordinal] — A Simple Approach to Ordinal Classification (2001)
- **Exists**: ✓
- **Authors**: ✓ Frank, Hall
- **Year**: ✓ 2001
- **Title**: ✓
- **Venue**: ✓ ECML 2001
- **Cite usage**: ✓ Ordinal classifier in method/appendix
- **Notes**: No issues.

### [corn_ordinal] — Deep Neural Networks for Rank-Consistent Ordinal Regression Based On Conditional Probabilities (2023)
- **Exists**: ✓
- **Authors**: ✓ Shi, Cao, Raschka
- **Year**: ✓ 2023
- **Title**: ✓
- **Venue**: ✓ Pattern Analysis and Applications vol 26, pp 941-955
- **Cite usage**: ✓ Ordinal classifier in method
- **Notes**: No issues.

### [diaz_soft_labels_ordinal] — Soft Labels for Ordinal Regression (2019)
- **Exists**: ✓
- **Authors**: ✓ Diaz, Marathe
- **Year**: ✓ 2019
- **Title**: ✓
- **Venue**: ✓ CVPR 2019
- **Cite usage**: ✗ NOT CITED in any tex file — orphaned
- **Notes**: Orphaned entry.

### [kasa_ordinality_nlp] — Exploring Ordinality in Text Classification: A Comparative Study of Explicit and Implicit Techniques (2024)
- **Exists**: ✓
- **Authors**: ✓ Kasa, Goel, Gupta, Roychowdhury, Priyatam, Bhanushali, Murthy
- **Year**: ✓ 2024
- **Title**: ✓
- **Venue**: ✓ Findings of ACL 2024
- **Cite usage**: ✗ NOT CITED in any tex file — orphaned
- **Notes**: Orphaned entry.

### [xgboost] — XGBoost: A Scalable Tree Boosting System (2016)
- **Exists**: ✓
- **Authors**: ✓ Chen, Guestrin
- **Year**: ✓ 2016
- **Title**: ✓
- **Venue**: ✓ KDD 2016
- **Cite usage**: ✓ Classifier in method
- **Notes**: No issues.

### [lakens_equivalence] — Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses (2017)
- **Exists**: ✓
- **Authors**: ✓ Lakens, Daniël
- **Year**: ✓ 2017
- **Title**: ✓
- **Venue**: ✓ Social Psychological and Personality Science vol 8, no 4, pp 355-362
- **Cite usage**: ✓ TOST in appendix
- **Notes**: No issues.

### [strobl_conditional_2008] — Conditional Variable Importance for Random Forests (2008)
- **Exists**: ✓
- **Authors**: ✓ Strobl, Boulesteix, Kneib, Augustin, Zeileis
- **Year**: ✓ 2008
- **Title**: ✓
- **Venue**: ✓ BMC Bioinformatics vol 9, pp 307
- **Cite usage**: ✗ NOT CITED in any tex file — orphaned
- **Notes**: Orphaned entry.

### [dolma] — Dolma: an Open Corpus of Three Trillion Tokens for Language Model Pretraining Research (2024)
- **Exists**: ✓
- **Authors**: ✓ Soldaini, Kinney, et al.
- **Year**: ✓ 2024
- **Title**: ✓
- **Venue**: ✓ ACL 2024
- **Cite usage**: ✓ Training corpora in intro
- **Notes**: No issues.

### [fineweb] — The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale (2024)
- **Exists**: ✓
- **Authors**: ✓ Penedo, Kydlíček, Ben Allal, Lozhkov, Mitchell, Raffel, Von Werra, Wolf
- **Year**: ✓ 2024
- **Title**: ✓
- **Venue**: ✓ NeurIPS 2024 Datasets and Benchmarks Track
- **Cite usage**: ✓ Training corpora in intro
- **Notes**: No issues.

### [mapping_llm_science] — Mapping the Increasing Use of LLMs in Scientific Papers (2024)
- **Exists**: ✓
- **Authors**: ✓ Liang, Zhang, Wu, et al.
- **Year**: ✓ 2024
- **Title**: ✓
- **Venue**: ✓ COLM 2024
- **Cite usage**: ✓ LLM content statistics in intro
- **Notes**: No issues.

### [monitoring_ai_review] — Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews (2024)
- **Exists**: ✓
- **Authors**: ✓ Liang, Izzo, Zhang, et al.
- **Year**: ✓ 2024
- **Title**: ✓
- **Venue**: ✓ ICML 2024
- **Cite usage**: ✓ LLM content statistics in intro
- **Notes**: No issues.

### [raid] — RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors (2024)
- **Exists**: ✓
- **Authors**: ✓ Dugan, Hwang, Trhlík, Zhu, Ludan, Xu, Ippolito, Callison-Burch
- **Year**: ✓ 2024
- **Title**: ✓
- **Venue**: ✓ ACL 2024, pp 12463-12492
- **Cite usage**: ✗ NOT CITED in any tex file — orphaned
- **Notes**: Orphaned entry.

### [human_texts_outliers] — Human Texts Are Outliers (2025)
- **Exists**: ✓ (but metadata is WRONG — see Critical Issues above)
- **Authors**: ✗ WRONG — bib has Li, Yafu et al.; actual is Zeng, Cong et al.
- **Year**: ✓ 2025
- **Title**: ✗ WRONG subtitle — bib has "Rethinking..."; actual is "Detecting LLM-generated Texts via..."
- **Venue**: ✗ OUTDATED — bib says arXiv; actual is NeurIPS 2025
- **Cite usage**: ✓ OOD detection in related work (claim is accurate for the real paper)
- **Notes**: See Critical Issues #1. All three metadata fields need correction.

### [xu_spectrum_detection] — Detecting Subtle Differences between Human and Model Languages Using Spectrum of Relative Likelihood (2024)
- **Exists**: ✓
- **Authors**: ✓ Xu, Wang, An, Liu, Li
- **Year**: ✓ 2024
- **Title**: ✓
- **Venue**: ✗ OUTDATED — bib says arXiv; published at EMNLP 2024 (ACL Anthology: 2024.emnlp-main.564)
- **Cite usage**: ✓ Spectral detection in related work
- **Notes**: See Critical Issues #2. Update venue to EMNLP 2024.

### [mauve] — MAUVE: Measuring the Gap Between Neural Text and Human Text using Divergence Frontiers (2021)
- **Exists**: ✓
- **Authors**: ✓ Pillutla, Swayamdipta, Zellers, Thickstun, Welleck, Choi, Harchaoui
- **Year**: ✓ 2021
- **Title**: ✓
- **Venue**: ✓ NeurIPS 2021 (Outstanding Paper Award)
- **Cite usage**: ✗ NOT CITED in any tex file — orphaned
- **Notes**: Orphaned entry.

---

## Cite Context Issues

All 48 actively cited references were checked against their usage context in the tex files. The claims made in the paper text are supported by the cited papers, with one caveat:

1. **[human_texts_outliers]** — The citation context ("Recent work reframes detection as an out-of-distribution problem") accurately describes what the REAL paper (Zeng et al., NeurIPS 2025) does, but the bib entry attributes the paper to the wrong authors (Li, Yafu et al.) with the wrong subtitle. The cite usage itself is valid; only the bib metadata needs correction.

No other cite-context mismatches were found.

---

## Orphaned Entries (25 total — in bib but not cited in any tex file)

1. gltr
2. feat_aug_transformer
3. paraphrase_evades
4. detection_possibilities
5. intrinsic_dim_detection
6. seqxgpt
7. grover
8. release_strategies
9. model_collapse_avoidable
10. seddik_synthetic_data
11. qurating
12. aaronson_watermark
13. nucleus_sampling
14. welleck_unlikelihood
15. koppel_authorship
16. uchendu_attribution
17. munir_looking_glass
18. briesch_self_consuming
19. jawahar_survey
20. beyond_final_actor
21. diaz_soft_labels_ordinal
22. kasa_ordinality_nlp
23. strobl_conditional_2008
24. raid
25. mauve

These entries won't appear in the compiled bibliography (BibTeX only includes cited entries), but they add clutter to the bib file and could be cleaned up.
