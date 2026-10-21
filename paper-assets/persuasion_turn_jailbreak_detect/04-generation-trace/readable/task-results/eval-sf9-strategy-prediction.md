# eval sf9 strategy prediction

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_sf9-strategy-prediction_20260518T091216_result.json`
- **Structured JSON:** [`1ddd1edd3e96f0af6929.json`](../../sessions/1d/1ddd1edd3e96f0af6929.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

SF9 评估完成。

**结果摘要：**

| 指标 | 值 |
|---|---|
| Overall Accuracy | **30.7%** |
| Cohen's Kappa | **0.126** |
| 总对话数 | 80 |
| 总 user turns | 645 |

**Per-class (有 GT 样本的类)：**

| Strategy | P | R | F1 | Support |
|---|---|---|---|---|
| rapport_building | 0.408 | 0.881 | 0.557 | 160 |
| logical_reframing | 0.321 | 0.121 | 0.176 | 140 |
| gradual_escalation | 0.233 | 0.310 | 0.266 | 129 |
| obfuscation | 0.000 | 0.000 | 0.000 | 160 |
| role_assignment | 0.000 | 0.000 | 0.000 | 36 |
| emotional_manipulation | 0.000 | 0.000 | 0.000 | 20 |

**关键发现：**
- 模型严重偏向预测 rapport_building（346/645 次预测为该类）
- obfuscation 有 160 个 GT 样本但 recall=0，全部被误分为 rapport_building(86) 和 gradual_escalation(41)
- 转移矩阵差异最大的地方：GT 中 rapport→obfuscation 概率 50%，但预测中该路径几乎消失（-49.7%）；logical_reframing→gradual_escalation GT 为 100% 但预测中降至 45.7%

结果 JSON 保存在 `/root/persuasion_turn_jailbreak_detect/results/sf9_strategy_prediction.json`，artifact 已注册为 `sf9_strategy_prediction`。

---
