# analysis oh error analysis debug

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_oh-error-analysis-debug_20260515T012051_result.json`
- **Structured JSON:** [`5ff32216b51ee75f791c.json`](../../sessions/5f/5ff32216b51ee75f791c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

排查完成，汇总结果：

## W1: Probe ZS macro_f1 (0.581 vs 0.5984)

**根因：评估范围不同，非 checkpoint 错误。**

- 0.5984 是 `fewshot_probe.py` / `oh_retrain_eval.py` 在 **test split**（6,122 windows，70/15/15 instance-level split）上的结果
- 0.5810 是 error analysis 在 **全部 43,366 conf>=2 windows** 上的结果
- 两者使用同一 checkpoint（`checkpoints_full/best_model.pt`, epoch 9）
- **0.5810 对于全量评估是正确的**，不需要修代码使其匹配 0.5984

注意：`checkpoints/best_model.pt`（epoch 3, val_f1=0.9511）是另一个 checkpoint，在全量 conf>=2 上给出 0.7588 — 这不是论文使用的 checkpoint。

## W2: Error overlap 28% → 100%

**根因：embeddings 和 windows_labeled.jsonl 之间的位置对齐错误。**

- `embeddings_fixed.pt` 有 143,057 条，`non_abstain_windows` 有 150,652 条
- 原代码用位置索引 `non_abstain_windows[i]`，但两者数量不同、顺序不同（142,688/143,057 位置错配）
- **修复**：改用 `(trajectory_id, step_indices)` 作为 key 进行精确匹配，100% 命中

## 修正后关键指标

| 指标 | 修正前 | 修正后 |
|------|--------|--------|
| Probe ZS macro_f1 (all conf>=2) | 0.5810 | 0.5810（无变化，checkpoint 不变） |
| Error overlap coverage | 12,328 (28.4%) | **43,366 (100%)** |
| Probe errors (on matched) | 2,460 | **8,643** |
| Both error | 2 | **31** |
| Probe-only errors | 2,458 | **8,612** |
| Struct-only errors | 11 | **26** |
| Overlap rate (probe→struct) | 0.08% | **0.4%** |

产出文件：
- `results/oh_crossagent_error_analysis_v2.json` — 修正后的完整分析结果
- `results/oh_error_debug_report.txt` — 排查报告

---
