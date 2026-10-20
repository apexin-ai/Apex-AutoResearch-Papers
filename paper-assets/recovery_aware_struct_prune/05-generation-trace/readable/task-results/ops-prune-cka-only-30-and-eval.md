# ops prune cka only 30 and eval

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prune_cka_only_30_and_eval_20260517T214241_result.json`
- **Structured JSON:** [`6c56ff92c4d438f26793.json`](../../sessions/6c/6c56ff92c4d438f26793.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

关键发现。代码中的 RASP 评分公式（第 202 行）：

```
score = importance × (1 - overlap)^alpha
```

**`alpha=0` 不是 CKA-only**，而是 `importance × 1 = importance`，等价于 standard 模式。

importance 作为乘法因子始终存在，当前代码无法纯靠参数组合得到 CKA-only scoring。

汇报结果：

1. **支持的 mode**: `standard`, `rasp`, `rasp-rlvr`（无 `cka_only`）
2. **评分公式**:
   - `rasp`: `I(h) × (1 - F(h))^α` — alpha 控制 CKA 权重，但 I(h) 始终是乘数
   - `rasp-rlvr`: `I(h) × F(h)^α` — 反向 CKA
   - `standard`: 纯 `I(h)`
3. **alpha=0 → standard**，不是 CKA-only
4. **要实现 CKA-only**，需要以下之一：
   - 新增 mode，scoring 为 `(1 - F(h))^α`（去掉 importance 乘数）
   - 或构造全 1 的 dummy importance_scores.pt，配合 `--mode rasp --alpha 1`
5. **cuda:2 空闲**（0MiB, 0% util），随时可提交 eval
6. **importance_scores.pt 和 cka_scores.pt 均存在**于 `results/` 下

请决定下一步：改代码加 mode，还是用 dummy importance 绕过？

---
