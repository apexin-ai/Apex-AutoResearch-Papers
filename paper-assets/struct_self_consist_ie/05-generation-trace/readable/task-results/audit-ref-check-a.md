# audit ref check A

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_ref-check-A_20260526T101756_result.json`
- **Structured JSON:** [`f7d5faf00a787454e26b.json`](../../sessions/f7/f7d5faf00a787454e26b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/ref_audit_worker_A.md`。

**核心结论**：64 条 bib entries 全部真实存在，无虚假引用。

**需修正（3 项）**：
1. **[li2023stepaware]** — 标题多了 "Large"，ACL 2023 proceedings 无此词
2. **[yee2019noisy]** — 作者列表（3人）与 bib 中 arXiv URL 指向的版本（4人，含 Nathan Ng）不一致
3. **[holm1979simple]** — Holm-Bonferroni 方法在正文中被引用 15+ 次但从未 `\cite`，bib entry 未被使用

**需关注（3 项）**：
- `snell2025scaling`: arXiv 与 ICLR proceedings 标题不同，bib 使用 proceedings 版，可接受
- `xu2024llmie`: 作者 "Wang, Yang" 在 S2 中缺失，需对照出版商确认
- `li2024simple`, `xiao2022uncertainty`: 在 bib 中但未被引用，建议删除或添加引用

---
