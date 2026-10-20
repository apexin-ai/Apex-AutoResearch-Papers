# analysis 355m 3seed full stats

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_355m_3seed_full_stats_20260514T125323_result.json`
- **Structured JSON:** [`deab141a07b0f1c543b9.json`](../../sessions/de/deab141a07b0f1c543b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

交叉验证全部匹配。以下是完整报告。

---

## 脚本完整输出（逐字）

```
============================================================
GPT2-medium (355M) 3-seed Analysis
============================================================
  OK    uncurated       seed=42: 8 gens (0-7) [all_results.json]
  OK    uncurated       seed=123: 8 gens (0-7) [all_results.json]
  OK    uncurated       seed=456: 8 gens (0-7) [all_results.json]
  OK    rgds            seed=42: 8 gens (0-7) [all_results.json]
  OK    rgds            seed=123: 8 gens (0-7) [all_results.json]
  OK    rgds            seed=456: 8 gens (0-7) [all_results.json]
  OK    external_only   seed=42: 8 gens (0-7) [all_results.json]
  OK    external_only   seed=123: 8 gens (0-7) [all_results.json]
  OK    external_only   seed=456: 8 gens (0-7) [all_results.json]
  OK    random_50       seed=42: 8 gens (0-7) [all_results.json]
  OK    random_50       seed=123: 8 gens (0-7) [all_results.json]
  OK    random_50       seed=456: 8 gens (0-7) [all_results.json]

============================================================
Gen7 Summary: mean +/- std (across seeds)
============================================================
Method          Seeds                    ppl                rankme                  rare
--------------------------------------------------------------------------------
uncurated       3/3s       85.57 +/-   6.95    437.90 +/-   5.39      0.01 +/-   0.00
rgds            3/3s       86.38 +/-   3.72    429.31 +/-   4.00      0.02 +/-   0.00
external_only   3/3s       80.10 +/-   2.67    425.99 +/-   4.21      0.02 +/-   0.00
random_50       3/3s       70.64 +/-   1.75    421.16 +/-   5.77      0.01 +/-   0.00

============================================================
PPL Trajectory (per gen, all seeds)
============================================================
Method              gen0     gen1     gen2     gen3     gen4     gen5     gen6     gen7
-------------------------------------------------------------------------------------
uncurated         26.4(3)   35.2(3)   47.7(3)   59.3(3)   67.9(3)   76.5(3)   82.5(3)   85.6(3)
rgds              26.1(3)   33.1(3)   42.2(3)   51.2(3)   59.3(3)   67.5(3)   75.8(3)   86.4(3)
external_only     26.2(3)   33.5(3)   43.1(3)   51.0(3)   60.3(3)   68.8(3)   75.6(3)   80.1(3)
random_50         26.2(3)   33.2(3)   42.2(3)   50.4(3)   57.9(3)   64.4(3)   71.3(3)   70.6(3)

============================================================
Paired t-tests (gen7, across seeds)
============================================================

  rgds_vs_uncurated -- C1: RGDS accelerates collapse
    ppl     : t=+0.161, p=0.8868 ns, d=+0.09, diff=+0.8077 (rgds>uncurated)
    rankme  : t=-1.587, p=0.2534 ns, d=-0.92, diff=-8.5938 (rgds&lt;uncurated)
    rare    : t=+4.360, p=0.0488 *, d=+2.52, diff=+0.0019 (rgds>uncurated)

  ext_vs_uncurated -- C2: external mitigates collapse
    ppl     : t=-0.985, p=0.4285 ns, d=-0.57, diff=-5.4718 (external_only&lt;uncurated)
    rankme  : t=-2.250, p=0.1534 ns, d=-1.30, diff=-11.9096 (external_only&lt;uncurated)
    rare    : t=+29.159, p=0.0012 **, d=+16.83, diff=+0.0025 (external_only>uncurated)

  rgds_vs_random50 -- C3: RGDS worse than random same-budget
    ppl     : t=+9.923, p=0.0100 *, d=+5.73, diff=+15.7361 (rgds>random_50)
    rankme  : t=+1.496, p=0.2733 ns, d=+0.86, diff=+8.1465 (rgds>random_50)
    rare    : t=+4.915, p=0.0390 *, d=+2.84, diff=+0.0027 (rgds>random_50)

  ext_vs_random50 -- C2: external vs random same-budget
    ppl     : t=+4.272, p=0.0507 ns, d=+2.47, diff=+9.4566 (external_only>random_50)
    rankme  : t=+0.960, p=0.4385 ns, d=+0.55, diff=+4.8307 (external_only>random_50)
    rare    : t=+16.296, p=0.0037 **, d=+9.41, diff=+0.0033 (external_only>random_50)

============================================================
Claim Verification Status
============================================================

  C1: Diversity ratio degrades across generations
    rgds seed=42: g0=0.976, g1=0.999, g2=0.922, g3=0.913, g4=0.799, g5=0.900, g6=0.762, g7=0.831
    rgds seed=123: g0=0.962, g1=0.889, g2=0.945, g3=0.847, g4=0.944, g5=0.900, g6=0.936, g7=0.873
    rgds seed=456: g0=0.923, g1=0.914, g2=0.919, g3=0.872, g4=0.954, g5=0.848, g6=0.893, g7=0.790

  C3: RGDS worse than Random-50 at same budget
    seed=42: rgds_ppl=82.84, random50_ppl=70.25, diff=+12.60 (RGDS worse)
    seed=123: rgds_ppl=90.25, random50_ppl=72.55, diff=+17.70 (RGDS worse)
    seed=456: rgds_ppl=86.03, random50_ppl=69.12, diff=+16.91 (RGDS worse)

CSV written: /root/div_cal_verify/artifacts/355m_3seed_ttest.csv (12 rows)

Data coverage: 12/12 method-seed combos loaded
```

## 交叉验证

| 验证项 | metrics.json 原值 | 脚本使用值 | 匹配 |
|--------|-------------------|-----------|------|
| rgds s456 gen7 PPL | 86.0349... | 86.03 | ✓ |
| random50 s456 gen7 PPL | 69.1228... | 69.12 | ✓ |
| uncurated s123 gen7 PPL | 87.0507... | (mean 85.57 包含此值) | ✓ |

## 一句话总结

**显著的比较：** RGDS vs Random50 的 PPL (p=0.0100\*) 和 rare (p=0.0390\*) 显著，确认 C3（RGDS 比同预算随机选择更差）；ext vs uncurated 的 rare (p=0.0012\*\*) 和 ext vs random50 的 rare (p=0.0037\*\*) 显著。

**不显著：** RGDS vs Uncurated 的 PPL (p=0.8868) 完全不显著——Uncurated 自身方差太大 (SD=6.95) 吞掉了差异；ext vs uncurated 的 PPL (p=0.4285) 同理；ext vs random50 的 PPL (p=0.0507) 刚好卡在边界未达显著（95% CI 包含 0）。

---
