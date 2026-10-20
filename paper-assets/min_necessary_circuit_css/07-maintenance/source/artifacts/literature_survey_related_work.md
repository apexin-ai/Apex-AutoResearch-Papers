# Related Work Literature Survey for CSS (Cross-method Structural Consensus)

> Generated: 2026-05-13 | Target: EMNLP 2026 Main (ARR deadline 2026-05-25)

---

## Direction 1: Cross-method Consensus / Ensemble in Mechanistic Interpretability

### 1.1 CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles
- **Authors:** Swapnil Parekh
- **Year:** 2026 (arXiv: 2603.00523)
- **Venue:** arXiv preprint (Feb 2026)
- **Core findings:** Reframes circuit discovery as an uncertainty-quantification problem. Constructs an ensemble of attribution graphs by pruning a *single* raw attribution run under multiple threshold configurations, assigns each edge a stability score (fraction of configs retaining it), and extracts a strict-consensus circuit (edges appearing in all views). On Gemma-2-2B and Llama-3.2-1B, strict consensus circuits are ~40× smaller than the union while retaining comparable explanatory power. Consensus-identified nodes beat matched non-consensus controls in causal relevance (p=0.0004).
- **Relation to CSS:** **直接竞争 (Primary competitor)**. CIRCUS varies pruning thresholds on a single attribution method to build consensus; CSS uses multiple independent discovery methods (EAP-IG, EP, ACDC/IFR). Key differentiators: (1) CSS captures cross-method agreement (different algorithms with different inductive biases), not just threshold robustness within one method; (2) CSS uses binary agreement rather than fractional stability scores; (3) CSS explicitly tests distribution-shift robustness. Must position CSS as complementary/stronger: method diversity > threshold diversity.

### 1.2 Certified Circuits: Stability Guarantees for Mechanistic Circuits
- **Authors:** Alaa Anani, Tobias Lorenz, Bernt Schiele, et al.
- **Year:** 2026 (arXiv: 2602.22968)
- **Venue:** arXiv preprint (Feb 2026)
- **Core findings:** Wraps any black-box discovery algorithm with randomized data subsampling to certify that circuit component inclusion decisions are invariant to bounded edit-distance perturbations of the concept dataset. On ImageNet with ResNet-101, certified circuits achieved 96% accuracy vs 86% baseline using half the neurons. Addresses dataset-to-circuit instability.
- **Relation to CSS:** **互补 (Complementary)**. Certified Circuits focuses on data perturbation stability for vision models with formal guarantees; CSS focuses on method-agreement stability for language model circuits. Both address instability but from orthogonal angles. Could cite as motivation for why stability matters.

### 1.3 Open Problems in Mechanistic Interpretability
- **Authors:** Lee Sharkey, Bilal Chughtai, Joshua Batson, et al. (29 authors, 18 organizations)
- **Year:** 2025 (arXiv: 2501.16496)
- **Venue:** arXiv preprint (Jan 2025), commissioned by Schmidt Sciences
- **Core findings:** Landmark collaborative paper establishing the field's consensus open problems. Highlights systematic non-identifiability: multiple circuits, features, and algorithm mappings can yield the same behavioral fidelity. Advocates reporting explanation ensembles and clarifying pragmatic vs. unicity criteria.
- **Relation to CSS:** **支持 (Supports CSS)**. Directly motivates multi-method consensus: if circuits are non-unique, reporting ensembles and agreement is essential. CSS operationalizes this recommendation.

### 1.4 Circuit Tracing: Revealing Computational Graphs in Language Models
- **Authors:** Anthropic (Dario Amodei team)
- **Year:** 2025
- **Venue:** Anthropic Technical Report (March 2025)
- **Core findings:** Uses cross-layer transcoders to build attribution graphs—graphical representations of computational steps where nodes are features and edges are causal interactions. Open-sourced circuit tracing tools supporting Gemma-2-2B, Llama-3.1-1B, Qwen3-4B.
- **Relation to CSS:** **互补 (Complementary)**. Provides a different paradigm (feature-level circuits via transcoders vs. component-level circuits). CSS methods operate at edge/component level; circuit tracing works at feature level. Represents a parallel direction worth acknowledging.

---

## Direction 2: Circuit Faithfulness Evaluation

### 2.1 Transformer Circuit Faithfulness Metrics Are Not Robust
- **Authors:** Joseph Miller, Bilal Chughtai, William Saunders
- **Year:** 2024
- **Venue:** COLM 2024
- **Core findings:** Faithfulness scores are highly sensitive to seemingly insignificant ablation methodology choices. Edge-level vs node-level ablation, resample vs mean ablation, and other methodological variations yield substantially different faithfulness percentages. Existing circuit faithfulness scores reflect researcher methodology as much as actual circuit quality.
- **Relation to CSS:** **强支持 (Strongly supports CSS)**. Core motivation for CSS: if single-method faithfulness metrics are unreliable, cross-method agreement provides a more robust signal. Directly supports the claim that binary consensus is more stable than score-dependent evaluation.

### 2.2 Have Faith in Faithfulness: Going Beyond Circuit Overlap When Finding Model Mechanisms
- **Authors:** Michael Hanna, Sandro Pezzelle, Yonatan Belinkov
- **Year:** 2024
- **Venue:** COLM 2024 (also ICML 2024 MI Workshop Spotlight)
- **Core findings:** Introduces EAP-IG (EAP with integrated gradients) which finds more faithful circuits than EAP. Key finding: high node overlap ≠ high faithfulness. When comparing circuits, measuring overlap is no substitute for measuring faithfulness.
- **Relation to CSS:** **支持+基础方法 (Supports + foundational method)**. EAP-IG is one of CSS's three discovery methods. The finding that overlap ≠ faithfulness motivates CSS's use of faithfulness-based evaluation rather than simple circuit overlap metrics.

### 2.3 MIB: A Mechanistic Interpretability Benchmark
- **Authors:** Yoav Goldberg, Yonatan Belinkov, et al.
- **Year:** 2025–2026 (arXiv: 2504.13151)
- **Venue:** ICML 2025 / ICLR 2026
- **Core findings:** Establishes two evaluation tracks—circuit localization and causal variable localization—across diverse tasks and models. Attribution and mask optimization methods perform best on circuit localization. Supervised DAS significantly outperforms unsupervised SAE features for causal variable localization.
- **Relation to CSS:** **互补 (Complementary)**. Provides standardized evaluation framework. CSS could adopt MIB tasks/metrics for evaluation; MIB results contextualize method performance differences.

### 2.4 Functional Faithfulness in the Wild: Circuit Discovery with Differentiable Computation Graph Pruning
- **Authors:** Lei Yu, Jingcheng Niu, Zining Zhu, et al.
- **Year:** 2024 (arXiv: 2407.03779)
- **Venue:** arXiv preprint (July 2024)
- **Core findings:** Introduces DiscoGP—differentiable masking that prunes both weights and edges. Extracts sheaves preserving 93–100% model performance using only 1–7% of original weights/connections. Identifies that activation-patching-based circuits tend to be neither functionally faithful nor complete.
- **Relation to CSS:** **互补 (Complementary)**. Shows that weight+edge pruning yields more faithful circuits than edge-only approaches, further highlighting that methodology choices dramatically affect circuit quality—supporting CSS's cross-method approach.

---

## Direction 3: Binary vs Continuous Scoring in Circuit Discovery

### 3.1 Finding Transformer Circuits with Edge Pruning
- **Authors:** Adithya Bhaskar, Alexander Wettig, Dan Friedman, et al.
- **Year:** 2024
- **Venue:** NeurIPS 2024
- **Core findings:** Frames circuit discovery as gradient-based optimization with binary masks over edges. EP is considerably more faithful on IOI and Greater-Than than both ACDC and EAP, especially at higher sparsities. Scales effectively to 100K examples where it is fastest and most faithful.
- **Relation to CSS:** **基础方法+支持 (Foundational method + supports)**. EP is one of CSS's discovery methods. Uses binary masks (0/1) for edge inclusion—directly relevant to CSS's binary consensus. Shows binary edge selection can be highly faithful.

### 3.2 Attribution Patching Outperforms Automated Circuit Discovery
- **Authors:** Aaquib Syed, Can Rager, Arthur Conmy
- **Year:** 2024
- **Venue:** BlackboxNLP 2024 (NeurIPS Workshop)
- **Core findings:** A simple method based on attribution patching outperforms ACDC while requiring just two forward passes + one backward pass. However, EAP's first-order approximations show lower faithfulness to the full model than EP.
- **Relation to CSS:** **支持 (Supports)**. Documents that different methods (ACDC, EAP, EP) yield different circuits with different faithfulness levels—core motivation for cross-method consensus. Methods that are fast (EAP) and methods that are faithful (EP) produce systematically different results.

### 3.3 Discovering Transformer Circuits via a Hybrid Attribution and Pruning Framework (HAP)
- **Authors:** Adithya Bhaskar, Alexander Wettig, et al.
- **Year:** 2025 (arXiv: 2510.03282)
- **Venue:** NeurIPS 2025
- **Core findings:** Two-stage pipeline: EAP filters unimportant edges (continuous scores → top-k), then EP refines with binary masks. HAP is ≥46% faster than EP while maintaining high faithfulness. Preserves cooperative circuit components (e.g., S-inhibition heads) that EAP alone prunes at high sparsity.
- **Relation to CSS:** **互补 (Complementary)**. Shows that combining methods sequentially (EAP→EP) improves over either alone. CSS takes a different combination approach: run methods independently, then take binary consensus. Complementary philosophies of method combination.

### 3.4 Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models
- **Authors:** Samuel Marks, Can Rager, Eric Michaud, Yonatan Belinkov, David Bau, Aaron Mueller
- **Year:** 2025
- **Venue:** ICLR 2025 (Oral)
- **Core findings:** Uses SAEs to identify features, then discovers feature-level causal circuits. Small feature circuits (<100 nodes) explain a large proportion of model performance on subject-verb agreement. Introduces SHIFT for improving classifier generalization by ablating task-irrelevant features.
- **Relation to CSS:** **互补 (Complementary)**. Operates at feature level (SAE features) vs. CSS's component level (attention heads, MLPs). Shows that sparse/binary feature selection is powerful for circuit analysis. CSS could potentially extend to feature-level consensus in future work.

### 3.5 Transcoders Find Interpretable LLM Feature Circuits
- **Authors:** Jacob Dunefsky, Philippe Morel, et al.
- **Year:** 2024
- **Venue:** NeurIPS 2024
- **Core findings:** Transcoders approximate dense MLP layers with wider, sparsely-activating layers. On par with SAEs in sparsity, faithfulness, and interpretability. Applied to reverse-engineer circuits in GPT-2-small including novel insights on the greater-than circuit.
- **Relation to CSS:** **互补 (Complementary)**. Offers alternative circuit representation (feature-level via transcoders). Relevant as a potential additional discovery method for CSS.

---

## Direction 4: Instability / Unreliability of Single-method Circuit Discovery

### 4.1 Mechanistic Interpretability as Statistical Estimation: A Variance Analysis
- **Authors:** Maxime Méloux et al.
- **Year:** 2025–2026 (arXiv: 2510.00845, revised Feb 2026)
- **Venue:** arXiv preprint
- **Core findings:** Frames circuit discovery as a statistical estimation problem. Uncovers fundamental instability: single-input CMA scores exhibit high intrinsic variance—causal effects are volatile random variables, not fixed properties. Small perturbations in input data or hyperparameters yield vastly different circuits. Focuses on EAP and EAP-IG, systematically decomposing variance sources.
- **Relation to CSS:** **强支持 (Strongly supports CSS)**. Provides quantitative evidence that single-method circuits are unstable. Directly motivates CSS: if individual methods have high variance, cross-method consensus filters out method-specific noise.

### 4.2 Circuit Stability Characterizes Language Model Generalization
- **Authors:** Alan Sun
- **Year:** 2025
- **Venue:** ACL 2025
- **Core findings:** Mathematically formalizes circuit stability—a model's ability to apply a consistent reasoning process (circuit) across inputs. Through three case studies, shows circuit stability predicts different aspects of generalization. Models that lack circuit stability fail to generalize.
- **Relation to CSS:** **支持 (Supports)**. Establishes that circuit stability is a valuable property. CSS targets a complementary notion of stability: consistency across methods rather than across inputs.

### 4.3 Finding Highly Interpretable Prompt-Specific Circuits in Language Models
- **Authors:** Gabriel Franco, Lucas M. Tassis, Azalea Rohr, Mark Crovella
- **Year:** 2026 (arXiv: 2602.13483)
- **Venue:** arXiv preprint (Feb 2026)
- **Core findings:** Circuits are prompt-specific even within a fixed task. Applying ACC++ to IOI in GPT-2, Pythia, and Gemma 2: no single circuit for IOI in any model—different prompt templates induce systematically different mechanisms.
- **Relation to CSS:** **支持+挑战 (Supports + challenges)**. Supports CSS by showing single circuits are insufficient; challenges CSS to demonstrate that consensus circuits are more stable across prompts. CSS should test prompt-level robustness.

### 4.4 Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees
- **Authors:** Itamar Hadad, Guy Katz, Shahaf Bassan
- **Year:** 2026
- **Venue:** ICLR 2026
- **Core findings:** Leverages neural network verification to yield circuits with provable guarantees: input domain robustness, robust patching, and minimality. Prior methods depend on heuristics without guarantees over continuous input domains. Applied to vision models.
- **Relation to CSS:** **互补 (Complementary)**. Takes a formal verification approach to robustness; CSS takes an empirical consensus approach. Both address circuit reliability but through fundamentally different mechanisms. Currently limited to vision models.

### 4.5 Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition (CD-T)
- **Authors:** Adelaide Hsu et al.
- **Year:** 2025
- **Venue:** ICLR 2025
- **Core findings:** Uses mathematical decomposition (no approximations) for circuit discovery. Reduces runtime from hours to seconds vs ACDC. Achieves 97% ROC AUC on IOI, Greater-Than, and Docstring tasks. Compatible with all transformer types, no training required.
- **Relation to CSS:** **互补 (Complementary)**. Provides yet another discovery method with different inductive biases than EAP-IG/EP/ACDC—could be a candidate additional method for CSS's ensemble.

### 4.6 Towards Automated Circuit Discovery for Mechanistic Interpretability (ACDC)
- **Authors:** Arthur Conmy, Augustine N. Mavor-Parker, Aaquib Lynch, Stefan Heimersheim, Adrià Garriga-Alonso
- **Year:** 2023
- **Venue:** NeurIPS 2023
- **Core findings:** Foundational automated circuit discovery method using iterative activation patching. Effective but slow (runtime scales linearly with edges). Recovers IOI, Greater-Than, Docstring circuits. Establishes benchmark tasks for circuit discovery evaluation.
- **Relation to CSS:** **基础方法 (Foundational method)**. ACDC is one of CSS's three discovery methods for GPT-2 Small. Its different algorithmic approach (iterative patching vs. gradient-based) provides genuine method diversity in CSS's ensemble.

---

## Additional Relevant Work

### RelP: Faithful and Efficient Circuit Discovery via Relevance Patching
- **Authors:** Farnoush Rezaei Jafari et al.
- **Year:** 2025
- **Venue:** NeurIPS 2025 MechInterp Workshop (Spotlight)
- **Core findings:** Replaces gradients in attribution patching with LRP propagation coefficients. For MLP outputs in GPT-2 Large, attribution patching achieves Pearson correlation 0.006 vs. RelP's 0.956 with activation patching ground truth. Faithfulness comparable to IG at lower cost.
- **Relation to CSS:** **互补 (Complementary)**. Another discovery method with different inductive bias. Documents dramatic differences between methods on the same components—supports CSS's premise.

---

## Key Takeaways for CSS Positioning

### 1. CSS fills a specific gap in the literature
The field has established that (a) circuit discovery methods disagree (Syed et al. 2024; Méloux et al. 2025), (b) faithfulness metrics are unreliable (Miller et al. 2024), and (c) circuits are sensitive to analyst choices (CIRCUS, Certified Circuits). CSS is the first to exploit **cross-method binary consensus** as a robustness mechanism, using method diversity rather than threshold/data perturbation diversity.

### 2. CIRCUS is the primary competitor — positioning is critical
CIRCUS (Parekh, 2026) is the closest work. Key differentiation:
- **CIRCUS:** varies pruning thresholds within one attribution method → threshold robustness
- **CSS:** uses multiple independent discovery methods → method robustness
- CSS argument: method diversity captures a broader space of inductive biases than threshold variation. A threshold ensemble still inherits the blind spots of its single underlying attribution method (e.g., EAP's first-order approximation errors). CSS's methods have structurally different failure modes (gradient-based vs. iterative patching vs. similarity-based).

### 3. The "instability problem" is well-documented — CSS offers a practical solution
Multiple papers (Méloux et al., Franco et al., Miller et al.) document that circuits are unstable across data, prompts, and methodology. The Open Problems paper (Sharkey et al. 2025) explicitly calls for reporting ensembles. CSS directly operationalizes this recommendation with a concrete, lightweight algorithm.

### 4. Binary scoring is underexplored relative to continuous scoring
Most methods produce continuous importance scores (EAP, EAP-IG, CD-T) and require threshold selection. Edge Pruning uses binary masks but within a single optimization. CSS's binary consensus (edge included/excluded per method → majority vote) is a distinct aggregation strategy that avoids score calibration issues across methods with incomparable scales.

### 5. Distribution-shift robustness is a novel evaluation angle
No existing work systematically evaluates whether consensus circuits maintain faithfulness under distribution shift. CSS's off-diagonal evaluation (train on distribution A, test on distribution B) is a distinctive contribution.

### 6. Recommended related work structure for the paper
1. **Circuit discovery methods** (ACDC, EAP-IG, EP, CD-T, HAP) — establish method landscape
2. **Faithfulness evaluation** (Miller et al. 2024, Hanna et al. 2024) — motivate robustness concerns
3. **Circuit instability** (Méloux et al. 2025, Franco et al. 2026, Sun 2025) — establish the problem CSS solves
4. **Consensus/stability approaches** (CIRCUS, Certified Circuits) — position CSS against alternatives
5. **Feature-level circuits** (Sparse Feature Circuits, Transcoders, Circuit Tracing) — acknowledge parallel direction, note CSS works at component level
