# Paper Framing — persuasion_turn_jailbreak_detect

## Target Venue
- Primary: EMNLP 2026 Main (ARR submission)
- Deadline: 2026-05-25 (ARR May cycle)
- Track: LLM Security / Discourse and Pragmatics
- Commitment deadline: 2026-08-02

## Title (Working)
DisPeD: Exploiting the Pragmatic Evasion Asymmetry for Robust Multi-Turn Jailbreak Detection

## Core Insight
Multi-turn jailbreak attacks can easily vary lexical and semantic content of individual turns, but the discourse-level persuasion playbook (rapport → reframing → escalation) is a structural necessity for attack success. Removing any stage either fails the attack or reduces it to a single-turn attack already covered by existing defenses. DisPeD exploits this asymmetry by fine-tuning DeBERTa on persuasion strategy classification, producing turn embeddings that encode pragmatic function rather than (only) semantic content.

## Core Claims (3)

### Claim 1: Pragmatic Evasion Asymmetry (Theoretical + Empirical)
An evasion hierarchy exists for multi-turn jailbreak detection: lexical features (easily evaded via paraphrasing) < semantic embeddings (moderate, per-turn representations kept "benign" per Bullwinkel et al. 2025) < pragmatic persuasion patterns (structurally difficult to evade, as the persuasion playbook is a functional prerequisite for attack success).
- Evidence needed: adversarial perturbation experiment showing treatment degrades less than lexical/semantic baselines under paraphrasing

### Claim 2: Early Detection via Persuasion Grounding
Persuasion-grounded turn embeddings (DeBERTa fine-tuned on 8-class persuasion taxonomy + intent) enable significantly earlier detection of multi-turn jailbreaks (at K=2-3 turns) compared to vanilla semantic embeddings, because persuasion strategy transitions (rapport → authority framing) manifest before explicitly harmful content appears.
- Evidence needed: early detection F1 at K=2,3 turns, treatment > baseline by >= 5pp on clean data (TF-IDF < 0.75)

### Claim 3: Monotonic Escalation Trajectory
Adversarial conversations exhibit a monotonic escalation trajectory in persuasion strategy space (trust → test → normalize → elicit), while benign conversations exhibit oscillatory or non-monotonic patterns. This distinction is the mechanistic basis for Claims 1-2.
- Evidence needed: strategy transition matrix visualization, trajectory analysis comparing jailbreak vs benign

## Story Spine

**Problem**: Multi-turn jailbreak attacks (Crescendo, FITD, Deceptive Delight) distribute adversarial intent across individually benign turns. Bullwinkel et al. (2025) show per-turn representations are deliberately kept in a "benign" region, causing representation-level defenses to fail with a 50-point ASR gap. DeepContext (2026) tracks generic semantic drift but confuses benign conversational evolution with adversarial manipulation.

**Gap**: Existing detectors operate at the lexical or semantic level where attacks deliberately hide. No published work combines persuasion-grounded turn representations with temporal sequence modeling for multi-turn jailbreak detection.

**Our angle**: We identify the Pragmatic Evasion Asymmetry. The persuasion playbook (rapport → reframing → escalation) is a structural necessity for multi-turn attack success. Unlike lexical or semantic features, pragmatic persuasion patterns cannot be evaded without abandoning the attack itself. DisPeD fine-tunes DeBERTa on an 8-class persuasion taxonomy to produce pragmatic-aware turn embeddings, then models the temporal strategy sequence with a GRU to detect the characteristic escalation trajectory.

**Headline result**: "DisPeD detects Crescendo-style jailbreaks at K=2 turns with F1=X vs Y for vanilla semantic baselines (+Z pp). Under adversarial paraphrasing that removes lexical cues, DisPeD maintains F1=W while lexical baselines degrade by V pp."

## Architecture (Simplified for MVE)

Single-track with persuasion grounding (full dual-track in future work):
1. **Stage 1**: DeBERTa-v3-base fine-tuned on multi-task objective: 8-class persuasion strategy classification + binary jailbreak-intent classification
2. **Stage 2**: Bi-GRU over DeBERTa [CLS] embeddings for conversation-level binary classification
3. **Baseline**: Same pipeline but with vanilla (not fine-tuned) DeBERTa embeddings

## Venue Fit Risks
- EMNLP 2026 LLM Security track: strong fit (dedicated track, high visibility)
- Discourse/Pragmatics reviewers may want more linguistic rigor: ground taxonomy in PAP (ACL 2024), Hagendorff (Nature Comm 2026), Cialdini principles, Speech Act Theory (Austin 1962, Searle 1969)
- Safety reviewers expect multiple attack types: need >= 2 attack families

## Anticipated Reviewer Concerns

### RC1: Lexical Shortcut (CRITICAL, must address pre-submission)
TF-IDF=1.0 on current data means lexical features alone perfectly separate classes. Must show the model works on data without lexical shortcuts.
- Mitigation: (a) register-normalize jailbreak data to match benign register, verify TF-IDF < 0.75, retrain; (b) adversarial perturbation evaluation (Claim 3)

### RC2: Small Dataset
480 samples is small for a detection paper.
- Mitigation: (a) statistical significance via bootstrap CI or paired tests; (b) cross-validation; (c) focus narrative on proof-of-concept for the principle, not SOTA numbers

### RC3: Single Attack Type (Crescendo Only)
Need generalization evidence.
- Mitigation: generate FITD-style and Deceptive Delight-style conversations using existing pipeline

### RC4: Strategy Label Confound (M004)
Benign turns hardcoded to strategy=7 creates shortcut for treatment model.
- Mitigation: (a) fix labeling (use "none"/9th class); (b) scrambled-label ablation

### RC5: No DeepContext Comparison
Paper positions against DeepContext but no reproduction.
- Mitigation: vanilla DeBERTa → GRU is a fair proxy baseline (same architecture, only difference is persuasion grounding). Note DeepContext has no public code. If time allows, attempt reproduction as P1.

### RC6: Interpretability Claims Without Human Eval
Strategy sequence outputs claimed interpretable but not evaluated.
- Mitigation: strategy transition matrix visualization (P1). Full human eval is future work given timeline constraints.

## Scope Boundary
- IN: persuasion-mediated multi-turn attacks (Crescendo, FITD, Deceptive Delight, social engineering jailbreaks)
- OUT (acknowledged limitation): pure information accumulation attacks, token smuggling, single-frame roleplay
- The semantic GRU track provides coverage for out-of-scope attack types as a safety net

## Theoretical Grounding
- Bullwinkel et al. (arXiv 2507.02956): per-turn representations kept "benign" by multi-turn attacks
- Speech Act Theory (Austin 1962, Searle 1969): existing detectors work at locutionary act level, DisPeD at illocutionary act level
- PAP (Zeng et al., ACL 2024): 40 persuasion techniques for jailbreaking
- Hagendorff (Nature Communications 2026): identifiable persuasion strategies in 97% ASR attacks
- "How Do LLMs Persuade?" (arXiv 2508.05625): persuasion dynamics extractable from turn-level representations
