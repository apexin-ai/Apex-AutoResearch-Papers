# analysis reward diag v2

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_reward_diag_v2_20260513T031210_result.json`
- **Structured JSON:** [`fa541e43535096aab213.json`](../../sessions/fa/fa541e43535096aab213.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。

## reward_diag_v2 结果汇报

### v1 vs v2 对比表

| 分量 | v1 mean | v1 std | v2 mean | v2 std | 变化 |
|------|---------|--------|---------|--------|------|
| Composite (0.4p+0.4s+0.2f) | 0.646 | 0.136 | 0.647 | 0.138 | ≈不变 |
| Provenance Fidelity | 0.547 | 0.172 | 0.546 | 0.173 | ≈不变 |
| Structural F1 | 0.569 | 0.223 | 0.571 | 0.226 | ≈不变 |
| Format Compliance | 1.000 | 0.000 | 1.000 | 0.000 | 不变 |

### 关键结论

**Provenance std = 0.173 >> 0.05，未饱和。** 三个有效分量（provenance, structural）在 v5 输出上的分布与 v4 几乎完全一致。

这意味着：
- v4→v5 的 AP 提升（0.51→0.95）主要是**格式修复**（thinking mode 污染消除），reward 函数对内容质量的评分本身没有受模板问题影响
- **grpo_pilot_v2 的 weight 配置可以沿用原方案**：format_weight=0.05（已饱和），provenance/structural 各 0.475
- GRPO 有充足的学习信号——composite top10-bottom10 gap = 0.489，provenance gap = 0.647，structural gap = 0.772

---
