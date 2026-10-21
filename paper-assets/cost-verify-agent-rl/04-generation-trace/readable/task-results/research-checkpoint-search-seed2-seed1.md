# research checkpoint search seed2 seed1

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_checkpoint_search_seed2_seed1_20260522T150913_result.json`
- **Structured JSON:** [`0ad8daabdfe2a0990d11.json`](../../sessions/0a/0ad8daabdfe2a0990d11.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 搜索结果

### Task A: seed2 step30 checkpoint

**不存在。** 两台服务器均无 `global_step_30` 目录。

seed2 现存最高 step 是 **step15**，有两份：

| 路径 | 服务器 | 格式 | 大小 | 完整性 |
|------|--------|------|------|--------|
| `/root/autodl-tmp/cost-verify-agent-rl/backups/exp029-seed2-bjb1/exp029-seed2/global_step_15/` | westd | FSDP (2-rank) | 21G | 完整（model/optim/extra_state 各2个rank文件）。`huggingface/` 子目录仅16M（只有 tokenizer/config，**无模型权重**） |
| `/root/autodl-tmp/checkpoints/exp029_seed2_step15_hf/` | westd | HF | 3.8G | 完整（`model.safetensors` + config + tokenizer） |

`latest_checkpointed_iteration.txt` = 15，说明 seed2 训练备份时只存到 step15，step30 从未被保存或已被删除。

---

### Task B: seed1 step5 checkpoint

**不存在。** 两台服务器均无名为 "seed1" 或原始 exp029（无 seed 后缀）的 checkpoint 目录。

已排查路径：
- bjb1 `/root/cost-verify-agent-rl/artifacts/exp029_episode_level/intermediate/` — 仅含 `config_diff.md`，无模型文件
- bjb1 `/root/autodl-tmp/checkpoints/` — 有 seed4/seed7/seed42/intervention_c_prime，无 seed1
- westd `/root/autodl-tmp/checkpoints/` — 有 seed3-8/seed42/seed200/seed2048，无 seed1
- bjb1 `/root/runs/` — 无 exp029 相关目录
- westd `/root/runs/` — 有 `gsweep-g100-h5-seed1`（sweep 运行，非 exp029 原始训练）

---

### Task C: ScienceWorld SFT checkpoint

**无明确标记为 "scienceworld" 的 checkpoint。** `find *scienceworld*` 两台服务器均为空。

westd 上有两个 SFT 相关 checkpoint，但无法从命名确认是 ScienceWorld：

| 路径 | 格式 | 大小 | 说明 |
|------|------|------|------|
| `/root/autodl-tmp/checkpoints/qwen3_8b_sft_v1/checkpoint-231/` | HF (Qwen3-8B, 5 shards) | 16G | 完整。命名仅 "sft_v1"，无 scienceworld 标识 |
| `/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4/` | HF (有 `training_args.bin`) | 未测 | exp021 ragen SFT v4，可能是通用 SFT |

---
