# analysis v4 inject25 s7 s1

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v4-inject25-s7-s1_20260515T223152_result.json`
- **Structured JSON:** [`1d190c1c087212e4db5e.json`](../../sessions/1d/1d190c1c087212e4db5e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已成功完成并更新 registry。汇总：

| 指标 | v4-taxei-fixed-inject25-s7 | v4-random-fixed-inject25-s1 |
|---|---|---|
| train_loss (avg) | 0.4242 | 0.4261 |
| final_step_loss | 0.2571 | 0.2442 |
| token_accuracy | 0.904 | 0.912 |
| train_steps | 1635 | 1635 |
| duration | 57.2 min | 57.0 min |
| memory | 17.55 GiB | 18.0 GiB |
| checkpoint | `.../v4_taxei_fixed_inject25_s7/v0-20260516-053222/checkpoint-1635` | `.../v4_random_fixed_inject25_s1/v0-20260516-053219/checkpoint-1635` |
| W&B | 无 | 无 |
| 异常 | 无 | 无 |

**与参考值对比**：指标正常，无偏离。
- s7 的 train_loss=0.4242 与 s1 参考值 0.4243 几乎一致
- 步数 1635、时长 ~57min 均吻合
- token_accuracy 0.90-0.91 与 r2 参考值 0.893 一致

---
