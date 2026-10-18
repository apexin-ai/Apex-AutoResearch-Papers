# exp qwen compounding sweep v2

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_qwen_compounding_sweep_v2_20260515T184907_result.json`
- **Structured JSON:** [`3b50f8c2029b6a7d61a9.json`](../../sessions/3b/3b50f8c2029b6a7d61a9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成：

1. **cuda:1 空闲** — 双卡均 0 MiB 占用
2. **生成 `qwen7b_hires_bf16_2bitonly_profiles.json`** — 从 `hires_profiles.json` 提取仅 2-bit 条目，28 层 × 4 heads = 112 KV head，格式与 Llama 2bitonly 一致
3. **实验 `qwen_compounding_sweep_v2` 已提交** — cuda:1, k_values=[0,2,4,8,16,32,64,128,256], budget=0.25, timeout=3h
4. **Registry 已更新为 RUNNING**，spec 含完整 provenance

---
