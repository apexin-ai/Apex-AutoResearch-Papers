# check scale up datagen status

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_scale-up-datagen-status_20260516T153201_result.json`
- **Structured JSON:** [`17ea1944508d490e525e.json`](../../sessions/17/17ea1944508d490e525e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

| 指标 | 数值 |
|------|------|
| 进程 PID 266813 | **已死** |
| 成功轨迹 | **797 条** |
| 失败轨迹 | 2,736 条 |
| 总尝试 | 3,533 条 |
| 成功率 | **22.6%** |
| 最后活动时间 | 2026-05-16 21:26 (本地时间) |
| 目标 | 1,000 条 |
| 差额 | **缺 203 条** |

进程已停止，数据在 `data/trajectories_scaleup_p1/`。797 成功条未达到 1000 目标，还需继续生成约 203 条（按当前 22.6% 成功率，需再跑约 900 个 task）。

---
