# infra plan009 diagnose resubmit

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_plan009-diagnose-resubmit_20260520T184915_result.json`
- **Structured JSON:** [`02f2d1fe21fb93c1c266.json`](../../sessions/02/02f2d1fe21fb93c1c266.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**plan009 已经成功完成，不需要修复。**

日志显示脚本于 2026-05-20 11:41 启动，25 秒内跑完全部 7 拓扑 × 3 个 K 值 × 全部病理矩阵类型（M=1000, N=5M），正常退出。

产出文件（`artifacts/plan009/`）：
- `pathological_bias_summary.json` — 167 KB
- `regression_results.txt` — 3.5 KB
- `plan009_run.log` — 27 KB

关键结果摘要：
- **confounding/mediation/collider/frontdoor**: R² = 0.61–0.77，spectral_gap 和 condition_number 显著正相关 |bias|
- **exposure**: R² = 0.11，catastrophic bias 高发（near_perm eps=0.01 时 15% 超阈值）
- **iv**: R² ≈ 0，回归基本无解释力（IV 估计量对矩阵特征不敏感）
- **GLOBAL**: R² ≈ 0，跨拓扑聚合后特征解释力消失（符合预期，不同拓扑的 bias 机制不同）

---
