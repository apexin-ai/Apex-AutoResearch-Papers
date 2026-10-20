# ops start 50pct evals all4

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_start-50pct-evals-all4_20260516T010757_result.json`
- **Structured JSON:** [`9ff652e1563addf82ec6.json`](../../sessions/9f/9ff652e1563addf82ec6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个 eval 全部启动成功，registry 已更新到 RUNNING。

| GPU | exp_id | checkpoint | tmux session |
|-----|--------|------------|--------------|
| cuda:0 | v4-taxei-fixed-inject50-s1-eval | `v4_taxei_fixed_inject50_s1/v0-20260516-075747/checkpoint-1635` | v4-taxei-fixed-inject50-s1-eval |
| cuda:1 | v4-random-fixed-inject50-s1-eval | `v4_random_fixed_inject50_s1/v1-20260516-075754/checkpoint-1635` | v4-random-fixed-inject50-s1-eval |
| cuda:2 | v4-taxei-fixed-inject50-s7-eval | `v4_taxei_fixed_inject50_s7/v0-20260516-075754/checkpoint-1635` | v4-taxei-fixed-inject50-s7-eval |
| cuda:3 | v4-random-fixed-inject50-s7-eval | `v4_random_fixed_inject50_s7/v0-20260516-075756/checkpoint-1635` | v4-random-fixed-inject50-s7-eval |

4 个 python3 进程均已确认在运行，各占一张 GPU。

---
