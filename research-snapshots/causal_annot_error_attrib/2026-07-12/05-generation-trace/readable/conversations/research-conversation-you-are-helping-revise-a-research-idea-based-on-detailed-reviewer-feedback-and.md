# Research conversation: You are helping revise a research idea based on detailed reviewer feedback and new research findings. I need you to comp

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 3
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-ace13499b3290f5f7.jsonl`
- **Structured JSON:** [`2e98394a5e51c61aa680.json`](../../sessions/2e/2e98394a5e51c61aa680.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

3 recorded events

### User

_source line 1 · 2026-05-16T09:15:03.978Z_

You are helping revise a research idea based on detailed reviewer feedback and new research findings. I need you to compose a complete revised JSON object. I'll provide the structure, key changes, and content for each field. Your job is to assemble it into a clean, complete JSON.

**Context**: This is round 6 of revision for a paper on "Geometry-Triggered Steering" (GTS) — selective activation steering for hallucination suppression. The idea has stagnated at scores 3.2-3.5 across 3 rounds. Today is May 16, 2026. ARR deadline is May 25 (9 days remain).

**Key changes for this major revision:**

1. **Reframe the core contribution** around the GRANULARITY MISMATCH between token-level intervention and claim-level evaluation, rather than centering on Mahalanobis distance. PCNet's 53.7% corruption rate is concrete evidence that token-level gating still damages correct text.

2. **Elevate PCNet to primary competitor** with full differentiation paragraph.

3. **Honestly position Euclidean→Mahalanobis** as a hypothesized improvement to ablate, not the core contribution.

4. **Add timing hypothesis disclaimer** noting Attractor Geometry paper's explicit limitation.

5. **Define realistic 9-day minimum viable scope.**

Here is the complete JSON to output. Output ONLY the JSON, no other text:

```json
{
  "change_type": "major",
  "title": "Claim-Level Selective Activation Steering for Factual Hallucination Suppression in Long-Form Generation",
  "core_problem": "Factual hallucination in LLMs has spurred a proliferation of geometry-aware detection and activation steering methods, yet a fundamental granularity mismatch persists: detection and intervention operate at token level, while factual evaluation operates at claim/sentence level. PCNet (May 2026) exemplifies this—its probabilistic-circuit gating achieves near-perfect detection AUROC yet still corrupts 53.7% of originally correct generations when intervening at every deviant token, because token-level decisions cannot distinguish 'this token is anomalous within an otherwise correct claim' from 'this claim is genuinely hallucinated.' FASB (NeurIPS 2025) addresses selective steering but operates correctively—detecting deviation after tokens are generated, then backtracking 10 tokens—which wastes compute and splits coherent claims. Spherical Steering (ICML 2026) applies per-token rotation with continuous vMF-gated intensity, achieving strong TruthfulQA gains but intervening indiscriminately across all claims. The Attractor Geometry paper (May 2026) demonstrates that Euclidean geometric margin separates correct recall from hallucination (AUROC 0.858 on TruthfulQA vs. entropy 0.656), but this result is detection-only and measured at first-digit positions on factoid completion—translation into targeted intervention at appropriate granularity during multi-sentence generation remains the open challenge.",
  "opportunity": "The unexploited sweet spot is pre-emptive claim-level gating: sentences are the natural unit of factual claims—the granularity FActScore evaluates, the granularity humans judge, and the granularity at which LLMs integrate context before next-sentence planning (supported by 'Think in Sentences,' April 2026). The key evidence that this granularity matters comes from PCNet's results: despite near-perfect token-level detection (AUROC up to 99% on extractive QA), its token-level intervention still corrupts 53.7% of correct generations and preserves only 79.3%. This is because anomaly at individual token positions does not reliably indicate that the entire claim is hallucinated—a high-NLL token may be stylistically unusual but factually correct, or may be part of a partially correct claim that token-level correction damages. A system that makes binary steer/skip decisions at sentence boundaries—preserving entire correct claims untouched while steering only claims where the model lacks factual grounding—can achieve higher preservation rates by avoiding sub-claim intervention entirely. The three-part framework (when: sentence boundaries; whether: geometric distance trigger; how much: per-layer intensity) addresses limitations in all current methods: PCNet's token-level corruption, FASB's corrective backtracking overhead, Spherical Steering's indiscriminate application, and Hallucination Basins' per-sequence uniformity.",
  "landscape": "**Selective geometric gating (primary competitors):**\n\n*PCNet (arXiv 2605.05953, May 2026)* is the closest concurrent work sharing the 'detect geometric anomaly → selectively intervene' paradigm. PCNet trains a Probabilistic Circuit as a density estimator over MLP-compressed residual stream states (4096→128 dims), computes exact NLL as anomaly score, and triggers PC-LDCD (contrastive decoding) only at deviant tokens. Results: TruthfulQA MC1 0.51 / MC2 0.65 on Llama-3.1-8B; near-perfect detection AUROC on extractive QA; corruption rate 53.7%, preservation rate 79.3%. Overhead: <2% for PC scoring, but 3.3–6.2 additional block evaluations per anomalous token for lookahead. GTS differs in three fundamental ways: (a) Granularity: sentence-level binary decisions preserve entire correct claims and avoid sub-claim corruption. PCNet evaluates NLL at every token, meaning intervention can damage partially correct claims—evidenced by its 53.7% corruption rate despite near-perfect detection. GTS's claim-level atomicity should achieve substantially lower corruption. (b) Intervention mechanism: activation steering shifts the model's own generation distribution toward factual attractors in a single forward pass, while contrastive decoding requires maintaining lookahead evaluations for top-k candidates at every anomalous position (PCNet's IGR ranges 0.41–0.78, meaning lookahead triggers at 41–78% of tokens). On long-form generation where many tokens are flagged, GTS's steering-only approach avoids this per-token lookahead cost. (c) Trigger interpretability: Euclidean/Mahalanobis distance from factual cluster centroids has a clear geometric interpretation (distance in representation space), while NLL from a trained probabilistic circuit is a learned density estimate whose failure modes are less transparent.\n\n*FASB (arXiv 2508.17621, NeurIPS 2025)* is the most direct prior work on 'when to steer,' using linear probes trained on attention head activations. It monitors concatenated question-and-generated-content states, triggers intervention when deviation is detected, and backtracks s=10 tokens to regenerate with steering. MC1 48.71% on TruthfulQA (LLaMA-2-7B-Chat). GTS differs in: (a) pre-emptive gating at sentence boundaries (no wasted tokens, no rollback) vs. FASB's corrective backtracking; (b) geometric distance trigger measuring knowledge absence vs. learned directional alignment on attention heads; (c) atomic claim-level decisions vs. token-level cuts that may split coherent claims. FASB's backtracking overhead scales linearly with intervention frequency—compounding on hallucination-dense long-form passages.\n\n**Geometry-aware steering (per-token):** Spherical Steering (arXiv 2602.08169, ICML 2026) uses geodesic rotation with a von Mises-Fisher confidence gate, achieving MC1 +15.80% on TruthfulQA (Llama-3.1-8B) with single-layer intervention (layer 24). Code released at github.com/chili-lab/Spherical-Steering. Per-token with continuous intensity—no claim-level selectivity. Hallucination Basins (arXiv 2604.04743, April 2026) proposes Adaptive Geometry-Aware Steering using Euclidean distance triggers and logistic-regression scalar maps at per-sequence granularity (uniform across all claims). Tested on 1B–8B models. GTS advances beyond both via within-sequence sentence-level selectivity.\n\n**Context-dependent directions:** Steering Vector Fields (SVF, arXiv 2602.01654, Feb 2026) learns differentiable concept-scoring MLPs for context-aware steering directions refreshed every K steps. Always steers—no gating. Complementary to GTS (GTS decides whether; SVF decides in which direction).\n\n**Utility preservation:** COAST (arXiv 2605.01167, May 2026) formalizes collateral damage as unintended feature-direction shifts and optimizes the steering vector via constrained optimization. Complementary to GTS (COAST optimizes the vector; GTS optimizes when to apply it).\n\n**Nonlinear geometry:** Curveball Steering (arXiv 2603.09313, March 2026) demonstrates substantial geometric distortion in activation spaces, supporting covariance-aware (Mahalanobis) over Euclidean distance.\n\n**Detection-only:** Attractor Geometry of Transformer Memory (arXiv 2605.05686, May 2026) demonstrates hallucination = basin absence with Euclidean geometric margin AUROC 0.858 on TruthfulQA (vs. entropy 0.656), 0.993 on controlled factoid tasks. All measurements at first-digit positions before autoregressive dynamics compound; the paper explicitly states 'transfer to open-domain settings requires further study.' Where Does Reasoning Break? (arXiv 2605.13772, May 2026) detects step-level hallucination via transport geometry. DRIFT (arXiv 2601.14210, Jan 2026) detects representational instability.\n\n**Calibration:** Calibrating Verbal Uncertainty (Ji et al., EMNLP 2025 Outstanding Paper) achieves ~31.9% reduction in confident hallucinations via linear-feature intervention—calibrates expression, does not correct generation.\n\n**Other steering:** ACT (WWW 2025), ODESteer (ICLR 2026, +5.7% over ACT), Guiding Giants/WAS (arXiv 2505.20309), SADI (arXiv 2410.12299), HELIX/Tethered Reasoning (arXiv 2602.17691). FLAS (arXiv 2605.05892, May 2026) learns concept-conditioned velocity fields for multi-step activation transport.\n\n**Supporting evidence:** Hallucination as Trajectory Commitment (arXiv 2604.15400, April 2026) provides causal evidence for early commitment with asymmetric attractor dynamics—supporting timely intervention before commitment propagates. Think in Sentences (arXiv 2604.10135, April 2026) demonstrates sentence boundary attention concentration patterns.",
  "approach": "We propose Claim-Level Selective Activation Steering (CLSAS), a method that bridges the granularity gap between token-level detection/intervention and claim-level factual evaluation. The central insight is that intervention granularity should match evaluation granularity: since factuality is assessed per-claim (FActScore, human judgment), steering decisions should be made per-claim—preserving entire correct sentences untouched while steering only sentences where the model lacks factual grounding.\n\n**Stage 1: TRIGGER (Geometric Distance at Sentence Boundaries)**\nDuring generation, at each sentence boundary (period/newline tokens), extract hidden-state activations at the boundary token across layers using nnsight intervention hooks. Compute geometric distance from factual cluster centroids:\n(a) Offline: From a calibration set (~2K examples from TruthfulQA + FELM correct-answer forward passes), collect hidden states at factual completion positions. Apply PCA to project from full hidden dimension (d=4096) to top-k principal components (k=256), yielding a well-conditioned 256×256 covariance matrix.\n(b) Online: Project the boundary token's activation into the PCA subspace. Compute distance to nearest factual centroid. We evaluate two distance metrics: (i) Euclidean distance δ_E(x) = ||h_pca − μ_pca||₂, matching the Attractor Geometry paper's validated metric (AUROC 0.858 on TruthfulQA); (ii) Mahalanobis distance δ_M(x) = √((h_pca − μ_pca)ᵀ Σ_pca⁻¹ (h_pca − μ_pca)), a hypothesized improvement motivated by OOD detection literature (Lee et al., NeurIPS 2018) that accounts for directional anisotropy in representation space.\n(c) When distance exceeds a calibrated threshold (set via precision-recall analysis targeting high precision ≥0.85 to minimize false interventions), flag the upcoming sentence for steering.\n\n**Critical clarification:** The 0.858 AUROC motivating this trigger was achieved with Euclidean distance on first-digit positions during factoid completion (Attractor Geometry, May 2026). Our application to sentence boundaries during multi-sentence open-ended generation is an extrapolation that we explicitly validate as Milestone 1. The Attractor Geometry authors note 'transfer to open-domain settings requires further study.' If Mahalanobis does not significantly outperform Euclidean in our ablation, the primary novelty contribution rests on claim-level selective gating itself—which remains differentiated from all baselines regardless of distance metric.\n\n**Timing Hypothesis Validation (Milestone 1, Days 1-2):**\nWe explicitly frame the following as a testable hypothesis: geometric distance at sentence boundary N is predictive of factual accuracy in sentence N+1. Validation protocol: (1) Generate 500 multi-sentence responses on LongFact/FActScore prompts using Llama-3.1-8B-Instruct. (2) Compute both Euclidean and Mahalanobis distance at every sentence boundary. (3) Annotate each subsequent sentence with FActScore. (4) Measure Spearman correlation between boundary distance and next-sentence factuality, and AUROC for binary classification. If AUROC < 0.70, we implement a look-ahead variant: extract distance from the first 3 generated tokens of the new sentence (before committing via speculative-style buffering). The look-ahead variant adds ~15% latency overhead but operates before the sentence is visible to the user. If look-ahead also fails (AUROC < 0.65), we fall back to a sliding-window approach using the mean distance over the last 5 tokens before the boundary.\n\n**Comparison to PCNet's trigger:** PCNet uses NLL from a trained probabilistic circuit as its anomaly score, evaluated at every token. This achieves near-perfect detection on extractive QA but still yields 53.7% corruption on correct generations. We hypothesize this is because token-level anomaly conflates stylistic deviation with factual error. Our sentence-level trigger aggregates geometric information at natural claim boundaries, making a single binary decision per claim—either the model has factual grounding for this claim (skip) or it doesn't (steer). This avoids sub-claim intervention entirely.\n\n**Stage 2: DIRECTION (Centroid-Directed Steering Vector)**\nCompute the steering direction as the unit vector from the current activation toward the factual cluster centroid at each layer in the PCA subspace, then project back to full space: v_steer = (μ_pca − h_pca) / ||μ_pca − h_pca||, lifted back to full dimensionality via PCA inverse transform. This yields an input-specific correction direction toward regions of successful fact recall.\n\n**Stage 3: INTENSITY (Per-Layer Weighted Steering)**\nA lightweight 2-layer MLP controller (hidden dim 64, inspired by Guiding Giants/WAS) takes [geometric_distance, layer_index/L, distance_velocity] as input (3D feature vector) and predicts per-layer steering weight λ_ℓ. Trained on a calibration set (~2K examples) to maximize FActScore on steered outputs while minimizing perplexity increase on non-flagged outputs. Steering: h_steered(ℓ) = h(ℓ) + λ_ℓ · v_steer(ℓ) at layers where λ_ℓ > ε.\n\n**Minimum Viable Scope (9 days, May 16–25):**\n- Days 1-2 (May 16-17): Timing hypothesis validation on Llama-3.1-8B-Instruct. This is the critical-path milestone—if it fails, immediately implement look-ahead variant.\n- Days 3-4 (May 18-19): Core CLSAS implementation + calibration. Run TruthfulQA and SimpleQA.\n- Days 5-6 (May 20-21): Run baselines (Spherical Steering from released code, FASB from released code). Run FActScore and MT-Bench on CLSAS.\n- Days 7-8 (May 22-23): Key ablations: 2×2 grid (Euclidean vs Mahalanobis × sentence-level vs token-level gating) on 4-benchmark core set. PCNet comparison if code is available; otherwise use reported numbers with matched model.\n- Day 9 (May 24): Writing, formatting, submission buffer.\n- Dropped from scope: COAST combination experiment, Qwen3-8B (secondary model), full 7-benchmark suite for ablations, GTS-FASB-trigger ablation.\n\n**Ablation Design (MVP):**\n- CLSAS-full vs. CLSAS-Euclidean (isolate Mahalanobis contribution)\n- CLSAS-full vs. CLSAS-pertoken (apply continuous per-token gating with our distance metric, matching PCNet/Spherical Steering's granularity—isolates the claim-level contribution)\n- CLSAS-full vs. CLSAS-sequence (single decision per sequence, matching Hallucination Basins' granularity)\n- CLSAS-full vs. CLSAS-scalar (replace per-layer MLP with single scalar, isolating controller contribution)\n- Direct comparison: CLSAS-full vs. Spherical Steering vs. FASB vs. PCNet (reported numbers if code unavailable)\n\n**Primary evaluation metrics:**\n- Corruption rate and preservation rate (matching PCNet's protocol): fraction of correct claims degraded / preserved by intervention\n- FActScore on long-form biographies (primary benchmark where claim-level advantage should be largest)\n- TruthfulQA MC1/MC2, SimpleQA accuracy, MT-Bench score\n- Intervention rate: fraction of sentences steered (lower is better for comparable factuality gains)\n- Latency overhead vs. baselines\n\nImplementation uses nnsight 0.7 on Llama-3.1-8B-Instruct. Qwen3-8B included only if time permits after MVP completion.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~120h H100 80GB",
      "gpu_utilization": "Low (~15-20%)",
      "timeline": "3-4 months",
      "team": "1-2 researchers with mechanistic interpretability + geometric ML experience",
      "estimated_gpu_cost": "$360-400",
      "factScore_api_cost": "$100-200"
    },
    "human_in_loop": {
      "gpu_hours": "~130h H100 80GB",
      "gpu_utilization": "Moderate (45-55%)",
      "timeline": "2-3 weeks",
      "team": "1 researcher, ~30min/day reviewing proposals",
      "claude_api_cost": "$150-250",
      "estimated_gpu_cost": "$390-430",
      "factScore_api_cost": "$100-200",
      "risk_note": "Timing hypothesis validation is critical-path. If it fails (AUROC < 0.70), look-ahead fallback adds ~3 days."
    },
    "auto_research": {
      "gpu_hours": "~140h H100 80GB",
      "gpu_utilization": "High (~85-90%)",
      "timeline": "9 days (May 16-25) with 2 H100 GPUs. Minimum viable paper scope: single model (Llama-3.1-8B), 4-benchmark core set for ablations, full baselines on FActScore+TruthfulQA+SimpleQA+MT-Bench.",
      "team": "0 (initial setup: provision GPUs, configure nnsight 0.7, clone Spherical Steering + FASB repos)",
      "claude_api_cost": "$250-350 (est. 3000-4000 turns)",
      "estimated_gpu_cost": "$420-450",
      "factScore_api_cost": "$100-200",
      "speed_bottleneck": "Timing hypothesis validation (days 1-2) is critical path. If it fails, look-ahead variant must be implemented immediately. Secondary: FActScore GPT-4 API calls.",
      "resource_optimization": "Budget achieved via: (1) single model (Llama-3.1-8B) for all experiments; (2) 4-benchmark core set (TruthfulQA, FActScore, SimpleQA, MT-Bench); (3) 2×2 ablation grid (distance metric × gating granularity) instead of separate sweeps; (4) use Spherical Steering and FASB released code directly; (5) PCNet comparison using reported numbers if code unavailable.",
      "minimum_viable_paper": "If timing hypothesis fails AND look-ahead also fails: pivot to a detection-only contribution (sentence-level geometric detection benchmark) comparing Euclidean/Mahalanobis at sentence boundaries vs. PCNet's token-level NLL. This is publishable as a shorter paper (findings track).",
      "risk_note": "Primary risk: timing hypothesis may fail (Attractor Geometry paper validated only on factoid completion at first-digit positions, explicitly disclaiming open-domain transfer). Mitigation: look-ahead variant, then sliding-window fallback. Secondary risk: claim-level gating may not outperform PCNet's token-level gating on short-form QA—advantage expected primarily on long-form generation (FActScore, LongFact). Tertiary risk: 9-day timeline leaves zero buffer for unexpected implementation issues."
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR submission deadline May 25, 2026; commitment deadline August 2, 2026)"
  ],
  "level": "top-tier",
  "key_references": [
    "Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits (PCNet, arXiv 2605.05953, May 2026)",
    "Steering When Necessary: Flexible Steering Large Language Models with Backtracking (FASB, arXiv 2508.17621, NeurIPS 2025)",
    "Spherical Steering: Geometry-Aware Activation Rotation for Language Models (arXiv 2602.08169, ICML 2026)",
    "Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination (arXiv 2605.05686, May 2026)",
    "Hallucination Basins: A Dynamic Framework for Understanding and Controlling LLM Hallucinations (arXiv 2604.04743, April 2026)",
    "Steering Vector Fields for Context-Aware Inference-Time Control in Large Language Models (SVF, arXiv 2602.01654, Feb 2026)",
    "Curveball Steering: The Right Direction To Steer Isn't Always Linear (arXiv 2603.09313, March 2026)",
    "Minimizing Collateral Damage in Activation Steering (COAST, arXiv 2605.01167, May 2026)",
    "Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention (FLAS, arXiv 2605.05892, May 2026)",
    "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations (Ji et al., EMNLP 2025 Outstanding Paper, arXiv 2503.14477)",
    "Tethered Reasoning (HELIX): Decoupling Entropy from Hallucination in Quantized LLMs via Manifold Steering (arXiv 2602.17691, Feb 2026)",
    "Adaptive Activation Steering: A Tuning-Free LLM Truthfulness Improvement Method (ACT, WWW 2025)",
    "ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment (ICLR 2026, arXiv 2602.17560)",
    "Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry (arXiv 2605.13772, May 2026)",
    "DRIFT: Detecting Representational Inconsistencies for Factual Truthfulness (arXiv 2601.14210, Jan 2026)",
    "Guiding Giants: Lightweight Controllers for Weighted Activation Steering in LLMs (arXiv 2505.20309, May 2025)",
    "Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics (arXiv 2604.15400, April 2026)",
    "Think in Sentences: Explicit Sentence Boundaries Enhance Language Model's Capabilities (arXiv 2604.10135, April 2026)",
    "A Simple Unified Framework for Detecting Out-of-Distribution Samples and Adversarial Attacks (Lee et al., NeurIPS 2018)",
    "Semantics-Adaptive Activation Intervention for LLMs via Dynamic Steering Vectors (SADI, arXiv 2410.12299, 2024)",
    "Dynamic Multimodal Activation Steering for Hallucination Mitigation in Large Vision-Language Models (ICLR 2026)"
  ],
  "description": "We propose Claim-Level Selective Activation Steering (CLSAS), a method that bridges the granularity gap between token-level hallucination detection/intervention and claim-level factual evaluation. The central insight is that intervention granularity should match evaluation granularity: since factuality is assessed per-claim (FActScore, human judgment), steering decisions should be per-claim—preserving entire correct sentences untouched while steering only claims where the model lacks factual grounding.\n\nThe motivation is concrete: PCNet (May 2026), the state-of-the-art in selective geometric gating, achieves near-perfect token-level hallucination detection (AUROC up to 99% on extractive QA) yet still corrupts 53.7% of originally correct generations when intervening token-by-token via contrastive decoding. We hypothesize this corruption stems from the granularity mismatch—token-level anomaly conflates stylistic deviation with factual error, and sub-claim interventions damage partially correct claims.\n\nCLSAS monitors geometric distance from residual stream activations to factual cluster centroids at sentence boundaries during generation. Building on the finding that Euclidean geometric margin separates correct recall from hallucination (AUROC 0.858 on TruthfulQA; Attractor Geometry, May 2026), we evaluate both Euclidean and Mahalanobis distance triggers—the latter a hypothesized improvement motivated by OOD detection literature (Lee et al., NeurIPS 2018) that we validate via ablation. When distance indicates basin absence, CLSAS computes an input-specific steering vector toward the factual centroid and applies it with per-layer weights from a lightweight MLP controller. Sentences within a factual basin are left entirely untouched.\n\nCLSAS addresses limitations in the closest concurrent work: (1) vs. PCNet (May 2026, MC1 0.51 on Llama-3.1-8B), CLSAS makes sentence-level binary decisions that avoid sub-claim corruption. PCNet's token-level NLL gating triggers at 41-78% of tokens (IGR), requiring costly lookahead evaluations at each; CLSAS intervenes only at sentence boundaries. (2) vs. FASB (NeurIPS 2025, MC1 48.71% on LLaMA-2-7B-Chat), CLSAS is pre-emptive—gating before generation rather than detecting deviation and rolling back 10 tokens. (3) vs. Spherical Steering (ICML 2026, +15% MC1), CLSAS makes binary claim-level steer/skip decisions rather than continuous per-token rotation, enabling complete preservation of correct claims. (4) vs. Hallucination Basins (April 2026), CLSAS provides within-sequence selectivity rather than uniform per-sequence correction.\n\nWe explicitly validate the timing hypothesis (distance at boundary N predicts factuality of sentence N+1) as Milestone 1 with a correlation study, noting the Attractor Geometry paper's disclaimer that results were measured at first-digit positions and 'transfer to open-domain settings requires further study.' A look-ahead fallback is specified if correlation is insufficient. We hypothesize CLSAS's advantage over token-level methods will be strongest on long-form generation (FActScore) where multiple claims coexist and token-level corruption compounds.\n\nMinimum viable scope for 9 remaining days: single model (Llama-3.1-8B-Instruct), 4-benchmark evaluation (TruthfulQA, FActScore, SimpleQA, MT-Bench), 2×2 ablation grid (distance metric × gating granularity), direct comparison with Spherical Steering and FASB using released code. Total budget: ≤140 H100-hours.",
  "project_name": "claim_level_selective_steering",
  "source": "web_research"
}
```

Please output this JSON exactly as provided, ensuring it is valid JSON. Do not add any text before or after the JSON.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "6c31b04f-5b26-44ca-b486-31fab11de0b0",
  "agentId": "ace13499b3290f5f7",
  "type": "user",
  "uuid": "981d8278-ff3e-4df6-bfa3-9e198e2786d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T09:15:03.984Z_

```json
{
  "parentUuid": "981d8278-ff3e-4df6-bfa3-9e198e2786d5",
  "isSidechain": true,
  "agentId": "ace13499b3290f5f7",
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
      "TaskStop",
      "TodoWrite",
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
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "977538ff-0141-464a-9c40-41f8062e62dd",
  "timestamp": "2026-05-16T09:15:03.984Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-16T09:16:50.604Z_



```json
{
  "change_type": "major",
  "title": "Claim-Level Selective Activation Steering for Factual Hallucination Suppression in Long-Form Generation",
  "core_problem": "Factual hallucination in LLMs has spurred a proliferation of geometry-aware detection and activation steering methods, yet a fundamental granularity mismatch persists: detection and intervention operate at token level, while factual evaluation operates at claim/sentence level. PCNet (May 2026) exemplifies this—its probabilistic-circuit gating achieves near-perfect detection AUROC yet still corrupts 53.7% of originally correct generations when intervening at every deviant token, because token-level decisions cannot distinguish 'this token is anomalous within an otherwise correct claim' from 'this claim is genuinely hallucinated.' FASB (NeurIPS 2025) addresses selective steering but operates correctively—detecting deviation after tokens are generated, then backtracking 10 tokens—which wastes compute and splits coherent claims. Spherical Steering (ICML 2026) applies per-token rotation with continuous vMF-gated intensity, achieving strong TruthfulQA gains but intervening indiscriminately across all claims. The Attractor Geometry paper (May 2026) demonstrates that Euclidean geometric margin separates correct recall from hallucination (AUROC 0.858 on TruthfulQA vs. entropy 0.656), but this result is detection-only and measured at first-digit positions on factoid completion—translation into targeted intervention at appropriate granularity during multi-sentence generation remains the open challenge.",
  "opportunity": "The unexploited sweet spot is pre-emptive claim-level gating: sentences are the natural unit of factual claims—the granularity FActScore evaluates, the granularity humans judge, and the granularity at which LLMs integrate context before next-sentence planning (supported by 'Think in Sentences,' April 2026). The key evidence that this granularity matters comes from PCNet's results: despite near-perfect token-level detection (AUROC up to 99% on extractive QA), its token-level intervention still corrupts 53.7% of correct generations and preserves only 79.3%. This is because anomaly at individual token positions does not reliably indicate that the entire claim is hallucinated—a high-NLL token may be stylistically unusual but factually correct, or may be part of a partially correct claim that token-level correction damages. A system that makes binary steer/skip decisions at sentence boundaries—preserving entire correct claims untouched while steering only claims where the model lacks factual grounding—can achieve higher preservation rates by avoiding sub-claim intervention entirely. The three-part framework (when: sentence boundaries; whether: geometric distance trigger; how much: per-layer intensity) addresses limitations in all current methods: PCNet's token-level corruption, FASB's corrective backtracking overhead, Spherical Steering's indiscriminate application, and Hallucination Basins' per-sequence uniformity.",
  "landscape": "**Selective geometric gating (primary competitors):**\n\n*PCNet (arXiv 2605.05953, May 2026)* is the closest concurrent work sharing the 'detect geometric anomaly → selectively intervene' paradigm. PCNet trains a Probabilistic Circuit as a density estimator over MLP-compressed residual stream states (4096→128 dims), computes exact NLL as anomaly score, and triggers PC-LDCD (contrastive decoding) only at deviant tokens. Results: TruthfulQA MC1 0.51 / MC2 0.65 on Llama-3.1-8B; near-perfect detection AUROC on extractive QA; corruption rate 53.7%, preservation rate 79.3%. Overhead: <2% for PC scoring, but 3.3–6.2 additional block evaluations per anomalous token for lookahead. GTS differs in three fundamental ways: (a) Granularity: sentence-level binary decisions preserve entire correct claims and avoid sub-claim corruption. PCNet evaluates NLL at every token, meaning intervention can damage partially correct claims—evidenced by its 53.7% corruption rate despite near-perfect detection. GTS's claim-level atomicity should achieve substantially lower corruption. (b) Intervention mechanism: activation steering shifts the model's own generation distribution toward factual attractors in a single forward pass, while contrastive decoding requires maintaining lookahead evaluations for top-k candidates at every anomalous position (PCNet's IGR ranges 0.41–0.78, meaning lookahead triggers at 41–78% of tokens). On long-form generation where many tokens are flagged, GTS's steering-only approach avoids this per-token lookahead cost. (c) Trigger interpretability: Euclidean/Mahalanobis distance from factual cluster centroids has a clear geometric interpretation (distance in representation space), while NLL from a trained probabilistic circuit is a learned density estimate whose failure modes are less transparent.\n\n*FASB (arXiv 2508.17621, NeurIPS 2025)* is the most direct prior work on 'when to steer,' using linear probes trained on attention head activations. It monitors concatenated question-and-generated-content states, triggers intervention when deviation is detected, and backtracks s=10 tokens to regenerate with steering. MC1 48.71% on TruthfulQA (LLaMA-2-7B-Chat). GTS differs in: (a) pre-emptive gating at sentence boundaries (no wasted tokens, no rollback) vs. FASB's corrective backtracking; (b) geometric distance trigger measuring knowledge absence vs. learned directional alignment on attention heads; (c) atomic claim-level decisions vs. token-level cuts that may split coherent claims. FASB's backtracking overhead scales linearly with intervention frequency—compounding on hallucination-dense long-form passages.\n\n**Geometry-aware steering (per-token):** Spherical Steering (arXiv 2602.08169, ICML 2026) uses geodesic rotation with a von Mises-Fisher confidence gate, achieving MC1 +15.80% on TruthfulQA (Llama-3.1-8B) with single-layer intervention (layer 24). Code released at github.com/chili-lab/Spherical-Steering. Per-token with continuous intensity—no claim-level selectivity. Hallucination Basins (arXiv 2604.04743, April 2026) proposes Adaptive Geometry-Aware Steering using Euclidean distance triggers and logistic-regression scalar maps at per-sequence granularity (uniform across all claims). Tested on 1B–8B models. GTS advances beyond both via within-sequence sentence-level selectivity.\n\n**Context-dependent directions:** Steering Vector Fields (SVF, arXiv 2602.01654, Feb 2026) learns differentiable concept-scoring MLPs for context-aware steering directions refreshed every K steps. Always steers—no gating. Complementary to GTS (GTS decides whether; SVF decides in which direction).\n\n**Utility preservation:** COAST (arXiv 2605.01167, May 2026) formalizes collateral damage as unintended feature-direction shifts and optimizes the steering vector via constrained optimization. Complementary to GTS (COAST optimizes the vector; GTS optimizes when to apply it).\n\n**Nonlinear geometry:** Curveball Steering (arXiv 2603.09313, March 2026) demonstrates substantial geometric distortion in activation spaces, supporting covariance-aware (Mahalanobis) over Euclidean distance.\n\n**Detection-only:** Attractor Geometry of Transformer Memory (arXiv 2605.05686, May 2026) demonstrates hallucination = basin absence with Euclidean geometric margin AUROC 0.858 on TruthfulQA (vs. entropy 0.656), 0.993 on controlled factoid tasks. All measurements at first-digit positions before autoregressive dynamics compound; the paper explicitly states 'transfer to open-domain settings requires further study.' Where Does Reasoning Break? (arXiv 2605.13772, May 2026) detects step-level hallucination via transport geometry. DRIFT (arXiv 2601.14210, Jan 2026) detects representational instability.\n\n**Calibration:** Calibrating Verbal Uncertainty (Ji et al., EMNLP 2025 Outstanding Paper) achieves ~31.9% reduction in confident hallucinations via linear-feature intervention—calibrates expression, does not correct generation.\n\n**Other steering:** ACT (WWW 2025), ODESteer (ICLR 2026, +5.7% over ACT), Guiding Giants/WAS (arXiv 2505.20309), SADI (arXiv 2410.12299), HELIX/Tethered Reasoning (arXiv 2602.17691). FLAS (arXiv 2605.05892, May 2026) learns concept-conditioned velocity fields for multi-step activation transport.\n\n**Supporting evidence:** Hallucination as Trajectory Commitment (arXiv 2604.15400, April 2026) provides causal evidence for early commitment with asymmetric attractor dynamics—supporting timely intervention before commitment propagates. Think in Sentences (arXiv 2604.10135, April 2026) demonstrates sentence boundary attention concentration patterns.",
  "approach": "We propose Claim-Level Selective Activation Steering (CLSAS), a method that bridges the granularity gap between token-level detection/intervention and claim-level factual evaluation. The central insight is that intervention granularity should match evaluation granularity: since factuality is assessed per-claim (FActScore, human judgment), steering decisions should be made per-claim—preserving entire correct sentences untouched while steering only sentences where the model lacks factual grounding.\n\n**Stage 1: TRIGGER (Geometric Distance at Sentence Boundaries)**\nDuring generation, at each sentence boundary (period/newline tokens), extract hidden-state activations at the boundary token across layers using nnsight intervention hooks. Compute geometric distance from factual cluster centroids:\n(a) Offline: From a calibration set (~2K examples from TruthfulQA + FELM correct-answer forward passes), collect hidden states at factual completion positions. Apply PCA to project from full hidden dimension (d=4096) to top-k principal components (k=256), yielding a well-conditioned 256×256 covariance matrix.\n(b) Online: Project the boundary token's activation into the PCA subspace. Compute distance to nearest factual centroid. We evaluate two distance metrics: (i) Euclidean distance δ_E(x) = ||h_pca − μ_pca||₂, matching the Attractor Geometry paper's validated metric (AUROC 0.858 on TruthfulQA); (ii) Mahalanobis distance δ_M(x) = √((h_pca − μ_pca)ᵀ Σ_pca⁻¹ (h_pca − μ_pca)), a hypothesized improvement motivated by OOD detection literature (Lee et al., NeurIPS 2018) that accounts for directional anisotropy in representation space.\n(c) When distance exceeds a calibrated threshold (set via precision-recall analysis targeting high precision ≥0.85 to minimize false interventions), flag the upcoming sentence for steering.\n\n**Critical clarification:** The 0.858 AUROC motivating this trigger was achieved with Euclidean distance on first-digit positions during factoid completion (Attractor Geometry, May 2026). Our application to sentence boundaries during multi-sentence open-ended generation is an extrapolation that we explicitly validate as Milestone 1. The Attractor Geometry authors note 'transfer to open-domain settings requires further study.' If Mahalanobis does not significantly outperform Euclidean in our ablation, the primary novelty contribution rests on claim-level selective gating itself—which remains differentiated from all baselines regardless of distance metric.\n\n**Timing Hypothesis Validation (Milestone 1, Days 1-2):**\nWe explicitly frame the following as a testable hypothesis: geometric distance at sentence boundary N is predictive of factual accuracy in sentence N+1. Validation protocol: (1) Generate 500 multi-sentence responses on LongFact/FActScore prompts using Llama-3.1-8B-Instruct. (2) Compute both Euclidean and Mahalanobis distance at every sentence boundary. (3) Annotate each subsequent sentence with FActScore. (4) Measure Spearman correlation between boundary distance and next-sentence factuality, and AUROC for binary classification. If AUROC < 0.70, we implement a look-ahead variant: extract distance from the first 3 generated tokens of the new sentence (before committing via speculative-style buffering). The look-ahead variant adds ~15% latency overhead but operates before the sentence is visible to the user. If look-ahead also fails (AUROC < 0.65), we fall back to a sliding-window approach using the mean distance over the last 5 tokens before the boundary.\n\n**Comparison to PCNet's trigger:** PCNet uses NLL from a trained probabilistic circuit as its anomaly score, evaluated at every token. This achieves near-perfect detection on extractive QA but still yields 53.7% corruption on correct generations. We hypothesize this is because token-level anomaly conflates stylistic deviation with factual error. Our sentence-level trigger aggregates geometric information at natural claim boundaries, making a single binary decision per claim—either the model has factual grounding for this claim (skip) or it doesn't (steer). This avoids sub-claim intervention entirely.\n\n**Stage 2: DIRECTION (Centroid-Directed Steering Vector)**\nCompute the steering direction as the unit vector from the current activation toward the factual cluster centroid at each layer in the PCA subspace, then project back to full space: v_steer = (μ_pca − h_pca) / ||μ_pca − h_pca||, lifted back to full dimensionality via PCA inverse transform. This yields an input-specific correction direction toward regions of successful fact recall.\n\n**Stage 3: INTENSITY (Per-Layer Weighted Steering)**\nA lightweight 2-layer MLP controller (hidden dim 64, inspired by Guiding Giants/WAS) takes [geometric_distance, layer_index/L, distance_velocity] as input (3D feature vector) and predicts per-layer steering weight λ_ℓ. Trained on a calibration set (~2K examples) to maximize FActScore on steered outputs while minimizing perplexity increase on non-flagged outputs. Steering: h_steered(ℓ) = h(ℓ) + λ_ℓ · v_steer(ℓ) at layers where λ_ℓ > ε.\n\n**Minimum Viable Scope (9 days, May 16–25):**\n- Days 1-2 (May 16-17): Timing hypothesis validation on Llama-3.1-8B-Instruct. This is the critical-path milestone—if it fails, immediately implement look-ahead variant.\n- Days 3-4 (May 18-19): Core CLSAS implementation + calibration. Run TruthfulQA and SimpleQA.\n- Days 5-6 (May 20-21): Run baselines (Spherical Steering from released code, FASB from released code). Run FActScore and MT-Bench on CLSAS.\n- Days 7-8 (May 22-23): Key ablations: 2×2 grid (Euclidean vs Mahalanobis × sentence-level vs token-level gating) on 4-benchmark core set. PCNet comparison if code is available; otherwise use reported numbers with matched model.\n- Day 9 (May 24): Writing, formatting, submission buffer.\n- Dropped from scope: COAST combination experiment, Qwen3-8B (secondary model), full 7-benchmark suite for ablations, GTS-FASB-trigger ablation.\n\n**Ablation Design (MVP):**\n- CLSAS-full vs. CLSAS-Euclidean (isolate Mahalanobis contribution)\n- CLSAS-full vs. CLSAS-pertoken (apply continuous per-token gating with our distance metric, matching PCNet/Spherical Steering's granularity—isolates the claim-level contribution)\n- CLSAS-full vs. CLSAS-sequence (single decision per sequence, matching Hallucination Basins' granularity)\n- CLSAS-full vs. CLSAS-scalar (replace per-layer MLP with single scalar, isolating controller contribution)\n- Direct comparison: CLSAS-full vs. Spherical Steering vs. FASB vs. PCNet (reported numbers if code unavailable)\n\n**Primary evaluation metrics:**\n- Corruption rate and preservation rate (matching PCNet's protocol): fraction of correct claims degraded / preserved by intervention\n- FActScore on long-form biographies (primary benchmark where claim-level advantage should be largest)\n- TruthfulQA MC1/MC2, SimpleQA accuracy, MT-Bench score\n- Intervention rate: fraction of sentences steered (lower is better for comparable factuality gains)\n- Latency overhead vs. baselines\n\nImplementation uses nnsight 0.7 on Llama-3.1-8B-Instruct. Qwen3-8B included only if time permits after MVP completion.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~120h H100 80GB",
      "gpu_utilization": "Low (~15-20%)",
      "timeline": "3-4 months",
      "team": "1-2 researchers with mechanistic interpretability + geometric ML experience",
      "estimated_gpu_cost": "$360-400",
      "factScore_api_cost": "$100-200"
    },
    "human_in_loop": {
      "gpu_hours": "~130h H100 80GB",
      "gpu_utilization": "Moderate (45-55%)",
      "timeline": "2-3 weeks",
      "team": "1 researcher, ~30min/day reviewing proposals",
      "claude_api_cost": "$150-250",
      "estimated_gpu_cost": "$390-430",
      "factScore_api_cost": "$100-200",
      "risk_note": "Timing hypothesis validation is critical-path. If it fails (AUROC < 0.70), look-ahead fallback adds ~3 days."
    },
    "auto_research": {
      "gpu_hours": "~140h H100 80GB",
      "gpu_utilization": "High (~85-90%)",
      "timeline": "9 days (May 16-25) with 2 H100 GPUs. Minimum viable paper scope: single model (Llama-3.1-8B), 4-benchmark core set for ablations, full baselines on FActScore+TruthfulQA+SimpleQA+MT-Bench.",
      "team": "0 (initial setup: provision GPUs, configure nnsight 0.7, clone Spherical Steering + FASB repos)",
      "claude_api_cost": "$250-350 (est. 3000-4000 turns)",
      "estimated_gpu_cost": "$420-450",
      "factScore_api_cost": "$100-200",
      "speed_bottleneck": "Timing hypothesis validation (days 1-2) is critical path. If it fails, look-ahead variant must be implemented immediately. Secondary: FActScore GPT-4 API calls.",
      "resource_optimization": "Budget achieved via: (1) single model (Llama-3.1-8B) for all experiments; (2) 4-benchmark core set (TruthfulQA, FActScore, SimpleQA, MT-Bench); (3) 2×2 ablation grid (distance metric × gating granularity) instead of separate sweeps; (4) use Spherical Steering and FASB released code directly; (5) PCNet comparison using reported numbers if code unavailable.",
      "minimum_viable_paper": "If timing hypothesis fails AND look-ahead also fails: pivot to a detection-only contribution (sentence-level geometric detection benchmark) comparing Euclidean/Mahalanobis at sentence boundaries vs. PCNet's token-level NLL. This is publishable as a shorter paper (findings track).",
      "risk_note": "Primary risk: timing hypothesis may fail (Attractor Geometry paper validated only on factoid completion at first-digit positions, explicitly disclaiming open-domain transfer). Mitigation: look-ahead variant, then sliding-window fallback. Secondary risk: claim-level gating may not outperform PCNet's token-level gating on short-form QA—advantage expected primarily on long-form generation (FActScore, LongFact). Tertiary risk: 9-day timeline leaves zero buffer for unexpected implementation issues."
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR submission deadline May 25, 2026; commitment deadline August 2, 2026)"
  ],
  "level": "top-tier",
  "key_references": [
    "Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits (PCNet, arXiv 2605.05953, May 2026)",
    "Steering When Necessary: Flexible Steering Large Language Models with Backtracking (FASB, arXiv 2508.17621, NeurIPS 2025)",
    "Spherical Steering: Geometry-Aware Activation Rotation for Language Models (arXiv 2602.08169, ICML 2026)",
    "Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination (arXiv 2605.05686, May 2026)",
    "Hallucination Basins: A Dynamic Framework for Understanding and Controlling LLM Hallucinations (arXiv 2604.04743, April 2026)",
    "Steering Vector Fields for Context-Aware Inference-Time Control in Large Language Models (SVF, arXiv 2602.01654, Feb 2026)",
    "Curveball Steering: The Right Direction To Steer Isn't Always Linear (arXiv 2603.09313, March 2026)",
    "Minimizing Collateral Damage in Activation Steering (COAST, arXiv 2605.01167, May 2026)",
    "Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention (FLAS, arXiv 2605.05892, May 2026)",
    "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations (Ji et al., EMNLP 2025 Outstanding Paper, arXiv 2503.14477)",
    "Tethered Reasoning (HELIX): Decoupling Entropy from Hallucination in Quantized LLMs via Manifold Steering (arXiv 2602.17691, Feb 2026)",
    "Adaptive Activation Steering: A Tuning-Free LLM Truthfulness Improvement Method (ACT, WWW 2025)",
    "ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment (ICLR 2026, arXiv 2602.17560)",
    "Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry (arXiv 2605.13772, May 2026)",
    "DRIFT: Detecting Representational Inconsistencies for Factual Truthfulness (arXiv 2601.14210, Jan 2026)",
    "Guiding Giants: Lightweight Controllers for Weighted Activation Steering in LLMs (arXiv 2505.20309, May 2025)",
    "Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics (arXiv 2604.15400, April 2026)",
    "Think in Sentences: Explicit Sentence Boundaries Enhance Language Model's Capabilities (arXiv 2604.10135, April 2026)",
    "A Simple Unified Framework for Detecting Out-of-Distribution Samples and Adversarial Attacks (Lee et al., NeurIPS 2018)",
    "Semantics-Adaptive Activation Intervention for LLMs via Dynamic Steering Vectors (SADI, arXiv 2410.12299, 2024)",
    "Dynamic Multimodal Activation Steering for Hallucination Mitigation in Large Vision-Language Models (ICLR 2026)"
  ],
  "description": "We propose Claim-Level Selective Activation Steering (CLSAS), a method that bridges the granularity gap between token-level hallucination detection/intervention and claim-level factual evaluation. The central insight is that intervention granularity should match evaluation granularity: since factuality is assessed per-claim (FActScore, human judgment), steering decisions should be per-claim—preserving entire correct sentences untouched while steering only claims where the model lacks factual grounding.\n\nThe motivation is concrete: PCNet (May 2026), the state-of-the-art in selective geometric gating, achieves near-perfect token-level hallucination detection (AUROC up to 99% on extractive QA) yet still corrupts 53.7% of originally correct generations when intervening token-by-token via contrastive decoding. We hypothesize this corruption stems from the granularity mismatch—token-level anomaly conflates stylistic deviation with factual error, and sub-claim interventions damage partially correct claims.\n\nCLSAS monitors geometric distance from residual stream activations to factual cluster centroids at sentence boundaries during generation. Building on the finding that Euclidean geometric margin separates correct recall from hallucination (AUROC 0.858 on TruthfulQA; Attractor Geometry, May 2026), we evaluate both Euclidean and Mahalanobis distance triggers—the latter a hypothesized improvement motivated by OOD detection literature (Lee et al., NeurIPS 2018) that we validate via ablation. When distance indicates basin absence, CLSAS computes an input-specific steering vector toward the factual centroid and applies it with per-layer weights from a lightweight MLP controller. Sentences within a factual basin are left entirely untouched.\n\nCLSAS addresses limitations in the closest concurrent work: (1) vs. PCNet (May 2026, MC1 0.51 on Llama-3.1-8B), CLSAS makes sentence-level binary decisions that avoid sub-claim corruption. PCNet's token-level NLL gating triggers at 41-78% of tokens (IGR), requiring costly lookahead evaluations at each; CLSAS intervenes only at sentence boundaries. (2) vs. FASB (NeurIPS 2025, MC1 48.71% on LLaMA-2-7B-Chat), CLSAS is pre-emptive—gating before generation rather than detecting deviation and rolling back 10 tokens. (3) vs. Spherical Steering (ICML 2026, +15% MC1), CLSAS makes binary claim-level steer/skip decisions rather than continuous per-token rotation, enabling complete preservation of correct claims. (4) vs. Hallucination Basins (April 2026), CLSAS provides within-sequence selectivity rather than uniform per-sequence correction.\n\nWe explicitly validate the timing hypothesis (distance at boundary N predicts factuality of sentence N+1) as Milestone 1 with a correlation study, noting the Attractor Geometry paper's disclaimer that results were measured at first-digit positions and 'transfer to open-domain settings requires further study.' A look-ahead fallback is specified if correlation is insufficient. We hypothesize CLSAS's advantage over token-level methods will be strongest on long-form generation (FActScore) where multiple claims coexist and token-level corruption compounds.\n\nMinimum viable scope for 9 remaining days: single model (Llama-3.1-8B-Instruct), 4-benchmark evaluation (TruthfulQA, FActScore, SimpleQA, MT-Bench), 2×2 ablation grid (distance metric × gating granularity), direct comparison with Spherical Steering and FASB using released code. Total budget: ≤140 H100-hours.",
  "project_name": "claim_level_selective_steering",
  "source": "web_research"
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "977538ff-0141-464a-9c40-41f8062e62dd",
  "isSidechain": true,
  "agentId": "ace13499b3290f5f7",
  "requestId": "req_011Cb5zakWhoTiXkKFMR9a6G",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "56e19716-4169-4f48-88f2-79a3a579096e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012oGU91qbcfVUvSewm6B1wU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16112,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16112,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---
