# code full 32layer attention analysis

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_full_32layer_attention_analysis_20260517T072443_result.json`
- **Structured JSON:** [`4668050277cc8d9863b0.json`](../../sessions/46/4668050277cc8d9863b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Results saved at `/root/autodl-tmp/vla-ssd/results/attention/full_32layer_attention_summary.json`.

**Sanity check:**
- Trained L1: 24/32, mean_text=0.573 (expected 25/32, 0.577) ✓
- Llama2base L1: 9/32, mean_text=0.363 (expected 9/32, 0.365) ✓
- Untrained L1: 0/32, mean_text=0.078 (expected 0/32, 0.117) — 0/32 matches; mean differs due to different init scheme (in-place normal vs `from_config`)

**Summary table (all 32 layers × 3 conditions):**

```
Layer | trained (n_dom text) | llama2base (n_dom text) | untrained (n_dom text)
L0    |  21/32  0.548        |  10/32  0.417           |   0/32  0.078
L1    |  24/32  0.573        |   9/32  0.363           |   0/32  0.078
L2-4  |   0-4   0.444-0.449  |   0/32  0.372-0.429     |   0/32  0.078
L5-8  |   1-3   0.441-0.460  |   8-12  0.471-0.492     |   0/32  0.078
L9-16 |   3-11  0.455-0.494  |  15-22  0.506-0.579     |   0/32  0.078
L17-23|   1-5   0.410-0.438  |   1-18  0.399-0.528     |   0/32  0.078
L24-30|   6-9   0.417-0.433  |   4-11  0.405-0.473     |   0/32  0.078
L31   |  18/32  0.540        |   8/32  0.330           |   0/32  0.078
```

**Key findings:**
- **Trained** peaks at L0 (21) and L1 (24), with a secondary peak at L31 (18). Mid-layers show moderate instruction attention.
- **Llama2base** peaks in mid-layers (L10: 22, L14: 22, L16: 22), inherited from pretrained language priors. L31 drops to 8.
- **Untrained** is pure uniform attention across all layers (proportional to region length: 256 image tokens dominate).

---
