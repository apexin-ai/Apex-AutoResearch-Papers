# check gradient json conflict rate

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gradient-json-conflict-rate_20260527T095951_result.json`
- **Structured JSON:** [`68ec89043b212732c142.json`](../../sessions/68/68ec89043b212732c142.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果非常明确。

## 核实结论

**三种计算方式完全一致**，不存在 per-layer average vs global 的差异：

| 指标 | Full OCC BN | Full OCC LN |
|------|-------------|-------------|
| Per-layer avg conflict rate | **45.6%** | **45.7%** |
| Global conflict rate (pooled) | **45.6%** | **45.7%** |
| Per-sample avg | **45.6%** | **45.7%** |

三个数字相同是因为每层有完全相同的 200 个 batch，且 skipped 的 2 层（全 None）不参与计算，所以 per-layer average = global pooled = per-sample average，数学上等价。

### 具体数据
- 有效层数：51 层（共 53 层，2 层无梯度跳过）
- 每层 200 batches
- Mean cosine similarity: +0.0065 (BN) / +0.0045 (LN) — 极接近零，略正
- Per-layer range: BN [0.38, 0.575], LN [0.40, 0.51]

### 论文该写什么
论文写 **"≈46%"** 是正确的。不存在 "≈50%" 的全局冲突率——那可能是看到某些个别层（如 `fused_featurizer.blocks.19` = 0.50 或 `blocks.24` = 0.575）误以为是全局数字。正确的全局数值就是 **45.6%-45.7%**，论文用 "≈46%" 完全准确。

---
