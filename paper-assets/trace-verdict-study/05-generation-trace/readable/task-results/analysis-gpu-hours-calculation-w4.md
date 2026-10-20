# analysis gpu hours calculation w4

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gpu_hours_calculation_w4_20260518T201553_result.json`
- **Structured JSON:** [`4776b3f6e9f678c053b9.json`](../../sessions/47/4776b3f6e9f678c053b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

- **总 GPU-hours: 322.2h**（Ethics statement 写的 "under 20" 严重低估）
- 115 个实验，102 个有运行时数据
- 按模型：Qwen-7B 235.6h (73.1%), CodeLlama-13B 40.4h (12.5%), DeepSeek-6.7B 30.8h (9.6%), Qwen-1.5B 15.0h (4.7%)
- 按状态：success 169.7h (52.7%), killed 114.9h (35.6%), negative 35.7h (11.1%), failed 2.0h (0.6%)
- killed 实验占 35.6%，主要是早期 Qwen-7B 的 vota/no_trace 迭代被终止重跑

Ethics statement 需要更新为 ~322 GPU-hours（单卡）。报告已注册为 `art_20260518_fa8fa6`。

---
