# ssh check exp progress 0519

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-exp-progress-0519_20260519T200335_result.json`
- **Structured JSON:** [`7545d5cd35a8bd44fcc7.json`](../../sessions/75/7545d5cd35a8bd44fcc7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练进度报告

### 状态总览

| 实验 | PID | 运行时间 | GPU | GPU利用率 | 已完成Gen | 当前状态 |
|------|-----|---------|-----|----------|----------|---------|
| exp_010 (pure collapse seed43) | 283142 | 14h11m | cuda:1 | 92% | Gen 0-5 | 生成 Gen6 数据 (28480/50000) |
| exp_011 (r=0.2 resume) | 319889 | 3h46m | cuda:0 | 95% | Gen 0-6 | 生成 Gen7 数据 (37760/40000) |

---

### exp_010 — Pure Collapse (seed43, r=0.0)

```
Gen | raw SLV  | EMA SLV  | Δ_t
0   | 2366.68  | 2366.68  | ---
1   | 2462.62  | 2414.65  | -0.020268
2   | 2466.63  | 2440.64  | -0.010981
3   | 2438.38  | 2439.51  | +0.000478
4   | 2404.60  | 2422.05  | +0.007375
5   | 2365.13  | 2393.59  | +0.012024
```

- Raw SLV 在 Gen2 达峰 2466.63 后持续下降，Gen5 已回落至 2365.13（低于 Gen0 基线 2366.68）
- EMA 从 Gen3 开始单调递减，collapse 信号明确
- **max Δ_t = +0.012024 (Gen5)**，collapse 正在加速

---

### exp_011 — Fixed Mix r=0.2 (seed42)

```
Gen | raw SLV  | EMA SLV  | Δ_t
0   | 2366.68  | 2366.68  | ---
1   | 2367.46  | 2367.07  | -0.000164
2   | 2358.31  | 2362.69  | +0.001852
3   | 2362.52  | 2362.61  | +0.000035
4   | 2379.19  | 2370.90  | -0.003504
5   | 2398.93  | 2384.92  | -0.005923
6   | 2429.83  | 2407.37  | -0.009488
```

- **EMA 非递减起点：Gen 4**（S̃_3=2362.61 → S̃_4=2370.90 → S̃_5=2384.92 → S̃_6=2407.37，连续 3 代递增）
- Raw SLV 从 Gen2 低谷 2358.31 开始恢复，Gen6 达 2429.83（+2.67% above baseline）
- **max Δ_t = +0.001852 (Gen2)**，controller signal 极弱，r=0.2 下 SLV 没有实质性下降
- 与 exp_010 对比：r=0.0 的 max Δ_t（+0.012）是 r=0.2 的 ~6.5 倍，符合 §4.5 Type II "controller silence" 结论

---

两个实验都在正常跑，无需干预。exp_010 还差 ~4 gen 完成全部 10 gen，预计 ~10h；exp_011 还差 ~3 gen，预计 ~5h。

---
