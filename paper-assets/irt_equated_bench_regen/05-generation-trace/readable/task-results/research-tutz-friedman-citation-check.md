# research tutz friedman citation check

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_tutz_friedman_citation_check_20260521T072415_result.json`
- **Structured JSON:** [`7885b6d00e2749eb1720.json`](../../sessions/78/7885b6d00e2749eb1720.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论

**"Tutz & Friedman (2007)" 不存在，是幻觉引用。**

### 证据

1. **多轮 Web 搜索全部未找到**：用 "Tutz Friedman 2007" 搭配 DIF、IRT、statistics、boosting 等关键词反复搜索，均无结果。

2. **Gerhard Tutz 2007 年的真实发表物**（DBLP 数据库确认）：
   - Tutz & Leitenstorfer (2007) — "Knot selection by boosting techniques", *Comp. Stat. & Data Analysis*
   - Tutz & Binder (2007) — "Boosting ridge regression", *Comp. Stat. & Data Analysis*
   - **没有与任何 Friedman 合作的论文**

3. **Tutz 在 DIF/IRT 领域的真实合作者**是 Berger (2016) 和 Schauberger (2015)，与 review_issues.yaml 中 R1 的独立判断一致。

4. **论文当前版本已不包含此引用** — `paper/` 目录和 `references.bib` 中均无 "Tutz" 字样。该引用可能仅出现在早期 dream report 草稿中，且已被清理。

### 建议

- 如果论文中需要引用 DIF 检测方法的树模型/正则化方法，**替换为真实引用**：
  - **Tutz & Berger (2016)** — "Item-Focused Trees for the Identification of Items in Differential Item Functioning", *Psychometrika* — 这是 Tutz 在 DIF 领域最相关的论文
  - **Tutz & Schauberger (2015)** — 如果涉及有序响应的 DIF
- 如果论文当前版本已不引用此文献，则 **review issue R2-N1 可以关闭**。

---
