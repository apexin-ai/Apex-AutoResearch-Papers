# check gamma 099 read

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gamma_099_read_20260512T194330_result.json`
- **Structured JSON:** [`359e54118025b68bc613.json`](../../sessions/35/359e54118025b68bc613.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**进程仍在运行** — 正在评估最后一个 gamma=0.99（prefill 已完成，eval 刚开始约 1%，预计还需 ~8 分钟）。

JSON 已有 gamma 0.1–0.95 的完整结果，汇总如下：

| Strategy | Gamma | PPL | vs Random |
|----------|-------|-----|-----------|
| **full** (上界) | — | **7.1822** | — |
| **recency** | — | **7.1758** | — |
| **random** (基线) | — | **7.6353** | 0% |
| ema_0.95 | 0.95 | 7.6367 | -0.02% (持平) |
| ema_0.9 | 0.9 | 7.7788 | -1.88% |
| ema_0.8 | 0.8 | 7.9878 | -4.62% |
| ema_0.5 | 0.5 | 8.1352 | -6.55% |
| ema_0.7 | 0.7 | 8.1367 | -6.57% |
| ema_0.1 | 0.1 | 8.1707 | -7.01% |
| ema_0.3 | 0.3 | 8.2099 | -7.53% |
| **ema_0.99** | **0.99** | **(运行中)** | — |

关键发现：
- **所有 EMA 策略均劣于 random baseline**，gamma 越高越接近 random 但从未超越
- **recency 是最强 eviction 策略**，PPL 7.1758 甚至略优于 full（7.1822）
- JSON 中 `conclusion` 已标记为 `"ema_method_flawed"`
- gamma=0.99 还在跑，按趋势应接近 recency 水平（因为 gamma→1 时 EMA 退化为 recency）

---
