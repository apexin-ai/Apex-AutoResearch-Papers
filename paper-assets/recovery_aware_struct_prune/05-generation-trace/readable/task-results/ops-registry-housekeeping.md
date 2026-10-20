# ops registry housekeeping

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_registry-housekeeping_20260515T024745_result.json`
- **Structured JSON:** [`9a8514f3649d25f5a50c.json`](../../sessions/9a/9a8514f3649d25f5a50c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**任务 1 — experiment_plan.yaml 更新：**
- `plan_002.registry_id`: `sft_rasp_20` → `[sft_rasp_20, sft_standard_20]`
- `plan_003.registry_id`: `grpo_stage2_rasp_20` → `[grpo_stage2_rasp_20, grpo_stage2_standard_20]`

**任务 2 — Registry metrics 更新：**

两个 SFT 实验的 metrics 已从 eval JSON 补全（来源：`/root/recovery_aware_struct_prune/results/eval_sft_*_combined.json`，N=100 greedy）：

| 指标 | sft_rasp_20 | sft_standard_20 |
|------|-------------|-----------------|
| greedy_accuracy | 57% (57/100) | 64% (64/100) |
| eos_rate_greedy | 0.99 | 0.99 |
| greedy_avg_len | 179.83 | 176.31 |
| greedy_min_len | 59 | 43 |
| greedy_max_len | 4096 | 4096 |

新增字段：`greedy_correct`, `greedy_total`, `greedy_min_len`, `greedy_max_len`。原有 metrics 数值确认与 JSON 一致。

注意：N=100 sampling eval（temperature=0.7）在两个模型上都被 kill 了（RASP 跑到 6%，Standard 跑到 18%），应该是 GRPO 训练抢了显存。`sampling_eos_rate_5` 仍是 5 样本快测数据。

---
