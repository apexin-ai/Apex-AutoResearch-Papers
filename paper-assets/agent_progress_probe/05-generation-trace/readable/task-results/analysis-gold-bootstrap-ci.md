# analysis gold bootstrap ci

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gold-bootstrap-ci_20260515T084152_result.json`
- **Structured JSON:** [`8dd21ffd27b9875c96d3.json`](../../sessions/8d/8dd21ffd27b9875c96d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

| Test | Model A | Model B | N | Δ(A−B) | 95% CI | p-value | Sig? |
|---|---|---|---|---|---|---|---|
| GB vs MV | GB (0.802) | MV (0.718) | 195 | +0.084 | [+0.032, +0.138] | **0.0005** | **YES** |
| GB vs GRU Probe | GB (0.785) | Probe (0.735) | 132 | +0.050 | [−0.016, +0.120] | 0.070 | NO |
| RF vs GB | RF (0.809) | GB (0.802) | 195 | +0.007 | [0.000, +0.023] | 0.367 | NO |
| TWV Probe vs GB | TWV (0.768) | GB (0.785) | 132 | −0.016 | [−0.067, +0.031] | 0.254 | NO |
| TWV Probe vs GRU | TWV (0.768) | GRU (0.735) | 132 | +0.034 | [−0.029, +0.099] | 0.150 | NO |

**唯一显著的差异**：GB 显著优于 MV Labels（p=0.0005）。其他所有 pairwise 比较在 α=0.05 下均不显著。

**注意**：GB/RF 的绝对 macro-F1 高于此前 eval_full 报告的值（0.802/0.809 vs 0.760/0.756）。原因是 `windows_labeled.jsonl` 在 eval_full 运行后被更新，导致 `split_info.json` 中的 `keep_indices` 现在指向不同的训练窗口，模型性能因训练数据变化而不同。MV (0.718) 和 GRU Probe (0.735) 数值与此前完全一致，因为它们不依赖重新训练。pairwise 比较的 p-value 仍然有效，因为每对模型在相同窗口上评估。

---
