# code stats and figures prep

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_stats-and-figures-prep_20260515T201552_result.json`
- **Structured JSON:** [`5a2f9e927eee18ccf4a5.json`](../../sessions/5a/5a2f9e927eee18ccf4a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个脚本已完成，全部通过 dry-run 并注册到 artifacts。

**产出汇总：**

| 脚本 | 路径 | 功能 |
|------|------|------|
| `fisher_exact_test.py` | `artifacts/analysis/` | Fisher exact test (2×2 pooled) + bootstrap CI (10000 resample, task-level) + per-task 对比表 |
| `magnitude_curve.py` | `artifacts/analysis/` | obs_only vs perdof 的 norm sensitivity curve，log-scale X 轴，argmin/VLA-only baseline 虚线，支持 spatial+object 双子图，输出 PDF+PNG |
| `comparison_table.py` | `artifacts/analysis/` | 6 method × 3 column (seed42/seed43/pooled) LaTeX tabular + per-task breakdown (obs_only vs argmin) |

**数据就绪后使用方式：**
- 填入 placeholder data 直接运行，或传 `--json data.json` 从文件加载
- magnitude_curve 的 spatial 数据已内嵌，直接 `python3 magnitude_curve.py` 即可出图
- object domain 数据到位后填入 `OBJECT_DATA` 字典，自动生成双子图

---
