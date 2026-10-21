# diagnose exp023 grpo parallel

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp023_grpo_parallel_20260515T041302_result.json`
- **Structured JSON:** [`a9b87b67dcc196b7e341.json`](../../sessions/a9/a9b87b67dcc196b7e341.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Diagnosis and fix complete. Here's the summary:

---

**Root cause**: `textworld.envs.pddl.logic._PARSER` is a module-level singleton `PddlLogicParser` (tatsu). Tatsu parsers are stateful — they maintain buffer position, memoization, etc. When `es_manager.reset()` dispatches multiple `_reset_single` calls via `ThreadPoolExecutor(max_workers=4)`, concurrent threads call `_PARSER.parse()` simultaneously, corrupting internal parser state. This caused both exp022 (`FailedExpectingEndOfText`) and exp023 (`FailedToken`) at the same grammar position.

**Fix**: Added `_TW_LOAD_LOCK = threading.Lock()` in `ragen/env/alfworld/env.py`, wrapping `register_game` + `make` + `alfred_env.reset()` (the PDDL-parse path). The lock serializes only the textworld loading phase; game file selection and post-reset processing remain parallel.

**Validation**: 16/16 parallel val env resets passed (max_workers=4, 20.7s).

**Rerun command**:
```bash
cd /root/cost-verify-agent-rl/RAGEN && nohup python train.py --config-name _alfworld_exp023_grpo_parallel > ~/runs/cost-verify-agent-rl/exp023_grpo_parallel_v2.log 2>&1 &
```

```json
{"root_cause":"textworld.envs.pddl.logic._PARSER is a module-level singleton tatsu parser that is not thread-safe. Concurrent ThreadPoolExecutor workers calling _PARSER.parse() during env.reset() corrupt parser internal state, causing FailedToken/FailedExpectingEndOfText at grammar line 196 (template :: \"take {o} from {r}\")","error_type":"infrastructure","fix_steps":["Added _TW_LOAD_LOCK = threading.Lock() in ragen/env/alfworld/env.py","Wrapped register_game + gym.make + alfred_env.reset() with _TW_LOAD_LOCK to serialize PDDL parsing","Verified: 16/16 parallel val env resets pass with max_workers=4"],"can_auto_fix":true}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "textworld.envs.pddl.logic._PARSER is a module-level singleton tatsu parser that is not thread-safe. Concurrent ThreadPoolExecutor workers calling _PARSER.parse() during env.reset() corrupt parser internal state, causing FailedToken/FailedExpectingEndOfText at grammar line 196 (template :: \"take {o} from {r}\")",
    "error_type": "infrastructure",
    "fix_steps": [
      "Added _TW_LOAD_LOCK = threading.Lock() in ragen/env/alfworld/env.py",
      "Wrapped register_game + gym.make + alfred_env.reset() with _TW_LOAD_LOCK to serialize PDDL parsing",
      "Verified: 16/16 parallel val env resets pass with max_workers=4"
    ],
    "can_auto_fix": true
  }
}
```

</details>

---
