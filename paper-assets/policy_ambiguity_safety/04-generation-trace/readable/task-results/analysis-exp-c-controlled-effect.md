# analysis exp c controlled effect

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_c_controlled_effect_20260522T215835_result.json`
- **Structured JSON:** [`e4a15b205c2ec113f77e.json`](../../sessions/e4/e4a15b205c2ec113f77e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。产出：

- **脚本**: `artifacts/controlled_effect_size/compute_controlled_effect.py`
- **结果**: `artifacts/controlled_effect_size/results.json`

## 核心发现

| 指标 | 值 |
|------|-----|
| Incompleteness uncontrolled Δpp | +49.2pp |
| Incompleteness controlled Δpp (控制 token count) | +49.3pp [42.4, 56.2] |
| Reduction from controlling | -0.1pp（essentially zero） |
| token_count 系数 | β=+0.027, p=0.003 |
| token_delta moderation (M3) | β=+0.021, p=0.003 |

## 解读

1. **控制 token count 后 incompleteness 效应不变**：49.2→49.3pp，所有 6 个 type 的 reduction 均 < 0.1pp。Information-addition confound 不解释 type-specific effects。

2. **token_count 系数为正**：更长的 clause 预测 MORE violations（β=+0.027），方向与 information-addition 假说相反（该假说预期更多信息→更少 violation→更大 delta，即系数应为负）。

3. **Token delta 按 type 排序**：incompleteness（34.6）和 authorization_scope（36.1）delta 最大，但 auth_scope 效应（36.0pp）远小于 incompleteness（49.2pp），进一步说明 token delta 不驱动 type 差异。

4. **Model 3 (moderation)**: `is_ambiguous:token_delta` 显著（p=0.003），说明 within-type 内 token delta 较大的 clause 确实有稍大的条件效应，但这是对已有 type-specific interaction 的微调，不改变 predicted Δpp。

---
