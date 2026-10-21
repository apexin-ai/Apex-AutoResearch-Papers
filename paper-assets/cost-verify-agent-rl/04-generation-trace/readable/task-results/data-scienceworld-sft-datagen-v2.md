# data scienceworld sft datagen v2

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_scienceworld_sft_datagen_v2_20260524T082502_result.json`
- **Structured JSON:** [`9702ccc0af7eccd06e62.json`](../../sessions/97/9702ccc0af7eccd06e62.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据生成运行正常：

- **已生成**: 13 条 train 数据（约 62 秒处理 10 个 variations）
- **全部 score=100**，gold path 质量好
- **无 timeout/error**
- tmux session `sw_datagen` 稳定运行中

按当前速度（~6s/variation），ScienceWorld 约有 ~900 个 variations（30 tasks × ~30 vars），预计总耗时约 **90 分钟**。var 152 将被自动跳过，超时 variation 会在 300s 后跳过并重建 env。

数据持续 append 写入 `/root/cost-verify-agent-rl/data/scienceworld_sft_train.jsonl`，中途中断不会丢失已生成数据。1h 后如未全部完成，>500 条即可直接用于 SFT。

---
