# eval occ s2 50r

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_occ-s2-50r_20260521T145118_result.json`
- **Structured JSON:** [`5ac3d0e343cbc211901f.json`](../../sessions/5a/5ac3d0e343cbc211901f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 正常运行，cuda:2 占用 16.8GB。

**状态汇总：**
- **PID**: 491663
- **配置**: occ_s2 47500_chkpt, libero_spatial, 50 rollouts/task, cuda:2
- **日志**: `/root/runs/occsafe_vla/eval_occ_s2_50r.log`
- **结果输出**: `/root/autodl-tmp/checkpoints/occ_s2/eval_47500_50r.json`
- **预计耗时**: ~90 分钟（20 rollouts 用了 35 分钟，50 rollouts 约 2.5x）

之前 20-rollout eval (50000_chkpt) 结果作参考：TSR=0.850, CAR=0.730。

需要我定时轮询进度吗？

---
