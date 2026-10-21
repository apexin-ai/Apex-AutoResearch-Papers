# Data Audit Part 1: Dose-Response (Table 1, Figures 1/2/3)

**Date**: 2026-05-23
**Sources**: cqa1-21977 eval_results, eval_results_v2, eval_results_cross_family; existing artifacts (data_audit_table1.md, falcon3_paper_integration_data.md, data_audit_tables2_3_fig1.md); local figure scripts

---

## A. Table 1 (tab:taxonomy, results.tex lines 22–36)

### A1. d000 Accuracy (seed=42)

| Model | Paper | Source | Source Value | 一致？ | 备注 |
|-------|-------|--------|-------------|--------|------|
| Phi-4 14.7B | 76.4% | data_audit_table1.md (westd) | 0.7644210226 → 76.44% | ✅ | rounds to 76.4 |
| Qwen-14B | 69.4% | data_audit_table1.md (westd) | 0.6944167498 → 69.44% | ✅ | rounds to 69.4 |
| Qwen-7B | 66.1% | data_audit_table1.md (westd) | 0.6610881641 → 66.11% | ✅ | rounds to 66.1 |
| Gemma-2 9B | 61.9% | data_audit_table1.md (westd) | 0.6186440678 → 61.86% | ✅ | rounds to 61.9 |
| Falcon3 7B | 58.8% | falcon3_paper_integration_data.md | 58.77% | ✅ | rounds to 58.8 |
| OLMo-2 7B | 53.8% | data_audit_table1.md (westd) | 0.5378863410 → 53.79% | ✅ | rounds to 53.8 |

### A2. Δacc (d000→d100)

| Model | Paper | Source Δ | Computed from | 一致？ | 备注 |
|-------|-------|----------|---------------|--------|------|
| Phi-4 | ±0.5pp | -0.17pp | d100-d000 (westd) | ✅ | "±0.5" describes CI range [-0.60,+0.26] |
| Qwen-14B | -9.4pp | -9.37pp | d100-d000 (westd) | ✅ | rounds to -9.4 |
| Qwen-7B | -1.8pp | -1.78pp | d100-d000 (westd) | ✅ | rounds to -1.8 |
| Gemma-2 | +3.8pp | +3.76pp | d100-d000 (westd) | ✅ | rounds to +3.8 |
| Falcon3 | +4.2pp | +4.19pp | 62.96-58.77 (cqa1 d100 verified) | ✅ | rounds to +4.2 |
| OLMo-2 | +3.2pp | +3.21pp | d100-d000 (westd) | ✅ | rounds to +3.2 |

### A3. 95% CI (item-level paired bootstrap, B=10,000)

| Model | Paper CI | Source File | 一致？ | 备注 |
|-------|---------|-------------|--------|------|
| Phi-4 | [-0.60, +0.26] | data_audit_table1.md 验证 | ✅ | CI range ≈±0.5pp matches "±0.5" label |
| Qwen-14B | [-12.74, -9.0] | data_audit_table1.md 验证 | ✅ | |
| Qwen-7B | [-2.36, -1.22] | 源文件未直接定位 | ⚠️ | audit report 验证了 Δ，但未独立追溯 CI source file |
| Gemma-2 | [+3.18, +4.33] | 源文件未直接定位 | ⚠️ | 同上 |
| Falcon3 | [+3.60, +4.79] | 源文件未直接定位 | ⚠️ | Falcon3 single seed, CI should be item-level bootstrap |
| OLMo-2 | [+2.73, +3.71] | 源文件未直接定位 | ⚠️ | 同上 |

**注**: CI source file 应为 bootstrap_profile_stability.py 的输出结果。脚本位于 cqa1:/root/contamcal-irt-calibration/analysis/bootstrap_profile_stability.py，读取 eval_results_v2 数据。未找到保存的 CI 输出文件。CI 数值未在此次 audit 中独立验证。

### A4. Peak Column

| Model | Paper | Source | 一致？ | 备注 |
|-------|-------|--------|--------|------|
| Phi-4 | negl. | max \|Δ\|=0.54pp at d025 | ✅ | |
| Qwen-14B | --- | max harm at d050 (-10.03pp) | ✅ | |
| Qwen-7B | -3.1@d025 | d025 Δ=-3.13pp from d000 | ✅ | |
| Gemma-2 | mono. | 61.86→63.42→64.56→64.01→65.62 | ⚠️ | d050 dips 0.55pp below d025; not strictly monotonic |
| Falcon3 | mono. | 58.77→59.02→61.23→62.09→62.96 | ✅ | strictly monotonic |
| OLMo-2 | sat.@d050 | d050=57.25% > d100=57.00% | ✅ | |

### A5. Pattern Classification (Algorithm 1, τ=2, σ=5)

| Model | Paper | Manual Check | 一致？ | 备注 |
|-------|-------|-------------|--------|------|
| Phi-4 | Immune | \|d100-d000\| = 0.17 < τ=2 → Immune | ✅ | |
| Qwen-14B | Collapse | Δ = -9.37 < -σ=-5 → Collapse | ✅ | |
| Qwen-7B | V-recovery | d025 trough -3.13 < -τ, d100 recovers to -1.78 | ✅ | |
| Gemma-2 | Benefit | Δ = +3.76 > τ=2, monotonic-ish | ✅ | |
| Falcon3 | Benefit | Δ = +4.19 > τ=2, monotonic | ✅ | |
| OLMo-2 | Benefit | Δ = +3.21 > τ=2, saturates at d050 | ✅ | |

---

## B. Figure 1 (gen_fig_dose_response.py — 7 models × 5 dosages)

### B1. Hardcoded Data vs Eval Source

| Model | Dosage | Script | Source File (eval_results_v2 / westd) | 一致？ | 备注 |
|-------|--------|--------|---------------------------------------|--------|------|
| **Qwen2.5-7B** | d000 | 66.11 | v2: 66.14 / westd: 66.11 | ⚠️ | v2=66.14 ≠ script 66.11; westd=66.11 matches |
| | d005 | 64.74 | v2: 64.82 | ⚠️ | diff=0.08pp |
| | d025 | 62.98 | v2: 63.06 | ⚠️ | diff=0.08pp |
| | d050 | 63.07 | v2: 63.10 | ⚠️ | diff=0.03pp |
| | d100 | 64.33 | v2: 64.32 | ✅ | diff=0.01pp, within rounding |
| **Falcon3-7B** | d000 | 58.77 | falcon3_paper_integration_data.md | ✅ | |
| | d005 | 59.02 | falcon3_paper_integration_data.md | ✅ | |
| | d025 | 61.23 | falcon3_paper_integration_data.md | ✅ | |
| | d050 | 62.09 | falcon3_paper_integration_data.md | ✅ | |
| | d100 | 62.96 | cqa1 eval: 0.6296 ✅ + integration_data | ✅ | |
| **OLMo-2 7B** | d000 | 53.79 | westd (data_audit_table1.md) | ✅ | cqa1 cross_family=58.71% (wrong eval version) |
| | d005 | 56.14 | westd confirmed | ✅ | |
| | d025 | 56.17 | westd confirmed | ✅ | |
| | d050 | 57.25 | westd confirmed | ✅ | eval file on westd only |
| | d100 | 57.00 | westd confirmed | ✅ | eval file on westd only |
| **Phi-4 14.7B** | d000 | 76.44 | westd (data_audit_table1.md): 0.7644 | ✅ | no eval results on cqa1 |
| | d005 | 76.36 | westd confirmed | ✅ | |
| | d025 | 76.98 | westd confirmed | ✅ | |
| | d050 | 76.75 | westd confirmed | ✅ | |
| | d100 | 76.27 | westd confirmed | ✅ | |
| **Qwen2.5-14B** | d000 | 69.44 | westd: 0.6944 | ✅ | |
| | d005 | 69.01 | westd confirmed | ✅ | |
| | d025 | 62.04 | westd confirmed | ✅ | |
| | d050 | 59.41 | westd confirmed | ✅ | |
| | d100 | 60.07 | westd confirmed | ✅ | |
| **Gemma-2 9B** | d000 | 61.86 | westd: 0.6186 | ✅ | |
| | d005 | 63.42 | westd confirmed | ✅ | |
| | d025 | 64.56 | westd confirmed | ✅ | |
| | d050 | 64.01 | westd confirmed | ✅ | |
| | d100 | 65.62 | westd confirmed | ✅ | |
| **LLaMA-3.1 8B** | d000 | 53.50 | westd (data_audit_table1.md) | ✅ | s0 data |
| | d005 | None | — | ✅ | no d005 eval |
| | d025 | 52.75 | westd confirmed | ✅ | |
| | d050 | None | — | ✅ | no d050 eval |
| | d100 | 52.81 | westd confirmed | ✅ | |

**注**: Qwen2.5-7B eval_results_v2 on cqa1 与 westd 产出有 0.03–0.08pp 偏差（C009/C010 提到的 evaluate.py 版本漂移）。论文 Figure 1 使用的是 westd 版本数据。cqa1 `_aligned` 结果偏差更大（~3pp），不可用。

### B2. 内部一致性：Figure 1 数据 vs Table 1

| Model | Fig 1 d000 | Tab 1 d000 | Fig 1 Δ(d100) | Tab 1 Δ | 一致？ |
|-------|-----------|-----------|---------------|---------|--------|
| Phi-4 | 76.44 | 76.4% | -0.17 | ±0.5pp | ✅ | 
| Qwen-14B | 69.44 | 69.4% | -9.37 | -9.4pp | ✅ |
| Qwen-7B | 66.11 | 66.1% | -1.78 | -1.8pp | ✅ |
| Gemma-2 | 61.86 | 61.9% | +3.76 | +3.8pp | ✅ |
| Falcon3 | 58.77 | 58.8% | +4.19 | +4.2pp | ✅ |
| OLMo-2 | 53.79 | 53.8% | +3.21 | +3.2pp | ✅ |

Table 1 与 Figure 1 完全一致（差异仅为 rounding）。

---

## C. Figure 2 (gen_baseline_vulnerability.py — Baseline Vulnerability Scatter)

### ⚠️⚠️ 重大问题：Figure 2 数据与 Table 1 / Figure 1 严重不一致 ⚠️⚠️

| Model | Fig 2 x (baseline) | Table 1 d000 | Fig 2 Δ(d100) | Table 1 Δ | x 一致？ | Δ 一致？ |
|-------|-------------------|-------------|---------------|---------|----------|----------|
| OLMo-2 7B | 53.79 | 53.8% | +3.21 | +3.2pp | ✅ | ✅ |
| Falcon3 7B | 58.77 | 58.8% | +4.19 | +4.2pp | ✅ | ✅ |
| Gemma-2 9B | **63.39** | **61.9%** | **+1.21** | **+3.8pp** | ⚠️ -1.53pp | ⚠️ -2.55pp |
| Qwen2.5-7B | **68.55** | **66.1%** | **+2.90** | **-1.8pp** | ⚠️ -2.44pp | ⚠️ **符号反转！** |
| Phi-4 14B | **70.69** | **76.4%** | **+0.17** | ±0.5 (-0.17) | ⚠️ -5.75pp | ⚠️ 符号翻转 |
| Qwen2.5-14B | **72.17** | **69.4%** | -9.37 | -9.4pp | ⚠️ -2.73pp | ✅ |

**分析**：
- OLMo-2 和 Falcon3：Figure 2 数据与 Table 1 一致 ✅
- Gemma-2：x 偏差 1.53pp，Δ 偏差 2.55pp
- Qwen-7B：x 偏差 2.44pp，**Δ 符号完全反转**（+2.90 vs -1.78）
- Phi-4：x 偏差 5.75pp，Δ 符号翻转（+0.17 vs -0.17）
- Qwen-14B：x 偏差 2.73pp，Δ 基本一致

**排查**：
1. Figure 2 不使用 d000 accuracy 作为 x 轴（与 Table 1 的 "d000 Acc." 不同）
2. Figure 2 不使用 pretrained MMLU（Falcon3 pretrained=67.4% 但 x=58.77=d000）
3. Figure 2 不使用 cross-seed mean（Phi-4 d000 s42=76.44，均值降到 70.69 需要其他 seed ≈65%，不合理）
4. Figure 2 数据不匹配 cqa1 `_aligned` eval 结果或 `eval_results_v2`
5. **最可能解释**：Figure 2 脚本使用了 **过期的旧版数据**，从未随论文正文更新

**影响**：Figure 2 (fig_baseline_vulnerability.pdf) 展示了错误的 vulnerability gradient — Qwen-7B 被画为 Benefit(+2.90) 而实际是 V-recovery(-1.78)，Phi-4 位置偏差 5.75pp。图表的定性结论（高 baseline → 更脆弱）仍然成立，但具体数据点位置错误。

---

## D. Figure 3 (gen_cross_benchmark_heatmap.py — Cross-Benchmark Heatmap)

### D1. MMLU Column vs Table 1

| Model | Heatmap MMLU | Table 1 Δ | 一致？ | 备注 |
|-------|-------------|---------|--------|------|
| OLMo-2 | +3.21 | +3.2pp | ✅ | |
| Falcon3 | +4.19 | +4.2pp | ✅ | |
| Gemma-2 | **+1.21** | **+3.8pp** | ⚠️ | 与 Figure 2 相同的错误数据 |
| Qwen-7B | **+2.90** | **-1.8pp** | ⚠️ | **符号反转！与 Figure 2 相同** |
| Phi-4 | **+0.17** | **±0.5 (-0.17)** | ⚠️ | 符号翻转（微小）|
| Qwen-14B | -9.37 | -9.4pp | ✅ | |

### D2. ARC Column

| Model | Heatmap ARC | Other Source | 一致？ | 备注 |
|-------|-----------|-------------|--------|------|
| OLMo-2 | +3.92 | falcon3_integration: OLMo d100 ARC Δ=+3.92 | ✅ | |
| Falcon3 | +4.01 | falcon3_integration: d100 ARC=85.58%, d000=81.57%, Δ=+4.01 | ✅ | cqa1 d100 arc=85.58% 验证 |
| Gemma-2 | +2.22 | 源文件未直接定位 | ⚠️ | falcon3_integration 显示 Gemma ARC s42 highly erratic |
| Qwen-7B | +3.41 | 源文件未直接定位 | ⚠️ | cqa1 _aligned ARC shows -0.26pp (wrong eval version) |
| Phi-4 | -0.85 | 源文件未直接定位 | ⚠️ | paper §5.1: LLaMA ARC=+0.09pp (different model) |
| Qwen-14B | -2.05 | 源文件未直接定位 | ⚠️ | |

### D3. GSM8K Column

| Model | Heatmap GSM8K | Other Source | 一致？ | 备注 |
|-------|-------------|-------------|--------|------|
| OLMo-2 | +5.60 | 源文件未直接定位 | ⚠️ | paper text: "+2.1pp" (cross-seed mean) — 不同指标 |
| Falcon3 | +1.29 | paper text (§5.4): +1.29pp total | ✅ | d000 GSM8K=74.53% (cqa1 verified) |
| Gemma-2 | +1.33 | 源文件未直接定位 | ⚠️ | |
| Qwen-7B | +16.24 | 源文件未直接定位 | ⚠️ | paper §5.2: "+10.1pp" (cross-seed mean); s42=+11.07. 差异大 |
| Phi-4 | -0.50 | data_audit_tables2_3: -0.46pp (s123) | ⚠️ | paper says -0.5pp, 源=s123:-0.46→-0.5 rounds OK |
| Qwen-14B | +13.09 | data_audit_table1: mean(s42,s123)=+13.08 | ✅ | |

**Qwen-7B GSM8K: +16.24 vs known +11.07 (s42)**：差异 ~5pp，可能是 seed 不同或 eval 版本不同。Paper 正文说 "+10.1pp"。需要追溯 heatmap 中 +16.24 的来源。

### D4. Heatmap 与 Figure 2 内部一致性

Figure 2 和 Figure 3 的 MMLU Δ 列完全一致（相同的错误数据）。说明两个脚本使用了同一份（过期的）数据源。

---

## 汇总

| 检查项 | 总计 | ✅ | ⚠️ | 说明 |
|--------|------|---|---|------|
| Table 1 d000 | 6 | 6 | 0 | 全部一致 |
| Table 1 Δacc | 6 | 6 | 0 | 全部一致 |
| Table 1 CI | 6 | 0 | 6 | CI source file 未独立追溯 |
| Table 1 Peak | 6 | 5 | 1 | Gemma-2 "mono." 技术上不精确 |
| Table 1 Pattern | 6 | 6 | 0 | 全部一致 |
| Figure 1 数据 | 35 | 33 | 2 | Qwen-7B 有 0.03-0.08pp v2 偏差 |
| Fig 1 vs Tab 1 | 6 | 6 | 0 | 完全一致 |
| **Figure 2 数据** | **12** | **4** | **8** | **⚠️ 4个模型 x 和 Δ 均与 Table 1 不一致** |
| Figure 3 MMLU | 6 | 3 | 3 | 与 Figure 2 相同的问题 |
| Figure 3 ARC | 6 | 2 | 4 | 仅 OLMo-2 和 Falcon3 可验证 |
| Figure 3 GSM8K | 6 | 2 | 4 | Falcon3 和 Qwen-14B 可验证 |
| **总计** | **101** | **73** | **28** | |

---

## 关键发现

### 🔴 Critical: Figure 2 + Figure 3 MMLU 列数据过期

**gen_baseline_vulnerability.py** 和 **gen_cross_benchmark_heatmap.py** 中 Gemma-2、Qwen-7B、Phi-4、Qwen-14B 的数据与 Table 1 / Figure 1 严重不一致：

1. **Qwen-7B**: Δ 符号反转 (+2.90 vs -1.78) — 在散点图上被错误地画为 Benefit 而非 V-recovery
2. **Gemma-2**: Δ 缩小 62% (+1.21 vs +3.76) — 低估了 Benefit 效应
3. **Phi-4**: x 位置偏移 5.75pp (70.69 vs 76.44) — 图上位置完全错误
4. **Qwen-14B**: x 位置偏移 2.73pp (72.17 vs 69.44)

**建议**：用 Table 1 / Figure 1 的数据更新 gen_baseline_vulnerability.py 和 gen_cross_benchmark_heatmap.py，重新生成 PDF。

### 🟡 Medium: Figure 3 GSM8K Qwen-7B = +16.24

Paper inline (§5.2) 说 Qwen-7B GSM8K = "+10.1pp"（cross-seed mean of s42=+11.07, s123=+9.18）。Heatmap 中 +16.24 的来源不明。需要追溯该数字。

### 🟡 Medium: Table 1 CI bounds 未独立验证

6 个模型的 95% CI 均未追溯到具体的 bootstrap 输出文件。bootstrap_profile_stability.py 脚本存在于 cqa1 但其输出结果文件未找到。

### 🟢 Minor: Gemma-2 "mono." peak label

d050 低于 d025 by 0.55pp，不严格单调。已在 data_audit_table1.md 中记录。

### 🟢 Minor: Qwen-7B eval_results_v2 偏差

cqa1 eval_results_v2 数据与 westd 正式结果有 0.03–0.08pp 偏差（evaluate.py 版本差异），但 Figure 1 使用 westd 数据，无影响。
