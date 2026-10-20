# ops 34685 eval status

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_34685-eval-status_20260526T232327_result.json`
- **Structured JSON:** [`7f855fc423b67cf5030a.json`](../../sessions/7f/7f855fc423b67cf5030a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Eval 状态汇总 (westd-34685)

| Eval | GPU | PID | 状态 | 进度 |
|------|-----|-----|------|------|
| **vanilla_v2_s1** | 0 | 516125 | **Running** | Task 8/10 (80%) — T7 刚完成 TSR=0.960 CAR=0.980，T8 已开始 |
| **vanilla_v2_s2** | 1 | 511757 | **Running** | 进程在跑，但 `/tmp/vanilla_v2_s2_eval.log` 不存在（日志可能输出到 tmux/stdout） |
| **detach_ln_s3** | 2 | 565727 | **Running** | Task 3/10 (30%), 当前 episode 86% (43/50) |
| **cutoff_25k_s1_v2** | 3 | 620069 | **Running** | Task 3/10 (30%), 当前 episode 84% (42/50) |

### GPU 使用情况
- 4 张卡各有 1 个 eval 进程，每个占 ~16.7 GB 显存
- GPU 3 另有一个已退出的 PID 567681（/proc 已不存在，nvidia-smi 残留）
- GPU Util 0-7%（正常，eval 主要是 CPU 端仿真）

### 注意事项
- **vanilla_v2_s2** 缺 eval 日志文件，无法确认具体进度。可能是启动时没做日志重定向（`> /tmp/vanilla_v2_s2_eval.log 2>&1`）。进程本身在正常运行。
- **vanilla_v2_s1** 进度最快，预计还需 ~2 个 task（约 10-15 分钟）即可完成。
- **detach_ln_s3** 和 **cutoff_25k_s1_v2** 进度接近，都在 Task 3，还有 7 个 task 待跑，预计还需 ~1.5-2 小时。

---
