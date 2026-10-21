# Method Section Recovery + Practitioner Decision Framework

## Part 1: Method Section Recovery Assessment

### Current State

The method section (§3) currently occupies ~1.5 pages with four subsections: Problem Setup (§3.1), Counterfactual Episode Collection (§3.2), Episode-Level Labeling (§3.3), and Death Avoidance Factor (§3.4). It includes one figure (pipeline overview) and five equations. The formalism is complete at a surface level but several items were compressed during the 10.5→8 page cut.

### Item-by-Item Assessment

#### 1. Per-step oracle tie rate 97.4% — full derivation

**Current treatment**: One sentence in §3.2: "97.4% of steps produce identical intermediate scores regardless of modality (5,726 of 5,878 steps across 11 prescreened task types)."

**What's missing**: No explanation of how per-step comparison was conducted (what "identical intermediate scores" means operationally), no discussion of WHY sparse terminal rewards cause this degeneracy (intermediate scores don't discriminate because only terminal outcome matters), no breakdown by task type showing the tie rate is uniformly high rather than driven by a few task types.

**Assessment**: The current one-sentence treatment is sufficient for readers who accept the claim. However, this number is **the key methodological motivation** for the entire episode-level approach — it justifies why the paper exists. A reviewer asking "why not just do per-step oracle labeling?" needs to see that the answer is structural, not a limitation of our setup. 2-3 sentences of explanation would strengthen this considerably.

**Recommendation**: **Restore 2-3 sentences to the main text** explaining the mechanism (sparse terminal rewards → intermediate scores are uninformative → per-step oracle degenerates). Move the per-task breakdown table to appendix. **+0.05 pages.**

#### 2. Counterfactual framework formal definitions (variable notation)

**Current treatment**: §3.1-3.3 define $\mathcal{O}$, $\mathcal{A}$, $\mathcal{M}$, $\pi$, $\rho$, pure-strategy trajectories, terminal score, death indicator, and the labeling function $L$. Five equations cover the key definitions.

**What's missing**: Essentially nothing substantive. The current notation is clean and complete. The only gap is that Algorithm 1 (the labeling algorithm pseudocode) is referenced but deferred to the appendix.

**Assessment**: The formalism is already at long-paper quality. The labeling algorithm pseudocode would add clarity but is appropriately placed in the appendix since the text description in §3.3 ("death-aware: prioritizes survival over score, then compares scores among same-status episodes") captures the logic concisely.

**Recommendation**: **Keep as-is.** The formal definitions are adequate. Moving Algorithm 1 into the main text would cost ~0.15 pages with marginal benefit since the verbal description is clear. **+0.0 pages.**

#### 3. Death dominance decomposition — mathematical derivation

**Current treatment**: §3.4 states the decomposition $\Delta_{\text{full}} \approx \delta \cdot P + \Delta_{\text{nd}}$ and defines DAF = $1 - \Delta_{\text{nd}} / \Delta_{\text{full}}$. Notes the approximation residual (0.23, or 0.8%). Includes the footnote about DAF > 1 when $\Delta_{\text{nd}} < 0$.

**What's missing**: The decomposition is presented as a definition rather than derived from conditional expectations. A proper derivation would show: $\Delta_{\text{full}} = \mathbb{E}[s^{\text{det}}] - \mathbb{E}[s^{\text{int}}]$, then condition on death status of each strategy (four cases: both die, both survive, only-int dies, only-det dies), showing how the death-asymmetry cases contribute $\delta \cdot P$ while the both-survive cases contribute $\Delta_{\text{nd}}$. This would make explicit what the "approximation" is (the cross-terms from both-die and asymmetric-but-surviving cases).

**Assessment**: For a methodology paper, the decomposition is the intellectual core. A reviewer with statistical training may find the current presentation hand-wavy — the jump from $\Delta_{\text{full}}$ to $\delta \cdot P + \Delta_{\text{nd}}$ skips the conditional expectation algebra. However, the residual is explicitly reported (0.8%), which provides empirical justification. The trade-off is rigor vs. space.

**Recommendation**: **Add 3-4 lines of derivation sketch to the main text** showing the conditioning argument. Not a full proof, but enough to make the decomposition feel derived rather than asserted. The residual reporting already handles the approximation concern. **+0.1 pages.**

#### 4. Episode-level vs step-level analysis justification

**Current treatment**: §3.2 opens with the per-step oracle degeneracy finding (97.4%) and then immediately moves to episode-level collection. The justification is implicit: step-level doesn't work → we do episode-level.

**What's missing**: (a) An explicit argument for why episode-level is the *right* unit of analysis, not just a fallback from step-level failure. Routing decisions compound across episodes — a single bad routing choice at step 5 can lead to death at step 15. The episode is the natural unit of counterfactual comparison because it captures these compounding effects. (b) Connection to the broader literature on trajectory-level vs step-level credit assignment (Ross et al. 2011 DAgger, the multi-step credit assignment problem in RL). (c) A brief note on why the "no free lunch" concern (episode labels applied to step-level routing creates label noise) is expected and informative rather than a limitation.

**Assessment**: This is the strongest candidate for recovery. The current paper's narrative arc is: "step-level fails → we do episode-level → episode-level reveals death dominance → but this signal is task-type-level, not step-level learnable." The philosophical justification for episode-level analysis strengthens the entire chain. It also preempts the reviewer question "why not try harder at step-level labeling?"

**Recommendation**: **Add 4-5 sentences as a dedicated paragraph in §3.2** after the 97.4% finding, making the positive case for episode-level analysis (compounding effects, trajectory as the natural counterfactual unit) before presenting the collection procedure. Reference the step-level label noise (~27.7% misalignment) as a preview of §4.5's router diagnostic. **+0.15 pages.**

### Summary Table

| Item | Verdict | Location | Added Pages |
|------|---------|----------|-------------|
| Per-step tie rate derivation | Restore 2-3 sentences | §3.2 main text | +0.05 |
| Formal definitions / notation | Keep as-is | Already adequate | +0.0 |
| DAF decomposition derivation | Add derivation sketch | §3.4 main text | +0.10 |
| Episode-level justification | Restore paragraph | §3.2 main text | +0.15 |
| **Total** | | | **+0.30** |

### Space Budget Impact

Current paper is at ~8 pages. Adding 0.30 pages requires trimming elsewhere. Candidates:
- Discussion §5 "Practitioner decision framework" paragraph is 6 sentences and could be compressed if the decision framework moves to appendix as a structured figure (+0.15 pages recovered)
- Experiments §4.1 "Sensitivity analysis" paragraph overlaps heavily with appendix references and could lose 2 sentences (+0.05 pages)
- The pipeline figure (Figure 1) is useful but could be reduced to 0.8\columnwidth if needed (+0.05 pages)

Net: recoverable space is ~0.25 pages, close to the 0.30 needed. Feasible with minor tightening.

---

## Part 2: Practitioner Decision Framework

### 50-Episode Pilot Protocol for Routing Signal Diagnosis

**Goal**: Given a new interactive environment with two computation modalities (e.g., internal reasoning vs. deterministic execution), determine whether learned routing adds value over a fixed strategy, using minimal compute.

#### Protocol

**Step 0: Select pilot instances.**
Choose 50 task instances spanning the environment's task-type diversity. Stratify by expected difficulty if task metadata is available. Use a fixed random seed for reproducibility.

**Step 1: Collect paired episodes.**
Run each instance under two pure strategies: always-internal and always-deterministic. Record per-episode: terminal score $s$, binary death/catastrophic-failure indicator $d$, and episode length $T$. Total cost: 100 episodes (50 pairs).

**Step 2: Compute death-rate differential ($\Delta$DR).**

$$\Delta\text{DR} = \text{DR}_{\text{internal}} - \text{DR}_{\text{deterministic}}$$

| $\Delta$DR | Interpretation | Action |
|-----------|---------------|--------|
| $> 15$ pp | Strong death dominance | Go to Step 3 |
| $5$--$15$ pp | Moderate signal | Go to Step 3, but routing may have mixed sources |
| $< 5$ pp | No death dominance | Go to Step 4 |

*Thresholds derived from: ScienceWorld $\Delta$DR = 26.5 pp (strong), MATH $\Delta$DR = 0 pp (none). The 15 pp boundary is set at ~60% of our observed strong signal; the 5 pp boundary accounts for sampling noise at $N=50$ (Wilson 95% CI width $\approx \pm 6$ pp at 20% base rate).*

**Step 3: Assess death dominance magnitude.**
Compute the death-asymmetry label fraction: among episode pairs where the two strategies produce different outcomes (non-tie labels), what fraction have one strategy dying and the other surviving?

$$f_{\text{death}} = \frac{|\{i : d_{\text{int}}^{(i)} \neq d_{\text{det}}^{(i)} \text{ and } \ell_i \neq \text{no-pref}\}|}{|\{i : \ell_i \neq \text{no-pref}\}|}$$

| $f_{\text{death}}$ | Interpretation | Recommendation |
|--------------------|---------------|----------------|
| $> 75\%$ | Death avoidance is the dominant routing signal | **Fixed deterministic strategy will match or exceed any learned router.** Invest in death prevention (grounding, guardrails), not routing. |
| $50$--$75\%$ | Death is major but not sole signal | Learned routing may capture non-death signal. Proceed with caution; expect modest gains over fixed strategy. |
| $< 50\%$ | Diverse routing signal | Learned routing is justified. Proceed to router training. |

*Thresholds derived from: ScienceWorld $f_{\text{death}}$ = 78.9% (strong dominance, router failed to exceed always-det); the 75% boundary captures this regime.*

**Step 4: Check per-step informativeness.**
If $\Delta$DR $< 5$ pp (no death dominance), assess whether step-level routing signal exists. Run per-step oracle comparison on the 50 pairs: at each step, compare the immediate reward/score under both modalities.

$$\text{Tie rate} = \frac{|\{(i,t) : r_{\text{int}}^{(i,t)} = r_{\text{det}}^{(i,t)}\}|}{|\text{all step pairs}|}$$

| Tie rate | Interpretation | Recommendation |
|----------|---------------|----------------|
| $> 90\%$ | Step-level signal is sparse | Episode-level analysis required. Step-level router training will lack supervision signal. |
| $70$--$90\%$ | Moderate step-level signal | Standard per-step oracle labeling is viable. Proceed with step-level router. |
| $< 70\%$ | Rich step-level signal | Per-step routing is well-supported. Dense rewards provide direct supervision. |

*Threshold derived from: ScienceWorld tie rate = 97.4% (extreme sparsity); environments with dense intermediate rewards (e.g., game score increments) would fall below 70%.*

#### Decision Summary (text-based decision tree)

```
Run 50-episode pilot (always-internal vs always-deterministic)
│
├─ ΔDR > 15 pp ──→ Compute f_death
│   ├─ f_death > 75% ──→ STOP: Use fixed deterministic strategy.
│   │                     Invest in death prevention, not routing.
│   └─ f_death ≤ 75% ──→ Mixed signal. Router training may help,
│                         but cap expectations (oracle margin likely small).
│
├─ ΔDR 5-15 pp ──→ Compute f_death (same branches as above,
│                   but with weaker prior on death dominance)
│
└─ ΔDR < 5 pp ──→ No death dominance. Check per-step tie rate.
    ├─ Tie rate > 90% ──→ Sparse rewards. Use episode-level
    │                      counterfactual labeling for routing signal.
    └─ Tie rate ≤ 90% ──→ Standard per-step oracle labeling is viable.
                           Proceed with step-level router training.
```

#### Cost Estimate

- 100 episodes (50 pairs) with a 7B model on ScienceWorld takes ~2 GPU-hours
- Compare to: our full router training consumed ~200 GPU-hours across 28 configurations without exceeding always-deterministic
- The pilot would have predicted that outcome at <1% of the compute cost

#### Validation Against Our Data

| Environment | $\Delta$DR | $f_{\text{death}}$ | Tie rate | Framework prediction | Actual outcome |
|-------------|-----------|-------------------|----------|---------------------|----------------|
| ScienceWorld (Qwen-7B) | 26.5 pp | 78.9% | 97.4% | Fixed det. strategy sufficient | Router ≤ always-det ✓ |
| ScienceWorld (Llama-8B) | 30.0 pp | ~83%* | — | Fixed det. strategy sufficient | Same pattern ✓ |
| ScienceWorld (Qwen-72B) | ~18 pp | ~80%* | — | Fixed det. strategy sufficient | DAF = 90.9% ✓ |
| MATH | 0 pp | — | — | No routing signal | $p = 0.81$ ✓ |

*Estimated from reported label distributions.

#### Placement Recommendation

This framework is currently a prose paragraph in Discussion (§5). Two options:
1. **Discussion (0.3 pages)**: Keep in §5 but restructure as the decision tree above, replacing the current prose paragraph. Fits the "practical implications" role of Discussion.
2. **Appendix**: Move the full decision tree with thresholds and validation table to appendix; keep a 2-sentence pointer in Discussion. Saves ~0.15 pages in main text.

Given the 8-page constraint and the 0.30 pages needed for Method recovery, **Option 2 is recommended**: appendix placement with a Discussion pointer. The framework is a secondary contribution (practical utility) and the appendix allows the full decision tree without space pressure.
