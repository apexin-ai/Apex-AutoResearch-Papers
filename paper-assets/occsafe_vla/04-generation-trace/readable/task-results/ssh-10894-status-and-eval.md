# ssh 10894 status and eval

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_10894_status_and_eval_20260526T033748_result.json`
- **Structured JSON:** [`23928f900d9cdff8b1f1.json`](../../sessions/23/23928f900d9cdff8b1f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Director 的报告有误——**4 张 GPU 全部在跑，利用率 89-99%**，没有实验完成或失败。

## 10894 状态

| 实验 | 训练状态 | 当前 step | 进度 | 50K ckpt | eval 状态 | GPU |
|------|---------|----------|------|----------|----------|-----|
| cutoff_45k_s2_v2 | **训练中** | 35302/50005 | 71% | 无 | — | cuda:0 (99%) |
| mvp_occ_s3_v2 | **训练中** | 24095/50005 | 48% | 无 | — | cuda:1 (99%) |
| full_occ_ln_s3_v2 | **训练中** | 24008/50005 | 48% | 无 | — | cuda:2 (89%) |
| ablation_occ_detach_s3_v2 | **训练中** | 23955/50005 | 48% | 无 | — | cuda:3 (98%) |

**关键指标（最新 log）**：
- cutoff_45k_s2_v2 @ step 35300: occ_loss=0.0086, action_loss=0.0967
- full_occ_ln_s3_v2 @ step 24000: occ_loss=0.0109, action_loss=0.0952
- ablation_occ_detach_s3_v2 @ step 23900: occ_loss=0.0109, action_loss=0.0903

**ETA 预估**：
- cutoff_45k_s2_v2: ~4h 剩余（~1.05 it/s）
- 其余 3 个: ~7h 剩余（~1.06 it/s）

**空闲 GPU**: 无。所有 4 张 GPU 满载运行中。不启动 eval。

---
