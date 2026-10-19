# code plan 701 fallback k10cache

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_701-fallback-k10cache_20260517T145427_result.json`
- **Structured JSON:** [`f6d261de427751e7537c.json`](../../sessions/f6/f6d261de427751e7537c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常启动并运行中。

**状态汇总：**
- **服务器**: bjb1-32546, GPU cuda:4
- **数据**: K=10 cache, 14570 samples (object benchmark), obs_dim=960
- **模型**: MultiScaleCRM, 327,522 params, multi_scale=False (单阶段 fallback)
- **训练**: 13113 train / 1457 val, batch_size=512, 26 batches/epoch
- **进展**: 已到 Epoch 4/50, val_loss 持续下降 0.009415 → 0.008158
- **Loss 分解**: L2=0.0082, dir=0.3461, tri=0.0107, mag=0.0013

ACCG 在单阶段 960D obs_features 上可以正常训练，loss 在快速收敛。`CRMK1FromK10Dataset` 已修改为从合并 tensor 加载 + 每 epoch 随机从 K=10 中选一个样本作为 K=1 action（数据增强效果）。代码已同步修复到 bjb2-28827。

---
