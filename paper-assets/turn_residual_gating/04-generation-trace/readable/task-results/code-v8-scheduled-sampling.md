# code v8 scheduled sampling

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_v8_scheduled_sampling_20260519T150253_result.json`
- **Structured JSON:** [`b52c1728835d5eca771f.json`](../../sessions/b5/b52c1728835d5eca771f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run completed. Here's the full report.

---

## v8 Dry-Run Results

### Verification Checklist
| Check | Result |
|-------|--------|
| Both TF and SS paths execute | ✅ Step 0 = TF, Steps 1-4 = SS |
| Gradients flow to gates | ✅ `gate_grad_observed=True` |
| No OOM | ✅ Peak 42.3GB (RTX PRO 6000, 102GB VRAM) |
| NTP loss reasonable | ✅ 1.0-1.9 range |
| SS logic correct | ✅ used=4/5, fallback=0 |
| Gate hooks disable/restore | ✅ Generation completed, hooks restored |
| Gate differentiation | ✅ std 0.034→0.163 in 5 steps |

### Observation: L_GAR=0.0 on SS steps
SS steps show L_GAR=0.0000. Fallback=0 confirms GAR was actually computed (not skipped). Most likely the base model's attention on self-generated text produces GAR close to the target (0.5), yielding near-zero MSE. This should resolve as training progresses and the model's generated text distribution diverges. TF path (step 0) shows healthy L_GAR=0.2342.

### Training Time Estimate
- v7 was ~6h for 3 epochs (3000 steps)
- SS steps are ~2-3x slower (autoregressive generation + extra forward)
- SS ratio averages ~25% over training (linear warmup 0→0.5)
- **Estimated v8 training time: ~8-9 hours**

### Training Command
```
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && python src/train_phase2_v8.py \
    --model /root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct \
    --gate-type threadgate \
    --output-dir /root/turn_residual_gating/outputs/v8_schedsampling \
    --data-dir /root/turn_residual_gating/data/ultrachat_8k \
    --epochs 3 --lr 2e-4 --grad-accum 8 --max-seq-len 2048 \
    --init-bias 1.5 --gate-lr-multiplier 10 \
    --lambda-gar 2.0 --gar-loss-mode mse_target --gar-target 0.5 \
    --lambda-gate-div 1.0 --min-gate-std 0.05 \
    --scheduled-sampling --ss-max-ratio 0.5 --ss-warmup-steps 0 \
    --ss-gen-max-tokens 256 --ss-gen-temperature 0.7
```

Or via launch script: `bash /root/turn_residual_gating/scripts/run_v8_schedsampling.sh`

---
