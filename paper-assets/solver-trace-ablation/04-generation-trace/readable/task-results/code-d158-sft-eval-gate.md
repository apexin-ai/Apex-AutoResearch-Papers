# code d158 sft eval gate

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d158-sft-eval-gate_20260520T145414_result.json`
- **Structured JSON:** [`4d7c33baec9119131b11.json`](../../sessions/4d/4d7c33baec9119131b11.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## D158 LLaMA SFT Eval Report

### 结果

| 指标 | 值 | 目标 |
|------|-----|------|
| **prove_rate** | **0.0% (0/100)** | ≥ 10% |
| mean_isr | 0.0000 | — |
| median_isr | 0.0000 | — |
| 耗时 | 650.9s (6.5s/sample) | — |

### Gate 判定：**FAILED**

prove_rate = 0.0%，远低于 10% 门槛。

### 根因分析

从生成样本可以看到两个致命问题：

1. **生成退化为重复循环**：模型输出正确 FOL 后，不停止生成，而是循环重复 system prompt 和模板（`...Conclusion: Advocate(mary)assistant\n\nUse standard FOL notation...assistant\n\nOutput format:\nPremises:\n1. ∀x...`），直到 max_new_tokens。Conclusion 被附加 `assistant` 后缀。

2. **Unicode FOL vs Prover9 语法**：模型输出 Unicode 符号（∀, →, ∧, ¬, ⊕），Prover9 需要 ASCII 语法（`all x`, `->`, `&`, `-`, `|`）。即使去掉重复问题，Prover9 也无法解析。

训练时 94.5% token accuracy 只是表面指标——模型学会了复制训练格式但未学会正确终止和使用 Prover9 兼容语法。

---
