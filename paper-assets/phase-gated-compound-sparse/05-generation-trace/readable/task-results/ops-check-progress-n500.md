# ops check progress n500

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-progress-n500_20260515T025542_result.json`
- **Structured JSON:** [`ae9303045a633ed486cc.json`](../../sessions/ae/ae9303045a633ed486cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 进度报告

### 实验 1: c2_n500_deepseek (DeepSeek-R1-Distill-Qwen-7B)

| GPU | 方法 | s015 | s020 | s025 | s030 |
|-----|------|------|------|------|------|
| GPU 0 | importance | ✅ 02:31 | ✅ 06:55 | 🔄 **462/500** | ⏳ 待启动 |
| GPU 1 | random | ✅ 02:05 | ✅ 06:30 | ✅ 10:54 | 🔄 **7/500** |

- 每个 condition 平均耗时: **~4h24m**
- GPU 0 s025 ETA: ~**11:17** (剩 38 个, ~20min), 之后跑 s030 → 全部完成约 **15:41**
- GPU 1 s030 刚启动 → 完成约 **15:19**
- **DeepSeek 整体完成 ETA: ~15:41**

### 实验 2: c2_qw_n500_r3 (Qwen2.5-7B-Instruct)

| GPU | 方法 | s015 | s020 | s025 | s030 |
|-----|------|------|------|------|------|
| GPU 2 | importance | ✅ 03:02 | ✅ 06:27 | ✅ 09:53 | 🔄 **153/500** |
| GPU 3 | random | ✅ 03:11 | ✅ 06:36 | ✅ 10:01 | 🔄 **136/500** |

- 每个 condition 平均耗时: **~3h25m**
- GPU 2 s030: 153/500, 已跑 ~1h04m → 完成约 **13:22**
- GPU 3 s030: 136/500, 已跑 ~56min → 完成约 **13:27**
- **Qwen 整体完成 ETA: ~13:27**

### GPU 利用率

| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| 0 | 78% | 33.4 / 97.9 GB |
| 1 | 76% | 18.6 / 97.9 GB |
| 2 | 78% | 27.8 / 97.9 GB |
| 3 | 77% | 28.4 / 97.9 GB |

### 汇总

- 16 个 condition 中已完成 **10 个**，正在跑 **4 个**，待启动 **2 个** (DS imp s030 待 s025 完成后自动启动)
- Qwen 实验预计 **今天 13:30** 前全部完成
- DeepSeek 实验预计 **今天 15:45** 前全部完成
- 所有 4 个 GPU 运行正常，进程健康

---
