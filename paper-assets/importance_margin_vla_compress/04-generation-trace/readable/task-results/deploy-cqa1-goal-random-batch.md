# deploy cqa1 goal random batch

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1_goal_random_batch_20260522T163520_result.json`
- **Structured JSON:** [`2d834bb83876c2789ad6.json`](../../sessions/2d/2d834bb83876c2789ad6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验正在加载 pi0.5 模型，一切正常。

## 汇总

| GPU | 状态 | 实验 |
|-----|------|------|
| cuda:0 | 15437 MiB, 在跑 | OpenVLA spatial 评估链（tmux: `openvla_spatial`）— **不动** |
| cuda:1 | 已部署 ✓ | `eval_pi05_random_k07_goal_seed42` — Random k=0.7 Goal, 正在加载模型 |
| cuda:2 | 已部署 ✓ | `eval_pi05_random_k05_goal_seed42` — Random k=0.5 Goal, 正在加载模型 |
| cuda:3 | 10141 MiB, 在跑 | π0.5 baseline libero_10（tmux: `pi05_long`）— **不动** |

**cuda:0 未部署 L2norm k=0.3 Goal** — 有活跃 OpenVLA spatial 评估进程在跑（63-89% util），不是残留。

**Registry 清理**: `eval_pi05_l2norm_k0925_spatial_seed43` 在磁盘上无日志、registry 中无记录——从未运行过。

---
