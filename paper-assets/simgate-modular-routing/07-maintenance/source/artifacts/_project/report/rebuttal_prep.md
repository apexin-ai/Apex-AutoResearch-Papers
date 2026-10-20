# EMNLP 2026 ARR Rebuttal Preparation

## Attack 1: Single-Environment Generalization

> "ScienceWorld is just one environment. How generalizable is your framework?"

We appreciate this concern and address it at two levels: the framework's generality and the specific finding's scope.

**Framework generality is empirically demonstrated across three environments.** We apply the identical diagnostic procedure—unchanged—to ScienceWorld, MATH (§3.4), and ALFWorld (§3.4), obtaining qualitatively distinct diagnoses: death dominance (DAF=90.4%), no extractable signal (p=0.81), and information asymmetry (DAF=0%), respectively. Each diagnosis is correct: always-deterministic is optimal for ScienceWorld, neither strategy dominates in MATH, and the information-advantaged strategy wins in ALFWorld. The framework's value lies in producing the correct diagnosis for each environment without modification—it is a diagnostic tool, not a claim that all environments exhibit death dominance.

**The specific finding (death dominance) is replicated across three model families** (Qwen2.5-7B, Llama-3.1-8B, Gemma-2-9B; DAF=88–90%, 2.2pp spread) and persists under 10× scaling to 72B (DAF=92.4%). This cross-model stability confirms death dominance is an environment property, not a model artifact. Additionally, a MiniHack pilot (Appendix R) correctly returns "no signal" as a fourth validated condition, further confirming framework applicability.

**Practical generalizability** is addressed by the ~50-episode pilot protocol (Appendix R), which correctly predicted all four tested conditions. The pilot is designed to be low-cost (4–8 GPU-hours vs. 200 for full router training), enabling practitioners to diagnose any new environment before committing to router development. We explicitly scope our quantitative claims to ScienceWorld while arguing the diagnostic methodology generalizes (Limitations §1).

---

## Attack 2: Trivial Finding

> "Given the -100 death penalty, isn't death dominance obvious?"

The existence of a death penalty makes death *relevant*—not dominant. Whether death avoidance actually accounts for the overwhelming majority of routing signal is an empirical question with three non-trivial answers:

**(i) 10× scaling does not eliminate death dominance.** Qwen2.5-72B reduces death rate from 42.9% to 30.6% but yields DAF=92.4%—higher than the 7B baseline (90.4%). If death dominance were a trivial artifact of weak models, capability scaling should reduce it; instead, the gap between internal and deterministic safety persists because both strategies improve, preserving the differential (§3.3).

**(ii) Reflexion self-correction yields DAF>100%.** Under Reflexion (N=3), Δ_nd=−0.47: the self-correcting agent slightly *outperforms* deterministic on non-death episodes, yet still loses overall because death asymmetry more than accounts for the full gap. This counterintuitive result—a stronger agent performing worse due to catastrophic vulnerability—was not predictable from the penalty structure alone (§3.3).

**(iii) The 0.5B inverted-U.** A 0.5B model shows *reduced* death rate (13.3%) because it is too weak to reach dangerous states, revealing a capability–vulnerability relationship where intermediate-capability models are most vulnerable. This non-monotonic pattern contradicts the intuition that "weaker models die more" (§5).

**Crucially, the primary metric is penalty-independent.** The 78.9% death-asymmetry label fraction holds at any penalty value P>0 (§2.4). DAF is a derived, P-dependent measure; we report both precisely to separate the structural finding (78.9%) from its score-space amplification. At P=0, 54 sole-signal episodes lose their discriminating power, but the remaining 41 non-tie labels still show 51.2% death asymmetry, confirming that death events carry routing-relevant information independent of penalty magnitude.

---

## Attack 3: No Actionable Solution

> "You diagnosed the problem but didn't solve it. What's the practical value?"

Our contribution follows the established pattern of diagnostic work that redirects community effort—analogous to "Attention is not Explanation" (Jain & Wallace, 2019), which did not propose a new attention mechanism but changed how researchers interpret and use attention weights. Similarly, our framework provides three forms of practical value:

**1. Cost-saving diagnostic.** The ~50-episode pilot protocol (Appendix R) answers "should we build a router?" in 4–8 GPU-hours. Our own experience validates this: we invested ~200 GPU-hours training routers (6 SFT variants × 8 seeds × 3 model scales) before the diagnostic framework revealed that always-deterministic is near-optimal. Had the pilot been run first, ~190 GPU-hours of router training would have been avoided. The framework transforms an open-ended engineering question into a quantitative decision with bounded cost.

**2. The diagnosis itself is actionable.** For ScienceWorld, the framework prescribes always-deterministic as the routing strategy—which achieves 90.5% of oracle non-tie decisions (§3.5). This is not "no solution"; it is the correct solution, derived from understanding the mechanism. The finding that routing signal equals task-type identity (confirmed by leave-one-task-type-out degradation to chance, cross-task transfer failure, and majority-vote baseline matching) means practitioners should invest in reducing internal-strategy death rates rather than building routers.

**3. Cross-environment applicability yields different prescriptions.** In ALFWorld (DAF=0%), the framework diagnoses information asymmetry rather than death dominance, suggesting that router development *is* warranted—a qualitatively different recommendation from the same diagnostic tool. The framework's value is not tied to any single prescription but to its ability to generate environment-specific guidance before expensive router training.
