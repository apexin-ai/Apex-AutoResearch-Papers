# ops fix exp029 seed2 bjb1

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_exp029_seed2_bjb1_20260518T101915_result.json`
- **Structured JSON:** [`e1c1aa7e110a0bcb3f83.json`](../../sessions/e1/e1c1aa7e110a0bcb3f83.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

重要发现：**实验已在运行（retry3），但使用的是旧的不匹配配置。**

当前运行的 retry3 加载的配置（Hydra 启动时读取）：
- `ppo_max_token_len_per_gpu: 16384` (seed1 = 65536)
- `ppo_mini_batch_size: 8` (seed1 = 16)
- `train.env_groups: 8` (seed1 = 16)
- `total_training_steps: 15` (seed1 = 100)

进度：**step 2/15**，约 880s/step，预计还需 ~3 小时完成。但这 15 步的结果与 seed1（100 步）**不具可比性**，无法用于 seed 复现。

我已覆写配置文件为与 seed1 一致的参数（仅 seed=43 不同）。有两个选择：

1. **让 retry3 跑完**（~3h），作为短期 sanity check，之后用修正配置跑 100 步
2. **现在终止 retry3**，直接用修正配置启动 100 步的正式 seed2 实验

考虑到这是 P0（核心 claim 的统计稳健性），建议**终止当前 15-step 实验，直接启动 100-step 正式版**。需要你确认是否 kill 当前实验。

**环境确认汇总：**
- GPU：2x RTX PRO 6000 (97GB each) ✓
- SFT checkpoint：`/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4/` ✓
- 磁盘：116G 可用 ✓
- 修正后的配置文件：`/root/cost-verify-agent-rl/RAGEN/config/_alfworld_exp029_episode_level_seed2.yaml` ✓

**启动命令（待确认后执行）：**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/cost-verify-agent-rl/RAGEN && \
rm -rf /tmp/fast_downward_* /tmp/ray/* /tmp/tmp* 2>/dev/null && \
export WANDB_PROJECT=cost-verify-agent-rl && \
CUDA_VISIBLE_DEVICES=0,1 python train.py --config-name _alfworld_exp029_episode_level_seed2 \
  2>&1 | tee /root/runs/cost-verify-agent-rl/exp029_episode_level_seed2_v2.log
```

---
