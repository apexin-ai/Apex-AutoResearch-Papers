# westb-23072 磁盘清理 & 实验状态报告
**时间**: 2026-05-17 17:50 UTC

## 磁盘使用（清理前后）

| 分区 | 总量 | 清理前 | 清理后 | 可用 |
|------|------|--------|--------|------|
| /dev/md0 (数据盘) | 14T | 6.9T (50%) | 6.9T (50%) | 7.2T |
| overlay (根分区) | 30G | 8.6G (29%) | 8.6G (29%) | 22G |

> 注意：数据盘已从原来的 250GB 扩容至 14T，磁盘满问题已不存在。

项目目录 `/root/autodl-tmp/recovery_aware_struct_prune/`: **189G → 155G**（释放 ~34G）

## 删除清单

| 目录 | 大小 | 原因 |
|------|------|------|
| grpo_stage2_standard_20_v8 | 12G | 旧 v8 GRPO checkpoint，已废弃 |
| pruned_rasp_alpha_0.0 | 12G | α 消融模型（α=0 极端值），实验已完成 |
| pruned_rasp_alpha_1.0 | 12G | α 消融模型（α=1 极端值），实验已完成 |
| grpo_rasp_rlvr_20 | 44K | 空目录 |
| __pycache__ | ~KB | 编译缓存 |

**未删除但可后续清理**：`sft_gradient_20/checkpoint-935` (35G，含 24GB optimizer.pt)。训练完成后可安全删除。

## 实验状态

### gradient_sft_v3（tmux: scoring_ablation_v2, GPU 0）
- **进度**: 1141/1870 steps (61%), epoch ~1.2/2.0
- **Loss**: 0.63 (下降中), token accuracy: 0.83
- **预计剩余**: ~13 分钟（1.09 s/it × 729 steps）

### scoring_ablation random postprune eval（tmux: scoring_ablation_random, GPU 1）
- **进度**: 89/200 samples (44%), acc=0.3000
- **EOS rate**: 44%, avg_len=2646
- **预计剩余**: ~86 分钟（46.5 s/sample × 111 remaining）

## nvidia-smi 快照

```
GPU 0: RTX PRO 6000 | 51581/97887 MiB | 71% util | 330W
  └─ PID 698674: python (sft_recovery.py on pruned_gradient_20)

GPU 1: RTX PRO 6000 | 12889/97887 MiB | 77% util | 303W
  └─ PID 696141: python (eval_gsm8k.py on pruned_random_20)
```

## 当前保留目录

| 目录 | 大小 | 状态 |
|------|------|------|
| sft_gradient_20 | 35G | 活跃 - 训练写入中 |
| pruned_gradient_20 | 12G | 活跃 - gradient SFT 源模型 |
| pruned_random_20 | 12G | 活跃 - random eval 中 |
| grpo_rasp_25 | 11G | 最新 GRPO 模型 |
| pruned_rasp_25 / 30 | 11G×2 | 不同剪枝率模型 |
| pruned_standard_25 / 30 | 11G×2 | 不同剪枝率模型 |
| pruned_rasp_rlvr_20 | 12G | RLVR 剪枝模型 |
| sft_rasp_25 | 11G | SFT 恢复模型 |
| sft_rasp_rlvr_20 | 12G | SFT 恢复模型 |
| sft_standard_25 | 11G | SFT 恢复模型 |
