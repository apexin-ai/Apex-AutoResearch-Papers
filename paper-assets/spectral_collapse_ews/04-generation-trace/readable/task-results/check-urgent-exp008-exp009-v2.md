# check urgent exp008 exp009 v2

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_urgent-exp008-exp009-v2_20260519T031646_result.json`
- **Structured JSON:** [`83db7873b1353b22edaf.json`](../../sessions/83/83db7873b1353b22edaf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### GPU 状态
| GPU | Utilization | Memory Used / Total |
|-----|------------|---------------------|
| 0 | 75% | 25017 / 97887 MiB |
| 1 | 87% | 25017 / 97887 MiB |

---

### exp_008 (r=0.3, cuda:1, pid=194372) — 运行中，Gen 9 采样阶段

进程存活。已完成 Gen 0-8（9 条记录），当前正在 Gen 9 采样（30720/35000 samples）。

| Gen | log_det | eff_rank | ppl | distinct4 |
|-----|---------|----------|-------|-----------|
| 0 | 2366.68 | 417.55 | 9.554 | 0.7414 |
| 1 | 2366.13 | 476.91 | 10.193 | 0.6894 |
| 2 | 2372.45 | 484.17 | 10.589 | 0.4892 |
| 3 | 2386.72 | 489.48 | 10.901 | 0.4646 |
| 4 | 2404.02 | 492.59 | 11.226 | 0.4682 |
| 5 | 2431.17 | 497.86 | 11.544 | 0.4508 |
| 6 | 2452.00 | 501.63 | 11.875 | 0.4176 |
| 7 | 2467.05 | 506.30 | 12.215 | 0.3964 |
| 8 | 2485.91 | 511.71 | 12.610 | 0.4058 |

趋势：log_det 单调上升（2366→2486），eff_rank 单调上升（417→512），ppl 单调上升（9.5→12.6），distinct4 大幅下降后趋稳（0.74→0.41）。Gen 9 采样完成后还需训练+评估，预计再完成 Gen 9 和 Gen 10 后结束。**exp_008 尚未完成，正在跑 Gen 9 的采样阶段。**

---

### exp_009 (r=0.25, cuda:0, pid=247492) — 运行中，Gen 4 采样阶段

进程存活。已完成 Gen 0-3（4 条记录），当前正在 Gen 4 采样（31360/37500 samples）。

| Gen | log_det | eff_rank | ppl | distinct4 |
|-----|---------|----------|-------|-----------|
| 0 | 2366.68 | 417.55 | 9.554 | 0.7414 |
| 1 | 2362.13 | 476.66 | 10.239 | 0.6499 |
| 2 | 2363.10 | 482.84 | 10.653 | 0.4973 |
| 3 | 2380.88 | 489.47 | 11.019 | 0.4419 |

趋势与 exp_008 类似但更缓（real_ratio 更高）。log_det 前两代几乎持平后缓升，符合 r=0.25 更多真实数据稀释的预期。还需完成 Gen 4-10，距完成较远。

---
