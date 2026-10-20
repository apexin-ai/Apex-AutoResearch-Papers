# code bootstrap ci analysis

**prism collapse mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_bootstrap_ci_analysis_20260516T011707_result.json`
- **Structured JSON:** [`e0c2c99dc019d0058ff6.json`](../../sessions/e0/e0c2c99dc019d0058ff6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**Entropy 信号**：
- Gen0 ρ=0.929 CI [0.925, 0.934]，Gen1 ρ=0.912 CI [0.906, 0.917]  — CI 包含已知参考值
- Δρ = -0.017，effect_size ≈ -5.8（显著下降）
- Permutation test p=0.50（仅 2 代数据，置换检验力有限，预期行为）

**Spectral_rank 信号**：
- Δρ ≈ +0.006，effect_size ≈ 0.4（无显著变化）
- Permutation test p=1.0（无下降趋势）

JSON 已保存至 `results/bootstrap_analysis.json`。现有 Condition 1/2/3 逻辑未修改。

---
