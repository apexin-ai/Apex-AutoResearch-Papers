# analysis v4 random fixed inject25 s1

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v4-random-fixed-inject25-s1_20260515T223153_result.json`
- **Structured JSON:** [`05a7d88a9c17af532cb6.json`](../../sessions/05/05a7d88a9c17af532cb6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已完成，registry 更新为 DONE。

## 总结

| 指标 | v4-random-fixed-inject25-s1 | v4-taxei-fixed-inject25-s7 |
|------|---------------------------|--------------------------|
| train_loss | 0.4261 | 0.4242 |
| final_step_loss | 0.2442 | 0.2571 |
| token_accuracy | 0.9123 | 0.9040 |
| train_steps | 1635 | 1635 |
| epochs | 3.0 | 3.0 |
| duration | 56.96 min | 57.17 min |
| data_count | 4358 | 4358 |
| memory | 18.0 GiB | 17.55 GiB |
| checkpoint | `checkpoint-1635` (3 saves: 545/1090/1635) | `checkpoint-1635` (3 saves: 545/1090/1635) |

无异常，无 warning（bitsandbytes libnvJitLink 警告为非关键，不影响训练）。两个实验 loss 和 token_acc 非常接近，Random 的 token_accuracy 略高（0.912 vs 0.904）。

---
