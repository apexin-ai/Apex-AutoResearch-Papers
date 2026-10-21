# Rebuttal Response Template — ARR May 2026 (v21)
# Paper: How Does Schema Complexity Predict Performance in Training-Free LLM IE?
# Prepared: 2026-05-21 | Upgraded from talking points v18

---

## TP1: Novelty
**预期审稿人问题**：The SCS metric is essentially cosine similarity of type name embeddings, which is well-known. LLM-PEE already uses similar partitioning. What is the novelty here?
**核心回复**：SCS's formal definition matches LLM-PEE's partitioning criterion, acknowledged in §2. No prior work uses it as an *independent variable* in controlled experiments: we isolate confusability from count via BCS-stratified batches, revealing three previously undocumented findings — task asymmetry (§4.3–4.4), merge amplification (§5), and few-shot gap widening (Appendix L).
**证据引用**：§2 ¶4 (LLM-PEE acknowledgement); §4.3 (BCS-controlled design); §5 + Appendix B Table 8 (SDGD, precision 0.563→0.210); Appendix L Table 22 (few-shot, gap +4.3pp)
**补充数据**：LLM-PEE reports decomposition improves NER; our SDGD on the *same task* shows F1 drops 0.445→0.251. MAVEN ED replicates: precision 0.287→0.091.

---

## TP2: Effect size
**预期审稿人问题**：The pairwise r²=1.3% is negligible. The typical batch gap of 2.2pp is not practically meaningful. Why should practitioners care?
**核心回复**：Pairwise r²=1.3% is the mechanism-level signal; the primary evidence is batch-level R²=22% (FewRel, n=100 random batches) to 58% (DocRED, n=110 pooled). The 2.2pp is the IQR-typical gap; production schemas with clustered types produce extreme-BCS batches where the gap reaches 25–31pp.
**证据引用**：Table 2 (pairwise, §4.2); §4.3 ¶Practical magnitude (R²=0.218, IQR=0.054); Appendix F Table 11 (extreme gaps); §4.3 ¶DocRED (R²=0.578); Appendix N (Monte Carlo, simulated R²=0.219 matching observed 0.218)
**补充数据**：FewRel extreme: 82.3% vs 51.0% (Δ=−31.2pp). DocRED count-16 extreme: Δ=−25.0pp (CI [21.9, 28.3]). Quartile comparison (100 random batches): 82.8% vs 78.9% (Δ=3.9pp). Conditional pairwise r²=7% (among non-zero confusion pairs) is the relevant amplification input.

---

## TP3: Generalizability — NER null
**预期审稿人问题**：The BCS signal is null for NER, arguably the more important task. Doesn't this severely limit the contribution?
**核心回复**：The task asymmetry is a *core finding* (C2), not a limitation. Pairwise SCS *is* significant in NER (r=0.112, p<0.001; Table 2), but batch-level aggregation fails because NER errors scatter across miss (49–56%), boundary (5–7%), and type substitution (3–10%) — none correlating with BCS. Relaxed matching confirms this is not a metric artifact (r=0.003, n=450; Appendix Y).
**证据引用**：Table 2 (pairwise, §4.2); Table 3 + Figure 2 (error taxonomy, §4.4); Appendix Y Table 28 (relaxed matching, 4 match modes all r≈0); Appendix Y text (per-error-mode: miss ρ=0.017, boundary ρ=−0.043, type_sub ρ=−0.010; per-count: count-2/6/12 all r<0.11, p>0.3)
**补充数据**：IntraSub *does* scale with BCS on extreme batches (ρ=1.0, Table 3) — the signal exists but is overwhelmed by miss-mode variance (43–65%) in random batches. Relaxed matching improves F1 by +4.2pp (98.4% batches improve) without recovering BCS signal — boundary errors are uniform, not BCS-dependent.

---

## TP4: Failed experiments
**预期审稿人问题**：Many experiments failed. Does this indicate poor methodology?
**核心回复**：This is an analysis paper — negative results *are* findings. SDGD failure reveals merge amplification (§5); renaming failure reveals label-familiarity confounds (Appendix X); few-shot widening reveals confusability is structural (Appendix L). Registry infrastructure failures (vLLM versioning, env setup) are tagged as engineering, not scientific.
**证据引用**：§5 + Appendix B Table 8 (SDGD: P 0.563→0.210); Appendix X Table 27 (renaming: −3.0/−8.8pp); Appendix L Table 22 (few-shot: gap +18.5→+22.8pp, p=0.014)
**补充数据**：MAVEN ED replicates merge amplification (P 0.287→0.091, 3.7× inflation). All scientific experiments produced interpretable results informing the paper.

---

## TP5: Correlational — no concrete examples
**预期审稿人问题**：The paper is all statistics with no qualitative grounding. Can you show actual confusion examples?
**核心回复**：Appendix V provides top-10 confused type pairs for both RE (Table 25) and NER (Table 26) with SCS values and confusion counts, plus three concrete extraction instances (Table 27) where all gold-predicted pairs have SCS>0.90 — illustrating argument reversal, containment inversion, and meronymy-membership conflation.
**证据引用**：Appendix V Table 25 (RE top-10); Table 26 (NER top-10); Table 27 (3 concrete instances with sentences)
**补充数据**：RE top: *instance of*/*taxon rank* (N=875 confusions); *followed by*/*follows* (SCS=0.90, N=400). NER top: *person-other*/*person-politician* (SCS=0.93, N=121). Low-SCS outliers reflect domain co-occurrence rather than semantic similarity.

---

## TP6: Renaming — "Just rename confusable labels"
**预期审稿人问题**：If high-SCS pairs cause confusion, simply rename them. Did you try?
**核心回复**：We reduced mean pairwise SCS from 0.87 to 0.67 (Δ=−0.20) via 14 label renamings. Accuracy *decreased* in both BCS groups, with a larger drop on high-BCS batches (−8.8pp vs −3.0pp; interaction −5.9pp, p<0.001). Label unfamiliarity outweighs confusability reduction — SCS captures deeper conceptual overlap that surface renaming cannot eliminate.
**证据引用**：Appendix X Table 27 (renaming: low 90.1→87.1%, high 69.3→60.5%); Limitations L4 (causal mechanism)
**补充数据**：Interaction: Δ_high − Δ_low = −5.9pp (t=−7.23, p<0.001, Cohen's d: −2.92 vs −1.09). Solo sanity check: 11/12 renamed labels individually recognizable (acc ≥ original −5pp). Renamed types per batch negatively correlated with accuracy change (r=−0.625, p<0.001).

---

## TP7: Separability ⚠️ HIGH RISK
**预期审稿人问题**：TOST passes on FewRel linear scale but fails on logit (p=0.209) and DocRED shows −9.4pp interaction. The "approximately separable" claim seems overstated.
**核心回复**：We present three converging analyses: (1) FewRel full-range regression (n=69, 5 count levels): interaction 0.47pp, TOST p=0.003 at ±3pp; (2) DocRED range-matched: controlling for BCS range restriction reduces interaction from 7.52pp to 0.93pp (CI [−7.13, 7.44]); (3) BCS–accuracy correlations are comparable across DocRED counts (ρ=−0.762 vs −0.693). We explicitly qualify: "approximately separable" throughout, with logit-scale and DocRED caveats in §4.4, §6, and Limitations L2.
**证据引用**：
- FewRel primary: §4.4 full-range regression; Appendix C Table 9 (TOST across 4 margins: ±1pp inconclusive, ±2pp marginal p=0.047, ±3pp established p=0.003, ±5pp p<0.001)
- FewRel logit: Appendix C ¶Logit-scale (p=0.209; back-transform: 2.78pp at floor, 2.53pp at median — both within ±3pp)
- DocRED raw: §4.4 (−9.4pp, CI [−12.9, −6.0])
- DocRED range-matched: Appendix C ¶Range-matched (0.93pp, CI [−7.13, 7.44]; BCS spread confound: 0.377 vs 0.263)
- Qualifications: Abstract ("approximately separable"); §6 ¶Boundary conditions ("logit-scale and DocRED evidence remain inconclusive, warranting larger-sample investigation"); Limitations L2
**补充数据**：
- FewRel interaction 90% CI: [−1.0, 2.0]pp — well below ±3pp
- DocRED power: reduced sample (n=29+55) has 80% power only for effects ≥10.5pp — wide CI is a power limitation, not evidence of large interaction
- Key framing: We claim *bounded* interaction, not zero. TOST bounds interaction below practical significance on FewRel linear; logit/DocRED are explicitly inconclusive. The two-dimensional framework is useful for practitioners regardless of whether interaction is exactly zero vs bounded-small.

---

## TP8: Format independence
**预期审稿人问题**：The BCS effect might be an artifact of enum-based constrained decoding forcing errors into type substitution.
**核心回复**：A paired comparison on 25 identical batch type sets shows virtually identical BCS–accuracy correlations under constrained (r=−0.45) and unconstrained (r=−0.44) decoding (Fisher z=−0.04, p=0.97). Only 2/25 batches differ, each by exactly 1 sample. The confusability effect is format-independent.
**证据引用**：Appendix K Table 13 (paired statistics); Table 14 (per-batch: 23/25 identical); §6 ¶Embedding similarity
**补充数据**：Mean accuracy: 79.5% vs 79.6% (Δ=−0.08pp). OOV rate: 0.08% (2/2400). Spearman ρ also matched: −0.157 vs −0.144. Models comply with schema semantics even without structural enforcement.

---

## TP9: Cross-model generalization
**预期审稿人问题**：Primary experiments are on Qwen3-32B only. Cross-model validation is limited.
**核心回复**：Both dimensions replicate across four models spanning three architecture families. Dimension 1: all four show monotonic RE decline (Table 1, Appendix J Table 18, Appendix K Table 19). Dimension 2: all four show significant BCS gaps for RE (Table 4 + Table 20). Secondary analyses are on the primary model for depth — stated in Limitations L1.
**证据引用**：Table 1 (LLaMA-8B count, Appendix A); Table 4 (LLaMA-8B BCS, Appendix A); Appendix J Table 18 (LLaMA-70B: RE −30.7pp, NER U-shape replicates); Appendix K Tables 19–20 (Gemini: ρ=−1.0 counts 4-32, BCS Δ=−17.6pp); Limitations L1
**补充数据**：BCS gaps: Qwen3 −31.2pp, LLaMA-8B −27.1pp (87%), LLaMA-70B −10.9pp (CI [3.0, 20.1]), Gemini −17.6pp (CI [15.1, 20.1]). High-BCS convergence to ~51% across Qwen3/LLaMA-8B suggests task-inherent difficulty floor. Scale attenuation is mild: 8B achieves 87% of 32B gap.

---

## TP10: Statistical honesty — Gemini outlier
**预期审稿人问题**：The Gemini count-16 correlation seems driven by a single outlier.
**核心回复**：We disclose this transparently in Appendix K: leave-one-out drops r from −0.80 to −0.42 (p=0.22). The outlier (BCS=0.97, acc=59.9%) drives leverage. The primary Gemini Dimension 2 evidence is count 8 (n=50, Δ=−17.6pp, CI [15.1, 20.1]) — robust and unaffected by single-point removal.
**证据引用**：Appendix K ¶Dimension 2 (LOO analysis); Table 20 (cross-model summary)
**补充数据**：LOO: Pearson −0.80→−0.42, Spearman −0.40→−0.18. Count-8 result robust: 25 low-BCS vs 25 high-BCS, wide CI excluding zero.

---

## TP11: Amplification mechanism
**预期审稿人问题**：How does 1.3% pair-level become 22–58% batch-level? Is this an aggregation artifact?
**核心回复**：Monte Carlo simulation (Appendix N) confirms ~3× geometric amplification from correlated pair aggregation (inter-pair SCS ρ=0.35), yielding simulated batch R²=0.219 — matching the observed 0.218. The relevant input is conditional pairwise r²=7% (non-zero confusion pairs), not the unconditional 1.3% diluted by 89% zero-confusion pairs.
**证据引用**：Appendix N (simulation: conditional R²=0.219, unconditional R²=0.044); §4.2 Table 2 (pairwise); §4.3 ¶Practical magnitude; Appendix M (BCS independence: VIF=1.06, BCS unique R²=0.259)
**补充数据**：Effective degrees of freedom: ~3.4 (not 28). Sensitivity: at ρ=0.20 (halved), batch R²≈0.22 still matches. DocRED R²=0.58 reflects document-level cross-sentence amplification. Non-independence is by design: BCS measures batch-level confusability precisely because co-present types interact during type resolution (Appendix N ¶Non-independence).

---

## TP12: No GPT-4 family
**预期审稿人问题**：You don't test any OpenAI model. This is a significant gap.
**核心回复**：Gemini 2.5 Flash covers the proprietary architecture angle with a state-of-the-art model. Convergent evidence across three families (Qwen, LLaMA, Gemini; 8B–70B, open-weight + proprietary) makes the pattern unlikely architecture-specific. GPT-4 omitted due to API cost constraints (72 GPU-hours invested). We welcome community replication.
**证据引用**：Table 20 (cross-model BCS summary, Appendix K); Appendix J (LLaMA-70B); Appendix K (Gemini); Limitations L1
**补充数据**：Three families, consistent direction. Gap magnitudes vary with capacity (ceiling compression at higher baselines). Adding GPT-4 increases family count but is unlikely to change directional finding.

---

## TP13: No solution — only diagnosis ⚠️ HIGH RISK
**预期审稿人问题**：SDGD fails, renaming fails, few-shot makes it worse. The paper offers no actionable method. This limits significance for EMNLP.
**核心回复**：Systematic diagnosis is a prerequisite for effective solutions. Prior work proposed solutions (LLM-PEE decomposition, CodeKGC schema engineering) without isolating failure modes — our analysis shows *why* those fail: merge amplification collapses precision 2.7–3.7× (§5, Appendix B Tables 8, 12), and all 5 routing strategies fall below single-pass (Table 12). The paper provides three actionable outputs: (1) pre-hoc BCS complexity audit before deployment; (2) SCS>0.85 pair flagging for targeted evaluation (§6); (3) evidence that future solutions must address embedding-space geometry, not surface manipulation.
**证据引用**：
- Why prior solutions fail: §5 body (merge amplification + routing failure); Appendix B Table 8 (NER: 4 modes, all below single-pass); Table 12 (RE: 5 routing strategies, best=36.5% vs single-pass 50.4%)
- Why naive fixes fail: Appendix X Table 27 (renaming: −3.0/−8.8pp); Appendix L Table 22 (few-shot: gap widens +4.3pp)
- Actionable outputs: §6 ¶Practical implications (SCS>0.85 threshold, BCS monitoring); §6 ¶Mechanistic hypothesis (embedding-space softmax competition)
- Oracle proves decomposition potential: Appendix B Table 10 (oracle 80.2% vs single-pass 50.4%; confusability-aware +1.4pp over random, p=0.19 n.s. — grouping is not the bottleneck, routing is)
- Format-independence rules out decoding as intervention: Appendix K Table 13
**补充数据**：
- Task-specific guidance already in §6: NER → reduce candidate types (Dim 1 is dominant lever); RE → flag SCS>0.85 pairs + monitor batch BCS as quality indicator (BCS-stratified gaps 25–31pp)
- MAVEN ED replicates merge amplification (P 0.287→0.091), confirming the barrier generalizes beyond NER
- Definitions do not help: name+definition SCS yields Δr of −0.023 to +0.035 vs name-only (Appendix P Table 15), consistent with LLMs underutilizing relation definitions (Zhou et al., 2024)
- Precedent: analysis papers accepted at *ACL on diagnostic value — "Are We Modeling the Task or the Annotator?" (Geva et al.); "Annotation Artifacts in NLI" (Gururangan et al.); "Right for the Wrong Reasons" (McCoy et al.)
