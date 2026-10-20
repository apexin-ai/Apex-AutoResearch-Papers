# analysis gemma27b bootstrap read

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gemma27b_bootstrap_read_20260524T091035_result.json`
- **Structured JSON:** [`a9a8918a8de87462cb01.json`](../../sessions/a9/a9a8918a8de87462cb01.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整结果如下。

## Gemma-2-27B Bootstrap CI 结果

### Self-scorer (Gemma-2-27B scores itself)

| Pair | AUC | 95% CI | Perm p | Boot std |
|------|-----|--------|--------|----------|
| 0v1 | 0.9695 | [0.9666, 0.9721] | 0.0001 | 0.0014 |
| 1v2 | 0.6196 | [0.6096, 0.6296] | 0.0001 | 0.0051 |
| 2v3 | 0.5388 | [0.5279, 0.5490] | 0.0001 | 0.0054 |
| 3v4 | 0.5069 | [0.4959, 0.5172] | 0.1099 | 0.0055 |
| 4v5 | 0.5124 | [0.5012, 0.5234] | 0.0147 | 0.0056 |

**K\* = 2** (max depth with AUC > 0.60)

### Cross-scorer (Qwen2.5-1.5B-Instruct scores Gemma-27B text)

| Pair | AUC | 95% CI | Perm p | Boot std |
|------|-----|--------|--------|----------|
| 0v1 | 0.8871 | [0.8811, 0.8930] | 0.0001 | 0.0030 |
| 1v2 | 0.5895 | [0.5795, 0.5997] | 0.0001 | 0.0052 |
| 2v3 | 0.5150 | [0.5045, 0.5254] | 0.0027 | 0.0054 |
| 3v4 | 0.5061 | [0.4952, 0.5165] | 0.1346 | 0.0054 |
| 4v5 | 0.5108 | [0.4998, 0.5218] | 0.0282 | 0.0056 |

**K\* = 1** (cross-scorer: 1v2 AUC=0.5895 < 0.60)

### Cross-scorer JSD

| Pair | JSD |
|------|-----|
| 0v1 | 0.0643 |
| 1v2 | 0.0106 |
| 2v3 | 0.0049 |
| 3v4 | 0.0042 |
| 4v5 | 0.0031 |

### 关键发现

- **Self-scorer K\*=2**：1v2 CI 下界 0.6096 > 0.60，2v3 CI 上界 0.5490 < 0.60，所以 K\*=2 稳定。
- **Cross-scorer K\*=1**：1v2 AUC=0.5895，CI=[0.5795, 0.5997]，上界不到 0.60，属于 borderline（自身判 K\*=2 但 cross 判 K\*=1）。
- 3v4 在两种 scorer 下 perm_p 都不显著（>0.10），CI 跨 0.50，确认 depth 3+ 不可区分。
- Bootstrap 参数：10000 bootstrap + 10000 permutation，seed=42。

---
