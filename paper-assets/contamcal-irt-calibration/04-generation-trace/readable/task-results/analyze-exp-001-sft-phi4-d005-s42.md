# analyze exp 001 sft phi4 d005 s42

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_exp_001_sft_phi4_d005_s42_20260519T032309_result.json`
- **Structured JSON:** [`97cc5bc204a666ffe7b9.json`](../../sessions/97/97cc5bc204a666ffe7b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Phi-4 d005 SFT 分析摘要

| 指标 | d005 | d000 (baseline) | 差异 |
|------|------|-----------------|------|
| final_loss (avg) | 1.185 | 1.183 | +0.002 |
| mean_token_accuracy | 0.7302 | 0.7287 | +0.0015 |
| total_steps | 3177 | 3125 | +52 (数据量略多) |
| train_runtime | 9321s (~2h35m) | 7500s (~2h05m) | +1821s |
| W&B | 无 | - | - |

**结论：success。** 训练正常完成，`.done` sentinel 存在，adapter 文件完整（222MB safetensors + tokenizer + config）。Loss 和 accuracy 与 d000 几乎一致，符合 5% 低污染剂量的预期（污染比例太低，对训练损失无显著影响）。lora_alpha=32 确认合规。无 W&B 日志。

注册表已更新为 DONE/success，checkpoint_path 和 log_path 均已设置。

---
