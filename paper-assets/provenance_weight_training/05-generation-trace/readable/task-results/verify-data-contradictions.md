# verify data contradictions

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_data_contradictions_20260523T111226_result.json`
- **Structured JSON:** [`53031e67352ef0f345b9.json`](../../sessions/53/53031e67352ef0f345b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

现在所有数据已查清。以下是完整报告。

---

## 问题 1：~2% clean vs 5.8% b\*=0 矛盾

### 查到的原始数据

**代码逻辑**（`/root/provenance_weight_training/weighting/alpha_eff.py:find_optimal_b`）：
- 当 `adaptive_tau=false` 时，`b*=0` 当且仅当 `α_eff(0) ≥ τ`
- 两个定义在该配置下**完全等价**

**实际训练配置**（`tau07_seed*/config.json`）：
- `tau=0.7`, `adaptive_tau=false`
- 因此 **b\*=0 ⟺ α_eff(0) ≥ 0.7**，是同一件事

**实际数据**（对 tau07_seed* 的 step_metrics.jsonl 分析）：

| Seed | 总 micro-batch | b\*=0 (= clean) | 比例 |
|------|-------------|------------|------|
| 42 | 24,412 | 1,419 | 5.81% |
| 123 | 24,412 | 1,391 | 5.70% |
| 456 | 24,412 | 1,449 | 5.94% |
| **均值** | | | **5.82%** |

**~2% 的来源**：`binding_stats_seed42.json`（`/root/provenance_weight_training/artifacts/figure_data/binding_stats_seed42.json`）产自 `extract_figure_data.py`，该脚本分析的是 `adaptive_fix_seed42`（**tau=0.8 旧实验**），不是 tau=0.7。在 tau=0.8 时，更少 batch 满足 α_eff(0) ≥ 0.8，故 clean=1.91%。

### 结论

- **b\*=0 和 α_eff(0) ≥ τ 是完全等价的**（因为 `adaptive_tau=false`）
- 正确值：**~5.8%**（不是 ~2%）
- ~2% 来自 tau=0.8 旧实验的数据泄漏

### 修正建议

results.tex line 126：将 "only ~2%" 改为 "~5.8%"

---

## 问题 2：61.8% vs 59.8% ESS-binding

### 查到的原始数据

**tau=0.7 实际三分类**（3 seed 平均）：

| 分类 | 比例 |
|------|------|
| Clean (b\*=0) | 5.82% |
| α_eff-binding (b>0, α_eff ≥ τ−0.005) | 50.91% |
| ESS-binding (b>0, α_eff < τ−0.005) | 43.27% |

**论文引用的数据**（来自 `binding_stats_seed42.json`，tau=0.8 旧实验）：

| 分类 | 比例 |
|------|------|
| Clean | 1.91% |
| α_eff-binding | 38.3% |
| ESS-binding | 59.78% |

**results.tex line 126**："38.2% α_eff-binding and 61.8% ESS-binding"
- 这是两分类表述（38.2 + 61.8 = 100% of non-clean）
- 38.2% 来自 tau=0.8 旧实验

**appendix.tex line 144**："38.2% α_eff-binding and 59.8% ESS-binding, with only ~2% clean"
- 三分类表述（38.2 + 59.8 + 2 = 100%）
- 也来自 tau=0.8 旧实验

**两处内部矛盾**：
1. results.tex 的 61.8% vs appendix.tex 的 59.8%：因为 results.tex 是 non-clean 中的占比（61.8% × 98% = 60.6%），appendix 是总占比（59.8%）
2. 所有数字都来自错误的实验（tau=0.8 而非 tau=0.7）

### 结论

- 正确的三分类（tau=0.7）：**5.8% clean / 50.9% α_eff-binding / 43.3% ESS-binding**
- 论文的 38.2%/59.8%/~2% 全部来自 tau=0.8 旧实验
- 还有 micro-batch 总数不一致：results.tex 说 25,991，实际 tau07_seed42 有 24,412

### 修正建议

统一更新为 tau=0.7 的真实数据。Appendix 改为 "5.8% clean, 50.9% α_eff-binding, 43.3% ESS-binding"。results.tex 对应修改。micro-batch 总数改为 24,412。

---

## 问题 3：R² 0.47→0.44 来源

### 查到的原始数据

**R²=0.47→0.44 出处**：`/root/provenance_weight_training/alpha_eff_variance_decomposition.json`，由 `variance_decomp_v3.py` 的模拟产出：
- B=4: R²\_adp = 0.4709（α_eff(**b\***) vs true_fraction 的 Pearson R²）
- B=16: R²\_adp = 0.4407

**Appendix K Table alpha\_corr 的 r=0.706→0.707**：
- 测量的是 α_eff(**0**) vs true batch real fraction
- B=4: r=0.706 → R²=0.498
- B=16: r=0.707 → R²=0.500

**这是两个不同指标**：
| 指标 | B=4 | B=16 | 来源 |
|------|------|------|------|
| R²(α\_eff(b\*), true) | 0.471 | 0.441 | 模拟 |
| R²(α\_eff(0), true) | 0.498 | 0.500 | Appendix table |

**额外问题**：`variance_decomp_v3.py` 的模拟使用了 `adaptive_tau`（tau_delta=0.3, tau_min=0.5），但实际训练用的是 `adaptive_tau=false`。模拟与训练配置不匹配。

### 结论

- 0.47→0.44 来自模拟的 R²(α_eff(b\*), true)，是真实计算出的值
- Appendix K 的 r=0.706→0.707 测量的是 R²(α_eff(0), true)=0.498→0.500
- discussion.tex line 69 说 "r≈0.70, explaining ~49% of variance"，但 line 74 接着说 "R²=0.47→0.44"，读者会误认为这是同一个 R²。实际上是不同指标
- 模拟用了 adaptive_tau 但训练没有，数据不可比

### 修正建议

discussion.tex line 74 应明确区分两个指标。建议改写为：
"Scaling from B=4 to B=16 reduces per-batch α_eff variance by 10.25×. The proxy-to-ground-truth correlation R²(α_eff(0), true) remains stable (0.50 → 0.50; Table X), confirming that the ceiling is set by detector quality."

如果要保留 0.47→0.44，需注明这是 α_eff(b\*) 而非 α_eff(0) 的 R²，并修复模拟中的 adaptive_tau 配置使其与训练一致。

---

## 问题 4：Qwen uniform downstream eval 路径

### 查到的原始数据

**`qwen_uniform_downstream` 目录**：
```
/root/autodl-tmp/provenance_weight_training/output/eval/qwen_uniform_downstream/
  __root__autodl-tmp__provenance_weight_training__output__models__llama3b_uniform_seed42__final/
    results_2026-05-18T02-13-58.029068.json
```
- 该 eval 评估的是 **Llama-3.2-3B uniform** 模型，不是 Qwen 0.6B
- ARC-Easy acc = 0.722（Llama 3B 的值）

**论文引用的正确数据来源**：
```
/root/autodl-tmp/provenance_weight_training/output/eval_results/uniform_seed42_downstream/
  __root__autodl-tmp__provenance_weight_training__output__models__qwen06b_uniform_seed42_v2__final/
    results_2026-05-20T11-39-04.925081.json
```
- ARC-Easy acc = **0.6574** ≈ 论文的 0.657 ✓
- ARC-Challenge acc_norm = 0.348 ✓
- HellaSwag acc_norm = 0.484 ✓
- PIQA acc = 0.686 ✓

**项目内部已知此问题**（`downstream_multiseed_summary.md` line 55）：
> "/tmp/qwen_uniform_downstream.log contains Llama-3.2-3B results (not Qwen 0.6B), excluded from this comparison."

### 结论

- `qwen_uniform_downstream` 目录确实指向了错误模型（Llama 3B）
- 但论文 Table O 的 Uniform 数值来自**另一个正确的 eval**（`eval_results/uniform_seed42_downstream/`），数值正确
- **论文数值无误**，但服务器上存在误导性的目录命名

### 修正建议

无需修改论文数值。建议清理或重命名服务器上的 `qwen_uniform_downstream` 目录以避免后续混淆。

---
