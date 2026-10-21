# ops status check ensure irt

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_status-check-ensure-irt_20260516T205255_result.json`
- **Structured JSON:** [`ac0828a3858379186cca.json`](../../sessions/ac/ac0828a3858379186cca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有进程正常运行，无需启动任何东西。

**状态汇总：**

| 任务 | 状态 | PID | GPU |
|------|------|-----|-----|
| Cross-family IRT (pooled_irt_all_scales) | 运行中 | 758619 | CPU only |
| Cross-family IRT (results_cross_family_irt) | 运行中 | 863568 | CPU only |
| d100 signals (MMLU, cuda:1) | 运行中 | 863173 | GPU 1 (562 MiB) |
| d100 eval (mmlu+gsm8k+arc+humaneval, cuda:5) | 运行中 | 831033 | GPU 5 (8304 MiB) |
| Fisher heatmap | 运行中 | 862089 + 8 workers | CPU only |

**GPU 占用：**
- GPU 0: 11933/24564 MiB (76%) — PID 825638
- GPU 1: 571/24564 MiB (19%) — d100 signals
- GPU 2: 7323/24564 MiB (62%) — PID 853489
- GPU 3: 7711/24564 MiB (62%) — PID 859365
- GPU 4: 6977/24564 MiB (62%) — PID 842929
- GPU 5: 8313/24564 MiB (80%) — d100 eval

Cross-family IRT 已在跑（两个实例），无需启动。

---
