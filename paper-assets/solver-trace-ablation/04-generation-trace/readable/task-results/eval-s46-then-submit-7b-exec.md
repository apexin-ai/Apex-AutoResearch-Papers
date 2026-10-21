# eval s46 then submit 7b exec

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_s46-then-submit-7b-exec_20260516T091847_result.json`
- **Structured JSON:** [`2d722b90493e81825841.json`](../../sessions/2d/2d722b90493e81825841.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Training PID is **799959**, running on cuda:0 only.

---

## Summary

### Step 1: s46 eval_sta results
| Metric | Value |
|--------|-------|
| Prove rate | **43/100 (43.0%)** |
| Mean ISR | 0.0061 |
| Proved-only ISR | 0.0143 |

### Step 2: classify_h7 taxonomy
| Category | Count | % of proved |
|----------|-------|-------------|
| Proved | 43 | - |
| H7a (text-match tautology) | 3 | 7.0% |
| H7b (obfuscated tautology) | 0 | 0.0% |
| H1 strict (concl in premises) | 39 | 90.7% |
| H8 (conj-collapse) | 4 | 9.3% |
| **Genuine** | **1** | **2.3%** |

Per C013 taxonomy: genuine = proved(43) − H7(3) − H1_exact(39) − H8(4) = **1** (some overlap between categories, net genuine = 1).

### Step 3: 7B (Qwen3-8B) exec-only pilot
- **Successfully launched** on cuda:0, tmux session `w2-qwen3-8b-exec-pilot`
- PID: 799959
- GPU memory: 48.6 GB / 97.9 GB (well within budget)
- Step 1 completed at 31.5s/step, prove_rate=0.500, reward=0.5000
- Config: `grpo_exec_only_8b.yaml` (batch=2, grad_accum=4, gradient_checkpointing, adamw_bnb_8bit)
- ETA: ~4.4 hours for 500 steps

---
