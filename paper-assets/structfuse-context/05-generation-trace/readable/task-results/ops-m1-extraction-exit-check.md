# ops m1 extraction exit check

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_m1-extraction-exit-check_20260513T105724_result.json`
- **Structured JSON:** [`fe67962f20a368137be6.json`](../../sessions/fe/fe67962f20a368137be6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

**结论：M1 提取正常完成。**

- **123/131 repos** 处理完毕 (93.9% 覆盖率)
- **15,897/44,173** instances 有结构数据 (36.0%，其中 CodeQL 15133 + Beniget 764)
- **28,276** instances 提取失败 (无结构信息但有输出文件)
- **6,696** instances 被跳过 (5852 clone 失败 + 836 checkout 失败)
- 输出：`all.jsonl` 6.6GB，耗时 ~14h
- 磁盘 88% (21GB 剩余)，清理守护进程仍在运行
- 剩余 2 个未清理 repo (sqlglot, flashtext)

---
