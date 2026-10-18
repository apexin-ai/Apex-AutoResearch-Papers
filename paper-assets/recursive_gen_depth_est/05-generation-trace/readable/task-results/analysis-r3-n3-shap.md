# analysis r3 n3 shap

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r3-n3-shap_20260515T191512_result.json`
- **Structured JSON:** [`7236795158bcdc089819.json`](../../sessions/72/7236795158bcdc089819.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

SHAP 分析已完成，结果已注册为 artifact (`art_20260515_1ec027`)。

## 核心发现

**SHAP vs Permutation Importance 高度一致**: mean Spearman ρ = 0.830 (0.749–0.916), all p < 0.001

**Top-2 特征在 9/9 cells 完全稳定**:
- **p90_ppl** (mean |SHAP| = 0.0894) — 全部 9 cell 进入 top-4
- **var_surprisal** (mean |SHAP| = 0.0803) — 全部 9 cell 进入 top-4
- PPL/surprisal 类特征占总 importance 的 **88.8%**

**SHAP Top-5 与 Gini Top-5 完全相同**（仅排序微调）: p90_ppl, var_surprisal, p75_ppl, mean_surprisal, mean_ppl → importance 排名对方法选择不敏感

## 论文修改建议
1. **删除** §5.4 attention-importance 相关分析 (ρ=-0.484)
2. **替换为** SHAP TreeExplainer 结果 — 理论保证的 Shapley values, mean ρ=0.830 验证 importance 鲁棒性
3. **保留** 线性探测负 R² 作为独立互补证据
4. 新叙事：RF 依赖 perplexity tail statistics → PLM fine-tuning 无法捕获 → hand-crafted 特征工程的必要性得到双重验证（SHAP + 线性探测）

---
