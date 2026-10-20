# eval exp4 dd ood perturbation

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp4-dd-ood-perturbation_20260518T104808_result.json`
- **Structured JSON:** [`ea79c49772b9098d79af.json`](../../sessions/ea/ea79c49772b9098d79af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifact registered (art_20260518_31ad5c). EXP-4 complete. Summary:

**EXP-4: DD OOD Adversarial Perturbation Results**

| Variant | Seeds | K | Clean F1 | Perturbed F1 | Delta |
|---|---|---|---|---|---|
| **9class** | 3 | k1 | 0.9905 | 0.9968 | +0.0063 |
| | | k3 | 0.9719 | 0.9936 | +0.0217 |
| | | full | 0.9968 | 1.0000 | +0.0032 |
| **binary** | 3 | k1 | 0.9936 | 1.0000 | +0.0064 |
| | | k3 | 0.9841 | 1.0000 | +0.0159 |
| | | full | 0.9968 | 1.0000 | +0.0032 |
| **scrambled** | 3 | k1 | 0.9968 | 0.9936 | -0.0032 |
| | | full | 0.9968 | 1.0000 | +0.0032 |
| **jb_mlm** | 3 | k1 | 0.9733 | 0.9733 | 0.0000 |
| | | full | 0.9138 | 0.9409 | +0.0271 |
| **wiki_mlm** | 3 | k1 | 0.9131 | 0.8808 | **-0.0323** |
| | | k2 | 0.9112 | 0.8597 | **-0.0515** |
| | | full | 0.9042 | 0.8715 | **-0.0327** |
| **topic** | 3 | k1 | 0.5912 | 0.6170 | +0.0259 |
| | | full | 0.5412 | 0.5765 | +0.0353 |
| **vanilla** | 1 | k1 | 0.5752 | 0.5205 | **-0.0547** |
| | | full | 0.2845 | 0.2711 | -0.0134 |

Key findings:
- **9class, binary, scrambled, jb_mlm**: Extremely robust to adversarial paraphrasing (delta near 0 or slightly positive across all K values)
- **wiki_mlm**: Only fine-tuned variant showing consistent degradation (delta -0.03 to -0.05), driven entirely by seed42
- **topic**: Low baseline performance but perturbation doesn't hurt much (high variance across seeds)
- **vanilla**: Weak baseline, slight degradation under perturbation

Results saved to server (`results/exp4_dd_ood_perturbation.json`) and registered as artifact `art_20260518_31ad5c`.

---
