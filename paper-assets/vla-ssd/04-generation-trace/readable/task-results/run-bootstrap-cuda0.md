# run bootstrap cuda0

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_bootstrap_cuda0_20260522T144626_result.json`
- **Structured JSON:** [`f8c22cb84128f3c9c1f7.json`](../../sessions/f8/f8c22cb84128f3c9c1f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

运行状态确认：

| 项目 | 状态 |
|------|------|
| tmux session `bootstrap_cuda0` | 运行中 |
| GPU 0 占用 | 15384 MiB (python PID 670838) |
| 当前任务 | OpenVLA goal trained — 正在提取特征 (450/5000) |

**与用户预期的差异**：脚本 argparse 没有 `long` 选项，数据目录也没有 `libero_long`，所以实际是：
- OpenVLA: goal/spatial/object × 2 = **6 runs**
- NORA: goal/spatial × 2 = **4 runs**（object ×2 会被脚本优雅跳过）
- 有效总计 **10 runs**，不是 12

---
