# research seed2 deep search

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_seed2_deep_search_20260522T151647_result.json`
- **Structured JSON:** [`103452f7b90f682bdba9.json`](../../sessions/10/103452f7b90f682bdba9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

搜索完毕。结论：

## seed2 checkpoint 搜索结果

**seed2 最高 step = 15，step 20/25/30 不存在。**

### 完整目录清单

| 路径 | 格式 | 大小 | 说明 |
|------|------|------|------|
| `/root/autodl-tmp/cost-verify-agent-rl/backups/exp029-seed2-bjb1/exp029-seed2/global_step_15/` | FSDP（actor/huggingface 子目录） | 21G（整个 backup） | 从 bjb1 备份过来的原始 FSDP checkpoint，huggingface 子目录只有 tokenizer 文件，无 model weights |
| `/root/autodl-tmp/checkpoints/exp029_seed2_step15_hf/` | HF（含 model.safetensors） | 3.8G | 已转换的 HF 格式 checkpoint，完整可用 |

### 确认不存在

- `global_step_20` / `global_step_25` / `global_step_30` — 两台服务器（westd + bjb1）均不存在
- `latest_checkpointed_iteration.txt` 内容为 `15`，证实训练只保存到 step 15
- `episode_level_seed2` — 无匹配
- `seed2*resume` / `seed2*westd` — 无匹配
- `exp029-seed200` 目录为空，与 seed2 无关

bjb1 上 seed2 数据已被完全清除（find 无结果），所有 seed2 存档仅在 westd 上述两个位置。

---
