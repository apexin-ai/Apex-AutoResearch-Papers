# ops mmlu fullitem tau

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_mmlu_fullitem_tau_20260517T133905_result.json`
- **Structured JSON:** [`dbec73c943504039a217.json`](../../sessions/db/dbec73c943504039a217.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Running successfully:
- **20 models x 14,042 items** (1.5B: 8, 3B: 12)
- 4 chains, ~1.2s/iteration warmup
- Estimated: 4 chains x 2000 iters x 1.2s ≈ 40 min per chain (parallel), total ~40-80 min

Key details:
- **Script**: `/root/contamcal-irt-calibration/exp006/compute_vanilla_2pl_tau_fullitems.py`
- **Stan model**: `stan_models/vanilla_2pl_noll.stan` (no log_lik, avoids 280k-entry output that crashed the previous run)
- **tmux session**: `vanilla_2pl_full`
- **Log**: `/root/autodl-tmp/exp006/vanilla_2pl_tau_fullitems.log`
- **Output**: `/root/autodl-tmp/exp006/vanilla_2pl_tau_fullitems.json`
- **Scales**: ['1.5B', '3B'] only (0.5B excluded)
- **PID**: running in tmux, CPU-only task

Estimated completion: ~60-90 min from now (~22:45-23:15 server time).

---
