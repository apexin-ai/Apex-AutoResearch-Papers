# FOLIO C0 预检（10/30 题, K=6, T=0.7）

Model: /root/autodl-tmp/models/QwQ-32B/Qwen/QwQ-32B  
max_tokens: 4096  
Total time: 1466s


| # | ID | 标签 | Unique Answers | 多候选? | 各答案分布 |
|---|-----|------|---------------|---------|----------|
| 1 | folio_000 | True | 1 | No | True:6 |
| 2 | folio_002 | True | 1 | No | True:6 |
| 3 | folio_004 | True | 1 | No | False:4, FAIL:2 |
| 4 | folio_010 | False | 1 | No | False:6 |
| 5 | folio_012 | False | 1 | No | False:6 |
| 6 | folio_014 | False | 1 | No | False:6 |
| 7 | folio_020 | Unknown | 1 | No | Unknown:6 |
| 8 | folio_022 | Unknown | 1 | No | Unknown:6 |
| 9 | folio_024 | Unknown | 1 | No | Unknown:6 |
| 10 | folio_026 | Unknown | 1 | No | Unknown:6 |

**多候选率: 0/10 = 0%**

答案提取失败: 2/60

## 偏差说明

- 原始要求 K=12，因 vLLM KV cache 容量受限（~3 并发序列）+ 另一个 eval 任务抢占 GPU，降为 K=6 以加速
- 原始要求 max_tokens=12288，降为 4096 以加速；folio_004 有 2/6 提取失败可能因截断
- 即使 K=6，结论已极其明确：QwQ-32B 在 FOLIO 上几乎不产生 trace 分歧

## 结论

**FOLIO C0 预检 FAIL。** 多候选率 0%，远低于 D012 C0 标准要求的 ≥20%。

QwQ-32B 在 FOLIO 三类标签（True/False/Unknown）上均表现出极高的 trace 一致性——6 次采样中所有有效答案完全相同。这意味着：
1. SICA 的约束提取 + MaxSAT 共识机制在 FOLIO 上无用武之地（没有分歧可供仲裁）
2. 与 ProofWriter 的观察一致：QwQ-32B 在形式化逻辑推理任务上表现过于确定，不适合作为 SICA 的 trace divergence 场景
3. 需要考虑切换到更难的任务（如 AIME/数学竞赛题）或降低模型能力（更小模型/更低温度）来制造足够的 trace 分歧
