# train scienceworld v6 bjb1

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_scienceworld_v6_bjb1_20260522T144908_result.json`
- **Structured JSON:** [`479be99c413463b18513.json`](../../sessions/47/479be99c413463b18513.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Pre-flight failed (C002)** — cannot start v6 training.

## 状态总结

### 磁盘 ✅
- 清理前: 43GB free → 删除 stella embedding cache (17GB) → **60GB free**

### v6 Config ✅ 已创建
`/root/cost-verify-agent-rl/RAGEN/config/_scienceworld_cell_c_grpo_v6.yaml`

关键参数 vs v5:

| 参数 | v5 | v6 |
|------|-----|-----|
| tasks | ScienceWorldSG_filtered (21 tasks) | **ScienceWorldSG_top5** (5 tasks: find-living-thing, find-non-living-thing, lifespan-longest-lived, lifespan-shortest-lived, lifespan-longest-lived-then-shortest-lived) |
| group_size | 16 | **4** |
| max_turn | 50 | **30** |
| ppo_mini_batch_size | 16 | **4** |
| lr | 1e-6 | 1e-6 (不变) |
| kl_loss_coef | 0.05 | 0.05 (不变) |
| response_length | 512 | 512 (不变) |
| collapse_detection | multi_turn_enabled: true | 不变 |

新增 env tag `ScienceWorldSG_top5` 已写入 `envs.yaml`。

### Checkpoint ❌ 阻塞
`/root/autodl-tmp/checkpoints/qwen3_scienceworld_sft/huggingface` 在 bjb1 和 westd 上均不存在，已在之前的磁盘清理中被删除。

**恢复方案**:
- SFT 训练数据 (`scienceworld_sft_train.parquet`) + 脚本 (`run_scienceworld_sft.sh`) 在 **westd-47453** 上可用
- 但 westd 4张 GPU 当前全部被占用 (~38GB/GPU)
- bjb1 GPUs 空闲，但缺少训练数据和 base model

**需要决策**: 
1. 等 westd GPU 空闲后在 westd 重训 SFT (~2.4h), 完成后 scp HF checkpoint 到 bjb1
2. 将数据 + base model 从 westd 传到 bjb1，在 bjb1 用 2 GPU 重训 SFT（更慢）
3. 其他方案？

---
