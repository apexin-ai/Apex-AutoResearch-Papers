# monitor 17855 t15 progress

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_17855_t15_progress_20260523T005954_result.json`
- **Structured JSON:** [`04049a439db7335f8992.json`](../../sessions/04/04049a439db7335f8992.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 6 个进程存活。根据 gen 目录时间戳计算进度：

### T=15 实验（1.4B，~67 min/gen）

| 实验 | 当前 gen / 总 gen | 预估剩余 | 状态 |
|------|------------------|----------|------|
| t15_a060_s42_fp32 | **14/15**（最后一个，训练中） | **~25 min** | running |
| t15_a050_s42_fp32 | **14/15**（最后一个，训练中） | **~28 min** | running |
| t15_a045_s42_fp32 | **12/15**（训练中） | **~2.7 h** | running |

a060 和 a050 从 start_gen=4 恢复，都已进入最后一个 gen（gen_14），即将完成。a045 从 start_gen=2 恢复，还剩 gen_12（当前）+ gen_13 + gen_14 共 3 个 gen。

### T=10 实验（1.4B s43，~68 min/gen）

| 实验 | 当前 gen / 总 gen | 预估剩余 | 状态 |
|------|------------------|----------|------|
| t10_a075_s43_fp32 | **4/10**（训练中） | **~6.0 h** | running |
| t10_a060_s43_fp32 | **4/10**（训练中） | **~6.0 h** | running |
| t10_a045_s43_fp32 | **0/10**（刚启动 12 min） | **~10 h** | running |

---
