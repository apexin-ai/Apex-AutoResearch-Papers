# diagnosis melt check and latex

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_melt-check-and-latex_20260519T235258_result.json`
- **Structured JSON:** [`131fc3aac94a0e0bb7fa.json`](../../sessions/13/131fc3aac94a0e0bb7fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/extended-task-validation/final_latex_table.md`。

**状态总结：**

- **Melt**: 11/20 episodes，rerun 在跑（首次 run 因 vllm EngineDeadError 崩溃后重启）
- **LaTeX 表格**: 已生成 4-task 版本（melt 行标 `---`），附带 5-task 占位模板
- **4-task 聚合**: n=80, Int DR=52.5%, Det DR=18.8%, ΔDR=+33.8pp, D/I/N=30/1/49
- **DAF**: 聚合 DAF=**0.987** — 98.7% 的 det-vs-int 差距来自死亡不对称。37 个双存活 episode 中 Δ_nd 仅 0.46 分，几乎可忽略。只有 find-living-thing 有微弱的非死亡差异（DAF=0.954），其余三个任务 DAF=1.000（非死亡 episode 完全平局）。

---
