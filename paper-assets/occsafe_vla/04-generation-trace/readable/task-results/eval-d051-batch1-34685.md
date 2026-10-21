# eval d051 batch1 34685

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_d051_batch1_34685_20260526T073351_result.json`
- **Structured JSON:** [`a6dc10f65cb343916294.json`](../../sessions/a6/a6dc10f65cb343916294.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部确认。

## 结果

| 实验 | 状态 | GPU | Eval PID |
|------|------|-----|----------|
| detach_bn_v2_s0 | eval 已启动 | cuda:0 | 50552 |
| detach_bn_v2_s1 | eval 已启动 | cuda:1 | 50755 |
| detach_bn_v2_s2 | eval 已启动 | cuda:2 | 51018 |
| full_occ_bn_v2_s1 | **仍在训练** | cuda:3 | — |

日志路径：`~/runs/occsafe_vla/&lt;EXP>_eval.log`

**未启动**：full_occ_bn_v2_s1 的 50000 checkpoint 尚不存在，训练仍在 cuda:3 上运行（PID 7427），需后续训练完成后单独启动 eval。

---
