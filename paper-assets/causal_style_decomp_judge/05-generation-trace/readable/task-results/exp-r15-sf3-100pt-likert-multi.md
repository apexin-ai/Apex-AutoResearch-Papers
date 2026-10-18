# exp r15 sf3 100pt likert multi

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_r15-sf3-100pt-likert-multi_20260523T065159_result.json`
- **Structured JSON:** [`acf7c66d662bdfe3b95f.json`](../../sessions/ac/acf7c66d662bdfe3b95f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存。总结：

| Judge | Scale | ATE | Cohen's d | p | Tie Rate |
|-------|-------|-----|-----------|---|----------|
| **Qwen3-32B** | 1-10 | 0.011 | 0.012 | 0.908 | 72.7% |
| **Qwen3-32B** | 1-100 | 1.830 | 0.153 | 0.154 | 51.1% |
| **Llama-3.3-70B** | 1-10 | 0.000 | 0.000 | 1.000 | 72.7% |
| **Llama-3.3-70B** | 1-100 | 1.386 | 0.085 | 0.440 | 39.8% |
| **GPT-4o** (ref) | 1-100 | -0.625 | -0.038 | 0.725 | 65.9% |

关键发现：
- **100pt 降低 tie rate**：Qwen -21.6pp，Llama -32.9pp，但 GPT-4o 仍高达 65.9%
- **ATE 全部不显著**（所有 p > 0.15），确认 formality 不系统性影响 quality 评分
- **有效粒度差异大**：GPT-4o 实际只用 5 个值（0/25/50/75/100），Qwen 聚集在 5 的倍数（~20 个 bin），Llama 使用最多样的非整数值（真正接近连续）
- Llama 有 5 个 pair 返回 score=0（超出范围），实际 n=83

---
