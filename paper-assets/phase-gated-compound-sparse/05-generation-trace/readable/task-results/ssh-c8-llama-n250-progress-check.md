# ssh c8 llama n250 progress check

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_c8_llama_n250_progress_check_20260516T150558_result.json`
- **Structured JSON:** [`bb152167dce9c6bd95ab.json`](../../sessions/bb/bb152167dce9c6bd95ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## c8_llama_n250_fixed 实验进度

### 已完成 (3/8)

| 条件 | 完成时间 (CST) | 结果文件大小 |
|------|---------|------------|
| importance_s015 | May 16 17:35 | 21MB ✓ |
| importance_s020 | May 16 17:32 | 21MB ✓ |
| importance_s025 | 预先完成 (GPU0 单跑) | 21MB ✓ |

### 正在运行 (3/8)

| 条件 | GPU | 已运行 | 预估剩余 |
|------|-----|--------|----------|
| random_s015 | GPU 2 (主脚本 Round 3) | 5h32m | ~45min |
| random_s020 | GPU 3 (主脚本 Round 3) | 5h32m | ~45min |
| importance_s030 | GPU 0 (chain 脚本) | 4h51m | ~1h25m |

### 未开始 (2/8)

| 条件 | 说明 |
|------|------|
| random_s025 | Round 4，等 Round 3 完成后启动 |
| random_s030 | Round 4，等 Round 3 完成后启动 |

### 时间估算

- 基准：Round 1 跑了 ~6h15m（250 problems，importance s015+s020 并行）
- **Round 3 完成**：约 May 17 00:10 CST
- **Round 4 开始→完成**：约 00:10 → 06:25 CST
- **importance_s030 完成**：约 00:30 CST（独立于主脚本）
- **全部 8 条件完成**：约 **May 17 06:25 CST**（~7h 后）

### 异常

- importance_s030 的 `profiling_results.json` 目前是 116 字节的 sentinel 占位文件——主脚本 Round 2 误判为已完成而跳过。实际由 `chain_s030_after_s025.sh`（PID 562663）在 GPU 0 上跑，guardian 脚本监控中。chain 完成后会用真实数据覆盖 sentinel。
- random_s015 和 random_s020 的输出目录目前为空——profiling 脚本在全部 250 个 problem 处理完后才一次性写出结果文件（非增量写入）。
- 无 OOM 或错误迹象，4 个 python 进程均在 100% CPU 正常运行。

---
