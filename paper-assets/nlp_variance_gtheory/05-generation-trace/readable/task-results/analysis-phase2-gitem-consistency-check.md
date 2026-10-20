# analysis phase2 gitem consistency check

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_phase2_gitem_consistency_check_20260521T230320_result.json`
- **Structured JSON:** [`fc96cee611cbf8c0c375.json`](../../sessions/fc/fc96cee611cbf8c0c375.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**根本原因：`exp004_ff_gstudy.py` 中的 bug**

`compute_g_item` 函数（约第120行）将 residual 除以 `1` 而非 `prod(non_item_facet_levels) = 2304`，导致 σ²(δ) 被膨胀约 2300 倍。

### Step 1: Facet 结构对比

| | 4-model 脚本 | 8-model FF 脚本 |
|---|---|---|
| Facets | model/temp/prompt/seed/ordering/item_id | 相同 |
| Henderson I | 相同实现 | 相同实现 |
| **residual in G_item** | **`÷ prod(non_item) = 1152`** | **`÷ 1` ← BUG** |

### Step 2: Bug 确认

| | G_item |
|---|---|
| 8-model buggy (÷1) | **0.2837** ← 匹配报告值 |
| 8-model correct (÷2304) | **0.8629** |
| 4-model subset (correct) | **0.7289** ← 精确匹配原值 |

### Step 3: 逐步加模型（correct 公式）

| Models | G_item | Δ |
|---|---|---|
| 4 (base) | 0.7289 | — |
| 5 (+InternLM) | 0.7916 | +0.063 |
| 6 (+DeepSeek) | 0.8111 | +0.020 |
| 7 (+OLMo) | 0.8412 | +0.030 |
| 8 (+Yi) | 0.8629 | +0.022 |

G_item **单调递增**，与报告的骤降完全相反。MMLU 同样趋势（0.816→0.896）。

### Step 4: Pairwise 相关

- 原4模型平均 r = 0.518
- 新4模型平均 r = 0.558
- 跨组平均 r = 0.564
- Qwen3-8B 与 DeepSeek 相关最低（r=0.196）

### 需要修复

`scripts/exp004_ff_gstudy.py` 第 ~120 行和 ~145 行，`compute_g_item` 和 `d_study_curve` 中：
```python
# 错误：
if key == "residual":
    divisor = 1
# 应改为：
if key == "residual":
    non_item = [f for f in FACETS if f != "item_id"]
    divisor = prod(n_levels[f] for f in non_item)
```

JSON 已保存到 `results/exp004_8model_analysis/gitem_consistency_check.json`。

---
