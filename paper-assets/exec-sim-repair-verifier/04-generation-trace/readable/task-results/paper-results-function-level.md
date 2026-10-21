# paper results function level

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_results-function-level_20260512T210301_result.json`
- **Structured JSON:** [`cd2f606ededf18d19cb6.json`](../../sessions/cd/cd2f606ededf18d19cb6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`docs/paper/experiments.tex` 已经包含了任务要求的全部内容：

| 任务要求 | 已有位置 | 状态 |
|---|---|---|
| §5.1 Function-level CLS vs CWM | `sec:func_results` (L30-56) | ✅ 有表格+5-seed means |
| §5.2 Model-Size Scaling | `sec:scaling` (L59-84) | ✅ 有表格+bootstrap CI |
| §5.3 CLS vs TRAJ Equivalence | `sec:equivalence` (L87-96) | ✅ TOST p=0.007 |
| §5.4 Oracle Frontier | `sec:oracle` (L99-128) | ✅ 有表格+stratified analysis |
| §5.5 Repo-level | `sec:repo` (L130-148) | ✅ placeholder |
| §5.6 Analysis | `sec:analysis` (L151-164) | ✅ error complementarity, majority voting, block correlation |

有几处与任务描述的差异：

1. **4B CLS-CWM bootstrap 统计量缺失**：experiments.tex 只写了 gap=1.24pp，没有报告 paired bootstrap 的 p=0.025、CI [0.46, 2.04]
2. **Error overlap 数据不一致**：experiments.tex 用非配对 oracle 90.63%，memory.md 中配对分析是 90.14%（+complementarity 34%, Jaccard 66%）
3. **任务 §5.1 中 TOST gap=-0.45pp 实际是 CLS vs TRAJ**（已正确放在 §5.3），不是 CLS vs CWM（CLS vs CWM 的 TOST p=0.0855，不等价）

experiments.tex 已经是完整的 Results section，不需要额外创建 results.tex。要我补上缺失的 4B bootstrap 统计量和更新 matched-seed oracle 数据吗？

---
