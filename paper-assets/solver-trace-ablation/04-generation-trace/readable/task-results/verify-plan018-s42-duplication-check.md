# verify plan018 s42 duplication check

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_plan018-s42-duplication-check_20260514T095924_result.json`
- **Structured JSON:** [`28b0d0c57c00cb458d58.json`](../../sessions/28/28b0d0c57c00cb458d58.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**plan018 random β=0.1 s42: 零 premise-conclusion duplication**

| 指标 | 值 |
|------|-----|
| Total / Proved | 100 / 79 (PR=0.79) |
| Single premise | **0/79 (0.0%)** |
| Premise=Conclusion | **0/79 (0.0%)** |
| N_premises 分布 | 3-15，中位数 ~7，无退化到单 premise |

### 与 ISR 组对比结论

**Random reward 控制组完全没有 conclusion duplication hacking。** 所有 79 个 proved 样本的 premise 数量分布在 3-15 之间，没有任何样本退化为单 premise，更不存在 premise=conclusion 的情况。

这证实了 **conclusion duplication 是 ISR reward 特异性诱导的退化**，而非 GRPO 训练的通用现象：
- random β=0.1 s42: 0% duplication，premise 分布健康（3-15）
- ISR β=0.1 s43/s44（已知问题组）: 高比例 premise=conclusion hacking

模型在 random reward 下没有动机去简化 formalization 结构，因为随机 reward 不会系统性地奖励 premise-conclusion 重复。ISR reward 则因为 "premise ⊂ conclusion → 必然 necessary" 的捷径而诱导了这种退化。

---
