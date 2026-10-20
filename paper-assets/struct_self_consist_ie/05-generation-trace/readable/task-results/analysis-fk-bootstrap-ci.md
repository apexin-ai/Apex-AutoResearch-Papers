# analysis fk bootstrap ci

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fk_bootstrap_ci_20260515T124826_result.json`
- **Structured JSON:** [`7df79f29cc8476d26b52.json`](../../sessions/7d/7df79f29cc8476d26b52.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果已保存到 `output/analysis_fk_bootstrap_ci.json`。

## 结果摘要

### SciERC NER (Qwen, 3 seeds, n=529)

| 比较 | seed42 | seed123 | seed456 |
|------|--------|---------|---------|
| **SJ - FK** | +0.147 CI[+0.07,+0.22] p=0.002** | +0.149 CI[+0.08,+0.22] p=0.001** | +0.160 CI[+0.08,+0.24] p=0.001** |
| **VC - FK** | +0.160 CI[+0.06,+0.26] p=0.001** | +0.138 CI[+0.04,+0.23] p=0.003** | +0.188 CI[+0.08,+0.29] p<0.001*** |
| EM - FK | +0.054 CI[-0.04,+0.15] n.s. | +0.062 CI[-0.03,+0.16] n.s. | +0.093 CI[-0.01,+0.19] p=0.048* |

### CoNLL NER (Qwen, n=2756)
| 比较 | delta | CI | p_perm |
|------|-------|----|----|
| **SJ - FK** | +0.056 | [+0.04, +0.07] | <0.001*** |
| VC - FK | +0.022 | [-0.00, +0.05] | 0.040* |
| **EM - FK** | +0.071 | [+0.05, +0.09] | <0.001*** |

### 关键发现
1. **SJ 和 VC 显著优于 FK**：在 SciERC NER 3 个 seed 中一致显著（p<0.003），delta 约 0.14-0.19
2. **EM vs FK 边界**：SciERC 上不显著（2/3 seeds），但 CoNLL 上高度显著（delta=0.07, p<0.001）
3. **RE 例外**：SciERC RE 中 FK 与其他信号无显著差异，甚至 FK > EM
4. **LLaMA CoNLL**：信号差异缩小（FK≈0.475 vs SJ≈0.484），但 SJ 和 EM 仍显著优于 FK
5. Bootstrap CI 和 permutation test 结论高度一致，互为 robustness check

---
