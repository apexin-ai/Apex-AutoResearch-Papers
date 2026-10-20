# analysis gsm8k token length

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gsm8k_token_length_20260515T172832_result.json`
- **Structured JSON:** [`1409041b55726668a747.json`](../../sessions/14/1409041b55726668a747.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

**结论：Token length 假设不成立。**

关键发现：

1. **DS 模型**（有 token length 变异：287–2047）：长题组 vs 短题组的 strategy specificity ratio 在所有 sparsity 水平均无显著差异（所有 p > 0.27）。s=0.15 和 s=0.20 甚至短题比长题 ratio 更高（方向相反）。

2. **QW 模型**：50 题全部生成 2047 tokens（撞 max_new_tokens 上限），无法做分层分析。QW 在 GSM8K 上持续耗尽生成预算。

3. **Phase segmentation 质量**：短题 DS 平均仍有 13.2 个 phase，无退化问题。分割质量不解释 ratio 衰减。

4. **需要探索替代假设**：GSM8K 的算术推理可能本身 sparsity landscape 更平坦，与推理链长度无关。

报告：`artifacts/gsm8k_token_length/report.md`
JSON 数据：服务器 `analysis_output/gsm8k/gsm8k_token_length_stratification.json`

---
