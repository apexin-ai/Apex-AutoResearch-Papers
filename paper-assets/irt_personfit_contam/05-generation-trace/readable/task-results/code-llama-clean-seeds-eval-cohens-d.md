# code llama clean seeds eval cohens d

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama-clean-seeds-eval-cohens-d_20260521T005713_result.json`
- **Structured JSON:** [`990832756565bb415e9e.json`](../../sessions/99/990832756565bb415e9e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

```
=== Llama n=3 Cohen's d (Snijders ℓz*) ===

| Condition  | seed | lz*     | acc    | θ      |
|------------|------|---------|--------|--------|
| clean      | 42   |  0.8446 | 0.5914 | -0.666 |
| clean_s2   | 123  | -0.1823 | 0.5954 | -0.630 |
| clean_s3   | 456  | -1.0844 | 0.5943 | -0.640 |
| contam_15  | 42   | -2.9922 | 0.6654 | -0.276 |
| contam_50  | 42   | -3.3313 | 0.6983 | -0.149 |

Baseline (n=3): mean=-0.1407, std=0.9652
Cohen's d (ddof=1): contam_15=-2.95, contam_50=-3.31

对比 Qwen: contam_15 d=-3.42, contam_50 d=-0.99
```

关键观察：
- Llama 两个 contamination 条件的 Cohen's d 都很大（|d|>2.9），效应极显著
- contam_50 的 |d| 在 Llama 上（3.31）远大于 Qwen（0.99），说明 Llama 对 50% 污染更敏感
- clean baseline 的 lz* 方差较大（std=0.97），3 个 seed 的 lz* 从 -1.08 到 +0.84 变化不小

---
