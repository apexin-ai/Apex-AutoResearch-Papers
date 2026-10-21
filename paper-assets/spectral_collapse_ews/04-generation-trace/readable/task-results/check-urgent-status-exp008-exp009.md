# check urgent status exp008 exp009

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_urgent-status-exp008-exp009_20260519T003945_result.json`
- **Structured JSON:** [`2b8e0da9615cfe11aa87.json`](../../sessions/2b/2b8e0da9615cfe11aa87.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态检查结果

---

### 1. exp_008 (r=0.3, cuda:1, pid=194372) — **存活，正在跑 Gen 8 数据生成**

**进程**: 存活，pid=194372 (wrapper bash), 实际 python pid=194377 在 GPU 1 上运行

**Results JSON: 8 条 generation 记录 (Gen 0–7)**

| Gen | log_det | eff_rank | ppl | distinct4 |
|-----|---------|----------|-----|-----------|
| 0 | 2366.68 | 417.55 | 9.554 | 0.7414 |
| 1 | 2366.13 | 476.91 | 10.193 | 0.6894 |
| 2 | 2372.45 | 484.17 | 10.589 | 0.4892 |
| 3 | 2386.72 | 489.48 | 10.901 | 0.4646 |
| 4 | 2404.02 | 492.59 | 11.226 | 0.4683 |
| 5 | 2431.17 | 497.86 | 11.544 | 0.4508 |
| 6 | 2452.00 | 501.63 | 11.875 | 0.4176 |
| 7 | 2467.05 | 506.30 | 12.215 | 0.3964 |

**日志**: 正在 Gen 8 数据生成，进度 14720/35000 samples

---

### 2. exp_009 (r=0.25, cuda:0, pid=247492) — **存活，正在跑 Gen 3 数据生成**

**进程**: 存活，pid=247492 (wrapper bash), 实际 python pid=247497 在 GPU 0 上运行

**Results JSON: 3 条 generation 记录 (Gen 0–2)**

| Gen | log_det | eff_rank | ppl | distinct4 |
|-----|---------|----------|-----|-----------|
| 0 | 2366.68 | 417.55 | 9.554 | 0.7414 |
| 1 | 2362.13 | 476.66 | 10.239 | 0.6499 |
| 2 | 2363.10 | 482.84 | 10.653 | 0.4973 |

**日志**: 正在 Gen 3 数据生成，进度 17600/37500 samples

---

### 3. GPU 状态

| GPU | 型号 | 显存占用 | 利用率 | 温度 | 功耗 |
|-----|------|---------|--------|------|------|
| 0 | RTX PRO 6000 | 25017/97887 MiB | 89% | 59°C | 268W/600W |
| 1 | RTX PRO 6000 | 25017/97887 MiB | 93% | 59°C | 302W/600W |

---

### 关键观察

**exp_008 (r=0.3)**: log_det 从 2366→2467 单调上升 (+100.4 over 7 gens), eff_rank 417→506 单调上升, ppl 9.55→12.22 持续恶化, distinct4 0.74→0.40 持续下降。控制器固定 r=0.3 未触发（符合预期 fixed_mix 模式）。Gen 8 正在生成中，预计还需若干小时完成 10 代。

**exp_009 (r=0.25)**: 只完成 2 代训练（Gen 0 是 baseline）。log_det 从 2366.68 → 2362.13 → 2363.10，前两代几乎持平甚至微降。distinct4 下降较快 0.74→0.50。今天凌晨 03:47 启动，进度较慢（Gen 3 数据生成 47%）。

---
