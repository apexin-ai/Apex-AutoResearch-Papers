# Paper Framing — persuasion_turn_jailbreak_detect

## Target Venue
- Primary: EMNLP 2026 Main (ARR submission)
- Deadline: 2026-05-25 (ARR May cycle)
- Track: LLM Security / Discourse and Pragmatics
- Commitment deadline: 2026-08-02

## Title (Working)
What Makes Multi-Turn Jailbreaks Detectable? A Systematic Decomposition of Cross-Attack Generalization

## Core Insight (D030 → D049 — classification-based DAPT reframe)
Domain adaptation universally improves cross-attack generalization across encoder architectures; encoder pretraining determines the difficulty threshold at which adaptation becomes critical. Systematic ablation across two encoders (DeBERTa-v3, RoBERTa) and three OOD attack families (DD, FITD, ActorAttack) reveals:

**On Deceptive Delight (moderate OOD)**: DeBERTa vanilla collapses (F1=0.31±0.03), continued pretraining bridges ~60pp (MLM=0.91±0.12), classification achieves 0.997±0.005. RoBERTa vanilla already succeeds (0.981±0.026) — hierarchy is flat. Scrambled=binary=9-class (all 0.997±0.005).

**On ActorAttack (hard OOD)**: RoBERTa vanilla ALSO collapses (0.466±0.163), proving "no DA needed" was DD-specific. DeBERTa vanilla=0.258±0.000. Both encoders benefit from DA: DeBERTa 9-class=0.972±0.026, RoBERTa 9-class=0.939±0.046. Binary (0.990±0.008) ≈ 9-class (0.972±0.026) ≈ scrambled (0.951±0.043) — all three classification variants equivalent at Full (max gap 3.9pp, variance intervals fully overlap, n=3). Label quality is not a significant factor on ActorAttack, consistent with DD findings (D032).

**On Human-Written Jailbreaks (exp8, ToxicChat, macro F1 — D036)**: Domain-adapted variants outperform vanilla on human-authored data from ToxicChat (LMSYS, 204 jailbreaks + 204 benign, balanced, no data leakage). Macro F1: JB-MLM=0.837±0.013, wiki-MLM=0.791±0.093, binary=0.705±0.072, scrambled=0.616±0.056, 9-class=0.596±0.087, topic=0.496±0.042, vanilla=0.413±0.021. All DA variants exceed vanilla (+18-42pp), confirming features learned from Qwen3-8B synthetic data transfer to human text. JB-MLM strongest on human data (reversed from synthetic where 9-class leads), suggesting pure domain exposure transfers better across the human/LLM style gap. Notably, wiki-MLM (0.791, out-of-domain text) outperforms ALL classification variants (binary=0.705, scrambled=0.616, 9-class=0.596), further demonstrating that MLM domain exposure mechanism dominates classification supervision on human data. The jb_mlm vs wiki_mlm gap (4.6pp, std overlap) is modest, suggesting domain specificity provides marginal benefit on human data. 9-class drops from best on synthetic OOD (0.997/0.972) to 5th on human data (0.596), indicating classification supervision overfits to synthetic data distribution. Paper must discuss this contrast explicitly. NOTE: verazuo/jailbreak_llms results INVALID (benign data leakage, M014) — removed from paper.

**Cross-encoder CKA (D029)**: Both MLM and 9-class reshape representations substantially (centered CKA < 0.5 vs vanilla), but representation change magnitude ≠ detection improvement. RoBERTa MLM changes more (CKA=0.393) yet gains only 0.6pp; DeBERTa MLM changes less (CKA=0.442) yet gains 60pp. The starting point determines the return on adaptation.

**Cross-LLM Generalization (D049/D051, exp16/exp16b/exp17)**: On mixed Qwen+Llama training data (exp16, 250+250, 3 seeds), the evidence hierarchy REVERSES to 9-class >> MLM ≈ vanilla. DD OOD: 9-class=0.818±0.096, MLM=0.289±0.101, vanilla=0.291±0.065. ToxicChat human data (D051 correction, balanced 408-sample eval): 9-class=0.550±0.052, vanilla=0.356±0.009 — NO improvement over Qwen-only (exp8 9-class=0.596±0.087, stds overlap). Mixed training eliminates single-LLM confound but does NOT improve human-data generalization. On Llama-only training (exp16b, seed 42): MLM ≤ vanilla on all OOD (Llama DD: MLM=0.191, vanilla=0.181; Llama AA: MLM=0.290, vanilla=0.411 — vanilla better by 12pp). Scaling to 1000 Qwen conversations (exp17, 3 seeds): 9-class maintains dominance on OOD (DD=0.889±0.041, AA=0.913±0.041) while MLM remains weak (DD=0.338±0.010, AA=0.351±0.018, ≈ vanilla). **Critical revision**: MLM effectiveness is specific to single-source (Qwen) training data; classification-based DAPT (9-class) is the ONLY robust adaptation across all training data compositions.

**Key nuances**: (1) Binary ≈ 9-class ≈ scrambled on ActorAttack Full (0.990 vs 0.972 vs 0.951, all within noise at n=3; D032). Label quality is not a detection-relevant factor on any OOD difficulty. (2) Classification supervision consistently reduces cross-seed variance 4-20x (Claim 3): 9-class std=0.005-0.026 vs MLM std=0.080-0.115, across both DD and ActorAttack. (3) Perturbation robustness is attack-family-dependent (Discussion finding): DD OOD Δ≈0, ActorAttack DA variants Δ=-0.17 to -0.35 (vanilla -0.009 floor effect). DA detection advantage survives perturbation (McNemar p<0.001) as Claim 1 corollary. (4) **D049**: MLM's ~60pp improvement on DD OOD is Qwen-specific; on mixed-LLM and Llama-only data, MLM ≈ vanilla. 9-class is the only universally robust DAPT variant.

## Novelty Positioning (D030 reframe)
NOT: "Persuasion-aware fine-tuning is the critical ingredient" (MLM control falsified this on DD).
NOT: "RoBERTa doesn't need domain adaptation" (ActorAttack falsified this — D030).
NOT: "Label quality matters on hard attacks" (3-seed ActorAttack: binary 0.990 ≈ 9-class 0.972 ≈ scrambled 0.951, all within noise; D032).
NOT: "Perturbation robustness generalizes across attack families" (exp6 falsified: DD Δ≈0 but ActorAttack Δ=-0.17 to -0.35 for all variants).
NOT: "MLM domain exposure is the universal mechanism" (D049: MLM effectiveness is Qwen-specific; on mixed-LLM and Llama-only data, MLM ≈ vanilla).
YES: "We systematically decompose cross-attack generalization across two encoder architectures, three OOD attack families, and two training data compositions. The key finding: classification-based domain adaptation (9-class) is the only universally robust adaptation variant — it improves generalization regardless of encoder architecture, attack complexity, or training data source. MLM continued pretraining is effective on single-source data but collapses on mixed-LLM training, revealing its effectiveness is condition-dependent. Classification supervision provides additional benefits: cross-seed stability (std reduced 4-20x vs MLM on synthetic OOD) and interpretability via strategy trajectories. Mixed-LLM training eliminates the single-LLM confound without degrading performance (exp16 ToxicChat=0.550±0.052 ≈ exp8 0.596±0.087 on balanced eval). DA's detection advantage survives adversarial perturbation (McNemar p<0.001), though absolute perturbation robustness is attack-family-dependent. Label quality (correct vs scrambled vs binary) does not significantly affect detection at any OOD difficulty level (D032)."

## Inherent Lexical Separability (D009)
Persuasive jailbreak conversations and general benign conversations are inherently lexically separable (TF-IDF≈1.0 on ALL data sources including real WildChat). TF-IDF remains strong on DD OOD (Full=0.961, per-prefix K1-K5 near-perfect). **But TF-IDF collapses on ActorAttack (Full=0.261, exp7)** — lexical features cannot capture multi-persona role-playing attack structure. DisPeD's value: (1) bridging 71pp gap vs TF-IDF on hard OOD (ActorAttack: 9-class=0.972 vs TF-IDF=0.261), (2) cross-seed stability (std 4-20x smaller than MLM variants), (3) interpretability via strategy trajectories.

## Comprehensive Ablation Picture (D014, updated D019/D020, revised D049)
Systematic ablation reveals the method's actual mechanism:
- **Critical (conditioned, D049)**: On single-source Qwen data, domain exposure in any form (MLM, scrambled, persuasion) bridges OOD gap from F1=0.28 to F1≈1.0. **However**, on mixed-LLM (Qwen+Llama) and different-source (Llama-only) data, only classification-based DAPT (9-class) reliably bridges the gap; MLM effectiveness is condition-dependent (Qwen-specific, provides no benefit on mixed data: DD OOD=0.289±0.101 ≈ vanilla=0.291).
- **Harmful**: Misaligned classification objective (topic: F1=0.54±0.21, -37pp vs MLM) — constrains representations toward irrelevant features
- **Non-critical on single-source**: Label granularity (binary≈scrambled≈9-class, 1-6pp gap on DD), Lambda tuning (all F1=1.0), Temporal modeling (mean pooling≈GRU on DD)
- **Now critical on multi-source (D049)**: Classification supervision itself — 9-class is the ONLY variant that maintains performance across training data compositions. MLM collapses on mixed data (DD OOD: 0.289±0.101 vs 9-class 0.818±0.096).
- **Implication (revised D049)**: On single-source data, domain exposure is sufficient. On multi-source/mixed data, classification supervision becomes essential. 9-class taxonomy provides: (1) robust cross-composition generalization, (2) cross-seed stability, (3) interpretability. The original "domain exposure is the mechanism" claim holds only within single-source training conditions.

## Core Claims (3, priority-ordered — D019 reframe, D034 Claim 3 restructure)

### Claim 1 (PRIMARY): Classification-Based DAPT Provides Robust Cross-Attack Generalization (D049 reframe)
Vanilla DeBERTa catastrophically fails on unseen attack types (F1=0.28 on DD). Classification-based domain-adaptive pretraining (9-class) bridges this gap robustly across ALL tested conditions — single-source (Qwen DD=0.997), mixed-LLM (DD=0.818), expanded scale (DD=0.889, AA=0.913). On single-source Qwen data, MLM also achieves near-perfect DD OOD (0.914±0.115), but this effectiveness is condition-dependent: on mixed Qwen+Llama data, MLM provides no benefit (DD=0.289±0.101, ≈ vanilla 0.291); on Llama-only data, MLM ≤ vanilla (DD: 0.191 vs 0.181; AA: 0.290 vs 0.411). 9-class is the ONLY adaptation variant that reliably improves generalization regardless of training data composition. Complete evidence hierarchy (Qwen-only DD Full F1, multi-seed): vanilla (0.28) < topic (0.54±0.21) < wiki-MLM (0.90±0.12) ≈ JB-MLM (0.91±0.12) < TF-IDF (0.96) < scrambled (0.99) ≈ binary (0.99) ≪ 9-class (1.00±0.005). On ActorAttack: TF-IDF collapses (0.261) while 9-class=0.972 (+71pp). ToxicChat human data (D051, balanced 408-sample eval): exp16 mixed 9-class=0.550±0.052 ≈ exp8 Qwen-only 9-class=0.596±0.087 — mixed training does NOT improve human-data generalization but eliminates single-LLM confound.
- Evidence: plan_017 MLM DD — 3-seed Full=0.914±0.115, K≤5 ≥0.97 (no classification labels)
- Evidence: plan_018 wiki-MLM DD — 3-seed Full=0.904±0.115, ≈ JB-MLM (domain specificity not significant at Full)
- Evidence: plan_016v2 topic DD — 3-seed 0.541±0.207 (misaligned classification hurts vs MLM)
- Evidence: plan_006 DD — Treatment F1=1.0, Baseline=0.28 (+72pp)
- Evidence: plan_006 scrambled DD — F1=0.935-0.990 (labels non-essential)
- Evidence: plan_013 binary DD — F1=0.99 (label granularity non-essential)
- Evidence: exp6 perturbation — DA detection advantage survives adversarial perturbation (9-class perturbed ActorAttack=0.768 >> vanilla=0.248, McNemar p<0.001). Domain adaptation's generalization benefit is not erased by paraphrasing attacks.
- Evidence: exp7 TF-IDF ActorAttack — TF-IDF Full=0.261 vs 9-class=0.972 (+71pp). TF-IDF collapses on structurally complex attacks (Precision=1.0 but Recall=0.15), proving lexical features are insufficient. DD OOD TF-IDF per-prefix: K1=1.0, K2=1.0, K3=0.994, K5=1.0, Full=0.961 — DD is fully solvable by lexical methods, but ActorAttack is not.
- Evidence: exp8 Human data (ToxicChat, macro F1) — 204 jailbreaks + 204 benign (LMSYS): JB-MLM=0.837±0.013, 9-class=0.596±0.087, vanilla=0.413±0.021. All DA >> vanilla (+18-42pp) on human-written jailbreaks completely independent of Qwen3-8B. (verazuo INVALID, M014)
- Evidence: exp16 Mixed-LLM (Qwen+Llama 250+250, 3 seeds) — 9-class DD OOD=0.818±0.096 >> MLM=0.289±0.101 ≈ vanilla=0.291±0.065. ToxicChat (balanced 408, D051): 9-class=0.550±0.052, vanilla=0.356±0.009 — NO improvement over Qwen-only (0.596). Classification-based DAPT is the ONLY robust variant on mixed training data for synthetic OOD.
- Evidence: exp16b Llama-only (seed 42) — MLM ≤ vanilla on all OOD sets (Llama DD: 0.191 vs 0.181; Llama AA: 0.290 vs 0.411 — vanilla BETTER by 12pp; Qwen DD: 0.333 vs 0.457). MLM provides NO benefit on different-source data.
- Evidence: exp17 Scale validation (Qwen 1000, 3 seeds, OOD only — IID leaked M019) — 9-class DD=0.889±0.041, AA=0.913±0.041 >> MLM DD=0.338±0.010, AA=0.351±0.018 ≈ vanilla DD=0.326, AA=0.508±0.085. 9-class dominance holds at 2x scale.
- Strength: very strong — multi-condition validation (single-source, mixed-LLM, different-source, 2x scale) proves classification-based DAPT is uniquely robust; MLM effectiveness condition-dependent; TF-IDF collapse on ActorAttack proves discourse-level advantage; human data cross-validates

### Claim 2 (ANALYSIS): Persuasion Taxonomy as Interpretability Layer
While the persuasion classification task does not contribute to detection performance, the 9-class taxonomy provides interpretability that MLM cannot: different attack types exhibit distinct strategy trajectories (Crescendo: gradual escalation 0.86→5.64, DD: emotional-manipulation→role-assignment, FITD: commitment patterns). This is the taxonomy's sole surviving value after the MLM control result.
- Evidence: plan_008 strategy transition matrices
- Evidence: plan_017 falsifies detection contribution, confirming interpretability-only role
- Strength: descriptive/analytical; interpretability value independent of detection mechanism

### Claim 3 (EMPIRICAL): Classification Supervision Provides Cross-Seed Stability (on synthetic OOD)
Classification supervision reduces cross-seed variance by 4-20x compared to MLM-only pretraining on synthetic OOD data. 9-class std=0.005 (DD) / 0.026 (ActorAttack) vs JB-MLM std=0.115 (DD) / 0.080 (ActorAttack). Binary and scrambled variants also achieve low variance (0.005-0.043).
- Evidence: 9-class DD 0.997±0.005 vs JB-MLM 0.914±0.115 (std 23x smaller)
- Evidence: 9-class ActorAttack 0.972±0.026 vs JB-MLM 0.893±0.080 (std 3x smaller)
- Evidence: wiki-MLM 0.904±0.115 — out-of-domain MLM equally unstable
- **CAVEAT (exp8, Reviewer-flagged)**: On human data (ToxicChat), variance pattern REVERSES: 9-class std=0.087 (HIGHEST), jb_mlm std=0.009 (lowest). Classification supervision destabilizes on far-OOD human data while MLM remains stable. Claim 3 must be explicitly scoped to "synthetic OOD data" in the paper, with human data reversal discussed in Discussion.
- Implication: Classification supervision stabilizes within the synthetic data distribution but may overfit to it. MLM provides more robust cross-distribution stability.
- Strength: strong on synthetic OOD (2 families, 7 variants, 3 seeds); DOES NOT hold on human data

### Perturbation Robustness (DISCUSSION FINDING — demoted from Claim, D033/D034)
Adversarial perturbation robustness does NOT generalize across attack families. On DD OOD, classification variants show near-zero degradation (Δ≈0 at K≥2). On ActorAttack, DA variants degrade substantially: 9-class Δ_full=-0.204±0.135, binary -0.250, scrambled -0.172, MLM -0.353. Vanilla Δ_full=-0.009 (floor effect: clean=0.258, near random). Better-performing variants have more room to degrade — perturbation narrows the DA-vanilla gap but does not eliminate it.
- DD robustness attribution (D026, holds on DD only): classification structure → Full/K≥3 Δ=0; correct+fine-grained → K=2 Δ=0; both contribute at K=1.
- ActorAttack: three-layer attribution does NOT hold. Ranking: scrambled (-0.172) < 9-class (-0.204) < binary (-0.250) < MLM (-0.353).
- DA detection advantage persists under perturbation (9-class perturbed=0.768 >> vanilla=0.248, McNemar p<0.001) — this is a corollary of Claim 1, not an independent robustness claim.
- 9-class ActorAttack perturbation has extreme seed variance: seed123=-0.013, seed42=-0.296, seed456=-0.303 (std=0.135).
- **Limitation**: Absolute perturbation robustness (Δ≈0) only verified on DD OOD. On ActorAttack, all DA variants degrade (vanilla near-zero due to floor). Mechanism hypothesis (distributed multi-turn signals more vulnerable to paraphrasing) is post-hoc and unverified — future work.
- Caveat (Reviewer #53): DD perturbation n=76, small sample.
- Data correction: vanilla/binary checkpoints were wrong in initial exp6 run (wrong GRU paths). Corrected values above verified against registry checkpoints.

## Story Spine (D019 reframe)

**Problem**: Multi-turn jailbreak attacks distribute adversarial intent across individually benign turns. Bullwinkel et al. (2025) show per-turn representations are deliberately kept in a "benign" region. DeepContext tracks generic semantic drift (F1=0.84) but collapses to F1=0.28 on unseen attack families.

**Gap**: What representation properties enable cross-attack generalization? Vanilla encoders fail catastrophically on unseen attacks. LLM-as-judge approaches (GPT-5.5 F1=0.19-0.45) cannot detect process-level manipulation. No published work systematically decomposes what makes the OOD gap bridgeable.

**Our angle**: We systematically investigate what enables cross-attack jailbreak detection through a comprehensive ablation study across encoder architectures, DAPT variants, and training data compositions. Starting with the hypothesis that persuasion-specific classification drives generalization, we progressively strip components: label quality (scrambled → same), label granularity (binary → same), temporal modeling (mean pooling → same), loss weighting (all lambda → same). On single-source data, MLM continued pretraining also achieves near-perfect detection (DD F1≈0.91). But extending to mixed-LLM training (Qwen+Llama) and cross-source evaluation reveals MLM's effectiveness is condition-dependent — classification-based DAPT (9-class) is the only variant that robustly generalizes across training data compositions.

**Headline result (D049/D051)**: "Vanilla semantic modeling collapses on unseen multi-turn attack types (F1=0.28 on Deceptive Delight). On single-source synthetic data, even MLM continued pretraining bridges ~60pp of this gap. However, this MLM effectiveness does not generalize: on mixed-LLM training data, MLM collapses while classification-based DAPT (9-class) maintains robust generalization. 9-class is the only adaptation variant that consistently improves detection across single-source, mixed-LLM, and cross-source conditions. Mixed-LLM training eliminates the single-LLM source confound without degrading performance, but does not improve human-data generalization (ToxicChat F1: mixed 0.550 ≈ single-source 0.596, D051). Classification supervision provides additional benefits: cross-seed stability (std reduced 4-20x vs MLM on synthetic OOD) and interpretability via persuasion strategy trajectories."

## Architecture

1. **Stage 1**: DeBERTa-v3-base fine-tuned on multi-task objective: 9-class persuasion strategy classification (8 strategies + none) + binary jailbreak-intent classification. Loss: L = L_strategy + 0.3 × L_intent
2. **Stage 2**: BiGRU over DeBERTa [CLS] embeddings → binary classifier for conversation-level jailbreak detection
3. **Baseline**: Same pipeline but with vanilla (not fine-tuned) DeBERTa embeddings
Note: All main results use BiGRU. Ablation (plan_015) shows mean pooling ≈ GRU on both IID and OOD, confirming temporal modeling is unnecessary. This is an ablation finding, not a design choice — GRU remains default for consistency with all reported experiments. Stage-1 training: 4 epochs, best checkpoint selected by validation.

## Venue Fit Risks
- EMNLP 2026 LLM Security track: strong fit (dedicated track, high visibility)
- Discourse/Pragmatics reviewers may want more linguistic rigor: ground taxonomy in PAP (ACL 2024), Hagendorff (Nature Comm 2026), Cialdini principles, Speech Act Theory (Austin 1962, Searle 1969)
- Safety reviewers expect multiple attack types: need >= 2 attack families

## Anticipated Reviewer Concerns

### RC1: Lexical Shortcut (CRITICAL — FULLY RESOLVED with exp7)
TF-IDF=1.0 IID and 0.96 OOD on DD. Lexical features are inherently strong on DD. BUT: **TF-IDF collapses on ActorAttack (Full=0.261, exp7)**. 9-class=0.972 → 71pp advantage. This is the definitive evidence that domain-adapted representations capture discourse-level features lexical methods cannot.
- Mitigation (fully resolved with exp7): (a) DD: acknowledge lexical separability (TF-IDF per-prefix K1-K5 near-perfect); (b) ActorAttack: TF-IDF catastrophically fails (Recall=0.15), while 9-class maintains 0.972 → proves domain adaptation captures attack structure beyond lexical cues; (c) the "difficulty threshold" narrative: lexical methods work on easy OOD (DD) but fail on hard OOD (ActorAttack), just like vanilla encoders; (d) DD perturbation: Treatment 0pp vs TF-IDF -1.3pp to -9.6pp; (e) interpretability via strategy trajectories. ✅ FULLY RESOLVED

### RC1b: Single-LLM Confound (CRITICAL — RESOLVED with exp8 + exp16)
All training/test data generated by Qwen3-8B → evidence hierarchy might be stylistic artifact. TWO independent mitigations:
1. **exp8 (ToxicChat human data)**: JB-MLM=0.837, 9-class=0.596, vanilla=0.413. All DA >> vanilla (+18-42pp), independent of Qwen3-8B.
2. **exp16 (Mixed Qwen+Llama training, 3 seeds)**: Trains on both Qwen and Llama-3.1-8B generated data. ToxicChat (D051 correction, balanced 408): 9-class=0.550±0.052 ≈ Qwen-only 0.596 — mixed training eliminates confound without degrading performance. Also reveals MLM provides no benefit on mixed data (DD OOD=0.289±0.101 ≈ vanilla=0.291±0.065), confirming "MLM suffices" was Qwen-specific.
3. **exp16b (Llama-only training, seed 42)**: MLM ≤ vanilla on all OOD sets, confirming MLM benefit is not universal across LLM sources.
- **D051 correction**: "dramatically improves human-data generalization" was false (based on eval file mismatch, M020). Mixed training's value: (1) eliminates single-LLM confound, (2) reveals classification-based DAPT as robust mechanism, (3) reveals MLM condition-dependency. NOT human-data improvement. ✅ RESOLVED (not UPGRADED)

### RC2: Small Dataset (RESOLVED with exp17)
480 samples is small for a detection paper.
- **exp17 (1000 Qwen conversations, 3 seeds)**: Doubled dataset with new topic seeds. OOD results consistent with 500-conv baseline: 9-class DD=0.889±0.041, AA=0.913±0.041; vanilla DD=0.326, AA=0.508±0.085. 9-class >> MLM ≈ vanilla hierarchy preserved at 2x scale. IID metrics leaked (M019), but OOD metrics are clean.
- The DAPT evidence hierarchy is robust to dataset scale — 500 conversations are sufficient for the conclusions drawn.
- Mitigation: (a) exp17 scale validation; (b) statistical significance via bootstrap CI; (c) multi-seed (3 seeds all experiments). ✅ RESOLVED

### RC3: Single Attack Type (Crescendo Only)
Need generalization evidence.
- Mitigation: generate FITD-style and Deceptive Delight-style conversations using existing pipeline

### RC4: Strategy Label Quality (D010)
Scrambled-label control (D010) shows correct strategy labels contribute only 1-6pp to cross-attack F1. This is not a confound but a finding: the persuasion multi-task objective works as a supervision signal even with imperfect labels. The 9-class taxonomy's primary value is interpretability (Claim 2), not detection.
- Mitigation: report scrambled control results transparently; position taxonomy as practical training objective with interpretability bonus

### RC5: No Production/LLM-as-Judge Baseline (Dream-surfaced)
Without comparing against zero-shot LLM-based detection (e.g., GPT-4/Claude prompted for conversation-level jailbreak detection), practical positioning is unknown.
- Result (zero-shot, exp5): Qwen3-8B DD macro_F1=0.244 (all predict benign), AA=0.244. GPT-5.5 F1=0.19-0.45 on Crescendo.
- Result (3-shot, exp10): Qwen3-8B DD macro_F1=0.566, AA=0.652. Large improvement over zero-shot but still 43pp/32pp below trained 9-class (0.997/0.972). Precision≈1.0 but Recall≤0.50 — LLM judge misses 50-60% of jailbreaks.
- Interesting: AA > DD for LLM judge (reversed from DeBERTa). DD's surface educational framing precisely deceives content-level analysis; ActorAttack's role-play patterns are more visible to LLM.
- K-value progression: DD K1=0.258 → Full=0.566; AA K1=0.406 → Full=0.652. More turns help LLM but still insufficient.
- NOTE: All LLM judge F1 values are macro F1 (recalculated from binary F1 after M013 correction). ✅ FULLY RESOLVED

### RC6: Interpretability Claims Without Human Eval
Strategy sequence outputs claimed interpretable but not evaluated.
- Mitigation: strategy transition matrix visualization + predicted-label trajectory analysis

### RC7: Related Work Inadequate (Dream-surfaced, THREE-TIER CONSISTENT)
~12 citations is far below venue norms (30-50). Missing coverage of: production safety systems (Llama Guard, WildGuard, ShieldGemma), LLM-as-judge, discourse analysis (RST, PDTB, dialogue acts), computational persuasion (Habernal & Gurevych 2016, Tan et al. 2016), red-teaming (HarmBench, Perez et al. 2022), annotation artifacts (Gururangan et al. 2018), adaptive attacks.
- Mitigation: expand to 30+ citations covering all missing categories (Paper Agent task)

### RC8: Incremental Novelty Over Prior Work (Dream-surfaced, TWO-TIER)
Pragmatic Evasion Asymmetry is a natural corollary of Zeng+Hagendorff+HowDoLLMs. Paper should position as "operationalizing known observations" not "identifying a new phenomenon."
- Mitigation: reframe contribution as operationalization + empirical validation (done in novelty positioning above)

### RC9: Multi-seed and Statistical Rigor (Dream-surfaced, THREE-TIER)
n=72 test set with single seed is inadequate.
- Result: 3-seed completed. Treatment F1=1.00±0.00 (zero variance), Baseline K=1 0.968±0.033. ✅ RESOLVED

### RC10: "None"-Collapse Ablation (Dream-surfaced, TWO-TIER)
Model may reduce to persuasion-presence detector rather than trajectory detector.
- Result: Confirmed (D013/D014). Binary≈9-class on DD (1-2pp gap). Mean pooling≈GRU. Model IS a persuasion-presence detector, not a trajectory detector. Paper acknowledges this honestly; 8-class value is interpretability only. ✅ RESOLVED (acknowledged)

### RC11: Lambda and Architecture Ablation (Dream-surfaced, TWO-TIER)
Lambda and architecture choices not ablated.
- Result: Lambda∈{0,0.3,0.5,2.0} all F1=1.0 (insensitive). Mean pooling≈GRU on IID and DD. Method robust to all hyperparameter/architecture choices. ✅ RESOLVED

## Domain-Adaptive Control Experiments (D018-D020)

### plan_016: Sentiment Control — FAILED (M010: label leakage)
- Sentiment labels perfectly correlated with jailbreak labels (all jailbreak→negative, benign→positive/neutral)
- Experiment invalid, abandoned

### plan_016v2: Topic Classification Control — DD OOD F1=0.541±0.207 (D020, 3-seed)
- 5-class topic classification (no intent head) on same jailbreak training text
- Cramer's V = 0.228, no label leakage
- 3-seed results: seed42=0.727, seed123=0.252, seed456=0.644. Mean=0.541±0.207
- Seed 123 (0.252) BELOW vanilla (0.284) — misaligned supervision can actively hurt
- IID stable: 0.974±0.022 — problem is purely OOD generalization instability
- Interpretation: misaligned classification yields unstable OOD generalization; some seeds worse than no training at all. Domain exposure without task interference (MLM=1.0) is strictly superior.

### plan_017: MLM Continued Pretraining Control — DD OOD F1≈1.0 (D019, 3-seed)
- Pure MLM (15% masking, no classification heads) on same jailbreak training text
- 3-seed DD OOD: K1=0.973±0.019, K2=0.993±0.009, K3=0.997±0.005, K5=0.997±0.005, Full=0.914±0.115
- Full instability from seed=456 GRU recall=0.64 (classifier-level, not embedding-level)
- vs Persuasion 3-seed: Full=0.997±0.005 (s42=1.0, s123=1.0, s456=0.990), K1=0.990±0.013, K2=0.981±0.013, K3=0.972±0.026, K5=0.997±0.005 — persuasion provides near-perfect stability (std 20x smaller than MLM)
- DECISIVE for detection: domain exposure alone achieves near-perfect detection (K≤5). Persuasion adds cross-seed stability (std 20x smaller) + perturbation robustness on DD OOD only (D034: not on ActorAttack) + interpretability.

### plan_018: Wikipedia MLM Control — DD OOD Full=0.904±0.115 (D022→D023, 3-seed)
- MLM on out-of-domain text (Wikipedia), same volume, same hyperparameters as plan_017
- Single seed (42): F1=0.742 — outlier due to GRU instability
- 3-seed: Full=0.904±0.115, K2=0.911±0.073 (other seeds 0.98+)
- vs Jailbreak MLM 3-seed: Full=0.914±0.115 (1pp gap, not significant), K2=0.993±0.009 (8pp gap)
- D023 CORRECTION: domain specificity NOT confirmed at full conversation (1pp gap in noise). Early detection (K≤5) shows ~6-8pp advantage for jailbreak-domain text.
- The real differentiator is persuasion classification (0.997±0.005) vs all MLM variants (~0.91±0.11 at full).

### Complete Control Decomposition (D019-D030, updated with ActorAttack)

| Variant | DD OOD Full | ActorAttack Full | ToxicChat (macro F1) | Pert Δ (IID) | Pert Δ (DD OOD) | Pert Δ (ActorAttack) |
|---------|-------------|-----------------|---------------------|-------------|----------------|---------------------|
| Vanilla DeBERTa | 0.312±0.026 | 0.258±0.000 | 0.413±0.021 | -0.118 | -0.068 (K1) | -0.009 (floor) |
| Wiki MLM | 0.904±0.115 | 0.686±0.297 | 0.791±0.093 | -0.121 | -0.033 | -0.141 |
| Topic classification | 0.541±0.207 | 0.625±0.141 | 0.496±0.042 | -0.040 | n/a | -0.049 |
| TF-IDF | 0.961 (K1=1.0) | **0.261** (K1=0.633) | 0.710 | -0.013 to -0.096 | n/a | n/a |
| Scrambled labels | 0.997±0.005 | 0.951±0.043 | 0.616±0.056 | 0.000 (Full) | +0.003 | **-0.172** |
| Binary persuasion | 0.997±0.005 | 0.990±0.008 | 0.705±0.072 | 0.000 (Full) | +0.003 | **-0.250** |
| JB MLM | 0.914±0.115 | 0.893±0.080 | **0.837±0.013** | -0.026 | +0.027 | **-0.353** |
| **9-class** | **0.997±0.005** | **0.972±0.026** | 0.596±0.087 | **0.000** | **+0.003** | **-0.204±0.135** |
| RoBERTa vanilla | 0.981±0.026 | 0.466±0.163 | — | n/a | n/a | n/a |
| RoBERTa MLM | 0.987±0.018 | 0.730±0.201 | — | n/a | n/a | n/a |
| RoBERTa 9-class | 0.994±0.005 | 0.939±0.046 | — | n/a | n/a | n/a |

**ActorAttack perturbation key finding (exp6, corrected)**: DD OOD Δ≈0 for all classification variants, but ActorAttack DA variants Δ=-0.17 to -0.35. Vanilla Δ=-0.009 (floor effect). Ranking: scrambled (-0.172) < 9-class (-0.204) < binary (-0.250) < MLM (-0.353). 9-class has extreme seed variance (std=0.135: seed123=-0.013, seed42=-0.296, seed456=-0.303). Better models degrade more in absolute terms, but retain large advantage over vanilla under perturbation (9-class perturbed=0.768 >> vanilla=0.248, McNemar p<0.001).

**Key pattern across DD vs ActorAttack (D030)**:
- DD (moderate OOD): scrambled ≈ binary ≈ 9-class → label quality irrelevant (ceiling effect)
- ActorAttack (hard OOD): binary (0.990±0.008) ≈ 9-class (0.972±0.026) ≈ scrambled (0.951±0.043) → all equivalent, max gap 3.9pp within noise at n=3 (D032). Consistent with DD: label quality is not a detection factor at any OOD difficulty
- RoBERTa vanilla: DD=0.981 (no DA needed) vs ActorAttack=0.466 (DA critical) → "no DA needed" was attack-specific
- DeBERTa 9-class (0.972) > RoBERTa 9-class (0.939) on ActorAttack → more extensive DA produces more robust representations

**Cross-LLM Pattern (D049)**:
- Qwen-trained MLM: DD OOD=0.914±0.115 (effective, ~60pp improvement)
- Mixed Qwen+Llama-trained MLM: DD OOD=0.289±0.101 (≈ vanilla, no benefit)
- Llama-only-trained MLM: Llama DD OOD=0.191 ≈ vanilla=0.181 (no benefit)
- 9-class: consistently best across ALL training compositions (Qwen: 0.997, mixed: 0.818, exp17-1000: 0.889)
- **Hypothesis**: Qwen's writing style has more distinctive surface patterns (e.g., structured jailbreak turns with consistent lexical cues) that MLM can capture via token-level co-occurrence learning. Llama's more diverse/natural style distributes signal across pragmatic rather than lexical features, requiring classification supervision to extract. Post-hoc, unverified — note as Discussion point.

**Four-layer value structure (D021-D026, updated D049)**:
1. **Detection**: On single-source Qwen data, continued pretraining (any domain) bridges most of OOD gap (0.28→0.91). **D049 revision**: This does NOT generalize to mixed-LLM or different-source data — on those conditions, only classification-based DAPT (9-class) reliably bridges the gap. On Qwen-only human data (exp8): MLM variants (jb_mlm=0.837, wiki_mlm=0.791) outperform classification variants. **D051 correction**: On mixed-LLM balanced ToxicChat: 9-class=0.550±0.052 ≈ Qwen-only 0.596 — no human-data improvement from mixed training.
2. **Stability**: Classification supervision provides seed stability ON SYNTHETIC OOD: 9-class 0.997±0.005 (std 20x smaller) vs JB MLM 0.914±0.115 vs wiki MLM 0.904±0.115. On human data: pattern REVERSES (9-class std=0.087 highest, jb_mlm std=0.009 lowest).
3. **Cross-seed Stability (Claim 3)**: Classification supervision reduces variance 4-20x vs MLM on synthetic OOD. 9-class std=0.005 (DD) / 0.026 (ActorAttack) vs JB-MLM std=0.115 / 0.080. Consistent across both synthetic OOD families but NOT on human data.
   - **Perturbation (Discussion finding, not Claim)**: DD OOD Δ≈0 for classification variants; ActorAttack ALL degrade (Δ=-0.17 to -0.35). DA advantage persists under perturbation (McNemar p<0.001) but this is Claim 1 corollary.
4. **Interpretability**: Persuasion taxonomy provides strategy trajectories MLM cannot (plan_008)

## Scope Boundary
- IN: persuasion-mediated multi-turn attacks (Crescendo, FITD, Deceptive Delight, social engineering jailbreaks)
- OUT (acknowledged limitation): pure information accumulation attacks, token smuggling, single-frame roleplay
- LIMITATION (D034): Absolute perturbation robustness (Δ≈0) only verified on DD OOD. On ActorAttack, DA variants degrade under paraphrasing (Δ=-0.17 to -0.35; vanilla -0.009 floor effect). Mechanism unverified. DA detection advantage persists under perturbation but at reduced magnitude.
- LIMITATION (D050): Architecture designed for multi-turn detection. ToxicChat (single-turn) performance is zero-shot transfer, not a design target. GRU can learn sequence length as spurious feature — exp17 (larger/longer training data) shows 18.1% single-turn JB detection vs exp16's 89.7%, demonstrating length-dependent GRU fragility on single-turn inputs.
- LIMITATION (D049): MLM DAPT effectiveness is condition-dependent (effective on Qwen-generated data, not on Llama-generated data). Classification-based DAPT (9-class) is the only universally robust adaptation across training data compositions.

## Theoretical Grounding
### Core References
- Bullwinkel et al. (arXiv 2507.02956): per-turn representations kept "benign" by multi-turn attacks
- Speech Act Theory (Austin 1962, Searle 1969): existing detectors at locutionary act level, DisPeD at illocutionary act level
- PAP (Zeng et al., ACL 2024): 40 persuasion techniques for jailbreaking
- Hagendorff (Nature Communications 2026): identifiable persuasion strategies in 97% ASR attacks
- "How Do LLMs Persuade?" (arXiv 2508.05625): persuasion dynamics extractable from turn-level representations

### Must-Cite Categories (Dream-identified gaps)
- **Production safety**: Llama Guard 2/3, ShieldGemma, WildGuard, Constitutional Classifiers
- **Multi-turn defenses**: BIID, G-Guard, SafeDream
- **Discourse analysis**: RST (Mann & Thompson 1988), PDTB, dialogue act classification (Stolcke et al. 2000)
- **Computational persuasion**: Habernal & Gurevych 2016, Tan et al. 2016
- **Red-teaming**: Perez et al. 2022, Ganguli et al. 2022, HarmBench (Mazeika et al. 2024)
- **Adaptive attacks**: Nasr & Carlini et al. 2025
- **Annotation artifacts**: Gururangan et al. 2018, Niven & Kao 2019, Poliak et al. 2018
- **Jailbreak taxonomies**: Wei et al. 2024, Chao et al. 2023 (PAIR)
