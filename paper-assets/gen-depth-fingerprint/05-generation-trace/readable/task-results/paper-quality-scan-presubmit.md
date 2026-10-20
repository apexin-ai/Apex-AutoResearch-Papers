# paper quality scan presubmit

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_quality-scan-presubmit_20260522T224640_result.json`
- **Structured JSON:** [`aa21e6e807345f8b2693.json`](../../sessions/aa/aa21e6e807345f8b2693.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 全文质量扫描报告

---

### CRITICAL (3)

| # | 类别 | 文件 | 行 | 问题 |
|---|------|------|----|------|
| C1 | 页限 | `conclusion.tex` | 1 | `\enlargethispage{8\baselineskip}` — ARR format checker 会直接 flag |
| C2 | 页限 | 14处 `.tex` 文件 | 多处 | 共 14 个 `\vspace{-Xmm}` 负值间距（conclusion 2处、discussion 3处、method 1处、results 4处、limitations 2处、main 2处）— format checker 标记风险高 |
| C3 | 页限 | `main.tex` | 46 | `\raggedbottom` 覆盖了 ACL style 的 `\flushbottom`，可能被 flag |

**影响**：如果 ARR 2026 使用自动 format checker（大概率），C1 几乎必定被拒格式审查。C2 风险视 checker 严格程度而定。建议全部移除，通过精简内容来满足页限。

---

### WARNING (2)

| # | 类别 | 文件 | 问题 |
|---|------|------|------|
| W1 | Related Work | `related_work.tex` | `reliable_detection` (Sadasivan, TMLR 2025) 已在 bib 中但未引用 — 与深度估计的鲁棒性直接相关 |
| W2 | Related Work | `related_work.tex` | `koike_mia_detection` (arXiv 2025) 已在 bib 中但未引用 — 与论文 NLL/MIA 分析线直接相关，应与 `min_k_percent` 共引 |

---

### INFO (3)

| # | 类别 | 文件 | 问题 |
|---|------|------|------|
| I1 | 引用 | `references.bib` | `drayson_detection_prevents_collapse` 存在于 bib 但全文未引用（孤儿条目）|
| I2 | 术语 | 全文 | DDR / "generation depth" / "depth profiling" 等核心术语 **一致性良好**，无混用 |
| I3 | Hedge | abstract + conclusion | "approximately preserved" 在 abstract 和 conclusion 中均出现；"near-stationary" 跨 4 个章节一致使用；无 overclaiming |

---

### 通过项 (无问题)

- **数字一致性** ✅ — Abstract 中 F1=0.694, 0.762, 0.905, d=0.76–1.17 与 results.tex 完全一致
- **交叉引用** ✅ — 154 个 `\ref{}` 全部有对应 `\label{}`，无悬空引用
- **拼写/语法** ✅ — 无双空格、重复词、缺失句号
- **Hedge 一致性** ✅ — "approximately preserved" 在 conclusion 中存在，无 CRITICAL
- **2025-2026 引用覆盖** ✅ — bib 中 17 篇 2025-2026 论文，13 篇已引用（76%），覆盖 model collapse、detection、watermark 主要方向

---

### 建议优先级

1. **立即处理**：移除 `\enlargethispage` 和所有负 `\vspace`，通过内容精简解决页限
2. **提交前处理**：补引 `reliable_detection` 和 `koike_mia_detection`，删除孤儿 bib 条目
3. **可选**：移除 `\raggedbottom`

---
