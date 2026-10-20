# eval v4 taxei seed1 eval

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_v4-taxei-seed1-eval_20260515T153802_result.json`
- **Structured JSON:** [`f7ec16266bff5219b256.json`](../../sessions/f7/f7ec16266bff5219b256.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

当前状态汇总：

| 实验 | 状态 | GPU | 说明 |
|------|------|-----|------|
| **v4-taxei-seed1** (训练) | DONE | - | loss=0.167, token_acc=0.942, checkpoint-3387 |
| **v4-taxei-seed7** (训练) | DONE | - | loss=0.175, token_acc=0.933, checkpoint-3387 |
| **v4-taxei-seed7-eval** | RUNNING | cuda:3 | PID 165338，正常运行 |
| **v4-taxei-seed1-eval** | QUEUED | - | OOM 失败 — cuda:2 被 `training_dynamics_forward.py` (PID 164797) 占用 25.5 GiB |

**需要等 training dynamics 完成释放 cuda:2 后重启 seed1 eval。** 该进程已运行约 2 分钟，做 vanilla 4358 条数据的 forward pass，预计几分钟内完成。要我轮询等待后自动重启 seed1 eval，还是你手动处理？

---
