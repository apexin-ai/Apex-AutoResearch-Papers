# eval c1 s42 code n1

**tbab multi turn** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_c1-s42-code-n1_20260518T105110_result.json`
- **Structured JSON:** [`1678cd7baf7f5f66d76f.json`](../../sessions/16/1678cd7baf7f5f66d76f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Sample 3 done: wrong (score=0, turns=10). Now 4/91. All 3 samples so far are wrong. ~6 min per sample consistent. Process is progressing normally.

Let me let this run and provide a status summary. The eval is running steadily in background.

**Current Status:**
1. **Checkpoint**: `/root/tbab_multi_turn/checkpoints/c1_lora_only_seed42/` (final adapter, 320MB)
2. **Process**: PID 25961, running on westb-25721, `CUDA_VISIBLE_DEVICES=0`
3. **Progress**: 3/91 completed, all wrong (score=0) so far
4. **Rate**: ~6 min/sample
5. **Estimated completion**: ~9 hours from start (~18:55 start → ~03:55 May 19)
6. **GPU memory**: 44GB/98GB (training 28GB + eval 16GB)
7. **Log file**: `/root/tbab_multi_turn/eval/results/c1_s42_code_n1_eval.log`
8. **Results**: will be saved to `/root/tbab_multi_turn/eval/results/c1_s42_code_n1/`
9. **Results so far**: 
   - Sample 1 (HumanEval/105, 8 shards): wrong, score=0, 8 turns
   - Sample 2 (HumanEval/106, 7 shards): wrong, score=0, 7 turns  
   - Sample 3 (HumanEval/109, 10 shards): wrong, score=0, 10 turns

All samples getting score=0 so far is expected for a LoRA-only baseline on code tasks — the model needs to track information across many conversation turns without any special attention mechanism.

The eval will continue running in background and write final metrics (P̄, A90, U10-90) to `summary_lora_only.json` when done. To monitor:
```bash
tail -5 /root/tbab_multi_turn/eval/results/c1_s42_code_n1_eval.log
```

---
