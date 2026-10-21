# 诊断报告: contamination_60_random_seed42

**日期**: 2026-05-18  
**服务器**: westd-30476  
**结论**: **误报 — 训练已成功完成**

## 失败根因

Cron 监控在 `~/runs/provenance_weight_training/contamination_60_random_seed42.log` 查找日志文件，但该文件不存在。训练日志实际写入了 output_dir 下的 `train_resume.log`（说明该实验是 resume 启动的，未将 stdout/stderr 重定向到 cron 监控路径）。加上训练脚本未启用 W&B，cron 判定无 metrics 并标记为 failed。

**实际上无任何 error/traceback/OOM/CUDA error。**

## 训练进度

- 总步数: 6103/6103 (100%)
- 训练时长: ~2h58m (train_runtime=10719s)
- 最终 train_loss: 6.4127
- Checkpoints: checkpoint-5500, checkpoint-6000, checkpoint-6103
- Final model: `/root/autodl-tmp/output/models/contamination_60_random_seed42/final/` (model.safetensors 1.19GB, 完整 tokenizer)

## GPU 当前状态

| GPU | 状态 | 显存占用 | 利用率 |
|-----|------|---------|--------|
| 0 | 空闲 | 0MiB/97887MiB | 0% |
| 1 | 空闲 | 0MiB/97887MiB | 0% |
| 2 | 忙碌 | 41757MiB (另一实验) | 98% |
| 3 | 空闲 | 0MiB/97887MiB | 0% |

cuda:3 已空闲，训练进程已退出。

## 是否可以直接重跑

不需要重跑。训练已完成，final model 已保存。如需重跑其他配置，环境/数据/模型均在位：
- 模型: `models/Qwen/Qwen3-0.6B` ✓
- 数据: `data/scored_data_60.jsonl` (371499 examples) ✓
- GPU cuda:3 空闲可用 ✓

## 建议

将此实验在监控系统中标记为 completed。后续实验启动时确保日志重定向到 `~/runs/provenance_weight_training/` 路径，并启用 W&B 上报。
