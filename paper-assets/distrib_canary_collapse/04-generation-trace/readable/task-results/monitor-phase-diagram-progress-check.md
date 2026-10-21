# monitor phase diagram progress check

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_phase_diagram_progress_check_20260521T212017_result.json`
- **Structured JSON:** [`c52571e4c6a272da2393.json`](../../sessions/c5/c52571e4c6a272da2393.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/report_progress.md`。

**关键发现：**

| 实验 | 进度 | 预计完成 |
|------|------|---------|
| t25_a075_s42_fp32 | 21/25 (84%) | ~06:55 最先完成 |
| t25_a045_s42_fp32_v2 | 19/25 (76%) | ~07:45 |
| t15_a060_s43_fp32 | 7/15 (47%) | ~08:10 |
| t15_a045_s43_fp32 | 5/15 (33%) | ~08:55 |
| t20_a045_s43_fp32 | 10/20 (50%) | ~09:05 |
| t20_a060_s43_fp32_v2 | 5/20 (25%) | ~11:20 |
| t25_a050_s42_fp32_v2 | 5/25 (20%) | ~13:15 |
| **t25_a060_s42_fp32_v2 ★** | **5/25 (20%)** | **~13:15 最晚** |

- 8/8 GPU 全部活跃，无 OOM 或异常
- T=15 两个实验并非最先完成——它们启动较晚，反而是更早启动的 T=25 a075 和 a045 会先跑完
- ★关键格 t25_a060 进度最慢（20%），预计还需 ~8h

---
