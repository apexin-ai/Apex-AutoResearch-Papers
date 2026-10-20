# infra fix batchsize16 nmin

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_fix_batchsize16_nmin_20260516T025533_result.json`
- **Structured JSON:** [`e27fbd251a3bb65e5694.json`](../../sessions/e2/e27fbd251a3bb65e5694.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。修改摘要：

- `--n_min 2` → `--n_min 8`
- 注释更新为 `n_min=8 (coupling rule: floor(B/2))`
- `bash -n` 语法检查通过
- 其他参数未变：batch_size=16, grad_accum=1, tau=0.8, seed=42, weighting_method=adaptive, --gradient_checkpointing 均保持原样

---
