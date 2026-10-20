# Research conversation: I need you to help me compose a large JSON object. I'll provide the complete content and you should output it as valid J

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 4
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ad6f042dde204c722.jsonl`
- **Structured JSON:** [`2adcacddc0e144d38edb.json`](../../sessions/2a/2adcacddc0e144d38edb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

4 recorded events

### User

_source line 1 · 2026-05-27T20:41:24.359Z_

I need you to help me compose a large JSON object. I'll provide the complete content and you should output it as valid JSON. This is a research idea revision. Here are the key changes I need incorporated:

Please output the following JSON exactly (I'll provide the full text). Just format it as clean JSON:

```json
{
  "title": "Proof-Structure Fingerprinting for Autoformalization Semantic Verification",
  "change_type": "major",
  "revision_notes": {
    "critical_1_hallucinated_statistic": "Removed the fabricated '80%+ of unsolved problems are due to formalization errors' claim attributed to Goedel-Prover-V2. Replaced with properly sourced evidence from the FATE benchmark (ICLR 2026): on FATE-H, DeepSeek-R1 achieves 71% natural-language reasoning accuracy but 0% formal proving accuracy; DeepSeek-Prover-V2 achieves 39% NL but only 3% formal. This demonstrates formalization quality — not mathematical reasoning — is the primary bottleneck, with Mathlib hallucinations and Lean proficiency issues appearing in nearly every failed proof attempt.",
    "critical_2_outdated_SOTA": "Updated from Goedel-Prover-V2-32B (88.1%) to reflect current landscape: Seed-Prover (99.6% MiniF2F-test, July 2025) saturates MiniF2F; Seed-Prover 1.5 (Dec 2025) solves 88% PutnamBench, 80% FATE-H, 33% FATE-X; BFS-Prover-V2-32B (95.08% MiniF2F-test, open-source weights on HuggingFace) is used as our open-source prover. MiniF2F near-saturation motivated the shift to harder benchmarks.",
    "critical_3_domain_mismatch": "Removed 'Do LLMs Game Formalization?' as ground truth. That paper evaluates on FOLIO/Multi-LogiEval (first-order logic, not math) and actually found NO evidence of systematic gaming. Replaced with: (a) FATE benchmark for formalization-as-bottleneck motivation, (b) Lean Atlas's five hallucination patterns for taxonomy, (c) synthetic unfaithful formalization generation via systematic statement weakening.",
    "major_4_missing_aria": "Added Aria (ICLR 2026) with detailed differentiation: Aria uses statement-level dependency decomposition for generation (Graph-of-Thought + AriaScorer retrieves Mathlib definitions for term-level grounding), while we analyze proof-level dependencies post-hoc for verification. These are complementary — Aria ensures correct concepts enter the formalization; we verify the proof reveals the formalization actually captured the intended mathematics.",
    "major_5_tactic_automation": "Addressed the fundamental challenge of automation tactics (simp, omega, aesop, decide) hiding true dependencies. Solution: analyze kernel-level elaborated proof terms rather than surface tactic scripts. Lean 4 elaborates all tactic proofs into fully-explicit Expr terms that the trusted kernel type-checks. We extract all referenced constants from these elaborated terms via recursive Expr traversal (cf. lean-training-data's premise extraction approach, which already prefixes simp-used constants with 's'). This transforms the challenge into a strength — we capture the TRUE dependency set that even the user cannot see from the tactic script.",
    "moderate_6_benchmark_saturation": "Shifted primary evaluation from MiniF2F (saturated at 99.6%) to MathAtlas (52K theorems, 178K dependency relations, 87 math areas, best model at 9.8% correctness — far from saturated). Added FATE-H/FATE-X (where formalization bottleneck is documented) and PutnamBench. MiniF2F retained only as sanity-check validation.",
    "moderate_7_missing_pseudo_formalization": "Added Pseudo-Formalization (Stanford, May 2026) to landscape. Differentiation: PF verifies informal proof correctness via natural-language Block Verification (no formal proof assistant needed); we verify formal proof semantic faithfulness by analyzing the Lean kernel proof term's dependency footprint. Different verification targets (proof correctness vs. formalization faithfulness) and different substrates (NL vs. formal).",
    "minor_8_mathlib_clustering": "Replaced untested unsupervised clustering with Mathlib's existing hierarchical module structure as the domain taxonomy. Mathlib organizes 274K+ theorems and 130K+ definitions into a well-curated hierarchy (Algebra, Topology, Analysis, Combinatorics, etc.) with ~70 second-level subdivisions (Algebra.Group, Topology.MetricSpace, Analysis.NormedSpace, etc.). This is a principled, human-curated taxonomy that eliminates the clustering quality concern entirely.",
    "R2_moderate_9_formalalign": "Added FormalAlign (ICLR 2025) to landscape with detailed differentiation. FormalAlign evaluates statement-pair alignment via a dual loss combining cross-entropy (certainty score measuring prediction confidence) and contrastive learning (similarity score measuring embedding alignment), achieving 99.21% alignment-selection on FormL4-Basic and 66.39% on MiniF2F-Valid but only 65% correctness vs. 79.58% human experts. Key distinction: FormalAlign scores NL↔FL statement pairs without examining proofs; PFS analyzes the kernel-level proof term's dependency domain signature. These are complementary — FormalAlign catches surface-level statement misalignment; PFS catches cases where a statement appears aligned but the proof reveals it captures weaker/different mathematics. PFS could serve as a second-stage filter after FormalAlign's first-stage screening.",
    "R2_moderate_10_false_positives": "Addressed the false positive problem from unexpected proof strategies with quantitative evidence from 'The Network Structure of Mathlib' (arXiv 2604.24797, April 2026). That analysis of 308K declarations and 8.4M edges found 50.9% of declaration-level edges cross namespace boundaries and only 0.34 NMI between naming conventions and dependency-based communities — confirming that cross-domain proofs are pervasive. However, the same paper reveals that 74.2% of all dependency edges are invisible compiler-synthesized infrastructure (typeclass resolution, coercions, automatic instances), not mathematical content. Our revised approach: (1) filter infrastructure edges by excluding compiler-synthesized dependencies, focusing on the ~25.8% of explicit mathematical-content edges that carry domain-specific signal; (2) leverage the paper's finding that 43.9% of edges are proof-only (not in the statement) — these proof-only dependencies are exactly the novel signal PFS exploits; (3) train the domain-signature predictor to output mixture distributions (Dirichlet-multinomial) rather than point predictions, acknowledging that problems may have legitimate multi-domain proof strategies; (4) compute domain-specific calibration thresholds using Mathlib's own theorems (some domains like Analysis.NormedSpace are inherently cross-domain, others like Combinatorics.SimpleGraph are more self-contained); (5) add a pilot measurement of the false-positive base rate by sampling 200 Mathlib theorems, comparing predicted vs. actual domain signatures, and reporting the rate of 'surprising but faithful' divergence. If this rate exceeds 15%, the JSD component alone is insufficient and the proof-complexity anomaly features (proof term size, dependency depth, distinct module count relative to problem difficulty) become the primary signal.",
    "R2_moderate_11_training_data": "Validated and corrected the ~50K Mathlib docstring claim. Mathlib's docBlame linter requires docstrings for definitions (~131K) but docBlameThm only encourages (not requires) docstrings for theorems (~275K). No public statistics exist on theorem docstring coverage, and the actual number with adequate NL descriptions is likely far below 50K. Revised training data strategy to use multiple complementary sources: (a) Herald dataset (ICLR 2025): 110K Mathlib4 theorems with LLM-generated NL annotations via hierarchical informalization, plus 44K NL-FL proof pairs — this is the primary training source; (b) LeanWorkbook (NeurIPS 2024): 57K NL-Lean pairs from AOPS competition problems; (c) Mathlib definitions with required docstrings (~131K) for supervised domain-signature learning; (d) Mathlib's own module structure as weak supervision — each theorem's module path provides a ground-truth 'home domain' that can bootstrap the predictor. Combined training set: ~300K+ samples from diverse sources, far exceeding the original 50K claim. Training target is also clarified: we predict dependency domain distributions, not reconstruct full informal descriptions, so even terse theorem names and module paths are informative.",
    "R2_minor_12_mathatlas_unfaithful": "Removed the claim about collecting 'naturally-occurring unfaithful formalizations from MathAtlas's formalization attempts.' MathAtlas contains only informal mathematical entities from textbooks; it does not include pre-labeled failed or unfaithful formalization attempts in the released dataset. Ground truth unfaithful formalizations now come exclusively from: (i) systematic synthetic statement weakening, (ii) Lean Atlas hallucination pattern injection, and (iii) a new source: comparing model-generated formalizations against MathAtlas's MA-Align benchmark (200 entities with binary aligned/misaligned labels) to identify and collect naturally misaligned examples from model outputs.",
    "R2_minor_13_roundtrip_verification": "Removed 'Faithful Autoformalization via Roundtrip Verification and Repair' from key references. That paper evaluates exclusively on Texas statutory text (150 traffic rules + 77 parks/wildlife rules) using many-sorted first-order logic with Z3 SMT solver — the authors explicitly state they 'do not claim the framework transfers to other genres.' Its roundtrip verification concept (formalize → informalize → re-formalize → check equivalence) is interesting but operates on a fundamentally different domain and formalism than mathematical theorem proving in Lean 4."
  },
  "core_problem": "Autoformalization quality is the binding constraint in formal theorem proving: on the FATE-H benchmark, models achieve 39-71% natural-language reasoning accuracy but only 0-3% formal proving accuracy, with Mathlib hallucinations and Lean proficiency issues appearing in nearly every failed attempt (FATE, ICLR 2026). Yet current verification methods check only syntactic correctness (type-checking), not whether a formalization semantically captures the intended mathematics. Existing automated alignment evaluation (FormalAlign, ICLR 2025) scores statement-pair alignment via learned embeddings but does not examine what the proof itself reveals about semantic faithfulness. Can we use the structure and complexity of a proof itself — specifically its dependency footprint over the mathematical library — as a post-hoc signal to detect semantically unfaithful formalizations?",
  "opportunity": "The FATE benchmark (ICLR 2026) demonstrated that formalization, not reasoning, is the primary bottleneck: models with strong informal reasoning systematically fail at faithful formalization into Lean 4. Lean Atlas (April 2026) catalogued five specific hallucination patterns (definition mismatches, missing assumptions, goal substitution, quantifier errors, type default semantic shifts) that survive type-checking. FormalAlign (ICLR 2025) automates statement-pair alignment scoring via dual embedding+generation loss (99.21% on FormL4-Basic) but operates only on statements, achieving just 65% correctness vs. human experts on subtle cases — it cannot examine whether the proof actually engages the expected mathematics. Other approaches use LLM-as-judge (ReForm, +22.6pp but inherently noisy), statement-level dependency decomposition for grounded generation (Aria, ICLR 2026, 68.5% accuracy on ProofNet), embedding-based retrieval (ProofBridge), structural fidelity metrics (ProofFlow, ProofScore 0.545 vs 0.123 baseline), or natural-language Block Verification (Pseudo-Formalization, Stanford May 2026). None exploit a key insight: the kernel-level proof term's Mathlib dependency footprint encodes what mathematics the formalization actually captures. Recent network analysis of Mathlib (April 2026) reveals that 43.9% of proof dependencies are proof-only — absent from the statement entirely — meaning the proof carries rich information about mathematical content that statement-level methods fundamentally cannot access. If an olympiad combinatorics problem is formalized and proved using only basic arithmetic lemmas from Mathlib.Algebra.Order, the formalization almost certainly captured a weaker statement — regardless of whether the tactic script looks reasonable or whether a statement-level alignment scorer rates it as aligned.",
  "landscape": "The FATE benchmark (ICLR 2026) establishes that on graduate/PhD-level algebra problems, formalization quality is the primary bottleneck: 71% NL accuracy drops to 0% formal accuracy for DeepSeek-R1 on FATE-H. FormalAlign (ICLR 2025) is the closest prior work on automated semantic alignment evaluation: it trains a dual-loss model (cross-entropy certainty + contrastive similarity) to score NL↔FL statement pairs, achieving 99.21% alignment-selection on FormL4-Basic and 66.39% on MiniF2F-Valid, but operates only at statement level and reaches 65% correctness vs. 79.58% human experts. ReForm (Feb 2026) uses reflective self-correction with LLM-as-judge, achieving 22.6pp improvement but relying on noisy LLM evaluation. CRAMF uses retrieval of Mathlib definitions to ground generation (up to 62.1% relative improvement). Aria (ICLR 2026) introduces a two-phase Graph-of-Thought system with AriaScorer that retrieves Mathlib definitions for term-level grounding, achieving 91.6% compilation and 68.5% accuracy on ProofNet and 44.0% on FATE-X; critically, Aria decomposes statement-level dependencies for generation, not proof-level dependencies for post-hoc verification. ProofFlow (ICLR 2026) introduces ProofScore combining syntactic, semantic, and structural fidelity metrics (0.545 vs 0.123 baseline), using dependency DAGs for structuring proof generation but not as a post-hoc semantic verifier. ProofBridge improves cross-modal retrieval by 3.28x over all-MiniLM-L6-v2 and achieves +31.14% semantic correctness. Pseudo-Formalization (Stanford, May 2026) verifies informal proof correctness via natural-language Block Verification, pareto-dominating LLM-as-judge baselines — but operates on natural language proofs, not formal proof terms. Lean Atlas (April 2026) classifies dependency graph edges (type vs. value) for human-AI collaborative verification but requires human review. The Network Structure of Mathlib (April 2026) provides crucial empirical context: 50.9% of declaration-level edges cross namespace boundaries and 74.2% are compiler-synthesized infrastructure, revealing that mathematical dependencies are heavily entangled but largely through automated mechanisms rather than mathematical content — a finding we exploit by filtering infrastructure edges to isolate content-level domain signals. MathAtlas (May 2026) introduces dependency-graph-enriched benchmarks (~178K relations, 87 math areas) but does not use dependencies as a verification signal. FormalEvolve (March 2026) addresses semantic drift via evolutionary search. FormaRL uses dual rewards (compiler + LLM comparison). Direct Dependency Retrieval improves autoformalization by retrieving Mathlib dependencies at generation time. The missing piece: no existing work extracts the elaborated proof term's mathematical-content dependency set (filtering compiler-synthesized infrastructure), compares its domain distribution against what the informal problem predicts, and uses proof-only dependencies — which constitute 43.9% of all edges — as a novel semantic faithfulness signal unavailable to any statement-level method.",
  "inspired_by": "FATE benchmark finding that formalization is the primary bottleneck (71% NL → 0% formal on FATE-H) + FormalAlign's demonstration that statement-level alignment evaluation reaches only 65% of human accuracy (leaving room for proof-level signals) + The Network Structure of Mathlib's finding that 43.9% of proof dependencies are proof-only and 74.2% are infrastructure (enabling infrastructure filtering for cleaner domain signals) + Lean Atlas's five hallucination patterns surviving type-checking + Aria's demonstration that dependency graphs improve autoformalization quality + pattern 'Verifier-as-Swiss-Army-Knife' (using verifier-derived signals for data quality filtering) + lean-training-data's premise extraction showing that elaborated proof term dependencies are extractable including simp-used constants",
  "approach": "Build a proof-structure fingerprinting pipeline in four phases:\n\nPhase 0 — Pilot Validation with False-Positive Measurement (weeks 1-3): Validate the core hypothesis AND measure the false-positive base rate. (a) Select 200 Mathlib theorems stratified across 10+ mathematical domains, extract their elaborated proof term dependencies, filter compiler-synthesized infrastructure edges (74.2% of all edges per Network Structure of Mathlib), and compute dependency domain signatures over Mathlib's module hierarchy. Compare each theorem's informal description (from Herald annotations or theorem name) against its actual filtered dependency signature. Measure the rate of 'surprising but faithful' domain divergence — theorems whose proofs legitimately draw from unexpected domains. This establishes the false-positive base rate. (b) From a 50-theorem subset with known faithful formal-informal pairs, generate 3 unfaithful variants each via systematic statement weakening (drop hypotheses, weaken quantifiers, substitute weaker type constraints — mirroring Lean Atlas's five hallucination patterns). Prove all versions with BFS-Prover-V2-32B. Show statistically significant divergence (Mann-Whitney U test) between faithful and unfaithful formalization proofs on infrastructure-filtered domain signatures. If Cohen's d < 0.5, pivot or abandon. If false-positive base rate >15%, the JSD component alone is insufficient — proceed with emphasis on proof-complexity anomaly features and multi-modal prediction.\n\nPhase 1 — Dependency Extraction with Infrastructure Filtering (weeks 2-4): Build a Lean 4 metaprogram that, given a completed proof, (a) extracts the fully-elaborated kernel proof term (which resolves all tactic automation — simp, omega, aesop, decide — into explicit constant references), (b) recursively traverses the Expr to collect all referenced Mathlib constants (using ConstantInfo lookups in the Environment), (c) classifies each edge as explicit-content vs. compiler-synthesized (leveraging the Lean elaborator's provenance information to distinguish user-written references from typeclass resolution, coercions, and automatic instances), and (d) maps each content-level constant to its Mathlib module path. This infrastructure filtering is a key technical contribution informed by the Network Structure of Mathlib's finding that 74.2% of edges are invisible infrastructure — removing these dramatically improves the domain-signal-to-noise ratio.\n\nPhase 2 — Multi-Modal Domain Signature Prediction (weeks 3-7): Using Mathlib's hierarchical module structure as a natural domain taxonomy (~70 second-level categories), compute 'dependency domain signatures' — normalized distribution vectors over module categories — for each proof's infrastructure-filtered dependencies. Train a domain-signature predictor using multiple complementary data sources: (a) Herald's 110K Mathlib4 theorem NL annotations (ICLR 2025) as primary training data — these are LLM-generated informalizations with hierarchical dependency context, paired with actual dependency signatures extracted in Phase 1; (b) LeanWorkbook's 57K NL-Lean pairs from competition problems; (c) Mathlib's ~131K definitions with required docstrings; (d) Mathlib's module structure as weak supervision — each theorem's module path provides ground-truth 'home domain' bootstrapping. Total: ~300K+ training samples. Crucially, the predictor outputs Dirichlet-multinomial mixture distributions rather than point predictions, acknowledging that problems may have legitimate multi-domain proof strategies (e.g., analytic number theory proofs that necessarily span Number Theory + Analysis + Topology). Additionally, compute domain-specific calibration thresholds: some Mathlib areas (e.g., Analysis.NormedSpace, Topology.Algebra) are inherently cross-domain with wide dependency spreads, while others (Combinatorics.SimpleGraph, Data.Nat.Prime) are more self-contained — calibration accounts for this structural variation.\n\nPhase 3 — Proof Fingerprint Score and Evaluation (weeks 5-10): Define the Proof Fingerprint Score (PFS) combining three signal types: (a) Infrastructure-Filtered Domain JSD: Jensen-Shannon divergence between predicted and actual dependency domain signatures after infrastructure filtering, with domain-specific calibration thresholds; (b) Proof-Complexity Anomaly Features: proof term size, maximum dependency depth, and number of distinct Mathlib modules invoked, each relative to estimated problem difficulty — these features are robust to cross-domain proofs since unfaithful formalizations tend to have systematically shorter/simpler proofs regardless of domain; (c) Proof-Only Dependency Ratio: the fraction of proof dependencies absent from the statement, leveraging the finding that 43.9% of edges are proof-only — unfaithful formalizations that trivialize a problem should show atypical proof-only dependency patterns. Evaluate on: (a) MathAtlas — primary benchmark (52K theorems, 178K dependency relations, 87 math areas; best existing model at 9.8% correctness), selecting ~500 theorems with proofs and generating synthetic unfaithful variants; (b) FATE-H/FATE-X — where formalization bottleneck is documented, using the two-stage evaluation to compare NL-correct-but-formally-wrong attempts; (c) PutnamBench — undergraduate competition problems in Lean 4; (d) MiniF2F — retained only as sanity-check validation. Ground truth unfaithful formalizations generated via: (i) systematic statement weakening (drop hypotheses, weaken bounds, simplify quantifiers, substitute weaker types), (ii) Lean Atlas hallucination pattern injection (definition mismatches, missing assumptions, goal substitution, quantifier errors, type default shifts), and (iii) collecting naturally misaligned model outputs by evaluating against MathAtlas's MA-Align benchmark (200 entities with binary aligned/misaligned labels). Use BFS-Prover-V2-32B (95.08% MiniF2F-test, open-source weights) for proof generation. Report false-positive rates alongside detection accuracy, broken down by mathematical domain. Demonstrate PFS as a plug-in verifier yielding complementary gains atop FormalAlign (+statement-level alignment), ReForm (+LLM-as-judge), Aria (+statement-level grounding), and ProofFlow (+structural DAG).",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "650",
      "timeline": "13 weeks",
      "estimated_gpu_cost": "$1,300"
    },
    "human_in_loop": {
      "gpu_hours": "450",
      "timeline": "11 weeks",
      "claude_api_cost": "$550",
      "estimated_gpu_cost": "$900"
    },
    "auto_research": {
      "gpu_hours": "450",
      "timeline": "7 weeks",
      "claude_api_cost": "$1,300",
      "estimated_gpu_cost": "$900",
      "speed_bottleneck": "Lean 4 kernel elaboration and type-checking is sequential and CPU-bound (5-60s per proof); dependency extraction with infrastructure classification over elaborated proof terms for the evaluation set (~2K proofs × 4 variants = 8K total) takes ~3 days on a 32-core server; proof search with BFS-Prover-V2-32B at pass@32 over ~2K problems requires ~150 A100-hours of inference; MathAtlas dependency graph processing for ~178K relations is a one-time ~12hr computation; Herald dataset integration and multi-source training data preparation adds ~1 week; false-positive base rate measurement on 200 Mathlib theorems adds ~2 days of extraction + analysis"
    }
  },
  "target_venues": [
    "ICLR 2027 (expected ~October 2026)",
    "AAAI 2027 (full paper deadline: July 28, 2026 — tight but feasible if pilot succeeds quickly)",
    "EACL 2027 via ARR August cycle (deadline: August 3, 2026)"
  ],
  "level": "solid-to-strong",
  "key_references": [
    "FATE: A Formal Benchmark Series for Frontier Algebra of Multiple Difficulty Levels (ICLR 2026) — primary evidence that formalization is the bottleneck",
    "FormalAlign: Automated Alignment Evaluation for Autoformalization (ICLR 2025) — closest prior work on automated semantic alignment; statement-level dual-loss alignment scoring",
    "Aria: An Agent for Retrieval and Iterative Auto-Formalization via Dependency Graph (ICLR 2026) — statement-level dependency decomposition for generation",
    "ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization (ICLR 2026) — ProofScore for structural fidelity",
    "The Network Structure of Mathlib (arXiv 2026) — quantitative analysis: 50.9% cross-namespace edges, 74.2% compiler-synthesized infrastructure, 43.9% proof-only dependencies",
    "Herald: A Natural Language Annotated Lean 4 Dataset (ICLR 2025) — 110K Mathlib4 theorem NL annotations via hierarchical informalization; primary training data source",
    "Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction (ICLR 2026) — autoformalization pipeline",
    "Seed-Prover: Deep and Broad Reasoning for Automated Theorem Proving (arXiv 2025) — saturates MiniF2F at 99.6%",
    "Seed-Prover 1.5: Mastering Undergraduate-Level Theorem Proving via Learning from Experience (arXiv 2025) — 88% PutnamBench, 80% FATE-H",
    "BFS-Prover-V2: Scalable Best-First Tree Search for Theorem Proving (arXiv 2026) — open-source SOTA step-prover, 95.08% MiniF2F",
    "Pseudo-Formalization for Automatic Proof Verification (arXiv 2026, Stanford) — NL Block Verification pareto-dominating LLM-as-judge",
    "Lean Atlas: An Integrated Proof Environment for Scalable Human-AI Collaborative Formalization (arXiv 2026) — five hallucination patterns, dependency edge classification",
    "ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization (arXiv 2025) — LLM-as-judge baseline",
    "MathAtlas: A Benchmark for Autoformalization in the Wild (arXiv 2026) — 52K theorems, 178K dependency relations, MA-Align benchmark",
    "Lean Workbook: A large-scale Lean problem set formalized from natural language math problems (NeurIPS 2024) — 57K NL-Lean pairs; training data source",
    "Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning (VerifAI Workshop, ICLR 2026) — cited for semantic gap finding in FOL domain only",
    "ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings (arXiv 2025) — cross-modal retrieval",
    "FormalEvolve: Neuro-Symbolic Evolutionary Search for Diverse and Prover-Effective Autoformalization (arXiv 2026)",
    "LeanDojo: Theorem Proving with Retrieval-Augmented Language Models (NeurIPS 2023)",
    "Improving Autoformalization Using Direct Dependency Retrieval (arXiv 2025)"
  ],
  "description": "Autoformalization — translating informal mathematics into machine-verifiable code — suffers from a critical verification gap: syntactic correctness (type-checking) does not guarantee semantic faithfulness, with the FATE benchmark showing models achieve 39-71% natural-language reasoning accuracy but only 0-3% formal proving accuracy, formalization being the primary bottleneck. Existing automated alignment evaluation (FormalAlign, ICLR 2025) scores statement-pair alignment via learned embeddings (99.21% on FormL4-Basic) but examines only statements, not proofs, and achieves only 65% of human expert accuracy on subtle cases. We propose Proof-Structure Fingerprinting, a novel post-hoc verification method that exploits the kernel-level proof term itself as a semantic signal. Our key insight is that a proof's Mathlib dependency footprint — the complete set of library constants referenced in the elaborated proof term that the Lean 4 kernel type-checks — encodes rich information about what mathematical content the formalization actually captures. Crucially, recent network analysis of Mathlib reveals that 43.9% of proof dependencies are proof-only (absent from the statement), meaning proof-level analysis accesses semantic information fundamentally unavailable to any statement-level method. The same analysis shows 74.2% of all dependency edges are compiler-synthesized infrastructure (typeclass resolution, coercions); we filter these to isolate mathematical-content dependencies that carry domain-specific signal. We build a pipeline that: (1) extracts complete proof dependencies from elaborated Lean 4 proof terms via kernel Expr traversal with infrastructure edge filtering, (2) computes dependency domain signatures over Mathlib's curated module hierarchy (~70 mathematical subdomain categories), (3) predicts expected domain signatures from informal statements using a Dirichlet-multinomial mixture model trained on ~300K multi-source samples (Herald's 110K Mathlib NL annotations, LeanWorkbook's 57K NL-Lean pairs, Mathlib's 131K documented definitions, and module-structure weak supervision), and (4) flags divergences via a Proof Fingerprint Score combining infrastructure-filtered domain JSD with domain-specific calibration, proof-complexity anomaly features (proof term size, dependency depth, module count relative to problem difficulty), and proof-only dependency ratio analysis. To address the challenge that legitimate proofs frequently draw from unexpected mathematical domains (50.9% of Mathlib edges cross namespace boundaries), we output multi-modal predicted signatures, apply domain-specific calibration thresholds, and rely on proof-complexity features that are robust to cross-domain strategies. A pilot experiment on 200 Mathlib theorems measures the false-positive base rate of 'surprising but faithful' domain divergence, followed by validation on 50 theorems with synthetically weakened variants, and full evaluation on MathAtlas (52K theorems, 178K dependency relations), FATE-H/FATE-X (where formalization bottleneck is documented), and PutnamBench, using BFS-Prover-V2-32B for proof generation. We demonstrate that proof fingerprinting detects unfaithful formalizations missed by both type-checking and statement-level alignment scoring, and yields complementary gains when combined with FormalAlign, ReForm, Aria, and ProofFlow.",
  "project_name": "proof_struct_fingerprint",
  "source": "web_research"
}
```

Please output this exactly as-is. Make sure the JSON is valid.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "b58fe7af-dbdd-4f53-8f35-10ac614b568e",
  "agentId": "ad6f042dde204c722",
  "type": "user",
  "uuid": "97daabae-38e1-40f7-b262-f6ce967127ab",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7462c804-9bf8-4f0e-b46e-3aeba9f41e8c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-27T20:41:24.364Z_

```json
{
  "parentUuid": "97daabae-38e1-40f7-b262-f6ce967127ab",
  "isSidechain": true,
  "agentId": "ad6f042dde204c722",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": [],
    "readdedNames": []
  },
  "type": "attachment",
  "uuid": "1c34da5d-2ad1-4482-b5bb-11074020d24a",
  "timestamp": "2026-05-27T20:41:24.364Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7462c804-9bf8-4f0e-b46e-3aeba9f41e8c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-27T20:41:24.365Z_

```json
{
  "parentUuid": "1c34da5d-2ad1-4482-b5bb-11074020d24a",
  "isSidechain": true,
  "agentId": "ad6f042dde204c722",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "34064142-8968-4d86-9921-a9891ca657ce",
  "timestamp": "2026-05-27T20:41:24.365Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7462c804-9bf8-4f0e-b46e-3aeba9f41e8c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-27T20:43:38.752Z_



Here is the valid JSON:

```json
{
  "title": "Proof-Structure Fingerprinting for Autoformalization Semantic Verification",
  "change_type": "major",
  "revision_notes": {
    "critical_1_hallucinated_statistic": "Removed the fabricated '80%+ of unsolved problems are due to formalization errors' claim attributed to Goedel-Prover-V2. Replaced with properly sourced evidence from the FATE benchmark (ICLR 2026): on FATE-H, DeepSeek-R1 achieves 71% natural-language reasoning accuracy but 0% formal proving accuracy; DeepSeek-Prover-V2 achieves 39% NL but only 3% formal. This demonstrates formalization quality — not mathematical reasoning — is the primary bottleneck, with Mathlib hallucinations and Lean proficiency issues appearing in nearly every failed proof attempt.",
    "critical_2_outdated_SOTA": "Updated from Goedel-Prover-V2-32B (88.1%) to reflect current landscape: Seed-Prover (99.6% MiniF2F-test, July 2025) saturates MiniF2F; Seed-Prover 1.5 (Dec 2025) solves 88% PutnamBench, 80% FATE-H, 33% FATE-X; BFS-Prover-V2-32B (95.08% MiniF2F-test, open-source weights on HuggingFace) is used as our open-source prover. MiniF2F near-saturation motivated the shift to harder benchmarks.",
    "critical_3_domain_mismatch": "Removed 'Do LLMs Game Formalization?' as ground truth. That paper evaluates on FOLIO/Multi-LogiEval (first-order logic, not math) and actually found NO evidence of systematic gaming. Replaced with: (a) FATE benchmark for formalization-as-bottleneck motivation, (b) Lean Atlas's five hallucination patterns for taxonomy, (c) synthetic unfaithful formalization generation via systematic statement weakening.",
    "major_4_missing_aria": "Added Aria (ICLR 2026) with detailed differentiation: Aria uses statement-level dependency decomposition for generation (Graph-of-Thought + AriaScorer retrieves Mathlib definitions for term-level grounding), while we analyze proof-level dependencies post-hoc for verification. These are complementary — Aria ensures correct concepts enter the formalization; we verify the proof reveals the formalization actually captured the intended mathematics.",
    "major_5_tactic_automation": "Addressed the fundamental challenge of automation tactics (simp, omega, aesop, decide) hiding true dependencies. Solution: analyze kernel-level elaborated proof terms rather than surface tactic scripts. Lean 4 elaborates all tactic proofs into fully-explicit Expr terms that the trusted kernel type-checks. We extract all referenced constants from these elaborated terms via recursive Expr traversal (cf. lean-training-data's premise extraction approach, which already prefixes simp-used constants with 's'). This transforms the challenge into a strength — we capture the TRUE dependency set that even the user cannot see from the tactic script.",
    "moderate_6_benchmark_saturation": "Shifted primary evaluation from MiniF2F (saturated at 99.6%) to MathAtlas (52K theorems, 178K dependency relations, 87 math areas, best model at 9.8% correctness — far from saturated). Added FATE-H/FATE-X (where formalization bottleneck is documented) and PutnamBench. MiniF2F retained only as sanity-check validation.",
    "moderate_7_missing_pseudo_formalization": "Added Pseudo-Formalization (Stanford, May 2026) to landscape. Differentiation: PF verifies informal proof correctness via natural-language Block Verification (no formal proof assistant needed); we verify formal proof semantic faithfulness by analyzing the Lean kernel proof term's dependency footprint. Different verification targets (proof correctness vs. formalization faithfulness) and different substrates (NL vs. formal).",
    "minor_8_mathlib_clustering": "Replaced untested unsupervised clustering with Mathlib's existing hierarchical module structure as the domain taxonomy. Mathlib organizes 274K+ theorems and 130K+ definitions into a well-curated hierarchy (Algebra, Topology, Analysis, Combinatorics, etc.) with ~70 second-level subdivisions (Algebra.Group, Topology.MetricSpace, Analysis.NormedSpace, etc.). This is a principled, human-curated taxonomy that eliminates the clustering quality concern entirely.",
    "R2_moderate_9_formalalign": "Added FormalAlign (ICLR 2025) to landscape with detailed differentiation. FormalAlign evaluates statement-pair alignment via a dual loss combining cross-entropy (certainty score measuring prediction confidence) and contrastive learning (similarity score measuring embedding alignment), achieving 99.21% alignment-selection on FormL4-Basic and 66.39% on MiniF2F-Valid but only 65% correctness vs. 79.58% human experts. Key distinction: FormalAlign scores NL↔FL statement pairs without examining proofs; PFS analyzes the kernel-level proof term's dependency domain signature. These are complementary — FormalAlign catches surface-level statement misalignment; PFS catches cases where a statement appears aligned but the proof reveals it captures weaker/different mathematics. PFS could serve as a second-stage filter after FormalAlign's first-stage screening.",
    "R2_moderate_10_false_positives": "Addressed the false positive problem from unexpected proof strategies with quantitative evidence from 'The Network Structure of Mathlib' (arXiv 2604.24797, April 2026). That analysis of 308K declarations and 8.4M edges found 50.9% of declaration-level edges cross namespace boundaries and only 0.34 NMI between naming conventions and dependency-based communities — confirming that cross-domain proofs are pervasive. However, the same paper reveals that 74.2% of all dependency edges are invisible compiler-synthesized infrastructure (typeclass resolution, coercions, automatic instances), not mathematical content. Our revised approach: (1) filter infrastructure edges by excluding compiler-synthesized dependencies, focusing on the ~25.8% of explicit mathematical-content edges that carry domain-specific signal; (2) leverage the paper's finding that 43.9% of edges are proof-only (not in the statement) — these proof-only dependencies are exactly the novel signal PFS exploits; (3) train the domain-signature predictor to output mixture distributions (Dirichlet-multinomial) rather than point predictions, acknowledging that problems may have legitimate multi-domain proof strategies; (4) compute domain-specific calibration thresholds using Mathlib's own theorems (some domains like Analysis.NormedSpace are inherently cross-domain, others like Combinatorics.SimpleGraph are more self-contained); (5) add a pilot measurement of the false-positive base rate by sampling 200 Mathlib theorems, comparing predicted vs. actual domain signatures, and reporting the rate of 'surprising but faithful' divergence. If this rate exceeds 15%, the JSD component alone is insufficient and the proof-complexity anomaly features (proof term size, dependency depth, distinct module count relative to problem difficulty) become the primary signal.",
    "R2_moderate_11_training_data": "Validated and corrected the ~50K Mathlib docstring claim. Mathlib's docBlame linter requires docstrings for definitions (~131K) but docBlameThm only encourages (not requires) docstrings for theorems (~275K). No public statistics exist on theorem docstring coverage, and the actual number with adequate NL descriptions is likely far below 50K. Revised training data strategy to use multiple complementary sources: (a) Herald dataset (ICLR 2025): 110K Mathlib4 theorems with LLM-generated NL annotations via hierarchical informalization, plus 44K NL-FL proof pairs — this is the primary training source; (b) LeanWorkbook (NeurIPS 2024): 57K NL-Lean pairs from AOPS competition problems; (c) Mathlib definitions with required docstrings (~131K) for supervised domain-signature learning; (d) Mathlib's own module structure as weak supervision — each theorem's module path provides a ground-truth 'home domain' that can bootstrap the predictor. Combined training set: ~300K+ samples from diverse sources, far exceeding the original 50K claim. Training target is also clarified: we predict dependency domain distributions, not reconstruct full informal descriptions, so even terse theorem names and module paths are informative.",
    "R2_minor_12_mathatlas_unfaithful": "Removed the claim about collecting 'naturally-occurring unfaithful formalizations from MathAtlas's formalization attempts.' MathAtlas contains only informal mathematical entities from textbooks; it does not include pre-labeled failed or unfaithful formalization attempts in the released dataset. Ground truth unfaithful formalizations now come exclusively from: (i) systematic synthetic statement weakening, (ii) Lean Atlas hallucination pattern injection, and (iii) a new source: comparing model-generated formalizations against MathAtlas's MA-Align benchmark (200 entities with binary aligned/misaligned labels) to identify and collect naturally misaligned examples from model outputs.",
    "R2_minor_13_roundtrip_verification": "Removed 'Faithful Autoformalization via Roundtrip Verification and Repair' from key references. That paper evaluates exclusively on Texas statutory text (150 traffic rules + 77 parks/wildlife rules) using many-sorted first-order logic with Z3 SMT solver — the authors explicitly state they 'do not claim the framework transfers to other genres.' Its roundtrip verification concept (formalize → informalize → re-formalize → check equivalence) is interesting but operates on a fundamentally different domain and formalism than mathematical theorem proving in Lean 4."
  },
  "core_problem": "Autoformalization quality is the binding constraint in formal theorem proving: on the FATE-H benchmark, models achieve 39-71% natural-language reasoning accuracy but only 0-3% formal proving accuracy, with Mathlib hallucinations and Lean proficiency issues appearing in nearly every failed attempt (FATE, ICLR 2026). Yet current verification methods check only syntactic correctness (type-checking), not whether a formalization semantically captures the intended mathematics. Existing automated alignment evaluation (FormalAlign, ICLR 2025) scores statement-pair alignment via learned embeddings but does not examine what the proof itself reveals about semantic faithfulness. Can we use the structure and complexity of a proof itself — specifically its dependency footprint over the mathematical library — as a post-hoc signal to detect semantically unfaithful formalizations?",
  "opportunity": "The FATE benchmark (ICLR 2026) demonstrated that formalization, not reasoning, is the primary bottleneck: models with strong informal reasoning systematically fail at faithful formalization into Lean 4. Lean Atlas (April 2026) catalogued five specific hallucination patterns (definition mismatches, missing assumptions, goal substitution, quantifier errors, type default semantic shifts) that survive type-checking. FormalAlign (ICLR 2025) automates statement-pair alignment scoring via dual embedding+generation loss (99.21% on FormL4-Basic) but operates only on statements, achieving just 65% correctness vs. human experts on subtle cases — it cannot examine whether the proof actually engages the expected mathematics. Other approaches use LLM-as-judge (ReForm, +22.6pp but inherently noisy), statement-level dependency decomposition for grounded generation (Aria, ICLR 2026, 68.5% accuracy on ProofNet), embedding-based retrieval (ProofBridge), structural fidelity metrics (ProofFlow, ProofScore 0.545 vs 0.123 baseline), or natural-language Block Verification (Pseudo-Formalization, Stanford May 2026). None exploit a key insight: the kernel-level proof term's Mathlib dependency footprint encodes what mathematics the formalization actually captures. Recent network analysis of Mathlib (April 2026) reveals that 43.9% of proof dependencies are proof-only — absent from the statement entirely — meaning the proof carries rich information about mathematical content that statement-level methods fundamentally cannot access. If an olympiad combinatorics problem is formalized and proved using only basic arithmetic lemmas from Mathlib.Algebra.Order, the formalization almost certainly captured a weaker statement — regardless of whether the tactic script looks reasonable or whether a statement-level alignment scorer rates it as aligned.",
  "landscape": "The FATE benchmark (ICLR 2026) establishes that on graduate/PhD-level algebra problems, formalization quality is the primary bottleneck: 71% NL accuracy drops to 0% formal accuracy for DeepSeek-R1 on FATE-H. FormalAlign (ICLR 2025) is the closest prior work on automated semantic alignment evaluation: it trains a dual-loss model (cross-entropy certainty + contrastive similarity) to score NL↔FL statement pairs, achieving 99.21% alignment-selection on FormL4-Basic and 66.39% on MiniF2F-Valid, but operates only at statement level and reaches 65% correctness vs. 79.58% human experts. ReForm (Feb 2026) uses reflective self-correction with LLM-as-judge, achieving 22.6pp improvement but relying on noisy LLM evaluation. CRAMF uses retrieval of Mathlib definitions to ground generation (up to 62.1% relative improvement). Aria (ICLR 2026) introduces a two-phase Graph-of-Thought system with AriaScorer that retrieves Mathlib definitions for term-level grounding, achieving 91.6% compilation and 68.5% accuracy on ProofNet and 44.0% on FATE-X; critically, Aria decomposes statement-level dependencies for generation, not proof-level dependencies for post-hoc verification. ProofFlow (ICLR 2026) introduces ProofScore combining syntactic, semantic, and structural fidelity metrics (0.545 vs 0.123 baseline), using dependency DAGs for structuring proof generation but not as a post-hoc semantic verifier. ProofBridge improves cross-modal retrieval by 3.28x over all-MiniLM-L6-v2 and achieves +31.14% semantic correctness. Pseudo-Formalization (Stanford, May 2026) verifies informal proof correctness via natural-language Block Verification, pareto-dominating LLM-as-judge baselines — but operates on natural language proofs, not formal proof terms. Lean Atlas (April 2026) classifies dependency graph edges (type vs. value) for human-AI collaborative verification but requires human review. The Network Structure of Mathlib (April 2026) provides crucial empirical context: 50.9% of declaration-level edges cross namespace boundaries and 74.2% are compiler-synthesized infrastructure, revealing that mathematical dependencies are heavily entangled but largely through automated mechanisms rather than mathematical content — a finding we exploit by filtering infrastructure edges to isolate content-level domain signals. MathAtlas (May 2026) introduces dependency-graph-enriched benchmarks (~178K relations, 87 math areas) but does not use dependencies as a verification signal. FormalEvolve (March 2026) addresses semantic drift via evolutionary search. FormaRL uses dual rewards (compiler + LLM comparison). Direct Dependency Retrieval improves autoformalization by retrieving Mathlib dependencies at generation time. The missing piece: no existing work extracts the elaborated proof term's mathematical-content dependency set (filtering compiler-synthesized infrastructure), compares its domain distribution against what the informal problem predicts, and uses proof-only dependencies — which constitute 43.9% of all edges — as a novel semantic faithfulness signal unavailable to any statement-level method.",
  "inspired_by": "FATE benchmark finding that formalization is the primary bottleneck (71% NL → 0% formal on FATE-H) + FormalAlign's demonstration that statement-level alignment evaluation reaches only 65% of human accuracy (leaving room for proof-level signals) + The Network Structure of Mathlib's finding that 43.9% of proof dependencies are proof-only and 74.2% are infrastructure (enabling infrastructure filtering for cleaner domain signals) + Lean Atlas's five hallucination patterns surviving type-checking + Aria's demonstration that dependency graphs improve autoformalization quality + pattern 'Verifier-as-Swiss-Army-Knife' (using verifier-derived signals for data quality filtering) + lean-training-data's premise extraction showing that elaborated proof term dependencies are extractable including simp-used constants",
  "approach": "Build a proof-structure fingerprinting pipeline in four phases:\n\nPhase 0 — Pilot Validation with False-Positive Measurement (weeks 1-3): Validate the core hypothesis AND measure the false-positive base rate. (a) Select 200 Mathlib theorems stratified across 10+ mathematical domains, extract their elaborated proof term dependencies, filter compiler-synthesized infrastructure edges (74.2% of all edges per Network Structure of Mathlib), and compute dependency domain signatures over Mathlib's module hierarchy. Compare each theorem's informal description (from Herald annotations or theorem name) against its actual filtered dependency signature. Measure the rate of 'surprising but faithful' domain divergence — theorems whose proofs legitimately draw from unexpected domains. This establishes the false-positive base rate. (b) From a 50-theorem subset with known faithful formal-informal pairs, generate 3 unfaithful variants each via systematic statement weakening (drop hypotheses, weaken quantifiers, substitute weaker type constraints — mirroring Lean Atlas's five hallucination patterns). Prove all versions with BFS-Prover-V2-32B. Show statistically significant divergence (Mann-Whitney U test) between faithful and unfaithful formalization proofs on infrastructure-filtered domain signatures. If Cohen's d < 0.5, pivot or abandon. If false-positive base rate >15%, the JSD component alone is insufficient — proceed with emphasis on proof-complexity anomaly features and multi-modal prediction.\n\nPhase 1 — Dependency Extraction with Infrastructure Filtering (weeks 2-4): Build a Lean 4 metaprogram that, given a completed proof, (a) extracts the fully-elaborated kernel proof term (which resolves all tactic automation — simp, omega, aesop, decide — into explicit constant references), (b) recursively traverses the Expr to collect all referenced Mathlib constants (using ConstantInfo lookups in the Environment), (c) classifies each edge as explicit-content vs. compiler-synthesized (leveraging the Lean elaborator's provenance information to distinguish user-written references from typeclass resolution, coercions, and automatic instances), and (d) maps each content-level constant to its Mathlib module path. This infrastructure filtering is a key technical contribution informed by the Network Structure of Mathlib's finding that 74.2% of edges are invisible infrastructure — removing these dramatically improves the domain-signal-to-noise ratio.\n\nPhase 2 — Multi-Modal Domain Signature Prediction (weeks 3-7): Using Mathlib's hierarchical module structure as a natural domain taxonomy (~70 second-level categories), compute 'dependency domain signatures' — normalized distribution vectors over module categories — for each proof's infrastructure-filtered dependencies. Train a domain-signature predictor using multiple complementary data sources: (a) Herald's 110K Mathlib4 theorem NL annotations (ICLR 2025) as primary training data — these are LLM-generated informalizations with hierarchical dependency context, paired with actual dependency signatures extracted in Phase 1; (b) LeanWorkbook's 57K NL-Lean pairs from competition problems; (c) Mathlib's ~131K definitions with required docstrings; (d) Mathlib's module structure as weak supervision — each theorem's module path provides ground-truth 'home domain' bootstrapping. Total: ~300K+ training samples. Crucially, the predictor outputs Dirichlet-multinomial mixture distributions rather than point predictions, acknowledging that problems may have legitimate multi-domain proof strategies (e.g., analytic number theory proofs that necessarily span Number Theory + Analysis + Topology). Additionally, compute domain-specific calibration thresholds: some Mathlib areas (e.g., Analysis.NormedSpace, Topology.Algebra) are inherently cross-domain with wide dependency spreads, while others (Combinatorics.SimpleGraph, Data.Nat.Prime) are more self-contained — calibration accounts for this structural variation.\n\nPhase 3 — Proof Fingerprint Score and Evaluation (weeks 5-10): Define the Proof Fingerprint Score (PFS) combining three signal types: (a) Infrastructure-Filtered Domain JSD: Jensen-Shannon divergence between predicted and actual dependency domain signatures after infrastructure filtering, with domain-specific calibration thresholds; (b) Proof-Complexity Anomaly Features: proof term size, maximum dependency depth, and number of distinct Mathlib modules invoked, each relative to estimated problem difficulty — these features are robust to cross-domain proofs since unfaithful formalizations tend to have systematically shorter/simpler proofs regardless of domain; (c) Proof-Only Dependency Ratio: the fraction of proof dependencies absent from the statement, leveraging the finding that 43.9% of edges are proof-only — unfaithful formalizations that trivialize a problem should show atypical proof-only dependency patterns. Evaluate on: (a) MathAtlas — primary benchmark (52K theorems, 178K dependency relations, 87 math areas; best existing model at 9.8% correctness), selecting ~500 theorems with proofs and generating synthetic unfaithful variants; (b) FATE-H/FATE-X — where formalization bottleneck is documented, using the two-stage evaluation to compare NL-correct-but-formally-wrong attempts; (c) PutnamBench — undergraduate competition problems in Lean 4; (d) MiniF2F — retained only as sanity-check validation. Ground truth unfaithful formalizations generated via: (i) systematic statement weakening (drop hypotheses, weaken bounds, simplify quantifiers, substitute weaker types), (ii) Lean Atlas hallucination pattern injection (definition mismatches, missing assumptions, goal substitution, quantifier errors, type default shifts), and (iii) collecting naturally misaligned model outputs by evaluating against MathAtlas's MA-Align benchmark (200 entities with binary aligned/misaligned labels). Use BFS-Prover-V2-32B (95.08% MiniF2F-test, open-source weights) for proof generation. Report false-positive rates alongside detection accuracy, broken down by mathematical domain. Demonstrate PFS as a plug-in verifier yielding complementary gains atop FormalAlign (+statement-level alignment), ReForm (+LLM-as-judge), Aria (+statement-level grounding), and ProofFlow (+structural DAG).",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "650",
      "timeline": "13 weeks",
      "estimated_gpu_cost": "$1,300"
    },
    "human_in_loop": {
      "gpu_hours": "450",
      "timeline": "11 weeks",
      "claude_api_cost": "$550",
      "estimated_gpu_cost": "$900"
    },
    "auto_research": {
      "gpu_hours": "450",
      "timeline": "7 weeks",
      "claude_api_cost": "$1,300",
      "estimated_gpu_cost": "$900",
      "speed_bottleneck": "Lean 4 kernel elaboration and type-checking is sequential and CPU-bound (5-60s per proof); dependency extraction with infrastructure classification over elaborated proof terms for the evaluation set (~2K proofs × 4 variants = 8K total) takes ~3 days on a 32-core server; proof search with BFS-Prover-V2-32B at pass@32 over ~2K problems requires ~150 A100-hours of inference; MathAtlas dependency graph processing for ~178K relations is a one-time ~12hr computation; Herald dataset integration and multi-source training data preparation adds ~1 week; false-positive base rate measurement on 200 Mathlib theorems adds ~2 days of extraction + analysis"
    }
  },
  "target_venues": [
    "ICLR 2027 (expected ~October 2026)",
    "AAAI 2027 (full paper deadline: July 28, 2026 — tight but feasible if pilot succeeds quickly)",
    "EACL 2027 via ARR August cycle (deadline: August 3, 2026)"
  ],
  "level": "solid-to-strong",
  "key_references": [
    "FATE: A Formal Benchmark Series for Frontier Algebra of Multiple Difficulty Levels (ICLR 2026) — primary evidence that formalization is the bottleneck",
    "FormalAlign: Automated Alignment Evaluation for Autoformalization (ICLR 2025) — closest prior work on automated semantic alignment; statement-level dual-loss alignment scoring",
    "Aria: An Agent for Retrieval and Iterative Auto-Formalization via Dependency Graph (ICLR 2026) — statement-level dependency decomposition for generation",
    "ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization (ICLR 2026) — ProofScore for structural fidelity",
    "The Network Structure of Mathlib (arXiv 2026) — quantitative analysis: 50.9% cross-namespace edges, 74.2% compiler-synthesized infrastructure, 43.9% proof-only dependencies",
    "Herald: A Natural Language Annotated Lean 4 Dataset (ICLR 2025) — 110K Mathlib4 theorem NL annotations via hierarchical informalization; primary training data source",
    "Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction (ICLR 2026) — autoformalization pipeline",
    "Seed-Prover: Deep and Broad Reasoning for Automated Theorem Proving (arXiv 2025) — saturates MiniF2F at 99.6%",
    "Seed-Prover 1.5: Mastering Undergraduate-Level Theorem Proving via Learning from Experience (arXiv 2025) — 88% PutnamBench, 80% FATE-H",
    "BFS-Prover-V2: Scalable Best-First Tree Search for Theorem Proving (arXiv 2026) — open-source SOTA step-prover, 95.08% MiniF2F",
    "Pseudo-Formalization for Automatic Proof Verification (arXiv 2026, Stanford) — NL Block Verification pareto-dominating LLM-as-judge",
    "Lean Atlas: An Integrated Proof Environment for Scalable Human-AI Collaborative Formalization (arXiv 2026) — five hallucination patterns, dependency edge classification",
    "ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization (arXiv 2025) — LLM-as-judge baseline",
    "MathAtlas: A Benchmark for Autoformalization in the Wild (arXiv 2026) — 52K theorems, 178K dependency relations, MA-Align benchmark",
    "Lean Workbook: A large-scale Lean problem set formalized from natural language math problems (NeurIPS 2024) — 57K NL-Lean pairs; training data source",
    "Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning (VerifAI Workshop, ICLR 2026) — cited for semantic gap finding in FOL domain only",
    "ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings (arXiv 2025) — cross-modal retrieval",
    "FormalEvolve: Neuro-Symbolic Evolutionary Search for Diverse and Prover-Effective Autoformalization (arXiv 2026)",
    "LeanDojo: Theorem Proving with Retrieval-Augmented Language Models (NeurIPS 2023)",
    "Improving Autoformalization Using Direct Dependency Retrieval (arXiv 2025)"
  ],
  "description": "Autoformalization — translating informal mathematics into machine-verifiable code — suffers from a critical verification gap: syntactic correctness (type-checking) does not guarantee semantic faithfulness, with the FATE benchmark showing models achieve 39-71% natural-language reasoning accuracy but only 0-3% formal proving accuracy, formalization being the primary bottleneck. Existing automated alignment evaluation (FormalAlign, ICLR 2025) scores statement-pair alignment via learned embeddings (99.21% on FormL4-Basic) but examines only statements, not proofs, and achieves only 65% of human expert accuracy on subtle cases. We propose Proof-Structure Fingerprinting, a novel post-hoc verification method that exploits the kernel-level proof term itself as a semantic signal. Our key insight is that a proof's Mathlib dependency footprint — the complete set of library constants referenced in the elaborated proof term that the Lean 4 kernel type-checks — encodes rich information about what mathematical content the formalization actually captures. Crucially, recent network analysis of Mathlib reveals that 43.9% of proof dependencies are proof-only (absent from the statement), meaning proof-level analysis accesses semantic information fundamentally unavailable to any statement-level method. The same analysis shows 74.2% of all dependency edges are compiler-synthesized infrastructure (typeclass resolution, coercions); we filter these to isolate mathematical-content dependencies that carry domain-specific signal. We build a pipeline that: (1) extracts complete proof dependencies from elaborated Lean 4 proof terms via kernel Expr traversal with infrastructure edge filtering, (2) computes dependency domain signatures over Mathlib's curated module hierarchy (~70 mathematical subdomain categories), (3) predicts expected domain signatures from informal statements using a Dirichlet-multinomial mixture model trained on ~300K multi-source samples (Herald's 110K Mathlib NL annotations, LeanWorkbook's 57K NL-Lean pairs, Mathlib's 131K documented definitions, and module-structure weak supervision), and (4) flags divergences via a Proof Fingerprint Score combining infrastructure-filtered domain JSD with domain-specific calibration, proof-complexity anomaly features (proof term size, dependency depth, module count relative to problem difficulty), and proof-only dependency ratio analysis. To address the challenge that legitimate proofs frequently draw from unexpected mathematical domains (50.9% of Mathlib edges cross namespace boundaries), we output multi-modal predicted signatures, apply domain-specific calibration thresholds, and rely on proof-complexity features that are robust to cross-domain strategies. A pilot experiment on 200 Mathlib theorems measures the false-positive base rate of 'surprising but faithful' domain divergence, followed by validation on 50 theorems with synthetically weakened variants, and full evaluation on MathAtlas (52K theorems, 178K dependency relations), FATE-H/FATE-X (where formalization bottleneck is documented), and PutnamBench, using BFS-Prover-V2-32B for proof generation. We demonstrate that proof fingerprinting detects unfaithful formalizations missed by both type-checking and statement-level alignment scoring, and yields complementary gains when combined with FormalAlign, ReForm, Aria, and ProofFlow.",
  "project_name": "proof_struct_fingerprint",
  "source": "web_research"
}
```

This is valid JSON. All strings are properly escaped, the structure is well-formed, and the em dashes and special characters within string values are preserved correctly. Would you like me to write this to a file?

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34064142-8968-4d86-9921-a9891ca657ce",
  "isSidechain": true,
  "agentId": "ad6f042dde204c722",
  "requestId": "req_011CbTipQX332RMr3T1Y36os",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a262a493-8303-4447-9c76-5fa320a3591a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7462c804-9bf8-4f0e-b46e-3aeba9f41e8c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ae45P7t4ZpHShJfVJTfc4i",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16426,
      "cache_read_input_tokens": 0,
      "output_tokens": 7646,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16426
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 7646,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 16426,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16426,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---
