# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：C5 pilot 边缘或失败（LLaMA 方向对但 gate 未达标），n=500 Qwen s015 仍跨零但正向趋势明显，需调整 claims 

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-3/589e47f3-a107-4a46-857a-74855f584341.jsonl`
- **Structured JSON:** [`76298e9d1b26f1c59514.json`](../../sessions/76/76298e9d1b26f1c59514.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T14:42:33.526Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T14:42:33.526Z",
  "sessionId": "589e47f3-a107-4a46-857a-74855f584341",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：C5 pilot 边缘或失败（LLaMA 方向对但 gate 未达标），n=500 Qwen s015 仍跨零但正向趋势明显，需调整 claims 强度\n核心假设：['C5 LLaMA-8B 显示正向 phase gradient 但回收 <30%（或 crossover 方向对但不显著）', 'C2 n=500 后 Qwen s015 CI 仍跨零，但点估计稳定正向（median diff ~0.04-0.05）', 'DeepSeek n=500 结果与现有 n=50 一致，无意外', 'Discrimination collapse Gini/CV 在可用架构上方向一致']\n关键指标范围：{'c5_llama_paired_median_diff_s025': [0.2, 1.0], 'c5_llama_cohens_d_s025': [0.15, 0.5], 'c5_llama_crossover_present': ['ambiguous'], 'c2_qw_s015_n500_ci_lower': [-0.01, 0.01], 'c2_qw_s015_n500_median_diff': [0.03, 0.06], 'c2_ds_n500_ci_width_reduction_pct': [15, 35], 'c2_ds_s015_n500_median_diff': [0.25, 0.35], 'confirmed_arch_families': [1]}\n叙事方向：调整 claims 强度：C5 降级为 \"preliminary evidence / suggestive pilot\" 放入 §5 Discussion 而非 §4 Results 主体，或作为 Appendix 补充证据。 C2 叙事改为 threshold framing：\"compound effect emerges above threshold sparsity (~s020)\"，Qwen s015 作为 boundary condition 讨论。 Title 去掉 \"across architectures\"，改为强调 Qwen-family 内的 cross-model replication（distillation vs instruction tuning）。RC1 诚实承认 同架构局限，以 mechanism 的 architecture-agnostic 性质作为间接论证。 贡献收缩为：(1) 发现 + 同架构跨训练验证，(2) 量化 gradient（threshold-dependent）， (3) discrimination collapse 机制。仍是 solid EMNLP empirical finding paper。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: phase-gated-compound-sparse\nfocus: D052 调整后的完整 plan：C5 pilot-first 跨架构验证、C2 n=500 预注册叙事、C7/C8 写作任务、Lethe/SparK 区分。重点关注：(1) pilot-first 策略是否足够支撑泛化性 claim；(2) C7/C8 作为写作任务是否被审稿人视为弱点；(3) 11 天 deadline 下 plan 可行性\n\n## paper_framing.md\n\n# Paper Framing — Phase-Gated Compound Sparsity\n\n> 最后更新: 2026-05-14 (D052 审稿应对调整) | 维护者: Director\n\n## Core Insight\n\nCompound sparsity（attention head pruning + KV cache eviction）的 severity 不是固定常数——它是 eviction strategy 和 reasoning phase 交互的涌现属性。Importance-based eviction 的 compound interaction severity（paired median difference: median(II_low_i − II_high_i)）随 sparsity 单调递增（DeepSeek: 0.32→1.15→3.97→9.94; Qwen: 0.048→0.208→1.109→2.619），而 random masking 三相 II 持平（7/8 FAIL; Qwen s030 PASS p=0.012 but d=-0.04 negligible）。Cohen's d（paired d_z, B=10000）从 small-medium 到 large（DeepSeek: 0.44→0.80; Qwen: 0.28→1.02，s015 边缘）。这一发现挑战了 compound degradation 均匀分布的隐含假设。\n\n**数字基准**：所有数字基于 bf16 per-problem paired 统计量（B=10000 bootstrap）。median_diff 定义为 median(II_low_i − II_high_i)（逐 problem 配对差的中位数）。fp16 旧数据已弃用。\n\n## Narrative Arc\n\nCompound sparsity 是高效 LLM 推理的实用部署需求，但 prior work（SparK, Ada-KV, SLiM）将 compound interaction 视为均匀超可加。我们发现 severity 是 strategy × phase 交互的涌现属性：importance eviction 的 compound interaction 在 low-sparsity phase 远大于 high-sparsity phase（paired median difference 单调递增 0.32→9.94），而 random eviction 在所有 phase 保持平坦（7/8 FAIL; 唯一例外 Qwen s030 p=0.012 效应量可忽略 d=-0.04）。Cross-model replication 方向一致（Qwen magnitude ~1/4 of DeepSeek，onset threshold s≥0.20）。C3 crossover 现象的 LLaMA 架构验证已列入计划（plan_009 pilot-first），以测试发现的跨架构泛化性。我们通过 discrimination collapse 机制解释这一现象：head pruning → importance score 的判别力崩塌（Gini/CV 下降跨模型一致）→ importance eviction 退化为有偏伪随机。Attention entropy redistribution 作为 model-dependent secondary effect 在 DeepSeek 上观察到，但在 Qwen 上不稳健（D044）。\n\n**Framing 硬约束（D015）**：\n- MUST: \\\"emergent phase-strategy interaction\\\"\n- MUST NOT: \\\"importance metric limitation / importance is broken\\\"\n- MUST NOT: claim \\\"importance masking produces super-additive interaction\\\" without qualifier — random masking also produces positive II. The distinguishing signal is **phase-dependent gradient** (importance: paired median difference 0.32→9.94 单调递增 vs random: 7/8 FAIL), not the existence of super-additivity itself (D023)\n\n## Core Claims\n\n| ID | Claim | Status | Key Evidence |\n|----|-------|--------|-------------|\n| C1 | Compound sparsity severity is strategy-dependent | confirmed | importance paired median diff 0.32→9.94 单调递增 vs random 7/8 FAIL (bf16; Qwen s030 PASS p=0.012 d=-0.04 negligible) |\n| C2 | Severity is phase-modulated (amplified in low-sparsity phase) | confirmed | bf16 paired median difference 单调递增: 0.32→1.15→3.97→9.94; Bonferroni p<0.005 全 4 水平 (D032)。预注册：n=500 后若 QW s015 CI 仍跨零，叙事改为 'compound effect emerges above threshold sparsity (~s020)' |\n| C3 | Phase-strategy crossover exists | confirmed | s=0.25: importance high_phase=0.032 < random=0.818, importance low_phase=7.196 > random=1.363 (bf16) |\n| C4 | Discrimination collapse as primary mechanism; entropy redistribution model-dependent | partially_confirmed | D044: Gini/CV 下降跨模型一致; entropy collapse DeepSeek 一致但 Qwen s025 反转(+0.045) s030≈0。30/30 problems completed. |\n| C5 | Phase-modulated compound severity generalizes across architectures | pilot_pending | Pilot-first: 2h oracle + heuristic (token position ratio as phase proxy) on LLaMA-8B, s025/s030. Gate: recover >30% compound degradation → full rollout; else → future work. Must include heuristic baseline (oracle upper bound + simple heuristic lower bound). |\n| C6 | Severity gradient is sub-exponential | confirmed | Growth rate decreasing: Δ增长因子 3.8×→4.8×→2.0×（递减） |\n| C7 | Abstract 精简至 150-200 词，突出核心发现（原 S3 升级） | action_required | 当前 ~600 词信息过载，需精简至 1-2 个关键定量结果。写作任务，无需实验。 |\n| C8 | II 与已有 super-additivity 概念明确区分（原 S7 升级） | action_required | §3 Methodology 加段讨论 II vs SparK/SLiM/UniComp 的 compound interaction 度量区别。写作+分析任务。 |\n\n## Anticipated Reviewer Concerns\n\n### RC1: Generalizability — 7B models only, single benchmark\n- **预期质疑**: \"Results on two 7B models and MATH-500 only. How do we know this generalizes to larger models or other reasoning tasks?\"\n- **应对**: Cross-model replication (DeepSeek-R1-Distill-Qwen-7B + Qwen2.5-7B-Instruct) 控制架构变量、隔离训练方式影响（distillation vs instruction tuning）。注意：两模型共享 Qwen2ForCausalLM 架构，不能 claim 跨架构泛化。MATH-500 是 standard benchmark。Limitations 必须诚实声明：(1) 同架构不同训练，不是跨架构；(2) 7B scale only；(3) 单 benchmark。机制解释 (discrimination collapse) 原则上 architecture-agnostic，但未实证验证。\n- **实验支撑**: C5 (Qwen cross-model). 若需加强可扩展到不同架构（如 LLaMA/Mistral），但 11 天 deadline 内不现实\n\n### RC2: Mechanism — entropy-discrimination collapse 缺乏直接测量\n- **预期质疑**: \"The mechanism is conceptual. Where is the empirical evidence for entropy increase and discrimination collapse?\"\n- **应对**: c4_entropy 实验已完成（DeepSeek 30/30 + Qwen 30/30）。D044 结论：Gini/CV 下降跨模型一致（discrimination collapse confirmed）；entropy redistribution 在 DeepSeek 上一致但在 Qwen 上 s025 方向反转、s030 近零（model-dependent）。论文以 discrimination collapse 为主线，entropy 作 DeepSeek 特有的强化因素。\n- **实验支撑**: c4_entropy (DeepSeek DONE) + qwen_c4_entropy (DONE, negative for entropy universality)\n\n### RC3: Practical impact — 没有 throughput 数据\n- **预期质疑**: \"No wall-clock or throughput measurements. Is the severity amplification reflected in actual inference speed?\"\n- **应对**: 本文定位是 empirical finding paper（发现 + 机制解释），不是 method paper。Throughput 不是 claim 的一部分。Discussion 中明确 phase-gated controller 作为 future direction。\n- **实验支撑**: 不需要额外实验\n\n### RC4: Statistical rigor — bootstrap 是否足够\n- **预期质疑**: \"Per-problem bootstrap with 50 problems — sufficient sample size?\"\n- **应对**: bf16 使用 B=10000 per-problem paired bootstrap，有效配对数 n=49 (DeepSeek) / n=46 (Qwen)。Permutation test 使用 paired median difference 作为 robust statistic（D032），Bonferroni 校正后全 4 水平 p<0.005。Cohen's d（paired d_z）作为辅助效应量（DeepSeek 0.44→0.80, Qwen 0.28→1.02）。可在 appendix 补充 per-problem 分布图（已生成 fig4_per_problem_dist.pdf）。\n- **实验支撑**: bf16 permutation test (D032) + Cohen's d per-problem paired (rebootstrap B=10000) 已完成\n\n### RC5: Novelty — prior work 是否已覆盖 phase-dependent sparsity\n- **预期质疑**: \"ThinKV and phase-aware methods already consider phase. What's new?\"\n- **应对**: Prior work 在单轴上分析 phase（ThinKV: phase-aware eviction）或 compound（SparK: joint compression）。没有工作同时分析 compound × phase × strategy 的三维交互。Crossover 现象（同一 strategy 在不同 phase 方向反转）是全新发现。Related Work 加 Lethe 引用区分 + SparK 对比。\n- **实验支撑**: C3 (crossover), Related Work §2 的 gap 分析\n\n## Paper Positioning\n\n**类型**: Empirical finding paper（非 method paper）\n**核心贡献**:\n1. 发现 compound sparsity severity 的 strategy × phase 交互\n2. 量化 severity gradient（bf16 paired median difference 0.32→9.94, Cohen's d 0.44→0.80）和 crossover 现象\n3. 提出 discrimination collapse 机制解释（Gini/CV 跨模型一致；entropy redistribution model-dependent）\n4. Cross-model replication 验证泛化性\n\n**投稿目标**: EMNLP 2026 ARR, deadline 2026-05-25\n**Rebuttal 准备**: Day 9 (2026-05-23) 预留 rebuttal letter 写作时间\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_interaction_index_profiling\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_ii_profiling_v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    mvp_verdict: PASS_technical_but_negative_hypothesis\n    ci_nonoverlap: true\n    sign_reversal: false\n    ii_reasoning_0.3: 17.79\n    ii_reasoning_0.3_ci:\n    - 4.09\n    - 38.76\n    ii_transition_0.3: 3.06\n    ii_transition_0.3_ci:\n    - 0.01\n    - 5.6\n    ii_reasoning_0.5: 468.9\n    ii_transition_0.5: 850.07\n    ii_execution_0.3: Inf\n    phase_distribution:\n      execution: 1.2%_25seg\n      reasoning: 8.1%_96seg\n      transition: 90.7%_192seg\n    total_tokens: 86207\n    all_ii_superadditive: true\n    amplitude_ratio_reas_vs_trans_0.3: 5.81\n    gmm_best_k: 5\n    gmm_means:\n    - 0.438\n    - 0.597\n    - 0.719\n    - 0.816\n    - 0.892\n    gmm_weights:\n    - 0.062\n    - 0.14\n    - 0.208\n    - 0.282\n    - 0.309\n    sparsity_global:\n      mean: 0.7653\n      std: 0.1364\n      median: 0.8004\n    quantile_boundaries:\n    - 0.7337\n    - 0.8482\n- exp_id: mvp_ii_profiling_v3\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    mvp_verdict: FAIL\n    ci_nonoverlap: false\n    sign_reversal: false\n    phase_distribution_balanced: true\n    ii_high_0.1:\n      mean: 0.2317\n      ci:\n      - 0.1338\n      - 0.3418\n    ii_low_0.1:\n      mean: 0.1711\n      ci:\n      - 0.0782\n      - 0.2768\n    ii_mid_0.1:\n      mean: 0.1607\n      ci:\n      - 0.0886\n      - 0.2489\n    ii_high_0.2:\n      mean: 2.1574\n      ci:\n      - 1.0605\n      - 3.5491\n    ii_low_0.2:\n      mean: 1.1294\n      ci:\n      - 0.4368\n      - 1.9593\n    ii_mid_0.2:\n      mean: 0.3049\n      ci:\n      - -1.0635\n      - 1.3044\n    total_tokens: 86207\n    no_nan_inf: true\n    segments:\n      high: 511\n      low: 454\n      mid: 391\n- exp_id: mvp_ii_profiling_v4\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_ii_profiling_v4b\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_ii_profiling_v4c\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_ii_profiling_v4d\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_ii_profiling_v4-random\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_v4a_r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_v4b_r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_v4c_r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_v4_random_r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: mvp_v4_legacy_s01\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    II_high_0.1:\n      mean: -0.1097\n      ci_low: -0.8066\n      ci_high: 0.41\n    II_mid_0.1:\n      mean: -15.966\n      ci_low: -47.991\n      ci_high: 1.288\n    II_low_0.1:\n      mean: 0\n      ci_low: 0\n      ci_high: 0\n    ppl_high_dense: 1.1462\n    ppl_high_both: 22.1302\n    ppl_mid_dense: 1.1226\n    ppl_mid_both: 47.5856\n    verdict: FAIL\n- exp_id: mvp_v4_legacy_s02\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_0.2:\n      mean: 21.2856\n      ci:\n      - 0.0292\n      - 63.163\n    ii_mid_0.2:\n      mean: 21.8743\n      ci:\n      - 4.9863\n      - 41.785\n    ii_low_0.2:\n      mean: 0\n      ci:\n      - 0\n      - 0\n    ppl_high:\n      dense: 1.15\n      attn: 1.32\n      kv: 104.42\n      both: 63.41\n    ppl_mid:\n      dense: 1.12\n      attn: 1.29\n      kv: 324.16\n      both: 170.47\n    ppl_low:\n      dense: 1.11\n      attn: 1.3\n      kv: 1.11\n      both: 1.3\n    problems_completed: 50\n    phase_tokens:\n      high: 25862\n      mid: 27996\n      low: 32349\n    mvp_verdict: PASS\n- exp_id: mvp_v4_legacy_s03\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_0.3:\n      mean: -224.5\n      ci_crosses_zero: true\n    verdict: FAIL_ci_crosses_zero\n- exp_id: mvp_v4_legacy_s025\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_v4_legacy_s035\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: mvp_v4_float32_s030\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_v5_fixed_s020\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    ii_high: 0.5\n    ii_mid: 3.52\n    ii_low: 31.89\n    ii_high_ci:\n    - 0.41\n    - 0.62\n    ii_mid_ci:\n    - 2.29\n    - 5.35\n    ii_low_ci:\n    - 18.74\n    - 47.22\n    ii_high_median: 0.33\n    ii_mid_median: 1.55\n    ii_low_median: 9.56\n    kv_ppl_high: 1.24\n    kv_ppl_mid: 3.65\n    kv_ppl_low: 14.11\n    both_ppl_high: 2.7\n    both_ppl_mid: 8.13\n    both_ppl_low: 42.64\n    problems: 50\n    ⚠️_WARNING: pre-fix code, INVALIDATED. Results found on disk after kill but code\n      lacked conda activation fix. Do NOT cite these numbers.\n- exp_id: mvp_v5_fixed_s030\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    ii_high: 1.18\n    ii_mid: 168.53\n    ii_low: 1926.23\n    ii_high_ci:\n    - 0.86\n    - 1.6\n    ii_mid_ci:\n    - 36.91\n    - 348.21\n    ii_low_ci:\n    - 179.17\n    - 4062.57\n    ii_high_median: 0.6\n    ii_mid_median: 7.47\n    ii_low_median: 44.63\n    kv_ppl_high: 1.4\n    kv_ppl_mid: 15.11\n    kv_ppl_low: 40.79\n    both_ppl_high: 5.71\n    both_ppl_mid: 137.61\n    both_ppl_low: 963.2\n    problems: 50\n    ⚠️_WARNING: pre-fix code, INVALIDATED. Results found on disk after kill but code\n      lacked conda activation fix. Do NOT cite these numbers.\n- exp_id: mvp_v5_fixed_s015\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ii_high: 0.306\n    ii_mid: 1.274\n    ii_low: 8.786\n    ii_high_ci:\n    - 0.256\n    - 0.359\n    ii_mid_ci:\n    - 0.895\n    - 1.749\n    ii_low_ci:\n    - 5.294\n    - 12.684\n    ii_high_median: 0.205\n    ii_mid_median: 0.696\n    ii_low_median: 2.627\n    ii_high_winsorized: 0.289\n    ii_mid_winsorized: 1.139\n    ii_low_winsorized: 8.408\n    kv_ppl_high: 1.2147\n    kv_ppl_mid: 2.1276\n    kv_ppl_low: 6.7451\n    both_ppl_high: 2.2835\n    both_ppl_mid: 3.9408\n    both_ppl_low: 16.9987\n    problems: 50\n    segments: 1356\n- exp_id: mvp_v5_fixed_s025\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ii_high: 0.851\n    ii_mid: 9.306\n    ii_low: 96.715\n    ii_high_ci:\n    - 0.703\n    - 0.999\n    ii_mid_ci:\n    - 6.092\n    - 13.303\n    ii_low_ci:\n    - 59.642\n    - 143.188\n    ii_high_median: 0.584\n    ii_mid_median: 4.522\n    ii_low_median: 30.903\n    ii_high_winsorized: 0.802\n    ii_mid_winsorized: 8.156\n    ii_low_winsorized: 94.931\n    kv_ppl_high: 1.3108\n    kv_ppl_mid: 6.1778\n    kv_ppl_low: 23.8919\n    both_ppl_high: 3.4623\n    both_ppl_mid: 16.4148\n    both_ppl_low: 104.1749\n    problems: 50\n    segments: 1356\n- exp_id: mvp_v5_fixed_s020_r2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ii_high_median: 0.3333\n    ii_mid_median: 1.5479\n    ii_low_median: 9.5627\n    ii_high_mean: 0.5044\n    ii_mid_mean: 3.5155\n    ii_low_mean: 31.8937\n    ii_high_ci:\n    - 0.41\n    - 0.62\n    ii_mid_ci:\n    - 2.29\n    - 5.35\n    ii_low_ci:\n    - 18.74\n    - 47.22\n    kv_ppl_high: 1.24\n    kv_ppl_mid: 3.65\n    kv_ppl_low: 14.11\n    both_ppl_high: 2.7\n    both_ppl_mid: 8.13\n    both_ppl_low: 42.64\n    problems: 50\n- exp_id: mvp_v5_fixed_s030_r2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ii_high_median: 0.5964\n    ii_mid_median: 7.4671\n    ii_low_median: 44.6324\n    ii_high_mean: 1.1832\n    ii_mid_mean: 168.53\n    ii_low_mean: 1926.23\n    ii_high_ci:\n    - 0.86\n    - 1.6\n    ii_mid_ci:\n    - 36.91\n    - 348.21\n    ii_low_ci:\n    - 179.17\n    - 4062.57\n    kv_ppl_high: 1.4\n    kv_ppl_mid: 15.11\n    kv_ppl_low: 40.79\n    both_ppl_high: 5.71\n    both_ppl_mid: 137.61\n    both_ppl_low: 963.2\n    problems: 50\n- exp_id: mvp_v5_random_s015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 0.1606\n    ii_mid_median: 0.252\n    ii_low_median: 0.1831\n    ii_high_mean: 0.4563\n    ii_mid_mean: 0.5134\n    ii_low_mean: 0.4775\n    ii_high_ci:\n    - 0.12\n    - 0.77\n    ii_mid_ci:\n    - 0.34\n    - 0.74\n    ii_low_ci:\n    - 0.28\n    - 0.7\n    kv_ppl_high: 3.14\n    kv_ppl_mid: 2.91\n    kv_ppl_low: 3.61\n    both_ppl_high: 3.92\n    both_ppl_mid: 4.14\n    both_ppl_low: 4.71\n    problems: 50\n- exp_id: mvp_v5_random_s025\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 3.0024\n    ii_mid_median: 2.9846\n    ii_low_median: 2.9146\n    ii_high_mean: 3.9052\n    ii_mid_mean: 7.9491\n    ii_low_mean: 3.9114\n    ii_high_ci:\n    - 0.98\n    - 6.34\n    ii_mid_ci:\n    - 4.67\n    - 11.87\n    ii_low_ci:\n    - 2.71\n    - 5.24\n    kv_ppl_high: 6.39\n    kv_ppl_mid: 6.11\n    kv_ppl_low: 9.07\n    both_ppl_high: 17.06\n    both_ppl_mid: 15.38\n    both_ppl_low: 29.32\n    problems: 50\n- exp_id: mvp_v5_random_s020\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 0.321331\n    ii_mid_median: 0.455663\n    ii_low_median: 0.591916\n    ii_high_mean: 0.855584\n    ii_mid_mean: 1.258123\n    ii_low_mean: 0.956933\n    ii_high_ci:\n    - -0.124133\n    - 1.616883\n    ii_mid_ci:\n    - 0.674852\n    - 2.075565\n    ii_low_ci:\n    - 0.583856\n    - 1.413355\n    kv_ppl_high: 4.2537\n    kv_ppl_mid: 4.3064\n    kv_ppl_low: 5.4048\n    both_ppl_high: 7.9749\n    both_ppl_mid: 6.8553\n    both_ppl_low: 22.5868\n    problems: 50\n- exp_id: mvp_v5_random_s030\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 5.377512\n    ii_mid_median: 5.886454\n    ii_low_median: 3.776818\n    ii_high_mean: 22.734534\n    ii_mid_mean: 10.943319\n    ii_low_mean: 11.840449\n    ii_high_ci:\n    - 10.352118\n    - 42.551951\n    ii_mid_ci:\n    - 7.398611\n    - 14.765315\n    ii_low_ci:\n    - 4.097309\n    - 23.545273\n    kv_ppl_high: 8.1027\n    kv_ppl_mid: 8.5701\n    kv_ppl_low: 13.4922\n    both_ppl_high: 41.3452\n    both_ppl_mid: 24.1992\n    both_ppl_low: 68.5301\n    problems: 50\n- exp_id: v6_importance_s025\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 0.6641\n    ii_mid_median: 5.3067\n    ii_low_median: 24.1619\n    ii_high_mean: 0.8842\n    ii_mid_mean: 10.057\n    ii_low_mean: 71.8854\n    per_problem_ii_count: 50\n    n_high: 42\n    n_mid: 23\n    n_low: 21\n    problems: 50\n    bootstrap_gradient_paired: 35.72\n    bootstrap_ci_paired:\n    - 9.52\n    - 101.54\n    bootstrap_gradient_unpaired: 36.38\n    bootstrap_ci_unpaired:\n    - 13.19\n    - 97.61\n    bootstrap_p: 0\n- exp_id: v6_importance_s030\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 0.8833\n    ii_mid_median: 7.2706\n    ii_low_median: 34.6937\n    ii_high_mean: 1.5151\n    ii_mid_mean: 78.8215\n    ii_low_mean: 1163.9677\n    per_problem_ii_count: 50\n    n_high: 40\n    n_mid: 22\n    n_low: 20\n    problems: 50\n    bootstrap_gradient_paired: 41.92\n    bootstrap_ci_paired:\n    - 19.14\n    - 299.76\n    bootstrap_gradient_unpaired: 39.28\n    bootstrap_ci_unpaired:\n    - 21.87\n    - 129.59\n    bootstrap_p: 0\n- exp_id: v6_importance_s015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 0.2266\n    ii_mid_median: 0.7432\n    ii_low_median: 2.8762\n    ii_high_mean: 0.2874\n    ii_mid_mean: 1.6858\n    ii_low_mean: 8.5161\n    per_problem_ii_count: 50\n    n_high: 43\n    n_mid: 32\n    n_low: 24\n    problems: 50\n    bootstrap_gradient_paired: 11.53\n    bootstrap_ci_paired:\n    - 3.49\n    - 23.78\n    bootstrap_gradient_unpaired: 12.69\n    bootstrap_ci_unpaired:\n    - 4.96\n    - 28.45\n    bootstrap_p: 0\n- exp_id: v6_importance_s020\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 0.3353\n    ii_mid_median: 1.6733\n    ii_low_median: 9.2538\n    ii_high_mean: 0.4936\n    ii_mid_mean: 4.9538\n    ii_low_mean: 25.8764\n    per_problem_ii_count: 50\n    n_high: 42\n    n_mid: 28\n    n_low: 21\n    problems: 50\n    bootstrap_gradient_paired: 11.05\n    bootstrap_ci_paired:\n    - 5.42\n    - 69.27\n    bootstrap_gradient_unpaired: 27.6\n    bootstrap_ci_unpaired:\n    - 6.55\n    - 75.16\n    bootstrap_p: 0\n- exp_id: qwen_importance_s015\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: qwen_importance_s020\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: qwen_importance_s025\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: qwen_importance_s030\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: v6_random_s015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 0.1606\n    ii_mid_median: 0.252\n    ii_low_median: 0.1831\n    ii_high_mean: 0.4563\n    ii_mid_mean: 0.5134\n    ii_low_mean: 0.4775\n    per_problem_ii_count: 50\n    n_high: 43\n    n_mid: 32\n    n_low: 28\n    bootstrap_gradient_paired: -0.2722\n    bootstrap_ci_paired:\n    - -0.7039\n    - 0.1548\n    bootstrap_p: 0.903\n    bootstrap_gradient_unpaired: -0.0592\n    bootstrap_ci_unpaired:\n    - -0.5341\n    - 0.3877\n    per_problem_ii_stats:\n      high:\n        min: -3.0621\n        max: 5.018\n        mean: 0.5386\n        median: 0.2003\n        std: 1.2085\n      mid:\n        min: -2.7245\n        max: 4.6713\n        mean: 0.3977\n        median: 0.299\n        std: 1.1456\n      low:\n        min: -0.4031\n        max: 3.7005\n        mean: 0.4806\n        median: 0.2465\n        std: 0.779\n    verdict: FAIL\n- exp_id: v6_random_s020\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_mean: 0.855584\n    ii_high_median: 0.321331\n    ii_high_ci:\n    - -0.124133\n    - 1.616883\n    ii_high_winsorized_mean: 0.913496\n    ii_mid_mean: 1.258123\n    ii_mid_median: 0.455663\n    ii_mid_ci:\n    - 0.674852\n    - 2.075565\n    ii_mid_winsorized_mean: 1.074102\n    ii_low_mean: 0.956933\n    ii_low_median: 0.591916\n    ii_low_ci:\n    - 0.583856\n    - 1.413355\n    ii_low_winsorized_mean: 0.96113\n    n_high: 511\n    n_mid: 391\n    n_low: 454\n    problems: 50\n    per_problem_ii_count: 50\n    gradient_mean_low_over_high: 1.118\n    gradient_median_low_over_high: 1.842\n    pass_fail: FAIL\n    perplexity_high_dense: 1.1462\n    perplexity_high_both: 7.9749\n    perplexity_mid_dense: 1.1226\n    perplexity_mid_both: 6.8553\n    perplexity_low_dense: 1.1105\n    perplexity_low_both: 22.5868\n- exp_id: v6_random_s025\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ii_high_median: 3.0024\n    ii_mid_median: 2.9846\n    ii_low_median: 2.9146\n    ii_high_mean: 3.9052\n    ii_mid_mean: 7.9491\n    ii_low_mean: 3.9114\n    per_problem_ii_count: 50\n    n_high: 36\n    n_mid: 25\n    n_low: 24\n    bootstrap_gradient_paired: -0.1199\n    bootstrap_ci_paired:\n    - -1.517\n    - 1.2461\n    bootstrap_p: 0.559\n    bootstrap_gradient_unpaired: -0.8616\n    bootstrap_ci_unpaired:\n    - -3.3911\n    - 1.5169\n    per_problem_ii_stats:\n      high:\n        min: -6.1388\n        max: 25.2471\n        mean: 4.4098\n        median: 3.0421\n        std: 6.0734\n      mid:\n        min: 0.158\n        max: 108.7242\n        mean: 7.5626\n        median: 2.1407\n        std: 20.926\n      low:\n        min: -0.1953\n        max: 12.8555\n        mean: 3.5806\n        median: 2.7289\n        std: 3.4915\n    verdict: FAIL\n- exp_id: v6_random_s030\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: v6_random_s030_r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: bf16_importance_s015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: -0.150213\n        median: 0.005752\n        ci:\n        - -0.294614\n        - -0.055385\n        winsorized_mean: -0.062378\n        skewness: -14.9912\n      mid:\n        mean: 0.447301\n        median: 0.080738\n        ci:\n        - 0.267993\n        - 0.668749\n        winsorized_mean: 0.324751\n        skewness: 4.7221\n      low:\n        mean: 2.405837\n        median: 0.398291\n        ci:\n        - 1.478784\n        - 3.667675\n        winsorized_mean: 1.278857\n        skewness: 9.5402\n    per_problem_ii_stats:\n      high:\n        n: 49\n        min: -0.188061\n        max: 0.335853\n        mean: -0.013405\n        median: 0.00012\n        std: 0.078483\n      mid:\n        n: 40\n        min: -0.169092\n        max: 3.88198\n        mean: 0.308621\n        median: 0.107114\n        std: 0.690186\n      low:\n        n: 50\n        min: -0.872983\n        max: 9.10289\n        mean: 0.725504\n        median: 0.315517\n        std: 1.731056\n    gradient_paired_aggregate_legacy: 69.24\n    median_difference: 0.3925\n    n_problems: 50\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: true\n      overall: PASS\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    perplexity:\n      high:\n        dense: 1.1689\n        attn: 1.4861\n        kv: 1.4481\n        both: 1.5911\n      mid:\n        dense: 1.2269\n        attn: 1.5137\n        kv: 2.5971\n        both: 3.4541\n      low:\n        dense: 1.2286\n        attn: 1.6147\n        kv: 8.9201\n        both: 12.5084\n- exp_id: bf16_importance_s020\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 0.1289\n        median: 0.0145\n        ci:\n        - -0.1975\n        - 0.6647\n        winsorized_mean: -0.0297\n        skewness: 16.67\n      mid:\n        mean: 1.2604\n        median: 0.2027\n        ci:\n        - 0.7466\n        - 1.8962\n        winsorized_mean: 0.766\n        skewness: 7.05\n      low:\n        mean: 6.0288\n        median: 1.4963\n        ci:\n        - 4.4671\n        - 7.9237\n        winsorized_mean: 4.3426\n        skewness: 6.01\n    per_problem_ii_stats:\n      high:\n        n: 49\n        min: -0.1884\n        max: 0.4196\n        mean: 0.0025\n        median: 0.0036\n        std: 0.0966\n      mid:\n        n: 40\n        min: -0.0519\n        max: 8.6969\n        mean: 0.6795\n        median: 0.1977\n        std: 1.4998\n      low:\n        n: 50\n        min: -1.6151\n        max: 22.6875\n        mean: 2.2301\n        median: 1.128\n        std: 4.3758\n    gradient_paired_aggregate_legacy: 5.9\n    median_difference: 1.4818\n    n_problems: 50\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: false\n      overall: PASS\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    perplexity:\n      high:\n        dense: 1.1689\n        attn: 1.5233\n        kv: 1.6191\n        both: 2.1047\n      mid:\n        dense: 1.2269\n        attn: 1.5375\n        kv: 3.5164\n        both: 5.4246\n      low:\n        dense: 1.2286\n        attn: 1.6486\n        kv: 15.7987\n        both: 23.74\n- exp_id: bf16_importance_s025\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 0.302756\n        median: 0.032363\n        ci:\n        - 0.083714\n        - 0.543977\n        winsorized_mean: 0.200962\n        skewness: 4.8826\n      mid:\n        mean: 5.729665\n        median: 1.118069\n        ci:\n        - 3.455574\n        - 8.471799\n        winsorized_mean: 4.189902\n        skewness: 8.2799\n      low:\n        mean: 25.852951\n        median: 7.195958\n        ci:\n        - 19.077082\n        - 33.497293\n        winsorized_mean: 19.319103\n        skewness: 7.3986\n    per_problem_ii_stats:\n      high:\n        n: 49\n        min: -0.316321\n        max: 4.003714\n        mean: 0.133714\n        median: 0.009873\n        std: 0.595358\n      mid:\n        n: 40\n        min: -0.024794\n        max: 18.720486\n        mean: 2.537744\n        median: 1.05707\n        std: 3.962575\n      low:\n        n: 50\n        min: -1.854733\n        max: 75.467653\n        mean: 11.28281\n        median: 3.954593\n        std: 16.620011\n    gradient_paired_aggregate_legacy: 222.35\n    median_difference: 7.1636\n    n_problems: 50\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: false\n      overall: PASS\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    perplexity:\n      high:\n        dense: 1.1689\n        attn: 1.6511\n        kv: 1.8628\n        both: 2.7026\n      mid:\n        dense: 1.2269\n        attn: 1.7039\n        kv: 5.6205\n        both: 13.3436\n      low:\n        dense: 1.2286\n        attn: 1.8366\n        kv: 31.756\n        both: 63.668\n- exp_id: bf16_importance_s030\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 0.5547\n        median: 0.0534\n        ci:\n        - 0.2773\n        - 0.9198\n        winsorized_mean: 0.3367\n        skewness: 10.62\n      mid:\n        mean: 11.3\n        median: 2.2833\n        ci:\n        - 6.865\n        - 17.2633\n        winsorized_mean: 8.1752\n        skewness: 9.19\n      low:\n        mean: 57.7946\n        median: 14.6395\n        ci:\n        - 41.4416\n        - 77.0467\n        winsorized_mean: 39.3143\n        skewness: 8.31\n    per_problem_ii_stats:\n      high:\n        n: 49\n        min: -0.5095\n        max: 4.4457\n        mean: 0.1976\n        median: 0.0343\n        std: 0.6793\n      mid:\n        n: 40\n        min: -0.1989\n        max: 34.0258\n        mean: 5.2585\n        median: 1.5173\n        std: 7.9382\n      low:\n        n: 50\n        min: -7.3027\n        max: 126.7985\n        mean: 22.6601\n        median: 9.9731\n        std: 28.4096\n    gradient_paired_aggregate_legacy: 57.24\n    median_difference: 14.5861\n    n_problems: 50\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: false\n      overall: PASS\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    perplexity:\n      high:\n        dense: 1.1689\n        attn: 1.7123\n        kv: 2.0544\n        both: 3.2372\n      mid:\n        dense: 1.2269\n        attn: 1.7894\n        kv: 9.4821\n        both: 24.2847\n      low:\n        dense: 1.2286\n        attn: 1.9347\n        kv: 51.6485\n        both: 122.61\n- exp_id: bf16_random_s015\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: bf16_random_s020\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: bf16_random_s025\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: bf16_random_s030\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: bf16_qwen_importance_s015\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: bf16_qwen_importance_s020\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: bf16_qwen_importance_s025\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: bf16_qwen_importance_s030\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: v6_random_s030_r3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    II_high_mean: 9.2364\n    II_mid_mean: -230.7604\n    II_low_mean: -7.4119\n    II_high_median: 4.0237\n    II_mid_median: 2.4272\n    II_low_median: 4.735\n    ppl_low_both: 88.94\n    per_problem_count: 50\n- exp_id: bf16_ds_imp_s015\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    median_difference: 0.323579\n    permutation_p: 0\n    cohens_d: 0.6068\n    bootstrap_ci_95:\n    - 0.198824\n    - 0.471566\n    wilcoxon_p: 0\n    n_bootstrap: 10000\n    n_paired: 49\n- exp_id: bf16_ds_imp_s020\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    median_difference: 1.15202\n    permutation_p: 0\n    cohens_d: 0.725\n    bootstrap_ci_95:\n    - 0.655454\n    - 1.256001\n    wilcoxon_p: 0\n    n_bootstrap: 10000\n    n_paired: 49\n- exp_id: bf16_ds_imp_s025\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    median_difference: 3.968568\n    permutation_p: 0\n    cohens_d: 0.9534\n    bootstrap_ci_95:\n    - 2.829037\n    - 5.291756\n    wilcoxon_p: 0\n    n_bootstrap: 10000\n    n_paired: 49\n- exp_id: bf16_ds_imp_s030\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    median_difference: 9.943595\n    permutation_p: 0\n    cohens_d: 1.1263\n    bootstrap_ci_95:\n    - 8.391554\n    - 16.652865\n    wilcoxon_p: 0\n    n_bootstrap: 10000\n    n_paired: 49\n- exp_id: bf16_ds_rand_s015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 0.2208\n        median: 0.0931\n        ci:\n        - -1.0091\n        - 1.5243\n        median_ci:\n        - 0.0024\n        - 0.1515\n        winsorized_mean: 0.3161\n        skewness: -5.4\n      mid:\n        mean: -3.3604\n        median: 0.0967\n        ci:\n        - -8.4057\n        - 0.3697\n        median_ci:\n        - 0.0219\n        - 0.197\n        winsorized_mean: -0.6366\n        skewness: -10.56\n      low:\n        mean: -1.8952\n        median: 0.1026\n        ci:\n        - -4.9698\n        - 0.2741\n        median_ci:\n        - 0.044\n        - 0.1755\n        winsorized_mean: 0.0521\n        skewness: -11.57\n    perplexity:\n      high:\n        dense: 1.1687\n        attn: 3.5947\n        kv: 2.9239\n        both: 5.7569\n      mid:\n        dense: 1.2269\n        attn: 297.7957\n        kv: 2.915\n        both: 11.3156\n      low:\n        dense: 1.2284\n        attn: 11.3419\n        kv: 3.6161\n        both: 6.2886\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    n_problems: 50\n    pass_fail:\n      ci_overlap: false\n      sign_reversal: false\n      overall: FAIL\n    median_difference: 0.0095\n- exp_id: bf16_ds_rand_s020\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 1.1216\n        median: 0.2918\n        ci:\n        - 0.0796\n        - 2.5834\n        median_ci:\n        - 0.1598\n        - 0.4581\n        winsorized_mean: 1.7664\n        skewness: 9.59\n      mid:\n        mean: -1.5827\n        median: 0.3504\n        ci:\n        - -6.0963\n        - 1.5735\n        median_ci:\n        - 0.1993\n        - 0.5226\n        winsorized_mean: 0.5839\n        skewness: -12.31\n      low:\n        mean: -0.4116\n        median: 0.2763\n        ci:\n        - -2.6034\n        - 1.209\n        median_ci:\n        - 0.2194\n        - 0.5487\n        winsorized_mean: 0.9942\n        skewness: -10.07\n    perplexity:\n      high:\n        dense: 1.1687\n        attn: 3.1905\n        kv: 3.8002\n        both: 8.8129\n      mid:\n        dense: 1.2269\n        attn: 67.8504\n        kv: 3.788\n        both: 11.4974\n      low:\n        dense: 1.2284\n        attn: 8.592\n        kv: 5.0078\n        both: 9.2001\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    n_problems: 50\n    pass_fail:\n      ci_overlap: false\n      sign_reversal: false\n      overall: FAIL\n    median_difference: -0.0155\n- exp_id: bf16_ds_rand_s025\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 3.59\n        median: 0.8182\n        ci:\n        - 1.4021\n        - 6.2327\n        median_ci:\n        - 0.5075\n        - 1.7217\n        winsorized_mean: 6.3965\n        skewness: -7.57\n      mid:\n        mean: -1.8455\n        median: 0.9324\n        ci:\n        - -10.3663\n        - 4.9342\n        median_ci:\n        - 0.7331\n        - 1.7003\n        winsorized_mean: 3.1014\n        skewness: -12.76\n      low:\n        mean: 0.7212\n        median: 1.3627\n        ci:\n        - -4.2068\n        - 4.5006\n        median_ci:\n        - 1.0869\n        - 2.6866\n        winsorized_mean: 4.1866\n        skewness: -15.85\n    perplexity:\n      high:\n        dense: 1.1687\n        attn: 7.237\n        kv: 4.9751\n        both: 17.7423\n      mid:\n        dense: 1.2269\n        attn: 868.3199\n        kv: 5.1165\n        both: 29.4661\n      low:\n        dense: 1.2284\n        attn: 24.3571\n        kv: 6.7993\n        both: 17.9694\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    n_problems: 50\n    pass_fail:\n      ci_overlap: false\n      sign_reversal: false\n      overall: FAIL\n    median_difference: 0.5445\n- exp_id: bf16_ds_rand_s030\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 7.5555\n        median: 2.5031\n        ci:\n        - 4.4087\n        - 11.6199\n        median_ci:\n        - 1.3292\n        - 4.1205\n        winsorized_mean: null\n        skewness: null\n      mid:\n        mean: 6.2518\n        median: 2.5918\n        ci:\n        - 2.1767\n        - 10.4757\n        median_ci:\n        - 1.8397\n        - 3.7888\n        winsorized_mean: null\n        skewness: null\n      low:\n        mean: 6.8323\n        median: 4.0414\n        ci:\n        - 3.2428\n        - 10.6996\n        median_ci:\n        - 2.2686\n        - 6.3579\n        winsorized_mean: null\n        skewness: null\n    perplexity:\n      high:\n        dense: 1.1687\n        attn: 16.7892\n        kv: 8.8073\n        both: 40.7553\n      mid:\n        dense: 1.2269\n        attn: 2461.9219\n        kv: 8.6662\n        both: 62.4422\n      low:\n        dense: 1.2284\n        attn: 55.2916\n        kv: 11.5789\n        both: 37.6009\n    phase_stats:\n      high:\n        n_tokens: 21086\n        n_segments: 387\n      mid:\n        n_tokens: 13306\n        n_segments: 191\n      low:\n        n_tokens: 27748\n        n_segments: 397\n    n_problems: 50\n    pass_fail:\n      ci_overlap: false\n      sign_reversal: false\n      overall: FAIL\n    median_difference: 1.5383\n- exp_id: bf16_qw_imp_s015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    median_difference: 0.047619\n    permutation_p: 0.0001\n    cohens_d: 0.3705\n    bootstrap_ci_95:\n    - -0.005077\n    - 0.109517\n    wilcoxon_p: 0.02958\n    n_bootstrap: 10000\n    n_paired: 46\n- exp_id: bf16_qw_imp_s020\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    median_difference: 0.207511\n    permutation_p: 0\n    cohens_d: 0.7224\n    bootstrap_ci_95:\n    - 0.067222\n    - 0.40226\n    wilcoxon_p: 3.4e-05\n    n_bootstrap: 10000\n    n_paired: 46\n- exp_id: bf16_qw_imp_s025\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    median_difference: 1.108706\n    permutation_p: 0\n    cohens_d: 1.2329\n    bootstrap_ci_95:\n    - 0.609247\n    - 1.469002\n    wilcoxon_p: 0\n    n_bootstrap: 10000\n    n_paired: 46\n- exp_id: bf16_qw_imp_s030\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    median_difference: 2.619385\n    permutation_p: 0\n    cohens_d: 1.4394\n    bootstrap_ci_95:\n    - 1.722281\n    - 3.651063\n    wilcoxon_p: 0\n    n_bootstrap: 10000\n    n_paired: 46\n- exp_id: bf16_qw_rand_s015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 1.6652\n        median: 0.1381\n        ci:\n        - 1.0986\n        - 2.4042\n        median_ci:\n        - 0.1025\n        - 0.2074\n        winsorized_mean: 1.0044\n        skewness: 7.1842\n      mid:\n        mean: 1.6975\n        median: 0.2194\n        ci:\n        - 0.4473\n        - 3.4612\n        median_ci:\n        - -0.0048\n        - 0.6621\n        winsorized_mean: 1.4038\n        skewness: 3.2101\n      low:\n        mean: 1.4082\n        median: 0.1878\n        ci:\n        - 0.8358\n        - 2.06\n        median_ci:\n        - 0.0962\n        - 0.3139\n        winsorized_mean: 0.9403\n        skewness: 7.1113\n    perplexity:\n      high:\n        dense: 1.0737\n        attn: 1.3939\n        kv: 2.0487\n        both: 4.2076\n      mid:\n        dense: 1.1322\n        attn: 1.4175\n        kv: 2.3709\n        both: 4.6105\n      low:\n        dense: 1.1517\n        attn: 1.7177\n        kv: 3.3253\n        both: 5.4788\n    phase_stats:\n      high:\n        n_tokens: 16289\n        n_segments: 295\n      mid:\n        n_tokens: 4372\n        n_segments: 26\n      low:\n        n_tokens: 32227\n        n_segments: 276\n    n_problems: 50\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: false\n      overall: FAIL\n    median_difference: -0.029401\n    permutation_test:\n      p_value: 0.7657\n      B: 10000\n    cohens_d: -0.0507\n    bootstrap_ci_95:\n    - -0.2106\n    - 0.2124\n    wilcoxon_p: 0.862554\n    phase_median_ii:\n      high: 0.1381\n      mid: 0.2194\n      low: 0.1878\n- exp_id: bf16_qw_rand_s020\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 2.58579\n        median: 0.48549\n        ci:\n        - 1.769404\n        - 3.501692\n        median_ci:\n        - 0.304626\n        - 0.658814\n        winsorized_mean: 1.80021\n        skewness: 5.4038\n      mid:\n        mean: 5.69684\n        median: 0.76699\n        ci:\n        - 1.69004\n        - 12.276143\n        median_ci:\n        - 0.482838\n        - 3.392541\n        winsorized_mean: 4.304174\n        skewness: 3.526\n      low:\n        mean: 65.915714\n        median: 0.614438\n        ci:\n        - -18.581948\n        - 221.709429\n        median_ci:\n        - 0.484725\n        - 0.848787\n        winsorized_mean: 2.389244\n        skewness: 16.2163\n    perplexity:\n      high:\n        dense: 1.0737\n        attn: 1.6115\n        kv: 2.5041\n        both: 5.9394\n      mid:\n        dense: 1.1322\n        attn: 1.7583\n        kv: 3.0658\n        both: 10.5578\n      low:\n        dense: 1.1517\n        attn: 75.631\n        kv: 4.3535\n        both: 140.6269\n    phase_stats:\n      high:\n        n_tokens: 16289\n        n_segments: 295\n      mid:\n        n_tokens: 4372\n        n_segments: 26\n      low:\n        n_tokens: 32227\n        n_segments: 276\n    n_problems: 50\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: false\n      overall: FAIL\n    median_difference: 0.128948\n    permutation_test:\n      p_value: 0.352\n      B: 10000\n    cohens_d: 0.247\n    bootstrap_ci_95:\n    - -0.139\n    - 0.215\n    wilcoxon_p: 0.149\n    phase_median_ii:\n      high: 0.4739\n      mid: 0.8757\n      low: 0.4847\n- exp_id: bf16_qw_rand_s025\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    interaction_index:\n      high:\n        mean: 14.4213\n        median: 1.6043\n        ci:\n        - 7.1074\n        - 23.4587\n        median_ci:\n        - 0.6977\n        - 3.0736\n        winsorized_mean: 9.3765\n        skewness: 4.8263\n      mid:\n        mean: 18.6458\n        median: 2.2225\n        ci:\n        - 3.3729\n        - 41.6037\n        median_ci:\n        - 0.6093\n        - 11.5889\n        winsorized_mean: 14.2901\n        skewness: 3.8245\n      low:\n        mean: 17.7277\n        median: 2.2641\n        ci:\n        - 4.3523\n        - 37.2093\n        median_ci:\n        - 1.2218\n        - 4.8561\n        winsorized_mean: 9.9876\n        skewness: 5.7652\n    perplexity:\n      high:\n        dense: 1.0737\n        attn: 2.0183\n        kv: 3.1882\n        both: 9.7654\n      mid:\n        dense: 1.1322\n        attn: 2.3476\n        kv: 4.0124\n        both: 17.3298\n      low:\n        dense: 1.1517\n        attn: 2.7834\n        kv: 5.8762\n        both: 25.4321\n    phase_stats:\n      high:\n        n_tokens: 16289\n        n_segments: 295\n      mid:\n        n_tokens: 4372\n        n_segments: 26\n      low:\n        n_tokens: 32227\n        n_segments: 276\n    n_problems: 50\n    pass_fail:\n      ci_overlap: true\n      sign_reversal: false\n      overall: FAIL\n    median_difference: 1.144074\n    permutation_test:\n      p_value: 0.1679\n      B: 10000\n    cohens_d: 0.1574\n    bootstrap_ci_95:\n    - -0.3166\n    - 4.1645\n    wilcoxon_p: 0.010313\n    phase_median_ii:\n      high: 1.6043\n      mid: 2.2225\n      low: 2.2641\n- exp_id: bf16_qw_rand_s030\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    median_high: 4.200557\n    median_mid: 6.477036\n    median_low: 8.065662\n    median_diff: 2.418272\n    permutation_p: 0.012\n    cohens_d: -0.03513\n    wilcoxon_p: 0.01566\n    bootstrap_ci_low: 0.241897\n    bootstrap_ci_high: 3.314824\n- exp_id: c4_entropy\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    importance_entropy_delta:\n      s015: -0.0402\n      s020: -0.0472\n      s025: -0.0446\n      s030: -0.0436\n    random_entropy_delta:\n      s015: 0.1283\n      s020: 0.136\n      s025: 0.2171\n      s030: 0.2327\n    importance_gini_delta:\n      s015: -0.0301\n      s020: -0.0404\n      s025: -0.0647\n      s030: -0.0806\n    random_gini_delta:\n      s015: -0.0309\n      s020: -0.0403\n      s025: -0.062\n      s030: -0.0732\n    importance_cv_delta:\n      s015: -0.564\n      s020: -0.774\n      s025: -1.287\n      s030: -1.665\n    random_cv_delta:\n      s015: -1.021\n      s020: -1.203\n      s025: -1.923\n      s030: -2.137\n    problems_completed: 30\n    runtime_minutes: 69.1\n- exp_id: qwen_c4_entropy\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    problems_completed: 30\n    qwen_importance_entropy_delta:\n      s015: -0.0733\n      s020: -0.0759\n      s025: 0.0451\n      s030: -0.0072\n    qwen_random_entropy_delta:\n      s015: 0.0838\n      s020: 0.0901\n      s025: 0.2168\n      s030: 0.1968\n    qwen_importance_gini_delta:\n      s015: -0.0103\n      s020: -0.0121\n      s025: -0.01\n      s030: -0.0202\n    qwen_random_gini_delta:\n      s015: -0.0186\n      s020: -0.0229\n      s025: -0.0337\n      s030: -0.0448\n    qwen_importance_cv_delta:\n      s015: -0.045\n      s020: -0.208\n      s025: -1.491\n      s030: -1.142\n    qwen_random_cv_delta:\n      s015: -0.778\n      s020: -0.889\n      s025: -1.5\n      s030: -1.677\n    cross_model_notes: random entropy increase consistent; importance entropy collapse\n      inconsistent at s025 (reversed to +0.045) and near-zero at s030; gini/cv directions\n      consistent but Qwen magnitudes smaller\n- exp_id: bf16_ds_imp_s010\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    verdict: FAIL\n    problems: 50\n    II_high_sparsity_median: 0.0027\n    II_high_sparsity_mean: -0.1998\n    II_low_sparsity_median: 0.0151\n    II_low_sparsity_mean: -0.1066\n    II_mid_sparsity_median: 0.0061\n    II_mid_sparsity_mean: -0.0131\n    high_sparsity_tokens: 21086\n    low_sparsity_tokens: 27748\n    mid_sparsity_tokens: 13306\n- exp_id: bf16_ds_imp_s035\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    verdict: PASS\n    problems: 50\n    II_high_sparsity_median: 0.1051\n    II_high_sparsity_mean: 1.4309\n    II_low_sparsity_median: 28.7649\n    II_low_sparsity_mean: 104.1892\n    II_mid_sparsity_median: 4.9542\n    II_mid_sparsity_mean: 20.326\n    high_sparsity_tokens: 21086\n    low_sparsity_tokens: 27748\n    mid_sparsity_tokens: 13306\n    ci_overlap_test: low_sparsity vs mid_sparsity CI non-overlapping at 0.35\n- exp_id: bf16_qw_imp_s010\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_problems: 50\n    overall_verdict: PASS\n    ci_overlap_test: PASS\n    sign_reversal_test: FAIL\n    high_sparsity_II_median: 0.0001\n    high_sparsity_II_median_CI:\n    - -0.0028\n    - 0.0005\n    high_sparsity_II_mean: -0.0887\n    high_sparsity_II_mean_CI:\n    - -0.1235\n    - -0.0591\n    low_sparsity_II_median: -0.0444\n    low_sparsity_II_median_CI:\n    - -0.0967\n    - -0.0152\n    low_sparsity_II_mean: -0.2431\n    low_sparsity_II_mean_CI:\n    - -0.3817\n    - -0.1202\n    mid_sparsity_II_median: -0.0359\n    mid_sparsity_II_median_CI:\n    - -0.0963\n    - -0.015\n    mid_sparsity_II_mean: -0.084\n    mid_sparsity_II_mean_CI:\n    - -0.1366\n    - -0.035\n    ppl_high_dense: 1.074\n    ppl_high_both: 1.228\n    ppl_low_dense: 1.152\n    ppl_low_both: 3.204\n    ppl_mid_dense: 1.133\n    ppl_mid_both: 1.741\n- exp_id: bf16_qw_imp_s035\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_problems: 50\n    overall_verdict: PASS\n    ci_overlap_test: PASS\n    sign_reversal_test: FAIL\n    high_sparsity_II_median: 0.0232\n    high_sparsity_II_median_CI:\n    - 0.0154\n    - 0.0383\n    high_sparsity_II_mean: 0.1643\n    high_sparsity_II_mean_CI:\n    - 0.0844\n    - 0.2495\n    low_sparsity_II_median: 8.2358\n    low_sparsity_II_median_CI:\n    - 6.1564\n    - 10.9231\n    low_sparsity_II_mean: 18.9673\n    low_sparsity_II_mean_CI:\n    - 14.5015\n    - 23.9752\n    mid_sparsity_II_median: 0.9577\n    mid_sparsity_II_median_CI:\n    - 0.171\n    - 3.5575\n    mid_sparsity_II_mean: 8.0734\n    mid_sparsity_II_mean_CI:\n    - 2.0224\n    - 16.8946\n    ppl_high_dense: 1.0738\n    ppl_high_both: 2.3435\n    ppl_low_dense: 1.1518\n    ppl_low_both: 58.0358\n    ppl_mid_dense: 1.1327\n    ppl_mid_both: 20.9912\n    high_sparsity_tokens: 16289\n    low_sparsity_tokens: 32227\n    mid_sparsity_tokens: 4372\n- exp_id: c2_n500_deepseek\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: c3_llama_arch\n  name: ''\n  status: PENDING\n  conclusion: killed\n  metrics: {}\n- exp_id: c2_ds_n500\n  name: ''\n  status: PENDING\n  conclusion: killed\n  metrics: {}\n- exp_id: c2_qw_n500\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: c3_llama\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-14T14:42:33.531Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T14:42:33.531Z",
  "sessionId": "589e47f3-a107-4a46-857a-74855f584341"
}
```

---

## Round 1

24 recorded events

### User

_source line 3 · 2026-05-14T14:42:33.559Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：C5 pilot 边缘或失败（LLaMA 方向对但 gate 未达标），n=500 Qwen s015 仍跨零但正向趋势明显，需调整 claims 强度
核心假设：['C5 LLaMA-8B 显示正向 phase gradient 但回收 <30%（或 crossover 方向对但不显著）', 'C2 n=500 后 Qwen s015 CI 仍跨零，但点估计稳定正向（median diff ~0.04-0.05）', 'DeepSeek n=500 结果与现有 n=50 一致，无意外', 'Discrimination collapse Gini/CV 在可用架构上方向一致']
关键指标范围：{'c5_llama_paired_median_diff_s025': [0.2, 1.0], 'c5_llama_cohens_d_s025': [0.15, 0.5], 'c5_llama_crossover_present': ['ambiguous'], 'c2_qw_s015_n500_ci_lower': [-0.01, 0.01], 'c2_qw_s015_n500_median_diff': [0.03, 0.06], 'c2_ds_n500_ci_width_reduction_pct': [15, 35], 'c2_ds_s015_n500_median_diff': [0.25, 0.35], 'confirmed_arch_families': [1]}
叙事方向：调整 claims 强度：C5 降级为 "preliminary evidence / suggestive pilot" 放入 §5 Discussion 而非 §4 Results 主体，或作为 Appendix 补充证据。 C2 叙事改为 threshold framing："compound effect emerges above threshold sparsity (~s020)"，Qwen s015 作为 boundary condition 讨论。 Title 去掉 "across architectures"，改为强调 Qwen-family 内的 cross-model replication（distillation vs instruction tuning）。RC1 诚实承认 同架构局限，以 mechanism 的 architecture-agnostic 性质作为间接论证。 贡献收缩为：(1) 发现 + 同架构跨训练验证，(2) 量化 gradient（threshold-dependent）， (3) discrimination collapse 机制。仍是 solid EMNLP empirical finding paper。


基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: phase-gated-compound-sparse
focus: D052 调整后的完整 plan：C5 pilot-first 跨架构验证、C2 n=500 预注册叙事、C7/C8 写作任务、Lethe/SparK 区分。重点关注：(1) pilot-first 策略是否足够支撑泛化性 claim；(2) C7/C8 作为写作任务是否被审稿人视为弱点；(3) 11 天 deadline 下 plan 可行性

## paper_framing.md

# Paper Framing — Phase-Gated Compound Sparsity

> 最后更新: 2026-05-14 (D052 审稿应对调整) | 维护者: Director

## Core Insight

Compound sparsity（attention head pruning + KV cache eviction）的 severity 不是固定常数——它是 eviction strategy 和 reasoning phase 交互的涌现属性。Importance-based eviction 的 compound interaction severity（paired median difference: median(II_low_i − II_high_i)）随 sparsity 单调递增（DeepSeek: 0.32→1.15→3.97→9.94; Qwen: 0.048→0.208→1.109→2.619），而 random masking 三相 II 持平（7/8 FAIL; Qwen s030 PASS p=0.012 but d=-0.04 negligible）。Cohen's d（paired d_z, B=10000）从 small-medium 到 large（DeepSeek: 0.44→0.80; Qwen: 0.28→1.02，s015 边缘）。这一发现挑战了 compound degradation 均匀分布的隐含假设。

**数字基准**：所有数字基于 bf16 per-problem paired 统计量（B=10000 bootstrap）。median_diff 定义为 median(II_low_i − II_high_i)（逐 problem 配对差的中位数）。fp16 旧数据已弃用。

## Narrative Arc

Compound sparsity 是高效 LLM 推理的实用部署需求，但 prior work（SparK, Ada-KV, SLiM）将 compound interaction 视为均匀超可加。我们发现 severity 是 strategy × phase 交互的涌现属性：importance eviction 的 compound interaction 在 low-sparsity phase 远大于 high-sparsity phase（paired median difference 单调递增 0.32→9.94），而 random eviction 在所有 phase 保持平坦（7/8 FAIL; 唯一例外 Qwen s030 p=0.012 效应量可忽略 d=-0.04）。Cross-model replication 方向一致（Qwen magnitude ~1/4 of DeepSeek，onset threshold s≥0.20）。C3 crossover 现象的 LLaMA 架构验证已列入计划（plan_009 pilot-first），以测试发现的跨架构泛化性。我们通过 discrimination collapse 机制解释这一现象：head pruning → importance score 的判别力崩塌（Gini/CV 下降跨模型一致）→ importance eviction 退化为有偏伪随机。Attention entropy redistribution 作为 model-dependent secondary effect 在 DeepSeek 上观察到，但在 Qwen 上不稳健（D044）。

**Framing 硬约束（D015）**：
- MUST: \"emergent phase-strategy interaction\"
- MUST NOT: \"importance metric limitation / importance is broken\"
- MUST NOT: claim \"importance masking produces super-additive interaction\" without qualifier — random masking also produces positive II. The distinguishing signal is **phase-dependent gradient** (importance: paired median difference 0.32→9.94 单调递增 vs random: 7/8 FAIL), not the existence of super-additivity itself (D023)

## Core Claims

| ID | Claim | Status | Key Evidence |
|----|-------|--------|-------------|
| C1 | Compound sparsity severity is strategy-dependent | confirmed | importance paired median diff 0.32→9.94 单调递增 vs random 7/8 FAIL (bf16; Qwen s030 PASS p=0.012 d=-0.04 negligible) |
| C2 | Severity is phase-modulated (amplified in low-sparsity phase) | confirmed | bf16 paired median difference 单调递增: 0.32→1.15→3.97→9.94; Bonferroni p<0.005 全 4 水平 (D032)。预注册：n=500 后若 QW s015 CI 仍跨零，叙事改为 'compound effect emerges above threshold sparsity (~s020)' |
| C3 | Phase-strategy crossover exists | confirmed | s=0.25: importance high_phase=0.032 < random=0.818, importance low_phase=7.196 > random=1.363 (bf16) |
| C4 | Discrimination collapse as primary mechanism; entropy redistribution model-dependent | partially_confirmed | D044: Gini/CV 下降跨模型一致; entropy collapse DeepSeek 一致但 Qwen s025 反转(+0.045) s030≈0。30/30 problems completed. |
| C5 | Phase-modulated compound severity generalizes across architectures | pilot_pending | Pilot-first: 2h oracle + heuristic (token position ratio as phase proxy) on LLaMA-8B, s025/s030. Gate: recover >30% compound degradation → full rollout; else → future work. Must include heuristic baseline (oracle upper bound + simple heuristic lower bound). |
| C6 | Severity gradient is sub-exponential | confirmed | Growth rate decreasing: Δ增长因子 3.8×→4.8×→2.0×（递减） |
| C7 | Abstract 精简至 150-200 词，突出核心发现（原 S3 升级） | action_required | 当前 ~600 词信息过载，需精简至 1-2 个关键定量结果。写作任务，无需实验。 |
| C8 | II 与已有 super-additivity 概念明确区分（原 S7 升级） | action_required | §3 Methodology 加段讨论 II vs SparK/SLiM/UniComp 的 compound interaction 度量区别。写作+分析任务。 |

## Anticipated Reviewer Concerns

### RC1: Generalizability — 7B models only, single benchmark
- **预期质疑**: "Results on two 7B models and MATH-500 only. How do we know this generalizes to larger models or other reasoning tasks?"
- **应对**: Cross-model replication (DeepSeek-R1-Distill-Qwen-7B + Qwen2.5-7B-Instruct) 控制架构变量、隔离训练方式影响（distillation vs instruction tuning）。注意：两模型共享 Qwen2ForCausalLM 架构，不能 claim 跨架构泛化。MATH-500 是 standard benchmark。Limitations 必须诚实声明：(1) 同架构不同训练，不是跨架构；(2) 7B scale only；(3) 单 benchmark。机制解释 (discrimination collapse) 原则上 architecture-agnostic，但未实证验证。
- **实验支撑**: C5 (Qwen cross-model). 若需加强可扩展到不同架构（如 LLaMA/Mistral），但 11 天 deadline 内不现实

### RC2: Mechanism — entropy-discrimination collapse 缺乏直接测量
- **预期质疑**: "The mechanism is conceptual. Where is the empirical evidence for entropy increase and discrimination collapse?"
- **应对**: c4_entropy 实验已完成（DeepSeek 30/30 + Qwen 30/30）。D044 结论：Gini/CV 下降跨模型一致（discrimination collapse confirmed）；entropy redistribution 在 DeepSeek 上一致但在 Qwen 上 s025 方向反转、s030 近零（model-dependent）。论文以 discrimination collapse 为主线，entropy 作 DeepSeek 特有的强化因素。
- **实验支撑**: c4_entropy (DeepSeek DONE) + qwen_c4_entropy (DONE, negative for entropy universality)

### RC3: Practical impact — 没有 throughput 数据
- **预期质疑**: "No wall-clock or throughput measurements. Is the severity amplification reflected in actual inference speed?"
- **应对**: 本文定位是 empirical finding paper（发现 + 机制解释），不是 method paper。Throughput 不是 claim 的一部分。Discussion 中明确 phase-gated controller 作为 future direction。
- **实验支撑**: 不需要额外实验

### RC4: Statistical rigor — bootstrap 是否足够
- **预期质疑**: "Per-problem bootstrap with 50 problems — sufficient sample size?"
- **应对**: bf16 使用 B=10000 per-problem paired bootstrap，有效配对数 n=49 (DeepSeek) / n=46 (Qwen)。Permutation test 使用 paired median difference 作为 robust statistic（D032），Bonferroni 校正后全 4 水平 p<0.005。Cohen's d（paired d_z）作为辅助效应量（DeepSeek 0.44→0.80, Qwen 0.28→1.02）。可在 appendix 补充 per-problem 分布图（已生成 fig4_per_problem_dist.pdf）。
- **实验支撑**: bf16 permutation test (D032) + Cohen's d per-problem paired (rebootstrap B=10000) 已完成

### RC5: Novelty — prior work 是否已覆盖 phase-dependent sparsity
- **预期质疑**: "ThinKV and phase-aware methods already consider phase. What's new?"
- **应对**: Prior work 在单轴上分析 phase（ThinKV: phase-aware eviction）或 compound（SparK: joint compression）。没有工作同时分析 compound × phase × strategy 的三维交互。Crossover 现象（同一 strategy 在不同 phase 方向反转）是全新发现。Related Work 加 Lethe 引用区分 + SparK 对比。
- **实验支撑**: C3 (crossover), Related Work §2 的 gap 分析

## Paper Positioning

**类型**: Empirical finding paper（非 method paper）
**核心贡献**:
1. 发现 compound sparsity severity 的 strategy × phase 交互
2. 量化 severity gradient（bf16 paired median difference 0.32→9.94, Cohen's d 0.44→0.80）和 crossover 现象
3. 提出 discrimination collapse 机制解释（Gini/CV 跨模型一致；entropy redistribution model-dependent）
4. Cross-model replication 验证泛化性

**投稿目标**: EMNLP 2026 ARR, deadline 2026-05-25
**Rebuttal 准备**: Day 9 (2026-05-23) 预留 rebuttal letter 写作时间


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
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: c3_llama_arch
  name: ''
  status: PENDING
  conclusion: killed
  metrics: {}
- exp_id: c2_ds_n500
  name: ''
  status: PENDING
  conclusion: killed
  metrics: {}
- exp_id: c2_qw_n500
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: c3_llama
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}

# 输出格式（YAML，仅输出一个 ```yaml 块）

```yaml
tier: median
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
  "promptId": "b0df8920-d739-47eb-a93d-268a74684922",
  "type": "user",
  "uuid": "dd0226e2-c32a-4052-9bcd-dcd7d93d9c93",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "589e47f3-a107-4a46-857a-74855f584341",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T14:42:33.556Z_

```json
{
  "parentUuid": "dd0226e2-c32a-4052-9bcd-dcd7d93d9c93",
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
  "uuid": "b78c3078-c840-4592-8307-73e7f1ee9bf3",
  "timestamp": "2026-05-14T14:42:33.556Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "589e47f3-a107-4a46-857a-74855f584341",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T14:42:33.556Z_

```json
{
  "parentUuid": "b78c3078-c840-4592-8307-73e7f1ee9bf3",
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
  "uuid": "73779524-4015-43b6-b252-d3194d2e1843",
  "timestamp": "2026-05-14T14:42:33.556Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "589e47f3-a107-4a46-857a-74855f584341",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-14T14:42:33.557Z_

```json
{
  "parentUuid": "73779524-4015-43b6-b252-d3194d2e1843",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "25a758be-1632-4b87-9276-850cc1f29f51",
  "timestamp": "2026-05-14T14:42:33.557Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "589e47f3-a107-4a46-857a-74855f584341",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：C5 pilot 边缘或失败（LLaMA 方向对但 gate 未达标），n=500 Qwen s015 仍跨零但正向趋势明显，需调整 claims 强度 核心假设：['C5 LLaMA-8B 显示正向 phase gradient 但回收 <30%（或 crossover 方向对但不显著）', 'C2 n…",
  "leafUuid": "25a758be-1632-4b87-9276-850cc1f29f51",
  "sessionId": "589e47f3-a107-4a46-857a-74855f584341"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Median sparsity phase-strategy interaction empirical validation",
  "sessionId": "589e47f3-a107-4a46-857a-74855f584341"
}
```

---

### Assistant

_source line 9 · 2026-05-14T14:42:37.226Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted data for each planned experiment in the experiment_plan, based on the "median" tier definition provided. I need to first find the experiment_plan to understand what experiments are planned, then generate predictions for each one.

Let me look at the experiment plan file first.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25a758be-1632-4b87-9276-850cc1f29f51",
  "isSidechain": false,
  "requestId": "req_011Cb2dwNu4uNxC6bwiCSJ9S",
  "type": "assistant",
  "uuid": "eeb6b97c-1611-462b-9aa5-7f2a2f9939b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "589e47f3-a107-4a46-857a-74855f584341",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TjV1wFng9bPzmtvxKdinRa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 27322,
      "cache_read_input_tokens": 11447,
      "output_tokens": 280,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27322,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 280,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 27322,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27322
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

_source line 10 · 2026-05-14T14:42:37.814Z_

Let me find the experiment plan to understand what experiments need predictions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eeb6b97c-1611-462b-9aa5-7f2a2f9939b1",
  "isSidechain": false,
  "requestId": "req_011Cb2dwNu4uNxC6bwiCSJ9S",
  "type": "assistant",
  "uuid": "b84a7469-359c-47e1-912b-3c0f7d7b2b5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "589e47f3-a107-4a46-857a-74855f584341",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TjV1wFng9bPzmtvxKdinRa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 27322,
      "cache_read_input_tokens": 11447,
      "output_tokens": 280,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27322,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 280,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 27322,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27322
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

_source line 11 · 2026-05-14T14:42:41.779Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01MyRPUBUzt9p2qNbyxScFjN`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find experiment plan files",
  "prompt": "Search the directory /home/ubuntu/.agent-ml-research-idea_gen_0509_11 for experiment plan files. Look for files named like \"experiment_plan*\", \"plan*\", or any YAML/MD files that contain experiment planning information with fields like \"plan_id\", \"planned\", \"PENDING\", \"RUNNING\" etc. Search breadth: very thorough. Report the full paths and key content of any files found."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b84a7469-359c-47e1-912b-3c0f7d7b2b5f",
  "isSidechain": false,
  "requestId": "req_011Cb2dwNu4uNxC6bwiCSJ9S",
  "type": "assistant",
  "uuid": "045b647b-e4c5-4925-8e9f-704c89d21d64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "589e47f3-a107-4a46-857a-74855f584341",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TjV1wFng9bPzmtvxKdinRa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 27322,
      "cache_read_input_tokens": 11447,
      "output_tokens": 280,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27322,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 280,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 27322,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27322
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

_source line 12 · 2026-05-14T14:43:12.063Z_

<details><summary>↩ Tool result · `toolu_01MyRPUBUzt9p2qNbyxScFjN`</summary>

```text
Perfect! I've completed a thorough search. Let me compile my findings:

## Search Results: Experiment Plan Files

I found **3 primary experiment plan files** in the directory along with supporting YAML documents. Here are the results:

### Primary Experiment Plan Files

#### 1. **redundancy-compound-sparsity** Project
**File:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/redundancy-compound-sparsity/experiment_plan.yaml`

**Content Summary:**
- Experiment plan for "Confound Resolution Phase" targeting EMNLP 2026 ARR (DDL: 2026-05-25)
- Contains **13 experiments** organized by status:
  - **COMPLETED (4 experiments):** mvp-001, mvp-001b, mvp-001c, neg-cross-model-001 (all DONE)
  - **P0-URGENT (2 experiments):** confound-ctrl-001, confound-ctrl-002 (PLANNED)
  - **P0 Core (3 experiments):** llama-sparsity-sweep, llama-layer-analysis, kv-bench-001 (PLANNED/PREPARING)
  - **P1 & P2 (4 experiments):** cross-arch-mistral, mla-signal-analysis, kv-eviction-wallclock, neg-per-head, kv-eviction-ablation, llama-downstream
- Key fields: `plan_id`, `status`, `priority`, `depends_on`, `gpu_hours`, `description`, `result`
- Notable statuses: DONE, PLANNED, PREPARING, SUSPENDED
- 12-day sprint timeline (5/12 → 5/25)

#### 2. **redundancy-compound-sparsity-2** Project (PATHC)
**File:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/redundancy-compound-sparsity-2/experiment_plan.yaml`

**Content Summary:**
- Experiment plan for path-computation KV cache eviction project
- Contains **34 experiments** organized by **phases**:
  - **Phase 0 (Sanity Gate):** pathc_sanity_reasoning, pathc_sanity_wikitext32k
  - **Phase 0b (Analysis Contingency):** analysis_heatmap, analysis_attn_vs_ema, analysis_tau_sweep, analysis_decay_curve, analysis_second_model
  - **Phase 1 (PPL Budget Sweep):** pathc_ppl_budget30/50/70
  - **Phase 2 (Baseline Comparison):** pathc_baseline_h2o, pathc_baseline_rkv
  - **Phase 3 (Ablation):** pathc_ablation_gamma, pathc_ablation_budget, pathc_ablation_grace, pathc_ablation_perhead
  - **Phase 4 (Reasoning Eval):** pathc_math500_eval
  - **Phase 5 (Scaling + Throughput):** pathc_scaling_32k, pathc_scaling_64k, pathc_throughput
- Key fields: `id`, `phase`, `description`, `claim`, `priority`, `depends_on`, `success_criterion`, `estimated_hours`, `registry_id`, `status`
- Notable statuses: pending, depends_on conditions
- Many experiments structured as gate-passing phases

#### 3. **phase-gated-compound-sparse** Project
**File:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/experiment_plan.yaml`

**Content Summary:**
- Experiment plan for "Phase-Gated Compound Sparsity" research targeting EMNLP 2026 ARR (DDL: 2026-05-25)
- Contains **15 experiments** organized by **claims (C1-C9)**:
  - **C1+C2 (Strategy-dependent):** plan_001 (pending), plan_002-003 (planned)
  - **C5 (Cross-model):** plan_004-005 (pending/planned)
  - **C4 (Entropy mechanism):** plan_006 (planned)
  - **C6 (Growth rate):** plan_007 (planned)
  - **C2/C7 (Statistical Power):** plan_009, plan_010 (RUNNING)
  - **C5b (Mitigation):** plan_011 (planned)
  - **C8 (Cross-architecture):** plan_012 (planned)
  - **Misc:** plan_013-015 (planned/done)
- Key fields: `plan_id`, `claim`, `title`, `description`, `priority`, `status`, `depends_on`, `registry_ids`, `gpu_hours_est`, `notes`
- Notable statuses: pending, planned, running, done
- Resource budget: 58.5 GPU hours estimated
- Timeline: n=500 experiments ~18h, pilot ~2h additional
- Two actively RUNNING experiments (plan_009, plan_010)

### Supporting Files

#### 4. **Writing Plan** (Phase-Gated Project)
**File:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/writing_plan.yaml`

**Content Summary:**
- Writing plan aligned with experiment plan
- Targets EMNLP 2026 ARR with 11 days remaining (updated 2026-05-14)
- Paper outline with 8 sections, 5 figures, 3 tables
- Claims-to-evidence mapping with confirmation status
- Writing priority schedule (Phase 1-5) with specific deliverables
- Risk analysis with mitigations
- 3-day submission buffer

#### 5. **Lock Files**
**File:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/redundancy-compound-sparsity-2/experiment_plan.lock` (empty/minimal)

---

### Summary Statistics

| Project | Experiments | Running | Planned | Done | Suspended |
|---------|-------------|---------|---------|------|-----------|
| redundancy-compound-sparsity | 13 | 0 | 8 | 4 | 1 |
| redundancy-compound-sparsity-2 | 34 | Gated phases | Most pending | - | - |
| phase-gated-compound-sparse | 15 | 2 | 10 | 2 | - |

All experiment plans are YAML-formatted and contain structured fields for plan_id, status, priority, dependencies, resource estimates, and registry linkages to actual experiment runs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "045b647b-e4c5-4925-8e9f-704c89d21d64",
  "isSidechain": false,
  "promptId": "b0df8920-d739-47eb-a93d-268a74684922",
  "type": "user",
  "uuid": "0d56f1d6-151e-4c94-b612-f9fa1c956d65",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the directory /home/ubuntu/.agent-ml-research-idea_gen_0509_11 for experiment plan files. Look for files named like \"experiment_plan*\", \"plan*\", or any YAML/MD files that contain experiment planning information with fields like \"plan_id\", \"planned\", \"PENDING\", \"RUNNING\" etc. Search breadth: very thorough. Report the full paths and key content of any files found.",
    "agentId": "af262e2445bf84121",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! I've completed a thorough search. Let me compile my findings:\n\n## Search Results: Experiment Plan Files\n\nI found **3 primary experiment plan files** in the directory along with supporting YAML documents. Here are the results:\n\n### Primary Experiment Plan Files\n\n#### 1. **redundancy-compound-sparsity** Project\n**File:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/redundancy-compound-sparsity/experiment_plan.yaml`\n\n**Content Summary:**\n- Experiment plan for \"Confound Resolution Phase\" targeting EMNLP 2026 ARR (DDL: 2026-05-25)\n- Contains **13 experiments** organized by status:\n  - **COMPLETED (4 experiments):** mvp-001, mvp-001b, mvp-001c, neg-cross-model-001 (all DONE)\n  - **P0-URGENT (2 experiments):** confound-ctrl-001, confound-ctrl-002 (PLANNED)\n  - **P0 Core (3 experiments):** llama-sparsity-sweep, llama-layer-analysis, kv-bench-001 (PLANNED/PREPARING)\n  - **P1 & P2 (4 experiments):** cross-arch-mistral, mla-signal-analysis, kv-eviction-wallclock, neg-per-head, kv-eviction-ablation, llama-downstream\n- Key fields: `plan_id`, `status`, `priority`, `depends_on`, `gpu_hours`, `description`, `result`\n- Notable statuses: DONE, PLANNED, PREPARING, SUSPENDED\n- 12-day sprint timeline (5/12 → 5/25)\n\n#### 2. **redundancy-compound-sparsity-2** Project (PATHC)\n**File:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/redundancy-compound-sparsity-2/experiment_plan.yaml`\n\n**Content Summary:**\n- Experiment plan for path-computation KV cache eviction project\n- Contains **34 experiments** organized by **phases**:\n  - **Phase 0 (Sanity Gate):** pathc_sanity_reasoning, pathc_sanity_wikitext32k\n  - **Phase 0b (Analysis Contingency):** analysis_heatmap, analysis_attn_vs_ema, analysis_tau_sweep, analysis_decay_curve, analysis_second_model\n  - **Phase 1 (PPL Budget Sweep):** pathc_ppl_budget30/50/70\n  - **Phase 2 (Baseline Comparison):** pathc_baseline_h2o, pathc_baseline_rkv\n  - **Phase 3 (Ablation):** pathc_ablation_gamma, pathc_ablation_budget, pathc_ablation_grace, pathc_ablation_perhead\n  - **Phase 4 (Reasoning Eval):** pathc_math500_eval\n  - **Phase 5 (Scaling + Throughput):** pathc_scaling_32k, pathc_scaling_64k, pathc_throughput\n- Key fields: `id`, `phase`, `description`, `claim`, `priority`, `depends_on`, `success_criterion`, `estimated_hours`, `registry_id`, `status`\n- Notable statuses: pending, depends_on conditions\n- Many experiments structured as gate-passing phases\n\n#### 3. **phase-gated-compound-sparse** Project\n**File:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/experiment_plan.yaml`\n\n**Content Summary:**\n- Experiment plan for \"Phase-Gated Compound Sparsity\" research targeting EMNLP 2026 ARR (DDL: 2026-05-25)\n- Contains **15 experiments** organized by **claims (C1-C9)**:\n  - **C1+C2 (Strategy-dependent):** plan_001 (pending), plan_002-003 (planned)\n  - **C5 (Cross-model):** plan_004-005 (pending/planned)\n  - **C4 (Entropy mechanism):** plan_006 (planned)\n  - **C6 (Growth rate):** plan_007 (planned)\n  - **C2/C7 (Statistical Power):** plan_009, plan_010 (RUNNING)\n  - **C5b (Mitigation):** plan_011 (planned)\n  - **C8 (Cross-architecture):** plan_012 (planned)\n  - **Misc:** plan_013-015 (planned/done)\n- Key fields: `plan_id`, `claim`, `title`, `description`, `priority`, `status`, `depends_on`, `registry_ids`, `gpu_hours_est`, `notes`\n- Notable statuses: pending, planned, running, done\n- Resource budget: 58.5 GPU hours estimated\n- Timeline: n=500 experiments ~18h, pilot ~2h additional\n- Two actively RUNNING experiments (plan_009, plan_010)\n\n### Supporting Files\n\n#### 4. **Writing Plan** (Phase-Gated Project)\n**File:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/writing_plan.yaml`\n\n**Content Summary:**\n- Writing plan aligned with experiment plan\n- Targets EMNLP 2026 ARR with 11 days remaining (updated 2026-05-14)\n- Paper outline with 8 sections, 5 figures, 3 tables\n- Claims-to-evidence mapping with confirmation status\n- Writing priority schedule (Phase 1-5) with specific deliverables\n- Risk analysis with mitigations\n- 3-day submission buffer\n\n#### 5. **Lock Files**\n**File:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/redundancy-compound-sparsity-2/experiment_plan.lock` (empty/minimal)\n\n---\n\n### Summary Statistics\n\n| Project | Experiments | Running | Planned | Done | Suspended |\n|---------|-------------|---------|---------|------|-----------|\n| redundancy-compound-sparsity | 13 | 0 | 8 | 4 | 1 |\n| redundancy-compound-sparsity-2 | 34 | Gated phases | Most pending | - | - |\n| phase-gated-compound-sparse | 15 | 2 | 10 | 2 | - |\n\nAll experiment plans are YAML-formatted and contain structured fields for plan_id, status, priority, dependencies, resource estimates, and registry linkages to actual experiment runs."
      }
    ],
    "totalDurationMs": 30275,
    "totalTokens": 55741,
    "totalToolUseCount": 11,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 776,
      "cache_read_input_tokens": 53328,
      "output_tokens": 1632,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 776
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 1632,
          "cache_read_input_tokens": 53328,
          "cache_creation_input_tokens": 776,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 776,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 5,
      "searchCount": 4,
      "bashCount": 2,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "045b647b-e4c5-4925-8e9f-704c89d21d64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "589e47f3-a107-4a46-857a-74855f584341",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T14:43:14.531Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CRjDXj3N2eQPgGwypcAC7H`</summary>

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
  "parentUuid": "0d56f1d6-151e-4c94-b612-f9fa1c956d65",
  "isSidechain": false,
  "requestId": "req_011Cb2dzDSdXjQZ5XQbs7JTM",
  "type": "assistant",
  "uuid": "906cf254-bda5-4347-96f1-ef1817b089f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "589e47f3-a107-4a46-857a-74855f584341",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Uxvus1rPjAAAt1DpGeYNw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1920,
      "cache_read_input_tokens": 38769,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1920,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 88,
          "cache_read_input_tokens": 38769,
          "cache_creation_input_tokens": 1920,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1920
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

_source line 14 · 2026-05-14T14:43:14.539Z_

<details><summary>↩ Tool result · `toolu_01CRjDXj3N2eQPgGwypcAC7H`</summary>

```text
1	# Experiment Plan — Phase-Gated Compound Sparsity
2	# 最后更新: 2026-05-14
3	# 维护者: Director
4	#
5	# 每个 plan 对应一个 claim（paper_framing.md），标注 priority / depends_on / status
6	# registry_id 链接已注册实验；无 registry_id = planned
7	
8	plans:
9	  # ============================================================
10	  # C1 + C2: Strategy-dependent, phase-modulated severity
11	  # ============================================================
12	  - plan_id: plan_001
13	    claim: C1, C2
14	    title: "DeepSeek importance bf16 × 4 sparsity"
15	    description: "bf16 重跑 DeepSeek importance masking (s015/s020/s025/s030)，消除 fp16 NaN 偏差"
16	    priority: P0
17	    status: pending
18	    depends_on: []
19	    registry_ids:
20	      - bf16_importance_s015
21	      - bf16_importance_s020
22	      - bf16_importance_s025
23	      - bf16_importance_s030
24	    gpu_hours_est: 3
25	    notes: "fp16 版本已完成但有 NaN 问题，需 bf16 重跑获得干净数据"
26	
27	  - plan_id: plan_002
28	    claim: C1
29	    title: "DeepSeek random bf16 × 4 sparsity"
30	    description: "bf16 重跑 DeepSeek random masking (s015/s020/s025/s030)，作为 importance 的配对对照"
31	    priority: P0
32	    status: planned
33	    depends_on: []
34	    registry_ids: []
35	    gpu_hours_est: 3
36	    notes: "与 plan_001 配对，论文数据必须同一 dtype"
37	
38	  # ============================================================
39	  # C3: Phase-strategy crossover
40	  # ============================================================
41	  - plan_id: plan_003
42	    claim: C3
43	    title: "Crossover analysis from plan_001 + plan_002"
44	    description: "从 bf16 importance vs random 数据中提取 per-phase II，验证方向反转"
45	    priority: P0
46	    status: planned
47	    depends_on: [plan_001, plan_002]
48	    registry_ids: []
49	    gpu_hours_est: 0
50	    notes: "纯分析任务，不需要额外 GPU。数据从 plan_001/002 派生"
51	
52	  # ============================================================
53	  # C5: Cross-model generalizability
54	  # ============================================================
55	  - plan_id: plan_004
56	    claim: C5
57	    title: "Qwen importance bf16 × 4 sparsity"
58	    description: "Qwen2.5-7B-Instruct importance masking bf16 (s015/s020/s025/s030)"
59	    priority: P0
60	    status: pending
61	    depends_on: []
62	    registry_ids:
63	      - qwen_importance_s015
64	      - qwen_importance_s020
65	      - qwen_importance_s025
66	      - qwen_importance_s030
67	    gpu_hours_est: 3
68	    notes: "cross-model replication 核心实验"
69	
70	  - plan_id: plan_005
71	    claim: C5
72	    title: "Qwen random bf16 × 4 sparsity"
73	    description: "Qwen2.5-7B-Instruct random masking bf16 (s015/s020/s025/s030)"
74	    priority: P0
75	    status: planned
76	    depends_on: []
77	    registry_ids: []
78	    gpu_hours_est: 3
79	    notes: "Qwen 的配对对照，验证 importance > random 在 Qwen 上也成立"
80	
81	  # ============================================================
82	  # C4: Entropy-discrimination collapse mechanism
83	  # ============================================================
84	  - plan_id: plan_006
85	    claim: C4
86	    title: "Attention entropy measurement (optional ablation)"
87	    description: "测量 pruned vs unpruned 的 attention entropy + importance score 分布，直接验证 mechanism"
88	    priority: P2
89	    status: planned
90	    depends_on: [plan_001]
91	    registry_ids: []
92	    gpu_hours_est: 2
93	    notes: "RC2 应对实验。仅在时间允许且 reviewer concern 预判需要时执行"
94	
95	  # ============================================================
96	  # C6: Sub-exponential growth
97	  # ============================================================
98	  - plan_id: plan_007
99	    claim: C6
100	    title: "Growth rate analysis from plan_001"
101	    description: "从 bf16 importance 4 sparsity 的 gradient 数据分析增长率模式"
102	    priority: P1
103	    status: planned
104	    depends_on: [plan_001]
105	    registry_ids: []
106	    gpu_hours_est: 0
107	    notes: "纯分析任务。fp16 数据已确认 sub-exponential (2.24→1.84→1.42)，bf16 需要再验证"
108	
109	  # ============================================================
110	  # Statistical validation
111	  # ============================================================
112	  - plan_id: plan_008
113	    claim: C1, C2, C3
114	    title: "Per-problem bootstrap CI (bf16 data)"
115	    description: "对 bf16 重跑数据重新做 B=10000 bootstrap CI"
116	    priority: P0
117	    status: planned
118	    depends_on: [plan_001, plan_002]
119	    registry_ids: []
120	    gpu_hours_est: 0.5
121	    notes: "fp16 版本 all p=0.0000，bf16 预计同样显著但必须重做"
122	
123	  # ============================================================
124	  # C2: n=500 Statistical Power
125	  # ============================================================
126	  - plan_id: plan_009
127	    claim: C2, C7
128	    title: "DeepSeek n=500 statistical power boost"
129	    description: "DeepSeek 8 conditions (imp/rand × 4 sparsity) 从 n=50 扩到 n=500 (full MATH-500)"
130	    priority: P0
131	    status: running
132	    depends_on: [plan_001, plan_002]
133	    registry_ids:
134	      - c2_n500_deepseek
135	    gpu_hours_est: 18
136	    notes: "预注册：若 QW s015 CI 仍跨零，叙事改为 threshold sparsity ~s020"
137	
138	  - plan_id: plan_010
139	    claim: C2, C7
140	    title: "Qwen n=500 statistical power boost"
141	    description: "Qwen 8 conditions (imp/rand × 4 sparsity) 从 n=50 扩到 n=500"
142	    priority: P0
143	    status: running
144	    depends_on: [plan_004, plan_005]
145	    registry_ids:
146	      - c2_qw_n500
147	    gpu_hours_est: 18
148	    notes: "与 plan_009 对称验证"
149	
150	  # ============================================================
151	  # C5b: Phase-aware Mitigation Pilot
152	  # ============================================================
153	  - plan_id: plan_011
154	    claim: C5b
155	    title: "Phase-aware mitigation pilot (oracle + heuristic)"
156	    description: "2h pilot: oracle phase assignment + token position ratio heuristic on s025/s030, measure compound degradation recovery"
157	    priority: P1
158	    status: planned
159	    depends_on: [plan_009, plan_010]
160	    registry_ids: []
161	    gpu_hours_est: 2
162	    notes: "pilot-first: >30% recovery → full scale; else → future work. Must include heuristic baseline (oracle upper bound + simple heuristic lower bound). Compute-matched."
163	
164	  # ============================================================
165	  # C8: Cross-architecture (LLaMA)
166	  # ============================================================
167	  - plan_id: plan_012
168	    claim: C8
169	    title: "LLaMA-8B cross-architecture validation"
170	    description: "DeepSeek-R1-Distill-Llama-8B 上复现 phase-modulated compound severity"
171	    priority: P1
172	    status: planned
173	    depends_on: []
174	    registry_ids:
175	      - c3_llama
176	    gpu_hours_est: 6
177	    notes: "验证 finding 不限于 Qwen2ForCausalLM 架构"
178	
179	  # ============================================================
180	  # C9: Lethe/SparK differentiation (no experiment needed)
181	  # ============================================================
182	  - plan_id: plan_013
183	    claim: C9
184	    title: "Related Work differentiation: Lethe + SparK"
185	    description: "§2 Related Work 加引用区分 Lethe (layer-time-adaptive KV pruning) 和 SparK (compound compression)"
186	    priority: P1
187	    status: planned
188	    depends_on: []
189	    registry_ids: []
190	    gpu_hours_est: 0
191	    notes: "纯写作任务，不需要额外实验"
192	
193	  # ============================================================
194	  # S3→C, S7→C upgrades
195	  # ============================================================
196	  - plan_id: plan_014
197	    claim: S3→C
198	    title: "Model-dependent onset threshold analysis"
199	    description: "分析 DeepSeek vs Qwen 的 onset threshold 差异 (s≥0.15 vs s≥0.20)"
200	    priority: P1
201	    status: done
202	    depends_on: [plan_001, plan_004]
203	    registry_ids: []
204	    gpu_hours_est: 0
205	    notes: "D037/D038 已确认。纯分析任务，数据已有"
206	
207	  - plan_id: plan_015
208	    claim: S7→C
209	    title: "Dose-response monotonicity verification"
210	    description: "6-point dose-response Spearman ρ=1.0 验证"
211	    priority: P1
212	    status: done
213	    depends_on: [plan_001, plan_004]
214	    registry_ids:
215	      - bf16_ds_imp_s010
216	      - bf16_ds_imp_s035
217	      - bf16_qw_imp_s010
218	      - bf16_qw_imp_s035
219	    gpu_hours_est: 0
220	    notes: "D047 已确认。6-point 单调性 Spearman ρ=1.0"
221	
222	# ============================================================
223	# 资源预算
224	# ============================================================
225	resource_budget:
226	  total_gpu_hours_est: 58.5
227	  gpu_type: "RTX PRO 6000 Blackwell 96GB"
228	  server: westd-22162
229	  gpus: [cuda:0, cuda:1, cuda:2, cuda:3]
230	  estimated_completion: "n=500 experiments ~18h, pilot ~2h additional"
231	  timeline:
232	    day_9: "2026-05-23 — rebuttal letter"
233	    deadline: "2026-05-25 — EMNLP 2026 ARR"
234	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "906cf254-bda5-4347-96f1-ef1817b089f6",
  "isSidechain": false,
  "promptId": "b0df8920-d739-47eb-a93d-268a74684922",
  "type": "user",
  "uuid": "09cb86c0-7ac2-47a6-91c6-137956c67a12",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/experiment_plan.yaml",
      "content": "# Experiment Plan — Phase-Gated Compound Sparsity\n# 最后更新: 2026-05-14\n# 维护者: Director\n#\n# 每个 plan 对应一个 claim（paper_framing.md），标注 priority / depends_on / status\n# registry_id 链接已注册实验；无 registry_id = planned\n\nplans:\n  # ============================================================\n  # C1 + C2: Strategy-dependent, phase-modulated severity\n  # ============================================================\n  - plan_id: plan_001\n    claim: C1, C2\n    title: \"DeepSeek importance bf16 × 4 sparsity\"\n    description: \"bf16 重跑 DeepSeek importance masking (s015/s020/s025/s030)，消除 fp16 NaN 偏差\"\n    priority: P0\n    status: pending\n    depends_on: []\n    registry_ids:\n      - bf16_importance_s015\n      - bf16_importance_s020\n      - bf16_importance_s025\n      - bf16_importance_s030\n    gpu_hours_est: 3\n    notes: \"fp16 版本已完成但有 NaN 问题，需 bf16 重跑获得干净数据\"\n\n  - plan_id: plan_002\n    claim: C1\n    title: \"DeepSeek random bf16 × 4 sparsity\"\n    description: \"bf16 重跑 DeepSeek random masking (s015/s020/s025/s030)，作为 importance 的配对对照\"\n    priority: P0\n    status: planned\n    depends_on: []\n    registry_ids: []\n    gpu_hours_est: 3\n    notes: \"与 plan_001 配对，论文数据必须同一 dtype\"\n\n  # ============================================================\n  # C3: Phase-strategy crossover\n  # ============================================================\n  - plan_id: plan_003\n    claim: C3\n    title: \"Crossover analysis from plan_001 + plan_002\"\n    description: \"从 bf16 importance vs random 数据中提取 per-phase II，验证方向反转\"\n    priority: P0\n    status: planned\n    depends_on: [plan_001, plan_002]\n    registry_ids: []\n    gpu_hours_est: 0\n    notes: \"纯分析任务，不需要额外 GPU。数据从 plan_001/002 派生\"\n\n  # ============================================================\n  # C5: Cross-model generalizability\n  # ============================================================\n  - plan_id: plan_004\n    claim: C5\n    title: \"Qwen importance bf16 × 4 sparsity\"\n    description: \"Qwen2.5-7B-Instruct importance masking bf16 (s015/s020/s025/s030)\"\n    priority: P0\n    status: pending\n    depends_on: []\n    registry_ids:\n      - qwen_importance_s015\n      - qwen_importance_s020\n      - qwen_importance_s025\n      - qwen_importance_s030\n    gpu_hours_est: 3\n    notes: \"cross-model replication 核心实验\"\n\n  - plan_id: plan_005\n    claim: C5\n    title: \"Qwen random bf16 × 4 sparsity\"\n    description: \"Qwen2.5-7B-Instruct random masking bf16 (s015/s020/s025/s030)\"\n    priority: P0\n    status: planned\n    depends_on: []\n    registry_ids: []\n    gpu_hours_est: 3\n    notes: \"Qwen 的配对对照，验证 importance > random 在 Qwen 上也成立\"\n\n  # ============================================================\n  # C4: Entropy-discrimination collapse mechanism\n  # ============================================================\n  - plan_id: plan_006\n    claim: C4\n    title: \"Attention entropy measurement (optional ablation)\"\n    description: \"测量 pruned vs unpruned 的 attention entropy + importance score 分布，直接验证 mechanism\"\n    priority: P2\n    status: planned\n    depends_on: [plan_001]\n    registry_ids: []\n    gpu_hours_est: 2\n    notes: \"RC2 应对实验。仅在时间允许且 reviewer concern 预判需要时执行\"\n\n  # ============================================================\n  # C6: Sub-exponential growth\n  # ============================================================\n  - plan_id: plan_007\n    claim: C6\n    title: \"Growth rate analysis from plan_001\"\n    description: \"从 bf16 importance 4 sparsity 的 gradient 数据分析增长率模式\"\n    priority: P1\n    status: planned\n    depends_on: [plan_001]\n    registry_ids: []\n    gpu_hours_est: 0\n    notes: \"纯分析任务。fp16 数据已确认 sub-exponential (2.24→1.84→1.42)，bf16 需要再验证\"\n\n  # ============================================================\n  # Statistical validation\n  # ============================================================\n  - plan_id: plan_008\n    claim: C1, C2, C3\n    title: \"Per-problem bootstrap CI (bf16 data)\"\n    description: \"对 bf16 重跑数据重新做 B=10000 bootstrap CI\"\n    priority: P0\n    status: planned\n    depends_on: [plan_001, plan_002]\n    registry_ids: []\n    gpu_hours_est: 0.5\n    notes: \"fp16 版本 all p=0.0000，bf16 预计同样显著但必须重做\"\n\n  # ============================================================\n  # C2: n=500 Statistical Power\n  # ============================================================\n  - plan_id: plan_009\n    claim: C2, C7\n    title: \"DeepSeek n=500 statistical power boost\"\n    description: \"DeepSeek 8 conditions (imp/rand × 4 sparsity) 从 n=50 扩到 n=500 (full MATH-500)\"\n    priority: P0\n    status: running\n    depends_on: [plan_001, plan_002]\n    registry_ids:\n      - c2_n500_deepseek\n    gpu_hours_est: 18\n    notes: \"预注册：若 QW s015 CI 仍跨零，叙事改为 threshold sparsity ~s020\"\n\n  - plan_id: plan_010\n    claim: C2, C7\n    title: \"Qwen n=500 statistical power boost\"\n    description: \"Qwen 8 conditions (imp/rand × 4 sparsity) 从 n=50 扩到 n=500\"\n    priority: P0\n    status: running\n    depends_on: [plan_004, plan_005]\n    registry_ids:\n      - c2_qw_n500\n    gpu_hours_est: 18\n    notes: \"与 plan_009 对称验证\"\n\n  # ============================================================\n  # C5b: Phase-aware Mitigation Pilot\n  # ============================================================\n  - plan_id: plan_011\n    claim: C5b\n    title: \"Phase-aware mitigation pilot (oracle + heuristic)\"\n    description: \"2h pilot: oracle phase assignment + token position ratio heuristic on s025/s030, measure compound degradation recovery\"\n    priority: P1\n    status: planned\n    depends_on: [plan_009, plan_010]\n    registry_ids: []\n    gpu_hours_est: 2\n    notes: \"pilot-first: >30% recovery → full scale; else → future work. Must include heuristic baseline (oracle upper bound + simple heuristic lower bound). Compute-matched.\"\n\n  # ============================================================\n  # C8: Cross-architecture (LLaMA)\n  # ============================================================\n  - plan_id: plan_012\n    claim: C8\n    title: \"LLaMA-8B cross-architecture validation\"\n    description: \"DeepSeek-R1-Distill-Llama-8B 上复现 phase-modulated compound severity\"\n    priority: P1\n    status: planned\n    depends_on: []\n    registry_ids:\n      - c3_llama\n    gpu_hours_est: 6\n    notes: \"验证 finding 不限于 Qwen2ForCausalLM 架构\"\n\n  # ============================================================\n  # C9: Lethe/SparK differentiation (no experiment needed)\n  # ============================================================\n  - plan_id: plan_013\n    claim: C9\n    title: \"Related Work differentiation: Lethe + SparK\"\n    description: \"§2 Related Work 加引用区分 Lethe (layer-time-adaptive KV pruning) 和 SparK (compound compression)\"\n    priority: P1\n    status: planned\n    depends_on: []\n    registry_ids: []\n    gpu_hours_est: 0\n    notes: \"纯写作任务，不需要额外实验\"\n\n  # ============================================================\n  # S3→C, S7→C upgrades\n  # ============================================================\n  - plan_id: plan_014\n    claim: S3→C\n    title: \"Model-dependent onset threshold analysis\"\n    description: \"分析 DeepSeek vs Qwen 的 onset threshold 差异 (s≥0.15 vs s≥0.20)\"\n    priority: P1\n    status: done\n    depends_on: [plan_001, plan_004]\n    registry_ids: []\n    gpu_hours_est: 0\n    notes: \"D037/D038 已确认。纯分析任务，数据已有\"\n\n  - plan_id: plan_015\n    claim: S7→C\n    title: \"Dose-response monotonicity verification\"\n    description: \"6-point dose-response Spearman ρ=1.0 验证\"\n    priority: P1\n    status: done\n    depends_on: [plan_001, plan_004]\n    registry_ids:\n      - bf16_ds_imp_s010\n      - bf16_ds_imp_s035\n      - bf16_qw_imp_s010\n      - bf16_qw_imp_s035\n    gpu_hours_est: 0\n    notes: \"D047 已确认。6-point 单调性 Spearman ρ=1.0\"\n\n# ============================================================\n# 资源预算\n# ============================================================\nresource_budget:\n  total_gpu_hours_est: 58.5\n  gpu_type: \"RTX PRO 6000 Blackwell 96GB\"\n  server: westd-22162\n  gpus: [cuda:0, cuda:1, cuda:2, cuda:3]\n  estimated_completion: \"n=500 experiments ~18h, pilot ~2h additional\"\n  timeline:\n    day_9: \"2026-05-23 — rebuttal letter\"\n    deadline: \"2026-05-25 — EMNLP 2026 ARR\"\n",
      "numLines": 234,
      "startLine": 1,
      "totalLines": 234
    }
  },
  "sourceToolAssistantUUID": "906cf254-bda5-4347-96f1-ef1817b089f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "589e47f3-a107-4a46-857a-74855f584341",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 15 · 2026-05-14T14:43:14.621Z_

````json
{
  "parentUuid": "09cb86c0-7ac2-47a6-91c6-137956c67a12",
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
  "uuid": "5e664a05-b985-4672-8bcb-1c37503c1187",
  "timestamp": "2026-05-14T14:43:14.621Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "589e47f3-a107-4a46-857a-74855f584341",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Runtime record

_source line 16_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：C5 pilot 边缘或失败（LLaMA 方向对但 gate 未达标），n=500 Qwen s015 仍跨零但正向趋势明显，需调整 claims 强度 核心假设：['C5 LLaMA-8B 显示正向 phase gradient 但回收 <30%（或 crossover 方向对但不显著）', 'C2 n…",
  "leafUuid": "5e664a05-b985-4672-8bcb-1c37503c1187",
  "sessionId": "589e47f3-a107-4a46-857a-74855f584341"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Median sparsity phase-strategy interaction empirical validation",
  "sessionId": "589e47f3-a107-4a46-857a-74855f584341"
}
```

---

### Assistant

_source line 18 · 2026-05-14T14:49:54.688Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full experiment plan. Let me identify all experiments that are in "planned", "running", or "pending" status (not "done"). I need to generate detailed predictions for the median tier.

Let me list the planned experiments:
1. **plan_001** (pending) - DeepSeek importance bf16 × 4 sparsity - already has registry data (bf16_importance_s015/s020/s025/s030) — these are DONE in the registry
2. **plan_002** (planned) - DeepSeek random bf16 × 4 sparsity - registry has bf16_ds_rand_s015/s020/s025/s030 — DONE


3. **plan_003** (planned) - Crossover analysis - pure analysis
4. **plan_004** (pending) - Qwen importance bf16 × 4 sparsity - registry has bf16_qw_imp_s015/s020/s025/s030 — DONE
5. **plan_005** (planned) - Qwen random bf16 × 4 sparsity - registry has bf16_qw_rand_s015/s020/s025/s030 — DONE
6. **plan_006** (planned) - Attention entropy measurement - registry has c4_entropy and qwen_c4_entropy — DONE
7. **plan_007** (planned) - Growth rate analysis - pure analysis
8. **plan_008** (planned) - Per-problem bootstrap CI - already done (bf16_ds_imp_s015/etc.)
9. **plan_009** (running) - DeepSeek n=500 — c2_n500_deepseek RUNNING
10. **plan_010** (running) - Qwen n=500 — c2_qw_n500 RUNNING
11. **plan_011** (planned) - Phase-aware mitigation pilot
12. **plan_012** (planned) - LLaMA-8B cross-architecture — c3_llama PREPARING
13. **plan_013** (planned) - Related Work differentiation - writing task
14. **plan_014** (done) - onset threshold
15. **plan_015** (done) - dose-response monotonicity

I'm noticing the plan statuses might be outdated since many of these already have registry data marked as DONE. The user is asking for predicted data for each planned experiment, but I need to check which ones genuinely still need predictions versus which already have results in the registry. The truly pending experiments that need synthetic data are the ones still running or preparing, while others like plan_001 already have completed data across multiple registry IDs.

Looking at what's actually left to predict, I should focus on the experiments that haven't finished yet: plan_009 and plan_010 are currently running, plan_011 hasn't started, and plan_012 is in preparation. But the user asked for all non-done experiments, so I should be comprehensive and include everything that isn't marked as complete. Looking at the experiment statuses, I see that plans 001-008 already have completed registry data, while 009-010 are currently running and 011-015 are either planned or done. The user's request seems to be asking for detailed predictions for each non-completed experiment, but since many already have actual data, I'm wondering if they want me to generate what median-tier predictions would look like for those as well, or just focus on the truly pending ones. Re-reading the request in Chinese, "每个 planned 实验" suggests they want predictions for experiments marked as "planned" status specifically — so I should focus on generating median-tier predictions for those entries rather than trying to predict data that's already been collected. I'm working through what the median-tier predictions should actually look like — defining the expected ranges for key metrics like the LLaMA paired differences, Cohen's d values, and whether crossover effects appear, along with stability expectations for the Qwen and DeepSeek results across different sample sizes.

Now I'm laying out the specific predictions for each remaining experiment, starting with what the DeepSeek n=500 results should show based on the current n=50 baseline data. Looking at the Qwen results with n=500, I expect s015 to stay in that 0.25-0.35 range for median difference while the confidence intervals tighten up, and all the other effect sizes should replicate with narrower bounds. For the s015 case specifically, the CI is still going to cross zero even with the larger sample, which is consistent with what I'm seeing in the current data.

Moving to the LLaMA-8B cross-architecture comparison, the median tier shows a positive phase gradient but the recovery stays below 30%, with paired differences around 0.2 to 1.0 and Cohen's d between 0.15 and 0.5—the crossover point is still ambiguous. The phase-aware mitigation pilot depends on finishing the earlier plans, and since the median recovery is below the 30% threshold, I'd expect the oracle approach to show some improvement but still fall short of the gate, with the heuristic performing even worse.

Now I need to be careful about which experiments to include in the full output and make sure I'm covering each planned experiment with the appropriate detail. I think the user wants predictions for all non-done experiments as a scenario analysis exercise — for completed ones I'll note the actual results, and for those still running I'll generate genuine predictions based on the median tier calibration.

Looking at the registry data, most experiments through plan_008 are already finished with results, while plan_009 and plan_010 are currently running, plan_012 is in preparation, and plan_011 and plan_013 haven't started yet — so those five are the ones where I need to provide forward-looking predictions.

For the completed experiments, I should base my predictions on their actual outcomes since the median tier should reflect reality. But for the truly forward-looking ones that haven't run yet, I need to generate predictions consistent with what the median tier would predict, focusing on plan_009 through plan_013 and noting which are still in progress versus which haven't begun.

The user is asking for predictions on every experiment that isn't marked as done, so I'll need to cover the full set. Let me work through each one systematically, starting with the completed data and moving to the forward-looking predictions. Also has completed registry data.

### plan_003: Crossover analysis (status: planned)
Pure analysis from plan_001+002 data. Under median tier with existing data, crossover exists at s025.

### plan_004: Qwen importance bf16 × 4 sparsity (status: pending)
Completed registry data.

### plan_005: Qwen random bf16 × 4 sparsity (status: planned)
Completed registry data.

### plan_006: Attention entropy measurement (status: planned)
Completed registry data (c4_entropy, qwen_c4_entropy).

### plan_007: Growth rate analysis (status: planned)
Pure analysis from plan_001 data.

### plan_008: Per-problem bootstrap CI (status: planned)
Completed in bf16_ds_imp_* entries.

### plan_009: DeepSeek n=500 (status: running)
Currently executing, waiting on genuine predictions.

### plan_010: Qwen n=500 (status: running)
Currently executing, waiting on genuine predictions.

### plan_011: Phase-aware mitigation pilot (status: planned)
Not started, depends on predictions.

### plan_012: LLaMA-8B (status: planned)
Preparing, depends on predictions.

### plan_013: Related Work differentiation (status: planned)
Writing task, no experiment data needed.

I'm realizing the user probably cares most about experiments that generate new data. The completed ones are done, the analysis-only tasks work from what's already there, and the writing doesn't require experimental results. So the experiments that actually need median-tier predictions are DeepSeek and Qwen at n=500.

Now I'm looking at the current n=50 importance scores to extrapolate what n=500 might show. I'm examining the confidence intervals and effect sizes across different sparsity levels to estimate how the patterns might scale up.

The median tier's prediction of only 15-35% CI width reduction seems surprisingly conservative given that 10× more data should theoretically narrow confidence intervals by about 68%. This suggests high variance across problems and diminishing returns from simply collecting more data. 15-35% reduction would suggest high heterogeneity or that the bootstrap was already saturating. Hmm, but the per-problem bootstrap with n=50 already used B=10000 bootstrap resamples — the n here is the number of problems (effective pairs), not bootstrap iterations. Going from 50 to 500 problems should shrink CI by about 1 - 1/√10 ≈ 68%.

The median tier says 15-35% CI width reduction — this seems deliberately conservative. Maybe it's reflecting that MATH-500 includes many very easy problems that don't differentiate well (floor/ceiling effects), so effective n doesn't scale linearly.

OK, for median tier predictions:

**DeepSeek n=500 importance:**
- s015: median_diff ≈ 0.30, CI=[0.19, 0.43], CI_width ≈ 0.24 → ~12% reduction, which is below the 15% floor

Let me reconsider the metric definition more carefully. The CI width reduction for DeepSeek is specified as 15-35%, and for s015 specifically the median difference should be 0.25-0.35. Currently at 0.3236, that stays in range. The current CI width of 0.273 would shrink by about 25% to roughly 0.205, giving a new interval around [0.20, 0.40]. Now I need to work through the same logic for s020.

For Qwen with n=500, the s015 median difference is quite small at 0.0476, with a CI that barely crosses zero. Even with a modest reduction, the interval would stay near [-0.005, 0.085] or [-0.008, 0.095], still straddling zero.

LLaMA-8B's s025 shows a paired median difference in the 0.2-1.0 range with Cohen's d between 0.15-0.5, which suggests the phase gradient is present but weak — possibly only significant at the relaxation point.

For the mitigation pilot, C5 falls into the "pilot edge/failure" category under the median tier, and since oracle recovery is below 30%, this experiment would demonstrate directional proof of concept but wouldn't meet the gate criteria. I'm classifying it as suggestive and moving it to the discussion section.

Now I'm structuring the YAML to capture all experiments systematically, using actual data where I have it and predictions for the rest. I'll organize this across all non-done experiments from plan_001 through plan_013.

Generating YAML structure... I need to clarify my approach here. The user asked for predictions for each planned experiment, so I should generate expected results for all of them — for the completed ones, that's just the actual data from the registry, and for the pending and running ones, I'll generate predictions based on the median tier assumptions. This way I'm providing a complete picture of what the median tier would expect across the entire experiment plan.

Now I'll write out the YAML with comprehensive coverage, making sure each prediction includes a clear rationale explaining why that result would occur under these conditions.

Generating the YAML structure... Generating the prediction table...

Now I'm looking at the Qwen baseline results with n=50, and the s015 sparsity level still has a confidence interval that crosses zero, which means the median difference is essentially negligible at around 0.04 to 0.

06. When I scale up to n=500 predictions, the pattern holds—s015 remains inconclusive with its interval still crossing zero, while s020 and beyond show clearer separation. Moving to the LLaMA-8B model, I'm predicting a paired median difference of 0.5 at the s025 sparsity tier.

For s030, I'm extrapolating based on the ratio pattern I see in DeepSeek—where s030 is about 2.5 times larger than s025—which would put LLaMA's s030 estimate around 1.25. The crossover between importance and random baselines remains ambiguous with overlapping confidence intervals, though the phase gradient is present if modest. Since recovery falls below the 30% threshold, I'd classify this pilot as suggestive rather than conclusive.

Now I'm clarifying what the recovery gate actually means: the phase-gated approach needs to recover at least 30% of the compound degradation to warrant a full rollout. For plan_012 with LLaMA-8B, the prediction shows a positive phase gradient is present, but the magnitude is too small—recovery stays below that 30% threshold. So C5 is testing both the validation (does LLaMA show the phase gradient?) and the mitigation (can we recover >30% of the degradation?). The median tier hypothesis shows the validation part worked directionally—phase gradient is there but weak, crossover direction is correct—but the mitigation gate failed at <30% recovery. This means plan_012 demonstrates the phase effect exists on LLaMA but the recovery mechanism didn't meet the threshold.

For plan_011, if it runs, the oracle would recover around 20-25% and the heuristic even less, both falling short of the gate. Now I'm ready to write out the comprehensive YAML with expected results for the analysis-only tasks and the existing entropy data for plan_006, then move on to plan_013 which is purely narrative.

Generating YAML structure... I'm deciding whether to include predictions for all 13 experiments or just the forward-looking ones. The user asked for "每个 planned 实验" — every planned experiment — so I should be comprehensive and include all of them. For the completed experiments with actual results, I'll note that the data is already in hand rather than treating them as predictions. Let me structure this to cover all 13 plans, distinguishing between genuine forecasts for the unknowns and documented outcomes for the finished work.

Generating the YAML output... / suggestive pilot" into §5 Discussion rather than §4 Results, or as supplementary evidence in the Appendix. I'm reframing C2's narrative around a threshold effect—the compound effect emerges above a critical sparsity level, with Qwen s015 serving as a boundary condition. The title should drop "across architectures" and instead emphasize cross-model replication within the Qwen family, contrasting distillation versus instruction tuning. For RC1, I'll acknowledge the same-architecture limitation honestly, using the mechanism's architecture-agnostic properties as indirect support. The contributions narrow to three points: discovering the effect and validating it across training methods within the same family, quantifying gradient dependence on sparsity thresholds, and characterizing the discrimination collapse mechanism. This remains a solid empirical finding for EMNLP.

Now I'm reviewing the completed DeepSeek importance experiments in bf16 precision across multiple sparsity levels, with median differences and effect sizes already measured. The experiment confirms phase-modulated severity across all sparsity levels with strong statistical support (p<0.005 post-Bonferroni, medium to large effect sizes), establishing the foundation for median tier predictions. Now I'm moving into the random bf16 variant for DeepSeek to validate these patterns under different initialization conditions. The random masking control shows a flat response pattern across all sparsity levels with no systematic phase gradient, which starkly contrasts with the strong monotonic gradient seen in importance masking—this directly supports the core claim that performance depends on the masking strategy. The median difference at s030 reaches 1.54 but lacks directional consistency across tiers, confirming that the phase-strategy relationship holds even when baseline effects are present.

Now I'm extracting crossover patterns from the bf16 importance versus random data to verify directional reversals across phases. The metrics show importance masking produces much lower intermediate impact in the high phase (0.032 vs 0.818 for random) but higher impact in the low phase (7.196 vs 1.363), indicating a clear crossover where the two strategies diverge in opposite directions depending on the phase. The crossover pattern is confirmed as a robust finding across the median tier in DeepSeek — this is the paper's most novel contribution, since prior work hasn't documented how compound interactions between strategy and reasoning phase can reverse direction. This directly validates the emergent phase-strategy interaction framework, and I'm now moving into the Qwen importance bf16 analysis across the four sparsity levels. Looking at the statistical results for the remaining scale factors, s030 shows a Cohen's d of 1.4394, and the onset threshold where effects become significant is s020. Comparing to DeepSeek's results, Qwen demonstrates the same monotonic increase pattern but at roughly one-quarter the magnitude, with the critical finding that s015's confidence interval crosses zero, indicating the compound effect is at a boundary condition for that scale factor.

The difference in magnitude between models likely stems from how Qwen was trained with instruction tuning rather than distillation, which affects attention patterns. To determine whether s015 represents a true effect or just noise at the current sample size of 50, I'd need to scale up to around 500 samples. Now I'm moving into the Qwen random bf16 experiments to continue validating these patterns. Looking at the s030 results more closely—the permutation p-value of 0.012 suggests statistical significance, but Cohen's d of -0.035 shows the actual effect is negligible. This is the one exception in the pattern of random masking failures across sparsity levels, but it's important to note in the paper that statistical significance doesn't equal practical significance here. The median difference of 2.418 is real, but the effect size tells us it's not meaningful in context, so I need to make sure this distinction is clear to avoid misinterpretation during review.

Now moving to plan_006 on attention entropy and discrimination mechanisms—I'm measuring how attention entropy and importance score distributions differ between pruned and unpruned models to understand the collapse in discrimination capacity. The discrimination collapse mechanism shows consistent direction across models in Gini and CV metrics, making it the primary explanation, though entropy redistribution proves less reliable in Qwen with directional reversals at certain sample sizes—so I'm positioning that as a secondary, model-specific effect. The core finding about Gini/CV alignment is already established, so the paper's narrative should center on discrimination collapse while treating entropy as a supporting detail that varies by model. I'm planning to present this through a discrimination metrics table and a heatmap comparing the coefficient deltas between DeepSeek and Qwen.

Now I'm analyzing growth rate patterns from the gradient data across sparsity levels, looking at how the median differences scale—the sequence shows decreasing growth factors as sparsity increases, which suggests the effect plateaus at higher levels. The sub-exponential growth pattern is actually reassuring for deployment—compound severity increases with sparsity but at a decelerating rate, so it's not a catastrophic explosion. I'm now moving into bootstrap confidence interval analysis for the bf16 data to validate these findings. The statistical framework is holding up well—even after Bonferroni correction, all conditions show significance except for Qwen s015, which has a borderline confidence interval that crosses zero. This is exactly what motivated expanding to n=500 for a more definitive result. Now I'm moving into the DeepSeek n=500 experiment to boost statistical power across all eight conditions. I'm noticing the confidence interval width reduction for s030 is slightly above the 35% upper bound, so I need to recalculate these values more carefully to keep them within the [15, 35] range for this tier.

Now I'm thinking through how the sample size scaling affects the confidence intervals — with n=500 problems instead of n=50, the standard error should decrease proportionally to 1/√n, which would give roughly a 3× narrowing. But the tier only allows 15-35% reduction, suggesting that most of the variance comes from heterogeneity across problems rather than sampling variability, so the CI width won't narrow as much as the raw sample size increase would suggest. Now I'm recalculating the confidence intervals for each scenario using a 25% reduction in width, which aligns with the median tier's conservative estimate. I'm working through the specific values for each sample size, computing the narrowed widths and corresponding confidence interval bounds around the median differences.

The random condition tests are all failing across the board, and there's no systematic phase dependence showing up in the gradient analysis. The Bonferroni correction confirms significance, the monotonic gradient holds, and I'm noting that the actual narrowing in the MATH-500 dataset falls well short of the theoretical √10 expectation—likely due to heterogeneity in the problem distribution. 包含大量简单题目（Phase-0 reasoning），这些题目的 compound interaction 接近零（floor effect），对 paired median difference 贡献有限。有效配对数从 49 增至约 400-450（部分题目因 phase assignment 不足被排除），但 per-problem II 分布高度偏斜（skewness 4-16），median 的 bootstrap CI 不如 mean 收窄快。点估计保持稳定（median_diff 变化 <10%），说明 n=50 的估计已经是合理的。Random 对照在扩大样本后仍然 FAIL，进一步巩固 strategy-dependent 的结论。

现在我在整理 n=500 更新的 CI 收窄对比、按稀疏度分类的 CI 宽度缩减总结，以及森林图和 per-problem II 分布的可视化来展示异质性。n=500 的主要价值不在于改变结论（n=50 已经显著），而是消除 sampling bias 的疑虑，并为 meta-analysis 提供更精确的 effect size 估计。DeepSeek 端没有意外——这是 median tier 的表现。

接下来是 Qwen 的 n=500 统计功效提升实验，涵盖 8 个条件（importance/random × 4 个稀疏度水平），从 n=50 扩展到 n=500。这是关键实验，预测 importance 条件下的 median difference 约 0.045，Cohen's d 约 0.35，置信区间 [-0.005, 0.095]，仍然跨越零。

在 s015 稀疏度下，未校正的 Wilcoxon p 值约 0.04（边界显著），但 Bonferroni 校正后 p 值为 0.16（不显著）。而在更高稀疏度 s020 和 s025 条件下，median difference 和 effect size 显著增大，置信区间不再跨越零，Bonferroni 校正后 p 值都小于 0.001。

s030 条件下 effect size 继续增强至 1.38，同样达到高度显著。相比之下，随机条件下只有 s030 通过检验（p=0.008，但 effect size 可忽略不计），其他稀疏度都失败了。这表明复合效应在 s020 附近出现阈值。

现在看 Qwen s015 为什么在 n=500 时仍然无法达到统计显著性——真实 effect size 非常小（约 0.35-0.37），即使样本量这么大也只能达到约 60% 的统计功效。Qwen 的指令微调导致注意力头的重要性分布更均匀，在低稀疏度下交互效应接近噪声水平。虽然中位数的配对差异是正向的，但分布的下四分位数接近零甚至略负，这在 bootstrap 重采样时会产生很大的不确定性。

当样本量从 50 增加到 500 时，中位差从 0.048 略微下降到 0.045，说明更多数据削弱了少数离群题目的影响，置信区间也从 [-0.005, 0.110] 收窄到 [-0.005, 0.095]，但下界仍然跨越零。相比之下，s020 及以上的稀疏度在 n=500 后置信区间明确远离零，这直接支持了一个阈值效应的解释——复合效应在 s≥0.020 处才真正显现，这与 DeepSeek 在 s015 就已显著的表现形成了鲜明对比，可以用模型相关的阈值差异来讨论。

我需要更新表格和图表来反映这些发现，特别是 Qwen 在 n=500 时的置信区间和 s015 处的分布情况。关键的叙事转变是：Qwen s015 的不显著结果不是失败，而是一个有信息量的零假设，它定义了复合效应的起始边界，支持了阈值框架的论点——相位调制效应只在稀疏度超过某个阈值时才出现。

现在我在规划一个 2 小时的试点研究，测试相位感知的缓解策略。我会用预言机分配（上界）和启发式方法（下界）来评估在 s025 和 s030 上的恢复潜力，预期复合困惑度能分别从 63.7 和 122.6 降低到约 49.8 和 100.5。

不过根据初步分析，即使完美的相位分配也只能恢复 18-22% 的性能，因为复合交互作用涉及多个层级和注意力头之间的不可分解的相互作用，这意味着这个方向可能不会达到 30% 的通过门槛。

用位置比率作为相位代理的启发式方法准确率约 65-70%，所以实际恢复只有预言机上界的 55%，虽然这个试点没有通过门槛进入主实验，但它为未来工作提供了有价值的理论基准。

我可以把这个失败转化为叙事优势：即使有完美的相位知识，也只能恢复约 20% 的复合退化，这说明仅靠相位感知的驱逐策略是不够的，根本问题在于判别能力的崩溃。现在我在准备 LLaMA-8B 的跨架构验证。

我预测在 DeepSeek-R1-Distill-Llama-8B 上会看到相位调制的复合严重性，但效果会比较弱——中位数差异在 0.55 到 1.40 之间，Cohen's d 在 0.30 到 0.42，统计显著性勉强通过 Bonferroni 校正。

交叉点方向正确但不显著，效应量约为 DeepSeek 的 1/7、Qwen 的 1/2，而且判别能力的衰减（Gini 和变异系数）方向一致但幅度较小。

LLaMA-8B 的结果更多是暗示性的，可能放在讨论或附录中。这个较弱的效应源于 LLaMA 的分组查询注意力架构与 Qwen 的混合方案不同——共享的 KV 头部使得剪枝的相位依赖性被平滑化了。

DeepSeek-R1-Distill-Llama-8B 虽然采用 LLaMA 架构但经过蒸馏，其注意力模式介于原生 LLaMA 和 DeepSeek 之间，导致效应量更小。样本量 n=50 对于检测 d=0.30 的功效仅约 0.35，所以置信区间较宽且结果处于边界显著性。交叉点方向正确但因随机基线本身的方差，差异未达显著——标记为模糊。Gini 和变异系数的判别方向一致但幅度更小，这支持了机制的架构依赖性。

LLaMA 结果在中位数层级下不足以支撑跨架构的主张，Cohen's d 在 0.30-0.42 范围属于小到中等效应量，交叉点结果模糊。我需要将这部分降级为初步证据，移至讨论或附录部分，并从标题中删除"跨架构"的表述。方向一致性虽然存在，但不足以构成强有力的证据。

现在我在规划如何在相关工作部分区分 Lethe 和 SparK 这两个方法。Lethe 采用层-时间自适应的 KV 剪枝，只在单一维度上操作，而我们的方法在头部剪枝、KV 驱逐和阶段策略之间实现了三维交互。SparK 虽然也做联合压缩，但假设复合交互是均匀的，而我们的发现表明情况更加复杂。

我需要补充两段新内容和四个引用，来清楚地阐明我们在复合交互、阶段依赖性和策略选择上的独特贡献。

Lethe 的时间自适应机制与我们的阶段门控看似相似，但它没有分析复合交互；SparK 虽然分析复合效应，却假设交互是均匀的——而我们的核心发现恰好推翻了这个假设。关键是要把定位从"我们做得更多"转向"我们发现了一个新维度：阶段依赖的梯度"。

现在我在验证所有关键指标的约束范围，确保数值在预期区间内且相互一致。

对于DeepSeek的n=500置信区间宽度缩减，我逐个检查了不同标准差设置下的百分比，发现s030的35.8%略微超出了[15, 35]的范围，需要调整。

重新计算后，将s030的新宽度改为5.50，得到33.4%的缩减，这样所有四个标准差设置的缩减比例都落在目标范围内。不过我注意到s030的当前置信区间宽度是8.261，需要再次核实这个数值。

现在检查s030的新预测区间[8.20, 13.80]是否合理——宽度为5.60，缩减32.2%，中位数差为9.70。虽然区间不对称（下方偏离1.50，上方偏离4.10），但这对于偏斜分布来说是合理的。接下来我要整理最终的YAML配置，然后仔细思考plan_011中"复合恢复"的含义——需要在s025处检查DeepSeek的复合困惑度数据。

现在看bf16_importance_s025的实际数据：高阶段的复合退化为1.5337（或2.31倍比率），低阶段则严重得多，达到62.44（51.8倍比率）。阶段感知的缓解策略是在低阶段使用较低稀疏度，在高阶段使用较高稀疏度，而预言机恢复意味着精确知道每个token所在的阶段。

在计算匹配的约束下，如果在低阶段降低稀疏度，就必须在高阶段增加稀疏度或减少总压缩比，这使得恢复变得困难得多。中位数层的预言机恢复约20%的事实反映了这个预算约束——你不能简单地到处使用低稀疏度。

现在我需要为Qwen n=500的随机条件做预测，然后完成YAML配置。

基于n=50的基线数据，我预计s015、s020和s025在更大样本量下仍会失败，而s030应该保持通过，效果差异不大。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e664a05-b985-4672-8bcb-1c37503c1187",
  "isSidechain": false,
  "requestId": "req_011Cb2dzQBYWbAWEZo6vwcPo",
  "type": "assistant",
  "uuid": "b13935d2-9aed-4f11-b53d-e1f3e5227dda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "589e47f3-a107-4a46-857a-74855f584341",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014wvYSHHWfGkKHoxcWGQ2BN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8373,
      "cache_read_input_tokens": 40689,
      "output_tokens": 20500,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8373,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 20500,
          "cache_read_input_tokens": 40689,
          "cache_creation_input_tokens": 8373,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8373
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

_source line 19 · 2026-05-14T14:49:54.696Z_

Now let me read the full experiment plan and check if there's any additional context about the running experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b13935d2-9aed-4f11-b53d-e1f3e5227dda",
  "isSidechain": false,
  "requestId": "req_011Cb2dzQBYWbAWEZo6vwcPo",
  "type": "assistant",
  "uuid": "8ad0c4d2-18dc-4db2-99db-b2efad26cbe3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "589e47f3-a107-4a46-857a-74855f584341",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014wvYSHHWfGkKHoxcWGQ2BN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8373,
      "cache_read_input_tokens": 40689,
      "output_tokens": 20500,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8373,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 20500,
          "cache_read_input_tokens": 40689,
          "cache_creation_input_tokens": 8373,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8373
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

_source line 20 · 2026-05-14T14:49:55.999Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ckidf38h1kjJDeSvvbSaBo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_framing.md",
  "offset": 0,
  "limit": 60
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ad0c4d2-18dc-4db2-99db-b2efad26cbe3",
  "isSidechain": false,
  "requestId": "req_011Cb2dzQBYWbAWEZo6vwcPo",
  "type": "assistant",
  "uuid": "261cce3b-332e-480b-b260-cf51c2e6bad6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "589e47f3-a107-4a46-857a-74855f584341",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014wvYSHHWfGkKHoxcWGQ2BN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8373,
      "cache_read_input_tokens": 40689,
      "output_tokens": 20500,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8373,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 20500,
          "cache_read_input_tokens": 40689,
          "cache_creation_input_tokens": 8373,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8373
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

_source line 21 · 2026-05-14T14:49:56.013Z_

<details><summary>↩ Tool result · `toolu_01Ckidf38h1kjJDeSvvbSaBo`</summary>

```text
0	# Paper Framing — Phase-Gated Compound Sparsity
1	
2	> 最后更新: 2026-05-14 (D052 审稿应对调整) | 维护者: Director
3	
4	## Core Insight
5	
6	Compound sparsity（attention head pruning + KV cache eviction）的 severity 不是固定常数——它是 eviction strategy 和 reasoning phase 交互的涌现属性。Importance-based eviction 的 compound interaction severity（paired median difference: median(II_low_i − II_high_i)）随 sparsity 单调递增（DeepSeek: 0.32→1.15→3.97→9.94; Qwen: 0.048→0.208→1.109→2.619），而 random masking 三相 II 持平（7/8 FAIL; Qwen s030 PASS p=0.012 but d=-0.04 negligible）。Cohen's d（paired d_z, B=10000）从 small-medium 到 large（DeepSeek: 0.44→0.80; Qwen: 0.28→1.02，s015 边缘）。这一发现挑战了 compound degradation 均匀分布的隐含假设。
7	
8	**数字基准**：所有数字基于 bf16 per-problem paired 统计量（B=10000 bootstrap）。median_diff 定义为 median(II_low_i − II_high_i)（逐 problem 配对差的中位数）。fp16 旧数据已弃用。
9	
10	## Narrative Arc
11	
12	Compound sparsity 是高效 LLM 推理的实用部署需求，但 prior work（SparK, Ada-KV, SLiM）将 compound interaction 视为均匀超可加。我们发现 severity 是 strategy × phase 交互的涌现属性：importance eviction 的 compound interaction 在 low-sparsity phase 远大于 high-sparsity phase（paired median difference 单调递增 0.32→9.94），而 random eviction 在所有 phase 保持平坦（7/8 FAIL; 唯一例外 Qwen s030 p=0.012 效应量可忽略 d=-0.04）。Cross-model replication 方向一致（Qwen magnitude ~1/4 of DeepSeek，onset threshold s≥0.20）。C3 crossover 现象的 LLaMA 架构验证已列入计划（plan_012 pilot-first），以测试发现的跨架构泛化性。我们通过 discrimination collapse 机制解释这一现象：head pruning → importance score 的判别力崩塌（Gini/CV 下降跨模型一致）→ importance eviction 退化为有偏伪随机。Attention entropy redistribution 作为 model-dependent secondary effect 在 DeepSeek 上观察到，但在 Qwen 上不稳健（D044）。
13	
14	**Framing 硬约束（D015）**：
15	- MUST: \"emergent phase-strategy interaction\"
16	- MUST NOT: \"importance metric limitation / importance is broken\"
17	- MUST NOT: claim \"importance masking produces super-additive interaction\" without qualifier — random masking also produces positive II. The distinguishing signal is **phase-dependent gradient** (importance: paired median difference 0.32→9.94 单调递增 vs random: 7/8 FAIL), not the existence of super-additivity itself (D023)
18	
19	## Core Claims
20	
21	| ID | Claim | Status | Key Evidence |
22	|----|-------|--------|-------------|
23	| C1 | Compound sparsity severity is strategy-dependent | confirmed | importance paired median diff 0.32→9.94 单调递增 vs random 7/8 FAIL (bf16; Qwen s030 PASS p=0.012 d=-0.04 negligible) |
24	| C2 | Severity is phase-modulated (amplified in low-sparsity phase) | confirmed | bf16 paired median difference 单调递增: 0.32→1.15→3.97→9.94; Bonferroni p<0.005 全 4 水平 (D032)。预注册：n=500 后若 QW s015 CI 仍跨零，叙事改为 'compound effect emerges above threshold sparsity (~s020)' |
25	| C3 | Phase-strategy crossover exists | confirmed | s=0.25: importance high_phase=0.032 < random=0.818, importance low_phase=7.196 > random=1.363 (bf16) |
26	| C4 | Discrimination collapse as primary mechanism; entropy redistribution model-dependent | partially_confirmed | D044: Gini/CV 下降跨模型一致; entropy collapse DeepSeek 一致但 Qwen s025 反转(+0.045) s030≈0。30/30 problems completed. |
27	| C5 | Phase-modulated compound severity generalizes across architectures | pilot_pending | Pilot-first: 2h oracle + heuristic (token position ratio as phase proxy) on LLaMA-8B, s025/s030. Gate: recover >30% compound degradation → full rollout; else → future work. Must include heuristic baseline (oracle upper bound + simple heuristic lower bound). |
28	| C5b | Phase-aware mitigation recovers compound degradation | planned | pilot: oracle + heuristic (token position ratio) on s025/s030, >30% recovery threshold |
29	| C6 | Severity gradient is sub-exponential | confirmed | Growth rate decreasing: Δ增长因子 3.8×→4.8×→2.0×（递减） |
30	| C7 | Statistical power at n=500 confirms dose-response | running | c2_n500_deepseek + c2_qw_n500 (n=500, 8 conditions each) |
31	| C8 | Cross-architecture validation (LLaMA) | planned | c3_llama (DeepSeek-R1-Distill-Llama-8B) |
32	| C9 | Differentiation from Lethe/SparK prior work | planned | Related Work §2 引用区分 + SparK gap analysis |
33	| S3→C | Onset threshold is model-dependent (DeepSeek s≥0.15, Qwen s≥0.20) | confirmed | D037/D038: Qwen s015 d=0.28 CI含0, s020+ 显著 |
34	| S7→C | Dose-response monotonicity (Spearman ρ=1.0) | confirmed | D047: 6-point dose-response, 单调递增 |
35	
36	## Anticipated Reviewer Concerns
37	
38	### RC1: Generalizability — 7B models only, single benchmark
39	- **预期质疑**: "Results on two 7B models and MATH-500 only. How do we know this generalizes to larger models or other reasoning tasks?"
40	- **应对**: Cross-model replication (DeepSeek-R1-Distill-Qwen-7B + Qwen2.5-7B-Instruct) 控制架构变量、隔离训练方式影响（distillation vs instruction tuning）。注意：两模型共享 Qwen2ForCausalLM 架构，不能 claim 跨架构泛化。MATH-500 是 standard benchmark。Limitations 必须诚实声明：(1) 同架构不同训练，不是跨架构；(2) 7B scale only；(3) 单 benchmark。机制解释 (discrimination collapse) 原则上 architecture-agnostic，但未实证验证。
41	- **实验支撑**: C5 (Qwen cross-model). 若需加强可扩展到不同架构（如 LLaMA/Mistral），但 11 天 deadline 内不现实
42	
43	### RC2: Mechanism — entropy-discrimination collapse 缺乏直接测量
44	- **预期质疑**: "The mechanism is conceptual. Where is the empirical evidence for entropy increase and discrimination collapse?"
45	- **应对**: c4_entropy 实验已完成（DeepSeek 30/30 + Qwen 30/30）。D044 结论：Gini/CV 下降跨模型一致（discrimination collapse confirmed）；entropy redistribution 在 DeepSeek 上一致但在 Qwen 上 s025 方向反转、s030 近零（model-dependent）。论文以 discrimination collapse 为主线，entropy 作 DeepSeek 特有的强化因素。
46	- **实验支撑**: c4_entropy (DeepSeek DONE) + qwen_c4_entropy (DONE, negative for entropy universality)
47	
48	### RC3: Practical impact — 没有 throughput 数据
49	- **预期质疑**: "No wall-clock or throughput measurements. Is the severity amplification reflected in actual inference speed?"
50	- **应对**: 本文定位是 empirical finding paper（发现 + 机制解释），不是 method paper。Throughput 不是 claim 的一部分。Discussion 中明确 phase-gated controller 作为 future direction。
51	  - C5b pilot-first 策略：先 2h 在 s025/s030 上测 oracle upper bound + simple heuristic (token position ratio as phase proxy)。Oracle 回收 >30% compound degradation 才全面铺开，否则降为 future work
52	  - Heuristic baseline 必须包含：oracle 上界 + simple heuristic 下界，compute-matched
53	- **实验支撑**: 不需要额外实验（mitigation pilot 见 C5b / plan_011）
54	
55	### RC4: Statistical rigor — bootstrap 是否足够
56	- **预期质疑**: "Per-problem bootstrap with 50 problems — sufficient sample size?"
57	- **应对**: bf16 使用 B=10000 per-problem paired bootstrap，有效配对数 n=49 (DeepSeek) / n=46 (Qwen)。Permutation test 使用 paired median difference 作为 robust statistic（D032），Bonferroni 校正后全 4 水平 p<0.005。Cohen's d（paired d_z）作为辅助效应量（DeepSeek 0.44→0.80, Qwen 0.28→1.02）。可在 appendix 补充 per-problem 分布图（已生成 fig4_per_problem_dist.pdf）。
58	- **实验支撑**: bf16 permutation test (D032) + Cohen's d per-problem paired (rebootstrap B=10000) 已完成
59	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "261cce3b-332e-480b-b260-cf51c2e6bad6",
  "isSidechain": false,
  "promptId": "b0df8920-d739-47eb-a93d-268a74684922",
  "type": "user",
  "uuid": "60917afe-4e07-40d7-82fc-1a800eb415c5",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_framing.md",
      "content": "# Paper Framing — Phase-Gated Compound Sparsity\n\n> 最后更新: 2026-05-14 (D052 审稿应对调整) | 维护者: Director\n\n## Core Insight\n\nCompound sparsity（attention head pruning + KV cache eviction）的 severity 不是固定常数——它是 eviction strategy 和 reasoning phase 交互的涌现属性。Importance-based eviction 的 compound interaction severity（paired median difference: median(II_low_i − II_high_i)）随 sparsity 单调递增（DeepSeek: 0.32→1.15→3.97→9.94; Qwen: 0.048→0.208→1.109→2.619），而 random masking 三相 II 持平（7/8 FAIL; Qwen s030 PASS p=0.012 but d=-0.04 negligible）。Cohen's d（paired d_z, B=10000）从 small-medium 到 large（DeepSeek: 0.44→0.80; Qwen: 0.28→1.02，s015 边缘）。这一发现挑战了 compound degradation 均匀分布的隐含假设。\n\n**数字基准**：所有数字基于 bf16 per-problem paired 统计量（B=10000 bootstrap）。median_diff 定义为 median(II_low_i − II_high_i)（逐 problem 配对差的中位数）。fp16 旧数据已弃用。\n\n## Narrative Arc\n\nCompound sparsity 是高效 LLM 推理的实用部署需求，但 prior work（SparK, Ada-KV, SLiM）将 compound interaction 视为均匀超可加。我们发现 severity 是 strategy × phase 交互的涌现属性：importance eviction 的 compound interaction 在 low-sparsity phase 远大于 high-sparsity phase（paired median difference 单调递增 0.32→9.94），而 random eviction 在所有 phase 保持平坦（7/8 FAIL; 唯一例外 Qwen s030 p=0.012 效应量可忽略 d=-0.04）。Cross-model replication 方向一致（Qwen magnitude ~1/4 of DeepSeek，onset threshold s≥0.20）。C3 crossover 现象的 LLaMA 架构验证已列入计划（plan_012 pilot-first），以测试发现的跨架构泛化性。我们通过 discrimination collapse 机制解释这一现象：head pruning → importance score 的判别力崩塌（Gini/CV 下降跨模型一致）→ importance eviction 退化为有偏伪随机。Attention entropy redistribution 作为 model-dependent secondary effect 在 DeepSeek 上观察到，但在 Qwen 上不稳健（D044）。\n\n**Framing 硬约束（D015）**：\n- MUST: \\\"emergent phase-strategy interaction\\\"\n- MUST NOT: \\\"importance metric limitation / importance is broken\\\"\n- MUST NOT: claim \\\"importance masking produces super-additive interaction\\\" without qualifier — random masking also produces positive II. The distinguishing signal is **phase-dependent gradient** (importance: paired median difference 0.32→9.94 单调递增 vs random: 7/8 FAIL), not the existence of super-additivity itself (D023)\n\n## Core Claims\n\n| ID | Claim | Status | Key Evidence |\n|----|-------|--------|-------------|\n| C1 | Compound sparsity severity is strategy-dependent | confirmed | importance paired median diff 0.32→9.94 单调递增 vs random 7/8 FAIL (bf16; Qwen s030 PASS p=0.012 d=-0.04 negligible) |\n| C2 | Severity is phase-modulated (amplified in low-sparsity phase) | confirmed | bf16 paired median difference 单调递增: 0.32→1.15→3.97→9.94; Bonferroni p<0.005 全 4 水平 (D032)。预注册：n=500 后若 QW s015 CI 仍跨零，叙事改为 'compound effect emerges above threshold sparsity (~s020)' |\n| C3 | Phase-strategy crossover exists | confirmed | s=0.25: importance high_phase=0.032 < random=0.818, importance low_phase=7.196 > random=1.363 (bf16) |\n| C4 | Discrimination collapse as primary mechanism; entropy redistribution model-dependent | partially_confirmed | D044: Gini/CV 下降跨模型一致; entropy collapse DeepSeek 一致但 Qwen s025 反转(+0.045) s030≈0。30/30 problems completed. |\n| C5 | Phase-modulated compound severity generalizes across architectures | pilot_pending | Pilot-first: 2h oracle + heuristic (token position ratio as phase proxy) on LLaMA-8B, s025/s030. Gate: recover >30% compound degradation → full rollout; else → future work. Must include heuristic baseline (oracle upper bound + simple heuristic lower bound). |\n| C5b | Phase-aware mitigation recovers compound degradation | planned | pilot: oracle + heuristic (token position ratio) on s025/s030, >30% recovery threshold |\n| C6 | Severity gradient is sub-exponential | confirmed | Growth rate decreasing: Δ增长因子 3.8×→4.8×→2.0×（递减） |\n| C7 | Statistical power at n=500 confirms dose-response | running | c2_n500_deepseek + c2_qw_n500 (n=500, 8 conditions each) |\n| C8 | Cross-architecture validation (LLaMA) | planned | c3_llama (DeepSeek-R1-Distill-Llama-8B) |\n| C9 | Differentiation from Lethe/SparK prior work | planned | Related Work §2 引用区分 + SparK gap analysis |\n| S3→C | Onset threshold is model-dependent (DeepSeek s≥0.15, Qwen s≥0.20) | confirmed | D037/D038: Qwen s015 d=0.28 CI含0, s020+ 显著 |\n| S7→C | Dose-response monotonicity (Spearman ρ=1.0) | confirmed | D047: 6-point dose-response, 单调递增 |\n\n## Anticipated Reviewer Concerns\n\n### RC1: Generalizability — 7B models only, single benchmark\n- **预期质疑**: \"Results on two 7B models and MATH-500 only. How do we know this generalizes to larger models or other reasoning tasks?\"\n- **应对**: Cross-model replication (DeepSeek-R1-Distill-Qwen-7B + Qwen2.5-7B-Instruct) 控制架构变量、隔离训练方式影响（distillation vs instruction tuning）。注意：两模型共享 Qwen2ForCausalLM 架构，不能 claim 跨架构泛化。MATH-500 是 standard benchmark。Limitations 必须诚实声明：(1) 同架构不同训练，不是跨架构；(2) 7B scale only；(3) 单 benchmark。机制解释 (discrimination collapse) 原则上 architecture-agnostic，但未实证验证。\n- **实验支撑**: C5 (Qwen cross-model). 若需加强可扩展到不同架构（如 LLaMA/Mistral），但 11 天 deadline 内不现实\n\n### RC2: Mechanism — entropy-discrimination collapse 缺乏直接测量\n- **预期质疑**: \"The mechanism is conceptual. Where is the empirical evidence for entropy increase and discrimination collapse?\"\n- **应对**: c4_entropy 实验已完成（DeepSeek 30/30 + Qwen 30/30）。D044 结论：Gini/CV 下降跨模型一致（discrimination collapse confirmed）；entropy redistribution 在 DeepSeek 上一致但在 Qwen 上 s025 方向反转、s030 近零（model-dependent）。论文以 discrimination collapse 为主线，entropy 作 DeepSeek 特有的强化因素。\n- **实验支撑**: c4_entropy (DeepSeek DONE) + qwen_c4_entropy (DONE, negative for entropy universality)\n\n### RC3: Practical impact — 没有 throughput 数据\n- **预期质疑**: \"No wall-clock or throughput measurements. Is the severity amplification reflected in actual inference speed?\"\n- **应对**: 本文定位是 empirical finding paper（发现 + 机制解释），不是 method paper。Throughput 不是 claim 的一部分。Discussion 中明确 phase-gated controller 作为 future direction。\n  - C5b pilot-first 策略：先 2h 在 s025/s030 上测 oracle upper bound + simple heuristic (token position ratio as phase proxy)。Oracle 回收 >30% compound degradation 才全面铺开，否则降为 future work\n  - Heuristic baseline 必须包含：oracle 上界 + simple heuristic 下界，compute-matched\n- **实验支撑**: 不需要额外实验（mitigation pilot 见 C5b / plan_011）\n\n### RC4: Statistical rigor — bootstrap 是否足够\n- **预期质疑**: \"Per-problem bootstrap with 50 problems — sufficient sample size?\"\n- **应对**: bf16 使用 B=10000 per-problem paired bootstrap，有效配对数 n=49 (DeepSeek) / n=46 (Qwen)。Permutation test 使用 paired median difference 作为 robust statistic（D032），Bonferroni 校正后全 4 水平 p<0.005。Cohen's d（paired d_z）作为辅助效应量（DeepSeek 0.44→0.80, Qwen 0.28→1.02）。可在 appendix 补充 per-problem 分布图（已生成 fig4_per_problem_dist.pdf）。\n- **实验支撑**: bf16 permutation test (D032) + Cohen's d per-problem paired (rebootstrap B=10000) 已完成\n",
      "numLines": 60,
      "startLine": 0,
      "totalLines": 85
    }
  },
  "sourceToolAssistantUUID": "261cce3b-332e-480b-b260-cf51c2e6bad6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "589e47f3-a107-4a46-857a-74855f584341",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：C5 pilot 边缘或失败（LLaMA 方向对但 gate 未达标），n=500 Qwen s015 仍跨零但正向趋势明显，需调整 claims 强度 核心假设：['C5 LLaMA-8B 显示正向 phase gradient 但回收 <30%（或 crossover 方向对但不显著）', 'C2 n…",
  "leafUuid": "60917afe-4e07-40d7-82fc-1a800eb415c5",
  "sessionId": "589e47f3-a107-4a46-857a-74855f584341"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Median sparsity phase-strategy interaction empirical validation",
  "sessionId": "589e47f3-a107-4a46-857a-74855f584341"
}
```

---

### Assistant

_source line 24 · 2026-05-14T14:53:26.964Z_

I have all the context needed. Let me now generate the comprehensive median-tier predictions for all non-done experiments.

```yaml
tier: median
narrative_guidance: >
  调整 claims 强度：C5 降级为 "preliminary evidence / suggestive pilot" 放入 §5 Discussion
  而非 §4 Results 主体，或作为 Appendix 补充证据。C2 叙事改为 threshold framing：
  "compound effect emerges above threshold sparsity (~s020)"，Qwen s015 作为 boundary
  condition 讨论。Title 去掉 "across architectures"，改为强调 Qwen-family 内的
  cross-model replication（distillation vs instruction tuning）。RC1 诚实承认同架构局限，
  以 mechanism 的 architecture-agnostic 性质作为间接论证。贡献收缩为：
  (1) 发现 + 同架构跨训练验证，(2) 量化 gradient（threshold-dependent），
  (3) discrimination collapse 机制。仍是 solid EMNLP empirical finding paper。

imagined_experiments:
  # ============================================================
  # plan_001: DeepSeek importance bf16 — COMPLETED (baseline anchor)
  # ============================================================
  - name: "DeepSeek importance bf16 × 4 sparsity"
    plan_id: plan_001
    description: "bf16 重跑 DeepSeek importance masking (s015/s020/s025/s030)，消除 fp16 NaN 偏差"
    expected_results:
      s015_median_diff: 0.3236
      s015_cohens_d: 0.6068
      s015_ci: [0.199, 0.472]
      s020_median_diff: 1.152
      s020_cohens_d: 0.725
      s020_ci: [0.655, 1.256]
      s025_median_diff: 3.969
      s025_cohens_d: 0.9534
      s025_ci: [2.829, 5.292]
      s030_median_diff: 9.944
      s030_cohens_d: 1.1263
      s030_ci: [8.392, 16.653]
      monotonic_gradient: true
      all_bonferroni_p: "<0.005"
      n_paired: 49
    result_rationale: >
      已完成实验，数据为 median tier 的锚点。bf16 消除 NaN 偏差后 paired median
      difference 呈清晰单调递增 (0.32→1.15→3.97→9.94)，Cohen's d 从 medium (0.61)
      到 large (1.13)。这些数据在所有 tier 下均不变——它们是已观测事实，不是预测。
    tables:
      - "Table 1 (DeepSeek importance 列): paired median diff + Cohen's d + CI"
    figures_description:
      - "Fig 2a: Phase gradient heatmap — II median across 3 phases × 4 sparsity"
    analysis: >
      核心证据锚点。4 水平 Bonferroni p<0.005，effect size medium→large。
      median tier 下游实验的所有预测以此为参照基线。

  # ============================================================
  # plan_002: DeepSeek random bf16 — COMPLETED (contrast anchor)
  # ============================================================
  - name: "DeepSeek random bf16 × 4 sparsity"
    plan_id: plan_002
    description: "bf16 重跑 DeepSeek random masking (s015/s020/s025/s030) 配对对照"
    expected_results:
      s015_median_diff: 0.0095
      s015_verdict: FAIL
      s020_median_diff: -0.0155
      s020_verdict: FAIL
      s025_median_diff: 0.5445
      s025_verdict: FAIL
      s030_median_diff: 1.5383
      s030_verdict: FAIL
      phase_gradient_present: false
      all_4_fail: "7/8 conditions FAIL (counting Qwen random)"
    result_rationale: >
      已完成实验。Random masking 4 水平 permutation test 全部 FAIL，paired median
      difference 近零或无系统方向。与 importance 的强单调梯度形成鲜明对比，
      直接支撑 C1 strategy-dependent claim。s030 median_diff=1.54 虽非零但
      无 phase gradient（high/mid/low II 无系统差异），不具 phase-modulation 特征。
    tables:
      - "Table 1 (DeepSeek random 列): FAIL 标注"
    figures_description:
      - "Fig 2b: Random masking flat II profile 对比 importance gradient"
    analysis: >
      Random flatness 是论文最关键的对照证据。Phase gradient 的特异性
      (importance-only) 排除了 "任何 compound interaction 都有 phase gradient" 的
      trivial 解释。

  # ============================================================
  # plan_003: Crossover analysis — DERIVABLE from plan_001+002
  # ============================================================
  - name: "Crossover analysis from plan_001 + plan_002"
    plan_id: plan_003
    description: "从 bf16 importance vs random 数据中提取 per-phase II，验证方向反转"
    expected_results:
      s025_importance_high_phase_median: 0.032
      s025_random_high_phase_median: 0.818
      s025_importance_low_phase_median: 7.196
      s025_random_low_phase_median: 1.363
      crossover_present: true
      crossover_significant: true
      direction: "importance < random (high phase) → importance > random (low phase)"
    result_rationale: >
      从已完成数据直接派生。在 s025，importance masking 在 high-sparsity phase 的
      II (0.032) 远低于 random (0.818)——importance 在早期 reasoning 反而比 random 好；
      但在 low-sparsity phase，importance II (7.196) 远超 random (1.363)——importance
      在晚期 reasoning 比 random 差得多。方向反转是 C3 crossover 的核心证据。
      这个 crossover 在所有 tier 下均成立——它是已确认的 DeepSeek 结果。
    tables:
      - "Table 2: Per-phase II — importance vs random at s025"
    figures_description:
      - "Fig 3: Crossover interaction plot — X轴 phase, Y轴 II, 两线交叉"
    analysis: >
      Crossover 是本文最独特的发现。Prior work 从未报告 compound interaction
      方向随 reasoning phase 反转。这直接否定了 compound degradation
      均匀分布的隐含假设。

  # ============================================================
  # plan_004: Qwen importance bf16 — COMPLETED
  # ============================================================
  - name: "Qwen importance bf16 × 4 sparsity"
    plan_id: plan_004
    description: "Qwen2.5-7B-Instruct importance masking bf16 (s015/s020/s025/s030)"
    expected_results:
      s015_median_diff: 0.0476
      s015_cohens_d: 0.3705
      s015_ci: [-0.005, 0.110]
      s015_ci_crosses_zero: true
      s020_median_diff: 0.2075
      s020_cohens_d: 0.7224
      s020_ci: [0.067, 0.402]
      s025_median_diff: 1.1087
      s025_cohens_d: 1.2329
      s025_ci: [0.609, 1.469]
      s030_median_diff: 2.6194
      s030_cohens_d: 1.4394
      s030_ci: [1.722, 3.651]
      onset_threshold: "s020"
      magnitude_ratio_vs_deepseek: "~1/4"
      n_paired: 46
    result_rationale: >
      已完成实验。Qwen 复现 DeepSeek 的单调模式 (0.048→0.208→1.109→2.619)
      但绝对量级约 1/4。关键：s015 CI 跨零 [-0.005, 0.110]——这个边界性
      是 median tier 叙事的核心驱动因素。Qwen 使用 instruction tuning
      (vs DeepSeek 的 R1 distillation)，attention pattern 更均匀，导致
      低 sparsity 下 head importance 差异更小，compound interaction 接近 noise floor。
    tables:
      - "Table 1 (Qwen importance 列)"
    figures_description:
      - "Fig 2c: Qwen phase gradient — magnitude ~1/4 of DeepSeek"
    analysis: >
      Qwen s015 的边缘性是 median tier 中 threshold framing 的实证基础。
      Cross-model replication 确认方向一致但量级不同——训练方式影响
      compound interaction 的 sensitivity。

  # ============================================================
  # plan_005: Qwen random bf16 — COMPLETED
  # ============================================================
  - name: "Qwen random bf16 × 4 sparsity"
    plan_id: plan_005
    description: "Qwen2.5-7B-Instruct random masking bf16 (s015/s020/s025/s030)"
    expected_results:
      s015_verdict: FAIL
      s015_cohens_d: -0.0507
      s015_perm_p: 0.766
      s020_verdict: FAIL
      s020_cohens_d: 0.247
      s020_perm_p: 0.352
      s025_verdict: FAIL
      s025_cohens_d: 0.1574
      s025_perm_p: 0.168
      s030_verdict: "PASS (p=0.012, d=-0.035 negligible)"
      s030_perm_p: 0.012
      s030_cohens_d: -0.035
      cross_model_random_pattern: "7/8 FAIL (DeepSeek 4/4 + Qwen 3/4)"
    result_rationale: >
      已完成实验。Qwen random 3/4 FAIL，与 DeepSeek random 4/4 FAIL 合计
      形成 7/8 FAIL 模式。唯一例外 Qwen s030 perm_p=0.012 但 Cohen's d=-0.035
      效应量可忽略。这个 exception 需论文中明确标注：统计显著但实际无意义。
      Random 的 phase-independent flatness 在两个模型上均稳健复现。
    tables:
      - "Table 1 (Qwen random 列): 3 FAIL + 1 PASS(negligible d)"
    figures_description: []
    analysis: >
      s030 PASS 的处理策略：在表中用脚注标注 "p=0.012 but |d|<0.05, negligible
      effect size"。审稿人可能问 "为什么 s030 PASS"——回应：sample size effect，
      大样本任何微小差异都可能 significant，效应量才是实质指标。

  # ============================================================
  # plan_006: Entropy/discrimination mechanism — COMPLETED
  # ============================================================
  - name: "Attention entropy + discrimination collapse measurement"
    plan_id: plan_006
    description: "测量 pruned vs unpruned 的 attention entropy + importance score Gini/CV"
    expected_results:
      ds_entropy_delta: {s015: -0.040, s020: -0.047, s025: -0.045, s030: -0.044}
      ds_gini_delta: {s015: -0.030, s020: -0.040, s025: -0.065, s030: -0.081}
      ds_cv_delta: {s015: -0.564, s020: -0.774, s025: -1.287, s030: -1.665}
      qw_entropy_delta: {s015: -0.073, s020: -0.076, s025: +0.045, s030: -0.007}
      qw_gini_delta: {s015: -0.010, s020: -0.012, s025: -0.010, s030: -0.020}
      qw_cv_delta: {s015: -0.045, s020: -0.208, s025: -1.491, s030: -1.142}
      cross_model_gini_cv_consistent: true
      cross_model_entropy_consistent: false
      problems_completed: 30
    result_rationale: >
      已完成实验。Discrimination collapse (Gini/CV 下降) 跨模型方向一致——
      head pruning 后 importance score 判别力系统性降低，两个模型均观察到。
      但 entropy redistribution 在 Qwen s025 反转 (+0.045)，说明 entropy
      collapse 是 DeepSeek 特有的（可能与 R1 distillation 的 attention 集中度
      有关），不是 universal mechanism。Median tier 预测 LLaMA 验证时
      Gini/CV 方向一致——这是 "在可用架构上方向一致" 假设的延伸。
    tables:
      - "Table 3: Discrimination collapse (Gini/CV) 跨模型对比"
    figures_description:
      - "Fig 4: Gini delta heatmap (DeepSeek vs Qwen × 4 sparsity)"
    analysis: >
      论文以 discrimination collapse 为 primary mechanism，entropy 降级为
      DeepSeek-specific amplifier。这避免了 Qwen entropy 反转的尴尬——
      转为 "model-dependent secondary effect" 的诚实表述。

  # ============================================================
  # plan_007: Growth rate analysis — DERIVABLE
  # ============================================================
  - name: "Growth rate analysis from plan_001"
    plan_id: plan_007
    description: "从 bf16 importance 数据分析增长率模式，验证 C6 sub-exponential"
    expected_results:
      ds_median_diff_series: [0.3236, 1.152, 3.969, 9.944]
      ds_growth_factors: [3.56, 3.44, 2.51]
      ds_growth_decreasing: true
      qw_median_diff_series: [0.0476, 0.2075, 1.1087, 2.6194]
      qw_growth_factors: [4.36, 5.34, 2.36]
      qw_growth_s025_to_s030_decreasing: true
      both_sub_exponential: true
    result_rationale: >
      从已有数据派生。DeepSeek 增长因子 3.56→3.44→2.51 单调递减。
      Qwen 增长因子 4.36→5.34→2.36 在 s020→s025 微升但 s025→s030 大幅下降。
      两模型在高 sparsity 端增速均放缓。物理解释：低 sparsity 段 eviction 优先
      移除低重要度 token，compound interaction 随每个被移除 token 的边际重要性
      递增而快速增长；但高 sparsity 段多数"安全"token 已被移除，剩余 token
      重要性趋同（discrimination collapse），边际增长减速。
    tables: []
    figures_description:
      - "Fig 2d inset: Growth factor deceleration curve"
    analysis: >
      Sub-exponential 是 positive framing 的重要论据：compound severity 可控，
      高 sparsity 下增速自然放缓而非指数爆炸，对实际部署是利好信号。

  # ============================================================
  # plan_008: Bootstrap CI — COMPLETED
  # ============================================================
  - name: "Per-problem bootstrap CI (bf16 data)"
    plan_id: plan_008
    description: "B=10000 paired bootstrap CI + permutation test (Bonferroni)"
    expected_results:
      ds_all_4_significant: true
      ds_bonferroni_p: "<0.005 全 4 水平"
      qw_s020_s025_s030_significant: true
      qw_s015_borderline: true
      qw_s015_bonferroni_p: "~0.0004 (permutation) 但 CI 跨零"
      bootstrap_B: 10000
      n_paired_ds: 49
      n_paired_qw: 46
    result_rationale: >
      已完成。统计框架使用 paired median difference 作为 robust statistic，
      permutation test B=10000 + Bonferroni 多重校正。DeepSeek 全部显著，
      Qwen s015 permutation_p=0.0001（显著）但 bootstrap CI 跨零——
      这种 permutation 显著但 CI 跨零的 discrepancy 来自 permutation test
      对任何系统性差异敏感，而 bootstrap CI 反映 median 估计的不确定性。
      n=500 扩展主要解决这个 discrepancy。
    tables:
      - "Table 1 CI 列 + significance markers"
    figures_description:
      - "Fig A1: Per-problem paired difference distribution (violin plots)"
    analysis: >
      RC4 的回应材料已充足。permutation + bootstrap + Cohen's d 三层验证
      确保统计稳健性。唯一的 grey area 是 Qwen s015，
      这正是 n=500 实验 (plan_010) 要解决的问题。

  # ============================================================
  # plan_009: DeepSeek n=500 — RUNNING (genuine prediction)
  # ============================================================
  - name: "DeepSeek n=500 statistical power boost"
    plan_id: plan_009
    description: "DeepSeek 8 conditions (imp/rand × 4 sparsity) n=50→n=500 (full MATH-500)"
    expected_results:
      # Importance conditions — CI narrowing, point estimates stable
      imp_s015_median_diff: 0.30
      imp_s015_cohens_d: 0.58
      imp_s015_ci: [0.22, 0.40]
      imp_s015_ci_width: 0.18
      imp_s015_ci_width_reduction_pct: 34
      imp_s020_median_diff: 1.10
      imp_s020_cohens_d: 0.70
      imp_s020_ci: [0.85, 1.25]
      imp_s020_ci_width_reduction_pct: 33
      imp_s025_median_diff: 3.85
      imp_s025_cohens_d: 0.92
      imp_s025_ci: [3.10, 4.80]
      imp_s025_ci_width_reduction_pct: 31
      imp_s030_median_diff: 9.70
      imp_s030_cohens_d: 1.10
      imp_s030_ci: [8.40, 14.10]
      imp_s030_ci_width_reduction_pct: 31
      # Random conditions — still FAIL
      rand_s015_verdict: FAIL
      rand_s020_verdict: FAIL
      rand_s025_verdict: FAIL
      rand_s030_verdict: FAIL
      # Overall
      all_bonferroni_significant: true
      monotonic_gradient_preserved: true
      n_problems: 500
      n_effective_paired: ~470
    result_rationale: >
      Median tier 预测 DeepSeek n=500 CI 收窄约 25-35%（远低于理论 √10≈68%）。
      原因：MATH-500 包含大量简单题目，这些题目的 reasoning trace 极短
      （phase assignment 仅 1-2 segments per phase），compound interaction
      接近 noise floor，对 paired median difference 贡献有限。有效配对数
      从 49 增至约 470（~30 题因 phase coverage 不足被排除），但 per-problem II
      分布的高偏斜度（skewness 4-16）使 median 的 bootstrap CI 不如 mean 收窄快。
      点估计微调（s015 从 0.324 降至 0.30）：简单题目的 near-zero II 拉低了
      overall median，但变化 <10%，说明 n=50 采样已是合理估计。
      Random 对照在 10× 样本下仍全部 FAIL，进一步排除 sampling bias。
    tables:
      - "Table 1 更新: n=500 CI (DeepSeek)"
      - "Table A1: CI width reduction summary by sparsity"
    figures_description:
      - "Fig A1: n=50 vs n=500 forest plot — CI narrowing 可视化"
      - "Fig A2: Per-problem II distribution (500 problems) violin — 展示 easy-problem floor effect"
    analysis: >
      DeepSeek n=500 在 median tier 下无 surprise。主要价值：
      (1) 用 full MATH-500 消除 reviewer 的 sampling bias 疑虑；
      (2) 更精确的 effect size 估计可用于 future meta-analysis；
      (3) Random 10× replication 彻底巩固 strategy-dependent contrast。

  # ============================================================
  # plan_010: Qwen n=500 — RUNNING (genuine prediction, CRITICAL)
  # ============================================================
  - name: "Qwen n=500 statistical power boost"
    plan_id: plan_010
    description: "Qwen 8 conditions (imp/rand × 4 sparsity) n=50→n=500"
    expected_results:
      # Importance conditions — s015 is the critical test
      imp_s015_median_diff: 0.045
      imp_s015_cohens_d: 0.35
      imp_s015_ci: [-0.005, 0.095]
      imp_s015_ci_crosses_zero: true
      imp_s015_point_estimate_positive: true
      imp_s015_wilcoxon_p: 0.038
      imp_s015_bonferroni_p: 0.152
      imp_s015_bonferroni_significant: false
      imp_s020_median_diff: 0.19
      imp_s020_cohens_d: 0.68
      imp_s020_ci: [0.10, 0.32]
      imp_s020_ci_crosses_zero: false
      imp_s020_bonferroni_p: "<0.001"
      imp_s025_median_diff: 1.05
      imp_s025_cohens_d: 1.18
      imp_s025_ci: [0.72, 1.35]
      imp_s025_bonferroni_p: "<0.001"
      imp_s030_median_diff: 2.55
      imp_s030_cohens_d: 1.38
      imp_s030_ci: [1.85, 3.30]
      imp_s030_bonferroni_p: "<0.001"
      # Random conditions
      rand_s015_verdict: FAIL
      rand_s020_verdict: FAIL
      rand_s025_verdict: FAIL
      rand_s030_verdict: "PASS (p~0.008, d~-0.03 negligible)"
      # Threshold analysis
      onset_threshold: "s020"
      threshold_framing: "compound effect emerges above s~0.020"
      n_problems: 500
      n_effective_paired: ~440
    result_rationale: >
      这是 median tier 的定义性预测。Qwen s015 在 n=500 后 CI 仍跨零的原因：

      (1) 效应量太小（d≈0.35）。对 paired design + Bonferroni α=0.0125，
      检测 d=0.35 需要 n≈120 paired observations 达到 power=0.80。虽然 n=500
      远超此数，但 MATH-500 中约 40% 的题目在 s015 下 compound interaction
      接近零（非常简单的算术题），实际有效 n 约 280-300；

      (2) Per-problem paired difference 在 s015 的分布呈双峰：多数题目
      差异 ≈0（简单题），少数题目差异 >0.2（需要深度 reasoning 的题），
      bootstrap median 在两个模式之间振荡；

      (3) Instruction tuning (Qwen) vs distillation (DeepSeek) 的关键差异：
      instruction tuning 产生更均匀的 attention distribution，head importance
      差异天然更小，s015 这个低 sparsity 下 compound interaction 确实
      接近 noise floor——这不是 power 不足，而是 true effect 接近零。

      s020 在 n=500 后清晰脱离零 (CI [0.10, 0.32])，与 s015 形成清晰的
      threshold boundary。这支持 "compound effect emerges above s~0.020" 的
      threshold framing，为叙事调整提供直接证据。

      Qwen s030 random 仍然 PASS (p~0.008) 但 d~-0.03——与 n=50 一致，
      更大样本确认这是 persistent but negligible 的统计 artifact。
    tables:
      - "Table 1 更新: Qwen n=500 CI + significance"
      - "Table 4: Threshold analysis — s015 boundary condition"
    figures_description:
      - "Fig 5: Qwen s015 per-problem paired difference distribution (n=500)"
      - "Fig 5 inset: s015 双峰分布 — 简单题 near-zero cluster vs 难题 positive cluster"
    analysis: >
      Qwen s015 的"不显著"是 informative null——它定义了 compound effect 的
      onset boundary。叙事从 "universally phase-modulated" 转为
      "phase-modulated above threshold sparsity (~s020)"。这实际上增强论文的
      精确度：与其 claim 所有 sparsity 都有效，不如给出清晰的 operating regime。
      RC1 应对：Qwen s015 boundary condition + DeepSeek s015 significant =
      onset threshold is model-dependent (与已确认的 S3→C 一致)。

  # ============================================================
  # plan_011: Phase-aware mitigation pilot — PLANNED (genuine prediction)
  # ============================================================
  - name: "Phase-aware mitigation pilot (oracle + heuristic)"
    plan_id: plan_011
    description: "2h pilot: oracle phase assignment + token position ratio heuristic, compute-matched"
    expected_results:
      # Oracle upper bound (perfect phase knowledge)
      oracle_s025_recovery_pct: 22
      oracle_s025_compound_ppl: 49.6
      oracle_s025_baseline_compound_ppl: 63.7
      oracle_s025_dense_ppl: 1.23
      oracle_s030_recovery_pct: 18
      oracle_s030_compound_ppl: 100.5
      oracle_s030_baseline_compound_ppl: 122.6
      # Heuristic lower bound (token position ratio proxy)
      heuristic_phase_accuracy: 0.67
      heuristic_s025_recovery_pct: 12
      heuristic_s025_compound_ppl: 55.3
      heuristic_s030_recovery_pct: 8
      heuristic_s030_compound_ppl: 113.0
      # Gate assessment
      gate_threshold: "30%"
      gate_passed: false
      recommendation: "降级为 future work"
    result_rationale: >
      Oracle recovery 仅 18-22% (<30% gate) 的根本原因：
      phase-aware eviction 只调整"什么时候 evict"，不改变"如何 evict"——
      discrimination collapse 发生在 importance scoring 层面，即使在正确的 phase
      减少 eviction rate，剩余的 eviction 仍然是低判别力的伪随机决策。
      具体机制：oracle 在 low-sparsity phase (compound interaction 最大处)
      降低 eviction rate，但 compute-matched constraint 要求在 high-sparsity phase
      相应增加 eviction rate，后者虽然 compound interaction 小但不是零——
      净收益被部分抵消。

      Heuristic (token position ratio) 作为 phase proxy 准确率约 67%——
      reasoning 的 phase 不完全与 token position 对应（回溯、correction、
      multi-step verification 打破了线性位置假设），导致 phase 分类噪声。
      Heuristic recovery (8-12%) 是 oracle (18-22%) 的约 50-55%，反映
      proxy accuracy 的传递损失。

      Gate 未通过 (max 22% < 30%) 意味着 mitigation 不进入论文 §4 Results，
      但 pilot 数据有论文价值：它量化了 phase-aware 方法的理论上限，
      表明单独调整 eviction timing 不足以解决 compound interaction——
      需要更根本的 scoring mechanism 改进。这实际上强化了 discrimination
      collapse 作为 root cause 的叙事。
    tables:
      - "Table A3 (Appendix): Mitigation pilot — oracle vs heuristic"
    figures_description:
      - "Fig A3: Recovery curve — oracle upper bound vs heuristic lower bound"
    analysis: >
      Pilot failure 在叙事上可转化为 positive insight：
      "Even oracle phase knowledge recovers only ~20% of compound degradation,
      confirming that the root cause is discrimination collapse in importance
      scoring, not suboptimal eviction timing." 这为 future work 明确了方向：
      fix the scoring, not the timing。

  # ============================================================
  # plan_012: LLaMA-8B cross-architecture — PREPARING (genuine prediction)
  # ============================================================
  - name: "LLaMA-8B cross-architecture validation"
    plan_id: plan_012
    description: "DeepSeek-R1-Distill-Llama-8B s025/s030 phase gradient + crossover"
    expected_results:
      # Phase gradient — present but weak
      s025_paired_median_diff: 0.55
      s025_cohens_d: 0.30
      s025_ci: [0.05, 1.20]
      s025_ci_crosses_zero: false
      s025_bonferroni_p: 0.028
      s030_paired_median_diff: 1.40
      s030_cohens_d: 0.42
      s030_ci: [0.18, 3.10]
      s030_ci_crosses_zero: false
      s030_bonferroni_p: 0.006
      # Crossover assessment
      crossover_direction_correct: true
      crossover_significant: false
      crossover_verdict: "ambiguous"
      s025_imp_high_phase: 0.08
      s025_rand_high_phase: 0.35
      s025_imp_low_phase: 0.95
      s025_rand_low_phase: 0.70
      crossover_gap: "importance low (0.95) > random low (0.70) 但 CI 重叠"
      # Discrimination collapse
      gini_delta_s025: -0.015
      gini_delta_s030: -0.022
      cv_delta_s025: -0.40
      cv_delta_s030: -0.65
      gini_cv_direction_consistent: true
      # Magnitude comparison
      magnitude_vs_deepseek: "~1/7"
      magnitude_vs_qwen: "~1/2"
      n_problems: 50
      n_paired: ~45
      # C5 verdict
      c5_verdict: "suggestive — positive gradient, small-medium effect size"
      paper_placement: "§5 Discussion or Appendix B"
      confirmed_arch_families: 1
    result_rationale: >
      LLaMA 效应量偏小的三个原因：

      (1) GQA 架构差异。LLaMA-8B 使用 Grouped Query Attention（8 KV heads shared
      across 32 Q heads），Qwen 使用类似但参数化不同的 GQA。GQA 中 pruning 一个
      KV head 影响 4 个 Q heads 的所有 attention，compound interaction 的
      phase-dependence 被 head sharing 部分平滑——每个被 prune 的 head 的影响
      分散到更多 query 位置，dilute 了 phase-specific signal；

      (2) Distillation source 差异。DeepSeek-R1-Distill-Llama-8B 虽然用
      DeepSeek-R1 蒸馏，但 target architecture 是 LLaMA，蒸馏过程中
      attention pattern 被 LLaMA 的 architectural prior 约束，不如
      DeepSeek-R1-Distill-Qwen-7B 那样忠实还原 R1 的 attention 模式；

      (3) n=50 power 不足。对 d=0.30-0.42 (small-medium)，n=50 paired 在
      α=0.025 (Bonferroni for 2 comparisons) 下 power 仅 0.35-0.55，
      导致 CI 宽且 barely significant。

      Crossover 方向正确但不显著：importance low-phase II (0.95) > random (0.70)
      是预期方向，但差异仅 0.25，而 bootstrap CI 宽度约 ±0.40，重叠严重。
      标记为 "ambiguous" 而非 "confirmed" 或 "absent"。

      Gini/CV 方向一致 (negative delta) 但 magnitude 更小——支持 mechanism
      的 architecture-agnostic 性质（方向一致）但不构成强证据。

      综合评估：LLaMA 结果 directionally consistent 但 underpowered。
      不足以支撑 "across architectures" claim，但也不 contradictory。
      适合放入 Discussion 作为 "suggestive evidence" 并诚实讨论 limitation。
    tables:
      - "Table A2 (Appendix): LLaMA-8B pilot results"
    figures_description:
      - "Fig A4: LLaMA phase gradient — 与 Qwen-family 量级对比"
      - "Fig A5: LLaMA crossover plot — 标注 ambiguous 区域"
    analysis: >
      Median tier 下 LLaMA 结果的论文处理：
      (1) Title 去掉 "across architectures"，改为 "Phase-Gated Compound Sparsity
      in Qwen-family Models" 或类似；
      (2) §5 Discussion 加段："Preliminary evidence from LLaMA-8B shows directionally
      consistent phase gradient (d=0.30-0.42) but insufficient power to confirm
      architectural generalization. We leave full cross-architecture validation
      to future work."
      (3) Limitations 明确声明 confirmed_arch_families=1 (Qwen2ForCausalLM)。

  # ============================================================
  # plan_013: Related Work differentiation — PLANNED (writing task)
  # ============================================================
  - name: "Related Work differentiation: Lethe + SparK"
    plan_id: plan_013
    description: "§2 Related Work 加引用区分 Lethe/SparK/ThinKV/UniComp"
    expected_results:
      lethe_gap: "layer-time-adaptive KV pruning, single-axis (layer × time); no compound interaction analysis"
      spark_gap: "joint compression but assumes uniform compound interaction; our finding directly contradicts this assumption"
      thinkv_gap: "phase-aware single-axis KV eviction; no compound × phase × strategy three-way interaction"
      unicomp_gap: "unified compression framework without phase decomposition"
      new_paragraphs: 2
      new_citations: 4
      positioning: "our unique contribution is the compound × phase × strategy three-way interaction — a dimension no prior work examines"
    result_rationale: >
      写作任务，无实验数据。在 median tier 下 Related Work 的 positioning 需要
      格外精确，因为贡献已收缩：不 claim 跨架构泛化，只 claim 同架构跨训练
      验证 + threshold-dependent gradient + mechanism。Positioning 核心是
      "我们发现了一个新维度"而非"我们做了更多实验"。

      Lethe 最需要区分：它的 layer-time-adaptive 与我们的 phase-gated 在
      名称上易混淆，但本质不同——Lethe 动态调整 per-layer eviction rate
      based on cumulative information loss，不涉及 compound interaction
      (head pruning + KV eviction 的交互)。我们的 phase decomposition
      分析的是 compound interaction 如何随 reasoning phase 变化。

      SparK 是最直接的 contrast：它假设 compound interaction 是均匀的
      (uniform across inference)，我们的核心发现正是否定这个假设——
      compound interaction 是 phase-dependent 且 strategy-specific 的。
    tables: []
    figures_description: []
    analysis: >
      Related Work 在 median tier 下的写作策略：
      强调 "three-way interaction (compound × phase × strategy)" 是
      literature gap，避免过度 claim 泛化性。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60917afe-4e07-40d7-82fc-1a800eb415c5",
  "isSidechain": false,
  "requestId": "req_011Cb2eW18o3t1MSTZuduuUy",
  "type": "assistant",
  "uuid": "53419f84-e0ee-40f4-98c7-b96617d97780",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11",
  "sessionId": "589e47f3-a107-4a46-857a-74855f584341",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ELRas7qfoJzbU9VgsKoRmm",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23344,
      "cache_read_input_tokens": 49062,
      "output_tokens": 10330,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23344,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10330,
          "cache_read_input_tokens": 49062,
          "cache_creation_input_tokens": 23344,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23344
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：C5 pilot 边缘或失败（LLaMA 方向对但 gate 未达标），n=500 Qwen s015 仍跨零但正向趋势明显，需调整 claims 强度 核心假设：['C5 LLaMA-8B 显示正向 phase gradient 但回收 <30%（或 crossover 方向对但不显著）', 'C2 n…",
  "leafUuid": "53419f84-e0ee-40f4-98c7-b96617d97780",
  "sessionId": "589e47f3-a107-4a46-857a-74855f584341"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Median sparsity phase-strategy interaction empirical validation",
  "sessionId": "589e47f3-a107-4a46-857a-74855f584341"
}
```

---
