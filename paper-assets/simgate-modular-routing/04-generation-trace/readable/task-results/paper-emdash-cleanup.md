# paper emdash cleanup

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_emdash-cleanup_20260521T135011_result.json`
- **Structured JSON:** [`8f40bb1546ca8a01e8d1.json`](../../sessions/8f/8f40bb1546ca8a01e8d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 替换清单

1. [abstract.tex:2] `routing---deciding when to rely on internal reasoning versus external tool use---is` → `routing (deciding when to rely on internal reasoning versus external tool use) is` (插入语→括号)
2. [abstract.tex:2] `death asymmetry---the internal strategy triggers catastrophic failure while the deterministic strategy survives` → `death asymmetry: the internal strategy triggers...` (定义→冒号)
3. [abstract.tex:2] `mechanisms---no extractable signal and information asymmetry, respectively---demonstrating` → `mechanisms (no extractable signal and information asymmetry, respectively), demonstrating` (插入语→括号)
4. [introduction.tex:4] `error-prone---the model may hallucinate...activated)---while` → `error-prone, as the model may hallucinate...activated), while` (插入语→逗号)
5. [introduction.tex:15] `death asymmetry---a single mechanism` → `death asymmetry, a single mechanism` (定义→逗号)
6. [experiments.tex:18] `ties---neither strategy outperforms the other---indicating` → `ties (neither strategy outperforms the other), indicating` (插入语→括号)
7. [experiments.tex:78] `probes---not cross-domain validation---testing` → `probes (not cross-domain validation), testing` (插入语→括号)
8. [experiments.tex:82] `admissible actions---an information asymmetry` → `admissible actions, an information asymmetry` (定义→逗号)
9. [experiments.tex:82] `asymmetry---not death avoidance---drives` → `asymmetry, not death avoidance, drives` (插入语→逗号)
10. [experiments.tex:112] `task-type-level---there is no step-level pattern` → `task-type-level: there is no step-level pattern` (定义→冒号)
11. [experiments.tex:112] `data regime---though` → `data regime, though` (转折→逗号)
12. [main.tex:43] `mismatch---applying correct-direction labels to uninformative steps---not` → `mismatch (applying correct-direction labels to uninformative steps), not` (插入语→括号)
13. [main.tex:52] `routing---for example, by combining DAF analysis with online policy learning---is` → `routing (for example, by combining DAF analysis with online policy learning) is` (插入语→括号)
14. [method.tex:67] `fraction---invariant to penalty magnitude---serves` → `fraction, invariant to penalty magnitude, serves` (插入语→逗号)
15. [related_work.tex:15] `rewards---the closest setting to ours;` → `rewards, the closest setting to ours;` (定义→逗号)
16. [保留] [introduction.tex:6] `assumption---that routing signal stems from diverse sources and a learned router can exploit it---remains untested` — 核心论点的修辞强调
17. [保留] [experiments.tex:107] `always-deterministic---an \emph{oracle degeneracy}` — 引入命名概念
18. [保留] [method.tex:75] `steps---a granularity mismatch, not label error---explaining` — 关键方法论澄清
19. [保留] [main.tex:777] `tasks---the opposite of a cherry-picking bias` — 强对比

## 统计
- 总 em-dash（正文）: 19 处 (修复前)
- 替换: 15 处
- 保留: 4 处
- 最终: 4 处 (目标 3-5 ✓)
- 表格占位符 `---`: 8 处 (未动)

## 编译结果
- Errors: 0
- 总页数: 25

## Page 8/9 边界
- Page 8 末尾: Conclusion 开头 "In ScienceWorld, death avoidance alone accounts for 78.9% of non-tie routing labels... a ~50-episode pilot suf-"
- Page 9 开头: "-fices for build-vs-buy decisions in new environments." 然后 Limitations
- ⚠️ **OVERFLOW**: Conclusion 溢出到 page 9（约 2 行），Limitations 从 page 9 line 668 开始

---
