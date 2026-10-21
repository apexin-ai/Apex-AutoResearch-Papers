# analysis gating bootstrap ci

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gating_bootstrap_ci_20260519T101033_result.json`
- **Structured JSON:** [`aa10c186800fe54186f6.json`](../../sessions/aa/aa10c186800fe54186f6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果汇总：

### Bootstrap CI (B=1000)

| 数据集 | mean ρ | 95% CI(ρ) | adjusted | 95% CI(adj) | routing |
|--------|--------|-----------|----------|-------------|---------|
| SciERC | 0.214 | [0.146, 0.281] | 0.167 | [0.116, 0.220] | **greedy** |
| CoNLL | 0.294 | [-0.061, 0.620] | 0.065 | [-0.009, 0.156] | **greedy** |
| FewNERD | 0.615 | [0.459, 0.759] | 0.516 | [0.374, 0.648] | **LP** |

### Threshold 敏感性
- Routing decisions 在 **τ∈[0.2, 0.4] 全范围一致**（SciERC/CoNLL 始终 greedy，FewNERD 始终 LP）
- Robust range（all stability ≥ 95%）：**τ ∈ [0.25, 0.35]**，τ=0.3 正好居中

### Greedy Fallback
- CoNLL 78% degeneracy → 样本几乎相同，construction 无新实体可聚合 → greedy 是唯一合理选择
- SciERC 33% negative ρ → LP 不可靠
- FewNERD 仅 14.3% negative ρ，16% degeneracy → LP well-justified

结果保存在 `output/gating_bootstrap/gating_analysis.json`（服务器端）和 artifact `gating_bootstrap_analysis`，memory.md 已更新。

---
