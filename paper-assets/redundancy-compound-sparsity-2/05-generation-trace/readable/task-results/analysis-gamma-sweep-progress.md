# analysis gamma sweep progress

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gamma_sweep_progress_20260512T174307_result.json`
- **Structured JSON:** [`fe0d273051157adf2793.json`](../../sessions/fe/fe0d273051157adf2793.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Gamma Sweep 进度报告

### 进程状态
**运行中** — PID 40063，已运行 1h10m，当前正在跑 `ema_0.5`（prefill 阶段 13%）

### 已完成结果

| 策略 | PPL | vs Random (7.6353) | vs Full (7.1822) |
|------|-----|-------------------|-------------------|
| full (上界) | 7.1822 | — | — |
| **recency** | **7.1758** | **+0.78%** ✓ | **-0.09%** |
| random (baseline) | 7.6353 | — | +6.31% |
| ema_0.1 | 8.1707 | **-7.01%** ✗ | +13.76% |
| ema_0.3 | 8.2099 | **-7.53%** ✗ | +14.31% |

### 分析

两个已完成的 EMA gamma 均**远差于 random**（-7% ~ -7.5%），且趋势在恶化（0.3 比 0.1 更差）。结果文件中 `conclusion` 已标记为 `"ema_method_flawed"`。

值得注意：**recency 策略 PPL 7.1758 几乎等于 full（7.1822）**，远好于 random，说明 eviction 机制本身没问题，但 EMA scoring 在选错 token evict。

### 剩余时间估算

每个 gamma 约 22 分钟（基于已完成的两个）。剩余 6 个 gamma（0.5–0.99），ema_0.5 已开始 prefill，预计 **约 2 小时完成全部**。

### Gate 判定（初步）

Gate 要求任一 gamma beat random ≥5%。目前两个都 **输给 random 7%+**。除非高 gamma 值出现质变（可能性低，因为高 gamma → 更接近 recency，而 recency 用的是完全不同的 scoring），大概率全部 fail。

---
