# data annotation materials

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_annotation_materials_20260514T102725_result.json`
- **Structured JSON:** [`15623f3a454806d31de5.json`](../../sessions/15/15623f3a454806d31de5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件都已生成。汇总结果：

### 产出

| 文件 | 路径 | 大小 |
|------|------|------|
| 标注样本 | `artifacts/annotation_sample_450.csv` | 993KB, 450 行 |
| 标注指南 | `artifacts/annotation_guide.md` | 3KB |

### 采样统计

**Confidence 分层**（总池 → 采样数）：
- c1: 39,408 → 250（progress=188, stagnation=62）
- c2: 14,609 → 150（progress=95, stagnation=55）
- c3: 792 → 50（progress=18, stagnation=32）

**总标签分布**：progress=301 (66.9%), stagnation=149 (33.1%)

**Trajectory outcome 分布**：
- submitted: 143
- submitted (exit_context): 210
- exit_context: 77
- early_exit: 16
- submitted_no_patch: 4

**CSV 列序**：id, trajectory_id, window_idx, confidence, agent_actions, annotator_label, **majority_label, trajectory_outcome**（后两列标注时隐藏）。

---
