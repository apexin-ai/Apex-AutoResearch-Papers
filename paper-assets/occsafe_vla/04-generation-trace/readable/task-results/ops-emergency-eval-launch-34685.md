# ops emergency eval launch 34685

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_emergency-eval-launch-34685_20260528T064224_result.json`
- **Structured JSON:** [`0e893c01602555c554bf.json`](../../sessions/0e/0e893c01602555c554bf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Eval 已在运行，无需干预。**

状态汇总：

| 项目 | 状态 |
|------|------|
| 轮询脚本 | PID 69355/69356 正常运行，已在 14:40 触发 eval |
| 50000_chkpt | 两个都存在且完整 |
| 训练 PID 56474/56822 | 已自然退出（进程列表中不存在） |
| **full_occ_ln_v2_s3 eval** | PID 70951，T0 进度 40% (20/50 rollouts)，~5s/rollout |
| **detach_ln_v2_s3 eval** | PID 70950，T0 进度 42% (21/50 rollouts)，~4.7s/rollout |

GPU 使用：
- GPU-e566d524: detach_ln_v2_s2 训练 (62GB) + 两个 eval (各 16GB)
- GPU-eebe2f28: full_occ_bn_v2_s2 训练 (62GB)

**预估 eval 完成时间**：10 个 task × 50 rollouts × ~5s = ~42 分钟。启动于 ~06:40 UTC，预计 ~07:22 UTC 完成，远在 12:00 UTC 截止前。

---
