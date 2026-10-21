# scienceworld_sft_bjb1_v2 诊断报告

## 结论：训练成功完成

## 基本信息

| 项目 | 值 |
|------|-----|
| 实验 ID | scienceworld_sft_bjb1_v2 |
| 模型 | Qwen3-1.7B |
| 数据 | 3586 train / 1791 val (ScienceWorld expert trajectories) |
| 服务器 | bjb1-17606, cuda:0 |
| PID | 171362 (已退出) |
| 总步数 | 450 (2 epochs) |
| 框架 | TRL 1.1.0, Transformers 4.57.6, PyTorch 2.10.0+cu128 |

## Checkpoints

| 目录 | 时间 |
|------|------|
| checkpoint-112 | May 25 07:41 |
| checkpoint-224 | May 25 08:24 |
| checkpoint-336 | May 25 09:07 |
| checkpoint-448 | May 25 09:51 |
| checkpoint-450 | May 25 09:51 |
| final/ | May 25 09:51 |

`final/` 包含完整模型：model.safetensors (3.4GB) + tokenizer + config。

## 训练曲线

### Train Loss
- Step 5: 0.5945 (token_acc=92.06%)
- Step 450: 0.0587 (token_acc=98.28%)

### Eval Loss
| Step | Epoch | Eval Loss | Token Accuracy |
|------|-------|-----------|----------------|
| 112 | 0.50 | 0.1233 | 97.15% |
| 224 | 1.00 | 0.0803 | 98.02% |
| 336 | 1.50 | 0.0728 | 98.18% |
| 448 | 1.99 | 0.0725 | 98.18% |

Eval loss 在 epoch 1.5 后收敛（0.0728→0.0725），无过拟合迹象。

## GPU 状态

cuda:0 已完全释放：0% 利用率，0 MiB 显存。可启动 Cell B seed 100。
