# diag occ extraction progress

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_occ_extraction_progress_20260520T112321_result.json`
- **Structured JSON:** [`9c5dd2bacd6a29ba87e7.json`](../../sessions/9c/9c5dd2bacd6a29ba87e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### OCC 提取进度

**10 个进程全部在运行**，已运行 1h49m，状态均为 `Rl`。

各 task 已完成 demo 数（每 task 共 50 个 demo）：

| Task | 完成 demo 数 | Task | 完成 demo 数 |
|------|-------------|------|-------------|
| 0 | 1 (demo_1 进行中) | 5 | 1 (demo_1 进行中) |
| 1 | 1 | 6 | 0 |
| 2 | 0 | 7 | 0 |
| 3 | 1 | 8 | 1 |
| 4 | 0 | 9 | 0 (demo_0 进行中) |

**总进度：~5/500 demos = ~1%**

大部分时间耗在初始化（加载 MuJoCo 场景、geom 分类等）。实际帧处理速度 ~1.8s/frame，每个 demo ~100 帧 ≈ 3 min/demo/process，但 10 个进程共享 CPU 导致实际慢很多。

**预估剩余时间：20-30 小时**（假设初始化已基本完成，后续纯处理提速）

### GPU 3 状态

| GPU | 利用率 | 显存占用 |
|-----|--------|---------|
| 0 | 99% | 63007/97887 MiB |
| 1 | 99% | 62237/97887 MiB |
| 2 | 99% | 62193/97887 MiB |
| **3** | **0%** | **5672/97887 MiB** |

GPU 3 利用率 0% — OCC 提取是 CPU-bound（MuJoCo 物理仿真 + 几何计算），GPU 仅用少量显存。

### Vanilla 训练进程

3 个训练进程全部正常运行（GPU 0-2 各占 99%）：

| PID | Seed | 运行时间 | 状态 |
|-----|------|---------|------|
| 100203 | 42 (s0) | 2h01m | Rsl |
| 97847 | 43 (s1) | 2h03m | Ssl |
| 98174 | 44 (s2) | 2h03m | Rsl |

### OCC Index

`occ_index.json` **尚不存在**，需等提取全部完成后运行 `build_occ_index.py`。

### 注意事项

10 个提取进程全部跑在 CPU 上（GPU 3 利用率 0%），相互争抢 CPU 资源导致整体很慢。如果想加速，可以考虑减少并行进程数（比如分两批各 5 个）或确认提取脚本是否有 GPU 加速路径。

---
