# Paper Framing: Calibration Failure Taxonomy for LLM User Simulators

> Plan B story — Director approved 2026-05-13
> Target: EMNLP 2026 Findings (ARR deadline 2026-05-25)

---

## Title Candidates

1. **"Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation"**
   - Pro: 直接点明贡献（taxonomy），关键词覆盖好
   - Con: 稍长

2. **"The Calibration Trap: Prompt-Based and Training-Based Corrections Both Fail for Dialect Bias in LLM User Simulators"**
   - Pro: "trap" 吸引眼球，涵盖两种方法
   - Con: 可能暗示过于 negative

3. **"Behavioral Calibration Considered Harmful? Systematic Failure Modes in Dialect-Aware User Simulation"**
   - Pro: Dijkstra 风格标题引发好奇，问号留余地
   - Con: "Considered Harmful" 可能被认为 cliché

**推荐**: Title 1 — 最准确传达贡献，reviewer-friendly。

---

## Core Story

**Problem**: LLM user simulators exhibit dialect-dependent behavioral biases — AAVE and Indian English speakers receive systematically different politeness and question-asking patterns compared to Standard American English (sim2real2026gap; seshadri2026lost). These biases propagate into agent evaluation, undermining fairness.

**Attempted Solution**: We apply two complementary calibration strategies:
- **BCP (Behavioral Calibration Prompting)**: Prompt-level injection of target behavioral rates
- **DPO (Direct Preference Optimization)**: Training-level alignment using dialect-calibrated preference pairs

**Finding**: Both strategies fail systematically. We document **the first taxonomy of calibration failure modes** for LLM user simulators, identifying four distinct mechanisms that explain why seemingly reasonable calibration interventions produce counterproductive outcomes.

**Framing**: This is NOT "we tried and failed." This is a systematic empirical analysis that (1) identifies previously undocumented failure mechanisms, (2) connects them to known phenomena in persona prompting and alignment, and (3) provides actionable constraints for future calibration research.

---

## Core Claims

### C1: BCP produces three systematic failure mechanisms
**Evidence strength**: Moderate (single model, single run, n=19-20 per variant)

| Failure Mode | Description | Key Metric | exp_id |
|---|---|---|---|
| FM1: Global Behavior Suppression | BCP calibration prompts collapse task completion regardless of target dimension | completion retention 52.3% (threshold ≥80%) | mvp-004 |
| FM2: Cross-Dimension Interference | Targeting one behavioral dimension perturbs non-targeted dimensions | politeness -25.6% when targeting question_rate; question_rate -52.3% when targeting politeness | mvp-004 |
| FM3: Overcorrection Rebound | Requesting extreme behavioral shift causes model to rebound in opposite direction | overcorrected politeness +4.2pp ~ +10.4pp above baseline (4 runs, 4/4 consistent) | hgate-dpo003-merged |

**Supporting numbers (mvp-004, Qwen2.5-7B-Instruct, n=19-20)**:
- FM1: aave completion 0.100 vs baseline 0.368 (-72.8%); indian 0.150 (-59.2%); mean calibrated 0.193
- FM2: single_dim_question politeness drops 25.6% (non-target); single_dim_politeness question_rate drops 52.3% (non-target)
  - **Base rate caveat**: question_rate baseline = 0.044 (~0.8 questions/task); 52.3% drop = absolute change from ~0.044 to ~0.021. Paper must report both absolute values and relative changes.
- FM3: **[primary]** hgate-dpo003-merged overcorrected politeness mean 0.574 vs baseline 0.502, gap +7.2pp (+14.3% relative), range +4.2pp ~ +10.4pp, 4/4 runs consistent; **[auxiliary]** mvp-004 single run: 0.605 vs 0.559 (+4.6pp, +8.2% relative)

**External support**:
- FM1: basil2025playing_pretend (persona prompting drops MMLU 71.6%→66.3%); hu2026expert_persona (accuracy degradation up to 30pp under persona)
- FM2: gupta2026intra_fairness (bias spillover effect in targeted alignment)
- FM3: no direct external parallel — novel observation

### C2: DPO+BCP interaction produces calibration reversal
**Evidence strength**: Strong (single model, 4 runs × 20 tasks = 80 episodes)

DPO training, despite learning effectively (acc 0.75-1.0, loss 0.653), reverses BCP calibration direction when combined:

| Metric | Base BCP (mvp-004) | DPO+BCP (hgate-dpo003-merged) |
|---|---|---|
| AAVE politeness gap | -0.091 (correct direction) | +0.064 (**reversed**) |
| Indian politeness gap | -0.099 (correct direction) | +0.063 (**reversed**) |
| H2 gap reduction | 25-28% (close to 30% threshold) | **-10.3%** (wrong direction) |
| Variant×run checks with gap expansion | — | **10/12** |
| Overcorrection rebound | +8.2% | **+14.3%** (amplified) |

**Key insight**: DPO-003 training *improved* tool-calling ability (merged completion 60% vs base 40%, diag-lora-merge). The reversal is not a DPO training failure — it's an **interaction effect** between DPO alignment and BCP prompting.

**External support**: lee2024dpo_toxicity (DPO bypasses rather than removes capabilities; alignment is fragile and reversible)

### C3: Scale-dependent failure severity
**Evidence strength**: Strong (two scales, 4 runs × 20 tasks = 80 episodes each)

BCP fails at both 7B and 14B, but the **failure mode** changes with scale:

| Failure Mode | 7B (mvp-004 / hgate-dpo003-merged) | 14B (qwen14b-bcp-001) |
|---|---|---|
| FM1: Completion collapse | ✅ (aave 0.100, indian 0.150) | ❌ Not replicated (H3 4/4 PASS, all variants >80% baseline) |
| FM2: Cross-dim interference | ✅ (pol -25.6%, qrate -52.3%) | ⚠️ Partial (H2 3/4 FAIL — insufficient calibration, not destructive) |
| FM3: Overcorrection rebound | ✅ (+7.2pp, 4/4 runs) | ❌ Not replicated (0/4 runs; overcorrected pol consistently BELOW baseline) |
| BCP overall effectiveness | ❌ Fails | ❌ Fails |

**Key insight**: BCP is ineffective at both scales, but the **failure mode transitions** with scale:
- **7B = "catastrophic over-response"**: BCP prompts overwhelm the model's limited capacity, collapsing task completion (FM1) and triggering overcorrection rebounds (FM3)
- **14B = "selective ignoring"**: The model maintains normal behavior (H3 PASS, high completion) but simply does not respond to calibration instructions (H2 FAIL)

This reveals a **safety-efficacy gap**: scaling resolves BCP's destructive side effects but not its calibration ineffectiveness. There is no "sweet spot" scale where BCP works — smaller models are harmed by it, larger models ignore it.

**14B specifics** (qwen14b-bcp-001, Qwen2.5-14B-Instruct FP16 TP=2, 4 runs × 20 tasks):
- Mean completion: 61.6% (vs 7B 36.8%, +67%)
- H1: 4/4 ✅ | H2: 1/4 ❌ (Run 2 pass due to anomalously high baseline 0.588) | H3: 4/4 ✅
- Per-run completion: 73.7% / 55.0% / 57.9% / 60.0%
- Mean politeness: 0.523 (vs 7B 0.559)

**Auxiliary evidence**:
- Llama-3-8B (llama-bcp-001): Floor effect (completion=5%). Tool-calling too weak to isolate BCP effect.
- Mistral-7B (mistral-bcp-001): completion=0%. No usable data.

### C4: Implications for future calibration research
**Evidence strength**: Analytical (grounded in C1-C3)

- **Implication 1**: Prompt-based calibration of behavioral rates in multi-turn agent dialogue faces a scale-dependent completion-calibration trade-off (FM1). At smaller scales (7B), BCP is destructive — it collapses task completion. At larger scales (14B), this harm disappears but calibration remains ineffective. This parallels the persona-accuracy trade-off (basil2025playing_pretend; hu2026expert_persona) but adds a scale dimension: larger models resist perturbation but aren't thereby calibrated.
- **Implication 2**: Behavioral dimensions are coupled — calibrating politeness rate without affecting question rate (or completion) requires methods that can disentangle dimensions (FM2). Possible direction: per-dimension reward models or constrained decoding (cf. khan2026decoding).
- **Implication 3**: DPO alignment and prompt-based calibration can interact adversarially (FM4). Future work must evaluate calibration methods in combination, not in isolation.
- **Implication 4**: Overcorrection rebound (FM3) at 7B suggests smaller models have an "attractor basin" for default behavioral rates that resists large perturbations. At 14B this rebound disappears — but calibration still fails (FM2 persists). Gradual/iterative calibration may outperform one-shot extreme targets, but the 14B result suggests the problem is deeper than perturbation magnitude.
- **Implication 5** (NEW): Scale-dependent failure severity implies that "BCP works at scale" is a misleading conclusion — while destructive side effects vanish, calibration efficacy does not improve. Future calibration methods cannot assume scaling alone will solve the problem.

---

## Reviewer Concerns (Pre-empted Attack Surfaces)

### RC1: "Single model — how do we know this generalizes?"
**Status**: Substantially mitigated (cross-scale, single model family)
- Qwen 7B + 14B cross-scale evidence: BCP fails at both scales (different severity profiles)
- Cross-scale data adds a contribution dimension (scale-dependent failure taxonomy) rather than just "replication"
- Llama-3-8B/Mistral-7B failed due to tool-calling limitations, NOT because BCP worked on them
- FM1 aligns with persona-accuracy trade-off documented across GPT-4, Claude, Llama in basil2025playing_pretend and hu2026expert_persona
- **Remaining limitation**: Single model family (Qwen2.5). Cross-family generalization (e.g., Llama, Mistral with sufficient tool-calling) remains future work. Explicitly acknowledged in limitations.
- **Honest hedge**: "We document BCP failure across two model scales within the Qwen2.5 family; the scale-dependent pattern of failure severity is itself a finding, but cross-family verification requires models with sufficient tool-calling ability in 16-tool settings."

### RC2: "n=20 tasks, high variance — statistical power?"
**Response**:
- BCP results (mvp-004): n=19-20 per variant, single run. Variance is a valid concern for absolute numbers.
- DPO+BCP results (hgate-dpo003-merged): 4 independent runs × 20 tasks = 80 episodes. Reversal effect consistent across 10/12 variant×run checks — this is not a variance artifact.
- FM3 (rebound): consistent direction in 4/4 runs for overcorrected variant.
- **Mitigation**: Report all individual run data (no cherry-picking, per memory.md rule). Frame claims around direction and consistency, not precise magnitudes.

### RC3: "This is just negative results — where's the contribution?"
**Response**:
- Negative-results papers exist at top venues (e.g., Findings track). But this is MORE than negative results:
  1. **Taxonomy**: First systematic categorization of calibration failure modes (FM1-FM4)
  2. **Mechanistic connections**: Link FM1→persona-accuracy trade-off, FM2→bias spillover, FM4→DPO bypass
  3. **Actionable implications**: Concrete constraints for future calibration methods
  4. **Interaction discovery**: FM4 (DPO+BCP reversal) is novel — no prior work documents this interaction

### RC4: "Why not try other calibration methods?"
**Response**:
- BCP and DPO represent the two main paradigms (prompt-time vs training-time). Covering both provides good coverage.
- Paper scope is diagnosis (failure taxonomy), not exhaustive method search.
- Implications section points to alternative approaches (constrained decoding, per-dimension reward, iterative calibration).

### RC5: "The evaluation framework (tau-bench) is a confound — maybe BCP works on simpler tasks?"
**Response**:
- tau-bench is the standard benchmark for tool-calling agent evaluation (yao2024taubench; sim2real2026gap uses it too).
- FM1 parallels persona-accuracy trade-off found on MMLU/general benchmarks — not tau-bench specific.
- But fairly: FM2 and FM3 may be task-dependent. Acknowledged in limitations.

---

## Evidence Map

| Claim | Sub-claim | Primary Experiment | Metric | Value | Secondary Experiment |
|---|---|---|---|---|---|
| C1 | FM1: completion collapse | mvp-004 | mean completion retention | 52.3% (need ≥80%) | hgate-dpo003-merged (excl. run2: 47-51% drop) |
| C1 | FM2: cross-dim interference | mvp-004 | non-target dim shift | politeness -25.6%, qrate -52.3% | — |
| C1 | FM3: overcorrection rebound | hgate-dpo003-merged | overcorrected pol vs baseline | +7.2pp mean (+14.3% rel), 4/4 runs consistent | mvp-004 (+4.6pp, single run) |
| C2 | FM4: DPO reversal of BCP | hgate-dpo003-merged | H2 gap reduction | -10.3% (wrong direction) | — |
| C2 | FM4: gap expansion count | hgate-dpo003-merged | variant×run checks | 10/12 expanded | — |
| C2 | DPO training effective | dpo-003 | rewards accuracy | 0.75-1.0 | diag-lora-merge (merged 60% vs base 40%) |
| C2 | Direction comparison | mvp-004 vs hgate-dpo003-merged | AAVE pol gap | -0.091 → +0.064 | Indian: -0.099 → +0.063 |
| C3 | Scale-dependent severity | qwen14b-bcp-001 | FM1 replication | ❌ (H3 4/4 PASS at 14B) | mvp-004 (FM1 confirmed at 7B) |
| C3 | Scale-dependent severity | qwen14b-bcp-001 | FM3 replication | ❌ (0/4 runs rebound at 14B) | hgate-dpo003-merged (4/4 at 7B) |
| C3 | BCP ineffective both scales | qwen14b-bcp-001 | H2 pass rate | 1/4 (14B) vs 0/1 (7B) | Both fail calibration |
| C3 | Completion improvement | qwen14b-bcp-001 | baseline completion | 61.6% (14B) vs 36.8% (7B) | +67% from scaling |
| C3 | Cross-model (auxiliary) | llama-bcp-001 | completion | 5% (floor) | Not usable for generalization |

---

## Contribution Statement

We present the first systematic taxonomy of calibration failure modes for LLM user simulators in agentic evaluation. Through controlled experiments on Qwen2.5-7B and Qwen2.5-14B in the tau-bench retail domain, we identify four failure mechanisms — global behavior suppression, cross-dimension interference, overcorrection rebound, and DPO-BCP interaction reversal — and reveal that their severity is **scale-dependent**: destructive side effects (completion collapse, overcorrection rebound) disappear at 14B, but calibration itself remains ineffective. This safety-efficacy gap shows that scaling resolves BCP's harms without solving its core limitation. Our findings establish concrete constraints for future calibration research and connect observed failures to broader phenomena in persona prompting and preference optimization.

---

## Key Literature Anchors

| Role in Paper | Paper | What It Provides |
|---|---|---|
| Core motivation | sim2real2026gap (arXiv 2603.11245) | Quantifies sim-vs-human gap in τ-bench; diagnoses the problem we attempt to solve |
| FM1 mechanism | basil2025playing_pretend (arXiv 2512.05858) | Persona prompting degrades accuracy; explains completion collapse |
| FM1 mechanism | hu2026expert_persona (arXiv 2603.18507) | Persona-accuracy trade-off up to 30pp; instruction-tuned models more susceptible |
| FM2 mechanism | gupta2026intra_fairness (arXiv 2602.16438) | Bias spillover in targeted alignment; parallel to cross-dim interference |
| FM4 mechanism | lee2024dpo_toxicity (ICML 2024) | DPO bypasses rather than removes capabilities; fragile alignment |
| Evaluation framework | yao2024taubench (arXiv 2406.12045) | τ-bench retail domain, pass^k metric |
| Bias context | seshadri2026lost (arXiv 2601.17087) | AAVE/Indian English speakers get worst simulator calibration |
| DPO method | rafailov2023dpo (NeurIPS 2023) | Core DPO algorithm reference |

---

## Open Items

- [x] **qwen14b-bcp-001 results** — C3 updated: scale-dependent failure severity (FM1/FM3 capacity-dependent, FM2 partial, BCP ineffective at both scales). D014.
- [ ] **Statistical tests** — add bootstrap CI for key comparisons (FM4 reversal direction, FM3 rebound magnitude, 7B-vs-14B completion difference) once data is finalized.
- [ ] **Figure plan** — taxonomy diagram (FM1-FM4), gap reversal visualization (base vs DPO politeness gaps), **scale-dependent severity heatmap** (7B vs 14B × FM1-FM3).
- [ ] **14B DPO (optional)** — would FM4 (DPO+BCP reversal) also show scale-dependent behavior? ~11-13h GPU. Contingent on new server GPU availability.
- [ ] **C1 annotation** — add note that FM1 and FM3 are documented at 7B; 14B evidence shows these are capacity-dependent. Paper must not overclaim "structural" for FM1/FM3.
