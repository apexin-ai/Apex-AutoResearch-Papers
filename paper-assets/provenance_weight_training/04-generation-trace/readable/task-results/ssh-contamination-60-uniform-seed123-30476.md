# ssh contamination 60 uniform seed123 30476

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_contamination_60_uniform_seed123_30476_20260517T235137_result.json`
- **Structured JSON:** [`b015f6f95e208fce2d0a.json`](../../sessions/b0/b015f6f95e208fce2d0a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练成功启动。

## 报告

| 项目 | 结果 |
|------|------|
| GPU 3 | RTX PRO 6000 Black, 41757MiB 占用, 95% GPU-Util |
| PID | 66327 (实际 python 进程) |
| weighting_method | **uniform** ✓ (log 确认 `weighting/b: 0.0`, `unweighted_loss == weighted_loss`) |
| max_steps | 6103 (200M tokens) |
| seed | 123 |
| 预计耗时 | ~3.7h (2.17s/it) |
| 无 --eval_data_path | ✓ |

Log 确认 `weighting_method: uniform`，且 `weighted_loss == unweighted_loss`（权重全为 1），baseline 对照组正常运行。

---
