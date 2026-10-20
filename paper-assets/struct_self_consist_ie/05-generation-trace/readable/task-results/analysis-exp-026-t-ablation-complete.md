# analysis exp 026 T ablation complete

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_026_T_ablation_complete_20260517T095526_result.json`
- **Structured JSON:** [`0a51610a0ec7d7267cb0.json`](../../sessions/0a/0a51610a0ec7d7267cb0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果已保存到服务器 (`exp_026_T_ablation_summary.json`) 和本地 artifacts。

## Temperature Ablation Summary (SciERC NER, N=8, ft_002_v2 rank=32)

| Metric | T=0.5 | T=0.8 | T=1.0 | T=1.2 |
|--------|-------|-------|-------|-------|
| **Degeneracy rate** | 0.328 | 0.196 | 0.127 | 0.080 |
| **LP range (mean)** | 0.022 | 0.043 | 0.060 | 0.075 |
| LP range (std) | 0.021 | 0.042 | 0.053 | 0.059 |
| Greedy F1 | 0.617 | 0.616 | 0.585* | 0.620 |
| Oracle F1 | 0.710 | 0.737 | 0.739 | 0.758 |
| Random F1 | 0.612 | 0.589 | 0.565 | 0.571 |
| **SJ sel F1** | 0.622 | 0.619 | 0.581 | 0.597 |
| **EM sel F1** | 0.619 | 0.611 | 0.571 | 0.596 |
| **VC sel F1** | 0.610 | 0.603 | 0.585 | 0.582 |
| **LP sel F1** | 0.622 | **0.627** | 0.584 | **0.621** |
| SJ rho | 0.333 | 0.378 | 0.370 | 0.384 |
| FK rho | 0.341 | 0.340 | 0.396 | 0.386 |
| EM rho | 0.257 | 0.267 | 0.231 | 0.273 |
| VC rho | 0.353 | 0.352 | 0.475 | 0.342 |
| LP rho | 0.208 | 0.212 | 0.134 | 0.182 |
| SJ AUROC | 0.644 | 0.662 | 0.679 | 0.683 |
| FK AUROC | 0.633 | 0.623 | 0.679 | 0.673 |
| EM AUROC | 0.600 | 0.610 | 0.615 | 0.637 |
| VC AUROC | 0.661 | 0.630 | 0.712 | 0.645 |
| LP AUROC | 0.577 | 0.571 | 0.558 | 0.566 |

**关键发现：**
1. **Degeneracy 单调下降**：T=0.5 (33%) → T=1.2 (8%)，低温严重退化
2. **LP range 单调上升**：0.022 → 0.075，高温扩大 LP 区分度
3. **LP selection 是唯一在 T=1.2 仍能 match greedy 的信号**（0.621 vs 0.620），SJ/EM/VC 在高温全部低于 greedy
4. **T=0.8 是 LP selection 的 sweet spot**：LP sel F1=0.627 > greedy 0.616 (+0.011)
5. **AUROC 趋势**：SJ/FK/EM 的 AUROC 随温度升高，VC 在 T=1.0 峰值后下降

*注：T=1.0 greedy F1 (0.585) 低于其他三组 (~0.618)，exp_012_logprob 可能使用不同 checkpoint，跨温度对比 selection delta (sel - greedy) 更可靠。

---
