# check gamma sweep json

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gamma_sweep_json_20260512T195155_result.json`
- **Structured JSON:** [`ce6a4e646899f7e89b4a.json`](../../sessions/ce/ce6a4e646899f7e89b4a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整结果如下：

## Gamma Sweep 结果

**配置**: DeepSeek-R1-Distill-Qwen-14B, budget_ratio=0.5, seq_len=32768, prefill=26214, eval=6554

### PPL 汇总

| Strategy | γ | PPL | vs Full (%) | vs Random (%) |
|----------|------|--------|-------------|---------------|
| **full** (oracle) | — | **7.1822** | — | — |
| **recency** | — | **7.1758** | -0.09 | +6.02 |
| **random** | — | 7.6353 | +6.31 | — |
| ema_0.99 | 0.99 | 7.5302 | +4.85 | **+1.38** |
| ema_0.95 | 0.95 | 7.6367 | +6.33 | -0.02 |
| ema_0.9 | 0.9 | 7.7788 | +8.31 | -1.88 |
| ema_0.8 | 0.8 | 7.9878 | +11.22 | -4.62 |
| ema_0.7 | 0.7 | 8.1367 | +13.29 | -6.57 |
| ema_0.5 | 0.5 | 8.1352 | +13.27 | -6.55 |
| ema_0.3 | 0.3 | 8.2099 | +14.31 | -7.53 |
| ema_0.1 | 0.1 | 8.1707 | +13.76 | -7.01 |

### 关键发现

- **结论: `ema_method_flawed`**，`significant_finding: false`
- **所有 EMA γ 值都劣于 random**，除了 γ=0.99 勉强赢 random 1.38%
- **recency 是最强 baseline**（PPL 7.1758，甚至微优于 full cache 的 7.1822）
- γ 越小（越重当前 attention），PPL 越差；γ 越大（越重历史），越接近 recency 的效果
- γ=0.99 本质上已经退化为近似 recency 策略

**核心问题**：EMA 分数并没有捕捉到比简单 recency 更好的 eviction 信号。当 γ→1 时 EMA 退化为 recency，性能才开始改善——说明 attention score 本身作为 importance 信号在这个 eviction 场景下不如"最近使用"有效。

---
