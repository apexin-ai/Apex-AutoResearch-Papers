# check bootstrap v3 urgent status

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_bootstrap_v3_urgent_status_20260523T080439_result.json`
- **Structured JSON:** [`9c69b8ee4bbef73bc6ed.json`](../../sessions/9c/9c69b8ee4bbef73bc6ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

**进程状态：双卡均活跃，无异常。**

| 项目 | GPU 0 | GPU 1 |
|------|-------|-------|
| 利用率 | **82%** | **0%**（正常，见下） |
| VRAM | 15.4 / 97.9 GB | 0.7 / 97.9 GB |
| PID | 728135 | 725751 |
| 当前任务 | `openvla_object_trained` — 提取中 ~1150/5000 samples | `tracvla_goal_untrained` — **RidgeCV 拟合阶段**（CPU-bound） |

**GPU 1 为 0% 的原因**：该进程已完成 5000 样本提取，正在做 RidgeCV 回归拟合，这是纯 CPU 计算，GPU 空闲是预期行为。

**完成进度：5/20**

已完成：
1. `openvla_goal/trained` ✅
2. `openvla_goal/untrained` ✅
3. `openvla_spatial/trained` ✅
4. `openvla_spatial/untrained` ✅
5. `tracvla_goal/trained` ✅

正在运行：
- `tracvla_goal/untrained`（GPU 1，RidgeCV 阶段，即将产出 JSON）
- `openvla_object/trained`（GPU 0，提取阶段 ~23%）

剩余 13 个条件待跑。两个 tmux session (`bootstrap_v3_cuda0`, `bootstrap_v3_cuda1`) 均正常，无需重启。

---
