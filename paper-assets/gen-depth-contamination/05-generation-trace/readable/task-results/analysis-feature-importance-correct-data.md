# analysis feature importance correct data

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_feature_importance_correct_data_20260521T195442_result.json`
- **Structured JSON:** [`3ad0103497942be39ab0.json`](../../sessions/3a/3ad0103497942be39ab0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

**1v2 Feature Importance（修正数据）**

| | OLMo-1B (K\*=1) | Pythia-1.4B (K\*=2) | Qwen-cont (K\*=2) |
|---|---|---|---|
| 1v2 raw AUC | 0.508 | 0.678 | 0.617 |
| #1 feature | Δ¹Surp σ +0.007 | **Surprisal σ +0.102** | **Surprisal σ +0.065** |
| #2 feature | Δ¹Surp Skew +0.005 | **Freq Entropy +0.043** | **Freq Entropy +0.037** |

**核心结论不变**：Surprisal σ 和 Freq Entropy 在 K\*≥2 模型中稳定占据 top-2；OLMo (K\*=1) 所有 feature ΔAUC < 0.007，无显著贡献。Pythia/Qwen-cont top-4 排序完全一致（Surp σ → Freq Entropy → Surp μ → Hapax Ratio）。

**数据源变更**：OLMo 从 cross-scored (`olmo_c4_qwen_scorer`) 改为 self-scored rerun；Pythia 从 cross-scored 改为 nucleus p=0.9 self-scored。exp_017 Qwen-cont self-scored 数据不在磁盘上，沿用 `qwen_cont256__qwen_base`（AUC 0.617 ≈ target 0.611）。

产出：
- 服务器 JSON: `results/feature_importance_correct/`
- 本地报告: `artifacts/feature_importance_correct_data.md`

---
