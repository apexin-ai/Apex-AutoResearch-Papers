# analysis k5 majority 10vs7 discrepancy

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_k5-majority-10vs7-discrepancy_20260524T071803_result.json`
- **Structured JSON:** [`ddc2c36550a1e573962b.json`](../../sessions/dd/ddc2c36550a1e573962b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

I now have all the data needed. Let me compile the full analysis.

## 1. 脚本对比

**regime_transition_corrected.json**
- 路径：`/root/cert_manip_resist_eval/artifacts/server_backup/results/regime_transition_corrected.json`
- **无可追溯的生成脚本** — 没有任何 `.py` 文件输出到此路径。文件创建时间 2026-05-24 02:04 AM，很可能由 Claude agent session 内联生成
- 回归：`log(ASR+eps) ~ log(K_eff) + log(eta_max+eps)` (majority vote panel ASR)
- 数据源：不可确定（无脚本可追溯）
- 结构有 `old`/`new` 对比：K5 old keff_sig=**7**, new keff_sig=**10**

**k5_aggregation_bootstrap.json**
- 路径：`/root/cert_manip_resist_eval/artifacts/results/plan001/k5_aggregation_bootstrap.json`
- 生成脚本：`/root/cert_manip_resist_eval/artifacts/scripts/run_k5_aggregation_bootstrap.py`
- 回归：同上 `log(ASR+1e-6) ~ log(K_eff) + log(eta_max+1e-6)`
- 数据源：`load_all_scores()` / `load_pairs()` / `load_mi_data()` （默认路径，V2 数据）
- majority_vote keff_fdr_sig = **7/12**
- 修改时间：2026-05-24 14:13（比 RT 晚 12 小时）

**关键差异：regime_transition_corrected.json 的 "old" K5 keff_sig=7 与 aggregation_bootstrap 的 7/12 完全一致。"10/12" 来自某种 "correction"，但无脚本可审计。**

---

## 2. OLS β 系数对比（K=5, majority vote）

| # | Condition | RT std_β | Agg std_β | Δ |
|---|-----------|---------|---------|---|
| 1 | mmlu×PI | 0.546 | 0.529 | ≈ |
| 2 | mmlu×syc | 0.456 | 0.455 | ≈ |
| 3 | mmlu×SM | 0.666 | 0.645 | ≈ |
| 4 | mmlu×VB | 0.414 | 0.335 | △ |
| 5 | **mmlu×PB** | **0.482** | **0.204** | **2.4×** |
| 6 | mmlu×AB | 0.405 | 0.499 | △ |
| 7 | **arc×PI** | 0.517 | 0.558 | △ |
| 8 | arc×syc | 0.096 | 0.065 | ≈ |
| 9 | arc×SM | 0.542 | 1.172 | **2.2×** |
| 10 | arc×VB | 0.393 | 0.418 | ≈ |
| 11 | **arc×PB** | **0.954** | **0.139** | **6.9×** |
| 12 | arc×AB | 0.269 | 0.226 | ≈ |

**OLS β 系数的系统性差异（尤其是 position_bias 相关条件）证明两个分析使用了不同的底层数据。**

---

## 3. P-value 逐条对比（K=5, majority vote, wild cluster bootstrap max-p → BH FDR 0.05）

| # | Condition | RT keff_final_p | Agg keff_final_p | RT keff_fdr_p | Agg keff_fdr_p | RT sig | Agg sig |
|---|-----------|----------------|-----------------|--------------|---------------|--------|---------|
| 1 | mmlu×PI | 0.0020 | 0.0030 | 0.0100 | 0.0108 | ✓ | ✓ |
| 2 | mmlu×syc | 0.0014 | 0.0030 | 0.0100 | 0.0108 | ✓ | ✓ |
| 3 | mmlu×SM | 0.0056 | 0.0056 | 0.0166 | 0.0134 | ✓ | ✓ |
| 4 | mmlu×VB | 0.0069 | 0.0074 | 0.0166 | 0.0148 | ✓ | ✓ |
| 5 | **mmlu×PB** | **0.0112** | **0.1145** | **0.0186** | **0.1527** | **✓** | **✗** |
| 6 | mmlu×AB | 0.0025 | 0.0036 | 0.0100 | 0.0108 | ✓ | ✓ |
| 7 | **arc×PI** | **0.0334** | **0.0629** | **0.0401** | **0.0944** | **✓** | **✗** |
| 8 | arc×syc | 0.4136 | 0.5621 | 0.4136 | 0.6132 | ✗ | ✗ |
| 9 | arc×SM | 0.0124 | 0.0010 | 0.0186 | 0.0108 | ✓ | ✓ |
| 10 | arc×VB | 0.0188 | 0.0153 | 0.0251 | 0.0262 | ✓ | ✓ |
| 11 | **arc×PB** | **0.0094** | **0.9790** | **0.0186** | **0.9790** | **✓** | **✗** |
| 12 | arc×AB | 0.1409 | 0.1499 | 0.1537 | 0.1799 | ✗ | ✗ |

**RT total: 10/12, Agg total: 7/12**

---

## 4. 结论

两个分析**不应该**给出相同结果，因为它们使用了**不同的底层数据**。核心证据：

1. **OLS β 系数不同**：如果数据相同，两个分析的 OLS 回归结果应完全一致（OLS 是确定性的），但实际差异显著，尤其是 position_bias 条件（arc×PB std_β: 0.954 vs 0.139，差 6.9 倍）

2. **无可追溯脚本**：regime_transition_corrected.json 没有对应的 Python 脚本，无法审计其数据加载路径和处理逻辑

3. **"old" 值恰好等于 7**：RT 的 `old.keff_sig=7` 与 aggregation_bootstrap 的 `7/12` 完全一致，暗示 RT 的"old"就是用 V2 数据跑的原始结果，而 "new"(10/12) 是某种修正后的结果——但这个修正无法复现

4. **position_bias 是重灾区**：3 个翻转条件中 2 个是 position_bias（mmlu×PB 和 arc×PB），arc×PB 的 bootstrap p-value 差异最为极端（0.0094 → 0.979，差 100 倍）

**建议：论文应引用 k5_aggregation_bootstrap.json 的 7/12（有可追溯脚本 + V2 数据 + 更晚生成），废弃 regime_transition_corrected.json 的 10/12。**

---
