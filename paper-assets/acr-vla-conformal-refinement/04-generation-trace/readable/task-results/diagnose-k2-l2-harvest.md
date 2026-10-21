# diagnose k2 l2 harvest

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_k2-l2-harvest_20260519T212754_result.json`
- **Structured JSON:** [`24035176a2a4fc39f97d.json`](../../sessions/24/24035176a2a4fc39f97d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**状态：运行中，约 45% 完成。**

- **进程** PID 995736，已运行 55 分钟，状态 `Rl`（running）
- **进度**：10 个 task × 5 episodes = 50 episodes 总计。目前完成了 5 个 task 的全部 episodes（25 ep）+ 第 6 个 task 的 2 ep = **27/50 episodes（54%）**
- 每个 episode 约 151s，剩余 ~23 episodes ≈ **58 分钟**
- **预计完成时间**：约 1 小时后

当前 log 中没有 "Episode" 关键词（用的是 "ep" 格式），grep 返回 0。输出重定向到 `/tmp/k2_l2_calibration.log` 而非 `logs/` 目录下的 log 文件。JSON 会在全部 50 episodes 跑完后才写入 `logs/k2_l2_calibration.json`。

---
