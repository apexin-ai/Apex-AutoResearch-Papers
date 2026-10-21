# audit gam data version compare

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_gam-data-version-compare_20260523T174455_result.json`
- **Structured JSON:** [`8cc7e2adfdc8ea38a4a3.json`](../../sessions/8c/8cc7e2adfdc8ea38a4a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

---

## 诊断报告

### 1. 原始 GAM 脚本

**路径**: `/root/cert_manip_resist_eval/scripts/run_gam_tier_analysis.py` (May 23 03:08)

**数据加载**: `load_mi_data()` → 统一 MI 矩阵 (`mi_matrix_15models.json`)

**ASR 计算**: 定义自己的 `compute_individual_asr()`，用 `.get("winner", "tie")` 处理无效分数 → error 响应被当作 "tie" 投票

**GAM 规格**: `LinearGAM(s(0, n_splines=8) + s(1, n_splines=8))`，用 `gam.gridsearch()` 自动选 lambda

**符号定义**: `pdep[-1] > pdep[0]` on `generate_X_grid(term=0, n=100)` → 与 bootstrap 完全相同

### 2. Bootstrap 脚本

**路径**: `/root/cert_manip_resist_eval/scripts/run_gam_bootstrap_ci_k3.py` (May 24 01:10)

**数据加载**: 同一个 `load_mi_data()` → 同一个 MI 矩阵

**ASR 计算**: 从 `unified_data_loader` 导入 `_is_valid_score`，**过滤掉 error/无效分数**，不计入 ASR

**GAM 规格**: 完全相同的 `LinearGAM(s(0, n_splines=8))`，gridsearch 选 lambda 后固定给 bootstrap 样本

### 3. K_eff 对比结果

**K_eff 值完全一致** — 两个脚本使用同一个 `load_mi_data()` 读同一个 `mi_matrix_15models.json`，不存在版本差异。

差异来源是 **ASR (y 变量)**，不是 K_eff (x 变量)。

### 4. 根因：ASR 计算 bug + gridsearch 随机性

Per-condition sign 对比：

| Condition | 原始 GAM | Bootstrap | 匹配 |
|---|---|---|---|
| mmlu×prompt_injection | + | + | OK |
| mmlu×score_manipulation | + | + | OK |
| mmlu×position_bias | + | + | OK |
| **mmlu×sycophancy** | **-** | **+** | MISMATCH |
| **mmlu×verbosity_bias** | **-** | **+** | MISMATCH |
| **mmlu×authority_bias** | **-** | **+** | MISMATCH |
| arc×prompt_injection | + | + | OK |
| arc×score_manipulation | + | + | OK |
| arc×position_bias | + | + | OK |
| **arc×sycophancy** | **-** | **+** | MISMATCH |
| **arc×verbosity_bias** | **-** | **+** | MISMATCH |
| **arc×authority_bias** | **-** | **+** | MISMATCH |

6 个 MISMATCH **全部是 shared_bias 攻击**（sycophancy/verbosity_bias/authority_bias），完美对应论文中声称的 taxonomy split。

**Bug 机制**：
- gpt-5.5、gemini-3.1-pro-preview、gemini-3.5-flash 有 ~4%（MMLU）和 ~1%（ARC）的 error 分数
- 原始脚本将 error 当 "tie"，产生虚假 ASR（如 gemini-3.1-pro-preview mmlu×sycophancy: 原始=0.0474, 过滤后=0.0000）
- 对 shared_bias 攻击（真实 ASR 低），这些虚假翻转按比例影响更大
- 膨胀的 frontier ASR 改变了 K_eff→ASR 的 GAM partial dependence 曲面形状
- 加上 `gridsearch()` 的 lambda 随机性（我的 fresh run 用原始方法只复现 2/6 负号而非 6/6），共同产生了 6:6 split

### 5. Table 1 OLS 使用的版本

**脚本**: `run_plan001_step4_panel_regression.py`

**导入**: `compute_corrected_asr, compute_corrected_panel_asr` → 使用 **`_is_valid_score` 过滤**（与 bootstrap 一致）

**结果**: 12/12 条件 keff_beta **全部正向**，全部显著（p < 0.02）

Table 1 OLS 使用的是 **正确版本** 的数据。

### 5. 结论

| 脚本 | ASR 方法 | K_eff sign 结果 |
|---|---|---|
| `run_gam_tier_analysis.py` | 旧（error→tie） | 6:6 split |
| `run_gam_tier_analysis_corrected.py` | 旧（error→tie） | 6:6 split |
| `run_gam_bootstrap_ci_k3.py` | 新（过滤 error） | 12/12 positive |
| `run_plan001_step4_panel_regression.py` | 新（过滤 error） | 12/12 positive |

**Canonical 数据源**: 过滤版 ASR（`_is_valid_score`），被 Table 1 OLS 和 bootstrap 使用。

**6:6 split 产生者**: `run_gam_tier_analysis.py` 中的旧 ASR 计算（将 error 当 tie）+ pygam gridsearch 随机性。这是 artifact，不是 genuine pattern。论文 Section 4.4 的 taxonomy split 声明需要修正。

---
