# exp-014 Diagnosis Report

## 失败根因（双重问题）

### 1. 环境未激活（EXIT_CODE=127 的原因）
- `deepspeed` 安装在 `/root/miniconda3/bin/deepspeed`，不在默认 PATH 中
- 原始提交命令 `bash -c "cd ... && deepspeed ..."` 缺少 `source /root/miniconda3/bin/activate`

### 2. GPU 分配冲突（训练中断的原因）
- 原始命令指定 `CUDA_VISIBLE_DEVICES=1,2`，但 `deepspeed --num_gpus 2` **会忽略 CUDA_VISIBLE_DEVICES**
- deepspeed 日志明确记录: `Detected VISIBLE_DEVICES=1,2 but ignoring it because --num_gpus cl args were used`
- deepspeed 实际分配 GPU 0,1，而 GPU 0 被 exp-004 (`run_exp004_act_baseline.py`, PID 18204) 占用 21.8GB/32.6GB
- 模型加载到 GPU 0 后 OOM 崩溃，日志在 GRPO 训练初始化后中断

## 日志关键内容

```
[02:22:40] Detected VISIBLE_DEVICES=1,2 but ignoring it because --num_gpus was used
[02:22:40] Setting CUDA_VISIBLE_DEVICES=0,1  # 实际用了 GPU 0,1
[02:22:52] Probe trained: accuracy=0.9945, AUROC=0.9999  # Probe 阶段成功
[02:23:03] Starting GRPO training with probe-based R1...
[02:23:03] Gradient accumulation steps mismatch warning
# 日志在此中断，无后续输出
```

## 环境信息

| 项目 | 值 |
|------|-----|
| 服务器 | westd-28034 |
| GPU | 4x NVIDIA RTX 5090 (32GB) |
| Python | 3.12.3 |
| PyTorch | 2.8.0+cu128 |
| DeepSpeed | 0.19.0 |
| CUDA Driver | 595.71.05 / CUDA 13.2 |

## GPU 状态（诊断时 2026-05-19 02:25）

| GPU | 显存占用 | 状态 |
|-----|---------|------|
| 0 | 21838/32607 MiB | exp-004 运行中 (PID 18204) |
| 1 | 2/32607 MiB | 空闲 |
| 2 | 2/32607 MiB | 空闲 |
| 3 | 2/32607 MiB | 空闲 |

## 正确的重试命令

```bash
source /root/miniconda3/bin/activate && cd /root/contrastive_entrain_calib/training && deepspeed --include localhost:1,2 run_exp014_continuous_probe.py
```

关键修改：
1. 添加 `source /root/miniconda3/bin/activate` 激活环境
2. 用 `--include localhost:1,2` 替代 `--num_gpus 2`，确保使用空闲的 GPU 1,2（deepspeed 的 `--include` 不会被忽略）

## 注意事项
- Probe 阶段已成功完成，checkpoint 在 `/root/contrastive_entrain_calib/checkpoints/exp014_probe_baseline/probe.pt`
- 脚本可能会重新训练 probe（如果没有 resume 逻辑），这不影响正确性
- 重试前确认 GPU 1,2 仍然空闲
