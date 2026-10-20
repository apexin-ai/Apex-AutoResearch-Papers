# analysis attention normalization entropy

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_attention_normalization_entropy_20260519T024015_result.json`
- **Structured JSON:** [`055973c014d07d90bc2c.json`](../../sessions/05/055973c014d07d90bc2c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated to DONE. Results:

## Token-Count Normalization

| Condition | Group | Text attn (raw) | Image attn (raw) | n_text | n_image | Per-token text | Per-token image | Ratio |
|---|---|---|---|---|---|---|---|---|
| trained | instr-dom 24h | 0.6239 | 0.1883 | 22.2 | 256 | 0.028104 | 0.000736 | **38.2x** |
| trained | control 8h | 0.4490 | 0.2711 | 22.2 | 256 | 0.020225 | 0.001059 | **19.1x** |
| untrained | instr-dom 24h | 0.1148 | 0.8805 | 22.2 | 256 | 0.005171 | 0.003439 | 1.5x |
| untrained | control 8h | 0.1234 | 0.8716 | 22.2 | 256 | 0.005559 | 0.003405 | 1.6x |

## Attention Entropy by Head Group

| Condition | Group | Mean entropy | Std | Normalized |
|---|---|---|---|---|
| trained_2cat | instr-dom 24h | 0.4647 | 0.1080 | 0.6705 |
| trained_2cat | control 8h | 0.5694 | 0.0547 | 0.8215 |
| untrained_2cat | instr-dom 24h | 0.3303 | 0.1230 | 0.4765 |
| untrained_2cat | control 8h | 0.3297 | 0.1796 | 0.4757 |
| trained_3cat | instr-dom 24h | 0.8817 | 0.1363 | 0.8026 |
| trained_3cat | control 8h | 1.0506 | 0.0242 | 0.9563 |

## Key Findings

- **Token asymmetry**: 256 image / 22.2 text = 11.5x
- Even after normalizing for this 11.5x asymmetry, trained instruction-dominant heads show **38.2x** per-token text/image ratio (control heads: 19.1x)
- Untrained baseline: both groups near parity (~1.5x), so the effect is training-induced
- Training amplifies the per-token ratio from 1.5x to 38.2x (**25.5x increase**)
- Instruction-dominant heads have **lower entropy** (0.465) than control heads (0.569), confirming sharper text specialization
- The raw "57.7% attention to text" claim is not an artifact of token count asymmetry

Output saved to `/root/autodl-tmp/vla-ssd/results/attention_normalization_entropy.json`.

---
