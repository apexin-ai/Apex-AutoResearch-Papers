# analysis gemma4 cosine compression

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gemma4_cosine_compression_20260522T165649_result.json`
- **Structured JSON:** [`c8d5438be47fb7b3d205.json`](../../sessions/c8/c8d5438be47fb7b3d205.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成，6 秒处理 520 个文件（287 个有效 trace，114,450 step-pairs）。

## 结果

### 42 层 Mean Cosine Distance

| 区间 | 层 | Mean Cos Dist | 特征 |
|------|-----|--------------|------|
| **Shallow** | L0 | 0.2148 | 异常高（embedding 层） |
| | L1 | 0.0180 | 最低 |
| | L2 | 0.0555 | |
| | L3 | 0.1009 | |
| | L4 | 0.1320 | |
| | L5 | 0.1756 | |
| Mid-low | L6-L15 | 0.043–0.148 | 先升后降 |
| Mid-high | L16-L29 | 0.048–0.278 | L22 峰值 0.278 |
| **Deep** | L30-L40 | 0.048–0.103 | 相对稳定低值 |
| | L41 | 0.5899 | 异常高（output 层） |

### Shallow vs Deep 对比

| 指标 | 值 |
|------|-----|
| Shallow (L0-L5) mean | **0.116122** |
| Deep (L30-L41) mean | **0.110737** |
| Ratio (shallow/deep) | **1.0486** |
| Compression | **未确认** |

### 结论

**Shallow compression 未确认。** Ratio = 1.049，shallow 层 mean cosine distance 反而略高于 deep 层（+4.9%）。

但数据揭示了更有趣的结构：
- **L0 和 L41 是 outlier**（embedding/output 层），cosine distance 远高于其他层
- 排除 L0/L41 后，shallow (L1-L5) mean ≈ 0.096，deep (L30-L40) mean ≈ 0.067 → ratio ≈ 1.43，shallow 实际比 deep **高 43%**——即 shallow 层变化更大，不是更小
- 真正的"低活动区"在 mid-depth (L11-L15)，mean ≈ 0.04-0.05
- L17-L23 有显著的 activity spike（peak L22 = 0.278）

Gemma-4 的 geometric profile 与假设相反：shallow 层并没有 compression，反而 deep 层更趋于稳定。

---
