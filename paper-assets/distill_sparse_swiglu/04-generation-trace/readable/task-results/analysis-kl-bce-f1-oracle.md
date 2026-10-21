# analysis kl bce f1 oracle

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_kl_bce_f1_oracle_20260517T051453_result.json`
- **Structured JSON:** [`b0609c1d8113018fe720.json`](../../sessions/b0/b0609c1d8113018fe720.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Server `westd-34887` is unreachable (connection refused on port 34887). The instance appears to be powered off.

**Script ready**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/kl_bce_f1_oracle.py`

**When server comes back**, deploy and run with:
```bash
# Upload to server
scp artifacts/kl_bce_f1_oracle.py connect.westd.seetacloud.com:/root/distill_sparse_swiglu/scripts/

# Run (GPU needed for model forward pass)
ssh connect.westd.seetacloud.com "cd /root/distill_sparse_swiglu && \
  source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
  CUDA_VISIBLE_DEVICES=0 nohup python -u scripts/kl_bce_f1_oracle.py \
  > ~/runs/distill_sparse_swiglu/kl_bce_f1_oracle.log 2>&1 &"
```

**Script details**:
- Loads LLaMA-3.1-8B, computes per-token magnitude top-k oracle at 50% retain
- KL checkpoint: `checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt`
- BCE checkpoint: searches `bce_isocompute_v3_s42/` dir, falls back to `bce_framework_lr3e3/predictor_bce_gumbel.pt`, falls back to random baseline
- Threshold: `logits > 0` (hard mask, same as inference protocol)
- Output: F1/precision/recall overall + per-layer breakdown → `artifacts/kl_bce_f1_oracle.json`
- 50 C4 validation samples, seq_len=2048, batch_size=2

---
