# monitor pi05 quicktest and p90

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_pi05-quicktest-and-p90_20260521T050016_result.json`
- **Structured JSON:** [`00ae5e3a8a34f3fda3e7.json`](../../sessions/00/00ae5e3a8a34f3fda3e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

9/10 tasks completed. Here's the summary:

---

## π0.5 quicktest
- PID 831620: **ALIVE**
- 运行时间: 20m21s
- 进度: **1/10 tasks** 完成
- Per-task SR:
  - `alphabet_soup` → **0% (0/5)**
- Overall SR: 尚未生成 JSON，仍在跑第 2 个 task

## P90-seed44
- PID 975409: **ALIVE**
- 运行时间: 1h57m38s
- 进度: **9/10 tasks** 完成，最后 1 个 task 进行中
- Per-task SR:

| Task | SR |
|------|----|
| black_bowl between plate & ramekin → plate | 80% (8/10) |
| black_bowl next to ramekin → plate | **100% (10/10)** |
| black_bowl from table center → plate | 0% (0/10) |
| black_bowl on cookie box → plate | 40% (4/10) |
| black_bowl in top drawer → plate | 10% (1/10) |
| black_bowl on ramekin → plate | 0% (0/10) |
| black_bowl next to cookie box → plate | **90% (9/10)** |
| black_bowl on stove → plate | 0% (0/10) |
| black_bowl next to plate → plate | 40% (4/10) |

- 9-task 中间 SR: **36/90 = 40.0%**
- 相比上次检查 (45.7% at 7/10) 有所下降，task 8 (stove) 和 task 9 (next to plate) 拖低了整体

---
