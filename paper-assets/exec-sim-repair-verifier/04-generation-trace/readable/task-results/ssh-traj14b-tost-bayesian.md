# ssh traj14b tost bayesian

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_traj14b-tost-bayesian_20260523T111150_result.json`
- **Structured JSON:** [`1ebd68946462ffec4012.json`](../../sessions/1e/1ebd68946462ffec4012.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## CLS vs TRAJ 14B 统计检验结果

### TOST (±2pp SESOI, clustered bootstrap)
- Method: Problem-level paired comparison (114 共享 problem_ids × 3 seeds = 342 obs)
- Observed mean diff (CLS−TRAJ): **+0.619pp**
- 95% CI: [−0.965, +2.189]pp
- TOST p-value (raw): **0.0431** → **Equivalent: YES**
- Min margin for equiv: 1.941pp (非常接近 2pp 阈值)

注意：seed-level parametric TOST (n=3) 给出 p=0.1874（underpowered），但 clustered bootstrap 利用了 114 个 cluster 的信息量。

### Bayesian ROPE (±2pp)
| Metric | Bootstrap | Parametric (seed-level) |
|--------|-----------|------------------------|
| P(ROPE) | **95.62%** | 74.29% |
| P(CLS better) | 4.31% | — |
| P(TRAJ better) | 0.07% | — |
| 95% HDI | — | [−4.42, +5.66]pp |

Bootstrap ROPE 强支持等价；parametric 因 n=3 不确定。

### Holm-Bonferroni (4 func-level equivalence tests)
| Rank | Comparison | Raw p | × | Adj p | Sig? |
|------|-----------|-------|---|-------|------|
| 1 | CLS-CWM 14B (3 seeds) | 0.0006 | ×4 | 0.0024 | YES |
| 2 | CLS-CWM 8B (5 seeds) | 0.007 | ×3 | 0.021 | YES |
| 3 | CLS-TRAJ 8B (5 seeds) | 0.025 | ×2 | 0.050 | NO |
| 4 | CLS-TRAJ 14B (3 seeds) | 0.0431 | ×1 | 0.050 | NO |

CLS-TRAJ 在两个 scale 都 borderline（adj p=0.050），与 8B 一致——CLS-CWM 稳健通过，CLS-TRAJ 方向一致但 Holm 校正后不 confirmatory。

### Scaling trend (problem-level gap)
- 4B: 3.11pp → 8B: −0.45pp → 14B: **+0.62pp**
- Raw accuracy gap: 4B→8B→14B = 3.11→−0.45→+1.07pp

### 关键观察
1. 14B TOST raw p=0.0431 < 0.05，比 8B 的 p=0.025 更弱，但 bootstrap ROPE 95.62% 比 8B per-test 的 54.2% 大幅改善
2. Problem-level 聚合后 gap 缩小到 +0.62pp（vs raw +1.07pp），因为 equal-weight-per-problem 消除了样本量差异的影响
3. CLS-CWM 14B p=0.0006 极强，可作为 scaling 强化论据

---
