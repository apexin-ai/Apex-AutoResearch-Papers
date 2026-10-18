# exp mistral compounding sweep v2

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_mistral_compounding_sweep_v2_20260515T183813_result.json`
- **Structured JSON:** [`051951b200026c4cd17e.json`](../../sessions/05/051951b200026c4cd17e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验启动正常：
- 模型已加载（Mistral-7B-v0.3, 256 KV heads）
- 使用 `mistral_hires_bf16_2bitonly_profiles_wrapped.json`（仅 2-bit + 16-bit，与 Llama 协议一致）
- 9 个 k 值 sweep：0,2,4,8,16,32,64,128,256
- budget=0.25
- WikiText-2 数据集已命中缓存
- 日志：`~/runs/ratekv/mistral_compounding_sweep_v2.log`
- 输出：`/root/ratekv/artifacts/mistral_compounding_sweep_v2_results.json`
- 预计 45-90 分钟完成

---
