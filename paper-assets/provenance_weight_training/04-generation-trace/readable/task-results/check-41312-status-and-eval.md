# check 41312 status and eval

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_41312_status_and_eval_20260518T015812_result.json`
- **Structured JSON:** [`18a717579851e197f23c.json`](../../sessions/18/18a717579851e197f23c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

**GPU 状态 (westd-41312)：** 4x RTX PRO 6000 Blackwell (98GB)，全部 100% 占用。

| 实验 | GPU | 进度 | ETA | 状态 |
|------|-----|------|-----|------|
| contamination_60_adaptive_seed456 | 0 | 370/6103 (6%) | ~3h31m | **running** |
| contamination_60_uniform_seed456 | 1 | 393/6103 (6%) | ~3h20m | **running** |
| grid_b0_1_seed123 | 2 | 390/6103 (6%) | ~3h20m | **running** |
| grid_b0_1_seed456 | 3 | 388/6103 (6%) | ~3h20m | **running** |

4 个实验均在运行中，刚跑了约 14 分钟，预计还需 ~3.5 小时完成。无 final checkpoint，暂无法 eval。

---
