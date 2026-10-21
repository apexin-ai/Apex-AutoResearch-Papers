# submit batch adaptive tau rho04

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_batch_adaptive_tau_rho04_20260516T110057_result.json`
- **Structured JSON:** [`dbe00a88a56027a3dfc5.json`](../../sessions/db/dbe00a88a56027a3dfc5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**已提交 `batch_adaptive_tau_rho04_seed42`，训练正常运行中。**

| 项目 | 值 |
|------|-----|
| PID | 326274 (子进程 326280 占用 GPU) |
| GPU | cuda:2 (bus B8:00.0)，46514 MiB 已占用 |
| 当前 step | 13/6103，~2.22s/it |
| 预计完成 | ~3h45m（约 14:45 UTC） |
| WANDB | offline 模式 |
| 日志 | `/root/provenance_weight_training/output/logs/batch_adaptive_tau_rho04_seed42.log` |

batch-adaptive τ 已在工作：日志显示 `tau_batch` 在 0.5–0.8 间动态变化（如 0.69、0.56、0.50、0.80、0.65），符合 `clamp(α_eff + 0.3, 0.5, 0.8)` 的预期行为。

---
