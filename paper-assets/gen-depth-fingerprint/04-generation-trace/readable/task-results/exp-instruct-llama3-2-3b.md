# exp instruct llama3 2 3b

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_instruct-llama3-2-3b_20260518T034629_result.json`
- **Structured JSON:** [`c4c972e183fed1608f67.json`](../../sessions/c4/c4c972e183fed1608f67.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Server remains unreachable. The AutoDL instance has likely hibernated or had a network disruption. 

**Status report for exp_054:**

**Completed:**
- Downloaded Llama-3.2-3B-Instruct via ModelScope to `/root/autodl-tmp/models/Llama-3.2-3B-Instruct-ms/LLM-Research/Llama-3___2-3B-Instruct`
- Generation started in tmux session `exp054` using `generate_chain_instruct.py` (497 seeds, shard 0/2)
- ~292/497 seeds (~59%) completed before connection loss
- Eval script prepared at `/root/gen-depth-fingerprint/eval_exp054_instruct_llama.py`

**If the server instance hibernated (GPU processes killed):**
- The script has **resume support** — when restarted, it skips already-completed seeds
- ~292 seeds should already be saved in `data/llama-3.2-3b-instruct/generations_shard0.jsonl`

**Next steps when server comes back:**
1. Check if tmux `exp054` is still running or if generation completed
2. If interrupted, resume generation: same command, it auto-skips done seeds
3. Run feature extraction:
   ```bash
   /root/miniconda3/bin/python extract_features.py --input data/llama-3.2-3b-instruct/generations_shard0.jsonl --output data/features_llama-3.2-3b-instruct.csv --device cuda:0
   ```
4. Run evaluation:
   ```bash
   /root/miniconda3/bin/python eval_exp054_instruct_llama.py
   ```

**Reference baseline (Llama-3.2-3B base):** binary F1=0.697, Spearman ρ all negative except entropy_max (+0.0859). Both Qwen and OLMo instruct variants showed massive direction reversals (negative → positive ρ).

---
