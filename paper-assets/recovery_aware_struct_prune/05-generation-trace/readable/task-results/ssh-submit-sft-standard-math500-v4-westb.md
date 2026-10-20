# ssh submit sft standard math500 v4 westb

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_submit_sft_standard_math500_v4_westb_20260523T115715_result.json`
- **Structured JSON:** [`a8a400d825ff728930c4.json`](../../sessions/a8/a8a400d825ff728930c4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**停止，磁盘不足。**

| 检查项 | 结果 |
|--------|------|
| sft_standard_20 模型 | **不存在**（westb 上没有） |
| /root/autodl-tmp 可用空间 | **9.2GB**（97% 已用） |
| eval_math500.py 版本 | **NEW 版本**（pred_answer 出现 3 次） |

**问题**: 模型 ~12GB，可用空间仅 9.2GB，无法 SCP。需要先在 westb 上清理至少 3-4GB 空间，或者改用 westd-32935 跑这个 eval。

---
