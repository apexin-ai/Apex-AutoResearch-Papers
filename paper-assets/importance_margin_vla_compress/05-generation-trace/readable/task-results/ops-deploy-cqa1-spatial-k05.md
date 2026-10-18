# ops deploy cqa1 spatial k05

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy-cqa1-spatial-k05_20260524T070705_result.json`
- **Structured JSON:** [`a7b7d1689f01acc4d2fc.json`](../../sessions/a7/a7b7d1689f01acc4d2fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。cqa1-33015 四卡全部占满：

| GPU | 实验 | 状态 |
|-----|------|------|
| 0 | Random k=0.7 Spatial post-fix | RUNNING |
| 1 | Random k=0.3 Spatial post-fix | RUNNING |
| 2 | **Random k=0.95 Spatial post-fix v2** (PID 978544) | 刚启动 |
| 3 | **L2norm k=0.5 Spatial seed42 post-fix** (PID 979181) | 刚启动 |

调整说明：k=0.5 Random Spatial post-fix v3 已于今天 12:39 完成（71.8%），无需重跑。GPU 3 改部署 L2norm k=0.5 Spatial post-fix 填补 L2norm 曲线缺口。

---
