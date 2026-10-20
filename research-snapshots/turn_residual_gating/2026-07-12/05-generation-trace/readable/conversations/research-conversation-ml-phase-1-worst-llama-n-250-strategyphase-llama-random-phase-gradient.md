# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：LLaMA n=250 高功效确认 strategy×phase 交互在 Llama 架构上可忽略；random phase gradient 稳健。

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 40
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-3/a3d601b9-90d6-4700-8195-7ac8fe55805b.jsonl`
- **Structured JSON:** [`3933c3c9e1a80c42fdaf.json`](../../sessions/39/3933c3c9e1a80c42fdaf.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T15:20:28.068Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T15:20:28.068Z",
  "sessionId": "a3d601b9-90d6-4700-8195-7ac8fe55805b",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：LLaMA n=250 高功效确认 strategy×phase 交互在 Llama 架构上可忽略；random phase gradient 稳健。GPQA 不显著或方向不一致。'Strategy-gated' 叙事崩塌——phase modulation 普遍存在但非 strategy-specific。\n核心假设：['LLaMA imp_vs_rand d_z 在 n=250 仍 <0.25——高功效零结果确认交互是 Qwen2 特异', 'LLaMA random phase gradient d_z≥0.35 被确认——compound severity 的 phase modulation 与 eviction strategy 无关（在 Llama 上）', 'GPQA phase gradient NS 或方向不一致——跨 task 泛化失败', 'Strategy-specificity 限于 Qwen2ForCausalLM 架构，非普遍性质']\n关键指标范围：{'llama_n250_imp_vs_rand_dz_s030': [0.08, 0.25], 'llama_n250_imp_vs_rand_dz_s025': [0.05, 0.18], 'llama_n250_bonferroni_sig_count_out_of_4': [0, 1], 'llama_n250_random_phase_gradient_dz': [0.35, 0.55], 'llama_n250_importance_phase_gradient_dz': [0.95, 1.2], 'gpqa_ds_s015_median_diff': [-0.05, 0.1], 'gpqa_bonferroni_p': [0.05, 1.0], 'gpqa_imp_rand_ratio': [0.5, 2.0]}\n叙事方向：完全 reframe。Title 改为 \"Phase-Dependent Compound Sparsity Severity in Reasoning LLMs\"（去掉 strategy-gated）。Core finding 收窄：compound sparsity severity 是 phase-modulated 的涌现属性，importance phase gradient 跨三模型两架构 一致（d_z≈1.0-1.2），但 strategy×phase 交互仅 Qwen2 架构显著，Llama 上 random 也产生 comparable phase gradient（d_z 0.35-0.55）。 论文重组为三层递进：(1) Phase gradient universality（核心贡献，跨模型/架构稳健）， (2) Strategy modulation 的 architecture-dependence（secondary finding， Qwen2 confirmed / Llama NS → 开放问题）， (3) Discrimination collapse 机制（Gini/CV 跨模型一致，作为 phase gradient 的 解释而非 strategy-specificity 的解释）。Scope 限于 MATH-500 + GSM8K（GPQA 仅 放 appendix 或不纳入）。EMNLP main 仍可冲——pitch 改为 \"first systematic quantitative characterization of phase-dependent compound sparsity\"， 强调：(a) dose-response monotonicity（ρ=1.0, n=500 两模型）, (b) sparsity threshold discovery（~s020-s025）, (c) discrimination collapse 机制。 Novelty 论证需加强 methodology 贡献（per-problem paired II metric + phase segmentation framework）。需重写 §1-§3，将 strategy 从核心 claim 降级到 architecture-dependent 观察。Limitations 增加一段 strategy-specificity 的 scope boundary。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: phase-gated-compound-sparse\nvenue: EMNLP 2026\nfocus: 重点评估：(1) cross-architecture generalization 从 n=49 升级到 n=250 后是否足够支撑 claim，量级差 25× 如何在论文中定位；(2) GPQA cross-task 扩展对 scope 短板的修复力度；(3) 当前 framing 作为正会投稿的竞争力，novelty 是否站得住\n\n## paper_framing.md\n\n# Paper Framing — Phase-Gated Compound Sparsity\n\n> 最后更新: 2026-05-16 (数值对齐 n=500 registry: DS median_diff 0.39/1.21/3.99/8.48; QW 0.07/0.31/1.07/3.16; Cohen's d registry 0.61→1.13/0.37→1.44; C7+C10 status→confirmed; imp/rand 2.7-15×) | 维护者: Director\n\n## Core Insight\n\nCompound sparsity（attention head pruning + KV cache eviction）的 severity 不是固定常数——它是 eviction strategy 和 reasoning phase 交互的涌现属性。Importance-based eviction 的 compound interaction severity（paired median difference: median(II_low_i − II_high_i)）随 sparsity 单调递增（DeepSeek: 0.39→1.21→3.99→8.48; Qwen: 0.07→0.31→1.07→3.16），而 random masking 在 s015/s020 NS，在 s025 跨模型显著但效应量远小于 importance（DS: 0.257 vs 3.986; QW: 0.393 vs 1.074, 2.7-15×差异），存在 sparsity threshold ~s020-s025（D063; s030 待定）。Cohen's d（per-problem paired, B=10000）从 medium 到 large（DeepSeek: 0.61→1.13; Qwen: 0.37→1.44，registry cohens_d s015→s030）。LLaMA 跨架构验证（D060）qualitative direction consistent（within-importance d_z~1.0），但 strategy×phase 交互弱于 Qwen2 架构（imp_vs_rand d_z 0.19→0.34, 仅 s030 显著），且 random 在 LLaMA 上也显示显著 phase gradient（d_z 0.35→0.44），与 DeepSeek/Qwen random 低 sparsity NS 模式定性不同。GSM8K 跨 benchmark 验证（D075）：importance masking 的 phase gradient 在 GSM8K 上同样单调递增（QW: 0.039→0.158→1.100→2.092; DS: 0.241→0.740→1.992→4.682），但 strategy specificity（importance/random gradient ratio）从 MATH-500 的 15-36× 衰减至 GSM8K 的 2.3-3.8×。注意：\"反转\"仅在原始 II_low 值上（random > importance），phase gradient 层面 importance ≥ random。Strategy specificity 的 task-dependence 机制是开放问题（见 §6 Discussion）。这一发现挑战了 compound degradation 均匀分布的隐含假设。\n\n**数字基准**：所有数字基于 bf16 per-problem paired 统计量（B=10000 bootstrap）。median_diff 定义为 median(II_low_i − II_high_i)（逐 problem 配对差的中位数）。fp16 旧数据已弃用。\n\n## Narrative Arc\n\nCompound sparsity 是高效 LLM 推理的实用部署需求，但 prior work（SparK, Ada-KV, SLiM）将 compound interaction 视为均匀超可加。我们发现 severity 是 strategy × phase 交互的涌现属性：importance eviction 的 compound interaction 在 low-sparsity phase 远大于 high-sparsity phase（paired median difference 单调递增 0.39→8.48），而 random eviction 在低 sparsity (s015/s020) NS，在 s025+ 跨模型显著但效应量远小于 importance (2.7-15×)——存在 sparsity threshold (~s020-s025)，低于阈值 compound effect importance-specific，高于阈值两者均触发但 importance 主导。Cross-model replication 方向一致（Qwen magnitude ~1/4 of DeepSeek，onset threshold s≥0.20）。LLaMA 跨架构验证已完成（c3_llama, D060）：qualitative direction consistent（importance phase gradient d_z≈1.0），但 imp_vs_rand 交互弱（d_z 0.19→0.34, 仅 s030 显著），且 random 也显示非平凡 phase gradient（d_z 0.35→0.44），strategy-dependence 强度 architecture-dependent。我们通过 discrimination collapse 机制解释这一现象：head pruning → importance score 的判别力崩塌（Gini/CV 下降跨模型一致）→ importance eviction 退化为有偏伪随机。Attention entropy redistribution 作为 model-dependent secondary effect 在 DeepSeek 上观察到，但在 Qwen 上不稳健（D044）。\n\n**Framing 硬约束（D015）**：\n- MUST: \\\\\\\"emergent phase-strategy interaction\\\\\\\"\n- MUST NOT: \\\\\\\"importance metric limitation / importance is broken\\\\\\\"\n- MUST NOT: claim \\\\\\\"importance masking produces super-additive interaction\\\\\\\" without qualifier — random masking also produces positive II, and at s025+ random is statistically significant (D063). The distinguishing signal is **magnitude gradient** (importance 2.7-15× larger) and **onset threshold** (random NS below ~s020, importance significant from s015+), not the existence of super-additivity itself (D023)\n\n## Core Claims\n\n| ID | Claim | Status | Key Evidence |\n|----|-------|--------|-------------|\n| C1 | Compound sparsity severity is strategy- and task-modulated | confirmed | MATH-500: importance gradient 15-36× random; GSM8K: ratio 衰减至 2.3-3.8× (D075)。Phase gradient 层面 importance ≥ random 跨 benchmark 成立，但 magnitude ratio task-dependent。Threshold ~s020-s025 (D063) |\n| C2 | Severity is phase-modulated (amplified in low-sparsity phase) | confirmed | bf16 paired median difference 单调递增: 0.39→1.21→3.99→8.48; Bonferroni p<0.005 全 4 水平 (D032)。预注册：n=500 后若 QW s015 CI 仍跨零，叙事改为 'compound effect emerges above threshold sparsity (~s020)' |\n| C3 | Phase-strategy crossover exists | confirmed | s=0.25: importance high_phase=0.032 < random=0.818, importance low_phase=7.196 > random=1.363 (bf16) |\n| C4 | Discrimination collapse as primary mechanism; entropy redistribution model-dependent | partially_confirmed | D044: Gini/CV 下降跨模型一致; entropy collapse DeepSeek 一致但 Qwen s025 反转(+0.045) s030≈0。30/30 problems completed. |\n| C5 | Phase-modulated compound severity generalizes across models | confirmed | DeepSeek + Qwen cross-model replication: 方向一致, Cohen's d ρ=1.0, gradient permutation p=0.043. Qwen magnitude ~1/4 of DeepSeek, onset threshold s≥0.20 (S3→C). |\n| C5b | Phase-aware mitigation recovers compound degradation | future_work | D056: pilot 完成 gate_failed。Oracle recovery 18% < 30% gate (Wilcoxon p=0.002)，heuristic 32% 但 CI 跨零。方向正确但效应量不足，需更精细 phase boundary estimation → future work |\n| C6 | Severity gradient is sub-exponential | confirmed | Growth rate decreasing: Δ增长因子 3.8×→4.8×→2.0×（递减） |\n| C7 | Statistical power at n=500 confirms dose-response | confirmed | c2_n500_deepseek (success) + c2_qw_n500_r3 (success): 两模型 n=500 全 4 sparsity Bonferroni p<0.005, Spearman ρ=1.0 |\n| C8 | Cross-architecture validation (LLaMA) | partially_confirmed | D060: within-importance phase gradient 强(d_z~1.0) ✓，但 imp_vs_rand 交互弱(d_z 0.19→0.34, 仅 s030 Bonferroni p=0.029 显著)。**关键**：random 在 LLaMA 上也显示显著 phase gradient(d_z 0.35→0.44, CI 排除零)，与 DeepSeek/Qwen random 低 sparsity NS 模式定性不同。Qualitative direction consistent, quantitative strategy×phase interaction weaker + architecture-dependent。论文禁用 \"confirms\"，改用 \"suggests\"/\"provides partial support\"。 |\n| C9 | Differentiation from Lethe/SparK prior work | planned | Related Work §2 引用区分 + SparK gap analysis |\n| S3→C | Onset threshold is model-dependent (DeepSeek s≥0.15, Qwen s≥0.20) | confirmed | D037/D038: Qwen s015 d_z=0.37 CI含0, s020+ 显著 |\n| C10 | Phase gradient cross-benchmark robust; strategy specificity task-modulated | confirmed | GSM8K DS gradient 0.241→4.682 单调递增; QW gradient 0.039→2.092; imp/rand ratio 衰减至 2.3-3.8× (D075)。QW random s025+s030 均 success |\n| S7→C | Dose-response monotonicity (Spearman ρ=1.0) | confirmed | D047: 6-point dose-response, 单调递增 |\n\n## Anticipated Reviewer Concerns\n\n### RC1: Generalizability — 7B models only, benchmark scope\n- **预期质疑**: \\\"Results on two 7B models and MATH-500 only. How do we know this generalizes to larger models or other reasoning tasks?\\\"\n- **应对**: 四层泛化证据：(1) Cross-model: DeepSeek-R1-Distill-Qwen-7B + Qwen2.5-7B-Instruct（同架构不同训练，ρ=1.0）(2) Cross-architecture: c3_llama (DeepSeek-R1-Distill-Llama-8B, LlamaForCausalLM)，qualitative direction consistent，但需加限定——LLaMA 上 random 也显示 phase gradient，strategy × phase 交互弱于 Qwen2 架构（D060）(3) **Cross-benchmark (D075)**: GSM8K（两模型）phase gradient 单调递增复现（DS: 0.241→4.682; QW: 0.039→2.092），但 strategy specificity ratio 从 MATH-500 15-36× 衰减至 2.3-3.8×，表明 phase modulation 跨 benchmark 稳健而 magnitude modulation task-dependent。Limitations 诚实声明：(a) 7B scale only；(b) strategy specificity 强度 task-dependent（GSM8K 衰减，可能因推理链更短）；(c) LLaMA 跨架构验证 n=50 限制功效；(d) random phase gradient 行为 architecture-dependent。\n- **实验支撑**: C5 (cross-model) + C8 (c3_llama cross-architecture) + C10 (cross-benchmark GSM8K, D075)\n\n### RC2: Mechanism — entropy-discrimination collapse 缺乏直接测量\n- **预期质疑**: \\\"The mechanism is conceptual. Where is the empirical evidence for entropy increase and discrimination collapse?\\\"\n- **应对**: c4_entropy 实验已完成（DeepSeek 30/30 + Qwen 30/30）。D044 结论：Gini/CV 下降跨模型一致（discrimination collapse confirmed）；entropy redistribution 在 DeepSeek 上一致但在 Qwen 上 s025 方向反转、s030 近零（model-dependent）。论文以 discrimination collapse 为主线，entropy 作 DeepSeek 特有的强化因素。\n- **实验支撑**: c4_entropy (DeepSeek DONE) + qwen_c4_entropy (DONE, negative for entropy universality)\n\n### RC3: Practical impact — 没有 throughput 数据\n- **预期质疑**: \\\"No wall-clock or throughput measurements. Is the severity amplification reflected in actual inference speed?\\\"\n- **应对**: 本文定位是 empirical finding paper（发现 + 机制解释），不是 method paper。Throughput 不是 claim 的一部分。Discussion 中明确 phase-gated controller 作为 future direction。\n  - C5b pilot 已完成（D056）：oracle recovery 18%（Wilcoxon p=0.002），heuristic recovery 32%（p=0.024），但两者 95% CI 均跨零。方向正确（Wilcoxon 显著）但效应量不足（未达 30% gate），需更精细的 phase boundary estimation。论文 §6 Discussion 诚实报告 pilot 结果 + future work。\n  - Heuristic > oracle 悖论值得提及：token position ratio 粗粒度划分可能恰好更适合 mitigation 场景，暗示 phase boundary 的最优粒度是开放问题。\n- **实验支撑**: c5b_pilot (gate_failed, D056)\n\n### RC4: Statistical rigor — bootstrap 是否足够\n- **预期质疑**: \\\"Per-problem bootstrap with 50 problems — sufficient sample size?\\\"\n- **应对**: bf16 使用 B=10000 per-problem paired bootstrap，有效配对数 n=49 (DeepSeek) / n=46 (Qwen)；n=500 实验进一步验证 (C7 running)。Permutation test 使用 paired median difference 作为 robust statistic（D032），Bonferroni 校正后全 4 水平 p<0.005。Dose-response 主用 Wilcoxon signed-rank p + median_diff（robust to outliers），Cohen's d 作为辅助效应量（DeepSeek 0.61→1.13, Qwen 0.37→1.44, registry cohens_d s015→s030），注释高 sparsity 下 d 受 outlier-driven variance 影响（DS s020→s025: median 3.3× jump 但 d 非单调，因极端 II 值影响分母，D064）。可在 appendix 补充 per-problem 分布图（已生成 fig4_per_problem_dist.pdf）。\n- **实验支撑**: bf16 permutation test (D032) + Cohen's d per-problem paired (rebootstrap B=10000) + n=500 Wilcoxon (C7 running)\n\n### RC5: Novelty — prior work 是否已覆盖 phase-dependent sparsity\n- **预期质疑**: \"ThinKV and phase-aware methods already consider phase. What's new?\"\n- **应对**: Prior work 在单轴上分析 phase（ThinKV: phase-aware eviction）或 compound（SparK: joint compression）。没有工作同时分析 compound × phase × strategy 的三维交互。Crossover 现象（同一 strategy 在不同 phase 方向反转）是全新发现。Related Work 加 Lethe 引用区分 + SparK 对比。具体区分：\n  - **ThinKV** (arxiv 2510.01290, Oct 2025): 在 KV cache 单轴上做 phase-aware 压缩（按 CoT 阶段差异化 eviction），但不涉及 pruning × eviction 的 compound interaction。我们研究的是双轴（head pruning × KV eviction）compound interaction 如何随 phase 变化，ThinKV 的单轴 phase-aware 策略是我们分析维度的子集。\n  - **Physics of KV Cache Compression** (arxiv 2603.01426, Mar 2026): 揭示了单轴 KV 压缩的 phase transition 和 representational rigidity，是机制层面最接近的工作。关键区分：他们刻画的是单一压缩轴上压缩率的 critical threshold（phase transition），我们刻画的是两种压缩方法的 compound interaction severity 如何被 reasoning phase 调制（phase-dependent gradient）——维度正交。\n  - **HIES** (arxiv 2510.13832, Oct 2025): 发现 importance score collapse 并提出 entropy 补偿，为我们的 discrimination collapse 机制提供独立 supporting evidence——他们在单轴上观察到的 score collapse 正是我们在 compound setting 中发现的 Gini/CV 下降的单轴对应。\n  - **R-KV** (arxiv 2505.24133, May 2025): 针对 reasoning task 做 KV compression 优化，属于 task-specific method。我们不是提出新方法，而是 mechanistic 分析 compound interaction 的 phase-dependent 行为，二者目标不同（optimization vs understanding）。\n- **实验支撑**: C3 (crossover), Related Work §2 的 gap 分析\n\n### RC6: Novelty vs Lethe/SparK\n- **预期质疑**: \"How does this differ from Lethe (AAAI 2026) which also does layer-time-adaptive KV pruning, or SparK which studies compound compression?\"\n- **应对**: Lethe 和 SparK 都没有分析 phase × strategy 的交互效应。Lethe 是 method paper（提出 adaptive eviction 方法），我们是 empirical finding paper（发现 phase-dependent severity gradient）。SparK 研究 compound compression 但将 interaction 视为均匀超可加，我们发现 interaction severity 随 phase 和 strategy 变化。新近工作进一步确认我们的独特定位：\n  - **Physics of KV Cache Compression** (arxiv 2603.01426, Mar 2026) 是最近的相关工作，研究单轴压缩的 phase transition 阈值行为。与我们的核心区别：他们的 phase transition 是压缩率维度上的 critical point，我们的 phase-dependent gradient 是 reasoning phase 维度上 compound interaction 的连续调制——两者刻画的 \"phase\" 语义不同（compression-rate phase vs reasoning phase）。\n  - **ThinKV** (arxiv 2510.01290, Oct 2025) 和 **R-KV** (arxiv 2505.24133, May 2025) 都在 KV compression 单轴上引入 phase/reasoning awareness，但均未涉及 compound interaction。我们的贡献在于揭示 pruning × eviction 双轴交互如何被 reasoning phase 调制，这是单轴方法无法观察到的涌现现象。\n  - **HIES** (arxiv 2510.13832, Oct 2025) 的 importance score collapse 发现为我们的 discrimination collapse 机制提供了独立佐证，但 HIES 聚焦于单轴补偿方法，未研究 collapse 在 compound setting 中的放大效应。\n  - Related Work §2 明确区分三者定位：Lethe/SparK = method/compound method, ThinKV/R-KV = single-axis phase-aware, Physics of KV = single-axis phase transition, HIES = single-axis collapse。我们 = compound × phase × strategy 三维交互分析。\n- **实验支撑**: 不需要额外实验，仅需 §2 引用区分\n\n## Paper Positioning\n\n**类型**: Empirical finding paper（非 method paper）\n**核心贡献**:\n1. 发现 compound sparsity severity 的 strategy × phase 交互\n2. 量化 severity gradient（bf16 paired median difference 0.39→8.48, Cohen's d 0.61→1.13）和 crossover 现象\n3. 提出 discrimination collapse 机制解释（Gini/CV 跨模型一致；entropy redistribution model-dependent）\n4. Cross-model + cross-architecture (LLaMA) replication 验证泛化性（三模型两架构；LLaMA partially_confirmed，strategy×phase 交互强度 architecture-dependent, D060）\n\n**投稿目标**: EMNLP 2026 ARR, deadline 2026-05-25\n**Rebuttal 准备**: Day 9 (2026-05-23) 预留 rebuttal letter 写作时间\n**关键时间线**：\n- Day 9 (2026-05-23): 预留写 rebuttal letter\n- Day 11 (2026-05-25): EMNLP 2026 ARR 截稿\n\n\n## experiment_plan (with registry status)\n\n- id: c1_bf16_importance_s025\n  claim: C1\n  description: 'II median: high=0.032, mid=1.118, low=7.196; importance masking shows\n    strong phase gradient'\n  registry_id: bf16_importance_s025\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics: &id003\n    interaction_index:\n      high:\n        mean: 0.302756\n        median: 0.032363\n        ci:\n        - 0.083714\n        - 0.543977\n        winsorized_mean: 0.200962\n        skewness: 4.8826\n      mid:\n        mean: 5.729665\n        median: 1.118069\n        ci:\n        - 3.455574\n        - 8.471799\n        winsorized_mean: 4.189902\n        skewness: 8.2799\n      low:\n        mean: 25.852951\n        median: 7.195958\n        ci:\n        - 19.077082\n        - 33.497293\n        winsorized_mean: 19.319103\n        skewness: 7.3986\n    per_problem_ii_stats:\n      high:\n        n: 49\n        min: -0.316321\n        max: 4.003714\n        mean: 0.133714\n        median: 0.009873\n        std: 0.595358\n      mid:\n        n: 40\n        min: -0.024794\n        max: 18.720486\n        mean: 2.537744\n        median: 1.05707\n        std: 3.962575\n      low:\n        n: 50\n        min: -1.854733\n        max: 75.467653\n        mean: 11.28281\n        median: 3.954593\n        std: 16.620011\n    gradient_paired_aggregate_legacy: 222.35\n    median_difference: 7.1636\n    n_problems: 50\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: false\n      overall: PASS\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    perplexity:\n      high:\n        dense: 1.1689\n        attn: 1.6511\n        kv: 1.8628\n        both: 2.7026\n      mid:\n        dense: 1.2269\n        attn: 1.7039\n        kv: 5.6205\n        both: 13.3436\n      low:\n        dense: 1.2286\n        attn: 1.8366\n        kv: 31.756\n        both: 63.668\n- id: c1_bf16_ds_rand_s025\n  claim: C1\n  description: 'Random II median: high=0.818, mid=0.932, low=1.363; flat gradient\n    vs importance'\n  registry_id: bf16_ds_rand_s025\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 3.59\n        median: 0.8182\n        ci:\n        - 1.4021\n        - 6.2327\n        median_ci:\n        - 0.5075\n        - 1.7217\n        winsorized_mean: 6.3965\n        skewness: -7.57\n      mid:\n        mean: -1.8455\n        median: 0.9324\n        ci:\n        - -10.3663\n        - 4.9342\n        median_ci:\n        - 0.7331\n        - 1.7003\n        winsorized_mean: 3.1014\n        skewness: -12.76\n      low:\n        mean: 0.7212\n        median: 1.3627\n        ci:\n        - -4.2068\n        - 4.5006\n        median_ci:\n        - 1.0869\n        - 2.6866\n        winsorized_mean: 4.1866\n        skewness: -15.85\n    perplexity:\n      high:\n        dense: 1.1687\n        attn: 7.237\n        kv: 4.9751\n        both: 17.7423\n      mid:\n        dense: 1.2269\n        attn: 868.3199\n        kv: 5.1165\n        both: 29.4661\n      low:\n        dense: 1.2284\n        attn: 24.3571\n        kv: 6.7993\n        both: 17.9694\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    n_problems: 50\n    pass_fail:\n      ci_overlap: false\n      sign_reversal: false\n      overall: FAIL\n    median_difference: 0.5445\n- id: c1_bf16_qw_imp_s025\n  claim: C1\n  description: 'Qwen cross-model: median_diff=1.109, Cohen''s d=1.233, p<1e-5'\n  registry_id: bf16_qw_imp_s025\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics:\n    median_difference: 1.108706\n    permutation_p: 0\n    cohens_d: 1.2329\n    bootstrap_ci_95:\n    - 0.609247\n    - 1.469002\n    wilcoxon_p: 0\n    n_bootstrap: 10000\n    n_paired: 46\n- id: c1_sf5_asymmetric_spot\n  claim: C1\n  description: 'Asymmetric configs: h02_kv03 D=19.13, h03_kv02 D=18.25; gradient consistent'\n  registry_id: sf5_asymmetric_spot\n  role: ablation\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics:\n    config_a_h02_kv03:\n      II_low: 19.51\n      II_mid: 6.05\n      II_high: 0.38\n      D: 19.13\n    config_b_h03_kv02:\n      II_low: 18.77\n      II_mid: 3.97\n      II_high: 0.52\n      D: 18.25\n    pre_registered_criterion_passed: true\n    gradient_direction: II_low >> II_mid >> II_high (consistent with symmetric baseline)\n- id: c1_c2_accuracy_eval\n  claim: C1\n  description: 'DS dense->s030 acc: 0.52->0.10 (-0.42); QW dense->s030: 0.32->0.14\n    (-0.18)'\n  registry_id: c2_accuracy_eval\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics:\n    n_problems: 50\n    ds_dense_acc: 0.52\n    ds_s015_acc: 0.36\n    ds_s015_delta: -0.16\n    ds_s030_acc: 0.1\n    ds_s030_delta: -0.42\n    qw_dense_acc: 0.32\n    qw_s015_acc: 0.34\n    qw_s015_delta: 0.02\n    qw_s030_acc: 0.14\n    qw_s030_delta: -0.18\n    ds_s030_chinese_reasoning_rate: 0.4\n    ds_dense_truncation_rate: 0.56\n    note: v2 rescored with fixed radical+degree matcher. DS s015 34→36, QW s015 32→34\n- id: c2_bf16_importance_s030\n  claim: C2\n  description: 'Phase gradient: II low=14.64 >> mid=2.28 >> high=0.053 (median); low/high\n    ratio ~276x'\n  registry_id: bf16_importance_s030\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics: &id001\n    interaction_index:\n      high:\n        mean: 0.5547\n        median: 0.0534\n        ci:\n        - 0.2773\n        - 0.9198\n        winsorized_mean: 0.3367\n        skewness: 10.62\n      mid:\n        mean: 11.3\n        median: 2.2833\n        ci:\n        - 6.865\n        - 17.2633\n        winsorized_mean: 8.1752\n        skewness: 9.19\n      low:\n        mean: 57.7946\n        median: 14.6395\n        ci:\n        - 41.4416\n        - 77.0467\n        winsorized_mean: 39.3143\n        skewness: 8.31\n    per_problem_ii_stats:\n      high:\n        n: 49\n        min: -0.5095\n        max: 4.4457\n        mean: 0.1976\n        median: 0.0343\n        std: 0.6793\n      mid:\n        n: 40\n        min: -0.1989\n        max: 34.0258\n        mean: 5.2585\n        median: 1.5173\n        std: 7.9382\n      low:\n        n: 50\n        min: -7.3027\n        max: 126.7985\n        mean: 22.6601\n        median: 9.9731\n        std: 28.4096\n    gradient_paired_aggregate_legacy: 57.24\n    median_difference: 14.5861\n    n_problems: 50\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: false\n      overall: PASS\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    perplexity:\n      high:\n        dense: 1.1689\n        attn: 1.7123\n        kv: 2.0544\n        both: 3.2372\n      mid:\n        dense: 1.2269\n        attn: 1.7894\n        kv: 9.4821\n        both: 24.2847\n      low:\n        dense: 1.2286\n        attn: 1.9347\n        kv: 51.6485\n        both: 122.61\n- id: c2_v6_importance_s030\n  claim: C2\n  description: II low_median=34.69, mid_median=7.27, high_median=0.88; bootstrap_gradient=41.92,\n    CI=[19.14,299.76]\n  registry_id: v6_importance_s030\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 0.8833\n    ii_mid_median: 7.2706\n    ii_low_median: 34.6937\n    ii_high_mean: 1.5151\n    ii_mid_mean: 78.8215\n    ii_low_mean: 1163.9677\n    per_problem_ii_count: 50\n    n_high: 40\n    n_mid: 22\n    n_low: 20\n    problems: 50\n    bootstrap_gradient_paired: 41.92\n    bootstrap_ci_paired:\n    - 19.14\n    - 299.76\n    bootstrap_gradient_unpaired: 39.28\n    bootstrap_ci_unpaired:\n    - 21.87\n    - 129.59\n    bootstrap_p: 0\n- id: c2_think_phase_validation\n  claim: C2\n  description: Phase segmentation kappa=0.887; thinking=57.8% low-sparsity, answer=62.7%\n    high-sparsity\n  registry_id: think_phase_validation\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics:\n    effective_n: 48\n    skipped_problems: 2\n    median_kappa: 0.887\n    thinking_in_low_sparsity_phase: 0.578\n    answer_in_high_sparsity_phase: 0.627\n    note: Phase segmentation based on dense model — 4 sparsity conditions share identical\n      phase boundaries, effective sample n=48 not n=192\n- id: c2_acc_qw_s030_n100\n  claim: C2\n  description: QW importance s030 accuracy=0.19 (n=100); dose-response monotonic decline\n    from dense=0.40\n  registry_id: acc_qw_s030_n100\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics:\n    batch1_correct: 7\n    batch1_total: 50\n    batch1_acc: 0.14\n    batch1_source: acc_qw_s030_b1_8k (v2, 8k tokens)\n    batch2_correct: 12\n    batch2_total: 50\n    batch2_acc: 0.24\n    combined_correct: 19\n    combined_total: 100\n    combined_acc: 0.19\n- id: c2_acc_ds_s015_8k_v2\n  claim: C2\n  description: DS s015 accuracy=0.48 vs dense=0.74; early onset of compound degradation\n  registry_id: acc_ds_s015_8k_v2\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.48\n    correct: 24\n    total: 50\n    truncation_rate: 0.32\n    truncated_count: 16\n    non_truncated_accuracy: 0.706\n    non_truncated_correct: 24\n    non_truncated_total: 34\n    wall_time_s: 3967\n    max_new_tokens: 8192\n- id: c3_v6_importance_s025\n  claim: C3\n  description: 'Importance: II low_median=24.16 >> high_median=0.66; strong phase\n    gradient (36x ratio)'\n  registry_id: v6_importance_s025\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 0.6641\n    ii_mid_median: 5.3067\n    ii_low_median: 24.1619\n    ii_high_mean: 0.8842\n    ii_mid_mean: 10.057\n    ii_low_mean: 71.8854\n    per_problem_ii_count: 50\n    n_high: 42\n    n_mid: 23\n    n_low: 21\n    problems: 50\n    bootstrap_gradient_paired: 35.72\n    bootstrap_ci_paired:\n    - 9.52\n    - 101.54\n    bootstrap_gradient_unpaired: 36.38\n    bootstrap_ci_unpaired:\n    - 13.19\n    - 97.61\n    bootstrap_p: 0\n- id: c3_v6_random_s025\n  claim: C3\n  description: 'Random: II low_median=2.91 ~ high_median=3.00; flat phase gradient\n    (bootstrap_p=0.559)'\n  registry_id: v6_random_s025\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 3.0024\n    ii_mid_median: 2.9846\n    ii_low_median: 2.9146\n    ii_high_mean: 3.9052\n    ii_mid_mean: 7.9491\n    ii_low_mean: 3.9114\n    per_problem_ii_count: 50\n    n_high: 36\n    n_mid: 25\n    n_low: 24\n    bootstrap_gradient_paired: -0.1199\n    bootstrap_ci_paired:\n    - -1.517\n    - 1.2461\n    bootstrap_p: 0.559\n    bootstrap_gradient_unpaired: -0.8616\n    bootstrap_ci_unpaired:\n    - -3.3911\n    - 1.5169\n    per_problem_ii_stats:\n      high:\n        min: -6.1388\n        max: 25.2471\n        mean: 4.4098\n        median: 3.0421\n        std: 6.0734\n      mid:\n        min: 0.158\n        max: 108.7242\n        mean: 7.5626\n        median: 2.1407\n        std: 20.926\n      low:\n        min: -0.1953\n        max: 12.8555\n        mean: 3.5806\n        median: 2.7289\n        std: 3.4915\n    verdict: FAIL\n- id: c3_bf16_importance_s020\n  claim: C3\n  description: 'Importance: II low=1.50, mid=0.20, high=0.015 (median); clear phase\n    separation'\n  registry_id: bf16_importance_s020\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics: &id002\n    interaction_index:\n      high:\n        mean: 0.1289\n        median: 0.0145\n        ci:\n        - -0.1975\n        - 0.6647\n        winsorized_mean: -0.0297\n        skewness: 16.67\n      mid:\n        mean: 1.2604\n        median: 0.2027\n        ci:\n        - 0.7466\n        - 1.8962\n        winsorized_mean: 0.766\n        skewness: 7.05\n      low:\n        mean: 6.0288\n        median: 1.4963\n        ci:\n        - 4.4671\n        - 7.9237\n        winsorized_mean: 4.3426\n        skewness: 6.01\n    per_problem_ii_stats:\n      high:\n        n: 49\n        min: -0.1884\n        max: 0.4196\n        mean: 0.0025\n        median: 0.0036\n        std: 0.0966\n      mid:\n        n: 40\n        min: -0.0519\n        max: 8.6969\n        mean: 0.6795\n        median: 0.1977\n        std: 1.4998\n      low:\n        n: 50\n        min: -1.6151\n        max: 22.6875\n        mean: 2.2301\n        median: 1.128\n        std: 4.3758\n    gradient_paired_aggregate_legacy: 5.9\n    median_difference: 1.4818\n    n_problems: 50\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: false\n      overall: PASS\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    perplexity:\n      high:\n        dense: 1.1689\n        attn: 1.5233\n        kv: 1.6191\n        both: 2.1047\n      mid:\n        dense: 1.2269\n        attn: 1.5375\n        kv: 3.5164\n        both: 5.4246\n      low:\n        dense: 1.2286\n        attn: 1.6486\n        kv: 15.7987\n        both: 23.74\n- id: c3_bf16_ds_rand_s020\n  claim: C3\n  description: 'Random: II high=0.292, mid=0.350, low=0.276 (median); no phase separation'\n  registry_id: bf16_ds_rand_s020\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 1.1216\n        median: 0.2918\n        ci:\n        - 0.0796\n        - 2.5834\n        median_ci:\n        - 0.1598\n        - 0.4581\n        winsorized_mean: 1.7664\n        skewness: 9.59\n      mid:\n        mean: -1.5827\n        median: 0.3504\n        ci:\n        - -6.0963\n        - 1.5735\n        median_ci:\n        - 0.1993\n        - 0.5226\n        winsorized_mean: 0.5839\n        skewness: -12.31\n      low:\n        mean: -0.4116\n        median: 0.2763\n        ci:\n        - -2.6034\n        - 1.209\n        median_ci:\n        - 0.2194\n        - 0.5487\n        winsorized_mean: 0.9942\n        skewness: -10.07\n    perplexity:\n      high:\n        dense: 1.1687\n        attn: 3.1905\n        kv: 3.8002\n        both: 8.8129\n      mid:\n        dense: 1.2269\n        attn: 67.8504\n        kv: 3.788\n        both: 11.4974\n      low:\n        dense: 1.2284\n        attn: 8.592\n        kv: 5.0078\n        both: 9.2001\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    n_problems: 50\n    pass_fail:\n      ci_overlap: false\n      sign_reversal: false\n      overall: FAIL\n    median_difference: -0.0155\n- id: c4_c4_entropy\n  claim: C4\n  description: 'DS importance entropy_delta: -0.04 to -0.05 (collapse); random: +0.13\n    to +0.23 (redistribution). Gini_delta: -0.03 to -0.08'\n  registry_id: c4_entropy\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics:\n    importance_entropy_delta:\n      s015: -0.0402\n      s020: -0.0472\n      s025: -0.0446\n      s030: -0.0436\n    random_entropy_delta:\n      s015: 0.1283\n      s020: 0.136\n      s025: 0.2171\n      s030: 0.2327\n    importance_gini_delta:\n      s015: -0.0301\n      s020: -0.0404\n      s025: -0.0647\n      s030: -0.0806\n    random_gini_delta:\n      s015: -0.0309\n      s020: -0.0403\n      s025: -0.062\n      s030: -0.0732\n    importance_cv_delta:\n      s015: -0.564\n      s020: -0.774\n      s025: -1.287\n      s030: -1.665\n    random_cv_delta:\n      s015: -1.021\n      s020: -1.203\n      s025: -1.923\n      s030: -2.137\n    problems_completed: 30\n    runtime_minutes: 69.1\n- id: c4_qwen_c4_entropy\n  claim: C4\n  description: 'QW importance entropy_delta mixed: s015=-0.073, s025=+0.045; Gini\n    weaker (-0.01 to -0.02). Model-dependent pattern'\n  registry_id: qwen_c4_entropy\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: negative\n  metrics:\n    problems_completed: 30\n    qwen_importance_entropy_delta:\n      s015: -0.0733\n      s020: -0.0759\n      s025: 0.0451\n      s030: -0.0072\n    qwen_random_entropy_delta:\n      s015: 0.0838\n      s020: 0.0901\n      s025: 0.2168\n      s030: 0.1968\n    qwen_importance_gini_delta:\n      s015: -0.0103\n      s020: -0.0121\n      s025: -0.01\n      s030: -0.0202\n    qwen_random_gini_delta:\n      s015: -0.0186\n      s020: -0.0229\n      s025: -0.0337\n      s030: -0.0448\n    qwen_importance_cv_delta:\n      s015: -0.045\n      s020: -0.208\n      s025: -1.491\n      s030: -1.142\n    qwen_random_cv_delta:\n      s015: -0.778\n      s020: -0.889\n      s025: -1.5\n      s030: -1.677\n    cross_model_notes: random entropy increase consistent; importance entropy collapse\n      inconsistent at s025 (reversed to +0.045) and near-zero at s030; gini/cv directions\n      consistent but Qwen magnitudes smaller\n- id: c5_bf16_qw_imp_s030\n  claim: C5\n  description: 'Qwen: median_diff=2.619, Cohen''s d=1.439, p<1e-5; replicates DeepSeek\n    pattern'\n  registry_id: bf16_qw_imp_s030\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics:\n    median_difference: 2.619385\n    permutation_p: 0\n    cohens_d: 1.4394\n    bootstrap_ci_95:\n    - 1.722281\n    - 3.651063\n    wilcoxon_p: 0\n    n_bootstrap: 10000\n    n_paired: 46\n- id: c5_bf16_importance_s030\n  claim: C5\n  description: 'DeepSeek: II low_median=14.64, high_median=0.053; strong phase gradient'\n  registry_id: bf16_importance_s030\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics: *id001\n- id: c5_c2_n500_deepseek\n  claim: C5\n  description: 'DS n=500: imp_s030 median_II=8.48, CI=[7.46,9.56], p=1.3e-78; robust\n    at scale'\n  registry_id: c2_n500_deepseek\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics: &id004\n    n_problems: 500\n    effective_n: 496\n    mid_null_rate: 0.102\n    imp_s015_median_ii: 0.3907\n    imp_s015_ci:\n    - 0.3496\n    - 0.4431\n    imp_s015_wilcoxon_p: 1.27e-70\n    imp_s020_median_ii: 1.2149\n    imp_s020_ci:\n    - 1.1072\n    - 1.3365\n    imp_s020_wilcoxon_p: 3.98e-75\n    imp_s025_median_ii: 3.9857\n    imp_s025_ci:\n    - 3.5272\n    - 4.3588\n    imp_s025_wilcoxon_p: 1.99e-78\n    imp_s030_median_ii: 8.4813\n    imp_s030_ci:\n    - 7.7543\n    - 9.6919\n    imp_s030_wilcoxon_p: 1.09e-79\n    rand_s015_median_ii: 0.0139\n    rand_s015_wilcoxon_p: 0.863\n    rand_s020_median_ii: 0.0315\n    rand_s020_wilcoxon_p: 0.28\n    rand_s025_median_ii: 0.2574\n    rand_s025_bonf_p: 0.005839\n    rand_s025_fdr_p: 0.001914\n    rand_s030_median_ii: 0.5096\n    rand_s030_bonf_p: 0.005903\n    rand_s030_fdr_p: 0.001914\n    dz_s015_s020: -0.925\n    dz_s020_s025: -0.824\n    dz_s025_s030: -0.773\n    dz_s015_s030: -0.944\n    all_dz_reliable: true\n    dose_response_monotonic: true\n    dose_response_spearman_rho: 1\n    dose_response_perm_p: 0.0417\n    imp_rand_ratio_range: 15.5-38.6x\n    bonferroni_k: 4\n    bonferroni_note: Bonferroni k=4 family-wise (D066 revision)\n- id: c5_c2_qw_n500_r3\n  claim: C5\n  description: 'QW n=500: imp_s030 median_II=4.33, p<1e-40; cross-model replication\n    at high power'\n  registry_id: c2_qw_n500_r3\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics: &id005\n    n_problems: 500\n    effective_n: 475\n    filter: low+high valid only (mid-null allowed)\n    mid_null_rate: 0.452\n    imp_s015_median_ii: 0.0659\n    imp_s015_ci:\n    - 0.0492\n    - 0.0925\n    imp_s015_wilcoxon_p: 8.66e-15\n    imp_s015_bonf_p: 3.46e-14\n    imp_s020_median_ii: 0.3073\n    imp_s020_ci:\n    - 0.2612\n    - 0.3564\n    imp_s020_wilcoxon_p: 6.84e-42\n    imp_s020_bonf_p: 2.74e-41\n    imp_s025_median_ii: 1.0745\n    imp_s025_ci:\n    - 0.9766\n    - 1.1787\n    imp_s025_wilcoxon_p: 1.06e-68\n    imp_s025_bonf_p: 4.25e-68\n    imp_s030_median_ii: 3.155\n    imp_s030_ci:\n    - 2.7834\n    - 3.5582\n    imp_s030_wilcoxon_p: 9.21e-74\n    imp_s030_bonf_p: 3.69e-73\n    rand_s015_median_ii: -0.0111\n    rand_s015_wilcoxon_p: 0.172\n    rand_s015_bonf_p: 0.687\n    rand_s020_median_ii: 0.0153\n    rand_s020_wilcoxon_p: 0.2\n    rand_s020_bonf_p: 0.8\n    rand_s025_median_ii: 0.3931\n    rand_s025_wilcoxon_p: 1.59e-11\n    rand_s025_bonf_p: 6.37e-11\n    rand_s025_fdr_p: 2.63e-11\n    rand_s030_median_ii: 0.9127\n    rand_s030_wilcoxon_p: 2.92e-15\n    rand_s030_bonf_p: 1.17e-14\n    rand_s030_fdr_p: 5.61e-15\n    dz_s015_s020: -0.629\n    dz_s020_s025: -0.865\n    dz_s025_s030: -0.767\n    dz_s015_s030: -0.923\n    all_dz_reliable: true\n    dose_response_monotonic: true\n    dose_response_spearman_rho: 1\n    dose_response_perm_p: 0.0417\n    imp_rand_ratio_range: 2.7-20.1x\n    bonferroni_k: 4\n    bonferroni_note: Bonferroni k=4 family-wise (D066 revision)\n- id: c5b_c5b_pilot\n  claim: C5b\n  description: 'Oracle recovery=18% (gate: >30% FAIL); heuristic recovery=31.7% but\n    CI crosses zero. s030 incomplete'\n  registry_id: c5b_pilot\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: negative\n  metrics:\n    s025_uniform_median_ii: 1.0435\n    s025_oracle_median_ii: 0.856\n    s025_oracle_recovery_pct: 18\n    s025_oracle_recovery_ci:\n    - -39\n    - 45.8\n    s025_oracle_wilcoxon_p: 0.0021\n    s025_heuristic_median_ii: 0.7127\n    s025_heuristic_recovery_pct: 31.7\n    s025_heuristic_recovery_ci:\n    - -22.8\n    - 66\n    s025_heuristic_wilcoxon_p: 0.0236\n    gate_criterion: oracle_recovery > 30%\n    gate_result: FAIL\n    s030_status: not_completed\n    n_problems: 30\n- id: c6_bf16_importance_s015\n  claim: C6\n  description: II low_median=0.398 at s=0.15\n  registry_id: bf16_importance_s015\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: -0.150213\n        median: 0.005752\n        ci:\n        - -0.294614\n        - -0.055385\n        winsorized_mean: -0.062378\n        skewness: -14.9912\n      mid:\n        mean: 0.447301\n        median: 0.080738\n        ci:\n        - 0.267993\n        - 0.668749\n        winsorized_mean: 0.324751\n        skewness: 4.7221\n      low:\n        mean: 2.405837\n        median: 0.398291\n        ci:\n        - 1.478784\n        - 3.667675\n        winsorized_mean: 1.278857\n        skewness: 9.5402\n    per_problem_ii_stats:\n      high:\n        n: 49\n        min: -0.188061\n        max: 0.335853\n        mean: -0.013405\n        median: 0.00012\n        std: 0.078483\n      mid:\n        n: 40\n        min: -0.169092\n        max: 3.88198\n        mean: 0.308621\n        median: 0.107114\n        std: 0.690186\n      low:\n        n: 50\n        min: -0.872983\n        max: 9.10289\n        mean: 0.725504\n        median: 0.315517\n        std: 1.731056\n    gradient_paired_aggregate_legacy: 69.24\n    median_difference: 0.3925\n    n_problems: 50\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: true\n      overall: PASS\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    perplexity:\n      high:\n        dense: 1.1689\n        attn: 1.4861\n        kv: 1.4481\n        both: 1.5911\n      mid:\n        dense: 1.2269\n        attn: 1.5137\n        kv: 2.5971\n        both: 3.4541\n      low:\n        dense: 1.2286\n        attn: 1.6147\n        kv: 8.9201\n        both: 12.5084\n- id: c6_bf16_importance_s020\n  claim: C6\n  description: II low_median=1.496 at s=0.20\n  registry_id: bf16_importance_s020\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics: *id002\n- id: c6_bf16_importance_s025\n  claim: C6\n  description: II low_median=7.196 at s=0.25\n  registry_id: bf16_importance_s025\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics: *id003\n- id: c6_bf16_importance_s030\n  claim: C6\n  description: II low_median=14.64 at s=0.30; growth 0.40->1.50->7.20->14.64 is sub-exponential\n  registry_id: bf16_importance_s030\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics: *id001\n- id: c7_c2_n500_deepseek\n  claim: C7\n  description: 'DS n=500: all 4 sparsities significant (p<1e-70); CIs non-overlapping\n    across dose levels'\n  registry_id: c2_n500_deepseek\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics: *id004\n- id: c7_c2_qw_n500_r3\n  claim: C7\n  description: 'QW n=500: all 4 sparsities significant (p<1e-14 Bonferroni-corrected);\n    mid_null_rate=45.2%'\n  registry_id: c2_qw_n500_r3\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics: *id005\n- id: c8_c3_llama\n  claim: C8\n  description: LLaMA-8B (LlamaForCausalLM) replicates phase-modulated compound severity\n    from Qwen2ForCausalLM\n  registry_id: c3_llama\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics:\n    model: DeepSeek-R1-Distill-Llama-8B\n    n_problems: 50\n    n_valid: 49\n    n_skipped: 1\n    conditions_completed: 8/8\n    n_bootstrap: 10000\n    bonferroni_k: 4\n    imp_vs_rand_dz:\n      s015: 0.1923\n      s020: 0.255\n      s025: 0.2902\n      s030: 0.3352\n    imp_vs_rand_dz_ci:\n      s015:\n      - -0.0862\n      - 0.496\n      s020:\n      - -0.0248\n      - 0.5381\n      s025:\n      - 0.0081\n      - 0.6121\n      s030:\n      - 0.0606\n      - 0.6629\n    imp_vs_rand_dz_interpretation:\n      s015: negligible\n      s020: small\n      s025: small\n      s030: small\n    imp_vs_rand_dz_monotonic: true\n    phase_gradient_importance_dz:\n      s015: 1.0079\n      s020: 1.108\n      s025: 1.1227\n      s030: 1.0038\n    phase_gradient_importance_dz_ci:\n      s015:\n      - 0.593\n      - 1.7025\n      s020:\n      - 0.8144\n      - 1.5698\n      s025:\n      - 0.8735\n      - 1.5768\n      s030:\n      - 0.8099\n      - 1.3519\n    phase_gradient_importance_interpretation: all_large\n    phase_gradient_random_dz:\n      s015: 0.3497\n      s020: 0.373\n      s025: 0.4476\n      s030: 0.4385\n    phase_gradient_random_dz_ci:\n      s015:\n      - 0.0665\n      - 0.6916\n      s020:\n      - 0.0868\n      - 0.7335\n      s025:\n      - 0.1669\n      - 0.7698\n      s030:\n      - 0.1966\n      - 0.707\n    phase_gradient_random_interpretation: all_small\n    median_diff:\n      s015: 0.0203\n      s020: 0.0221\n      s025: 0.0947\n      s030: 0.3562\n    median_diff_ci:\n      s015:\n      - 0.0016\n      - 0.0435\n      s020:\n      - -0.0905\n      - 0.187\n      s025:\n      - -0.0037\n      - 0.3029\n      s030:\n      - -0.0691\n      - 0.5442\n    wilcoxon_p:\n      s015: 0.0549\n      s020: 0.0632\n      s025: 0.0209\n      s030: 0.0074\n    wilcoxon_p_bonferroni:\n      s015: 0.2195\n      s020: 0.2527\n      s025: 0.0834\n      s030: 0.0294\n    significant_bonferroni:\n      s015: false\n      s020: false\n      s025: false\n      s030: true\n    cross_arch_comparison:\n      deepseek_importance_dz:\n        s015: 0.4416\n        s020: 0.5195\n        s025: 0.6831\n        s030: 0.8031\n      llama_importance_dz:\n        s015: 1.0079\n        s020: 1.108\n        s025: 1.1227\n        s030: 1.0038\n      delta:\n        s015: 0.5663\n        s020: 0.5885\n        s025: 0.4396\n        s030: 0.2007\n      note: LLaMA shows uniformly large d_z (all >1.0) vs DeepSeek medium-to-large\n- id: c10_gsm8k_profiling_ds\n  claim: C10\n  description: 'DS GSM8K importance gradient: s015=0.241, s020=0.740, s025=1.992,\n    s030=4.636 (monotonic)'\n  registry_id: gsm8k_profiling_ds\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics:\n    version: v3_median\n    n_problems: 50\n    method: median + Wilcoxon + bootstrap_median(B=10000)\n    importance:\n      s015:\n        median_gradient: 0.241\n        ci_low: 0.077\n        ci_high: 0.478\n        wilcoxon_p: 0.0003\n      s020:\n        median_gradient: 0.74\n        ci_low: 0.314\n        ci_high: 1.119\n        wilcoxon_p: 0.0001\n      s025:\n        median_gradient: 1.992\n        ci_low: 0.933\n        ci_high: 2.82\n        wilcoxon_p: 0.0001\n      s030:\n        median_gradient: 4.682\n        ci_low: 2.121\n        ci_high: 10.557\n        wilcoxon_p: 0.0001\n    imp_rand_ratio:\n      s015: 2.3\n      s020: 2.5\n      s025: 3.8\n      s030: 2.8\n    dose_response_monotonic: true\n- id: c10_gsm8k_profiling_qw\n  claim: C10\n  description: 'QW GSM8K importance gradient: s015=0.039, s020=0.158, s025=1.100,\n    s030=2.092 (monotonic)'\n  registry_id: gsm8k_profiling_qw\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics:\n    version: v3_median\n    n_problems: 50\n    method: median + Wilcoxon + bootstrap_median(B=10000)\n    importance:\n      s015:\n        median_gradient: 0.039\n      s020:\n        median_gradient: 0.158\n      s025:\n        median_gradient: 1.1\n      s030:\n        median_gradient: 2.092\n    qw_rand_s030: INVALID\n- id: c10_gsm8k_qw_rand_s025_v2\n  claim: C10\n  description: 'QW random s025 GSM8K: II median_high=0.72, low=1.48; phase gradient\n    weaker than importance'\n  registry_id: gsm8k_qw_rand_s025_v2\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics:\n    verdict: PASS\n    n_problems: 50\n    n_bootstrap: 1000\n    seed: 42\n    high_sparsity:\n      n_segments: 216\n      n_tokens: 9326\n      ppl_dense: 1.0695\n      ppl_attn: 5.9362\n      ppl_kv: 3.4316\n      ppl_both: 15.7484\n      ii_mean: 6.5954\n      ii_ci:\n      - 1.1114\n      - 11.3791\n      ii_median: 0.7176\n      ii_median_ci:\n      - 0.5959\n      - 0.9347\n      winsorized_mean: 6.5046\n      skewness: -4.6807\n      outlier_count: 3\n    low_sparsity:\n      n_segments: 252\n      n_tokens: 29224\n      ppl_dense: 1.1972\n      ppl_attn: 11.5347\n      ppl_kv: 5.6038\n      ppl_both: 21.6874\n      ii_mean: 2.3883\n      ii_ci:\n      - -8.4602\n      - 11.029\n      ii_median: 1.4587\n      ii_median_ci:\n      - 1.1121\n      - 2.0451\n      winsorized_mean: 5.8911\n      skewness: -7.6074\n      outlier_count: 4\n    mid_sparsity:\n      n_segments: 51\n      n_tokens: 5954\n      ppl_dense: 1.2601\n      ppl_attn: 13.4132\n      ppl_kv: 6.4841\n      ppl_both: 20.8714\n      ii_mean: 4.5407\n      ii_ci:\n      - -4.8854\n      - 12.4605\n      ii_median: 1.1272\n      ii_median_ci:\n      - 0.637\n      - 3.3729\n      winsorized_mean: 6.3284\n      skewness: -3.4048\n      outlier_count: 1\n- id: c10_gsm8k_qw_rand_s030_v2\n  claim: C10\n  description: 'QW random s030 GSM8K: II median_high=2.31, low=5.87; compound effect\n    on GSM8K confirmed'\n  registry_id: gsm8k_qw_rand_s030_v2\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics:\n    verdict: PASS\n    n_problems: 50\n    n_bootstrap: 1000\n    seed: 42\n    high_sparsity:\n      n_segments: 216\n      n_tokens: 9326\n      null_ratio: 2/50\n      ppl_dense: 1.0695\n      ppl_attn: 6.5613\n      ppl_kv: 4.481\n      ppl_both: 23.7486\n      ii_mean: 11.83\n      ii_median: 2.31\n      ii_ci:\n      - 6.17\n      - 17.04\n      ii_median_ci:\n      - 1.64\n      - 2.81\n      winsorized_mean: 10.55\n      skewness: -2.29\n      outlier_count: 7\n    low_sparsity:\n      n_segments: 252\n      n_tokens: 29224\n      null_ratio: 5/50\n      ppl_dense: 1.1972\n      ppl_attn: 6.3283\n      ppl_kv: 8.5374\n      ppl_both: 56.2304\n      ii_mean: 31.26\n      ii_median: 5.2\n      ii_ci:\n      - 17.84\n      - 47.86\n      ii_median_ci:\n      - 3.95\n      - 7.24\n      winsorized_mean: 16.35\n      skewness: 7.57\n      outlier_count: 4\n    mid_sparsity:\n      n_segments: 51\n      n_tokens: 5954\n      null_ratio: 17/50\n      ppl_dense: 1.2601\n      ppl_attn: 18.6162\n      ppl_kv: 11.6625\n      ppl_both: 47.9019\n      ii_mean: 18.02\n      ii_median: 2.7\n      ii_ci:\n      - 0.09\n      - 36.69\n      ii_median_ci:\n      - 1.46\n      - 8.77\n      winsorized_mean: 18.22\n      skewness: 0.43\n      outlier_count: 2\n- id: s3_c_bf16_ds_imp_s010\n  claim: S3->C\n  description: 'DS s=0.10: II_high_median=0.003, verdict=FAIL; below onset threshold\n    for DeepSeek'\n  registry_id: bf16_ds_imp_s010\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: negative\n  metrics:\n    verdict: FAIL\n    problems: 50\n    II_high_sparsity_median: 0.0027\n    II_high_sparsity_mean: -0.1998\n    II_low_sparsity_median: 0.0151\n    II_low_sparsity_mean: -0.1066\n    II_mid_sparsity_median: 0.0061\n    II_mid_sparsity_mean: -0.0131\n    high_sparsity_tokens: 21086\n    low_sparsity_tokens: 27748\n    mid_sparsity_tokens: 13306\n- id: s3_c_bf16_qw_imp_s010\n  claim: S3->C\n  description: 'QW s=0.10: overall_verdict=PASS, CI_overlap_test=PASS; Qwen onset\n    earlier than DeepSeek'\n  registry_id: bf16_qw_imp_s010\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics:\n    n_problems: 50\n    overall_verdict: PASS\n    ci_overlap_test: PASS\n    sign_reversal_test: FAIL\n    high_sparsity_II_median: 0.0001\n    high_sparsity_II_median_CI:\n    - -0.0028\n    - 0.0005\n    high_sparsity_II_mean: -0.0887\n    high_sparsity_II_mean_CI:\n    - -0.1235\n    - -0.0591\n    low_sparsity_II_median: -0.0444\n    low_sparsity_II_median_CI:\n    - -0.0967\n    - -0.0152\n    low_sparsity_II_mean: -0.2431\n    low_sparsity_II_mean_CI:\n    - -0.3817\n    - -0.1202\n    mid_sparsity_II_median: -0.0359\n    mid_sparsity_II_median_CI:\n    - -0.0963\n    - -0.015\n    mid_sparsity_II_mean: -0.084\n    mid_sparsity_II_mean_CI:\n    - -0.1366\n    - -0.035\n    ppl_high_dense: 1.074\n    ppl_high_both: 1.228\n    ppl_low_dense: 1.152\n    ppl_low_both: 3.204\n    ppl_mid_dense: 1.133\n    ppl_mid_both: 1.741\n- id: s3_c_bf16_qw_imp_s015\n  claim: S3->C\n  description: 'QW s=0.15: median_diff=0.048, permutation_p=0.0001; confirmed above\n    threshold'\n  registry_id: bf16_qw_imp_s015\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics:\n    median_difference: 0.047619\n    permutation_p: 0.0001\n    cohens_d: 0.3705\n    bootstrap_ci_95:\n    - -0.005077\n    - 0.109517\n    wilcoxon_p: 0.02958\n    n_bootstrap: 10000\n    n_paired: 46\n- id: s7_c_c2_n500_deepseek\n  claim: S7->C\n  description: 'DS n=500 monotonic: imp median II 0.39->1.21->3.99->8.48 across s015-s030\n    (Spearman rho=1.0)'\n  registry_id: c2_n500_deepseek\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics: *id004\n- id: s7_c_c2_qw_n500_r3\n  claim: S7->C\n  description: 'QW n=500 monotonic: imp median II 0.066->0.307->1.075->4.33 across\n    s015-s030 (Spearman rho=1.0)'\n  registry_id: c2_qw_n500_r3\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics: *id005\n- id: s7_c_bf16_qw_imp_s035\n  claim: S7->C\n  description: 'QW s=0.35: low_II_median=8.24; extends dose-response beyond s030'\n  registry_id: bf16_qw_imp_s035\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics:\n    n_problems: 50\n    overall_verdict: PASS\n    ci_overlap_test: PASS\n    sign_reversal_test: FAIL\n    high_sparsity_II_median: 0.0232\n    high_sparsity_II_median_CI:\n    - 0.0154\n    - 0.0383\n    high_sparsity_II_mean: 0.1643\n    high_sparsity_II_mean_CI:\n    - 0.0844\n    - 0.2495\n    low_sparsity_II_median: 8.2358\n    low_sparsity_II_median_CI:\n    - 6.1564\n    - 10.9231\n    low_sparsity_II_mean: 18.9673\n    low_sparsity_II_mean_CI:\n    - 14.5015\n    - 23.9752\n    mid_sparsity_II_median: 0.9577\n    mid_sparsity_II_median_CI:\n    - 0.171\n    - 3.5575\n    mid_sparsity_II_mean: 8.0734\n    mid_sparsity_II_mean_CI:\n    - 2.0224\n    - 16.8946\n    ppl_high_dense: 1.0738\n    ppl_high_both: 2.3435\n    ppl_low_dense: 1.1518\n    ppl_low_both: 58.0358\n    ppl_mid_dense: 1.1327\n    ppl_mid_both: 20.9912\n    high_sparsity_tokens: 16289\n    low_sparsity_tokens: 32227\n    mid_sparsity_tokens: 4372\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_interaction_index_profiling\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_ii_profiling_v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    mvp_verdict: PASS_technical_but_negative_hypothesis\n    ci_nonoverlap: true\n    sign_reversal: false\n    ii_reasoning_0.3: 17.79\n    ii_reasoning_0.3_ci:\n    - 4.09\n    - 38.76\n    ii_transition_0.3: 3.06\n    ii_transition_0.3_ci:\n    - 0.01\n    - 5.6\n    ii_reasoning_0.5: 468.9\n    ii_transition_0.5: 850.07\n    ii_execution_0.3: Inf\n    phase_distribution:\n      execution: 1.2%_25seg\n      reasoning: 8.1%_96seg\n      transition: 90.7%_192seg\n    total_tokens: 86207\n    all_ii_superadditive: true\n    amplitude_ratio_reas_vs_trans_0.3: 5.81\n    gmm_best_k: 5\n    gmm_means:\n    - 0.438\n    - 0.597\n    - 0.719\n    - 0.816\n    - 0.892\n    gmm_weights:\n    - 0.062\n    - 0.14\n    - 0.208\n    - 0.282\n    - 0.309\n    sparsity_global:\n      mean: 0.7653\n      std: 0.1364\n      median: 0.8004\n    quantile_boundaries:\n    - 0.7337\n    - 0.8482\n- exp_id: mvp_ii_profiling_v3\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    mvp_verdict: FAIL\n    ci_nonoverlap: false\n    sign_reversal: false\n    phase_distribution_balanced: true\n    ii_high_0.1:\n      mean: 0.2317\n      ci:\n      - 0.1338\n      - 0.3418\n    ii_low_0.1:\n      mean: 0.1711\n      ci:\n      - 0.0782\n      - 0.2768\n    ii_mid_0.1:\n      mean: 0.1607\n      ci:\n      - 0.0886\n      - 0.2489\n    ii_high_0.2:\n      mean: 2.1574\n      ci:\n      - 1.0605\n      - 3.5491\n    ii_low_0.2:\n      mean: 1.1294\n      ci:\n      - 0.4368\n      - 1.9593\n    ii_mid_0.2:\n      mean: 0.3049\n      ci:\n      - -1.0635\n      - 1.3044\n    total_tokens: 86207\n    no_nan_inf: true\n    segments:\n      high: 511\n      low: 454\n      mid: 391\n- exp_id: mvp_ii_profiling_v4\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_ii_profiling_v4b\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_ii_profiling_v4c\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_ii_profiling_v4d\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_ii_profiling_v4-random\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_v4a_r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_v4b_r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_v4c_r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_v4_random_r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp_v4_legacy_s01\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    II_high_0.1:\n      mean: -0.1097\n      ci_low: -0.8066\n      ci_high: 0.41\n    II_mid_0.1:\n      mean: -15.966\n      ci_low: -47.991\n      ci_high: 1.288\n    II_low_0.1:\n      mean: 0\n      ci_low: 0\n      ci_high: 0\n    ppl_high_dense: 1.1462\n    ppl_high_both: 22.1302\n    ppl_mid_dense: 1.1226\n    ppl_mid_both: 47.5856\n    verdict: FAIL\n- exp_id: mvp_v4_legacy_s02\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_0.2:\n      mean: 21.2856\n      ci:\n      - 0.0292\n      - 63.163\n    ii_mid_0.2:\n      mean: 21.8743\n      ci:\n      - 4.9863\n      - 41.785\n    ii_low_0.2:\n      mean: 0\n      ci:\n      - 0\n      - 0\n    ppl_high:\n      dense: 1.15\n      attn: 1.32\n      kv: 104.42\n      both: 63.41\n    ppl_mid:\n      dense: 1.12\n      attn: 1.29\n      kv: 324.16\n      both: 170.47\n    ppl_low:\n      dense: 1.11\n      attn: 1.3\n      kv: 1.11\n      both: 1.3\n    problems_completed: 50\n    phase_tokens:\n      high: 25862\n      mid: 27996\n      low: 32349\n    mvp_verdict: PASS\n- exp_id: mvp_v4_legacy_s03\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_0.3:\n      mean: -224.5\n      ci_crosses_zero: true\n    verdict: FAIL_ci_crosses_zero\n- exp_id: mvp_v4_legacy_s025\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_v4_legacy_s035\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_v4_float32_s030\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_v5_fixed_s020\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    ii_high: 0.5\n    ii_mid: 3.52\n    ii_low: 31.89\n    ii_high_ci:\n    - 0.41\n    - 0.62\n    ii_mid_ci:\n    - 2.29\n    - 5.35\n    ii_low_ci:\n    - 18.74\n    - 47.22\n    ii_high_median: 0.33\n    ii_mid_median: 1.55\n    ii_low_median: 9.56\n    kv_ppl_high: 1.24\n    kv_ppl_mid: 3.65\n    kv_ppl_low: 14.11\n    both_ppl_high: 2.7\n    both_ppl_mid: 8.13\n    both_ppl_low: 42.64\n    problems: 50\n    ⚠️_WARNING: pre-fix code, INVALIDATED. Results found on disk after kill but code\n      lacked conda activation fix. Do NOT cite these numbers.\n- exp_id: mvp_v5_fixed_s030\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    ii_high: 1.18\n    ii_mid: 168.53\n    ii_low: 1926.23\n    ii_high_ci:\n    - 0.86\n    - 1.6\n    ii_mid_ci:\n    - 36.91\n    - 348.21\n    ii_low_ci:\n    - 179.17\n    - 4062.57\n    ii_high_median: 0.6\n    ii_mid_median: 7.47\n    ii_low_median: 44.63\n    kv_ppl_high: 1.4\n    kv_ppl_mid: 15.11\n    kv_ppl_low: 40.79\n    both_ppl_high: 5.71\n    both_ppl_mid: 137.61\n    both_ppl_low: 963.2\n    problems: 50\n    ⚠️_WARNING: pre-fix code, INVALIDATED. Results found on disk after kill but code\n      lacked conda activation fix. Do NOT cite these numbers.\n- exp_id: mvp_v5_fixed_s015\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ii_high: 0.306\n    ii_mid: 1.274\n    ii_low: 8.786\n    ii_high_ci:\n    - 0.256\n    - 0.359\n    ii_mid_ci:\n    - 0.895\n    - 1.749\n    ii_low_ci:\n    - 5.294\n    - 12.684\n    ii_high_median: 0.205\n    ii_mid_median: 0.696\n    ii_low_median: 2.627\n    ii_high_winsorized: 0.289\n    ii_mid_winsorized: 1.139\n    ii_low_winsorized: 8.408\n    kv_ppl_high: 1.2147\n    kv_ppl_mid: 2.1276\n    kv_ppl_low: 6.7451\n    both_ppl_high: 2.2835\n    both_ppl_mid: 3.9408\n    both_ppl_low: 16.9987\n    problems: 50\n    segments: 1356\n- exp_id: mvp_v5_fixed_s025\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ii_high: 0.851\n    ii_mid: 9.306\n    ii_low: 96.715\n    ii_high_ci:\n    - 0.703\n    - 0.999\n    ii_mid_ci:\n    - 6.092\n    - 13.303\n    ii_low_ci:\n    - 59.642\n    - 143.188\n    ii_high_median: 0.584\n    ii_mid_median: 4.522\n    ii_low_median: 30.903\n    ii_high_winsorized: 0.802\n    ii_mid_winsorized: 8.156\n    ii_low_winsorized: 94.931\n    kv_ppl_high: 1.3108\n    kv_ppl_mid: 6.1778\n    kv_ppl_low: 23.8919\n    both_ppl_high: 3.4623\n    both_ppl_mid: 16.4148\n    both_ppl_low: 104.1749\n    problems: 50\n    segments: 1356\n- exp_id: mvp_v5_fixed_s020_r2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ii_high_median: 0.3333\n    ii_mid_median: 1.5479\n    ii_low_median: 9.5627\n    ii_high_mean: 0.5044\n    ii_mid_mean: 3.5155\n    ii_low_mean: 31.8937\n    ii_high_ci:\n    - 0.41\n    - 0.62\n    ii_mid_ci:\n    - 2.29\n    - 5.35\n    ii_low_ci:\n    - 18.74\n    - 47.22\n    kv_ppl_high: 1.24\n    kv_ppl_mid: 3.65\n    kv_ppl_low: 14.11\n    both_ppl_high: 2.7\n    both_ppl_mid: 8.13\n    both_ppl_low: 42.64\n    problems: 50\n- exp_id: mvp_v5_fixed_s030_r2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ii_high_median: 0.5964\n    ii_mid_median: 7.4671\n    ii_low_median: 44.6324\n    ii_high_mean: 1.1832\n    ii_mid_mean: 168.53\n    ii_low_mean: 1926.23\n    ii_high_ci:\n    - 0.86\n    - 1.6\n    ii_mid_ci:\n    - 36.91\n    - 348.21\n    ii_low_ci:\n    - 179.17\n    - 4062.57\n    kv_ppl_high: 1.4\n    kv_ppl_mid: 15.11\n    kv_ppl_low: 40.79\n    both_ppl_high: 5.71\n    both_ppl_mid: 137.61\n    both_ppl_low: 963.2\n    problems: 50\n- exp_id: mvp_v5_random_s015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 0.1606\n    ii_mid_median: 0.252\n    ii_low_median: 0.1831\n    ii_high_mean: 0.4563\n    ii_mid_mean: 0.5134\n    ii_low_mean: 0.4775\n    ii_high_ci:\n    - 0.12\n    - 0.77\n    ii_mid_ci:\n    - 0.34\n    - 0.74\n    ii_low_ci:\n    - 0.28\n    - 0.7\n    kv_ppl_high: 3.14\n    kv_ppl_mid: 2.91\n    kv_ppl_low: 3.61\n    both_ppl_high: 3.92\n    both_ppl_mid: 4.14\n    both_ppl_low: 4.71\n    problems: 50\n- exp_id: mvp_v5_random_s025\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 3.0024\n    ii_mid_median: 2.9846\n    ii_low_median: 2.9146\n    ii_high_mean: 3.9052\n    ii_mid_mean: 7.9491\n    ii_low_mean: 3.9114\n    ii_high_ci:\n    - 0.98\n    - 6.34\n    ii_mid_ci:\n    - 4.67\n    - 11.87\n    ii_low_ci:\n    - 2.71\n    - 5.24\n    kv_ppl_high: 6.39\n    kv_ppl_mid: 6.11\n    kv_ppl_low: 9.07\n    both_ppl_high: 17.06\n    both_ppl_mid: 15.38\n    both_ppl_low: 29.32\n    problems: 50\n- exp_id: mvp_v5_random_s020\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 0.321331\n    ii_mid_median: 0.455663\n    ii_low_median: 0.591916\n    ii_high_mean: 0.855584\n    ii_mid_mean: 1.258123\n    ii_low_mean: 0.956933\n    ii_high_ci:\n    - -0.124133\n    - 1.616883\n    ii_mid_ci:\n    - 0.674852\n    - 2.075565\n    ii_low_ci:\n    - 0.583856\n    - 1.413355\n    kv_ppl_high: 4.2537\n    kv_ppl_mid: 4.3064\n    kv_ppl_low: 5.4048\n    both_ppl_high: 7.9749\n    both_ppl_mid: 6.8553\n    both_ppl_low: 22.5868\n    problems: 50\n- exp_id: mvp_v5_random_s030\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 5.377512\n    ii_mid_median: 5.886454\n    ii_low_median: 3.776818\n    ii_high_mean: 22.734534\n    ii_mid_mean: 10.943319\n    ii_low_mean: 11.840449\n    ii_high_ci:\n    - 10.352118\n    - 42.551951\n    ii_mid_ci:\n    - 7.398611\n    - 14.765315\n    ii_low_ci:\n    - 4.097309\n    - 23.545273\n    kv_ppl_high: 8.1027\n    kv_ppl_mid: 8.5701\n    kv_ppl_low: 13.4922\n    both_ppl_high: 41.3452\n    both_ppl_mid: 24.1992\n    both_ppl_low: 68.5301\n    problems: 50\n- exp_id: v6_importance_s025\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 0.6641\n    ii_mid_median: 5.3067\n    ii_low_median: 24.1619\n    ii_high_mean: 0.8842\n    ii_mid_mean: 10.057\n    ii_low_mean: 71.8854\n    per_problem_ii_count: 50\n    n_high: 42\n    n_mid: 23\n    n_low: 21\n    problems: 50\n    bootstrap_gradient_paired: 35.72\n    bootstrap_ci_paired:\n    - 9.52\n    - 101.54\n    bootstrap_gradient_unpaired: 36.38\n    bootstrap_ci_unpaired:\n    - 13.19\n    - 97.61\n    bootstrap_p: 0\n- exp_id: v6_importance_s030\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 0.8833\n    ii_mid_median: 7.2706\n    ii_low_median: 34.6937\n    ii_high_mean: 1.5151\n    ii_mid_mean: 78.8215\n    ii_low_mean: 1163.9677\n    per_problem_ii_count: 50\n    n_high: 40\n    n_mid: 22\n    n_low: 20\n    problems: 50\n    bootstrap_gradient_paired: 41.92\n    bootstrap_ci_paired:\n    - 19.14\n    - 299.76\n    bootstrap_gradient_unpaired: 39.28\n    bootstrap_ci_unpaired:\n    - 21.87\n    - 129.59\n    bootstrap_p: 0\n- exp_id: v6_importance_s015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 0.2266\n    ii_mid_median: 0.7432\n    ii_low_median: 2.8762\n    ii_high_mean: 0.2874\n    ii_mid_mean: 1.6858\n    ii_low_mean: 8.5161\n    per_problem_ii_count: 50\n    n_high: 43\n    n_mid: 32\n    n_low: 24\n    problems: 50\n    bootstrap_gradient_paired: 11.53\n    bootstrap_ci_paired:\n    - 3.49\n    - 23.78\n    bootstrap_gradient_unpaired: 12.69\n    bootstrap_ci_unpaired:\n    - 4.96\n    - 28.45\n    bootstrap_p: 0\n- exp_id: v6_importance_s020\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 0.3353\n    ii_mid_median: 1.6733\n    ii_low_median: 9.2538\n    ii_high_mean: 0.4936\n    ii_mid_mean: 4.9538\n    ii_low_mean: 25.8764\n    per_problem_ii_count: 50\n    n_high: 42\n    n_mid: 28\n    n_low: 21\n    problems: 50\n    bootstrap_gradient_paired: 11.05\n    bootstrap_ci_paired:\n    - 5.42\n    - 69.27\n    bootstrap_gradient_unpaired: 27.6\n    bootstrap_ci_unpaired:\n    - 6.55\n    - 75.16\n    bootstrap_p: 0\n- exp_id: qwen_importance_s015\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: qwen_importance_s020\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: qwen_importance_s025\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: qwen_importance_s030\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: v6_random_s015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 0.1606\n    ii_mid_median: 0.252\n    ii_low_median: 0.1831\n    ii_high_mean: 0.4563\n    ii_mid_mean: 0.5134\n    ii_low_mean: 0.4775\n    per_problem_ii_count: 50\n    n_high: 43\n    n_mid: 32\n    n_low: 28\n    bootstrap_gradient_paired: -0.2722\n    bootstrap_ci_paired:\n    - -0.7039\n    - 0.1548\n    bootstrap_p: 0.903\n    bootstrap_gradient_unpaired: -0.0592\n    bootstrap_ci_unpaired:\n    - -0.5341\n    - 0.3877\n    per_problem_ii_stats:\n      high:\n        min: -3.0621\n        max: 5.018\n        mean: 0.5386\n        median: 0.2003\n        std: 1.2085\n      mid:\n        min: -2.7245\n        max: 4.6713\n        mean: 0.3977\n        median: 0.299\n        std: 1.1456\n      low:\n        min: -0.4031\n        max: 3.7005\n        mean: 0.4806\n        median: 0.2465\n        std: 0.779\n    verdict: FAIL\n- exp_id: v6_random_s020\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_mean: 0.855584\n    ii_high_median: 0.321331\n    ii_high_ci:\n    - -0.124133\n    - 1.616883\n    ii_high_winsorized_mean: 0.913496\n    ii_mid_mean: 1.258123\n    ii_mid_median: 0.455663\n    ii_mid_ci:\n    - 0.674852\n    - 2.075565\n    ii_mid_winsorized_mean: 1.074102\n    ii_low_mean: 0.956933\n    ii_low_median: 0.591916\n    ii_low_ci:\n    - 0.583856\n    - 1.413355\n    ii_low_winsorized_mean: 0.96113\n    n_high: 511\n    n_mid: 391\n    n_low: 454\n    problems: 50\n    per_problem_ii_count: 50\n    gradient_mean_low_over_high: 1.118\n    gradient_median_low_over_high: 1.842\n    pass_fail: FAIL\n    perplexity_high_dense: 1.1462\n    perplexity_high_both: 7.9749\n    perplexity_mid_dense: 1.1226\n    perplexity_mid_both: 6.8553\n    perplexity_low_dense: 1.1105\n    perplexity_low_both: 22.5868\n- exp_id: v6_random_s025\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 3.0024\n    ii_mid_median: 2.9846\n    ii_low_median: 2.9146\n    ii_high_mean: 3.9052\n    ii_mid_mean: 7.9491\n    ii_low_mean: 3.9114\n    per_problem_ii_count: 50\n    n_high: 36\n    n_mid: 25\n    n_low: 24\n    bootstrap_gradient_paired: -0.1199\n    bootstrap_ci_paired:\n    - -1.517\n    - 1.2461\n    bootstrap_p: 0.559\n    bootstrap_gradient_unpaired: -0.8616\n    bootstrap_ci_unpaired:\n    - -3.3911\n    - 1.5169\n    per_problem_ii_stats:\n      high:\n        min: -6.1388\n        max: 25.2471\n        mean: 4.4098\n        median: 3.0421\n        std: 6.0734\n      mid:\n        min: 0.158\n        max: 108.7242\n        mean: 7.5626\n        median: 2.1407\n        std: 20.926\n      low:\n        min: -0.1953\n        max: 12.8555\n        mean: 3.5806\n        median: 2.7289\n        std: 3.4915\n    verdict: FAIL\n- exp_id: v6_random_s030\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: v6_random_s030_r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: bf16_importance_s015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: -0.150213\n        median: 0.005752\n        ci:\n        - -0.294614\n        - -0.055385\n        winsorized_mean: -0.062378\n        skewness: -14.9912\n      mid:\n        mean: 0.447301\n        median: 0.080738\n        ci:\n        - 0.267993\n        - 0.668749\n        winsorized_mean: 0.324751\n        skewness: 4.7221\n      low:\n        mean: 2.405837\n        median: 0.398291\n        ci:\n        - 1.478784\n        - 3.667675\n        winsorized_mean: 1.278857\n        skewness: 9.5402\n    per_problem_ii_stats:\n      high:\n        n: 49\n        min: -0.188061\n        max: 0.335853\n        mean: -0.013405\n        median: 0.00012\n        std: 0.078483\n      mid:\n        n: 40\n        min: -0.169092\n        max: 3.88198\n        mean: 0.308621\n        median: 0.107114\n        std: 0.690186\n      low:\n        n: 50\n        min: -0.872983\n        max: 9.10289\n        mean: 0.725504\n        median: 0.315517\n        std: 1.731056\n    gradient_paired_aggregate_legacy: 69.24\n    median_difference: 0.3925\n    n_problems: 50\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: true\n      overall: PASS\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    perplexity:\n      high:\n        dense: 1.1689\n        attn: 1.4861\n        kv: 1.4481\n        both: 1.5911\n      mid:\n        dense: 1.2269\n        attn: 1.5137\n        kv: 2.5971\n        both: 3.4541\n      low:\n        dense: 1.2286\n        attn: 1.6147\n        kv: 8.9201\n        both: 12.5084\n- exp_id: bf16_importance_s020\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 0.1289\n        median: 0.0145\n        ci:\n        - -0.1975\n        - 0.6647\n        winsorized_mean: -0.0297\n        skewness: 16.67\n      mid:\n        mean: 1.2604\n        median: 0.2027\n        ci:\n        - 0.7466\n        - 1.8962\n        winsorized_mean: 0.766\n        skewness: 7.05\n      low:\n        mean: 6.0288\n        median: 1.4963\n        ci:\n        - 4.4671\n        - 7.9237\n        winsorized_mean: 4.3426\n        skewness: 6.01\n    per_problem_ii_stats:\n      high:\n        n: 49\n        min: -0.1884\n        max: 0.4196\n        mean: 0.0025\n        median: 0.0036\n        std: 0.0966\n      mid:\n        n: 40\n        min: -0.0519\n        max: 8.6969\n        mean: 0.6795\n        median: 0.1977\n        std: 1.4998\n      low:\n        n: 50\n        min: -1.6151\n        max: 22.6875\n        mean: 2.2301\n        median: 1.128\n        std: 4.3758\n    gradient_paired_aggregate_legacy: 5.9\n    median_difference: 1.4818\n    n_problems: 50\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: false\n      overall: PASS\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    perplexity:\n      high:\n        dense: 1.1689\n        attn: 1.5233\n        kv: 1.6191\n        both: 2.1047\n      mid:\n        dense: 1.2269\n        attn: 1.5375\n        kv: 3.5164\n        both: 5.4246\n      low:\n        dense: 1.2286\n        attn: 1.6486\n        kv: 15.7987\n        both: 23.74\n- exp_id: bf16_importance_s025\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 0.302756\n        median: 0.032363\n        ci:\n        - 0.083714\n        - 0.543977\n        winsorized_mean: 0.200962\n        skewness: 4.8826\n      mid:\n        mean: 5.729665\n        median: 1.118069\n        ci:\n        - 3.455574\n        - 8.471799\n        winsorized_mean: 4.189902\n        skewness: 8.2799\n      low:\n        mean: 25.852951\n        median: 7.195958\n        ci:\n        - 19.077082\n        - 33.497293\n        winsorized_mean: 19.319103\n        skewness: 7.3986\n    per_problem_ii_stats:\n      high:\n        n: 49\n        min: -0.316321\n        max: 4.003714\n        mean: 0.133714\n        median: 0.009873\n        std: 0.595358\n      mid:\n        n: 40\n        min: -0.024794\n        max: 18.720486\n        mean: 2.537744\n        median: 1.05707\n        std: 3.962575\n      low:\n        n: 50\n        min: -1.854733\n        max: 75.467653\n        mean: 11.28281\n        median: 3.954593\n        std: 16.620011\n    gradient_paired_aggregate_legacy: 222.35\n    median_difference: 7.1636\n    n_problems: 50\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: false\n      overall: PASS\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    perplexity:\n      high:\n        dense: 1.1689\n        attn: 1.6511\n        kv: 1.8628\n        both: 2.7026\n      mid:\n        dense: 1.2269\n        attn: 1.7039\n        kv: 5.6205\n        both: 13.3436\n      low:\n        dense: 1.2286\n        attn: 1.8366\n        kv: 31.756\n        both: 63.668\n- exp_id: bf16_importance_s030\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 0.5547\n        median: 0.0534\n        ci:\n        - 0.2773\n        - 0.9198\n        winsorized_mean: 0.3367\n        skewness: 10.62\n      mid:\n        mean: 11.3\n        median: 2.2833\n        ci:\n        - 6.865\n        - 17.2633\n        winsorized_mean: 8.1752\n        skewness: 9.19\n      low:\n        mean: 57.7946\n        median: 14.6395\n        ci:\n        - 41.4416\n        - 77.0467\n        winsorized_mean: 39.3143\n        skewness: 8.31\n    per_problem_ii_stats:\n      high:\n        n: 49\n        min: -0.5095\n        max: 4.4457\n        mean: 0.1976\n        median: 0.0343\n        std: 0.6793\n      mid:\n        n: 40\n        min: -0.1989\n        max: 34.0258\n        mean: 5.2585\n        median: 1.5173\n        std: 7.9382\n      low:\n        n: 50\n        min: -7.3027\n        max: 126.7985\n        mean: 22.6601\n        median: 9.9731\n        std: 28.4096\n    gradient_paired_aggregate_legacy: 57.24\n    median_difference: 14.5861\n    n_problems: 50\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: false\n      overall: PASS\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    perplexity:\n      high:\n        dense: 1.1689\n        attn: 1.7123\n        kv: 2.0544\n        both: 3.2372\n      mid:\n        dense: 1.2269\n        attn: 1.7894\n        kv: 9.4821\n        both: 24.2847\n      low:\n        dense: 1.2286\n        attn: 1.9347\n        kv: 51.6485\n        both: 122.61\n- exp_id: bf16_random_s015\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: bf16_random_s020\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: bf16_random_s025\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: bf16_random_s030\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: bf16_qwen_importance_s015\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: bf16_qwen_importance_s020\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: bf16_qwen_importance_s025\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: bf16_qwen_importance_s030\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: v6_random_s030_r3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    II_high_mean: 9.2364\n    II_mid_mean: -230.7604\n    II_low_mean: -7.4119\n    II_high_median: 4.0237\n    II_mid_median: 2.4272\n    II_low_median: 4.735\n    ppl_low_both: 88.94\n    per_problem_count: 50\n- exp_id: bf16_ds_imp_s015\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    median_difference: 0.323579\n    permutation_p: 0\n    cohens_d: 0.6068\n    bootstrap_ci_95:\n    - 0.198824\n    - 0.471566\n    wilcoxon_p: 0\n    n_bootstrap: 10000\n    n_paired: 49\n- exp_id: bf16_ds_imp_s020\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    median_difference: 1.15202\n    permutation_p: 0\n    cohens_d: 0.725\n    bootstrap_ci_95:\n    - 0.655454\n    - 1.256001\n    wilcoxon_p: 0\n    n_bootstrap: 10000\n    n_paired: 49\n- exp_id: bf16_ds_imp_s025\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    median_difference: 3.968568\n    permutation_p: 0\n    cohens_d: 0.9534\n    bootstrap_ci_95:\n    - 2.829037\n    - 5.291756\n    wilcoxon_p: 0\n    n_bootstrap: 10000\n    n_paired: 49\n- exp_id: bf16_ds_imp_s030\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    median_difference: 9.943595\n    permutation_p: 0\n    cohens_d: 1.1263\n    bootstrap_ci_95:\n    - 8.391554\n    - 16.652865\n    wilcoxon_p: 0\n    n_bootstrap: 10000\n    n_paired: 49\n- exp_id: bf16_ds_rand_s015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 0.2208\n        median: 0.0931\n        ci:\n        - -1.0091\n        - 1.5243\n        median_ci:\n        - 0.0024\n        - 0.1515\n        winsorized_mean: 0.3161\n        skewness: -5.4\n      mid:\n        mean: -3.3604\n        median: 0.0967\n        ci:\n        - -8.4057\n        - 0.3697\n        median_ci:\n        - 0.0219\n        - 0.197\n        winsorized_mean: -0.6366\n        skewness: -10.56\n      low:\n        mean: -1.8952\n        median: 0.1026\n        ci:\n        - -4.9698\n        - 0.2741\n        median_ci:\n        - 0.044\n        - 0.1755\n        winsorized_mean: 0.0521\n        skewness: -11.57\n    perplexity:\n      high:\n        dense: 1.1687\n        attn: 3.5947\n        kv: 2.9239\n        both: 5.7569\n      mid:\n        dense: 1.2269\n        attn: 297.7957\n        kv: 2.915\n        both: 11.3156\n      low:\n        dense: 1.2284\n        attn: 11.3419\n        kv: 3.6161\n        both: 6.2886\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    n_problems: 50\n    pass_fail:\n      ci_overlap: false\n      sign_reversal: false\n      overall: FAIL\n    median_difference: 0.0095\n- exp_id: bf16_ds_rand_s020\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 1.1216\n        median: 0.2918\n        ci:\n        - 0.0796\n        - 2.5834\n        median_ci:\n        - 0.1598\n        - 0.4581\n        winsorized_mean: 1.7664\n        skewness: 9.59\n      mid:\n        mean: -1.5827\n        median: 0.3504\n        ci:\n        - -6.0963\n        - 1.5735\n        median_ci:\n        - 0.1993\n        - 0.5226\n        winsorized_mean: 0.5839\n        skewness: -12.31\n      low:\n        mean: -0.4116\n        median: 0.2763\n        ci:\n        - -2.6034\n        - 1.209\n        median_ci:\n        - 0.2194\n        - 0.5487\n        winsorized_mean: 0.9942\n        skewness: -10.07\n    perplexity:\n      high:\n        dense: 1.1687\n        attn: 3.1905\n        kv: 3.8002\n        both: 8.8129\n      mid:\n        dense: 1.2269\n        attn: 67.8504\n        kv: 3.788\n        both: 11.4974\n      low:\n        dense: 1.2284\n        attn: 8.592\n        kv: 5.0078\n        both: 9.2001\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    n_problems: 50\n    pass_fail:\n      ci_overlap: false\n      sign_reversal: false\n      overall: FAIL\n    median_difference: -0.0155\n- exp_id: bf16_ds_rand_s025\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 3.59\n        median: 0.8182\n        ci:\n        - 1.4021\n        - 6.2327\n        median_ci:\n        - 0.5075\n        - 1.7217\n        winsorized_mean: 6.3965\n        skewness: -7.57\n      mid:\n        mean: -1.8455\n        median: 0.9324\n        ci:\n        - -10.3663\n        - 4.9342\n        median_ci:\n        - 0.7331\n        - 1.7003\n        winsorized_mean: 3.1014\n        skewness: -12.76\n      low:\n        mean: 0.7212\n        median: 1.3627\n        ci:\n        - -4.2068\n        - 4.5006\n        median_ci:\n        - 1.0869\n        - 2.6866\n        winsorized_mean: 4.1866\n        skewness: -15.85\n    perplexity:\n      high:\n        dense: 1.1687\n        attn: 7.237\n        kv: 4.9751\n        both: 17.7423\n      mid:\n        dense: 1.2269\n        attn: 868.3199\n        kv: 5.1165\n        both: 29.4661\n      low:\n        dense: 1.2284\n        attn: 24.3571\n        kv: 6.7993\n        both: 17.9694\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    n_problems: 50\n    pass_fail:\n      ci_overlap: false\n      sign_reversal: false\n      overall: FAIL\n    median_difference: 0.5445\n- exp_id: bf16_ds_rand_s030\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 7.5555\n        median: 2.5031\n        ci:\n        - 4.4087\n        - 11.6199\n        median_ci:\n        - 1.3292\n        - 4.1205\n        winsorized_mean: null\n        skewness: null\n      mid:\n        mean: 6.2518\n        median: 2.5918\n        ci:\n        - 2.1767\n        - 10.4757\n        median_ci:\n        - 1.8397\n        - 3.7888\n        winsorized_mean: null\n        skewness: null\n      low:\n        mean: 6.8323\n        median: 4.0414\n        ci:\n        - 3.2428\n        - 10.6996\n        median_ci:\n        - 2.2686\n        - 6.3579\n        winsorized_mean: null\n        skewness: null\n    perplexity:\n      high:\n        dense: 1.1687\n        attn: 16.7892\n        kv: 8.8073\n        both: 40.7553\n      mid:\n        dense: 1.2269\n        attn: 2461.9219\n        kv: 8.6662\n        both: 62.4422\n      low:\n        dense: 1.2284\n        attn: 55.2916\n        kv: 11.5789\n        both: 37.6009\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    n_problems: 50\n    pass_fail:\n      ci_overlap: false\n      sign_reversal: false\n      overall: FAIL\n    median_difference: 1.5383\n- exp_id: bf16_qw_imp_s015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    median_difference: 0.047619\n    permutation_p: 0.0001\n    cohens_d: 0.3705\n    bootstrap_ci_95:\n    - -0.005077\n    - 0.109517\n    wilcoxon_p: 0.02958\n    n_bootstrap: 10000\n    n_paired: 46\n- exp_id: bf16_qw_imp_s020\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    median_difference: 0.207511\n    permutation_p: 0\n    cohens_d: 0.7224\n    bootstrap_ci_95:\n    - 0.067222\n    - 0.40226\n    wilcoxon_p: 3.4e-05\n    n_bootstrap: 10000\n    n_paired: 46\n- exp_id: bf16_qw_imp_s025\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    median_difference: 1.108706\n    permutation_p: 0\n    cohens_d: 1.2329\n    bootstrap_ci_95:\n    - 0.609247\n    - 1.469002\n    wilcoxon_p: 0\n    n_bootstrap: 10000\n    n_paired: 46\n- exp_id: bf16_qw_imp_s030\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    median_difference: 2.619385\n    permutation_p: 0\n    cohens_d: 1.4394\n    bootstrap_ci_95:\n    - 1.722281\n    - 3.651063\n    wilcoxon_p: 0\n    n_bootstrap: 10000\n    n_paired: 46\n- exp_id: bf16_qw_rand_s015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 1.6652\n        median: 0.1381\n        ci:\n        - 1.0986\n        - 2.4042\n        median_ci:\n        - 0.1025\n        - 0.2074\n        winsorized_mean: 1.0044\n        skewness: 7.1842\n      mid:\n        mean: 1.6975\n        median: 0.2194\n        ci:\n        - 0.4473\n        - 3.4612\n        median_ci:\n        - -0.0048\n        - 0.6621\n        winsorized_mean: 1.4038\n        skewness: 3.2101\n      low:\n        mean: 1.4082\n        median: 0.1878\n        ci:\n        - 0.8358\n        - 2.06\n        median_ci:\n        - 0.0962\n        - 0.3139\n        winsorized_mean: 0.9403\n        skewness: 7.1113\n    perplexity:\n      high:\n        dense: 1.0737\n        attn: 1.3939\n        kv: 2.0487\n        both: 4.2076\n      mid:\n        dense: 1.1322\n        attn: 1.4175\n        kv: 2.3709\n        both: 4.6105\n      low:\n        dense: 1.1517\n        attn: 1.7177\n        kv: 3.3253\n        both: 5.4788\n    phase_stats:\n      high:\n        n_tokens: 16289\n        n_segments: 295\n      mid:\n        n_tokens: 4372\n        n_segments: 26\n      low:\n        n_tokens: 32227\n        n_segments: 276\n    n_problems: 50\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: false\n      overall: FAIL\n    median_difference: -0.029401\n    permutation_test:\n      p_value: 0.7657\n      B: 10000\n    cohens_d: -0.0507\n    bootstrap_ci_95:\n    - -0.2106\n    - 0.2124\n    wilcoxon_p: 0.862554\n    phase_median_ii:\n      high: 0.1381\n      mid: 0.2194\n      low: 0.1878\n- exp_id: bf16_qw_rand_s020\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 2.58579\n        median: 0.48549\n        ci:\n        - 1.769404\n        - 3.501692\n        median_ci:\n        - 0.304626\n        - 0.658814\n        winsorized_mean: 1.80021\n        skewness: 5.4038\n      mid:\n        mean: 5.69684\n        median: 0.76699\n        ci:\n        - 1.69004\n        - 12.276143\n        median_ci:\n        - 0.482838\n        - 3.392541\n        winsorized_mean: 4.304174\n        skewness: 3.526\n      low:\n        mean: 65.915714\n        median: 0.614438\n        ci:\n        - -18.581948\n        - 221.709429\n        median_ci:\n        - 0.484725\n        - 0.848787\n        winsorized_mean: 2.389244\n        skewness: 16.2163\n    perplexity:\n      high:\n        dense: 1.0737\n        attn: 1.6115\n        kv: 2.5041\n        both: 5.9394\n      mid:\n        dense: 1.1322\n        attn: 1.7583\n        kv: 3.0658\n        both: 10.5578\n      low:\n        dense: 1.1517\n        attn: 75.631\n        kv: 4.3535\n        both: 140.6269\n    phase_stats:\n      high:\n        n_tokens: 16289\n        n_segments: 295\n      mid:\n        n_tokens: 4372\n        n_segments: 26\n      low:\n        n_tokens: 32227\n        n_segments: 276\n    n_problems: 50\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: false\n      overall: FAIL\n    median_difference: 0.128948\n    permutation_test:\n      p_value: 0.352\n      B: 10000\n    cohens_d: 0.247\n    bootstrap_ci_95:\n    - -0.139\n    - 0.215\n    wilcoxon_p: 0.149\n    phase_median_ii:\n      high: 0.4739\n      mid: 0.8757\n      low: 0.4847\n- exp_id: bf16_qw_rand_s025\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 14.4213\n        median: 1.6043\n        ci:\n        - 7.1074\n        - 23.4587\n        median_ci:\n        - 0.6977\n        - 3.0736\n        winsorized_mean: 9.3765\n        skewness: 4.8263\n      mid:\n        mean: 18.6458\n        median: 2.2225\n        ci:\n        - 3.3729\n        - 41.6037\n        median_ci:\n        - 0.6093\n        - 11.5889\n        winsorized_mean: 14.2901\n        skewness: 3.8245\n      low:\n        mean: 17.7277\n        median: 2.2641\n        ci:\n        - 4.3523\n        - 37.2093\n        median_ci:\n        - 1.2218\n        - 4.8561\n        winsorized_mean: 9.9876\n        skewness: 5.7652\n    perplexity:\n      high:\n        dense: 1.0737\n        attn: 2.0183\n        kv: 3.1882\n        both: 9.7654\n      mid:\n        dense: 1.1322\n        attn: 2.3476\n        kv: 4.0124\n        both: 17.3298\n      low:\n        dense: 1.1517\n        attn: 2.7834\n        kv: 5.8762\n        both: 25.4321\n    phase_stats:\n      high:\n        n_tokens: 16289\n        n_segments: 295\n      mid:\n        n_tokens: 4372\n        n_segments: 26\n      low:\n        n_tokens: 32227\n        n_segments: 276\n    n_problems: 50\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: false\n      overall: FAIL\n    median_difference: 1.144074\n    permutation_test:\n      p_value: 0.1679\n      B: 10000\n    cohens_d: 0.1574\n    bootstrap_ci_95:\n    - -0.3166\n    - 4.1645\n    wilcoxon_p: 0.010313\n    phase_median_ii:\n      high: 1.6043\n      mid: 2.2225\n      low: 2.2641\n- exp_id: bf16_qw_rand_s030\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    median_high: 4.200557\n    median_mid: 6.477036\n    median_low: 8.065662\n    median_diff: 2.418272\n    permutation_p: 0.012\n    cohens_d: -0.03513\n    wilcoxon_p: 0.01566\n    bootstrap_ci_low: 0.241897\n    bootstrap_ci_high: 3.314824\n- exp_id: c4_entropy\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    importance_entropy_delta:\n      s015: -0.0402\n      s020: -0.0472\n      s025: -0.0446\n      s030: -0.0436\n    random_entropy_delta:\n      s015: 0.1283\n      s020: 0.136\n      s025: 0.2171\n      s030: 0.2327\n    importance_gini_delta:\n      s015: -0.0301\n      s020: -0.0404\n      s025: -0.0647\n      s030: -0.0806\n    random_gini_delta:\n      s015: -0.0309\n      s020: -0.0403\n      s025: -0.062\n      s030: -0.0732\n    importance_cv_delta:\n      s015: -0.564\n      s020: -0.774\n      s025: -1.287\n      s030: -1.665\n    random_cv_delta:\n      s015: -1.021\n      s020: -1.203\n      s025: -1.923\n      s030: -2.137\n    problems_completed: 30\n    runtime_minutes: 69.1\n- exp_id: qwen_c4_entropy\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    problems_completed: 30\n    qwen_importance_entropy_delta:\n      s015: -0.0733\n      s020: -0.0759\n      s025: 0.0451\n      s030: -0.0072\n    qwen_random_entropy_delta:\n      s015: 0.0838\n      s020: 0.0901\n      s025: 0.2168\n      s030: 0.1968\n    qwen_importance_gini_delta:\n      s015: -0.0103\n      s020: -0.0121\n      s025: -0.01\n      s030: -0.0202\n    qwen_random_gini_delta:\n      s015: -0.0186\n      s020: -0.0229\n      s025: -0.0337\n      s030: -0.0448\n    qwen_importance_cv_delta:\n      s015: -0.045\n      s020: -0.208\n      s025: -1.491\n      s030: -1.142\n    qwen_random_cv_delta:\n      s015: -0.778\n      s020: -0.889\n      s025: -1.5\n      s030: -1.677\n    cross_model_notes: random entropy increase consistent; importance entropy collapse\n      inconsistent at s025 (reversed to +0.045) and near-zero at s030; gini/cv directions\n      consistent but Qwen magnitudes smaller\n- exp_id: bf16_ds_imp_s010\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    verdict: FAIL\n    problems: 50\n    II_high_sparsity_median: 0.0027\n    II_high_sparsity_mean: -0.1998\n    II_low_sparsity_median: 0.0151\n    II_low_sparsity_mean: -0.1066\n    II_mid_sparsity_median: 0.0061\n    II_mid_sparsity_mean: -0.0131\n    high_sparsity_tokens: 21086\n    low_sparsity_tokens: 27748\n    mid_sparsity_tokens: 13306\n- exp_id: bf16_ds_imp_s035\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    verdict: PASS\n    problems: 50\n    II_high_sparsity_median: 0.1051\n    II_high_sparsity_mean: 1.4309\n    II_low_sparsity_median: 28.7649\n    II_low_sparsity_mean: 104.1892\n    II_mid_sparsity_median: 4.9542\n    II_mid_sparsity_mean: 20.326\n    high_sparsity_tokens: 21086\n    low_sparsity_tokens: 27748\n    mid_sparsity_tokens: 13306\n    ci_overlap_test: low_sparsity vs mid_sparsity CI non-overlapping at 0.35\n- exp_id: bf16_qw_imp_s010\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_problems: 50\n    overall_verdict: PASS\n    ci_overlap_test: PASS\n    sign_reversal_test: FAIL\n    high_sparsity_II_median: 0.0001\n    high_sparsity_II_median_CI:\n    - -0.0028\n    - 0.0005\n    high_sparsity_II_mean: -0.0887\n    high_sparsity_II_mean_CI:\n    - -0.1235\n    - -0.0591\n    low_sparsity_II_median: -0.0444\n    low_sparsity_II_median_CI:\n    - -0.0967\n    - -0.0152\n    low_sparsity_II_mean: -0.2431\n    low_sparsity_II_mean_CI:\n    - -0.3817\n    - -0.1202\n    mid_sparsity_II_median: -0.0359\n    mid_sparsity_II_median_CI:\n    - -0.0963\n    - -0.015\n    mid_sparsity_II_mean: -0.084\n    mid_sparsity_II_mean_CI:\n    - -0.1366\n    - -0.035\n    ppl_high_dense: 1.074\n    ppl_high_both: 1.228\n    ppl_low_dense: 1.152\n    ppl_low_both: 3.204\n    ppl_mid_dense: 1.133\n    ppl_mid_both: 1.741\n- exp_id: bf16_qw_imp_s035\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_problems: 50\n    overall_verdict: PASS\n    ci_overlap_test: PASS\n    sign_reversal_test: FAIL\n    high_sparsity_II_median: 0.0232\n    high_sparsity_II_median_CI:\n    - 0.0154\n    - 0.0383\n    high_sparsity_II_mean: 0.1643\n    high_sparsity_II_mean_CI:\n    - 0.0844\n    - 0.2495\n    low_sparsity_II_median: 8.2358\n    low_sparsity_II_median_CI:\n    - 6.1564\n    - 10.9231\n    low_sparsity_II_mean: 18.9673\n    low_sparsity_II_mean_CI:\n    - 14.5015\n    - 23.9752\n    mid_sparsity_II_median: 0.9577\n    mid_sparsity_II_median_CI:\n    - 0.171\n    - 3.5575\n    mid_sparsity_II_mean: 8.0734\n    mid_sparsity_II_mean_CI:\n    - 2.0224\n    - 16.8946\n    ppl_high_dense: 1.0738\n    ppl_high_both: 2.3435\n    ppl_low_dense: 1.1518\n    ppl_low_both: 58.0358\n    ppl_mid_dense: 1.1327\n    ppl_mid_both: 20.9912\n    high_sparsity_tokens: 16289\n    low_sparsity_tokens: 32227\n    mid_sparsity_tokens: 4372\n- exp_id: c2_n500_deepseek\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_problems: 500\n    effective_n: 496\n    mid_null_rate: 0.102\n    imp_s015_median_ii: 0.3907\n    imp_s015_ci:\n    - 0.3496\n    - 0.4431\n    imp_s015_wilcoxon_p: 1.27e-70\n    imp_s020_median_ii: 1.2149\n    imp_s020_ci:\n    - 1.1072\n    - 1.3365\n    imp_s020_wilcoxon_p: 3.98e-75\n    imp_s025_median_ii: 3.9857\n    imp_s025_ci:\n    - 3.5272\n    - 4.3588\n    imp_s025_wilcoxon_p: 1.99e-78\n    imp_s030_median_ii: 8.4813\n    imp_s030_ci:\n    - 7.7543\n    - 9.6919\n    imp_s030_wilcoxon_p: 1.09e-79\n    rand_s015_median_ii: 0.0139\n    rand_s015_wilcoxon_p: 0.863\n    rand_s020_median_ii: 0.0315\n    rand_s020_wilcoxon_p: 0.28\n    rand_s025_median_ii: 0.2574\n    rand_s025_bonf_p: 0.005839\n    rand_s025_fdr_p: 0.001914\n    rand_s030_median_ii: 0.5096\n    rand_s030_bonf_p: 0.005903\n    rand_s030_fdr_p: 0.001914\n    dz_s015_s020: -0.925\n    dz_s020_s025: -0.824\n    dz_s025_s030: -0.773\n    dz_s015_s030: -0.944\n    all_dz_reliable: true\n    dose_response_monotonic: true\n    dose_response_spearman_rho: 1\n    dose_response_perm_p: 0.0417\n    imp_rand_ratio_range: 15.5-38.6x\n    bonferroni_k: 4\n    bonferroni_note: Bonferroni k=4 family-wise (D066 revision)\n- exp_id: c3_llama_arch\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: c2_ds_n500\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: c2_qw_n500\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: c3_llama\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    model: DeepSeek-R1-Distill-Llama-8B\n    n_problems: 50\n    n_valid: 49\n    n_skipped: 1\n    conditions_completed: 8/8\n    n_bootstrap: 10000\n    bonferroni_k: 4\n    imp_vs_rand_dz:\n      s015: 0.1923\n      s020: 0.255\n      s025: 0.2902\n      s030: 0.3352\n    imp_vs_rand_dz_ci:\n      s015:\n      - -0.0862\n      - 0.496\n      s020:\n      - -0.0248\n      - 0.5381\n      s025:\n      - 0.0081\n      - 0.6121\n      s030:\n      - 0.0606\n      - 0.6629\n    imp_vs_rand_dz_interpretation:\n      s015: negligible\n      s020: small\n      s025: small\n      s030: small\n    imp_vs_rand_dz_monotonic: true\n    phase_gradient_importance_dz:\n      s015: 1.0079\n      s020: 1.108\n      s025: 1.1227\n      s030: 1.0038\n    phase_gradient_importance_dz_ci:\n      s015:\n      - 0.593\n      - 1.7025\n      s020:\n      - 0.8144\n      - 1.5698\n      s025:\n      - 0.8735\n      - 1.5768\n      s030:\n      - 0.8099\n      - 1.3519\n    phase_gradient_importance_interpretation: all_large\n    phase_gradient_random_dz:\n      s015: 0.3497\n      s020: 0.373\n      s025: 0.4476\n      s030: 0.4385\n    phase_gradient_random_dz_ci:\n      s015:\n      - 0.0665\n      - 0.6916\n      s020:\n      - 0.0868\n      - 0.7335\n      s025:\n      - 0.1669\n      - 0.7698\n      s030:\n      - 0.1966\n      - 0.707\n    phase_gradient_random_interpretation: all_small\n    median_diff:\n      s015: 0.0203\n      s020: 0.0221\n      s025: 0.0947\n      s030: 0.3562\n    median_diff_ci:\n      s015:\n      - 0.0016\n      - 0.0435\n      s020:\n      - -0.0905\n      - 0.187\n      s025:\n      - -0.0037\n      - 0.3029\n      s030:\n      - -0.0691\n      - 0.5442\n    wilcoxon_p:\n      s015: 0.0549\n      s020: 0.0632\n      s025: 0.0209\n      s030: 0.0074\n    wilcoxon_p_bonferroni:\n      s015: 0.2195\n      s020: 0.2527\n      s025: 0.0834\n      s030: 0.0294\n    significant_bonferroni:\n      s015: false\n      s020: false\n      s025: false\n      s030: true\n    cross_arch_comparison:\n      deepseek_importance_dz:\n        s015: 0.4416\n        s020: 0.5195\n        s025: 0.6831\n        s030: 0.8031\n      llama_importance_dz:\n        s015: 1.0079\n        s020: 1.108\n        s025: 1.1227\n        s030: 1.0038\n      delta:\n        s015: 0.5663\n        s020: 0.5885\n        s025: 0.4396\n        s030: 0.2007\n      note: LLaMA shows uniformly large d_z (all >1.0) vs DeepSeek medium-to-large\n- exp_id: c5b_pilot\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    s025_uniform_median_ii: 1.0435\n    s025_oracle_median_ii: 0.856\n    s025_oracle_recovery_pct: 18\n    s025_oracle_recovery_ci:\n    - -39\n    - 45.8\n    s025_oracle_wilcoxon_p: 0.0021\n    s025_heuristic_median_ii: 0.7127\n    s025_heuristic_recovery_pct: 31.7\n    s025_heuristic_recovery_ci:\n    - -22.8\n    - 66\n    s025_heuristic_wilcoxon_p: 0.0236\n    gate_criterion: oracle_recovery > 30%\n    gate_result: FAIL\n    s030_status: not_completed\n    n_problems: 30\n- exp_id: c2_qw_n500_r3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_problems: 500\n    effective_n: 475\n    filter: low+high valid only (mid-null allowed)\n    mid_null_rate: 0.452\n    imp_s015_median_ii: 0.0659\n    imp_s015_ci:\n    - 0.0492\n    - 0.0925\n    imp_s015_wilcoxon_p: 8.66e-15\n    imp_s015_bonf_p: 3.46e-14\n    imp_s020_median_ii: 0.3073\n    imp_s020_ci:\n    - 0.2612\n    - 0.3564\n    imp_s020_wilcoxon_p: 6.84e-42\n    imp_s020_bonf_p: 2.74e-41\n    imp_s025_median_ii: 1.0745\n    imp_s025_ci:\n    - 0.9766\n    - 1.1787\n    imp_s025_wilcoxon_p: 1.06e-68\n    imp_s025_bonf_p: 4.25e-68\n    imp_s030_median_ii: 3.155\n    imp_s030_ci:\n    - 2.7834\n    - 3.5582\n    imp_s030_wilcoxon_p: 9.21e-74\n    imp_s030_bonf_p: 3.69e-73\n    rand_s015_median_ii: -0.0111\n    rand_s015_wilcoxon_p: 0.172\n    rand_s015_bonf_p: 0.687\n    rand_s020_median_ii: 0.0153\n    rand_s020_wilcoxon_p: 0.2\n    rand_s020_bonf_p: 0.8\n    rand_s025_median_ii: 0.3931\n    rand_s025_wilcoxon_p: 1.59e-11\n    rand_s025_bonf_p: 6.37e-11\n    rand_s025_fdr_p: 2.63e-11\n    rand_s030_median_ii: 0.9127\n    rand_s030_wilcoxon_p: 2.92e-15\n    rand_s030_bonf_p: 1.17e-14\n    rand_s030_fdr_p: 5.61e-15\n    dz_s015_s020: -0.629\n    dz_s020_s025: -0.865\n    dz_s025_s030: -0.767\n    dz_s015_s030: -0.923\n    all_dz_reliable: true\n    dose_response_monotonic: true\n    dose_response_spearman_rho: 1\n    dose_response_perm_p: 0.0417\n    imp_rand_ratio_range: 2.7-20.1x\n    bonferroni_k: 4\n    bonferroni_note: Bonferroni k=4 family-wise (D066 revision)\n- exp_id: sf5_asymmetric_spot\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    config_a_h02_kv03:\n      II_low: 19.51\n      II_mid: 6.05\n      II_high: 0.38\n      D: 19.13\n    config_b_h03_kv02:\n      II_low: 18.77\n      II_mid: 3.97\n      II_high: 0.52\n      D: 18.25\n    pre_registered_criterion_passed: true\n    gradient_direction: II_low >> II_mid >> II_high (consistent with symmetric baseline)\n- exp_id: gsm8k_profiling_ds\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    version: v3_median\n    n_problems: 50\n    method: median + Wilcoxon + bootstrap_median(B=10000)\n    importance:\n      s015:\n        median_gradient: 0.241\n        ci_low: 0.077\n        ci_high: 0.478\n        wilcoxon_p: 0.0003\n      s020:\n        median_gradient: 0.74\n        ci_low: 0.314\n        ci_high: 1.119\n        wilcoxon_p: 0.0001\n      s025:\n        median_gradient: 1.992\n        ci_low: 0.933\n        ci_high: 2.82\n        wilcoxon_p: 0.0001\n      s030:\n        median_gradient: 4.682\n        ci_low: 2.121\n        ci_high: 10.557\n        wilcoxon_p: 0.0001\n    imp_rand_ratio:\n      s015: 2.3\n      s020: 2.5\n      s025: 3.8\n      s030: 2.8\n    dose_response_monotonic: true\n- exp_id: gsm8k_profiling_qw\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    version: v3_median\n    n_problems: 50\n    method: median + Wilcoxon + bootstrap_median(B=10000)\n    importance:\n      s015:\n        median_gradient: 0.039\n      s020:\n        median_gradient: 0.158\n      s025:\n        median_gradient: 1.1\n      s030:\n        median_gradient: 2.092\n    qw_rand_s030: INVALID\n- exp_id: think_phase_validation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    effective_n: 48\n    skipped_problems: 2\n    median_kappa: 0.887\n    thinking_in_low_sparsity_phase: 0.578\n    answer_in_high_sparsity_phase: 0.627\n    note: Phase segmentation based on dense model — 4 sparsity conditions share identical\n      phase boundaries, effective sample n=48 not n=192\n- exp_id: r9c2-spike\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: r9c2-spike-v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: r9c2-spike-v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: c2_accuracy_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_problems: 50\n    ds_dense_acc: 0.52\n    ds_s015_acc: 0.36\n    ds_s015_delta: -0.16\n    ds_s030_acc: 0.1\n    ds_s030_delta: -0.42\n    qw_dense_acc: 0.32\n    qw_s015_acc: 0.34\n    qw_s015_delta: 0.02\n    qw_s030_acc: 0.14\n    qw_s030_delta: -0.18\n    ds_s030_chinese_reasoning_rate: 0.4\n    ds_dense_truncation_rate: 0.56\n    note: v2 rescored with fixed radical+degree matcher. DS s015 34→36, QW s015 32→34\n- exp_id: acc_ds_s020\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ds_s020_acc: 0.26\n    ds_s020_acc_v2: 0.26\n    ds_s020_correct: 13\n    ds_s020_total: 50\n    ds_s020_delta_vs_dense: -0.26\n    output_truncated_count: 32\n    output_truncated_rate: 0.64\n    extraction_failure_count: 31\n    extraction_failure_rate: 0.62\n    total_time_s: 1560\n    note: v2 rescored with fixed radical+degree matcher; 0 changes. Dense baseline=0.52\n- exp_id: acc_ds_s025\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy: 0.08\n    correct: 4\n    total: 50\n    null_count: 37\n    null_rate: 0.74\n    output_truncated_count: 38\n    output_truncated_rate: 0.76\n    wrong_count: 9\n    wrong_rate: 0.18\n    extraction_failure_count: 1\n    extraction_failure_rate: 0.02\n    total_time_s: 1670.5\n    heads_pruned: 196\n    delta_vs_dense: -0.44\n- exp_id: acc_qw_s020\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    qw_s020_acc: 0.26\n    qw_s020_correct: 13\n    qw_s020_total: 50\n    qw_s020_delta_vs_dense: -0.06\n    null_count: 2\n    null_rate: 0.04\n    output_truncated_count: 2\n    output_truncated_rate: 0.04\n    extraction_failure_count: 0\n    extraction_failure_rate: 0\n    wrong_count: 35\n    wrong_rate: 0.7\n    heads_pruned: 140\n    total_time_s: 598\n    note: v2 rescored with fixed radical+degree matcher\n- exp_id: acc_qw_s025\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    qw_s025_acc: 0.32\n    qw_s025_correct: 16\n    qw_s025_total: 50\n    qw_s025_delta_vs_dense: 0\n    null_count: 8\n    null_rate: 0.16\n    output_truncated_count: 2\n    output_truncated_rate: 0.04\n    extraction_failure_count: 6\n    extraction_failure_rate: 0.12\n    wrong_count: 26\n    wrong_rate: 0.52\n    heads_pruned: 196\n    total_time_s: 559\n    note: v2 rescored with fixed radical+degree matcher; 3 problems flipped (sqrt+degree)\n- exp_id: acc_qw_s020_n100\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    batch1_acc: 0.26\n    batch1_correct: 13\n    batch1_total: 50\n    batch1_source: acc_qw_s020_b1_8k (v2, 8k tokens)\n    batch2_acc: 0.46\n    batch2_correct: 23\n    batch2_total: 50\n    combined_acc: 0.36\n    combined_correct: 36\n    combined_total: 100\n    note: 'batch effect: batch1=26% vs batch2=46%, Δ=20pp'\n- exp_id: acc_qw_s025_n100\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    batch1_acc: 0.32\n    batch1_correct: 16\n    batch1_total: 50\n    batch1_source: acc_qw_s025_b1_8k (v2, 8k tokens)\n    batch2_acc: 0.34\n    batch2_correct: 17\n    batch2_total: 50\n    combined_acc: 0.33\n    combined_correct: 33\n    combined_total: 100\n- exp_id: acc_ds_dense_8k\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: acc_ds_s015_8k\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: acc_ds_s020_8k\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: acc_ds_s025_8k\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: acc_ds_s030_8k\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: acc_qw_dense_n100\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    batch1_correct: 22\n    batch1_total: 50\n    batch1_acc: 0.44\n    batch1_source: acc_qw_dense_b1_8k (v2, 8k tokens)\n    batch2_correct: 24\n    batch2_total: 50\n    batch2_acc: 0.48\n    combined_correct: 46\n    combined_total: 100\n    combined_acc: 0.46\n- exp_id: acc_qw_s015_n100\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    batch1_acc: 0.46\n    batch1_correct: 23\n    batch1_total: 50\n    batch1_source: acc_qw_s015_b1_8k (v2, 8k tokens)\n    batch2_acc: 0.38\n    batch2_correct: 19\n    batch2_total: 50\n    combined_acc: 0.42\n    combined_correct: 42\n    combined_total: 100\n- exp_id: acc_qw_s030_n100\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    batch1_correct: 7\n    batch1_total: 50\n    batch1_acc: 0.14\n    batch1_source: acc_qw_s030_b1_8k (v2, 8k tokens)\n    batch2_correct: 12\n    batch2_total: 50\n    batch2_acc: 0.24\n    combined_correct: 19\n    combined_total: 100\n    combined_acc: 0.19\n- exp_id: acc_ds_s015_8k_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.48\n    correct: 24\n    total: 50\n    truncation_rate: 0.32\n    truncated_count: 16\n    non_truncated_accuracy: 0.706\n    non_truncated_correct: 24\n    non_truncated_total: 34\n    wall_time_s: 3967\n    max_new_tokens: 8192\n- exp_id: acc_ds_s020_8k_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.3\n    correct: 15\n    total: 50\n    truncated_count: 28\n    truncated_rate: 0.56\n    extraction_failures: 1\n    non_truncated_accuracy: 0.682\n    non_truncated_correct: 15\n    non_truncated_total: 22\n    total_time_seconds: 5549\n    max_new_tokens: 8192\n- exp_id: acc_ds_s025_8k_v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy: 0.08\n    correct: 4\n    total: 50\n    truncated_count: 38\n    truncated_rate: 0.76\n    avg_tokens: 6343.8\n    max_new_tokens: 8192\n    total_time_seconds: 6827.8\n    null_count: 36\n- exp_id: acc_ds_s030_8k_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.04\n    correct: 2\n    total: 50\n    truncation_rate: 0.76\n    truncated_count: 38\n    extraction_failures: 3\n    non_truncated_accuracy: 0.167\n    non_truncated_correct: 2\n    non_truncated_total: 12\n    max_new_tokens: 8192\n    avg_tokens: 6566.3\n    total_time_seconds: 7095.1\n- exp_id: gsm8k_qw_rand_s025\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: gsm8k_qw_rand_s030\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: acc_qw_s020_n100_b2_fix\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    batch2_correct: 23\n    batch2_total: 50\n    batch2_acc: 0.46\n    batch1_correct_v2: 13\n    batch1_total: 50\n    batch1_acc_v2: 0.26\n    combined_correct: 36\n    combined_total: 100\n    combined_acc: 0.36\n    null_count: 2\n    truncated_count: 1\n    total_time_seconds: 884.3\n    max_new_tokens: 8192\n    original_batch2_correct: 22\n    original_batch2_acc: 0.44\n    delta_vs_original: +1 correct (+0.02 acc)\n- exp_id: acc_qw_s025_n100_b2_fix\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.34\n    correct: 17\n    n_problems: 50\n    truncation_rate: 0.06\n    truncated_count: 3\n    avg_tokens: 1044\n    max_new_tokens: 8192\n    total_time_seconds: 1099\n    batch: b2 (problems 51-100)\n    merged_n100_accuracy: 0.33\n    merged_n100_correct: 33\n    merged_n100_note: batch1 used max_new_tokens=2048, batch2_fix used 8192 — mismatch\n- exp_id: acc_ds_dense_8k_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.74\n    correct: 37\n    n_problems: 50\n    truncation_rate: 0.16\n    truncated_count: 8\n    avg_tokens: 3126\n    max_new_tokens: 8192\n    total_time_seconds: 2882\n- exp_id: gsm8k_qw_rand_s025_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    verdict: PASS\n    n_problems: 50\n    n_bootstrap: 1000\n    seed: 42\n    high_sparsity:\n      n_segments: 216\n      n_tokens: 9326\n      ppl_dense: 1.0695\n      ppl_attn: 5.9362\n      ppl_kv: 3.4316\n      ppl_both: 15.7484\n      ii_mean: 6.5954\n      ii_ci:\n      - 1.1114\n      - 11.3791\n      ii_median: 0.7176\n      ii_median_ci:\n      - 0.5959\n      - 0.9347\n      winsorized_mean: 6.5046\n      skewness: -4.6807\n      outlier_count: 3\n    low_sparsity:\n      n_segments: 252\n      n_tokens: 29224\n      ppl_dense: 1.1972\n      ppl_attn: 11.5347\n      ppl_kv: 5.6038\n      ppl_both: 21.6874\n      ii_mean: 2.3883\n      ii_ci:\n      - -8.4602\n      - 11.029\n      ii_median: 1.4587\n      ii_median_ci:\n      - 1.1121\n      - 2.0451\n      winsorized_mean: 5.8911\n      skewness: -7.6074\n      outlier_count: 4\n    mid_sparsity:\n      n_segments: 51\n      n_tokens: 5954\n      ppl_dense: 1.2601\n      ppl_attn: 13.4132\n      ppl_kv: 6.4841\n      ppl_both: 20.8714\n      ii_mean: 4.5407\n      ii_ci:\n      - -4.8854\n      - 12.4605\n      ii_median: 1.1272\n      ii_median_ci:\n      - 0.637\n      - 3.3729\n      winsorized_mean: 6.3284\n      skewness: -3.4048\n      outlier_count: 1\n- exp_id: gsm8k_qw_rand_s030_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    verdict: PASS\n    n_problems: 50\n    n_bootstrap: 1000\n    seed: 42\n    high_sparsity:\n      n_segments: 216\n      n_tokens: 9326\n      null_ratio: 2/50\n      ppl_dense: 1.0695\n      ppl_attn: 6.5613\n      ppl_kv: 4.481\n      ppl_both: 23.7486\n      ii_mean: 11.83\n      ii_median: 2.31\n      ii_ci:\n      - 6.17\n      - 17.04\n      ii_median_ci:\n      - 1.64\n      - 2.81\n      winsorized_mean: 10.55\n      skewness: -2.29\n      outlier_count: 7\n    low_sparsity:\n      n_segments: 252\n      n_tokens: 29224\n      null_ratio: 5/50\n      ppl_dense: 1.1972\n      ppl_attn: 6.3283\n      ppl_kv: 8.5374\n      ppl_both: 56.2304\n      ii_mean: 31.26\n      ii_median: 5.2\n      ii_ci:\n      - 17.84\n      - 47.86\n      ii_median_ci:\n      - 3.95\n      - 7.24\n      winsorized_mean: 16.35\n      skewness: 7.57\n      outlier_count: 4\n    mid_sparsity:\n      n_segments: 51\n      n_tokens: 5954\n      null_ratio: 17/50\n      ppl_dense: 1.2601\n      ppl_attn: 18.6162\n      ppl_kv: 11.6625\n      ppl_both: 47.9019\n      ii_mean: 18.02\n      ii_median: 2.7\n      ii_ci:\n      - 0.09\n      - 36.69\n      ii_median_ci:\n      - 1.46\n      - 8.77\n      winsorized_mean: 18.22\n      skewness: 0.43\n      outlier_count: 2\n- exp_id: acc_qw_dense_b1_8k\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.44\n    correct: 22\n    n_problems: 50\n    truncation_rate: 0.02\n    truncated_count: 1\n    avg_tokens: 759.7\n    max_tokens_generated: 8192\n    max_new_tokens: 8192\n    total_time_seconds: 681.8\n    null_count: 0\n    batch: b1_v2 (problems 1-50, 8k tokens)\n    old_batch1_acc: 0.32\n    old_batch1_correct: 16\n    new_combined_n100_acc: 0.46\n    new_combined_n100_correct: 46\n    batch2_acc: 0.48\n    batch2_correct: 24\n- exp_id: acc_qw_s015_b1_8k\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.46\n    correct: 23\n    total: 50\n    truncation_rate_8k: 0.02\n    gen_over_2k: 3\n    gen_over_2k_all_wrong: true\n    max_gen_length: 8192\n    mean_gen_length: 776\n    batch: b1_v2 (problems 1-50, 8k tokens)\n    batch2_acc: 0.38\n    batch2_correct: 19\n    new_combined_n100_acc: 0.42\n    new_combined_n100_correct: 42\n    batch2_source: acc_qw_s015_n100\n- exp_id: acc_qw_s020_b1_8k\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.26\n    correct: 13\n    n_problems: 50\n    truncation_rate: 0.02\n    truncated_count: 1\n    avg_tokens: 722.1\n    max_tokens_generated: 8192\n    max_new_tokens: 8192\n    total_time_seconds: 729.1\n    null_count: 0\n    batch: b1_v2 (problems 1-50, 8k tokens)\n    old_batch1_acc: 0.26\n    old_batch1_correct: 13\n    new_combined_n100_acc: 0.36\n    new_combined_n100_correct: 36\n    batch2_acc: 0.46\n    batch2_correct: 23\n- exp_id: acc_qw_s025_b1_8k\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy: 0.32\n    correct: 16\n    n_problems: 50\n    truncation_rate: 0.04\n    truncated_count: 2\n    extraction_failures: 6\n    avg_tokens: 797.3\n    total_time_seconds: 831.6\n    batch: b1_v2 (problems 1-50, 8k tokens)\n    batch2_acc: 0.34\n    batch2_correct: 17\n    new_combined_n100_acc: 0.33\n    new_combined_n100_correct: 33\n    batch2_source: acc_qw_s025_n100_b2_fix\n- exp_id: acc_qw_s030_b1_8k\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy: 0.14\n    correct: 7\n    total: 50\n    truncation_rate: 0.04\n    truncated_count: 2\n    extraction_failures: 8\n    max_new_tokens: 8192\n    total_time_seconds: 886.7\n    batch: b1_v2 (problems 1-50, 8k tokens)\n    old_batch1_acc: 0.14\n    old_batch1_correct: 7\n    batch2_acc: 0.24\n    batch2_correct: 12\n    new_combined_n100_acc: 0.19\n    new_combined_n100_correct: 19\n- exp_id: c8_llama_n250\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    first_run_failed: true\n    failure_reason: 'bash wrapper wait logic bug: subprocess OOM/error exits silently,\n      script marks DONE without output validation. All 8 output dirs empty.'\n    fix_worker: worker_code_c8_llama_n250_fix_20260516T031229\n    fix_plan: 1) diagnose script + OOM, 2) fix exit code + output validation + GPU\n      monitor, 3) dry-run 1 condition on GPU 2, 4) full launch on GPU 2-3 via submit_training_job\n- exp_id: c4_think_validation_math500\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    v2_math500_kappa_adaptive: 0.88\n    v2_math500_ds_problems: 48\n    v2_math500_ds_tokens: 32055\n    v2_math500_thinking_in_low: 0.816\n    v2_math500_answer_in_high: 0.655\n    v2_math500_temporal_ordering_ds: 0.576\n    v2_math500_temporal_ordering_qw: 0.479\n    v2_qw_pct_positive: 0.98\n    v2_scope: MATH-500\n    v2_models: DS+QW\n    v2_status: ALL_CRITERIA_MET\n    v1_kappa_adaptive: 0.8804\n    v1_auc: 0.9808\n    SCOPE_FLAG: v2_validated_on_MATH500\n- exp_id: c5_per_phase_gini\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    qw_complete: true\n    ds_complete: true\n    n_problems: 30\n    qw_dense_gini_baselines:\n      low: 0.2675\n      mid: 0.2078\n      high: 0.2599\n    qw_importance:\n      s015:\n        global_delta: -0.0103\n        low_delta: -0.0165\n        mid_delta: -0.0094\n        high_delta: -0.012\n      s020:\n        global_delta: -0.0121\n        low_delta: -0.02\n        mid_delta: -0.0115\n        high_delta: -0.0143\n      s025:\n        global_delta: -0.01\n        low_delta: -0.0286\n        mid_delta: -0.0168\n        high_delta: -0.0207\n      s030:\n        global_delta: -0.0202\n        low_delta: -0.035\n        mid_delta: -0.0183\n        high_delta: -0.0239\n    qw_random:\n      s015:\n        global_delta: -0.0186\n        low_delta: -0.0083\n        mid_delta: -0.0038\n        high_delta: -0.0036\n      s020:\n        global_delta: -0.0229\n        low_delta: -0.0119\n        mid_delta: -0.0053\n        high_delta: -0.0067\n      s025:\n        global_delta: -0.0337\n        low_delta: -0.0014\n        mid_delta: -0.0081\n        high_delta: 0.0045\n      s030:\n        global_delta: -0.0447\n        low_delta: -0.0221\n        mid_delta: -0.0077\n        high_delta: -0.0061\n    ds_importance:\n      s015:\n        global_delta: -0.0301\n        low_delta: -0.0163\n        mid_delta: -0.0073\n        high_delta: -0.0152\n      s020:\n        global_delta: -0.0404\n        low_delta: -0.0209\n        mid_delta: -0.0092\n        high_delta: -0.02\n      s025:\n        global_delta: -0.0647\n        low_delta: -0.0313\n        mid_delta: -0.0133\n        high_delta: -0.0267\n      s030:\n        global_delta: -0.0806\n        low_delta: -0.0373\n        mid_delta: -0.0183\n        high_delta: -0.0314\n    ds_random:\n      s015:\n        global_delta: -0.0309\n        low_delta: -0.0102\n        mid_delta: -0.0006\n        high_delta: -0.0062\n      s020:\n        global_delta: -0.0403\n        low_delta: -0.012\n        mid_delta: -0.0007\n        high_delta: -0.0085\n      s025:\n        global_delta: -0.062\n        low_delta: -0.015\n        mid_delta: -0.0096\n        high_delta: -0.0112\n      s030:\n        global_delta: -0.0732\n        low_delta: -0.0183\n        mid_delta: -0.0093\n        high_delta: -0.0138\n    key_finding: 'Both models: importance pruning low-phase Gini delta consistently\n      largest and monotonically increases with sparsity (DS: -0.016 to -0.037; QW:\n      -0.017 to -0.035). Random pruning shows weaker per-phase structure. Supports\n      discrimination collapse hypothesis.'\n- exp_id: c9_gsm8k_power_analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    min_detectable_d_n50: 0.4042\n    random_conditions_all_NS: true\n    random_max_abs_d: 0.164\n    random_conditions:\n      ds_rand_s015_d: -0.017\n      ds_rand_s015_power: 0.052\n      ds_rand_s020_d: -0.063\n      ds_rand_s020_power: 0.072\n      ds_rand_s025_d: 0.026\n      ds_rand_s025_power: 0.054\n      ds_rand_s030_d: 0.058\n      ds_rand_s030_power: 0.069\n      qw_rand_s015_d: -0.154\n      qw_rand_s015_power: 0.187\n      qw_rand_s020_d: 0.113\n      qw_rand_s020_power: 0.123\n      qw_rand_s025_d: 0.163\n      qw_rand_s025_power: 0.203\n      qw_rand_s030_d: 0.165\n      qw_rand_s030_power: 0.207\n    qw_importance_adequately_powered:\n      s025_d: 0.62\n      s025_power: 0.99\n      s030_d: 0.64\n      s030_power: 0.99\n    REVIEWER_WARNING: t-test Cohen's d power analysis ONLY valid for random conditions.\n      Importance conditions have heavy-tail distributions where t-test severely misestimates\n      (e.g. DS s030 d=0.008 but Wilcoxon p=0.0001). DO NOT cite importance t-test\n      power in paper.\n    paper_citable_conclusions:\n    - 'Random: all 8 conditions NS (max|d|=0.164), n=50 detects d>=0.40 → absence\n      of evidence not evidence of absence'\n    - QW importance s025/s030 adequately powered (d≈0.63, power>0.99)\n- exp_id: c10_lang_switching\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    method: CPU analysis of existing gen_snippet data (3/5 sparsities)\n    coverage: dense, s015, s030 (s020/s025 missing gen_snippet)\n    n_per_sparsity: 50\n    dense:\n      switch_rate: 0\n      cn_count: 0\n      en_count: 50\n      cn_acc: null\n      en_acc: 0.52\n    s015:\n      switch_rate: 0.04\n      cn_count: 2\n      en_count: 48\n      cn_acc: 0\n      en_acc: 0.375\n    s030:\n      switch_rate: 0.4\n      cn_count: 20\n      en_count: 30\n      cn_acc: 0.1\n      en_acc: 0.1\n    trend: 'Monotonically increasing: 0% → 4% → 40%. Chinese responses have much lower\n      accuracy (10% at s030 vs 52% dense English).'\n    checkpoint_path: /root/autodl-tmp/pacs/results_c10_lang_cpu.json\n- exp_id: c8_llama_n250_fixed\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: c10-lang-s020-s025\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: c10_lang_s020_s025\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    s020:\n      n: 50\n      accuracy: 0.26\n      switch_rate: 0.14\n      switch_count: 7\n      mean_cn_ratio: 0.066\n      cn_acc: 0.333\n      en_acc: 0.25\n    s025:\n      n: 50\n      accuracy: 0.1\n      switch_rate: 0.32\n      switch_count: 16\n      mean_cn_ratio: 0.152\n      cn_acc: 0.2\n      en_acc: 0.057\n    wall_time_s: 11680.6\n    output_path: /root/autodl-tmp/pacs/results_c10_lang_s020_s025.json\n- exp_id: c8_llama_gpu0_s025\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_problems: 250\n    n_bootstrap: 1000\n    segmentation: quantile\n    per_phase_ii_median:\n      high: 0.0171\n      mid: 0.1916\n      low: 0.388\n    per_phase_ii_mean:\n      high: 0.0218\n      mid: 0.2126\n      low: 0.4713\n    phase_gradient_median_diff: 0.3761\n    phase_gradient_median_diff_ci95:\n    - 0.3147\n    - 0.4039\n    wilcoxon_p_one_sided: 4.3e-39\n    bonferroni_p_k4: 1.72e-38\n    cohens_dz: 1.1174\n    rank_biserial_r: 0.8689\n    n_paired: 244\n    pos_neg_ratio: 228/16\n- exp_id: gpqa_ds_importance_s015\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-16T15:20:28.073Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T15:20:28.073Z",
  "sessionId": "a3d601b9-90d6-4700-8195-7ac8fe55805b"
}
```

---

## Round 1

38 recorded events

### User

_source line 3 · 2026-05-16T15:20:28.103Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：LLaMA n=250 高功效确认 strategy×phase 交互在 Llama 架构上可忽略；random phase gradient 稳健。GPQA 不显著或方向不一致。'Strategy-gated' 叙事崩塌——phase modulation 普遍存在但非 strategy-specific。
核心假设：['LLaMA imp_vs_rand d_z 在 n=250 仍 <0.25——高功效零结果确认交互是 Qwen2 特异', 'LLaMA random phase gradient d_z≥0.35 被确认——compound severity 的 phase modulation 与 eviction strategy 无关（在 Llama 上）', 'GPQA phase gradient NS 或方向不一致——跨 task 泛化失败', 'Strategy-specificity 限于 Qwen2ForCausalLM 架构，非普遍性质']
关键指标范围：{'llama_n250_imp_vs_rand_dz_s030': [0.08, 0.25], 'llama_n250_imp_vs_rand_dz_s025': [0.05, 0.18], 'llama_n250_bonferroni_sig_count_out_of_4': [0, 1], 'llama_n250_random_phase_gradient_dz': [0.35, 0.55], 'llama_n250_importance_phase_gradient_dz': [0.95, 1.2], 'gpqa_ds_s015_median_diff': [-0.05, 0.1], 'gpqa_bonferroni_p': [0.05, 1.0], 'gpqa_imp_rand_ratio': [0.5, 2.0]}
叙事方向：完全 reframe。Title 改为 "Phase-Dependent Compound Sparsity Severity in Reasoning LLMs"（去掉 strategy-gated）。Core finding 收窄：compound sparsity severity 是 phase-modulated 的涌现属性，importance phase gradient 跨三模型两架构 一致（d_z≈1.0-1.2），但 strategy×phase 交互仅 Qwen2 架构显著，Llama 上 random 也产生 comparable phase gradient（d_z 0.35-0.55）。 论文重组为三层递进：(1) Phase gradient universality（核心贡献，跨模型/架构稳健）， (2) Strategy modulation 的 architecture-dependence（secondary finding， Qwen2 confirmed / Llama NS → 开放问题）， (3) Discrimination collapse 机制（Gini/CV 跨模型一致，作为 phase gradient 的 解释而非 strategy-specificity 的解释）。Scope 限于 MATH-500 + GSM8K（GPQA 仅 放 appendix 或不纳入）。EMNLP main 仍可冲——pitch 改为 "first systematic quantitative characterization of phase-dependent compound sparsity"， 强调：(a) dose-response monotonicity（ρ=1.0, n=500 两模型）, (b) sparsity threshold discovery（~s020-s025）, (c) discrimination collapse 机制。 Novelty 论证需加强 methodology 贡献（per-problem paired II metric + phase segmentation framework）。需重写 §1-§3，将 strategy 从核心 claim 降级到 architecture-dependent 观察。Limitations 增加一段 strategy-specificity 的 scope boundary。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: phase-gated-compound-sparse
venue: EMNLP 2026
focus: 重点评估：(1) cross-architecture generalization 从 n=49 升级到 n=250 后是否足够支撑 claim，量级差 25× 如何在论文中定位；(2) GPQA cross-task 扩展对 scope 短板的修复力度；(3) 当前 framing 作为正会投稿的竞争力，novelty 是否站得住

## paper_framing.md

# Paper Framing — Phase-Gated Compound Sparsity

> 最后更新: 2026-05-16 (数值对齐 n=500 registry: DS median_diff 0.39/1.21/3.99/8.48; QW 0.07/0.31/1.07/3.16; Cohen's d registry 0.61→1.13/0.37→1.44; C7+C10 status→confirmed; imp/rand 2.7-15×) | 维护者: Director

## Core Insight

Compound sparsity（attention head pruning + KV cache eviction）的 severity 不是固定常数——它是 eviction strategy 和 reasoning phase 交互的涌现属性。Importance-based eviction 的 compound interaction severity（paired median difference: median(II_low_i − II_high_i)）随 sparsity 单调递增（DeepSeek: 0.39→1.21→3.99→8.48; Qwen: 0.07→0.31→1.07→3.16），而 random masking 在 s015/s020 NS，在 s025 跨模型显著但效应量远小于 importance（DS: 0.257 vs 3.986; QW: 0.393 vs 1.074, 2.7-15×差异），存在 sparsity threshold ~s020-s025（D063; s030 待定）。Cohen's d（per-problem paired, B=10000）从 medium 到 large（DeepSeek: 0.61→1.13; Qwen: 0.37→1.44，registry cohens_d s015→s030）。LLaMA 跨架构验证（D060）qualitative direction consistent（within-importance d_z~1.0），但 strategy×phase 交互弱于 Qwen2 架构（imp_vs_rand d_z 0.19→0.34, 仅 s030 显著），且 random 在 LLaMA 上也显示显著 phase gradient（d_z 0.35→0.44），与 DeepSeek/Qwen random 低 sparsity NS 模式定性不同。GSM8K 跨 benchmark 验证（D075）：importance masking 的 phase gradient 在 GSM8K 上同样单调递增（QW: 0.039→0.158→1.100→2.092; DS: 0.241→0.740→1.992→4.682），但 strategy specificity（importance/random gradient ratio）从 MATH-500 的 15-36× 衰减至 GSM8K 的 2.3-3.8×。注意："反转"仅在原始 II_low 值上（random > importance），phase gradient 层面 importance ≥ random。Strategy specificity 的 task-dependence 机制是开放问题（见 §6 Discussion）。这一发现挑战了 compound degradation 均匀分布的隐含假设。

**数字基准**：所有数字基于 bf16 per-problem paired 统计量（B=10000 bootstrap）。median_diff 定义为 median(II_low_i − II_high_i)（逐 problem 配对差的中位数）。fp16 旧数据已弃用。

## Narrative Arc

Compound sparsity 是高效 LLM 推理的实用部署需求，但 prior work（SparK, Ada-KV, SLiM）将 compound interaction 视为均匀超可加。我们发现 severity 是 strategy × phase 交互的涌现属性：importance eviction 的 compound interaction 在 low-sparsity phase 远大于 high-sparsity phase（paired median difference 单调递增 0.39→8.48），而 random eviction 在低 sparsity (s015/s020) NS，在 s025+ 跨模型显著但效应量远小于 importance (2.7-15×)——存在 sparsity threshold (~s020-s025)，低于阈值 compound effect importance-specific，高于阈值两者均触发但 importance 主导。Cross-model replication 方向一致（Qwen magnitude ~1/4 of DeepSeek，onset threshold s≥0.20）。LLaMA 跨架构验证已完成（c3_llama, D060）：qualitative direction consistent（importance phase gradient d_z≈1.0），但 imp_vs_rand 交互弱（d_z 0.19→0.34, 仅 s030 显著），且 random 也显示非平凡 phase gradient（d_z 0.35→0.44），strategy-dependence 强度 architecture-dependent。我们通过 discrimination collapse 机制解释这一现象：head pruning → importance score 的判别力崩塌（Gini/CV 下降跨模型一致）→ importance eviction 退化为有偏伪随机。Attention entropy redistribution 作为 model-dependent secondary effect 在 DeepSeek 上观察到，但在 Qwen 上不稳健（D044）。

**Framing 硬约束（D015）**：
- MUST: \\\"emergent phase-strategy interaction\\\"
- MUST NOT: \\\"importance metric limitation / importance is broken\\\"
- MUST NOT: claim \\\"importance masking produces super-additive interaction\\\" without qualifier — random masking also produces positive II, and at s025+ random is statistically significant (D063). The distinguishing signal is **magnitude gradient** (importance 2.7-15× larger) and **onset threshold** (random NS below ~s020, importance significant from s015+), not the existence of super-additivity itself (D023)

## Core Claims

| ID | Claim | Status | Key Evidence |
|----|-------|--------|-------------|
| C1 | Compound sparsity severity is strategy- and task-modulated | confirmed | MATH-500: importance gradient 15-36× random; GSM8K: ratio 衰减至 2.3-3.8× (D075)。Phase gradient 层面 importance ≥ random 跨 benchmark 成立，但 magnitude ratio task-dependent。Threshold ~s020-s025 (D063) |
| C2 | Severity is phase-modulated (amplified in low-sparsity phase) | confirmed | bf16 paired median difference 单调递增: 0.39→1.21→3.99→8.48; Bonferroni p<0.005 全 4 水平 (D032)。预注册：n=500 后若 QW s015 CI 仍跨零，叙事改为 'compound effect emerges above threshold sparsity (~s020)' |
| C3 | Phase-strategy crossover exists | confirmed | s=0.25: importance high_phase=0.032 < random=0.818, importance low_phase=7.196 > random=1.363 (bf16) |
| C4 | Discrimination collapse as primary mechanism; entropy redistribution model-dependent | partially_confirmed | D044: Gini/CV 下降跨模型一致; entropy collapse DeepSeek 一致但 Qwen s025 反转(+0.045) s030≈0。30/30 problems completed. |
| C5 | Phase-modulated compound severity generalizes across models | confirmed | DeepSeek + Qwen cross-model replication: 方向一致, Cohen's d ρ=1.0, gradient permutation p=0.043. Qwen magnitude ~1/4 of DeepSeek, onset threshold s≥0.20 (S3→C). |
| C5b | Phase-aware mitigation recovers compound degradation | future_work | D056: pilot 完成 gate_failed。Oracle recovery 18% < 30% gate (Wilcoxon p=0.002)，heuristic 32% 但 CI 跨零。方向正确但效应量不足，需更精细 phase boundary estimation → future work |
| C6 | Severity gradient is sub-exponential | confirmed | Growth rate decreasing: Δ增长因子 3.8×→4.8×→2.0×（递减） |
| C7 | Statistical power at n=500 confirms dose-response | confirmed | c2_n500_deepseek (success) + c2_qw_n500_r3 (success): 两模型 n=500 全 4 sparsity Bonferroni p<0.005, Spearman ρ=1.0 |
| C8 | Cross-architecture validation (LLaMA) | partially_confirmed | D060: within-importance phase gradient 强(d_z~1.0) ✓，但 imp_vs_rand 交互弱(d_z 0.19→0.34, 仅 s030 Bonferroni p=0.029 显著)。**关键**：random 在 LLaMA 上也显示显著 phase gradient(d_z 0.35→0.44, CI 排除零)，与 DeepSeek/Qwen random 低 sparsity NS 模式定性不同。Qualitative direction consistent, quantitative strategy×phase interaction weaker + architecture-dependent。论文禁用 "confirms"，改用 "suggests"/"provides partial support"。 |
| C9 | Differentiation from Lethe/SparK prior work | planned | Related Work §2 引用区分 + SparK gap analysis |
| S3→C | Onset threshold is model-dependent (DeepSeek s≥0.15, Qwen s≥0.20) | confirmed | D037/D038: Qwen s015 d_z=0.37 CI含0, s020+ 显著 |
| C10 | Phase gradient cross-benchmark robust; strategy specificity task-modulated | confirmed | GSM8K DS gradient 0.241→4.682 单调递增; QW gradient 0.039→2.092; imp/rand ratio 衰减至 2.3-3.8× (D075)。QW random s025+s030 均 success |
| S7→C | Dose-response monotonicity (Spearman ρ=1.0) | confirmed | D047: 6-point dose-response, 单调递增 |

## Anticipated Reviewer Concerns

### RC1: Generalizability — 7B models only, benchmark scope
- **预期质疑**: \"Results on two 7B models and MATH-500 only. How do we know this generalizes to larger models or other reasoning tasks?\"
- **应对**: 四层泛化证据：(1) Cross-model: DeepSeek-R1-Distill-Qwen-7B + Qwen2.5-7B-Instruct（同架构不同训练，ρ=1.0）(2) Cross-architecture: c3_llama (DeepSeek-R1-Distill-Llama-8B, LlamaForCausalLM)，qualitative direction consistent，但需加限定——LLaMA 上 random 也显示 phase gradient，strategy × phase 交互弱于 Qwen2 架构（D060）(3) **Cross-benchmark (D075)**: GSM8K（两模型）phase gradient 单调递增复现（DS: 0.241→4.682; QW: 0.039→2.092），但 strategy specificity ratio 从 MATH-500 15-36× 衰减至 2.3-3.8×，表明 phase modulation 跨 benchmark 稳健而 magnitude modulation task-dependent。Limitations 诚实声明：(a) 7B scale only；(b) strategy specificity 强度 task-dependent（GSM8K 衰减，可能因推理链更短）；(c) LLaMA 跨架构验证 n=50 限制功效；(d) random phase gradient 行为 architecture-dependent。
- **实验支撑**: C5 (cross-model) + C8 (c3_llama cross-architecture) + C10 (cross-benchmark GSM8K, D075)

### RC2: Mechanism — entropy-discrimination collapse 缺乏直接测量
- **预期质疑**: \"The mechanism is conceptual. Where is the empirical evidence for entropy increase and discrimination collapse?\"
- **应对**: c4_entropy 实验已完成（DeepSeek 30/30 + Qwen 30/30）。D044 结论：Gini/CV 下降跨模型一致（discrimination collapse confirmed）；entropy redistribution 在 DeepSeek 上一致但在 Qwen 上 s025 方向反转、s030 近零（model-dependent）。论文以 discrimination collapse 为主线，entropy 作 DeepSeek 特有的强化因素。
- **实验支撑**: c4_entropy (DeepSeek DONE) + qwen_c4_entropy (DONE, negative for entropy universality)

### RC3: Practical impact — 没有 throughput 数据
- **预期质疑**: \"No wall-clock or throughput measurements. Is the severity amplification reflected in actual inference speed?\"
- **应对**: 本文定位是 empirical finding paper（发现 + 机制解释），不是 method paper。Throughput 不是 claim 的一部分。Discussion 中明确 phase-gated controller 作为 future direction。
  - C5b pilot 已完成（D056）：oracle recovery 18%（Wilcoxon p=0.002），heuristic recovery 32%（p=0.024），但两者 95% CI 均跨零。方向正确（Wilcoxon 显著）但效应量不足（未达 30% gate），需更精细的 phase boundary estimation。论文 §6 Discussion 诚实报告 pilot 结果 + future work。
  - Heuristic > oracle 悖论值得提及：token position ratio 粗粒度划分可能恰好更适合 mitigation 场景，暗示 phase boundary 的最优粒度是开放问题。
- **实验支撑**: c5b_pilot (gate_failed, D056)

### RC4: Statistical rigor — bootstrap 是否足够
- **预期质疑**: \"Per-problem bootstrap with 50 problems — sufficient sample size?\"
- **应对**: bf16 使用 B=10000 per-problem paired bootstrap，有效配对数 n=49 (DeepSeek) / n=46 (Qwen)；n=500 实验进一步验证 (C7 running)。Permutation test 使用 paired median difference 作为 robust statistic（D032），Bonferroni 校正后全 4 水平 p<0.005。Dose-response 主用 Wilcoxon signed-rank p + median_diff（robust to outliers），Cohen's d 作为辅助效应量（DeepSeek 0.61→1.13, Qwen 0.37→1.44, registry cohens_d s015→s030），注释高 sparsity 下 d 受 outlier-driven variance 影响（DS s020→s025: median 3.3× jump 但 d 非单调，因极端 II 值影响分母，D064）。可在 appendix 补充 per-problem 分布图（已生成 fig4_per_problem_dist.pdf）。
- **实验支撑**: bf16 permutation test (D032) + Cohen's d per-problem paired (rebootstrap B=10000) + n=500 Wilcoxon (C7 running)

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
4. Cross-model + cross-architecture (LLaMA) replication 验证泛化性（三模型两架构；LLaMA partially_confirmed，strategy×phase 交互强度 architecture-dependent, D060）

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
  status: RUNNING
  conclusion: ''
  metrics: {}
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
  "promptId": "1b3ef117-44ac-4494-a1a3-d617fc268060",
  "type": "user",
  "uuid": "c3c4cf84-f6c5-47df-a724-d8bafb5bfdc6",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "a3d601b9-90d6-4700-8195-7ac8fe55805b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T15:20:28.099Z_

```json
{
  "parentUuid": "c3c4cf84-f6c5-47df-a724-d8bafb5bfdc6",
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
  "uuid": "1c045ae4-4d25-472b-a25d-0399c302f698",
  "timestamp": "2026-05-16T15:20:28.099Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "a3d601b9-90d6-4700-8195-7ac8fe55805b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T15:20:28.099Z_

```json
{
  "parentUuid": "1c045ae4-4d25-472b-a25d-0399c302f698",
  "isSidechain": false,
  "attachment": {
    "type": "agent_listing_delta",
    "addedTypes": [
      "claude",
      "Explore",
      "general-purpose",
      "Plan",
      "statusline-setup"
    ],
    "addedLines": [
      "- claude: Catch-all for any task that doesn't fit a more specific agent. FleetView's default when no agent name is typed. (Tools: *)",
      "- Explore: Fast read-only search agent for locating code. Use it to find files by pattern (eg. \"src/components/**/*.tsx\"), grep for symbols or keywords (eg. \"API endpoints\"), or answer \"where is X defined / which files reference Y.\" Do NOT use it for code review, design-doc auditing, cross-file consistency checks, or open-ended analysis — it reads excerpts rather than whole files and will miss content past its read window. When calling, specify search breadth: \"quick\" for a single targeted lookup, \"medium\" for moderate exploration, or \"very thorough\" to search across multiple locations and naming conventions. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- general-purpose: General-purpose agent for researching complex questions, searching for code, and executing multi-step tasks. When you are searching for a keyword or file and are not confident that you will find the right match in the first few tries use this agent to perform the search for you. (Tools: *)",
      "- Plan: Software architect agent for designing implementation plans. Use this when you need to plan the implementation strategy for a task. Returns step-by-step plans, identifies critical files, and considers architectural trade-offs. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- statusline-setup: Use this agent to configure the user's Claude Code status line setting. (Tools: Read, Edit)"
    ],
    "removedTypes": [],
    "isInitial": true,
    "showConcurrencyNote": true
  },
  "type": "attachment",
  "uuid": "f18442eb-8f4b-4006-88b0-a9c882e6f493",
  "timestamp": "2026-05-16T15:20:28.099Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "a3d601b9-90d6-4700-8195-7ac8fe55805b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-16T15:20:28.099Z_

```json
{
  "parentUuid": "f18442eb-8f4b-4006-88b0-a9c882e6f493",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "7533380e-15f3-4959-b6b6-c0a0d080c12f",
  "timestamp": "2026-05-16T15:20:28.099Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "a3d601b9-90d6-4700-8195-7ac8fe55805b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：LLaMA n=250 高功效确认 strategy×phase 交互在 Llama 架构上可忽略；random phase gradient 稳健。GPQA 不显著或方向不一致。'Strategy-gated' 叙事崩塌——phase modulation 普遍存在但非 strategy-specific…",
  "leafUuid": "7533380e-15f3-4959-b6b6-c0a0d080c12f",
  "sessionId": "a3d601b9-90d6-4700-8195-7ac8fe55805b"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Phase-dependent compound sparsity in reasoning models",
  "sessionId": "a3d601b9-90d6-4700-8195-7ac8fe55805b"
}
```

---

### Assistant

_source line 9 · 2026-05-16T15:20:33.165Z_

I'll analyze the experiment plan and generate detailed predictions for the "worst" tier. Let me first check what experiments are currently planned/running.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7533380e-15f3-4959-b6b6-c0a0d080c12f",
  "isSidechain": false,
  "requestId": "req_011Cb6USsdsCjbp7qXXGa2Vx",
  "type": "assistant",
  "uuid": "a26f3f5f-0cbb-471b-883b-10e1dcb5b904",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "a3d601b9-90d6-4700-8195-7ac8fe55805b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015XDVtkHfqap3NPmKomMs72",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 57241,
      "cache_read_input_tokens": 11447,
      "output_tokens": 225,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 57241,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 225,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 57241,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 57241
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

_source line 10 · 2026-05-16T15:20:36.948Z_

<details open><summary>🔧 Tool call — Agent · `toolu_013GWdLkBtr7TWCiPoh7Aaiq`</summary>

```json
{
  "description": "Find planned experiments",
  "prompt": "In the directory /home/ubuntu/.agent-ml-research-idea_gen_0509_11, search for any files that define an experiment_plan, particularly looking for experiments with status \"planned\" or \"RUNNING\". Check files like experiment_plan.yaml, experiment_plan.md, or any YAML/JSON files in the project root or subdirectories that contain experiment definitions. Also check the paper_framing.md or any planning documents. Report the full content of any planned/running experiments you find, including their IDs, descriptions, claims, and any pre-registered criteria."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a26f3f5f-0cbb-471b-883b-10e1dcb5b904",
  "isSidechain": false,
  "requestId": "req_011Cb6USsdsCjbp7qXXGa2Vx",
  "type": "assistant",
  "uuid": "98399896-0ac6-4082-9342-018b2fda9496",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "a3d601b9-90d6-4700-8195-7ac8fe55805b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015XDVtkHfqap3NPmKomMs72",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 57241,
      "cache_read_input_tokens": 11447,
      "output_tokens": 225,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 57241,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 225,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 57241,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 57241
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

_source line 11 · 2026-05-16T15:22:07.974Z_

<details><summary>↩ Tool result · `toolu_013GWdLkBtr7TWCiPoh7Aaiq`</summary>

```text
Here is the complete report of all experiment plans and their planned/running experiments across the three projects.

---

## Three `experiment_plan.yaml` files found

### 1. `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/experiment_plan.yaml`

**Project**: phase-gated-compound-sparse
**Type**: Retrospective experiment-to-claim mapping (38 experiments across 13 claims)
**Generated**: 2026-05-16

This file is primarily a mapping of completed experiments to claims. The relevant non-confirmed claims are:

**Claims with status "running":**

- **C7** -- "Statistical power at n=500 confirms dose-response" -- status: `running`
  - Experiment `c7_c2_n500_deepseek`: DS n=500, all 4 sparsities significant (p<1e-70), CIs non-overlapping
  - Experiment `c7_c2_qw_n500_r3`: QW n=500, all 4 sparsities significant (p<1e-14 Bonferroni-corrected), mid_null_rate=45.2%

- **C10** -- "Phase gradient cross-benchmark robust; strategy specificity task-modulated" -- status: `running`
  - Experiment `c10_gsm8k_profiling_ds`: DS GSM8K importance gradient monotonic (s015=0.241 to s030=4.636)
  - Experiment `c10_gsm8k_profiling_qw`: QW GSM8K importance gradient monotonic (s015=0.039 to s030=2.092)
  - Experiment `c10_gsm8k_qw_rand_s025_v2`: QW random s025 GSM8K phase gradient weaker than importance
  - Experiment `c10_gsm8k_qw_rand_s030_v2`: QW random s030 GSM8K compound effect confirmed

**Claim with status "planned":**

- **C9** -- "Differentiation from Lethe/SparK prior work" -- status: `planned`
  - No experiments are yet mapped to this claim in the plan file.

**Registry RUNNING entries for this project:**

- `c8_llama_n250_fixed` -- RUNNING since 2026-05-16T03:20. C8 LLaMA n=250 cross-architecture validation (DeepSeek-R1-Distill-Llama-8B, 8 conditions: imp/rand x 4 sparsity, MATH-500, max_new_tokens=8192). Server: westd-22162, GPU cuda:2+cuda:3.

- `gpqa_ds_importance_s015` -- RUNNING since 2026-05-16T05:13. Cross-task generalization: compound sparsity on GPQA Diamond (non-math reasoning) using quantile 3-segment phase decomposition. DS-R1 importance s015 as first condition. Server: westd-22162, GPU cuda:1.

---

### 2. `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/redundancy-compound-sparsity/experiment_plan.yaml`

**Project**: redundancy-compound-sparsity
**Target**: EMNLP 2026 ARR (DDL: 2026-05-25)
**Last updated**: 2026-05-12
**Note**: D004 MLA narrative SUSPENDED -- DeepSeek-R1-Distill-Qwen-7B is GQA not MLA

**PLANNED experiments:**

- **confound-ctrl-001** (P0-URGENT)
  - Name: "Confound control: DeepSeek-R1-Distill-Llama-8B (same arch + reasoning)"
  - Claim: Confound resolution: architecture vs reasoning training
  - Description: Perfect control -- same Llama GQA architecture as Llama-3.1-8B + same reasoning distillation. If r~0.15 then reasoning is confound; if r~0.47 then architecture matters.
  - Model: deepseek-ai/DeepSeek-R1-Distill-Llama-8B
  - GPU hours: 2
  - Depends on: neg-cross-model-001
  - Status in plan: PLANNED
  - **Status in registry: RUNNING** (since 2026-05-12T02:27, server seetacloud-bjb2-structtts, pid 24628)

- **confound-ctrl-002** (P0)
  - Name: "Confound control: Qwen2-7B-Instruct (same arch + instruction)"
  - Claim: Confound resolution: architecture vs reasoning training
  - Description: Second control -- same Qwen2 GQA architecture + instruction training. If r~0.47 then Qwen2 arch is fine, reasoning is confound.
  - Model: Qwen/Qwen2-7B-Instruct
  - GPU hours: 2
  - Depends on: mvp-001b
  - Status in plan: PLANNED
  - Status in registry: PREPARING

- **llama-sparsity-sweep** (P0)
  - Name: "Llama sparsity level sweep: push delta-pert higher"
  - Claim: Claim 1, 3 (strengthen GQA positive evidence)
  - Description: Test higher sparsity on Llama {50%, 55%, 60%, 65%, 70%}. Current delta-pert=+6.6% at 55%.
  - Model: meta-llama/Llama-3.1-8B-Instruct
  - GPU hours: 4
  - Status: PLANNED

- **llama-layer-analysis** (P0)
  - Name: "Llama per-layer r + delta-pert decomposition"
  - Claim: Claim 3 (per-layer architecture comparison)
  - Description: Per-layer analysis on Llama data. Compare with DeepSeek per-layer profile.
  - GPU hours: 1
  - Status: PLANNED

- **kv-bench-001** (P0)
  - Name: "KV eviction benchmark: CARC-KV vs baselines"
  - Claim: Claim 4 (O(1) KV eviction)
  - Description: CARC-KV (O(1)) vs H2O (O(n)) vs SnapKV vs StreamingLLM. KV budgets {30%, 50%, 70%}.
  - Model: deepseek-ai/DeepSeek-R1-Distill-Qwen-7B
  - GPU hours: 20
  - Status: PREPARING

- **cross-arch-mistral** (P1)
  - Name: "Mistral-7B validation (2nd GQA model)"
  - Claim: Claim 1 (GQA generalization)
  - Description: Repeat validation on Mistral-7B-Instruct.
  - Model: mistralai/Mistral-7B-Instruct-v0.3
  - GPU hours: 6
  - Status: PLANNED

- **mla-signal-analysis** (P1) -- **SUSPENDED**
  - Name: "MLA latent space semantic fidelity analysis"
  - Claim: Claim 2 (mechanistic: why MLA breaks signal)
  - Description: SUSPENDED (D005) -- no MLA model available.
  - Status: SUSPENDED

- **kv-eviction-wallclock** (P1)
  - Name: "Wall-clock: O(1) vs O(n) eviction cost"
  - Claim: Claim 4
  - Description: Eviction overhead timing at L={4K, 8K, 16K, 32K}.
  - GPU hours: 10
  - Status: PLANNED

- **neg-per-head** (P1)
  - Name: "Per-head KV contribution analysis"
  - Claim: Claim 2, 3 (head count 4 vs 8)
  - Description: Normalize per-head signal contribution.
  - GPU hours: 2
  - Status: PLANNED

- **kv-eviction-ablation** (P2)
  - Name: "KV eviction: key-only vs key+value anchor"
  - Claim: Claim 4
  - GPU hours: 5
  - Status: PLANNED

- **llama-downstream** (P2)
  - Name: "Llama two-tier sparsity downstream accuracy"
  - Claim: Claim 1 (practical value of cross-axis on GQA)
  - Description: Apply CARC two-tier MLP sparsity on Llama: 55% redundant / 40% novel. Compare accuracy vs uniform sparsity on MATH.
  - GPU hours: 6
  - Status: PLANNED

---

### 3. `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/redundancy-compound-sparsity-2/experiment_plan.yaml`

**Project**: redundancy-compound-sparsity-2 (CARC / KV eviction focused)
**Structure**: 6 phases (Phase 0 through Phase 5)

All experiments in this file lack an explicit status field (none say PLANNED/RUNNING), but none have registry_ids pointing to completed results except the Phase 0 sanity experiments. The experiments are:

**Phase 0 -- Sanity Gate:**
- `pathc_sanity_reasoning`: EMA vs random eviction PPL on reasoning traces (MATH-500). Success: PPL gap >= 5%. registry_id: d003_reasoning_traces
- `pathc_sanity_wikitext32k`: EMA vs recency eviction PPL on WikiText-2 32K. Success: EMA PPL < recency PPL. registry_id: d003_wikitext_32k

**Phase 0b -- Analysis Paper Contingency (triggered if Phase 0 FAIL):**
- `analysis_heatmap`: Per-layer heatmap visualization of spatial decoupling
- `analysis_attn_vs_ema`: Attention-score vs EMA signal comparison. Success: quantitative comparison showing EMA vs attention score correlation/divergence
- `analysis_tau_sweep`: Tau (EMA decay) sensitivity sweep. Success: clear trend in PPL vs gamma curve
- `analysis_decay_curve`: Information decay curve analysis. Success: distinct decay curves for reasoning vs repetitive tokens
- `analysis_second_model`: Qwen2.5-7B validation for generalization

**Phase 1 -- PPL Budget Sweep:**
- `pathc_ppl_budget30`: PPL at 30% KV budget. Success: PPL degradation <= 10%
- `pathc_ppl_budget50`: PPL at 50% KV budget. Success: PPL degradation <= 5%
- `pathc_ppl_budget70`: PPL at 70% KV budget. Success: PPL degradation <= 2%

**Phase 2 -- Baseline Comparison:**
- `pathc_baseline_h2o`: H2O baseline comparison. Success: CARC PPL < H2O PPL at 50%
- `pathc_baseline_rkv`: R-KV baseline (O(B^2) vs O(1)). Success: PPL within 2% of R-KV + throughput advantage

**Phase 3 -- Ablation:**
- `pathc_ablation_gamma`: EMA gamma sensitivity (0.5, 0.7, 0.9, 0.95)
- `pathc_ablation_budget`: Budget ratio sweep (20%-80% in 10% steps)
- `pathc_ablation_grace`: Grace window size sweep (0, 50, 100, 175, 250, 500)
- `pathc_ablation_perhead`: Per-head vs concatenated EMA comparison

**Phase 4 -- Reasoning Eval:**
- `pathc_math500_eval`: MATH-500 accuracy with CARC at 50% budget. Success: accuracy >= 90% of full cache

**Phase 5 -- Scaling + Throughput:**
- `pathc_scaling_32k`: 32K context PPL. Success: degradation <= 5%
- `pathc_scaling_64k`: 64K context PPL. Success: degradation <= 8%
- `pathc_throughput`: Throughput benchmark. Success: within 5% of full cache

---

### Additional RUNNING entry in global registry

- `inverted_ema_reasoning_v2` -- RUNNING since 2026-05-12T17:25, server westd-16980, model DeepSeek-R1-Distill-Qwen-14B, GPU cuda:1. Rerun of inverted_ema_reasoning (killed at 85% on GPU 0).

---

### Summary of active work

| Status | Count | Location |
|--------|-------|----------|
| RUNNING | 2 | phase-gated-compound-sparse registry (c8_llama_n250_fixed, gpqa_ds_importance_s015) |
| RUNNING | 1 | redundancy-compound-sparsity registry (confound-ctrl-001) |
| RUNNING | 1 | global registry (inverted_ema_reasoning_v2) |
| planned (claim) | 1 | phase-gated-compound-sparse (C9: differentiation from prior work) |
| running (claim) | 2 | phase-gated-compound-sparse (C7: n=500 dose-response, C10: cross-benchmark) |
| PLANNED | 9 | redundancy-compound-sparsity experiment_plan (confound controls, Llama sweep, KV benchmarks, Mistral, ablations) |
| implicit planned | ~18 | redundancy-compound-sparsity-2 (all phases 0-5, no status field set) |

agentId: a8f88448717419ecd (use SendMessage with to: 'a8f88448717419ecd' to continue this agent)
&lt;usage>total_tokens: 59003
tool_uses: 15
duration_ms: 91018&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "98399896-0ac6-4082-9342-018b2fda9496",
  "isSidechain": false,
  "promptId": "1b3ef117-44ac-4494-a1a3-d617fc268060",
  "type": "user",
  "uuid": "0ade52ea-6cbb-4409-b07b-a6bb92ce6112",
  "toolUseResult": {
    "status": "completed",
    "prompt": "In the directory /home/ubuntu/.agent-ml-research-idea_gen_0509_11, search for any files that define an experiment_plan, particularly looking for experiments with status \"planned\" or \"RUNNING\". Check files like experiment_plan.yaml, experiment_plan.md, or any YAML/JSON files in the project root or subdirectories that contain experiment definitions. Also check the paper_framing.md or any planning documents. Report the full content of any planned/running experiments you find, including their IDs, descriptions, claims, and any pre-registered criteria.",
    "agentId": "a8f88448717419ecd",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the complete report of all experiment plans and their planned/running experiments across the three projects.\n\n---\n\n## Three `experiment_plan.yaml` files found\n\n### 1. `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/experiment_plan.yaml`\n\n**Project**: phase-gated-compound-sparse\n**Type**: Retrospective experiment-to-claim mapping (38 experiments across 13 claims)\n**Generated**: 2026-05-16\n\nThis file is primarily a mapping of completed experiments to claims. The relevant non-confirmed claims are:\n\n**Claims with status \"running\":**\n\n- **C7** -- \"Statistical power at n=500 confirms dose-response\" -- status: `running`\n  - Experiment `c7_c2_n500_deepseek`: DS n=500, all 4 sparsities significant (p<1e-70), CIs non-overlapping\n  - Experiment `c7_c2_qw_n500_r3`: QW n=500, all 4 sparsities significant (p<1e-14 Bonferroni-corrected), mid_null_rate=45.2%\n\n- **C10** -- \"Phase gradient cross-benchmark robust; strategy specificity task-modulated\" -- status: `running`\n  - Experiment `c10_gsm8k_profiling_ds`: DS GSM8K importance gradient monotonic (s015=0.241 to s030=4.636)\n  - Experiment `c10_gsm8k_profiling_qw`: QW GSM8K importance gradient monotonic (s015=0.039 to s030=2.092)\n  - Experiment `c10_gsm8k_qw_rand_s025_v2`: QW random s025 GSM8K phase gradient weaker than importance\n  - Experiment `c10_gsm8k_qw_rand_s030_v2`: QW random s030 GSM8K compound effect confirmed\n\n**Claim with status \"planned\":**\n\n- **C9** -- \"Differentiation from Lethe/SparK prior work\" -- status: `planned`\n  - No experiments are yet mapped to this claim in the plan file.\n\n**Registry RUNNING entries for this project:**\n\n- `c8_llama_n250_fixed` -- RUNNING since 2026-05-16T03:20. C8 LLaMA n=250 cross-architecture validation (DeepSeek-R1-Distill-Llama-8B, 8 conditions: imp/rand x 4 sparsity, MATH-500, max_new_tokens=8192). Server: westd-22162, GPU cuda:2+cuda:3.\n\n- `gpqa_ds_importance_s015` -- RUNNING since 2026-05-16T05:13. Cross-task generalization: compound sparsity on GPQA Diamond (non-math reasoning) using quantile 3-segment phase decomposition. DS-R1 importance s015 as first condition. Server: westd-22162, GPU cuda:1.\n\n---\n\n### 2. `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/redundancy-compound-sparsity/experiment_plan.yaml`\n\n**Project**: redundancy-compound-sparsity\n**Target**: EMNLP 2026 ARR (DDL: 2026-05-25)\n**Last updated**: 2026-05-12\n**Note**: D004 MLA narrative SUSPENDED -- DeepSeek-R1-Distill-Qwen-7B is GQA not MLA\n\n**PLANNED experiments:**\n\n- **confound-ctrl-001** (P0-URGENT)\n  - Name: \"Confound control: DeepSeek-R1-Distill-Llama-8B (same arch + reasoning)\"\n  - Claim: Confound resolution: architecture vs reasoning training\n  - Description: Perfect control -- same Llama GQA architecture as Llama-3.1-8B + same reasoning distillation. If r~0.15 then reasoning is confound; if r~0.47 then architecture matters.\n  - Model: deepseek-ai/DeepSeek-R1-Distill-Llama-8B\n  - GPU hours: 2\n  - Depends on: neg-cross-model-001\n  - Status in plan: PLANNED\n  - **Status in registry: RUNNING** (since 2026-05-12T02:27, server seetacloud-bjb2-structtts, pid 24628)\n\n- **confound-ctrl-002** (P0)\n  - Name: \"Confound control: Qwen2-7B-Instruct (same arch + instruction)\"\n  - Claim: Confound resolution: architecture vs reasoning training\n  - Description: Second control -- same Qwen2 GQA architecture + instruction training. If r~0.47 then Qwen2 arch is fine, reasoning is confound.\n  - Model: Qwen/Qwen2-7B-Instruct\n  - GPU hours: 2\n  - Depends on: mvp-001b\n  - Status in plan: PLANNED\n  - Status in registry: PREPARING\n\n- **llama-sparsity-sweep** (P0)\n  - Name: \"Llama sparsity level sweep: push delta-pert higher\"\n  - Claim: Claim 1, 3 (strengthen GQA positive evidence)\n  - Description: Test higher sparsity on Llama {50%, 55%, 60%, 65%, 70%}. Current delta-pert=+6.6% at 55%.\n  - Model: meta-llama/Llama-3.1-8B-Instruct\n  - GPU hours: 4\n  - Status: PLANNED\n\n- **llama-layer-analysis** (P0)\n  - Name: \"Llama per-layer r + delta-pert decomposition\"\n  - Claim: Claim 3 (per-layer architecture comparison)\n  - Description: Per-layer analysis on Llama data. Compare with DeepSeek per-layer profile.\n  - GPU hours: 1\n  - Status: PLANNED\n\n- **kv-bench-001** (P0)\n  - Name: \"KV eviction benchmark: CARC-KV vs baselines\"\n  - Claim: Claim 4 (O(1) KV eviction)\n  - Description: CARC-KV (O(1)) vs H2O (O(n)) vs SnapKV vs StreamingLLM. KV budgets {30%, 50%, 70%}.\n  - Model: deepseek-ai/DeepSeek-R1-Distill-Qwen-7B\n  - GPU hours: 20\n  - Status: PREPARING\n\n- **cross-arch-mistral** (P1)\n  - Name: \"Mistral-7B validation (2nd GQA model)\"\n  - Claim: Claim 1 (GQA generalization)\n  - Description: Repeat validation on Mistral-7B-Instruct.\n  - Model: mistralai/Mistral-7B-Instruct-v0.3\n  - GPU hours: 6\n  - Status: PLANNED\n\n- **mla-signal-analysis** (P1) -- **SUSPENDED**\n  - Name: \"MLA latent space semantic fidelity analysis\"\n  - Claim: Claim 2 (mechanistic: why MLA breaks signal)\n  - Description: SUSPENDED (D005) -- no MLA model available.\n  - Status: SUSPENDED\n\n- **kv-eviction-wallclock** (P1)\n  - Name: \"Wall-clock: O(1) vs O(n) eviction cost\"\n  - Claim: Claim 4\n  - Description: Eviction overhead timing at L={4K, 8K, 16K, 32K}.\n  - GPU hours: 10\n  - Status: PLANNED\n\n- **neg-per-head** (P1)\n  - Name: \"Per-head KV contribution analysis\"\n  - Claim: Claim 2, 3 (head count 4 vs 8)\n  - Description: Normalize per-head signal contribution.\n  - GPU hours: 2\n  - Status: PLANNED\n\n- **kv-eviction-ablation** (P2)\n  - Name: \"KV eviction: key-only vs key+value anchor\"\n  - Claim: Claim 4\n  - GPU hours: 5\n  - Status: PLANNED\n\n- **llama-downstream** (P2)\n  - Name: \"Llama two-tier sparsity downstream accuracy\"\n  - Claim: Claim 1 (practical value of cross-axis on GQA)\n  - Description: Apply CARC two-tier MLP sparsity on Llama: 55% redundant / 40% novel. Compare accuracy vs uniform sparsity on MATH.\n  - GPU hours: 6\n  - Status: PLANNED\n\n---\n\n### 3. `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/redundancy-compound-sparsity-2/experiment_plan.yaml`\n\n**Project**: redundancy-compound-sparsity-2 (CARC / KV eviction focused)\n**Structure**: 6 phases (Phase 0 through Phase 5)\n\nAll experiments in this file lack an explicit status field (none say PLANNED/RUNNING), but none have registry_ids pointing to completed results except the Phase 0 sanity experiments. The experiments are:\n\n**Phase 0 -- Sanity Gate:**\n- `pathc_sanity_reasoning`: EMA vs random eviction PPL on reasoning traces (MATH-500). Success: PPL gap >= 5%. registry_id: d003_reasoning_traces\n- `pathc_sanity_wikitext32k`: EMA vs recency eviction PPL on WikiText-2 32K. Success: EMA PPL < recency PPL. registry_id: d003_wikitext_32k\n\n**Phase 0b -- Analysis Paper Contingency (triggered if Phase 0 FAIL):**\n- `analysis_heatmap`: Per-layer heatmap visualization of spatial decoupling\n- `analysis_attn_vs_ema`: Attention-score vs EMA signal comparison. Success: quantitative comparison showing EMA vs attention score correlation/divergence\n- `analysis_tau_sweep`: Tau (EMA decay) sensitivity sweep. Success: clear trend in PPL vs gamma curve\n- `analysis_decay_curve`: Information decay curve analysis. Success: distinct decay curves for reasoning vs repetitive tokens\n- `analysis_second_model`: Qwen2.5-7B validation for generalization\n\n**Phase 1 -- PPL Budget Sweep:**\n- `pathc_ppl_budget30`: PPL at 30% KV budget. Success: PPL degradation <= 10%\n- `pathc_ppl_budget50`: PPL at 50% KV budget. Success: PPL degradation <= 5%\n- `pathc_ppl_budget70`: PPL at 70% KV budget. Success: PPL degradation <= 2%\n\n**Phase 2 -- Baseline Comparison:**\n- `pathc_baseline_h2o`: H2O baseline comparison. Success: CARC PPL < H2O PPL at 50%\n- `pathc_baseline_rkv`: R-KV baseline (O(B^2) vs O(1)). Success: PPL within 2% of R-KV + throughput advantage\n\n**Phase 3 -- Ablation:**\n- `pathc_ablation_gamma`: EMA gamma sensitivity (0.5, 0.7, 0.9, 0.95)\n- `pathc_ablation_budget`: Budget ratio sweep (20%-80% in 10% steps)\n- `pathc_ablation_grace`: Grace window size sweep (0, 50, 100, 175, 250, 500)\n- `pathc_ablation_perhead`: Per-head vs concatenated EMA comparison\n\n**Phase 4 -- Reasoning Eval:**\n- `pathc_math500_eval`: MATH-500 accuracy with CARC at 50% budget. Success: accuracy >= 90% of full cache\n\n**Phase 5 -- Scaling + Throughput:**\n- `pathc_scaling_32k`: 32K context PPL. Success: degradation <= 5%\n- `pathc_scaling_64k`: 64K context PPL. Success: degradation <= 8%\n- `pathc_throughput`: Throughput benchmark. Success: within 5% of full cache\n\n---\n\n### Additional RUNNING entry in global registry\n\n- `inverted_ema_reasoning_v2` -- RUNNING since 2026-05-12T17:25, server westd-16980, model DeepSeek-R1-Distill-Qwen-14B, GPU cuda:1. Rerun of inverted_ema_reasoning (killed at 85% on GPU 0).\n\n---\n\n### Summary of active work\n\n| Status | Count | Location |\n|--------|-------|----------|\n| RUNNING | 2 | phase-gated-compound-sparse registry (c8_llama_n250_fixed, gpqa_ds_importance_s015) |\n| RUNNING | 1 | redundancy-compound-sparsity registry (confound-ctrl-001) |\n| RUNNING | 1 | global registry (inverted_ema_reasoning_v2) |\n| planned (claim) | 1 | phase-gated-compound-sparse (C9: differentiation from prior work) |\n| running (claim) | 2 | phase-gated-compound-sparse (C7: n=500 dose-response, C10: cross-benchmark) |\n| PLANNED | 9 | redundancy-compound-sparsity experiment_plan (confound controls, Llama sweep, KV benchmarks, Mistral, ablations) |\n| implicit planned | ~18 | redundancy-compound-sparsity-2 (all phases 0-5, no status field set) |"
      }
    ],
    "totalDurationMs": 91018,
    "totalTokens": 59003,
    "totalToolUseCount": 15,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4122,
      "cache_read_input_tokens": 51441,
      "output_tokens": 3439,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4122
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3439,
          "cache_read_input_tokens": 51441,
          "cache_creation_input_tokens": 4122,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4122,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 8,
      "searchCount": 7,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "98399896-0ac6-4082-9342-018b2fda9496",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "a3d601b9-90d6-4700-8195-7ac8fe55805b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-16T15:27:02.241Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture. The user wants me to generate detailed "worst" tier predictions for the experiments in the `phase-gated-compound-sparse` project's experiment_plan. The key running/planned experiments are:

1. **c8_llama_n250_fixed** (RUNNING) - LLaMA n=250 cross-architecture validation
2. **gpqa_ds_importance_s015** (RUNNING) - GPQA cross-task generalization

The "worst" tier is defined as:
- LLaMA n=250 高功效确认 strategy×phase 交互在 Llama 架构上可忽略


- Random phase gradient 稳健
- GPQA 不显著或方向不一致
- Strategy-gated 叙事崩塌

I need to examine the experiment_plan more carefully to identify all planned and running experiments that require predictions. The user specifically asked for detailed data on each planned experiment, so I should focus on the ones still in progress or upcoming rather than the completed ones.

Looking at the registry, the currently running experiments are c8_llama_n250_fixed and gpqa_ds_importance_s015, with c8_llama_gpu0_s025 already finished with initial results. The key question is what these experiments will reveal—particularly whether the LLaMA n=250 run confirms that strategy and phase interactions are negligible, and whether the random phase gradient effect holds up with a larger sample size. Looking at the GPQA experiment structure, gpqa_ds_importance_s015 appears to be just the first condition in a series, with additional sparsity levels (s020, s025, s030) and a random baseline variant likely planned as follow-ups. Combined with the eight conditions from the LLaMA experiment, I need to map out predictions across all these planned conditions under the worst-case tier scenario. Looking at the metric ranges for the worst tier across both the LLaMA and GPQA experiments, I'm identifying the key predictions I need to generate. The main experiments to focus on are the LLaMA n=250 cross-architecture setup and the GPQA cross-task generalization tests, since those are the ones with concrete metric definitions already established. I should also check what's happening with the GPU variant of the c8 experiment to see if that's another prediction target. s025 which is already done - this gives us partial data on one condition of the n=250 experiment:
- n=250, importance s025
- phase_gradient_median_diff: 0.3761
- wilcoxon_p: 4.3e-39
- cohens_dz: 1.1174

This is actually consistent with the worst tier prediction (importance phase gradient d_z ≈ 1.0-1.2). The importance phase gradient is strong even in worst tier - it's the strategy×phase interaction that's weak.

Now I'm mapping out what conditions still need to run for c8_llama_n250_fixed - beyond the completed s025 importance condition, there are the other importance seeds plus all the randomization conditions across different seeds. For GPQA, only one importance condition is currently running, so there should be additional conditions to complete there as well.

Looking more carefully at the experiment plan IDs and their statuses, I notice the listed experiments show DONE, but the running registry clearly has new work underway that represents upgrades or extensions of earlier experiments. ama (which was n=49/50)
2. gpqa_ds_importance_s015 - This is the first GPQA condition

So the "planned" experiments are the ones that are RUNNING or haven't been started yet for the GPQA and LLaMA n=250 work.

Let me now create the full prediction set. I'll organize by:

1. **c8_llama_n250** - LLaMA n=250 cross-architecture (includes both imp and rand, all 4 sparsities)
2. **GPQA cross-task** - DeepSeek importance on GPQA Diamond (multiple sparsity levels)

For the worst tier narrative, the key predictions are:
- LLaMA n=250 imp_vs_rand d_z still small (< 0.25) — confirming it's a high-powered null
- LLaMA random phase gradient confirmed (d_z ≥ 0.35)
- LLaMA importance phase gradient confirmed (d_z ≈ 1.0-1.2)
- GPQA results are NS or direction inconsistent
- Strategy-specificity is Qwen2-specific

Now I'm looking at the detailed numerical predictions for each experiment. I have c8_llama_gpu0_s025 showing d_z = 1.1174 for the importance phase gradient at n=250, and examining the n=49 baseline results across sparsity levels to project what the n=250 scaling should look like.

With 5× more statistical power at n=250, the importance versus random comparison should remain small (likely 0.15-0.25 range) even with tighter confidence intervals, suggesting the n=49 estimates might have been slightly inflated. The phase gradient effects for both importance and random conditions should remain robust, with the importance phase gradient staying in the 1.0-1.2 range and random phase gradient holding around 0.35-0.45. , the true effect could be smaller than the n=49 point estimate. With n=250, the confidence interval would narrow to roughly ±0.13 around the point estimate, giving me a much tighter picture of where the effect actually sits.

Now I'm ready to draft the full YAML predictions. For the LLaMA cross-architecture experiment at n=250, I'm expecting phase gradient effect sizes around 1.0-1.2 across all sparsity levels with p-values well below 1e-30, and median differences that increase monotonically with sparsity.

For the random conditions, I'm predicting phase gradients in the 0.35-0.55 range—notably stronger than what I saw with DeepSeek and Qwen—with significant Wilcoxon results across all sparsity levels. The strategy by phase interaction is where I expect the weakest findings: effect sizes under 0.25 with minimal Bonferroni-corrected significance, which would be the most concerning null result for demonstrating strategy specificity.

On the GPQA cross-task experiment, I'm anticipating small median differences for DeepSeek importance at s015, somewhere between 0.02-0.08, with weak or inconsistent phase gradients and likely non-significant Bonferroni-corrected p-values.

Now I need to think through the structure more carefully. The user is asking for detailed data on each planned experiment, but looking at what's actually running, I have two main efforts: the LLaMA n=250 fixed experiment and the GPQA DeepSeek importance s015 condition. I should organize my predictions around these two core experiments and consider what additional GPQA conditions would be needed to complete the picture. Looking at the partial result from c8_llama_gpu0_s025, the effect size and confidence interval align well with my predictions for the worst-performing tier—the Cohen's d_z of 1.1174 falls right in the expected range of 0.95 to 1.2. Now I need to structure the full YAML output with the main c8_llama_n250_fixed experiment and its various condition analyses, plus the GPQA experiments that are either running or need predictions.

Generating YAML output... Finishing the YAML structure with the remaining experiment entries, then I need to check the naming conventions against existing plan IDs to make sure they're consistent with the registry format.

Looking at the two main experimental efforts here—the LLaMA n=250 upgrade and the GPQA cross-task work—I should organize the entries around those natural units. Now I'm thinking through what the importance phase gradient predictions would be at n=250, building from the baseline measurements at n=49.

For the importance phase gradient, I see the s025 value is already observed at 1.117, and I'm predicting the other seed values should cluster around similar magnitudes, mostly in the 0.95-1.15 range. The random phase gradient measurements from n=49 show more variation, ranging from 0.35 to 0.45, and I'm expecting those patterns to hold at the larger sample size.

Now looking at the LLaMA importance versus random interaction effect, the estimates at n=49 show a clear trend where higher sparsity levels produce larger effects, starting around 0.19 at s015 and climbing to 0.34 at s030. The confidence intervals are quite wide at this sample size, but I'm predicting they'll tighten considerably at n=250, with most lower sparsity values becoming non-significant while the higher sparsity effects remain detectable.

Let me verify this against the Bonferroni-corrected threshold—with four tests and α=0.0125, I need to check whether the z-statistic for the s030 effect at n=250 would cross that boundary. At d_z=0.20 with n=250, that gives roughly 3.16, which should be significant. So the worst tier would have just s030 crossing the Bonferroni threshold with a d_z around 0.20, while the others fall short. Now I'm working through what the median differences might look like at n=250, scaling from the values I observed at n=49 where s030 showed the largest effect at 0.3562. regress somewhat. The existing c8_llama_gpu0_s025 result shows imp s025 has median_diff = 0.3761 and d_z = 1.12 for the phase gradient (within importance only). But we need the imp_vs_rand comparison, which requires the random data too.

For the imp_vs_rand median_diff at n=250, worst tier predicts:
- s015: ~0.015 [CI: -0.005, 0.035]
- s020: ~0.025 [CI: -0.010, 0.060]
- s025: ~0.065 [CI: 0.005, 0.125]
- s030: ~0.180 [CI: 0.050, 0.310]

These are small effects, mostly NS after Bonferroni.

On GPQA Diamond, the phase gradient effect either disappears or becomes inconsistent. The worst tier predicts minimal median differences across all importance levels—s015 around 0.03, s020 around 0.08, and s025 around 0.15—all falling short of significance even before Bonferroni correction, suggesting the strategy doesn't generalize to harder reasoning tasks. The worst-case scenario for GPQA would show non-monotonic effects across the dataset sizes, with some negative differences and inconsistent directionality that breaks the expected pattern. This would result in low Spearman correlation, no statistical significance even before multiple comparison correction, and minimal separation between the strategy and random baseline. Now I'm realizing I should check what experiments are actually planned versus already completed—looking back at the experiment_plan, all listed experiments show DONE status, but there are two RUNNING experiments in the registry that I should focus on instead. I'm going to structure the output with detailed predictions for each experiment—the LLaMA n=250 run and the GPQA conditions—making sure to include specific metrics, statistical comparisons, and the tables and figures that would emerge from these analyses. Let me draft this as a comprehensive YAML block now. I'm mapping these metrics to two core experiments: the main LLaMA fixed setup and a GPQA sweep across different sparsity levels. I need to verify whether random gradient conditions are included for GPQA since the importance-to-random ratio metric suggests they are, then I'll structure the full prediction output with tables and figures.

Now I'm planning the specific tables and figures I'll generate—phase gradient comparisons across conditions, importance versus random breakdowns, and cross-benchmark interactions—before moving into the detailed numerical predictions for each experimental condition.

Generating numerical predictions for each condition... Now I'm looking at the results for subject s030, which shows a phase gradient effect size of 1.00 with a substantial median difference of 0.85 and highly significant p-value. I'm also compiling the metrics for the random phase gradient condition across subjects, where the effect sizes are notably smaller, ranging from 0.36 to 0.45, with correspondingly smaller median differences and p-values in the range of 1e-6 to 1e-8. Looking at the s030 results for the importance versus random interaction, the effect size is 0.22 with a p-value of 0.0035, which crosses the Bonferroni threshold at 0.014—this is the only significant result in that comparison. Across all conditions, the importance phase gradient shows a mean effect size of 1.05 compared to 0.41 for random, giving roughly a 2.6× ratio, which is substantially lower than what I'm seeing with other architectures. The dose-response pattern holds for importance conditions and approximately for random ones. Now I'm moving into the GPQA predictions for the worst tier, starting with the DS importance conditions. Looking at the dose-response pattern across these conditions, the median differences show no clear monotonic trend, and the Spearman correlation is weak and non-significant. The random condition results show minimal separation between strategy and chance performance, with the improvement ratio hovering near 1.0. I've got all the numbers I need now to compile the final YAML output.

For the c8_llama_n250 analysis, the high-powered study confirms that strategy and phase interact minimally on LLaMA, while the importance phase shows robust gradients matching the smaller sample but with tighter confidence intervals. The random phase also produces meaningful gradients, which undermines the idea that phase effects are strategy-specific—instead, phase modulation appears universal across architectures, though strategy sensitivity varies. For GPQA, the phase gradient fails to replicate on Diamond, and the non-monotonic pattern with non-significant results suggests the effect doesn't generalize to this domain.

The shorter reasoning chains and different cognitive structure in GPQA likely explain why phase modulation doesn't emerge there, so the findings are really specific to mathematical reasoning tasks. Given that GPQA doesn't show the effect, it makes sense to move it to the appendix or exclude it entirely. I'm also settling on n=50 for GPQA to keep consistency across experiments, accounting for the higher per-problem variability on harder questions. Now I need to write out the complete YAML with result_rationale for every prediction, making sure the worst tier classification aligns with the decision to exclude or appendix GPQA.

The core assumptions driving my predictions are that the imp_vs_rand effect stays below 0.25 for LLaMA at n=250 (showing the interaction is Qwen2-specific), the random phase gradient stays above 0.35 for LLaMA (confirming phase modulation works independently of eviction strategy), GPQA shows no consistent phase gradient across tasks (cross-task generalization fails), and strategy-specificity is limited to Qwen2's architecture rather than being universal. I'm now matching these assumptions to the specific experiments in the plan to finalize the predictions.

Looking at what's actually running, I see c8_llama_n250_fixed is the n=250 upgrade I need to predict for, and gpqa_ds_importance_s015 is the GPQA experiment that's active. Since only the s015 seed is running for GPQA, I should predict what the full GPQA sweep would look like based on the worst tier definition, then structure my YAML predictions around these two main experiments. I'm narrowing down to just the experiments that are actually running in the pipeline right now—the LLaMA cross-architecture validation and the GPQA importance sampling condition—rather than trying to predict the full sweep that might have been planned. The registry is pretty clear about what's actively executing, so I should stick with those concrete cases. I'm listing out the remaining GPQA conditions across different sparsity levels, plus a cross-task synthesis experiment. But I'm second-guessing whether the user will actually run all of these—only s015 is currently active, so maybe I should focus on what's realistically planned versus what a complete worst-tier scenario would include. Let me just write out the predictions pragmatically, covering both the actively running experiments and what the full analysis would look like if they decide to expand. now. I'm overthinking the structure.

Final structure:
1. c8_llama_n250_fixed (comprehensive, all conditions)
2. gpqa_ds_importance_s015 (the running experiment)
3. gpqa_full_sweep (what the full GPQA experiment set would show)

These three cover all the worst tier metrics.

Let me write the YAML now. It will be long but the user asked for detailed data.

Actually, I realize I should also check: are there any other planned experiments in the experiment_plan that I'm missing? Let me re-check...

The experiment_plan lists claims C1-C10 and S3→C, S7→C. All experiments under these claims are status: DONE. The only "planned" claim is C9 (differentiation from prior work), which is a writing task, not an experiment.

The RUNNING experiments in the registry are the c8_llama_n250_fixed upgrade and gpqa_ds_importance_s015 cross-task experiment. So my prediction set should cover these two plus the implied GPQA follow-ups.

Now I need to structure the c8_llama_n250_fixed predictions carefully since it includes all 8 conditions—the importance phase gradient across 4 conditions, the random phase gradient across 4 conditions, and the strategy×phase interactions. Let me organize this with sub-sections for each component.

For GPQA, I'll predict the individual condition results and cross-task comparisons.

I'm going to write the YAML output now with comprehensive expected results, rationales, tables, and figure descriptions for each experiment.

Generating experiment specifications... Looking at the confidence intervals for the random phase gradient effect sizes, they're all relatively wide and overlap substantially with zero, which aligns with the small-to-medium interpretation. The median differences are notably smaller than the intentional phase gradient condition across all sample sizes, and while all four Wilcoxon tests remain significant after Bonferroni correction, the effect sizes tell a different story—the random manipulation produces much weaker and less consistent effects compared to the deliberate phase gradient manipulation.

Now examining the interaction between strategy and phase type, the effect sizes comparing intentional versus random phase gradients increase progressively from 0.10 at s015 to 0.22 at s030, suggesting the difference between strategies becomes more pronounced with larger samples. The confidence intervals start overlapping zero at smaller sample sizes but become increasingly separated from zero as sample size grows, and the Wilcoxon p-values show a clear downward trend, with only the largest sample size reaching significance even after Bonferroni correction. The random phase gradient holds up consistently across LLaMA even with random eviction, which differs qualitatively from Qwen2's pattern—suggesting phase modulation isn't tied to a specific eviction strategy. The interaction effect between importance and random phases grows monotonically but remains small even at n=250 (max d_z=0.22), with only s030 reaching Bonferroni significance at the borderline, indicating this is a high-powered null result where we have sufficient statistical power to detect effects if they existed.

Generating comparison table... Looking at the bar chart comparing importance-weighted versus random gradient strategies across sparsity levels, I see the importance-based approach consistently hovers around 1.0 while random stays near 0.4, with the separation between them only reaching statistical significance at the s030 level. The cross-architecture comparison reveals a striking difference: Qwen2 models show a much larger gap between strategies (0.44-0.80), while LLaMA exhibits minimal separation (0.10-0.22), suggesting the effectiveness of strategy selection is heavily dependent on the model architecture. With n=250 providing strong statistical power, the small effect sizes for strategy specificity in this worst-case scenario are becoming clearer.

The key finding is that LLaMA's random eviction produces substantial phase gradients (around 0.40) even without importance-based selection, whereas Qwen2 shows no significant effect at lower sparsity levels regardless of strategy. This indicates LLaMA's architecture has an inherent sensitivity to KV cache disruptions during reasoning phases that isn't contingent on whether the eviction strategy preserves important entries—the attention patterns themselves appear fundamentally more vulnerable to any cache perturbation, while Qwen2's attention mechanisms seem better equipped to tolerate random KV cache modifications.

This reshapes the paper's narrative: the phase modulation effect is universal across eviction strategies rather than strategy-specific, so the core contribution should be reframed around phase-dependent compound sparsity severity as an architectural phenomenon rather than a strategy-by-phase interaction. The methodology of paired problem analysis with phase segmentation still holds, but strategy specificity becomes secondary to the architecture-dependent observation.

Now I'm looking at the expected results for the GPQA Diamond subset with importance masking at 0.15 sparsity using quantile phase decomposition. The median difference is small (0.03) with a confidence interval crossing zero, and the Wilcoxon test shows no significance, suggesting the phase gradient effect is present but extremely weak in this non-mathematical reasoning task compared to what we'd expect from MATH-500 or GSM8K.

The key insight is that GPQA's reasoning patterns are less structured than mathematical tasks—there's no clear "think-calculate-verify" progression that maps cleanly to sparsity phases, so phase segmentation based on the model's sparsity patterns doesn't capture the task dynamics as effectively. At s=0.15 sparsity, the compound interaction effects are already minimal, which explains why the median difference drops from 0.39 on MATH-500 to just 0.03 on GPQA.

To really determine if cross-task generalization works, I need to look at the s=0.25 and s=0.30 results—if those higher sparsity levels also show no significant effect or inconsistent directions, then the approach isn't generalizing across tasks. Looking at the statistical results for the non-math reasoning test, the phase gradient approach shows inconsistent performance across sparsity levels, with s020 actually showing a reversal in direction compared to the math domain, suggesting the phase segmentation method doesn't generalize as robustly to general reasoning tasks.

The weaker effects likely stem from two factors: GPQA reasoning chains are substantially shorter than math problems, giving less opportunity for phase differences to accumulate, and the reasoning patterns across GPQA questions are more heterogeneous, so the model's sparsity structure may not follow a consistent phase organization across different reasoning types.

Generating markdown table... Generating markdown table...

The GPQA results completely fail to replicate the phase gradient pattern seen in MATH-500 and GSM8K. There are four critical differences: the effect sizes are dramatically smaller (peak of 0.08 versus 3.99), the monotonic increase breaks down with direction reversals at higher sparsity levels, all GPQA coefficients are statistically non-significant while MATH-500 shows universal significance, and the s020 negative value suggests the high-sparsity phase behaves differently than expected.

Given these findings, GPQA shouldn't be included in the main paper—it belongs in the appendix as a negative result or should be excluded entirely. This means the paper's scope becomes explicitly limited to mathematical reasoning tasks, and I need to add a limitations section acknowledging that cross-task generalization remains unverified. This weakens the EMNLP submission since reviewers will inevitably ask why we're only looking at math, though I can argue that mathematical reasoning represents the clearest manifestation of phase-structured reasoning and that extending to other domains is a natural next step.

For future work, I'm planning an experiment on GPQA using DeepSeek's random masking strategy at different sparsity levels to test whether the importance-versus-random separation holds outside mathematical reasoning. However, since the importance gradient on GPQA is already near zero and statistically insignificant, the ratio between importance and random conditions would be uninformative—both numerator and denominator approach zero, making the ratio unreliable.

I expect the worst-case ratio to fluctuate between 0.5 and 2.0, indicating no meaningful strategy separation on GPQA, which contrasts sharply with the much larger ratios observed on MATH-500 (15-36×) and GSM8K (2.3-3.8×). This reinforces that strategy specificity is highly task-dependent. The core issue is that the phase gradient itself doesn't replicate on GPQA, so I can't really assess strategy specificity there—it's not that the strategy fails, but rather that the foundational effect isn't present to begin with.

The distinction matters: one interpretation suggests strategies aren't important, while the other points to task type as the determining factor for whether phase modulation occurs at all. I'm cross-checking my predictions against the worst-tier metric ranges to ensure they align with the observed data.

Finalizing the YAML output...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ade52ea-6cbb-4409-b07b-a6bb92ce6112",
  "isSidechain": false,
  "requestId": "req_011Cb6UaEYue5peJQxGzHNGs",
  "type": "assistant",
  "uuid": "b964fbf7-7ace-4c6f-95d5-b2526194796e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "a3d601b9-90d6-4700-8195-7ac8fe55805b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JD1LoBimaCubQrtTCNrvj5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3738,
      "cache_read_input_tokens": 68688,
      "output_tokens": 17273,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3738,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 17273,
          "cache_read_input_tokens": 68688,
          "cache_creation_input_tokens": 3738,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3738
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

_source line 13 · 2026-05-16T15:27:02.286Z_

Let me check the partial results already available for the running experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b964fbf7-7ace-4c6f-95d5-b2526194796e",
  "isSidechain": false,
  "requestId": "req_011Cb6UaEYue5peJQxGzHNGs",
  "type": "assistant",
  "uuid": "9ea70625-fb03-4a35-8efd-aa7471908081",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "a3d601b9-90d6-4700-8195-7ac8fe55805b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JD1LoBimaCubQrtTCNrvj5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3738,
      "cache_read_input_tokens": 68688,
      "output_tokens": 17273,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3738,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 17273,
          "cache_read_input_tokens": 68688,
          "cache_creation_input_tokens": 3738,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3738
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

_source line 14 · 2026-05-16T15:27:04.133Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01JH9XQw2YD7c7MXezEtJj41`</summary>

```json
{
  "pattern": "c8_llama_n250|gpqa_ds_importance",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ea70625-fb03-4a35-8efd-aa7471908081",
  "isSidechain": false,
  "requestId": "req_011Cb6UaEYue5peJQxGzHNGs",
  "type": "assistant",
  "uuid": "fdd18231-ed2b-4223-94fa-905bc9eae802",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "a3d601b9-90d6-4700-8195-7ac8fe55805b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JD1LoBimaCubQrtTCNrvj5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3738,
      "cache_read_input_tokens": 68688,
      "output_tokens": 17273,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3738,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 17273,
          "cache_read_input_tokens": 68688,
          "cache_creation_input_tokens": 3738,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3738
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

_source line 15 · 2026-05-16T15:27:04.344Z_

<details><summary>↩ Tool result · `toolu_01JH9XQw2YD7c7MXezEtJj41`</summary>

```text
Found 157 files
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/logs/phase2_worst_attempt0.log
projects/phase-gated-compound-sparse/logs/chats/feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4.jsonl
projects/phase-gated-compound-sparse/logs/workers/worker_ops_check_s030_gpu0_20260516T152633.log
projects/phase-gated-compound-sparse/registry.yaml
projects/phase-gated-compound-sparse/logs/chats/feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4_reviewer.jsonl
projects/phase-gated-compound-sparse/logs/workers/worker_ops_gpqa_prep_remaining_20260516T152422_result.json
projects/phase-gated-compound-sparse/report.md
projects/phase-gated-compound-sparse/checkpoints/gpqa_ds_importance_s020_QUEUED_20260516T152623.json
projects/phase-gated-compound-sparse/logs/workers/worker_ops_gpqa_prep_remaining_20260516T152422.log
projects/phase-gated-compound-sparse/logs/chats/feishu_group_oc_fdc656be1c7fe17c11ab639cdbce3710_director.jsonl
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/logs/phase2_median_attempt0.log
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/logs/phase2_best_attempt0.log
projects/phase-gated-compound-sparse/logs/workers/worker_ssh_c8_llama_n250_progress_check_20260516T150558_result.json
projects/phase-gated-compound-sparse/logs/chats/worker_ssh_c8_llama_n250_progress_check_20260516T150558.jsonl
projects/phase-gated-compound-sparse/logs/workers/worker_ssh_c8_llama_n250_progress_check_20260516T150558.log
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/logs/phase1_attempt0.log
projects/phase-gated-compound-sparse/logs/ralph_loop_timeline.jsonl
projects/phase-gated-compound-sparse/logs/chats/feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4_paper_agent.jsonl
projects/phase-gated-compound-sparse/logs/chats/worker_ops_c8_main_progress_20260516T144339.jsonl
projects/phase-gated-compound-sparse/logs/workers/worker_ops_c8_main_progress_20260516T144339.log
projects/phase-gated-compound-sparse/task_context/agent.md
projects/phase-gated-compound-sparse/logs/chats/archive/feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4_20260516T144128_862210.jsonl
projects/phase-gated-compound-sparse/checkpoints/c8_llama_gpu0_s025_DONE_20260516T140444.json
projects/phase-gated-compound-sparse/checkpoints/c8_llama_gpu0_s025_RUNNING_20260516T140438.json
projects/phase-gated-compound-sparse/logs/workers/worker_ops_gpu_full_status_20260516T140155_result.json
projects/phase-gated-compound-sparse/logs/workers/worker_ops_gpu_full_status_20260516T140155.log
projects/phase-gated-compound-sparse/task_context/director.md
projects/phase-gated-compound-sparse/logs/chats/archive/feishu_group_oc_fdc656be1c7fe17c11ab639cdbce3710_director_20260516T140226_790641.jsonl
projects/phase-gated-compound-sparse/task_context/reviewer.md
projects/phase-gated-compound-sparse/logs/chats/archive/feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4_reviewer_20260516T140222_348277.jsonl
projects/phase-gated-compound-sparse/logs/chats/feishu_dm_oc_82773423f52f26bb5bf8c8f58f32dee0_briefer.jsonl
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/meta.yaml
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/logs/review_worst.log
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/worst/review_context.yaml
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/logs/review_median.log
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/median/review_context.yaml
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/logs/review_best.log
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/best/review_context.yaml
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/logs/paper_agent_worst.log
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/worst/experiment_data.json
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/worst/imagined_experiments.yaml
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/logs/paper_agent_median.log
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/median/experiment_data.json
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/median/imagined_experiments.yaml
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/logs/paper_agent_best.log
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/best/experiment_data.json
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/best/imagined_experiments.yaml
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/logs/phase2_worst_attempt0.log
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/logs/phase2_median_attempt0.log
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/logs/phase2_best_attempt0.log
projects/phase-gated-compound-sparse/checkpoints/gpqa_ds_importance_s015_RUNNING_20260516T074332.json
projects/phase-gated-compound-sparse/checkpoints/gpqa_ds_importance_s015_ALLOCATED_20260516T074301.json
projects/phase-gated-compound-sparse/checkpoints/gpqa_ds_importance_s015_ALLOCATED_20260516T074222.json
projects/phase-gated-compound-sparse/logs/chats/worker_ops_gpu_status_check_20260516T071711.jsonl
projects/phase-gated-compound-sparse/logs/workers/worker_ops_gpu_status_check_20260516T071711.log
projects/phase-gated-compound-sparse/logs/workers/worker_ops_restore_sentinel_files_20260516T062824.log
projects/phase-gated-compound-sparse/logs/workers/worker_ops_fix_sentinel_files_20260516T062655_result.json
projects/phase-gated-compound-sparse/logs/workers/worker_ops_fix_sentinel_files_20260516T062655.log
projects/phase-gated-compound-sparse/logs/workers/worker_ops_c8_main_progress_20260516T061610_result.json
projects/phase-gated-compound-sparse/logs/workers/worker_ops_c8_main_progress_20260516T061610.log
projects/phase-gated-compound-sparse/checkpoints/gpqa_ds_importance_s015_QUEUED_20260516T061541.json
projects/phase-gated-compound-sparse/logs/workers/worker_analysis_c10_result_prep_20260516T060318.log
projects/phase-gated-compound-sparse/ROADMAP.md
projects/phase-gated-compound-sparse/decisions.yaml
projects/phase-gated-compound-sparse/logs/workers/worker_ops_post_restart_gpu_check_20260516T051659.log
projects/phase-gated-compound-sparse/checkpoints/gpqa_ds_importance_s015_PREPARING_20260516T051315.json
projects/phase-gated-compound-sparse/logs/workers/worker_code_gpqa_chat_template_support_20260516T050928_result.json
projects/phase-gated-compound-sparse/logs/workers/worker_code_gpqa_chat_template_support_20260516T050928.log
projects/phase-gated-compound-sparse/logs/workers/worker_research_gpqa_think_evaluation_20260516T045554.log
projects/phase-gated-compound-sparse/logs/chats/cron_hook_acc_qw_s020_n100_b2_fix.jsonl
projects/phase-gated-compound-sparse/task_context/history/agent/loop_14_1778942488.md
projects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_acc_qw_s020_n100_b2_fix_20260516T045621_114470.jsonl
projects/phase-gated-compound-sparse/logs/chats/cron_hook_acc_ds_s030_8k_v2.jsonl
projects/phase-gated-compound-sparse/task_context/history/agent/loop_14_1778907381.md
projects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_acc_ds_s030_8k_v2_20260516T045508_468184.jsonl
projects/phase-gated-compound-sparse/logs/chats/cron_hook_acc_qw_s020_b1_8k.jsonl
projects/phase-gated-compound-sparse/logs/workers/worker_ops_c8_s030_chain_setup_20260516T043746.log
projects/phase-gated-compound-sparse/logs/chats/cron_hook_gsm8k_qw_rand_s030.jsonl
projects/phase-gated-compound-sparse/task_context/history/agent/loop_14_1778907308.md
projects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_gsm8k_qw_rand_s030_20260516T043711_981237.jsonl
projects/phase-gated-compound-sparse/artifacts/review_issues.yaml
projects/phase-gated-compound-sparse/task_context/history/agent/loop_14_1778906231.md
projects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_acc_qw_s020_b1_8k_20260516T043158_294396.jsonl
projects/phase-gated-compound-sparse/logs/chats/worker_ops_c8_race_condition_fix_20260516T042414.jsonl
projects/phase-gated-compound-sparse/logs/workers/worker_ops_c8_race_condition_fix_20260516T042414.log
projects/phase-gated-compound-sparse/checkpoints/c8_llama_gpu0_s025_RUNNING_20260516T042616.json
projects/phase-gated-compound-sparse/logs/workers/worker_ops_verify_paper_and_update_memory_20260516T042142.log
projects/phase-gated-compound-sparse/checkpoints/c8_llama_gpu0_s025_ALLOCATED_20260516T042604.json
projects/phase-gated-compound-sparse/checkpoints/c8_llama_gpu0_s025_QUEUED_20260516T042600.json
projects/phase-gated-compound-sparse/memory.md
projects/phase-gated-compound-sparse/checkpoints/c8_llama_gpu0_s025_PREPARING_20260516T042553.json
projects/phase-gated-compound-sparse/logs/workers/worker_ops_c10_c8_progress_check_20260516T042155.log
projects/phase-gated-compound-sparse/logs/chats/cron_hook_acc_qw_s015_b1_8k.jsonl
projects/phase-gated-compound-sparse/logs/workers/worker_research_literature-linkage-dose-curve_20260516T041915.log
projects/phase-gated-compound-sparse/logs/chats/cron_hook_acc_qw_dense_b1_8k.jsonl
projects/phase-gated-compound-sparse/logs/workers/worker_ops_session16_gpu_diag_20260516T040904_result.json
projects/phase-gated-compound-sparse/logs/chats/worker_ops_session16_gpu_diag_20260516T040904.jsonl
projects/phase-gated-compound-sparse/logs/workers/worker_ops_session16_gpu_diag_20260516T040904.log
projects/phase-gated-compound-sparse/logs/chats/cron_hook_acc_qw_s025.jsonl
projects/phase-gated-compound-sparse/logs/workers/worker_ops_gpu_status_check_20260516T040752_result.json
projects/phase-gated-compound-sparse/logs/chats/worker_ops_gpu_status_check_20260516T040752.jsonl
projects/phase-gated-compound-sparse/logs/workers/worker_ops_gpu_status_check_20260516T040752.log
projects/phase-gated-compound-sparse/logs/chats/worker_code_c8_gpu0_s025_20260516T040415.jsonl
projects/phase-gated-compound-sparse/logs/workers/worker_code_c8_gpu0_s025_20260516T040415.log
projects/phase-gated-compound-sparse/logs/workers/worker_ops_gpu0_utilization_20260516T040159.log
projects/phase-gated-compound-sparse/logs/workers/worker_paper_section-corrections_20260516T034937.log
projects/phase-gated-compound-sparse/logs/workers/worker_paper_appendix_fixes_r10_20260516T035040.log
projects/phase-gated-compound-sparse/logs/chats/cron_hook_acc_qw_s020.jsonl
projects/phase-gated-compound-sparse/task_context/history/agent/loop_14_1778904783.md
projects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_acc_qw_s025_20260516T035032_441330.jsonl
projects/phase-gated-compound-sparse/logs/chats/cron_hook_acc_ds_s020.jsonl
projects/phase-gated-compound-sparse/task_context/history/agent/loop_14_1778903432.md
projects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_acc_qw_s020_20260516T034619_741921.jsonl
projects/phase-gated-compound-sparse/task_context/history/agent/loop_14_1778903179.md
projects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_acc_ds_s020_20260516T034501_894754.jsonl
projects/phase-gated-compound-sparse/logs/workers/worker_ops_download_figure1_20260516T034044.log
projects/phase-gated-compound-sparse/logs/chats/cron_hook_acc_ds_s015_8k_v2.jsonl
projects/phase-gated-compound-sparse/logs/chats/cron_hook_acc_ds_s025.jsonl
projects/phase-gated-compound-sparse/task_context/history/agent/loop_14_1778902593.md
projects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_acc_ds_s025_20260516T032919_426254.jsonl
projects/phase-gated-compound-sparse/logs/chats/cron_hook_acc_ds_s025_8k_v2.jsonl
projects/phase-gated-compound-sparse/checkpoints/c8_llama_n250_fixed_RUNNING_20260516T032445.json
projects/phase-gated-compound-sparse/checkpoints/c8_llama_n250_fixed_ALLOCATED_20260516T032425.json
projects/phase-gated-compound-sparse/checkpoints/c8_llama_n250_fixed_QUEUED_20260516T032420.json
projects/phase-gated-compound-sparse/checkpoints/c8_llama_n250_fixed_PENDING_20260516T032416.json
projects/phase-gated-compound-sparse/logs/workers/worker_code_c8_llama_n250_fix_20260516T031229_result.json
projects/phase-gated-compound-sparse/logs/workers/worker_code_c8_llama_n250_fix_20260516T031229.log
projects/phase-gated-compound-sparse/checkpoints/c10_lang_switching_DONE_20260516T031713.json
projects/phase-gated-compound-sparse/checkpoints/c10_lang_switching_DONE_20260516T031712.json
projects/phase-gated-compound-sparse/checkpoints/c10_lang_switching_DONE_20260516T031212.json
projects/phase-gated-compound-sparse/checkpoints/c8_llama_n250_DONE_20260516T031211.json
projects/phase-gated-compound-sparse/checkpoints/c10_lang_switching_RUNNING_20260516T031158.json
projects/phase-gated-compound-sparse/checkpoints/c8_llama_n250_RUNNING_20260516T031157.json
projects/phase-gated-compound-sparse/logs/workers/worker_analysis_c5_per_phase_gini_20260516T024150.log
projects/phase-gated-compound-sparse/logs/workers/worker_ops_kill_c10_and_check_data_20260516T025832_result.json
projects/phase-gated-compound-sparse/logs/chats/worker_ops_kill_c10_and_check_data_20260516T025832.jsonl
projects/phase-gated-compound-sparse/logs/workers/worker_ops_kill_c10_and_check_data_20260516T025832.log
projects/phase-gated-compound-sparse/logs/workers/worker_diagnose_c10_gpu_conflict_20260516T025710.log
projects/phase-gated-compound-sparse/logs/workers/worker_analysis_c4_think_validation_math500_20260516T024906.log
projects/phase-gated-compound-sparse/checkpoints/c10_lang_switching_RUNNING_20260516T025650.json
projects/phase-gated-compound-sparse/logs/workers/worker_registry_c3_llama_metrics_backfill_20260516T025245.log
projects/phase-gated-compound-sparse/logs/workers/worker_analysis_c10_lang_switching_20260516T024225.log
projects/phase-gated-compound-sparse/logs/chats/cron_hook_gsm8k_qw_rand_s025_v2.jsonl
projects/phase-gated-compound-sparse/logs/chats/cron_hook_gsm8k_profiling_qw.jsonl
projects/phase-gated-compound-sparse/task_context/history/agent/loop_14_1778899558.md
projects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_gsm8k_profiling_qw_20260516T024548_513211.jsonl
projects/phase-gated-compound-sparse/logs/chats/cron_hook_acc_ds_dense_8k_v2.jsonl
projects/phase-gated-compound-sparse/task_context/history/agent/loop_14_1778899548.md
projects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_acc_ds_dense_8k_v2_20260516T023952_496662.jsonl
projects/phase-gated-compound-sparse/task_context/history/director/loop_9.md
projects/phase-gated-compound-sparse/logs/chats/archive/feishu_group_oc_fdc656be1c7fe17c11ab639cdbce3710_director_20260516T023902_731152.jsonl
projects/phase-gated-compound-sparse/logs/workers/worker_code_c8_llama_n250_20260516T023333_result.json
projects/phase-gated-compound-sparse/logs/chats/worker_code_c8_llama_n250_20260516T023333.jsonl
projects/phase-gated-compound-sparse/logs/workers/worker_code_c8_llama_n250_20260516T023333.log
projects/phase-gated-compound-sparse/checkpoints/c8_llama_n250_RUNNING_20260516T023711.json
projects/phase-gated-compound-sparse/checkpoints/c8_llama_n250_QUEUED_20260516T023706.json
projects/phase-gated-compound-sparse/checkpoints/c8_llama_n250_PREPARING_20260516T023237.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fdd18231-ed2b-4223-94fa-905bc9eae802",
  "isSidechain": false,
  "promptId": "1b3ef117-44ac-4494-a1a3-d617fc268060",
  "type": "user",
  "uuid": "2b2c2bb2-910b-4bb7-ac54-95c225ab97f8",
  "toolUseResult": {
    "mode": "files_with_matches",
    "filenames": [
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/logs/phase2_worst_attempt0.log",
      "projects/phase-gated-compound-sparse/logs/chats/feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4.jsonl",
      "projects/phase-gated-compound-sparse/logs/workers/worker_ops_check_s030_gpu0_20260516T152633.log",
      "projects/phase-gated-compound-sparse/registry.yaml",
      "projects/phase-gated-compound-sparse/logs/chats/feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4_reviewer.jsonl",
      "projects/phase-gated-compound-sparse/logs/workers/worker_ops_gpqa_prep_remaining_20260516T152422_result.json",
      "projects/phase-gated-compound-sparse/report.md",
      "projects/phase-gated-compound-sparse/checkpoints/gpqa_ds_importance_s020_QUEUED_20260516T152623.json",
      "projects/phase-gated-compound-sparse/logs/workers/worker_ops_gpqa_prep_remaining_20260516T152422.log",
      "projects/phase-gated-compound-sparse/logs/chats/feishu_group_oc_fdc656be1c7fe17c11ab639cdbce3710_director.jsonl",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/logs/phase2_median_attempt0.log",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/logs/phase2_best_attempt0.log",
      "projects/phase-gated-compound-sparse/logs/workers/worker_ssh_c8_llama_n250_progress_check_20260516T150558_result.json",
      "projects/phase-gated-compound-sparse/logs/chats/worker_ssh_c8_llama_n250_progress_check_20260516T150558.jsonl",
      "projects/phase-gated-compound-sparse/logs/workers/worker_ssh_c8_llama_n250_progress_check_20260516T150558.log",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/logs/phase1_attempt0.log",
      "projects/phase-gated-compound-sparse/logs/ralph_loop_timeline.jsonl",
      "projects/phase-gated-compound-sparse/logs/chats/feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4_paper_agent.jsonl",
      "projects/phase-gated-compound-sparse/logs/chats/worker_ops_c8_main_progress_20260516T144339.jsonl",
      "projects/phase-gated-compound-sparse/logs/workers/worker_ops_c8_main_progress_20260516T144339.log",
      "projects/phase-gated-compound-sparse/task_context/agent.md",
      "projects/phase-gated-compound-sparse/logs/chats/archive/feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4_20260516T144128_862210.jsonl",
      "projects/phase-gated-compound-sparse/checkpoints/c8_llama_gpu0_s025_DONE_20260516T140444.json",
      "projects/phase-gated-compound-sparse/checkpoints/c8_llama_gpu0_s025_RUNNING_20260516T140438.json",
      "projects/phase-gated-compound-sparse/logs/workers/worker_ops_gpu_full_status_20260516T140155_result.json",
      "projects/phase-gated-compound-sparse/logs/workers/worker_ops_gpu_full_status_20260516T140155.log",
      "projects/phase-gated-compound-sparse/task_context/director.md",
      "projects/phase-gated-compound-sparse/logs/chats/archive/feishu_group_oc_fdc656be1c7fe17c11ab639cdbce3710_director_20260516T140226_790641.jsonl",
      "projects/phase-gated-compound-sparse/task_context/reviewer.md",
      "projects/phase-gated-compound-sparse/logs/chats/archive/feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4_reviewer_20260516T140222_348277.jsonl",
      "projects/phase-gated-compound-sparse/logs/chats/feishu_dm_oc_82773423f52f26bb5bf8c8f58f32dee0_briefer.jsonl",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/meta.yaml",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/logs/review_worst.log",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/worst/review_context.yaml",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/logs/review_median.log",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/median/review_context.yaml",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/logs/review_best.log",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/best/review_context.yaml",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/logs/paper_agent_worst.log",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/worst/experiment_data.json",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/worst/imagined_experiments.yaml",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/logs/paper_agent_median.log",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/median/experiment_data.json",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/median/imagined_experiments.yaml",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/logs/paper_agent_best.log",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/best/experiment_data.json",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/best/imagined_experiments.yaml",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/logs/phase2_worst_attempt0.log",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/logs/phase2_median_attempt0.log",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/logs/phase2_best_attempt0.log",
      "projects/phase-gated-compound-sparse/checkpoints/gpqa_ds_importance_s015_RUNNING_20260516T074332.json",
      "projects/phase-gated-compound-sparse/checkpoints/gpqa_ds_importance_s015_ALLOCATED_20260516T074301.json",
      "projects/phase-gated-compound-sparse/checkpoints/gpqa_ds_importance_s015_ALLOCATED_20260516T074222.json",
      "projects/phase-gated-compound-sparse/logs/chats/worker_ops_gpu_status_check_20260516T071711.jsonl",
      "projects/phase-gated-compound-sparse/logs/workers/worker_ops_gpu_status_check_20260516T071711.log",
      "projects/phase-gated-compound-sparse/logs/workers/worker_ops_restore_sentinel_files_20260516T062824.log",
      "projects/phase-gated-compound-sparse/logs/workers/worker_ops_fix_sentinel_files_20260516T062655_result.json",
      "projects/phase-gated-compound-sparse/logs/workers/worker_ops_fix_sentinel_files_20260516T062655.log",
      "projects/phase-gated-compound-sparse/logs/workers/worker_ops_c8_main_progress_20260516T061610_result.json",
      "projects/phase-gated-compound-sparse/logs/workers/worker_ops_c8_main_progress_20260516T061610.log",
      "projects/phase-gated-compound-sparse/checkpoints/gpqa_ds_importance_s015_QUEUED_20260516T061541.json",
      "projects/phase-gated-compound-sparse/logs/workers/worker_analysis_c10_result_prep_20260516T060318.log",
      "projects/phase-gated-compound-sparse/ROADMAP.md",
      "projects/phase-gated-compound-sparse/decisions.yaml",
      "projects/phase-gated-compound-sparse/logs/workers/worker_ops_post_restart_gpu_check_20260516T051659.log",
      "projects/phase-gated-compound-sparse/checkpoints/gpqa_ds_importance_s015_PREPARING_20260516T051315.json",
      "projects/phase-gated-compound-sparse/logs/workers/worker_code_gpqa_chat_template_support_20260516T050928_result.json",
      "projects/phase-gated-compound-sparse/logs/workers/worker_code_gpqa_chat_template_support_20260516T050928.log",
      "projects/phase-gated-compound-sparse/logs/workers/worker_research_gpqa_think_evaluation_20260516T045554.log",
      "projects/phase-gated-compound-sparse/logs/chats/cron_hook_acc_qw_s020_n100_b2_fix.jsonl",
      "projects/phase-gated-compound-sparse/task_context/history/agent/loop_14_1778942488.md",
      "projects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_acc_qw_s020_n100_b2_fix_20260516T045621_114470.jsonl",
      "projects/phase-gated-compound-sparse/logs/chats/cron_hook_acc_ds_s030_8k_v2.jsonl",
      "projects/phase-gated-compound-sparse/task_context/history/agent/loop_14_1778907381.md",
      "projects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_acc_ds_s030_8k_v2_20260516T045508_468184.jsonl",
      "projects/phase-gated-compound-sparse/logs/chats/cron_hook_acc_qw_s020_b1_8k.jsonl",
      "projects/phase-gated-compound-sparse/logs/workers/worker_ops_c8_s030_chain_setup_20260516T043746.log",
      "projects/phase-gated-compound-sparse/logs/chats/cron_hook_gsm8k_qw_rand_s030.jsonl",
      "projects/phase-gated-compound-sparse/task_context/history/agent/loop_14_1778907308.md",
      "projects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_gsm8k_qw_rand_s030_20260516T043711_981237.jsonl",
      "projects/phase-gated-compound-sparse/artifacts/review_issues.yaml",
      "projects/phase-gated-compound-sparse/task_context/history/agent/loop_14_1778906231.md",
      "projects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_acc_qw_s020_b1_8k_20260516T043158_294396.jsonl",
      "projects/phase-gated-compound-sparse/logs/chats/worker_ops_c8_race_condition_fix_20260516T042414.jsonl",
      "projects/phase-gated-compound-sparse/logs/workers/worker_ops_c8_race_condition_fix_20260516T042414.log",
      "projects/phase-gated-compound-sparse/checkpoints/c8_llama_gpu0_s025_RUNNING_20260516T042616.json",
      "projects/phase-gated-compound-sparse/logs/workers/worker_ops_verify_paper_and_update_memory_20260516T042142.log",
      "projects/phase-gated-compound-sparse/checkpoints/c8_llama_gpu0_s025_ALLOCATED_20260516T042604.json",
      "projects/phase-gated-compound-sparse/checkpoints/c8_llama_gpu0_s025_QUEUED_20260516T042600.json",
      "projects/phase-gated-compound-sparse/memory.md",
      "projects/phase-gated-compound-sparse/checkpoints/c8_llama_gpu0_s025_PREPARING_20260516T042553.json",
      "projects/phase-gated-compound-sparse/logs/workers/worker_ops_c10_c8_progress_check_20260516T042155.log",
      "projects/phase-gated-compound-sparse/logs/chats/cron_hook_acc_qw_s015_b1_8k.jsonl",
      "projects/phase-gated-compound-sparse/logs/workers/worker_research_literature-linkage-dose-curve_20260516T041915.log",
      "projects/phase-gated-compound-sparse/logs/chats/cron_hook_acc_qw_dense_b1_8k.jsonl",
      "projects/phase-gated-compound-sparse/logs/workers/worker_ops_session16_gpu_diag_20260516T040904_result.json",
      "projects/phase-gated-compound-sparse/logs/chats/worker_ops_session16_gpu_diag_20260516T040904.jsonl",
      "projects/phase-gated-compound-sparse/logs/workers/worker_ops_session16_gpu_diag_20260516T040904.log",
      "projects/phase-gated-compound-sparse/logs/chats/cron_hook_acc_qw_s025.jsonl",
      "projects/phase-gated-compound-sparse/logs/workers/worker_ops_gpu_status_check_20260516T040752_result.json",
      "projects/phase-gated-compound-sparse/logs/chats/worker_ops_gpu_status_check_20260516T040752.jsonl",
      "projects/phase-gated-compound-sparse/logs/workers/worker_ops_gpu_status_check_20260516T040752.log",
      "projects/phase-gated-compound-sparse/logs/chats/worker_code_c8_gpu0_s025_20260516T040415.jsonl",
      "projects/phase-gated-compound-sparse/logs/workers/worker_code_c8_gpu0_s025_20260516T040415.log",
      "projects/phase-gated-compound-sparse/logs/workers/worker_ops_gpu0_utilization_20260516T040159.log",
      "projects/phase-gated-compound-sparse/logs/workers/worker_paper_section-corrections_20260516T034937.log",
      "projects/phase-gated-compound-sparse/logs/workers/worker_paper_appendix_fixes_r10_20260516T035040.log",
      "projects/phase-gated-compound-sparse/logs/chats/cron_hook_acc_qw_s020.jsonl",
      "projects/phase-gated-compound-sparse/task_context/history/agent/loop_14_1778904783.md",
      "projects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_acc_qw_s025_20260516T035032_441330.jsonl",
      "projects/phase-gated-compound-sparse/logs/chats/cron_hook_acc_ds_s020.jsonl",
      "projects/phase-gated-compound-sparse/task_context/history/agent/loop_14_1778903432.md",
      "projects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_acc_qw_s020_20260516T034619_741921.jsonl",
      "projects/phase-gated-compound-sparse/task_context/history/agent/loop_14_1778903179.md",
      "projects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_acc_ds_s020_20260516T034501_894754.jsonl",
      "projects/phase-gated-compound-sparse/logs/workers/worker_ops_download_figure1_20260516T034044.log",
      "projects/phase-gated-compound-sparse/logs/chats/cron_hook_acc_ds_s015_8k_v2.jsonl",
      "projects/phase-gated-compound-sparse/logs/chats/cron_hook_acc_ds_s025.jsonl",
      "projects/phase-gated-compound-sparse/task_context/history/agent/loop_14_1778902593.md",
      "projects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_acc_ds_s025_20260516T032919_426254.jsonl",
      "projects/phase-gated-compound-sparse/logs/chats/cron_hook_acc_ds_s025_8k_v2.jsonl",
      "projects/phase-gated-compound-sparse/checkpoints/c8_llama_n250_fixed_RUNNING_20260516T032445.json",
      "projects/phase-gated-compound-sparse/checkpoints/c8_llama_n250_fixed_ALLOCATED_20260516T032425.json",
      "projects/phase-gated-compound-sparse/checkpoints/c8_llama_n250_fixed_QUEUED_20260516T032420.json",
      "projects/phase-gated-compound-sparse/checkpoints/c8_llama_n250_fixed_PENDING_20260516T032416.json",
      "projects/phase-gated-compound-sparse/logs/workers/worker_code_c8_llama_n250_fix_20260516T031229_result.json",
      "projects/phase-gated-compound-sparse/logs/workers/worker_code_c8_llama_n250_fix_20260516T031229.log",
      "projects/phase-gated-compound-sparse/checkpoints/c10_lang_switching_DONE_20260516T031713.json",
      "projects/phase-gated-compound-sparse/checkpoints/c10_lang_switching_DONE_20260516T031712.json",
      "projects/phase-gated-compound-sparse/checkpoints/c10_lang_switching_DONE_20260516T031212.json",
      "projects/phase-gated-compound-sparse/checkpoints/c8_llama_n250_DONE_20260516T031211.json",
      "projects/phase-gated-compound-sparse/checkpoints/c10_lang_switching_RUNNING_20260516T031158.json",
      "projects/phase-gated-compound-sparse/checkpoints/c8_llama_n250_RUNNING_20260516T031157.json",
      "projects/phase-gated-compound-sparse/logs/workers/worker_analysis_c5_per_phase_gini_20260516T024150.log",
      "projects/phase-gated-compound-sparse/logs/workers/worker_ops_kill_c10_and_check_data_20260516T025832_result.json",
      "projects/phase-gated-compound-sparse/logs/chats/worker_ops_kill_c10_and_check_data_20260516T025832.jsonl",
      "projects/phase-gated-compound-sparse/logs/workers/worker_ops_kill_c10_and_check_data_20260516T025832.log",
      "projects/phase-gated-compound-sparse/logs/workers/worker_diagnose_c10_gpu_conflict_20260516T025710.log",
      "projects/phase-gated-compound-sparse/logs/workers/worker_analysis_c4_think_validation_math500_20260516T024906.log",
      "projects/phase-gated-compound-sparse/checkpoints/c10_lang_switching_RUNNING_20260516T025650.json",
      "projects/phase-gated-compound-sparse/logs/workers/worker_registry_c3_llama_metrics_backfill_20260516T025245.log",
      "projects/phase-gated-compound-sparse/logs/workers/worker_analysis_c10_lang_switching_20260516T024225.log",
      "projects/phase-gated-compound-sparse/logs/chats/cron_hook_gsm8k_qw_rand_s025_v2.jsonl",
      "projects/phase-gated-compound-sparse/logs/chats/cron_hook_gsm8k_profiling_qw.jsonl",
      "projects/phase-gated-compound-sparse/task_context/history/agent/loop_14_1778899558.md",
      "projects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_gsm8k_profiling_qw_20260516T024548_513211.jsonl",
      "projects/phase-gated-compound-sparse/logs/chats/cron_hook_acc_ds_dense_8k_v2.jsonl",
      "projects/phase-gated-compound-sparse/task_context/history/agent/loop_14_1778899548.md",
      "projects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_acc_ds_dense_8k_v2_20260516T023952_496662.jsonl",
      "projects/phase-gated-compound-sparse/task_context/history/director/loop_9.md",
      "projects/phase-gated-compound-sparse/logs/chats/archive/feishu_group_oc_fdc656be1c7fe17c11ab639cdbce3710_director_20260516T023902_731152.jsonl",
      "projects/phase-gated-compound-sparse/logs/workers/worker_code_c8_llama_n250_20260516T023333_result.json",
      "projects/phase-gated-compound-sparse/logs/chats/worker_code_c8_llama_n250_20260516T023333.jsonl",
      "projects/phase-gated-compound-sparse/logs/workers/worker_code_c8_llama_n250_20260516T023333.log",
      "projects/phase-gated-compound-sparse/checkpoints/c8_llama_n250_RUNNING_20260516T023711.json",
      "projects/phase-gated-compound-sparse/checkpoints/c8_llama_n250_QUEUED_20260516T023706.json",
      "projects/phase-gated-compound-sparse/checkpoints/c8_llama_n250_PREPARING_20260516T023237.json"
    ],
    "numFiles": 157
  },
  "sourceToolAssistantUUID": "fdd18231-ed2b-4223-94fa-905bc9eae802",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "a3d601b9-90d6-4700-8195-7ac8fe55805b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-16T15:27:05.065Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01MxzxWvmaQshKy23RcTok6u`</summary>

```json
{
  "pattern": "status: planned|status: PLANNED|status: RUNNING",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b2c2bb2-910b-4bb7-ac54-95c225ab97f8",
  "isSidechain": false,
  "requestId": "req_011Cb6UaEYue5peJQxGzHNGs",
  "type": "assistant",
  "uuid": "e806f36d-deb1-4600-9ff0-5cdacebb461f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "a3d601b9-90d6-4700-8195-7ac8fe55805b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JD1LoBimaCubQrtTCNrvj5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3738,
      "cache_read_input_tokens": 68688,
      "output_tokens": 17273,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3738,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 17273,
          "cache_read_input_tokens": 68688,
          "cache_creation_input_tokens": 3738,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3738
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

_source line 17_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：LLaMA n=250 高功效确认 strategy×phase 交互在 Llama 架构上可忽略；random phase gradient 稳健。GPQA 不显著或方向不一致。'Strategy-gated' 叙事崩塌——phase modulation 普遍存在但非 strategy-specific…",
  "leafUuid": "e806f36d-deb1-4600-9ff0-5cdacebb461f",
  "sessionId": "a3d601b9-90d6-4700-8195-7ac8fe55805b"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Phase-dependent compound sparsity in reasoning models",
  "sessionId": "a3d601b9-90d6-4700-8195-7ac8fe55805b"
}
```

---

### Tool result

_source line 19 · 2026-05-16T15:27:05.382Z_

<details><summary>↩ Tool result · `toolu_01MxzxWvmaQshKy23RcTok6u`</summary>

```text
&lt;persisted-output>
Output too large (31.9KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11/a3d601b9-90d6-4700-8195-7ac8fe55805b/tool-results/toolu_01MxzxWvmaQshKy23RcTok6u.txt

Preview (first 2KB):
projects/phase-gated-compound-sparse/experiment_plan.yaml:293:    status: planned
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T143543/logs/phase2_worst_attempt0.log:10:[Omitted long matching line]
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T143543/logs/phase2_worst_attempt0.log:15:[Omitted long matching line]
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T143543/logs/phase2_median_attempt0.log:22:[Omitted long matching line]
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T143543/logs/phase2_median_attempt0.log:28:[Omitted long matching line]
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T143543/logs/phase2_median_attempt0.log:44:[Omitted long matching line]
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T143543/logs/phase2_median_attempt0.log:45:[Omitted long matching line]
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T143543/logs/phase2_best_attempt0.log:5:[Omitted long matching line]
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T143543/logs/phase2_best_attempt0.log:6:[Omitted long matching line]
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T143543/logs/phase2_best_attempt0.log:7:[Omitted long matching line]
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T143543/logs/phase2_best_attempt0.log:31:[Omitted long matching line]
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T143543/logs/phase2_best_attempt0.log:37:[Omitted long matching line]
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T143543/logs/phase2_best_attempt0.log:49:[Omitted long matching line]
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T143543/logs/phase2_best_attempt0.log:61:[Omitted long matching line]
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e806f36d-deb1-4600-9ff0-5cdacebb461f",
  "isSidechain": false,
  "promptId": "1b3ef117-44ac-4494-a1a3-d617fc268060",
  "type": "user",
  "uuid": "fce1f3f6-c59d-4197-a68b-98c344c81934",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "projects/phase-gated-compound-sparse/experiment_plan.yaml:293:    status: planned\nprojects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T143543/logs/phase2_worst_attempt0.log:10:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T143543/logs/phase2_worst_attempt0.log:15:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T143543/logs/phase2_median_attempt0.log:22:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T143543/logs/phase2_median_attempt0.log:28:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T143543/logs/phase2_median_attempt0.log:44:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T143543/logs/phase2_median_attempt0.log:45:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T143543/logs/phase2_best_attempt0.log:5:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T143543/logs/phase2_best_attempt0.log:6:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T143543/logs/phase2_best_attempt0.log:7:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T143543/logs/phase2_best_attempt0.log:31:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T143543/logs/phase2_best_attempt0.log:37:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T143543/logs/phase2_best_attempt0.log:49:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T143543/logs/phase2_best_attempt0.log:61:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T143543/logs/phase2_best_attempt0.log:63:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T143543/logs/phase2_best_attempt0.log:65:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/logs/phase2_worst_attempt0.log:27:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/logs/phase2_worst_attempt0.log:30:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/logs/phase2_worst_attempt0.log:39:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/logs/phase2_worst_attempt0.log:42:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/logs/phase2_worst_attempt0.log:45:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/logs/phase2_worst_attempt0.log:48:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/logs/phase2_worst_attempt0.log:51:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/logs/phase2_worst_attempt0.log:58:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/logs/phase2_best_attempt0.log:24:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T054026/logs/phase2_worst_attempt0.log:15:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T054026/logs/phase2_worst_attempt0.log:21:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T054026/logs/phase2_worst_attempt0.log:28:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T054026/logs/phase2_median_attempt0.log:26:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T054026/logs/phase2_median_attempt0.log:33:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T054026/logs/phase2_median_attempt0.log:43:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T054026/logs/phase2_best_attempt0.log:33:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T054026/logs/phase2_best_attempt0.log:50:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T054026/logs/phase2_best_attempt0.log:62:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T054026/logs/phase2_best_attempt0.log:65:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T054026/logs/phase2_best_attempt0.log:66:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T054026/logs/phase2_best_attempt0.log:81:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260514T054026/logs/phase2_best_attempt0.log:125:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/logs/phase2_worst_attempt0.log:3:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/logs/phase2_worst_attempt0.log:12:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/logs/phase2_worst_attempt0.log:18:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/logs/phase2_median_attempt0.log:10:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/logs/phase2_median_attempt0.log:11:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/logs/phase2_median_attempt0.log:16:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/logs/phase2_median_attempt0.log:20:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/logs/phase2_best_attempt0.log:4:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/logs/phase2_best_attempt0.log:5:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/logs/phase2_best_attempt0.log:7:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/logs/phase2_best_attempt0.log:13:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/logs/phase2_best_attempt0.log:14:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/logs/phase2_best_attempt0.log:16:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/logs/phase2_best_attempt0.log:19:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/registry.yaml:6645:    status: RUNNING\nprojects/phase-gated-compound-sparse/registry.yaml:6783:    status: RUNNING\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_v4c_r2_20260514T192337_440146.jsonl:75:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_ii_profiling_v4c_20260514T153335_689313.jsonl:40:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_ii_profiling_v4c_20260514T153335_689313.jsonl:51:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/feishu_group_oc_fdc656be1c7fe17c11ab639cdbce3710_director_20260514T053100_914965.jsonl:69:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/feishu_group_oc_fdc656be1c7fe17c11ab639cdbce3710_director_20260514T053100_914965.jsonl:287:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_v5_random_s030_20260515T005233_487896.jsonl:38:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_ii_profiling_v4_20260514T053849_262501.jsonl:67:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_v4b_r2_20260514T183856_124442.jsonl:17:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_bf16_ds_rand_s020_20260514T204036_873452.jsonl:53:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_bf16_ds_rand_s020_20260514T204036_873452.jsonl:65:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_ii_profiling_v4-random_20260514T183917_693546.jsonl:17:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_v6_random_s015_20260514T220242_840298.jsonl:50:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_c2_qw_n500_20260514T173702_871564.jsonl:78:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_acc_qw_s020_20260516T002415_946129.jsonl:55:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_acc_qw_s020_20260516T002415_946129.jsonl:64:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_v4a_r2_20260514T192227_357866.jsonl:46:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_ii_profiling_v2_20260515T043754_472588.jsonl:25:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_v6_random_s030_20260514T153236_148263.jsonl:83:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_interaction_index_profiling_20260514T183842_016512.jsonl:52:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_interaction_index_profiling_20260514T183842_016512.jsonl:56:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_interaction_index_profiling_20260514T183842_016512.jsonl:62:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_interaction_index_profiling_20260514T183842_016512.jsonl:64:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_interaction_index_profiling_20260514T183842_016512.jsonl:66:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_ii_profiling_v4c_20260514T221821_223315.jsonl:48:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_ii_profiling_v4c_20260514T221821_223315.jsonl:50:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_ii_profiling_v4_20260514T161542_711657.jsonl:112:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_ii_profiling_v4_20260514T161542_711657.jsonl:128:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_ii_profiling_v4b_20260515T013327_140965.jsonl:29:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_bf16_importance_s020_20260514T224640_748959.jsonl:80:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_v5_random_s025_20260515T013319_531789.jsonl:49:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_v5_random_s025_20260515T013319_531789.jsonl:55:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_v6_random_s020_20260515T013337_597190.jsonl:37:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_v6_random_s020_20260515T013337_597190.jsonl:39:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_v6_random_s020_20260515T013337_597190.jsonl:41:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_v6_random_s020_20260514T091131_374671.jsonl:106:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_v6_random_s030_20260514T214514_712081.jsonl:48:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_bf16_ds_rand_s015_20260515T013344_317282.jsonl:51:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_bf16_ds_rand_s015_20260515T013344_317282.jsonl:63:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_v4c_r2_20260514T223154_568735.jsonl:93:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4_20260516T002234_304642.jsonl:993:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4_reviewer_20260516T140222_348277.jsonl:243:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4_reviewer_20260514T024645_006577.jsonl:1410:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_v6_random_s030_20260514T183647_510985.jsonl:53:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_v6_random_s015_20260514T091531_094726.jsonl:66:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_ii_profiling_v4-random_20260514T053215_710532.jsonl:61:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4_20260514T122403_227655.jsonl:503:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4_20260514T122403_227655.jsonl:939:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4_20260514T122403_227655.jsonl:941:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4_20260514T122403_227655.jsonl:1017:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4_20260514T122403_227655.jsonl:1862:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_c4_entropy_20260515T005130_872647.jsonl:44:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_ii_profiling_v4-random_20260514T153412_443992.jsonl:54:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_ii_profiling_v4-random_20260514T153412_443992.jsonl:64:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_ii_profiling_v4-random_20260514T153412_443992.jsonl:99:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_bf16_qw_imp_s025_20260514T224515_033481.jsonl:17:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_ii_profiling_v4b_20260514T161557_389936.jsonl:103:{\"ts\": \"2026-05-14T16:14:32.093644+00:00\", \"role\": \"tool_result\", \"session\": \"cron:hook:mvp_ii_profiling_v4b\", \"text\": \"Type of experiments: &lt;class 'dict'>\\nKey: c2_ds_n500, Value type: &lt;class 'dict'>\\n  status: DONE\\nKey: c3_llama_arch, Value type: &lt;class 'dict'>\\n  status: DONE\\nKey: c2_n500_deepseek, Value type: &lt;class 'dict'>\\n  status: RUNNING\", \"tool\": \"Bash\", \"elapsed_ms\": 101}\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_ii_profiling_v4b_20260514T161557_389936.jsonl:105:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_v4b_r2_20260514T055816_812106.jsonl:103:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_interaction_index_profiling_20260515T042010_544353.jsonl:123:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4_reviewer_20260514T082159_969842.jsonl:543:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4_reviewer_20260514T082159_969842.jsonl:1496:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4_reviewer_20260514T082159_969842.jsonl:1510:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_ii_profiling_v4_20260514T090244_956480.jsonl:92:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_v6_random_s030_r3_20260514T122511_384902.jsonl:63:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_v6_random_s020_20260514T185944_867547.jsonl:69:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4_20260515T120125_855041.jsonl:350:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_v5_random_s020_20260514T214455_865770.jsonl:59:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_v5_random_s020_20260514T214455_865770.jsonl:70:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_v5_random_s030_20260514T214554_076198.jsonl:43:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_v5_random_s030_20260514T214554_076198.jsonl:58:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/workers/worker_knowledge_d052-framing-update_20260514T143357.log:9:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/workers/worker_knowledge_d052-framing-update_20260514T143357.log:17:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/workers/worker_knowledge_d052-framing-update_20260514T143357.log:22:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/workers/worker_knowledge_d052-framing-update_20260514T143357.log:24:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/workers/worker_knowledge_d052-framing-update_20260514T143357.log:25:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/workers/worker_knowledge_d052-framing-update_20260514T143357.log:30:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4_20260516T144128_862210.jsonl:813:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4_20260516T144128_862210.jsonl:1072:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4_20260516T144128_862210.jsonl:1083:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_gsm8k_profiling_ds_20260515T224722_364905.jsonl:55:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_v6_random_s030_r3_20260515T013324_598744.jsonl:61:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_v4c_r2_20260514T161611_420589.jsonl:90:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_v5_random_s025_20260514T153248_881249.jsonl:59:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_v6_random_s015_20260515T013340_915980.jsonl:37:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_v6_random_s015_20260515T013340_915980.jsonl:80:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_v4b_r2_20260514T153303_033083.jsonl:67:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_ii_profiling_v4c_20260514T122354_130251.jsonl:91:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_ii_profiling_v4c_20260514T122354_130251.jsonl:119:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_ii_profiling_v4c_20260514T122354_130251.jsonl:127:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_bf16_importance_s020_20260514T161610_236116.jsonl:48:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_bf16_importance_s020_20260514T161610_236116.jsonl:72:{\"ts\": \"2026-05-14T16:14:40.615070+00:00\", \"role\": \"tool\", \"session\": \"cron:hook:bf16_importance_s020\", \"text\": \"called Bash\", \"tool\": \"Bash\", \"tool_args\": {\"command\": \"grep -A 5 \\\"status: RUNNING\\\\|status: PENDING\\\\|status: PREPARING\\\\|status: QUEUED\\\\|status: ALLOCATED\\\" /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/registry.yaml | head -100\", \"description\": \"Find all non-terminal experiments\"}}\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_bf16_importance_s020_20260514T161610_236116.jsonl:73:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_bf16_importance_s020_20260514T161610_236116.jsonl:77:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_bf16_importance_s020_20260514T161610_236116.jsonl:79:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_bf16_importance_s020_20260514T161610_236116.jsonl:81:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_bf16_importance_s020_20260514T161610_236116.jsonl:85:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4_reviewer_20260514T122733_670530.jsonl:244:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4_reviewer_20260514T122733_670530.jsonl:397:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4_reviewer_20260514T122733_670530.jsonl:473:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4_reviewer_20260514T122733_670530.jsonl:497:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4_reviewer_20260514T122733_670530.jsonl:506:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4_reviewer_20260514T122733_670530.jsonl:515:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4_reviewer_20260514T122733_670530.jsonl:529:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4_reviewer_20260514T122733_670530.jsonl:545:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4_reviewer_20260514T122733_670530.jsonl:561:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4_reviewer_20260514T122733_670530.jsonl:646:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4_reviewer_20260514T122733_670530.jsonl:675:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4_20260514T192023_063195.jsonl:1597:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4_20260514T192023_063195.jsonl:1603:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4_20260514T192023_063195.jsonl:1630:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4_20260514T192023_063195.jsonl:1638:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4_20260514T192023_063195.jsonl:1650:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4_20260514T192023_063195.jsonl:1657:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4_20260514T192023_063195.jsonl:2119:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_acc_qw_s025_20260516T002640_858115.jsonl:59:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_v5_random_s020_20260515T005103_569594.jsonl:41:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_v4b_r2_20260515T013330_084396.jsonl:43:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_v5_random_s015_20260514T225153_684852.jsonl:42:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_ii_profiling_v2_20260514T161630_038754.jsonl:50:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_ii_profiling_v2_20260514T161630_038754.jsonl:53:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_v4c_r2_20260515T013708_444866.jsonl:55:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_acc_qw_s020_n100_b2_fix_20260516T045621_114470.jsonl:89:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_ii_profiling_v4_20260514T192910_037867.jsonl:137:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_interaction_index_profiling_20260514T214544_629263.jsonl:44:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_interaction_index_profiling_20260514T214544_629263.jsonl:68:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_interaction_index_profiling_20260514T214544_629263.jsonl:93:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_interaction_index_profiling_20260514T214544_629263.jsonl:107:{\"ts\": \"2026-05-14T21:44:35.136646+00:00\", \"role\": \"tool_result\", \"session\": \"cron:hook:mvp_interaction_index_profiling\", \"text\": \"4167:  c2_n500_deepseek:\\n4168-    status: RUNNING\\n4169-    retry_count: 0\\n4170-    created_at: '2026-05-14T13:33:50.628Z'\\n--\\n4350:  c2_qw_n500_r3:\\n4351-    status: RUNNING\\n4352-    retry_count: 0\\n4353-    created_at: '2026-05-14T19:26:53.700Z'\", \"tool\": \"Grep\", \"elapsed_ms\": 53}\nprojects/phase-gated-compound-sparse/logs/chats/archive/feishu_group_oc_fdc656be1c7fe17c11ab639cdbce3710_director_20260515T103054_664948.jsonl:109:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/feishu_group_oc_fdc656be1c7fe17c11ab639cdbce3710_director_20260515T103054_664948.jsonl:2696:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_v5_random_s030_20260514T173600_009630.jsonl:77:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_v5_random_s030_20260514T173600_009630.jsonl:83:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_v6_random_s030_20260515T005156_345388.jsonl:56:{\"ts\": \"2026-05-15T00:50:08.798454+00:00\", \"role\": \"tool\", \"session\": \"cron:hook:v6_random_s030\", \"text\": \"called Grep\", \"tool\": \"Grep\", \"tool_args\": {\"pattern\": \"status: RUNNING\", \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/registry.yaml\", \"output_mode\": \"content\", \"-B\": \"2\", \"-A\": \"5\"}}\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_v6_random_s030_20260515T005156_345388.jsonl:57:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_v6_random_s030_20260515T005156_345388.jsonl:61:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_v6_random_s030_20260515T005156_345388.jsonl:63:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_c4_entropy_20260514T214413_581576.jsonl:17:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_ii_profiling_v4-random_20260514T214425_731499.jsonl:49:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_ii_profiling_v4b_20260514T061756_417000.jsonl:56:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/archive/cron_hook_mvp_ii_profiling_v4_20260515T013803_907005.jsonl:20:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/chats/feishu_group_oc_b6401b894d32f1aac1ce3e54ce0d0bd4_paper_agent.jsonl:3691:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/workers/worker_research_paper-writing-prep_20260514T051718.log:51:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/workers/worker_research_paper-writing-prep_20260514T051718.log:54:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/workers/worker_knowledge_experiment_plan_yaml_20260516T002829.log:40:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/workers/worker_knowledge_experiment_plan_yaml_20260516T002829.log:50:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/workers/worker_knowledge_experiment_plan_yaml_20260516T002829.log:53:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/workers/worker_knowledge_experiment_plan_yaml_20260516T002829.log:55:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/workers/worker_knowledge_experiment_plan_yaml_20260516T002829.log:56:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/workers/worker_knowledge_experiment_plan_yaml_20260516T002829.log:63:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/workers/worker_knowledge_experiment_plan_yaml_20260516T002829.log:66:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/workers/worker_knowledge_experiment_plan_yaml_20260516T002829.log:67:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/workers/worker_prep_c5b-pilot-design_20260514T144238.log:25:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/workers/worker_edit_d052-framing-plan-update_20260514T143137.log:9:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/workers/worker_edit_d052-framing-plan-update_20260514T143137.log:16:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/workers/worker_edit_d052-framing-plan-update_20260514T143137.log:17:[Omitted long matching line]\nprojects/phase-gated-compound-sparse/logs/workers/worker_writing_paper-methodology_20260514T052759.log:28:[Omitted long matching line]",
    "numLines": 209
  },
  "sourceToolAssistantUUID": "e806f36d-deb1-4600-9ff0-5cdacebb461f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "a3d601b9-90d6-4700-8195-7ac8fe55805b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：LLaMA n=250 高功效确认 strategy×phase 交互在 Llama 架构上可忽略；random phase gradient 稳健。GPQA 不显著或方向不一致。'Strategy-gated' 叙事崩塌——phase modulation 普遍存在但非 strategy-specific…",
  "leafUuid": "fce1f3f6-c59d-4197-a68b-98c344c81934",
  "sessionId": "a3d601b9-90d6-4700-8195-7ac8fe55805b"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Phase-dependent compound sparsity in reasoning models",
  "sessionId": "a3d601b9-90d6-4700-8195-7ac8fe55805b"
}
```

---

### Assistant

_source line 22 · 2026-05-16T15:27:11.318Z_

<details><summary>Logged reasoning block</summary>

```text
Let me check the experiment_plan.yaml for the planned experiment at line 293, and also check for GPQA queued experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fce1f3f6-c59d-4197-a68b-98c344c81934",
  "isSidechain": false,
  "requestId": "req_011Cb6UxA8MpjchzJqURV1NU",
  "type": "assistant",
  "uuid": "dc4e493b-ed13-4218-bf17-9396c71a30e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "a3d601b9-90d6-4700-8195-7ac8fe55805b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y2HjBcfegVyhqsMLVVpNZK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23790,
      "cache_read_input_tokens": 72426,
      "output_tokens": 257,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23790,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 257,
          "cache_read_input_tokens": 72426,
          "cache_creation_input_tokens": 23790,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23790
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

_source line 23 · 2026-05-16T15:27:12.300Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QP9pWEtDw7KvCq6BhLhLSS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/experiment_plan.yaml",
  "offset": 280,
  "limit": 40
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc4e493b-ed13-4218-bf17-9396c71a30e6",
  "isSidechain": false,
  "requestId": "req_011Cb6UxA8MpjchzJqURV1NU",
  "type": "assistant",
  "uuid": "96a76e13-a711-4904-85c2-65a84b29006e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "a3d601b9-90d6-4700-8195-7ac8fe55805b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y2HjBcfegVyhqsMLVVpNZK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23790,
      "cache_read_input_tokens": 72426,
      "output_tokens": 257,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23790,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 257,
          "cache_read_input_tokens": 72426,
          "cache_creation_input_tokens": 23790,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23790
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

_source line 24 · 2026-05-16T15:27:12.310Z_

<details><summary>↩ Tool result · `toolu_01QP9pWEtDw7KvCq6BhLhLSS`</summary>

```text
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
  "parentUuid": "96a76e13-a711-4904-85c2-65a84b29006e",
  "isSidechain": false,
  "promptId": "1b3ef117-44ac-4494-a1a3-d617fc268060",
  "type": "user",
  "uuid": "848d4f1f-b8a9-4525-9fd0-be019dca118c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/experiment_plan.yaml",
      "content": "    description: Phase-aware mitigation recovers compound degradation\n    status: future_work\n  C6:\n    description: Severity gradient is sub-exponential\n    status: confirmed\n  C7:\n    description: Statistical power at n=500 confirms dose-response\n    status: running\n  C8:\n    description: Cross-architecture validation (LLaMA)\n    status: partially_confirmed\n  C9:\n    description: Differentiation from Lethe/SparK prior work\n    status: planned\n  C10:\n    description: Phase gradient cross-benchmark robust; strategy specificity task-modulated\n    status: running\n  S3->C:\n    description: Onset threshold is model-dependent\n    status: confirmed\n  S7->C:\n    description: Dose-response monotonicity (Spearman rho=1.0)\n    status: confirmed\n",
      "numLines": 24,
      "startLine": 280,
      "totalLines": 303
    }
  },
  "sourceToolAssistantUUID": "96a76e13-a711-4904-85c2-65a84b29006e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "a3d601b9-90d6-4700-8195-7ac8fe55805b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-16T15:27:13.321Z_

<details><summary>↩ Tool result · `toolu_017Ay5MQSBMH7Lo23NfQW79i`</summary>

```text
1	{
2	  "exp_id": "gpqa_ds_importance_s020",
3	  "project": "phase-gated-compound-sparse",
4	  "state": "QUEUED",
5	  "previous_state": "PREPARING",
6	  "experiment_data": {
7	    "status": "QUEUED",
8	    "retry_count": 0,
9	    "created_at": "2026-05-16T15:26:23.378Z",
10	    "updated_at": "2026-05-16T15:26:23.378Z"
11	  },
12	  "timestamp": "2026-05-16T15:26:23.731186+00:00",
13	  "trigger": "update_registry"
14	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5116661c-6cb3-4067-95d2-ae3c60d7798e",
  "isSidechain": false,
  "promptId": "1b3ef117-44ac-4494-a1a3-d617fc268060",
  "type": "user",
  "uuid": "e8c1caad-8cdd-43d6-a86d-8a932d806649",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/checkpoints/gpqa_ds_importance_s020_QUEUED_20260516T152623.json",
      "content": "{\n  \"exp_id\": \"gpqa_ds_importance_s020\",\n  \"project\": \"phase-gated-compound-sparse\",\n  \"state\": \"QUEUED\",\n  \"previous_state\": \"PREPARING\",\n  \"experiment_data\": {\n    \"status\": \"QUEUED\",\n    \"retry_count\": 0,\n    \"created_at\": \"2026-05-16T15:26:23.378Z\",\n    \"updated_at\": \"2026-05-16T15:26:23.378Z\"\n  },\n  \"timestamp\": \"2026-05-16T15:26:23.731186+00:00\",\n  \"trigger\": \"update_registry\"\n}",
      "numLines": 14,
      "startLine": 1,
      "totalLines": 14
    }
  },
  "sourceToolAssistantUUID": "5116661c-6cb3-4067-95d2-ae3c60d7798e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "a3d601b9-90d6-4700-8195-7ac8fe55805b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-16T15:27:13.303Z_

<details open><summary>🔧 Tool call — Read · `toolu_017Ay5MQSBMH7Lo23NfQW79i`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/checkpoints/gpqa_ds_importance_s020_QUEUED_20260516T152623.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "848d4f1f-b8a9-4525-9fd0-be019dca118c",
  "isSidechain": false,
  "requestId": "req_011Cb6UxA8MpjchzJqURV1NU",
  "type": "assistant",
  "uuid": "5116661c-6cb3-4067-95d2-ae3c60d7798e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "a3d601b9-90d6-4700-8195-7ac8fe55805b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y2HjBcfegVyhqsMLVVpNZK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23790,
      "cache_read_input_tokens": 72426,
      "output_tokens": 257,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23790,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 257,
          "cache_read_input_tokens": 72426,
          "cache_creation_input_tokens": 23790,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23790
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

_source line 27 · 2026-05-16T15:27:13.406Z_

````json
{
  "parentUuid": "e8c1caad-8cdd-43d6-a86d-8a932d806649",
  "isSidechain": false,
  "attachment": {
    "type": "nested_memory",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/CLAUDE.md",
    "content": {
      "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/CLAUDE.md",
      "type": "Project",
      "content": "## 当前项目\n当前绑定项目：**phase-gated-compound-sparse**\n\n## 按需查阅\n- 项目配置：`load_project_config(\"phase-gated-compound-sparse\")` 或 `load_project_config(\"phase-gated-compound-sparse\", section=\"execution\")`\n- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）\n- 路线图：`read_roadmap()` 读取研究方向和短期任务\n- 产出目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/`（写文件后用 `register_artifact` 注册）\n\n## Worker 操作规范\n\n### ssh-env-setup\n\n# 远程服务器环境搭建规范\n\n## 核心原则\n\n**先探测，再安装。** 不要假设服务器上什么都没有——很多包已经装好了。安装前必须走 discovery 流程。\n\n**镜像快速路径**：连接服务器后，先用 `detect_image` 检测是否为预置镜像。如果是已知镜像且版本匹配，跳过基础环境搭建（Phase 1-4），直接安装项目特有依赖。未检测到镜像时走传统流程。\n\n**aml-train 镜像使用 conda 环境**（不是 venv）。环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`。pip/python 在 `/root/miniconda3/bin/` 下。**不要假设 .venv 存在，不要创建 venv。**\n\n## Phase 1: 环境探测（用 ssh_read_only）\n\n连接到服务器后，第一步永远是收集信息，不要直接装东西：\n\n```bash\n# 1. Python 环境\nwhich python3 && python3 --version\npip3 --version 2>/dev/null || echo \"NO_PIP\"\n\n# 2. CUDA 环境\nnvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader 2>/dev/null || echo \"NO_GPU\"\nnvcc --version 2>/dev/null | grep \"release\" || echo \"NO_NVCC\"\n\n# 3. 包管理器\nls -d /opt/miniconda3 ~/miniconda3 ~/.conda 2>/dev/null || echo \"NO_CONDA\"\nls -d .venv venv env 2>/dev/null || echo \"NO_VENV\"\npip3 list --format=freeze 2>/dev/null | grep -iE \"torch|transformers|flash\" || echo \"NO_ML_PKGS\"\n\n# 4. PEP 668 检查\npython3 -c \"import sysconfig; print(sysconfig.get_path('stdlib'))\" 2>/dev/null\nls /usr/lib/python*/EXTERNALLY-MANAGED 2>/dev/null && echo \"PEP668_MANAGED\" || echo \"PEP668_OK\"\n```\n\n根据探测结果决定安装策略，不要猜。\n\n## Phase 2: 环境策略选择\n\n根据 Phase 1 结果选择**一个**策略，不要混用：\n\n| 探测结果 | 策略 | 说明 |\n|----------|------|------|\n| 项目目录有 `.venv/` | 用它：`source .venv/bin/activate` | 最优先 |\n| 有 conda 且有写权限 | `conda activate base` 或创建专属 env | 次优先 |\n| PEP668_MANAGED + 无 venv | 创建 venv：`python3 -m venv .venv && source .venv/bin/activate` | 不要用 --break-system-packages |\n| PEP668_OK（无保护） | 直接 `pip install`（旧系统） | 仍建议 venv |\n\n**决不混用 conda install + pip install 到同一环境。** 选了 pip 就全用 pip。\n\n## Phase 3: PyTorch 安装\n\n### CUDA 版本映射（2025-2026 常用）\n\n先从 `nvcc --version` 或 `nvidia-smi` 获取 CUDA 版本，然后匹配：\n\n| CUDA 版本 | PyTorch pip index URL | 推荐 torch 版本 |\n|-----------|----------------------|-----------------|\n| 11.8 | `https://download.pytorch.org/whl/cu118` | ≥ 2.0 |\n| 12.1 | `https://download.pytorch.org/whl/cu121` | ≥ 2.1 |\n| 12.4 | `https://download.pytorch.org/whl/cu124` | ≥ 2.4 |\n| 12.6 | `https://download.pytorch.org/whl/cu126` | ≥ 2.6 |\n\n**不要猜版本号。** 如果不确定可用版本：\n```bash\npip index versions torch --index-url https://download.pytorch.org/whl/cu121 2>/dev/null | head -3\n```\n\n安装命令：\n```bash\npip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu{CUDA_SHORT}\n```\n\n### 大包超时处理\n\nPyTorch wheel 约 500MB-2GB，默认 SSH 超时可能不够。策略：\n\n```bash\n# 方法 1: nohup + 轮询（推荐）\nnohup pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 > /tmp/pip_install.log 2>&1 &\necho $!  # 记录 PID\n\n# 后续用 ssh_read_only 轮询\ncat /tmp/pip_install.log | tail -5\nps -p &lt;PID> -o pid= 2>/dev/null && echo \"STILL_RUNNING\" || echo \"DONE\"\n```\n\n```bash\n# 方法 2: 加大 pip 超时\npip install --timeout 300 torch ...\n```\n\n## Phase 4: 验证（必须执行）\n\n安装后必须验证，不要假设成功：\n\n```bash\npython3 -c \"\nimport torch\nprint(f'torch={torch.__version__}, cuda={torch.cuda.is_available()}, gpus={torch.cuda.device_count()}')\nif torch.cuda.is_available():\n    for i in range(torch.cuda.device_count()):\n        print(f'  GPU {i}: {torch.cuda.get_device_name(i)} ({torch.cuda.get_device_properties(i).total_mem // 1024**3}GB)')\n\"\n```\n\n验证失败的常见原因：\n- `torch.cuda.is_available()` 返回 False → CUDA 版本和 torch 不匹配，重装正确版本\n- `ImportError: libcudnn` → 缺 cuDNN，装 `nvidia-cudnn-cu1x`\n- GPU 数量不对 → 检查 `CUDA_VISIBLE_DEVICES` 环境变量\n\n## Phase 5: 项目依赖\n\n基础环境就绪后，安装项目依赖：\n\n```bash\n# 优先用 requirements.txt / pyproject.toml\npip install -r requirements.txt  # 或 pip install -e .\n\n# 常用 ML 依赖补装\npip install transformers datasets einops accelerate wandb\n```\n\nflash-attention 特殊处理（编译型包）：\n```bash\n# 需要匹配的 CUDA toolkit，编译耗时 5-15 分钟\npip install flash-attn --no-build-isolation\n# 如果编译失败，试预编译版本\npip install flash-attn --no-build-isolation 2>/dev/null || pip install flash-attn-wheels\n```\n\n## ssh_read_only vs ssh_execute 使用规则\n\n| 操作 | 用哪个工具 |\n|------|-----------|\n| 检查环境（python --version, nvidia-smi, pip list） | `ssh_read_only` |\n| 读文件内容、查日志 | `ssh_read_only` |\n| 安装包（pip install, conda install） | `ssh_execute` |\n| 创建/修改文件、启动进程 | `ssh_execute` |\n| 运行实验脚本 | `ssh_execute` |\n\n**原则：能用 read_only 就用 read_only，只有要改变服务器状态时才用 execute。**\n\n## AutoDL 专项注意事项\n\nAutoDL 实例有一系列特殊约束，5 个项目反复踩坑，必须遵守：\n\n### 磁盘\n- **根分区只有 ~30GB，严禁存大文件。** 模型、数据集、HF cache 全部放数据盘 `/root/autodl-tmp/`\n- 设置 `HF_HOME=/root/autodl-tmp/.hf_cache`，否则 HF 默认缓存到根分区导致磁盘满\n- 下载模型时用 `--local-dir /root/autodl-tmp/models/&lt;name>`，不要用默认路径\n\n### 网络\n- pip install / git clone 前必须 `source /etc/network_turbo` 启用代理加速，否则 pypi.nvidia.com 504 超时、GitHub TLS 断连\n- HF 下载设 `HF_HUB_DISABLE_XET=1`，xet_get 在 AutoDL 上返回 401\n- **SSL 证书**：`network_turbo` 的代理使用自签名证书，Python 默认 SSL 验证会失败。必须设置 `REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt` 和 `SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt`，否则 HF 下载、datasets 加载等全部报 SSL 错误\n- **大模型下载优先用 ModelScope**：AutoDL 代理下载 HuggingFace 大文件极慢（~200KB/s），改用 ModelScope 国内 CDN 速度快很多。`pip install modelscope && python -c \"from modelscope import snapshot_download; snapshot_download('Qwen/Qwen2.5-7B-Instruct', cache_dir='/root/autodl-tmp/.hf_cache')\"`\n\n### SSH\n- **AutoDL 实例重启后 SSH 端口会变。** 连接失败时不要反复重试，应提示用户去控制台查新端口并更新 `~/.ssh/config`\n\n## 经验沉淀\n\n- [2026-04-05] Worker 首次连接服务器时，先用一条 ssh_read_only 组合命令完成全部探测，减少 SSH 往返次数\n- [2026-04-05] 遇到 PEP 668 时创建 venv 而非 --break-system-packages，避免污染系统 Python\n- [2026-04-05] PyTorch 大包安装用 nohup 后台执行 + 轮询方式，避免 SSH 超时导致安装中断\n- [2026-04-05] conda 环境和 pip 不要混用——如果项目用 pip，就全部用 pip\n- [2026-04-09] sync_code 前确保本地 commit 已 push 到 remote，否则服务器 git pull 拉不到最新代码\n- [2026-04-09] venv 创建后用 `which python` 验证路径指向正确的 venv python，不要假设系统 PATH 正确\n\n## 更多 Skills（按需加载）\n\n执行相关任务前，先 Read 对应 skill 获取环境配置和最佳实践。\n\n- **check-training-status** — 当用户问训练进度/实验状态/查状态时使用。用专用工具查看训练状态，禁止 ssh_execute。  →  `/home/ubuntu/agent-ml-research/skills/global/check-training-status.skill.md`\n- **rebuttal** — 撰写和优化学术 rebuttal——逐条回应审稿意见，生成 response letter。当收到审稿意见、需要写 rebuttal、回复 reviewer 评论时使用。关键词：rebuttal、审稿意见、reviewer response、author response、meta-review、AC 意见。  →  `/home/ubuntu/agent-ml-research/skills/global/rebuttal.skill.md`\n- **review-reviewer-session-start** — Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。  →  `/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md`\n- **reference-audit** — 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。  →  `/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md`\n- **accelerate-distributed** — HuggingFace Accelerate 分布式训练指南——4行代码实现多GPU/DeepSpeed/FSDP/混合精度。多GPU训练时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/accelerate-distributed.skill.md`\n- **draw-paper-figure** — 生成学术论文级 matplotlib 图表——reliability diagrams、ECE heatmap、T* scatter plot、模型对比图，直接在 A6000 服务器上执行，输出 PDF/PNG  →  `/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md`\n- **experiment-analysis** — 实验结果分析框架——统计显著性检验、消融分析、baseline 对比、可视化建议。分析实验结果或撰写论文 Results 部分时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/experiment-analysis.skill.md`\n- **hf-hub** — HuggingFace Hub CLI (hf) — 下载/上传模型和数据集、管理缓存、搜索论文和模型。涉及 HuggingFace 资源操作时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/hf-hub.skill.md`\n- **latex-paper** — ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`\n- **lm-eval-harness** — lm-evaluation-harness 模型评估指南——MMLU/GSM8K/HumanEval 等 60+ 学术基准测试。评估模型质量、对比实验时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/lm-eval-harness.skill.md`\n- **ml-experiment-guide** — 跨项目 ML 实验避坑指南——从多个项目沉淀的通用踩坑经验与最佳实践。当 Worker 准备写实验代码、或排查实验问题时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ml-experiment-guide.skill.md`\n- **paper-banana** — 用 PaperBanana 生成发表级学术统计图——LLM 写 matplotlib 代码 + Critic 迭代 3 轮，输入 CSV/JSON 数据 + 意图描述即可。需要 GOOGLE_API_KEY。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-banana.skill.md`\n- **paper-image-extractor** — 从论文 PDF 或 arXiv 源码包提取图表——优先 arXiv 原始图片，回退 PDF 解析。用户说\"提取图\"/\"抽图\"/\"extract figures\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-image-extractor.skill.md`\n- **peft-lora** — PEFT/LoRA/QLoRA 参数高效微调指南——LoRA 配置选择、QLoRA 量化训练、Adapter 管理与合并。微调大模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/peft-lora.skill.md`\n- **research-news** — 每日论文推荐——搜索 arXiv 最新论文，按相关性/新颖性/影响力评分，生成推荐列表。Director 说\"有什么新论文\"/\"最近进展\"/\"research news\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/research-news.skill.md`\n- **trl-training** — TRL (Transformer Reinforcement Learning) 训练指南——SFT/DPO/GRPO/KTO 配置与最佳实践。训练或对齐语言模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/trl-training.skill.md`\n- **wandb-guide** — W&B 查询最佳实践——如何高效使用 fetch_wandb_metrics / compare_wandb_runs / get_best_wandb_run 分析实验结果。分析实验指标时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/wandb-guide.skill.md`\n",
      "contentDiffersFromDisk": false
    },
    "displayPath": "projects/phase-gated-compound-sparse/.claude/CLAUDE.md"
  },
  "type": "attachment",
  "uuid": "61ef6b2e-7a0d-4e4d-9a38-a2c04a5b6b1b",
  "timestamp": "2026-05-16T15:27:13.406Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "a3d601b9-90d6-4700-8195-7ac8fe55805b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Assistant

_source line 28 · 2026-05-16T15:27:19.608Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clearer picture. The running/planned experiments are:

1. **c8_llama_n250_fixed** (RUNNING) - LLaMA n=250 cross-architecture validation
2. **gpqa_ds_importance_s015** (RUNNING) - GPQA first condition
3. **gpqa_ds_importance_s020** (QUEUED) - GPQA second condition

Let me also check what other GPQA conditions might be queued/planned.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61ef6b2e-7a0d-4e4d-9a38-a2c04a5b6b1b",
  "isSidechain": false,
  "requestId": "req_011Cb6UxkQdBo6HxrxbQcU4p",
  "type": "assistant",
  "uuid": "64166858-c76c-4c60-82d8-2c1b0efed4aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "a3d601b9-90d6-4700-8195-7ac8fe55805b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HSnmLrWiYTouQa8S7avrJo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5749,
      "cache_read_input_tokens": 96216,
      "output_tokens": 337,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5749,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 337,
          "cache_read_input_tokens": 96216,
          "cache_creation_input_tokens": 5749,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5749
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

_source line 29 · 2026-05-16T15:27:21.519Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01C4aNJAKCfP9WePKPBQMpDe`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/checkpoints/gpqa_* 2>/dev/null | sort",
  "description": "List GPQA checkpoint files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64166858-c76c-4c60-82d8-2c1b0efed4aa",
  "isSidechain": false,
  "requestId": "req_011Cb6UxkQdBo6HxrxbQcU4p",
  "type": "assistant",
  "uuid": "8dd58993-f0b5-4348-aa44-192ae1f1516f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "a3d601b9-90d6-4700-8195-7ac8fe55805b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HSnmLrWiYTouQa8S7avrJo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5749,
      "cache_read_input_tokens": 96216,
      "output_tokens": 337,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5749,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 337,
          "cache_read_input_tokens": 96216,
          "cache_creation_input_tokens": 5749,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5749
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

_source line 30 · 2026-05-16T15:27:21.770Z_

<details><summary>↩ Tool result · `toolu_01C4aNJAKCfP9WePKPBQMpDe`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/checkpoints/gpqa_ds_importance_s015_ALLOCATED_20260516T074222.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/checkpoints/gpqa_ds_importance_s015_ALLOCATED_20260516T074301.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/checkpoints/gpqa_ds_importance_s015_PREPARING_20260516T051315.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/checkpoints/gpqa_ds_importance_s015_QUEUED_20260516T061541.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/checkpoints/gpqa_ds_importance_s015_RUNNING_20260516T074332.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/checkpoints/gpqa_ds_importance_s020_QUEUED_20260516T152623.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8dd58993-f0b5-4348-aa44-192ae1f1516f",
  "isSidechain": false,
  "promptId": "1b3ef117-44ac-4494-a1a3-d617fc268060",
  "type": "user",
  "uuid": "55b7f599-f211-4913-9572-fa67310ffeb8",
  "toolUseResult": {
    "stdout": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/checkpoints/gpqa_ds_importance_s015_ALLOCATED_20260516T074222.json\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/checkpoints/gpqa_ds_importance_s015_ALLOCATED_20260516T074301.json\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/checkpoints/gpqa_ds_importance_s015_PREPARING_20260516T051315.json\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/checkpoints/gpqa_ds_importance_s015_QUEUED_20260516T061541.json\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/checkpoints/gpqa_ds_importance_s015_RUNNING_20260516T074332.json\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/checkpoints/gpqa_ds_importance_s020_QUEUED_20260516T152623.json",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "8dd58993-f0b5-4348-aa44-192ae1f1516f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "a3d601b9-90d6-4700-8195-7ac8fe55805b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-16T15:27:21.953Z_

<details><summary>↩ Tool result · `toolu_01BpVdomvv3FaqiYDgWQoLcY`</summary>

```text
1	# phase-gated-compound-sparse — Research Dashboard
2	
3	> 最后更新: 2026-05-16 04:36 UTC | 更新原因: 目标会议更新为 EMNLP 2025 main + headline 验证通过 + GPU0 状态更新 + 远程 tex 同步
4	
5	> 核心文档链: paper_framing.md → experiment_plan.yaml → 本 ROADMAP
6	
7	## 核心方向
8	**Phase-modulated compound sparsity severity**：importance-based eviction 的 compound interaction severity 随 sparsity 单调递增（n=500 confirmed）。详见 paper_framing.md。
9	
10	## 目标会议
11	EMNLP 2025 main conference — **截稿 2026-05-25（距今 9 天）**（没中延 Findings）
12	
13	## 当前进展
14	- 阶段：**Round 10 修订收尾 → 接近 Round 11 提交**
15	- 129 实验完成（63 success / 17 negative / 17 failed），38 plan experiments 全部 done（coverage 92.1%）
16	- 实验侧：5/6 CPU 任务完成，仅剩 c8_llama_n250_fixed（GPU running）+ c10_lang_s020_s025（GPU running）
17	- 写作侧：4/4 主要修正完成（bib审计✅ abstract/intro✅ §4-7✅ appendix✅），headline 数字一致性已验证通过✅
18	
19	## ⚠️ Round 11 提交前 Blocking Checklist
20	- [x] **Headline 数字一致性**：本地 tex 全部使用 n=500 数据（Reviewer + Worker 双重验证通过）。远程旧副本 rsync 同步中
21	- [ ] c8_llama_n250_fixed 完成 + 结果写入论文
22	- [x] 用户确认目标会议：EMNLP 2025 main conference（没中延 Findings）
23	- [ ] Figure 1 PDF 生成 → 已派 Worker，生成中
24	- [x] 远程 tex 同步完成验证（74 文件 rsync，旧数字已清除）
25	- [ ] Round 11 提交
26	
27	## Round 10 修订进度
28	
29	### 实验任务
30	- [x] **P1-CPU** &lt;think> token position validation — DONE (D093: adaptive κ=0.8804)
31	- [x] **P1-CPU** Per-phase Gini decomposition — DONE (Reviewer PASS: DS+QW 30/30, low_delta > mid > high)
32	- [x] **P2-CPU** GSM8K power analysis — DONE (D092)
33	- [x] **P2-CPU** MATH-500 language switching — DONE (c10_lang_switching success)
34	- [ ] **P1-GPU** LLaMA n=250 — c8_llama_n250_fixed RUNNING（GPU2+3）
35	- [ ] c10_lang_s020_s025 — RUNNING（GPU1）
36	
37	### 写作任务（Paper Agent）
38	- [x] MUSTAFAR 删除 + bib 全量审计 — Reviewer PASS
39	- [x] Abstract/Intro rewrite — 完成，**headline 数字需验证**（见 Blocking Checklist）
40	- [x] §4-7 corrections — Reviewer PASS
41	- [x] Appendix fixes — 完成
42	
43	## GPU 状态
44	- RTX 6000 Pro ×4: westd-22162 cuda:0~3
45	- GPU0: c8_llama_gpu0_s025 RUNNING (PID 315052, preemptive acceleration)
46	- GPU1: c10_lang_s020_s025
47	- GPU2+3: c8_llama_n250_fixed
48	- 已用: ~36h / ~250h 预算
49	
50	## 审稿回溯·系统性问题（Round 10 Holistic Pass）
51	
52	### SYSTEMIC_ISSUE #1: 写作可信度 → Paper Agent 修正完成
53	R10-C1 (MUSTAFAR ✅), R10-W1 (overclaiming ✅), R10-W3 (H2O confound ✅), R10-W4 (GPU deanon ✅), R10-W5 (statistical gaps ✅), R10-W6 (clarity ✅)
54	
55	### SYSTEMIC_ISSUE #2: 实验证据厚度 → 5/6 完成
56	R10-C3 (LLaMA n=250 running), R10-C4 (&lt;think> ✅), R10-C5 (Gini ✅), R10-W5 (pilot CI ✅)
57	
58	### 非系统性 Critical: 定位调整
59	R10-C2 → Main conference（用户确认），没中延 Findings
60	
61	## Scope 扩展（Director 批准）
62	
63	### 线路 A: GPQA Diamond（非数学推理）
64	- [ ] 数据下载 + pipeline 适配（CPU Worker 进行中）
65	- [ ] DS + QW × importance × 4 sparsities + 2 random controls = 10 runs
66	- 等 GPU 释放后开跑
67	
68	### 线路 B: 14B 模型（scale 扩展）
69	- [ ] Qwen2.5-14B-Instruct 下载（CPU Worker 进行中）
70	- [ ] MATH-500 × importance × 4 sparsities + 1 random control = 5 runs
71	- 等模型下载 + GPU 释放后开跑
72	
73	## 关键决策日志
74	
75	| ID | 日期 | 摘要 | 关联实验 |
76	|----|------|------|----------|
77	| D098 | 2026-05-16 | GPQA segmentation: quantile 三分为 primary，&lt;/think> 二 | gpqa_ds_importance_s015, c4_think_validation_math500 |
78	| D097 | 2026-05-16 | 撤回 D091 Findings track framing 决策，按 EMNLP main con | — |
79	| D096 | 2026-05-16 | Session 15 决策：c10 等 c5 释放 GPU、Paper Agent 启动 Findi | c5_per_phase_gini, c8_llama_n250_fixed, c10_lang_switching |
80	| D095 | 2026-05-16 | c8_llama_n250 数据丢失，GPU 2/3 立即重跑；c10 排队等 c5 释放 GPU | c8_llama_n250, c10_lang_switching, c5_per_phase_gini |
81	| D094 | 2026-05-16 | c8_llama_n250 数据全丢事故——c10 越权 GPU 使用导致级联失败，c8 需从头重跑 | c8_llama_n250, c10_lang_switching |
82	| D093 | 2026-05-16 | &lt;think> phase validation 达标：adaptive κ=0.8804, AUC | c4_think_validation_math500 |
83	| D092 | 2026-05-16 | c9 power analysis 仅报告 random 条件；importance 条件丢弃 t- | c9_gsm8k_power_analysis |
84	| D091 | 2026-05-16 | R10 审稿 Weak Reject (2.25/5)：接受 Findings track，启动 5 | c3_llama, think_phase_validation, c4_entropy |
85	| D090 | 2026-05-16 | Round 10 dual dose curve 完成：DS 5-point (0.74→0.04) | acc_ds_dense_8k_v2, acc_ds_s015_8k_v2, acc_ds_s020_8k_v2, acc_ds_s025_8k_v2, acc_ds_s030_8k_v2, acc_qw_s030_b1_8k, acc_qw_s025_b1_8k |
86	| D089 | 2026-05-16 | DS 8k v2 揭示双 regime 结构：s≤0.20 截断驱动（非截断 acc ~71% 稳定 | acc_ds_dense_8k_v2, acc_ds_s015_8k_v2, acc_ds_s020_8k_v2, acc_ds_s025_8k_v2, acc_ds_s030_8k_v2 |
87	
88	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a58c141f-2239-4a77-9963-bb1de528248e",
  "isSidechain": false,
  "promptId": "1b3ef117-44ac-4494-a1a3-d617fc268060",
  "type": "user",
  "uuid": "4bb61718-d581-43d5-9f62-9ec06fe7d176",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/ROADMAP.md",
      "content": "# phase-gated-compound-sparse — Research Dashboard\n\n> 最后更新: 2026-05-16 04:36 UTC | 更新原因: 目标会议更新为 EMNLP 2025 main + headline 验证通过 + GPU0 状态更新 + 远程 tex 同步\n\n> 核心文档链: paper_framing.md → experiment_plan.yaml → 本 ROADMAP\n\n## 核心方向\n**Phase-modulated compound sparsity severity**：importance-based eviction 的 compound interaction severity 随 sparsity 单调递增（n=500 confirmed）。详见 paper_framing.md。\n\n## 目标会议\nEMNLP 2025 main conference — **截稿 2026-05-25（距今 9 天）**（没中延 Findings）\n\n## 当前进展\n- 阶段：**Round 10 修订收尾 → 接近 Round 11 提交**\n- 129 实验完成（63 success / 17 negative / 17 failed），38 plan experiments 全部 done（coverage 92.1%）\n- 实验侧：5/6 CPU 任务完成，仅剩 c8_llama_n250_fixed（GPU running）+ c10_lang_s020_s025（GPU running）\n- 写作侧：4/4 主要修正完成（bib审计✅ abstract/intro✅ §4-7✅ appendix✅），headline 数字一致性已验证通过✅\n\n## ⚠️ Round 11 提交前 Blocking Checklist\n- [x] **Headline 数字一致性**：本地 tex 全部使用 n=500 数据（Reviewer + Worker 双重验证通过）。远程旧副本 rsync 同步中\n- [ ] c8_llama_n250_fixed 完成 + 结果写入论文\n- [x] 用户确认目标会议：EMNLP 2025 main conference（没中延 Findings）\n- [ ] Figure 1 PDF 生成 → 已派 Worker，生成中\n- [x] 远程 tex 同步完成验证（74 文件 rsync，旧数字已清除）\n- [ ] Round 11 提交\n\n## Round 10 修订进度\n\n### 实验任务\n- [x] **P1-CPU** &lt;think> token position validation — DONE (D093: adaptive κ=0.8804)\n- [x] **P1-CPU** Per-phase Gini decomposition — DONE (Reviewer PASS: DS+QW 30/30, low_delta > mid > high)\n- [x] **P2-CPU** GSM8K power analysis — DONE (D092)\n- [x] **P2-CPU** MATH-500 language switching — DONE (c10_lang_switching success)\n- [ ] **P1-GPU** LLaMA n=250 — c8_llama_n250_fixed RUNNING（GPU2+3）\n- [ ] c10_lang_s020_s025 — RUNNING（GPU1）\n\n### 写作任务（Paper Agent）\n- [x] MUSTAFAR 删除 + bib 全量审计 — Reviewer PASS\n- [x] Abstract/Intro rewrite — 完成，**headline 数字需验证**（见 Blocking Checklist）\n- [x] §4-7 corrections — Reviewer PASS\n- [x] Appendix fixes — 完成\n\n## GPU 状态\n- RTX 6000 Pro ×4: westd-22162 cuda:0~3\n- GPU0: c8_llama_gpu0_s025 RUNNING (PID 315052, preemptive acceleration)\n- GPU1: c10_lang_s020_s025\n- GPU2+3: c8_llama_n250_fixed\n- 已用: ~36h / ~250h 预算\n\n## 审稿回溯·系统性问题（Round 10 Holistic Pass）\n\n### SYSTEMIC_ISSUE #1: 写作可信度 → Paper Agent 修正完成\nR10-C1 (MUSTAFAR ✅), R10-W1 (overclaiming ✅), R10-W3 (H2O confound ✅), R10-W4 (GPU deanon ✅), R10-W5 (statistical gaps ✅), R10-W6 (clarity ✅)\n\n### SYSTEMIC_ISSUE #2: 实验证据厚度 → 5/6 完成\nR10-C3 (LLaMA n=250 running), R10-C4 (&lt;think> ✅), R10-C5 (Gini ✅), R10-W5 (pilot CI ✅)\n\n### 非系统性 Critical: 定位调整\nR10-C2 → Main conference（用户确认），没中延 Findings\n\n## Scope 扩展（Director 批准）\n\n### 线路 A: GPQA Diamond（非数学推理）\n- [ ] 数据下载 + pipeline 适配（CPU Worker 进行中）\n- [ ] DS + QW × importance × 4 sparsities + 2 random controls = 10 runs\n- 等 GPU 释放后开跑\n\n### 线路 B: 14B 模型（scale 扩展）\n- [ ] Qwen2.5-14B-Instruct 下载（CPU Worker 进行中）\n- [ ] MATH-500 × importance × 4 sparsities + 1 random control = 5 runs\n- 等模型下载 + GPU 释放后开跑\n\n## 关键决策日志\n\n| ID | 日期 | 摘要 | 关联实验 |\n|----|------|------|----------|\n| D098 | 2026-05-16 | GPQA segmentation: quantile 三分为 primary，&lt;/think> 二 | gpqa_ds_importance_s015, c4_think_validation_math500 |\n| D097 | 2026-05-16 | 撤回 D091 Findings track framing 决策，按 EMNLP main con | — |\n| D096 | 2026-05-16 | Session 15 决策：c10 等 c5 释放 GPU、Paper Agent 启动 Findi | c5_per_phase_gini, c8_llama_n250_fixed, c10_lang_switching |\n| D095 | 2026-05-16 | c8_llama_n250 数据丢失，GPU 2/3 立即重跑；c10 排队等 c5 释放 GPU | c8_llama_n250, c10_lang_switching, c5_per_phase_gini |\n| D094 | 2026-05-16 | c8_llama_n250 数据全丢事故——c10 越权 GPU 使用导致级联失败，c8 需从头重跑 | c8_llama_n250, c10_lang_switching |\n| D093 | 2026-05-16 | &lt;think> phase validation 达标：adaptive κ=0.8804, AUC | c4_think_validation_math500 |\n| D092 | 2026-05-16 | c9 power analysis 仅报告 random 条件；importance 条件丢弃 t- | c9_gsm8k_power_analysis |\n| D091 | 2026-05-16 | R10 审稿 Weak Reject (2.25/5)：接受 Findings track，启动 5 | c3_llama, think_phase_validation, c4_entropy |\n| D090 | 2026-05-16 | Round 10 dual dose curve 完成：DS 5-point (0.74→0.04) | acc_ds_dense_8k_v2, acc_ds_s015_8k_v2, acc_ds_s020_8k_v2, acc_ds_s025_8k_v2, acc_ds_s030_8k_v2, acc_qw_s030_b1_8k, acc_qw_s025_b1_8k |\n| D089 | 2026-05-16 | DS 8k v2 揭示双 regime 结构：s≤0.20 截断驱动（非截断 acc ~71% 稳定 | acc_ds_dense_8k_v2, acc_ds_s015_8k_v2, acc_ds_s020_8k_v2, acc_ds_s025_8k_v2, acc_ds_s030_8k_v2 |\n\n",
      "numLines": 88,
      "startLine": 1,
      "totalLines": 88
    }
  },
  "sourceToolAssistantUUID": "a58c141f-2239-4a77-9963-bb1de528248e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "a3d601b9-90d6-4700-8195-7ac8fe55805b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-16T15:27:21.949Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BpVdomvv3FaqiYDgWQoLcY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/ROADMAP.md",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55b7f599-f211-4913-9572-fa67310ffeb8",
  "isSidechain": false,
  "requestId": "req_011Cb6UxkQdBo6HxrxbQcU4p",
  "type": "assistant",
  "uuid": "a58c141f-2239-4a77-9963-bb1de528248e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "a3d601b9-90d6-4700-8195-7ac8fe55805b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HSnmLrWiYTouQa8S7avrJo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5749,
      "cache_read_input_tokens": 96216,
      "output_tokens": 337,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5749,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 337,
          "cache_read_input_tokens": 96216,
          "cache_creation_input_tokens": 5749,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5749
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

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：LLaMA n=250 高功效确认 strategy×phase 交互在 Llama 架构上可忽略；random phase gradient 稳健。GPQA 不显著或方向不一致。'Strategy-gated' 叙事崩塌——phase modulation 普遍存在但非 strategy-specific…",
  "leafUuid": "4bb61718-d581-43d5-9f62-9ec06fe7d176",
  "sessionId": "a3d601b9-90d6-4700-8195-7ac8fe55805b"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Phase-dependent compound sparsity in reasoning models",
  "sessionId": "a3d601b9-90d6-4700-8195-7ac8fe55805b"
}
```

---

### Assistant

_source line 35 · 2026-05-16T15:28:32.160Z_

<details><summary>Logged reasoning block</summary>

```text
Now I see the full picture. The planned experiments for this project include:

**Currently running/queued:**
1. c8_llama_n250_fixed (RUNNING, GPU2+3) - LLaMA n=250 cross-architecture, 8 conditions
2. gpqa_ds_importance_s015 (RUNNING, GPU1) - GPQA Diamond first condition
3. gpqa_ds_importance_s020 (QUEUED)

**Planned (from ROADMAP Scope expansion):**


4. GPQA Diamond with dataset and question weighting across importance levels and 4 sparsities, plus 2 random controls—10 runs total
5. Qwen2.5-14B-Instruct on MATH-500 with importance and 4 sparsities plus 1 random control—5 runs total

So the full experimental pipeline consists of the LLaMA cross-architecture study, the GPQA Diamond conditions, and the 14B model experiments.

Now I'm checking which of these actually fall under the worst tier definition. The tier specification only mentions LLaMA n=250 and GPQA metrics, so the 14B model experiments aren't part of what I need to predict for that tier. I should focus on the LLaMA n=250 conditions and GPQA results instead. Looking at the metrics I need to track for the worst tier definition—the median difference, Bonferroni p-values, and importance-to-random ratios from the DS GPQA results—I'm now ready to compile the full YAML structure. I'll organize it with the LLaMA aggregate baseline, then the four sparsity levels for DS importance, the QW importance experiments across all levels, the random controls, and the cross-task validation.

Actually, I'm realizing I should group these by their natural experimental units rather than listing every single variant. The user asked for each planned experiment, so I need to check what's actually registered in the experiment plan—the main LLaMA run, the DS importance series, the QW importance series, the random controls, and the synthesis analysis. Let me verify which of these are already in the registry versus queued. I'm settling on listing the experiments by their actual status—running, queued, and planned—rather than breaking down every single GPQA condition separately. For the GPQA experiments, I'll group related conditions together to keep things manageable while still providing detailed predictions for each major experiment category.

Now I'm working through the specific numbers I have so far, starting with the c8_llama baseline where I've got partial results showing an importance score around 1.1 with a median difference of about 0.38.

Looking at the c3_llama data at n=49, I can see how the phase gradient metrics scale across different conditions, which gives me a sense of what to expect when I extrapolate to n=250. The importance phase gradient values cluster around 1.0-1.1, while the random phase gradient sits lower around 0.35-0.45. Based on these patterns, I'm estimating the ranges I'd expect to see at the larger sample size and picking representative values within those ranges.

Now I'm working through the statistical significance for the importance versus random comparison at n=250. I'm calculating z-scores for each effect size estimate and checking whether they'd survive Bonferroni correction across the four comparisons. The smaller effect sizes around 0.09-0.12 don't reach significance even before correction, while the larger ones like 0.15 get closer but still fall short after adjusting for multiple comparisons.

Only s030 with its effect size of 0.21 produces a significant result that survives the correction, giving me a count of 1 significant finding—right at the boundary of the worst tier. Now I'm looking at the median differences from the cross-strategy comparison at n=49 and projecting what those values might shrink to at the larger sample size of n=250.

The median differences should remain relatively stable as a location parameter while the confidence intervals tighten, so I'm adjusting the estimates downward slightly to reflect the worst-tier pattern. I'm also working through the phase gradient comparisons separately for both the random and importance-weighted conditions at n=250.

Now I'm shifting focus to GPQA Diamond, which has 198 problems total. The key question is whether they're using all of them or subsampling—the registry doesn't specify n_problems yet, so I'm assuming n=50 to stay consistent with the MATH-500 experiments. GPQA differs fundamentally from MATH-500 since it involves non-math reasoning across science, philosophy, and law domains.

The reasoning chains are much shorter here, typically under 500 tokens compared to MATH-500's 2000+, and the thinking patterns are less structured, which means the phase segmentation might not map cleanly onto distinct reasoning stages. Under worst-tier conditions, I'd expect the phase gradient to be weak or inconsistent, with no clear dose-response relationship and strategy separation hovering near 1.

Now I'm finalizing the YAML with specific numbers and rationales, and I need to compute all the values once more for consistency before writing it out.

Looking at the c8_llama_n250_fixed results, I'm calculating the phase gradients across the importance and random conditions. The importance phase gradient d_z averages around 1.04 across the seed values, while the random phase gradient d_z is much lower at around 0.44. The difference between importance and random shows a clear trend, starting at 0.09 for s015 and climbing to 0.21 for s030, indicating stronger separation at higher seed values.

Now examining the median differences in paired comparisons, the importance condition shows much larger effects than random, particularly at s030 where the median difference reaches 0.850 compared to just 0.120 for random. The gap between importance and random median differences grows substantially with seed size, from 0.012 at s015 to 0.195 at s030. Only the s030 comparison reaches Bonferroni significance. Moving into the GPQA DS importance analysis, the median differences are much smaller here, with s015 showing 0.03 and s020 showing a slight negative effect of -0.02.

For GPQA DS, none of the comparisons reach significance even before correction, and the pattern across seed sizes shows no monotonic trend with a Spearman correlation of only 0.4. The GPQA QW importance results are similarly weak, with all median differences staying below 0.04 and no significant effects across any seed size.

Looking at the random control comparisons, the importance effect at s030 is nearly identical to the random baseline, giving an importance-to-random ratio of just 0.83, which suggests the signal is barely distinguishable from noise.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4bb61718-d581-43d5-9f62-9ec06fe7d176",
  "isSidechain": false,
  "requestId": "req_011Cb6UyQ7mWoU6XWEDZ4eT8",
  "type": "assistant",
  "uuid": "fba2c85d-d5b7-4117-be8d-c13067228a1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "a3d601b9-90d6-4700-8195-7ac8fe55805b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J3o6oEJdUdGLXWfDtMqZPv",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3216,
      "cache_read_input_tokens": 101965,
      "output_tokens": 14602,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3216,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14602,
          "cache_read_input_tokens": 101965,
          "cache_creation_input_tokens": 3216,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3216
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

_source line 36 · 2026-05-16T15:31:39.271Z_

Now I have the complete picture: 2 running experiments (c8_llama_n250_fixed, gpqa_ds_importance_s015), 1 queued (gpqa_ds_importance_s020), and GPQA scope expansion planned (DS+QW × 4 sparsities + 2 random = 10 runs).

```yaml
tier: worst
narrative_guidance: >
  Title 改为 "Phase-Dependent Compound Sparsity Severity in Reasoning LLMs"（去掉 strategy-gated）。
  Core finding 收窄：compound sparsity severity 是 phase-modulated 的涌现属性，
  importance phase gradient 跨三模型两架构一致（d_z≈1.0-1.2），但 strategy×phase 交互仅
  Qwen2 架构显著，Llama 上 random 也产生 comparable phase gradient（d_z 0.35-0.55）。
  论文重组为三层递进：(1) Phase gradient universality（核心贡献，跨模型/架构稳健），
  (2) Strategy modulation 的 architecture-dependence（secondary finding，Qwen2 confirmed / Llama NS → 开放问题），
  (3) Discrimination collapse 机制（Gini/CV 跨模型一致，作为 phase gradient 的解释
  而非 strategy-specificity 的解释）。Scope 限于 MATH-500 + GSM8K（GPQA 仅放 appendix 或不纳入）。
  EMNLP main 仍可冲——pitch 改为 "first systematic quantitative characterization of
  phase-dependent compound sparsity"，强调 dose-response monotonicity（ρ=1.0, n=500 两模型）、
  sparsity threshold discovery（~s020-s025）、discrimination collapse 机制。
  Novelty 论证需加强 methodology 贡献（per-problem paired II metric + phase segmentation framework）。
  需重写 §1-§3，将 strategy 从核心 claim 降级到 architecture-dependent 观察。
  Limitations 增加一段 strategy-specificity 的 scope boundary。

imagined_experiments:

  # ============================================================
  # Experiment 1: LLaMA n=250 Cross-Architecture Validation
  # ============================================================
  - name: "LLaMA n=250 cross-architecture validation (8 conditions)"
    plan_id: c8_llama_n250_fixed
    description: >
      DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM), MATH-500 n=250 problems,
      8 conditions (importance/random × s015/s020/s025/s030)。从 c3_llama (n=49)
      升级到 n=250，功效提升 ~5×。n=250 对 d=0.25 的检测功效 >0.95。
      已有 partial result：c8_llama_gpu0_s025 (importance s025, d_z=1.1174)。
    expected_results:
      n_problems: 250
      n_valid: 244
      n_bootstrap: 10000
      bonferroni_k: 4

      # --- Importance phase gradient (within-strategy) ---
      imp_phase_gradient_dz:
        s015: 0.97
        s020: 1.06
        s025: 1.12
        s030: 1.01
      imp_phase_gradient_dz_ci:
        s015: [0.81, 1.13]
        s020: [0.90, 1.22]
        s025: [0.93, 1.31]
        s030: [0.85, 1.17]
      imp_phase_gradient_interpretation: all_large
      imp_median_diff:
        s015: 0.019
        s020: 0.060
        s025: 0.376
        s030: 0.850
      imp_median_diff_ci:
        s015: [0.012, 0.025]
        s020: [0.042, 0.078]
        s025: [0.315, 0.404]
        s030: [0.720, 1.000]
      imp_wilcoxon_p:
        s015: 2.0e-22
        s020: 5.0e-27
        s025: 4.3e-39
        s030: 1.0e-37
      imp_bonferroni_all_sig: true
      imp_dose_response_monotonic: true
      imp_spearman_rho: 1.0

      # --- Random phase gradient (within-strategy) ---
      rand_phase_gradient_dz:
        s015: 0.38
        s020: 0.42
        s025: 0.48
        s030: 0.46
      rand_phase_gradient_dz_ci:
        s015: [0.24, 0.52]
        s020: [0.28, 0.56]
        s025: [0.34, 0.62]
        s030: [0.32, 0.60]
      rand_phase_gradient_interpretation: all_small_to_medium
      rand_median_diff:
        s015: 0.007
        s020: 0.012
        s025: 0.048
        s030: 0.120
      rand_median_diff_ci:
        s015: [0.001, 0.014]
        s020: [0.003, 0.022]
        s025: [0.020, 0.078]
        s030: [0.058, 0.190]
      rand_wilcoxon_p:
        s015: 3.5e-04
        s020: 8.0e-06
        s025: 2.0e-09
        s030: 5.0e-09
      rand_bonferroni_all_sig: true
      rand_dose_response_monotonic: true

      # --- Strategy × phase interaction (imp vs rand) ---
      imp_vs_rand_dz:
        s015: 0.09
        s020: 0.12
        s025: 0.15
        s030: 0.21
      imp_vs_rand_dz_ci:
        s015: [-0.04, 0.22]
        s020: [-0.01, 0.25]
        s025: [0.02, 0.28]
        s030: [0.08, 0.34]
      imp_vs_rand_dz_interpretation:
        s015: negligible
        s020: negligible
        s025: small
        s030: small
      imp_vs_rand_median_diff:
        s015: 0.012
        s020: 0.018
        s025: 0.068
        s030: 0.195
      imp_vs_rand_wilcoxon_p:
        s015: 0.12
        s020: 0.055
        s025: 0.015
        s030: 0.0009
      imp_vs_rand_bonferroni_p:
        s015: 0.48
        s020: 0.22
        s025: 0.060
        s030: 0.0036
      imp_vs_rand_bonferroni_sig:
        s015: false
        s020: false
        s025: false
        s030: true
      bonferroni_sig_count_out_of_4: 1

      # --- Cross-architecture comparison ---
      imp_rand_gradient_ratio_llama: 2.4
      imp_rand_gradient_ratio_qwen2_ds: 16.6
      imp_rand_gradient_ratio_qwen2_qw: 3.5
      architecture_dependence_confirmed: true

    result_rationale: >
      n=49→n=250 提供约 5× 功效提升。三个核心预测及其原因：

      (1) Importance phase gradient 保持 d_z≈1.0（范围 0.97-1.12）：
      c3_llama 在 n=49 已显示 d_z 1.00-1.12（所有 CI 排除零），且 c8_llama_gpu0_s025
      在 n=250 已实测 d_z=1.1174。n=250 使 CI 从宽度 ~0.8 缩窄到 ~0.3，
      但点估计不会实质性变化，因为 n=49 的估计已经是稳健的（bootstrap B=10000）。
      这确认了 phase-dependent compound severity 在 LLaMA 架构上是真实的涌现属性。

      (2) Random phase gradient 被确认（d_z 0.38-0.48，所有 CI 排除零）：
      c3_llama n=49 已显示 random d_z 0.35-0.45 但 CI 较宽（下界 0.07-0.20）。
      n=250 将 CI 压缩到下界 0.24-0.34，稳固排除零。这是 worst 档的关键发现：
      LLaMA 上 random eviction 也产生显著的 phase-dependent compound interaction。
      机制推测：LLaMA 的 attention 分布在 reasoning 不同阶段对 KV cache 扰动
      的敏感性不同，与扰动是 importance-based 还是 random 无关。
      这与 Qwen2 架构形成对比——Qwen2 上 random 在 s015/s020 NS，
      说明 Qwen2 的 attention pattern 能更好地容忍 random KV loss。

      (3) imp_vs_rand 交互仍然很小（d_z 0.09-0.21，仅 s030 Bonferroni 显著）：
      n=250 对 d=0.25 的功效 >0.95，但观测到的最大 d_z=0.21 < 0.25 阈值。
      与 n=49 的点估计（0.19-0.34）相比有所回落，这符合小样本效应量膨胀
      的统计预期。s030 的 Bonferroni p=0.0036 达到显著，但 d_z=0.21 仍是 small effect，
      实质上是高功效确认了 strategy×phase 交互在 Llama 上可忽略。
      对比 Qwen2 架构上的 imp_vs_rand dz（DS n=500: 0.44-0.80），
      LLaMA 的 0.09-0.21 小了 3-5×，确认了 architecture-dependence。

    tables:
      - name: "Table: LLaMA n=250 Phase Gradient Summary"
        content: |
          | Sparsity | Imp d_z [95% CI]    | Rand d_z [95% CI]    | Imp-Rand d_z [95% CI] | Bonf. sig |
          |----------|---------------------|----------------------|-----------------------|-----------|
          | s015     | 0.97 [0.81, 1.13]   | 0.38 [0.24, 0.52]   | 0.09 [−0.04, 0.22]   | NS        |
          | s020     | 1.06 [0.90, 1.22]   | 0.42 [0.28, 0.56]   | 0.12 [−0.01, 0.25]   | NS        |
          | s025     | 1.12 [0.93, 1.31]   | 0.48 [0.34, 0.62]   | 0.15 [0.02, 0.28]    | NS        |
          | s030     | 1.01 [0.85, 1.17]   | 0.46 [0.32, 0.60]   | 0.21 [0.08, 0.34]    | * (p=.004)|

      - name: "Table: Cross-Architecture Strategy Specificity Comparison"
        content: |
          | Architecture | Model              | Imp/Rand Gradient Ratio | Strategy×Phase Sig |
          |--------------|--------------------|------------------------|--------------------|
          | Qwen2        | DS-R1-Distill-7B   | 16.6× (n=500)          | 4/4 Bonferroni     |
          | Qwen2        | QW-2.5-7B          | 3.5× (n=500)           | 4/4 Bonferroni     |
          | LlamaForCausalLM | DS-R1-Distill-Llama-8B | 2.4× (n=250)   | 1/4 Bonferroni     |

    figures_description:
      - >
        Fig A: LLaMA n=250 paired phase gradient comparison。双 bar chart（每 sparsity level
        importance vs random），error bars = 95% CI on d_z。Importance 一致 ~1.0（蓝色），
        random 一致 ~0.4（橙色）。两者都显著高于零，但间距远小于 Qwen2 架构。
      - >
        Fig B: Cross-architecture strategy×phase interaction heatmap。行=架构（Qwen2-DS, Qwen2-QW, LLaMA），
        列=sparsity level。颜色=imp_vs_rand d_z。Qwen2 行显示从绿（medium）到红（large），
        LLaMA 行几乎全绿（negligible-small）。视觉呈现 architecture-dependence。

    analysis: >
      这是 worst 档的决定性实验。n=250 的高功效使得 imp_vs_rand d_z<0.25 成为可信的零结果，
      而非功效不足导致的假阴性。三个核心结论：

      (1) Phase gradient universality 被加强：importance phase gradient d_z≈1.0
      跨三个模型两个架构一致（DS Qwen2: 0.44-0.80; QW Qwen2: 0.37-1.44; LLaMA: 0.97-1.12），
      这是论文最强的贡献点。

      (2) Strategy specificity 局限于 Qwen2 架构：LLaMA 上 random 也显示显著 phase gradient
      (d_z 0.38-0.48)，打破了 "importance eviction 特有" 的叙事。在 Qwen2 上 random 在
      s015/s020 NS 但在 LLaMA 上全部显著，说明 architecture 决定了 strategy specificity
      是否成立。

      (3) "Strategy-gated" framing 无法维持：原标题和核心 claim 需要 reframe。
      Phase modulation 是普遍的（universality），strategy 作用是 architecture-dependent
      的 secondary modulator（not a gating mechanism）。

      对论文结构的影响：
      - §1 Introduction: 重写 motivation，从 "strategy-gated" 改为 "phase-dependent"
      - §3 Main results: Lead with phase gradient universality，然后 strategy modulation as secondary
      - §5 Discussion: 新增 "Architecture-Dependence of Strategy Modulation" 小节
      - §6 Limitations: 明确声明 strategy-specificity scope boundary
      - C8 claim 从 "partially_confirmed" 改为 narrative-aware 表述：
        "Phase gradient confirmed cross-architecture; strategy×phase interaction architecture-dependent"


  # ============================================================
  # Experiment 2: GPQA DS Importance Sweep (s015-s030)
  # ============================================================
  - name: "GPQA DeepSeek importance sweep (4 sparsity levels)"
    plan_id: gpqa_ds_importance_s015_to_s030
    description: >
      DeepSeek-R1-Distill-Qwen-7B, GPQA Diamond subset, importance masking at
      s015/s020/s025/s030。Quantile 3-segment phase decomposition (D098)。
      测试 phase-dependent compound severity 是否泛化到非数学推理。
      gpqa_ds_importance_s015 RUNNING, s020 QUEUED, s025/s030 planned。
    expected_results:
      n_problems: 50
      segmentation: quantile_3segment
      n_bootstrap: 10000
      bonferroni_k: 4

      importance_per_phase_ii_median:
        s015:
          high: 0.004
          mid: 0.012
          low: 0.035
        s020:
          high: 0.018
          mid: 0.008
          low: 0.015
        s025:
          high: 0.025
          mid: 0.052
          low: 0.108
        s030:
          high: 0.040
          mid: 0.035
          low: 0.088
      importance_median_diff:
        s015: 0.03
        s020: -0.02
        s025: 0.08
        s030: 0.05
      importance_median_diff_ci:
        s015: [-0.02, 0.09]
        s020: [-0.10, 0.06]
        s025: [-0.03, 0.22]
        s030: [-0.08, 0.25]
      importance_wilcoxon_p:
        s015: 0.18
        s020: 0.65
        s025: 0.09
        s030: 0.15
      importance_bonferroni_p:
        s015: 0.72
        s020: 1.00
        s025: 0.36
        s030: 0.60
      bonferroni_sig_count: 0
      phase_gradient_dz:
        s015: 0.22
        s020: -0.08
        s025: 0.30
        s030: 0.18
      dose_response_monotonic: false
      dose_response_pattern: "0.03, -0.02, 0.08, 0.05 (non-monotonic, s020 direction reversal)"
      spearman_rho: 0.40
      spearman_p: 0.60

    result_rationale: >
      GPQA Diamond 是 graduate-level 非数学推理（物理/化学/生物/哲学/法律），
      与 MATH-500/GSM8K 的结构化数学推理在多个维度不同，导致 phase gradient 失败：

      (1) 推理链长度差异：MATH-500 平均 >2000 tokens（DeepSeek），
      GPQA 平均 ~300-800 tokens。短推理链意味着 phase 间差异积累的 token 更少，
      compound interaction 的 phase-dependent 放大效应被稀释。
      Phase segmentation 在 <500 token 的推理链上，每个 phase 可能只有 100-150 tokens，
      统计量估计不稳定。

      (2) 推理结构差异：数学推理有明确的 "exploratory thinking → structured calculation → verification"
      阶段，这些阶段对应不同的 attention sparsity pattern（已由 think_phase_validation kappa=0.887 确认）。
      GPQA 的推理模式更异质——有些是知识检索（低依赖链），有些是逻辑推导（中等依赖链），
      有些是排除法（浅广搜索）。dense model 的 sparsity pattern 不一定形成
      数学推理那样清晰的 phase 结构。

      (3) s020 方向反转的机制：在某些 GPQA 问题上，"answer extraction" 阶段
      （通常对应 high-sparsity phase）的 compound interaction 可能反而高于
      "reasoning" 阶段，因为 GPQA 的答案需要精确引用科学事实或逻辑规则，
      这要求 attention 对 context 中特定 KV entries 有精确访问。
      而数学推理的 answer extraction 通常只需要从已计算的结果中提取数字，
      对 KV cache 的依赖更低。

      (4) n=50 功效问题：如果 GPQA 上的真实 effect size 很小（d_z < 0.3），
      n=50 的功效约 30%，大量 NS 结果是预期的。但 dose-response 非单调性
      不是功效问题——如果真实效应存在，方向至少应一致。
      s020 方向反转（negative median_diff）是质性失败，非功效问题。

    tables:
      - name: "Table: GPQA DS Importance Phase Gradient"
        content: |
          | Sparsity | median_diff | 95% CI          | Wilcoxon p | Bonf. p | d_z   |
          |----------|-------------|-----------------|------------|---------|-------|
          | s015     | 0.03        | [−0.02, 0.09]   | 0.18       | 0.72    | 0.22  |
          | s020     | −0.02       | [−0.10, 0.06]   | 0.65       | 1.00    | −0.08 |
          | s025     | 0.08        | [−0.03, 0.22]   | 0.09       | 0.36    | 0.30  |
          | s030     | 0.05        | [−0.08, 0.25]   | 0.15       | 0.60    | 0.18  |

      - name: "Table: Cross-Benchmark Comparison (DS importance median_diff)"
        content: |
          | Sparsity | MATH-500 (n=500) | GSM8K (n=50) | GPQA (n=50)    |
          |----------|------------------|--------------|----------------|
          | s015     | 0.391***         | 0.241***     | 0.03 NS        |
          | s020     | 1.215***         | 0.740***     | −0.02 NS (↻)  |
          | s025     | 3.986***         | 1.992***     | 0.08 NS        |
          | s030     | 8.481***         | 4.682***     | 0.05 NS        |
          | ρ        | 1.0              | 1.0          | 0.40           |
          Note: ↻ = direction reversal; *** = Bonferroni p<0.005

    figures_description:
      - >
        Fig: 三 benchmark phase gradient dose-response 对比。三条线（MATH-500=蓝实线，
        GSM8K=绿虚线，GPQA=红点线），x=sparsity level，y=median_diff (log scale for MATH/GSM)。
        MATH-500 和 GSM8K 都显示清晰的单调上升，GPQA 在零线附近波动且 s020 为负。
        GPQA 的 error bars（95% CI）全部跨越零线。

    analysis: >
      GPQA 4 个 sparsity level 的结果全面失败：零个 Bonferroni 显著，
      dose-response 非单调（s020 方向反转），Spearman ρ=0.40（NS）。
      这与 MATH-500（ρ=1.0, 全部 p<1e-70）和 GSM8K（ρ=1.0, 全部 p<0.001）
      形成质性差异。

      关键判断：这是 task-type boundary 而非 power 问题。
      如果仅是 n=50 功效不足，应预期方向一致但 p 值不显著——
      而 s020 的方向反转和 s030&lt;s025 的非单调性是质性不一致，
      即使 n=500 也不太可能变成单调显著。

      对论文的影响：
      - GPQA 结果放 Appendix 作为 negative result，或完全不纳入主文
      - Paper scope 明确限于 mathematical reasoning（MATH-500 + GSM8K）
      - Discussion 新增段落解释为何 phase modulation 可能是 math-reasoning-specific：
        结构化 CoT 的长链依赖是 phase gradient 的前提条件
      - Limitations 增加 "cross-task generalization remains an open question"


  # ============================================================
  # Experiment 3: GPQA QW Importance Sweep
  # ============================================================
  - name: "GPQA Qwen importance sweep (4 sparsity levels)"
    plan_id: gpqa_qw_importance_s015_to_s030
    description: >
      Qwen2.5-7B-Instruct, GPQA Diamond, importance masking at s015-s030。
      Cross-model replication of GPQA results。ROADMAP 线路 A 的一部分。
    expected_results:
      n_problems: 50
      importance_median_diff:
        s015: 0.01
        s020: 0.03
        s025: -0.01
        s030: 0.04
      importance_median_diff_ci:
        s015: [-0.03, 0.05]
        s020: [-0.04, 0.10]
        s025: [-0.08, 0.06]
        s030: [-0.06, 0.15]
      importance_wilcoxon_p:
        s015: 0.45
        s020: 0.32
        s025: 0.78
        s030: 0.22
      bonferroni_sig_count: 0
      dose_response_monotonic: false
      dose_response_pattern: "0.01, 0.03, -0.01, 0.04 (non-monotonic, s025 direction reversal)"
      spearman_rho: 0.20
      spearman_p: 0.80

    result_rationale: >
      Qwen2.5-7B-Instruct 在 MATH-500 上的 importance phase gradient 已知弱于
      DeepSeek（QW n=500 median_diff: 0.066→3.155 vs DS: 0.391→8.481，约 1/3 量级）。
      在 GPQA 上，这个已经较弱的信号进一步被稀释：
      (1) QW 在 GPQA 上的推理链可能更短（非数学不触发长 CoT），phase 分割更粗糙；
      (2) QW 的 compound interaction 效应量在 MATH-500 上已是 DS 的 ~1/3，
      在 GPQA 上预期进一步衰减到接近零；
      (3) s025 方向反转（与 DS 的 s020 反转位置不同）表明 phase gradient 
      失败不是系统性的"缺一个 sparsity level"，而是整个模式在 GPQA 上不稳健。
      两个模型在不同 sparsity level 出现方向反转，是 phase segmentation
      在非数学推理上不适用的强证据。

    tables:
      - name: "Table: GPQA QW Importance Phase Gradient"
        content: |
          | Sparsity | median_diff | 95% CI          | Wilcoxon p | Bonf. p |
          |----------|-------------|-----------------|------------|---------|
          | s015     | 0.01        | [−0.03, 0.05]   | 0.45       | 1.00    |
          | s020     | 0.03        | [−0.04, 0.10]   | 0.32       | 1.00    |
          | s025     | −0.01       | [−0.08, 0.06]   | 0.78       | 1.00    |
          | s030     | 0.04        | [−0.06, 0.15]   | 0.22       | 0.88    |

    figures_description:
      - >
        Fig: GPQA DS vs QW importance phase gradient。两 panel，每 panel 四个 bar
        （s015-s030），error bars = 95% CI。两模型都在零线附近波动，
        DS 在 s020 为负，QW 在 s025 为负。无一致方向。

    analysis: >
      QW 在 GPQA 上复制了 DS 的失败模式：全部 NS，dose-response 非单调。
      两个模型的方向反转出现在不同 sparsity level（DS: s020, QW: s025），
      排除了"某个 sparsity level 恰好在边界"的解释——如果 phase gradient 真实存在
      但效应弱，两模型应在相同方向上一致，即使 p 值不显著。
      Cross-model 方向不一致是 GPQA 上 phase gradient 不存在的强证据。


  # ============================================================
  # Experiment 4: GPQA Random Controls
  # ============================================================
  - name: "GPQA random masking controls (DS s025 + s030)"
    plan_id: gpqa_ds_random_controls
    description: >
      DeepSeek random masking on GPQA Diamond at s025/s030。
      ROADMAP 线路 A 规划的 2 个 random control conditions。
      测试 GPQA 上是否存在 importance/random separation。
    expected_results:
      n_problems: 50
      random_median_diff:
        s025: 0.05
        s030: 0.04
      random_median_diff_ci:
        s025: [-0.04, 0.15]
        s030: [-0.06, 0.16]
      random_wilcoxon_p:
        s025: 0.25
        s030: 0.30
      imp_rand_ratio:
        s025: 1.60
        s030: 1.25
      overall_imp_rand_ratio: 1.20
      strategy_separation: false

    result_rationale: >
      在 GPQA 上 importance gradient 本身已接近零/NS（DS s025 median_diff=0.08, s030=0.05），
      因此 imp/rand ratio 无信息量——分子分母都接近零，比值可以是任意正数。
      预测 ratio 在 0.5-2.0 范围内浮动：
      - s025: imp=0.08, rand=0.05, ratio=1.6——看似 importance 略大，
        但两者 CI 都跨零，差异无统计意义
      - s030: imp=0.05, rand=0.04, ratio=1.25——几乎无差异
      
      对比 MATH-500（ratio 15.5-38.6×, n=500）和 GSM8K（ratio 2.3-3.8×, n=50），
      GPQA 的 ratio ~1.2 表明在非数学推理上完全没有 strategy separation。
      这不是 "strategy specificity 在 GPQA 上也存在但更弱" ——
      而是 "phase gradient 在 GPQA 上不存在，所以 strategy 区分无从谈起"。

    tables:
      - name: "Table: GPQA Strategy Specificity (DS importance vs random)"
        content: |
          | Sparsity | Imp med_diff | Rand med_diff | Ratio | MATH-500 Ratio |
          |----------|-------------|---------------|-------|----------------|
          | s025     | 0.08 NS     | 0.05 NS       | 1.6   | 15.5×          |
          | s030     | 0.05 NS     | 0.04 NS       | 1.25  | 16.6×          |

    figures_description: []

    analysis: >
      GPQA random controls 确认了 worst 档预期：无 strategy separation。
      但需注意，这不是独立的 negative finding——它是 GPQA phase gradient 整体失败的
      downstream 后果。如果 base effect 不存在，strategy modulation 无从测量。
      在论文中，这应作为 GPQA negative result 的补充证据，
      而非独立的 "strategy specificity fails on GPQA" claim。


  # ============================================================
  # Experiment 5: GPQA Cross-Task Synthesis
  # ============================================================
  - name: "GPQA cross-task generalization synthesis"
    plan_id: gpqa_cross_task_synthesis
    description: >
      汇总 GPQA 全部 10 条件的结果，与 MATH-500 和 GSM8K 对比，
      评估 cross-task generalization 的整体状态。
    expected_results:
      gpqa_ds_bonferroni_sig_count: 0
      gpqa_qw_bonferroni_sig_count: 0
      gpqa_total_sig_count_out_of_10: 0
      gpqa_ds_dose_response_monotonic: false
      gpqa_qw_dose_response_monotonic: false
      gpqa_ds_spearman_rho: 0.40
      gpqa_qw_spearman_rho: 0.20
      gpqa_imp_rand_ratio_range: "0.5-2.0"
      cross_model_direction_consistency: false
      cross_benchmark_comparison:
        math500_sig_rate: "8/8 (DS+QW importance all Bonferroni sig)"
        gsm8k_sig_rate: "6/8 (importance all sig, random mixed)"
        gpqa_sig_rate: "0/10 (none significant)"
      task_complexity_gradient:
        math500_avg_chain_length: ">2000 tokens"
        gsm8k_avg_chain_length: "~800 tokens"
        gpqa_avg_chain_length: "~400 tokens"
      strategy_specificity_by_benchmark:
        math500_imp_rand_ratio: "15-36×"
        gsm8k_imp_rand_ratio: "2.3-3.8×"
        gpqa_imp_rand_ratio: "0.5-2.0×"

    result_rationale: >
      三个 benchmark 形成清晰的 task-complexity gradient：
      
      MATH-500（长链结构化数学推理, ~2000+ tokens）：
      Phase gradient 最强（DS median_diff 0.39→8.48），strategy specificity 最高（15-36×），
      全部显著。这是 phase-dependent compound severity 的"最佳条件"——
      长推理链提供足够的 token 来积累 phase-dependent 差异，
      结构化 CoT 的 exploration→calculation→verification 阶段
      自然映射到 high→mid→low sparsity phases。
      
      GSM8K（中链基础数学推理, ~800 tokens）：
      Phase gradient 存在但更弱（DS: 0.24→4.68, 约 MATH-500 的 1/2），
      strategy specificity 衰减至 2.3-3.8×。GSM8K 推理链更短，
      phase 间差异积累更少，但基本数学推理仍保持足够的 phase 结构。
      
      GPQA（短链非数学推理, ~400 tokens）：
      Phase gradient 消失。两个关键差异导致失败：
      (a) 推理链过短（~400 tokens），三段 phase 分割后每段仅 ~130 tokens，
      统计量估计极不稳定；
      (b) 非数学推理的 attention pattern 不形成数学 CoT 那样的清晰 phase 结构，
      quantile-based phase segmentation 捕获的不是有意义的 reasoning stage 转换，
      而是噪声。

      对论文叙事的影响：
      从 "phase modulation 是 universal property of reasoning LLMs"
      退缩为 "phase modulation 是 structured mathematical reasoning 的涌现属性"。
      这缩小了 novelty scope 但增加了 specificity——
      可以 argue 数学推理是最清晰的 "phase-structured" 推理范式，
      我们的发现精确刻画了这个 regime 的行为，
      泛化到其他推理类型是明确声明的 future work。

    tables:
      - name: "Table: Cross-Benchmark Phase Gradient Summary"
        content: |
          | Benchmark | Chain Length | Sig Rate   | ρ (DS) | ρ (QW) | Imp/Rand Ratio |
          |-----------|-------------|------------|--------|--------|----------------|
          | MATH-500  | ~2000 tok   | 8/8 (100%) | 1.0    | 1.0    | 15-36×         |
          | GSM8K     | ~800 tok    | 6/8 (75%)  | 1.0    | 1.0    | 2.3-3.8×       |
          | GPQA      | ~400 tok    | 0/10 (0%)  | 0.40   | 0.20   | 0.5-2.0×       |

    figures_description:
      - >
        Fig: Task-complexity gradient visualization。三列 panel (MATH-500, GSM8K, GPQA)。
        每列：上方 bar chart 为 DS importance median_diff × 4 sparsity levels（y-axis log），
        下方热力图为 per-phase II median（3×4 grid, phase×sparsity）。
        MATH-500 和 GSM8K 显示清晰的从左上到右下的 gradient pattern，
        GPQA 的热力图近乎均匀噪声。

    analysis: >
      GPQA 的全面失败将论文 scope 限定于数学推理。这对 EMNLP 投稿的影响：

      负面影响：
      - Reviewer 会问 "为什么只研究数学推理"——需要在 Related Work 和 Discussion 中
        充分论证数学 CoT 是 phase-structured reasoning 的 canonical case
      - "Phase-Dependent Compound Sparsity Severity in Reasoning LLMs" 中的 "Reasoning"
        实际只覆盖 math reasoning，可能被认为 overclaiming

      应对策略：
      - Title 加限定："...in Mathematical Reasoning LLMs" 或保持当前 title
        但在 abstract 第一句声明 scope
      - 将 task-complexity gradient (MATH>GSM8K>GPQA) 本身作为一个 finding：
        "phase modulation strength correlates with reasoning chain length and structural complexity"
        (虽然只有 3 个数据点，但方向清晰)
      - GPQA negative result 放 Appendix B，诚实报告，转化为 "scope boundary evidence"

      EMNLP main 可行性评估：
      - 缩小 scope 后仍有足够 novelty：phase gradient universality 跨模型/架构/benchmark（数学类），
        dose-response characterization，discrimination collapse 机制，methodology 贡献
      - 但 reviewer 对 generalizability 的 concern 无法用 GPQA 正面数据回应，
        需要其他策略（如 "math reasoning is the most important use case for reasoning LLMs"
        的 practical relevance argument）
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fba2c85d-d5b7-4117-be8d-c13067228a1d",
  "isSidechain": false,
  "requestId": "req_011Cb6UyQ7mWoU6XWEDZ4eT8",
  "type": "assistant",
  "uuid": "35babeb7-a21f-4532-a5f0-2121cadd5c4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "a3d601b9-90d6-4700-8195-7ac8fe55805b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J3o6oEJdUdGLXWfDtMqZPv",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3216,
      "cache_read_input_tokens": 101965,
      "output_tokens": 14602,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3216,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14602,
          "cache_read_input_tokens": 101965,
          "cache_creation_input_tokens": 3216,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3216
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

_source line 37_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：LLaMA n=250 高功效确认 strategy×phase 交互在 Llama 架构上可忽略；random phase gradient 稳健。GPQA 不显著或方向不一致。'Strategy-gated' 叙事崩塌——phase modulation 普遍存在但非 strategy-specific…",
  "leafUuid": "35babeb7-a21f-4532-a5f0-2121cadd5c4d",
  "sessionId": "a3d601b9-90d6-4700-8195-7ac8fe55805b"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "ai-title",
  "aiTitle": "Phase-dependent compound sparsity in reasoning models",
  "sessionId": "a3d601b9-90d6-4700-8195-7ac8fe55805b"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：LLaMA n=250 高功效确认 strategy×phase 交互在 Llama 架构上可忽略；random phase gradient 稳健。GPQA 不显著或方向不一致。'Strategy-gated' 叙事崩塌——phase modulation 普遍存在但非 strategy-specific…",
  "leafUuid": "35babeb7-a21f-4532-a5f0-2121cadd5c4d",
  "sessionId": "a3d601b9-90d6-4700-8195-7ac8fe55805b"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Phase-dependent compound sparsity in reasoning models",
  "sessionId": "a3d601b9-90d6-4700-8195-7ac8fe55805b"
}
```

---
