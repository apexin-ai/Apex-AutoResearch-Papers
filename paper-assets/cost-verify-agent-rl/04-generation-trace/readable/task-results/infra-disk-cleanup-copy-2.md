# infra disk cleanup

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_disk-cleanup_20260514T155044_result.json`
- **Structured JSON:** [`5b689c37bd2475f32c68.json`](../../sessions/5b/5b689c37bd2475f32c68.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

- **磁盘**：/root/autodl-tmp 250G 中已用 83G (33%)，并非 95% 满。
- **Checkpoints 目录**：要删除的三个目录（exp012_grpo、exp013b_grpo、exp013e）**已不存在**。当前仅有：
  - exp008_sft/ — 3.3G（受保护，不删）
  - exp015/ — 21G
  - exp016/ — 21G
  - exp017_expert_sft/ — 9.7G（正在运行）

要删除的目标已经被清理过了，磁盘使用率 33%，空间充足（168G 可用），无需额外清理。

---
