# plan018-additive-random-b01 s43/s44 提交就绪报告

**日期**: 2026-05-14
**参考基准**: plan018-additive-random-b01-s42 (PR=0.79, ISR=0.104)

## 验证结果

| 项目 | 状态 |
|------|------|
| Config 文件 | 已创建 (`configs/plan018_random_b01_s43.yaml`, `configs/plan018_random_b01_s44.yaml`) |
| 数据文件 | `data/train_500_seed42.jsonl` 存在 |
| 模型路径 | `/root/autodl-tmp/models/Qwen3-4B` 存在 |
| Output 目录 | 不存在，无覆盖风险 |
| 磁盘空间 | 112G 可用（需 ~32GB，充足） |
| save_total_limit | 1（脚本硬编码 line 419） |
| log_completions | False（脚本硬编码 line 425） |

## 关键配置参数

| 参数 | 值 |
|------|-----|
| reward_mode | additive_random |
| beta (ISR weight) | 0.1 |
| num_steps | 500 |
| seed | 43 / 44 |
| per_device_batch_size | 4 |
| gradient_accumulation_steps | 2 |
| num_generations | 4 |
| max_completion_length | 512 |
| learning_rate | 1e-6 |
| solver | prover9 |
| bf16 | True |

## ⚠️ Config 加载 Bug 注意

`train_grpo.py` 的 config 加载逻辑（line ~349）只在 CLI 默认值为 None 时才用 YAML 值覆盖。以下参数有非 None 默认值，**必须通过 CLI 显式传入**：
- `--beta 0.1`（默认 0.3）
- `--num_steps 500`（默认 100）
- `--seed 43/44`（默认 42）

## 提交命令

### s43（GPU N）
```bash
export CUDA_VISIBLE_DEVICES=N && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && nohup python scripts/train_grpo.py \
  --config configs/plan018_random_b01_s43.yaml \
  --beta 0.1 --num_steps 500 --seed 43 \
  > /root/autodl-tmp/outputs/plan018_additive_random_b01_s43.log 2>&1 &
```

### s44（GPU M）
```bash
export CUDA_VISIBLE_DEVICES=M && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && nohup python scripts/train_grpo.py \
  --config configs/plan018_random_b01_s44.yaml \
  --beta 0.1 --num_steps 500 --seed 44 \
  > /root/autodl-tmp/outputs/plan018_additive_random_b01_s44.log 2>&1 &
```

**GPU 分配**：等 plan002-additive-b01-s43/s44 训练完成后，N 和 M 替换为空闲 GPU 编号（0 或 1）。提交后用 `nvidia-smi` 确认只占用分配的 GPU（C002 约束）。

## 文件路径

| 文件 | 路径 |
|------|------|
| Config s43 | `/root/solver-trace-ablation/configs/plan018_random_b01_s43.yaml` |
| Config s44 | `/root/solver-trace-ablation/configs/plan018_random_b01_s44.yaml` |
| Output s43 | `/root/autodl-tmp/outputs/plan018_additive_random_b01_s43/` |
| Output s44 | `/root/autodl-tmp/outputs/plan018_additive_random_b01_s44/` |
| 训练数据 | `/root/solver-trace-ablation/data/train_500_seed42.jsonl` |
