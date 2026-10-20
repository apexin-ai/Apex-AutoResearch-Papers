# launch alpha3 pipeline westb1

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_launch_alpha3_pipeline_westb1_20260522T071018_result.json`
- **Structured JSON:** [`bc1571f1f8039c0a4e8a.json`](../../sessions/bc/bc1571f1f8039c0a4e8a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
== 1.5B RASP MATH-500 ==
Status: DONE
Accuracy: 6.2% (31/500) — registry updated (eval_math500_sft_rasp_20_1p5b, conclusion=negative)

== Scores 传输 ==
importance_scores.pt: 已存在 (17KB)
cka_scores.pt: 已存在 (122KB)

== DeepSeek 基础模型 ==
Path: /root/autodl-tmp/recovery_aware_struct_prune/models/DeepSeek-R1-Distill-Qwen-7B
(已下载 via ModelScope, 14.3GB, 已删除释放空间给 pipeline)

== α=3.0 Pipeline ==
PID: 162174 on GPU 1
Stage: SFT (prune完成, 19.09% actual sparsity, 0 attn + 200 MLP groups pruned, 6.16B params)
30s check: GPU 1 加载中 (SFT loading pruned model), 22GB disk free
Log: /tmp/alpha3p0_pipeline.log
```

Pipeline stages: prune ✓ → SFT (running) → GRPO (100 steps) → GSM8K eval (GRPO) → GSM8K eval (SFT)

---
