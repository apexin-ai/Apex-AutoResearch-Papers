# code exp w8 a5 violation

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-w8-a5-violation_20260522T101532_result.json`
- **Structured JSON:** [`162e96d6232f8dd56be5.json`](../../sessions/16/162e96d6232f8dd56be5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验 W8 完成。核心发现：

**Aligned（正相关：high-error × large-Δτ）**
- Naive 在 S₁ 上 coverage 仅 25%，RMSE 0.184 — bias 被 δ×Δτ 乘积放大
- Global corrected 改善有限（S₁ coverage 78%），因为全局 CM 无法捕捉子群差异
- **EC-HTE (EB) 在两个子群都达到 95%+ coverage**，RMSE 降至 0.100 (S₁) / 0.069 (S₀)

**Adversarial（负相关：high-error × small-Δτ）**
- Naive bias 被削弱但仍显著（S₁ coverage 78%）
- Global corrected 在 S₀ 反而变差（coverage 78%），因为全局校正对 low-error 子群过度校正
- **EC-HTE (EB) 同样保持 93-98% coverage**

**结论**：EC-HTE 在两种相关结构下都维持近 nominal coverage，不依赖 A5 假设。

产出文件：
- 代码：`exp_w8_a5_violation.py`
- 聚合结果：`results/exp_w8_a5_violation.csv`
- 原始数据：`results/exp_w8_a5_violation_raw.csv`
- LaTeX 段落已在脚本输出末尾生成

---
