# fix registry westb1 westd3

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_registry_westb1_westd3_20260521T233542_result.json`
- **Structured JSON:** [`639a33ab7d77471e0f1d.json`](../../sessions/63/639a33ab7d77471e0f1d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个实验全部修复完成。汇总：

| 实验 | 修复前 | 修复后 |
|------|--------|--------|
| **eval_math500_sft_standard_25** | DONE, 无 pid/gpu | RUNNING, westb:1, PID 104592 |
| **eval_math500_sft_cka_only_20_v6** | PREPARING, 无 hypothesis/parent/spec | RUNNING, westb:1, PID 118095, parent=v5, hypothesis 已填 |
| **eval_math500_sft_random_20** | RUNNING, 无 gpu/pid | RUNNING, westd:3, PID 385685 |

注意 `eval_math500_sft_standard_25` 保留了历史记录（v1 结果 13% accuracy 已被 Director 批准采用），retry_count 递增到 1。当前运行是新一轮 eval。

---
