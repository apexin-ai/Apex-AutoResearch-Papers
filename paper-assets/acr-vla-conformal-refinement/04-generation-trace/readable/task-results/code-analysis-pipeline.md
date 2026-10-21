# code analysis pipeline

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_analysis-pipeline_20260515T132601_result.json`
- **Structured JSON:** [`7803dff7cdf5754c937a.json`](../../sessions/78/7803dff7cdf5754c937a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个脚本全部通过语法验证，已在 `/root/acr-vla-conformal-refinement/scripts/` 创建完成：

| 脚本 | 功能 |
|------|------|
| `analyze_fisher_exact.py` | 合并两个 seed 的成功/失败 counts，Fisher exact test + bootstrap 95% CI |
| `plot_magnitude_curve.py` | obs_only vs perdof 两条线 + argmin baseline，输出学术风格 PDF |
| `summarize_object_table.py` | 10 tasks × N methods LaTeX 表格，bold 最佳，含 avg±std |

`figures/` 目录也已创建。所有依赖（scipy 1.17.1, matplotlib 3.10.5）已就绪。

---
