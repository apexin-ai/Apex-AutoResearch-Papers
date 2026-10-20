# ops cuda0 check and queue experiment

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cuda0_check_and_queue_experiment_20260521T104029_result.json`
- **Structured JSON:** [`9e550ea1a88bc250ad94.json`](../../sessions/9e/9e550ea1a88bc250ad94.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**cuda:0 不可用。**

| GPU | 显存占用 | 利用率 | 状态 |
|-----|---------|--------|------|
| cuda:0 | 49175 / 97887 MiB | 0% | 被占用 |
| cuda:1 | 41191 / 97887 MiB | 100% | 训练中 |

**原因**：PID 693144 (`qwen7b_full_trace_seed456_v2`) 同时持有两张 GPU（`/dev/nvidia1` + `/dev/nvidia3`）。该进程是正在运行的训练任务（`train_sft.py --condition full_trace --seed 456 --gpu 0`），cuda:1 利用率 100%，不能 kill。

cuda:0 上 49175 MiB 的占用是该训练进程分配的显存（尽管 `--gpu 0` 指定了单卡，进程仍打开了两个 GPU 设备文件）。需等该训练结束后 cuda:0 才会释放。

---
