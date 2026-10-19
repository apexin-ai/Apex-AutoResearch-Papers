# monitor factorial step10 watch r1

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_factorial-step10-watch-r1_20260518T052805_result.json`
- **Structured JSON:** [`8e30e9ce5e9a77006725.json`](../../sessions/8e/8e30e9ce5e9a77006725.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the data. Here's the report:

```
FACTORIAL: step 7/15 (computing step 8, log last write 12:45 +0800)
  step 10 val: 未到达

  step 0 val (OOD):  success=2.2%,  pass@1=2.2%,  action_valid=37.8%
  step 1 train:      success=20.3%, pass@8=68.8%, action_valid=85.6%, kl=0.238,  entropy=0.359
  step 2 train:      success=6.3%,  pass@8=31.3%, action_valid=84.0%
  step 3 train:      success=5.5%,  pass@8=31.3%, action_valid=79.5%, kl=1.077,  entropy=0.567
  step 4 train:      success=3.1%,  pass@8=18.8%, action_valid=83.7%, kl=0.638,  entropy=0.617
  step 5 train:      success=15.6%, pass@8=62.5%, action_valid=79.9%, kl=0.735,  entropy=0.699
  step 5 val (OOD):  success=6.0%,  pass@1=6.0%,  action_valid=57.6%
  step 6 train:      success=25.8%, pass@8=81.3%, action_valid=81.5%, kl=0.789,  entropy=0.719
  step 7 train:      success=17.2%, pass@8=43.8%, action_valid=77.2%, kl=1.774,  entropy=0.621

  趋势：success 高方差（3%-26%），kl_loss 持续攀升（0.24→1.77），action_valid 下降（86%→77%）
  step 7→8 用时 ~56min，预计 step 8 完成 ~13:41 +0800
  进程：大概率存活（尾部有 step 8 rollout warnings）

GSWEEP_G080: step 1/15 (computing step 2, log last write 13:13 +0800)
  step 0 val:   success=9.4%, pass@1=9.4%, action_valid=79.7%
  step 1 train: success=0.0%, pass@8=0.0%, action_valid=80.3%, kl=0.044, entropy=0.341

  step 2、3 数据尚无。step 1 用时 ~46min，预计 step 2 完成 ~14:00 +0800
  进程：存活（13:13 仍有输出）
```

---
