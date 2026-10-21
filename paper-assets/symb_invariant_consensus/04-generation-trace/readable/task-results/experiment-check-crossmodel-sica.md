# experiment check crossmodel sica

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_check-crossmodel-sica_20260521T090909_result.json`
- **Structured JSON:** [`5b6ef34358e64c1a1ac8.json`](../../sessions/5b/5b6ef34358e64c1a1ac8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态：进行中

**exp-d126-crossmodel-sica** 正在 westd-16639 上运行。

| 指标 | 值 |
|------|------|
| 进度 | **8/204** (~3.9%) |
| 启动时间 | 16:40 (今天) |
| 每样本耗时 | ~4 分钟 |
| 剩余 | 196 样本 × 4 min ≈ **13 小时** |
| 预计完成 | **~明天 06:00 (May 22)** |

**服务状态：**
- Mistral-7B (port 8000, cuda:0) — 运行中
- Qwen3-14B (port 8001, cuda:1) — 运行中
- 实验脚本 PID 414515 — 运行中

**当前处理：** 第 8 个样本 `ProofWriter_RelNoneg-OWA-D5-487_Q19`，正在做 Qwen3→Mistral cross-extraction。

**目录结构已生成：**
- `mistral_traces/` — Mistral 推理 trace
- `extraction_mistral_same/` — Mistral 同模型约束提取
- `extraction_mistral_cross_qwen3/` — Mistral→Qwen3 跨模型提取
- `extraction_qwen3_same/` — Qwen3 同模型提取
- `extraction_qwen3_cross_mistral/` — Qwen3→Mistral 跨模型提取

实验运行正常，无需干预。预计明天凌晨完成后再来收割结果。

---
