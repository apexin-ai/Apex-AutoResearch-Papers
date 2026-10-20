# ops transfer scores westd 20260522

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_transfer_scores_westd_20260522_20260522T051106_result.json`
- **Structured JSON:** [`3c8a022c9743a5216790.json`](../../sessions/3c/3c8a022c9743a5216790.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**无需中转。westd-32935 已有 7B DeepSeek scores。**

```
== 找到的 scores 文件 ==
westb: /root/recovery_aware_struct_prune/results/{importance_scores,cka_scores}.pt (17KB, 122KB)
westd: /root/recovery_aware_struct_prune/results/{importance_scores,cka_scores}.pt (17KB, 122KB, 同大小)

== 7B DeepSeek scores ==
importance: /root/recovery_aware_struct_prune/results/importance_scores.pt ✓ (28层×4 KV groups)
cka: /root/recovery_aware_struct_prune/results/cka_scores.pt ✓ (28层, keys=attn_overlap/mlp_overlap/attn_cka_matrix)

== 中转状态 ==
无需传输 — westd-32935 已有完整文件

== 验证 ==
westd importance_scores: OK (weights_only=True 加载成功)
westd cka_scores: OK (weights_only=True 加载成功)
```

---
