# ops replace westd38929 gpu01 pi05 goal

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_replace-westd38929-gpu01-pi05-goal_20260524T073034_result.json`
- **Structured JSON:** [`2f765ba0e5b5228d7c22.json`](../../sessions/2f/2f765ba0e5b5228d7c22.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。westd-38929 当前 GPU 状态：

| GPU | 显存占用 | 实验 |
|-----|---------|------|
| 0 | 10,538 MiB | `eval_pi05_random_k09_goal_seed42_postfix` ✅ |
| 1 | 10,532 MiB | `eval_pi05_random_k085_goal_seed42_postfix` ✅ |
| 2 | 1 MiB | 空闲 |
| 3 | 4,856 MiB | X-VLA 实验（未动） |

已完成：
- 终止 GPU 0/1 上的 X-VLA 实验（`eval_xvla_l2norm_k03_long_seed42`, `eval_xvla_random_k03_long_seed42`），registry 标记 killed
- GPU 0 部署 π0.5 Random k=0.9 Goal post-fix
- GPU 1 部署 π0.5 Random k=0.85 Goal post-fix
- 两个实验 registry 已注册为 RUNNING，模型已加载上 GPU

---
