# Paper Framing — ACIB

## Target Venue
CoRL 2026 (abstract deadline 5/26, paper deadline 5/29)

## Core Insight

Three architectural constraints are necessary for IB-based token importance learning in compact VLAs:
1. **Gradient isolation**: Joint training corrupts the base policy through gradient pollution (-7.8pp, v7). The action expert must be frozen.
2. **Connector participation**: Scorer-only training on frozen features lacks capacity for spatial conditioning, producing only global bias (v7.1). The connector must participate in representation learning.
3. **Weight preservation**: Even minimal connector drift (0.4% parameter change) significantly damages spatial reasoning (-6.6pp, p<0.05, v7.2). Effects on other task types are not statistically significant at 500 episodes. LoRA-based connector training preserves original weights exactly when scoring is disabled (α=0.0 = baseline by construction), eliminating the drift confound and enabling clean measurement of the pure scoring contribution.

## Title Candidates

1. **Action-Conditioned Information Bottleneck for Interpretable Vision-Language-Action Models**
2. **Learning What to See: Decoupled Token Importance Scoring for Compact VLAs**
3. **ACIB: Token-Level Information Bottleneck with Gradient-Isolated Training for Robotic Manipulation**
4. **Three Constraints for Token Importance Learning in Compact VLAs** (new — emphasizes the analysis contribution)

## Core Claims

| # | Claim | Status | Evidence |
|---|-------|--------|----------|
| C1 | Joint training of IB auxiliary losses corrupts the base policy through gradient pollution, even when scoring is disabled (α=0.0) | **VERIFIED** | v7: α=0.0 SR=58.2% vs baseline=66.0% (-7.8pp); α=0.1 (-9.8pp); α=1.0 seed1 (-7.6pp), seed2 (-14.6pp) |
| C2 | Scorer-only training (123K params on frozen features) lacks capacity for spatial conditioning and only produces global bias | **VERIFIED** | v7.1: Probe A cos>0.8 all pairs; weight_std negligible; heatmaps identical across instructions |
| C3 | Connector+scorer decoupled training achieves true action-conditioned spatial importance | **VERIFIED** | v7.2: Probe A cos∈[0.593, 0.944]; weight_std>0.19; 2 seeds consistent |
| C4 | Log-barrier contrastive loss resolves the vanishing gradient problem of standard cosine contrastive when similarities are high | **VERIFIED** | v7.1→v7.2 transition: log(1-cos+ε) enables gradient flow through connector |
| C5 | Connector drift (0.4% weight change) significantly damages spatial reasoning (-6.6pp, p<0.05). Effects on other suites are not statistically significant (object -2.2pp p=0.23, goal +2.2pp p=0.20). The drift confound makes it impossible to isolate the scoring effect without exact baseline recovery | **VERIFIED** | v7.2 α=0.0: spatial 59.4%(-6.6pp, sig), object 65.6%(-2.2pp, NS), goal 78.6%(+2.2pp, NS). 3-suite avg -2.2pp. Sanity check FAIL |
| C6 | LoRA-isolated connector training provides exact baseline recovery (α=0.0 = baseline by construction), eliminating the drift confound and enabling clean measurement of scoring contribution | **PENDING** | `[PENDING: v7.3 LoRA Probe A + α=0.0 eval]` |
| C7 | ACIB scoring at inference time preserves or improves base policy performance when measured against exact baseline | **PENDING** | `[PENDING: v7.3 α=1.0 vs α=0.0 full eval across 4 suites]` |
| C8 | ACIB-scored models exhibit improved robustness to visual perturbations on task-irrelevant regions | **PENDING** | `[PENDING: Perturbation robustness eval]` |
| C9 | ACIB provides meaningful efficiency gains via token dropping at configurable thresholds | **PENDING** | `[PENDING: Token dropping efficiency measurements]` |
| C10 | Connector fine-tuning (not just scorer) is the critical ingredient for spatial conditioning | **PENDING** | `[PENDING: Connector-only ablation without scorer]` |

## Story Arc

### Problem (1 paragraph)
Vision-Language-Action models process all visual tokens uniformly regardless of task relevance. For compact VLAs (e.g., SmolVLA with only 64 visual tokens), every token matters, yet the model has no mechanism to distinguish action-relevant from irrelevant visual information. This limits interpretability, robustness to visual distractors, and inference efficiency.

### Failed Intuitions (1 paragraph — sets up our insight)
The natural approach is to add an information bottleneck auxiliary loss during training that teaches a scorer which tokens matter. However, we show through systematic experiments (v1-v7) that this intuition fails catastrophically in compact VLAs: joint training of IB objectives corrupts the base policy through gradient pollution, degrading performance by 7-15 percentage points even when scoring is disabled at inference. Training only a lightweight scorer on frozen features (v7.1) avoids corruption but produces only global bias without spatial discrimination. Unfreezing the connector for representation learning (v7.2) achieves spatial conditioning but introduces a new problem: even 0.4% connector weight drift significantly damages spatial reasoning (-6.6pp, p<0.05), and the resulting representation shift makes it impossible to cleanly isolate the scoring contribution from the drift confound.

### Insight (1 paragraph)
The key insight is that three constraints must be simultaneously satisfied: (1) the action expert must be shielded from all auxiliary gradients, (2) the connector must participate in learning task-discriminative features (not just the scorer), and (3) the connector's original weights must be perfectly recoverable to provide an exact baseline for comparison. LoRA-based connector training satisfies all three: low-rank adapters enable spatial conditioning through the connector, while disabling LoRA (scale=0) exactly recovers the pretrained connector, providing a clean control condition that eliminates the drift confound.

### Method (1 paragraph)
ACIB consists of: (1) a lightweight scorer network that produces per-token importance weights conditioned on both visual features and language instructions; (2) a log-barrier contrastive loss that enforces different instructions yield different importance distributions; (3) LoRA-isolated connector training that enables representation learning while preserving original weights exactly; (4) residual soft modulation that applies learned importance scores at inference without hard token dropping.

### Validation (1 paragraph)
We validate on LIBERO (4 suites, 40 tasks) using SmolVLA as backbone. Probe A (cosine similarity between importance maps under different instructions) confirms spatial conditioning. [PENDING: v7.3 LoRA α=0.0 recovers exact baseline performance. α=1.0 evaluation determines whether scoring improves, preserves, or degrades performance. Perturbation experiments test robustness. Efficiency measurements quantify token reduction potential.]

## Paper Structure

### Abstract (150-250 words)
Problem: VLAs lack mechanism to identify action-relevant visual information. Contribution: ACIB with three architectural constraints for IB training in compact VLAs. Key result: spatial conditioning + interpretability. [Performance claim depends on v7.3 results]

### 1. Introduction (1.5 pages)
Motivate why token importance matters for VLAs. Present the gradient pollution problem as surprising finding. Present connector sensitivity as second surprising finding. State contributions: (1) failure taxonomy revealing three necessary constraints, (2) LoRA-isolated connector+scorer architecture, (3) log-barrier contrastive loss, (4) comprehensive evaluation on LIBERO.

### 2. Related Work (0.75 pages)
Three threads: (a) Information bottleneck in RL/robot learning (BC-IB, VIB-RL, MIB); (b) Visual token pruning/selection (LightVLA, DivPrune, ATP-LLaVA, SparseVLM, VLA-ADP, Compressor-VLA); (c) VLA robustness (RobustVLA, ReVLA). Position ACIB as first token-level IB with decoupled training for compact VLAs.

### 3. Method (2 pages)
3.1 Problem formulation and SmolVLA architecture. 3.2 Scorer network design. 3.3 Log-barrier contrastive loss. 3.4 LoRA-isolated connector training (why full fine-tuning fails, why scorer-only is insufficient). 3.5 Inference-time scoring modes (soft modulation / hard pruning).

### 4. Why Naive Approaches Fail: A Constraint Discovery (1 page)
Systematic presentation of v1-v7.2 failures. Each variant: what was tried, what constraint it violates, diagnostic evidence. Culminates in the three-constraint framework and LoRA solution.

### 5. Experiments (2 pages)
5.1 Setup (LIBERO, SmolVLA, metrics). 5.2 Main results: [depends on v7.3]. 5.3 Probe A analysis: spatial conditioning verification. 5.4 Perturbation robustness. 5.5 Efficiency measurements. 5.6 Ablations (connector-only, scorer-only, joint training, full-ft connector, loss variants).

### 6. Discussion and Limitations (0.5 pages)
Limitations: single backbone, single benchmark, compact-VLA-specific findings. Future: scaling to larger VLAs, real-robot transfer, adaptive α.

### 7. Conclusion (0.25 pages)

## Anticipated Reviewer Concerns

| Concern | Response Strategy |
|---------|------------------|
| "Only tested on one backbone (SmolVLA) and one benchmark (LIBERO)" | Acknowledge; argue compact VLAs are the regime where this matters most. SmolVLA's 64-token budget makes token selection maximally impactful. LIBERO provides 40 diverse tasks across 4 difficulty suites. |
| "No real-robot experiments" | Standard for CoRL simulation papers when benchmark is established. LIBERO is well-accepted. |
| "How does this compare to simply using attention weights as importance?" | Ablation: attention-based baseline (planned). Learned scorer is action-conditioned; attention is not instruction-specific at inference. |
| "The failure taxonomy is interesting but the final method is simple" | Frame simplicity as a strength. The failures reveal necessary constraints; the final design is minimal precisely because we understand those constraints. |
| "Why not just train a larger scorer instead of unfreezing connector?" | v7.1 demonstrates capacity on frozen features is insufficient. Connector must reshape representations, not just read them. |
| "Efficiency gains are modest given only 64 tokens" | Frame primary contribution as interpretability and constraint discovery. For larger VLAs (256+ tokens), efficiency gains scale proportionally. |
| "BC-IB (ICML 2025) already does IB for behavior cloning" | BC-IB: single fused latent (not per-token), MINE estimator (not contrastive), no interpretable importance maps, no gradient pollution analysis (they fine-tune everything). Different operating regime. |
| "LightVLA already does token selection for VLAs" | LightVLA: hard pruning for efficiency, no IB framework, no contrastive conditioning, no gradient pollution analysis, targets 7B models (different regime). |
| "VLA-ADP / Compressor-VLA do similar token compression" | Need to verify these papers exist (literature_map entries may be hallucinated). If real: they target efficiency in large VLAs, not IB-principled importance in compact VLAs with constraint analysis. |
| "The connector sensitivity finding is specific to SmolVLA's architecture" | Acknowledge but argue: PixelShuffle connectors are common in compact VLAs; the sensitivity likely generalizes to any connector that serves as a tight bottleneck between vision encoder and action expert. |

## Key Figures

1. **Figure 1 (teaser)**: Side-by-side importance heatmaps for different instructions on same scene, showing spatial conditioning. Plus performance comparison: joint training (-7.8pp) vs LoRA-isolated (TBD).

2. **Figure 2 (method overview)**: Architecture diagram showing frozen (gray), LoRA (blue), scorer (orange) components. Gradient flow arrows. α=0.0 path (LoRA disabled, exact baseline) vs α=1.0 path (scoring active).

3. **Figure 3 (constraint discovery)**: Three-panel showing each constraint violation and its consequence. v7: gradient pollution; v7.1: global bias; v7.2: connector sensitivity.

4. **Figure 4 (Probe A results)**: Cosine similarity comparison across versions: v7 (joint) → v7.1 (scorer-only, global bias) → v7.2 (connector+scorer, spatial but fragile) → v7.3 (LoRA, spatial + preserved).

5. **Figure 5 (main results table)**: 4-suite LIBERO SR for baseline, ACIB α=0.0, ACIB α=1.0, + ablations.

6. **Figure 6 (perturbation robustness)**: `[PENDING]`

7. **Figure 7 (importance map gallery)**: Multiple scenes x multiple instructions showing qualitative token importance.

## Ablation Design

| Ablation | Purpose | Status |
|----------|---------|--------|
| Joint training (v7) | Show gradient pollution (Constraint 1) | **Done** |
| Scorer-only (v7.1) | Show capacity insufficiency (Constraint 2) | **Done** |
| Full-ft connector+scorer (v7.2) | Show connector sensitivity (Constraint 3) | **Done** (Probe A PASS, eval FAIL: -6.6pp/-5.0pp spatial) |
| LoRA connector+scorer (v7.3) | Our method — satisfies all 3 constraints | `[PENDING: training + eval]` |
| α=0.0 passthrough (v7.3) | Verify exact baseline recovery | `[PENDING]` |
| α=1.0 full scoring (v7.3) | Core performance gate | `[PENDING]` |
| Connector-only (no scorer) | Isolate connector contribution | `[PENDING]` |
| Random importance baseline | Lower bound for scoring quality | `[PENDING]` |
| Attention-based importance | Heuristic comparison | `[PENDING]` |
| Standard cosine loss (no log-barrier) | Justify log-barrier design | `[PENDING]` |
| Perturbation: relevant vs irrelevant regions | Robustness claim | `[PENDING]` |

## Positioning Summary

**vs BC-IB**: Token-level (interpretable) vs representation-level; decoupled training vs joint; gradient pollution analysis absent in BC-IB.

**vs LightVLA**: IB-principled vs heuristic pruning; soft gating vs hard selection; robustness-focused vs efficiency-focused; compact VLA regime (64 tokens) vs large VLA (256+ tokens).

**vs RobustVLA**: Training-time regularization vs post-training RL; interpretable importance maps vs black-box Jacobian penalty; potentially complementary.

**vs DivPrune/ATP-LLaVA**: Learned end-to-end with action loss vs attention-based heuristics; action-conditioned vs text-conditioned.

**vs VLA-ADP / Compressor-VLA / VLA-Pruner**: ⚠️ These entries from literature_map.yaml may be LLM hallucinations (2026 papers). Must WebSearch verify arxiv IDs before citing. If real: they target inference efficiency in large VLAs, not constraint analysis for IB training in compact VLAs.

## Framing Strategy: Direction C (Hybrid) — D052

**Two-arm structure, weight adjusted by v7.3 results:**

| v7.3 Result | Primary Arm | Secondary Arm | Core Claim |
|-------------|------------|---------------|------------|
| α=1.0 ≥ baseline+1pp | Method (LoRA) | Constraint analysis | "ACIB+LoRA preserves/improves + interpretability" |
| α=1.0 ∈ baseline±1pp | Constraint analysis | Method (LoRA as engineering solution) | "Three constraints + LoRA enables clean scoring + interpretability" |
| α=1.0 < baseline-2pp | Constraint analysis only | — | "Why IB token importance requires extreme care in compact VLAs" |

**Statistical discipline (D052):**
- Only claim statistically significant results (spatial -6.6pp, p<0.05)
- Suite variation (object/goal) stays as observation paragraph, not contribution
- Never claim goal +2.2pp as "improvement" (p=0.20)
- v7.3 scorer increment < 1pp → claim "preserves", not "improves"

**Contingency: v7.3 α=1.0 regresses**
- Mitigations: (a) α sweep (0.1/0.3/0.5); (b) additive modulation; (c) layer-selective scoring
- If all fail: reframe as analysis paper (Direction B-lite)

**Contingency: v7.3 Probe A fails (cos > 0.8)**
- Mitigations: LoRA rank 16/32
- Unlikely given v7.2 full connector Probe A PASS

## Writing Timeline

- 5/17-18: v7.2 eval completes, v7.3 LoRA trains + evals
- 5/19-20: v7.3 results → finalize framing → Method + Experiments sections
- 5/21-22: Introduction + Related Work + Constraint Discovery
- 5/23-24: Abstract + Figures + polish
- 5/25: Internal review + final edits
- 5/26: Abstract submission
- 5/27-28: Camera-ready polish
- 5/29: Paper submission
