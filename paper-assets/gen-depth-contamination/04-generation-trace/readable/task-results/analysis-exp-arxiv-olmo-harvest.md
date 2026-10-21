# analysis exp arXiv olmo harvest

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_arXiv_olmo_harvest_20260517T120756_result.json`
- **Structured JSON:** [`fc741176a5ae3a4029b0.json`](../../sessions/fc/fc741176a5ae3a4029b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验成功完成。

## 结果汇报

**状态**: SUCCESS (EXIT_CODE=0)

### Pairwise AUC (adjacent depths)

| Depth Pair | AUC | 判定 |
|---|---|---|
| 0 vs 1 | **0.9958** | ≫ 0.6 ✓ distinguishable |
| 1 vs 2 | 0.5034 | < 0.6 ✗ chance |
| 2 vs 3 | 0.5069 | < 0.6 ✗ chance |
| 3 vs 4 | 0.5021 | < 0.6 ✗ chance |
| 4 vs 5 | 0.5037 | < 0.6 ✗ chance |

### K* = 1

第一个 AUC 低于 theta=0.6 的 depth pair 是 1v2，所以 K\* = 1。

### 与前序实验对比

| 实验 | 模型 | 域 | K* |
|---|---|---|---|
| exp-024 | Qwen-2.5-1.5B | arXiv | 3 |
| exp-025 | Pythia-1.4B | arXiv | 3 |
| **exp_arXiv_olmo** | **OLMo-1B** | **arXiv** | **1** |

**OLMo-1B 结果异常**：K\*=1 远低于预期的 3。0v1 的 AUC 极高 (0.9958)，但从 depth 1 开始所有 pair 都降到 chance level (~0.50)。这意味着 OLMo 只能区分"原始 vs 一次改写"，之后所有改写深度的特征完全不可分。

可能原因：
- OLMo-1B 的 tokenizer/perplexity 信号在改写文本上迅速饱和
- 模型对改写风格的敏感度远低于 Qwen 和 Pythia

### 文件路径
- **结果目录**: `/root/autodl-tmp/gen-depth-contamination/results/exp_arXiv_olmo/`
- **日志**: `/root/runs/gen-depth-contamination/exp_arXiv_olmo.log`
- **数据**: `/root/autodl-tmp/gen-depth-contamination/data/exp_arXiv_olmo/` (6 depths × 2200 samples)

### 补充指标
- JSD: 0v1 = 0.329 (高), 1v2 ~ 4v5 ≈ 0.007 (接近零)
- Ordinal 6-class accuracy: 33% (MAE=1.35)，基本是 random

---
