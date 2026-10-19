# ssh check bjb2 40593 pid388460

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-bjb2-40593-pid388460_20260517T112920_result.json`
- **Structured JSON:** [`6724bc9d8d5c4aeaa6e4.json`](../../sessions/67/6724bc9d8d5c4aeaa6e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：保留，进程正常运行中。**

证据：
- **PID 388460** 存活，运行 1h33m，RSS ~10GB
- **日志** `/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed47.log`（17 行）
- **最后一行有 rollout 输出**：
  ```
  pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 5/10, success so far: 0/5
  ```
  第一个 task 已完成 5/10 rollouts，正在继续推进。
- **日志最后修改** 19:16（约 14 分钟前），robosuite 每个 rollout 最多 300 步，单个 rollout 耗时数分钟属正常
- **GPU**：RTX 4090D，12% util，5628MiB 占用，PID 388460 在使用 GPU。eval 模式下 GPU 利用率低是正常的（大部分时间在 CPU 端跑仿真）

Reviewer 之前检查时可能只看到初始化阶段（16 行无 rollout），但现在第 17 行已有 rollout 进展。进程未挂死。

---
