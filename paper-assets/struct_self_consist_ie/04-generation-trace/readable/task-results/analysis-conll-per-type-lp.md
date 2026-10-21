# analysis conll per type lp

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_conll_per_type_lp_20260517T044124_result.json`
- **Structured JSON:** [`0648b3ee2e8d8ac4ea55.json`](../../sessions/06/0648b3ee2e8d8ac4ea55.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果总结

数据来源: `exp_002_conll_n16_r1024/samples.jsonl` (3453 instances, N=16 samples, 2756 有 gold entities)

| Type | N | Degen% | Greedy F1 | LP Sel F1 | Δ(pp) | LP ρ | Headroom |
|------|--:|-------:|----------:|----------:|------:|-----:|---------:|
| MISC | 341 | 23.2% | 0.7879 | 0.7659 | **-2.19** | 0.270 | 12.57pp |
| PER | 791 | 42.6% | 0.9375 | 0.9267 | -1.08 | 0.334 | 4.11pp |
| LOC | 661 | 47.5% | 0.9061 | 0.8999 | -0.62 | 0.319 | 3.97pp |
| ORG | 963 | 54.3% | 0.9247 | 0.9192 | -0.55 | 0.368 | 3.80pp |

**关键发现：**

1. **LP selection 在所有 4 个 type 上全面失败**，全部 Δ 为负。
2. **MISC 是最有趣的反例**：degeneracy 最低 (23.2%)，headroom 最大 (12.57pp)，即有充足的多样性和改进空间，但 LP selection 反而最差 (-2.19pp)。说明即使去掉 degeneracy 的影响，LP 仍然是 anti-signal。
3. **因果分析呈现反直觉的 ρ=1.000**：degeneracy 越低 → LP delta 越差。这意味着不是 degeneracy 压制了 LP，而是 LP 本身在 non-degenerate instances 上选得更差（MISC 的 LP ρ=0.270 最低，弱正相关不足以做出正确选择）。

输出文件：
- CSV: `exp_002_conll_n16_r1024/per_type_lp_analysis.csv`
- LaTeX: `exp_002_conll_n16_r1024/per_type_lp_table.tex`

---
