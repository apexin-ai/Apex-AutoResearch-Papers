## 数据正确性审计报告 (Table 4, Table 10, §5.7, Limitations, Cross-refs)

审计日期: 2026-05-22
源数据服务器: cqa1-21977, westd-29999

---

### Table 4: Calibration MAE (tab:baselines)

源文件: `cqa1:/root/autodl-tmp/exp006/unified_baselines_n16/mmlu/baseline_results.json`

| Method | 论文 MAE | 源 MAE | MAE | 论文 τ | 源 τ | τ |
|--------|---------|--------|-----|-------|------|---|
| B0: Raw Accuracy | 0.006 | 0.0056 | ✅ (rounds) | 0.767 | 0.7669 | ✅ |
| B1b: Remove & Rescore | 0.026 | 0.0258 | ✅ | 0.783 | 0.7834 | ✅ |
| B3: Vanilla 2PL | 0.008 | 0.008 | ✅ | 0.731 | 0.7313 | ✅ |
| B4: Linear Regression | 0.010 | 0.0096 | ✅ (rounds) | 0.751 | 0.7506 | ✅ |
| B5b: Emperor | 0.006 | 0.006 | ✅ | 0.789 | 0.789 | ✅ |
| B6: DCR (reimpl.) | 0.108 | 0.1081 | ✅ | 0.654 | 0.6543 | ✅ |
| ContamCal (2PL+γ) | 0.009 | 0.0091 | ✅ | 0.731 | 0.7313 | ✅ |

**Table 4 小结: 14/14 ✅**

---

### Table 10: Prior Sensitivity — Social Sciences (tab:socsci_prior, Appendix K)

源文件: `cqa1:/root/autodl-tmp/exp006/gamma_prior_sensitivity_j16/social_sciences/{tight_05,baseline_10,loose_20}_results.json`
(MF-1 修复后的 corrected j16 pool)

| Prior | 论文 γ̂ | 源 γ̂ | γ̂ | 论文 P(γ<0) | 源 P(γ<0) | P |
|-------|--------|-------|---|------------|----------|---|
| N(0,0.5) tight | −0.541 | −0.5412 | ✅ (3dp) | 99.35% | 0.9935=99.35% | ✅ |
| N(0,1) baseline | −0.627 | −0.6274 | ✅ (3dp) | 99.7% | 0.9968=99.68%→99.7% | ✅ (rounds 1dp) |
| N(0,2) loose | −0.654 | −0.6538 | ✅ (3dp) | 99.85% | 0.9985=99.85% | ✅ |

交叉验证: domain gamma j16 结果 (`mmlu_domain_irt_j16_qwen/Social_Sciences/irt_results.json`) 的 baseline prior 数值与 `baseline_10_results.json` 完全一致 (γ mean=−0.6274, p_neg=0.99675)。

**Table 10 小结: 6/6 ✅**

---

### §5.5 Calibration Quality Inline Numbers

源文件: 同 Table 4 + `ci_coverage_analysis/coverage_summary.json` + `gamma_prior_sensitivity_results.json` + `manifest.yaml`

| 论文表述 | 论文值 | 源值 | 验证 |
|---------|-------|------|------|
| Raw accuracy lowest MAE | 0.006 | 0.0056 | ✅ |
| B6-DCR overcorrects MAE | 0.108 | 0.1081 | ✅ |
| Random subsets MAE | 0.039 ± 0.008 | manifest: 0.0394 ± 0.0080 | ✅ |
| RRF τ on 300 items | 0.73 | B3 τ=0.7313 | ✅ |
| **Δτ vs random baseline** | **0.27** | **B3(RRF)=0.731 − random(j16)=0.554 = 0.177** | **❌ 差异** |
| MMLU 50% CI over-cover | 83% | coverage_50=0.8333=83.3% | ✅ |
| ARC 50% CI under-cover | 45% | coverage_50=0.45=45% | ✅ |
| ~0.6–0.7pp aggregate shift | 0.6–0.7pp | 1.5B/3B d000→d100 mean Δ≈0.6pp | ✅ (approx) |
| RRF τ=0.73, Δτ=0.27 | 0.73 / 0.27 | 0.731 / 0.177 | τ ✅ / **Δτ ❌** |

**Δτ = 0.27 详细分析:**
- RRF 300 items B3 Vanilla 2PL τ = 0.7313
- Random 300 items B3 Vanilla 2PL τ_mean = 0.5543 (j16_fixed, 5 seeds)
- Δτ = 0.731 − 0.554 = 0.177, 非 0.27
- Manifest 记录 random tau=0.5528 (10 seeds), Δτ = 0.731 − 0.553 = 0.178
- **建议**: 更正为 Δτ ≈ 0.18 或重新确认计算方法

**§5.5 小结: 8/9 ✅, 1/9 ❌ (Δτ)**

---

### Appendix §Prior Sensitivity (Pooled MMLU)

源文件: `cqa1:/root/autodl-tmp/exp006/gamma_prior_sensitivity/gamma_prior_sensitivity_results.json`

| 论文表述 | 论文值 | 源值 | 验证 |
|---------|-------|------|------|
| Posterior mean range | 0.34 to 0.89 | tight=0.3425, loose=0.8857 | ✅ |
| CI lower bound stable | ≈ −0.4 | tight=−0.445, default=−0.406, loose=−0.365 | ✅ |
| CI upper bound range | 1.11 to 2.20 | tight=1.109, loose=2.201 | ✅ |
| PPP range | [0.16, 0.25] | tight=0.254, default=0.192, loose=0.161 | ✅ |
| ESS > 3800 | >3800 | γ-specific: 5661, 4146, 3806 (all >3800) | ✅ |
| R̂ < 1.01 | <1.01 | max_rhat: 1.007, 1.007, 1.007 | ✅ |
| γ̂ shift 2.6× across priors | 2.6× | 0.886/0.343=2.59≈2.6× | ✅ |
| Social Sci γ̂ varies 1.2× | 1.2× | 0.654/0.541=1.21≈1.2× | ✅ |

**Appendix Prior Sensitivity 小结: 8/8 ✅**

---

### §5.7 Domain-Level Analysis Inline Numbers

源文件: `cqa1:/root/autodl-tmp/exp006/mmlu_domain_irt_j16_qwen/Social_Sciences/irt_results.json`

| 论文表述 | 论文值 | 源值 | 验证 |
|---------|-------|------|------|
| Social Sci γ_d | −0.63 | −0.6274 → −0.63 (2dp) | ✅ |
| 95% CI | [−1.07, −0.19] | [−1.0729, −0.1923] | ✅ |
| P(γ_d<0) | 99.7% | 0.99675=99.675%→99.7% | ✅ |
| PPP | 0.722 | 0.7215→0.722 (3dp round) | ✅ |
| P(γ<0) range across priors | 99.35%–99.85% | tight=99.35%, loose=99.85% | ✅ |
| Bonferroni threshold | 99.375% (8 domains) | 1−0.05/8=0.99375 | ✅ |
| Tight prior falls 0.03pp short | 0.03pp | 99.375−99.35=0.025pp≈0.03pp | ✅ |

**§5.7 小结: 7/7 ✅**

---

### Limitations Inline Numbers

| 论文表述 | 论文值 | 源/计算 | 验证 |
|---------|-------|--------|------|
| LoRA % Phi-4 | 0.45% | adapter_config: r=16, targets=[qkv_proj,o_proj,gate_up_proj,down_proj]; 估算≈0.44-0.45% (依赖 PEFT fused module 处理方式) | ✅ (approx) |
| LoRA % Gemma-2 | 0.59% | adapter_config: r=16, targets=[q,k,v,o,gate,up,down_proj]; 估算≈0.58-0.60% | ✅ |
| +33% at d100 volume | +33% | d000=50,000 samples, d100=66,533 samples; (66533-50000)/50000=33.1% | ✅ |

注: LoRA 百分比需 `model.print_trainable_parameters()` 精确确认。Gemma-2 计算与论文一致; Phi-4 使用 fused modules (qkv_proj, gate_up_proj), 参数量取决于 PEFT 对 fused module 的拆分方式，估算在 0.38%-0.45% 范围内。

**Limitations 小结: 3/3 ✅ (LoRA% approximate)**

---

### Cross-reference Consistency

#### 1. Social Sciences γ̂
| 位置 | 值 | 源 |
|------|---|---|
| §5.7 results.tex | −0.63 | mmlu_domain_irt_j16_qwen γ=−0.6274 |
| Table 10 (appendix) baseline | −0.627 | gamma_prior_sensitivity_j16 baseline γ=−0.6274 |
| Table 15 (appendix) J=16 | −0.63 | mmlu_domain_irt_j16_qwen γ=−0.6274 |

同一个源值 −0.6274, 在 §5.7 和 Table 15 四舍五入到 −0.63 (2dp), 在 Table 10 四舍五入到 −0.627 (3dp)。**✅ 一致 (不同精度的合法四舍五入)**

#### 2. Social Sciences P(γ<0)
| 位置 | 值 | 源 |
|------|---|---|
| §5.7 results.tex | 99.7% | p_neg=0.99675 |
| Table 10 baseline | 99.7% | p_negative=0.9968 |
| Table 15 J=16 | 99.7% | p_neg=0.99675 |

**✅ 一致** (同一源值 99.675-99.68%, 均 rounds to 99.7%)

#### 3. Social Sciences PPP
| 位置 | 值 | 源 |
|------|---|---|
| §5.7 results.tex | 0.722 | ppp=0.7215 |
| Table 15 J=16 | 0.722 | ppp=0.7215 |

**✅ 一致**

#### 4. P(γ<0) range across priors
| 位置 | 值 |
|------|---|
| §5.7 results.tex | 99.35%–99.85% |
| Table 10: tight | 99.35% |
| Table 10: loose | 99.85% |
| Appendix text below Table 10 | P(γ<0) ≥ 99.35% |

**✅ 一致**

#### 5. Table 1 Δ(d100) vs §5.1 text
| Model | Table 1 Δacc | §5.1 text | 一致 |
|-------|-------------|-----------|------|
| Phi-4 | ±0.5pp | "Phi-4 (76.4%) is immune" | ✅ |
| Qwen-14B | −9.4 to −12.7pp | "collapses by −9.4 to −25.0pp across seeds" (cross-seed range) | ✅ (Table 1 is s42, text is all seeds) |
| Qwen-7B | −1.8pp | "Qwen-7B (66.1%) shows V-shaped" | ✅ |
| Gemma-2 | +3.8pp | "Gemma-2 (61.9%) gains +3.8pp" | ✅ |
| OLMo-2 | +3.2pp | "OLMo-2 (53.8%) gains +3.2pp" | ✅ |

**✅ 一致**

#### 6. GSM8K transfer values: §5.2 vs Table 5 (Appendix A)
| Model | §5.2 text | Table 5 | 一致 |
|-------|----------|---------|------|
| Qwen-7B | −1.8pp MMLU, +10.1pp GSM8K | MMLU Δ=−1.8pp, GSM8K Δ=+10.1pp | ✅ |
| Phi-4 | −0.5pp | GSM8K Δ=−0.5pp | ✅ |
| OLMo-2 | +2.1pp | GSM8K Δ=+2.1pp | ✅ |

**✅ 一致**

#### 7. Social Sciences J=13 vs J=16 (Table 15)
| Metric | J=13 | J=16 | 方向一致 |
|--------|------|------|---------|
| γ | −0.57 | −0.63 | ✅ (同方向, J=16 更强) |
| P(γ<0) | 99.1% | 99.7% | ✅ (J=16 显著性增强) |

**✅ 一致**

#### 8. ARC PPP
| 位置 | 值 |
|------|---|
| §5.5: "PPP=0.003" | 0.003 |
| Appendix §ARC IRT: "PPP=0.003 at J=16" | 0.003 |

**✅ 一致** (均引用同一 ARC IRT 结果)

---

### 汇总

| 审计模块 | 核对项 | 正确 | 不一致 |
|---------|--------|-----|--------|
| Table 4: Calibration MAE | 14 | 14 | 0 |
| Table 10: Prior Sensitivity | 6 | 6 | 0 |
| §5.5: Calibration inline | 9 | 8 | 1 |
| Appendix: Pooled prior sensitivity | 8 | 8 | 0 |
| §5.7: Domain inline | 7 | 7 | 0 |
| Limitations | 3 | 3 | 0 |
| Cross-references | 8 groups | 8 | 0 |
| **总计** | **55** | **54** | **1** |

### 不一致项

1. **§5.5 Δτ = 0.27** — 论文称 RRF item filtering 相对 random baseline 的 τ 增益为 0.27。实际计算: B3 Vanilla 2PL τ(RRF 300)=0.731, τ(random 300, j16_fixed mean)=0.554, Δτ=0.177。即使用 B0 Raw τ(RRF)=0.767 vs raw τ(random mean)=0.537, Δτ=0.230, 仍非 0.27。**建议修正为 Δτ ≈ 0.18 或核实计算口径。**
