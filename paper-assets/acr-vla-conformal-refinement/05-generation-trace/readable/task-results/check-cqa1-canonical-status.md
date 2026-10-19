# check cqa1 canonical status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_cqa1-canonical-status_20260524T234136_result.json`
- **Structured JSON:** [`b464f73d51d5a28732a7.json`](../../sessions/b4/b464f73d51d5a28732a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### Canonical 实验状态（全部正在运行）

| 实验 | GPU | PID | 已完成 tasks | 总 tasks | 进度 |
|------|-----|-----|-------------|----------|------|
| adaptive-k10-spatial-s42 | 0 | 209914 | 2/10 | 在 task 3 中 | ~25% |
| adaptive-k10-spatial-s43 | 1 | 210191 | 2/10 | 在 task 3 中 | ~25% |
| adaptive-k10-spatial-s44 | 2 | 210468 | 2/10 | 在 task 3 中 | ~25% |
| adaptive-k10-spatial-s48 | 3 | 210826 | 2/10 | 在 task 3 开头 | ~20% |
| adaptive-k10-spatial-s49 | 4 | 211578 | 2/10 | 在 task 3 开头 | ~20% |
| vla-only-spatial-s44 | 5 | 230414 | 1/10 | 在 task 2 中 | ~15% |

所有 6 个 canonical 实验已在 07:07-07:24 UTC 成功部署并正常运行约 35 分钟。GPU 利用率 15-26%（adaptive），GPU 5 为 99%（VLA-only + 旧实验共享）。

### 旧实验
- **eval-supp-long-vla-only-s48** (GPU 5, PID 91476)：仍在跑，7/10 tasks 完成，已运行 ~4 小时，接近完成
- **eval-spatial-vla-only-s42-cqa1**：已完成，overall 78.5% (157/200)

### GPU 空闲情况
- **0 个空闲 GPU**。6 张 4090D 全部占满
- GPU 5 共享了两个实验（旧 long-s48 快完了，完成后会释放一些显存）

### 性能观察
Adaptive K=10 的前两个 task 成绩很好：
- Task 1 (bowl between plate and ramekin): 95-100%
- Task 2 (bowl next to ramekin): 85-95%

预计全部 canonical 实验还需 **~1.5-2 小时** 完成（spatial 10 tasks × 20 rollouts，当前速度 ~15 min/task for adaptive）。

---
