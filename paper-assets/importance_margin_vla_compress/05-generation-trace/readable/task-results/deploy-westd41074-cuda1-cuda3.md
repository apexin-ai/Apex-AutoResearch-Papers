# deploy westd41074 cuda1 cuda3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd41074_cuda1_cuda3_20260522T182503_result.json`
- **Structured JSON:** [`8f7d7c8c3756c8e1a66f.json`](../../sessions/8f/8f7d7c8c3756c8e1a66f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息齐全。汇总如下：

---

## westd-41074 四卡状态

| GPU | VRAM | 状态 | 进程 |
|-----|------|------|------|
| **cuda:0** | 10.4 GB / 26% | **运行中** | Goal L2norm k=0.3 — 正在跑 T6/10，累计 SR≈52% |
| **cuda:1** | 加载中 | **刚部署** | Long L2norm k=0.7 (seed42) — 模型加载中 |
| **cuda:2** | 10.7 GB / 16% | **运行中** | Attention k=0.7 Object — T2/10，SR=0% (attention 30%裁剪太狠) |
| **cuda:3** | 27.5 GB / 0% | **运行中** | M64 训练 (v6) — 仍在跑，不动 |

## 任务执行结果

**任务 A** — cuda:1 Long L2norm k=0.7 已部署，tmux session `eval_l2norm_k07_long`, 日志 `eval_pi05_l2norm_k07_long_seed42_v2.log`，artifact 已注册。

**任务 B** — cuda:3 M64 训练仍在跑（27.5 GB VRAM），不部署 Random k=0.9。

**任务 C** — cuda:0 是 Goal L2norm k=0.3（`--suite libero_goal --keep_ratio 0.3`），当前进度 T6/10，累计 SR≈52%，未完成。

## 收割：Long L2norm k=0.9 已完成

**SR = 81.0%**（405/500, 132.5 min）

Per-task: 96%, 100%, 88%, 100%, 92%, 96%, 10%, 84%, 46%, 98%

T6（white mug + chocolate pudding）断崖 10%，T8（both moka pots on stove）46%，其余 ≥84%。与 Object k=0.9 的 97.2% 相比，Long 下降明显但仍保持 81%。

---
