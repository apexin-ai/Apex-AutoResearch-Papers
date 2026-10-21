# ssh check warmstart and eval

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-warmstart-and-eval_20260516T164331_result.json`
- **Structured JSON:** [`089ff4f10e971b2afdb7.json`](../../sessions/08/089ff4f10e971b2afdb7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both experiments were already registered as failed by a prior process. Here's the full status report:

---

## Status: Both FAILED

### gated-isr-warmstart-t02-s42 (cuda:0)
- **Stopped at**: step 100/300 (killed externally, no traceback in log)
- **Learning signal**: 4/100 steps with non-zero loss (4%) — essentially zero learning
- **gate_pass**: 0.000 for ALL logged steps — ISR gate blocked every reward
- **Root cause**: ISR always < 0.2 threshold → reward = 0 → grad_norm = 0 → no learning
- **Checkpoint**: DELETED (output dir wiped)

### gated-isr-warmstart-t02-s43 (cuda:1)
- **Crashed at**: step 100/300 — `SafetensorError: No space left on device (os error 28)`
- **Learning signal**: 32/100 steps with non-zero loss (32%) — sparse but real
- **gate_pass**: occasionally > 0 (e.g. step 93: 0.333), peak reward=0.875 at steps 31, 37, 65
- **Root cause**: Disk exhaustion at checkpoint save + ISR gate too strict for consistent signal
- **Checkpoint**: DELETED (output dir wiped)

### Diagnosis

| Factor | s42 | s43 |
|--------|-----|-----|
| Steps with reward > 0 | 3/100 (3%) | 21/100 (21%) |
| Steps with loss ≠ 0 | 4/100 | 32/100 |
| Max ISR observed | 0.125 | 0.625 |
| gate_pass ever > 0 | NO | YES (sparse) |

**Primary failure**: ISR gate threshold τ=0.2 is too strict for the warmstart model. The model generates proofs (prove_rate often > 0.5) but with low ISR scores (mostly < 0.2), so the gate zeros out all reward. This creates total reward collapse — the GRPO objective sees `frac_reward_zero_std=1.0` (all samples get same reward), producing zero gradients.

**Secondary failure**: Disk full (C003 related) — two simultaneous experiments each saving 2 checkpoints (~16GB each) exceeded available space.

### Eval: NOT POSSIBLE
Checkpoints have been deleted. No eval can be performed.

### vs. Success Criteria (PR > 50% AND genuine > 30%)
These experiments cannot meet the criteria — they effectively produced untrained models (zero gradient for almost all steps).

---
