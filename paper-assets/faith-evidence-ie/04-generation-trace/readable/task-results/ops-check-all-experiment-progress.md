# ops check all experiment progress

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-all-experiment-progress_20260515T230403_result.json`
- **Structured JSON:** [`893e6f5cd5cda99634fa.json`](../../sessions/89/893e6f5cd5cda99634fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度汇总

| # | 实验 | GPU | 状态 | 进度 | 估算剩余 |
|---|------|-----|------|------|----------|
| 1 | plan_001_flat_nli_seed44 | cuda:0 (19.2GB, 38%) | **训练完成，正在做最终 eval** | 507/507 steps (100%) | eval 进度未知（log 被截断） |
| 2 | reeval_flat_nli_s43 | cuda:1 (16.9GB, 86%) | **推理中** | 7/62 batches (11%) | ~54 min（~58s/batch） |
| 3 | plan_001_flat_nli_seed45 | cuda:2 (19.7GB, 94%) | **训练完成，正在做最终 eval** | 训练 507/507 done；eval 34/985 docs (3%) | eval ~60 min |
| 4 | eval_plan_012_dpo_1ep_fixed_r2 | cuda:3 (30.7GB, 88%) | **推理中** | 34/62 batches (55%) | ~53 min（~113s/batch） |

### 关键细节

**seed44 (cuda:0)** — 训练 507/507 完成，最终 loss=0.5736，epoch 2.96。进程仍存活，正在做训练结束后的 eval，GPU 利用率降到 38% 说明已从训练切到推理。

**seed45 (cuda:2)** — 训练 507/507 完成，最终 eval @ step 507 已出中间结果：**F1=0.4876, Evi-F1=0.7927, EDCR=0.6517**。当前正在跑 985 个 doc 的完整 eval（才到 3%）。

**reeval_s43 (cuda:1)** — 7 分钟前刚启动，11% 进度，每 batch ~58s。

**dpo_1ep_fixed_r2 (cuda:3)** — 过半，55% 进度，每 batch ~113s（比 reeval 慢一倍，因 DPO 模型生成更长）。注意 GPU 3 上有两个 python 进程（PID 261622 + 262080），占用 30.7GB。

### 预计完成时间线
- seed44 最终 eval：不确定（log 截断，需再查）
- seed45 最终 eval：~60 min（约 08:05 UTC）
- reeval_s43：~54 min（约 08:00 UTC）
- dpo_1ep_fixed_r2：~53 min（约 08:00 UTC）

---
