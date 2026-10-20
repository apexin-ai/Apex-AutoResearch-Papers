# analysis entity construction fair n8

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_entity_construction_fair_n8_20260519T023154_result.json`
- **Structured JSON:** [`51b42927769b9758f9cd.json`](../../sessions/51/51b42927769b9758f9cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

### N=8 Entity Construction Fair Evaluation

| Dataset | Method | ΔF1 vs Greedy | 95% CI | p-value | Sig? |
|---------|--------|--------------|--------|---------|------|
| **SciERC** | Uniform Confirm (θ=2/N) | **+1.54pp** | [+0.03, +3.12] | 0.023 | **YES** |
| | LP-w Confirm | **+1.67pp** | [+0.37, +3.03] | 0.004 | **YES** |
| | LP-w CV | **+1.25pp** | [-0.09, +2.68] | 0.035 | **YES** |
| | Uniform CV | +1.12pp | [-0.29, +2.61] | 0.057 | no |
| **CoNLL** | Uniform CV | -0.39pp | [-0.83, +0.04] | 0.963 | no |
| | LP-w CV | -0.39pp | [-0.83, +0.04] | 0.963 | no |
| | All others | negative | — | — | no |
| **FewNERD** | LP-w Confirm | **+0.88pp** | [+0.67, +1.09] | 0.000 | **YES** |
| | LP-w CV | **+0.88pp** | [+0.67, +1.09] | 0.000 | **YES** |
| | Uniform Confirm (θ=2/N) | **+0.32pp** | [+0.08, +0.56] | 0.003 | **YES** |
| | Uniform CV | **+0.32pp** | [+0.08, +0.56] | 0.003 | **YES** |

**与 N=16 对比要点：**
- **SciERC**: N=8 的 confirm (θ=0.25) 比 N=16 (θ=0.125) 效果更好（+1.54pp vs N=16 的 +0.28pp），3 个方法显著
- **CoNLL**: N=8 和 N=16 一样，construction 都不显著优于 greedy（greedy baseline 本身就很高 ~90.8%）
- **FewNERD**: N=8 的 LP-weighted 方法高度显著（p≈0），但 ΔF1 绝对值比 N=16 小（+0.88pp vs N=16 的 +1.42pp）

结果已保存到 `output/entity_construction_fair_n8/fair_results.json` 和 `bootstrap_tests.json`。

---
