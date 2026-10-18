# ops cqa1 fill cuda0 check cuda1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1-fill-cuda0-check-cuda1_20260521T052140_result.json`
- **Structured JSON:** [`f915526e409c70e9797a.json`](../../sessions/f9/f915526e409c70e9797a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部确认完毕。

---

### 产出汇总

**1. X-VLA random k=0.7 Object — 已完成**
- **Overall SR: 65.2% (326/500)**, 95% CI: [60.9%, 69.2%]
- Per task:

| Task | SR | Description |
|------|-----|-------------|
| 0 | 98% (49/50) | alphabet soup |
| 1 | **0%** (0/50) | cream cheese |
| 2 | 100% (50/50) | salad dressing |
| 3 | 94% (47/50) | bbq sauce |
| 4 | 62% (31/50) | ketchup |
| 5 | 96% (48/50) | tomato sauce |
| 6 | **10%** (5/50) | butter |
| 7 | 92% (46/50) | milk |
| 8 | **0%** (0/50) | chocolate pudding |
| 9 | 100% (50/50) | orange juice |

耗时 77.3 min。

**2. X-VLA Spatial random k=0.5 — 已启动**
- PID: 118373 (实际子进程 118463)
- GPU 0: 4046MiB 占用，运行正常
- 日志: `~/runs/importance_margin_vla_compress/eval_xvla_random_k05_spatial_seed42.log`
- Task 0 前 2 eps 已成功

**其他 GPU 状态**: GPU 1 空闲，GPU 2 跑 k=0.3 Object (PID 60485)，GPU 3 跑 k=0.5 Object seed43 (PID 61785)。

---
