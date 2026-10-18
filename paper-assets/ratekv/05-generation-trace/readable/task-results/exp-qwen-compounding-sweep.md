# exp qwen compounding sweep

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_qwen_compounding_sweep_20260515T184057_result.json`
- **Structured JSON:** [`a3d069504fd84722f7d9.json`](../../sessions/a3/a3d069504fd84722f7d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。

**状态汇总：**
- 实验 `qwen_compounding_sweep` 已在 westd-37397 cuda:1 上运行（PID 361571）
- 使用 `hires_profiles.json`（bf16 精度，2/4/8 bit，与 Llama/Mistral 一致）
- k_values: 0,2,4,8,16,32,64,128,256，budget=0.25
- 输出：`/root/ratekv/artifacts/qwen_compounding_sweep_results.json`
- Registry 已更新为 RUNNING
- 日志：`~/runs/ratekv/qwen_compounding_sweep.log`
- 预计 45-90 分钟完成

---
