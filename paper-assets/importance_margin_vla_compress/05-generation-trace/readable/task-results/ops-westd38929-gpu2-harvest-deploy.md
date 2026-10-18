# ops westd38929 gpu2 harvest deploy

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd38929-gpu2-harvest-deploy_20260524T073607_result.json`
- **Structured JSON:** [`556a3a7b81410e2f6c54.json`](../../sessions/55/556a3a7b81410e2f6c54.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。

**Step 1 — L2norm k=0.5 Long 结果收割:**
| 指标 | 值 |
|------|------|
| Overall SR | **44.6%** (223/500) |
| 95% CI | [40.3%, 49.0%] |
| Per-task | 26%, 0%, 48%, 84%, 36%, 88%, 48%, 78%, 34%, 4% |

对比：L2norm k=0.7 Long=49.4%, Random k=0.85 Long=35.0%。L2norm 在 50% token 保留下仍比 Random 85% 保留高近 10pp，importance scoring 有效。

**Step 2 — GPU 2 新实验部署:**
- `eval_pi05_random_k07_goal_seed42_postfix` — PID 863249, 模型加载中
- Registry 已更新为 RUNNING

westd-38929 当前 GPU 分配：
- GPU 0: π0.5 Random k=0.9 Goal ✓
- GPU 1: π0.5 Random k=0.85 Goal ✓
- GPU 2: π0.5 Random k=0.7 Goal ← **新部署**
- GPU 3: X-VLA 实验 ✓

---
