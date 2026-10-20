# eval v4 vanilla seed1 eval

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_v4-vanilla-seed1-eval_20260515T144713_result.json`
- **Structured JSON:** [`d2e90cec17b972948c19.json`](../../sessions/d2/d2e90cec17b972948c19.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

- **Registry**: `v4-vanilla-seed1` (DONE, parent) + `v4-vanilla-seed1-eval` (RUNNING)
- **Eval**: tmux session `v4-vanilla-seed1-eval` 在 cuda:0 上运行，模型已加载 (17GB)
- **命令**: `recovery.py --no_inject --task_list eval_tasks_47.json --num_episodes 47 --seed 42`
- **日志**: `~/runs/tax_error_inject_agent/v4-vanilla-seed1-eval.log`
- **输出**: `eval_results/v4_vanilla_seed1_eval.json`
- **Cron**: 每 8 分钟检查一次，完成后自动更新 registry metrics 并对比 seed=42 baseline (61.7%)

---
