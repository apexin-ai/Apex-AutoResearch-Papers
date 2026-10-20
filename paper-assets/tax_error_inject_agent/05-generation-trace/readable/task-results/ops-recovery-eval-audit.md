# ops recovery eval audit

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_recovery-eval-audit_20260516T031812_result.json`
- **Structured JSON:** [`bce6b8ab01d11ec928d4.json`](../../sessions/bc/bce6b8ab01d11ec928d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

确认完毕。**7/15 已完成，8/15 缺失。** 之前报告的 7/15 与文件系统一致。

## Recovery Eval 完成状态

| # | Condition | Seed | Status | File | Rate | Total |
|---|-----------|------|--------|------|------|-------|
| 1 | Vanilla | 42 | **done** | `v4_vanilla_recovery_eval.json` | 0.617 | 47 |
| 2 | Vanilla | 0 | **done** | `v4_vanilla_recovery_eval_s0.json` | 0.681 | 47 |
| 3 | Vanilla | 123 | **done** | `v4_vanilla_recovery_eval_s123.json` | 0.660 | 47 |
| 4 | Vanilla | 1 | missing | — | — | — |
| 5 | Vanilla | 7 | missing | — | — | — |
| 6 | TaxEI | 42 | **done** | `v4_taxei_recovery_eval.json` | 0.596 | 47 |
| 7 | TaxEI | 0 | **done** | `v4_taxei_recovery_eval_s0.json` | 0.468 | 47 |
| 8 | TaxEI | 123 | **done** | `v4_taxei_recovery_eval_s123.json` | 0.617 | 47 |
| 9 | TaxEI | 1 | missing | — | — | — |
| 10 | TaxEI | 7 | missing | — | — | — |
| 11 | Random | 42 | **done** | `v4_random_recovery_eval.json` | 0.638 | 47 |
| 12 | Random | 0 | missing | — | — | — |
| 13 | Random | 123 | missing | — | — | — |
| 14 | Random | 1 | missing | — | — | — |
| 15 | Random | 7 | missing | — | — | — |

### 关键发现

- **完成 7/15**：Vanilla 3个 (42/0/123)，TaxEI 3个 (42/0/123)，Random 1个 (42)
- **缺失 8/15**：所有 condition 的 seed=1 和 seed=7 都缺；Random 额外缺 seed=0 和 seed=123
- `v4_taxei_recovery_eval_r2.json` 是 TaxEI seed=42 的重复运行（同模型、同结果 0.596），不算额外格子
- 所有文件的 eval seed 均为 42，training seed 体现在 checkpoint 路径中
- 所有文件 `total_episodes=47`，`inject=true`，`detection_rate=0.0`

---
