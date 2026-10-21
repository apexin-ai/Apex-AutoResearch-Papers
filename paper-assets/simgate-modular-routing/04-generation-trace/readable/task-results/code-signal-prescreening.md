# code signal prescreening

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_signal-prescreening_20260513T154322_result.json`
- **Structured JSON:** [`93781dfa07a0e3b240b8.json`](../../sessions/93/93781dfa07a0e3b240b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

dry-run 通过，import 无报错，参数解析正常。

**产出**: `/root/autodl-tmp/simgate-modular-routing/src/signal_prescreening.py` 已写入并验证。

脚本与 `phase1_signal.py` 的关键差异:
- `--task_type` 单个任务（非逗号分隔）
- 默认 5 episodes（可 `--episodes` 覆盖）
- 仅 2-way：always-internal（纯 LLM，无 death filter）+ always-deterministic（fork + death filter）
- 每 episode 追加写入 JSONL，结束后打印 summary 含 Δ(D-I) 和方向判定（>1 POSITIVE / <-1 NEGATIVE / 其他 NEUTRAL）

---
