# exp-003-p2 数据完整性检查

检查时间: 2026-05-20

## 1. Pure 模型 log_samples (1.3B)

全部存在，均为 lm-eval `--log_samples` 全 benchmark 输出（含 per-example logprob）：

| 模型 | 文件路径 | 大小 |
|------|----------|------|
| GatedDeltaNet-pure | `lm_eval_clean/1.3B-100B-GatedDeltaNet-pure.json` | 127M |
| RetNet-pure | `lm_eval_clean/1.3B-100B-RetNet-pure.json` | 127M |
| HGRN2-pure | `lm_eval_clean/1.3B-100B-HGRN2-pure.json` | 127M |

另有 GDN-pure LAMBADA-only 结果文件: `1.3B-100B-GatedDeltaNet-pure_lambada_only.json` (7.6M)，格式为 results（非 per-example samples）。

## 2. H3-1 (hybrid-3-1) 模型 log_samples (1.3B)

| 模型 | 文件路径 | 大小 | 状态 |
|------|----------|------|------|
| GatedDeltaNet h3-1 | 顶层无 log_samples，仅 `_results.json` (14K) | — | **缺失** |
| RetNet h3-1 | `lm_eval_clean/1.3B-100B-RetNet-hybrid-3-1.json` | 127M | 存在 |
| HGRN2 h3-1 | `lm_eval_clean/1.3B-100B-HGRN2-hybrid-3-1.json` | 127M | 存在 |

**注意**: GDN h3-1 的 log_samples 缺失。`1.3b/GDN-h3-1-logsamples/` 下有一个 12K 文件，是 results 格式（非 per-example）。顶层 `1.3B-100B-GatedDeltaNet-hybrid-3-1_results.json` 也仅是聚合 scores。

GDN **h12-1** 的 log_samples 存在: `1.3B-100B-GatedDeltaNet-hybrid-12-1.json` (127M)。

## 3. exp-003-p2 分析脚本和输出

| 文件 | 存在 | 详情 |
|------|------|------|
| `analysis/sample_perplexity_analysis.py` | ✓ | 12K, 2026-05-19 22:06 |
| `analysis/sample_perplexity_results.csv` | ✓ | 226K, 5154 行 (header + 5153 examples = LAMBADA 全集) |
| `analysis/sample_perplexity_summary.json` | ✓ | 统计检验结果 |
| `analysis/sample_perplexity_figure.pdf` | ✓ | 可视化 |
| `analysis/lambada_per_example.csv` | ✓ | 5162 行, 列含 `gdn_h12` (非 h3) |
| `analysis/lambada_matched_per_example.csv` | ✓ | 5162 行, matched comparison |

### sample_perplexity_results.csv 字段
```
doc_id, GDN_pure_loss, GDN_helped, GDN_hurt, RetNet_pure_loss, RetNet_helped, RetNet_hurt, HGRN2_pure_loss, HGRN2_helped, HGRN2_hurt
```

### 统计检验结果 (summary.json)
- GDN: helped=462, hurt=615, Mann-Whitney p=0.209 (不显著)
- RetNet: helped=426, hurt=495, p=0.659 (不显著)
- HGRN2: helped=548, hurt=395, p=0.248 (不显著)
- 结论: within-arch helped vs hurt perplexity 差异不显著

### lambada_per_example.csv 注意
列名使用 `gdn_h12`（hybrid-12-1）而非 `gdn_h3`（hybrid-3-1），说明 **GDN 的 per-example 分析使用了 h12-1 作为 hybrid baseline**，可能因为 h3-1 log_samples 缺失。

## 4. 结论

| 项 | 状态 |
|----|------|
| Pure 模型 log_samples | ✅ 3/3 完整 |
| H3-1 模型 log_samples | ⚠️ 2/3 (GDN h3-1 缺失，分析用了 h12-1 替代) |
| 分析脚本和结果 | ✅ 完整，5153 examples 覆盖 LAMBADA 全集 |
| 是否需要重跑 GPU inference | **视需求而定** — 如果要求 GDN 也用 h3-1 做 per-example 对比（与 RetNet/HGRN2 一致），需补跑 GDN h3-1 的 `--log_samples` eval；如果接受用 h12-1 作为 GDN hybrid baseline，则现有数据已足够 |
