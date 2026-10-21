# ops urgent 17855 status check

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent-17855-status-check_20260523T123720_result.json`
- **Structured JSON:** [`7ea0be2371fa8a33da71.json`](../../sessions/7e/7ea0be2371fa8a33da71.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**westd-17855 在线，6 个实验全部存活。**

| GPU | 实验 | PID | 运行时间 | 显存占用 | GPU利用率 |
|-----|------|-----|---------|---------|----------|
| cuda:0 | t15_a060_s43 | 749427 | 9h51m | 31135 MiB | 88% |
| cuda:1 | t15_a050_s43 | 750075 | 9h48m | 27725 MiB | 88% |
| cuda:2 | t10_a050_s44 | 781724 | 3h31m | 27725 MiB | 100% |
| cuda:3 | t10_a060_s44 | 780907 | 3h36m | 27725 MiB | 99% |
| cuda:4 | t10_a045_s44 | 796624 | 5m08s | 11245 MiB | 89% |
| cuda:5 | t15_a045_s43 | 762806 | 7h41m | 27725 MiB | 98% |

所有 GPU 满负荷运行，无需标记 kill。

---
