# analysis d102 prep for t15 s43

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d102_prep_for_t15_s43_20260523T021140_result.json`
- **Structured JSON:** [`73477d1bb3d9b87b0057.json`](../../sessions/73/73477d1bb3d9b87b0057.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## D102 分析环境就绪性报告

### westd-17855

| 检查项 | 状态 | 详情 |
|--------|------|------|
| `run_5method_analysis_d102.py` | ✅ | 458 行，与 19828 一致 |
| `permutation_granger.py` | ✅ | 355 行，与 19828 一致 |
| D105 3sigma 阈值文件 | ✅ | `results/analysis/3sigma_recompute_d105_17855.json`（含 per_pair 数据） |
| scipy | ✅ | 1.17.1 |
| statsmodels | ✅ | 0.14.6 |
| mauve-text | ✅ | 已安装（conda base） |
| 磁盘空间 | ⚠️ | **21G 可用 / 350G（95% 已用）** — 分析脚本本身不需要大量磁盘，但非常紧张 |
| T=15 实验目录 | ✅ | `t15_a045_s42_fp32_14b`, `t15_a050_s42_fp32_14b`, `t15_a060_s42_fp32_14b` 已存在 |
| T=10 s43 实验目录 | ✅ | `14b_t10_a060_s43_fp32`, `14b_t10_a075_s43_fp32`, `t10_a045_s43_fp32_14b` 已存在 |

### westd-19828

| 检查项 | 状态 | 详情 |
|--------|------|------|
| `run_5method_analysis_d102.py` | ✅ | 458 行，与 17855 一致 |
| `permutation_granger.py` | ✅ | 355 行，与 17855 一致 |
| D105 3sigma 阈值文件 | ✅ | `results/analysis/3sigma_recompute_d105.json`（多实验覆盖） |
| scipy | ✅ | 1.17.1 |
| statsmodels | ✅ | 0.14.6 |
| mauve-text | ✅ | 已安装（conda base） |
| 磁盘空间 | ✅ | **105G 可用 / 250G（59% 已用）** |
| T=10 s43 实验目录 | ✅ | `14b_t10_a050_s43_fp32` 已存在 |
| 额外分析脚本 | ✅ | `d102_rerun_8pair.py` 也在此服务器 |

### 总结

两台服务器 D102 分析环境**均已就绪**，脚本版本一致（458 行），Python 依赖齐全。

唯一关注点：**westd-17855 磁盘仅剩 21G（95%）**。D102 分析输出 JSON 较小（几百 KB），不会有问题。但如果有新实验要跑在 17855 上，需要先清理空间。

---
