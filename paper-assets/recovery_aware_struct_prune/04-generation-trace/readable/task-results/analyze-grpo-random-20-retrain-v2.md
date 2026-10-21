# analyze grpo random 20 retrain v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_grpo_random_20_retrain_v2_20260523T192328_result.json`
- **Structured JSON:** [`32994a126a575deacd62.json`](../../sessions/32/32994a126a575deacd62.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

---

**分析结论（汇报用）：**

`grpo_random_20_retrain_v2` 训练正常完成（100 steps, 3.07h）。Final reward=0.2875，处于 standard_20 (0.15–0.30) 范围的高端，高于 cka_only_20 (0.15–0.25)。训练过程中 reward 在 0.16–0.29 间波动，无 collapse 迹象，KL 稳定在 ~0.004。Random pruning 作为最弱 baseline，其 GRPO recovery reward 与 structured methods 差距不大，说明 GRPO recovery 对 pruning criterion 的敏感度可能低于预期——这对后续 method comparison 分析值得关注。Checkpoint 已保存至 `/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_retrain/`。

---
