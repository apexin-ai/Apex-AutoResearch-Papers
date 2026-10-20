# check exp009 exp010 progress

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp009-exp010-progress_20260519T103016_result.json`
- **Structured JSON:** [`3a85cbc3a9f74b52407d.json`](../../sessions/3a/3a85cbc3a9f74b52407d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### exp_009 — r=0.25, cuda:0, pid=247492
**进程存活** ✓ — 正在生成 Gen 8 数据 (9600/37500 samples)

已完成 8 代 (Gen 0-7)：

| Gen | log_det | eff_rank | ppl | distinct4 |
|-----|---------|----------|-------|----------|
| 0 | 2366.68 | 417.55 | 9.554 | 0.7414 |
| 1 | 2362.13 | 476.66 | 10.239 | 0.6499 |
| 2 | 2363.10 | 482.84 | 10.653 | 0.4973 |
| 3 | 2380.88 | 489.47 | 11.019 | 0.4419 |
| 4 | 2393.37 | 491.21 | 11.343 | 0.4298 |
| 5 | 2421.22 | 495.84 | 11.669 | 0.4192 |
| 6 | 2436.38 | 498.59 | 11.974 | 0.3969 |
| 7 | 2447.08 | 500.66 | 12.295 | 0.3889 |

趋势：log_det 持续上升 (+80.4, Gen 0→7)，eff_rank 从 417→501，ppl 缓慢恶化 9.55→12.30，d4 从 0.74 降至 0.39。controller_ratio 始终锁定在 0.25。

---

### exp_010 — pure collapse seed43, cuda:1, pid=283142
**进程存活** ✓ — 正在生成 Gen 2 数据 (46400/50000 samples，即将完成)

已完成 2 代 (Gen 0-1)：

| Gen | log_det | eff_rank | ppl | distinct4 |
|-----|---------|----------|-------|----------|
| 0 | 2366.68 | 417.55 | 9.554 | 0.7415 |
| 1 | 2462.62 | 490.83 | 11.371 | 0.5997 |

纯合成训练 1 代后 log_det 已飙升 +95.9（比 exp_009 同期的 -4.5 剧烈得多），eff_rank 一步从 417→491，ppl 跳至 11.37，d4 降至 0.60。mix_ratio=0.0 确认无真实数据混入。

---

### GPU 状态

| GPU | Util | Memory |
|-----|------|--------|
| 0 | 93% | 25017 / 97887 MiB |
| 1 | 92% | 25017 / 97887 MiB |

两卡均满负荷运行。exp_009 还差 Gen 8, 9 两代；exp_010 还差 Gen 2-9 共 8 代，预计耗时较长。

---
