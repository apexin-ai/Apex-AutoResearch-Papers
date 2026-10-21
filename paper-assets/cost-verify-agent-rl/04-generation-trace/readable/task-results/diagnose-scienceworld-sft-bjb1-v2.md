# diagnose scienceworld sft bjb1 v2

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_scienceworld_sft_bjb1_v2_20260525T015705_result.json`
- **Structured JSON:** [`21ca118330884bdc94ea.json`](../../sessions/21/21ca118330884bdc94ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**scienceworld_sft_bjb1_v2 训练成功完成。**

| 指标 | 值 |
|------|-----|
| 总步数 | 450/450 (2 epochs) |
| Train loss | 0.5945 → 0.0587 |
| Eval loss | 0.0725 (step 448) |
| Token accuracy | 98.18% (eval) / 98.28% (train) |
| Checkpoints | 112, 224, 336, 448, 450 + final |
| Final 模型 | `/root/autodl-tmp/checkpoints/scienceworld_sft_bjb1/final/` (3.4GB) |

Eval loss 在 epoch 1.5 后基本收敛（0.0728→0.0725），无过拟合。

**GPU cuda:0 已完全释放**（0% 利用率，0 MiB 显存），可以启动 Cell B seed 100。

Registry 已更新为 DONE/success，报告已注册为 artifact。

---
