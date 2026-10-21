# analysis 72b fewnerd construction

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_72b_fewnerd_construction_20260519T142544_result.json`
- **Structured JSON:** [`94b87ef09a4533fb844a.json`](../../sessions/94/94b87ef09a4533fb844a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新（含三个数据集完整 metrics）。

## 总结

**FewNERD 72B ZS construction 全面失败**：LP-weighted -0.20pp, θ=2/N -1.70pp, LP selection -0.40pp。所有 consensus variant 阈值组合也均为负。

72B ZS 三数据集 construction 全景：

| Dataset | Degen | LP ρ | LP-wt ΔF1 | θ=2/N ΔF1 |
|---|---|---|---|---|
| **SciERC** | 21.0% | 0.081 | **+1.53pp** ✓ | -0.52pp |
| **FewNERD** | 46.2% | 0.119 | **-0.20pp** ✗ | -1.70pp |
| **CoNLL** | 67.7% | -0.002 | -0.37pp | -0.92pp |

**Pattern 清晰**：degeneracy 是 construction 成败的决定因素。SciERC (degen=21%) 成功，FewNERD (46%) 和 CoNLL (68%) 失败。LP ρ 正面（FewNERD 0.119 > SciERC 0.081）不足以抵消高 degeneracy 的破坏性——这直接支持论文 "degeneracy gates construction" 的 narrative。

---
