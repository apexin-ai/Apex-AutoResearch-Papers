# Diagnostic Report: train_baseline_control_100k crash

**Server:** cqa1-33015 | **PID:** 100236 | **Date:** 2026-05-18

## 1. 崩溃原因

**W&B API key 未配置。** 训练脚本在 `wandb.init()` 处崩溃，未进入训练循环。

```
Traceback (most recent call last):
  File "/root/autodl-tmp/importance_margin_vla_compress/train_baseline_control.py", line 558, in <module>
    main()
  File "/root/autodl-tmp/importance_margin_vla_compress/train_baseline_control.py", line 473, in main
    wandb.init(
  ...
wandb.errors.errors.UsageError: No API key configured. Use `wandb login` to log in.
EXIT_CODE=1
```

模型加载、checkpoint 加载（step 99999）、数据集初始化均成功，在调用 `wandb.init()` 时立即失败。

## 2. 根因分析

cqa1-33015 上没有任何 W&B 认证：
- `~/.netrc` 不存在
- `~/.config/wandb/` 不存在
- 环境变量 `WANDB_API_KEY` 未设置

训练命令中设置了 `HF_HUB_OFFLINE=1` 和 `TRANSFORMERS_OFFLINE=1` 但未设置 `WANDB_API_KEY`。脚本在 line 473 无条件调用 `wandb.init()`，没有 offline fallback。

## 3. 其他环境状态

| 项目 | 状态 |
|------|------|
| 磁盘 | /root/autodl-tmp 88% used (33G free), 偏紧但可用 |
| GPU 0 | 空闲 (1MiB) |
| GPU 1 | 被 eval_random_prune_smolvla.py (PID 92881) 占用，3103MiB |
| GPU 2-3 | 空闲 |
| checkpoint | checkpoints/libero_full_ft/step_099999/checkpoint.pt 加载成功 |
| dmesg | 无权限读取（容器环境），未见系统级 OOM/GPU 错误 |

## 4. 修复建议

**方案 A（推荐）：设置 WANDB_API_KEY 环境变量**

在训练命令中增加 `export WANDB_API_KEY=[REDACTED]

**方案 B：wandb offline mode**

在训练命令中增加 `export WANDB_MODE=offline`，训练结束后用 `wandb sync` 上传。

## 5. 修复后的完整训练命令

### 方案 A（在线 logging）
```bash
bash -c "export PATH=/root/miniconda3/bin:\$PATH && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export WANDB_API_KEY=[REDACTED] && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=0 python train_baseline_control.py --config configs/baseline_control.yaml --wandb_project smart-compress-vla --wandb_run baseline_control_fresh_lr"
```

### 方案 B（offline logging）
```bash
bash -c "export PATH=/root/miniconda3/bin:\$PATH && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export WANDB_MODE=offline && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=0 python train_baseline_control.py --config configs/baseline_control.yaml --wandb_project smart-compress-vla --wandb_run baseline_control_fresh_lr"
```

注意：已加 `CUDA_VISIBLE_DEVICES=0`，因为 GPU 1 当前被 eval 占用。
