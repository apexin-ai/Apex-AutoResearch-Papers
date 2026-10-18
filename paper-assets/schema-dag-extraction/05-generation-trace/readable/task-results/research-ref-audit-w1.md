# research ref audit w1

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_ref-audit-w1_20260526T101506_result.json`
- **Structured JSON:** [`2fa2f10e28701fafe837.json`](../../sessions/2f/2fa2f10e28701fafe837.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。63 条引用逐条通过 WebSearch 验证，结果：

**✗ 1 个错误（必须修复）：**
- `peterson2019human`：页码 `9617--9626` 应为 `9616--9625`（差一页）

**⚠ 2 个警告（建议修复）：**
- `golde-2025-familiarity`：booktitle 用了旧名 "North American Chapter"，NAACL 2025 已改名 "Nations of the Americas Chapter"（同文件 `boylan-2025-glirel` 已用新名，不一致）
- `baan-2023-ecological`：bib key 含 "baan" 但无此作者（第一作者为 Orlikowski），不影响编译但易造成混乱

**无虚构论文。** 所有 63 篇引用均真实存在，作者/标题/年份/venue 信息正确。引用上下文也无错位使用。

报告已写入 `artifacts/_project/report/ref_audit_worker1.md`。

---
