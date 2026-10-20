# Literature Scan: Phase-Adaptive Compound Compression

**Date**: 2026-05-14  
**Focus**: Papers (2024-2026) relevant to phase-gated compound sparsity and the magnitude crossover phenomenon

---

## 1. Phase-Adaptive / Dynamic Compression

### 1.1 Twilight: Adaptive Attention Sparsity with Hierarchical Top-p Pruning
- **Authors**: Lin, Tang, Yang, Wang, Tang, Tian, Stoica, Han, Gao
- **Venue**: NeurIPS 2025 Spotlight
- **Core**: Uses top-p sampling idea to adaptively decide per-token/per-step attention budget -- prunes up to 98% tokens dynamically
- **Relation**: **Support** -- demonstrates that fixed budget is suboptimal and adaptive per-step budget is superior, but operates at token level within a single sparsity axis (no compound interaction)
- **Gap**: Does not address compound sparsity or phase-dependent metric switching

### 1.2 LAVa: Layer-wise KV Cache Eviction with Dynamic Budget Allocation
- **Authors**: Shen, Yuan, Zhang, Wang, Jiang, Nguyen
- **Venue**: EMNLP 2025 Findings
- **Core**: First unified strategy for cache eviction + dynamic budget via Layer Attention Output Loss; discovers that layer budgets matter for generation, head budgets for extraction
- **Relation**: **Support** -- task-conditional budget allocation aligns with our per-phase budget idea; but no temporal/phase axis
- **Gap**: Budget allocation is static per task type, not dynamic across reasoning phases

### 1.3 LKV: End-to-End Learning of Head-wise Budgets and Token Selection
- **Venue**: arXiv 2605.06676, 2026
- **Core**: First end-to-end differentiable framework for jointly learning head budgets (LKV-H) and token selection (LKV-T), replacing all heuristics
- **Relation**: **Orthogonal/Complement** -- learned budget allocation is the mechanism we need; could serve as backbone for phase-gated controller
- **Gap**: Does not model temporal phase transitions; budget is learned offline, not adapted per generation step

### 1.4 SOL: Self-Optimizing Language Models -- Compute Where it Counts
- **Venue**: arXiv 2605.10875, 2026
- **Core**: Learns per-token compute allocation policy (easy tokens less compute, hard tokens more)
- **Relation**: **Methodological parallel** -- per-token adaptive allocation analogous to per-phase adaptive compression; validates learned controller approach

### 1.5 Token-Budget-Aware LLM Reasoning
- **Venue**: ACL 2025 Findings (arXiv 2412.18547)
- **Core**: LLMs can adaptively allocate thinking budget per query difficulty using self-consistency as proxy
- **Relation**: **Support** -- reasoning budget should vary; directly supports phase-adaptive compression for reasoning models

### 1.6 BudgetThinker: Empowering Budget-aware LLM Reasoning with Control Tokens
- **Venue**: arXiv 2508.17196, 2025
- **Core**: Inserts special control tokens to inform model of remaining token budget; two-stage SFT+RL pipeline
- **Relation**: **Orthogonal** -- budget-aware generation from compute perspective; could inspire phase-transition signaling

---

## 2. Compound/Joint Sparsity Interaction

### 2.1 SparK: Query-Aware Unstructured Sparsity with Recoverable KV Cache Channel Pruning
- **Venue**: AAAI 2026
- **Core**: Reports compound KV cache sparsity (channel + token) produces super-additive degradation (ThinK+SnapKV degrades 65%)
- **Relation**: **Direct competitor** -- first to quantify compound super-additivity; our work extends this with phase-dependent analysis

### 2.2 SLiM: One-shot Quantization and Sparsity with Low-rank Approximation
- **Authors**: Mozaffari et al.
- **Venue**: ICML 2025
- **Core**: Q+S aggregated error is non-additive; uses low-rank adapter to compensate compound compression error
- **Relation**: **Support** -- independently confirms non-additive compound error; complementary error compensation framework

### 2.3 LServe: Efficient Long-sequence LLM Serving with Unified Sparse Attention
- **Venue**: MLSys 2025
- **Core**: Integrates sparse attention + low-bit KV cache quantization into single GPU kernel; treats as separate components
- **Relation**: **Background** -- demonstrates industrial need for compound compression; lacks interaction analysis

### 2.4 GRASPrune: Global Gating for Budgeted Structured Pruning
- **Authors**: Wang et al.
- **Venue**: ACL 2026 Main
- **Core**: Learned gate scores for joint pruning of FFN channels + KV head groups under global budget
- **Relation**: **Direct competitor** -- joint pruning with learned gates; but static (no phase adaptation)

### 2.5 A Systematic Study of Compression Ordering for LLMs
- **Venue**: arXiv 2511.19495, 2025
- **Core**: P->KD->Q ordering optimal; quantization-first causes irreversible information loss; interaction depends on ordering
- **Relation**: **Support** -- ordering matters for compound compression; our phase-gating is a temporal ordering dimension

### 2.6 EVICPRESS: Joint KV-Cache Compression and Eviction
- **Venue**: arXiv 2512.14946, 2025
- **Core**: Jointly optimizes eviction and compression (quantization) for KV cache
- **Relation**: **Method-component** -- joint optimization within KV cache; single temporal axis, no head pruning compound

---

## 3. Reasoning-Phase-Dependent Model Behavior

### 3.1 RaaS: Reasoning-Aware Attention Sparsity
- **Authors**: Hu, Huang, Wang et al.
- **Venue**: ACL 2025 Findings
- **Core**: Discovers milestone tokens in reasoning -- tokens emerge, become important, then fade permanently. Achieves O(L) time+memory
- **Relation**: **Strong support** -- directly demonstrates phase-dependent token importance dynamics; "first important then not" pattern is a specific case of our observation
- **Gap**: Only considers single eviction dimension; no compound interaction study

### 3.2 Demystifying Reasoning Dynamics: Thinking Tokens are Information Peaks
- **Venue**: NeurIPS 2025
- **Core**: MI between intermediate representations and correct answer exhibits sudden peaks at thinking tokens ("Hmm", "Wait", "Therefore"); these tokens are disproportionately important
- **Relation**: **Strong support** -- reasoning has discrete info-critical phases; compression during peaks catastrophic, between peaks aggressive compression possible
- **Gap**: Information-theoretic analysis only; no compression/sparsity experiments

### 3.3 Decision Representation Transitions in Layer-Pruned LLMs
- **Venue**: arXiv 2605.07271, 2026
- **Core**: Layer pruning reveals Silent/Decisive Phase; Decision Margin undergoes sign reversal (neg->pos) at Transition Point
- **Relation**: **Strong support** -- sign reversal in pruning sensitivity directly analogous to our magnitude crossover
- **Gap**: Layer pruning (spatial), not temporal phase during generation

### 3.4 Doing More With Less: Revisiting LLM Pruning for Test-Time Scaling
- **Venue**: arXiv 2604.25098, 2026
- **Core**: Unstructured pruning + TTS can exceed unpruned baseline (Qwen3-8B); structured pruning catastrophically fails
- **Relation**: **Support** -- another performance inversion case; method that hurts in one regime helps in another

### 3.5 NSA: Native Sparse Attention (DeepSeek)
- **Venue**: ACL 2025 Best Paper
- **Core**: Hardware-aligned trainable sparse attention with dynamic hierarchical strategy (coarse compression + fine selection)
- **Relation**: **Background** -- demonstrates that sparse attention should be natively trained, not post-hoc; hierarchical strategy resonates with multi-phase approach

---

## 4. KV Cache Eviction Strategy Comparison

### 4.1 DefensiveKV: Taming the Fragility of KV Cache Eviction
- **Venue**: ICLR 2026
- **Core**: Reveals stability assumption (fixed important subset) is fragile; importance scores are highly non-stationary. Proposes defensive aggregation for worst-case risk control
- **Relation**: **Direct support** -- independently discovers importance-based methods fail under certain conditions due to non-stationarity; directly related to our crossover
- **Gap**: Statistical analysis, not phase-decomposed; no compound interaction

### 4.2 The Pitfalls of KV Cache Compression
- **Venue**: arXiv 2510.00231, 2025
- **Core**: In multi-instruction prompting, certain instructions degrade much more rapidly; compression method + instruction order bias interactions
- **Relation**: **Support** -- condition-dependent failure of uniform compression; analogous to phase-dependent failure

### 4.3 RetentiveKV: Uncertainty-Aware Multimodal KV Cache Eviction
- **Venue**: arXiv 2605.04075, 2026
- **Core**: "Deferred Importance" phenomenon -- tokens exhibit low initial salience but become pivotal at later timesteps
- **Relation**: **Strong support** -- directly relevant; importance scores computed early mislead later-phase utility

### 4.4 More Than a Quick Glance: Overcoming Greedy Bias in KV-Cache Compression
- **Venue**: arXiv 2602.02199, 2026
- **Core**: Single attention-score metric is "greedy" -- misses structurally relevant tokens; proposes multi-metric scoring
- **Relation**: **Support** -- single metric failure under certain conditions is our crossover in metric space

### 4.5 Ada-KV: Adaptive Budget Allocation for KV Cache Eviction
- **Venue**: NeurIPS 2025
- **Core**: Per-head adaptive budget based on attention pattern concentration
- **Relation**: **Method-component** -- per-head adaptation is spatial analog of our per-phase adaptation

### 4.6 SqueezeAttention: 2D Management of KV-Cache
- **Venue**: ICLR 2025
- **Core**: Joint layer-wise + sequence-wise budget optimization; layers categorized by cosine similarity
- **Relation**: **Method-component** -- 2D optimization (layer x sequence); we add 3rd dimension (temporal phase)

### 4.7 The Sparse Frontier: Sparse Attention Trade-offs
- **Venue**: arXiv 2504.17768, 2025
- **Core**: No universal optimal sparse attention strategy; optimal trade-off depends on task and phase (prefilling vs decoding)
- **Relation**: **Support** -- confirms strategy optimality is condition-dependent

### 4.8 MixedDimKV: Beyond Token Eviction
- **Venue**: arXiv 2603.20616, 2026
- **Core**: Allocates dimensions to tokens at granular level (not binary keep/evict); full attention quality at 6.25% cache
- **Relation**: **Method-component** -- continuous budget allocation enables smooth phase transitions

### 4.9 OBCache: Optimal Brain KV Cache Pruning
- **Venue**: arXiv 2510.07651, 2025
- **Core**: Second-order Taylor for joint K-V pruning saliency; key-pruning impacts more than value-pruning
- **Relation**: **Method-component** -- principled saliency; K vs V asymmetry potentially phase-dependent

---

## 5. Magnitude Crossover / Performance Inversion

### 5.1 Phase Transitions in Large Language Model Compression
- **Authors**: Ma et al.
- **Venue**: npj Artificial Intelligence (Nature), 2026
- **Core**: Universal phase transition boundaries; structured 30-45% collapse, unstructured 55-65%. Multi-dimensional PTP orthogonal -- joint safe zone achievable but narrow
- **Relation**: **Direct support** -- phase transitions per axis are independent; crossing one PTP while another is safe explains our crossover

### 5.2 Phase Transitions in Neural Networks Pruning (Thermodynamic)
- **Venue**: arXiv 2602.15224, 2026
- **Core**: Free-energy transition predicts sharp collapse; 3-5% stable before, 30%+ drop after
- **Relation**: **Support** -- our crossover may be importance-method crossing PTP while random stays below

### 5.3 UniComp: Unified Evaluation of LLM Compression
- **Authors**: Wang et al.
- **Venue**: arXiv 2602.09130, 2026
- **Core**: 40+ benchmarks; compression has consistent knowledge bias -- reasoning/multilingual degrade most
- **Relation**: **Background** -- compression effects are task-dependent; supports per-phase evaluation

---

## 6. Novelty Assessment

### KNOWN in the literature:
1. Compound compression error is non-additive / super-additive (SparK, SLiM)
2. Importance scores are non-stationary during generation (RaaS, DefensiveKV, RetentiveKV)
3. Phase transitions exist independently per compression axis (Ma et al., arXiv 2602.15224)
4. Adaptive budget allocation outperforms uniform (Ada-KV, LAVa, SqueezeAttention, Twilight)
5. Reasoning has discrete information phases with different computational needs (MI peaks, milestone tokens)
6. Fixed sparsity strategies fail under certain conditions (Sparse Frontier, Pitfalls)

### NOT known -- our novelty gap:
1. **Magnitude crossover in compound sparsity**: No paper reports importance-based eviction dramatically superior at one phase but catastrophically inferior at another within compound sparsity. DefensiveKV identifies fragility but not compound x phase interaction.
2. **Phase gradient asymmetry (900x)**: The quantitative finding that importance method's sensitivity to phase is ~900x random's gradient is unprecedented.
3. **Phase-gated compound controller**: No existing work proposes switching eviction strategy (not just budget) based on reasoning phase in compound sparsity context.
4. **Interaction-aware phase boundaries**: Existing phase-adaptive methods (RaaS, ThinKV) adapt budget within one axis; none address how boundaries should differ when multiple axes interact.

### Closest competitors:
| Paper | Threat Level | Why not a blocker |
|-------|-------------|-------------------|
| ThinKV (ICLR 2026 Oral) | High | Phase-based but single compression axis |
| DefensiveKV (ICLR 2026) | Medium | Importance instability but no compound or phase decomposition |
| GRASPrune (ACL 2026) | Medium | Joint compound pruning but static, no phase |
| SparK (AAAI 2026) | Medium | Compound super-additivity but no phase analysis |

### Conclusion
The magnitude crossover phenomenon in compound sparsity -- where the optimal strategy flips between reasoning phases -- is a genuinely novel finding. The closest observations are: (a) DefensiveKV's fragility (statistical, not phase-decomposed), (b) RaaS's milestone tokens (single axis), and (c) phase transition theory (per-axis thresholds). Our contribution unifies these into a compound x phase interaction framework with quantitative crossover evidence.
