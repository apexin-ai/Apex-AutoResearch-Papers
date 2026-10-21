# research cell b config

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_cell_b_config_20260524T232713_result.json`
- **Structured JSON:** [`ba91c310fe84d2a4908b.json`](../../sessions/ba/ba91c310fe84d2a4908b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息充分了。汇总 Cell B 配置。

---

## Cell B (h=2, episode-level advantage) 调研结果

### 1. 已有配置文件

`/root/cost-verify-agent-rl/RAGEN/config/_alfworld_factorial_h2_episode_adv.yaml` — 已存在，关键参数：

| 参数 | 值 |
|------|-----|
| `context_window_mode` | `step_independent` |
| `step_independent_history_length` | 2 |
| `advantage_mode` | `episode_level` |
| `total_training_steps` | 15 |
| `save_freq` / `test_freq` | 5 |
| `val_before_train` | True |
| Train | 16 groups × 8 = 128 episodes (AlfworldSG) |
| Val | 134 episodes (AlfworldOOD) |
| Base model | `qwen3_exp021_ragen_sft_v4` |
| GPUs | 2 (cuda:0,1) |
| LR | 1e-6, KL coef 0.01, clip 0.2/0.28 |

与 hsweep-h2 的唯一区别：增加了 `advantage_mode: "episode_level"` + val 用 134 OOD episodes。

### 2. Registry 状态

无已有 Cell B 实验注册。无 checkpoint 存在。

### 3. 训练时长估算

从 `hsweep-h2-seed1.log` 实测时间戳（同样 h=2, 15 steps, 2 GPUs）：

| 阶段 | 时间点 | 累计 |
|------|--------|------|
| 开始 | 05-17 12:18 | 0h |
| Step 5 ckpt | 05-17 16:28 | 4h 10min |
| Step 10 ckpt | 05-17 19:42 | 7h 24min |
| Step 15 ckpt | 05-17 22:29 | 10h 11min |

hsweep-h2 用 32-ep SG val，factorial 用 134-ep OOD val（~4.2x 更重）。估算：
- **纯训练步（无 val）**：~28 min/step → 15 steps ≈ **7 小时**
- **含 134-ep OOD val**：val 每次 ~3-3.5h，共 4 次 val（step 0/5/10/15）→ 总计 **~19-21 小时/seed**

**建议**：多种子跑时可关闭 `val_before_train` 并降 `test_freq`，训练后统一做 post-hoc OOD eval，可省约一半时间。

### 4. 训练命令模板

```bash
#!/bin/bash
set -euo pipefail

SEED=${1:?Usage: $0 &lt;seed> [gpu_ids]}
GPU_IDS=${2:-"0,1"}
CKPT_DIR="/root/autodl-tmp/checkpoints/factorial-h2-episode-adv/seed${SEED}/"

source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export TMPDIR=/root/autodl-tmp/tmp/ && mkdir -p $TMPDIR
export ALFWORLD_DATA=/root/autodl-tmp/alfworld
export HF_HOME=/root/autodl-tmp/.hf_cache
export RAY_memory_monitor_refresh_ms=0
export RAY_SYSTEM_MEMORY=210000000000
export HYDRA_FULL_ERROR=1
export CUDA_VISIBLE_DEVICES=${GPU_IDS}
export WANDB_PROJECT=cost-verify-agent-rl
export WANDB_NAME="factorial_h2_episodeadv_s${SEED}"
export WANDB_MODE=online
export WANDB_DIR=/root/autodl-tmp/wandb && mkdir -p $WANDB_DIR

mkdir -p "$CKPT_DIR"
rm -rf /tmp/fast_downward_* /tmp/ray/* /tmp/tmp* 2>/dev/null || true

cd /root/cost-verify-agent-rl/RAGEN
python train.py --config-name _alfworld_factorial_h2_episode_adv \
    seed.train=${SEED} \
    seed.val=${SEED} \
    system.CUDA_VISIBLE_DEVICES="\"${GPU_IDS}\"" \
    trainer.experiment_name="factorial-h2-episode-adv-s${SEED}" \
    trainer.local_log_dir="\"${CKPT_DIR}\"" \
    trainer.default_local_dir="\"${CKPT_DIR}\"" \
    2>&1 | tee ~/runs/cost-verify-agent-rl/factorial_h2_episodeadv_s${SEED}.log
```

Seed 策略参照 launch_hsweep.sh: `SEED * 10000`（seed1→10000, seed2→20000, seed3→30000）。

### 5. OOD Eval 命令模板

已有脚本 `eval_ood_seed5.py`（修改 CHECKPOINT 路径即可复用），或用通用脚本：

```bash
cd /root/cost-verify-agent-rl
CUDA_VISIBLE_DEVICES=0 python scripts/eval_checkpoint.py \
    --checkpoint_path /root/autodl-tmp/checkpoints/factorial-h2-episode-adv/seed${SEED}/global_step_${STEP}/actor/huggingface \
    --num_episodes 134 \
    --temperature 0.4 \
    --max_steps 50 \
    --gpu 0 \
    --gpu_memory_utilization 0.35 \
    --output_dir /root/autodl-tmp/eval_results/
```

也可用 `eval_checkpoint_full_context.py`（评估时用 full context 而非 h=2 窗口）来做公平的 inference-time 对比。

预计单次 134-ep eval 耗时：**~2.5-3.5 小时**（单 GPU）。

---
