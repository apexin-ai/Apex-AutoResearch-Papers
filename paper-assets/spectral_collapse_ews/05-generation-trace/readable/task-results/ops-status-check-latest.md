# ops status check latest

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_status-check-latest_20260518T192858_result.json`
- **Structured JSON:** [`4663f8c68a690864bd64.json`](../../sessions/46/4663f8c68a690864bd64.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

### exp_007 (r=0.2) — 5 entries (gen0-4), PID 188503 ALIVE (uptime 10h38m)

| gen | eff_rank | log_det | ppl | d4 | loss | sv1 |
|-----|----------|---------|------|--------|--------|-------|
| 0 | 417.5 | 2366.7 | 9.554 | 0.7414 | - | 1942.8 |
| 1 | 476.7 | 2367.5 | 10.282 | 0.6737 | 1.7653 | 960.9 |
| 2 | 481.6 | 2358.3 | 10.741 | 0.4978 | 1.6709 | 882.0 |
| 3 | 486.5 | 2362.5 | 11.137 | 0.4665 | 1.4208 | 806.1 |
| 4 | 490.3 | 2379.2 | 11.512 | 0.4515 | 1.3255 | 760.2 |

### exp_008 (r=0.3) — 5 entries (gen0-4), PID 194372 ALIVE (uptime 9h11m)

| gen | eff_rank | log_det | ppl | d4 | loss | sv1 |
|-----|----------|---------|------|--------|--------|-------|
| 0 | 417.5 | 2366.7 | 9.554 | 0.7414 | - | 1942.8 |
| 1 | 476.9 | 2366.1 | 10.193 | 0.6894 | 1.8359 | 951.7 |
| 2 | 484.2 | 2372.4 | 10.589 | 0.4892 | 1.7744 | 878.0 |
| 3 | 489.5 | 2386.7 | 10.901 | 0.4646 | 1.5056 | 824.6 |
| 4 | 492.6 | 2404.0 | 11.226 | 0.4682 | 1.4455 | 789.9 |

### GPU
| GPU | Memory | Util |
|-----|--------|------|
| 0 | 25017 MiB | 97% |
| 1 | 25017 MiB | 88% |

两个实验都在运行中（目标 10 gen，当前各完成 gen0-4），均在训练 gen5。r=0.3 的 log_det 在 gen3-4 出现回升趋势（2366→2372→2387→2404），d4 在 gen4 也微弱反弹（0.4646→0.4682），而 r=0.2 的 log_det 和 d4 持续下降。

---
