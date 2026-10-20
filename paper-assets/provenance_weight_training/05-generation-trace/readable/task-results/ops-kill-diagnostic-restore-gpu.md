# ops kill diagnostic restore gpu

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-diagnostic-restore-gpu_20260514T084731_result.json`
- **Structured JSON:** [`760e24170b24c0bd8ec8.json`](../../sessions/76/760e24170b24c0bd8ec8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成，汇总结果：

1. **进程 kill**：78065 和 77192 均已成功终止
2. **GPU 显存**：4 张卡全部 ~46523 MiB，利用率 99%，GPU 2/3 恢复正常
3. **训练速度**：
   - `grid_b1_0_seed123`（GPU 2）：**2.12s/it**，已恢复
   - `grid_b1_5_seed123`（GPU 3）：**2.11s/it**，已恢复
4. **`contamination_ratio` 默认值**：**0.2**（第 213 行 `default=0.2`）。诊断实验必须显式传 `--contamination_ratio 0.0` 和 `--contamination_ratio 1.0`，否则会用默认的 0.2。另外 `tau` 会根据 contamination_ratio 自动计算：`tau = 1.0 - contamination_ratio * 0.5`。

---
