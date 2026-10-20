# data annotation fix

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_annotation-fix_20260514T115316_result.json`
- **Structured JSON:** [`42d91c7719e904af1945.json`](../../sessions/42/42d91c7719e904af1945.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。3 个文件已写到 `artifacts/` 目录：

**annotation_sample_650.csv** — 650 行标注样本
- 450 SWE-agent + 200 OpenHands
- 列：id, trajectory_id, window_idx, confidence, agent_actions, annotator_label, source
- `majority_label` 和 `trajectory_outcome` 已移除（修复 1）

**annotation_mapping.csv** — 650 行隐藏元数据
- 含 majority_label, trajectory_outcome, source, is_calibration, 3 个 LF 值
- 30 个校准样本标记 `is_calibration=True`（修复 2）
- 20 个 LF 全盲区窗口（3 个 LF 全部 abstain，majority_label=-1）（修复 3）
- 200 个 OpenHands 窗口（c1=120, c2=60, c3=20）（修复 4）

**annotation_guide.md** — 更新后的标注指南
- 新增校准流程：独立标注 30 个校准样本 → 计算 Fleiss' κ → 讨论分歧 → 正式标注

---
