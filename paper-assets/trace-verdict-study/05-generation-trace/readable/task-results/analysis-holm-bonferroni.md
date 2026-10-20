# analysis holm bonferroni

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_holm_bonferroni_20260522T070013_result.json`
- **Structured JSON:** [`4b7aa6886bee361aad43.json`](../../sessions/4b/4b7aa6886bee361aad43.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有文件已生成且 JSON 可解析。结果汇总：

### 统计概览
- **总 pairwise 比较**: 80（4 models × 各自 condition pairs）
- **原始显著 (p<0.05)**: 70/80 (87.5%)
- **Holm-Bonferroni 校正后显著**: 67/80 (83.8%)
- **BH FDR 校正后显著**: 70/80 (87.5%)

### Holm-Bonferroni 校正后失去显著性的 3 个比较
| Model | Pair | Diff | orig_p | holm_p |
|-------|------|------|--------|--------|
| Qwen-1.5B | ae_only vs exception_only | -0.0075 | 0.012 | 0.060 |
| Qwen-1.5B | ae_only vs nomarker | +0.0128 | 0.015 | 0.060 |
| DeepSeek-6.7B | loop_only vs vota | -0.0319 | 0.037 | 0.110 |

### 关键 Borderline 比较（校正后 p-value）
- **CodeLlama loop_only vs no_trace** (仅 0.56pp 差距): holm_p=0.708, **不显著** — 符合预期
- **Qwen-7B label_only vs loop_only** (0.59pp): holm_p=1.000, **不显著**
- **full_trace vs no_trace**: 所有模型校正后均显著 (holm_p < 0.006)
- **loop_only vs ae_only**: 所有模型校正后均显著

### 结论
多重比较校正影响极小。80 个比较中仅 3 个在 Holm-Bonferroni 后失去显著性，且都是原本就 borderline 的小差距 (≤3.2pp)。论文核心结论（Tier 结构、trace 类型排序）完全不受影响。

---
