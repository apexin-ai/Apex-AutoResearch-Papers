# Paper Framing — persuasion_turn_jailbreak_detect

## Target Venue
- Primary: EMNLP 2026 Main (ARR submission)
- Deadline: 2026-05-25 (ARR May cycle)
- Track: LLM Security / Discourse and Pragmatics
- Commitment deadline: 2026-08-02

## Title (Working)
DisPeD: Persuasion-Aware Fine-Tuning for Robust Cross-Attack Multi-Turn Jailbreak Detection

## Core Insight
Prior work established that persuasion is systematic in jailbreaks (Zeng et al. 2024), universal in successful attacks (Hagendorff 2026), and extractable from representations (arXiv 2508.05625). DisPeD operationalizes these observations: fine-tuning DeBERTa on an 8-class persuasion taxonomy as a multi-task objective produces turn embeddings that capture attack-relevant pragmatic features. The key finding is that vanilla semantic temporal modeling (the DeepContext-like approach: generic encoder + GRU) catastrophically fails on unseen attack types (F1=0.28 on DD), while persuasion-aware fine-tuning enables robust cross-attack generalization (F1=1.0). Even scrambled strategy labels achieve F1=0.98, confirming that the fine-tuning process on persuasion-related text, not specific label assignments, is the critical ingredient. The 8-class taxonomy additionally provides native interpretability via strategy trajectory analysis.

## Novelty Positioning (Dream-informed)
NOT: "We discover that persuasion patterns exist in jailbreaks" (already known).
NOT: "An evasion hierarchy exists: lexical < semantic < pragmatic" (TF-IDF=0.94 on DD contradicts this).
YES: "We show that vanilla semantic temporal modeling fails catastrophically on unseen attack types, and that persuasion-aware fine-tuning provides an effective and accessible supervision signal for learning cross-attack-robust representations. The persuasion multi-task objective bridges the OOD generalization gap that generic encoders cannot."

## Inherent Lexical Separability (D009)
Persuasive jailbreak conversations and general benign conversations are inherently lexically separable (TF-IDF≈1.0 on ALL data sources including real WildChat). TF-IDF remains strong even OOD (F1=0.94 on DD). The paper acknowledges this and positions DisPeD's value as: (1) bridging the vanilla temporal modeling gap (+72pp on DD), (2) zero degradation under adversarial perturbation (plan_004), (3) interpretability via strategy trajectories.

## Comprehensive Ablation Picture (D014)
Systematic ablation reveals the method's actual mechanism:
- **Critical**: Persuasion-domain DeBERTa fine-tuning (any form) — bridges OOD gap from F1=0.28 to F1=1.0
- **Non-critical**: Label granularity (binary≈scrambled≈8-class, 1-6pp gap on DD), Lambda tuning (all F1=1.0), Temporal modeling (mean pooling≈GRU on DD)
- **Implication**: The persuasion multi-task objective is an effective and accessible supervision signal. Architecture and annotation precision are secondary. 8-class taxonomy provides interpretability, not detection advantage.

## Core Claims (3, priority-ordered)

### Claim 1 (PRIMARY): Cross-Attack Generalization via Persuasion-Aware Fine-Tuning
Fine-tuning DeBERTa on persuasion-annotated conversations produces turn embeddings that enable cross-attack generalization, while vanilla semantic embeddings fail. A model trained on Crescendo detects unseen Deceptive Delight attacks with F1=0.99-1.0 while vanilla DeBERTa collapses to F1=0.28-0.58 (+42-72pp delta). The multi-task persuasion objective acts as an effective supervision signal for learning pragmatic features shared across attack types. Scrambled-label control (D010): randomizing strategy labels reduces cross-attack F1 by only 1-6pp (Scrambled F1=0.935-0.990), confirming that the fine-tuning process on persuasion-related text, not the specific label assignments, is the primary driver. This positions the persuasion taxonomy as a practical, low-annotation-barrier training objective rather than requiring precise strategy labels.
- Evidence: plan_006 DD cross-attack — Treatment F1=0.99-1.0 vs Baseline 0.28-0.58
- Evidence: plan_006 scrambled DD — Scrambled F1=0.935-0.990 (Treatment-Scrambled gap 1-6pp, both >> Baseline +36-70pp)
- Implication: 8-class taxonomy value is primarily interpretability (Claim 2), not detection performance
- Strength: strong empirical support for fine-tuning effect; labels are helpful but not essential

### Claim 2 (ANALYSIS): Characteristic Persuasion Trajectories as Interpretability
Different multi-turn attack types exhibit distinct but recognizable persuasion strategy trajectories: Crescendo shows gradual escalation (mean strategy index 0.86→5.64), FITD follows commitment-escalation patterns, Deceptive Delight uses emotional-manipulation→role-assignment sequences. Benign conversations lack these structured escalation patterns. NOTE (D014): mean pooling ≈ GRU on DD, so the model does NOT rely on temporal ordering for detection. Trajectories are a descriptive/interpretability contribution, not a detection mechanism.
- Evidence: plan_008 strategy transition matrices
- Evidence: plan_015 DD — mean pooling F1=1.0 ≈ GRU F1=1.0, proving detection doesn't depend on turn ordering
- Strength: descriptive/analytical, interpretability value only; does NOT drive detection performance

### Claim 3 (EMPIRICAL): Robustness Under OOD and Adversarial Perturbation
Vanilla semantic temporal modeling is consistently the most fragile approach: catastrophic OOD failure (F1=0.28 on DD) and significant perturbation degradation (-12-15pp). Persuasion-aware fine-tuning is the most robust: F1=1.0 on unseen attacks AND zero degradation under adversarial perturbation at K≥2. TF-IDF is intermediate: strong OOD (0.94) and mostly robust under perturbation at K≥3 (-1.3pp), but degrades at early detection K=1 (-9.6pp). The strongest differentiation is at **early detection under perturbation** (K=1): Treatment -2.6pp vs TF-IDF -9.6pp vs Baseline -14.6pp.
- Evidence: plan_006 cross-attack — Treatment=1.0, TF-IDF=0.94, Baseline=0.28 on DD
- Evidence: plan_004 perturbation (D012) — Treatment 0pp at K≥2, Baseline -12-15pp, TF-IDF -1.3pp(K≥3) to -9.6pp(K=1)
- Note: Treatment vs TF-IDF gap is small at K≥3 (1.3pp, n=76). Strongest claim is at K=1-2.
- Strength: strong empirical support across both OOD and perturbation dimensions

## Story Spine

**Problem**: Multi-turn jailbreak attacks (Crescendo, FITD, Deceptive Delight) distribute adversarial intent across individually benign turns. Bullwinkel et al. (2025) show per-turn representations are deliberately kept in a "benign" region, causing representation-level defenses to fail with a 50-point ASR gap. DeepContext (Su et al., arXiv 2602.16935, 2026) tracks generic semantic drift via RNN over BERT embeddings (F1=0.84) but confuses benign conversational evolution with adversarial manipulation.

**Gap**: Vanilla semantic temporal modeling (the natural approach: generic encoder + RNN over turn embeddings) catastrophically fails to generalize across attack types. DeepContext achieves F1=0.84 on in-distribution data but the approach collapses to F1=0.28 on unseen attack families. Production multi-turn guards (Llama Guard, WildGuard, ShieldGemma) and LLM-as-judge approaches detect individual harmful outputs but not the adversarial manipulation process. No published work uses persuasion-grounded fine-tuning to bridge this OOD generalization gap.

**Our angle**: DisPeD uses persuasion strategy classification as a multi-task fine-tuning objective, teaching the encoder to attend to attack-relevant pragmatic features shared across attack types. Aggregation over fine-tuned turn embeddings (mean pooling or GRU, both equivalent per plan_015) enables conversation-level detection. The persuasion objective provides an accessible supervision signal: even with imperfect (scrambled) strategy labels or binary labels, fine-tuning on persuasion-related text produces representations that generalize to unseen attacks (F1=1.0 on DD), while vanilla embeddings collapse (F1=0.28). The 8-class taxonomy additionally enables native interpretability through strategy trajectory analysis.

**Headline result**: "Vanilla semantic temporal modeling collapses on unseen attack types (F1=0.28 on Deceptive Delight). DisPeD, fine-tuned on persuasion strategy classification, achieves F1=1.0 on the same unseen attacks (+72pp). This generalization survives label scrambling (F1 drops only 1-6pp), confirming that the persuasion fine-tuning objective, not precise annotations, bridges the cross-attack OOD gap."

## Architecture

1. **Stage 1**: DeBERTa-v3-base fine-tuned on multi-task objective: 8-class persuasion strategy classification + binary jailbreak-intent classification
2. **Stage 2**: Aggregation (GRU or mean pooling, equivalent per plan_015) over DeBERTa [CLS] embeddings for conversation-level binary classification
3. **Baseline**: Same pipeline but with vanilla (not fine-tuned) DeBERTa embeddings
Note: plan_015 shows GRU ≈ mean pooling on both IID and OOD. Paper reports GRU as default architecture but ablation shows temporal modeling is not the source of improvement.

## Venue Fit Risks
- EMNLP 2026 LLM Security track: strong fit (dedicated track, high visibility)
- Discourse/Pragmatics reviewers may want more linguistic rigor: ground taxonomy in PAP (ACL 2024), Hagendorff (Nature Comm 2026), Cialdini principles, Speech Act Theory (Austin 1962, Searle 1969)
- Safety reviewers expect multiple attack types: need >= 2 attack families

## Anticipated Reviewer Concerns

### RC1: Lexical Shortcut (CRITICAL, must address pre-submission)
TF-IDF=1.0 IID and 0.94 OOD on DD. Lexical features are inherently strong for this task (D009). DisPeD cannot claim superiority over TF-IDF on raw detection performance alone.
- Mitigation strategy (post-D010): (a) acknowledge inherent lexical separability honestly; (b) DisPeD's primary value vs TF-IDF is interpretability (strategy trajectories, Claim 2) and bridging the vanilla temporal modeling gap (Claim 3); (c) plan_004 adversarial perturbation (pending): if TF-IDF degrades under paraphrasing but treatment doesn't, this demonstrates complementary robustness; (d) the core comparison that motivates DisPeD is vs vanilla DeBERTa+GRU (DeepContext approach, F1=0.28 on DD), not vs TF-IDF; (e) persuasion fine-tuning as supervision signal is the contribution, not beating a bag-of-words

### RC2: Small Dataset
480 samples is small for a detection paper.
- Mitigation: (a) statistical significance via bootstrap CI or paired tests; (b) cross-validation; (c) focus narrative on proof-of-concept for the principle, not SOTA numbers

### RC3: Single Attack Type (Crescendo Only)
Need generalization evidence.
- Mitigation: generate FITD-style and Deceptive Delight-style conversations using existing pipeline

### RC4: Strategy Label Quality (D010)
Scrambled-label control (D010) shows correct strategy labels contribute only 1-6pp to cross-attack F1. This is not a confound but a finding: the persuasion multi-task objective works as a supervision signal even with imperfect labels. The 8-class taxonomy's primary value is interpretability (Claim 2), not detection.
- Mitigation: report scrambled control results transparently; position taxonomy as practical training objective with interpretability bonus

### RC5: No Production/LLM-as-Judge Baseline (Dream-surfaced)
Without comparing against zero-shot LLM-based detection (e.g., GPT-4/Claude prompted for conversation-level jailbreak detection), practical positioning is unknown.
- Result: GPT-5.5 (frontier LLM) achieves F1=0.19-0.45 on Crescendo (precision=1.0, recall=0.11-0.29). Qwen3-8B F1=0.0-0.15. Both far below Treatment F1=1.0. GPT-5.5 is deceived by Crescendo's "surface educational framing," confirming that content-level analysis cannot detect persuasion dynamics. Unparseable rate 30-47% (increases with conversation length); paper must report this and provide unparseable-excluded upper bound. Even assuming best-case unparseable correction, LLM judge F1 ≈ 0.7-0.8, still far below Treatment=1.0. ✅ RESOLVED

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

## Scope Boundary
- IN: persuasion-mediated multi-turn attacks (Crescendo, FITD, Deceptive Delight, social engineering jailbreaks)
- OUT (acknowledged limitation): pure information accumulation attacks, token smuggling, single-frame roleplay

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
