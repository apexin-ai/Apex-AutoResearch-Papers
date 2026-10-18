# ops 14b status westd

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_14b-status-westd_20260518T030534_result.json`
- **Structured JSON:** [`544b82ef25fa5739415a.json`](../../sessions/54/544b82ef25fa5739415a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态：正在运行

| 项目 | 状态 |
|------|------|
| **PID** | 20700 存活，GPU 0 占用 32,372 MiB，92% util |
| **当前阶段** | Phase 3.1b — 生成 d1（LoRA finetune on d0 已完成） |
| **d0** | 完成 5000/5000 samples，LoRA 训练 loss=0.5451 (3 epochs, ~41min) |
| **d1** | 正在生成，已写入 2001 行（目标 5000），文件仍在增长 |
| **d2, d3** | 尚未开始 |
| **结果目录** | `results/qwen25_14b_scale/` 已创建但为空，尚未到 RF 训练阶段 |

### 进度估算

已完成流程：d0 生成 → d0 LoRA finetune → d1 生成中 (40%)

剩余流程：d1 生成剩余 → d1 LoRA finetune → d2 生成 → d2 LoRA finetune → d3 生成 → RF 训练 + 评估

每个 depth 周期（生成 + finetune）约 1.5-2 小时（参考 d0 周期）。d1 生成约完成 40%，还剩 ~3 个完整周期 + d1 收尾。

**预估 ETA：5-7 小时后完成**（约今天 16:00-18:00 UTC+8）。

---
