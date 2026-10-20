# ops check 34685 gpu util

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_34685_gpu_util_20260524T153424_result.json`
- **Structured JSON:** [`2c52840287fb2394e58b.json`](../../sessions/2c/2c52840287fb2394e58b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个进程全部正常运行。GPU 2/3 低利用率是 eval 特征，不是问题。

| GPU | 任务 | GPU-Util | 显存占用 | 温度 | 进程状态 | 运行时间 |
|-----|------|----------|----------|------|----------|----------|
| 0 | cutoff_45k_s1 (训练) | **81%** | 62203/97887 MiB | 71°C | Ssl, 正常 | 3h04m |
| 1 | cutoff_15k_s1 (训练) | **97%** | 62203/97887 MiB | 69°C | Ssl, 正常 | 3h39m |
| 2 | cutoff_25k_s1_eval | **2%** | 16211/97887 MiB | 38°C | Sl, 正常 | 42m |
| 3 | reverse_cutoff_s1_eval | **0%** | 16778/97887 MiB | 38°C | Sl, 正常 | 42m |

**判断：正常，无需干预。**

- GPU 2/3 是 eval 任务（`evaluate_safelibero.py`，50 rollouts），eval 本身是 CPU-bound 的仿真 + 间歇 GPU 推理，利用率低是正常特征。
- 日志确认两个 eval 都在正常推进：cutoff_25k 在 Task 8 的第 47/50 rollout，reverse_cutoff 在 Task 8 的第 37/50 rollout。
- GPU 0/1 训练任务利用率 81%/97%，完全正常。
- 注意实际 eval PID 是子进程（892653/892925），而非 wrapper bash 进程（892641/892913），两组都活着。

---
