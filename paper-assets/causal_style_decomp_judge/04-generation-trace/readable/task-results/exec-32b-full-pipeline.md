# exec 32b full pipeline

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exec_32b_full_pipeline_20260520T171934_result.json`
- **Structured JSON:** [`cc4df617b6cda9a15d0c.json`](../../sessions/cc/cc4df617b6cda9a15d0c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全流程完成。

---

## Counterfactual Gen
- 状态: 完成
- 总条数: 100

## Content Verification
- 总条数: 100
- NLI>=0.90 pass rate: 88.0%
- NLI mean: 0.8956
- BERTScore>=0.92: 25

## Judge Scoring
- 总条数: 100（去重后）
- Null scores: 0
- Duplicates: 0

## ATE Analysis (完整 stdout)

### PRIMARY ANALYSIS (NLI≥0.90, n=88)
```
Overall:
  N = 88
  Raw ATE          = -0.1023  (SE=0.1490)
  Raw 95% CI       = [-0.3985, +0.1940]
  Raw p-value      = 0.494428
  Raw Cohen's d    = -0.0731
  Rewrite bias     = -0.2045
  Corrected ATE    = +0.1023  (SE=0.1048)
  Corrected 95% CI = [-0.1060, +0.3106]
  Corrected p      = 0.331808
  Corrected d      = +0.1040

Directional:
  formal→casual  (n=50): Corrected ATE = +0.1400, p = 0.331996, d = +0.1386
  casual→formal  (n=38): Corrected ATE = +0.0526, p = 0.736542, d = +0.0550

Stratified:
  nli_cf≥0.90 (n=88): ATE=+0.1023, p=0.331808, d=+0.1040
  bertscore_cf≥0.85 (n=60): ATE=+0.0333, p=0.810681, d=+0.0311
  bertscore_cf≥0.88 (n=41): ATE=-0.1707, p=0.241382, d=-0.1857
  bertscore_cf≥0.90 (n=29): ATE=-0.1724, p=0.305327, d=-0.1939
  bertscore_cf≥0.92 (n=25): ATE=-0.1600, p=0.356264, d=-0.1881
  all (n=88): ATE=+0.1023, p=0.331808, d=+0.1040
```

### SENSITIVITY 1: exclude NLI<0.50 (n=88)
```
Overall:
  N = 88
  Raw ATE          = -0.1023  (SE=0.1490)
  Raw 95% CI       = [-0.3985, +0.1940]
  Raw p-value      = 0.494428
  Raw Cohen's d    = -0.0731
  Rewrite bias     = -0.2045
  Corrected ATE    = +0.1023  (SE=0.1048)
  Corrected 95% CI = [-0.1060, +0.3106]
  Corrected p      = 0.331808
  Corrected d      = +0.1040

Directional:
  formal→casual  (n=50): Corrected ATE = +0.1400, p = 0.331996, d = +0.1386
  casual→formal  (n=38): Corrected ATE = +0.0526, p = 0.736542, d = +0.0550

Stratified: (same as PRIMARY — no records with NLI<0.50 after NLI≥0.90 filter)
```

### SENSITIVITY 2: winsorize at 3σ (n=88)
```
Winsorize bounds=[-4.30, +4.09], clipped 2 values

Overall:
  N = 88
  Raw ATE          = -0.0636  (SE=0.1331)
  Raw 95% CI       = [-0.3281, +0.2009]
  Raw p-value      = 0.634078
  Raw Cohen's d    = -0.0509
  Rewrite bias     = -0.1595
  Corrected ATE    = +0.0959  (SE=0.1050)
  Corrected 95% CI = [-0.1127, +0.3045]
  Corrected p      = 0.363294
  Corrected d      = +0.0974

Directional:
  formal→casual  (n=50): Corrected ATE = +0.1400, p = 0.331996, d = +0.1386
  casual→formal  (n=38): Corrected ATE = +0.0379, p = 0.808917, d = +0.0395
```

### REFERENCE: all records (n=100)
```
Overall:
  N = 100
  Raw ATE          = -0.0800  (SE=0.1656)
  Raw 95% CI       = [-0.4085, +0.2485]
  Raw p-value      = 0.630015
  Raw Cohen's d    = -0.0483
  Rewrite bias     = -0.1800
  Corrected ATE    = +0.1000  (SE=0.0959)
  Corrected 95% CI = [-0.0902, +0.2902]
  Corrected p      = 0.299475
  Corrected d      = +0.1043

Directional:
  formal→casual  (n=59): Corrected ATE = +0.1525, p = 0.236397, d = +0.1558
  casual→formal  (n=41): Corrected ATE = +0.0244, p = 0.868200, d = +0.0261
```

## RATE Ratios
```
ate_primary: raw=-0.1023, corr=+0.1023, ratio=-1.0000
ate_sens1:   raw=-0.1023, corr=+0.1023, ratio=-1.0000
ate_sens2:   raw=-0.0636, corr=+0.0959, ratio=-1.5091
ate_all:     raw=-0.0800, corr=+0.1000, ratio=-1.2500
```

## 输出文件
```
-rw-r--r-- 1 root root  2701 May 21 01:28 ate_all_summary.csv
-rw-r--r-- 1 root root 39700 May 21 01:28 ate_bar.png
-rw-r--r-- 1 root root  2712 May 21 01:28 ate_primary_summary.csv
-rw-r--r-- 1 root root  2712 May 21 01:28 ate_sens1_summary.csv
-rw-r--r-- 1 root root  2750 May 21 01:28 ate_sens2_summary.csv
-rw-r--r-- 1 root root 72673 May 21 01:28 score_violin.png
```

---
