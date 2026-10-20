# code prepare gated isr replication

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare-gated-isr-replication_20260516T184753_result.json`
- **Structured JSON:** [`cdd45fe7ccb7b4ab2cec.json`](../../sessions/cd/cdd45fe7ccb7b4ab2cec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All the information is gathered. Here's the complete report:

---

## Correction: τ=0.2 vs τ=0.15

**The 95.2% genuine result is from `gated-isr-warmstart-t015-s43` (τ=0.15), NOT τ=0.2.** All τ=0.2 warmstart runs failed with gate_pass=0.000 — the warmstarted model couldn't exceed ISR 0.2. Preparing replications of the **τ=0.15** approach.

---

## Existing Configuration (the success)

**`configs/grpo_isr_warmstart_t015.yaml`:**
```yaml
model_path: /root/autodl-tmp/outputs/exec_retrain_v3_s43/checkpoint-200
data_path: data/proofwriter_fol_100.jsonl
reward_mode: isr_gated
isr_threshold: 0.15
min_components: 2
warmup_steps: 0
num_steps: 300
per_device_batch_size: 1
gradient_accumulation_steps: 4
num_generations: 8          # K=8
max_completion_length: 512
learning_rate: 1.0e-6
solver: prover9
gradient_checkpointing: true
save_total_limit: 1
save_steps: 50
no_wandb: true
```

Original command:
```bash
python scripts/train_grpo.py --config configs/grpo_isr_warmstart_t015.yaml --seed 43 --output_dir /root/autodl-tmp/outputs/gated_warmstart_v3_t015_s43
```

---

## Replication 1: τ=0.15 seed=42 (READY)

Warmstart checkpoint EXISTS: `/root/autodl-tmp/outputs/exec_retrain_v3_s42/checkpoint-200`

**Training command:**
```bash
export CUDA_VISIBLE_DEVICES=0
python scripts/train_grpo.py \
  --config configs/grpo_isr_warmstart_t015.yaml \
  --model_path /root/autodl-tmp/outputs/exec_retrain_v3_s42/checkpoint-200 \
  --seed 42 \
  --output_dir /root/autodl-tmp/outputs/gated_warmstart_v3_t015_s42
```

---

## Replication 2: τ=0.15 seed=44 (BLOCKED — needs exec-retrain first)

No `exec_retrain_v3_s44/checkpoint-200` exists. Must first train exec-only baseline:

**Step 1 — Exec retrain (500 steps, ~1hr):**
```bash
export CUDA_VISIBLE_DEVICES=1
python scripts/train_grpo.py \
  --config configs/grpo_exec_retrain.yaml \
  --seed 44 \
  --output_dir /root/autodl-tmp/outputs/exec_retrain_v3_s44 \
  --save_steps 50 \
  --save_total_limit 1
```
(Note: original exec_retrain config has save_total_limit=10 — override to 1 per C003)

**Step 2 — Gated warmstart (300 steps, ~25min):**
```bash
export CUDA_VISIBLE_DEVICES=1
python scripts/train_grpo.py \
  --config configs/grpo_isr_warmstart_t015.yaml \
  --model_path /root/autodl-tmp/outputs/exec_retrain_v3_s44/checkpoint-200 \
  --seed 44 \
  --output_dir /root/autodl-tmp/outputs/gated_warmstart_v3_t015_s44
```

---

## Status & Issues

| Item | Status |
|------|--------|
| Warmstart ckpt s42 | `/root/autodl-tmp/outputs/exec_retrain_v3_s42/checkpoint-200` ✓ |
| Warmstart ckpt s43 | `/root/autodl-tmp/outputs/exec_retrain_v3_s43/checkpoint-200` ✓ |
| Warmstart ckpt s44 | **MISSING** — needs exec-retrain first |
| Data file | `data/proofwriter_fol_100.jsonl` (98KB) ✓ |
| Disk free | 50GB on /root/autodl-tmp |
| Disk per experiment | ~30GB (warmstart output) |
| GPUs | 2x RTX PRO 6000 98GB — currently running eval_sta.py (will free soon) |

**Disk concern:** 50GB free can fit 1 warmstart (~30GB). Running both replications sequentially requires cleaning old outputs between runs, or trimming save_total_limit behavior. If exec-retrain for s44 also needed (~15GB), total footprint = 15 + 30 + 30 = 75GB > 50GB available.

**Recommendation:** After eval finishes, clean `gated_warmstart_v3_t015_s43/checkpoint-300/` subdir (~15GB) to reclaim space, then run s42 first. For s44, can clean s42's checkpoint after eval.

---
