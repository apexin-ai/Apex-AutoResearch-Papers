# ssh p0 functional action delta probe

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_p0-functional-action-delta-probe_20260515T232553_result.json`
- **Structured JSON:** [`06ecb9b2ec915e5c46c6.json`](../../sessions/06/06ecb9b2ec915e5c46c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All complete. Results summary:

| Source | mean_R² | overall_R² |
|---|---|---|
| **SigLIP+Projector** | 0.1181 | 0.1053 |
| **Trained image_mean L14** | 0.1215 | 0.1091 |
| **Untrained best (L0)** | 0.1174 | 0.1070 |

**Bootstrap CI** (projector - trained L14): delta=-0.0034, 95% CI=[-0.0066, +0.0005], p=0.04

**Key observations:**
- All three are very close (~0.117–0.122), with projector slightly below trained L14
- Untrained best layer is **L0** (0.1174), virtually identical to projector (0.1181) — expected since L0 image_mean in untrained model is essentially the projector output
- The difference between projector and trained L14 is marginally significant (p=0.04) but tiny (Δ=0.003)
- Per-dim R²: position deltas (dz=0.46, dx=0.29, dy=0.25) are most predictable; rotation/gripper are low
- **Gate**: projector (0.1181) < LLM best (0.1215), but the gap is small

**Note**: These image_mean R² values (~0.12) are substantially higher than the last_preaction baselines from MVP-2 (~0.06), because image_mean averages over all visual tokens rather than using a single pre-action token.

Results saved at `/root/autodl-tmp/vla-ssd/results/functional_validation/action_delta_probe_projector.json`. Artifact registered as `art_20260515_393354`.

---
