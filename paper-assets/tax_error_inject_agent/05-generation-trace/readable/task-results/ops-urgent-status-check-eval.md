# ops urgent status check eval

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent-status-check-eval_20260514T182806_result.json`
- **Structured JSON:** [`62d32cafa0186b17db40.json`](../../sessions/62/62d32cafa0186b17db40.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 个实验正在运行，没有已完成的。汇总如下：

| 实验 | GPU | 状态 | 进度 | 预计剩余 | checkpoint |
|------|-----|------|------|----------|------------|
| v4-vanilla-seed0 | cuda:0 (PID 71959) | **RUNNING** | 1273/1635 (78%), epoch 2.28 | ~14min | checkpoint-545, checkpoint-1090 |
| v4-taxei-seed0 | cuda:1 (PID 72151) | **RUNNING** | 1392/3387 (41%), epoch 1.12 | ~1h7min | checkpoint-1129 |
| v4-random-seed0 | cuda:2 (PID 72488) | **RUNNING** | 1387/3387 (41%), epoch 1.12 | ~1h8min | checkpoint-1129 |
| v4-vanilla-seed123 | cuda:3 (PID 77937) | **RUNNING** | 77/1635 (5%), epoch 0.13 | ~55min | 无 |

**关键发现：**

- **report.md 与实际一致** — 4 个实验全部在跑，GPU 占用正常（18-19GB/卡）
- **v4-vanilla-seed0 即将完成**（~14min 后），已有 epoch 1、2 的 checkpoint
- **v4-taxei-seed0 和 v4-random-seed0** 进度相近，刚过 epoch 1
- **v4-vanilla-seed123** 刚启动 ~3 分钟
- Registry PID 和 nvidia-smi PID 有出入（swift 会 fork 子进程），但 GPU 分配正确

**无需立即操作。** v4-vanilla-seed0 约 14 分钟后完成，届时可启动 eval。其他 3 个至少还要 55min~1h+。

---
