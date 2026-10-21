# run ate final 20260520

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_ate_final_20260520_20260520T144044_result.json`
- **Structured JSON:** [`90d6544cbd7ba69967e6.json`](../../sessions/90/90d6544cbd7ba69967e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Scoring 状态
- 总条数: 100
- Null scores: 0
- 重复 ID: 0

## ATE Analysis 完整输出
```
Loaded 100 scored records

============================================================
  Overall ATE Analysis (formality axis)
============================================================
  N = 100
  Raw ATE          = -0.0800  (SE=0.1161)
  Raw 95% CI       = [-0.3103, +0.1503]
  Raw p-value      = 0.492260
  Raw Cohen's d    = -0.0689
  Rewrite bias     = -0.2000
  Corrected ATE    = +0.1200  (SE=0.1028)
  Corrected 95% CI = [-0.0839, +0.3239]
  Corrected p      = 0.245749
  Corrected d      = +0.1168

============================================================
  Directional Analysis
============================================================

  formal→casual  (n=62)
    Corrected ATE = +0.0645, p = 0.567930, d = +0.0729

  casual→formal  (n=38)
    Corrected ATE = +0.2105, p = 0.299657, d = +0.1706

============================================================
  Stratified Analysis
============================================================
  primary: nli_cf≥0.90 (n=95): ATE=+0.1263, p=0.245852, d=+0.1198
  secondary: bertscore_cf≥0.85 (n=76): ATE=+0.1184, p=0.348828, d=+0.1081
  secondary: bertscore_cf≥0.88 (n=57): ATE=+0.1228, p=0.441571, d=+0.1027
  secondary: bertscore_cf≥0.90 (n=48): ATE=+0.1250, p=0.485292, d=+0.1015
  secondary: bertscore_cf≥0.92 (n=37): ATE=+0.0541, p=0.796895, d=+0.0426
  tertiary: all (n=100): ATE=+0.1200, p=0.245749, d=+0.1168

Saved summary to data/ate_summary.csv
Saved plots to data//
```

## RATE Ratio
- Raw ATE: -0.0800
- Corrected ATE: +0.1200
- RATE ratio: -1.5000

## 输出文件
```
-rw-r--r-- 1 root root 38820 May 20 22:42 ate_bar.png
-rw-r--r-- 1 root root  2729 May 20 22:42 ate_summary.csv
-rw-r--r-- 1 root root 69883 May 20 22:42 score_violin.png
```

---
