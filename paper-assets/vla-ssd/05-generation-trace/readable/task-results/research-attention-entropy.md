# research attention entropy

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_attention_entropy_20260517T033742_result.json`
- **Structured JSON:** [`aa8c368d1f74d7934124.json`](../../sessions/aa/aa8c368d1f74d7934124.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results:

## Attention Entropy Analysis (Layer 1)

### 2-category comparison (image vs text/instruction) — fair comparison

| Metric | Trained | Untrained |
|--------|---------|-----------|
| **Mean entropy** | 0.4909 | 0.3301 |
| **Std entropy** | 0.1075 | 0.1393 |
| **Normalized (H/ln2)** | 0.7082 | 0.4763 |
| Max possible | 0.6931 (ln2) | 0.6931 (ln2) |

### 3-category (trained only: bos, image, text)

| Metric | Value |
|--------|-------|
| Mean entropy | 0.9240 |
| Std entropy | 0.1394 |
| Normalized (H/ln3) | 0.8410 |
| Max possible | 1.0986 (ln3) |

### Key finding

**Trained model has significantly higher entropy** (0.491 vs 0.330, +49% relative increase).

- **Untrained**: heads are highly specialized, attending predominantly to image tokens (low entropy, normalized 0.48)
- **Trained**: attention redistributes toward a more balanced image+text split (normalized 0.71)
- Training increases entropy in 28/32 heads; only heads 0, 6, 16, 25 show decreased entropy (they were already relatively balanced or became more text-specialized)

Saved to `/root/autodl-tmp/vla-ssd/results/attention/entropy_analysis.json`.

---
