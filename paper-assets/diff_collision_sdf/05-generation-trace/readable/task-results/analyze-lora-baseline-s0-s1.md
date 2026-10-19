# analyze lora baseline s0 s1

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_lora_baseline_s0_s1_20260526T013600_result.json`
- **Structured JSON:** [`34e4ca171cd0a9cfdf67.json`](../../sessions/34/34e4ca171cd0a9cfdf67.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 LoRA baseline 实验均已完成，registry 已更新为 DONE/success。

## 汇总

| | seed0 | seed1 |
|---|---|---|
| **总 steps** | 30,000 | 30,000 |
| **最终 loss** | 0.01343 | 0.01408 |
| **best loss** | 0.01025 @ step 24000 | 0.01130 @ step 14000 |
| **grad_norm** | 0.10538 | 0.10628 |
| **time/step** | 4.61s | 4.62s |
| **resume2 耗时** | 7h43m | 7h43m |
| **30K checkpoint** | `.../pi05_lora_baseline_object_pudding_seed0/30000` | `.../pi05_lora_baseline_object_pudding_seed1/30000` |
| **best checkpoint** | `.../seed0/best` (step 24000) | `.../seed1/best` (step 14000) |

两个实验无报错，进度条到 100%，checkpoint 30000 和 best 均存在。W&B offline 日志已保存。可用于后续 eval 对照。

---
