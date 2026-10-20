# code swebench full run

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_swebench-full-run_20260512T040331_result.json`
- **Structured JSON:** [`58c25e32a50321556211.json`](../../sessions/58/58c25e32a50321556211.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务结果汇报：

---

## 1. SWE-bench 全量构建 — 已成功启动

| 项目 | 值 |
|------|------|
| PID | 2312582 |
| 日志 | `/tmp/swebench_full.log` |
| 状态 | RUNNING — 评估阶段进行中 |
| 实例数 | 250 选中，10 已有（pilot），正在跑 240 个 |
| 进度 | `0/240` (刚启动) |

大量 "WARNING: No Docker image found" 是正常的——只有 pilot 阶段的 9 个镜像已预拉取，其余会按需拉取。预计 12-24h 完成。

---

## 2. mvp-b-train 原始评估结果（eval_results.json）

| 指标 | 值 |
|------|------|
| test_set_size | 1890 |
| overall_accuracy | **87.51%** |
| majority_baseline | 51.75% |
| gap vs baseline | +35.77pp |

**Per-class:**

| Class | Precision | Recall | F1 | Support |
|-------|-----------|--------|----|---------|
| Pass | 93.24 | 81.80 | 87.15 | 978 |
| Fail | 82.75 | 93.64 | 87.86 | 912 |

**Confusion matrix:** TN=854, FP=58, FN=178, TP=800, unparseable=0

---
