# eval detach bn v2 3seeds

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_detach_bn_v2_3seeds_20260526T073800_result.json`
- **Structured JSON:** [`fef562cf9e321f9eead9.json`](../../sessions/fe/fef562cf9e321f9eead9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### 训练验证（全部通过）

| exp_id | final step | occ_loss | action_loss | checkpoint | EXIT_CODE |
|--------|-----------|----------|-------------|------------|-----------|
| detach_bn_v2_s0 | 50005 | 0.0095 | 0.0449 | ✅ ~14.4GB | 0 |
| detach_bn_v2_s1 | 50005 | 0.0089 | 0.0513 | ✅ ~14.4GB | 0 |
| detach_bn_v2_s2 | 50005 | 0.0094 | 0.0481 | ✅ ~14.4GB | 0 |

### Eval 提交（全部成功）

| eval_id | server | GPU | PID | log |
|---------|--------|-----|-----|-----|
| detach_bn_v2_s0_eval | westd-34685 | cuda:0 | 69726 | `~/runs/occsafe_vla/detach_bn_v2_s0_eval.log` |
| detach_bn_v2_s1_eval | westd-34685 | cuda:1 | 70093 | `~/runs/occsafe_vla/detach_bn_v2_s1_eval.log` |
| detach_bn_v2_s2_eval | westd-34685 | cuda:2 | 70490 | `~/runs/occsafe_vla/detach_bn_v2_s2_eval.log` |

无异常。3 路 50-rollout SafeLIBERO eval 已在 westd-34685 cuda:0/1/2 并行运行。

---
