# check running experiments

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_running-experiments_20260514T143237_result.json`
- **Structured JSON:** [`70892d6250f288e249c3.json`](../../sessions/70/70892d6250f288e249c3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

状态报告已写入 `artifacts/running_experiments_check.md`。

**汇总：**

| 实验 | 进程 | 进度 | 备注 |
|------|------|------|------|
| math-200-fixed | 存活 (PID 295420) | 29/200 (14.5%) | 正常推理中，通过 vLLM server port 8000 |
| alfworld-cf-full | 存活 (PID 290564) | 45/140 (32%) | **全部 FAIL**（达 50 步上限），0 SUCCESS |

两个需要关注的问题：
1. **alfworld 成功率为 0%** — 45 个完成的 episode 全部失败，可能需要提前终止排查原因
2. **3 个残留 dryrun 进程**仍在运行，占用内存资源

---
