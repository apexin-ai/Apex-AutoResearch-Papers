# analysis exp 001 sft 14b d100 s42

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_001_sft_14b_d100_s42_20260519T002054_result.json`
- **Structured JSON:** [`0887d8b42c497a78ec34.json`](../../sessions/08/0887d8b42c497a78ec34.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 14B d100 s42 训练结果

| 项目 | 值 |
|---|---|
| **结论** | **SUCCESS** |
| .done | 存在 |
| total_steps | 4159/4159 (100%) |
| epoch | 1.0 |
| final_loss | ~1.000 (step 4150) |
| final_token_accuracy | ~0.753 (step 4150) |
| lora_alpha | 32 (符合规范) |
| lora_r | 16 |
| lr | 5e-5 |
| num_samples | 66,533 |
| batch_size | 1 × grad_accum 16 |
| adapter 大小 | 275MB |

训练正常完成，loss 在 0.94–1.06 区间波动，token accuracy 稳定在 0.75 附近，lr 已衰减至接近零。

---
