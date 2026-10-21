# healthcheck westd27271 gpu0 stall

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_healthcheck-westd27271-gpu0-stall_20260523T221725_result.json`
- **Structured JSON:** [`f22245e4b4092ba9a34b.json`](../../sessions/f2/f22245e4b4092ba9a34b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### GPU 0 — eval_openvla_l2norm_k05_goal_seed42_v3 (PID 380585)

| 项目 | 状态 |
|------|------|
| 进程 | **存活**，运行 3h12m |
| GPU 显存 | 15964 MiB |
| GPU util | 39% |
| 日志最后更新 | 2026-05-24 06:16:16 (刚刚) |
| 当前进度 | **Task 8/10** "turn on the stove"，Ep 30/50，task_sr=29/30 |
| 速度 | ~2.0 eps/min |

**结论：正常运行，无 stall。** 之前报告的无日志更新是日志路径检查错误（日志在 `~/runs/` 不在 `/tmp/`）。预计剩余 ~1h 完成（Task 8 剩 20 ep + Task 9-10 各 50 ep）。

已完成 task SR 汇总：
- Task 4: 6.0%, Task 5: 66.0%, Task 6: 20.0%, Task 7: 22.0%

### GPU 1 — eval_openvla_baseline_long_seed42 (PID 291093)

| 项目 | 状态 |
|------|------|
| 进程 | **存活**，运行 6h38m |
| GPU 显存 | 15816 MiB |
| GPU util | 70% |
| 日志最后更新 | 2026-05-24 06:16:26 (刚刚) |
| 当前进度 | **Task 9/10**，Ep 20/50，task_sr=5/20 |
| 速度 | ~1.1 eps/min |

**结论：正常运行。** 预计剩余 ~1h 完成。

**总结：两个 GPU 均正常工作，无 hang，无需干预。**

---
