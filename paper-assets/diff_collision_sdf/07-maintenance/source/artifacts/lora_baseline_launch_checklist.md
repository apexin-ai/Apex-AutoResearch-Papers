# Pi0.5 LoRA Baseline Launch Checklist

## 1. 脚本状态

| 项目 | 状态 |
|------|------|
| 服务器路径 | `/root/colliforce-vla/scripts/train_pi05_lora_baseline.py` |
| 是否在服务器上 | YES — 与本地 artifact 版本一致 |
| Bug fix: Phase 2 `>=` (L113) | INCLUDED |
| Bug fix: Dummy param (L105) | INCLUDED |

### 关键参数确认

| 参数 | 值 |
|------|-----|
| num_train_steps | 30,000 |
| Phase 1 (LoRA frozen) | 0 ~ 4999 步 |
| Phase 2 (LoRA unfrozen) | >= 5000 步, 100步 gradient warmup |
| LoRA rank | PaliGemma=16, Action Expert=32 |
| LR | 2.5e-5 cosine decay |
| batch_size | 32 |
| save_interval | 2,000 |
| scene | object_pudding |
| checkpoint base | `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/` |

## 2. 磁盘空间

| 分区 | 可用 | 判定 |
|------|------|------|
| `/root/autodl-tmp` (250G) | 75GB | PASS (需 ~30GB) |
| `/` (30G) | 12GB | OK (checkpoints 不写这里) |

## 3. 启动命令

### Seed 0 (cuda:0)

> **注意**: 已存在 dry-run 残留 `pi05_lora_baseline_object_pudding_seed0/`（仅 2 步），启动前须删除：

```bash
rm -rf /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/pi05_lora_baseline_object_pudding_seed0/
```

启动命令：
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/colliforce-vla && \
WANDB_MODE=offline nohup python scripts/train_pi05_lora_baseline.py \
  --scene object_pudding --seed 0 --gpu 0 \
  --num_train_steps 30000 --batch_size 32 \
  > /tmp/train_pi05_lora_baseline_s0.log 2>&1 &
```

### Seed 1 (cuda:1)

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/colliforce-vla && \
WANDB_MODE=offline nohup python scripts/train_pi05_lora_baseline.py \
  --scene object_pudding --seed 1 --gpu 1 \
  --num_train_steps 30000 --batch_size 32 \
  > /tmp/train_pi05_lora_baseline_s1.log 2>&1 &
```

### 启动后验证

```bash
# 检查进程
ps aux | grep train_pi05_lora_baseline | grep -v grep

# 检查日志（等 1-2 分钟后）
tail -20 /tmp/train_pi05_lora_baseline_s0.log
tail -20 /tmp/train_pi05_lora_baseline_s1.log
```

## 4. Blockers / 注意事项

| # | 类型 | 描述 |
|---|------|------|
| B1 | BLOCKER | 须等 s0_l005 / s0_l01 训练完成释放 GPU 后再启动 |
| B2 | ACTION REQUIRED | 启动 seed0 前须删除 dry-run 残留目录（见上方命令），否则 TrainConfig 会因 `overwrite=False` 报错 |
| N1 | NOTE | 两个 seed 各用 1 张卡，30k 步预计 ~18-22h |
| N2 | NOTE | Checkpoint 路径自动含 seed 后缀，不会冲突：`pi05_lora_baseline_object_pudding_seed{0,1}` |
