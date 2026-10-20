# check gamma sweep collect

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gamma_sweep_collect_20260512T193953_result.json`
- **Structured JSON:** [`a1eeb51c40b1dea15678.json`](../../sessions/a1/a1eeb51c40b1dea15678.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**进程状态**：PID 40063 仍在运行（已运行 ~3h07m），当前正在执行最后一个配置 **gamma=0.99**，prefill 阶段 73%（38/52）。

**gamma=0.99 预计剩余时间**：prefill 还剩 ~4 分钟，之后 eval 约 ~8 分钟，总计约 **12-15 分钟后完成**。

### 已完成的完整结果

| Strategy | gamma | PPL | vs Full | vs Random |
|----------|-------|-----|---------|-----------|
| **full** (baseline) | — | **7.1822** | — | — |
| **recency** | — | **7.1758** | -0.09% | — |
| **random** | — | **7.6353** | +6.31% | — |
| ema_0.1 | 0.1 | 8.1707 | +13.76% | -7.01% |
| ema_0.3 | 0.3 | 8.2099 | +14.31% | -7.53% |
| ema_0.5 | 0.5 | 8.1352 | +13.27% | -6.55% |
| ema_0.7 | 0.7 | 8.1367 | +13.29% | -6.57% |
| ema_0.8 | 0.8 | 7.9878 | +11.22% | -4.62% |
| ema_0.9 | 0.9 | 7.7788 | +8.31% | -1.88% |
| **ema_0.95** | 0.95 | **7.6367** | +6.33% | **-0.02%** |
| ema_0.99 | 0.99 | ⏳ 运行中 | — | — |

### 关键发现

- JSON 中的结论是 `"ema_method_flawed"`：所有 EMA gamma 值的 PPL 都 **差于** random baseline
- gamma 越大（越接近 1.0）PPL 越好，趋势明确：0.95 时几乎追平 random（差 0.02%）
- **recency** 策略表现最好，PPL 7.1758 甚至略优于 full KV cache（7.1822）
- gamma=0.99 正在运行，按趋势预计 PPL 可能略优于 random，但仍远差于 recency/full

---
