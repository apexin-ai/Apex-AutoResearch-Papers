# analysis pgamma discrepancy trace

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_pgamma-discrepancy-trace_20260521T174440_result.json`
- **Structured JSON:** [`5aa6f0c0b80c229f114c.json`](../../sessions/5a/5aa6f0c0b80c229f114c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。以下是完整的追溯结果。

---

## 99.7% 来源
- **文件**: `/root/autodl-tmp/exp006/mmlu_domain_irt_j16_qwen/Social_Sciences/irt_results.json`
- **脚本**: `exp006/run_mmlu_domain_gamma_j16.py`
- **配置**: J=16 (Qwen 1.5B×8 + 3B×8), I=2000 (subsampled from 3077), seed=42
- **Stan**: `contam_irt_2pl_gamma.stan` → `gamma ~ std_normal()` = **N(0,1)**
- **MCMC**: 4 chains × 1000 warmup + 1000 samples, adapt_delta=0.95, treedepth=12
- **原始值**: p_neg = **0.99675** (四舍五入为 99.7%)
- **gamma**: mean=-0.6274, CI=[-1.073, -0.192], mean_acc=0.7198

## 98.48% 来源
- **文件**: `/root/autodl-tmp/exp006/gamma_prior_sensitivity/social_sciences/baseline_10_results.json`
- **脚本**: `exp006/gamma_prior_sensitivity_resume.py` (imports model list from `run_mmlu_domain_gamma_no05b.py`)
- **配置**: J=16, I=2000, seed=42
- **Stan**: `contam_irt_2pl_gamma.stan` → `gamma ~ std_normal()` = **N(0,1)** (**同一先验！**)
- **MCMC**: 4 chains × 1000 warmup + 1000 samples, adapt_delta=0.95, treedepth=12 (**同一配置！**)
- **原始值**: p_negative = **0.9848**
- **gamma**: mean=-0.4967, CI=[-0.943, -0.055], mean_acc=0.7085

## 差异列表

| 维度 | §5.7 (99.7%) | Appendix K (98.48%) |
|------|-------------|---------------------|
| 先验 | N(0,1) | N(0,1) **相同** |
| Stan model | contam_irt_2pl_gamma.stan | contam_irt_2pl_gamma.stan **相同** |
| MCMC config | 4×1000, seed=42 | 4×1000, seed=42 **相同** |
| **Model whitelist** | `run_mmlu_domain_gamma_j16.py` 的 16 模型集 | `run_mmlu_domain_gamma_no05b.py` 的模型集（**不同！**） |
| mean_acc | 0.7198 | 0.7085 |
| gamma mean | -0.6274 | -0.4967 |

## 结论

**根因**：两个数字使用完全相同的先验 N(0,1)、相同的 Stan 模型、相同的 MCMC 配置，但**不同的模型集**。

- 敏感性分析脚本从 `run_mmlu_domain_gamma_no05b.py` 导入 MODEL_WHITELIST（原设计为 J=13，无 3B d000），而非 `run_mmlu_domain_gamma_j16.py` 的 J=16 模型集。
- 虽然两次运行都输出 n_models=16（no05b 白名单在运行时可能被临时扩展），但模型组成不同（mean_acc 差 1.13pp 证实）。

**Appendix K Table 10 的 baseline_10 行应该与 §5.7 完全一致（都是 N(0,1) 先验、J=16），但由于模型集不同导致 98.48% ≠ 99.675%。这是一个数据对齐 bug，不是先验敏感性差异。**

**修复方案**：用 `run_mmlu_domain_gamma_j16.py` 的 MODEL_WHITELIST 重跑敏感性分析，确保只变化先验（tight/baseline/loose）而固定模型集。

---
