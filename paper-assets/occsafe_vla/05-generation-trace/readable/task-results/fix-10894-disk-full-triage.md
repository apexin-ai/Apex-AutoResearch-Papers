# fix 10894 disk full triage

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_10894-disk-full-triage_20260527T071434_result.json`
- **Structured JSON:** [`c57c56ccba197f404111.json`](../../sessions/c5/c57c56ccba197f404111.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here's the full diagnostic report.

---

## 1. Experiment Status

| Experiment | GPU | Status | Detail |
|---|---|---|---|
| **full_occ_ln_v2_s1c** | cuda:0 | **RUNNING** | PID 481426, ~step 20k+, 62GB VRAM, started 08:37 CST |
| **full_occ_ln_v2_s2** | cuda:1 | **RUNNING** | PID 481643, ~step 20k+, 62GB VRAM, started 08:37 CST |
| **detach_ln_v2_s0c** | cuda:2 | **CRASHED** | Disk full at 20k checkpoint save (~14:30 CST). GPU idle. **Checkpoint dir already deleted** (by cleanup daemon or externally). |
| **full_occ_ln_v2_s0d** | cuda:3 | **CRASHED** | Same cause and timing. GPU idle. **Checkpoint dir already deleted.** |

None of the 4 experiments are in the registry.

Estimated schedule for running experiments: 30k save ~17:30 CST, 40k ~20:30, 50k ~23:30.

---

## 2. Disk Usage Distribution

**Total: 216G / 250G (87%), 34G free** (was 100% at 14:35, freed by crash cleanup at 15:35)

| Category | Size |
|---|---|
| Checkpoints | ~171G |
| Models (openvla-7b) | 15G |
| Libero datasets | 5.9G |
| Data (modified_libero_rlds) | 2G |
| Other | ~22G |

**Checkpoint breakdown:**

Old completed (each ~15G, only 50k_chkpt):
| Dir | Size | Registry |
|---|---|---|
| ablation_occ_detach_s3_v2 | 15G | DONE/success |
| cutoff_45k_s2_v2 | 15G | — |
| detach_ln_s3 | 15G | — |
| full_occ_ln_s0 | 15G | — |
| full_occ_ln_s3_v2 | 15G | DONE/success |
| mvp_occ_s3_v2 | 15G | DONE/success |
| reverse_cutoff_s2_v2 | 15G | DONE/success |
| vanilla_v2_s1 | 15G | — |
| cutoff_15k_s1 | 0.5G | — |
| **Subtotal** | **~120.5G** | |

Running (each has 10k + 20k checkpoints):
| Dir | Size |
|---|---|
| full_occ_ln_v2_s1c | 30G |
| full_occ_ln_v2_s2 | 30G |

11 empty/abandoned dirs (0-4K each): negligible.

---

## 3. Safe Deletion Candidates

**Tier 1 — Empty/abandoned dirs (~0 space, just cleanup):**
cutoff_25k_s2, reverse_cutoff_s2, full_occ_ln_v2_s0, full_occ_ln_v2_s1, detach_ln_v2_s0, detach_ln_v2_s0b, detach_ln_v2_s1, detach_ln_v2_s1c, full_occ_bn_v2_s1, full_occ_ln_v2_s0b, full_occ_ln_v2_s1b

**Tier 2 — Old completed experiments (need your confirmation on which are fully evaluated):**

| Dir | Size | Notes |
|---|---|---|
| ablation_occ_detach_s3_v2 | 15G | DONE/success in registry |
| cutoff_45k_s2_v2 | 15G | |
| detach_ln_s3 | 15G | |
| full_occ_ln_s0 | 15G | |
| full_occ_ln_s3_v2 | 15G | DONE/success in registry |
| mvp_occ_s3_v2 | 15G | DONE/success in registry |
| reverse_cutoff_s2_v2 | 15G | DONE/success, has 40k+50k |
| vanilla_v2_s1 | 15G | |
| cutoff_15k_s1 | 0.5G | |
| **Total if all deleted** | **~120.5G** | |

---

## 4. Space Projection

**If only 2 experiments continue (no restart):** 34G free is enough. The cleanup daemon (keeps 2 latest chkpts) handles rolling saves. Next save at ~17:30 CST will temporarily use 30G but daemon will reclaim it at next cycle.

**If restarting crashed 2 on GPU 2,3:** Peak usage at overlapping save times could hit ~285G (>250G). **Need to delete at least 60G of old checkpoints** (4 old experiment dirs) before restarting.

---
