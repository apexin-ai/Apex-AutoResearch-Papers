# diagnose eval best s0 l005 exit

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_best_s0_l005_exit_20260527T234016_result.json`
- **Structured JSON:** [`2b6984fb2b69a56dad61.json`](../../sessions/2b/2b6984fb2b69a56dad61.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**eval_pi05_a1_best_s0_l005 正常完成**，无错误。使用 30000 checkpoint（seed0_l005 唯一 checkpoint）。

### 结果

| Task | Name | TSR | CAR |
|------|------|-----|-----|
| 0 | pick up orange juice → basket | 28.0% | 50.0% |
| 1 | (object task) | 70.0% | 74.0% |
| 2 | pick up milk → basket | 52.0% | 68.0% |
| 3 | pick up bbq sauce → basket | 58.0% | 26.0% |
| **Avg** | | **52.0%** | **54.5%** |

Task 3 的 CAR 极低（26%），拖累整体 CAR。Task 0 的 TSR 也很差（28%）。Registry 已更新为 DONE/success。

---
