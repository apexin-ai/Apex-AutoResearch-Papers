# Paper Update Checklist — contamcal-irt-calibration

> Generated 2026-05-19. Paper: 7 pages main text. Deadline: EMNLP 2026 ARR May 25 (D+6).
> Current state: docs/paper/*.tex. Sections: abstract, introduction, related_work, method, experimental_setup, results, conclusion (merged with discussion), limitations, ethics, appendix.

---

## Section: Abstract (abstract.tex)

- [ ] **P0** 更新 seed 信息：当前写 "seed=42"，V-recovery 已双种子确认（D165），改为 "confirmed across two seeds" 并更新 Δacc 表述（s42 partial −1.82pp, s123 full 0.00pp → "mid-dosage trough with seed-dependent recovery extent"）
- [ ] **P1** 加入 GSM8K negative control 结果（待 eval 完成）：一句话 "GSM8K (open-ended) shows near-zero contamination effect, confirming format-dependent vulnerability"
- [ ] **P1** 加入 DiD finding 一句："Item-level DiD shows no memorization; effects arise from global capability modulation"
- [ ] **P0** triple-seed 完成后：如升级为 taxonomy 需改 "observed profiles" → "taxonomy"；如降级为 3-pattern 需相应修改（gated on s0 results）

## Section: Introduction (introduction.tex)

- [ ] **P0** Contribution 1 更新：当前写 "Five-pattern contamination taxonomy"，但 framing 要求仅 triple-seed 后才能称 taxonomy。在 s0 完成前改为 "Five observed dose-response profiles"，或在 triple-seed 确认后保持 taxonomy
- [ ] **P0** V-recovery 描述更新：当前贡献列表中未提及双种子确认。加 "confirmed across two seeds (partial and full recovery)" 到 Contribution 1
- [ ] **P1** Contribution 2 (DiD global modulation) 已在当前版本中，检查是否需要更新措辞以反映 "all 5 families" 的 DiD 结果
- [ ] **P1** GSM8K 结果整合后，在 contributions 或 intro 末尾加一句 benchmark-conditionality framing

## Section: Related Work (related_work.tex)

- [ ] **P1** 检查是否已引用 Han et al. 2026 (quantifying contamination via psychometric DIF)——当前已有，OK
- [ ] **P1** 考虑加 1 句 multi-family contamination profiling 的空白（当前 related work 没有显式说 "no prior work profiles across families"——这在 intro 中说了，related work 可加一句呼应）

## Section: Method (method.tex)

- [ ] **P0** Algorithm 1 volatility fix (v2)：当前 method.tex 的 Algorithm 1 已包含 v* mid-trajectory check（line 3, 71-78），确认与 v2 180/180 版本一致。需验证 paper 中的伪代码是否完全匹配 profile_classifier.py v2
- [ ] **P1** 如 triple-seed 结果出来且 profile 合并（如 V-type + U-type → "harm"），Algorithm 1 的输出集合需更新

## Section: Experimental Setup (experimental_setup.tex)

- [ ] **P0** 更新 seed 信息：当前写 "Models at ≤3B are trained with two seeds"。7B/14B 如果 s123 完成，需更新为 "7B with two seeds, 14B/Phi-4/OLMo-2/Gemma-2 with one seed"（或等 s0 后写 "7B with three seeds"）
- [ ] **P0** 更新 checkpoint 总数：当前 "over 50 checkpoints"，s123 完成后实际数量需核实更新
- [ ] **P1** GSM8K eval 协议：当前 benchmarks 段已提 GSM8K，但 eval 细节（8-shot CoT, generation-based）未在 setup 中写明。如 GSM8K 结果入主文，需补 eval 协议细节
- [ ] **P1** evaluate.py 版本声明：C009 约束要求 eval 一致性。考虑在 setup 加一句 "All evaluations use a unified evaluation script verified via hash consistency across servers"

## Section: Results (results.tex)

### 5.1 Five Dose-Response Patterns
- [ ] **P0** Table 1 加 s123 列：当前 Table 1 只有 seed=42 数据。V-recovery 双种子已确认（D165），至少更新 Qwen-7B 行加 s123 Δacc=0.00pp。其他 4 family s123 结果 pending
- [ ] **P0** V-recovery 段落更新：当前 ¶30 已写 "V-shaped harm-then-recovery under both seeds (trough at d025 for seed=42, d005 for seed=123; recovery extent varies from partial to full)"——确认此句与 D165 结果一致，OK。但 Table 1 需同步更新数据
- [ ] **P0** Triple-seed 完成后：Table 1 加 error bars（3-seed mean ± std），或改为 "2-seed confirmed" 表述
- [ ] **P1** Domain decomposition 已有一句引用 Appendix（¶30 末尾 "Cross-family domain decomposition reveals consistent directionality..."），确认 Appendix 内容与 D166 domain decomposition 数据一致

### 5.2 Item-Level Memorization Test (DiD)
- [ ] **P0** 确认 Table 2 (DiD) 数据是否为 aligned evaluate.py 版本结果。D161 记录 DiD 完成，但需确认是 s42 aligned 还是旧 eval 版本
- [ ] **P1** 如有 s123 DiD 数据，可在文字中加 "replicated under seed=123" 一句

### 5.3 Calibration Quality
- [ ] **P1** 当前 calibration 仅在 Qwen ≤3B (J=16) 上做。如 s123/s0 完成后做 cross-family IRT fitting（2PL+γ on 7B-14.7B），需更新 Table 3 或加新表
- [ ] **P1** IRT 2PL+γ fitting 待 s123 eval 完成后执行，结果可能更新 calibration 数据

### 5.4 Signal Failure
- [ ] **P1** 当前 signal failure 数据来自 ≤3B Qwen。如有 7B-14.7B signal 数据可加一句跨规模确认

### 5.5 Domain-Level Analysis
- [ ] **P1** 当前 domain analysis 仅在 Qwen ≤3B。Cross-family domain decomposition（D166, STEM resilient / Social Sci sensitive）已有 Appendix 内容。确认 Appendix 文字与数据一致

### GSM8K（新增子节或加入现有框架）
- [ ] **P0** GSM8K eval 完成后：加入 Results 作为 negative control。选项：(a) 新子节 "5.X GSM8K: Format-Dependent Vulnerability"，(b) 整合入 5.1 作为 paragraph。建议 (b) 省空间——在 baseline threshold 段加一段 "GSM8K (open-ended) shows near-zero contamination effect across all families, confirming that dose-response profiles are benchmark-conditioned"
- [ ] **P1** 如 GSM8K 有 family-specific 差异（如某 family 在 GSM8K 上也有变化），需要额外讨论

## Section: Discussion and Conclusion (conclusion.tex)

- [ ] **P0** ¶1 "Five patterns, not one"：更新 V-recovery 描述。当前已有 "consistent across benchmarks" 但未提双种子确认。加 "V-recovery is confirmed across two seeds with varying recovery extent"
- [ ] **P0** 如 GSM8K 结果显著，加一段 benchmark-conditionality 讨论（当前 discussion 未显式讨论 GSM8K negative control 的含义）
- [ ] **P1** DiD 段：当前 ¶1 已提 "Item-level DiD analysis shows these patterns arise from global capability modulation"。如有新数据（s123 DiD）可加强
- [ ] **P1** Domain decomposition 讨论：当前 ¶3 提 domain analysis。如 STEM-resilient / Social-Sci-sensitive 数据已在 Appendix，加一句具体数据引用

## Section: Limitations (limitations.tex)

- [ ] **P0** "Single seed" 段落更新：当前写 "confirmed across two seeds (s42, s123)"。如 s0 完成前提交，保持此表述。如 s0 完成，改为 "triple-seed validated"
- [ ] **P0** 如 GSM8K eval 完成但仅 d000+d100 两个端点，在 limitations 加 "GSM8K evaluated at endpoint dosages only (d000, d100); intermediate dosage profiles not characterized"
- [ ] **P1** Prompt format sensitivity 段（当前最后一段）：已提 "pattern shapes may vary with prompt format"——确认与 D154b 一致，OK
- [ ] **P1** 考虑加 "Benefit models (OLMo-2, Gemma-2) may exhibit different behavior under pretraining contamination vs SFT injection" 以呼应 DiD global-modulation finding

## Section: Ethics (ethics.tex)

- [ ] **P1** 当前已完整覆盖。无需更新，除非 GSM8K 引入新 benchmark 需提及（已在 list 中）

## Section: Appendix (appendix.tex)

### Existing appendix sections（确认数据一致性）
- [ ] **P0** Appendix A (ARC Cross-Benchmark): 确认与 s42 aligned eval 数据一致
- [ ] **P0** Appendix K (Sensitivity): 确认 30/30 → 180/180 更新。当前写 "30 (τ,σ) combinations"，但 D164/Algorithm v2 报告 180/180 (6 families × 30 combos)。需更新描述或确认 30/30 是 per-family

### 新增 appendix 内容
- [ ] **P0** Domain decomposition 完整数据表：Appendix L (sec:domain_decomposition) 已有定性描述 + 数据。确认 STEM 2.8pp / Social Sci 5.1pp 数据已在文中
- [ ] **P1** GSM8K 详细结果表（eval 完成后）：per-family GSM8K accuracy at d000/d100
- [ ] **P1** V-recovery 双种子对比图：s42 vs s123 trajectory overlay（已有数据可直接生成）
- [ ] **P1** Fisher Information 推导：framing 提到 "must derive I(γ) for appendix"。如来得及，加入推导

## Section: Figures

- [ ] **P0** Fig 1 (dose-response): 确认当前 fig_dose_response.pdf 使用 s42 aligned eval 数据（非旧 eval 版本）
- [ ] **P0** Fig 2 (treated/untreated DiD): 确认使用 aligned eval 数据
- [ ] **P1** 如加 GSM8K 结果：可在 Fig 1 加 subplot 或在 appendix 加单独图
- [ ] **P1** 如加 s123 数据：考虑在 appendix 加 s123 dose-response overlay 图
- [ ] **P1** Baseline vs effect scatter (fig_baseline_vs_effect.pdf): 确认已是 aligned eval 数据

## Section: References

- [ ] **P1** 确认所有已引用论文的 bib 条目完整（特别是 han2026quantifying, schaeffer2026causally 等 2026 引用）
- [ ] **P1** 检查是否遗漏 framing 中要求的引用（DIF literature, conformal prediction 等——部分为 appendix/future work 引用）

---

## Priority Summary

**P0 (must have for submission, ~15 items)**:
1. V-recovery 双种子确认整合到 abstract + results Table 1 + discussion
2. Algorithm 1 v2 一致性验证（method 伪代码 vs profile_classifier.py）
3. GSM8K 结果整合（待 eval 完成）
4. Experimental setup seed/checkpoint 数更新
5. Figure 数据一致性验证（aligned eval）
6. Sensitivity 描述更新（30→180）
7. Limitations seed 段更新
8. DiD 数据版本确认

**P1 (nice to have, ~20 items)**:
1. s123 cross-family 数据更新（Table 1 扩展）
2. GSM8K 在各 section 的引用
3. Domain decomposition appendix 完善
4. Related work 呼应句
5. Fisher Information 推导
6. V-recovery 双种子对比图
7. Reference audit
