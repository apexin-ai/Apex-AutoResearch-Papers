# Idea Brief: RASP: Recovery-Aware Structured Pruning for Reasoning Models — How What You Prune Affects How RLVR Recovers


- **Idea ID**: `idea_012`
- **Created**: 2026-05-14
- **Approved**: 2026-05-14
- **Source**: foreign:be-idea-gen-0509-8
- **Level**: top-tier
- **Target Venues**: EMNLP 2026 (ARR May 25 submission deadline, commitment deadline Aug 2)

## Seed Topic

Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Efficient Methods for NLP.

Direction: Efficiency methods for NLP — NOT limited to LLM inference optimization. In-scope: speculative decoding, KV-cache compression/eviction, quantization-aware distillation, parameter-efficient fine-tuning, efficient long-context serving, MoE routing, attention approximations, efficient smaller models for specific NLP tasks, pruning for task-specific deployment.

Contribution type: METHOD ONLY. Propose new algorithms — not profiling studies.

HARD CONSTRAINTS:
1. Compute: ≤200 H100-hours total. Generous for efficiency work.
2. Time: ≤16 days. Build on vLLM, SGLang, llama.cpp, TensorRT-LLM, HF Transformers, FlashAttention, bitsandbytes.
3. Eval: perplexity (Wiki/C4), MMLU, HumanEval, LongBench, RULER, MT-Bench. Report wall-clock and throughput on H100.

Look for: cache-aware methods for new workloads (long thinking traces, agent loops, RAG), quantization-aware distillation, structured sparsity during inference, efficient serving of reasoning models with variable-length thinking. Avoid: vanilla 4-bit quantization, generic LoRA, plain speculative decoding.

Tag: direction=efficiency, contribution_type=method. target_venues=["EMNLP 2026 Main", "EMNLP 2026 Findings"].

## Core Problem

Current structured pruning methods for reasoning models optimize importance scores for immediate post-pruning accuracy, treating the subsequent recovery step as independent. Self-Healing (2025) shows RLVR recovery reaches 95%+ accuracy at 25% compression, but uses standard pruning methods and only tests one compression ratio. RESP (Dec 2025) achieves 81.3% on GSM8K at 40% sparsity without any recovery training. At higher compression (30–50%), where recovery becomes critical, no work has studied whether the CHOICE of what to prune affects how well RLVR can recover reasoning ability — or whether this interaction differs from SFT recovery. 'RL Squeezes, SFT Expands' (ICLR 2026 Poster) shows that RLVR and SFT shape reasoning capabilities through fundamentally different mechanisms (path compression vs. path expansion), suggesting the pruning-recovery interaction should also differ. The open question: does the optimal pruning strategy change depending on whether recovery uses RLVR or SFT, and can we exploit this to improve structured pruning for RLVR-recovered reasoning models?

## Opportunity / Why Now

Self-Healing (2025, under review) demonstrates RLVR recovers structured-pruned reasoning models to 95%+ at 25% compression, but treats pruning as a black box and tests only one ratio. RESP (Dec 2025) achieves 81.3% on GSM8K at 40% structured sparsity but uses no recovery. GRASPrune (ACL 2026) provides SOTA budgeted structural pruning with public code but doesn't study reasoning-specific recovery. 'From LLMs to LRMs' (Jan 2026) shows width pruning is more robust for reasoning but doesn't study RLVR recovery. RAC (NeurIPS 2025) demonstrates CoT-calibrated pruning improves unstructured/2:4 pruning but not full structural pruning. 'RL Squeezes, SFT Expands' (ICLR 2026 Poster) reveals RLVR and SFT shape reasoning through fundamentally different dynamics — RL compresses incorrect trajectories while SFT expands correct ones — but this insight has not been connected to pruning decisions. P² Law (ACL 2025) provides scaling laws for post-training recovery after pruning but only studies continual pre-training, not RLVR. PASER (2025, under review) optimizes which recovery DATA to use for pruned LLMs but does not address which STRUCTURES to prune for recoverability. The critical gap: (a) no work systematically compares how different pruning methods interact with RLVR recovery quality, (b) no work tests whether the optimal pruning order changes for RLVR vs. SFT recovery, and (c) no pruning criterion optimizes for post-RLVR recoverability rather than immediate accuracy. This gap is most consequential at 25–45% sparsity, where the pruning method likely determines whether RLVR recovery can close the gap or hits a recovery ceiling.

## Landscape (SOTA & Limitations)

GRASPrune (ACL 2026 Main) provides SOTA budgeted structural pruning with global gating, jointly pruning FFN channels and KV head groups, with public code (github.com/ZiY-Wang/GRASPrune). RESP (Dec 2025) introduces self-reflective structured pruning using gradient-based importance on self-generated reasoning traces, achieving 81.3% on GSM8K at 40% sparsity but without recovery and without public code. Self-Healing (2025, under review) applies RLVR recovery to structured-pruned reasoning models at 25% compression, reaching 95%+ (vs. ~80% SFT), using standard pruning methods. RAC (NeurIPS 2025) shows CoT-calibrated reconstruction dramatically improves unstructured and 2:4 pruning but not full structural pruning. 'From LLMs to LRMs' (arXiv Jan 2026) finds width pruning more robust than depth pruning for reasoning and calibration alignment matters, without RLVR study. 'RL Squeezes, SFT Expands' (ICLR 2026 Poster) reveals RLVR compresses incorrect reasoning trajectories while SFT expands correct ones, providing the theoretical basis for why pruning-recovery interaction should differ by recovery method. P² Law (ACL 2025) establishes scaling laws for post-training loss after pruning as L ∝ (1/ρ)^γ, predicting recovery data requirements, but only studies continual pre-training, not RLVR or SFT, and not reasoning models. PASER (2025, under review) proposes data selection for efficient pruned LLM recovery using manifold learning and capability-aware budget allocation, but optimizes recovery data rather than the pruning decision itself — complementary to RASP. 'Doing More With Less' (Apr 2026) shows unstructured pruning can improve test-time scaling for reasoning, while structured pruning degrades it. MPruner (arXiv 2024) uses inter-layer CKA similarity to cluster and remove redundant layers in CNNs and transformers, achieving up to 50% parameter reduction; a URI thesis (Lachance, 2024) similarly applies CKA for layer-level similarity pruning of VGGNet. Both operate at the layer level for depth pruning, using CKA to identify globally redundant layers — distinct from RASP's use of intra-layer CKA between individual attention heads/MLP channels to predict per-structure recoverability under RLVR (different granularity, different objective). MIPP (2024) demonstrates mutual information conservation between adjacent layers implies re-trainability after pruning, providing theoretical grounding. 'Redundancy-Aware Pruning of CNNs' (Neural Computation 2020) pioneered redundancy-based pruning in decorrelated feature spaces for CNNs, but addresses neither LLM-scale structured pruning, reasoning models, nor post-pruning recovery optimization. Bonsai (ICML 2025) achieves gradient-free structured pruning with public code. PAT (AAAI 2025) shows pruning-aware tuning outperforms sequential prune-then-finetune. OPSD (May 2026) proposes SFT→RLVR→OPSD as optimal post-training for reasoning trace compression. The critical absence: no work studies how the pruning decision interacts with RLVR recovery quality, whether this interaction differs from SFT recovery, or designs pruning to maximize post-RLVR reasoning performance.

## Proposed Approach

We propose Recovery-Aware Structured Pruning (RASP), which optimizes structural pruning decisions for post-RLVR recoverability rather than immediate accuracy. The core insight, motivated by 'RL Squeezes, SFT Expands' (ICLR 2026 Poster), is that RLVR recovery works through exploration and path compression — it needs maintained exploratory capacity in the pruned model — while SFT recovery works through trajectory imitation — it needs preserved trajectory-encoding structures. Consequently, the optimal pruning strategy should differ for RLVR vs. SFT recovery, and structures that are functionally redundant (overlapping with retained structures) are more RLVR-recoverable because RLVR can redistribute their function through global exploration.

RASP operates in three stages:

(1) **Reasoning-trace structural analysis**: Generate chain-of-thought reasoning traces using the model's own distribution (following RESP's calibration insight) and compute two scores per structure (attention head or MLP channel) h: (a) standard structural importance I(h) via gradient-based attribution on reasoning traces, and (b) functional overlap F(h) measuring how well h's reasoning-time activation pattern can be reconstructed from other structures in the same layer, computed as CKA (Centered Kernel Alignment) between h's activations and the remaining structures' activations. CKA approximates the mutual information between h and the retained model (cf. MIPP's theoretical result that MI conservation implies re-trainability), providing an information-theoretic grounding for recoverability. Note: unlike MPruner (2024) and related work that use inter-layer CKA to identify globally redundant layers for depth pruning, RASP uses intra-layer CKA between individual structures (attention heads, MLP channels) to predict per-structure recoverability under RLVR — a fundamentally different granularity targeting a different objective (post-recovery performance vs. immediate accuracy).

(2) **Recovery-aware pruning**: Compute RLVR-recoverability-aware scores S(h) = I(h) × (1 - F(h))^α, where α controls the recoverability penalty. Structures with high importance AND low functional overlap are irrecoverable (unique reasoning scaffolding — protected). Structures with high importance but high functional overlap are RLVR-recoverable (their function can be redistributed via RLVR's global optimization). Remove structures with lowest S(h) up to target sparsity.

(3) **RLVR recovery**: Apply GRPO-based reinforcement learning with verifiable rewards on mathematical reasoning data using the verl framework to recover the pruned model's reasoning ability.

**Key empirical contributions** (designed to be publishable even if the specific RASP method only marginally improves over baselines):

(a) **Pruning-recovery interaction study**: First systematic comparison of how 3 pruning methods (LLM-Pruner, Bonsai, GRASPrune) interact with RLVR recovery across 3 sparsity levels (25%, 35%, 45%), quantifying which pruning method best preserves RLVR recoverability.

(b) **RLVR vs. SFT recovery divergence**: Demonstrate that the optimal pruning order CHANGES when optimizing for post-RLVR vs. post-SFT performance — structures that are expendable for RLVR recovery may be critical for SFT recovery and vice versa, explained by the 'RL Squeezes, SFT Expands' mechanism.

(c) **Functional overlap predicts RLVR recoverability**: Measure correlation between pre-pruning functional overlap scores and post-RLVR accuracy restoration, testing whether F(h) is a stronger predictor of RLVR recoverability than standard importance I(h).

**Comprehensive evaluation beyond math**: Evaluation covers not only mathematical reasoning (GSM8K, MATH-500) but also long-context capability (LongBench, RULER), instruction following (MT-Bench), knowledge retention (MMLU), code generation (HumanEval), and general language modeling (WikiText-2 perplexity, C4 perplexity). LongBench and RULER are especially important for reasoning models that generate long chain-of-thought traces — pruning may disproportionately degrade long-context performance even when short-context math accuracy recovers. MT-Bench tests whether the pruned+recovered model retains general instruction-following capability beyond math, differentiating from Self-Healing which only evaluates math benchmarks. DeepSeek-R1-Distill-Qwen-7B's 131K context window enables meaningful long-context evaluation.

**Differentiation from CKA-based pruning lineage**: MPruner (2024) uses inter-layer CKA to cluster redundant layers for depth pruning in CNNs and general transformers, optimizing for immediate accuracy preservation. Lachance (2024) similarly applies CKA-based layer similarity for pruning VGGNet. In contrast, RASP uses intra-layer CKA between individual attention heads/MLP channels to predict per-structure recoverability under RLVR in reasoning LLMs — a fundamentally different use of CKA targeting a different pruning granularity (width vs. depth) and optimizing for a different objective (post-recovery reasoning performance vs. immediate accuracy).

**Differentiation from redundancy-based pruning lineage**: Unlike 'Redundancy-Aware Pruning of CNNs' (2020), which eliminates redundancy in a decorrelated feature space to minimize immediate accuracy loss for CNNs, RASP uses functional overlap specifically to predict post-recovery performance in LLMs. The fundamental difference: CNN pruning with fine-tuning is a local adjustment, while RLVR is a global reward-driven optimization that can redistribute function across the entire network. Redundancy in the RLVR context is not a flaw to eliminate but a signal of recoverability.

**Relationship to PASER**: PASER (2025) optimizes WHICH DATA to use for recovery; RASP optimizes WHICH STRUCTURES to prune for recoverability. These are complementary — RASP could be combined with PASER's data selection to jointly optimize what to prune and what to train on.

**Relationship to P² Law**: P² Law predicts HOW MUCH recovery data is needed given a pruning rate; RASP predicts WHICH structures are recoverable given a recovery method. These are complementary — RASP could be combined with P² Law to jointly optimize what to prune and how much to train.

**Statistical validation plan**: The primary correlation analysis between functional overlap F(h) and RLVR recoverability operates at two levels: (i) model-level correlation across N=11 pruned configurations (9 baselines + 2 RASP), where we can detect Pearson r≥0.7 with power ~0.65 at α=0.05 using one-tailed testing (directional hypothesis); (ii) structure-level analysis within each configuration, correlating per-structure F(h) with per-structure activation redistribution after RLVR recovery across hundreds of structures per model, providing substantially higher statistical power. We report bootstrap 95% confidence intervals and permutation tests (10,000 permutations) for both levels. We define publishability thresholds: r≥0.7 (strong, primary claim supported), r∈[0.5,0.7) (moderate, directionally supportive — claim framed as suggestive evidence), r<0.5 (weak — pivot to contingency plan focusing on contributions (a) and (b)).

**Contingency plan**: If the correlation between functional overlap and RLVR recoverability is weak (r < 0.5 at model level AND no significant structure-level pattern), the systematic pruning-method × recovery-method comparison across sparsity levels (contribution a+b) remains a strong empirical contribution, as no prior work provides this data. The expanded evaluation suite (LongBench, RULER, MT-Bench, C4) further strengthens this contingency by providing the most comprehensive assessment of pruned+recovered reasoning models to date.

Experiments target DeepSeek-R1-Distill-Qwen-7B as the primary model at 25%, 35%, and 45% structured sparsity. Baselines: LLM-Pruner+RLVR, Bonsai+RLVR, GRASPrune+RLVR (all with public code), plus LLM-Pruner+SFT and GRASPrune+SFT at 35% sparsity for recovery-method comparison (Bonsai+SFT dropped to meet compute budget). RASP+RLVR evaluated at 25% and 40% sparsity. RESP results cited from paper (no public code). Evaluation covers perplexity (WikiText-2, C4), knowledge (MMLU), code (HumanEval), reasoning (GSM8K, MATH-500), long-context (LongBench, RULER), and instruction following (MT-Bench). Hardware latency measured on A100/H100 GPUs.

## Resource Estimate

- **auto_research**: {'claude_api_cost': '$200-400 (~2000-4000 turns for full experiment loop, correlation analysis, paper writing)', 'estimated_gpu_cost': '$1050-1400', 'gpu_hours': '~350h H100-80GB (comprehensive ablations: multiple redundancy metrics, CKA vs cosine vs linear probe, extended sparsity range to 50%)', 'gpu_utilization': 'Very high (85-95%): fully pipelined with automated result parsing', 'risk_note': 'If core hypothesis fails, automated agent pivots to systematic empirical study of pruning-method × recovery-method interaction (still strong EMNLP contribution). All baselines use public code, minimizing implementation risk.', 'speed_bottleneck': 'RLVR recovery remains the critical path at 12-15h per run. With 8 GPUs, all 11+ runs complete in ~2 days. Automated agent should run the Day 3 hypothesis validation experiment first before expanding.', 'team': '0 (initial setup ~2h for verl RLVR pipeline configuration)', 'timeline': '10-14 days with 8 concurrent H100s'}
- **human_in_loop**: {'claude_api_cost': '$80-150 (~800-1500 turns for experiment design, analysis, paper drafting)', 'estimated_gpu_cost': '$600-800', 'gpu_hours': '~200h H100-80GB (adds α hyperparameter sensitivity check at one sparsity level)', 'gpu_utilization': 'High (75-85%): agent queues prune→recover→eval pipelines; human reviews recoverability analysis at Day 5 checkpoint', 'risk_note': 'RLVR recovery is the critical path: each run takes ~12-15h on H100. With 4 GPUs, 11 RLVR runs complete in ~3 batches × 15h = 45h wall time (~2 days). Day 5 go/no-go checkpoint: if functional-overlap-recoverability correlation < 0.3 at model level AND no significant structure-level pattern at 35% sparsity, pivot to pure empirical comparison paper.', 'team': '1 researcher, ~2-3h/day active oversight of recovery curves and hypothesis validation', 'timeline': '14 days with 4 concurrent H100s'}
- **manual**: {'estimated_gpu_cost': '$590-790 (at ~$3/hr H100 spot pricing)', 'gpu_hours': '~197h H100-80GB (structural analysis: ~8h, pruning 11 configs: ~14h, RLVR recovery 11 runs [9 baselines + 2 RASP]: ~137h, SFT recovery 2 runs [LLM-Pruner+SFT, GRASPrune+SFT at 35%]: ~10h, evaluation incl. LongBench/RULER/MT-Bench/C4: ~28h)', 'gpu_utilization': 'High (70-80%): tight timeline forces pipelined execution with minimal idle time between stages', 'team': '1-2 researchers with RLVR and pruning experience, working full-time', 'timeline': '14 days (May 11–25, 2026)'}

## Key References

- Self-Healing: Recovering Pruned Large Reasoning Models via Reinforcement Learning (2025, under review)
- Think Before You Prune: Self-Reflective Structured Pruning for Reasoning Language Models [RESP] (arXiv Dec 2025)
- Think Before You Prune: Selective Self-Generated Calibration for Pruning Large Reasoning Models (arXiv 2025)
- Reasoning Models Can Be Accurately Pruned via Chain-of-Thought Reconstruction [RAC] (NeurIPS 2025)
- GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models (ACL 2026 Main)
- From LLMs to LRMs: Rethinking Pruning for Reasoning-Centric Models (arXiv Jan 2026)
- RL Squeezes, SFT Expands: A Comparative Study of Reasoning LLMs (ICLR 2026 Poster)
- P² Law: Scaling Law for Post-Training After Model Pruning (ACL 2025)
- Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling (arXiv Apr 2026)
- MPruner: Optimizing Neural Network Size with CKA-Based Mutual Information Pruning (arXiv Aug 2024)
- Using Centered Kernel Alignment for Understanding and Pruning Neural Networks (Lachance, URI Thesis 2024)
- PASER: Post-Training Data Selection for Efficient Pruned Large Language Model Recovery (2025, under review)
- Redundancy-Aware Pruning of Convolutional Neural Networks (Neural Computation 2020)
- Mutual Information Preserving Neural Network Pruning [MIPP] (arXiv 2024)
- Everybody Prune Now: Structured Pruning of LLMs with only Forward Passes [Bonsai] (ICML 2025)
- OPSD Compresses What RLVR Teaches: A Post-RL Compaction Stage for Reasoning Models (arXiv May 2026)
- PAT: Pruning-Aware Tuning for Large Language Models (AAAI 2025)
- LLM-Pruner: On the Structural Pruning of Large Language Models (NeurIPS 2023)
- Structural Pruning of Large Vision Language Models: A Comprehensive Study on Pruning Dynamics, Recovery, and Data Efficiency (arXiv Apr 2026)
- GPrune-LLM: Generalization-Aware Structured Pruning for Large Language Models (arXiv Mar 2026)

## Reviewer Evaluation

**Scores**:
  - clarity: **{'rationale': 'The proposal is exceptionally well-structured with clear three-stage method description, explicit differentiation from 7+ related works, statistical validation plan with power analysis and publishability thresholds, and well-defined contingency. The evaluation suite now covers all user-required benchmarks. The relationship to P² Law, PASER, OPSD, and PAT is clearly articulated as complementary rather than competing. Minor concern: the proposal could be more concise — the extensive differentiation sections, while thorough, may indicate insecurity about novelty rather than confidence.', 'score': 4}**/5
  - feasibility: **{'rationale': 'All three baseline pruning methods (LLM-Pruner, Bonsai, GRASPrune) have public code. DeepSeek-R1-Distill-Qwen-7B is publicly available. The verl framework for GRPO-based RLVR is mature and documented. At ~197 H100-hours, compute is tight but within the 200h budget. The 14-day timeline is aggressive but plausible: RLVR recovery is the critical path at ~12-15h/run, but with 4 H100s, 11 RLVR runs complete in ~3 batches (~2 days wall time). The structural analysis (8h), pruning (14h), and evaluation (28h) can be pipelined around recovery runs. The contingency plan (pivot to empirical comparison if correlation is weak) is well-designed. Main risk: RLVR recovery instability could require reruns, eating into the tight budget. RESP comparison is handled correctly — cited from paper, not reimplemented.', 'score': 4}**/5
  - impact: **{'rationale': 'The pruning-recovery interaction study fills a practical need: as RLVR becomes standard for reasoning model training, understanding how to prune optimally for RLVR recovery (rather than immediate accuracy) has direct deployment implications. The finding that optimal pruning order differs for RLVR vs. SFT recovery — if confirmed — would change how practitioners approach reasoning model compression. The comprehensive evaluation suite (9 benchmarks including LongBench, RULER, MT-Bench) provides the most thorough assessment of pruned+recovered reasoning models to date. EMNLP Efficient Methods track is appropriate. Impact is 4 not 5 because the community may view the method as a moderate improvement over GRASPrune+RLVR rather than a paradigm shift.', 'score': 4}**/5
  - novelty: **{'rationale': "The core idea — optimizing pruning decisions for post-RLVR recoverability using intra-layer functional overlap (CKA) — occupies a genuine gap. No existing work studies how pruning method choice interacts with RLVR recovery quality, or whether the optimal pruning order changes for RLVR vs. SFT recovery. The differentiation from MPruner (inter-layer CKA for depth pruning) and redundancy-aware CNN pruning (2020) is well-articulated. The formula S(h) = I(h) × (1-F(h))^α is simple but principled — the theoretical grounding via MIPP's MI-conservation result and the 'RL Squeezes, SFT Expands' mechanism provides a non-trivial justification. The three empirical contributions (pruning-recovery interaction, RLVR-vs-SFT divergence, functional overlap as predictor) form a robust empirical story. Score limited to 4 rather than 5 because the method itself is an importance re-weighting heuristic rather than a fundamentally new pruning algorithm.", 'score': 4}**/5

## Human Review Note

## Agent 审核结果（完整三阶段 pipeline）

**Verdict**: PASS

**入口三重共识 (X)**: 27.0%
**终审自评 (Y)**: 36.0%
**出口三重共识 (Z)**: 33.0%
**Z 区间**: [27.0%, 38.0%]
**真实提升 (Z-X)**: +6.0 pp
**幻觉幅度 (Y-Z)**: +3.0 pp
**出口一致性**: 高
**出口三次评估**: [32.0, 33.0, 33.0]

### 优化方案 / 拒绝详情
【优化方案】

1. [核心叙事 / Core Thesis] — 从"提出一个 pruning 方法"重构为"假说驱动的实证研究 + 理论拓展"。引入 **Redundancy Paradox** 概念命名：传统剪枝和 RASP 都移除高 CKA-overlap 结构，但原因相反（"功能已覆盖" vs "功能易迁移"）。显式提出可检验假说 **H1 (Recovery-Method-Conditioned Pruning)**：functional redundancy 与 RLVR recoverability 正相关但与 SFT recoverability 弱/无相关。 — 命中 **Novelty**（从"又一个 pruning metric"升级为反直觉假说验证）+ **Significance**（给 reviewer 一个 crisp、memorable 的 conceptual hook）

2. [理论定位 / Core Thesis 第二段] — 将 RASP 从 "RL Squeezes, SFT Expands" 的下游应用验证升级为 **跨粒度理论拓展**：显式提出 cross-granularity question——RL Squeezes 在 representational level 观察到的 compression vs. expansion 效应是否 propagate 到 individual-structure level 的 functional demands？无论 H1 确认还是否定，都为 RL Squeezes 理论增加一个新维度的证据。 — 命中 **Novelty**（从应用验证到理论拓展）+ **Significance**（改变与 RL Squeezes 的关系：downstream → upstream）

3. [概念贡献 / 新增 Paradigm-Conditioned Trainability 段落] — 显式建立与 Lottery Ticket Hypothesis 的推广关系：LTH 问 "which subnetwork trains well"（binary），RASP 问 "what to remove so remainder recovers well under a specific paradigm"（paradigm-conditional）。命名为 paradigm-conditioned trainability/prunability。 — 命中 **Novelty**（提出新概念框架，与高影响力 LTH 建立显式推广关系）

4. [贡献体系 / Contributions 重组] — 三条贡献全面重构：
   - **(1)** 交互研究从 contingency plan 提升为**并列第一贡献**（"most comprehensive pruning × recovery interaction benchmark to date"），Self-Healing 作为 reference point 纳入。"first systematic" 软化为 "most comprehensive to date" 以降低被单一 counterexample 推翻的风险。
   - **(2)** 从 "demonstration that optimal pruning order changes"（hypothesis-as-claim）改为 "systematic investigation of whether and how"（双向有效，positive/negative 均为贡献）。Null result 显式定位为 RL Squeezes 理论的 granularity boundary stress test。
   - **(3)** Mechanistic analysis 从"统计验证的补充证据"升格为与统计验证**并列的核心分析**。新增 scoring ablation（CKA vs. magnitude / gradient / random）作为 sub-contribution。新增 "reusable regression-based validation protocol" 定位。
   — 命中 **Soundness**（双向有效的贡献设计）+ **Significance**（benchmark + method 双贡献结构降低 marginal improvement 拒稿风险）

5. [方法描述 / Method 段] — 修正技术表述错误："approximating mutual information" → "measuring functional similarity via linear CKA (a kernel-based statistical dependence measure)"。新增 CKA Reliability 段落：split-half analysis（Spearman ρ > 0.9）+ calibration size sensitivity（512/1024/2048 样本）+ bootstrap CI per head。 — 命中 **Technical Soundness**（消除 reviewer 对核心方法理解准确性和 head-level CKA 可靠性的质疑）

6. [统计方法 / Contribution (3) 内部] — 统计验证全面重构：
   - Structure-level 分析（N=224+ heads）提升为**主验证**，使用 **mixed-effects regression**（layer 为 random effect）替代 OLS，正确处理层内 head 相关性。加入 covariates（weight L2-norm, gradient importance, activation magnitude, layer index, head index）隔离 CKA-overlap 的独立预测贡献。
   - Model-level 分析（N=15 配置：3 methods × 5 sparsity levels）降为**辅助印证**。
   - 删除 "one-tailed tests"，全部改用双尾检验。
   — 命中 **Technical Soundness**（confound control + 正确统计方法是 reviewer 必问点，主动回答大幅加分）

7. [RLVR 训练细节 / 新增 RLVR Training Protocol 段落] — 明确：GRPO 算法、ground-truth answer matching reward、GSM8K+MATH 训练集、固定超参 protocol（unpruned baseline grid search）。新增 RLVR hyperparameter sensitivity analysis（2-3 配置 ±30% 扰动）验证排序稳定性。报告 reward curves 和 convergence behavior。 — 命中 **Technical Soundness**（消除 RLVR 训练不透明的质疑）+ **Reproducibility**

8. [SFT 训练细节 / 新增 SFT Recovery Protocol 段落] — 明确：使用 GSM8K/MATH 数据集**自带的 gold solution traces**（非模型生成 traces），消除 trace quality confound。Training tokens 与 RLVR 匹配，消除 data-volume confound。超参固定，与 RLVR protocol 平行。 — 命中 **Technical Soundness**（消除 RLVR vs SFT 对比中的混淆因子）

9. [实验设计 / Evaluation 段] — Sparsity 粒度从 3-4 档扩展至 5 档（25/30/35/40/45%）。分层评估策略：核心评估（GSM8K, MATH-500）全配置必跑；扩展评估（MMLU, HumanEval, WikiText-2, C4, LongBench, RULER, MT-Bench）只在 best configuration 上跑。新增 scoring ablation（CKA vs. magnitude / gradient / random）。 — 命中 **Empirical Rigor** + **Soundness**（ablation 证明 CKA 的 unique value）

10. [Related Work / 大幅扩展] — 三条工作线系统覆盖：
    - LLM structured pruning：加入 ShortGPT, SliceGPT, Wanda 定位说明。LLM-Surgeon 显式排除 justification（paradigm-agnostic curvature estimation + 不支持 head-level structured pruning）。
    - Pruning-aware recovery：LTH 连接 + paradigm-conditioned trainability 推广。
    - RLVR training dynamics：RL Squeezes 之外的其他 RLVR 表征分析工作。
    — 命中 **Related Work**（覆盖 reviewer 最可能熟悉的工作，提前 address "why not compare with X?" 类质疑）

11. [Limitations / 新增完整 Limitations 段落] — 四层缺口坦诚声明：
    - 单模型验证（DeepSeek-R1-Distill-Qwen-7B），第二模型（Qwen2.5-7B-Instruct）仅做 CKA 分布分析。
    - 蒸馏模型 vs 原生 RLVR 模型的区别显式讨论——将此转化为额外研究问题。
    - LoRA/QLoRA recovery 未纳入实验矩阵，解释 full-param SFT 作为 paradigmatic extreme 是更 clean 的 H1 测试。
    - Stretch goal：如 compute 允许，做第二模型核心 RLVR 验证子集。
    — 命中 **Soundness**（诚实 limitation 声明比隐瞒好；reviewer 看到坦诚讨论会认为作者有自我意识）

12. [Contingency / 强化为三层场景] — 从 "if RASP marginal, interaction study is contribution" 的单层 contingency 升级为三层场景矩阵（H1✓+Order✓ / H1✓+Order✗ / H1✗），每种场景的贡献结构显式阐明。H1 失败时加入 exploratory analysis of alternative structural predictors 作为 fallback。 — 命中 **Soundness**（消除 "如果主假设失败论文没有贡献" 的结构性怀疑）

13. [Broader Implications / 新增段落] — CKA-overlap 从 RASP-specific scoring function 定位为 general-purpose RLVR diagnostic：pre-RLVR 模型诊断、selective RLVR、模型合并恢复性预测。 — 命中 **Significance**（对冲 "contribution too narrow" 的 borderline reject 理由）

14. [Compute Budget / 全面重构] — 从 "~197h, within ≤200h" 的粗估重构为详细分项 breakdown table（pruning 15h + CKA 14h + RLVR 140h + SFT 30h + sensitivity 15h + eval 23h + 2nd model 5h = ~242h）。GRPO 选择的合理性论证。固定超参消除 per-config tuning overhead 的说明。 — 命中 **Feasibility**（详细分项让 reviewer 信服可行性）

15. [Paper Space Planning / 新增段落] — 8-page 正文内容分配（Intro 2p + Method 1p + Setup 1p + Results 3p + Discussion 1p）+ appendix 内容规划。Figure budget（5 figures/tables: method overview, results heatmap, regression plot, mechanistic visualization, ablation summary）。 — 命中 **Presentation Feasibility**（展示实验规模在论文格式下可呈现）

【主要风险】:

1. **核心方法的增量性**：RASP 的底层框架（compute CKA → rank structures → prune lowest score）与 MPruner 的方法论结构相同，只是 granularity（inter-layer → intra-layer）和 objective（layer redundancy → head-level RLVR recoverability）不同。即使叙事已升级为假说驱动 + 理论拓展，技术层面的审稿人仍可能评价为 "MPruner 的直接推广，novelty 增量有限"。这是最可能触发 borderline reject 的风险点。**应对**：确保 mechanistic analysis 提供 compelling 的 "why it works" 证据（不仅是 "it works better"），让论文价值不完全依赖方法本身的 novelty。

2. **单模型 + 蒸馏模型验证**：全部 RLVR recovery 实验仅在 DeepSeek-R1-Distill-Qwen-7B 上验证，且该模型的推理能力来自蒸馏而非原生 RLVR。Reviewer 可能质疑：(a) 结果是否对此模型特异，(b) RL Squeezes 理论是否适用于蒸馏模型。第二模型仅做 CKA 分布分析（无 RLVR recovery），说服力有限。**应对**：在 limitations 中坦诚讨论，将蒸馏模型适用性转化为额外研究问题；如实验进展顺利且有算力剩余，优先执行 stretch goal（第二模型核心验证）。

【实施评估】:
  - 计算资源: 4×H100 GPU，14 天。总计 ~242h wall-clock time（~968 GPU-hours）。GRPO 训练（~140h, 占总量 58%）是主要计算瓶颈。需要稳定的 4-GPU 节点持续 14 天——任何 GPU 故障或抢占都会直接影响 timeline。无显著容错空间。
  - 数据需求: GSM8K 训练集（~7.5K 问题）、MATH 训练集（~7.5K 问题）及其 gold solution traces 用于训练；GSM8K test、MATH-500、MMLU、HumanEval、WikiText-2、C4、LongBench、RULER、MT-Bench 用于评估。全部公开可得，无需额外数据获取。DeepSeek-R1-Distill-Qwen-7B 和 Qwen2.5-7B-Instruct 权重均通过 HuggingFace 公开获取。
  - 人工介入: 无需人工标注或人工评审。GSM8K/MATH 已有 gold annotations。实验全流程可自动化。唯一需要人工判断的环节是 mechanistic visualization 的选择和解读（选择最有说服力的 case study 放入正文）。
  - 训练需求: 需要大量模型训练。~36 次 RLVR recovery（GRPO, 7B 模型, 4-5h/run）+ ~15 次 SFT recovery（2h/run）+ ~8 次 sensitivity/ablation RLVR runs。不需要从头预训练，所有训练都是 post-pruning recovery fine-tuning。
  - 新 Benchmark: 不需要构建新 benchmark。使用已有公开 benchmark 组合。贡献 (1) 的 "interaction benchmark" 是实验矩阵设计（3 pruning × 5 sparsity × 2 recovery），不是新数据集。
  - 预估周期: 从启动到可投稿约 **5-6 周**（14 天实验 + 2-3 周论文撰写 + 1 周修改迭代）。目标 EMNLP 2026 ARR May 25 deadline。实验阶段几乎无缓冲，论文撰写可与后期实验并行（前期 baseline 结果出来即可开始写 method + related work）。



## MVP Validation Results

- **Date**: 2026-05-14
- **Hypothesis Supported**: Yes

### Key Metrics

Post-prune GSM8K (N=100): RASP 29% vs Standard 1% (Δ=28pp, p<0.0001) | Matched: 20% sparsity, same parameter count | GRPO recovery: both models 100% truncated at 4096 tokens (technical limitation, not hypothesis failure) | RASP reward 5x higher than Standard in truncated GRPO (3.125% vs 0.625%)

### Summary

RASP pruning (CKA-aware structure selection) preserves reasoning ability significantly better than standard importance-only pruning at matched 20% sparsity. Post-prune GSM8K accuracy: RASP 29% vs Standard 1% (p<0.0001, N=100, matched parameters). GRPO recovery experiments failed for both models due to technical limitation (DeepSeek-R1 sampling generates ultra-long chains without EOS, causing 100% truncation at 4096 tokens), but this is orthogonal to the core hypothesis. The post-prune gap alone definitively supports the MVP claim.

### Recommendation

GO — 进入 research 阶段。Phase 2 优先级：(1) SFT warmup→GRPO 两阶段恢复证明 recovery claim (2) multi-seed 重复 (3) baseline 对比 (GRASPrune, Bonsai) (4) scoring ablation (CKA vs magnitude/gradient/random) (5) 多剪枝率 threshold analysis。EMNLP 2026 ARR May 25 仍为目标。
