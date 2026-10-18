# harvest eval pi05 l2norm k095 goal seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_eval_pi05_l2norm_k095_goal_seed42_20260523T224752_result.json`
- **Structured JSON:** [`77f390d47383b15519e6.json`](../../sessions/77/77f390d47383b15519e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

## 报告

### eval_pi05_l2norm_k095_goal_seed42 结果

| 指标 | 值 |
|------|-----|
| **Overall SR** | **90.8%** (454/500) |
| Elapsed | 90.4 min |
| Conclusion | negative（符合预期，接近 baseline ~91.6%） |
| Log path | `logs/eval_pi05_l2norm_k095_goal_seed42.log` |
| Result JSON | `eval_results/pi05_l2norm_k0.95_libero_goal_seed42.json` |

Per-task: 3 tasks 100%，最低 "put the wine bottle on the rack" 46%（一贯的难 task）。

**L2norm Goal 全曲线**: k=0.3→?, k=0.5→76.4%, k=0.7→89.0%, k=0.85→85.8%, k=0.9→90.6%, k=0.925→89.0%, **k=0.95→90.8%**

Registry 已更新为 DONE。Cron 不存在（已被其他 session 删除）。

### GPU 0 新任务已部署

**eval_pi05_random_k09_object_seed42_v2** — PID 459609, cqa1-33015 GPU 0, tmux session `eval_pi05_random_k09_object_seed42_v2`, registry 已更新为 RUNNING。

---
