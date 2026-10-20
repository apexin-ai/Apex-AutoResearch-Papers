# ops check training progress

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-training-progress_20260515T230245_result.json`
- **Structured JSON:** [`c7fbce7ecb5f925be9e9.json`](../../sessions/c7/c7fbce7ecb5f925be9e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度汇总

### GPU 状态
| GPU | 显存占用 | 利用率 | 任务 |
|-----|---------|--------|------|
| 0 | 19175/32607 MiB (59%) | 38% | seed44 训练 |
| 1 | 16925/32607 MiB (52%) | 88% | reeval s43 |
| 2 | 19745/32607 MiB (61%) | 40% | seed45 训练 |
| 3 | 30704/32607 MiB (94%) | 95% | DPO eval |

### 各实验状态

**1. plan_001_flat_nli_seed44** (cuda:0) — **训练完成 507/507 steps (100%)**
- 已完成 3 epochs，最后 loss=0.5736, mean_token_accuracy=0.857
- Epoch 2 eval_loss=0.753, eval_mean_token_accuracy=0.830
- 运行时间 1h24m，正在收尾（保存 checkpoint/eval）
- 无异常

**2. plan_001_flat_nli_seed45** (cuda:2) — **训练完成 507/507 steps (100%)**
- 已完成 3 epochs，最后 loss=0.5931, mean_token_accuracy=0.854
- Epoch 2 eval_loss=0.753, eval_mean_token_accuracy=0.830
- 运行时间 1h37m，正在收尾
- 无异常

**3. eval_plan_012_dpo_1ep_fixed_r2** (cuda:3) — **推理中 33/62 batches (53%)**
- 速度 ~113s/batch
- 预估剩余 **~55 分钟**
- 运行时间 1h04m
- 无异常

**4. reeval_flat_nli_s43** (cuda:1) — **推理中 5/62 batches (8%)**
- 刚启动 6 分钟，已正常产出
- 速度 ~57s/batch（比 DPO eval 快一倍，可能模型更小/生成更短）
- 预估剩余 **~54 分钟**
- 无异常

所有 4 个进程正常运行，无 OOM 或错误。两个训练即将结束（进入 final eval/save），两个 eval 大约还需 ~55 分钟。

---
