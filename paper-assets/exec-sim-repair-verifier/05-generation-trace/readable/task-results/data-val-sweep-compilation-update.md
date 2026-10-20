# data val sweep compilation update

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_val-sweep-compilation-update_20260515T064909_result.json`
- **Structured JSON:** [`6506913b1946a874b5c2.json`](../../sessions/65/6506913b1946a874b5c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 结果汇总

### 1. val_sweep_compilation.md 更新

**Val 新增：** ckpt-1400 (85.97%), ckpt-1600 (86.75%) — 均低于 ckpt-1000 峰值，确认 post-peak decline。

**Test 新增：** ckpt-800 (83.53%, f1_fail=69.17), ckpt-1200 (83.84%, f1_fail=65.49), ckpt-1400 (85.47%, running_acc only)。

**Baseline 修正：** 8B s42 val majority baseline 72.96% → **75.88%**，gap 相应从 +15.27 pp 修正为 +12.35 pp。

### 2. s42 resume save_total_limit

- 代码默认值：`save_total_limit=5`
- 实际启动参数：`--save_total_limit 35`（见 agent_context spec）
- 当前 checkpoint 数量：**13 个**（800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200）

### 3. Checkpoint 丢失风险

**无风险。** save_total_limit=35，当前仅 13 个 checkpoint，远未触及上限。即使训练跑完 3 epochs（预计 ~6600 steps，约 33 个 checkpoint @save_steps=200），也在 35 的限制内。

---
