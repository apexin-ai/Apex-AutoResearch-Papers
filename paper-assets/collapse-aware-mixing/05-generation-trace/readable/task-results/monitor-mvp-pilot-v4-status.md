# monitor mvp pilot v4 status

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_mvp_pilot_v4_status_20260512T145808_result.json`
- **Structured JSON:** [`d3817fd32d9b8c49b042.json`](../../sessions/d3/d3817fd32d9b8c49b042.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## mvp_pilot_v4 训练状态

**GPU**
- 利用率: 86%，显存: 22,885 / 97,887 MiB (~23%)

**进程**
- PID 28471 运行中，已运行 6 分 04 秒
- 命令: `python3 pilot_pipeline.py --num_generations 3 --tokens_per_generation 90M`
- 另有 2 个 DataLoader worker 子进程 (28665, 28666)

**训练进度**
- 当前: **G0 (第 0 代 / 共 3 代)**，step **151 / 1373**，进度 ~11%
- 速度: ~2.09 s/step（稳定）
- G0/training/ 下已保存 `checkpoint-152`（第一个 checkpoint）

**预估剩余时间**
- G0 剩余: (1373 - 151) × 2.09s ≈ **42 分钟**
- 3 代总计: 1373 × 3 × 2.09s ≈ 8610s ≈ **2 小时 24 分钟**
- 已消耗 ~6 分钟，预估总剩余: **约 2 小时 18 分钟**

**Summary**: 尚未生成 (`pilot_summary.json` 不存在)。训练正常运行中，无异常。

---
