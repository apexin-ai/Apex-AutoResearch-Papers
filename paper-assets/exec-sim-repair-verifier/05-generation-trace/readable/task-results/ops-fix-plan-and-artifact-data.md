# ops fix plan and artifact data

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-plan-and-artifact-data_20260514T005608_result.json`
- **Structured JSON:** [`7657b0de1e909c1a6f72.json`](../../sessions/76/7657b0de1e909c1a6f72.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

### 任务 1: experiment_plan.yaml registry_id 映射

| plan id | registry_id | conclusion | 关键指标 |
|---------|-------------|------------|---------|
| per-test-precision-recall | `per-test-precision-recall` | success | accuracy=87.51% |
| block-corr-empirical | `block-corr-empirical` | success | ICC=0.1909 |
| per-test-majority-voting | `per-test-majority-voting` | negative | accuracy_mv=86.83% |

三个 `registry_id` 已写入 experiment_plan.yaml。

### 任务 2: unparseable_pct 修正

| 实验 | 原值(计数) | 修正值(百分比) | 计算方式 |
|------|-----------|--------------|---------|
| repo-level-cwm-v11 | 376 | 75.2% | 376/500×100 |
| repo-level-cls-8b | 136 | 1.39% | 136/9784×100 |
| repo-level-cls-v5 | 132 | 1.35% | 132/9784×100 |

注：JSON 中嵌套的 `raw_metrics` 部分已有正确百分比值，无需修改。仅修正了顶层 parsed 字段。

### 修改文件清单
1. `experiment_plan.yaml` — 新增 3 个 registry_id
2. `artifacts/all_experiments_parsed.json` — 修正 3 个 unparseable_pct 值

---
