# diagnose grpo v2 step50 eval

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_grpo_v2_step50_eval_20260513T102931_result.json`
- **Structured JSON:** [`3040d409317a70ec1b65.json`](../../sessions/30/3040d409317a70ec1b65.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 1. grpo_v2_step50_eval — 已完成

评估于 `2026-05-13 18:28:53` 成功结束，结果文件 14.7MB 已写入。

**汇总指标（985 samples）：**

| 指标 | 值 |
|------|-----|
| **RE-F1** | **0.4384** |
| **Evi-F1** | **0.3705** |
| **Attribution Precision** | **0.9424** |

### 2. grpo_pilot_v2 — 仍在运行

进程 88042 存活，已运行 **4h58m**。训练进度 **97/100 步**，预计剩余约 10 分钟。

最近几步关键指标：
- Step 95: reward=0.607, loss=0.024, clipped_ratio=0.81（生成长度触顶 2048）
- Step 96: reward=0.757, loss=-0.062
- Step 97: reward=0.745, loss=-0.219

输出目录 `grpo_v2/` 已有 `checkpoint-50`。训练完成后应产生 step-100 的 final checkpoint。

### 3. GPU 状态

| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| GPU 0 | **0%** | 0 / 97887 MiB（空闲） |
| GPU 1 | **59%** | 35813 / 97887 MiB（v2 训练中） |

GPU 0 空闲——eval 已结束释放。GPU 1 正在跑 v2 训练最后几步。

**结论：** eval 已成功完成，v2 训练还剩 ~3 步（约 10 分钟）即将完成。无异常。

---
