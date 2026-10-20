# analysis paper outline ab variants

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 5
- **Recorded user turns:** 0
- **Tool calls:** 2
- **Original source:** `logs/chats/worker_analysis_paper_outline_ab_variants_20260517T035337.jsonl`
- **Structured JSON:** [`6457560827e791a817db.json`](../../sessions/64/6457560827e791a817db.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

5 recorded events

### Tool call

_source line 1 · 2026-05-17T03:55:34.888607+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/collapse_aware_reward_rebalancing/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_outline_ab_variants_20260517T035337",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/collapse_aware_reward_rebalancing/artifacts/",
    "description": "List artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-17T03:55:34.888961+00:00_

analysis_carr_fullft_lr2e5_nocuration_01.md
carr_dryrun_feasibility_report.md
carr_fullft_lr2e5_probe_01_metrics.json
collapse_signal_report.json
collapse_signal_summary.md
experiment_data_table.md
paper_outline_d.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_outline_ab_variants_20260517T035337",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T03:55:34.889169+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/collapse_aware_reward_rebalancing/artifacts/paper_outline_ab.md",
  "content": "# Outline A: Pure Negative Result (K=16 also fails to collapse)\n\n## Title Candidates\n\n1. \"Does Iterative Reward Curation Kill Diversity? A Systematic Negative Finding\"\n2. \"The Resilience of Output Diversity Under Iterative Best-of-K Selection\"\n3. \"No Collapse: Diversity Persists Through Iterative Reward-Based Curation\"\n\n## Abstract (core 3 sentences)\n\nIterative reward curation, where the highest-scored output among K candidates is selected for retraining, is widely assumed to cause progressive diversity collapse. We systematically test this assumption across 6 conditions (K=4/8/16, LoRA/Full-FT, varying learning rates) over 3 generations on Qwen3-0.6B with 2200 UltraFeedback prompts, measuring Vendi Score diversity, quality, and distributional shift. Contrary to expectation, no condition produces meaningful diversity loss (max Vendi change: -0.27%), while training loss decreases monotonically, revealing that standard small-scale iterative curation reshapes style without collapsing the output distribution.\n\n## Sections + Key Points\n\n### 1. Introduction\n- Iterative curation is increasingly common (RLHF pipelines, self-play, synthetic data loops)\n- Diversity collapse is a stated concern in DIVE, DARLING, CD-RLHF, GEM, Kirk et al.\n- No systematic study isolating curation pressure from other collapse sources (mode-seeking RL, KL penalty absence)\n- We conduct controlled experiments: pure best-of-K SFT loop, no RL, no KL\n- Core finding: collapse does not occur under standard small-scale conditions\n- Implications: the field may be solving a problem that doesn't exist in this regime\n\n### 2. Related Work\n- **Diversity in RLHF**: Kirk et al. (ICLR'24) taxonomy, DIVE iterative DPO, DARLING decoding\n- **Reward-based selection**: Best-of-N sampling literature, ArmoRM, reward model diversity\n- **Synthetic data loops**: self-improvement cycles, data contamination vs. collapse\n- **Negative results in NLP**: positioning within empirical study tradition\n\n### 3. Method\n- **Pipeline**: Generate K candidates per prompt → ArmoRM score → select top-1 → SFT on selected → repeat\n- **Conditions**: 2 architectures (LoRA r=16, Full-FT) × 3 K values (4, 8, 16) × LR variants\n- **Baselines**: No-curation control (random selection from K candidates for SFT)\n- **Metrics**: Vendi Score (embedding diversity), reward score (quality), pairwise similarity, training loss\n- **Scale**: Qwen3-0.6B, 2200 prompts from UltraFeedback, 3 iterative generations\n- **CARR dry-run**: Mann-Whitney U rebalancing with text heuristic proxies as supplementary analysis\n\n### 4. Results\n- **No collapse across all conditions**: Vendi Score changes within ±1% of baseline drift\n  - LoRA K=4: -0.27% vs baseline +3.13%\n  - LoRA K=8: +0.04%\n  - Full-FT K=4 lr=5e-6: +0.91% vs baseline +1.37%\n  - Full-FT K=4 lr=2e-5: +0.68%\n  - K=16: [still within normal range]\n- **Quality stable**: all conditions ±1% reward score\n- **Training loss monotonically decreasing**: models learn the curated distribution, but it doesn't narrow\n- **LoRA artifact**: LoRA baseline shows +3.13% diversity growth vs Full-FT +1.37%, independent of curation\n\n### 5. Analysis\n- **Why no collapse?** Hypotheses: (a) K≤16 retention rate (6.25-25%) insufficient selection pressure; (b) prompt diversity maintains output diversity; (c) reward model doesn't concentrate probability mass\n- **LoRA artifact investigation**: regularization effect of low-rank constraint preserves diversity\n- **CARR proxy covariance**: text heuristic proxies (length, vocab richness, structure) correlate r=0.63-0.77 with reward, 99.3% selection overlap with ArmoRM alone, indicating multi-objective rebalancing adds nothing in this regime\n- **Comparison to prior claims**: reconciling with DIVE/Kirk et al. findings (different mechanisms: RL vs. SFT, KL-free vs. KL-constrained)\n\n### 6. Discussion\n- **Scope limitations**: sub-1B model, <5K prompts, ≤16 candidates, ≤3 generations\n- **When might collapse occur?** Extreme K, many more generations, stronger reward models, narrower prompt sets\n- **Practical implications**: practitioners need not add diversity interventions for standard curation pipelines at this scale\n- **Relation to mode collapse in RL**: iterative SFT on curated data ≠ reward maximization via policy gradient\n\n### 7. Conclusion\n- Under standard small-scale conditions, iterative reward curation does not cause diversity collapse\n- The community should distinguish curation-induced collapse from RL-induced collapse\n- Future work: scaling K, generations, model size to find actual boundary\n\n## Contributions\n\n1. **Systematic empirical study** of diversity under iterative reward curation across 6 conditions × 3 generations (under standard small-scale conditions: sub-1B, <5K prompts, K≤16)\n2. **Negative finding with practical value**: no diversity intervention needed for standard curation pipelines at this scale, contra assumptions in DIVE/DARLING/CD-RLHF\n3. **LoRA diversity artifact**: LoRA training inflates measured diversity vs Full-FT independent of curation, a confound for future diversity studies\n4. **Taxonomy of collapse sources**: distinguishing curation pressure from RL mode-seeking, KL divergence, and data homogeneity as independent collapse mechanisms\n\n## Tables/Figures\n\n| ID | Type | Content | Purpose |\n|----|------|---------|---------|\n| Fig 1 | Line plot | Vendi Score across 3 generations, all 6 conditions + baselines | Core result: no collapse trajectory |\n| Fig 2 | Diagram | Pipeline overview (generate → score → select → SFT → repeat) | Method clarity |\n| Table 1 | Results | Full metrics: Vendi, reward, pairwise sim, per condition per generation | Complete numerical evidence |\n| Table 2 | Comparison | Our conditions vs. prior work settings (model size, K, generations, RL vs SFT) | Scope positioning |\n| Fig 3 | Bar chart | LoRA vs Full-FT baseline diversity drift | LoRA artifact evidence |\n| Fig 4 | Scatter/heatmap | CARR proxy correlations + selection overlap | Proxy covariance finding |\n| Table 3 | Taxonomy | Sources of collapse: curation / RL / KL / data, with literature pointers | Conceptual contribution |\n\n---\n\n# Outline B: Boundary Finding (K=16 triggers collapse)\n\n## Title Candidates\n\n1. \"The Collapse Threshold: Iterative Reward Curation Triggers Diversity Loss Only Under Extreme Selection Pressure\"\n2. \"When Does Best-of-K Curation Break Diversity? Identifying the Selection Pressure Boundary\"\n3. \"Safe Curation: Diversity Collapse Requires K≥16 in Iterative Reward Selection\"\n\n## Abstract (core 3 sentences)\n\nIterative reward curation is assumed to progressively erode output diversity, yet the conditions under which collapse actually occurs remain uncharacterized. Through systematic experiments across 6 conditions (K=4/8/16, LoRA/Full-FT) over 3 generations, we identify a sharp boundary: diversity remains stable for K≤8 (retention ≥12.5%) but collapses at K=16 (retention 6.25%), establishing that standard curation is safe while extreme selection pressure is not. This boundary provides a practical guideline: practitioners can safely use best-of-K curation with K≤8 without diversity interventions, while K≥16 requires explicit diversity preservation mechanisms.\n\n## Sections + Key Points\n\n### 1. Introduction\n- Iterative curation ubiquitous in modern alignment pipelines\n- Diversity collapse concern motivates complex interventions (DIVE, DARLING, CD-RLHF, GEM)\n- Missing: characterization of WHEN collapse actually occurs\n- Key insight: collapse is not gradual, it has a threshold tied to selection pressure (retention rate)\n- Our contribution: identify boundary at K=16 / 6.25% retention, below which standard curation is safe\n- Practical value: tells practitioners exactly when to worry (and when not to)\n\n### 2. Related Work\n- **Diversity preservation methods**: DIVE, DARLING, CD-RLHF, GEM (all assume collapse is default)\n- **Selection pressure in evolutionary computation**: tournament size, truncation selection, parallels to best-of-K\n- **Kirk et al.**: diversity taxonomy, but no systematic threshold study\n- **Reward model properties**: ArmoRM, concentration of reward mass\n\n### 3. Method\n- **Pipeline**: identical to Outline A\n- **Conditions**: designed to sweep selection pressure: K=4 (25%), K=8 (12.5%), K=16 (6.25%)\n- **Architecture axis**: LoRA vs Full-FT (controls for regularization confound)\n- **Metrics**: Vendi Score, reward score, generation-over-generation diversity delta, pairwise cosine similarity distribution\n- **Threshold detection**: operationalize \"collapse\" as Vendi Score drop > X% sustained across generations\n- **CARR dry-run**: test whether multi-objective rebalancing can prevent collapse at K=16\n\n### 4. Results\n\n#### 4.1 Safe regime (K≤8): No collapse\n- LoRA K=4: Vendi -0.27% (within baseline noise of +3.13%)\n- LoRA K=8: Vendi +0.04%\n- Full-FT K=4: +0.68% to +0.91%\n- Quality stable (±1%), training loss decreasing\n\n#### 4.2 Collapse regime (K=16): Diversity breaks\n- Full-FT K=16 lr=2e-5: Vendi drops [X]% by generation 3\n- Pairwise similarity increases, distribution narrows\n- Quality initially improves then plateaus (reward hacking signature)\n- Training loss still decreases (model converges to narrow mode)\n\n#### 4.3 Boundary characterization\n- Sharp transition between K=8 (safe) and K=16 (collapse)\n- Not gradual: K=4 and K=8 nearly identical, K=16 qualitatively different\n- Retention rate 6.25% as critical threshold\n\n#### 4.4 Supplementary findings\n- LoRA artifact: +3.13% baseline drift suggests LoRA regularization preserves diversity\n- CARR proxy covariance: r=0.63-0.77, 99.3% overlap, rebalancing cannot rescue K=16 collapse because proxies align with reward\n\n### 5. Analysis\n- **Why the threshold?** At K≤8, prompt-level diversity dominates selection pressure; at K=16, selection pressure overwhelms prompt diversity\n- **LoRA as implicit diversity preservation**: low-rank constraint limits how far model can drift per iteration\n- **Why CARR fails at the boundary**: when text proxies covary with reward (r=0.63-0.77), rebalancing selects the same outputs (99.3% overlap), so it cannot counteract extreme selection pressure\n- **Evolutionary analogy**: K maps to tournament size; known phase transition in evolutionary computation at high tournament pressure\n\n### 6. Practical Guidelines\n- **Safe curation**: K≤8 (retention ≥12.5%) requires no diversity intervention at sub-1B scale\n- **Danger zone**: K≥16 (retention ≤6.25%) requires explicit diversity mechanisms\n- **Architecture choice**: LoRA provides implicit diversity buffer vs Full-FT\n- **Proxy-based rebalancing insufficient**: when proxies correlate with reward, they cannot independently preserve diversity\n- **Recommendations for scaling**: expected threshold may shift with model size, prompt diversity, generation count\n\n### 7. Discussion\n- **Scope**: sub-1B model, <5K prompts, ≤3 generations; threshold may differ at larger scale\n- **Implications for existing methods**: DIVE/DARLING/CD-RLHF may be solving a problem only relevant at extreme K or many generations\n- **Open questions**: does threshold shift with model capacity? With prompt set size? With number of generations?\n\n### 8. Conclusion\n- Diversity collapse under iterative curation is not a default outcome but a threshold phenomenon\n- Boundary at K=16 / 6.25% retention provides actionable guidance\n- Standard pipelines (K≤8) are safe; extreme selection requires intervention\n\n## Contributions\n\n1. **Collapse boundary identification**: diversity loss occurs at K≥16 (retention ≤6.25%) but not at K≤8, establishing a sharp threshold for iterative reward curation\n2. **Practical safety guideline**: standard best-of-K curation (K≤8) does not require diversity interventions at sub-1B scale with <5K prompts over ≤3 generations\n3. **Failure mode characterization**: at the boundary, proxy-based rebalancing (CARR) fails due to reward-proxy covariance (r=0.63-0.77), indicating that independent diversity signals are necessary\n4. **LoRA regularization effect**: LoRA training provides implicit diversity preservation vs Full-FT, relevant as a confound and as a practical mitigation\n\n## Tables/Figures\n\n| ID | Type | Content | Purpose |\n|----|------|---------|---------|\n| Fig 1 | Line plot | Vendi Score across generations: K=4, K=8 flat; K=16 drops | Core boundary visualization |\n| Fig 2 | Diagram | Pipeline + selection pressure illustration (K→retention rate) | Method + intuition |\n| Table 1 | Results | Full metrics per condition per generation | Complete evidence |\n| Fig 3 | Phase diagram | Selection pressure (K) vs diversity change, with threshold marked | Boundary characterization |\n| Fig 4 | Distribution plot | Pairwise similarity distributions: K=8 vs K=16 at gen 3 | Collapse mechanism |\n| Table 2 | Guidelines | K value → retention → collapse risk → recommended intervention | Practical contribution |\n| Fig 5 | Bar chart | LoRA vs Full-FT diversity trajectories | Regularization finding |\n| Fig 6 | Correlation matrix | CARR proxy scores vs ArmoRM reward | Proxy covariance evidence |\n| Table 3 | Comparison | Our threshold vs. prior work assumptions | Positioning |\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_outline_ab_variants_20260517T035337",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/collapse_aware_reward_rebalancing/artifacts/paper_outline_ab.md",
    "content": "# Outline A: Pure Negative Result (K=16 also fails to collapse)\n\n## Title Candidates\n\n1. \"Does Iterative Reward Curation Kill Diversity? A Systematic Negative Finding\"\n2. \"The Resilience of Output Diversity Under Iterative Best-of-K Selection\"\n3. \"No Collapse: Diversity Persists Through Iterative Reward-Based Curation\"\n\n## Abstract (core 3 sentences)\n\nIterative reward curation, where the highest-scored output among K candidates is selected for retraining, is widely assumed to cause progressive diversity collapse. We systematically test this assumption across 6 conditions (K=4/8/16, LoRA/Full-FT, varying learning rates) over 3 generations on Qwen3-0.6B with 2200 UltraFeedback prompts, measuring Vendi Score diversity, quality, and distributional shift. Contrary to expectation, no condition produces meaningful diversity loss (max Vendi change: -0.27%), while training loss decreases monotonically, revealing that standard small-scale iterative curation reshapes style without collapsing the output distribution.\n\n## Sections + Key Points\n\n### 1. Introduction\n- Iterative curation is increasingly common (RLHF pipelines, self-play, synthetic data loops)\n- Diversity collapse is a stated concern in DIVE, DARLING, CD-RLHF, GEM, Kirk et al.\n- No systematic study isolating curation pressure from other collapse sources (mode-seeking RL, KL penalty absence)\n- We conduct controlled experiments: pure best-of-K SFT loop, no RL, no KL\n- Core finding: collapse does not occur under standard small-scale conditions\n- Implications: the field may be solving a problem that doesn't exist in this regime\n\n### 2. Related Work\n- **Diversity in RLHF**: Kirk et al. (ICLR'24) taxonomy, DIVE iterative DPO, DARLING decoding\n- **Reward-based selection**: Best-of-N sampling literature, ArmoRM, reward model diversity\n- **Synthetic data loops**: self-improvement cycles, data contamination vs. collapse\n- **Negative results in NLP**: positioning within empirical study tradition\n\n### 3. Method\n- **Pipeline**: Generate K candidates per prompt → ArmoRM score → select top-1 → SFT on selected → repeat\n- **Conditions**: 2 architectures (LoRA r=16, Full-FT) × 3 K values (4, 8, 16) × LR variants\n- **Baselines**: No-curation control (random selection from K candidates for SFT)\n- **Metrics**: Vendi Score (embedding diversity), reward score (quality), pairwise similarity, training loss\n- **Scale**: Qwen3-0.6B, 2200 prompts from UltraFeedback, 3 iterative generations\n- **CARR dry-run**: Mann-Whitney U rebalancing with text heuristic proxies as supplementary analysis\n\n### 4. Results\n- **No collapse across all conditions**: Vendi Score changes within ±1% of baseline drift\n  - LoRA K=4: -0.27% vs baseline +3.13%\n  - LoRA K=8: +0.04%\n  - Full-FT K=4 lr=5e-6: +0.91% vs baseline +1.37%\n  - Full-FT K=4 lr=2e-5: +0.68%\n  - K=16: [still within normal range]\n- **Quality stable**: all conditions ±1% reward score\n- **Training loss monotonically decreasing**: models learn the curated distribution, but it doesn't narrow\n- **LoRA artifact**: LoRA baseline shows +3.13% diversity growth vs Full-FT +1.37%, independent of curation\n\n### 5. Analysis\n- **Why no collapse?** Hypotheses: (a) K≤16 retention rate (6.25-25%) insufficient selection pressure; (b) prompt diversity maintains output diversity; (c) reward model doesn't concentrate probability mass\n- **LoRA artifact investigation**: regularization effect of low-rank constraint preserves diversity\n- **CARR proxy covariance**: text heuristic proxies (length, vocab richness, structure) correlate r=0.63-0.77 with reward, 99.3% selection overlap with ArmoRM alone, indicating multi-objective rebalancing adds nothing in this regime\n- **Comparison to prior claims**: reconciling with DIVE/Kirk et al. findings (different mechanisms: RL vs. SFT, KL-free vs. KL-constrained)\n\n### 6. Discussion\n- **Scope limitations**: sub-1B model, <5K prompts, ≤16 candidates, ≤3 generations\n- **When might collapse occur?** Extreme K, many more generations, stronger reward models, narrower prompt sets\n- **Practical implications**: practitioners need not add diversity interventions for standard curation pipelines at this scale\n- **Relation to mode collapse in RL**: iterative SFT on curated data ≠ reward maximization via policy gradient\n\n### 7. Conclusion\n- Under standard small-scale conditions, iterative reward curation does not cause diversity collapse\n- The community should distinguish curation-induced collapse from RL-induced collapse\n- Future work: scaling K, generations, model size to find actual boundary\n\n## Contributions\n\n1. **Systematic empirical study** of diversity under iterative reward curation across 6 conditions × 3 generations (under standard small-scale conditions: sub-1B, <5K prompts, K≤16)\n2. **Negative finding with practical value**: no diversity intervention needed for standard curation pipelines at this scale, contra assumptions in DIVE/DARLING/CD-RLHF\n3. **LoRA diversity artifact**: LoRA training inflates measured diversity vs Full-FT independent of curation, a confound for future diversity studies\n4. **Taxonomy of collapse sources**: distinguishing curation pressure from RL mode-seeking, KL divergence, and data homogeneity as independent collapse mechanisms\n\n## Tables/Figures\n\n| ID | Type | Content | Purpose |\n|----|------|---------|---------|\n| Fig 1 | Line plot | Vendi Score across 3 generations, all 6 conditions + baselines | Core result: no collapse trajectory |\n| Fig 2 | Diagram | Pipeline overview (generate → score → select → SFT → repeat) | Method clarity |\n| Table 1 | Results | Full metrics: Vendi, reward, pairwise sim, per condition per generation | Complete numerical evidence |\n| Table 2 | Comparison | Our conditions vs. prior work settings (model size, K, generations, RL vs SFT) | Scope positioning |\n| Fig 3 | Bar chart | LoRA vs Full-FT baseline diversity drift | LoRA artifact evidence |\n| Fig 4 | Scatter/heatmap | CARR proxy correlations + selection overlap | Proxy covariance finding |\n| Table 3 | Taxonomy | Sources of collapse: curation / RL / KL / data, with literature pointers | Conceptual contribution |\n\n---\n\n# Outline B: Boundary Finding (K=16 triggers collapse)\n\n## Title Candidates\n\n1. \"The Collapse Threshold: Iterative Reward Curation Triggers Diversity Loss Only Under Extreme Selection Pressure\"\n2. \"When Does Best-of-K Curation Break Diversity? Identifying the Selection Pressure Boundary\"\n3. \"Safe Curation: Diversity Collapse Requires K≥16 in Iterative Reward Selection\"\n\n## Abstract (core 3 sentences)\n\nIterative reward curation is assumed to progressively erode output diversity, yet the conditions under which collapse actually occurs remain uncharacterized. Through systematic experiments across 6 conditions (K=4/8/16, LoRA/Full-FT) over 3 generations, we identify a sharp boundary: diversity remains stable for K≤8 (retention ≥12.5%) but collapses at K=16 (retention 6.25%), establishing that standard curation is safe while extreme selection pressure is not. This boundary provides a practical guideline: practitioners can safely use best-of-K curation with K≤8 without diversity interventions, while K≥16 requires explicit diversity preservation mechanisms.\n\n## Sections + Key Points\n\n### 1. Introduction\n- Iterative curation ubiquitous in modern alignment pipelines\n- Diversity collapse concern motivates complex interventions (DIVE, DARLING, CD-RLHF, GEM)\n- Missing: characterization of WHEN collapse actually occurs\n- Key insight: collapse is not gradual, it has a threshold tied to selection pressure (retention rate)\n- Our contribution: identify boundary at K=16 / 6.25% retention, below which standard curation is safe\n- Practical value: tells practitioners exactly when to worry (and when not to)\n\n### 2. Related Work\n- **Diversity preservation methods**: DIVE, DARLING, CD-RLHF, GEM (all assume collapse is default)\n- **Selection pressure in evolutionary computation**: tournament size, truncation selection, parallels to best-of-K\n- **Kirk et al.**: diversity taxonomy, but no systematic threshold study\n- **Reward model properties**: ArmoRM, concentration of reward mass\n\n### 3. Method\n- **Pipeline**: identical to Outline A\n- **Conditions**: designed to sweep selection pressure: K=4 (25%), K=8 (12.5%), K=16 (6.25%)\n- **Architecture axis**: LoRA vs Full-FT (controls for regularization confound)\n- **Metrics**: Vendi Score, reward score, generation-over-generation diversity delta, pairwise cosine similarity distribution\n- **Threshold detection**: operationalize \"collapse\" as Vendi Score drop > X% sustained across generations\n- **CARR dry-run**: test whether multi-objective rebalancing can prevent collapse at K=16\n\n### 4. Results\n\n#### 4.1 Safe regime (K≤8): No collapse\n- LoRA K=4: Vendi -0.27% (within baseline noise of +3.13%)\n- LoRA K=8: Vendi +0.04%\n- Full-FT K=4: +0.68% to +0.91%\n- Quality stable (±1%), training loss decreasing\n\n#### 4.2 Collapse regime (K=16): Diversity breaks\n- Full-FT K=16 lr=2e-5: Vendi drops [X]% by generation 3\n- Pairwise similarity increases, distribution narrows\n- Quality initially improves then plateaus (reward hacking signature)\n- Training loss still decreases (model converges to narrow mode)\n\n#### 4.3 Boundary characterization\n- Sharp transition between K=8 (safe) and K=16 (collapse)\n- Not gradual: K=4 and K=8 nearly identical, K=16 qualitatively different\n- Retention rate 6.25% as critical threshold\n\n#### 4.4 Supplementary findings\n- LoRA artifact: +3.13% baseline drift suggests LoRA regularization preserves diversity\n- CARR proxy covariance: r=0.63-0.77, 99.3% overlap, rebalancing cannot rescue K=16 collapse because proxies align with reward\n\n### 5. Analysis\n- **Why the threshold?** At K≤8, prompt-level diversity dominates selection pressure; at K=16, selection pressure overwhelms prompt diversity\n- **LoRA as implicit diversity preservation**: low-rank constraint limits how far model can drift per iteration\n- **Why CARR fails at the boundary**: when text proxies covary with reward (r=0.63-0.77), rebalancing selects the same outputs (99.3% overlap), so it cannot counteract extreme selection pressure\n- **Evolutionary analogy**: K maps to tournament size; known phase transition in evolutionary computation at high tournament pressure\n\n### 6. Practical Guidelines\n- **Safe curation**: K≤8 (retention ≥12.5%) requires no diversity intervention at sub-1B scale\n- **Danger zone**: K≥16 (retention ≤6.25%) requires explicit diversity mechanisms\n- **Architecture choice**: LoRA provides implicit diversity buffer vs Full-FT\n- **Proxy-based rebalancing insufficient**: when proxies correlate with reward, they cannot independently preserve diversity\n- **Recommendations for scaling**: expected threshold may shift with model size, prompt diversity, generation count\n\n### 7. Discussion\n- **Scope**: sub-1B model, <5K prompts, ≤3 generations; threshold may differ at larger scale\n- **Implications for existing methods**: DIVE/DARLING/CD-RLHF may be solving a problem only relevant at extreme K or many generations\n- **Open questions**: does threshold shift with model capacity? With prompt set size? With number of generations?\n\n### 8. Conclusion\n- Diversity collapse under iterative curation is not a default outcome but a threshold phenomenon\n- Boundary at K=16 / 6.25% retention provides actionable guidance\n- Standard pipelines (K≤8) are safe; extreme selection requires intervention\n\n## Contributions\n\n1. **Collapse boundary identification**: diversity loss occurs at K≥16 (retention ≤6.25%) but not at K≤8, establishing a sharp threshold for iterative reward curation\n2. **Practical safety guideline**: standard best-of-K curation (K≤8) does not require diversity interventions at sub-1B scale with <5K prompts over ≤3 generations\n3. **Failure mode characterization**: at the boundary, proxy-based rebalancing (CARR) fails due to reward-proxy covariance (r=0.63-0.77), indicating that independent diversity signals are necessary\n4. **LoRA regularization effect**: LoRA training provides implicit diversity preservation vs Full-FT, relevant as a confound and as a practical mitigation\n\n## Tables/Figures\n\n| ID | Type | Content | Purpose |\n|----|------|---------|---------|\n| Fig 1 | Line plot | Vendi Score across generations: K=4, K=8 flat; K=16 drops | Core boundary visualization |\n| Fig 2 | Diagram | Pipeline + selection pressure illustration (K→retention rate) | Method + intuition |\n| Table 1 | Results | Full metrics per condition per generation | Complete evidence |\n| Fig 3 | Phase diagram | Selection pressure (K) vs diversity change, with threshold marked | Boundary characterization |\n| Fig 4 | Distribution plot | Pairwise similarity distributions: K=8 vs K=16 at gen 3 | Collapse mechanism |\n| Table 2 | Guidelines | K value → retention → collapse risk → recommended intervention | Practical contribution |\n| Fig 5 | Bar chart | LoRA vs Full-FT diversity trajectories | Regularization finding |\n| Fig 6 | Correlation matrix | CARR proxy scores vs ArmoRM reward | Proxy covariance evidence |\n| Table 3 | Comparison | Our threshold vs. prior work assumptions | Positioning |\n"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T03:55:34.889482+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/collapse_aware_reward_rebalancing/artifacts/paper_outline_ab.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_outline_ab_variants_20260517T035337",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-17T03:55:34.889654+00:00_

已写入 `artifacts/paper_outline_ab.md`。

两套 outline 的核心区别：

- **Outline A** (纯 negative result): 贡献靠方法论 rigor + collapse 源头 taxonomy + LoRA artifact，故事是 "the field is solving a non-problem in this regime"，风险是 reviewer 觉得 scope 太小、insight 不够
- **Outline B** (boundary finding): 故事更强，有 actionable threshold (K=16 / 6.25% retention)，贡献是正面的 practical guideline + failure mode characterization，但依赖 K=16 实验确实触发 collapse

建议等 K=16 结果出来再决定走哪条线。如果 K=16 触发了 collapse，Outline B 明显更有竞争力（positive framing + actionable）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_paper_outline_ab_variants_20260517T035337"
}
```

</details>

---
