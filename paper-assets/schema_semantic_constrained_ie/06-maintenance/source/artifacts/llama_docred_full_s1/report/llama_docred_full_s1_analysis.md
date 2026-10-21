# Llama-3.1-8B DocRED full_s1 实验分析

**Date:** 2026-05-14
**Checker:** fixed_20260514_v2 (strip + alias + unique_et)
**F1 method:** all_set

## Metrics

### Violation Rates

| Metric | Llama unconstrained | Llama full_s1 | Delta | Qwen full_s1 |
|--------|-------------------|--------------|-------|-------------|
| ET | 0.13% | **0.00%** | -0.13pp | 0.00% |
| RV | 16.03% | **0.00%** | -16.03pp | 0.03% |
| DR | 26.07% | **2.55%** | -23.52pp | 10.19% |
| CF | 0.17% | **12.02%** | +11.85pp | 2.57% |
| Parse fail | 68/998 | 91/998 | +23 | — |

### F1 Scores

| Metric | Llama unconstrained | Llama full_s1 | Delta | Qwen full_s1 |
|--------|-------------------|--------------|-------|-------------|
| E-F1 | 55.65% | 55.01% | -0.64pp | 59.37% |
| E-P | 61.22% | 61.41% | +0.19pp | — |
| E-R | 51.02% | 49.82% | -1.20pp | — |
| R-F1 | 5.98% | 6.27% | +0.29pp | 8.23% |
| R-P | 5.22% | 5.49% | +0.27pp | — |
| R-R | 7.00% | 7.32% | +0.32pp | — |

### Counts

| | Unconstrained | full_s1 |
|---|---|---|
| Docs checked | 930/998 | 907/998 |
| Unique entities | 11525 | 11296 |
| Triples | 16437 | 16368 |
| Fuzzy relation matches | 121 | 0 |

## 三方对比：Llama unconstrained → Llama full_s1 → Qwen full_s1

| Metric | Llama uncon | Llama full_s1 | Qwen full_s1 |
|--------|------------|--------------|-------------|
| DR | 26.07% | 2.55% | 10.19% |
| RV | 16.03% | 0.00% | 0.03% |
| ET | 0.13% | 0.00% | 0.00% |
| CF | 0.17% | **12.02%** | 2.57% |
| E-F1 | 55.65% | 55.01% | 59.37% |
| R-F1 | 5.98% | 6.27% | 8.23% |

## 结论

**Conclusion: success (with CF caveat)**

1. **结构性违规大幅消除**：ET/RV 降至 0%，DR 从 26.07% 降至 2.55%（-23.52pp），效果甚至优于 Qwen full_s1（10.19%）。grammar 约束完全消除了 ET 和 RV 违规，semantic 约束进一步压低了 DR。

2. **CF 违规暴涨是主要问题**：CF 从 0.17% 飙升至 12.02%（+11.85pp），远高于 Qwen full_s1 的 2.57%。原因：约束解码在不同 triple 上下文中强制选择合法类型，导致同一实体在不同关系中被分配了不一致的类型。Llama 比 Qwen 更严重，说明 Llama 的 entity type 预测更容易被约束扰动。

3. **F1 基本持平**：E-F1 微降 0.64pp，R-F1 微升 0.29pp。约束解码没有显著改变任务性能，但也没有损害。

4. **Parse failures 增加**：68 → 91（+23），constrained decoding 略增加了生成失败率。

5. **与 Qwen 对比**：Llama full_s1 在 DR/RV/ET 上优于 Qwen full_s1，但 CF 远差，且 F1 整体低于 Qwen（E-F1 55.01% vs 59.37%，R-F1 6.27% vs 8.23%）。
