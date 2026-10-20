# ops status check westd

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_status-check-westd_20260514T212959_result.json`
- **Structured JSON:** [`b047a7fa97091141e9c9.json`](../../sessions/b0/b047a7fa97091141e9c9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 3 个进程存活：

| 任务 | PID | 运行时长 | 状态 |
|------|-----|---------|------|
| alpha_sweep_a000_s42 (α=0.0, cuda:0) | 46716 | **2h 28m 56s** | 运行中 |
| alpha_sweep_a025_s42_v3 (α=0.25, cuda:1) — wrapper | 53069 | **26m 28s** | 运行中 |
| alpha_sweep_a025_s42_v3 (α=0.25, cuda:1) — python | 53074 | **26m 28s** | 运行中 |

GPU 利用率：

| GPU | 利用率 | 显存占用 |
|-----|--------|---------|
| GPU 0 | 43% | 14,391 / 97,887 MiB |
| GPU 1 | 68% | 12,753 / 97,887 MiB |

两个实验均正常运行，GPU 都在活跃计算。α=0.0 已跑约 2.5 小时，α=0.25 刚启动约半小时。

---
