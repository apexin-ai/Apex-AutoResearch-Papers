# diagnose westd47453 ssh failure

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_westd47453_ssh_failure_20260517T093150_result.json`
- **Structured JSON:** [`9906e74efff087a63f28.json`](../../sessions/99/9906e74efff087a63f28.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**三个进程全部存活，正在正常训练中。** 标记 failed 纯粹是 SSH 监控连接中断的误报。

| 实验 | PID | 状态 | 进度 | 预计剩余 | Checkpoint |
|------|-----|------|------|----------|------------|
| **batch_adaptive_tau_rho06_seed42** | 372142 | ALIVE (9h45m) | 7849/8477 (93%) | ~3 min | 尚未保存 |
| **bs8_auto_nmin_seed42** | 370013 | ALIVE (10h05m) | 4812/6103 (79%) | ~56 min | 尚未保存 |
| **rho02_adaptive_tau09_seed42** | 367604 | ALIVE (10h32m) | 2004/8477 (24%) | ~33 min | 尚未保存 |

### 详细说明

1. **batch_adaptive_tau_rho06_seed42** — 即将完成（~3分钟内），速度 3.23 it/s，总 8477 步。
2. **bs8_auto_nmin_seed42** — 速度较慢（2.6 s/it），当前 epoch 0.21，总 6103 步，预计 ~1h 内完成。
3. **rho02_adaptive_tau09_seed42** — 速度 3.23 it/s，但仅完成 24%（2004/8477），预计 ~33 min 完成当前 epoch 进度条显示的剩余部分。

### 结论

- **误报**：三个实验均未中断、未报错、未被杀，训练正常推进中
- Checkpoint 目录尚不存在，说明模型保存发生在训练结束时
- 建议：将这 3 个实验状态从 `failed` 改回 `running`，等待训练自然结束后采集指标

---
