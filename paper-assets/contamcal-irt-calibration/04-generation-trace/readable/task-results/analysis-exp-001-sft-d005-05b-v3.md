# analysis exp 001 sft d005 05B v3

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_001_sft_d005_05B_v3_20260514T005659_result.json`
- **Structured JSON:** [`bf32a754221e9439e77c.json`](../../sessions/bf/bf32a754221e9439e77c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验 `exp_001_sft_d005_05B_v3` 分析完成，registry 已更新为 DONE/success。

**结果摘要：**

| 指标 | 5% dosage | 0% baseline | delta |
|------|-----------|-------------|-------|
| final_loss | 1.478 | 1.4894 | **-0.011** |
| mean_train_loss | 1.5424 | 1.5388 | +0.004 |
| token_accuracy | 0.667 | 0.682 | **-0.015** |
| training_time | 56.1 min | 52.9 min | +3.2 min |

5% contamination dosage 与 0% baseline 的训练指标差异很小：final loss 略低，mean loss 和 token accuracy 基本持平。这符合预期——低剂量污染对训练 loss 的影响微乎其微，真正的差异应体现在 eval 阶段的 benchmark accuracy 上。

---
