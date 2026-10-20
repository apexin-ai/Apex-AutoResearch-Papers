# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：Reviewers fully accept empirical-finding framing; recency control + triple d

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-1/801dd6fc-5861-4c46-a727-64581ec2a334.jsonl`
- **Structured JSON:** [`e4ac69e99697112e8c83.json`](../../sessions/e4/e4ac69e99697112e8c83.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-17T01:29:19.976Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-17T01:29:19.976Z",
  "sessionId": "801dd6fc-5861-4c46-a727-64581ec2a334",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：Reviewers fully accept empirical-finding framing; recency control + triple dissociation seen as clean novel contribution; cross-architecture variation treated as interesting secondary finding rather than weakness\n核心假设：['Empirical finding paper without practical method accepted at EMNLP (precedent: scaling laws papers, probing papers)', 'Recency control resolves circularity concern definitively — no reviewer requests causal intervention', 'Architecture-dependent strategy specificity (LLaMA 2.0-2.6× vs DS 15-17×) framed as discovery, not confound', '50-citation related work + explicit gap analysis convinces reviewers of novelty vs ThinKV/SparK/Lethe', '7B scale accepted with honest limitations paragraph; no hard reject on scale alone', 'Discrimination collapse mechanism (Gini/CV consistent cross-model) accepted despite entropy being model-dependent']\n关键指标范围：{'arr_overall_scores': [3.5, 4.5], 'arr_soundness': [3.5, 4.0], 'acceptance_probability': [0.55, 0.75], 'reviewer_novelty_concern_count': [0, 1], 'claims_requiring_adjustment': [0, 1]}\n叙事方向：Original framing intact: 'emergent phase-strategy interaction' as core contribution, triple dissociation (importance/random/recency) as methodological novelty, architecture-dependence as scope-expanding finding. C1-C11 全部保留原始强度。Discussion 正常报告 GSM8K ratio 衰减和 LLaMA specificity 差异作为 open questions，不需要 hedge main claims。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: phase-gated-compound-sparse\nfocus: Key improvements since last dream: (1) recency scoring-independent control confirms phase gradient is attention-score-specific (three-way dissociation: importance/random/recency), (2) full 8-condition LLaMA cross-architecture validation (n=250, all PASS), (3) expanded related work (50 citations), (4) \"why not causal\" self-defense in discussion, (5) dense baseline phase stats. Evaluate whether these address the previous dream's main criticisms: narrow novelty, circularity concern, thin references, no figures, no practical method.\n\n## paper_framing.md\n\n# Paper Framing — Phase-Gated Compound Sparsity\n\n> 最后更新: 2026-05-17 (D102: C11 confirmed — recency triple NS across s015/s025/s030; s015+s025 primary, s030 supplementary) | 维护者: Director\n\n## Core Insight\n\nCompound sparsity（attention head pruning + KV cache eviction）的 severity 不是固定常数——它是 eviction strategy 和 reasoning phase 交互的涌现属性。Importance-based eviction 的 compound interaction severity（paired median difference: median(II_low_i − II_high_i)）随 sparsity 单调递增（DeepSeek: 0.39→1.21→3.99→8.48; Qwen: 0.07→0.31→1.07→3.16），而 random masking 在 s015/s020 NS，在 s025 跨模型显著但效应量远小于 importance（DS: 0.257 vs 3.986; QW: 0.393 vs 1.074, 2.7-17×差异），存在 sparsity threshold ~s020-s025（D063; s030 待定）。Cohen's d（per-problem paired, B=10000）从 medium 到 large（DeepSeek: 0.61→1.13; Qwen: 0.37→1.44，registry cohens_d s015→s030）。LLaMA 跨架构验证（D060, c8_llama_n250_fixed, n=250）：within-importance phase gradient 强（d_z=0.81-1.15, all p<10^-29, all monotonic），且 random 在 LLaMA 上所有条件均显著（d_z=0.41-0.46, all p<10^-12），imp/rand Δ ratio 仅 2.0-2.6×（vs DeepSeek 15-17×），strategy×phase 交互强度 architecture-dependent。GSM8K 跨 benchmark 验证（D075）：importance masking 的 phase gradient 在 GSM8K 上同样单调递增（QW: 0.039→0.158→1.100→2.092; DS: 0.241→0.740→1.992→4.682），但 strategy specificity（importance/random gradient ratio）从 MATH-500 的 15-17× 衰减至 GSM8K 的 2.3-3.8×。注意：\"反转\"仅在原始 II_low 值上（random > importance），phase gradient 层面 importance ≥ random。Strategy specificity 的 task-dependence 机制是开放问题（见 §6 Discussion）。这一发现挑战了 compound degradation 均匀分布的隐含假设。\n\n**数字基准**：所有数字基于 bf16 per-problem paired 统计量（B=10000 bootstrap）。median_diff 定义为 median(II_low_i − II_high_i)（逐 problem 配对差的中位数）。fp16 旧数据已弃用。\n\n## Narrative Arc\n\nCompound sparsity 是高效 LLM 推理的实用部署需求，但 prior work（SparK, Ada-KV, SLiM）将 compound interaction 视为均匀超可加。我们发现 severity 是 strategy × phase 交互的涌现属性：importance eviction 的 compound interaction 在 low-sparsity phase 远大于 high-sparsity phase（paired median difference 单调递增 0.39→8.48），而 random eviction 在低 sparsity (s015/s020) NS，在 s025+ 跨模型显著但效应量远小于 importance (2.7-17×)——存在 sparsity threshold (~s020-s025)，低于阈值 compound effect importance-specific，高于阈值两者均触发但 importance 主导。Cross-model replication 方向一致（Qwen magnitude ~1/4 of DeepSeek，onset threshold s≥0.20）。LLaMA 跨架构验证已完成（c8_llama_n250_fixed, n=250, D060）：within-importance phase gradient 强（d_z=0.81-1.15, all p<10^-29），random 所有条件显著（d_z=0.41-0.46, all p<10^-12），但 imp/rand ratio 仅 2.0-2.6×（远低于 DS 15-17×），strategy×phase 交互强度 architecture-dependent。Recency-based eviction（scoring-independent control, D100/D102）跨三个 sparsity level 均产生 null phase gradient（s015+s025 为 primary evidence，s030 supplementary due to numerical instability at extreme sparsity），确认 phase-dependent severity 是 attention-score-based eviction 的特有交互效应而非 token removal 的 trivial 副产物。我们通过 discrimination collapse 机制解释这一现象：head pruning → importance score 的判别力崩塌（Gini/CV 下降跨模型一致）→ importance eviction 退化为有偏伪随机。Attention entropy redistribution 作为 model-dependent secondary effect 在 DeepSeek 上观察到，但在 Qwen 上不稳健（D044）。\n\n**Framing 硬约束（D015）**：\n- MUST: \\\"emergent phase-strategy interaction\\\"\n- MUST NOT: \\\"importance metric limitation / importance is broken\\\"\n- MUST NOT: claim \\\"importance masking produces super-additive interaction\\\" without qualifier — random masking also produces positive II, and at s025+ random is statistically significant (D063). The distinguishing signal is **magnitude gradient** (importance 2.7-17× larger) and **onset threshold** (random NS below ~s020, importance significant from s015+), not the existence of super-additivity itself (D023)\n\n## Core Claims\n\n| ID | Claim | Status | Key Evidence |\n|----|-------|--------|-------------|\n| C1 | Compound sparsity severity is strategy- and task-modulated | confirmed | MATH-500: importance gradient 15-17× random (DeepSeek s025-s030); GSM8K: ratio 衰减至 2.3-3.8× (D075)。Phase gradient 层面 importance ≥ random 跨 benchmark 成立，但 magnitude ratio task-dependent。Threshold ~s020-s025 (D063) |\n| C2 | Severity is phase-modulated (amplified in low-sparsity phase) | confirmed | bf16 paired median difference 单调递增: 0.39→1.21→3.99→8.48; Bonferroni p<0.005 全 4 水平 (D032)。预注册：n=500 后若 QW s015 CI 仍跨零，叙事改为 'compound effect emerges above threshold sparsity (~s020)' |\n| C3 | Phase-strategy crossover exists | confirmed | s=0.25: importance high_phase=0.032 < random=0.818, importance low_phase=7.196 > random=1.363 (bf16) |\n| C4 | Discrimination collapse as primary mechanism; entropy redistribution model-dependent | partially_confirmed | D044: Gini/CV 下降跨模型一致; entropy collapse DeepSeek 一致但 Qwen s025 反转(+0.045) s030≈0。30/30 problems completed. |\n| C5 | Phase-modulated compound severity generalizes across models | confirmed | DeepSeek + Qwen cross-model replication: 方向一致, Cohen's d ρ=1.0, gradient permutation p=0.043. Qwen magnitude ~1/4 of DeepSeek, onset threshold s≥0.20 (S3→C). |\n| C5b | Phase-aware mitigation recovers compound degradation | future_work | D056: pilot 完成 gate_failed。Oracle recovery 18% < 30% gate (Wilcoxon p=0.002)，heuristic 32% 但 CI 跨零。方向正确但效应量不足，需更精细 phase boundary estimation → future work |\n| C6 | Severity gradient is sub-exponential | confirmed | Growth rate decreasing: Δ增长因子 3.8×→4.8×→2.0×（递减） |\n| C7 | Statistical power at n=500 confirms dose-response | confirmed | c2_n500_deepseek (success) + c2_qw_n500_r3 (success): 两模型 n=500 全 4 sparsity Bonferroni p<0.005, Spearman ρ=1.0 |\n| C8 | Cross-architecture validation (LLaMA) | confirmed | c8_llama_n250_fixed (n=250, D060): within-importance phase gradient d_z=0.81-1.15 (all p<10^-29, all monotonic) ✓。Random 所有条件显著 (d_z=0.41-0.46, all p<10^-12)，与 DeepSeek/Qwen random 低 sparsity NS 模式定性不同。Imp/rand Δ ratio 2.0-2.6×（远低于 DS 15-17×）。Strategy specificity architecture-dependent。n=250 功效充分。 |\n| C9 | Differentiation from Lethe/SparK prior work | planned | Related Work §2 引用区分 + SparK gap analysis |\n| C10 | Phase gradient cross-benchmark robust; strategy specificity task-modulated | confirmed | GSM8K DS gradient 0.241→4.682 单调递增; QW gradient 0.039→2.092; imp/rand ratio 衰减至 2.3-3.8× (D075)。QW random s025+s030 均 success |\n| C11 | Phase-dependent severity absent under scoring-independent eviction (recency control) | confirmed | D102: 三个 sparsity level 全部 NS。s015+s025 为 primary evidence (n=100 each, both d_z < 0.1, p > 0.5); s030 supplementary (numerical instability at extreme sparsity)。对比 importance: d_z=0.574-1.15, ratio=119.8×。Triple dissociation confirmed: importance 有 gradient, recency + random 均 NS。排除 (a) phase segmentation circularity (b) H2O scoring pathway confound。文献中无先例将 recency eviction 作为 methodological control (experimental design contribution)。 |\n| S3→C | Onset threshold is model-dependent (DeepSeek s≥0.15, Qwen s≥0.20) | confirmed | D037/D038: Qwen s015 d_z=0.37 CI含0, s020+ 显著 |\n| S7→C | Dose-response monotonicity (Spearman ρ=1.0) | confirmed | D047: 6-point dose-response, 单调递增 |\n\n## Anticipated Reviewer Concerns\n\n### RC1: Generalizability — 7B models only, benchmark scope\n- **预期质疑**: \\\"Results on two 7B models and MATH-500 only. How do we know this generalizes to larger models or other reasoning tasks?\\\"\n- **应对**: 四层泛化证据：(1) Cross-model: DeepSeek-R1-Distill-Qwen-7B + Qwen2.5-7B-Instruct（同架构不同训练，ρ=1.0）(2) Cross-architecture: c8_llama_n250_fixed (DeepSeek-R1-Distill-Llama-8B, LlamaForCausalLM, n=250)，within-importance phase gradient 强 (d_z=0.81-1.15)，但 strategy specificity 弱于 Qwen2 架构（2.0-2.6× vs 15-17×），strategy×phase 交互强度 architecture-dependent (3) **Cross-benchmark (D075)**: GSM8K（两模型）phase gradient 单调递增复现（DS: 0.241→4.682; QW: 0.039→2.092），但 strategy specificity ratio 从 MATH-500 15-17× 衰减至 2.3-3.8×，表明 phase modulation 跨 benchmark 稳健而 magnitude modulation task-dependent。Limitations 诚实声明：(a) 7B scale only；(b) strategy specificity 强度 task-dependent（GSM8K 衰减，可能因推理链更短）；(c) random phase gradient 行为 architecture-dependent。\n- **实验支撑**: C5 (cross-model) + C8 (c8_llama_n250_fixed cross-architecture, n=250) + C10 (cross-benchmark GSM8K, D075)\n\n### RC2: Methodology — phase segmentation circularity and scoring confound\n- **预期质疑**: \\\"Your phase segmentation uses perplexity computed from the same model whose sparsity you're measuring. Isn't this circular? And H2O's attention-score mechanism could itself create the phase gradient artifact.\\\"\n- **应对**: Recency-based eviction (scoring-independent control, D102 confirmed) produces null phase gradient across all three sparsity levels (s015+s025 primary, s030 supplementary), confirming the observed severity pattern is specific to attention-score-based methods, not an artifact of (a) phase segmentation itself or (b) the scoring computation pathway. Triple dissociation: importance shows gradient (d_z=0.574+), recency and random both NS. Novel experimental design: repurposing recency eviction as methodological control has no precedent in literature (H2O/StreamingLLM use it only as performance baseline).\n- **实验支撑**: C11 (recency_s015/s025/s030, D102 confirmed) + c4_entropy (discrimination collapse mechanism, D044)\n\n### RC3: Practical impact — 没有 throughput 数据\n- **预期质疑**: \\\"No wall-clock or throughput measurements. Is the severity amplification reflected in actual inference speed?\\\"\n- **应对**: 本文定位是 empirical finding paper（发现 + 机制解释），不是 method paper。Throughput 不是 claim 的一部分。Discussion 中明确 phase-gated controller 作为 future direction。\n  - C5b pilot 已完成（D056）：oracle recovery 18%（Wilcoxon p=0.002），heuristic recovery 32%（p=0.024），但两者 95% CI 均跨零。方向正确（Wilcoxon 显著）但效应量不足（未达 30% gate），需更精细的 phase boundary estimation。论文 §6 Discussion 诚实报告 pilot 结果 + future work。\n  - Heuristic > oracle 悖论值得提及：token position ratio 粗粒度划分可能恰好更适合 mitigation 场景，暗示 phase boundary 的最优粒度是开放问题。\n- **实验支撑**: c5b_pilot (gate_failed, D056)\n\n### RC4: Statistical rigor — bootstrap 是否足够\n- **预期质疑**: \\\"Per-problem bootstrap with 50 problems — sufficient sample size?\\\"\n- **应对**: bf16 使用 B=10000 per-problem paired bootstrap，有效配对数 n=49 (DeepSeek) / n=46 (Qwen)；n=500 实验进一步验证 (C7 confirmed)。Permutation test 使用 paired median difference 作为 robust statistic（D032），Bonferroni 校正后全 4 水平 p<0.005。Dose-response 主用 Wilcoxon signed-rank p + median_diff（robust to outliers），Cohen's d 作为辅助效应量（DeepSeek 0.61→1.13, Qwen 0.37→1.44, registry cohens_d s015→s030），注释高 sparsity 下 d 受 outlier-driven variance 影响（DS s020→s025: median 3.3× jump 但 d 非单调，因极端 II 值影响分母，D064）。可在 appendix 补充 per-problem 分布图（已生成 fig4_per_problem_dist.pdf）。\n- **实验支撑**: bf16 permutation test (D032) + Cohen's d per-problem paired (rebootstrap B=10000) + n=500 Wilcoxon (C7 confirmed)\n\n### RC5: Novelty — prior work 是否已覆盖 phase-dependent sparsity\n- **预期质疑**: \"ThinKV and phase-aware methods already consider phase. What's new?\"\n- **应对**: Prior work 在单轴上分析 phase（ThinKV: phase-aware eviction）或 compound（SparK: joint compression）。没有工作同时分析 compound × phase × strategy 的三维交互。Crossover 现象（同一 strategy 在不同 phase 方向反转）是全新发现。Related Work 加 Lethe 引用区分 + SparK 对比。具体区分：\n  - **ThinKV** (arxiv 2510.01290, Oct 2025): 在 KV cache 单轴上做 phase-aware 压缩（按 CoT 阶段差异化 eviction），但不涉及 pruning × eviction 的 compound interaction。我们研究的是双轴（head pruning × KV eviction）compound interaction 如何随 phase 变化，ThinKV 的单轴 phase-aware 策略是我们分析维度的子集。\n  - **Physics of KV Cache Compression** (arxiv 2603.01426, Mar 2026): 揭示了单轴 KV 压缩的 phase transition 和 representational rigidity，是机制层面最接近的工作。关键区分：他们刻画的是单一压缩轴上压缩率的 critical threshold（phase transition），我们刻画的是两种压缩方法的 compound interaction severity 如何被 reasoning phase 调制（phase-dependent gradient）——维度正交。\n  - **HIES** (arxiv 2510.13832, Oct 2025): 发现 importance score collapse 并提出 entropy 补偿，为我们的 discrimination collapse 机制提供独立 supporting evidence——他们在单轴上观察到的 score collapse 正是我们在 compound setting 中发现的 Gini/CV 下降的单轴对应。\n  - **R-KV** (arxiv 2505.24133, May 2025): 针对 reasoning task 做 KV compression 优化，属于 task-specific method。我们不是提出新方法，而是 mechanistic 分析 compound interaction 的 phase-dependent 行为，二者目标不同（optimization vs understanding）。\n- **实验支撑**: C3 (crossover), Related Work §2 的 gap 分析\n\n### RC6: Novelty vs Lethe/SparK\n- **预期质疑**: \"How does this differ from Lethe (AAAI 2026) which also does layer-time-adaptive KV pruning, or SparK which studies compound compression?\"\n- **应对**: Lethe 和 SparK 都没有分析 phase × strategy 的交互效应。Lethe 是 method paper（提出 adaptive eviction 方法），我们是 empirical finding paper（发现 phase-dependent severity gradient）。SparK 研究 compound compression 但将 interaction 视为均匀超可加，我们发现 interaction severity 随 phase 和 strategy 变化。新近工作进一步确认我们的独特定位：\n  - **Physics of KV Cache Compression** (arxiv 2603.01426, Mar 2026) 是最近的相关工作，研究单轴压缩的 phase transition 阈值行为。与我们的核心区别：他们的 phase transition 是压缩率维度上的 critical point，我们的 phase-dependent gradient 是 reasoning phase 维度上 compound interaction 的连续调制——两者刻画的 \"phase\" 语义不同（compression-rate phase vs reasoning phase）。\n  - **ThinKV** (arxiv 2510.01290, Oct 2025) 和 **R-KV** (arxiv 2505.24133, May 2025) 都在 KV compression 单轴上引入 phase/reasoning awareness，但均未涉及 compound interaction。我们的贡献在于揭示 pruning × eviction 双轴交互如何被 reasoning phase 调制，这是单轴方法无法观察到的涌现现象。\n  - **HIES** (arxiv 2510.13832, Oct 2025) 的 importance score collapse 发现为我们的 discrimination collapse 机制提供了独立佐证，但 HIES 聚焦于单轴补偿方法，未研究 collapse 在 compound setting 中的放大效应。\n  - Related Work §2 明确区分三者定位：Lethe/SparK = method/compound method, ThinKV/R-KV = single-axis phase-aware, Physics of KV = single-axis phase transition, HIES = single-axis collapse。我们 = compound × phase × strategy 三维交互分析。\n- **实验支撑**: 不需要额外实验，仅需 §2 引用区分\n\n## Paper Positioning\n\n**类型**: Empirical finding paper（非 method paper）\n**核心贡献**:\n1. 发现 compound sparsity severity 的 strategy × phase 交互\n2. 量化 severity gradient（bf16 paired median difference 0.39→8.48, Cohen's d 0.61→1.13）和 crossover 现象\n3. 提出 discrimination collapse 机制解释（Gini/CV 跨模型一致；entropy redistribution model-dependent）\n4. Cross-model + cross-architecture (LLaMA, n=250) replication 验证泛化性（三模型两架构；strategy×phase 交互强度 architecture-dependent, D060）\n5. Novel use of scoring-independent eviction (recency-based) as methodological control — experimental design contribution 排除 phase segmentation circularity 和 scoring pathway confound (C11, D102 confirmed)\n\n**投稿目标**: EMNLP 2026 ARR, deadline 2026-05-25\n**Rebuttal 准备**: Day 9 (2026-05-23) 预留 rebuttal letter 写作时间\n**关键时间线**：\n- Day 9 (2026-05-23): 预留写 rebuttal letter\n- Day 11 (2026-05-25): EMNLP 2026 ARR 截稿\n\n\n## experiment_plan (with registry status)\n\n- id: c1_bf16_importance_s025\n  claim: C1\n  description: 'II median: high=0.032, mid=1.118, low=7.196; importance masking shows\n    strong phase gradient'\n  registry_id: bf16_importance_s025\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics: &id003\n    interaction_index:\n      high:\n        mean: 0.302756\n        median: 0.032363\n        ci:\n        - 0.083714\n        - 0.543977\n        winsorized_mean: 0.200962\n        skewness: 4.8826\n      mid:\n        mean: 5.729665\n        median: 1.118069\n        ci:\n        - 3.455574\n        - 8.471799\n        winsorized_mean: 4.189902\n        skewness: 8.2799\n      low:\n        mean: 25.852951\n        median: 7.195958\n        ci:\n        - 19.077082\n        - 33.497293\n        winsorized_mean: 19.319103\n        skewness: 7.3986\n    per_problem_ii_stats:\n      high:\n        n: 49\n        min: -0.316321\n        max: 4.003714\n        mean: 0.133714\n        median: 0.009873\n        std: 0.595358\n      mid:\n        n: 40\n        min: -0.024794\n        max: 18.720486\n        mean: 2.537744\n        median: 1.05707\n        std: 3.962575\n      low:\n        n: 50\n        min: -1.854733\n        max: 75.467653\n        mean: 11.28281\n        median: 3.954593\n        std: 16.620011\n    gradient_paired_aggregate_legacy: 222.35\n    median_difference: 7.1636\n    n_problems: 50\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: false\n      overall: PASS\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    perplexity:\n      high:\n        dense: 1.1689\n        attn: 1.6511\n        kv: 1.8628\n        both: 2.7026\n      mid:\n        dense: 1.2269\n        attn: 1.7039\n        kv: 5.6205\n        both: 13.3436\n      low:\n        dense: 1.2286\n        attn: 1.8366\n        kv: 31.756\n        both: 63.668\n- id: c1_bf16_ds_rand_s025\n  claim: C1\n  description: 'Random II median: high=0.818, mid=0.932, low=1.363; flat gradient\n    vs importance'\n  registry_id: bf16_ds_rand_s025\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 3.59\n        median: 0.8182\n        ci:\n        - 1.4021\n        - 6.2327\n        median_ci:\n        - 0.5075\n        - 1.7217\n        winsorized_mean: 6.3965\n        skewness: -7.57\n      mid:\n        mean: -1.8455\n        median: 0.9324\n        ci:\n        - -10.3663\n        - 4.9342\n        median_ci:\n        - 0.7331\n        - 1.7003\n        winsorized_mean: 3.1014\n        skewness: -12.76\n      low:\n        mean: 0.7212\n        median: 1.3627\n        ci:\n        - -4.2068\n        - 4.5006\n        median_ci:\n        - 1.0869\n        - 2.6866\n        winsorized_mean: 4.1866\n        skewness: -15.85\n    perplexity:\n      high:\n        dense: 1.1687\n        attn: 7.237\n        kv: 4.9751\n        both: 17.7423\n      mid:\n        dense: 1.2269\n        attn: 868.3199\n        kv: 5.1165\n        both: 29.4661\n      low:\n        dense: 1.2284\n        attn: 24.3571\n        kv: 6.7993\n        both: 17.9694\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    n_problems: 50\n    pass_fail:\n      ci_overlap: false\n      sign_reversal: false\n      overall: FAIL\n    median_difference: 0.5445\n- id: c1_bf16_qw_imp_s025\n  claim: C1\n  description: 'Qwen cross-model: median_diff=1.109, Cohen''s d=1.233, p<1e-5'\n  registry_id: bf16_qw_imp_s025\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics:\n    median_difference: 1.108706\n    permutation_p: 0\n    cohens_d: 1.2329\n    bootstrap_ci_95:\n    - 0.609247\n    - 1.469002\n    wilcoxon_p: 0\n    n_bootstrap: 10000\n    n_paired: 46\n- id: c1_sf5_asymmetric_spot\n  claim: C1\n  description: 'Asymmetric configs: h02_kv03 D=19.13, h03_kv02 D=18.25; gradient consistent'\n  registry_id: sf5_asymmetric_spot\n  role: ablation\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics:\n    config_a_h02_kv03:\n      II_low: 19.51\n      II_mid: 6.05\n      II_high: 0.38\n      D: 19.13\n    config_b_h03_kv02:\n      II_low: 18.77\n      II_mid: 3.97\n      II_high: 0.52\n      D: 18.25\n    pre_registered_criterion_passed: true\n    gradient_direction: II_low >> II_mid >> II_high (consistent with symmetric baseline)\n- id: c1_c2_accuracy_eval\n  claim: C1\n  description: 'DS dense->s030 acc: 0.52->0.10 (-0.42); QW dense->s030: 0.32->0.14\n    (-0.18)'\n  registry_id: c2_accuracy_eval\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics:\n    n_problems: 50\n    ds_dense_acc: 0.52\n    ds_s015_acc: 0.36\n    ds_s015_delta: -0.16\n    ds_s030_acc: 0.1\n    ds_s030_delta: -0.42\n    qw_dense_acc: 0.32\n    qw_s015_acc: 0.34\n    qw_s015_delta: 0.02\n    qw_s030_acc: 0.14\n    qw_s030_delta: -0.18\n    ds_s030_chinese_reasoning_rate: 0.4\n    ds_dense_truncation_rate: 0.56\n    note: v2 rescored with fixed radical+degree matcher. DS s015 34→36, QW s015 32→34\n- id: c2_bf16_importance_s030\n  claim: C2\n  description: 'Phase gradient: II low=14.64 >> mid=2.28 >> high=0.053 (median); low/high\n    ratio ~276x'\n  registry_id: bf16_importance_s030\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics: &id001\n    interaction_index:\n      high:\n        mean: 0.5547\n        median: 0.0534\n        ci:\n        - 0.2773\n        - 0.9198\n        winsorized_mean: 0.3367\n        skewness: 10.62\n      mid:\n        mean: 11.3\n        median: 2.2833\n        ci:\n        - 6.865\n        - 17.2633\n        winsorized_mean: 8.1752\n        skewness: 9.19\n      low:\n        mean: 57.7946\n        median: 14.6395\n        ci:\n        - 41.4416\n        - 77.0467\n        winsorized_mean: 39.3143\n        skewness: 8.31\n    per_problem_ii_stats:\n      high:\n        n: 49\n        min: -0.5095\n        max: 4.4457\n        mean: 0.1976\n        median: 0.0343\n        std: 0.6793\n      mid:\n        n: 40\n        min: -0.1989\n        max: 34.0258\n        mean: 5.2585\n        median: 1.5173\n        std: 7.9382\n      low:\n        n: 50\n        min: -7.3027\n        max: 126.7985\n        mean: 22.6601\n        median: 9.9731\n        std: 28.4096\n    gradient_paired_aggregate_legacy: 57.24\n    median_difference: 14.5861\n    n_problems: 50\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: false\n      overall: PASS\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    perplexity:\n      high:\n        dense: 1.1689\n        attn: 1.7123\n        kv: 2.0544\n        both: 3.2372\n      mid:\n        dense: 1.2269\n        attn: 1.7894\n        kv: 9.4821\n        both: 24.2847\n      low:\n        dense: 1.2286\n        attn: 1.9347\n        kv: 51.6485\n        both: 122.61\n- id: c2_v6_importance_s030\n  claim: C2\n  description: II low_median=34.69, mid_median=7.27, high_median=0.88; bootstrap_gradient=41.92,\n    CI=[19.14,299.76]\n  registry_id: v6_importance_s030\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 0.8833\n    ii_mid_median: 7.2706\n    ii_low_median: 34.6937\n    ii_high_mean: 1.5151\n    ii_mid_mean: 78.8215\n    ii_low_mean: 1163.9677\n    per_problem_ii_count: 50\n    n_high: 40\n    n_mid: 22\n    n_low: 20\n    problems: 50\n    bootstrap_gradient_paired: 41.92\n    bootstrap_ci_paired:\n    - 19.14\n    - 299.76\n    bootstrap_gradient_unpaired: 39.28\n    bootstrap_ci_unpaired:\n    - 21.87\n    - 129.59\n    bootstrap_p: 0\n- id: c2_think_phase_validation\n  claim: C2\n  description: Phase segmentation kappa=0.887; thinking=57.8% low-sparsity, answer=62.7%\n    high-sparsity\n  registry_id: think_phase_validation\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics:\n    effective_n: 48\n    skipped_problems: 2\n    median_kappa: 0.887\n    thinking_in_low_sparsity_phase: 0.578\n    answer_in_high_sparsity_phase: 0.627\n    note: Phase segmentation based on dense model — 4 sparsity conditions share identical\n      phase boundaries, effective sample n=48 not n=192\n- id: c2_acc_qw_s030_n100\n  claim: C2\n  description: QW importance s030 accuracy=0.19 (n=100); dose-response monotonic decline\n    from dense=0.40\n  registry_id: acc_qw_s030_n100\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics:\n    batch1_correct: 7\n    batch1_total: 50\n    batch1_acc: 0.14\n    batch1_source: acc_qw_s030_b1_8k (v2, 8k tokens)\n    batch2_correct: 12\n    batch2_total: 50\n    batch2_acc: 0.24\n    combined_correct: 19\n    combined_total: 100\n    combined_acc: 0.19\n- id: c2_acc_ds_s015_8k_v2\n  claim: C2\n  description: DS s015 accuracy=0.48 vs dense=0.74; early onset of compound degradation\n  registry_id: acc_ds_s015_8k_v2\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.48\n    correct: 24\n    total: 50\n    truncation_rate: 0.32\n    truncated_count: 16\n    non_truncated_accuracy: 0.706\n    non_truncated_correct: 24\n    non_truncated_total: 34\n    wall_time_s: 3967\n    max_new_tokens: 8192\n- id: c3_v6_importance_s025\n  claim: C3\n  description: 'Importance: II low_median=24.16 >> high_median=0.66; strong phase\n    gradient (36x ratio)'\n  registry_id: v6_importance_s025\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 0.6641\n    ii_mid_median: 5.3067\n    ii_low_median: 24.1619\n    ii_high_mean: 0.8842\n    ii_mid_mean: 10.057\n    ii_low_mean: 71.8854\n    per_problem_ii_count: 50\n    n_high: 42\n    n_mid: 23\n    n_low: 21\n    problems: 50\n    bootstrap_gradient_paired: 35.72\n    bootstrap_ci_paired:\n    - 9.52\n    - 101.54\n    bootstrap_gradient_unpaired: 36.38\n    bootstrap_ci_unpaired:\n    - 13.19\n    - 97.61\n    bootstrap_p: 0\n- id: c3_v6_random_s025\n  claim: C3\n  description: 'Random: II low_median=2.91 ~ high_median=3.00; flat phase gradient\n    (bootstrap_p=0.559)'\n  registry_id: v6_random_s025\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 3.0024\n    ii_mid_median: 2.9846\n    ii_low_median: 2.9146\n    ii_high_mean: 3.9052\n    ii_mid_mean: 7.9491\n    ii_low_mean: 3.9114\n    per_problem_ii_count: 50\n    n_high: 36\n    n_mid: 25\n    n_low: 24\n    bootstrap_gradient_paired: -0.1199\n    bootstrap_ci_paired:\n    - -1.517\n    - 1.2461\n    bootstrap_p: 0.559\n    bootstrap_gradient_unpaired: -0.8616\n    bootstrap_ci_unpaired:\n    - -3.3911\n    - 1.5169\n    per_problem_ii_stats:\n      high:\n        min: -6.1388\n        max: 25.2471\n        mean: 4.4098\n        median: 3.0421\n        std: 6.0734\n      mid:\n        min: 0.158\n        max: 108.7242\n        mean: 7.5626\n        median: 2.1407\n        std: 20.926\n      low:\n        min: -0.1953\n        max: 12.8555\n        mean: 3.5806\n        median: 2.7289\n        std: 3.4915\n    verdict: FAIL\n- id: c3_bf16_importance_s020\n  claim: C3\n  description: 'Importance: II low=1.50, mid=0.20, high=0.015 (median); clear phase\n    separation'\n  registry_id: bf16_importance_s020\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics: &id002\n    interaction_index:\n      high:\n        mean: 0.1289\n        median: 0.0145\n        ci:\n        - -0.1975\n        - 0.6647\n        winsorized_mean: -0.0297\n        skewness: 16.67\n      mid:\n        mean: 1.2604\n        median: 0.2027\n        ci:\n        - 0.7466\n        - 1.8962\n        winsorized_mean: 0.766\n        skewness: 7.05\n      low:\n        mean: 6.0288\n        median: 1.4963\n        ci:\n        - 4.4671\n        - 7.9237\n        winsorized_mean: 4.3426\n        skewness: 6.01\n    per_problem_ii_stats:\n      high:\n        n: 49\n        min: -0.1884\n        max: 0.4196\n        mean: 0.0025\n        median: 0.0036\n        std: 0.0966\n      mid:\n        n: 40\n        min: -0.0519\n        max: 8.6969\n        mean: 0.6795\n        median: 0.1977\n        std: 1.4998\n      low:\n        n: 50\n        min: -1.6151\n        max: 22.6875\n        mean: 2.2301\n        median: 1.128\n        std: 4.3758\n    gradient_paired_aggregate_legacy: 5.9\n    median_difference: 1.4818\n    n_problems: 50\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: false\n      overall: PASS\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    perplexity:\n      high:\n        dense: 1.1689\n        attn: 1.5233\n        kv: 1.6191\n        both: 2.1047\n      mid:\n        dense: 1.2269\n        attn: 1.5375\n        kv: 3.5164\n        both: 5.4246\n      low:\n        dense: 1.2286\n        attn: 1.6486\n        kv: 15.7987\n        both: 23.74\n- id: c3_bf16_ds_rand_s020\n  claim: C3\n  description: 'Random: II high=0.292, mid=0.350, low=0.276 (median); no phase separation'\n  registry_id: bf16_ds_rand_s020\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 1.1216\n        median: 0.2918\n        ci:\n        - 0.0796\n        - 2.5834\n        median_ci:\n        - 0.1598\n        - 0.4581\n        winsorized_mean: 1.7664\n        skewness: 9.59\n      mid:\n        mean: -1.5827\n        median: 0.3504\n        ci:\n        - -6.0963\n        - 1.5735\n        median_ci:\n        - 0.1993\n        - 0.5226\n        winsorized_mean: 0.5839\n        skewness: -12.31\n      low:\n        mean: -0.4116\n        median: 0.2763\n        ci:\n        - -2.6034\n        - 1.209\n        median_ci:\n        - 0.2194\n        - 0.5487\n        winsorized_mean: 0.9942\n        skewness: -10.07\n    perplexity:\n      high:\n        dense: 1.1687\n        attn: 3.1905\n        kv: 3.8002\n        both: 8.8129\n      mid:\n        dense: 1.2269\n        attn: 67.8504\n        kv: 3.788\n        both: 11.4974\n      low:\n        dense: 1.2284\n        attn: 8.592\n        kv: 5.0078\n        both: 9.2001\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    n_problems: 50\n    pass_fail:\n      ci_overlap: false\n      sign_reversal: false\n      overall: FAIL\n    median_difference: -0.0155\n- id: c4_c4_entropy\n  claim: C4\n  description: 'DS importance entropy_delta: -0.04 to -0.05 (collapse); random: +0.13\n    to +0.23 (redistribution). Gini_delta: -0.03 to -0.08'\n  registry_id: c4_entropy\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics:\n    importance_entropy_delta:\n      s015: -0.0402\n      s020: -0.0472\n      s025: -0.0446\n      s030: -0.0436\n    random_entropy_delta:\n      s015: 0.1283\n      s020: 0.136\n      s025: 0.2171\n      s030: 0.2327\n    importance_gini_delta:\n      s015: -0.0301\n      s020: -0.0404\n      s025: -0.0647\n      s030: -0.0806\n    random_gini_delta:\n      s015: -0.0309\n      s020: -0.0403\n      s025: -0.062\n      s030: -0.0732\n    importance_cv_delta:\n      s015: -0.564\n      s020: -0.774\n      s025: -1.287\n      s030: -1.665\n    random_cv_delta:\n      s015: -1.021\n      s020: -1.203\n      s025: -1.923\n      s030: -2.137\n    problems_completed: 30\n    runtime_minutes: 69.1\n- id: c4_qwen_c4_entropy\n  claim: C4\n  description: 'QW importance entropy_delta mixed: s015=-0.073, s025=+0.045; Gini\n    weaker (-0.01 to -0.02). Model-dependent pattern'\n  registry_id: qwen_c4_entropy\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: negative\n  metrics:\n    problems_completed: 30\n    qwen_importance_entropy_delta:\n      s015: -0.0733\n      s020: -0.0759\n      s025: 0.0451\n      s030: -0.0072\n    qwen_random_entropy_delta:\n      s015: 0.0838\n      s020: 0.0901\n      s025: 0.2168\n      s030: 0.1968\n    qwen_importance_gini_delta:\n      s015: -0.0103\n      s020: -0.0121\n      s025: -0.01\n      s030: -0.0202\n    qwen_random_gini_delta:\n      s015: -0.0186\n      s020: -0.0229\n      s025: -0.0337\n      s030: -0.0448\n    qwen_importance_cv_delta:\n      s015: -0.045\n      s020: -0.208\n      s025: -1.491\n      s030: -1.142\n    qwen_random_cv_delta:\n      s015: -0.778\n      s020: -0.889\n      s025: -1.5\n      s030: -1.677\n    cross_model_notes: random entropy increase consistent; importance entropy collapse\n      inconsistent at s025 (reversed to +0.045) and near-zero at s030; gini/cv directions\n      consistent but Qwen magnitudes smaller\n- id: c5_bf16_qw_imp_s030\n  claim: C5\n  description: 'Qwen: median_diff=2.619, Cohen''s d=1.439, p<1e-5; replicates DeepSeek\n    pattern'\n  registry_id: bf16_qw_imp_s030\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics:\n    median_difference: 2.619385\n    permutation_p: 0\n    cohens_d: 1.4394\n    bootstrap_ci_95:\n    - 1.722281\n    - 3.651063\n    wilcoxon_p: 0\n    n_bootstrap: 10000\n    n_paired: 46\n- id: c5_bf16_importance_s030\n  claim: C5\n  description: 'DeepSeek: II low_median=14.64, high_median=0.053; strong phase gradient'\n  registry_id: bf16_importance_s030\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics: *id001\n- id: c5_c2_n500_deepseek\n  claim: C5\n  description: 'DS n=500: imp_s030 median_II=8.48, CI=[7.46,9.56], p=1.3e-78; robust\n    at scale'\n  registry_id: c2_n500_deepseek\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics: &id004\n    n_problems: 500\n    effective_n: 496\n    mid_null_rate: 0.102\n    imp_s015_median_ii: 0.3907\n    imp_s015_ci:\n    - 0.3496\n    - 0.4431\n    imp_s015_wilcoxon_p: 1.27e-70\n    imp_s020_median_ii: 1.2149\n    imp_s020_ci:\n    - 1.1072\n    - 1.3365\n    imp_s020_wilcoxon_p: 3.98e-75\n    imp_s025_median_ii: 3.9857\n    imp_s025_ci:\n    - 3.5272\n    - 4.3588\n    imp_s025_wilcoxon_p: 1.99e-78\n    imp_s030_median_ii: 8.4813\n    imp_s030_ci:\n    - 7.7543\n    - 9.6919\n    imp_s030_wilcoxon_p: 1.09e-79\n    rand_s015_median_ii: 0.0139\n    rand_s015_wilcoxon_p: 0.863\n    rand_s020_median_ii: 0.0315\n    rand_s020_wilcoxon_p: 0.28\n    rand_s025_median_ii: 0.2574\n    rand_s025_bonf_p: 0.005839\n    rand_s025_fdr_p: 0.001914\n    rand_s030_median_ii: 0.5096\n    rand_s030_bonf_p: 0.005903\n    rand_s030_fdr_p: 0.001914\n    dz_s015_s020: -0.925\n    dz_s020_s025: -0.824\n    dz_s025_s030: -0.773\n    dz_s015_s030: -0.944\n    all_dz_reliable: true\n    dose_response_monotonic: true\n    dose_response_spearman_rho: 1\n    dose_response_perm_p: 0.0417\n    imp_rand_ratio_range: 15.5-38.6x\n    bonferroni_k: 4\n    bonferroni_note: Bonferroni k=4 family-wise (D066 revision)\n- id: c5_c2_qw_n500_r3\n  claim: C5\n  description: 'QW n=500: imp_s030 median_II=4.33, p<1e-40; cross-model replication\n    at high power'\n  registry_id: c2_qw_n500_r3\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics: &id005\n    n_problems: 500\n    effective_n: 475\n    filter: low+high valid only (mid-null allowed)\n    mid_null_rate: 0.452\n    imp_s015_median_ii: 0.0659\n    imp_s015_ci:\n    - 0.0492\n    - 0.0925\n    imp_s015_wilcoxon_p: 8.66e-15\n    imp_s015_bonf_p: 3.46e-14\n    imp_s020_median_ii: 0.3073\n    imp_s020_ci:\n    - 0.2612\n    - 0.3564\n    imp_s020_wilcoxon_p: 6.84e-42\n    imp_s020_bonf_p: 2.74e-41\n    imp_s025_median_ii: 1.0745\n    imp_s025_ci:\n    - 0.9766\n    - 1.1787\n    imp_s025_wilcoxon_p: 1.06e-68\n    imp_s025_bonf_p: 4.25e-68\n    imp_s030_median_ii: 3.155\n    imp_s030_ci:\n    - 2.7834\n    - 3.5582\n    imp_s030_wilcoxon_p: 9.21e-74\n    imp_s030_bonf_p: 3.69e-73\n    rand_s015_median_ii: -0.0111\n    rand_s015_wilcoxon_p: 0.172\n    rand_s015_bonf_p: 0.687\n    rand_s020_median_ii: 0.0153\n    rand_s020_wilcoxon_p: 0.2\n    rand_s020_bonf_p: 0.8\n    rand_s025_median_ii: 0.3931\n    rand_s025_wilcoxon_p: 1.59e-11\n    rand_s025_bonf_p: 6.37e-11\n    rand_s025_fdr_p: 2.63e-11\n    rand_s030_median_ii: 0.9127\n    rand_s030_wilcoxon_p: 2.92e-15\n    rand_s030_bonf_p: 1.17e-14\n    rand_s030_fdr_p: 5.61e-15\n    dz_s015_s020: -0.629\n    dz_s020_s025: -0.865\n    dz_s025_s030: -0.767\n    dz_s015_s030: -0.923\n    all_dz_reliable: true\n    dose_response_monotonic: true\n    dose_response_spearman_rho: 1\n    dose_response_perm_p: 0.0417\n    imp_rand_ratio_range: 2.7-20.1x\n    bonferroni_k: 4\n    bonferroni_note: Bonferroni k=4 family-wise (D066 revision)\n- id: c5b_c5b_pilot\n  claim: C5b\n  description: 'Oracle recovery=18% (gate: >30% FAIL); heuristic recovery=31.7% but\n    CI crosses zero. s030 incomplete'\n  registry_id: c5b_pilot\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: negative\n  metrics:\n    s025_uniform_median_ii: 1.0435\n    s025_oracle_median_ii: 0.856\n    s025_oracle_recovery_pct: 18\n    s025_oracle_recovery_ci:\n    - -39\n    - 45.8\n    s025_oracle_wilcoxon_p: 0.0021\n    s025_heuristic_median_ii: 0.7127\n    s025_heuristic_recovery_pct: 31.7\n    s025_heuristic_recovery_ci:\n    - -22.8\n    - 66\n    s025_heuristic_wilcoxon_p: 0.0236\n    gate_criterion: oracle_recovery > 30%\n    gate_result: FAIL\n    s030_status: not_completed\n    n_problems: 30\n- id: c6_bf16_importance_s015\n  claim: C6\n  description: II low_median=0.398 at s=0.15\n  registry_id: bf16_importance_s015\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: -0.150213\n        median: 0.005752\n        ci:\n        - -0.294614\n        - -0.055385\n        winsorized_mean: -0.062378\n        skewness: -14.9912\n      mid:\n        mean: 0.447301\n        median: 0.080738\n        ci:\n        - 0.267993\n        - 0.668749\n        winsorized_mean: 0.324751\n        skewness: 4.7221\n      low:\n        mean: 2.405837\n        median: 0.398291\n        ci:\n        - 1.478784\n        - 3.667675\n        winsorized_mean: 1.278857\n        skewness: 9.5402\n    per_problem_ii_stats:\n      high:\n        n: 49\n        min: -0.188061\n        max: 0.335853\n        mean: -0.013405\n        median: 0.00012\n        std: 0.078483\n      mid:\n        n: 40\n        min: -0.169092\n        max: 3.88198\n        mean: 0.308621\n        median: 0.107114\n        std: 0.690186\n      low:\n        n: 50\n        min: -0.872983\n        max: 9.10289\n        mean: 0.725504\n        median: 0.315517\n        std: 1.731056\n    gradient_paired_aggregate_legacy: 69.24\n    median_difference: 0.3925\n    n_problems: 50\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: true\n      overall: PASS\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    perplexity:\n      high:\n        dense: 1.1689\n        attn: 1.4861\n        kv: 1.4481\n        both: 1.5911\n      mid:\n        dense: 1.2269\n        attn: 1.5137\n        kv: 2.5971\n        both: 3.4541\n      low:\n        dense: 1.2286\n        attn: 1.6147\n        kv: 8.9201\n        both: 12.5084\n- id: c6_bf16_importance_s020\n  claim: C6\n  description: II low_median=1.496 at s=0.20\n  registry_id: bf16_importance_s020\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics: *id002\n- id: c6_bf16_importance_s025\n  claim: C6\n  description: II low_median=7.196 at s=0.25\n  registry_id: bf16_importance_s025\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics: *id003\n- id: c6_bf16_importance_s030\n  claim: C6\n  description: II low_median=14.64 at s=0.30; growth 0.40->1.50->7.20->14.64 is sub-exponential\n  registry_id: bf16_importance_s030\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics: *id001\n- id: c7_c2_n500_deepseek\n  claim: C7\n  description: 'DS n=500: all 4 sparsities significant (p<1e-70); CIs non-overlapping\n    across dose levels'\n  registry_id: c2_n500_deepseek\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics: *id004\n- id: c7_c2_qw_n500_r3\n  claim: C7\n  description: 'QW n=500: all 4 sparsities significant (p<1e-14 Bonferroni-corrected);\n    mid_null_rate=45.2%'\n  registry_id: c2_qw_n500_r3\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics: *id005\n- id: c8_c3_llama\n  claim: C8\n  description: LLaMA-8B (LlamaForCausalLM) replicates phase-modulated compound severity\n    from Qwen2ForCausalLM\n  registry_id: c3_llama\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics:\n    model: DeepSeek-R1-Distill-Llama-8B\n    n_problems: 50\n    n_valid: 49\n    n_skipped: 1\n    conditions_completed: 8/8\n    n_bootstrap: 10000\n    bonferroni_k: 4\n    imp_vs_rand_dz:\n      s015: 0.1923\n      s020: 0.255\n      s025: 0.2902\n      s030: 0.3352\n    imp_vs_rand_dz_ci:\n      s015:\n      - -0.0862\n      - 0.496\n      s020:\n      - -0.0248\n      - 0.5381\n      s025:\n      - 0.0081\n      - 0.6121\n      s030:\n      - 0.0606\n      - 0.6629\n    imp_vs_rand_dz_interpretation:\n      s015: negligible\n      s020: small\n      s025: small\n      s030: small\n    imp_vs_rand_dz_monotonic: true\n    phase_gradient_importance_dz:\n      s015: 1.0079\n      s020: 1.108\n      s025: 1.1227\n      s030: 1.0038\n    phase_gradient_importance_dz_ci:\n      s015:\n      - 0.593\n      - 1.7025\n      s020:\n      - 0.8144\n      - 1.5698\n      s025:\n      - 0.8735\n      - 1.5768\n      s030:\n      - 0.8099\n      - 1.3519\n    phase_gradient_importance_interpretation: all_large\n    phase_gradient_random_dz:\n      s015: 0.3497\n      s020: 0.373\n      s025: 0.4476\n      s030: 0.4385\n    phase_gradient_random_dz_ci:\n      s015:\n      - 0.0665\n      - 0.6916\n      s020:\n      - 0.0868\n      - 0.7335\n      s025:\n      - 0.1669\n      - 0.7698\n      s030:\n      - 0.1966\n      - 0.707\n    phase_gradient_random_interpretation: all_small\n    median_diff:\n      s015: 0.0203\n      s020: 0.0221\n      s025: 0.0947\n      s030: 0.3562\n    median_diff_ci:\n      s015:\n      - 0.0016\n      - 0.0435\n      s020:\n      - -0.0905\n      - 0.187\n      s025:\n      - -0.0037\n      - 0.3029\n      s030:\n      - -0.0691\n      - 0.5442\n    wilcoxon_p:\n      s015: 0.0549\n      s020: 0.0632\n      s025: 0.0209\n      s030: 0.0074\n    wilcoxon_p_bonferroni:\n      s015: 0.2195\n      s020: 0.2527\n      s025: 0.0834\n      s030: 0.0294\n    significant_bonferroni:\n      s015: false\n      s020: false\n      s025: false\n      s030: true\n    cross_arch_comparison:\n      deepseek_importance_dz:\n        s015: 0.4416\n        s020: 0.5195\n        s025: 0.6831\n        s030: 0.8031\n      llama_importance_dz:\n        s015: 1.0079\n        s020: 1.108\n        s025: 1.1227\n        s030: 1.0038\n      delta:\n        s015: 0.5663\n        s020: 0.5885\n        s025: 0.4396\n        s030: 0.2007\n      note: LLaMA shows uniformly large d_z (all >1.0) vs DeepSeek medium-to-large\n- id: c10_gsm8k_profiling_ds\n  claim: C10\n  description: 'DS GSM8K importance gradient: s015=0.241, s020=0.740, s025=1.992,\n    s030=4.636 (monotonic)'\n  registry_id: gsm8k_profiling_ds\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics:\n    version: v3_median\n    n_problems: 50\n    method: median + Wilcoxon + bootstrap_median(B=10000)\n    importance:\n      s015:\n        median_gradient: 0.241\n        ci_low: 0.077\n        ci_high: 0.478\n        wilcoxon_p: 0.0003\n      s020:\n        median_gradient: 0.74\n        ci_low: 0.314\n        ci_high: 1.119\n        wilcoxon_p: 0.0001\n      s025:\n        median_gradient: 1.992\n        ci_low: 0.933\n        ci_high: 2.82\n        wilcoxon_p: 0.0001\n      s030:\n        median_gradient: 4.682\n        ci_low: 2.121\n        ci_high: 10.557\n        wilcoxon_p: 0.0001\n    imp_rand_ratio:\n      s015: 2.3\n      s020: 2.5\n      s025: 3.8\n      s030: 2.8\n    dose_response_monotonic: true\n- id: c10_gsm8k_profiling_qw\n  claim: C10\n  description: 'QW GSM8K importance gradient: s015=0.039, s020=0.158, s025=1.100,\n    s030=2.092 (monotonic)'\n  registry_id: gsm8k_profiling_qw\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics:\n    version: v3_median\n    n_problems: 50\n    method: median + Wilcoxon + bootstrap_median(B=10000)\n    importance:\n      s015:\n        median_gradient: 0.039\n      s020:\n        median_gradient: 0.158\n      s025:\n        median_gradient: 1.1\n      s030:\n        median_gradient: 2.092\n    qw_rand_s030: INVALID\n- id: c10_gsm8k_qw_rand_s025_v2\n  claim: C10\n  description: 'QW random s025 GSM8K: II median_high=0.72, low=1.48; phase gradient\n    weaker than importance'\n  registry_id: gsm8k_qw_rand_s025_v2\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics:\n    verdict: PASS\n    n_problems: 50\n    n_bootstrap: 1000\n    seed: 42\n    high_sparsity:\n      n_segments: 216\n      n_tokens: 9326\n      ppl_dense: 1.0695\n      ppl_attn: 5.9362\n      ppl_kv: 3.4316\n      ppl_both: 15.7484\n      ii_mean: 6.5954\n      ii_ci:\n      - 1.1114\n      - 11.3791\n      ii_median: 0.7176\n      ii_median_ci:\n      - 0.5959\n      - 0.9347\n      winsorized_mean: 6.5046\n      skewness: -4.6807\n      outlier_count: 3\n    low_sparsity:\n      n_segments: 252\n      n_tokens: 29224\n      ppl_dense: 1.1972\n      ppl_attn: 11.5347\n      ppl_kv: 5.6038\n      ppl_both: 21.6874\n      ii_mean: 2.3883\n      ii_ci:\n      - -8.4602\n      - 11.029\n      ii_median: 1.4587\n      ii_median_ci:\n      - 1.1121\n      - 2.0451\n      winsorized_mean: 5.8911\n      skewness: -7.6074\n      outlier_count: 4\n    mid_sparsity:\n      n_segments: 51\n      n_tokens: 5954\n      ppl_dense: 1.2601\n      ppl_attn: 13.4132\n      ppl_kv: 6.4841\n      ppl_both: 20.8714\n      ii_mean: 4.5407\n      ii_ci:\n      - -4.8854\n      - 12.4605\n      ii_median: 1.1272\n      ii_median_ci:\n      - 0.637\n      - 3.3729\n      winsorized_mean: 6.3284\n      skewness: -3.4048\n      outlier_count: 1\n- id: c10_gsm8k_qw_rand_s030_v2\n  claim: C10\n  description: 'QW random s030 GSM8K: II median_high=2.31, low=5.87; compound effect\n    on GSM8K confirmed'\n  registry_id: gsm8k_qw_rand_s030_v2\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics:\n    verdict: PASS\n    n_problems: 50\n    n_bootstrap: 1000\n    seed: 42\n    high_sparsity:\n      n_segments: 216\n      n_tokens: 9326\n      null_ratio: 2/50\n      ppl_dense: 1.0695\n      ppl_attn: 6.5613\n      ppl_kv: 4.481\n      ppl_both: 23.7486\n      ii_mean: 11.83\n      ii_median: 2.31\n      ii_ci:\n      - 6.17\n      - 17.04\n      ii_median_ci:\n      - 1.64\n      - 2.81\n      winsorized_mean: 10.55\n      skewness: -2.29\n      outlier_count: 7\n    low_sparsity:\n      n_segments: 252\n      n_tokens: 29224\n      null_ratio: 5/50\n      ppl_dense: 1.1972\n      ppl_attn: 6.3283\n      ppl_kv: 8.5374\n      ppl_both: 56.2304\n      ii_mean: 31.26\n      ii_median: 5.2\n      ii_ci:\n      - 17.84\n      - 47.86\n      ii_median_ci:\n      - 3.95\n      - 7.24\n      winsorized_mean: 16.35\n      skewness: 7.57\n      outlier_count: 4\n    mid_sparsity:\n      n_segments: 51\n      n_tokens: 5954\n      null_ratio: 17/50\n      ppl_dense: 1.2601\n      ppl_attn: 18.6162\n      ppl_kv: 11.6625\n      ppl_both: 47.9019\n      ii_mean: 18.02\n      ii_median: 2.7\n      ii_ci:\n      - 0.09\n      - 36.69\n      ii_median_ci:\n      - 1.46\n      - 8.77\n      winsorized_mean: 18.22\n      skewness: 0.43\n      outlier_count: 2\n- id: s3_c_bf16_ds_imp_s010\n  claim: S3->C\n  description: 'DS s=0.10: II_high_median=0.003, verdict=FAIL; below onset threshold\n    for DeepSeek'\n  registry_id: bf16_ds_imp_s010\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: negative\n  metrics:\n    verdict: FAIL\n    problems: 50\n    II_high_sparsity_median: 0.0027\n    II_high_sparsity_mean: -0.1998\n    II_low_sparsity_median: 0.0151\n    II_low_sparsity_mean: -0.1066\n    II_mid_sparsity_median: 0.0061\n    II_mid_sparsity_mean: -0.0131\n    high_sparsity_tokens: 21086\n    low_sparsity_tokens: 27748\n    mid_sparsity_tokens: 13306\n- id: s3_c_bf16_qw_imp_s010\n  claim: S3->C\n  description: 'QW s=0.10: overall_verdict=PASS, CI_overlap_test=PASS; Qwen onset\n    earlier than DeepSeek'\n  registry_id: bf16_qw_imp_s010\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics:\n    n_problems: 50\n    overall_verdict: PASS\n    ci_overlap_test: PASS\n    sign_reversal_test: FAIL\n    high_sparsity_II_median: 0.0001\n    high_sparsity_II_median_CI:\n    - -0.0028\n    - 0.0005\n    high_sparsity_II_mean: -0.0887\n    high_sparsity_II_mean_CI:\n    - -0.1235\n    - -0.0591\n    low_sparsity_II_median: -0.0444\n    low_sparsity_II_median_CI:\n    - -0.0967\n    - -0.0152\n    low_sparsity_II_mean: -0.2431\n    low_sparsity_II_mean_CI:\n    - -0.3817\n    - -0.1202\n    mid_sparsity_II_median: -0.0359\n    mid_sparsity_II_median_CI:\n    - -0.0963\n    - -0.015\n    mid_sparsity_II_mean: -0.084\n    mid_sparsity_II_mean_CI:\n    - -0.1366\n    - -0.035\n    ppl_high_dense: 1.074\n    ppl_high_both: 1.228\n    ppl_low_dense: 1.152\n    ppl_low_both: 3.204\n    ppl_mid_dense: 1.133\n    ppl_mid_both: 1.741\n- id: s3_c_bf16_qw_imp_s015\n  claim: S3->C\n  description: 'QW s=0.15: median_diff=0.048, permutation_p=0.0001; confirmed above\n    threshold'\n  registry_id: bf16_qw_imp_s015\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics:\n    median_difference: 0.047619\n    permutation_p: 0.0001\n    cohens_d: 0.3705\n    bootstrap_ci_95:\n    - -0.005077\n    - 0.109517\n    wilcoxon_p: 0.02958\n    n_bootstrap: 10000\n    n_paired: 46\n- id: s7_c_c2_n500_deepseek\n  claim: S7->C\n  description: 'DS n=500 monotonic: imp median II 0.39->1.21->3.99->8.48 across s015-s030\n    (Spearman rho=1.0)'\n  registry_id: c2_n500_deepseek\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics: *id004\n- id: s7_c_c2_qw_n500_r3\n  claim: S7->C\n  description: 'QW n=500 monotonic: imp median II 0.066->0.307->1.075->4.33 across\n    s015-s030 (Spearman rho=1.0)'\n  registry_id: c2_qw_n500_r3\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics: *id005\n- id: s7_c_bf16_qw_imp_s035\n  claim: S7->C\n  description: 'QW s=0.35: low_II_median=8.24; extends dose-response beyond s030'\n  registry_id: bf16_qw_imp_s035\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics:\n    n_problems: 50\n    overall_verdict: PASS\n    ci_overlap_test: PASS\n    sign_reversal_test: FAIL\n    high_sparsity_II_median: 0.0232\n    high_sparsity_II_median_CI:\n    - 0.0154\n    - 0.0383\n    high_sparsity_II_mean: 0.1643\n    high_sparsity_II_mean_CI:\n    - 0.0844\n    - 0.2495\n    low_sparsity_II_median: 8.2358\n    low_sparsity_II_median_CI:\n    - 6.1564\n    - 10.9231\n    low_sparsity_II_mean: 18.9673\n    low_sparsity_II_mean_CI:\n    - 14.5015\n    - 23.9752\n    mid_sparsity_II_median: 0.9577\n    mid_sparsity_II_median_CI:\n    - 0.171\n    - 3.5575\n    mid_sparsity_II_mean: 8.0734\n    mid_sparsity_II_mean_CI:\n    - 2.0224\n    - 16.8946\n    ppl_high_dense: 1.0738\n    ppl_high_both: 2.3435\n    ppl_low_dense: 1.1518\n    ppl_low_both: 58.0358\n    ppl_mid_dense: 1.1327\n    ppl_mid_both: 20.9912\n    high_sparsity_tokens: 16289\n    low_sparsity_tokens: 32227\n    mid_sparsity_tokens: 4372\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_interaction_index_profiling\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_ii_profiling_v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    mvp_verdict: PASS_technical_but_negative_hypothesis\n    ci_nonoverlap: true\n    sign_reversal: false\n    ii_reasoning_0.3: 17.79\n    ii_reasoning_0.3_ci:\n    - 4.09\n    - 38.76\n    ii_transition_0.3: 3.06\n    ii_transition_0.3_ci:\n    - 0.01\n    - 5.6\n    ii_reasoning_0.5: 468.9\n    ii_transition_0.5: 850.07\n    ii_execution_0.3: Inf\n    phase_distribution:\n      execution: 1.2%_25seg\n      reasoning: 8.1%_96seg\n      transition: 90.7%_192seg\n    total_tokens: 86207\n    all_ii_superadditive: true\n    amplitude_ratio_reas_vs_trans_0.3: 5.81\n    gmm_best_k: 5\n    gmm_means:\n    - 0.438\n    - 0.597\n    - 0.719\n    - 0.816\n    - 0.892\n    gmm_weights:\n    - 0.062\n    - 0.14\n    - 0.208\n    - 0.282\n    - 0.309\n    sparsity_global:\n      mean: 0.7653\n      std: 0.1364\n      median: 0.8004\n    quantile_boundaries:\n    - 0.7337\n    - 0.8482\n- exp_id: mvp_ii_profiling_v3\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    mvp_verdict: FAIL\n    ci_nonoverlap: false\n    sign_reversal: false\n    phase_distribution_balanced: true\n    ii_high_0.1:\n      mean: 0.2317\n      ci:\n      - 0.1338\n      - 0.3418\n    ii_low_0.1:\n      mean: 0.1711\n      ci:\n      - 0.0782\n      - 0.2768\n    ii_mid_0.1:\n      mean: 0.1607\n      ci:\n      - 0.0886\n      - 0.2489\n    ii_high_0.2:\n      mean: 2.1574\n      ci:\n      - 1.0605\n      - 3.5491\n    ii_low_0.2:\n      mean: 1.1294\n      ci:\n      - 0.4368\n      - 1.9593\n    ii_mid_0.2:\n      mean: 0.3049\n      ci:\n      - -1.0635\n      - 1.3044\n    total_tokens: 86207\n    no_nan_inf: true\n    segments:\n      high: 511\n      low: 454\n      mid: 391\n- exp_id: mvp_ii_profiling_v4\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_ii_profiling_v4b\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_ii_profiling_v4c\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_ii_profiling_v4d\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_ii_profiling_v4-random\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_v4a_r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_v4b_r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_v4c_r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_v4_random_r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp_v4_legacy_s01\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    II_high_0.1:\n      mean: -0.1097\n      ci_low: -0.8066\n      ci_high: 0.41\n    II_mid_0.1:\n      mean: -15.966\n      ci_low: -47.991\n      ci_high: 1.288\n    II_low_0.1:\n      mean: 0\n      ci_low: 0\n      ci_high: 0\n    ppl_high_dense: 1.1462\n    ppl_high_both: 22.1302\n    ppl_mid_dense: 1.1226\n    ppl_mid_both: 47.5856\n    verdict: FAIL\n- exp_id: mvp_v4_legacy_s02\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_0.2:\n      mean: 21.2856\n      ci:\n      - 0.0292\n      - 63.163\n    ii_mid_0.2:\n      mean: 21.8743\n      ci:\n      - 4.9863\n      - 41.785\n    ii_low_0.2:\n      mean: 0\n      ci:\n      - 0\n      - 0\n    ppl_high:\n      dense: 1.15\n      attn: 1.32\n      kv: 104.42\n      both: 63.41\n    ppl_mid:\n      dense: 1.12\n      attn: 1.29\n      kv: 324.16\n      both: 170.47\n    ppl_low:\n      dense: 1.11\n      attn: 1.3\n      kv: 1.11\n      both: 1.3\n    problems_completed: 50\n    phase_tokens:\n      high: 25862\n      mid: 27996\n      low: 32349\n    mvp_verdict: PASS\n- exp_id: mvp_v4_legacy_s03\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_0.3:\n      mean: -224.5\n      ci_crosses_zero: true\n    verdict: FAIL_ci_crosses_zero\n- exp_id: mvp_v4_legacy_s025\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_v4_legacy_s035\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_v4_float32_s030\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_v5_fixed_s020\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    ii_high: 0.5\n    ii_mid: 3.52\n    ii_low: 31.89\n    ii_high_ci:\n    - 0.41\n    - 0.62\n    ii_mid_ci:\n    - 2.29\n    - 5.35\n    ii_low_ci:\n    - 18.74\n    - 47.22\n    ii_high_median: 0.33\n    ii_mid_median: 1.55\n    ii_low_median: 9.56\n    kv_ppl_high: 1.24\n    kv_ppl_mid: 3.65\n    kv_ppl_low: 14.11\n    both_ppl_high: 2.7\n    both_ppl_mid: 8.13\n    both_ppl_low: 42.64\n    problems: 50\n    ⚠️_WARNING: pre-fix code, INVALIDATED. Results found on disk after kill but code\n      lacked conda activation fix. Do NOT cite these numbers.\n- exp_id: mvp_v5_fixed_s030\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    ii_high: 1.18\n    ii_mid: 168.53\n    ii_low: 1926.23\n    ii_high_ci:\n    - 0.86\n    - 1.6\n    ii_mid_ci:\n    - 36.91\n    - 348.21\n    ii_low_ci:\n    - 179.17\n    - 4062.57\n    ii_high_median: 0.6\n    ii_mid_median: 7.47\n    ii_low_median: 44.63\n    kv_ppl_high: 1.4\n    kv_ppl_mid: 15.11\n    kv_ppl_low: 40.79\n    both_ppl_high: 5.71\n    both_ppl_mid: 137.61\n    both_ppl_low: 963.2\n    problems: 50\n    ⚠️_WARNING: pre-fix code, INVALIDATED. Results found on disk after kill but code\n      lacked conda activation fix. Do NOT cite these numbers.\n- exp_id: mvp_v5_fixed_s015\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ii_high: 0.306\n    ii_mid: 1.274\n    ii_low: 8.786\n    ii_high_ci:\n    - 0.256\n    - 0.359\n    ii_mid_ci:\n    - 0.895\n    - 1.749\n    ii_low_ci:\n    - 5.294\n    - 12.684\n    ii_high_median: 0.205\n    ii_mid_median: 0.696\n    ii_low_median: 2.627\n    ii_high_winsorized: 0.289\n    ii_mid_winsorized: 1.139\n    ii_low_winsorized: 8.408\n    kv_ppl_high: 1.2147\n    kv_ppl_mid: 2.1276\n    kv_ppl_low: 6.7451\n    both_ppl_high: 2.2835\n    both_ppl_mid: 3.9408\n    both_ppl_low: 16.9987\n    problems: 50\n    segments: 1356\n- exp_id: mvp_v5_fixed_s025\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ii_high: 0.851\n    ii_mid: 9.306\n    ii_low: 96.715\n    ii_high_ci:\n    - 0.703\n    - 0.999\n    ii_mid_ci:\n    - 6.092\n    - 13.303\n    ii_low_ci:\n    - 59.642\n    - 143.188\n    ii_high_median: 0.584\n    ii_mid_median: 4.522\n    ii_low_median: 30.903\n    ii_high_winsorized: 0.802\n    ii_mid_winsorized: 8.156\n    ii_low_winsorized: 94.931\n    kv_ppl_high: 1.3108\n    kv_ppl_mid: 6.1778\n    kv_ppl_low: 23.8919\n    both_ppl_high: 3.4623\n    both_ppl_mid: 16.4148\n    both_ppl_low: 104.1749\n    problems: 50\n    segments: 1356\n- exp_id: mvp_v5_fixed_s020_r2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ii_high_median: 0.3333\n    ii_mid_median: 1.5479\n    ii_low_median: 9.5627\n    ii_high_mean: 0.5044\n    ii_mid_mean: 3.5155\n    ii_low_mean: 31.8937\n    ii_high_ci:\n    - 0.41\n    - 0.62\n    ii_mid_ci:\n    - 2.29\n    - 5.35\n    ii_low_ci:\n    - 18.74\n    - 47.22\n    kv_ppl_high: 1.24\n    kv_ppl_mid: 3.65\n    kv_ppl_low: 14.11\n    both_ppl_high: 2.7\n    both_ppl_mid: 8.13\n    both_ppl_low: 42.64\n    problems: 50\n- exp_id: mvp_v5_fixed_s030_r2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ii_high_median: 0.5964\n    ii_mid_median: 7.4671\n    ii_low_median: 44.6324\n    ii_high_mean: 1.1832\n    ii_mid_mean: 168.53\n    ii_low_mean: 1926.23\n    ii_high_ci:\n    - 0.86\n    - 1.6\n    ii_mid_ci:\n    - 36.91\n    - 348.21\n    ii_low_ci:\n    - 179.17\n    - 4062.57\n    kv_ppl_high: 1.4\n    kv_ppl_mid: 15.11\n    kv_ppl_low: 40.79\n    both_ppl_high: 5.71\n    both_ppl_mid: 137.61\n    both_ppl_low: 963.2\n    problems: 50\n- exp_id: mvp_v5_random_s015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 0.1606\n    ii_mid_median: 0.252\n    ii_low_median: 0.1831\n    ii_high_mean: 0.4563\n    ii_mid_mean: 0.5134\n    ii_low_mean: 0.4775\n    ii_high_ci:\n    - 0.12\n    - 0.77\n    ii_mid_ci:\n    - 0.34\n    - 0.74\n    ii_low_ci:\n    - 0.28\n    - 0.7\n    kv_ppl_high: 3.14\n    kv_ppl_mid: 2.91\n    kv_ppl_low: 3.61\n    both_ppl_high: 3.92\n    both_ppl_mid: 4.14\n    both_ppl_low: 4.71\n    problems: 50\n- exp_id: mvp_v5_random_s025\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 3.0024\n    ii_mid_median: 2.9846\n    ii_low_median: 2.9146\n    ii_high_mean: 3.9052\n    ii_mid_mean: 7.9491\n    ii_low_mean: 3.9114\n    ii_high_ci:\n    - 0.98\n    - 6.34\n    ii_mid_ci:\n    - 4.67\n    - 11.87\n    ii_low_ci:\n    - 2.71\n    - 5.24\n    kv_ppl_high: 6.39\n    kv_ppl_mid: 6.11\n    kv_ppl_low: 9.07\n    both_ppl_high: 17.06\n    both_ppl_mid: 15.38\n    both_ppl_low: 29.32\n    problems: 50\n- exp_id: mvp_v5_random_s020\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 0.321331\n    ii_mid_median: 0.455663\n    ii_low_median: 0.591916\n    ii_high_mean: 0.855584\n    ii_mid_mean: 1.258123\n    ii_low_mean: 0.956933\n    ii_high_ci:\n    - -0.124133\n    - 1.616883\n    ii_mid_ci:\n    - 0.674852\n    - 2.075565\n    ii_low_ci:\n    - 0.583856\n    - 1.413355\n    kv_ppl_high: 4.2537\n    kv_ppl_mid: 4.3064\n    kv_ppl_low: 5.4048\n    both_ppl_high: 7.9749\n    both_ppl_mid: 6.8553\n    both_ppl_low: 22.5868\n    problems: 50\n- exp_id: mvp_v5_random_s030\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 5.377512\n    ii_mid_median: 5.886454\n    ii_low_median: 3.776818\n    ii_high_mean: 22.734534\n    ii_mid_mean: 10.943319\n    ii_low_mean: 11.840449\n    ii_high_ci:\n    - 10.352118\n    - 42.551951\n    ii_mid_ci:\n    - 7.398611\n    - 14.765315\n    ii_low_ci:\n    - 4.097309\n    - 23.545273\n    kv_ppl_high: 8.1027\n    kv_ppl_mid: 8.5701\n    kv_ppl_low: 13.4922\n    both_ppl_high: 41.3452\n    both_ppl_mid: 24.1992\n    both_ppl_low: 68.5301\n    problems: 50\n- exp_id: v6_importance_s025\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 0.6641\n    ii_mid_median: 5.3067\n    ii_low_median: 24.1619\n    ii_high_mean: 0.8842\n    ii_mid_mean: 10.057\n    ii_low_mean: 71.8854\n    per_problem_ii_count: 50\n    n_high: 42\n    n_mid: 23\n    n_low: 21\n    problems: 50\n    bootstrap_gradient_paired: 35.72\n    bootstrap_ci_paired:\n    - 9.52\n    - 101.54\n    bootstrap_gradient_unpaired: 36.38\n    bootstrap_ci_unpaired:\n    - 13.19\n    - 97.61\n    bootstrap_p: 0\n- exp_id: v6_importance_s030\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 0.8833\n    ii_mid_median: 7.2706\n    ii_low_median: 34.6937\n    ii_high_mean: 1.5151\n    ii_mid_mean: 78.8215\n    ii_low_mean: 1163.9677\n    per_problem_ii_count: 50\n    n_high: 40\n    n_mid: 22\n    n_low: 20\n    problems: 50\n    bootstrap_gradient_paired: 41.92\n    bootstrap_ci_paired:\n    - 19.14\n    - 299.76\n    bootstrap_gradient_unpaired: 39.28\n    bootstrap_ci_unpaired:\n    - 21.87\n    - 129.59\n    bootstrap_p: 0\n- exp_id: v6_importance_s015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 0.2266\n    ii_mid_median: 0.7432\n    ii_low_median: 2.8762\n    ii_high_mean: 0.2874\n    ii_mid_mean: 1.6858\n    ii_low_mean: 8.5161\n    per_problem_ii_count: 50\n    n_high: 43\n    n_mid: 32\n    n_low: 24\n    problems: 50\n    bootstrap_gradient_paired: 11.53\n    bootstrap_ci_paired:\n    - 3.49\n    - 23.78\n    bootstrap_gradient_unpaired: 12.69\n    bootstrap_ci_unpaired:\n    - 4.96\n    - 28.45\n    bootstrap_p: 0\n- exp_id: v6_importance_s020\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 0.3353\n    ii_mid_median: 1.6733\n    ii_low_median: 9.2538\n    ii_high_mean: 0.4936\n    ii_mid_mean: 4.9538\n    ii_low_mean: 25.8764\n    per_problem_ii_count: 50\n    n_high: 42\n    n_mid: 28\n    n_low: 21\n    problems: 50\n    bootstrap_gradient_paired: 11.05\n    bootstrap_ci_paired:\n    - 5.42\n    - 69.27\n    bootstrap_gradient_unpaired: 27.6\n    bootstrap_ci_unpaired:\n    - 6.55\n    - 75.16\n    bootstrap_p: 0\n- exp_id: qwen_importance_s015\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: qwen_importance_s020\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: qwen_importance_s025\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: qwen_importance_s030\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: v6_random_s015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 0.1606\n    ii_mid_median: 0.252\n    ii_low_median: 0.1831\n    ii_high_mean: 0.4563\n    ii_mid_mean: 0.5134\n    ii_low_mean: 0.4775\n    per_problem_ii_count: 50\n    n_high: 43\n    n_mid: 32\n    n_low: 28\n    bootstrap_gradient_paired: -0.2722\n    bootstrap_ci_paired:\n    - -0.7039\n    - 0.1548\n    bootstrap_p: 0.903\n    bootstrap_gradient_unpaired: -0.0592\n    bootstrap_ci_unpaired:\n    - -0.5341\n    - 0.3877\n    per_problem_ii_stats:\n      high:\n        min: -3.0621\n        max: 5.018\n        mean: 0.5386\n        median: 0.2003\n        std: 1.2085\n      mid:\n        min: -2.7245\n        max: 4.6713\n        mean: 0.3977\n        median: 0.299\n        std: 1.1456\n      low:\n        min: -0.4031\n        max: 3.7005\n        mean: 0.4806\n        median: 0.2465\n        std: 0.779\n    verdict: FAIL\n- exp_id: v6_random_s020\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_mean: 0.855584\n    ii_high_median: 0.321331\n    ii_high_ci:\n    - -0.124133\n    - 1.616883\n    ii_high_winsorized_mean: 0.913496\n    ii_mid_mean: 1.258123\n    ii_mid_median: 0.455663\n    ii_mid_ci:\n    - 0.674852\n    - 2.075565\n    ii_mid_winsorized_mean: 1.074102\n    ii_low_mean: 0.956933\n    ii_low_median: 0.591916\n    ii_low_ci:\n    - 0.583856\n    - 1.413355\n    ii_low_winsorized_mean: 0.96113\n    n_high: 511\n    n_mid: 391\n    n_low: 454\n    problems: 50\n    per_problem_ii_count: 50\n    gradient_mean_low_over_high: 1.118\n    gradient_median_low_over_high: 1.842\n    pass_fail: FAIL\n    perplexity_high_dense: 1.1462\n    perplexity_high_both: 7.9749\n    perplexity_mid_dense: 1.1226\n    perplexity_mid_both: 6.8553\n    perplexity_low_dense: 1.1105\n    perplexity_low_both: 22.5868\n- exp_id: v6_random_s025\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 3.0024\n    ii_mid_median: 2.9846\n    ii_low_median: 2.9146\n    ii_high_mean: 3.9052\n    ii_mid_mean: 7.9491\n    ii_low_mean: 3.9114\n    per_problem_ii_count: 50\n    n_high: 36\n    n_mid: 25\n    n_low: 24\n    bootstrap_gradient_paired: -0.1199\n    bootstrap_ci_paired:\n    - -1.517\n    - 1.2461\n    bootstrap_p: 0.559\n    bootstrap_gradient_unpaired: -0.8616\n    bootstrap_ci_unpaired:\n    - -3.3911\n    - 1.5169\n    per_problem_ii_stats:\n      high:\n        min: -6.1388\n        max: 25.2471\n        mean: 4.4098\n        median: 3.0421\n        std: 6.0734\n      mid:\n        min: 0.158\n        max: 108.7242\n        mean: 7.5626\n        median: 2.1407\n        std: 20.926\n      low:\n        min: -0.1953\n        max: 12.8555\n        mean: 3.5806\n        median: 2.7289\n        std: 3.4915\n    verdict: FAIL\n- exp_id: v6_random_s030\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: v6_random_s030_r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: bf16_importance_s015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: -0.150213\n        median: 0.005752\n        ci:\n        - -0.294614\n        - -0.055385\n        winsorized_mean: -0.062378\n        skewness: -14.9912\n      mid:\n        mean: 0.447301\n        median: 0.080738\n        ci:\n        - 0.267993\n        - 0.668749\n        winsorized_mean: 0.324751\n        skewness: 4.7221\n      low:\n        mean: 2.405837\n        median: 0.398291\n        ci:\n        - 1.478784\n        - 3.667675\n        winsorized_mean: 1.278857\n        skewness: 9.5402\n    per_problem_ii_stats:\n      high:\n        n: 49\n        min: -0.188061\n        max: 0.335853\n        mean: -0.013405\n        median: 0.00012\n        std: 0.078483\n      mid:\n        n: 40\n        min: -0.169092\n        max: 3.88198\n        mean: 0.308621\n        median: 0.107114\n        std: 0.690186\n      low:\n        n: 50\n        min: -0.872983\n        max: 9.10289\n        mean: 0.725504\n        median: 0.315517\n        std: 1.731056\n    gradient_paired_aggregate_legacy: 69.24\n    median_difference: 0.3925\n    n_problems: 50\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: true\n      overall: PASS\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    perplexity:\n      high:\n        dense: 1.1689\n        attn: 1.4861\n        kv: 1.4481\n        both: 1.5911\n      mid:\n        dense: 1.2269\n        attn: 1.5137\n        kv: 2.5971\n        both: 3.4541\n      low:\n        dense: 1.2286\n        attn: 1.6147\n        kv: 8.9201\n        both: 12.5084\n- exp_id: bf16_importance_s020\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 0.1289\n        median: 0.0145\n        ci:\n        - -0.1975\n        - 0.6647\n        winsorized_mean: -0.0297\n        skewness: 16.67\n      mid:\n        mean: 1.2604\n        median: 0.2027\n        ci:\n        - 0.7466\n        - 1.8962\n        winsorized_mean: 0.766\n        skewness: 7.05\n      low:\n        mean: 6.0288\n        median: 1.4963\n        ci:\n        - 4.4671\n        - 7.9237\n        winsorized_mean: 4.3426\n        skewness: 6.01\n    per_problem_ii_stats:\n      high:\n        n: 49\n        min: -0.1884\n        max: 0.4196\n        mean: 0.0025\n        median: 0.0036\n        std: 0.0966\n      mid:\n        n: 40\n        min: -0.0519\n        max: 8.6969\n        mean: 0.6795\n        median: 0.1977\n        std: 1.4998\n      low:\n        n: 50\n        min: -1.6151\n        max: 22.6875\n        mean: 2.2301\n        median: 1.128\n        std: 4.3758\n    gradient_paired_aggregate_legacy: 5.9\n    median_difference: 1.4818\n    n_problems: 50\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: false\n      overall: PASS\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    perplexity:\n      high:\n        dense: 1.1689\n        attn: 1.5233\n        kv: 1.6191\n        both: 2.1047\n      mid:\n        dense: 1.2269\n        attn: 1.5375\n        kv: 3.5164\n        both: 5.4246\n      low:\n        dense: 1.2286\n        attn: 1.6486\n        kv: 15.7987\n        both: 23.74\n- exp_id: bf16_importance_s025\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 0.302756\n        median: 0.032363\n        ci:\n        - 0.083714\n        - 0.543977\n        winsorized_mean: 0.200962\n        skewness: 4.8826\n      mid:\n        mean: 5.729665\n        median: 1.118069\n        ci:\n        - 3.455574\n        - 8.471799\n        winsorized_mean: 4.189902\n        skewness: 8.2799\n      low:\n        mean: 25.852951\n        median: 7.195958\n        ci:\n        - 19.077082\n        - 33.497293\n        winsorized_mean: 19.319103\n        skewness: 7.3986\n    per_problem_ii_stats:\n      high:\n        n: 49\n        min: -0.316321\n        max: 4.003714\n        mean: 0.133714\n        median: 0.009873\n        std: 0.595358\n      mid:\n        n: 40\n        min: -0.024794\n        max: 18.720486\n        mean: 2.537744\n        median: 1.05707\n        std: 3.962575\n      low:\n        n: 50\n        min: -1.854733\n        max: 75.467653\n        mean: 11.28281\n        median: 3.954593\n        std: 16.620011\n    gradient_paired_aggregate_legacy: 222.35\n    median_difference: 7.1636\n    n_problems: 50\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: false\n      overall: PASS\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    perplexity:\n      high:\n        dense: 1.1689\n        attn: 1.6511\n        kv: 1.8628\n        both: 2.7026\n      mid:\n        dense: 1.2269\n        attn: 1.7039\n        kv: 5.6205\n        both: 13.3436\n      low:\n        dense: 1.2286\n        attn: 1.8366\n        kv: 31.756\n        both: 63.668\n- exp_id: bf16_importance_s030\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 0.5547\n        median: 0.0534\n        ci:\n        - 0.2773\n        - 0.9198\n        winsorized_mean: 0.3367\n        skewness: 10.62\n      mid:\n        mean: 11.3\n        median: 2.2833\n        ci:\n        - 6.865\n        - 17.2633\n        winsorized_mean: 8.1752\n        skewness: 9.19\n      low:\n        mean: 57.7946\n        median: 14.6395\n        ci:\n        - 41.4416\n        - 77.0467\n        winsorized_mean: 39.3143\n        skewness: 8.31\n    per_problem_ii_stats:\n      high:\n        n: 49\n        min: -0.5095\n        max: 4.4457\n        mean: 0.1976\n        median: 0.0343\n        std: 0.6793\n      mid:\n        n: 40\n        min: -0.1989\n        max: 34.0258\n        mean: 5.2585\n        median: 1.5173\n        std: 7.9382\n      low:\n        n: 50\n        min: -7.3027\n        max: 126.7985\n        mean: 22.6601\n        median: 9.9731\n        std: 28.4096\n    gradient_paired_aggregate_legacy: 57.24\n    median_difference: 14.5861\n    n_problems: 50\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: false\n      overall: PASS\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    perplexity:\n      high:\n        dense: 1.1689\n        attn: 1.7123\n        kv: 2.0544\n        both: 3.2372\n      mid:\n        dense: 1.2269\n        attn: 1.7894\n        kv: 9.4821\n        both: 24.2847\n      low:\n        dense: 1.2286\n        attn: 1.9347\n        kv: 51.6485\n        both: 122.61\n- exp_id: bf16_random_s015\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: bf16_random_s020\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: bf16_random_s025\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: bf16_random_s030\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: bf16_qwen_importance_s015\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: bf16_qwen_importance_s020\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: bf16_qwen_importance_s025\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: bf16_qwen_importance_s030\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: v6_random_s030_r3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    II_high_mean: 9.2364\n    II_mid_mean: -230.7604\n    II_low_mean: -7.4119\n    II_high_median: 4.0237\n    II_mid_median: 2.4272\n    II_low_median: 4.735\n    ppl_low_both: 88.94\n    per_problem_count: 50\n- exp_id: bf16_ds_imp_s015\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    median_difference: 0.323579\n    permutation_p: 0\n    cohens_d: 0.6068\n    bootstrap_ci_95:\n    - 0.198824\n    - 0.471566\n    wilcoxon_p: 0\n    n_bootstrap: 10000\n    n_paired: 49\n- exp_id: bf16_ds_imp_s020\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    median_difference: 1.15202\n    permutation_p: 0\n    cohens_d: 0.725\n    bootstrap_ci_95:\n    - 0.655454\n    - 1.256001\n    wilcoxon_p: 0\n    n_bootstrap: 10000\n    n_paired: 49\n- exp_id: bf16_ds_imp_s025\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    median_difference: 3.968568\n    permutation_p: 0\n    cohens_d: 0.9534\n    bootstrap_ci_95:\n    - 2.829037\n    - 5.291756\n    wilcoxon_p: 0\n    n_bootstrap: 10000\n    n_paired: 49\n- exp_id: bf16_ds_imp_s030\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    median_difference: 9.943595\n    permutation_p: 0\n    cohens_d: 1.1263\n    bootstrap_ci_95:\n    - 8.391554\n    - 16.652865\n    wilcoxon_p: 0\n    n_bootstrap: 10000\n    n_paired: 49\n- exp_id: bf16_ds_rand_s015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 0.2208\n        median: 0.0931\n        ci:\n        - -1.0091\n        - 1.5243\n        median_ci:\n        - 0.0024\n        - 0.1515\n        winsorized_mean: 0.3161\n        skewness: -5.4\n      mid:\n        mean: -3.3604\n        median: 0.0967\n        ci:\n        - -8.4057\n        - 0.3697\n        median_ci:\n        - 0.0219\n        - 0.197\n        winsorized_mean: -0.6366\n        skewness: -10.56\n      low:\n        mean: -1.8952\n        median: 0.1026\n        ci:\n        - -4.9698\n        - 0.2741\n        median_ci:\n        - 0.044\n        - 0.1755\n        winsorized_mean: 0.0521\n        skewness: -11.57\n    perplexity:\n      high:\n        dense: 1.1687\n        attn: 3.5947\n        kv: 2.9239\n        both: 5.7569\n      mid:\n        dense: 1.2269\n        attn: 297.7957\n        kv: 2.915\n        both: 11.3156\n      low:\n        dense: 1.2284\n        attn: 11.3419\n        kv: 3.6161\n        both: 6.2886\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    n_problems: 50\n    pass_fail:\n      ci_overlap: false\n      sign_reversal: false\n      overall: FAIL\n    median_difference: 0.0095\n- exp_id: bf16_ds_rand_s020\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 1.1216\n        median: 0.2918\n        ci:\n        - 0.0796\n        - 2.5834\n        median_ci:\n        - 0.1598\n        - 0.4581\n        winsorized_mean: 1.7664\n        skewness: 9.59\n      mid:\n        mean: -1.5827\n        median: 0.3504\n        ci:\n        - -6.0963\n        - 1.5735\n        median_ci:\n        - 0.1993\n        - 0.5226\n        winsorized_mean: 0.5839\n        skewness: -12.31\n      low:\n        mean: -0.4116\n        median: 0.2763\n        ci:\n        - -2.6034\n        - 1.209\n        median_ci:\n        - 0.2194\n        - 0.5487\n        winsorized_mean: 0.9942\n        skewness: -10.07\n    perplexity:\n      high:\n        dense: 1.1687\n        attn: 3.1905\n        kv: 3.8002\n        both: 8.8129\n      mid:\n        dense: 1.2269\n        attn: 67.8504\n        kv: 3.788\n        both: 11.4974\n      low:\n        dense: 1.2284\n        attn: 8.592\n        kv: 5.0078\n        both: 9.2001\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    n_problems: 50\n    pass_fail:\n      ci_overlap: false\n      sign_reversal: false\n      overall: FAIL\n    median_difference: -0.0155\n- exp_id: bf16_ds_rand_s025\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 3.59\n        median: 0.8182\n        ci:\n        - 1.4021\n        - 6.2327\n        median_ci:\n        - 0.5075\n        - 1.7217\n        winsorized_mean: 6.3965\n        skewness: -7.57\n      mid:\n        mean: -1.8455\n        median: 0.9324\n        ci:\n        - -10.3663\n        - 4.9342\n        median_ci:\n        - 0.7331\n        - 1.7003\n        winsorized_mean: 3.1014\n        skewness: -12.76\n      low:\n        mean: 0.7212\n        median: 1.3627\n        ci:\n        - -4.2068\n        - 4.5006\n        median_ci:\n        - 1.0869\n        - 2.6866\n        winsorized_mean: 4.1866\n        skewness: -15.85\n    perplexity:\n      high:\n        dense: 1.1687\n        attn: 7.237\n        kv: 4.9751\n        both: 17.7423\n      mid:\n        dense: 1.2269\n        attn: 868.3199\n        kv: 5.1165\n        both: 29.4661\n      low:\n        dense: 1.2284\n        attn: 24.3571\n        kv: 6.7993\n        both: 17.9694\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    n_problems: 50\n    pass_fail:\n      ci_overlap: false\n      sign_reversal: false\n      overall: FAIL\n    median_difference: 0.5445\n- exp_id: bf16_ds_rand_s030\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 7.5555\n        median: 2.5031\n        ci:\n        - 4.4087\n        - 11.6199\n        median_ci:\n        - 1.3292\n        - 4.1205\n        winsorized_mean: null\n        skewness: null\n      mid:\n        mean: 6.2518\n        median: 2.5918\n        ci:\n        - 2.1767\n        - 10.4757\n        median_ci:\n        - 1.8397\n        - 3.7888\n        winsorized_mean: null\n        skewness: null\n      low:\n        mean: 6.8323\n        median: 4.0414\n        ci:\n        - 3.2428\n        - 10.6996\n        median_ci:\n        - 2.2686\n        - 6.3579\n        winsorized_mean: null\n        skewness: null\n    perplexity:\n      high:\n        dense: 1.1687\n        attn: 16.7892\n        kv: 8.8073\n        both: 40.7553\n      mid:\n        dense: 1.2269\n        attn: 2461.9219\n        kv: 8.6662\n        both: 62.4422\n      low:\n        dense: 1.2284\n        attn: 55.2916\n        kv: 11.5789\n        both: 37.6009\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    n_problems: 50\n    pass_fail:\n      ci_overlap: false\n      sign_reversal: false\n      overall: FAIL\n    median_difference: 1.5383\n- exp_id: bf16_qw_imp_s015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    median_difference: 0.047619\n    permutation_p: 0.0001\n    cohens_d: 0.3705\n    bootstrap_ci_95:\n    - -0.005077\n    - 0.109517\n    wilcoxon_p: 0.02958\n    n_bootstrap: 10000\n    n_paired: 46\n- exp_id: bf16_qw_imp_s020\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    median_difference: 0.207511\n    permutation_p: 0\n    cohens_d: 0.7224\n    bootstrap_ci_95:\n    - 0.067222\n    - 0.40226\n    wilcoxon_p: 3.4e-05\n    n_bootstrap: 10000\n    n_paired: 46\n- exp_id: bf16_qw_imp_s025\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    median_difference: 1.108706\n    permutation_p: 0\n    cohens_d: 1.2329\n    bootstrap_ci_95:\n    - 0.609247\n    - 1.469002\n    wilcoxon_p: 0\n    n_bootstrap: 10000\n    n_paired: 46\n- exp_id: bf16_qw_imp_s030\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    median_difference: 2.619385\n    permutation_p: 0\n    cohens_d: 1.4394\n    bootstrap_ci_95:\n    - 1.722281\n    - 3.651063\n    wilcoxon_p: 0\n    n_bootstrap: 10000\n    n_paired: 46\n- exp_id: bf16_qw_rand_s015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 1.6652\n        median: 0.1381\n        ci:\n        - 1.0986\n        - 2.4042\n        median_ci:\n        - 0.1025\n        - 0.2074\n        winsorized_mean: 1.0044\n        skewness: 7.1842\n      mid:\n        mean: 1.6975\n        median: 0.2194\n        ci:\n        - 0.4473\n        - 3.4612\n        median_ci:\n        - -0.0048\n        - 0.6621\n        winsorized_mean: 1.4038\n        skewness: 3.2101\n      low:\n        mean: 1.4082\n        median: 0.1878\n        ci:\n        - 0.8358\n        - 2.06\n        median_ci:\n        - 0.0962\n        - 0.3139\n        winsorized_mean: 0.9403\n        skewness: 7.1113\n    perplexity:\n      high:\n        dense: 1.0737\n        attn: 1.3939\n        kv: 2.0487\n        both: 4.2076\n      mid:\n        dense: 1.1322\n        attn: 1.4175\n        kv: 2.3709\n        both: 4.6105\n      low:\n        dense: 1.1517\n        attn: 1.7177\n        kv: 3.3253\n        both: 5.4788\n    phase_stats:\n      high:\n        n_tokens: 16289\n        n_segments: 295\n      mid:\n        n_tokens: 4372\n        n_segments: 26\n      low:\n        n_tokens: 32227\n        n_segments: 276\n    n_problems: 50\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: false\n      overall: FAIL\n    median_difference: -0.029401\n    permutation_test:\n      p_value: 0.7657\n      B: 10000\n    cohens_d: -0.0507\n    bootstrap_ci_95:\n    - -0.2106\n    - 0.2124\n    wilcoxon_p: 0.862554\n    phase_median_ii:\n      high: 0.1381\n      mid: 0.2194\n      low: 0.1878\n- exp_id: bf16_qw_rand_s020\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 2.58579\n        median: 0.48549\n        ci:\n        - 1.769404\n        - 3.501692\n        median_ci:\n        - 0.304626\n        - 0.658814\n        winsorized_mean: 1.80021\n        skewness: 5.4038\n      mid:\n        mean: 5.69684\n        median: 0.76699\n        ci:\n        - 1.69004\n        - 12.276143\n        median_ci:\n        - 0.482838\n        - 3.392541\n        winsorized_mean: 4.304174\n        skewness: 3.526\n      low:\n        mean: 65.915714\n        median: 0.614438\n        ci:\n        - -18.581948\n        - 221.709429\n        median_ci:\n        - 0.484725\n        - 0.848787\n        winsorized_mean: 2.389244\n        skewness: 16.2163\n    perplexity:\n      high:\n        dense: 1.0737\n        attn: 1.6115\n        kv: 2.5041\n        both: 5.9394\n      mid:\n        dense: 1.1322\n        attn: 1.7583\n        kv: 3.0658\n        both: 10.5578\n      low:\n        dense: 1.1517\n        attn: 75.631\n        kv: 4.3535\n        both: 140.6269\n    phase_stats:\n      high:\n        n_tokens: 16289\n        n_segments: 295\n      mid:\n        n_tokens: 4372\n        n_segments: 26\n      low:\n        n_tokens: 32227\n        n_segments: 276\n    n_problems: 50\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: false\n      overall: FAIL\n    median_difference: 0.128948\n    permutation_test:\n      p_value: 0.352\n      B: 10000\n    cohens_d: 0.247\n    bootstrap_ci_95:\n    - -0.139\n    - 0.215\n    wilcoxon_p: 0.149\n    phase_median_ii:\n      high: 0.4739\n      mid: 0.8757\n      low: 0.4847\n- exp_id: bf16_qw_rand_s025\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 14.4213\n        median: 1.6043\n        ci:\n        - 7.1074\n        - 23.4587\n        median_ci:\n        - 0.6977\n        - 3.0736\n        winsorized_mean: 9.3765\n        skewness: 4.8263\n      mid:\n        mean: 18.6458\n        median: 2.2225\n        ci:\n        - 3.3729\n        - 41.6037\n        median_ci:\n        - 0.6093\n        - 11.5889\n        winsorized_mean: 14.2901\n        skewness: 3.8245\n      low:\n        mean: 17.7277\n        median: 2.2641\n        ci:\n        - 4.3523\n        - 37.2093\n        median_ci:\n        - 1.2218\n        - 4.8561\n        winsorized_mean: 9.9876\n        skewness: 5.7652\n    perplexity:\n      high:\n        dense: 1.0737\n        attn: 2.0183\n        kv: 3.1882\n        both: 9.7654\n      mid:\n        dense: 1.1322\n        attn: 2.3476\n        kv: 4.0124\n        both: 17.3298\n      low:\n        dense: 1.1517\n        attn: 2.7834\n        kv: 5.8762\n        both: 25.4321\n    phase_stats:\n      high:\n        n_tokens: 16289\n        n_segments: 295\n      mid:\n        n_tokens: 4372\n        n_segments: 26\n      low:\n        n_tokens: 32227\n        n_segments: 276\n    n_problems: 50\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: false\n      overall: FAIL\n    median_difference: 1.144074\n    permutation_test:\n      p_value: 0.1679\n      B: 10000\n    cohens_d: 0.1574\n    bootstrap_ci_95:\n    - -0.3166\n    - 4.1645\n    wilcoxon_p: 0.010313\n    phase_median_ii:\n      high: 1.6043\n      mid: 2.2225\n      low: 2.2641\n- exp_id: bf16_qw_rand_s030\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    median_high: 4.200557\n    median_mid: 6.477036\n    median_low: 8.065662\n    median_diff: 2.418272\n    permutation_p: 0.012\n    cohens_d: -0.03513\n    wilcoxon_p: 0.01566\n    bootstrap_ci_low: 0.241897\n    bootstrap_ci_high: 3.314824\n- exp_id: c4_entropy\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    importance_entropy_delta:\n      s015: -0.0402\n      s020: -0.0472\n      s025: -0.0446\n      s030: -0.0436\n    random_entropy_delta:\n      s015: 0.1283\n      s020: 0.136\n      s025: 0.2171\n      s030: 0.2327\n    importance_gini_delta:\n      s015: -0.0301\n      s020: -0.0404\n      s025: -0.0647\n      s030: -0.0806\n    random_gini_delta:\n      s015: -0.0309\n      s020: -0.0403\n      s025: -0.062\n      s030: -0.0732\n    importance_cv_delta:\n      s015: -0.564\n      s020: -0.774\n      s025: -1.287\n      s030: -1.665\n    random_cv_delta:\n      s015: -1.021\n      s020: -1.203\n      s025: -1.923\n      s030: -2.137\n    problems_completed: 30\n    runtime_minutes: 69.1\n- exp_id: qwen_c4_entropy\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    problems_completed: 30\n    qwen_importance_entropy_delta:\n      s015: -0.0733\n      s020: -0.0759\n      s025: 0.0451\n      s030: -0.0072\n    qwen_random_entropy_delta:\n      s015: 0.0838\n      s020: 0.0901\n      s025: 0.2168\n      s030: 0.1968\n    qwen_importance_gini_delta:\n      s015: -0.0103\n      s020: -0.0121\n      s025: -0.01\n      s030: -0.0202\n    qwen_random_gini_delta:\n      s015: -0.0186\n      s020: -0.0229\n      s025: -0.0337\n      s030: -0.0448\n    qwen_importance_cv_delta:\n      s015: -0.045\n      s020: -0.208\n      s025: -1.491\n      s030: -1.142\n    qwen_random_cv_delta:\n      s015: -0.778\n      s020: -0.889\n      s025: -1.5\n      s030: -1.677\n    cross_model_notes: random entropy increase consistent; importance entropy collapse\n      inconsistent at s025 (reversed to +0.045) and near-zero at s030; gini/cv directions\n      consistent but Qwen magnitudes smaller\n- exp_id: bf16_ds_imp_s010\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    verdict: FAIL\n    problems: 50\n    II_high_sparsity_median: 0.0027\n    II_high_sparsity_mean: -0.1998\n    II_low_sparsity_median: 0.0151\n    II_low_sparsity_mean: -0.1066\n    II_mid_sparsity_median: 0.0061\n    II_mid_sparsity_mean: -0.0131\n    high_sparsity_tokens: 21086\n    low_sparsity_tokens: 27748\n    mid_sparsity_tokens: 13306\n- exp_id: bf16_ds_imp_s035\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    verdict: PASS\n    problems: 50\n    II_high_sparsity_median: 0.1051\n    II_high_sparsity_mean: 1.4309\n    II_low_sparsity_median: 28.7649\n    II_low_sparsity_mean: 104.1892\n    II_mid_sparsity_median: 4.9542\n    II_mid_sparsity_mean: 20.326\n    high_sparsity_tokens: 21086\n    low_sparsity_tokens: 27748\n    mid_sparsity_tokens: 13306\n    ci_overlap_test: low_sparsity vs mid_sparsity CI non-overlapping at 0.35\n- exp_id: bf16_qw_imp_s010\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_problems: 50\n    overall_verdict: PASS\n    ci_overlap_test: PASS\n    sign_reversal_test: FAIL\n    high_sparsity_II_median: 0.0001\n    high_sparsity_II_median_CI:\n    - -0.0028\n    - 0.0005\n    high_sparsity_II_mean: -0.0887\n    high_sparsity_II_mean_CI:\n    - -0.1235\n    - -0.0591\n    low_sparsity_II_median: -0.0444\n    low_sparsity_II_median_CI:\n    - -0.0967\n    - -0.0152\n    low_sparsity_II_mean: -0.2431\n    low_sparsity_II_mean_CI:\n    - -0.3817\n    - -0.1202\n    mid_sparsity_II_median: -0.0359\n    mid_sparsity_II_median_CI:\n    - -0.0963\n    - -0.015\n    mid_sparsity_II_mean: -0.084\n    mid_sparsity_II_mean_CI:\n    - -0.1366\n    - -0.035\n    ppl_high_dense: 1.074\n    ppl_high_both: 1.228\n    ppl_low_dense: 1.152\n    ppl_low_both: 3.204\n    ppl_mid_dense: 1.133\n    ppl_mid_both: 1.741\n- exp_id: bf16_qw_imp_s035\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_problems: 50\n    overall_verdict: PASS\n    ci_overlap_test: PASS\n    sign_reversal_test: FAIL\n    high_sparsity_II_median: 0.0232\n    high_sparsity_II_median_CI:\n    - 0.0154\n    - 0.0383\n    high_sparsity_II_mean: 0.1643\n    high_sparsity_II_mean_CI:\n    - 0.0844\n    - 0.2495\n    low_sparsity_II_median: 8.2358\n    low_sparsity_II_median_CI:\n    - 6.1564\n    - 10.9231\n    low_sparsity_II_mean: 18.9673\n    low_sparsity_II_mean_CI:\n    - 14.5015\n    - 23.9752\n    mid_sparsity_II_median: 0.9577\n    mid_sparsity_II_median_CI:\n    - 0.171\n    - 3.5575\n    mid_sparsity_II_mean: 8.0734\n    mid_sparsity_II_mean_CI:\n    - 2.0224\n    - 16.8946\n    ppl_high_dense: 1.0738\n    ppl_high_both: 2.3435\n    ppl_low_dense: 1.1518\n    ppl_low_both: 58.0358\n    ppl_mid_dense: 1.1327\n    ppl_mid_both: 20.9912\n    high_sparsity_tokens: 16289\n    low_sparsity_tokens: 32227\n    mid_sparsity_tokens: 4372\n- exp_id: c2_n500_deepseek\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_problems: 500\n    effective_n: 496\n    mid_null_rate: 0.102\n    imp_s015_median_ii: 0.3907\n    imp_s015_ci:\n    - 0.3496\n    - 0.4431\n    imp_s015_wilcoxon_p: 1.27e-70\n    imp_s020_median_ii: 1.2149\n    imp_s020_ci:\n    - 1.1072\n    - 1.3365\n    imp_s020_wilcoxon_p: 3.98e-75\n    imp_s025_median_ii: 3.9857\n    imp_s025_ci:\n    - 3.5272\n    - 4.3588\n    imp_s025_wilcoxon_p: 1.99e-78\n    imp_s030_median_ii: 8.4813\n    imp_s030_ci:\n    - 7.7543\n    - 9.6919\n    imp_s030_wilcoxon_p: 1.09e-79\n    rand_s015_median_ii: 0.0139\n    rand_s015_wilcoxon_p: 0.863\n    rand_s020_median_ii: 0.0315\n    rand_s020_wilcoxon_p: 0.28\n    rand_s025_median_ii: 0.2574\n    rand_s025_bonf_p: 0.005839\n    rand_s025_fdr_p: 0.001914\n    rand_s030_median_ii: 0.5096\n    rand_s030_bonf_p: 0.005903\n    rand_s030_fdr_p: 0.001914\n    dz_s015_s020: -0.925\n    dz_s020_s025: -0.824\n    dz_s025_s030: -0.773\n    dz_s015_s030: -0.944\n    all_dz_reliable: true\n    dose_response_monotonic: true\n    dose_response_spearman_rho: 1\n    dose_response_perm_p: 0.0417\n    imp_rand_ratio_range: 15.5-38.6x\n    bonferroni_k: 4\n    bonferroni_note: Bonferroni k=4 family-wise (D066 revision)\n- exp_id: c3_llama_arch\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: c2_ds_n500\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: c2_qw_n500\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: c3_llama\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    model: DeepSeek-R1-Distill-Llama-8B\n    n_problems: 50\n    n_valid: 49\n    n_skipped: 1\n    conditions_completed: 8/8\n    n_bootstrap: 10000\n    bonferroni_k: 4\n    imp_vs_rand_dz:\n      s015: 0.1923\n      s020: 0.255\n      s025: 0.2902\n      s030: 0.3352\n    imp_vs_rand_dz_ci:\n      s015:\n      - -0.0862\n      - 0.496\n      s020:\n      - -0.0248\n      - 0.5381\n      s025:\n      - 0.0081\n      - 0.6121\n      s030:\n      - 0.0606\n      - 0.6629\n    imp_vs_rand_dz_interpretation:\n      s015: negligible\n      s020: small\n      s025: small\n      s030: small\n    imp_vs_rand_dz_monotonic: true\n    phase_gradient_importance_dz:\n      s015: 1.0079\n      s020: 1.108\n      s025: 1.1227\n      s030: 1.0038\n    phase_gradient_importance_dz_ci:\n      s015:\n      - 0.593\n      - 1.7025\n      s020:\n      - 0.8144\n      - 1.5698\n      s025:\n      - 0.8735\n      - 1.5768\n      s030:\n      - 0.8099\n      - 1.3519\n    phase_gradient_importance_interpretation: all_large\n    phase_gradient_random_dz:\n      s015: 0.3497\n      s020: 0.373\n      s025: 0.4476\n      s030: 0.4385\n    phase_gradient_random_dz_ci:\n      s015:\n      - 0.0665\n      - 0.6916\n      s020:\n      - 0.0868\n      - 0.7335\n      s025:\n      - 0.1669\n      - 0.7698\n      s030:\n      - 0.1966\n      - 0.707\n    phase_gradient_random_interpretation: all_small\n    median_diff:\n      s015: 0.0203\n      s020: 0.0221\n      s025: 0.0947\n      s030: 0.3562\n    median_diff_ci:\n      s015:\n      - 0.0016\n      - 0.0435\n      s020:\n      - -0.0905\n      - 0.187\n      s025:\n      - -0.0037\n      - 0.3029\n      s030:\n      - -0.0691\n      - 0.5442\n    wilcoxon_p:\n      s015: 0.0549\n      s020: 0.0632\n      s025: 0.0209\n      s030: 0.0074\n    wilcoxon_p_bonferroni:\n      s015: 0.2195\n      s020: 0.2527\n      s025: 0.0834\n      s030: 0.0294\n    significant_bonferroni:\n      s015: false\n      s020: false\n      s025: false\n      s030: true\n    cross_arch_comparison:\n      deepseek_importance_dz:\n        s015: 0.4416\n        s020: 0.5195\n        s025: 0.6831\n        s030: 0.8031\n      llama_importance_dz:\n        s015: 1.0079\n        s020: 1.108\n        s025: 1.1227\n        s030: 1.0038\n      delta:\n        s015: 0.5663\n        s020: 0.5885\n        s025: 0.4396\n        s030: 0.2007\n      note: LLaMA shows uniformly large d_z (all >1.0) vs DeepSeek medium-to-large\n- exp_id: c5b_pilot\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    s025_uniform_median_ii: 1.0435\n    s025_oracle_median_ii: 0.856\n    s025_oracle_recovery_pct: 18\n    s025_oracle_recovery_ci:\n    - -39\n    - 45.8\n    s025_oracle_wilcoxon_p: 0.0021\n    s025_heuristic_median_ii: 0.7127\n    s025_heuristic_recovery_pct: 31.7\n    s025_heuristic_recovery_ci:\n    - -22.8\n    - 66\n    s025_heuristic_wilcoxon_p: 0.0236\n    gate_criterion: oracle_recovery > 30%\n    gate_result: FAIL\n    s030_status: not_completed\n    n_problems: 30\n- exp_id: c2_qw_n500_r3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_problems: 500\n    effective_n: 475\n    filter: low+high valid only (mid-null allowed)\n    mid_null_rate: 0.452\n    imp_s015_median_ii: 0.0659\n    imp_s015_ci:\n    - 0.0492\n    - 0.0925\n    imp_s015_wilcoxon_p: 8.66e-15\n    imp_s015_bonf_p: 3.46e-14\n    imp_s020_median_ii: 0.3073\n    imp_s020_ci:\n    - 0.2612\n    - 0.3564\n    imp_s020_wilcoxon_p: 6.84e-42\n    imp_s020_bonf_p: 2.74e-41\n    imp_s025_median_ii: 1.0745\n    imp_s025_ci:\n    - 0.9766\n    - 1.1787\n    imp_s025_wilcoxon_p: 1.06e-68\n    imp_s025_bonf_p: 4.25e-68\n    imp_s030_median_ii: 3.155\n    imp_s030_ci:\n    - 2.7834\n    - 3.5582\n    imp_s030_wilcoxon_p: 9.21e-74\n    imp_s030_bonf_p: 3.69e-73\n    rand_s015_median_ii: -0.0111\n    rand_s015_wilcoxon_p: 0.172\n    rand_s015_bonf_p: 0.687\n    rand_s020_median_ii: 0.0153\n    rand_s020_wilcoxon_p: 0.2\n    rand_s020_bonf_p: 0.8\n    rand_s025_median_ii: 0.3931\n    rand_s025_wilcoxon_p: 1.59e-11\n    rand_s025_bonf_p: 6.37e-11\n    rand_s025_fdr_p: 2.63e-11\n    rand_s030_median_ii: 0.9127\n    rand_s030_wilcoxon_p: 2.92e-15\n    rand_s030_bonf_p: 1.17e-14\n    rand_s030_fdr_p: 5.61e-15\n    dz_s015_s020: -0.629\n    dz_s020_s025: -0.865\n    dz_s025_s030: -0.767\n    dz_s015_s030: -0.923\n    all_dz_reliable: true\n    dose_response_monotonic: true\n    dose_response_spearman_rho: 1\n    dose_response_perm_p: 0.0417\n    imp_rand_ratio_range: 2.7-20.1x\n    bonferroni_k: 4\n    bonferroni_note: Bonferroni k=4 family-wise (D066 revision)\n- exp_id: sf5_asymmetric_spot\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    config_a_h02_kv03:\n      II_low: 19.51\n      II_mid: 6.05\n      II_high: 0.38\n      D: 19.13\n    config_b_h03_kv02:\n      II_low: 18.77\n      II_mid: 3.97\n      II_high: 0.52\n      D: 18.25\n    pre_registered_criterion_passed: true\n    gradient_direction: II_low >> II_mid >> II_high (consistent with symmetric baseline)\n- exp_id: gsm8k_profiling_ds\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    version: v3_median\n    n_problems: 50\n    method: median + Wilcoxon + bootstrap_median(B=10000)\n    importance:\n      s015:\n        median_gradient: 0.241\n        ci_low: 0.077\n        ci_high: 0.478\n        wilcoxon_p: 0.0003\n      s020:\n        median_gradient: 0.74\n        ci_low: 0.314\n        ci_high: 1.119\n        wilcoxon_p: 0.0001\n      s025:\n        median_gradient: 1.992\n        ci_low: 0.933\n        ci_high: 2.82\n        wilcoxon_p: 0.0001\n      s030:\n        median_gradient: 4.682\n        ci_low: 2.121\n        ci_high: 10.557\n        wilcoxon_p: 0.0001\n    imp_rand_ratio:\n      s015: 2.3\n      s020: 2.5\n      s025: 3.8\n      s030: 2.8\n    dose_response_monotonic: true\n- exp_id: gsm8k_profiling_qw\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    version: v3_median\n    n_problems: 50\n    method: median + Wilcoxon + bootstrap_median(B=10000)\n    importance:\n      s015:\n        median_gradient: 0.039\n      s020:\n        median_gradient: 0.158\n      s025:\n        median_gradient: 1.1\n      s030:\n        median_gradient: 2.092\n    qw_rand_s030: INVALID\n- exp_id: think_phase_validation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    effective_n: 48\n    skipped_problems: 2\n    median_kappa: 0.887\n    thinking_in_low_sparsity_phase: 0.578\n    answer_in_high_sparsity_phase: 0.627\n    note: Phase segmentation based on dense model — 4 sparsity conditions share identical\n      phase boundaries, effective sample n=48 not n=192\n- exp_id: r9c2-spike\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: r9c2-spike-v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: r9c2-spike-v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: c2_accuracy_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_problems: 50\n    ds_dense_acc: 0.52\n    ds_s015_acc: 0.36\n    ds_s015_delta: -0.16\n    ds_s030_acc: 0.1\n    ds_s030_delta: -0.42\n    qw_dense_acc: 0.32\n    qw_s015_acc: 0.34\n    qw_s015_delta: 0.02\n    qw_s030_acc: 0.14\n    qw_s030_delta: -0.18\n    ds_s030_chinese_reasoning_rate: 0.4\n    ds_dense_truncation_rate: 0.56\n    note: v2 rescored with fixed radical+degree matcher. DS s015 34→36, QW s015 32→34\n- exp_id: acc_ds_s020\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ds_s020_acc: 0.26\n    ds_s020_acc_v2: 0.26\n    ds_s020_correct: 13\n    ds_s020_total: 50\n    ds_s020_delta_vs_dense: -0.26\n    output_truncated_count: 32\n    output_truncated_rate: 0.64\n    extraction_failure_count: 31\n    extraction_failure_rate: 0.62\n    total_time_s: 1560\n    note: v2 rescored with fixed radical+degree matcher; 0 changes. Dense baseline=0.52\n- exp_id: acc_ds_s025\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy: 0.08\n    correct: 4\n    total: 50\n    null_count: 37\n    null_rate: 0.74\n    output_truncated_count: 38\n    output_truncated_rate: 0.76\n    wrong_count: 9\n    wrong_rate: 0.18\n    extraction_failure_count: 1\n    extraction_failure_rate: 0.02\n    total_time_s: 1670.5\n    heads_pruned: 196\n    delta_vs_dense: -0.44\n- exp_id: acc_qw_s020\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    qw_s020_acc: 0.26\n    qw_s020_correct: 13\n    qw_s020_total: 50\n    qw_s020_delta_vs_dense: -0.06\n    null_count: 2\n    null_rate: 0.04\n    output_truncated_count: 2\n    output_truncated_rate: 0.04\n    extraction_failure_count: 0\n    extraction_failure_rate: 0\n    wrong_count: 35\n    wrong_rate: 0.7\n    heads_pruned: 140\n    total_time_s: 598\n    note: v2 rescored with fixed radical+degree matcher\n- exp_id: acc_qw_s025\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    qw_s025_acc: 0.32\n    qw_s025_correct: 16\n    qw_s025_total: 50\n    qw_s025_delta_vs_dense: 0\n    null_count: 8\n    null_rate: 0.16\n    output_truncated_count: 2\n    output_truncated_rate: 0.04\n    extraction_failure_count: 6\n    extraction_failure_rate: 0.12\n    wrong_count: 26\n    wrong_rate: 0.52\n    heads_pruned: 196\n    total_time_s: 559\n    note: v2 rescored with fixed radical+degree matcher; 3 problems flipped (sqrt+degree)\n- exp_id: acc_qw_s020_n100\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    batch1_acc: 0.26\n    batch1_correct: 13\n    batch1_total: 50\n    batch1_source: acc_qw_s020_b1_8k (v2, 8k tokens)\n    batch2_acc: 0.46\n    batch2_correct: 23\n    batch2_total: 50\n    combined_acc: 0.36\n    combined_correct: 36\n    combined_total: 100\n    note: 'batch effect: batch1=26% vs batch2=46%, Δ=20pp'\n- exp_id: acc_qw_s025_n100\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    batch1_acc: 0.32\n    batch1_correct: 16\n    batch1_total: 50\n    batch1_source: acc_qw_s025_b1_8k (v2, 8k tokens)\n    batch2_acc: 0.34\n    batch2_correct: 17\n    batch2_total: 50\n    combined_acc: 0.33\n    combined_correct: 33\n    combined_total: 100\n- exp_id: acc_ds_dense_8k\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: acc_ds_s015_8k\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: acc_ds_s020_8k\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: acc_ds_s025_8k\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: acc_ds_s030_8k\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: acc_qw_dense_n100\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    batch1_correct: 22\n    batch1_total: 50\n    batch1_acc: 0.44\n    batch1_source: acc_qw_dense_b1_8k (v2, 8k tokens)\n    batch2_correct: 24\n    batch2_total: 50\n    batch2_acc: 0.48\n    combined_correct: 46\n    combined_total: 100\n    combined_acc: 0.46\n- exp_id: acc_qw_s015_n100\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    batch1_acc: 0.46\n    batch1_correct: 23\n    batch1_total: 50\n    batch1_source: acc_qw_s015_b1_8k (v2, 8k tokens)\n    batch2_acc: 0.38\n    batch2_correct: 19\n    batch2_total: 50\n    combined_acc: 0.42\n    combined_correct: 42\n    combined_total: 100\n- exp_id: acc_qw_s030_n100\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    batch1_correct: 7\n    batch1_total: 50\n    batch1_acc: 0.14\n    batch1_source: acc_qw_s030_b1_8k (v2, 8k tokens)\n    batch2_correct: 12\n    batch2_total: 50\n    batch2_acc: 0.24\n    combined_correct: 19\n    combined_total: 100\n    combined_acc: 0.19\n- exp_id: acc_ds_s015_8k_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.48\n    correct: 24\n    total: 50\n    truncation_rate: 0.32\n    truncated_count: 16\n    non_truncated_accuracy: 0.706\n    non_truncated_correct: 24\n    non_truncated_total: 34\n    wall_time_s: 3967\n    max_new_tokens: 8192\n- exp_id: acc_ds_s020_8k_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.3\n    correct: 15\n    total: 50\n    truncated_count: 28\n    truncated_rate: 0.56\n    extraction_failures: 1\n    non_truncated_accuracy: 0.682\n    non_truncated_correct: 15\n    non_truncated_total: 22\n    total_time_seconds: 5549\n    max_new_tokens: 8192\n- exp_id: acc_ds_s025_8k_v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy: 0.08\n    correct: 4\n    total: 50\n    truncated_count: 38\n    truncated_rate: 0.76\n    avg_tokens: 6343.8\n    max_new_tokens: 8192\n    total_time_seconds: 6827.8\n    null_count: 36\n- exp_id: acc_ds_s030_8k_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.04\n    correct: 2\n    total: 50\n    truncation_rate: 0.76\n    truncated_count: 38\n    extraction_failures: 3\n    non_truncated_accuracy: 0.167\n    non_truncated_correct: 2\n    non_truncated_total: 12\n    max_new_tokens: 8192\n    avg_tokens: 6566.3\n    total_time_seconds: 7095.1\n- exp_id: gsm8k_qw_rand_s025\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: gsm8k_qw_rand_s030\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: acc_qw_s020_n100_b2_fix\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    batch2_correct: 23\n    batch2_total: 50\n    batch2_acc: 0.46\n    batch1_correct_v2: 13\n    batch1_total: 50\n    batch1_acc_v2: 0.26\n    combined_correct: 36\n    combined_total: 100\n    combined_acc: 0.36\n    null_count: 2\n    truncated_count: 1\n    total_time_seconds: 884.3\n    max_new_tokens: 8192\n    original_batch2_correct: 22\n    original_batch2_acc: 0.44\n    delta_vs_original: +1 correct (+0.02 acc)\n- exp_id: acc_qw_s025_n100_b2_fix\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.34\n    correct: 17\n    n_problems: 50\n    truncation_rate: 0.06\n    truncated_count: 3\n    avg_tokens: 1044\n    max_new_tokens: 8192\n    total_time_seconds: 1099\n    batch: b2 (problems 51-100)\n    merged_n100_accuracy: 0.33\n    merged_n100_correct: 33\n    merged_n100_note: batch1 used max_new_tokens=2048, batch2_fix used 8192 — mismatch\n- exp_id: acc_ds_dense_8k_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.74\n    correct: 37\n    n_problems: 50\n    truncation_rate: 0.16\n    truncated_count: 8\n    avg_tokens: 3126\n    max_new_tokens: 8192\n    total_time_seconds: 2882\n- exp_id: gsm8k_qw_rand_s025_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    verdict: PASS\n    n_problems: 50\n    n_bootstrap: 1000\n    seed: 42\n    high_sparsity:\n      n_segments: 216\n      n_tokens: 9326\n      ppl_dense: 1.0695\n      ppl_attn: 5.9362\n      ppl_kv: 3.4316\n      ppl_both: 15.7484\n      ii_mean: 6.5954\n      ii_ci:\n      - 1.1114\n      - 11.3791\n      ii_median: 0.7176\n      ii_median_ci:\n      - 0.5959\n      - 0.9347\n      winsorized_mean: 6.5046\n      skewness: -4.6807\n      outlier_count: 3\n    low_sparsity:\n      n_segments: 252\n      n_tokens: 29224\n      ppl_dense: 1.1972\n      ppl_attn: 11.5347\n      ppl_kv: 5.6038\n      ppl_both: 21.6874\n      ii_mean: 2.3883\n      ii_ci:\n      - -8.4602\n      - 11.029\n      ii_median: 1.4587\n      ii_median_ci:\n      - 1.1121\n      - 2.0451\n      winsorized_mean: 5.8911\n      skewness: -7.6074\n      outlier_count: 4\n    mid_sparsity:\n      n_segments: 51\n      n_tokens: 5954\n      ppl_dense: 1.2601\n      ppl_attn: 13.4132\n      ppl_kv: 6.4841\n      ppl_both: 20.8714\n      ii_mean: 4.5407\n      ii_ci:\n      - -4.8854\n      - 12.4605\n      ii_median: 1.1272\n      ii_median_ci:\n      - 0.637\n      - 3.3729\n      winsorized_mean: 6.3284\n      skewness: -3.4048\n      outlier_count: 1\n- exp_id: gsm8k_qw_rand_s030_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    verdict: PASS\n    n_problems: 50\n    n_bootstrap: 1000\n    seed: 42\n    high_sparsity:\n      n_segments: 216\n      n_tokens: 9326\n      null_ratio: 2/50\n      ppl_dense: 1.0695\n      ppl_attn: 6.5613\n      ppl_kv: 4.481\n      ppl_both: 23.7486\n      ii_mean: 11.83\n      ii_median: 2.31\n      ii_ci:\n      - 6.17\n      - 17.04\n      ii_median_ci:\n      - 1.64\n      - 2.81\n      winsorized_mean: 10.55\n      skewness: -2.29\n      outlier_count: 7\n    low_sparsity:\n      n_segments: 252\n      n_tokens: 29224\n      null_ratio: 5/50\n      ppl_dense: 1.1972\n      ppl_attn: 6.3283\n      ppl_kv: 8.5374\n      ppl_both: 56.2304\n      ii_mean: 31.26\n      ii_median: 5.2\n      ii_ci:\n      - 17.84\n      - 47.86\n      ii_median_ci:\n      - 3.95\n      - 7.24\n      winsorized_mean: 16.35\n      skewness: 7.57\n      outlier_count: 4\n    mid_sparsity:\n      n_segments: 51\n      n_tokens: 5954\n      null_ratio: 17/50\n      ppl_dense: 1.2601\n      ppl_attn: 18.6162\n      ppl_kv: 11.6625\n      ppl_both: 47.9019\n      ii_mean: 18.02\n      ii_median: 2.7\n      ii_ci:\n      - 0.09\n      - 36.69\n      ii_median_ci:\n      - 1.46\n      - 8.77\n      winsorized_mean: 18.22\n      skewness: 0.43\n      outlier_count: 2\n- exp_id: acc_qw_dense_b1_8k\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.44\n    correct: 22\n    n_problems: 50\n    truncation_rate: 0.02\n    truncated_count: 1\n    avg_tokens: 759.7\n    max_tokens_generated: 8192\n    max_new_tokens: 8192\n    total_time_seconds: 681.8\n    null_count: 0\n    batch: b1_v2 (problems 1-50, 8k tokens)\n    old_batch1_acc: 0.32\n    old_batch1_correct: 16\n    new_combined_n100_acc: 0.46\n    new_combined_n100_correct: 46\n    batch2_acc: 0.48\n    batch2_correct: 24\n- exp_id: acc_qw_s015_b1_8k\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.46\n    correct: 23\n    total: 50\n    truncation_rate_8k: 0.02\n    gen_over_2k: 3\n    gen_over_2k_all_wrong: true\n    max_gen_length: 8192\n    mean_gen_length: 776\n    batch: b1_v2 (problems 1-50, 8k tokens)\n    batch2_acc: 0.38\n    batch2_correct: 19\n    new_combined_n100_acc: 0.42\n    new_combined_n100_correct: 42\n    batch2_source: acc_qw_s015_n100\n- exp_id: acc_qw_s020_b1_8k\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.26\n    correct: 13\n    n_problems: 50\n    truncation_rate: 0.02\n    truncated_count: 1\n    avg_tokens: 722.1\n    max_tokens_generated: 8192\n    max_new_tokens: 8192\n    total_time_seconds: 729.1\n    null_count: 0\n    batch: b1_v2 (problems 1-50, 8k tokens)\n    old_batch1_acc: 0.26\n    old_batch1_correct: 13\n    new_combined_n100_acc: 0.36\n    new_combined_n100_correct: 36\n    batch2_acc: 0.46\n    batch2_correct: 23\n- exp_id: acc_qw_s025_b1_8k\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy: 0.32\n    correct: 16\n    n_problems: 50\n    truncation_rate: 0.04\n    truncated_count: 2\n    extraction_failures: 6\n    avg_tokens: 797.3\n    total_time_seconds: 831.6\n    batch: b1_v2 (problems 1-50, 8k tokens)\n    batch2_acc: 0.34\n    batch2_correct: 17\n    new_combined_n100_acc: 0.33\n    new_combined_n100_correct: 33\n    batch2_source: acc_qw_s025_n100_b2_fix\n- exp_id: acc_qw_s030_b1_8k\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy: 0.14\n    correct: 7\n    total: 50\n    truncation_rate: 0.04\n    truncated_count: 2\n    extraction_failures: 8\n    max_new_tokens: 8192\n    total_time_seconds: 886.7\n    batch: b1_v2 (problems 1-50, 8k tokens)\n    old_batch1_acc: 0.14\n    old_batch1_correct: 7\n    batch2_acc: 0.24\n    batch2_correct: 12\n    new_combined_n100_acc: 0.19\n    new_combined_n100_correct: 19\n- exp_id: c8_llama_n250\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    first_run_failed: true\n    failure_reason: 'bash wrapper wait logic bug: subprocess OOM/error exits silently,\n      script marks DONE without output validation. All 8 output dirs empty.'\n    fix_worker: worker_code_c8_llama_n250_fix_20260516T031229\n    fix_plan: 1) diagnose script + OOM, 2) fix exit code + output validation + GPU\n      monitor, 3) dry-run 1 condition on GPU 2, 4) full launch on GPU 2-3 via submit_training_job\n- exp_id: c4_think_validation_math500\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    v2_math500_kappa_adaptive: 0.88\n    v2_math500_ds_problems: 48\n    v2_math500_ds_tokens: 32055\n    v2_math500_thinking_in_low: 0.816\n    v2_math500_answer_in_high: 0.655\n    v2_math500_temporal_ordering_ds: 0.576\n    v2_math500_temporal_ordering_qw: 0.479\n    v2_qw_pct_positive: 0.98\n    v2_scope: MATH-500\n    v2_models: DS+QW\n    v2_status: ALL_CRITERIA_MET\n    v1_kappa_adaptive: 0.8804\n    v1_auc: 0.9808\n    SCOPE_FLAG: v2_validated_on_MATH500\n- exp_id: c5_per_phase_gini\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    qw_complete: true\n    ds_complete: true\n    n_problems: 30\n    qw_dense_gini_baselines:\n      low: 0.2675\n      mid: 0.2078\n      high: 0.2599\n    qw_importance:\n      s015:\n        global_delta: -0.0103\n        low_delta: -0.0165\n        mid_delta: -0.0094\n        high_delta: -0.012\n      s020:\n        global_delta: -0.0121\n        low_delta: -0.02\n        mid_delta: -0.0115\n        high_delta: -0.0143\n      s025:\n        global_delta: -0.01\n        low_delta: -0.0286\n        mid_delta: -0.0168\n        high_delta: -0.0207\n      s030:\n        global_delta: -0.0202\n        low_delta: -0.035\n        mid_delta: -0.0183\n        high_delta: -0.0239\n    qw_random:\n      s015:\n        global_delta: -0.0186\n        low_delta: -0.0083\n        mid_delta: -0.0038\n        high_delta: -0.0036\n      s020:\n        global_delta: -0.0229\n        low_delta: -0.0119\n        mid_delta: -0.0053\n        high_delta: -0.0067\n      s025:\n        global_delta: -0.0337\n        low_delta: -0.0014\n        mid_delta: -0.0081\n        high_delta: 0.0045\n      s030:\n        global_delta: -0.0447\n        low_delta: -0.0221\n        mid_delta: -0.0077\n        high_delta: -0.0061\n    ds_importance:\n      s015:\n        global_delta: -0.0301\n        low_delta: -0.0163\n        mid_delta: -0.0073\n        high_delta: -0.0152\n      s020:\n        global_delta: -0.0404\n        low_delta: -0.0209\n        mid_delta: -0.0092\n        high_delta: -0.02\n      s025:\n        global_delta: -0.0647\n        low_delta: -0.0313\n        mid_delta: -0.0133\n        high_delta: -0.0267\n      s030:\n        global_delta: -0.0806\n        low_delta: -0.0373\n        mid_delta: -0.0183\n        high_delta: -0.0314\n    ds_random:\n      s015:\n        global_delta: -0.0309\n        low_delta: -0.0102\n        mid_delta: -0.0006\n        high_delta: -0.0062\n      s020:\n        global_delta: -0.0403\n        low_delta: -0.012\n        mid_delta: -0.0007\n        high_delta: -0.0085\n      s025:\n        global_delta: -0.062\n        low_delta: -0.015\n        mid_delta: -0.0096\n        high_delta: -0.0112\n      s030:\n        global_delta: -0.0732\n        low_delta: -0.0183\n        mid_delta: -0.0093\n        high_delta: -0.0138\n    key_finding: 'Both models: importance pruning low-phase Gini delta consistently\n      largest and monotonically increases with sparsity (DS: -0.016 to -0.037; QW:\n      -0.017 to -0.035). Random pruning shows weaker per-phase structure. Supports\n      discrimination collapse hypothesis.'\n- exp_id: c9_gsm8k_power_analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    min_detectable_d_n50: 0.4042\n    random_conditions_all_NS: true\n    random_max_abs_d: 0.164\n    random_conditions:\n      ds_rand_s015_d: -0.017\n      ds_rand_s015_power: 0.052\n      ds_rand_s020_d: -0.063\n      ds_rand_s020_power: 0.072\n      ds_rand_s025_d: 0.026\n      ds_rand_s025_power: 0.054\n      ds_rand_s030_d: 0.058\n      ds_rand_s030_power: 0.069\n      qw_rand_s015_d: -0.154\n      qw_rand_s015_power: 0.187\n      qw_rand_s020_d: 0.113\n      qw_rand_s020_power: 0.123\n      qw_rand_s025_d: 0.163\n      qw_rand_s025_power: 0.203\n      qw_rand_s030_d: 0.165\n      qw_rand_s030_power: 0.207\n    qw_importance_adequately_powered:\n      s025_d: 0.62\n      s025_power: 0.99\n      s030_d: 0.64\n      s030_power: 0.99\n    REVIEWER_WARNING: t-test Cohen's d power analysis ONLY valid for random conditions.\n      Importance conditions have heavy-tail distributions where t-test severely misestimates\n      (e.g. DS s030 d=0.008 but Wilcoxon p=0.0001). DO NOT cite importance t-test\n      power in paper.\n    paper_citable_conclusions:\n    - 'Random: all 8 conditions NS (max|d|=0.164), n=50 detects d>=0.40 → absence\n      of evidence not evidence of absence'\n    - QW importance s025/s030 adequately powered (d≈0.63, power>0.99)\n- exp_id: c10_lang_switching\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    method: CPU analysis of existing gen_snippet data (3/5 sparsities)\n    coverage: dense, s015, s030 (s020/s025 missing gen_snippet)\n    n_per_sparsity: 50\n    dense:\n      switch_rate: 0\n      cn_count: 0\n      en_count: 50\n      cn_acc: null\n      en_acc: 0.52\n    s015:\n      switch_rate: 0.04\n      cn_count: 2\n      en_count: 48\n      cn_acc: 0\n      en_acc: 0.375\n    s030:\n      switch_rate: 0.4\n      cn_count: 20\n      en_count: 30\n      cn_acc: 0.1\n      en_acc: 0.1\n    trend: 'Monotonically increasing: 0% → 4% → 40%. Chinese responses have much lower\n      accuracy (10% at s030 vs 52% dense English).'\n    checkpoint_path: /root/autodl-tmp/pacs/results_c10_lang_cpu.json\n- exp_id: c8_llama_n250_fixed\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_problems: 250\n    model: DeepSeek-R1-Distill-Llama-8B\n    conditions_completed: 8/8\n    importance:\n      s015:\n        median_gradient: 0.050099\n        ci:\n        - 0.045477\n        - 0.058804\n        wilcoxon_p: 1.44e-29\n        cohens_dz: 0.814\n        monotonic: true\n      s020:\n        median_gradient: 0.158708\n        ci:\n        - 0.141193\n        - 0.181937\n        wilcoxon_p: 8.94e-35\n        cohens_dz: 1.01\n        monotonic: true\n      s025:\n        median_gradient: 0.376131\n        ci:\n        - 0.315704\n        - 0.402861\n        wilcoxon_p: 4.3e-39\n        cohens_dz: 1.1151\n        monotonic: true\n      s030:\n        median_gradient: 0.695435\n        ci:\n        - 0.639426\n        - 0.770102\n        wilcoxon_p: 1.48e-40\n        cohens_dz: 1.15\n        monotonic: true\n    random:\n      s015:\n        median_gradient: 0.025489\n        ci:\n        - 0.019942\n        - 0.033342\n        wilcoxon_p: 9.28e-13\n        cohens_dz: 0.4359\n        monotonic: true\n      s020:\n        median_gradient: 0.065003\n        ci:\n        - 0.052258\n        - 0.088191\n        wilcoxon_p: 3.63e-15\n        cohens_dz: 0.4588\n        monotonic: true\n      s025:\n        median_gradient: 0.184201\n        ci:\n        - 0.112738\n        - 0.247119\n        wilcoxon_p: 3.75e-13\n        cohens_dz: 0.4239\n        monotonic: true\n      s030:\n        median_gradient: 0.270653\n        ci:\n        - 0.193489\n        - 0.368089\n        wilcoxon_p: 6.0e-12\n        cohens_dz: 0.4104\n        monotonic: true\n    dose_response_monotonic: true\n    imp_rand_ratio_range: 1.97-2.57x\n    all_conditions_significant: true\n    importance_effect_size_range: 0.81-1.15 (large)\n    random_effect_size_range: 0.41-0.46 (medium)\n- exp_id: c10-lang-s020-s025\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: c10_lang_s020_s025\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    s020:\n      n: 50\n      accuracy: 0.26\n      switch_rate: 0.14\n      switch_count: 7\n      mean_cn_ratio: 0.066\n      cn_acc: 0.333\n      en_acc: 0.25\n    s025:\n      n: 50\n      accuracy: 0.1\n      switch_rate: 0.32\n      switch_count: 16\n      mean_cn_ratio: 0.152\n      cn_acc: 0.2\n      en_acc: 0.057\n    wall_time_s: 11680.6\n    output_path: /root/autodl-tmp/pacs/results_c10_lang_s020_s025.json\n- exp_id: c8_llama_gpu0_s025\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_problems: 250\n    n_bootstrap: 1000\n    segmentation: quantile\n    per_phase_ii_median:\n      high: 0.0171\n      mid: 0.1916\n      low: 0.388\n    per_phase_ii_mean:\n      high: 0.0218\n      mid: 0.2126\n      low: 0.4713\n    phase_gradient_median_diff: 0.3761\n    phase_gradient_median_diff_ci95:\n    - 0.3147\n    - 0.4039\n    wilcoxon_p_one_sided: 4.3e-39\n    bonferroni_p_k4: 1.72e-38\n    cohens_dz: 1.1174\n    rank_biserial_r: 0.8689\n    n_paired: 244\n    pos_neg_ratio: 228/16\n- exp_id: gpqa_ds_importance_s015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_problems: 198\n    interaction_index:\n      high:\n        mean: 0.191363\n        median: 0.012758\n        ci:\n        - 0.047972\n        - 0.514786\n        median_ci:\n        - 0.011463\n        - 0.013936\n        winsorized_mean: 0.039667\n        skewness: 77\n      mid:\n        mean: 0.87787\n        median: 0.102412\n        ci:\n        - 0.72315\n        - 1.039118\n        median_ci:\n        - 0.092683\n        - 0.115074\n        winsorized_mean: 0.532911\n        skewness: 7.7\n      low:\n        mean: 5.991797\n        median: 0.960161\n        ci:\n        - 5.235965\n        - 6.732278\n        median_ci:\n        - 0.892882\n        - 1.03306\n        winsorized_mean: 3.945337\n        skewness: 8.88\n    perplexity:\n      high:\n        dense: 1.1777\n        attn: 1.5205\n        kv: 1.702\n        both: 2.2531\n      mid:\n        dense: 1.3075\n        attn: 1.6733\n        kv: 3.2369\n        both: 4.7222\n      low:\n        dense: 1.4216\n        attn: 1.9771\n        kv: 19.3067\n        both: 27.6495\n    phase_stats:\n      high:\n        n_tokens: 479658\n        n_segments: 6261\n      mid:\n        n_tokens: 276409\n        n_segments: 2185\n      low:\n        n_tokens: 465085\n        n_segments: 5128\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: false\n      overall: PASS\n    gradient_direction: low > mid > high\n    median_ratio_low_high: 75.2\n- exp_id: gpqa_ds_importance_s020\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: recency_s025\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    phase_gradient:\n      median_diff: 1.1186\n      cohens_dz: 0.2205\n      p_value: 0.00922\n      significant: true\n      direction: reversed (low_sparsity more damaged)\n    comparison_importance_s025:\n      importance_median_diff: -1.0745\n      importance_cohens_dz: -0.7778\n      importance_p_value: 1.06e-68\n      gradient_directions_opposite: true\n      importance_effect_3.5x_stronger: true\n    comparison_random_s025:\n      random_median_diff: -0.3931\n      random_cohens_dz: -0.0172\n      random_p_value: 1.59e-11\n    interaction_index:\n      high_sparsity_median: -0.000346\n      mid_sparsity_median: -0.02246\n      low_sparsity_median: -0.091106\n    config:\n      model: DeepSeek-R1-Distill-Qwen-7B\n      masking_method: recency\n      sparsity: 0.25\n      n_problems: 100\n      seed: 42\n- exp_id: recency_s030\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    phase_gradient:\n      median_diff: -1982.57\n      ci_low: -9391.77\n      ci_high: 882.08\n      cohens_dz: -0.096\n      p_value: 0.114\n      significant: false\n      effect_size: negligible\n    comparison_importance_s030:\n      median_diff: 8.48\n      cohens_dz: 0.33\n      p_value: 1.09e-79\n      significant: true\n    comparison_random_s030:\n      median_diff: 0.51\n      cohens_dz: -0.049\n      p_value: 0.00148\n      significant: true\n    interaction_index:\n      high_sparsity_median: -0.0018\n      mid_sparsity_median: -0.016\n      low_sparsity_median: 0.1099\n    n_problems: 100\n    model: DeepSeek-R1-Distill-Qwen-7B\n    masking_method: recency\n    sparsity: 0.3\n- exp_id: recency_s015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_problems: 100\n    model: DeepSeek-R1-Distill-Qwen-7B\n    masking_method: recency\n    sparsity: 0.15\n    phase_gradient:\n      median_diff: -0.0026\n      cohens_dz: 0.083\n      p_value: 0.77\n      significant: false\n    comparison_importance_s015:\n      median_diff: 0.39\n      cohens_dz: 0.574\n      p_value: < 1e-70\n      significant: true\n    comparison_random_s015:\n      median_diff: 0.014\n      cohens_dz: -0.045\n      p_value: 0.86\n      significant: false\n    interpretation: Recency eviction shows NO phase gradient (NS, negligible effect),\n      confirming phase-dependent severity is attention-score-specific\n- exp_id: gpqa_ds_importance_s025\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: gpqa_ds_importance_s030\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: gpqa_ds_random_s020\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-17T01:29:19.980Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-17T01:29:19.980Z",
  "sessionId": "801dd6fc-5861-4c46-a727-64581ec2a334"
}
```

---

## Round 1

26 recorded events

### User

_source line 3 · 2026-05-17T01:29:20.006Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：Reviewers fully accept empirical-finding framing; recency control + triple dissociation seen as clean novel contribution; cross-architecture variation treated as interesting secondary finding rather than weakness
核心假设：['Empirical finding paper without practical method accepted at EMNLP (precedent: scaling laws papers, probing papers)', 'Recency control resolves circularity concern definitively — no reviewer requests causal intervention', 'Architecture-dependent strategy specificity (LLaMA 2.0-2.6× vs DS 15-17×) framed as discovery, not confound', '50-citation related work + explicit gap analysis convinces reviewers of novelty vs ThinKV/SparK/Lethe', '7B scale accepted with honest limitations paragraph; no hard reject on scale alone', 'Discrimination collapse mechanism (Gini/CV consistent cross-model) accepted despite entropy being model-dependent']
关键指标范围：{'arr_overall_scores': [3.5, 4.5], 'arr_soundness': [3.5, 4.0], 'acceptance_probability': [0.55, 0.75], 'reviewer_novelty_concern_count': [0, 1], 'claims_requiring_adjustment': [0, 1]}
叙事方向：Original framing intact: 'emergent phase-strategy interaction' as core contribution, triple dissociation (importance/random/recency) as methodological novelty, architecture-dependence as scope-expanding finding. C1-C11 全部保留原始强度。Discussion 正常报告 GSM8K ratio 衰减和 LLaMA specificity 差异作为 open questions，不需要 hedge main claims。

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
tier: best
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
  "promptId": "b55edb12-8b05-4782-9d97-5ec5c1db7737",
  "type": "user",
  "uuid": "19a116f9-32d8-424b-b959-42921fb8ce70",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "801dd6fc-5861-4c46-a727-64581ec2a334",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-17T01:29:20.001Z_

```json
{
  "parentUuid": "19a116f9-32d8-424b-b959-42921fb8ce70",
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
  "uuid": "e36093f5-c9fe-4b35-b435-8b33c247b80b",
  "timestamp": "2026-05-17T01:29:20.001Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "801dd6fc-5861-4c46-a727-64581ec2a334",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-17T01:29:20.001Z_

```json
{
  "parentUuid": "e36093f5-c9fe-4b35-b435-8b33c247b80b",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "f3ac2bc3-9257-4604-9aa9-c84840ec53ef",
  "timestamp": "2026-05-17T01:29:20.001Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "801dd6fc-5861-4c46-a727-64581ec2a334",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Reviewers fully accept empirical-finding framing; recency control + triple dissociation seen as clean novel contribution; cross-architecture variation trea…",
  "leafUuid": "f3ac2bc3-9257-4604-9aa9-c84840ec53ef",
  "sessionId": "801dd6fc-5861-4c46-a727-64581ec2a334"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Phase-modulated compound sparsity with recency control confirmed",
  "sessionId": "801dd6fc-5861-4c46-a727-64581ec2a334"
}
```

---

### Assistant

_source line 8 · 2026-05-17T01:30:15.523Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted data for each "planned" experiment in the experiment_plan, based on the "best" tier definition they've provided. Let me look through the experiment_plan to find experiments with status "planned" or that haven't been completed yet.

Looking at the experiment_plan, I see all experiments listed have status "DONE". But wait - let me look at the registry for experiments with status "RUNNING":
- gpqa_ds_importance_s020 (RUNNING)


- gpqa_ds_importance_s025 (RUNNING)
- gpqa_ds_importance_s030 (RUNNING)
- gpqa_ds_random_s020 (RUNNING)

And in the experiment_plan, I see C9 (Differentiation from Lethe/SparK prior work) has status "planned". Let me check if C9 actually appears in the experiment_plan list or if it's just referenced in the table.

Looking more carefully, all the experiments in experiment_plan show status "DONE", but C9 is marked as "planned" in the claims table. There's a mismatch here—the RUNNING experiments in the registry don't seem to correspond to C9, and C9 doesn't have a matching entry in the experiment_plan with "planned" status. Let me review the full experiment_plan list to see what's actually there. with `status: DONE`. But the RUNNING experiments in the registry (gpqa_*) don't appear in the experiment_plan. And C9 is listed as "planned" in the Core Claims table.

I think the user wants me to predict results for the RUNNING experiments (GPQA validation) and C9, which is marked as "planned". Let me look at the registry more carefully—I see gpqa_ds_importance_s020, s025, and s030 are all RUNNING, along with gpqa_ds_random_s020, while the recency experiments are already DONE. So I need to generate predictions for those RUNNING GPQA experiments plus C9. Looking at the experiment registry more carefully, I see that the RUNNING experiments are only listed there, while the experiment_plan section shows completed work. The user is asking me to generate predictions for those four active experiments based on the "best" tier framework.

For these GPQA validation experiments extending to a harder benchmark, I need to predict results that align with the narrative where reviewers accept the empirical findings, the recency control and triple dissociation hold up cleanly, and cross-architecture variation reads as interesting rather than concerning. Using the reference completed experiment as a baseline, I'll work out what plausible results would support this framing across the different seed variations. Looking at the GPQA s015 results, the 75.2x ratio is notably stronger than MATH-500's ~69x, which tracks with GPQA's longer reasoning chains requiring more precision. I'm now extrapolating the scaling patterns for s020, s025, and s030 based on how MATH-500 and GSM8K progressed, while expecting random to show minimal or no gradient in the best tier.

For s020, applying the typical 3.1x scaling factor gives me predictions around 0.04 for high, 0.35 for mid, and 3.2 for low. For s025, the 3.3x progression yields roughly 0.10, 1.2, and 10.5 across the tiers. For s030, I'm using the 2.1x scaling to estimate the final values.

The random baseline at s020 shows no meaningful gradient—medians cluster around 0.08-0.15 with p > 0.1—which is the expected pattern for non-importance sampling.

Now I'm wondering if there are other planned experiments I haven't accounted for yet. Let me check what files exist in the project directory to see if there's a more complete list somewhere.

Actually, the user has already given me the context I need. I should focus on generating predictions for the four RUNNING GPQA experiments and any clearly planned ones from the claims table. The only other planned experiment I see is C9 about differentiating from prior work, but that's a writing task, not a computational one.

So I'll structure my output around the four RUNNING GPQA experiments.

Wait, let me reconsider what the user is actually asking for. They want me to expand on each "planned" experiment in the experiment_plan section, but looking at what they provided, all entries show status: DONE. There are no planned entries visible in the experiment_plan they shared.

The RUNNING experiments in the registry could be what they're referring to, but I should check if there's an actual experiment plan file in the project that might contain planned entries I haven't seen yet.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3ac2bc3-9257-4604-9aa9-c84840ec53ef",
  "isSidechain": false,
  "requestId": "req_011Cb7GsoJDvCXH2qoWv2K7i",
  "type": "assistant",
  "uuid": "f64d4c40-ebd9-425f-a120-da3712fd0567",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "801dd6fc-5861-4c46-a727-64581ec2a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KWkuyzvqWi7ZR4vMMiiNdg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 58881,
      "cache_read_input_tokens": 11841,
      "output_tokens": 2909,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 58881,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 2909,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 58881,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 58881
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

_source line 9 · 2026-05-17T01:30:15.653Z_

Let me check the project directory for the full experiment plan with planned experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f64d4c40-ebd9-425f-a120-da3712fd0567",
  "isSidechain": false,
  "requestId": "req_011Cb7GsoJDvCXH2qoWv2K7i",
  "type": "assistant",
  "uuid": "9cfba9d3-e4eb-4f20-bfb1-fca162210e08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "801dd6fc-5861-4c46-a727-64581ec2a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KWkuyzvqWi7ZR4vMMiiNdg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 58881,
      "cache_read_input_tokens": 11841,
      "output_tokens": 2909,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 58881,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 2909,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 58881,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 58881
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

_source line 10 · 2026-05-17T01:30:18.709Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01NBSeyWoGDuqY7DF18hk8Sq`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find planned experiments file",
  "prompt": "In /home/ubuntu/.agent-ml-research-idea_gen_0509_11, find any YAML or markdown file that contains an experiment_plan with experiments that have status \"planned\" or \"PLANNED\". Look for files like experiment_plan.yaml, experiment_plan.md, or similar. Also check for any file containing \"gpqa\" in the name. Search breadth: medium."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9cfba9d3-e4eb-4f20-bfb1-fca162210e08",
  "isSidechain": false,
  "requestId": "req_011Cb7GsoJDvCXH2qoWv2K7i",
  "type": "assistant",
  "uuid": "e4975de3-2374-4b45-9506-598cf859e5b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "801dd6fc-5861-4c46-a727-64581ec2a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KWkuyzvqWi7ZR4vMMiiNdg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 58881,
      "cache_read_input_tokens": 11841,
      "output_tokens": 2909,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 58881,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 2909,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 58881,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 58881
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

_source line 11 · 2026-05-17T01:30:37.986Z_

<details><summary>↩ Tool result · `toolu_01NBSeyWoGDuqY7DF18hk8Sq`</summary>

```text
Perfect! Now let me create a comprehensive summary. Based on my search, I found the relevant files with experiment plans containing "PLANNED" status experiments and many GPQA-related files.

## Summary

I found the following files matching your search criteria:

### Experiment Plan Files with "PLANNED" or "PLANNED" Status:

**1. redundancy-compound-sparsity project**
File: `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/redundancy-compound-sparsity/experiment_plan.yaml`

This file contains 10 experiments with "PLANNED" status:
- `confound-ctrl-001`: Confound control with DeepSeek-R1-Distill-Llama-8B
- `confound-ctrl-002`: Confound control with Qwen2-7B-Instruct
- `llama-sparsity-sweep`: Llama sparsity level sweep (P0 priority)
- `llama-layer-analysis`: Llama per-layer analysis (P0 priority)
- `cross-arch-mistral`: Mistral-7B validation (P1 priority)
- `kv-eviction-wallclock`: Wall-clock timing for O(1) vs O(n) eviction (P1 priority)
- `neg-per-head`: Per-head KV contribution analysis (P1 priority)
- `kv-eviction-ablation`: KV eviction key-only vs key+value ablation (P2 priority)
- `llama-downstream`: Llama two-tier sparsity downstream accuracy (P2 priority)

There's also 1 experiment with "PREPARING" status: `kv-bench-001` (KV eviction benchmark)

**2. redundancy-compound-sparsity-2 project**
File: `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/redundancy-compound-sparsity-2/experiment_plan.yaml`

This file contains NO experiments with "PLANNED" status (all are in various phases: sanity gate, ablation, etc.)

**3. phase-gated-compound-sparse project**
File: `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/experiment_plan.yaml`

This file contains experiments mapped to claims (C1-C10) with various statuses including "planned" (e.g., claim C9 has status: "planned" for differentiation from prior work)

### GPQA-Related Files:

Many files containing "gpqa" in the name were found in `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/`, including:
- Worker logs related to GPQA pipeline preparation, prompting, evaluation
- Checkpoint files tracking GPQA experiments (gpqa_ds_importance and gpqa_ds_random series)
- Analysis reports: `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/gpqa_ds_importance_s015_analysis.md` and related subdirectories
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e4975de3-2374-4b45-9506-598cf859e5b2",
  "isSidechain": false,
  "promptId": "b55edb12-8b05-4782-9d97-5ec5c1db7737",
  "type": "user",
  "uuid": "899e0616-4449-4d23-866c-b1dfc21808c9",
  "toolUseResult": {
    "status": "completed",
    "prompt": "In /home/ubuntu/.agent-ml-research-idea_gen_0509_11, find any YAML or markdown file that contains an experiment_plan with experiments that have status \"planned\" or \"PLANNED\". Look for files like experiment_plan.yaml, experiment_plan.md, or similar. Also check for any file containing \"gpqa\" in the name. Search breadth: medium.",
    "agentId": "a55a34dcd3a99585a",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now let me create a comprehensive summary. Based on my search, I found the relevant files with experiment plans containing \"PLANNED\" status experiments and many GPQA-related files.\n\n## Summary\n\nI found the following files matching your search criteria:\n\n### Experiment Plan Files with \"PLANNED\" or \"PLANNED\" Status:\n\n**1. redundancy-compound-sparsity project**\nFile: `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/redundancy-compound-sparsity/experiment_plan.yaml`\n\nThis file contains 10 experiments with \"PLANNED\" status:\n- `confound-ctrl-001`: Confound control with DeepSeek-R1-Distill-Llama-8B\n- `confound-ctrl-002`: Confound control with Qwen2-7B-Instruct\n- `llama-sparsity-sweep`: Llama sparsity level sweep (P0 priority)\n- `llama-layer-analysis`: Llama per-layer analysis (P0 priority)\n- `cross-arch-mistral`: Mistral-7B validation (P1 priority)\n- `kv-eviction-wallclock`: Wall-clock timing for O(1) vs O(n) eviction (P1 priority)\n- `neg-per-head`: Per-head KV contribution analysis (P1 priority)\n- `kv-eviction-ablation`: KV eviction key-only vs key+value ablation (P2 priority)\n- `llama-downstream`: Llama two-tier sparsity downstream accuracy (P2 priority)\n\nThere's also 1 experiment with \"PREPARING\" status: `kv-bench-001` (KV eviction benchmark)\n\n**2. redundancy-compound-sparsity-2 project**\nFile: `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/redundancy-compound-sparsity-2/experiment_plan.yaml`\n\nThis file contains NO experiments with \"PLANNED\" status (all are in various phases: sanity gate, ablation, etc.)\n\n**3. phase-gated-compound-sparse project**\nFile: `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/experiment_plan.yaml`\n\nThis file contains experiments mapped to claims (C1-C10) with various statuses including \"planned\" (e.g., claim C9 has status: \"planned\" for differentiation from prior work)\n\n### GPQA-Related Files:\n\nMany files containing \"gpqa\" in the name were found in `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/`, including:\n- Worker logs related to GPQA pipeline preparation, prompting, evaluation\n- Checkpoint files tracking GPQA experiments (gpqa_ds_importance and gpqa_ds_random series)\n- Analysis reports: `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/gpqa_ds_importance_s015_analysis.md` and related subdirectories"
      }
    ],
    "totalDurationMs": 19270,
    "totalTokens": 51916,
    "totalToolUseCount": 10,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 1015,
      "cache_read_input_tokens": 50138,
      "output_tokens": 759,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1015
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 759,
          "cache_read_input_tokens": 50138,
          "cache_creation_input_tokens": 1015,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1015,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 3,
      "searchCount": 7,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "e4975de3-2374-4b45-9506-598cf859e5b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "801dd6fc-5861-4c46-a727-64581ec2a334",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-17T01:30:42.105Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01M919JewMWkhpKsnHA4otjB`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/experiment_plan.yaml | grep -A 10 \"status: planned\" | head -100",
  "description": "Find planned experiments in phase-gated project"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "899e0616-4449-4d23-866c-b1dfc21808c9",
  "isSidechain": false,
  "requestId": "req_011Cb7GyYVet3KCg2Wwo5Lvx",
  "type": "assistant",
  "uuid": "7d91454a-8cdd-4a0d-92f6-ace2ba69d7cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "801dd6fc-5861-4c46-a727-64581ec2a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0135sFnaqsiuCm83pwfDnMkx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3661,
      "cache_read_input_tokens": 70722,
      "output_tokens": 244,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3661,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 244,
          "cache_read_input_tokens": 70722,
          "cache_creation_input_tokens": 3661,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3661
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

_source line 13 · 2026-05-17T01:30:42.298Z_

<details><summary>↩ Tool result · `toolu_01M919JewMWkhpKsnHA4otjB`</summary>

```text
    status: planned
  C10:
    description: Phase gradient cross-benchmark robust; strategy specificity task-modulated
    status: running
  S3->C:
    description: Onset threshold is model-dependent
    status: confirmed
  S7->C:
    description: Dose-response monotonicity (Spearman rho=1.0)
    status: confirmed
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d91454a-8cdd-4a0d-92f6-ace2ba69d7cf",
  "isSidechain": false,
  "promptId": "b55edb12-8b05-4782-9d97-5ec5c1db7737",
  "type": "user",
  "uuid": "5018527c-16ca-4387-b834-72c43e7d6a33",
  "toolUseResult": {
    "stdout": "    status: planned\n  C10:\n    description: Phase gradient cross-benchmark robust; strategy specificity task-modulated\n    status: running\n  S3->C:\n    description: Onset threshold is model-dependent\n    status: confirmed\n  S7->C:\n    description: Dose-response monotonicity (Spearman rho=1.0)\n    status: confirmed",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "7d91454a-8cdd-4a0d-92f6-ace2ba69d7cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "801dd6fc-5861-4c46-a727-64581ec2a334",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-17T01:30:43.018Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Y85kXPr1W9A14iGe6YdFRf`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/experiment_plan.yaml | grep -B 5 \"RUNNING\\|planned\\|PLANNED\" | head -80",
  "description": "Find RUNNING/planned experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5018527c-16ca-4387-b834-72c43e7d6a33",
  "isSidechain": false,
  "requestId": "req_011Cb7GyYVet3KCg2Wwo5Lvx",
  "type": "assistant",
  "uuid": "58838878-7233-4123-96e4-414b39b34d33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "801dd6fc-5861-4c46-a727-64581ec2a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0135sFnaqsiuCm83pwfDnMkx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3661,
      "cache_read_input_tokens": 70722,
      "output_tokens": 244,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3661,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 244,
          "cache_read_input_tokens": 70722,
          "cache_creation_input_tokens": 3661,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3661
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

_source line 15 · 2026-05-17T01:30:43.098Z_

<details><summary>↩ Tool result · `toolu_01Y85kXPr1W9A14iGe6YdFRf`</summary>

```text
  C8:
    description: Cross-architecture validation (LLaMA)
    status: partially_confirmed
  C9:
    description: Differentiation from Lethe/SparK prior work
    status: planned
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58838878-7233-4123-96e4-414b39b34d33",
  "isSidechain": false,
  "promptId": "b55edb12-8b05-4782-9d97-5ec5c1db7737",
  "type": "user",
  "uuid": "0bf5b6a3-5ea6-43b0-a743-1186961da17d",
  "toolUseResult": {
    "stdout": "  C8:\n    description: Cross-architecture validation (LLaMA)\n    status: partially_confirmed\n  C9:\n    description: Differentiation from Lethe/SparK prior work\n    status: planned",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "58838878-7233-4123-96e4-414b39b34d33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "801dd6fc-5861-4c46-a727-64581ec2a334",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 16_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Reviewers fully accept empirical-finding framing; recency control + triple dissociation seen as clean novel contribution; cross-architecture variation trea…",
  "leafUuid": "0bf5b6a3-5ea6-43b0-a743-1186961da17d",
  "sessionId": "801dd6fc-5861-4c46-a727-64581ec2a334"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Phase-modulated compound sparsity with recency control confirmed",
  "sessionId": "801dd6fc-5861-4c46-a727-64581ec2a334"
}
```

---

### Tool call

_source line 18 · 2026-05-17T01:30:45.831Z_

<details open><summary>🔧 Tool call — Read · `toolu_01S2a3N6VwDxQ6K8SvnRxTF6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0bf5b6a3-5ea6-43b0-a743-1186961da17d",
  "isSidechain": false,
  "requestId": "req_011Cb7GyvLZTYMQenEo28jvJ",
  "type": "assistant",
  "uuid": "9294d03f-322b-4178-ac74-688d4652d186",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "801dd6fc-5861-4c46-a727-64581ec2a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UBa3RuYB1peK2azasJXzsf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 447,
      "cache_read_input_tokens": 74383,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 447,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 88,
          "cache_read_input_tokens": 74383,
          "cache_creation_input_tokens": 447,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 447
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

_source line 19 · 2026-05-17T01:30:45.838Z_

<details><summary>↩ Tool result · `toolu_01S2a3N6VwDxQ6K8SvnRxTF6`</summary>

```text
1	# experiment_plan.yaml — Retrospective experiment-to-claim mapping
2	# Generated 2026-05-16 | project: phase-gated-compound-sparse
3	# 38 experiments mapped across 13 claims
4	
5	experiments:
6	- id: c1_bf16_importance_s025
7	  claim: C1
8	  description: 'II median: high=0.032, mid=1.118, low=7.196; importance masking shows
9	    strong phase gradient'
10	  registry_id: bf16_importance_s025
11	  role: primary
12	  priority: high
13	- id: c1_bf16_ds_rand_s025
14	  claim: C1
15	  description: 'Random II median: high=0.818, mid=0.932, low=1.363; flat gradient
16	    vs importance'
17	  registry_id: bf16_ds_rand_s025
18	  role: primary
19	  priority: high
20	- id: c1_bf16_qw_imp_s025
21	  claim: C1
22	  description: 'Qwen cross-model: median_diff=1.109, Cohen''s d=1.233, p<1e-5'
23	  registry_id: bf16_qw_imp_s025
24	  role: supporting
25	  priority: medium
26	- id: c1_sf5_asymmetric_spot
27	  claim: C1
28	  description: 'Asymmetric configs: h02_kv03 D=19.13, h03_kv02 D=18.25; gradient consistent'
29	  registry_id: sf5_asymmetric_spot
30	  role: ablation
31	  priority: medium
32	- id: c1_c2_accuracy_eval
33	  claim: C1
34	  description: 'DS dense->s030 acc: 0.52->0.10 (-0.42); QW dense->s030: 0.32->0.14
35	    (-0.18)'
36	  registry_id: c2_accuracy_eval
37	  role: supporting
38	  priority: medium
39	- id: c2_bf16_importance_s030
40	  claim: C2
41	  description: 'Phase gradient: II low=14.64 >> mid=2.28 >> high=0.053 (median); low/high
42	    ratio ~276x'
43	  registry_id: bf16_importance_s030
44	  role: primary
45	  priority: high
46	- id: c2_v6_importance_s030
47	  claim: C2
48	  description: II low_median=34.69, mid_median=7.27, high_median=0.88; bootstrap_gradient=41.92,
49	    CI=[19.14,299.76]
50	  registry_id: v6_importance_s030
51	  role: primary
52	  priority: high
53	- id: c2_think_phase_validation
54	  claim: C2
55	  description: Phase segmentation kappa=0.887; thinking=57.8% low-sparsity, answer=62.7%
56	    high-sparsity
57	  registry_id: think_phase_validation
58	  role: supporting
59	  priority: medium
60	- id: c2_acc_qw_s030_n100
61	  claim: C2
62	  description: QW importance s030 accuracy=0.19 (n=100); dose-response monotonic decline
63	    from dense=0.40
64	  registry_id: acc_qw_s030_n100
65	  role: supporting
66	  priority: medium
67	- id: c2_acc_ds_s015_8k_v2
68	  claim: C2
69	  description: DS s015 accuracy=0.48 vs dense=0.74; early onset of compound degradation
70	  registry_id: acc_ds_s015_8k_v2
71	  role: supporting
72	  priority: medium
73	- id: c3_v6_importance_s025
74	  claim: C3
75	  description: 'Importance: II low_median=24.16 >> high_median=0.66; strong phase
76	    gradient (36x ratio)'
77	  registry_id: v6_importance_s025
78	  role: primary
79	  priority: high
80	- id: c3_v6_random_s025
81	  claim: C3
82	  description: 'Random: II low_median=2.91 ~ high_median=3.00; flat phase gradient
83	    (bootstrap_p=0.559)'
84	  registry_id: v6_random_s025
85	  role: primary
86	  priority: high
87	- id: c3_bf16_importance_s020
88	  claim: C3
89	  description: 'Importance: II low=1.50, mid=0.20, high=0.015 (median); clear phase
90	    separation'
91	  registry_id: bf16_importance_s020
92	  role: supporting
93	  priority: medium
94	- id: c3_bf16_ds_rand_s020
95	  claim: C3
96	  description: 'Random: II high=0.292, mid=0.350, low=0.276 (median); no phase separation'
97	  registry_id: bf16_ds_rand_s020
98	  role: supporting
99	  priority: medium
100	- id: c4_c4_entropy
101	  claim: C4
102	  description: 'DS importance entropy_delta: -0.04 to -0.05 (collapse); random: +0.13
103	    to +0.23 (redistribution). Gini_delta: -0.03 to -0.08'
104	  registry_id: c4_entropy
105	  role: primary
106	  priority: high
107	- id: c4_qwen_c4_entropy
108	  claim: C4
109	  description: 'QW importance entropy_delta mixed: s015=-0.073, s025=+0.045; Gini
110	    weaker (-0.01 to -0.02). Model-dependent pattern'
111	  registry_id: qwen_c4_entropy
112	  role: primary
113	  priority: high
114	- id: c5_bf16_qw_imp_s030
115	  claim: C5
116	  description: 'Qwen: median_diff=2.619, Cohen''s d=1.439, p<1e-5; replicates DeepSeek
117	    pattern'
118	  registry_id: bf16_qw_imp_s030
119	  role: primary
120	  priority: high
121	- id: c5_bf16_importance_s030
122	  claim: C5
123	  description: 'DeepSeek: II low_median=14.64, high_median=0.053; strong phase gradient'
124	  registry_id: bf16_importance_s030
125	  role: primary
126	  priority: high
127	- id: c5_c2_n500_deepseek
128	  claim: C5
129	  description: 'DS n=500: imp_s030 median_II=8.48, CI=[7.46,9.56], p=1.3e-78; robust
130	    at scale'
131	  registry_id: c2_n500_deepseek
132	  role: supporting
133	  priority: medium
134	- id: c5_c2_qw_n500_r3
135	  claim: C5
136	  description: 'QW n=500: imp_s030 median_II=4.33, p<1e-40; cross-model replication
137	    at high power'
138	  registry_id: c2_qw_n500_r3
139	  role: supporting
140	  priority: medium
141	- id: c5b_c5b_pilot
142	  claim: C5b
143	  description: 'Oracle recovery=18% (gate: >30% FAIL); heuristic recovery=31.7% but
144	    CI crosses zero. s030 incomplete'
145	  registry_id: c5b_pilot
146	  role: primary
147	  priority: high
148	- id: c6_bf16_importance_s015
149	  claim: C6
150	  description: II low_median=0.398 at s=0.15
151	  registry_id: bf16_importance_s015
152	  role: primary
153	  priority: high
154	- id: c6_bf16_importance_s020
155	  claim: C6
156	  description: II low_median=1.496 at s=0.20
157	  registry_id: bf16_importance_s020
158	  role: supporting
159	  priority: medium
160	- id: c6_bf16_importance_s025
161	  claim: C6
162	  description: II low_median=7.196 at s=0.25
163	  registry_id: bf16_importance_s025
164	  role: supporting
165	  priority: medium
166	- id: c6_bf16_importance_s030
167	  claim: C6
168	  description: II low_median=14.64 at s=0.30; growth 0.40->1.50->7.20->14.64 is sub-exponential
169	  registry_id: bf16_importance_s030
170	  role: supporting
171	  priority: medium
172	- id: c7_c2_n500_deepseek
173	  claim: C7
174	  description: 'DS n=500: all 4 sparsities significant (p<1e-70); CIs non-overlapping
175	    across dose levels'
176	  registry_id: c2_n500_deepseek
177	  role: primary
178	  priority: high
179	- id: c7_c2_qw_n500_r3
180	  claim: C7
181	  description: 'QW n=500: all 4 sparsities significant (p<1e-14 Bonferroni-corrected);
182	    mid_null_rate=45.2%'
183	  registry_id: c2_qw_n500_r3
184	  role: primary
185	  priority: high
186	- id: c8_c3_llama
187	  claim: C8
188	  description: LLaMA-8B (LlamaForCausalLM) replicates phase-modulated compound severity
189	    from Qwen2ForCausalLM
190	  registry_id: c3_llama
191	  role: primary
192	  priority: high
193	- id: c10_gsm8k_profiling_ds
194	  claim: C10
195	  description: 'DS GSM8K importance gradient: s015=0.241, s020=0.740, s025=1.992,
196	    s030=4.636 (monotonic)'
197	  registry_id: gsm8k_profiling_ds
198	  role: primary
199	  priority: high
200	- id: c10_gsm8k_profiling_qw
201	  claim: C10
202	  description: 'QW GSM8K importance gradient: s015=0.039, s020=0.158, s025=1.100,
203	    s030=2.092 (monotonic)'
204	  registry_id: gsm8k_profiling_qw
205	  role: primary
206	  priority: high
207	- id: c10_gsm8k_qw_rand_s025_v2
208	  claim: C10
209	  description: 'QW random s025 GSM8K: II median_high=0.72, low=1.48; phase gradient
210	    weaker than importance'
211	  registry_id: gsm8k_qw_rand_s025_v2
212	  role: supporting
213	  priority: medium
214	- id: c10_gsm8k_qw_rand_s030_v2
215	  claim: C10
216	  description: 'QW random s030 GSM8K: II median_high=2.31, low=5.87; compound effect
217	    on GSM8K confirmed'
218	  registry_id: gsm8k_qw_rand_s030_v2
219	  role: supporting
220	  priority: medium
221	- id: s3_c_bf16_ds_imp_s010
222	  claim: S3->C
223	  description: 'DS s=0.10: II_high_median=0.003, verdict=FAIL; below onset threshold
224	    for DeepSeek'
225	  registry_id: bf16_ds_imp_s010
226	  role: primary
227	  priority: high
228	- id: s3_c_bf16_qw_imp_s010
229	  claim: S3->C
230	  description: 'QW s=0.10: overall_verdict=PASS, CI_overlap_test=PASS; Qwen onset
231	    earlier than DeepSeek'
232	  registry_id: bf16_qw_imp_s010
233	  role: primary
234	  priority: high
235	- id: s3_c_bf16_qw_imp_s015
236	  claim: S3->C
237	  description: 'QW s=0.15: median_diff=0.048, permutation_p=0.0001; confirmed above
238	    threshold'
239	  registry_id: bf16_qw_imp_s015
240	  role: supporting
241	  priority: medium
242	- id: s7_c_c2_n500_deepseek
243	  claim: S7->C
244	  description: 'DS n=500 monotonic: imp median II 0.39->1.21->3.99->8.48 across s015-s030
245	    (Spearman rho=1.0)'
246	  registry_id: c2_n500_deepseek
247	  role: primary
248	  priority: high
249	- id: s7_c_c2_qw_n500_r3
250	  claim: S7->C
251	  description: 'QW n=500 monotonic: imp median II 0.066->0.307->1.075->4.33 across
252	    s015-s030 (Spearman rho=1.0)'
253	  registry_id: c2_qw_n500_r3
254	  role: primary
255	  priority: high
256	- id: s7_c_bf16_qw_imp_s035
257	  claim: S7->C
258	  description: 'QW s=0.35: low_II_median=8.24; extends dose-response beyond s030'
259	  registry_id: bf16_qw_imp_s035
260	  role: supporting
261	  priority: medium
262	_claims:
263	  C1:
264	    description: Compound sparsity severity is strategy- and task-modulated
265	    status: confirmed
266	  C2:
267	    description: Severity is phase-modulated (amplified in low-sparsity phase)
268	    status: confirmed
269	  C3:
270	    description: Phase-strategy crossover exists
271	    status: confirmed
272	  C4:
273	    description: Discrimination collapse as primary mechanism; entropy redistribution
274	      model-dependent
275	    status: partially_confirmed
276	  C5:
277	    description: Phase-modulated compound severity generalizes across models
278	    status: confirmed
279	  C5b:
280	    description: Phase-aware mitigation recovers compound degradation
281	    status: future_work
282	  C6:
283	    description: Severity gradient is sub-exponential
284	    status: confirmed
285	  C7:
286	    description: Statistical power at n=500 confirms dose-response
287	    status: running
288	  C8:
289	    description: Cross-architecture validation (LLaMA)
290	    status: partially_confirmed
291	  C9:
292	    description: Differentiation from Lethe/SparK prior work
293	    status: planned
294	  C10:
295	    description: Phase gradient cross-benchmark robust; strategy specificity task-modulated
296	    status: running
297	  S3->C:
298	    description: Onset threshold is model-dependent
299	    status: confirmed
300	  S7->C:
301	    description: Dose-response monotonicity (Spearman rho=1.0)
302	    status: confirmed
303	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9294d03f-322b-4178-ac74-688d4652d186",
  "isSidechain": false,
  "promptId": "b55edb12-8b05-4782-9d97-5ec5c1db7737",
  "type": "user",
  "uuid": "6808a564-d31b-45ca-aaa2-25854eb9dbf4",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/experiment_plan.yaml",
      "content": "# experiment_plan.yaml — Retrospective experiment-to-claim mapping\n# Generated 2026-05-16 | project: phase-gated-compound-sparse\n# 38 experiments mapped across 13 claims\n\nexperiments:\n- id: c1_bf16_importance_s025\n  claim: C1\n  description: 'II median: high=0.032, mid=1.118, low=7.196; importance masking shows\n    strong phase gradient'\n  registry_id: bf16_importance_s025\n  role: primary\n  priority: high\n- id: c1_bf16_ds_rand_s025\n  claim: C1\n  description: 'Random II median: high=0.818, mid=0.932, low=1.363; flat gradient\n    vs importance'\n  registry_id: bf16_ds_rand_s025\n  role: primary\n  priority: high\n- id: c1_bf16_qw_imp_s025\n  claim: C1\n  description: 'Qwen cross-model: median_diff=1.109, Cohen''s d=1.233, p<1e-5'\n  registry_id: bf16_qw_imp_s025\n  role: supporting\n  priority: medium\n- id: c1_sf5_asymmetric_spot\n  claim: C1\n  description: 'Asymmetric configs: h02_kv03 D=19.13, h03_kv02 D=18.25; gradient consistent'\n  registry_id: sf5_asymmetric_spot\n  role: ablation\n  priority: medium\n- id: c1_c2_accuracy_eval\n  claim: C1\n  description: 'DS dense->s030 acc: 0.52->0.10 (-0.42); QW dense->s030: 0.32->0.14\n    (-0.18)'\n  registry_id: c2_accuracy_eval\n  role: supporting\n  priority: medium\n- id: c2_bf16_importance_s030\n  claim: C2\n  description: 'Phase gradient: II low=14.64 >> mid=2.28 >> high=0.053 (median); low/high\n    ratio ~276x'\n  registry_id: bf16_importance_s030\n  role: primary\n  priority: high\n- id: c2_v6_importance_s030\n  claim: C2\n  description: II low_median=34.69, mid_median=7.27, high_median=0.88; bootstrap_gradient=41.92,\n    CI=[19.14,299.76]\n  registry_id: v6_importance_s030\n  role: primary\n  priority: high\n- id: c2_think_phase_validation\n  claim: C2\n  description: Phase segmentation kappa=0.887; thinking=57.8% low-sparsity, answer=62.7%\n    high-sparsity\n  registry_id: think_phase_validation\n  role: supporting\n  priority: medium\n- id: c2_acc_qw_s030_n100\n  claim: C2\n  description: QW importance s030 accuracy=0.19 (n=100); dose-response monotonic decline\n    from dense=0.40\n  registry_id: acc_qw_s030_n100\n  role: supporting\n  priority: medium\n- id: c2_acc_ds_s015_8k_v2\n  claim: C2\n  description: DS s015 accuracy=0.48 vs dense=0.74; early onset of compound degradation\n  registry_id: acc_ds_s015_8k_v2\n  role: supporting\n  priority: medium\n- id: c3_v6_importance_s025\n  claim: C3\n  description: 'Importance: II low_median=24.16 >> high_median=0.66; strong phase\n    gradient (36x ratio)'\n  registry_id: v6_importance_s025\n  role: primary\n  priority: high\n- id: c3_v6_random_s025\n  claim: C3\n  description: 'Random: II low_median=2.91 ~ high_median=3.00; flat phase gradient\n    (bootstrap_p=0.559)'\n  registry_id: v6_random_s025\n  role: primary\n  priority: high\n- id: c3_bf16_importance_s020\n  claim: C3\n  description: 'Importance: II low=1.50, mid=0.20, high=0.015 (median); clear phase\n    separation'\n  registry_id: bf16_importance_s020\n  role: supporting\n  priority: medium\n- id: c3_bf16_ds_rand_s020\n  claim: C3\n  description: 'Random: II high=0.292, mid=0.350, low=0.276 (median); no phase separation'\n  registry_id: bf16_ds_rand_s020\n  role: supporting\n  priority: medium\n- id: c4_c4_entropy\n  claim: C4\n  description: 'DS importance entropy_delta: -0.04 to -0.05 (collapse); random: +0.13\n    to +0.23 (redistribution). Gini_delta: -0.03 to -0.08'\n  registry_id: c4_entropy\n  role: primary\n  priority: high\n- id: c4_qwen_c4_entropy\n  claim: C4\n  description: 'QW importance entropy_delta mixed: s015=-0.073, s025=+0.045; Gini\n    weaker (-0.01 to -0.02). Model-dependent pattern'\n  registry_id: qwen_c4_entropy\n  role: primary\n  priority: high\n- id: c5_bf16_qw_imp_s030\n  claim: C5\n  description: 'Qwen: median_diff=2.619, Cohen''s d=1.439, p<1e-5; replicates DeepSeek\n    pattern'\n  registry_id: bf16_qw_imp_s030\n  role: primary\n  priority: high\n- id: c5_bf16_importance_s030\n  claim: C5\n  description: 'DeepSeek: II low_median=14.64, high_median=0.053; strong phase gradient'\n  registry_id: bf16_importance_s030\n  role: primary\n  priority: high\n- id: c5_c2_n500_deepseek\n  claim: C5\n  description: 'DS n=500: imp_s030 median_II=8.48, CI=[7.46,9.56], p=1.3e-78; robust\n    at scale'\n  registry_id: c2_n500_deepseek\n  role: supporting\n  priority: medium\n- id: c5_c2_qw_n500_r3\n  claim: C5\n  description: 'QW n=500: imp_s030 median_II=4.33, p<1e-40; cross-model replication\n    at high power'\n  registry_id: c2_qw_n500_r3\n  role: supporting\n  priority: medium\n- id: c5b_c5b_pilot\n  claim: C5b\n  description: 'Oracle recovery=18% (gate: >30% FAIL); heuristic recovery=31.7% but\n    CI crosses zero. s030 incomplete'\n  registry_id: c5b_pilot\n  role: primary\n  priority: high\n- id: c6_bf16_importance_s015\n  claim: C6\n  description: II low_median=0.398 at s=0.15\n  registry_id: bf16_importance_s015\n  role: primary\n  priority: high\n- id: c6_bf16_importance_s020\n  claim: C6\n  description: II low_median=1.496 at s=0.20\n  registry_id: bf16_importance_s020\n  role: supporting\n  priority: medium\n- id: c6_bf16_importance_s025\n  claim: C6\n  description: II low_median=7.196 at s=0.25\n  registry_id: bf16_importance_s025\n  role: supporting\n  priority: medium\n- id: c6_bf16_importance_s030\n  claim: C6\n  description: II low_median=14.64 at s=0.30; growth 0.40->1.50->7.20->14.64 is sub-exponential\n  registry_id: bf16_importance_s030\n  role: supporting\n  priority: medium\n- id: c7_c2_n500_deepseek\n  claim: C7\n  description: 'DS n=500: all 4 sparsities significant (p<1e-70); CIs non-overlapping\n    across dose levels'\n  registry_id: c2_n500_deepseek\n  role: primary\n  priority: high\n- id: c7_c2_qw_n500_r3\n  claim: C7\n  description: 'QW n=500: all 4 sparsities significant (p<1e-14 Bonferroni-corrected);\n    mid_null_rate=45.2%'\n  registry_id: c2_qw_n500_r3\n  role: primary\n  priority: high\n- id: c8_c3_llama\n  claim: C8\n  description: LLaMA-8B (LlamaForCausalLM) replicates phase-modulated compound severity\n    from Qwen2ForCausalLM\n  registry_id: c3_llama\n  role: primary\n  priority: high\n- id: c10_gsm8k_profiling_ds\n  claim: C10\n  description: 'DS GSM8K importance gradient: s015=0.241, s020=0.740, s025=1.992,\n    s030=4.636 (monotonic)'\n  registry_id: gsm8k_profiling_ds\n  role: primary\n  priority: high\n- id: c10_gsm8k_profiling_qw\n  claim: C10\n  description: 'QW GSM8K importance gradient: s015=0.039, s020=0.158, s025=1.100,\n    s030=2.092 (monotonic)'\n  registry_id: gsm8k_profiling_qw\n  role: primary\n  priority: high\n- id: c10_gsm8k_qw_rand_s025_v2\n  claim: C10\n  description: 'QW random s025 GSM8K: II median_high=0.72, low=1.48; phase gradient\n    weaker than importance'\n  registry_id: gsm8k_qw_rand_s025_v2\n  role: supporting\n  priority: medium\n- id: c10_gsm8k_qw_rand_s030_v2\n  claim: C10\n  description: 'QW random s030 GSM8K: II median_high=2.31, low=5.87; compound effect\n    on GSM8K confirmed'\n  registry_id: gsm8k_qw_rand_s030_v2\n  role: supporting\n  priority: medium\n- id: s3_c_bf16_ds_imp_s010\n  claim: S3->C\n  description: 'DS s=0.10: II_high_median=0.003, verdict=FAIL; below onset threshold\n    for DeepSeek'\n  registry_id: bf16_ds_imp_s010\n  role: primary\n  priority: high\n- id: s3_c_bf16_qw_imp_s010\n  claim: S3->C\n  description: 'QW s=0.10: overall_verdict=PASS, CI_overlap_test=PASS; Qwen onset\n    earlier than DeepSeek'\n  registry_id: bf16_qw_imp_s010\n  role: primary\n  priority: high\n- id: s3_c_bf16_qw_imp_s015\n  claim: S3->C\n  description: 'QW s=0.15: median_diff=0.048, permutation_p=0.0001; confirmed above\n    threshold'\n  registry_id: bf16_qw_imp_s015\n  role: supporting\n  priority: medium\n- id: s7_c_c2_n500_deepseek\n  claim: S7->C\n  description: 'DS n=500 monotonic: imp median II 0.39->1.21->3.99->8.48 across s015-s030\n    (Spearman rho=1.0)'\n  registry_id: c2_n500_deepseek\n  role: primary\n  priority: high\n- id: s7_c_c2_qw_n500_r3\n  claim: S7->C\n  description: 'QW n=500 monotonic: imp median II 0.066->0.307->1.075->4.33 across\n    s015-s030 (Spearman rho=1.0)'\n  registry_id: c2_qw_n500_r3\n  role: primary\n  priority: high\n- id: s7_c_bf16_qw_imp_s035\n  claim: S7->C\n  description: 'QW s=0.35: low_II_median=8.24; extends dose-response beyond s030'\n  registry_id: bf16_qw_imp_s035\n  role: supporting\n  priority: medium\n_claims:\n  C1:\n    description: Compound sparsity severity is strategy- and task-modulated\n    status: confirmed\n  C2:\n    description: Severity is phase-modulated (amplified in low-sparsity phase)\n    status: confirmed\n  C3:\n    description: Phase-strategy crossover exists\n    status: confirmed\n  C4:\n    description: Discrimination collapse as primary mechanism; entropy redistribution\n      model-dependent\n    status: partially_confirmed\n  C5:\n    description: Phase-modulated compound severity generalizes across models\n    status: confirmed\n  C5b:\n    description: Phase-aware mitigation recovers compound degradation\n    status: future_work\n  C6:\n    description: Severity gradient is sub-exponential\n    status: confirmed\n  C7:\n    description: Statistical power at n=500 confirms dose-response\n    status: running\n  C8:\n    description: Cross-architecture validation (LLaMA)\n    status: partially_confirmed\n  C9:\n    description: Differentiation from Lethe/SparK prior work\n    status: planned\n  C10:\n    description: Phase gradient cross-benchmark robust; strategy specificity task-modulated\n    status: running\n  S3->C:\n    description: Onset threshold is model-dependent\n    status: confirmed\n  S7->C:\n    description: Dose-response monotonicity (Spearman rho=1.0)\n    status: confirmed\n",
      "numLines": 303,
      "startLine": 1,
      "totalLines": 303
    }
  },
  "sourceToolAssistantUUID": "9294d03f-322b-4178-ac74-688d4652d186",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "801dd6fc-5861-4c46-a727-64581ec2a334",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 20 · 2026-05-17T01:30:45.907Z_

````json
{
  "parentUuid": "6808a564-d31b-45ca-aaa2-25854eb9dbf4",
  "isSidechain": false,
  "attachment": {
    "type": "nested_memory",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/CLAUDE.md",
    "content": {
      "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/CLAUDE.md",
      "type": "Project",
      "content": "## 当前项目\n当前绑定项目：**phase-gated-compound-sparse**\n\n## 按需查阅\n- 项目配置：`load_project_config(\"phase-gated-compound-sparse\")` 或 `load_project_config(\"phase-gated-compound-sparse\", section=\"execution\")`\n- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）\n- 路线图：`read_roadmap()` 读取研究方向和短期任务\n- 产出目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/`（写文件后用 `register_artifact` 注册）\n\n## Worker 操作规范\n\n### paper-writing-norms\n\n# 论文写作风格规范\n\n> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。\n\n---\n\n## 一、总体写作哲学\n\n### 1.1 故事驱动，不是数据堆砌\n\n- 论文必须以\"故事线\"为核心展开：问题 → 洞察 → 方法 → 验证\n- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进\n- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌\n- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing\n\n### 1.2 主线统一性\n\n- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**\n- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C\n- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机\n- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线\n\n### 1.3 专有名词必须有定义\n\n- 首次出现的专有名词/缩写必须给出完整定义和解释\n- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）\n- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用\n- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug\n\n### 1.4 写作前必读同类优秀论文\n\n- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可\n- 重点学：\n  - Abstract 怎么用最少篇幅讲完故事\n  - Introduction 怎么从大问题切入到具体贡献\n  - Related Work 怎么 positioning 自己（不是 survey）\n  - Table/Figure 怎么压缩信息密度\n- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大\n- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文\n\n---\n\n## 二、Abstract 写作规范\n\n### 2.1 四个必答问题（150-250 words）\n\nAbstract 必须在很短的篇幅内清楚回答：\n1. **研究什么问题** — 1-2 句话交代背景和痛点\n2. **为什么重要** — 现有方法的不足（不用写太多）\n3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）\n4. **结果说明什么** — 用具体实验结论支撑贡献\n\n### 2.2 禁忌\n\n- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim\n- **禁止过度宣传**：不说 \"revolutionary\"、\"groundbreaking\"\n- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元\n- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了\n- **缩写必须定义**：Abstract 中首次出现的缩写必须展开\n\n### 2.3 审稿人视角检验\n\n写完后用这个标准自检：审稿人能否在 30 秒内判断——\n- 问题是否重要？\n- 方法是否清楚？\n- 贡献是否可信？\n- 结果是否有说服力？\n\n---\n\n## 三、Introduction 写作规范\n\n### 3.1 完整叙事线（5 段结构）\n\nIntroduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：\n\n1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈\n2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题\n3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）\n4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题\n5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献\n\n### 3.2 整体叙事结构\n\n```\n现有进展 → 关键缺口 → 本文洞察 → 方法概述 → 实验证据 → 贡献总结\n```\n\n### 3.3 禁忌\n\n- **禁止泛泛介绍**：不要开头就写 \"LLMs have shown remarkable capabilities...\"，要从具体问题切入\n- **禁止缺少过渡**：每段之间必须有逻辑连接\n- **禁止实验报告风格**：Introduction 不是 \"我们做了 X 实验得到了 Y 结果\" 的罗列\n- 每条 Contribution 必须有对应的 section/table 支撑\n- Contribution 列表中不能出现未在前文铺垫过的概念\n\n---\n\n## 四、Related Work 写作规范\n\n### 4.1 目标\n\n让审稿人相信：作者理解这个领域，知道自己的方法站在什么位置，清楚相对已有工作的真实增量在哪里。\n\n### 4.2 结构要求\n\n- 把已有工作分成几个清晰的主题（如模型训练、推理增强、工具调用、数据构建、评测等）\n- 每类简要说明：已有方法做了什么、解决了哪些问题、和本文的关系\n- 帮助读者理解：哪些是本文直接继承的，哪些方法不同但解决相似问题，哪些留下了本文要解决的缺口\n\n### 4.3 禁忌\n\n- **禁止论文堆砌**：不要写成 \"A proposed X. B proposed Y. C proposed Z.\" 的列表\n- **目标不是展示读了多少论文**，而是做归纳和比较\n- Contribution claim（\"To our knowledge, no prior work...\"）应放在 Introduction，不在 Related Work\n\n### 4.4 引用充足度\n\n- 引用必须覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**\n- 任何一类缺失，审稿人会立刻看出来调研不充分\n- 引用密度参照目标会议近年录用论文的量级——明显偏少意味着 Related Work 调研不足\n\n---\n\n## 五、去 AI 写作风格（硬规则）\n\n以下模式是 AI 生成文本的典型标志，审稿人一眼能看出。**必须全部消除。**\n\n### 5.1 严禁破折号（最显著的 AI 痕迹）\n\n**这是 AI 写作最容易被识别的标志，审稿人最敏感。单列为最高优先级硬规则。**\n\n- 解释性 em-dash（—，U+2014）和 en-dash（–，U+2013）必须**全部删除**\n- 替代方式：用逗号、括号或拆分为两个句子\n- 强制检查命令：\n  ```bash\n  grep -n \"—\" paper/*.tex     # em-dash，每处人工判断是否必要\n  grep -n \" – \" paper/*.tex   # 解释性 en-dash，几乎都应删除\n  ```\n- 例外（允许保留）：表格分隔符、数字范围（`2020–2024`、`pp. 12–18`）、专有名词（`Newton–Raphson`）\n\n### 5.2 段落与句式\n\n- **禁止过度分段**：不需要每 2-3 句就换段，自然段 5-8 句是正常的\n- **减少关系从句**（which, that, who）：能用简洁直接的句子就不用从句\n- **禁止 -ing 短语结尾**：如 \"..., highlighting the applicability of...\" / \"..., demonstrating the effectiveness of...\"。这是 AI 写作最典型的标志之一\n- **禁止连续使用 \"Furthermore\" / \"Moreover\" / \"Additionally\"**：一段内最多用一个过渡词\n- **避免 \"It is worth noting that...\" / \"Notably, ...\"**：直接写要说的内容\n\n### 5.3 用词黑名单\n\n- 避免 \"delve into\" / \"leverage\" / \"utilize\" / \"facilitate\" — 用 \"explore\" / \"use\" / \"enable\"\n- 避免 \"a myriad of\" / \"a plethora of\" — 用 \"many\" / \"various\"\n- 避免 \"in the realm of\" / \"in the context of\" — 直接说\n- 避免 \"paradigm shift\" / \"novel\" 过度使用\n\n### 5.4 校对清单（4 步）\n\n1. 全文 proofread 语法和拼写\n2. 检查所有代词/指示词（this, that, it）是否指代明确\n3. **`grep \"—\"` + `grep \" – \"` 全文清零**（删除所有解释性 dash，§5.1）\n4. `grep \"ing,\"` 模式——大部分 -ing 分词短语需要改写\n\n---\n\n## 六、图表与视觉规范\n\n### 6.1 知识密度原则\n\n- **图表的信息必须紧凑**——不能为了美观而留大量白空间\n- 一张图如果只传达一个简单信息，要么缩小要么合并到其他图中\n- 能用 inline text 说清的不要占一整个 Figure\n\n### 6.2 表格规范\n\n- 表格和正文文字不能视觉重叠（检查 column 宽度和 alignment）\n- 小数精度全表统一\n- 最优加粗、次优下划线\n- Caption 必须自包含\n\n### 6.3 图片规范\n\n- 数值标签不能被线、bar、点遮住——用白色背景或偏移标签\n- 图中字体 >= 7pt（打印后仍可读）\n- 栏宽约束需匹配目标 venue 模板要求\n- 概念图/流程图要有信息量，不要画一个 trivial 的 pipeline 然后占半页\n\n### 6.4 空间效率\n\n- 顶会正文页数严格受限（具体页数查目标会议官网），每 cm² 都是宝贵资源\n- 优先使用 `\\subfigure` 合并相关图\n- Table 能 inline 就不要单独浮动\n- 图表占比与其对叙事的贡献成正比\n\n---\n\n## 七、投稿前通用准备\n\n### 7.1 模板必须官方（硬规则）\n\n- LaTeX 模板**必须从目标会议官网下载**（CallForPapers / Author Instructions 页面）\n- **不要用**：\n  - 网上他人转载的复制版本（可能被改过 margin / 行号设置）\n  - 上一年的模板（参数可能变：字体、margin、行号、anonymous 选项等）\n  - 组里学长留的旧版本（来源不明、无法追溯）\n- 风险：\n  - 样式不符合 → desk reject\n  - margin 不对 → 被审稿人质疑诚信\n  - reference 格式错 → 被认为不规范\n- 流程：先查会议官网 templates → 找不到再 `WebSearch \"{venue} {year} latex template official\"` → 仍找不到汇报 Director（不要用就近年版本顶替）\n- `\\documentclass[]{}` 选项必须与目标 venue + 阶段（review / camera-ready）一致\n\n### 7.2 投稿要求逐项核对\n\n- 目标会议如要求 Checklist / Ethical Statement / Broader Impact Statement / Reproducibility Statement，必须**认真填每一项**，不要全写 N/A\n- 页数限制：查目标会议官网\n- 匿名化要求：review 版 vs camera-ready 版本设置不同\n- 行号开启（review 版常需）\n- 字体大小、margin 不得修改 sty 文件\n\n### 7.3 最终修改 10 项检查流程\n\n提交前必须逐一检查：\n1. 所有最新实验结果已全部录入\n2. 根据实验结果将叙事调至最优状态\n3. 附录所有内容在正文中被引用且融入叙事\n4. 无数据堆砌（每个数字服务于叙事推进）\n5. Abstract 和 Introduction 具有吸引力（不是实验报告风格）\n6. 全文主线统一（idea 变化后各章节逻辑一致）\n7. 所有专有名词有定义\n8. 无 AI 风格标志（dash、-ing phrases、过度分段）\n9. 图表知识密度高、无视觉遮挡\n10. Reference 覆盖直接相关方法、baseline、benchmark、理论基础\n\n## 更多 Skills（按需加载）\n\n执行相关任务前，先 Read 对应 skill 获取环境配置和最佳实践。\n\n- **ssh-env-setup** — 远程服务器 Python/CUDA 环境搭建规范——discovery-first 流程、PEP 668 处理、PyTorch 版本选择。当需要在远程服务器搭建训练环境时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ssh-env-setup.skill.md`\n- **check-training-status** — 当用户问训练进度/实验状态/查状态时使用。用专用工具查看训练状态，禁止 ssh_execute。  →  `/home/ubuntu/agent-ml-research/skills/global/check-training-status.skill.md`\n- **rebuttal** — 撰写和优化学术 rebuttal——逐条回应审稿意见，生成 response letter。当收到审稿意见、需要写 rebuttal、回复 reviewer 评论时使用。关键词：rebuttal、审稿意见、reviewer response、author response、meta-review、AC 意见。  →  `/home/ubuntu/agent-ml-research/skills/global/rebuttal.skill.md`\n- **review-reviewer-session-start** — Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。  →  `/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md`\n- **reference-audit** — 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。  →  `/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md`\n- **accelerate-distributed** — HuggingFace Accelerate 分布式训练指南——4行代码实现多GPU/DeepSpeed/FSDP/混合精度。多GPU训练时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/accelerate-distributed.skill.md`\n- **draw-paper-figure** — 生成学术论文级 matplotlib 图表——reliability diagrams、ECE heatmap、T* scatter plot、模型对比图，直接在 A6000 服务器上执行，输出 PDF/PNG  →  `/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md`\n- **experiment-analysis** — 实验结果分析框架——统计显著性检验、消融分析、baseline 对比、可视化建议。分析实验结果或撰写论文 Results 部分时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/experiment-analysis.skill.md`\n- **hf-hub** — HuggingFace Hub CLI (hf) — 下载/上传模型和数据集、管理缓存、搜索论文和模型。涉及 HuggingFace 资源操作时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/hf-hub.skill.md`\n- **latex-paper** — ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`\n- **lm-eval-harness** — lm-evaluation-harness 模型评估指南——MMLU/GSM8K/HumanEval 等 60+ 学术基准测试。评估模型质量、对比实验时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/lm-eval-harness.skill.md`\n- **ml-experiment-guide** — 跨项目 ML 实验避坑指南——从多个项目沉淀的通用踩坑经验与最佳实践。当 Worker 准备写实验代码、或排查实验问题时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ml-experiment-guide.skill.md`\n- **paper-banana** — 用 PaperBanana 生成发表级学术统计图——LLM 写 matplotlib 代码 + Critic 迭代 3 轮，输入 CSV/JSON 数据 + 意图描述即可。需要 GOOGLE_API_KEY。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-banana.skill.md`\n- **paper-image-extractor** — 从论文 PDF 或 arXiv 源码包提取图表——优先 arXiv 原始图片，回退 PDF 解析。用户说\"提取图\"/\"抽图\"/\"extract figures\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-image-extractor.skill.md`\n- **peft-lora** — PEFT/LoRA/QLoRA 参数高效微调指南——LoRA 配置选择、QLoRA 量化训练、Adapter 管理与合并。微调大模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/peft-lora.skill.md`\n- **research-news** — 每日论文推荐——搜索 arXiv 最新论文，按相关性/新颖性/影响力评分，生成推荐列表。Director 说\"有什么新论文\"/\"最近进展\"/\"research news\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/research-news.skill.md`\n- **trl-training** — TRL (Transformer Reinforcement Learning) 训练指南——SFT/DPO/GRPO/KTO 配置与最佳实践。训练或对齐语言模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/trl-training.skill.md`\n- **wandb-guide** — W&B 查询最佳实践——如何高效使用 fetch_wandb_metrics / compare_wandb_runs / get_best_wandb_run 分析实验结果。分析实验指标时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/wandb-guide.skill.md`\n",
      "contentDiffersFromDisk": false
    },
    "displayPath": "projects/phase-gated-compound-sparse/.claude/CLAUDE.md"
  },
  "type": "attachment",
  "uuid": "96e19899-c3dd-4e9a-8743-02ea7786d287",
  "timestamp": "2026-05-17T01:30:45.907Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "801dd6fc-5861-4c46-a727-64581ec2a334",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Reviewers fully accept empirical-finding framing; recency control + triple dissociation seen as clean novel contribution; cross-architecture variation trea…",
  "leafUuid": "96e19899-c3dd-4e9a-8743-02ea7786d287",
  "sessionId": "801dd6fc-5861-4c46-a727-64581ec2a334"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Phase-modulated compound sparsity with recency control confirmed",
  "sessionId": "801dd6fc-5861-4c46-a727-64581ec2a334"
}
```

---

### Assistant

_source line 23 · 2026-05-17T01:31:46.475Z_

<details><summary>Logged reasoning block</summary>

```text
Now I see the full picture. The experiment_plan.yaml has all experiments but they're all listed as entries that have been done. The claims status at the bottom shows:
- C9: planned
- C7: running
- C10: running

And in the registry, there are RUNNING experiments:
- gpqa_ds_importance_s020
- gpqa_ds_importance_s025
- gpqa_ds_importance_s030
- gpqa_ds_random_s020

These GPQA experiments appear to be a NEW cross-benchmark validation (GPQA as a third benchmark beyond MATH-500 and GSM8K). 

I need to figure out what the user actually means by "planned" experiments - they might be referring to the claims with planned status, the currently running experiments in the registry, or perhaps there's a separate file I haven't found yet with planned experiments that haven't been added to the main plan yet. Looking at the remaining RUNNING experiments—gpqa_ds_importance_s025, s030, and gpqa_ds_random_s020—these are all part of validating the phase gradient finding across a harder benchmark to strengthen the cross-benchmark robustness claim. In the "best" scenario where reviewers accept the empirical-finding framing and view the recency control plus triple dissociation as a clean novel contribution, I'd expect these GPQA results to confirm the phase gradient pattern and demonstrate monotonic scaling behavior, which would reinforce C10's expansion to a third benchmark.

Now I'm looking at the reference data from GPQA s015 and the scaling patterns from MATH-500 to project what these upcoming results might show.

I'm noticing that GPQA has much longer reasoning chains than MATH-500, and the s015 already demonstrates a 75.2x low-to-high ratio, which suggests the scaling dynamics might differ from what I'm seeing in MATH-500. has low=0.398, high=0.006, ratio ~66x). GPQA is probably a harder benchmark with more reasoning-intensive problems, so we'd expect:
- Stronger phase gradients (more tokens in reasoning phases)
- Possibly stronger strategy specificity (because more complex reasoning = more reliance on importance-based attention patterns)

Let me refine predictions:

**gpqa_ds_importance_s020:**
- Based on MATH-500 scaling and GPQA s015 as anchor
- high median: 0.0128 × (0.0145/0.0058) ≈ 0.032 (scaling from s015→s020 high ratio in MATH-500)
- Actually, let me be more careful. In MATH-500:
  - s015 high median = 0.0058, s020 high median = 0.0145 (2.5x)
  - s015 mid median = 0.081, s020 mid median = 0.203 (2.5x)
  - s015 low median = 0.398, s020 low median = 1.496 (3.8x)
  - median_diff = 0.393, s020 median_diff = 1.482 (3.8x)

Now applying these scaling factors to GPQA, where s015 gives me high=0.0128, mid=0.1024, low=0.960. If I scale by the same ratios, s020 should reach roughly high≈0.032, mid≈0.256, low≈3.65, with a median difference around 3.62.

But GPQA problems are substantially longer than MATH-500 (1.2M tokens vs 62K), meaning more reasoning content and more opportunities for the compound effect to accumulate. So the scaling might be even stronger. Let me adjust my predictions upward: s020 median_diff around 3.2-4.0, s025 around 10-14, and s030 around 20-30.

For the random baseline at s020 in GPQA, I need to check what happened in MATH-500—there it was not significant with median_diff=-0.016 and p=0.28. I'm trying to figure out what that means for GPQA's random performance at s020.

Now I'm thinking about what the "best" tier results should look like: clear confirmation of the phase gradient across all GPQA conditions, monotonic dose-response, strategy specificity somewhere between the extremes I've seen (maybe 5-10× as a moderate value reflecting task complexity), and random at s020 staying non-significant to support the threshold hypothesis. Let me work out precise predictions for these scenarios.

Actually, I should check whether there are other planned experiments beyond GPQA that I need to account for. Looking at the experiment plan file, I notice the GPQA experiments are currently running but aren't actually listed in the experiment_plan.yaml itself—that file only contains the C1-C10 entries. So the "planned" experiments the user is asking about are really just the GPQA series that's already in progress, plus maybe C9 which is about related work differentiation but that's more of a writing task than an experimental one. Let me focus on what's actually testable with the GPQA data. 对 experiment_plan 中每个 planned 实验展开详细数据。也许用户指的是计划中引用但在声明级别有"planned"状态的实验？

声明中非确认状态的有：
- C9: planned（与 Lethe/SparK 的区分）
- C5b: future_work（阶段感知缓解）
- C4: partially_confirmed（判别崩溃）

但 C5b 明确是"future_work"，C4 的实验已完成（只是部分确认）。C9 没有实验条目。

我觉得用户可能搞混了，或者他们问的是当前运行的 GPQA 实验，这些是为了扩展 C10 的下一步实验。让我查看注册表中当前运行或计划中的所有实验。

看了注册表条目后，我发现有一系列清晰的 GPQA 实验：s020、s025、s030 都在运行中，还有随机版本的 s020。我会为这些运行中的实验和 C9（作为写作/框架任务）生成预测。

现在我要生成最终的 YAML 输出，为"best"层级提供详细的预测。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96e19899-c3dd-4e9a-8743-02ea7786d287",
  "isSidechain": false,
  "requestId": "req_011Cb7Gz8K8dLQKKLofZ22PH",
  "type": "assistant",
  "uuid": "b5327844-ff6a-40ab-9d6a-f1476f25b60a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "801dd6fc-5861-4c46-a727-64581ec2a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FYmL9wPirBunqDBKuSz6iF",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10669,
      "cache_read_input_tokens": 74830,
      "output_tokens": 8311,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10669,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8311,
          "cache_read_input_tokens": 74830,
          "cache_creation_input_tokens": 10669,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10669
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

_source line 24 · 2026-05-17T01:33:36.169Z_

Now I have the full picture. The RUNNING/planned experiments are:
- `gpqa_ds_importance_s020`, `gpqa_ds_importance_s025`, `gpqa_ds_importance_s030` (RUNNING)
- `gpqa_ds_random_s020` (RUNNING)
- C9 (planned - writing/framing task)

These extend C10 (cross-benchmark validation) to GPQA as a third, harder benchmark. Let me generate predictions calibrated to the "best" tier.

```yaml
tier: best
narrative_guidance: |
  Best tier: Reviewers accept GPQA as compelling third-benchmark evidence. Phase gradient monotonic on GPQA confirms reasoning-complexity-dependence of the compound interaction. Strategy specificity ratio on GPQA falls between MATH-500 (15-17×) and GSM8K (2.3-3.8×), naturally interpreted as task-complexity gradient (GPQA > MATH-500 > GSM8K in reasoning depth, correlating with specificity). Random NS at s020 on GPQA further strengthens triple dissociation alongside recency control. No reviewer raises GPQA-specific methodology concern. C9 differentiation via 50-citation related work + explicit gap analysis fully resolves novelty concern.

imagined_experiments:
  - name: "GPQA DS Importance s020"
    plan_id: "gpqa_ds_importance_s020"
    description: "DeepSeek importance masking phase gradient on GPQA at sparsity=0.20, n=198"
    expected_results:
      n_problems: 198
      interaction_index_high_median: 0.038
      interaction_index_high_ci: [0.031, 0.048]
      interaction_index_mid_median: 0.342
      interaction_index_mid_ci: [0.278, 0.421]
      interaction_index_low_median: 3.24
      interaction_index_low_ci: [2.81, 3.72]
      median_difference: 3.20
      median_difference_ci: [2.76, 3.69]
      wilcoxon_p: 1.8e-32
      cohens_dz: 0.89
      gradient_direction: "low > mid > high (monotonic)"
      median_ratio_low_high: 85.3
      pass_fail: PASS
      perplexity_high_both: 2.65
      perplexity_mid_both: 8.12
      perplexity_low_both: 42.8
    result_rationale: |
      GPQA problems have substantially longer reasoning chains than MATH-500 (avg ~6100 tokens vs ~1200), 
      providing more token-level observations per problem and stronger statistical separation between phases.
      At s015, GPQA already showed median_ratio_low_high=75.2× (vs MATH-500 ~66×), indicating GPQA's 
      deeper reasoning amplifies the phase gradient. Scaling s015→s020 in MATH-500 shows ~3.8× increase 
      in low_median (0.398→1.496). Applying similar scaling to GPQA s015 low=0.960 gives ~3.4× = 3.24.
      The slightly smaller scaling factor (3.4× vs 3.8×) reflects diminishing returns at higher absolute 
      II values on longer sequences. High phase stays near-zero because compound interaction barely 
      manifests in answer-formatting tokens regardless of sparsity level. Wilcoxon p is extremely small
      due to n=198 effective pairs (vs n=50 in MATH-500), giving massive statistical power.
      In best tier, this cleanly extends the dose-response to a third benchmark with no complications.
    tables:
      - name: "Table S-GPQA-1: GPQA Importance Phase Gradient (s020)"
        columns: [phase, n_tokens, n_segments, II_median, II_mean, "95% CI"]
        rows:
          - [high, 479658, 6261, 0.038, 0.52, "[0.031, 0.048]"]
          - [mid, 276409, 2185, 0.342, 1.89, "[0.278, 0.421]"]
          - [low, 465085, 5128, 3.24, 12.6, "[2.81, 3.72]"]
    figures_description:
      - "Dose-response subplot in Figure 3(c): GPQA importance gradient 0.96→3.24→X→Y across s015-s030, parallel line above GSM8K and below MATH-500 per-token-normalized values"
    analysis: |
      GPQA s020 confirms phase gradient on graduate-level science reasoning. The effect size (d_z=0.89) 
      is larger than MATH-500 s020 (d_z≈0.73) due to both longer reasoning chains providing more 
      statistical leverage and harder problems intensifying reliance on attention-score-based token 
      selection. The median_ratio_low_high=85.3× exceeds MATH-500 (~103× at s020), consistent with 
      reasoning-difficulty amplifying the phase-strategy interaction.

  - name: "GPQA DS Importance s025"
    plan_id: "gpqa_ds_importance_s025"
    description: "DeepSeek importance masking phase gradient on GPQA at sparsity=0.25, n=198"
    expected_results:
      n_problems: 198
      interaction_index_high_median: 0.098
      interaction_index_high_ci: [0.072, 0.131]
      interaction_index_mid_median: 1.28
      interaction_index_mid_ci: [1.02, 1.61]
      interaction_index_low_median: 10.7
      interaction_index_low_ci: [9.1, 12.8]
      median_difference: 10.6
      median_difference_ci: [8.98, 12.7]
      wilcoxon_p: 3.2e-36
      cohens_dz: 1.04
      gradient_direction: "low > mid > high (monotonic)"
      median_ratio_low_high: 109.2
      pass_fail: PASS
      perplexity_high_both: 3.8
      perplexity_mid_both: 18.4
      perplexity_low_both: 89.2
    result_rationale: |
      Scaling from s020→s025 in MATH-500 shows ~3.3× increase (1.21→3.99 at n=500). Applying to 
      GPQA s020 predicted low=3.24 gives 3.24×3.3=10.7. This is consistent with the sub-exponential 
      growth pattern (C6): growth factor decreasing as sparsity increases. At s025, the compound 
      interaction enters a regime where discrimination collapse is severe enough to produce large 
      absolute II values even in the high-perplexity phase (low_median>10), but the phase gradient 
      remains strongly monotonic because importance-score discrimination degrades proportionally more 
      in low-sparsity reasoning phases where attention patterns are more distributed and pruning 
      removes more critical heads. The ratio 109.2× continues the trend of increasing ratio with 
      sparsity (75.2→85.3→109.2) because high-phase II grows slower than low-phase II.
      In best tier, the strong d_z=1.04 makes this among the clearest evidence points across all benchmarks.
    tables:
      - name: "Table S-GPQA-2: GPQA Importance Phase Gradient (s025)"
        columns: [phase, II_median, II_mean, "95% CI", wilcoxon_p]
        rows:
          - [high, 0.098, 0.84, "[0.072, 0.131]", "-"]
          - [mid, 1.28, 5.6, "[1.02, 1.61]", "-"]
          - [low, 10.7, 38.2, "[9.1, 12.8]", "-"]
          - ["gradient (low-high)", 10.6, "-", "[8.98, 12.7]", "3.2e-36"]
    figures_description:
      - "Contributes to Figure 3(c) GPQA dose-response curve: s025 point continues monotonic trajectory"
      - "Heatmap panel in Figure 4: GPQA row at s025 shows deep red in low-sparsity cell"
    analysis: |
      s025 is the critical sparsity level where MATH-500 showed the onset of random gradient significance 
      (DS: p=0.006). On GPQA, the importance gradient at s025 is massive (d_z=1.04), providing strong 
      contrast for the strategy specificity argument. This is the sparsity level where the crossover 
      phenomenon (C3) becomes most visible — importance dominates in low-phase while being near-zero in high-phase.

  - name: "GPQA DS Importance s030"
    plan_id: "gpqa_ds_importance_s030"
    description: "DeepSeek importance masking phase gradient on GPQA at sparsity=0.30, n=198"
    expected_results:
      n_problems: 198
      interaction_index_high_median: 0.21
      interaction_index_high_ci: [0.15, 0.29]
      interaction_index_mid_median: 3.4
      interaction_index_mid_ci: [2.6, 4.5]
      interaction_index_low_median: 22.8
      interaction_index_low_ci: [18.9, 28.1]
      median_difference: 22.6
      median_difference_ci: [18.7, 27.9]
      wilcoxon_p: 8.7e-38
      cohens_dz: 1.12
      gradient_direction: "low > mid > high (monotonic)"
      median_ratio_low_high: 108.6
      pass_fail: PASS
      dose_response_spearman_rho: 1.0
      dose_response_perm_p: 0.042
      perplexity_high_both: 5.1
      perplexity_mid_both: 34.6
      perplexity_low_both: 158.3
      gpqa_full_series_median_gradient: [0.960, 3.24, 10.7, 22.8]
    result_rationale: |
      Scaling s025→s030 in MATH-500 shows ~2.1× (3.99→8.48 at n=500). Applying to GPQA s025 predicted 
      low=10.7 gives 10.7×2.13=22.8. The sub-exponential growth continues (growth factors: 3.4×, 3.3×, 2.1×, 
      decreasing). At s030, both benchmarks (MATH-500 and GPQA) show saturation in the growth rate, 
      consistent with C6's sub-exponential claim. The absolute magnitude on GPQA (~22.8) substantially 
      exceeds MATH-500 (~8.48) at the same sparsity — this is expected because GPQA's longer reasoning 
      chains accumulate more compound degradation per problem. The ratio stabilizes (~109→108) because 
      at extreme sparsity even high-phase tokens start showing non-trivial II (0.21 vs near-zero at s015).
      In best tier, the complete 4-point GPQA dose-response (0.96→3.24→10.7→22.8) with Spearman ρ=1.0 
      provides unambiguous cross-benchmark validation. The monotonic series across three benchmarks 
      (MATH-500, GSM8K, GPQA) with consistent direction but task-dependent magnitude is exactly the 
      "interesting empirical finding" framing that reviewers accept.
    tables:
      - name: "Table S-GPQA-3: Complete GPQA Dose-Response (DS Importance)"
        columns: [sparsity, II_low_median, II_high_median, median_diff, "Cohen's d_z", p_value]
        rows:
          - ["0.15", 0.960, 0.013, 0.947, 0.78, "1.4e-29"]
          - ["0.20", 3.24, 0.038, 3.20, 0.89, "1.8e-32"]
          - ["0.25", 10.7, 0.098, 10.6, 1.04, "3.2e-36"]
          - ["0.30", 22.8, 0.21, 22.6, 1.12, "8.7e-38"]
    figures_description:
      - "Figure 3(c) complete: GPQA 4-point monotonic dose-response, steeper slope than MATH-500 when normalized by problem count"
      - "Cross-benchmark comparison figure: three parallel monotonic lines (MATH-500, GSM8K, GPQA) with different magnitudes but same direction — visual evidence of benchmark-robust phase gradient"
    analysis: |
      The complete GPQA series confirms cross-benchmark robustness on the hardest available benchmark.
      Key comparison: GPQA absolute magnitudes ~2.7× MATH-500 at each sparsity level (22.8 vs 8.48 at s030),
      attributable to longer reasoning chains (avg 6100 vs 1200 tokens). Growth rate pattern is consistent 
      (sub-exponential, factors 3.4→3.3→2.1 on GPQA vs 3.1→3.3→2.1 on MATH-500), confirming C6 
      cross-benchmark. Dose-response Spearman ρ=1.0 matches MATH-500 and GSM8K perfectly.

  - name: "GPQA DS Random s020"
    plan_id: "gpqa_ds_random_s020"
    description: "DeepSeek random masking phase gradient on GPQA at sparsity=0.20, n=198"
    expected_results:
      n_problems: 198
      interaction_index_high_median: 0.072
      interaction_index_high_ci: [0.048, 0.102]
      interaction_index_mid_median: 0.089
      interaction_index_mid_ci: [0.054, 0.138]
      interaction_index_low_median: 0.11
      interaction_index_low_ci: [0.067, 0.162]
      median_difference: 0.038
      median_difference_ci: [-0.021, 0.098]
      wilcoxon_p: 0.18
      cohens_dz: 0.08
      gradient_direction: "no significant gradient (flat)"
      pass_fail: FAIL
      imp_rand_ratio_at_s020: 84.2
      comparison_importance_s020_median_diff: 3.20
      comparison_importance_s020_p: 1.8e-32
    result_rationale: |
      On MATH-500 at s020, random masking shows NS phase gradient (DS: median_diff=-0.016, p=0.28; 
      QW: median_diff=0.013, p=0.20). This is the critical sparsity level below the onset threshold 
      (~s020-s025) where random does NOT produce compound phase interaction. On GPQA, despite the 
      longer reasoning chains providing more statistical power (n=198 vs n=500 on MATH-500), random 
      at s020 should remain NS because the mechanism is fundamentally different: random masking does 
      not trigger discrimination collapse (Gini/CV unchanged under random vs importance pruning at 
      low sparsity). The small positive median_diff=0.038 reflects minor stochastic variation, not 
      systematic phase dependence. The CI crossing zero confirms NS.
      
      In best tier, this is crucial: random NS at s020 on GPQA strengthens the onset-threshold finding 
      (random onset ~s020-s025) on a third benchmark, and the imp/rand ratio at s020 (3.20/0.038 ≈ 84×) 
      dramatically demonstrates strategy specificity. Reviewers see this as clean evidence that the 
      phase gradient is specific to importance-based scoring, not a trivial artifact of token removal.
      
      GPQA's higher statistical power (n=198) makes the NS finding MORE convincing than MATH-500's 
      (where n=50 left some ambiguity about underpowering). Here, minimum detectable d at n=198 is 
      ~0.20, and the observed d_z=0.08 is well below this — genuine absence, not lack of power.
    tables:
      - name: "Table S-GPQA-4: Strategy Comparison at s020 (GPQA)"
        columns: [strategy, II_low_median, II_high_median, median_diff, p_value, "d_z"]
        rows:
          - [importance, 3.24, 0.038, 3.20, "1.8e-32", 0.89]
          - [random, 0.11, 0.072, 0.038, 0.18, 0.08]
          - ["imp/rand ratio", "-", "-", "84×", "-", "11.1×"]
    figures_description:
      - "Figure 3(d): Strategy specificity panel showing importance (steep line) vs random (flat line) on GPQA at s020"
      - "Contributes to Table 2 cross-benchmark strategy specificity: GPQA s020 imp/rand ratio = 84× (vs MATH-500 15-38×, GSM8K 2.3-3.8×)"
    analysis: |
      The NS result for random at s020 on GPQA is one of the most valuable findings for the paper's 
      narrative. It demonstrates that even with massive statistical power (n=198, detectable d≥0.20), 
      random masking does NOT produce phase-dependent compound interaction below the onset threshold.
      Combined with the recency control (C11: triple NS across s015/s025/s030), this creates a 
      four-way dissociation: importance shows gradient, random NS below threshold, random weak above 
      threshold, recency always NS. The imp/rand ratio of 84× on GPQA is even larger than MATH-500's 
      15-38× range, suggesting that harder reasoning tasks amplify strategy specificity.
      
      This addresses RC2 (circularity concern) from a different angle: if phase segmentation were 
      creating an artifact, random masking would show it too at high statistical power. It doesn't.

  - name: "C9 Related Work Differentiation"
    plan_id: "c9_differentiation"
    description: "50-citation Related Work §2 with explicit gap analysis differentiating from ThinKV/SparK/Lethe/HIES/R-KV/Physics-of-KV"
    expected_results:
      total_citations: 52
      direct_competitor_citations: 8
      gap_analysis_paragraphs: 3
      taxonomy_categories: ["single-axis KV compression (ThinKV, R-KV, StreamingLLM)", "compound compression methods (SparK, SLiM)", "phase-transition analysis (Physics of KV Cache)", "importance score analysis (HIES, H2O)", "adaptive eviction methods (Lethe, Ada-KV)", "reasoning-aware compression (R-KV, DynamicKV)"]
      novelty_positioning: "compound × phase × strategy three-way interaction (no prior work analyzes all three dimensions simultaneously)"
      reviewer_novelty_concern_probability: 0.15
    result_rationale: |
      In best tier, the 50-citation related work with explicit gap analysis fully resolves reviewer 
      novelty concerns. The taxonomy clearly shows that prior work operates on subsets of our three 
      dimensions: ThinKV/R-KV do phase-aware single-axis, SparK does compound without phase, HIES 
      does score-collapse without compound interaction, Physics-of-KV does phase-transition on single axis.
      No work simultaneously analyzes compound × phase × strategy interaction.
      
      The key framing move is positioning our work as "empirical discovery" rather than "method improvement,"
      which sidesteps the "why not use ThinKV's phase-aware approach" question. We're not competing with 
      these methods — we're revealing a phenomenon they haven't characterized.
      
      With 52 citations (above the median for EMNLP empirical papers) and explicit gap analysis tables,
      at most 1 reviewer raises a novelty concern (best tier: reviewer_novelty_concern_count ∈ [0,1]),
      and it's easily addressed by pointing to the gap analysis table.
    tables:
      - name: "Table 1: Positioning vs Prior Work (in paper)"
        columns: [method, compound, phase_aware, strategy_comparison, "our contribution"]
        rows:
          - ["ThinKV (2025)", "✗", "✓ (single-axis)", "✗", "We analyze compound interaction's phase dependence"]
          - ["SparK (2024)", "✓", "✗", "✗", "We reveal phase modulation of their compound effect"]
          - ["HIES (2025)", "✗", "✗", "✗ (single-axis collapse)", "We show collapse amplified in compound setting"]
          - ["Physics of KV (2026)", "✗", "✓ (rate threshold)", "✗", "Our 'phase' = reasoning phase, not compression rate"]
          - ["Lethe (AAAI 2026)", "✗", "✓ (adaptive)", "✗", "Method paper; we provide mechanistic understanding"]
          - ["Ours", "✓", "✓ (reasoning phase)", "✓ (imp/rand/recency)", "Three-way interaction + mechanism"]
    figures_description:
      - "No figure needed for C9 — positioning conveyed through Table 1 and inline gap analysis"
    analysis: |
      C9 is a writing/framing task, not a computational experiment. In best tier, the comprehensive 
      related work resolves RC5 and RC6 definitively. The key innovation is framing recency eviction 
      as "experimental design contribution" (novel methodological control) alongside the empirical findings.
      This gives the paper TWO novelty angles: (1) empirical discovery of three-way interaction, 
      (2) methodological contribution of scoring-independent control design.
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5327844-ff6a-40ab-9d6a-f1476f25b60a",
  "isSidechain": false,
  "requestId": "req_011Cb7Gz8K8dLQKKLofZ22PH",
  "type": "assistant",
  "uuid": "95c0f13e-a1c9-4cb8-8775-31d4eb972eec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "801dd6fc-5861-4c46-a727-64581ec2a334",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FYmL9wPirBunqDBKuSz6iF",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10669,
      "cache_read_input_tokens": 74830,
      "output_tokens": 8311,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10669,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8311,
          "cache_read_input_tokens": 74830,
          "cache_creation_input_tokens": 10669,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10669
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

_source line 25_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Reviewers fully accept empirical-finding framing; recency control + triple dissociation seen as clean novel contribution; cross-architecture variation trea…",
  "leafUuid": "95c0f13e-a1c9-4cb8-8775-31d4eb972eec",
  "sessionId": "801dd6fc-5861-4c46-a727-64581ec2a334"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Phase-modulated compound sparsity with recency control confirmed",
  "sessionId": "801dd6fc-5861-4c46-a727-64581ec2a334"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Reviewers fully accept empirical-finding framing; recency control + triple dissociation seen as clean novel contribution; cross-architecture variation trea…",
  "leafUuid": "95c0f13e-a1c9-4cb8-8775-31d4eb972eec",
  "sessionId": "801dd6fc-5861-4c46-a727-64581ec2a334"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Phase-modulated compound sparsity with recency control confirmed",
  "sessionId": "801dd6fc-5861-4c46-a727-64581ec2a334"
}
```

---
