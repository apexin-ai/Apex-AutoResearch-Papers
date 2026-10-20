# ops contamination60 status check

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_contamination60_status_check_20260516T005550_result.json`
- **Structured JSON:** [`d6450b25aebff80276c0.json`](../../sessions/d6/d6450b25aebff80276c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验**全部仍在运行**，未完成。

## 当前状态

| 实验 | PID | 状态 | 进度 | step | 已运行 | 预计剩余 |
|------|-----|------|------|------|--------|----------|
| contamination_60_seed42_r2 (adaptive) | 257977 | RUNNING | 78% | 4747/6103 | 3h02m | ~52min |
| contamination_60_uniform_seed42 | 250074 | RUNNING | 97.6% | 5957/6103 | 3h30m | ~5min |
| contamination_60_ess_only_seed42 | 265012 | RUNNING | 38.6% | 2358/6103 | 1h26m | ~2h12m |
| contamination_60_grid_b0_5_seed42 | 255781 | RUNNING | 85.4% | 5215/6103 | 3h07m | ~31min |

## GPU 状态
全部 4 卡在用，利用率 94-98%，显存 ~46.5GB/97.8GB。

## 结论
- **uniform** 最快完成，约 5 分钟后
- **grid_b0_5** 约 31 分钟后
- **seed42_r2 (adaptive)** 约 52 分钟后
- **ess_only** 启动最晚，约 2h12m 后完成

Post-hoc eval 需要等训练完成。uniform 即将完成，建议等全部跑完后统一做 eval，或者 uniform 完成后先单独跑它的 eval。

---
