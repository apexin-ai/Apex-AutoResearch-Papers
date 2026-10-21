# ssh urgent status check home

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_urgent-status-check-home_20260513T110152_result.json`
- **Structured JSON:** [`b612b8298d251a30f34c.json`](../../sessions/b6/b612b8298d251a30f34c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## CLS v5 状态汇报

| 项目 | 值 |
|------|-----|
| **PID 2947259** | **ALIVE**，运行 3h20m，GPU 93%/19.5GB |
| **当前 step** | ~1175 / 6633 (17%) |
| **max_steps** | 6633 (3 epochs) |
| **预计剩余** | ~10h（~6.8s/it） |

### eval_loss 趋势

| step | eval_loss |
|------|-----------|
| 200 | 0.1258 |
| 400 | 0.0761 |
| **600** | **0.0642** ← best |
| 800 | 0.2045 |
| 1000 | 0.1624 |

### train_loss 趋势（近3个log点）

| step | train_loss |
|------|-----------|
| 900 | 0.4092 |
| 950 | 0.6277 |
| 1000 | 0.4144 |
| 1150 | 0.4104 |

### Best checkpoint
`/home/sonny/exec-sim-repair-verifier/checkpoints_repo_cls_v5/checkpoint-600`（eval_loss=0.0642）

### 注意
eval_loss 在 step 600 后显著回升（0.0642 → 0.2045 → 0.1624），存在过拟合迹象。train_loss 仍在缓慢下降但 eval 已开始震荡。训练仍在进行中（17%），需关注后续 eval 是否能回落。

---
