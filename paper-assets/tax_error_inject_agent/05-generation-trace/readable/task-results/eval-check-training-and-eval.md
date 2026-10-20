# eval check training and eval

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_check-training-and-eval_20260515T005320_result.json`
- **Structured JSON:** [`c75c9fb3786763c9b06e.json`](../../sessions/c7/c75c9fb3786763c9b06e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 个训练都在跑，无已完成。状态汇总：

| 实验 | GPU | Step | 进度 | Loss | ETA |
|------|-----|------|------|------|-----|
| v4-taxei-fixed-inject50 | cuda:0 | 789/1635 | 48% | 0.403 | ~28 min |
| v4-random-fixed-inject10 | cuda:2 | 722/1635 | 44% | 0.425 | ~33 min |
| v4-random-fixed-inject25 | cuda:1 | 190/1635 | 12% | 0.592 | ~47 min |
| v4-random-fixed-inject50 | cuda:3 | 253/1635 | 15% | 0.654 | ~43 min |

cuda:0 和 cuda:2 上的训练最先完成（~28-33 min），cuda:1 和 cuda:3 的后启动，还需 ~43-47 min。

最早完成的是 inject50（cuda:0），约 28 分钟后。需要等训练完成后再启动 eval。要设置定时检查吗？

---
