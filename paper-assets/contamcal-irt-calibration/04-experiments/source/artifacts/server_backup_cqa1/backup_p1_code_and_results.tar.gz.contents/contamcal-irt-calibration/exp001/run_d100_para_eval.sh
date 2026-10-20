#!/bin/bash
CUDA_VISIBLE_DEVICES=2 python /root/contamcal-irt-calibration/exp001/evaluate.py \
  --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B \
  --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter \
  --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42_para_aligned \
  --benchmarks mmlu gsm8k arc_challenge humaneval \
  --mc-format aligned \
  --paraphrase-dir /root/autodl-tmp/exp001/paraphrases \
  --cache-dir /root/autodl-tmp/.hf_cache
