# code prep remaining scripts

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep_remaining_scripts_20260516T184939_result.json`
- **Structured JSON:** [`1e1e30643c46d9fb7dbd.json`](../../sessions/1e/1e1e30643c46d9fb7dbd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个脚本**已存在**且全部通过验证：

| 脚本 | bash -n | CUDA=-1 | WANDB=disabled | output→autodl-tmp |
|------|---------|---------|----------------|-------------------|
| `run_rho02_adaptive_tau09_seed42.sh` | ✓ | ✓ | ✓ | ✓ |
| `run_batch_adaptive_tau_rho06_seed42.sh` | ✓ | ✓ | ✓ | ✓ |
| `run_bs8_auto_nmin_seed42.sh` | ✓ | ✓ | ✓ | ✓ |

关于 `bs8_auto_nmin` 的 n_min=4：训练代码 `pretrain_weighted.py:331-332` 已有 auto 逻辑 `n_min = max(2, batch_size // 2)`，bs=8 时自动得到 4，无需显式指定。

脚本已就绪，GPU 释放后可直接 submit。

---
