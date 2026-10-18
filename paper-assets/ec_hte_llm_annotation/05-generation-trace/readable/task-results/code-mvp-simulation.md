# code mvp simulation

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp_simulation_20260520T175313_result.json`
- **Structured JSON:** [`b7b22232cfd1bbece7db.json`](../../sessions/b7/b7b22232cfd1bbece7db.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

N_MC=100 完整结果，3.4 秒完成。关键发现清晰且稳定：

**Extreme regime (misclass_A=0.25, misclass_B=0.05), n_expert=500:**

| 子群 | 方法 | bias_z0 | bias_z1 | rmse_z0 | rmse_z1 |
|------|------|---------|---------|---------|---------|
| A (高误差) | Naive | **+0.098** | **-0.100** | 0.116 | 0.120 |
| A | Global | +0.054 | -0.055 | 0.096 | 0.100 |
| A | **EC-HTE** | **-0.009** | **+0.008** | 0.111 | 0.113 |
| B (低误差) | Naive | +0.009 | -0.025 | 0.058 | 0.066 |
| B | Global | **-0.070** | **+0.055** | 0.100 | 0.093 |
| B | **EC-HTE** | **-0.014** | **-0.002** | 0.063 | 0.066 |

核心验证：
1. **Naive** 在高误差子群 A 偏差大 (|bias_z1|=0.10)
2. **Global 在子群 A 欠校正** (|bias_z1|=0.055 vs EC-HTE's 0.008)，**在子群 B 过校正加偏** (|bias_z1|=0.055 vs Naive's 0.025)
3. **EC-HTE 在两个子群均接近无偏** (|bias| < 0.015)
4. **Homogeneous regime**: Global ≈ EC-HTE（符合预期——无异质性时两者等价）
5. n_expert 增加时 EC-HTE 的 bias 下降（100→500: subgroup A bias_z1 从 0.024→0.008）

CSV 已保存到 `/home/ubuntu/ec_hte_llm_annotation/results/mvp_results.csv` 和 `mvp_results_raw.csv`。

---
