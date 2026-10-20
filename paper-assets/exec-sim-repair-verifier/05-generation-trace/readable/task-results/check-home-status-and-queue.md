# check home status and queue

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_home-status-and-queue_20260514T200433_result.json`
- **Structured JSON:** [`3b28b8c36b1f13481cd7.json`](../../sessions/3b/3b28b8c36b1f13481cd7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### GPU 状态
- GPU 100% 占用, 31727/32607 MiB
- **正在运行**: seed123 ckpt-600 val@5120 (PID 3165829, 已运行 2m42s, 352/9335 samples = 3.8%)
- 预计剩余约 65 分钟

### 已完成的 val@5120 结果

| Checkpoint | Acc% | F1_macro | F1_fail | F1_pass | Unparseable% | Truncated% |
|---|---|---|---|---|---|---|
| **8B ckpt-3000** | **89.50** | **84.08** | 74.78 | 93.37 | 0% | 2.51% |
| **seed123 (4B) ckpt-400** | **86.01** | **79.66** | 68.30 | 91.02 | 0% | 2.51% |
| 8B conda ckpt-400 | 80.47 | 75.84 | 65.27 | 86.42 | 0% | 2.51% |

### 当前队列
seed123 ckpt-600 val@5120 已在运行，无需手动启动。完成后下一个应启动 seed123 ckpt-800 val@5120。

seed123 ckpt-400 结果：86.01% acc / 79.66 F1_macro，比 8B ckpt-3000 (89.50/84.08) 低约 3.5pp，但作为 4B 模型 early checkpoint 表现不错。

---
