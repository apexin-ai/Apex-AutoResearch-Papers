# ops xvla seed44 cqa1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_xvla-seed44-cqa1_20260520T132249_result.json`
- **Structured JSON:** [`d409b8a45864a5e566a0.json`](../../sessions/d4/d409b8a45864a5e566a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 seed44 实验已注册并在运行。汇总：

## 启动状态

| 实验 | GPU | PID | 状态 |
|------|-----|-----|------|
| `eval_xvla_prune_k07_seed44` (k=0.7, seed44) | GPU 0 | 115960 | RUNNING |
| `eval_xvla_prune_k09_seed44` (k=0.9, seed44) | GPU 1 | 116978 | RUNNING |
| seed43 k=0.5 (已有) | GPU 3 | 894197 | RUNNING |

**预估完成时间**（基于 seed43 耗时）：
- k=0.9: ~54 min → **约 22:18 UTC**
- k=0.7: ~91 min → **约 22:55 UTC**

## seed43 已完成结果

**k=0.7 seed43**: SR=**59.0%** (295/500), CI=[54.6%, 63.2%], 耗时 5446s

| Task | SR |
|------|----|
| 0 alphabet soup | 98% |
| 1 cream cheese | 0% |
| 2 salad dressing | 100% |
| 3 bbq sauce | 84% |
| 4 ketchup | 34% |
| 5 tomato sauce | 94% |
| 6 butter | 18% |
| 7 milk | 72% |
| 8 chocolate pudding | 2% |
| 9 orange juice | 88% |

**k=0.9 seed43**: SR=**97.6%** (488/500), CI=[95.9%, 98.6%], 耗时 3225s — 所有 task ≥92%。

对比 seed42: k=0.7 从 56.2% → 59.0%（seed43 略高但在 CI 内），k=0.9 从 99.2% → 97.6%（同样 CI 内）。cliff 模式跨 seed 可复现。

---
