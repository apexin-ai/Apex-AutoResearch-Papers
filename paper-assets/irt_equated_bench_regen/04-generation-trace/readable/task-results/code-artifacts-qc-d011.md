# code artifacts qc d011

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_artifacts_qc_d011_20260520T234539_result.json`
- **Structured JSON:** [`01cdc1763389346344ba.json`](../../sessions/01/01cdc1763389346344ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

QC 完成。结论：

- **9/9 已完成实验**的 artifacts 完整（report + 数据 CSV 全在，非空，列名合理）
- **2 个非终态实验**状态符合预期（plan_015 PREPARING+killed，plan_017 PREPARING）
- **3 个 minor issues**：
  1. `mmlu_cf_ground_truth` manifest 路径指向 `artifacts/` 根目录，实际在 `_project/data/`
  2. `plan_001b` registry 缺 structured metrics（数据在 CSV 和 notes 里，只是没结构化）
  3. `mvp_dif_power_sim_phase2` registry 缺 notes 字段

均不影响数据完整性。报告已注册为 `art_20260520_cbdba2`。

---
