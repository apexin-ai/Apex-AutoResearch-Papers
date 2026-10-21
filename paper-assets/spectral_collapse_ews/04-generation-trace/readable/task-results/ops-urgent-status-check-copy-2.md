# ops urgent status check

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent-status-check_20260521T231412_result.json`
- **Structured JSON:** [`eb13193022e38ab78d18.json`](../../sessions/eb/eb13193022e38ab78d18.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态报告

### GPU
| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 0% | 0 / 97887 MiB (空闲) |
| 1 | 94% | 25017 / 97887 MiB (运行中) |

### exp_014b (r=0.25, seed43) — **已完成**
- gen_0 ~ gen_10 全部完成，EXIT_CODE=0
- 最后一个 checkpoint 时间: May 22 06:21 (gen_10)
- 结果摘要:

| Gen | Eff.Rank | Perplexity | Distinct-4 | Train Loss |
|-----|----------|------------|------------|------------|
| 0 | 417.55 | 9.55 | 0.7415 | — |
| 1 | 475.66 | 10.23 | 0.6584 | 1.802 |
| 2 | 483.00 | 10.65 | 0.5574 | 1.722 |
| 3 | 488.96 | 11.00 | 0.4772 | 1.521 |
| 4 | 491.74 | 11.35 | 0.3735 | 1.363 |
| 5 | 495.60 | 11.67 | 0.3378 | 1.200 |
| 6 | 497.83 | 12.00 | 0.3374 | 1.053 |
| 7 | 502.04 | 12.41 | 0.3700 | 1.060 |
| 8 | 506.76 | 12.77 | 0.3586 | 1.093 |
| 9 | 510.49 | 13.18 | 0.3848 | 1.073 |
| 10 | 515.56 | 13.61 | 0.3380 | 1.061 |

### exp_015 (r=0.25, seed44) — **运行中，gen_6 完成，正在跑 gen_7**
- gen_0 ~ gen_6 checkpoint 已存在
- 日志显示正在生成 gen_7 的合成数据 (24640/37500 samples)
- GPU 1 在 94% 利用率，确认进程活跃
- 已有结果 (到 gen_6):

| Gen | Eff.Rank | Perplexity | Distinct-4 | Train Loss |
|-----|----------|------------|------------|------------|
| 0 | 417.55 | 9.55 | 0.7305 | — |
| 1 | 475.92 | 10.22 | 0.6379 | 1.800 |
| 2 | 484.39 | 10.64 | 0.5156 | 1.689 |
| 3 | 488.62 | 11.00 | 0.4518 | 1.473 |
| 4 | 493.01 | 11.33 | 0.4156 | 1.388 |
| 5 | 494.32 | 11.64 | 0.4008 | 1.319 |
| 6 | 498.74 | 11.97 | 0.3994 | 1.294 |

- 预计还需 ~4 代 (gen_7~10)，每代约 2h，约 **8 小时后完成**

### 磁盘
`/root/autodl-tmp`: 163G / 250G 已用，**剩余 88G (34%)**，空间充足。

---
