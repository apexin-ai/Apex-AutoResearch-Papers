# monitor phase1 r5 urgent check

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_phase1-r5-urgent-check_20260513T214846_result.json`
- **Structured JSON:** [`2d4a07336edc5159807f.json`](../../sessions/2d/2d4a07336edc5159807f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态：完成 ✓

### 进程/GPU 状态
- 两个进程均已退出（EXIT_CODE=0）
- GPU 0 & 1: 利用率 0%, 显存 0 MiB / 97887 MiB（已完全释放）

### 训练进度
- exec-only: **100/100 steps** completed (15m43s, 9.44s/it)
- exec-sta: **100/100 steps** completed (16m53s, 10.13s/it)

### 指标总结

| 指标 | exec-only | exec-sta | Δ |
|------|-----------|----------|---|
| overall prove_rate | 0.15125 | 0.10000 | +0.051 |
| overall isr_mean | 0.14750 | 0.04347 | +0.104 |
| overall reward_mean | 0.15125 | 0.07174 | +0.080 |
| last-20 prove_rate MA | 0.20000 | 0.15000 | +0.050 |
| last-20 isr_mean MA | 0.20000 | 0.04956 | +0.150 |
| last-20 reward_mean MA | 0.20000 | 0.09978 | +0.100 |
| first-20 prove_rate MA | 0.11875 | 0.08125 | +0.038 |
| first-20 isr_mean MA | 0.11875 | 0.05182 | +0.067 |

### ISR 解耦验证

**exec-only: isr_mean ≡ prove_rate（完全相等）**
- 所有 100 步中 isr_mean = prove_rate，无一例外
- 这是预期行为：二值 ISR = 1 if proved else 0，所以均值 = prove_rate
- reward_mean 也等于 isr_mean（reward = binary ISR）

**exec-sta: isr_mean << prove_rate（显著解耦）**
- overall: isr/pr = 0.043/0.100 = **43%**（proved 的定理平均 ISR 仅 0.43）
- last-20: isr/pr = 0.050/0.150 = **33%**（后期更差）
- 典型例子：step 86 pr=0.50 但 isr=0.111；step 85 pr=0.25 但 isr=0.051

### prove_rate 趋势
- exec-only: 0.119 → 0.200（**↑68%**）— 有明显上升
- exec-sta: 0.081 → 0.150（**↑85%**）— 上升幅度更大

### Reward Hacking 信号

**关键发现：exec-sta 的 ISR 在 prove_rate 上升时保持平坦甚至下降。**

| 区间 | exec-sta prove_rate | exec-sta isr_mean | ISR/PR 比值 |
|------|--------------------|--------------------|-------------|
| first-20 | 0.081 | 0.052 | 64% |
| last-20 | 0.150 | 0.050 | 33% |

prove_rate 翻了近一倍（+85%），但 ISR 几乎没变（-4%）。这说明模型学会了 prove 更多定理，但新 prove 的定理 formalization 质量更差。ISR/PR 比从 64% 降到 33%。

exec-only 无法检测这种退化——它的 ISR ≡ prove_rate，任何 proof 都得满分。

### MVP 判定

**ISR 解耦信号已验证。** 核心实验假设成立：
1. ✅ continuous ISR ≠ prove_rate（exec-sta 中 ISR 仅为 prove_rate 的 33-43%）
2. ✅ binary ISR = prove_rate（exec-only 中完全重合，无法区分质量）
3. ✅ prove_rate↑ 而 ISR→（exec-sta 的 ISR 在训练中不随 prove_rate 提升）
4. ✅ 这暗示 reward hacking 风险：如果只用 binary prove/not-prove 做 reward，模型会倾向 tautological shortcuts

**局限**：整体指标水平偏低（prove_rate 10-20%），方差大（batch_size=8 导致逐步波动剧烈），100 步可能不足以观察到更稳定的趋势。

### 原始数据（最后 20 步逐步数据）

**exec-only:**
```
step  pr     isr      rw
81   0.125  0.12500  0.12500
82   0.125  0.12500  0.12500
83   0.125  0.12500  0.12500
84   0.250  0.25000  0.25000
85   0.125  0.12500  0.12500
86   0.500  0.50000  0.50000
87   0.500  0.50000  0.50000
88   0.000  0.00000  0.00000
89   0.250  0.25000  0.25000
90   0.000  0.00000  0.00000
91   0.500  0.50000  0.50000
92   0.250  0.25000  0.25000
93   0.000  0.00000  0.00000
94   0.000  0.00000  0.00000
95   0.000  0.00000  0.00000
96   0.250  0.25000  0.25000
97   0.375  0.37500  0.37500
98   0.000  0.00000  0.00000
99   0.250  0.25000  0.25000
100  0.375  0.37500  0.37500
```

**exec-sta:**
```
step  pr     isr      rw
81   0.000  0.00000  0.00000
82   0.125  0.01562  0.07031
83   0.125  0.10000  0.11250
84   0.250  0.11806  0.18403
85   0.250  0.05134  0.15067
86   0.500  0.11111  0.30556
87   0.250  0.03125  0.14062
88   0.000  0.00000  0.00000
89   0.500  0.20714  0.35357
90   0.000  0.00000  0.00000
91   0.375  0.11688  0.24594
92   0.000  0.00000  0.00000
93   0.000  0.00000  0.00000
94   0.125  0.06250  0.09375
95   0.000  0.00000  0.00000
96   0.250  0.09402  0.17201
97   0.250  0.08333  0.16667
98   0.000  0.00000  0.00000
99   0.000  0.00000  0.00000
100  0.000  0.00000  0.00000
```

---
