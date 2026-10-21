# ops check w10 theta results

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_w10_theta_results_20260517T170720_result.json`
- **Structured JSON:** [`3170d888e80fc5da7b5a.json`](../../sessions/31/3170d888e80fc5da7b5a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集。汇总如下：

---

## 1. W10 Exclusion Sensitivity 结果

**目录**: `/root/autodl-tmp/exp006/exclusion_sensitivity/`
**状态**: 4/6 rates 完成（缺 excl60, excl70）

| Excl% | N_items_total | N_items_fit | τ (Kendall) | PPP | γ_mean | γ_CI [2.5%, 97.5%] | MAE | Rhat_max | all_ok |
|-------|-------------|-------------|-------------|-------|--------|---------------------|-------|----------|--------|
| 0% | 14042 | 2000 | 0.4602 | 0.208 | 0.1277 | [-0.381, 0.632] | 0.0098 | 1.0154 | **true** |
| 30% | 9830 | 2000 | 0.5752 | 0.139 | 0.2811 | [-0.145, 0.726] | 0.0099 | 1.0151 | false (ESS=683) |
| 40% | 8426 | 2000 | 0.6040 | 0.675 | -0.1880 | [-0.588, 0.225] | 0.0074 | 1.0171 | false (ESS=615) |
| 50% | 7021 | 2000 | 0.5464 | 0.130 | 0.2420 | [-0.101, 0.595] | 0.0087 | 1.0165 | false (ESS=780) |

J = 13 models for all rates. 0 divergences across all fits.

---

## 2. θ Domain IRT (J=16, cross-family) 结果

**目录**: `/root/autodl-tmp/exp006/mmlu_domain_irt_j16_cross_family/`
**8 个域目录**，7 个有实质结果，1 个 (Business_Law) post-processing 失败。

### γ 汇总表

| Domain | N_items (orig) | N_fit | γ_mean | γ_median | 95% CI | PPP | Rhat | ESS | Status |
|--------|---------------|-------|--------|----------|--------|------|------|------|--------|
| STEM_Math | 1190 | 1190 | -0.386 | -0.383 | [-0.999, 0.200] | 0.998 | 1.009 | 1448 | OK |
| STEM_Science | 1397 | 1397 | 0.042 | 0.041 | [-0.535, 0.633] | 0.981 | 1.008 | 1444 | OK |
| STEM_CS_Eng | 557 | 557 | 0.362 | 0.358 | [-0.443, 1.184] | 0.893 | 1.006 | 1615 | OK |
| Medical | 1640 | 1640 | 0.218 | 0.222 | [-0.336, 0.738] | **0.000** | **0.000** | **0** | diag broken |
| Humanities | 2816→2000 | 2000 | -0.954 | -0.952 | [-1.425, -0.485] | 1.000 | 1.008 | 1477 | OK |
| Social_Sciences | 3077→2000 | 2000 | -1.092 | -1.094 | [-1.497, -0.674] | 1.000 | 1.008 | 1338 | OK |
| Business_Law | 2482→2000 | 2000 | **empty** | - | - | **0.000** | **0.000** | **0** | **FAILED** |
| Other | 883 | 883 | -0.880 | -0.879 | [-1.548, -0.233] | **0.000** | **0.000** | **0** | diag broken |

**注意**: Medical, Business_Law, Other 三个域的 diagnostics (rhat=0, ess=0, ppp=0) 明显异常，post-processing 可能出错（csv 在 /tmp 被清理?）。Business_Law 连 gamma/theta 都是空的。

### θ 范围速览 (mean, model order from model_order.json)

模型顺序: 1.5B d000s123, d000s42, d005s123, d005s42, d025s123, d025s42, d100s123, d100s42 | Llama3B d000s42, d005s42, d025s42 | Qwen3B d005s123, d025s123, d025v3s42, d100a32s123, d100a32s42

| Domain | 1.5B θ range | Llama-3B θ range | Qwen-3B θ range |
|--------|-------------|-----------------|-----------------|
| STEM_Math | [-0.51, -0.36] | [-1.74, -1.46] | [-0.16, 0.10] |
| STEM_Science | [0.36, 0.46] | [-0.98, -0.77] | [0.57, 0.75] |
| STEM_CS_Eng | [0.38, 0.51] | [-0.96, -0.68] | [0.35, 0.55] |
| Medical | [0.47, 0.63] | [-0.63, -0.44] | [0.82, 1.01] |
| Humanities | [0.26, 0.32] | [-0.75, -0.62] | [0.46, 0.54] |
| Social_Sciences | [1.02, 1.11] | [-0.47, -0.25] | [1.46, 1.55] |
| Other | [0.87, 0.93] | [0.09, 0.36] | [1.50, 1.54] |

---

## 3. excl00 配置详情

从脚本 `/root/contamcal-irt-calibration/exp006/sensitivity_exclusion_rate.py` 读取：

**模型 (J=13, MODEL_WHITELIST)**:
- 8x Qwen2.5-1.5B: d000/d005/d025/d100 × s42/s123
- 5x Qwen2.5-3B: d005_s123, d025_s123, d025_v3_s42, d100_a32_s123, d100_a32_s42

**Item 选择方式**: 
- 先按 RRF exposure 排序，排除最高 exposure 的 `excl_rate%` items
- excl00 = 不排除任何 item (全部 14042 items 保留)
- 保留 pool > 2000 时，`np.random.seed(42)` 随机抽样 2000 items
- 所以 excl00 = **从 14042 MMLU items 中 seed=42 随机抽 2000**

**其他配置**:
- Benchmark: MMLU only
- Scales: 1.5B + 3B
- Eval results: `/root/autodl-tmp/exp001/eval_results` (skip_para=True)
- RRF scores: `/root/autodl-tmp/exp003/rrf_all_scales/exposure_scores.json`
- Stan model: 2PL+γ, chains=2, warmup=1000, sampling=1000, adapt_delta=0.95, max_treedepth=12, seed=42

---

**总结**:
- Exclusion sensitivity: 4/6 完成，缺 60% 和 70%
- Domain IRT: 8 域中 5 个完全正常，Medical/Other diagnostics 异常 (post-processing bug)，Business_Law 彻底失败
- 两个任务都可能还在运行中（exclusion 最后一个 excl50 完成于 01:03 5/18），需要检查是否有活跃进程

---
