# diag tau sweep progress

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_tau-sweep-progress_20260526T012347_result.json`
- **Structured JSON:** [`4edf484c72c0ed1bf507.json`](../../sessions/4e/4edf484c72c0ed1bf507.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### bjb1-32546 (Spatial τ-sweep) — **正常运行，接近完成**

所有 6 个进程在最近 5 分钟内有写入，活跃中。Spatial benchmark = 10 任务/run。

| τ | 已完成任务 | 当前进度 |
|---|---|---|
| 0.05 | 9/10 | task 10 (wooden_cabinet) rollout 10/20 |
| 0.10 | 8/10 | task 9 (next_to_plate) rollout 15/20 |
| 0.15 | 9/10 | task 10 部分 |
| 0.20 | 9/10 | task 10 rollout 10/20 |
| 0.30 | 9/10 | task 10 部分 |
| 0.35 | 9/10 | task 10 部分 |

**关于 6h 异常性**：单 job SmolVLA Spatial 60-90 min 是正常的，但这里 **6 jobs 并发跑在同一 GPU 上**（日志全在 /tmp/eval_tau00X.log），吞吐 ~6× 衰减，6h 完成 ~90% 符合预期，不是异常。剩余 30-60 min。

**输出文件**：暂无最终 JSON。预期路径 `logs/eval_spatial_adaptive_k2_tau0XX_seed42.json`。

---

### bjb2-28827 (Spatial τ=0.40/0.45 + Goal paired) — **正常运行**

6 个进程活跃。

| 实验 | 已完成 | 当前 |
|---|---|---|
| tau040 spatial | 8/10 | task 9 rollout 10/20 |
| tau045 spatial | 8/10 | task 9 rollout 15/20 |
| goal_vla_s45 | 8/10 | task 9 |
| goal_vla_s47 | 8/10 | task 9 (turn_on_stove) 完成 |
| goal_adapt_s45 | 7/10 | task 8 完成 / task 9 开始 |
| goal_adapt_s47 | 7/10 | task 8 |

剩余 30-90 min。无最终 JSON。

---

### cqa1-32758 (Goal τ-sweep) — **⚠️ 有 3 个停了**

7 jobs，只有 4 个在最近 5 分钟有写入。Goal benchmark = 10 任务。

**活跃** (4 个，所有 3/10 任务完成，刚进 task 4 top_drawer)：
- tau015, tau020, tau030, tau035

**停滞** (3 个)：
- **tau005**：mtime 09:23（~10 分钟前停），3/10 完成，停在 task 4 rollout 5/20
- **tau010**：mtime 09:22（~11 分钟前停），3/10 完成，停在 task 4 rollout 5/20
- **tau040**：mtime 08:23（**~67 分钟前停**），3/10 完成，停在 task 3 后。**已死**

**整体异常**：7 jobs 并发跑了 6h 只完成 3/10 任务，吞吐严重塌陷（Goal max_steps=300 比 Spatial 大，加上 7 路并发）。即使 4 个活跃 job 继续，按当前速度还要 ~14h 才能跑完，不现实。

**建议**：
1. cqa1 上 tau040（死掉 1h+）需要重启或放弃
2. tau005/tau010 也可能已死，确认进程状态
3. cqa1 的 7 路并发吞吐太低，可能需要分批跑（每次 ≤ 3 路）

---
