# check exp028c step10 val

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp028c_step10_val_20260516T074949_result.json`
- **Structured JSON:** [`b5a3be383371c2001ef0.json`](../../sessions/b5/b5a3be383371c2001ef0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**Step 10 val success = 0%（0/16），从 step 5 的 6.25% 跌至零。**

关键数据：

| | Step 0 | Step 5 | Step 10 |
|---|---|---|---|
| **Val success** | 6.25% | 6.25% | **0%** |
| Val action_is_valid | 0.745 | 0.965 | 0.936 |
| Train success | — | 9.4% | 18.75% |
| Train pass@8 | — | 37.5% | 50% |

Train-val 严重分歧：训练集 success 翻倍增长至 18.75%，但 val 完全归零。entropy 持续下降 (0.236→0.215)，策略在收窄。val action_is_valid 仍高 (0.936) 说明动作格式没问题，但策略本身无法泛化。

训练仍在继续，预计 step 15 val 约 18:30 出。

报告已写入 `artifacts/exp028c_selfguide_recipe/intermediate/step10_val_check.md`。

---
