# code synthetic depth scores 20260522

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_synthetic_depth_scores_20260522_20260522T051326_result.json`
- **Structured JSON:** [`129c52c1672db38fde6a.json`](../../sessions/12/129c52c1672db38fde6a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。全部信息汇总如下：

---

```
== 原始 importance scores 格式 ==
文件: importance_scores_qwen_math_7b.pt
Keys: [attn_importance, mlp_importance]
attn_importance: dict{0..27} → tensor shape=[4], per-layer GQA group scores
mlp_importance: dict{0..27} → tensor shape=[28], per-layer MLP group scores

== 合成 scores 设计 ==
Layer 0-9  (early): score = 1.0    → 保留
Layer 10-17 (mid):  score = 0.5    → 视剪枝比例决定
Layer 18-27 (late): score = 0.001  → 优先剪枝

== 生成验证 ==
synthetic_depth_scores.pt: OK (westd-32935:/root/autodl-tmp/recovery_aware_struct_prune/)
  attn: 28 layers × shape=[4], range=[0.001, 1.0]
  mlp:  28 layers × shape=[28], range=[0.001, 1.0]

== prune 命令模板 (westd-32935) ==
python src/prune.py \
  --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B \
  --importance_path /root/autodl-tmp/recovery_aware_struct_prune/synthetic_depth_scores.pt \
  --mode standard \
  --sparsity 0.2 \
  --output_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_depth_first_20
```

---
