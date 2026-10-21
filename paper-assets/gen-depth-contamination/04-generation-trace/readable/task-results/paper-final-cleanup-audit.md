# paper final cleanup audit

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_final_cleanup_audit_20260517T074016_result.json`
- **Structured JSON:** [`ec774a1a46537198be62.json`](../../sessions/ec/ec774a1a46537198be62.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 1. Dash 检查（Em-dash / 解释性 En-dash）
状态：✅ 无问题

仅在注释行发现 2 处 em-dash，均不在正文中：
1. `main.tex:1` — `% EMNLP 2026 Main — ARR May 2026`（LaTeX 注释）
2. `references.bib:2` — `% Source: literature_map.yaml — verified 2026-05-15`（bib 注释）

解释性 en-dash（` – `）：0 处。

---

## 2. -ing Phrase 检查
状态：✅ 无问题

匹配到 ~10 处 `[a-z]ing,` 模式，但均为正常学术用语（如 "resampling,""ordering,""narrowing,"），无 AI 典型标志性句尾 -ing 短语（如 ", demonstrating the effectiveness of..."）。bib 文件中的匹配为格式性内容（`inproceedings,` 等），无需处理。

---

## 3. Reference 一致性检查
状态：⚠️ 有 2 处小问题

### 问题列表
1. **`references.bib: basani2026diveye`** — `@article` 条目缺少 `volume` 和 `pages` 字段。若论文已发表可补充；若为 accepted/in press 则可接受。
2. **NeurIPS venue 命名不一致** — 3 篇 NeurIPS 论文（`tirumala2023d4`, `xie2023doremi`, `krishna2023paraphrasing`）使用 `"Advances in NeurIPS"`，其余会议均用 `"Proceedings of ..."`。建议统一为 `"Advances in Neural Information Processing Systems"` 或 `"Proceedings of NeurIPS"`。

断裂引用：0 处。孤立条目：0 处。作者名格式：全部一致（`Last, First`）。Title 大小写保护：全部已正确使用花括号。

---

## 4. Figure/Table Caption 自包含性
状态：⚠️ 有 7 处问题（4 处明确问题 + 3 处 borderline）

### 问题列表

**明确问题：**

1. **`method.tex:59`** `\caption{Experimental configurations.}` → 过于简短，缺少列含义说明。建议改为：*"Summary of model configurations. Config: shorthand label; Model: architecture and size; Mode: generation strategy (rewrite or continuation); $N$: number of seed documents per depth level."*

2. **`experiments_c1.tex:102`** `\caption{Neural probe $\auc$ (frozen-encoder MLP).}` → 缺少列说明和 depth pair 上下文。建议补充被比较的深度对、$K^*_{\text{neural}}$ 含义。

3. **`experiments_c1.tex:128`** `\caption{Cross-domain $\Kempirical$ (arXiv vs.\ C4/Wikipedia).}` → 过于简短，"vs." 用法歧义（实际是三个 domain 并列）。建议补充列定义和行含义。

4. **`experiments_c3.tex:11`** `\caption{Downstream filtering performance (5 seeds).}` → 过于模糊，未说明 metric（MMLU/HellaSwag）、filtering 策略、seed 用途。

**Borderline：**

5. **`experiments_c1.tex:55`** `$\Kempirical$ vs.\ $\theta$` caption — 使用 $K^*_{\text{empirical}}$ 和 $\theta$ 但未在 caption 内定义。建议加括号注释。

6. **`experiments_c1.tex:69`** 转移 heatmap caption — 未解释行/列语义和 "retention" 计算方式。

7. **`appendix_extended.tex:100`** `MMLU by contamination ratio and filtering strategy` — 未定义 "contamination ratio" 和 filtering strategy 具体含义。

---
