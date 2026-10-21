# Layer Stability Analysis: Deep Dive + Visualization Plan

## 1. Literature Review

### 1.1 Layer-wise Probing in LLMs/VLMs

Layer-wise probing is a mature methodology with well-established baselines:

- **Tenney et al. (ACL 2019)** "BERT Rediscovers the Classical NLP Pipeline": Edge probing across BERT layers shows linguistic tasks appear in pipeline order (POS→parsing→NER→SRL→coreference). Established the layer-wise probing paradigm.
- **Hewitt & Manning (NAACL 2019)** "A Structural Probe for Finding Syntax": Linear probes recover parse tree structure from BERT/ELMo embeddings, showing syntax is geometrically encoded.
- **Chen et al. (arXiv:2312.04333, 2024)** "Is Bigger and Deeper Always Better? Probing LLaMA Across Scales and Layers": Lower/middle LLaMA-2 layers have negligible arithmetic/factual knowledge but possess logical reasoning; factual capabilities show sharp jumps in deeper layers.
- **Jin et al. (COLING 2025)** "Exploring Concept Depth": More complex concepts are acquired in deeper layers across LLaMA/Gemma/Qwen families.
- **Ling et al. (arXiv:2506.02132, 2025)** "Echoes of BERT": Extended Tenney's analysis to 25 modern LLMs (Pythia, OLMo-2, Gemma-2, Qwen2.5, Llama-3.1). Hierarchical pipeline persists but larger models compress it toward earlier layers.
- **Belrose et al. (arXiv:2303.08112, 2023)** "Tuned Lens": Affine probes at each layer decode hidden states into vocabulary distributions, showing progressive prediction refinement layer-by-layer.

**Relevance to our work**: These papers establish that layer-wise probing is standard methodology. However, none focus on the *stability* (variance) of probe performance across layers. They report per-layer accuracy curves but don't analyze whether fine-tuning makes these curves smoother. This is our gap.

### 1.2 Representation Stability & Fine-tuning Effects

- **Kornblith et al. (ICML 2019)** CKA: Standard metric for cross-layer/cross-model representational similarity.
- **Phang et al. (BlackboxNLP 2021)** "Fine-Tuned Transformers Show Clusters of Similar Representations Across Layers": CKA on fine-tuned RoBERTa reveals block diagonal structure—strong within-cluster similarity in early/late layers. Top layers become so similar they can be pruned without performance loss.
- **Zhou & Srikumar (ACL 2022)** "A Closer Look at How Fine-tuning Changes BERT": Fine-tuning increases inter-class distances while preserving spatial structure. Changes are task-directed, not arbitrary.
- **Khayatan et al. (ICCV 2025, arXiv:2501.03012)**: Fine-tuning multimodal LLMs makes concept-related features more linearly separable in deeper layers.
- **Sharma et al. (arXiv:2410.21228, 2024)** "LoRA vs Full Fine-tuning: An Illusion of Equivalence": LoRA produces "intruder dimensions" absent in full fine-tuning, changing representation geometry differently.
- **Ethayarajh (EMNLP 2019)**: All layers of BERT/GPT-2 produce anisotropic representations; upper layers are more context-specific.

**Relevance**: Phang et al.'s finding that fine-tuning creates block-diagonal CKA structure is the closest analog to our stability finding—fine-tuning homogenizes representations within layer blocks. Our per-layer probe stability extends this: not just CKA similarity, but functional uniformity (consistent R² across layers).

### 1.3 Layer Collapse & Neural Collapse

- **Papyan et al. (PNAS 2020)** "Neural Collapse": Terminal phase of training causes within-class variability to collapse, class means converge to simplex ETF. Foundational.
- **Wu & Papyan (NeurIPS 2024)** "Linguistic Collapse": Neural collapse extends to causal LLMs, developing with scale and regularization.
- **Rangamani et al. (ICML 2023)** "Feature Learning through Intermediate Neural Collapse": Within-class covariance decreases relative to between-class covariance progressively deeper into trained networks. **Key**: collapse is progressive across depth, not just at final layer.
- **Zhou et al. (CPAL 2025)** "Are All Layers Created Equal": Deeper layers enhance NC and aid generalization but are more susceptible to memorization; middle layers contribute minimally.
- **Dong et al. (ICML 2021)** "Attention is Not All You Need": Pure self-attention without skip connections converges doubly-exponentially to rank-1 matrix. Skip connections prevent collapse.
- **Noci et al. (NeurIPS 2022)**: Stacking self-attention causes rank collapse at initialization, causing gradient vanishing.
- **Nait Saada et al. (ICML 2025, arXiv:2410.07799)**: Rank collapse in width worsens with context length, spectral gap causes this.
- **Zhai et al. (ICML 2023)**: Attention entropy collapse—attention scores become pathologically concentrated; sigma-Reparam prevents it.
- **Arefin et al. (ICLR 2025)** "Seq-VCR": Intermediate representation collapse limits reasoning. Preventing it via regularization achieves 99.5% on 5×5 integer multiplication vs 0% baseline.

**Relevance**: Our "untrained collapse" (probe failure in ~50% of layers) aligns with Noci et al.'s rank collapse at initialization. The key insight: VLA fine-tuning *resolves* initialization-induced collapse, creating functional representations across all layers. Arefin et al. is the strongest parallel—they show intermediate collapse limits capability, which mirrors our finding that untrained models have collapsed intermediate layers.

### 1.4 VLA Representation Analysis

- **Haon et al. (CoRL 2025, arXiv:2509.00328)** "Mechanistic Interpretability for Steering VLAs": Projects FFN activations onto token embedding basis, identifies sparse semantic directions (speed, direction) causally linked to action selection. Zero-shot behavioral control on OpenVLA/pi0.
- **Grant et al. (arXiv:2603.19233, 2026)** "Not All Features Are Created Equal": Cross-architecture study on 6 VLAs. Visual pathway dominates; <25% of FFN neurons rewired for action prediction. LIBERO-Goal shows language matters when vision is ambiguous.
- **Swann et al. (arXiv:2603.19183, 2026)**: SAEs on VLA hidden layers: majority of features are memorized demos, some are interpretable motion primitives. Linear probes decode task states >90% accuracy across most layers.
- **Kachaev et al. (arXiv:2510.25616, 2025)** "Don't Blind Your VLA": Naive action fine-tuning induces representation collapse and attention sink, with diffuse/misplaced attention maps.
- **Hancock et al. (ICLR 2025, arXiv:2509.22195)** "VLM2VLA": LoRA-only fine-tuning minimally modifies VLM backbone, preserving VLM capabilities.

**Relevance**: Grant et al. confirms vision dominance (aligns with our negative result). Kachaev et al.'s finding that fine-tuning *induces* representation collapse is the opposite of our finding that fine-tuning *resolves* collapse—critical distinction. Their collapse is about losing visual grounding; our collapse is about randomly-initialized LLM layers being non-functional. Swann et al.'s >90% linear probe accuracy across layers supports our stability finding.

---

## 2. Story Strength Assessment

### 2.1 The Claim

> **"VLA training reorganizes LLM representations into a stable, layer-uniform action-encoding pathway."**

Evidence:
- **Action prediction probe**: Trained R² = 0.45–0.68 (31/33 layers > untrained), untrained = 0.05–0.62 with multiple convergence failures
- **Action-delta probe**: Trained = stable 0.04–0.06 across L5-L30, untrained = catastrophic (L5-L28 ≈ 0, only L1-L4 and L32 nonzero)
- **Temporal distance probe**: Trained 17/33 healthy layers vs untrained more collapse

### 2.2 Standalone Paper Potential: **Weak standalone, strong contribution**

**For**: 
- Novel angle—nobody has reported probe *stability* (variance across layers) as a metric; existing work reports per-layer curves but doesn't analyze their smoothness
- Three independent probe types converge on the same pattern
- Connects to theoretical literature (rank collapse at initialization, intermediate neural collapse)
- Practically relevant: if a VLA has stable representations, individual layers can be pruned/distilled more safely

**Against**:
- Single model (OpenVLA-7B) + single benchmark (LIBERO-10)—reviewers will demand generalization
- The "stability" claim needs a formal metric (e.g., coefficient of variation of per-layer R²), not just visual inspection
- Untrained baseline is a randomly-initialized LLM with frozen SigLIP—some reviewers may argue this isn't a meaningful comparison (who cares about untrained model internals?)
- Peak-performance gap is small (ΔR² = 0.067 best-vs-best), so the "information content" story is negative
- No causal evidence that stability → downstream performance

**Verdict**: Not enough for a standalone paper at CoRL 2026. Best positioned as a section within a broader "What does VLA training learn?" analysis paper (Option B from ROADMAP), or as supporting evidence in the LIBERO-Goal instruction-conditioned probing paper (Option A).

### 2.3 Reviewer Attack Surface

1. **"Untrained is a straw man"**: Random LLM weights are unrealistic. Compare to *pre-trained but not action-fine-tuned* Llama-2 instead.
   - **Mitigation**: Add Prismatic-7B (pre-trained VLM, no action fine-tuning) as a baseline. This distinguishes VLM pre-training effect from VLA fine-tuning effect.
   
2. **"Single model, single benchmark"**: OpenVLA-7B on LIBERO-10 only.
   - **Mitigation**: Add at least one more VLA (e.g., OpenVLA with different LoRA configs, or a smaller VLA like Octo) and one more benchmark (LIBERO-Goal or Bridge-v2).

3. **"No formal stability metric"**: "Stable" and "collapsed" are informal.
   - **Mitigation**: Define CoV(R²) = std(R²) / mean(R²) across layers. Report with confidence intervals. Run permutation test for stability difference.

4. **"Correlation ≠ Causation"**: Stable probes don't prove the model *uses* these representations.
   - **Mitigation**: Layer ablation (zero out individual layers, measure action prediction degradation). If trained model degrades uniformly while untrained degrades only at specific layers, this supports the "distributed pathway" claim.

5. **"Vision encoder confound"**: SigLIP is frozen; maybe it's just passing clean signal through residual connections.
   - **Mitigation**: Compare probe R² with and without residual stream (ablate skip connections at test time). Or probe on LLM-only activations (subtract vision-projected component).

### 2.4 What This Finding Actually Says

The most defensible framing:

> VLA action fine-tuning does not inject new information beyond what the vision encoder provides (negative result on information content). However, it structurally reorganizes the LLM backbone: randomly initialized layers that fail to maintain coherent representations become uniformly functional after training. This suggests VLA training's primary effect on the LLM is **representational infrastructure**—creating a stable computational substrate—rather than **information enrichment**.

This framing:
- Acknowledges the negative result honestly
- Positions stability as a structural finding about *how* fine-tuning works, not *what* it learns
- Connects to pruning/efficiency literature (if all layers are uniform, some are redundant)
- Opens door to follow-up: *why* is uniformity beneficial for action prediction?

---

## 3. Visualization Schemes

### Figure 1: Layer-wise Probe Performance Comparison (Primary Figure)

**Type**: Multi-panel line plot with confidence bands

**Layout**: 1 row × 3 columns (one per probe type)

**Panel A — Action Prediction Probe (R²)**
- X-axis: Layer index (0–32)
- Y-axis: R² (range 0–0.8)
- Lines: Trained OpenVLA (blue, solid), Untrained OpenVLA (red, dashed), DINO-v2 (green, horizontal dashed line at R²=0.676)
- Shading: 95% CI bands (bootstrap, task-level)
- Annotations: Mark collapsed/unconverged layers for untrained with × markers
- Key visual: Blue line is flat and high; red line is jagged with gaps

**Panel B — Action-Delta Probe (R²)**
- X-axis: Layer index (0–32)
- Y-axis: R² (range -0.05–0.10)
- Lines: Trained (blue), Untrained (red), DINO (green horizontal)
- Key visual: Blue line is a flat band around 0.05; red line is zero everywhere except L1-4 and L32

**Panel C — Temporal Distance Probe (Spearman ρ)**
- X-axis: Layer index (0–32)
- Y-axis: ρ (range 0–1.0)
- Lines: Trained (blue), Untrained (red), DINO (green horizontal at 0.901)
- Markers: × for collapsed layers (ρ=0)
- Key visual: Blue has more healthy points; both have collapsed layers but untrained has more

**Data sources**: 
- Trained action R²: `mvp2_action_trained` experiment results (per-layer R² from ridge regression)
- Untrained action R²: `mvp2_action_untrained` results
- DINO R²: `mvp2_action_dino` results
- Temporal distance: `mvp_probe_trained`, `mvp_probe_untrained`, `dinov2_baseline`
- Action-delta: from MVP-2 action-delta analysis

**matplotlib spec**:
```python
fig, axes = plt.subplots(1, 3, figsize=(15, 4.5), sharey=False)
# Use seaborn style, Nature-quality fonts
# Color palette: trained=#2196F3, untrained=#F44336, dino=#4CAF50
# Line width: 2pt for main, 1pt for CI bands
# Font: 10pt labels, 11pt panel titles
# Add CoV(R²) annotation in each panel corner
```

---

### Figure 2: Stability Metric Comparison (Bar Chart)

**Type**: Grouped bar chart with error bars

**Layout**: Single panel

**X-axis**: Probe type (Action R², Action-Delta R², Temporal ρ)
**Y-axis**: Coefficient of Variation = std/mean of per-layer metric (excluding collapsed layers)
**Bars**: Trained (blue), Untrained (red)
**Error bars**: Bootstrap 95% CI on CoV

**Expected pattern**: Untrained CoV >> Trained CoV for all three probe types

**Purpose**: Quantifies "stability" formally. A single number per condition that captures the core finding.

**Data**: Computed from per-layer metrics in Figure 1.

**matplotlib spec**:
```python
fig, ax = plt.subplots(1, 1, figsize=(5, 4))
# Grouped bars, width=0.35
# Hatching for untrained bars
# Significance stars (**/***) above paired bars
# Y-axis label: "Coefficient of Variation (lower = more stable)"
```

---

### Figure 3: Layer Health Heatmap

**Type**: Binary/categorical heatmap

**Layout**: Single panel, 3 rows × 33 columns

**Rows**: Action Probe, Action-Delta Probe, Temporal Distance Probe
**Columns**: Layers 0–32
**Cell color**: 
- Green: Trained > Untrained (functional gain)
- Yellow: Trained ≈ Untrained (no change)
- Red: Collapsed in untrained (probe failed to converge or R² ≈ 0)
- Gray: Collapsed in both

**Cell annotation**: Δ value (trained − untrained) in each cell

**Expected pattern**: Green dominates for trained; red band in middle layers for untrained (especially action-delta L5-L28)

**Purpose**: Single-glance summary of the layer stability finding across all probes. Good for talks/posters.

**Data**: Per-layer metrics from all three probe types, thresholds:
- Collapsed: R² < 0.05 or ρ < 0.1 or probe failed to converge
- Functional gain: trained − untrained > 0.05

**matplotlib spec**:
```python
fig, ax = plt.subplots(1, 1, figsize=(14, 2.5))
# Use imshow or pcolormesh
# Custom colormap: diverging RdYlGn
# Add text annotations in each cell (small font, 7pt)
# X-ticks every 4 layers, minor ticks every layer
# Bold border around "collapse zone" (L5-L28 for action-delta)
```

---

## 4. Additional Experiments Needed

### Priority 1 (Required for any publication)

| Experiment | Purpose | Effort | Impact |
|-----------|---------|--------|--------|
| **Pre-trained VLM baseline** (Prismatic-7B, no action FT) | Distinguish VLM pre-training effect from VLA fine-tuning effect. Addresses "untrained is straw man" attack. | 1 day (feature extraction + probing) | Critical—without this, the comparison is random-init vs trained, which is trivially expected |
| **Formal stability metric** (CoV with bootstrap CI, permutation test) | Quantify "stability" rigorously | 0.5 day (reanalysis of existing data) | Critical—current claim is qualitative |
| **Per-layer probe convergence diagnostics** | Document which untrained layers failed to converge and why (loss curves, gradient norms) | 0.5 day | Addresses reviewer concern about probe quality vs representation quality |

### Priority 2 (Strongly recommended)

| Experiment | Purpose | Effort | Impact |
|-----------|---------|--------|--------|
| **Second VLA model** (e.g., OpenVLA with LoRA-only, or smaller model) | Generalization across architectures | 2-3 days | Addresses single-model concern |
| **LIBERO-Goal probing** | Test if stability pattern holds in vision-ambiguous setting where language matters | 2-3 days | Could strengthen story significantly—if stability + language sensitivity co-occur |
| **CKA analysis** (layer-to-layer similarity matrix, trained vs untrained) | Connect to Phang et al.'s block-diagonal finding; show VLA training creates different CKA structure | 1 day | Strengthens theoretical grounding |

### Priority 3 (Nice to have)

| Experiment | Purpose | Effort | Impact |
|-----------|---------|--------|--------|
| **Layer ablation** (zero out individual layers, measure action loss) | Causal evidence that stable representations are *used* | 1-2 days | Addresses correlation≠causation |
| **Representation rank analysis** (effective rank per layer, trained vs untrained) | Connect to rank collapse literature (Noci et al., Dong et al.) | 0.5 day | Mechanistic understanding |
| **Attention entropy per layer** (trained vs untrained) | Connect to Zhai et al.'s entropy collapse; check if VLA training increases attention entropy | 0.5 day | Additional angle on stability |

### Timeline Assessment (CoRL deadline: May 29 = 14 days)

- Priority 1 experiments: ~2 days → **must start immediately**
- Priority 2 (second model + LIBERO-Goal): 2-3 days each, can partially parallelize → **feasible if started by May 17**
- Priority 3: cherry-pick 1-2 based on Priority 1/2 results
- Writing: 3-4 days for full paper
- **Verdict**: Tight but feasible for Option B paper if Priority 1 is completed by May 17 and writing starts May 22.
