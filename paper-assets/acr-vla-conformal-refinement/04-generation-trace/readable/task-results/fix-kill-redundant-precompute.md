# fix kill redundant precompute

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_kill-redundant-precompute_20260522T184643_result.json`
- **Structured JSON:** [`fee161e02f46aebd6dbe.json`](../../sessions/fe/fee161e02f46aebd6dbe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### (a) crm_cache_v5 完整性

| Suite | 样本范围 | 聚合文件 | 状态 |
|-------|---------|---------|------|
| object | 0–4857 (3 shards) | expert_actions/k_samples/obs_features.pt | 完整 |
| spatial | 0–4056 (3 shards) | 同上 | 完整 |
| goal | 0–61728 (1 shard) | 同上 | 完整 |
| long | 0–131000+ (1 shard) | 同上 | 完整 |

### (b) 进程 Kill 结果

| 服务器 | PID | 任务 | 结果 |
|--------|-----|------|------|
| bjb1-18228 | 883211 | long precompute pi05 | killed |
| bjb2-28827 | 206132 | goal shard 0/3 pi05 | killed |
| bjb2-28827 | 206279 | goal shard 1/3 pi05 | killed |
| bjb2-28827 | 206558 | goal shard 2/3 pi05 | killed |

### (c) GPU 释放确认

- **bjb1-18228**: 全部 4 GPU 已释放（0 MiB used）
- **bjb2-28827**: GPU 3/4/5 已释放（0 MiB），GPU 0 有 541 MiB 占用（非本次进程相关）

---
