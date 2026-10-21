# analyze exp 001 sft phi4 d050 s42

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_exp_001_sft_phi4_d050_s42_20260519T063248_result.json`
- **Structured JSON:** [`80059abc79768e3c9c24.json`](../../sessions/80/80059abc79768e3c9c24.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated to DONE/success. Summary:

| Metric | d000 | d005 | d025 | **d050** |
|---|---|---|---|---|
| train_loss | 1.183 | 1.185 | 1.187 | **1.189** |
| final_step_loss | — | — | 1.139 | **1.117** |
| final_step_accuracy | — | — | 0.7329 | **0.7414** |
| mean_token_accuracy | 0.7287 | 0.7302 | — | **0.7253** |
| total_steps | 3125 | 3177 | 3384 | **3642** |

- **train_loss 1.189** — 与 dosage chain 完全一致（随 dosage 缓慢上升）
- **train_runtime** ~3h03m (11,000s)
- **lora_alpha=32** 确认正确
- Checkpoint: `/root/autodl-tmp/exp001/checkpoints/phi-4_d050_s42/lora_adapter`
- 无 W&B run，无 eval metrics
- Steps 从 d000 的 3125 增长到 3642，因为 d050 数据量更大 (58,266 samples)

---
