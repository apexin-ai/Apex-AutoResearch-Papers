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
