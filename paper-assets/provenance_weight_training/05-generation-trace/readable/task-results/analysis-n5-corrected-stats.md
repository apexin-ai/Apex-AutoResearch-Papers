# analysis n5 corrected stats

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_n5_corrected_stats_20260524T084245_result.json`
- **Structured JSON:** [`748c256620c4f14343a8.json`](../../sessions/74/748c256620c4f14343a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

计算完成。完整统计结果如下：

---

## N=5 统计分析结果（B=4 修正后）

### 数据表

| Seed | Adaptive (B=4) | Uniform (B=4) | Δ (A−U) |
|------|----------------|---------------|---------|
| 42   | 17.680         | 17.694        | −0.0140 |
| 123  | 17.666         | 17.686        | −0.0200 |
| 456  | 17.677         | 17.702        | −0.0250 |
| 789  | 17.668         | 17.696        | −0.0280 |
| 234  | 17.678         | 17.708        | −0.0300 |

### 统计量

| 指标 | 值 |
|------|-----|
| 5-seed Mean Δ | **−0.0234** |
| SD of Δ | 0.0065 |
| SE of Δ | 0.0029 (= 0.0065/√5) |
| Paired t (df=4) | **−8.0931** |
| p (uncorrected) | **0.001267** |
| p BH-corrected (k=9, rank 1) | **0.01140** |
| 95% BCa Bootstrap CI | **[−0.0280, −0.0176]** |
| Cohen's d | **−3.62** |
| Cohen's d 95% CI | [−4.86, −2.38] |
| Effect size interpretation | Large |
| CI excludes 0 | Yes |

### 验证结果

- **adaptive_seed789**: 训练日志确认 `batch_size: 4`，无 gradient_accumulation（默认=1），即有效 batch size = 4 ✓
- **adaptive_seed234**: 训练日志确认 `batch_size: 4`，无 gradient_accumulation（默认=1），即有效 batch size = 4 ✓
- **uniform_seed789**: holdout PPL = 17.6955（eval JSON 确认，与 Director 值 17.696 吻合）
- **uniform_seed234**: holdout PPL = 17.7083（eval JSON 确认，与 Director 值 17.708 吻合）
- adaptive seed789/234 的 eval JSON 不在服务器上，PPL 值（17.668/17.678）取自 Director 确认值

JSON 结果已保存至 `/root/autodl-tmp/provenance_weight_training/output/eval_results/n5_corrected_stats.json`。

---
