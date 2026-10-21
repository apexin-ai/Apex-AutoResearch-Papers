# analysis llama32 3B d025 sft

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_llama32_3B_d025_sft_20260516T174920_result.json`
- **Structured JSON:** [`371e17862e7040eebf5c.json`](../../sessions/37/371e17862e7040eebf5c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。摘要：

| 项目 | 值 |
|------|-----|
| **Checkpoint** | `/root/autodl-tmp/exp001/checkpoints/Llama-3.2-3B_d025_s42/merged/` (2 shards, ~6.4GB) |
| **LoRA adapter** | `/root/autodl-tmp/exp001/checkpoints/Llama-3.2-3B_d025_s42/lora_adapter/` |
| **训练 loss** | 2.385 → 1.454 (avg 1.527) |
| **Mean token accuracy** | 0.525 → 0.675 |
| **Steps / Epoch** | 3384 / 1 |
| **训练时间** | 8349s ≈ 2h19m (2.32 GPU-hours) |
| **配置** | LoRA r=16, alpha=32, lr=5e-5, batch=2×8, seq_len=2048, 54133 samples |
| **日志** | `~/runs/contamcal-irt-calibration/exp_001_sft_llama32_3B_d025_s42.log` |

注：eval 实验 `exp_001_eval_llama32_3B_d025_s42` 已在 PREPARING 状态，MMLU 结果已产出（`eval_results/Llama-3.2-3B_d025_s42_aligned/mmlu_results.json`），其余 benchmark 评估进行中。

---
