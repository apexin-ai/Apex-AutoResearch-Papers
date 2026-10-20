# ops v5 kill v6 launch

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_v5_kill_v6_launch_20260518T175344_result.json`
- **Structured JSON:** [`46eab3390405758f7a0b.json`](../../sessions/46/46eab3390405758f7a0b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报如下：

---

### 1. v5 Kill 状态
- tmux session `phase2_tg_s42_v5` 已 kill，但有残留 python 进程 (PID 3644, 85GB VRAM)
- 手动 kill -9 清理，GPU 完全释放

### 2. GPU 释放确认
- nvidia-smi: 0MiB / 97887MiB, 0% util, 无 python 进程

### 3. Dry-run 结果

| 指标 | Step 0 | Step 4 |
|------|--------|--------|
| L_NTP | 2.0275 | 1.6544 |
| L_GAR | -0.0161 | -0.0147 |
| Total Loss | 2.0114 | 1.6397 |

- **Gate 梯度**: True
- **L_GAR 非零**: 是（约 -0.01 ~ -0.02）
- **初始 gate 统计 (step 0)**: mean=0.8097, std=0.0341, min=0.6836, max=0.8672
- **最终 gate 统计 (step 5)**: mean=0.8025, std=0.0842, min=0.5547, max=0.9805
- **报错**: 无（修复了一个 `total_mem` → `total_memory` 的 typo）

### 4. 全量训练
- 已通过 tmux session `phase2_tg_s42_v6` 启动，3000 total steps, 3 epochs
- GPU 占用 84GB, 86% util，已在正常训练
- Registry 已更新为 RUNNING

---
