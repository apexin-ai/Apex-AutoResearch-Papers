# code prep eval and grpo

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep-eval-and-grpo_20260514T210716_result.json`
- **Structured JSON:** [`9bf8cea83c1b28c7a032.json`](../../sessions/9b/9bf8cea83c1b28c7a032.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All info collected. Here's the report:

---

## 任务 1: Eval 脚本准备情况

**脚本**: `/root/cost-verify-agent-rl/scripts/eval_sft_fast.py` ✅ 存在

**vLLM**: v0.18.1 ✅ 已安装

**问题**: 脚本没有 argparse，参数是硬编码的。当前硬编码指向 exp017：
```python
model_path = "/root/autodl-tmp/checkpoints/exp017_expert_sft/final/"
output_path = "/root/cost-verify-agent-rl/artifacts/eval_exp017_fast.json"
```

**启动前需修改脚本** 中两行：
```python
model_path = "/root/autodl-tmp/checkpoints/exp019b_expert_sft_v3/final/"
output_path = "/root/cost-verify-agent-rl/artifacts/eval_exp019b_fast.json"
```

**Eval 启动命令**（修改脚本后，在 cuda:1 上运行）：
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export ALFWORLD_DATA=/root/autodl-tmp/alfworld
cd /root/cost-verify-agent-rl
CUDA_VISIBLE_DEVICES=1 python scripts/eval_sft_fast.py
```

参数：20 episodes, max 30 steps, temperature 0.4, gpu_memory_utilization=0.85

---

## 任务 2: GRPO 训练准备情况

**入口**: `RAGEN/train.py`（Hydra 配置驱动）

**最相关配置**: `_alfworld_exp018_sft_grpo` — 专门设计为 SFT→GRPO 的配置
- model_path 当前指向 `exp017_expert_sft/final`，需改为 `exp019b_expert_sft_v3/final`
- lr: 5e-7, kl_loss_coef: 0.1, total_steps: 30, GRPO with gamma=0.95
- 使用 2 GPU (cuda:0,1)

**对比 exp015/exp016**:
| | exp015 | exp016 | exp018 |
|---|---|---|---|
| model_path | qwen3_sft_final | qwen3_sft_final | exp017_expert_sft/final |
| lr | 1e-7 | (check config) | 5e-7 |
| 其余 | 基本相同 | 基本相同 | 基本相同 |

**GRPO 启动脚本模板** (`run_exp018.sh`):
```bash
#!/bin/bash
set -euo pipefail
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export TMPDIR=/root/autodl-tmp/tmp/ && mkdir -p $TMPDIR
export ALFWORLD_DATA=/root/autodl-tmp/alfworld
export RAY_memory_monitor_refresh_ms=0
export RAY_SYSTEM_MEMORY=210000000000
export HYDRA_FULL_ERROR=1
export CUDA_VISIBLE_DEVICES=0,1
cd /root/cost-verify-agent-rl/RAGEN
python train.py --config-name _alfworld_exp018_sft_grpo \
  model_path=/root/autodl-tmp/checkpoints/exp019b_expert_sft_v3/final \
  trainer.experiment_name=exp020-alfworld-sft-grpo \
  trainer.local_log_dir=/root/autodl-tmp/checkpoints/exp020/ \
  trainer.default_local_dir=/root/autodl-tmp/checkpoints/exp020/ \
  es_manager.val.env_groups=4 \
  'es_manager.val.env_configs.n_groups=[4]'
```

---

## 待处理项

1. **Eval 前**: 需要 `ssh_execute` 修改 `eval_sft_fast.py` 中的 model_path 和 output_path（或者复制一份专用脚本）
2. **GRPO 前**: 需要创建 exp020 配置 yaml（或用 Hydra CLI override model_path），并创建 `run_exp020.sh`
3. **时序约束**: Eval 可在 exp019b 完成后立即在 cuda:1 跑；GRPO 需要 2 GPU，必须等 eval 也跑完（或者先跑 eval，eval 完再启动 GRPO 用双卡）

是否现在就修改脚本/创建配置文件？

---
