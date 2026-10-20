# experiment feature overlap lf only

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_feature-overlap-lf-only_20260515T031743_result.json`
- **Structured JSON:** [`eda0475d6ea76cff6d0c.json`](../../sessions/ed/eda0475d6ea76cff6d0c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。3 行对比表 (GB):

| Feature Set | #Feat | In-Dom. macro_F1 | Cross-Ag. macro_F1 |
|---|---|---|---|
| Full (all 30) | 30 | 0.9951 | 0.9674 |
| **LF-overlap only** | **11** | **0.9937** | **0.9770** |
| Residual only | 19 | 0.9515 | 0.5656 |

关键发现：11 个 LF-overlap 特征**单独**就能达到 cross-agent 0.977，甚至高于 full 30 的 0.967（+1.0pp）。而 19 个 residual 特征 cross-agent 仅 0.566。这说明 cross-agent 泛化能力几乎完全来自 LF-overlap 特征，residual 特征不仅没有帮助，反而在 full 模型中引入了噪声，轻微拖累了跨 agent 性能。

验证一致性：full_30 和 residual_19 的数字与原始 ablation 完全匹配。

---
