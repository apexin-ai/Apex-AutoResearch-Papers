# analysis eval pi05 random k085 object seed42 postfix

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_pi05_random_k085_object_seed42_postfix_20260524T042601_result.json`
- **Structured JSON:** [`b087943776d8eaacdf11.json`](../../sessions/b0/b087943776d8eaacdf11.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

```
total_episodes: 500
total_successes: 28
success_rate: 5.6%
per_task: [6%, 2%, 2%, 2%, 12%, 8%, 4%, 8%, 4%, 8%]
conclusion: negative — disruption peak 是真实现象，非 RNG bug
```

**关键发现：** Post-fix (5.6%) 与 pre-fix (5.0%) 基本一致，+0.6pp 在噪声范围内 (binomial SE ~1pp)。CPU RNG fix 没有改变结果。

**这意味着：**
- k=0.85 random pruning 在 Object suite 上的极端退化 (~94pp drop) 是**真实的 disruption peak**
- L2-norm 同样 k=0.85 保持 99.0%，说明 importance-based 选择在此区间至关重要
- Object suite 对 random token removal 的敏感度远超 Goal (52.4%) 和 Spatial (56.6%)

产出已写入 `artifacts/eval_pi05_random_k085_object_postfix_results.md` 并注册到 manifest。

---
