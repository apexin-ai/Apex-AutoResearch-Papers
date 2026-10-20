# exp44_multi_llm_mixed 诊断报告

**诊断时间**: 2026-05-22 13:56 (服务器时间)  
**结论**: 误报。实验未崩溃，当前仍在正常运行。

## 错误类型

**假阳性 (False Positive)** — 监控系统误判为 failed，实际进程正常运行中。

## 当前状态

| 项目 | 状态 |
|------|------|
| PID | 31463 (active, 145% CPU, 2.6GB RAM) |
| GPU | cuda:0, 2214MiB / 97887MiB, 76% util |
| 阶段 | 评估阶段 — Seed 123 推理中 |
| 训练 | 3个seed全部完成 (seed 42/123/456) |
| 磁盘 | 根分区 32%, 数据盘 37% — 正常 |
| 日志 | 无 Traceback/OOM/Error |

## 训练进度 (已完成)

- Seed 42: DeBERTa 4 epochs (best val_loss=0.4670), GRU early stop epoch 6 (val_f1=1.0)
- Seed 123: DeBERTa 4 epochs (best val_loss=0.4682), GRU early stop epoch 6 (val_f1=1.0)
- Seed 456: DeBERTa 4 epochs (best val_loss=0.4539), GRU early stop epoch 6 (val_f1=1.0)

## 评估进度 (进行中)

- Seed 42 完成:
  - IID F1: 1.0000, Acc: 1.0000
  - WildChat FPR: 0.0000
  - Qwen OOD DD/AA/FITD recall: 1.0000 (all)
  - Llama crescendo/dd/aa/fitd recall: 1.0000 (all)
- Seed 123: DeBERTa weights loaded,正在提取 embeddings 进行推理
- Seed 456: 待执行

## 监控误判原因分析

1. **无 W&B 集成**: 脚本只在最后写 `results/exp44_multi_llm_mixed.json`，不上报 W&B metrics，监控系统无法检测到训练心跳
2. **PID 跟踪错误**: 实验分两步启动（先 FITD generation PID 26918，再 training PID 31463），监控可能跟踪的是已结束的 FITD 进程或 shell wrapper
3. **无 tmux session**: 进程以 nohup 方式运行，tmux ls 无结果，监控如果依赖 tmux 检测则会判定为 dead

## 训练命令

```bash
# 启动方式 (exp44_wait_and_train.sh)
source /root/miniconda3/etc/profile.d/conda.sh
conda activate base
cd /root/persuasion_turn_jailbreak_detect
CUDA_VISIBLE_DEVICES=0 python scripts/exp44_train_mixed_llm.py
```

## 检查点位置

```
/root/autodl-tmp/persuasion_turn_jailbreak_detect/checkpoints/exp44_mixed_seed42/
/root/autodl-tmp/persuasion_turn_jailbreak_detect/checkpoints/exp44_mixed_seed123/
/root/autodl-tmp/persuasion_turn_jailbreak_detect/checkpoints/exp44_mixed_seed456/
```

## 建议

1. **无需修复** — 等待进程自然完成（预计还需 5-10 分钟完成 Seed 123/456 评估）
2. **结果文件**: 完成后自动保存到 `/root/persuasion_turn_jailbreak_detect/results/exp44_multi_llm_mixed.json`
3. **监控改进**: 对非 W&B 实验，应通过 PID 存活 + 日志更新时间判断状态，而非依赖 W&B heartbeat
