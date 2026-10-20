# label_only Seed Robustness Experiment Prep

## Parent Experiment
- **exp_id**: full_trace_label_only_seed42
- **accuracy**: 86.22% [84.37%, 88.07%]
- **checkpoint**: `/root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_label_only/final`

## Configuration
- **Model**: Qwen2.5-Coder-7B-Instruct (`/root/trace-verdict-study/models/Qwen2.5-Coder-7B-Instruct`)
- **Data**: `/root/autodl-tmp/trace-verdict-study-data/full_trace_{train,test}.jsonl` (4720 train / 1190 test)
- **Condition**: `full_trace` with `--label_only_loss` (completion-only loss on pass/fail token)
- **max_length**: 2048 (train) / 2048 (eval) -- matched
- **Hyperparams**: LoRA r=16, alpha=32, dropout=0.05, lr=2e-4, warmup=0.1, batch=4, grad_accum=8, epochs=3, bf16

## Validation Checklist
- [x] Data files exist: `full_trace_train.jsonl` (4720 lines), `full_trace_test.jsonl` (1190 lines)
- [x] Model files exist: 4 safetensors shards + tokenizer
- [x] Data loading + tokenization dry-run passed (CPU, printed "Sample completion: pass")
- [x] `--label_only_loss` path verified: uses prompt-completion format with `completion_only_loss=True`
- [x] Eval max_length=2048 matches training max_length=2048 (both default)
- [ ] GPU dry-run (--max_steps 1): SKIPPED -- both GPUs occupied by ae_only experiments
- [x] Output dirs won't conflict with parent (`full_trace_label_only_seed123/456` vs `full_trace_label_only/`)

## Training Commands

### label_only_seed123 (cuda:0)

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition full_trace --label_only_loss --gradient_checkpointing --gpu 0 --seed 123 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_label_only_seed123 --wandb_project trace-verdict-study --wandb_run_name label_only_seed123 && python eval/evaluate.py --condition full_trace --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_label_only_seed123/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_label_only_seed123/final/eval_results.json --save_predictions"
```

### label_only_seed456 (cuda:1)

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition full_trace --label_only_loss --gradient_checkpointing --gpu 0 --seed 456 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_label_only_seed456 --wandb_project trace-verdict-study --wandb_run_name label_only_seed456 && python eval/evaluate.py --condition full_trace --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_label_only_seed456/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_label_only_seed456/final/eval_results.json --save_predictions"
```

**Note**: Both commands use `--gpu 0` as the logical device. The submit system sets `CUDA_VISIBLE_DEVICES` to the physical GPU (0 or 1).

## Estimated Training Time
- Parent (seed42) wall clock: ~2-2.5h (train + eval), based on full_trace_seed42_v5 (7852s = 2.18h)
- Expected per seed: ~2-2.5h
- Total (parallel on 2 GPUs): ~2-2.5h

## submit_training_job Parameters

### seed123
- **server**: westd-11235
- **account**: root
- **gpu**: cuda:0
- **command**: (see above)
- **exp_id**: label_only_seed123
- **log_path**: `/tmp/label_only_seed123.log`

### seed456
- **server**: westd-11235
- **account**: root
- **gpu**: cuda:1
- **command**: (see above)
- **exp_id**: label_only_seed456
- **log_path**: `/tmp/label_only_seed456.log`
