# ops cuda4 conflict resolution

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cuda4-conflict-resolution_20260515T033317_result.json`
- **Structured JSON:** [`f1a2d06d00ffef3c5889.json`](../../sessions/f1/f1a2d06d00ffef3c5889.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cuda:4 已清理完毕。

**结果汇总：**

| PID | 任务 | 状态 | 显存 |
|-----|------|------|------|
| 493617 | exp_008_instruct_05B_eval | 运行中 ✓ | 3540MiB |
| 494109 | exp_001_eval_05B_d000_s42_v2 | 运行中 ✓ | 3686MiB |
| 493813 | exp_001_sft_05B_d025_s123 | **已 kill** | — |

cuda:4 当前总占用 7240MiB / 24564MiB（29%），两个 eval 任务共存无压力。SFT 进程树（python + timeout + tmux session）已全部清理。

---
