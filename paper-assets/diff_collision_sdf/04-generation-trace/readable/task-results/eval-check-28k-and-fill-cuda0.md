# eval check 28k and fill cuda0

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_check_28k_and_fill_cuda0_20260527T071340_result.json`
- **Structured JSON:** [`52642791401d6ecd3415.json`](../../sessions/52/52642791401d6ecd3415.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

命令行参数确认正确，`--pi05` 存在。

汇总：

**28K eval 已启动（cuda:0）**
- PID: 694475（主进程），父进程 694470
- Checkpoint: `.../a1_sdf_pi05_object_pudding_seed0_l1/28000`
- 日志: `/tmp/eval_28k_s0_l1.log`
- 参数已确认含 `--pi05`

**注意**：任务给的 checkpoint 路径有误——实际目录是 `seed0_l1`（不是 `seed0_l01_high`）。`seed0_l01` 目录下的 30000 是 5月24日旧 run 的产物。

**训练进度**
| 任务 | 当前 step | 进度 | 预计剩余 |
|------|----------|------|---------|
| λ=0.1 s0 (cuda:1) | 28530/30000 | 95% | ~1h54m |
| λ=0.1 s1 (cuda:2) | 27984/30000 | 93% | ~2h37m |

---
