# status precompute progress check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_precompute-progress-check_20260522T160708_result.json`
- **Structured JSON:** [`14bc39c98892f56cdebe.json`](../../sessions/14/14bc39c98892f56cdebe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### GPU 使用

| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 1% | 1.9 GB (空闲) |
| 1 | 18% | 6.9 GB |
| 2 | 1% | 1.9 GB (空闲) |
| 3 | 17% | 9.7 GB |
| 4 | 19% | 9.7 GB |
| 5 | 19% | 9.7 GB |

### SmolVLA Precompute 任务

**3 个 SmolVLA precompute 日志全部为空（0 字节）：**
- `precompute-smolvla-object-k10.log` — 创建于 22 日 23:47，0 bytes
- `precompute-smolvla-spatial-k10.log` — 创建于 22 日 23:48，0 bytes
- `precompute-smolvla-goal-k10.log` — 创建于 22 日 23:48，0 bytes

这 3 个任务**未实际运行**或启动时立即失败（未产生任何输出）。

### 实际在跑的任务

1. **`precompute-lerobot-object-fixed.log`**（仍在写入，2105 bytes）
   - 进度：Task 1 ep 8 / 共 10 tasks × 10 eps = **19/100 episodes**（19%）
   - 速度：~19.5s/ep
   - 预计剩余：81 eps × 19.5s ≈ **26 分钟**
   - 无错误

2. **`eval-lerobot-long-seed{0,1,2}.log`**（3 个，各 ~12MB，仍在写入）
   - 占用 GPU 3/4/5（9.7GB 每个）
   - 这是 lerobot long-horizon 评估，不是 SmolVLA precompute

### 结论

SmolVLA 的 3 个 precompute 任务（object/spatial/goal）**没有成功启动**，日志文件被创建但无内容写入。需要检查启动命令或 tmux session 确认失败原因。GPU 3/4/5 当前被 eval-lerobot-long 评估任务占用。

---
