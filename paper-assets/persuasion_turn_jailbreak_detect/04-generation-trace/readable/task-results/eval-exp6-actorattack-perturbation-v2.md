# eval exp6 actorattack perturbation v2

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp6-actorattack-perturbation-v2_20260518T135631_result.json`
- **Structured JSON:** [`906a839a93b1ad9e7710.json`](../../sessions/90/906a839a93b1ad9e7710.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Here's the summary:

**EXP-6 ActorAttack Adversarial Perturbation Results**

| Variant | Clean K1 | Pert K1 | Δ K1 | Clean Full | Pert Full | Δ Full |
|---------|----------|---------|------|------------|-----------|--------|
| 9class | 0.773 | 0.633 | -0.140 | 0.972 | 0.768 | -0.204 |
| binary | 0.765 | 0.639 | -0.126 | 0.994 | 0.640 | -0.353 |
| scrambled | 0.721 | 0.616 | -0.104 | 0.951 | 0.779 | -0.172 |
| jb_mlm | 0.736 | 0.657 | -0.079 | 0.893 | 0.541 | -0.353 |
| wiki_mlm | 0.656 | 0.601 | -0.055 | 0.686 | 0.545 | -0.141 |
| topic | 0.514 | 0.526 | +0.012 | 0.625 | 0.577 | -0.049 |
| vanilla | 0.439 | 0.292 | -0.146 | 0.365 | 0.248 | -0.116 |

**McNemar 9class vs vanilla**: All seeds, all K values: p < 0.001 (both clean and perturbed), direction 9class > vanilla.

**Conclusion: Negative** — Unlike DD OOD (where classification-supervised variants had near-zero perturbation delta), ALL variants show substantial degradation on ActorAttack perturbation (Δ = -0.05 to -0.35). However, 9class still significantly outperforms vanilla even on perturbed data (McNemar all p<0.001).

**Registry updated**: `exp6_actorattack_perturbation` → DONE (negative), `exp2_actorattack_mcnemar` → metrics updated with clean McNemar results.

---
