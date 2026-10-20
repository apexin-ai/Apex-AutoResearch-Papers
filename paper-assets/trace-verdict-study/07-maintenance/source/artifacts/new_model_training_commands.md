# Training Commands: Qwen-1.5B & CodeLlama-7B Experiments

Generated: 2026-05-16

## Model Paths
- Qwen-2.5-Coder-1.5B-Instruct: `/root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct`
- CodeLlama-7b-Instruct-hf: `/root/autodl-tmp/models/CodeLlama-7b-Instruct-hf`

## LoRA Config (both models)
- r=16, alpha=32, dropout=0.05
- target_modules: q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj

---

## Qwen-2.5-Coder-1.5B-Instruct (4 experiments)

### qwen1.5b_exception_only_seed42
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition exception_only --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen1.5b_exception_only_seed42 --wandb_project trace-verdict-study --wandb_run_name qwen1.5b_exception_only_seed42 && python eval/evaluate.py --condition exception_only --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen1.5b_exception_only_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/qwen1.5b_exception_only_seed42/final/eval_results.json --save_predictions"
```

### qwen1.5b_no_trace_seed42
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition no_trace --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen1.5b_no_trace_seed42 --wandb_project trace-verdict-study --wandb_run_name qwen1.5b_no_trace_seed42 && python eval/evaluate.py --condition no_trace --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen1.5b_no_trace_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/qwen1.5b_no_trace_seed42/final/eval_results.json --save_predictions"
```

### qwen1.5b_vota_seed42
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition vota --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen1.5b_vota_seed42 --wandb_project trace-verdict-study --wandb_run_name qwen1.5b_vota_seed42 && python eval/evaluate.py --condition vota --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen1.5b_vota_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/qwen1.5b_vota_seed42/final/eval_results.json --save_predictions"
```

### qwen1.5b_full_trace_seed42
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition full_trace --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen1.5b_full_trace_seed42 --wandb_project trace-verdict-study --wandb_run_name qwen1.5b_full_trace_seed42 && python eval/evaluate.py --condition full_trace --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen1.5b_full_trace_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/qwen1.5b_full_trace_seed42/final/eval_results.json --save_predictions"
```

---

## CodeLlama-7b-Instruct-hf (3 experiments)

### codellama_exception_only_seed42
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition exception_only --model_path /root/autodl-tmp/models/CodeLlama-7b-Instruct-hf --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama_exception_only_seed42 --wandb_project trace-verdict-study --wandb_run_name codellama_exception_only_seed42 && python eval/evaluate.py --condition exception_only --model_path /root/autodl-tmp/models/CodeLlama-7b-Instruct-hf --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama_exception_only_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/codellama_exception_only_seed42/final/eval_results.json --save_predictions"
```

### codellama_no_trace_seed42
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition no_trace --model_path /root/autodl-tmp/models/CodeLlama-7b-Instruct-hf --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama_no_trace_seed42 --wandb_project trace-verdict-study --wandb_run_name codellama_no_trace_seed42 && python eval/evaluate.py --condition no_trace --model_path /root/autodl-tmp/models/CodeLlama-7b-Instruct-hf --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama_no_trace_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/codellama_no_trace_seed42/final/eval_results.json --save_predictions"
```

### codellama_vota_seed42
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition vota --model_path /root/autodl-tmp/models/CodeLlama-7b-Instruct-hf --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama_vota_seed42 --wandb_project trace-verdict-study --wandb_run_name codellama_vota_seed42 && python eval/evaluate.py --condition vota --model_path /root/autodl-tmp/models/CodeLlama-7b-Instruct-hf --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama_vota_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/codellama_vota_seed42/final/eval_results.json --save_predictions"
```

---

## Notes
- Both GPUs currently occupied by label_only experiments; queue these after completion
- Qwen-1.5B: ~3GB model, should be fast to train (smaller than 7B)
- CodeLlama-7B: ~13GB model, similar footprint to Qwen-7B / DeepSeek-6.7B
- LoRA target modules confirmed compatible: both Qwen and LLaMA families use same attention/MLP projection names
- train_sft.py uses `tokenizer.apply_chat_template()` — works with any HF model that has a chat template
