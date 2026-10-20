# analysis bootstrap crossdomain fix

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bootstrap-crossdomain-fix_20260514T214206_result.json`
- **Structured JSON:** [`bea4452590421a4d729c.json`](../../sessions/be/bea4452590421a4d729c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifact registered (`art_20260514_f2255d`).

**结果汇总：**

| | Task 1: GB vs Probe (OH test) | Task 2: RF vs Probe (SWE-agent) |
|---|---|---|
| n | 20,807 | 1,824 |
| Method A F1 | GB = 0.9767 | RF = 0.9951 ✓ |
| Method B F1 | Probe = 0.6443 | Probe = 0.9055 |
| Delta | +0.3324 | +0.0896 |
| 95% CI | [0.3241, 0.3407] | [0.0744, 0.1057] |
| p-value | < 0.001 | < 0.001 |

**关键发现：** Probe 在 OH test split 上 F1 只有 0.6443，远低于 GB 的 0.9767。原因是 OH `embeddings.pt` 的标签是过期版本（stagnation rate 6.6%），而 `windows_labeled.jsonl` 当前标签（stagnation rate 21.4%）才是 ground truth。Probe 在旧标签上训练，用新标签评估自然偏差大。

Task 2 RF F1 = 0.9951，完全匹配预期值。

---
