# ops snapshot bjb1 45299 session resume

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_snapshot_bjb1_45299_session_resume_20260520T194054_result.json`
- **Structured JSON:** [`c9fb5b52a257f01a87cb.json`](../../sessions/c9/c9fb5b52a257f01a87cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
exp_030c (Cheetah σ=1.0): step=116K, eval_return=162.2 (@115K), ve_ratio=0.14, 进程状态=alive (PID 920973, 2h51m)
exp_031 (PickCube σ=0.2): step=132.5K, eval_return=23.45 (@132.5K), ve_ratio=0.18, 进程状态=alive (PID 908459, 6h58m)
GPU状态: cuda:0=14% (3.9GB/98GB)  cuda:1=7% (2.8GB/98GB)
```

**exp_030c 细节:**
- eval_return 轨迹: 8→88→166→**372 (peak@35K)**→144→266→197→108→96→73→123→162
- 35K 后大幅回落，115K 回升到 162 但远不及 peak
- ve_ratio=0.14，gate 完全锁死在 dt=2（gate_dt_2_frac=1.0，entropy=0）
- train_return@116K ≈ 95

**exp_031 细节:**
- eval_return 轨迹: 2.4→19.2→17.7→11.5→7.8→4.8→10.4→16.2→19.1→19.6→14.5→17.9→19.7→**23.5 (@132.5K)**
- NVE 从 peak（约 3.7x）已崩到 0.18，确认 negative result
- gate 同样锁死 dt=2，entropy=0
- 正在跑 132.5K 的 eval，距目标 210K 还有 77.5K 步
- train_return 在 18-25 区间波动，无上升趋势

**问题信号:** 两个实验的 gate 都 100% 锁死在 dt=2，完全没有自适应行为。gate_empirical_entropy=0，gate_entropy_ratio=0。这不是 gating 机制在做选择，而是退化成了固定 horizon。

---
