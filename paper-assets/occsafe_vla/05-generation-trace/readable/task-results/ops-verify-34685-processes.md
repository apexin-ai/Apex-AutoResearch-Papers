# ops verify 34685 processes

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify_34685_processes_20260525T075053_result.json`
- **Structured JSON:** [`21fd0ccd984c447dcfd2.json`](../../sessions/21/21fd0ccd984c447dcfd2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**全部 4 个实验均存活，GPU 满载运行。**

| 实验 | PID | GPU | 状态 | 运行时间 | GPU利用率 | 显存占用 |
|------|-----|-----|------|----------|-----------|----------|
| cutoff_25k_s2_v3 | 11510 | cuda:0 | **存活** (Ssl) | 3h08m | 99% | 62203/97887 MiB |
| reverse_cutoff_s2_v3 | 8347 | cuda:1 | **存活** (Rsl) | 3h11m | 99% | 62203/97887 MiB |
| cutoff_45k_s1_v3 | 2112 | cuda:2 | **存活** (S) | 3h17m | 98% | 62779/97887 MiB |
| cutoff_15k_s2_v2 | 2475 | cuda:3 | **存活** (S) | 3h17m | 99% | 62203/97887 MiB |

`get_project_resource_usage` 显示 cuda:0 和 cuda:1 空闲是误报——实际 4 张 GPU 全部 98-99% 利用率，显存各占 ~62GB/98GB。Registry 无需更新。

---
