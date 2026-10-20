# run phi3 nlp control

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_phi3_nlp_control_20260523T231450_result.json`
- **Structured JSON:** [`6399ec557a6d3878810e.json`](../../sessions/63/6399ec557a6d3878810e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifact registered. Here's the summary:

## Phi-3-mini NLP Control — Results

| Metric | Phi-3-mini-instruct | Llama-2-chat |
|--------|-------------------|--------------|
| Layers | 32 | 32 |
| Hidden dim | 3072 | 4096 |
| Params | 3.8B | 7B |
| Samples | 5000 | 5000 |
| Peak R² | 0.1555 (L0) | 0.1555 (L15) |
| Exit R² | 0.1555 (L31) | 0.1555 (L31) |
| **ΔR² (exit collapse)** | **0.0000** | **0.0000** |
| Mean R² | 0.1555 | 0.1553 |

R² profile is completely flat across all 32 layers (range: 0.1552–0.1555), matching the Llama-2-chat control. Both NLP controls show ΔR²=0.000, confirming exit collapse is VLA-specific — text-only LLMs that share the same backbone architectures as VLAs show no R² degradation at exit layers.

Job completed in 2.7 min on westd-19183 cuda:0. Results saved at `/root/autodl-tmp/vla-ssd/results/phi3_nlp_control/summary.json`.

---
