# P0-1 SciERC AUROC 计算管道差异追溯报告

## 1. 两套 AUROC 值的具体计算代码路径

### Paper Table 1（正确值）
- **脚本**: `code/analyze_exp015_unified.py`
- **数据**: `output/exp_012_logprob/samples_with_logprobs.jsonl` (551 instances, 529 NER valid)
- **AUROC 函数**: `auroc_simple()` (line 36) + `compute_metrics()` (line 113)
- **Binarization**: `labels = (y >= median_f1).astype(int)` (line 124) — **F1 ≥ median**
- **Median F1**: 0.6667 (= 2/3)
- **正/负类划分**: 301 positive / 228 negative

### Registry (`all_signals_5signal.json`)
- **脚本**: `code/analyze_exp012_rerun_5signal.py`
- **数据**: `output/exp_012_rerun_1024/samples.jsonl` (551 instances, 529 NER valid)
- **AUROC 函数**: `safe_auroc()` (line 78) — Mann-Whitney U via `scipy.stats.rankdata`
- **Binarization**: `binary_correct = (f1_arr >= 1.0).astype(int)` (line 186) — **F1 = 1.0 (perfect extraction)**
- **正/负类划分**: 132 positive / 397 negative

### 第三套（已修复 bug，曾影响 appendix multi-seed table）
- **函数**: `code/evaluation.py:compute_auroc()` (line 309)
- **旧代码**: `F1 > median`（正类 236 instances）
- **新代码**: `F1 >= median`（已修复，与 Paper Table 1 一致）

## 2. 差异根因

**根因是 binarization 阈值完全不同**，不是 bug，而是两个脚本用了不同的 AUROC 定义：

| 属性 | Paper Table 1 | Registry |
|------|--------------|----------|
| 阈值 | F1 ≥ median (0.6667) | F1 = 1.0 (perfect) |
| 正类数 | 301 (56.9%) | 132 (24.9%) |
| 负类数 | 228 (43.1%) | 397 (75.1%) |
| 语义 | "信号能否区分高于/低于中位数的 instance?" | "信号能否预测完美抽取?" |

### 为什么 EM 偏差最大 (13.5pp)

EM (Exact Match Rate) 衡量多个 sample 中最常见输出出现的频率。当多个 sample 完全一致时 EM=1.0，这与 F1=1.0（完美抽取）强相关——但与 F1 是否高于 0.667 的关系弱得多。因此 EM 在 "predict perfect" 任务上 AUROC=0.749 远高于 "above median" 任务上的 0.614。

### 为什么 LP 恰好匹配

LP (Log Probability) 对 SciERC 的 discriminative power 在两种 binarization 下恰好相近（0.578 vs 0.578），这是巧合而非系统性原因。

### 为什么 ρ 不受影响

Spearman ρ 直接在连续 F1 值上计算，不涉及 binarization，所以两个脚本的 ρ 完全一致。

## 3. 正确值是哪套

**Paper Table 1 的 median binarization 是正确的。**

理由：
1. **论文方法论一致性**: §3 明确定义 AUROC 为 "classifying instances as above/below median F1"
2. **统计惯例**: median split 的标准做法是 ≥ median 归上组
3. **15 个值全部验证通过**（5 signals × 3 datasets，误差 < 0.0005）
4. **"Predict perfect" 语义不合理**: SciERC 上只有 24.9% instance 达到 F1=1.0，这使得 AUROC 测量的是极端情况而非一般质量估计能力

Registry 的 `F1 >= 1.0` 定义在 CoNLL 上恰好与 median 一致（因为 CoNLL median F1 = 1.0），但在 SciERC 上两者大幅偏离。

## 4. 信号排序结论

### Paper Table 1 排序（正确，median binarization）
| Rank | Signal | AUROC |
|------|--------|-------|
| 1 | VC | .663 |
| 2 | SJ | .650 |
| 3 | EM | .614 |
| 4 | FK | .602 |
| 5 | LP | .578 |

### Registry 排序（不适用于 paper，perfect binarization）
| Rank | Signal | AUROC |
|------|--------|-------|
| 1 | EM | .749 |
| 2 | SJ | .692 |
| 3 | VC | .684 |
| 4 | FK | .629 |
| 5 | LP | .578 |

**EM 不是 SciERC AUROC 最高信号**（在 paper 定义下）。VC 和 SJ 仍然排名前两位。EM 仅在 "predict perfect extraction" 的不同语义下表现最佳。

## 5. 已存在的修复记录

`output/d114_auroc_investigation/` 目录下已有完整调查：
- `investigation.md` — 根因分析（`>` vs `>=` 的 evaluation.py bug + registry 用不同阈值）
- `table1_update.md` — Table 1 无需更新的确认
- `unified_auroc.json` — 修正后的全量 AUROC 数据

`evaluation.py:compute_auroc` 已从 `> median` 修复为 `>= median`。

## 6. 待办

- [ ] Appendix multi-seed table（`\ref{tab:multiseed}`）需要用修正后的 `compute_auroc` 重新生成，AUROC 值将下降约 0.013–0.033
- [ ] Registry 中 `exp_012_rerun_1024` 的 AUROC 值应标注为 "perfect-F1 threshold"，避免与 paper 的 median threshold 混淆
