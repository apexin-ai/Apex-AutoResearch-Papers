# ops harvest xvla random k09 long

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest_xvla_random_k09_long_20260523T080003_result.json`
- **Structured JSON:** [`a4be5d80803b2dc816ab.json`](../../sessions/a4/a4be5d80803b2dc816ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

收割完成。汇总：

### eval_xvla_random_k09_long_seed42 — DONE ✓
- **SR = 29.6%** (148/500)，95% CI [25.8%, 33.7%]
- Suite: libero_10, mode: random, keep_ratio=0.9
- Per-task: T3=96%, T5=98%, T9=50%, T4=36%, T1=16%, 其余 5 个 task=0%
- Registry 已更新 → DONE/success

### eval_xvla_random_k05_goal_seed42 — 仍在运行
- PID 250272 存活，已跑 1h47m
- 当前可见 episodes 全部 FAIL（steps=800），尚未完成

### 分析
X-VLA Random LIBERO-10 完整曲线：

| keep_ratio | SR |
|---|---|
| k=0.95 | 48.2% |
| **k=0.9** | **29.6%** |
| k=0.7 | 53.0% |
| k=0.5 | 61.6% |

k=0.9 是全系列最低点（29.6%），显著低于 k=0.95（48.2%），且远低于更激进的 k=0.7（53.0%）和 k=0.5（61.6%）。Random pruning 的非单调性在 k=0.9 处最为极端——保留 90% token 反而是最差的。这与 L2 norm 在 k=0.9 崩溃（27.5%）的模式一致，说明 ~10% pruning 是一个"最差点"，pruning 太少反而引入最大干扰。

无活跃 cron 需要删除。

---
