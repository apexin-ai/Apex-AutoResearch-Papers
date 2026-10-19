# infra status check 4items

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_status-check-4items_20260522T170352_result.json`
- **Structured JSON:** [`66e7ddf174d9106cdfe3.json`](../../sessions/66/66e7ddf174d9106cdfe3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### 1. Gemma L21 Steering (PID 499402)
- **状态**: 运行中，已 1h07m
- **进度**: 模型刚加载完毕，尚未开始 alpha 推理
- **GPU**: GPU 0, 18570 MiB
- **L17 已完成结果** (probe acc = 0.7532):

| Alpha | steering_flips | control_flips | fisher_p | p2c | c2p |
|-------|---------------|---------------|----------|-----|-----|
| -20.0 | 2 | 8 | 0.1038 | 0 | 0 |
| -10.0 | 2 | 2 | 1.0000 | 0 | 0 |
| -5.0  | 2 | 1 | 1.0000 | 0 | 0 |
| 5.0   | 1 | 3 | 0.6226 | 0 | 0 |
| 10.0  | 2 | 2 | 1.0000 | 0 | 0 |
| 20.0  | 1 | 4 | 0.3710 | 0 | 0 |

**L17 steering 完全无效** — 所有 alpha 下 p2c=0, c2p=0，steering flips 与 control flips 无显著差异。

### 2. DE Probe Training (PID 496671)
- **状态**: 运行中，已 1h50m
- **进度**: EN→EN 方向，bootstrap 426/2000（~21%）
- **待完成**: EN→EN 剩余 + ZH→EN + DE→EN（3个语言方向，每个2000 seeds）
- **预计**: 当前方向还需 ~1.5h，全部完成约 6-7h
- **无 GPU 占用**（CPU-only 训练，32 jobs 并行）

### 3. Gemma Probe n=2000 (PID 476334)
- **状态**: 运行中，已 6h19m
- **进度**: en_zh 方向已完成（56.8min），zh_en 方向 1394/2000（~70%）
- **预计**: zh_en 还需 ~20min 完成，之后输出结果文件
- **无 GPU 占用**（CPU-only）

### 4. GPU 状态

| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| 0 | 18579 / 97887 MiB | 26% |
| 1-3 | 空闲 | 0% |

GPU 1-3 完全空闲，仅 L21 steering 占用 GPU 0。

---
