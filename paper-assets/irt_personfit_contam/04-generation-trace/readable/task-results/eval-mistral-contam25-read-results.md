# eval mistral contam25 read results

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_mistral-contam25-read-results_20260524T063910_result.json`
- **Structured JSON:** [`84294bae804961d64355.json`](../../sessions/84/84294bae804961d64355.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here are the complete contam_25 Mistral results:

## contam_25 完整指标

| Metric | Value |
|--------|-------|
| n_seen | 3,510 |
| n_unseen | 10,532 |
| θ_MLE | -0.544 |
| **Accuracy** | overall: 0.620, seen: 0.754, unseen: 0.575 |
| **lz\* free** | overall: **-3.066**, seen: -1.866, unseen: -0.865 |
| **lz\* fixed** | **-7.276** |

### Cohen's d

| θ mode | point | 95% CI |
|--------|-------|--------|
| free (baseline: μ=4.024, σ=2.052) | **3.46** | — |
| fixed (baseline: μ=3.291, σ=2.522) | **4.19** | [2.66, 13.64] |

## 更新后的剂量表

| 条件 | lz\*_fixed | Cohen's d (fixed) | 95% CI |
|------|-----------|-----------|--------|
| contam_5 | -6.64 | 3.94 | [2.47, 12.93] |
| contam_15 | -3.48 | 2.69 | [1.53, 9.06] |
| **contam_25** | **-7.28** | **4.19** | **[2.66, 13.64]** |
| contam_50 | -11.33 | 5.80 | [3.87, 18.45] |

注意 contam_15 → contam_25 存在跳跃（d 从 2.69 升到 4.19），剂量-效应关系非严格单调（contam_5 的 d=3.94 反而高于 contam_15 的 2.69）。

---
