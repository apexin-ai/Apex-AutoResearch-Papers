# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：GPQA random 也显示强 gradient（ratio ≈ 1×）+ 审稿人认为现象是 trivial（token removal 的必然后果

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 22
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-1/5ce792ab-ebc9-4b52-8f9c-3b1fb1b17c1f.jsonl`
- **Structured JSON:** [`675fad80c10aa7787a9c.json`](../../sessions/67/675fad80c10aa7787a9c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-17T01:44:08.717Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-17T01:44:08.717Z",
  "sessionId": "5ce792ab-ebc9-4b52-8f9c-3b1fb1b17c1f",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：GPQA random 也显示强 gradient（ratio ≈ 1×）+ 审稿人认为现象是 trivial（token removal 的必然后果而非 scoring-specific）+ 需要完全 reframe 核心 claim\n核心假设：['GPQA importance gradient 存在但 random 同样强（imp/rand ratio < 2×，类似 LLaMA 模式）', '审稿人质疑：如果 random 在长推理链 benchmark 上也有 gradient，那 \"importance-specific\" claim 不成立', 'Recency control 的 null 结果被审稿人解读为 \"recency 太弱（保留最近 token 本身就是好策略），不是有效 control\"', '审稿人认为 discrimination collapse 机制只是 obvious 的 \"pruning reduces score quality\" 重述', 'C5b mitigation pilot 失败被视为 \"连 direction 都不确定\" 的 negative signal']\n关键指标范围：{'gpqa_importance_median_gradient_s030': [1.5, 4.0], 'gpqa_imp_rand_ratio': [1.0, 2.0], 'cross_benchmark_specificity_range': '仅 MATH-500 DS ratio > 5×; 其余所有条件 < 3×', 'recency_max_dz_across_sparsities': [0.0, 0.15], 'reviewer_novelty_score': [2.0, 3.0], 'reviewer_overall_score': [2.5, 3.0], 'acceptance_probability': [0.08, 0.25]}\n叙事方向：Reframe：核心贡献不再是 'importance-specific phase interaction'，而是 'phase-dependent compound severity is a universal phenomenon whose magnitude scales with eviction method discriminativeness'。新叙事逻辑：任何 non-trivial eviction（importance/random）都产生 phase-dependent compound severity，但 severity magnitude 与 eviction method 的 token discrimination strength 正相关（importance > random >> recency≈null）。Recency 的 null 不是因为 scoring-independent，而是因为 recency 作为 eviction 策略本身 preserves temporal locality（对 reasoning 相对温和）。这个 reframe 仍然是新发现（prior work 未量化），但 novelty claim 从 'qualitative dissociation' 降为 'quantitative scaling law'。同一 venue（EMNLP），但需要重写 intro + framing + 补充 eviction discriminativeness 的量化指标（如 eviction overlap with oracle）。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: phase-gated-compound-sparse\nfocus: Key improvements since last dream: (1) recency scoring-independent control confirms phase gradient is attention-score-specific (three-way dissociation: importance/random/recency), (2) full 8-condition LLaMA cross-architecture validation (n=250, all PASS), (3) expanded related work (50 citations), (4) \"why not causal\" self-defense in discussion, (5) dense baseline phase stats. Evaluate whether these address the previous dream's main criticisms: narrow novelty, circularity concern, thin references, no figures, no practical method.\n\n## paper_framing.md\n\n# Paper Framing — Phase-Gated Compound Sparsity\n\n> 最后更新: 2026-05-17 (D102: C11 confirmed — recency triple NS across s015/s025/s030; s015+s025 primary, s030 supplementary) | 维护者: Director\n\n## Core Insight\n\nCompound sparsity（attention head pruning + KV cache eviction）的 severity 不是固定常数——它是 eviction strategy 和 reasoning phase 交互的涌现属性。Importance-based eviction 的 compound interaction severity（paired median difference: median(II_low_i − II_high_i)）随 sparsity 单调递增（DeepSeek: 0.39→1.21→3.99→8.48; Qwen: 0.07→0.31→1.07→3.16），而 random masking 在 s015/s020 NS，在 s025 跨模型显著但效应量远小于 importance（DS: 0.257 vs 3.986; QW: 0.393 vs 1.074, 2.7-17×差异），存在 sparsity threshold ~s020-s025（D063; s030 待定）。Cohen's d（per-problem paired, B=10000）从 medium 到 large（DeepSeek: 0.61→1.13; Qwen: 0.37→1.44，registry cohens_d s015→s030）。LLaMA 跨架构验证（D060, c8_llama_n250_fixed, n=250）：within-importance phase gradient 强（d_z=0.81-1.15, all p<10^-29, all monotonic），且 random 在 LLaMA 上所有条件均显著（d_z=0.41-0.46, all p<10^-12），imp/rand Δ ratio 仅 2.0-2.6×（vs DeepSeek 15-17×），strategy×phase 交互强度 architecture-dependent。GSM8K 跨 benchmark 验证（D075）：importance masking 的 phase gradient 在 GSM8K 上同样单调递增（QW: 0.039→0.158→1.100→2.092; DS: 0.241→0.740→1.992→4.682），但 strategy specificity（importance/random gradient ratio）从 MATH-500 的 15-17× 衰减至 GSM8K 的 2.3-3.8×。注意：\"反转\"仅在原始 II_low 值上（random > importance），phase gradient 层面 importance ≥ random。Strategy specificity 的 task-dependence 机制是开放问题（见 §6 Discussion）。这一发现挑战了 compound degradation 均匀分布的隐含假设。\n\n**数字基准**：所有数字基于 bf16 per-problem paired 统计量（B=10000 bootstrap）。median_diff 定义为 median(II_low_i − II_high_i)（逐 problem 配对差的中位数）。fp16 旧数据已弃用。\n\n## Narrative Arc\n\nCompound sparsity 是高效 LLM 推理的实用部署需求，但 prior work（SparK, Ada-KV, SLiM）将 compound interaction 视为均匀超可加。我们发现 severity 是 strategy × phase 交互的涌现属性：importance eviction 的 compound interaction 在 low-sparsity phase 远大于 high-sparsity phase（paired median difference 单调递增 0.39→8.48），而 random eviction 在低 sparsity (s015/s020) NS，在 s025+ 跨模型显著但效应量远小于 importance (2.7-17×)——存在 sparsity threshold (~s020-s025)，低于阈值 compound effect importance-specific，高于阈值两者均触发但 importance 主导。Cross-model replication 方向一致（Qwen magnitude ~1/4 of DeepSeek，onset threshold s≥0.20）。LLaMA 跨架构验证已完成（c8_llama_n250_fixed, n=250, D060）：within-importance phase gradient 强（d_z=0.81-1.15, all p<10^-29），random 所有条件显著（d_z=0.41-0.46, all p<10^-12），但 imp/rand ratio 仅 2.0-2.6×（远低于 DS 15-17×），strategy×phase 交互强度 architecture-dependent。Recency-based eviction（scoring-independent control, D100/D102）跨三个 sparsity level 均产生 null phase gradient（s015+s025 为 primary evidence，s030 supplementary due to numerical instability at extreme sparsity），确认 phase-dependent severity 是 attention-score-based eviction 的特有交互效应而非 token removal 的 trivial 副产物。我们通过 discrimination collapse 机制解释这一现象：head pruning → importance score 的判别力崩塌（Gini/CV 下降跨模型一致）→ importance eviction 退化为有偏伪随机。Attention entropy redistribution 作为 model-dependent secondary effect 在 DeepSeek 上观察到，但在 Qwen 上不稳健（D044）。\n\n**Framing 硬约束（D015）**：\n- MUST: \\\"emergent phase-strategy interaction\\\"\n- MUST NOT: \\\"importance metric limitation / importance is broken\\\"\n- MUST NOT: claim \\\"importance masking produces super-additive interaction\\\" without qualifier — random masking also produces positive II, and at s025+ random is statistically significant (D063). The distinguishing signal is **magnitude gradient** (importance 2.7-17× larger) and **onset threshold** (random NS below ~s020, importance significant from s015+), not the existence of super-additivity itself (D023)\n\n## Core Claims\n\n| ID | Claim | Status | Key Evidence |\n|----|-------|--------|-------------|\n| C1 | Compound sparsity severity is strategy- and task-modulated | confirmed | MATH-500: importance gradient 15-17× random (DeepSeek s025-s030); GSM8K: ratio 衰减至 2.3-3.8× (D075)。Phase gradient 层面 importance ≥ random 跨 benchmark 成立，但 magnitude ratio task-dependent。Threshold ~s020-s025 (D063) |\n| C2 | Severity is phase-modulated (amplified in low-sparsity phase) | confirmed | bf16 paired median difference 单调递增: 0.39→1.21→3.99→8.48; Bonferroni p<0.005 全 4 水平 (D032)。预注册：n=500 后若 QW s015 CI 仍跨零，叙事改为 'compound effect emerges above threshold sparsity (~s020)' |\n| C3 | Phase-strategy crossover exists | confirmed | s=0.25: importance high_phase=0.032 < random=0.818, importance low_phase=7.196 > random=1.363 (bf16) |\n| C4 | Discrimination collapse as primary mechanism; entropy redistribution model-dependent | partially_confirmed | D044: Gini/CV 下降跨模型一致; entropy collapse DeepSeek 一致但 Qwen s025 反转(+0.045) s030≈0。30/30 problems completed. |\n| C5 | Phase-modulated compound severity generalizes across models | confirmed | DeepSeek + Qwen cross-model replication: 方向一致, Cohen's d ρ=1.0, gradient permutation p=0.043. Qwen magnitude ~1/4 of DeepSeek, onset threshold s≥0.20 (S3→C). |\n| C5b | Phase-aware mitigation recovers compound degradation | future_work | D056: pilot 完成 gate_failed。Oracle recovery 18% < 30% gate (Wilcoxon p=0.002)，heuristic 32% 但 CI 跨零。方向正确但效应量不足，需更精细 phase boundary estimation → future work |\n| C6 | Severity gradient is sub-exponential | confirmed | Growth rate decreasing: Δ增长因子 3.8×→4.8×→2.0×（递减） |\n| C7 | Statistical power at n=500 confirms dose-response | confirmed | c2_n500_deepseek (success) + c2_qw_n500_r3 (success): 两模型 n=500 全 4 sparsity Bonferroni p<0.005, Spearman ρ=1.0 |\n| C8 | Cross-architecture validation (LLaMA) | confirmed | c8_llama_n250_fixed (n=250, D060): within-importance phase gradient d_z=0.81-1.15 (all p<10^-29, all monotonic) ✓。Random 所有条件显著 (d_z=0.41-0.46, all p<10^-12)，与 DeepSeek/Qwen random 低 sparsity NS 模式定性不同。Imp/rand Δ ratio 2.0-2.6×（远低于 DS 15-17×）。Strategy specificity architecture-dependent。n=250 功效充分。 |\n| C9 | Differentiation from Lethe/SparK prior work | planned | Related Work §2 引用区分 + SparK gap analysis |\n| C10 | Phase gradient cross-benchmark robust; strategy specificity task-modulated | confirmed | GSM8K DS gradient 0.241→4.682 单调递增; QW gradient 0.039→2.092; imp/rand ratio 衰减至 2.3-3.8× (D075)。QW random s025+s030 均 success |\n| C11 | Phase-dependent severity absent under scoring-independent eviction (recency control) | confirmed | D102: 三个 sparsity level 全部 NS。s015+s025 为 primary evidence (n=100 each, both d_z < 0.1, p > 0.5); s030 supplementary (numerical instability at extreme sparsity)。对比 importance: d_z=0.574-1.15, ratio=119.8×。Triple dissociation confirmed: importance 有 gradient, recency + random 均 NS。排除 (a) phase segmentation circularity (b) H2O scoring pathway confound。文献中无先例将 recency eviction 作为 methodological control (experimental design contribution)。 |\n| S3→C | Onset threshold is model-dependent (DeepSeek s≥0.15, Qwen s≥0.20) | confirmed | D037/D038: Qwen s015 d_z=0.37 CI含0, s020+ 显著 |\n| S7→C | Dose-response monotonicity (Spearman ρ=1.0) | confirmed | D047: 6-point dose-response, 单调递增 |\n\n## Anticipated Reviewer Concerns\n\n### RC1: Generalizability — 7B models only, benchmark scope\n- **预期质疑**: \\\"Results on two 7B models and MATH-500 only. How do we know this generalizes to larger models or other reasoning tasks?\\\"\n- **应对**: 四层泛化证据：(1) Cross-model: DeepSeek-R1-Distill-Qwen-7B + Qwen2.5-7B-Instruct（同架构不同训练，ρ=1.0）(2) Cross-architecture: c8_llama_n250_fixed (DeepSeek-R1-Distill-Llama-8B, LlamaForCausalLM, n=250)，within-importance phase gradient 强 (d_z=0.81-1.15)，但 strategy specificity 弱于 Qwen2 架构（2.0-2.6× vs 15-17×），strategy×phase 交互强度 architecture-dependent (3) **Cross-benchmark (D075)**: GSM8K（两模型）phase gradient 单调递增复现（DS: 0.241→4.682; QW: 0.039→2.092），但 strategy specificity ratio 从 MATH-500 15-17× 衰减至 2.3-3.8×，表明 phase modulation 跨 benchmark 稳健而 magnitude modulation task-dependent。Limitations 诚实声明：(a) 7B scale only；(b) strategy specificity 强度 task-dependent（GSM8K 衰减，可能因推理链更短）；(c) random phase gradient 行为 architecture-dependent。\n- **实验支撑**: C5 (cross-model) + C8 (c8_llama_n250_fixed cross-architecture, n=250) + C10 (cross-benchmark GSM8K, D075)\n\n### RC2: Methodology — phase segmentation circularity and scoring confound\n- **预期质疑**: \\\"Your phase segmentation uses perplexity computed from the same model whose sparsity you're measuring. Isn't this circular? And H2O's attention-score mechanism could itself create the phase gradient artifact.\\\"\n- **应对**: Recency-based eviction (scoring-independent control, D102 confirmed) produces null phase gradient across all three sparsity levels (s015+s025 primary, s030 supplementary), confirming the observed severity pattern is specific to attention-score-based methods, not an artifact of (a) phase segmentation itself or (b) the scoring computation pathway. Triple dissociation: importance shows gradient (d_z=0.574+), recency and random both NS. Novel experimental design: repurposing recency eviction as methodological control has no precedent in literature (H2O/StreamingLLM use it only as performance baseline).\n- **实验支撑**: C11 (recency_s015/s025/s030, D102 confirmed) + c4_entropy (discrimination collapse mechanism, D044)\n\n### RC3: Practical impact — 没有 throughput 数据\n- **预期质疑**: \\\"No wall-clock or throughput measurements. Is the severity amplification reflected in actual inference speed?\\\"\n- **应对**: 本文定位是 empirical finding paper（发现 + 机制解释），不是 method paper。Throughput 不是 claim 的一部分。Discussion 中明确 phase-gated controller 作为 future direction。\n  - C5b pilot 已完成（D056）：oracle recovery 18%（Wilcoxon p=0.002），heuristic recovery 32%（p=0.024），但两者 95% CI 均跨零。方向正确（Wilcoxon 显著）但效应量不足（未达 30% gate），需更精细的 phase boundary estimation。论文 §6 Discussion 诚实报告 pilot 结果 + future work。\n  - Heuristic > oracle 悖论值得提及：token position ratio 粗粒度划分可能恰好更适合 mitigation 场景，暗示 phase boundary 的最优粒度是开放问题。\n- **实验支撑**: c5b_pilot (gate_failed, D056)\n\n### RC4: Statistical rigor — bootstrap 是否足够\n- **预期质疑**: \\\"Per-problem bootstrap with 50 problems — sufficient sample size?\\\"\n- **应对**: bf16 使用 B=10000 per-problem paired bootstrap，有效配对数 n=49 (DeepSeek) / n=46 (Qwen)；n=500 实验进一步验证 (C7 confirmed)。Permutation test 使用 paired median difference 作为 robust statistic（D032），Bonferroni 校正后全 4 水平 p<0.005。Dose-response 主用 Wilcoxon signed-rank p + median_diff（robust to outliers），Cohen's d 作为辅助效应量（DeepSeek 0.61→1.13, Qwen 0.37→1.44, registry cohens_d s015→s030），注释高 sparsity 下 d 受 outlier-driven variance 影响（DS s020→s025: median 3.3× jump 但 d 非单调，因极端 II 值影响分母，D064）。可在 appendix 补充 per-problem 分布图（已生成 fig4_per_problem_dist.pdf）。\n- **实验支撑**: bf16 permutation test (D032) + Cohen's d per-problem paired (rebootstrap B=10000) + n=500 Wilcoxon (C7 confirmed)\n\n### RC5: Novelty — prior work 是否已覆盖 phase-dependent sparsity\n- **预期质疑**: \"ThinKV and phase-aware methods already consider phase. What's new?\"\n- **应对**: Prior work 在单轴上分析 phase（ThinKV: phase-aware eviction）或 compound（SparK: joint compression）。没有工作同时分析 compound × phase × strategy 的三维交互。Crossover 现象（同一 strategy 在不同 phase 方向反转）是全新发现。Related Work 加 Lethe 引用区分 + SparK 对比。具体区分：\n  - **ThinKV** (arxiv 2510.01290, Oct 2025): 在 KV cache 单轴上做 phase-aware 压缩（按 CoT 阶段差异化 eviction），但不涉及 pruning × eviction 的 compound interaction。我们研究的是双轴（head pruning × KV eviction）compound interaction 如何随 phase 变化，ThinKV 的单轴 phase-aware 策略是我们分析维度的子集。\n  - **Physics of KV Cache Compression** (arxiv 2603.01426, Mar 2026): 揭示了单轴 KV 压缩的 phase transition 和 representational rigidity，是机制层面最接近的工作。关键区分：他们刻画的是单一压缩轴上压缩率的 critical threshold（phase transition），我们刻画的是两种压缩方法的 compound interaction severity 如何被 reasoning phase 调制（phase-dependent gradient）——维度正交。\n  - **HIES** (arxiv 2510.13832, Oct 2025): 发现 importance score collapse 并提出 entropy 补偿，为我们的 discrimination collapse 机制提供独立 supporting evidence——他们在单轴上观察到的 score collapse 正是我们在 compound setting 中发现的 Gini/CV 下降的单轴对应。\n  - **R-KV** (arxiv 2505.24133, May 2025): 针对 reasoning task 做 KV compression 优化，属于 task-specific method。我们不是提出新方法，而是 mechanistic 分析 compound interaction 的 phase-dependent 行为，二者目标不同（optimization vs understanding）。\n- **实验支撑**: C3 (crossover), Related Work §2 的 gap 分析\n\n### RC6: Novelty vs Lethe/SparK\n- **预期质疑**: \"How does this differ from Lethe (AAAI 2026) which also does layer-time-adaptive KV pruning, or SparK which studies compound compression?\"\n- **应对**: Lethe 和 SparK 都没有分析 phase × strategy 的交互效应。Lethe 是 method paper（提出 adaptive eviction 方法），我们是 empirical finding paper（发现 phase-dependent severity gradient）。SparK 研究 compound compression 但将 interaction 视为均匀超可加，我们发现 interaction severity 随 phase 和 strategy 变化。新近工作进一步确认我们的独特定位：\n  - **Physics of KV Cache Compression** (arxiv 2603.01426, Mar 2026) 是最近的相关工作，研究单轴压缩的 phase transition 阈值行为。与我们的核心区别：他们的 phase transition 是压缩率维度上的 critical point，我们的 phase-dependent gradient 是 reasoning phase 维度上 compound interaction 的连续调制——两者刻画的 \"phase\" 语义不同（compression-rate phase vs reasoning phase）。\n  - **ThinKV** (arxiv 2510.01290, Oct 2025) 和 **R-KV** (arxiv 2505.24133, May 2025) 都在 KV compression 单轴上引入 phase/reasoning awareness，但均未涉及 compound interaction。我们的贡献在于揭示 pruning × eviction 双轴交互如何被 reasoning phase 调制，这是单轴方法无法观察到的涌现现象。\n  - **HIES** (arxiv 2510.13832, Oct 2025) 的 importance score collapse 发现为我们的 discrimination collapse 机制提供了独立佐证，但 HIES 聚焦于单轴补偿方法，未研究 collapse 在 compound setting 中的放大效应。\n  - Related Work §2 明确区分三者定位：Lethe/SparK = method/compound method, ThinKV/R-KV = single-axis phase-aware, Physics of KV = single-axis phase transition, HIES = single-axis collapse。我们 = compound × phase × strategy 三维交互分析。\n- **实验支撑**: 不需要额外实验，仅需 §2 引用区分\n\n## Paper Positioning\n\n**类型**: Empirical finding paper（非 method paper）\n**核心贡献**:\n1. 发现 compound sparsity severity 的 strategy × phase 交互\n2. 量化 severity gradient（bf16 paired median difference 0.39→8.48, Cohen's d 0.61→1.13）和 crossover 现象\n3. 提出 discrimination collapse 机制解释（Gini/CV 跨模型一致；entropy redistribution model-dependent）\n4. Cross-model + cross-architecture (LLaMA, n=250) replication 验证泛化性（三模型两架构；strategy×phase 交互强度 architecture-dependent, D060）\n5. Novel use of scoring-independent eviction (recency-based) as methodological control — experimental design contribution 排除 phase segmentation circularity 和 scoring pathway confound (C11, D102 confirmed)\n\n**投稿目标**: EMNLP 2026 ARR, deadline 2026-05-25\n**Rebuttal 准备**: Day 9 (2026-05-23) 预留 rebuttal letter 写作时间\n**关键时间线**：\n- Day 9 (2026-05-23): 预留写 rebuttal letter\n- Day 11 (2026-05-25): EMNLP 2026 ARR 截稿\n\n\n## experiment_plan (with registry status)\n\n- id: c1_bf16_importance_s025\n  claim: C1\n  description: 'II median: high=0.032, mid=1.118, low=7.196; importance masking shows\n    strong phase gradient'\n  registry_id: bf16_importance_s025\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics: &id003\n    interaction_index:\n      high:\n        mean: 0.302756\n        median: 0.032363\n        ci:\n        - 0.083714\n        - 0.543977\n        winsorized_mean: 0.200962\n        skewness: 4.8826\n      mid:\n        mean: 5.729665\n        median: 1.118069\n        ci:\n        - 3.455574\n        - 8.471799\n        winsorized_mean: 4.189902\n        skewness: 8.2799\n      low:\n        mean: 25.852951\n        median: 7.195958\n        ci:\n        - 19.077082\n        - 33.497293\n        winsorized_mean: 19.319103\n        skewness: 7.3986\n    per_problem_ii_stats:\n      high:\n        n: 49\n        min: -0.316321\n        max: 4.003714\n        mean: 0.133714\n        median: 0.009873\n        std: 0.595358\n      mid:\n        n: 40\n        min: -0.024794\n        max: 18.720486\n        mean: 2.537744\n        median: 1.05707\n        std: 3.962575\n      low:\n        n: 50\n        min: -1.854733\n        max: 75.467653\n        mean: 11.28281\n        median: 3.954593\n        std: 16.620011\n    gradient_paired_aggregate_legacy: 222.35\n    median_difference: 7.1636\n    n_problems: 50\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: false\n      overall: PASS\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    perplexity:\n      high:\n        dense: 1.1689\n        attn: 1.6511\n        kv: 1.8628\n        both: 2.7026\n      mid:\n        dense: 1.2269\n        attn: 1.7039\n        kv: 5.6205\n        both: 13.3436\n      low:\n        dense: 1.2286\n        attn: 1.8366\n        kv: 31.756\n        both: 63.668\n- id: c1_bf16_ds_rand_s025\n  claim: C1\n  description: 'Random II median: high=0.818, mid=0.932, low=1.363; flat gradient\n    vs importance'\n  registry_id: bf16_ds_rand_s025\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 3.59\n        median: 0.8182\n        ci:\n        - 1.4021\n        - 6.2327\n        median_ci:\n        - 0.5075\n        - 1.7217\n        winsorized_mean: 6.3965\n        skewness: -7.57\n      mid:\n        mean: -1.8455\n        median: 0.9324\n        ci:\n        - -10.3663\n        - 4.9342\n        median_ci:\n        - 0.7331\n        - 1.7003\n        winsorized_mean: 3.1014\n        skewness: -12.76\n      low:\n        mean: 0.7212\n        median: 1.3627\n        ci:\n        - -4.2068\n        - 4.5006\n        median_ci:\n        - 1.0869\n        - 2.6866\n        winsorized_mean: 4.1866\n        skewness: -15.85\n    perplexity:\n      high:\n        dense: 1.1687\n        attn: 7.237\n        kv: 4.9751\n        both: 17.7423\n      mid:\n        dense: 1.2269\n        attn: 868.3199\n        kv: 5.1165\n        both: 29.4661\n      low:\n        dense: 1.2284\n        attn: 24.3571\n        kv: 6.7993\n        both: 17.9694\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    n_problems: 50\n    pass_fail:\n      ci_overlap: false\n      sign_reversal: false\n      overall: FAIL\n    median_difference: 0.5445\n- id: c1_bf16_qw_imp_s025\n  claim: C1\n  description: 'Qwen cross-model: median_diff=1.109, Cohen''s d=1.233, p<1e-5'\n  registry_id: bf16_qw_imp_s025\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics:\n    median_difference: 1.108706\n    permutation_p: 0\n    cohens_d: 1.2329\n    bootstrap_ci_95:\n    - 0.609247\n    - 1.469002\n    wilcoxon_p: 0\n    n_bootstrap: 10000\n    n_paired: 46\n- id: c1_sf5_asymmetric_spot\n  claim: C1\n  description: 'Asymmetric configs: h02_kv03 D=19.13, h03_kv02 D=18.25; gradient consistent'\n  registry_id: sf5_asymmetric_spot\n  role: ablation\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics:\n    config_a_h02_kv03:\n      II_low: 19.51\n      II_mid: 6.05\n      II_high: 0.38\n      D: 19.13\n    config_b_h03_kv02:\n      II_low: 18.77\n      II_mid: 3.97\n      II_high: 0.52\n      D: 18.25\n    pre_registered_criterion_passed: true\n    gradient_direction: II_low >> II_mid >> II_high (consistent with symmetric baseline)\n- id: c1_c2_accuracy_eval\n  claim: C1\n  description: 'DS dense->s030 acc: 0.52->0.10 (-0.42); QW dense->s030: 0.32->0.14\n    (-0.18)'\n  registry_id: c2_accuracy_eval\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics:\n    n_problems: 50\n    ds_dense_acc: 0.52\n    ds_s015_acc: 0.36\n    ds_s015_delta: -0.16\n    ds_s030_acc: 0.1\n    ds_s030_delta: -0.42\n    qw_dense_acc: 0.32\n    qw_s015_acc: 0.34\n    qw_s015_delta: 0.02\n    qw_s030_acc: 0.14\n    qw_s030_delta: -0.18\n    ds_s030_chinese_reasoning_rate: 0.4\n    ds_dense_truncation_rate: 0.56\n    note: v2 rescored with fixed radical+degree matcher. DS s015 34→36, QW s015 32→34\n- id: c2_bf16_importance_s030\n  claim: C2\n  description: 'Phase gradient: II low=14.64 >> mid=2.28 >> high=0.053 (median); low/high\n    ratio ~276x'\n  registry_id: bf16_importance_s030\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics: &id001\n    interaction_index:\n      high:\n        mean: 0.5547\n        median: 0.0534\n        ci:\n        - 0.2773\n        - 0.9198\n        winsorized_mean: 0.3367\n        skewness: 10.62\n      mid:\n        mean: 11.3\n        median: 2.2833\n        ci:\n        - 6.865\n        - 17.2633\n        winsorized_mean: 8.1752\n        skewness: 9.19\n      low:\n        mean: 57.7946\n        median: 14.6395\n        ci:\n        - 41.4416\n        - 77.0467\n        winsorized_mean: 39.3143\n        skewness: 8.31\n    per_problem_ii_stats:\n      high:\n        n: 49\n        min: -0.5095\n        max: 4.4457\n        mean: 0.1976\n        median: 0.0343\n        std: 0.6793\n      mid:\n        n: 40\n        min: -0.1989\n        max: 34.0258\n        mean: 5.2585\n        median: 1.5173\n        std: 7.9382\n      low:\n        n: 50\n        min: -7.3027\n        max: 126.7985\n        mean: 22.6601\n        median: 9.9731\n        std: 28.4096\n    gradient_paired_aggregate_legacy: 57.24\n    median_difference: 14.5861\n    n_problems: 50\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: false\n      overall: PASS\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    perplexity:\n      high:\n        dense: 1.1689\n        attn: 1.7123\n        kv: 2.0544\n        both: 3.2372\n      mid:\n        dense: 1.2269\n        attn: 1.7894\n        kv: 9.4821\n        both: 24.2847\n      low:\n        dense: 1.2286\n        attn: 1.9347\n        kv: 51.6485\n        both: 122.61\n- id: c2_v6_importance_s030\n  claim: C2\n  description: II low_median=34.69, mid_median=7.27, high_median=0.88; bootstrap_gradient=41.92,\n    CI=[19.14,299.76]\n  registry_id: v6_importance_s030\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 0.8833\n    ii_mid_median: 7.2706\n    ii_low_median: 34.6937\n    ii_high_mean: 1.5151\n    ii_mid_mean: 78.8215\n    ii_low_mean: 1163.9677\n    per_problem_ii_count: 50\n    n_high: 40\n    n_mid: 22\n    n_low: 20\n    problems: 50\n    bootstrap_gradient_paired: 41.92\n    bootstrap_ci_paired:\n    - 19.14\n    - 299.76\n    bootstrap_gradient_unpaired: 39.28\n    bootstrap_ci_unpaired:\n    - 21.87\n    - 129.59\n    bootstrap_p: 0\n- id: c2_think_phase_validation\n  claim: C2\n  description: Phase segmentation kappa=0.887; thinking=57.8% low-sparsity, answer=62.7%\n    high-sparsity\n  registry_id: think_phase_validation\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics:\n    effective_n: 48\n    skipped_problems: 2\n    median_kappa: 0.887\n    thinking_in_low_sparsity_phase: 0.578\n    answer_in_high_sparsity_phase: 0.627\n    note: Phase segmentation based on dense model — 4 sparsity conditions share identical\n      phase boundaries, effective sample n=48 not n=192\n- id: c2_acc_qw_s030_n100\n  claim: C2\n  description: QW importance s030 accuracy=0.19 (n=100); dose-response monotonic decline\n    from dense=0.40\n  registry_id: acc_qw_s030_n100\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics:\n    batch1_correct: 7\n    batch1_total: 50\n    batch1_acc: 0.14\n    batch1_source: acc_qw_s030_b1_8k (v2, 8k tokens)\n    batch2_correct: 12\n    batch2_total: 50\n    batch2_acc: 0.24\n    combined_correct: 19\n    combined_total: 100\n    combined_acc: 0.19\n- id: c2_acc_ds_s015_8k_v2\n  claim: C2\n  description: DS s015 accuracy=0.48 vs dense=0.74; early onset of compound degradation\n  registry_id: acc_ds_s015_8k_v2\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.48\n    correct: 24\n    total: 50\n    truncation_rate: 0.32\n    truncated_count: 16\n    non_truncated_accuracy: 0.706\n    non_truncated_correct: 24\n    non_truncated_total: 34\n    wall_time_s: 3967\n    max_new_tokens: 8192\n- id: c3_v6_importance_s025\n  claim: C3\n  description: 'Importance: II low_median=24.16 >> high_median=0.66; strong phase\n    gradient (36x ratio)'\n  registry_id: v6_importance_s025\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 0.6641\n    ii_mid_median: 5.3067\n    ii_low_median: 24.1619\n    ii_high_mean: 0.8842\n    ii_mid_mean: 10.057\n    ii_low_mean: 71.8854\n    per_problem_ii_count: 50\n    n_high: 42\n    n_mid: 23\n    n_low: 21\n    problems: 50\n    bootstrap_gradient_paired: 35.72\n    bootstrap_ci_paired:\n    - 9.52\n    - 101.54\n    bootstrap_gradient_unpaired: 36.38\n    bootstrap_ci_unpaired:\n    - 13.19\n    - 97.61\n    bootstrap_p: 0\n- id: c3_v6_random_s025\n  claim: C3\n  description: 'Random: II low_median=2.91 ~ high_median=3.00; flat phase gradient\n    (bootstrap_p=0.559)'\n  registry_id: v6_random_s025\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 3.0024\n    ii_mid_median: 2.9846\n    ii_low_median: 2.9146\n    ii_high_mean: 3.9052\n    ii_mid_mean: 7.9491\n    ii_low_mean: 3.9114\n    per_problem_ii_count: 50\n    n_high: 36\n    n_mid: 25\n    n_low: 24\n    bootstrap_gradient_paired: -0.1199\n    bootstrap_ci_paired:\n    - -1.517\n    - 1.2461\n    bootstrap_p: 0.559\n    bootstrap_gradient_unpaired: -0.8616\n    bootstrap_ci_unpaired:\n    - -3.3911\n    - 1.5169\n    per_problem_ii_stats:\n      high:\n        min: -6.1388\n        max: 25.2471\n        mean: 4.4098\n        median: 3.0421\n        std: 6.0734\n      mid:\n        min: 0.158\n        max: 108.7242\n        mean: 7.5626\n        median: 2.1407\n        std: 20.926\n      low:\n        min: -0.1953\n        max: 12.8555\n        mean: 3.5806\n        median: 2.7289\n        std: 3.4915\n    verdict: FAIL\n- id: c3_bf16_importance_s020\n  claim: C3\n  description: 'Importance: II low=1.50, mid=0.20, high=0.015 (median); clear phase\n    separation'\n  registry_id: bf16_importance_s020\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics: &id002\n    interaction_index:\n      high:\n        mean: 0.1289\n        median: 0.0145\n        ci:\n        - -0.1975\n        - 0.6647\n        winsorized_mean: -0.0297\n        skewness: 16.67\n      mid:\n        mean: 1.2604\n        median: 0.2027\n        ci:\n        - 0.7466\n        - 1.8962\n        winsorized_mean: 0.766\n        skewness: 7.05\n      low:\n        mean: 6.0288\n        median: 1.4963\n        ci:\n        - 4.4671\n        - 7.9237\n        winsorized_mean: 4.3426\n        skewness: 6.01\n    per_problem_ii_stats:\n      high:\n        n: 49\n        min: -0.1884\n        max: 0.4196\n        mean: 0.0025\n        median: 0.0036\n        std: 0.0966\n      mid:\n        n: 40\n        min: -0.0519\n        max: 8.6969\n        mean: 0.6795\n        median: 0.1977\n        std: 1.4998\n      low:\n        n: 50\n        min: -1.6151\n        max: 22.6875\n        mean: 2.2301\n        median: 1.128\n        std: 4.3758\n    gradient_paired_aggregate_legacy: 5.9\n    median_difference: 1.4818\n    n_problems: 50\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: false\n      overall: PASS\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    perplexity:\n      high:\n        dense: 1.1689\n        attn: 1.5233\n        kv: 1.6191\n        both: 2.1047\n      mid:\n        dense: 1.2269\n        attn: 1.5375\n        kv: 3.5164\n        both: 5.4246\n      low:\n        dense: 1.2286\n        attn: 1.6486\n        kv: 15.7987\n        both: 23.74\n- id: c3_bf16_ds_rand_s020\n  claim: C3\n  description: 'Random: II high=0.292, mid=0.350, low=0.276 (median); no phase separation'\n  registry_id: bf16_ds_rand_s020\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 1.1216\n        median: 0.2918\n        ci:\n        - 0.0796\n        - 2.5834\n        median_ci:\n        - 0.1598\n        - 0.4581\n        winsorized_mean: 1.7664\n        skewness: 9.59\n      mid:\n        mean: -1.5827\n        median: 0.3504\n        ci:\n        - -6.0963\n        - 1.5735\n        median_ci:\n        - 0.1993\n        - 0.5226\n        winsorized_mean: 0.5839\n        skewness: -12.31\n      low:\n        mean: -0.4116\n        median: 0.2763\n        ci:\n        - -2.6034\n        - 1.209\n        median_ci:\n        - 0.2194\n        - 0.5487\n        winsorized_mean: 0.9942\n        skewness: -10.07\n    perplexity:\n      high:\n        dense: 1.1687\n        attn: 3.1905\n        kv: 3.8002\n        both: 8.8129\n      mid:\n        dense: 1.2269\n        attn: 67.8504\n        kv: 3.788\n        both: 11.4974\n      low:\n        dense: 1.2284\n        attn: 8.592\n        kv: 5.0078\n        both: 9.2001\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    n_problems: 50\n    pass_fail:\n      ci_overlap: false\n      sign_reversal: false\n      overall: FAIL\n    median_difference: -0.0155\n- id: c4_c4_entropy\n  claim: C4\n  description: 'DS importance entropy_delta: -0.04 to -0.05 (collapse); random: +0.13\n    to +0.23 (redistribution). Gini_delta: -0.03 to -0.08'\n  registry_id: c4_entropy\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics:\n    importance_entropy_delta:\n      s015: -0.0402\n      s020: -0.0472\n      s025: -0.0446\n      s030: -0.0436\n    random_entropy_delta:\n      s015: 0.1283\n      s020: 0.136\n      s025: 0.2171\n      s030: 0.2327\n    importance_gini_delta:\n      s015: -0.0301\n      s020: -0.0404\n      s025: -0.0647\n      s030: -0.0806\n    random_gini_delta:\n      s015: -0.0309\n      s020: -0.0403\n      s025: -0.062\n      s030: -0.0732\n    importance_cv_delta:\n      s015: -0.564\n      s020: -0.774\n      s025: -1.287\n      s030: -1.665\n    random_cv_delta:\n      s015: -1.021\n      s020: -1.203\n      s025: -1.923\n      s030: -2.137\n    problems_completed: 30\n    runtime_minutes: 69.1\n- id: c4_qwen_c4_entropy\n  claim: C4\n  description: 'QW importance entropy_delta mixed: s015=-0.073, s025=+0.045; Gini\n    weaker (-0.01 to -0.02). Model-dependent pattern'\n  registry_id: qwen_c4_entropy\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: negative\n  metrics:\n    problems_completed: 30\n    qwen_importance_entropy_delta:\n      s015: -0.0733\n      s020: -0.0759\n      s025: 0.0451\n      s030: -0.0072\n    qwen_random_entropy_delta:\n      s015: 0.0838\n      s020: 0.0901\n      s025: 0.2168\n      s030: 0.1968\n    qwen_importance_gini_delta:\n      s015: -0.0103\n      s020: -0.0121\n      s025: -0.01\n      s030: -0.0202\n    qwen_random_gini_delta:\n      s015: -0.0186\n      s020: -0.0229\n      s025: -0.0337\n      s030: -0.0448\n    qwen_importance_cv_delta:\n      s015: -0.045\n      s020: -0.208\n      s025: -1.491\n      s030: -1.142\n    qwen_random_cv_delta:\n      s015: -0.778\n      s020: -0.889\n      s025: -1.5\n      s030: -1.677\n    cross_model_notes: random entropy increase consistent; importance entropy collapse\n      inconsistent at s025 (reversed to +0.045) and near-zero at s030; gini/cv directions\n      consistent but Qwen magnitudes smaller\n- id: c5_bf16_qw_imp_s030\n  claim: C5\n  description: 'Qwen: median_diff=2.619, Cohen''s d=1.439, p<1e-5; replicates DeepSeek\n    pattern'\n  registry_id: bf16_qw_imp_s030\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics:\n    median_difference: 2.619385\n    permutation_p: 0\n    cohens_d: 1.4394\n    bootstrap_ci_95:\n    - 1.722281\n    - 3.651063\n    wilcoxon_p: 0\n    n_bootstrap: 10000\n    n_paired: 46\n- id: c5_bf16_importance_s030\n  claim: C5\n  description: 'DeepSeek: II low_median=14.64, high_median=0.053; strong phase gradient'\n  registry_id: bf16_importance_s030\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics: *id001\n- id: c5_c2_n500_deepseek\n  claim: C5\n  description: 'DS n=500: imp_s030 median_II=8.48, CI=[7.46,9.56], p=1.3e-78; robust\n    at scale'\n  registry_id: c2_n500_deepseek\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics: &id004\n    n_problems: 500\n    effective_n: 496\n    mid_null_rate: 0.102\n    imp_s015_median_ii: 0.3907\n    imp_s015_ci:\n    - 0.3496\n    - 0.4431\n    imp_s015_wilcoxon_p: 1.27e-70\n    imp_s020_median_ii: 1.2149\n    imp_s020_ci:\n    - 1.1072\n    - 1.3365\n    imp_s020_wilcoxon_p: 3.98e-75\n    imp_s025_median_ii: 3.9857\n    imp_s025_ci:\n    - 3.5272\n    - 4.3588\n    imp_s025_wilcoxon_p: 1.99e-78\n    imp_s030_median_ii: 8.4813\n    imp_s030_ci:\n    - 7.7543\n    - 9.6919\n    imp_s030_wilcoxon_p: 1.09e-79\n    rand_s015_median_ii: 0.0139\n    rand_s015_wilcoxon_p: 0.863\n    rand_s020_median_ii: 0.0315\n    rand_s020_wilcoxon_p: 0.28\n    rand_s025_median_ii: 0.2574\n    rand_s025_bonf_p: 0.005839\n    rand_s025_fdr_p: 0.001914\n    rand_s030_median_ii: 0.5096\n    rand_s030_bonf_p: 0.005903\n    rand_s030_fdr_p: 0.001914\n    dz_s015_s020: -0.925\n    dz_s020_s025: -0.824\n    dz_s025_s030: -0.773\n    dz_s015_s030: -0.944\n    all_dz_reliable: true\n    dose_response_monotonic: true\n    dose_response_spearman_rho: 1\n    dose_response_perm_p: 0.0417\n    imp_rand_ratio_range: 15.5-38.6x\n    bonferroni_k: 4\n    bonferroni_note: Bonferroni k=4 family-wise (D066 revision)\n- id: c5_c2_qw_n500_r3\n  claim: C5\n  description: 'QW n=500: imp_s030 median_II=4.33, p<1e-40; cross-model replication\n    at high power'\n  registry_id: c2_qw_n500_r3\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics: &id005\n    n_problems: 500\n    effective_n: 475\n    filter: low+high valid only (mid-null allowed)\n    mid_null_rate: 0.452\n    imp_s015_median_ii: 0.0659\n    imp_s015_ci:\n    - 0.0492\n    - 0.0925\n    imp_s015_wilcoxon_p: 8.66e-15\n    imp_s015_bonf_p: 3.46e-14\n    imp_s020_median_ii: 0.3073\n    imp_s020_ci:\n    - 0.2612\n    - 0.3564\n    imp_s020_wilcoxon_p: 6.84e-42\n    imp_s020_bonf_p: 2.74e-41\n    imp_s025_median_ii: 1.0745\n    imp_s025_ci:\n    - 0.9766\n    - 1.1787\n    imp_s025_wilcoxon_p: 1.06e-68\n    imp_s025_bonf_p: 4.25e-68\n    imp_s030_median_ii: 3.155\n    imp_s030_ci:\n    - 2.7834\n    - 3.5582\n    imp_s030_wilcoxon_p: 9.21e-74\n    imp_s030_bonf_p: 3.69e-73\n    rand_s015_median_ii: -0.0111\n    rand_s015_wilcoxon_p: 0.172\n    rand_s015_bonf_p: 0.687\n    rand_s020_median_ii: 0.0153\n    rand_s020_wilcoxon_p: 0.2\n    rand_s020_bonf_p: 0.8\n    rand_s025_median_ii: 0.3931\n    rand_s025_wilcoxon_p: 1.59e-11\n    rand_s025_bonf_p: 6.37e-11\n    rand_s025_fdr_p: 2.63e-11\n    rand_s030_median_ii: 0.9127\n    rand_s030_wilcoxon_p: 2.92e-15\n    rand_s030_bonf_p: 1.17e-14\n    rand_s030_fdr_p: 5.61e-15\n    dz_s015_s020: -0.629\n    dz_s020_s025: -0.865\n    dz_s025_s030: -0.767\n    dz_s015_s030: -0.923\n    all_dz_reliable: true\n    dose_response_monotonic: true\n    dose_response_spearman_rho: 1\n    dose_response_perm_p: 0.0417\n    imp_rand_ratio_range: 2.7-20.1x\n    bonferroni_k: 4\n    bonferroni_note: Bonferroni k=4 family-wise (D066 revision)\n- id: c5b_c5b_pilot\n  claim: C5b\n  description: 'Oracle recovery=18% (gate: >30% FAIL); heuristic recovery=31.7% but\n    CI crosses zero. s030 incomplete'\n  registry_id: c5b_pilot\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: negative\n  metrics:\n    s025_uniform_median_ii: 1.0435\n    s025_oracle_median_ii: 0.856\n    s025_oracle_recovery_pct: 18\n    s025_oracle_recovery_ci:\n    - -39\n    - 45.8\n    s025_oracle_wilcoxon_p: 0.0021\n    s025_heuristic_median_ii: 0.7127\n    s025_heuristic_recovery_pct: 31.7\n    s025_heuristic_recovery_ci:\n    - -22.8\n    - 66\n    s025_heuristic_wilcoxon_p: 0.0236\n    gate_criterion: oracle_recovery > 30%\n    gate_result: FAIL\n    s030_status: not_completed\n    n_problems: 30\n- id: c6_bf16_importance_s015\n  claim: C6\n  description: II low_median=0.398 at s=0.15\n  registry_id: bf16_importance_s015\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: -0.150213\n        median: 0.005752\n        ci:\n        - -0.294614\n        - -0.055385\n        winsorized_mean: -0.062378\n        skewness: -14.9912\n      mid:\n        mean: 0.447301\n        median: 0.080738\n        ci:\n        - 0.267993\n        - 0.668749\n        winsorized_mean: 0.324751\n        skewness: 4.7221\n      low:\n        mean: 2.405837\n        median: 0.398291\n        ci:\n        - 1.478784\n        - 3.667675\n        winsorized_mean: 1.278857\n        skewness: 9.5402\n    per_problem_ii_stats:\n      high:\n        n: 49\n        min: -0.188061\n        max: 0.335853\n        mean: -0.013405\n        median: 0.00012\n        std: 0.078483\n      mid:\n        n: 40\n        min: -0.169092\n        max: 3.88198\n        mean: 0.308621\n        median: 0.107114\n        std: 0.690186\n      low:\n        n: 50\n        min: -0.872983\n        max: 9.10289\n        mean: 0.725504\n        median: 0.315517\n        std: 1.731056\n    gradient_paired_aggregate_legacy: 69.24\n    median_difference: 0.3925\n    n_problems: 50\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: true\n      overall: PASS\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    perplexity:\n      high:\n        dense: 1.1689\n        attn: 1.4861\n        kv: 1.4481\n        both: 1.5911\n      mid:\n        dense: 1.2269\n        attn: 1.5137\n        kv: 2.5971\n        both: 3.4541\n      low:\n        dense: 1.2286\n        attn: 1.6147\n        kv: 8.9201\n        both: 12.5084\n- id: c6_bf16_importance_s020\n  claim: C6\n  description: II low_median=1.496 at s=0.20\n  registry_id: bf16_importance_s020\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics: *id002\n- id: c6_bf16_importance_s025\n  claim: C6\n  description: II low_median=7.196 at s=0.25\n  registry_id: bf16_importance_s025\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics: *id003\n- id: c6_bf16_importance_s030\n  claim: C6\n  description: II low_median=14.64 at s=0.30; growth 0.40->1.50->7.20->14.64 is sub-exponential\n  registry_id: bf16_importance_s030\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics: *id001\n- id: c7_c2_n500_deepseek\n  claim: C7\n  description: 'DS n=500: all 4 sparsities significant (p<1e-70); CIs non-overlapping\n    across dose levels'\n  registry_id: c2_n500_deepseek\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics: *id004\n- id: c7_c2_qw_n500_r3\n  claim: C7\n  description: 'QW n=500: all 4 sparsities significant (p<1e-14 Bonferroni-corrected);\n    mid_null_rate=45.2%'\n  registry_id: c2_qw_n500_r3\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics: *id005\n- id: c8_c3_llama\n  claim: C8\n  description: LLaMA-8B (LlamaForCausalLM) replicates phase-modulated compound severity\n    from Qwen2ForCausalLM\n  registry_id: c3_llama\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics:\n    model: DeepSeek-R1-Distill-Llama-8B\n    n_problems: 50\n    n_valid: 49\n    n_skipped: 1\n    conditions_completed: 8/8\n    n_bootstrap: 10000\n    bonferroni_k: 4\n    imp_vs_rand_dz:\n      s015: 0.1923\n      s020: 0.255\n      s025: 0.2902\n      s030: 0.3352\n    imp_vs_rand_dz_ci:\n      s015:\n      - -0.0862\n      - 0.496\n      s020:\n      - -0.0248\n      - 0.5381\n      s025:\n      - 0.0081\n      - 0.6121\n      s030:\n      - 0.0606\n      - 0.6629\n    imp_vs_rand_dz_interpretation:\n      s015: negligible\n      s020: small\n      s025: small\n      s030: small\n    imp_vs_rand_dz_monotonic: true\n    phase_gradient_importance_dz:\n      s015: 1.0079\n      s020: 1.108\n      s025: 1.1227\n      s030: 1.0038\n    phase_gradient_importance_dz_ci:\n      s015:\n      - 0.593\n      - 1.7025\n      s020:\n      - 0.8144\n      - 1.5698\n      s025:\n      - 0.8735\n      - 1.5768\n      s030:\n      - 0.8099\n      - 1.3519\n    phase_gradient_importance_interpretation: all_large\n    phase_gradient_random_dz:\n      s015: 0.3497\n      s020: 0.373\n      s025: 0.4476\n      s030: 0.4385\n    phase_gradient_random_dz_ci:\n      s015:\n      - 0.0665\n      - 0.6916\n      s020:\n      - 0.0868\n      - 0.7335\n      s025:\n      - 0.1669\n      - 0.7698\n      s030:\n      - 0.1966\n      - 0.707\n    phase_gradient_random_interpretation: all_small\n    median_diff:\n      s015: 0.0203\n      s020: 0.0221\n      s025: 0.0947\n      s030: 0.3562\n    median_diff_ci:\n      s015:\n      - 0.0016\n      - 0.0435\n      s020:\n      - -0.0905\n      - 0.187\n      s025:\n      - -0.0037\n      - 0.3029\n      s030:\n      - -0.0691\n      - 0.5442\n    wilcoxon_p:\n      s015: 0.0549\n      s020: 0.0632\n      s025: 0.0209\n      s030: 0.0074\n    wilcoxon_p_bonferroni:\n      s015: 0.2195\n      s020: 0.2527\n      s025: 0.0834\n      s030: 0.0294\n    significant_bonferroni:\n      s015: false\n      s020: false\n      s025: false\n      s030: true\n    cross_arch_comparison:\n      deepseek_importance_dz:\n        s015: 0.4416\n        s020: 0.5195\n        s025: 0.6831\n        s030: 0.8031\n      llama_importance_dz:\n        s015: 1.0079\n        s020: 1.108\n        s025: 1.1227\n        s030: 1.0038\n      delta:\n        s015: 0.5663\n        s020: 0.5885\n        s025: 0.4396\n        s030: 0.2007\n      note: LLaMA shows uniformly large d_z (all >1.0) vs DeepSeek medium-to-large\n- id: c10_gsm8k_profiling_ds\n  claim: C10\n  description: 'DS GSM8K importance gradient: s015=0.241, s020=0.740, s025=1.992,\n    s030=4.636 (monotonic)'\n  registry_id: gsm8k_profiling_ds\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics:\n    version: v3_median\n    n_problems: 50\n    method: median + Wilcoxon + bootstrap_median(B=10000)\n    importance:\n      s015:\n        median_gradient: 0.241\n        ci_low: 0.077\n        ci_high: 0.478\n        wilcoxon_p: 0.0003\n      s020:\n        median_gradient: 0.74\n        ci_low: 0.314\n        ci_high: 1.119\n        wilcoxon_p: 0.0001\n      s025:\n        median_gradient: 1.992\n        ci_low: 0.933\n        ci_high: 2.82\n        wilcoxon_p: 0.0001\n      s030:\n        median_gradient: 4.682\n        ci_low: 2.121\n        ci_high: 10.557\n        wilcoxon_p: 0.0001\n    imp_rand_ratio:\n      s015: 2.3\n      s020: 2.5\n      s025: 3.8\n      s030: 2.8\n    dose_response_monotonic: true\n- id: c10_gsm8k_profiling_qw\n  claim: C10\n  description: 'QW GSM8K importance gradient: s015=0.039, s020=0.158, s025=1.100,\n    s030=2.092 (monotonic)'\n  registry_id: gsm8k_profiling_qw\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics:\n    version: v3_median\n    n_problems: 50\n    method: median + Wilcoxon + bootstrap_median(B=10000)\n    importance:\n      s015:\n        median_gradient: 0.039\n      s020:\n        median_gradient: 0.158\n      s025:\n        median_gradient: 1.1\n      s030:\n        median_gradient: 2.092\n    qw_rand_s030: INVALID\n- id: c10_gsm8k_qw_rand_s025_v2\n  claim: C10\n  description: 'QW random s025 GSM8K: II median_high=0.72, low=1.48; phase gradient\n    weaker than importance'\n  registry_id: gsm8k_qw_rand_s025_v2\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics:\n    verdict: PASS\n    n_problems: 50\n    n_bootstrap: 1000\n    seed: 42\n    high_sparsity:\n      n_segments: 216\n      n_tokens: 9326\n      ppl_dense: 1.0695\n      ppl_attn: 5.9362\n      ppl_kv: 3.4316\n      ppl_both: 15.7484\n      ii_mean: 6.5954\n      ii_ci:\n      - 1.1114\n      - 11.3791\n      ii_median: 0.7176\n      ii_median_ci:\n      - 0.5959\n      - 0.9347\n      winsorized_mean: 6.5046\n      skewness: -4.6807\n      outlier_count: 3\n    low_sparsity:\n      n_segments: 252\n      n_tokens: 29224\n      ppl_dense: 1.1972\n      ppl_attn: 11.5347\n      ppl_kv: 5.6038\n      ppl_both: 21.6874\n      ii_mean: 2.3883\n      ii_ci:\n      - -8.4602\n      - 11.029\n      ii_median: 1.4587\n      ii_median_ci:\n      - 1.1121\n      - 2.0451\n      winsorized_mean: 5.8911\n      skewness: -7.6074\n      outlier_count: 4\n    mid_sparsity:\n      n_segments: 51\n      n_tokens: 5954\n      ppl_dense: 1.2601\n      ppl_attn: 13.4132\n      ppl_kv: 6.4841\n      ppl_both: 20.8714\n      ii_mean: 4.5407\n      ii_ci:\n      - -4.8854\n      - 12.4605\n      ii_median: 1.1272\n      ii_median_ci:\n      - 0.637\n      - 3.3729\n      winsorized_mean: 6.3284\n      skewness: -3.4048\n      outlier_count: 1\n- id: c10_gsm8k_qw_rand_s030_v2\n  claim: C10\n  description: 'QW random s030 GSM8K: II median_high=2.31, low=5.87; compound effect\n    on GSM8K confirmed'\n  registry_id: gsm8k_qw_rand_s030_v2\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics:\n    verdict: PASS\n    n_problems: 50\n    n_bootstrap: 1000\n    seed: 42\n    high_sparsity:\n      n_segments: 216\n      n_tokens: 9326\n      null_ratio: 2/50\n      ppl_dense: 1.0695\n      ppl_attn: 6.5613\n      ppl_kv: 4.481\n      ppl_both: 23.7486\n      ii_mean: 11.83\n      ii_median: 2.31\n      ii_ci:\n      - 6.17\n      - 17.04\n      ii_median_ci:\n      - 1.64\n      - 2.81\n      winsorized_mean: 10.55\n      skewness: -2.29\n      outlier_count: 7\n    low_sparsity:\n      n_segments: 252\n      n_tokens: 29224\n      null_ratio: 5/50\n      ppl_dense: 1.1972\n      ppl_attn: 6.3283\n      ppl_kv: 8.5374\n      ppl_both: 56.2304\n      ii_mean: 31.26\n      ii_median: 5.2\n      ii_ci:\n      - 17.84\n      - 47.86\n      ii_median_ci:\n      - 3.95\n      - 7.24\n      winsorized_mean: 16.35\n      skewness: 7.57\n      outlier_count: 4\n    mid_sparsity:\n      n_segments: 51\n      n_tokens: 5954\n      null_ratio: 17/50\n      ppl_dense: 1.2601\n      ppl_attn: 18.6162\n      ppl_kv: 11.6625\n      ppl_both: 47.9019\n      ii_mean: 18.02\n      ii_median: 2.7\n      ii_ci:\n      - 0.09\n      - 36.69\n      ii_median_ci:\n      - 1.46\n      - 8.77\n      winsorized_mean: 18.22\n      skewness: 0.43\n      outlier_count: 2\n- id: s3_c_bf16_ds_imp_s010\n  claim: S3->C\n  description: 'DS s=0.10: II_high_median=0.003, verdict=FAIL; below onset threshold\n    for DeepSeek'\n  registry_id: bf16_ds_imp_s010\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: negative\n  metrics:\n    verdict: FAIL\n    problems: 50\n    II_high_sparsity_median: 0.0027\n    II_high_sparsity_mean: -0.1998\n    II_low_sparsity_median: 0.0151\n    II_low_sparsity_mean: -0.1066\n    II_mid_sparsity_median: 0.0061\n    II_mid_sparsity_mean: -0.0131\n    high_sparsity_tokens: 21086\n    low_sparsity_tokens: 27748\n    mid_sparsity_tokens: 13306\n- id: s3_c_bf16_qw_imp_s010\n  claim: S3->C\n  description: 'QW s=0.10: overall_verdict=PASS, CI_overlap_test=PASS; Qwen onset\n    earlier than DeepSeek'\n  registry_id: bf16_qw_imp_s010\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics:\n    n_problems: 50\n    overall_verdict: PASS\n    ci_overlap_test: PASS\n    sign_reversal_test: FAIL\n    high_sparsity_II_median: 0.0001\n    high_sparsity_II_median_CI:\n    - -0.0028\n    - 0.0005\n    high_sparsity_II_mean: -0.0887\n    high_sparsity_II_mean_CI:\n    - -0.1235\n    - -0.0591\n    low_sparsity_II_median: -0.0444\n    low_sparsity_II_median_CI:\n    - -0.0967\n    - -0.0152\n    low_sparsity_II_mean: -0.2431\n    low_sparsity_II_mean_CI:\n    - -0.3817\n    - -0.1202\n    mid_sparsity_II_median: -0.0359\n    mid_sparsity_II_median_CI:\n    - -0.0963\n    - -0.015\n    mid_sparsity_II_mean: -0.084\n    mid_sparsity_II_mean_CI:\n    - -0.1366\n    - -0.035\n    ppl_high_dense: 1.074\n    ppl_high_both: 1.228\n    ppl_low_dense: 1.152\n    ppl_low_both: 3.204\n    ppl_mid_dense: 1.133\n    ppl_mid_both: 1.741\n- id: s3_c_bf16_qw_imp_s015\n  claim: S3->C\n  description: 'QW s=0.15: median_diff=0.048, permutation_p=0.0001; confirmed above\n    threshold'\n  registry_id: bf16_qw_imp_s015\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics:\n    median_difference: 0.047619\n    permutation_p: 0.0001\n    cohens_d: 0.3705\n    bootstrap_ci_95:\n    - -0.005077\n    - 0.109517\n    wilcoxon_p: 0.02958\n    n_bootstrap: 10000\n    n_paired: 46\n- id: s7_c_c2_n500_deepseek\n  claim: S7->C\n  description: 'DS n=500 monotonic: imp median II 0.39->1.21->3.99->8.48 across s015-s030\n    (Spearman rho=1.0)'\n  registry_id: c2_n500_deepseek\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics: *id004\n- id: s7_c_c2_qw_n500_r3\n  claim: S7->C\n  description: 'QW n=500 monotonic: imp median II 0.066->0.307->1.075->4.33 across\n    s015-s030 (Spearman rho=1.0)'\n  registry_id: c2_qw_n500_r3\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics: *id005\n- id: s7_c_bf16_qw_imp_s035\n  claim: S7->C\n  description: 'QW s=0.35: low_II_median=8.24; extends dose-response beyond s030'\n  registry_id: bf16_qw_imp_s035\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics:\n    n_problems: 50\n    overall_verdict: PASS\n    ci_overlap_test: PASS\n    sign_reversal_test: FAIL\n    high_sparsity_II_median: 0.0232\n    high_sparsity_II_median_CI:\n    - 0.0154\n    - 0.0383\n    high_sparsity_II_mean: 0.1643\n    high_sparsity_II_mean_CI:\n    - 0.0844\n    - 0.2495\n    low_sparsity_II_median: 8.2358\n    low_sparsity_II_median_CI:\n    - 6.1564\n    - 10.9231\n    low_sparsity_II_mean: 18.9673\n    low_sparsity_II_mean_CI:\n    - 14.5015\n    - 23.9752\n    mid_sparsity_II_median: 0.9577\n    mid_sparsity_II_median_CI:\n    - 0.171\n    - 3.5575\n    mid_sparsity_II_mean: 8.0734\n    mid_sparsity_II_mean_CI:\n    - 2.0224\n    - 16.8946\n    ppl_high_dense: 1.0738\n    ppl_high_both: 2.3435\n    ppl_low_dense: 1.1518\n    ppl_low_both: 58.0358\n    ppl_mid_dense: 1.1327\n    ppl_mid_both: 20.9912\n    high_sparsity_tokens: 16289\n    low_sparsity_tokens: 32227\n    mid_sparsity_tokens: 4372\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_interaction_index_profiling\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_ii_profiling_v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    mvp_verdict: PASS_technical_but_negative_hypothesis\n    ci_nonoverlap: true\n    sign_reversal: false\n    ii_reasoning_0.3: 17.79\n    ii_reasoning_0.3_ci:\n    - 4.09\n    - 38.76\n    ii_transition_0.3: 3.06\n    ii_transition_0.3_ci:\n    - 0.01\n    - 5.6\n    ii_reasoning_0.5: 468.9\n    ii_transition_0.5: 850.07\n    ii_execution_0.3: Inf\n    phase_distribution:\n      execution: 1.2%_25seg\n      reasoning: 8.1%_96seg\n      transition: 90.7%_192seg\n    total_tokens: 86207\n    all_ii_superadditive: true\n    amplitude_ratio_reas_vs_trans_0.3: 5.81\n    gmm_best_k: 5\n    gmm_means:\n    - 0.438\n    - 0.597\n    - 0.719\n    - 0.816\n    - 0.892\n    gmm_weights:\n    - 0.062\n    - 0.14\n    - 0.208\n    - 0.282\n    - 0.309\n    sparsity_global:\n      mean: 0.7653\n      std: 0.1364\n      median: 0.8004\n    quantile_boundaries:\n    - 0.7337\n    - 0.8482\n- exp_id: mvp_ii_profiling_v3\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    mvp_verdict: FAIL\n    ci_nonoverlap: false\n    sign_reversal: false\n    phase_distribution_balanced: true\n    ii_high_0.1:\n      mean: 0.2317\n      ci:\n      - 0.1338\n      - 0.3418\n    ii_low_0.1:\n      mean: 0.1711\n      ci:\n      - 0.0782\n      - 0.2768\n    ii_mid_0.1:\n      mean: 0.1607\n      ci:\n      - 0.0886\n      - 0.2489\n    ii_high_0.2:\n      mean: 2.1574\n      ci:\n      - 1.0605\n      - 3.5491\n    ii_low_0.2:\n      mean: 1.1294\n      ci:\n      - 0.4368\n      - 1.9593\n    ii_mid_0.2:\n      mean: 0.3049\n      ci:\n      - -1.0635\n      - 1.3044\n    total_tokens: 86207\n    no_nan_inf: true\n    segments:\n      high: 511\n      low: 454\n      mid: 391\n- exp_id: mvp_ii_profiling_v4\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_ii_profiling_v4b\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_ii_profiling_v4c\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_ii_profiling_v4d\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_ii_profiling_v4-random\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_v4a_r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_v4b_r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_v4c_r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_v4_random_r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp_v4_legacy_s01\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    II_high_0.1:\n      mean: -0.1097\n      ci_low: -0.8066\n      ci_high: 0.41\n    II_mid_0.1:\n      mean: -15.966\n      ci_low: -47.991\n      ci_high: 1.288\n    II_low_0.1:\n      mean: 0\n      ci_low: 0\n      ci_high: 0\n    ppl_high_dense: 1.1462\n    ppl_high_both: 22.1302\n    ppl_mid_dense: 1.1226\n    ppl_mid_both: 47.5856\n    verdict: FAIL\n- exp_id: mvp_v4_legacy_s02\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_0.2:\n      mean: 21.2856\n      ci:\n      - 0.0292\n      - 63.163\n    ii_mid_0.2:\n      mean: 21.8743\n      ci:\n      - 4.9863\n      - 41.785\n    ii_low_0.2:\n      mean: 0\n      ci:\n      - 0\n      - 0\n    ppl_high:\n      dense: 1.15\n      attn: 1.32\n      kv: 104.42\n      both: 63.41\n    ppl_mid:\n      dense: 1.12\n      attn: 1.29\n      kv: 324.16\n      both: 170.47\n    ppl_low:\n      dense: 1.11\n      attn: 1.3\n      kv: 1.11\n      both: 1.3\n    problems_completed: 50\n    phase_tokens:\n      high: 25862\n      mid: 27996\n      low: 32349\n    mvp_verdict: PASS\n- exp_id: mvp_v4_legacy_s03\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_0.3:\n      mean: -224.5\n      ci_crosses_zero: true\n    verdict: FAIL_ci_crosses_zero\n- exp_id: mvp_v4_legacy_s025\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_v4_legacy_s035\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_v4_float32_s030\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_v5_fixed_s020\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    ii_high: 0.5\n    ii_mid: 3.52\n    ii_low: 31.89\n    ii_high_ci:\n    - 0.41\n    - 0.62\n    ii_mid_ci:\n    - 2.29\n    - 5.35\n    ii_low_ci:\n    - 18.74\n    - 47.22\n    ii_high_median: 0.33\n    ii_mid_median: 1.55\n    ii_low_median: 9.56\n    kv_ppl_high: 1.24\n    kv_ppl_mid: 3.65\n    kv_ppl_low: 14.11\n    both_ppl_high: 2.7\n    both_ppl_mid: 8.13\n    both_ppl_low: 42.64\n    problems: 50\n    ⚠️_WARNING: pre-fix code, INVALIDATED. Results found on disk after kill but code\n      lacked conda activation fix. Do NOT cite these numbers.\n- exp_id: mvp_v5_fixed_s030\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    ii_high: 1.18\n    ii_mid: 168.53\n    ii_low: 1926.23\n    ii_high_ci:\n    - 0.86\n    - 1.6\n    ii_mid_ci:\n    - 36.91\n    - 348.21\n    ii_low_ci:\n    - 179.17\n    - 4062.57\n    ii_high_median: 0.6\n    ii_mid_median: 7.47\n    ii_low_median: 44.63\n    kv_ppl_high: 1.4\n    kv_ppl_mid: 15.11\n    kv_ppl_low: 40.79\n    both_ppl_high: 5.71\n    both_ppl_mid: 137.61\n    both_ppl_low: 963.2\n    problems: 50\n    ⚠️_WARNING: pre-fix code, INVALIDATED. Results found on disk after kill but code\n      lacked conda activation fix. Do NOT cite these numbers.\n- exp_id: mvp_v5_fixed_s015\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ii_high: 0.306\n    ii_mid: 1.274\n    ii_low: 8.786\n    ii_high_ci:\n    - 0.256\n    - 0.359\n    ii_mid_ci:\n    - 0.895\n    - 1.749\n    ii_low_ci:\n    - 5.294\n    - 12.684\n    ii_high_median: 0.205\n    ii_mid_median: 0.696\n    ii_low_median: 2.627\n    ii_high_winsorized: 0.289\n    ii_mid_winsorized: 1.139\n    ii_low_winsorized: 8.408\n    kv_ppl_high: 1.2147\n    kv_ppl_mid: 2.1276\n    kv_ppl_low: 6.7451\n    both_ppl_high: 2.2835\n    both_ppl_mid: 3.9408\n    both_ppl_low: 16.9987\n    problems: 50\n    segments: 1356\n- exp_id: mvp_v5_fixed_s025\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ii_high: 0.851\n    ii_mid: 9.306\n    ii_low: 96.715\n    ii_high_ci:\n    - 0.703\n    - 0.999\n    ii_mid_ci:\n    - 6.092\n    - 13.303\n    ii_low_ci:\n    - 59.642\n    - 143.188\n    ii_high_median: 0.584\n    ii_mid_median: 4.522\n    ii_low_median: 30.903\n    ii_high_winsorized: 0.802\n    ii_mid_winsorized: 8.156\n    ii_low_winsorized: 94.931\n    kv_ppl_high: 1.3108\n    kv_ppl_mid: 6.1778\n    kv_ppl_low: 23.8919\n    both_ppl_high: 3.4623\n    both_ppl_mid: 16.4148\n    both_ppl_low: 104.1749\n    problems: 50\n    segments: 1356\n- exp_id: mvp_v5_fixed_s020_r2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ii_high_median: 0.3333\n    ii_mid_median: 1.5479\n    ii_low_median: 9.5627\n    ii_high_mean: 0.5044\n    ii_mid_mean: 3.5155\n    ii_low_mean: 31.8937\n    ii_high_ci:\n    - 0.41\n    - 0.62\n    ii_mid_ci:\n    - 2.29\n    - 5.35\n    ii_low_ci:\n    - 18.74\n    - 47.22\n    kv_ppl_high: 1.24\n    kv_ppl_mid: 3.65\n    kv_ppl_low: 14.11\n    both_ppl_high: 2.7\n    both_ppl_mid: 8.13\n    both_ppl_low: 42.64\n    problems: 50\n- exp_id: mvp_v5_fixed_s030_r2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ii_high_median: 0.5964\n    ii_mid_median: 7.4671\n    ii_low_median: 44.6324\n    ii_high_mean: 1.1832\n    ii_mid_mean: 168.53\n    ii_low_mean: 1926.23\n    ii_high_ci:\n    - 0.86\n    - 1.6\n    ii_mid_ci:\n    - 36.91\n    - 348.21\n    ii_low_ci:\n    - 179.17\n    - 4062.57\n    kv_ppl_high: 1.4\n    kv_ppl_mid: 15.11\n    kv_ppl_low: 40.79\n    both_ppl_high: 5.71\n    both_ppl_mid: 137.61\n    both_ppl_low: 963.2\n    problems: 50\n- exp_id: mvp_v5_random_s015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 0.1606\n    ii_mid_median: 0.252\n    ii_low_median: 0.1831\n    ii_high_mean: 0.4563\n    ii_mid_mean: 0.5134\n    ii_low_mean: 0.4775\n    ii_high_ci:\n    - 0.12\n    - 0.77\n    ii_mid_ci:\n    - 0.34\n    - 0.74\n    ii_low_ci:\n    - 0.28\n    - 0.7\n    kv_ppl_high: 3.14\n    kv_ppl_mid: 2.91\n    kv_ppl_low: 3.61\n    both_ppl_high: 3.92\n    both_ppl_mid: 4.14\n    both_ppl_low: 4.71\n    problems: 50\n- exp_id: mvp_v5_random_s025\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 3.0024\n    ii_mid_median: 2.9846\n    ii_low_median: 2.9146\n    ii_high_mean: 3.9052\n    ii_mid_mean: 7.9491\n    ii_low_mean: 3.9114\n    ii_high_ci:\n    - 0.98\n    - 6.34\n    ii_mid_ci:\n    - 4.67\n    - 11.87\n    ii_low_ci:\n    - 2.71\n    - 5.24\n    kv_ppl_high: 6.39\n    kv_ppl_mid: 6.11\n    kv_ppl_low: 9.07\n    both_ppl_high: 17.06\n    both_ppl_mid: 15.38\n    both_ppl_low: 29.32\n    problems: 50\n- exp_id: mvp_v5_random_s020\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 0.321331\n    ii_mid_median: 0.455663\n    ii_low_median: 0.591916\n    ii_high_mean: 0.855584\n    ii_mid_mean: 1.258123\n    ii_low_mean: 0.956933\n    ii_high_ci:\n    - -0.124133\n    - 1.616883\n    ii_mid_ci:\n    - 0.674852\n    - 2.075565\n    ii_low_ci:\n    - 0.583856\n    - 1.413355\n    kv_ppl_high: 4.2537\n    kv_ppl_mid: 4.3064\n    kv_ppl_low: 5.4048\n    both_ppl_high: 7.9749\n    both_ppl_mid: 6.8553\n    both_ppl_low: 22.5868\n    problems: 50\n- exp_id: mvp_v5_random_s030\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 5.377512\n    ii_mid_median: 5.886454\n    ii_low_median: 3.776818\n    ii_high_mean: 22.734534\n    ii_mid_mean: 10.943319\n    ii_low_mean: 11.840449\n    ii_high_ci:\n    - 10.352118\n    - 42.551951\n    ii_mid_ci:\n    - 7.398611\n    - 14.765315\n    ii_low_ci:\n    - 4.097309\n    - 23.545273\n    kv_ppl_high: 8.1027\n    kv_ppl_mid: 8.5701\n    kv_ppl_low: 13.4922\n    both_ppl_high: 41.3452\n    both_ppl_mid: 24.1992\n    both_ppl_low: 68.5301\n    problems: 50\n- exp_id: v6_importance_s025\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 0.6641\n    ii_mid_median: 5.3067\n    ii_low_median: 24.1619\n    ii_high_mean: 0.8842\n    ii_mid_mean: 10.057\n    ii_low_mean: 71.8854\n    per_problem_ii_count: 50\n    n_high: 42\n    n_mid: 23\n    n_low: 21\n    problems: 50\n    bootstrap_gradient_paired: 35.72\n    bootstrap_ci_paired:\n    - 9.52\n    - 101.54\n    bootstrap_gradient_unpaired: 36.38\n    bootstrap_ci_unpaired:\n    - 13.19\n    - 97.61\n    bootstrap_p: 0\n- exp_id: v6_importance_s030\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 0.8833\n    ii_mid_median: 7.2706\n    ii_low_median: 34.6937\n    ii_high_mean: 1.5151\n    ii_mid_mean: 78.8215\n    ii_low_mean: 1163.9677\n    per_problem_ii_count: 50\n    n_high: 40\n    n_mid: 22\n    n_low: 20\n    problems: 50\n    bootstrap_gradient_paired: 41.92\n    bootstrap_ci_paired:\n    - 19.14\n    - 299.76\n    bootstrap_gradient_unpaired: 39.28\n    bootstrap_ci_unpaired:\n    - 21.87\n    - 129.59\n    bootstrap_p: 0\n- exp_id: v6_importance_s015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 0.2266\n    ii_mid_median: 0.7432\n    ii_low_median: 2.8762\n    ii_high_mean: 0.2874\n    ii_mid_mean: 1.6858\n    ii_low_mean: 8.5161\n    per_problem_ii_count: 50\n    n_high: 43\n    n_mid: 32\n    n_low: 24\n    problems: 50\n    bootstrap_gradient_paired: 11.53\n    bootstrap_ci_paired:\n    - 3.49\n    - 23.78\n    bootstrap_gradient_unpaired: 12.69\n    bootstrap_ci_unpaired:\n    - 4.96\n    - 28.45\n    bootstrap_p: 0\n- exp_id: v6_importance_s020\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 0.3353\n    ii_mid_median: 1.6733\n    ii_low_median: 9.2538\n    ii_high_mean: 0.4936\n    ii_mid_mean: 4.9538\n    ii_low_mean: 25.8764\n    per_problem_ii_count: 50\n    n_high: 42\n    n_mid: 28\n    n_low: 21\n    problems: 50\n    bootstrap_gradient_paired: 11.05\n    bootstrap_ci_paired:\n    - 5.42\n    - 69.27\n    bootstrap_gradient_unpaired: 27.6\n    bootstrap_ci_unpaired:\n    - 6.55\n    - 75.16\n    bootstrap_p: 0\n- exp_id: qwen_importance_s015\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: qwen_importance_s020\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: qwen_importance_s025\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: qwen_importance_s030\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: v6_random_s015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 0.1606\n    ii_mid_median: 0.252\n    ii_low_median: 0.1831\n    ii_high_mean: 0.4563\n    ii_mid_mean: 0.5134\n    ii_low_mean: 0.4775\n    per_problem_ii_count: 50\n    n_high: 43\n    n_mid: 32\n    n_low: 28\n    bootstrap_gradient_paired: -0.2722\n    bootstrap_ci_paired:\n    - -0.7039\n    - 0.1548\n    bootstrap_p: 0.903\n    bootstrap_gradient_unpaired: -0.0592\n    bootstrap_ci_unpaired:\n    - -0.5341\n    - 0.3877\n    per_problem_ii_stats:\n      high:\n        min: -3.0621\n        max: 5.018\n        mean: 0.5386\n        median: 0.2003\n        std: 1.2085\n      mid:\n        min: -2.7245\n        max: 4.6713\n        mean: 0.3977\n        median: 0.299\n        std: 1.1456\n      low:\n        min: -0.4031\n        max: 3.7005\n        mean: 0.4806\n        median: 0.2465\n        std: 0.779\n    verdict: FAIL\n- exp_id: v6_random_s020\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_mean: 0.855584\n    ii_high_median: 0.321331\n    ii_high_ci:\n    - -0.124133\n    - 1.616883\n    ii_high_winsorized_mean: 0.913496\n    ii_mid_mean: 1.258123\n    ii_mid_median: 0.455663\n    ii_mid_ci:\n    - 0.674852\n    - 2.075565\n    ii_mid_winsorized_mean: 1.074102\n    ii_low_mean: 0.956933\n    ii_low_median: 0.591916\n    ii_low_ci:\n    - 0.583856\n    - 1.413355\n    ii_low_winsorized_mean: 0.96113\n    n_high: 511\n    n_mid: 391\n    n_low: 454\n    problems: 50\n    per_problem_ii_count: 50\n    gradient_mean_low_over_high: 1.118\n    gradient_median_low_over_high: 1.842\n    pass_fail: FAIL\n    perplexity_high_dense: 1.1462\n    perplexity_high_both: 7.9749\n    perplexity_mid_dense: 1.1226\n    perplexity_mid_both: 6.8553\n    perplexity_low_dense: 1.1105\n    perplexity_low_both: 22.5868\n- exp_id: v6_random_s025\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 3.0024\n    ii_mid_median: 2.9846\n    ii_low_median: 2.9146\n    ii_high_mean: 3.9052\n    ii_mid_mean: 7.9491\n    ii_low_mean: 3.9114\n    per_problem_ii_count: 50\n    n_high: 36\n    n_mid: 25\n    n_low: 24\n    bootstrap_gradient_paired: -0.1199\n    bootstrap_ci_paired:\n    - -1.517\n    - 1.2461\n    bootstrap_p: 0.559\n    bootstrap_gradient_unpaired: -0.8616\n    bootstrap_ci_unpaired:\n    - -3.3911\n    - 1.5169\n    per_problem_ii_stats:\n      high:\n        min: -6.1388\n        max: 25.2471\n        mean: 4.4098\n        median: 3.0421\n        std: 6.0734\n      mid:\n        min: 0.158\n        max: 108.7242\n        mean: 7.5626\n        median: 2.1407\n        std: 20.926\n      low:\n        min: -0.1953\n        max: 12.8555\n        mean: 3.5806\n        median: 2.7289\n        std: 3.4915\n    verdict: FAIL\n- exp_id: v6_random_s030\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: v6_random_s030_r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: bf16_importance_s015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: -0.150213\n        median: 0.005752\n        ci:\n        - -0.294614\n        - -0.055385\n        winsorized_mean: -0.062378\n        skewness: -14.9912\n      mid:\n        mean: 0.447301\n        median: 0.080738\n        ci:\n        - 0.267993\n        - 0.668749\n        winsorized_mean: 0.324751\n        skewness: 4.7221\n      low:\n        mean: 2.405837\n        median: 0.398291\n        ci:\n        - 1.478784\n        - 3.667675\n        winsorized_mean: 1.278857\n        skewness: 9.5402\n    per_problem_ii_stats:\n      high:\n        n: 49\n        min: -0.188061\n        max: 0.335853\n        mean: -0.013405\n        median: 0.00012\n        std: 0.078483\n      mid:\n        n: 40\n        min: -0.169092\n        max: 3.88198\n        mean: 0.308621\n        median: 0.107114\n        std: 0.690186\n      low:\n        n: 50\n        min: -0.872983\n        max: 9.10289\n        mean: 0.725504\n        median: 0.315517\n        std: 1.731056\n    gradient_paired_aggregate_legacy: 69.24\n    median_difference: 0.3925\n    n_problems: 50\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: true\n      overall: PASS\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    perplexity:\n      high:\n        dense: 1.1689\n        attn: 1.4861\n        kv: 1.4481\n        both: 1.5911\n      mid:\n        dense: 1.2269\n        attn: 1.5137\n        kv: 2.5971\n        both: 3.4541\n      low:\n        dense: 1.2286\n        attn: 1.6147\n        kv: 8.9201\n        both: 12.5084\n- exp_id: bf16_importance_s020\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 0.1289\n        median: 0.0145\n        ci:\n        - -0.1975\n        - 0.6647\n        winsorized_mean: -0.0297\n        skewness: 16.67\n      mid:\n        mean: 1.2604\n        median: 0.2027\n        ci:\n        - 0.7466\n        - 1.8962\n        winsorized_mean: 0.766\n        skewness: 7.05\n      low:\n        mean: 6.0288\n        median: 1.4963\n        ci:\n        - 4.4671\n        - 7.9237\n        winsorized_mean: 4.3426\n        skewness: 6.01\n    per_problem_ii_stats:\n      high:\n        n: 49\n        min: -0.1884\n        max: 0.4196\n        mean: 0.0025\n        median: 0.0036\n        std: 0.0966\n      mid:\n        n: 40\n        min: -0.0519\n        max: 8.6969\n        mean: 0.6795\n        median: 0.1977\n        std: 1.4998\n      low:\n        n: 50\n        min: -1.6151\n        max: 22.6875\n        mean: 2.2301\n        median: 1.128\n        std: 4.3758\n    gradient_paired_aggregate_legacy: 5.9\n    median_difference: 1.4818\n    n_problems: 50\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: false\n      overall: PASS\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    perplexity:\n      high:\n        dense: 1.1689\n        attn: 1.5233\n        kv: 1.6191\n        both: 2.1047\n      mid:\n        dense: 1.2269\n        attn: 1.5375\n        kv: 3.5164\n        both: 5.4246\n      low:\n        dense: 1.2286\n        attn: 1.6486\n        kv: 15.7987\n        both: 23.74\n- exp_id: bf16_importance_s025\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 0.302756\n        median: 0.032363\n        ci:\n        - 0.083714\n        - 0.543977\n        winsorized_mean: 0.200962\n        skewness: 4.8826\n      mid:\n        mean: 5.729665\n        median: 1.118069\n        ci:\n        - 3.455574\n        - 8.471799\n        winsorized_mean: 4.189902\n        skewness: 8.2799\n      low:\n        mean: 25.852951\n        median: 7.195958\n        ci:\n        - 19.077082\n        - 33.497293\n        winsorized_mean: 19.319103\n        skewness: 7.3986\n    per_problem_ii_stats:\n      high:\n        n: 49\n        min: -0.316321\n        max: 4.003714\n        mean: 0.133714\n        median: 0.009873\n        std: 0.595358\n      mid:\n        n: 40\n        min: -0.024794\n        max: 18.720486\n        mean: 2.537744\n        median: 1.05707\n        std: 3.962575\n      low:\n        n: 50\n        min: -1.854733\n        max: 75.467653\n        mean: 11.28281\n        median: 3.954593\n        std: 16.620011\n    gradient_paired_aggregate_legacy: 222.35\n    median_difference: 7.1636\n    n_problems: 50\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: false\n      overall: PASS\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    perplexity:\n      high:\n        dense: 1.1689\n        attn: 1.6511\n        kv: 1.8628\n        both: 2.7026\n      mid:\n        dense: 1.2269\n        attn: 1.7039\n        kv: 5.6205\n        both: 13.3436\n      low:\n        dense: 1.2286\n        attn: 1.8366\n        kv: 31.756\n        both: 63.668\n- exp_id: bf16_importance_s030\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 0.5547\n        median: 0.0534\n        ci:\n        - 0.2773\n        - 0.9198\n        winsorized_mean: 0.3367\n        skewness: 10.62\n      mid:\n        mean: 11.3\n        median: 2.2833\n        ci:\n        - 6.865\n        - 17.2633\n        winsorized_mean: 8.1752\n        skewness: 9.19\n      low:\n        mean: 57.7946\n        median: 14.6395\n        ci:\n        - 41.4416\n        - 77.0467\n        winsorized_mean: 39.3143\n        skewness: 8.31\n    per_problem_ii_stats:\n      high:\n        n: 49\n        min: -0.5095\n        max: 4.4457\n        mean: 0.1976\n        median: 0.0343\n        std: 0.6793\n      mid:\n        n: 40\n        min: -0.1989\n        max: 34.0258\n        mean: 5.2585\n        median: 1.5173\n        std: 7.9382\n      low:\n        n: 50\n        min: -7.3027\n        max: 126.7985\n        mean: 22.6601\n        median: 9.9731\n        std: 28.4096\n    gradient_paired_aggregate_legacy: 57.24\n    median_difference: 14.5861\n    n_problems: 50\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: false\n      overall: PASS\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    perplexity:\n      high:\n        dense: 1.1689\n        attn: 1.7123\n        kv: 2.0544\n        both: 3.2372\n      mid:\n        dense: 1.2269\n        attn: 1.7894\n        kv: 9.4821\n        both: 24.2847\n      low:\n        dense: 1.2286\n        attn: 1.9347\n        kv: 51.6485\n        both: 122.61\n- exp_id: bf16_random_s015\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: bf16_random_s020\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: bf16_random_s025\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: bf16_random_s030\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: bf16_qwen_importance_s015\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: bf16_qwen_importance_s020\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: bf16_qwen_importance_s025\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: bf16_qwen_importance_s030\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: v6_random_s030_r3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    II_high_mean: 9.2364\n    II_mid_mean: -230.7604\n    II_low_mean: -7.4119\n    II_high_median: 4.0237\n    II_mid_median: 2.4272\n    II_low_median: 4.735\n    ppl_low_both: 88.94\n    per_problem_count: 50\n- exp_id: bf16_ds_imp_s015\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    median_difference: 0.323579\n    permutation_p: 0\n    cohens_d: 0.6068\n    bootstrap_ci_95:\n    - 0.198824\n    - 0.471566\n    wilcoxon_p: 0\n    n_bootstrap: 10000\n    n_paired: 49\n- exp_id: bf16_ds_imp_s020\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    median_difference: 1.15202\n    permutation_p: 0\n    cohens_d: 0.725\n    bootstrap_ci_95:\n    - 0.655454\n    - 1.256001\n    wilcoxon_p: 0\n    n_bootstrap: 10000\n    n_paired: 49\n- exp_id: bf16_ds_imp_s025\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    median_difference: 3.968568\n    permutation_p: 0\n    cohens_d: 0.9534\n    bootstrap_ci_95:\n    - 2.829037\n    - 5.291756\n    wilcoxon_p: 0\n    n_bootstrap: 10000\n    n_paired: 49\n- exp_id: bf16_ds_imp_s030\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    median_difference: 9.943595\n    permutation_p: 0\n    cohens_d: 1.1263\n    bootstrap_ci_95:\n    - 8.391554\n    - 16.652865\n    wilcoxon_p: 0\n    n_bootstrap: 10000\n    n_paired: 49\n- exp_id: bf16_ds_rand_s015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 0.2208\n        median: 0.0931\n        ci:\n        - -1.0091\n        - 1.5243\n        median_ci:\n        - 0.0024\n        - 0.1515\n        winsorized_mean: 0.3161\n        skewness: -5.4\n      mid:\n        mean: -3.3604\n        median: 0.0967\n        ci:\n        - -8.4057\n        - 0.3697\n        median_ci:\n        - 0.0219\n        - 0.197\n        winsorized_mean: -0.6366\n        skewness: -10.56\n      low:\n        mean: -1.8952\n        median: 0.1026\n        ci:\n        - -4.9698\n        - 0.2741\n        median_ci:\n        - 0.044\n        - 0.1755\n        winsorized_mean: 0.0521\n        skewness: -11.57\n    perplexity:\n      high:\n        dense: 1.1687\n        attn: 3.5947\n        kv: 2.9239\n        both: 5.7569\n      mid:\n        dense: 1.2269\n        attn: 297.7957\n        kv: 2.915\n        both: 11.3156\n      low:\n        dense: 1.2284\n        attn: 11.3419\n        kv: 3.6161\n        both: 6.2886\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    n_problems: 50\n    pass_fail:\n      ci_overlap: false\n      sign_reversal: false\n      overall: FAIL\n    median_difference: 0.0095\n- exp_id: bf16_ds_rand_s020\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 1.1216\n        median: 0.2918\n        ci:\n        - 0.0796\n        - 2.5834\n        median_ci:\n        - 0.1598\n        - 0.4581\n        winsorized_mean: 1.7664\n        skewness: 9.59\n      mid:\n        mean: -1.5827\n        median: 0.3504\n        ci:\n        - -6.0963\n        - 1.5735\n        median_ci:\n        - 0.1993\n        - 0.5226\n        winsorized_mean: 0.5839\n        skewness: -12.31\n      low:\n        mean: -0.4116\n        median: 0.2763\n        ci:\n        - -2.6034\n        - 1.209\n        median_ci:\n        - 0.2194\n        - 0.5487\n        winsorized_mean: 0.9942\n        skewness: -10.07\n    perplexity:\n      high:\n        dense: 1.1687\n        attn: 3.1905\n        kv: 3.8002\n        both: 8.8129\n      mid:\n        dense: 1.2269\n        attn: 67.8504\n        kv: 3.788\n        both: 11.4974\n      low:\n        dense: 1.2284\n        attn: 8.592\n        kv: 5.0078\n        both: 9.2001\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    n_problems: 50\n    pass_fail:\n      ci_overlap: false\n      sign_reversal: false\n      overall: FAIL\n    median_difference: -0.0155\n- exp_id: bf16_ds_rand_s025\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 3.59\n        median: 0.8182\n        ci:\n        - 1.4021\n        - 6.2327\n        median_ci:\n        - 0.5075\n        - 1.7217\n        winsorized_mean: 6.3965\n        skewness: -7.57\n      mid:\n        mean: -1.8455\n        median: 0.9324\n        ci:\n        - -10.3663\n        - 4.9342\n        median_ci:\n        - 0.7331\n        - 1.7003\n        winsorized_mean: 3.1014\n        skewness: -12.76\n      low:\n        mean: 0.7212\n        median: 1.3627\n        ci:\n        - -4.2068\n        - 4.5006\n        median_ci:\n        - 1.0869\n        - 2.6866\n        winsorized_mean: 4.1866\n        skewness: -15.85\n    perplexity:\n      high:\n        dense: 1.1687\n        attn: 7.237\n        kv: 4.9751\n        both: 17.7423\n      mid:\n        dense: 1.2269\n        attn: 868.3199\n        kv: 5.1165\n        both: 29.4661\n      low:\n        dense: 1.2284\n        attn: 24.3571\n        kv: 6.7993\n        both: 17.9694\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    n_problems: 50\n    pass_fail:\n      ci_overlap: false\n      sign_reversal: false\n      overall: FAIL\n    median_difference: 0.5445\n- exp_id: bf16_ds_rand_s030\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 7.5555\n        median: 2.5031\n        ci:\n        - 4.4087\n        - 11.6199\n        median_ci:\n        - 1.3292\n        - 4.1205\n        winsorized_mean: null\n        skewness: null\n      mid:\n        mean: 6.2518\n        median: 2.5918\n        ci:\n        - 2.1767\n        - 10.4757\n        median_ci:\n        - 1.8397\n        - 3.7888\n        winsorized_mean: null\n        skewness: null\n      low:\n        mean: 6.8323\n        median: 4.0414\n        ci:\n        - 3.2428\n        - 10.6996\n        median_ci:\n        - 2.2686\n        - 6.3579\n        winsorized_mean: null\n        skewness: null\n    perplexity:\n      high:\n        dense: 1.1687\n        attn: 16.7892\n        kv: 8.8073\n        both: 40.7553\n      mid:\n        dense: 1.2269\n        attn: 2461.9219\n        kv: 8.6662\n        both: 62.4422\n      low:\n        dense: 1.2284\n        attn: 55.2916\n        kv: 11.5789\n        both: 37.6009\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    n_problems: 50\n    pass_fail:\n      ci_overlap: false\n      sign_reversal: false\n      overall: FAIL\n    median_difference: 1.5383\n- exp_id: bf16_qw_imp_s015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    median_difference: 0.047619\n    permutation_p: 0.0001\n    cohens_d: 0.3705\n    bootstrap_ci_95:\n    - -0.005077\n    - 0.109517\n    wilcoxon_p: 0.02958\n    n_bootstrap: 10000\n    n_paired: 46\n- exp_id: bf16_qw_imp_s020\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    median_difference: 0.207511\n    permutation_p: 0\n    cohens_d: 0.7224\n    bootstrap_ci_95:\n    - 0.067222\n    - 0.40226\n    wilcoxon_p: 3.4e-05\n    n_bootstrap: 10000\n    n_paired: 46\n- exp_id: bf16_qw_imp_s025\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    median_difference: 1.108706\n    permutation_p: 0\n    cohens_d: 1.2329\n    bootstrap_ci_95:\n    - 0.609247\n    - 1.469002\n    wilcoxon_p: 0\n    n_bootstrap: 10000\n    n_paired: 46\n- exp_id: bf16_qw_imp_s030\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    median_difference: 2.619385\n    permutation_p: 0\n    cohens_d: 1.4394\n    bootstrap_ci_95:\n    - 1.722281\n    - 3.651063\n    wilcoxon_p: 0\n    n_bootstrap: 10000\n    n_paired: 46\n- exp_id: bf16_qw_rand_s015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 1.6652\n        median: 0.1381\n        ci:\n        - 1.0986\n        - 2.4042\n        median_ci:\n        - 0.1025\n        - 0.2074\n        winsorized_mean: 1.0044\n        skewness: 7.1842\n      mid:\n        mean: 1.6975\n        median: 0.2194\n        ci:\n        - 0.4473\n        - 3.4612\n        median_ci:\n        - -0.0048\n        - 0.6621\n        winsorized_mean: 1.4038\n        skewness: 3.2101\n      low:\n        mean: 1.4082\n        median: 0.1878\n        ci:\n        - 0.8358\n        - 2.06\n        median_ci:\n        - 0.0962\n        - 0.3139\n        winsorized_mean: 0.9403\n        skewness: 7.1113\n    perplexity:\n      high:\n        dense: 1.0737\n        attn: 1.3939\n        kv: 2.0487\n        both: 4.2076\n      mid:\n        dense: 1.1322\n        attn: 1.4175\n        kv: 2.3709\n        both: 4.6105\n      low:\n        dense: 1.1517\n        attn: 1.7177\n        kv: 3.3253\n        both: 5.4788\n    phase_stats:\n      high:\n        n_tokens: 16289\n        n_segments: 295\n      mid:\n        n_tokens: 4372\n        n_segments: 26\n      low:\n        n_tokens: 32227\n        n_segments: 276\n    n_problems: 50\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: false\n      overall: FAIL\n    median_difference: -0.029401\n    permutation_test:\n      p_value: 0.7657\n      B: 10000\n    cohens_d: -0.0507\n    bootstrap_ci_95:\n    - -0.2106\n    - 0.2124\n    wilcoxon_p: 0.862554\n    phase_median_ii:\n      high: 0.1381\n      mid: 0.2194\n      low: 0.1878\n- exp_id: bf16_qw_rand_s020\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 2.58579\n        median: 0.48549\n        ci:\n        - 1.769404\n        - 3.501692\n        median_ci:\n        - 0.304626\n        - 0.658814\n        winsorized_mean: 1.80021\n        skewness: 5.4038\n      mid:\n        mean: 5.69684\n        median: 0.76699\n        ci:\n        - 1.69004\n        - 12.276143\n        median_ci:\n        - 0.482838\n        - 3.392541\n        winsorized_mean: 4.304174\n        skewness: 3.526\n      low:\n        mean: 65.915714\n        median: 0.614438\n        ci:\n        - -18.581948\n        - 221.709429\n        median_ci:\n        - 0.484725\n        - 0.848787\n        winsorized_mean: 2.389244\n        skewness: 16.2163\n    perplexity:\n      high:\n        dense: 1.0737\n        attn: 1.6115\n        kv: 2.5041\n        both: 5.9394\n      mid:\n        dense: 1.1322\n        attn: 1.7583\n        kv: 3.0658\n        both: 10.5578\n      low:\n        dense: 1.1517\n        attn: 75.631\n        kv: 4.3535\n        both: 140.6269\n    phase_stats:\n      high:\n        n_tokens: 16289\n        n_segments: 295\n      mid:\n        n_tokens: 4372\n        n_segments: 26\n      low:\n        n_tokens: 32227\n        n_segments: 276\n    n_problems: 50\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: false\n      overall: FAIL\n    median_difference: 0.128948\n    permutation_test:\n      p_value: 0.352\n      B: 10000\n    cohens_d: 0.247\n    bootstrap_ci_95:\n    - -0.139\n    - 0.215\n    wilcoxon_p: 0.149\n    phase_median_ii:\n      high: 0.4739\n      mid: 0.8757\n      low: 0.4847\n- exp_id: bf16_qw_rand_s025\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 14.4213\n        median: 1.6043\n        ci:\n        - 7.1074\n        - 23.4587\n        median_ci:\n        - 0.6977\n        - 3.0736\n        winsorized_mean: 9.3765\n        skewness: 4.8263\n      mid:\n        mean: 18.6458\n        median: 2.2225\n        ci:\n        - 3.3729\n        - 41.6037\n        median_ci:\n        - 0.6093\n        - 11.5889\n        winsorized_mean: 14.2901\n        skewness: 3.8245\n      low:\n        mean: 17.7277\n        median: 2.2641\n        ci:\n        - 4.3523\n        - 37.2093\n        median_ci:\n        - 1.2218\n        - 4.8561\n        winsorized_mean: 9.9876\n        skewness: 5.7652\n    perplexity:\n      high:\n        dense: 1.0737\n        attn: 2.0183\n        kv: 3.1882\n        both: 9.7654\n      mid:\n        dense: 1.1322\n        attn: 2.3476\n        kv: 4.0124\n        both: 17.3298\n      low:\n        dense: 1.1517\n        attn: 2.7834\n        kv: 5.8762\n        both: 25.4321\n    phase_stats:\n      high:\n        n_tokens: 16289\n        n_segments: 295\n      mid:\n        n_tokens: 4372\n        n_segments: 26\n      low:\n        n_tokens: 32227\n        n_segments: 276\n    n_problems: 50\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: false\n      overall: FAIL\n    median_difference: 1.144074\n    permutation_test:\n      p_value: 0.1679\n      B: 10000\n    cohens_d: 0.1574\n    bootstrap_ci_95:\n    - -0.3166\n    - 4.1645\n    wilcoxon_p: 0.010313\n    phase_median_ii:\n      high: 1.6043\n      mid: 2.2225\n      low: 2.2641\n- exp_id: bf16_qw_rand_s030\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    median_high: 4.200557\n    median_mid: 6.477036\n    median_low: 8.065662\n    median_diff: 2.418272\n    permutation_p: 0.012\n    cohens_d: -0.03513\n    wilcoxon_p: 0.01566\n    bootstrap_ci_low: 0.241897\n    bootstrap_ci_high: 3.314824\n- exp_id: c4_entropy\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    importance_entropy_delta:\n      s015: -0.0402\n      s020: -0.0472\n      s025: -0.0446\n      s030: -0.0436\n    random_entropy_delta:\n      s015: 0.1283\n      s020: 0.136\n      s025: 0.2171\n      s030: 0.2327\n    importance_gini_delta:\n      s015: -0.0301\n      s020: -0.0404\n      s025: -0.0647\n      s030: -0.0806\n    random_gini_delta:\n      s015: -0.0309\n      s020: -0.0403\n      s025: -0.062\n      s030: -0.0732\n    importance_cv_delta:\n      s015: -0.564\n      s020: -0.774\n      s025: -1.287\n      s030: -1.665\n    random_cv_delta:\n      s015: -1.021\n      s020: -1.203\n      s025: -1.923\n      s030: -2.137\n    problems_completed: 30\n    runtime_minutes: 69.1\n- exp_id: qwen_c4_entropy\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    problems_completed: 30\n    qwen_importance_entropy_delta:\n      s015: -0.0733\n      s020: -0.0759\n      s025: 0.0451\n      s030: -0.0072\n    qwen_random_entropy_delta:\n      s015: 0.0838\n      s020: 0.0901\n      s025: 0.2168\n      s030: 0.1968\n    qwen_importance_gini_delta:\n      s015: -0.0103\n      s020: -0.0121\n      s025: -0.01\n      s030: -0.0202\n    qwen_random_gini_delta:\n      s015: -0.0186\n      s020: -0.0229\n      s025: -0.0337\n      s030: -0.0448\n    qwen_importance_cv_delta:\n      s015: -0.045\n      s020: -0.208\n      s025: -1.491\n      s030: -1.142\n    qwen_random_cv_delta:\n      s015: -0.778\n      s020: -0.889\n      s025: -1.5\n      s030: -1.677\n    cross_model_notes: random entropy increase consistent; importance entropy collapse\n      inconsistent at s025 (reversed to +0.045) and near-zero at s030; gini/cv directions\n      consistent but Qwen magnitudes smaller\n- exp_id: bf16_ds_imp_s010\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    verdict: FAIL\n    problems: 50\n    II_high_sparsity_median: 0.0027\n    II_high_sparsity_mean: -0.1998\n    II_low_sparsity_median: 0.0151\n    II_low_sparsity_mean: -0.1066\n    II_mid_sparsity_median: 0.0061\n    II_mid_sparsity_mean: -0.0131\n    high_sparsity_tokens: 21086\n    low_sparsity_tokens: 27748\n    mid_sparsity_tokens: 13306\n- exp_id: bf16_ds_imp_s035\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    verdict: PASS\n    problems: 50\n    II_high_sparsity_median: 0.1051\n    II_high_sparsity_mean: 1.4309\n    II_low_sparsity_median: 28.7649\n    II_low_sparsity_mean: 104.1892\n    II_mid_sparsity_median: 4.9542\n    II_mid_sparsity_mean: 20.326\n    high_sparsity_tokens: 21086\n    low_sparsity_tokens: 27748\n    mid_sparsity_tokens: 13306\n    ci_overlap_test: low_sparsity vs mid_sparsity CI non-overlapping at 0.35\n- exp_id: bf16_qw_imp_s010\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_problems: 50\n    overall_verdict: PASS\n    ci_overlap_test: PASS\n    sign_reversal_test: FAIL\n    high_sparsity_II_median: 0.0001\n    high_sparsity_II_median_CI:\n    - -0.0028\n    - 0.0005\n    high_sparsity_II_mean: -0.0887\n    high_sparsity_II_mean_CI:\n    - -0.1235\n    - -0.0591\n    low_sparsity_II_median: -0.0444\n    low_sparsity_II_median_CI:\n    - -0.0967\n    - -0.0152\n    low_sparsity_II_mean: -0.2431\n    low_sparsity_II_mean_CI:\n    - -0.3817\n    - -0.1202\n    mid_sparsity_II_median: -0.0359\n    mid_sparsity_II_median_CI:\n    - -0.0963\n    - -0.015\n    mid_sparsity_II_mean: -0.084\n    mid_sparsity_II_mean_CI:\n    - -0.1366\n    - -0.035\n    ppl_high_dense: 1.074\n    ppl_high_both: 1.228\n    ppl_low_dense: 1.152\n    ppl_low_both: 3.204\n    ppl_mid_dense: 1.133\n    ppl_mid_both: 1.741\n- exp_id: bf16_qw_imp_s035\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_problems: 50\n    overall_verdict: PASS\n    ci_overlap_test: PASS\n    sign_reversal_test: FAIL\n    high_sparsity_II_median: 0.0232\n    high_sparsity_II_median_CI:\n    - 0.0154\n    - 0.0383\n    high_sparsity_II_mean: 0.1643\n    high_sparsity_II_mean_CI:\n    - 0.0844\n    - 0.2495\n    low_sparsity_II_median: 8.2358\n    low_sparsity_II_median_CI:\n    - 6.1564\n    - 10.9231\n    low_sparsity_II_mean: 18.9673\n    low_sparsity_II_mean_CI:\n    - 14.5015\n    - 23.9752\n    mid_sparsity_II_median: 0.9577\n    mid_sparsity_II_median_CI:\n    - 0.171\n    - 3.5575\n    mid_sparsity_II_mean: 8.0734\n    mid_sparsity_II_mean_CI:\n    - 2.0224\n    - 16.8946\n    ppl_high_dense: 1.0738\n    ppl_high_both: 2.3435\n    ppl_low_dense: 1.1518\n    ppl_low_both: 58.0358\n    ppl_mid_dense: 1.1327\n    ppl_mid_both: 20.9912\n    high_sparsity_tokens: 16289\n    low_sparsity_tokens: 32227\n    mid_sparsity_tokens: 4372\n- exp_id: c2_n500_deepseek\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_problems: 500\n    effective_n: 496\n    mid_null_rate: 0.102\n    imp_s015_median_ii: 0.3907\n    imp_s015_ci:\n    - 0.3496\n    - 0.4431\n    imp_s015_wilcoxon_p: 1.27e-70\n    imp_s020_median_ii: 1.2149\n    imp_s020_ci:\n    - 1.1072\n    - 1.3365\n    imp_s020_wilcoxon_p: 3.98e-75\n    imp_s025_median_ii: 3.9857\n    imp_s025_ci:\n    - 3.5272\n    - 4.3588\n    imp_s025_wilcoxon_p: 1.99e-78\n    imp_s030_median_ii: 8.4813\n    imp_s030_ci:\n    - 7.7543\n    - 9.6919\n    imp_s030_wilcoxon_p: 1.09e-79\n    rand_s015_median_ii: 0.0139\n    rand_s015_wilcoxon_p: 0.863\n    rand_s020_median_ii: 0.0315\n    rand_s020_wilcoxon_p: 0.28\n    rand_s025_median_ii: 0.2574\n    rand_s025_bonf_p: 0.005839\n    rand_s025_fdr_p: 0.001914\n    rand_s030_median_ii: 0.5096\n    rand_s030_bonf_p: 0.005903\n    rand_s030_fdr_p: 0.001914\n    dz_s015_s020: -0.925\n    dz_s020_s025: -0.824\n    dz_s025_s030: -0.773\n    dz_s015_s030: -0.944\n    all_dz_reliable: true\n    dose_response_monotonic: true\n    dose_response_spearman_rho: 1\n    dose_response_perm_p: 0.0417\n    imp_rand_ratio_range: 15.5-38.6x\n    bonferroni_k: 4\n    bonferroni_note: Bonferroni k=4 family-wise (D066 revision)\n- exp_id: c3_llama_arch\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: c2_ds_n500\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: c2_qw_n500\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: c3_llama\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    model: DeepSeek-R1-Distill-Llama-8B\n    n_problems: 50\n    n_valid: 49\n    n_skipped: 1\n    conditions_completed: 8/8\n    n_bootstrap: 10000\n    bonferroni_k: 4\n    imp_vs_rand_dz:\n      s015: 0.1923\n      s020: 0.255\n      s025: 0.2902\n      s030: 0.3352\n    imp_vs_rand_dz_ci:\n      s015:\n      - -0.0862\n      - 0.496\n      s020:\n      - -0.0248\n      - 0.5381\n      s025:\n      - 0.0081\n      - 0.6121\n      s030:\n      - 0.0606\n      - 0.6629\n    imp_vs_rand_dz_interpretation:\n      s015: negligible\n      s020: small\n      s025: small\n      s030: small\n    imp_vs_rand_dz_monotonic: true\n    phase_gradient_importance_dz:\n      s015: 1.0079\n      s020: 1.108\n      s025: 1.1227\n      s030: 1.0038\n    phase_gradient_importance_dz_ci:\n      s015:\n      - 0.593\n      - 1.7025\n      s020:\n      - 0.8144\n      - 1.5698\n      s025:\n      - 0.8735\n      - 1.5768\n      s030:\n      - 0.8099\n      - 1.3519\n    phase_gradient_importance_interpretation: all_large\n    phase_gradient_random_dz:\n      s015: 0.3497\n      s020: 0.373\n      s025: 0.4476\n      s030: 0.4385\n    phase_gradient_random_dz_ci:\n      s015:\n      - 0.0665\n      - 0.6916\n      s020:\n      - 0.0868\n      - 0.7335\n      s025:\n      - 0.1669\n      - 0.7698\n      s030:\n      - 0.1966\n      - 0.707\n    phase_gradient_random_interpretation: all_small\n    median_diff:\n      s015: 0.0203\n      s020: 0.0221\n      s025: 0.0947\n      s030: 0.3562\n    median_diff_ci:\n      s015:\n      - 0.0016\n      - 0.0435\n      s020:\n      - -0.0905\n      - 0.187\n      s025:\n      - -0.0037\n      - 0.3029\n      s030:\n      - -0.0691\n      - 0.5442\n    wilcoxon_p:\n      s015: 0.0549\n      s020: 0.0632\n      s025: 0.0209\n      s030: 0.0074\n    wilcoxon_p_bonferroni:\n      s015: 0.2195\n      s020: 0.2527\n      s025: 0.0834\n      s030: 0.0294\n    significant_bonferroni:\n      s015: false\n      s020: false\n      s025: false\n      s030: true\n    cross_arch_comparison:\n      deepseek_importance_dz:\n        s015: 0.4416\n        s020: 0.5195\n        s025: 0.6831\n        s030: 0.8031\n      llama_importance_dz:\n        s015: 1.0079\n        s020: 1.108\n        s025: 1.1227\n        s030: 1.0038\n      delta:\n        s015: 0.5663\n        s020: 0.5885\n        s025: 0.4396\n        s030: 0.2007\n      note: LLaMA shows uniformly large d_z (all >1.0) vs DeepSeek medium-to-large\n- exp_id: c5b_pilot\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    s025_uniform_median_ii: 1.0435\n    s025_oracle_median_ii: 0.856\n    s025_oracle_recovery_pct: 18\n    s025_oracle_recovery_ci:\n    - -39\n    - 45.8\n    s025_oracle_wilcoxon_p: 0.0021\n    s025_heuristic_median_ii: 0.7127\n    s025_heuristic_recovery_pct: 31.7\n    s025_heuristic_recovery_ci:\n    - -22.8\n    - 66\n    s025_heuristic_wilcoxon_p: 0.0236\n    gate_criterion: oracle_recovery > 30%\n    gate_result: FAIL\n    s030_status: not_completed\n    n_problems: 30\n- exp_id: c2_qw_n500_r3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_problems: 500\n    effective_n: 475\n    filter: low+high valid only (mid-null allowed)\n    mid_null_rate: 0.452\n    imp_s015_median_ii: 0.0659\n    imp_s015_ci:\n    - 0.0492\n    - 0.0925\n    imp_s015_wilcoxon_p: 8.66e-15\n    imp_s015_bonf_p: 3.46e-14\n    imp_s020_median_ii: 0.3073\n    imp_s020_ci:\n    - 0.2612\n    - 0.3564\n    imp_s020_wilcoxon_p: 6.84e-42\n    imp_s020_bonf_p: 2.74e-41\n    imp_s025_median_ii: 1.0745\n    imp_s025_ci:\n    - 0.9766\n    - 1.1787\n    imp_s025_wilcoxon_p: 1.06e-68\n    imp_s025_bonf_p: 4.25e-68\n    imp_s030_median_ii: 3.155\n    imp_s030_ci:\n    - 2.7834\n    - 3.5582\n    imp_s030_wilcoxon_p: 9.21e-74\n    imp_s030_bonf_p: 3.69e-73\n    rand_s015_median_ii: -0.0111\n    rand_s015_wilcoxon_p: 0.172\n    rand_s015_bonf_p: 0.687\n    rand_s020_median_ii: 0.0153\n    rand_s020_wilcoxon_p: 0.2\n    rand_s020_bonf_p: 0.8\n    rand_s025_median_ii: 0.3931\n    rand_s025_wilcoxon_p: 1.59e-11\n    rand_s025_bonf_p: 6.37e-11\n    rand_s025_fdr_p: 2.63e-11\n    rand_s030_median_ii: 0.9127\n    rand_s030_wilcoxon_p: 2.92e-15\n    rand_s030_bonf_p: 1.17e-14\n    rand_s030_fdr_p: 5.61e-15\n    dz_s015_s020: -0.629\n    dz_s020_s025: -0.865\n    dz_s025_s030: -0.767\n    dz_s015_s030: -0.923\n    all_dz_reliable: true\n    dose_response_monotonic: true\n    dose_response_spearman_rho: 1\n    dose_response_perm_p: 0.0417\n    imp_rand_ratio_range: 2.7-20.1x\n    bonferroni_k: 4\n    bonferroni_note: Bonferroni k=4 family-wise (D066 revision)\n- exp_id: sf5_asymmetric_spot\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    config_a_h02_kv03:\n      II_low: 19.51\n      II_mid: 6.05\n      II_high: 0.38\n      D: 19.13\n    config_b_h03_kv02:\n      II_low: 18.77\n      II_mid: 3.97\n      II_high: 0.52\n      D: 18.25\n    pre_registered_criterion_passed: true\n    gradient_direction: II_low >> II_mid >> II_high (consistent with symmetric baseline)\n- exp_id: gsm8k_profiling_ds\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    version: v3_median\n    n_problems: 50\n    method: median + Wilcoxon + bootstrap_median(B=10000)\n    importance:\n      s015:\n        median_gradient: 0.241\n        ci_low: 0.077\n        ci_high: 0.478\n        wilcoxon_p: 0.0003\n      s020:\n        median_gradient: 0.74\n        ci_low: 0.314\n        ci_high: 1.119\n        wilcoxon_p: 0.0001\n      s025:\n        median_gradient: 1.992\n        ci_low: 0.933\n        ci_high: 2.82\n        wilcoxon_p: 0.0001\n      s030:\n        median_gradient: 4.682\n        ci_low: 2.121\n        ci_high: 10.557\n        wilcoxon_p: 0.0001\n    imp_rand_ratio:\n      s015: 2.3\n      s020: 2.5\n      s025: 3.8\n      s030: 2.8\n    dose_response_monotonic: true\n- exp_id: gsm8k_profiling_qw\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    version: v3_median\n    n_problems: 50\n    method: median + Wilcoxon + bootstrap_median(B=10000)\n    importance:\n      s015:\n        median_gradient: 0.039\n      s020:\n        median_gradient: 0.158\n      s025:\n        median_gradient: 1.1\n      s030:\n        median_gradient: 2.092\n    qw_rand_s030: INVALID\n- exp_id: think_phase_validation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    effective_n: 48\n    skipped_problems: 2\n    median_kappa: 0.887\n    thinking_in_low_sparsity_phase: 0.578\n    answer_in_high_sparsity_phase: 0.627\n    note: Phase segmentation based on dense model — 4 sparsity conditions share identical\n      phase boundaries, effective sample n=48 not n=192\n- exp_id: r9c2-spike\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: r9c2-spike-v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: r9c2-spike-v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: c2_accuracy_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_problems: 50\n    ds_dense_acc: 0.52\n    ds_s015_acc: 0.36\n    ds_s015_delta: -0.16\n    ds_s030_acc: 0.1\n    ds_s030_delta: -0.42\n    qw_dense_acc: 0.32\n    qw_s015_acc: 0.34\n    qw_s015_delta: 0.02\n    qw_s030_acc: 0.14\n    qw_s030_delta: -0.18\n    ds_s030_chinese_reasoning_rate: 0.4\n    ds_dense_truncation_rate: 0.56\n    note: v2 rescored with fixed radical+degree matcher. DS s015 34→36, QW s015 32→34\n- exp_id: acc_ds_s020\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ds_s020_acc: 0.26\n    ds_s020_acc_v2: 0.26\n    ds_s020_correct: 13\n    ds_s020_total: 50\n    ds_s020_delta_vs_dense: -0.26\n    output_truncated_count: 32\n    output_truncated_rate: 0.64\n    extraction_failure_count: 31\n    extraction_failure_rate: 0.62\n    total_time_s: 1560\n    note: v2 rescored with fixed radical+degree matcher; 0 changes. Dense baseline=0.52\n- exp_id: acc_ds_s025\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy: 0.08\n    correct: 4\n    total: 50\n    null_count: 37\n    null_rate: 0.74\n    output_truncated_count: 38\n    output_truncated_rate: 0.76\n    wrong_count: 9\n    wrong_rate: 0.18\n    extraction_failure_count: 1\n    extraction_failure_rate: 0.02\n    total_time_s: 1670.5\n    heads_pruned: 196\n    delta_vs_dense: -0.44\n- exp_id: acc_qw_s020\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    qw_s020_acc: 0.26\n    qw_s020_correct: 13\n    qw_s020_total: 50\n    qw_s020_delta_vs_dense: -0.06\n    null_count: 2\n    null_rate: 0.04\n    output_truncated_count: 2\n    output_truncated_rate: 0.04\n    extraction_failure_count: 0\n    extraction_failure_rate: 0\n    wrong_count: 35\n    wrong_rate: 0.7\n    heads_pruned: 140\n    total_time_s: 598\n    note: v2 rescored with fixed radical+degree matcher\n- exp_id: acc_qw_s025\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    qw_s025_acc: 0.32\n    qw_s025_correct: 16\n    qw_s025_total: 50\n    qw_s025_delta_vs_dense: 0\n    null_count: 8\n    null_rate: 0.16\n    output_truncated_count: 2\n    output_truncated_rate: 0.04\n    extraction_failure_count: 6\n    extraction_failure_rate: 0.12\n    wrong_count: 26\n    wrong_rate: 0.52\n    heads_pruned: 196\n    total_time_s: 559\n    note: v2 rescored with fixed radical+degree matcher; 3 problems flipped (sqrt+degree)\n- exp_id: acc_qw_s020_n100\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    batch1_acc: 0.26\n    batch1_correct: 13\n    batch1_total: 50\n    batch1_source: acc_qw_s020_b1_8k (v2, 8k tokens)\n    batch2_acc: 0.46\n    batch2_correct: 23\n    batch2_total: 50\n    combined_acc: 0.36\n    combined_correct: 36\n    combined_total: 100\n    note: 'batch effect: batch1=26% vs batch2=46%, Δ=20pp'\n- exp_id: acc_qw_s025_n100\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    batch1_acc: 0.32\n    batch1_correct: 16\n    batch1_total: 50\n    batch1_source: acc_qw_s025_b1_8k (v2, 8k tokens)\n    batch2_acc: 0.34\n    batch2_correct: 17\n    batch2_total: 50\n    combined_acc: 0.33\n    combined_correct: 33\n    combined_total: 100\n- exp_id: acc_ds_dense_8k\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: acc_ds_s015_8k\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: acc_ds_s020_8k\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: acc_ds_s025_8k\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: acc_ds_s030_8k\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: acc_qw_dense_n100\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    batch1_correct: 22\n    batch1_total: 50\n    batch1_acc: 0.44\n    batch1_source: acc_qw_dense_b1_8k (v2, 8k tokens)\n    batch2_correct: 24\n    batch2_total: 50\n    batch2_acc: 0.48\n    combined_correct: 46\n    combined_total: 100\n    combined_acc: 0.46\n- exp_id: acc_qw_s015_n100\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    batch1_acc: 0.46\n    batch1_correct: 23\n    batch1_total: 50\n    batch1_source: acc_qw_s015_b1_8k (v2, 8k tokens)\n    batch2_acc: 0.38\n    batch2_correct: 19\n    batch2_total: 50\n    combined_acc: 0.42\n    combined_correct: 42\n    combined_total: 100\n- exp_id: acc_qw_s030_n100\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    batch1_correct: 7\n    batch1_total: 50\n    batch1_acc: 0.14\n    batch1_source: acc_qw_s030_b1_8k (v2, 8k tokens)\n    batch2_correct: 12\n    batch2_total: 50\n    batch2_acc: 0.24\n    combined_correct: 19\n    combined_total: 100\n    combined_acc: 0.19\n- exp_id: acc_ds_s015_8k_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.48\n    correct: 24\n    total: 50\n    truncation_rate: 0.32\n    truncated_count: 16\n    non_truncated_accuracy: 0.706\n    non_truncated_correct: 24\n    non_truncated_total: 34\n    wall_time_s: 3967\n    max_new_tokens: 8192\n- exp_id: acc_ds_s020_8k_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.3\n    correct: 15\n    total: 50\n    truncated_count: 28\n    truncated_rate: 0.56\n    extraction_failures: 1\n    non_truncated_accuracy: 0.682\n    non_truncated_correct: 15\n    non_truncated_total: 22\n    total_time_seconds: 5549\n    max_new_tokens: 8192\n- exp_id: acc_ds_s025_8k_v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy: 0.08\n    correct: 4\n    total: 50\n    truncated_count: 38\n    truncated_rate: 0.76\n    avg_tokens: 6343.8\n    max_new_tokens: 8192\n    total_time_seconds: 6827.8\n    null_count: 36\n- exp_id: acc_ds_s030_8k_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.04\n    correct: 2\n    total: 50\n    truncation_rate: 0.76\n    truncated_count: 38\n    extraction_failures: 3\n    non_truncated_accuracy: 0.167\n    non_truncated_correct: 2\n    non_truncated_total: 12\n    max_new_tokens: 8192\n    avg_tokens: 6566.3\n    total_time_seconds: 7095.1\n- exp_id: gsm8k_qw_rand_s025\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: gsm8k_qw_rand_s030\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: acc_qw_s020_n100_b2_fix\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    batch2_correct: 23\n    batch2_total: 50\n    batch2_acc: 0.46\n    batch1_correct_v2: 13\n    batch1_total: 50\n    batch1_acc_v2: 0.26\n    combined_correct: 36\n    combined_total: 100\n    combined_acc: 0.36\n    null_count: 2\n    truncated_count: 1\n    total_time_seconds: 884.3\n    max_new_tokens: 8192\n    original_batch2_correct: 22\n    original_batch2_acc: 0.44\n    delta_vs_original: +1 correct (+0.02 acc)\n- exp_id: acc_qw_s025_n100_b2_fix\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.34\n    correct: 17\n    n_problems: 50\n    truncation_rate: 0.06\n    truncated_count: 3\n    avg_tokens: 1044\n    max_new_tokens: 8192\n    total_time_seconds: 1099\n    batch: b2 (problems 51-100)\n    merged_n100_accuracy: 0.33\n    merged_n100_correct: 33\n    merged_n100_note: batch1 used max_new_tokens=2048, batch2_fix used 8192 — mismatch\n- exp_id: acc_ds_dense_8k_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.74\n    correct: 37\n    n_problems: 50\n    truncation_rate: 0.16\n    truncated_count: 8\n    avg_tokens: 3126\n    max_new_tokens: 8192\n    total_time_seconds: 2882\n- exp_id: gsm8k_qw_rand_s025_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    verdict: PASS\n    n_problems: 50\n    n_bootstrap: 1000\n    seed: 42\n    high_sparsity:\n      n_segments: 216\n      n_tokens: 9326\n      ppl_dense: 1.0695\n      ppl_attn: 5.9362\n      ppl_kv: 3.4316\n      ppl_both: 15.7484\n      ii_mean: 6.5954\n      ii_ci:\n      - 1.1114\n      - 11.3791\n      ii_median: 0.7176\n      ii_median_ci:\n      - 0.5959\n      - 0.9347\n      winsorized_mean: 6.5046\n      skewness: -4.6807\n      outlier_count: 3\n    low_sparsity:\n      n_segments: 252\n      n_tokens: 29224\n      ppl_dense: 1.1972\n      ppl_attn: 11.5347\n      ppl_kv: 5.6038\n      ppl_both: 21.6874\n      ii_mean: 2.3883\n      ii_ci:\n      - -8.4602\n      - 11.029\n      ii_median: 1.4587\n      ii_median_ci:\n      - 1.1121\n      - 2.0451\n      winsorized_mean: 5.8911\n      skewness: -7.6074\n      outlier_count: 4\n    mid_sparsity:\n      n_segments: 51\n      n_tokens: 5954\n      ppl_dense: 1.2601\n      ppl_attn: 13.4132\n      ppl_kv: 6.4841\n      ppl_both: 20.8714\n      ii_mean: 4.5407\n      ii_ci:\n      - -4.8854\n      - 12.4605\n      ii_median: 1.1272\n      ii_median_ci:\n      - 0.637\n      - 3.3729\n      winsorized_mean: 6.3284\n      skewness: -3.4048\n      outlier_count: 1\n- exp_id: gsm8k_qw_rand_s030_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    verdict: PASS\n    n_problems: 50\n    n_bootstrap: 1000\n    seed: 42\n    high_sparsity:\n      n_segments: 216\n      n_tokens: 9326\n      null_ratio: 2/50\n      ppl_dense: 1.0695\n      ppl_attn: 6.5613\n      ppl_kv: 4.481\n      ppl_both: 23.7486\n      ii_mean: 11.83\n      ii_median: 2.31\n      ii_ci:\n      - 6.17\n      - 17.04\n      ii_median_ci:\n      - 1.64\n      - 2.81\n      winsorized_mean: 10.55\n      skewness: -2.29\n      outlier_count: 7\n    low_sparsity:\n      n_segments: 252\n      n_tokens: 29224\n      null_ratio: 5/50\n      ppl_dense: 1.1972\n      ppl_attn: 6.3283\n      ppl_kv: 8.5374\n      ppl_both: 56.2304\n      ii_mean: 31.26\n      ii_median: 5.2\n      ii_ci:\n      - 17.84\n      - 47.86\n      ii_median_ci:\n      - 3.95\n      - 7.24\n      winsorized_mean: 16.35\n      skewness: 7.57\n      outlier_count: 4\n    mid_sparsity:\n      n_segments: 51\n      n_tokens: 5954\n      null_ratio: 17/50\n      ppl_dense: 1.2601\n      ppl_attn: 18.6162\n      ppl_kv: 11.6625\n      ppl_both: 47.9019\n      ii_mean: 18.02\n      ii_median: 2.7\n      ii_ci:\n      - 0.09\n      - 36.69\n      ii_median_ci:\n      - 1.46\n      - 8.77\n      winsorized_mean: 18.22\n      skewness: 0.43\n      outlier_count: 2\n- exp_id: acc_qw_dense_b1_8k\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.44\n    correct: 22\n    n_problems: 50\n    truncation_rate: 0.02\n    truncated_count: 1\n    avg_tokens: 759.7\n    max_tokens_generated: 8192\n    max_new_tokens: 8192\n    total_time_seconds: 681.8\n    null_count: 0\n    batch: b1_v2 (problems 1-50, 8k tokens)\n    old_batch1_acc: 0.32\n    old_batch1_correct: 16\n    new_combined_n100_acc: 0.46\n    new_combined_n100_correct: 46\n    batch2_acc: 0.48\n    batch2_correct: 24\n- exp_id: acc_qw_s015_b1_8k\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.46\n    correct: 23\n    total: 50\n    truncation_rate_8k: 0.02\n    gen_over_2k: 3\n    gen_over_2k_all_wrong: true\n    max_gen_length: 8192\n    mean_gen_length: 776\n    batch: b1_v2 (problems 1-50, 8k tokens)\n    batch2_acc: 0.38\n    batch2_correct: 19\n    new_combined_n100_acc: 0.42\n    new_combined_n100_correct: 42\n    batch2_source: acc_qw_s015_n100\n- exp_id: acc_qw_s020_b1_8k\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.26\n    correct: 13\n    n_problems: 50\n    truncation_rate: 0.02\n    truncated_count: 1\n    avg_tokens: 722.1\n    max_tokens_generated: 8192\n    max_new_tokens: 8192\n    total_time_seconds: 729.1\n    null_count: 0\n    batch: b1_v2 (problems 1-50, 8k tokens)\n    old_batch1_acc: 0.26\n    old_batch1_correct: 13\n    new_combined_n100_acc: 0.36\n    new_combined_n100_correct: 36\n    batch2_acc: 0.46\n    batch2_correct: 23\n- exp_id: acc_qw_s025_b1_8k\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy: 0.32\n    correct: 16\n    n_problems: 50\n    truncation_rate: 0.04\n    truncated_count: 2\n    extraction_failures: 6\n    avg_tokens: 797.3\n    total_time_seconds: 831.6\n    batch: b1_v2 (problems 1-50, 8k tokens)\n    batch2_acc: 0.34\n    batch2_correct: 17\n    new_combined_n100_acc: 0.33\n    new_combined_n100_correct: 33\n    batch2_source: acc_qw_s025_n100_b2_fix\n- exp_id: acc_qw_s030_b1_8k\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy: 0.14\n    correct: 7\n    total: 50\n    truncation_rate: 0.04\n    truncated_count: 2\n    extraction_failures: 8\n    max_new_tokens: 8192\n    total_time_seconds: 886.7\n    batch: b1_v2 (problems 1-50, 8k tokens)\n    old_batch1_acc: 0.14\n    old_batch1_correct: 7\n    batch2_acc: 0.24\n    batch2_correct: 12\n    new_combined_n100_acc: 0.19\n    new_combined_n100_correct: 19\n- exp_id: c8_llama_n250\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    first_run_failed: true\n    failure_reason: 'bash wrapper wait logic bug: subprocess OOM/error exits silently,\n      script marks DONE without output validation. All 8 output dirs empty.'\n    fix_worker: worker_code_c8_llama_n250_fix_20260516T031229\n    fix_plan: 1) diagnose script + OOM, 2) fix exit code + output validation + GPU\n      monitor, 3) dry-run 1 condition on GPU 2, 4) full launch on GPU 2-3 via submit_training_job\n- exp_id: c4_think_validation_math500\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    v2_math500_kappa_adaptive: 0.88\n    v2_math500_ds_problems: 48\n    v2_math500_ds_tokens: 32055\n    v2_math500_thinking_in_low: 0.816\n    v2_math500_answer_in_high: 0.655\n    v2_math500_temporal_ordering_ds: 0.576\n    v2_math500_temporal_ordering_qw: 0.479\n    v2_qw_pct_positive: 0.98\n    v2_scope: MATH-500\n    v2_models: DS+QW\n    v2_status: ALL_CRITERIA_MET\n    v1_kappa_adaptive: 0.8804\n    v1_auc: 0.9808\n    SCOPE_FLAG: v2_validated_on_MATH500\n- exp_id: c5_per_phase_gini\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    qw_complete: true\n    ds_complete: true\n    n_problems: 30\n    qw_dense_gini_baselines:\n      low: 0.2675\n      mid: 0.2078\n      high: 0.2599\n    qw_importance:\n      s015:\n        global_delta: -0.0103\n        low_delta: -0.0165\n        mid_delta: -0.0094\n        high_delta: -0.012\n      s020:\n        global_delta: -0.0121\n        low_delta: -0.02\n        mid_delta: -0.0115\n        high_delta: -0.0143\n      s025:\n        global_delta: -0.01\n        low_delta: -0.0286\n        mid_delta: -0.0168\n        high_delta: -0.0207\n      s030:\n        global_delta: -0.0202\n        low_delta: -0.035\n        mid_delta: -0.0183\n        high_delta: -0.0239\n    qw_random:\n      s015:\n        global_delta: -0.0186\n        low_delta: -0.0083\n        mid_delta: -0.0038\n        high_delta: -0.0036\n      s020:\n        global_delta: -0.0229\n        low_delta: -0.0119\n        mid_delta: -0.0053\n        high_delta: -0.0067\n      s025:\n        global_delta: -0.0337\n        low_delta: -0.0014\n        mid_delta: -0.0081\n        high_delta: 0.0045\n      s030:\n        global_delta: -0.0447\n        low_delta: -0.0221\n        mid_delta: -0.0077\n        high_delta: -0.0061\n    ds_importance:\n      s015:\n        global_delta: -0.0301\n        low_delta: -0.0163\n        mid_delta: -0.0073\n        high_delta: -0.0152\n      s020:\n        global_delta: -0.0404\n        low_delta: -0.0209\n        mid_delta: -0.0092\n        high_delta: -0.02\n      s025:\n        global_delta: -0.0647\n        low_delta: -0.0313\n        mid_delta: -0.0133\n        high_delta: -0.0267\n      s030:\n        global_delta: -0.0806\n        low_delta: -0.0373\n        mid_delta: -0.0183\n        high_delta: -0.0314\n    ds_random:\n      s015:\n        global_delta: -0.0309\n        low_delta: -0.0102\n        mid_delta: -0.0006\n        high_delta: -0.0062\n      s020:\n        global_delta: -0.0403\n        low_delta: -0.012\n        mid_delta: -0.0007\n        high_delta: -0.0085\n      s025:\n        global_delta: -0.062\n        low_delta: -0.015\n        mid_delta: -0.0096\n        high_delta: -0.0112\n      s030:\n        global_delta: -0.0732\n        low_delta: -0.0183\n        mid_delta: -0.0093\n        high_delta: -0.0138\n    key_finding: 'Both models: importance pruning low-phase Gini delta consistently\n      largest and monotonically increases with sparsity (DS: -0.016 to -0.037; QW:\n      -0.017 to -0.035). Random pruning shows weaker per-phase structure. Supports\n      discrimination collapse hypothesis.'\n- exp_id: c9_gsm8k_power_analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    min_detectable_d_n50: 0.4042\n    random_conditions_all_NS: true\n    random_max_abs_d: 0.164\n    random_conditions:\n      ds_rand_s015_d: -0.017\n      ds_rand_s015_power: 0.052\n      ds_rand_s020_d: -0.063\n      ds_rand_s020_power: 0.072\n      ds_rand_s025_d: 0.026\n      ds_rand_s025_power: 0.054\n      ds_rand_s030_d: 0.058\n      ds_rand_s030_power: 0.069\n      qw_rand_s015_d: -0.154\n      qw_rand_s015_power: 0.187\n      qw_rand_s020_d: 0.113\n      qw_rand_s020_power: 0.123\n      qw_rand_s025_d: 0.163\n      qw_rand_s025_power: 0.203\n      qw_rand_s030_d: 0.165\n      qw_rand_s030_power: 0.207\n    qw_importance_adequately_powered:\n      s025_d: 0.62\n      s025_power: 0.99\n      s030_d: 0.64\n      s030_power: 0.99\n    REVIEWER_WARNING: t-test Cohen's d power analysis ONLY valid for random conditions.\n      Importance conditions have heavy-tail distributions where t-test severely misestimates\n      (e.g. DS s030 d=0.008 but Wilcoxon p=0.0001). DO NOT cite importance t-test\n      power in paper.\n    paper_citable_conclusions:\n    - 'Random: all 8 conditions NS (max|d|=0.164), n=50 detects d>=0.40 → absence\n      of evidence not evidence of absence'\n    - QW importance s025/s030 adequately powered (d≈0.63, power>0.99)\n- exp_id: c10_lang_switching\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    method: CPU analysis of existing gen_snippet data (3/5 sparsities)\n    coverage: dense, s015, s030 (s020/s025 missing gen_snippet)\n    n_per_sparsity: 50\n    dense:\n      switch_rate: 0\n      cn_count: 0\n      en_count: 50\n      cn_acc: null\n      en_acc: 0.52\n    s015:\n      switch_rate: 0.04\n      cn_count: 2\n      en_count: 48\n      cn_acc: 0\n      en_acc: 0.375\n    s030:\n      switch_rate: 0.4\n      cn_count: 20\n      en_count: 30\n      cn_acc: 0.1\n      en_acc: 0.1\n    trend: 'Monotonically increasing: 0% → 4% → 40%. Chinese responses have much lower\n      accuracy (10% at s030 vs 52% dense English).'\n    checkpoint_path: /root/autodl-tmp/pacs/results_c10_lang_cpu.json\n- exp_id: c8_llama_n250_fixed\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_problems: 250\n    model: DeepSeek-R1-Distill-Llama-8B\n    conditions_completed: 8/8\n    importance:\n      s015:\n        median_gradient: 0.050099\n        ci:\n        - 0.045477\n        - 0.058804\n        wilcoxon_p: 1.44e-29\n        cohens_dz: 0.814\n        monotonic: true\n      s020:\n        median_gradient: 0.158708\n        ci:\n        - 0.141193\n        - 0.181937\n        wilcoxon_p: 8.94e-35\n        cohens_dz: 1.01\n        monotonic: true\n      s025:\n        median_gradient: 0.376131\n        ci:\n        - 0.315704\n        - 0.402861\n        wilcoxon_p: 4.3e-39\n        cohens_dz: 1.1151\n        monotonic: true\n      s030:\n        median_gradient: 0.695435\n        ci:\n        - 0.639426\n        - 0.770102\n        wilcoxon_p: 1.48e-40\n        cohens_dz: 1.15\n        monotonic: true\n    random:\n      s015:\n        median_gradient: 0.025489\n        ci:\n        - 0.019942\n        - 0.033342\n        wilcoxon_p: 9.28e-13\n        cohens_dz: 0.4359\n        monotonic: true\n      s020:\n        median_gradient: 0.065003\n        ci:\n        - 0.052258\n        - 0.088191\n        wilcoxon_p: 3.63e-15\n        cohens_dz: 0.4588\n        monotonic: true\n      s025:\n        median_gradient: 0.184201\n        ci:\n        - 0.112738\n        - 0.247119\n        wilcoxon_p: 3.75e-13\n        cohens_dz: 0.4239\n        monotonic: true\n      s030:\n        median_gradient: 0.270653\n        ci:\n        - 0.193489\n        - 0.368089\n        wilcoxon_p: 6.0e-12\n        cohens_dz: 0.4104\n        monotonic: true\n    dose_response_monotonic: true\n    imp_rand_ratio_range: 1.97-2.57x\n    all_conditions_significant: true\n    importance_effect_size_range: 0.81-1.15 (large)\n    random_effect_size_range: 0.41-0.46 (medium)\n- exp_id: c10-lang-s020-s025\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: c10_lang_s020_s025\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    s020:\n      n: 50\n      accuracy: 0.26\n      switch_rate: 0.14\n      switch_count: 7\n      mean_cn_ratio: 0.066\n      cn_acc: 0.333\n      en_acc: 0.25\n    s025:\n      n: 50\n      accuracy: 0.1\n      switch_rate: 0.32\n      switch_count: 16\n      mean_cn_ratio: 0.152\n      cn_acc: 0.2\n      en_acc: 0.057\n    wall_time_s: 11680.6\n    output_path: /root/autodl-tmp/pacs/results_c10_lang_s020_s025.json\n- exp_id: c8_llama_gpu0_s025\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_problems: 250\n    n_bootstrap: 1000\n    segmentation: quantile\n    per_phase_ii_median:\n      high: 0.0171\n      mid: 0.1916\n      low: 0.388\n    per_phase_ii_mean:\n      high: 0.0218\n      mid: 0.2126\n      low: 0.4713\n    phase_gradient_median_diff: 0.3761\n    phase_gradient_median_diff_ci95:\n    - 0.3147\n    - 0.4039\n    wilcoxon_p_one_sided: 4.3e-39\n    bonferroni_p_k4: 1.72e-38\n    cohens_dz: 1.1174\n    rank_biserial_r: 0.8689\n    n_paired: 244\n    pos_neg_ratio: 228/16\n- exp_id: gpqa_ds_importance_s015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_problems: 198\n    interaction_index:\n      high:\n        mean: 0.191363\n        median: 0.012758\n        ci:\n        - 0.047972\n        - 0.514786\n        median_ci:\n        - 0.011463\n        - 0.013936\n        winsorized_mean: 0.039667\n        skewness: 77\n      mid:\n        mean: 0.87787\n        median: 0.102412\n        ci:\n        - 0.72315\n        - 1.039118\n        median_ci:\n        - 0.092683\n        - 0.115074\n        winsorized_mean: 0.532911\n        skewness: 7.7\n      low:\n        mean: 5.991797\n        median: 0.960161\n        ci:\n        - 5.235965\n        - 6.732278\n        median_ci:\n        - 0.892882\n        - 1.03306\n        winsorized_mean: 3.945337\n        skewness: 8.88\n    perplexity:\n      high:\n        dense: 1.1777\n        attn: 1.5205\n        kv: 1.702\n        both: 2.2531\n      mid:\n        dense: 1.3075\n        attn: 1.6733\n        kv: 3.2369\n        both: 4.7222\n      low:\n        dense: 1.4216\n        attn: 1.9771\n        kv: 19.3067\n        both: 27.6495\n    phase_stats:\n      high:\n        n_tokens: 479658\n        n_segments: 6261\n      mid:\n        n_tokens: 276409\n        n_segments: 2185\n      low:\n        n_tokens: 465085\n        n_segments: 5128\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: false\n      overall: PASS\n    gradient_direction: low > mid > high\n    median_ratio_low_high: 75.2\n- exp_id: gpqa_ds_importance_s020\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: recency_s025\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    phase_gradient:\n      median_diff: 1.1186\n      cohens_dz: 0.2205\n      p_value: 0.00922\n      significant: true\n      direction: reversed (low_sparsity more damaged)\n    comparison_importance_s025:\n      importance_median_diff: -1.0745\n      importance_cohens_dz: -0.7778\n      importance_p_value: 1.06e-68\n      gradient_directions_opposite: true\n      importance_effect_3.5x_stronger: true\n    comparison_random_s025:\n      random_median_diff: -0.3931\n      random_cohens_dz: -0.0172\n      random_p_value: 1.59e-11\n    interaction_index:\n      high_sparsity_median: -0.000346\n      mid_sparsity_median: -0.02246\n      low_sparsity_median: -0.091106\n    config:\n      model: DeepSeek-R1-Distill-Qwen-7B\n      masking_method: recency\n      sparsity: 0.25\n      n_problems: 100\n      seed: 42\n- exp_id: recency_s030\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    phase_gradient:\n      median_diff: -1982.57\n      ci_low: -9391.77\n      ci_high: 882.08\n      cohens_dz: -0.096\n      p_value: 0.114\n      significant: false\n      effect_size: negligible\n    comparison_importance_s030:\n      median_diff: 8.48\n      cohens_dz: 0.33\n      p_value: 1.09e-79\n      significant: true\n    comparison_random_s030:\n      median_diff: 0.51\n      cohens_dz: -0.049\n      p_value: 0.00148\n      significant: true\n    interaction_index:\n      high_sparsity_median: -0.0018\n      mid_sparsity_median: -0.016\n      low_sparsity_median: 0.1099\n    n_problems: 100\n    model: DeepSeek-R1-Distill-Qwen-7B\n    masking_method: recency\n    sparsity: 0.3\n- exp_id: recency_s015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_problems: 100\n    model: DeepSeek-R1-Distill-Qwen-7B\n    masking_method: recency\n    sparsity: 0.15\n    phase_gradient:\n      median_diff: -0.0026\n      cohens_dz: 0.083\n      p_value: 0.77\n      significant: false\n    comparison_importance_s015:\n      median_diff: 0.39\n      cohens_dz: 0.574\n      p_value: < 1e-70\n      significant: true\n    comparison_random_s015:\n      median_diff: 0.014\n      cohens_dz: -0.045\n      p_value: 0.86\n      significant: false\n    interpretation: Recency eviction shows NO phase gradient (NS, negligible effect),\n      confirming phase-dependent severity is attention-score-specific\n- exp_id: gpqa_ds_importance_s025\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: gpqa_ds_importance_s030\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: gpqa_ds_random_s020\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-17T01:44:08.721Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-17T01:44:08.721Z",
  "sessionId": "5ce792ab-ebc9-4b52-8f9c-3b1fb1b17c1f"
}
```

---

## Round 1

20 recorded events

### User

_source line 3 · 2026-05-17T01:44:08.748Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：GPQA random 也显示强 gradient（ratio ≈ 1×）+ 审稿人认为现象是 trivial（token removal 的必然后果而非 scoring-specific）+ 需要完全 reframe 核心 claim
核心假设：['GPQA importance gradient 存在但 random 同样强（imp/rand ratio < 2×，类似 LLaMA 模式）', '审稿人质疑：如果 random 在长推理链 benchmark 上也有 gradient，那 "importance-specific" claim 不成立', 'Recency control 的 null 结果被审稿人解读为 "recency 太弱（保留最近 token 本身就是好策略），不是有效 control"', '审稿人认为 discrimination collapse 机制只是 obvious 的 "pruning reduces score quality" 重述', 'C5b mitigation pilot 失败被视为 "连 direction 都不确定" 的 negative signal']
关键指标范围：{'gpqa_importance_median_gradient_s030': [1.5, 4.0], 'gpqa_imp_rand_ratio': [1.0, 2.0], 'cross_benchmark_specificity_range': '仅 MATH-500 DS ratio > 5×; 其余所有条件 < 3×', 'recency_max_dz_across_sparsities': [0.0, 0.15], 'reviewer_novelty_score': [2.0, 3.0], 'reviewer_overall_score': [2.5, 3.0], 'acceptance_probability': [0.08, 0.25]}
叙事方向：Reframe：核心贡献不再是 'importance-specific phase interaction'，而是 'phase-dependent compound severity is a universal phenomenon whose magnitude scales with eviction method discriminativeness'。新叙事逻辑：任何 non-trivial eviction（importance/random）都产生 phase-dependent compound severity，但 severity magnitude 与 eviction method 的 token discrimination strength 正相关（importance > random >> recency≈null）。Recency 的 null 不是因为 scoring-independent，而是因为 recency 作为 eviction 策略本身 preserves temporal locality（对 reasoning 相对温和）。这个 reframe 仍然是新发现（prior work 未量化），但 novelty claim 从 'qualitative dissociation' 降为 'quantitative scaling law'。同一 venue（EMNLP），但需要重写 intro + framing + 补充 eviction discriminativeness 的量化指标（如 eviction overlap with oracle）。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: phase-gated-compound-sparse
focus: Key improvements since last dream: (1) recency scoring-independent control confirms phase gradient is attention-score-specific (three-way dissociation: importance/random/recency), (2) full 8-condition LLaMA cross-architecture validation (n=250, all PASS), (3) expanded related work (50 citations), (4) "why not causal" self-defense in discussion, (5) dense baseline phase stats. Evaluate whether these address the previous dream's main criticisms: narrow novelty, circularity concern, thin references, no figures, no practical method.

## paper_framing.md

# Paper Framing — Phase-Gated Compound Sparsity

> 最后更新: 2026-05-17 (D102: C11 confirmed — recency triple NS across s015/s025/s030; s015+s025 primary, s030 supplementary) | 维护者: Director

## Core Insight

Compound sparsity（attention head pruning + KV cache eviction）的 severity 不是固定常数——它是 eviction strategy 和 reasoning phase 交互的涌现属性。Importance-based eviction 的 compound interaction severity（paired median difference: median(II_low_i − II_high_i)）随 sparsity 单调递增（DeepSeek: 0.39→1.21→3.99→8.48; Qwen: 0.07→0.31→1.07→3.16），而 random masking 在 s015/s020 NS，在 s025 跨模型显著但效应量远小于 importance（DS: 0.257 vs 3.986; QW: 0.393 vs 1.074, 2.7-17×差异），存在 sparsity threshold ~s020-s025（D063; s030 待定）。Cohen's d（per-problem paired, B=10000）从 medium 到 large（DeepSeek: 0.61→1.13; Qwen: 0.37→1.44，registry cohens_d s015→s030）。LLaMA 跨架构验证（D060, c8_llama_n250_fixed, n=250）：within-importance phase gradient 强（d_z=0.81-1.15, all p<10^-29, all monotonic），且 random 在 LLaMA 上所有条件均显著（d_z=0.41-0.46, all p<10^-12），imp/rand Δ ratio 仅 2.0-2.6×（vs DeepSeek 15-17×），strategy×phase 交互强度 architecture-dependent。GSM8K 跨 benchmark 验证（D075）：importance masking 的 phase gradient 在 GSM8K 上同样单调递增（QW: 0.039→0.158→1.100→2.092; DS: 0.241→0.740→1.992→4.682），但 strategy specificity（importance/random gradient ratio）从 MATH-500 的 15-17× 衰减至 GSM8K 的 2.3-3.8×。注意："反转"仅在原始 II_low 值上（random > importance），phase gradient 层面 importance ≥ random。Strategy specificity 的 task-dependence 机制是开放问题（见 §6 Discussion）。这一发现挑战了 compound degradation 均匀分布的隐含假设。

**数字基准**：所有数字基于 bf16 per-problem paired 统计量（B=10000 bootstrap）。median_diff 定义为 median(II_low_i − II_high_i)（逐 problem 配对差的中位数）。fp16 旧数据已弃用。

## Narrative Arc

Compound sparsity 是高效 LLM 推理的实用部署需求，但 prior work（SparK, Ada-KV, SLiM）将 compound interaction 视为均匀超可加。我们发现 severity 是 strategy × phase 交互的涌现属性：importance eviction 的 compound interaction 在 low-sparsity phase 远大于 high-sparsity phase（paired median difference 单调递增 0.39→8.48），而 random eviction 在低 sparsity (s015/s020) NS，在 s025+ 跨模型显著但效应量远小于 importance (2.7-17×)——存在 sparsity threshold (~s020-s025)，低于阈值 compound effect importance-specific，高于阈值两者均触发但 importance 主导。Cross-model replication 方向一致（Qwen magnitude ~1/4 of DeepSeek，onset threshold s≥0.20）。LLaMA 跨架构验证已完成（c8_llama_n250_fixed, n=250, D060）：within-importance phase gradient 强（d_z=0.81-1.15, all p<10^-29），random 所有条件显著（d_z=0.41-0.46, all p<10^-12），但 imp/rand ratio 仅 2.0-2.6×（远低于 DS 15-17×），strategy×phase 交互强度 architecture-dependent。Recency-based eviction（scoring-independent control, D100/D102）跨三个 sparsity level 均产生 null phase gradient（s015+s025 为 primary evidence，s030 supplementary due to numerical instability at extreme sparsity），确认 phase-dependent severity 是 attention-score-based eviction 的特有交互效应而非 token removal 的 trivial 副产物。我们通过 discrimination collapse 机制解释这一现象：head pruning → importance score 的判别力崩塌（Gini/CV 下降跨模型一致）→ importance eviction 退化为有偏伪随机。Attention entropy redistribution 作为 model-dependent secondary effect 在 DeepSeek 上观察到，但在 Qwen 上不稳健（D044）。

**Framing 硬约束（D015）**：
- MUST: \"emergent phase-strategy interaction\"
- MUST NOT: \"importance metric limitation / importance is broken\"
- MUST NOT: claim \"importance masking produces super-additive interaction\" without qualifier — random masking also produces positive II, and at s025+ random is statistically significant (D063). The distinguishing signal is **magnitude gradient** (importance 2.7-17× larger) and **onset threshold** (random NS below ~s020, importance significant from s015+), not the existence of super-additivity itself (D023)

## Core Claims

| ID | Claim | Status | Key Evidence |
|----|-------|--------|-------------|
| C1 | Compound sparsity severity is strategy- and task-modulated | confirmed | MATH-500: importance gradient 15-17× random (DeepSeek s025-s030); GSM8K: ratio 衰减至 2.3-3.8× (D075)。Phase gradient 层面 importance ≥ random 跨 benchmark 成立，但 magnitude ratio task-dependent。Threshold ~s020-s025 (D063) |
| C2 | Severity is phase-modulated (amplified in low-sparsity phase) | confirmed | bf16 paired median difference 单调递增: 0.39→1.21→3.99→8.48; Bonferroni p<0.005 全 4 水平 (D032)。预注册：n=500 后若 QW s015 CI 仍跨零，叙事改为 'compound effect emerges above threshold sparsity (~s020)' |
| C3 | Phase-strategy crossover exists | confirmed | s=0.25: importance high_phase=0.032 < random=0.818, importance low_phase=7.196 > random=1.363 (bf16) |
| C4 | Discrimination collapse as primary mechanism; entropy redistribution model-dependent | partially_confirmed | D044: Gini/CV 下降跨模型一致; entropy collapse DeepSeek 一致但 Qwen s025 反转(+0.045) s030≈0。30/30 problems completed. |
| C5 | Phase-modulated compound severity generalizes across models | confirmed | DeepSeek + Qwen cross-model replication: 方向一致, Cohen's d ρ=1.0, gradient permutation p=0.043. Qwen magnitude ~1/4 of DeepSeek, onset threshold s≥0.20 (S3→C). |
| C5b | Phase-aware mitigation recovers compound degradation | future_work | D056: pilot 完成 gate_failed。Oracle recovery 18% < 30% gate (Wilcoxon p=0.002)，heuristic 32% 但 CI 跨零。方向正确但效应量不足，需更精细 phase boundary estimation → future work |
| C6 | Severity gradient is sub-exponential | confirmed | Growth rate decreasing: Δ增长因子 3.8×→4.8×→2.0×（递减） |
| C7 | Statistical power at n=500 confirms dose-response | confirmed | c2_n500_deepseek (success) + c2_qw_n500_r3 (success): 两模型 n=500 全 4 sparsity Bonferroni p<0.005, Spearman ρ=1.0 |
| C8 | Cross-architecture validation (LLaMA) | confirmed | c8_llama_n250_fixed (n=250, D060): within-importance phase gradient d_z=0.81-1.15 (all p<10^-29, all monotonic) ✓。Random 所有条件显著 (d_z=0.41-0.46, all p<10^-12)，与 DeepSeek/Qwen random 低 sparsity NS 模式定性不同。Imp/rand Δ ratio 2.0-2.6×（远低于 DS 15-17×）。Strategy specificity architecture-dependent。n=250 功效充分。 |
| C9 | Differentiation from Lethe/SparK prior work | planned | Related Work §2 引用区分 + SparK gap analysis |
| C10 | Phase gradient cross-benchmark robust; strategy specificity task-modulated | confirmed | GSM8K DS gradient 0.241→4.682 单调递增; QW gradient 0.039→2.092; imp/rand ratio 衰减至 2.3-3.8× (D075)。QW random s025+s030 均 success |
| C11 | Phase-dependent severity absent under scoring-independent eviction (recency control) | confirmed | D102: 三个 sparsity level 全部 NS。s015+s025 为 primary evidence (n=100 each, both d_z < 0.1, p > 0.5); s030 supplementary (numerical instability at extreme sparsity)。对比 importance: d_z=0.574-1.15, ratio=119.8×。Triple dissociation confirmed: importance 有 gradient, recency + random 均 NS。排除 (a) phase segmentation circularity (b) H2O scoring pathway confound。文献中无先例将 recency eviction 作为 methodological control (experimental design contribution)。 |
| S3→C | Onset threshold is model-dependent (DeepSeek s≥0.15, Qwen s≥0.20) | confirmed | D037/D038: Qwen s015 d_z=0.37 CI含0, s020+ 显著 |
| S7→C | Dose-response monotonicity (Spearman ρ=1.0) | confirmed | D047: 6-point dose-response, 单调递增 |

## Anticipated Reviewer Concerns

### RC1: Generalizability — 7B models only, benchmark scope
- **预期质疑**: \"Results on two 7B models and MATH-500 only. How do we know this generalizes to larger models or other reasoning tasks?\"
- **应对**: 四层泛化证据：(1) Cross-model: DeepSeek-R1-Distill-Qwen-7B + Qwen2.5-7B-Instruct（同架构不同训练，ρ=1.0）(2) Cross-architecture: c8_llama_n250_fixed (DeepSeek-R1-Distill-Llama-8B, LlamaForCausalLM, n=250)，within-importance phase gradient 强 (d_z=0.81-1.15)，但 strategy specificity 弱于 Qwen2 架构（2.0-2.6× vs 15-17×），strategy×phase 交互强度 architecture-dependent (3) **Cross-benchmark (D075)**: GSM8K（两模型）phase gradient 单调递增复现（DS: 0.241→4.682; QW: 0.039→2.092），但 strategy specificity ratio 从 MATH-500 15-17× 衰减至 2.3-3.8×，表明 phase modulation 跨 benchmark 稳健而 magnitude modulation task-dependent。Limitations 诚实声明：(a) 7B scale only；(b) strategy specificity 强度 task-dependent（GSM8K 衰减，可能因推理链更短）；(c) random phase gradient 行为 architecture-dependent。
- **实验支撑**: C5 (cross-model) + C8 (c8_llama_n250_fixed cross-architecture, n=250) + C10 (cross-benchmark GSM8K, D075)

### RC2: Methodology — phase segmentation circularity and scoring confound
- **预期质疑**: \"Your phase segmentation uses perplexity computed from the same model whose sparsity you're measuring. Isn't this circular? And H2O's attention-score mechanism could itself create the phase gradient artifact.\"
- **应对**: Recency-based eviction (scoring-independent control, D102 confirmed) produces null phase gradient across all three sparsity levels (s015+s025 primary, s030 supplementary), confirming the observed severity pattern is specific to attention-score-based methods, not an artifact of (a) phase segmentation itself or (b) the scoring computation pathway. Triple dissociation: importance shows gradient (d_z=0.574+), recency and random both NS. Novel experimental design: repurposing recency eviction as methodological control has no precedent in literature (H2O/StreamingLLM use it only as performance baseline).
- **实验支撑**: C11 (recency_s015/s025/s030, D102 confirmed) + c4_entropy (discrimination collapse mechanism, D044)

### RC3: Practical impact — 没有 throughput 数据
- **预期质疑**: \"No wall-clock or throughput measurements. Is the severity amplification reflected in actual inference speed?\"
- **应对**: 本文定位是 empirical finding paper（发现 + 机制解释），不是 method paper。Throughput 不是 claim 的一部分。Discussion 中明确 phase-gated controller 作为 future direction。
  - C5b pilot 已完成（D056）：oracle recovery 18%（Wilcoxon p=0.002），heuristic recovery 32%（p=0.024），但两者 95% CI 均跨零。方向正确（Wilcoxon 显著）但效应量不足（未达 30% gate），需更精细的 phase boundary estimation。论文 §6 Discussion 诚实报告 pilot 结果 + future work。
  - Heuristic > oracle 悖论值得提及：token position ratio 粗粒度划分可能恰好更适合 mitigation 场景，暗示 phase boundary 的最优粒度是开放问题。
- **实验支撑**: c5b_pilot (gate_failed, D056)

### RC4: Statistical rigor — bootstrap 是否足够
- **预期质疑**: \"Per-problem bootstrap with 50 problems — sufficient sample size?\"
- **应对**: bf16 使用 B=10000 per-problem paired bootstrap，有效配对数 n=49 (DeepSeek) / n=46 (Qwen)；n=500 实验进一步验证 (C7 confirmed)。Permutation test 使用 paired median difference 作为 robust statistic（D032），Bonferroni 校正后全 4 水平 p<0.005。Dose-response 主用 Wilcoxon signed-rank p + median_diff（robust to outliers），Cohen's d 作为辅助效应量（DeepSeek 0.61→1.13, Qwen 0.37→1.44, registry cohens_d s015→s030），注释高 sparsity 下 d 受 outlier-driven variance 影响（DS s020→s025: median 3.3× jump 但 d 非单调，因极端 II 值影响分母，D064）。可在 appendix 补充 per-problem 分布图（已生成 fig4_per_problem_dist.pdf）。
- **实验支撑**: bf16 permutation test (D032) + Cohen's d per-problem paired (rebootstrap B=10000) + n=500 Wilcoxon (C7 confirmed)

### RC5: Novelty — prior work 是否已覆盖 phase-dependent sparsity
- **预期质疑**: "ThinKV and phase-aware methods already consider phase. What's new?"
- **应对**: Prior work 在单轴上分析 phase（ThinKV: phase-aware eviction）或 compound（SparK: joint compression）。没有工作同时分析 compound × phase × strategy 的三维交互。Crossover 现象（同一 strategy 在不同 phase 方向反转）是全新发现。Related Work 加 Lethe 引用区分 + SparK 对比。具体区分：
  - **ThinKV** (arxiv 2510.01290, Oct 2025): 在 KV cache 单轴上做 phase-aware 压缩（按 CoT 阶段差异化 eviction），但不涉及 pruning × eviction 的 compound interaction。我们研究的是双轴（head pruning × KV eviction）compound interaction 如何随 phase 变化，ThinKV 的单轴 phase-aware 策略是我们分析维度的子集。
  - **Physics of KV Cache Compression** (arxiv 2603.01426, Mar 2026): 揭示了单轴 KV 压缩的 phase transition 和 representational rigidity，是机制层面最接近的工作。关键区分：他们刻画的是单一压缩轴上压缩率的 critical threshold（phase transition），我们刻画的是两种压缩方法的 compound interaction severity 如何被 reasoning phase 调制（phase-dependent gradient）——维度正交。
  - **HIES** (arxiv 2510.13832, Oct 2025): 发现 importance score collapse 并提出 entropy 补偿，为我们的 discrimination collapse 机制提供独立 supporting evidence——他们在单轴上观察到的 score collapse 正是我们在 compound setting 中发现的 Gini/CV 下降的单轴对应。
  - **R-KV** (arxiv 2505.24133, May 2025): 针对 reasoning task 做 KV compression 优化，属于 task-specific method。我们不是提出新方法，而是 mechanistic 分析 compound interaction 的 phase-dependent 行为，二者目标不同（optimization vs understanding）。
- **实验支撑**: C3 (crossover), Related Work §2 的 gap 分析

### RC6: Novelty vs Lethe/SparK
- **预期质疑**: "How does this differ from Lethe (AAAI 2026) which also does layer-time-adaptive KV pruning, or SparK which studies compound compression?"
- **应对**: Lethe 和 SparK 都没有分析 phase × strategy 的交互效应。Lethe 是 method paper（提出 adaptive eviction 方法），我们是 empirical finding paper（发现 phase-dependent severity gradient）。SparK 研究 compound compression 但将 interaction 视为均匀超可加，我们发现 interaction severity 随 phase 和 strategy 变化。新近工作进一步确认我们的独特定位：
  - **Physics of KV Cache Compression** (arxiv 2603.01426, Mar 2026) 是最近的相关工作，研究单轴压缩的 phase transition 阈值行为。与我们的核心区别：他们的 phase transition 是压缩率维度上的 critical point，我们的 phase-dependent gradient 是 reasoning phase 维度上 compound interaction 的连续调制——两者刻画的 "phase" 语义不同（compression-rate phase vs reasoning phase）。
  - **ThinKV** (arxiv 2510.01290, Oct 2025) 和 **R-KV** (arxiv 2505.24133, May 2025) 都在 KV compression 单轴上引入 phase/reasoning awareness，但均未涉及 compound interaction。我们的贡献在于揭示 pruning × eviction 双轴交互如何被 reasoning phase 调制，这是单轴方法无法观察到的涌现现象。
  - **HIES** (arxiv 2510.13832, Oct 2025) 的 importance score collapse 发现为我们的 discrimination collapse 机制提供了独立佐证，但 HIES 聚焦于单轴补偿方法，未研究 collapse 在 compound setting 中的放大效应。
  - Related Work §2 明确区分三者定位：Lethe/SparK = method/compound method, ThinKV/R-KV = single-axis phase-aware, Physics of KV = single-axis phase transition, HIES = single-axis collapse。我们 = compound × phase × strategy 三维交互分析。
- **实验支撑**: 不需要额外实验，仅需 §2 引用区分

## Paper Positioning

**类型**: Empirical finding paper（非 method paper）
**核心贡献**:
1. 发现 compound sparsity severity 的 strategy × phase 交互
2. 量化 severity gradient（bf16 paired median difference 0.39→8.48, Cohen's d 0.61→1.13）和 crossover 现象
3. 提出 discrimination collapse 机制解释（Gini/CV 跨模型一致；entropy redistribution model-dependent）
4. Cross-model + cross-architecture (LLaMA, n=250) replication 验证泛化性（三模型两架构；strategy×phase 交互强度 architecture-dependent, D060）
5. Novel use of scoring-independent eviction (recency-based) as methodological control — experimental design contribution 排除 phase segmentation circularity 和 scoring pathway confound (C11, D102 confirmed)

**投稿目标**: EMNLP 2026 ARR, deadline 2026-05-25
**Rebuttal 准备**: Day 9 (2026-05-23) 预留 rebuttal letter 写作时间
**关键时间线**：
- Day 9 (2026-05-23): 预留写 rebuttal letter
- Day 11 (2026-05-25): EMNLP 2026 ARR 截稿


## experiment_plan (with registry status)

- id: c1_bf16_importance_s025
  claim: C1
  description: 'II median: high=0.032, mid=1.118, low=7.196; importance masking shows
    strong phase gradient'
  registry_id: bf16_importance_s025
  role: primary
  priority: high
  status: DONE
  conclusion: success
  metrics: &id003
    interaction_index:
      high:
        mean: 0.302756
        median: 0.032363
        ci:
        - 0.083714
        - 0.543977
        winsorized_mean: 0.200962
        skewness: 4.8826
      mid:
        mean: 5.729665
        median: 1.118069
        ci:
        - 3.455574
        - 8.471799
        winsorized_mean: 4.189902
        skewness: 8.2799
      low:
        mean: 25.852951
        median: 7.195958
        ci:
        - 19.077082
        - 33.497293
        winsorized_mean: 19.319103
        skewness: 7.3986
    per_problem_ii_stats:
      high:
        n: 49
        min: -0.316321
        max: 4.003714
        mean: 0.133714
        median: 0.009873
        std: 0.595358
      mid:
        n: 40
        min: -0.024794
        max: 18.720486
        mean: 2.537744
        median: 1.05707
        std: 3.962575
      low:
        n: 50
        min: -1.854733
        max: 75.467653
        mean: 11.28281
        median: 3.954593
        std: 16.620011
    gradient_paired_aggregate_legacy: 222.35
    median_difference: 7.1636
    n_problems: 50
    pass_fail:
      ci_overlap: true
      sign_reversal: false
      overall: PASS
    phase_stats:
      high:
        n_tokens: 21086
        n_segments: 387
      mid:
        n_tokens: 13306
        n_segments: 191
      low:
        n_tokens: 27748
        n_segments: 397
    perplexity:
      high:
        dense: 1.1689
        attn: 1.6511
        kv: 1.8628
        both: 2.7026
      mid:
        dense: 1.2269
        attn: 1.7039
        kv: 5.6205
        both: 13.3436
      low:
        dense: 1.2286
        attn: 1.8366
        kv: 31.756
        both: 63.668
- id: c1_bf16_ds_rand_s025
  claim: C1
  description: 'Random II median: high=0.818, mid=0.932, low=1.363; flat gradient
    vs importance'
  registry_id: bf16_ds_rand_s025
  role: primary
  priority: high
  status: DONE
  conclusion: success
  metrics:
    interaction_index:
      high:
        mean: 3.59
        median: 0.8182
        ci:
        - 1.4021
        - 6.2327
        median_ci:
        - 0.5075
        - 1.7217
        winsorized_mean: 6.3965
        skewness: -7.57
      mid:
        mean: -1.8455
        median: 0.9324
        ci:
        - -10.3663
        - 4.9342
        median_ci:
        - 0.7331
        - 1.7003
        winsorized_mean: 3.1014
        skewness: -12.76
      low:
        mean: 0.7212
        median: 1.3627
        ci:
        - -4.2068
        - 4.5006
        median_ci:
        - 1.0869
        - 2.6866
        winsorized_mean: 4.1866
        skewness: -15.85
    perplexity:
      high:
        dense: 1.1687
        attn: 7.237
        kv: 4.9751
        both: 17.7423
      mid:
        dense: 1.2269
        attn: 868.3199
        kv: 5.1165
        both: 29.4661
      low:
        dense: 1.2284
        attn: 24.3571
        kv: 6.7993
        both: 17.9694
    phase_stats:
      high:
        n_tokens: 21086
        n_segments: 387
      mid:
        n_tokens: 13306
        n_segments: 191
      low:
        n_tokens: 27748
        n_segments: 397
    n_problems: 50
    pass_fail:
      ci_overlap: false
      sign_reversal: false
      overall: FAIL
    median_difference: 0.5445
- id: c1_bf16_qw_imp_s025
  claim: C1
  description: 'Qwen cross-model: median_diff=1.109, Cohen''s d=1.233, p<1e-5'
  registry_id: bf16_qw_imp_s025
  role: supporting
  priority: medium
  status: DONE
  conclusion: success
  metrics:
    median_difference: 1.108706
    permutation_p: 0
    cohens_d: 1.2329
    bootstrap_ci_95:
    - 0.609247
    - 1.469002
    wilcoxon_p: 0
    n_bootstrap: 10000
    n_paired: 46
- id: c1_sf5_asymmetric_spot
  claim: C1
  description: 'Asymmetric configs: h02_kv03 D=19.13, h03_kv02 D=18.25; gradient consistent'
  registry_id: sf5_asymmetric_spot
  role: ablation
  priority: medium
  status: DONE
  conclusion: success
  metrics:
    config_a_h02_kv03:
      II_low: 19.51
      II_mid: 6.05
      II_high: 0.38
      D: 19.13
    config_b_h03_kv02:
      II_low: 18.77
      II_mid: 3.97
      II_high: 0.52
      D: 18.25
    pre_registered_criterion_passed: true
    gradient_direction: II_low >> II_mid >> II_high (consistent with symmetric baseline)
- id: c1_c2_accuracy_eval
  claim: C1
  description: 'DS dense->s030 acc: 0.52->0.10 (-0.42); QW dense->s030: 0.32->0.14
    (-0.18)'
  registry_id: c2_accuracy_eval
  role: supporting
  priority: medium
  status: DONE
  conclusion: success
  metrics:
    n_problems: 50
    ds_dense_acc: 0.52
    ds_s015_acc: 0.36
    ds_s015_delta: -0.16
    ds_s030_acc: 0.1
    ds_s030_delta: -0.42
    qw_dense_acc: 0.32
    qw_s015_acc: 0.34
    qw_s015_delta: 0.02
    qw_s030_acc: 0.14
    qw_s030_delta: -0.18
    ds_s030_chinese_reasoning_rate: 0.4
    ds_dense_truncation_rate: 0.56
    note: v2 rescored with fixed radical+degree matcher. DS s015 34→36, QW s015 32→34
- id: c2_bf16_importance_s030
  claim: C2
  description: 'Phase gradient: II low=14.64 >> mid=2.28 >> high=0.053 (median); low/high
    ratio ~276x'
  registry_id: bf16_importance_s030
  role: primary
  priority: high
  status: DONE
  conclusion: success
  metrics: &id001
    interaction_index:
      high:
        mean: 0.5547
        median: 0.0534
        ci:
        - 0.2773
        - 0.9198
        winsorized_mean: 0.3367
        skewness: 10.62
      mid:
        mean: 11.3
        median: 2.2833
        ci:
        - 6.865
        - 17.2633
        winsorized_mean: 8.1752
        skewness: 9.19
      low:
        mean: 57.7946
        median: 14.6395
        ci:
        - 41.4416
        - 77.0467
        winsorized_mean: 39.3143
        skewness: 8.31
    per_problem_ii_stats:
      high:
        n: 49
        min: -0.5095
        max: 4.4457
        mean: 0.1976
        median: 0.0343
        std: 0.6793
      mid:
        n: 40
        min: -0.1989
        max: 34.0258
        mean: 5.2585
        median: 1.5173
        std: 7.9382
      low:
        n: 50
        min: -7.3027
        max: 126.7985
        mean: 22.6601
        median: 9.9731
        std: 28.4096
    gradient_paired_aggregate_legacy: 57.24
    median_difference: 14.5861
    n_problems: 50
    pass_fail:
      ci_overlap: true
      sign_reversal: false
      overall: PASS
    phase_stats:
      high:
        n_tokens: 21086
        n_segments: 387
      mid:
        n_tokens: 13306
        n_segments: 191
      low:
        n_tokens: 27748
        n_segments: 397
    perplexity:
      high:
        dense: 1.1689
        attn: 1.7123
        kv: 2.0544
        both: 3.2372
      mid:
        dense: 1.2269
        attn: 1.7894
        kv: 9.4821
        both: 24.2847
      low:
        dense: 1.2286
        attn: 1.9347
        kv: 51.6485
        both: 122.61
- id: c2_v6_importance_s030
  claim: C2
  description: II low_median=34.69, mid_median=7.27, high_median=0.88; bootstrap_gradient=41.92,
    CI=[19.14,299.76]
  registry_id: v6_importance_s030
  role: primary
  priority: high
  status: DONE
  conclusion: success
  metrics:
    ii_high_median: 0.8833
    ii_mid_median: 7.2706
    ii_low_median: 34.6937
    ii_high_mean: 1.5151
    ii_mid_mean: 78.8215
    ii_low_mean: 1163.9677
    per_problem_ii_count: 50
    n_high: 40
    n_mid: 22
    n_low: 20
    problems: 50
    bootstrap_gradient_paired: 41.92
    bootstrap_ci_paired:
    - 19.14
    - 299.76
    bootstrap_gradient_unpaired: 39.28
    bootstrap_ci_unpaired:
    - 21.87
    - 129.59
    bootstrap_p: 0
- id: c2_think_phase_validation
  claim: C2
  description: Phase segmentation kappa=0.887; thinking=57.8% low-sparsity, answer=62.7%
    high-sparsity
  registry_id: think_phase_validation
  role: supporting
  priority: medium
  status: DONE
  conclusion: success
  metrics:
    effective_n: 48
    skipped_problems: 2
    median_kappa: 0.887
    thinking_in_low_sparsity_phase: 0.578
    answer_in_high_sparsity_phase: 0.627
    note: Phase segmentation based on dense model — 4 sparsity conditions share identical
      phase boundaries, effective sample n=48 not n=192
- id: c2_acc_qw_s030_n100
  claim: C2
  description: QW importance s030 accuracy=0.19 (n=100); dose-response monotonic decline
    from dense=0.40
  registry_id: acc_qw_s030_n100
  role: supporting
  priority: medium
  status: DONE
  conclusion: success
  metrics:
    batch1_correct: 7
    batch1_total: 50
    batch1_acc: 0.14
    batch1_source: acc_qw_s030_b1_8k (v2, 8k tokens)
    batch2_correct: 12
    batch2_total: 50
    batch2_acc: 0.24
    combined_correct: 19
    combined_total: 100
    combined_acc: 0.19
- id: c2_acc_ds_s015_8k_v2
  claim: C2
  description: DS s015 accuracy=0.48 vs dense=0.74; early onset of compound degradation
  registry_id: acc_ds_s015_8k_v2
  role: supporting
  priority: medium
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.48
    correct: 24
    total: 50
    truncation_rate: 0.32
    truncated_count: 16
    non_truncated_accuracy: 0.706
    non_truncated_correct: 24
    non_truncated_total: 34
    wall_time_s: 3967
    max_new_tokens: 8192
- id: c3_v6_importance_s025
  claim: C3
  description: 'Importance: II low_median=24.16 >> high_median=0.66; strong phase
    gradient (36x ratio)'
  registry_id: v6_importance_s025
  role: primary
  priority: high
  status: DONE
  conclusion: success
  metrics:
    ii_high_median: 0.6641
    ii_mid_median: 5.3067
    ii_low_median: 24.1619
    ii_high_mean: 0.8842
    ii_mid_mean: 10.057
    ii_low_mean: 71.8854
    per_problem_ii_count: 50
    n_high: 42
    n_mid: 23
    n_low: 21
    problems: 50
    bootstrap_gradient_paired: 35.72
    bootstrap_ci_paired:
    - 9.52
    - 101.54
    bootstrap_gradient_unpaired: 36.38
    bootstrap_ci_unpaired:
    - 13.19
    - 97.61
    bootstrap_p: 0
- id: c3_v6_random_s025
  claim: C3
  description: 'Random: II low_median=2.91 ~ high_median=3.00; flat phase gradient
    (bootstrap_p=0.559)'
  registry_id: v6_random_s025
  role: primary
  priority: high
  status: DONE
  conclusion: success
  metrics:
    ii_high_median: 3.0024
    ii_mid_median: 2.9846
    ii_low_median: 2.9146
    ii_high_mean: 3.9052
    ii_mid_mean: 7.9491
    ii_low_mean: 3.9114
    per_problem_ii_count: 50
    n_high: 36
    n_mid: 25
    n_low: 24
    bootstrap_gradient_paired: -0.1199
    bootstrap_ci_paired:
    - -1.517
    - 1.2461
    bootstrap_p: 0.559
    bootstrap_gradient_unpaired: -0.8616
    bootstrap_ci_unpaired:
    - -3.3911
    - 1.5169
    per_problem_ii_stats:
      high:
        min: -6.1388
        max: 25.2471
        mean: 4.4098
        median: 3.0421
        std: 6.0734
      mid:
        min: 0.158
        max: 108.7242
        mean: 7.5626
        median: 2.1407
        std: 20.926
      low:
        min: -0.1953
        max: 12.8555
        mean: 3.5806
        median: 2.7289
        std: 3.4915
    verdict: FAIL
- id: c3_bf16_importance_s020
  claim: C3
  description: 'Importance: II low=1.50, mid=0.20, high=0.015 (median); clear phase
    separation'
  registry_id: bf16_importance_s020
  role: supporting
  priority: medium
  status: DONE
  conclusion: success
  metrics: &id002
    interaction_index:
      high:
        mean: 0.1289
        median: 0.0145
        ci:
        - -0.1975
        - 0.6647
        winsorized_mean: -0.0297
        skewness: 16.67
      mid:
        mean: 1.2604
        median: 0.2027
        ci:
        - 0.7466
        - 1.8962
        winsorized_mean: 0.766
        skewness: 7.05
      low:
        mean: 6.0288
        median: 1.4963
        ci:
        - 4.4671
        - 7.9237
        winsorized_mean: 4.3426
        skewness: 6.01
    per_problem_ii_stats:
      high:
        n: 49
        min: -0.1884
        max: 0.4196
        mean: 0.0025
        median: 0.0036
        std: 0.0966
      mid:
        n: 40
        min: -0.0519
        max: 8.6969
        mean: 0.6795
        median: 0.1977
        std: 1.4998
      low:
        n: 50
        min: -1.6151
        max: 22.6875
        mean: 2.2301
        median: 1.128
        std: 4.3758
    gradient_paired_aggregate_legacy: 5.9
    median_difference: 1.4818
    n_problems: 50
    pass_fail:
      ci_overlap: true
      sign_reversal: false
      overall: PASS
    phase_stats:
      high:
        n_tokens: 21086
        n_segments: 387
      mid:
        n_tokens: 13306
        n_segments: 191
      low:
        n_tokens: 27748
        n_segments: 397
    perplexity:
      high:
        dense: 1.1689
        attn: 1.5233
        kv: 1.6191
        both: 2.1047
      mid:
        dense: 1.2269
        attn: 1.5375
        kv: 3.5164
        both: 5.4246
      low:
        dense: 1.2286
        attn: 1.6486
        kv: 15.7987
        both: 23.74
- id: c3_bf16_ds_rand_s020
  claim: C3
  description: 'Random: II high=0.292, mid=0.350, low=0.276 (median); no phase separation'
  registry_id: bf16_ds_rand_s020
  role: supporting
  priority: medium
  status: DONE
  conclusion: success
  metrics:
    interaction_index:
      high:
        mean: 1.1216
        median: 0.2918
        ci:
        - 0.0796
        - 2.5834
        median_ci:
        - 0.1598
        - 0.4581
        winsorized_mean: 1.7664
        skewness: 9.59
      mid:
        mean: -1.5827
        median: 0.3504
        ci:
        - -6.0963
        - 1.5735
        median_ci:
        - 0.1993
        - 0.5226
        winsorized_mean: 0.5839
        skewness: -12.31
      low:
        mean: -0.4116
        median: 0.2763
        ci:
        - -2.6034
        - 1.209
        median_ci:
        - 0.2194
        - 0.5487
        winsorized_mean: 0.9942
        skewness: -10.07
    perplexity:
      high:
        dense: 1.1687
        attn: 3.1905
        kv: 3.8002
        both: 8.8129
      mid:
        dense: 1.2269
        attn: 67.8504
        kv: 3.788
        both: 11.4974
      low:
        dense: 1.2284
        attn: 8.592
        kv: 5.0078
        both: 9.2001
    phase_stats:
      high:
        n_tokens: 21086
        n_segments: 387
      mid:
        n_tokens: 13306
        n_segments: 191
      low:
        n_tokens: 27748
        n_segments: 397
    n_problems: 50
    pass_fail:
      ci_overlap: false
      sign_reversal: false
      overall: FAIL
    median_difference: -0.0155
- id: c4_c4_entropy
  claim: C4
  description: 'DS importance entropy_delta: -0.04 to -0.05 (collapse); random: +0.13
    to +0.23 (redistribution). Gini_delta: -0.03 to -0.08'
  registry_id: c4_entropy
  role: primary
  priority: high
  status: DONE
  conclusion: success
  metrics:
    importance_entropy_delta:
      s015: -0.0402
      s020: -0.0472
      s025: -0.0446
      s030: -0.0436
    random_entropy_delta:
      s015: 0.1283
      s020: 0.136
      s025: 0.2171
      s030: 0.2327
    importance_gini_delta:
      s015: -0.0301
      s020: -0.0404
      s025: -0.0647
      s030: -0.0806
    random_gini_delta:
      s015: -0.0309
      s020: -0.0403
      s025: -0.062
      s030: -0.0732
    importance_cv_delta:
      s015: -0.564
      s020: -0.774
      s025: -1.287
      s030: -1.665
    random_cv_delta:
      s015: -1.021
      s020: -1.203
      s025: -1.923
      s030: -2.137
    problems_completed: 30
    runtime_minutes: 69.1
- id: c4_qwen_c4_entropy
  claim: C4
  description: 'QW importance entropy_delta mixed: s015=-0.073, s025=+0.045; Gini
    weaker (-0.01 to -0.02). Model-dependent pattern'
  registry_id: qwen_c4_entropy
  role: primary
  priority: high
  status: DONE
  conclusion: negative
  metrics:
    problems_completed: 30
    qwen_importance_entropy_delta:
      s015: -0.0733
      s020: -0.0759
      s025: 0.0451
      s030: -0.0072
    qwen_random_entropy_delta:
      s015: 0.0838
      s020: 0.0901
      s025: 0.2168
      s030: 0.1968
    qwen_importance_gini_delta:
      s015: -0.0103
      s020: -0.0121
      s025: -0.01
      s030: -0.0202
    qwen_random_gini_delta:
      s015: -0.0186
      s020: -0.0229
      s025: -0.0337
      s030: -0.0448
    qwen_importance_cv_delta:
      s015: -0.045
      s020: -0.208
      s025: -1.491
      s030: -1.142
    qwen_random_cv_delta:
      s015: -0.778
      s020: -0.889
      s025: -1.5
      s030: -1.677
    cross_model_notes: random entropy increase consistent; importance entropy collapse
      inconsistent at s025 (reversed to +0.045) and near-zero at s030; gini/cv directions
      consistent but Qwen magnitudes smaller
- id: c5_bf16_qw_imp_s030
  claim: C5
  description: 'Qwen: median_diff=2.619, Cohen''s d=1.439, p<1e-5; replicates DeepSeek
    pattern'
  registry_id: bf16_qw_imp_s030
  role: primary
  priority: high
  status: DONE
  conclusion: success
  metrics:
    median_difference: 2.619385
    permutation_p: 0
    cohens_d: 1.4394
    bootstrap_ci_95:
    - 1.722281
    - 3.651063
    wilcoxon_p: 0
    n_bootstrap: 10000
    n_paired: 46
- id: c5_bf16_importance_s030
  claim: C5
  description: 'DeepSeek: II low_median=14.64, high_median=0.053; strong phase gradient'
  registry_id: bf16_importance_s030
  role: primary
  priority: high
  status: DONE
  conclusion: success
  metrics: *id001
- id: c5_c2_n500_deepseek
  claim: C5
  description: 'DS n=500: imp_s030 median_II=8.48, CI=[7.46,9.56], p=1.3e-78; robust
    at scale'
  registry_id: c2_n500_deepseek
  role: supporting
  priority: medium
  status: DONE
  conclusion: success
  metrics: &id004
    n_problems: 500
    effective_n: 496
    mid_null_rate: 0.102
    imp_s015_median_ii: 0.3907
    imp_s015_ci:
    - 0.3496
    - 0.4431
    imp_s015_wilcoxon_p: 1.27e-70
    imp_s020_median_ii: 1.2149
    imp_s020_ci:
    - 1.1072
    - 1.3365
    imp_s020_wilcoxon_p: 3.98e-75
    imp_s025_median_ii: 3.9857
    imp_s025_ci:
    - 3.5272
    - 4.3588
    imp_s025_wilcoxon_p: 1.99e-78
    imp_s030_median_ii: 8.4813
    imp_s030_ci:
    - 7.7543
    - 9.6919
    imp_s030_wilcoxon_p: 1.09e-79
    rand_s015_median_ii: 0.0139
    rand_s015_wilcoxon_p: 0.863
    rand_s020_median_ii: 0.0315
    rand_s020_wilcoxon_p: 0.28
    rand_s025_median_ii: 0.2574
    rand_s025_bonf_p: 0.005839
    rand_s025_fdr_p: 0.001914
    rand_s030_median_ii: 0.5096
    rand_s030_bonf_p: 0.005903
    rand_s030_fdr_p: 0.001914
    dz_s015_s020: -0.925
    dz_s020_s025: -0.824
    dz_s025_s030: -0.773
    dz_s015_s030: -0.944
    all_dz_reliable: true
    dose_response_monotonic: true
    dose_response_spearman_rho: 1
    dose_response_perm_p: 0.0417
    imp_rand_ratio_range: 15.5-38.6x
    bonferroni_k: 4
    bonferroni_note: Bonferroni k=4 family-wise (D066 revision)
- id: c5_c2_qw_n500_r3
  claim: C5
  description: 'QW n=500: imp_s030 median_II=4.33, p<1e-40; cross-model replication
    at high power'
  registry_id: c2_qw_n500_r3
  role: supporting
  priority: medium
  status: DONE
  conclusion: success
  metrics: &id005
    n_problems: 500
    effective_n: 475
    filter: low+high valid only (mid-null allowed)
    mid_null_rate: 0.452
    imp_s015_median_ii: 0.0659
    imp_s015_ci:
    - 0.0492
    - 0.0925
    imp_s015_wilcoxon_p: 8.66e-15
    imp_s015_bonf_p: 3.46e-14
    imp_s020_median_ii: 0.3073
    imp_s020_ci:
    - 0.2612
    - 0.3564
    imp_s020_wilcoxon_p: 6.84e-42
    imp_s020_bonf_p: 2.74e-41
    imp_s025_median_ii: 1.0745
    imp_s025_ci:
    - 0.9766
    - 1.1787
    imp_s025_wilcoxon_p: 1.06e-68
    imp_s025_bonf_p: 4.25e-68
    imp_s030_median_ii: 3.155
    imp_s030_ci:
    - 2.7834
    - 3.5582
    imp_s030_wilcoxon_p: 9.21e-74
    imp_s030_bonf_p: 3.69e-73
    rand_s015_median_ii: -0.0111
    rand_s015_wilcoxon_p: 0.172
    rand_s015_bonf_p: 0.687
    rand_s020_median_ii: 0.0153
    rand_s020_wilcoxon_p: 0.2
    rand_s020_bonf_p: 0.8
    rand_s025_median_ii: 0.3931
    rand_s025_wilcoxon_p: 1.59e-11
    rand_s025_bonf_p: 6.37e-11
    rand_s025_fdr_p: 2.63e-11
    rand_s030_median_ii: 0.9127
    rand_s030_wilcoxon_p: 2.92e-15
    rand_s030_bonf_p: 1.17e-14
    rand_s030_fdr_p: 5.61e-15
    dz_s015_s020: -0.629
    dz_s020_s025: -0.865
    dz_s025_s030: -0.767
    dz_s015_s030: -0.923
    all_dz_reliable: true
    dose_response_monotonic: true
    dose_response_spearman_rho: 1
    dose_response_perm_p: 0.0417
    imp_rand_ratio_range: 2.7-20.1x
    bonferroni_k: 4
    bonferroni_note: Bonferroni k=4 family-wise (D066 revision)
- id: c5b_c5b_pilot
  claim: C5b
  description: 'Oracle recovery=18% (gate: >30% FAIL); heuristic recovery=31.7% but
    CI crosses zero. s030 incomplete'
  registry_id: c5b_pilot
  role: primary
  priority: high
  status: DONE
  conclusion: negative
  metrics:
    s025_uniform_median_ii: 1.0435
    s025_oracle_median_ii: 0.856
    s025_oracle_recovery_pct: 18
    s025_oracle_recovery_ci:
    - -39
    - 45.8
    s025_oracle_wilcoxon_p: 0.0021
    s025_heuristic_median_ii: 0.7127
    s025_heuristic_recovery_pct: 31.7
    s025_heuristic_recovery_ci:
    - -22.8
    - 66
    s025_heuristic_wilcoxon_p: 0.0236
    gate_criterion: oracle_recovery > 30%
    gate_result: FAIL
    s030_status: not_completed
    n_problems: 30
- id: c6_bf16_importance_s015
  claim: C6
  description: II low_median=0.398 at s=0.15
  registry_id: bf16_importance_s015
  role: primary
  priority: high
  status: DONE
  conclusion: success
  metrics:
    interaction_index:
      high:
        mean: -0.150213
        median: 0.005752
        ci:
        - -0.294614
        - -0.055385
        winsorized_mean: -0.062378
        skewness: -14.9912
      mid:
        mean: 0.447301
        median: 0.080738
        ci:
        - 0.267993
        - 0.668749
        winsorized_mean: 0.324751
        skewness: 4.7221
      low:
        mean: 2.405837
        median: 0.398291
        ci:
        - 1.478784
        - 3.667675
        winsorized_mean: 1.278857
        skewness: 9.5402
    per_problem_ii_stats:
      high:
        n: 49
        min: -0.188061
        max: 0.335853
        mean: -0.013405
        median: 0.00012
        std: 0.078483
      mid:
        n: 40
        min: -0.169092
        max: 3.88198
        mean: 0.308621
        median: 0.107114
        std: 0.690186
      low:
        n: 50
        min: -0.872983
        max: 9.10289
        mean: 0.725504
        median: 0.315517
        std: 1.731056
    gradient_paired_aggregate_legacy: 69.24
    median_difference: 0.3925
    n_problems: 50
    pass_fail:
      ci_overlap: true
      sign_reversal: true
      overall: PASS
    phase_stats:
      high:
        n_tokens: 21086
        n_segments: 387
      mid:
        n_tokens: 13306
        n_segments: 191
      low:
        n_tokens: 27748
        n_segments: 397
    perplexity:
      high:
        dense: 1.1689
        attn: 1.4861
        kv: 1.4481
        both: 1.5911
      mid:
        dense: 1.2269
        attn: 1.5137
        kv: 2.5971
        both: 3.4541
      low:
        dense: 1.2286
        attn: 1.6147
        kv: 8.9201
        both: 12.5084
- id: c6_bf16_importance_s020
  claim: C6
  description: II low_median=1.496 at s=0.20
  registry_id: bf16_importance_s020
  role: supporting
  priority: medium
  status: DONE
  conclusion: success
  metrics: *id002
- id: c6_bf16_importance_s025
  claim: C6
  description: II low_median=7.196 at s=0.25
  registry_id: bf16_importance_s025
  role: supporting
  priority: medium
  status: DONE
  conclusion: success
  metrics: *id003
- id: c6_bf16_importance_s030
  claim: C6
  description: II low_median=14.64 at s=0.30; growth 0.40->1.50->7.20->14.64 is sub-exponential
  registry_id: bf16_importance_s030
  role: supporting
  priority: medium
  status: DONE
  conclusion: success
  metrics: *id001
- id: c7_c2_n500_deepseek
  claim: C7
  description: 'DS n=500: all 4 sparsities significant (p<1e-70); CIs non-overlapping
    across dose levels'
  registry_id: c2_n500_deepseek
  role: primary
  priority: high
  status: DONE
  conclusion: success
  metrics: *id004
- id: c7_c2_qw_n500_r3
  claim: C7
  description: 'QW n=500: all 4 sparsities significant (p<1e-14 Bonferroni-corrected);
    mid_null_rate=45.2%'
  registry_id: c2_qw_n500_r3
  role: primary
  priority: high
  status: DONE
  conclusion: success
  metrics: *id005
- id: c8_c3_llama
  claim: C8
  description: LLaMA-8B (LlamaForCausalLM) replicates phase-modulated compound severity
    from Qwen2ForCausalLM
  registry_id: c3_llama
  role: primary
  priority: high
  status: DONE
  conclusion: success
  metrics:
    model: DeepSeek-R1-Distill-Llama-8B
    n_problems: 50
    n_valid: 49
    n_skipped: 1
    conditions_completed: 8/8
    n_bootstrap: 10000
    bonferroni_k: 4
    imp_vs_rand_dz:
      s015: 0.1923
      s020: 0.255
      s025: 0.2902
      s030: 0.3352
    imp_vs_rand_dz_ci:
      s015:
      - -0.0862
      - 0.496
      s020:
      - -0.0248
      - 0.5381
      s025:
      - 0.0081
      - 0.6121
      s030:
      - 0.0606
      - 0.6629
    imp_vs_rand_dz_interpretation:
      s015: negligible
      s020: small
      s025: small
      s030: small
    imp_vs_rand_dz_monotonic: true
    phase_gradient_importance_dz:
      s015: 1.0079
      s020: 1.108
      s025: 1.1227
      s030: 1.0038
    phase_gradient_importance_dz_ci:
      s015:
      - 0.593
      - 1.7025
      s020:
      - 0.8144
      - 1.5698
      s025:
      - 0.8735
      - 1.5768
      s030:
      - 0.8099
      - 1.3519
    phase_gradient_importance_interpretation: all_large
    phase_gradient_random_dz:
      s015: 0.3497
      s020: 0.373
      s025: 0.4476
      s030: 0.4385
    phase_gradient_random_dz_ci:
      s015:
      - 0.0665
      - 0.6916
      s020:
      - 0.0868
      - 0.7335
      s025:
      - 0.1669
      - 0.7698
      s030:
      - 0.1966
      - 0.707
    phase_gradient_random_interpretation: all_small
    median_diff:
      s015: 0.0203
      s020: 0.0221
      s025: 0.0947
      s030: 0.3562
    median_diff_ci:
      s015:
      - 0.0016
      - 0.0435
      s020:
      - -0.0905
      - 0.187
      s025:
      - -0.0037
      - 0.3029
      s030:
      - -0.0691
      - 0.5442
    wilcoxon_p:
      s015: 0.0549
      s020: 0.0632
      s025: 0.0209
      s030: 0.0074
    wilcoxon_p_bonferroni:
      s015: 0.2195
      s020: 0.2527
      s025: 0.0834
      s030: 0.0294
    significant_bonferroni:
      s015: false
      s020: false
      s025: false
      s030: true
    cross_arch_comparison:
      deepseek_importance_dz:
        s015: 0.4416
        s020: 0.5195
        s025: 0.6831
        s030: 0.8031
      llama_importance_dz:
        s015: 1.0079
        s020: 1.108
        s025: 1.1227
        s030: 1.0038
      delta:
        s015: 0.5663
        s020: 0.5885
        s025: 0.4396
        s030: 0.2007
      note: LLaMA shows uniformly large d_z (all >1.0) vs DeepSeek medium-to-large
- id: c10_gsm8k_profiling_ds
  claim: C10
  description: 'DS GSM8K importance gradient: s015=0.241, s020=0.740, s025=1.992,
    s030=4.636 (monotonic)'
  registry_id: gsm8k_profiling_ds
  role: primary
  priority: high
  status: DONE
  conclusion: success
  metrics:
    version: v3_median
    n_problems: 50
    method: median + Wilcoxon + bootstrap_median(B=10000)
    importance:
      s015:
        median_gradient: 0.241
        ci_low: 0.077
        ci_high: 0.478
        wilcoxon_p: 0.0003
      s020:
        median_gradient: 0.74
        ci_low: 0.314
        ci_high: 1.119
        wilcoxon_p: 0.0001
      s025:
        median_gradient: 1.992
        ci_low: 0.933
        ci_high: 2.82
        wilcoxon_p: 0.0001
      s030:
        median_gradient: 4.682
        ci_low: 2.121
        ci_high: 10.557
        wilcoxon_p: 0.0001
    imp_rand_ratio:
      s015: 2.3
      s020: 2.5
      s025: 3.8
      s030: 2.8
    dose_response_monotonic: true
- id: c10_gsm8k_profiling_qw
  claim: C10
  description: 'QW GSM8K importance gradient: s015=0.039, s020=0.158, s025=1.100,
    s030=2.092 (monotonic)'
  registry_id: gsm8k_profiling_qw
  role: primary
  priority: high
  status: DONE
  conclusion: success
  metrics:
    version: v3_median
    n_problems: 50
    method: median + Wilcoxon + bootstrap_median(B=10000)
    importance:
      s015:
        median_gradient: 0.039
      s020:
        median_gradient: 0.158
      s025:
        median_gradient: 1.1
      s030:
        median_gradient: 2.092
    qw_rand_s030: INVALID
- id: c10_gsm8k_qw_rand_s025_v2
  claim: C10
  description: 'QW random s025 GSM8K: II median_high=0.72, low=1.48; phase gradient
    weaker than importance'
  registry_id: gsm8k_qw_rand_s025_v2
  role: supporting
  priority: medium
  status: DONE
  conclusion: success
  metrics:
    verdict: PASS
    n_problems: 50
    n_bootstrap: 1000
    seed: 42
    high_sparsity:
      n_segments: 216
      n_tokens: 9326
      ppl_dense: 1.0695
      ppl_attn: 5.9362
      ppl_kv: 3.4316
      ppl_both: 15.7484
      ii_mean: 6.5954
      ii_ci:
      - 1.1114
      - 11.3791
      ii_median: 0.7176
      ii_median_ci:
      - 0.5959
      - 0.9347
      winsorized_mean: 6.5046
      skewness: -4.6807
      outlier_count: 3
    low_sparsity:
      n_segments: 252
      n_tokens: 29224
      ppl_dense: 1.1972
      ppl_attn: 11.5347
      ppl_kv: 5.6038
      ppl_both: 21.6874
      ii_mean: 2.3883
      ii_ci:
      - -8.4602
      - 11.029
      ii_median: 1.4587
      ii_median_ci:
      - 1.1121
      - 2.0451
      winsorized_mean: 5.8911
      skewness: -7.6074
      outlier_count: 4
    mid_sparsity:
      n_segments: 51
      n_tokens: 5954
      ppl_dense: 1.2601
      ppl_attn: 13.4132
      ppl_kv: 6.4841
      ppl_both: 20.8714
      ii_mean: 4.5407
      ii_ci:
      - -4.8854
      - 12.4605
      ii_median: 1.1272
      ii_median_ci:
      - 0.637
      - 3.3729
      winsorized_mean: 6.3284
      skewness: -3.4048
      outlier_count: 1
- id: c10_gsm8k_qw_rand_s030_v2
  claim: C10
  description: 'QW random s030 GSM8K: II median_high=2.31, low=5.87; compound effect
    on GSM8K confirmed'
  registry_id: gsm8k_qw_rand_s030_v2
  role: supporting
  priority: medium
  status: DONE
  conclusion: success
  metrics:
    verdict: PASS
    n_problems: 50
    n_bootstrap: 1000
    seed: 42
    high_sparsity:
      n_segments: 216
      n_tokens: 9326
      null_ratio: 2/50
      ppl_dense: 1.0695
      ppl_attn: 6.5613
      ppl_kv: 4.481
      ppl_both: 23.7486
      ii_mean: 11.83
      ii_median: 2.31
      ii_ci:
      - 6.17
      - 17.04
      ii_median_ci:
      - 1.64
      - 2.81
      winsorized_mean: 10.55
      skewness: -2.29
      outlier_count: 7
    low_sparsity:
      n_segments: 252
      n_tokens: 29224
      null_ratio: 5/50
      ppl_dense: 1.1972
      ppl_attn: 6.3283
      ppl_kv: 8.5374
      ppl_both: 56.2304
      ii_mean: 31.26
      ii_median: 5.2
      ii_ci:
      - 17.84
      - 47.86
      ii_median_ci:
      - 3.95
      - 7.24
      winsorized_mean: 16.35
      skewness: 7.57
      outlier_count: 4
    mid_sparsity:
      n_segments: 51
      n_tokens: 5954
      null_ratio: 17/50
      ppl_dense: 1.2601
      ppl_attn: 18.6162
      ppl_kv: 11.6625
      ppl_both: 47.9019
      ii_mean: 18.02
      ii_median: 2.7
      ii_ci:
      - 0.09
      - 36.69
      ii_median_ci:
      - 1.46
      - 8.77
      winsorized_mean: 18.22
      skewness: 0.43
      outlier_count: 2
- id: s3_c_bf16_ds_imp_s010
  claim: S3->C
  description: 'DS s=0.10: II_high_median=0.003, verdict=FAIL; below onset threshold
    for DeepSeek'
  registry_id: bf16_ds_imp_s010
  role: primary
  priority: high
  status: DONE
  conclusion: negative
  metrics:
    verdict: FAIL
    problems: 50
    II_high_sparsity_median: 0.0027
    II_high_sparsity_mean: -0.1998
    II_low_sparsity_median: 0.0151
    II_low_sparsity_mean: -0.1066
    II_mid_sparsity_median: 0.0061
    II_mid_sparsity_mean: -0.0131
    high_sparsity_tokens: 21086
    low_sparsity_tokens: 27748
    mid_sparsity_tokens: 13306
- id: s3_c_bf16_qw_imp_s010
  claim: S3->C
  description: 'QW s=0.10: overall_verdict=PASS, CI_overlap_test=PASS; Qwen onset
    earlier than DeepSeek'
  registry_id: bf16_qw_imp_s010
  role: primary
  priority: high
  status: DONE
  conclusion: success
  metrics:
    n_problems: 50
    overall_verdict: PASS
    ci_overlap_test: PASS
    sign_reversal_test: FAIL
    high_sparsity_II_median: 0.0001
    high_sparsity_II_median_CI:
    - -0.0028
    - 0.0005
    high_sparsity_II_mean: -0.0887
    high_sparsity_II_mean_CI:
    - -0.1235
    - -0.0591
    low_sparsity_II_median: -0.0444
    low_sparsity_II_median_CI:
    - -0.0967
    - -0.0152
    low_sparsity_II_mean: -0.2431
    low_sparsity_II_mean_CI:
    - -0.3817
    - -0.1202
    mid_sparsity_II_median: -0.0359
    mid_sparsity_II_median_CI:
    - -0.0963
    - -0.015
    mid_sparsity_II_mean: -0.084
    mid_sparsity_II_mean_CI:
    - -0.1366
    - -0.035
    ppl_high_dense: 1.074
    ppl_high_both: 1.228
    ppl_low_dense: 1.152
    ppl_low_both: 3.204
    ppl_mid_dense: 1.133
    ppl_mid_both: 1.741
- id: s3_c_bf16_qw_imp_s015
  claim: S3->C
  description: 'QW s=0.15: median_diff=0.048, permutation_p=0.0001; confirmed above
    threshold'
  registry_id: bf16_qw_imp_s015
  role: supporting
  priority: medium
  status: DONE
  conclusion: success
  metrics:
    median_difference: 0.047619
    permutation_p: 0.0001
    cohens_d: 0.3705
    bootstrap_ci_95:
    - -0.005077
    - 0.109517
    wilcoxon_p: 0.02958
    n_bootstrap: 10000
    n_paired: 46
- id: s7_c_c2_n500_deepseek
  claim: S7->C
  description: 'DS n=500 monotonic: imp median II 0.39->1.21->3.99->8.48 across s015-s030
    (Spearman rho=1.0)'
  registry_id: c2_n500_deepseek
  role: primary
  priority: high
  status: DONE
  conclusion: success
  metrics: *id004
- id: s7_c_c2_qw_n500_r3
  claim: S7->C
  description: 'QW n=500 monotonic: imp median II 0.066->0.307->1.075->4.33 across
    s015-s030 (Spearman rho=1.0)'
  registry_id: c2_qw_n500_r3
  role: primary
  priority: high
  status: DONE
  conclusion: success
  metrics: *id005
- id: s7_c_bf16_qw_imp_s035
  claim: S7->C
  description: 'QW s=0.35: low_II_median=8.24; extends dose-response beyond s030'
  registry_id: bf16_qw_imp_s035
  role: supporting
  priority: medium
  status: DONE
  conclusion: success
  metrics:
    n_problems: 50
    overall_verdict: PASS
    ci_overlap_test: PASS
    sign_reversal_test: FAIL
    high_sparsity_II_median: 0.0232
    high_sparsity_II_median_CI:
    - 0.0154
    - 0.0383
    high_sparsity_II_mean: 0.1643
    high_sparsity_II_mean_CI:
    - 0.0844
    - 0.2495
    low_sparsity_II_median: 8.2358
    low_sparsity_II_median_CI:
    - 6.1564
    - 10.9231
    low_sparsity_II_mean: 18.9673
    low_sparsity_II_mean_CI:
    - 14.5015
    - 23.9752
    mid_sparsity_II_median: 0.9577
    mid_sparsity_II_median_CI:
    - 0.171
    - 3.5575
    mid_sparsity_II_mean: 8.0734
    mid_sparsity_II_mean_CI:
    - 2.0224
    - 16.8946
    ppl_high_dense: 1.0738
    ppl_high_both: 2.3435
    ppl_low_dense: 1.1518
    ppl_low_both: 58.0358
    ppl_mid_dense: 1.1327
    ppl_mid_both: 20.9912
    high_sparsity_tokens: 16289
    low_sparsity_tokens: 32227
    mid_sparsity_tokens: 4372


## registry (completed experiments)

- exp_id: mvp_interaction_index_profiling
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: mvp_ii_profiling_v2
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    mvp_verdict: PASS_technical_but_negative_hypothesis
    ci_nonoverlap: true
    sign_reversal: false
    ii_reasoning_0.3: 17.79
    ii_reasoning_0.3_ci:
    - 4.09
    - 38.76
    ii_transition_0.3: 3.06
    ii_transition_0.3_ci:
    - 0.01
    - 5.6
    ii_reasoning_0.5: 468.9
    ii_transition_0.5: 850.07
    ii_execution_0.3: Inf
    phase_distribution:
      execution: 1.2%_25seg
      reasoning: 8.1%_96seg
      transition: 90.7%_192seg
    total_tokens: 86207
    all_ii_superadditive: true
    amplitude_ratio_reas_vs_trans_0.3: 5.81
    gmm_best_k: 5
    gmm_means:
    - 0.438
    - 0.597
    - 0.719
    - 0.816
    - 0.892
    gmm_weights:
    - 0.062
    - 0.14
    - 0.208
    - 0.282
    - 0.309
    sparsity_global:
      mean: 0.7653
      std: 0.1364
      median: 0.8004
    quantile_boundaries:
    - 0.7337
    - 0.8482
- exp_id: mvp_ii_profiling_v3
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    mvp_verdict: FAIL
    ci_nonoverlap: false
    sign_reversal: false
    phase_distribution_balanced: true
    ii_high_0.1:
      mean: 0.2317
      ci:
      - 0.1338
      - 0.3418
    ii_low_0.1:
      mean: 0.1711
      ci:
      - 0.0782
      - 0.2768
    ii_mid_0.1:
      mean: 0.1607
      ci:
      - 0.0886
      - 0.2489
    ii_high_0.2:
      mean: 2.1574
      ci:
      - 1.0605
      - 3.5491
    ii_low_0.2:
      mean: 1.1294
      ci:
      - 0.4368
      - 1.9593
    ii_mid_0.2:
      mean: 0.3049
      ci:
      - -1.0635
      - 1.3044
    total_tokens: 86207
    no_nan_inf: true
    segments:
      high: 511
      low: 454
      mid: 391
- exp_id: mvp_ii_profiling_v4
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: mvp_ii_profiling_v4b
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: mvp_ii_profiling_v4c
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: mvp_ii_profiling_v4d
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: mvp_ii_profiling_v4-random
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: mvp_v4a_r2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: mvp_v4b_r2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: mvp_v4c_r2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: mvp_v4_random_r2
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: mvp_v4_legacy_s01
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    II_high_0.1:
      mean: -0.1097
      ci_low: -0.8066
      ci_high: 0.41
    II_mid_0.1:
      mean: -15.966
      ci_low: -47.991
      ci_high: 1.288
    II_low_0.1:
      mean: 0
      ci_low: 0
      ci_high: 0
    ppl_high_dense: 1.1462
    ppl_high_both: 22.1302
    ppl_mid_dense: 1.1226
    ppl_mid_both: 47.5856
    verdict: FAIL
- exp_id: mvp_v4_legacy_s02
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ii_high_0.2:
      mean: 21.2856
      ci:
      - 0.0292
      - 63.163
    ii_mid_0.2:
      mean: 21.8743
      ci:
      - 4.9863
      - 41.785
    ii_low_0.2:
      mean: 0
      ci:
      - 0
      - 0
    ppl_high:
      dense: 1.15
      attn: 1.32
      kv: 104.42
      both: 63.41
    ppl_mid:
      dense: 1.12
      attn: 1.29
      kv: 324.16
      both: 170.47
    ppl_low:
      dense: 1.11
      attn: 1.3
      kv: 1.11
      both: 1.3
    problems_completed: 50
    phase_tokens:
      high: 25862
      mid: 27996
      low: 32349
    mvp_verdict: PASS
- exp_id: mvp_v4_legacy_s03
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ii_high_0.3:
      mean: -224.5
      ci_crosses_zero: true
    verdict: FAIL_ci_crosses_zero
- exp_id: mvp_v4_legacy_s025
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: mvp_v4_legacy_s035
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: mvp_v4_float32_s030
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: mvp_v5_fixed_s020
  name: ''
  status: DONE
  conclusion: killed
  metrics:
    ii_high: 0.5
    ii_mid: 3.52
    ii_low: 31.89
    ii_high_ci:
    - 0.41
    - 0.62
    ii_mid_ci:
    - 2.29
    - 5.35
    ii_low_ci:
    - 18.74
    - 47.22
    ii_high_median: 0.33
    ii_mid_median: 1.55
    ii_low_median: 9.56
    kv_ppl_high: 1.24
    kv_ppl_mid: 3.65
    kv_ppl_low: 14.11
    both_ppl_high: 2.7
    both_ppl_mid: 8.13
    both_ppl_low: 42.64
    problems: 50
    ⚠️_WARNING: pre-fix code, INVALIDATED. Results found on disk after kill but code
      lacked conda activation fix. Do NOT cite these numbers.
- exp_id: mvp_v5_fixed_s030
  name: ''
  status: DONE
  conclusion: killed
  metrics:
    ii_high: 1.18
    ii_mid: 168.53
    ii_low: 1926.23
    ii_high_ci:
    - 0.86
    - 1.6
    ii_mid_ci:
    - 36.91
    - 348.21
    ii_low_ci:
    - 179.17
    - 4062.57
    ii_high_median: 0.6
    ii_mid_median: 7.47
    ii_low_median: 44.63
    kv_ppl_high: 1.4
    kv_ppl_mid: 15.11
    kv_ppl_low: 40.79
    both_ppl_high: 5.71
    both_ppl_mid: 137.61
    both_ppl_low: 963.2
    problems: 50
    ⚠️_WARNING: pre-fix code, INVALIDATED. Results found on disk after kill but code
      lacked conda activation fix. Do NOT cite these numbers.
- exp_id: mvp_v5_fixed_s015
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    ii_high: 0.306
    ii_mid: 1.274
    ii_low: 8.786
    ii_high_ci:
    - 0.256
    - 0.359
    ii_mid_ci:
    - 0.895
    - 1.749
    ii_low_ci:
    - 5.294
    - 12.684
    ii_high_median: 0.205
    ii_mid_median: 0.696
    ii_low_median: 2.627
    ii_high_winsorized: 0.289
    ii_mid_winsorized: 1.139
    ii_low_winsorized: 8.408
    kv_ppl_high: 1.2147
    kv_ppl_mid: 2.1276
    kv_ppl_low: 6.7451
    both_ppl_high: 2.2835
    both_ppl_mid: 3.9408
    both_ppl_low: 16.9987
    problems: 50
    segments: 1356
- exp_id: mvp_v5_fixed_s025
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    ii_high: 0.851
    ii_mid: 9.306
    ii_low: 96.715
    ii_high_ci:
    - 0.703
    - 0.999
    ii_mid_ci:
    - 6.092
    - 13.303
    ii_low_ci:
    - 59.642
    - 143.188
    ii_high_median: 0.584
    ii_mid_median: 4.522
    ii_low_median: 30.903
    ii_high_winsorized: 0.802
    ii_mid_winsorized: 8.156
    ii_low_winsorized: 94.931
    kv_ppl_high: 1.3108
    kv_ppl_mid: 6.1778
    kv_ppl_low: 23.8919
    both_ppl_high: 3.4623
    both_ppl_mid: 16.4148
    both_ppl_low: 104.1749
    problems: 50
    segments: 1356
- exp_id: mvp_v5_fixed_s020_r2
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    ii_high_median: 0.3333
    ii_mid_median: 1.5479
    ii_low_median: 9.5627
    ii_high_mean: 0.5044
    ii_mid_mean: 3.5155
    ii_low_mean: 31.8937
    ii_high_ci:
    - 0.41
    - 0.62
    ii_mid_ci:
    - 2.29
    - 5.35
    ii_low_ci:
    - 18.74
    - 47.22
    kv_ppl_high: 1.24
    kv_ppl_mid: 3.65
    kv_ppl_low: 14.11
    both_ppl_high: 2.7
    both_ppl_mid: 8.13
    both_ppl_low: 42.64
    problems: 50
- exp_id: mvp_v5_fixed_s030_r2
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    ii_high_median: 0.5964
    ii_mid_median: 7.4671
    ii_low_median: 44.6324
    ii_high_mean: 1.1832
    ii_mid_mean: 168.53
    ii_low_mean: 1926.23
    ii_high_ci:
    - 0.86
    - 1.6
    ii_mid_ci:
    - 36.91
    - 348.21
    ii_low_ci:
    - 179.17
    - 4062.57
    kv_ppl_high: 1.4
    kv_ppl_mid: 15.11
    kv_ppl_low: 40.79
    both_ppl_high: 5.71
    both_ppl_mid: 137.61
    both_ppl_low: 963.2
    problems: 50
- exp_id: mvp_v5_random_s015
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ii_high_median: 0.1606
    ii_mid_median: 0.252
    ii_low_median: 0.1831
    ii_high_mean: 0.4563
    ii_mid_mean: 0.5134
    ii_low_mean: 0.4775
    ii_high_ci:
    - 0.12
    - 0.77
    ii_mid_ci:
    - 0.34
    - 0.74
    ii_low_ci:
    - 0.28
    - 0.7
    kv_ppl_high: 3.14
    kv_ppl_mid: 2.91
    kv_ppl_low: 3.61
    both_ppl_high: 3.92
    both_ppl_mid: 4.14
    both_ppl_low: 4.71
    problems: 50
- exp_id: mvp_v5_random_s025
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ii_high_median: 3.0024
    ii_mid_median: 2.9846
    ii_low_median: 2.9146
    ii_high_mean: 3.9052
    ii_mid_mean: 7.9491
    ii_low_mean: 3.9114
    ii_high_ci:
    - 0.98
    - 6.34
    ii_mid_ci:
    - 4.67
    - 11.87
    ii_low_ci:
    - 2.71
    - 5.24
    kv_ppl_high: 6.39
    kv_ppl_mid: 6.11
    kv_ppl_low: 9.07
    both_ppl_high: 17.06
    both_ppl_mid: 15.38
    both_ppl_low: 29.32
    problems: 50
- exp_id: mvp_v5_random_s020
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ii_high_median: 0.321331
    ii_mid_median: 0.455663
    ii_low_median: 0.591916
    ii_high_mean: 0.855584
    ii_mid_mean: 1.258123
    ii_low_mean: 0.956933
    ii_high_ci:
    - -0.124133
    - 1.616883
    ii_mid_ci:
    - 0.674852
    - 2.075565
    ii_low_ci:
    - 0.583856
    - 1.413355
    kv_ppl_high: 4.2537
    kv_ppl_mid: 4.3064
    kv_ppl_low: 5.4048
    both_ppl_high: 7.9749
    both_ppl_mid: 6.8553
    both_ppl_low: 22.5868
    problems: 50
- exp_id: mvp_v5_random_s030
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ii_high_median: 5.377512
    ii_mid_median: 5.886454
    ii_low_median: 3.776818
    ii_high_mean: 22.734534
    ii_mid_mean: 10.943319
    ii_low_mean: 11.840449
    ii_high_ci:
    - 10.352118
    - 42.551951
    ii_mid_ci:
    - 7.398611
    - 14.765315
    ii_low_ci:
    - 4.097309
    - 23.545273
    kv_ppl_high: 8.1027
    kv_ppl_mid: 8.5701
    kv_ppl_low: 13.4922
    both_ppl_high: 41.3452
    both_ppl_mid: 24.1992
    both_ppl_low: 68.5301
    problems: 50
- exp_id: v6_importance_s025
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ii_high_median: 0.6641
    ii_mid_median: 5.3067
    ii_low_median: 24.1619
    ii_high_mean: 0.8842
    ii_mid_mean: 10.057
    ii_low_mean: 71.8854
    per_problem_ii_count: 50
    n_high: 42
    n_mid: 23
    n_low: 21
    problems: 50
    bootstrap_gradient_paired: 35.72
    bootstrap_ci_paired:
    - 9.52
    - 101.54
    bootstrap_gradient_unpaired: 36.38
    bootstrap_ci_unpaired:
    - 13.19
    - 97.61
    bootstrap_p: 0
- exp_id: v6_importance_s030
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ii_high_median: 0.8833
    ii_mid_median: 7.2706
    ii_low_median: 34.6937
    ii_high_mean: 1.5151
    ii_mid_mean: 78.8215
    ii_low_mean: 1163.9677
    per_problem_ii_count: 50
    n_high: 40
    n_mid: 22
    n_low: 20
    problems: 50
    bootstrap_gradient_paired: 41.92
    bootstrap_ci_paired:
    - 19.14
    - 299.76
    bootstrap_gradient_unpaired: 39.28
    bootstrap_ci_unpaired:
    - 21.87
    - 129.59
    bootstrap_p: 0
- exp_id: v6_importance_s015
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ii_high_median: 0.2266
    ii_mid_median: 0.7432
    ii_low_median: 2.8762
    ii_high_mean: 0.2874
    ii_mid_mean: 1.6858
    ii_low_mean: 8.5161
    per_problem_ii_count: 50
    n_high: 43
    n_mid: 32
    n_low: 24
    problems: 50
    bootstrap_gradient_paired: 11.53
    bootstrap_ci_paired:
    - 3.49
    - 23.78
    bootstrap_gradient_unpaired: 12.69
    bootstrap_ci_unpaired:
    - 4.96
    - 28.45
    bootstrap_p: 0
- exp_id: v6_importance_s020
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ii_high_median: 0.3353
    ii_mid_median: 1.6733
    ii_low_median: 9.2538
    ii_high_mean: 0.4936
    ii_mid_mean: 4.9538
    ii_low_mean: 25.8764
    per_problem_ii_count: 50
    n_high: 42
    n_mid: 28
    n_low: 21
    problems: 50
    bootstrap_gradient_paired: 11.05
    bootstrap_ci_paired:
    - 5.42
    - 69.27
    bootstrap_gradient_unpaired: 27.6
    bootstrap_ci_unpaired:
    - 6.55
    - 75.16
    bootstrap_p: 0
- exp_id: qwen_importance_s015
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: qwen_importance_s020
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: qwen_importance_s025
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: qwen_importance_s030
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: v6_random_s015
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ii_high_median: 0.1606
    ii_mid_median: 0.252
    ii_low_median: 0.1831
    ii_high_mean: 0.4563
    ii_mid_mean: 0.5134
    ii_low_mean: 0.4775
    per_problem_ii_count: 50
    n_high: 43
    n_mid: 32
    n_low: 28
    bootstrap_gradient_paired: -0.2722
    bootstrap_ci_paired:
    - -0.7039
    - 0.1548
    bootstrap_p: 0.903
    bootstrap_gradient_unpaired: -0.0592
    bootstrap_ci_unpaired:
    - -0.5341
    - 0.3877
    per_problem_ii_stats:
      high:
        min: -3.0621
        max: 5.018
        mean: 0.5386
        median: 0.2003
        std: 1.2085
      mid:
        min: -2.7245
        max: 4.6713
        mean: 0.3977
        median: 0.299
        std: 1.1456
      low:
        min: -0.4031
        max: 3.7005
        mean: 0.4806
        median: 0.2465
        std: 0.779
    verdict: FAIL
- exp_id: v6_random_s020
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ii_high_mean: 0.855584
    ii_high_median: 0.321331
    ii_high_ci:
    - -0.124133
    - 1.616883
    ii_high_winsorized_mean: 0.913496
    ii_mid_mean: 1.258123
    ii_mid_median: 0.455663
    ii_mid_ci:
    - 0.674852
    - 2.075565
    ii_mid_winsorized_mean: 1.074102
    ii_low_mean: 0.956933
    ii_low_median: 0.591916
    ii_low_ci:
    - 0.583856
    - 1.413355
    ii_low_winsorized_mean: 0.96113
    n_high: 511
    n_mid: 391
    n_low: 454
    problems: 50
    per_problem_ii_count: 50
    gradient_mean_low_over_high: 1.118
    gradient_median_low_over_high: 1.842
    pass_fail: FAIL
    perplexity_high_dense: 1.1462
    perplexity_high_both: 7.9749
    perplexity_mid_dense: 1.1226
    perplexity_mid_both: 6.8553
    perplexity_low_dense: 1.1105
    perplexity_low_both: 22.5868
- exp_id: v6_random_s025
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ii_high_median: 3.0024
    ii_mid_median: 2.9846
    ii_low_median: 2.9146
    ii_high_mean: 3.9052
    ii_mid_mean: 7.9491
    ii_low_mean: 3.9114
    per_problem_ii_count: 50
    n_high: 36
    n_mid: 25
    n_low: 24
    bootstrap_gradient_paired: -0.1199
    bootstrap_ci_paired:
    - -1.517
    - 1.2461
    bootstrap_p: 0.559
    bootstrap_gradient_unpaired: -0.8616
    bootstrap_ci_unpaired:
    - -3.3911
    - 1.5169
    per_problem_ii_stats:
      high:
        min: -6.1388
        max: 25.2471
        mean: 4.4098
        median: 3.0421
        std: 6.0734
      mid:
        min: 0.158
        max: 108.7242
        mean: 7.5626
        median: 2.1407
        std: 20.926
      low:
        min: -0.1953
        max: 12.8555
        mean: 3.5806
        median: 2.7289
        std: 3.4915
    verdict: FAIL
- exp_id: v6_random_s030
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: v6_random_s030_r2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: bf16_importance_s015
  name: ''
  status: DONE
  conclusion: success
  metrics:
    interaction_index:
      high:
        mean: -0.150213
        median: 0.005752
        ci:
        - -0.294614
        - -0.055385
        winsorized_mean: -0.062378
        skewness: -14.9912
      mid:
        mean: 0.447301
        median: 0.080738
        ci:
        - 0.267993
        - 0.668749
        winsorized_mean: 0.324751
        skewness: 4.7221
      low:
        mean: 2.405837
        median: 0.398291
        ci:
        - 1.478784
        - 3.667675
        winsorized_mean: 1.278857
        skewness: 9.5402
    per_problem_ii_stats:
      high:
        n: 49
        min: -0.188061
        max: 0.335853
        mean: -0.013405
        median: 0.00012
        std: 0.078483
      mid:
        n: 40
        min: -0.169092
        max: 3.88198
        mean: 0.308621
        median: 0.107114
        std: 0.690186
      low:
        n: 50
        min: -0.872983
        max: 9.10289
        mean: 0.725504
        median: 0.315517
        std: 1.731056
    gradient_paired_aggregate_legacy: 69.24
    median_difference: 0.3925
    n_problems: 50
    pass_fail:
      ci_overlap: true
      sign_reversal: true
      overall: PASS
    phase_stats:
      high:
        n_tokens: 21086
        n_segments: 387
      mid:
        n_tokens: 13306
        n_segments: 191
      low:
        n_tokens: 27748
        n_segments: 397
    perplexity:
      high:
        dense: 1.1689
        attn: 1.4861
        kv: 1.4481
        both: 1.5911
      mid:
        dense: 1.2269
        attn: 1.5137
        kv: 2.5971
        both: 3.4541
      low:
        dense: 1.2286
        attn: 1.6147
        kv: 8.9201
        both: 12.5084
- exp_id: bf16_importance_s020
  name: ''
  status: DONE
  conclusion: success
  metrics:
    interaction_index:
      high:
        mean: 0.1289
        median: 0.0145
        ci:
        - -0.1975
        - 0.6647
        winsorized_mean: -0.0297
        skewness: 16.67
      mid:
        mean: 1.2604
        median: 0.2027
        ci:
        - 0.7466
        - 1.8962
        winsorized_mean: 0.766
        skewness: 7.05
      low:
        mean: 6.0288
        median: 1.4963
        ci:
        - 4.4671
        - 7.9237
        winsorized_mean: 4.3426
        skewness: 6.01
    per_problem_ii_stats:
      high:
        n: 49
        min: -0.1884
        max: 0.4196
        mean: 0.0025
        median: 0.0036
        std: 0.0966
      mid:
        n: 40
        min: -0.0519
        max: 8.6969
        mean: 0.6795
        median: 0.1977
        std: 1.4998
      low:
        n: 50
        min: -1.6151
        max: 22.6875
        mean: 2.2301
        median: 1.128
        std: 4.3758
    gradient_paired_aggregate_legacy: 5.9
    median_difference: 1.4818
    n_problems: 50
    pass_fail:
      ci_overlap: true
      sign_reversal: false
      overall: PASS
    phase_stats:
      high:
        n_tokens: 21086
        n_segments: 387
      mid:
        n_tokens: 13306
        n_segments: 191
      low:
        n_tokens: 27748
        n_segments: 397
    perplexity:
      high:
        dense: 1.1689
        attn: 1.5233
        kv: 1.6191
        both: 2.1047
      mid:
        dense: 1.2269
        attn: 1.5375
        kv: 3.5164
        both: 5.4246
      low:
        dense: 1.2286
        attn: 1.6486
        kv: 15.7987
        both: 23.74
- exp_id: bf16_importance_s025
  name: ''
  status: DONE
  conclusion: success
  metrics:
    interaction_index:
      high:
        mean: 0.302756
        median: 0.032363
        ci:
        - 0.083714
        - 0.543977
        winsorized_mean: 0.200962
        skewness: 4.8826
      mid:
        mean: 5.729665
        median: 1.118069
        ci:
        - 3.455574
        - 8.471799
        winsorized_mean: 4.189902
        skewness: 8.2799
      low:
        mean: 25.852951
        median: 7.195958
        ci:
        - 19.077082
        - 33.497293
        winsorized_mean: 19.319103
        skewness: 7.3986
    per_problem_ii_stats:
      high:
        n: 49
        min: -0.316321
        max: 4.003714
        mean: 0.133714
        median: 0.009873
        std: 0.595358
      mid:
        n: 40
        min: -0.024794
        max: 18.720486
        mean: 2.537744
        median: 1.05707
        std: 3.962575
      low:
        n: 50
        min: -1.854733
        max: 75.467653
        mean: 11.28281
        median: 3.954593
        std: 16.620011
    gradient_paired_aggregate_legacy: 222.35
    median_difference: 7.1636
    n_problems: 50
    pass_fail:
      ci_overlap: true
      sign_reversal: false
      overall: PASS
    phase_stats:
      high:
        n_tokens: 21086
        n_segments: 387
      mid:
        n_tokens: 13306
        n_segments: 191
      low:
        n_tokens: 27748
        n_segments: 397
    perplexity:
      high:
        dense: 1.1689
        attn: 1.6511
        kv: 1.8628
        both: 2.7026
      mid:
        dense: 1.2269
        attn: 1.7039
        kv: 5.6205
        both: 13.3436
      low:
        dense: 1.2286
        attn: 1.8366
        kv: 31.756
        both: 63.668
- exp_id: bf16_importance_s030
  name: ''
  status: DONE
  conclusion: success
  metrics:
    interaction_index:
      high:
        mean: 0.5547
        median: 0.0534
        ci:
        - 0.2773
        - 0.9198
        winsorized_mean: 0.3367
        skewness: 10.62
      mid:
        mean: 11.3
        median: 2.2833
        ci:
        - 6.865
        - 17.2633
        winsorized_mean: 8.1752
        skewness: 9.19
      low:
        mean: 57.7946
        median: 14.6395
        ci:
        - 41.4416
        - 77.0467
        winsorized_mean: 39.3143
        skewness: 8.31
    per_problem_ii_stats:
      high:
        n: 49
        min: -0.5095
        max: 4.4457
        mean: 0.1976
        median: 0.0343
        std: 0.6793
      mid:
        n: 40
        min: -0.1989
        max: 34.0258
        mean: 5.2585
        median: 1.5173
        std: 7.9382
      low:
        n: 50
        min: -7.3027
        max: 126.7985
        mean: 22.6601
        median: 9.9731
        std: 28.4096
    gradient_paired_aggregate_legacy: 57.24
    median_difference: 14.5861
    n_problems: 50
    pass_fail:
      ci_overlap: true
      sign_reversal: false
      overall: PASS
    phase_stats:
      high:
        n_tokens: 21086
        n_segments: 387
      mid:
        n_tokens: 13306
        n_segments: 191
      low:
        n_tokens: 27748
        n_segments: 397
    perplexity:
      high:
        dense: 1.1689
        attn: 1.7123
        kv: 2.0544
        both: 3.2372
      mid:
        dense: 1.2269
        attn: 1.7894
        kv: 9.4821
        both: 24.2847
      low:
        dense: 1.2286
        attn: 1.9347
        kv: 51.6485
        both: 122.61
- exp_id: bf16_random_s015
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: bf16_random_s020
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: bf16_random_s025
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: bf16_random_s030
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: bf16_qwen_importance_s015
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: bf16_qwen_importance_s020
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: bf16_qwen_importance_s025
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: bf16_qwen_importance_s030
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: v6_random_s030_r3
  name: ''
  status: DONE
  conclusion: success
  metrics:
    II_high_mean: 9.2364
    II_mid_mean: -230.7604
    II_low_mean: -7.4119
    II_high_median: 4.0237
    II_mid_median: 2.4272
    II_low_median: 4.735
    ppl_low_both: 88.94
    per_problem_count: 50
- exp_id: bf16_ds_imp_s015
  name: ''
  status: DONE
  conclusion: killed
  metrics:
    median_difference: 0.323579
    permutation_p: 0
    cohens_d: 0.6068
    bootstrap_ci_95:
    - 0.198824
    - 0.471566
    wilcoxon_p: 0
    n_bootstrap: 10000
    n_paired: 49
- exp_id: bf16_ds_imp_s020
  name: ''
  status: DONE
  conclusion: killed
  metrics:
    median_difference: 1.15202
    permutation_p: 0
    cohens_d: 0.725
    bootstrap_ci_95:
    - 0.655454
    - 1.256001
    wilcoxon_p: 0
    n_bootstrap: 10000
    n_paired: 49
- exp_id: bf16_ds_imp_s025
  name: ''
  status: DONE
  conclusion: killed
  metrics:
    median_difference: 3.968568
    permutation_p: 0
    cohens_d: 0.9534
    bootstrap_ci_95:
    - 2.829037
    - 5.291756
    wilcoxon_p: 0
    n_bootstrap: 10000
    n_paired: 49
- exp_id: bf16_ds_imp_s030
  name: ''
  status: DONE
  conclusion: killed
  metrics:
    median_difference: 9.943595
    permutation_p: 0
    cohens_d: 1.1263
    bootstrap_ci_95:
    - 8.391554
    - 16.652865
    wilcoxon_p: 0
    n_bootstrap: 10000
    n_paired: 49
- exp_id: bf16_ds_rand_s015
  name: ''
  status: DONE
  conclusion: success
  metrics:
    interaction_index:
      high:
        mean: 0.2208
        median: 0.0931
        ci:
        - -1.0091
        - 1.5243
        median_ci:
        - 0.0024
        - 0.1515
        winsorized_mean: 0.3161
        skewness: -5.4
      mid:
        mean: -3.3604
        median: 0.0967
        ci:
        - -8.4057
        - 0.3697
        median_ci:
        - 0.0219
        - 0.197
        winsorized_mean: -0.6366
        skewness: -10.56
      low:
        mean: -1.8952
        median: 0.1026
        ci:
        - -4.9698
        - 0.2741
        median_ci:
        - 0.044
        - 0.1755
        winsorized_mean: 0.0521
        skewness: -11.57
    perplexity:
      high:
        dense: 1.1687
        attn: 3.5947
        kv: 2.9239
        both: 5.7569
      mid:
        dense: 1.2269
        attn: 297.7957
        kv: 2.915
        both: 11.3156
      low:
        dense: 1.2284
        attn: 11.3419
        kv: 3.6161
        both: 6.2886
    phase_stats:
      high:
        n_tokens: 21086
        n_segments: 387
      mid:
        n_tokens: 13306
        n_segments: 191
      low:
        n_tokens: 27748
        n_segments: 397
    n_problems: 50
    pass_fail:
      ci_overlap: false
      sign_reversal: false
      overall: FAIL
    median_difference: 0.0095
- exp_id: bf16_ds_rand_s020
  name: ''
  status: DONE
  conclusion: success
  metrics:
    interaction_index:
      high:
        mean: 1.1216
        median: 0.2918
        ci:
        - 0.0796
        - 2.5834
        median_ci:
        - 0.1598
        - 0.4581
        winsorized_mean: 1.7664
        skewness: 9.59
      mid:
        mean: -1.5827
        median: 0.3504
        ci:
        - -6.0963
        - 1.5735
        median_ci:
        - 0.1993
        - 0.5226
        winsorized_mean: 0.5839
        skewness: -12.31
      low:
        mean: -0.4116
        median: 0.2763
        ci:
        - -2.6034
        - 1.209
        median_ci:
        - 0.2194
        - 0.5487
        winsorized_mean: 0.9942
        skewness: -10.07
    perplexity:
      high:
        dense: 1.1687
        attn: 3.1905
        kv: 3.8002
        both: 8.8129
      mid:
        dense: 1.2269
        attn: 67.8504
        kv: 3.788
        both: 11.4974
      low:
        dense: 1.2284
        attn: 8.592
        kv: 5.0078
        both: 9.2001
    phase_stats:
      high:
        n_tokens: 21086
        n_segments: 387
      mid:
        n_tokens: 13306
        n_segments: 191
      low:
        n_tokens: 27748
        n_segments: 397
    n_problems: 50
    pass_fail:
      ci_overlap: false
      sign_reversal: false
      overall: FAIL
    median_difference: -0.0155
- exp_id: bf16_ds_rand_s025
  name: ''
  status: DONE
  conclusion: success
  metrics:
    interaction_index:
      high:
        mean: 3.59
        median: 0.8182
        ci:
        - 1.4021
        - 6.2327
        median_ci:
        - 0.5075
        - 1.7217
        winsorized_mean: 6.3965
        skewness: -7.57
      mid:
        mean: -1.8455
        median: 0.9324
        ci:
        - -10.3663
        - 4.9342
        median_ci:
        - 0.7331
        - 1.7003
        winsorized_mean: 3.1014
        skewness: -12.76
      low:
        mean: 0.7212
        median: 1.3627
        ci:
        - -4.2068
        - 4.5006
        median_ci:
        - 1.0869
        - 2.6866
        winsorized_mean: 4.1866
        skewness: -15.85
    perplexity:
      high:
        dense: 1.1687
        attn: 7.237
        kv: 4.9751
        both: 17.7423
      mid:
        dense: 1.2269
        attn: 868.3199
        kv: 5.1165
        both: 29.4661
      low:
        dense: 1.2284
        attn: 24.3571
        kv: 6.7993
        both: 17.9694
    phase_stats:
      high:
        n_tokens: 21086
        n_segments: 387
      mid:
        n_tokens: 13306
        n_segments: 191
      low:
        n_tokens: 27748
        n_segments: 397
    n_problems: 50
    pass_fail:
      ci_overlap: false
      sign_reversal: false
      overall: FAIL
    median_difference: 0.5445
- exp_id: bf16_ds_rand_s030
  name: ''
  status: DONE
  conclusion: success
  metrics:
    interaction_index:
      high:
        mean: 7.5555
        median: 2.5031
        ci:
        - 4.4087
        - 11.6199
        median_ci:
        - 1.3292
        - 4.1205
        winsorized_mean: null
        skewness: null
      mid:
        mean: 6.2518
        median: 2.5918
        ci:
        - 2.1767
        - 10.4757
        median_ci:
        - 1.8397
        - 3.7888
        winsorized_mean: null
        skewness: null
      low:
        mean: 6.8323
        median: 4.0414
        ci:
        - 3.2428
        - 10.6996
        median_ci:
        - 2.2686
        - 6.3579
        winsorized_mean: null
        skewness: null
    perplexity:
      high:
        dense: 1.1687
        attn: 16.7892
        kv: 8.8073
        both: 40.7553
      mid:
        dense: 1.2269
        attn: 2461.9219
        kv: 8.6662
        both: 62.4422
      low:
        dense: 1.2284
        attn: 55.2916
        kv: 11.5789
        both: 37.6009
    phase_stats:
      high:
        n_tokens: 21086
        n_segments: 387
      mid:
        n_tokens: 13306
        n_segments: 191
      low:
        n_tokens: 27748
        n_segments: 397
    n_problems: 50
    pass_fail:
      ci_overlap: false
      sign_reversal: false
      overall: FAIL
    median_difference: 1.5383
- exp_id: bf16_qw_imp_s015
  name: ''
  status: DONE
  conclusion: success
  metrics:
    median_difference: 0.047619
    permutation_p: 0.0001
    cohens_d: 0.3705
    bootstrap_ci_95:
    - -0.005077
    - 0.109517
    wilcoxon_p: 0.02958
    n_bootstrap: 10000
    n_paired: 46
- exp_id: bf16_qw_imp_s020
  name: ''
  status: DONE
  conclusion: success
  metrics:
    median_difference: 0.207511
    permutation_p: 0
    cohens_d: 0.7224
    bootstrap_ci_95:
    - 0.067222
    - 0.40226
    wilcoxon_p: 3.4e-05
    n_bootstrap: 10000
    n_paired: 46
- exp_id: bf16_qw_imp_s025
  name: ''
  status: DONE
  conclusion: success
  metrics:
    median_difference: 1.108706
    permutation_p: 0
    cohens_d: 1.2329
    bootstrap_ci_95:
    - 0.609247
    - 1.469002
    wilcoxon_p: 0
    n_bootstrap: 10000
    n_paired: 46
- exp_id: bf16_qw_imp_s030
  name: ''
  status: DONE
  conclusion: success
  metrics:
    median_difference: 2.619385
    permutation_p: 0
    cohens_d: 1.4394
    bootstrap_ci_95:
    - 1.722281
    - 3.651063
    wilcoxon_p: 0
    n_bootstrap: 10000
    n_paired: 46
- exp_id: bf16_qw_rand_s015
  name: ''
  status: DONE
  conclusion: success
  metrics:
    interaction_index:
      high:
        mean: 1.6652
        median: 0.1381
        ci:
        - 1.0986
        - 2.4042
        median_ci:
        - 0.1025
        - 0.2074
        winsorized_mean: 1.0044
        skewness: 7.1842
      mid:
        mean: 1.6975
        median: 0.2194
        ci:
        - 0.4473
        - 3.4612
        median_ci:
        - -0.0048
        - 0.6621
        winsorized_mean: 1.4038
        skewness: 3.2101
      low:
        mean: 1.4082
        median: 0.1878
        ci:
        - 0.8358
        - 2.06
        median_ci:
        - 0.0962
        - 0.3139
        winsorized_mean: 0.9403
        skewness: 7.1113
    perplexity:
      high:
        dense: 1.0737
        attn: 1.3939
        kv: 2.0487
        both: 4.2076
      mid:
        dense: 1.1322
        attn: 1.4175
        kv: 2.3709
        both: 4.6105
      low:
        dense: 1.1517
        attn: 1.7177
        kv: 3.3253
        both: 5.4788
    phase_stats:
      high:
        n_tokens: 16289
        n_segments: 295
      mid:
        n_tokens: 4372
        n_segments: 26
      low:
        n_tokens: 32227
        n_segments: 276
    n_problems: 50
    pass_fail:
      ci_overlap: true
      sign_reversal: false
      overall: FAIL
    median_difference: -0.029401
    permutation_test:
      p_value: 0.7657
      B: 10000
    cohens_d: -0.0507
    bootstrap_ci_95:
    - -0.2106
    - 0.2124
    wilcoxon_p: 0.862554
    phase_median_ii:
      high: 0.1381
      mid: 0.2194
      low: 0.1878
- exp_id: bf16_qw_rand_s020
  name: ''
  status: DONE
  conclusion: success
  metrics:
    interaction_index:
      high:
        mean: 2.58579
        median: 0.48549
        ci:
        - 1.769404
        - 3.501692
        median_ci:
        - 0.304626
        - 0.658814
        winsorized_mean: 1.80021
        skewness: 5.4038
      mid:
        mean: 5.69684
        median: 0.76699
        ci:
        - 1.69004
        - 12.276143
        median_ci:
        - 0.482838
        - 3.392541
        winsorized_mean: 4.304174
        skewness: 3.526
      low:
        mean: 65.915714
        median: 0.614438
        ci:
        - -18.581948
        - 221.709429
        median_ci:
        - 0.484725
        - 0.848787
        winsorized_mean: 2.389244
        skewness: 16.2163
    perplexity:
      high:
        dense: 1.0737
        attn: 1.6115
        kv: 2.5041
        both: 5.9394
      mid:
        dense: 1.1322
        attn: 1.7583
        kv: 3.0658
        both: 10.5578
      low:
        dense: 1.1517
        attn: 75.631
        kv: 4.3535
        both: 140.6269
    phase_stats:
      high:
        n_tokens: 16289
        n_segments: 295
      mid:
        n_tokens: 4372
        n_segments: 26
      low:
        n_tokens: 32227
        n_segments: 276
    n_problems: 50
    pass_fail:
      ci_overlap: true
      sign_reversal: false
      overall: FAIL
    median_difference: 0.128948
    permutation_test:
      p_value: 0.352
      B: 10000
    cohens_d: 0.247
    bootstrap_ci_95:
    - -0.139
    - 0.215
    wilcoxon_p: 0.149
    phase_median_ii:
      high: 0.4739
      mid: 0.8757
      low: 0.4847
- exp_id: bf16_qw_rand_s025
  name: ''
  status: DONE
  conclusion: success
  metrics:
    interaction_index:
      high:
        mean: 14.4213
        median: 1.6043
        ci:
        - 7.1074
        - 23.4587
        median_ci:
        - 0.6977
        - 3.0736
        winsorized_mean: 9.3765
        skewness: 4.8263
      mid:
        mean: 18.6458
        median: 2.2225
        ci:
        - 3.3729
        - 41.6037
        median_ci:
        - 0.6093
        - 11.5889
        winsorized_mean: 14.2901
        skewness: 3.8245
      low:
        mean: 17.7277
        median: 2.2641
        ci:
        - 4.3523
        - 37.2093
        median_ci:
        - 1.2218
        - 4.8561
        winsorized_mean: 9.9876
        skewness: 5.7652
    perplexity:
      high:
        dense: 1.0737
        attn: 2.0183
        kv: 3.1882
        both: 9.7654
      mid:
        dense: 1.1322
        attn: 2.3476
        kv: 4.0124
        both: 17.3298
      low:
        dense: 1.1517
        attn: 2.7834
        kv: 5.8762
        both: 25.4321
    phase_stats:
      high:
        n_tokens: 16289
        n_segments: 295
      mid:
        n_tokens: 4372
        n_segments: 26
      low:
        n_tokens: 32227
        n_segments: 276
    n_problems: 50
    pass_fail:
      ci_overlap: true
      sign_reversal: false
      overall: FAIL
    median_difference: 1.144074
    permutation_test:
      p_value: 0.1679
      B: 10000
    cohens_d: 0.1574
    bootstrap_ci_95:
    - -0.3166
    - 4.1645
    wilcoxon_p: 0.010313
    phase_median_ii:
      high: 1.6043
      mid: 2.2225
      low: 2.2641
- exp_id: bf16_qw_rand_s030
  name: ''
  status: DONE
  conclusion: success
  metrics:
    median_high: 4.200557
    median_mid: 6.477036
    median_low: 8.065662
    median_diff: 2.418272
    permutation_p: 0.012
    cohens_d: -0.03513
    wilcoxon_p: 0.01566
    bootstrap_ci_low: 0.241897
    bootstrap_ci_high: 3.314824
- exp_id: c4_entropy
  name: ''
  status: DONE
  conclusion: success
  metrics:
    importance_entropy_delta:
      s015: -0.0402
      s020: -0.0472
      s025: -0.0446
      s030: -0.0436
    random_entropy_delta:
      s015: 0.1283
      s020: 0.136
      s025: 0.2171
      s030: 0.2327
    importance_gini_delta:
      s015: -0.0301
      s020: -0.0404
      s025: -0.0647
      s030: -0.0806
    random_gini_delta:
      s015: -0.0309
      s020: -0.0403
      s025: -0.062
      s030: -0.0732
    importance_cv_delta:
      s015: -0.564
      s020: -0.774
      s025: -1.287
      s030: -1.665
    random_cv_delta:
      s015: -1.021
      s020: -1.203
      s025: -1.923
      s030: -2.137
    problems_completed: 30
    runtime_minutes: 69.1
- exp_id: qwen_c4_entropy
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    problems_completed: 30
    qwen_importance_entropy_delta:
      s015: -0.0733
      s020: -0.0759
      s025: 0.0451
      s030: -0.0072
    qwen_random_entropy_delta:
      s015: 0.0838
      s020: 0.0901
      s025: 0.2168
      s030: 0.1968
    qwen_importance_gini_delta:
      s015: -0.0103
      s020: -0.0121
      s025: -0.01
      s030: -0.0202
    qwen_random_gini_delta:
      s015: -0.0186
      s020: -0.0229
      s025: -0.0337
      s030: -0.0448
    qwen_importance_cv_delta:
      s015: -0.045
      s020: -0.208
      s025: -1.491
      s030: -1.142
    qwen_random_cv_delta:
      s015: -0.778
      s020: -0.889
      s025: -1.5
      s030: -1.677
    cross_model_notes: random entropy increase consistent; importance entropy collapse
      inconsistent at s025 (reversed to +0.045) and near-zero at s030; gini/cv directions
      consistent but Qwen magnitudes smaller
- exp_id: bf16_ds_imp_s010
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    verdict: FAIL
    problems: 50
    II_high_sparsity_median: 0.0027
    II_high_sparsity_mean: -0.1998
    II_low_sparsity_median: 0.0151
    II_low_sparsity_mean: -0.1066
    II_mid_sparsity_median: 0.0061
    II_mid_sparsity_mean: -0.0131
    high_sparsity_tokens: 21086
    low_sparsity_tokens: 27748
    mid_sparsity_tokens: 13306
- exp_id: bf16_ds_imp_s035
  name: ''
  status: DONE
  conclusion: success
  metrics:
    verdict: PASS
    problems: 50
    II_high_sparsity_median: 0.1051
    II_high_sparsity_mean: 1.4309
    II_low_sparsity_median: 28.7649
    II_low_sparsity_mean: 104.1892
    II_mid_sparsity_median: 4.9542
    II_mid_sparsity_mean: 20.326
    high_sparsity_tokens: 21086
    low_sparsity_tokens: 27748
    mid_sparsity_tokens: 13306
    ci_overlap_test: low_sparsity vs mid_sparsity CI non-overlapping at 0.35
- exp_id: bf16_qw_imp_s010
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n_problems: 50
    overall_verdict: PASS
    ci_overlap_test: PASS
    sign_reversal_test: FAIL
    high_sparsity_II_median: 0.0001
    high_sparsity_II_median_CI:
    - -0.0028
    - 0.0005
    high_sparsity_II_mean: -0.0887
    high_sparsity_II_mean_CI:
    - -0.1235
    - -0.0591
    low_sparsity_II_median: -0.0444
    low_sparsity_II_median_CI:
    - -0.0967
    - -0.0152
    low_sparsity_II_mean: -0.2431
    low_sparsity_II_mean_CI:
    - -0.3817
    - -0.1202
    mid_sparsity_II_median: -0.0359
    mid_sparsity_II_median_CI:
    - -0.0963
    - -0.015
    mid_sparsity_II_mean: -0.084
    mid_sparsity_II_mean_CI:
    - -0.1366
    - -0.035
    ppl_high_dense: 1.074
    ppl_high_both: 1.228
    ppl_low_dense: 1.152
    ppl_low_both: 3.204
    ppl_mid_dense: 1.133
    ppl_mid_both: 1.741
- exp_id: bf16_qw_imp_s035
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n_problems: 50
    overall_verdict: PASS
    ci_overlap_test: PASS
    sign_reversal_test: FAIL
    high_sparsity_II_median: 0.0232
    high_sparsity_II_median_CI:
    - 0.0154
    - 0.0383
    high_sparsity_II_mean: 0.1643
    high_sparsity_II_mean_CI:
    - 0.0844
    - 0.2495
    low_sparsity_II_median: 8.2358
    low_sparsity_II_median_CI:
    - 6.1564
    - 10.9231
    low_sparsity_II_mean: 18.9673
    low_sparsity_II_mean_CI:
    - 14.5015
    - 23.9752
    mid_sparsity_II_median: 0.9577
    mid_sparsity_II_median_CI:
    - 0.171
    - 3.5575
    mid_sparsity_II_mean: 8.0734
    mid_sparsity_II_mean_CI:
    - 2.0224
    - 16.8946
    ppl_high_dense: 1.0738
    ppl_high_both: 2.3435
    ppl_low_dense: 1.1518
    ppl_low_both: 58.0358
    ppl_mid_dense: 1.1327
    ppl_mid_both: 20.9912
    high_sparsity_tokens: 16289
    low_sparsity_tokens: 32227
    mid_sparsity_tokens: 4372
- exp_id: c2_n500_deepseek
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n_problems: 500
    effective_n: 496
    mid_null_rate: 0.102
    imp_s015_median_ii: 0.3907
    imp_s015_ci:
    - 0.3496
    - 0.4431
    imp_s015_wilcoxon_p: 1.27e-70
    imp_s020_median_ii: 1.2149
    imp_s020_ci:
    - 1.1072
    - 1.3365
    imp_s020_wilcoxon_p: 3.98e-75
    imp_s025_median_ii: 3.9857
    imp_s025_ci:
    - 3.5272
    - 4.3588
    imp_s025_wilcoxon_p: 1.99e-78
    imp_s030_median_ii: 8.4813
    imp_s030_ci:
    - 7.7543
    - 9.6919
    imp_s030_wilcoxon_p: 1.09e-79
    rand_s015_median_ii: 0.0139
    rand_s015_wilcoxon_p: 0.863
    rand_s020_median_ii: 0.0315
    rand_s020_wilcoxon_p: 0.28
    rand_s025_median_ii: 0.2574
    rand_s025_bonf_p: 0.005839
    rand_s025_fdr_p: 0.001914
    rand_s030_median_ii: 0.5096
    rand_s030_bonf_p: 0.005903
    rand_s030_fdr_p: 0.001914
    dz_s015_s020: -0.925
    dz_s020_s025: -0.824
    dz_s025_s030: -0.773
    dz_s015_s030: -0.944
    all_dz_reliable: true
    dose_response_monotonic: true
    dose_response_spearman_rho: 1
    dose_response_perm_p: 0.0417
    imp_rand_ratio_range: 15.5-38.6x
    bonferroni_k: 4
    bonferroni_note: Bonferroni k=4 family-wise (D066 revision)
- exp_id: c3_llama_arch
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: c2_ds_n500
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: c2_qw_n500
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: c3_llama
  name: ''
  status: DONE
  conclusion: success
  metrics:
    model: DeepSeek-R1-Distill-Llama-8B
    n_problems: 50
    n_valid: 49
    n_skipped: 1
    conditions_completed: 8/8
    n_bootstrap: 10000
    bonferroni_k: 4
    imp_vs_rand_dz:
      s015: 0.1923
      s020: 0.255
      s025: 0.2902
      s030: 0.3352
    imp_vs_rand_dz_ci:
      s015:
      - -0.0862
      - 0.496
      s020:
      - -0.0248
      - 0.5381
      s025:
      - 0.0081
      - 0.6121
      s030:
      - 0.0606
      - 0.6629
    imp_vs_rand_dz_interpretation:
      s015: negligible
      s020: small
      s025: small
      s030: small
    imp_vs_rand_dz_monotonic: true
    phase_gradient_importance_dz:
      s015: 1.0079
      s020: 1.108
      s025: 1.1227
      s030: 1.0038
    phase_gradient_importance_dz_ci:
      s015:
      - 0.593
      - 1.7025
      s020:
      - 0.8144
      - 1.5698
      s025:
      - 0.8735
      - 1.5768
      s030:
      - 0.8099
      - 1.3519
    phase_gradient_importance_interpretation: all_large
    phase_gradient_random_dz:
      s015: 0.3497
      s020: 0.373
      s025: 0.4476
      s030: 0.4385
    phase_gradient_random_dz_ci:
      s015:
      - 0.0665
      - 0.6916
      s020:
      - 0.0868
      - 0.7335
      s025:
      - 0.1669
      - 0.7698
      s030:
      - 0.1966
      - 0.707
    phase_gradient_random_interpretation: all_small
    median_diff:
      s015: 0.0203
      s020: 0.0221
      s025: 0.0947
      s030: 0.3562
    median_diff_ci:
      s015:
      - 0.0016
      - 0.0435
      s020:
      - -0.0905
      - 0.187
      s025:
      - -0.0037
      - 0.3029
      s030:
      - -0.0691
      - 0.5442
    wilcoxon_p:
      s015: 0.0549
      s020: 0.0632
      s025: 0.0209
      s030: 0.0074
    wilcoxon_p_bonferroni:
      s015: 0.2195
      s020: 0.2527
      s025: 0.0834
      s030: 0.0294
    significant_bonferroni:
      s015: false
      s020: false
      s025: false
      s030: true
    cross_arch_comparison:
      deepseek_importance_dz:
        s015: 0.4416
        s020: 0.5195
        s025: 0.6831
        s030: 0.8031
      llama_importance_dz:
        s015: 1.0079
        s020: 1.108
        s025: 1.1227
        s030: 1.0038
      delta:
        s015: 0.5663
        s020: 0.5885
        s025: 0.4396
        s030: 0.2007
      note: LLaMA shows uniformly large d_z (all >1.0) vs DeepSeek medium-to-large
- exp_id: c5b_pilot
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    s025_uniform_median_ii: 1.0435
    s025_oracle_median_ii: 0.856
    s025_oracle_recovery_pct: 18
    s025_oracle_recovery_ci:
    - -39
    - 45.8
    s025_oracle_wilcoxon_p: 0.0021
    s025_heuristic_median_ii: 0.7127
    s025_heuristic_recovery_pct: 31.7
    s025_heuristic_recovery_ci:
    - -22.8
    - 66
    s025_heuristic_wilcoxon_p: 0.0236
    gate_criterion: oracle_recovery > 30%
    gate_result: FAIL
    s030_status: not_completed
    n_problems: 30
- exp_id: c2_qw_n500_r3
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n_problems: 500
    effective_n: 475
    filter: low+high valid only (mid-null allowed)
    mid_null_rate: 0.452
    imp_s015_median_ii: 0.0659
    imp_s015_ci:
    - 0.0492
    - 0.0925
    imp_s015_wilcoxon_p: 8.66e-15
    imp_s015_bonf_p: 3.46e-14
    imp_s020_median_ii: 0.3073
    imp_s020_ci:
    - 0.2612
    - 0.3564
    imp_s020_wilcoxon_p: 6.84e-42
    imp_s020_bonf_p: 2.74e-41
    imp_s025_median_ii: 1.0745
    imp_s025_ci:
    - 0.9766
    - 1.1787
    imp_s025_wilcoxon_p: 1.06e-68
    imp_s025_bonf_p: 4.25e-68
    imp_s030_median_ii: 3.155
    imp_s030_ci:
    - 2.7834
    - 3.5582
    imp_s030_wilcoxon_p: 9.21e-74
    imp_s030_bonf_p: 3.69e-73
    rand_s015_median_ii: -0.0111
    rand_s015_wilcoxon_p: 0.172
    rand_s015_bonf_p: 0.687
    rand_s020_median_ii: 0.0153
    rand_s020_wilcoxon_p: 0.2
    rand_s020_bonf_p: 0.8
    rand_s025_median_ii: 0.3931
    rand_s025_wilcoxon_p: 1.59e-11
    rand_s025_bonf_p: 6.37e-11
    rand_s025_fdr_p: 2.63e-11
    rand_s030_median_ii: 0.9127
    rand_s030_wilcoxon_p: 2.92e-15
    rand_s030_bonf_p: 1.17e-14
    rand_s030_fdr_p: 5.61e-15
    dz_s015_s020: -0.629
    dz_s020_s025: -0.865
    dz_s025_s030: -0.767
    dz_s015_s030: -0.923
    all_dz_reliable: true
    dose_response_monotonic: true
    dose_response_spearman_rho: 1
    dose_response_perm_p: 0.0417
    imp_rand_ratio_range: 2.7-20.1x
    bonferroni_k: 4
    bonferroni_note: Bonferroni k=4 family-wise (D066 revision)
- exp_id: sf5_asymmetric_spot
  name: ''
  status: DONE
  conclusion: success
  metrics:
    config_a_h02_kv03:
      II_low: 19.51
      II_mid: 6.05
      II_high: 0.38
      D: 19.13
    config_b_h03_kv02:
      II_low: 18.77
      II_mid: 3.97
      II_high: 0.52
      D: 18.25
    pre_registered_criterion_passed: true
    gradient_direction: II_low >> II_mid >> II_high (consistent with symmetric baseline)
- exp_id: gsm8k_profiling_ds
  name: ''
  status: DONE
  conclusion: success
  metrics:
    version: v3_median
    n_problems: 50
    method: median + Wilcoxon + bootstrap_median(B=10000)
    importance:
      s015:
        median_gradient: 0.241
        ci_low: 0.077
        ci_high: 0.478
        wilcoxon_p: 0.0003
      s020:
        median_gradient: 0.74
        ci_low: 0.314
        ci_high: 1.119
        wilcoxon_p: 0.0001
      s025:
        median_gradient: 1.992
        ci_low: 0.933
        ci_high: 2.82
        wilcoxon_p: 0.0001
      s030:
        median_gradient: 4.682
        ci_low: 2.121
        ci_high: 10.557
        wilcoxon_p: 0.0001
    imp_rand_ratio:
      s015: 2.3
      s020: 2.5
      s025: 3.8
      s030: 2.8
    dose_response_monotonic: true
- exp_id: gsm8k_profiling_qw
  name: ''
  status: DONE
  conclusion: success
  metrics:
    version: v3_median
    n_problems: 50
    method: median + Wilcoxon + bootstrap_median(B=10000)
    importance:
      s015:
        median_gradient: 0.039
      s020:
        median_gradient: 0.158
      s025:
        median_gradient: 1.1
      s030:
        median_gradient: 2.092
    qw_rand_s030: INVALID
- exp_id: think_phase_validation
  name: ''
  status: DONE
  conclusion: success
  metrics:
    effective_n: 48
    skipped_problems: 2
    median_kappa: 0.887
    thinking_in_low_sparsity_phase: 0.578
    answer_in_high_sparsity_phase: 0.627
    note: Phase segmentation based on dense model — 4 sparsity conditions share identical
      phase boundaries, effective sample n=48 not n=192
- exp_id: r9c2-spike
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: r9c2-spike-v2
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: r9c2-spike-v3
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: c2_accuracy_eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n_problems: 50
    ds_dense_acc: 0.52
    ds_s015_acc: 0.36
    ds_s015_delta: -0.16
    ds_s030_acc: 0.1
    ds_s030_delta: -0.42
    qw_dense_acc: 0.32
    qw_s015_acc: 0.34
    qw_s015_delta: 0.02
    qw_s030_acc: 0.14
    qw_s030_delta: -0.18
    ds_s030_chinese_reasoning_rate: 0.4
    ds_dense_truncation_rate: 0.56
    note: v2 rescored with fixed radical+degree matcher. DS s015 34→36, QW s015 32→34
- exp_id: acc_ds_s020
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    ds_s020_acc: 0.26
    ds_s020_acc_v2: 0.26
    ds_s020_correct: 13
    ds_s020_total: 50
    ds_s020_delta_vs_dense: -0.26
    output_truncated_count: 32
    output_truncated_rate: 0.64
    extraction_failure_count: 31
    extraction_failure_rate: 0.62
    total_time_s: 1560
    note: v2 rescored with fixed radical+degree matcher; 0 changes. Dense baseline=0.52
- exp_id: acc_ds_s025
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    accuracy: 0.08
    correct: 4
    total: 50
    null_count: 37
    null_rate: 0.74
    output_truncated_count: 38
    output_truncated_rate: 0.76
    wrong_count: 9
    wrong_rate: 0.18
    extraction_failure_count: 1
    extraction_failure_rate: 0.02
    total_time_s: 1670.5
    heads_pruned: 196
    delta_vs_dense: -0.44
- exp_id: acc_qw_s020
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    qw_s020_acc: 0.26
    qw_s020_correct: 13
    qw_s020_total: 50
    qw_s020_delta_vs_dense: -0.06
    null_count: 2
    null_rate: 0.04
    output_truncated_count: 2
    output_truncated_rate: 0.04
    extraction_failure_count: 0
    extraction_failure_rate: 0
    wrong_count: 35
    wrong_rate: 0.7
    heads_pruned: 140
    total_time_s: 598
    note: v2 rescored with fixed radical+degree matcher
- exp_id: acc_qw_s025
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    qw_s025_acc: 0.32
    qw_s025_correct: 16
    qw_s025_total: 50
    qw_s025_delta_vs_dense: 0
    null_count: 8
    null_rate: 0.16
    output_truncated_count: 2
    output_truncated_rate: 0.04
    extraction_failure_count: 6
    extraction_failure_rate: 0.12
    wrong_count: 26
    wrong_rate: 0.52
    heads_pruned: 196
    total_time_s: 559
    note: v2 rescored with fixed radical+degree matcher; 3 problems flipped (sqrt+degree)
- exp_id: acc_qw_s020_n100
  name: ''
  status: DONE
  conclusion: success
  metrics:
    batch1_acc: 0.26
    batch1_correct: 13
    batch1_total: 50
    batch1_source: acc_qw_s020_b1_8k (v2, 8k tokens)
    batch2_acc: 0.46
    batch2_correct: 23
    batch2_total: 50
    combined_acc: 0.36
    combined_correct: 36
    combined_total: 100
    note: 'batch effect: batch1=26% vs batch2=46%, Δ=20pp'
- exp_id: acc_qw_s025_n100
  name: ''
  status: DONE
  conclusion: success
  metrics:
    batch1_acc: 0.32
    batch1_correct: 16
    batch1_total: 50
    batch1_source: acc_qw_s025_b1_8k (v2, 8k tokens)
    batch2_acc: 0.34
    batch2_correct: 17
    batch2_total: 50
    combined_acc: 0.33
    combined_correct: 33
    combined_total: 100
- exp_id: acc_ds_dense_8k
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: acc_ds_s015_8k
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: acc_ds_s020_8k
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: acc_ds_s025_8k
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: acc_ds_s030_8k
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: acc_qw_dense_n100
  name: ''
  status: DONE
  conclusion: success
  metrics:
    batch1_correct: 22
    batch1_total: 50
    batch1_acc: 0.44
    batch1_source: acc_qw_dense_b1_8k (v2, 8k tokens)
    batch2_correct: 24
    batch2_total: 50
    batch2_acc: 0.48
    combined_correct: 46
    combined_total: 100
    combined_acc: 0.46
- exp_id: acc_qw_s015_n100
  name: ''
  status: DONE
  conclusion: success
  metrics:
    batch1_acc: 0.46
    batch1_correct: 23
    batch1_total: 50
    batch1_source: acc_qw_s015_b1_8k (v2, 8k tokens)
    batch2_acc: 0.38
    batch2_correct: 19
    batch2_total: 50
    combined_acc: 0.42
    combined_correct: 42
    combined_total: 100
- exp_id: acc_qw_s030_n100
  name: ''
  status: DONE
  conclusion: success
  metrics:
    batch1_correct: 7
    batch1_total: 50
    batch1_acc: 0.14
    batch1_source: acc_qw_s030_b1_8k (v2, 8k tokens)
    batch2_correct: 12
    batch2_total: 50
    batch2_acc: 0.24
    combined_correct: 19
    combined_total: 100
    combined_acc: 0.19
- exp_id: acc_ds_s015_8k_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.48
    correct: 24
    total: 50
    truncation_rate: 0.32
    truncated_count: 16
    non_truncated_accuracy: 0.706
    non_truncated_correct: 24
    non_truncated_total: 34
    wall_time_s: 3967
    max_new_tokens: 8192
- exp_id: acc_ds_s020_8k_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.3
    correct: 15
    total: 50
    truncated_count: 28
    truncated_rate: 0.56
    extraction_failures: 1
    non_truncated_accuracy: 0.682
    non_truncated_correct: 15
    non_truncated_total: 22
    total_time_seconds: 5549
    max_new_tokens: 8192
- exp_id: acc_ds_s025_8k_v2
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    accuracy: 0.08
    correct: 4
    total: 50
    truncated_count: 38
    truncated_rate: 0.76
    avg_tokens: 6343.8
    max_new_tokens: 8192
    total_time_seconds: 6827.8
    null_count: 36
- exp_id: acc_ds_s030_8k_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.04
    correct: 2
    total: 50
    truncation_rate: 0.76
    truncated_count: 38
    extraction_failures: 3
    non_truncated_accuracy: 0.167
    non_truncated_correct: 2
    non_truncated_total: 12
    max_new_tokens: 8192
    avg_tokens: 6566.3
    total_time_seconds: 7095.1
- exp_id: gsm8k_qw_rand_s025
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: gsm8k_qw_rand_s030
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: acc_qw_s020_n100_b2_fix
  name: ''
  status: DONE
  conclusion: success
  metrics:
    batch2_correct: 23
    batch2_total: 50
    batch2_acc: 0.46
    batch1_correct_v2: 13
    batch1_total: 50
    batch1_acc_v2: 0.26
    combined_correct: 36
    combined_total: 100
    combined_acc: 0.36
    null_count: 2
    truncated_count: 1
    total_time_seconds: 884.3
    max_new_tokens: 8192
    original_batch2_correct: 22
    original_batch2_acc: 0.44
    delta_vs_original: +1 correct (+0.02 acc)
- exp_id: acc_qw_s025_n100_b2_fix
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.34
    correct: 17
    n_problems: 50
    truncation_rate: 0.06
    truncated_count: 3
    avg_tokens: 1044
    max_new_tokens: 8192
    total_time_seconds: 1099
    batch: b2 (problems 51-100)
    merged_n100_accuracy: 0.33
    merged_n100_correct: 33
    merged_n100_note: batch1 used max_new_tokens=2048, batch2_fix used 8192 — mismatch
- exp_id: acc_ds_dense_8k_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.74
    correct: 37
    n_problems: 50
    truncation_rate: 0.16
    truncated_count: 8
    avg_tokens: 3126
    max_new_tokens: 8192
    total_time_seconds: 2882
- exp_id: gsm8k_qw_rand_s025_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    verdict: PASS
    n_problems: 50
    n_bootstrap: 1000
    seed: 42
    high_sparsity:
      n_segments: 216
      n_tokens: 9326
      ppl_dense: 1.0695
      ppl_attn: 5.9362
      ppl_kv: 3.4316
      ppl_both: 15.7484
      ii_mean: 6.5954
      ii_ci:
      - 1.1114
      - 11.3791
      ii_median: 0.7176
      ii_median_ci:
      - 0.5959
      - 0.9347
      winsorized_mean: 6.5046
      skewness: -4.6807
      outlier_count: 3
    low_sparsity:
      n_segments: 252
      n_tokens: 29224
      ppl_dense: 1.1972
      ppl_attn: 11.5347
      ppl_kv: 5.6038
      ppl_both: 21.6874
      ii_mean: 2.3883
      ii_ci:
      - -8.4602
      - 11.029
      ii_median: 1.4587
      ii_median_ci:
      - 1.1121
      - 2.0451
      winsorized_mean: 5.8911
      skewness: -7.6074
      outlier_count: 4
    mid_sparsity:
      n_segments: 51
      n_tokens: 5954
      ppl_dense: 1.2601
      ppl_attn: 13.4132
      ppl_kv: 6.4841
      ppl_both: 20.8714
      ii_mean: 4.5407
      ii_ci:
      - -4.8854
      - 12.4605
      ii_median: 1.1272
      ii_median_ci:
      - 0.637
      - 3.3729
      winsorized_mean: 6.3284
      skewness: -3.4048
      outlier_count: 1
- exp_id: gsm8k_qw_rand_s030_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    verdict: PASS
    n_problems: 50
    n_bootstrap: 1000
    seed: 42
    high_sparsity:
      n_segments: 216
      n_tokens: 9326
      null_ratio: 2/50
      ppl_dense: 1.0695
      ppl_attn: 6.5613
      ppl_kv: 4.481
      ppl_both: 23.7486
      ii_mean: 11.83
      ii_median: 2.31
      ii_ci:
      - 6.17
      - 17.04
      ii_median_ci:
      - 1.64
      - 2.81
      winsorized_mean: 10.55
      skewness: -2.29
      outlier_count: 7
    low_sparsity:
      n_segments: 252
      n_tokens: 29224
      null_ratio: 5/50
      ppl_dense: 1.1972
      ppl_attn: 6.3283
      ppl_kv: 8.5374
      ppl_both: 56.2304
      ii_mean: 31.26
      ii_median: 5.2
      ii_ci:
      - 17.84
      - 47.86
      ii_median_ci:
      - 3.95
      - 7.24
      winsorized_mean: 16.35
      skewness: 7.57
      outlier_count: 4
    mid_sparsity:
      n_segments: 51
      n_tokens: 5954
      null_ratio: 17/50
      ppl_dense: 1.2601
      ppl_attn: 18.6162
      ppl_kv: 11.6625
      ppl_both: 47.9019
      ii_mean: 18.02
      ii_median: 2.7
      ii_ci:
      - 0.09
      - 36.69
      ii_median_ci:
      - 1.46
      - 8.77
      winsorized_mean: 18.22
      skewness: 0.43
      outlier_count: 2
- exp_id: acc_qw_dense_b1_8k
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.44
    correct: 22
    n_problems: 50
    truncation_rate: 0.02
    truncated_count: 1
    avg_tokens: 759.7
    max_tokens_generated: 8192
    max_new_tokens: 8192
    total_time_seconds: 681.8
    null_count: 0
    batch: b1_v2 (problems 1-50, 8k tokens)
    old_batch1_acc: 0.32
    old_batch1_correct: 16
    new_combined_n100_acc: 0.46
    new_combined_n100_correct: 46
    batch2_acc: 0.48
    batch2_correct: 24
- exp_id: acc_qw_s015_b1_8k
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.46
    correct: 23
    total: 50
    truncation_rate_8k: 0.02
    gen_over_2k: 3
    gen_over_2k_all_wrong: true
    max_gen_length: 8192
    mean_gen_length: 776
    batch: b1_v2 (problems 1-50, 8k tokens)
    batch2_acc: 0.38
    batch2_correct: 19
    new_combined_n100_acc: 0.42
    new_combined_n100_correct: 42
    batch2_source: acc_qw_s015_n100
- exp_id: acc_qw_s020_b1_8k
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.26
    correct: 13
    n_problems: 50
    truncation_rate: 0.02
    truncated_count: 1
    avg_tokens: 722.1
    max_tokens_generated: 8192
    max_new_tokens: 8192
    total_time_seconds: 729.1
    null_count: 0
    batch: b1_v2 (problems 1-50, 8k tokens)
    old_batch1_acc: 0.26
    old_batch1_correct: 13
    new_combined_n100_acc: 0.36
    new_combined_n100_correct: 36
    batch2_acc: 0.46
    batch2_correct: 23
- exp_id: acc_qw_s025_b1_8k
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    accuracy: 0.32
    correct: 16
    n_problems: 50
    truncation_rate: 0.04
    truncated_count: 2
    extraction_failures: 6
    avg_tokens: 797.3
    total_time_seconds: 831.6
    batch: b1_v2 (problems 1-50, 8k tokens)
    batch2_acc: 0.34
    batch2_correct: 17
    new_combined_n100_acc: 0.33
    new_combined_n100_correct: 33
    batch2_source: acc_qw_s025_n100_b2_fix
- exp_id: acc_qw_s030_b1_8k
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    accuracy: 0.14
    correct: 7
    total: 50
    truncation_rate: 0.04
    truncated_count: 2
    extraction_failures: 8
    max_new_tokens: 8192
    total_time_seconds: 886.7
    batch: b1_v2 (problems 1-50, 8k tokens)
    old_batch1_acc: 0.14
    old_batch1_correct: 7
    batch2_acc: 0.24
    batch2_correct: 12
    new_combined_n100_acc: 0.19
    new_combined_n100_correct: 19
- exp_id: c8_llama_n250
  name: ''
  status: DONE
  conclusion: failed
  metrics:
    first_run_failed: true
    failure_reason: 'bash wrapper wait logic bug: subprocess OOM/error exits silently,
      script marks DONE without output validation. All 8 output dirs empty.'
    fix_worker: worker_code_c8_llama_n250_fix_20260516T031229
    fix_plan: 1) diagnose script + OOM, 2) fix exit code + output validation + GPU
      monitor, 3) dry-run 1 condition on GPU 2, 4) full launch on GPU 2-3 via submit_training_job
- exp_id: c4_think_validation_math500
  name: ''
  status: DONE
  conclusion: success
  metrics:
    v2_math500_kappa_adaptive: 0.88
    v2_math500_ds_problems: 48
    v2_math500_ds_tokens: 32055
    v2_math500_thinking_in_low: 0.816
    v2_math500_answer_in_high: 0.655
    v2_math500_temporal_ordering_ds: 0.576
    v2_math500_temporal_ordering_qw: 0.479
    v2_qw_pct_positive: 0.98
    v2_scope: MATH-500
    v2_models: DS+QW
    v2_status: ALL_CRITERIA_MET
    v1_kappa_adaptive: 0.8804
    v1_auc: 0.9808
    SCOPE_FLAG: v2_validated_on_MATH500
- exp_id: c5_per_phase_gini
  name: ''
  status: DONE
  conclusion: success
  metrics:
    qw_complete: true
    ds_complete: true
    n_problems: 30
    qw_dense_gini_baselines:
      low: 0.2675
      mid: 0.2078
      high: 0.2599
    qw_importance:
      s015:
        global_delta: -0.0103
        low_delta: -0.0165
        mid_delta: -0.0094
        high_delta: -0.012
      s020:
        global_delta: -0.0121
        low_delta: -0.02
        mid_delta: -0.0115
        high_delta: -0.0143
      s025:
        global_delta: -0.01
        low_delta: -0.0286
        mid_delta: -0.0168
        high_delta: -0.0207
      s030:
        global_delta: -0.0202
        low_delta: -0.035
        mid_delta: -0.0183
        high_delta: -0.0239
    qw_random:
      s015:
        global_delta: -0.0186
        low_delta: -0.0083
        mid_delta: -0.0038
        high_delta: -0.0036
      s020:
        global_delta: -0.0229
        low_delta: -0.0119
        mid_delta: -0.0053
        high_delta: -0.0067
      s025:
        global_delta: -0.0337
        low_delta: -0.0014
        mid_delta: -0.0081
        high_delta: 0.0045
      s030:
        global_delta: -0.0447
        low_delta: -0.0221
        mid_delta: -0.0077
        high_delta: -0.0061
    ds_importance:
      s015:
        global_delta: -0.0301
        low_delta: -0.0163
        mid_delta: -0.0073
        high_delta: -0.0152
      s020:
        global_delta: -0.0404
        low_delta: -0.0209
        mid_delta: -0.0092
        high_delta: -0.02
      s025:
        global_delta: -0.0647
        low_delta: -0.0313
        mid_delta: -0.0133
        high_delta: -0.0267
      s030:
        global_delta: -0.0806
        low_delta: -0.0373
        mid_delta: -0.0183
        high_delta: -0.0314
    ds_random:
      s015:
        global_delta: -0.0309
        low_delta: -0.0102
        mid_delta: -0.0006
        high_delta: -0.0062
      s020:
        global_delta: -0.0403
        low_delta: -0.012
        mid_delta: -0.0007
        high_delta: -0.0085
      s025:
        global_delta: -0.062
        low_delta: -0.015
        mid_delta: -0.0096
        high_delta: -0.0112
      s030:
        global_delta: -0.0732
        low_delta: -0.0183
        mid_delta: -0.0093
        high_delta: -0.0138
    key_finding: 'Both models: importance pruning low-phase Gini delta consistently
      largest and monotonically increases with sparsity (DS: -0.016 to -0.037; QW:
      -0.017 to -0.035). Random pruning shows weaker per-phase structure. Supports
      discrimination collapse hypothesis.'
- exp_id: c9_gsm8k_power_analysis
  name: ''
  status: DONE
  conclusion: success
  metrics:
    min_detectable_d_n50: 0.4042
    random_conditions_all_NS: true
    random_max_abs_d: 0.164
    random_conditions:
      ds_rand_s015_d: -0.017
      ds_rand_s015_power: 0.052
      ds_rand_s020_d: -0.063
      ds_rand_s020_power: 0.072
      ds_rand_s025_d: 0.026
      ds_rand_s025_power: 0.054
      ds_rand_s030_d: 0.058
      ds_rand_s030_power: 0.069
      qw_rand_s015_d: -0.154
      qw_rand_s015_power: 0.187
      qw_rand_s020_d: 0.113
      qw_rand_s020_power: 0.123
      qw_rand_s025_d: 0.163
      qw_rand_s025_power: 0.203
      qw_rand_s030_d: 0.165
      qw_rand_s030_power: 0.207
    qw_importance_adequately_powered:
      s025_d: 0.62
      s025_power: 0.99
      s030_d: 0.64
      s030_power: 0.99
    REVIEWER_WARNING: t-test Cohen's d power analysis ONLY valid for random conditions.
      Importance conditions have heavy-tail distributions where t-test severely misestimates
      (e.g. DS s030 d=0.008 but Wilcoxon p=0.0001). DO NOT cite importance t-test
      power in paper.
    paper_citable_conclusions:
    - 'Random: all 8 conditions NS (max|d|=0.164), n=50 detects d>=0.40 → absence
      of evidence not evidence of absence'
    - QW importance s025/s030 adequately powered (d≈0.63, power>0.99)
- exp_id: c10_lang_switching
  name: ''
  status: DONE
  conclusion: success
  metrics:
    method: CPU analysis of existing gen_snippet data (3/5 sparsities)
    coverage: dense, s015, s030 (s020/s025 missing gen_snippet)
    n_per_sparsity: 50
    dense:
      switch_rate: 0
      cn_count: 0
      en_count: 50
      cn_acc: null
      en_acc: 0.52
    s015:
      switch_rate: 0.04
      cn_count: 2
      en_count: 48
      cn_acc: 0
      en_acc: 0.375
    s030:
      switch_rate: 0.4
      cn_count: 20
      en_count: 30
      cn_acc: 0.1
      en_acc: 0.1
    trend: 'Monotonically increasing: 0% → 4% → 40%. Chinese responses have much lower
      accuracy (10% at s030 vs 52% dense English).'
    checkpoint_path: /root/autodl-tmp/pacs/results_c10_lang_cpu.json
- exp_id: c8_llama_n250_fixed
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n_problems: 250
    model: DeepSeek-R1-Distill-Llama-8B
    conditions_completed: 8/8
    importance:
      s015:
        median_gradient: 0.050099
        ci:
        - 0.045477
        - 0.058804
        wilcoxon_p: 1.44e-29
        cohens_dz: 0.814
        monotonic: true
      s020:
        median_gradient: 0.158708
        ci:
        - 0.141193
        - 0.181937
        wilcoxon_p: 8.94e-35
        cohens_dz: 1.01
        monotonic: true
      s025:
        median_gradient: 0.376131
        ci:
        - 0.315704
        - 0.402861
        wilcoxon_p: 4.3e-39
        cohens_dz: 1.1151
        monotonic: true
      s030:
        median_gradient: 0.695435
        ci:
        - 0.639426
        - 0.770102
        wilcoxon_p: 1.48e-40
        cohens_dz: 1.15
        monotonic: true
    random:
      s015:
        median_gradient: 0.025489
        ci:
        - 0.019942
        - 0.033342
        wilcoxon_p: 9.28e-13
        cohens_dz: 0.4359
        monotonic: true
      s020:
        median_gradient: 0.065003
        ci:
        - 0.052258
        - 0.088191
        wilcoxon_p: 3.63e-15
        cohens_dz: 0.4588
        monotonic: true
      s025:
        median_gradient: 0.184201
        ci:
        - 0.112738
        - 0.247119
        wilcoxon_p: 3.75e-13
        cohens_dz: 0.4239
        monotonic: true
      s030:
        median_gradient: 0.270653
        ci:
        - 0.193489
        - 0.368089
        wilcoxon_p: 6.0e-12
        cohens_dz: 0.4104
        monotonic: true
    dose_response_monotonic: true
    imp_rand_ratio_range: 1.97-2.57x
    all_conditions_significant: true
    importance_effect_size_range: 0.81-1.15 (large)
    random_effect_size_range: 0.41-0.46 (medium)
- exp_id: c10-lang-s020-s025
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: c10_lang_s020_s025
  name: ''
  status: DONE
  conclusion: success
  metrics:
    s020:
      n: 50
      accuracy: 0.26
      switch_rate: 0.14
      switch_count: 7
      mean_cn_ratio: 0.066
      cn_acc: 0.333
      en_acc: 0.25
    s025:
      n: 50
      accuracy: 0.1
      switch_rate: 0.32
      switch_count: 16
      mean_cn_ratio: 0.152
      cn_acc: 0.2
      en_acc: 0.057
    wall_time_s: 11680.6
    output_path: /root/autodl-tmp/pacs/results_c10_lang_s020_s025.json
- exp_id: c8_llama_gpu0_s025
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n_problems: 250
    n_bootstrap: 1000
    segmentation: quantile
    per_phase_ii_median:
      high: 0.0171
      mid: 0.1916
      low: 0.388
    per_phase_ii_mean:
      high: 0.0218
      mid: 0.2126
      low: 0.4713
    phase_gradient_median_diff: 0.3761
    phase_gradient_median_diff_ci95:
    - 0.3147
    - 0.4039
    wilcoxon_p_one_sided: 4.3e-39
    bonferroni_p_k4: 1.72e-38
    cohens_dz: 1.1174
    rank_biserial_r: 0.8689
    n_paired: 244
    pos_neg_ratio: 228/16
- exp_id: gpqa_ds_importance_s015
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n_problems: 198
    interaction_index:
      high:
        mean: 0.191363
        median: 0.012758
        ci:
        - 0.047972
        - 0.514786
        median_ci:
        - 0.011463
        - 0.013936
        winsorized_mean: 0.039667
        skewness: 77
      mid:
        mean: 0.87787
        median: 0.102412
        ci:
        - 0.72315
        - 1.039118
        median_ci:
        - 0.092683
        - 0.115074
        winsorized_mean: 0.532911
        skewness: 7.7
      low:
        mean: 5.991797
        median: 0.960161
        ci:
        - 5.235965
        - 6.732278
        median_ci:
        - 0.892882
        - 1.03306
        winsorized_mean: 3.945337
        skewness: 8.88
    perplexity:
      high:
        dense: 1.1777
        attn: 1.5205
        kv: 1.702
        both: 2.2531
      mid:
        dense: 1.3075
        attn: 1.6733
        kv: 3.2369
        both: 4.7222
      low:
        dense: 1.4216
        attn: 1.9771
        kv: 19.3067
        both: 27.6495
    phase_stats:
      high:
        n_tokens: 479658
        n_segments: 6261
      mid:
        n_tokens: 276409
        n_segments: 2185
      low:
        n_tokens: 465085
        n_segments: 5128
    pass_fail:
      ci_overlap: true
      sign_reversal: false
      overall: PASS
    gradient_direction: low > mid > high
    median_ratio_low_high: 75.2
- exp_id: gpqa_ds_importance_s020
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: recency_s025
  name: ''
  status: DONE
  conclusion: success
  metrics:
    phase_gradient:
      median_diff: 1.1186
      cohens_dz: 0.2205
      p_value: 0.00922
      significant: true
      direction: reversed (low_sparsity more damaged)
    comparison_importance_s025:
      importance_median_diff: -1.0745
      importance_cohens_dz: -0.7778
      importance_p_value: 1.06e-68
      gradient_directions_opposite: true
      importance_effect_3.5x_stronger: true
    comparison_random_s025:
      random_median_diff: -0.3931
      random_cohens_dz: -0.0172
      random_p_value: 1.59e-11
    interaction_index:
      high_sparsity_median: -0.000346
      mid_sparsity_median: -0.02246
      low_sparsity_median: -0.091106
    config:
      model: DeepSeek-R1-Distill-Qwen-7B
      masking_method: recency
      sparsity: 0.25
      n_problems: 100
      seed: 42
- exp_id: recency_s030
  name: ''
  status: DONE
  conclusion: success
  metrics:
    phase_gradient:
      median_diff: -1982.57
      ci_low: -9391.77
      ci_high: 882.08
      cohens_dz: -0.096
      p_value: 0.114
      significant: false
      effect_size: negligible
    comparison_importance_s030:
      median_diff: 8.48
      cohens_dz: 0.33
      p_value: 1.09e-79
      significant: true
    comparison_random_s030:
      median_diff: 0.51
      cohens_dz: -0.049
      p_value: 0.00148
      significant: true
    interaction_index:
      high_sparsity_median: -0.0018
      mid_sparsity_median: -0.016
      low_sparsity_median: 0.1099
    n_problems: 100
    model: DeepSeek-R1-Distill-Qwen-7B
    masking_method: recency
    sparsity: 0.3
- exp_id: recency_s015
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n_problems: 100
    model: DeepSeek-R1-Distill-Qwen-7B
    masking_method: recency
    sparsity: 0.15
    phase_gradient:
      median_diff: -0.0026
      cohens_dz: 0.083
      p_value: 0.77
      significant: false
    comparison_importance_s015:
      median_diff: 0.39
      cohens_dz: 0.574
      p_value: < 1e-70
      significant: true
    comparison_random_s015:
      median_diff: 0.014
      cohens_dz: -0.045
      p_value: 0.86
      significant: false
    interpretation: Recency eviction shows NO phase gradient (NS, negligible effect),
      confirming phase-dependent severity is attention-score-specific
- exp_id: gpqa_ds_importance_s025
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: gpqa_ds_importance_s030
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: gpqa_ds_random_s020
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}

# 输出格式（YAML，仅输出一个 ```yaml 块）

```yaml
tier: worst
narrative_guidance: "..."
imagined_experiments:
  - name: "..."
    plan_id: "..."
    description: "..."
    expected_results: {metric: value, ...}
    result_rationale: "..."
    tables: []
    figures_description: []
    analysis: "..."
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "ce667af9-41a5-4bed-8a5c-6707db53531e",
  "type": "user",
  "uuid": "a0e6638a-d238-4fee-ace5-c49e48f5e7e3",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "5ce792ab-ebc9-4b52-8f9c-3b1fb1b17c1f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-17T01:44:08.744Z_

```json
{
  "parentUuid": "a0e6638a-d238-4fee-ace5-c49e48f5e7e3",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "17c784b0-ed8e-4694-a571-54301d88ee3f",
  "timestamp": "2026-05-17T01:44:08.744Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "5ce792ab-ebc9-4b52-8f9c-3b1fb1b17c1f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-17T01:44:08.744Z_

```json
{
  "parentUuid": "17c784b0-ed8e-4694-a571-54301d88ee3f",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "ff0d8d98-aa3e-4abb-8221-438979079c79",
  "timestamp": "2026-05-17T01:44:08.744Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "5ce792ab-ebc9-4b52-8f9c-3b1fb1b17c1f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：GPQA random 也显示强 gradient（ratio ≈ 1×）+ 审稿人认为现象是 trivial（token removal 的必然后果而非 scoring-specific）+ 需要完全 reframe 核心 claim 核心假设：['GPQA importance gradient 存在但…",
  "leafUuid": "ff0d8d98-aa3e-4abb-8221-438979079c79",
  "sessionId": "5ce792ab-ebc9-4b52-8f9c-3b1fb1b17c1f"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Phase-gated compound sparsity in worst-case scenario",
  "sessionId": "5ce792ab-ebc9-4b52-8f9c-3b1fb1b17c1f"
}
```

---

### Assistant

_source line 8 · 2026-05-17T01:45:25.233Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted experimental results for the "worst" tier scenario for each experiment in the experiment_plan that has a "planned" status. Let me look through the experiment_plan to find experiments with status "planned" or currently "RUNNING".

Looking at the experiment_plan and registry, I can see the following experiments that are currently RUNNING (not yet completed):
- gpqa_ds_importance_s020
- gpqa_ds_importance_s025
- gpqa_ds_importance_s030
- gpqa_ds_random_s020

And from the claims table, C9 (Differentiation from Lethe/SparK prior work) is "planned".


Let me re-examine the request more carefully. The user is asking for "planned" experiments specifically, so I need to distinguish between RUNNING and PLANNED statuses. Looking at the registry again, I should identify which experiments have a "planned" status rather than "RUNNING" or "DONE". The GPQA experiments currently running in the registry are the ones the user wants predictions for—specifically the importance-based variants at different sample sizes and the random baseline. The critical metric to watch is the median gradient at s030, since if the random variant shows similarly strong gradients, reviewers might dismiss the phenomenon as trivial, which would require a complete reframing of the findings. Looking at the GPQA experiments currently running, I need to predict outcomes for the importance variants at different sparsity levels and the random variant at s020, then identify what other random experiments should exist to complete the matrix. Under the worst-case scenario where random experiments show similarly strong phase gradients as the completed importance baseline, the importance-to-random ratio would collapse toward 1×, fundamentally challenging the narrative that phase interactions are importance-specific rather than universal phenomena tied to eviction discriminativeness. These might be planned but not yet started.

Let me construct the predictions for the "worst" tier. I need to think about what each experiment would show in this scenario.

For the "worst" tier on GPQA:
- Importance still shows phase gradient (that's established), but the gradient magnitude on GPQA is in the range [1.5, 4.0] for s030
- Random ALSO shows strong gradient, with imp/rand ratio only 1.0-2.0×
- This mirrors the LLaMA pattern where imp/rand ratio was only 2.0-2.6×

Let me construct detailed predictions:

**gpqa_ds_importance_s020:**
- We have s015 data: median gradient = 0.947 (low median - high median)
- For s020 under worst tier, the gradient should be moderate, maybe 1.2-1.8
- Following the dose-response pattern from MATH-500 (s015→s020 ratio ≈ 3×), but GPQA might scale differently

Now I'm examining the s015 GPQA data more carefully. The gradient is defined as the median difference between low and high conditions, which gives 0.947. Since the worst tier predicts s030 gradients in the [1.5, 4.0] range, and s015 is already at 0.947, I need to figure out how this scales across the sequence.

The dose-response on GPQA is much flatter than MATH-500—going from ~0.95 at s015 to ~2.5 at s030 is only a 2.6× increase, compared to MATH-500's 21.7× jump. This flattening makes sense given that longer reasoning chains on GPQA reduce the specificity of the phenomenon. For the random gradient under worst tier, the ratio stays low at 1-2×, which aligns with what I saw in the LLaMA results.

Looking at the experiment registry, I can see several importance-based runs are already executing across s020, s025, and s030, along with a random s020 run. There are likely planned but not yet started runs for the remaining random sparsity levels, though I should focus on what's actually documented rather than speculating about the full experiment plan. Now I'm working through the specific predictions for each RUNNING experiment under the worst-case tier scenario, starting with the GPQA importance sampling variants and estimating their gradient values based on the s015 baseline and expected dose-response patterns for longer reasoning tasks. Looking at the remaining random experiments, the gradient patterns hold consistent—random_s015 shows about 1.6× the ratio, random_s025 around 1.7×, and random_s030 closer to 1.5×, all staying within that [1.0, 2.0] worst-tier range. But I'm realizing I need to clarify what the user is actually asking for: are they wanting me to detail only the experiments that haven't been run yet, or should I be predicting results for all planned experiments under the worst-tier scenario?

Given the context of this exercise, I think they're asking for predictions on the GPQA experiments that are still in progress. Let me focus on those and generate the YAML output with my rationale for each prediction.

For the "worst" tier predictions, I'm noticing that GPQA's importance gradient is weaker than MATH-500 because the multi-domain reasoning chains are longer and more heterogeneous, which makes the perplexity-based phase segmentation noisier and dilutes the concentration effect. Meanwhile, GPQA's random eviction shows a strong gradient because the reasoning chains are so tightly coupled that any token removal in the dense reasoning phases disrupts the multi-hop dependencies, regardless of whether it's importance-weighted or random.

The recency null result makes more sense now under this interpretation: recency isn't proving scoring-independence, but rather that it's just a weak eviction method for sequential reasoning tasks since it preserves temporal locality. And I'm checking the experiment registry to see which GPQA importance sparsity runs are actually running versus planned.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff0d8d98-aa3e-4abb-8221-438979079c79",
  "isSidechain": false,
  "requestId": "req_011Cb7J1K1TwtWz9t4Rc8eFg",
  "type": "assistant",
  "uuid": "321ba4fd-44c4-43b2-89ef-5a699f07770b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "5ce792ab-ebc9-4b52-8f9c-3b1fb1b17c1f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XffRefFxXTMAbTWWnjBuyc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 59176,
      "cache_read_input_tokens": 11841,
      "output_tokens": 3852,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 59176,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3852,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 59176,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 59176
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-17T01:45:25.906Z_

Looking at the registry, the RUNNING/planned experiments are the GPQA series. Let me generate worst-tier predictions for each.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "321ba4fd-44c4-43b2-89ef-5a699f07770b",
  "isSidechain": false,
  "requestId": "req_011Cb7J1K1TwtWz9t4Rc8eFg",
  "type": "assistant",
  "uuid": "3fdf8a68-e7bc-4b93-8400-2e9fe5822f2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "5ce792ab-ebc9-4b52-8f9c-3b1fb1b17c1f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XffRefFxXTMAbTWWnjBuyc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 59176,
      "cache_read_input_tokens": 11841,
      "output_tokens": 3852,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 59176,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3852,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 59176,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 59176
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-17T01:45:27.848Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01PmJuRSGJXC8GpsBdgqzMuU`</summary>

```json
{
  "pattern": "gpqa.*plan|GPQA.*experiment",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3fdf8a68-e7bc-4b93-8400-2e9fe5822f2b",
  "isSidechain": false,
  "requestId": "req_011Cb7J1K1TwtWz9t4Rc8eFg",
  "type": "assistant",
  "uuid": "5516ba7a-97b6-48cc-a17e-a182179ce551",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "5ce792ab-ebc9-4b52-8f9c-3b1fb1b17c1f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XffRefFxXTMAbTWWnjBuyc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 59176,
      "cache_read_input_tokens": 11841,
      "output_tokens": 3852,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 59176,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3852,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 59176,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 59176
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-17T01:45:28.107Z_

<details><summary>↩ Tool result · `toolu_01PmJuRSGJXC8GpsBdgqzMuU`</summary>

```text
Found 84 files
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260517T013445/logs/phase2_worst_attempt0.log
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260517T013445/logs/phase2_median_attempt0.log
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260517T013445/logs/phase2_best_attempt0.log
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260517T013445/logs/phase1_attempt0.log
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260517T012753/logs/phase2_median_attempt0.log
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260517T012753/logs/phase2_best_attempt0.log
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260517T005655/logs/review_median.log
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260517T005655/logs/review_best.log
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260517T005655/logs/paper_agent_worst.log
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260517T005655/worst/paper.tex
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260517T005655/logs/paper_agent_median.log
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260517T005655/logs/paper_agent_best.log
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260517T005655/logs/phase2_worst_attempt0.log
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260517T005655/logs/phase2_median_attempt0.log
projects/phase-gated-compound-sparse/logs/chats/feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4.jsonl
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260517T005655/logs/phase2_best_attempt0.log
projects/phase-gated-compound-sparse/logs/chats/feishu_group_oc_fdc656be1c7fe17c11ab639cdbce3710_director.jsonl
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260517T005655/logs/phase1_attempt0.log
projects/phase-gated-compound-sparse/logs/chats/cron_hook_recency_s030.jsonl
projects/phase-gated-compound-sparse/logs/chats/feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4_paper_agent.jsonl
projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex
projects/phase-gated-compound-sparse/logs/workers/worker_paper_limitations_update_20260516T232234.log
projects/phase-gated-compound-sparse/logs/workers/worker_paper_bib_new_refs_20260516T232247.log
projects/phase-gated-compound-sparse/logs/workers/worker_paper_recency_section_draft_20260516T231521.log
projects/phase-gated-compound-sparse/logs/workers/worker_analysis_recency_analysis_prep_20260516T230743.log
projects/phase-gated-compound-sparse/logs/chats/worker_paper_tex_consistency_fixes_20260516T224936.jsonl
projects/phase-gated-compound-sparse/logs/workers/worker_paper_tex_consistency_fixes_20260516T224936.log
projects/phase-gated-compound-sparse/logs/workers/worker_paper_post_llama_consistency_check_20260516T224223.log
projects/phase-gated-compound-sparse/logs/workers/worker_paper_c8_llama_results_integration_20260516T220519.log
projects/phase-gated-compound-sparse/logs/chats/cron_hook_c8_llama_n250_fixed.jsonl
projects/phase-gated-compound-sparse/logs/workers/worker_analysis_c8_llama_n250_fixed_20260516T214849.log
projects/phase-gated-compound-sparse/logs/workers/worker_code_recency_s015_submit_20260516T201238.log
projects/phase-gated-compound-sparse/logs/chats/cron_hook_gpqa_ds_importance_s015.jsonl
projects/phase-gated-compound-sparse/logs/workers/worker_analysis_gpqa_ds_importance_s015_20260516T201020.log
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T164305/logs/review_worst.log
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T164305/logs/review_median.log
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T164305/logs/review_best.log
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T164305/logs/paper_agent_worst.log
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T164305/logs/paper_agent_median.log
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T164305/logs/paper_agent_best.log
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T164305/logs/phase2_worst_attempt1.log
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T164305/logs/phase2_worst_attempt0.log
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T164305/logs/phase2_median_attempt0.log
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T164305/logs/phase2_best_attempt0.log
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T164305/logs/phase1_attempt0.log
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/meta.yaml
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/logs/review_worst.log
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/worst/review_report.md
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/logs/review_median.log
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/median/review_report.md
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/logs/review_best.log
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/best/review_report.md
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/logs/paper_agent_worst.log
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/worst/paper.tex
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/worst/experiment_data.json
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/logs/paper_agent_median.log
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/logs/paper_agent_best.log
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/best/paper.tex
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/logs/phase2_worst_attempt0.log
projects/phase-gated-compound-sparse/logs/workers/worker_ops_gpqa_prep_remaining_20260516T152422.log
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/logs/phase2_median_attempt0.log
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/logs/phase2_best_attempt0.log
projects/phase-gated-compound-sparse/logs/workers/worker_ssh_c8_llama_n250_progress_check_20260516T150558.log
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/logs/phase1_attempt0.log
projects/phase-gated-compound-sparse/logs/workers/worker_ops_gpu_full_status_20260516T140155.log
projects/phase-gated-compound-sparse/logs/chats/archive/feishu_group_oc_fdc656be1c7fe17c11ab639cdbce3710_director_20260516T140226_790641.jsonl
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/logs/review_worst.log
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/worst/review_report.md
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/logs/review_median.log
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/logs/review_best.log
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/logs/paper_agent_worst.log
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/worst/paper.tex
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/logs/paper_agent_median.log
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/logs/paper_agent_best.log
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/logs/phase2_worst_attempt0.log
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/logs/phase2_median_attempt0.log
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/logs/phase2_best_attempt0.log
projects/phase-gated-compound-sparse/logs/workers/worker_ops_c10_lang_investigate_20260516T073734.log
projects/phase-gated-compound-sparse/logs/chats/worker_code_gpqa_pipeline_prep_20260516T044908.jsonl
projects/phase-gated-compound-sparse/logs/chats/feishu_group_oc_57b24a804b56707ec9118a483a8ac65e_director.jsonl
projects/phase-gated-compound-sparse/logs/chats/feishu_group_oc_57b24a804b56707ec9118a483a8ac65e_reviewer_1.jsonl
projects/phase-gated-compound-sparse/logs/chats/feishu_group_oc_57b24a804b56707ec9118a483a8ac65e_reviewer_2.jsonl
projects/phase-gated-compound-sparse/logs/chats/archive/feishu_group_oc_fdc656be1c7fe17c11ab639cdbce3710_director_20260515T164851_320015.jsonl
projects/phase-gated-compound-sparse/logs/workers/worker_research_m2_m4_code_readiness_20260513T195814.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5516ba7a-97b6-48cc-a17e-a182179ce551",
  "isSidechain": false,
  "promptId": "ce667af9-41a5-4bed-8a5c-6707db53531e",
  "type": "user",
  "uuid": "b7787eba-42ca-4ba1-8cfc-1ccaaebe5f9a",
  "toolUseResult": {
    "mode": "files_with_matches",
    "filenames": [
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260517T013445/logs/phase2_worst_attempt0.log",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260517T013445/logs/phase2_median_attempt0.log",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260517T013445/logs/phase2_best_attempt0.log",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260517T013445/logs/phase1_attempt0.log",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260517T012753/logs/phase2_median_attempt0.log",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260517T012753/logs/phase2_best_attempt0.log",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260517T005655/logs/review_median.log",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260517T005655/logs/review_best.log",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260517T005655/logs/paper_agent_worst.log",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260517T005655/worst/paper.tex",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260517T005655/logs/paper_agent_median.log",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260517T005655/logs/paper_agent_best.log",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260517T005655/logs/phase2_worst_attempt0.log",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260517T005655/logs/phase2_median_attempt0.log",
      "projects/phase-gated-compound-sparse/logs/chats/feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4.jsonl",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260517T005655/logs/phase2_best_attempt0.log",
      "projects/phase-gated-compound-sparse/logs/chats/feishu_group_oc_fdc656be1c7fe17c11ab639cdbce3710_director.jsonl",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260517T005655/logs/phase1_attempt0.log",
      "projects/phase-gated-compound-sparse/logs/chats/cron_hook_recency_s030.jsonl",
      "projects/phase-gated-compound-sparse/logs/chats/feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4_paper_agent.jsonl",
      "projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex",
      "projects/phase-gated-compound-sparse/logs/workers/worker_paper_limitations_update_20260516T232234.log",
      "projects/phase-gated-compound-sparse/logs/workers/worker_paper_bib_new_refs_20260516T232247.log",
      "projects/phase-gated-compound-sparse/logs/workers/worker_paper_recency_section_draft_20260516T231521.log",
      "projects/phase-gated-compound-sparse/logs/workers/worker_analysis_recency_analysis_prep_20260516T230743.log",
      "projects/phase-gated-compound-sparse/logs/chats/worker_paper_tex_consistency_fixes_20260516T224936.jsonl",
      "projects/phase-gated-compound-sparse/logs/workers/worker_paper_tex_consistency_fixes_20260516T224936.log",
      "projects/phase-gated-compound-sparse/logs/workers/worker_paper_post_llama_consistency_check_20260516T224223.log",
      "projects/phase-gated-compound-sparse/logs/workers/worker_paper_c8_llama_results_integration_20260516T220519.log",
      "projects/phase-gated-compound-sparse/logs/chats/cron_hook_c8_llama_n250_fixed.jsonl",
      "projects/phase-gated-compound-sparse/logs/workers/worker_analysis_c8_llama_n250_fixed_20260516T214849.log",
      "projects/phase-gated-compound-sparse/logs/workers/worker_code_recency_s015_submit_20260516T201238.log",
      "projects/phase-gated-compound-sparse/logs/chats/cron_hook_gpqa_ds_importance_s015.jsonl",
      "projects/phase-gated-compound-sparse/logs/workers/worker_analysis_gpqa_ds_importance_s015_20260516T201020.log",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T164305/logs/review_worst.log",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T164305/logs/review_median.log",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T164305/logs/review_best.log",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T164305/logs/paper_agent_worst.log",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T164305/logs/paper_agent_median.log",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T164305/logs/paper_agent_best.log",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T164305/logs/phase2_worst_attempt1.log",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T164305/logs/phase2_worst_attempt0.log",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T164305/logs/phase2_median_attempt0.log",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T164305/logs/phase2_best_attempt0.log",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T164305/logs/phase1_attempt0.log",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/meta.yaml",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/logs/review_worst.log",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/worst/review_report.md",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/logs/review_median.log",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/median/review_report.md",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/logs/review_best.log",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/best/review_report.md",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/logs/paper_agent_worst.log",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/worst/paper.tex",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/worst/experiment_data.json",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/logs/paper_agent_median.log",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/logs/paper_agent_best.log",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/best/paper.tex",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/logs/phase2_worst_attempt0.log",
      "projects/phase-gated-compound-sparse/logs/workers/worker_ops_gpqa_prep_remaining_20260516T152422.log",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/logs/phase2_median_attempt0.log",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/logs/phase2_best_attempt0.log",
      "projects/phase-gated-compound-sparse/logs/workers/worker_ssh_c8_llama_n250_progress_check_20260516T150558.log",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/logs/phase1_attempt0.log",
      "projects/phase-gated-compound-sparse/logs/workers/worker_ops_gpu_full_status_20260516T140155.log",
      "projects/phase-gated-compound-sparse/logs/chats/archive/feishu_group_oc_fdc656be1c7fe17c11ab639cdbce3710_director_20260516T140226_790641.jsonl",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/logs/review_worst.log",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/worst/review_report.md",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/logs/review_median.log",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/logs/review_best.log",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/logs/paper_agent_worst.log",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/worst/paper.tex",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/logs/paper_agent_median.log",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/logs/paper_agent_best.log",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/logs/phase2_worst_attempt0.log",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/logs/phase2_median_attempt0.log",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/logs/phase2_best_attempt0.log",
      "projects/phase-gated-compound-sparse/logs/workers/worker_ops_c10_lang_investigate_20260516T073734.log",
      "projects/phase-gated-compound-sparse/logs/chats/worker_code_gpqa_pipeline_prep_20260516T044908.jsonl",
      "projects/phase-gated-compound-sparse/logs/chats/feishu_group_oc_57b24a804b56707ec9118a483a8ac65e_director.jsonl",
      "projects/phase-gated-compound-sparse/logs/chats/feishu_group_oc_57b24a804b56707ec9118a483a8ac65e_reviewer_1.jsonl",
      "projects/phase-gated-compound-sparse/logs/chats/feishu_group_oc_57b24a804b56707ec9118a483a8ac65e_reviewer_2.jsonl",
      "projects/phase-gated-compound-sparse/logs/chats/archive/feishu_group_oc_fdc656be1c7fe17c11ab639cdbce3710_director_20260515T164851_320015.jsonl",
      "projects/phase-gated-compound-sparse/logs/workers/worker_research_m2_m4_code_readiness_20260513T195814.log"
    ],
    "numFiles": 84
  },
  "sourceToolAssistantUUID": "5516ba7a-97b6-48cc-a17e-a182179ce551",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "5ce792ab-ebc9-4b52-8f9c-3b1fb1b17c1f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-17T01:45:28.416Z_

<details open><summary>🔧 Tool call — Glob · `toolu_014WfrRhcW1pXyt7wmK9rW1H`</summary>

```json
{
  "pattern": "**/gpqa*plan*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7787eba-42ca-4ba1-8cfc-1ccaaebe5f9a",
  "isSidechain": false,
  "requestId": "req_011Cb7J1K1TwtWz9t4Rc8eFg",
  "type": "assistant",
  "uuid": "4289468b-86c0-425b-8d61-18c35671d72e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "5ce792ab-ebc9-4b52-8f9c-3b1fb1b17c1f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XffRefFxXTMAbTWWnjBuyc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 59176,
      "cache_read_input_tokens": 11841,
      "output_tokens": 3852,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 59176,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3852,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 59176,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 59176
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-17T01:45:28.439Z_

<details><summary>↩ Tool result · `toolu_014WfrRhcW1pXyt7wmK9rW1H`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4289468b-86c0-425b-8d61-18c35671d72e",
  "isSidechain": false,
  "promptId": "ce667af9-41a5-4bed-8a5c-6707db53531e",
  "type": "user",
  "uuid": "648255a4-2f4b-4ccd-9f39-e999feb8b29a",
  "toolUseResult": {
    "filenames": [],
    "durationMs": 15,
    "numFiles": 0,
    "truncated": false
  },
  "sourceToolAssistantUUID": "4289468b-86c0-425b-8d61-18c35671d72e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "5ce792ab-ebc9-4b52-8f9c-3b1fb1b17c1f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 14_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：GPQA random 也显示强 gradient（ratio ≈ 1×）+ 审稿人认为现象是 trivial（token removal 的必然后果而非 scoring-specific）+ 需要完全 reframe 核心 claim 核心假设：['GPQA importance gradient 存在但…",
  "leafUuid": "648255a4-2f4b-4ccd-9f39-e999feb8b29a",
  "sessionId": "5ce792ab-ebc9-4b52-8f9c-3b1fb1b17c1f"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Phase-gated compound sparsity in worst-case scenario",
  "sessionId": "5ce792ab-ebc9-4b52-8f9c-3b1fb1b17c1f"
}
```

---

### Tool call

_source line 16 · 2026-05-17T01:45:34.635Z_

<details open><summary>🔧 Tool call — Agent · `toolu_013iYygKzWbo9qDDas4McnRz`</summary>

```json
{
  "description": "Find GPQA experiment plan",
  "subagent_type": "Explore",
  "prompt": "In the project at /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/, find the GPQA experiment plan or any file that lists what GPQA experiments are planned (beyond gpqa_ds_importance_s015 which is already done). Look for files that define the full set of GPQA experiments including random conditions. Check:\n1. Any experiment plan files mentioning GPQA\n2. The worker log for gpqa prep: worker_ops_gpqa_prep_remaining_20260516T152422.log\n3. Any decision log entries about GPQA\n\nSearch breadth: medium"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "648255a4-2f4b-4ccd-9f39-e999feb8b29a",
  "isSidechain": false,
  "requestId": "req_011Cb7J7Be7kHq3upKLKtJQv",
  "type": "assistant",
  "uuid": "cfd00c3c-d833-4c9e-aa35-4f40cd28e39c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "5ce792ab-ebc9-4b52-8f9c-3b1fb1b17c1f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013RrmKEpUsdEoCYaHgwytKA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7039,
      "cache_read_input_tokens": 71017,
      "output_tokens": 243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7039,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 243,
          "cache_read_input_tokens": 71017,
          "cache_creation_input_tokens": 7039,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7039
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-17T01:46:09.875Z_

<details><summary>↩ Tool result · `toolu_013iYygKzWbo9qDDas4McnRz`</summary>

```text
Perfect! Now let me create a comprehensive summary. I have all the information needed about the GPQA experiment plan.

## Summary: GPQA Experiment Plan

Based on my search of the project files, here's the complete GPQA experiment plan beyond the completed `gpqa_ds_importance_s015`:

### Decision Context (D098)
Found in `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/decisions.yaml` - Decision D098 (2026-05-16):
- **Segmentation strategy**: Quantile 3-segment decomposition as primary; `&lt;/think>` token-based validation as supplementary
- **Rationale**: Maintains consistency with existing paper framework (quantile established as primary method in background.tex L29-31, methodology.tex L14)
- **Role**: GPQA supplements MATH-500 to validate quantile-based phase segmentation on non-mathematical reasoning tasks

### Completed Experiment
- **gpqa_ds_importance_s015**: DeepSeek-R1-Distill-Qwen-7B, GPQA Diamond (198 problems), importance masking at s=0.15
  - Status: DONE (2026-05-16 15:43 → 2026-05-17 04:07, ~12.4 hours)
  - Result: PASS - Confirms monotonic severity gradient across phases (high=0.0128, mid=0.1024, low=0.9602 median II)
  - Evidence: 75x severity ratio between low and high sparsity phases

### Remaining GPQA Experiments (9 conditions)
Full command list written to `/root/autodl-tmp/pacs/gpqa_remaining_commands.txt` during worker operation 2026-05-16T152422:

#### DeepSeek-R1-Distill-Qwen-7B (5 conditions)
**Importance masking (3 sparsity levels):**
- `gpqa_ds_importance_s020` (s=0.20)
- `gpqa_ds_importance_s025` (s=0.25)
- `gpqa_ds_importance_s030` (s=0.30)

**Random masking controls (2 sparsity levels):**
- `gpqa_ds_random_s020` (s=0.20)
- `gpqa_ds_random_s025` (s=0.25)

#### Qwen2.5-7B-Instruct (4 conditions)
**Importance masking (4 sparsity levels):**
- `gpqa_qw_importance_s015` (s=0.15)
- `gpqa_qw_importance_s020` (s=0.20)
- `gpqa_qw_importance_s025` (s=0.25)
- `gpqa_qw_importance_s030` (s=0.30)

### Experimental Design Notes
- **Dataset**: GPQA Diamond (198 problems total)
- **Task type**: General knowledge (non-mathematical) to test phase-gradient generalization beyond MATH-500
- **Phase segmentation**: Quantile 3-segment (low/mid/high sparsity phases)
- **Max tokens**: 8192 for both model families (accommodates reasoning chains)
- **Min phase length**: 10 tokens
- **Status as of 2026-05-17**: Awaiting GPU availability; all 4 GPUs occupied by LLaMA and GSM8K experiments

### Key References
- Experiment plan metadata: `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/experiment_plan.yaml`
- Worker prep log: `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/logs/workers/worker_ops_gpqa_prep_remaining_20260516T152422.log`
- Completed analysis: `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/gpqa_ds_importance_s015_analysis.md`
- ROADMAP entries: `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/ROADMAP.md` (lines 63-71 describe GPQA as "Scope 扩展·线路 A")
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cfd00c3c-d833-4c9e-aa35-4f40cd28e39c",
  "isSidechain": false,
  "promptId": "ce667af9-41a5-4bed-8a5c-6707db53531e",
  "type": "user",
  "uuid": "c6b2c147-c182-45c5-ab8a-c93f436a0a8f",
  "toolUseResult": {
    "status": "completed",
    "prompt": "In the project at /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/, find the GPQA experiment plan or any file that lists what GPQA experiments are planned (beyond gpqa_ds_importance_s015 which is already done). Look for files that define the full set of GPQA experiments including random conditions. Check:\n1. Any experiment plan files mentioning GPQA\n2. The worker log for gpqa prep: worker_ops_gpqa_prep_remaining_20260516T152422.log\n3. Any decision log entries about GPQA\n\nSearch breadth: medium",
    "agentId": "aeea5adab0308efe6",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now let me create a comprehensive summary. I have all the information needed about the GPQA experiment plan.\n\n## Summary: GPQA Experiment Plan\n\nBased on my search of the project files, here's the complete GPQA experiment plan beyond the completed `gpqa_ds_importance_s015`:\n\n### Decision Context (D098)\nFound in `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/decisions.yaml` - Decision D098 (2026-05-16):\n- **Segmentation strategy**: Quantile 3-segment decomposition as primary; `&lt;/think>` token-based validation as supplementary\n- **Rationale**: Maintains consistency with existing paper framework (quantile established as primary method in background.tex L29-31, methodology.tex L14)\n- **Role**: GPQA supplements MATH-500 to validate quantile-based phase segmentation on non-mathematical reasoning tasks\n\n### Completed Experiment\n- **gpqa_ds_importance_s015**: DeepSeek-R1-Distill-Qwen-7B, GPQA Diamond (198 problems), importance masking at s=0.15\n  - Status: DONE (2026-05-16 15:43 → 2026-05-17 04:07, ~12.4 hours)\n  - Result: PASS - Confirms monotonic severity gradient across phases (high=0.0128, mid=0.1024, low=0.9602 median II)\n  - Evidence: 75x severity ratio between low and high sparsity phases\n\n### Remaining GPQA Experiments (9 conditions)\nFull command list written to `/root/autodl-tmp/pacs/gpqa_remaining_commands.txt` during worker operation 2026-05-16T152422:\n\n#### DeepSeek-R1-Distill-Qwen-7B (5 conditions)\n**Importance masking (3 sparsity levels):**\n- `gpqa_ds_importance_s020` (s=0.20)\n- `gpqa_ds_importance_s025` (s=0.25)\n- `gpqa_ds_importance_s030` (s=0.30)\n\n**Random masking controls (2 sparsity levels):**\n- `gpqa_ds_random_s020` (s=0.20)\n- `gpqa_ds_random_s025` (s=0.25)\n\n#### Qwen2.5-7B-Instruct (4 conditions)\n**Importance masking (4 sparsity levels):**\n- `gpqa_qw_importance_s015` (s=0.15)\n- `gpqa_qw_importance_s020` (s=0.20)\n- `gpqa_qw_importance_s025` (s=0.25)\n- `gpqa_qw_importance_s030` (s=0.30)\n\n### Experimental Design Notes\n- **Dataset**: GPQA Diamond (198 problems total)\n- **Task type**: General knowledge (non-mathematical) to test phase-gradient generalization beyond MATH-500\n- **Phase segmentation**: Quantile 3-segment (low/mid/high sparsity phases)\n- **Max tokens**: 8192 for both model families (accommodates reasoning chains)\n- **Min phase length**: 10 tokens\n- **Status as of 2026-05-17**: Awaiting GPU availability; all 4 GPUs occupied by LLaMA and GSM8K experiments\n\n### Key References\n- Experiment plan metadata: `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/experiment_plan.yaml`\n- Worker prep log: `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/logs/workers/worker_ops_gpqa_prep_remaining_20260516T152422.log`\n- Completed analysis: `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/gpqa_ds_importance_s015_analysis.md`\n- ROADMAP entries: `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/ROADMAP.md` (lines 63-71 describe GPQA as \"Scope 扩展·线路 A\")"
      }
    ],
    "totalDurationMs": 35236,
    "totalTokens": 51084,
    "totalToolUseCount": 20,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1239,
      "cache_read_input_tokens": 48759,
      "output_tokens": 1079,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1239
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 1079,
          "cache_read_input_tokens": 48759,
          "cache_creation_input_tokens": 1239,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1239,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 6,
      "searchCount": 3,
      "bashCount": 11,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "cfd00c3c-d833-4c9e-aa35-4f40cd28e39c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "5ce792ab-ebc9-4b52-8f9c-3b1fb1b17c1f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-17T01:49:11.027Z_

Now I have the full GPQA experiment plan. Let me generate worst-tier predictions for all planned experiments.

```yaml
tier: worst
narrative_guidance: >
  核心贡献从 'importance-specific phase interaction' reframe 为
  'phase-dependent compound severity is a universal phenomenon whose magnitude
  scales with eviction method discriminativeness'。GPQA 结果证实 random 在长推理链
  benchmark 上同样产生强 phase gradient（imp/rand ratio ≈ 1.5-2.0×，复现 LLaMA 模式），
  审稿人认为这削弱了 "importance-specific" 的核心 claim。Recency null 被解读为
  recency 本身是温和策略（保留 temporal locality），而非证明 scoring-specificity。
  新叙事：任何 non-trivial eviction 都产生 phase-dependent compound severity，
  severity magnitude 与 eviction discriminativeness 正相关（importance > random >> recency≈null），
  这是 quantitative scaling law 而非 qualitative dissociation。
  仍可投 EMNLP 但需重写 intro/framing，novelty claim 从 'dissociation discovery'
  降为 'scaling law quantification'。

imagined_experiments:
  - name: "gpqa_ds_importance_s020"
    plan_id: "gpqa_ds_importance_s020"
    description: "DeepSeek GPQA Diamond importance masking s=0.20, 198 problems, quantile phase segmentation"
    expected_results:
      n_problems: 198
      high_median_ii: 0.035
      mid_median_ii: 0.28
      low_median_ii: 1.85
      median_gradient_low_minus_high: 1.82
      ci_95: [1.45, 2.25]
      wilcoxon_p: 3.2e-28
      cohens_dz: 0.72
      monotonic: true
      low_high_ratio: 52.9
      dose_response_vs_s015: "1.82 vs 0.95 (1.9× increase)"
    result_rationale: >
      GPQA 的推理链比 MATH-500 更长且更异质（跨物理/化学/生物），phase segmentation 噪声更大。
      Importance gradient 存在且单调递增，但从 s015→s020 的增幅仅 ~1.9×（vs MATH-500 的 ~3.1×）。
      原因：GPQA 问题的 token 分布在 phase 间更均匀（每个 phase 内的 segment 数远多于 MATH-500），
      稀释了低 sparsity phase 的 vulnerability 集中效应。Gradient 数值在 [1.5, 2.0] 左右，
      显著但不如 MATH-500 dramatic。
    tables:
      - title: "GPQA DS Importance s020 Phase II"
        rows:
          - {phase: high, median_ii: 0.035, mean_ii: 0.22, ci: "[0.09, 0.45]"}
          - {phase: mid, median_ii: 0.28, mean_ii: 1.15, ci: "[0.85, 1.52]"}
          - {phase: low, median_ii: 1.85, mean_ii: 8.4, ci: "[6.8, 10.3]"}
    figures_description:
      - "Phase gradient bar plot: 三 phase 的 median II 呈弱单调递增，error bars 较宽"
    analysis: >
      Gradient 存在且统计显著，支持 phase-dependent severity 在 GPQA 上泛化。
      但增幅弱于 MATH-500 同 sparsity（MATH-500 s020 median_diff=1.48 vs GPQA 1.82，
      表面看 GPQA 更大是因为绝对值基线不同；normalized 后 GPQA scaling factor 更平坦）。
      关键问题：这个 gradient 是否 importance-specific 取决于 random 对照。

  - name: "gpqa_ds_importance_s025"
    plan_id: "gpqa_ds_importance_s025"
    description: "DeepSeek GPQA Diamond importance masking s=0.25, 198 problems"
    expected_results:
      n_problems: 198
      high_median_ii: 0.08
      mid_median_ii: 0.62
      low_median_ii: 2.85
      median_gradient_low_minus_high: 2.77
      ci_95: [2.1, 3.5]
      wilcoxon_p: 8.1e-35
      cohens_dz: 0.88
      monotonic: true
      low_high_ratio: 35.6
      dose_response_vs_s020: "2.77 vs 1.82 (1.52× increase)"
    result_rationale: >
      继续单调递增但 marginal increase 递减（s020→s025 仅 1.52×，vs s015→s020 的 1.9×）。
      这与 MATH-500 的 sub-exponential growth 一致（C6 confirmed），但在 GPQA 上递减更快。
      原因：GPQA 的长推理链在高 sparsity 时进入 "saturation regime"——低 sparsity phase 的
      perplexity 已经很高（可能 >50），进一步增加 sparsity 的 marginal 破坏效果有限。
      Ratio 35.6× 比 s015 的 75.2× 下降，说明 high phase 的 II 也在上升（0.008→0.035→0.08），
      three-way separation 在缩小。
    tables:
      - title: "GPQA DS Importance s025 Phase II"
        rows:
          - {phase: high, median_ii: 0.08, mean_ii: 0.45, ci: "[0.25, 0.72]"}
          - {phase: mid, median_ii: 0.62, mean_ii: 3.8, ci: "[2.6, 5.2]"}
          - {phase: low, median_ii: 2.85, mean_ii: 15.2, ci: "[11.5, 19.8]"}
    figures_description:
      - "Dose-response curve: s015→s025 gradient 增长曲线明显比 MATH-500 平坦"
    analysis: >
      Phase gradient 稳健但 scaling 平坦。如果 random s025 也达到 ~1.5-2.0，
      imp/rand ratio 仅 1.4-1.8×，无法支撑 "importance-specific" claim。

  - name: "gpqa_ds_importance_s030"
    plan_id: "gpqa_ds_importance_s030"
    description: "DeepSeek GPQA Diamond importance masking s=0.30, 198 problems"
    expected_results:
      n_problems: 198
      high_median_ii: 0.15
      mid_median_ii: 1.05
      low_median_ii: 3.45
      median_gradient_low_minus_high: 3.30
      ci_95: [2.4, 4.0]
      wilcoxon_p: 2.5e-38
      cohens_dz: 0.95
      monotonic: true
      low_high_ratio: 23.0
      dose_response_full: "0.95 → 1.82 → 2.77 → 3.30 (sub-exponential, Δ factors: 1.9×, 1.52×, 1.19×)"
      growth_rate_decreasing: true
    result_rationale: >
      Worst tier 核心指标：gpqa_importance_median_gradient_s030 落在 [1.5, 4.0] 范围内，
      这里预测 3.30。比 MATH-500 的 8.48（n=500）或 14.59（n=50）弱得多。
      原因有三：(1) GPQA 问题的推理链更长（平均 6000+ tokens vs MATH-500 ~1200），
      phase segmentation 的 signal-to-noise ratio 降低；(2) GPQA 是 multiple-choice 而非
      open-ended generation，即使推理过程被严重扰乱，最终仍可能 "猜中" 正确选项，
      limiting the maximum compound interaction observable；(3) 在极高 sparsity 时
      GPQA 进入 "ceiling effect"——所有 phase 都严重受损，phase 间差异被压缩。
      s030 已接近 saturation，gradient 增幅仅 1.19×。
    tables:
      - title: "GPQA DS Importance Dose-Response Summary"
        rows:
          - {sparsity: "s015", median_gradient: 0.95, ci: "[0.89, 1.03]", dz: 0.814}
          - {sparsity: "s020", median_gradient: 1.82, ci: "[1.45, 2.25]", dz: 0.72}
          - {sparsity: "s025", median_gradient: 2.77, ci: "[2.1, 3.5]", dz: 0.88}
          - {sparsity: "s030", median_gradient: 3.30, ci: "[2.4, 4.0]", dz: 0.95}
    figures_description:
      - "GPQA vs MATH-500 dose-response comparison: GPQA 曲线明显平坦，s030 仅为 MATH-500 的 39%"
    analysis: >
      Dose-response 单调但 sub-exponential 且明显比 MATH-500 弱。
      审稿人会指出：如果 gradient magnitude 是 task-dependent 且 GPQA 上 weak，
      那 paper 的核心 claim 被限制为 "on specific math benchmarks with medium-length chains"。
      结合 random 同样显示 gradient 的结果，specificity claim 被严重削弱。

  - name: "gpqa_ds_random_s020"
    plan_id: "gpqa_ds_random_s020"
    description: "DeepSeek GPQA Diamond random masking s=0.20, 198 problems"
    expected_results:
      n_problems: 198
      high_median_ii: 0.025
      mid_median_ii: 0.22
      low_median_ii: 1.25
      median_gradient_low_minus_high: 1.20
      ci_95: [0.85, 1.60]
      wilcoxon_p: 4.7e-18
      cohens_dz: 0.52
      monotonic: true
      imp_rand_ratio_s020: 1.52
      comparison_math500_rand_s020: "MATH-500 random s020 median_diff = -0.016 (NS); GPQA random s020 = 1.20 (p<1e-17)"
    result_rationale: >
      这是 worst tier 的关键 negative 结果。GPQA random masking 在 s020 已产生
      显著且 non-trivial 的 phase gradient（d_z=0.52, medium effect）。
      对比 MATH-500 random s020 完全 NS（median_diff=-0.016），GPQA random 的行为
      qualitatively 不同。原因：GPQA 的长推理链（平均 6000+ tokens）意味着
      random eviction 在低 sparsity phase（reasoning-heavy）会移除更多 token
      （因为该 phase 有更多 token），造成的破坏本身就与 phase position 相关。
      这是一个 trivial 的 "longer phase = more tokens removed = more damage" 效应，
      不需要 scoring-specific mechanism 来解释。审稿人会认为 GPQA 上
      importance 和 random 的 gradient 只是 token count per phase 的函数，
      而非 attention score discriminativeness 的证据。
      Imp/rand ratio 仅 1.52×（远低于 MATH-500 的 15-17×），复现 LLaMA 的模式（2.0-2.6×）。
    tables:
      - title: "GPQA DS Random s020 Phase II"
        rows:
          - {phase: high, median_ii: 0.025, mean_ii: 0.18, ci: "[0.05, 0.35]"}
          - {phase: mid, median_ii: 0.22, mean_ii: 0.85, ci: "[0.45, 1.30]"}
          - {phase: low, median_ii: 1.25, mean_ii: 5.2, ci: "[3.1, 7.8]"}
      - title: "Imp/Rand Ratio Cross-Benchmark"
        rows:
          - {benchmark: "MATH-500 (DS)", s020_ratio: "∞ (rand NS)", s025_ratio: 15.5, s030_ratio: 16.6}
          - {benchmark: "GSM8K (DS)", s020_ratio: 2.5, s025_ratio: 3.8, s030_ratio: 2.8}
          - {benchmark: "GPQA (DS)", s020_ratio: 1.52, s025_ratio: "~1.6 (projected)", s030_ratio: "~1.5 (projected)"}
    figures_description:
      - "Three-way comparison: importance vs random phase gradient on GPQA，两条线几乎平行"
    analysis: >
      审稿人的核心攻击点：如果 GPQA random gradient 和 importance gradient 几乎一样强
      （ratio 1.5×），那 "discrimination collapse" 机制不是必要解释——
      任何 token removal 在长链上都产生 phase-dependent damage。
      Phase gradient 可能只是 "phase 内 token 数量" 的 trivial 后果。
      Reframe 需要论证：即使 ratio 小，importance 仍然 consistently > random
      跨所有条件，这是 "discriminativeness scaling" 而非 absence of specificity。

  - name: "gpqa_ds_random_s025"
    plan_id: "gpqa_ds_random_s025"
    description: "DeepSeek GPQA Diamond random masking s=0.25, 198 problems"
    expected_results:
      n_problems: 198
      high_median_ii: 0.06
      mid_median_ii: 0.48
      low_median_ii: 1.95
      median_gradient_low_minus_high: 1.89
      ci_95: [1.3, 2.5]
      wilcoxon_p: 1.8e-22
      cohens_dz: 0.58
      monotonic: true
      imp_rand_ratio_s025: 1.47
      comparison_math500: "MATH-500 random s025 median_diff=0.54 (significant but weak); GPQA random s025=1.89 (strong)"
    result_rationale: >
      Random gradient 继续增强，且 imp/rand ratio 进一步压缩到 1.47×。
      注意在 MATH-500 上 random s025 的 median_diff=0.54 已经 significant（D063 阈值效应），
      但远小于 importance 的 7.16（ratio 13.2×）。在 GPQA 上这个 ratio 坍缩到 1.47×。
      原因：GPQA 的长 context 使得 attention score 的 discriminativeness 本身就弱
      （信息分散在更多 token 上），importance 和 random eviction 的 "effective difference"
      被 context length 稀释。这正是审稿人的 "trivial" 论点：
      在足够长的 context 上，importance scoring 不再提供相对于 random 的显著优势，
      因此 importance-specific phase interaction 的 claim 成为 benchmark-specific artifact。
    tables:
      - title: "GPQA DS Random s025 Phase II"
        rows:
          - {phase: high, median_ii: 0.06, mean_ii: 0.35, ci: "[0.15, 0.60]"}
          - {phase: mid, median_ii: 0.48, mean_ii: 2.1, ci: "[1.2, 3.2]"}
          - {phase: low, median_ii: 1.95, mean_ii: 9.5, ci: "[6.0, 13.5]"}
    figures_description:
      - "Imp vs Random gradient comparison at s025: bars nearly equal height"
    analysis: >
      Ratio 1.47× 落在 worst tier 指定范围 [1.0, 2.0] 内。
      审稿人结论：GPQA 数据表明 phase gradient 不是 importance-specific 现象，
      而是 token removal 在长推理链上的 universal phase-dependent effect。
      Paper 必须放弃 "qualitative dissociation" claim，转向 "quantitative scaling"。

  - name: "gpqa_qw_importance_s015"
    plan_id: "gpqa_qw_importance_s015"
    description: "Qwen2.5-7B GPQA Diamond importance masking s=0.15, 198 problems"
    expected_results:
      n_problems: 198
      high_median_ii: 0.003
      mid_median_ii: 0.025
      low_median_ii: 0.18
      median_gradient_low_minus_high: 0.177
      ci_95: [0.12, 0.24]
      wilcoxon_p: 2.3e-12
      cohens_dz: 0.45
      monotonic: true
    result_rationale: >
      Qwen 在 MATH-500 上的 magnitude 约为 DeepSeek 的 1/4（已确认模式）。
      GPQA 上预期同样的缩放：DS GPQA s015 gradient=0.95，QW ≈ 0.95/5.3 ≈ 0.18
      （GPQA 上 Qwen 的 effective 推理链更短、更 shallow，因为 Qwen 不是 reasoning-specialized model，
      导致 phase gradient 更弱）。Phase gradient 存在但效应量 medium-small (d_z=0.45)。
      Onset threshold 可能与 MATH-500 相似（s≥0.15 barely significant）。
    tables:
      - title: "GPQA QW Importance s015"
        rows:
          - {phase: high, median_ii: 0.003, mean_ii: 0.015, ci: "[-0.005, 0.04]"}
          - {phase: mid, median_ii: 0.025, mean_ii: 0.12, ci: "[0.06, 0.20]"}
          - {phase: low, median_ii: 0.18, mean_ii: 0.95, ci: "[0.65, 1.30]"}
    figures_description: []
    analysis: >
      Qwen GPQA gradient 非常弱（0.177 vs DS 的 0.95），但仍统计显著。
      问题在于这么小的效应量在审稿人看来是 "technically significant but practically irrelevant"。

  - name: "gpqa_qw_importance_s020"
    plan_id: "gpqa_qw_importance_s020"
    description: "Qwen2.5-7B GPQA Diamond importance masking s=0.20, 198 problems"
    expected_results:
      n_problems: 198
      high_median_ii: 0.008
      mid_median_ii: 0.065
      low_median_ii: 0.45
      median_gradient_low_minus_high: 0.442
      ci_95: [0.30, 0.60]
      wilcoxon_p: 5.1e-18
      cohens_dz: 0.55
      monotonic: true
    result_rationale: >
      Qwen s020 继续增长（0.177→0.442, 2.5× factor），与 MATH-500 上 Qwen s015→s020 的
      增长模式一致（0.048→0.208, 4.3×）。GPQA 上增幅略弱是因为 Qwen 在 GPQA 任务上
      推理链更短（非 reasoning-specialized），phase segmentation 的三段中 mid 段占比小，
      导致 low/high 差异的 signal 被 within-phase variance 部分掩盖。
    tables:
      - title: "GPQA QW Importance s020"
        rows:
          - {phase: high, median_ii: 0.008, mean_ii: 0.04, ci: "[0.01, 0.08]"}
          - {phase: mid, median_ii: 0.065, mean_ii: 0.35, ci: "[0.18, 0.55]"}
          - {phase: low, median_ii: 0.45, mean_ii: 2.1, ci: "[1.4, 2.9]"}
    figures_description: []
    analysis: >
      Gradient 确认 Qwen 在 GPQA 上也有 phase modulation，但 magnitude 仅为 DS 的 ~1/4。
      Cross-model scaling 与 MATH-500 一致（QW/DS ratio ≈ 0.24）。

  - name: "gpqa_qw_importance_s025"
    plan_id: "gpqa_qw_importance_s025"
    description: "Qwen2.5-7B GPQA Diamond importance masking s=0.25, 198 problems"
    expected_results:
      n_problems: 198
      high_median_ii: 0.02
      mid_median_ii: 0.15
      low_median_ii: 0.85
      median_gradient_low_minus_high: 0.83
      ci_95: [0.55, 1.15]
      wilcoxon_p: 1.2e-25
      cohens_dz: 0.68
      monotonic: true
    result_rationale: >
      继续 sub-exponential 增长（0.442→0.83, 1.88×）。Qwen 在 s025 效应量进入
      medium-to-large 范围，pattern 与 MATH-500 一致。但在 worst tier 下，
      如果同时有 Qwen random GPQA 数据（即使没在当前 plan 中），
      审稿人会 extrapolate LLaMA pattern 预期 ratio 同样 ≈1.5-2.0×。
    tables:
      - title: "GPQA QW Importance s025"
        rows:
          - {phase: high, median_ii: 0.02, mean_ii: 0.12, ci: "[0.05, 0.20]"}
          - {phase: mid, median_ii: 0.15, mean_ii: 0.75, ci: "[0.45, 1.10]"}
          - {phase: low, median_ii: 0.85, mean_ii: 4.2, ci: "[2.8, 5.8]"}
    figures_description: []
    analysis: >
      在没有 Qwen random GPQA 对照的情况下，审稿人会引用 DS random GPQA 数据
      论证 "even on the same benchmark, random shows strong gradient"。

  - name: "gpqa_qw_importance_s030"
    plan_id: "gpqa_qw_importance_s030"
    description: "Qwen2.5-7B GPQA Diamond importance masking s=0.30, 198 problems"
    expected_results:
      n_problems: 198
      high_median_ii: 0.04
      mid_median_ii: 0.30
      low_median_ii: 1.35
      median_gradient_low_minus_high: 1.31
      ci_95: [0.85, 1.80]
      wilcoxon_p: 3.8e-30
      cohens_dz: 0.78
      monotonic: true
      qw_ds_ratio_gpqa_s030: 0.40
    result_rationale: >
      Qwen s030 gradient 1.31 — 约为 DS s030（3.30）的 40%。
      比 MATH-500 上的 QW/DS ratio（3.155/8.48=37%）略高但在同一量级。
      Cross-model scaling 跨 benchmark 一致（~35-40%）是 positive signal，
      但绝对值 1.31 太弱——审稿人会说 "Qwen on GPQA shows a phase gradient
      indistinguishable from noise on any individual problem"。
      注意 worst tier gpqa_importance_median_gradient_s030 范围是 [1.5, 4.0]，
      这里 Qwen 的 1.31 甚至低于下限——但该范围指的是 DS（primary model）。
      Qwen 作为 cross-model replication 不需要单独达标。
    tables:
      - title: "GPQA QW Full Dose-Response"
        rows:
          - {sparsity: "s015", gradient: 0.177, dz: 0.45}
          - {sparsity: "s020", gradient: 0.442, dz: 0.55}
          - {sparsity: "s025", gradient: 0.830, dz: 0.68}
          - {sparsity: "s030", gradient: 1.310, dz: 0.78}
    figures_description:
      - "QW GPQA dose-response 与 DS GPQA 并列，显示一致的单调递增但 magnitude ~40%"
    analysis: >
      Cross-model replication 方向一致，QW/DS ratio 跨 benchmark 稳定。
      但问题是 Qwen magnitude 太小，使得 "practically meaningful" 的论证困难。

  - name: "gpqa_ds_random_s030_projected"
    plan_id: "gpqa_ds_random_s030 (projected from s020+s025 pattern)"
    description: "Projected: DeepSeek GPQA random s=0.30 based on worst-tier scaling"
    expected_results:
      n_problems: 198
      high_median_ii: 0.10
      mid_median_ii: 0.75
      low_median_ii: 2.35
      median_gradient_low_minus_high: 2.25
      ci_95: [1.5, 3.1]
      wilcoxon_p: 5.0e-25
      cohens_dz: 0.62
      monotonic: true
      imp_rand_ratio_s030: 1.47
      cross_benchmark_ratio_comparison: "MATH-500: 16.6×; GSM8K: 2.8×; GPQA: 1.47×"
    result_rationale: >
      Random s030 gradient 投射为 ~2.25（基于 s020=1.20, s025=1.89 的增长趋势，
      factor 1.58×→1.19×，递减模式）。Imp/rand ratio 在 s030 为 3.30/2.25=1.47×。
      这是 worst tier 的核心 devastating 结果：GPQA 上 strategy specificity
      几乎消失（ratio < 1.5×），与 LLaMA MATH-500（2.0-2.6×）相当甚至更弱。
      审稿人总结："The claimed importance-specificity is an artifact of short-to-medium
      math chains (MATH-500). On longer, more heterogeneous reasoning (GPQA),
      random eviction produces essentially the same phase-dependent pattern."
      这迫使 reframe：paper 的贡献不再是 "importance eviction has unique phase interaction"，
      而是 "all eviction methods show phase-dependent compound severity,
      with magnitude proportional to discriminativeness"。
    tables:
      - title: "GPQA Imp/Rand Ratio Across Sparsities (Worst Tier)"
        rows:
          - {sparsity: "s020", imp_gradient: 1.82, rand_gradient: 1.20, ratio: 1.52}
          - {sparsity: "s025", imp_gradient: 2.77, rand_gradient: 1.89, ratio: 1.47}
          - {sparsity: "s030", imp_gradient: 3.30, rand_gradient: 2.25, ratio: 1.47}
      - title: "Cross-Benchmark Strategy Specificity (DS, s030)"
        rows:
          - {benchmark: "MATH-500", imp_gradient: 8.48, rand_gradient: 0.51, ratio: "16.6×"}
          - {benchmark: "GSM8K", imp_gradient: 4.68, rand_gradient: 1.67, ratio: "2.8×"}
          - {benchmark: "GPQA", imp_gradient: 3.30, rand_gradient: 2.25, ratio: "1.47×"}
    figures_description:
      - "Strategy specificity ratio 随 benchmark reasoning chain length 递减的 trend line"
      - "Scatter: chain length (x) vs imp/rand ratio (y)，negative correlation"
    analysis: >
      Cross-benchmark specificity 模式清晰：MATH-500（短链） > GSM8K（中链） > GPQA（长链）。
      审稿人解读：importance 的 "advantage" over random 随 context length 递减，
      因为在长 context 中 attention score 的 discriminativeness 本身就降低
      （信息分散、head attention pattern 更 uniform）。
      这支持 worst tier narrative："phase-dependent compound severity is universal;
      importance-specificity is a function of context length, not a fundamental property."
      Paper reframe 后的 contribution 是量化这个 scaling law。

  - name: "recency_worst_tier_reinterpretation"
    plan_id: "C11 (recency reinterpretation under worst tier)"
    description: "Recency null results reinterpreted by reviewers as trivial temporal locality preservation"
    expected_results:
      recency_s015_dz: 0.083
      recency_s025_dz: 0.22
      recency_s030_dz: -0.096
      all_NS: true
      max_dz: 0.22
      reviewer_interpretation: "Recency preserves temporal locality → mild eviction for sequential reasoning → null is expected, not informative"
    result_rationale: >
      Recency 实验数据不变（已 confirmed），但审稿人的解读改变。
      Worst tier 下审稿人认为：recency eviction 保留最近 token 本身就是对 sequential
      reasoning 最温和的策略（因为 reasoning chain 是从左到右构建的，最近 token 包含
      当前推理步骤）。因此 recency 的 null gradient 不是因为它 "scoring-independent"
      （从而排除 scoring pathway confound），而是因为它作为 eviction 策略本身就弱
      （eviction overlap with oracle 高，即 recency 保留的 token 恰好是最重要的）。
      如果 recency 的 token preservation 与 importance ranking 高度重合，
      那它不是有效的 negative control。审稿人要求：quantify eviction overlap
      between recency selection and importance ranking（如果 overlap > 70%，
      recency 就不是 "independent" control）。
      Worst tier 中 recency_max_dz_across_sparsities 在 [0.0, 0.15] 范围内
      （s025 的 0.22 略超此范围但 direction 反转 → 不支持 gradient hypothesis）。
    tables:
      - title: "Recency Control Results (Actual Data, Reviewer Reinterpretation)"
        rows:
          - {sparsity: "s015", dz: 0.083, p: 0.77, reviewer_note: "NS — but expected if recency≈importance"}
          - {sparsity: "s025", dz: 0.22, p: 0.009, reviewer_note: "Barely significant, REVERSED direction"}
          - {sparsity: "s030", dz: -0.096, p: 0.114, reviewer_note: "NS, numerical instability"}
    figures_description: []
    analysis: >
      审稿人的 counter-argument：recency 不是有效 control 因为它 by construction
      preserves the most recent (and for reasoning, most critical) tokens。
      需要补充 eviction overlap 分析：计算 recency eviction set 与 importance
      bottom-k set 的 Jaccard overlap。如果 overlap 低（<30%），control 有效；
      如果 overlap 高（>60%），control 被 confound。
      这是 worst tier 下需要额外实验（eviction overlap quantification）来
      defend C11 的情况，但 deadline 前可能无法完成。

  - name: "reviewer_assessment_worst"
    plan_id: "overall_reviewer_simulation"
    description: "Simulated reviewer scores and key criticisms under worst tier"
    expected_results:
      novelty_score: 2.5
      soundness_score: 3.0
      significance_score: 2.0
      overall_score: 2.75
      acceptance_probability: 0.15
      key_criticisms:
        - "Phase gradient on GPQA is NOT importance-specific (ratio 1.5×). Core claim fails to generalize."
        - "Recency control is confounded by temporal locality — not an independent control."
        - "The 'discrimination collapse' mechanism is just restating 'pruning hurts quality'."
        - "MATH-500 specificity (15-17×) appears to be a benchmark-specific artifact of medium chain lengths."
        - "C5b mitigation failure + no practical contribution = purely descriptive paper with limited impact."
      recommended_decision: "reject (borderline)"
    result_rationale: >
      Worst tier 审稿人 profile：一位 KV cache 方向的 expert reviewer 会直接指出
      GPQA random gradient 使 "importance-specific" claim 不成立。Novelty 从
      "qualitative dissociation" 降为 "quantitative observation"，且观察本身可被
      trivialized 为 "longer reasoning chains are more fragile to any eviction"。
      Soundness 3.0（实验本身做得好，statistics 严谨），但 significance 2.0
      （无 practical method，无 clear actionable insight）。
      Overall 2.75 → borderline reject，acceptance probability 约 15%。
      即使 reframe 成功（"scaling law" narrative），也需要 additional evidence：
      (1) eviction overlap quantification defending recency control，
      (2) explicit discriminativeness metric (e.g., oracle overlap) 量化 importance
      vs random 的 eviction quality 差异作为 scaling law 的 x-axis。
    tables:
      - title: "Projected Reviewer Scores (Worst Tier)"
        rows:
          - {criterion: "Novelty", score: 2.5, note: "quantitative, not qualitative"}
          - {criterion: "Soundness", score: 3.0, note: "rigorous stats, proper controls"}
          - {criterion: "Significance", score: 2.0, note: "no method, no clear utility"}
          - {criterion: "Clarity", score: 3.5, note: "well-written if reframed"}
          - {criterion: "Overall", score: 2.75, note: "borderline reject"}
    figures_description: []
    analysis: >
      Reframe strategy under worst tier:
      (1) Title 改为 "Phase-Dependent Compound Severity Scales with Eviction Discriminativeness"
      (2) 放弃 importance-specific framing，embrace universality as the finding
      (3) 引入 eviction discriminativeness 作为 quantitative predictor（oracle overlap metric）
      (4) 论证即使 universal，prior work 从未量化 phase×strategy×sparsity 三维 interaction
      (5) Acknowledge GPQA ratio ~1.5× honestly，但强调 monotonic ordering
          (importance > random > recency) 跨所有 benchmarks/architectures 是 consistent
      这仍然是 publishable contribution 但需要降低 novelty claim 的强度。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6b2c147-c182-45c5-ab8a-c93f436a0a8f",
  "isSidechain": false,
  "requestId": "req_011Cb7JAEhW4kLbHa8mf7Ykb",
  "type": "assistant",
  "uuid": "582c4502-d0af-48ac-a217-803012ca4860",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "5ce792ab-ebc9-4b52-8f9c-3b1fb1b17c1f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VjCSMTrCMCkV8Yp7JLeVcf",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1331,
      "cache_read_input_tokens": 78056,
      "output_tokens": 9812,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1331,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9812,
          "cache_read_input_tokens": 78056,
          "cache_creation_input_tokens": 1331,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1331
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 19_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：GPQA random 也显示强 gradient（ratio ≈ 1×）+ 审稿人认为现象是 trivial（token removal 的必然后果而非 scoring-specific）+ 需要完全 reframe 核心 claim 核心假设：['GPQA importance gradient 存在但…",
  "leafUuid": "582c4502-d0af-48ac-a217-803012ca4860",
  "sessionId": "5ce792ab-ebc9-4b52-8f9c-3b1fb1b17c1f"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Phase-gated compound sparsity in worst-case scenario",
  "sessionId": "5ce792ab-ebc9-4b52-8f9c-3b1fb1b17c1f"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：GPQA random 也显示强 gradient（ratio ≈ 1×）+ 审稿人认为现象是 trivial（token removal 的必然后果而非 scoring-specific）+ 需要完全 reframe 核心 claim 核心假设：['GPQA importance gradient 存在但…",
  "leafUuid": "582c4502-d0af-48ac-a217-803012ca4860",
  "sessionId": "5ce792ab-ebc9-4b52-8f9c-3b1fb1b17c1f"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Phase-gated compound sparsity in worst-case scenario",
  "sessionId": "5ce792ab-ebc9-4b52-8f9c-3b1fb1b17c1f"
}
```

---
