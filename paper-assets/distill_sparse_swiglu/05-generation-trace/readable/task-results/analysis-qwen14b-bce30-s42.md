# analysis qwen14b bce30 s42

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen14b_bce30_s42_20260517T155633_result.json`
- **Structured JSON:** [`7a7b6fa141ce5e3bd1bb.json`](../../sessions/7a/7a7b6fa141ce5e3bd1bb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All results collected. Here's the summary:

```
=== qwen14b_bce30_s42 ===
final_loss: 0.5561
final_bce_loss: 0.5324
actual_sparsity: 0.300 (model-level, TEAL global allocation)
constraint_satisfied: true
training_steps: 1000
checkpoint_path: /root/distill_sparse_swiglu/checkpoints/qwen14b_bce30_s42/predictor_bce.pt
ppl_dense: 5.18
ppl_predictor_hard_mask: 5.57
ppl_teal_sparse: 8.76
training_completed_normally: yes
log_tail (last 5 lines):
  [Step 980/1000] loss=0.5563 bce=0.5326 reg=0.0237 sparsity=0.064 lr=1.22e-06
  [Step 990/1000] loss=0.5571 bce=0.5334 reg=0.0237 sparsity=0.063 lr=3.05e-07
  [Step 1000/1000] loss=0.5561 bce=0.5324 reg=0.0236 sparsity=0.064 lr=0.00e+00
  BCE training complete: 1000 steps in 424.2s (0.42s/step)
  Saved checkpoint -> checkpoints/qwen14b_bce30_s42/predictor_bce.pt

=== kl30_s456_uniform_eval ===
wikitext2_ppl: 8.7947
arc_challenge_acc_norm: 0.4505
winogrande_acc: 0.6875
mmlu_acc: 0.4198
gsm8k_exact_match: 0.0758
actual_sparsity: 0.301 (uniform per-layer, all 32 layers identical)
```

**Notes:**
- qwen14b training log 中 `sparsity` 列 (~0.064) 是训练过程中 predictor 的 regularization diagnostic，不是实际推理 sparsity。实际 TEAL global mask 在 eval 时确认为 model-level 0.300。
- Qwen-14B 使用非均匀分配：早期层高 sparsity (Layer 1: 0.917)，中间层低 (Layer 14: 0.078)，后期层递增 (Layer 47: 0.808)。
- kl30_s456_uniform_eval 使用 uniform 分配，所有 32 层均为 0.301。

---
