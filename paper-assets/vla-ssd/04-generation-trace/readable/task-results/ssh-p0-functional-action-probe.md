# ssh p0 functional action probe

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_p0-functional-action-probe_20260515T232234_result.json`
- **Structured JSON:** [`0c95db7320944d8609ee.json`](../../sessions/0c/0c95db7320944d8609ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifact registered. Here's the complete results summary:

## Action Probe Results (LIBERO-Goal, 10 tasks, 500 demos)

| Model | mean_R² | overall_R² | grip_acc |
|-------|---------|-----------|----------|
| **SigLIP+Projector** | **0.7063** | 0.7169 | 0.9221 |
| VLA Trained image_mean L19 | 0.6832 | 0.6961 | 0.9182 |
| VLA Trained image_mean L23 | 0.5736 | 0.5900 | 0.8924 |
| **LLM (last_preaction) L19** | **0.7309** | 0.7397 | 0.9184 |
| Untrained image_mean best (L0) | 0.7136 | 0.7234 | 0.9218 |

**Gate: PASS** (projector 0.7063 ≥ 0.683 threshold)

**Bootstrap CI** (projector vs LLM L19): delta = -0.0246, 95% CI = [-0.040, -0.009], p = 0.0014

Key observations:
- Projector exceeds the stated 0.683 threshold and beats image_mean at the same layer (0.7063 vs 0.6832 at L19)
- LLM last_preaction L19 is significantly higher (0.7309), indicating the LLM adds action-relevant processing on LIBERO-Goal
- Untrained image_mean L0 = 0.7136 is close to the projector — this is essentially the projector output after one random transformer layer, confirming the visual features already carry strong action information before LLM processing
- Sharp dip at untrained L10-11 (R² ~ 0.03-0.05), possibly due to random weight interference at specific layers

Results saved to `/root/autodl-tmp/vla-ssd/results/functional_validation/action_probe_projector.json`

---
