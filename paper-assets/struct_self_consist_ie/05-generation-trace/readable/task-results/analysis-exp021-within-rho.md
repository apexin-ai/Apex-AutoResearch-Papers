# analysis exp021 within rho

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp021_within_rho_20260517T203007_result.json`
- **Structured JSON:** [`cf6f140f05c63d899b9e.json`](../../sessions/cf/cf6f140f05c63d899b9e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

**exp_021 (3-epoch) vs exp_028 (5-epoch) within-instance ρ(LP, F1)，同 5000 实例子集，N=8：**

| Metric | 3-epoch | 5-epoch | Delta |
|--------|---------|---------|-------|
| ρ mean | **0.5241** | 0.4066 | -0.1175 |
| ρ median | **0.6667** | 0.6151 | -0.0516 |
| ρ std | 0.4673 | 0.5506 | +0.0833 |
| Valid instances | 3723/4351 (85.6%) | 2988/4351 (68.7%) | -16.9pp |

**Alignment 受 convergence 明显影响。** 5-epoch over-convergence 同时导致：
1. Degeneracy 大幅上升（11.1%→31.3%），更多实例 LP/F1 方差为零被排除
2. 剩余有效实例的 LP-F1 对齐也变差（mean ρ 降 0.12）
3. 全量 exp_021（37648 实例）within-instance ρ：mean=0.5106, median=0.6667，与子集一致

---
