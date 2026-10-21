# code plan 002 eval

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan-002-eval_20260514T233401_result.json`
- **Structured JSON:** [`aeb24ae52bc59fa68848.json`](../../sessions/ae/aeb24ae52bc59fa68848.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果摘要：

### 1. Leave-One-Generator-Out CV
平均 macro-F1 = **0.8037**。gen-0 分类最容易（F1 > 0.91），gen-1 最难（F1 0.58–0.71）。Pythia-1b 泛化最好（0.8507），OLMo-2-1b 最差（0.7519）。

### 2. Leave-One-Family-Out
两个方向差异极小（Δ = +0.0107），说明深度指纹在 Pythia 和非 Pythia 家族间高度可迁移。

### 3. Feature Ablation
| Feature Set | Avg Macro-F1 |
|---|---|
| full (7 features) | 0.8037 |
| reference_only (5) | 0.7543 |
| surface_only (2) | 0.7471 |

两组子集都显著弱于 full（McNemar p ≈ 0），表面特征和参考特征互补。

### 4. Permutation Importance
Top 3: **hapax_ratio** (0.289) > **ttr** (0.168) > **entropy_mean** (0.160)。tail_decay 贡献最小。

### 5. entropy_std 结论
去掉 entropy_std 后 macro-F1 仅下降 0.0049，drift 幅度（0.12）远小于 entropy_mean（1.50）。**entropy_std 更可能是 H1（模型特有 artifact），而非通用深度信号。**

产出文件已保存在服务器 `data/cross_generator_results.json` 和 `data/cross_generator_report.md`。

---
