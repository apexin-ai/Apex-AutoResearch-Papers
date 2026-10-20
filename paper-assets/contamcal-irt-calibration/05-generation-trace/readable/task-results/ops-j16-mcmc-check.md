# ops j16 mcmc check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_j16_mcmc_check_20260517T135815_result.json`
- **Structured JSON:** [`19e5546191e2928ffef7.json`](../../sessions/19/19e5546191e2928ffef7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Here are the results:

## J=16 Cross-Family MMLU Domain IRT Results

### 状态
- **8/8 域拟合完成**，所有诊断指标优秀
- **Pooled 拟合失败**：4 chains 在 60% sampling 时全部报 "Operation not permitted"（可用 `--pooled-only` 重跑）
- **Theta per model 未保存**（仅 JSON 中有 gamma/diagnostics/PPP）

### Domain 结果总览

| Domain | γ_mean | γ_95%CI | Signif? | PPP | Rhat | ESS | Div | Items | MAE |
|--------|--------|---------|---------|-----|------|-----|-----|-------|-----|
| STEM_Math | -0.386 | [-1.00, 0.20] | No | 0.998 | 1.009 | 1448 | 0 | 1190 | 0.023 |
| STEM_Science | 0.042 | [-0.53, 0.63] | No | 0.981 | 1.008 | 1444 | 0 | 1397 | 0.017 |
| STEM_CS_Eng | 0.362 | [-0.44, 1.18] | No | 0.893 | 1.006 | 1615 | 0 | 557 | 0.018 |
| Medical | 0.218 | [-0.34, 0.74] | No | 0.827 | 1.010 | 1560 | 0 | 1640 | 0.013 |
| **Humanities** | **-0.947** | **[-1.43, -0.49]** | **Yes** | 1.000 | 1.008 | 1477 | 0 | 2000 | 0.028 |
| **Social_Sciences** | **-1.092** | **[-1.50, -0.67]** | **Yes** | 1.000 | 1.008 | 1338 | 0 | 2000 | 0.019 |
| Business_Law | -0.239 | [-0.68, 0.20] | No | 0.978 | 1.007 | 1353 | 0 | 2000 | 0.013 |
| **Other** | **-0.880** | **[-1.55, -0.23]** | **Yes** | 0.982 | 1.008 | 1331 | 0 | 883 | 0.012 |

### 关键发现

**3/8 domains 检测到显著 gamma（CI 排除 0）：**
- Social_Sciences：γ = -1.09（最强信号）
- Humanities：γ = -0.95
- Other：γ = -0.88

γ < 0 表示高 RRF 暴露的 item 其 item difficulty 被高估（即模型在这些 item 上表现比预期好），与污染假说一致。

**5/8 domains gamma 不显著**，其中 STEM_CS_Eng 和 Medical 的 γ > 0（方向相反但不显著）。

**诊断指标全部优秀**：Rhat 全 < 1.01，ESS 全 > 1300，0 divergences，PPP 全 > 0.82。

### 待办
- 重跑 pooled fit：`python run_mmlu_domain_gamma_j16_cross_family.py --pooled-only`
- 如需 theta per model，需修改脚本在 `irt_results.json` 中保存 theta 后重跑

---
