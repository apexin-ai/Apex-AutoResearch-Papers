# analysis kl30 s456 train and s123 eval

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_kl30_s456_train_and_s123_eval_20260517T133046_result.json`
- **Structured JSON:** [`e75fe9d4a0b9913a33a1.json`](../../sessions/e7/e75fe9d4a0b9913a33a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== kl30_s456_train ===
Status: completed (EXIT_CODE=0)
Final Loss: 0.2021 (kl_norm)
Actual Sparsity: 28.9%
Constraint: 0.000000 (satisfied)
Checkpoint exists: yes (152MB, 2026-05-17 21:28)
Checkpoint path: /root/distill_sparse_swiglu/checkpoints/kl_30pct_s456/predictor_kl_normalized.pt
Note: 训练日志无 validation PPL — 这是 predictor 训练，PPL 需单独 eval

=== kl30_s123_eval (uniform allocation) ===
Status: completed (EXIT_CODE=0)
PPL (wikitext2): 8.8308
ARC-Challenge: acc=0.4096, acc_norm=0.4531
WinoGrande: 0.6938
MMLU: 0.3944
GSM8K: 0.0751
Runtime: ~2155s (~36min)

=== 对比 ===
                s42 uniform    s123 uniform    delta
MMLU            0.4061         0.3944          -0.0117
PPL (wiki2)     —              8.8308          

MMLU vs s42 global (0.2527):  s123 uniform = +14.2pp gain ✓
```

s456 训练正常完成，sparsity 收敛到 ~29%（目标 30%），constraint 归零，checkpoint 已保存。需要单独跑 eval 才能拿到 s456 的 PPL。

s123 uniform eval 完成，MMLU=0.3944 比 s42 uniform 的 0.4061 低约 1.2pp，但相对 s42 global (0.2527) 仍有 +14.2pp 的显著提升，基本符合 hypothesis。

---
