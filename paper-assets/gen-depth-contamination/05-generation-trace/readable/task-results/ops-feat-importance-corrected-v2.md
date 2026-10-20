# ops feat importance corrected v2

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_feat_importance_corrected_v2_20260521T092834_result.json`
- **Structured JSON:** [`12431824745703913cf5.json`](../../sessions/12/12431824745703913cf5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the data. Here is the final report.

---

## Feature Importance 数据源审计 + 重跑结果

### 1. LLaMA-3.1-8B — ✅ 已有正确结果（无需重跑）

- **数据源**: `data/exp_018_llama8b/features.csv`
- **AUC 验证**: 1v2 baseline_auc = **0.6104** (target 0.6123, Δ=0.0019 ✅)
- **结果位置**: `results/feature_importance/importance_results.json`

**1v2 Feature Importance Top-5** (baseline AUC = 0.6104):

| Rank | Feature | Mean Importance | Std |
|------|---------|----------------|-----|
| 1 | surp_std | 0.0583 | 0.0064 |
| 2 | surp_d2_std | 0.0218 | 0.0068 |
| 3 | freq_entropy | 0.0170 | 0.0061 |
| 4 | surp_mean | 0.0133 | 0.0048 |
| 5 | ttr | 0.0060 | 0.0054 |

**2v3 baseline AUC**: 0.5318

---

### 2. Qwen-1.5B (cont) — ✅ 已有正确结果（corrected 版本）

- **数据源**: `data_exp022_cross_scorer/qwen_cont256__qwen_base/features.csv`
- **AUC 验证**: 1v2 baseline_auc = **0.6169** (target 0.6112, Δ=0.0057 ✅)
- **结果位置**: `results/feature_importance_qwen_cont_corrected/importance_results.json`

**1v2 Feature Importance Top-5** (baseline AUC = 0.6169):

| Rank | Feature | Mean Importance | Std |
|------|---------|----------------|-----|
| 1 | surp_std | 0.0653 | 0.0035 |
| 2 | freq_entropy | 0.0369 | 0.0066 |
| 3 | surp_mean | 0.0357 | 0.0051 |
| 4 | hapax_ratio | 0.0267 | 0.0077 |
| 5 | surp_kurt | 0.0134 | 0.0040 |

**2v3 baseline AUC**: 0.5552

---

### 3. OLMo-1B — ❌ 正确数据缺失，无法重跑

- **目标 AUC**: 0.6145
- **现有数据**: `data/olmo_c4_qwen_scorer/features.csv` → AUC = **0.5001** (Δ=0.1144, 远超 ±0.01 容差)
- **原因**: OLMo C4 的 depth chain JSONL 文件是 `data/olmo_c4_cont/` 的符号链接，该目录数据已于 5 月 20 日被重新生成，原始产出 AUC=0.6145 的数据不在磁盘上
- **穷举搜索**: 全服务器 50+ features.csv 均未找到 AUC≈0.6145 的匹配

---

### 4. Pythia-1.4B — ❌ 正确数据缺失，无法重跑

- **目标 AUC**: 0.6539
- **现有数据**: `data/pythia_c4_qwen_scorer/features.csv` → AUC = **0.6064** (Δ=0.0475, 远超 ±0.01 容差)
- **原因**: Pythia C4 的 depth chain 数据是 5 月 21 日新生成的，与产出主表 AUC=0.6539 的原始数据不同。之前的错误 feature importance 使用了 wiki domain 数据 (`data/exp_wiki_pythia/features.csv`)，也不正确
- **穷举搜索**: 全服务器 50+ features.csv 均未找到 AUC≈0.6539 的匹配

---

### 总结

| 模型 | 状态 | 1v2 AUC (实际 / 目标) | Top-1 Feature |
|------|------|----------------------|---------------|
| LLaMA-3.1-8B | ✅ 正确 | 0.6104 / 0.6123 | surp_std (0.0583) |
| Qwen-1.5B (cont) | ✅ 正确 | 0.6169 / 0.6112 | surp_std (0.0653) |
| OLMo-1B | ❌ 缺失 | 0.5001 / 0.6145 | — |
| Pythia-1.4B | ❌ 缺失 | 0.6064 / 0.6539 | — |
| Qwen-1.5B (base) | ✅ 原有正确 | (未检查) | (不在本次任务范围) |

**结论**: OLMo 和 Pythia 需要重新生成 C4 domain + Qwen scorer 的完整 depth chain，才能恢复主表对应的 AUC 并重跑 feature importance。当前磁盘上的 depth chain 数据均为近期重新生成，与原始实验条件不一致。

---
