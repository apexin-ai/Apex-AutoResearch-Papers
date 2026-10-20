# diagnose batch adaptive tau rho04

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_batch_adaptive_tau_rho04_20260516T234054_result.json`
- **Structured JSON:** [`9e475b15f13fb1903a09.json`](../../sessions/9e/9e475b15f13fb1903a09.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。

## 汇报

| 指标 | 值 |
|------|-----|
| eval_loss_holdout | 2.8725 |
| eval_ppl_holdout | **17.681** |
| 阈值 (fixed τ=0.8) | 17.653 |
| 判定 | **未通过** (17.681 > 17.653) |

**结论：negative。** Batch adaptive τ 在 ρ=0.4 seed=42 条件下 PPL = 17.681，略高于 fixed τ=0.8 的 17.653（差距 0.028）。Claim 3 无法升级。

差距极小（0.16%），说明 batch adaptive τ 的效果与 fixed τ 几乎持平，没有带来有意义的改善。adaptive 策略在 clean batch 上降低了 τ（从日志可见 τ_batch 常低于 0.8），但这并未转化为更好的 holdout 泛化。

---
