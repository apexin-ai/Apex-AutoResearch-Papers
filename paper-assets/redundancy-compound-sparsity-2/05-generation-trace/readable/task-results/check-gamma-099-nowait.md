# check gamma 099 nowait

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gamma_099_nowait_20260512T194709_result.json`
- **Structured JSON:** [`a013453d3ced18bdd52c.json`](../../sessions/a0/a013453d3ced18bdd52c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Gamma Sweep 结果

**PID 40063 仍在运行** — gamma=0.99 正在评估中（eval 进度 ~49%，约还需 4 分钟）。

已完成的 gamma 值（0.1–0.95）结果全部在 JSON 中：

| Strategy | γ | PPL | vs Full (+%) | vs Random (+%) |
|----------|------|--------|-------------|---------------|
| **full** | — | **7.1822** | baseline | — |
| **recency** | — | **7.1758** | -0.09% | — |
| **random** | — | **7.6353** | +6.31% | baseline |
| ema_0.1 | 0.1 | 8.1707 | +13.76% | -7.01% |
| ema_0.3 | 0.3 | 8.2099 | +14.31% | -7.53% |
| ema_0.5 | 0.5 | 8.1352 | +13.27% | -6.55% |
| ema_0.7 | 0.7 | 8.1367 | +13.29% | -6.57% |
| ema_0.8 | 0.8 | 7.9878 | +11.22% | -4.62% |
| ema_0.9 | 0.9 | 7.7788 | +8.31% | -1.88% |
| ema_0.95 | 0.95 | 7.6367 | +6.33% | -0.02% |
| ema_0.99 | 0.99 | ⏳ 运行中 | — | — |

**关键发现：**
- 脚本自身结论：`"conclusion": "ema_method_flawed"`，`"significant_finding": false`
- **所有 EMA gamma 都比 random baseline 更差**（负 gap_pct 表示 EMA PPL 高于 random）
- 最佳 EMA 是 γ=0.95，PPL=7.6367，勉强持平 random（7.6353），差距仅 -0.02%
- 趋势清晰：γ 越高（越接近 recency）PPL 越好，说明 EMA 没有带来额外价值
- **recency（7.1758）甚至略优于 full KV（7.1822）**，是最强策略

gamma=0.99 还在跑，预计几分钟后完成，但趋势已经明确——即使 γ=0.99 也大概率不会超过 recency。

---
