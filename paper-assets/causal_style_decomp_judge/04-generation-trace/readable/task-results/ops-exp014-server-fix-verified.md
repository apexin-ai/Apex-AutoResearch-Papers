# ops exp014 server fix verified

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp014_server_fix_verified_20260521T001036_result.json`
- **Structured JSON:** [`faf9bf60f9f52ceede05.json`](../../sessions/fa/faf9bf60f9f52ceede05.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Step 7 完整输出：**

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
  No text length data available (need --verified-file)

  --- Position Bias ---
  Consistent (n=55): Trial1 A rate=69.1%, Trial2 A rate=30.9%
  Inconsistent (n=43): Trial1 A rate=55.8%, Trial2 A rate=55.8%

  --- Interpretation ---
  ✓ No significant systematic bias detected in consistency filter
```

---

## 最终确认

| 项目 | 状态 |
|------|------|
| CSV 文件存在 | `/root/.../artifacts/reanalysis_outputs/exp014_logistic_decomposition.csv` — **978 bytes** |
| 6 行数据 | 2 direction_subset + 2 pair_bootstrap + 2 gee |
| exp-012 | 成功执行，无报错 |

### 关键数字总结

**exp-014 Logistic Decomposition (n=98 pairs, 196 obs)：**

| 效应 | 方法 | OR | 95% CI | p |
|------|------|----|--------|---|
| **formal_effect** | Pair-bootstrap | **2.2095** | [1.2280, 4.3053] | **0.0121** ✓ |
| **formal_effect** | GEE | **2.2103** | [1.2100, 4.0377] | **0.0099** ✓ |
| original_effect | Pair-bootstrap | 1.8145 | [0.9757, 3.3693] | 0.0643 |
| original_effect | GEE | 1.8172 | [0.9948, 3.3194] | 0.0520 |

两种方法高度一致。formality effect 显著 (p<0.05)，original preference 边缘不显著。Pair-level bootstrap 和 GEE 的 OR 几乎相同（2.21），验证了修复的正确性。

---
