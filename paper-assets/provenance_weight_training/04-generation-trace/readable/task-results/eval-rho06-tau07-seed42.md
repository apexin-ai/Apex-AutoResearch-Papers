# eval rho06 tau07 seed42

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_rho06_tau07_seed42_20260520T030536_result.json`
- **Structured JSON:** [`b6d62d1133a7350803db.json`](../../sessions/b6/b6d62d1133a7350803db.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。`rho06_tau07_seed42` 全量 eval 结果：

**PPL 指标**
- Holdout: **17.53** (< 17.73 baseline → success)
- OpenWebText: **18.21**
- Wikipedia: **15.27**

**Downstream tasks**
| Task | acc_norm |
|------|---------|
| ARC-Easy | 0.6208 |
| ARC-Challenge | 0.3524 |
| HellaSwag | 0.4801 |
| PIQA | 0.6931 |
| Winogrande (acc) | 0.5785 |

Registry 已更新为 DONE/success。τ=0.7 在 ρ=0.6 下 holdout PPL 与 τ=0.8 hybrid (17.53) 持平，优于 τ=0.8 batch_adaptive (17.73)。

---
