# monitor exp progress check

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp_progress_check_20260517T210201_result.json`
- **Structured JSON:** [`bc6553afaa2067b155fe.json`](../../sessions/bc/bc6553afaa2067b155fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个进程均在运行。汇总如下：

---

## exp_005 — adaptive k=20 (PID 116947, 运行 7h45m, 当前正在训练 Gen 5)

| Gen | eff_rank | log_det | ppl | distinct_4 | mix_ratio | controller |
|-----|----------|---------|-----|------------|-----------|------------|
| 0 | 417.5 | 2366.7 | 9.55 | 0.741 | — | — |
| 1 | 476.9 | 2366.5 | 10.09 | 0.661 | 0.5 | 未触发 |
| 2 | 486.9 | 2395.2 | 10.42 | 0.615 | 0.5 | 未触发 |
| 3 | 496.1 | 2425.4 | 10.76 | 0.440 | 0.5 | 未触发 |
| 4 | 501.8 | **2450.7** | 11.13 | **0.384** | 0.5 | 未触发 |

**关键发现：log_det 持续上升（2366→2395→2425→2450），没有下降趋势。Controller 从未触发（ratio 始终 0.5）。** distinct_4 从 0.74 剧烈下降到 0.38，多样性已显著退化，但 log_det 信号没有检测到这一点（因为 log_det 在涨而非跌）。effective_rank 也在持续上升。

---

## exp_006 — adaptive k=10 (PID 134913, 运行 3h09m, 当前正在训练 Gen 3)

| Gen | eff_rank | log_det | ppl | distinct_4 | mix_ratio | controller |
|-----|----------|---------|-----|------------|-----------|------------|
| 0 | 417.5 | 2366.7 | 9.55 | 0.741 | — | — |
| 1 | 477.3 | 2365.1 | 10.09 | 0.710 | 0.5 | 未触发 |
| 2 | 487.1 | 2394.0 | 10.42 | 0.600 | 0.5 | 未触发 |

Controller 未触发。趋势与 exp_005 前两代一致（log_det 微降后回升）。

---

## exp_004 — fixed_mix baseline (PID 135411, 运行 3h06m, 当前正在训练 Gen 2)

| Gen | eff_rank | log_det | ppl | distinct_4 | mix_ratio | controller |
|-----|----------|---------|-----|------------|-----------|------------|
| 0 | 417.5 | 2366.7 | 9.55 | 0.741 | — | — |
| 1 | 477.9 | 2366.6 | 10.08 | 0.669 | 0.5 | — |

固定 mix baseline，进度较慢，刚完成 Gen 1。

---

## 核心问题

**exp_005 的 controller 在 5 代中从未触发。** log_det 不仅没下降，反而单调上升了 84 点（2366→2450）。这意味着 log_det 作为 collapse 预警信号在当前设置下失效了——模型多样性（distinct_4）已经腰斩（0.74→0.38），但 log_det 完全没有反映出退化趋势。tau=0.002 的阈值和 log_det 信号的方向可能都需要重新审视。

---
