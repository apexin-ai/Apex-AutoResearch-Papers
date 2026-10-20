# greedy_f1 差异审计报告

## 1. 差异描述

| 来源 | seed 456 greedy_f1 | 数据源 |
|------|-------------------|--------|
| Registry `exp_001_n16_seed456` | **0.6617** | `output/exp001_n16_seed456/report.json` |
| 分析文件 `analysis_scierc_n16_3seed_selection_f1.json` | **0.6182** | `output/exp_001_seed456_v2/samples.jsonl` |
| **Δ** | **4.35pp** | |

## 2. 根因：Micro vs Macro F1 聚合方式

### 2.1 Registry / report.json 的计算方式

`evaluation.py → generate_evaluation_report()` 调用 `compute_ner_f1()`：

```python
# 全局累加 TP/FP/FN，然后计算 → micro-averaged F1
total_tp = total_fp = total_fn = 0
for pred, gold in zip(predictions, golds):
    tp, fp, fn = entity_strict_match(pred["entities"], gold["entities"])
    total_tp += tp; total_fp += fp; total_fn += fn
return _prf(total_tp, total_fp, total_fn)  # → 0.6617
```

### 2.2 分析脚本的计算方式

`analysis_scierc_n16_selection.py → analyze_single_seed()`：

```python
# 逐实例计算 F1，然后取均值 → macro-averaged F1 (mean per-instance)
for inst in data:
    greedy_f1 = per_instance_f1(greedy, gold, "ner")
    greedy_f1s.append(greedy_f1)
result["greedy_f1"] = np.mean(greedy_f1s)  # → 0.6182
```

### 2.3 为什么 micro > macro？

Micro F1 按**实体**加权（含更多实体的句子贡献更多 TP），macro F1 按**实例**等权平均。两个因素使 macro 被压低：

1. **空 gold 实例**：22 个 `gold_entities = []` 的实例，不论模型输出什么，`per_instance_f1 = 0`。在 micro 计算中这些实例仅贡献少量 FP，对全局 F1 影响极小。
2. **少实体实例的高方差**：只有 1-2 个 gold entity 的实例，F1 要么 1.0 要么 0.0，大量 0.0 拉低 macro 均值。

### 2.4 三个 seed 的对比验证

| Seed | 数据目录 | 推理模式 | Micro F1 (report.json) | Macro F1 (分析脚本) | Δ |
|------|---------|---------|----------------------|-------------------|-----|
| 42 | exp_001_seed42_v2 | **ner** | 0.6621 | 0.6185 | 4.36pp |
| 123 | exp_001_seed123_v2 | **ner** | 0.6621 | 0.6185 | 4.36pp |
| 456 | exp_001_seed456_v2 | **joint** | 0.6633 | 0.6182 | 4.51pp |

micro-macro gap 在三个 seed 上高度一致（~4.4pp），确认这是系统性的聚合方式差异，而非数据错误。

注意：seed 42/123 的 macro F1 完全相同（0.61846...），因为 greedy decode（T=0）不依赖 seed，三个 seed 使用同一模型、同一数据，greedy 输出完全一致。seed 456 的微小差异（0.6182 vs 0.6185）是因为其推理模式为 joint（影响模型生成行为），而非 ner-only。

## 3. 附加发现：数据源不一致

Registry `exp_001_n16_seed456` 的数据来自 `output/exp001_n16_seed456/`（joint 模式，一次单独的推理运行），而分析脚本读取 `output/exp_001_seed456_v2/`（也是 joint 模式，但不同的推理运行）。这导致 micro F1 也略有不同（0.6617 vs 0.6633），但不是主要问题。

更关键的不一致：
- seed 42/123 v2 目录使用 `--subtask ner`（NER-only 推理）
- seed 456 v2 目录使用 `--subtask joint`（NER+RE 联合推理）

分析脚本将三者统一按 NER-only 方式评估（`subtask="ner"`），所以结果可比，但推理模式不一致可能造成微小的 greedy 输出差异。

## 4. 对 ρ 的影响

**Micro vs macro 对 ρ 无影响。**

ρ (Spearman correlation) 始终基于 **per-instance 值**计算：

```python
rho = spearman(signal_scores, per_instance_f1_values)
```

micro/macro 区别仅影响 per-instance F1 的**聚合方式**，不影响 per-instance F1 值本身。因此：
- 同一数据上的 ρ 完全相同，不论报告 micro 还是 macro F1
- 不同文档中的 ρ 差异来自**不同推理运行**（不同 seed → 不同 samples → 不同 signal scores），与 F1 聚合方式无关

### Registry vs report.json ρ 差异

| 来源 | SJ ρ (NER, full) | FK ρ (NER, full) |
|------|-----------------|-----------------|
| exp001_n16_seed456 report.json | 0.4098 | 0.2723 |
| exp_001_seed456_v2 report.json | 0.4171 | 0.2766 (estimated) |
| Registry exp_001_n16_seed456 | 0.4134 | 0.3448 |

Registry 的 ρ 值与两份 report.json 均不完全匹配，说明 registry metrics 可能由第三个评估脚本（如 `exp001_postprocess.py` 或 `eval_n16_5signal.py`）单独计算，使用了不同的 signal 实现（例如含 5 个信号的版本，包括 VC/EM/LP，而早期 report.json 只有 SJ/FK）。

## 5. 哪个 F1 应进论文

### 建议方案

| 论文场景 | 应使用的 F1 | 理由 |
|---------|------------|------|
| Table 1: 模型整体质量 | **Micro F1** (~0.66) | NER 领域标准，与 prior work 可比 |
| Selection 实验（信号选择 vs greedy 的 Δ） | **Macro F1** (~0.62) | 选择在实例级操作，macro 是自然的评估方式 |
| ρ / AUROC 相关性分析 | Per-instance F1 | 不涉及聚合，不受 micro/macro 影响 |

**关键原则**：同一表格内所有数值必须使用同一聚合方式。当前分析文件的 selection F1 使用 macro（正确），但如果论文中 greedy baseline F1 引用 registry 的 micro 值，会产生虚假的 4pp 改进或退化。

### 推荐统一方案

1. Selection 相关表格全部使用 **macro F1**（分析脚本已正确实现）
2. 论文正文提及模型整体性能时使用 **micro F1**，并注明 "micro-averaged"
3. 在论文的 metrics 定义段落明确说明：*"For selection experiments, we report instance-averaged (macro) F1 to match the per-instance selection mechanism."*

## 6. 需要的修复

1. **Registry 标注**：在 registry 的 `exp_001_n16_seed456` 中添加注释 `f1_type: micro`，避免后续混淆
2. **Seed 456 推理模式对齐**：`exp_001_seed456_v2` 使用 joint 模式，而 seed 42/123 使用 ner 模式。建议用统一模式重新生成 seed 456 数据，或在论文中注明此不一致（实际影响 <0.3pp）
3. **分析脚本添加 micro F1**：在 `analysis_scierc_n16_selection.py` 中同时计算并输出 micro F1，方便论文引用
