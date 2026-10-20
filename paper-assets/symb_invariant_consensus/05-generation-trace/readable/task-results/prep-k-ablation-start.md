# prep k ablation start

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_k-ablation-start_20260516T192219_result.json`
- **Structured JSON:** [`2afc71d0cddf55b11d6d.json`](../../sessions/2a/2afc71d0cddf55b11d6d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Everything verified. Here's the report:

```
VLLM_STATUS: running (PID=174298, Qwen2.5-14B-Instruct, max_model_len=8192)
DATA_PW: /root/symb_invariant_consensus/data/proofwriter_30.json (30 problems)
DATA_FOLIO: /root/symb_invariant_consensus/data/folio_30.json (30 problems)
COMMAND: bash /root/symb_invariant_consensus/scripts/run_k_ablation.sh
EST_GPU_H: ~5.8h (D012 K=12 took 58min for 60 problems × 6 K-values, but cost scales ~linearly with K; weighted avg ≈ 58min × (6+8+11+12+16+20)/(12×6) ≈ 58min × 1.01 per run → ~5.8h total)
```

**Notes:**
- Script is at `/root/symb_invariant_consensus/scripts/run_k_ablation.sh`, chmod +x done
- D012 baseline (K=12, 60 problems) took 3500s. Since LLM calls scale linearly with K, the 6 runs will take roughly: K6≈29min, K8≈39min, K11≈53min, K12≈58min, K16≈77min, K20≈97min → **total ~5.9h**
- `--seed 42` added for reproducibility
- Ready for `submit_training_job` with command: `bash /root/symb_invariant_consensus/scripts/run_k_ablation.sh`

---
