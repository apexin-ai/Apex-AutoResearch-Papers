# paper table1 ci fix

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_table1-ci-fix_20260514T145609_result.json`
- **Structured JSON:** [`36dc5bb5d99cb0ab13d1.json`](../../sessions/36/36dc5bb5d99cb0ab13d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。变更汇总：

**`docs/paper/experiments.tex`**（3 处修改）：
1. **表头** `90\% CI` → `95\% CI`
2. **表格 5 行数据**全部替换为 registry plan-003-bootstrap-95ci 的值
3. **caption** `90\% confidence intervals computed via bootstrap` → `95\% Bootstrap CIs`
4. **正文 End-to-end evaluation 段落**中两处内联 CI 值和标注从 90% 更新为 95%

**`artifacts/_project/paper/latex/experiments.tex`** — 已经是 95% CI + 正确数值，无需修改。

Death % 列两处均为 42.9/16.3/27.8/14.3/17.6%，一致。全文已无 90% CI 残留。

---
