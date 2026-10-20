# Server Data Inventory — westd-18266

**Date**: 2026-05-23

---

## 1. 总体大小

```
11G     /root/autodl-tmp/simgate-modular-routing/
```

## 2. 各子目录大小（降序）

```
9.4G    checkpoints/
1.3G    results/
31M     logs/
30M     data/
7.7M    crafter_pilot/
2.4M    wandb/
1.3M    artifacts/
1.3M    src/
984K    docs/
780K    scripts/
736K    paper/
328K    figures/
220K    guided_router/
56K     analysis/
32K     notes/
0       configs/
```

## 3. Checkpoint / 模型权重

大量 `.safetensors`、`.pt`、`.bin` 文件存在于 `checkpoints/` 和 `results/` 目录中（输出被截断，原始输出超过 45000 字符）。

主要分布：

- `results/ablation_data_size/` — scale_25pct, scale_50pct 等多 seed checkpoint
- `results/ablation_r3/` — scale_25pct ~ scale_200pct 多 seed checkpoint
- `checkpoints/seed-robustness-seed42` ~ `seed49` — 每个含 checkpoint-110, checkpoint-165, final_adapter

文件类型：
- `adapter_model.safetensors` — LoRA adapter 权重
- `optimizer.pt` — 优化器状态
- `scheduler.pt` — 学习率调度器状态
- `training_args.bin` — 训练参数

## 4. results 目录概览

**107 个条目**（含子目录和文件），涵盖：

- 消融实验：`ablation_b_*`, `ablation_data_size`, `ablation_r3`
- 跨模型评估：`llama_cross_model_full`, `gemma_*`, `backbone_72b`
- Baseline：`baseline_245eps`, `majority_vote_baseline`, `reflexion_baseline_*`
- 统计分析：`bootstrap_95ci.json`, `cross_model_bootstrap_cis.*`, `unified_episode_bootstrap.json`
- SFT 数据：`sft_data`, `sft_data_death_aware`, `sft_data_test`
- 各阶段计划评估：`plan-003` ~ `plan-013`, `plan_001b` ~ `plan_012`
- 其他：`death_*`, `penalty_*`, `grounding_*`, `routing-patterns`, `seed-robustness*`

## 5. 运行中的进程

**无 Python/vLLM/Torch 训练进程运行。** 仅有系统服务：

```
supervisord, proxy, jupyter-lab, tensorboard, sshd, autopanel
```

## 6. GPU 状态

```
NVIDIA RTX PRO 6000 Blackwell Server Edition, 0 MiB / 97887 MiB, 0% utilization
```

GPU 完全空闲，未被占用。
