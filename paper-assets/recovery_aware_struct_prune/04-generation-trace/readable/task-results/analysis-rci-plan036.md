# analysis rci plan036

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_rci_plan036_20260520T024750_result.json`
- **Structured JSON:** [`3711801ca768138149e9.json`](../../sessions/37/3711801ca768138149e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

plan_036 完成。结果：

## CKA Diversity Scores

| Method | Mean Diagonal CKA | Diversity (1-mean) |
|--------|:-:|:-:|
| CKA-only | 0.620 | **0.380** |
| RASP | 0.882 | 0.118 |
| Standard | 0.904 | 0.096 |
| Random | 0.923 | 0.077 |

## Spearman Rank Correlations

| Comparison | ρ | p | n |
|---|:-:|:-:|:-:|
| Diversity vs peak_reward (all 4) | **0.20** | 0.80 | 4 |
| Diversity vs peak_reward (excl random) | 0.50 | 0.67 | 3 |
| Diversity vs GSM8K accuracy (excl random) | **1.00** | 0.00 | 3 |

## 关键发现

- **ρ > 0.9 假设部分成立**：CKA diversity 完美预测 GSM8K accuracy 的 rank order（cka_only 64.22% > rasp 60.88% > standard 59.44%），但 n=3 统计效力有限
- **Random 是 outlier**：diversity 最低 (0.077) 但 peak_reward 第二高 (0.190)，打破了 diversity→peak_reward 的单调关系
- **Diversity 与 peak_reward 相关性弱** (ρ=0.2)：peak_reward 是训练时指标，受 reward hacking/oscillation 影响，不如 GSM8K 稳定
- **可写入论文的结论**：CKA diversity 可作为 optimization-based pruning methods 的 zero-cost RL recovery predictor（对 GSM8K final accuracy），但 random baseline 需要其他解释（可能保留了 CKA 未捕捉的 RL-favorable 结构特性）

Artifact 已注册：`art_20260520_7f9772`，完整 JSON 存于 westb-23072 的 results/ 目录。

---
