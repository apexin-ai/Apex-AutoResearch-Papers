# ops registry cleanup running audit

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_registry_cleanup_running_audit_20260519T105257_result.json`
- **Structured JSON:** [`de5bf9bbffdef1b52b0e.json`](../../sessions/de/de5bf9bbffdef1b52b0e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 审计结果

### RUNNING 条目状态（共 5 个）

| 实验 | 服务器/GPU | PID | 运行时间 | 状态 |
|---|---|---|---|---|
| grpo_cka_only_20_seed123 | westb cuda:1 | 857962 | 7h18m | ALIVE |
| eval_humaneval_grpo_standard_20_fair_2048_v3 | westd cuda:2 | 76392 | 3h50m | ALIVE |
| eval_humaneval_sft_cka_only_20_2048_v2 | westd cuda:1 | 78740 | 3h15m | ALIVE |
| eval_gsm8k_grpo_standard_20_fair_v2 | westd cuda:0 | 83299 | 1h54m | ALIVE |
| eval_humaneval_sft_standard_20_2048_v3 | westd cuda:3 | 86171 | 1h15m | ALIVE |

**全部 5 个 PID 存活，无需清理。**

### 已知 DEAD 条目

4 个均已不在 RUNNING 状态，registry 已正确更新：
- `eval_humaneval_grpo_standard_20_fair_2048` → DONE/failed
- `eval_humaneval_sft_cka_only_20_2048` → DONE/failed
- `eval_humaneval_grpo_cka_only_20_2048` → DONE/success (pass@1=20.12%)
- `eval_math500_sft_standard_20_2048_v2` → 未在 registry 中找到（RUNNING/DONE 均无此条目）

### Cron 监控

**当前无任何 cron job。** 5 个活跃实验均无 cron 监控。

---
