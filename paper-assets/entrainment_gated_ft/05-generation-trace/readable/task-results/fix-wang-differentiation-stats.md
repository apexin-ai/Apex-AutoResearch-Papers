# fix wang differentiation stats

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_wang_differentiation_stats_20260519T133238_result.json`
- **Structured JSON:** [`8140a374556e2547b097.json`](../../sessions/81/8140a374556e2547b097.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已审查完毕。**未发现任何需要修正的错误**：

**错误 1 ("4/6 benchmarks")**: 文件中不存在 "4/6"、"four of six"、"majority"、"most benchmarks" 等表述。文件已正确记录：
- LAMBADA: ρ=-1.0, p=0.0083（显著）
- ARC-Easy, MMLU: ρ=-0.7, p=0.117（suggestive, underpowered）
- HellaSwag: ρ=+0.3, p=0.742（无收敛）
- ARC-Challenge: ρ=+0.6, p=0.883（无收敛）
- Winogrande: ρ=+0.1, p=0.608（无收敛）

这些数值与你提供的"实际数据"完全一致，出现在文件的至少 3 处（Section 1 详述、Section 4 task-specificity、Summary Table）。

**错误 2 ("7B 计划")**: 文件中不存在 "7B"、"three-point"、"89%"。唯一的 scale 讨论是 340M vs 1.3B 对比，与实际情况一致。

**结论**: `wang_et_al_differentiation.md` 的统计 claims 已经是正确的，无需修改。

---
