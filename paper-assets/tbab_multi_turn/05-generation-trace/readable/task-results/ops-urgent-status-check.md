# ops urgent status check

**tbab multi turn** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent-status-check_20260518T192253_result.json`
- **Structured JSON:** [`230295731c5cc0e84da9.json`](../../sessions/23/230295731c5cc0e84da9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### GPU
- RTX PRO 6000 | 73°C | 510W/600W | 31GB/98GB | GPU-Util 100%
- 占用进程: C2_s42 训练 (PID 67820)

### 进程状态

| 进程 | 状态 | 详情 |
|------|------|------|
| **eval_c4_s42** | 已完成 | P̄ = 5.49% (5/91) |
| **eval_c1_s137** | 已完成 | P̄ = 5.49% (5/91) |
| **mvp_c2_s42** | 训练中 | **238/471 steps (50.5%)**, ~12s/step, ETA ~46 min |
| **mvp_c4_s137** | 已完成 | EXIT_CODE=0, checkpoint saved |

### 全部 Eval 结果

| 实验 | P̄ | Correct | HumanEval | LiveCodeBench |
|------|-----|---------|-----------|---------------|
| C1_s42 | **7.69%** | 7/91 | — | — |
| C1_s137 | 5.49% | 5/91 | 5.6% | 5.5% |
| C4_s42 | 5.49% | 5/91 | 8.3% | 3.6% |

### Checkpoints

- c1_lora_only_seed42 ✓ (eval done)
- c1_lora_only_seed137 ✓ (eval done)
- c4_full_tbab_seed42 ✓ (eval done)
- c4_full_tbab_seed137 ✓ (训练完成, **未 eval**)
- c2_pos_reset_seed42 (训练中 50%)

### mvp_gate.py 无法运行

需要 C1-C4 x 2 seeds 共 8 个实验，当前只有 3 个 eval 完成。缺失：
- **C4_s137 eval** — checkpoint 已就绪，但 GPU 被 C2_s42 占用
- **C2_s42** — 训练中，~46 min 后完成，之后还需 eval
- **C2_s137** — 未开始
- **C3 (两个 seed)** — 未开始

Agent 空闲 62 分钟的原因：两个 eval 已完成退出，C4_s137 训练也已完成退出，当前只剩 C2_s42 在自动训练。没有新任务被调度。

---
