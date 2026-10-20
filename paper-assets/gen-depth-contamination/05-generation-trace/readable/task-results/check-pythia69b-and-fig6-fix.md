# check pythia69b and fig6 fix

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_pythia69b_and_fig6_fix_20260521T170803_result.json`
- **Structured JSON:** [`11e152c95076046e2b86.json`](../../sessions/11/11e152c95076046e2b86.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### Part A: Pythia-6.9B nucleus 状态

| 项目 | 状态 |
|------|------|
| PID 443243 | **存活**，已运行 2h 28m |
| GPU 0 | 94% 利用率, 14.5/24.5 GB |
| 数据进度 | depth_0 + depth_1 完成（共需 depth 0-4，当前生成 depth 2） |
| Feature extraction | 未开始（features.csv 不存在） |
| Results | 空 |
| 预计 | 约 40% 生成完成，整个 pipeline（生成+特征+分类）预计还需 3-4 小时 |

### Part B: Figure 6 重绘完成

**数据源修正：**

| 模型 | 数据来源 | 1v2 AUC | CI 来源 |
|------|---------|---------|---------|
| Qwen-1.5B-RW | `exp_qwen_retrain_chain/bootstrap_ci.json` | 0.9611 | 10k bootstrap |
| **Pythia-1.4B** | **`exp_14b_c4/bootstrap_ci_results.json`** | **0.6210** | **10k bootstrap** |
| OLMo-1B | `exp_olmo1b_c4_rerun/pairwise_auc.json` | 0.5080 | 5-fold SE |
| Qwen-1.5B-cont | `results_exp022_cross_scorer/qwen_cont256__qwen_base/pairwise_auc.json` | 0.6282 | 5-fold SE |

Pythia-1.4B 1v2 AUC 从 0.879 (greedy) 修正为 0.621 (nucleus)。

**注意**：Pythia 的 0.621 与你提到的主表值 0.6539 有差异（~0.03），`exp_14b_c4` 是唯一可用的 Pythia nucleus bootstrap CI 数据。新的 nucleus 重跑（PID 443243 是 6.9B；`data/exp_pythia14b_c4_nuc/` 只有 depth_0，看起来是个未完成的 1.4B nucleus 重跑）完成后可以重新计算。

输出：`docs/paper/figures/fig_s1_auc_decay_ci.{pdf,png}`

---
