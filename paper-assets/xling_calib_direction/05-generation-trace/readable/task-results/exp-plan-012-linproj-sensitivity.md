# exp plan 012 linproj sensitivity

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_plan_012_linproj_sensitivity_20260520T232058_result.json`
- **Structured JSON:** [`465ba7c1ed672cd1da98.json`](../../sessions/46/465ba7c1ed672cd1da98.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果已保存到 `/root/xling_calib_direction/results/linproj_sensitivity.csv`（320行数据，8层×5语言×8个N值）。

## 关键发现

**Mean-shift 效果因层和语言差异极大，不是稳健的校准方法。**

### 有效的组合（ΔECE < 0，mean-shift 改善校准）

| Layer | Lang | ECE_ZS | ECE_MS(all) | ΔECE |
|-------|------|--------|-------------|------|
| 8 | sw | 0.629 | 0.479 | **-0.150** |
| 8 | zh | 0.445 | 0.347 | **-0.098** |
| 12 | zh | 0.418 | 0.379 | -0.039 |
| 0 | hi | 0.444 | 0.424 | -0.020 |

### 有害的组合（ΔECE > 0，mean-shift 恶化校准）

| Layer | Lang | ECE_ZS | ECE_MS(all) | ΔECE |
|-------|------|--------|-------------|------|
| 0 | sw | 0.313 | 0.451 | **+0.138** |
| 0 | zh | 0.314 | 0.367 | +0.053 |
| 0 | ko | 0.375 | 0.426 | +0.050 |
| 8 | hi | 0.488 | 0.535 | +0.047 |

### N 的影响

- N=10 时方差大（std ~0.03-0.07），N≥200 后基本稳定（std <0.01）
- N 对 mean-shift 方向（改善/恶化）无影响——小 N 和大 N 的 ΔECE 符号一致
- 对于有效组合（layer8-sw），N=10 反而效果最好（ΔECE=-0.169 vs all=-0.150），但方差高

### 结论
Mean-shift 不是通用校准方法。它只在特定 layer-language 组合上有效（如 layer8 的 sw/zh），在其他组合上反而恶化校准。这说明语言间的 representation shift 不是简单的均值平移。

---
