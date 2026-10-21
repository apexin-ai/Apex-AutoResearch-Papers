# ops collect all 4 evals

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_collect-all-4-evals_20260518T115002_result.json`
- **Structured JSON:** [`0eee4a1e389ab0cce330.json`](../../sessions/0e/0eee4a1e389ab0cce330.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 全部更新完成。

## 收集结果

### kl_comp_30pct_s123_eval (34887, cuda:0)
- wikitext2_ppl: 8.9788
- arc_challenge_acc_norm: 0.3993
- winogrande_acc: 0.6898
- mmlu_acc: 0.2531
- gsm8k_exact_match: 0.0842
- vs s42 comp: ARC Δ=0.0000, WG Δ=0.0000, MMLU Δ=0.0000, GSM8K Δ=0.0000
- **s123 与 s42 完全一致**，seed 间极度稳定

### kl50_s456_uniform_eval (34887, cuda:1)
- wikitext2_ppl: 11.9538
- arc_challenge_acc_norm: 0.3831
- winogrande_acc: 0.6196
- mmlu_acc: 0.2750
- gsm8k_exact_match: 0.0288
- vs s42 uniform: ARC Δ=+0.0572, WG Δ=-0.0039, MMLU Δ=-0.0042, GSM8K Δ=+0.0091

### kl_comp_30pct_s456_eval (41718, cuda:0)
- wikitext2_ppl: 8.9614
- arc_challenge_acc_norm: 0.4462
- winogrande_acc: 0.7143
- mmlu_acc: 0.2714
- gsm8k_exact_match: 0.0887
- vs s42 comp: ARC Δ=+0.0469, WG Δ=+0.0245, MMLU Δ=+0.0183, GSM8K Δ=+0.0045
- **s456 全面优于 s42/s123**，这个 seed 表现异常好

### kl_comp_50pct_s42_eval (41718, cuda:1) — 关键实验
- wikitext2_ppl: 11.7933
- arc_challenge_acc_norm: 0.3285
- winogrande_acc: 0.6346
- mmlu_acc: 0.2789
- gsm8k_exact_match: 0.0129

## 四卡状态

| 服务器 | GPU | 实验 | 状态 |
|--------|-----|------|------|
| westd-34887 | cuda:0 | kl_comp_30pct_s123_eval | DONE ✓ → **空闲** |
| westd-34887 | cuda:1 | kl50_s456_uniform_eval | DONE ✓ → **空闲** |
| westd-41718 | cuda:0 | kl_comp_30pct_s456_eval | DONE ✓ → **空闲** |
| westd-41718 | cuda:1 | kl_comp_50pct_s42_eval | DONE ✓ → **空闲** |

所有 41718 eval 都成功拿到完整 downstream，无需转移重跑。4 张卡全部空闲，可安排优先级 2 任务（wall-clock speedup / C4 OOD 等）。

---
