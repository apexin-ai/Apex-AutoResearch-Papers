# diagnose exp029 real crash

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp029_real_crash_20260516T191610_result.json`
- **Structured JSON:** [`c3cbe804401de9875003.json`](../../sessions/c3/c3cbe804401de9875003.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**崩溃原因**: **CUDA OOM (显存不足)**

`loss.backward()` 阶段尝试分配 9.27 GiB 失败。GPU 0 总共 94.97 GiB，本进程已用 55.41 GiB，另一个进程 (PID 895286/895287) 占用 35.66 GiB，仅剩 3.87 GiB 空闲。

错误发生在 `dp_actor.py:468` → `update_policy` → `loss.backward()`，即 actor 梯度计算阶段。

**最后完成的 step**: **Step 1**（rollout + old_log_prob + ref + advantage 全部完成，update_actor 进行到 backward 时 OOM）

关键指标快照（step 1 训练数据）：
- train/AlfworldSG/success: 17.97%
- train/AlfworldSG/pass@8: 56.25%
- batch_size: 128, num_mini_batches: 4
- response_length/mean: 12689

**Checkpoint**: 无。`/root/autodl-tmp/checkpoints/exp029` 目录只有 `train_restart.log`，没有模型文件。

**GPU 当前状态**: 两块 GPU 各占用 ~38 GiB（残留显存未释放）。

**根因**: 共享 GPU 上另一进程占 35.66 GiB 导致本项目 backward 时显存不够。或者 batch_size=128 + response_length ~12K tokens + 4 mini-batches 在 backward 阶段的激活梯度超出了单 GPU 剩余容量。

---
