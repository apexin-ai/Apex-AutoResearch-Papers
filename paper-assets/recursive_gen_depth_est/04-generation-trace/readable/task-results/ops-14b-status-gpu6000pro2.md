# ops 14b status gpu6000pro2

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_14b-status-gpu6000pro2_20260518T024344_result.json`
- **Structured JSON:** [`d57af65ba3d38a65a5a7.json`](../../sessions/d5/d57af65ba3d38a65a5a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## qwen25_14b_scale_002 状态报告

**进程**: PID 806751 存活，GPU 0 占用 32376MiB，利用率 89%

**模型下载**: 8/8 shards 全部完成（shard 5 昨晚 SSL 错误后自动重试成功，00:26 完成）

**生成进度**:
| depth | 行数 | 状态 | 最后修改 |
|-------|------|------|---------|
| d0 | 5000 | 完成 | 05:51 |
| d1 | 3736/5000 | **进行中 (74.7%)** | 11:03 |
| d2 | 未开始 | - | - |
| d3 | 未开始 | - | - |

**当前阶段**: d1 生成中

**ETA 估算**:
- d0 耗时 ~4.5h，d1 速率 ~718 samples/h（14B 比小模型慢）
- d1 剩余 ~1264 samples → ~1.8h → 约 12:50 完成
- d2/d3 各约 7h
- RF 训练 ~30min
- **预计总完成时间: ~May 19 03:00-04:00**

**结果文件**: 尚无 `qwen25_14b_scale_002` 结果目录

---
