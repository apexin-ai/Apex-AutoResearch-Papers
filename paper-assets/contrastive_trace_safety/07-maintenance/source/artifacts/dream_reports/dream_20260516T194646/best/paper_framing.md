# Paper Framing — contrastive_trace_safety

## Target Venue
- Primary: EMNLP 2026 Main (LLM Security Track)
- Fallback: EMNLP 2026 Findings
- Deadline: ARR submission May 25, 2026 (9 days)

## Core Claims (3 条)

1. **Static hidden-state probes fail to reliably detect safety commitment in reasoning model traces** — static per-step probes (LogisticRegression, linear classifiers analogous to SafeSwitch/SIREN) achieve <50% detection coverage on the commitment detection task, despite hidden states containing strong safety-relevant signal (Fisher discriminant ratio 17-18 in full representation space).

2. **Temporal window probes saturate oracle-achievable detection coverage** — a simple temporal window LogisticRegression (W=15 steps) achieves 76.7% detection coverage, matching the label-oracle upper bound. The +30pp improvement over static probes comes from capturing "safety reasoning density decline" patterns invisible to single-step classification.

3. **Pre-textual detection of safety commitment is fundamentally limited in hidden-state space** — no hidden-state method (static, temporal window, or sequential GRU) achieves positive detection lead time. The oracle's +31-step advantage comes from directly observing label sequences; hidden states encode current safety state but not future safety trajectory. This establishes a principled limitation boundary for hidden-state monitoring approaches.

## Story Spine

- **Problem**: Reasoning models exhibit "self-jailbreak" — safety reasoning and harmful execution are interleaved throughout extended CoT (84% of traces contain safety labels after step 10), culminating in a "commitment point" where safety reasoning permanently ceases. Existing hidden-state jailbreak detectors (TrajGuard, SafeSwitch, SIREN) are designed for instruction-tuned models where the attack is an adversarial INPUT; they have never been evaluated on reasoning-model self-jailbreak where the attack is the model's OWN reasoning process.

- **Existing approaches & their gaps**: Hidden-state detectors achieve 95% defense rate on standard LLMs (TrajGuard) but operate at token-level granularity. Reasoning-model safety analysis (Self-Jailbreaking, HarmThoughts) characterizes the phenomenon but doesn't provide deployable detectors. Text-level CoT monitors (SafeRemind, SafeThink) are vulnerable to pathological CoT. No work bridges hidden-state detection TO reasoning-model self-jailbreak.

- **Our framing**: We provide the first systematic evaluation of hidden-state detection methods on reasoning-model safety commitment, discovering that (a) the safety signal exists but is distributed across minor principal components (PCA top-3 explains only 17% variance, Fisher drops from 17→1), making geometric methods (Mahalanobis/TrajGuard) fail; (b) temporal context is critical for reliable detection but cannot anticipate future safety trajectory; (c) a simple temporal window probe is surprisingly optimal — complex architectures (GRU) offer no advantage at current data scales.

- **Headline result template**: "On HarmThoughts reasoning traces, temporal window probes achieve 76.7% detection coverage (matching oracle ceiling), while static probes achieve only 46.5% — but no method achieves pre-textual detection (best lead time = -0.2 steps vs oracle +31 steps)."

## Venue Fit Risks

- **EMNLP LLM Security track fit**: Strong — defense/detection method for reasoning model jailbreak, directly addressing "defense lags behind attack" gap noted in track CFP.
- **Method simplicity risk**: Core method is temporal window LogisticRegression (not a novel architecture). Mitigate: frame as empirical study with method insight ("simplicity IS the finding — complex temporal models don't help at this data scale").
- **Negative finding risk**: Claim 3 (pre-textual detection impossible) could be seen as "limitation" not "contribution." Mitigate: frame as establishing principled boundary — knowing what's NOT possible is valuable for practitioners deploying safety monitors.
- **Cross-architecture coverage**: MVP only tested on r1-8b (Llama-3.1 base). Must validate on Qwen2.5-based models (r1-32b, QwQ-32B) for the "cross-architecture" story. If temporal advantage doesn't hold cross-architecture → Claim 2 weakens to single-model.

## Anticipated Reviewer Concerns

1. "Temporal window LR is trivial — where's the method novelty?" → Primary contribution is empirical study; method insight is that simplicity matches oracle ceiling.
2. "Only tested on one model family" → Cross-architecture experiments (P0) will address.
3. "Lead time is negative — what's the practical use?" → Coverage matters for post-hoc audit; real-time monitoring with ≤0 lead time still allows intervention at commitment point (vs missing it entirely with static methods).
4. "209 training traces is too few — results may not generalize" → Cross-model validation + bootstrap CIs.
5. "Why not use the full 16-label taxonomy for richer supervision?" → Ablation planned (P1).
