# analysis w4 item id pct inconsistency

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_w4_item_id_pct_inconsistency_20260521T204018_result.json`
- **Structured JSON:** [`8958d344955039273c40.json`](../../sessions/89/8958d344955039273c40.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All three numbers are now fully traced. The registry's 74.48% is the mean η² across samples: (75.88 + 75.38 + 72.18) / 3 = 74.48% exactly.

---

## 调查结论

三个数字的差异来自**两个维度**的变化：**估计方法**（η² vs Henderson I）和**分析设计**（6-facet vs 5-facet）。

### 溯源表

| 报告值 | 实际值 | 方法 | Facets | 数据范围 | 来源文件 |
|--------|--------|------|--------|---------|---------|
| **61.1%** | 61.08% | SS proportion (η²) = SS(item)/SS(total) | 6 (含 precision) | 全精度, 239,200 records | 旧版 gstudy_full.py 输出（已被覆盖）|
| **54.85%** | 54.85% | Henderson I 方差分量估计 | 6 (含 precision) | 同上数据 | 当前 `llama_single_model_gstudy.json` |
| **74.48%** | 74.48% | SS proportion (η²) 三样本均值 | 5 (无 precision) | bf16-only, 3×86,400 | registry.yaml（旧值）|
| *(71.59%)* | 71.59% | Henderson I 三样本均值 | 5 (无 precision) | 同上 | 当前 `exp001b_resampling_gstudy.json` |

### 关键发现

1. **61.1% 不是 bug**。我在服务器上重新计算确认：当前 `llama_full.csv` 的 η²(item_id) = 61.08%，与论文报告的 61.1% 完全一致。

2. **54.85% 也不是 bug**。是同一数据用 Henderson I（ANOVA EMS 法）估计的方差分量百分比。Henderson I 从 MS(item) 中扣除了 item 交互项的贡献，所以比 η² 低 ~6pp。

3. **74.48% vs 71.59%**：同样是 η² vs Henderson I 的差异。我验证了 3 个 resampling 样本的 η²: 75.88%, 75.38%, 72.18%，均值恰好 = 74.48%。

4. **G = 0.9184 是 Henderson I G 系数**（正确）。旧的 G = 0.6108 就是 η² 本身，被错标为 G 系数（registry 注释记录的 bug）。

### §4.1 应该用哪个？

**用 Henderson I (54.85%)，配合 G = 0.9184**。理由：

- 论文的核心贡献是将 G-theory 引入 NLP — 必须使用 G-theory 标准方法（Henderson I 方差分量估计）
- G = 0.9184 本身就是 Henderson I 计算的。如果百分比报 η²(61.1%) 而 G 报 Henderson I(0.9184)，方法论上不自洽：读者无法从报告的百分比复现出报告的 G 值
- exp001b 的数值也应统一为 Henderson I: mean = 71.6%

### 需要更新的位置

论文中所有引用 61.1% 的位置都需要改为 54.85%，包括：
- §4.1 single-model variance decomposition
- single-model vs cross-model 对比（61.1% → 42.1% 需更新为 54.85% → 对应的 cross-model Henderson I 值）
- null simulation 对比（"0.08% vs 61.1%" 需更新）
- exp001b 引用（74.48% → 71.6%）

### 建议标注方式

论文中应明确标注：

> Variance components are estimated using Henderson Type I (ANOVA expected mean squares) method. Percentages represent each component's proportion of total estimated variance (σ̂²), not sum-of-squares proportions (η²).

这样读者不会与 η² 混淆。

---
