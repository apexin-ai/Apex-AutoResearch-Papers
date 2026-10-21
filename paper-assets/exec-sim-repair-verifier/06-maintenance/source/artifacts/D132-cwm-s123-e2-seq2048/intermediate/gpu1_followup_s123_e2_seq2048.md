# GPU 1 Follow-up: D132-cwm-s123-e2-seq2048

Trigger: cron callback for `deepseek-cwm-repo-s42-epoch2-eval` (PID 662946, GPU 1) completion

## Verified Prerequisites
- s123 checkpoint-8844 path: `/root/autodl-tmp/checkpoints_deepseek_cwm_repo_s123/checkpoint-8844/`
  - adapter_model.safetensors: 67MB, complete
  - All files present (adapter_config.json, optimizer.pt, trainer_state.json, etc.)

## Launch Command (seetacloud GPU 1)
```bash
cd /home/sonny/exec-sim-repair-verifier && CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 /root/miniconda3/bin/python eval_repo_cwm.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints_deepseek_cwm_repo_s123/checkpoint-8844 \
  --model_name /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct \
  --split test --max_seq_length 2048 --max_new_tokens 512 --batch_size 1 \
  --device cuda:0 \
  --output_dir /root/autodl-tmp/eval_results/deepseek_cwm_repo_s123_e2_seq2048/
```

## Registry Info
- exp_id: D132-cwm-s123-e2-seq2048
- hypothesis: CWM s123 epoch 2 eval @seq2048: seed variance baseline. 与 D133 s42 e2 @seq2048 对比 = clean seed variance（同 epoch 同 seq，仅 seed 不同）。
- parent: D133-cwm-s42-e2-seq2048-home
- server: seetacloud-westd-4x5090
- gpu: cuda:1
