# check bootstrap results urgent

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_bootstrap_results_urgent_20260522T200251_result.json`
- **Structured JSON:** [`237e715a28803cbe1926.json`](../../sessions/23/237e715a28803cbe1926.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Bootstrap 进度报告

### Tmux Sessions
| Session | 状态 |
|---------|------|
| `bootstrap_cuda0` | **运行中** (created May 22 23:54) |
| `bootstrap_cuda1` | **运行中** (created May 22 23:54) |

### GPU 状态
- GPU 0: **0% util**, 2135/97887 MiB — bootstrap 阶段是 CPU-bound（kernel matrix 计算）
- GPU 1: **0% util**, 691/97887 MiB — 同上

### 当前进度

两个 GPU 都仍在**第 1 个条件**的 bootstrap 阶段，尚无结果 JSON 产出：

| GPU | 当前任务 | Bootstrap 进度 | 最后时间戳 |
|-----|----------|---------------|-----------|
| cuda0 | `openvla / goal / trained` | **400/1000** | 03:21:55 |
| cuda1 | `tracvla / goal / trained` | **400/1000** | 03:18:58 |

### 结果文件
**0 个** — `/root/autodl-tmp/vla-ssd/results/bootstrap_r2/` 目录为空。

### 任务队列

**cuda0 (12 条件):**
1. openvla goal trained ← **进行中 (400/1000)**
2. openvla goal untrained
3. openvla spatial trained/untrained
4. openvla object trained/untrained
5. openvla long trained/untrained
6. nora goal trained/untrained
7. nora spatial trained/untrained

**cuda1 (8 条件):**
1. tracvla goal trained ← **进行中 (400/1000)**
2. tracvla goal untrained
3. tracvla spatial trained/untrained
4. tracvla object trained/untrained
5. tracvla long trained/untrained

### ETA 估算

Bootstrap 从 ~00:03 开始，03:22 达到 400/1000 → **每条件 ~8.3 小时**：
- 当前条件剩余 600 iter ≈ **~5 小时**
- **cuda0 总计**: 12 条件 × 8.3h ≈ **~100 小时 (4.2 天)**
- **cuda1 总计**: 8 条件 × 8.3h ≈ **~66 小时 (2.8 天)**

这个速度非常慢。1000 次 bootstrap 配合 kernel ridge regression 在 CPU 上跑代价很高。如果需要加速，可以考虑：减少 `n_bootstrap`（如 500）、用 linear ridge 代替 kernel ridge、或并行化 bootstrap 循环。

---
