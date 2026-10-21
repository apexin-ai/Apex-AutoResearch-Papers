# ssh degeneracy filtering construction

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_degeneracy_filtering_construction_20260522T093014_result.json`
- **Structured JSON:** [`3c9ffe07979ba0f0186d.json`](../../sessions/3c/3c9ffe07979ba0f0186d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。三个数据集结果汇总（micro-F1，θ=0.5）：

```
Dataset    n_total  n_nondeg  n_deg(%)   Full Δ(pp)  NonDeg Δ(pp)  Deg Δ(pp)  Consistent
─────────────────────────────────────────────────────────────────────────────────────────
SciERC         551       473    78(14.2%)     +3.03        +3.36       0.00        Yes
CoNLL         3453      1179  2274(65.9%)     +2.70        +5.18       0.00        Yes
FewNERD      37648     30198  7450(19.8%)     +6.60        +7.08       0.00        Yes
```

详细 F1：
```
SciERC:   Greedy=0.6327  Constr=0.6630  (Full Δ=+3.03pp)
          NonDeg: Greedy=0.6094  Constr=0.6430  (Δ=+3.36pp)
          Deg:    Greedy=0.8305  Constr=0.8305  (Δ=0.00pp)

CoNLL:    Greedy=0.8822  Constr=0.9092  (Full Δ=+2.70pp)
          NonDeg: Greedy=0.7970  Constr=0.8488  (Δ=+5.18pp)
          Deg:    Greedy=0.9708  Constr=0.9708  (Δ=0.00pp)

FewNERD:  Greedy=0.7108  Constr=0.7768  (Full Δ=+6.60pp)
          NonDeg: Greedy=0.7010  Constr=0.7718  (Δ=+7.08pp)
          Deg:    Greedy=0.8415  Constr=0.8415  (Δ=0.00pp)
```

关键发现：

1. **Degenerate construction == greedy 完全一致**（三个数据集均 Yes）——验证了理论预期。

2. **非 degenerate 子集的 construction Δ 在所有 3 个数据集上都为正**，且大于全集 Δ：
   - SciERC: +3.36 > +3.03 (放大 +0.33pp)
   - CoNLL: +5.18 > +2.70 (放大 +2.48pp)
   - FewNERD: +7.08 > +6.60 (放大 +0.48pp)

3. **CoNLL 的 degeneracy 比例最高（65.9%）**，degenerate 稀释效应最显著——全集 +2.70pp 被稀释到远低于非 degenerate 子集的 +5.18pp。这解释了为什么 CoNLL 在之前的 macro-F1 分析中可能出现负 Δ（degenerate 的高 F1 baseline 拉低了 delta 的加权平均）。

4. 关于与任务描述中数字（+1.40, +0.32, -0.39）的差异：之前的 `entity_construction_fair_n8` 使用 **instance-level mean F1**（macro），本分析使用的是任务要求的 **micro-F1**。两种度量下，filtering 非 degenerate 的方向性结论一致。

---
