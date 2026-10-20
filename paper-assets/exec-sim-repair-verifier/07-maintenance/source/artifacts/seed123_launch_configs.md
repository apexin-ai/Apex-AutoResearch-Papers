# Seed123 Repo-Level Launch Configs

准备于 2026-05-13，用于 CLS v4 和 CWM v10 训练完成后立即启动 seed=123 复现实验。

---

## 1. CLS seed123（home-1x5090, account: sonny）

### 环境激活

```bash
source /home/sonny/miniconda3/etc/profile.d/conda.sh && conda activate base
```

### 启动命令

```bash
cd /home/sonny/exec-sim-repair-verifier && \
source /home/sonny/miniconda3/etc/profile.d/conda.sh && conda activate base && \
CUDA_VISIBLE_DEVICES=0 nohup python3 -u train_repo_verifier.py \
  --seed 123 \
  --output_dir /home/sonny/exec-sim-repair-verifier/checkpoints_repo_cls_seed123/ \
  --run_name repo-cls-qwen3-4b-lora-home-seed123 \
  --no_wandb \
  --device cuda:0 \
  > /tmp/repo-level-cls-seed123_stdout.log 2>&1 &
echo "CLS_SEED123_PID=$!"
```

### 完整超参数

| 参数 | 值 |
|------|-----|
| 脚本 | `train_repo_verifier.py` |
| 模型 | `Qwen/Qwen3-4B` |
| 数据 | `/home/sonny/exec-sim-repair-verifier/data/swebench_full` |
| seed | **123** |
| batch_size | 2 |
| grad_accumulation | 16 |
| lr | 2e-4 |
| epochs | 3 |
| max_seq_length | 2048 |
| warmup_ratio | 0.1 |
| LoRA | r=16, alpha=32, dropout=0.05 |
| eval/save_steps | 200（脚本内硬编码） |
| device | cuda:0 |

### 预期输出

- Checkpoint: `/home/sonny/exec-sim-repair-verifier/checkpoints_repo_cls_seed123/`
- Best model: `/home/sonny/exec-sim-repair-verifier/checkpoints_repo_cls_seed123/best/`
- 日志: `/tmp/repo-level-cls-seed123_stdout.log`
- 总步数: 6633

---

## 2. CWM seed123（seetacloud-westd-4x5090, account: root）

### 环境激活

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
```

### 启动命令

```bash
cd /home/sonny/exec-sim-repair-verifier && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
CUDA_VISIBLE_DEVICES=2 nohup python3 -u train_repo_cwm.py \
  --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B \
  --seed 123 \
  --output_dir /root/autodl-tmp/checkpoints_repo_cwm_seed123/ \
  --run_name repo-cwm-qwen3-4b-lora-seed123 \
  --no_wandb \
  --save_steps 100 \
  --device cuda:0 \
  > /root/autodl-tmp/cwm_seed123_train.log 2>&1 &
echo "CWM_SEED123_PID=$!"
```

### 完整超参数

| 参数 | 值 |
|------|-----|
| 脚本 | `train_repo_cwm.py` |
| 模型 | `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B` |
| 数据 | `/home/sonny/exec-sim-repair-verifier/data/swebench_full` |
| seed | **123** |
| batch_size | 1 |
| grad_accumulation | 32 |
| lr | 2e-4 |
| epochs | 3 |
| max_seq_length | 2048 |
| warmup_ratio | 0.1 |
| LoRA | r=16, alpha=32, dropout=0.05 |
| save_steps | 100 |
| device | cuda:0（CUDA_VISIBLE_DEVICES=2） |

### 预期输出

- Checkpoint: `/root/autodl-tmp/checkpoints_repo_cwm_seed123/`
- Best model: `/root/autodl-tmp/checkpoints_repo_cwm_seed123/best/`
- 日志: `/root/autodl-tmp/cwm_seed123_train.log`
- 总步数: 6633

---

## 注意事项

1. CWM seed123 是全新训练，不用 `--resume_from_checkpoint`
2. CWM 用 `CUDA_VISIBLE_DEVICES=2` 绑定物理 GPU 2，`--device cuda:0` 是映射后的逻辑设备
3. CLS 脚本无 `--save_steps` 参数，eval/save_steps 硬编码 200
4. 有效 batch size 均为 32（CLS: 2×16, CWM: 1×32）
5. 两个脚本除 seed/output_dir/run_name 外，其余配置与原始训练完全一致
