# Paper Framing — contrastive_trace_safety

## Target Venue
- Primary: EMNLP 2026 Main (LLM Security Track)
- Deadline: ARR submission May 25, 2026 (9 days)

## Core Claims (3 条)

1. **Hidden-state probes achieve substantially more precise safety commitment detection than text-based monitoring** — on HarmThoughts traces (r1-8b), hidden-state temporal probes achieve pre-commitment FPR 16% vs text-based probes' 27-36% (1.7-2.2x lower), with precision 58-62% vs 45-49% (+10-13pp). Coverage is comparable between modalities (both ~65% with temporal window), but hidden-state monitoring fires more accurately in the critical pre-commitment window. Unsupervised geometric methods (Mahalanobis/TrajGuard) fail entirely due to signal distribution in minor principal components.

2. **Temporal context is necessary for commitment detection regardless of signal modality** — both hidden-state and text-based probes gain ~+5pp coverage from temporal windowing (W=15), confirming that commitment detection requires multi-step context. GRU sequence models can push coverage further (76-93%, unstable across seeds) but at the cost of higher false positive rates (safe FPR 62% vs LR 39%). The temporal improvement is method-agnostic; the precision advantage is modality-specific.

3. **Pre-textual detection of safety commitment remains fundamentally unreliable** — neither sequential models (GRU: mean lead +4.7-8.4 steps, median 0), change-point detection (BOCPD: coverage 93% but lead +3.5 < simple threshold +4.9), nor text monitoring achieves reliable early detection. CUSUM fails entirely. The oracle's +31-step advantage (100% early detection) reveals that hidden states encode current safety state well but poorly predict future trajectory. This is a principled limitation, not a method gap.

## Story Spine

- **Problem**: Reasoning models exhibit "self-jailbreak" — safety reasoning and harmful execution interleave throughout extended CoT, culminating in a "commitment point" where safety reasoning permanently ceases. Existing hidden-state detectors (TrajGuard, SafeSwitch, SIREN) target adversarial INPUT attacks on instruction-tuned models; they have never been evaluated on reasoning-model self-jailbreak where the threat is the model's OWN reasoning process.

- **Existing approaches & gaps**: Hidden-state detectors achieve 95% defense on standard LLMs (TrajGuard) but operate at token-level. Reasoning-model safety analysis (Self-Jailbreaking, HarmThoughts) characterizes the phenomenon without providing deployable detectors. Text-level CoT monitors (SafeRemind, SafeThink) are vulnerable to pathological CoT and, as we show, produce higher false positive rates in the pre-commitment window.

- **Our framing**: We provide the first systematic evaluation of detection methods for reasoning-model safety commitment, discovering that: (a) the safety signal exists in hidden states but is distributed across minor principal components (PCA top-3 explains 17% variance, Fisher drops 17→1), causing geometric detectors to fail; (b) temporal context is necessary for both hidden-state and text probes, but hidden-state probes achieve decisively lower pre-commitment false positive rates (16% vs 27-36%); (c) despite positive mean lead time, pre-textual detection remains unreliable — GRU, BOCPD, and CUSUM all fail to reliably detect before textual commitment, establishing a principled gap between current capabilities and the oracle ceiling.

- **Headline result**: "On HarmThoughts traces, hidden-state temporal probes detect safety commitment with 16% pre-commitment FPR and 62% precision, compared to text-based probes' 27-36% FPR and 45-49% precision. Both modalities benefit equally from temporal context (+5pp coverage), but reliable pre-textual detection remains elusive (GRU: 39% early detection rate vs oracle 100%)."

## Key Evidence Summary (r1-8b, n=43 test traces)

| Method | Coverage | Lead Time | Pre-CP FPR | Precision | Safe FPR |
|--------|----------|-----------|------------|-----------|----------|
| Text static | 60.5% | +4.3 | 35.6% | 44.8% | 50.2% |
| Text temporal W=15 | 65.1% | +11.5* | 27.2% | 48.7% | 38.5% |
| HS static LR L14 | 60.5% | +3.0 | 16.2% | 62.2% | 39.0% |
| HS temporal LR W=15 | 65.1% | +4.9 | 16.0% | 58.3% | 39.2% |
| GRU multi-7L h=256 | 76-93%** | +4.7-8.4** | 28.0% | 57.3% | 61.6% |
| BOCPD lambda=10 | 93.0% | +3.5 | n/a | n/a | n/a |
| TrajGuard (MD) | failed | — | — | — | — |

*Text lead time inflated by high pre-CP FPR (trigger-happy detection)
**GRU results vary significantly across training runs — multi-seed reporting required

## Venue Fit Risks

- **EMNLP LLM Security track fit**: Strong — defense/detection evaluation for reasoning model jailbreak.
- **Method simplicity risk**: Core methods are temporal LR and GRU — neither architecturally novel. Mitigate: frame as empirical study with method insight; contribution is systematic evaluation + discovery of what matters (temporal context + precision advantage of hidden states).
- **Statistical power risk**: n=43 traces on r1-8b yields wide confidence intervals (exp-006 bootstrap: temporal vs static coverage p=0.572). Mitigate: cross-architecture validation on 32B models (exp-001/002) — consistent effects across 3+ models is strong evidence even without per-model significance.
- **High safe FPR risk**: All methods show 39-62% safe FPR — deployment utility is limited. Must acknowledge honestly as limitation. Frame: these are linear probes as diagnostic tools; production deployment would require threshold tuning + ensemble methods.

## Anticipated Reviewer Concerns

1. "Temporal window LR is trivial — where's the method novelty?" → Primary contribution is empirical study; insight that simple methods saturate oracle ceiling. BOCPD evaluation adds systematic method comparison.
2. "Only tested on one model family" → Cross-architecture experiments (P0) on r1-32b + QwQ-32B will validate. [IN PROGRESS]
3. "GRU results are unstable" → Will report multi-seed mean+/-std. Coverage variance (76-93%) is itself informative about signal reliability.
4. "209 training traces is too few" → Cross-model validation + bootstrap CIs + per-fold CV variance.
5. "Why not fine-grained 16-label taxonomy?" → Ablation planned (P1).
6. "Text baseline comparison?" → RESOLVED: text baseline shows HS has decisive precision advantage (pre-CP FPR 16% vs 27-36%).
7. "Commitment point definition circular?" → CP defined as last safety label + 1; cross-model consistency suggests real phenomenon.
8. "Missing related work?" → RESOLVED: RepE, refusal direction, PRMs, BOCPD, control tasks all cited.
9. "No FPR analysis?" → RESOLVED: full FPR + precision analysis on safe traces completed.
10. "All safe FPR > 39% — is this useful?" → NEW. Frame as diagnostic tool limitation; threshold tuning for deployment is future work. The precision ADVANTAGE of HS over text holds regardless.

## Title Candidates
- "Temporal Probing for Safety Commitment Detection in Reasoning Models"
- "When Does Temporal Context Matter? Hidden-State Detection of Safety Commitment in Reasoning Models"
- "Hidden-State vs. Text Monitoring for Safety Commitment Detection in Reasoning Models"
