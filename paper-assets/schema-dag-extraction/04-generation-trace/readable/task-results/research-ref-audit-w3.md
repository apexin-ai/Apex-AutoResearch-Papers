# research ref audit w3

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_ref-audit-w3_20260526T103506_result.json`
- **Structured JSON:** [`f0d8657007337550d22d.json`](../../sessions/f0/f0d8657007337550d22d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。59 条引用全部经 WebSearch 验证，无幻觉论文。

**3 个必须修复的错误**：
1. **baan-2023-ecological** — key 写了 "baan" 但作者里没有 Baan（实际是 Orlikowski 等人），需改 key 并更新所有 cite
2. **reflect-learn-2026** — 作者 "Li, Shaoyuan" 应为 "Li, Shao-Yuan"（带连字符）
3. **promptner-2023** — 已被 ICLR 2024 接收，bib 仍引 arXiv，应改为 ICLR 2024 正式版

**8 个建议关注项**（⚠）：主要是 arXiv preprint 可能已被正式接收（dlisc-2025/spt-2025/chen-2026-multi-instance），以及若干 venue 命名惯例差异。

报告已写入 `artifacts/_project/report/ref_audit_worker3.md`。

---
