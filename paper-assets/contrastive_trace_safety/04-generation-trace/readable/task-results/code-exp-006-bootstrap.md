# code exp 006 bootstrap

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_006_bootstrap_20260516T203617_result.json`
- **Structured JSON:** [`87dbae8f6380cd211af9.json`](../../sessions/87/87dbae8f6380cd211af9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-006 完成。结果摘要：

**Bootstrap B=1000, n_test=43, threshold=0.5, K=5**

| Method | Accuracy | Crossing Rate | Lead Time |
|--------|----------|--------------|-----------|
| Static LR | 0.768 [0.702, 0.827] | 60.4% [44.2, 74.4] | +2.9 [-2.8, +9.5] |
| Temporal LR W=15 | 0.731 [0.654, 0.804] | 60.6% [46.5, 74.4] | +5.0 [-0.8, +11.9] |
| GRU single L14 | 0.790 [0.734, 0.848] | 51.4% [37.2, 67.4] | -2.0 [-8.6, +4.9] |
| GRU multi-7L | 0.799 [0.742, 0.854] | 51.4% [37.2, 67.4] | -0.4 [-6.4, +6.1] |

**Paired tests（p-value = P(delta≤0)）：**
- Temporal LR vs Static LR: crossing Δ=+0.001 (p=0.57), lead_time Δ=+2.1 (p=0.19)
- GRU multi vs Static LR: crossing Δ=-0.094 (p=0.94), lead_time Δ=-3.3 (p=0.94)
- GRU multi vs Temporal LR: crossing Δ=-0.095 (p=0.91), lead_time Δ=-5.4 (p=0.99)

**发现：** 所有方法间差异不显著（CIs 重叠严重）。GRU 在此次重训中表现低于之前实验（早停在第6轮触发），Temporal LR W=15 的 lead_time 数值上最好（+5.0），但 p=0.19 不显著。小测试集（n=43）导致 CI 很宽。

脚本：`src/experiments/bootstrap_ci.py`，输出：`artifacts/exp_006_bootstrap/bootstrap_results.json`。

---
