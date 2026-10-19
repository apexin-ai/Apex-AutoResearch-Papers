# code baseline std libero10

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_baseline_std_libero10_20260516T030235_result.json`
- **Structured JSON:** [`782e47de5d27b560f409.json`](../../sessions/78/782e47de5d27b560f409.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评测已成功启动，正在执行 rollout（520 步，当前进度 5%，~1 it/s）。checkpoint 加载正常，无 OOM 或错误。

**总结**：
- `mvp1_baseline_std_libero10` 已在 westb-13953 cuda:1 上运行，PID 738549
- 使用 `scripts/eval_baseline.py`（之前任务描述的 `lerobot/scripts/eval.py` 路径不存在，已修正）
- libero_10 有 10 个 task × 50 episodes，每个 rollout 最多 520 步，预计 5-8 小时完成
- Registry 已注册为 RUNNING，parent=mvp1_baseline_std

---
