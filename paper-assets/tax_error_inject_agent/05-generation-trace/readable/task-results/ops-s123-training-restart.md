# ops s123 training restart

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_s123-training-restart_20260516T130029_result.json`
- **Structured JSON:** [`54b41bce8c7f4c7f42ef.json`](../../sessions/54/54b41bce8c7f4c7f42ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**所有 sessions 都在正常运行，不是 stale 的。** 它们都在今天 20:52 刚创建，且 GPU 占用率很高。

## 当前状态

| GPU | 显存 | 利用率 | 进程 |
|-----|------|--------|------|
| 0 | 16837 MiB | 89% | `eval/injected_eval.py` — TaxEI s0 eval (PID 278314) |
| 1 | 24807 MiB | 99% | `swift sft` — vanilla-s123 训练 (PID 277575) |
| 2 | 26335 MiB | 99% | `swift sft` — taxei-s123 训练 (PID 277781) |
| 3 | 26335 MiB | 99% | `swift sft` — random-s123 训练 (PID 277973) |

## tmux sessions（全部活跃）
- `llama31-vanilla-s123` — GPU 1 训练中
- `llama31-taxei-s123` — GPU 2 训练中
- `llama31-random-s123` — GPU 3 训练中
- `llama31-taxei-s0-eval` — GPU 0 eval 中

**无需清理，s123 三个训练已经在跑了。** 看起来是之前已经成功提交了。

---
