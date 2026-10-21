# viz selection gap significance

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_selection_gap_significance_20260514T234434_result.json`
- **Structured JSON:** [`02f99ce4cc327b3ce2ba.json`](../../sessions/02/02f99ce4cc327b3ce2ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图表已生成。结果：

- **NER 面板**：3 个信号均有 bootstrap 95% CI error bars，标签改为 "+0.1 n.s."、"-1.0 n.s."、"+0.6 n.s."
- **RE 面板**：无 error bars（无 bootstrap 数据），标签也加了 "n.s."
- 标题已从 "N=1024" 改为 "N=8"
- Oracle/random 标注保留

输出文件：
- `artifacts/figures/fig_selection_gap_1024.pdf`
- `artifacts/figures/fig_selection_gap_1024.png`
- 脚本：`artifacts/figures/plot_selection_gap_1024_v2.py`

---
