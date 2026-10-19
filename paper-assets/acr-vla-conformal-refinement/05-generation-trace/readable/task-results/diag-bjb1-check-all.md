# diag bjb1 check all

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_bjb1-check-all_20260514T020843_result.json`
- **Structured JSON:** [`7828294705d69dcf0e3a.json`](../../sessions/78/7828294705d69dcf0e3a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

所有 4 个实验 **均在正常运行**，没有 hang。进程实际运行时间远短于用户预估的 12-14 小时（可能是之前有重启）。

---

### 1. crm-train-k5 (PID 139839 → 子进程 139850)
- **状态：🟢 正在运行**
- 实际运行时间：**26 分钟**（非 12 小时）
- 进度：**epoch 9/50**，每 epoch 752 batch，正常推进
- val_loss 在下降（epoch 8 达到 best: 0.011849）
- GPU 0：8002MiB / 24564MiB，9% 利用率
- 预计剩余：~2 小时完成全部 50 epochs

### 2. eval-acr-spatial-v2 (PID 117814)
- **状态：🟢 正在运行**
- 实际运行时间：**2 小时 25 分钟**
- 进度：**2/10 tasks 完成**
  - task 1: 40.0% (4/10)
  - task 2: 70.0% (7/10)
- GPU 1：1459MiB，20% 利用率（+ GPU 0 上 3714MiB 共享显存）
- 预计剩余：每 task ~70 分钟，还需 **~9 小时**

### 3. eval-reconvla-spatial-v3 (PID 118108)
- **状态：🟢 正在运行**
- 实际运行时间：**2 小时 25 分钟**
- 进度：**~2.5/10 tasks 完成**（task 3 进行到 rollout 5/10）
  - task 1: 60.0% (6/10)
  - task 2: 100.0% (10/10)
  - task 3: 进行中 (0/5 so far)
- GPU 2：1423MiB，19% 利用率
- 预计剩余：~**7-8 小时**

### 4. crm-train-a4-scalar-unc (PID 121984)
- **状态：🟢 即将完成**
- 实际运行时间：**2 小时 23 分钟**
- 进度：**epoch 48/50**，batch 100/752
- val_loss 已收敛至 0.008399
- GPU 3：532MiB，9% 利用率
- 预计剩余：**~10 分钟**

---

### 关键发现

1. **没有进程 hang**，全部在正常产出日志和使用 GPU
2. 进程实际 etime 是 **0.5-2.5 小时**，不是 12-14 小时——可能之前的进程被 kill 后重启了
3. **crm-train-k5 比预期慢**的原因是 50 epochs × 752 batches，数据量大，5-15 分钟的预期不现实
4. **两个 eval 实验会跑很久**（~10 小时），因为每个 task 的 rollout 涉及实际 robosuite 仿真，每次 rollout 最多 300 步
5. **scalar_unc 训练马上完成**，约 10 分钟内结束

---
