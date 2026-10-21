# ops check feature oracle status

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_feature_oracle_status_20260522T212157_result.json`
- **Structured JSON:** [`7d4a3fd10e3672ffef33.json`](../../sessions/7d/7d4a3fd10e3672ffef33.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已完整记录。实验 `oracle_true_gt_feature_v11` 状态 DONE/negative，metrics 和 notes 均已填充。

**结果汇总：**

| Task | CAR | Avg Displacement | Avg Refined/ep |
|------|-----|------------------|----------------|
| orange_juice | 90.0% | 0.0023m | 248.5 |
| chocolate_pudding | 47.5% | 0.0473m | 241.8 |
| milk | 82.5% | 0.0086m | 236.7 |
| bbq_sauce | 87.5% | 0.0097m | 240.0 |
| **Overall** | **76.9%** | — | **241.7** |

- TSR = 0%（全部任务）
- Fake safe rate = 96.7%（119/123 safe episodes displacement < 0.1mm）
- Feature-space oracle 每步都 refine（avg 241.7/ep vs action-space 14），gradient magnitude 极小（0.004-0.006），但 CAR 仍未超 baseline（79%）

进程已正常退出，无需进一步操作。Registry 已由之前的 agent 完整更新。

---
