# grpo_rasp_20_4096 训练状态报告

**检查时间**: 2026-05-15 07:25 (服务器时间) / 2026-05-14 (本地)

## 进程状态
- **PID**: 244606 (bash wrapper) → 244611 (python)
- **状态**: ✅ 运行中，已运行 27 分钟
- **GPU**: cuda:1，NVIDIA RTX PRO 6000 Blackwell

## 训练进度
- **当前步数**: 8 / 500 (1.6%)
- **Step 速度**: ~173 秒/步 (~2.88 分钟/步)
- **预计剩余时间**: ~23.6 小时
- **预计完成时间**: 2026-05-16 ~07:00 (服务器时间)

## 关键指标
- 尚未输出（训练步数未达到首个 logging_steps 阈值）
- 配置: loss_type=dapo, epsilon=0.2, temperature=0.7, num_generations=4, max_completion_length=4096

## GPU 利用率
| GPU | 利用率 | 显存占用 | 温度 | 功耗 |
|-----|--------|----------|------|------|
| cuda:0 | 89% | 17,703 / 97,887 MiB (18%) | 58°C | 339W/600W |
| cuda:1 | 98% | 74,690 / 97,887 MiB (76%) | 64°C | 407W/600W |

- cuda:0 上有另一个 python 进程 (PID 239932)
- cuda:1 被本实验完全占用

## W&B 信息
- **Run ID**: ccx0jr0z
- **Run Name**: grpo_pruned_rasp_20
- **Project**: recovery_aware_struct_prune
- **URL**: https://wandb.ai/xiaoyucorynne-/recovery_aware_struct_prune/runs/ccx0jr0z

## 训练配置摘要
- 模型: DeepSeek-R1-Distill-Qwen-7B RASP 20% pruned (6.16B params)
- 数据: GSM8K 2000 samples (本地缓存)
- 输出路径: /root/autodl-tmp/recovered_rasp_20_4096
- save_strategy: steps, save_steps=200, save_total_limit=2
- generation_batch_size=16, steps_per_generation=8
- reward desert patience: 50 log events

## 异常
- HuggingFace Hub 网络不可达，但成功 fallback 到本地缓存数据集，无影响
- vLLM 版本警告 (0.18.1 vs 支持的 0.11.0-0.17.1)，未影响运行
