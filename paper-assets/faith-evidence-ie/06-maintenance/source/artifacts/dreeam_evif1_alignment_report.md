# DREEAM Evi-F1 对齐分析报告（实测版）

**日期**: 2026-05-17  
**状态**: 已验证，代码已修改

## 结论

我们已有的 `evi_f1_joint` 指标与 DREEAM 协议一致（已通过代码比对和数值交叉验证）。此前一直报告的 `evi_f1` 是膨胀指标（仅在 TP triples 上计算 evidence P/R），不可与 DREEAM 对比。

## 1. 协议差异

### 我们的 `compute_evi_f1`（膨胀，不可比）
```
Precision = 正确 evidence / TP triples 的预测 evidence
Recall   = 正确 evidence / TP triples 的 gold evidence
```
不惩罚 FP triples 产生的多余 evidence，也不惩罚 FN triples 遗漏的 gold evidence。

### DREEAM 协议 = 我们的 `compute_evi_f1_joint`
```
Precision = 正确 evidence / 所有预测 evidence（含 FP triples）
Recall   = 正确 evidence / 所有 gold evidence（含 FN triples）
```
来源：DREEAM `official_evaluate()` 函数 = DocRED 官方评测协议。

### 实现验证
逐行比对 `evaluator.py:compute_evi_f1_joint` 与 `baselines/dreeam/evaluation.py:official_evaluate`，逻辑完全一致。唯一差异是实体匹配方式（名称 vs 索引），这是 LLM 方法的固有特点。

## 2. DREEAM baseline 实测

用 DREEAM 官方评估代码对我们复现的 RoBERTa teacher 预测重新评测：
```
RE:  P=66.95  R=60.51  F1=63.57
Evi: P=60.53  R=48.76  F1=54.01
Ign-F1=61.72
```

## 3. 全模型数值对比

| 模型 | RE F1 | evi_f1 (膨胀) | evi_f1_joint (DREEAM) | EDCR |
|------|-------|--------------|----------------------|------|
| SFT 4B baseline | 40.49 | 79.86 | **31.47** | 0.698 |
| RSFT-CED s42 | 45.17 | 81.74 | **35.18** | 0.657 |
| RSFT-CED s43 | 46.01 | 80.63 | **36.05** | 0.654 |
| RSFT-CED s44 (best 4B) | 46.21 | 80.50 | **36.77** | 0.635 |
| RSFT-CED s45 | 45.14 | 81.74 | **35.58** | 0.655 |
| RSFT-flat-NLI s43 r2 | 45.86 | 81.13 | **35.80** | 0.655 |
| RSFT-flat-NLI s44 | 46.15 | 81.31 | **35.97** | 0.646 |
| RSFT-flat-NLI s45 | 45.51 | 81.54 | **35.56** | 0.652 |
| RSFT-topk3 | 44.54 | 80.88 | **34.78** | 0.664 |
| Qwen3-1.7B SFT | 49.45 | 83.16 | **39.58** | 0.670 |
| Qwen3-1.7B RSFT r2 | 52.19 | 83.09 | **42.23** | 0.630 |
| Qwen3-8B SFT | 52.62 | 81.88 | **41.39** | 0.651 |
| LLaMA-8B SFT | 55.14 | 81.51 | **43.17** | 0.628 |
| LLaMA-8B RSFT r3 (best) | 56.74 | 82.55 | **45.71** | 0.586 |
| DPO-CED | 40.34 | 80.88 | **30.69** | 0.714 |
| GRPO g8 ckpt100 | 45.49 | 80.86 | **35.71** | 0.632 |
| **DREEAM (RoBERTa)** | **63.57** | - | **54.01** | - |

## 4. 关键发现

1. **evi_f1 膨胀约 2.2x**：所有模型 `evi_f1` ≈ 0.80，`evi_f1_joint` ≈ 0.31-0.46。

2. **所有模型低于 DREEAM**：最好的 LLaMA-8B RSFT (45.71) 仍低于 DREEAM (54.01) 约 8.3 个点。

3. **evi_f1_joint 与 RE F1 高度相关**（r > 0.99）：当前瓶颈是 RE 本身，不是 evidence 定位。

4. **EDCR 高 (0.58-0.71)**：即使在 TP triples 上，约 60-70% 预测 evidence 是非 gold 句，evidence 定位能力也需改进。

5. **RSFT 改进方向正确**：SFT→RSFT 提升 RE F1 约 5-6 个点（40→46 for 4B），evi_f1_joint 相应提升约 5 个点（31→37）。

## 5. 代码修改记录

- `eval/inference.py`: 显示输出从 `Evi-F1` 改为 `Evi-F1(DREEAM)` + `Evi-F1(TP)`
- `eval/batch_eval.py`: summary 中增加 `evi_f1_joint` 字段；显示输出增加 `Evi-F1(DREEAM)`

无需修改 `evaluator.py`（`compute_evi_f1_joint` 已正确实现 DREEAM 协议）。

## 6. 论文建议

- 论文中 Evi-F1 **必须使用 `evi_f1_joint`**（DREEAM 协议）
- `evi_f1`（TP-only）可作为 Analysis/Appendix 的补充指标，说明在 TP triples 上 evidence 定位质量
- 与 DREEAM 的差距主要来自 RE F1 差距（63.57 vs 40-57），应在论文中分析
