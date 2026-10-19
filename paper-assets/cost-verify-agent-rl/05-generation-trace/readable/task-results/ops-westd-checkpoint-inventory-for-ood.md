# ops westd checkpoint inventory for ood

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_checkpoint_inventory_for_ood_20260522T015538_result.json`
- **Structured JSON:** [`7cdf20ea911bbed330d2.json`](../../sessions/7c/7cdf20ea911bbed330d2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All HF checkpoints verified with complete model files. Here's the full report:

## Checkpoint Inventory

| Checkpoint | Location | Size | HF Ready? | OOD eval done? |
|---|---|---|---|---|
| **Seed 4** step 15 | westd + bjb1 | 3.8G HF | Yes | **Yes** (30.60%) |
| **Seed 5** step 10 | westd | 25G raw + 3.8G HF | Yes | **No** |
| **Seed 6** step 15 | westd | 25G raw + 3.8G HF | Yes | **No** |
| **Seed 7 high-KL** step 5 | westd + bjb1 | 3.8G HF | Yes | **Yes** (9.70%) |
| **Seed 7 high-KL** step 7 | westd + bjb1 | 3.8G HF | Yes | **Yes** |
| **Seed 8** step 5 | westd | 3.8G HF | Yes | **Yes** (11.94%) |
| **Seed 1** | — | — | — | **Yes** (23.88%) |
| **Intervention C** step 5 | — | — | — | **Yes** (10.45%) |
| **Intervention C** step 7 | — | — | — | **Yes** (14.93%) |
| **Intervention C hard-cap** step 5 | westd | 3.8G HF | Yes | **No** |
| **Intervention C hard-cap** step 7 | westd | 3.8G HF (via raw) | Needs convert | **No** |
| **C'** step 5 | westd + bjb1 | 3.8G HF | Yes | **Yes** (0.0%) |
| **Seed 2** step 15 | — | — | — | **Gone** — no checkpoint on either server |
| **Seed 3** final | westd (empty dir) | 0 | — | **Gone** — empty directory |
| **Seed 7 original** pre-collapse step 5 | — | — | — | **Gone** — only high-KL variant exists |

## Missing (confirmed unrecoverable)
- **Seed 2 step 15**: not found on either server
- **Seed 3 final**: empty directory on westd, absent from bjb1
- **Seed 7 original pre-collapse**: only the high-KL variant checkpoints remain (already OOD eval'd)

## Actionable: OOD eval candidates on westd cuda:0,1

Three checkpoints with HF models ready, no OOD eval yet:

| Priority | Checkpoint | Path on westd |
|---|---|---|
| 1 | **Seed 5 step 10** | `exp029-seed5/global_step_10_hf` |
| 2 | **Seed 6 step 15** | `exp029-seed6/global_step_15_hf` |
| 3 | **Intervention C hard-cap step 5** | `intervention_c_hard_cap_step5_hf` |

(Intervention C hard-cap step 7 has raw checkpoint but no `_hf` — would need conversion first.)

All three priority checkpoints are on westd and ready to run OOD eval on cuda:0,1 right now.

---
