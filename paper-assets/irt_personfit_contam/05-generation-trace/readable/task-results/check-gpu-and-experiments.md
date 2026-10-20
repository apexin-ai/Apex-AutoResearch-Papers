# check gpu and experiments

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gpu-and-experiments_20260524T115421_result.json`
- **Structured JSON:** [`25441692878bc0f05347.json`](../../sessions/25/25441692878bc0f05347.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 检查结果

### GPU 状态
4× NVIDIA RTX PRO 6000 Blackwell (各 96GB)，**全部空闲**，显存 0 MiB，利用率 0%。

### 3 个实验状态：全部已正常完成

无运行进程、无 GPU 占用。三个实验均已产出 checkpoint 和 results：

| 实验 | 对应目录名 | Checkpoint | Results | 完成时间 |
|------|-----------|------------|---------|----------|
| exp-llama-15pct-s1-pilot | `contam_15` | `checkpoints/llama/contam_15/` (May 23 23:26) | `contam_15_results.json` (May 23 23:55) | ~May 23 23:55 |
| exp-llama-25pct-s3 | `contam_25_s3` | `checkpoints/llama/contam_25_s3/` (May 23 21:13) | `contam_25_s3_results.json` (May 24 00:01) | ~May 24 00:01 |
| exp-llama-5pct-s3 | `contam_5_s3` | `checkpoints/llama/contam_5_s3/` (May 23 21:14) | `contam_5_s3_results.json` (May 24 00:00) | ~May 24 00:00 |

### 部分结果速览

| Condition | theta_mle | lz_star |
|-----------|-----------|---------|
| contam_5_s3 | -0.428 | -1.952 |
| contam_15 | -0.315 | -4.659 |
| contam_25_s3 | -0.246 | -3.197 |

另有 `contam_5_full_analysis.json`（May 24 12:16）包含 accuracy 分析：overall=0.638, seen=0.801, unseen=0.629。

---
