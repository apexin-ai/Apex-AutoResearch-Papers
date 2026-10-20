# Outline A: Metric-Dependent Collapse (K=16 also no semantic collapse)

## Title Candidates

1. "Does Reward Curation Kill Diversity? It Depends on What You Measure"
2. "Semantic Resilience, Format Collapse: Metric-Dependent Diversity Loss in Iterative Reward Curation"
3. "The Collapse That Standard Metrics Miss: Format Homogenization in Iterative Best-of-K Selection"

## Abstract (core 3 sentences)

Iterative reward curation, where the highest-scored output among K candidates is selected for retraining, is widely assumed to cause progressive diversity collapse. We systematically test this across 7 training configurations over 3 generations and find the answer is metric-dependent: semantic diversity (embedding-based Vendi Score) remains resilient across all conditions (max change: -0.27%), while format diversity (opening patterns, template structure) collapses significantly, with near-duplicate opening rates rising from 50% to 84% under curation. This reveals that diversity collapse under reward curation is real but mischaracterized by standard metrics, and we propose complementary format-level measurements to capture the overlooked homogenization mode.

## Sections + Key Points

### 1. Introduction
- Iterative curation is increasingly common (RLHF pipelines, self-play, synthetic data loops)
- Diversity collapse is a stated concern in DIVE, DARLING, CD-RLHF, GEM, Kirk et al.
- No systematic study isolating curation pressure from other collapse sources (mode-seeking RL, KL penalty absence)
- We conduct controlled experiments: pure best-of-K SFT loop, no RL, no KL
- Core finding: collapse does not occur under standard small-scale conditions
- Implications: the field may be solving a problem that doesn't exist in this regime

### 2. Related Work
- **Diversity in RLHF**: Kirk et al. (ICLR'24) taxonomy, DIVE iterative DPO, DARLING decoding
- **Reward-based selection**: Best-of-N sampling literature, ArmoRM, reward model diversity
- **Synthetic data loops**: self-improvement cycles, data contamination vs. collapse
- **Negative results in NLP**: positioning within empirical study tradition

### 3. Method
- **Pipeline**: Generate K candidates per prompt → ArmoRM score → select top-1 → SFT on selected → repeat
- **Conditions**: 2 architectures (LoRA r=16, Full-FT) × 3 K values (4, 8, 16) × LR variants
- **Baselines**: No-curation control (random selection from K candidates for SFT)
- **Metrics**: Vendi Score (embedding diversity), reward score (quality), pairwise similarity, training loss
- **Scale**: Qwen3-0.6B, 2200 prompts from UltraFeedback, 3 iterative generations
- **CARR dry-run**: Mann-Whitney U rebalancing with text heuristic proxies as supplementary analysis

### 4. Results
- **No collapse across all conditions**: Vendi Score changes within ±1% of baseline drift
  - LoRA K=4: -0.27% vs baseline +3.13%
  - LoRA K=8: +0.04%
  - Full-FT K=4 lr=5e-6: +0.91% vs baseline +1.37%
  - Full-FT K=4 lr=2e-5: +0.68%
  - K=16: [still within normal range]
- **Quality stable**: all conditions ±1% reward score
- **Training loss monotonically decreasing**: models learn the curated distribution, but it doesn't narrow
- **Direction reversal**: curation effect flips from suppression to facilitation as capacity increases:
    - LoRA: -3.40pp | Full-FT lr=5e-6: -0.46pp | Full-FT lr=2e-5: **+0.63pp**
  - **LoRA artifact**: LoRA baseline shows +3.13% diversity growth vs Full-FT +1.37%, independent of curation

### 5. Analysis
- **Why no collapse?** Hypotheses: (a) K≤16 retention rate (6.25-25%) insufficient selection pressure; (b) prompt diversity maintains output diversity; (c) reward model doesn't concentrate probability mass
- **LoRA artifact investigation**: regularization effect of low-rank constraint preserves diversity
- **CARR proxy covariance**: text heuristic proxies (length, vocab richness, structure) correlate r=0.63-0.77 with reward, 99.3% selection overlap with ArmoRM alone, indicating multi-objective rebalancing adds nothing in this regime
- **Comparison to prior claims**: reconciling with DIVE/Kirk et al. findings (different mechanisms: RL vs. SFT, KL-free vs. KL-constrained)

### 6. Discussion
- **Scope limitations**: sub-1B model, <5K prompts, ≤16 candidates, ≤3 generations
- **When might collapse occur?** Extreme K, many more generations, stronger reward models, narrower prompt sets
- **Practical implications**: practitioners need not add diversity interventions for standard curation pipelines at this scale
- **Relation to mode collapse in RL**: iterative SFT on curated data ≠ reward maximization via policy gradient

### 7. Conclusion
- Under standard small-scale conditions, iterative reward curation does not cause diversity collapse
- The community should distinguish curation-induced collapse from RL-induced collapse
- Future work: scaling K, generations, model size to find actual boundary

## Contributions

1. [CONFIRMED] **Systematic empirical study**: semantic diversity resilient under iterative reward curation (7 configs × 3 gens, sub-1B, <5K prompts, K≤16, ≤3 gens)
2. [CONFIRMED] **Metric-dependent collapse**: format/template diversity collapses (opening unique 70%→37%, near-dup 50%→84%) while Vendi Score stays flat — collapse is real but mischaracterized
3. [CONFIRMED] **Direction reversal**: curation effect flips from suppression (-3.4pp under LoRA) to facilitation (+0.63pp under aggressive Full-FT)
4. [CONFIRMED] **Measurement contribution**: opening_entropy + near_duplicate_start_rate as complementary metrics for format homogenization
5. [DEPENDS ON K=16] **Boundary condition**: K=16 behavior (strengthens the finding or reveals semantic collapse threshold)

## Tables/Figures

| ID | Type | Content | Purpose |
|----|------|---------|---------|
| Fig 1 | Line plot | Vendi Score across 3 generations, all 6 conditions + baselines | Core result: no collapse trajectory |
| Fig 2 | Diagram | Pipeline overview (generate → score → select → SFT → repeat) | Method clarity |
| Table 1 | Results | Full metrics: Vendi, reward, pairwise sim, per condition per generation | Complete numerical evidence |
| Table 2 | Comparison | Our conditions vs. prior work settings (model size, K, generations, RL vs SFT) | Scope positioning |
| Fig 3 | Bar chart | LoRA vs Full-FT baseline diversity drift | LoRA artifact evidence |
| Fig 4 | Scatter/heatmap | CARR proxy correlations + selection overlap | Proxy covariance finding |
| Table 3 | Taxonomy | Sources of collapse: curation / RL / KL / data, with literature pointers | Conceptual contribution |

---

# Outline B: Boundary Finding (K=16 triggers collapse)

## Title Candidates

1. "The Collapse Threshold: Iterative Reward Curation Triggers Diversity Loss Only Under Extreme Selection Pressure"
2. "When Does Best-of-K Curation Break Diversity? Identifying the Selection Pressure Boundary"
3. "Safe Curation: Diversity Collapse Requires K≥16 in Iterative Reward Selection"

## Abstract (core 3 sentences)

Iterative reward curation is assumed to progressively erode output diversity, yet the conditions under which collapse occurs and what dimensions it affects remain uncharacterized. Through systematic experiments across 7 configurations over 3 generations, we find collapse is both threshold-dependent and metric-dependent: semantic diversity (Vendi Score) collapses only at K=16 (retention 6.25%), while format diversity (opening patterns) degrades at all curation levels, with near-duplicate start rates rising from 50% to 84%. This dual characterization provides actionable guidance: standard embedding metrics miss format collapse entirely, and practitioners need both threshold awareness (K≤8 is semantically safe) and format-level monitoring.

## Sections + Key Points

### 1. Introduction
- Iterative curation ubiquitous in modern alignment pipelines
- Diversity collapse concern motivates complex interventions (DIVE, DARLING, CD-RLHF, GEM)
- Missing: characterization of WHEN collapse actually occurs
- Key insight: collapse is not gradual, it has a threshold tied to selection pressure (retention rate)
- Our contribution: identify boundary at K=16 / 6.25% retention, below which standard curation is safe
- Practical value: tells practitioners exactly when to worry (and when not to)

### 2. Related Work
- **Diversity preservation methods**: DIVE, DARLING, CD-RLHF, GEM (all assume collapse is default)
- **Selection pressure in evolutionary computation**: tournament size, truncation selection, parallels to best-of-K
- **Kirk et al.**: diversity taxonomy, but no systematic threshold study
- **Reward model properties**: ArmoRM, concentration of reward mass

### 3. Method
- **Pipeline**: identical to Outline A
- **Conditions**: designed to sweep selection pressure: K=4 (25%), K=8 (12.5%), K=16 (6.25%)
- **Architecture axis**: LoRA vs Full-FT (controls for regularization confound)
- **Metrics**: Vendi Score, reward score, generation-over-generation diversity delta, pairwise cosine similarity distribution
- **Threshold detection**: operationalize "collapse" as Vendi Score drop > X% sustained across generations
- **CARR dry-run**: test whether multi-objective rebalancing can prevent collapse at K=16

### 4. Results

#### 4.1 Safe regime (K≤8): No collapse
- LoRA K=4: Vendi -0.27% (within baseline noise of +3.13%)
- LoRA K=8: Vendi +0.04%
- Full-FT K=4: +0.68% to +0.91%
- Quality stable (±1%), training loss decreasing

#### 4.2 Collapse regime (K=16): Diversity breaks
- Full-FT K=16 lr=2e-5: Vendi drops [X]% by generation 3
- Pairwise similarity increases, distribution narrows
- Quality initially improves then plateaus (reward hacking signature)
- Training loss still decreases (model converges to narrow mode)

#### 4.3 Boundary characterization
- Sharp transition between K=8 (safe) and K=16 (collapse)
- Not gradual: K=4 and K=8 nearly identical, K=16 qualitatively different
- Retention rate 6.25% as critical threshold

#### 4.4 Supplementary findings
- LoRA artifact: +3.13% baseline drift suggests LoRA regularization preserves diversity
- CARR proxy covariance: r=0.63-0.77, 99.3% overlap, rebalancing cannot rescue K=16 collapse because proxies align with reward

### 5. Analysis
- **Why the threshold?** At K≤8, prompt-level diversity dominates selection pressure; at K=16, selection pressure overwhelms prompt diversity
- **LoRA as implicit diversity preservation**: low-rank constraint limits how far model can drift per iteration
- **Why CARR fails at the boundary**: when text proxies covary with reward (r=0.63-0.77), rebalancing selects the same outputs (99.3% overlap), so it cannot counteract extreme selection pressure
- **Evolutionary analogy**: K maps to tournament size; known phase transition in evolutionary computation at high tournament pressure

### 6. Practical Guidelines
- **Safe curation**: K≤8 (retention ≥12.5%) requires no diversity intervention at sub-1B scale
- **Danger zone**: K≥16 (retention ≤6.25%) requires explicit diversity mechanisms
- **Architecture choice**: LoRA provides implicit diversity buffer vs Full-FT
- **Proxy-based rebalancing insufficient**: when proxies correlate with reward, they cannot independently preserve diversity
- **Recommendations for scaling**: expected threshold may shift with model size, prompt diversity, generation count

### 7. Discussion
- **Scope**: sub-1B model, <5K prompts, ≤3 generations; threshold may differ at larger scale
- **Implications for existing methods**: DIVE/DARLING/CD-RLHF may be solving a problem only relevant at extreme K or many generations
- **Open questions**: does threshold shift with model capacity? With prompt set size? With number of generations?

### 8. Conclusion
- Diversity collapse under iterative curation is not a default outcome but a threshold phenomenon
- Boundary at K=16 / 6.25% retention provides actionable guidance
- Standard pipelines (K≤8) are safe; extreme selection requires intervention

## Contributions

1. [DEPENDS ON K=16] **Semantic collapse boundary**: Vendi Score loss occurs only at K≥16 (retention ≤6.25%), establishing a sharp threshold
2. [CONFIRMED] **Metric-dependent collapse**: format/template diversity collapses at ALL curation levels (opening unique 70%→37%, near-dup 50%→84%), undetected by Vendi Score
3. [CONFIRMED] **Direction reversal**: curation suppresses (-3.4pp) under LoRA but facilitates (+0.63pp) under aggressive Full-FT
4. [CONFIRMED] **Measurement contribution**: opening_entropy + near_duplicate_start_rate capture format homogenization that embedding metrics miss
5. [CONFIRMED] **CARR failure mode**: proxy-based rebalancing fails (r=0.63-0.77 covariance), cannot rescue format or semantic collapse

## Tables/Figures

| ID | Type | Content | Purpose |
|----|------|---------|---------|
| Fig 1 | Line plot | Vendi Score across generations: K=4, K=8 flat; K=16 drops | Core boundary visualization |
| Fig 2 | Diagram | Pipeline + selection pressure illustration (K→retention rate) | Method + intuition |
| Table 1 | Results | Full metrics per condition per generation | Complete evidence |
| Fig 3 | Phase diagram | Selection pressure (K) vs diversity change, with threshold marked | Boundary characterization |
| Fig 4 | Distribution plot | Pairwise similarity distributions: K=8 vs K=16 at gen 3 | Collapse mechanism |
| Table 2 | Guidelines | K value → retention → collapse risk → recommended intervention | Practical contribution |
| Fig 5 | Bar chart | LoRA vs Full-FT diversity trajectories | Regularization finding |
| Fig 6 | Correlation matrix | CARR proxy scores vs ArmoRM reward | Proxy covariance evidence |
| Table 3 | Comparison | Our threshold vs. prior work assumptions | Positioning |
