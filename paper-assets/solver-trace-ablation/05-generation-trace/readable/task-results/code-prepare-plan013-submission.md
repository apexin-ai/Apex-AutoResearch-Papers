# code prepare plan013 submission

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare-plan013-submission_20260513T234655_result.json`
- **Structured JSON:** [`6c4cb9dc7fae5053b054.json`](../../sessions/6c/6c4cb9dc7fae5053b054.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。汇总结果：

---

**验证结果：全部 OK**

| 检查项 | 状态 |
|--------|------|
| `configs/grpo_random_reward.yaml` | ✓ 存在，内容正确 |
| `scripts/train_grpo.py` random_reward 模式 | ✓ L173-186 实现完整 |
| `data/train_500_seed42.jsonl` | ✓ 500 samples |
| `models/Qwen3-4B` | ✓ 存在 |
| reward_mode=random_reward | ✓ |
| exec_weight=0.9, sta_weight=0.1 | ✓ |
| num_steps=500, K=8, seed=42 | ✓ |
| output_dir=/root/autodl-tmp/outputs/plan013_random_reward_s42 | ✓ |
| 所有 import | ✓ 无报错 |
| **cuda:0** | **空闲** (0 MiB, 0% util) |
| cuda:1 | 占用 (80355 MiB) |

**配置文件完整内容：**
```yaml
model_path: /root/solver-trace-ablation/models/Qwen3-4B
data_path: data/train_500_seed42.jsonl
reward_mode: random_reward
output_dir: /root/autodl-tmp/outputs/plan013_random_reward_s42
num_steps: 500
per_device_batch_size: 4
gradient_accumulation_steps: 2
num_generations: 8
max_completion_length: 512
learning_rate: 1.0e-6
exec_weight: 0.9
sta_weight: 0.1
seed: 42
solver: prover9
logic_type: fol
wandb_project: solver-trace-ablation
wandb_run: plan013_random_reward
no_wandb: false
```

**推荐提交命令：**
```
bash -c 'CUDA_VISIBLE_DEVICES=0 source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_random_reward.yaml'
```

注：配置文件中已包含 num_steps=500、seed=42、output_dir，无需在命令行重复指定。vLLM 版本警告（0.18.1 vs TRL 支持的 0.11-0.17）不影响训练（GRPO 不走 vLLM 路径）。

---
