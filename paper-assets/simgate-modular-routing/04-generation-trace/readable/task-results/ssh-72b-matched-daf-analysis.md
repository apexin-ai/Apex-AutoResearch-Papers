# ssh 72b matched daf analysis

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_72b-matched-daf-analysis_20260518T064417_result.json`
- **Structured JSON:** [`8503d27d0930f7f6dfae.json`](../../sessions/85/8503d27d0930f7f6dfae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No `register_artifact` tool available in this session. The artifact file is written and verified.

**Done.** Artifact written to `/root/autodl-tmp/simgate-modular-routing/artifacts/72b_matched_10task_daf.md` on westb-13313.

Core results:
- **10 death-prone tasks** compared across 7B (205 episodes) and 72B (235 episodes)
- **DAF is scale-independent**: 100% → 97.5% (ep-weighted), with 8/10 tasks at perfect 100% at both scales
- **Death rates drop with scale**: internal 51.2% → 33.2%, deterministic 19.5% → 3.0%
- **No dominance shifts**: all death-dominated tasks remain death-dominated at 72B
- The 2 sub-100% tasks (identify-life-stages-2 at 87.5%, measure-melting-point at 90%) each have only 1 score-driven label out of 8-10 decisive episodes

---
