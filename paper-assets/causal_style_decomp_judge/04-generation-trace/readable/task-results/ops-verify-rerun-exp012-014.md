# ops verify rerun exp012 014

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify_rerun_exp012_014_20260521T000026_result.json`
- **Structured JSON:** [`0ec6e08bc80ec8236fcb.json`](../../sessions/0e/0ec6e08bc80ec8236fcb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

注意 exp-012 和 exp-014 脚本没有 CSV 写入逻辑（代码中虽然接受 `--output-dir` 参数但没有实际写 CSV）。exp-011 成功生成了 CSV。

现在整理完整报告。

---

## 完整验证报告

### 1. exp-012: Consistency Filter Bias Analysis — 完整 console output

```
Loaded 100 pairwise records

======================================================================
  Consistency Filter Bias Analysis
======================================================================
  Total valid: 98
  Consistent:   55 (56.1%)
  Inconsistent: 43 (43.9%)

  --- NLI Score ---
  Consistent (n=55):   mean=0.8588, std=0.3270
  Inconsistent (n=43): mean=0.9383, std=0.2056
  Mann-Whitney U: U=1214.0, p=0.824367
  KS test: D=0.1383, p=0.680267

  --- BERTScore ---
  Consistent (n=55):   mean=0.8547
  Inconsistent (n=43): mean=0.8847
  Mann-Whitney U: U=965.0, p=0.120293

  --- Response Length ---
  Original length — consistent: mean=560, inconsistent: mean=733
    Mann-Whitney U: p=0.137405
  |orig-cf| length diff — consistent: mean=110, inconsistent: mean=127
    Mann-Whitney U: p=0.714958

  --- Position Bias ---
  Consistent (n=55): Trial1 A rate=69.1%, Trial2 A rate=30.9%
  Inconsistent (n=43): Trial1 A rate=55.8%, Trial2 A rate=55.8%

  --- Interpretation ---
  ✓ No significant systematic bias detected in consistency filter
```

### 2. exp-014: Logistic Decomposition — 完整 console output

```
Loaded 100 pairwise records

======================================================================
  Direction-Asymmetry Analysis (formality)
======================================================================
  Consistent pairs: 55

  --- formal→casual (n=33) ---
  formal wins: 26/33 (78.8%)
  casual wins: 7/33
  95% CI (Wilson): [0.6225, 0.8932]
  Sign test p: 0.001319
  Significant: YES
  Interpretation: formal=original → formal win = prefer ORIGINAL
    Formality effect and original preference are CONFOUNDED (same direction)

  --- casual→formal (n=22) ---
  formal wins: 12/22 (54.5%)
  casual wins: 10/22
  95% CI (Wilson): [0.3466, 0.7308]
  Sign test p: 0.831812
  Significant: NO
  Interpretation: casual=original → formal win = prefer REWRITE
    Formality effect and original preference are OPPOSING
    This subset cleanly isolates formality effect from original preference

======================================================================
  Logistic Regression Decomposition (formality)
======================================================================
  Observations: 196 (2 trials × 98 records)
  DV: chose_position_A (1/0)
  IV1: is_formal_in_A (formality effect)
  IV2: is_original_in_A (original preference)

  Intercept (position A bias): -0.5851

  formal_effect:
    Coefficient: 0.7928 (SE=0.3117)
    95% CI (bootstrap): [0.2029, 1.4304]
    Odds ratio: 2.2095
    z=2.5434, p=0.010979
    Significant: YES

  original_effect:
    Coefficient: 0.5958 (SE=0.3012)
    95% CI (bootstrap): [0.0135, 1.1914]
    Odds ratio: 1.8145
    z=1.9781, p=0.047914
    Significant: YES
```

### 3. exp-011: NLI Threshold Sensitivity — 完整 console output

```
Loaded 100 pairwise records

Loaded 100 records from verified_32b.jsonl

================================================================================
  NLI Threshold Sensitivity — formality axis (n=100)
================================================================================
  Threshold    N pass     Pass%      NLI mean     BS mean      PW N     PW win%    PW p      
  ----------------------------------------------------------------------------
  0.70         89         89.0       0.9894       0.8799       47       72.3       0.0031    
  0.75         89         89.0       0.9894       0.8799       47       72.3       0.0031    
  0.80         89         89.0       0.9894       0.8799       47       72.3       0.0031    
  0.85         89         89.0       0.9894       0.8799       47       72.3       0.0031    
  0.90         88         88.0       0.9906       0.8798       46       73.9       0.0016    
  0.95         85         85.0       0.9925       0.8794       45       73.3       0.0025    

  NLI distribution: mean=0.8956, std=0.2792, min=0.0001, max=0.9990
  formal (n=59): NLI mean=0.8793
  casual (n=41): NLI mean=0.9190

Saved CSV to .../reanalysis_outputs/exp011_nli_sensitivity.csv
```

### 4. 生成的输出文件

| 文件 | 路径 |
|------|------|
| exp-011 CSV | `artifacts/reanalysis_outputs/exp011_nli_sensitivity.csv` |
| pairwise 数据 (下载) | `artifacts/reanalysis_outputs/pairwise_results_32b.jsonl` (100 records) |
| verified 数据 (下载) | `artifacts/reanalysis_outputs/verified_32b.jsonl` (100 records) |

注意：exp-012 和 exp-014 的脚本代码中接受 `--output-dir` 参数但**未实现 CSV 写入逻辑**，仅输出 console report。

### 5. 比对结论：之前报告的数字与实际执行结果对比

#### exp-012 — **完全一致 ✓**

| 指标 | 之前报告 | 实际执行 | 匹配 |
|------|---------|---------|------|
| Consistent n | 55 | 55 | ✓ |
| Inconsistent n | 43 | 43 | ✓ |
| NLI MWU p | 0.824367 | 0.824367 | ✓ |
| BERTScore MWU p | 0.120293 | 0.120293 | ✓ |

#### exp-014 — **完全一致 ✓**

| 指标 | 之前报告 | 实际执行 | 匹配 |
|------|---------|---------|------|
| formal_effect coef | 0.7928 | 0.7928 | ✓ |
| formal_effect OR | 2.2095 | 2.2095 | ✓ |
| formal_effect p | 0.010979 | 0.010979 | ✓ |
| original_effect coef | 0.5958 | 0.5958 | ✓ |
| original_effect OR | 1.8145 | 1.8145 | ✓ |
| original_effect p | 0.047914 | 0.047914 | ✓ |
| formal→casual win rate | 78.8% | 78.8% | ✓ |
| formal→casual p | 0.001319 | 0.001319 | ✓ |
| casual→formal win rate | 54.5% | 54.5% | ✓ |
| casual→formal p | 0.831812 | 0.831812 | ✓ |

#### exp-011 — **完全一致 ✓**

| 指标 | 之前报告 | 实际执行 | 匹配 |
|------|---------|---------|------|
| Pass rate @0.90 | 88% | 88.0% | ✓ |
| PW win rate @0.90 | 73.9% | 73.9% | ✓ |
| PW p @0.90 | 0.0016 | 0.0016 | ✓ |

### 总结

**所有三个实验的数字完全一致，无任何差异。** 之前 worker 确实执行了脚本并正确报告了结果，问题仅在于没有将输出文件保存到 artifacts 目录。现在数据文件和 exp-011 CSV 已保存在 `artifacts/reanalysis_outputs/`。exp-012 和 exp-014 的脚本需要补充 CSV 写入逻辑才能持久化输出。

---
