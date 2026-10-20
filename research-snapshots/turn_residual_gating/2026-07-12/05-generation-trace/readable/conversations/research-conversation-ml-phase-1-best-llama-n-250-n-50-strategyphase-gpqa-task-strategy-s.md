# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：LLaMA n=250 揭示 n=50 功效不足掩盖了中等 strategy×phase 交互；GPQA 确认跨 task 泛化且 strategy s

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 42
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-3/8ea52053-5c5d-477c-85fd-15c4d095d3f8.jsonl`
- **Structured JSON:** [`7a6f2694413b8c5cbe1a.json`](../../sessions/7a/7a6f2694413b8c5cbe1a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T15:05:31.508Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T15:05:31.508Z",
  "sessionId": "8ea52053-5c5d-477c-85fd-15c4d095d3f8",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：LLaMA n=250 揭示 n=50 功效不足掩盖了中等 strategy×phase 交互；GPQA 确认跨 task 泛化且 strategy specificity 强。三维交互叙事完全成立。\n核心假设：['LLaMA imp_vs_rand d_z 在 n=50 被噪声衰减；n=250 揭示真实中等效应（d_z≥0.4 at s030）', 'LLaMA random phase gradient 在 n=50 被过估；n=250 收缩至 d_z<0.25（小效应或 NS）', 'GPQA importance phase gradient Bonferroni 显著；imp/rand ratio ≥5×', 'C8 从 partially_confirmed 升级为 confirmed；strategy×phase 交互跨架构成立']\n关键指标范围：{'llama_n250_imp_vs_rand_dz_s030': [0.45, 0.6], 'llama_n250_imp_vs_rand_dz_s025': [0.35, 0.5], 'llama_n250_bonferroni_sig_count_out_of_4': [3, 4], 'llama_n250_random_phase_gradient_dz': [0.1, 0.25], 'llama_n250_importance_phase_gradient_dz': [1.0, 1.2], 'gpqa_ds_s015_median_diff': [0.25, 0.5], 'gpqa_bonferroni_p': [1e-06, 0.01], 'gpqa_imp_rand_ratio': [5, 20]}\n叙事方向：原始 framing \"phase-gated compound sparsity\" 完全成立。 Strategy × phase × compound 三维交互在三模型（DS/QW/LLaMA）、两架构（Qwen2/Llama）、 三 benchmark（MATH-500/GSM8K/GPQA）上一致复现。LLaMA n=250 高功效下 imp_vs_rand d_z 达中等效应量，random phase gradient 收缩至不显著或可忽略， 消除 n=50 的 architecture-dependent 限定。GPQA 提供第三 benchmark + 跨推理领域 （科学→数学）泛化。C8 升级为 confirmed，论文 claims 无需调整。 Title/framing 保持 \"phase-gated\"，EMNLP main 正会强竞争力—— novelty 同时具备现象发现（三维交互）和机制解释（discrimination collapse）， 泛化证据覆盖模型/架构/任务三个维度。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: phase-gated-compound-sparse\nvenue: EMNLP 2026\nfocus: 重点评估：(1) cross-architecture generalization 从 n=49 升级到 n=250 后是否足够支撑 claim，量级差 25× 如何在论文中定位；(2) GPQA cross-task 扩展对 scope 短板的修复力度；(3) 当前 framing 作为正会投稿的竞争力，novelty 是否站得住\n\n## paper_framing.md\n\n# Paper Framing — Phase-Gated Compound Sparsity\n\n> 最后更新: 2026-05-16 (数值对齐 n=500 registry: DS median_diff 0.39/1.21/3.99/8.48; QW 0.07/0.31/1.07/3.16; Cohen's d registry 0.61→1.13/0.37→1.44; C7+C10 status→confirmed; imp/rand 2.7-15×) | 维护者: Director\n\n## Core Insight\n\nCompound sparsity（attention head pruning + KV cache eviction）的 severity 不是固定常数——它是 eviction strategy 和 reasoning phase 交互的涌现属性。Importance-based eviction 的 compound interaction severity（paired median difference: median(II_low_i − II_high_i)）随 sparsity 单调递增（DeepSeek: 0.39→1.21→3.99→8.48; Qwen: 0.07→0.31→1.07→3.16），而 random masking 在 s015/s020 NS，在 s025 跨模型显著但效应量远小于 importance（DS: 0.257 vs 3.986; QW: 0.393 vs 1.074, 2.7-15×差异），存在 sparsity threshold ~s020-s025（D063; s030 待定）。Cohen's d（per-problem paired, B=10000）从 medium 到 large（DeepSeek: 0.61→1.13; Qwen: 0.37→1.44，registry cohens_d s015→s030）。LLaMA 跨架构验证（D060）qualitative direction consistent（within-importance d_z~1.0），但 strategy×phase 交互弱于 Qwen2 架构（imp_vs_rand d_z 0.19→0.34, 仅 s030 显著），且 random 在 LLaMA 上也显示显著 phase gradient（d_z 0.35→0.44），与 DeepSeek/Qwen random 低 sparsity NS 模式定性不同。GSM8K 跨 benchmark 验证（D075）：importance masking 的 phase gradient 在 GSM8K 上同样单调递增（QW: 0.039→0.158→1.100→2.092; DS: 0.241→0.740→1.992→4.682），但 strategy specificity（importance/random gradient ratio）从 MATH-500 的 15-36× 衰减至 GSM8K 的 2.3-3.8×。注意：\"反转\"仅在原始 II_low 值上（random > importance），phase gradient 层面 importance ≥ random。Strategy specificity 的 task-dependence 机制是开放问题（见 §6 Discussion）。这一发现挑战了 compound degradation 均匀分布的隐含假设。\n\n**数字基准**：所有数字基于 bf16 per-problem paired 统计量（B=10000 bootstrap）。median_diff 定义为 median(II_low_i − II_high_i)（逐 problem 配对差的中位数）。fp16 旧数据已弃用。\n\n## Narrative Arc\n\nCompound sparsity 是高效 LLM 推理的实用部署需求，但 prior work（SparK, Ada-KV, SLiM）将 compound interaction 视为均匀超可加。我们发现 severity 是 strategy × phase 交互的涌现属性：importance eviction 的 compound interaction 在 low-sparsity phase 远大于 high-sparsity phase（paired median difference 单调递增 0.39→8.48），而 random eviction 在低 sparsity (s015/s020) NS，在 s025+ 跨模型显著但效应量远小于 importance (2.7-15×)——存在 sparsity threshold (~s020-s025)，低于阈值 compound effect importance-specific，高于阈值两者均触发但 importance 主导。Cross-model replication 方向一致（Qwen magnitude ~1/4 of DeepSeek，onset threshold s≥0.20）。LLaMA 跨架构验证已完成（c3_llama, D060）：qualitative direction consistent（importance phase gradient d_z≈1.0），但 imp_vs_rand 交互弱（d_z 0.19→0.34, 仅 s030 显著），且 random 也显示非平凡 phase gradient（d_z 0.35→0.44），strategy-dependence 强度 architecture-dependent。我们通过 discrimination collapse 机制解释这一现象：head pruning → importance score 的判别力崩塌（Gini/CV 下降跨模型一致）→ importance eviction 退化为有偏伪随机。Attention entropy redistribution 作为 model-dependent secondary effect 在 DeepSeek 上观察到，但在 Qwen 上不稳健（D044）。\n\n**Framing 硬约束（D015）**：\n- MUST: \\\\\\\"emergent phase-strategy interaction\\\\\\\"\n- MUST NOT: \\\\\\\"importance metric limitation / importance is broken\\\\\\\"\n- MUST NOT: claim \\\\\\\"importance masking produces super-additive interaction\\\\\\\" without qualifier — random masking also produces positive II, and at s025+ random is statistically significant (D063). The distinguishing signal is **magnitude gradient** (importance 2.7-15× larger) and **onset threshold** (random NS below ~s020, importance significant from s015+), not the existence of super-additivity itself (D023)\n\n## Core Claims\n\n| ID | Claim | Status | Key Evidence |\n|----|-------|--------|-------------|\n| C1 | Compound sparsity severity is strategy- and task-modulated | confirmed | MATH-500: importance gradient 15-36× random; GSM8K: ratio 衰减至 2.3-3.8× (D075)。Phase gradient 层面 importance ≥ random 跨 benchmark 成立，但 magnitude ratio task-dependent。Threshold ~s020-s025 (D063) |\n| C2 | Severity is phase-modulated (amplified in low-sparsity phase) | confirmed | bf16 paired median difference 单调递增: 0.39→1.21→3.99→8.48; Bonferroni p<0.005 全 4 水平 (D032)。预注册：n=500 后若 QW s015 CI 仍跨零，叙事改为 'compound effect emerges above threshold sparsity (~s020)' |\n| C3 | Phase-strategy crossover exists | confirmed | s=0.25: importance high_phase=0.032 < random=0.818, importance low_phase=7.196 > random=1.363 (bf16) |\n| C4 | Discrimination collapse as primary mechanism; entropy redistribution model-dependent | partially_confirmed | D044: Gini/CV 下降跨模型一致; entropy collapse DeepSeek 一致但 Qwen s025 反转(+0.045) s030≈0。30/30 problems completed. |\n| C5 | Phase-modulated compound severity generalizes across models | confirmed | DeepSeek + Qwen cross-model replication: 方向一致, Cohen's d ρ=1.0, gradient permutation p=0.043. Qwen magnitude ~1/4 of DeepSeek, onset threshold s≥0.20 (S3→C). |\n| C5b | Phase-aware mitigation recovers compound degradation | future_work | D056: pilot 完成 gate_failed。Oracle recovery 18% < 30% gate (Wilcoxon p=0.002)，heuristic 32% 但 CI 跨零。方向正确但效应量不足，需更精细 phase boundary estimation → future work |\n| C6 | Severity gradient is sub-exponential | confirmed | Growth rate decreasing: Δ增长因子 3.8×→4.8×→2.0×（递减） |\n| C7 | Statistical power at n=500 confirms dose-response | confirmed | c2_n500_deepseek (success) + c2_qw_n500_r3 (success): 两模型 n=500 全 4 sparsity Bonferroni p<0.005, Spearman ρ=1.0 |\n| C8 | Cross-architecture validation (LLaMA) | partially_confirmed | D060: within-importance phase gradient 强(d_z~1.0) ✓，但 imp_vs_rand 交互弱(d_z 0.19→0.34, 仅 s030 Bonferroni p=0.029 显著)。**关键**：random 在 LLaMA 上也显示显著 phase gradient(d_z 0.35→0.44, CI 排除零)，与 DeepSeek/Qwen random 低 sparsity NS 模式定性不同。Qualitative direction consistent, quantitative strategy×phase interaction weaker + architecture-dependent。论文禁用 \"confirms\"，改用 \"suggests\"/\"provides partial support\"。 |\n| C9 | Differentiation from Lethe/SparK prior work | planned | Related Work §2 引用区分 + SparK gap analysis |\n| S3→C | Onset threshold is model-dependent (DeepSeek s≥0.15, Qwen s≥0.20) | confirmed | D037/D038: Qwen s015 d_z=0.37 CI含0, s020+ 显著 |\n| C10 | Phase gradient cross-benchmark robust; strategy specificity task-modulated | confirmed | GSM8K DS gradient 0.241→4.682 单调递增; QW gradient 0.039→2.092; imp/rand ratio 衰减至 2.3-3.8× (D075)。QW random s025+s030 均 success |\n| S7→C | Dose-response monotonicity (Spearman ρ=1.0) | confirmed | D047: 6-point dose-response, 单调递增 |\n\n## Anticipated Reviewer Concerns\n\n### RC1: Generalizability — 7B models only, benchmark scope\n- **预期质疑**: \\\"Results on two 7B models and MATH-500 only. How do we know this generalizes to larger models or other reasoning tasks?\\\"\n- **应对**: 四层泛化证据：(1) Cross-model: DeepSeek-R1-Distill-Qwen-7B + Qwen2.5-7B-Instruct（同架构不同训练，ρ=1.0）(2) Cross-architecture: c3_llama (DeepSeek-R1-Distill-Llama-8B, LlamaForCausalLM)，qualitative direction consistent，但需加限定——LLaMA 上 random 也显示 phase gradient，strategy × phase 交互弱于 Qwen2 架构（D060）(3) **Cross-benchmark (D075)**: GSM8K（两模型）phase gradient 单调递增复现（DS: 0.241→4.682; QW: 0.039→2.092），但 strategy specificity ratio 从 MATH-500 15-36× 衰减至 2.3-3.8×，表明 phase modulation 跨 benchmark 稳健而 magnitude modulation task-dependent。Limitations 诚实声明：(a) 7B scale only；(b) strategy specificity 强度 task-dependent（GSM8K 衰减，可能因推理链更短）；(c) LLaMA 跨架构验证 n=50 限制功效；(d) random phase gradient 行为 architecture-dependent。\n- **实验支撑**: C5 (cross-model) + C8 (c3_llama cross-architecture) + C10 (cross-benchmark GSM8K, D075)\n\n### RC2: Mechanism — entropy-discrimination collapse 缺乏直接测量\n- **预期质疑**: \\\"The mechanism is conceptual. Where is the empirical evidence for entropy increase and discrimination collapse?\\\"\n- **应对**: c4_entropy 实验已完成（DeepSeek 30/30 + Qwen 30/30）。D044 结论：Gini/CV 下降跨模型一致（discrimination collapse confirmed）；entropy redistribution 在 DeepSeek 上一致但在 Qwen 上 s025 方向反转、s030 近零（model-dependent）。论文以 discrimination collapse 为主线，entropy 作 DeepSeek 特有的强化因素。\n- **实验支撑**: c4_entropy (DeepSeek DONE) + qwen_c4_entropy (DONE, negative for entropy universality)\n\n### RC3: Practical impact — 没有 throughput 数据\n- **预期质疑**: \\\"No wall-clock or throughput measurements. Is the severity amplification reflected in actual inference speed?\\\"\n- **应对**: 本文定位是 empirical finding paper（发现 + 机制解释），不是 method paper。Throughput 不是 claim 的一部分。Discussion 中明确 phase-gated controller 作为 future direction。\n  - C5b pilot 已完成（D056）：oracle recovery 18%（Wilcoxon p=0.002），heuristic recovery 32%（p=0.024），但两者 95% CI 均跨零。方向正确（Wilcoxon 显著）但效应量不足（未达 30% gate），需更精细的 phase boundary estimation。论文 §6 Discussion 诚实报告 pilot 结果 + future work。\n  - Heuristic > oracle 悖论值得提及：token position ratio 粗粒度划分可能恰好更适合 mitigation 场景，暗示 phase boundary 的最优粒度是开放问题。\n- **实验支撑**: c5b_pilot (gate_failed, D056)\n\n### RC4: Statistical rigor — bootstrap 是否足够\n- **预期质疑**: \\\"Per-problem bootstrap with 50 problems — sufficient sample size?\\\"\n- **应对**: bf16 使用 B=10000 per-problem paired bootstrap，有效配对数 n=49 (DeepSeek) / n=46 (Qwen)；n=500 实验进一步验证 (C7 running)。Permutation test 使用 paired median difference 作为 robust statistic（D032），Bonferroni 校正后全 4 水平 p<0.005。Dose-response 主用 Wilcoxon signed-rank p + median_diff（robust to outliers），Cohen's d 作为辅助效应量（DeepSeek 0.61→1.13, Qwen 0.37→1.44, registry cohens_d s015→s030），注释高 sparsity 下 d 受 outlier-driven variance 影响（DS s020→s025: median 3.3× jump 但 d 非单调，因极端 II 值影响分母，D064）。可在 appendix 补充 per-problem 分布图（已生成 fig4_per_problem_dist.pdf）。\n- **实验支撑**: bf16 permutation test (D032) + Cohen's d per-problem paired (rebootstrap B=10000) + n=500 Wilcoxon (C7 running)\n\n### RC5: Novelty — prior work 是否已覆盖 phase-dependent sparsity\n- **预期质疑**: \"ThinKV and phase-aware methods already consider phase. What's new?\"\n- **应对**: Prior work 在单轴上分析 phase（ThinKV: phase-aware eviction）或 compound（SparK: joint compression）。没有工作同时分析 compound × phase × strategy 的三维交互。Crossover 现象（同一 strategy 在不同 phase 方向反转）是全新发现。Related Work 加 Lethe 引用区分 + SparK 对比。具体区分：\n  - **ThinKV** (arxiv 2510.01290, Oct 2025): 在 KV cache 单轴上做 phase-aware 压缩（按 CoT 阶段差异化 eviction），但不涉及 pruning × eviction 的 compound interaction。我们研究的是双轴（head pruning × KV eviction）compound interaction 如何随 phase 变化，ThinKV 的单轴 phase-aware 策略是我们分析维度的子集。\n  - **Physics of KV Cache Compression** (arxiv 2603.01426, Mar 2026): 揭示了单轴 KV 压缩的 phase transition 和 representational rigidity，是机制层面最接近的工作。关键区分：他们刻画的是单一压缩轴上压缩率的 critical threshold（phase transition），我们刻画的是两种压缩方法的 compound interaction severity 如何被 reasoning phase 调制（phase-dependent gradient）——维度正交。\n  - **HIES** (arxiv 2510.13832, Oct 2025): 发现 importance score collapse 并提出 entropy 补偿，为我们的 discrimination collapse 机制提供独立 supporting evidence——他们在单轴上观察到的 score collapse 正是我们在 compound setting 中发现的 Gini/CV 下降的单轴对应。\n  - **R-KV** (arxiv 2505.24133, May 2025): 针对 reasoning task 做 KV compression 优化，属于 task-specific method。我们不是提出新方法，而是 mechanistic 分析 compound interaction 的 phase-dependent 行为，二者目标不同（optimization vs understanding）。\n- **实验支撑**: C3 (crossover), Related Work §2 的 gap 分析\n\n### RC6: Novelty vs Lethe/SparK\n- **预期质疑**: \"How does this differ from Lethe (AAAI 2026) which also does layer-time-adaptive KV pruning, or SparK which studies compound compression?\"\n- **应对**: Lethe 和 SparK 都没有分析 phase × strategy 的交互效应。Lethe 是 method paper（提出 adaptive eviction 方法），我们是 empirical finding paper（发现 phase-dependent severity gradient）。SparK 研究 compound compression 但将 interaction 视为均匀超可加，我们发现 interaction severity 随 phase 和 strategy 变化。新近工作进一步确认我们的独特定位：\n  - **Physics of KV Cache Compression** (arxiv 2603.01426, Mar 2026) 是最近的相关工作，研究单轴压缩的 phase transition 阈值行为。与我们的核心区别：他们的 phase transition 是压缩率维度上的 critical point，我们的 phase-dependent gradient 是 reasoning phase 维度上 compound interaction 的连续调制——两者刻画的 \"phase\" 语义不同（compression-rate phase vs reasoning phase）。\n  - **ThinKV** (arxiv 2510.01290, Oct 2025) 和 **R-KV** (arxiv 2505.24133, May 2025) 都在 KV compression 单轴上引入 phase/reasoning awareness，但均未涉及 compound interaction。我们的贡献在于揭示 pruning × eviction 双轴交互如何被 reasoning phase 调制，这是单轴方法无法观察到的涌现现象。\n  - **HIES** (arxiv 2510.13832, Oct 2025) 的 importance score collapse 发现为我们的 discrimination collapse 机制提供了独立佐证，但 HIES 聚焦于单轴补偿方法，未研究 collapse 在 compound setting 中的放大效应。\n  - Related Work §2 明确区分三者定位：Lethe/SparK = method/compound method, ThinKV/R-KV = single-axis phase-aware, Physics of KV = single-axis phase transition, HIES = single-axis collapse。我们 = compound × phase × strategy 三维交互分析。\n- **实验支撑**: 不需要额外实验，仅需 §2 引用区分\n\n## Paper Positioning\n\n**类型**: Empirical finding paper（非 method paper）\n**核心贡献**:\n1. 发现 compound sparsity severity 的 strategy × phase 交互\n2. 量化 severity gradient（bf16 paired median difference 0.39→8.48, Cohen's d 0.61→1.13）和 crossover 现象\n3. 提出 discrimination collapse 机制解释（Gini/CV 跨模型一致；entropy redistribution model-dependent）\n4. Cross-model + cross-architecture (LLaMA) replication 验证泛化性（三模型两架构；LLaMA partially_confirmed，strategy×phase 交互强度 architecture-dependent, D060）\n\n**投稿目标**: EMNLP 2026 ARR, deadline 2026-05-25\n**Rebuttal 准备**: Day 9 (2026-05-23) 预留 rebuttal letter 写作时间\n**关键时间线**：\n- Day 9 (2026-05-23): 预留写 rebuttal letter\n- Day 11 (2026-05-25): EMNLP 2026 ARR 截稿\n\n\n## experiment_plan (with registry status)\n\n- id: c1_bf16_importance_s025\n  claim: C1\n  description: 'II median: high=0.032, mid=1.118, low=7.196; importance masking shows\n    strong phase gradient'\n  registry_id: bf16_importance_s025\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics: &id003\n    interaction_index:\n      high:\n        mean: 0.302756\n        median: 0.032363\n        ci:\n        - 0.083714\n        - 0.543977\n        winsorized_mean: 0.200962\n        skewness: 4.8826\n      mid:\n        mean: 5.729665\n        median: 1.118069\n        ci:\n        - 3.455574\n        - 8.471799\n        winsorized_mean: 4.189902\n        skewness: 8.2799\n      low:\n        mean: 25.852951\n        median: 7.195958\n        ci:\n        - 19.077082\n        - 33.497293\n        winsorized_mean: 19.319103\n        skewness: 7.3986\n    per_problem_ii_stats:\n      high:\n        n: 49\n        min: -0.316321\n        max: 4.003714\n        mean: 0.133714\n        median: 0.009873\n        std: 0.595358\n      mid:\n        n: 40\n        min: -0.024794\n        max: 18.720486\n        mean: 2.537744\n        median: 1.05707\n        std: 3.962575\n      low:\n        n: 50\n        min: -1.854733\n        max: 75.467653\n        mean: 11.28281\n        median: 3.954593\n        std: 16.620011\n    gradient_paired_aggregate_legacy: 222.35\n    median_difference: 7.1636\n    n_problems: 50\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: false\n      overall: PASS\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    perplexity:\n      high:\n        dense: 1.1689\n        attn: 1.6511\n        kv: 1.8628\n        both: 2.7026\n      mid:\n        dense: 1.2269\n        attn: 1.7039\n        kv: 5.6205\n        both: 13.3436\n      low:\n        dense: 1.2286\n        attn: 1.8366\n        kv: 31.756\n        both: 63.668\n- id: c1_bf16_ds_rand_s025\n  claim: C1\n  description: 'Random II median: high=0.818, mid=0.932, low=1.363; flat gradient\n    vs importance'\n  registry_id: bf16_ds_rand_s025\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 3.59\n        median: 0.8182\n        ci:\n        - 1.4021\n        - 6.2327\n        median_ci:\n        - 0.5075\n        - 1.7217\n        winsorized_mean: 6.3965\n        skewness: -7.57\n      mid:\n        mean: -1.8455\n        median: 0.9324\n        ci:\n        - -10.3663\n        - 4.9342\n        median_ci:\n        - 0.7331\n        - 1.7003\n        winsorized_mean: 3.1014\n        skewness: -12.76\n      low:\n        mean: 0.7212\n        median: 1.3627\n        ci:\n        - -4.2068\n        - 4.5006\n        median_ci:\n        - 1.0869\n        - 2.6866\n        winsorized_mean: 4.1866\n        skewness: -15.85\n    perplexity:\n      high:\n        dense: 1.1687\n        attn: 7.237\n        kv: 4.9751\n        both: 17.7423\n      mid:\n        dense: 1.2269\n        attn: 868.3199\n        kv: 5.1165\n        both: 29.4661\n      low:\n        dense: 1.2284\n        attn: 24.3571\n        kv: 6.7993\n        both: 17.9694\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    n_problems: 50\n    pass_fail:\n      ci_overlap: false\n      sign_reversal: false\n      overall: FAIL\n    median_difference: 0.5445\n- id: c1_bf16_qw_imp_s025\n  claim: C1\n  description: 'Qwen cross-model: median_diff=1.109, Cohen''s d=1.233, p<1e-5'\n  registry_id: bf16_qw_imp_s025\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics:\n    median_difference: 1.108706\n    permutation_p: 0\n    cohens_d: 1.2329\n    bootstrap_ci_95:\n    - 0.609247\n    - 1.469002\n    wilcoxon_p: 0\n    n_bootstrap: 10000\n    n_paired: 46\n- id: c1_sf5_asymmetric_spot\n  claim: C1\n  description: 'Asymmetric configs: h02_kv03 D=19.13, h03_kv02 D=18.25; gradient consistent'\n  registry_id: sf5_asymmetric_spot\n  role: ablation\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics:\n    config_a_h02_kv03:\n      II_low: 19.51\n      II_mid: 6.05\n      II_high: 0.38\n      D: 19.13\n    config_b_h03_kv02:\n      II_low: 18.77\n      II_mid: 3.97\n      II_high: 0.52\n      D: 18.25\n    pre_registered_criterion_passed: true\n    gradient_direction: II_low >> II_mid >> II_high (consistent with symmetric baseline)\n- id: c1_c2_accuracy_eval\n  claim: C1\n  description: 'DS dense->s030 acc: 0.52->0.10 (-0.42); QW dense->s030: 0.32->0.14\n    (-0.18)'\n  registry_id: c2_accuracy_eval\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics:\n    n_problems: 50\n    ds_dense_acc: 0.52\n    ds_s015_acc: 0.36\n    ds_s015_delta: -0.16\n    ds_s030_acc: 0.1\n    ds_s030_delta: -0.42\n    qw_dense_acc: 0.32\n    qw_s015_acc: 0.34\n    qw_s015_delta: 0.02\n    qw_s030_acc: 0.14\n    qw_s030_delta: -0.18\n    ds_s030_chinese_reasoning_rate: 0.4\n    ds_dense_truncation_rate: 0.56\n    note: v2 rescored with fixed radical+degree matcher. DS s015 34→36, QW s015 32→34\n- id: c2_bf16_importance_s030\n  claim: C2\n  description: 'Phase gradient: II low=14.64 >> mid=2.28 >> high=0.053 (median); low/high\n    ratio ~276x'\n  registry_id: bf16_importance_s030\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics: &id001\n    interaction_index:\n      high:\n        mean: 0.5547\n        median: 0.0534\n        ci:\n        - 0.2773\n        - 0.9198\n        winsorized_mean: 0.3367\n        skewness: 10.62\n      mid:\n        mean: 11.3\n        median: 2.2833\n        ci:\n        - 6.865\n        - 17.2633\n        winsorized_mean: 8.1752\n        skewness: 9.19\n      low:\n        mean: 57.7946\n        median: 14.6395\n        ci:\n        - 41.4416\n        - 77.0467\n        winsorized_mean: 39.3143\n        skewness: 8.31\n    per_problem_ii_stats:\n      high:\n        n: 49\n        min: -0.5095\n        max: 4.4457\n        mean: 0.1976\n        median: 0.0343\n        std: 0.6793\n      mid:\n        n: 40\n        min: -0.1989\n        max: 34.0258\n        mean: 5.2585\n        median: 1.5173\n        std: 7.9382\n      low:\n        n: 50\n        min: -7.3027\n        max: 126.7985\n        mean: 22.6601\n        median: 9.9731\n        std: 28.4096\n    gradient_paired_aggregate_legacy: 57.24\n    median_difference: 14.5861\n    n_problems: 50\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: false\n      overall: PASS\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    perplexity:\n      high:\n        dense: 1.1689\n        attn: 1.7123\n        kv: 2.0544\n        both: 3.2372\n      mid:\n        dense: 1.2269\n        attn: 1.7894\n        kv: 9.4821\n        both: 24.2847\n      low:\n        dense: 1.2286\n        attn: 1.9347\n        kv: 51.6485\n        both: 122.61\n- id: c2_v6_importance_s030\n  claim: C2\n  description: II low_median=34.69, mid_median=7.27, high_median=0.88; bootstrap_gradient=41.92,\n    CI=[19.14,299.76]\n  registry_id: v6_importance_s030\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 0.8833\n    ii_mid_median: 7.2706\n    ii_low_median: 34.6937\n    ii_high_mean: 1.5151\n    ii_mid_mean: 78.8215\n    ii_low_mean: 1163.9677\n    per_problem_ii_count: 50\n    n_high: 40\n    n_mid: 22\n    n_low: 20\n    problems: 50\n    bootstrap_gradient_paired: 41.92\n    bootstrap_ci_paired:\n    - 19.14\n    - 299.76\n    bootstrap_gradient_unpaired: 39.28\n    bootstrap_ci_unpaired:\n    - 21.87\n    - 129.59\n    bootstrap_p: 0\n- id: c2_think_phase_validation\n  claim: C2\n  description: Phase segmentation kappa=0.887; thinking=57.8% low-sparsity, answer=62.7%\n    high-sparsity\n  registry_id: think_phase_validation\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics:\n    effective_n: 48\n    skipped_problems: 2\n    median_kappa: 0.887\n    thinking_in_low_sparsity_phase: 0.578\n    answer_in_high_sparsity_phase: 0.627\n    note: Phase segmentation based on dense model — 4 sparsity conditions share identical\n      phase boundaries, effective sample n=48 not n=192\n- id: c2_acc_qw_s030_n100\n  claim: C2\n  description: QW importance s030 accuracy=0.19 (n=100); dose-response monotonic decline\n    from dense=0.40\n  registry_id: acc_qw_s030_n100\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics:\n    batch1_correct: 7\n    batch1_total: 50\n    batch1_acc: 0.14\n    batch1_source: acc_qw_s030_b1_8k (v2, 8k tokens)\n    batch2_correct: 12\n    batch2_total: 50\n    batch2_acc: 0.24\n    combined_correct: 19\n    combined_total: 100\n    combined_acc: 0.19\n- id: c2_acc_ds_s015_8k_v2\n  claim: C2\n  description: DS s015 accuracy=0.48 vs dense=0.74; early onset of compound degradation\n  registry_id: acc_ds_s015_8k_v2\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.48\n    correct: 24\n    total: 50\n    truncation_rate: 0.32\n    truncated_count: 16\n    non_truncated_accuracy: 0.706\n    non_truncated_correct: 24\n    non_truncated_total: 34\n    wall_time_s: 3967\n    max_new_tokens: 8192\n- id: c3_v6_importance_s025\n  claim: C3\n  description: 'Importance: II low_median=24.16 >> high_median=0.66; strong phase\n    gradient (36x ratio)'\n  registry_id: v6_importance_s025\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 0.6641\n    ii_mid_median: 5.3067\n    ii_low_median: 24.1619\n    ii_high_mean: 0.8842\n    ii_mid_mean: 10.057\n    ii_low_mean: 71.8854\n    per_problem_ii_count: 50\n    n_high: 42\n    n_mid: 23\n    n_low: 21\n    problems: 50\n    bootstrap_gradient_paired: 35.72\n    bootstrap_ci_paired:\n    - 9.52\n    - 101.54\n    bootstrap_gradient_unpaired: 36.38\n    bootstrap_ci_unpaired:\n    - 13.19\n    - 97.61\n    bootstrap_p: 0\n- id: c3_v6_random_s025\n  claim: C3\n  description: 'Random: II low_median=2.91 ~ high_median=3.00; flat phase gradient\n    (bootstrap_p=0.559)'\n  registry_id: v6_random_s025\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 3.0024\n    ii_mid_median: 2.9846\n    ii_low_median: 2.9146\n    ii_high_mean: 3.9052\n    ii_mid_mean: 7.9491\n    ii_low_mean: 3.9114\n    per_problem_ii_count: 50\n    n_high: 36\n    n_mid: 25\n    n_low: 24\n    bootstrap_gradient_paired: -0.1199\n    bootstrap_ci_paired:\n    - -1.517\n    - 1.2461\n    bootstrap_p: 0.559\n    bootstrap_gradient_unpaired: -0.8616\n    bootstrap_ci_unpaired:\n    - -3.3911\n    - 1.5169\n    per_problem_ii_stats:\n      high:\n        min: -6.1388\n        max: 25.2471\n        mean: 4.4098\n        median: 3.0421\n        std: 6.0734\n      mid:\n        min: 0.158\n        max: 108.7242\n        mean: 7.5626\n        median: 2.1407\n        std: 20.926\n      low:\n        min: -0.1953\n        max: 12.8555\n        mean: 3.5806\n        median: 2.7289\n        std: 3.4915\n    verdict: FAIL\n- id: c3_bf16_importance_s020\n  claim: C3\n  description: 'Importance: II low=1.50, mid=0.20, high=0.015 (median); clear phase\n    separation'\n  registry_id: bf16_importance_s020\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics: &id002\n    interaction_index:\n      high:\n        mean: 0.1289\n        median: 0.0145\n        ci:\n        - -0.1975\n        - 0.6647\n        winsorized_mean: -0.0297\n        skewness: 16.67\n      mid:\n        mean: 1.2604\n        median: 0.2027\n        ci:\n        - 0.7466\n        - 1.8962\n        winsorized_mean: 0.766\n        skewness: 7.05\n      low:\n        mean: 6.0288\n        median: 1.4963\n        ci:\n        - 4.4671\n        - 7.9237\n        winsorized_mean: 4.3426\n        skewness: 6.01\n    per_problem_ii_stats:\n      high:\n        n: 49\n        min: -0.1884\n        max: 0.4196\n        mean: 0.0025\n        median: 0.0036\n        std: 0.0966\n      mid:\n        n: 40\n        min: -0.0519\n        max: 8.6969\n        mean: 0.6795\n        median: 0.1977\n        std: 1.4998\n      low:\n        n: 50\n        min: -1.6151\n        max: 22.6875\n        mean: 2.2301\n        median: 1.128\n        std: 4.3758\n    gradient_paired_aggregate_legacy: 5.9\n    median_difference: 1.4818\n    n_problems: 50\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: false\n      overall: PASS\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    perplexity:\n      high:\n        dense: 1.1689\n        attn: 1.5233\n        kv: 1.6191\n        both: 2.1047\n      mid:\n        dense: 1.2269\n        attn: 1.5375\n        kv: 3.5164\n        both: 5.4246\n      low:\n        dense: 1.2286\n        attn: 1.6486\n        kv: 15.7987\n        both: 23.74\n- id: c3_bf16_ds_rand_s020\n  claim: C3\n  description: 'Random: II high=0.292, mid=0.350, low=0.276 (median); no phase separation'\n  registry_id: bf16_ds_rand_s020\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 1.1216\n        median: 0.2918\n        ci:\n        - 0.0796\n        - 2.5834\n        median_ci:\n        - 0.1598\n        - 0.4581\n        winsorized_mean: 1.7664\n        skewness: 9.59\n      mid:\n        mean: -1.5827\n        median: 0.3504\n        ci:\n        - -6.0963\n        - 1.5735\n        median_ci:\n        - 0.1993\n        - 0.5226\n        winsorized_mean: 0.5839\n        skewness: -12.31\n      low:\n        mean: -0.4116\n        median: 0.2763\n        ci:\n        - -2.6034\n        - 1.209\n        median_ci:\n        - 0.2194\n        - 0.5487\n        winsorized_mean: 0.9942\n        skewness: -10.07\n    perplexity:\n      high:\n        dense: 1.1687\n        attn: 3.1905\n        kv: 3.8002\n        both: 8.8129\n      mid:\n        dense: 1.2269\n        attn: 67.8504\n        kv: 3.788\n        both: 11.4974\n      low:\n        dense: 1.2284\n        attn: 8.592\n        kv: 5.0078\n        both: 9.2001\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    n_problems: 50\n    pass_fail:\n      ci_overlap: false\n      sign_reversal: false\n      overall: FAIL\n    median_difference: -0.0155\n- id: c4_c4_entropy\n  claim: C4\n  description: 'DS importance entropy_delta: -0.04 to -0.05 (collapse); random: +0.13\n    to +0.23 (redistribution). Gini_delta: -0.03 to -0.08'\n  registry_id: c4_entropy\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics:\n    importance_entropy_delta:\n      s015: -0.0402\n      s020: -0.0472\n      s025: -0.0446\n      s030: -0.0436\n    random_entropy_delta:\n      s015: 0.1283\n      s020: 0.136\n      s025: 0.2171\n      s030: 0.2327\n    importance_gini_delta:\n      s015: -0.0301\n      s020: -0.0404\n      s025: -0.0647\n      s030: -0.0806\n    random_gini_delta:\n      s015: -0.0309\n      s020: -0.0403\n      s025: -0.062\n      s030: -0.0732\n    importance_cv_delta:\n      s015: -0.564\n      s020: -0.774\n      s025: -1.287\n      s030: -1.665\n    random_cv_delta:\n      s015: -1.021\n      s020: -1.203\n      s025: -1.923\n      s030: -2.137\n    problems_completed: 30\n    runtime_minutes: 69.1\n- id: c4_qwen_c4_entropy\n  claim: C4\n  description: 'QW importance entropy_delta mixed: s015=-0.073, s025=+0.045; Gini\n    weaker (-0.01 to -0.02). Model-dependent pattern'\n  registry_id: qwen_c4_entropy\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: negative\n  metrics:\n    problems_completed: 30\n    qwen_importance_entropy_delta:\n      s015: -0.0733\n      s020: -0.0759\n      s025: 0.0451\n      s030: -0.0072\n    qwen_random_entropy_delta:\n      s015: 0.0838\n      s020: 0.0901\n      s025: 0.2168\n      s030: 0.1968\n    qwen_importance_gini_delta:\n      s015: -0.0103\n      s020: -0.0121\n      s025: -0.01\n      s030: -0.0202\n    qwen_random_gini_delta:\n      s015: -0.0186\n      s020: -0.0229\n      s025: -0.0337\n      s030: -0.0448\n    qwen_importance_cv_delta:\n      s015: -0.045\n      s020: -0.208\n      s025: -1.491\n      s030: -1.142\n    qwen_random_cv_delta:\n      s015: -0.778\n      s020: -0.889\n      s025: -1.5\n      s030: -1.677\n    cross_model_notes: random entropy increase consistent; importance entropy collapse\n      inconsistent at s025 (reversed to +0.045) and near-zero at s030; gini/cv directions\n      consistent but Qwen magnitudes smaller\n- id: c5_bf16_qw_imp_s030\n  claim: C5\n  description: 'Qwen: median_diff=2.619, Cohen''s d=1.439, p<1e-5; replicates DeepSeek\n    pattern'\n  registry_id: bf16_qw_imp_s030\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics:\n    median_difference: 2.619385\n    permutation_p: 0\n    cohens_d: 1.4394\n    bootstrap_ci_95:\n    - 1.722281\n    - 3.651063\n    wilcoxon_p: 0\n    n_bootstrap: 10000\n    n_paired: 46\n- id: c5_bf16_importance_s030\n  claim: C5\n  description: 'DeepSeek: II low_median=14.64, high_median=0.053; strong phase gradient'\n  registry_id: bf16_importance_s030\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics: *id001\n- id: c5_c2_n500_deepseek\n  claim: C5\n  description: 'DS n=500: imp_s030 median_II=8.48, CI=[7.46,9.56], p=1.3e-78; robust\n    at scale'\n  registry_id: c2_n500_deepseek\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics: &id004\n    n_problems: 500\n    effective_n: 496\n    mid_null_rate: 0.102\n    imp_s015_median_ii: 0.3907\n    imp_s015_ci:\n    - 0.3496\n    - 0.4431\n    imp_s015_wilcoxon_p: 1.27e-70\n    imp_s020_median_ii: 1.2149\n    imp_s020_ci:\n    - 1.1072\n    - 1.3365\n    imp_s020_wilcoxon_p: 3.98e-75\n    imp_s025_median_ii: 3.9857\n    imp_s025_ci:\n    - 3.5272\n    - 4.3588\n    imp_s025_wilcoxon_p: 1.99e-78\n    imp_s030_median_ii: 8.4813\n    imp_s030_ci:\n    - 7.7543\n    - 9.6919\n    imp_s030_wilcoxon_p: 1.09e-79\n    rand_s015_median_ii: 0.0139\n    rand_s015_wilcoxon_p: 0.863\n    rand_s020_median_ii: 0.0315\n    rand_s020_wilcoxon_p: 0.28\n    rand_s025_median_ii: 0.2574\n    rand_s025_bonf_p: 0.005839\n    rand_s025_fdr_p: 0.001914\n    rand_s030_median_ii: 0.5096\n    rand_s030_bonf_p: 0.005903\n    rand_s030_fdr_p: 0.001914\n    dz_s015_s020: -0.925\n    dz_s020_s025: -0.824\n    dz_s025_s030: -0.773\n    dz_s015_s030: -0.944\n    all_dz_reliable: true\n    dose_response_monotonic: true\n    dose_response_spearman_rho: 1\n    dose_response_perm_p: 0.0417\n    imp_rand_ratio_range: 15.5-38.6x\n    bonferroni_k: 4\n    bonferroni_note: Bonferroni k=4 family-wise (D066 revision)\n- id: c5_c2_qw_n500_r3\n  claim: C5\n  description: 'QW n=500: imp_s030 median_II=4.33, p<1e-40; cross-model replication\n    at high power'\n  registry_id: c2_qw_n500_r3\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics: &id005\n    n_problems: 500\n    effective_n: 475\n    filter: low+high valid only (mid-null allowed)\n    mid_null_rate: 0.452\n    imp_s015_median_ii: 0.0659\n    imp_s015_ci:\n    - 0.0492\n    - 0.0925\n    imp_s015_wilcoxon_p: 8.66e-15\n    imp_s015_bonf_p: 3.46e-14\n    imp_s020_median_ii: 0.3073\n    imp_s020_ci:\n    - 0.2612\n    - 0.3564\n    imp_s020_wilcoxon_p: 6.84e-42\n    imp_s020_bonf_p: 2.74e-41\n    imp_s025_median_ii: 1.0745\n    imp_s025_ci:\n    - 0.9766\n    - 1.1787\n    imp_s025_wilcoxon_p: 1.06e-68\n    imp_s025_bonf_p: 4.25e-68\n    imp_s030_median_ii: 3.155\n    imp_s030_ci:\n    - 2.7834\n    - 3.5582\n    imp_s030_wilcoxon_p: 9.21e-74\n    imp_s030_bonf_p: 3.69e-73\n    rand_s015_median_ii: -0.0111\n    rand_s015_wilcoxon_p: 0.172\n    rand_s015_bonf_p: 0.687\n    rand_s020_median_ii: 0.0153\n    rand_s020_wilcoxon_p: 0.2\n    rand_s020_bonf_p: 0.8\n    rand_s025_median_ii: 0.3931\n    rand_s025_wilcoxon_p: 1.59e-11\n    rand_s025_bonf_p: 6.37e-11\n    rand_s025_fdr_p: 2.63e-11\n    rand_s030_median_ii: 0.9127\n    rand_s030_wilcoxon_p: 2.92e-15\n    rand_s030_bonf_p: 1.17e-14\n    rand_s030_fdr_p: 5.61e-15\n    dz_s015_s020: -0.629\n    dz_s020_s025: -0.865\n    dz_s025_s030: -0.767\n    dz_s015_s030: -0.923\n    all_dz_reliable: true\n    dose_response_monotonic: true\n    dose_response_spearman_rho: 1\n    dose_response_perm_p: 0.0417\n    imp_rand_ratio_range: 2.7-20.1x\n    bonferroni_k: 4\n    bonferroni_note: Bonferroni k=4 family-wise (D066 revision)\n- id: c5b_c5b_pilot\n  claim: C5b\n  description: 'Oracle recovery=18% (gate: >30% FAIL); heuristic recovery=31.7% but\n    CI crosses zero. s030 incomplete'\n  registry_id: c5b_pilot\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: negative\n  metrics:\n    s025_uniform_median_ii: 1.0435\n    s025_oracle_median_ii: 0.856\n    s025_oracle_recovery_pct: 18\n    s025_oracle_recovery_ci:\n    - -39\n    - 45.8\n    s025_oracle_wilcoxon_p: 0.0021\n    s025_heuristic_median_ii: 0.7127\n    s025_heuristic_recovery_pct: 31.7\n    s025_heuristic_recovery_ci:\n    - -22.8\n    - 66\n    s025_heuristic_wilcoxon_p: 0.0236\n    gate_criterion: oracle_recovery > 30%\n    gate_result: FAIL\n    s030_status: not_completed\n    n_problems: 30\n- id: c6_bf16_importance_s015\n  claim: C6\n  description: II low_median=0.398 at s=0.15\n  registry_id: bf16_importance_s015\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: -0.150213\n        median: 0.005752\n        ci:\n        - -0.294614\n        - -0.055385\n        winsorized_mean: -0.062378\n        skewness: -14.9912\n      mid:\n        mean: 0.447301\n        median: 0.080738\n        ci:\n        - 0.267993\n        - 0.668749\n        winsorized_mean: 0.324751\n        skewness: 4.7221\n      low:\n        mean: 2.405837\n        median: 0.398291\n        ci:\n        - 1.478784\n        - 3.667675\n        winsorized_mean: 1.278857\n        skewness: 9.5402\n    per_problem_ii_stats:\n      high:\n        n: 49\n        min: -0.188061\n        max: 0.335853\n        mean: -0.013405\n        median: 0.00012\n        std: 0.078483\n      mid:\n        n: 40\n        min: -0.169092\n        max: 3.88198\n        mean: 0.308621\n        median: 0.107114\n        std: 0.690186\n      low:\n        n: 50\n        min: -0.872983\n        max: 9.10289\n        mean: 0.725504\n        median: 0.315517\n        std: 1.731056\n    gradient_paired_aggregate_legacy: 69.24\n    median_difference: 0.3925\n    n_problems: 50\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: true\n      overall: PASS\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    perplexity:\n      high:\n        dense: 1.1689\n        attn: 1.4861\n        kv: 1.4481\n        both: 1.5911\n      mid:\n        dense: 1.2269\n        attn: 1.5137\n        kv: 2.5971\n        both: 3.4541\n      low:\n        dense: 1.2286\n        attn: 1.6147\n        kv: 8.9201\n        both: 12.5084\n- id: c6_bf16_importance_s020\n  claim: C6\n  description: II low_median=1.496 at s=0.20\n  registry_id: bf16_importance_s020\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics: *id002\n- id: c6_bf16_importance_s025\n  claim: C6\n  description: II low_median=7.196 at s=0.25\n  registry_id: bf16_importance_s025\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics: *id003\n- id: c6_bf16_importance_s030\n  claim: C6\n  description: II low_median=14.64 at s=0.30; growth 0.40->1.50->7.20->14.64 is sub-exponential\n  registry_id: bf16_importance_s030\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics: *id001\n- id: c7_c2_n500_deepseek\n  claim: C7\n  description: 'DS n=500: all 4 sparsities significant (p<1e-70); CIs non-overlapping\n    across dose levels'\n  registry_id: c2_n500_deepseek\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics: *id004\n- id: c7_c2_qw_n500_r3\n  claim: C7\n  description: 'QW n=500: all 4 sparsities significant (p<1e-14 Bonferroni-corrected);\n    mid_null_rate=45.2%'\n  registry_id: c2_qw_n500_r3\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics: *id005\n- id: c8_c3_llama\n  claim: C8\n  description: LLaMA-8B (LlamaForCausalLM) replicates phase-modulated compound severity\n    from Qwen2ForCausalLM\n  registry_id: c3_llama\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics:\n    model: DeepSeek-R1-Distill-Llama-8B\n    n_problems: 50\n    n_valid: 49\n    n_skipped: 1\n    conditions_completed: 8/8\n    n_bootstrap: 10000\n    bonferroni_k: 4\n    imp_vs_rand_dz:\n      s015: 0.1923\n      s020: 0.255\n      s025: 0.2902\n      s030: 0.3352\n    imp_vs_rand_dz_ci:\n      s015:\n      - -0.0862\n      - 0.496\n      s020:\n      - -0.0248\n      - 0.5381\n      s025:\n      - 0.0081\n      - 0.6121\n      s030:\n      - 0.0606\n      - 0.6629\n    imp_vs_rand_dz_interpretation:\n      s015: negligible\n      s020: small\n      s025: small\n      s030: small\n    imp_vs_rand_dz_monotonic: true\n    phase_gradient_importance_dz:\n      s015: 1.0079\n      s020: 1.108\n      s025: 1.1227\n      s030: 1.0038\n    phase_gradient_importance_dz_ci:\n      s015:\n      - 0.593\n      - 1.7025\n      s020:\n      - 0.8144\n      - 1.5698\n      s025:\n      - 0.8735\n      - 1.5768\n      s030:\n      - 0.8099\n      - 1.3519\n    phase_gradient_importance_interpretation: all_large\n    phase_gradient_random_dz:\n      s015: 0.3497\n      s020: 0.373\n      s025: 0.4476\n      s030: 0.4385\n    phase_gradient_random_dz_ci:\n      s015:\n      - 0.0665\n      - 0.6916\n      s020:\n      - 0.0868\n      - 0.7335\n      s025:\n      - 0.1669\n      - 0.7698\n      s030:\n      - 0.1966\n      - 0.707\n    phase_gradient_random_interpretation: all_small\n    median_diff:\n      s015: 0.0203\n      s020: 0.0221\n      s025: 0.0947\n      s030: 0.3562\n    median_diff_ci:\n      s015:\n      - 0.0016\n      - 0.0435\n      s020:\n      - -0.0905\n      - 0.187\n      s025:\n      - -0.0037\n      - 0.3029\n      s030:\n      - -0.0691\n      - 0.5442\n    wilcoxon_p:\n      s015: 0.0549\n      s020: 0.0632\n      s025: 0.0209\n      s030: 0.0074\n    wilcoxon_p_bonferroni:\n      s015: 0.2195\n      s020: 0.2527\n      s025: 0.0834\n      s030: 0.0294\n    significant_bonferroni:\n      s015: false\n      s020: false\n      s025: false\n      s030: true\n    cross_arch_comparison:\n      deepseek_importance_dz:\n        s015: 0.4416\n        s020: 0.5195\n        s025: 0.6831\n        s030: 0.8031\n      llama_importance_dz:\n        s015: 1.0079\n        s020: 1.108\n        s025: 1.1227\n        s030: 1.0038\n      delta:\n        s015: 0.5663\n        s020: 0.5885\n        s025: 0.4396\n        s030: 0.2007\n      note: LLaMA shows uniformly large d_z (all >1.0) vs DeepSeek medium-to-large\n- id: c10_gsm8k_profiling_ds\n  claim: C10\n  description: 'DS GSM8K importance gradient: s015=0.241, s020=0.740, s025=1.992,\n    s030=4.636 (monotonic)'\n  registry_id: gsm8k_profiling_ds\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics:\n    version: v3_median\n    n_problems: 50\n    method: median + Wilcoxon + bootstrap_median(B=10000)\n    importance:\n      s015:\n        median_gradient: 0.241\n        ci_low: 0.077\n        ci_high: 0.478\n        wilcoxon_p: 0.0003\n      s020:\n        median_gradient: 0.74\n        ci_low: 0.314\n        ci_high: 1.119\n        wilcoxon_p: 0.0001\n      s025:\n        median_gradient: 1.992\n        ci_low: 0.933\n        ci_high: 2.82\n        wilcoxon_p: 0.0001\n      s030:\n        median_gradient: 4.682\n        ci_low: 2.121\n        ci_high: 10.557\n        wilcoxon_p: 0.0001\n    imp_rand_ratio:\n      s015: 2.3\n      s020: 2.5\n      s025: 3.8\n      s030: 2.8\n    dose_response_monotonic: true\n- id: c10_gsm8k_profiling_qw\n  claim: C10\n  description: 'QW GSM8K importance gradient: s015=0.039, s020=0.158, s025=1.100,\n    s030=2.092 (monotonic)'\n  registry_id: gsm8k_profiling_qw\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics:\n    version: v3_median\n    n_problems: 50\n    method: median + Wilcoxon + bootstrap_median(B=10000)\n    importance:\n      s015:\n        median_gradient: 0.039\n      s020:\n        median_gradient: 0.158\n      s025:\n        median_gradient: 1.1\n      s030:\n        median_gradient: 2.092\n    qw_rand_s030: INVALID\n- id: c10_gsm8k_qw_rand_s025_v2\n  claim: C10\n  description: 'QW random s025 GSM8K: II median_high=0.72, low=1.48; phase gradient\n    weaker than importance'\n  registry_id: gsm8k_qw_rand_s025_v2\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics:\n    verdict: PASS\n    n_problems: 50\n    n_bootstrap: 1000\n    seed: 42\n    high_sparsity:\n      n_segments: 216\n      n_tokens: 9326\n      ppl_dense: 1.0695\n      ppl_attn: 5.9362\n      ppl_kv: 3.4316\n      ppl_both: 15.7484\n      ii_mean: 6.5954\n      ii_ci:\n      - 1.1114\n      - 11.3791\n      ii_median: 0.7176\n      ii_median_ci:\n      - 0.5959\n      - 0.9347\n      winsorized_mean: 6.5046\n      skewness: -4.6807\n      outlier_count: 3\n    low_sparsity:\n      n_segments: 252\n      n_tokens: 29224\n      ppl_dense: 1.1972\n      ppl_attn: 11.5347\n      ppl_kv: 5.6038\n      ppl_both: 21.6874\n      ii_mean: 2.3883\n      ii_ci:\n      - -8.4602\n      - 11.029\n      ii_median: 1.4587\n      ii_median_ci:\n      - 1.1121\n      - 2.0451\n      winsorized_mean: 5.8911\n      skewness: -7.6074\n      outlier_count: 4\n    mid_sparsity:\n      n_segments: 51\n      n_tokens: 5954\n      ppl_dense: 1.2601\n      ppl_attn: 13.4132\n      ppl_kv: 6.4841\n      ppl_both: 20.8714\n      ii_mean: 4.5407\n      ii_ci:\n      - -4.8854\n      - 12.4605\n      ii_median: 1.1272\n      ii_median_ci:\n      - 0.637\n      - 3.3729\n      winsorized_mean: 6.3284\n      skewness: -3.4048\n      outlier_count: 1\n- id: c10_gsm8k_qw_rand_s030_v2\n  claim: C10\n  description: 'QW random s030 GSM8K: II median_high=2.31, low=5.87; compound effect\n    on GSM8K confirmed'\n  registry_id: gsm8k_qw_rand_s030_v2\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics:\n    verdict: PASS\n    n_problems: 50\n    n_bootstrap: 1000\n    seed: 42\n    high_sparsity:\n      n_segments: 216\n      n_tokens: 9326\n      null_ratio: 2/50\n      ppl_dense: 1.0695\n      ppl_attn: 6.5613\n      ppl_kv: 4.481\n      ppl_both: 23.7486\n      ii_mean: 11.83\n      ii_median: 2.31\n      ii_ci:\n      - 6.17\n      - 17.04\n      ii_median_ci:\n      - 1.64\n      - 2.81\n      winsorized_mean: 10.55\n      skewness: -2.29\n      outlier_count: 7\n    low_sparsity:\n      n_segments: 252\n      n_tokens: 29224\n      null_ratio: 5/50\n      ppl_dense: 1.1972\n      ppl_attn: 6.3283\n      ppl_kv: 8.5374\n      ppl_both: 56.2304\n      ii_mean: 31.26\n      ii_median: 5.2\n      ii_ci:\n      - 17.84\n      - 47.86\n      ii_median_ci:\n      - 3.95\n      - 7.24\n      winsorized_mean: 16.35\n      skewness: 7.57\n      outlier_count: 4\n    mid_sparsity:\n      n_segments: 51\n      n_tokens: 5954\n      null_ratio: 17/50\n      ppl_dense: 1.2601\n      ppl_attn: 18.6162\n      ppl_kv: 11.6625\n      ppl_both: 47.9019\n      ii_mean: 18.02\n      ii_median: 2.7\n      ii_ci:\n      - 0.09\n      - 36.69\n      ii_median_ci:\n      - 1.46\n      - 8.77\n      winsorized_mean: 18.22\n      skewness: 0.43\n      outlier_count: 2\n- id: s3_c_bf16_ds_imp_s010\n  claim: S3->C\n  description: 'DS s=0.10: II_high_median=0.003, verdict=FAIL; below onset threshold\n    for DeepSeek'\n  registry_id: bf16_ds_imp_s010\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: negative\n  metrics:\n    verdict: FAIL\n    problems: 50\n    II_high_sparsity_median: 0.0027\n    II_high_sparsity_mean: -0.1998\n    II_low_sparsity_median: 0.0151\n    II_low_sparsity_mean: -0.1066\n    II_mid_sparsity_median: 0.0061\n    II_mid_sparsity_mean: -0.0131\n    high_sparsity_tokens: 21086\n    low_sparsity_tokens: 27748\n    mid_sparsity_tokens: 13306\n- id: s3_c_bf16_qw_imp_s010\n  claim: S3->C\n  description: 'QW s=0.10: overall_verdict=PASS, CI_overlap_test=PASS; Qwen onset\n    earlier than DeepSeek'\n  registry_id: bf16_qw_imp_s010\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics:\n    n_problems: 50\n    overall_verdict: PASS\n    ci_overlap_test: PASS\n    sign_reversal_test: FAIL\n    high_sparsity_II_median: 0.0001\n    high_sparsity_II_median_CI:\n    - -0.0028\n    - 0.0005\n    high_sparsity_II_mean: -0.0887\n    high_sparsity_II_mean_CI:\n    - -0.1235\n    - -0.0591\n    low_sparsity_II_median: -0.0444\n    low_sparsity_II_median_CI:\n    - -0.0967\n    - -0.0152\n    low_sparsity_II_mean: -0.2431\n    low_sparsity_II_mean_CI:\n    - -0.3817\n    - -0.1202\n    mid_sparsity_II_median: -0.0359\n    mid_sparsity_II_median_CI:\n    - -0.0963\n    - -0.015\n    mid_sparsity_II_mean: -0.084\n    mid_sparsity_II_mean_CI:\n    - -0.1366\n    - -0.035\n    ppl_high_dense: 1.074\n    ppl_high_both: 1.228\n    ppl_low_dense: 1.152\n    ppl_low_both: 3.204\n    ppl_mid_dense: 1.133\n    ppl_mid_both: 1.741\n- id: s3_c_bf16_qw_imp_s015\n  claim: S3->C\n  description: 'QW s=0.15: median_diff=0.048, permutation_p=0.0001; confirmed above\n    threshold'\n  registry_id: bf16_qw_imp_s015\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics:\n    median_difference: 0.047619\n    permutation_p: 0.0001\n    cohens_d: 0.3705\n    bootstrap_ci_95:\n    - -0.005077\n    - 0.109517\n    wilcoxon_p: 0.02958\n    n_bootstrap: 10000\n    n_paired: 46\n- id: s7_c_c2_n500_deepseek\n  claim: S7->C\n  description: 'DS n=500 monotonic: imp median II 0.39->1.21->3.99->8.48 across s015-s030\n    (Spearman rho=1.0)'\n  registry_id: c2_n500_deepseek\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics: *id004\n- id: s7_c_c2_qw_n500_r3\n  claim: S7->C\n  description: 'QW n=500 monotonic: imp median II 0.066->0.307->1.075->4.33 across\n    s015-s030 (Spearman rho=1.0)'\n  registry_id: c2_qw_n500_r3\n  role: primary\n  priority: high\n  status: DONE\n  conclusion: success\n  metrics: *id005\n- id: s7_c_bf16_qw_imp_s035\n  claim: S7->C\n  description: 'QW s=0.35: low_II_median=8.24; extends dose-response beyond s030'\n  registry_id: bf16_qw_imp_s035\n  role: supporting\n  priority: medium\n  status: DONE\n  conclusion: success\n  metrics:\n    n_problems: 50\n    overall_verdict: PASS\n    ci_overlap_test: PASS\n    sign_reversal_test: FAIL\n    high_sparsity_II_median: 0.0232\n    high_sparsity_II_median_CI:\n    - 0.0154\n    - 0.0383\n    high_sparsity_II_mean: 0.1643\n    high_sparsity_II_mean_CI:\n    - 0.0844\n    - 0.2495\n    low_sparsity_II_median: 8.2358\n    low_sparsity_II_median_CI:\n    - 6.1564\n    - 10.9231\n    low_sparsity_II_mean: 18.9673\n    low_sparsity_II_mean_CI:\n    - 14.5015\n    - 23.9752\n    mid_sparsity_II_median: 0.9577\n    mid_sparsity_II_median_CI:\n    - 0.171\n    - 3.5575\n    mid_sparsity_II_mean: 8.0734\n    mid_sparsity_II_mean_CI:\n    - 2.0224\n    - 16.8946\n    ppl_high_dense: 1.0738\n    ppl_high_both: 2.3435\n    ppl_low_dense: 1.1518\n    ppl_low_both: 58.0358\n    ppl_mid_dense: 1.1327\n    ppl_mid_both: 20.9912\n    high_sparsity_tokens: 16289\n    low_sparsity_tokens: 32227\n    mid_sparsity_tokens: 4372\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_interaction_index_profiling\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_ii_profiling_v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    mvp_verdict: PASS_technical_but_negative_hypothesis\n    ci_nonoverlap: true\n    sign_reversal: false\n    ii_reasoning_0.3: 17.79\n    ii_reasoning_0.3_ci:\n    - 4.09\n    - 38.76\n    ii_transition_0.3: 3.06\n    ii_transition_0.3_ci:\n    - 0.01\n    - 5.6\n    ii_reasoning_0.5: 468.9\n    ii_transition_0.5: 850.07\n    ii_execution_0.3: Inf\n    phase_distribution:\n      execution: 1.2%_25seg\n      reasoning: 8.1%_96seg\n      transition: 90.7%_192seg\n    total_tokens: 86207\n    all_ii_superadditive: true\n    amplitude_ratio_reas_vs_trans_0.3: 5.81\n    gmm_best_k: 5\n    gmm_means:\n    - 0.438\n    - 0.597\n    - 0.719\n    - 0.816\n    - 0.892\n    gmm_weights:\n    - 0.062\n    - 0.14\n    - 0.208\n    - 0.282\n    - 0.309\n    sparsity_global:\n      mean: 0.7653\n      std: 0.1364\n      median: 0.8004\n    quantile_boundaries:\n    - 0.7337\n    - 0.8482\n- exp_id: mvp_ii_profiling_v3\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    mvp_verdict: FAIL\n    ci_nonoverlap: false\n    sign_reversal: false\n    phase_distribution_balanced: true\n    ii_high_0.1:\n      mean: 0.2317\n      ci:\n      - 0.1338\n      - 0.3418\n    ii_low_0.1:\n      mean: 0.1711\n      ci:\n      - 0.0782\n      - 0.2768\n    ii_mid_0.1:\n      mean: 0.1607\n      ci:\n      - 0.0886\n      - 0.2489\n    ii_high_0.2:\n      mean: 2.1574\n      ci:\n      - 1.0605\n      - 3.5491\n    ii_low_0.2:\n      mean: 1.1294\n      ci:\n      - 0.4368\n      - 1.9593\n    ii_mid_0.2:\n      mean: 0.3049\n      ci:\n      - -1.0635\n      - 1.3044\n    total_tokens: 86207\n    no_nan_inf: true\n    segments:\n      high: 511\n      low: 454\n      mid: 391\n- exp_id: mvp_ii_profiling_v4\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_ii_profiling_v4b\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_ii_profiling_v4c\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_ii_profiling_v4d\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_ii_profiling_v4-random\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_v4a_r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_v4b_r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_v4c_r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_v4_random_r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp_v4_legacy_s01\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    II_high_0.1:\n      mean: -0.1097\n      ci_low: -0.8066\n      ci_high: 0.41\n    II_mid_0.1:\n      mean: -15.966\n      ci_low: -47.991\n      ci_high: 1.288\n    II_low_0.1:\n      mean: 0\n      ci_low: 0\n      ci_high: 0\n    ppl_high_dense: 1.1462\n    ppl_high_both: 22.1302\n    ppl_mid_dense: 1.1226\n    ppl_mid_both: 47.5856\n    verdict: FAIL\n- exp_id: mvp_v4_legacy_s02\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_0.2:\n      mean: 21.2856\n      ci:\n      - 0.0292\n      - 63.163\n    ii_mid_0.2:\n      mean: 21.8743\n      ci:\n      - 4.9863\n      - 41.785\n    ii_low_0.2:\n      mean: 0\n      ci:\n      - 0\n      - 0\n    ppl_high:\n      dense: 1.15\n      attn: 1.32\n      kv: 104.42\n      both: 63.41\n    ppl_mid:\n      dense: 1.12\n      attn: 1.29\n      kv: 324.16\n      both: 170.47\n    ppl_low:\n      dense: 1.11\n      attn: 1.3\n      kv: 1.11\n      both: 1.3\n    problems_completed: 50\n    phase_tokens:\n      high: 25862\n      mid: 27996\n      low: 32349\n    mvp_verdict: PASS\n- exp_id: mvp_v4_legacy_s03\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_0.3:\n      mean: -224.5\n      ci_crosses_zero: true\n    verdict: FAIL_ci_crosses_zero\n- exp_id: mvp_v4_legacy_s025\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_v4_legacy_s035\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_v4_float32_s030\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_v5_fixed_s020\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    ii_high: 0.5\n    ii_mid: 3.52\n    ii_low: 31.89\n    ii_high_ci:\n    - 0.41\n    - 0.62\n    ii_mid_ci:\n    - 2.29\n    - 5.35\n    ii_low_ci:\n    - 18.74\n    - 47.22\n    ii_high_median: 0.33\n    ii_mid_median: 1.55\n    ii_low_median: 9.56\n    kv_ppl_high: 1.24\n    kv_ppl_mid: 3.65\n    kv_ppl_low: 14.11\n    both_ppl_high: 2.7\n    both_ppl_mid: 8.13\n    both_ppl_low: 42.64\n    problems: 50\n    ⚠️_WARNING: pre-fix code, INVALIDATED. Results found on disk after kill but code\n      lacked conda activation fix. Do NOT cite these numbers.\n- exp_id: mvp_v5_fixed_s030\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    ii_high: 1.18\n    ii_mid: 168.53\n    ii_low: 1926.23\n    ii_high_ci:\n    - 0.86\n    - 1.6\n    ii_mid_ci:\n    - 36.91\n    - 348.21\n    ii_low_ci:\n    - 179.17\n    - 4062.57\n    ii_high_median: 0.6\n    ii_mid_median: 7.47\n    ii_low_median: 44.63\n    kv_ppl_high: 1.4\n    kv_ppl_mid: 15.11\n    kv_ppl_low: 40.79\n    both_ppl_high: 5.71\n    both_ppl_mid: 137.61\n    both_ppl_low: 963.2\n    problems: 50\n    ⚠️_WARNING: pre-fix code, INVALIDATED. Results found on disk after kill but code\n      lacked conda activation fix. Do NOT cite these numbers.\n- exp_id: mvp_v5_fixed_s015\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ii_high: 0.306\n    ii_mid: 1.274\n    ii_low: 8.786\n    ii_high_ci:\n    - 0.256\n    - 0.359\n    ii_mid_ci:\n    - 0.895\n    - 1.749\n    ii_low_ci:\n    - 5.294\n    - 12.684\n    ii_high_median: 0.205\n    ii_mid_median: 0.696\n    ii_low_median: 2.627\n    ii_high_winsorized: 0.289\n    ii_mid_winsorized: 1.139\n    ii_low_winsorized: 8.408\n    kv_ppl_high: 1.2147\n    kv_ppl_mid: 2.1276\n    kv_ppl_low: 6.7451\n    both_ppl_high: 2.2835\n    both_ppl_mid: 3.9408\n    both_ppl_low: 16.9987\n    problems: 50\n    segments: 1356\n- exp_id: mvp_v5_fixed_s025\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ii_high: 0.851\n    ii_mid: 9.306\n    ii_low: 96.715\n    ii_high_ci:\n    - 0.703\n    - 0.999\n    ii_mid_ci:\n    - 6.092\n    - 13.303\n    ii_low_ci:\n    - 59.642\n    - 143.188\n    ii_high_median: 0.584\n    ii_mid_median: 4.522\n    ii_low_median: 30.903\n    ii_high_winsorized: 0.802\n    ii_mid_winsorized: 8.156\n    ii_low_winsorized: 94.931\n    kv_ppl_high: 1.3108\n    kv_ppl_mid: 6.1778\n    kv_ppl_low: 23.8919\n    both_ppl_high: 3.4623\n    both_ppl_mid: 16.4148\n    both_ppl_low: 104.1749\n    problems: 50\n    segments: 1356\n- exp_id: mvp_v5_fixed_s020_r2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ii_high_median: 0.3333\n    ii_mid_median: 1.5479\n    ii_low_median: 9.5627\n    ii_high_mean: 0.5044\n    ii_mid_mean: 3.5155\n    ii_low_mean: 31.8937\n    ii_high_ci:\n    - 0.41\n    - 0.62\n    ii_mid_ci:\n    - 2.29\n    - 5.35\n    ii_low_ci:\n    - 18.74\n    - 47.22\n    kv_ppl_high: 1.24\n    kv_ppl_mid: 3.65\n    kv_ppl_low: 14.11\n    both_ppl_high: 2.7\n    both_ppl_mid: 8.13\n    both_ppl_low: 42.64\n    problems: 50\n- exp_id: mvp_v5_fixed_s030_r2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ii_high_median: 0.5964\n    ii_mid_median: 7.4671\n    ii_low_median: 44.6324\n    ii_high_mean: 1.1832\n    ii_mid_mean: 168.53\n    ii_low_mean: 1926.23\n    ii_high_ci:\n    - 0.86\n    - 1.6\n    ii_mid_ci:\n    - 36.91\n    - 348.21\n    ii_low_ci:\n    - 179.17\n    - 4062.57\n    kv_ppl_high: 1.4\n    kv_ppl_mid: 15.11\n    kv_ppl_low: 40.79\n    both_ppl_high: 5.71\n    both_ppl_mid: 137.61\n    both_ppl_low: 963.2\n    problems: 50\n- exp_id: mvp_v5_random_s015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 0.1606\n    ii_mid_median: 0.252\n    ii_low_median: 0.1831\n    ii_high_mean: 0.4563\n    ii_mid_mean: 0.5134\n    ii_low_mean: 0.4775\n    ii_high_ci:\n    - 0.12\n    - 0.77\n    ii_mid_ci:\n    - 0.34\n    - 0.74\n    ii_low_ci:\n    - 0.28\n    - 0.7\n    kv_ppl_high: 3.14\n    kv_ppl_mid: 2.91\n    kv_ppl_low: 3.61\n    both_ppl_high: 3.92\n    both_ppl_mid: 4.14\n    both_ppl_low: 4.71\n    problems: 50\n- exp_id: mvp_v5_random_s025\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 3.0024\n    ii_mid_median: 2.9846\n    ii_low_median: 2.9146\n    ii_high_mean: 3.9052\n    ii_mid_mean: 7.9491\n    ii_low_mean: 3.9114\n    ii_high_ci:\n    - 0.98\n    - 6.34\n    ii_mid_ci:\n    - 4.67\n    - 11.87\n    ii_low_ci:\n    - 2.71\n    - 5.24\n    kv_ppl_high: 6.39\n    kv_ppl_mid: 6.11\n    kv_ppl_low: 9.07\n    both_ppl_high: 17.06\n    both_ppl_mid: 15.38\n    both_ppl_low: 29.32\n    problems: 50\n- exp_id: mvp_v5_random_s020\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 0.321331\n    ii_mid_median: 0.455663\n    ii_low_median: 0.591916\n    ii_high_mean: 0.855584\n    ii_mid_mean: 1.258123\n    ii_low_mean: 0.956933\n    ii_high_ci:\n    - -0.124133\n    - 1.616883\n    ii_mid_ci:\n    - 0.674852\n    - 2.075565\n    ii_low_ci:\n    - 0.583856\n    - 1.413355\n    kv_ppl_high: 4.2537\n    kv_ppl_mid: 4.3064\n    kv_ppl_low: 5.4048\n    both_ppl_high: 7.9749\n    both_ppl_mid: 6.8553\n    both_ppl_low: 22.5868\n    problems: 50\n- exp_id: mvp_v5_random_s030\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 5.377512\n    ii_mid_median: 5.886454\n    ii_low_median: 3.776818\n    ii_high_mean: 22.734534\n    ii_mid_mean: 10.943319\n    ii_low_mean: 11.840449\n    ii_high_ci:\n    - 10.352118\n    - 42.551951\n    ii_mid_ci:\n    - 7.398611\n    - 14.765315\n    ii_low_ci:\n    - 4.097309\n    - 23.545273\n    kv_ppl_high: 8.1027\n    kv_ppl_mid: 8.5701\n    kv_ppl_low: 13.4922\n    both_ppl_high: 41.3452\n    both_ppl_mid: 24.1992\n    both_ppl_low: 68.5301\n    problems: 50\n- exp_id: v6_importance_s025\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 0.6641\n    ii_mid_median: 5.3067\n    ii_low_median: 24.1619\n    ii_high_mean: 0.8842\n    ii_mid_mean: 10.057\n    ii_low_mean: 71.8854\n    per_problem_ii_count: 50\n    n_high: 42\n    n_mid: 23\n    n_low: 21\n    problems: 50\n    bootstrap_gradient_paired: 35.72\n    bootstrap_ci_paired:\n    - 9.52\n    - 101.54\n    bootstrap_gradient_unpaired: 36.38\n    bootstrap_ci_unpaired:\n    - 13.19\n    - 97.61\n    bootstrap_p: 0\n- exp_id: v6_importance_s030\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 0.8833\n    ii_mid_median: 7.2706\n    ii_low_median: 34.6937\n    ii_high_mean: 1.5151\n    ii_mid_mean: 78.8215\n    ii_low_mean: 1163.9677\n    per_problem_ii_count: 50\n    n_high: 40\n    n_mid: 22\n    n_low: 20\n    problems: 50\n    bootstrap_gradient_paired: 41.92\n    bootstrap_ci_paired:\n    - 19.14\n    - 299.76\n    bootstrap_gradient_unpaired: 39.28\n    bootstrap_ci_unpaired:\n    - 21.87\n    - 129.59\n    bootstrap_p: 0\n- exp_id: v6_importance_s015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 0.2266\n    ii_mid_median: 0.7432\n    ii_low_median: 2.8762\n    ii_high_mean: 0.2874\n    ii_mid_mean: 1.6858\n    ii_low_mean: 8.5161\n    per_problem_ii_count: 50\n    n_high: 43\n    n_mid: 32\n    n_low: 24\n    problems: 50\n    bootstrap_gradient_paired: 11.53\n    bootstrap_ci_paired:\n    - 3.49\n    - 23.78\n    bootstrap_gradient_unpaired: 12.69\n    bootstrap_ci_unpaired:\n    - 4.96\n    - 28.45\n    bootstrap_p: 0\n- exp_id: v6_importance_s020\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 0.3353\n    ii_mid_median: 1.6733\n    ii_low_median: 9.2538\n    ii_high_mean: 0.4936\n    ii_mid_mean: 4.9538\n    ii_low_mean: 25.8764\n    per_problem_ii_count: 50\n    n_high: 42\n    n_mid: 28\n    n_low: 21\n    problems: 50\n    bootstrap_gradient_paired: 11.05\n    bootstrap_ci_paired:\n    - 5.42\n    - 69.27\n    bootstrap_gradient_unpaired: 27.6\n    bootstrap_ci_unpaired:\n    - 6.55\n    - 75.16\n    bootstrap_p: 0\n- exp_id: qwen_importance_s015\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: qwen_importance_s020\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: qwen_importance_s025\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: qwen_importance_s030\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: v6_random_s015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 0.1606\n    ii_mid_median: 0.252\n    ii_low_median: 0.1831\n    ii_high_mean: 0.4563\n    ii_mid_mean: 0.5134\n    ii_low_mean: 0.4775\n    per_problem_ii_count: 50\n    n_high: 43\n    n_mid: 32\n    n_low: 28\n    bootstrap_gradient_paired: -0.2722\n    bootstrap_ci_paired:\n    - -0.7039\n    - 0.1548\n    bootstrap_p: 0.903\n    bootstrap_gradient_unpaired: -0.0592\n    bootstrap_ci_unpaired:\n    - -0.5341\n    - 0.3877\n    per_problem_ii_stats:\n      high:\n        min: -3.0621\n        max: 5.018\n        mean: 0.5386\n        median: 0.2003\n        std: 1.2085\n      mid:\n        min: -2.7245\n        max: 4.6713\n        mean: 0.3977\n        median: 0.299\n        std: 1.1456\n      low:\n        min: -0.4031\n        max: 3.7005\n        mean: 0.4806\n        median: 0.2465\n        std: 0.779\n    verdict: FAIL\n- exp_id: v6_random_s020\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_mean: 0.855584\n    ii_high_median: 0.321331\n    ii_high_ci:\n    - -0.124133\n    - 1.616883\n    ii_high_winsorized_mean: 0.913496\n    ii_mid_mean: 1.258123\n    ii_mid_median: 0.455663\n    ii_mid_ci:\n    - 0.674852\n    - 2.075565\n    ii_mid_winsorized_mean: 1.074102\n    ii_low_mean: 0.956933\n    ii_low_median: 0.591916\n    ii_low_ci:\n    - 0.583856\n    - 1.413355\n    ii_low_winsorized_mean: 0.96113\n    n_high: 511\n    n_mid: 391\n    n_low: 454\n    problems: 50\n    per_problem_ii_count: 50\n    gradient_mean_low_over_high: 1.118\n    gradient_median_low_over_high: 1.842\n    pass_fail: FAIL\n    perplexity_high_dense: 1.1462\n    perplexity_high_both: 7.9749\n    perplexity_mid_dense: 1.1226\n    perplexity_mid_both: 6.8553\n    perplexity_low_dense: 1.1105\n    perplexity_low_both: 22.5868\n- exp_id: v6_random_s025\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 3.0024\n    ii_mid_median: 2.9846\n    ii_low_median: 2.9146\n    ii_high_mean: 3.9052\n    ii_mid_mean: 7.9491\n    ii_low_mean: 3.9114\n    per_problem_ii_count: 50\n    n_high: 36\n    n_mid: 25\n    n_low: 24\n    bootstrap_gradient_paired: -0.1199\n    bootstrap_ci_paired:\n    - -1.517\n    - 1.2461\n    bootstrap_p: 0.559\n    bootstrap_gradient_unpaired: -0.8616\n    bootstrap_ci_unpaired:\n    - -3.3911\n    - 1.5169\n    per_problem_ii_stats:\n      high:\n        min: -6.1388\n        max: 25.2471\n        mean: 4.4098\n        median: 3.0421\n        std: 6.0734\n      mid:\n        min: 0.158\n        max: 108.7242\n        mean: 7.5626\n        median: 2.1407\n        std: 20.926\n      low:\n        min: -0.1953\n        max: 12.8555\n        mean: 3.5806\n        median: 2.7289\n        std: 3.4915\n    verdict: FAIL\n- exp_id: v6_random_s030\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: v6_random_s030_r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: bf16_importance_s015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: -0.150213\n        median: 0.005752\n        ci:\n        - -0.294614\n        - -0.055385\n        winsorized_mean: -0.062378\n        skewness: -14.9912\n      mid:\n        mean: 0.447301\n        median: 0.080738\n        ci:\n        - 0.267993\n        - 0.668749\n        winsorized_mean: 0.324751\n        skewness: 4.7221\n      low:\n        mean: 2.405837\n        median: 0.398291\n        ci:\n        - 1.478784\n        - 3.667675\n        winsorized_mean: 1.278857\n        skewness: 9.5402\n    per_problem_ii_stats:\n      high:\n        n: 49\n        min: -0.188061\n        max: 0.335853\n        mean: -0.013405\n        median: 0.00012\n        std: 0.078483\n      mid:\n        n: 40\n        min: -0.169092\n        max: 3.88198\n        mean: 0.308621\n        median: 0.107114\n        std: 0.690186\n      low:\n        n: 50\n        min: -0.872983\n        max: 9.10289\n        mean: 0.725504\n        median: 0.315517\n        std: 1.731056\n    gradient_paired_aggregate_legacy: 69.24\n    median_difference: 0.3925\n    n_problems: 50\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: true\n      overall: PASS\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    perplexity:\n      high:\n        dense: 1.1689\n        attn: 1.4861\n        kv: 1.4481\n        both: 1.5911\n      mid:\n        dense: 1.2269\n        attn: 1.5137\n        kv: 2.5971\n        both: 3.4541\n      low:\n        dense: 1.2286\n        attn: 1.6147\n        kv: 8.9201\n        both: 12.5084\n- exp_id: bf16_importance_s020\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 0.1289\n        median: 0.0145\n        ci:\n        - -0.1975\n        - 0.6647\n        winsorized_mean: -0.0297\n        skewness: 16.67\n      mid:\n        mean: 1.2604\n        median: 0.2027\n        ci:\n        - 0.7466\n        - 1.8962\n        winsorized_mean: 0.766\n        skewness: 7.05\n      low:\n        mean: 6.0288\n        median: 1.4963\n        ci:\n        - 4.4671\n        - 7.9237\n        winsorized_mean: 4.3426\n        skewness: 6.01\n    per_problem_ii_stats:\n      high:\n        n: 49\n        min: -0.1884\n        max: 0.4196\n        mean: 0.0025\n        median: 0.0036\n        std: 0.0966\n      mid:\n        n: 40\n        min: -0.0519\n        max: 8.6969\n        mean: 0.6795\n        median: 0.1977\n        std: 1.4998\n      low:\n        n: 50\n        min: -1.6151\n        max: 22.6875\n        mean: 2.2301\n        median: 1.128\n        std: 4.3758\n    gradient_paired_aggregate_legacy: 5.9\n    median_difference: 1.4818\n    n_problems: 50\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: false\n      overall: PASS\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    perplexity:\n      high:\n        dense: 1.1689\n        attn: 1.5233\n        kv: 1.6191\n        both: 2.1047\n      mid:\n        dense: 1.2269\n        attn: 1.5375\n        kv: 3.5164\n        both: 5.4246\n      low:\n        dense: 1.2286\n        attn: 1.6486\n        kv: 15.7987\n        both: 23.74\n- exp_id: bf16_importance_s025\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 0.302756\n        median: 0.032363\n        ci:\n        - 0.083714\n        - 0.543977\n        winsorized_mean: 0.200962\n        skewness: 4.8826\n      mid:\n        mean: 5.729665\n        median: 1.118069\n        ci:\n        - 3.455574\n        - 8.471799\n        winsorized_mean: 4.189902\n        skewness: 8.2799\n      low:\n        mean: 25.852951\n        median: 7.195958\n        ci:\n        - 19.077082\n        - 33.497293\n        winsorized_mean: 19.319103\n        skewness: 7.3986\n    per_problem_ii_stats:\n      high:\n        n: 49\n        min: -0.316321\n        max: 4.003714\n        mean: 0.133714\n        median: 0.009873\n        std: 0.595358\n      mid:\n        n: 40\n        min: -0.024794\n        max: 18.720486\n        mean: 2.537744\n        median: 1.05707\n        std: 3.962575\n      low:\n        n: 50\n        min: -1.854733\n        max: 75.467653\n        mean: 11.28281\n        median: 3.954593\n        std: 16.620011\n    gradient_paired_aggregate_legacy: 222.35\n    median_difference: 7.1636\n    n_problems: 50\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: false\n      overall: PASS\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    perplexity:\n      high:\n        dense: 1.1689\n        attn: 1.6511\n        kv: 1.8628\n        both: 2.7026\n      mid:\n        dense: 1.2269\n        attn: 1.7039\n        kv: 5.6205\n        both: 13.3436\n      low:\n        dense: 1.2286\n        attn: 1.8366\n        kv: 31.756\n        both: 63.668\n- exp_id: bf16_importance_s030\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 0.5547\n        median: 0.0534\n        ci:\n        - 0.2773\n        - 0.9198\n        winsorized_mean: 0.3367\n        skewness: 10.62\n      mid:\n        mean: 11.3\n        median: 2.2833\n        ci:\n        - 6.865\n        - 17.2633\n        winsorized_mean: 8.1752\n        skewness: 9.19\n      low:\n        mean: 57.7946\n        median: 14.6395\n        ci:\n        - 41.4416\n        - 77.0467\n        winsorized_mean: 39.3143\n        skewness: 8.31\n    per_problem_ii_stats:\n      high:\n        n: 49\n        min: -0.5095\n        max: 4.4457\n        mean: 0.1976\n        median: 0.0343\n        std: 0.6793\n      mid:\n        n: 40\n        min: -0.1989\n        max: 34.0258\n        mean: 5.2585\n        median: 1.5173\n        std: 7.9382\n      low:\n        n: 50\n        min: -7.3027\n        max: 126.7985\n        mean: 22.6601\n        median: 9.9731\n        std: 28.4096\n    gradient_paired_aggregate_legacy: 57.24\n    median_difference: 14.5861\n    n_problems: 50\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: false\n      overall: PASS\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    perplexity:\n      high:\n        dense: 1.1689\n        attn: 1.7123\n        kv: 2.0544\n        both: 3.2372\n      mid:\n        dense: 1.2269\n        attn: 1.7894\n        kv: 9.4821\n        both: 24.2847\n      low:\n        dense: 1.2286\n        attn: 1.9347\n        kv: 51.6485\n        both: 122.61\n- exp_id: bf16_random_s015\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: bf16_random_s020\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: bf16_random_s025\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: bf16_random_s030\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: bf16_qwen_importance_s015\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: bf16_qwen_importance_s020\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: bf16_qwen_importance_s025\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: bf16_qwen_importance_s030\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: v6_random_s030_r3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    II_high_mean: 9.2364\n    II_mid_mean: -230.7604\n    II_low_mean: -7.4119\n    II_high_median: 4.0237\n    II_mid_median: 2.4272\n    II_low_median: 4.735\n    ppl_low_both: 88.94\n    per_problem_count: 50\n- exp_id: bf16_ds_imp_s015\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    median_difference: 0.323579\n    permutation_p: 0\n    cohens_d: 0.6068\n    bootstrap_ci_95:\n    - 0.198824\n    - 0.471566\n    wilcoxon_p: 0\n    n_bootstrap: 10000\n    n_paired: 49\n- exp_id: bf16_ds_imp_s020\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    median_difference: 1.15202\n    permutation_p: 0\n    cohens_d: 0.725\n    bootstrap_ci_95:\n    - 0.655454\n    - 1.256001\n    wilcoxon_p: 0\n    n_bootstrap: 10000\n    n_paired: 49\n- exp_id: bf16_ds_imp_s025\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    median_difference: 3.968568\n    permutation_p: 0\n    cohens_d: 0.9534\n    bootstrap_ci_95:\n    - 2.829037\n    - 5.291756\n    wilcoxon_p: 0\n    n_bootstrap: 10000\n    n_paired: 49\n- exp_id: bf16_ds_imp_s030\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    median_difference: 9.943595\n    permutation_p: 0\n    cohens_d: 1.1263\n    bootstrap_ci_95:\n    - 8.391554\n    - 16.652865\n    wilcoxon_p: 0\n    n_bootstrap: 10000\n    n_paired: 49\n- exp_id: bf16_ds_rand_s015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 0.2208\n        median: 0.0931\n        ci:\n        - -1.0091\n        - 1.5243\n        median_ci:\n        - 0.0024\n        - 0.1515\n        winsorized_mean: 0.3161\n        skewness: -5.4\n      mid:\n        mean: -3.3604\n        median: 0.0967\n        ci:\n        - -8.4057\n        - 0.3697\n        median_ci:\n        - 0.0219\n        - 0.197\n        winsorized_mean: -0.6366\n        skewness: -10.56\n      low:\n        mean: -1.8952\n        median: 0.1026\n        ci:\n        - -4.9698\n        - 0.2741\n        median_ci:\n        - 0.044\n        - 0.1755\n        winsorized_mean: 0.0521\n        skewness: -11.57\n    perplexity:\n      high:\n        dense: 1.1687\n        attn: 3.5947\n        kv: 2.9239\n        both: 5.7569\n      mid:\n        dense: 1.2269\n        attn: 297.7957\n        kv: 2.915\n        both: 11.3156\n      low:\n        dense: 1.2284\n        attn: 11.3419\n        kv: 3.6161\n        both: 6.2886\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    n_problems: 50\n    pass_fail:\n      ci_overlap: false\n      sign_reversal: false\n      overall: FAIL\n    median_difference: 0.0095\n- exp_id: bf16_ds_rand_s020\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 1.1216\n        median: 0.2918\n        ci:\n        - 0.0796\n        - 2.5834\n        median_ci:\n        - 0.1598\n        - 0.4581\n        winsorized_mean: 1.7664\n        skewness: 9.59\n      mid:\n        mean: -1.5827\n        median: 0.3504\n        ci:\n        - -6.0963\n        - 1.5735\n        median_ci:\n        - 0.1993\n        - 0.5226\n        winsorized_mean: 0.5839\n        skewness: -12.31\n      low:\n        mean: -0.4116\n        median: 0.2763\n        ci:\n        - -2.6034\n        - 1.209\n        median_ci:\n        - 0.2194\n        - 0.5487\n        winsorized_mean: 0.9942\n        skewness: -10.07\n    perplexity:\n      high:\n        dense: 1.1687\n        attn: 3.1905\n        kv: 3.8002\n        both: 8.8129\n      mid:\n        dense: 1.2269\n        attn: 67.8504\n        kv: 3.788\n        both: 11.4974\n      low:\n        dense: 1.2284\n        attn: 8.592\n        kv: 5.0078\n        both: 9.2001\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    n_problems: 50\n    pass_fail:\n      ci_overlap: false\n      sign_reversal: false\n      overall: FAIL\n    median_difference: -0.0155\n- exp_id: bf16_ds_rand_s025\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 3.59\n        median: 0.8182\n        ci:\n        - 1.4021\n        - 6.2327\n        median_ci:\n        - 0.5075\n        - 1.7217\n        winsorized_mean: 6.3965\n        skewness: -7.57\n      mid:\n        mean: -1.8455\n        median: 0.9324\n        ci:\n        - -10.3663\n        - 4.9342\n        median_ci:\n        - 0.7331\n        - 1.7003\n        winsorized_mean: 3.1014\n        skewness: -12.76\n      low:\n        mean: 0.7212\n        median: 1.3627\n        ci:\n        - -4.2068\n        - 4.5006\n        median_ci:\n        - 1.0869\n        - 2.6866\n        winsorized_mean: 4.1866\n        skewness: -15.85\n    perplexity:\n      high:\n        dense: 1.1687\n        attn: 7.237\n        kv: 4.9751\n        both: 17.7423\n      mid:\n        dense: 1.2269\n        attn: 868.3199\n        kv: 5.1165\n        both: 29.4661\n      low:\n        dense: 1.2284\n        attn: 24.3571\n        kv: 6.7993\n        both: 17.9694\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    n_problems: 50\n    pass_fail:\n      ci_overlap: false\n      sign_reversal: false\n      overall: FAIL\n    median_difference: 0.5445\n- exp_id: bf16_ds_rand_s030\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 7.5555\n        median: 2.5031\n        ci:\n        - 4.4087\n        - 11.6199\n        median_ci:\n        - 1.3292\n        - 4.1205\n        winsorized_mean: null\n        skewness: null\n      mid:\n        mean: 6.2518\n        median: 2.5918\n        ci:\n        - 2.1767\n        - 10.4757\n        median_ci:\n        - 1.8397\n        - 3.7888\n        winsorized_mean: null\n        skewness: null\n      low:\n        mean: 6.8323\n        median: 4.0414\n        ci:\n        - 3.2428\n        - 10.6996\n        median_ci:\n        - 2.2686\n        - 6.3579\n        winsorized_mean: null\n        skewness: null\n    perplexity:\n      high:\n        dense: 1.1687\n        attn: 16.7892\n        kv: 8.8073\n        both: 40.7553\n      mid:\n        dense: 1.2269\n        attn: 2461.9219\n        kv: 8.6662\n        both: 62.4422\n      low:\n        dense: 1.2284\n        attn: 55.2916\n        kv: 11.5789\n        both: 37.6009\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    n_problems: 50\n    pass_fail:\n      ci_overlap: false\n      sign_reversal: false\n      overall: FAIL\n    median_difference: 1.5383\n- exp_id: bf16_qw_imp_s015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    median_difference: 0.047619\n    permutation_p: 0.0001\n    cohens_d: 0.3705\n    bootstrap_ci_95:\n    - -0.005077\n    - 0.109517\n    wilcoxon_p: 0.02958\n    n_bootstrap: 10000\n    n_paired: 46\n- exp_id: bf16_qw_imp_s020\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    median_difference: 0.207511\n    permutation_p: 0\n    cohens_d: 0.7224\n    bootstrap_ci_95:\n    - 0.067222\n    - 0.40226\n    wilcoxon_p: 3.4e-05\n    n_bootstrap: 10000\n    n_paired: 46\n- exp_id: bf16_qw_imp_s025\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    median_difference: 1.108706\n    permutation_p: 0\n    cohens_d: 1.2329\n    bootstrap_ci_95:\n    - 0.609247\n    - 1.469002\n    wilcoxon_p: 0\n    n_bootstrap: 10000\n    n_paired: 46\n- exp_id: bf16_qw_imp_s030\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    median_difference: 2.619385\n    permutation_p: 0\n    cohens_d: 1.4394\n    bootstrap_ci_95:\n    - 1.722281\n    - 3.651063\n    wilcoxon_p: 0\n    n_bootstrap: 10000\n    n_paired: 46\n- exp_id: bf16_qw_rand_s015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 1.6652\n        median: 0.1381\n        ci:\n        - 1.0986\n        - 2.4042\n        median_ci:\n        - 0.1025\n        - 0.2074\n        winsorized_mean: 1.0044\n        skewness: 7.1842\n      mid:\n        mean: 1.6975\n        median: 0.2194\n        ci:\n        - 0.4473\n        - 3.4612\n        median_ci:\n        - -0.0048\n        - 0.6621\n        winsorized_mean: 1.4038\n        skewness: 3.2101\n      low:\n        mean: 1.4082\n        median: 0.1878\n        ci:\n        - 0.8358\n        - 2.06\n        median_ci:\n        - 0.0962\n        - 0.3139\n        winsorized_mean: 0.9403\n        skewness: 7.1113\n    perplexity:\n      high:\n        dense: 1.0737\n        attn: 1.3939\n        kv: 2.0487\n        both: 4.2076\n      mid:\n        dense: 1.1322\n        attn: 1.4175\n        kv: 2.3709\n        both: 4.6105\n      low:\n        dense: 1.1517\n        attn: 1.7177\n        kv: 3.3253\n        both: 5.4788\n    phase_stats:\n      high:\n        n_tokens: 16289\n        n_segments: 295\n      mid:\n        n_tokens: 4372\n        n_segments: 26\n      low:\n        n_tokens: 32227\n        n_segments: 276\n    n_problems: 50\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: false\n      overall: FAIL\n    median_difference: -0.029401\n    permutation_test:\n      p_value: 0.7657\n      B: 10000\n    cohens_d: -0.0507\n    bootstrap_ci_95:\n    - -0.2106\n    - 0.2124\n    wilcoxon_p: 0.862554\n    phase_median_ii:\n      high: 0.1381\n      mid: 0.2194\n      low: 0.1878\n- exp_id: bf16_qw_rand_s020\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 2.58579\n        median: 0.48549\n        ci:\n        - 1.769404\n        - 3.501692\n        median_ci:\n        - 0.304626\n        - 0.658814\n        winsorized_mean: 1.80021\n        skewness: 5.4038\n      mid:\n        mean: 5.69684\n        median: 0.76699\n        ci:\n        - 1.69004\n        - 12.276143\n        median_ci:\n        - 0.482838\n        - 3.392541\n        winsorized_mean: 4.304174\n        skewness: 3.526\n      low:\n        mean: 65.915714\n        median: 0.614438\n        ci:\n        - -18.581948\n        - 221.709429\n        median_ci:\n        - 0.484725\n        - 0.848787\n        winsorized_mean: 2.389244\n        skewness: 16.2163\n    perplexity:\n      high:\n        dense: 1.0737\n        attn: 1.6115\n        kv: 2.5041\n        both: 5.9394\n      mid:\n        dense: 1.1322\n        attn: 1.7583\n        kv: 3.0658\n        both: 10.5578\n      low:\n        dense: 1.1517\n        attn: 75.631\n        kv: 4.3535\n        both: 140.6269\n    phase_stats:\n      high:\n        n_tokens: 16289\n        n_segments: 295\n      mid:\n        n_tokens: 4372\n        n_segments: 26\n      low:\n        n_tokens: 32227\n        n_segments: 276\n    n_problems: 50\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: false\n      overall: FAIL\n    median_difference: 0.128948\n    permutation_test:\n      p_value: 0.352\n      B: 10000\n    cohens_d: 0.247\n    bootstrap_ci_95:\n    - -0.139\n    - 0.215\n    wilcoxon_p: 0.149\n    phase_median_ii:\n      high: 0.4739\n      mid: 0.8757\n      low: 0.4847\n- exp_id: bf16_qw_rand_s025\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 14.4213\n        median: 1.6043\n        ci:\n        - 7.1074\n        - 23.4587\n        median_ci:\n        - 0.6977\n        - 3.0736\n        winsorized_mean: 9.3765\n        skewness: 4.8263\n      mid:\n        mean: 18.6458\n        median: 2.2225\n        ci:\n        - 3.3729\n        - 41.6037\n        median_ci:\n        - 0.6093\n        - 11.5889\n        winsorized_mean: 14.2901\n        skewness: 3.8245\n      low:\n        mean: 17.7277\n        median: 2.2641\n        ci:\n        - 4.3523\n        - 37.2093\n        median_ci:\n        - 1.2218\n        - 4.8561\n        winsorized_mean: 9.9876\n        skewness: 5.7652\n    perplexity:\n      high:\n        dense: 1.0737\n        attn: 2.0183\n        kv: 3.1882\n        both: 9.7654\n      mid:\n        dense: 1.1322\n        attn: 2.3476\n        kv: 4.0124\n        both: 17.3298\n      low:\n        dense: 1.1517\n        attn: 2.7834\n        kv: 5.8762\n        both: 25.4321\n    phase_stats:\n      high:\n        n_tokens: 16289\n        n_segments: 295\n      mid:\n        n_tokens: 4372\n        n_segments: 26\n      low:\n        n_tokens: 32227\n        n_segments: 276\n    n_problems: 50\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: false\n      overall: FAIL\n    median_difference: 1.144074\n    permutation_test:\n      p_value: 0.1679\n      B: 10000\n    cohens_d: 0.1574\n    bootstrap_ci_95:\n    - -0.3166\n    - 4.1645\n    wilcoxon_p: 0.010313\n    phase_median_ii:\n      high: 1.6043\n      mid: 2.2225\n      low: 2.2641\n- exp_id: bf16_qw_rand_s030\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    median_high: 4.200557\n    median_mid: 6.477036\n    median_low: 8.065662\n    median_diff: 2.418272\n    permutation_p: 0.012\n    cohens_d: -0.03513\n    wilcoxon_p: 0.01566\n    bootstrap_ci_low: 0.241897\n    bootstrap_ci_high: 3.314824\n- exp_id: c4_entropy\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    importance_entropy_delta:\n      s015: -0.0402\n      s020: -0.0472\n      s025: -0.0446\n      s030: -0.0436\n    random_entropy_delta:\n      s015: 0.1283\n      s020: 0.136\n      s025: 0.2171\n      s030: 0.2327\n    importance_gini_delta:\n      s015: -0.0301\n      s020: -0.0404\n      s025: -0.0647\n      s030: -0.0806\n    random_gini_delta:\n      s015: -0.0309\n      s020: -0.0403\n      s025: -0.062\n      s030: -0.0732\n    importance_cv_delta:\n      s015: -0.564\n      s020: -0.774\n      s025: -1.287\n      s030: -1.665\n    random_cv_delta:\n      s015: -1.021\n      s020: -1.203\n      s025: -1.923\n      s030: -2.137\n    problems_completed: 30\n    runtime_minutes: 69.1\n- exp_id: qwen_c4_entropy\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    problems_completed: 30\n    qwen_importance_entropy_delta:\n      s015: -0.0733\n      s020: -0.0759\n      s025: 0.0451\n      s030: -0.0072\n    qwen_random_entropy_delta:\n      s015: 0.0838\n      s020: 0.0901\n      s025: 0.2168\n      s030: 0.1968\n    qwen_importance_gini_delta:\n      s015: -0.0103\n      s020: -0.0121\n      s025: -0.01\n      s030: -0.0202\n    qwen_random_gini_delta:\n      s015: -0.0186\n      s020: -0.0229\n      s025: -0.0337\n      s030: -0.0448\n    qwen_importance_cv_delta:\n      s015: -0.045\n      s020: -0.208\n      s025: -1.491\n      s030: -1.142\n    qwen_random_cv_delta:\n      s015: -0.778\n      s020: -0.889\n      s025: -1.5\n      s030: -1.677\n    cross_model_notes: random entropy increase consistent; importance entropy collapse\n      inconsistent at s025 (reversed to +0.045) and near-zero at s030; gini/cv directions\n      consistent but Qwen magnitudes smaller\n- exp_id: bf16_ds_imp_s010\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    verdict: FAIL\n    problems: 50\n    II_high_sparsity_median: 0.0027\n    II_high_sparsity_mean: -0.1998\n    II_low_sparsity_median: 0.0151\n    II_low_sparsity_mean: -0.1066\n    II_mid_sparsity_median: 0.0061\n    II_mid_sparsity_mean: -0.0131\n    high_sparsity_tokens: 21086\n    low_sparsity_tokens: 27748\n    mid_sparsity_tokens: 13306\n- exp_id: bf16_ds_imp_s035\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    verdict: PASS\n    problems: 50\n    II_high_sparsity_median: 0.1051\n    II_high_sparsity_mean: 1.4309\n    II_low_sparsity_median: 28.7649\n    II_low_sparsity_mean: 104.1892\n    II_mid_sparsity_median: 4.9542\n    II_mid_sparsity_mean: 20.326\n    high_sparsity_tokens: 21086\n    low_sparsity_tokens: 27748\n    mid_sparsity_tokens: 13306\n    ci_overlap_test: low_sparsity vs mid_sparsity CI non-overlapping at 0.35\n- exp_id: bf16_qw_imp_s010\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_problems: 50\n    overall_verdict: PASS\n    ci_overlap_test: PASS\n    sign_reversal_test: FAIL\n    high_sparsity_II_median: 0.0001\n    high_sparsity_II_median_CI:\n    - -0.0028\n    - 0.0005\n    high_sparsity_II_mean: -0.0887\n    high_sparsity_II_mean_CI:\n    - -0.1235\n    - -0.0591\n    low_sparsity_II_median: -0.0444\n    low_sparsity_II_median_CI:\n    - -0.0967\n    - -0.0152\n    low_sparsity_II_mean: -0.2431\n    low_sparsity_II_mean_CI:\n    - -0.3817\n    - -0.1202\n    mid_sparsity_II_median: -0.0359\n    mid_sparsity_II_median_CI:\n    - -0.0963\n    - -0.015\n    mid_sparsity_II_mean: -0.084\n    mid_sparsity_II_mean_CI:\n    - -0.1366\n    - -0.035\n    ppl_high_dense: 1.074\n    ppl_high_both: 1.228\n    ppl_low_dense: 1.152\n    ppl_low_both: 3.204\n    ppl_mid_dense: 1.133\n    ppl_mid_both: 1.741\n- exp_id: bf16_qw_imp_s035\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_problems: 50\n    overall_verdict: PASS\n    ci_overlap_test: PASS\n    sign_reversal_test: FAIL\n    high_sparsity_II_median: 0.0232\n    high_sparsity_II_median_CI:\n    - 0.0154\n    - 0.0383\n    high_sparsity_II_mean: 0.1643\n    high_sparsity_II_mean_CI:\n    - 0.0844\n    - 0.2495\n    low_sparsity_II_median: 8.2358\n    low_sparsity_II_median_CI:\n    - 6.1564\n    - 10.9231\n    low_sparsity_II_mean: 18.9673\n    low_sparsity_II_mean_CI:\n    - 14.5015\n    - 23.9752\n    mid_sparsity_II_median: 0.9577\n    mid_sparsity_II_median_CI:\n    - 0.171\n    - 3.5575\n    mid_sparsity_II_mean: 8.0734\n    mid_sparsity_II_mean_CI:\n    - 2.0224\n    - 16.8946\n    ppl_high_dense: 1.0738\n    ppl_high_both: 2.3435\n    ppl_low_dense: 1.1518\n    ppl_low_both: 58.0358\n    ppl_mid_dense: 1.1327\n    ppl_mid_both: 20.9912\n    high_sparsity_tokens: 16289\n    low_sparsity_tokens: 32227\n    mid_sparsity_tokens: 4372\n- exp_id: c2_n500_deepseek\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_problems: 500\n    effective_n: 496\n    mid_null_rate: 0.102\n    imp_s015_median_ii: 0.3907\n    imp_s015_ci:\n    - 0.3496\n    - 0.4431\n    imp_s015_wilcoxon_p: 1.27e-70\n    imp_s020_median_ii: 1.2149\n    imp_s020_ci:\n    - 1.1072\n    - 1.3365\n    imp_s020_wilcoxon_p: 3.98e-75\n    imp_s025_median_ii: 3.9857\n    imp_s025_ci:\n    - 3.5272\n    - 4.3588\n    imp_s025_wilcoxon_p: 1.99e-78\n    imp_s030_median_ii: 8.4813\n    imp_s030_ci:\n    - 7.7543\n    - 9.6919\n    imp_s030_wilcoxon_p: 1.09e-79\n    rand_s015_median_ii: 0.0139\n    rand_s015_wilcoxon_p: 0.863\n    rand_s020_median_ii: 0.0315\n    rand_s020_wilcoxon_p: 0.28\n    rand_s025_median_ii: 0.2574\n    rand_s025_bonf_p: 0.005839\n    rand_s025_fdr_p: 0.001914\n    rand_s030_median_ii: 0.5096\n    rand_s030_bonf_p: 0.005903\n    rand_s030_fdr_p: 0.001914\n    dz_s015_s020: -0.925\n    dz_s020_s025: -0.824\n    dz_s025_s030: -0.773\n    dz_s015_s030: -0.944\n    all_dz_reliable: true\n    dose_response_monotonic: true\n    dose_response_spearman_rho: 1\n    dose_response_perm_p: 0.0417\n    imp_rand_ratio_range: 15.5-38.6x\n    bonferroni_k: 4\n    bonferroni_note: Bonferroni k=4 family-wise (D066 revision)\n- exp_id: c3_llama_arch\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: c2_ds_n500\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: c2_qw_n500\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: c3_llama\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    model: DeepSeek-R1-Distill-Llama-8B\n    n_problems: 50\n    n_valid: 49\n    n_skipped: 1\n    conditions_completed: 8/8\n    n_bootstrap: 10000\n    bonferroni_k: 4\n    imp_vs_rand_dz:\n      s015: 0.1923\n      s020: 0.255\n      s025: 0.2902\n      s030: 0.3352\n    imp_vs_rand_dz_ci:\n      s015:\n      - -0.0862\n      - 0.496\n      s020:\n      - -0.0248\n      - 0.5381\n      s025:\n      - 0.0081\n      - 0.6121\n      s030:\n      - 0.0606\n      - 0.6629\n    imp_vs_rand_dz_interpretation:\n      s015: negligible\n      s020: small\n      s025: small\n      s030: small\n    imp_vs_rand_dz_monotonic: true\n    phase_gradient_importance_dz:\n      s015: 1.0079\n      s020: 1.108\n      s025: 1.1227\n      s030: 1.0038\n    phase_gradient_importance_dz_ci:\n      s015:\n      - 0.593\n      - 1.7025\n      s020:\n      - 0.8144\n      - 1.5698\n      s025:\n      - 0.8735\n      - 1.5768\n      s030:\n      - 0.8099\n      - 1.3519\n    phase_gradient_importance_interpretation: all_large\n    phase_gradient_random_dz:\n      s015: 0.3497\n      s020: 0.373\n      s025: 0.4476\n      s030: 0.4385\n    phase_gradient_random_dz_ci:\n      s015:\n      - 0.0665\n      - 0.6916\n      s020:\n      - 0.0868\n      - 0.7335\n      s025:\n      - 0.1669\n      - 0.7698\n      s030:\n      - 0.1966\n      - 0.707\n    phase_gradient_random_interpretation: all_small\n    median_diff:\n      s015: 0.0203\n      s020: 0.0221\n      s025: 0.0947\n      s030: 0.3562\n    median_diff_ci:\n      s015:\n      - 0.0016\n      - 0.0435\n      s020:\n      - -0.0905\n      - 0.187\n      s025:\n      - -0.0037\n      - 0.3029\n      s030:\n      - -0.0691\n      - 0.5442\n    wilcoxon_p:\n      s015: 0.0549\n      s020: 0.0632\n      s025: 0.0209\n      s030: 0.0074\n    wilcoxon_p_bonferroni:\n      s015: 0.2195\n      s020: 0.2527\n      s025: 0.0834\n      s030: 0.0294\n    significant_bonferroni:\n      s015: false\n      s020: false\n      s025: false\n      s030: true\n    cross_arch_comparison:\n      deepseek_importance_dz:\n        s015: 0.4416\n        s020: 0.5195\n        s025: 0.6831\n        s030: 0.8031\n      llama_importance_dz:\n        s015: 1.0079\n        s020: 1.108\n        s025: 1.1227\n        s030: 1.0038\n      delta:\n        s015: 0.5663\n        s020: 0.5885\n        s025: 0.4396\n        s030: 0.2007\n      note: LLaMA shows uniformly large d_z (all >1.0) vs DeepSeek medium-to-large\n- exp_id: c5b_pilot\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    s025_uniform_median_ii: 1.0435\n    s025_oracle_median_ii: 0.856\n    s025_oracle_recovery_pct: 18\n    s025_oracle_recovery_ci:\n    - -39\n    - 45.8\n    s025_oracle_wilcoxon_p: 0.0021\n    s025_heuristic_median_ii: 0.7127\n    s025_heuristic_recovery_pct: 31.7\n    s025_heuristic_recovery_ci:\n    - -22.8\n    - 66\n    s025_heuristic_wilcoxon_p: 0.0236\n    gate_criterion: oracle_recovery > 30%\n    gate_result: FAIL\n    s030_status: not_completed\n    n_problems: 30\n- exp_id: c2_qw_n500_r3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_problems: 500\n    effective_n: 475\n    filter: low+high valid only (mid-null allowed)\n    mid_null_rate: 0.452\n    imp_s015_median_ii: 0.0659\n    imp_s015_ci:\n    - 0.0492\n    - 0.0925\n    imp_s015_wilcoxon_p: 8.66e-15\n    imp_s015_bonf_p: 3.46e-14\n    imp_s020_median_ii: 0.3073\n    imp_s020_ci:\n    - 0.2612\n    - 0.3564\n    imp_s020_wilcoxon_p: 6.84e-42\n    imp_s020_bonf_p: 2.74e-41\n    imp_s025_median_ii: 1.0745\n    imp_s025_ci:\n    - 0.9766\n    - 1.1787\n    imp_s025_wilcoxon_p: 1.06e-68\n    imp_s025_bonf_p: 4.25e-68\n    imp_s030_median_ii: 3.155\n    imp_s030_ci:\n    - 2.7834\n    - 3.5582\n    imp_s030_wilcoxon_p: 9.21e-74\n    imp_s030_bonf_p: 3.69e-73\n    rand_s015_median_ii: -0.0111\n    rand_s015_wilcoxon_p: 0.172\n    rand_s015_bonf_p: 0.687\n    rand_s020_median_ii: 0.0153\n    rand_s020_wilcoxon_p: 0.2\n    rand_s020_bonf_p: 0.8\n    rand_s025_median_ii: 0.3931\n    rand_s025_wilcoxon_p: 1.59e-11\n    rand_s025_bonf_p: 6.37e-11\n    rand_s025_fdr_p: 2.63e-11\n    rand_s030_median_ii: 0.9127\n    rand_s030_wilcoxon_p: 2.92e-15\n    rand_s030_bonf_p: 1.17e-14\n    rand_s030_fdr_p: 5.61e-15\n    dz_s015_s020: -0.629\n    dz_s020_s025: -0.865\n    dz_s025_s030: -0.767\n    dz_s015_s030: -0.923\n    all_dz_reliable: true\n    dose_response_monotonic: true\n    dose_response_spearman_rho: 1\n    dose_response_perm_p: 0.0417\n    imp_rand_ratio_range: 2.7-20.1x\n    bonferroni_k: 4\n    bonferroni_note: Bonferroni k=4 family-wise (D066 revision)\n- exp_id: sf5_asymmetric_spot\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    config_a_h02_kv03:\n      II_low: 19.51\n      II_mid: 6.05\n      II_high: 0.38\n      D: 19.13\n    config_b_h03_kv02:\n      II_low: 18.77\n      II_mid: 3.97\n      II_high: 0.52\n      D: 18.25\n    pre_registered_criterion_passed: true\n    gradient_direction: II_low >> II_mid >> II_high (consistent with symmetric baseline)\n- exp_id: gsm8k_profiling_ds\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    version: v3_median\n    n_problems: 50\n    method: median + Wilcoxon + bootstrap_median(B=10000)\n    importance:\n      s015:\n        median_gradient: 0.241\n        ci_low: 0.077\n        ci_high: 0.478\n        wilcoxon_p: 0.0003\n      s020:\n        median_gradient: 0.74\n        ci_low: 0.314\n        ci_high: 1.119\n        wilcoxon_p: 0.0001\n      s025:\n        median_gradient: 1.992\n        ci_low: 0.933\n        ci_high: 2.82\n        wilcoxon_p: 0.0001\n      s030:\n        median_gradient: 4.682\n        ci_low: 2.121\n        ci_high: 10.557\n        wilcoxon_p: 0.0001\n    imp_rand_ratio:\n      s015: 2.3\n      s020: 2.5\n      s025: 3.8\n      s030: 2.8\n    dose_response_monotonic: true\n- exp_id: gsm8k_profiling_qw\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    version: v3_median\n    n_problems: 50\n    method: median + Wilcoxon + bootstrap_median(B=10000)\n    importance:\n      s015:\n        median_gradient: 0.039\n      s020:\n        median_gradient: 0.158\n      s025:\n        median_gradient: 1.1\n      s030:\n        median_gradient: 2.092\n    qw_rand_s030: INVALID\n- exp_id: think_phase_validation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    effective_n: 48\n    skipped_problems: 2\n    median_kappa: 0.887\n    thinking_in_low_sparsity_phase: 0.578\n    answer_in_high_sparsity_phase: 0.627\n    note: Phase segmentation based on dense model — 4 sparsity conditions share identical\n      phase boundaries, effective sample n=48 not n=192\n- exp_id: r9c2-spike\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: r9c2-spike-v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: r9c2-spike-v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: c2_accuracy_eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_problems: 50\n    ds_dense_acc: 0.52\n    ds_s015_acc: 0.36\n    ds_s015_delta: -0.16\n    ds_s030_acc: 0.1\n    ds_s030_delta: -0.42\n    qw_dense_acc: 0.32\n    qw_s015_acc: 0.34\n    qw_s015_delta: 0.02\n    qw_s030_acc: 0.14\n    qw_s030_delta: -0.18\n    ds_s030_chinese_reasoning_rate: 0.4\n    ds_dense_truncation_rate: 0.56\n    note: v2 rescored with fixed radical+degree matcher. DS s015 34→36, QW s015 32→34\n- exp_id: acc_ds_s020\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ds_s020_acc: 0.26\n    ds_s020_acc_v2: 0.26\n    ds_s020_correct: 13\n    ds_s020_total: 50\n    ds_s020_delta_vs_dense: -0.26\n    output_truncated_count: 32\n    output_truncated_rate: 0.64\n    extraction_failure_count: 31\n    extraction_failure_rate: 0.62\n    total_time_s: 1560\n    note: v2 rescored with fixed radical+degree matcher; 0 changes. Dense baseline=0.52\n- exp_id: acc_ds_s025\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy: 0.08\n    correct: 4\n    total: 50\n    null_count: 37\n    null_rate: 0.74\n    output_truncated_count: 38\n    output_truncated_rate: 0.76\n    wrong_count: 9\n    wrong_rate: 0.18\n    extraction_failure_count: 1\n    extraction_failure_rate: 0.02\n    total_time_s: 1670.5\n    heads_pruned: 196\n    delta_vs_dense: -0.44\n- exp_id: acc_qw_s020\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    qw_s020_acc: 0.26\n    qw_s020_correct: 13\n    qw_s020_total: 50\n    qw_s020_delta_vs_dense: -0.06\n    null_count: 2\n    null_rate: 0.04\n    output_truncated_count: 2\n    output_truncated_rate: 0.04\n    extraction_failure_count: 0\n    extraction_failure_rate: 0\n    wrong_count: 35\n    wrong_rate: 0.7\n    heads_pruned: 140\n    total_time_s: 598\n    note: v2 rescored with fixed radical+degree matcher\n- exp_id: acc_qw_s025\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    qw_s025_acc: 0.32\n    qw_s025_correct: 16\n    qw_s025_total: 50\n    qw_s025_delta_vs_dense: 0\n    null_count: 8\n    null_rate: 0.16\n    output_truncated_count: 2\n    output_truncated_rate: 0.04\n    extraction_failure_count: 6\n    extraction_failure_rate: 0.12\n    wrong_count: 26\n    wrong_rate: 0.52\n    heads_pruned: 196\n    total_time_s: 559\n    note: v2 rescored with fixed radical+degree matcher; 3 problems flipped (sqrt+degree)\n- exp_id: acc_qw_s020_n100\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    batch1_acc: 0.26\n    batch1_correct: 13\n    batch1_total: 50\n    batch1_source: acc_qw_s020_b1_8k (v2, 8k tokens)\n    batch2_acc: 0.46\n    batch2_correct: 23\n    batch2_total: 50\n    combined_acc: 0.36\n    combined_correct: 36\n    combined_total: 100\n    note: 'batch effect: batch1=26% vs batch2=46%, Δ=20pp'\n- exp_id: acc_qw_s025_n100\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    batch1_acc: 0.32\n    batch1_correct: 16\n    batch1_total: 50\n    batch1_source: acc_qw_s025_b1_8k (v2, 8k tokens)\n    batch2_acc: 0.34\n    batch2_correct: 17\n    batch2_total: 50\n    combined_acc: 0.33\n    combined_correct: 33\n    combined_total: 100\n- exp_id: acc_ds_dense_8k\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: acc_ds_s015_8k\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: acc_ds_s020_8k\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: acc_ds_s025_8k\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: acc_ds_s030_8k\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: acc_qw_dense_n100\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    batch1_correct: 22\n    batch1_total: 50\n    batch1_acc: 0.44\n    batch1_source: acc_qw_dense_b1_8k (v2, 8k tokens)\n    batch2_correct: 24\n    batch2_total: 50\n    batch2_acc: 0.48\n    combined_correct: 46\n    combined_total: 100\n    combined_acc: 0.46\n- exp_id: acc_qw_s015_n100\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    batch1_acc: 0.46\n    batch1_correct: 23\n    batch1_total: 50\n    batch1_source: acc_qw_s015_b1_8k (v2, 8k tokens)\n    batch2_acc: 0.38\n    batch2_correct: 19\n    batch2_total: 50\n    combined_acc: 0.42\n    combined_correct: 42\n    combined_total: 100\n- exp_id: acc_qw_s030_n100\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    batch1_correct: 7\n    batch1_total: 50\n    batch1_acc: 0.14\n    batch1_source: acc_qw_s030_b1_8k (v2, 8k tokens)\n    batch2_correct: 12\n    batch2_total: 50\n    batch2_acc: 0.24\n    combined_correct: 19\n    combined_total: 100\n    combined_acc: 0.19\n- exp_id: acc_ds_s015_8k_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.48\n    correct: 24\n    total: 50\n    truncation_rate: 0.32\n    truncated_count: 16\n    non_truncated_accuracy: 0.706\n    non_truncated_correct: 24\n    non_truncated_total: 34\n    wall_time_s: 3967\n    max_new_tokens: 8192\n- exp_id: acc_ds_s020_8k_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.3\n    correct: 15\n    total: 50\n    truncated_count: 28\n    truncated_rate: 0.56\n    extraction_failures: 1\n    non_truncated_accuracy: 0.682\n    non_truncated_correct: 15\n    non_truncated_total: 22\n    total_time_seconds: 5549\n    max_new_tokens: 8192\n- exp_id: acc_ds_s025_8k_v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy: 0.08\n    correct: 4\n    total: 50\n    truncated_count: 38\n    truncated_rate: 0.76\n    avg_tokens: 6343.8\n    max_new_tokens: 8192\n    total_time_seconds: 6827.8\n    null_count: 36\n- exp_id: acc_ds_s030_8k_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.04\n    correct: 2\n    total: 50\n    truncation_rate: 0.76\n    truncated_count: 38\n    extraction_failures: 3\n    non_truncated_accuracy: 0.167\n    non_truncated_correct: 2\n    non_truncated_total: 12\n    max_new_tokens: 8192\n    avg_tokens: 6566.3\n    total_time_seconds: 7095.1\n- exp_id: gsm8k_qw_rand_s025\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: gsm8k_qw_rand_s030\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: acc_qw_s020_n100_b2_fix\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    batch2_correct: 23\n    batch2_total: 50\n    batch2_acc: 0.46\n    batch1_correct_v2: 13\n    batch1_total: 50\n    batch1_acc_v2: 0.26\n    combined_correct: 36\n    combined_total: 100\n    combined_acc: 0.36\n    null_count: 2\n    truncated_count: 1\n    total_time_seconds: 884.3\n    max_new_tokens: 8192\n    original_batch2_correct: 22\n    original_batch2_acc: 0.44\n    delta_vs_original: +1 correct (+0.02 acc)\n- exp_id: acc_qw_s025_n100_b2_fix\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.34\n    correct: 17\n    n_problems: 50\n    truncation_rate: 0.06\n    truncated_count: 3\n    avg_tokens: 1044\n    max_new_tokens: 8192\n    total_time_seconds: 1099\n    batch: b2 (problems 51-100)\n    merged_n100_accuracy: 0.33\n    merged_n100_correct: 33\n    merged_n100_note: batch1 used max_new_tokens=2048, batch2_fix used 8192 — mismatch\n- exp_id: acc_ds_dense_8k_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.74\n    correct: 37\n    n_problems: 50\n    truncation_rate: 0.16\n    truncated_count: 8\n    avg_tokens: 3126\n    max_new_tokens: 8192\n    total_time_seconds: 2882\n- exp_id: gsm8k_qw_rand_s025_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    verdict: PASS\n    n_problems: 50\n    n_bootstrap: 1000\n    seed: 42\n    high_sparsity:\n      n_segments: 216\n      n_tokens: 9326\n      ppl_dense: 1.0695\n      ppl_attn: 5.9362\n      ppl_kv: 3.4316\n      ppl_both: 15.7484\n      ii_mean: 6.5954\n      ii_ci:\n      - 1.1114\n      - 11.3791\n      ii_median: 0.7176\n      ii_median_ci:\n      - 0.5959\n      - 0.9347\n      winsorized_mean: 6.5046\n      skewness: -4.6807\n      outlier_count: 3\n    low_sparsity:\n      n_segments: 252\n      n_tokens: 29224\n      ppl_dense: 1.1972\n      ppl_attn: 11.5347\n      ppl_kv: 5.6038\n      ppl_both: 21.6874\n      ii_mean: 2.3883\n      ii_ci:\n      - -8.4602\n      - 11.029\n      ii_median: 1.4587\n      ii_median_ci:\n      - 1.1121\n      - 2.0451\n      winsorized_mean: 5.8911\n      skewness: -7.6074\n      outlier_count: 4\n    mid_sparsity:\n      n_segments: 51\n      n_tokens: 5954\n      ppl_dense: 1.2601\n      ppl_attn: 13.4132\n      ppl_kv: 6.4841\n      ppl_both: 20.8714\n      ii_mean: 4.5407\n      ii_ci:\n      - -4.8854\n      - 12.4605\n      ii_median: 1.1272\n      ii_median_ci:\n      - 0.637\n      - 3.3729\n      winsorized_mean: 6.3284\n      skewness: -3.4048\n      outlier_count: 1\n- exp_id: gsm8k_qw_rand_s030_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    verdict: PASS\n    n_problems: 50\n    n_bootstrap: 1000\n    seed: 42\n    high_sparsity:\n      n_segments: 216\n      n_tokens: 9326\n      null_ratio: 2/50\n      ppl_dense: 1.0695\n      ppl_attn: 6.5613\n      ppl_kv: 4.481\n      ppl_both: 23.7486\n      ii_mean: 11.83\n      ii_median: 2.31\n      ii_ci:\n      - 6.17\n      - 17.04\n      ii_median_ci:\n      - 1.64\n      - 2.81\n      winsorized_mean: 10.55\n      skewness: -2.29\n      outlier_count: 7\n    low_sparsity:\n      n_segments: 252\n      n_tokens: 29224\n      null_ratio: 5/50\n      ppl_dense: 1.1972\n      ppl_attn: 6.3283\n      ppl_kv: 8.5374\n      ppl_both: 56.2304\n      ii_mean: 31.26\n      ii_median: 5.2\n      ii_ci:\n      - 17.84\n      - 47.86\n      ii_median_ci:\n      - 3.95\n      - 7.24\n      winsorized_mean: 16.35\n      skewness: 7.57\n      outlier_count: 4\n    mid_sparsity:\n      n_segments: 51\n      n_tokens: 5954\n      null_ratio: 17/50\n      ppl_dense: 1.2601\n      ppl_attn: 18.6162\n      ppl_kv: 11.6625\n      ppl_both: 47.9019\n      ii_mean: 18.02\n      ii_median: 2.7\n      ii_ci:\n      - 0.09\n      - 36.69\n      ii_median_ci:\n      - 1.46\n      - 8.77\n      winsorized_mean: 18.22\n      skewness: 0.43\n      outlier_count: 2\n- exp_id: acc_qw_dense_b1_8k\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.44\n    correct: 22\n    n_problems: 50\n    truncation_rate: 0.02\n    truncated_count: 1\n    avg_tokens: 759.7\n    max_tokens_generated: 8192\n    max_new_tokens: 8192\n    total_time_seconds: 681.8\n    null_count: 0\n    batch: b1_v2 (problems 1-50, 8k tokens)\n    old_batch1_acc: 0.32\n    old_batch1_correct: 16\n    new_combined_n100_acc: 0.46\n    new_combined_n100_correct: 46\n    batch2_acc: 0.48\n    batch2_correct: 24\n- exp_id: acc_qw_s015_b1_8k\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.46\n    correct: 23\n    total: 50\n    truncation_rate_8k: 0.02\n    gen_over_2k: 3\n    gen_over_2k_all_wrong: true\n    max_gen_length: 8192\n    mean_gen_length: 776\n    batch: b1_v2 (problems 1-50, 8k tokens)\n    batch2_acc: 0.38\n    batch2_correct: 19\n    new_combined_n100_acc: 0.42\n    new_combined_n100_correct: 42\n    batch2_source: acc_qw_s015_n100\n- exp_id: acc_qw_s020_b1_8k\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.26\n    correct: 13\n    n_problems: 50\n    truncation_rate: 0.02\n    truncated_count: 1\n    avg_tokens: 722.1\n    max_tokens_generated: 8192\n    max_new_tokens: 8192\n    total_time_seconds: 729.1\n    null_count: 0\n    batch: b1_v2 (problems 1-50, 8k tokens)\n    old_batch1_acc: 0.26\n    old_batch1_correct: 13\n    new_combined_n100_acc: 0.36\n    new_combined_n100_correct: 36\n    batch2_acc: 0.46\n    batch2_correct: 23\n- exp_id: acc_qw_s025_b1_8k\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy: 0.32\n    correct: 16\n    n_problems: 50\n    truncation_rate: 0.04\n    truncated_count: 2\n    extraction_failures: 6\n    avg_tokens: 797.3\n    total_time_seconds: 831.6\n    batch: b1_v2 (problems 1-50, 8k tokens)\n    batch2_acc: 0.34\n    batch2_correct: 17\n    new_combined_n100_acc: 0.33\n    new_combined_n100_correct: 33\n    batch2_source: acc_qw_s025_n100_b2_fix\n- exp_id: acc_qw_s030_b1_8k\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    accuracy: 0.14\n    correct: 7\n    total: 50\n    truncation_rate: 0.04\n    truncated_count: 2\n    extraction_failures: 8\n    max_new_tokens: 8192\n    total_time_seconds: 886.7\n    batch: b1_v2 (problems 1-50, 8k tokens)\n    old_batch1_acc: 0.14\n    old_batch1_correct: 7\n    batch2_acc: 0.24\n    batch2_correct: 12\n    new_combined_n100_acc: 0.19\n    new_combined_n100_correct: 19\n- exp_id: c8_llama_n250\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    first_run_failed: true\n    failure_reason: 'bash wrapper wait logic bug: subprocess OOM/error exits silently,\n      script marks DONE without output validation. All 8 output dirs empty.'\n    fix_worker: worker_code_c8_llama_n250_fix_20260516T031229\n    fix_plan: 1) diagnose script + OOM, 2) fix exit code + output validation + GPU\n      monitor, 3) dry-run 1 condition on GPU 2, 4) full launch on GPU 2-3 via submit_training_job\n- exp_id: c4_think_validation_math500\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    v2_math500_kappa_adaptive: 0.88\n    v2_math500_ds_problems: 48\n    v2_math500_ds_tokens: 32055\n    v2_math500_thinking_in_low: 0.816\n    v2_math500_answer_in_high: 0.655\n    v2_math500_temporal_ordering_ds: 0.576\n    v2_math500_temporal_ordering_qw: 0.479\n    v2_qw_pct_positive: 0.98\n    v2_scope: MATH-500\n    v2_models: DS+QW\n    v2_status: ALL_CRITERIA_MET\n    v1_kappa_adaptive: 0.8804\n    v1_auc: 0.9808\n    SCOPE_FLAG: v2_validated_on_MATH500\n- exp_id: c5_per_phase_gini\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    qw_complete: true\n    ds_complete: true\n    n_problems: 30\n    qw_dense_gini_baselines:\n      low: 0.2675\n      mid: 0.2078\n      high: 0.2599\n    qw_importance:\n      s015:\n        global_delta: -0.0103\n        low_delta: -0.0165\n        mid_delta: -0.0094\n        high_delta: -0.012\n      s020:\n        global_delta: -0.0121\n        low_delta: -0.02\n        mid_delta: -0.0115\n        high_delta: -0.0143\n      s025:\n        global_delta: -0.01\n        low_delta: -0.0286\n        mid_delta: -0.0168\n        high_delta: -0.0207\n      s030:\n        global_delta: -0.0202\n        low_delta: -0.035\n        mid_delta: -0.0183\n        high_delta: -0.0239\n    qw_random:\n      s015:\n        global_delta: -0.0186\n        low_delta: -0.0083\n        mid_delta: -0.0038\n        high_delta: -0.0036\n      s020:\n        global_delta: -0.0229\n        low_delta: -0.0119\n        mid_delta: -0.0053\n        high_delta: -0.0067\n      s025:\n        global_delta: -0.0337\n        low_delta: -0.0014\n        mid_delta: -0.0081\n        high_delta: 0.0045\n      s030:\n        global_delta: -0.0447\n        low_delta: -0.0221\n        mid_delta: -0.0077\n        high_delta: -0.0061\n    ds_importance:\n      s015:\n        global_delta: -0.0301\n        low_delta: -0.0163\n        mid_delta: -0.0073\n        high_delta: -0.0152\n      s020:\n        global_delta: -0.0404\n        low_delta: -0.0209\n        mid_delta: -0.0092\n        high_delta: -0.02\n      s025:\n        global_delta: -0.0647\n        low_delta: -0.0313\n        mid_delta: -0.0133\n        high_delta: -0.0267\n      s030:\n        global_delta: -0.0806\n        low_delta: -0.0373\n        mid_delta: -0.0183\n        high_delta: -0.0314\n    ds_random:\n      s015:\n        global_delta: -0.0309\n        low_delta: -0.0102\n        mid_delta: -0.0006\n        high_delta: -0.0062\n      s020:\n        global_delta: -0.0403\n        low_delta: -0.012\n        mid_delta: -0.0007\n        high_delta: -0.0085\n      s025:\n        global_delta: -0.062\n        low_delta: -0.015\n        mid_delta: -0.0096\n        high_delta: -0.0112\n      s030:\n        global_delta: -0.0732\n        low_delta: -0.0183\n        mid_delta: -0.0093\n        high_delta: -0.0138\n    key_finding: 'Both models: importance pruning low-phase Gini delta consistently\n      largest and monotonically increases with sparsity (DS: -0.016 to -0.037; QW:\n      -0.017 to -0.035). Random pruning shows weaker per-phase structure. Supports\n      discrimination collapse hypothesis.'\n- exp_id: c9_gsm8k_power_analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    min_detectable_d_n50: 0.4042\n    random_conditions_all_NS: true\n    random_max_abs_d: 0.164\n    random_conditions:\n      ds_rand_s015_d: -0.017\n      ds_rand_s015_power: 0.052\n      ds_rand_s020_d: -0.063\n      ds_rand_s020_power: 0.072\n      ds_rand_s025_d: 0.026\n      ds_rand_s025_power: 0.054\n      ds_rand_s030_d: 0.058\n      ds_rand_s030_power: 0.069\n      qw_rand_s015_d: -0.154\n      qw_rand_s015_power: 0.187\n      qw_rand_s020_d: 0.113\n      qw_rand_s020_power: 0.123\n      qw_rand_s025_d: 0.163\n      qw_rand_s025_power: 0.203\n      qw_rand_s030_d: 0.165\n      qw_rand_s030_power: 0.207\n    qw_importance_adequately_powered:\n      s025_d: 0.62\n      s025_power: 0.99\n      s030_d: 0.64\n      s030_power: 0.99\n    REVIEWER_WARNING: t-test Cohen's d power analysis ONLY valid for random conditions.\n      Importance conditions have heavy-tail distributions where t-test severely misestimates\n      (e.g. DS s030 d=0.008 but Wilcoxon p=0.0001). DO NOT cite importance t-test\n      power in paper.\n    paper_citable_conclusions:\n    - 'Random: all 8 conditions NS (max|d|=0.164), n=50 detects d>=0.40 → absence\n      of evidence not evidence of absence'\n    - QW importance s025/s030 adequately powered (d≈0.63, power>0.99)\n- exp_id: c10_lang_switching\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    method: CPU analysis of existing gen_snippet data (3/5 sparsities)\n    coverage: dense, s015, s030 (s020/s025 missing gen_snippet)\n    n_per_sparsity: 50\n    dense:\n      switch_rate: 0\n      cn_count: 0\n      en_count: 50\n      cn_acc: null\n      en_acc: 0.52\n    s015:\n      switch_rate: 0.04\n      cn_count: 2\n      en_count: 48\n      cn_acc: 0\n      en_acc: 0.375\n    s030:\n      switch_rate: 0.4\n      cn_count: 20\n      en_count: 30\n      cn_acc: 0.1\n      en_acc: 0.1\n    trend: 'Monotonically increasing: 0% → 4% → 40%. Chinese responses have much lower\n      accuracy (10% at s030 vs 52% dense English).'\n    checkpoint_path: /root/autodl-tmp/pacs/results_c10_lang_cpu.json\n- exp_id: c8_llama_n250_fixed\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: c10-lang-s020-s025\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: c10_lang_s020_s025\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    s020:\n      n: 50\n      accuracy: 0.26\n      switch_rate: 0.14\n      switch_count: 7\n      mean_cn_ratio: 0.066\n      cn_acc: 0.333\n      en_acc: 0.25\n    s025:\n      n: 50\n      accuracy: 0.1\n      switch_rate: 0.32\n      switch_count: 16\n      mean_cn_ratio: 0.152\n      cn_acc: 0.2\n      en_acc: 0.057\n    wall_time_s: 11680.6\n    output_path: /root/autodl-tmp/pacs/results_c10_lang_s020_s025.json\n- exp_id: c8_llama_gpu0_s025\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_problems: 250\n    n_bootstrap: 1000\n    segmentation: quantile\n    per_phase_ii_median:\n      high: 0.0171\n      mid: 0.1916\n      low: 0.388\n    per_phase_ii_mean:\n      high: 0.0218\n      mid: 0.2126\n      low: 0.4713\n    phase_gradient_median_diff: 0.3761\n    phase_gradient_median_diff_ci95:\n    - 0.3147\n    - 0.4039\n    wilcoxon_p_one_sided: 4.3e-39\n    bonferroni_p_k4: 1.72e-38\n    cohens_dz: 1.1174\n    rank_biserial_r: 0.8689\n    n_paired: 244\n    pos_neg_ratio: 228/16\n- exp_id: gpqa_ds_importance_s015\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-16T15:05:31.512Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T15:05:31.512Z",
  "sessionId": "8ea52053-5c5d-477c-85fd-15c4d095d3f8"
}
```

---

## Round 1

40 recorded events

### User

_source line 3 · 2026-05-16T15:05:31.546Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：LLaMA n=250 揭示 n=50 功效不足掩盖了中等 strategy×phase 交互；GPQA 确认跨 task 泛化且 strategy specificity 强。三维交互叙事完全成立。
核心假设：['LLaMA imp_vs_rand d_z 在 n=50 被噪声衰减；n=250 揭示真实中等效应（d_z≥0.4 at s030）', 'LLaMA random phase gradient 在 n=50 被过估；n=250 收缩至 d_z<0.25（小效应或 NS）', 'GPQA importance phase gradient Bonferroni 显著；imp/rand ratio ≥5×', 'C8 从 partially_confirmed 升级为 confirmed；strategy×phase 交互跨架构成立']
关键指标范围：{'llama_n250_imp_vs_rand_dz_s030': [0.45, 0.6], 'llama_n250_imp_vs_rand_dz_s025': [0.35, 0.5], 'llama_n250_bonferroni_sig_count_out_of_4': [3, 4], 'llama_n250_random_phase_gradient_dz': [0.1, 0.25], 'llama_n250_importance_phase_gradient_dz': [1.0, 1.2], 'gpqa_ds_s015_median_diff': [0.25, 0.5], 'gpqa_bonferroni_p': [1e-06, 0.01], 'gpqa_imp_rand_ratio': [5, 20]}
叙事方向：原始 framing "phase-gated compound sparsity" 完全成立。 Strategy × phase × compound 三维交互在三模型（DS/QW/LLaMA）、两架构（Qwen2/Llama）、 三 benchmark（MATH-500/GSM8K/GPQA）上一致复现。LLaMA n=250 高功效下 imp_vs_rand d_z 达中等效应量，random phase gradient 收缩至不显著或可忽略， 消除 n=50 的 architecture-dependent 限定。GPQA 提供第三 benchmark + 跨推理领域 （科学→数学）泛化。C8 升级为 confirmed，论文 claims 无需调整。 Title/framing 保持 "phase-gated"，EMNLP main 正会强竞争力—— novelty 同时具备现象发现（三维交互）和机制解释（discrimination collapse）， 泛化证据覆盖模型/架构/任务三个维度。


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
  "promptId": "6dc2d8ec-28c8-43cb-89c7-84c3b4e58d64",
  "type": "user",
  "uuid": "2d26248b-9346-4efb-a643-b47ed9b36d8d",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "8ea52053-5c5d-477c-85fd-15c4d095d3f8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T15:05:31.540Z_

```json
{
  "parentUuid": "2d26248b-9346-4efb-a643-b47ed9b36d8d",
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
  "uuid": "162c77e0-fe9a-475e-9b83-857dacc7a42e",
  "timestamp": "2026-05-16T15:05:31.540Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "8ea52053-5c5d-477c-85fd-15c4d095d3f8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T15:05:31.540Z_

```json
{
  "parentUuid": "162c77e0-fe9a-475e-9b83-857dacc7a42e",
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
  "uuid": "7341e352-f0fe-4e10-822d-4e37bb686a8c",
  "timestamp": "2026-05-16T15:05:31.540Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "8ea52053-5c5d-477c-85fd-15c4d095d3f8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-16T15:05:31.540Z_

```json
{
  "parentUuid": "7341e352-f0fe-4e10-822d-4e37bb686a8c",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "76482fae-daea-4b0b-bcad-3106cd36263d",
  "timestamp": "2026-05-16T15:05:31.540Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "8ea52053-5c5d-477c-85fd-15c4d095d3f8",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：LLaMA n=250 揭示 n=50 功效不足掩盖了中等 strategy×phase 交互；GPQA 确认跨 task 泛化且 strategy specificity 强。三维交互叙事完全成立。 核心假设：['LLaMA imp_vs_rand d_z 在 n=50 被噪声衰减；n=250 揭示真实中等…",
  "leafUuid": "76482fae-daea-4b0b-bcad-3106cd36263d",
  "sessionId": "8ea52053-5c5d-477c-85fd-15c4d095d3f8"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Phase-gated compound sparsity validation at scale",
  "sessionId": "8ea52053-5c5d-477c-85fd-15c4d095d3f8"
}
```

---

### Assistant

_source line 9 · 2026-05-16T15:06:41.282Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted data for each planned experiment in the experiment_plan, based on the "best" tier definition provided. Let me analyze what's needed:

The "best" tier means:
- LLaMA n=250 reveals that n=50 had insufficient power masking medium strategy×phase interaction
- GPQA confirms cross-task generalization with strong strategy specificity
- The three-dimensional interaction narrative fully holds

Core hypotheses:
1. LLaMA imp_vs_rand d_z at n=50 was noise-attenuated; n=250 reveals true medium effects (d_z≥0.4 at s030)


2. The random phase gradient effect at n=50 was inflated and should shrink below the small effect threshold when we scale to n=250
3. GPQA's importance phase gradient achieves Bonferroni significance with a strong importance-to-random ratio
4. The strategy×phase interaction upgrades to confirmed status across architectures

I'm now setting the expected value ranges for the key metrics, with LLaMA's n=250 importance versus random effect anchored between 0.45-0.6 for the s030 condition and 0.35-0.5 for s025, while tracking Bonferroni significance counts.

Looking at the experiment status, I see that most experiments are already complete, but there are two still running: the LLaMA n=250 fixed variant and the GPQA importance sampling experiment at s015, so I need to account for these ongoing runs when evaluating the current state of the results. I'm realizing the user wants me to generate predicted results for experiments in the plan based on the "best" tier scenario, but I need to clarify which experiments they're referring to—the ones marked DONE in the plan or the currently RUNNING ones in the registry like c8_llama_n250_fixed and gpqa_ds_importance_s015.

For the LLaMA n=250 replication to hit the "best" tier, I'd need to predict effect sizes around 0.45-0.6 for the main comparisons, with 3-4 out of 4 Bonferroni-significant results, and smaller effect sizes for the random phase gradient that shrink as sample size increases.

For GPQA, the cross-task importance experiment should show median differences between 0.25-0.5, strong statistical significance (p-values from 1e-6 to 0.01), and importance-to-random ratios in the 5-20× range.

The two actively running experiments are the full LLaMA n=250 replication and the GPQA DeepSeek importance experiment at s015, though there's also a partial result from the s025 importance condition that's already completed.

To properly assess the importance-to-random ratio for GPQA, I'll need to predict results for both the importance and random baseline conditions across different sparsities, then structure the output to show how these experiments fulfill the best-tier requirements. I see the distinction now—the experiment_plan lists completed experiments, but the RUNNING experiments in the registry are the new ones driving toward the best tier. I need to generate predictions for those active experiments: the full LLaMA n=250 replication and the GPQA importance profiling across different sparsity levels. Looking at the existing experimental data to calibrate my predictions—I can see the importance versus random ratios for LLaMA n=50 across different sparsity levels, and the phase gradient metrics show consistent patterns. The n=250 results at s025 align well with these trends, so I can use this as a baseline to extrapolate what the other sparsity levels should yield.

For the larger n=250 experiments, I'm expecting the importance-versus-random gap to widen further while the random gradient signal shrinks, keeping the importance gradient robust across the board. The GPQA and DeepSeek reference data suggest similar effect sizes should hold, so I need to map out which experiments are actually queued up and verify I have the right predictions in place. ~0.42 at s025 and ~0.32 at s020, with s015 dropping to ~0.25. I expect three of the four conditions to show Bonferroni significance, particularly at the higher sample sizes. The random phase gradient should shrink considerably to around 0.18, while the importance phase gradient climbs to roughly 1.1. For GPQA, the importance sampling shows a clear phase gradient effect with s015 median differences around 0.35 and very strong Bonferroni significance, giving an importance-to-random ratio of approximately 8×.

Now I'm thinking through which specific GPQA experiments would actually be needed to validate this—likely importance sampling runs at s015, s020, s025, and s030, paired with corresponding random baseline runs to compute the ratios. Let me map out the expected results for each condition.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76482fae-daea-4b0b-bcad-3106cd36263d",
  "isSidechain": false,
  "requestId": "req_011Cb6TJnjr8fz5ruDdzAcPy",
  "type": "assistant",
  "uuid": "097a615c-ce33-4131-ad5e-d51f1e9e018c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "8ea52053-5c5d-477c-85fd-15c4d095d3f8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017NVEnYcajxPWbA3kKTu4Je",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 57030,
      "cache_read_input_tokens": 11447,
      "output_tokens": 3538,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 57030,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3538,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 57030,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 57030
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

_source line 10 · 2026-05-16T15:06:41.405Z_

Looking at the registry, there are two RUNNING experiments that need predictions: `c8_llama_n250_fixed` and `gpqa_ds_importance_s015`. I'll also predict the implied GPQA random baseline needed to compute the imp/rand ratio.

Let me check the current state of these experiments for calibration.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "097a615c-ce33-4131-ad5e-d51f1e9e018c",
  "isSidechain": false,
  "requestId": "req_011Cb6TJnjr8fz5ruDdzAcPy",
  "type": "assistant",
  "uuid": "ae17f801-535d-493b-be8d-414ff889914d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "8ea52053-5c5d-477c-85fd-15c4d095d3f8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017NVEnYcajxPWbA3kKTu4Je",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 57030,
      "cache_read_input_tokens": 11447,
      "output_tokens": 3538,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 57030,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3538,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 57030,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 57030
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

_source line 11 · 2026-05-16T15:06:41.407Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01SsExYu1d4BBmeumpLTd1Hs`</summary>

```json
{
  "pattern": "c8_llama_n250|gpqa_ds",
  "glob": "*.yaml",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae17f801-535d-493b-be8d-414ff889914d",
  "isSidechain": false,
  "requestId": "req_011Cb6TJnjr8fz5ruDdzAcPy",
  "type": "assistant",
  "uuid": "837d5984-c49b-4750-8d46-c0baedb6ebbf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "8ea52053-5c5d-477c-85fd-15c4d095d3f8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017NVEnYcajxPWbA3kKTu4Je",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 57030,
      "cache_read_input_tokens": 11447,
      "output_tokens": 3538,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 57030,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3538,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 57030,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 57030
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

_source line 12 · 2026-05-16T15:06:41.431Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01U267Lgt5TjPmR6nX2HQYfX`</summary>

```json
{
  "pattern": "**/*experiment_plan*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "837d5984-c49b-4750-8d46-c0baedb6ebbf",
  "isSidechain": false,
  "requestId": "req_011Cb6TJnjr8fz5ruDdzAcPy",
  "type": "assistant",
  "uuid": "c2739139-aaaa-4dd9-95d9-b9de1882bfe2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "8ea52053-5c5d-477c-85fd-15c4d095d3f8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017NVEnYcajxPWbA3kKTu4Je",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 57030,
      "cache_read_input_tokens": 11447,
      "output_tokens": 3538,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 57030,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3538,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 57030,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 57030
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

_source line 13 · 2026-05-16T15:06:41.465Z_

<details><summary>↩ Tool result · `toolu_01SsExYu1d4BBmeumpLTd1Hs`</summary>

```text
Found 11 files
config/crons.yaml
projects/phase-gated-compound-sparse/registry.yaml
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/meta.yaml
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/worst/review_context.yaml
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/median/review_context.yaml
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/best/review_context.yaml
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/worst/imagined_experiments.yaml
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/median/imagined_experiments.yaml
projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/best/imagined_experiments.yaml
projects/phase-gated-compound-sparse/decisions.yaml
projects/phase-gated-compound-sparse/artifacts/review_issues.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "837d5984-c49b-4750-8d46-c0baedb6ebbf",
  "isSidechain": false,
  "promptId": "6dc2d8ec-28c8-43cb-89c7-84c3b4e58d64",
  "type": "user",
  "uuid": "67c04134-54c9-4bb6-b476-bfce6a516cf5",
  "toolUseResult": {
    "mode": "files_with_matches",
    "filenames": [
      "config/crons.yaml",
      "projects/phase-gated-compound-sparse/registry.yaml",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/meta.yaml",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/worst/review_context.yaml",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/median/review_context.yaml",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/best/review_context.yaml",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/worst/imagined_experiments.yaml",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/median/imagined_experiments.yaml",
      "projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/best/imagined_experiments.yaml",
      "projects/phase-gated-compound-sparse/decisions.yaml",
      "projects/phase-gated-compound-sparse/artifacts/review_issues.yaml"
    ],
    "numFiles": 11
  },
  "sourceToolAssistantUUID": "837d5984-c49b-4750-8d46-c0baedb6ebbf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "8ea52053-5c5d-477c-85fd-15c4d095d3f8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T15:06:41.470Z_

<details><summary>↩ Tool result · `toolu_01U267Lgt5TjPmR6nX2HQYfX`</summary>

```text
projects/redundancy-compound-sparsity/experiment_plan.yaml
projects/redundancy-compound-sparsity-2/experiment_plan.lock
projects/redundancy-compound-sparsity-2/experiment_plan.yaml
projects/phase-gated-compound-sparse/logs/workers/worker_knowledge_experiment_plan_yaml_20260516T002829.log
projects/phase-gated-compound-sparse/logs/workers/worker_knowledge_experiment_plan_yaml_20260516T002829_result.json
projects/phase-gated-compound-sparse/experiment_plan.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2739139-aaaa-4dd9-95d9-b9de1882bfe2",
  "isSidechain": false,
  "promptId": "6dc2d8ec-28c8-43cb-89c7-84c3b4e58d64",
  "type": "user",
  "uuid": "4d932f6d-e37e-4c1e-a570-7e255a3adb6a",
  "toolUseResult": {
    "filenames": [
      "projects/redundancy-compound-sparsity/experiment_plan.yaml",
      "projects/redundancy-compound-sparsity-2/experiment_plan.lock",
      "projects/redundancy-compound-sparsity-2/experiment_plan.yaml",
      "projects/phase-gated-compound-sparse/logs/workers/worker_knowledge_experiment_plan_yaml_20260516T002829.log",
      "projects/phase-gated-compound-sparse/logs/workers/worker_knowledge_experiment_plan_yaml_20260516T002829_result.json",
      "projects/phase-gated-compound-sparse/experiment_plan.yaml"
    ],
    "durationMs": 33,
    "numFiles": 6,
    "truncated": false
  },
  "sourceToolAssistantUUID": "c2739139-aaaa-4dd9-95d9-b9de1882bfe2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "8ea52053-5c5d-477c-85fd-15c4d095d3f8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T15:06:47.706Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RDvhqnBrvHzTMf2N4WRN8T`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/experiment_plan.yaml",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d932f6d-e37e-4c1e-a570-7e255a3adb6a",
  "isSidechain": false,
  "requestId": "req_011Cb6TPwcn5Bx6Y8xJjxMyF",
  "type": "assistant",
  "uuid": "437306d1-8a23-4f99-beb4-8ca1fa89e719",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "8ea52053-5c5d-477c-85fd-15c4d095d3f8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RLdFFzkiPJnYfkrsMaHQYa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4035,
      "cache_read_input_tokens": 68477,
      "output_tokens": 211,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4035,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 211,
          "cache_read_input_tokens": 68477,
          "cache_creation_input_tokens": 4035,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4035
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

_source line 16 · 2026-05-16T15:06:47.718Z_

<details><summary>↩ Tool result · `toolu_01RDvhqnBrvHzTMf2N4WRN8T`</summary>

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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "437306d1-8a23-4f99-beb4-8ca1fa89e719",
  "isSidechain": false,
  "promptId": "6dc2d8ec-28c8-43cb-89c7-84c3b4e58d64",
  "type": "user",
  "uuid": "42a0d6d1-8374-4d47-974e-d015b48d782b",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/experiment_plan.yaml",
      "content": "# experiment_plan.yaml — Retrospective experiment-to-claim mapping\n# Generated 2026-05-16 | project: phase-gated-compound-sparse\n# 38 experiments mapped across 13 claims\n\nexperiments:\n- id: c1_bf16_importance_s025\n  claim: C1\n  description: 'II median: high=0.032, mid=1.118, low=7.196; importance masking shows\n    strong phase gradient'\n  registry_id: bf16_importance_s025\n  role: primary\n  priority: high\n- id: c1_bf16_ds_rand_s025\n  claim: C1\n  description: 'Random II median: high=0.818, mid=0.932, low=1.363; flat gradient\n    vs importance'\n  registry_id: bf16_ds_rand_s025\n  role: primary\n  priority: high\n- id: c1_bf16_qw_imp_s025\n  claim: C1\n  description: 'Qwen cross-model: median_diff=1.109, Cohen''s d=1.233, p<1e-5'\n  registry_id: bf16_qw_imp_s025\n  role: supporting\n  priority: medium\n- id: c1_sf5_asymmetric_spot\n  claim: C1\n  description: 'Asymmetric configs: h02_kv03 D=19.13, h03_kv02 D=18.25; gradient consistent'\n  registry_id: sf5_asymmetric_spot\n  role: ablation\n  priority: medium\n- id: c1_c2_accuracy_eval\n  claim: C1\n  description: 'DS dense->s030 acc: 0.52->0.10 (-0.42); QW dense->s030: 0.32->0.14\n    (-0.18)'\n  registry_id: c2_accuracy_eval\n  role: supporting\n  priority: medium\n- id: c2_bf16_importance_s030\n  claim: C2\n  description: 'Phase gradient: II low=14.64 >> mid=2.28 >> high=0.053 (median); low/high\n    ratio ~276x'\n  registry_id: bf16_importance_s030\n  role: primary\n  priority: high\n- id: c2_v6_importance_s030\n  claim: C2\n  description: II low_median=34.69, mid_median=7.27, high_median=0.88; bootstrap_gradient=41.92,\n    CI=[19.14,299.76]\n  registry_id: v6_importance_s030\n  role: primary\n  priority: high\n- id: c2_think_phase_validation\n  claim: C2\n  description: Phase segmentation kappa=0.887; thinking=57.8% low-sparsity, answer=62.7%\n    high-sparsity\n  registry_id: think_phase_validation\n  role: supporting\n  priority: medium\n- id: c2_acc_qw_s030_n100\n  claim: C2\n  description: QW importance s030 accuracy=0.19 (n=100); dose-response monotonic decline\n    from dense=0.40\n  registry_id: acc_qw_s030_n100\n  role: supporting\n  priority: medium\n- id: c2_acc_ds_s015_8k_v2\n  claim: C2\n  description: DS s015 accuracy=0.48 vs dense=0.74; early onset of compound degradation\n  registry_id: acc_ds_s015_8k_v2\n  role: supporting\n  priority: medium\n- id: c3_v6_importance_s025\n  claim: C3\n  description: 'Importance: II low_median=24.16 >> high_median=0.66; strong phase\n    gradient (36x ratio)'\n  registry_id: v6_importance_s025\n  role: primary\n  priority: high\n- id: c3_v6_random_s025\n  claim: C3\n  description: 'Random: II low_median=2.91 ~ high_median=3.00; flat phase gradient\n    (bootstrap_p=0.559)'\n  registry_id: v6_random_s025\n  role: primary\n  priority: high\n- id: c3_bf16_importance_s020\n  claim: C3\n  description: 'Importance: II low=1.50, mid=0.20, high=0.015 (median); clear phase\n    separation'\n  registry_id: bf16_importance_s020\n  role: supporting\n  priority: medium\n- id: c3_bf16_ds_rand_s020\n  claim: C3\n  description: 'Random: II high=0.292, mid=0.350, low=0.276 (median); no phase separation'\n  registry_id: bf16_ds_rand_s020\n  role: supporting\n  priority: medium\n- id: c4_c4_entropy",
      "numLines": 100,
      "startLine": 1,
      "totalLines": 303
    }
  },
  "sourceToolAssistantUUID": "437306d1-8a23-4f99-beb4-8ca1fa89e719",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "8ea52053-5c5d-477c-85fd-15c4d095d3f8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T15:06:48.220Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QSM14EszVN4xxNSTQrPfXk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/best/imagined_experiments.yaml",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42a0d6d1-8374-4d47-974e-d015b48d782b",
  "isSidechain": false,
  "requestId": "req_011Cb6TPwcn5Bx6Y8xJjxMyF",
  "type": "assistant",
  "uuid": "073b3c2e-c408-4b12-99b4-052d0eb1f7c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "8ea52053-5c5d-477c-85fd-15c4d095d3f8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RLdFFzkiPJnYfkrsMaHQYa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4035,
      "cache_read_input_tokens": 68477,
      "output_tokens": 211,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4035,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 211,
          "cache_read_input_tokens": 68477,
          "cache_creation_input_tokens": 4035,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4035
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

_source line 18 · 2026-05-16T15:06:48.244Z_

<details><summary>↩ Tool result · `toolu_01QSM14EszVN4xxNSTQrPfXk`</summary>

```text
1	tier: best
2	narrative_guidance: '原始framing完全成立——compound sparsity severity是strategy×phase交互的涌现属性，
3	  跨三架构(DeepSeek-Qwen2/Qwen2/LLaMA)三benchmark(MATH-500/GSM8K/GPQA)复现。 Discrimination
4	  collapse是primary mechanism（Gini/CV跨模型定量预测interaction severity， per-phase Spearman
5	  ρ=1.0，Pearson r≥0.85）。Strategy specificity是稳健的general finding 而非architecture-dependent
6	  caveat——LLaMA n=250将imp_vs_rand d_z提升至medium effect（0.52）， 3个sparsity水平Bonferroni显著，同时random
7	  phase gradient从n=50的0.35-0.44衰减至0.15-0.22 （不再Bonferroni显著），解除C8的architecture-dependent限定。论文可以在Abstract/Intro
8	  直接声明''strategy×phase interaction generalizes across architectures and reasoning
9	  tasks''， 无需hedging。
10	
11	  '
12	imagined_experiments:
13	- name: LLaMA n=250 Cross-Architecture Full Validation
14	  plan_id: c8_llama_n250_fixed
15	  description: '在DeepSeek-R1-Distill-Llama-8B上扩展至n=250 problems（当前n=50）， 8个条件（importance/random
16	    × s015/s020/s025/s030）。 目标：(1) imp_vs_rand d_z达到medium effect（≥0.4）； (2) 2+个sparsity水平Bonferroni显著；
17	    (3) random phase gradient在n=250下减弱或不再显著。
18	
19	    '
20	  expected_results:
21	    model: DeepSeek-R1-Distill-Llama-8B
22	    n_problems: 250
23	    n_valid: 246
24	    n_skipped: 4
25	    conditions_completed: 8/8
26	    n_bootstrap: 10000
27	    bonferroni_k: 4
28	    imp_vs_rand_dz:
29	      s015: 0.24
30	      s020: 0.33
31	      s025: 0.43
32	      s030: 0.52
33	    imp_vs_rand_dz_ci:
34	      s015:
35	      - 0.07
36	      - 0.41
37	      s020:
38	      - 0.16
39	      - 0.5
40	      s025:
41	      - 0.26
42	      - 0.6
43	      s030:
44	      - 0.35
45	      - 0.69
46	    imp_vs_rand_dz_interpretation:
47	      s015: small
48	      s020: small
49	      s025: medium
50	      s030: medium
51	    imp_vs_rand_dz_monotonic: true
52	    phase_gradient_importance_dz:
53	      s015: 0.92
54	      s020: 1.01
55	      s025: 1.05
56	      s030: 0.97
57	    phase_gradient_importance_dz_ci:
58	      s015:
59	      - 0.72
60	      - 1.12
61	      s020:
62	      - 0.83
63	      - 1.19
64	      s025:
65	      - 0.88
66	      - 1.22
67	      s030:
68	      - 0.81
69	      - 1.13
70	    phase_gradient_importance_interpretation: all_large
71	    phase_gradient_random_dz:
72	      s015: 0.15
73	      s020: 0.18
74	      s025: 0.21
75	      s030: 0.22
76	    phase_gradient_random_dz_ci:
77	      s015:
78	      - -0.02
79	      - 0.32
80	      s020:
81	      - 0.01
82	      - 0.35
83	      s025:
84	      - 0.04
85	      - 0.38
86	      s030:
87	      - 0.05
88	      - 0.39
89	    phase_gradient_random_interpretation: negligible_to_small
90	    median_diff:
91	      s015: 0.025
92	      s020: 0.052
93	      s025: 0.148
94	      s030: 0.415
95	    median_diff_ci:
96	      s015:
97	      - 0.008
98	      - 0.045
99	      s020:
100	      - 0.012
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "073b3c2e-c408-4b12-99b4-052d0eb1f7c5",
  "isSidechain": false,
  "promptId": "6dc2d8ec-28c8-43cb-89c7-84c3b4e58d64",
  "type": "user",
  "uuid": "7885dce7-6e6d-4b8f-8d34-23c5849de70e",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/best/imagined_experiments.yaml",
      "content": "tier: best\nnarrative_guidance: '原始framing完全成立——compound sparsity severity是strategy×phase交互的涌现属性，\n  跨三架构(DeepSeek-Qwen2/Qwen2/LLaMA)三benchmark(MATH-500/GSM8K/GPQA)复现。 Discrimination\n  collapse是primary mechanism（Gini/CV跨模型定量预测interaction severity， per-phase Spearman\n  ρ=1.0，Pearson r≥0.85）。Strategy specificity是稳健的general finding 而非architecture-dependent\n  caveat——LLaMA n=250将imp_vs_rand d_z提升至medium effect（0.52）， 3个sparsity水平Bonferroni显著，同时random\n  phase gradient从n=50的0.35-0.44衰减至0.15-0.22 （不再Bonferroni显著），解除C8的architecture-dependent限定。论文可以在Abstract/Intro\n  直接声明''strategy×phase interaction generalizes across architectures and reasoning\n  tasks''， 无需hedging。\n\n  '\nimagined_experiments:\n- name: LLaMA n=250 Cross-Architecture Full Validation\n  plan_id: c8_llama_n250_fixed\n  description: '在DeepSeek-R1-Distill-Llama-8B上扩展至n=250 problems（当前n=50）， 8个条件（importance/random\n    × s015/s020/s025/s030）。 目标：(1) imp_vs_rand d_z达到medium effect（≥0.4）； (2) 2+个sparsity水平Bonferroni显著；\n    (3) random phase gradient在n=250下减弱或不再显著。\n\n    '\n  expected_results:\n    model: DeepSeek-R1-Distill-Llama-8B\n    n_problems: 250\n    n_valid: 246\n    n_skipped: 4\n    conditions_completed: 8/8\n    n_bootstrap: 10000\n    bonferroni_k: 4\n    imp_vs_rand_dz:\n      s015: 0.24\n      s020: 0.33\n      s025: 0.43\n      s030: 0.52\n    imp_vs_rand_dz_ci:\n      s015:\n      - 0.07\n      - 0.41\n      s020:\n      - 0.16\n      - 0.5\n      s025:\n      - 0.26\n      - 0.6\n      s030:\n      - 0.35\n      - 0.69\n    imp_vs_rand_dz_interpretation:\n      s015: small\n      s020: small\n      s025: medium\n      s030: medium\n    imp_vs_rand_dz_monotonic: true\n    phase_gradient_importance_dz:\n      s015: 0.92\n      s020: 1.01\n      s025: 1.05\n      s030: 0.97\n    phase_gradient_importance_dz_ci:\n      s015:\n      - 0.72\n      - 1.12\n      s020:\n      - 0.83\n      - 1.19\n      s025:\n      - 0.88\n      - 1.22\n      s030:\n      - 0.81\n      - 1.13\n    phase_gradient_importance_interpretation: all_large\n    phase_gradient_random_dz:\n      s015: 0.15\n      s020: 0.18\n      s025: 0.21\n      s030: 0.22\n    phase_gradient_random_dz_ci:\n      s015:\n      - -0.02\n      - 0.32\n      s020:\n      - 0.01\n      - 0.35\n      s025:\n      - 0.04\n      - 0.38\n      s030:\n      - 0.05\n      - 0.39\n    phase_gradient_random_interpretation: negligible_to_small\n    median_diff:\n      s015: 0.025\n      s020: 0.052\n      s025: 0.148\n      s030: 0.415\n    median_diff_ci:\n      s015:\n      - 0.008\n      - 0.045\n      s020:\n      - 0.012",
      "numLines": 100,
      "startLine": 1,
      "totalLines": 703
    }
  },
  "sourceToolAssistantUUID": "073b3c2e-c408-4b12-99b4-052d0eb1f7c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "8ea52053-5c5d-477c-85fd-15c4d095d3f8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 19 · 2026-05-16T15:06:48.317Z_

````json
{
  "parentUuid": "7885dce7-6e6d-4b8f-8d34-23c5849de70e",
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
  "uuid": "b7a2d0e8-46a2-4b9d-b213-bdbc0934dc28",
  "timestamp": "2026-05-16T15:06:48.317Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "8ea52053-5c5d-477c-85fd-15c4d095d3f8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：LLaMA n=250 揭示 n=50 功效不足掩盖了中等 strategy×phase 交互；GPQA 确认跨 task 泛化且 strategy specificity 强。三维交互叙事完全成立。 核心假设：['LLaMA imp_vs_rand d_z 在 n=50 被噪声衰减；n=250 揭示真实中等…",
  "leafUuid": "b7a2d0e8-46a2-4b9d-b213-bdbc0934dc28",
  "sessionId": "8ea52053-5c5d-477c-85fd-15c4d095d3f8"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Phase-gated compound sparsity validation at scale",
  "sessionId": "8ea52053-5c5d-477c-85fd-15c4d095d3f8"
}
```

---

### Tool call

_source line 22 · 2026-05-16T15:06:54.115Z_

<details open><summary>🔧 Tool call — Read · `toolu_0158VBMZcy2LtSCKHrVGoSa6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/best/imagined_experiments.yaml",
  "offset": 100,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7a2d0e8-46a2-4b9d-b213-bdbc0934dc28",
  "isSidechain": false,
  "requestId": "req_011Cb6TQSaKQBHK6iea1ZSjH",
  "type": "assistant",
  "uuid": "8f9e3211-11f8-4bc4-a9a6-db4a6612c767",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "8ea52053-5c5d-477c-85fd-15c4d095d3f8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017CwefMstW5rx698QkLKnFi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8013,
      "cache_read_input_tokens": 72512,
      "output_tokens": 140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8013,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 140,
          "cache_read_input_tokens": 72512,
          "cache_creation_input_tokens": 8013,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8013
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

_source line 23 · 2026-05-16T15:06:54.125Z_

<details><summary>↩ Tool result · `toolu_0158VBMZcy2LtSCKHrVGoSa6`</summary>

```text
100	      - 0.012
101	      - 0.108
102	      s025:
103	      - 0.055
104	      - 0.28
105	      s030:
106	      - 0.18
107	      - 0.62
108	    wilcoxon_p:
109	      s015: 0.018
110	      s020: 0.004
111	      s025: 0.00035
112	      s030: 1.8e-05
113	    wilcoxon_p_bonferroni:
114	      s015: 0.072
115	      s020: 0.016
116	      s025: 0.0014
117	      s030: 7.2e-05
118	    significant_bonferroni:
119	      s015: false
120	      s020: true
121	      s025: true
122	      s030: true
123	    bonferroni_significant_count: 3
124	    cross_arch_comparison:
125	      deepseek_qwen2_imp_vs_rand_dz_s030: 0.8
126	      llama_imp_vs_rand_dz_s030: 0.52
127	      delta: 0.28
128	      note: 'LLaMA effect weaker than Qwen2 architecture but now unambiguously medium
129	        (d_z=0.52, CI excludes zero). Architecture modulates magnitude but not direction
130	        — strategy×phase interaction is a general phenomenon.
131	
132	        '
133	  result_rationale: 'n=50时imp_vs_rand d_z=0.19→0.34，CI极宽（s030 CI=[0.06,0.66]），统计功效不足。
134	    n=250使SE缩小√5≈2.24倍，效应量估计趋于真值。 关键推理：(1) n=50时random phase gradient d_z=0.35-0.44可能被采样变异性膨胀——
135	    random masking本质是无差别噪声注入，不应产生与importance同等的strategy-dependent phase调制。在n=250下，采样噪声被平滑，random
136	    d_z回落至~0.15-0.22，不再Bonferroni显著。 这与DS/QW在低sparsity下random NS的模式一致——n=50时LLaMA
137	    random显著是Type I error 因小样本变异性所致。(2) importance的phase gradient在LLaMA上始终强烈（d_z≈1.0，
138	    源于LLaMA架构的attention head数量28/层 vs Qwen2的28/层但GQA结构不同）， n=250确认这不是偶然。(3) imp_vs_rand
139	    d_z在n=250下稳定至0.24→0.52， s020/s025/s030三个水平Bonferroni显著，因为真效应在这些水平上为medium（d_z≈0.35-0.55），
140	    n=250给出>90%的功效。
141	
142	    '
143	  tables:
144	  - name: 'Table: LLaMA n=250 vs n=50 Effect Size Comparison'
145	    columns:
146	    - sparsity
147	    - n50_dz
148	    - n250_dz
149	    - n250_bonf_p
150	    - n250_significant
151	    rows:
152	    - - s015
153	      - 0.19
154	      - 0.24
155	      - 0.072
156	      - NS
157	    - - s020
158	      - 0.26
159	      - 0.33
160	      - 0.016
161	      - ✓
162	    - - s025
163	      - 0.29
164	      - 0.43
165	      - 0.0014
166	      - ✓
167	    - - s030
168	      - 0.34
169	      - 0.52
170	      - 7.2e-05
171	      - ✓
172	  - name: 'Table: Random Phase Gradient Attenuation (n=50 → n=250)'
173	    columns:
174	    - sparsity
175	    - n50_random_dz
176	    - n250_random_dz
177	    - n250_random_CI_contains_zero
178	    rows:
179	    - - s015
180	      - 0.35
181	      - 0.15
182	      - 'yes'
183	    - - s020
184	      - 0.37
185	      - 0.18
186	      - borderline
187	    - - s025
188	      - 0.45
189	      - 0.21
190	      - no (but not Bonf)
191	    - - s030
192	      - 0.44
193	      - 0.22
194	      - no (but not Bonf)
195	  figures_description:
196	  - 'fig_c8_n250_dz_comparison.pdf: 左panel=imp_vs_rand d_z随sparsity变化（n=50虚线 vs n=250实线，含CI
197	    band），右panel=random phase gradient d_z的n=50→n=250衰减，灰色区域标注Bonferroni显著阈值'
198	  - 'fig_c8_cross_arch_forest.pdf: Forest plot展示三架构(DS/QW/LLaMA)在4个sparsity水平的imp_vs_rand
199	    d_z及95% CI'
200	  analysis: 'LLaMA n=250结果解除了C8的architecture-dependent限定。三个关键变化： (1) imp_vs_rand d_z从n=50的仅s030
201	    Bonferroni显著(p=0.029)提升至3个水平显著 (s020 p=0.016, s025 p=0.001, s030 p<0.001)； (2)
202	    s030 d_z=0.52（medium effect），在best范围[0.4,0.65]内； (3) random phase gradient从d_z=0.35-0.44衰减至0.15-0.22，无一Bonferroni显著——
203	    这与DS/QW模式一致，排除了"LLaMA上random也strategy-dependent"的alternative explanation。 论文可删除"suggests"/"provides
204	    partial support"措辞，改为 "Cross-architecture validation on LLaMA (n=250) confirms
205	    strategy×phase interaction with medium effect size (d_z=0.52 at s=0.30, Bonferroni
206	    p<0.001)"。 Limitation仅保留magnitude差异（LLaMA d_z=0.52 vs Qwen2 d_z=0.80）。
207	
208	    '
209	- name: GPQA DeepSeek Importance Phase Gradient Profiling
210	  plan_id: gpqa_profiling_ds
211	  description: '在DeepSeek-R1-Distill-Qwen-7B上对GPQA-Diamond子集(n=50)运行importance masking
212	    across 4 sparsity levels (s015/s020/s025/s030)，验证phase gradient单调递增。
213	
214	    '
215	  expected_results:
216	    model: DeepSeek-R1-Distill-Qwen-7B
217	    benchmark: GPQA-Diamond
218	    n_problems: 50
219	    method: median + Wilcoxon + bootstrap_median(B=10000)
220	    importance:
221	      s015:
222	        median_gradient: 0.185
223	        ci_low: 0.062
224	        ci_high: 0.385
225	        wilcoxon_p: 0.0008
226	      s020:
227	        median_gradient: 0.582
228	        ci_low: 0.241
229	        ci_high: 0.935
230	        wilcoxon_p: 0.0002
231	      s025:
232	        median_gradient: 1.748
233	        ci_low: 0.82
234	        ci_high: 2.51
235	        wilcoxon_p: 0.0001
236	      s030:
237	        median_gradient: 4.105
238	        ci_low: 1.89
239	        ci_high: 8.82
240	        wilcoxon_p: 0.0001
241	    dose_response_monotonic: true
242	    spearman_rho: 1.0
243	    cross_benchmark_comparison:
244	      math500_ds_gradient_s030: 8.48
245	      gsm8k_ds_gradient_s030: 4.682
246	      gpqa_ds_gradient_s030: 4.105
247	      note: GPQA gradient magnitude between MATH-500 and GSM8K
248	  result_rationale: 'GPQA-Diamond是graduate-level科学推理任务，难度高于MATH-500。预测phase gradient
249	    单调递增的理由：(1) GPQA的reasoning chain通常较长（涉及多步科学推理）， 大量token落入low-sparsity phase——head
250	    pruning在这些phase中导致importance score 的discrimination collapse更严重，compound interaction因此更大；
251	    (2) DS在MATH-500上gradient为0.39→8.48，GSM8K上为0.241→4.682——GPQA预计 在两者之间（~0.19→4.10），因为GPQA虽然难度高但问题更短（多选题format），
252	    reasoning chain长度介于MATH和GSM之间； (3) 单调性在三个benchmark上一致，因为phase gradient的物理机制（discrimination
253	    collapse 在late phase最严重→compound interaction在low-sparsity phase最大）不依赖于task类型。
254	
255	    '
256	  tables:
257	  - name: 'Table: Cross-Benchmark Phase Gradient Comparison (DeepSeek)'
258	    columns:
259	    - sparsity
260	    - MATH-500
261	    - GSM8K
262	    - GPQA
263	    rows:
264	    - - s015
265	      - 0.39
266	      - 0.241
267	      - 0.185
268	    - - s020
269	      - 1.21
270	      - 0.74
271	      - 0.582
272	    - - s025
273	      - 3.99
274	      - 1.992
275	      - 1.748
276	    - - s030
277	      - 8.48
278	      - 4.682
279	      - 4.105
280	  figures_description:
281	  - 'fig_cross_benchmark_gradient.pdf: 三条线(MATH/GSM/GPQA)展示DS importance phase gradient随sparsity的dose-response曲线，标注均为单调递增'
282	  analysis: 'GPQA上DS importance phase gradient 0.185→4.105单调递增，Spearman ρ=1.0， 复现了MATH-500和GSM8K上的核心发现。Gradient
283	    magnitude介于MATH-500(8.48) 和GSM8K(4.682)之间，反映GPQA推理链长度的中间特性。 三benchmark全部单调递增（cross_benchmark_phase_gradient_monotonic_count=3），
284	    确认phase modulation是跨task的robust finding。
285	
286	    '
287	- name: GPQA Qwen Importance Phase Gradient Profiling
288	  plan_id: gpqa_profiling_qw
289	  description: '在Qwen2.5-7B-Instruct上对GPQA-Diamond(n=50)运行importance masking across
290	    4 sparsity levels，验证cross-model replication。
291	
292	    '
293	  expected_results:
294	    model: Qwen2.5-7B-Instruct
295	    benchmark: GPQA-Diamond
296	    n_problems: 50
297	    importance:
298	      s015:
299	        median_gradient: 0.042
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f9e3211-11f8-4bc4-a9a6-db4a6612c767",
  "isSidechain": false,
  "promptId": "6dc2d8ec-28c8-43cb-89c7-84c3b4e58d64",
  "type": "user",
  "uuid": "4a38f90e-6a51-4a09-9404-433d1eb572a9",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/best/imagined_experiments.yaml",
      "content": "      - 0.012\n      - 0.108\n      s025:\n      - 0.055\n      - 0.28\n      s030:\n      - 0.18\n      - 0.62\n    wilcoxon_p:\n      s015: 0.018\n      s020: 0.004\n      s025: 0.00035\n      s030: 1.8e-05\n    wilcoxon_p_bonferroni:\n      s015: 0.072\n      s020: 0.016\n      s025: 0.0014\n      s030: 7.2e-05\n    significant_bonferroni:\n      s015: false\n      s020: true\n      s025: true\n      s030: true\n    bonferroni_significant_count: 3\n    cross_arch_comparison:\n      deepseek_qwen2_imp_vs_rand_dz_s030: 0.8\n      llama_imp_vs_rand_dz_s030: 0.52\n      delta: 0.28\n      note: 'LLaMA effect weaker than Qwen2 architecture but now unambiguously medium\n        (d_z=0.52, CI excludes zero). Architecture modulates magnitude but not direction\n        — strategy×phase interaction is a general phenomenon.\n\n        '\n  result_rationale: 'n=50时imp_vs_rand d_z=0.19→0.34，CI极宽（s030 CI=[0.06,0.66]），统计功效不足。\n    n=250使SE缩小√5≈2.24倍，效应量估计趋于真值。 关键推理：(1) n=50时random phase gradient d_z=0.35-0.44可能被采样变异性膨胀——\n    random masking本质是无差别噪声注入，不应产生与importance同等的strategy-dependent phase调制。在n=250下，采样噪声被平滑，random\n    d_z回落至~0.15-0.22，不再Bonferroni显著。 这与DS/QW在低sparsity下random NS的模式一致——n=50时LLaMA\n    random显著是Type I error 因小样本变异性所致。(2) importance的phase gradient在LLaMA上始终强烈（d_z≈1.0，\n    源于LLaMA架构的attention head数量28/层 vs Qwen2的28/层但GQA结构不同）， n=250确认这不是偶然。(3) imp_vs_rand\n    d_z在n=250下稳定至0.24→0.52， s020/s025/s030三个水平Bonferroni显著，因为真效应在这些水平上为medium（d_z≈0.35-0.55），\n    n=250给出>90%的功效。\n\n    '\n  tables:\n  - name: 'Table: LLaMA n=250 vs n=50 Effect Size Comparison'\n    columns:\n    - sparsity\n    - n50_dz\n    - n250_dz\n    - n250_bonf_p\n    - n250_significant\n    rows:\n    - - s015\n      - 0.19\n      - 0.24\n      - 0.072\n      - NS\n    - - s020\n      - 0.26\n      - 0.33\n      - 0.016\n      - ✓\n    - - s025\n      - 0.29\n      - 0.43\n      - 0.0014\n      - ✓\n    - - s030\n      - 0.34\n      - 0.52\n      - 7.2e-05\n      - ✓\n  - name: 'Table: Random Phase Gradient Attenuation (n=50 → n=250)'\n    columns:\n    - sparsity\n    - n50_random_dz\n    - n250_random_dz\n    - n250_random_CI_contains_zero\n    rows:\n    - - s015\n      - 0.35\n      - 0.15\n      - 'yes'\n    - - s020\n      - 0.37\n      - 0.18\n      - borderline\n    - - s025\n      - 0.45\n      - 0.21\n      - no (but not Bonf)\n    - - s030\n      - 0.44\n      - 0.22\n      - no (but not Bonf)\n  figures_description:\n  - 'fig_c8_n250_dz_comparison.pdf: 左panel=imp_vs_rand d_z随sparsity变化（n=50虚线 vs n=250实线，含CI\n    band），右panel=random phase gradient d_z的n=50→n=250衰减，灰色区域标注Bonferroni显著阈值'\n  - 'fig_c8_cross_arch_forest.pdf: Forest plot展示三架构(DS/QW/LLaMA)在4个sparsity水平的imp_vs_rand\n    d_z及95% CI'\n  analysis: 'LLaMA n=250结果解除了C8的architecture-dependent限定。三个关键变化： (1) imp_vs_rand d_z从n=50的仅s030\n    Bonferroni显著(p=0.029)提升至3个水平显著 (s020 p=0.016, s025 p=0.001, s030 p<0.001)； (2)\n    s030 d_z=0.52（medium effect），在best范围[0.4,0.65]内； (3) random phase gradient从d_z=0.35-0.44衰减至0.15-0.22，无一Bonferroni显著——\n    这与DS/QW模式一致，排除了\"LLaMA上random也strategy-dependent\"的alternative explanation。 论文可删除\"suggests\"/\"provides\n    partial support\"措辞，改为 \"Cross-architecture validation on LLaMA (n=250) confirms\n    strategy×phase interaction with medium effect size (d_z=0.52 at s=0.30, Bonferroni\n    p<0.001)\"。 Limitation仅保留magnitude差异（LLaMA d_z=0.52 vs Qwen2 d_z=0.80）。\n\n    '\n- name: GPQA DeepSeek Importance Phase Gradient Profiling\n  plan_id: gpqa_profiling_ds\n  description: '在DeepSeek-R1-Distill-Qwen-7B上对GPQA-Diamond子集(n=50)运行importance masking\n    across 4 sparsity levels (s015/s020/s025/s030)，验证phase gradient单调递增。\n\n    '\n  expected_results:\n    model: DeepSeek-R1-Distill-Qwen-7B\n    benchmark: GPQA-Diamond\n    n_problems: 50\n    method: median + Wilcoxon + bootstrap_median(B=10000)\n    importance:\n      s015:\n        median_gradient: 0.185\n        ci_low: 0.062\n        ci_high: 0.385\n        wilcoxon_p: 0.0008\n      s020:\n        median_gradient: 0.582\n        ci_low: 0.241\n        ci_high: 0.935\n        wilcoxon_p: 0.0002\n      s025:\n        median_gradient: 1.748\n        ci_low: 0.82\n        ci_high: 2.51\n        wilcoxon_p: 0.0001\n      s030:\n        median_gradient: 4.105\n        ci_low: 1.89\n        ci_high: 8.82\n        wilcoxon_p: 0.0001\n    dose_response_monotonic: true\n    spearman_rho: 1.0\n    cross_benchmark_comparison:\n      math500_ds_gradient_s030: 8.48\n      gsm8k_ds_gradient_s030: 4.682\n      gpqa_ds_gradient_s030: 4.105\n      note: GPQA gradient magnitude between MATH-500 and GSM8K\n  result_rationale: 'GPQA-Diamond是graduate-level科学推理任务，难度高于MATH-500。预测phase gradient\n    单调递增的理由：(1) GPQA的reasoning chain通常较长（涉及多步科学推理）， 大量token落入low-sparsity phase——head\n    pruning在这些phase中导致importance score 的discrimination collapse更严重，compound interaction因此更大；\n    (2) DS在MATH-500上gradient为0.39→8.48，GSM8K上为0.241→4.682——GPQA预计 在两者之间（~0.19→4.10），因为GPQA虽然难度高但问题更短（多选题format），\n    reasoning chain长度介于MATH和GSM之间； (3) 单调性在三个benchmark上一致，因为phase gradient的物理机制（discrimination\n    collapse 在late phase最严重→compound interaction在low-sparsity phase最大）不依赖于task类型。\n\n    '\n  tables:\n  - name: 'Table: Cross-Benchmark Phase Gradient Comparison (DeepSeek)'\n    columns:\n    - sparsity\n    - MATH-500\n    - GSM8K\n    - GPQA\n    rows:\n    - - s015\n      - 0.39\n      - 0.241\n      - 0.185\n    - - s020\n      - 1.21\n      - 0.74\n      - 0.582\n    - - s025\n      - 3.99\n      - 1.992\n      - 1.748\n    - - s030\n      - 8.48\n      - 4.682\n      - 4.105\n  figures_description:\n  - 'fig_cross_benchmark_gradient.pdf: 三条线(MATH/GSM/GPQA)展示DS importance phase gradient随sparsity的dose-response曲线，标注均为单调递增'\n  analysis: 'GPQA上DS importance phase gradient 0.185→4.105单调递增，Spearman ρ=1.0， 复现了MATH-500和GSM8K上的核心发现。Gradient\n    magnitude介于MATH-500(8.48) 和GSM8K(4.682)之间，反映GPQA推理链长度的中间特性。 三benchmark全部单调递增（cross_benchmark_phase_gradient_monotonic_count=3），\n    确认phase modulation是跨task的robust finding。\n\n    '\n- name: GPQA Qwen Importance Phase Gradient Profiling\n  plan_id: gpqa_profiling_qw\n  description: '在Qwen2.5-7B-Instruct上对GPQA-Diamond(n=50)运行importance masking across\n    4 sparsity levels，验证cross-model replication。\n\n    '\n  expected_results:\n    model: Qwen2.5-7B-Instruct\n    benchmark: GPQA-Diamond\n    n_problems: 50\n    importance:\n      s015:\n        median_gradient: 0.042",
      "numLines": 200,
      "startLine": 100,
      "totalLines": 703
    }
  },
  "sourceToolAssistantUUID": "8f9e3211-11f8-4bc4-a9a6-db4a6612c767",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "8ea52053-5c5d-477c-85fd-15c4d095d3f8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-16T15:06:57.599Z_

<details open><summary>🔧 Tool call — Read · `toolu_017yZPLNif6ioLvE7xNvb6Ni`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/best/imagined_experiments.yaml",
  "offset": 298,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a38f90e-6a51-4a09-9404-433d1eb572a9",
  "isSidechain": false,
  "requestId": "req_011Cb6TQsn8NiVgQgAoLfjRr",
  "type": "assistant",
  "uuid": "f25a4d65-847b-47f7-a298-566bdf246869",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "8ea52053-5c5d-477c-85fd-15c4d095d3f8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FNkWumBYFKMA9G7f6TrpuQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3489,
      "cache_read_input_tokens": 80525,
      "output_tokens": 140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3489,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 140,
          "cache_read_input_tokens": 80525,
          "cache_creation_input_tokens": 3489,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3489
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

_source line 25 · 2026-05-16T15:06:57.607Z_

<details><summary>↩ Tool result · `toolu_017yZPLNif6ioLvE7xNvb6Ni`</summary>

```text
298	      s015:
299	        median_gradient: 0.042
300	        ci_low: 0.008
301	        ci_high: 0.095
302	        wilcoxon_p: 0.015
303	      s020:
304	        median_gradient: 0.195
305	        ci_low: 0.078
306	        ci_high: 0.358
307	        wilcoxon_p: 0.0005
308	      s025:
309	        median_gradient: 0.882
310	        ci_low: 0.45
311	        ci_high: 1.32
312	        wilcoxon_p: 0.0001
313	      s030:
314	        median_gradient: 2.35
315	        ci_low: 1.28
316	        ci_high: 3.68
317	        wilcoxon_p: 0.0001
318	    dose_response_monotonic: true
319	    spearman_rho: 1.0
320	    qw_ds_gradient_ratio_s030: 0.57
321	    note: QW magnitude ~57% of DS, consistent with MATH-500 pattern (QW ~37% of DS)
322	  result_rationale: 'QW在MATH-500上gradient为0.066→3.155（DS的~37%），在GSM8K上为0.039→2.092。
323	    GPQA预测QW gradient 0.042→2.350，DS比QW比值约1.75×，略低于MATH-500的2.7×但 高于GSM8K的2.2×。QW
324	    magnitude一贯小于DS（可能因Qwen2.5-7B-Instruct的 attention head utilization更均匀，pruning影响较分散），但方向和单调性完全一致。
325	    Onset threshold仍在s020+——s015 gradient仅0.042但CI不跨零（GPQA难度使得即使 低sparsity也有可检测的compound
326	    effect）。
327	
328	    '
329	  tables:
330	  - name: 'Table: Cross-Benchmark Phase Gradient Comparison (Qwen)'
331	    columns:
332	    - sparsity
333	    - MATH-500
334	    - GSM8K
335	    - GPQA
336	    rows:
337	    - - s015
338	      - 0.066
339	      - 0.039
340	      - 0.042
341	    - - s020
342	      - 0.307
343	      - 0.158
344	      - 0.195
345	    - - s025
346	      - 1.075
347	      - 1.1
348	      - 0.882
349	    - - s030
350	      - 3.155
351	      - 2.092
352	      - 2.35
353	  figures_description:
354	  - 'fig_qw_cross_benchmark.pdf: 与DS对应的QW三benchmark gradient曲线'
355	  analysis: 'QW在GPQA上完美复现单调递增模式。结合DS，两模型×三benchmark共6个 dose-response曲线全部单调（Spearman
356	    ρ=1.0）。QW-GPQA的gradient magnitude 与QW-GSM8K接近（s030: 2.35 vs 2.09），暗示QW在不同推理任务上的compound
357	    sensitivity较为稳定，而DS variation更大（MATH=8.48, GSM=4.68, GPQA=4.10）。
358	
359	    '
360	- name: GPQA Random Baselines and Strategy Specificity Ratio
361	  plan_id: gpqa_random_baselines
362	  description: '在GPQA-Diamond(n=50)上对DS和QW运行random masking across 4 sparsity levels，
363	    计算strategy specificity ratio (importance/random gradient)，验证≥5×。
364	
365	    '
366	  expected_results:
367	    ds_random:
368	      s015:
369	        median_gradient: 0.022
370	      s020:
371	        median_gradient: 0.068
372	      s025:
373	        median_gradient: 0.232
374	      s030:
375	        median_gradient: 0.548
376	    qw_random:
377	      s015:
378	        median_gradient: 0.006
379	      s020:
380	        median_gradient: 0.028
381	      s025:
382	        median_gradient: 0.125
383	      s030:
384	        median_gradient: 0.38
385	    strategy_specificity_ratio_ds:
386	      s015: 8.4
387	      s020: 8.6
388	      s025: 7.5
389	      s030: 7.5
390	    strategy_specificity_ratio_qw:
391	      s015: 7.0
392	      s020: 7.0
393	      s025: 7.1
394	      s030: 6.2
395	    strategy_specificity_ratio_range: 6.2-8.6×
396	    all_ratios_above_5x: true
397	    cross_benchmark_specificity_comparison:
398	      math500: 15-36×
399	      gsm8k: 2.3-3.8×
400	      gpqa: 6.2-8.6×
401	  result_rationale: 'Strategy specificity ratio的task-dependence与reasoning chain结构相关：
402	    (1) MATH-500推理链最长最复杂（竞赛数学），importance score的phase-dependent discrimination collapse最剧烈→ratio最高（15-36×）；
403	    (2) GSM8K推理链最短最规律（小学数学），importance和random的差异被压缩→ratio 最低（2.3-3.8×）； (3) GPQA居中（graduate
404	    QA，推理步骤中等长度），ratio 6.2-8.6×。 所有GPQA ratio≥5×，满足best tier阈值。物理解释：GPQA的scientific
405	    reasoning 涉及领域知识检索和逻辑链推理，importance score对这些pattern的编码比 random有明显优势，但不如MATH-500中复杂数学推理的优势大。
406	    random baseline在GPQA上仍产生可测量的compound effect（特别是s025+）， 但magnitude远小于importance——与DS/QW在MATH-500上的模式定性一致。
407	
408	    '
409	  tables:
410	  - name: 'Table: Strategy Specificity Ratio Across Benchmarks'
411	    columns:
412	    - benchmark
413	    - ratio_range
414	    - interpretation
415	    rows:
416	    - - MATH-500
417	      - 15-36×
418	      - very_high
419	    - - GPQA
420	      - 6.2-8.6×
421	      - high
422	    - - GSM8K
423	      - 2.3-3.8×
424	      - moderate
425	  figures_description:
426	  - 'fig_specificity_heatmap.pdf: 3×4 heatmap (benchmark × sparsity) 展示strategy specificity
427	    ratio，颜色从蓝(2×)到红(36×)，标注5×阈值线'
428	  - 'fig_gpqa_imp_vs_rand.pdf: GPQA上importance vs random gradient的双线图（DS和QW各一个panel），阴影区域表示两者差距'
429	  analysis: 'GPQA strategy specificity ratio 6.2-8.6×，全部超过5×阈值。 与MATH-500(15-36×)和GSM8K(2.3-3.8×)形成interpretable
430	    gradient： 推理链复杂度↑ → specificity ratio↑。这支持"discrimination collapse是 mechanism、而非importance
431	    metric本身有缺陷"的framing——如果是metric缺陷， ratio不应随task difficulty系统性变化。Strategy specificity的task-dependence
432	    机制现在有了三点数据（从moderate到very_high），可以在Discussion中 提出"推理链复杂度调制specificity"的初步假说。
433	
434	    '
435	- name: Discrimination Collapse Quantitative Correlation Analysis
436	  plan_id: mechanism_gini_correlation
437	  description: '利用已完成的c5_per_phase_gini和c2_n500数据，计算per-phase Gini_delta 与interaction
438	    severity（II median）的跨模型定量相关，验证r≥0.7。
439	
440	    '
441	  expected_results:
442	    analysis_type: correlation of per-phase Gini collapse magnitude with II severity
443	    data_source: c5_per_phase_gini (n=30 per model) + c2_n500 (n=500 per model)
444	    ds_within_model:
445	      gini_delta_low_phase:
446	      - -0.0163
447	      - -0.0209
448	      - -0.0313
449	      - -0.0373
450	      ii_median:
451	      - 0.3907
452	      - 1.2149
453	      - 3.9857
454	      - 8.4813
455	      spearman_rho: 1.0
456	      pearson_r: 0.93
457	      pearson_p: 0.035
458	    qw_within_model:
459	      gini_delta_low_phase:
460	      - -0.0165
461	      - -0.02
462	      - -0.0286
463	      - -0.035
464	      ii_median:
465	      - 0.0659
466	      - 0.3073
467	      - 1.0745
468	      - 3.155
469	      spearman_rho: 1.0
470	      pearson_r: 0.95
471	      pearson_p: 0.025
472	    cross_model_pooled:
473	      n_datapoints: 8
474	      spearman_rho: 0.88
475	      pearson_r: 0.85
476	      pearson_p: 0.004
477	    cv_correlation:
478	      ds_cv_delta_vs_ii_spearman: 1.0
479	      qw_cv_delta_vs_ii_spearman: 1.0
480	      cross_model_cv_pearson_r: 0.87
481	    llama_validation:
482	      note: 'LLaMA c8_llama_n250 data可进一步验证——如果LLaMA per-phase Gini也 与II monotonically相关，则三模型cross-model
483	        r预计提升至0.88+
484	
485	        '
486	      llama_predicted_gini_delta_low_phase:
487	      - -0.012
488	      - -0.016
489	      - -0.022
490	      - -0.028
491	      llama_predicted_ii_from_n250:
492	      - 0.025
493	      - 0.052
494	      - 0.148
495	      - 0.415
496	      llama_predicted_within_r: 0.91
497	  result_rationale: 'Gini delta和II的相关性有坚实的机制基础：head pruning → 剩余head的importance score分布变得更均匀（Gini下降）→
498	    importance-based eviction丧失判别力 → eviction近似随机 → compound interaction增大。因此Gini下降幅度应与II
499	    severity 正相关。具体地： (1) DS low-phase Gini delta [-0.016→-0.037] 与 II [0.39→8.48]
500	    完美单调共变 （Spearman ρ=1.0），Pearson r=0.93源于两者均近似幂律增长但指数不同； (2) QW同样单调（Gini [-0.017→-0.035]，II
501	    [0.066→3.155]），Pearson r略高(0.95) 因为QW的II增长更接近线性（log-scale上更平缓）； (3) 跨模型pooling(8点)r=0.85，因为DS和QW的Gini-magnitude关系有共同的正趋势
502	    但斜率不同（DS单位Gini下降对应更大的II增加），这正好反映两模型architecture 差异——Gini→II的传递函数是architecture-dependent的，但方向和monotonicity
503	    是universal的。 所有r>0.7，满足best tier要求。CV delta提供一致的supporting evidence。
504	
505	    '
506	  tables:
507	  - name: 'Table: Gini-II Correlation Summary'
508	    columns:
509	    - scope
510	    - Spearman ρ
511	    - Pearson r
512	    - p-value
513	    - interpretation
514	    rows:
515	    - - DS within-model
516	      - 1.0
517	      - 0.93
518	      - 0.035
519	      - strong monotonic
520	    - - QW within-model
521	      - 1.0
522	      - 0.95
523	      - 0.025
524	      - strong monotonic
525	    - - Cross-model pooled
526	      - 0.88
527	      - 0.85
528	      - 0.004
529	      - robust cross-model
530	  - name: 'Table: Per-Phase Gini Delta vs II Median (Low-Phase)'
531	    columns:
532	    - model
533	    - sparsity
534	    - gini_delta
535	    - ii_median
536	    rows:
537	    - - DS
538	      - s015
539	      - -0.0163
540	      - 0.3907
541	    - - DS
542	      - s020
543	      - -0.0209
544	      - 1.2149
545	    - - DS
546	      - s025
547	      - -0.0313
548	      - 3.9857
549	    - - DS
550	      - s030
551	      - -0.0373
552	      - 8.4813
553	    - - QW
554	      - s015
555	      - -0.0165
556	      - 0.0659
557	    - - QW
558	      - s020
559	      - -0.02
560	      - 0.3073
561	    - - QW
562	      - s025
563	      - -0.0286
564	      - 1.0745
565	    - - QW
566	      - s030
567	      - -0.035
568	      - 3.155
569	  figures_description:
570	  - 'fig_gini_ii_scatter.pdf: 散点图展示|Gini_delta|(x轴) vs II_median(y轴,log scale)，DS圆点QW方块，按sparsity着色（浅→深），回归线及r²标注'
571	  - 'fig_mechanism_schematic.pdf: 因果链示意图：head pruning → Gini↓ → discrimination collapse
572	    → compound II↑，箭头上标注cross-model r值'
573	  analysis: 'Per-phase Gini delta与II severity的定量相关是discrimination collapse假说的 最终实证验证。DS和QW各4个sparsity水平给出8个数据点，跨模型Pearson
574	    r=0.85, Spearman ρ=0.88，远超r≥0.7阈值。更重要的是： (1) 两模型within-model ρ均为1.0（完美单调），排除了"Gini下降但II不增加"
575	    或"II增加但Gini不下降"的反例； (2) Pearson r<1.0源于非线性关系（II随Gini近似幂律增长），这恰好与 discrimination
576	    collapse机制的非线性传递函数一致——Gini小幅下降在接近 临界阈值时引发不成比例的判别力崩塌； (3) CV delta给出一致结果（r=0.87），提供converging
577	    evidence。 论文§5 Mechanism可以声明"Gini decline quantitatively predicts interaction
578	    severity (cross-model r=0.85, p=0.004)"。
579	
580	    '
581	- name: Language Switching at Intermediate Sparsities (s020/s025)
582	  plan_id: c10_lang_s020_s025
583	  description: '填补s020和s025的language switching rate数据（当前已有dense=0%, s015=4%, s030=40%），确认monotonic
584	    dose-response。
585	
586	    '
587	  expected_results:
588	    method: CPU analysis of gen_snippet data
589	    n_per_sparsity: 50
590	    s020:
591	      switch_rate: 0.12
592	      cn_count: 6
593	      en_count: 44
594	      cn_acc: 0.0
595	      en_acc: 0.3
596	    s025:
597	      switch_rate: 0.26
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f25a4d65-847b-47f7-a298-566bdf246869",
  "isSidechain": false,
  "promptId": "6dc2d8ec-28c8-43cb-89c7-84c3b4e58d64",
  "type": "user",
  "uuid": "e16d1b77-5c1e-4772-92c2-25ea8e4452e1",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/best/imagined_experiments.yaml",
      "content": "      s015:\n        median_gradient: 0.042\n        ci_low: 0.008\n        ci_high: 0.095\n        wilcoxon_p: 0.015\n      s020:\n        median_gradient: 0.195\n        ci_low: 0.078\n        ci_high: 0.358\n        wilcoxon_p: 0.0005\n      s025:\n        median_gradient: 0.882\n        ci_low: 0.45\n        ci_high: 1.32\n        wilcoxon_p: 0.0001\n      s030:\n        median_gradient: 2.35\n        ci_low: 1.28\n        ci_high: 3.68\n        wilcoxon_p: 0.0001\n    dose_response_monotonic: true\n    spearman_rho: 1.0\n    qw_ds_gradient_ratio_s030: 0.57\n    note: QW magnitude ~57% of DS, consistent with MATH-500 pattern (QW ~37% of DS)\n  result_rationale: 'QW在MATH-500上gradient为0.066→3.155（DS的~37%），在GSM8K上为0.039→2.092。\n    GPQA预测QW gradient 0.042→2.350，DS比QW比值约1.75×，略低于MATH-500的2.7×但 高于GSM8K的2.2×。QW\n    magnitude一贯小于DS（可能因Qwen2.5-7B-Instruct的 attention head utilization更均匀，pruning影响较分散），但方向和单调性完全一致。\n    Onset threshold仍在s020+——s015 gradient仅0.042但CI不跨零（GPQA难度使得即使 低sparsity也有可检测的compound\n    effect）。\n\n    '\n  tables:\n  - name: 'Table: Cross-Benchmark Phase Gradient Comparison (Qwen)'\n    columns:\n    - sparsity\n    - MATH-500\n    - GSM8K\n    - GPQA\n    rows:\n    - - s015\n      - 0.066\n      - 0.039\n      - 0.042\n    - - s020\n      - 0.307\n      - 0.158\n      - 0.195\n    - - s025\n      - 1.075\n      - 1.1\n      - 0.882\n    - - s030\n      - 3.155\n      - 2.092\n      - 2.35\n  figures_description:\n  - 'fig_qw_cross_benchmark.pdf: 与DS对应的QW三benchmark gradient曲线'\n  analysis: 'QW在GPQA上完美复现单调递增模式。结合DS，两模型×三benchmark共6个 dose-response曲线全部单调（Spearman\n    ρ=1.0）。QW-GPQA的gradient magnitude 与QW-GSM8K接近（s030: 2.35 vs 2.09），暗示QW在不同推理任务上的compound\n    sensitivity较为稳定，而DS variation更大（MATH=8.48, GSM=4.68, GPQA=4.10）。\n\n    '\n- name: GPQA Random Baselines and Strategy Specificity Ratio\n  plan_id: gpqa_random_baselines\n  description: '在GPQA-Diamond(n=50)上对DS和QW运行random masking across 4 sparsity levels，\n    计算strategy specificity ratio (importance/random gradient)，验证≥5×。\n\n    '\n  expected_results:\n    ds_random:\n      s015:\n        median_gradient: 0.022\n      s020:\n        median_gradient: 0.068\n      s025:\n        median_gradient: 0.232\n      s030:\n        median_gradient: 0.548\n    qw_random:\n      s015:\n        median_gradient: 0.006\n      s020:\n        median_gradient: 0.028\n      s025:\n        median_gradient: 0.125\n      s030:\n        median_gradient: 0.38\n    strategy_specificity_ratio_ds:\n      s015: 8.4\n      s020: 8.6\n      s025: 7.5\n      s030: 7.5\n    strategy_specificity_ratio_qw:\n      s015: 7.0\n      s020: 7.0\n      s025: 7.1\n      s030: 6.2\n    strategy_specificity_ratio_range: 6.2-8.6×\n    all_ratios_above_5x: true\n    cross_benchmark_specificity_comparison:\n      math500: 15-36×\n      gsm8k: 2.3-3.8×\n      gpqa: 6.2-8.6×\n  result_rationale: 'Strategy specificity ratio的task-dependence与reasoning chain结构相关：\n    (1) MATH-500推理链最长最复杂（竞赛数学），importance score的phase-dependent discrimination collapse最剧烈→ratio最高（15-36×）；\n    (2) GSM8K推理链最短最规律（小学数学），importance和random的差异被压缩→ratio 最低（2.3-3.8×）； (3) GPQA居中（graduate\n    QA，推理步骤中等长度），ratio 6.2-8.6×。 所有GPQA ratio≥5×，满足best tier阈值。物理解释：GPQA的scientific\n    reasoning 涉及领域知识检索和逻辑链推理，importance score对这些pattern的编码比 random有明显优势，但不如MATH-500中复杂数学推理的优势大。\n    random baseline在GPQA上仍产生可测量的compound effect（特别是s025+）， 但magnitude远小于importance——与DS/QW在MATH-500上的模式定性一致。\n\n    '\n  tables:\n  - name: 'Table: Strategy Specificity Ratio Across Benchmarks'\n    columns:\n    - benchmark\n    - ratio_range\n    - interpretation\n    rows:\n    - - MATH-500\n      - 15-36×\n      - very_high\n    - - GPQA\n      - 6.2-8.6×\n      - high\n    - - GSM8K\n      - 2.3-3.8×\n      - moderate\n  figures_description:\n  - 'fig_specificity_heatmap.pdf: 3×4 heatmap (benchmark × sparsity) 展示strategy specificity\n    ratio，颜色从蓝(2×)到红(36×)，标注5×阈值线'\n  - 'fig_gpqa_imp_vs_rand.pdf: GPQA上importance vs random gradient的双线图（DS和QW各一个panel），阴影区域表示两者差距'\n  analysis: 'GPQA strategy specificity ratio 6.2-8.6×，全部超过5×阈值。 与MATH-500(15-36×)和GSM8K(2.3-3.8×)形成interpretable\n    gradient： 推理链复杂度↑ → specificity ratio↑。这支持\"discrimination collapse是 mechanism、而非importance\n    metric本身有缺陷\"的framing——如果是metric缺陷， ratio不应随task difficulty系统性变化。Strategy specificity的task-dependence\n    机制现在有了三点数据（从moderate到very_high），可以在Discussion中 提出\"推理链复杂度调制specificity\"的初步假说。\n\n    '\n- name: Discrimination Collapse Quantitative Correlation Analysis\n  plan_id: mechanism_gini_correlation\n  description: '利用已完成的c5_per_phase_gini和c2_n500数据，计算per-phase Gini_delta 与interaction\n    severity（II median）的跨模型定量相关，验证r≥0.7。\n\n    '\n  expected_results:\n    analysis_type: correlation of per-phase Gini collapse magnitude with II severity\n    data_source: c5_per_phase_gini (n=30 per model) + c2_n500 (n=500 per model)\n    ds_within_model:\n      gini_delta_low_phase:\n      - -0.0163\n      - -0.0209\n      - -0.0313\n      - -0.0373\n      ii_median:\n      - 0.3907\n      - 1.2149\n      - 3.9857\n      - 8.4813\n      spearman_rho: 1.0\n      pearson_r: 0.93\n      pearson_p: 0.035\n    qw_within_model:\n      gini_delta_low_phase:\n      - -0.0165\n      - -0.02\n      - -0.0286\n      - -0.035\n      ii_median:\n      - 0.0659\n      - 0.3073\n      - 1.0745\n      - 3.155\n      spearman_rho: 1.0\n      pearson_r: 0.95\n      pearson_p: 0.025\n    cross_model_pooled:\n      n_datapoints: 8\n      spearman_rho: 0.88\n      pearson_r: 0.85\n      pearson_p: 0.004\n    cv_correlation:\n      ds_cv_delta_vs_ii_spearman: 1.0\n      qw_cv_delta_vs_ii_spearman: 1.0\n      cross_model_cv_pearson_r: 0.87\n    llama_validation:\n      note: 'LLaMA c8_llama_n250 data可进一步验证——如果LLaMA per-phase Gini也 与II monotonically相关，则三模型cross-model\n        r预计提升至0.88+\n\n        '\n      llama_predicted_gini_delta_low_phase:\n      - -0.012\n      - -0.016\n      - -0.022\n      - -0.028\n      llama_predicted_ii_from_n250:\n      - 0.025\n      - 0.052\n      - 0.148\n      - 0.415\n      llama_predicted_within_r: 0.91\n  result_rationale: 'Gini delta和II的相关性有坚实的机制基础：head pruning → 剩余head的importance score分布变得更均匀（Gini下降）→\n    importance-based eviction丧失判别力 → eviction近似随机 → compound interaction增大。因此Gini下降幅度应与II\n    severity 正相关。具体地： (1) DS low-phase Gini delta [-0.016→-0.037] 与 II [0.39→8.48]\n    完美单调共变 （Spearman ρ=1.0），Pearson r=0.93源于两者均近似幂律增长但指数不同； (2) QW同样单调（Gini [-0.017→-0.035]，II\n    [0.066→3.155]），Pearson r略高(0.95) 因为QW的II增长更接近线性（log-scale上更平缓）； (3) 跨模型pooling(8点)r=0.85，因为DS和QW的Gini-magnitude关系有共同的正趋势\n    但斜率不同（DS单位Gini下降对应更大的II增加），这正好反映两模型architecture 差异——Gini→II的传递函数是architecture-dependent的，但方向和monotonicity\n    是universal的。 所有r>0.7，满足best tier要求。CV delta提供一致的supporting evidence。\n\n    '\n  tables:\n  - name: 'Table: Gini-II Correlation Summary'\n    columns:\n    - scope\n    - Spearman ρ\n    - Pearson r\n    - p-value\n    - interpretation\n    rows:\n    - - DS within-model\n      - 1.0\n      - 0.93\n      - 0.035\n      - strong monotonic\n    - - QW within-model\n      - 1.0\n      - 0.95\n      - 0.025\n      - strong monotonic\n    - - Cross-model pooled\n      - 0.88\n      - 0.85\n      - 0.004\n      - robust cross-model\n  - name: 'Table: Per-Phase Gini Delta vs II Median (Low-Phase)'\n    columns:\n    - model\n    - sparsity\n    - gini_delta\n    - ii_median\n    rows:\n    - - DS\n      - s015\n      - -0.0163\n      - 0.3907\n    - - DS\n      - s020\n      - -0.0209\n      - 1.2149\n    - - DS\n      - s025\n      - -0.0313\n      - 3.9857\n    - - DS\n      - s030\n      - -0.0373\n      - 8.4813\n    - - QW\n      - s015\n      - -0.0165\n      - 0.0659\n    - - QW\n      - s020\n      - -0.02\n      - 0.3073\n    - - QW\n      - s025\n      - -0.0286\n      - 1.0745\n    - - QW\n      - s030\n      - -0.035\n      - 3.155\n  figures_description:\n  - 'fig_gini_ii_scatter.pdf: 散点图展示|Gini_delta|(x轴) vs II_median(y轴,log scale)，DS圆点QW方块，按sparsity着色（浅→深），回归线及r²标注'\n  - 'fig_mechanism_schematic.pdf: 因果链示意图：head pruning → Gini↓ → discrimination collapse\n    → compound II↑，箭头上标注cross-model r值'\n  analysis: 'Per-phase Gini delta与II severity的定量相关是discrimination collapse假说的 最终实证验证。DS和QW各4个sparsity水平给出8个数据点，跨模型Pearson\n    r=0.85, Spearman ρ=0.88，远超r≥0.7阈值。更重要的是： (1) 两模型within-model ρ均为1.0（完美单调），排除了\"Gini下降但II不增加\"\n    或\"II增加但Gini不下降\"的反例； (2) Pearson r<1.0源于非线性关系（II随Gini近似幂律增长），这恰好与 discrimination\n    collapse机制的非线性传递函数一致——Gini小幅下降在接近 临界阈值时引发不成比例的判别力崩塌； (3) CV delta给出一致结果（r=0.87），提供converging\n    evidence。 论文§5 Mechanism可以声明\"Gini decline quantitatively predicts interaction\n    severity (cross-model r=0.85, p=0.004)\"。\n\n    '\n- name: Language Switching at Intermediate Sparsities (s020/s025)\n  plan_id: c10_lang_s020_s025\n  description: '填补s020和s025的language switching rate数据（当前已有dense=0%, s015=4%, s030=40%），确认monotonic\n    dose-response。\n\n    '\n  expected_results:\n    method: CPU analysis of gen_snippet data\n    n_per_sparsity: 50\n    s020:\n      switch_rate: 0.12\n      cn_count: 6\n      en_count: 44\n      cn_acc: 0.0\n      en_acc: 0.3\n    s025:\n      switch_rate: 0.26",
      "numLines": 300,
      "startLine": 298,
      "totalLines": 703
    }
  },
  "sourceToolAssistantUUID": "f25a4d65-847b-47f7-a298-566bdf246869",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "8ea52053-5c5d-477c-85fd-15c4d095d3f8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：LLaMA n=250 揭示 n=50 功效不足掩盖了中等 strategy×phase 交互；GPQA 确认跨 task 泛化且 strategy specificity 强。三维交互叙事完全成立。 核心假设：['LLaMA imp_vs_rand d_z 在 n=50 被噪声衰减；n=250 揭示真实中等…",
  "leafUuid": "e16d1b77-5c1e-4772-92c2-25ea8e4452e1",
  "sessionId": "8ea52053-5c5d-477c-85fd-15c4d095d3f8"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Phase-gated compound sparsity validation at scale",
  "sessionId": "8ea52053-5c5d-477c-85fd-15c4d095d3f8"
}
```

---

### Tool call

_source line 28 · 2026-05-16T15:07:03.211Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BcabGg5jHFCJLbdB7h47H7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/best/imagined_experiments.yaml",
  "offset": 596,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e16d1b77-5c1e-4772-92c2-25ea8e4452e1",
  "isSidechain": false,
  "requestId": "req_011Cb6TR8URFKVnZmFmF4wTj",
  "type": "assistant",
  "uuid": "608f94e4-1e6b-417d-8c97-e1343b504fd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "8ea52053-5c5d-477c-85fd-15c4d095d3f8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016LyPhEqBYmGV6SCDbNij47",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4941,
      "cache_read_input_tokens": 84014,
      "output_tokens": 140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4941,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 140,
          "cache_read_input_tokens": 84014,
          "cache_creation_input_tokens": 4941,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4941
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

_source line 29 · 2026-05-16T15:07:03.219Z_

<details><summary>↩ Tool result · `toolu_01BcabGg5jHFCJLbdB7h47H7`</summary>

```text
596	    s025:
597	      switch_rate: 0.26
598	      cn_count: 13
599	      en_count: 37
600	      cn_acc: 0.077
601	      en_acc: 0.108
602	    full_dose_response:
603	      dense: 0.0
604	      s015: 0.04
605	      s020: 0.12
606	      s025: 0.26
607	      s030: 0.4
608	    monotonic: true
609	    spearman_rho: 1.0
610	  result_rationale: 'Language switching是compound sparsity的behavioral symptom——DeepSeek-R1-Distill
611	    在中文语料上训练，severe compound degradation使模型退回到训练时更frequent的 中文pattern。剂量-响应关系应当单调：
612	    (1) dense→s015: 仅2/50切换（4%），compound effect极轻，几乎不影响language control； (2) s020:
613	    预测12%（6/50），compound interaction开始可测（II median=1.21）， 部分问题的reasoning chain中出现中文片段；
614	    (3) s025: 预测26%（13/50），II=3.99的compound degradation显著干扰language control； (4) s030:
615	    已观察40%（20/50），与II=8.48一致。 递增模式跟随II的dose-response曲线（ρ=1.0），为compound degradation的
616	    behavioral manifestation提供独立evidence。
617	
618	    '
619	  tables:
620	  - name: 'Table: Language Switching Dose-Response'
621	    columns:
622	    - sparsity
623	    - switch_rate
624	    - cn_count
625	    - cn_acc
626	    - en_acc
627	    - II_median
628	    rows:
629	    - - dense
630	      - 0%
631	      - 0
632	      - n/a
633	      - 0.52
634	      - 0
635	    - - s015
636	      - 4%
637	      - 2
638	      - 0.0
639	      - 0.375
640	      - 0.39
641	    - - s020
642	      - 12%
643	      - 6
644	      - 0.0
645	      - 0.3
646	      - 1.21
647	    - - s025
648	      - 26%
649	      - 13
650	      - 0.077
651	      - 0.108
652	      - 3.99
653	    - - s030
654	      - 40%
655	      - 20
656	      - 0.1
657	      - 0.1
658	      - 8.48
659	  figures_description:
660	  - 'fig_lang_switching.pdf: 双Y轴图——左轴=language switching rate(%)随sparsity递增，右轴=II_median，两条曲线同步上升展示behavioral-statistical
661	    correspondence'
662	  analysis: 's020=12%, s025=26%填补了dose-response的两个关键中间点，确认language switching 与II severity完美共变。这作为Appendix中的behavioral
663	    evidence支撑主文claims—— compound sparsity不仅在perplexity/II层面可测，其behavioral consequence
664	    （language degradation）也遵循相同的dose-response模式。
665	
666	    '
667	- name: C9 Related Work Differentiation (Lethe/SparK/ThinKV/HIES Gap Analysis)
668	  plan_id: c9_related_work
669	  description: '§2 Related Work写作——定位本文与Lethe, SparK, ThinKV, Physics of KV Cache,
670	    HIES, R-KV的precise distinction。非计算实验，纯分析写作任务。
671	
672	    '
673	  expected_results:
674	    output_type: manuscript_section
675	    gap_analysis:
676	      lethe_distinction: Lethe = adaptive method paper; we = empirical finding of
677	        phase×strategy interaction
678	      spark_distinction: SparK = uniform compound analysis; we = non-uniform phase-dependent
679	        interaction
680	      thinkv_distinction: ThinKV = single-axis phase-aware; we = dual-axis compound
681	        × phase
682	      physics_kv_distinction: PhysicsKV = compression-rate phase transition; we =
683	        reasoning-phase compound gradient
684	      hies_distinction: HIES = single-axis score collapse + fix; we = compound amplification
685	        of collapse
686	      rkv_distinction: R-KV = task-specific optimization; we = mechanistic understanding
687	    positioning: '我们是唯一同时分析 pruning × eviction compound interaction 如何随 reasoning
688	      phase 和 eviction strategy 变化的工作。三个维度(compound × phase × strategy) 的同时交互分析是本文的unique
689	      contribution，prior work仅覆盖其中一到两个维度。
690	
691	      '
692	  result_rationale: 'C9是writing task而非计算实验。在best tier下，gap analysis清晰地将本文 定位为"compound
693	    × phase × strategy三维交互分析"的首次系统研究。 每篇prior work覆盖这三维中的子集：Lethe覆盖phase+method，SparK覆盖compound，
694	    ThinKV覆盖phase（单轴），HIES覆盖collapse mechanism（单轴）， Physics of KV覆盖compression-rate
695	    phase transition（不同语义的"phase"）。 本文独特地将三个维度交叉分析，发现了crossover现象和discrimination collapse
696	    的compound amplification——这些是单维分析无法观察到的涌现性质。
697	
698	    '
699	  tables: []
700	  figures_description: []
701	  analysis: C9不需要额外实验数据。§2 Related Work通过引用区分完成gap analysis， 明确本文在compound×phase×strategy三维空间中的unique
702	    positioning。 在best tier下这个positioning是无争议的——没有prior work同时分析这三个维度。
703	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "608f94e4-1e6b-417d-8c97-e1343b504fd1",
  "isSidechain": false,
  "promptId": "6dc2d8ec-28c8-43cb-89c7-84c3b4e58d64",
  "type": "user",
  "uuid": "10776798-a00c-4661-bf93-ad62f2900077",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T073742/best/imagined_experiments.yaml",
      "content": "    s025:\n      switch_rate: 0.26\n      cn_count: 13\n      en_count: 37\n      cn_acc: 0.077\n      en_acc: 0.108\n    full_dose_response:\n      dense: 0.0\n      s015: 0.04\n      s020: 0.12\n      s025: 0.26\n      s030: 0.4\n    monotonic: true\n    spearman_rho: 1.0\n  result_rationale: 'Language switching是compound sparsity的behavioral symptom——DeepSeek-R1-Distill\n    在中文语料上训练，severe compound degradation使模型退回到训练时更frequent的 中文pattern。剂量-响应关系应当单调：\n    (1) dense→s015: 仅2/50切换（4%），compound effect极轻，几乎不影响language control； (2) s020:\n    预测12%（6/50），compound interaction开始可测（II median=1.21）， 部分问题的reasoning chain中出现中文片段；\n    (3) s025: 预测26%（13/50），II=3.99的compound degradation显著干扰language control； (4) s030:\n    已观察40%（20/50），与II=8.48一致。 递增模式跟随II的dose-response曲线（ρ=1.0），为compound degradation的\n    behavioral manifestation提供独立evidence。\n\n    '\n  tables:\n  - name: 'Table: Language Switching Dose-Response'\n    columns:\n    - sparsity\n    - switch_rate\n    - cn_count\n    - cn_acc\n    - en_acc\n    - II_median\n    rows:\n    - - dense\n      - 0%\n      - 0\n      - n/a\n      - 0.52\n      - 0\n    - - s015\n      - 4%\n      - 2\n      - 0.0\n      - 0.375\n      - 0.39\n    - - s020\n      - 12%\n      - 6\n      - 0.0\n      - 0.3\n      - 1.21\n    - - s025\n      - 26%\n      - 13\n      - 0.077\n      - 0.108\n      - 3.99\n    - - s030\n      - 40%\n      - 20\n      - 0.1\n      - 0.1\n      - 8.48\n  figures_description:\n  - 'fig_lang_switching.pdf: 双Y轴图——左轴=language switching rate(%)随sparsity递增，右轴=II_median，两条曲线同步上升展示behavioral-statistical\n    correspondence'\n  analysis: 's020=12%, s025=26%填补了dose-response的两个关键中间点，确认language switching 与II severity完美共变。这作为Appendix中的behavioral\n    evidence支撑主文claims—— compound sparsity不仅在perplexity/II层面可测，其behavioral consequence\n    （language degradation）也遵循相同的dose-response模式。\n\n    '\n- name: C9 Related Work Differentiation (Lethe/SparK/ThinKV/HIES Gap Analysis)\n  plan_id: c9_related_work\n  description: '§2 Related Work写作——定位本文与Lethe, SparK, ThinKV, Physics of KV Cache,\n    HIES, R-KV的precise distinction。非计算实验，纯分析写作任务。\n\n    '\n  expected_results:\n    output_type: manuscript_section\n    gap_analysis:\n      lethe_distinction: Lethe = adaptive method paper; we = empirical finding of\n        phase×strategy interaction\n      spark_distinction: SparK = uniform compound analysis; we = non-uniform phase-dependent\n        interaction\n      thinkv_distinction: ThinKV = single-axis phase-aware; we = dual-axis compound\n        × phase\n      physics_kv_distinction: PhysicsKV = compression-rate phase transition; we =\n        reasoning-phase compound gradient\n      hies_distinction: HIES = single-axis score collapse + fix; we = compound amplification\n        of collapse\n      rkv_distinction: R-KV = task-specific optimization; we = mechanistic understanding\n    positioning: '我们是唯一同时分析 pruning × eviction compound interaction 如何随 reasoning\n      phase 和 eviction strategy 变化的工作。三个维度(compound × phase × strategy) 的同时交互分析是本文的unique\n      contribution，prior work仅覆盖其中一到两个维度。\n\n      '\n  result_rationale: 'C9是writing task而非计算实验。在best tier下，gap analysis清晰地将本文 定位为\"compound\n    × phase × strategy三维交互分析\"的首次系统研究。 每篇prior work覆盖这三维中的子集：Lethe覆盖phase+method，SparK覆盖compound，\n    ThinKV覆盖phase（单轴），HIES覆盖collapse mechanism（单轴）， Physics of KV覆盖compression-rate\n    phase transition（不同语义的\"phase\"）。 本文独特地将三个维度交叉分析，发现了crossover现象和discrimination collapse\n    的compound amplification——这些是单维分析无法观察到的涌现性质。\n\n    '\n  tables: []\n  figures_description: []\n  analysis: C9不需要额外实验数据。§2 Related Work通过引用区分完成gap analysis， 明确本文在compound×phase×strategy三维空间中的unique\n    positioning。 在best tier下这个positioning是无争议的——没有prior work同时分析这三个维度。\n",
      "numLines": 108,
      "startLine": 596,
      "totalLines": 703
    }
  },
  "sourceToolAssistantUUID": "608f94e4-1e6b-417d-8c97-e1343b504fd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "8ea52053-5c5d-477c-85fd-15c4d095d3f8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-16T15:07:33.781Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a complete picture of the existing "best" tier imagined experiments from the dream report. The user is asking me to produce the same kind of output but based on the experiment_plan. Let me check which experiments in the plan are "planned" (not yet done). 

Looking at the experiment_plan as provided in the user's message, all experiments have status: DONE. The RUNNING experiments in the registry are:
1. c8_llama_n250_fixed
2. gpqa_ds_importance_s015

But the dream report already has imagined experiments. The user is asking me to generate predictions based on the "best" tier definition for the experiments that are currently RUNNING or planned to support the narrative.
 
I'm re-reading the request more carefully — the user wants detailed predictions for planned experiments from the experiment_plan, but all the entries shown have status DONE. Looking at the RUNNING experiments in the registry, c8_llama_n250_fixed is the one that's actively running and would need predicted data to match the "best" tier narrative. I see the confusion now—all the experiments in the provided plan already show DONE status with results, but the user is asking me to expand predictions for "planned" experiments. I think they want me to generate detailed predictions for the currently running experiments like the DeepSeek importance phase and the LLaMA validation, including the rationale for each predicted result. I'm realizing that the mechanism correlation analysis can be computed from existing data, so the truly active experiments are just c8_llama_n250_fixed and gpqa_ds_importance_s015. Now I'm pulling together the comprehensive predictions for the "best" tier by calibrating against the performance metrics I already have from similar experiments like the n=250 importance run and the MATH/GSM8K datasets.

Generating YAML output...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10776798-a00c-4661-bf93-ad62f2900077",
  "isSidechain": false,
  "requestId": "req_011Cb6TRYYkzv2zxTMqBJTDP",
  "type": "assistant",
  "uuid": "598e5a97-0d9d-4e64-9805-58885896e1d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "8ea52053-5c5d-477c-85fd-15c4d095d3f8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YAkx3N6RXvUp7bZL3GgU6w",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1887,
      "cache_read_input_tokens": 88955,
      "output_tokens": 1416,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1887,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1416,
          "cache_read_input_tokens": 88955,
          "cache_creation_input_tokens": 1887,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1887
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

_source line 31 · 2026-05-16T15:07:34.417Z_

Now I have the full picture. The existing dream report already has predictions for the "best" tier. Let me now produce the definitive, fully detailed prediction output calibrated against the actual partial results (especially `c8_llama_gpu0_s025` which gives ground truth for n=250 importance s025).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "598e5a97-0d9d-4e64-9805-58885896e1d5",
  "isSidechain": false,
  "requestId": "req_011Cb6TRYYkzv2zxTMqBJTDP",
  "type": "assistant",
  "uuid": "7768c103-8b7b-4f1a-bb21-7610ea414537",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "8ea52053-5c5d-477c-85fd-15c4d095d3f8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YAkx3N6RXvUp7bZL3GgU6w",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1887,
      "cache_read_input_tokens": 88955,
      "output_tokens": 1416,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1887,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1416,
          "cache_read_input_tokens": 88955,
          "cache_creation_input_tokens": 1887,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1887
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

_source line 32 · 2026-05-16T15:07:35.254Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QkmhMjeC4Bsn89xapyCG2J`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/experiment_plan.yaml",
  "offset": 100,
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7768c103-8b7b-4f1a-bb21-7610ea414537",
  "isSidechain": false,
  "requestId": "req_011Cb6TRYYkzv2zxTMqBJTDP",
  "type": "assistant",
  "uuid": "42076558-99e1-4939-a750-e0f15bdb9f77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "8ea52053-5c5d-477c-85fd-15c4d095d3f8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YAkx3N6RXvUp7bZL3GgU6w",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1887,
      "cache_read_input_tokens": 88955,
      "output_tokens": 1416,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1887,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1416,
          "cache_read_input_tokens": 88955,
          "cache_creation_input_tokens": 1887,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1887
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

_source line 33 · 2026-05-16T15:07:35.268Z_

<details><summary>↩ Tool result · `toolu_01QkmhMjeC4Bsn89xapyCG2J`</summary>

```text
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "42076558-99e1-4939-a750-e0f15bdb9f77",
  "isSidechain": false,
  "promptId": "6dc2d8ec-28c8-43cb-89c7-84c3b4e58d64",
  "type": "user",
  "uuid": "0ce6e86f-5c89-4e4c-bfe5-3ed001a815bf",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/experiment_plan.yaml",
      "content": "- id: c4_c4_entropy\n  claim: C4\n  description: 'DS importance entropy_delta: -0.04 to -0.05 (collapse); random: +0.13\n    to +0.23 (redistribution). Gini_delta: -0.03 to -0.08'\n  registry_id: c4_entropy\n  role: primary\n  priority: high\n- id: c4_qwen_c4_entropy\n  claim: C4\n  description: 'QW importance entropy_delta mixed: s015=-0.073, s025=+0.045; Gini\n    weaker (-0.01 to -0.02). Model-dependent pattern'\n  registry_id: qwen_c4_entropy\n  role: primary\n  priority: high\n- id: c5_bf16_qw_imp_s030\n  claim: C5\n  description: 'Qwen: median_diff=2.619, Cohen''s d=1.439, p<1e-5; replicates DeepSeek\n    pattern'\n  registry_id: bf16_qw_imp_s030\n  role: primary\n  priority: high\n- id: c5_bf16_importance_s030\n  claim: C5\n  description: 'DeepSeek: II low_median=14.64, high_median=0.053; strong phase gradient'\n  registry_id: bf16_importance_s030\n  role: primary\n  priority: high\n- id: c5_c2_n500_deepseek\n  claim: C5\n  description: 'DS n=500: imp_s030 median_II=8.48, CI=[7.46,9.56], p=1.3e-78; robust\n    at scale'\n  registry_id: c2_n500_deepseek\n  role: supporting\n  priority: medium\n- id: c5_c2_qw_n500_r3\n  claim: C5\n  description: 'QW n=500: imp_s030 median_II=4.33, p<1e-40; cross-model replication\n    at high power'\n  registry_id: c2_qw_n500_r3\n  role: supporting\n  priority: medium\n- id: c5b_c5b_pilot\n  claim: C5b\n  description: 'Oracle recovery=18% (gate: >30% FAIL); heuristic recovery=31.7% but\n    CI crosses zero. s030 incomplete'\n  registry_id: c5b_pilot\n  role: primary\n  priority: high\n- id: c6_bf16_importance_s015\n  claim: C6\n  description: II low_median=0.398 at s=0.15\n  registry_id: bf16_importance_s015\n  role: primary\n  priority: high\n- id: c6_bf16_importance_s020\n  claim: C6\n  description: II low_median=1.496 at s=0.20\n  registry_id: bf16_importance_s020\n  role: supporting\n  priority: medium\n- id: c6_bf16_importance_s025\n  claim: C6\n  description: II low_median=7.196 at s=0.25\n  registry_id: bf16_importance_s025\n  role: supporting\n  priority: medium\n- id: c6_bf16_importance_s030\n  claim: C6\n  description: II low_median=14.64 at s=0.30; growth 0.40->1.50->7.20->14.64 is sub-exponential\n  registry_id: bf16_importance_s030\n  role: supporting\n  priority: medium\n- id: c7_c2_n500_deepseek\n  claim: C7\n  description: 'DS n=500: all 4 sparsities significant (p<1e-70); CIs non-overlapping\n    across dose levels'\n  registry_id: c2_n500_deepseek\n  role: primary\n  priority: high\n- id: c7_c2_qw_n500_r3\n  claim: C7\n  description: 'QW n=500: all 4 sparsities significant (p<1e-14 Bonferroni-corrected);\n    mid_null_rate=45.2%'\n  registry_id: c2_qw_n500_r3\n  role: primary\n  priority: high\n- id: c8_c3_llama\n  claim: C8\n  description: LLaMA-8B (LlamaForCausalLM) replicates phase-modulated compound severity\n    from Qwen2ForCausalLM\n  registry_id: c3_llama\n  role: primary\n  priority: high\n- id: c10_gsm8k_profiling_ds\n  claim: C10\n  description: 'DS GSM8K importance gradient: s015=0.241, s020=0.740, s025=1.992,\n    s030=4.636 (monotonic)'\n  registry_id: gsm8k_profiling_ds\n  role: primary\n  priority: high",
      "numLines": 100,
      "startLine": 100,
      "totalLines": 303
    }
  },
  "sourceToolAssistantUUID": "42076558-99e1-4939-a750-e0f15bdb9f77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "8ea52053-5c5d-477c-85fd-15c4d095d3f8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 34 · 2026-05-16T15:07:35.359Z_

```json
{
  "parentUuid": "0ce6e86f-5c89-4e4c-bfe5-3ed001a815bf",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "02036f6a-3c36-4101-acae-2d2f25ce9d0b",
  "timestamp": "2026-05-16T15:07:35.359Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "8ea52053-5c5d-477c-85fd-15c4d095d3f8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 35 · 2026-05-16T15:07:38.801Z_

<details open><summary>🔧 Tool call — Read · `toolu_014v2EyDAksg17Gkhu9YKigF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/experiment_plan.yaml",
  "offset": 200,
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02036f6a-3c36-4101-acae-2d2f25ce9d0b",
  "isSidechain": false,
  "requestId": "req_011Cb6TTukXVtik7Q5DP1pnR",
  "type": "assistant",
  "uuid": "a4540e9e-e90e-4bd5-b340-da1b0315416f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "8ea52053-5c5d-477c-85fd-15c4d095d3f8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WYkTrKnsaJAkkXTQeT8AJF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2998,
      "cache_read_input_tokens": 90842,
      "output_tokens": 122,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2998,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 122,
          "cache_read_input_tokens": 90842,
          "cache_creation_input_tokens": 2998,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2998
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

_source line 36 · 2026-05-16T15:07:38.821Z_

<details><summary>↩ Tool result · `toolu_014v2EyDAksg17Gkhu9YKigF`</summary>

```text
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4540e9e-e90e-4bd5-b340-da1b0315416f",
  "isSidechain": false,
  "promptId": "6dc2d8ec-28c8-43cb-89c7-84c3b4e58d64",
  "type": "user",
  "uuid": "a69b711c-43d7-4571-928a-d0e5f971d35f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/experiment_plan.yaml",
      "content": "- id: c10_gsm8k_profiling_qw\n  claim: C10\n  description: 'QW GSM8K importance gradient: s015=0.039, s020=0.158, s025=1.100,\n    s030=2.092 (monotonic)'\n  registry_id: gsm8k_profiling_qw\n  role: primary\n  priority: high\n- id: c10_gsm8k_qw_rand_s025_v2\n  claim: C10\n  description: 'QW random s025 GSM8K: II median_high=0.72, low=1.48; phase gradient\n    weaker than importance'\n  registry_id: gsm8k_qw_rand_s025_v2\n  role: supporting\n  priority: medium\n- id: c10_gsm8k_qw_rand_s030_v2\n  claim: C10\n  description: 'QW random s030 GSM8K: II median_high=2.31, low=5.87; compound effect\n    on GSM8K confirmed'\n  registry_id: gsm8k_qw_rand_s030_v2\n  role: supporting\n  priority: medium\n- id: s3_c_bf16_ds_imp_s010\n  claim: S3->C\n  description: 'DS s=0.10: II_high_median=0.003, verdict=FAIL; below onset threshold\n    for DeepSeek'\n  registry_id: bf16_ds_imp_s010\n  role: primary\n  priority: high\n- id: s3_c_bf16_qw_imp_s010\n  claim: S3->C\n  description: 'QW s=0.10: overall_verdict=PASS, CI_overlap_test=PASS; Qwen onset\n    earlier than DeepSeek'\n  registry_id: bf16_qw_imp_s010\n  role: primary\n  priority: high\n- id: s3_c_bf16_qw_imp_s015\n  claim: S3->C\n  description: 'QW s=0.15: median_diff=0.048, permutation_p=0.0001; confirmed above\n    threshold'\n  registry_id: bf16_qw_imp_s015\n  role: supporting\n  priority: medium\n- id: s7_c_c2_n500_deepseek\n  claim: S7->C\n  description: 'DS n=500 monotonic: imp median II 0.39->1.21->3.99->8.48 across s015-s030\n    (Spearman rho=1.0)'\n  registry_id: c2_n500_deepseek\n  role: primary\n  priority: high\n- id: s7_c_c2_qw_n500_r3\n  claim: S7->C\n  description: 'QW n=500 monotonic: imp median II 0.066->0.307->1.075->4.33 across\n    s015-s030 (Spearman rho=1.0)'\n  registry_id: c2_qw_n500_r3\n  role: primary\n  priority: high\n- id: s7_c_bf16_qw_imp_s035\n  claim: S7->C\n  description: 'QW s=0.35: low_II_median=8.24; extends dose-response beyond s030'\n  registry_id: bf16_qw_imp_s035\n  role: supporting\n  priority: medium\n_claims:\n  C1:\n    description: Compound sparsity severity is strategy- and task-modulated\n    status: confirmed\n  C2:\n    description: Severity is phase-modulated (amplified in low-sparsity phase)\n    status: confirmed\n  C3:\n    description: Phase-strategy crossover exists\n    status: confirmed\n  C4:\n    description: Discrimination collapse as primary mechanism; entropy redistribution\n      model-dependent\n    status: partially_confirmed\n  C5:\n    description: Phase-modulated compound severity generalizes across models\n    status: confirmed\n  C5b:\n    description: Phase-aware mitigation recovers compound degradation\n    status: future_work\n  C6:\n    description: Severity gradient is sub-exponential\n    status: confirmed\n  C7:\n    description: Statistical power at n=500 confirms dose-response\n    status: running\n  C8:\n    description: Cross-architecture validation (LLaMA)\n    status: partially_confirmed\n  C9:\n    description: Differentiation from Lethe/SparK prior work\n    status: planned\n  C10:\n    description: Phase gradient cross-benchmark robust; strategy specificity task-modulated\n    status: running\n  S3->C:\n    description: Onset threshold is model-dependent\n    status: confirmed",
      "numLines": 100,
      "startLine": 200,
      "totalLines": 303
    }
  },
  "sourceToolAssistantUUID": "a4540e9e-e90e-4bd5-b340-da1b0315416f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "8ea52053-5c5d-477c-85fd-15c4d095d3f8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 37_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：LLaMA n=250 揭示 n=50 功效不足掩盖了中等 strategy×phase 交互；GPQA 确认跨 task 泛化且 strategy specificity 强。三维交互叙事完全成立。 核心假设：['LLaMA imp_vs_rand d_z 在 n=50 被噪声衰减；n=250 揭示真实中等…",
  "leafUuid": "a69b711c-43d7-4571-928a-d0e5f971d35f",
  "sessionId": "8ea52053-5c5d-477c-85fd-15c4d095d3f8"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "ai-title",
  "aiTitle": "Phase-gated compound sparsity validation at scale",
  "sessionId": "8ea52053-5c5d-477c-85fd-15c4d095d3f8"
}
```

---

### Assistant

_source line 39 · 2026-05-16T15:07:57.812Z_

<details><summary>Logged reasoning block</summary>

```text
Now I see the structure. The experiment_plan has claims with statuses:
- C8: partially_confirmed
- C9: planned
- C10: running (but experiments for it are mostly DONE)

The RUNNING registry experiments are:
- c8_llama_n250_fixed
- gpqa_ds_importance_s015

So the "planned" experiments that need predictions for the best tier are:
1. c8_llama_n250_fixed (upgrading C8 from partially_confirmed to confirmed)
2. gpqa_ds_importance_s015 (and related GPQA experiments for cross-task generalization)


3. C9 (related work differentiation - writing task, no computation)

Now I'm assembling the comprehensive YAML output with all the experiments needed to support the best tier narrative: the LLaMA n=250 run, the GPQA importance sampling variants across different seeds, the random baseline experiments for comparison, cross-model generalization tests, and the correlation analysis from existing data.

For the importance versus random comparison at n=250, I'm using the ground truth from the LLaMA n=250 importance run to calibrate my predictions—the phase gradient median difference was 0.3761 with a very strong effect size. The key assumption is that random sampling at n=50 showed inflated phase gradients (0.35-0.44) due to small sample noise, and scaling to n=250 should compress this to 0.1-0.25, which would push the importance-versus-random effect size from the n=50 range of 0.19-0.34 up to 0.35-0.6.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a69b711c-43d7-4571-928a-d0e5f971d35f",
  "isSidechain": false,
  "requestId": "req_011Cb6TUAfTgYNssiXtnitf6",
  "type": "assistant",
  "uuid": "1ec5ae8e-398d-4cde-8af4-7957c34c013d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "8ea52053-5c5d-477c-85fd-15c4d095d3f8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0143PvZiTuikEYUycCEmQTVs",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1528,
      "cache_read_input_tokens": 93840,
      "output_tokens": 9839,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1528,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9839,
          "cache_read_input_tokens": 93840,
          "cache_creation_input_tokens": 1528,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1528
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

_source line 40 · 2026-05-16T15:10:49.603Z_

I now have all the data needed. The experiment_plan has claims C8 (partially_confirmed), C9 (planned), and C10 (running) as the ones needing "best" tier predictions. The RUNNING registry experiments are `c8_llama_n250_fixed` and `gpqa_ds_importance_s015`. Let me produce the comprehensive prediction output, calibrated against the ground-truth partial result from `c8_llama_gpu0_s025` (n=250, importance s025: d_z=1.1174, median_diff=0.3761).

```yaml
tier: best
narrative_guidance: |
  原始 framing "phase-gated compound sparsity" 完全成立。Strategy × phase × compound 三维交互
  在三模型（DS/QW/LLaMA）、两架构（Qwen2/Llama）、三 benchmark（MATH-500/GSM8K/GPQA）上一致复现。
  LLaMA n=250 高功效下 imp_vs_rand d_z 达中等效应量（~0.52 at s030），random phase gradient 收缩至
  不显著（d_z~0.18），消除 n=50 的 architecture-dependent 限定。GPQA 提供跨推理领域（科学→数学）泛化，
  strategy specificity ratio ≥5× 确认 importance 的 phase-dependent compound interaction 
  不是 metric artifact 而是 genuine phenomenon。C8 升级为 confirmed，论文 claims 无需调整。
  Title/framing 保持 "phase-gated"，EMNLP main 正会强竞争力——novelty 同时具备现象发现（三维交互）
  和机制解释（discrimination collapse），泛化证据覆盖模型/架构/任务三个维度。

imagined_experiments:
  - name: "LLaMA n=250 Cross-Architecture Full Validation"
    plan_id: "c8_llama_n250_fixed"
    description: |
      DeepSeek-R1-Distill-Llama-8B 上 n=250 problems，8 条件（importance/random × s015/s020/s025/s030）。
      关键验证：(1) imp_vs_rand d_z 达 medium effect；(2) 3+ sparsity Bonferroni 显著；
      (3) random phase gradient 在 n=250 下衰减至 negligible。
    expected_results:
      model: DeepSeek-R1-Distill-Llama-8B
      n_problems: 250
      n_valid: 244
      n_skipped: 6
      conditions_completed: 8/8
      n_bootstrap: 10000
      bonferroni_k: 4
      imp_vs_rand_dz:
        s015: 0.25
        s020: 0.34
        s025: 0.44
        s030: 0.52
      imp_vs_rand_dz_ci:
        s015: [0.08, 0.42]
        s020: [0.17, 0.51]
        s025: [0.27, 0.61]
        s030: [0.35, 0.69]
      imp_vs_rand_dz_interpretation:
        s015: small
        s020: small_to_medium
        s025: medium
        s030: medium
      imp_vs_rand_dz_monotonic: true
      phase_gradient_importance_dz:
        s015: 0.95
        s020: 1.04
        s025: 1.12
        s030: 0.98
      phase_gradient_importance_dz_ci:
        s015: [0.75, 1.15]
        s020: [0.86, 1.22]
        s025: [0.94, 1.30]
        s030: [0.82, 1.14]
      phase_gradient_importance_interpretation: all_large
      phase_gradient_random_dz:
        s015: 0.14
        s020: 0.17
        s025: 0.20
        s030: 0.22
      phase_gradient_random_dz_ci:
        s015: [-0.03, 0.31]
        s020: [0.00, 0.34]
        s025: [0.03, 0.37]
        s030: [0.05, 0.39]
      phase_gradient_random_interpretation: negligible_to_small
      phase_gradient_random_bonferroni_significant:
        s015: false
        s020: false
        s025: false
        s030: false
      median_diff:
        s015: 0.024
        s020: 0.055
        s025: 0.152
        s030: 0.42
      median_diff_ci:
        s015: [0.007, 0.044]
        s020: [0.015, 0.112]
        s025: [0.058, 0.285]
        s030: [0.19, 0.63]
      wilcoxon_p:
        s015: 0.015
        s020: 0.003
        s025: 0.00028
        s030: 1.5e-05
      wilcoxon_p_bonferroni:
        s015: 0.060
        s020: 0.012
        s025: 0.0011
        s030: 6.0e-05
      significant_bonferroni:
        s015: false
        s020: true
        s025: true
        s030: true
      bonferroni_significant_count: 3
      cross_arch_comparison:
        deepseek_qwen2_imp_vs_rand_dz_s030: 0.80
        llama_imp_vs_rand_dz_s030: 0.52
        delta: 0.28
        note: "LLaMA effect weaker in magnitude but unambiguously medium (CI excludes zero). Architecture modulates strength but not direction."
    result_rationale: |
      n=50 时 imp_vs_rand d_z=0.19→0.34，CI 极宽（s030: [0.06, 0.66]），仅 s030 Bonferroni 
      显著（p=0.029）。n=250 使 SE 缩小 √5≈2.24 倍，效应量估计趋于真值。三个关键机制：
      
      (1) Random phase gradient 衰减：n=50 时 random d_z=0.35-0.44 可能被采样变异性膨胀。
      Random masking 是无差别噪声注入，不应产生与 importance 同等的 strategy-dependent phase 调制。
      在 n=250 下采样噪声被平滑，random d_z 回落至 ~0.14-0.22，无一 Bonferroni 显著——
      与 DS/QW 在 n=500 下 random s015/s020 NS 的模式一致。n=50 时 LLaMA random 显著
      很可能是 Type I error（多重比较 + 小样本变异性）。
      
      (2) Importance gradient 稳定：c8_llama_gpu0_s025 已验证 n=250 importance s025 
      d_z=1.1174（与 n=50 的 1.12 一致），确认 importance phase gradient 是 robust signal 
      而非偶然。全 4 水平 d_z 维持在 0.95-1.12（large effect）。
      
      (3) imp_vs_rand 提升：当 random gradient 从 ~0.44 缩至 ~0.22 而 importance 保持 ~1.0+，
      两者差距扩大→imp_vs_rand d_z 从 0.34 提升至 0.52。s020/s025/s030 三水平获得
      Bonferroni 显著性（n=250 给出 >90% power 检测 d_z≥0.35 的效应）。
    tables:
      - name: "LLaMA n=250 vs n=50 Effect Size Comparison"
        columns: [sparsity, n50_imp_rand_dz, n250_imp_rand_dz, n250_bonf_p, significant]
        rows:
          - [s015, 0.19, 0.25, 0.060, "NS"]
          - [s020, 0.26, 0.34, 0.012, "✓"]
          - [s025, 0.29, 0.44, 0.0011, "✓"]
          - [s030, 0.34, 0.52, 6.0e-05, "✓"]
      - name: "Random Phase Gradient Attenuation n=50 → n=250"
        columns: [sparsity, n50_random_dz, n250_random_dz, n250_CI_contains_zero, bonf_significant]
        rows:
          - [s015, 0.35, 0.14, "yes", "no"]
          - [s020, 0.37, 0.17, "borderline", "no"]
          - [s025, 0.45, 0.20, "no", "no"]
          - [s030, 0.44, 0.22, "no", "no"]
    figures_description:
      - "fig_c8_n250_forest.pdf: Forest plot 三架构 (DS-Qwen2/QW/LLaMA) × 4 sparsity 的 imp_vs_rand d_z 及 95% CI。LLaMA n=250 点位从 n=50 虚线位置移至 medium zone。"
      - "fig_c8_random_attenuation.pdf: 左=importance dz (稳定 ~1.0)，右=random dz (从 0.35-0.44 衰减至 0.14-0.22)，双 panel 对比 n=50 vs n=250。"
    analysis: |
      LLaMA n=250 解除 C8 的 architecture-dependent 限定。三个关键变化：
      (1) imp_vs_rand d_z s030=0.52（medium），s020/s025/s030 Bonferroni 显著（3/4）；
      (2) random phase gradient 全部无 Bonferroni 显著——与 DS/QW 模式一致；
      (3) importance gradient 稳定（d_z=0.95-1.12），与 c8_llama_gpu0_s025 已验证的 1.1174 吻合。
      论文可改为 "Cross-architecture validation confirms strategy×phase interaction 
      (d_z=0.52, Bonferroni p<0.001 at s=0.30)" 而非 "suggests/provides partial support"。
      C8 从 partially_confirmed 升级为 confirmed。

  - name: "GPQA DeepSeek Importance Phase Gradient Profiling"
    plan_id: "gpqa_ds_importance_s015"
    description: |
      DeepSeek-R1-Distill-Qwen-7B 对 GPQA-Diamond (n=50) 运行 importance masking，
      4 sparsity levels (s015/s020/s025/s030)。验证 phase gradient 单调递增跨 benchmark。
    expected_results:
      model: DeepSeek-R1-Distill-Qwen-7B
      benchmark: GPQA-Diamond
      n_problems: 50
      method: "median + Wilcoxon + bootstrap_median(B=10000)"
      importance:
        s015:
          median_gradient: 0.19
          ci_low: 0.065
          ci_high: 0.39
          wilcoxon_p: 0.0006
          bonferroni_p: 0.0024
        s020:
          median_gradient: 0.58
          ci_low: 0.24
          ci_high: 0.95
          wilcoxon_p: 0.0002
          bonferroni_p: 0.0008
        s025:
          median_gradient: 1.72
          ci_low: 0.82
          ci_high: 2.55
          wilcoxon_p: 0.0001
          bonferroni_p: 0.0004
        s030:
          median_gradient: 4.15
          ci_low: 1.9
          ci_high: 8.9
          wilcoxon_p: 0.0001
          bonferroni_p: 0.0004
      dose_response_monotonic: true
      spearman_rho: 1.0
      bonferroni_sig_count: 4
      all_bonferroni_significant: true
    result_rationale: |
      GPQA-Diamond 是 graduate-level 科学推理，推理链结构介于 MATH-500（长复杂链）和 
      GSM8K（短规律链）之间。预测 phase gradient 单调递增：
      
      (1) 物理机制不依赖 task 类型——head pruning → discrimination collapse → compound interaction 
      在 low-sparsity phase 最严重，此机制跨 benchmark 通用。MATH-500 和 GSM8K 已 100% 单调。
      
      (2) Gradient magnitude 预计介于 MATH-500 (0.39→8.48) 和 GSM8K (0.24→4.68) 之间：
      GPQA 多选题 format 使 reasoning chain 比 MATH-500 短（平均 token 更少），但科学推理
      的知识检索步骤比 GSM8K 算术多，compound sensitivity 居中。预测 s030 ≈ 4.15。
      
      (3) 全 4 水平 Bonferroni 显著——DS 在 MATH-500 n=50 时 s015 就显著 (d=0.61)，
      GPQA 虽然绝对 magnitude 略小但效应仍在 detectable 范围，n=50 配合 DS 的强 signal 足够。
    tables:
      - name: "Cross-Benchmark Phase Gradient (DeepSeek Importance)"
        columns: [sparsity, MATH-500_n500, GSM8K_n50, GPQA_n50]
        rows:
          - [s015, 0.39, 0.241, 0.19]
          - [s020, 1.21, 0.740, 0.58]
          - [s025, 3.99, 1.992, 1.72]
          - [s030, 8.48, 4.682, 4.15]
    figures_description:
      - "fig_cross_benchmark_ds.pdf: 三条 dose-response 曲线 (MATH/GSM/GPQA) 均单调递增，GPQA 居中。"
    analysis: |
      DS GPQA gradient 0.19→4.15 单调递增（ρ=1.0），全 4 水平 Bonferroni 显著。
      三 benchmark 全部单调复现，phase modulation 是跨推理领域的 robust finding。
      Magnitude ordering MATH > GPQA > GSM 反映推理链复杂度对 compound sensitivity 的调制。

  - name: "GPQA Qwen Importance Phase Gradient Cross-Model"
    plan_id: "gpqa_profiling_qw"
    description: |
      Qwen2.5-7B-Instruct 对 GPQA-Diamond (n=50) importance masking，验证 cross-model 复现。
    expected_results:
      model: Qwen2.5-7B-Instruct
      benchmark: GPQA-Diamond
      n_problems: 50
      importance:
        s015:
          median_gradient: 0.038
          ci_low: 0.005
          ci_high: 0.088
          wilcoxon_p: 0.018
          bonferroni_p: 0.072
        s020:
          median_gradient: 0.19
          ci_low: 0.075
          ci_high: 0.35
          wilcoxon_p: 0.0004
          bonferroni_p: 0.0016
        s025:
          median_gradient: 0.85
          ci_low: 0.42
          ci_high: 1.30
          wilcoxon_p: 0.0001
          bonferroni_p: 0.0004
        s030:
          median_gradient: 2.28
          ci_low: 1.22
          ci_high: 3.55
          wilcoxon_p: 0.0001
          bonferroni_p: 0.0004
      dose_response_monotonic: true
      spearman_rho: 1.0
      bonferroni_sig_count: 3
      qw_ds_ratio_s030: 0.55
      note: "QW magnitude ~55% of DS, consistent with MATH-500 pattern (QW ~37%). GPQA ratio slightly higher because QW's science reasoning less disadvantaged than math."
    result_rationale: |
      QW 在 MATH-500 上 gradient 为 0.066→3.155（DS 的 ~37%），在 GSM8K 上为 0.039→2.092。
      GPQA 预测 QW gradient 0.038→2.28，DS/QW 比值约 1.8×。
      
      QW magnitude 一贯小于 DS（Qwen2.5-7B-Instruct 的 attention head utilization 更均匀，
      pruning 影响较分散），但方向和单调性完全一致。s015 Bonferroni 边缘不显著（p=0.072），
      与 MATH-500 上 QW s015 CI 含零的 onset threshold 模式一致——QW 在最低 sparsity 效应弱，
      但 s020+ 稳定显著。
    tables:
      - name: "Cross-Benchmark Phase Gradient (Qwen Importance)"
        columns: [sparsity, MATH-500_n500, GSM8K_n50, GPQA_n50]
        rows:
          - [s015, 0.066, 0.039, 0.038]
          - [s020, 0.307, 0.158, 0.19]
          - [s025, 1.075, 1.100, 0.85]
          - [s030, 3.155, 2.092, 2.28]
    figures_description:
      - "fig_cross_benchmark_qw.pdf: QW 三 benchmark gradient 曲线，标注 onset threshold ~s020。"
    analysis: |
      QW GPQA 单调递增复现（ρ=1.0），3/4 Bonferroni 显著。结合 DS，两模型×三 benchmark
      共 6 条 dose-response 曲线全部单调。QW-GPQA s030=2.28 与 QW-GSM8K s030=2.09 接近，
      暗示 QW 跨 task 的 compound sensitivity 较稳定。

  - name: "GPQA Random Baselines and Strategy Specificity"
    plan_id: "gpqa_random_baselines"
    description: |
      DS 和 QW 对 GPQA-Diamond (n=50) 运行 random masking，计算 imp/rand ratio。
      验证 strategy specificity ≥5×。
    expected_results:
      ds_random:
        s015:
          median_gradient: 0.024
          wilcoxon_p: 0.12
        s020:
          median_gradient: 0.072
          wilcoxon_p: 0.045
        s025:
          median_gradient: 0.24
          wilcoxon_p: 0.008
        s030:
          median_gradient: 0.55
          wilcoxon_p: 0.003
      qw_random:
        s015:
          median_gradient: 0.005
          wilcoxon_p: 0.38
        s020:
          median_gradient: 0.025
          wilcoxon_p: 0.15
        s025:
          median_gradient: 0.12
          wilcoxon_p: 0.022
        s030:
          median_gradient: 0.36
          wilcoxon_p: 0.006
      strategy_specificity_ratio_ds:
        s015: 7.9
        s020: 8.1
        s025: 7.2
        s030: 7.5
      strategy_specificity_ratio_qw:
        s015: 7.6
        s020: 7.6
        s025: 7.1
        s030: 6.3
      strategy_specificity_ratio_range: "6.3-8.1×"
      all_ratios_above_5x: true
      cross_benchmark_specificity:
        MATH-500: "15-36×"
        GPQA: "6.3-8.1×"
        GSM8K: "2.3-3.8×"
    result_rationale: |
      Strategy specificity ratio 的 task-dependence 与 reasoning chain 结构相关：
      
      (1) MATH-500 推理链最长最复杂（竞赛数学），importance score 的 phase-dependent 
      discrimination collapse 最剧烈 → ratio 最高（15-36×）；
      
      (2) GSM8K 推理链最短最规律（小学数学），importance 和 random 的差异被压缩 → 
      ratio 最低（2.3-3.8×）；
      
      (3) GPQA 居中——graduate-level QA 涉及多步科学推理但为多选题 format（答案段短），
      reasoning 部分复杂度介于两者之间。ratio 6.3-8.1× 满足 ≥5× 的 best 阈值。
      
      物理解释：GPQA 的 scientific reasoning 涉及领域知识检索和逻辑链推理，importance 
      score 对这些 pattern 的编码比 random 有明显优势（score collapse 使 importance 退化
      但仍保留部分 phase-dependent 判别力），但不如 MATH-500 中长推理链的累积优势大。
      
      Random baseline 在 GPQA s025+ 产生可测 compound effect（p<0.05），但 magnitude 
      远小于 importance——与 DS/QW 在 MATH-500 n=500 上 random s025 显著但 ratio 15-38× 
      的模式定性一致。
    tables:
      - name: "Strategy Specificity Ratio Across Benchmarks"
        columns: [benchmark, ratio_range, interpretation, reasoning_chain_complexity]
        rows:
          - [MATH-500, "15-36×", very_high, "长复杂链（竞赛数学）"]
          - [GPQA, "6.3-8.1×", high, "中等链（科学推理多选）"]
          - [GSM8K, "2.3-3.8×", moderate, "短规律链（小学算术）"]
      - name: "GPQA imp/rand Ratio by Sparsity"
        columns: [sparsity, DS_imp, DS_rand, DS_ratio, QW_imp, QW_rand, QW_ratio]
        rows:
          - [s015, 0.19, 0.024, 7.9, 0.038, 0.005, 7.6]
          - [s020, 0.58, 0.072, 8.1, 0.19, 0.025, 7.6]
          - [s025, 1.72, 0.24, 7.2, 0.85, 0.12, 7.1]
          - [s030, 4.15, 0.55, 7.5, 2.28, 0.36, 6.3]
    figures_description:
      - "fig_gpqa_specificity.pdf: 双线图 DS/QW importance vs random gradient on GPQA，阴影面积标注 imp/rand ratio ≥5× zone。"
      - "fig_specificity_by_task.pdf: Bar chart 三 benchmark 的 mean ratio（MATH=25×, GPQA=7.4×, GSM=3.0×），ordered by chain complexity。"
    analysis: |
      GPQA strategy specificity 6.3-8.1× 全部超过 5× 阈值，填补了 MATH (15-36×) 和 
      GSM (2.3-3.8×) 之间的 gap。三 benchmark 形成 interpretable gradient：推理链复杂度↑ 
      → specificity ratio↑。这支持 "discrimination collapse 是 mechanism" 的 framing——
      如果是 importance metric 本身有缺陷，ratio 不应随 task difficulty 系统性变化。
      GPQA 数据使论文可以声明 "strategy specificity is a robust phenomenon (≥5×) across 
      diverse reasoning tasks"。

  - name: "Discrimination Collapse Quantitative Prediction"
    plan_id: "mechanism_gini_correlation"
    description: |
      利用已完成的 c5_per_phase_gini 和 c2_n500 数据，计算 per-phase Gini_delta 
      与 II severity 的跨模型定量相关。验证 Spearman ρ=1.0, Pearson r≥0.85。
    expected_results:
      analysis_type: "correlation of per-phase Gini collapse with II severity"
      data_source: "c5_per_phase_gini (n=30/model) + c2_n500 (n=500/model)"
      ds_within_model:
        gini_delta_low: [-0.0163, -0.0209, -0.0313, -0.0373]
        ii_median: [0.3907, 1.2149, 3.9857, 8.4813]
        spearman_rho: -1.0
        pearson_r: -0.94
        pearson_p: 0.031
      qw_within_model:
        gini_delta_low: [-0.0165, -0.0200, -0.0286, -0.0350]
        ii_median: [0.0659, 0.3073, 1.0745, 3.1550]
        spearman_rho: -1.0
        pearson_r: -0.96
        pearson_p: 0.022
      cross_model_pooled:
        n_datapoints: 8
        spearman_rho: -0.90
        pearson_r: -0.86
        pearson_p: 0.003
      cv_correlation:
        ds_cv_vs_ii_spearman: -1.0
        qw_cv_vs_ii_spearman: -1.0
        cross_model_cv_pearson: -0.88
    result_rationale: |
      Gini delta 和 II 的相关性有坚实的因果机制：head pruning → 剩余 head 的 importance 
      score 分布更均匀（Gini 下降）→ importance-based eviction 丧失判别力 → eviction 近似
      随机 → compound interaction 增大。因此 |Gini 下降| 应与 II severity 正相关。
      
      (1) DS low-phase Gini delta [-0.016→-0.037] 与 II [0.39→8.48] 完美单调共变
      （Spearman ρ=-1.0 因为 Gini 是负值——更负=更大 collapse=更大 II）。
      Pearson r=-0.94 因两者均近似幂律增长但指数不同。
      
      (2) QW 同样单调（Gini [-0.017→-0.035]，II [0.066→3.155]），Pearson r 略高(-0.96)
      因为 QW 的 II 增长在 log-scale 更接近线性。
      
      (3) 跨模型 pooling (8 points) r=-0.86——DS 和 QW 共享正趋势但斜率不同（DS 单位 
      Gini 下降对应更大 II 增加），反映 Gini→II 传递函数是 architecture-dependent 的，
      但方向和 monotonicity 是 universal 的。
      
      数据已存在（c5_per_phase_gini + c2_n500），仅需分析脚本。
    tables:
      - name: "Gini-II Correlation Summary"
        columns: [scope, Spearman_ρ, Pearson_r, p_value]
        rows:
          - ["DS within-model", -1.0, -0.94, 0.031]
          - ["QW within-model", -1.0, -0.96, 0.022]
          - ["Cross-model pooled (n=8)", -0.90, -0.86, 0.003]
    figures_description:
      - "fig_gini_ii_scatter.pdf: |Gini_delta| vs II_median (log y-axis)，DS 圆/QW 方，按 sparsity 着色。回归线及 r² 标注。"
    analysis: |
      Within-model Spearman ρ=1.0（完美单调）排除了 "Gini 下降但 II 不增加" 的反例。
      Cross-model r=-0.86 (p=0.003) 远超 r≥0.7 阈值。论文 §5 可声明 "Gini decline 
      quantitatively predicts interaction severity (cross-model r=0.86, p=0.003)"，
      将 discrimination collapse 从 qualitative hypothesis 提升至 quantitative predictor。

  - name: "C8 Status Upgrade: confirmed"
    plan_id: "c8_upgrade"
    description: |
      基于 c8_llama_n250_fixed 结果，将 C8 从 partially_confirmed 升级为 confirmed。
      更新论文措辞和 claim table。
    expected_results:
      c8_old_status: partially_confirmed
      c8_new_status: confirmed
      language_changes:
        remove: ["suggests", "provides partial support", "architecture-dependent caveat"]
        add: ["confirms strategy×phase interaction across architectures", "medium effect size (d_z=0.52)"]
      limitation_retained: "magnitude differs across architectures (LLaMA d_z=0.52 vs Qwen2 d_z=0.80)"
      paper_abstract_update: "can claim 'generalizes across architectures' without hedging"
    result_rationale: |
      C8 升级的三个充分条件在 best tier 下全部满足：
      (1) imp_vs_rand d_z ≥ 0.4 at s030 → ✓ (0.52, medium effect)
      (2) ≥2 sparsity Bonferroni significant → ✓ (3/4 显著)
      (3) random phase gradient 不再 Bonferroni significant → ✓ (0/4 显著)
      
      n=50 时的 "architecture-dependent" caveat 源于两个 anomaly：(a) imp_vs_rand 弱
      (仅 s030 p=0.029)；(b) random 也显示 phase gradient (d_z=0.35-0.44)。
      n=250 同时解决了两者——(a) 3 水平显著，(b) random 衰减至 negligible。
      这说明 n=50 的 anomaly 是统计功效不足 + 小样本变异性的产物，不是 architecture 
      本身的差异。Strategy×phase interaction 是跨架构的 general phenomenon。
    tables: []
    figures_description: []
    analysis: |
      C8 confirmed 使论文 claim table 全部为 confirmed（除 C5b future_work 和 C4 
      partially_confirmed）。核心贡献 "strategy×phase interaction generalizes across 
      architectures" 无需 hedging，EMNLP reviewer 不能以 "only works on one architecture" 
      dismiss。

  - name: "C9 Related Work Gap Analysis"
    plan_id: "c9_related_work"
    description: |
      §2 Related Work 写作——定位与 Lethe/SparK/ThinKV/Physics of KV/HIES/R-KV 的区分。
      纯分析写作任务，无计算。
    expected_results:
      output_type: manuscript_section
      positioning: |
        唯一同时分析 pruning × eviction compound interaction 如何随 reasoning phase 
        和 eviction strategy 变化的工作。三维 (compound × phase × strategy) 交互分析
        是 unique contribution。
      gap_matrix:
        Lethe: "adaptive method; no compound×phase analysis"
        SparK: "compound but uniform; no phase modulation"
        ThinKV: "single-axis phase-aware; no compound interaction"
        Physics_of_KV: "compression-rate phase transition (different 'phase' semantics)"
        HIES: "single-axis score collapse; no compound amplification"
        R-KV: "task-specific optimization; not mechanistic analysis"
    result_rationale: |
      C9 是 writing task。在 best tier 下 positioning 清晰无争议——没有 prior work 同时
      分析三个维度。关键区分：our "phase" = reasoning phase（temporal），Physics of KV 
      "phase" = compression-rate critical point（parametric）——语义正交。
      HIES 的 score collapse 发现反而是 supporting evidence，不是 prior art。
    tables: []
    figures_description: []
    analysis: "§2 通过 6 篇工作的精确区分完成 novelty positioning。无需额外实验。"
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ec5ae8e-398d-4cde-8af4-7957c34c013d",
  "isSidechain": false,
  "requestId": "req_011Cb6TUAfTgYNssiXtnitf6",
  "type": "assistant",
  "uuid": "bc0d9e9c-e14d-4e4e-91fa-d3b2bccee568",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "8ea52053-5c5d-477c-85fd-15c4d095d3f8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0143PvZiTuikEYUycCEmQTVs",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1528,
      "cache_read_input_tokens": 93840,
      "output_tokens": 9839,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1528,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9839,
          "cache_read_input_tokens": 93840,
          "cache_creation_input_tokens": 1528,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1528
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

_source line 41_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：LLaMA n=250 揭示 n=50 功效不足掩盖了中等 strategy×phase 交互；GPQA 确认跨 task 泛化且 strategy specificity 强。三维交互叙事完全成立。 核心假设：['LLaMA imp_vs_rand d_z 在 n=50 被噪声衰减；n=250 揭示真实中等…",
  "leafUuid": "bc0d9e9c-e14d-4e4e-91fa-d3b2bccee568",
  "sessionId": "8ea52053-5c5d-477c-85fd-15c4d095d3f8"
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "ai-title",
  "aiTitle": "Phase-gated compound sparsity validation at scale",
  "sessionId": "8ea52053-5c5d-477c-85fd-15c4d095d3f8"
}
```

---
