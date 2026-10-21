# paper reference audit

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_reference-audit_20260522T010830_result.json`
- **Structured JSON:** [`b7fd3a7988a04d78aab2.json`](../../sessions/b7/b7fd3a7988a04d78aab2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。

**已自动修复 6 项**（arXiv → 正式发表版本）：
- `tripathi2025pairwise` → COLM 2025
- `wang2023faireval` → ACL 2024（补全作者 Kong, Lingpeng）
- `li2024calibraeval` → ACL 2025
- `ye2024justice` → ICLR 2025（补全 2 位缺失作者）
- `he2021debertav3` → ICLR 2023
- `shi2024judging` → IJCNLP-AACL 2025

**交叉引用**：53 条 bib 全部被 tex 引用，tex 中无缺失引用，无冗余条目，无重复。

**Tripathi (R7-REF1)**：已正确包含并引用于 `experiments.tex:135`，已从 arXiv 升级为 COLM 2025。

**6 条仍为 arXiv preprint**（未找到正式版本）：wang2026fairjudge、casse2026concise、counterfactual2025rhetorical、soumik2026judging、celikyilmaz2020evaluation、stureborg2024inconsistent。

**需人工确认 4 项**见报告末尾（key 命名不规范、`and others` 缩写、老 preprint 是否替换）。

报告路径：`artifacts/reference_audit_report.md`

---
