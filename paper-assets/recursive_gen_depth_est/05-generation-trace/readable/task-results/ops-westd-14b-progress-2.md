# ops westd 14b progress 2

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-14b-progress-2_20260518T115037_result.json`
- **Structured JSON:** [`2ddbbf502e6c674455e7.json`](../../sessions/2d/2ddbbf502e6c674455e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

| 项目 | 状态 |
|---|---|
| **GPU** | GPU 0 在用 (92% util, 32G/98G VRAM, PID 20700 python3)，GPU 1 空闲 |
| **数据** | d0: 5000, d1: 5000, d2: 3510 (生成中) |
| **训练进度** | d1 LoRA 训练已完成 (3 epoch, loss 0.3451, 42min)，adapter 已保存。当前正在 **Phase 3.2b: 用 LoRA(d1) 生成 d2**，模型权重加载完成，正在推理生成 5000 条 d2 样本 (已出 3510 条) |
| **结果目录** | `results/qwen25_14b*/` 为空，尚未产出最终结果 |

进展正常，d2 生成约完成 70% (3510/5000)。

---
