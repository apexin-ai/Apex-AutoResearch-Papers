# ops fix baseline eval norm stats

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_baseline_eval_norm_stats_20260522T020252_result.json`
- **Structured JSON:** [`7021083195f29f107ab8.json`](../../sessions/70/7021083195f29f107ab8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Log 最后停在 Task 0 初始化（Safety level: II），环境还在渲染/初始化阶段，这对 LIBERO 的 MuJoCo 环境是正常的。进程在跑，GPU 在占用，没有报错。

**汇报：**

1. **norm_stats.json** — 复制成功，1126 bytes，路径 `/root/autodl-tmp/checkpoints/baseline_object_pudding_eval/best/assets/physical-intelligence/libero/norm_stats.json`
2. **baseline eval PID** — 300495（GPU 1 上的新进程）；GPU 0 的 PID 191747 是其他已有任务
3. **GPU 1 使用** — 已占用 8271 MiB（PID 300495）
4. **Log 状态** — 正常。norm_stats 从新路径成功加载（`Loaded norm stats from .../baseline_object_pudding_eval/best/assets/...`），已进入 Task 0 环境初始化，无报错。SafeLIBERO object suite level II 已开始。

---
