# submit hybrid westd41312

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_hybrid_westd41312_20260516T112525_result.json`
- **Structured JSON:** [`ff3f17e70b263fe364cf.json`](../../sessions/ff/ff3f17e70b263fe364cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验已注册并运行。汇总：

| 实验 | PID | GPU | 显存占用 | 利用率 | 速度 | 预计完成 |
|------|-----|-----|---------|--------|------|---------|
| hybrid_rho04_seed42 | 3656 | cuda:2 | 46.5 GB / 95.6 GB | 100% | ~2.4 s/it | ~4h (6103 steps) |
| hybrid_rho06_seed42 | 3727 | cuda:3 | 46.5 GB / 95.6 GB | 100% | ~2.3 s/it | ~3h50m (6103 steps) |

脚本修复：两个脚本均补上了 `CUDA_VISIBLE_DEVICES`（rho04→2, rho06→3）。

日志路径：
- `/root/provenance_weight_training/output/logs/hybrid_rho04_seed42.log`
- `/root/provenance_weight_training/output/logs/hybrid_rho06_seed42.log`

注意：GPU 0 和 1 也在满载（可能是其他实验），当前提交的两个实验在 GPU 2/3 上互不干扰。

---
