# Table 3 数据修复 + 94.4% 引用修复报告

## 1. SC Baseline 调查结果

### 数据来源确认

每个 generator 的 NLI combo 实验结果文件（westd-16639）：

| Generator | 结果文件 | 文件中 SC | 论文 SC | 差异 |
|-----------|---------|----------|--------|------|
| Mistral-7B | `r11_3verifier_canonical.json` | 39.33% (236/600) | 39.33% | ✅ 一致 |
| LLaMA-3.1-8B | `exp092_llama8b_pw_nli_combo/results.json` | 70.00% (420/600) | 72.50% | ❌ -2.50pp |
| Qwen2.5-14B | `qwen14b_pw_nli_combo/results.json` | 73.50% (441/600) | 74.00% | ❌ -0.50pp |
| Qwen3-14B | `d116_qwen3_pw_deberta_large/results.json` | 85.00% (510/600) | 85.83% | ❌ -0.83pp |

### 72.50% 的来源

`artifacts/nli_recompute_exp091_exp092.json`（2026-05-22 tiebreaking 修复记录）确认：
- combo 实验的 SC baseline 始终是 70.00%（LLaMA）和 73.50%（Qwen2.5）
- 72.50% 来自 **finetuned DeBERTa combo 实验**（`deberta_ft_combo_all_fixed/results.json`，`llama8b.sc_baseline = 0.725`），是不同实验的不同 traces，被错误地用到了 zero-shot Table 3

### Multi-seed 验证

LLaMA-3.1-8B multi-seed SICA 实验的 SC 值：
- seed42: 72.20% (n=223, 不完整)
- seed123: 71.33% (n=600)
- seed456: 73.55% (n=121, 不完整)
- seed789: 74.30% (n=323, 不完整)

均不是 72.50%。combo 实验（n=600, SC=70.00%）是 Table 3 的唯一正确来源。

---

## 2. Table 3 修正值

### 修正后的 Table 3 (tab:cross_generator_nli, w=3)

| Generator | Family | SC | Gap | Combo Δ (w=3) | p |
|-----------|--------|------|------|-------------|---|
| Mistral-7B | Mistral | 39.33% | +15.67 | +6.67pp | <0.001 |
| **LLaMA-3.1-8B** | LLaMA | **70.00%** | **-15.00** | **+3.33pp** | **0.052** |
| **Qwen2.5-14B** | Qwen | **73.50%** | **-18.50** | **+1.17pp** | **0.230** |
| **Qwen3-14B** | Qwen | **85.00%** | **-30.00** | **+1.00pp** | **0.146** |

### 数据溯源

- **LLaMA SC=70.00%**: `exp092_llama8b_pw_nli_combo/results.json` → `sc_baseline: 0.7`
- **LLaMA w3 Δ=+3.33pp**: 同文件 → `combo.w3.delta_pp: 3.33`
- **LLaMA w3 p=0.052**: 同文件 → `combo.w3.mcnemar_p: 0.0519`（四舍五入）
- **Qwen2.5 SC=73.50%**: `qwen14b_pw_nli_combo/results.json` → `sc_baseline: 0.735`
- **Qwen2.5 w3 Δ=+1.17pp**: 同文件 → `combo.w3.delta_pp: 1.17`
- **Qwen2.5 w3 p=0.230**: 同文件 → `combo.w3.mcnemar_p: 0.2295`
- **Qwen3 SC=85.00%**: `d116_qwen3_pw_deberta_large/results.json` → `sc_baseline: 0.85`
- **Qwen3 w3 Δ=+1.00pp**: 同文件 → `combo.w3.delta_pp: 1.0`
- **Qwen3 w3 p=0.146**: 同文件 → `combo.w3.mcnemar_p: 0.146`

---

## 3. BH 校正重算

### 新的 12 条件 BH 校正（m=12, α=0.05）

| Rank | Condition | Raw p | BH-adjusted p | Significant? |
|------|-----------|-------|---------------|-------------|
| 1 | Mistral w5 | 6.18e-7 | 7.42e-6 | *** |
| 2 | Mistral w3 | 1.13e-5 | 6.78e-5 | *** |
| 3 | **LLaMA w1** | **0.0012** | **0.0048** | *** → **新增** ** |
| 4 | LLaMA w3 | 0.0519 | 0.125 | |
| 5 | Qwen3 w5 | 0.0522 | 0.125 | |
| 6 | Qwen3 w1 | 0.125 | 0.250 | |
| 7 | Qwen3 w3 | 0.146 | 0.250 | |
| 8 | Qwen2.5 w5 | 0.1934 | 0.290 | |
| 9 | Qwen2.5 w3 | 0.2295 | 0.306 | |
| 10 | Qwen2.5 w1 | 0.3438 | 0.385 | |
| 11 | Mistral w1 | 0.359 | 0.385 | |
| 12 | LLaMA w5 | 0.3846 | 0.385 | |

**关键变化**: 显著条件从 2 个变为 3 个。LLaMA-3.1-8B w=1（+3.33pp, p_BH=0.0048）在 BH 校正后显著。

---

## 4. 94.4% 调查结果

### 来源

diagnosis.tex:118 原文：
> "constraint ablation shows MAX-SAT and count-only agree on 94.4% of predictions (n=804)"

### 数据检查

- `tab:ablation`（appendix.tex:385-400）显示：
  - SICA (MAX-SAT) vs SC agreement: 773/804 = **96.14%**
  - Count-only vs SC agreement: 774/804 = **96.27%**
- grep 所有结果文件，未找到 94.4% 作为 agreement 指标
- `0.944` 出现在日志中均为单个问题的 `satisfied_ratio`（如 34/36=0.944），与全局 agreement 无关
- analysis.tex 已更新为 "≥99%"（引用 tab:alpha-ablation，FOLIO n=204 数据，正确）

### 结论

94.4% 无法追溯到任何结果文件，可能来自早期版本计算。已修正为引用 tab:ablation 的实际数据（>96%）。

---

## 5. 已执行的修改

### 5.1 solutions.tex

| 位置 | 修改内容 |
|------|---------|
| Line 12 | "SC ≥ 72%" → "all three generators above the verifier"; "Δ ≤ +0.83pp" → "Δ ≤ +3.33pp" |
| Line 15 | "47-point" → "46-point"; "Δ ≤ +0.83pp" → "Δ ≤ +3.33pp"; 添加 LLaMA w=1 显著性说明 |
| Line 27 | LLaMA: SC 72.50→70.00, Gap -17.50→-15.00, Δ +0.83→+3.33, p 0.665→0.052 |
| Line 28 | Qwen2.5: SC 74.00→73.50, Gap -19.00→-18.50, Δ +0.67→+1.17, p 0.503→0.230 |
| Line 29 | Qwen3: SC 85.83→85.00, Gap -30.83→-30.00, Δ +0.50→+1.00, p 0.45→0.146 |

### 5.2 appendix.tex

| 位置 | 修改内容 |
|------|---------|
| Line 938 | "SC ≥ 72%" → "above-verifier generators"; "two of twelve" → "three of twelve"; 添加 LLaMA w=1 |
| Line 948 (caption) | "Two of twelve" → "Three of twelve"; 添加 {**} 标注 |
| Lines 955-973 | Table 28 全部数据更新：SC、Gap、Δ、p_raw、p_BH、significance markers |

### 5.3 diagnosis.tex

| 位置 | 修改内容 |
|------|---------|
| Line 118 | "MAX-SAT and count-only agree on 94.4%" → "both MAX-SAT and count-only each agree with SC on >96% (Table ref)" |

### 5.4 figures/gen_capability_gap_scatter.py

| 位置 | 修改内容 |
|------|---------|
| Line 32 | Qwen3 PW-D5: (-30.83, 0.50) → (-30.00, 1.00) |
| Line 33 | Qwen2.5 PW-D5: (-19.00, 0.67) → (-18.50, 1.17) |
| Line 39 | LLaMA: (-17.50, 0.83) → (-15.00, 3.33) |
| Annotations | 对应坐标更新 |

---

## 6. 级联影响（需 Director 决策）

### 6.1 Figure 7 (capability_gap_scatter) 需要重新生成

figure 脚本已更新，但 PDF 需要在服务器上重新运行 Python 生成。LLaMA 数据点从 (gap=-17.5, Δ=0.83) 移动到 (gap=-15.0, Δ=3.33)，图形外观会有明显变化。

### 6.2 叙事影响（CRITICAL）

修正后的数据改变了论文的一个核心论点：

**旧叙事**: "只有 Mistral（SC 低于 verifier）获得显著提升；所有 SC ≥ 72% 的 generator 无显著提升（Δ ≤ 0.83pp）" — 干净的 capability gap 二分法。

**新叙事**: LLaMA-3.1-8B（SC=70%, 高于 verifier 的 55%）在 w=1 时获得 **BH 校正后显著** 的 +3.33pp（p_BH=0.0048）。这意味着：
1. Capability gap 不是简单的 "低于 verifier 才有效"
2. 即使 SC 高于 verifier 15pp 的 generator 也能从外部验证中获益
3. 不过 w=3 时 LLaMA 的 p=0.052 未通过 BH，且 gain 随 SC 增加仍单调递减

**建议**: capability-gap pattern 仍然成立（monotonically decreasing），但 breakeven point 的描述需要调整。当前文本已添加 LLaMA w=1 显著性的注释，Director 可能需要进一步调整叙事框架。

### 6.3 Qwen3-14B SC 在 experiments.tex 和 diagnosis.tex 中可能也有误

experiments.tex:37 和 diagnosis.tex:34 的主 SICA 结果表显示 Qwen3 SC=85.83%，但 exp033（SICA 实验）的 `sc_accuracy=0.85`（85.00%）。这是 Table 3 之外的另一个潜在不一致，建议 Director 单独核查。

### 6.4 Finetuned table (tab:finetuned-nli) Mistral SC 微小差异

finetuned combo 数据文件显示 Mistral `sc_baseline=0.3917`（39.17%），但表中写 39.33%。差异 0.17pp（1 个问题），可能来自 tiebreaking 差异。建议 Director 核查是否需要修正。

### 6.5 Spearman 相关性可能需要重算

solutions.tex:15 引用 "Spearman ρ=1.0, p=0.003, n=6"。数据点变化后，排序可能仍然完美单调（monotonically decreasing verified: 6.67 > 3.33 > 1.17 > 1.00），但 Spearman 统计量应基于新数据重新验证。
