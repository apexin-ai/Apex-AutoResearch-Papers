# No-Evidence Test Eval Commands (D147 spot-check)

Generated: 2026-05-21

## Pre-flight (C001)
```bash
# 确认目标 GPU 显存占用 < 2GB
nvidia-smi --query-gpu=index,memory.used --format=csv,noheader
```

## 14B SFT no-evidence test eval

```bash
CUDA_VISIBLE_DEVICES=X source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && python -m freige.eval.test_inference \
  --model_path /root/autodl-tmp/sft_output_14b/checkpoint-144 \
  --base_model /root/autodl-tmp/models/Qwen/Qwen3-14B \
  --data_path /root/autodl-tmp/data/re-docred-repo/data \
  --output_dir /root/autodl-tmp/eval_results/test_eval_14b_sft_no_evi_s42 \
  --batch_size 1 \
  --max_new_tokens 2048 \
  --no-quantize \
  --seed 42 \
  --split test_revised \
  --no_evidence
```

## 1.7B SFT no-evidence test eval

```bash
CUDA_VISIBLE_DEVICES=X source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && python -m freige.eval.test_inference \
  --model_path /root/autodl-tmp/sft_output_qwen3_1_7b_bf16 \
  --base_model /root/autodl-tmp/models/Qwen/Qwen3-1.7B \
  --data_path /root/autodl-tmp/data/re-docred-repo/data \
  --output_dir /root/autodl-tmp/eval_results/test_eval_1_7b_sft_no_evi_s42 \
  --batch_size 1 \
  --max_new_tokens 2048 \
  --no-quantize \
  --seed 42 \
  --split test_revised \
  --no_evidence
```

## Checklist
- [x] 14B adapter exists: `/root/autodl-tmp/sft_output_14b/checkpoint-144/adapter_config.json`
- [x] 1.7B adapter exists: `/root/autodl-tmp/sft_output_qwen3_1_7b_bf16/adapter_config.json`
- [x] `--no_evidence` flag confirmed (test_inference.py L149)
- [x] `--base_model` overridden (default is Qwen3-4B, not correct for 14B/1.7B)
- [x] `eval_results/` directory exists
- [ ] C001: nvidia-smi pre-flight before submission
- [ ] C002/C003: CUDA_VISIBLE_DEVICES=X set (replace X at submission time)
