# analysis cutoff 45k s2 v2

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cutoff_45k_s2_v2_20260526T075923_result.json`
- **Structured JSON:** [`c16df32adacc588c752a.json`](../../sessions/c1/c16df32adacc588c752a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完成。汇总如下：

---

## cutoff_45k_s2_v2 训练结果

**状态**: 正常完成，50005/50005 steps，EXIT_CODE=0

**最终指标** (step 50000):
| Metric | Value |
|--------|-------|
| action_loss | 0.0703 |
| occ_loss | 0.0080 |
| depth_loss | 0.0000 |
| 训练时长 | ~14.3h |

**Checkpoint**: `/root/autodl-tmp/checkpoints/cutoff_45k_s2_v2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--cutoff_45k_s2_v2--50000_chkpt`

**W&B**: 未启用，日志中无 wandb 记录。

---

### cutoff_45k 系列对比

| 实验 | Status | action_loss | occ_loss | Eval TSR | Eval CAR |
|------|--------|-------------|----------|----------|----------|
| cutoff_45k_s0 | DONE/success | — | — | 0.896 | 0.764 |
| cutoff_45k_s1 | killed | — | — | — | — |
| cutoff_45k_s1_v2 | failed | — | — | — | — |
| cutoff_45k_s1_v3 | failed | — | — | — | — |
| **cutoff_45k_s2_v2** | **DONE/success** | **0.0703** | **0.0080** | **待 eval** | **待 eval** |

**s1 全部失败**，无法做完整 3-seed 对比。目前只有 s0 和 s2 两个 seed 成功训练完成。

### 与 baseline 对比（训练 loss）

| 实验 | action_loss | occ_loss |
|------|-------------|----------|
| mvp_occ_s0 (Full OCC BN) | — | — |
| full_occ_retrain_s0 | 0.0417 | 0.0104 |
| cutoff_45k_s2_v2 | 0.0703 | 0.0080 |

cutoff_45k_s2_v2 的 action_loss (0.0703) 明显高于 full_occ_retrain_s0 (0.0417)，但 occ_loss (0.008) 略低。这与 cutoff 的设计预期一致——45k step 后切断 OCC 梯度，action_loss 没有 OCC 辅助信号的持续帮助，收敛稍差。

### 需要启动 eval

是，cutoff_45k_s2_v2 训练完成，需要启动 eval 以获取 TSR/CAR 指标。

---
