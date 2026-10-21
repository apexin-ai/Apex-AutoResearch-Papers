# ops check eval s2 ckpt2500

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-eval-s2-ckpt2500_20260525T144459_result.json`
- **Structured JSON:** [`8befca1615df959fafef.json`](../../sessions/8b/8befca1615df959fafef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

**exp-003-s2-eval-ckpt2500 结果：**

| 指标 | 值 |
|------|-----|
| ToF | 0.0663 |
| NoF | 0.9669 |
| SYCONScore | **0.1241** |
| n_total | 362 |
| 耗时 | 4896s |

**对比参考：** seed 1 ckpt-3000 SYCONScore=0.095 → seed 2 ckpt-2500 为 0.1241，略高但同一量级，符合 R3-only GRPO 的低 SYCONScore 预期。

**ckpt-3000 eval：** 未在输出中找到。原始 spec 显示 ckpt2500+ckpt3000 chained，但进程只完成了 ckpt-2500 就退出了。如果需要 ckpt-3000 eval 需单独重跑。

**日志路径：** `/root/contrastive_entrain_calib/results/exp003s2_d027_eval/`

---
