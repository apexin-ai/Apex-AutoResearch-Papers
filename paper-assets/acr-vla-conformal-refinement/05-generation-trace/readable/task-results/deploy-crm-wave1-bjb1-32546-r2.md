# deploy crm wave1 bjb1 32546 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_crm-wave1-bjb1-32546-r2_20260525T101908_result.json`
- **Structured JSON:** [`c4b53d7972298a43afd4.json`](../../sessions/c4/c4b53d7972298a43afd4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

发现关键冲突：GPU 0/1/2 上已经在跑前 3 个实验（goal-s43、goal-s44、object-s42），用的就是 crm_smolvla_3suite_v1 checkpoint，已运行约 1 分 40 秒：

```
PID 93006 → goal seed43   (GPU 0, etime 01:46)
PID 93268 → goal seed44   (GPU 1, etime 01:44)
PID 93531 → object seed42 (GPU 2, etime 01:41)
```

但这些进程是裸 python 启动的，**不是通过 submit_training_job 注册的**，所以不在 training registry 里、不能用 check_training_status 追踪。

两种处理方案，需要你确认：

**A. 保留现有 3 个 + 只提交剩余 3 个（object-s43、object-s44、spatial-s48 到 GPU 3/4/5）**
- 优点：不浪费已跑 1 分 40 秒的进度
- 缺点：前 3 个不在 registry 里，状态无法用工具追踪

**B. 杀掉现有 3 个 + 用 submit_training_job 重新提交全部 6 个**
- 优点：所有 6 个实验都在 registry 里，统一管理
- 缺点：丢失 ~2 分钟进度（每个 rollout 通常更长，损失很小）

倾向 **B**（任务明确要求"必须用 submit_training_job"），但要不要 kill 现有进程请你拍板。

---
