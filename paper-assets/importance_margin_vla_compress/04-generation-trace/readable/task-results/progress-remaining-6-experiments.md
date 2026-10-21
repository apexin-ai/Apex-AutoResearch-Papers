# progress remaining 6 experiments

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_progress_remaining_6_experiments_20260528T080247_result.json`
- **Structured JSON:** [`a485f7c24990fda2f65a.json`](../../sessions/a4/a485f7c24990fda2f65a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| # | 实验 | 服务器 | 进度 | 累计 SR | 预估完成 (UTC) |
|---|------|--------|------|---------|---------------|
| 1 | Attn k=0.7 s45 | westd-41074 | **已完成** 10/10 | **53.8%** | ✅ 已结束 (EXIT_CODE=0) |
| 2 | Random k=0.85 s46 | westd-41074 | T7 ep30/50 (7.6/10) | 44.9% (T0-6) | ~16:38 UTC |
| 3 | L2norm k=0.75 s46 | westd-41074 | T8 完成，进入 T9 (9/10) | 71.3% (T0-8) | ~16:16 UTC |
| 4 | Attn k=0.85 s46 | westd-38929 | T7 ep30/50 (7.6/10) | 50.0% (T0-6) | ~16:37 UTC |

预估逻辑：各实验平均 ~15-17min/task，根据当前进度和已用时间外推。三个在跑的实验都预计在 **16:40 UTC 前完成**，距离 C002 截止线 (08:00 UTC 已过) 无关，但都在 12:00 UTC 论文截止前的数据可用。

---
