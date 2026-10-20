# analysis counterfactual spatial

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_counterfactual_spatial_20260520T213636_result.json`
- **Structured JSON:** [`c3fa125f4ca9e6edf65b.json`](../../sessions/c3/c3fa125f4ca9e6edf65b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

---

## 结构化总结

**Conclusion: SUCCESS**

### 核心 Metrics

| Condition | Cohen's d | Cross-task (mean±std) | CV |
|-----------|-----------|----------------------|------|
| empty | 0.942 | 0.954 ± 0.176 | 0.185 |
| wrong | 0.851 | 0.853 ± 0.079 | 0.093 |
| shuffled | 0.833 | 0.839 ± 0.139 | 0.166 |
| paraphrased | 0.806 | 0.809 ± 0.104 | 0.128 |

所有条件 d > 0.8，所有 p = 0。10 个 task 全部 d > 0.6，wrong 条件 CV=0.093（跨 task 极其一致）。

### 与 Parent（counterfactual_10tasks, LIBERO-Goal）对比

| Condition | Goal d | Spatial d | Δ |
|-----------|--------|-----------|--------|
| empty | 0.978 | 0.942 | −0.036 |
| wrong | 0.924 | 0.851 | −0.073 |
| shuffled | 0.763 | 0.833 | +0.070 |
| paraphrased | 0.707 | 0.806 | +0.099 |

- **wrong** 从 0.924 降至 0.851：符合预期，Goal 的 wrong 包含 task-identity + spatial 两个信号，Spatial 的 wrong 只有 spatial preposition 差异。剩余 d=0.851 即**纯空间语义敏感度**。
- **shuffled/paraphrased** 在 Spatial 上反而更高，说明空间介词的语序/同义替换对模型影响更大（空间词汇的冗余度低于动作/物体词汇）。

### Hypothesis 判断

Hypothesis 成立：仅替换空间介词（同一物体、同一动作）即产生 d=0.851 的大效应，且 10 个空间配置全部一致。Instruction-dominant heads 确实路由了 fine-grained spatial information，而非仅仅 task identity。

---
