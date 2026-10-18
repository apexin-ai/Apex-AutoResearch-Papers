# ops pi05 attention entropy

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_pi05-attention-entropy_20260521T103825_result.json`
- **Structured JSON:** [`a450c6803123dfcecdd8.json`](../../sessions/a4/a450c6803123dfcecdd8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results are in. Let me summarize.

## π0.5 Attention Entropy Results

**Overall: 0.6655 ± 0.1576**

Per-layer (18 Gemma-2B layers):
| Layer | Entropy | Std | Vis Frac |
|-------|---------|-----|----------|
| L0 | 0.2251 | 0.0096 | 0.754 |
| L1 | 0.4417 | 0.0185 | 0.790 |
| L2 | 0.5864 | 0.0285 | 0.942 |
| L3 | 0.6630 | 0.0161 | 0.879 |
| L4 | 0.6909 | 0.0213 | 0.891 |
| L5-L8 | 0.58-0.65 | | 0.88-0.92 |
| L9-L13 | 0.65-0.79 | | 0.76-0.95 |
| **L14** | **0.9048** | 0.0064 | 0.916 |
| L15 | 0.8945 | 0.0065 | 0.854 |
| L16 | 0.8751 | 0.0114 | 0.893 |
| L17 | 0.6535 | 0.0129 | 0.723 |

**Cross-model comparison (attention entropy):**
| Model | Connector | Entropy |
|-------|-----------|---------|
| SmolVLA | Pixel-shuffle + cross-attn | 0.9521 |
| **π0.5** | **Linear projection** | **0.6655** |
| X-VLA | Linear projection | 0.6138 |

Key observations:
1. π0.5 entropy (0.6655) is **close to X-VLA** (0.6138), consistent with both using linear projection connectors
2. **Not close to 0.959** as initially expected — the 0.959 value for π0 likely refers to a different metric (possibly L2 norm entropy, which is 0.9997 for π0.5)
3. Per-layer pattern: entropy starts low (0.22) at early layers, peaks at L14 (0.90), then drops at the final layer (0.65)
4. Vision attention fraction is high (72-95%), meaning most attention goes to vision tokens

Results saved to `eval_results/pi05_attention_entropy_perlayer.json` on westd-41074.

---
