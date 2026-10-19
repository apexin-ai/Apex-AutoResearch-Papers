# diagnose bjb2 28827 failures

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_bjb2-28827-failures_20260521T003110_result.json`
- **Structured JSON:** [`5ae6aa550f5b9b704be1.json`](../../sessions/5a/5ae6aa550f5b9b704be1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 诊断报告：bjb2-28827 上 4 个实验进程消失

### 结论：全部正常完成，非失败

所有 4 个实验均**成功跑完并正常退出**，不需要重跑。Reconcile 误判为 failed 是因为进程完成后 PID 消失，而 reconcile 用 PID 存活作为健康信号，无法区分"正常退出"和"崩溃"。

### 各实验结果

| 实验 | Norm | Seed | Overall SR | JSON 产出 | 完成时间 |
|------|------|------|-----------|-----------|---------|
| norm01_seed53 | 0.1 | 53 | **19.0%** (19/100) | `eval_obs_only_object_norm01_seed53.json` | 08:18 |
| norm01_seed54 | 0.1 | 54 | **15.0%** (15/100) | `eval_obs_only_object_norm01_seed54.json` | 08:19 |
| norm005_seed50 | 0.05 | 50 | **13.0%** (13/100) | `eval_obs_only_object_norm005_seed50.json` | 08:19 |
| norm003_seed46 | 0.03 | 46 | **15.0%** (15/100) | `eval_obs_only_object_norm003_seed46.json` | 08:19 |

结果 JSON 文件均位于 `/root/acr-vla-conformal-refinement/logs/`，结构完整（包含 per_task 分解）。

### seed56 状态

seed56（pid=865274）也已**正常完成**，结果：15.0% (15/100)，JSON 写入于 08:30。reconcile 之前没报 miss 可能只是因为它完成得稍晚，timing 上恰好错过了检测窗口。

### 当前服务器状态

- GPU 0-4：空闲（0% util，1MiB）
- GPU 5：正在跑 **seed60 norm01**（pid=890017，已运行 ~1h05m，3389MiB）
- 磁盘充裕：数据盘 213GB 可用，根盘 18GB 可用
- 无 OOM/kill 记录

### 建议

- **不需要重跑**——直接将 4 个实验标记为 completed，结果从上述 JSON 文件提取
- Reconcile 逻辑可考虑增加对结果文件的检查：PID 消失时先看 output JSON 是否存在且完整，再决定标记 failed 还是 completed

---
