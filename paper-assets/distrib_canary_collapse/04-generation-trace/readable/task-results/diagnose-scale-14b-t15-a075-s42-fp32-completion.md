# diagnose scale 14b t15 a075 s42 fp32 completion

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_scale_14b_t15_a075_s42_fp32_completion_20260523T005827_result.json`
- **Structured JSON:** [`6251d36dc9d52a537067.json`](../../sessions/62/6251d36dc9d52a537067.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验状态：仍在运行**

- **PID 793171**：状态 R（运行中），已运行 12h21m
- **进度**：gen_0 ~ gen_10 完成，gen_11 正在训练，目标 gen_14（T=15）
- **每 generation 耗时**：~67 min（gen_9→gen_10 间隔 4007s）
- **预计剩余**：4 个 generation × 67 min ≈ **4.5 小时**
- **磁盘**：146G/250G 已用，105G 可用，无风险
- **cuda:0**：被占用，不可用

实验正常运行中，无需干预。预计约 4.5 小时后完成，届时可运行 D102 分析。

---
