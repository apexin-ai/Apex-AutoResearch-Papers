# check read trajectory data

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_read-trajectory-data_20260516T014325_result.json`
- **Structured JSON:** [`4d023a456d304a9bd833.json`](../../sessions/4d/4d023a456d304a9bd833.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## V8 Checkpoint Trajectory 数据

### 训练进度
v8 当前 **step 26150/30000** (87%)，loss=0.0022，sps=3.1

### Trajectory 完整数据表（steps 2k–20k，每 2k 一个 checkpoint）

| Step | Standard (ACIS) | ACIS+Prune | Bypass (no ACIS) | Random Prune | ACIS Advantage |
|------|----------------|------------|-------------------|--------------|----------------|
| 2000 | 0.03787 | 0.03570 | 0.05842 | 0.04250 | 0.00680 |
| 4000 | 0.02563 | 0.02317 | 0.05024 | 0.02967 | 0.00650 |
| 6000 | 0.02040 | 0.01655 | 0.04046 | 0.02580 | 0.00925 |
| 8000 | 0.01848 | 0.01658 | 0.03845 | 0.02485 | 0.00827 |
| 10000 | 0.01310 | 0.00959 | 0.03597 | 0.02068 | 0.01109 |
| 12000 | 0.01455 | 0.01055 | 0.03719 | 0.01932 | 0.00878 |
| 14000 | 0.01705 | 0.01082 | 0.03943 | 0.02016 | 0.00933 |
| 16000 | 0.01022 | 0.00610 | 0.03188 | 0.01797 | 0.01187 |
| 18000 | 0.00899 | 0.00482 | 0.03325 | 0.01644 | 0.01162 |
| 20000 | 0.00782 | 0.00420 | 0.03275 | 0.01724 | 0.01304 |

**Baseline v5 final**: 0.00408

### 关键观察

- **Standard loss** 从 0.0379 → 0.0078，持续下降（-79%）
- **ACIS+Prune loss** 从 0.0357 → 0.0042，逼近 baseline 0.00408（仅差 3%）
- **Bypass loss** 下降缓慢，停滞在 ~0.033，说明 ACIS 路由对性能至关重要
- **ACIS Advantage**（ACIS 剪枝 vs 随机剪枝）从 0.0068 → 0.0130，随训练推进优势持续扩大
- Standard vs Bypass 的差距 (0.0078 vs 0.0327) 表明 ACIS 路由提供 ~4.2x 的 loss 改善

产出目录还包含 `checkpoint_trajectory.png` 和 `acis_advantage.png` 两张可视化图。

---
