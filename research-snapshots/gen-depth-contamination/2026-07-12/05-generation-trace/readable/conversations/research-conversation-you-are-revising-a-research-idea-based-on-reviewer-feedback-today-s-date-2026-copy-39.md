# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-10 (UTC).** ## Original idea { "tit

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 46
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-2/f0b9fbaa-4159-4906-9e7b-5c7c38fdb4da.jsonl`
- **Structured JSON:** [`a3deb9e230c4c3ca457f.json`](../../sessions/a3/a3deb9e230c4c3ca457f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T09:30:25.808Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T09:30:25.808Z",
  "sessionId": "f0b9fbaa-4159-4906-9e7b-5c7c38fdb4da",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-10 (UTC).**\n\n## Original idea\n{\n  \"title\": \"Latent-Distribution Candidate Selection for Frozen World Action Models: OOD Consistency Scoring and Action-Latent Value Learning\",\n  \"core_problem\": \"Pretrained WAMs generate a single action trajectory at inference and provide no mechanism to compare candidate futures. Adding planning capability currently requires one of three costly interventions: (1) full fine-tuning of the video model on robot demos (Cosmos Policy, ICLR 2026: 384–3,072 H100-hours); (2) training a separate action-conditioned world model alongside the frozen policy (GPC, RAL 2025); or (3) architectural co-design or RL loops (H-WM, GigaBrain RAMP, WAV). Fast-WAM (arXiv 2603.16666) demonstrates that action-only inference achieves 97.6% on LIBERO (Table 2) and 91.8% on RoboTwin (Table 1) at 190ms, motivating candidate generation from frozen WAM action-only inference rather than expensive video rollouts.\\n\\nThe test-time candidate selection literature (2024–2026) has established three tiers of action representation for scoring candidates, with each tier providing increasingly structured quality-discriminative geometry:\\n\\n**Tier 1 — Cartesian action space**: V-GPS (arXiv 2410.13816, CoRL 2024) trains a Q-function via offline RL (Cal-QL) on raw 7-dimensional Cartesian action vectors concatenated with ResNet-34 image embeddings, scoring K=50 candidates from frozen generalist policies (Octo, RT-1X, OpenVLA) and achieving +82.8% relative improvement on real-robot tasks — establishing that value-function re-ranking of frozen policies works in Cartesian+image space. KDPE (arXiv 2508.10511, CoRL 2025) applies kernel density estimation to Cartesian action trajectories (end-effector position, SO(3)-orientation, gripper state) from Diffusion Policy to filter multimodal outputs, generating N=100 candidates; achieves 88.2% vs. 85% on RoboMimic/MimicGen. Critical KDPE finding: KDPE-OOD (selecting the most out-of-distribution trajectory) performs worse than KDPE (selecting the most typical) — confirming that in-distribution selection is the correct direction. Both Tier 1 methods operate on low-dimensional raw action representations with no latent structure encoding physical plausibility beyond what is captured by pixel-level image embeddings.\\n\\n**Tier 2 — VLA action tokens**: MG-Select (arXiv 2510.05681, ICLR 2026) uses KL-divergence from a masked unconditional VLA distribution as a training-free confidence signal, achieving 168% relative improvement on RoboCasa pick-and-place. RoVer (arXiv 2510.10975, ICLR 2026) trains a 0.2B Process Reward Model that scores candidates from frozen VLAs. Both operate on VLA action tokens from architectures trained on language-action pairs without joint video-action pretraining, lacking the video-physics co-regularization that structures WAM action latents.\\n\\n**Tier 3 — WAM action latents** (this paper's domain): UWM and DreamZero generate action latents z_a from joint video-action diffusion pretraining. Cosmos Policy (ICLR 2026) implements Best-of-N in its planning mode by generating B candidates and scoring each via a fine-tuned value function — but requires rollout fine-tuning (1,536 H100-hours for RoboCasa) because demonstration-only training 'cannot correctly predict failure states.'\\n\\nThe central unanswered question — which Tier 1 and Tier 2 approaches cannot answer — is: (1) Do WAM action latents z_a, regularized by joint video-action pretraining, form a latent success distribution that is more structured and separable from failure regimes than VLA action tokens (Tier 2) or Cartesian action representations (Tier 1), enabling lightweight OOD-based candidate scoring without any rollout data? (2) Does operating in WAM latent space alone (without needing an image at inference) enable a more compact, efficient quality discriminator than Tier 1 methods that require both image and action? These questions are grounded in the FAIL-Detect (arXiv 2503.08558, RSS 2025) finding that OOD detection on success-only demonstrations reliably identifies failures — but have not been applied to WAM action latents or to pre-execution candidate selection.\\n\\nImportant caveat on z_a geometry: In action-only inference (video timestep = T), video tokens are at full noise and provide no inference-time conditioning. The quality-discriminative structure of z_a is therefore a training-time property — joint pretraining causes the model to learn representations where z_a co-varies with visual futures, but whether this geometry persists as a success/failure discriminator when video is absent at inference is not proven a priori. Step 1 (LOC diagnostic) is the first empirical test. If H1 fails (AUC < 0.55), LOC reports a negative result and Value MLP becomes the sole primary contribution.\\n\\nThe companion question of whether video denoising error (as opposed to latent OOD scoring) is a reliable zero-training signal is answered negatively by Cosmos Policy's own finding and by EVA (arXiv 2603.17808), which demonstrates an 'executability gap' showing that visual coherence does not predict task success.\\n\\nNo existing work demonstrates Best-of-N candidate selection using WAM action latents' distributional structure — either zero-training (OOD scoring) or lightweight-trained (value MLP) — without modifying any WAM weights or requiring rollout data for the zero-training path. The three-tier hierarchy predicts that z_a offers the richest quality-discriminative geometry for frozen-policy candidate selection, a hypothesis this paper tests empirically.\",\n  \"opportunity\": \"UWM's independent per-modality diffusion timestep architecture (RSS 2025) natively supports action-only inference (video timestep = T, action timestep = 0), producing action latents z_a jointly pretrained with video. This creates two complementary WAM-specific approaches to candidate selection:\\n\\n**Method 1 — Latent OOD Consistency Scoring (LOC, zero weight updates)**: Encode LIBERO-90 success demonstrations through frozen UWM in action-only mode to obtain a reference distribution {z_a^success}. Fit a lightweight density estimator — KNN-based nonconformity score (k=10) or Gaussian Mixture Model (k≤5 components) — on {z_a^success}. At inference, sample B=4–8 action-only candidates from frozen UWM, obtain latents {z_{a,1}, ..., z_{a,B}}, and score each: S_LOC(z_{a,i}) = −log p̂(z_{a,i}) (nonconformity score). Select a_{i*} = argmin_i S_LOC(z_{a,i}) (most in-distribution candidate). Total inference overhead: B × ~5ms = 20–40ms for B=4–8. Cost: ~30–60 minutes to fit density estimator on encoded latents; no WAM weight updates.\\n\\nTheoretical basis: (1) FAIL-Detect (RSS 2025) proves that OOD detection on success-only demonstration data reliably detects policy failures — the success-demo distribution implicitly excludes failure modes; (2) KDPE (CoRL 2025) demonstrates in Cartesian action space that selecting the most IN-distribution trajectory improves performance, while KDPE-OOD performs worse — validating the in-distribution selection direction for LOC; (3) z_a from joint video-action pretraining is hypothesized to encode physical plausibility in a tighter quality-discriminative geometry than both Cartesian action space (KDPE, V-GPS) and VLA action tokens. **Inference-time caveat**: In action-only mode, video tokens are at full noise (timestep T) — this quality-discriminative geometry is a training-time property of the learned weights, not an inference-time video conditioning effect. Step 1 empirically tests whether this training-time property persists as a quality signal without video input. LOC is reported as a negative result if AUC < 0.55.\\n\\nKey differentiation from KDPE and V-GPS (Tier 1 methods): (a) density estimation in WAM action latent space z_a, not Cartesian action space (position/orientation/gripper) or 7D delta actions; (b) success-demonstrations-only reference distribution establishing a quality anchor, not all training data (KDPE) or a separately collected offline RL dataset (V-GPS); (c) no image required at inference — z_a encodes visual-physical context from joint pretraining, unlike V-GPS which concatenates a ResNet-34 image embedding with the raw action for every candidate; (d) B=4–8 candidates vs. KDPE's N=100 and V-GPS's K=50. LOC implements success-mode latent selection; KDPE implements Cartesian-space all-data-mode selection; V-GPS implements offline-RL Q-function scoring in Cartesian+image space — these are mechanistically distinct quality signals across the three representational tiers.\\n\\nDifferentiation from MG-Select: LOC scores membership in the success demonstration distribution (latent OOD density); MG-Select measures KL divergence of task-conditioned output from masked unconditional distribution (action-space distributional uncertainty).\\n\\nNote on Cosmos Policy planning mode: Cosmos Policy also implements Best-of-N — generates B actions, predicts future states and values, executes the highest-value action. However, (a) requires fine-tuning a value function on rollout data (1,536 H100-hours for RoboCasa) because demonstration-only training 'cannot correctly predict failure states'; (b) 15 total forward passes per candidate. LOC requires zero rollout data, zero weight updates, and ~5ms per candidate.\\n\\n**Method 2 — Action-Latent Value MLP (≤40 H100-hours training)**: A 3-layer MLP trained on WAM action latents z_a from LIBERO-90 success demonstrations AND explicitly collected failure trajectories scores each candidate via V(z_{a,i}) ∈ [0,1]. Hard argmax Best-of-N is the primary result. Key hypothesis: z_a regularized by joint video-action pretraining is more linearly separable between success and failure regimes than raw action outputs, VLA action tokens, or Cartesian representations — enabling a simpler, image-free quality discriminator.\\n\\nDifferentiation from V-GPS (CoRL 2024): V-GPS trains a Q-function via offline RL (Cal-QL) on (image observation, raw 7D Cartesian action) pairs — requiring both a ResNet-34 image encoder and the raw action candidate at inference; our Value MLP trains on WAM action latents z_a alone via binary success/failure supervision — no image required at inference because z_a already encodes visual-physical context from joint pretraining. V-GPS validates the value re-ranking paradigm in Cartesian+image space for VLA-family policies; our Value MLP asks whether WAM latent space provides a more compact, image-free quality signal with stronger success/failure linear separability. Additionally, V-GPS uses sparse binary rewards + Cal-QL offline RL; our Value MLP uses direct binary classification supervision, making it trainable in <5 H100-hours vs. V-GPS's offline RL pipeline. Other differentiations: (a) vs. WAV — WAV trains a trajectory value module as a new architectural component from scratch; Value MLP is plug-in-compatible with any pretrained WAM; (b) vs. RoVer — RoVer requires a 0.2B PRM trained on process labels; Value MLP uses a 3-layer MLP trained on binary success/failure labels; (c) vs. Cosmos Policy — requires 1,536 H100-hours rollout fine-tuning; Value MLP requires ≤40 H100-hours.\\n\\n**Comparison of LOC vs. Value MLP is itself a central contribution**: Their empirical comparison characterizes when WAM latent OOD scoring is sufficient versus when labeled training adds necessary discriminative power — and whether this latent-space approach outperforms Tier 1 (Cartesian + image, V-GPS) and Tier 2 (VLA token distributional uncertainty, MG-Select) methods.\\n\\n**Mandatory RoboCasa baseline validation before committing to targets**: World2Act (arXiv 2603.10422, March 2026) reports UWM achieving 60.8% on RoboCasa using 1,000 real demonstration fine-tuning. Since UWM was trained only on DROID data and has not been fine-tuned on RoboCasa tasks, the frozen UWM baseline (no RoboCasa demos) is expected to be substantially lower — likely 10–25%. Primary performance target: ≥10pp absolute improvement over the measured frozen baseline.\",\n  \"landscape\": \"Cosmos Policy (arXiv 2601.16163, ICLR 2026) is the primary comparison point for absolute performance. Fully fine-tunes Cosmos-Predict2-2B on robot demos (384 H100-hours ALOHA, 1,536 RoboCasa, 3,072 LIBERO). Achieves 98.5% LIBERO and 67.1% RoboCasa. Its planning mode implements Best-of-N candidate selection: generates B candidate actions, predicts future states (3 queries to world model) and values (5 queries to value function per future state, 15 total predictions per action), and executes via majority-mean aggregation. Key distinction: Cosmos Policy's authors explicitly state that demo-only training 'cannot correctly predict failure states' — rollout fine-tuning is required for the planning value function. LOC requires zero rollout data and zero weight updates; Value MLP requires ≤40 H100-hours vs. 1,536 H100-hours.\\n\\nV-GPS (arXiv 2410.13816, CoRL 2024) — CRITICAL PRIOR WORK for Value MLP. 'Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance.' Trains a Q-function via offline RL (Cal-QL) on sparse binary rewards from demonstration data; architecture: ResNet-34 image encoder with FiLM language conditioning, 7-dimensional Cartesian action vector concatenated with image embedding passed through 2-layer MLP to predict scalar Q-value. At inference, samples K=50 action candidates from frozen generalist policies (Octo-small, Octo-base, Octo-small-1.5, RT-1X, OpenVLA) and re-ranks by Q-value. Achieves +82.8% relative improvement on real-robot 6-task benchmark (Octo-small-1.5 baseline: 24%, V-GPS: 44%). Key differentiations from our Value MLP: (a) V-GPS operates in Cartesian+image space — requires both ResNet-34 image embedding AND raw 7D action candidate at every inference call; our Value MLP operates on WAM z_a alone — no image needed at inference because z_a encodes visual-physical context from joint pretraining; (b) V-GPS uses offline RL (Cal-QL) training pipeline; our Value MLP uses binary success/failure classification, trainable in <5 H100-hours; (c) V-GPS applies to generalist VLA policies (Cartesian action outputs without video-physics pretraining); our Value MLP exploits WAM-specific latent geometry from joint video-action pretraining. V-GPS validates the paradigm (value re-ranking of frozen policies works) in Tier 1 (Cartesian+image space); our paper asks whether Tier 3 (WAM latent space) provides a more discriminative, image-free signal.\\n\\nKDPE (arXiv 2508.10511, CoRL 2025) — CRITICAL PRIOR WORK. Applies manifold-aware KDE to Cartesian action trajectories (end-effector position/SO(3)-orientation/gripper) from Diffusion Policy; generates N=100 candidates; achieves 88.2% vs. 85% on RoboMimic/MimicGen. CRITICAL FINDING: KDPE-OOD (selecting most out-of-distribution trajectory) performs WORSE than KDPE (selecting most typical) — validates in-distribution selection direction for LOC. Differentiates from LOC: (a) Cartesian action space vs. WAM action latent space; (b) all training data vs. success-only reference; (c) no WAM-specific joint pretraining regularization; (d) N=100 candidates vs. LOC's B=4–8.\\n\\nWorld2Act (arXiv 2603.10422, March 2026) — post-training framework achieving ~66% on RoboCasa using 50 real + 50 imagined demos; reports UWM achieves 60.8% on RoboCasa with 1,000-demo fine-tuning (confirming frozen UWM baseline is ~10–25%); differentiation: World2Act requires contrastive post-training to align VLA latents; LOC exploits WAM alignment inherited from joint pretraining.\\n\\nFast-WAM (arXiv 2603.16666) — CRITICAL FRAMING: 97.6% LIBERO-avg (Table 2) and 91.8% RoboTwin (Table 1) at 190ms without video; single trajectory only; our method uses same action-only inference for candidate generation and adds LOC selection at B × 5ms overhead.\\n\\nRoVer (arXiv 2510.10975, ICLR 2026) — CRITICAL PRIOR WORK: generates B VLA candidates, trains 0.2B PRM; differentiation: requires 0.2B model training vs. LOC's zero training and Value MLP's 3-layer MLP; VLA action tokens lack video-physics regularization.\\n\\nVerifier-free Test-Time Sampling / MG-Select (arXiv 2510.05681, ICLR 2026) — CRITICAL PRIOR WORK: training-free KL-from-masked-distribution scoring for frozen VLAs; 168% relative improvement on RoboCasa pick-and-place; differentiation: MG-Select measures action-space distributional uncertainty, LOC measures latent OOD membership relative to success demo distribution.\\n\\nWorld-Value-Action (WAV) Model (arXiv 2604.14732, April 2026) — trajectory value module requiring training from scratch, new architectural component; iterative latent-space inference concentrating probability mass on high-value trajectories. Verified metrics (Table 1, Figure 2): 99.6% LIBERO overall average across 4 splits (Spatial/Object/Goal/Long, Table 1); LIBERO-Long specifically 98.1% (Table 1); 75.6% real-world average (Figure 2, dual-arm Piper robot, 15 trials per task). Note: WAV's LIBERO evaluation covers 4 benchmark splits but does not include LIBERO-90; our primary evaluation uses LIBERO-Long and RoboCasa. Differentiation: WAV trains value and world model jointly from scratch (architectural co-design); our method leaves all WAM weights frozen and is plug-in-compatible with any pretrained WAM.\\n\\nBest-of-Q (arXiv 2601.22701, January 2026) — Q-function re-ranking of frozen VLM agents for digital tasks (web/OS control); mechanistically analogous to V-GPS applied to digital agents; not in robot manipulation domain but confirms paradigm generality beyond robotics.\\n\\nALT Policy (arXiv 2505.05787, May 2025) — 'Demystifying Diffusion Policies: Action Memorization and Simple Lookup Table Alternatives': demystifies diffusion policies as implicit nearest-neighbor lookup tables, using contrastive image encoder distance in observation latent space as a runtime OOD signal for single-trajectory retrieval. Related to LOC in applying latent-space OOD proximity as a quality signal, but operates in observation (not action) latent space and retrieves a single stored trajectory rather than scoring multi-candidate selections.\\n\\nUNISafe (arXiv 2505.00779, May 2025) — 'Uncertainty-aware Latent Safety Filters for Avoiding Out-of-Distribution Failures': calibrates a world model's epistemic uncertainty via conformal prediction to detect OOD state predictions, then performs Hamilton-Jacobi reachability in augmented latent+uncertainty space to synthesize a policy-agnostic safety filter. Related to LOC in applying conformal prediction to world-model latents, but targets state-space safety intervention rather than pre-execution action-latent candidate selection for task performance.\\n\\nVLS (arXiv 2602.03973, February 2026) — 'Steering Pretrained Robot Policies via Vision-Language Models': applies VLM-generated reward gradients to steer frozen diffusion/flow-matching policies' denoising process toward semantically correct behaviors; training-free guidance via language-conditioned reward signals, not latent-space density or value functions. Different mechanism from both LOC and Value MLP; concurrent work.\\n\\nFAIL-Detect (arXiv 2503.08558, RSS 2025) — SUPPORTING WORK: proves OOD detection on success-only demonstration data reliably detects policy failures; uses flow-based density estimation on distilled policy signals; motivates LOC's use of KNN/GMM density on success demo latents; FAIL-Detect is execution-time monitoring, LOC is pre-execution candidate selection — Step 1 LOC diagnostic is the first empirical test of whether this principle transfers to pre-execution WAM z_a.\\n\\nEVA (arXiv 2603.17808, 2026) — identifies 'executability gap' showing visually coherent world model rollouts can violate kinematic constraints; supports LOC over PCS: visual denoising error does not predict task success.\\n\\nWAV: see above. Compose Your Policies! / GPC (arXiv 2510.01068) — training-free convex composition of multiple frozen policy distributions; operates at distribution level, not discrete candidate selection from single WAM. GPC-RANK (arXiv 2502.00622, IEEE RAL 2025): frozen policy + separately trained action-conditioned world model + hard argmax; uses world-model reward prediction for scoring, not WAM action latent OOD. When to Trust Imagination (arXiv 2605.06222, May 2026): FFDC adaptively decides action chunk sizes during single-trajectory execution; orthogonal and combinable.\",\n  \"approach\": \"Primary backbone: UWM (github.com/WEIRDLabUW/unified-world-model, RSS 2025), whose independent per-modality diffusion timestep architecture supports action-only inference (policy mode: video timestep = T, action timestep = 0). All WAM weights frozen throughout.\\n\\n**Step 0a — Frozen UWM Baseline Validation on RoboCasa (MANDATORY FIRST STEP)**: Run B=1 frozen UWM action-only inference on 50 episodes of representative RoboCasa tasks (kitchen manipulation subset). Expected baseline: 10–25% (UWM trained on DROID data only; World2Act reports 60.8% with 1,000-demo fine-tuning, confirming frozen baseline is substantially lower). Decision tree: if baseline ≥ 30%, proceed with current framing; if baseline 10–25%, confirm ≥10pp absolute improvement framing. Cost: ~2–3 H100-hours.\\n\\n**Step 0b — Reference Distribution Encoding for LOC**: Encode LIBERO-90 success demos through frozen UWM in action-only mode to obtain {z_a^success}. Fit density estimators: (a) KNN nonconformity model (k=10, Euclidean distance); (b) GMM (k=3,5 components, full covariance). Split latents 80/20 train/hold-out for AUC evaluation in Step 1. Cost: ~10–15 H100-hours encoding; ~30 minutes fitting density estimator. Steps 0b and 0c can run in parallel after Step 0a completes.\\n\\n**Step 0c — Failure Demonstration Collection (required for Value MLP)**: (a) Primary negatives: run frozen UWM (B=1) on LIBERO-Long and validated RoboCasa tasks; expected failure rate 30–50% on RoboCasa tasks, 5–15% on LIBERO-Long, yielding 500–2,000 failure trajectories. Cost: 15–20 H100-hours. (b) Synthetic supplement: Gaussian action perturbation (σ ∈ {0.05, 0.1}) on 20% of LIBERO-90 success demos, simulate in MuJoCo, flag truncated episodes as failures. Cost: <1 H100-hour. Combined: balanced 2,000–4,000 positive / 2,000–4,000 negative training set.\\n\\n**Step 1 — LOC Diagnostic (MANDATORY before main ablation)**: Empirically tests Hypothesis H1: 'WAM joint pretraining creates a latent success distribution where S_LOC(z_a) achieves AUC > 0.60 as a binary success predictor.' Theoretical motivation: FAIL-Detect's principle (OOD on success-only data detects failures) + KDPE's empirical confirmation (in-distribution selection outperforms outlier selection in Cartesian space). Inference-time caveat: z_a geometry is a training-time property — in action-only inference, video tokens are at full noise (timestep T) providing no inference-time conditioning. We hypothesize that joint training causes z_a to learn quality-discriminative representations even without video input, but Step 1 is the first empirical test of this hypothesis. If H1 fails (AUC < 0.55), LOC reports a negative result.\\n\\nProtocol: Sample B=16 action-only candidates from frozen UWM on 3 RoboCasa tasks, execute each in simulation (ground-truth success/failure), compute LOC and comparison scores.\\n\\nLOC metrics: (1) AUC of S_LOC as binary success predictor on held-out demos (target H1: AUC > 0.60); (2) Spearman ρ of S_LOC with success labels (target ρ > 0.3); (3) compare KNN vs. GMM density estimators. Also compute: S_PCS = ||ε − ε_θ(x_{t*}, z_{a,i}, t*)||² for the same candidates, varying t* ∈ {T/4, T/2, 3T/4} (expected to show lower AUC based on Cosmos Policy finding and EVA's executability gap); MG-Select-style KL score as Tier 2 comparison; KDPE-style Cartesian density as Tier 1 comparison baseline.\\n\\nExpected result: LOC AUC > PCS AUC ≈ MG-Select AUC ≈ KDPE-Cartesian AUC, confirming Tier 3 (WAM latent) is more informative than Tier 1 (Cartesian) and Tier 2 (VLA token distributional uncertainty) methods.\\n\\nDecision tree: if AUC ≥ 0.60, LOC is primary zero-training method; if LOC 0.55–0.60, both methods reported with LOC as secondary; if LOC < 0.55, LOC reported as negative result with informative comparison.\\n\\n**Step 2 — Diversity Pilot (combined with LOC diagnostic)**: Same B=16 rollouts measure: pairwise cosine distance of action latents {z_{a,i}} (target mean > 0.05; if lower, increase noise temperature T_noise ∈ {1.5, 2.0}); LOC AUC conditional on latent diversity.\\n\\n**Step 3 — Value MLP Training**: 3-layer MLP (input: flattened z_a; output: scalar V ∈ [0,1]) trained via binary cross-entropy on balanced success/failure latents from Steps 0b and 0c. Report binary classification accuracy on held-out split (target > 75%). Key distinction from V-GPS: no image input required at inference — z_a encodes visual-physical context from joint pretraining, making the Value MLP an image-free quality discriminator. Cost: ~3–5 H100-hours.\\n\\n**Step 4 — Inference-Time Best-of-N Planning**: At each planning step, sample B=4–8 action-only trajectories from frozen UWM.\\n\\nPrimary results (two methods):\\n- LOC selection: a_{i*} = argmin_i S_LOC(z_{a,i}) at best density estimator from diagnostic [zero weight updates, WAM-specific, no image at inference]\\n- Value MLP selection: a_{i*} = argmax_i V(z_{a,i}) [lightweight training, WAM-specific, no image at inference]\\n\\nComparisons (required): V-GPS-style Cartesian Q-function applied to WAM action outputs (Tier 1 baseline); MG-Select-style KL scoring applied to WAM action-only inference (Tier 2 baseline); random selection (B=4–8, sanity check); single-trajectory WAM B=1 (frozen baseline).\\n\\nAblation (secondary): (a) PCS denoising error selection at best t* from diagnostic (expected to underperform LOC); (b) soft MPPI w_i ∝ exp(β·V(z_{a,i})) to document action-averaging artifact; (c) action-only z_a vs. full video+action latent for LOC and Value MLP scoring.\\n\\n**Ablation Grid**: B ∈ {1, 4, 8} (B=1 is frozen WAM single-trajectory baseline); selection method: LOC KNN vs. LOC GMM (primary zero-training) vs. Value MLP hard argmax (primary trained) vs. V-GPS-style Cartesian scoring (Tier 1 baseline) vs. MG-Select-style KL (Tier 2 baseline) vs. random selection (sanity check); T_noise fixed at 1.0 in primary ablation; execution regime: (a) open-loop vs. (b) periodic replanning every K=5 action chunks.\\n\\n**Primary hypotheses**: (H1, tested in Step 1 LOC diagnostic) LOC achieves Spearman ρ > 0.3 and AUC > 0.6, confirming WAM success latents form an OOD-detectable distribution even without video input at inference — tested empirically in Step 1; (H2) LOC outperforms PCS and MG-Select-style KL in the diagnostic; (H3) Value MLP achieves ≥10pp improvement over B=1 baseline on RoboCasa; (H4) LOC achieves ≥5pp improvement over B=1 with zero weight updates; (H5) Both methods outperform V-GPS-style Cartesian scoring and MG-Select-style KL applied to WAM outputs, confirming the Tier 3 latent quality-discrimination advantage.\\n\\n**Standalone Value MLP contribution (applicable if LOC fails H1)**: If LOC AUC < 0.55 in the diagnostic, the paper's narrative shifts to Value MLP as the primary contribution: (a) vs. V-GPS — V-GPS requires ResNet-34 image embedding + 7D Cartesian action at every inference call (Tier 1, image-dependent); Value MLP operates on WAM z_a alone (no image at inference), trained via binary classification rather than offline RL; (b) vs. WAV — WAV trains from scratch as architectural co-design; Value MLP is plug-in-compatible with any pretrained WAM; (c) vs. RoVer — RoVer requires a 0.2B PRM on process labels; Value MLP uses a 3-layer MLP on binary success/failure labels; (d) vs. Cosmos Policy — 1,536 H100-hours rollout fine-tuning vs. ≤40 H100-hours; (e) vs. KDPE — KDPE operates in Cartesian space with all training data; Value MLP uses WAM latent space with success/failure-labeled data. Central empirical claim: joint pretraining creates a latent space where success/failure are more linearly separable than in Cartesian action space, enabling a 3-layer image-free MLP to match or exceed the discriminative power that V-GPS achieves via a ResNet-34-augmented Q-function with offline RL.\\n\\n**Proactive framing against fine-tuned baselines**: Expected absolute RoboCasa performance (~20–35% after ≥10pp improvement from 10–25% frozen baseline) will appear weak against Cosmos Policy (67.1%) and World2Act (~66%). The paper must explicitly frame this in the introduction and evaluation sections: 'Our methods are orthogonal to fine-tuning — they extract planning value from existing pretrained WAMs in settings where domain-specific demonstration data is unavailable. The comparison target is B=1 frozen WAM inference at the same data budget (zero domain-specific demos for LOC; ≤40 H100-hours of simulation rollouts for Value MLP), not fine-tuned models that consumed 1,000 real robot demonstrations or 1,536 H100-hours of rollout fine-tuning. In zero-demonstration deployment scenarios — a common real-world constraint — our methods improve over the no-adaptation baseline by ≥10pp without any weight updates or real robot data collection. The gap versus fine-tuned methods quantifies the cost of the zero-demonstration constraint, not a failure of candidate selection.'\\n\\n**Evaluation Benchmarks**: (a) Primary — RoboCasa: Cosmos Policy fine-tuned 67.1%; World2Act (Cosmos+World2Act) ~66%; frozen UWM expected 10–25% (validated in Step 0a); absolute target ≥10pp over frozen baseline. (b) Secondary — LIBERO-Long: near saturation for strong frozen WAMs (Fast-WAM 95.2%, Table 2); included to characterize gain profile vs. task difficulty. (c) Baselines: B=1 frozen WAM, random selection, V-GPS-style Cartesian scoring, MG-Select-style KL applied to WAM.\\n\\nDreamZero cross-WAM validation deferred to camera-ready. CoRL submission rests on UWM alone.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~140h H100\",\n      \"gpu_utilization\": \"HIGH idle (~35–55%): GPU waits while researcher implements LOC density estimator (KNN/GMM fitting), interprets LOC diagnostic results, debugs failure collection pipeline, and designs ablations.\",\n      \"timeline\": \"2–3 months\",\n      \"team\": \"1–2 researchers\",\n      \"estimated_gpu_cost\": \"~$350 (140h × $2.50/h blended Lambda/RunPod/Vast.ai H100 rate)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~165h H100\",\n      \"gpu_utilization\": \"MODERATE idle (~20–30%): agent handles code scaffolding, baseline validation, LOC diagnostic, failure collection, demo encoding, density estimator fitting, and experiment submission; human reviews Step 0a baseline and LOC diagnostic results at daily check-ins to make go/no-go decisions\",\n      \"timeline\": \"3–4 weeks\",\n      \"team\": \"1 researcher, ~30 min/day check-in\",\n      \"claude_api_cost\": \"$150–250 (~1,500–2,500 turns at mixed Sonnet/Opus rates)\",\n      \"estimated_gpu_cost\": \"~$413 (165h × $2.50/h)\",\n      \"risk_note\": \"Step 0a (frozen UWM RoboCasa baseline) and LOC diagnostic are hard sequential dependencies before main ablation. Sequential order: 0a baseline validation (2–3 H100-hours, Day 1–2) → LOC diagnostic (3–5 H100-hours, Day 2–4) → failure collection (15–20 H100-hours, Day 3–7, parallel with LOC) → demo encoding + density fitting (10–15 H100-hours, Day 5–9) → Value MLP training (3–5 H100-hours, Day 9–10) → main ablations (Day 10–18). RoboCasa simulation setup requires separate engineering effort from LIBERO. DreamZero cross-WAM deferred to camera-ready.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~185h H100 (revised from prior 320h estimate; ablation grid pruned to stay within ≤200h hard constraint)\",\n      \"gpu_budget_breakdown\": \"Step 0a frozen UWM baseline: ~3h; Steps 0b+0c in parallel (demo encoding + failure collection): ~32h billed (12h encoding + 20h failure collection running concurrently); Step 1 LOC diagnostic: ~4h; Step 3 Value MLP training: ~5h; Main ablation grid (B ∈ {1,4,8} × 6 methods × 3 seeds × 2 benchmarks = 108 runs × ~1.2h avg): ~130h; contingency/reruns: ~11h. Total: ~185h billed GPU-hours. With 4 GPUs running ablation batch concurrently: wall-clock ≈ 44h setup + 33h ablations = 77h wall-clock; billed ≤ 200h hard constraint.\",\n      \"gpu_utilization\": \"MINIMAL idle (~5–10%): agent pipelines baseline validation, LOC diagnostic, failure collection, demo encoding, density fitting, MLP training, and evaluation continuously.\",\n      \"timeline\": \"7–10 days with 4 H100 GPUs simultaneously\",\n      \"team\": \"0 (only initial repo setup and credential configuration)\",\n      \"claude_api_cost\": \"$200–350 (~2,500–4,000 turns at Opus rates)\",\n      \"estimated_gpu_cost\": \"~$463 (185h × $2.50/h)\",\n      \"ablation_grid_vs_prior\": \"Ablation grid expanded from 5 to 6 selection methods by adding V-GPS-style Cartesian scoring as a Tier 1 baseline, providing direct Tier 1 vs. Tier 3 comparison. T_noise sweep ({1.0,1.5,2.0}) dropped from auto research grid — T_noise fixed at 1.0 unless diversity pilot (Step 2) shows mean cosine distance < 0.05. B grid: {1,4,8} (B=1 is frozen WAM single-trajectory baseline). PCS full ablation retained only in Step 1 LOC diagnostic.\",\n      \"speed_bottleneck\": \"Step 0a baseline validation → LOC diagnostic → (parallel: failure collection + demo encoding) → density fitting (trivial) + Value MLP training is a 5-step sequential dependency spanning ~8 days minimum. RoboCasa evaluation rollouts: each ablation variant requires sequential per-task evaluation; with 4 GPUs running 4 variants concurrently, the full grid needs ~5–7 days.\",\n      \"risk_note\": \"LOC density estimation (KNN/GMM) is a standard sklearn/torch operation requiring no custom implementation. Main implementation risk: UWM action latent extraction in action-only mode (video timestep = T, action timestep = 0) — this mode is supported by UWM's architecture but may require engineering to extract z_a as a fixed-size vector for density estimation. If z_a is not directly accessible, the Action Decoder intermediate activations serve as a substitute latent representation. V-GPS-style Cartesian baseline requires implementing the Cartesian action extraction and Q-function scoring as an additional comparison method.\"\n    }\n  },\n  \"target_venues\": [\n    \"CoRL 2026 (Abstract deadline: May 26, 2026; Full paper: May 29, 2026; Conference: Nov 9–12, Austin TX) — TIGHT but viable: 19 days from 2026-05-10. Step 0a RoboCasa baseline must run immediately (Day 1–2). Minimum viable submission: frozen UWM RoboCasa baseline validation + LOC diagnostic figure (including PCS and Tier 1/Tier 2 comparison showing expected negative results) + LOC and/or Value MLP Best-of-N results (primary) + LIBERO-Long (secondary) + B/hard-argmax ablation + V-GPS-style Cartesian and MG-Select-style KL baseline comparisons. DreamZero cross-WAM deferred to camera-ready.\",\n    \"ICLR 2027 (deadline ~September–October 2026) — More feasible timeline for complete ablation grid, latent geometry analysis (success/failure separation across Tier 1/2/3 representations), DreamZero cross-WAM evaluation, and potential real-world experiments.\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"V-GPS: Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance (arXiv 2410.13816, CoRL 2024) — CRITICAL PRIOR WORK for Value MLP: trains Q-function via offline RL (Cal-QL) on sparse binary rewards; architecture: ResNet-34 image encoder + 7D Cartesian action → scalar Q-value; applies to frozen Octo-small/Octo-base/Octo-small-1.5/RT-1X/OpenVLA; samples K=50 candidates; achieves +82.8% relative improvement (Octo-small-1.5 baseline 24% → V-GPS 44%) on real-robot 6-task benchmark; validates value re-ranking paradigm for frozen policies in Tier 1 (Cartesian+image) space. Differentiates from Value MLP: (a) V-GPS requires ResNet-34 image embedding + raw 7D action at every inference call; Value MLP uses WAM z_a alone (no image needed at inference); (b) offline RL training vs. binary classification; (c) Cartesian+image vs. WAM latent space\",\n    \"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning (arXiv 2601.16163, ICLR 2026) — CRITICAL PRIOR WORK: implements Best-of-N planning mode (15 forward passes per action via majority-mean aggregation of world model + value function queries); requires rollout fine-tuning because demo-only training 'cannot correctly predict failure states'; 1,536 H100-hours for RoboCasa; 98.5% LIBERO, 67.1% RoboCasa; our LOC requires zero rollout data and zero weight updates\",\n    \"KDPE: A Kernel Density Estimation Strategy for Diffusion Policy Trajectory Selection (arXiv 2508.10511, CoRL 2025) — CRITICAL PRIOR WORK: applies manifold-aware KDE to Cartesian action trajectories (end-effector position/SO(3)-orientation/gripper) from Diffusion Policy; generates N=100 candidates; achieves 88.2% vs. 85% on RoboMimic/MimicGen; CRITICAL FINDING: KDPE-OOD (selecting most out-of-distribution trajectory) performs WORSE than KDPE — validates in-distribution selection direction for LOC; Tier 1 (Cartesian space) method\",\n    \"World2Act (arXiv 2603.10422, March 2026) — post-training framework achieving ~66% on RoboCasa using 50 real + 50 imagined demos; reports UWM achieves 60.8% on RoboCasa with 1,000-demo fine-tuning (confirming frozen UWM baseline is ~10–25%); differentiation: World2Act requires contrastive post-training to align VLA latents; LOC exploits WAM alignment inherited from joint pretraining\",\n    \"Fast-WAM: World Action Models without Test-Time Video (arXiv 2603.16666) — CRITICAL FRAMING: 97.6% LIBERO-avg (Table 2) and 91.8% RoboTwin (Table 1) at 190ms without video; single trajectory only; our method uses same action-only inference for candidate generation and adds LOC selection at B × 5ms overhead\",\n    \"FAIL-Detect: Failure Detection as OOD Detection for Robot Manipulation (arXiv 2503.08558, RSS 2025) — SUPPORTING WORK: proves OOD detection on success-only demonstration data reliably detects policy failures; motivates LOC's use of KNN/GMM density on success demo latents; FAIL-Detect is execution-time monitoring, LOC is pre-execution candidate selection — Step 1 LOC diagnostic is the first empirical test of whether this principle transfers to pre-execution WAM z_a in action-only inference mode\",\n    \"EVA: Aligning Video World Models with Executability (arXiv 2603.17808, 2026) — identifies 'executability gap' showing visually coherent world model rollouts can violate kinematic constraints; supports LOC over PCS: visual denoising error does not predict task success\",\n    \"RoVer: Robot Reward Model as Test-Time Verifier for Vision-Language-Action Models (arXiv 2510.10975, ICLR 2026) — CRITICAL PRIOR WORK: generates B VLA candidates, trains 0.2B PRM; Tier 2 (VLA action token) method; differentiation: requires 0.2B model training vs. LOC's zero training and Value MLP's 3-layer MLP; VLA action tokens lack video-physics regularization\",\n    \"Verifier-free Test-Time Sampling / MG-Select (arXiv 2510.05681, ICLR 2026) — CRITICAL PRIOR WORK: training-free KL-from-masked-distribution scoring for frozen VLAs; 168% relative improvement on RoboCasa pick-and-place; Tier 2 (VLA action token distributional uncertainty) method; differentiation: MG-Select measures action-space distributional uncertainty, LOC measures latent OOD membership relative to success demo distribution\",\n    \"World-Value-Action (WAV) Model (arXiv 2604.14732, April 2026) — trajectory value module requiring architectural co-design and training from scratch; verified metrics: 99.6% LIBERO overall average across 4 splits (Spatial/Object/Goal/Long, Table 1); LIBERO-Long specifically 98.1% (Table 1); 75.6% real-world (Figure 2, dual-arm Piper robot, 15 trials per task); our method leaves all WAM weights frozen and is plug-in-compatible with pretrained WAMs\",\n    \"ALT Policy (arXiv 2505.05787, May 2025) — 'Demystifying Diffusion Policies: Action Memorization and Simple Lookup Table Alternatives': uses contrastive image encoder distance in observation latent space as runtime OOD signal for single nearest-neighbor action retrieval; related to LOC in applying latent-space proximity as a quality signal, but in observation (not action) latent space and via retrieval rather than multi-candidate selection\",\n    \"UNISafe (arXiv 2505.00779, May 2025) — 'Uncertainty-aware Latent Safety Filters for Avoiding Out-of-Distribution Failures': calibrates world model epistemic uncertainty via conformal prediction for OOD-based safety filtering in state latent space; related to LOC in applying conformal prediction to world-model latents, but targets state-space safety rather than pre-execution action-latent candidate selection\",\n    \"VLS: Steering Pretrained Robot Policies via Vision-Language Models (arXiv 2602.03973, February 2026) — training-free VLM-reward-gradient guidance of frozen diffusion/flow-matching policies' denoising process; different mechanism from both LOC (latent OOD density) and Value MLP (binary classification); concurrent work\",\n    \"Compose Your Policies! / GPC (arXiv 2510.01068) — training-free convex composition of multiple frozen policy distributions; operates at distribution level, not discrete candidate selection from single WAM\",\n    \"Inference-Time Enhancement / GPC-RANK (arXiv 2502.00622, IEEE RAL 2025) — frozen policy + separately trained action-conditioned world model + hard argmax; uses world-model reward prediction for scoring, not WAM action latent OOD\",\n    \"Unified World Models / UWM (arXiv 2504.02792, RSS 2025) — primary backbone; independent per-modality timesteps support action-only inference; publicly available weights and code\",\n    \"Diffusion Policy (arXiv 2303.04137, RSS 2023 / IJRR 2024) — documents multi-modal action distribution handling; confirms averaging over manipulation action modes produces infeasible blended actions; justifies hard argmax over soft MPPI weighting\",\n    \"When to Trust Imagination (arXiv 2605.06222, May 2026) — CONCURRENT WORK: FFDC adaptively decides action chunk sizes; orthogonal to our pre-execution selection; combinable\",\n    \"World Action Models as Zero-shot Policies / DreamZero (arXiv 2602.15922) — 14B joint video+action DiT; secondary backbone for cross-WAM validation in camera-ready/ICLR version\",\n    \"OA-WAM (arXiv 2605.06481, May 2026) — concurrent work; different problem (object binding)\",\n    \"CKT-WAM (arXiv 2605.06247, May 2026) — concurrent work; different problem (cross-WAM knowledge transfer)\",\n    \"GigaBrain-0.5M* (arXiv 2602.12099) — RAMP RL loop requires 30%+ more training\",\n    \"H-WM (arXiv 2602.11291) — requires hierarchical architectural co-design\",\n    \"Latent Diffusion Planning (arXiv 2504.16925) — trains diffusion planner from scratch\"\n  ],\n  \"description\": \"Latent-Distribution Candidate Selection (LDCS) converts any pretrained video-diffusion World Action Model into a multi-candidate planner at inference time without modifying any WAM weight, exploiting WAM-specific latent structure through two complementary methods — positioned within a three-tier action representation hierarchy for candidate selection.\\n\\n**The three-tier framing**: Existing candidate selection methods operate in three representational tiers: (1) Cartesian action space — KDPE (kernel density, N=100 candidates) and V-GPS (Q-function re-ranking via offline RL on 7D actions + ResNet-34 image embeddings, +82.8% real-robot improvement, CoRL 2024), both requiring raw action representations and, for V-GPS, image input at every inference call; (2) VLA action tokens — MG-Select (KL-divergence confidence) and RoVer (0.2B PRM) without video-physics co-regularization; (3) WAM action latents z_a — continuous latents from joint video-action diffusion pretraining (this paper). The central hypothesis: WAM latent space offers richer quality-discriminative geometry than Tier 1 (Cartesian+image) or Tier 2 (VLA tokens), enabling simpler discriminators without image input at inference.\\n\\n**Inference-time caveat on z_a geometry**: In action-only inference (video timestep = T), video tokens are at full noise — no inference-time video conditioning occurs. The quality-discriminative structure of z_a is a training-time property of joint pretraining. Step 1 (LOC diagnostic) is the first empirical test of whether this geometry persists as a success/failure discriminator without video input. If H1 fails (AUC < 0.55), LOC reports a negative result and Value MLP becomes the sole primary contribution.\\n\\n**Method 1 — Latent OOD Consistency Scoring (LOC, zero weight updates)**: Fit a KNN or GMM density estimator on WAM action latents {z_a^success} from LIBERO-90 success demos. At inference, sample B=4–8 action-only candidates and score each by nonconformity: S_LOC(z_{a,i}) = −log p̂(z_{a,i}). Select argmin (most in-distribution candidate). Overhead: B × ~5ms = 20–40ms for B=4–8. No image needed at inference.\\n\\n**Method 2 — Action-Latent Value MLP (≤40 H100-hours)**: 3-layer MLP trained on {z_a^success} and explicitly collected failure latents. Hard argmax selection. No image needed at inference — z_a encodes visual-physical context from joint pretraining. Differentiated from V-GPS: operates on WAM z_a alone (no ResNet-34 image embedding), uses binary classification (not offline RL), and is trained in <5 H100-hours. Central hypothesis: joint pretraining creates a latent space where success/failure are more linearly separable than in Cartesian action space, enabling a 3-layer image-free MLP to match or exceed discriminative power that V-GPS achieves via Cartesian+image Q-function.\\n\\n**LOC Diagnostic (mandatory, Step 1)**: B=16 rollouts on 3 RoboCasa tasks, measuring AUC of S_LOC as binary success predictor (target H1: AUC > 0.6), compared against: (a) video denoising error S_PCS, (b) MG-Select-style KL (Tier 2), (c) V-GPS-style Cartesian density (Tier 1). Tests the full three-tier hierarchy in a controlled diagnostic before committing to the main ablation.\\n\\nPrimary evaluation: RoboCasa (target ≥10pp absolute over frozen baseline; Cosmos Policy 67.1% / World2Act ~66% as fine-tuned upper references — explicitly framed as orthogonal to our zero-demonstration deployment target). Secondary: LIBERO-Long. Auto research ablation grid: B ∈ {1,4,8} × 6 methods × 3 seeds × 2 benchmarks (~185 billed H100-hours ≤ 200h hard constraint). CoRL submission: UWM only; DreamZero cross-WAM deferred to camera-ready.\",\n  \"project_name\": \"frozen_wam_mppi\",\n  \"source\": \"web_research\"\n}\n\n## Reviewer feedback (round 7)\nIssues: [\"PERSISTENT FACTUAL ERROR — WAV metrics STILL incorrect in Round 7 despite explicit Round 6 instruction: The submission claims '99.6% LIBERO overall average across 4 splits (Table 1)' for WAV (arXiv 2604.14732). Independent verification confirms WAV reports Spatial 100.0%, Object 98.6%, Goal 94.4%, Long 98.1% — averaging ~97.8%, not 99.6%. This error was explicitly flagged in Round 6 with the instruction 'Fetch the WAV paper PDF directly and correct the stated metrics with table references.' The generator responded by adding 'verified metrics (Table 1, Figure 2)' — but the numbers remain wrong. Citing incorrect metrics for a concurrent paper is a credibility-damaging error that CoRL reviewers will catch.\", \"SIGNIFICANT — Two published concurrent papers are uncited and must be differentiated: (1) Latent Policy Barrier (arXiv 2508.05941): uses Euclidean distance in visual observation latent space to nearest expert demo state as OOD signal, steering the policy if the state is OOD. Differentiates from LOC: LPB operates on observation latents (not WAM action latents z_a), does runtime execution-time steering (not pre-execution candidate selection), and uses a separate dynamics model rather than the frozen WAM's joint pretraining. (2) Latent Policy Steering (arXiv 2507.13340): trains a value function in world model latent space using both expert states and policy-rollout states, achieving +50% relative improvement with 30 demos on real-world tasks. Differentiates from Value MLP: LPS uses optic flow as embodiment-agnostic action representation (not WAM action latents z_a), requires policy-rollout data for training (not just binary success/failure from demos+frozen-policy failures), and does not exploit WAM joint-pretraining latent geometry. Both papers must be added to related work with explicit differentiation — they establish that latent-space OOD and value functions for robot policy improvement is an active published direction, and reviewers in this space will know them.\", \"MODERATE — Being-H0.7 (arXiv 2605.00078, May 2026) achieves 99.2% on LIBERO and represents a strong concurrent WAM. While not a candidate selection paper (it uses latent prior-posterior alignment rather than Best-of-N scoring), it should be briefly mentioned in the landscape section as a concurrent WAM result to contextualize LIBERO score comparisons.\", \"MINOR — The claim that KDPE-OOD performs substantially worse (ToolHang: 7% vs 76%) is now independently confirmed and is a strong supporting finding for LOC's in-distribution selection direction. The submission should explicitly cite these KDPE ablation numbers (not just 'KDPE-OOD performs worse') since the magnitude of the effect (7% vs 76%) is a compelling empirical motivator.\"]\nFeedback: Round 7 has correctly addressed all Round 6 issues: V-GPS cited with three-tier hierarchy differentiation, LOC hypothesis correctly framed as H1 with diagnostic gate, action-only mode caveat stated, ALT Policy and UNISafe cited, RoboCasa framing proactively addressed, budget correctly computed. Three targeted fixes are needed:\n\n**1. Fix WAV metrics immediately (0.5 day) — do not submit with wrong numbers.** The correct WAV LIBERO numbers are approximately Spatial 100.0%, Object 98.6%, Goal 94.4%, Long 98.1% (average ~97.8%, NOT 99.6%). Correct the landscape and key_references entries to match the actual table values. This is the third consecutive round this error has appeared; a CoRL reviewer who has read WAV will notice immediately.\n\n**2. Add Latent Policy Barrier (arXiv 2508.05941) and Latent Policy Steering (arXiv 2507.13340) to related work (1 day).** Write: 'Latent Policy Barrier (LPB, 2025) uses Euclidean distance in visual observation latent space to nearest expert demo state for OOD detection during execution; our LOC operates in WAM action latent space z_a (not observation latents) and scores B pre-execution candidates rather than performing runtime steering, exploiting WAM joint-pretraining geometry unavailable to observation-space methods. Latent Policy Steering (LPS, 2025) trains a value function in world model latent space using expert plus policy-rollout states; our Value MLP uses WAM-specific z_a from joint video-action pretraining and requires only binary success/failure labels from collected failures (no rollout policy-visit data), testing whether joint pretraining creates a more linearly separable latent geometry.' These differentiations are legitimate and clear — turning the citations into positioning assets rather than gaps.\n\n**3. Strengthen the KDPE-OOD citation with magnitude (0.5 day).** The ToolHang ablation (KDPE-OOD 7% vs KDPE 76%) is a striking finding that empirically motivates in-distribution selection. Cite this specific number in the LOC motivation: 'KDPE finds that out-of-distribution selection collapses performance on ToolHang (7% vs. 76%), providing strong empirical grounding for LOC's argmin selection direction.'\n\nWith these three fixes (~2 days), the submission is CoRL-ready. The three-tier hierarchy and mandatory LOC diagnostic with fallback are strong scientific contributions. Minimum viable submission scope (UWM + RoboCasa + LIBERO-Long + LOC diagnostic figure + B/hard-argmax ablation) remains the right call.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.\n- Address each issue specifically.\n\n## 深度调研要求（每一轮修订都必须执行）\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。\n   - 搜索最新的相关论文（arXiv, conference proceedings）\n   - 搜索 benchmark/leaderboard 确认当前 SOTA\n   - 搜索可能遗漏的相关工作和 concurrent work\n\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，\n   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。\n\n3. **深度思考**：在修订之前，先独立思考以下问题：\n   - 这个 idea 的核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach 来解决同一个核心问题？\n   - 修订后的 idea 相比上一版有什么本质性的改进？\n\n4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，\n   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。\n\n## 针对 Review 意见的定向搜索\n\n对 reviewer 指出的每个问题，执行以下搜索流程：\n\n1. **如果 reviewer 说'已有类似工作'**：\n   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读\n   - 搜索该论文的 cited-by，找到后续跟进工作\n   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot\n\n2. **如果 reviewer 说'SOTA 过时'**：\n   - 用 Papers With Code 查看当前排行榜\n   - 搜索过去 6 个月的最新方法\n   - 更新你的 landscape 和 baseline\n\n3. **如果 reviewer 说'可行性有问题'**：\n   - 搜索类似规模实验的实际成本和时间线\n   - 搜索 GitHub 上是否有可复用的实现\n   - 搜索相关数据集/模型的可获取性\n\n4. **如果 reviewer 说'novelty 不足'**：\n   - 对核心方法尽量做 3-5 种不同关键词组合的搜索\n   - 搜索相邻领域是否有类似思路\n   - 如果确实 novelty 不足，考虑 major revision 或 pivot\n\n- Use WebSearch to find updated information if the reviewer flagged outdated claims.\n- You have full freedom in how much to change:\n  - Minor fix: if only specific details are wrong, correct them and keep everything else.\n  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.\n  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.\n- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.\n- In the output JSON, include a \"change_type\" field with one of: \"minor\", \"major\", or \"pivot\" to indicate the scope of your changes.\n- Output the revised idea as a COMPLETE JSON object (same schema as original, plus \"change_type\").\n\n## 停滞提醒\n这个 idea 已经经过 7 轮修订，近 3 轮的平均分从 3.2 到 3.5，没有明显改善。\n\n请认真思考：\n- 当前方向是否存在根本性的瓶颈？反复的 minor fix 是否在回避核心问题？\n- 如果你认为问题出在 approach 而非 framing，可以做 major revision。\n- 如果你认为 core problem 本身就有问题（gap 不存在、问题不够重要），pivot 到同一研究领域下的新方向可能是更好的选择。\n- 当然，如果你有信心这一轮修订能实现突破，继续改进也完全可以。\n\n最终由你判断——做你认为最能提升 idea 质量的选择。"
}
```

---

### Runtime record

_source line 2 · 2026-05-10T09:30:25.812Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T09:30:25.812Z",
  "sessionId": "f0b9fbaa-4159-4906-9e7b-5c7c38fdb4da"
}
```

---

## Round 1

44 recorded events

### User

_source line 3 · 2026-05-10T09:30:25.854Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-10 (UTC).**

## Original idea
{
  "title": "Latent-Distribution Candidate Selection for Frozen World Action Models: OOD Consistency Scoring and Action-Latent Value Learning",
  "core_problem": "Pretrained WAMs generate a single action trajectory at inference and provide no mechanism to compare candidate futures. Adding planning capability currently requires one of three costly interventions: (1) full fine-tuning of the video model on robot demos (Cosmos Policy, ICLR 2026: 384–3,072 H100-hours); (2) training a separate action-conditioned world model alongside the frozen policy (GPC, RAL 2025); or (3) architectural co-design or RL loops (H-WM, GigaBrain RAMP, WAV). Fast-WAM (arXiv 2603.16666) demonstrates that action-only inference achieves 97.6% on LIBERO (Table 2) and 91.8% on RoboTwin (Table 1) at 190ms, motivating candidate generation from frozen WAM action-only inference rather than expensive video rollouts.\n\nThe test-time candidate selection literature (2024–2026) has established three tiers of action representation for scoring candidates, with each tier providing increasingly structured quality-discriminative geometry:\n\n**Tier 1 — Cartesian action space**: V-GPS (arXiv 2410.13816, CoRL 2024) trains a Q-function via offline RL (Cal-QL) on raw 7-dimensional Cartesian action vectors concatenated with ResNet-34 image embeddings, scoring K=50 candidates from frozen generalist policies (Octo, RT-1X, OpenVLA) and achieving +82.8% relative improvement on real-robot tasks — establishing that value-function re-ranking of frozen policies works in Cartesian+image space. KDPE (arXiv 2508.10511, CoRL 2025) applies kernel density estimation to Cartesian action trajectories (end-effector position, SO(3)-orientation, gripper state) from Diffusion Policy to filter multimodal outputs, generating N=100 candidates; achieves 88.2% vs. 85% on RoboMimic/MimicGen. Critical KDPE finding: KDPE-OOD (selecting the most out-of-distribution trajectory) performs worse than KDPE (selecting the most typical) — confirming that in-distribution selection is the correct direction. Both Tier 1 methods operate on low-dimensional raw action representations with no latent structure encoding physical plausibility beyond what is captured by pixel-level image embeddings.\n\n**Tier 2 — VLA action tokens**: MG-Select (arXiv 2510.05681, ICLR 2026) uses KL-divergence from a masked unconditional VLA distribution as a training-free confidence signal, achieving 168% relative improvement on RoboCasa pick-and-place. RoVer (arXiv 2510.10975, ICLR 2026) trains a 0.2B Process Reward Model that scores candidates from frozen VLAs. Both operate on VLA action tokens from architectures trained on language-action pairs without joint video-action pretraining, lacking the video-physics co-regularization that structures WAM action latents.\n\n**Tier 3 — WAM action latents** (this paper's domain): UWM and DreamZero generate action latents z_a from joint video-action diffusion pretraining. Cosmos Policy (ICLR 2026) implements Best-of-N in its planning mode by generating B candidates and scoring each via a fine-tuned value function — but requires rollout fine-tuning (1,536 H100-hours for RoboCasa) because demonstration-only training 'cannot correctly predict failure states.'\n\nThe central unanswered question — which Tier 1 and Tier 2 approaches cannot answer — is: (1) Do WAM action latents z_a, regularized by joint video-action pretraining, form a latent success distribution that is more structured and separable from failure regimes than VLA action tokens (Tier 2) or Cartesian action representations (Tier 1), enabling lightweight OOD-based candidate scoring without any rollout data? (2) Does operating in WAM latent space alone (without needing an image at inference) enable a more compact, efficient quality discriminator than Tier 1 methods that require both image and action? These questions are grounded in the FAIL-Detect (arXiv 2503.08558, RSS 2025) finding that OOD detection on success-only demonstrations reliably identifies failures — but have not been applied to WAM action latents or to pre-execution candidate selection.\n\nImportant caveat on z_a geometry: In action-only inference (video timestep = T), video tokens are at full noise and provide no inference-time conditioning. The quality-discriminative structure of z_a is therefore a training-time property — joint pretraining causes the model to learn representations where z_a co-varies with visual futures, but whether this geometry persists as a success/failure discriminator when video is absent at inference is not proven a priori. Step 1 (LOC diagnostic) is the first empirical test. If H1 fails (AUC < 0.55), LOC reports a negative result and Value MLP becomes the sole primary contribution.\n\nThe companion question of whether video denoising error (as opposed to latent OOD scoring) is a reliable zero-training signal is answered negatively by Cosmos Policy's own finding and by EVA (arXiv 2603.17808), which demonstrates an 'executability gap' showing that visual coherence does not predict task success.\n\nNo existing work demonstrates Best-of-N candidate selection using WAM action latents' distributional structure — either zero-training (OOD scoring) or lightweight-trained (value MLP) — without modifying any WAM weights or requiring rollout data for the zero-training path. The three-tier hierarchy predicts that z_a offers the richest quality-discriminative geometry for frozen-policy candidate selection, a hypothesis this paper tests empirically.",
  "opportunity": "UWM's independent per-modality diffusion timestep architecture (RSS 2025) natively supports action-only inference (video timestep = T, action timestep = 0), producing action latents z_a jointly pretrained with video. This creates two complementary WAM-specific approaches to candidate selection:\n\n**Method 1 — Latent OOD Consistency Scoring (LOC, zero weight updates)**: Encode LIBERO-90 success demonstrations through frozen UWM in action-only mode to obtain a reference distribution {z_a^success}. Fit a lightweight density estimator — KNN-based nonconformity score (k=10) or Gaussian Mixture Model (k≤5 components) — on {z_a^success}. At inference, sample B=4–8 action-only candidates from frozen UWM, obtain latents {z_{a,1}, ..., z_{a,B}}, and score each: S_LOC(z_{a,i}) = −log p̂(z_{a,i}) (nonconformity score). Select a_{i*} = argmin_i S_LOC(z_{a,i}) (most in-distribution candidate). Total inference overhead: B × ~5ms = 20–40ms for B=4–8. Cost: ~30–60 minutes to fit density estimator on encoded latents; no WAM weight updates.\n\nTheoretical basis: (1) FAIL-Detect (RSS 2025) proves that OOD detection on success-only demonstration data reliably detects policy failures — the success-demo distribution implicitly excludes failure modes; (2) KDPE (CoRL 2025) demonstrates in Cartesian action space that selecting the most IN-distribution trajectory improves performance, while KDPE-OOD performs worse — validating the in-distribution selection direction for LOC; (3) z_a from joint video-action pretraining is hypothesized to encode physical plausibility in a tighter quality-discriminative geometry than both Cartesian action space (KDPE, V-GPS) and VLA action tokens. **Inference-time caveat**: In action-only mode, video tokens are at full noise (timestep T) — this quality-discriminative geometry is a training-time property of the learned weights, not an inference-time video conditioning effect. Step 1 empirically tests whether this training-time property persists as a quality signal without video input. LOC is reported as a negative result if AUC < 0.55.\n\nKey differentiation from KDPE and V-GPS (Tier 1 methods): (a) density estimation in WAM action latent space z_a, not Cartesian action space (position/orientation/gripper) or 7D delta actions; (b) success-demonstrations-only reference distribution establishing a quality anchor, not all training data (KDPE) or a separately collected offline RL dataset (V-GPS); (c) no image required at inference — z_a encodes visual-physical context from joint pretraining, unlike V-GPS which concatenates a ResNet-34 image embedding with the raw action for every candidate; (d) B=4–8 candidates vs. KDPE's N=100 and V-GPS's K=50. LOC implements success-mode latent selection; KDPE implements Cartesian-space all-data-mode selection; V-GPS implements offline-RL Q-function scoring in Cartesian+image space — these are mechanistically distinct quality signals across the three representational tiers.\n\nDifferentiation from MG-Select: LOC scores membership in the success demonstration distribution (latent OOD density); MG-Select measures KL divergence of task-conditioned output from masked unconditional distribution (action-space distributional uncertainty).\n\nNote on Cosmos Policy planning mode: Cosmos Policy also implements Best-of-N — generates B actions, predicts future states and values, executes the highest-value action. However, (a) requires fine-tuning a value function on rollout data (1,536 H100-hours for RoboCasa) because demonstration-only training 'cannot correctly predict failure states'; (b) 15 total forward passes per candidate. LOC requires zero rollout data, zero weight updates, and ~5ms per candidate.\n\n**Method 2 — Action-Latent Value MLP (≤40 H100-hours training)**: A 3-layer MLP trained on WAM action latents z_a from LIBERO-90 success demonstrations AND explicitly collected failure trajectories scores each candidate via V(z_{a,i}) ∈ [0,1]. Hard argmax Best-of-N is the primary result. Key hypothesis: z_a regularized by joint video-action pretraining is more linearly separable between success and failure regimes than raw action outputs, VLA action tokens, or Cartesian representations — enabling a simpler, image-free quality discriminator.\n\nDifferentiation from V-GPS (CoRL 2024): V-GPS trains a Q-function via offline RL (Cal-QL) on (image observation, raw 7D Cartesian action) pairs — requiring both a ResNet-34 image encoder and the raw action candidate at inference; our Value MLP trains on WAM action latents z_a alone via binary success/failure supervision — no image required at inference because z_a already encodes visual-physical context from joint pretraining. V-GPS validates the value re-ranking paradigm in Cartesian+image space for VLA-family policies; our Value MLP asks whether WAM latent space provides a more compact, image-free quality signal with stronger success/failure linear separability. Additionally, V-GPS uses sparse binary rewards + Cal-QL offline RL; our Value MLP uses direct binary classification supervision, making it trainable in <5 H100-hours vs. V-GPS's offline RL pipeline. Other differentiations: (a) vs. WAV — WAV trains a trajectory value module as a new architectural component from scratch; Value MLP is plug-in-compatible with any pretrained WAM; (b) vs. RoVer — RoVer requires a 0.2B PRM trained on process labels; Value MLP uses a 3-layer MLP trained on binary success/failure labels; (c) vs. Cosmos Policy — requires 1,536 H100-hours rollout fine-tuning; Value MLP requires ≤40 H100-hours.\n\n**Comparison of LOC vs. Value MLP is itself a central contribution**: Their empirical comparison characterizes when WAM latent OOD scoring is sufficient versus when labeled training adds necessary discriminative power — and whether this latent-space approach outperforms Tier 1 (Cartesian + image, V-GPS) and Tier 2 (VLA token distributional uncertainty, MG-Select) methods.\n\n**Mandatory RoboCasa baseline validation before committing to targets**: World2Act (arXiv 2603.10422, March 2026) reports UWM achieving 60.8% on RoboCasa using 1,000 real demonstration fine-tuning. Since UWM was trained only on DROID data and has not been fine-tuned on RoboCasa tasks, the frozen UWM baseline (no RoboCasa demos) is expected to be substantially lower — likely 10–25%. Primary performance target: ≥10pp absolute improvement over the measured frozen baseline.",
  "landscape": "Cosmos Policy (arXiv 2601.16163, ICLR 2026) is the primary comparison point for absolute performance. Fully fine-tunes Cosmos-Predict2-2B on robot demos (384 H100-hours ALOHA, 1,536 RoboCasa, 3,072 LIBERO). Achieves 98.5% LIBERO and 67.1% RoboCasa. Its planning mode implements Best-of-N candidate selection: generates B candidate actions, predicts future states (3 queries to world model) and values (5 queries to value function per future state, 15 total predictions per action), and executes via majority-mean aggregation. Key distinction: Cosmos Policy's authors explicitly state that demo-only training 'cannot correctly predict failure states' — rollout fine-tuning is required for the planning value function. LOC requires zero rollout data and zero weight updates; Value MLP requires ≤40 H100-hours vs. 1,536 H100-hours.\n\nV-GPS (arXiv 2410.13816, CoRL 2024) — CRITICAL PRIOR WORK for Value MLP. 'Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance.' Trains a Q-function via offline RL (Cal-QL) on sparse binary rewards from demonstration data; architecture: ResNet-34 image encoder with FiLM language conditioning, 7-dimensional Cartesian action vector concatenated with image embedding passed through 2-layer MLP to predict scalar Q-value. At inference, samples K=50 action candidates from frozen generalist policies (Octo-small, Octo-base, Octo-small-1.5, RT-1X, OpenVLA) and re-ranks by Q-value. Achieves +82.8% relative improvement on real-robot 6-task benchmark (Octo-small-1.5 baseline: 24%, V-GPS: 44%). Key differentiations from our Value MLP: (a) V-GPS operates in Cartesian+image space — requires both ResNet-34 image embedding AND raw 7D action candidate at every inference call; our Value MLP operates on WAM z_a alone — no image needed at inference because z_a encodes visual-physical context from joint pretraining; (b) V-GPS uses offline RL (Cal-QL) training pipeline; our Value MLP uses binary success/failure classification, trainable in <5 H100-hours; (c) V-GPS applies to generalist VLA policies (Cartesian action outputs without video-physics pretraining); our Value MLP exploits WAM-specific latent geometry from joint video-action pretraining. V-GPS validates the paradigm (value re-ranking of frozen policies works) in Tier 1 (Cartesian+image space); our paper asks whether Tier 3 (WAM latent space) provides a more discriminative, image-free signal.\n\nKDPE (arXiv 2508.10511, CoRL 2025) — CRITICAL PRIOR WORK. Applies manifold-aware KDE to Cartesian action trajectories (end-effector position/SO(3)-orientation/gripper) from Diffusion Policy; generates N=100 candidates; achieves 88.2% vs. 85% on RoboMimic/MimicGen. CRITICAL FINDING: KDPE-OOD (selecting most out-of-distribution trajectory) performs WORSE than KDPE (selecting most typical) — validates in-distribution selection direction for LOC. Differentiates from LOC: (a) Cartesian action space vs. WAM action latent space; (b) all training data vs. success-only reference; (c) no WAM-specific joint pretraining regularization; (d) N=100 candidates vs. LOC's B=4–8.\n\nWorld2Act (arXiv 2603.10422, March 2026) — post-training framework achieving ~66% on RoboCasa using 50 real + 50 imagined demos; reports UWM achieves 60.8% on RoboCasa with 1,000-demo fine-tuning (confirming frozen UWM baseline is ~10–25%); differentiation: World2Act requires contrastive post-training to align VLA latents; LOC exploits WAM alignment inherited from joint pretraining.\n\nFast-WAM (arXiv 2603.16666) — CRITICAL FRAMING: 97.6% LIBERO-avg (Table 2) and 91.8% RoboTwin (Table 1) at 190ms without video; single trajectory only; our method uses same action-only inference for candidate generation and adds LOC selection at B × 5ms overhead.\n\nRoVer (arXiv 2510.10975, ICLR 2026) — CRITICAL PRIOR WORK: generates B VLA candidates, trains 0.2B PRM; differentiation: requires 0.2B model training vs. LOC's zero training and Value MLP's 3-layer MLP; VLA action tokens lack video-physics regularization.\n\nVerifier-free Test-Time Sampling / MG-Select (arXiv 2510.05681, ICLR 2026) — CRITICAL PRIOR WORK: training-free KL-from-masked-distribution scoring for frozen VLAs; 168% relative improvement on RoboCasa pick-and-place; differentiation: MG-Select measures action-space distributional uncertainty, LOC measures latent OOD membership relative to success demo distribution.\n\nWorld-Value-Action (WAV) Model (arXiv 2604.14732, April 2026) — trajectory value module requiring training from scratch, new architectural component; iterative latent-space inference concentrating probability mass on high-value trajectories. Verified metrics (Table 1, Figure 2): 99.6% LIBERO overall average across 4 splits (Spatial/Object/Goal/Long, Table 1); LIBERO-Long specifically 98.1% (Table 1); 75.6% real-world average (Figure 2, dual-arm Piper robot, 15 trials per task). Note: WAV's LIBERO evaluation covers 4 benchmark splits but does not include LIBERO-90; our primary evaluation uses LIBERO-Long and RoboCasa. Differentiation: WAV trains value and world model jointly from scratch (architectural co-design); our method leaves all WAM weights frozen and is plug-in-compatible with any pretrained WAM.\n\nBest-of-Q (arXiv 2601.22701, January 2026) — Q-function re-ranking of frozen VLM agents for digital tasks (web/OS control); mechanistically analogous to V-GPS applied to digital agents; not in robot manipulation domain but confirms paradigm generality beyond robotics.\n\nALT Policy (arXiv 2505.05787, May 2025) — 'Demystifying Diffusion Policies: Action Memorization and Simple Lookup Table Alternatives': demystifies diffusion policies as implicit nearest-neighbor lookup tables, using contrastive image encoder distance in observation latent space as a runtime OOD signal for single-trajectory retrieval. Related to LOC in applying latent-space OOD proximity as a quality signal, but operates in observation (not action) latent space and retrieves a single stored trajectory rather than scoring multi-candidate selections.\n\nUNISafe (arXiv 2505.00779, May 2025) — 'Uncertainty-aware Latent Safety Filters for Avoiding Out-of-Distribution Failures': calibrates a world model's epistemic uncertainty via conformal prediction to detect OOD state predictions, then performs Hamilton-Jacobi reachability in augmented latent+uncertainty space to synthesize a policy-agnostic safety filter. Related to LOC in applying conformal prediction to world-model latents, but targets state-space safety intervention rather than pre-execution action-latent candidate selection for task performance.\n\nVLS (arXiv 2602.03973, February 2026) — 'Steering Pretrained Robot Policies via Vision-Language Models': applies VLM-generated reward gradients to steer frozen diffusion/flow-matching policies' denoising process toward semantically correct behaviors; training-free guidance via language-conditioned reward signals, not latent-space density or value functions. Different mechanism from both LOC and Value MLP; concurrent work.\n\nFAIL-Detect (arXiv 2503.08558, RSS 2025) — SUPPORTING WORK: proves OOD detection on success-only demonstration data reliably detects policy failures; uses flow-based density estimation on distilled policy signals; motivates LOC's use of KNN/GMM density on success demo latents; FAIL-Detect is execution-time monitoring, LOC is pre-execution candidate selection — Step 1 LOC diagnostic is the first empirical test of whether this principle transfers to pre-execution WAM z_a.\n\nEVA (arXiv 2603.17808, 2026) — identifies 'executability gap' showing visually coherent world model rollouts can violate kinematic constraints; supports LOC over PCS: visual denoising error does not predict task success.\n\nWAV: see above. Compose Your Policies! / GPC (arXiv 2510.01068) — training-free convex composition of multiple frozen policy distributions; operates at distribution level, not discrete candidate selection from single WAM. GPC-RANK (arXiv 2502.00622, IEEE RAL 2025): frozen policy + separately trained action-conditioned world model + hard argmax; uses world-model reward prediction for scoring, not WAM action latent OOD. When to Trust Imagination (arXiv 2605.06222, May 2026): FFDC adaptively decides action chunk sizes during single-trajectory execution; orthogonal and combinable.",
  "approach": "Primary backbone: UWM (github.com/WEIRDLabUW/unified-world-model, RSS 2025), whose independent per-modality diffusion timestep architecture supports action-only inference (policy mode: video timestep = T, action timestep = 0). All WAM weights frozen throughout.\n\n**Step 0a — Frozen UWM Baseline Validation on RoboCasa (MANDATORY FIRST STEP)**: Run B=1 frozen UWM action-only inference on 50 episodes of representative RoboCasa tasks (kitchen manipulation subset). Expected baseline: 10–25% (UWM trained on DROID data only; World2Act reports 60.8% with 1,000-demo fine-tuning, confirming frozen baseline is substantially lower). Decision tree: if baseline ≥ 30%, proceed with current framing; if baseline 10–25%, confirm ≥10pp absolute improvement framing. Cost: ~2–3 H100-hours.\n\n**Step 0b — Reference Distribution Encoding for LOC**: Encode LIBERO-90 success demos through frozen UWM in action-only mode to obtain {z_a^success}. Fit density estimators: (a) KNN nonconformity model (k=10, Euclidean distance); (b) GMM (k=3,5 components, full covariance). Split latents 80/20 train/hold-out for AUC evaluation in Step 1. Cost: ~10–15 H100-hours encoding; ~30 minutes fitting density estimator. Steps 0b and 0c can run in parallel after Step 0a completes.\n\n**Step 0c — Failure Demonstration Collection (required for Value MLP)**: (a) Primary negatives: run frozen UWM (B=1) on LIBERO-Long and validated RoboCasa tasks; expected failure rate 30–50% on RoboCasa tasks, 5–15% on LIBERO-Long, yielding 500–2,000 failure trajectories. Cost: 15–20 H100-hours. (b) Synthetic supplement: Gaussian action perturbation (σ ∈ {0.05, 0.1}) on 20% of LIBERO-90 success demos, simulate in MuJoCo, flag truncated episodes as failures. Cost: <1 H100-hour. Combined: balanced 2,000–4,000 positive / 2,000–4,000 negative training set.\n\n**Step 1 — LOC Diagnostic (MANDATORY before main ablation)**: Empirically tests Hypothesis H1: 'WAM joint pretraining creates a latent success distribution where S_LOC(z_a) achieves AUC > 0.60 as a binary success predictor.' Theoretical motivation: FAIL-Detect's principle (OOD on success-only data detects failures) + KDPE's empirical confirmation (in-distribution selection outperforms outlier selection in Cartesian space). Inference-time caveat: z_a geometry is a training-time property — in action-only inference, video tokens are at full noise (timestep T) providing no inference-time conditioning. We hypothesize that joint training causes z_a to learn quality-discriminative representations even without video input, but Step 1 is the first empirical test of this hypothesis. If H1 fails (AUC < 0.55), LOC reports a negative result.\n\nProtocol: Sample B=16 action-only candidates from frozen UWM on 3 RoboCasa tasks, execute each in simulation (ground-truth success/failure), compute LOC and comparison scores.\n\nLOC metrics: (1) AUC of S_LOC as binary success predictor on held-out demos (target H1: AUC > 0.60); (2) Spearman ρ of S_LOC with success labels (target ρ > 0.3); (3) compare KNN vs. GMM density estimators. Also compute: S_PCS = ||ε − ε_θ(x_{t*}, z_{a,i}, t*)||² for the same candidates, varying t* ∈ {T/4, T/2, 3T/4} (expected to show lower AUC based on Cosmos Policy finding and EVA's executability gap); MG-Select-style KL score as Tier 2 comparison; KDPE-style Cartesian density as Tier 1 comparison baseline.\n\nExpected result: LOC AUC > PCS AUC ≈ MG-Select AUC ≈ KDPE-Cartesian AUC, confirming Tier 3 (WAM latent) is more informative than Tier 1 (Cartesian) and Tier 2 (VLA token distributional uncertainty) methods.\n\nDecision tree: if AUC ≥ 0.60, LOC is primary zero-training method; if LOC 0.55–0.60, both methods reported with LOC as secondary; if LOC < 0.55, LOC reported as negative result with informative comparison.\n\n**Step 2 — Diversity Pilot (combined with LOC diagnostic)**: Same B=16 rollouts measure: pairwise cosine distance of action latents {z_{a,i}} (target mean > 0.05; if lower, increase noise temperature T_noise ∈ {1.5, 2.0}); LOC AUC conditional on latent diversity.\n\n**Step 3 — Value MLP Training**: 3-layer MLP (input: flattened z_a; output: scalar V ∈ [0,1]) trained via binary cross-entropy on balanced success/failure latents from Steps 0b and 0c. Report binary classification accuracy on held-out split (target > 75%). Key distinction from V-GPS: no image input required at inference — z_a encodes visual-physical context from joint pretraining, making the Value MLP an image-free quality discriminator. Cost: ~3–5 H100-hours.\n\n**Step 4 — Inference-Time Best-of-N Planning**: At each planning step, sample B=4–8 action-only trajectories from frozen UWM.\n\nPrimary results (two methods):\n- LOC selection: a_{i*} = argmin_i S_LOC(z_{a,i}) at best density estimator from diagnostic [zero weight updates, WAM-specific, no image at inference]\n- Value MLP selection: a_{i*} = argmax_i V(z_{a,i}) [lightweight training, WAM-specific, no image at inference]\n\nComparisons (required): V-GPS-style Cartesian Q-function applied to WAM action outputs (Tier 1 baseline); MG-Select-style KL scoring applied to WAM action-only inference (Tier 2 baseline); random selection (B=4–8, sanity check); single-trajectory WAM B=1 (frozen baseline).\n\nAblation (secondary): (a) PCS denoising error selection at best t* from diagnostic (expected to underperform LOC); (b) soft MPPI w_i ∝ exp(β·V(z_{a,i})) to document action-averaging artifact; (c) action-only z_a vs. full video+action latent for LOC and Value MLP scoring.\n\n**Ablation Grid**: B ∈ {1, 4, 8} (B=1 is frozen WAM single-trajectory baseline); selection method: LOC KNN vs. LOC GMM (primary zero-training) vs. Value MLP hard argmax (primary trained) vs. V-GPS-style Cartesian scoring (Tier 1 baseline) vs. MG-Select-style KL (Tier 2 baseline) vs. random selection (sanity check); T_noise fixed at 1.0 in primary ablation; execution regime: (a) open-loop vs. (b) periodic replanning every K=5 action chunks.\n\n**Primary hypotheses**: (H1, tested in Step 1 LOC diagnostic) LOC achieves Spearman ρ > 0.3 and AUC > 0.6, confirming WAM success latents form an OOD-detectable distribution even without video input at inference — tested empirically in Step 1; (H2) LOC outperforms PCS and MG-Select-style KL in the diagnostic; (H3) Value MLP achieves ≥10pp improvement over B=1 baseline on RoboCasa; (H4) LOC achieves ≥5pp improvement over B=1 with zero weight updates; (H5) Both methods outperform V-GPS-style Cartesian scoring and MG-Select-style KL applied to WAM outputs, confirming the Tier 3 latent quality-discrimination advantage.\n\n**Standalone Value MLP contribution (applicable if LOC fails H1)**: If LOC AUC < 0.55 in the diagnostic, the paper's narrative shifts to Value MLP as the primary contribution: (a) vs. V-GPS — V-GPS requires ResNet-34 image embedding + 7D Cartesian action at every inference call (Tier 1, image-dependent); Value MLP operates on WAM z_a alone (no image at inference), trained via binary classification rather than offline RL; (b) vs. WAV — WAV trains from scratch as architectural co-design; Value MLP is plug-in-compatible with any pretrained WAM; (c) vs. RoVer — RoVer requires a 0.2B PRM on process labels; Value MLP uses a 3-layer MLP on binary success/failure labels; (d) vs. Cosmos Policy — 1,536 H100-hours rollout fine-tuning vs. ≤40 H100-hours; (e) vs. KDPE — KDPE operates in Cartesian space with all training data; Value MLP uses WAM latent space with success/failure-labeled data. Central empirical claim: joint pretraining creates a latent space where success/failure are more linearly separable than in Cartesian action space, enabling a 3-layer image-free MLP to match or exceed the discriminative power that V-GPS achieves via a ResNet-34-augmented Q-function with offline RL.\n\n**Proactive framing against fine-tuned baselines**: Expected absolute RoboCasa performance (~20–35% after ≥10pp improvement from 10–25% frozen baseline) will appear weak against Cosmos Policy (67.1%) and World2Act (~66%). The paper must explicitly frame this in the introduction and evaluation sections: 'Our methods are orthogonal to fine-tuning — they extract planning value from existing pretrained WAMs in settings where domain-specific demonstration data is unavailable. The comparison target is B=1 frozen WAM inference at the same data budget (zero domain-specific demos for LOC; ≤40 H100-hours of simulation rollouts for Value MLP), not fine-tuned models that consumed 1,000 real robot demonstrations or 1,536 H100-hours of rollout fine-tuning. In zero-demonstration deployment scenarios — a common real-world constraint — our methods improve over the no-adaptation baseline by ≥10pp without any weight updates or real robot data collection. The gap versus fine-tuned methods quantifies the cost of the zero-demonstration constraint, not a failure of candidate selection.'\n\n**Evaluation Benchmarks**: (a) Primary — RoboCasa: Cosmos Policy fine-tuned 67.1%; World2Act (Cosmos+World2Act) ~66%; frozen UWM expected 10–25% (validated in Step 0a); absolute target ≥10pp over frozen baseline. (b) Secondary — LIBERO-Long: near saturation for strong frozen WAMs (Fast-WAM 95.2%, Table 2); included to characterize gain profile vs. task difficulty. (c) Baselines: B=1 frozen WAM, random selection, V-GPS-style Cartesian scoring, MG-Select-style KL applied to WAM.\n\nDreamZero cross-WAM validation deferred to camera-ready. CoRL submission rests on UWM alone.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~140h H100",
      "gpu_utilization": "HIGH idle (~35–55%): GPU waits while researcher implements LOC density estimator (KNN/GMM fitting), interprets LOC diagnostic results, debugs failure collection pipeline, and designs ablations.",
      "timeline": "2–3 months",
      "team": "1–2 researchers",
      "estimated_gpu_cost": "~$350 (140h × $2.50/h blended Lambda/RunPod/Vast.ai H100 rate)"
    },
    "human_in_loop": {
      "gpu_hours": "~165h H100",
      "gpu_utilization": "MODERATE idle (~20–30%): agent handles code scaffolding, baseline validation, LOC diagnostic, failure collection, demo encoding, density estimator fitting, and experiment submission; human reviews Step 0a baseline and LOC diagnostic results at daily check-ins to make go/no-go decisions",
      "timeline": "3–4 weeks",
      "team": "1 researcher, ~30 min/day check-in",
      "claude_api_cost": "$150–250 (~1,500–2,500 turns at mixed Sonnet/Opus rates)",
      "estimated_gpu_cost": "~$413 (165h × $2.50/h)",
      "risk_note": "Step 0a (frozen UWM RoboCasa baseline) and LOC diagnostic are hard sequential dependencies before main ablation. Sequential order: 0a baseline validation (2–3 H100-hours, Day 1–2) → LOC diagnostic (3–5 H100-hours, Day 2–4) → failure collection (15–20 H100-hours, Day 3–7, parallel with LOC) → demo encoding + density fitting (10–15 H100-hours, Day 5–9) → Value MLP training (3–5 H100-hours, Day 9–10) → main ablations (Day 10–18). RoboCasa simulation setup requires separate engineering effort from LIBERO. DreamZero cross-WAM deferred to camera-ready."
    },
    "auto_research": {
      "gpu_hours": "~185h H100 (revised from prior 320h estimate; ablation grid pruned to stay within ≤200h hard constraint)",
      "gpu_budget_breakdown": "Step 0a frozen UWM baseline: ~3h; Steps 0b+0c in parallel (demo encoding + failure collection): ~32h billed (12h encoding + 20h failure collection running concurrently); Step 1 LOC diagnostic: ~4h; Step 3 Value MLP training: ~5h; Main ablation grid (B ∈ {1,4,8} × 6 methods × 3 seeds × 2 benchmarks = 108 runs × ~1.2h avg): ~130h; contingency/reruns: ~11h. Total: ~185h billed GPU-hours. With 4 GPUs running ablation batch concurrently: wall-clock ≈ 44h setup + 33h ablations = 77h wall-clock; billed ≤ 200h hard constraint.",
      "gpu_utilization": "MINIMAL idle (~5–10%): agent pipelines baseline validation, LOC diagnostic, failure collection, demo encoding, density fitting, MLP training, and evaluation continuously.",
      "timeline": "7–10 days with 4 H100 GPUs simultaneously",
      "team": "0 (only initial repo setup and credential configuration)",
      "claude_api_cost": "$200–350 (~2,500–4,000 turns at Opus rates)",
      "estimated_gpu_cost": "~$463 (185h × $2.50/h)",
      "ablation_grid_vs_prior": "Ablation grid expanded from 5 to 6 selection methods by adding V-GPS-style Cartesian scoring as a Tier 1 baseline, providing direct Tier 1 vs. Tier 3 comparison. T_noise sweep ({1.0,1.5,2.0}) dropped from auto research grid — T_noise fixed at 1.0 unless diversity pilot (Step 2) shows mean cosine distance < 0.05. B grid: {1,4,8} (B=1 is frozen WAM single-trajectory baseline). PCS full ablation retained only in Step 1 LOC diagnostic.",
      "speed_bottleneck": "Step 0a baseline validation → LOC diagnostic → (parallel: failure collection + demo encoding) → density fitting (trivial) + Value MLP training is a 5-step sequential dependency spanning ~8 days minimum. RoboCasa evaluation rollouts: each ablation variant requires sequential per-task evaluation; with 4 GPUs running 4 variants concurrently, the full grid needs ~5–7 days.",
      "risk_note": "LOC density estimation (KNN/GMM) is a standard sklearn/torch operation requiring no custom implementation. Main implementation risk: UWM action latent extraction in action-only mode (video timestep = T, action timestep = 0) — this mode is supported by UWM's architecture but may require engineering to extract z_a as a fixed-size vector for density estimation. If z_a is not directly accessible, the Action Decoder intermediate activations serve as a substitute latent representation. V-GPS-style Cartesian baseline requires implementing the Cartesian action extraction and Q-function scoring as an additional comparison method."
    }
  },
  "target_venues": [
    "CoRL 2026 (Abstract deadline: May 26, 2026; Full paper: May 29, 2026; Conference: Nov 9–12, Austin TX) — TIGHT but viable: 19 days from 2026-05-10. Step 0a RoboCasa baseline must run immediately (Day 1–2). Minimum viable submission: frozen UWM RoboCasa baseline validation + LOC diagnostic figure (including PCS and Tier 1/Tier 2 comparison showing expected negative results) + LOC and/or Value MLP Best-of-N results (primary) + LIBERO-Long (secondary) + B/hard-argmax ablation + V-GPS-style Cartesian and MG-Select-style KL baseline comparisons. DreamZero cross-WAM deferred to camera-ready.",
    "ICLR 2027 (deadline ~September–October 2026) — More feasible timeline for complete ablation grid, latent geometry analysis (success/failure separation across Tier 1/2/3 representations), DreamZero cross-WAM evaluation, and potential real-world experiments."
  ],
  "level": "solid",
  "key_references": [
    "V-GPS: Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance (arXiv 2410.13816, CoRL 2024) — CRITICAL PRIOR WORK for Value MLP: trains Q-function via offline RL (Cal-QL) on sparse binary rewards; architecture: ResNet-34 image encoder + 7D Cartesian action → scalar Q-value; applies to frozen Octo-small/Octo-base/Octo-small-1.5/RT-1X/OpenVLA; samples K=50 candidates; achieves +82.8% relative improvement (Octo-small-1.5 baseline 24% → V-GPS 44%) on real-robot 6-task benchmark; validates value re-ranking paradigm for frozen policies in Tier 1 (Cartesian+image) space. Differentiates from Value MLP: (a) V-GPS requires ResNet-34 image embedding + raw 7D action at every inference call; Value MLP uses WAM z_a alone (no image needed at inference); (b) offline RL training vs. binary classification; (c) Cartesian+image vs. WAM latent space",
    "Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning (arXiv 2601.16163, ICLR 2026) — CRITICAL PRIOR WORK: implements Best-of-N planning mode (15 forward passes per action via majority-mean aggregation of world model + value function queries); requires rollout fine-tuning because demo-only training 'cannot correctly predict failure states'; 1,536 H100-hours for RoboCasa; 98.5% LIBERO, 67.1% RoboCasa; our LOC requires zero rollout data and zero weight updates",
    "KDPE: A Kernel Density Estimation Strategy for Diffusion Policy Trajectory Selection (arXiv 2508.10511, CoRL 2025) — CRITICAL PRIOR WORK: applies manifold-aware KDE to Cartesian action trajectories (end-effector position/SO(3)-orientation/gripper) from Diffusion Policy; generates N=100 candidates; achieves 88.2% vs. 85% on RoboMimic/MimicGen; CRITICAL FINDING: KDPE-OOD (selecting most out-of-distribution trajectory) performs WORSE than KDPE — validates in-distribution selection direction for LOC; Tier 1 (Cartesian space) method",
    "World2Act (arXiv 2603.10422, March 2026) — post-training framework achieving ~66% on RoboCasa using 50 real + 50 imagined demos; reports UWM achieves 60.8% on RoboCasa with 1,000-demo fine-tuning (confirming frozen UWM baseline is ~10–25%); differentiation: World2Act requires contrastive post-training to align VLA latents; LOC exploits WAM alignment inherited from joint pretraining",
    "Fast-WAM: World Action Models without Test-Time Video (arXiv 2603.16666) — CRITICAL FRAMING: 97.6% LIBERO-avg (Table 2) and 91.8% RoboTwin (Table 1) at 190ms without video; single trajectory only; our method uses same action-only inference for candidate generation and adds LOC selection at B × 5ms overhead",
    "FAIL-Detect: Failure Detection as OOD Detection for Robot Manipulation (arXiv 2503.08558, RSS 2025) — SUPPORTING WORK: proves OOD detection on success-only demonstration data reliably detects policy failures; motivates LOC's use of KNN/GMM density on success demo latents; FAIL-Detect is execution-time monitoring, LOC is pre-execution candidate selection — Step 1 LOC diagnostic is the first empirical test of whether this principle transfers to pre-execution WAM z_a in action-only inference mode",
    "EVA: Aligning Video World Models with Executability (arXiv 2603.17808, 2026) — identifies 'executability gap' showing visually coherent world model rollouts can violate kinematic constraints; supports LOC over PCS: visual denoising error does not predict task success",
    "RoVer: Robot Reward Model as Test-Time Verifier for Vision-Language-Action Models (arXiv 2510.10975, ICLR 2026) — CRITICAL PRIOR WORK: generates B VLA candidates, trains 0.2B PRM; Tier 2 (VLA action token) method; differentiation: requires 0.2B model training vs. LOC's zero training and Value MLP's 3-layer MLP; VLA action tokens lack video-physics regularization",
    "Verifier-free Test-Time Sampling / MG-Select (arXiv 2510.05681, ICLR 2026) — CRITICAL PRIOR WORK: training-free KL-from-masked-distribution scoring for frozen VLAs; 168% relative improvement on RoboCasa pick-and-place; Tier 2 (VLA action token distributional uncertainty) method; differentiation: MG-Select measures action-space distributional uncertainty, LOC measures latent OOD membership relative to success demo distribution",
    "World-Value-Action (WAV) Model (arXiv 2604.14732, April 2026) — trajectory value module requiring architectural co-design and training from scratch; verified metrics: 99.6% LIBERO overall average across 4 splits (Spatial/Object/Goal/Long, Table 1); LIBERO-Long specifically 98.1% (Table 1); 75.6% real-world (Figure 2, dual-arm Piper robot, 15 trials per task); our method leaves all WAM weights frozen and is plug-in-compatible with pretrained WAMs",
    "ALT Policy (arXiv 2505.05787, May 2025) — 'Demystifying Diffusion Policies: Action Memorization and Simple Lookup Table Alternatives': uses contrastive image encoder distance in observation latent space as runtime OOD signal for single nearest-neighbor action retrieval; related to LOC in applying latent-space proximity as a quality signal, but in observation (not action) latent space and via retrieval rather than multi-candidate selection",
    "UNISafe (arXiv 2505.00779, May 2025) — 'Uncertainty-aware Latent Safety Filters for Avoiding Out-of-Distribution Failures': calibrates world model epistemic uncertainty via conformal prediction for OOD-based safety filtering in state latent space; related to LOC in applying conformal prediction to world-model latents, but targets state-space safety rather than pre-execution action-latent candidate selection",
    "VLS: Steering Pretrained Robot Policies via Vision-Language Models (arXiv 2602.03973, February 2026) — training-free VLM-reward-gradient guidance of frozen diffusion/flow-matching policies' denoising process; different mechanism from both LOC (latent OOD density) and Value MLP (binary classification); concurrent work",
    "Compose Your Policies! / GPC (arXiv 2510.01068) — training-free convex composition of multiple frozen policy distributions; operates at distribution level, not discrete candidate selection from single WAM",
    "Inference-Time Enhancement / GPC-RANK (arXiv 2502.00622, IEEE RAL 2025) — frozen policy + separately trained action-conditioned world model + hard argmax; uses world-model reward prediction for scoring, not WAM action latent OOD",
    "Unified World Models / UWM (arXiv 2504.02792, RSS 2025) — primary backbone; independent per-modality timesteps support action-only inference; publicly available weights and code",
    "Diffusion Policy (arXiv 2303.04137, RSS 2023 / IJRR 2024) — documents multi-modal action distribution handling; confirms averaging over manipulation action modes produces infeasible blended actions; justifies hard argmax over soft MPPI weighting",
    "When to Trust Imagination (arXiv 2605.06222, May 2026) — CONCURRENT WORK: FFDC adaptively decides action chunk sizes; orthogonal to our pre-execution selection; combinable",
    "World Action Models as Zero-shot Policies / DreamZero (arXiv 2602.15922) — 14B joint video+action DiT; secondary backbone for cross-WAM validation in camera-ready/ICLR version",
    "OA-WAM (arXiv 2605.06481, May 2026) — concurrent work; different problem (object binding)",
    "CKT-WAM (arXiv 2605.06247, May 2026) — concurrent work; different problem (cross-WAM knowledge transfer)",
    "GigaBrain-0.5M* (arXiv 2602.12099) — RAMP RL loop requires 30%+ more training",
    "H-WM (arXiv 2602.11291) — requires hierarchical architectural co-design",
    "Latent Diffusion Planning (arXiv 2504.16925) — trains diffusion planner from scratch"
  ],
  "description": "Latent-Distribution Candidate Selection (LDCS) converts any pretrained video-diffusion World Action Model into a multi-candidate planner at inference time without modifying any WAM weight, exploiting WAM-specific latent structure through two complementary methods — positioned within a three-tier action representation hierarchy for candidate selection.\n\n**The three-tier framing**: Existing candidate selection methods operate in three representational tiers: (1) Cartesian action space — KDPE (kernel density, N=100 candidates) and V-GPS (Q-function re-ranking via offline RL on 7D actions + ResNet-34 image embeddings, +82.8% real-robot improvement, CoRL 2024), both requiring raw action representations and, for V-GPS, image input at every inference call; (2) VLA action tokens — MG-Select (KL-divergence confidence) and RoVer (0.2B PRM) without video-physics co-regularization; (3) WAM action latents z_a — continuous latents from joint video-action diffusion pretraining (this paper). The central hypothesis: WAM latent space offers richer quality-discriminative geometry than Tier 1 (Cartesian+image) or Tier 2 (VLA tokens), enabling simpler discriminators without image input at inference.\n\n**Inference-time caveat on z_a geometry**: In action-only inference (video timestep = T), video tokens are at full noise — no inference-time video conditioning occurs. The quality-discriminative structure of z_a is a training-time property of joint pretraining. Step 1 (LOC diagnostic) is the first empirical test of whether this geometry persists as a success/failure discriminator without video input. If H1 fails (AUC < 0.55), LOC reports a negative result and Value MLP becomes the sole primary contribution.\n\n**Method 1 — Latent OOD Consistency Scoring (LOC, zero weight updates)**: Fit a KNN or GMM density estimator on WAM action latents {z_a^success} from LIBERO-90 success demos. At inference, sample B=4–8 action-only candidates and score each by nonconformity: S_LOC(z_{a,i}) = −log p̂(z_{a,i}). Select argmin (most in-distribution candidate). Overhead: B × ~5ms = 20–40ms for B=4–8. No image needed at inference.\n\n**Method 2 — Action-Latent Value MLP (≤40 H100-hours)**: 3-layer MLP trained on {z_a^success} and explicitly collected failure latents. Hard argmax selection. No image needed at inference — z_a encodes visual-physical context from joint pretraining. Differentiated from V-GPS: operates on WAM z_a alone (no ResNet-34 image embedding), uses binary classification (not offline RL), and is trained in <5 H100-hours. Central hypothesis: joint pretraining creates a latent space where success/failure are more linearly separable than in Cartesian action space, enabling a 3-layer image-free MLP to match or exceed discriminative power that V-GPS achieves via Cartesian+image Q-function.\n\n**LOC Diagnostic (mandatory, Step 1)**: B=16 rollouts on 3 RoboCasa tasks, measuring AUC of S_LOC as binary success predictor (target H1: AUC > 0.6), compared against: (a) video denoising error S_PCS, (b) MG-Select-style KL (Tier 2), (c) V-GPS-style Cartesian density (Tier 1). Tests the full three-tier hierarchy in a controlled diagnostic before committing to the main ablation.\n\nPrimary evaluation: RoboCasa (target ≥10pp absolute over frozen baseline; Cosmos Policy 67.1% / World2Act ~66% as fine-tuned upper references — explicitly framed as orthogonal to our zero-demonstration deployment target). Secondary: LIBERO-Long. Auto research ablation grid: B ∈ {1,4,8} × 6 methods × 3 seeds × 2 benchmarks (~185 billed H100-hours ≤ 200h hard constraint). CoRL submission: UWM only; DreamZero cross-WAM deferred to camera-ready.",
  "project_name": "frozen_wam_mppi",
  "source": "web_research"
}

## Reviewer feedback (round 7)
Issues: ["PERSISTENT FACTUAL ERROR — WAV metrics STILL incorrect in Round 7 despite explicit Round 6 instruction: The submission claims '99.6% LIBERO overall average across 4 splits (Table 1)' for WAV (arXiv 2604.14732). Independent verification confirms WAV reports Spatial 100.0%, Object 98.6%, Goal 94.4%, Long 98.1% — averaging ~97.8%, not 99.6%. This error was explicitly flagged in Round 6 with the instruction 'Fetch the WAV paper PDF directly and correct the stated metrics with table references.' The generator responded by adding 'verified metrics (Table 1, Figure 2)' — but the numbers remain wrong. Citing incorrect metrics for a concurrent paper is a credibility-damaging error that CoRL reviewers will catch.", "SIGNIFICANT — Two published concurrent papers are uncited and must be differentiated: (1) Latent Policy Barrier (arXiv 2508.05941): uses Euclidean distance in visual observation latent space to nearest expert demo state as OOD signal, steering the policy if the state is OOD. Differentiates from LOC: LPB operates on observation latents (not WAM action latents z_a), does runtime execution-time steering (not pre-execution candidate selection), and uses a separate dynamics model rather than the frozen WAM's joint pretraining. (2) Latent Policy Steering (arXiv 2507.13340): trains a value function in world model latent space using both expert states and policy-rollout states, achieving +50% relative improvement with 30 demos on real-world tasks. Differentiates from Value MLP: LPS uses optic flow as embodiment-agnostic action representation (not WAM action latents z_a), requires policy-rollout data for training (not just binary success/failure from demos+frozen-policy failures), and does not exploit WAM joint-pretraining latent geometry. Both papers must be added to related work with explicit differentiation — they establish that latent-space OOD and value functions for robot policy improvement is an active published direction, and reviewers in this space will know them.", "MODERATE — Being-H0.7 (arXiv 2605.00078, May 2026) achieves 99.2% on LIBERO and represents a strong concurrent WAM. While not a candidate selection paper (it uses latent prior-posterior alignment rather than Best-of-N scoring), it should be briefly mentioned in the landscape section as a concurrent WAM result to contextualize LIBERO score comparisons.", "MINOR — The claim that KDPE-OOD performs substantially worse (ToolHang: 7% vs 76%) is now independently confirmed and is a strong supporting finding for LOC's in-distribution selection direction. The submission should explicitly cite these KDPE ablation numbers (not just 'KDPE-OOD performs worse') since the magnitude of the effect (7% vs 76%) is a compelling empirical motivator."]
Feedback: Round 7 has correctly addressed all Round 6 issues: V-GPS cited with three-tier hierarchy differentiation, LOC hypothesis correctly framed as H1 with diagnostic gate, action-only mode caveat stated, ALT Policy and UNISafe cited, RoboCasa framing proactively addressed, budget correctly computed. Three targeted fixes are needed:

**1. Fix WAV metrics immediately (0.5 day) — do not submit with wrong numbers.** The correct WAV LIBERO numbers are approximately Spatial 100.0%, Object 98.6%, Goal 94.4%, Long 98.1% (average ~97.8%, NOT 99.6%). Correct the landscape and key_references entries to match the actual table values. This is the third consecutive round this error has appeared; a CoRL reviewer who has read WAV will notice immediately.

**2. Add Latent Policy Barrier (arXiv 2508.05941) and Latent Policy Steering (arXiv 2507.13340) to related work (1 day).** Write: 'Latent Policy Barrier (LPB, 2025) uses Euclidean distance in visual observation latent space to nearest expert demo state for OOD detection during execution; our LOC operates in WAM action latent space z_a (not observation latents) and scores B pre-execution candidates rather than performing runtime steering, exploiting WAM joint-pretraining geometry unavailable to observation-space methods. Latent Policy Steering (LPS, 2025) trains a value function in world model latent space using expert plus policy-rollout states; our Value MLP uses WAM-specific z_a from joint video-action pretraining and requires only binary success/failure labels from collected failures (no rollout policy-visit data), testing whether joint pretraining creates a more linearly separable latent geometry.' These differentiations are legitimate and clear — turning the citations into positioning assets rather than gaps.

**3. Strengthen the KDPE-OOD citation with magnitude (0.5 day).** The ToolHang ablation (KDPE-OOD 7% vs KDPE 76%) is a striking finding that empirically motivates in-distribution selection. Cite this specific number in the LOC motivation: 'KDPE finds that out-of-distribution selection collapses performance on ToolHang (7% vs. 76%), providing strong empirical grounding for LOC's argmin selection direction.'

With these three fixes (~2 days), the submission is CoRL-ready. The three-tier hierarchy and mandatory LOC diagnostic with fallback are strong scientific contributions. Minimum viable submission scope (UWM + RoboCasa + LIBERO-Long + LOC diagnostic figure + B/hard-argmax ablation) remains the right call.

## Instructions
- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.
- Address each issue specifically.

## 深度调研要求（每一轮修订都必须执行）

不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。

1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。
   - 搜索最新的相关论文（arXiv, conference proceedings）
   - 搜索 benchmark/leaderboard 确认当前 SOTA
   - 搜索可能遗漏的相关工作和 concurrent work

2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，
   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。

3. **深度思考**：在修订之前，先独立思考以下问题：
   - 这个 idea 的核心假设是否仍然成立？
   - reviewer 的批评是否揭示了更深层的问题？
   - 有没有更好的 framing 或 approach 来解决同一个核心问题？
   - 修订后的 idea 相比上一版有什么本质性的改进？

4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，
   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。

## 针对 Review 意见的定向搜索

对 reviewer 指出的每个问题，执行以下搜索流程：

1. **如果 reviewer 说'已有类似工作'**：
   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读
   - 搜索该论文的 cited-by，找到后续跟进工作
   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot

2. **如果 reviewer 说'SOTA 过时'**：
   - 用 Papers With Code 查看当前排行榜
   - 搜索过去 6 个月的最新方法
   - 更新你的 landscape 和 baseline

3. **如果 reviewer 说'可行性有问题'**：
   - 搜索类似规模实验的实际成本和时间线
   - 搜索 GitHub 上是否有可复用的实现
   - 搜索相关数据集/模型的可获取性

4. **如果 reviewer 说'novelty 不足'**：
   - 对核心方法尽量做 3-5 种不同关键词组合的搜索
   - 搜索相邻领域是否有类似思路
   - 如果确实 novelty 不足，考虑 major revision 或 pivot

- Use WebSearch to find updated information if the reviewer flagged outdated claims.
- You have full freedom in how much to change:
  - Minor fix: if only specific details are wrong, correct them and keep everything else.
  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.
  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.
- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.
- In the output JSON, include a "change_type" field with one of: "minor", "major", or "pivot" to indicate the scope of your changes.
- Output the revised idea as a COMPLETE JSON object (same schema as original, plus "change_type").

## 停滞提醒
这个 idea 已经经过 7 轮修订，近 3 轮的平均分从 3.2 到 3.5，没有明显改善。

请认真思考：
- 当前方向是否存在根本性的瓶颈？反复的 minor fix 是否在回避核心问题？
- 如果你认为问题出在 approach 而非 framing，可以做 major revision。
- 如果你认为 core problem 本身就有问题（gap 不存在、问题不够重要），pivot 到同一研究领域下的新方向可能是更好的选择。
- 当然，如果你有信心这一轮修订能实现突破，继续改进也完全可以。

最终由你判断——做你认为最能提升 idea 质量的选择。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "30743365-00ab-422a-8f74-21081fe9d3c6",
  "type": "user",
  "uuid": "3b944877-4cef-41a7-98d4-21a62b083878",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b9fbaa-4159-4906-9e7b-5c7c38fdb4da",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T09:30:25.850Z_

```json
{
  "parentUuid": "3b944877-4cef-41a7-98d4-21a62b083878",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "8ec4a365-0091-46bb-bcdc-86c587ca185f",
  "timestamp": "2026-05-10T09:30:25.850Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b9fbaa-4159-4906-9e7b-5c7c38fdb4da",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T09:30:25.850Z_

```json
{
  "parentUuid": "8ec4a365-0091-46bb-bcdc-86c587ca185f",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "dde58a63-2f5c-441f-8e9a-5ff93d390a14",
  "timestamp": "2026-05-10T09:30:25.850Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b9fbaa-4159-4906-9e7b-5c7c38fdb4da",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Latent-Distribution Candidate Selection for Frozen World Action Models…",
  "leafUuid": "dde58a63-2f5c-441f-8e9a-5ff93d390a14",
  "sessionId": "f0b9fbaa-4159-4906-9e7b-5c7c38fdb4da"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Frozen WAM candidate selection via action latent OOD scoring",
  "sessionId": "f0b9fbaa-4159-4906-9e7b-5c7c38fdb4da"
}
```

---

### Assistant

_source line 8 · 2026-05-10T09:30:37.767Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the situation carefully before making any decisions.

**Current State:**
- Round 7 of revisions, stagnant at 3.2-3.5 average score over recent rounds
- The reviewer has identified 4 issues, 3 of which are fixable (WAV metrics correction, adding 2 new papers, strengthening KDPE-OOD citation)
- The reviewer says "With these three fixes (~2 days), the submission is CoRL-ready"
- The reviewer explicitly states the three-tier hierarchy and mandatory LOC diagnostic with fallback are strong scientific contributions

**Issues to fix:**


First, I need to verify the WAV metrics—the paper reports 99.6% overall average, but the actual breakdown shows Spatial at 100.0%, Object at 98.6%, Goal at 94.4%, and Long at 98.1%, which averages closer to 97.8%. I should pull the paper to confirm these numbers. Second, I need to add citations for two recent papers on latent policy barriers and steering. Third, I should strengthen the KDPE-OOD discussion by highlighting the stark difference in ToolHang performance—7% versus 76%. The reviewer's feedback is actually encouraging here, signaling that these targeted fixes could push the work toward acceptance. I need to pull the WAV paper to verify those metrics, then grab the two latent policy papers to write proper differentiations, and check the KDPE paper for the ToolHang numbers—I'll fetch these in parallel to move quickly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dde58a63-2f5c-441f-8e9a-5ff93d390a14",
  "isSidechain": false,
  "requestId": "req_011CateuDrdZLKetiSBwC87z",
  "type": "assistant",
  "uuid": "fdd73ebe-2bb3-42b9-83e4-6cdbca237fb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b9fbaa-4159-4906-9e7b-5c7c38fdb4da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_018q1Q6jxKSb8ERPyGr7tvoj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21285,
      "cache_read_input_tokens": 11631,
      "output_tokens": 747,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21285,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 747,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 21285,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21285
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-10T09:30:37.792Z_

I'll start by fetching the WAV paper and the two new papers in parallel to get accurate information before making any edits.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fdd73ebe-2bb3-42b9-83e4-6cdbca237fb1",
  "isSidechain": false,
  "requestId": "req_011CateuDrdZLKetiSBwC87z",
  "type": "assistant",
  "uuid": "5a5a6cf3-fd72-4587-9160-52f341a51373",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b9fbaa-4159-4906-9e7b-5c7c38fdb4da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_018q1Q6jxKSb8ERPyGr7tvoj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21285,
      "cache_read_input_tokens": 11631,
      "output_tokens": 747,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21285,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 747,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 21285,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21285
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-10T09:30:37.801Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Eq2tBQKxPvnLDdy8bZD93g`</summary>

```json
{
  "query": "select:WebFetch,WebSearch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a5a6cf3-fd72-4587-9160-52f341a51373",
  "isSidechain": false,
  "requestId": "req_011CateuDrdZLKetiSBwC87z",
  "type": "assistant",
  "uuid": "2b6f6575-96bd-4984-9dc8-211cd311121c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b9fbaa-4159-4906-9e7b-5c7c38fdb4da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_018q1Q6jxKSb8ERPyGr7tvoj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21285,
      "cache_read_input_tokens": 11631,
      "output_tokens": 747,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21285,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 747,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 21285,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21285
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T09:30:37.813Z_

<details><summary>↩ Tool result · `toolu_01Eq2tBQKxPvnLDdy8bZD93g`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b6f6575-96bd-4984-9dc8-211cd311121c",
  "isSidechain": false,
  "promptId": "30743365-00ab-422a-8f74-21081fe9d3c6",
  "type": "user",
  "uuid": "2e9179f0-33f9-42d7-a82c-bdaff9905733",
  "toolUseResult": {
    "matches": [
      "WebFetch",
      "WebSearch"
    ],
    "query": "select:WebFetch,WebSearch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "2b6f6575-96bd-4984-9dc8-211cd311121c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b9fbaa-4159-4906-9e7b-5c7c38fdb4da",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-10T09:30:40.720Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me fetch the three key papers in parallel:
1. WAV paper (arXiv 2604.14732) - to get correct LIBERO metrics
2. Latent Policy Barrier (arXiv 2508.05941) - new paper to cite
3. Latent Policy Steering (arXiv 2507.13340) - new paper to cite
4. KDPE paper (arXiv 2508.10511) - to confirm ToolHang numbers

I'll fetch all four in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e9179f0-33f9-42d7-a82c-bdaff9905733",
  "isSidechain": false,
  "requestId": "req_011Catev6pzNEw6ozH4HEdSD",
  "type": "assistant",
  "uuid": "fe7aefaf-6893-46ef-9739-d86fea52f637",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b9fbaa-4159-4906-9e7b-5c7c38fdb4da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BLefQCC8JqQzuUcwMV4KPh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1767,
      "cache_read_input_tokens": 32916,
      "output_tokens": 738,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1767,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 738,
          "cache_read_input_tokens": 32916,
          "cache_creation_input_tokens": 1767,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1767
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-10T09:30:41.108Z_

Fetching the WAV paper, both new papers, and the KDPE paper in parallel to get accurate data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe7aefaf-6893-46ef-9739-d86fea52f637",
  "isSidechain": false,
  "requestId": "req_011Catev6pzNEw6ozH4HEdSD",
  "type": "assistant",
  "uuid": "56409e77-84c2-4fca-aa70-80a15b0c7147",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b9fbaa-4159-4906-9e7b-5c7c38fdb4da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BLefQCC8JqQzuUcwMV4KPh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1767,
      "cache_read_input_tokens": 32916,
      "output_tokens": 738,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1767,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 738,
          "cache_read_input_tokens": 32916,
          "cache_creation_input_tokens": 1767,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1767
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-10T09:30:42.680Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HECRMDhehGQCVU1x1b5791`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.14732",
  "prompt": "Extract all LIBERO benchmark numbers (Spatial, Object, Goal, Long splits) and real-world robot task success rates from Table 1 and Figure 2. Report exact percentages cited in the paper for WAV model performance."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56409e77-84c2-4fca-aa70-80a15b0c7147",
  "isSidechain": false,
  "requestId": "req_011Catev6pzNEw6ozH4HEdSD",
  "type": "assistant",
  "uuid": "bd154423-2e8b-4423-ba25-f2ce6da0d1ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b9fbaa-4159-4906-9e7b-5c7c38fdb4da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BLefQCC8JqQzuUcwMV4KPh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1767,
      "cache_read_input_tokens": 32916,
      "output_tokens": 738,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1767,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 738,
          "cache_read_input_tokens": 32916,
          "cache_creation_input_tokens": 1767,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1767
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-10T09:30:44.948Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01YcN3br1ZA8Vfg7GGTuy4CP`</summary>

```json
{
  "url": "https://arxiv.org/abs/2508.05941",
  "prompt": "Extract: (1) what latent space is used for OOD detection (observation or action?), (2) what the method does at runtime vs pre-execution, (3) whether it uses a frozen policy or modifies weights, (4) key performance numbers, (5) the core mechanism in 2-3 sentences. Focus on what differentiates it from action-latent candidate selection methods."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd154423-2e8b-4423-ba25-f2ce6da0d1ce",
  "isSidechain": false,
  "requestId": "req_011Catev6pzNEw6ozH4HEdSD",
  "type": "assistant",
  "uuid": "854b2909-98d3-430b-8dc9-71b6abe3f184",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b9fbaa-4159-4906-9e7b-5c7c38fdb4da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BLefQCC8JqQzuUcwMV4KPh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1767,
      "cache_read_input_tokens": 32916,
      "output_tokens": 738,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1767,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 738,
          "cache_read_input_tokens": 32916,
          "cache_creation_input_tokens": 1767,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1767
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-10T09:30:45.340Z_

<details><summary>↩ Tool result · `toolu_01HECRMDhehGQCVU1x1b5791`</summary>

```text
I cannot extract the specific benchmark numbers you're requesting from the provided content. The webpage excerpt only shows the abstract and metadata for the arXiv paper, which states that "WAV model consistently outperforms state-of-the-art methods, achieving significant improvements in task success rate, generalization ability, and robustness, especially in long-horizon and compositional scenarios."

However, the actual Tables 1 and Figure 2 containing the LIBERO benchmark results (Spatial, Object, Goal, Long splits) and real-world robot task success rates are not included in this page content. To obtain those exact percentages, you would need to access the full PDF or HTML version of the paper using the links provided on the page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd154423-2e8b-4423-ba25-f2ce6da0d1ce",
  "isSidechain": false,
  "promptId": "30743365-00ab-422a-8f74-21081fe9d3c6",
  "type": "user",
  "uuid": "0bce78f2-26bf-4b58-8727-af70f7f770df",
  "toolUseResult": {
    "bytes": 48255,
    "code": 200,
    "codeText": "OK",
    "result": "I cannot extract the specific benchmark numbers you're requesting from the provided content. The webpage excerpt only shows the abstract and metadata for the arXiv paper, which states that \"WAV model consistently outperforms state-of-the-art methods, achieving significant improvements in task success rate, generalization ability, and robustness, especially in long-horizon and compositional scenarios.\"\n\nHowever, the actual Tables 1 and Figure 2 containing the LIBERO benchmark results (Spatial, Object, Goal, Long splits) and real-world robot task success rates are not included in this page content. To obtain those exact percentages, you would need to access the full PDF or HTML version of the paper using the links provided on the page.",
    "durationMs": 2657,
    "url": "https://arxiv.org/abs/2604.14732"
  },
  "sourceToolAssistantUUID": "bd154423-2e8b-4423-ba25-f2ce6da0d1ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b9fbaa-4159-4906-9e7b-5c7c38fdb4da",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-10T09:30:46.856Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Xhf6KhA4CXYtdkeC4DmNK2`</summary>

```json
{
  "url": "https://arxiv.org/abs/2507.13340",
  "prompt": "Extract: (1) what latent space is used for the value function, (2) what action representation is used (optic flow or joint angles?), (3) whether rollout data is required for training, (4) key performance numbers (+50% relative improvement?), (5) the core mechanism in 2-3 sentences. Focus on what differentiates it from WAM action-latent value methods."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0bce78f2-26bf-4b58-8727-af70f7f770df",
  "isSidechain": false,
  "requestId": "req_011Catev6pzNEw6ozH4HEdSD",
  "type": "assistant",
  "uuid": "e6db4cf5-f7ed-43d3-8982-d95db8bd9150",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b9fbaa-4159-4906-9e7b-5c7c38fdb4da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BLefQCC8JqQzuUcwMV4KPh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1767,
      "cache_read_input_tokens": 32916,
      "output_tokens": 738,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1767,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 738,
          "cache_read_input_tokens": 32916,
          "cache_creation_input_tokens": 1767,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1767
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-10T09:30:48.465Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SwYwSRUxq9pyiAtuYMN9jJ`</summary>

```json
{
  "url": "https://arxiv.org/abs/2508.10511",
  "prompt": "Find the ToolHang ablation numbers for KDPE vs KDPE-OOD. What is the exact success rate for KDPE on ToolHang vs KDPE-OOD on ToolHang? Also confirm the overall RoboMimic/MimicGen results (88.2% vs 85%)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6db4cf5-f7ed-43d3-8982-d95db8bd9150",
  "isSidechain": false,
  "requestId": "req_011Catev6pzNEw6ozH4HEdSD",
  "type": "assistant",
  "uuid": "2f4967c6-0b8a-49ff-98cf-51c4453285a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b9fbaa-4159-4906-9e7b-5c7c38fdb4da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BLefQCC8JqQzuUcwMV4KPh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1767,
      "cache_read_input_tokens": 32916,
      "output_tokens": 738,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1767,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 738,
          "cache_read_input_tokens": 32916,
          "cache_creation_input_tokens": 1767,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1767
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-10T09:30:50.433Z_

<details><summary>↩ Tool result · `toolu_01YcN3br1ZA8Vfg7GGTuy4CP`</summary>

```text
# Latent Policy Barrier: Key Technical Details

Based on the abstract provided, here's what can be extracted:

**(1) Latent Space for OOD Detection:**
The abstract specifies that LPB uses "the latent embeddings of expert demonstrations" to create a barrier. This indicates **observation latent space** (from the base diffusion policy trained on expert visual data), not action latents.

**(2) Runtime vs Pre-execution:**
"At inference time, the dynamics model predicts future latent states and optimizes them to stay within the expert distribution." This is a **runtime correction mechanism**—it actively constrains predictions during execution rather than pre-computing safe trajectories.

**(3) Policy Modification:**
The framework employs "two separate modules: a base diffusion policy solely on expert data, and a dynamics model trained on both expert and suboptimal policy rollout data." The base policy appears **frozen** while the dynamics model guides corrections, though the abstract doesn't explicitly state weight modification.

**(4) Performance Numbers:**
No specific metrics (success rates, error margins, improvement percentages) are included in the abstract.

**(5) Core Mechanism:**
LPB treats expert demonstration embeddings as implicit boundaries separating safe from unsafe states. During inference, a learned dynamics model forecasts future latent positions and optimizes them to remain within the expert distribution, decoupling imitation quality from out-of-distribution recovery.

**Key Differentiator:** Unlike action-latent selection methods, LPB operates in observation latent space and uses dynamics modeling for proactive state constraint rather than retrospective action filtering.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "854b2909-98d3-430b-8dc9-71b6abe3f184",
  "isSidechain": false,
  "promptId": "30743365-00ab-422a-8f74-21081fe9d3c6",
  "type": "user",
  "uuid": "8a4dab00-9d8d-434d-af64-0993d162b6b3",
  "toolUseResult": {
    "bytes": 46001,
    "code": 200,
    "codeText": "OK",
    "result": "# Latent Policy Barrier: Key Technical Details\n\nBased on the abstract provided, here's what can be extracted:\n\n**(1) Latent Space for OOD Detection:**\nThe abstract specifies that LPB uses \"the latent embeddings of expert demonstrations\" to create a barrier. This indicates **observation latent space** (from the base diffusion policy trained on expert visual data), not action latents.\n\n**(2) Runtime vs Pre-execution:**\n\"At inference time, the dynamics model predicts future latent states and optimizes them to stay within the expert distribution.\" This is a **runtime correction mechanism**—it actively constrains predictions during execution rather than pre-computing safe trajectories.\n\n**(3) Policy Modification:**\nThe framework employs \"two separate modules: a base diffusion policy solely on expert data, and a dynamics model trained on both expert and suboptimal policy rollout data.\" The base policy appears **frozen** while the dynamics model guides corrections, though the abstract doesn't explicitly state weight modification.\n\n**(4) Performance Numbers:**\nNo specific metrics (success rates, error margins, improvement percentages) are included in the abstract.\n\n**(5) Core Mechanism:**\nLPB treats expert demonstration embeddings as implicit boundaries separating safe from unsafe states. During inference, a learned dynamics model forecasts future latent positions and optimizes them to remain within the expert distribution, decoupling imitation quality from out-of-distribution recovery.\n\n**Key Differentiator:** Unlike action-latent selection methods, LPB operates in observation latent space and uses dynamics modeling for proactive state constraint rather than retrospective action filtering.",
    "durationMs": 5482,
    "url": "https://arxiv.org/abs/2508.05941"
  },
  "sourceToolAssistantUUID": "854b2909-98d3-430b-8dc9-71b6abe3f184",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b9fbaa-4159-4906-9e7b-5c7c38fdb4da",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-10T09:30:53.303Z_

<details><summary>↩ Tool result · `toolu_01Xhf6KhA4CXYtdkeC4DmNK2`</summary>

```text
Based on the provided arXiv page content, here's what I can extract:

**(1) Latent Space for Value Function:**
Not explicitly specified in the abstract or page content provided.

**(2) Action Representation:**
The paper uses "optical flow as an embodiment-agnostic action representation" rather than joint angles, enabling it to leverage data across different robot embodiments and human demonstrations.

**(3) Rollout Data Requirement:**
Not clearly stated in the available content. The method involves finetuning a world model and training a base policy on target embodiment demonstrations, but whether rollout data is specifically required isn't detailed.

**(4) Key Performance Numbers:**
The paper reports "10.6% on average across four Robomimic tasks" for simulation and significantly stronger real-world results: "70% relative improvement with 30-50 target-embodiment demonstrations, and 44% relative improvement with 60-100 demonstrations."

**(5) Core Mechanism:**
Latent Policy Steering (LPS) pretrains world models on multi-embodiment data using optical flow, then finetunes on target embodiment demonstrations. It subsequently uses the finetuned world model and learned value function to evaluate and select superior actions from a behavior-cloned base policy.

The key differentiator appears to be leveraging embodiment-agnostic optical flow for cross-embodiment pretraining rather than assuming aligned action spaces.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e6db4cf5-f7ed-43d3-8982-d95db8bd9150",
  "isSidechain": false,
  "promptId": "30743365-00ab-422a-8f74-21081fe9d3c6",
  "type": "user",
  "uuid": "6ae130d5-e0d1-4a91-aaca-ed53b7c38169",
  "toolUseResult": {
    "bytes": 46989,
    "code": 200,
    "codeText": "OK",
    "result": "Based on the provided arXiv page content, here's what I can extract:\n\n**(1) Latent Space for Value Function:**\nNot explicitly specified in the abstract or page content provided.\n\n**(2) Action Representation:**\nThe paper uses \"optical flow as an embodiment-agnostic action representation\" rather than joint angles, enabling it to leverage data across different robot embodiments and human demonstrations.\n\n**(3) Rollout Data Requirement:**\nNot clearly stated in the available content. The method involves finetuning a world model and training a base policy on target embodiment demonstrations, but whether rollout data is specifically required isn't detailed.\n\n**(4) Key Performance Numbers:**\nThe paper reports \"10.6% on average across four Robomimic tasks\" for simulation and significantly stronger real-world results: \"70% relative improvement with 30-50 target-embodiment demonstrations, and 44% relative improvement with 60-100 demonstrations.\"\n\n**(5) Core Mechanism:**\nLatent Policy Steering (LPS) pretrains world models on multi-embodiment data using optical flow, then finetunes on target embodiment demonstrations. It subsequently uses the finetuned world model and learned value function to evaluate and select superior actions from a behavior-cloned base policy.\n\nThe key differentiator appears to be leveraging embodiment-agnostic optical flow for cross-embodiment pretraining rather than assuming aligned action spaces.",
    "durationMs": 6443,
    "url": "https://arxiv.org/abs/2507.13340"
  },
  "sourceToolAssistantUUID": "e6db4cf5-f7ed-43d3-8982-d95db8bd9150",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b9fbaa-4159-4906-9e7b-5c7c38fdb4da",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-10T09:31:31.146Z_

<details><summary>↩ Tool result · `toolu_01SwYwSRUxq9pyiAtuYMN9jJ`</summary>

```text
I cannot provide the specific ablation numbers you're requesting. The webpage content provided is only the arXiv abstract page for the paper, which contains the title, author names, and a brief summary. It does not include the actual paper content, results tables, or experimental data comparing KDPE vs KDPE-OOD on ToolHang or the RoboMimic/MimicGen results you mentioned.

To find these specific performance metrics, you would need to access the full PDF or HTML version of the paper using the links provided on the page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2f4967c6-0b8a-49ff-98cf-51c4453285a8",
  "isSidechain": false,
  "promptId": "30743365-00ab-422a-8f74-21081fe9d3c6",
  "type": "user",
  "uuid": "c07af1e8-a17e-4891-b3ed-f2f3e70fe535",
  "toolUseResult": {
    "bytes": 47577,
    "code": 200,
    "codeText": "OK",
    "result": "I cannot provide the specific ablation numbers you're requesting. The webpage content provided is only the arXiv abstract page for the paper, which contains the title, author names, and a brief summary. It does not include the actual paper content, results tables, or experimental data comparing KDPE vs KDPE-OOD on ToolHang or the RoboMimic/MimicGen results you mentioned.\n\nTo find these specific performance metrics, you would need to access the full PDF or HTML version of the paper using the links provided on the page.",
    "durationMs": 42676,
    "url": "https://arxiv.org/abs/2508.10511"
  },
  "sourceToolAssistantUUID": "2f4967c6-0b8a-49ff-98cf-51c4453285a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b9fbaa-4159-4906-9e7b-5c7c38fdb4da",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-10T09:31:33.744Z_

<details><summary>Logged reasoning block</summary>

```text
The abstract pages didn't have the full content. Let me try to fetch the HTML version or PDF for the WAV paper and KDPE paper to get the specific metrics. Let me try fetching the HTML papers directly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c07af1e8-a17e-4891-b3ed-f2f3e70fe535",
  "isSidechain": false,
  "requestId": "req_011Catez2QT216aDNrWR5KhF",
  "type": "assistant",
  "uuid": "bbbe6b4f-fa5b-4be3-813c-519fc28f154d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b9fbaa-4159-4906-9e7b-5c7c38fdb4da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01HNCWZ9FUB9Dfghg3fGQWqs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1801,
      "cache_read_input_tokens": 34683,
      "output_tokens": 639,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1801,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 639,
          "cache_read_input_tokens": 34683,
          "cache_creation_input_tokens": 1801,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1801
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-10T09:31:34.122Z_

The abstract pages didn't have the tables. Let me fetch the full HTML versions of the WAV and KDPE papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bbbe6b4f-fa5b-4be3-813c-519fc28f154d",
  "isSidechain": false,
  "requestId": "req_011Catez2QT216aDNrWR5KhF",
  "type": "assistant",
  "uuid": "9e85a054-c6a4-4afc-899f-f15533d106b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b9fbaa-4159-4906-9e7b-5c7c38fdb4da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01HNCWZ9FUB9Dfghg3fGQWqs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1801,
      "cache_read_input_tokens": 34683,
      "output_tokens": 639,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1801,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 639,
          "cache_read_input_tokens": 34683,
          "cache_creation_input_tokens": 1801,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1801
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-10T09:31:35.042Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01P4BroqXyWkjos2kNTxWFyU`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.14732",
  "prompt": "Find all LIBERO benchmark numbers in Table 1: Spatial, Object, Goal, Long splits for the WAV model. Also find real-world robot results in Figure 2. Report exact success rate percentages."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e85a054-c6a4-4afc-899f-f15533d106b1",
  "isSidechain": false,
  "requestId": "req_011Catez2QT216aDNrWR5KhF",
  "type": "assistant",
  "uuid": "7ef0ab46-002b-4cdf-b29b-c752e5245511",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b9fbaa-4159-4906-9e7b-5c7c38fdb4da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01HNCWZ9FUB9Dfghg3fGQWqs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1801,
      "cache_read_input_tokens": 34683,
      "output_tokens": 639,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1801,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 639,
          "cache_read_input_tokens": 34683,
          "cache_creation_input_tokens": 1801,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1801
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-10T09:31:36.621Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015GBWmxyARHn5vTMQXz2zWe`</summary>

```json
{
  "url": "https://arxiv.org/html/2508.10511",
  "prompt": "Find the ToolHang ablation results comparing KDPE vs KDPE-OOD. Look for any table showing per-task performance on ToolHang. Also report the overall RoboMimic/MimicGen results. Exact percentages needed."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ef0ab46-002b-4cdf-b29b-c752e5245511",
  "isSidechain": false,
  "requestId": "req_011Catez2QT216aDNrWR5KhF",
  "type": "assistant",
  "uuid": "f3faf2a5-f6a5-4d7a-ab96-e6d0f8e7fa04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b9fbaa-4159-4906-9e7b-5c7c38fdb4da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01HNCWZ9FUB9Dfghg3fGQWqs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1801,
      "cache_read_input_tokens": 34683,
      "output_tokens": 639,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1801,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 639,
          "cache_read_input_tokens": 34683,
          "cache_creation_input_tokens": 1801,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1801
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-10T09:31:38.574Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018HogAPU8zqQaemUsU9EoAF`</summary>

```json
{
  "url": "https://arxiv.org/html/2508.05941",
  "prompt": "Extract: (1) what latent space (observation vs action vs world model) is used for OOD detection/barrier, (2) does it use Euclidean distance to nearest neighbor in the expert demo latent space, (3) does it do runtime steering vs pre-execution candidate selection, (4) any key performance numbers. 3-4 sentences summary."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3faf2a5-f6a5-4d7a-ab96-e6d0f8e7fa04",
  "isSidechain": false,
  "requestId": "req_011Catez2QT216aDNrWR5KhF",
  "type": "assistant",
  "uuid": "60fb89c0-e806-46d1-9229-e1c97551e4bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b9fbaa-4159-4906-9e7b-5c7c38fdb4da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01HNCWZ9FUB9Dfghg3fGQWqs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1801,
      "cache_read_input_tokens": 34683,
      "output_tokens": 639,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1801,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 639,
          "cache_read_input_tokens": 34683,
          "cache_creation_input_tokens": 1801,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1801
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-10T09:31:38.642Z_

<details><summary>↩ Tool result · `toolu_01P4BroqXyWkjos2kNTxWFyU`</summary>

```text
# WAV Model Performance Results

## LIBERO Benchmark (Table 1)
The WAV model achieved the following scores across the four LIBERO task suites:

- **Spatial**: 100.0%
- **Object**: 98.6%
- **Goal**: 94.4%
- **Long**: 98.1%
- **Overall Average**: 99.6%

## Real-World Robot Results (Figure 2)
On physical robotic manipulation tasks, the WAV model demonstrated substantially higher performance than the baseline:

- **Average Success Rate**: 75.6% (compared to 35.6% for the GE-ACT baseline)

The results showed consistent improvements across all tested real-world tasks, with the paper noting that "WAV achieved a significantly higher success rate across all tasks than the baseline."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7ef0ab46-002b-4cdf-b29b-c752e5245511",
  "isSidechain": false,
  "promptId": "30743365-00ab-422a-8f74-21081fe9d3c6",
  "type": "user",
  "uuid": "ff3ebfd3-b60f-43c1-bebd-20f755311ef9",
  "toolUseResult": {
    "bytes": 414859,
    "code": 200,
    "codeText": "OK",
    "result": "# WAV Model Performance Results\n\n## LIBERO Benchmark (Table 1)\nThe WAV model achieved the following scores across the four LIBERO task suites:\n\n- **Spatial**: 100.0%\n- **Object**: 98.6%\n- **Goal**: 94.4%\n- **Long**: 98.1%\n- **Overall Average**: 99.6%\n\n## Real-World Robot Results (Figure 2)\nOn physical robotic manipulation tasks, the WAV model demonstrated substantially higher performance than the baseline:\n\n- **Average Success Rate**: 75.6% (compared to 35.6% for the GE-ACT baseline)\n\nThe results showed consistent improvements across all tested real-world tasks, with the paper noting that \"WAV achieved a significantly higher success rate across all tasks than the baseline.\"",
    "durationMs": 3594,
    "url": "https://arxiv.org/html/2604.14732"
  },
  "sourceToolAssistantUUID": "7ef0ab46-002b-4cdf-b29b-c752e5245511",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b9fbaa-4159-4906-9e7b-5c7c38fdb4da",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-10T09:31:39.577Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FeuZ5FCP9hvn6E5F6EEFbc`</summary>

```json
{
  "url": "https://arxiv.org/html/2507.13340",
  "prompt": "Extract: (1) exact latent space used for value function training (world model latent, observation latent, or action latent?), (2) does it use optical flow as action representation?, (3) does it require policy rollout data for training the value function?, (4) performance improvement numbers (70% relative improvement?), (5) does it use a frozen world model or jointly trained? 3-4 sentences."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff3ebfd3-b60f-43c1-bebd-20f755311ef9",
  "isSidechain": false,
  "requestId": "req_011Catez2QT216aDNrWR5KhF",
  "type": "assistant",
  "uuid": "5c0508ed-75a2-4477-8130-448a4e014746",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b9fbaa-4159-4906-9e7b-5c7c38fdb4da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01HNCWZ9FUB9Dfghg3fGQWqs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1801,
      "cache_read_input_tokens": 34683,
      "output_tokens": 639,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1801,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 639,
          "cache_read_input_tokens": 34683,
          "cache_creation_input_tokens": 1801,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1801
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Runtime record

_source line 29_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Latent-Distribution Candidate Selection for Frozen World Action Models…",
  "leafUuid": "5c0508ed-75a2-4477-8130-448a4e014746",
  "sessionId": "f0b9fbaa-4159-4906-9e7b-5c7c38fdb4da"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Frozen WAM candidate selection via action latent OOD scoring",
  "sessionId": "f0b9fbaa-4159-4906-9e7b-5c7c38fdb4da"
}
```

---

### Tool result

_source line 31 · 2026-05-10T09:31:40.258Z_

<details><summary>↩ Tool result · `toolu_015GBWmxyARHn5vTMQXz2zWe`</summary>

```text
# KDPE vs KDPE-OOD Performance on ToolHang

Based on Table 1 in the results section, here are the ToolHang ablation comparisons:

**ToolHang Performance (ph dataset):**
- KDPE-OOD-C: 7.0%
- KDPE-C: 76.0%

**ToolHang Performance (Transformer):**
- KDPE-OOD-T: 2.0%
- KDPE-T: 66.0%

This represents a dramatic performance gap on this precision task, with the standard KDPE approach substantially outperforming the out-of-distribution variant that selects trajectories with minimum density.

## Overall Benchmark Results

**CNN-based Models Average Success Rate:**
- KDPE-C: 88.2%

**Transformer-based Models Average Success Rate:**
- KDPE-T: 81.2%

The paper notes that "KDPE achieves a larger performance improvement w.r.t. DP on precision tasks as ToolHang," demonstrating that trajectory filtering proves particularly valuable for high-precision manipulation requiring careful action selection.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3faf2a5-f6a5-4d7a-ab96-e6d0f8e7fa04",
  "isSidechain": false,
  "promptId": "30743365-00ab-422a-8f74-21081fe9d3c6",
  "type": "user",
  "uuid": "38afe5e6-8f6a-480b-8453-9219b197b2de",
  "toolUseResult": {
    "bytes": 225520,
    "code": 200,
    "codeText": "OK",
    "result": "# KDPE vs KDPE-OOD Performance on ToolHang\n\nBased on Table 1 in the results section, here are the ToolHang ablation comparisons:\n\n**ToolHang Performance (ph dataset):**\n- KDPE-OOD-C: 7.0%\n- KDPE-C: 76.0%\n\n**ToolHang Performance (Transformer):**\n- KDPE-OOD-T: 2.0%\n- KDPE-T: 66.0%\n\nThis represents a dramatic performance gap on this precision task, with the standard KDPE approach substantially outperforming the out-of-distribution variant that selects trajectories with minimum density.\n\n## Overall Benchmark Results\n\n**CNN-based Models Average Success Rate:**\n- KDPE-C: 88.2%\n\n**Transformer-based Models Average Success Rate:**\n- KDPE-T: 81.2%\n\nThe paper notes that \"KDPE achieves a larger performance improvement w.r.t. DP on precision tasks as ToolHang,\" demonstrating that trajectory filtering proves particularly valuable for high-precision manipulation requiring careful action selection.",
    "durationMs": 3635,
    "url": "https://arxiv.org/html/2508.10511"
  },
  "sourceToolAssistantUUID": "f3faf2a5-f6a5-4d7a-ab96-e6d0f8e7fa04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b9fbaa-4159-4906-9e7b-5c7c38fdb4da",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-10T09:31:44.494Z_

<details><summary>↩ Tool result · `toolu_018HogAPU8zqQaemUsU9EoAF`</summary>

```text
# Latent Policy Barrier: Key Technical Details

**(1) Latent Space for OOD Detection:**
The method uses the **observation latent space** from the base diffusion policy's visual encoder. The paper states: "we encode it into a latent representation z=hθ(o) using the frozen visual encoder hθ from the base policy."

**(2) Distance Metric:**
Yes, it employs Euclidean distance to nearest neighbors in expert demonstration space. The latent OOD score is defined as: "δ(z)=‖z−zNN‖²₂" where zNN is "the nearest neighbor of z in the expert latent space."

**(3) Runtime Steering Approach:**
It performs **runtime steering during action denoising**, not pre-execution selection. During the final denoising steps when out-of-distribution states are detected (δ(z)>τ), the method "take[s] the gradient of latent OOD score of predicted future latent state through the dynamics model and use[s] this gradient to refine the action denoising process."

**(4) Key Performance Numbers:**
On simulated tasks with 20% expert demonstrations, LPB achieves: Transport (0.85 success), Tool-Hang (0.39), Push-T (0.65). On real robots, it improves Cup Arrangement from baseline performance to matching on in-distribution poses while substantially outperforming on out-of-distribution scenarios; Belt Assembly improves from 0.55 to 0.75 success rate.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "60fb89c0-e806-46d1-9229-e1c97551e4bd",
  "isSidechain": false,
  "promptId": "30743365-00ab-422a-8f74-21081fe9d3c6",
  "type": "user",
  "uuid": "dcefe34e-5bbf-41fc-86fd-13c844151557",
  "toolUseResult": {
    "bytes": 217506,
    "code": 200,
    "codeText": "OK",
    "result": "# Latent Policy Barrier: Key Technical Details\n\n**(1) Latent Space for OOD Detection:**\nThe method uses the **observation latent space** from the base diffusion policy's visual encoder. The paper states: \"we encode it into a latent representation z=hθ(o) using the frozen visual encoder hθ from the base policy.\"\n\n**(2) Distance Metric:**\nYes, it employs Euclidean distance to nearest neighbors in expert demonstration space. The latent OOD score is defined as: \"δ(z)=‖z−zNN‖²₂\" where zNN is \"the nearest neighbor of z in the expert latent space.\"\n\n**(3) Runtime Steering Approach:**\nIt performs **runtime steering during action denoising**, not pre-execution selection. During the final denoising steps when out-of-distribution states are detected (δ(z)>τ), the method \"take[s] the gradient of latent OOD score of predicted future latent state through the dynamics model and use[s] this gradient to refine the action denoising process.\"\n\n**(4) Key Performance Numbers:**\nOn simulated tasks with 20% expert demonstrations, LPB achieves: Transport (0.85 success), Tool-Hang (0.39), Push-T (0.65). On real robots, it improves Cup Arrangement from baseline performance to matching on in-distribution poses while substantially outperforming on out-of-distribution scenarios; Belt Assembly improves from 0.55 to 0.75 success rate.",
    "durationMs": 5918,
    "url": "https://arxiv.org/html/2508.05941"
  },
  "sourceToolAssistantUUID": "60fb89c0-e806-46d1-9229-e1c97551e4bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b9fbaa-4159-4906-9e7b-5c7c38fdb4da",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-10T09:31:44.986Z_

<details><summary>↩ Tool result · `toolu_01FeuZ5FCP9hvn6E5F6EEFbc`</summary>

```text
# Latent Policy Steering: Key Technical Details

**(1) Latent Space:** The value function operates in the "world model's latent state space," leveraging representations from the Dreamer v3 architecture where the WM encoder maps observations to latent states.

**(2) Optical Flow Action Representation:** Yes. The method uses "optical flow as an embodiment-agnostic action representation" during pretraining, then switches to normalized robot actions during target embodiment finetuning.

**(3) Policy Rollout Data:** Yes. Algorithm 1 shows the value function trains on both expert demonstration states and "a predicted action plan" sampled from the base policy, enabling it to "see" distribution-shifted states before inference.

**(4) Performance Gains:** Real-world experiments achieved "70% relative improvement with 30-50 target-embodiment demonstrations, and 44% relative improvement with 60-100 demonstrations." Simulated benchmarks showed 10.6% average improvement across four Robomimic tasks.

**(5) World Model Training:** The WM is jointly trained with the value function during target finetuning—"the value function leverages the latent state representation from the WM, but its gradients do not flow back into the WM," keeping the pretrained dynamics frozen while only updating the value estimator.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5c0508ed-75a2-4477-8130-448a4e014746",
  "isSidechain": false,
  "promptId": "30743365-00ab-422a-8f74-21081fe9d3c6",
  "type": "user",
  "uuid": "5d40d6a9-f295-47c4-b64f-dc94aa480d85",
  "toolUseResult": {
    "bytes": 210073,
    "code": 200,
    "codeText": "OK",
    "result": "# Latent Policy Steering: Key Technical Details\n\n**(1) Latent Space:** The value function operates in the \"world model's latent state space,\" leveraging representations from the Dreamer v3 architecture where the WM encoder maps observations to latent states.\n\n**(2) Optical Flow Action Representation:** Yes. The method uses \"optical flow as an embodiment-agnostic action representation\" during pretraining, then switches to normalized robot actions during target embodiment finetuning.\n\n**(3) Policy Rollout Data:** Yes. Algorithm 1 shows the value function trains on both expert demonstration states and \"a predicted action plan\" sampled from the base policy, enabling it to \"see\" distribution-shifted states before inference.\n\n**(4) Performance Gains:** Real-world experiments achieved \"70% relative improvement with 30-50 target-embodiment demonstrations, and 44% relative improvement with 60-100 demonstrations.\" Simulated benchmarks showed 10.6% average improvement across four Robomimic tasks.\n\n**(5) World Model Training:** The WM is jointly trained with the value function during target finetuning—\"the value function leverages the latent state representation from the WM, but its gradients do not flow back into the WM,\" keeping the pretrained dynamics frozen while only updating the value estimator.",
    "durationMs": 5406,
    "url": "https://arxiv.org/html/2507.13340"
  },
  "sourceToolAssistantUUID": "5c0508ed-75a2-4477-8130-448a4e014746",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b9fbaa-4159-4906-9e7b-5c7c38fdb4da",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 34 · 2026-05-10T09:31:44.990Z_

```json
{
  "parentUuid": "5d40d6a9-f295-47c4-b64f-dc94aa480d85",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "53b3b83b-d941-4d83-af0c-88973d8aacc2",
  "timestamp": "2026-05-10T09:31:44.990Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b9fbaa-4159-4906-9e7b-5c7c38fdb4da",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 35 · 2026-05-10T09:34:15.780Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the key information I need:

**WAV Metrics (from HTML paper):**
- Spatial: 100.0%
- Object: 98.6%
- Goal: 94.4%
- Long: 98.1%
- Overall Average: 99.6% (NOT ~97.8% as the reviewer suggested)

Wait - this is interesting. The WAV HTML paper says the overall average IS 99.6%. But the reviewer said "averaging ~97.8%, not 99.6%." Let me check: (100.0 + 98.6 + 94.4 + 98.1) / 4 = 391.1 / 4 = 97.775% ≈ 97.8%.


So the raw arithmetic average of the four LIBERO splits is 97.8%, but the paper reports 99.6% as the overall average—this discrepancy suggests they might be weighting by task count or calculating across all tasks rather than averaging the split averages. Looking at LIBERO's structure, each suite has different numbers of tasks, so a task-level success rate would produce different weighting than a simple split average.

The paper itself reports 99.6% overall, while the reviewer's calculation of 97.8% comes from averaging the four split percentages directly. If LIBERO-Goal is at 94.4% and the others range from 98-100%, the arithmetic mean would be around 97.8%, yet the paper shows 99.6%—which suggests they're either computing the metric differently, weighting by episode count, or using a different aggregation method entirely. The WAV paper itself reports 99.6% as the overall average, which matches the original claim, so the reviewer's arithmetic of 97.8% appears to be incorrect or based on a different calculation method. Since the paper explicitly states 99.6% in Table 1 alongside the individual split scores, that's the authoritative number to use. I'm realizing the discrepancy might stem from how the averages are computed—WAV's 99.6% could be a weighted average across all individual tasks rather than a simple arithmetic mean of the four split percentages, especially if LIBERO-Long's tasks have different difficulty distributions that affect the overall calculation. The reviewer's manual averaging of 97.8% assumes equal weighting across splits, but that may not reflect how WAV actually computed their reported figure. ~97.8%, not 99.6%." The reviewer is doing simple arithmetic: (100+98.6+94.4+98.1)/4 = 97.775%.

But the paper's own reported overall average is 99.6%. This doesn't add up unless:
1. The 99.6% doesn't include LIBERO-Goal (94.4%) - i.e., it's averaging only Spatial, Object, Long: (100+98.6+98.1)/3 = 99.567% ≈ 99.6%!

That's it! The WAV paper might be reporting a 3-split "LIBERO overall" (Spatial, Object, Long) of 99.6%, while also reporting LIBERO-Goal separately at 94.4%. This is consistent with the original idea which notes "WAV's LIBERO evaluation covers 4 benchmark splits but does not include LIBERO-90."

Now I'm recalling the full LIBERO structure: there are five distinct benchmarks—Spatial, Object, Goal, and Long each with 10 tasks, plus LIBERO-90 with 90 tasks total. Different papers compute their "overall" averages in different ways, so if WAV's 99.6% figure excludes the Goal split at 94.4%, that would explain the discrepancy with the reviewer's calculation. I'm working through the math on how WAV might be calculating that 99.6% overall average—it doesn't match a simple average of all four splits, so either they're only averaging three of them (Spatial, Object, Long) or weighting the episodes differently across tasks. The most plausible explanation is that they're excluding the Goal split or computing the overall differently than I initially assumed. The WAV paper itself reports 99.6% as the official overall average, so the discrepancy with the simple arithmetic mean of 97.8% suggests WAV is computing this metric differently—perhaps across individual task episodes rather than just averaging the four split-level numbers. I should accept what the paper claims while acknowledging this methodological difference to address the reviewer's concern. The paper actually reports both numbers in Table 1: the four individual split accuracies and a 99.6% overall average, likely computed as a micro-average across all episodes rather than a simple macro-average of the splits. So the reviewer's concern about 99.6% being incorrect stems from calculating it differently—they're averaging the four splits arithmetically to get ~97.8%, but the paper uses a different weighting method that yields 99.6%.

The right approach is to report what the paper explicitly states (99.6% as the overall average) while also including the individual split numbers, and I can note that the simple average of those splits comes to around 97.8% if that distinction matters for clarity. I'm realizing the WAV paper might have a separate evaluation methodology that produces that 99.6% figure—perhaps using different success criteria or additional benchmarks like LIBERO-10. Since I can't verify this without the full paper, I should stick with the four split numbers I can confirm and compute their arithmetic mean: (100.0 + 98.6 + 94.4 + 98.1) / 4 = 97.8%. I'll report the individual splits as verified and either use this computed average or note the discrepancy rather than claiming the 99.6% without confirmation. so the reviewer is right about the arithmetic. The question is whether WAV actually reports 99.6% or whether that number is an error.

Let me take another approach and think about LIBERO: the standard LIBERO benchmark has 4 suites (Spatial, Object, Goal, Long) each with 10 tasks and 50 episodes per task. Total = 2000 episodes. The "overall" success rate would be the count of successes across all 2000 episodes divided by 2000. If the distribution of success within each split is very skewed (many tasks at 100% and a few at much lower rates pulling the average down), the split-level average could be 97.8% while the overall might be different... but actually across the same 2000 episodes, the micro-average equals the macro-average since all splits have equal size.

So 99.6% overall from (100.0 + 98.6 + 94.4 + 98.1)/4 = 97.8% doesn't add up unless the overall is calculated differently—maybe it excludes one of the splits, or the splits have unequal weighting. Let me check if dropping the Goal split or using different weights could produce 99.6%, but none of the combinations I'm testing seem to match. The individual task numbers within LIBERO-Long might be higher than the suite average suggests, but that doesn't resolve the discrepancy. Given the reviewer's repeated flagging and independent verification of the split scores (Spatial 100.0%, Object 98.6%, Goal 94.4%, Long 98.1%), I should trust their arithmetic: the correct overall average is ~97.8%, not 99.6%. The 99.6% figure might be from a different metric or calculation, so I'll report the verified individual splits and use 97.8% as the overall average as the reviewer instructed. I'm realizing the core issue: the WAV paper itself reports 99.6% as an overall average in Table 1, which is a legitimate number they calculated—likely using a different methodology than a simple arithmetic mean of the four splits. The reviewer is correct that averaging the four split percentages arithmetically gives ~97.8%, but that doesn't mean the paper's 99.6% figure is wrong, just that it's computed differently. I can report both numbers accurately: the individual splits and the paper's stated overall average. Looking at how other papers report LIBERO results, there's a consistent pattern: when individual splits are in the 95-100% range, averaging them gives something like 97-98%, not 99.6%. The discrepancy suggests WAV might be including an additional suite or using different normalization. Since the reviewer explicitly verified the numbers, I should just accept their determination and update the claims accordingly.

I'll revise the WAV metrics to show the individual split results—100.0% Spatial, 98.6% Object, 94.4% Goal, 98.1% Long—with the correct ~97.8% average, since that's what the arithmetic actually yields. The 99.6% figure in the current submission appears to be the error.

Now I need to check the LPS results from the arXiv paper.  The reviewer mentions "+50% relative improvement" but the actual paper reports 70% relative improvement with 30-50 target-embodiment demos, so I'll use the 70% figure instead.

Let me outline the JSON updates: I need to fix the WAV metrics across the landscape and key_references sections by replacing the incorrect 99.6% overall average with the individual split percentages and correct average. I also need to add the Latent Policy Barrier method, which uses Euclidean distance in the visual observation latent space.

Continuing with the additions: Latent Policy Steering uses a value function in the world model latent space with optical flow as the action representation, achieving that 70% relative improvement on real-world tasks with 30-50 demos. I'll need to integrate both of these new methods into the landscape, core_problem, opportunity, and key_references sections.

I should also strengthen the KDPE-OOD citation by adding the specific ToolHang numbers showing the performance gap, and include Being-H0.7 as a concurrent result achieving 99.2% on LIBERO. Since these are mostly citation additions and metric corrections rather than fundamental changes to the framing, this is a relatively contained revision. I've got the metrics for Being-H0.7 now — 99.2% on LIBERO with concurrent WAM. Now I'll write out the complete updated JSON, making sure to revise all the relevant sections consistently with these new details.

For the key_references section, I'm replacing the WAV entry to break down the LIBERO results by split (Spatial 100.0%, Object 98.6%, Goal 94.4%, Long 98.1%) and clarify that our method keeps all WAM weights frozen while remaining plug-in-compatible with any pretrained WAM.

In the landscape section, I need to condense the WAV description to focus on its core characteristics — a trajectory value module that requires training from scratch as a new architectural component, with iterative latent-space inference. Looking at the LIBERO breakdown across all four splits—Spatial, Object, Goal, and Long—with that ~97.8% average, and noting the 75.6% real-world performance on the dual-arm Piper setup. The key distinction is that WAV requires joint training of value and world model from the ground up, whereas our approach keeps the pretrained world model frozen and works as a plug-in module.

Now I need to integrate LPB and LPS into the landscape, core problem, and references. LPB differs from LOC in that it operates on the visual encoder's latent space with runtime gradient-based steering when out-of-distribution, while LOC uses the action latent space with pre-execution candidate selection and no dynamics model. LPS operates in the world model's state latent space, distinct from the value MLP approach.

I should also note KDPE's dramatic performance collapse on ToolHang when selecting the most out-of-distribution trajectory, and mention Being-H0.7 as a concurrent WAM baseline achieving 99.2% on LIBERO-combined. I need to systematically update the JSON fields. The core issue is fixing WAV's metrics in the landscape section—it currently claims 99.6% LIBERO overall average, but I should replace that with individual split performance around 97.8% average. I also need to strengthen the KDPE-OOD citation by adding ToolHang numbers and ensure LPB and LPS are mentioned in related work. Let me work through each field methodically to keep the changes targeted and minimal. I need to clarify the literature context by explaining how LPB and LPS relate to but don't directly address the same research questions, then integrate the specific ToolHang metrics (KDPE-OOD-C: 7% vs KDPE-C: 76%) into both the core problem and opportunity sections to strengthen the empirical grounding, and finally correct the WAV verification numbers in the landscape section. Writing the corrected JSON with updated metrics and new model references...

The WAV discrepancy might stem from how the paper weights the splits—though with equal task counts across LIBERO splits, a simple average should match. Let me verify the math: even if I calculate the weighted average across all episodes, the result stays consistent, so the 99.6% figure likely refers to a different aggregation method or metric definition than what I'm seeing in the individual split breakdowns.

I'll go with reporting the four split numbers explicitly and dropping the 99.6% overall claim, since the arithmetic doesn't support it as a straightforward average. This addresses the reviewer's concern directly and is more transparent than relying on a potentially different calculation method from the original paper.

Now I'm finalizing the JSON with my decisions: WAV gets the four individual split percentages without an overall average, KDPE-OOD needs ToolHang comparisons added throughout, and for LPB I'm documenting the Euclidean distance mechanism in the visual latent space.

For LPS, the key differentiator is using a world model latent state space with optical flow rather than action latents, plus it requires policy-rollout data and shows modest simulation gains. Being-H0.7 achieves 99.2% on LIBERO using concurrent WAM...

Now I'm organizing this comparison into a structured JSON format to capture all the mechanisms, performance metrics, and differentiators across these approaches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53b3b83b-d941-4d83-af0c-88973d8aacc2",
  "isSidechain": false,
  "requestId": "req_011Catf13iMYsMDMRw1D9wkA",
  "type": "assistant",
  "uuid": "bc3edb5a-1b9c-4fc1-bd0e-5a35b60eaadb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b9fbaa-4159-4906-9e7b-5c7c38fdb4da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01NBiC3yBYA1n3FiLqzPqghU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1962,
      "cache_read_input_tokens": 36484,
      "output_tokens": 10296,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1962,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10296,
          "cache_read_input_tokens": 36484,
          "cache_creation_input_tokens": 1962,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1962
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-10T09:34:18.022Z_

Good. Now I have all the data I need:
- **WAV**: Paper HTML confirms Spatial 100.0%, Object 98.6%, Goal 94.4%, Long 98.1% — arithmetic average is **97.8%**, not 99.6%. (The paper may have an "Overall" row computed differently, but the reviewer correctly identifies the arithmetic inconsistency.)
- **KDPE ToolHang**: KDPE-OOD-C: **7%** vs KDPE-C: **76%** (CNN models) — a dramatic gap
- **LPB**: Euclidean distance to nearest expert demo in **observation latent space** (frozen visual encoder), gradient-based **runtime steering** during denoising, separate dynamics model trained on expert + suboptimal rollout data
- **LPS**: Value function in **world model latent state space** (Dreamer v3), **optical flow** action representation, requires **policy rollout data**, 70% relative improvement with 30–50 demos

Now I'll apply all four targeted fixes and output the complete revised JSON.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc3edb5a-1b9c-4fc1-bd0e-5a35b60eaadb",
  "isSidechain": false,
  "requestId": "req_011Catf13iMYsMDMRw1D9wkA",
  "type": "assistant",
  "uuid": "1e8a8833-af4a-4996-ad3e-ba5c9bbae84b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b9fbaa-4159-4906-9e7b-5c7c38fdb4da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01NBiC3yBYA1n3FiLqzPqghU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1962,
      "cache_read_input_tokens": 36484,
      "output_tokens": 10296,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1962,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10296,
          "cache_read_input_tokens": 36484,
          "cache_creation_input_tokens": 1962,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1962
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-10T09:34:18.308Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Dzv9TQwgkATeaqfM5bqS6p`</summary>

```json
{
  "query": "Being-H0.7 arXiv 2605.00078 LIBERO results 99.2% world action model 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e8a8833-af4a-4996-ad3e-ba5c9bbae84b",
  "isSidechain": false,
  "requestId": "req_011Catf13iMYsMDMRw1D9wkA",
  "type": "assistant",
  "uuid": "0cbbde74-29eb-4da9-87e5-378211fd7eaf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b9fbaa-4159-4906-9e7b-5c7c38fdb4da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01NBiC3yBYA1n3FiLqzPqghU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1962,
      "cache_read_input_tokens": 36484,
      "output_tokens": 10296,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1962,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10296,
          "cache_read_input_tokens": 36484,
          "cache_creation_input_tokens": 1962,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1962
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Runtime record

_source line 38_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Latent-Distribution Candidate Selection for Frozen World Action Models…",
  "leafUuid": "0cbbde74-29eb-4da9-87e5-378211fd7eaf",
  "sessionId": "f0b9fbaa-4159-4906-9e7b-5c7c38fdb4da"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "ai-title",
  "aiTitle": "Frozen WAM candidate selection via action latent OOD scoring",
  "sessionId": "f0b9fbaa-4159-4906-9e7b-5c7c38fdb4da"
}
```

---

### Tool result

_source line 40 · 2026-05-10T09:34:23.237Z_

<details><summary>↩ Tool result · `toolu_01Dzv9TQwgkATeaqfM5bqS6p`</summary>

```text
Web search results for query: "Being-H0.7 arXiv 2605.00078 LIBERO results 99.2% world action model 2026"

Links: [{"title":"Being-H0.7: A Latent World-Action Model from Egocentric Videos","url":"https://arxiv.org/html/2605.00078v1"},{"title":"Being-H0.5: Scaling Human-Centric Robot Learning for Cross-Embodiment Generalization","url":"https://arxiv.org/html/2601.12993v1"},{"title":"GitHub - BeingBeyond/Being-H: Being-H is BeingBeyond's family of human-centric embodied foundation models. · GitHub","url":"https://github.com/BeingBeyond/Being-H"},{"title":"[2601.12993] Being-H0.5: Scaling Human-Centric Robot Learning for Cross-Embodiment Generalization","url":"https://arxiv.org/abs/2601.12993"},{"title":"Being-H0: Vision-Language-Action Pretraining from Large-Scale Human Videos","url":"https://arxiv.org/html/2507.15597v1"},{"title":"Being-H0.5: Scaling Human-Centric Robot Learning for Cross ...","url":"https://research.beingbeyond.com/being-h05"},{"title":"Being-H0","url":"https://beingbeyond.github.io/Being-H0/"},{"title":"[2507.15597] Being-H0: Vision-Language-Action Pretraining from Large-Scale Human Videos","url":"https://arxiv.org/abs/2507.15597"},{"title":"From Pixels to Tokens: A Systematic Study of Latent Action Supervision for Vision-Language-Action Models","url":"https://arxiv.org/html/2605.04678v1"},{"title":"VeriFence: Lightweight and Precise Spectre Defenses for ...","url":"https://arxiv.org/pdf/2405.00078"}]

Based on the search results, I found information about Being-H0.7 and its performance on LIBERO:

On LIBERO, Being-H0.7 reaches a 99.2% average success rate, with strong performance across all suites.

Being-H0.7 is BeingBeyond's flagship WAM (World-Action Model) model. It builds a Latent World-Action Model that differs from VLAs and WAMs, introducing a latent reasoning space via a set of latent queries in the prior branch, further endowed with world modeling by the joint alignment with a future-aware posterior branch.

Pretrained on large-scale egocentric videos, Being-H0.7 achieves strong performance across diverse robot tasks. The paper was published on arXiv as 2605.00078 on April 30, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0cbbde74-29eb-4da9-87e5-378211fd7eaf",
  "isSidechain": false,
  "promptId": "30743365-00ab-422a-8f74-21081fe9d3c6",
  "type": "user",
  "uuid": "b634d299-8f19-4e39-bc1e-d0d48930b965",
  "toolUseResult": {
    "query": "Being-H0.7 arXiv 2605.00078 LIBERO results 99.2% world action model 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Ht75fpgLyWHjfi2x6mggQb",
        "content": [
          {
            "title": "Being-H0.7: A Latent World-Action Model from Egocentric Videos",
            "url": "https://arxiv.org/html/2605.00078v1"
          },
          {
            "title": "Being-H0.5: Scaling Human-Centric Robot Learning for Cross-Embodiment Generalization",
            "url": "https://arxiv.org/html/2601.12993v1"
          },
          {
            "title": "GitHub - BeingBeyond/Being-H: Being-H is BeingBeyond's family of human-centric embodied foundation models. · GitHub",
            "url": "https://github.com/BeingBeyond/Being-H"
          },
          {
            "title": "[2601.12993] Being-H0.5: Scaling Human-Centric Robot Learning for Cross-Embodiment Generalization",
            "url": "https://arxiv.org/abs/2601.12993"
          },
          {
            "title": "Being-H0: Vision-Language-Action Pretraining from Large-Scale Human Videos",
            "url": "https://arxiv.org/html/2507.15597v1"
          },
          {
            "title": "Being-H0.5: Scaling Human-Centric Robot Learning for Cross ...",
            "url": "https://research.beingbeyond.com/being-h05"
          },
          {
            "title": "Being-H0",
            "url": "https://beingbeyond.github.io/Being-H0/"
          },
          {
            "title": "[2507.15597] Being-H0: Vision-Language-Action Pretraining from Large-Scale Human Videos",
            "url": "https://arxiv.org/abs/2507.15597"
          },
          {
            "title": "From Pixels to Tokens: A Systematic Study of Latent Action Supervision for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2605.04678v1"
          },
          {
            "title": "VeriFence: Lightweight and Precise Spectre Defenses for ...",
            "url": "https://arxiv.org/pdf/2405.00078"
          }
        ]
      },
      "Based on the search results, I found information about Being-H0.7 and its performance on LIBERO:\n\nOn LIBERO, Being-H0.7 reaches a 99.2% average success rate, with strong performance across all suites.\n\nBeing-H0.7 is BeingBeyond's flagship WAM (World-Action Model) model. It builds a Latent World-Action Model that differs from VLAs and WAMs, introducing a latent reasoning space via a set of latent queries in the prior branch, further endowed with world modeling by the joint alignment with a future-aware posterior branch.\n\nPretrained on large-scale egocentric videos, Being-H0.7 achieves strong performance across diverse robot tasks. The paper was published on arXiv as 2605.00078 on April 30, 2026."
    ],
    "durationSeconds": 4.913439400000003
  },
  "sourceToolAssistantUUID": "0cbbde74-29eb-4da9-87e5-378211fd7eaf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b9fbaa-4159-4906-9e7b-5c7c38fdb4da",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-10T09:34:34.793Z_

<details><summary>Logged reasoning block</summary>

```text
Good. Being-H0.7 achieves 99.2% on LIBERO - confirmed. Now let me write the complete updated JSON.

Let me structure all the changes:

**Section updates needed:**

1. **core_problem** - fix WAV metrics (remove 99.6%), add ToolHang numbers to KDPE-OOD, add brief mention of LPB and LPS in the literature gap paragraph

2. **opportunity** - add ToolHang numbers to KDPE section, add LPB/LPS differentiations


3. **landscape** - fix WAV metrics, add LPB, LPS, Being-H0.7 entries
4. **approach** - LPB/LPS mentioned as additional related work baselines? Maybe just a brief note.
5. **key_references** - fix WAV, add LPB, LPS, Being-H0.7
6. **description** - fix WAV metrics

Now I'm going through the JSON systematically to make these updates, starting with correcting the WAV metrics in the description field and ensuring all the new model entries are properly integrated throughout.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b634d299-8f19-4e39-bc1e-d0d48930b965",
  "isSidechain": false,
  "requestId": "req_011CatfCi9CwFWV3HsAXPvbd",
  "type": "assistant",
  "uuid": "45acbc0f-40a5-412d-bc0a-788de755dbd8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b9fbaa-4159-4906-9e7b-5c7c38fdb4da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_016P45ZyjTvLEcfNbk7z6jQD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11016,
      "cache_read_input_tokens": 38446,
      "output_tokens": 16394,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11016,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 16394,
          "cache_read_input_tokens": 38446,
          "cache_creation_input_tokens": 11016,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11016
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-10T09:40:02.171Z_

Confirmed: Being-H0.7 achieves 99.2% on LIBERO average. Now I have all I need to write the complete corrected JSON.

```json
{
  "title": "Latent-Distribution Candidate Selection for Frozen World Action Models: OOD Consistency Scoring and Action-Latent Value Learning",
  "change_type": "minor",
  "core_problem": "Pretrained WAMs generate a single action trajectory at inference and provide no mechanism to compare candidate futures. Adding planning capability currently requires one of three costly interventions: (1) full fine-tuning of the video model on robot demos (Cosmos Policy, ICLR 2026: 384–3,072 H100-hours); (2) training a separate action-conditioned world model alongside the frozen policy (GPC, RAL 2025); or (3) architectural co-design or RL loops (H-WM, GigaBrain RAMP, WAV). Fast-WAM (arXiv 2603.16666) demonstrates that action-only inference achieves 97.6% on LIBERO (Table 2) and 91.8% on RoboTwin (Table 1) at 190ms, motivating candidate generation from frozen WAM action-only inference rather than expensive video rollouts.\n\nThe test-time candidate selection literature (2024–2026) has established three tiers of action representation for scoring candidates, with each tier providing increasingly structured quality-discriminative geometry:\n\n**Tier 1 — Cartesian action space**: V-GPS (arXiv 2410.13816, CoRL 2024) trains a Q-function via offline RL (Cal-QL) on raw 7-dimensional Cartesian action vectors concatenated with ResNet-34 image embeddings, scoring K=50 candidates from frozen generalist policies (Octo, RT-1X, OpenVLA) and achieving +82.8% relative improvement on real-robot tasks — establishing that value-function re-ranking of frozen policies works in Cartesian+image space. KDPE (arXiv 2508.10511, CoRL 2025) applies kernel density estimation to Cartesian action trajectories (end-effector position, SO(3)-orientation, gripper state) from Diffusion Policy to filter multimodal outputs, generating N=100 candidates; achieves 88.2% vs. 85% on RoboMimic/MimicGen. Critical KDPE finding: KDPE-OOD (selecting the most out-of-distribution trajectory) performs dramatically worse than KDPE on the ToolHang precision task (KDPE-OOD-C: 7% vs. KDPE-C: 76%, Table 1) — confirming that in-distribution selection is the correct direction for LOC. Both Tier 1 methods operate on low-dimensional raw action representations with no latent structure encoding physical plausibility beyond what is captured by pixel-level image embeddings.\n\n**Tier 2 — VLA action tokens**: MG-Select (arXiv 2510.05681, ICLR 2026) uses KL-divergence from a masked unconditional VLA distribution as a training-free confidence signal, achieving 168% relative improvement on RoboCasa pick-and-place. RoVer (arXiv 2510.10975, ICLR 2026) trains a 0.2B Process Reward Model that scores candidates from frozen VLAs. Both operate on VLA action tokens from architectures trained on language-action pairs without joint video-action pretraining, lacking the video-physics co-regularization that structures WAM action latents.\n\n**Adjacent latent-space methods (not candidate selection)**: Latent Policy Barrier (LPB, arXiv 2508.05941, 2025) measures Euclidean distance in visual observation latent space (frozen visual encoder from base diffusion policy) to the nearest expert demo state as an OOD signal, then performs gradient-based steering of the action denoising process at runtime when OOD is detected — using a separate dynamics model trained on expert plus suboptimal rollout data. Latent Policy Steering (LPS, arXiv 2507.13340, 2025) trains a value function in world model latent state space (Dreamer v3) on expert plus policy-rollout states, using optical flow as an embodiment-agnostic action representation, achieving 70% relative improvement with 30–50 demos on real-world tasks. Neither approach answers the question we ask: do WAM action latents z_a, shaped by joint video-action pretraining, enable pre-execution candidate scoring without rollout data or observation-space engineering?\n\n**Tier 3 — WAM action latents** (this paper's domain): UWM and DreamZero generate action latents z_a from joint video-action diffusion pretraining. Cosmos Policy (ICLR 2026) implements Best-of-N in its planning mode by generating B candidates and scoring each via a fine-tuned value function — but requires rollout fine-tuning (1,536 H100-hours for RoboCasa) because demonstration-only training 'cannot correctly predict failure states.'\n\nThe central unanswered question — which Tier 1 and Tier 2 approaches cannot answer, and which LPB/LPS do not address — is: (1) Do WAM action latents z_a, regularized by joint video-action pretraining, form a latent success distribution that is more structured and separable from failure regimes than VLA action tokens (Tier 2) or Cartesian action representations (Tier 1), enabling lightweight OOD-based candidate scoring without any rollout data? (2) Does operating in WAM latent space alone (without needing an image at inference) enable a more compact, efficient quality discriminator than Tier 1 methods that require both image and action? These questions are grounded in the FAIL-Detect (arXiv 2503.08558, RSS 2025) finding that OOD detection on success-only demonstrations reliably identifies failures — but have not been applied to WAM action latents or to pre-execution candidate selection.\n\nImportant caveat on z_a geometry: In action-only inference (video timestep = T), video tokens are at full noise and provide no inference-time conditioning. The quality-discriminative structure of z_a is therefore a training-time property — joint pretraining causes the model to learn representations where z_a co-varies with visual futures, but whether this geometry persists as a success/failure discriminator when video is absent at inference is not proven a priori. Step 1 (LOC diagnostic) is the first empirical test. If H1 fails (AUC < 0.55), LOC reports a negative result and Value MLP becomes the sole primary contribution.\n\nThe companion question of whether video denoising error (as opposed to latent OOD scoring) is a reliable zero-training signal is answered negatively by Cosmos Policy's own finding and by EVA (arXiv 2603.17808), which demonstrates an 'executability gap' showing that visual coherence does not predict task success.\n\nNo existing work demonstrates Best-of-N candidate selection using WAM action latents' distributional structure — either zero-training (OOD scoring) or lightweight-trained (value MLP) — without modifying any WAM weights or requiring rollout data for the zero-training path. The three-tier hierarchy predicts that z_a offers the richest quality-discriminative geometry for frozen-policy candidate selection, a hypothesis this paper tests empirically.",
  "opportunity": "UWM's independent per-modality diffusion timestep architecture (RSS 2025) natively supports action-only inference (video timestep = T, action timestep = 0), producing action latents z_a jointly pretrained with video. This creates two complementary WAM-specific approaches to candidate selection:\n\n**Method 1 — Latent OOD Consistency Scoring (LOC, zero weight updates)**: Encode LIBERO-90 success demonstrations through frozen UWM in action-only mode to obtain a reference distribution {z_a^success}. Fit a lightweight density estimator — KNN-based nonconformity score (k=10) or Gaussian Mixture Model (k≤5 components) — on {z_a^success}. At inference, sample B=4–8 action-only candidates from frozen UWM, obtain latents {z_{a,1}, ..., z_{a,B}}, and score each: S_LOC(z_{a,i}) = −log p̂(z_{a,i}) (nonconformity score). Select a_{i*} = argmin_i S_LOC(z_{a,i}) (most in-distribution candidate). Total inference overhead: B × ~5ms = 20–40ms for B=4–8. Cost: ~30–60 minutes to fit density estimator on encoded latents; no WAM weight updates.\n\nTheoretical basis: (1) FAIL-Detect (RSS 2025) proves that OOD detection on success-only demonstration data reliably detects policy failures — the success-demo distribution implicitly excludes failure modes; (2) KDPE (CoRL 2025) demonstrates in Cartesian action space that selecting the most IN-distribution trajectory improves performance, while KDPE-OOD collapses performance on the ToolHang precision task (KDPE-OOD-C: 7% vs. KDPE-C: 76%) — validating the in-distribution selection direction for LOC; (3) z_a from joint video-action pretraining is hypothesized to encode physical plausibility in a tighter quality-discriminative geometry than both Cartesian action space (KDPE, V-GPS) and VLA action tokens. **Inference-time caveat**: In action-only mode, video tokens are at full noise (timestep T) — this quality-discriminative geometry is a training-time property of the learned weights, not an inference-time video conditioning effect. Step 1 empirically tests whether this training-time property persists as a quality signal without video input. LOC is reported as a negative result if AUC < 0.55.\n\nKey differentiation from KDPE and V-GPS (Tier 1 methods): (a) density estimation in WAM action latent space z_a, not Cartesian action space (position/orientation/gripper) or 7D delta actions; (b) success-demonstrations-only reference distribution establishing a quality anchor, not all training data (KDPE) or a separately collected offline RL dataset (V-GPS); (c) no image required at inference — z_a encodes visual-physical context from joint pretraining, unlike V-GPS which concatenates a ResNet-34 image embedding with the raw action for every candidate; (d) B=4–8 candidates vs. KDPE's N=100 and V-GPS's K=50. LOC implements success-mode latent selection; KDPE implements Cartesian-space all-data-mode selection; V-GPS implements offline-RL Q-function scoring in Cartesian+image space — these are mechanistically distinct quality signals across the three representational tiers.\n\nDifferentiation from MG-Select: LOC scores membership in the success demonstration distribution (latent OOD density); MG-Select measures KL divergence of task-conditioned output from masked unconditional distribution (action-space distributional uncertainty).\n\nDifferentiation from Latent Policy Barrier (LPB, arXiv 2508.05941): LPB operates in visual observation latent space (frozen visual encoder from base diffusion policy), measures Euclidean distance to nearest expert demo observation embedding, and performs gradient-based runtime steering of action denoising when out-of-distribution — requiring a separate dynamics model trained on expert plus suboptimal rollout data. LOC operates in WAM action latent space z_a (not observation latents), uses KNN/GMM density estimation on success demos, and scores B candidates PRE-EXECUTION rather than steering during execution — exploiting WAM joint-pretraining geometry unavailable to observation-space methods and requiring zero rollout data.\n\nNote on Cosmos Policy planning mode: Cosmos Policy also implements Best-of-N — generates B actions, predicts future states and values, executes the highest-value action. However, (a) requires fine-tuning a value function on rollout data (1,536 H100-hours for RoboCasa) because demonstration-only training 'cannot correctly predict failure states'; (b) 15 total forward passes per candidate. LOC requires zero rollout data, zero weight updates, and ~5ms per candidate.\n\n**Method 2 — Action-Latent Value MLP (≤40 H100-hours training)**: A 3-layer MLP trained on WAM action latents z_a from LIBERO-90 success demonstrations AND explicitly collected failure trajectories scores each candidate via V(z_{a,i}) ∈ [0,1]. Hard argmax Best-of-N is the primary result. Key hypothesis: z_a regularized by joint video-action pretraining is more linearly separable between success and failure regimes than raw action outputs, VLA action tokens, or Cartesian representations — enabling a simpler, image-free quality discriminator.\n\nDifferentiation from V-GPS (CoRL 2024): V-GPS trains a Q-function via offline RL (Cal-QL) on (image observation, raw 7D Cartesian action) pairs — requiring both a ResNet-34 image encoder and the raw action candidate at inference; our Value MLP trains on WAM action latents z_a alone via binary success/failure supervision — no image required at inference because z_a already encodes visual-physical context from joint pretraining. V-GPS validates the value re-ranking paradigm in Cartesian+image space for VLA-family policies; our Value MLP asks whether WAM latent space provides a more compact, image-free quality signal with stronger success/failure linear separability. Additionally, V-GPS uses sparse binary rewards + Cal-QL offline RL; our Value MLP uses direct binary classification supervision, making it trainable in <5 H100-hours vs. V-GPS's offline RL pipeline. Other differentiations: (a) vs. WAV — WAV trains a trajectory value module as a new architectural component from scratch; Value MLP is plug-in-compatible with any pretrained WAM; (b) vs. RoVer — RoVer requires a 0.2B PRM trained on process labels; Value MLP uses a 3-layer MLP trained on binary success/failure labels; (c) vs. Cosmos Policy — requires 1,536 H100-hours rollout fine-tuning; Value MLP requires ≤40 H100-hours.\n\nDifferentiation from Latent Policy Steering (LPS, arXiv 2507.13340): LPS trains a value function in world model latent state space (Dreamer v3 architecture) using optical flow as an embodiment-agnostic action representation, requiring both expert demonstration states and policy-rollout states for training (so the value function sees distribution-shifted states). Our Value MLP trains on WAM-specific action latents z_a from joint video-action pretraining — not observation/state latents — and requires only binary success/failure labels from collected failures without policy-visit rollout data, testing whether WAM joint pretraining creates a more linearly separable latent geometry that enables a 3-layer image-free MLP to match discriminative power achieved by observation-space value functions.\n\n**Comparison of LOC vs. Value MLP is itself a central contribution**: Their empirical comparison characterizes when WAM latent OOD scoring is sufficient versus when labeled training adds necessary discriminative power — and whether this latent-space approach outperforms Tier 1 (Cartesian + image, V-GPS) and Tier 2 (VLA token distributional uncertainty, MG-Select) methods.\n\n**Mandatory RoboCasa baseline validation before committing to targets**: World2Act (arXiv 2603.10422, March 2026) reports UWM achieving 60.8% on RoboCasa using 1,000 real demonstration fine-tuning. Since UWM was trained only on DROID data and has not been fine-tuned on RoboCasa tasks, the frozen UWM baseline (no RoboCasa demos) is expected to be substantially lower — likely 10–25%. Primary performance target: ≥10pp absolute improvement over the measured frozen baseline.",
  "landscape": "Cosmos Policy (arXiv 2601.16163, ICLR 2026) is the primary comparison point for absolute performance. Fully fine-tunes Cosmos-Predict2-2B on robot demos (384 H100-hours ALOHA, 1,536 RoboCasa, 3,072 LIBERO). Achieves 98.5% LIBERO and 67.1% RoboCasa. Its planning mode implements Best-of-N candidate selection: generates B candidate actions, predicts future states (3 queries to world model) and values (5 queries to value function per future state, 15 total predictions per action), and executes via majority-mean aggregation. Key distinction: Cosmos Policy's authors explicitly state that demo-only training 'cannot correctly predict failure states' — rollout fine-tuning is required for the planning value function. LOC requires zero rollout data and zero weight updates; Value MLP requires ≤40 H100-hours vs. 1,536 H100-hours.\n\nV-GPS (arXiv 2410.13816, CoRL 2024) — CRITICAL PRIOR WORK for Value MLP. 'Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance.' Trains a Q-function via offline RL (Cal-QL) on sparse binary rewards from demonstration data; architecture: ResNet-34 image encoder with FiLM language conditioning, 7-dimensional Cartesian action vector concatenated with image embedding passed through 2-layer MLP to predict scalar Q-value. At inference, samples K=50 action candidates from frozen generalist policies (Octo-small, Octo-base, Octo-small-1.5, RT-1X, OpenVLA) and re-ranks by Q-value. Achieves +82.8% relative improvement on real-robot 6-task benchmark (Octo-small-1.5 baseline: 24%, V-GPS: 44%). Key differentiations from our Value MLP: (a) V-GPS operates in Cartesian+image space — requires both ResNet-34 image embedding AND raw 7D action candidate at every inference call; our Value MLP operates on WAM z_a alone — no image needed at inference because z_a encodes visual-physical context from joint pretraining; (b) V-GPS uses offline RL (Cal-QL) training pipeline; our Value MLP uses binary success/failure classification, trainable in <5 H100-hours; (c) V-GPS applies to generalist VLA policies (Cartesian action outputs without video-physics pretraining); our Value MLP exploits WAM-specific latent geometry from joint video-action pretraining. V-GPS validates the paradigm (value re-ranking of frozen policies works) in Tier 1 (Cartesian+image space); our paper asks whether Tier 3 (WAM latent space) provides a more discriminative, image-free signal.\n\nKDPE (arXiv 2508.10511, CoRL 2025) — CRITICAL PRIOR WORK. Applies manifold-aware KDE to Cartesian action trajectories (end-effector position/SO(3)-orientation/gripper) from Diffusion Policy; generates N=100 candidates; achieves 88.2% vs. 85% on RoboMimic/MimicGen (CNN-based). CRITICAL FINDING: KDPE-OOD (selecting most out-of-distribution trajectory) collapses performance on the ToolHang precision task to 7% (KDPE-OOD-C) vs. 76% for KDPE-C — a dramatic 69pp gap that provides strong empirical grounding for LOC's argmin selection direction. Differentiates from LOC: (a) Cartesian action space vs. WAM action latent space; (b) all training data vs. success-only reference; (c) no WAM-specific joint pretraining regularization; (d) N=100 candidates vs. LOC's B=4–8.\n\nWorld2Act (arXiv 2603.10422, March 2026) — post-training framework achieving ~66% on RoboCasa using 50 real + 50 imagined demos; reports UWM achieves 60.8% on RoboCasa with 1,000-demo fine-tuning (confirming frozen UWM baseline is ~10–25%); differentiation: World2Act requires contrastive post-training to align VLA latents; LOC exploits WAM alignment inherited from joint pretraining.\n\nFast-WAM (arXiv 2603.16666) — CRITICAL FRAMING: 97.6% LIBERO-avg (Table 2) and 91.8% RoboTwin (Table 1) at 190ms without video; single trajectory only; our method uses same action-only inference for candidate generation and adds LOC selection at B × 5ms overhead.\n\nRoVer (arXiv 2510.10975, ICLR 2026) — CRITICAL PRIOR WORK: generates B VLA candidates, trains 0.2B PRM; differentiation: requires 0.2B model training vs. LOC's zero training and Value MLP's 3-layer MLP; VLA action tokens lack video-physics regularization.\n\nVerifier-free Test-Time Sampling / MG-Select (arXiv 2510.05681, ICLR 2026) — CRITICAL PRIOR WORK: training-free KL-from-masked-distribution scoring for frozen VLAs; 168% relative improvement on RoboCasa pick-and-place; differentiation: MG-Select measures action-space distributional uncertainty, LOC measures latent OOD membership relative to success demo distribution.\n\nWorld-Value-Action (WAV) Model (arXiv 2604.14732, April 2026) — trajectory value module requiring training from scratch, new architectural component; iterative latent-space inference concentrating probability mass on high-value trajectories. LIBERO results (Table 1): Spatial 100.0%, Object 98.6%, Goal 94.4%, Long 98.1% (~97.8% arithmetic average across 4 splits); 75.6% real-world average (Figure 2, dual-arm Piper robot, 15 trials per task). Note: WAV's LIBERO evaluation covers 4 benchmark splits but does not include LIBERO-90; our primary evaluation uses LIBERO-Long and RoboCasa. Differentiation: WAV trains value and world model jointly from scratch (architectural co-design); our method leaves all WAM weights frozen and is plug-in-compatible with any pretrained WAM.\n\nBeing-H0.7 (arXiv 2605.00078, May 2026) — concurrent WAM achieving 99.2% on LIBERO average via latent prior-posterior alignment between egocentric video pretraining and robot action finetuning. Not a candidate selection paper — uses a single-trajectory policy architecture rather than Best-of-N scoring. Cited to contextualize the near-saturation LIBERO performance level for strong recent WAMs; our method targets RoboCasa as the meaningful discrimination benchmark.\n\nLatent Policy Barrier (LPB, arXiv 2508.05941, 2025) — uses Euclidean distance in visual observation latent space (frozen visual encoder from base diffusion policy) to nearest expert demo state as OOD signal; at inference, monitors OOD score and applies gradient-based action denoising corrections at runtime when the predicted state leaves the expert distribution; uses a separate dynamics model trained on expert plus suboptimal rollout data. Differentiation from LOC: LPB operates on observation latents (not WAM action latents z_a), performs runtime execution-time steering (not pre-execution candidate selection), and requires a dynamics model trained on rollout data rather than zero rollout data. LOC exploits WAM joint-pretraining geometry unavailable to observation-space methods and scores B candidates before execution.\n\nLatent Policy Steering (LPS, arXiv 2507.13340, 2025) — trains a value function in world model latent state space (Dreamer v3 architecture) on expert demonstration states plus policy-rollout states, using optical flow as an embodiment-agnostic action representation; achieves 70% relative improvement with 30–50 target-embodiment demonstrations on real-world tasks and 10.6% average improvement on Robomimic. Differentiation from Value MLP: LPS trains its value function in world model latent state space (not WAM action latents z_a from joint video-action pretraining); requires policy-rollout data (not just binary success/failure from collected failures); uses optical flow rather than WAM z_a. Our Value MLP tests whether WAM joint pretraining creates a more linearly separable action-latent geometry enabling a 3-layer image-free MLP trained only on binary success/failure labels.\n\nBest-of-Q (arXiv 2601.22701, January 2026) — Q-function re-ranking of frozen VLM agents for digital tasks (web/OS control); mechanistically analogous to V-GPS applied to digital agents; not in robot manipulation domain but confirms paradigm generality beyond robotics.\n\nALT Policy (arXiv 2505.05787, May 2025) — 'Demystifying Diffusion Policies: Action Memorization and Simple Lookup Table Alternatives': demystifies diffusion policies as implicit nearest-neighbor lookup tables, using contrastive image encoder distance in observation latent space as a runtime OOD signal for single-trajectory retrieval. Related to LOC in applying latent-space OOD proximity as a quality signal, but operates in observation (not action) latent space and retrieves a single stored trajectory rather than scoring multi-candidate selections.\n\nUNISafe (arXiv 2505.00779, May 2025) — 'Uncertainty-aware Latent Safety Filters for Avoiding Out-of-Distribution Failures': calibrates a world model's epistemic uncertainty via conformal prediction to detect OOD state predictions, then performs Hamilton-Jacobi reachability in augmented latent+uncertainty space to synthesize a policy-agnostic safety filter. Related to LOC in applying conformal prediction to world-model latents, but targets state-space safety intervention rather than pre-execution action-latent candidate selection for task performance.\n\nVLS (arXiv 2602.03973, February 2026) — 'Steering Pretrained Robot Policies via Vision-Language Models': applies VLM-generated reward gradients to steer frozen diffusion/flow-matching policies' denoising process toward semantically correct behaviors; training-free guidance via language-conditioned reward signals, not latent-space density or value functions. Different mechanism from both LOC and Value MLP; concurrent work.\n\nFAIL-Detect (arXiv 2503.08558, RSS 2025) — SUPPORTING WORK: proves OOD detection on success-only demonstration data reliably detects policy failures; uses flow-based density estimation on distilled policy signals; motivates LOC's use of KNN/GMM density on success demo latents; FAIL-Detect is execution-time monitoring, LOC is pre-execution candidate selection — Step 1 LOC diagnostic is the first empirical test of whether this principle transfers to pre-execution WAM z_a.\n\nEVA (arXiv 2603.17808, 2026) — identifies 'executability gap' showing visually coherent world model rollouts can violate kinematic constraints; supports LOC over PCS: visual denoising error does not predict task success.\n\nWAV: see above. Compose Your Policies! / GPC (arXiv 2510.01068) — training-free convex composition of multiple frozen policy distributions; operates at distribution level, not discrete candidate selection from single WAM. GPC-RANK (arXiv 2502.00622, IEEE RAL 2025): frozen policy + separately trained action-conditioned world model + hard argmax; uses world-model reward prediction for scoring, not WAM action latent OOD. When to Trust Imagination (arXiv 2605.06222, May 2026): FFDC adaptively decides action chunk sizes during single-trajectory execution; orthogonal and combinable.",
  "approach": "Primary backbone: UWM (github.com/WEIRDLabUW/unified-world-model, RSS 2025), whose independent per-modality diffusion timestep architecture supports action-only inference (policy mode: video timestep = T, action timestep = 0). All WAM weights frozen throughout.\n\n**Step 0a — Frozen UWM Baseline Validation on RoboCasa (MANDATORY FIRST STEP)**: Run B=1 frozen UWM action-only inference on 50 episodes of representative RoboCasa tasks (kitchen manipulation subset). Expected baseline: 10–25% (UWM trained on DROID data only; World2Act reports 60.8% with 1,000-demo fine-tuning, confirming frozen baseline is substantially lower). Decision tree: if baseline ≥ 30%, proceed with current framing; if baseline 10–25%, confirm ≥10pp absolute improvement framing. Cost: ~2–3 H100-hours.\n\n**Step 0b — Reference Distribution Encoding for LOC**: Encode LIBERO-90 success demos through frozen UWM in action-only mode to obtain {z_a^success}. Fit density estimators: (a) KNN nonconformity model (k=10, Euclidean distance); (b) GMM (k=3,5 components, full covariance). Split latents 80/20 train/hold-out for AUC evaluation in Step 1. Cost: ~10–15 H100-hours encoding; ~30 minutes fitting density estimator. Steps 0b and 0c can run in parallel after Step 0a completes.\n\n**Step 0c — Failure Demonstration Collection (required for Value MLP)**: (a) Primary negatives: run frozen UWM (B=1) on LIBERO-Long and validated RoboCasa tasks; expected failure rate 30–50% on RoboCasa tasks, 5–15% on LIBERO-Long, yielding 500–2,000 failure trajectories. Cost: 15–20 H100-hours. (b) Synthetic supplement: Gaussian action perturbation (σ ∈ {0.05, 0.1}) on 20% of LIBERO-90 success demos, simulate in MuJoCo, flag truncated episodes as failures. Cost: <1 H100-hour. Combined: balanced 2,000–4,000 positive / 2,000–4,000 negative training set.\n\n**Step 1 — LOC Diagnostic (MANDATORY before main ablation)**: Empirically tests Hypothesis H1: 'WAM joint pretraining creates a latent success distribution where S_LOC(z_a) achieves AUC > 0.60 as a binary success predictor.' Theoretical motivation: FAIL-Detect's principle (OOD on success-only data detects failures) + KDPE's empirical confirmation (KDPE-OOD collapses ToolHang from 76% to 7%, confirming in-distribution selection outperforms outlier selection in Cartesian space). Inference-time caveat: z_a geometry is a training-time property — in action-only inference, video tokens are at full noise (timestep T) providing no inference-time conditioning. We hypothesize that joint training causes z_a to learn quality-discriminative representations even without video input, but Step 1 is the first empirical test of this hypothesis. If H1 fails (AUC < 0.55), LOC reports a negative result.\n\nProtocol: Sample B=16 action-only candidates from frozen UWM on 3 RoboCasa tasks, execute each in simulation (ground-truth success/failure), compute LOC and comparison scores.\n\nLOC metrics: (1) AUC of S_LOC as binary success predictor on held-out demos (target H1: AUC > 0.60); (2) Spearman ρ of S_LOC with success labels (target ρ > 0.3); (3) compare KNN vs. GMM density estimators. Also compute: S_PCS = ||ε − ε_θ(x_{t*}, z_{a,i}, t*)||² for the same candidates, varying t* ∈ {T/4, T/2, 3T/4} (expected to show lower AUC based on Cosmos Policy finding and EVA's executability gap); MG-Select-style KL score as Tier 2 comparison; KDPE-style Cartesian density as Tier 1 comparison baseline.\n\nExpected result: LOC AUC > PCS AUC ≈ MG-Select AUC ≈ KDPE-Cartesian AUC, confirming Tier 3 (WAM latent) is more informative than Tier 1 (Cartesian) and Tier 2 (VLA token distributional uncertainty) methods.\n\nDecision tree: if AUC ≥ 0.60, LOC is primary zero-training method; if LOC 0.55–0.60, both methods reported with LOC as secondary; if LOC < 0.55, LOC reported as negative result with informative comparison.\n\n**Step 2 — Diversity Pilot (combined with LOC diagnostic)**: Same B=16 rollouts measure: pairwise cosine distance of action latents {z_{a,i}} (target mean > 0.05; if lower, increase noise temperature T_noise ∈ {1.5, 2.0}); LOC AUC conditional on latent diversity.\n\n**Step 3 — Value MLP Training**: 3-layer MLP (input: flattened z_a; output: scalar V ∈ [0,1]) trained via binary cross-entropy on balanced success/failure latents from Steps 0b and 0c. Report binary classification accuracy on held-out split (target > 75%). Key distinction from V-GPS: no image input required at inference — z_a encodes visual-physical context from joint pretraining, making the Value MLP an image-free quality discriminator. Cost: ~3–5 H100-hours.\n\n**Step 4 — Inference-Time Best-of-N Planning**: At each planning step, sample B=4–8 action-only trajectories from frozen UWM.\n\nPrimary results (two methods):\n- LOC selection: a_{i*} = argmin_i S_LOC(z_{a,i}) at best density estimator from diagnostic [zero weight updates, WAM-specific, no image at inference]\n- Value MLP selection: a_{i*} = argmax_i V(z_{a,i}) [lightweight training, WAM-specific, no image at inference]\n\nComparisons (required): V-GPS-style Cartesian Q-function applied to WAM action outputs (Tier 1 baseline); MG-Select-style KL scoring applied to WAM action-only inference (Tier 2 baseline); random selection (B=4–8, sanity check); single-trajectory WAM B=1 (frozen baseline).\n\nAblation (secondary): (a) PCS denoising error selection at best t* from diagnostic (expected to underperform LOC); (b) soft MPPI w_i ∝ exp(β·V(z_{a,i})) to document action-averaging artifact; (c) action-only z_a vs. full video+action latent for LOC and Value MLP scoring.\n\n**Ablation Grid**: B ∈ {1, 4, 8} (B=1 is frozen WAM single-trajectory baseline); selection method: LOC KNN vs. LOC GMM (primary zero-training) vs. Value MLP hard argmax (primary trained) vs. V-GPS-style Cartesian scoring (Tier 1 baseline) vs. MG-Select-style KL (Tier 2 baseline) vs. random selection (sanity check); T_noise fixed at 1.0 in primary ablation; execution regime: (a) open-loop vs. (b) periodic replanning every K=5 action chunks.\n\n**Primary hypotheses**: (H1, tested in Step 1 LOC diagnostic) LOC achieves Spearman ρ > 0.3 and AUC > 0.6, confirming WAM success latents form an OOD-detectable distribution even without video input at inference — tested empirically in Step 1; (H2) LOC outperforms PCS and MG-Select-style KL in the diagnostic; (H3) Value MLP achieves ≥10pp improvement over B=1 baseline on RoboCasa; (H4) LOC achieves ≥5pp improvement over B=1 with zero weight updates; (H5) Both methods outperform V-GPS-style Cartesian scoring and MG-Select-style KL applied to WAM outputs, confirming the Tier 3 latent quality-discrimination advantage.\n\n**Standalone Value MLP contribution (applicable if LOC fails H1)**: If LOC AUC < 0.55 in the diagnostic, the paper's narrative shifts to Value MLP as the primary contribution: (a) vs. V-GPS — V-GPS requires ResNet-34 image embedding + 7D Cartesian action at every inference call (Tier 1, image-dependent); Value MLP operates on WAM z_a alone (no image at inference), trained via binary classification rather than offline RL; (b) vs. WAV — WAV trains from scratch as architectural co-design; Value MLP is plug-in-compatible with any pretrained WAM; (c) vs. RoVer — RoVer requires a 0.2B PRM on process labels; Value MLP uses a 3-layer MLP on binary success/failure labels; (d) vs. Cosmos Policy — 1,536 H100-hours rollout fine-tuning vs. ≤40 H100-hours; (e) vs. KDPE — KDPE operates in Cartesian space with all training data; Value MLP uses WAM latent space with success/failure-labeled data; (f) vs. LPS — LPS requires policy-rollout data and operates in world model state latent space; Value MLP uses only binary success/failure labels in WAM action latent space. Central empirical claim: joint pretraining creates a latent space where success/failure are more linearly separable than in Cartesian action space, enabling a 3-layer image-free MLP to match or exceed the discriminative power that V-GPS achieves via a ResNet-34-augmented Q-function with offline RL.\n\n**Proactive framing against fine-tuned baselines**: Expected absolute RoboCasa performance (~20–35% after ≥10pp improvement from 10–25% frozen baseline) will appear weak against Cosmos Policy (67.1%) and World2Act (~66%). The paper must explicitly frame this in the introduction and evaluation sections: 'Our methods are orthogonal to fine-tuning — they extract planning value from existing pretrained WAMs in settings where domain-specific demonstration data is unavailable. The comparison target is B=1 frozen WAM inference at the same data budget (zero domain-specific demos for LOC; ≤40 H100-hours of simulation rollouts for Value MLP), not fine-tuned models that consumed 1,000 real robot demonstrations or 1,536 H100-hours of rollout fine-tuning. In zero-demonstration deployment scenarios — a common real-world constraint — our methods improve over the no-adaptation baseline by ≥10pp without any weight updates or real robot data collection. The gap versus fine-tuned methods quantifies the cost of the zero-demonstration constraint, not a failure of candidate selection.'\n\n**Evaluation Benchmarks**: (a) Primary — RoboCasa: Cosmos Policy fine-tuned 67.1%; World2Act (Cosmos+World2Act) ~66%; frozen UWM expected 10–25% (validated in Step 0a); absolute target ≥10pp over frozen baseline. (b) Secondary — LIBERO-Long: near saturation for strong frozen WAMs (Fast-WAM 95.2%, Table 2); included to characterize gain profile vs. task difficulty. (c) Baselines: B=1 frozen WAM, random selection, V-GPS-style Cartesian scoring, MG-Select-style KL applied to WAM.\n\nDreamZero cross-WAM validation deferred to camera-ready. CoRL submission rests on UWM alone.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~140h H100",
      "gpu_utilization": "HIGH idle (~35–55%): GPU waits while researcher implements LOC density estimator (KNN/GMM fitting), interprets LOC diagnostic results, debugs failure collection pipeline, and designs ablations.",
      "timeline": "2–3 months",
      "team": "1–2 researchers",
      "estimated_gpu_cost": "~$350 (140h × $2.50/h blended Lambda/RunPod/Vast.ai H100 rate)"
    },
    "human_in_loop": {
      "gpu_hours": "~165h H100",
      "gpu_utilization": "MODERATE idle (~20–30%): agent handles code scaffolding, baseline validation, LOC diagnostic, failure collection, demo encoding, density estimator fitting, and experiment submission; human reviews Step 0a baseline and LOC diagnostic results at daily check-ins to make go/no-go decisions",
      "timeline": "3–4 weeks",
      "team": "1 researcher, ~30 min/day check-in",
      "claude_api_cost": "$150–250 (~1,500–2,500 turns at mixed Sonnet/Opus rates)",
      "estimated_gpu_cost": "~$413 (165h × $2.50/h)",
      "risk_note": "Step 0a (frozen UWM RoboCasa baseline) and LOC diagnostic are hard sequential dependencies before main ablation. Sequential order: 0a baseline validation (2–3 H100-hours, Day 1–2) → LOC diagnostic (3–5 H100-hours, Day 2–4) → failure collection (15–20 H100-hours, Day 3–7, parallel with LOC) → demo encoding + density fitting (10–15 H100-hours, Day 5–9) → Value MLP training (3–5 H100-hours, Day 9–10) → main ablations (Day 10–18). RoboCasa simulation setup requires separate engineering effort from LIBERO. DreamZero cross-WAM deferred to camera-ready."
    },
    "auto_research": {
      "gpu_hours": "~185h H100 (revised from prior 320h estimate; ablation grid pruned to stay within ≤200h hard constraint)",
      "gpu_budget_breakdown": "Step 0a frozen UWM baseline: ~3h; Steps 0b+0c in parallel (demo encoding + failure collection): ~32h billed (12h encoding + 20h failure collection running concurrently); Step 1 LOC diagnostic: ~4h; Step 3 Value MLP training: ~5h; Main ablation grid (B ∈ {1,4,8} × 6 methods × 3 seeds × 2 benchmarks = 108 runs × ~1.2h avg): ~130h; contingency/reruns: ~11h. Total: ~185h billed GPU-hours. With 4 GPUs running ablation batch concurrently: wall-clock ≈ 44h setup + 33h ablations = 77h wall-clock; billed ≤ 200h hard constraint.",
      "gpu_utilization": "MINIMAL idle (~5–10%): agent pipelines baseline validation, LOC diagnostic, failure collection, demo encoding, density fitting, MLP training, and evaluation continuously.",
      "timeline": "7–10 days with 4 H100 GPUs simultaneously",
      "team": "0 (only initial repo setup and credential configuration)",
      "claude_api_cost": "$200–350 (~2,500–4,000 turns at Opus rates)",
      "estimated_gpu_cost": "~$463 (185h × $2.50/h)",
      "ablation_grid_vs_prior": "Ablation grid expanded from 5 to 6 selection methods by adding V-GPS-style Cartesian scoring as a Tier 1 baseline, providing direct Tier 1 vs. Tier 3 comparison. T_noise sweep ({1.0,1.5,2.0}) dropped from auto research grid — T_noise fixed at 1.0 unless diversity pilot (Step 2) shows mean cosine distance < 0.05. B grid: {1,4,8} (B=1 is frozen WAM single-trajectory baseline). PCS full ablation retained only in Step 1 LOC diagnostic.",
      "speed_bottleneck": "Step 0a baseline validation → LOC diagnostic → (parallel: failure collection + demo encoding) → density fitting (trivial) + Value MLP training is a 5-step sequential dependency spanning ~8 days minimum. RoboCasa evaluation rollouts: each ablation variant requires sequential per-task evaluation; with 4 GPUs running 4 variants concurrently, the full grid needs ~5–7 days.",
      "risk_note": "LOC density estimation (KNN/GMM) is a standard sklearn/torch operation requiring no custom implementation. Main implementation risk: UWM action latent extraction in action-only mode (video timestep = T, action timestep = 0) — this mode is supported by UWM's architecture but may require engineering to extract z_a as a fixed-size vector for density estimation. If z_a is not directly accessible, the Action Decoder intermediate activations serve as a substitute latent representation. V-GPS-style Cartesian baseline requires implementing the Cartesian action extraction and Q-function scoring as an additional comparison method."
    }
  },
  "target_venues": [
    "CoRL 2026 (Abstract deadline: May 26, 2026; Full paper: May 29, 2026; Conference: Nov 9–12, Austin TX) — TIGHT but viable: 19 days from 2026-05-10. Step 0a RoboCasa baseline must run immediately (Day 1–2). Minimum viable submission: frozen UWM RoboCasa baseline validation + LOC diagnostic figure (including PCS and Tier 1/Tier 2 comparison showing expected negative results) + LOC and/or Value MLP Best-of-N results (primary) + LIBERO-Long (secondary) + B/hard-argmax ablation + V-GPS-style Cartesian and MG-Select-style KL baseline comparisons. DreamZero cross-WAM deferred to camera-ready.",
    "ICLR 2027 (deadline ~September–October 2026) — More feasible timeline for complete ablation grid, latent geometry analysis (success/failure separation across Tier 1/2/3 representations), DreamZero cross-WAM evaluation, and potential real-world experiments."
  ],
  "level": "solid",
  "key_references": [
    "V-GPS: Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance (arXiv 2410.13816, CoRL 2024) — CRITICAL PRIOR WORK for Value MLP: trains Q-function via offline RL (Cal-QL) on sparse binary rewards; architecture: ResNet-34 image encoder + 7D Cartesian action → scalar Q-value; applies to frozen Octo-small/Octo-base/Octo-small-1.5/RT-1X/OpenVLA; samples K=50 candidates; achieves +82.8% relative improvement (Octo-small-1.5 baseline 24% → V-GPS 44%) on real-robot 6-task benchmark; validates value re-ranking paradigm for frozen policies in Tier 1 (Cartesian+image) space. Differentiates from Value MLP: (a) V-GPS requires ResNet-34 image embedding + raw 7D action at every inference call; Value MLP uses WAM z_a alone (no image needed at inference); (b) offline RL training vs. binary classification; (c) Cartesian+image vs. WAM latent space",
    "Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning (arXiv 2601.16163, ICLR 2026) — CRITICAL PRIOR WORK: implements Best-of-N planning mode (15 forward passes per action via majority-mean aggregation of world model + value function queries); requires rollout fine-tuning because demo-only training 'cannot correctly predict failure states'; 1,536 H100-hours for RoboCasa; 98.5% LIBERO, 67.1% RoboCasa; our LOC requires zero rollout data and zero weight updates",
    "KDPE: A Kernel Density Estimation Strategy for Diffusion Policy Trajectory Selection (arXiv 2508.10511, CoRL 2025) — CRITICAL PRIOR WORK: applies manifold-aware KDE to Cartesian action trajectories (end-effector position/SO(3)-orientation/gripper) from Diffusion Policy; generates N=100 candidates; achieves 88.2% (CNN) on RoboMimic/MimicGen. CRITICAL FINDING: KDPE-OOD (selecting most out-of-distribution trajectory) collapses ToolHang performance to 7% (KDPE-OOD-C) vs. 76% (KDPE-C) — a 69pp gap providing strong empirical grounding for LOC's argmin selection direction. Tier 1 (Cartesian space) method",
    "World2Act (arXiv 2603.10422, March 2026) — post-training framework achieving ~66% on RoboCasa using 50 real + 50 imagined demos; reports UWM achieves 60.8% on RoboCasa with 1,000-demo fine-tuning (confirming frozen UWM baseline is ~10–25%); differentiation: World2Act requires contrastive post-training to align VLA latents; LOC exploits WAM alignment inherited from joint pretraining",
    "Fast-WAM: World Action Models without Test-Time Video (arXiv 2603.16666) — CRITICAL FRAMING: 97.6% LIBERO-avg (Table 2) and 91.8% RoboTwin (Table 1) at 190ms without video; single trajectory only; our method uses same action-only inference for candidate generation and adds LOC selection at B × 5ms overhead",
    "FAIL-Detect: Failure Detection as OOD Detection for Robot Manipulation (arXiv 2503.08558, RSS 2025) — SUPPORTING WORK: proves OOD detection on success-only demonstration data reliably detects policy failures; motivates LOC's use of KNN/GMM density on success demo latents; FAIL-Detect is execution-time monitoring, LOC is pre-execution candidate selection — Step 1 LOC diagnostic is the first empirical test of whether this principle transfers to pre-execution WAM z_a in action-only inference mode",
    "EVA: Aligning Video World Models with Executability (arXiv 2603.17808, 2026) — identifies 'executability gap' showing visually coherent world model rollouts can violate kinematic constraints; supports LOC over PCS: visual denoising error does not predict task success",
    "RoVer: Robot Reward Model as Test-Time Verifier for Vision-Language-Action Models (arXiv 2510.10975, ICLR 2026) — CRITICAL PRIOR WORK: generates B VLA candidates, trains 0.2B PRM; Tier 2 (VLA action token) method; differentiation: requires 0.2B model training vs. LOC's zero training and Value MLP's 3-layer MLP; VLA action tokens lack video-physics regularization",
    "Verifier-free Test-Time Sampling / MG-Select (arXiv 2510.05681, ICLR 2026) — CRITICAL PRIOR WORK: training-free KL-from-masked-distribution scoring for frozen VLAs; 168% relative improvement on RoboCasa pick-and-place; Tier 2 (VLA action token distributional uncertainty) method; differentiation: MG-Select measures action-space distributional uncertainty, LOC measures latent OOD membership relative to success demo distribution",
    "World-Value-Action (WAV) Model (arXiv 2604.14732, April 2026) — trajectory value module requiring architectural co-design and training from scratch; LIBERO results (Table 1): Spatial 100.0%, Object 98.6%, Goal 94.4%, Long 98.1% (~97.8% arithmetic average across 4 splits); 75.6% real-world average (Figure 2, dual-arm Piper robot, 15 trials per task); our method leaves all WAM weights frozen and is plug-in-compatible with pretrained WAMs",
    "Being-H0.7 (arXiv 2605.00078, May 2026) — concurrent WAM achieving 99.2% on LIBERO average via latent prior-posterior alignment between egocentric video pretraining and robot action finetuning; uses single-trajectory policy (not Best-of-N candidate selection); cited to contextualize near-saturation LIBERO performance for strong WAMs; our primary discrimination benchmark is RoboCasa",
    "Latent Policy Barrier (LPB, arXiv 2508.05941, 2025) — uses Euclidean distance in visual observation latent space (frozen visual encoder from base diffusion policy, δ(z)=‖z−z_NN‖²₂) to nearest expert demo embedding as OOD signal; gradient-based runtime steering of action denoising when OOD detected, using a separate dynamics model trained on expert plus suboptimal rollout data. Differentiates from LOC: (a) observation latent space vs. WAM action latent z_a; (b) runtime execution-time steering vs. pre-execution candidate scoring; (c) dynamics model requires rollout data vs. LOC requires zero rollout data; (d) single-trajectory steering vs. Best-of-N selection exploiting WAM joint-pretraining geometry",
    "Latent Policy Steering (LPS, arXiv 2507.13340, 2025) — trains value function in world model latent state space (Dreamer v3) on expert demonstration states plus policy-rollout states; uses optical flow as embodiment-agnostic action representation; achieves 70% relative improvement with 30–50 target-embodiment demonstrations (real-world) and 10.6% average improvement on Robomimic. Differentiates from Value MLP: (a) world model latent STATE space vs. WAM action latent z_a; (b) optical flow action representation vs. WAM z_a from joint video-action pretraining; (c) requires policy-rollout data for training vs. Value MLP uses only binary success/failure labels from demonstrations + collected failures; (d) does not exploit WAM joint-pretraining latent geometry for action-space separability",
    "ALT Policy (arXiv 2505.05787, May 2025) — 'Demystifying Diffusion Policies: Action Memorization and Simple Lookup Table Alternatives': uses contrastive image encoder distance in observation latent space as runtime OOD signal for single nearest-neighbor action retrieval; related to LOC in applying latent-space proximity as a quality signal, but in observation (not action) latent space and via retrieval rather than multi-candidate selection",
    "UNISafe (arXiv 2505.00779, May 2025) — 'Uncertainty-aware Latent Safety Filters for Avoiding Out-of-Distribution Failures': calibrates world model epistemic uncertainty via conformal prediction for OOD-based safety filtering in state latent space; related to LOC in applying conformal prediction to world-model latents, but targets state-space safety rather than pre-execution action-latent candidate selection",
    "VLS: Steering Pretrained Robot Policies via Vision-Language Models (arXiv 2602.03973, February 2026) — training-free VLM-reward-gradient guidance of frozen diffusion/flow-matching policies' denoising process; different mechanism from both LOC (latent OOD density) and Value MLP (binary classification); concurrent work",
    "Compose Your Policies! / GPC (arXiv 2510.01068) — training-free convex composition of multiple frozen policy distributions; operates at distribution level, not discrete candidate selection from single WAM",
    "Inference-Time Enhancement / GPC-RANK (arXiv 2502.00622, IEEE RAL 2025) — frozen policy + separately trained action-conditioned world model + hard argmax; uses world-model reward prediction for scoring, not WAM action latent OOD",
    "Unified World Models / UWM (arXiv 2504.02792, RSS 2025) — primary backbone; independent per-modality timesteps support action-only inference; publicly available weights and code",
    "Diffusion Policy (arXiv 2303.04137, RSS 2023 / IJRR 2024) — documents multi-modal action distribution handling; confirms averaging over manipulation action modes produces infeasible blended actions; justifies hard argmax over soft MPPI weighting",
    "When to Trust Imagination (arXiv 2605.06222, May 2026) — CONCURRENT WORK: FFDC adaptively decides action chunk sizes; orthogonal to our pre-execution selection; combinable",
    "World Action Models as Zero-shot Policies / DreamZero (arXiv 2602.15922) — 14B joint video+action DiT; secondary backbone for cross-WAM validation in camera-ready/ICLR version",
    "OA-WAM (arXiv 2605.06481, May 2026) — concurrent work; different problem (object binding)",
    "CKT-WAM (arXiv 2605.06247, May 2026) — concurrent work; different problem (cross-WAM knowledge transfer)",
    "GigaBrain-0.5M* (arXiv 2602.12099) — RAMP RL loop requires 30%+ more training",
    "H-WM (arXiv 2602.11291) — requires hierarchical architectural co-design",
    "Latent Diffusion Planning (arXiv 2504.16925) — trains diffusion planner from scratch"
  ],
  "description": "Latent-Distribution Candidate Selection (LDCS) converts any pretrained video-diffusion World Action Model into a multi-candidate planner at inference time without modifying any WAM weight, exploiting WAM-specific latent structure through two complementary methods — positioned within a three-tier action representation hierarchy for candidate selection.\n\n**The three-tier framing**: Existing candidate selection methods operate in three representational tiers: (1) Cartesian action space — KDPE (kernel density, N=100 candidates; KDPE-OOD collapses ToolHang to 7% vs. KDPE's 76%, confirming in-distribution selection) and V-GPS (Q-function re-ranking via offline RL on 7D actions + ResNet-34 image embeddings, +82.8% real-robot improvement, CoRL 2024), both requiring raw action representations and, for V-GPS, image input at every inference call; (2) VLA action tokens — MG-Select (KL-divergence confidence) and RoVer (0.2B PRM) without video-physics co-regularization; (3) WAM action latents z_a — continuous latents from joint video-action diffusion pretraining (this paper). Adjacent latent-space methods that do not perform candidate selection include Latent Policy Barrier (observation latent OOD with gradient-based runtime steering) and Latent Policy Steering (world model state latent value function with optical flow and policy-rollout data). The central hypothesis: WAM action latent space offers richer quality-discriminative geometry than Tier 1 (Cartesian+image) or Tier 2 (VLA tokens), enabling simpler discriminators without image input at inference — an orthogonal capability not addressed by LPB or LPS.\n\n**Inference-time caveat on z_a geometry**: In action-only inference (video timestep = T), video tokens are at full noise — no inference-time video conditioning occurs. The quality-discriminative structure of z_a is a training-time property of joint pretraining. Step 1 (LOC diagnostic) is the first empirical test of whether this geometry persists as a success/failure discriminator without video input. If H1 fails (AUC < 0.55), LOC reports a negative result and Value MLP becomes the sole primary contribution.\n\n**Method 1 — Latent OOD Consistency Scoring (LOC, zero weight updates)**: Fit a KNN or GMM density estimator on WAM action latents {z_a^success} from LIBERO-90 success demos. At inference, sample B=4–8 action-only candidates and score each by nonconformity: S_LOC(z_{a,i}) = −log p̂(z_{a,i}). Select argmin (most in-distribution candidate). Overhead: B × ~5ms = 20–40ms for B=4–8. No image needed at inference.\n\n**Method 2 — Action-Latent Value MLP (≤40 H100-hours)**: 3-layer MLP trained on {z_a^success} and explicitly collected failure latents. Hard argmax selection. No image needed at inference — z_a encodes visual-physical context from joint pretraining. Differentiated from V-GPS: operates on WAM z_a alone (no ResNet-34 image embedding), uses binary classification (not offline RL), and is trained in <5 H100-hours. Differentiated from LPS: does not require policy-rollout data and operates in WAM action latent space (not world model state latent space or optical flow). Central hypothesis: joint pretraining creates a latent space where success/failure are more linearly separable than in Cartesian action space, enabling a 3-layer image-free MLP to match or exceed discriminative power that V-GPS achieves via Cartesian+image Q-function.\n\n**LOC Diagnostic (mandatory, Step 1)**: B=16 rollouts on 3 RoboCasa tasks, measuring AUC of S_LOC as binary success predictor (target H1: AUC > 0.6), compared against: (a) video denoising error S_PCS, (b) MG-Select-style KL (Tier 2), (c) V-GPS-style Cartesian density (Tier 1). Tests the full three-tier hierarchy in a controlled diagnostic before committing to the main ablation.\n\nPrimary evaluation: RoboCasa (target ≥10pp absolute over frozen baseline; Cosmos Policy 67.1% / World2Act ~66% as fine-tuned upper references — explicitly framed as orthogonal to our zero-demonstration deployment target). Secondary: LIBERO-Long. Auto research ablation grid: B ∈ {1,4,8} × 6 methods × 3 seeds × 2 benchmarks (~185 billed H100-hours ≤ 200h hard constraint). CoRL submission: UWM only; DreamZero cross-WAM deferred to camera-ready.",
  "project_name": "frozen_wam_mppi",
  "source": "web_research"
}
```

---

**Summary of all changes made (minor revision):**

**1. WAV metrics corrected** — Removed the arithmetically inconsistent "99.6% overall average across 4 splits" claim. Now consistently reports: "Spatial 100.0%, Object 98.6%, Goal 94.4%, Long 98.1% (~97.8% arithmetic average across 4 splits)" in `landscape`, `key_references`, and `description`. The 75.6% real-world figure is retained.

**2. KDPE-OOD strengthened with ToolHang magnitude** — All KDPE-OOD mentions now include the specific numbers: "KDPE-OOD-C: 7% vs. KDPE-C: 76% on ToolHang (Table 1)" — a 69pp gap that makes the empirical case for LOC's argmin direction far more compelling than "performs worse."

**3. Latent Policy Barrier (arXiv 2508.05941) added** — Added to `core_problem`, `opportunity` (LOC differentiation), `landscape`, and `key_references`. Differentiation is precise: observation latent vs. WAM action latent z_a; runtime gradient steering vs. pre-execution candidate scoring; requires rollout-trained dynamics model vs. zero rollout data.

**4. Latent Policy Steering (arXiv 2507.13340) added** — Added to `core_problem`, `opportunity` (Value MLP differentiation), `landscape`, and `key_references`. Differentiation: world model state latent (Dreamer v3) + optical flow + policy-rollout data vs. WAM action latent z_a + binary success/failure labels only.

**5. Being-H0.7 (arXiv 2605.00078) added** — Brief mention in `landscape` and `key_references` as a concurrent WAM achieving 99.2% on LIBERO via latent prior-posterior alignment (not candidate selection), contextualizing LIBERO score comparisons without conflating it with this paper's problem.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45acbc0f-40a5-412d-bc0a-788de755dbd8",
  "isSidechain": false,
  "requestId": "req_011CatfCi9CwFWV3HsAXPvbd",
  "type": "assistant",
  "uuid": "02500cc7-f3e9-4daf-b13f-4f528d329d2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b9fbaa-4159-4906-9e7b-5c7c38fdb4da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_016P45ZyjTvLEcfNbk7z6jQD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11016,
      "cache_read_input_tokens": 38446,
      "output_tokens": 16394,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11016,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 16394,
          "cache_read_input_tokens": 38446,
          "cache_creation_input_tokens": 11016,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11016
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Runtime record

_source line 43_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Latent-Distribution Candidate Selection for Frozen World Action Models…",
  "leafUuid": "02500cc7-f3e9-4daf-b13f-4f528d329d2b",
  "sessionId": "f0b9fbaa-4159-4906-9e7b-5c7c38fdb4da"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "Frozen WAM candidate selection via action latent OOD scoring",
  "sessionId": "f0b9fbaa-4159-4906-9e7b-5c7c38fdb4da"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Latent-Distribution Candidate Selection for Frozen World Action Models…",
  "leafUuid": "02500cc7-f3e9-4daf-b13f-4f528d329d2b",
  "sessionId": "f0b9fbaa-4159-4906-9e7b-5c7c38fdb4da"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "ai-title",
  "aiTitle": "Frozen WAM candidate selection via action latent OOD scoring",
  "sessionId": "f0b9fbaa-4159-4906-9e7b-5c7c38fdb4da"
}
```

---
