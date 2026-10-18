# deploy cqa1 cuda2 harvest 20260522

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1_cuda2_harvest_20260522_20260522T215037_result.json`
- **Structured JSON:** [`f688ff30773c62162deb.json`](../../sessions/f6/f688ff30773c62162deb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Session 存活，模型加载中。

## 执行总结

### GPU 状态 (cqa1-33015)
| GPU | 显存 | 任务 | 状态 |
|-----|------|------|------|
| cuda:0 | 10.2GB | π0.5 L2norm k=0.7 Goal s42 | RUNNING (T3, 74%) |
| cuda:1 | 10.3GB | π0.5 Random k=0.95 Goal s42 | RUNNING (T3, 83.3%) |
| cuda:2 | 加载中 | **π0.5 Random k=0.3 Goal s43** | 刚部署，模型加载中 |
| cuda:3 | 10.7GB | pi05_long chain | RUNNING |

### 收割
- **eval_pi05_random_k03_goal_seed42**: SR=**51.8%** (259/500, 140min) → Registry DONE

### 部署
- **eval_pi05_random_k03_goal_seed43**: cuda:2, tmux `eval_random_k03_goal_s43` → Registry RUNNING

### Registry 修复
- **eval_pi05_random_k03_goal_seed42**: 新建 → DONE (success, SR=51.8%)
- **eval_pi05_l2norm_k07_goal_seed42**: 新建 → RUNNING (实际在 cuda:0 上跑，T3/10 进度 74%)
- ~~DEPLOYED→RUNNING 问题~~：实验原本不在 registry，已新建并设为 RUNNING

---
