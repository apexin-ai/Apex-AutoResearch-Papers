# Cross-model CV 方式修复报告

## 问题

审稿指出：cross-model chain binary F1=0.764 使用 sample-level 5-fold StratifiedKFold CV，与主表的 generator-level held-out (LOGO) 设计矛盾。

## 分析

代码确认：`cross_model_chains.py` 的 `phase_evaluate()` 在全局 balance 后做 5-fold StratifiedKFold，样本随机分配到各 fold，同一 generator 的样本可能同时出现在 train/test，确实是 sample-level CV。

## 修复方案

实现 LOGO（leave-one-generator-out）评估。Cross-model chain 数据中每个 depth 1-4 样本有 `generator_at_depth` 标签，记录该样本由哪个 generator 生成：

- **5 个 generator**: olmo-2-1b, pythia-1b, pythia-2.8b, qwen3-0.6b, qwen3-1.7b
- **LOGO 分 fold 方式**: 每 fold 持出一个 generator 的所有 depth 1-4 样本
- **Depth-0 (wikipedia)**: 均分到 5 个 fold（depth-0 是人类文本，不关联特定 generator）
- **每 fold 训练集**: balance 至最小类别数量

脚本: `scripts/cross_model_logo.py`

## 结果

### LOGO 总体

| 指标 | 原 5-fold CV | LOGO | Delta | 95% Bootstrap CI |
|------|-------------|------|-------|-----------------|
| 3-class macro F1 | 0.809 | **0.789** | -0.020 | [0.777, 0.800] |
| Binary F1 (gen-1 vs gen-2+) | 0.764 | **0.830** | +0.066 | [0.818, 0.841] |

### Per-generator LOGO

| Generator | 3-class F1 | Binary F1 | n_test |
|-----------|-----------|-----------|--------|
| olmo-2-1b | 0.768 | 0.810 | 982 |
| pythia-1b | 0.810 | 0.832 | 928 |
| pythia-2.8b | 0.791 | 0.819 | 950 |
| qwen3-0.6b | 0.780 | 0.815 | 968 |
| qwen3-1.7b | 0.795 | 0.871 | 945 |

### Per-class 指标 (LOGO pooled)

| Class | Precision | Recall | F1 |
|-------|-----------|--------|-----|
| gen-0 | 0.881 | 0.953 | 0.916 |
| gen-1 | 0.523 | 0.766 | 0.622 |
| gen-2+ | 0.929 | 0.749 | 0.829 |

### Confusion Matrix (LOGO pooled)

```
           Pred gen-0  Pred gen-1  Pred gen-2+
True gen-0       948         44           3
True gen-1        74        757         157
True gen-2+       54        647        2089
```

## 解读

1. **3-class macro F1 下降 0.02**: 符合预期——LOGO 比 sample-level CV 更严格，训练时完全未见 held-out generator 的样本。gen-1 precision 从 0.716 降至 0.523 是主要来源。

2. **Binary F1 从 0.764 提升至 0.830**: LOGO 迫使分类器学习 generator-invariant 的 depth 特征，反而提升了 gen-1 vs gen-2+ 的区分能力。原 5-fold CV 的 binary F1 较低可能因为全局 balance 后数据量较小（2964 vs 4773）。

3. **所有 5 个 generator 的 binary F1 均 ≥ 0.81**: 跨 generator 泛化稳定，最低 olmo-2-1b (0.810)，最高 qwen3-1.7b (0.871)。

## 论文更新建议

- 将 cross-model chain 结果从 binary F1=0.764 (5-fold CV) 更新为 **binary F1=0.830 [0.818, 0.841]** (LOGO)
- 3-class macro F1 = 0.789 [0.777, 0.800]
- 明确标注使用 LOGO 评估，与主表方法论一致
- 需更新位置: abstract, §5.1 results, conclusion, limitations

## 数据文件

- 结果 JSON: `results/cross_model_logo_results.json` (服务器)
- 脚本: `scripts/cross_model_logo.py` (服务器)
