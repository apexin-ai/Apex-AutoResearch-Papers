# ssh check fewnerd pt n16 n32 status

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_fewnerd_pt_n16_n32_status_20260522T121332_result.json`
- **Structured JSON:** [`3fa2957e83b272ebad5c.json`](../../sessions/3f/3fa2957e83b272ebad5c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both experiments are **still running**.

## Experiment 1: `exp_fewnerd_pretrained_n16_s42`
| Field | Value |
|-------|-------|
| PID | 392445 |
| Elapsed | 6h 43m |
| GPU | cuda:1 (86% util, 30079/32607 MiB) |
| Progress | **82%** — 494,608 / 602,368 prompts |
| Speed | ~3,727 input toks/s, ~5,669 output toks/s (~32 it/s) |
| ETA | ~107K prompts left ÷ ~32 it/s ≈ **~56 min remaining** |

## Experiment 2: `exp_fewnerd_pretrained_n32_s42`
| Field | Value |
|-------|-------|
| PID | 387491 |
| Elapsed | 8h 01m |
| GPU | cuda:3 (79% util, 29785/32607 MiB) |
| Progress | **49%** — 595,328 / 1,204,736 prompts |
| Speed | ~3,765 input toks/s, ~5,621 output toks/s (~30 it/s) |
| ETA | ~609K prompts left ÷ ~30 it/s ≈ **~5.6 hours remaining** |

## GPU Overview
| GPU | Utilization | VRAM |
|-----|-------------|------|
| 0 | 92% | 30,261 / 32,607 MiB |
| 1 | 86% | 30,079 / 32,607 MiB ← n16 |
| 2 | 94% | 30,173 / 32,607 MiB |
| 3 | 79% | 29,785 / 32,607 MiB ← n32 |

All 4 GPUs are heavily loaded. The n32 experiment has 2× the total prompts (1.2M vs 602K) because `n_samples=32` generates twice as many candidates as `n_samples=16`. The n16 run should finish within the hour; n32 has roughly 5-6 hours to go.

---
