# diagnose nora untrained cf exit

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_nora_untrained_cf_exit_20260521T074711_result.json`
- **Structured JSON:** [`94d74b871ea739cc1f74.json`](../../sessions/94/94d74b871ea739cc1f74.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已无活跃任务，无需清除。

---

**实验 nora_goal_untrained_cf — 成功完成**

4 个 condition 全部跑完，耗时 31.2 min。Last-layer (L35) metrics：

| Condition | cos_dist | Cohen's d |
|-----------|----------|-----------|
| empty | 0.0814 | 19.01 |
| shuffled | 0.0332 | 7.43 |
| wrong | 0.0143 | 7.71 |
| paraphrased | 0.0041 | 7.11 |

**排序**: empty > shuffled > wrong > paraphrased

输出文件: `/root/autodl-tmp/vla-ssd/results/nora_goal/untrained/counterfactual_combined.json`

Registry 已更新为 DONE/success。

---
