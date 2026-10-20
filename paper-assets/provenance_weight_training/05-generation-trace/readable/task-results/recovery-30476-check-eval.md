# recovery 30476 check eval

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_recovery_30476_check_eval_20260518T024402_result.json`
- **Structured JSON:** [`69cebef9de99f3473462.json`](../../sessions/69/69cebef9de99f3473462.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 确认完毕，registry 已有正确数据。以下是全部 8 个实验的状态汇总：

---

## westd-30476 (4x RTX PRO 6000, 3 GPU 在用)

| 实验 | GPU | 状态 | 进度 | ETA |
|------|-----|------|------|-----|
| **contamination_60_seed123** | - (已释放) | **DONE** | PPL=**17.73**, Loss=2.8754 | - |
| contamination_60_uniform_seed123 | cuda:3 | RUNNING | 5482/6103 (**90%**) | ~22 min |
| grid_b0_2_seed456 | cuda:0 | RUNNING | 2149/6103 (**35%**) | ~2h18m |
| grid_b0_2_seed123 | cuda:1 | RUNNING | 2140/6103 (**35%**) | ~2h18m |

## westd-41312 (4x RTX PRO 6000, 4 GPU 全部在用)

| 实验 | GPU | 状态 | 进度 | ETA |
|------|-----|------|------|-----|
| contamination_60_adaptive_seed456 | cuda:0 | RUNNING | 2110/6103 (**35%**) | ~2h27m |
| contamination_60_uniform_seed456 | cuda:1 | RUNNING | 2369/6103 (**39%**) | ~2h10m |
| grid_b0_1_seed123 | cuda:2 | RUNNING | 2248/6103 (**37%**) | ~2h17m |
| grid_b0_1_seed456 | cuda:3 | RUNNING | 2243/6103 (**37%**) | ~2h15m |

## 已完成操作
- contamination_60_seed123 eval 已确认：PPL=17.73, Loss=2.8754, 4,077,068 tokens（与 registry 一致）
- 7 个 RUNNING 实验的 registry 状态已全部从 PREPARING 更新为 RUNNING
- 所有实验预计 ~2-2.5h 后完成（contamination_60_uniform_seed123 最快，约 22 min）

---
