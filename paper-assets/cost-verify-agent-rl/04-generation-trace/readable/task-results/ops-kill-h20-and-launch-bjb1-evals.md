# ops kill h20 and launch bjb1 evals

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-h20-and-launch-bjb1-evals_20260519T103320_result.json`
- **Structured JSON:** [`931436aaaad35380e9d5.json`](../../sessions/93/931436aaaad35380e9d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

### Step 1: Kill h=20 ✅
- PID 77613 及子进程（ray workers 81050, 81051）已全部 kill
- cuda:0, cuda:1 显存已归零（0MiB / 97887MiB），无运行进程

### Step 2: exp029_seed2 checkpoint ❌ 不可用
- bjb1 上 `/root/autodl-tmp/checkpoints/exp029/` 仅有 `global_step_15`，**无 `global_step_30`**
- 整个 bjb1 上不存在任何 `seed2` 变体目录
- **OOD eval 无法启动，停止该部分**

### Step 3: 8B SFT checkpoint ❌ 拷贝未完成
- `/root/autodl-tmp/checkpoints/qwen3_8b_sft_v1/checkpoint-231/` 应有 7 个 safetensors 分片
- 当前完成 2/7（model-00001, model-00002），shard 3 正在 rsync（~2.5G/~4.5G）
- rsync 从 18:15 开始，已 19 分钟传了 ~12G，剩余 ~20G，预计还需 ~30 分钟
- **clean eval 无法启动，停止该部分**

### 磁盘
- `/root/autodl-tmp`: 187G/250G used，64G free。8B 完整 checkpoint ~32G，空间够

### 下一步需要你决定
1. **exp029_seed2 global_step_30** 在哪？是否在 westd 上？需要从别处拷贝过来？
2. **8B eval** rsync 完成后（~18:50-19:05）再启动，还是你另有安排？

---
