# fix plan006 config num steps

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_plan006-config-num-steps_20260514T090925_result.json`
- **Structured JSON:** [`d603f59bcf65a24796e7.json`](../../sessions/d6/d603f59bcf65a24796e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修改完成，3 个 Prolog config 文件的 `num_steps` 已从 100 改为 500：

| 文件 | 行号 | 修改 |
|------|------|------|
| `grpo_prolog_exec_only.yaml` | L6 | 100 → 500 |
| `grpo_prolog_exec_sta.yaml` | L6 | 100 → 500 |
| `grpo_prolog_exec_only_k16_warmup.yaml` | L6 | 100 → 500 |

没有 `max_steps` / `num_training_steps` 等其他字段名。运行中的 FOL 实验（cuda:0 PID 466128, cuda:1 PID 466540）不受影响。

---
