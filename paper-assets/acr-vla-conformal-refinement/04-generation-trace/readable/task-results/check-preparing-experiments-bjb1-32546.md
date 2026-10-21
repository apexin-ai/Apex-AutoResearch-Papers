# check preparing experiments bjb1 32546

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_preparing-experiments-bjb1-32546_20260516T072341_result.json`
- **Structured JSON:** [`fe28ca28985906372511.json`](../../sessions/fe/fe28ca28985906372511.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**3 个实验全部正常运行中。** Cron reconcile 未检测到是因为它们不在 tmux session 中（而是由 tmux session `eval-acr-object-v4-obs-only` 下的子 shell 启动）。

| 实验 | PID (python) | 状态 | 运行时长 | GPU | GPU 显存 | GPU 利用率 |
|------|-------------|------|---------|-----|---------|-----------|
| eval-scalar-object-seed44-r2 | 226878 | `Rl` (运行中) | ~12min | cuda:0 | 5665 MiB | 20% |
| eval-obs-only-object-norm01-seed44 | 227086 | `Rl` (运行中) | ~12min | cuda:4 | 5665 MiB | 23% |
| eval-obs-only-object-default-seed44 | 229751 | `Rl` (运行中) | ~10min | cuda:5 | 5665 MiB | 22% |

**日志进度**：3 个实验都已完成模型加载和环境初始化（"10 tasks loaded"），正在执行 rollout 评估。日志输出到 stdout 被重定向到文件，evaluate.py 用了 `-u` 无缓冲模式，当前没有新输出说明 rollout 正在跑但还没打 print。

**Cron 未检测到的原因**：这 3 个实验的 bash wrapper 进程挂在已有的 tmux session `eval-acr-object-v4-obs-only` 下，而非各自独立的 tmux session。Reconcile 可能是按 session 名匹配的，找不到名为 `eval-scalar-object-seed44-r2` 等的独立 session。

---
