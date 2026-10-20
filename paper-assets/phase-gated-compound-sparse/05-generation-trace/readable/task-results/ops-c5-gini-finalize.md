# ops c5 gini finalize

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_c5_gini_finalize_20260516T035624_result.json`
- **Structured JSON:** [`7978bea44b661071f347.json`](../../sessions/79/7978bea44b661071f347.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集完成。

## 结果报告

### 完成状态
- **DS c5_gini: 30/30 完成** ✓
- **QW c5_gini: 30/30 完成** ✓
- **PID 307021: 已结束**
- **GPU 0: 已释放** (0MiB / 97887MiB)
- **无 error/traceback**

---

### DS (DeepSeek-R1-Distill-Qwen-7B) Per-Phase Gini Delta Mean

| Sparsity | Method | Global | Low | Mid | High |
|----------|--------|--------|-----|-----|------|
| s015 | importance | -0.0301 | -0.0163 | -0.0073 | -0.0152 |
| s015 | random | -0.0309 | -0.0102 | -0.0006 | -0.0062 |
| s020 | importance | -0.0404 | -0.0209 | -0.0092 | -0.0200 |
| s020 | random | -0.0403 | -0.0120 | -0.0007 | -0.0085 |
| s025 | importance | -0.0647 | -0.0313 | -0.0133 | -0.0267 |
| s025 | random | -0.0620 | -0.0150 | -0.0096 | -0.0112 |
| s030 | importance | -0.0806 | -0.0373 | -0.0183 | -0.0314 |
| s030 | random | -0.0732 | -0.0183 | -0.0093 | -0.0138 |

### QW (Qwen2.5-7B-Instruct) Per-Phase Gini Delta Mean

| Sparsity | Method | Global | Low | Mid | High |
|----------|--------|--------|-----|-----|------|
| s015 | importance | -0.0103 | -0.0165 | -0.0094 | -0.0120 |
| s015 | random | -0.0186 | -0.0083 | -0.0038 | -0.0036 |
| s020 | importance | -0.0121 | -0.0200 | -0.0115 | -0.0143 |
| s020 | random | -0.0229 | -0.0119 | -0.0053 | -0.0067 |
| s025 | importance | -0.0100 | -0.0286 | -0.0168 | -0.0207 |
| s025 | random | -0.0337 | -0.0014 | -0.0081 | **+0.0045** |
| s030 | importance | -0.0202 | -0.0350 | -0.0183 | -0.0239 |
| s030 | random | -0.0447 | -0.0221 | -0.0077 | -0.0061 |

### 关键模式

**DS**: importance 在所有 phase 上 delta 绝对值都大于 random（pruning 压缩 Gini 更多），low_sparsity phase 受影响最大，mid_sparsity 最小。

**QW**: importance 的 per-phase delta 更均匀（low ≈ mid ≈ high），random 则 phase 间差异大。注意 s025_random 的 high_sparsity phase 出现 **+0.0045**（Gini 反增），是唯一正值。QW 的 global delta 呈现反直觉模式：importance 的 global |delta| 反而比 random 小（如 s030: -0.0202 vs -0.0447），说明 QW 上 importance pruning 对全局 Gini 的压缩反而更温和，但在 per-phase 层面影响更深。

---
