# code plan006 prolog readiness

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan006-prolog-readiness_20260514T053638_result.json`
- **Structured JSON:** [`8198348a866a4ca2cc8d.json`](../../sessions/81/8198348a866a4ca2cc8d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Report written to `/root/solver-trace-ablation/plan006_readiness_report.txt`.

**Status: NEARLY_READY**

What's ready:
- Training data (`train_500_seed42.jsonl`) — model generates Prolog from NL, same data as FOL experiments
- Config (`grpo_prolog_exec_only.yaml`) — logic_type=prolog, solver=prolog, all settings correct
- Reward function — `train_grpo.py` fully dispatches to `prolog_sta_reward` when logic_type=prolog
- SWI-Prolog 8.4.2 available, solver integration complete (`src/solvers/prolog.py` + factory)
- Disk: 172G free — sufficient
- `save_total_limit=1` hardcoded (C003)
- Multi-seed via CLI override (`--seed N --output_dir ...`)

What's missing:
1. **eval_sta.py Prolog support** — only supports FOL currently. Needed for C004-compliant post-training ISR comparison. ~15-30 min to add. Not a launch blocker.
2. **Dry-run** — both GPUs occupied (GPU 0: 81%, GPU 1: 98%). Recommend running first seed as dry-run (2 steps) before committing all 3.

---
