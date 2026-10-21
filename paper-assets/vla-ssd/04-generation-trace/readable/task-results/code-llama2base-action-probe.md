# code llama2base action probe

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama2base_action_probe_20260517T204531_result.json`
- **Structured JSON:** [`914a86e36e971b4b1adc.json`](../../sessions/91/914a86e36e971b4b1adc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4/10 done. Continuing at ~5 min/task. ~30 min left for remaining 6 tasks + probe training. Job is running well on its own, within the time budget.

The job is submitted via `submit_training_job` with tmux session `llama2base_action_probe` on westd-19183, cuda:1.

**Status summary:**
- Script: `/root/vla-ssd/scripts/llama2base_action_probe.py`
- Phase 1 (feature extraction): 4/10 tasks completed, ~30 min remaining
- Phase 2 (probe training): will run automatically after extraction, ~5 min for 33 layers
- Output: `/root/autodl-tmp/vla-ssd/results/action_probe/llama2base_action_probe.json`
- Log: `~/runs/vla-ssd/llama2base_action_probe.log`
- ETA: ~35-40 min total remaining (~1h total runtime)

The script will:
1. Extract features to H5 files (image_mean + last_preaction at all 33 layers)
2. Train MLP(4096->256->7) probes per layer with image_mean readout
3. Save results with per-task R², comparison with trained/untrained from existing data
4. Print full 33-layer comparison table at the end

---
