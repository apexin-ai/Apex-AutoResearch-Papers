# code metaworld baseline

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_metaworld_baseline_20260524T160423_result.json`
- **Structured JSON:** [`ecd8c76e95915f12ea3f.json`](../../sessions/ec/ecd8c76e95915f12ea3f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 4 phases deployed successfully on westd-38929:

**Phase 1 (Environment):** MetaWorld 3.0.0 installed, eval script transferred, SmolVLA checkpoint + SmolVLM2-500M-Instruct base model downloaded via hf-mirror.com.

**Phase 2 (Baseline):** Complete.
| Task | SR |
|------|-----|
| reach-v3 | 28% (7/25) |
| push-v3 | 24% (6/25) |
| pick-place-v3 | 8% (2/25) |
| drawer-open-v3 | 52% (13/25) |
| assembly-v3 | 20% (5/25) |
| **Overall** | **26.4%** [95% CI: 19.5-34.7%] |

**Phase 3 (Pruning Sweep):** Both running in parallel:
- **Random** (GPU 1, PID 613253): k=0.5 task 2/5 in progress. reach-v3 k=0.5 → 20% SR
- **L2norm** (GPU 3, PID 614338): k=0.5 task 2/5 in progress. reach-v3 k=0.5 → 4% SR

Each sweep runs 4 k_ratios × 5 tasks × 50 episodes. ETA ~60 min.

**Phase 4 (Registry):** 3 entries created:
- `eval_smolvla_metaworld_baseline` → DONE
- `eval_smolvla_metaworld_random_sweep` → RUNNING
- `eval_smolvla_metaworld_l2norm_sweep` → RUNNING

Early signal: L2norm k=0.5 (4% on reach-v3) is performing **worse** than Random k=0.5 (20%), consistent with the scale-invariance hypothesis for Linear connectors.

---
