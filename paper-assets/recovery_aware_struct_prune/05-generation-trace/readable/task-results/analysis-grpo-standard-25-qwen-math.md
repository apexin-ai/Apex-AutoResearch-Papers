# analysis grpo standard 25 qwen math

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_grpo_standard_25_qwen_math_20260516T154213_result.json`
- **Structured JSON:** [`685f6c9fd2cface6fe2a.json`](../../sessions/68/685f6c9fd2cface6fe2a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。Registry 已更新为 DONE/success。

**结论: success** — Qwen2.5-Math-7B Standard 25% GRPO 展示了 **mild transient dip** pattern:
- Reward dip: step 20-30 (0.20 → 0.106, -47%)，step 40 恢复至 0.211
- frac_zero_std 峰值 0.425（未达 collapse 阈值 0.8）
- 比 DeepSeek Standard 20% 的 dip 更早出现（step 20-30 vs step 60），符合"更高稀疏度→更早 dip"假设
- 2 次极端 loss/KL spike（step 40: 3.7e14, step 80: 2.2e5）但均自行恢复，为 Qwen Math 特有的数值不稳定现象

---
