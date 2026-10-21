# health object experiments

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_health_object-experiments_20260515T100306_result.json`
- **Structured JSON:** [`256e9bfa9a4486b11dbb.json`](../../sessions/25/256e9bfa9a4486b11dbb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

6 个 registry 全部更新完毕。

---

## 总结

**全部 6 个进程存活**，无卡住或死掉。

**进度排行**（按 tasks done）：
- GPU 0-3: 均完成 **5/10** tasks（~7h elapsed）
- GPU 5 (vla_mean): **4/10** tasks
- GPU 4 (obs-only-norm02): **3/10** tasks（晚启动 2.5h）

**5-task 中期成绩**（关键数据）：

| 方法 | 5-task SR | vs baseline |
|------|-----------|-------------|
| **crm_obs_only (norm=0.1)** | **16%** | **+4pp over baseline** |
| crm_perdof | 10% | ≈ baseline |
| reconvla (argmin) | 8% | -4pp |
| crm_scalar | 4% | -8pp |
| vla_only (single, done) | 12% | baseline |

**obs_only 继续领先**，特别是 bbq_sauce 上 40% 远超其他方法。scalar 表现最差。

**ETA**：
- GPU 0-3 (5/10 done): **~01:00 May 16**
- GPU 4-5 (3-4/10 done): **~03:00 May 16**

---
