# analysis r22 cpu analyses corrected

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r22_cpu_analyses_corrected_20260519T183833_result.json`
- **Structured JSON:** [`d53b7f5d7168138b6780.json`](../../sessions/d5/d53b7f5d7168138b6780.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个分析完成，结果已保存。

### A1: FP8 count_16 BCS Δ noise propagation CI

| 指标 | 值 |
|------|-----|
| low-BCS mean acc | 70.83% |
| high-BCS mean acc | 59.90% |
| **Δ (low − high)** | **+10.94pp** |
| noise σ | 0.88pp per batch |
| **95% CI** | **[+9.84, +12.02]pp** |
| CI excludes zero | **Yes** |

即使考虑 FP8 greedy decoding 噪声（σ=0.88pp），count_16 的 BCS gap 仍然稳健，CI 完全在零以上。Bootstrap std 仅 0.56pp，噪声对 Δ 的影响很小。

### A3: Fisher z-test 同源基线修正

找到 **10 个相同 type sets** 同时在 constrained 和 unconstrained decoding 下有结果：

| 条件 | Pearson r | Spearman ρ | n |
|------|-----------|------------|---|
| Constrained (count_8) | −0.332 (p=0.35) | −0.079 | 10 |
| Unconstrained (matched 10) | −0.709 (p=0.02) | −0.152 | 10 |

| Fisher z-test | 值 |
|------|-----|
| **Fisher z** | **1.012** |
| **p** | **0.311** |
| Significant (α=0.05) | **No** |

关键发现：使用同源基线后，**constrained 和 unconstrained 的 BCS-accuracy 相关性差异不显著**（p=0.311）。这与之前用异源 ρ=-0.919 vs ρ=-0.139（p=2e-6）的结论完全不同。

值得注意的反转：同源对照下 unconstrained (r=−0.709) 反而比 constrained (r=−0.332) BCS-accuracy 相关更强，方向与预期相反。n=10 power 不足以做定论，但之前的 Fisher z 结果确实被 batch selection confound 严重放大了。

---
