# ops data migration westd to westb

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_data_migration_westd_to_westb_20260524T155740_result.json`
- **Structured JSON:** [`73d0ebdebe91304621b4.json`](../../sessions/73/73d0ebdebe91304621b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**空间不足，无法完成全量迁移。**

数据摘要：

| | westd-32935 (源) | westb-23072 (目标) |
|---|---|---|
| autodl-tmp 总容量 | 未查 | **250G** |
| 项目数据大小 | **562G** | 205G |
| 可用空间 | — | **31G** |

westb 的数据盘总共只有 250G，即使清空所有现有数据也装不下 westd 的 562G。

两边的数据基本不重叠：
- **westd 独有**：大量 floor/alpha/seed ablation 实验（grpo_cka_only_20_floor_*, sft_standard_15/25, pruned_standard_15/25/30, 各种 seed 变体等），约 50+ 个 11-13G 的 checkpoint 目录
- **westb 独有**：1.5B 模型实验、qwen_math 实验、rasp_rlvr 等

**方案选项：**

1. **扩容 westb 数据盘** — AutoDL 控制台可以扩容，需要你手动操作
2. **选择性迁移** — 只迁移关键结果文件（results/、eval_*.json、logs/、artifacts/、*.log），跳过大 checkpoint 目录。这些小文件总共不到 1G
3. **只迁移 results + 必要 checkpoint** — 告诉我哪些 checkpoint 是论文必需的，其余跳过
4. **换一台更大磁盘的机器**

你要怎么处理？

---
