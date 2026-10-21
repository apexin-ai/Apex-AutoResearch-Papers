# extract spatial untrained phases

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_extract_spatial_untrained_phases_20260522T111532_result.json`
- **Structured JSON:** [`ac7fe6590e10dd27164e.json`](../../sessions/ac/ac7fe6590e10dd27164e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## OpenVLA Spatial Untrained — 全 Phase 数据汇总

### 1. R² Probing

| 位置 | Peak R² | Peak Layer | Exit R² (L31) | Δ (peak−exit) |
|------|---------|------------|---------------|----------------|
| image_mean | **0.8431** | L11 | 0.8089 | 0.0342 |
| last_preaction | **0.8261** | L20 | 0.7768 | 0.0493 |

逐层 R²（image_mean）：L0=0.823 → L11=0.843（peak）→ L31=0.809，整体变化幅度很小（~0.02 range in mid layers）。

### 2. L1 Attention Profile

| 类别 | Head 数 | 占比 |
|------|---------|------|
| instruction_dominant | **25**/32 | 78.1% |
| image_dominant | 0/32 | 0% |
| mixed | 7/32 | 21.9% |

### 3. Cross-instruction Classification

| 指标 | 值 |
|------|-----|
| Accuracy | **~1.000**（所有层、两种位置均为 0.999–1.0）|
| Chance level | 0.10 |

所有 32 层的分类准确率均接近 1.0（L0-L9 image_mean 为 0.999，L10+ 为 1.0）。

### 4. RSA Analysis

| 位置 | Best Layer | Correlation | 95% CI |
|------|-----------|-------------|--------|
| image_mean | **L4** | **0.6051** | [0.497, 0.699] |
| last_preaction | L4 | 0.5671 | [0.466, 0.672] |

逐层 RSA（image_mean）：L0=0.552 → L4=0.605（peak）→ L16=0.576 → L31=0.465，从中层开始逐步下降。

### 汇总

| Phase | 关键指标 | 值 |
|-------|---------|-----|
| R² Probing | peak R² / layer | 0.843 / L11 |
| R² Probing | exit R² / Δ | 0.809 / 0.034 |
| L1 Attention | instr-dominant heads | 25/32 |
| Cross-instruction | accuracy | ~1.000 |
| RSA | peak correlation / layer | 0.605 / L4 |

---
