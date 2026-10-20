# analysis llama docred bootstrap recompute

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_llama-docred-bootstrap-recompute_20260523T110303_result.json`
- **Structured JSON:** [`197df972845b89c863df.json`](../../sessions/19/197df972845b89c863df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Bootstrap CI and Cohen's d 已经用修正后数据计算过。所有结果齐全：

```
=== Llama DocRED S1 Bootstrap Test (修正后) ===
DR Unconstrained: 0.49% (80/16171)
DR S1:            0.21% (33/16074)
ΔDR:              -0.29 pp (↓57%)
p-value:          0.0001
95% CI of ΔDR:    [-0.53, -0.10] pp
Cohen's d:        -3.02 (large)
Bonferroni p:     0.0004 (k=4)

结论: p<0.001 成立 ✓
```

**Appendix 验证结果:**

`appendix_discussion.tex` 第193行 Llama DocRED DR% reduction 行：
```
Llama-3.1-8B & DocRED & -0.29 & [-0.53, -0.10] & <.001 & -3.02
```

逐项对比 `r20_cohens_d_pvalues.json`：
| 指标 | 表中 | 计算值 | 匹配 |
|------|------|--------|------|
| ΔDR | -0.29 | -0.2894 | ✓ |
| CI lower | -0.53 | -0.5336 | ✓ |
| CI upper | -0.10 | -0.1000 | ✓ |
| p | <.001 | 0.0001 | ✓ |
| d | -3.02 | -3.0191 | ✓ |

**Appendix 已基于修正后数据更新，无需修改。** 论文 §5.1 "all DR reductions are (p<0.001)" 的 claim 对 Llama DocRED ↓57% 依然成立（p=0.0001, |d|=3.02, p_Bonf=0.0004 < 0.005）。

---
