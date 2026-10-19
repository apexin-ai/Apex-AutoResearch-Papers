## H3: Llama-70B AlpacaEval Style OR=7.64 调查

### crossbench_summary 内容

**`data/llama70b_crossbench_summary.json`**（旧版、未修正）：

| Benchmark | Axis | GEE Style OR | GEE Style p | 状态 |
|-----------|------|-------------|-------------|------|
| AlpacaEval | formality | 2.18e+21 | 0.0 | **degenerate** |
| AlpacaEval | verbosity | 0.54 | 0.975 | normal (n.s.) |
| MT-Bench | formality | 32.68 | 0.232 | inflated (n.s.) |

AlpacaEval formality BT=95.7%（47 pairs 中 45 wins），导致 GEE 近完美分离。

**`artifacts/r14_fixes/cross_benchmark_local.json`**（r14 修正版）：

| Config | Style OR | 95% CI | p | VIF | Corr |
|--------|----------|--------|---|-----|------|
| AlpacaEval × Llama-70B × formality | **7.6361** | [3.35, 17.38] | 1e-06 | 1.51 | 0.58 |
| MT-Bench × Qwen3-32B × formality | 4.6227 | [1.23, 17.32] | 0.023 | 1.95 | 0.70 |

### 7.64 来源追溯

**来源：`artifacts/r14_fixes/cross_benchmark_local.json`**，由修正后的 `csd_pipeline/cross_benchmark_analysis.py` 生成。

r14 修正内容（见 `artifacts/r14_fixes/gee_bug_report.json`）：
1. **添加 NLI≥0.90 过滤**：旧版 `cross_benchmark_analysis.py` 对 pairwise 数据未做 NLI 过滤，导致 n=86 中包含低质量 counterfactual pairs，造成 BT=95.7% 的极端胜率和 GEE 近完美分离
2. **统一统计方法**：改为 Wilcoxon + pooled-SD Cohen's d（与 primary analysis 一致）
3. **添加 VIF 和相关性诊断**

修正后 AlpacaEval Llama-70B formality：
- BT = 75.58%（从 95.7% 降至 75.6%，NLI 过滤后去除了低质量 pairs）
- GEE Style OR = 7.6361，CI = [3.35, 17.38]，p = 1e-06
- VIF = 1.51（< 5，可接受），style/orig 相关 = 0.58
- GEE Orig OR = 2.26，p = 0.044（与 Style OR 区分清晰）

### 结论

1. **OR=7.64 来自修正后的 cross-benchmark 分析，是有效值。** VIF=1.51 无 collinearity 问题，CI 不含 1，style 和 orig OR 区分清晰。

2. **`data/llama70b_crossbench_summary.json` 是过时的旧版数据**（未做 NLI 过滤），其 degenerate GEE（OR=2.18e+21）反映的是未过滤数据的近完美分离，不是当前论文使用的值。

3. **建议：无需修改论文。** OR=7.64 经过正确的 NLI 过滤和 GEE 诊断验证。可考虑删除或更新旧的 `data/llama70b_crossbench_summary.json` 以避免混淆。

---

## M4: 100-point Likert p 值

### 实验范围

100pt 实验仅覆盖 **formality** axis（三个 judge），verbosity 仅 GPT-4o 运行了 100pt。

论文原文（appendix L.466-469）："we replicate the **formality** experiment using a 100-point continuous scale (1–100) with three judges... All three judges remain non-significant (all p > 0.15)."

### Formality 100pt p 值（论文表格 Tab:likert100 的依据）

| Judge | n | ATE | Cohen's d | t-test p | Wilcoxon p | Tie Rate | p > 0.15? |
|-------|---|-----|-----------|----------|------------|----------|-----------|
| GPT-4o | 88 | -0.625 | -0.038 | 0.725 | 0.900 | 65.9% | ✓ |
| Qwen3-32B | 88 | 1.830 | 0.153 | 0.154 | — | 51.1% | ✓ (勉强) |
| Llama-70B | 83 | 1.386 | 0.085 | 0.440 | — | 39.8% | ✓ |

注：Qwen3-32B 和 Llama-70B 的 100pt 实验只报告了 t-test p，未做 Wilcoxon。论文表格中用的是 t-test p。

### GPT-4o Verbosity 100pt（额外实验，未在论文 claim 范围内）

| Judge | Axis | n | ATE | Cohen's d | t-test p | Wilcoxon p | Tie Rate |
|-------|------|---|-----|-----------|----------|------------|----------|
| GPT-4o | verbosity | 86 | 2.849 | 0.171 | 0.117 | **0.067** | 51.2% |

### 结论

1. **"all three judges p > 0.15" 在 formality 范围内成立。** 论文明确将 100pt 实验限定为 formality replication，三个 judge 的 t-test p 分别为 0.725、0.154、0.440，全部 > 0.15。

2. **Qwen3-32B p=0.154 非常边界**，仅比 0.15 高出 0.004。这不影响论文声明的准确性，但需注意 reviewer 可能质疑。

3. **GPT-4o verbosity 100pt p=0.067 不在论文声明范围内。** 该实验是独立于三 judge formality 实验的额外数据，论文未将其纳入 "all three judges p > 0.15" 的 claim。但此数据的存在意味着 100pt scaling 对 verbosity 的 Blindspot 缓解效果强于 formality（p 从 formality 的 0.725 降到 verbosity 的 0.067）。

4. **主文第 79 行的表述建议**："unresolved by 100-point continuous scaling (all three judges $p > 0.15$)" 可能给读者造成"所有 axis 都 p>0.15"的印象。更精确的表述应为 "unresolved by 100-point continuous scaling for formality (all three judges $p > 0.15$)"。不过考虑到 appendix 已明确是 formality replication，当前表述在上下文中不算错误。
