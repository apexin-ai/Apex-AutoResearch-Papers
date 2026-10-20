# Paper Framing — simgate-modular-routing

## Target Venue
- Primary: EMNLP 2026 Main (ARR short paper, 4 pages + references)
- Fallback: EMNLP 2026 Findings
- Deadline: ARR May 25, 2026 (12 days remaining)

## Core Insight

LLM agents on rule-governed environments face catastrophic failures from hallucinated state transitions. Deterministic external computation (environment simulators, code interpreters) eliminates these failures at CPU-only cost — but no method learns WHEN to invoke it via an explicit, interpretable router. MVP evidence: death avoidance is the primary mechanism (+30-40 points from preventing -100 penalties), and selective routing outperforms unconditional simulation by +10-17 points.

## Core Claims (2 claims for short paper)

**C1 (Selective routing to deterministic computation)**: On ScienceWorld, learned selective routing to a deterministic environment simulator significantly outperforms both pure LLM reasoning and unconditional simulation. The primary value mechanism is catastrophic failure prevention: the simulator serves as a "safety net" that intercepts actions leading to irreversible negative outcomes, rather than providing positive task guidance.

**C2 (Explicit modular router)**: A lightweight explicit router (Qwen3-1.7B, ~1.7B params), trained via SFT on counterfactual trajectory labels, achieves effective per-step routing that is (a) interpretable — routing decisions can be analyzed per task category to reveal systematic LLM failure modes, (b) architecturally decoupled from the agent backbone, and (c) consistent across task categories sharing similar failure patterns.

## Story Spine

- **Problem**: LLM agents hallucinate state transitions on rule-governed environments (temperature physics, chemical reactions), leading to catastrophic failures. ITP-R routes to an approximate LLM world model but underperforms pure internal reasoning (62.58 vs CogRouter 84.6 on ScienceWorld). ReTool/AgentMath learn when to invoke code interpreters but use implicit routing entangled with the backbone. No method provides an explicit, modular router for selective invocation of ground-truth deterministic computation.

- **Our framing**: We recast the "when to simulate" problem as safety-aware routing. Deterministic computation is not primarily a performance booster — it is a catastrophic failure prevention mechanism. A lightweight explicit router learns to detect high-risk states where LLM reasoning is likely to fail catastrophically, and routes those steps to deterministic computation for ground-truth verification. This "router-as-safety-net" framing explains why: (1) the gain is concentrated in death avoidance (+30-40 points from preventing -100 penalties), (2) selective routing beats unconditional simulation (not every step needs the safety net), and (3) the router's decisions are interpretable as a diagnostic of where LLMs systematically fail.

- **Headline result template**: "On ScienceWorld, SimGate achieves [X] score (vs CogRouter 84.6, ITP-R 62.58), reducing catastrophic failures by [Y]% compared to pure LLM reasoning, while using [Z]% fewer simulator invocations than always-simulate."

## Paper Structure (4-page short paper)

| Section | Pages | Content |
|---------|-------|---------|
| Abstract | 0.2 | Safety-aware routing framing, headline numbers |
| Introduction | 0.8 | Problem + gap + contribution (2 claims) |
| Method | 1.0 | 3-component framework: backbone + deterministic oracle + explicit router; counterfactual training pipeline (4-step); router architecture |
| Experiments | 1.5 | Main results table + explicit vs implicit ablation + routing pattern analysis figure |
| Conclusion | 0.3 | Summary + limitations + future (MATH, API routing) |
| References | ~0.5 | Not counted in 4-page limit |

## Anticipated Reviewer Concerns & Mitigations

1. **"Novelty is incremental — just SFT a small model to classify"**
   - Mitigation: Contribution is the empirical finding (death avoidance mechanism + routing patterns) more than the architecture. Router-as-diagnostic-probe reveals systematic LLM failure modes. Explicit vs implicit ablation quantifies the gap.

2. **"Only one benchmark (ScienceWorld)"**
   - Mitigation: Short paper format justifies focused evaluation. ScienceWorld uniquely tests rule-governed dynamics with catastrophic penalties. Discuss MATH/API extension as future work.

3. **"Comparison unfair — CogRouter uses RL (CoPO), you use SFT"**
   - Mitigation: Our primary comparison is SimGate vs ablated baselines (always-internal, always-deterministic, random, heuristic) — all same training budget. CogRouter/ITP-R cited from papers for context.

4. **"Death avoidance is trivial — just filter dangerous actions"**
   - Mitigation: Always-deterministic (which filters every step) underperforms oracle routing by 10-17 points. The non-trivial part is SELECTIVE invocation — knowing which steps need the safety net. Routing pattern analysis shows the router learns meaningful state-dependent decisions.

5. **"DAgger gap — SFT on oracle labels under base policy may not transfer"**
   - Mitigation: Acknowledge explicitly (cite Ross et al. 2011). Report train/test gap. If significant, discuss DAgger-style iterative relabeling as extension.

## Venue Fit Risks

- EMNLP LLM Agents track is a natural fit (tool use + planning + evaluation)
- Short paper format matches focused contribution scope
- Risk: Reviewer may expect ALFWorld evaluation (standard agent benchmark pair) — address in "Scope & Future Work" paragraph
- Risk: "Safety-aware" framing may be perceived as overselling if death avoidance is the ONLY signal — need to check if positive guidance signal emerges in full trajectory collection (even small positive guidance would strengthen the story)

## Key Differences from IDEA_BRIEF

1. **Scope narrowed**: IDEA_BRIEF proposed 3 tracks (ScienceWorld + ALFWorld + MATH). Short paper focuses on ScienceWorld only in main text; MATH as P1 extension; ALFWorld deferred.
2. **Framing shifted**: From "general routing to deterministic computation" to "safety-aware routing" based on MVP death avoidance finding.
3. **Claims reduced**: From 4 hypotheses (H1-H4) to 2 focused claims (C1-C2).
4. **"ANY form" softened**: Per Human Review Note #4, "across multiple forms" instead of "ANY form". Paper demonstrates principle on simulators; code interpreters discussed as extension.
