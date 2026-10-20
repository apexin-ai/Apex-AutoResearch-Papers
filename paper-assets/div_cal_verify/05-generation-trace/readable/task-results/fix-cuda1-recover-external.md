# fix cuda1 recover external

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_cuda1_recover_external_20260514T031012_result.json`
- **Structured JSON:** [`2b106db6d1df6f339632.json`](../../sessions/2b/2b106db6d1df6f339632.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

seed123 进程已确认运行（PID 405067）。它还在初始化阶段（Python 加载模块），GPU 显存很快会分配。

---

## 报告

### 1. medium_external_seed42：已完成 ✓

Gen 0→7 全部完成，关键指标：

| Gen | PPL | RankMe | kNN | Rare n-gram | Rank Corr |
|-----|-----|--------|-----|-------------|-----------|
| 0 | 26.33 | 363.43 | 0.988 | 0.0346 | +0.035 |
| 7 | 77.74 | 421.50 | 0.988 | 0.0165 | -0.007 |

PPL 增长 2.95x，RankMe +58，kNN 稳定 0.988。Registry 已更新为 DONE/success。

### 2. medium_external_seed123：已成功启动 ✓

- PID 405067，tmux session `medium_external_seed123`
- 运行在 cuda:1（`CUDA_VISIBLE_DEVICES=1`）
- 日志：`/root/autodl-tmp/div_cal_verify/medium_external_seed123.log`
- Registry 已标记 RUNNING

### 3. cuda:1 恢复状态

进程已启动，当前在 Python 初始化阶段（加载 transformers/torch 模块）。显存即将分配。cuda:0 上的 uncurated_seed123 正常运行中（71641 MiB, ~50% util）。

dummy tmux session `medium_random50` 已清理。

---
