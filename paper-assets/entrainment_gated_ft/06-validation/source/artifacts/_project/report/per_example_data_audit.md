# Per-Example Data Audit

**日期**: 2026-05-19  
**服务器**: westb-48145  
**路径**: `/root/entrainment_gated_ft/lm_eval_clean/`

## 数据格式说明

per-example 数据存在两种格式：
1. **嵌入式 JSON**（~127-132MB）：lm_eval 旧版输出，per-example 数据嵌入在单个大 JSON 文件中，覆盖所有 benchmark
2. **JSONL logsamples**：`samples/` 子目录下的独立 JSONL 文件，每个 benchmark 一个文件

## 1.3B Models

Benchmarks: lambada_openai, hellaswag, winogrande, arc_easy, arc_challenge, mmlu

| 模型 | aggregate results | per-example (嵌入 JSON) | per-example (JSONL logsamples) | benchmarks with samples |
|------|-------------------|------------------------|-------------------------------|------------------------|
| GDN-pure | ✅ | ✅ 127M | — | all 6 benchmarks |
| GDN-h3-1 | ✅ (14K) | ❌ | ✅ lambada_openai (5153 lines) | lambada_openai only |
| GDN-h6-1 | ✅ (14K) | ❌ | ✅ lambada_openai (5153 lines) | lambada_openai only |
| GDN-h12-1 | ✅ 127M (含 per-example) | ✅ 127M | — | all 6 benchmarks |
| GDN-h24-1 | ✅ (14K) | ❌ | ✅ lambada_openai (5153 lines) | lambada_openai only |
| HGRN2-pure | ✅ 127M | ✅ 127M | — | all 6 benchmarks |
| HGRN2-h3-1 | ✅ 127M | ✅ 127M | — | all 6 benchmarks |
| HGRN2-h6-1 | ✅ 127M | ✅ 127M | — | all 6 benchmarks |
| HGRN2-h12-1 | ✅ 127M | ✅ 127M | — | all 6 benchmarks |
| HGRN2-h24-1 | ✅ 127M | ✅ 127M | — | all 6 benchmarks |
| RetNet-pure | ✅ 127M + 14K | ✅ 127M | — | all 6 benchmarks |
| RetNet-h3-1 | ✅ 127M | ✅ 127M | — | all 6 benchmarks |
| RetNet-h6-1 | ✅ 127M | ✅ 127M | — | all 6 benchmarks |
| RetNet-h12-1 | ✅ 127M | ✅ 127M | — | all 6 benchmarks |
| RetNet-h24-1 | ✅ 127M | ✅ 127M | — | all 6 benchmarks |
| Transformer baseline | ✅ 127M | ✅ 127M | — | all 6 benchmarks |

**Multiseed 数据**（`multiseed/` 子目录，仅 aggregate `results.json`，无 per-example）：
- GDN-pure: seed_0, seed_1, seed_4
- GDN-h24-1: seed_0, seed_4

**其他文件**：
- `GDN-pure_lambada_only.json` (7.6M) — lambada 单独评估，含 per-example
- `summary_all_1.3b.csv` (2.7K, 17 行) — 全模型 aggregate 汇总表

## 340M Models

| 模型 | aggregate results | per-example (嵌入 JSON) | per-example (JSONL logsamples) | benchmarks with samples |
|------|-------------------|------------------------|-------------------------------|------------------------|
| GDN-pure | ✅ 132M | ✅ 132M | — | all benchmarks |
| GDN-h3-1 | ✅ 132M | ✅ 132M | — | all benchmarks |
| GDN-h6-1 | ✅ 132M | ✅ 132M | — | all benchmarks |
| GDN-h12-1 | ✅ 132M | ✅ 132M | — | all benchmarks |
| GDN-h24-1 (New) | ✅ 132M | ✅ 132M | — | all benchmarks |
| Transformer baseline | ✅ 132M | ✅ 132M | — | all benchmarks |
| RetNet-pure | ✅ (144K, aggregate only) | ❌ | ❌ | — |
| RetNet-h3-1 | ✅ (aggregate only) | ❌ | ❌ | — |
| RetNet-h6-1 | ✅ (aggregate only) | ❌ | ❌ | — |
| RetNet-h12-1 | ✅ (aggregate only) | ❌ | ❌ | — |
| RetNet-h24-1 | ✅ (aggregate only) | ❌ | ❌ | — |
| HGRN2-pure | ✅ (144K, aggregate only) | ❌ | ❌ | — |
| HGRN2-h3-1 | ✅ (aggregate only) | ❌ | ❌ | — |
| HGRN2-h6-1 | ✅ (aggregate only) | ❌ | ❌ | — |
| HGRN2-h12-1 | ✅ (aggregate only) | ❌ | ❌ | — |
| HGRN2-h24-1 | ✅ (aggregate only) | ❌ | ❌ | — |

## Analysis CSV Files

| 文件名 | 行数 | 列 | 内容描述 |
|--------|------|-----|----------|
| `lambada_per_example.csv` | 5162 (5161 examples) | doc_id, context_length, target, gdn_pure_acc, gdn_pure_lp, gdn_h12_acc, gdn_h12_lp, hgrn2_pure_acc, hgrn2_pure_lp, hgrn2_h3_acc, hgrn2_h3_lp | 4 模型在 lambada 上的 per-example accuracy 和 logprob（GDN pure/h12, HGRN2 pure/h3） |
| `lambada_matched_per_example.csv` | 5162 (5161 examples) | doc_id, context_length, target, gdn_pure_acc, gdn_pure_lp, gdn_h31_acc, gdn_h31_lp, hgrn2_pure_acc, hgrn2_pure_lp, hgrn2_h31_acc, hgrn2_h31_lp | 4 模型 matched 对比（GDN pure/h31, HGRN2 pure/h31） |
| `cross_scale_summary.csv` | 61 (60 rows) | scale, attn_layers, benchmark, arch_std, arch_range, arch_values, min_std_attn, min_std, reduction_pct, rebound_pct | 跨规模收敛性分析汇总 |

## 缺口分析

### 需要补跑 log_samples 的模型

**1.3B — 高优先级**：
- **GDN-h3-1**: 仅有 lambada_openai 的 JSONL logsamples，缺少 hellaswag/winogrande/arc_easy/arc_challenge/mmlu 的 per-example 数据
- **GDN-h6-1**: 同上
- **GDN-h24-1**: 同上

> 注：这 3 个模型的 aggregate `_results.json` 只有 14K，说明当初只跑了 `--log_samples` 但输出格式是 JSONL 而非嵌入 JSON，且只对 lambada_openai 保留了 samples。如需全 benchmark per-example 数据，需用大 JSON 格式重跑或为其他 benchmark 补跑 `--log_samples`。

**340M — 需补跑**：
- **RetNet 全系列**（pure, h3-1, h6-1, h12-1, h24-1）：仅有 aggregate，无任何 per-example 数据
- **HGRN2 全系列**（pure, h3-1, h6-1, h12-1, h24-1）：仅有 aggregate，无任何 per-example 数据

> 340M 的 RetNet 和 HGRN2 是后批次跑的评估（`run_all.log`），没有用 `--log_samples` 参数。

### 当前 per-example 数据能支撑的分析

1. **1.3B 全架构 per-example 对比**（lambada + 其他 benchmark）：GDN-pure, GDN-h12-1, 全部 HGRN2, 全部 RetNet, Transformer baseline — 共 13 个模型，覆盖完整
2. **1.3B GDN 系列 lambada per-example 对比**：所有 5 个 GDN 变体（pure, h3, h6, h12, h24）都有 lambada per-example 数据
3. **340M GDN + Transformer per-example 对比**：6 个模型有完整 per-example 数据
4. **Analysis CSV 已有分析**：lambada per-example 对比已做（GDN pure/h12 vs HGRN2 pure/h3 两组），matched 版本也做了（GDN pure/h31 vs HGRN2 pure/h31）
5. **跨规模分析**：cross_scale_summary.csv 覆盖 1.3B 和 340M 的 convergence 分析

### 不能做的分析（缺数据）

- **340M RetNet/HGRN2 per-example 粒度分析**：无法做 per-example 难度分层、attention 效果、context length 依赖等分析
- **340M 全架构 per-example 对比**：缺少 RetNet 和 HGRN2 的 per-example 数据
- **1.3B GDN-h3/h6/h24 在 lambada 以外 benchmark 的 per-example 分析**：仅有 lambada logsamples
