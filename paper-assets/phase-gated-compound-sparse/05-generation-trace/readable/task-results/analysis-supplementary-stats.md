# analysis supplementary stats

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_supplementary_stats_20260515T082515_result.json`
- **Structured JSON:** [`7ec1526b1e412c126707.json`](../../sessions/7e/7ec1526b1e412c126707.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 5 项分析完成。

**结果摘要：**

1. **CI Width Shrinkage**: 16 个 condition 的 CI 宽度缩窄 2.5–5.9×（均值 3.7×），直接证明 n=500 的精度提升。

2. **BH-FDR**: 44 个检验中，BH-FDR 显著 37 个 vs Bonferroni 32 个。DS random s025/s030 的 Wilcoxon 从 Bonferroni borderline (p≈0.065) 恢复为 BH 显著 (q < 0.002)。

3. **JT Test**: 所有 4 组（DS/QW × imp/rand）均高度显著（z=6.2–33.7, 全部 p < 1e-9），彻底解决 4-point Spearman p=0.042 功效不足的质疑。

4. **G Bootstrap CI**: Importance masking G=22–148×（所有 CI 远离 1），确认低相位放大效应。Random masking G≈0.5–1.3，无相位不对称性。

5. **Spearman**: 确认 scipy 默认两尾。精确排列（4!=24）：两尾 p=0.0833，单尾 p=0.0417。此前报告的 p=0.042 即为单尾精确值。

**输出文件：**
- JSON: `/root/autodl-tmp/pacs/analysis_output/supplementary_stats.json`
- 摘要: `artifacts/n500_analysis/supplementary_stats.md`

---
