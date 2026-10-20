# ssh mistral deploy continue

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_mistral_deploy_continue_20260524T051833_result.json`
- **Structured JSON:** [`4e4bb046340145ca505a.json`](../../sessions/4e/4e4bb046340145ca505a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

I'm hitting conversation context limits with all this polling. Let me provide my final status report:

**Download progress as of 13:57 CST: 9/14 shards, 43G/~63G (~68%)**

The deploy script (PID 537098) is fully automated on the server and will continue independently. Here's a summary of everything set up:

### Automated pipeline (runs without me):
1. **Download monitor**: Waits for PID 534407 to finish (~20 min remaining)
2. **Validation**: Checks 14/14 shards exist, no .aria2 files
3. **vLLM startup**: `CUDA_VISIBLE_DEVICES=3`, port 8003, AWQ quantization, max-model-len 8192
4. **Health check**: Polls `localhost:8003/v1/models` up to 5 min

### What the next worker needs to do:
1. Check deploy log: `tail -5 /tmp/mistral_deploy.log` — look for `VLLM_READY`
2. Start collect.py:
```bash
cd /root/gated_mfrm_judge_bias/exp001 && \
nohup python collect.py --config configs/config_mistral-large-2_local_n17.yaml --workers 4 > /tmp/collect_mistral_large2_n17.log 2>&1 & echo $!
```
3. Verify: `tail -20 /tmp/collect_mistral_large2_n17.log`
4. Report: nvidia-smi for GPU mem, PID, initial speed

### Fix applied:
- Removed trailing `/` from config model_name to match vLLM's `--model` argument

### Warnings:
- Do NOT kill processes on cuda:0/1/2 (other experiments)
- If `VLLM_FAILED` appears, check cuda:3 for residual processes

---
