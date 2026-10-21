# Plan 017: Cross-seed Budget Curve (tail-512 x 4 models x 2 seeds)

**Condition**: `full_trace_tail_512`
**Seeds**: 123, 456 (seed42 already done)
**Server**: westd-11235
**GPU**: 0 (single GPU per job)
**Total experiments**: 8

> Note: Existing Qwen-7B seed42 (`full_trace_tail_seed42`) used condition `full_trace_tail`, not `full_trace_tail_512`. New seeds use `full_trace_tail_512` for cross-model consistency. Verify this is acceptable before launching.

---

## 1. qwen7b_full_trace_tail512_seed123

- **exp_id**: qwen7b_full_trace_tail512_seed123
- **server**: westd-11235
- **gpu**: 0
- **estimated_hours**: 2.5 (train ~2.2h + eval ~0.3h)
- **command**:
```bash
bash -c 'export CUDA_VISIBLE_DEVICES=0 && /root/miniconda3/bin/python /root/trace-verdict-study/train/train_sft.py \
  --condition full_trace_tail_512 \
  --model_path /root/trace-verdict-study/models/Qwen2.5-Coder-7B-Instruct \
  --seed 123 \
  --gradient_checkpointing \
  --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_full_trace_tail512_seed123/ \
  --wandb_run_name qwen7b_full_trace_tail512_seed123 \
&& /root/miniconda3/bin/python /root/trace-verdict-study/eval/evaluate.py \
  --condition full_trace_tail_512 \
  --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_full_trace_tail512_seed123/final \
  --model_path /root/trace-verdict-study/models/Qwen2.5-Coder-7B-Instruct \
  --save_predictions'
```

---

## 2. qwen7b_full_trace_tail512_seed456

- **exp_id**: qwen7b_full_trace_tail512_seed456
- **server**: westd-11235
- **gpu**: 0
- **estimated_hours**: 2.5
- **command**:
```bash
bash -c 'export CUDA_VISIBLE_DEVICES=0 && /root/miniconda3/bin/python /root/trace-verdict-study/train/train_sft.py \
  --condition full_trace_tail_512 \
  --model_path /root/trace-verdict-study/models/Qwen2.5-Coder-7B-Instruct \
  --seed 456 \
  --gradient_checkpointing \
  --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_full_trace_tail512_seed456/ \
  --wandb_run_name qwen7b_full_trace_tail512_seed456 \
&& /root/miniconda3/bin/python /root/trace-verdict-study/eval/evaluate.py \
  --condition full_trace_tail_512 \
  --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_full_trace_tail512_seed456/final \
  --model_path /root/trace-verdict-study/models/Qwen2.5-Coder-7B-Instruct \
  --save_predictions'
```

---

## 3. deepseek_full_trace_tail512_seed123

- **exp_id**: deepseek_full_trace_tail512_seed123
- **server**: westd-11235
- **gpu**: 0
- **estimated_hours**: 1.5 (train ~1.2h + eval ~0.3h)
- **command**:
```bash
bash -c 'export CUDA_VISIBLE_DEVICES=0 && /root/miniconda3/bin/python /root/trace-verdict-study/train/train_sft.py \
  --condition full_trace_tail_512 \
  --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct \
  --seed 123 \
  --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace_tail512_seed123/ \
  --wandb_run_name deepseek_full_trace_tail512_seed123 \
&& /root/miniconda3/bin/python /root/trace-verdict-study/eval/evaluate.py \
  --condition full_trace_tail_512 \
  --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace_tail512_seed123/final \
  --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct \
  --save_predictions'
```

---

## 4. deepseek_full_trace_tail512_seed456

- **exp_id**: deepseek_full_trace_tail512_seed456
- **server**: westd-11235
- **gpu**: 0
- **estimated_hours**: 1.5
- **command**:
```bash
bash -c 'export CUDA_VISIBLE_DEVICES=0 && /root/miniconda3/bin/python /root/trace-verdict-study/train/train_sft.py \
  --condition full_trace_tail_512 \
  --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct \
  --seed 456 \
  --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace_tail512_seed456/ \
  --wandb_run_name deepseek_full_trace_tail512_seed456 \
&& /root/miniconda3/bin/python /root/trace-verdict-study/eval/evaluate.py \
  --condition full_trace_tail_512 \
  --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace_tail512_seed456/final \
  --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct \
  --save_predictions'
```

---

## 5. qwen15b_full_trace_tail512_seed123

- **exp_id**: qwen15b_full_trace_tail512_seed123
- **server**: westd-11235
- **gpu**: 0
- **estimated_hours**: 0.4 (train ~0.25h + eval ~0.1h)
- **command**:
```bash
bash -c 'export CUDA_VISIBLE_DEVICES=0 && /root/miniconda3/bin/python /root/trace-verdict-study/train/train_sft.py \
  --condition full_trace_tail_512 \
  --model_path /root/trace-verdict-study/models/Qwen2.5-Coder-1.5B-Instruct \
  --seed 123 \
  --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_tail512_seed123/ \
  --wandb_run_name qwen15b_full_trace_tail512_seed123 \
&& /root/miniconda3/bin/python /root/trace-verdict-study/eval/evaluate.py \
  --condition full_trace_tail_512 \
  --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_tail512_seed123/final \
  --model_path /root/trace-verdict-study/models/Qwen2.5-Coder-1.5B-Instruct \
  --save_predictions'
```

---

## 6. qwen15b_full_trace_tail512_seed456

- **exp_id**: qwen15b_full_trace_tail512_seed456
- **server**: westd-11235
- **gpu**: 0
- **estimated_hours**: 0.4
- **command**:
```bash
bash -c 'export CUDA_VISIBLE_DEVICES=0 && /root/miniconda3/bin/python /root/trace-verdict-study/train/train_sft.py \
  --condition full_trace_tail_512 \
  --model_path /root/trace-verdict-study/models/Qwen2.5-Coder-1.5B-Instruct \
  --seed 456 \
  --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_tail512_seed456/ \
  --wandb_run_name qwen15b_full_trace_tail512_seed456 \
&& /root/miniconda3/bin/python /root/trace-verdict-study/eval/evaluate.py \
  --condition full_trace_tail_512 \
  --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_tail512_seed456/final \
  --model_path /root/trace-verdict-study/models/Qwen2.5-Coder-1.5B-Instruct \
  --save_predictions'
```

---

## 7. codellama13b_full_trace_tail512_seed123

- **exp_id**: codellama13b_full_trace_tail512_seed123
- **server**: westd-11235
- **gpu**: 0
- **estimated_hours**: 2.2 (train ~1.8h + eval ~0.4h)
- **command**:
```bash
bash -c 'export CUDA_VISIBLE_DEVICES=0 && /root/miniconda3/bin/python /root/trace-verdict-study/train/train_sft.py \
  --condition full_trace_tail_512 \
  --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf/ \
  --seed 123 \
  --gradient_checkpointing \
  --label_only_loss \
  --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_full_trace_tail512_seed123/ \
  --wandb_run_name codellama13b_full_trace_tail512_seed123 \
&& /root/miniconda3/bin/python /root/trace-verdict-study/eval/evaluate.py \
  --condition full_trace_tail_512 \
  --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_full_trace_tail512_seed123/final \
  --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf/ \
  --save_predictions'
```

---

## 8. codellama13b_full_trace_tail512_seed456

- **exp_id**: codellama13b_full_trace_tail512_seed456
- **server**: westd-11235
- **gpu**: 0
- **estimated_hours**: 2.2
- **command**:
```bash
bash -c 'export CUDA_VISIBLE_DEVICES=0 && /root/miniconda3/bin/python /root/trace-verdict-study/train/train_sft.py \
  --condition full_trace_tail_512 \
  --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf/ \
  --seed 456 \
  --gradient_checkpointing \
  --label_only_loss \
  --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_full_trace_tail512_seed456/ \
  --wandb_run_name codellama13b_full_trace_tail512_seed456 \
&& /root/miniconda3/bin/python /root/trace-verdict-study/eval/evaluate.py \
  --condition full_trace_tail_512 \
  --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_full_trace_tail512_seed456/final \
  --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf/ \
  --save_predictions'
```

---

## GPU Time Budget Summary

| Model | Per-run (h) | x2 seeds | Subtotal |
|---|---|---|---|
| Qwen-7B | 2.5 | 2 | 5.0h |
| DeepSeek-6.7B | 1.5 | 2 | 3.0h |
| Qwen-1.5B | 0.4 | 2 | 0.8h |
| CodeLlama-13B | 2.2 | 2 | 4.4h |
| **Total (sequential)** | | | **13.2h** |

Estimates based on seed42 checkpoint timestamps (checkpoint-148 to checkpoint-444 delta, extrapolated to full 3-epoch training + standalone eval).

## Recommended Execution Order

Run smaller/faster jobs first to get early signal:
1. qwen15b seed123 + seed456 (0.8h total)
2. deepseek seed123 + seed456 (3.0h total)
3. qwen7b seed123 + seed456 (5.0h total)
4. codellama13b seed123 + seed456 (4.4h total)

## Constraints Applied

- C001: N/A (no paper edits)
- C002: `/root/miniconda3/bin/python` (not bare python), Qwen-7B has `--gradient_checkpointing`, model paths use `/root/trace-verdict-study/models/` for Qwen family, no `--epochs` flag used
- CodeLlama-13B: `--gradient_checkpointing` + `--label_only_loss`
