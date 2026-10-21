# analysis bootstrap reconcile

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bootstrap_reconcile_20260515T152233_result.json`
- **Structured JSON:** [`bbb2fc7fbeaa1b9d6830.json`](../../sessions/bb/bbb2fc7fbeaa1b9d6830.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是完整分析结果。

---

## 不一致 1: Few-NERD pairwise Pearson r — 0.112 vs 0.156

### 原因：prediction 数据被覆盖

Registry 的 r=0.156 是在 **exp002（V1 prompt）** 期间计算的。之后 **exp003a（V2 prompt rerun）** 重跑了 `run_experiment.py --mode exp2 --prompt_version v2`，覆盖了 `artifacts/predictions_exp2.json`。

`pairwise_confusion_analysis.py` 和 `bootstrap_ci.py` 都从同一文件读取：
```python
PREDICTIONS_PATH = "/root/schema-dag-extraction/artifacts/predictions_exp2.json"
```

二者在当前数据上得到一致的 r=0.112（`pairwise_confusion_correlation.json` 验证了这一点）。

Registry 自己也已注意到这个问题（`bootstrap_ci_analysis.metrics.fewnerd_pairwise_r.note`）：
> "point estimate 0.112 vs old 0.156 — re-run confirmed current value"

V2 prompt 大幅减少了 over-prediction（pred/gold ratio 从 ~3.5x 降到 ~1.1x），减少了 spurious confusion 事件，降低了 BCS-confusion 相关性。

### 建议

**论文使用 r=0.112，95% CI [0.076, 0.156]。**

理由：V2 prompt 减少了 over-prediction 噪声，r=0.112 是更干净的估计。V1 的 r=0.156 被大量 spurious FP 人为抬高。CI 上界恰好 ≈ 0.156，说明两个值在统计上一致。

---

## 不一致 2: confusion ratio count_12 — 21.2x vs 9.9x

### 原因：三重不一致

通过交叉验证 V1 reeval 数据（`exp2_reeval_results_v1.json`），确认 registry 的 9.9x 来源：

| 维度 | Registry (9.9x) | Bootstrap (21.2x) |
|------|-----------------|-------------------|
| **数据** | V1 reeval（V1 prompt） | V2 reeval（V2 prompt, CLEAN） |
| **分子** | wrong_type count 直接相除 | wrong_type / total_gold 的比值 |
| **分母** | 无（count ratio）| total_gold |
| **rates 分母** | wrong_type / total_fp | wrong_type / total_gold |

**验证 registry 9.9x 的来源：**

V1 数据 count_12 extreme batches：
- high_bcs: wrong_type=**79**, total_gold=568, total_fp=1647
- low_bcs: wrong_type=**8**, total_gold=287, total_fp=1306
- Registry ratio = **79/8 = 9.875 ≈ 9.9**（raw count ratio）
- Registry rates: 79/1647=**0.048**, 8/1306=**0.0061**（wrong_type/total_fp）

V2 数据 count_12 extreme batches（bootstrap 使用）：
- high_bcs: wrong_type=42, total_gold=568
- low_bcs: wrong_type=1, total_gold=287
- Bootstrap ratio = (42/568)/(1/287) = 0.0739/0.00348 = **21.2x**

**Registry 有两个方法论 bug：**
1. Ratio 是 count 之比（79/8），不是 rate 之比——忽略了高、低 BCS batch 的 gold entity 数量不同（568 vs 287）
2. Rates 用 wrong_type/total_fp，但 total_fp 在 V1 远大于 V2（V1 over-prediction 严重），这个分母混淆了 over-prediction 效应和 type confusion 效应

### 建议

**论文使用 21.2x，95% CI [5.3, 52.2]。**

理由：
- Bootstrap 方法正确：rate ratio（wrong_type/total_gold）控制了 batch 大小差异
- V2 数据更干净（over-prediction 已修正）
- CI 下界 5.3x 仍然远 >1，定性结论稳健
- **但务必在论文中承认 CI 极宽**，因为 low-BCS batch 仅有 1 个 wrong_type event。建议描述为："high-BCS batches exhibit >5x higher type confusion rate (point estimate 21.2x, 95% CI [5.3, 52.2])"，强调下界而非点估计

如果 reviewer 质疑 21.2x 的稳定性，可补充 count_6 数据（25.3x [6.1, 60.5]）和 random batch 对比（ratio 2.4x）作为 robustness evidence。

---
