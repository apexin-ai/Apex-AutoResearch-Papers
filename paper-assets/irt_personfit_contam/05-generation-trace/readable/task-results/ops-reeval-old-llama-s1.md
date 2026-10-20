# ops reeval old llama s1

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_reeval-old-llama-s1_20260523T124931_result.json`
- **Structured JSON:** [`5a31d6ae071a0022cc8e.json`](../../sessions/5a/5a31d6ae071a0022cc8e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

The eval is progressing but very slowly due to GPU contention (4 processes sharing GPU 3). Here's the current status:

**Setup completed:**
- Symlinks created: `ctrl_contam_pilot/checkpoints/llama/contam_15_s1` → old `contam_15` checkpoint
- Symlinks created: `ctrl_contam_pilot/checkpoints/llama/contam_50_s1` → old `contam_50` checkpoint
- Both evals running sequentially via `/tmp/run_eval_s1.sh` (PID 136059, child Python PID 136064)

**Current progress:**
- **contam_15_s1**: 5500/14042 items (~39%), accuracy ~63.8%
- **contam_50_s1**: queued (runs after 15% finishes)
- Rate: ~500 items per 12 min (GPU 3 shared with 3 training jobs)

**Estimated remaining time:**
- contam_15_s1: ~3.4 hours to finish
- contam_50_s1: ~5.6 hours after that
- Total: ~9 hours

**How to check later:**
```bash
# Check progress
grep "acc=" /tmp/eval_contam15_s1.log
grep "acc=" /tmp/eval_contam50_s1.log

# Check if done
cat /tmp/eval_s1_status.log

# Read results when done
cat /root/autodl-tmp/ctrl_contam_pilot/results/llama/contam_15_s1_results.json
cat /root/autodl-tmp/ctrl_contam_pilot/results/llama/contam_50_s1_results.json
```

**Cohen's d formula** (to compute when results are ready):
```
d = (lz*_contam - (-0.312)) / 0.840
```
where clean baseline: mean=-0.312, std=0.840

The eval is running correctly and will complete on its own. The process is using `nohup` so it persists across SSH disconnects.

---
