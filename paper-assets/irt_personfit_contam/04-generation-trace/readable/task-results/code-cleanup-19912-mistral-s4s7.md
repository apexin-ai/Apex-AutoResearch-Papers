# code cleanup 19912 mistral s4s7

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cleanup-19912-mistral-s4s7_20260521T134007_result.json`
- **Structured JSON:** [`283e5594a2faeea64adf.json`](../../sessions/28/283e5594a2faeea64adf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 产出汇总

| 项目 | 结果 |
|------|------|
| **Kill 冗余进程** | 全部清除，GPUs 0-2 已释放至 0 MiB |
| **Mistral 代码** | `/root/autodl-tmp/ctrl_contam_mistral/train.py` 已存在，SEED_MAP 包含 clean_s4-s7 |
| **4 个训练状态** | 全部启动成功 |

| GPU | Condition | PID | 显存 | 状态 |
|-----|-----------|-----|------|------|
| 0 | clean_s5 | 36082 | 8369 MiB | 45/939 steps, ~1.13s/it |
| 1 | clean_s6 | 36162 | 8283 MiB | 运行中 |
| 2 | clean_s7 | 36239 | 8561 MiB | 运行中 |
| 3 | clean_s4 | (已运行) | 9339 MiB | 136/939 steps, ~1.09s/it |

**预计训练时长**: 939 steps × ~1.15s/step ≈ **18 分钟/任务**。clean_s4 已跑了 ~3 分钟，s5-s7 刚启动，全部完成约需 **15-18 分钟**。

---
