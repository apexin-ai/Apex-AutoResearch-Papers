# Upcoming Eval Commands

All commands run from `/root/autodl-tmp/tax_error_inject_agent` with conda base activated.

```bash
cd /root/autodl-tmp/tax_error_inject_agent
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
```

Helper function to find the final checkpoint:
```bash
find_final_ckpt() {
    local latest_run=$(ls -dt "$1"/v*-*/ 2>/dev/null | head -1)
    echo $(ls -d "$latest_run"/checkpoint-* 2>/dev/null | sort -V | tail -1)
}
```

BASE_MODEL=/root/autodl-tmp/models/Qwen/Qwen3-8B

---

## 1. v4-taxei-seed123 (clean eval)

Checkpoint dir: `checkpoints/mini_taxei_sft_v4_seed123/`
Status: checkpoint-1129 exists (training likely complete)

```bash
CKPT=$(find_final_ckpt checkpoints/mini_taxei_sft_v4_seed123)
CUDA_VISIBLE_DEVICES=0 python eval/recovery.py \
    --model_path "$CKPT" \
    --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B \
    --no_inject \
    --output eval_results/v4_taxei_seed123_eval.json \
    --device cuda:0
```

## 2. v4-random-seed123 (clean eval)

Checkpoint dir: `checkpoints/mini_random_sft_v4_seed123/`
Status: training in progress (no checkpoint yet, only logging.jsonl)

```bash
CKPT=$(find_final_ckpt checkpoints/mini_random_sft_v4_seed123)
CUDA_VISIBLE_DEVICES=1 python eval/recovery.py \
    --model_path "$CKPT" \
    --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B \
    --no_inject \
    --output eval_results/v4_random_seed123_eval.json \
    --device cuda:0
```

## 3. v4-taxei-fixed-inject10 (clean eval)

Checkpoint dir: `output/v4-fixed-inject10/` (NOT checkpoints/taxei_fixed_inject10/)
Status: checkpoint-545 exists in `output/v4-fixed-inject10/v0-20260515-061243/`

```bash
CKPT=$(find_final_ckpt output/v4-fixed-inject10)
CUDA_VISIBLE_DEVICES=2 python eval/recovery.py \
    --model_path "$CKPT" \
    --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B \
    --no_inject \
    --output eval_results/v4_taxei_fixed_inject10_eval.json \
    --device cuda:0
```

## 4. v4-taxei-fixed-inject25 (clean eval)

Checkpoint dir: `output/v4-fixed-inject25/`
Status: training in progress (no checkpoint yet, only logging.jsonl in `v0-20260515-063144/`)

```bash
CKPT=$(find_final_ckpt output/v4-fixed-inject25)
CUDA_VISIBLE_DEVICES=3 python eval/recovery.py \
    --model_path "$CKPT" \
    --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B \
    --no_inject \
    --output eval_results/v4_taxei_fixed_inject25_eval.json \
    --device cuda:0
```

## 5. v4-taxei-fixed-inject50 (clean eval)

Checkpoint dir: TBD (training not yet started)
Data ready: `data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject50.jsonl` (4,358 lines)

```bash
# After training completes, determine the actual output directory:
# CKPT_DIR=output/v4-fixed-inject50  OR  checkpoints/taxei_fixed_inject50
CKPT=$(find_final_ckpt $CKPT_DIR)
CUDA_VISIBLE_DEVICES=0 python eval/recovery.py \
    --model_path "$CKPT" \
    --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B \
    --no_inject \
    --output eval_results/v4_taxei_fixed_inject50_eval.json \
    --device cuda:0
```

---

## Recovery Eval Variants (injection mode)

For any of the above, add `--inject --inject_mode action` or `--inject --inject_mode context` instead of `--no_inject`:

```bash
# Action injection recovery
CUDA_VISIBLE_DEVICES=N python eval/recovery.py \
    --model_path "$CKPT" \
    --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B \
    --inject --inject_mode action \
    --output eval_results/v4_taxei_fixed_inject{RATIO}_recovery_action.json \
    --device cuda:0

# Context injection recovery
CUDA_VISIBLE_DEVICES=N python eval/recovery.py \
    --model_path "$CKPT" \
    --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B \
    --inject --inject_mode context \
    --output eval_results/v4_taxei_fixed_inject{RATIO}_recovery_context.json \
    --device cuda:0
```

---

## Notes

- `CUDA_VISIBLE_DEVICES` maps to physical GPU; `--device cuda:0` is always 0 because the env var remaps it
- GPU whitelist: cuda:0-3 only (constraint C001)
- Task list: eval uses `eval/eval_tasks_47.json` (47 solvable tasks) by default
- Each eval takes ~20-40 min per model on a single 5090
