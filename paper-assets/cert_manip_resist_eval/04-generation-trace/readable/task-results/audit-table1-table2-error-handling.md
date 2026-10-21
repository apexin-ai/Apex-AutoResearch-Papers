# audit table1 table2 error handling

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_table1-table2-error-handling_20260523T174828_result.json`
- **Structured JSON:** [`06adb37d2b377a2738a1.json`](../../sessions/06/06adb37d2b377a2738a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。以下是完整报告。

---

## 诊断报告：V1 Bug (`.get("winner", "tie")`) 影响范围

### 1. 统一数据加载层

**`src/unified_data_loader.py`** 有两套 ASR 函数：
- **V2 (正确)**: `compute_corrected_asr()`, `compute_corrected_panel_asr()` — 使用 `_is_valid_score()` 跳过 error 样本
- `_is_valid_score(score)`: `score.get("winner") is not None and not score.get("error")` (line 232)
- 也导出 `_is_valid_score` 供外部脚本使用

**问题**: 多个脚本虽然从 unified_data_loader 导入数据加载函数，但**自己重新定义了 ASR 计算函数**，且用的是 V1 bug 版本。

---

### 2. 各脚本 Error Handling 逐一诊断

| 脚本 | 对应论文内容 | Error Handling | 受 V1 Bug 影响？ |
|------|------------|---------------|-----------------|
| `run_condition_dominance.py` | Table 1 dominance | `.get("winner", "tie")` lines 82,84,95,99 | **是 (V1)** |
| `run_residualized_keff_15model.py` | Table 1 OLS regression | `.get("winner", "tie")` lines 63,65,75,79,91 | **是 (V1)** |
| `run_aggregation_loglog.py` | Table 2 (4 agg methods, log-log) | `.get("winner", "tie")` lines 71,73,90,91 | **是 (V1)** |
| `run_aggregation_regression_15model.py` | Table 2 (residualized) | 自定义 `_is_valid_score()` 跳过 error | **否 (V2)** |
| `run_claim6_panel_design_15model.py` | Claim 6 panel design | 导入 `_is_valid_score` 从 unified_data_loader | **否 (V2)** |
| `run_wild_cluster_bootstrap_v2.py` | K=3 bootstrap | `.get("winner", "tie")` lines 67,69,80,84 | **是 (V1)** |
| `run_k5_wild_cluster_bootstrap.py` | K=5 regime transition | `.get("winner", "tie")` lines 69,71,82,86 | **是 (V1)** |
| `run_k7_wild_cluster_bootstrap.py` | K=7 regime transition | `.get("winner", "tie")` lines 69,71,82,86 | **是 (V1)** |
| `run_plan010_aggregation.py` | 旧 6-model aggregation | 只用 6 个 local 模型 | **不受影响**（local 模型几乎无 error） |

---

### 3. Error 分布表

**高 Error 模型**（API 模型）：

| Model | Total Scores | Total Errors | Error Rate |
|-------|-------------|-------------|-----------|
| gemini-3.5-flash | 4200 | 742 | **17.67%** |
| gemini-3.1-pro-preview | 4200 | 335 | **7.98%** |
| gpt-5.5 | 4200 | 129 | **3.07%** |

**按 Benchmark × Attack 细分（高 error 模型）**：

| Model | Benchmark | Attack | Errors/300 | Rate |
|-------|-----------|--------|-----------|------|
| gemini-3.5-flash | mmlu | prompt_injection | 97 | **32.3%** |
| gemini-3.5-flash | mmlu | sycophancy | 86 | **28.7%** |
| gemini-3.5-flash | mmlu | verbosity_bias | 82 | **27.3%** |
| gemini-3.5-flash | mmlu | authority_bias | 82 | **27.3%** |
| gemini-3.5-flash | mmlu | position_bias | 81 | **27.0%** |
| gemini-3.5-flash | mmlu | clean | 79 | **26.3%** |
| gemini-3.5-flash | mmlu | score_manipulation | 77 | **25.7%** |
| gemini-3.5-flash | arc | prompt_injection | 31 | 10.3% |
| gemini-3.5-flash | arc | clean/syc/score/verb/auth | 19-23 | 6.3-7.7% |
| gemini-3.1-pro-preview | mmlu | prompt_injection | 50 | **16.7%** |
| gemini-3.1-pro-preview | mmlu | score_manipulation | 48 | **16.0%** |
| gemini-3.1-pro-preview | mmlu | verbosity_bias/position/auth | 33-38 | 11-12.7% |
| gemini-3.1-pro-preview | mmlu | clean | 35 | 11.7% |
| gemini-3.1-pro-preview | arc | all conditions | 3-10 | 1.0-3.3% |
| gpt-5.5 | mmlu | clean | 23 | 7.7% |
| gpt-5.5 | mmlu | score_manipulation | 21 | 7.0% |
| gpt-5.5 | mmlu | other attacks | 13-15 | 4.3-5.0% |
| gpt-5.5 | arc | all conditions | 1-5 | 0.3-1.7% |

**低 Error 模型**：其余 12 个模型的 error rate 均 < 0.2%（0-7 个 errors / 4200 samples）。

---

### 4. 判断

| 分析内容 | 受 V1 Bug 影响？ | 影响程度 | 说明 |
|---------|-----------------|---------|------|
| **Table 1** (dominance + OLS regression) | **是** | **高** | `run_condition_dominance.py` 和 `run_residualized_keff_15model.py` 都用 V1。gemini-3.5-flash 在 mmlu 上高达 25-32% error 被当作 tie，直接影响该模型参与的所有 455 个 panel 的 ASR 计算。 |
| **Table 2** (aggregation comparison) | **部分** | **中** | `run_aggregation_loglog.py` (log-log 版) 是 V1；`run_aggregation_regression_15model.py` (residualized 版) 是 V2。论文最终用哪个需要确认。 |
| **Regime Transition** (K=3/5/7 bootstrap) | **是** | **高** | 全部三个脚本 (v2, k5, k7) 都是 V1。K=5 有 C(15,5)=3003 panels，K=7 有 C(15,7)=6435 panels，高 error 模型被包含在大量 panel 中，error→tie 会系统性压低 ASR（错误地让 panel 看起来更 robust）。 |

**核心问题**：unified_data_loader 的 V2 corrected 函数已经写好，但大多数实际分析脚本**没有调用它们**，而是各自复制粘贴了 V1 版本的 ASR 计算函数。这是一个典型的"修了但没修完"的情况——数据加载层修好了，消费层没跟上。

---
