# research citation audit 1

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_citation-audit-1_20260526T101436_result.json`
- **Structured JSON:** [`44d36505be40a926a5cb.json`](../../sessions/44/44d36505be40a926a5cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。报告已写入 `artifacts/citation_audit_worker1.md`。

核心发现：

**3 个关键错误：**
1. **`laban2025lost`** — 已发表于 ICLR 2026（Oral + Best Paper），但 bib 仍引为 arXiv 2025 预印本
2. **`raposo2024mixture`** — 会议写错：实际是 ICLR 2025，bib 写成 ICML 2024
3. **`he2019exposure`** — 已发表于 EMNLP 2021 且标题完全改变（"Exposure Bias versus Self-Recovery..."），bib 仍用 2019 arXiv 旧标题

**2 个次要问题：**
4. **`brunner2020identifiability`**（未被引用）— 末位作者 "Andreas Krause" 应为 "Roger Wattenhofer"
5. **`bachlechner2021rezero`** — 作者名应为 "Huanru Henry Mao" 和 "Garrison W. Cottrell"

**0 篇幻觉论文。** 全部 58 条 bib entry 均真实存在。12 条在 bib 中但未被正文引用。46 条被引用的论文中，41 条完全正确，上下文使用均准确。

---
