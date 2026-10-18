# eval plan 009 token importance v3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan_009_token_importance_v3_20260516T164707_result.json`
- **Structured JSON:** [`23dc2a53e9f382e8337f.json`](../../sessions/23/23dc2a53e9f382e8337f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**Plan 009 Token Importance 分析 — 100 samples on imm_anchor_v8b_twostage**

| 指标 | 值 |
|------|-----|
| Spearman correlation (importance vs gradient) | **0.407 ± 0.102** (median 0.407) |
| Gradient ratio (retained / pruned) | **1.70x** |
| Retained tokens grad mean | 3.11e-4 |
| Pruned tokens grad mean | 1.83e-4 |
| Visual tokens per sample | 64 |

ACIS importance scores 与 action prediction gradient magnitude 有中等正相关 (ρ≈0.41)，被 ACIS 保留的 top-50% tokens 的梯度幅度比被删除的 bottom-50% 高 70%。这说明 ACIS 确实倾向于保留对 action prediction 贡献更大的 visual tokens。

Part B (attention weight 分布) 未执行 — Part A 已充分验证 ACIS 的选择合理性。

---
