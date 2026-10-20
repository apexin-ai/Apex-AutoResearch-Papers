# analysis v4 random fixed inject10 s1

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v4-random-fixed-inject10-s1_20260515T210333_result.json`
- **Structured JSON:** [`2d5f4da7f0fe720974ff.json`](../../sessions/2d/2d5f4da7f0fe720974ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。汇总：

**v4-random-fixed-inject10-s1** → `DONE` / `success`

| 指标 | 值 |
|---|---|
| final_loss | 0.3096 |
| train_loss_avg | 0.4238 |
| final_token_acc | 0.8902 |
| total_steps | 1635 |
| epochs | 3 |
| train_runtime_sec | 3488 |
| memory_gib | 18.13 |
| train_speed_s_per_it | 2.132 |
| checkpoint | `.../v4_random_fixed_inject10_s1/v1-20260516-040130/checkpoint-1635` |
| W&B | 无 |

训练正常收敛，EXIT_CODE=0。与同系列 TaxEI s7 对比：Random 的 avg loss 略高（0.4238 vs 0.4212），final token_acc 略低（0.890 vs 0.905），符合预期。

---
