# eval vanilla 50r check and launch

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_vanilla-50r-check-and-launch_20260521T174821_result.json`
- **Structured JSON:** [`8e61199db1e8f642266d.json`](../../sessions/8e/8e61199db1e8f642266d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

s1 和 s2 也在正常推进（T0 ~40/50），即将完成第一个 task。

## 汇报

### Checkpoint 可用性
| Seed | 47500_chkpt | 50000_chkpt (westd-34685) | 操作 |
|------|-------------|---------------------------|------|
| vanilla_s0 | 不存在 | ✓ 已有 | 直接使用 |
| vanilla_s1 | 不存在 | ✓ 已有 | 直接使用 |
| vanilla_s2 | 不存在 | ✗ 不存在 | 从 westd-10894 rsync（15GB，已完成）|

**注意：3 个 seed 都没有 47500_chkpt，使用 50000_chkpt 替代。**

### 3 个 Eval PID
| Eval | GPU | PID | Log |
|------|-----|-----|-----|
| vanilla_s0 | cuda:1 | 739035 | `/root/eval_logs/vanilla_s0_50000_50r.log` |
| vanilla_s1 | cuda:2 | 740428 | `/root/eval_logs/vanilla_s1_50000_50r.log` |
| vanilla_s2 | cuda:3 | 741283 | `/root/eval_logs/vanilla_s2_50000_50r.log` |

### 碰撞检测验证
- **s0 T0 已完成**: TSR=1.000, CAR=0.980 — 碰撞检测正常工作
- s1、s2 T0 进行中（~80%），正常推进中
- 碰撞指标以 CAR（Collision Avoidance Rate）形式在每个 task 完成时输出，不是 per-rollout 的 max_disp

---
