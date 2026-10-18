# ops check gemma2 yi15 status

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_gemma2_yi15_status_20260514T150407_result.json`
- **Structured JSON:** [`0a4a76e85303439f0197.json`](../../sessions/0a/0a4a76e85303439f0197.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### 1. gemma2_9b_full_pipeline — **已完成**

- **进程**：已退出，GPU 无占用（cuda:0 显存 0MiB，利用率 0%）
- **结果**：成功完成全部 5 个阶段，耗时 0.3h，结果保存在 `/root/ratekv/gemma2_full_results.json`
- **关键指标**：
  - Baseline (bf16) PPL: 711.38
  - Non-uniform MCKP PPL: 514.62 (+65.29 vs uniform)
  - Uniform 4-bit PPL: 579.91
  - Top-5% concentration: 1.6361, L0 dominance: 5.34x
  - Best k: 16 (PPL=377.87)
  - Verdict: **PASS**
- **模型下载**：gemma-2-9b 完整下载（35GB，8 个 shard 全部就位）

### 2. yi15_9b_full_pipeline — **首次运行失败，正在重试（等待模型下载）**

- **首次运行**（wait_and_run_yi15.sh 旧版）：
  - 22:51 下载判定完成（只检查了 1 个 shard 就认为下载完成——旧脚本有 bug）
  - 22:51 启动 pipeline → 立即崩溃：`FileNotFoundError: model-00001-of-00004.safetensors` 不存在
  - 原因：ModelScope 并行下载，旧脚本没有正确检查所有 4 个 shard
  
- **当前状态**（wait_and_run_yi15_v2.sh 新版，PID 233159）：
  - 进程存活，正在等待 4 个 shard 全部下载完成
  - 目前 Yi-1.5-9B 目录 7.3GB，已有 2/4 shard（model-00002 和 model-00004）
  - model-00001 和 model-00003 仍在由 PID 228878 下载中（下载速度约 400-600 KB/s，分别完成 61% 和 68%）
  - v2 脚本逻辑正确：等 4 个 shard 都出现 + 文件大小稳定后才启动 pipeline
  
- **预计**：Yi 模型总约 18GB，当前 7.3GB，剩余约 10GB，按 ~500KB/s 估算还需 **~5-6 小时**才能下载完成并启动 pipeline

### 异常

- Yi 模型下载速度极慢（~500KB/s），可能是 ModelScope CDN 到该服务器的带宽限制
- cuda:1 空闲，等 Yi 下载完后 v2 脚本会自动在 cuda:1 上启动 pipeline

---
