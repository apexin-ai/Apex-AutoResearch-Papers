# ssh exp004 result check

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp004-result-check_20260515T070804_result.json`
- **Structured JSON:** [`51991d162da4522defbd.json`](../../sessions/51/51991d162da4522defbd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp004_exp2.log 文件在增长（从 69 行到 93 行），re-run **仍在运行**，正在处理 count_12_random_7。而且 `eval_exp2.json` 的开头是 `count_6_low_bcs`，说明原始 MAVEN exp2 结果已保存在 artifacts 根目录（不带 "maven" 前缀）。

---

## exp-004 MAVEN BCS Study 结果报告

### 1. 退出原因

**PID 224685 的原始进程（logs/exp1.log + logs/exp2.log）：正常完成。**
- exp1（count curve）在 07:01 完成，耗时 12475.5s
- exp2（BCS controlled）在 10:21 完成，耗时 11732.5s
- 无 Error/Traceback/OOM

**artifacts/exp004_exp2.log 中的 re-run（500 samples/batch）：仍在运行中**，已完成 8 个 batch（count_12 系列），正在处理 count_12_random_7。

### 2. 结果文件清单

| 文件 | 大小 | 说明 |
|------|------|------|
| `exp004/eval_maven_exp1.json` | 53KB | MAVEN exp1 评估结果 |
| `exp004/predictions_maven_exp1.json` | 45MB | MAVEN exp1 预测 |
| `exp004/batch_config_maven_exp1.json` | 55KB | MAVEN exp1 批次配置 |
| `artifacts/eval_exp2.json` | 18KB | MAVEN exp2 评估结果（原始 run，无 maven 前缀） |
| `artifacts/predictions_exp2.json` | 31MB | MAVEN exp2 预测（原始 run） |
| `artifacts/batch_config_exp2.json` | 19KB | MAVEN exp2 批次配置（原始 run） |
| `exp004/batch_config_maven_exp2.json` | 28KB | MAVEN exp2 re-run 配置 |

### 3. 关键指标摘要

**exp1 (Count Curve)** — 500 samples/batch:

| Types | n_batch | avg exact_F1 | avg relaxed_F1 | avg BCS |
|-------|---------|-------------|----------------|---------|
| 1 | 64 | ~0.009 | ~0.106 | 0.000 |
| 2 | 5 | ~0.009 | ~0.067 | ~0.702 |
| 6 | 5 | ~0.003 | ~0.103 | ~0.892 |
| 12 | 5 | ~0.008 | ~0.146 | ~0.921 |
| 22 | 5 | ~0.013 | ~0.185 | ~0.933 |
| 44 | 5 | ~0.018 | ~0.247 | ~0.967 |
| 64 | 5 | ~0.013 | ~0.245 | ~0.973 |

**exp2 (BCS Controlled)** — 1000 samples/batch, 关键对比:

| Batch | exact_F1 | relaxed_F1 | BCS |
|-------|----------|------------|-----|
| count_6_high_bcs | **0.0354** | **0.2110** | 0.9447 |
| count_6_low_bcs | 0.0068 | 0.0890 | 0.8709 |
| count_12_high_bcs | **0.0151** | **0.1568** | 0.9447 |
| count_12_low_bcs | 0.0068 | 0.1050 | 0.9148 |
| count_6_random (×25) | ~0.007 | ~0.107 | ~0.893 |
| count_12_random (×25) | ~0.009 | ~0.140 | ~0.930 |

### 4. 结论: **SUCCESS (partial re-run in progress)**

原始实验（PID 224685）exp1 和 exp2 均正常完成。**BCS 效应明确**：
- count_6: high_bcs 的 relaxed_F1 是 low_bcs 的 **2.4×**（0.211 vs 0.089）
- count_12: high_bcs 的 relaxed_F1 是 low_bcs 的 **1.5×**（0.157 vs 0.105）

exp004 子目录的 re-run（500 samples/batch 版本）正在运行中，预计还需要一段时间完成剩余 ~46 个 batch。注意原始 MAVEN exp2 的 eval 文件保存为 `artifacts/eval_exp2.json`（无 "maven" 前缀），可能和 Few-NERD exp2 混淆——建议确认该文件内容确实是 MAVEN 数据。

---
