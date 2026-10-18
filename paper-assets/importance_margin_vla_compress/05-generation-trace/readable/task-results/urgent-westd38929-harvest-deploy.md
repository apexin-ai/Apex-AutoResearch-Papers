# urgent westd38929 harvest deploy

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_westd38929-harvest-deploy_20260524T021321_result.json`
- **Structured JSON:** [`54252eb14c96c0e981ce.json`](../../sessions/54/54252eb14c96c0e981ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

## Phase 1 收割

| 实验 | 状态 | SR | 说明 |
|------|------|-----|------|
| eval_xvla_random_k085_object_seed42 | **DONE** | 65.0% (325/500) | Registry 已更新 |
| eval_xvla_random_k085_goal_seed42 | RUNNING (GPU 2) | 进行中 ~task 6-7 | PID 674830 |
| eval_xvla_random_k085_spatial_seed42 | RUNNING (GPU 3) | 进行中 task 8 | PID 674970，预计 30min 内完成 |

## Phase 2 部署

| GPU | 实验 | PID | 状态 |
|-----|------|-----|------|
| 0 | eval_xvla_l2norm_k05_goal_seed42_v2 | 950541 | 已启动，正在出结果 |
| 1 | eval_xvla_l2norm_k05_spatial_seed42_v2 | 951171 | 已启动，正在出结果 |

4 GPU 满载。GPU 2/3 的 k085 实验完成后可部署 l2norm k07 goal/spatial（如需 Table 2 数据）。

---
