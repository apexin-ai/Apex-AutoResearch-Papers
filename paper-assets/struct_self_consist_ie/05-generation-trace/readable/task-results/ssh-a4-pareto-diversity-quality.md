# ssh a4 pareto diversity quality

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_a4-pareto-diversity-quality_20260520T090124_result.json`
- **Structured JSON:** [`c12002243daf0c1fcfef.json`](../../sessions/c1/c12002243daf0c1fcfef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。输出文件：

- `artifacts/a4_pareto_diversity/pareto_plot.png` / `.pdf`
- `artifacts/a4_pareto_diversity/pareto_analysis.json`

**核心发现：**

| Config | 1−degen | Uniform ΔF1 | VC ΔF1 | Pareto? |
|--------|---------|-------------|--------|---------|
| T=0.7 | 0.777 | **+1.81** | +1.17 | Uniform only |
| T=0.8 | 0.819 | +1.25 | **+1.68** | VC only |
| Mix 0.7+1.0 | 0.830 | +1.43 | +1.67 | **Both** |
| T=1.0 | 0.877 | +0.75 | +1.21 | Both (highest diversity) |
| Mix 0.8+1.0 | 0.789 | −0.17 | +0.47 | **Dominated** |

1. **Mix 0.7+1.0 双 Pareto 最优**：well-separated temperatures 产生互补多样性，兼顾 diversity 和 quality
2. **VC construction 压平 trade-off**：VC Pareto 斜率比 Uniform 平缓 ~50%，diversity 代价更小
3. **Mix 0.8+1.0 被支配**：两个接近的 T 混合后 degeneracy 反而高于单一 T=0.8，construction 增益消失

---
