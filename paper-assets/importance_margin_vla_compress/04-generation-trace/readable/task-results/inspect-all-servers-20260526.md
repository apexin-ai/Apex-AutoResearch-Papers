# inspect all servers 20260526

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_inspect_all_servers_20260526_20260526T024344_result.json`
- **Structured JSON:** [`9649728cc8e4953a56a6.json`](../../sessions/96/9649728cc8e4953a56a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态汇总

### westd-41074 — 4× RTX PRO 6000 Blackwell (98GB)

| GPU | 显存占用 | GPU利用率 | PID | 状态 |
|-----|---------|----------|-----|------|
| 0 | 16.2/98 GB | **0%** | 303189 | ⚠️ 进程在但利用率 0%，可能已完成（Random k=0.85 Long v2?） |
| 1 | 10.7/98 GB | 21% | 319659 | ✅ 训练中 — π0.5 L2norm k=0.75 Long v3 |
| 2 | 16.0/98 GB | **0%** | 259181 | ⚠️ 进程在但利用率 0%，可能已完成（attn_k07_object?） |
| 3 | 10.6/98 GB | 23% | 315599 | ✅ 训练中 — π0.5 zeromask_random k=0.9 Object v3 |

GPU0 和 GPU2 进程仍占显存但利用率 0%，大概率训练已完成（进程挂起或在做收尾）。

### westd-38929 — 4× RTX PRO 6000 Blackwell (98GB)

| GPU | 显存占用 | GPU利用率 | PID | 状态 |
|-----|---------|----------|-----|------|
| 0 | 15.8/98 GB | 65% | 6815 | ✅ 训练中 — attn_k07_long_v2 |
| 1 | 15.9/98 GB | 49% | 7009 | ✅ 训练中 — l2norm_k07_long_v2 |
| 2 | 15.9/98 GB | 79% | 7384 | ✅ 训练中 — random_k07_long_v2 |
| 3 | 15.9/98 GB | 79% | 8069 | ✅ 训练中 — l2norm_k085_long_v2 |

全部 4 卡满载训练中，PID 与预期吻合。

### cqa1-33015 — 4× RTX 4090 D (24GB) ✅ 已恢复在线

| GPU | 显存占用 | GPU利用率 | 进程 |
|-----|---------|----------|------|
| 0-3 | 0/24 GB | 0% | 无 |

**全部 4 卡空闲**，无任何实验进程。

### westd-27271 — 2× RTX PRO 6000 Blackwell (98GB) ✅ 已恢复在线

| GPU | 显存占用 | GPU利用率 | 进程 |
|-----|---------|----------|------|
| 0-1 | 0/98 GB | 100%* | 无 |

**2 卡空闲**（无计算进程）。利用率显示 100% 但无进程，可能是驱动层 artifact 或后台系统任务。

---

### 总结

- **活跃训练**: 6 个实验运行中（41074×2 + 38929×4）
- **疑似完成**: 41074 GPU0（Random k=0.85 Long v2?）和 GPU2（attn_k07_object?）— 进程在但 GPU 利用率 0%，需查日志确认
- **空闲可用**: cqa1-33015 全部 4×4090D + westd-27271 全部 2×Blackwell = **6 卡空闲**

---
