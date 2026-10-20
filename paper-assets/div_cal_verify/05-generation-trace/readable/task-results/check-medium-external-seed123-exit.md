# check medium external seed123 exit

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_medium_external_seed123_exit_20260514T064713_result.json`
- **Structured JSON:** [`a7871473690621a42bba.json`](../../sessions/a7/a7871473690621a42bba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：**SUCCESS**

实验 `medium_external_seed123` 已正常完成全部 8 代（gen_0 ~ gen_7），日志末尾显示 `===== COMPLETE =====`。

### Gen 7 关键指标

| 指标 | 值 |
|------|-----|
| Perplexity | 79.56 |
| RankMe | 429.83 |
| k-NN accuracy | 0.9880 |
| Rare n-gram | 0.0161 |
| Rank corr | -0.0533 |
| Selection ratio | 1.222 |

### 全代 Metrics 汇总

| Gen | PPL | RankMe | kNN | Rare | Corr |
|-----|------|--------|------|------|------|
| 0 | 26.30 | 366.16 | 0.9880 | 0.0343 | 0.0119 |
| 1 | 33.62 | 400.20 | 0.9880 | 0.0303 | 0.0077 |
| 2 | 44.51 | 417.58 | 0.9880 | 0.0246 | -0.0114 |
| 3 | 51.18 | 421.73 | 0.9880 | 0.0206 | -0.0140 |
| 4 | 61.11 | 427.42 | 0.9880 | 0.0184 | -0.0282 |
| 5 | 69.58 | 429.36 | 0.9880 | 0.0172 | -0.0232 |
| 6 | 74.33 | 428.14 | 0.9880 | 0.0168 | -0.0458 |
| 7 | 79.56 | 429.83 | 0.9880 | 0.0161 | -0.0533 |

趋势：PPL 逐代上升（26→80），RankMe 饱和在 ~430，kNN 恒定 0.988，rare n-gram 逐代下降，rank correlation 逐代变负。

### Auto chain 状态

tmux 命令在 read-only 模式下被阻止，无法确认 auto_cuda1 chain 是否已启动。需要用 `ssh_execute` 检查 tmux sessions。

---
