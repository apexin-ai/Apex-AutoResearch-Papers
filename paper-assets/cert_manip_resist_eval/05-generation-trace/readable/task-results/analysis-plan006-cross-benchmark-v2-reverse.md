# analysis plan006 cross benchmark v2 reverse

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan006-cross-benchmark-v2-reverse_20260524T103516_result.json`
- **Structured JSON:** [`cce704ab642c5b0793fc.json`](../../sessions/cc/cce704ab642c5b0793fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存到 `cross_benchmark_v2_bidirectional.json`。

## 完整结果

### β(K_eff) Sign Consistency: 17/18（对称，两个方向相同）

| K | 一致/总数 | 不一致条件 |
|---|----------|-----------|
| K=3 | 5/6 | **K3×position_bias** (MMLU β=+0.084, ARC β=−0.050) |
| K=5 | 6/6 | — |
| K=7 | 6/6 | — |

### Cross-Predict R² 双向对比

| Condition | MMLU→ARC R² | ARC→MMLU R² |
|-----------|-------------|-------------|
| K3×prompt_injection | 0.238 | **0.362** |
| K3×sycophancy | 0.130 | **0.156** |
| K3×score_manipulation | 0.178 | **0.360** |
| K3×verbosity_bias | 0.242 | **0.324** |
| K3×position_bias | −0.842 | 0.091 |
| K3×authority_bias | 0.096 | 0.070 |
| K5×prompt_injection | 0.220 | **0.299** |
| K5×sycophancy | −0.145 | −0.648 |
| K5×score_manipulation | **0.249** | 0.194 |
| K5×verbosity_bias | 0.120 | **0.293** |
| K5×position_bias | −2.528 | 0.086 |
| K5×authority_bias | −0.185 | −0.441 |
| K7×prompt_injection | 0.147 | **0.188** |
| K7×sycophancy | −0.469 | −1.772 |
| K7×score_manipulation | **0.188** | 0.148 |
| K7×verbosity_bias | −0.206 | **0.186** |
| K7×position_bias | −3.490 | 0.097 |
| K7×authority_bias | −0.489 | −1.014 |

### 关键发现

1. **Sign consistency 是对称的**：`sign(β_keff_MMLU) == sign(β_keff_ARC)` 不分方向，17/18 适用于两个方向。V1 的 14/18 和 10/18 差异应来自不同的定义或数据版本。

2. **Cross-predict R² 不对称**：ARC→MMLU方向在多数条件下R²更高（尤其K3），说明用ARC系数预测MMLU比反过来更准。这可能因为ARC拟合的系数更保守，泛化性更好。

3. **唯一不一致条件**：K3×position_bias（MMLU β_keff=+0.084 接近0，ARC β_keff=−0.050 不显著 p=0.43）。

---
