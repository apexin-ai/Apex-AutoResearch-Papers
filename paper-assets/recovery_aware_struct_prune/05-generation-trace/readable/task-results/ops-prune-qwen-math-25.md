# ops prune qwen math 25

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prune_qwen_math_25_20260516T093018_result.json`
- **Structured JSON:** [`b689fd08cbdf30850a2a.json`](../../sessions/b6/b689fd08cbdf30850a2a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**三个阻塞问题**：

### 1. 模型路径不对
- 指定: `/root/autodl-tmp/Qwen2.5-Math-7B` ❌
- 实际: `/root/autodl-tmp/models/Qwen2.5-Math-7B` ✅ (15GB)

### 2. Scores 文件名不匹配
- `results/importance_scores_qwen_math.pt` ❌ 不存在
- `results/cka_scores_qwen_math.pt` ❌ 不存在
- 现有: `results/importance_scores.pt` (18K, May 15) 和 `results/cka_scores.pt` (120K, May 15)
- 这些 scores 很可能就是 Qwen Math 的（已有 `pruned_qwen_math_rasp_20` 和 `pruned_qwen_math_standard_20` 就是用它们生成的）

### 3. 磁盘空间不足
- 可用: **2.3GB**，需要 ~22GB
- `/root/autodl-tmp` 已用 248G/250G
- 现有产出占 ~220GB（17 个 pruned/sft 目录 + 2 个原始模型）

**需要你决定**：
1. Scores 文件是否直接用 `importance_scores.pt` / `cka_scores.pt`？
2. 需要删除哪些旧产出来腾出 ~22GB 空间？候选：
   - `sft_standard_25` (0 bytes，空目录)
   - `pruned_graspune_20` + `sft_graspune_20` (24GB，GrASP baseline)
   - `pruned_rasp_20` / `pruned_standard_20` / `sft_rasp_20_westd` / `sft_standard_20_westd` (DeepSeek 20% 相关，若 westb 上有备份)

---
