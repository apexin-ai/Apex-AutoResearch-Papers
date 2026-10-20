# analysis c8 llama n250 metrics

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_c8_llama_n250_metrics_20260516T215823_result.json`
- **Structured JSON:** [`53adc3377fc15e93aa2c.json`](../../sessions/53/53adc3377fc15e93aa2c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。`c8_llama_n250_fixed` 已标记为 DONE，全部指标已写入 registry。

**汇总**：

| 条件 | median gradient | 95% CI | Wilcoxon p | Cohen's dz | Monotonic |
|------|----:|----:|----:|----:|:---:|
| imp s015 | 0.0501 | [0.0455, 0.0588] | 1.4e-29 | 0.81 | ✓ |
| imp s020 | 0.1587 | [0.1412, 0.1819] | 8.9e-35 | 1.01 | ✓ |
| imp s025 | 0.3761 | [0.3157, 0.4029] | 4.3e-39 | 1.12 | ✓ |
| imp s030 | 0.6954 | [0.6394, 0.7701] | 1.5e-40 | 1.15 | ✓ |
| rnd s015 | 0.0255 | [0.0199, 0.0333] | 9.3e-13 | 0.44 | ✓ |
| rnd s020 | 0.0650 | [0.0523, 0.0882] | 3.6e-15 | 0.46 | ✓ |
| rnd s025 | 0.1842 | [0.1127, 0.2471] | 3.8e-13 | 0.42 | ✓ |
| rnd s030 | 0.2707 | [0.1935, 0.3681] | 6.0e-12 | 0.41 | ✓ |

- Importance/Random ratio: **1.97x-2.57x**
- Dose-response: 两组均**单调递增**
- Hypothesis confirmed: importance-based 效应量 large (0.81-1.15), random medium (0.41-0.46)

---
