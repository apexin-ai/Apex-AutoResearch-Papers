# 3 GPU Relay Commands (2026-05-18)

## Relay 1 (P0): GPU 0 — CLS v5 eval (ckpt-2105, epoch 1, seq8192)

**触发条件**: `deepseek-cls-repo-v5` 训练完成 (GPU 0, PID 698033)

**前置检查** (已验证 2026-05-18):
- checkpoint-2105 存在: `/root/autodl-tmp/checkpoints_deepseek_cls_repo_v5/checkpoint-2105/` ✓
- base model 存在: `/root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct/` ✓
- eval 脚本: `eval_repo_cls.py` (无 `--output_dir` 参数, 需手动建目录)
- 注意: `--max_seq_length 8192` (CLS canonical seq length)

**exp_id**: `deepseek-cls-repo-v5-ckpt2105-test-seq8192`

**启动命令**:
```bash
mkdir -p /root/autodl-tmp/eval_results/deepseek_cls_repo_v5_ckpt2105_test_seq8192 && \
cd /home/sonny/exec-sim-repair-verifier && \
CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 nohup /root/miniconda3/bin/python eval_repo_cls.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints_deepseek_cls_repo_v5/checkpoint-2105 \
  --model_name /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct \
  --data_dir data/swebench_full \
  --split test \
  --max_seq_length 8192 \
  --batch_size 1 \
  --device cuda:0 \
  --output /root/autodl-tmp/eval_results/deepseek_cls_repo_v5_ckpt2105_test_seq8192/eval_summary.json \
  --pred_output /root/autodl-tmp/eval_results/deepseek_cls_repo_v5_ckpt2105_test_seq8192/predictions.jsonl \
  > /root/autodl-tmp/eval_results/deepseek_cls_repo_v5_ckpt2105_test_seq8192/eval.log 2>&1 &
```

---

## Relay 2 (P0): GPU 3 — Qwen3-8B TRAJ repo 训练

**触发条件**: GPU 3 当前任务完成后

**前置检查** (已验证 2026-05-18):
- base model 存在: `/root/autodl-tmp/models/Qwen/Qwen3-8B/` ✓
- 训练脚本存在: `/home/sonny/exec-sim-repair-verifier/train_traj_verifier.py` ✓
- 数据存在: `/home/sonny/exec-sim-repair-verifier/data/swebench_full/traj_train.jsonl` ✓

**exp_id**: `qwen3-8b-traj-repo`

**启动命令**:
```bash
cd /home/sonny/exec-sim-repair-verifier && \
CUDA_VISIBLE_DEVICES=3 HF_HUB_OFFLINE=1 nohup /root/miniconda3/bin/python train_traj_verifier.py \
  --data_dir data/swebench_full/ \
  --model_name /root/autodl-tmp/models/Qwen/Qwen3-8B \
  --output_dir /root/autodl-tmp/checkpoints_qwen3_8b_traj_repo/ \
  --run_name qwen3-8b-traj-repo \
  --seed 42 \
  --max_seq_length 8192 \
  --batch_size 1 \
  --grad_accumulation 8 \
  --lr 2e-4 \
  --epochs 3 \
  --lora_rank 16 \
  --lora_alpha 32 \
  --no_wandb \
  > /root/autodl-tmp/checkpoints_qwen3_8b_traj_repo/train.log 2>&1 &
```

注意: `nohup` 前需确保 output_dir 存在。改为:
```bash
mkdir -p /root/autodl-tmp/checkpoints_qwen3_8b_traj_repo && \
cd /home/sonny/exec-sim-repair-verifier && \
CUDA_VISIBLE_DEVICES=3 HF_HUB_OFFLINE=1 nohup /root/miniconda3/bin/python train_traj_verifier.py \
  --data_dir data/swebench_full/ \
  --model_name /root/autodl-tmp/models/Qwen/Qwen3-8B \
  --output_dir /root/autodl-tmp/checkpoints_qwen3_8b_traj_repo/ \
  --run_name qwen3-8b-traj-repo \
  --seed 42 \
  --max_seq_length 8192 \
  --batch_size 1 \
  --grad_accumulation 8 \
  --lr 2e-4 \
  --epochs 3 \
  --lora_rank 16 \
  --lora_alpha 32 \
  --no_wandb \
  > /root/autodl-tmp/checkpoints_qwen3_8b_traj_repo/train.log 2>&1 &
```

---

## Relay 3 (P1): GPU 1 — CWM s123 e2 @seq2048 eval

**触发条件**: GPU 1 当前任务完成后

**前置检查** (已验证 2026-05-18):
- checkpoint 存在: `/root/autodl-tmp/checkpoints_deepseek_cwm_repo_s123/checkpoint-8844/` ✓ (含 adapter_model.safetensors)
- base model 存在: `/root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct/` ✓

**exp_id**: `deepseek-cwm-repo-s123-e2-seq2048`

**启动命令**:
```bash
mkdir -p /root/autodl-tmp/eval_results/deepseek_cwm_repo_s123_e2_seq2048 && \
cd /home/sonny/exec-sim-repair-verifier && \
CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 nohup /root/miniconda3/bin/python eval_repo_cwm.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints_deepseek_cwm_repo_s123/checkpoint-8844 \
  --model_name /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct \
  --split test \
  --max_seq_length 2048 \
  --max_new_tokens 512 \
  --batch_size 1 \
  --device cuda:0 \
  --output_dir /root/autodl-tmp/eval_results/deepseek_cwm_repo_s123_e2_seq2048/ \
  > /root/autodl-tmp/eval_results/deepseek_cwm_repo_s123_e2_seq2048/eval.log 2>&1 &
```

---

## 快速参考

| Relay | GPU | 类型 | exp_id | 优先级 |
|-------|-----|------|--------|--------|
| 1 | 0 | CLS eval | deepseek-cls-repo-v5-ckpt2105-test-seq8192 | P0 |
| 2 | 3 | TRAJ train | qwen3-8b-traj-repo | P0 |
| 3 | 1 | CWM eval | deepseek-cwm-repo-s123-e2-seq2048 | P1 |
