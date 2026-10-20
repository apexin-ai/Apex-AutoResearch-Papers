# analysis math500 token length contrast

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_math500_token_length_contrast_20260515T172843_result.json`
- **Structured JSON:** [`9ecfae785d55e7eeccd5.json`](../../sessions/9e/9ecfae785d55e7eeccd5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**MATH-500 (n=500)**: 长题组的 |strategy specificity| 比短题组高 30-43%，Mann-Whitney U 检验在所有 sparsity 水平显著（p=0.0002 ~ 0.013），per-problem Spearman 相关在 s015-s025 显著。**假设在 MATH-500 上成立。**

**GSM8K (n=50)**: 方向相反——短题 specificity 更高，s025/s030 处负相关显著。原因可能是 GSM8K 短题推理结构更紧凑，长题多为 2047 截断的挣扎生成。

**跨 benchmark**: GSM8K 中位数 (540) 落在 MATH-500 短题区间内，但 GSM8K 短题的 specificity 与 MATH-500 短题相当甚至更高，说明 **raw token length 单独不能解释 specificity，需要同时考虑 task complexity**。

交付物：
- 报告：`artifacts/math500_token_length/report.md`
- JSON：服务器 `analysis_output/math500_token_length_stratification.json` (44KB)
- 脚本：服务器 `analysis/math500_token_length_stratification.py`

---
