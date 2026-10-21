# research ref audit worker 1

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_ref-audit-worker-1_20260526T102052_result.json`
- **Structured JSON:** [`6933a55330b3c4a29dc3.json`](../../sessions/69/6933a55330b3c4a29dc3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。结果写入 `ref_audit_worker1.md`。

**核心发现：**

| 严重级别 | 条目 | 问题 |
|---------|------|------|
| **CRITICAL** | `human_texts_outliers` | arXiv:2510.08602 的真实作者是 Cong Zeng 等人，标题副标题也不同，bib 中的作者和标题是幻觉生成的 |
| **ERROR** | `diveye` | 会议写的 ICLR 2026，实际发表在 TMLR 2026 |
| **WARNING** | `xu_spectrum_detection` | 已发表于 EMNLP 2024，但仍标为 arXiv preprint |
| **WARNING** | `beyond_final_actor` | ACL 2026 未能从官方接收列表独立确认 |

另外发现 **25 条 bib entry 在所有 tex 文件中未被引用**（详见报告末尾列表），编译时会产生 warning，建议清理或补充引用。

---
