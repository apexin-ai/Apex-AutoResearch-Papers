# paper bib audit r10

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_bib_audit_r10_20260516T032723_result.json`
- **Structured JSON:** [`11e3a09db957eb61c9b1.json`](../../sessions/11/11e3a09db957eb61c9b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果如下：

**MUSTAFAR 状态**：`mustafar-neurips2025` 已不在 `references.bib` 和所有 `.tex` 文件中（此前已删除）。无需额外修改 bib/tex。

**全量审计结果（42 条）**：
- ✅ 39 条完全验证通过
- ⚠️ 3 条有轻微问题（均非学术诚信问题）：
  - `snapkv-neurips2024`：标题大小写 "You Are" vs "You are"（纯格式）
  - `hold-onto-thought-neurips2025`：实际发表于 NeurIPS 2025 ER Workshop 而非主会（bib 标注为 arXiv preprint，不算错误）
  - `deepseek-r1-2025`：作者用 "DeepSeek-AI"（arXiv 惯例），Nature 版用个人作者名
- ❌ 0 条伪造

**产出文件**：
- `artifacts/_project/report/bib_audit_r10.md` — 完整审计报告
- `artifacts/_project/paper/citation_audit_report.md` — 旧报告已标注 MUSTAFAR 为 ❌ FAKE 并标记为 superseded

---
