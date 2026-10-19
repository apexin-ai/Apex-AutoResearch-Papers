# ops pareto analysis

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_pareto-analysis_20260521T061127_result.json`
- **Structured JSON:** [`44b481005f4c56f865c2.json`](../../sessions/44/44b481005f4c56f865c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

执行成功。完整输出：

```
[ar] HV=0.0370  rho=+0.857 (p=0.0065)  Pareto: [24, 27]  tradeoff=NO
[hi] HV=0.0369  rho=+0.310 (p=0.4556)  Pareto: [20, 27]  tradeoff=NO
[ko] HV=0.0360  rho=+0.714 (p=0.0465)  Pareto: [24, 27]  tradeoff=NO
[sw] HV=0.0148  rho=+0.762 (p=0.0280)  Pareto: [27]  tradeoff=NO
[zh] HV=0.0456  rho=+0.857 (p=0.0065)  Pareto: [24, 27]  tradeoff=NO

Wrote results/pareto/pareto_detail.csv
Wrote results/pareto/pareto_summary.csv
Wrote results/pareto/pareto_results.json
```

关键发现（回应 R2-N2）：

- **所有 5 种语言的 tradeoff 均为 NO** — Spearman rho 全部为正，说明 EN probe 质量和跨语言迁移效果**不存在 tradeoff**，深层同时在两个目标上更优。
- **Spearman 相关**：ar/zh 最强（rho=+0.857, p=0.0065），ko（rho=+0.714, p=0.047）和 sw（rho=+0.762, p=0.028）显著，hi 不显著（rho=+0.310, p=0.456）。
- **Pareto 前沿**：layer 24 和 27 主导（4/5 语言），sw 仅 layer 27 Pareto 最优。
- **Hypervolume**：zh 最大（0.0456），sw 最小（0.0148），反映跨语言迁移效果的语言间差异。

输出文件写入 `results/pareto/`（detail CSV、summary CSV、JSON）。

---
