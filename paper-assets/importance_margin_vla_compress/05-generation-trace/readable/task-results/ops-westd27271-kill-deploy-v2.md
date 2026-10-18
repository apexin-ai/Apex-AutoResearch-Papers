# ops westd27271 kill deploy v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd27271_kill_deploy_v2_20260522T091858_result.json`
- **Structured JSON:** [`26e4613c881237f3b8e3.json`](../../sessions/26/26e4613c881237f3b8e3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇报：

---

**Kill:** PID 213482 → 已杀（PID 212585 也连带退出，两个 GPU 均释放）

**Object seed43 缺口:**
- l2norm k=0.925 → MISSING（已部署 GPU 0）
- l2norm k=0.95 → 被误杀需重跑（已部署 GPU 1）
- l2norm k=0.9 → RUNNING（registry 中标记 RUNNING，需确认在哪台服务器）

**Spatial seed43 缺口:**
- l2norm k=0.3 → MISSING
- random k=0.3 → MISSING
- l2norm k=0.5 → MISSING

**部署:**
- GPU 0 → l2norm_k0925_object_seed43 (PID 325659)
- GPU 1 → l2norm_k095_object_seed43_v2 (PID 325931)

**GPU 状态:**

| GPU | PID | 实验 | 显存 |
|-----|-----|------|------|
| 0 | 325659 | l2norm k=0.925 object seed43 | 加载中（CPU→GPU） |
| 1 | 325931 | l2norm k=0.95 object seed43 v2 | 加载中（CPU→GPU） |

⚠️ 注意：registry 中 `eval_pi05_l2norm_k09_object_seed43` 和 `eval_pi05_l2norm_k0925_spatial_seed43`、`eval_pi05_random_k05_spatial_seed43` 标记为 RUNNING，但不在本机——可能在其他服务器上，或已失效需核实。

---
