# paper checklist items 134

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_checklist-items-134_20260521T093818_result.json`
- **Structured JSON:** [`2d570b2d25be0b0fa139.json`](../../sessions/2d/2d570b2d25be0b0fa139.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译成功，无错误，输出 23 页 PDF。

三处修改：
1. **Appendix I** (Router Training Details)：添加了 agent inference parameters 段落——ScienceWorld T=0.3/256 tokens，MATH T=0.0/2048 tokens，ALFWorld T=0.3/256 tokens，均通过 vLLM v0.21.0 服务
2. **Appendix C** (Per-Task Decomposition)：开头添加 ScienceWorld v1.2.3 版本声明
3. **Appendix L** (Cross-Environment Details)：ALFWorld 表格后添加 MATH subset composition——Algebra 585 (73.6%)、Counting & Probability 210 (26.4%)，共 795 题（注：实际数据仅含这 2 个类别，非预期的 7 个）

---
