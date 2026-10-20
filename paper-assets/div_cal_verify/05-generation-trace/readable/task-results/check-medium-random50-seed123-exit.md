# check medium random50 seed123 exit

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_medium_random50_seed123_exit_20260514T083159_result.json`
- **Structured JSON:** [`f5dd282a66da9316ebb2.json`](../../sessions/f5/f5dd282a66da9316ebb2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 检查结果

### medium_random50_seed123：**已正常完成** ✓

日志末尾有 `===== COMPLETE =====`，结束时间 Thu May 14 16:29:43 CST 2026。gen_0 到 gen_7 全部完成，输出在 `/root/autodl-tmp/div_cal_verify/results_medium_random50_seed123/random_50/`。

### 各代 PPL 值

| Gen | PPL | RankMe | kNN | Rare n-gram | Rank Corr |
|-----|-----|--------|-----|-------------|-----------|
| 0 | 26.31 | 363.28 | 0.988 | 0.0343 | +0.019 |
| 1 | 33.54 | 399.19 | 0.988 | 0.0298 | +0.013 |
| 2 | 43.31 | 417.48 | 0.988 | 0.0224 | +0.008 |
| 3 | 50.01 | 423.83 | 0.988 | 0.0187 | -0.013 |
| 4 | 56.82 | 425.56 | 0.988 | 0.0160 | -0.034 |
| 5 | 65.35 | 426.70 | 0.988 | 0.0154 | -0.053 |
| 6 | 70.43 | 421.46 | 0.988 | 0.0140 | -0.047 |
| 7 | **72.55** | 421.96 | 0.988 | 0.0131 | -0.049 |

PPL 从 26.31 升至 72.55（2.76x 退化），kNN 全程稳定 0.988，rare n-gram 从 3.4% 降至 1.3%。

### auto_chain_cuda0_seed456：**已触发** ✓

`chain_cuda0_seed456` tmux session 已于 16:30:31 创建（random50_seed123 完成后 48 秒），正在运行 `medium_uncurated_seed456`。

### cuda:0 当前状态

cuda:0 上有进程占用 19250 MiB 但 GPU-Util 0%（可能在数据加载/生成阶段）。cuda:1 上 python3 占用 28738 MiB，GPU-Util 100%。

**注意**：没有 W&B 数据是因为这个实验没有配置 W&B logging，结果只写到了本地 `all_results.json`。

---
