# check urgent exp009 exp010 20h

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_urgent-exp009-exp010-20h_20260519T115030_result.json`
- **Structured JSON:** [`f1eab35751718ac9d271.json`](../../sessions/f1/f1eab35751718ac9d271.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### 1. 进程状态
| 实验 | PID | 状态 |
|------|-----|------|
| exp_009 (r=0.25, cuda:0) | 247492 | **存活** |
| exp_010 (pure, cuda:1) | 283142 | **存活** |

### 2. GPU 状态
| GPU | 利用率 | 显存 |
|-----|--------|------|
| cuda:0 | 96% | 25017 / 97887 MiB |
| cuda:1 | 89% | 25017 / 97887 MiB |

### 3. exp_009: fixed_mix r=0.25 seed42 — **8/10 代完成，正在训练 Gen 8**

| Gen | raw_SLV | EMA_SLV | eff_rank | ppl | d4 |
|-----|---------|---------|----------|-----|-----|
| 0 | 2366.68 | 2366.68 | 417.55 | 9.554 | 0.7414 |
| 1 | 2362.13 | 2364.41 | 476.66 | 10.239 | 0.6499 |
| 2 | 2363.10 | 2363.76 | 482.84 | 10.653 | 0.4973 |
| 3 | 2380.88 | 2372.32 | 489.47 | 11.019 | 0.4419 |
| 4 | 2393.37 | 2382.84 | 491.21 | 11.343 | 0.4298 |
| 5 | 2421.22 | 2402.03 | 495.84 | 11.669 | 0.4192 |
| 6 | 2436.38 | 2419.20 | 498.59 | 11.974 | 0.3969 |
| 7 | 2447.08 | 2433.14 | 500.66 | 12.295 | 0.3889 |

- **EMA violations (2):** Gen 1 (-2.27), Gen 2 (-0.65) — 仅初始小幅抖动，Gen 3 起严格单调递增
- SLV 从 2366→2447 (+3.4%)，eff_rank 从 417→500 (+19.9%)
- 日志尾部：Step 2000-2400，loss ~1.31（Gen 8 训练中）

### 4. exp_010: pure_collapse seed43 — **3/10 代完成，正在训练 Gen 3**

| Gen | raw_SLV | EMA_SLV | eff_rank | ppl | d4 |
|-----|---------|---------|----------|-----|-----|
| 0 | 2366.68 | 2366.68 | 417.55 | 9.554 | 0.7415 |
| 1 | 2462.62 | 2414.65 | 490.83 | 11.371 | 0.5997 |
| 2 | 2466.63 | 2440.64 | 496.24 | 13.565 | 0.5048 |

- **EMA: 严格单调递增，无 violations**
- Pure collapse 速度明显更快：仅 2 代 SLV 就从 2366→2466 (+4.2%)，vs fixed_mix 7 代才到 2447
- ppl 飙升也更剧烈：9.55→13.57（+42%），d4 下降到 0.50
- 日志尾部：padding_side warning（生成阶段中，Gen 3 数据合成）

### 关键观察

exp_010 (pure) 进度慢（才 3/10 代）但每代 collapse 更猛烈；exp_009 (r=0.25) 已接近完成（8/10），collapse 被 25% 真实数据显著减缓。两个实验都在正常运行。

---
