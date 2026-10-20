# ssh server cleanup and exp001 launch

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_server-cleanup-and-exp001-launch_20260513T175223_result.json`
- **Structured JSON:** [`4a20de555d78f8bac215.json`](../../sessions/4a/4a20de555d78f8bac215.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

vLLM failed as expected, fell back to transformers successfully. Model loaded, generation started (0/439 batches for MMLU's 14042 items). The process is running.

**Summary:**

| Step | Status |
|------|--------|
| 1. Disk cleanup | SKIP (84G free already) |
| 2. Kill GPU processes | DONE (4 PIDs killed, 6 GPUs at 0MiB) |
| 3. Sync 6 code files | DONE (all 6 files verified on remote) |
| 4. Install deps + verify | DONE (rouge-score, nltk, sentence-transformers installed; all 4 scripts pass `--help`) |
| 5. Launch Phase 1 | RUNNING |

**Phase 1 status:**
- PID: `186841`
- Log: `/root/contamcal-irt-calibration/exp001/phase1_paraphrase.log`
- Backend: transformers (vLLM fallback triggered due to duplicate template name bug)
- Model: Qwen2.5-7B-Instruct on GPU 0
- Progress: generating MMLU paraphrases (14042 items, 439 batches)
- Note: transformers mode is sequential per-item, so MMLU alone will take several hours on a single GPU

---
