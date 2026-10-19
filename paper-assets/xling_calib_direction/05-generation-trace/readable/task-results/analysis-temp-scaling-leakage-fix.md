# analysis temp scaling leakage fix

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_temp_scaling_leakage_fix_20260520T201907_result.json`
- **Structured JSON:** [`de52296fe00e77c4b665.json`](../../sessions/de/de52296fe00e77c4b665.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果出来了。与之前有 leakage 的结果差异巨大。

```
=== Data Leakage Confirmation ===
问题: temp_scaling.py / temp_scaling_l27.py 在 test set 上优化 T 并在同一 test set 上报告 ECE
修复: 3-way split (60/20/20), T 在 val 上优化, ECE 在 test 上报告

=== Fixed Temperature Scaling Results ===
Split: train=8424, val=2809, test=2809

Layer | T     | AUROC  | ECE_orig | ECE_cal | P1
 0    | 0.77  | 0.6240 | 0.1683   | 0.1944  | FAIL
 4    | 0.78  | 0.6367 | 0.1795   | 0.2010  | FAIL
 8    | 0.76  | 0.6346 | 0.2101   | 0.2320  | FAIL
12    | 0.77  | 0.6113 | 0.2158   | 0.2357  | FAIL
16    | 0.76  | 0.6691 | 0.2282   | 0.2479  | FAIL
20    | 0.68  | 0.7227 | 0.2334   | 0.2505  | FAIL
24    | 0.67  | 0.7486 | 0.1982   | 0.2205  | FAIL
27    | 0.62  | 0.7541 | 0.1951   | 0.2216  | FAIL

Best layer for P1: L27, ECE_cal=0.2216 → FAIL

=== 对比 ===
             之前(leakage)    修复后(3-way split)
L24 T:       5.36             0.67
L24 ECE:     0.0888 (PASS)    0.2205 (FAIL)
L27 T:       6.21             0.62
L27 ECE:     0.0744 (PASS)    0.2216 (FAIL)
```

关键发现：

1. **P1 全部 FAIL** — 之前的 PASS 完全是 data leakage 导致的假象
2. **T 值方向反转** — 旧 T>5（过度自信需降温），新 T<1（欠自信需升温），说明旧 T 严重过拟合 test set
3. **Temperature scaling 反而恶化 ECE** — 所有层的 ECE_cal > ECE_orig，单参数 T 在 val→test 上不泛化
4. **AUROC 不受影响** — L27 仍为 0.7541（discrimination 能力不变，仅 calibration 评估失真）

---
