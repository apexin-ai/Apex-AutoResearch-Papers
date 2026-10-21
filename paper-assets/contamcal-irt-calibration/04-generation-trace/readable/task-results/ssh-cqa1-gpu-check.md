# ssh cqa1 gpu check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_cqa1-gpu-check_20260519T000021_result.json`
- **Structured JSON:** [`a1096516160227635df9.json`](../../sessions/a1/a1096516160227635df9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 信息

| 项目 | 值 |
|------|-----|
| GPU 数量 | **1 张** |
| 型号 | NVIDIA GeForce RTX 4090 D |
| 显存 | 24564 MiB（总），已用 22928 MiB |
| CUDA | 13.0 |
| Driver | 580.76.05 |

当前 GPU 上有 2 个 Python 进程：PID 161500（6106 MiB）和 PID 170366（16808 MiB）。

## Eval 进程状态

PID 160404 **存活**，是 `run_eval_mmlu_arc_original.sh` 的启动 shell（05:51 启动）。实际执行脚本的子进程是 PID 160406（`bash /root/contamcal-irt-calibration/exp001/run_eval_mmlu_arc_original.sh`）。GPU 上的两个 Python 进程（161500、170366）应为该 eval 脚本产生的评估任务。

---
