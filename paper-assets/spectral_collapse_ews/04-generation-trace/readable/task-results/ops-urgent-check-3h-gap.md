# ops urgent check 3h gap

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent-check-3h-gap_20260518T192240_result.json`
- **Structured JSON:** [`0db1a900b8699ed7b7a1.json`](../../sessions/0d/0db1a900b8699ed7b7a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### 1. exp_007 (r=0.2) — **ALIVE**
- PID 188503，正在 **Gen 5 fine-tuning**（step 1900+），GPU 0 占用 25017 MiB / 96%
- 已完成 5 个 gen（gen0-gen4）:

| Gen | log_det | eff_rank | ppl | d4 |
|-----|---------|----------|-----|----|
| 0 | 2366.7 | 417.5 | 9.554 | 0.741 |
| 1 | 2367.5 | 476.7 | 10.282 | 0.674 |
| 2 | 2358.3 | 481.6 | 10.741 | 0.498 |
| 3 | 2362.5 | 486.5 | 11.137 | 0.467 |
| **4** | **2379.2** | **490.3** | **11.512** | **0.451** |

log_det 在 gen2 短暂下降后反弹至 gen4=2379.2（超过 gen0 基线）。ppl 持续上升，d4 持续下降。

### 2. exp_008 (r=0.3) — **ALIVE**
- PID 194377，正在 **Gen 5 样本生成**（26240/35000），GPU 1 占用 25017 MiB / 94%
- 已完成 5 个 gen（gen0-gen4），目标 10 gen:

| Gen | log_det | eff_rank | ppl | d4 |
|-----|---------|----------|-----|----|
| 0 | 2366.7 | 417.5 | 9.554 | 0.741 |
| 1 | 2366.1 | 476.9 | 10.193 | 0.689 |
| 2 | 2372.4 | 484.2 | 10.589 | 0.489 |
| 3 | 2386.7 | 489.5 | 10.901 | 0.465 |
| **4** | **2404.0** | **492.6** | **11.226** | **0.468** |

log_det 强劲上升趋势（+37.3 over 4 gens），与 r=0.2 对比更明显。d4 在 gen4 微反弹。

### 3. r=0.25 启动 — **未执行**

两块 GPU 均满载，exp_007 仍在运行。等 exp_007 完成后（预计 Gen 5 fine-tuning 还需 ~1-2 小时）才能释放 cuda:0 启动 r=0.25。

---
