# analysis stratified bootstrap check

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_stratified_bootstrap_check_20260522T104144_result.json`
- **Structured JSON:** [`b795f5a9db4b602db76e.json`](../../sessions/b7/b795f5a9db4b602db76e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：**分层对 CI 影响微小**（<10% 变化），不需要替换 simple bootstrap。

关键数字对比：

| 指标 | Simple CI width | Stratified CI width | 变化 |
|------|----------------|-------------------|------|
| G_item | 0.0395 | 0.0410 | **+3.95%** |
| item_id% | 9.376 | 9.662 | **+3.05%** |
| model:item_id | 6.392 | 6.358 | -0.53% |
| residual | 4.177 | 4.226 | +1.16% |

Stratified bootstrap 的 CI 反而略宽（~3-4%），因为分层约束了每次 resample 必须包含所有 10 个 subject，减少了 bootstrap 样本的变异性空间。主要 component（item_id, model:item_id, residual）的 CI 差异均在 ±5% 以内。

结论：simple bootstrap 的结果可靠，分层结构对 CI 估计无实质影响。

---
