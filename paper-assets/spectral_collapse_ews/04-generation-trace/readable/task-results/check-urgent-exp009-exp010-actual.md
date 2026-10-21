# check urgent exp009 exp010 actual

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_urgent-exp009-exp010-actual_20260519T114841_result.json`
- **Structured JSON:** [`6f796c1bc62fb465f30b.json`](../../sessions/6f/6f796c1bc62fb465f30b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

---

## exp_009 (r=0.25, fixed_mix, cuda:0) — 进行中

**进程**: PID 247492 存活，正在训练 Gen 8（Step 2000，loss ~1.31）

**已完成 8/11 条记录 (Gen 0-7)**:

| Gen | log_det | eff_rank | ppl | distinct_4 |
|-----|---------|----------|-----|------------|
| 0 | 2366.68 | 417.55 | 9.554 | 0.7414 |
| 1 | 2362.13 | 476.66 | 10.239 | 0.6499 |
| 2 | 2363.10 | 482.84 | 10.653 | 0.4973 |
| 3 | 2380.88 | 489.47 | 11.019 | 0.4419 |
| 4 | 2393.37 | 491.21 | 11.343 | 0.4298 |
| 5 | 2421.22 | 495.84 | 11.669 | 0.4192 |
| 6 | 2436.38 | 498.59 | 11.974 | 0.3969 |
| 7 | 2447.08 | 500.66 | 12.295 | 0.3889 |

趋势：log_det 从 Gen 1 起单调递增（2362→2447），eff_rank 持续上升（417→501），ppl 持续恶化（9.5→12.3），d4 持续下降（0.74→0.39）。尚未完成 10 gen，EMA 计算待完成后执行。

---

## exp_010 (pure collapse, seed43, cuda:1) — 进行中

**进程**: PID 283142 存活，正在 Gen 3 的样本生成阶段（17600/50000 samples）

**已完成 3/11 条记录 (Gen 0-2)**:

| Gen | log_det | eff_rank | ppl | distinct_4 |
|-----|---------|----------|-----|------------|
| 0 | 2366.68 | 417.55 | 9.554 | 0.7415 |
| 1 | 2462.62 | 490.83 | 11.371 | 0.5997 |
| 2 | 2466.63 | 496.24 | 13.565 | 0.5048 |

趋势：pure collapse 恶化速度远快于 fixed_mix。Gen 1 单步 log_det 跳升 +95.94（对比 exp_009 的 Gen 1 仅 -4.55）。ppl 到 Gen 2 已达 13.57（exp_009 到 Gen 7 才 12.30）。

---

## GPU 状态

| GPU | 利用率 | 显存使用 | 总显存 |
|-----|--------|---------|--------|
| 0 | 97% | 25017 MiB | 97887 MiB |
| 1 | 94% | 25017 MiB | 97887 MiB |

两块 GPU 均满载运行，exp_009 预计还需 ~2-3 gen 完成（约数小时），exp_010 还需 ~7 gen（明显更久）。

---
