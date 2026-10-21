# analysis qwen14b mask divergence

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen14b-mask-divergence_20260519T065150_result.json`
- **Structured JSON:** [`b6a792650e15945dbd80.json`](../../sessions/b6/b6a792650e15945dbd80.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Analysis complete. Results summary:

## Per-layer Jaccard Divergence (KL mask vs Magnitude mask, 30% sparsity)

| Metric | Qwen-14B (48L) | LLaMA-8B (32L) |
|--------|---------------|----------------|
| Mean Jaccard | **0.4016** | **0.3939** |
| Std | 0.0756 | 0.0314 |
| Max J (layer) | 0.446 (L11) | 0.482 (L0) |
| Min J (layer) | 0.063 (L4) | 0.353 (L14) |
| First quarter | 0.334 | 0.440 |
| Middle half | 0.427 | 0.376 |
| Last quarter | 0.419 | 0.384 |

**Key findings for reviewer response:**

1. **Cross-scale consistency**: Both models show ~0.40 mean Jaccard divergence, confirming the predictor discovers non-trivial patterns that differ substantially from magnitude pruning across architectures (LLaMA vs Qwen) and scales (8B vs 14B).

2. **Per-layer profiles differ by architecture**: LLaMA-8B shows a smooth gradient (highest divergence at early layers, decreasing toward middle). Qwen-14B shows a V-shaped pattern with anomalously low divergence at L3-6 (especially L4=0.063), suggesting early Qwen layers' KL-important neurons happen to align with high-magnitude neurons.

3. **Qwen-14B has more heterogeneous layer behavior** (std 0.076 vs 0.031), consistent with its deeper architecture having more specialized layer roles.

4. **The ~40% Jaccard distance means ~60% of kept neurons agree** between KL and magnitude masks, while ~40% are uniquely selected by each method. This validates that the predictor learns importance patterns not reducible to activation magnitude.

Results saved to `westd-34887:results/qwen14b_mask_divergence_30pct.json` and `results/llama8b_mask_divergence_30pct.json`.

---
