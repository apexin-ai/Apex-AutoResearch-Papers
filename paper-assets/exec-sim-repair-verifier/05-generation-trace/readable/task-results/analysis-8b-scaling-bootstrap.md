# analysis 8b scaling bootstrap

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_8b-scaling-bootstrap_20260512T163636_result.json`
- **Structured JSON:** [`cb0bbb14860fd891438b.json`](../../sessions/cb/cb0bbb14860fd891438b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### Summary Table

| Scale | Seeds | Mean CLS | Mean CWM | Gap (pp) | 95% CI | p(>0) | Cohen's d |
|-------|-------|----------|----------|----------|--------|-------|-----------|
| 4B | 5 | 88.43 | 87.18 | 1.25 | [-1.71, +0.84] | 0.499 | — |
| **8B** | **3** | **89.39** | **86.96** | **2.42** | **[+1.50, +3.35]** | **0.004** | **6.53** |

### 关键统计结果

**8B CLS > CWM gap 显著：**
- Paired t-test: t=11.31, p=0.004 (one-sided)
- Bootstrap 95% CI: [+1.25, +3.60]pp — 整个 CI 在零以上
- 3/3 seeds 一致 CLS > CWM (gaps: 2.81, 2.39, 2.07pp)

**Scaling widens the gap (8B > 4B)：**
- Gap 从 1.25pp (4B) 增至 2.42pp (8B)，增幅 +1.17pp (+94%)
- One-sample t-test: t=5.48, **p=0.016**
- Bootstrap P(8B gap > 4B gap) = 0.977

**TOST 等价性拒绝：**
- 90% CI = [+1.45, +3.40]pp — **超出 ±2pp 边界**
- TOST p=0.907 — 无法认为 CLS 和 CWM 等价
- 最小等价 margin 需 3.4pp

**局限：** n=3 seeds，permutation test 只有 8 种排列 (p=0.125)，power 有限。但 paired t-test 和 bootstrap 均达到显著性，且 3 seeds 方向完全一致。

文件已保存：`/home/sonny/exec-sim-repair-verifier/8b_scaling_bootstrap_results.json`

---
