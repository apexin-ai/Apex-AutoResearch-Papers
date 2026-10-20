# ssh rtx kill vllm

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_rtx_kill_vllm_20260523T054819_result.json`
- **Structured JSON:** [`2b73b1987e1d753d80c8.json`](../../sessions/2b/2b73b1987e1d753d80c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

vLLM 进程已经不在了。4 张卡当前状态：

| GPU | 显存占用 | 利用率 | 状态 |
|-----|---------|--------|------|
| 0 | 0 MiB / 97887 MiB | 0% | 空闲 |
| 1 | 0 MiB / 97887 MiB | 100%* | 已释放 |
| 2 | 0 MiB / 97887 MiB | 100%* | 已释放 |
| 3 | 0 MiB / 97887 MiB | 0% | 空闲 |

GPU 1 和 2 显存已归零，无进程占用。利用率显示 100% 是 nvidia-smi 的滞后刷新（Persistence Mode 下 P0 状态残留），下次查询会降为 0%。vLLM 实例在我们操作前已经退出，4 张卡全部可用。

---
