# analysis r11 q5 freq dispersion

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r11-q5-freq-dispersion_20260517T100043_result.json`
- **Structured JSON:** [`b25a86f17f1c7178686b.json`](../../sessions/b2/b25a86f17f1c7178686b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果汇总：

---

## 结果

**FewRel type frequency: 完全 balanced（700 instances/type, SD=0）**
→ Type frequency dispersion 对所有 batch 恒为 0，不是有效 predictor。
→ 改用 **type difficulty dispersion**（per-type accuracy 的 std）。

### 主要结果（fewrel_16rel_bootstrap, n=100 batches, 8 types from 16-rel pool）

| Model | R² | Key coeff (p) |
|-------|------|------|
| accuracy ~ BCS | 0.406 | -0.449 (p=1.0e-12) |
| accuracy ~ mean_type_difficulty | 0.445 | 1.072 (p=3.5e-14) |
| accuracy ~ BCS + mean_diff | **0.704** | BCS: -0.367 (p=6.8e-15), mean: 0.897 (p=2.4e-16) |

### Variance Decomposition (BCS + mean_type_difficulty)

| Component | R² | % of explained |
|-----------|-----|------|
| Unique to BCS | 0.259 | 36.8% |
| Unique to composition | 0.298 | 42.3% |
| Shared (BCS ∩ composition) | 0.147 | 20.9% |
| **Total** | **0.704** | 100% |

- **Partial R² of BCS** (controlling composition): **0.467**
- r(BCS, mean_type_difficulty) = -0.21, VIF = 1.06

### Robustness (independent difficulty estimates from separate experiment)

With difficulty estimated from a different 10-type-batch experiment:
- BCS unique: **0.326 (75.9%)**
- Composition unique: 0.023 (5.4%)
- Shared: 0.080 (18.7%)

### Pair vs Batch R²

| Level | R² | n |
|-------|------|------|
| Batch | 0.406 | 100 |
| Pair | 0.0072 | 49,600 |
| Ratio | 56.4x | — |

### 回答审稿人

1. FewRel 完全 balanced → type frequency dispersion 恒为零，**无法解释任何 batch R² variance**。
2. 用 type difficulty（composition effect）作为替代 confound：BCS 的 63.7% R² 是 unique 的（独立估计时升至 75.9%），composition 贡献了 shared 的 20.9%（独立估计时仅 18.7%）。
3. BCS 在控制 composition 后 partial R²=0.467，仍高度显著（p=6.8e-15）。
4. Batch/pair R² gap（56.4x）来自 aggregation（within-batch noise averaging），不是 composition artifact。

---
