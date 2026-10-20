# Idea Brief: Representation-Grounded Diversity Selection with Collapse-Aware Failsafe for Iterative Synthetic Training


- **Idea ID**: `idea_011`
- **Created**: 2026-05-10
- **Source**: web_research
- **Level**: top-tier
- **Target Venues**: EMNLP 2026 (ARR deadline: May 25, 2026; commitment deadline: August 2, 2026) — primary target, feasible with reduced scope, AAAI 2027 (abstract: ~July 2026; paper: ~August 2026) — fallback with expanded experiments (second model pair, third dataset)

## Seed Topic

Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Machine Learning for NLP / Resources and Evaluation. Aligns with EMNLP 2026 special theme "New Missions for NLP Research" which explicitly calls for work on data contamination, synthetic data feedback loops, and data governance.

Direction: Synthetic data quality, model collapse prevention, contamination detection. In-scope: synthetic data verification/filtering methods, detecting training data contamination in benchmarks, methods to break recursive data feedback loops, data mixing strategies that prevent quality degradation, principled synthetic data generation with quality guarantees.

Contribution type: METHOD ONLY. Must propose a concrete detection algorithm, filtering pipeline, or training recipe — not just an observation about model collapse. Method + analysis OK.

HARD CONSTRAINTS:
1. Compute: ≤200 H100-hours total. Model collapse experiments need multiple training iterations — budget for small models (1B-3B) across 3-5 generations.
2. Time: ≤16 days. Use small open models (Pythia, OLMo-1B, Qwen-0.5B/1.8B) for iterative collapse experiments.
3. Eval: perplexity degradation curves, downstream task quality (MMLU, HellaSwag), diversity metrics (self-BLEU, n-gram entropy), contamination detection accuracy.

This is a hot EMNLP 2026 special theme area with relatively few established methods — high novelty potential.

Tag: direction=data_governance, contribution_type=method. target_venues=["EMNLP 2026 Main", "EMNLP 2026 Findings"].

## Generation Journey

1. **Start** — 开始生成，seed: 'Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Machine Learning for NLP / Resources and Evaluation. Aligns with EMNLP 2026 special theme "New Missions for NLP Research" which explicitly calls for work on data contamination, synthetic data feedback loops, and data governance.\n\nDirection: Synthetic data quality, model collapse prevention, contamination detection. In-scope: synthetic data verification/filtering methods, detecting training data contamination in benchmarks, methods to break recursive data feedback loops, data mixing strategies that prevent quality degradation, principled synthetic data generation with quality guarantees.\n\nContribution type: METHOD ONLY. Must propose a concrete detection algorithm, filtering pipeline, or training recipe — not just an observation about model collapse. Method + analysis OK.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Model collapse experiments need multiple training iterations — budget for small models (1B-3B) across 3-5 generations.\n2. Time: ≤16 days. Use small open models (Pythia, OLMo-1B, Qwen-0.5B/1.8B) for iterative collapse experiments.\n3. Eval: perplexity degradation curves, downstream task quality (MMLU, HellaSwag), diversity metrics (self-BLEU, n-gram entropy), contamination detection accuracy.\n\nThis is a hot EMNLP 2026 special theme area with relatively few established methods — high novelty potential.\n\nTag: direction=data_governance, contribution_type=method. target_venues=["EMNLP 2026 Main", "EMNLP 2026 Findings"].'
2. **Problem Discovery** (325s) — 发现 4 个研究方向
   - Training-Time Early Warning Signals for Model Collapse
   - Generational Depth Fingerprinting for Synthetic Text Triage
   - Diversity-Calibrated Verification for Collapse-Resistant Synthetic Data
   - Collapse-Aware Adaptive Mixing for Synthetic-Real Training
3. **Method Synthesis** (287s) — 完成: "Training-Time Early Warning Signals for Model Collapse" [top-tier] → EMNLP 2026 (ARR submission May 25, 2026 — special theme: Data as a Bottleneck and a Responsibility), AAAI 2027 (expected deadline ~August 2026)
3. **Method Synthesis** (779s) — 完成: "Generational Depth Fingerprinting for Synthetic Text Triage" [solid] → EMNLP 2026 (ARR deadline: May 25, 2026), AAAI 2027 (paper deadline: August 2, 2026), ICLR 2027 (paper deadline: September 24, 2026), NAACL 2027 (ARR deadline: October 16, 2026), EACL 2027 (ARR deadline: October 16, 2026)
3. **Method Synthesis** (557s) — 完成: "Diversity-Calibrated Verification for Collapse-Resistant Synthetic Data" [solid] → EMNLP 2026 (ARR deadline: May 25, 2026), AACL-IJCNLP 2026 (ARR deadline: May 25, 2026), AAAI 2027 (abstract: July 25, 2026; paper: August 1, 2026)
3. **Method Synthesis** (616s) — 完成: "Collapse-Aware Adaptive Mixing for Synthetic-Real Training" [solid] → EMNLP 2026 (ARR submission deadline: May 25, 2026), AAAI 2027 (paper deadline: August 1, 2026), NeurIPS 2026 Workshops (suggested submission: August 29, 2026), ICLR 2027 (estimated deadline: September-October 2026, not yet announced)

## Core Problem

Current synthetic data filtering for iterative training either relies on quality-only criteria (self-verification, perplexity thresholds) that ignore diversity, or measures diversity in fixed external embedding spaces (cluster membership, Contriever embeddings) that cannot track how the student model's own representation space evolves across training generations. Yet representational collapse in the student is precisely the mechanism driving model collapse, as proven by the Strong Model Collapse result (ICLR 2025). Methods that do use model-internal representations for diversity-driven selection — DaaR (NeurIPS 2025) uses the LLM's own frozen embeddings with entropy-based diversity estimation, DiverseEvol uses model embeddings with Vendi Score, SAE-based approaches use sparse autoencoder features, MONA (NeurIPS 2025) uses monosemantic neuronal activations for task-specific data selection — all operate in single-phase fine-tuning and assume the representation space remains trustworthy throughout. Crucially, these methods also lack an explicit articulation of WHY model-internal diversity scoring selects better data than external embeddings: the student's representations encode which feature distinctions it currently relies on for prediction, meaning diversity in this space directly targets the features whose collapse would degrade performance, whereas external embeddings are blind to task-specific feature importance. In iterative multi-generation training, representations themselves degrade, creating a fundamental paradox: the very space used to measure diversity becomes less reliable as collapse progresses. No existing method addresses this paradox by jointly tracking representation quality and diversity across generations, nor provides a principled mechanism to detect when model-internal diversity scoring becomes unreliable.

## Opportunity / Why Now

The Strong Model Collapse paper proves collapse stems from tail distribution erosion across generations. Recent work on capability emergence dynamics (arXiv:2602.15997) shows that representation collapse is gradual, measurable via effective rank (RankMe), and precedes behavioral degradation — meaning there exists a window where model-internal representations are collapsing but still discriminative enough to be useful for diversity scoring. This creates a concrete opportunity: use model-internal diversity scoring during the window when it is most informative (early-to-mid collapse), and fall back to external embeddings when representation quality degrades past a critical threshold. The key mechanism underpinning this opportunity is that the student model's representation space encodes which feature distinctions it currently leverages for prediction — diversity in this space means 'diverse along dimensions the student actively uses,' directly targeting what the model needs to prevent collapse of its own learned features. External embeddings like Contriever capture generic semantic similarity but are blind to which features the student has learned to prioritize: a dataset that is diverse in Contriever-space may be concentrated in precisely the feature dimensions the student needs to preserve. This 'task-specific feature alignment' advantage is empirically supported by MONA (NeurIPS 2025), which demonstrates that model-internal neuronal activations capture aspects of internal computation that external embeddings systematically miss, leading to superior data selection across tasks and models. DaaR (NeurIPS 2025) further validates that model-internal embeddings are effective for diversity-driven data selection, but operates with frozen embeddings in a single training phase — it does not address the multi-generation setting where the model's own representations progressively degrade. The critical missing piece is a representation quality monitor that determines when the model's representations cross from 'degrading but useful' to 'too collapsed to trust,' enabling a principled transition to external embeddings. Additionally, 'What Matters in LLM-generated Data' (arXiv:2506.19262) demonstrates that the diversity-performance relationship is non-monotonic — combining model-internal diversity measurement with collapse-adaptive scheduling would create the first method that tracks and counteracts collapse from the student model's own perspective while avoiding excessive diversity that hurts performance.

## Landscape (SOTA & Limitations)

Self-verification (NeurIPS 2025) filters by model confidence and provably prevents collapse under accurate confidence assumptions, but ignores diversity entirely. DCES ('Countering Model Collapse via Dynamic Center-Edge Sampling', Electronics 2026) uses cluster-based sampling that preserves edge/tail samples with quality filtering and dynamic ratio adjustment — the closest prior work on iterative collapse, but relies on external k-means clustering in sentence embedding space rather than model-internal diversity scoring, and cannot detect when its own clustering space misaligns with the student's feature space. DiSF ('Combatting Dimensional Collapse via Diversified File Selection', ICLR 2025 Oral) achieves eigenvalue uniformity in feature covariance via greedy submodular selection using Contriever embeddings — our primary methodological inspiration for the selection algorithm, but uses fixed Contriever embeddings and targets pretraining dimensional collapse, not iterative model collapse across generations. Quad ('Harnessing Diversity for Important Data Selection', ICLR 2025 Poster) jointly optimizes quality and diversity via multi-armed bandits but targets pretraining data selection, not iterative synthetic training collapse. DaaR ('Diversity as a Reward', NeurIPS 2025) is the closest work to our core claim: it uses the LLM's own frozen embedding-layer representations for self-supervised diversity estimation via an MLP entropy probe, achieving SOTA across multiple benchmarks. However, DaaR operates in single-phase fine-tuning with frozen embeddings — it does not track representation quality across multiple training generations, has no failsafe mechanism for when representations degrade, and does not address iterative model collapse. DiverseEvol (arXiv:2311.08182) uses the model's own embedding space for diversity-driven iterative data selection with Vendi Score, but operates in single-iteration instruction tuning without multi-generation collapse tracking. MONA ('Task-Specific Data Selection for Instruction Tuning via Monosemantic Neuronal Activations', NeurIPS 2025) demonstrates that model-internal neuronal activations capture 'how the model internally processes samples' and outperform external embedding baselines (BGE, LLM2Vec) for task-specific data selection — directly supporting our argument that model-internal diversity scoring has a mechanistic advantage over external embeddings. However, MONA targets single-phase instruction tuning with no multi-generation tracking or failsafe. SAE-based diversity (arXiv:2502.14050) uses sparse autoencoder features from a separate model, not the student's own evolving representations. 'Anatomy of Capability Emergence' (arXiv:2602.15997) shows that representations collapse to low-dimensional states (measurable via RankMe/effective rank) before recovering, and that geometric changes precede behavioral ones — directly supporting the existence of a window where collapsing representations remain discriminative. 'Representation Collapse in Machine Translation Through the Lens of Angular Dispersion' (EACL 2026 Findings) demonstrates that representation collapse is gradual across training and measurable via angular dispersion. 'What Matters in LLM-generated Data' (arXiv:2506.19262) finds moderately diverse data enhances performance but highly diverse data hurts — challenging monotonic diversity assumptions. DCScore (ICML 2025) proposes classification-based diversity measurement with axiomatic foundations. Quality-Weighted Vendi Score (ICML 2024) provides a principled joint quality-diversity metric. No existing work (a) grounds diversity measurement in the student model's own evolving representations across multiple training generations, (b) monitors representation quality to determine when model-internal diversity scoring becomes unreliable, or (c) provides a principled failsafe from model-internal to external embeddings in the iterative collapse setting.

## Proposed Approach

We propose Representation-Grounded Diversity Selection (RGDS), a synthetic data selection pipeline that measures diversity in the student model's own evolving representation space across iterative training generations, with a principled failsafe mechanism that detects when model-internal representations become too degraded and switches to external embeddings.

**Why Model-Internal Diversity Scoring Selects Better Data.** The core mechanism is task-specific feature alignment: the student model's representation space encodes which feature distinctions it currently relies on for prediction. Diversity in this space means 'diverse along dimensions the student actively uses,' directly targeting what the model needs to prevent collapse of its own learned features. External embeddings (e.g., Contriever) capture generic semantic similarity but are blind to which features the student has learned to prioritize — a dataset that is diverse in Contriever-space may be concentrated in precisely the feature dimensions the student needs to preserve. This advantage is empirically grounded: MONA (NeurIPS 2025) demonstrates that model-internal representations outperform external embedding baselines for data selection because they reflect the model's internal computation rather than surface similarity. The advantage is strongest during early-to-mid collapse, when the student's representations are degrading but still encode meaningful task-specific structure — precisely the window RGDS exploits before falling back to external embeddings.

**Architecture Overview.** At each generation t, RGDS operates in four steps:

**(1) Representation extraction and quality assessment.** All candidate synthetic samples plus a fixed held-out reference set R (a random 5K-sample subset of the original human training data, held constant across all generations) are passed through the current student model M_{t-1}, extracting last-hidden-layer representations. We compute two representation quality metrics on R's representations: (a) effective rank via RankMe (Shannon entropy of normalized singular values of the representation matrix), and (b) k-NN probe accuracy — a 5-NN classifier on R's representations to distinguish samples containing rare n-grams (bottom 10% frequency) from common ones, measuring whether the representation space still discriminates tail from center.

**(2) Failsafe decision.** If effective rank drops below τ_rank = 50% of the generation-0 value, OR k-NN probe accuracy drops below τ_knn = 60% (near random for binary classification), RGDS switches to external embeddings (Contriever-110M) for the remaining steps. This resolves the representation degeneration paradox: RGDS uses model-internal diversity when it is most informative (early-to-mid collapse, when representations are degrading but still discriminative) and falls back to stable external representations when model-internal ones become unreliable.

**(3) Diversity-quality joint selection.** Representations are PCA-projected to d=32 dimensions, with PCA fitted on the reference set R (ensuring comparability across generations). A greedy submodular algorithm (adapted from DiSF) iteratively selects candidates that maximize covariance eigenvalue uniformity in the projected space, subject to a quality floor (samples with perplexity above the 90th percentile of R's perplexity under M_{t-1} are excluded). The selection maximizes F(S) = exp(-||C(S)||_F), where minimizing ||C||_F² directly minimizes eigenvalue variance per DiSF's Lemma 1.

**(4) Collapse-adaptive diversity scheduling.** RGDS monitors the eigenvalue uniformity ratio u_t of R's raw d_model-dimensional covariance matrix (EMA-smoothed with fixed decay α=0.3). The diversity weight λ_t follows a dead-zone controller: if ũ_t < 0.8·ũ_0, λ_t = min(λ_{t-1} · 1.5, 3.0); if ũ_t ≥ 0.9·ũ_0, λ_t = max(λ_{t-1} · 0.8, 0.5); otherwise λ_t = λ_{t-1}. Default λ_0 = 1.0. This addresses the non-monotonic diversity finding — diversity is intensified only when the model signals collapse.

**Key Empirical Contribution: Representation Quality Monitor.** Rather than relying on a theoretical argument about representation injectivity (which cannot rigorously bound distance distortion under collapse), we position the Representation Quality Monitor as a primary empirical contribution. At each generation, we plot: (a) RankMe effective rank trajectory, (b) k-NN probe accuracy trajectory, and (c) rank correlation between model-internal and Contriever-based diversity scores. These curves directly characterize the window during which model-internal diversity scoring remains valid, validate the failsafe thresholds, and constitute a reusable analysis tool for future work on iterative training. Prior work supports this approach: 'Anatomy of Capability Emergence' (arXiv:2602.15997) shows representation geometry changes precede behavioral collapse.

**Relationship to DaaR.** DaaR (NeurIPS 2025) validates the premise that model-internal embeddings are effective for diversity-driven data selection. RGDS extends this insight to the multi-generation iterative setting by: (a) tracking representation quality across generations rather than assuming frozen/stable embeddings, (b) providing a failsafe mechanism when representations degrade past usability, and (c) coupling diversity scoring with collapse-adaptive scheduling.

**Contingency Framing.** If the core hypothesis yields a negative result (RGDS ≈ RGDS-external-only), indicating that model-internal diversity scoring does not meaningfully outperform external embeddings even during the valid window, the paper's contribution shifts to three independently valuable components: (a) the Representation Quality Monitor as a reusable diagnostic tool characterizing the window during which model-internal representations remain discriminative — a novel analysis contribution regardless of whether that window proves useful for selection, (b) the collapse-adaptive scheduling mechanism, which is independent of the diversity embedding source and addresses the non-monotonic diversity finding, and (c) the empirical finding that external embeddings suffice for diversity-driven collapse prevention, which itself simplifies future system design. This contingency is acknowledged upfront; the experimental design (RGDS vs. RGDS-external-only as a core comparison) directly tests the hypothesis rather than assuming it.

**Experimental Design.** We validate RGDS on iterative training loops using Qwen3-1.7B (student) with Qwen3-4B (fixed generator) on two datasets: WikiText-103 (encyclopedic text, standard collapse benchmark with heterogeneous content expected to produce faster collapse) and PubMed abstracts (domain-specific biomedical text, ~10M-token subset, where domain coherence is expected to slow representational degradation and produce a wider model-internal window). PubMed is specifically chosen to provide at least one scenario where the model-internal window is demonstrably wide, as domain-specific corpora maintain more coherent representation structure under iterative training.

Core methods (5, run for 6 generations):
1. RGDS (full method)
2. RGDS-external-only (Contriever embeddings throughout — isolates model-grounded contribution)
3. DCES (cluster-based center-edge sampling — strongest iterative collapse baseline)
4. Self-verification (quality-only filtering — ablates diversity entirely)
5. Uncurated (no filtering)

Additional condition: A mixed-training variant where each generation trains on 70% selected synthetic data + 30% original human data, run for RGDS and RGDS-external-only only (2 additional runs per dataset). This controls the collapse rate and is expected to widen the model-internal window, providing a setting where the mechanism advantage is most clearly observable.

Ablations (reported in appendix): failsafe threshold sensitivity (τ_rank ∈ {0.3, 0.5, 0.7}, τ_knn ∈ {0.55, 0.60, 0.65}), and RGDS-no-failsafe (model-internal throughout, testing degeneration limits).

Collapse metrics:
- Rare n-gram survival rate (tail preservation)
- Quality-Weighted Vendi Score trajectory (ICML 2024)
- Downstream perplexity on held-out data
- Representation Quality Monitor curves (RankMe effective rank + k-NN probe accuracy across generations)
- Rank correlation between model-internal and Contriever diversity scores across generations (characterizing window validity)

A second model family (Pythia-1.4B/6.9B) and third dataset (OpenWebText) are noted as future work for generalizability validation.

**Hyperparameter Design.** We fix α=0.3 (EMA decay), d=32 (PCA dimensions), and quality floor at the 90th percentile as non-tuned defaults based on standard practice. Only three parameters are tuned: τ_rank, τ_knn (failsafe thresholds, validated via sensitivity analysis), and λ_0 (initial diversity weight). The dead-zone bounds (λ_min=0.5, λ_max=3.0) are reported in sensitivity analysis but not treated as tuned parameters.

## Resource Estimate

- **auto_research**: {'claude_api_cost': '$150-300 (1500-3000 turns)', 'estimated_gpu_cost': '$1190 (340h × $3.50/hr H100)', 'gpu_hours': '~340h H100 (exhaustive: all methods × 6 gens × 2 datasets, mixed-training variants, multiple threshold variants; ~30% wasted on marginal ablations)', 'gpu_utilization': 'Near-zero idle: agent pipelines generation→selection→training→evaluation continuously across 4 GPUs', 'risk_note': 'Without human pruning, agent may over-explore threshold sensitivity space; core focus should be Representation Quality Monitor analysis and RGDS vs. RGDS-external-only comparison', 'speed_bottleneck': 'Sequential dependency within each generation chain; parallelism from running different methods × datasets simultaneously', 'team': '0 (initial setup only)', 'timeline': '5-7 days with 4 H100 GPUs in parallel'}
- **human_in_loop**: {'claude_api_cost': '$60-120 (600-1200 turns: experiment pipeline coding, result visualization, paper drafting)', 'estimated_gpu_cost': '$630 (180h × $3.50/hr H100)', 'gpu_hours': '~180h H100 (core experiments: ~90h across 2 datasets + mixed variant; ablations over failsafe thresholds + no-failsafe variant: ~55h; buffer: ~35h)', 'gpu_utilization': 'Low idle (~35%): agent queues next generation as soon as selection completes', 'risk_note': 'Tight timeline for ARR May 25 deadline — prioritize core 5-method comparison, mixed-training variant, and Representation Quality Monitor analysis; defer threshold ablations to camera-ready if needed. Contingency framing ensures paper is publishable even if RGDS ≈ RGDS-external-only.', 'team': '1 researcher, ~30min/day reviewing Representation Quality Monitor curves', 'timeline': '12-15 days (experiments ~5 days with 4 GPUs; analysis + paper writing ~7-10 days)'}
- **manual**: {'estimated_gpu_cost': '$525 (150h × $3.50/hr H100)', 'gpu_hours': '~150h H100 (generation: ~10h shared; training: 5 core methods × 6 gens × 2 datasets × 0.5h = 30h; mixed-training variant: 2 methods × 6 gens × 2 datasets × 0.5h = 12h; forward passes/selection: ~25h; evaluation: ~12h; ablations: ~40h; buffer: ~21h)', 'gpu_utilization': 'Moderate idle (~50%): GPU waits during diversity scoring implementation and collapse metric analysis', 'team': '1-2 researchers', 'timeline': '12-15 days (experiments ~6 days with 4 GPUs in parallel; analysis + writing ~6-9 days)'}

## Key References

- Strong Model Collapse (ICLR 2025)
- Self-Verification Provably Prevents Model Collapse in Recursive Synthetic Training (NeurIPS 2025)
- Diversity as a Reward: Fine-Tuning LLMs on a Mixture of Domain-Undetermined Data [DaaR] (NeurIPS 2025, arXiv:2502.04380)
- Task-Specific Data Selection for Instruction Tuning via Monosemantic Neuronal Activations [MONA] (NeurIPS 2025, arXiv:2503.15573)
- Countering Model Collapse in Iterative Self-Training via Dynamic Center-Edge Sampling [DCES] (Electronics 2026)
- Combatting Dimensional Collapse via Diversified File Selection [DiSF] (ICLR 2025 Oral, arXiv:2504.20644)
- Harnessing Diversity for Important Data Selection in Pretraining LLMs [Quad] (ICLR 2025 Poster)
- Self-Evolved Diverse Data Sampling for Efficient Instruction Tuning [DiverseEvol] (arXiv:2311.08182)
- Diversity-driven Data Selection for Language Model Tuning through Sparse Autoencoder (arXiv:2502.14050)
- Anatomy of Capability Emergence: Scale-Invariant Representation Collapse and Top-Down Reorganization (arXiv:2602.15997, Feb 2026)
- Representation Collapse in Machine Translation Through the Lens of Angular Dispersion (EACL 2026 Findings, arXiv:2602.17287)
- What Matters in LLM-generated Data: Diversity and Its Effect on Model Fine-Tuning (arXiv:2506.19262)
- RankMe: Assessing Downstream Performance of Pretrained Self-Supervised Representations (ICML 2023)
- Quality-Weighted Vendi Scores and Their Application to Diverse Experimental Design (ICML 2024)
- Measuring Diversity in Synthetic Datasets [DCScore] (ICML 2025, arXiv:2502.08512)
- AI Models Collapse When Trained on Recursively Generated Data (Nature 2024)
- How to Synthesize Text Data without Model Collapse? [ToEdit] (ICML 2025)
- From Collapse to Improvement: Statistical Perspectives on Iterative Training (arXiv:2602.10531, Feb 2026)
- Better Fine-Tuning by Reducing Representational Collapse (ICLR 2021, arXiv:2008.03156)
- The Vendi Score: A Diversity Evaluation Metric for Machine Learning (arXiv:2210.02410)
- Synthetic Eggs in Many Baskets: Impact of Synthetic Data Diversity on LLM Fine-Tuning (ACL 2026 Findings)
- A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective (arXiv:2509.16499)

## Reviewer Evaluation

**Scores**:
  - clarity: **{'rationale': 'The proposal is exceptionally well-structured after 4 rounds of revision. The 4-step architecture is clearly delineated, the relationship to DaaR, DCES, and DiSF is explicitly stated, and the mechanism-of-advantage argument (task-specific feature alignment) is clearly articulated. The contingency framing and hyperparameter reduction show mature thinking. Minor weakness: the dead-zone controller specification is dense and could be simplified for the paper.', 'score': 4}**/5
  - feasibility: **{'rationale': 'Compute budget is realistic: 5 methods × 6 generations × 2 datasets × ~0.5h training = ~30h core training, plus generation, selection overhead, and ablations fits within ~150-180 H100-hours. Both Qwen3-1.7B and Qwen3-4B are confirmed available on HuggingFace. WikiText-103 and PubMed abstracts are standard. Timeline is tight but achievable with 4 parallel GPUs and a pre-existing codebase for iterative training loops. The contingency framing (paper publishable even if RGDS ≈ RGDS-external-only) significantly de-risks the project. Main risk is implementation complexity of the full pipeline in 16 days.', 'score': 4}**/5
  - impact: **{'rationale': "Directly addresses EMNLP 2026's special theme on synthetic data feedback loops and data governance. The Representation Quality Monitor as a reusable diagnostic tool has standalone value regardless of the main result. The failsafe mechanism addresses a real gap: practitioners need to know when model-internal metrics become unreliable during iterative training. The field is active (DCES, DaaR, DiSF, self-verification all from 2025-2026) and this paper positions itself distinctly. Impact is 'solid contribution' rather than 'paradigm-shifting.'", 'score': 4}**/5
  - novelty: **{'rationale': "The combination of model-internal diversity scoring across multiple training generations with a principled failsafe mechanism is genuinely novel. DaaR (NeurIPS 2025) validates model-internal diversity for single-phase fine-tuning; DCES uses external clustering; DiSF uses Contriever. No prior work addresses the 'representation degeneration paradox' — using a collapsing model's own representations for diversity scoring while monitoring when to fall back. The Representation Quality Monitor (RankMe + k-NN probe across generations) is a novel diagnostic contribution. However, the core pipeline (PCA + submodular selection + quality floor) is standard, and the novelty is primarily in the multi-generation monitoring/failsafe framing rather than the selection algorithm itself.", 'score': 4}**/5

## Human Review Note

## Agent 审核结果（完整三阶段 pipeline）

**Verdict**: PASS

**入口三重共识 (X)**: 25.0%
**终审自评 (Y)**: 36.0%
**出口三重共识 (Z)**: 31.0%
**Z 区间**: [27.0%, 36.0%]
**真实提升 (Z-X)**: +6.0 pp
**幻觉幅度 (Y-Z)**: +5.0 pp
**出口一致性**: 高
**出口三次评估**: [30.0, 33.0, 32.0]

### 优化方案 / 拒绝详情
Now I have the full original proposal and the complete iteration history. Let me produce the Role C final output.

【优化方案】

1. **标题** — 从原始方法导向标题 "Representation-Grounded Diversity Selection with Collapse-Aware Failsafe for Iterative Synthetic Training" 改为研究问题导向 "When Do Model-Internal Representations Help Prevent Iterative Collapse? Representation-Grounded Diversity Selection with Adaptive Reliability Monitoring"。以问句形式点明核心科学问题，使论文在任何实验结果下都构成贡献 — 命中 **Novelty / Significance**

2. **核心定位重构（全文框架性改动，最关键的单一改动）** — 原始 proposal 定位为"提出 RGDS 方法论"（method paper），优化为"回答 model-internal representations 在 iterative collapse 中何时有效/何时失效"（empirical study paper）。原始的核心问题是 "model-internal 是否优于 external"（binary yes/no），改为 "Under what conditions does model-internal diversity guidance remain reliable, and when does it fail?"（条件分析框架）。引入 **"window of advantage"** 概念——live representations 在早期代优于 frozen/external 但后期反转的生成窗口，这个窗口的存在和长度是核心 empirical question — 命中 **Novelty / Technical Soundness**

3. **术语修正与概念操作化** — 原始 "representation degeneration paradox" 改为 "self-referential quality degradation"。理由：(a) 与 Gao et al. (2019) 的 representation degeneration 术语冲突；(b) 并非严格的逻辑 paradox 而是 feedback loop；(c) 新术语更精确地描述了核心问题。增加 semi-formal 操作化定义：self-referential quality degradation 发生在 quality metric Q(M_g)（如 effective rank）在模型 M_g 被迭代训练于 Q(M_g) 所选数据时单调递减 — 命中 **Novelty / Soundness**

4. **反 tautology 论证（Introduction 新增核心段落）** — 原始 proposal 未预判审稿人的"这不是显然的吗？如果模型 collapse 了表征当然也 collapse"质疑。优化后在 Motivation 中增加显式论证：(a) representation degradation 的时间线与 model collapse 时间线可能不同步（先/后/同步都有可能），(b) 不同 representation layer/projection 对 collapse 的敏感度不同，(c) "window of advantage" 的存在和长度是 empirically non-obvious 的问题。这段论证堵住了最可能的根本性质疑 — 命中 **Technical Soundness**

5. **删除 Dual-Outcome Hedge（原始 proposal 中最大的红旗）** — 原始明确写了 "If the core hypothesis (model-internal > external) yields negative results, the paper's contribution shifts to the Monitor as a diagnostic tool, the collapse-adaptive scheduling mechanism, and the finding t



## MVP Validation Results

- **Date**: 2026-05-13
- **Hypothesis Supported**: Yes

### Key Metrics

RGDS ratio: 1.04→0.52 (Gen 0→7) | External ratio: >1.0 all 8 gens (1.095 at Gen 7) | RGDS PPL: 75.07 vs uncurated 50.28 (+49%) | RGDS rare n-gram: 0.0051 vs uncurated 0.0090 (-43%) | External PPL: 45.51 (-9.5% vs uncurated) | External rare n-gram: 0.0099 (+10% vs uncurated)

### Summary

Embedding Alignment Gap 假说全面验证通过。Phase 2 三方法对比实验（GPT2-125M, WikiText-103, 8代 self-iterate）证实：(1) RGDS 内部嵌入 diversity selection 加速崩塌（PPL +49%, rare n-gram -43% vs uncurated），selection ratio 从 1.04 下降至 0.52；(2) 冻结外部嵌入（Contriever）全 8 代 ratio >1.0，PPL -9.5%, rare n-gram +10% vs uncurated；(3) 训练设计经独立审计确认为 cumulative fine-tuning（M_t→M_{t+1}），排除 checkpoint-reset 伪影。seed=123 复现进行中（Gen 5/7），早期数据与 seed=42 一致。Dream full review 评估：Best 3.0 Findings conditional, Median 3.0 borderline, Worst 2.0 reject。

### Recommendation

GO — 进入研究阶段。核心现象真实且效应量大（Cohen's d >3），方向正确。需完成：多 seed 统计检验、GPT2-medium 跨规模验证、OpenWebText 跨数据集、re-anchoring 缓解实验、related work 扩充至 25+ 篇。目标 EMNLP 2026 ARR Findings（DDL 5/25，12天）。
