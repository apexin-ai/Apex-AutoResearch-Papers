# audit ref verify w1

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_ref-verify-w1_20260526T101812_result.json`
- **Structured JSON:** [`858cb0fd714c5a6c964f.json`](../../sessions/85/858cb0fd714c5a6c964f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成，报告已写入 `artifacts/ref_audit_worker1.md`。

核心发现：
- **48 条引用全部真实存在**，无虚构论文
- **5 个严重问题**：`schulman2015trpo` 作者顺序错、`lightman2024lets` 两个作者名拼写错（Yuri→Yura, Harrison→Harri）、`istar2025` 已被 ICLR 2026 接收但仍标为 arXiv、`kazemnejad2024vineppo` 标题为旧 preprint 版本、`gradientcoupling2025` 标题为 v1 但论文已在 v2 更名
- **3 个中等问题**：`turnppo2025` venue 待更新、`ouyang2022instructgpt` 作者名 Jeffrey→Jeff、`ahmadian2024back` 缺连字符
- **14 个 bib entry 未被引用**，其中 `gradientcoupling2025`/`sweetrl2025`/`mtgrpo2025`/`istar2025` 与论文主题高度相关，建议补引或清理

---
