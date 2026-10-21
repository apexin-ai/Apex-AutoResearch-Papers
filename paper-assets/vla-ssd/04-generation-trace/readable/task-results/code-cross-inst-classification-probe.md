# code cross inst classification probe

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cross_inst_classification_probe_20260516T235147_result.json`
- **Structured JSON:** [`fe4b812b991e481a8584.json`](../../sessions/fe/fe4b812b991e481a8584.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done. Results:

## Classification Results (10-way, chance = 10%)

### Trained Model

| Position | L0 | L8 | L16 | L24 | L31 |
|----------|----|----|-----|-----|-----|
| **image_mean** | 10.0% | 10.0% | 10.0% | 10.0% | 9.6% |
| **last_preaction** | 10.0% | **100%** | **100%** | **100%** | **100%** |

### Untrained Model

| Position | L0 | L8 | L16 | L24 | L31 |
|----------|----|----|-----|-----|-----|
| **image_mean** | 10.0% | 10.0% | 10.0% | 10.0% | 10.0% |
| **last_preaction** | 10.0% | 98.2% | 92.3% | 86.4% | 82.0% |

### DINOv2 baseline: 10.0% (chance)

Key findings:
- **image_mean** never encodes instruction identity (always at chance) — visual tokens are purely visual regardless of instruction
- **last_preaction in trained model** hits perfect 100% classification from L8 onward — the action token perfectly encodes which instruction was given, and this generalizes across unseen tasks
- **last_preaction in untrained model** also classifies well (98.2% at L8), but accuracy *degrades* in deeper layers (down to 82% at L31) — the random projection head diffuses the signal. In contrast, training makes the instruction encoding stronger and perfectly maintained through all layers

Results saved to `/root/autodl-tmp/vla-ssd/results/cross_instruction/classification_results.json`.

---
