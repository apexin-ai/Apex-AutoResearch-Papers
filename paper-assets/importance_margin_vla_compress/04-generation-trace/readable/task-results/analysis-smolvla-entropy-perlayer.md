# analysis smolvla entropy perlayer

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_smolvla_entropy_perlayer_20260518T063522_result.json`
- **Structured JSON:** [`2a6633aa787cfb8ccbb9.json`](../../sessions/2a/2a6633aa787cfb8ccbb9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Experiment complete. Here's the summary:

**SmolVLA Per-Layer Attention Entropy Results** (256 LIBERO images, 9 tasks, 16 VLM layers):

| Layer | Entropy Ratio | Std | Vision Attn Frac |
|-------|-------------|-----|-----------------|
| L0 | 0.979 | 0.005 | 0.585 |
| L4 | 0.927 | 0.020 | 0.418 |
| L7 | 0.958 | 0.010 | 0.549 |
| L13 | 0.917 | 0.019 | 0.557 |
| L15 | 0.953 | 0.013 | 0.651 |
| **Overall** | **0.944** | **0.020** | — |

**Key finding**: SmolVLA entropy stays flat at **0.92-0.98** across all 16 layers (range = 0.06). This is a stark contrast to OpenVLA's progressive sharpening from 0.98 → 0.48 (range = 0.50). The hypothesis is confirmed: pixel-shuffle creates uniformly high attention entropy at every depth, meaning no layer naturally identifies redundant vision tokens for pruning.

Script saved at `measure_smolvla_entropy_perlayer.py`, results at `eval_results/smolvla_attention_entropy_perlayer.json`.

---
