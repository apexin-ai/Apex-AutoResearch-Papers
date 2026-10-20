# ops c7 baseline config audit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_c7_baseline_config_audit_20260517T163424_result.json`
- **Structured JSON:** [`466385903ec63cf6cd6f.json`](../../sessions/46/466385903ec63cf6cd6f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Confirmed — only `irt_results.json` in each, no baselines. Here's the full report:

---

## C7 调查结果

### 1. Table 5 (ARC): J=13 数据

**已存在。** `pooled_irt_all_scales/arc_challenge/irt_results.json` 有 J=13 (1.5B×6 + 3B×7) 2PL+γ IRT 结果：
- raw_mae=0.034, cal_mae=0.015, γ=0.486 (CI includes zero)
- 这就是 Table 4 正文用的数据

**但没有 baselines.json。** 旧的 baselines (包括 B6-DCR) 只在旧配置（J=8/9，0.5B+1.5B）上跑过，MAE: B6_dcr_fuzzy ARC=0.191, GSM8K=0.213。pooled_irt_all_scales 目录下三个 benchmark 只有 irt_results.json，没有任何 baselines 数据。

### 2. Table 6 (GSM8K): J 配置

**pooled_irt_all_scales/gsm8k 是 J=20（三个 scale 全含）**，不是 J=13。因为 GSM8K 不受 position bias 影响，0.5B 被保留：
- 0.5B×7 + 1.5B×6 + 3B×7 = 20 models
- raw_mae=0.163, cal_mae=0.008

**不存在"J=13 仅 1.5B+3B"的 GSM8K 单独跑。** "0.5B-only" 数据来自 scale_stratified_irt/scale_0.5B/gsm8k (N=7)。

### 3. DCR MAE=0.245/0.263 来源

**这两个数字不在当前论文 tex 文件中**（grep 全文无匹配），是之前提交版本的残留。它们的数据来源是 **PPP 值**（不是 MAE）：
- 3B_mmlu PPP = 0.263
- 3B_gsm8k PPP = 0.245
来自 `scale_stratified_irt` 的 3B 单 scale 结果。

真正的 DCR 数据：代码中有 `DCRFuzzyBaseline` 重实现（`baselines.py:272`），在旧的 J=8/9 跑中产出 MAE=0.191 (ARC) / 0.213 (GSM8K)。**但论文同时写"qualitative comparison only, no public implementation"**（experimental_setup.tex:36），与实际有重实现矛盾 — 审稿人抓住了这个。

### 4. 要统一到 J=13，需要什么

| Benchmark | 现状 | 需要做的 |
|-----------|------|---------|
| **ARC** | J=13 IRT 已有，无 baselines | 在 pooled_irt_all_scales/arc_challenge 上重跑 baselines pipeline（B0-B6） |
| **MMLU** | J=15 IRT 已有，无 baselines | 同上，或解释 J=15 vs J=13 差异（1.5B 多了 d025_s123 和 d100_s123） |
| **GSM8K** | J=20 IRT 已有（含 0.5B），无 baselines | 要么用 J=20（合理因为 0.5B 无 position bias），要么单独跑 J=13；无论如何需重跑 baselines |
| **DCR 描述** | 有重实现但论文说 "qualitative/no public impl" | 二选一：(a) 承认是重实现并报告准确 MAE，(b) 删除具体数字只做定性比较 |

**不需要重跑 MCMC** — IRT 结果已存在。只需在对应数据上运行 baselines 计算脚本（`baselines.py` 中的 B0-B6 methods），输入是 correctness_matrix 和 exposure_scores。

---
