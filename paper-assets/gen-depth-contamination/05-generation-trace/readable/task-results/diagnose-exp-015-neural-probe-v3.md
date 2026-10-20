# diagnose exp 015 neural probe v3

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_015_neural_probe_v3_20260515T092510_result.json`
- **Structured JSON:** [`8e3fea750e7f613e0a2b.json`](../../sessions/8e/8e3fea750e7f613e0a2b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Diagnosis complete. Here's the full picture:

```json
{
  "root_cause": "Two distinct failures: (1) v2 OOM: old script loaded model inside run_one_dataset() (line 367), combined with concurrent exp-006 process, device_map='auto' reserved 90% GPU → two processes exceeded 24GB. (2) v3 'OOM': actually EXIT_CODE=129 (SIGHUP), SSH session dropped after Qwen-cont completed — Pythia/OLMo never ran, not a real OOM.",
  "error_type": "resource (v2), connectivity (v3)",
  "zombie_processes": [],
  "active_process": {"pid": 108774, "mem_gib": 6.7, "status": "RUNNING — Pythia-1.4B embeddings 86%, Model 1/3, in tmux session exp015"},
  "qwen_cont_results_complete": true,
  "fix_applied": "N/A — a new run is already in progress and healthy",
  "fix_verified": false,
  "rerun_command": "N/A — already running",
  "can_auto_fix": false
}
```

**Key findings:**

1. **No zombie processes.** PID 108774 is an **active, healthy run** (started 17:16, tmux session `exp015`). It's processing all 3 models sequentially: Pythia → OLMo → Qwen-cont.

2. **v3 script memory management is correct:**
   - `del llm, tokenizer; gc.collect(); torch.cuda.empty_cache()` after each model ✓
   - `@torch.no_grad()` on embedding extraction ✓
   - OOM auto-halving works ✓
   - Pythia-1.4B loaded at only 2.63GB, total 6.8GB — well within 24GB budget

3. **Previous "v3 OOM" was actually SIGHUP (EXIT_CODE=129)** — SSH dropped, not an OOM. The run was NOT in tmux before, so SSH disconnect killed it. Current run IS in tmux, so it's safe.

4. **Qwen-cont results are complete and saved** in `artifacts/exp015_neural_probe_results.json` (K\*=3, acc=0.4335). The current run will overwrite with all 3 datasets' results.

5. **ETA**: ~25-30 min remaining (Pythia nearly done → OLMo ~5 min → Qwen-cont ~8 min → MLP training ~10 min).

**Remaining non-critical improvements** (post-run, not urgent):
- `device_map="auto"` reserves 90% GPU — should use explicit `.to(device)` for small models to leave headroom
- No `--skip_completed` flag — Qwen-cont will be re-computed unnecessarily (~8 min waste)

**Recommendation**: Let it finish. Don't touch anything.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "Two distinct failures: (1) v2 OOM: old script loaded model inside run_one_dataset() (line 367), combined with concurrent exp-006 process, device_map='auto' reserved 90% GPU → two processes exceeded 24GB. (2) v3 'OOM': actually EXIT_CODE=129 (SIGHUP), SSH session dropped after Qwen-cont completed — Pythia/OLMo never ran, not a real OOM.",
    "error_type": "resource (v2), connectivity (v3)",
    "zombie_processes": [],
    "active_process": {
      "pid": 108774,
      "mem_gib": 6.7,
      "status": "RUNNING — Pythia-1.4B embeddings 86%, Model 1/3, in tmux session exp015"
    },
    "qwen_cont_results_complete": true,
    "fix_applied": "N/A — a new run is already in progress and healthy",
    "fix_verified": false,
    "rerun_command": "N/A — already running",
    "can_auto_fix": false
  }
}
```

</details>

---
