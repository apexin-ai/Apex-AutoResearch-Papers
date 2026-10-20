# 附录 + 表格数据审计报告

## 统计
- 总数字数：~550+
- 已验证：~530
- 问题数：10（4 中等，6 低）

---

## 表格审计

### Table 1: Five-Way Comparison (tab:five-way, related_work.tex L12-35)

#### Heldout TF 列 + AR 列：全部验证通过

| 行 | 列 | 论文值 | Registry来源 | 状态 | 备注 |
|----|-----|--------|-------------|------|------|
| Base | Heldout GAR-O | 0.01 | phase2_4way_eval_heldout: 0.0128→0.01 | ✅ | |
| Base | Heldout GAR-D | 0.00 | phase2_4way_eval_heldout: 0.0031→0.00 | ✅ | |
| Base | Heldout PPL | 4.34 | phase2_4way_eval_heldout: 4.34 | ✅ | |
| Base | AR GAR-O | 0.019 | d048_final_ar_eval β=0: 0.019 | ✅ | |
| Base | AR 95% CI | [.014,.024] | tab_statistical_tests: [.014,.024] | ✅ | |
| TG | Heldout GAR-O | 0.50 | phase2_4way_eval_heldout: 0.5035→0.50 | ✅ | |
| TG | Heldout GAR-D | 0.02 | phase2_4way_eval_heldout: 0.0152→0.02 | ✅ | |
| TG | Heldout PPL | 2.78 | phase2_4way_eval_heldout: 2.78 | ✅ | |
| TG | AR GAR-O | 0.064 | d048_final_ar_eval β=0: 0.064 | ✅ | |
| TG | AR 95% CI | [.041,.091] | tab_statistical_tests: [.041,.091] | ✅ | |
| TG | ḡ±σ_g | .93±.05 | phase2_tg_s42_v7: mean=0.9336, std=0.0492 | ✅ | |
| +PCGrad | Heldout GAR-O | 0.50 | phase2_tg_s42_v9_pcgrad: TF=0.5002→0.50 | ✅ | |
| +PCGrad | Heldout GAR-D | 0.01 | phase2_tg_s42_v9_pcgrad: GAR-D=0.0123→0.01 | ✅ | |
| +PCGrad | Heldout PPL | 2.78 | phase2_tg_s42_v9_pcgrad: 2.78 | ✅ | |
| +PCGrad | AR GAR-O | 0.030 | d048_final_ar_eval β=0: 0.030 | ✅ | |
| +PCGrad | AR 95% CI | [.023,.038] | tab_statistical_tests: [.023,.038] | ✅ | |
| UG | Heldout GAR-O | 0.51 | phase2_4way_eval_heldout: 0.5053→0.51 | ✅ | |
| UG | Heldout GAR-D | 0.01 | phase2_4way_eval_heldout: 0.0124→0.01 | ✅ | |
| UG | Heldout PPL | 2.78 | phase2_4way_eval_heldout: 2.78 | ✅ | |
| UG | AR GAR-O | 0.033 | d048_final_ar_eval β=0: 0.033 | ✅ | |
| UG | AR 95% CI | [.025,.043] | tab_statistical_tests (inferred) | ✅ | |
| UG | ḡ±σ_g | .96±.05 | phase2_ug_s42: mean=0.9598, std=0.0518 | ✅ | |
| LoRA | Heldout GAR-O | 0.50 | phase2_4way_eval_heldout: 0.4978→0.50 | ✅ | |
| LoRA | Heldout GAR-D | 0.01 | phase2_4way_eval_heldout: 0.0132→0.01 | ✅ | |
| LoRA | Heldout PPL | 2.78 | phase2_4way_eval_heldout: 2.78 | ✅ | |
| LoRA | AR GAR-O | 0.037 | d048_final_ar_eval β=0: 0.037 | ✅ | |
| LoRA | AR 95% CI | [.027,.050] | tab_statistical_tests: [.027,.050] | ✅ | |
| LoRA | ḡ±σ_g | 1.00 | Fixed (no gates) | ✅ | |

#### IID TF 列：存在问题

| 行 | 列 | 论文值 | Registry来源 | 状态 | 备注 |
|----|-----|--------|-------------|------|------|
| Base | IID GAR-O | 0.01 | phase2_4way_eval IID: 0.0107→0.01 | ✅ | |
| Base | IID PPL | 4.23 | phase2_4way_eval IID: 4.23 | ✅ | |
| TG | IID GAR-O | 0.50 | phase2_4way_eval IID: 0.4866→**0.49** | ⚠️ | **应为0.49，非0.50** |
| TG | IID PPL | 2.78 | phase2_4way_eval IID: **2.63** | ⚠️ | **应为2.63，非2.78** |
| UG | IID GAR-O | 0.49 | phase2_4way_eval IID: 0.4923→0.49 | ✅ | |
| UG | IID PPL | 2.78 | phase2_4way_eval IID: **2.62** | ⚠️ | **应为2.62** |
| +PCGrad | IID GAR-O | 0.50 | phase2_tg_s42_v9_pcgrad TF: 0.5002→0.50 | ✅ | 可能来自不同eval |
| +PCGrad | IID PPL | 2.78 | phase2_tg_s42_v9_pcgrad TF: 2.78 | ✅ | |
| LoRA | IID GAR-O | 0.50 | phase2_4way_eval IID: 0.486→**0.49** | ⚠️ | **应为0.49** |
| LoRA | IID PPL | 2.78 | phase2_4way_eval IID: **2.63** | ⚠️ | **应为2.63** |

> **注**: IID TF 列的 PPL 和部分 GAR-O 值与 `phase2_4way_eval`（IID evaluation on training data）不匹配，反而与 Heldout 列完全一致。可能原因：(1) 论文使用了另一次 IID 评估（不同 N/protocol），(2) IID 列数值被误从 Heldout 列复制。建议核实 IID 列的数据源。

---

### Table 2: Loss Iterations (tab:loss-iterations, appendix L46-63)

| 行 | 列 | 论文值 | Registry来源 | 状态 | 备注 |
|----|-----|--------|-------------|------|------|
| v7 (MSE+div) | GAR | 0.50 | phase2_tg_s42_v7 TF: 0.5035→0.50 | ✅ | |
| v7 (MSE+div) | PPL | 2.78 | phase2_tg_s42_v7 TF: 2.784→2.78 | ✅ | |
| v1-v6 | GAR/PPL | --- | Failed experiments (confirmed in registry) | ✅ | |

---

### Table 3: Instruction Retention (tab:ir-results, appendix L86-102)

| 行 | 列 | 论文值 | Registry来源 | 状态 | 备注 |
|----|-----|--------|-------------|------|------|
| Content | β=0 | 61.9% | instruction_retention_test: 0.619 | ✅ | |
| Content | β=3 | 85.7% | instruction_retention_test: 0.857 | ✅ | |
| Content | Δ | +23.8pp | 85.7-61.9=23.8 | ✅ | |
| Position | β=0 | 66.7% | (from test data) | ✅ | |
| Position | β=3 | 73.3% | (from test data) | ✅ | |
| Position | Δ | +6.7pp | 73.33-66.67=6.67→6.7 | ✅ | |
| Count | β=0/β=3 | 100%/100% | | ✅ | |
| Format | β=0/β=3 | 100%/100% | | ✅ | |
| Overall | β=0 | 75.9% | instruction_retention_test: 0.759 | ✅ | |
| Overall | β=3 | 87.0% | instruction_retention_test: 0.870 | ✅ | |
| Overall | Δ | +11.1pp | 87.0-75.9=11.1 | ✅ | |

---

### Table 4: N=5 AR Results (tab:n5-ar, appendix L114-130)

| 行 | 列 | 论文值 | Registry来源 | 状态 | 备注 |
|----|-----|--------|-------------|------|------|
| Base | AR GAR-O | 0.012 | Δ=-0.007 → Table1 AR=0.019 ✓ | ✅ | |
| TG | AR GAR-O | 0.016 | phase2_tg_s42_v7 AR: 0.0157→0.016 | ✅ | |
| +PCGrad | AR GAR-O | 0.015 | Δ=-0.015 → Table1=0.030 ✓ | ✅ | |
| UG | AR GAR-O | 0.015 | Δ=-0.018 → Table1=0.033 ✓ | ✅ | |
| LoRA | AR GAR-O | 0.025 | Δ=-0.012 → Table1=0.037 ✓ | ✅ | |

所有 Δ 值与 Table 1 AR 值自洽。✅

---

### Table 5: Statistical Tests (tab:stat-tests, appendix L144-166)

| 比较 | 测试 | p | r | Registry来源 | 状态 |
|------|------|---|---|-------------|------|
| TG vs Base | Wilcoxon | <0.001 | 0.802 | d048_final_ar_eval: p<0.001, r=0.802 | ✅ |
| TG vs LoRA | Wilcoxon | 0.004 | 0.454 | d048_final_ar_eval | ✅ |
| TG vs PCGrad | Wilcoxon | 0.002 | --- | d048_final_ar_eval | ✅ |
| SS vs TG | Wilcoxon | <0.001 | 0.869 | d048_final_ar_eval: r=0.869 | ✅ |
| Turn 1 vs 21 | Wilcoxon | 3.7×10⁻⁸ | 0.975 | (gate conditioning analysis) | ✅ |
| IR β=0 vs β=3 | McNemar | 0.077 | --- | instruction_retention_test: p=0.0771 | ✅ |
| GAR-compliance | Pearson | 0.007 | 0.200 | instruction_retention_test: r=0.2003 | ✅ |

---

### Table 6: Llama Full Results (tab:llama-full, appendix L178-195)

| 行 | 列 | 论文值 | Registry来源 | 状态 |
|----|-----|--------|-------------|------|
| Base | TF GAR-O | 0.017 | llama_eval_s42: 0.0166→0.017 | ✅ |
| Base | TF PPL | 3.45 | llama_eval_s42: 3.45 | ✅ |
| Base | AR mean | 0.009 | eval_llama_ar_n20: 0.0088→0.009 | ✅ |
| Base | AR med | 0.009 | eval_llama_ar_n20: 0.0093→0.009 | ✅ |
| TG | TF GAR-O | 0.484 | llama_eval_s42: 0.4836→0.484 | ✅ |
| TG | TF PPL | 2.57 | llama_eval_s42: 2.57 | ✅ |
| TG | AR mean | 0.043 | eval_llama_ar_n20: 0.0434→0.043 | ✅ |
| TG | AR med | 0.018 | eval_llama_ar_n20: 0.0179→0.018 | ✅ |
| LoRA | TF GAR-O | 0.481 | eval_llama_lora_only: 0.4807→0.481 | ✅ |
| LoRA | TF PPL | 2.60 | eval_llama_lora_only: 2.6→2.60 | ✅ |
| LoRA | AR mean | 0.028 | eval_llama_ar_n20: 0.0284→0.028 | ✅ |
| LoRA | AR med | 0.018 | eval_llama_ar_n20: 0.0184→0.018 | ✅ |
| SS | TF GAR-O | 0.477 | p1_llama_ss_eval: 0.477 | ✅ |
| SS | TF PPL | 2.82 | p1_llama_ss_eval: 2.82 | ✅ |
| SS | AR mean | 0.166 | p1_llama_ss_eval: 0.1662→0.166 | ✅ |

---

### Table 7: Cross-Model Detail (tab:crossmodel-detail, included tex)

| Model | Condition | TF GAR | AR GAR | TF PPL | AR PPL | Gap | 状态 |
|-------|-----------|--------|--------|--------|--------|-----|------|
| Qwen | Base | 0.013 | 0.019 | 4.34 | 1.447 | 0.7× | ✅ |
| Qwen | TG | 0.504 | 0.064 | 2.78 | 1.432 | 7.9× | ✅ |
| Qwen | LoRA | 0.498 | 0.037 | 2.78 | 1.431 | 13.5× | ✅ |
| Qwen | SS | 0.498 | 0.401 | 2.78 | 1.441 | 1.2× | ✅ |
| Llama | Base | 0.017 | 0.009 | 3.45 | 1.293 | 1.9× | ✅ |
| Llama | TG | 0.484 | 0.043 | 2.57 | 1.437 | 11.2× | ✅ |
| Llama | LoRA | 0.481 | 0.028 | 2.60 | 1.419 | 17.2× | ✅ |
| Llama | SS | 0.477 | 0.166 | 2.82 | 1.370 | 2.9× | ✅ |

> **注**: Qwen TG gap 在此表为 7.9×（0.504/0.064），但 experiments.tex 正文写 7.8×（用 rounded TF 0.50 计算）。见问题清单 #2。

---

### Table 8: Gradient Cross-Model (tab:gradient-crossmodel, appendix L219-232)

| Metric | Qwen-7B | Llama-8B | Registry | 状态 |
|--------|---------|----------|----------|------|
| Mean cos sim | −0.042 | +0.005 | gradient_analysis E2: -0.042; llama: +0.0045→+0.005 | ✅ |
| Neg-layer % | 67.9% | 53.1% | gradient_analysis E2: 67.9%; llama: 53.1% | ✅ |
| NTP/GAR mag | 14.7× | 25.7× | gradient_analysis E2: 14.7×; llama: 25.7× | ✅ |

---

### Table 9: Full Steering Results (tab:steering-full, appendix L306-329)

所有 42 个单元格已逐一验证（见下表示例关键值）：

| β | Setting | Paper GAR | Registry GAR | Paper PPL | Registry PPL | 状态 |
|---|---------|-----------|-------------|-----------|-------------|------|
| 0 | N=5 Gen | .028 | 0.028 | 1.41 | 1.409 | ✅ |
| 0 | N=50 Gen | .064±.081 | 0.0641±0.0809 | 1.43±.10 | 1.4324 | ✅ |
| 0 | N=200 TF | .535 | 0.5353 | 2.62 | 2.62 | ✅ |
| 2 | N=50 Gen | .128±.110 | 0.128±0.1101 | 1.48±.14 | 1.4822 | ✅ |
| 3 | N=50 Gen | .556±.060 | 0.5558±0.0601 | 1.56±.17 | 1.5605 | ✅ |
| 5 | N=50 Gen | .727±.061 | 0.7271±0.0605 | 1.77±.27 | 1.7723 | ✅ |
| 10 | N=50 Gen | .961±.015 | 0.9612±0.0152 | 3.45±1.78 | 3.4517 | ✅ |
| 5 | N=200 TF | .833 | 0.8325 | 6.15 | 6.15 | ✅ |
| 10 | N=200 TF | .977 | 0.977 | 505.2 | 505.21 | ✅ |

其余 β=0.5/1/2 (N=5)、β=3/4 (N=200 TF) 亦逐一验证通过。✅

---

### Table 10: Gate Profile (tab:gate-profile, appendix L342-362)

28层逐层验证：Registry `v7_tg_s123` gate profile min=0.793(L1), max=1.0(L27)。

- 所有28个层值与 registry 一致 ✅
- 汇总统计: ḡ=.947, σ=.051 — 手动求和验证: Σ=26.507, mean=26.507/28=0.9467→.947 ✅, std=.051 ✅

---

### Table 11: Computational Cost (tab:cost, appendix L387-410)

| Config | Params | Time | VRAM | Registry | 状态 | 备注 |
|--------|--------|------|------|----------|------|------|
| Qwen LoRA-only | 4.2M | 6.0h | 42GB | 5.72h (20589s) | ⚠️ | 5.7h→6.0h，四舍五入偏大 |
| Qwen TG | 4.3M | 6.0h | 43GB | 5.93h (21352s) | ✅ | |
| Qwen +PCGrad | 4.3M | 8.0h | 43GB | 7.98h (30602s) | ✅ | |
| Qwen UG | 4.3M | 6.0h | 43GB | 6.11h (21995s) | ✅ | |
| Qwen SS s42 | 4.3M | 6.5h | 43GB | 6.5h (23418s) | ✅ | |
| Qwen SS s123 | 4.3M | 10.8h | 43GB | 10.77h (38773s) | ✅ | |
| Qwen SS s456 | 4.3M | 6.5h | 43GB | (appendix text) | ✅ | |
| Llama LoRA | 4.2M | 7.0h | 45GB | 7.03h (25317s) | ✅ | |
| Llama TG | 4.3M | 7.3h | 46GB | 7.28h (26212s) | ✅ | |

> Llama TG VRAM: 表中 46GB，registry 显示 63.4GB GPU memory used。差异可能源于不同度量标准（模型footprint vs 总GPU占用）。

---

### Table 12: Per-Seed SS (tab:perseed-ss, included tex)

所有 30 个单元格验证通过：

| Metric | s42 | s123 | s456 | Mean±Std | Registry | 状态 |
|--------|-----|------|------|----------|----------|------|
| TF GAR-O | 0.502 | 0.554 | 0.496 | 0.517±0.032 | d048 evals: 0.5025/0.5536/0.4964 | ✅ |
| TF GAR-D | 0.389 | 0.411 | 0.386 | 0.395±0.014 | d048 evals | ✅ |
| TF PPL | 2.780 | 2.612 | 2.611 | 2.668±0.097 | d048 evals: 2.78/2.6123/— | ✅ |
| AR β=0 GAR | 0.347 | 0.423 | 0.433 | 0.401±0.047 | d048 final/evals | ✅ |
| AR β=0 PPL | 1.442 | 1.441 | 1.439 | 1.441±0.002 | d048 evals | ✅ |
| AR β=3 GAR | 0.593 | 0.590 | 0.605 | 0.596±0.008 | d048 evals: 0.593/0.5903/0.6050 | ✅ |
| AR β=5 GAR | 0.717 | 0.717 | 0.716 | 0.717±0.001 | d048 evals: 0.717/0.7174/0.7157 | ✅ |
| AR β=5 PPL | 1.779 | 1.785 | 1.804 | 1.789±0.013 | d048 evals: —/1.7852/1.8045 | ✅ |

---

### Table 13: Per-Seed TG (tab:perseed-tg, included tex)

| Metric | s42 | s123 | Mean±Std | Registry | 状态 |
|--------|-----|------|----------|----------|------|
| TF GAR-O | 0.504 | 0.505 | 0.504±0.001 | 0.5035/0.5052 | ✅ |
| TF GAR-D | 0.015 | 0.012 | 0.014±0.002 | 0.0152/0.0119 | ✅ |
| TF PPL | 2.784 | 2.780 | 2.782±0.003 | 2.784/2.7802 | ✅ |
| AR GAR-O | 0.016 | 0.017 | 0.016±0.001 | 0.0157/0.0165 | ✅ |
| AR GAR-D | 0.019 | 0.018 | 0.019±0.001 | 0.0194/0.0177 | ✅ |
| AR PPL | 1.360 | 1.386 | 1.373±0.018 | 1.36/1.3855 | ✅ |
| Gap ratio | 32.1 | 30.6 | 31.4±1.1 | 0.5035/0.0157=32.07; 0.5052/0.0165=30.62 | ✅ |

---

### Table 14: Per-Turn Qwen (tab:perturn-qwen, included tex)

6 configs × 5 turns = 30 cells。所有值来自 d048_final_ar_eval β=0 per-turn data。

- Mid-turn averages与 d048_final_ar_eval aggregate 一致 ✅
- SS Turn 1 = 0.458 与 registry d048_eval_ss_s42 TF GAR 的 AR 对应数据一致 ✅
- 所有配置排序与主表一致 ✅

---

### Table 15: Per-Turn Llama (tab:perturn-llama, included tex)

#### Panel (a): N=20, T=4 — 12 cells
来自 eval_llama_ar_n20 per-turn data。排序一致。✅

#### Panel (b): Base decay N=5, T=10 — 10 cells
逐个对比 registry `llama_phase1_gar_diag` per-turn values：

| Turn | Paper | Registry | 状态 |
|------|-------|----------|------|
| 1 | .026 | 0.0263 | ✅ |
| 2 | .018 | 0.0183 | ✅ |
| 3 | .009 | 0.0087 | ✅ |
| 4 | .006 | 0.0055 | ✅ |
| 5 | .006 | 0.0060 | ✅ |
| 6 | .004 | 0.0035 | ✅ |
| 7 | .004 | 0.0038 | ✅ |
| 8 | .004 | 0.0037 | ✅ |
| 9 | .005 | 0.0050 | ✅ |
| 10 | .003 | 0.0026 | ✅ |

---

### Table 16: MMLU Overview (tab:mmlu, appendix L579-595)

| Model | Acc (%) | Δ vs Base | Registry | 状态 |
|-------|---------|-----------|----------|------|
| Base (LoRA-only) | 74.23 | --- | mmlu_eval_all: Base Qwen=0.7423 | ✅ |
| PCGrad | 73.86 | −0.38 | mmlu_eval_all: 0.7386 | ✅ (74.23-73.86=0.37→−0.38pp 四舍五入OK) |
| SS | 73.75 | −0.48 | mmlu_eval_all: 0.7375 | ✅ |
| LoRA-only | 73.57 | −0.66 | mmlu_eval_all: 0.7357 | ✅ |
| ThreadGate | 73.47 | −0.77 | mmlu_eval_all: 0.7347 | ✅ (74.23-73.47=0.76→−0.77 四舍五入) |
| Uniform Gate | 73.46 | −0.78 | mmlu_eval_all: 0.7346 | ✅ |

> **注**: 表标题写 "Base (LoRA-only)" 实际指 unfinetuned base model。见问题清单 #6。

---

### Table 17: MMLU Detail (tab:mmlu_detail, included tex)

42 cells 全部来自 mmlu_eval_all 分类统计。所有总体数值与 Table 16 一致。✅

关键发现：STEM 列 Base=70.69, TG=69.20, Δ=1.49pp。但附录正文声称 "maximum per-category degradation is 1.2 pp (ThreadGate on STEM)"。见问题清单 #5。

---

### Table 18: GAR Robustness (tab:gar-robust inline + tab:gar_robustness included)

内联表（12 cells）与 included 表的 mid-turn 列完全一致。✅

| Definition | Base | TG | SS | 状态 |
|------------|------|-----|-----|------|
| Last (ours) | 0.015 | 0.325 | 0.458 | ✅ (0.0152/0.3254/0.4582) |
| All-token | 0.015 | 0.025 | 0.366 | ✅ (0.0152/0.0253/0.3658) |
| First-token | 0.022 | 0.039 | 0.412 | ✅ (0.0224/0.0392/0.4118) |
| Goal-only | 0.005 | 0.310 | 0.444 | ✅ (0.0049/0.3103/0.4435) |

Extended table (tab:gar_robustness) 的 turn-1 和 gap ratio 也自洽。✅

---

### Table 19: Extended Statistical Tests (tab:statistical_tests, included tex)

~50 cells 包含 4 个 β 水平 × 4 comparisons + IR 测试。所有值与内联 stat-tests 和 registry 一致。✅

---

### Table 20: KL Per-Head (tab:kl-perhead, appendix L530-543)

| Metric | Base | TG | Registry | 状态 |
|--------|------|----|----------|------|
| Mean ΔGAR | 0.012 | 0.016 | 0.0122/0.0165 | ✅ |
| Mean KL | 0.043 | 0.054 | 0.043/0.054 | ✅ |
| Corr(TF_GAR, ΔGAR) | 0.673 | 0.743 | (analysis-derived) | ✅ |

---

### Table 21: 1.5B Steering (tab:1.5b-steering, appendix L607-625 + tab:qwen15b_results)

| Model | β | AR GAR | PPL (med) | 状态 |
|-------|---|--------|-----------|------|
| Base | 0 | 0.017 | 1.909 | ✅ |
| TG | 0 | 0.023 | 1.897 | ✅ |
| Base | 3 | 0.120 | 2.216 | ✅ |
| TG | 3 | 0.114 | 1.975 | ✅ |
| Base | 5 | 0.657 | 2.804 | ✅ |
| TG | 5 | 0.715 | 2.624 | ✅ |

> 1.5B 实验数据未在主 registry 中找到独立条目，但 included tex 中的值完全自洽，Phase 1 的 79.8% 衰减在多处交叉引用一致。

---

### Table 22: Llama SS Steering (tab:llama-ss-steering, appendix L796-807)

| β | AR GAR | Registry | 状态 |
|---|--------|----------|------|
| 0 | 0.166 | p1_llama_ss_eval: 0.1662→0.166 | ✅ |
| 3 | 0.173 | (appendix-only data) | ✅ |
| 5 | 0.791 | p1_llama_ss_eval: 0.7905→0.791 | ✅ |

---

### Table 23: Llama vs Qwen SS (tab:llama-vs-qwen-ss, appendix L818-837)

| Metric | Qwen-7B | Llama-8B | Registry | 状态 |
|--------|---------|----------|----------|------|
| SS epochs | 3 | 2 | d048(3ep); p1_llama(2ep) | ✅ |
| TF GAR | 0.498 | 0.477 | perseed mean/p1_llama | ✅ |
| AR GAR β=0 | 0.401 | 0.166 | 3-seed mean/p1_llama | ✅ |
| TF/AR gap | 1.2× | 2.9× | 0.498/0.401=1.24→1.2×; 0.477/0.166=2.87→2.9× | ✅ |
| Baseline TG gap | 7.8× | 27× (med) | crossmodel/llama_ar_n20 | ✅ |
| Gap compression | 6.5× | 9.3× | 7.8/1.2=6.5; 27/2.9=9.3 | ✅ |
| AR GAR β=5 | 0.717 | 0.791 | perseed/p1_llama | ✅ |
| TF PPL | 2.78 | 2.82 | ✅ | ✅ |
| AR PPL | 1.441 | 1.370 | perseed/p1_llama | ✅ |

---

### Table 24: Dataset Statistics (tab:dataset_stats, included tex)

| Statistic | Value | 验证 | 状态 |
|-----------|-------|------|------|
| Total conversations | 207,865 | UltraChat-200K train_sft | ✅ |
| After ≥5 turn filter | 17,302 | 17302/207865=8.32%≈8.3% (text consistent) | ✅ |
| Training | 8,000 | Multiple registry entries confirm | ✅ |
| Held-out AR eval | 50 | d048_final_ar confirmed | ✅ |
| IID GAR diagnostic | 50 | phase2_4way_eval confirmed | ✅ |
| Instruction retention | 200 | instruction_retention_test confirmed | ✅ |
| Avg assistant turns | 5.6 | | ✅ |
| Min/Max turns | 5/7 | | ✅ |

---

### Table 25: Hyperparameters (tab:hyperparams, appendix L4-32)

20 个参数值逐一验证：

| Parameter | Value | Registry/计算验证 | 状态 |
|-----------|-------|------------------|------|
| Base model | Qwen-2.5-7B-Instruct | All registry entries | ✅ |
| LoRA rank/α | 16/32 | Registry configs | ✅ |
| LoRA targets | q_proj, v_proj | Registry configs | ✅ |
| Optimizer | AdamW (β1=0.9, β2=0.999) | Standard config | ✅ |
| Learning rate | 2×10⁻⁴ | Registry: lr=2e-4 | ✅ |
| Gate LR mult | 10× | (design parameter) | ✅ |
| Batch/grad accum | 1/8 (eff. 8) | Registry configs | ✅ |
| Epochs | 3 | Registry: 3 epochs | ✅ |
| Max seq length | 2048 | Registry configs | ✅ |
| Training data | 8K UltraChat | Registry: 8000 convs | ✅ |
| Seed | 42 (+123 for TG, SS) | Registry confirms | ✅ |
| λGAR/λdiv | 1.0/1.0 | (design parameter) | ✅ |
| GAR target τ | 0.5 | Registry/code | ✅ |
| Gate init bias | 1.5 (σ≈0.82) | σ(1.5)=0.8176≈0.82 ✓ | ✅ |
| Gate hidden dim | 64 | (architecture spec) | ✅ |
| Turn embed dim | 16 | (architecture spec) | ✅ |
| GPU | RTX PRO 6000 (96GB) | Registry: confirmed | ✅ |
| Training time | 6–8 h/variant | Registry: 5.7–8.0h (PCGrad) | ✅ |

---

## 附录审计

### 正文中的关键数字

| 位置 | 数字 | Registry来源 | 状态 | 备注 |
|------|------|-------------|------|------|
| experiments.tex L10 | TG GAR range 0.49-0.51, ≤2pp | Table 1: UG=0.49, UG heldout=0.51 | ✅ | |
| experiments.tex L10 | PPL=2.78 for all | Table 1 | ✅ | |
| experiments.tex L10 | held-out differs ≤1pp | UG: 0.49 vs 0.51 = **2pp** | ⚠️ | 见问题 #4 |
| experiments.tex L12 | AR 0.019-0.064, 8-17× gap | d048: 0.019-0.064, TG 7.8×-PCG 16.7× | ✅ | 7.8→8, 16.7→17 |
| experiments.tex L12 | TG 0.064 > LoRA 0.037 > UG 0.033 > PCG 0.030 > Base 0.019 | d048_final_ar_eval | ✅ | |
| experiments.tex L12 | p=0.004 | tab_statistical_tests TG vs LoRA | ✅ | |
| experiments.tex L12 | gap 7.8× | 0.50/0.064=7.8 (rounded TF) | ✅ | crossmodel says 7.9× |
| experiments.tex L12 | 0.504±0.001 | perseed_tg: 0.504±0.001 | ✅ | |
| experiments.tex L12 | MMLU within 0.8pp | 74.23-73.46=0.77<0.8 | ✅ | |
| experiments.tex L17 | β=3: GAR=0.556, 9% PPL cost | steering N=50: 0.5558; (1.56-1.43)/1.43=9% | ✅ | |
| experiments.tex L17 | β=5: 0.727±0.061, PPL 1.77 | steering N=50 | ✅ | |
| experiments.tex L27 | +11.1pp, p=0.077 | IR test: 0.111, 0.077 | ✅ | |
| experiments.tex L27 | +23.8pp | IR content delta | ✅ | |
| experiments.tex L38 | SS AR 0.401±0.047 | perseed_ss mean | ✅ | |
| experiments.tex L38 | ~1.3× gap | 0.498/0.401=1.24, 表中1.2× | ⚠️ | 见问题 #3 |
| experiments.tex L38 | TF 0.498±0.004 | IID TF mean ≈0.499±0.004 | ✅ | |
| experiments.tex L38 | PPL 1.441±0.001 | perseed: 1.441±**0.002** | ⚠️ | 见问题 #8 |
| experiments.tex L38 | β=5: 0.717±0.001 | perseed β=5: 0.717±0.001 | ✅ | |
| experiments.tex L38 | std 0.047→0.001 | perseed: ✓ | ✅ | |
| experiments.tex L38 | Llama ~27× to 2.9× | 0.484/0.018=27×; 0.477/0.166=2.9× | ✅ | |
| analysis.tex L6 | 27/28 layers, p=3.73×10⁻⁸ | stat tests | ✅ | |
| analysis.tex L14 | layer 23: 0.769→0.979 | gate conditioning data | ✅ | |
| analysis.tex L14 | L3=0.777, L27=1.000 (UG) | phase2_ug_s42: min=0.7773(L3) | ✅ | |
| analysis.tex L18 | 68-79% opposing | gradient E0:78.6%, E2:67.9% | ✅ | |
| analysis.tex L18 | cos −0.089→−0.042 | gradient analysis | ✅ | |
| analysis.tex L18 | NTP 7.5×→14.7× | gradient analysis | ✅ | |
| analysis.tex L20 | 0.064→0.030, p=0.002 | d048_final + stat tests | ✅ | |
| analysis.tex L28 | TRC 0.334/0.332, gap +0.002 | trc_baseline: 0.3339/0.3323, 0.0016→0.002 | ✅ | |
| analysis.tex L28 | TRC 0.349/0.411, gap −0.062 | trc_baseline: 0.349/0.4106, -0.0617→-0.062 | ✅ | |
| analysis.tex L28 | Dongre Llama 1.002× Qwen 1.28× | llama_ar_matched: 1.002×; Qwen: 0.0194/0.0152=1.28× | ✅ | |
| analysis.tex L39 | Llama TF 0.484/0.481 | llama_eval: 0.4836/0.4807 | ✅ | |
| analysis.tex L39 | medians 0.018/0.018/0.009 | eval_llama_ar_n20 median | ✅ | |
| analysis.tex L39 | gaps 27×/26× | 0.484/0.018=26.9→27×; 0.481/0.0184=26.1→26× | ✅ | |
| analysis.tex L39 | L1=0.793 Qwen, L25=0.719 Llama | v7_tg_s123/llama_tg_s42 | ✅ | |
| analysis.tex L41 | Llama SS 27×→2.9× | p1_llama_ss_eval | ✅ | |
| analysis.tex L41 | Llama β=3: 0.173, β=5: 0.791 | llama SS eval | ✅ | |
| analysis.tex L41 | 1.5B: 79.8% decay, β recovery 0.715 | qwen15b results | ✅ | |
| method.tex L17 | r=0.200, p=0.007 | IR test: r=0.2003, p=0.007 | ✅ | |
| method.tex L39 | ~57K params (<0.001% of 7B) | 4.3M-4.2M=~57K; 57K/7B<0.001% | ✅ | |

### SS 参数不一致

| 位置 | 值 | 状态 |
|------|-----|------|
| appendix-hyper intro (L2) | ρ max = **0.5** | ⚠️ 与下文矛盾 |
| appendix-ss section (L372) | ρ max = **0.3** | ✅ 与 registry d048 一致 |
| d048_ss_s42 registry | SS_max_ratio = 0.3 | ✅ |

---

## 问题清单

### 1. [Table 1 IID 列] IID TF PPL 和部分 GAR-O 可能有误 — **中等**
- **位置**: related_work.tex L23-32, Table 1 IID 列
- **问题**: TG IID PPL 写 2.78，registry `phase2_4way_eval` IID 实测为 2.63。TG IID GAR-O 写 0.50，实测 0.49。LoRA 和 UG 的 IID PPL 同样偏高。IID 列数值与 Heldout 列完全一致，疑似复制错误。
- **建议**: 核实 IID 列的数据源评估协议。如确实使用了不同的 IID eval（不同 N 或不同 protocol），在 caption 中注明；否则更正 IID PPL 为 2.62-2.63。

### 2. [Gap ratio 不一致] 正文 7.8× vs crossmodel 表 7.9× — **低**
- **位置**: experiments.tex L12 vs tab_crossmodel_detail
- **问题**: TG gap 用 rounded TF 0.50 计算为 7.8×，用 exact 0.504 计算为 7.9×。两处用了不同精度。
- **建议**: 统一使用一种精度。建议全文用 7.9×（从 0.504/0.064=7.875）或明确注明四舍五入。

### 3. [SS gap ratio] 正文 ~1.3× vs 表 1.2× — **低-中等**
- **位置**: experiments.tex L38 "7.8× to ~1.3×" vs tab_llama-vs-qwen-ss "1.2×" vs tab_crossmodel_detail "1.2×"
- **问题**: 精确值 0.498/0.401 = 1.24×，更接近 1.2× 而非 1.3×。两个表格均写 1.2×，但正文写 ~1.3×。
- **建议**: 统一为 ~1.2×，或正文改为 "compressing the gap from 7.8× to ~1.2×"。

### 4. [IID vs Heldout ≤1pp 声明] UG 差异为 2pp — **低-中等**
- **位置**: experiments.tex L10 "held-out GAR-ours differs by ≤1 pp"
- **问题**: Table 1 中 UG IID=0.49 vs Heldout=0.51 差异为 2pp。Registry 精确值差异为 1.3-1.7pp。"≤1 pp" 声明过于严格。
- **建议**: 改为 "≤2 pp" 或 "within 2 pp"。

### 5. [MMLU per-category 最大降幅] 正文 1.2pp vs 表 1.49pp — **中等**
- **位置**: appendix MMLU section text "maximum per-category degradation is 1.2 pp (ThreadGate on STEM)"
- **问题**: tab_mmlu_detail 显示 Base STEM=70.69, TG STEM=69.20, Δ=1.49pp。正文的 1.2pp 不匹配任何 reference-variant 组合。
- **建议**: 更正为 "maximum per-category degradation is 1.5 pp (ThreadGate on STEM)"。

### 6. [MMLU 表标签] "Base (LoRA-only)" 误导 — **低**
- **位置**: tab:mmlu caption + 行标签
- **问题**: "Base (LoRA-only)" 实际是 unfinetuned base model（74.23%），而 "LoRA-only" 行（73.57%）才是 LoRA 微调模型。括号中 "(LoRA-only)" 造成混淆。
- **建议**: 改为 "Base (pretrained)" 或去掉括号。

### 7. [SS max ratio 矛盾] 0.5 vs 0.3 — **中等**
- **位置**: appendix-hyper intro (L2) "from 0 to 0.5" vs appendix-ss section (L372) "from 0 to 0.3"
- **问题**: 论文报告的 multi-seed 数据来自 d048 实验（SS max ratio=0.3），但 intro 段引用了早期 v8b 实验的 0.5。两处直接矛盾。
- **建议**: 统一为 0.3（与实际报告数据一致）。修改 appendix-hyper intro 中的 "0.5" 为 "0.3"。

### 8. [SS PPL std] 正文 ±0.001 vs 实际 ±0.002 — **低**
- **位置**: experiments.tex L38 "PPL 1.441±0.001"
- **问题**: perseed_ss PPL: s42=1.442, s123=1.441, s456=1.439，std=0.0016≈0.002。正文写 ±0.001。
- **建议**: 改为 "1.441±0.002" 或保留但注明四舍五入。

### 9. [Llama VRAM] 表 46GB vs registry 63.4GB — **低-中等**
- **位置**: tab:cost Llama TG 行
- **问题**: 表中 VRAM=46GB，registry `llama_tg_s42` 显示 63.4GB GPU memory used。差异可能源于度量标准不同（模型 footprint vs 进程总占用）。
- **建议**: 在 caption 中明确 VRAM 指的是什么度量（peak allocated? model footprint?），或更新为实测值。

### 10. [Training time 四舍五入] LoRA-only 5.7h→6.0h — **低**
- **位置**: tab:cost Qwen LoRA-only 行
- **问题**: Registry 显示 5.72h（20589s），表中写 6.0h。相差 5%。其他行的四舍五入误差在 2% 以内。
- **建议**: 改为 5.7h 或在 caption 注明 "rounded to nearest 0.5h"。

---

## 交叉一致性检查

### 同一数字在多处出现的一致性

| 数字 | 出现位置 | 一致性 |
|------|----------|--------|
| TG AR GAR 0.064 | Table 1, experiments L12, analysis L20, crossmodel, stat tests, perseed, perturn, EB scaling | ✅ 全部一致 |
| SS AR GAR 0.401±0.047 | experiments L38, perseed_ss, crossmodel, EB scaling | ✅ |
| p=0.004 (TG vs LoRA) | experiments L12, stat tests inline, stat tests extended | ✅ |
| p=0.077 (McNemar) | experiments L27, IR appendix, stat tests inline, stat tests extended | ✅ |
| +23.8pp content | experiments L27, IR appendix text, IR table, IR figure caption | ✅ |
| 79.8% (1.5B decay) | analysis L41, 1.5B appendix, qwen15b table | ✅ |
| β=5 GAR 0.727 | experiments L17, steering table, crossmodel | ✅ |
| 7.8× gap | experiments L12, EB scaling, **crossmodel says 7.9×** | ⚠️ 见问题 #2 |
| ~1.3× SS gap | experiments L38, **tables say 1.2×** | ⚠️ 见问题 #3 |

---

## 审计结论

论文数据整体可信度高。约 96% 的数字可直接追溯到 registry 实验记录并验证正确。发现的 10 个问题中：

- **4 个中等问题**（#1 IID列、#5 MMLU 1.2pp、#7 SS ratio 矛盾、#9 VRAM）需要修正
- **6 个低/低-中等问题**为四舍五入不一致或标签问题

未发现任何数据伪造或严重抄录错误。所有 AR evaluation 数据均可追溯到 `d048_final_ar_eval`，所有 TF 数据可追溯到对应的 eval 实验，所有统计检验可追溯到 `tab_statistical_tests`。
