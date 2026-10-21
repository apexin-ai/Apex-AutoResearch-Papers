# ops cross family pooled irt refit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cross_family_pooled_irt_refit_20260517T000103_result.json`
- **Structured JSON:** [`d42bee51f9ba36028ccf.json`](../../sessions/d4/d42bee51f9ba36028ccf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

Cross-family pooled IRT 完成。

### 核心发现：ARC 污染信号具有 family-specificity

| Benchmark | Pool | N | γ | 95% CI | PPP | cal_MAE |
|-----------|------|---|---|--------|-----|---------|
| **ARC** | Qwen-only | 16 | **0.727** | [0.02, 1.44] | 0.003 | 0.020 |
| **ARC** | Qwen+Llama | 20 | **0.002** | [-0.57, 0.60] | 0.449 | 0.015 |
| GSM8K | Qwen-only | 24 | 0.064 | [-0.36, 0.49] | 0.541 | 0.006 |
| GSM8K | Qwen+Llama | 28 | -0.110 | [-0.52, 0.28] | 0.832 | 0.008 |

### 关键结论

1. **ARC family-specificity 强烈确认**：Qwen-only γ=0.73 (CI excludes zero)，加入 4 个 Llama respondents 后 γ→0.00 (CI includes zero)。Δγ = -0.725。
2. **GSM8K**：两个 pool 的 γ 都接近零，GSM8K 的 RRF 信号本身不足以支撑 contamination 效应估计。
3. **诊断良好**：所有 fit 无 divergences，Rhat < 1.01，ESS > 1300。
4. **解读**：Llama 模型的 RRF exposure scores 在各 dosage 间无明显区分（~0.15-0.18），说明 RRF 信号是 Qwen-specific 的。当 IRT 模型看到 Llama 有相似 exposure 但无对应 performance boost 时，global γ 被拉向零。

### 产出文件
- 结果 JSON: `/root/autodl-tmp/exp006/results_cross_family_irt_v2/pooled_rrf_irt_results.json`
- Combined RRF: `/root/autodl-tmp/exp003/rrf_cross_family_qwen_llama/exposure_scores.json` (29 models)
- Qwen-only baseline: `/root/autodl-tmp/exp006/results_pooled_irt_qwen_n24/pooled_rrf_irt_results.json`

---
