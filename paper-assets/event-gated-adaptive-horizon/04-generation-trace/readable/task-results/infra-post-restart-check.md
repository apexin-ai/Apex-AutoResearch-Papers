# infra post restart check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_post-restart-check_20260517T013552_result.json`
- **Structured JSON:** [`5db278b6d18564d18537.json`](../../sessions/5d/5db278b6d18564d18537.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

| 实验 | 状态 | 最后 step | 目标 step | 进度 | GPU |
|------|------|-----------|-----------|------|-----|
| **exp_019a_v2_pickcube_baseline** (PID 629444) | 存活 | 65,483 | 200,000 | 32.7% | cuda:1, 4152 MiB |
| **exp_008d_civo_trigger_s3** (PID 635744) | 存活 | 48,000 | 105,000 | 45.7% | cuda:0, 3259 MiB |

**GPU 状态：**
- GPU 0 (RTX PRO 6000): 3946 MiB / 97887 MiB, 14% util, 38°C
- GPU 1 (RTX PRO 6000): 4161 MiB / 97887 MiB, 17% util, 45°C

两个实验均在服务器重启后正常存活，无异常。

---
