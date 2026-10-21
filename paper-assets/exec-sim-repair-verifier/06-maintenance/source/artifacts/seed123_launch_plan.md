# Seed123 Launch Plan

Created: 2026-05-13

---

## 1. CLS v4 当前进度 (home-1x5090)

| 项目 | 值 |
|------|-----|
| 进程 PID | 2885139 (alive, 运行 3h18m) |
| 当前 step | ~1123 / 6633 (17%) |
| 当前 epoch | ~0.50 |
| 最新 eval (step 1000) | eval_loss = **0.2410**, epoch 0.4523 |
| 最新 train (step 1100) | loss = 0.4469, lr = 1.85e-4 |
| 速度 | ~7 s/it |
| 预计剩余 | ~10.7h (约 5510 steps × 7s) |
| 预计完成 | 2026-05-13 ~23:00 UTC+8 |
| Checkpoints | 200, 800, 1000 |
| GPU | 98% util, 19465/32607 MiB |

---

## 2. CWM v10 当前进度 (seetacloud-westd-4x5090)

| 项目 | 值 |
|------|-----|
| 进程 PID | 105205 (alive, 运行 1h34m) |
| 当前 step | ~594 / 6633 (9%) |
| 当前 epoch | ~0.25 |
| 最新 eval (step 500) | eval_loss = **0.3294**, epoch 0.23 |
| 最新 train (step 550) | loss = 1.9143, lr = 1.65e-4 |
| 速度 | ~8 s/it |
| 预计剩余 | ~13.4h (约 6039 steps × 8s) |
| 预计完成 | 2026-05-14 ~02:00 UTC+8 |
| Checkpoints | 300, 400, 500 |
| GPU | GPU2: 88% util, 21067/32607 MiB (单卡) |

---

## 3. CLS seed123 启动命令 (home-1x5090)

**服务器**: home-1x5090, user: sonny
**Python 环境**: 系统 python3 (进程 PATH: /home/sonny/.local/bin:/usr/local/bin:...)
**训练脚本**: train_repo_verifier.py

### 训练参数 (与 v4 一致，仅改 seed 和输出路径)

| 参数 | 值 |
|------|-----|
| model_name | Qwen/Qwen3-4B (默认) |
| seed | **123** |
| max_seq_length | 2048 |
| batch_size | 2 |
| grad_accumulation | 16 |
| lr | 2e-4 |
| epochs | 3 |
| warmup_ratio | 0.1 |
| lora_rank | 16 |
| lora_alpha | 32 |
| lora_dropout | 0.05 |
| save_steps | 200 |
| eval_steps | 200 |

### 启动命令

```bash
cd /home/sonny/exec-sim-repair-verifier && \
nohup python3 train_repo_verifier.py \
  --seed 123 \
  --output_dir /home/sonny/exec-sim-repair-verifier/checkpoints_repo_cls_home_seed123/ \
  --run_name repo-cls-qwen3-4b-lora-home-seed123 \
  --no_wandb \
  > /tmp/repo-level-cls-v4-seed123_stdout.log 2>&1 &
echo "PID=$!"
```

---

## 4. CWM seed123 启动命令 (seetacloud-westd-4x5090)

**服务器**: seetacloud-westd-4x5090, user: root
**Python 环境**: conda base (/root/miniconda3/)
**训练脚本**: train_repo_cwm.py

### 训练参数 (与 v10 一致，仅改 seed 和输出路径)

| 参数 | 值 |
|------|-----|
| model_name | /root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B |
| seed | **123** |
| max_seq_length | 2048 |
| batch_size | 1 |
| grad_accumulation | 32 |
| lr | 2e-4 |
| epochs | 3 |
| warmup_ratio | 0.1 |
| lora_rank | 16 |
| lora_alpha | 32 |
| lora_dropout | 0.05 |
| save_steps | 100 |
| eval_steps | 100 |
| device | cuda:0 |

### 启动命令

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /home/sonny/exec-sim-repair-verifier && \
nohup python3 -u train_repo_cwm.py \
  --seed 123 \
  --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B \
  --output_dir /root/autodl-tmp/checkpoints_repo_cwm_v9_seed123/ \
  --run_name repo-cwm-qwen3-4b-lora-seed123 \
  --save_steps 100 \
  --device cuda:0 \
  --no_wandb \
  > /root/autodl-tmp/cwm_v9_seed123_train.log 2>&1 &
echo "PID=$!"
```

---

## 注意事项

- CLS seed123 需等 v4 训练完成后启动（预计 5/13 23:00），否则 GPU 冲突（home 只有 1 张 5090）
- CWM seed123 可用其他空闲 GPU (cuda:1/cuda:3) 并行启动，无需等 v10 完成
- 两个 seed123 实验不使用 wandb（与当前训练一致）
- 不使用 --resume_from_checkpoint（全新训练）
