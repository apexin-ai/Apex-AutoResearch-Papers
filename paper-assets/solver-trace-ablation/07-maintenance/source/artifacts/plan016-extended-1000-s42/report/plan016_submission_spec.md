# plan016-extended-1000-s42 提交规格

## 训练命令

```bash
export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 1000 --seed 42 --output_dir /root/autodl-tmp/outputs/plan016_extended_1000_s42
```

## submit_training_job 参数

- **server**: westd-39279
- **account**: root
- **gpu**: cuda:1
- **command**: `bash -c "export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 1000 --seed 42 --output_dir /root/autodl-tmp/outputs/plan016_extended_1000_s42"`

## spec (for registry RUNNING transition)

```json
{
  "command": "bash -c \"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 1000 --seed 42 --output_dir /root/autodl-tmp/outputs/plan016_extended_1000_s42\"",
  "server": "westd-39279",
  "gpu": ["cuda:1"],
  "data_path": "/root/solver-trace-ablation/data/train_500_seed42.jsonl",
  "data_count": 500,
  "model_name": "Qwen3-4B",
  "seed": 42,
  "hypothesis": "Extended 1000-step exec-only: verify s42 genuine convergence",
  "plan_id": "plan_016"
}
```

## 配置确认

| 参数 | 值 | 来源 |
|------|-----|------|
| reward_mode | execution_only | configs/grpo_exec_only.yaml |
| num_steps | 1000 | CLI override |
| K (num_generations) | 8 | configs/grpo_exec_only.yaml |
| seed | 42 | CLI override |
| data_path | data/train_500_seed42.jsonl | CLI override (C001) |
| model_path | /root/autodl-tmp/models/Qwen3-4B | configs/grpo_exec_only.yaml |
| output_dir | /root/autodl-tmp/outputs/plan016_extended_1000_s42 | CLI override |
| save_total_limit | 1 | 脚本硬编码 L418 (C003) |
| log_completions | False | 脚本硬编码 L423 (C003) |
| save_only_model | True | 脚本硬编码 L419 |
| CUDA_VISIBLE_DEVICES | 1 | export 显式设置 (C002) |
| learning_rate | 1e-6 | configs/grpo_exec_only.yaml |
| per_device_batch_size | 4 | configs/grpo_exec_only.yaml |
| gradient_accumulation_steps | 2 | configs/grpo_exec_only.yaml |
| max_completion_length | 512 | configs/grpo_exec_only.yaml |

## ⚠️ 磁盘空间警告

/root/autodl-tmp 当前 244G/250G (98%)，仅剩 6.4G。1000 步训练需要 ~15G 用于模型 checkpoint。

**提交前必须清理旧实验，建议删除（均已 DONE）：**

| 目录 | 大小 | 实验 | 结论 |
|------|------|------|------|
| grpo_exec_only | 15G | sta-phase1-exec-only-r5 | 旧 100 步 phase1 |
| grpo_exec_sta | 15G | sta-phase1-exec-sta-r5 | 旧 100 步 phase1 |
| plan001_exec_only_s43_r4 | 46G | plan001-exec-only-s43-r4 | negative (PR=14%) |
| plan001_exec_only_s44 | 31G | plan001-exec-only-s44 | negative (tautological) |

清理以上任意两个即可释放 >30G 空间。

## 预估运行时间

plan001-s42-r2 500 步耗时 ~64 min。1000 步预计 ~120-130 min (~2h)。
