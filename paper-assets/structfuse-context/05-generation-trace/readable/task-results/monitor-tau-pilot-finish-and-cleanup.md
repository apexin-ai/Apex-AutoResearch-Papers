# monitor tau pilot finish and cleanup

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_tau_pilot_finish_and_cleanup_20260513T000052_result.json`
- **Structured JSON:** [`cc4e34676d62d003a4e6.json`](../../sessions/cc/cc4e34676d62d003a4e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

---

### 1. τ=0.05 最终指标

| 指标 | 值 |
|------|-----|
| val_loss | 0.1392 |
| recall@1 | 0.8425 |
| recall@5 | 0.8425 |
| recall@10 | 0.8425 |

recall@1/5/10 完全相同，说明 pool_size 很小或 evaluation 逻辑有问题（可能只在 positive 和 3 个 negative 之间排序，pool_size=4）。

### 2. 与 MVP baseline 对比

| 配置 | recall@1 | pool_size |
|------|----------|-----------|
| MVP baseline (τ=0.07, random) | **0.984** | 25 |
| τ=0.05 pilot | 0.843 | ~4 (推测) |

τ=0.05 在更小的 pool 上 recall 反而更低，表现明显差于 τ=0.07。τ 过小可能导致 softmax 过于尖锐、梯度不稳定。

### 3. GPU cuda:4
已释放：0% 利用率，3 MiB 显存。

### 4. M1 提取进度
- PID 577864 运行中，已跑 3h14m
- **20 个 repo**，**3857 个 instance**（JSON 文件）
- 仍在处理中（最新日志：oauthlib, flake8, cantools 等）

### 5. StarCoder 下载
- 路径：`/root/autodl-tmp/.hf_cache/starcoder2-3b/`
- 大小：**3.9 GB**（含 config.json，看起来已下载完成）

### 6. 清理
- tau_pilot_0.05/0.1/0.2 checkpoint 目录已删除
- 数据盘 169G 用了 118G，剩余 52G (70%)

---
