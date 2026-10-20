# Llama DocRED Unconstrained — max_new_tokens 6144 vs 4096

- **exp_id**: `llama_docred_unconstrained_mt6144`
- **server**: westd-16980 (cuda:0)
- **model**: Llama-3.1-8B-Instruct
- **dataset**: DocRED dev (998 docs)
- **mode**: unconstrained
- **checker**: `analyze_llama_docred.py` (fixed_20260514_v2, all_set F1)
- **input**: `outputs/llama_docred_unconstrained_mt6144.jsonl`
- **summary**: `outputs/analysis_llama_docred_unconstrained_mt6144_v2.json`

## 关键指标对比

| 指标 | mt4096 (baseline) | mt6144 | Δ |
|---|---:|---:|---:|
| documents_checked | 930 | 931 | +1 |
| parse_failures | 68 | 67 | **−1** |
| unique_entities | 11,525 | 11,534 | +9 |
| total_triples | 16,437 | 16,584 | +147 (+0.9%) |
| dr_eligible_triples | 13,789 | 13,936 | +147 |
| ET (entity-type viol.) | 0.13% | 0.13% | 0.00pp |
| RV (relation vocab) | 16.03% | 15.89% | −0.14pp |
| DR (domain/range, all) | 26.07% | 26.18% | +0.11pp |
| DR (eligible only) | — | 31.15% | — |
| CF (cross-field) | 0.17% | 0.17% | 0.00pp |
| Entity P / R / F1 | 61.22 / 51.02 / 55.65 | 61.19 / 51.06 / 55.67 | −0.03 / +0.04 / +0.02pp |
| Relation P / R / F1 | 5.22 / 7.00 / 5.98 | 5.18 / 7.00 / 5.95 | −0.04 / 0.00 / −0.03pp |
| Wall clock | ~5h 02m | ~5h 39m | +37min |

## Parse failures 来源分析

mt6144 仍有 67 个 parse failure，其中 **绝大多数 inference 时间 ~96s**——这是 batch_size=1 下生成到 max_new_tokens 上限的典型耗时特征。换句话说，模型并非因为文档长而需要更多输出 token，而是 **陷入重复/退化循环直到 token cap**。把 cap 从 4096 抬到 6144 只挽救了 1 个文档（68→67），说明真正可被 token 预算挽回的失败是个位数。

## 结论

- max_new_tokens 4096 → 6144 对 unconstrained 生成 **无实质影响**：F1 抖动 <0.1pp，违规率几乎不变，parse failure 仅减少 1 例。
- 多出来的 147 条 triples 主要来自被挽救的那 1 个文档以及 token 预算更宽松后模型在已成功文档里多输出的几条尾部三元组，对整体 R-F1 没有正向贡献（R-P 略降）。
- 代价：wall clock 多 ~12%（+37 分钟）。
- **建议**：保留 mt4096 作为 unconstrained 基线，不必为更长 max_new_tokens 付出额外推理时间；如要降低 parse failure，应改进 prompt 抑制循环（如加 stop sequence、降 repetition penalty）或加事后修复，而非加 token 预算。
