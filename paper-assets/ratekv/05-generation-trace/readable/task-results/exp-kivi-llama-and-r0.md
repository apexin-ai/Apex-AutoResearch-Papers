# exp kivi llama and r0

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_kivi_llama_and_r0_20260515T114602_result.json`
- **Structured JSON:** [`8685cc0876de36bb63f5.json`](../../sessions/86/8685cc0876de36bb63f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 6 个 KIVI eval 完成，artifact 已注册。汇总：

### KIVI Baseline PPL (WikiText-2)

| Model | Bits | r128 (原始) | r0 (公平对比) | Δ |
|-------|------|------------|-------------|---|
| **Qwen2.5-7B** | 2-bit | 12.83 | 13.34 | +0.51 |
| **Qwen2.5-7B** | 4-bit | 9.90 | 9.91 | +0.01 |
| **Llama-3.1-8B** | 2-bit | 9.84 | 10.08 | +0.24 |
| **Llama-3.1-8B** | 4-bit | 8.14 | 8.14 | +0.005 |

**关键发现**：
- **4-bit 几乎不受 residual_length 影响**（Δ < 0.02），r128 的 25% fp16 residual 对 4-bit 没实质帮助
- **2-bit 受影响明显**：Qwen +0.51, Llama +0.24。说明 reviewer 的 concern 有道理——r128 在 2-bit 下确实给了 KIVI 不公平的优势
- r0 结果可直接用于论文中的 strict-budget fair comparison

服务器产出文件：
- `artifacts/kivi_qwen25_7b.json` (r128)
- `artifacts/kivi_llama31_8b_r128.json`
- `artifacts/kivi_qwen25_7b_r0.json`
- `artifacts/kivi_llama31_8b_r0.json`

---
