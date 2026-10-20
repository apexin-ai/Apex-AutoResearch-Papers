# ops rasp v9 status and eval

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_rasp-v9-status-and-eval_20260516T024248_result.json`
- **Structured JSON:** [`28f1a18bb8c411b2a350.json`](../../sessions/28/28f1a18bb8c411b2a350.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## RASP v9 状态汇报

**训练仍在运行中**，不启动 eval。

| 项目 | 值 |
|------|-----|
| PID | 566666 (alive, elapsed 2h39m) |
| 当前 step | 20 / 30 |
| 剩余 steps | 10 |
| step 耗时 | ~405-410s/step (~6.8 min) |
| 预计完成 | **~68 min 后**（约 11:33） |

**Checkpoint 列表**：

| Checkpoint | 状态 | 保存时间 |
|-----------|------|---------|
| checkpoint-5 | ✓ | 08:41 |
| checkpoint-10 | ✓ | 09:15 |
| checkpoint-15 | ✓ | 09:49 |
| checkpoint-20 | ✓ | 10:25 |
| checkpoint-25 | 待生成 | ETA ~10:59 |
| checkpoint-30 | 待生成 | ETA ~11:33 |

**GPU 状态**：
- cuda:0: 71683/97887 MiB, 100% util → v9 训练中
- cuda:1: 29653/97887 MiB, 97% util → eval_step5 运行中

**训练指标 (step 20)**：reward=0.039, loss=-0.003, kl=0.001, clipped_ratio=98%。reward 从 step-10 的 0.015 上升到 0.039，有正向趋势。

训练完成后再启动 step-10 eval。

---
