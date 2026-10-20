# check running progress v2

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_running_progress_v2_20260514T071631_result.json`
- **Structured JSON:** [`5c2659aca0cfcda411dc.json`](../../sessions/5c/5c2659aca0cfcda411dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 1. random50_seed123 (cuda:0)

| Gen | Perplexity | RankMe | Rare n-gram | 耗时 |
|-----|-----------|--------|-------------|------|
| 0 | 26.31 | 363.28 | 0.0343 | 727s (12.1m) |
| 1 | 33.54 | 399.19 | 0.0298 | 681s (11.4m) |
| 2 | 43.31 | 417.48 | 0.0224 | 686s (11.4m) |

- **当前进度**: Gen 3/7 训练中（[3/5] Training student），log 末尾显示 gen_2 训练步骤，但 gen_2 metrics 已写入，说明 gen_2 刚完成、gen_3 正在进行
- **已完成**: 3/8 代 (gen_0–gen_2)
- **剩余预估**: 5 代 × ~698s ≈ **58 分钟**（约 16:15 完成）
- **趋势**: perplexity 逐代上升（26→33→43），rare n-gram 下降——符合 model collapse 预期

### 2. external_seed456 (cuda:1)

- **启动时间**: 15:11:28（仅 5 分钟前）
- **当前进度**: Gen 0/7，gen_0 目录已创建但无 metrics，正在初始化/生成阶段
- **剩余预估**: 参考 random50 的 ~700s/gen，8 代 ≈ **93 分钟**（约 16:45 完成）

### 3. 异常检查

- **无异常**。两张 GPU 利用率 49%/48%，温度 45°C/44°C，显存使用正常（71.6GB/19.3GB）。无 OOM/error。
- `torch_dtype` deprecated 警告可忽略。

### 4. chain_cuda0_seed456.sh

- **存在**，内容正确：`medium_uncurated_seed456 → medium_rgds_seed456 → medium_random50_seed456`，三个实验在 cuda:0 上串行执行
- 脚本可执行权限已设置

### 5. 自动衔接机制

- **没有**。无 auto-chain/wait 进程在等待 random50_seed123 完成。random50_seed123 跑完后需要 **手动启动** chain_cuda0_seed456.sh。

预计 random50_seed123 约 16:15 完成，届时需要手动在 cuda:0 的 tmux session 中启动 chain 脚本。

---
