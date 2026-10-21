# analysis r5 first differencing sim

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r5_first_differencing_sim_20260520T204921_result.json`
- **Structured JSON:** [`dd8c3673faa33544e9b8.json`](../../sessions/dd/dd8c3673faa33544e9b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

### J2 First-Differencing Power Simulation (T=11, 1000 reps, 200 perms)

| Effect | β | Raw Power | Diff Power | Perm Power | Diff Loss | Perm Retention |
|--------|-----|-----------|------------|------------|-----------|----------------|
| Small | 0.1 | 0.117 | 0.075 | 0.087 | **35.9%** | 74.4% |
| Medium | 0.3 | 0.201 | 0.131 | 0.160 | **34.8%** | 79.6% |
| Large | 0.6 | 0.458 | 0.250 | 0.387 | **45.4%** | 84.5% |

**结论：First-differencing 在 T=11 下平均损失 39% 统计功效。Permutation Granger 保留了 80% 的 raw-levels 功效，无需差分。**

实证 DGP（a050_s42_fp32 token_entropy→perplexity）的 Cohen's f² = 4.81，远超 "large" 标准（0.35），说明我们实验中的因果信号极强，但 T=11 的短序列仍严重制约检验功效。

输出已保存到 `artifacts/j2_first_diff_power_simulation.json`。

---
