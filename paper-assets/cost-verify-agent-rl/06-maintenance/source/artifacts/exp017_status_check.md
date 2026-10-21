# exp017 状态检查报告

时间: 2026-05-14 00:10 CST

## 1. exp017_expert_sft 训练状态: ✅ 已完成

- **进程 PID 353947**: 已结束（`ps -p 353947` 返回空）
- **训练耗时**: 1573s ≈ 26 分钟（3 epochs, 462 steps）
- **最终 train_loss**: 0.1434（末尾 step loss ~0.04, mean_token_accuracy ~0.983）
- **train_samples/sec**: 4.69, total_flos: 1.21e17
- **日志**: `/root/runs/cost-verify-agent-rl/exp017_expert_sft.log`
- **Checkpoint**:
  - `/root/autodl-tmp/checkpoints/exp017_expert_sft/final/` → 完整模型 3.44GB (model.safetensors, Qwen3-1.7B 全参)
  - `checkpoint-154/`, `checkpoint-308/`, `checkpoint-462/` → 每 epoch 末
- **训练数据**: `/root/autodl-tmp/expert_sft/expert_sft_train.jsonl` (11.5MB), val 0.6MB
- **入口点**: `scripts/run_expert_sft.sh` → `scripts/sft_train.py`（TRL SFT, bs=4×4=16, lr=2e-5, max_seq=4096）

无 tmux session 残留。

## 2. 磁盘空间

```
/dev/md0        250G  105G  146G  42%  /root/autodl-tmp     ✅ 充裕
overlay          30G  7.3G   23G  25%  /                    ✅ OK
```

**`/root/autodl-tmp/checkpoints/` 占用**:

| 目录 | 大小 | 状态 |
|---|---|---|
| exp008_sft | 3.3G | ⚠️ 被 `qwen3_sft_final` 软链引用，保留 |
| exp015 | 21G | 🗑️ 可清理（旧失败实验） |
| exp016 | 21G | 🗑️ 可清理（旧失败实验） |
| exp017_expert_sft | 33G | ✅ 当前活跃，含 3 epoch ckpt + final |

可清理: exp015 + exp016 = **42GB**。无紧急清理需求（磁盘 146G 可用）。

## 3. exp018 准备状态: ✅ 就绪

- **入口脚本**: `/root/cost-verify-agent-rl/scripts/run_exp018.sh`
- **Config**: `/root/cost-verify-agent-rl/RAGEN/config/_alfworld_exp018_sft_grpo.yaml`
- **`model_path`**: `/root/autodl-tmp/checkpoints/exp017_expert_sft/final` ✅ 存在 (3.4GB)
- **输出目录**: `/root/autodl-tmp/checkpoints/exp018/`（启动时创建）
- **关键参数**:
  - GRPO, total_training_steps=30, save_freq=5, test_freq=20, val_before_train=True
  - GPU: `CUDA_VISIBLE_DEVICES=0,1`, n_gpus_per_node=2 ✅ 合规 C001
  - lr=5e-7, kl_loss_coef=0.1, clip_ratio_low/high=0.2/0.28
  - rollout: response_length=1024, max_model_len=8192, gpu_mem_util=0.4, enforce_eager=True
  - env: AlfworldSG, train env_groups=4×group_size=16, val env_groups=16
  - max_actor_ckpt_to_keep=3, resume_mode=disable

## Pre-flight Checklist (启动 exp018 前)

- [x] SFT checkpoint 存在且完整 (3.4GB safetensors)
- [x] config `model_path` 指向 exp017 final
- [x] GPU 设置为 cuda:0,1
- [x] 磁盘充足（>10GB，实际 146GB）
- [ ] 启动前再次 `nvidia-smi` 确认 GPU 空闲
- [ ] 确认 `/root/autodl-tmp/alfworld` 数据存在
- [ ] vLLM/verl 沿用 exp016 已成功栈，无需再验证
