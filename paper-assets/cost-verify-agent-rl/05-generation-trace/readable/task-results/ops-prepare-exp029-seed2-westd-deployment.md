# ops prepare exp029 seed2 westd deployment

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prepare-exp029-seed2-westd-deployment_20260518T212259_result.json`
- **Structured JSON:** [`02b4f457077a48cb4133.json`](../../sessions/02/02b4f457077a48cb4133.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息收集完毕。以下是完整验证报告。

---

## 1. Checkpoint 完整性 ✅ 通过

路径：`/root/cost-verify-agent-rl/backups/exp029-seed2-bjb1/exp029-seed2/global_step_15/actor/`

| 文件 | 大小 | 状态 |
|------|------|------|
| model_world_size_2_rank_0.pt | 3.8G | ✓ |
| model_world_size_2_rank_1.pt | 3.8G | ✓ |
| optim_world_size_2_rank_0.pt | 6.5G | ✓ |
| optim_world_size_2_rank_1.pt | 6.5G | ✓ |
| extra_state_world_size_2_rank_0.pt | 15K | ✓ |
| extra_state_world_size_2_rank_1.pt | 15K | ✓ |
| fsdp_config.json | 46B | ✓ (world_size=2) |
| huggingface/ (tokenizer, 9 files) | ~16M | ✓ |
| latest_checkpointed_iteration.txt | "15" | ✓ |

总计 ~21G，所有关键组件完整。FSDP world_size=2 匹配目标 2-GPU 配置。

## 2. SFT 模型 ✅ 通过（路径不同）

- 预期路径 `/root/cost-verify-agent-rl/qwen3_exp021_ragen_sft_v4/` **不存在**
- 实际位置：`/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4/`（11 files, 3.3G）
- bjb1 config 中 `model_path` 已指向此路径，无需修改

## 3. Config 文件 ❌ 需从 bjb1 传输

westd 上不存在 `_alfworld_exp029_episode_level_seed2.yaml`。bjb1 上有现成可用版本：

**关键参数确认：**
- `seed: {train: 43, val: 123}` ✓
- `optimizer_offload: false` ✓（FSDP resume 必须）
- `max_actor_ckpt_to_keep: 3` ✓
- `resume_mode: auto` ✓
- `model_path: /root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4` ✓
- `CUDA_VISIBLE_DEVICES: 0,1` ✓
- `default_local_dir: /root/autodl-tmp/checkpoints/exp029-seed2/` ✓

**需要执行：** scp config 从 bjb1 到 westd

## 4. 磁盘空间 ⚠️ 紧张但可行

| 分区 | 总量 | 已用 | 可用 | 用途 |
|------|------|------|------|------|
| overlay (/) | 30G | 24G | 6.2G | 系统 + 备份 checkpoint (21G 在此) |
| /root/autodl-tmp | 250G | 228G | **23G** | checkpoints + 代码 |

**autodl-tmp 主要占用：**
- `factorial-h2-episode-adv/`: 62G
- `factorial-h2-episodeadv-seed2/`: 41G（运行中，完成后可释放）
- `qwen3_exp021_ragen_sft_v4/`: 3.3G
- `cost-verify-agent-rl/` (代码): 21G

**空间规划：**
- exp029_seed2 需要：3 checkpoints × 21G = **63G**
- factorial_seed2 完成后释放 41G → 可用 64G → **刚好够，无余量**
- 建议：同时清理 `factorial-h2-episode-adv/`（62G，如已完成）以获得充足余量
- 备份 checkpoint 在 overlay，用 **symlink** 到 autodl-tmp 避免额外复制

## 5. 部署准备命令（不执行）

### Step A: 传输 config（现在可做）

```bash
# 在 westd 上执行，从 bjb1 scp config
scp connect.bjb1.seetacloud.com:/root/cost-verify-agent-rl/RAGEN/config/_alfworld_exp029_episode_level_seed2.yaml \
    /root/autodl-tmp/cost-verify-agent-rl/RAGEN/config/
```

### Step B: 建立 checkpoint symlink（factorial_seed2 完成后）

```bash
# 清理 factorial_seed2 checkpoints 释放空间
rm -rf /root/autodl-tmp/checkpoints/factorial-h2-episodeadv-seed2/

# symlink 备份 checkpoint 到训练期望路径
ln -s /root/cost-verify-agent-rl/backups/exp029-seed2-bjb1/exp029-seed2/global_step_15 \
      /root/autodl-tmp/checkpoints/exp029-seed2/global_step_15
cp /root/cost-verify-agent-rl/backups/exp029-seed2-bjb1/exp029-seed2/latest_checkpointed_iteration.txt \
   /root/autodl-tmp/checkpoints/exp029-seed2/
```

### Step C: 启动训练

```bash
cd /root/autodl-tmp/cost-verify-agent-rl/RAGEN

# 清理 /tmp 防磁盘满
rm -rf /tmp/fast_downward_* /tmp/ray/* /tmp/tmp* 2>/dev/null

export TMPDIR=/root/autodl-tmp/tmp
export TORCH_COMPILE_DISABLE=1
export PYTHONUNBUFFERED=1
export WANDB_PROJECT=cost-verify-agent-rl
export CUDA_VISIBLE_DEVICES=0,1

python train.py --config-name _alfworld_exp029_episode_level_seed2
```

### 关键风险

1. **磁盘紧张**：即使释放 factorial_seed2 的 41G，也只有 64G 对 63G 需求，几乎零余量。强烈建议确认 `factorial-h2-episode-adv/`（62G）是否可清理。
2. **Symlink resume**：需确认 RAGEN 的 checkpoint loader 能通过 symlink 读取。如果不行，需要实际 move（但 overlay → autodl-tmp 跨分区只能 copy，会吃 21G 空间）。
3. **Step B 的 `mkdir -p`**：symlink 前需先 `mkdir -p /root/autodl-tmp/checkpoints/exp029-seed2/`。

---
