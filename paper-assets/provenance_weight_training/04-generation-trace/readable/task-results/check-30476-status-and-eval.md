# check 30476 status and eval

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_30476_status_and_eval_20260518T015821_result.json`
- **Structured JSON:** [`c2ce3197327b709c4def.json`](../../sessions/c2/c2ce3197327b709c4def.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

| 实验 | GPU | 进度 | ETA |
|------|-----|------|-----|
| **grid_b0_2_seed456** | cuda:0 (99%, 41.7G) | 297/6103 (5%) | ~3h23m |
| **grid_b0_2_seed123** | cuda:1 (95%, 41.7G) | 286/6103 (5%) | ~3h23m |
| **contamination_60_seed123** | cuda:2 (99%, 41.7G) | 4645/6103 (76%) | ~55m |
| **contamination_60_uniform_seed123** | cuda:3 (99%, 41.7G) | 3632/6103 (59%) | ~1h26m |

**全部 4 个实验仍在运行中**，没有 final checkpoint，无法执行 eval。

- 两个 grid 实验刚启动约 12 分钟，预计还需 ~3.5 小时
- contamination_60_seed123 进度最快，预计 ~55 分钟完成
- contamination_60_uniform_seed123 预计 ~1.5 小时完成

---
