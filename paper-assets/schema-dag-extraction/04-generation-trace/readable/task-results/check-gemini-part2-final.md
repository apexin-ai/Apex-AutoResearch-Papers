# check gemini part2 final

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gemini_part2_final_20260519T222709_result.json`
- **Structured JSON:** [`053794a5f90e1ed88c44.json`](../../sessions/05/053794a5f90e1ed88c44.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Gemini Dim2 BCS-controlled 实验结果

**状态**: 已完成。6720 samples, 60 batches。

### 按 count level

| Count Level | Batches | Low BCS Acc | High BCS Acc | Gap | Pearson r | Spearman ρ |
|-------------|---------|-------------|--------------|-----|-----------|------------|
| count_8 | 50 (25+25) | 0.9050 | 0.7292 | **+17.58pp** | -0.8873 | -0.7428 |
| count_16 | 10 (5+5) | 0.8146 | 0.7281 | **+8.65pp** | -0.8043 | -0.4012 |

### 全局汇总

- **Pooled Pearson r = -0.8690**
- **Pooled Spearman ρ = -0.8046**
- BCS 越高 → accuracy 越低，负相关非常强

### 要点

1. **count_8 效果最显著**：low-high gap 达 17.58pp，Pearson r=-0.89，BCS 对 schema 复杂度的预测力在小 schema 上最强
2. **count_16 gap 收窄到 8.65pp**：Spearman 仅 -0.40，可能因为只有 5 batches/group，统计功效不足
3. **count_16_high_4 是极端异常点**：BCS=0.9706（远超其他 high batch 的 0.58-0.62），acc 仅 0.5990，拉大了 Pearson 但可能扭曲 Spearman
4. count_8 的 low group 中多个 batch acc > 0.95（最高 0.9792），说明低 BCS schema 对 Gemini 几乎无难度

---
