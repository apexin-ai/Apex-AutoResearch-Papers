# ops d168 westd38929 smolvla v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d168_westd38929_smolvla_v2_20260522T141953_result.json`
- **Structured JSON:** [`e8d79b52bed12d7b809b.json`](../../sessions/e8/e8d79b52bed12d7b809b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**全 4 卡已在跑 SmolVLA 实验，不需要重新部署。** 以下是当前状态：

---

### GPU 0 — `smolvla_object` (PID 232565)
| 顺序 | 实验 | 状态 |
|------|------|------|
| 1 | l2_norm k=0.95 libero_object | **运行中** — Task 0: 2.0%, 正在跑 Task 1 |
| 2 | random_prune k=0.95 libero_object | 排队 |

⚠️ **与你的任务不同**: 你要求的是 l2_norm k=0.95/0.9/0.7/0.5，但当前队列是 l2_norm k=0.95 + random_prune k=0.95。k=0.9/0.7/0.5 未排入。

预估：当前实验还剩 ~42 min，总队列 ~1.5h 完成。

---

### GPU 1 — `smolvla_spatial` (PID 232641)
| 顺序 | 实验 | 状态 |
|------|------|------|
| 1 | baseline libero_spatial | **运行中** — Task 0: 60.0%, 正在跑 Task 1 |
| 2 | l2_norm k=0.95 libero_spatial | 排队 |
| 3 | random_prune k=0.95 libero_spatial | 排队 |

✅ **与你的任务完全一致。** 预估总队列 ~2.5h。

---

### GPU 2 — `smolvla_goal` (PID 232843, CUDA_VISIBLE_DEVICES=3)
| 顺序 | 实验 | 状态 |
|------|------|------|
| 1 | baseline libero_goal | **运行中** — Task 0: 60.0%, Task 1: 86.0%, 正在跑 Task 2 |
| 2 | l2_norm k=0.95 libero_goal | 排队 |
| 3 | random_prune k=0.95 libero_goal | 排队 |

✅ **与你的任务完全一致。** 预估总队列 ~2h。

---

### GPU 3 — `smolvla_long` (PID 249436, CUDA_VISIBLE_DEVICES=2)
| 顺序 | 实验 | 状态 |
|------|------|------|
| 1 | baseline libero_10 | **运行中** — 刚开始 ~6 min, 正在跑 Task 0 Ep 25/50 |
| 2 | l2_norm k=0.95 libero_10 | 排队 |
| 3 | random_prune k=0.95 libero_10 | 排队 |

✅ **与你的任务完全一致。** libero_10 max_steps=520，每实验 ~80 min，总队列 ~4h。

---

### 总结

- GPU 1/2/3 上的实验与你要求的 **完全一致**，已在运行，无需操作
- GPU 0 的队列与你的要求 **不同**：缺少 l2_norm k=0.9/0.7/0.5，多了 random_prune k=0.95
- 所有实验约在 22:12 启动（~8 分钟前），最早结束的是 GPU 0（~1.5h），最晚是 GPU 3（~4h）

**需要决策**: GPU 0 当前 random_prune k=0.95 完成后，是否追加 l2_norm k=0.9/0.7/0.5？或者现在就修改队列？

---
