# code scoring ablation random

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_scoring_ablation_random_20260517T085145_result.json`
- **Structured JSON:** [`039775b584aa193b7d66.json`](../../sessions/03/039775b584aa193b7d66.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`exit 0` inserted at line 54, before the RANDOM section. When gradient finishes on cuda:0, the script will exit cleanly without trying random/cka_only.

**结果：**

| GPU | tmux session | Methods | Status |
|-----|-------------|---------|--------|
| cuda:0 | `scoring_ablation_v2` | gradient only (steps 2-4) | SFT running (PID 694917) |
| cuda:1 | `scoring_ablation_random` | random → cka_only (各4步) | random prune 进行中 (PID 695525) |

- `run_remaining_ablation.sh` 已在 gradient 后插入 `exit 0`，不会再跑 random/cka_only
- `run_random_cka_ablation.sh` random 完成后自动继续 cka_only
- 日志：`/root/autodl-tmp/recovery_aware_struct_prune/results/random_cka_ablation_log.txt`

---
