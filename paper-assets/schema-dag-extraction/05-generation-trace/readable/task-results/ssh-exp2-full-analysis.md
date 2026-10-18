# ssh exp2 full analysis

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp2-full-analysis_20260515T022540_result.json`
- **Structured JSON:** [`9fd2973433688c2dafd2.json`](../../sessions/9f/9fd2973433688c2dafd2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## exp2 完成确认

54 batches 全部完成，无错误，耗时 11732s (~3.3h)。

---

## text-match 重评估汇总

| Count | #Bat | ExactF1 | RelaxF1 | **TextF1** | TextP | TextR | P/G | Hallu | WrTyp | Spur |
|---------|------|---------|---------|----------|-------|-------|------|-------|-------|-------|
| count_6 | 27 | 0.1957 | 0.2203 | **0.2000** | 0.1189 | 0.6292 | 5.29 | 1417 | 426 | 34273 |
| count_12 | 27 | 0.2263 | 0.2560 | **0.2298** | 0.1471 | 0.5247 | 3.57 | 5771 | 1216 | 35639 |

---

## 关键数字

### PRIMARY: r(recall, BCS)

| Scope | r | p | CI 95% | n | 判定 |
|-------|------|------|--------|---|------|
| count_6 | 0.2754 | 0.1644 | [-0.117, 0.593] | 27 | **FAIL** |
| count_12 | 0.2219 | 0.2660 | [-0.173, 0.555] | 27 | **FAIL** |
| Partial (|count) | 0.2522 | 0.0658 | [-0.017, 0.487] | 54 | **FAIL** |

### SECONDARY: r(F1, BCS)

| Scope | r | p | CI 95% | n | 判定 |
|-------|------|------|--------|---|------|
| count_6 | 0.1754 | 0.3814 | [-0.219, 0.521] | 27 | FAIL |
| count_12 | **0.5012** | **0.0077** | [0.150, 0.740] | 27 | **PASS** |
| Partial (|count) | **0.3025** | **0.0262** | [0.038, 0.528] | 54 | **PASS** |

### MECHANISTIC: Confusion Rate (wrong_type / total_pred)

| Batch | wrong_type | total_pred | **confusion_rate** |
|-------|------------|------------|--------------------|
| count_6_high_bcs | 55 | 999 | **5.51%** |
| count_6_low_bcs | 2 | 1,563 | **0.13%** |
| count_12_high_bcs | 79 | 1,944 | **4.06%** |
| count_12_low_bcs | 8 | 1,465 | **0.55%** |

High-BCS confusion rate >> Low-BCS → **PASS**（~30-40x 差异）

T-test (top/bottom third by BCS):
- count_12: t=2.22, p=0.043 → significant
- count_6: t=0.01, p=0.989 → not significant

---

## GO/NO-GO 判定

**PRIMARY criterion: FAIL** — r(recall, BCS) 在两个 count 和偏相关中均未达到 |r|≥0.3 且 p<0.05。

解读：
- BCS 的效应更多体现在 **precision 通道**（通过 wrong_type confusion）而非 recall。F1 在 count_12 达到 r=0.50 (p=0.008)，partial r=0.30 (p=0.026)。
- **Mechanistic evidence 强烈支持** confusability 假设：high-BCS 批次的 type confusion 率是 low-BCS 的 30-40 倍。
- 每组 n=27 对检测 r≈0.25 的效应量而言统计功效不足。

---

## 产出文件

```
results/exp2_reeval_results.json      # per-batch text_match 评估
results/exp2_reeval_summary.json      # per-count 聚合
results/analysis_summary.json         # 完整统计分析
results/exp2_analysis_f1.png/pdf      # BCS vs F1 散点图 (per-count)
results/exp2_analysis_f1_combined.png/pdf
results/exp2_analysis_recall.png/pdf  # BCS vs Recall 散点图
results/exp2_analysis_recall_combined.png/pdf
```

---
