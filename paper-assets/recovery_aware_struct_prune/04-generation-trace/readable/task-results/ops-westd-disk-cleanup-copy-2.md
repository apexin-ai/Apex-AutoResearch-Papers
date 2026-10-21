# ops westd disk cleanup

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_disk_cleanup_20260520T094742_result.json`
- **Structured JSON:** [`7b0b16f4c51b89265344.json`](../../sessions/7b/7b0b16f4c51b89265344.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

**结果**: /dev/md0 可用空间从 70G → **185G**，释放 115G，目标达成。

清理内容：
- 2 个 optimizer.pt（22G）
- 8 个冗余 checkpoint-100 目录（97G）——均已验证 root 目录有相同的最终模型

安全跳过了 grpo_cka_only_15、grpo_shortgpt_20、grpo_standard_15 的 checkpoint（无 root 模型，是唯一副本）。

报告已写入 `artifacts/westd_cleanup_report.md`。

---
