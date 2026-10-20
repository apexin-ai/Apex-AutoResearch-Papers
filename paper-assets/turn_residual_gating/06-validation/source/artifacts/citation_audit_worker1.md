# Citation Audit Report — Worker 1

## Summary
- Total bib entries: 58
- Cited in paper: 46
- Uncited (in bib only): 12
- Verified OK: 41
- Issues found: 5 (3 critical, 2 minor)
- Potentially hallucinated: 0

## Critical Issues

| # | Bib Key | Issue |
|---|---------|-------|
| 1 | `laban2025lost` | Published at **ICLR 2026 (Oral, Best Paper)**, but cited as arXiv 2025 preprint. Must upgrade venue, year, and entry type. |
| 2 | `raposo2024mixture` | Venue is **ICLR 2025**, NOT ICML 2024. Year should be 2025. |
| 3 | `he2019exposure` | Published at **EMNLP 2021** with new title "Exposure Bias versus Self-Recovery: Are Distortions Really Incremental for Autoregressive Text Generation?". Currently cites old arXiv 2019 title/year. |

## Other Issues

| # | Bib Key | Severity | Issue |
|---|---------|----------|-------|
| 4 | `brunner2020identifiability` | Medium | Last author "Andreas Krause" is **wrong** — should be "Roger Wattenhofer" (both ETH Zurich, likely confusion). Entry is uncited so low practical impact. |
| 5 | `bachlechner2021rezero` | Minor | Author names should be "Huanru Henry Mao" (not "Henry Mao") and "Garrison W. Cottrell" (not "Gary Cottrell") per official UAI proceedings. |

## Uncited Bib Entries (12)

These entries exist in `references.bib` but are not `\cite`d anywhere in the paper:

| Bib Key | Paper |
|---------|-------|
| `hsieh2024found` | Found in the Middle (Findings ACL 2024) |
| `luo2025flexidepth` | Adaptive Layer-skipping (COLM 2025) |
| `navon2022nash` | Multi-Task Learning as Bargaining Game (ICML 2022) |
| `vaswani2017attention` | Attention Is All You Need (NeurIPS 2017) |
| `he2016deep` | Deep Residual Learning (CVPR 2016) |
| `vig2019multiscale` | Multiscale Visualization of Attention (ACL 2019 Demo) |
| `abnar2020quantifying` | Quantifying Attention Flow (ACL 2020) |
| `ethayarajh2019contextual` | How Contextual are Contextualized Word Representations (EMNLP 2019) |
| `brunner2020identifiability` | On Identifiability in Transformers (ICLR 2020) |
| `zhou2020drophead` | Scheduled DropHead (Findings EMNLP 2020) |
| `dauphin2017language` | Language Modeling with Gated CNNs (ICML 2017) |
| `shazeer2020glu` | GLU Variants Improve Transformer (arXiv 2020) |

## Per-Citation Checklist

### [dongre2026attention] Dongre et al. (2026) — When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction
- Exists: ✓
- Authors: ✓ (Vardhan Dongre, Joseph Hsieh, Viet Dac Lai, Seunghyun Yoon, Trung Bui, Dilek Hakkani-Tür)
- Year: ✓ (2026)
- Title: ✓
- Venue: ✓ (arXiv preprint arXiv:2605.12922)
- arXiv→published upgrade needed: No (very recent, May 2026)
- Context usage correct: ✓ — Paper claims "measured significant GAR decline across 12 models" and "residual probes retain goal information (AUC=0.98)". Consistent with the paper's contributions.
- Notes: Clean.

### [hong2025rhea] Hong et al. (2025) — Rhea: Role-aware Heuristic Episodic Attention for Conversational LLMs
- Exists: ✓
- Authors: ✓
- Year: ✓ (2025)
- Title: ✓
- Venue: ✓ (arXiv preprint arXiv:2512.06869)
- arXiv→published upgrade needed: No
- Context usage correct: ✓ — Cited as an "inference-time remedy" alongside li2024measuring. Rhea proposes episodic attention for conversational LLMs, consistent with this characterization.
- Notes: Clean.

### [laban2025lost] Laban et al. (2025) — LLMs Get Lost In Multi-Turn Conversation
- Exists: ✓
- Authors: ✓ (Philippe Laban, Hiroaki Hayashi, Yingbo Zhou, Jennifer Neville)
- Year: ✗ — Should be **2026** (ICLR 2026)
- Title: ✓
- Venue: ✗ — Cited as arXiv 2025 preprint, but **published at ICLR 2026 as Oral / Best Paper**
- arXiv→published upgrade needed: **YES** — Must upgrade to `@inproceedings{laban2026lost, booktitle={ICLR}, year={2026}}`
- Context usage correct: ✓ — Cited for "quality gaps at later turns" in multi-turn dialogue.
- Notes: **CRITICAL.** Citing an ICLR Best Paper as arXiv preprint is a reviewer red flag.

### [liu2026intent] Liu et al. (2026) — Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation
- Exists: ✓
- Authors: ✓ (Geng Liu, Fei Zhu, Rong Feng, Changyi Ma, Shiqi Wang, Gaofeng Meng)
- Year: ✓ (2026)
- Title: ✓ (matches arXiv version)
- Venue: ✓ (arXiv preprint arXiv:2602.07338)
- arXiv→published upgrade needed: Possibly — An OpenReview submission for ICLR 2026 exists (id=3x94uVDCeq) possibly under a different title ("Explicating the Implicit: Bridging the Intent Alignment Gap in Multi-Turn Conversation"). Needs investigation.
- Context usage correct: ✓ — Cited for quality gaps at later turns.
- Notes: Investigate ICLR 2026 acceptance status and possible title change.

### [bai2024mtbench101] Bai et al. (2024) — MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogues
- Exists: ✓
- Authors: ✓
- Year: ✓ (2024)
- Title: ✓
- Venue: ✓ (ACL 2024, confirmed on ACL Anthology 2024.acl-long.401)
- arXiv→published upgrade needed: No
- Context usage correct: ✓ — Cited as a multi-turn benchmark.
- Notes: Clean.

### [fan2020layerdrop] Fan et al. (2020) — Reducing Transformer Depth on Demand with Structured Dropout (LayerDrop)
- Exists: ✓
- Authors: ✓ (Angela Fan, Edouard Grave, Armand Joulin)
- Year: ✓ (2020)
- Title: ✓
- Venue: ✓ (ICLR 2020)
- arXiv→published upgrade needed: No
- Context usage correct: ✓ — Cited for "layer pruning" alongside gromov2024unreasonable.
- Notes: Clean.

### [raposo2024mixture] Raposo et al. (2024) — Mixture-of-Depths: Dynamically Allocating Compute in Transformer-Based Language Models
- Exists: ✓
- Authors: ✓ (David Raposo, Sam Ritter, Blake Richards, Timothy Lillicrap, Peter Conway Humphreys, Adam Santoro)
- Year: ✗ — Should be **2025** (published at ICLR 2025, not ICML 2024)
- Title: ✓
- Venue: ✗ — Bib says "International Conference on Machine Learning" (ICML 2024), but actually published at **ICLR 2025**
- arXiv→published upgrade needed: N/A (venue/year correction needed)
- Context usage correct: ✓ — Cited for "adaptive depth" alongside schuster2022calm.
- Notes: **CRITICAL.** Wrong venue (ICML→ICLR) and wrong year (2024→2025).

### [schuster2022calm] Schuster et al. (2022) — Confident Adaptive Language Modeling
- Exists: ✓
- Authors: ✓
- Year: ✓ (2022)
- Title: ✓
- Venue: ✓ (NeurIPS 2022)
- arXiv→published upgrade needed: No
- Context usage correct: ✓ — Cited for "adaptive depth".
- Notes: Clean.

### [qiu2025gated] Qiu et al. (2025) — Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free
- Exists: ✓
- Authors: ✓
- Year: ✓ (NeurIPS 2025)
- Title: ✓
- Venue: ✓ (NeurIPS 2025, Oral, Best Paper Award)
- arXiv→published upgrade needed: No
- Context usage correct: ✓ — Cited for "per-head sigmoid gates achieving MMLU +2.03 at 15B scale". Consistent with the paper's findings.
- Notes: Clean.

### [xiao2024streaming] Xiao et al. (2024) — Efficient Streaming Language Models with Attention Sinks
- Exists: ✓
- Authors: ✓
- Year: ✓ (2024)
- Title: ✓
- Venue: ✓ (ICLR 2024)
- arXiv→published upgrade needed: No
- Context usage correct: ✓ — Cited for "retains anchor tokens" (StreamingLLM). Accurate description.
- Notes: Clean.

### [zhang2024tell] Zhang et al. (2024) — Tell Your Model Where to Attend: Post-hoc Attention Steering for LLMs
- Exists: ✓
- Authors: ✓
- Year: ✓ (2024)
- Title: ✓
- Venue: ✓ (ICLR 2024)
- arXiv→published upgrade needed: No
- Context usage correct: ✓ — Cited as "PASTA" for attention steering. Accurate.
- Notes: Clean.

### [bengio2015scheduled] Bengio et al. (2015) — Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks
- Exists: ✓
- Authors: ✓ (Samy Bengio, Oriol Vinyals, Navdeep Jaitly, Noam Shazeer)
- Year: ✓ (2015)
- Title: ✓
- Venue: ✓ (NeurIPS 2015)
- arXiv→published upgrade needed: No
- Context usage correct: ✓ — Cited for "curriculum-based mixing" and exposure bias. Foundational scheduled sampling paper.
- Notes: Clean.

### [ranzato2016sequence] Ranzato et al. (2016) — Sequence Level Training with Recurrent Neural Networks
- Exists: ✓
- Authors: ✓
- Year: ✓ (2016)
- Title: ✓
- Venue: ✓ (ICLR 2016)
- arXiv→published upgrade needed: No
- Context usage correct: ✓ — Cited for "sequence-level objectives".
- Notes: Clean.

### [lamb2016professor] Lamb et al. (2016) — Professor Forcing: A New Algorithm for Training Recurrent Networks
- Exists: ✓
- Authors: ✓ (Alex Lamb, Anirudh Goyal, Ying Zhang, Saizheng Zhang, Aaron Courville, Yoshua Bengio)
- Year: ✓ (2016)
- Title: ✓
- Venue: ✓ (NeurIPS 2016)
- arXiv→published upgrade needed: No
- Context usage correct: ✓ — Cited for "adversarial regularization" to address exposure bias. Accurate.
- Notes: Clean.

### [leblond2018searnn] Leblond et al. (2018) — SEARNN: Training RNNs with Global-Local Losses
- Exists: ✓
- Authors: ✓
- Year: ✓ (2018)
- Title: ✓
- Venue: ✓ (ICLR 2018)
- arXiv→published upgrade needed: No
- Context usage correct: ✓ — Cited for "search-based training".
- Notes: Clean.

### [he2019exposure] He et al. (2019) — Quantifying Exposure Bias for Neural Language Generation
- Exists: ✓ (but outdated citation)
- Authors: ✓ (Tianxing He, Jingzhao Zhang, Zhiming Zhou, James Glass)
- Year: ✗ — Should be **2021** (published at EMNLP 2021)
- Title: ✗ — Published title is **"Exposure Bias versus Self-Recovery: Are Distortions Really Incremental for Autoregressive Text Generation?"**
- Venue: ✗ — Should be **EMNLP 2021**, not arXiv 2019
- arXiv→published upgrade needed: **YES** — Must update title, year, venue. ACL Anthology: 2021.emnlp-main.415
- Context usage correct: ✓ — Cited for "self-recovery analysis" which aligns with the published title about self-recovery.
- Notes: **CRITICAL.** Title, year, and venue all need correction. The paper evolved significantly from 2019 preprint to 2021 publication.

### [wiseman2016sequence] Wiseman & Rush (2016) — Sequence-to-Sequence Learning as Beam-Search Optimization
- Exists: ✓
- Authors: ✓
- Year: ✓ (2016)
- Title: ✓
- Venue: ✓ (EMNLP 2016)
- arXiv→published upgrade needed: No
- Context usage correct: ✓ — Cited for training-inference distributional mismatch context.
- Notes: Clean.

### [arora2022exposure] Arora et al. (2022) — Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation
- Exists: ✓
- Authors: ✓
- Year: ✓ (2022)
- Title: ✓
- Venue: ✓ (Findings of ACL 2022)
- arXiv→published upgrade needed: No
- Context usage correct: ✓ — Cited for exposure bias and error accumulation.
- Notes: Clean.

### [li2024measuring] Li et al. (2024) — Measuring and Controlling Instruction (In)Stability in Language Model Dialogs
- Exists: ✓
- Authors: ✓
- Year: ✓ (2024)
- Title: ✓
- Venue: ✓ (COLM 2024)
- arXiv→published upgrade needed: No
- Context usage correct: ✓ — Cited for "independently quantified instruction instability and proposed split-softmax".
- Notes: Clean.

### [yu2020pcgrad] Yu et al. (2020) — Gradient Surgery for Multi-Task Learning
- Exists: ✓
- Authors: ✓
- Year: ✓ (2020)
- Title: ✓
- Venue: ✓ (NeurIPS 2020)
- arXiv→published upgrade needed: No
- Context usage correct: ✓ — Cited for "projects conflicting gradients onto the other's normal plane". Accurate description of PCGrad.
- Notes: Clean.

### [chen2018gradnorm] Chen et al. (2018) — GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks
- Exists: ✓
- Authors: ✓
- Year: ✓ (2018)
- Title: ✓
- Venue: ✓ (ICML 2018)
- arXiv→published upgrade needed: No
- Context usage correct: ✓ — Cited alongside discussion of gradient magnitude imbalance.
- Notes: Clean.

### [liu2021cagrad] Liu et al. (2021) — Conflict-Averse Gradient Descent for Multi-task Learning
- Exists: ✓
- Authors: ✓
- Year: ✓ (2021)
- Title: ✓
- Venue: ✓ (NeurIPS 2021)
- arXiv→published upgrade needed: No
- Context usage correct: ✓ — Cited for "treat gradient conflict as the root cause".
- Notes: Clean.

### [bachlechner2021rezero] Bachlechner et al. (2021) — ReZero is All You Need: Fast Convergence at Large Depth
- Exists: ✓
- Authors: ✗ — "Mao, Henry" should be **"Mao, Huanru Henry"**; "Cottrell, Gary" should be **"Cottrell, Garrison W."** per UAI proceedings (PMLR v161)
- Year: ✓ (2021)
- Title: ✓
- Venue: ✓ (UAI 2021)
- arXiv→published upgrade needed: No
- Context usage correct: ✓ — Cited for "initializes a single trainable scalar at zero to stabilize deep network training". Exact description of ReZero.
- Notes: Minor author name corrections needed.

### [grattafiori2024llama3] Grattafiori et al. (2024) — The Llama 3 Herd of Models
- Exists: ✓
- Authors: ✓ (Aaron Grattafiori first author in latest arXiv version v3)
- Year: ✓ (2024)
- Title: ✓
- Venue: ✓ (arXiv preprint, no peer-reviewed venue)
- arXiv→published upgrade needed: No (industry report, no conference publication)
- Context usage correct: ✓ — Cited for Llama-3.1-8B-Instruct model.
- Notes: Clean.

### [gromov2024unreasonable] Gromov et al. (2025) — The Unreasonable Ineffectiveness of the Deeper Layers
- Exists: ✓
- Authors: ✓
- Year: ✓ (bib says 2025, correct for ICLR 2025; bib key uses 2024 arXiv year, cosmetic only)
- Title: ✓
- Venue: ✓ (ICLR 2025)
- arXiv→published upgrade needed: No
- Context usage correct: ✓ — Cited for "early layers capture local syntax while later layers integrate long-range context" and "layer pruning". Consistent with the paper's findings about deeper layers being removable.
- Notes: Clean.

### [srivastava2015highway] Srivastava et al. (2015) — Highway Networks
- Exists: ✓
- Authors: ✓
- Year: ✓ (2015)
- Title: ✓
- Venue: ✓ (ICML 2015 Deep Learning Workshop)
- arXiv→published upgrade needed: No (workshop citation is standard practice; full paper "Training Very Deep Networks" exists at NeurIPS 2015 but under different title)
- Context usage correct: ✓ — Cited for "highway networks" in gating context.
- Notes: Clean.

### [hu2022lora] Hu et al. (2022) — LoRA: Low-Rank Adaptation of Large Language Models
- Exists: ✓
- Authors: ✓
- Year: ✓ (2022)
- Title: ✓
- Venue: ✓ (ICLR 2022)
- arXiv→published upgrade needed: No
- Context usage correct: ✓ — Cited for LoRA fine-tuning method.
- Notes: Clean.

### [zhang2020dialogpt] Zhang et al. (2020) — DialoGPT: Large-Scale Generative Pre-training for Conversational Response Generation
- Exists: ✓
- Authors: ✓
- Year: ✓ (2020)
- Title: ✓
- Venue: ✓ (ACL 2020 System Demonstrations)
- arXiv→published upgrade needed: No
- Context usage correct: ✓ — Cited for early dialogue systems.
- Notes: Clean.

### [roller2021recipes] Roller et al. (2021) — Recipes for Building an Open-Domain Chatbot
- Exists: ✓
- Authors: ✓
- Year: ✓ (2021)
- Title: ✓
- Venue: ✓ (EACL 2021)
- arXiv→published upgrade needed: No
- Context usage correct: ✓ — Cited for early dialogue systems.
- Notes: Clean.

### [zheng2024judging] Zheng et al. (2023) — Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena
- Exists: ✓
- Authors: ✓
- Year: ✓ (year field says 2023, correct for NeurIPS 2023)
- Title: ✓
- Venue: ✓ (NeurIPS 2023, Datasets and Benchmarks Track)
- arXiv→published upgrade needed: No
- Context usage correct: ✓ — Cited for "MT-Bench" benchmark.
- Notes: Bib key `zheng2024judging` uses 2024 but year field is 2023. Cosmetic key inconsistency only; no impact on rendered output.

### [clark2019what] Clark et al. (2019) — What Does BERT Look At? An Analysis of BERT's Attention
- Exists: ✓
- Authors: ✓
- Year: ✓ (2019)
- Title: ✓
- Venue: ✓ (ACL 2019 BlackboxNLP Workshop)
- arXiv→published upgrade needed: No
- Context usage correct: ✓ — Cited for "head specialization" analysis.
- Notes: Clean.

### [voita2019analyzing] Voita et al. (2019) — Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned
- Exists: ✓
- Authors: ✓
- Year: ✓ (2019)
- Title: ✓
- Venue: ✓ (ACL 2019)
- arXiv→published upgrade needed: No
- Context usage correct: ✓ — Cited for "head specialization" analysis.
- Notes: Clean.

### [kovaleva2019revealing] Kovaleva et al. (2019) — Revealing the Dark Secrets of BERT
- Exists: ✓
- Authors: ✓
- Year: ✓ (2019)
- Title: ✓
- Venue: ✓ (EMNLP 2019)
- arXiv→published upgrade needed: No
- Context usage correct: ✓ — Cited for attention analysis/head specialization.
- Notes: Clean.

### [liu2024lost] Liu et al. (2024) — Lost in the Middle: How Language Models Use Long Contexts
- Exists: ✓
- Authors: ✓
- Year: ✓ (2024)
- Title: ✓
- Venue: ✓ (TACL 2024, volume 12, pp 157-173)
- arXiv→published upgrade needed: No
- Context usage correct: ✓ — Cited for "positional bias calibration".
- Notes: Clean.

### [zhang2019bridging] Zhang et al. (2019) — Bridging the Gap between Training and Inference for Neural Machine Translation
- Exists: ✓
- Authors: ✓
- Year: ✓ (2019)
- Title: ✓
- Venue: ✓ (ACL 2019)
- arXiv→published upgrade needed: No
- Context usage correct: ✓ — Cited for "bridging strategies for NMT" in exposure bias context.
- Notes: Clean.

### [mihaylova2019scheduled] Mihaylova & Martins (2019) — Scheduled Sampling for Transformers
- Exists: ✓
- Authors: ✓
- Year: ✓ (2019)
- Title: ✓
- Venue: ✓ (ACL 2019 Student Research Workshop, pp 351-356)
- arXiv→published upgrade needed: No
- Context usage correct: ✓ — Cited for "extended scheduled sampling to transformers for single-turn NMT". Accurate.
- Notes: Clean.

### [dou2019attention] Dou et al. (2019) — Attention Forcing for Sequence-to-sequence Model Training
- Exists: ✓
- Authors: ✓ (Qingyun Dou, Yiting Lu, Joshua Efiong, Mark J. F. Gales)
- Year: ✓ (2019)
- Title: ✓
- Venue: ✓ (arXiv preprint; ICLR 2020 submission was not accepted)
- arXiv→published upgrade needed: No (remains unpublished)
- Context usage correct: ✓ — Cited for "proposed attention forcing (supervising cross-attention during NMT)". Accurate description.
- Notes: Clean.

### [dou2022parallel] Dou & Gales (2022) — Parallel Attention Forcing for Machine Translation
- Exists: ✓
- Authors: ✓
- Year: ✓ (2022)
- Title: ✓
- Venue: ✓ (arXiv preprint; no peer-reviewed venue found)
- arXiv→published upgrade needed: No
- Context usage correct: ✓ — Cited for "extended [attention forcing] with KL-divergence switching". Consistent with the paper.
- Notes: Clean.

### [li2016persona] Li et al. (2016) — A Persona-Based Neural Conversation Model
- Exists: ✓
- Authors: ✓ (minor: "Georgios Spithourakis" missing middle initial "P." per ACL Anthology)
- Year: ✓ (2016)
- Title: ✓
- Venue: ✓ (ACL 2016, pp 994-1003)
- arXiv→published upgrade needed: No
- Context usage correct: ✓ — Cited for early dialogue systems.
- Notes: Very minor — "Georgios Spithourakis" could be "Georgios P. Spithourakis".

### [xu2022goldfish] Xu et al. (2022) — Beyond Goldfish Memory: Long-Term Open-Domain Conversation
- Exists: ✓
- Authors: ✓
- Year: ✓ (2022)
- Title: ✓
- Venue: ✓ (ACL 2022, pp 5180-5197)
- arXiv→published upgrade needed: No
- Context usage correct: ✓ — Cited for "modern long-context models" in dialogue.
- Notes: Clean.

### [veit2016residual] Veit et al. (2016) — Residual Networks Behave Like Ensembles of Relatively Shallow Networks
- Exists: ✓
- Authors: ✓
- Year: ✓ (2016)
- Title: ✓
- Venue: ✓ (NeurIPS 2016)
- arXiv→published upgrade needed: No
- Context usage correct: ✓ — Cited for "residual networks can be viewed as ensembles of shallow paths". Exact main thesis.
- Notes: Clean.

### [dong2021attention] Dong et al. (2021) — Attention is Not All You Need: Pure Attention Loses Rank Doubly Exponentially with Depth
- Exists: ✓
- Authors: ✓
- Year: ✓ (2021)
- Title: ✓
- Venue: ✓ (ICML 2021, pp 2793-2803)
- arXiv→published upgrade needed: No
- Context usage correct: ✓ — Cited for "attention collapse in deep transformers". Accurate.
- Notes: Clean.

### [lin2022truthfulqa] Lin et al. (2022) — TruthfulQA: Measuring How Models Mimic Human Falsehoods
- Exists: ✓
- Authors: ✓
- Year: ✓ (2022)
- Title: ✓
- Venue: ✓ (ACL 2022, pp 3214-3252)
- arXiv→published upgrade needed: No
- Context usage correct: ✓ — Cited as an evaluation benchmark in Limitations section.
- Notes: Clean.

### [hendrycks2021measuring] Hendrycks et al. (2021) — Measuring Massive Multitask Language Understanding
- Exists: ✓
- Authors: ✓
- Year: ✓ (2021)
- Title: ✓
- Venue: ✓ (ICLR 2021)
- arXiv→published upgrade needed: No
- Context usage correct: ✓ — Cited for "MMLU 5-shot" benchmark. Accurate.
- Notes: Clean.

### [dettmers2023qlora] Dettmers et al. (2023) — QLoRA: Efficient Finetuning of Quantized LLMs
- Exists: ✓
- Authors: ✓
- Year: ✓ (2023)
- Title: ✓
- Venue: ✓ (NeurIPS 2023)
- arXiv→published upgrade needed: No
- Context usage correct: ✓ — Cited alongside LoRA for fine-tuning setup.
- Notes: Clean.

### [ding2023ultrachat] Ding et al. (2023) — Enhancing Chat Language Models by Scaling High-quality Instructional Conversations
- Exists: ✓
- Authors: ✓
- Year: ✓ (2023)
- Title: ✓
- Venue: ✓ (EMNLP 2023)
- arXiv→published upgrade needed: No
- Context usage correct: ✓ — Cited for UltraChat dataset used in all experiments.
- Notes: Clean.

---

## Uncited Entries Detail (for completeness)

### [hsieh2024found] — Verified ✓, Findings ACL 2024, all fields correct. Not cited.
### [luo2025flexidepth] — Verified ✓, COLM 2025, all fields correct. Not cited.
### [navon2022nash] — Verified ✓, ICML 2022, all fields correct. Not cited.
### [vaswani2017attention] — Verified ✓, NeurIPS 2017, all fields correct. Not cited.
### [he2016deep] — Verified ✓, CVPR 2016, all fields correct. Not cited.
### [vig2019multiscale] — Verified ✓, ACL 2019 Demo, all fields correct. Not cited.
### [abnar2020quantifying] — Verified ✓, ACL 2020, all fields correct. Not cited.
### [ethayarajh2019contextual] — Verified ✓, EMNLP 2019, all fields correct. Not cited.
### [brunner2020identifiability] — **Author error**: "Andreas Krause" should be "Roger Wattenhofer". Not cited.
### [zhou2020drophead] — Verified ✓, Findings EMNLP 2020, all fields correct. Not cited.
### [dauphin2017language] — Verified ✓, ICML 2017, all fields correct. Not cited.
### [shazeer2020glu] — Verified ✓, arXiv preprint (never published), all fields correct. Not cited.
