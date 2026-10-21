# fix cls predictions plan b

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_cls-predictions-plan-b_20260519T160337_result.json`
- **Structured JSON:** [`833f5ecd3926bb9e277d.json`](../../sessions/83/833f5ecd3926bb9e277d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总如下：

---

### 修改汇总

**1. `docs/paper/appendix.tex` 行 293**
| 字段 | Before | After |
|------|--------|-------|
| Fail F1 | 87.86% | 87.59% |
| Fail Precision | 82.75% | 86.20% |
| Fail Recall | 93.64% | 89.04% |
| "42.1% perfectly predicted" | 存在 | 已删除 |

添加了 LaTeX 注释标注来源：`derived from overlap analysis (error_overlap_matched_seed.json); FP=130, FN=100, TP=848, TN=812`

**2. `artifacts/paper_materials.md`**
- 行 166：删除 "48 (42.1%) perfect prediction"，标注为 suspect checkpoint 数据
- 行 175-177 Majority Voting 表 Greedy 列：87.51→87.83, 87.86→87.59, 87.15→88.06，Delta 相应更新

**3. `artifacts/comprehensive_results_summary.md`**
- CLS 4B s42 行（行28）已有正确值（87.83/88.06/87.59/89.45/86.71/86.20/89.04），无需修改

**4. 远程 suspect 文件**
- `predictions_cls_seed42.jsonl` → `predictions_cls_seed42.jsonl.SUSPECT` ✓

### 内部一致性验证
- TP=848 + TN=812 + FP=130 + FN=100 = 1890 ✓
- correct = 848+812 = 1660, accuracy = 1660/1890 = 87.83% ✓
- Pass P = 848/(848+100) = 89.45%, R = 848/978 = 86.71%, F1 = 88.06% ✓
- Fail P = 812/(812+130) = 86.20%, R = 812/912 = 89.04%, F1 = 87.59% ✓
- Oracle accuracy 90.63% 未修改 ✓

> 注意：Majority Vote K=3 列（86.83/87.29/86.33）也来自同一 suspect checkpoint，无法通过 overlap 反推修正，需重跑实验才能更新。

---
