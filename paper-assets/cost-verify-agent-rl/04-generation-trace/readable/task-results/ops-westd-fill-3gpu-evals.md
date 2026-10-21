# ops westd fill 3gpu evals

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_fill_3gpu_evals_20260522T122601_result.json`
- **Structured JSON:** [`fbdc5c82470a6d7116a3.json`](../../sessions/fb/fbdc5c82470a6d7116a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here's the situation after thorough exploration:

**All 4 GPUs on westd are idle** — the c_prime eval on GPU 1 already finished (11.94% success).

**All HF checkpoints on westd have been OOD eval'd:**

| Checkpoint | OOD Success | Status |
|---|---|---|
| seed4_step15 | done | ✓ |
| seed5_step10 v2 | 25.37% | just finished |
| seed6_step15 | done | ✓ |
| seed8_step5 | 13.43% (v2) | just finished |
| seed2048_step5 | done | ✓ |
| intervention_c step5/step7 | done | ✓ |
| high_kl step5/step7 | done | ✓ |
| SFT baseline v3 | done | ✓ |
| c_prime_step5 | 11.94% | just finished |

**Only 1 remaining candidate:**
- **seed2_step15** — FSDP checkpoint exists at `/root/autodl-tmp/cost-verify-agent-rl/backups/exp029-seed2-bjb1/exp029-seed2/global_step_15/actor/` but has NO HF conversion. Needs FSDP→HF conversion before eval.

**Cannot eval:**
- seed3: checkpoint directory is empty (permanently lost as expected)
- seed42: on bjb1, not on westd
- No other unconverted FSDP steps exist (each seed only kept its final step)

**I cannot start 3 OOD evals** because there's at most 1 unconverted checkpoint remaining. Want me to:
1. Convert seed2_step15 FSDP→HF and run that eval?
2. Transfer seed42 from bjb1 to westd?
3. Something else?

---
