# launch grpo alpha3p0 v2 westb0

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_launch_grpo_alpha3p0_v2_westb0_20260522T104100_result.json`
- **Structured JSON:** [`064498e62fcf35d8892a.json`](../../sessions/06/064498e62fcf35d8892a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据盘 250GB 已 100% 满，无法启动训练。任务描述说"约 44GB free"，但实际只剩 3.3MB。

主要占用：
- `recovery_aware_struct_prune/`: 235GB（其中 `grpo_qwen_math_cka_only_20` 单独占 38GB）
- `models/`: 15GB

删除损坏的 `grpo_rasp_alpha3p0_20/checkpoint-100/`（~7.2GB）远不够，训练输出需要约 11-12GB，加上训练过程中的临时开销，至少需要清出 ~20-30GB。

需要你决定哪些旧实验目录可以删除。候选：
- `grpo_qwen_math_cka_only_20` — **38GB**，清掉后空间直接够用
- `grpo_standard_25_westb` — 11GB
- `grpo_cka_only_20_seed123` — 12GB
- 1.5B 系列（9个目录 × ~2.8GB = ~25GB）

你要删哪些？

---
