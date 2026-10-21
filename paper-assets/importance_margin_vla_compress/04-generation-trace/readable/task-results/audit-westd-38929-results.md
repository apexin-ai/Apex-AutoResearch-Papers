# audit westd 38929 results

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_westd-38929-results_20260521T163448_result.json`
- **Structured JSON:** [`7074bab9fdd7c499fd43.json`](../../sessions/70/7074bab9fdd7c499fd43.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Baseline restarted on GPU2, all 4 GPUs now active. Here's the status:

## 仍在运行

| 实验 | GPU | 进度 | 部分数据 | ETA |
|------|-----|------|---------|-----|
| **random k=0.5 seed42** | 0 | Task 10/10, Ep 30/50 | Tasks 1-9: 142/450 (31.6%) | **~12 min** |
| **random k=0.7 seed43** | 1 | Task 9/10, Ep 30/50 | Tasks 1-8: 203/400 (50.8%) | ~37 min |
| **baseline seed42** | 2 | Task 1/10, Ep 0 (刚重启) | — | ~5 hr |
| **l2norm k=0.3 seed43** | 3 | Task 9/10, Ep 20/50 | Tasks 1-8: 98/400 (24.5%) | ~47 min |

### random k=0.5 seed42 逐 task 明细（9/10 完成）

| Task | SR |
|------|----|
| 1 alphabet soup | 28/50 (56.0%) |
| 2 | 1/50 (2.0%) |
| 3 | 20/50 (40.0%) |
| 4 | 29/50 (58.0%) |
| 5 ketchup | 30/50 (60.0%) |
| 6 tomato sauce | 13/50 (26.0%) |
| 7 butter | 0/50 (0.0%) |
| 8 milk | 6/50 (12.0%) |
| 9 chocolate pudding | 15/50 (30.0%) |
| 10 orange juice | 23/30 进行中 |

**估算 overall SR: ~36%** (Task 10 按 23/30 pace 约 38/50，总计 ~180/500)

### 关键对比

- **random k=0.5 seed42 ~36%** vs seed7 35.8% → 高度一致，seed variance 极小
- **random k=0.5 ~36% < L2norm k=0.5 39.2%** → 确认 D132 预测：高 CV MLP connector 上 L2norm > random（~3pp 差距）

### baseline seed42 问题

原进程 (PID 186981) 已死，**无日志无输出**。可能原因：`results/` 目录不存在导致后续问题，或 OOM。已在 GPU2 重启（PID 363254），日志写入 `logs/eval_openvla_baseline_object_seed42.log`，已创建 `results/` 目录。预计 ~5 小时完成。

---
