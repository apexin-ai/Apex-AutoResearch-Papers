# ops critical cutoff bug fix 34685

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_critical_cutoff_bug_fix_34685_20260525T035030_result.json`
- **Structured JSON:** [`9b70085206722a2b2828.json`](../../sessions/9b/9b70085206722a2b2828.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

| 项目 | 结果 |
|------|------|
| **cutoff_45k_s1 kill** | 成功 (PID 20913, force killed) |
| **cutoff_25k_s2 验证** | 通过，从 pretrained 从头训练，无 resume |
| **reverse_cutoff_s2 验证** | 通过，从 pretrained 从头训练，无 resume |
| **cutoff_45k_s1_v2 新实验** | PID=96645，westd-34685:cuda:0，已注册 RUNNING |
| **磁盘清理** | 释放 ~119GB（cutoff_15k_s1 中间 4 个 + cutoff_45k_s1 无效 4 个，各 15GB） |
| **磁盘状态** | 275G → 156G used，195G available (45%) |

---
