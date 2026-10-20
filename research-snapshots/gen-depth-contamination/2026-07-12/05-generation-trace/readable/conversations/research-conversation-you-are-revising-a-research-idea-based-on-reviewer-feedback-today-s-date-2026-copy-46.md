# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-10 (UTC).** ## Original idea { "tit

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-3/4e26c6f2-72e3-4741-87ef-c0d8359a2540.jsonl`
- **Structured JSON:** [`e92b499343b8f59d7751.json`](../../sessions/e9/e92b499343b8f59d7751.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T09:13:58.035Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T09:13:58.035Z",
  "sessionId": "4e26c6f2-72e3-4741-87ef-c0d8359a2540",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-10 (UTC).**\n\n## Original idea\n{\n  \"title\": \"Latent-Distribution Candidate Selection for Frozen World Action Models: OOD Consistency Scoring and Action-Latent Value Learning\",\n  \"core_problem\": \"Pretrained WAMs generate a single action trajectory at inference and provide no mechanism to compare candidate futures. Adding planning capability currently requires one of three costly interventions: (1) full fine-tuning of the video model on robot demos (Cosmos Policy, ICLR 2026: 384–3,072 H100-hours); (2) training a separate action-conditioned world model alongside the frozen policy (GPC, RAL 2025); or (3) architectural co-design or RL loops (H-WM, GigaBrain RAMP, WAV). Fast-WAM (arXiv 2603.16666) demonstrates that action-only inference achieves 97.6% on LIBERO (Table 2) and 91.8% on RoboTwin (Table 1) at 190ms, motivating candidate generation from frozen WAM action-only inference rather than expensive video rollouts.\\n\\nThe VLA test-time compute literature (2025–2026) has addressed candidate selection for VLA architectures: RoVer (arXiv 2510.10975, ICLR 2026) trains a 0.2B Process Reward Model; MG-Select (arXiv 2510.05681, ICLR 2026) uses KL-divergence from a masked unconditional VLA distribution as a training-free confidence signal, achieving 168% relative improvement on RoboCasa pick-and-place; Cosmos Policy (ICLR 2026) implements Best-of-N in its planning mode by generating B candidates and scoring each via a fine-tuned value function — but crucially, Cosmos Policy's authors report that a model trained only on demonstrations 'cannot correctly predict failure states' and that rollout fine-tuning is required to enable effective planning. KDPE (arXiv 2508.10511, CoRL 2025) applies kernel density estimation in Cartesian action space (end-effector position, orientation, gripper state) to filter Diffusion Policy trajectory outputs, achieving 88.2% vs. 85% average on RoboMimic/MimicGen — but critically, KDPE-OOD (selecting the most out-of-distribution trajectory) performed *worse* than KDPE (selecting the most typical), and KDPE uses all training demonstrations rather than a success-specific reference distribution. None of these approaches exploit WAMs' unique property: joint video-action pretraining that regularizes action latents z_a to be consistent with physically plausible visual futures, forming a success-biased latent distribution.\\n\\nThe central unanswered question — which VLA and Cartesian-space approaches cannot answer — is: (1) Do WAM action latents z_a, regularized by joint video-action pretraining, form a latent success distribution that is more structured and separable from failure regimes than VLA action tokens or Cartesian action representations, enabling lightweight OOD-based candidate scoring without any rollout data? (2) Is this latent OOD signal more informative than action-space distributional uncertainty (MG-Select's KL signal) or Cartesian-space density (KDPE) for candidate selection? These questions are grounded in the FAIL-Detect (arXiv 2503.08558, RSS 2025) finding that OOD detection on success-only demonstrations reliably identifies failures — but have not been applied to WAM action latents or to pre-execution candidate selection. The companion question of whether video denoising error (as opposed to latent OOD scoring) is a reliable zero-training signal is answered negatively by Cosmos Policy's own finding and by EVA (arXiv 2603.17808), which demonstrates an 'executability gap' showing that visual coherence does not predict task success.\\n\\nNo existing work demonstrates Best-of-N candidate selection using WAM action latents' distributional structure — either zero-training (OOD scoring) or lightweight-trained (value MLP) — without modifying any WAM weights or requiring rollout data for the zero-training path.\",\n  \"opportunity\": \"UWM's independent per-modality diffusion timestep architecture (RSS 2025) natively supports action-only inference (video timestep = T, action timestep = 0), producing action latents z_a jointly pretrained with video. This creates two complementary WAM-specific approaches to candidate selection, exploiting the distributional structure of the WAM's joint video-action pretraining:\\n\\n**Method 1 — Latent OOD Consistency Scoring (LOC, zero weight updates)**: Encode LIBERO-90 success demonstrations through frozen UWM in action-only mode to obtain a reference distribution {z_a^success}. Fit a lightweight density estimator — KNN-based nonconformity score (k=10) or Gaussian Mixture Model (k≤5 components) — on {z_a^success}. At inference, sample B=4–8 action-only candidates from frozen UWM, obtain latents {z_{a,1}, ..., z_{a,B}}, and score each: S_LOC(z_{a,i}) = −log p̂(z_{a,i}) (nonconformity score). Select a_{i*} = argmin_i S_LOC(z_{a,i}) (most in-distribution candidate). Total inference overhead: B × ~5ms = 20–40ms for B=4–8. Cost: ~30–60 minutes to fit density estimator on encoded latents; no WAM weight updates.\\n\\nTheoretical basis: (1) FAIL-Detect (RSS 2025) proves that OOD detection on success-only demonstration data reliably detects policy failures — the success-demo distribution implicitly excludes failure modes; (2) KDPE (CoRL 2025) demonstrates in Cartesian action space that selecting the most IN-distribution trajectory improves performance, while KDPE-OOD (selecting the most out-of-distribution trajectory) performs *worse* — validating the in-distribution selection direction for LOC; (3) z_a regularized by joint video-action pretraining encodes physical plausibility co-varying with video futures, creating a success-specific latent distribution with tighter quality-discriminative geometry than both Cartesian action space (KDPE) and VLA action tokens. LOC is WAM-specific in that this geometry is a direct consequence of joint video-action pretraining absent in VLAs and not present in action-space methods.\\n\\nKey differentiation from KDPE: (a) density estimation in WAM action latent space z_a, not Cartesian action space (position/orientation/gripper); (b) success-demonstrations-only reference distribution establishing a quality anchor, not all training data; (c) exploitation of WAM-specific joint pretraining regularization that aligns z_a with physical plausibility, unavailable in action-space methods; (d) B=4–8 candidates vs. KDPE's N=100, significantly cheaper inference. LOC implements success-mode selection; KDPE implements all-data-mode selection — these are mechanistically distinct quality signals.\\n\\nDifferentiation from MG-Select: LOC scores membership in the success demonstration distribution (latent OOD density); MG-Select measures KL divergence of task-conditioned output from masked unconditional distribution (action-space distributional uncertainty). One measures distributional membership relative to labeled success data, the other measures task-conditioning confidence.\\n\\nNote on Cosmos Policy planning mode: Cosmos Policy also implements Best-of-N — generates B actions, predicts future states and values, executes the highest-value action. However, (a) requires fine-tuning a value function on rollout data (1,536 H100-hours for RoboCasa) because demonstration-only training 'cannot correctly predict failure states'; (b) 15 total forward passes per candidate. LOC requires zero rollout data, zero weight updates, and ~5ms per candidate.\\n\\nNote on PCS: Video denoising error S_PCS = ||ε − ε_θ(x_{t*}, z_{a,i}, t*)||² is retained as a diagnostic comparison in Step 1, not as a primary method. Cosmos Policy's explicit finding and EVA's 'executability gap' provide strong prior evidence that denoising error is a weak candidate selection signal.\\n\\n**Method 2 — Action-Latent Value MLP (≤40 H100-hours training)**: A 3-layer MLP trained on WAM action latents z_a from LIBERO-90 success demonstrations AND explicitly collected failure trajectories scores each candidate via V(z_{a,i}) ∈ [0,1]. Hard argmax Best-of-N is the primary result. Key hypothesis: z_a regularized by joint video-action pretraining is more linearly separable between success and failure regimes than raw action outputs or VLA action tokens (the latent geometry argument). Failure demonstrations collected via frozen UWM rollouts in simulation (~15–20 H100-hours) plus Gaussian-perturbed synthetic failures (<1 H100-hour).\\n\\n**Comparison of LOC vs. Value MLP is itself a central contribution**: LOC requires zero training and no rollout data, but relies on the WAM's latent success distribution being well-separated from failure trajectories at inference; Value MLP requires failure demonstration collection but directly learns the task-specific quality function. Their empirical comparison characterizes when WAM latent OOD scoring is sufficient versus when labeled training adds necessary discriminative power — and whether this latent-space OOD approach outperforms action-space density estimation (KDPE-style) and distributional uncertainty (MG-Select-style KL).\\n\\n**Mandatory RoboCasa baseline validation before committing to targets**: World2Act (arXiv 2603.10422, March 2026) reports UWM achieving 60.8% on RoboCasa using 1,000 real demonstration fine-tuning. Since UWM was trained only on DROID data and has not been fine-tuned on RoboCasa tasks, the frozen UWM baseline (no RoboCasa demos) is expected to be substantially lower — likely 10–25%. Primary performance target: ≥10pp absolute improvement over the measured frozen baseline.\",\n  \"landscape\": \"Cosmos Policy (arXiv 2601.16163, ICLR 2026) is the primary comparison point for absolute performance. Fully fine-tunes Cosmos-Predict2-2B on robot demos (384 H100-hours ALOHA, 1,536 RoboCasa, 3,072 LIBERO). Achieves 98.5% LIBERO and 67.1% RoboCasa. Its planning mode implements Best-of-N candidate selection: generates B candidate actions, predicts future states (3 queries to world model) and values (5 queries to value function per future state, 15 total predictions per action), and executes via majority-mean aggregation. Key distinction: Cosmos Policy's authors explicitly state that demo-only training 'cannot correctly predict failure states' — rollout fine-tuning is required for the planning value function. LOC requires zero rollout data and zero weight updates; Value MLP requires ≤40 H100-hours vs. 1,536 H100-hours.\\n\\nKDPE (arXiv 2508.10511, CoRL 2025) — NEWLY ADDED. Applies kernel density estimation to Cartesian action trajectories (end-effector position, orientation via SO(3) Lie group logarithm map, gripper state) generated by Diffusion Policy to filter multimodal outputs. Generates N=100 candidates and selects the trajectory with highest density (most typical). Achieves 88.2% vs. 85% average on RoboMimic/MimicGen tasks; real-robot evaluation on PickPlush, CubeSort, CoffeeMaking. Critical finding: KDPE-OOD (selecting the *most out-of-distribution* trajectory) performed *worse* than standard KDPE (selecting most typical) — confirming that in-distribution selection direction is correct and that the quality of the reference distribution matters. LOC differs from KDPE in three fundamental ways: (a) density estimation in the WAM's action latent space z_a rather than Cartesian action space — the latent space is regularized by joint video-action pretraining to encode physical plausibility, a quality signal absent from Cartesian position/orientation; (b) success-demonstrations-only reference distribution rather than all training data — LOC anchors the reference to task success, not behavioral frequency; (c) exploitation of WAM-specific joint pretraining that structures z_a along physical plausibility dimensions unavailable in action-space-only density methods. Additionally, LOC uses B=4–8 candidates vs. KDPE's N=100, providing a practical inference-cost advantage.\\n\\nWorld2Act (arXiv 2603.10422, March 2026) — Achieves ~66% on RoboCasa (Cosmos Policy + World2Act) using only 50 real + 50 imagined demos. Method: aligns VLA action latents with world model video dynamics via a contrastive matching objective. Reports UWM achieves 60.8% on RoboCasa with 1,000-demo fine-tuning (confirming frozen UWM baseline is substantially lower). Differentiation: World2Act requires contrastive post-training to align VLA action latents with video dynamics (modifies weights); our LOC method requires zero post-training — the alignment is inherited from UWM's joint pretraining.\\n\\nFast-WAM (arXiv 2603.16666) is the critical framing reference. Action-only inference achieves 97.6% LIBERO-avg (Table 2) and 91.8% RoboTwin (Table 1) at 190ms latency. Generates a single action trajectory with no candidate comparison. Complementary framing: Fast-WAM targets latency-critical deployment (single trajectory, fastest); our method targets success-critical tasks (B trajectories, select best via latent scoring at B × 5ms overhead).\\n\\nRoVer (arXiv 2510.10975, ICLR 2026) — Generates B candidate actions from frozen VLAs, trains a 0.2B Process Reward Model that scores candidates AND predicts refinement directions. Differentiation: (1) RoVer requires training a 0.2B PRM on process labels; LOC requires zero training and Value MLP requires only a 3-layer MLP; (2) RoVer applies to VLA action tokens lacking video-physics regularization; our methods target WAM action latents z_a jointly trained with video.\\n\\nVerifier-free / MG-Select (arXiv 2510.05681, ICLR 2026) — Training-free Best-of-N using KL-divergence from masked unconditional VLA distribution. 168% relative improvement on RoboCasa pick-and-place. Differentiation: MG-Select measures distributional uncertainty (how much task conditioning shifts the distribution from its unconditional prior) — an action-space confidence signal. LOC measures latent OOD membership (whether z_{a,i} is in-distribution relative to success demonstrations) — a latent-space quality signal. Mechanistically distinct and directly compared in ablation grid.\\n\\nFAIL-Detect (arXiv 2503.08558, RSS 2025) — Frames failure detection as sequential OOD detection using conformal prediction on success-only demonstration data. Demonstrates that OOD detection trained only on successes reliably detects failures at execution time. LOC applies the same OOD detection principle to WAM action latents z_a for pre-execution candidate selection. LOC differs: (1) pre-execution selection vs. execution monitoring; (2) WAM-specific latent structure from joint video-action pretraining; (3) direct density estimation in action latent space vs. distilled scalar signal. FAIL-Detect is cited as motivating the principle; Step 1 LOC diagnostic is the first empirical test of whether this principle transfers to pre-execution WAM z_a scoring.\\n\\nEVA (arXiv 2603.17808, 2026) — Identifies 'executability gap': visually coherent rollouts can violate kinematic constraints. Supports LOC over PCS: visual denoising error does not imply executable actions, while action latent OOD is more directly quality-relevant.\\n\\nWAV: World-Value-Action Model (arXiv 2604.14732, April 2026) — Integrates a trajectory value module as a new architectural component trained from scratch; iterative latent-space inference concentrating probability mass on high-value trajectories. 99.6% LIBERO, 75.6% real-world dual-arm. Differentiation: WAV modifies the architecture and trains from scratch; our method leaves all WAM weights frozen. WAV is plug-in-incompatible with pretrained WAMs; our method is plug-in-compatible with any pretrained WAM.\\n\\nCompose Your Policies! / GPC (arXiv 2510.01068) — Training-free convex composition of multiple frozen policy distributions. Different: operates at distribution level (combining score functions of multiple policies), not discrete candidate selection from a single frozen WAM.\\n\\nGPC-RANK (arXiv 2502.00622, IEEE RAL 2025): frozen policy + separately trained action-conditioned world model + hard argmax. Our method uses the WAM's own action latent space as the evaluation substrate — no separate world model.\\n\\nWhen to Trust Imagination (arXiv 2605.06222, May 2026): FFDC adaptively decides action chunk sizes during single-trajectory execution. Orthogonal and combinable with our pre-execution selection.\",\n  \"approach\": \"Primary backbone: UWM (github.com/WEIRDLabUW/unified-world-model, RSS 2025), whose independent per-modality diffusion timestep architecture supports action-only inference (policy mode: video timestep = T, action timestep = 0). All WAM weights frozen throughout.\\n\\n**Step 0a — Frozen UWM Baseline Validation on RoboCasa (MANDATORY FIRST STEP)**: Run B=1 frozen UWM action-only inference on 50 episodes of representative RoboCasa tasks (kitchen manipulation subset). Expected baseline: 10–25% (UWM trained on DROID data only; World2Act reports 60.8% with 1,000-demo fine-tuning, confirming frozen baseline is substantially lower). Decision tree: if baseline ≥ 30%, proceed with current framing; if baseline 10–25%, confirm ≥10pp absolute improvement framing. Cost: ~2–3 H100-hours.\\n\\n**Step 0b — Reference Distribution Encoding for LOC**: Encode LIBERO-90 success demos through frozen UWM in action-only mode to obtain {z_a^success}. Fit density estimators: (a) KNN nonconformity model (k=10, Euclidean distance); (b) GMM (k=3,5 components, full covariance). Split latents 80/20 train/hold-out for AUC evaluation in Step 1. Cost: ~10–15 H100-hours encoding; ~30 minutes fitting density estimator. Steps 0b and 0c can run in parallel after Step 0a completes.\\n\\n**Step 0c — Failure Demonstration Collection (required for Value MLP)**: (a) Primary negatives: run frozen UWM (B=1) on LIBERO-Long and validated RoboCasa tasks; expected failure rate 30–50% on RoboCasa tasks, 5–15% on LIBERO-Long, yielding 500–2,000 failure trajectories. Cost: 15–20 H100-hours. (b) Synthetic supplement: Gaussian action perturbation (σ ∈ {0.05, 0.1}) on 20% of LIBERO-90 success demos, simulate in MuJoCo, flag truncated episodes as failures. Cost: <1 H100-hour. Combined: balanced 2,000–4,000 positive / 2,000–4,000 negative training set.\\n\\n**Step 1 — LOC Diagnostic (MANDATORY before main ablation)**: Empirically tests Hypothesis H1: 'WAM joint pretraining creates a latent success distribution where S_LOC(z_a) achieves AUC > 0.60 as a binary success predictor.' This hypothesis is motivated by FAIL-Detect's principle and KDPE's finding that in-distribution selection outperforms out-of-distribution selection in action space — but Step 1 is the first empirical test of whether WAM z_a, generated via action-only inference (not execution-time monitoring as in FAIL-Detect), shows the same property in the action latent space.\\n\\nProtocol: Sample B=16 action-only candidates from frozen UWM on 3 RoboCasa tasks, execute each in simulation (ground-truth success/failure), compute LOC and PCS scores.\\n\\nLOC metrics: (1) AUC of S_LOC as binary success predictor on held-out demos (target AUC > 0.60); (2) Spearman ρ of S_LOC with success labels (target ρ > 0.3); (3) compare KNN vs. GMM density estimators. Also compute S_PCS = ||ε − ε_θ(x_{t*}, z_{a,i}, t*)||² for the same candidates, varying t* ∈ {T/4, T/2, 3T/4} — expected to show lower AUC and ρ than LOC based on Cosmos Policy finding and EVA's executability gap evidence. Also compute MG-Select-style KL score as third comparison signal.\\n\\nExpected result: LOC AUC > PCS AUC ≈ MG-Select AUC, confirming latent OOD density is more informative than video denoising error or action-space distributional uncertainty.\\n\\nDecision tree for LOC: if AUC ≥ 0.60, LOC is reported as primary zero-training method; if LOC 0.55–0.60, both methods reported with LOC as secondary; if LOC < 0.55, LOC reported as negative result with informative comparison.\\n\\nThis diagnostic is itself a key scientific contribution: it empirically tests whether WAM joint pretraining creates a success latent distribution that is more quality-discriminative than video denoising error, distributional uncertainty, or action-space density (KDPE's domain).\\n\\n**Step 2 — Diversity Pilot (combined with LOC diagnostic)**: Same B=16 rollouts measure: pairwise cosine distance of action latents {z_{a,i}} (target mean > 0.05; if lower, increase noise temperature T_noise ∈ {1.5, 2.0}); LOC AUC conditional on latent diversity. Binary classification accuracy on held-out demo set as latent separability sanity check.\\n\\n**Step 3 — Value MLP Training**: 3-layer MLP (input: flattened z_a; output: scalar V ∈ [0,1]) trained via binary cross-entropy on balanced success/failure latents from Steps 0b and 0c. Report binary classification accuracy on held-out split (target > 75%). Cost: ~3–5 H100-hours.\\n\\n**Step 4 — Inference-Time Best-of-N Planning**: At each planning step, sample B=4–8 action-only trajectories from frozen UWM.\\n\\nPrimary results (two methods):\\n- LOC selection: a_{i*} = argmin_i S_LOC(z_{a,i}) at best density estimator from diagnostic [zero weight updates, WAM-specific]\\n- Value MLP selection: a_{i*} = argmax_i V(z_{a,i}) [lightweight training, WAM-specific]\\n\\nComparisons (required): MG-Select-style KL scoring applied to WAM action-only inference; random selection (B=4–8, sanity check); single-trajectory WAM B=1 (frozen baseline).\\n\\nAblation (secondary): (a) PCS denoising error selection at best t* from diagnostic (expected to underperform LOC); (b) soft MPPI w_i ∝ exp(β·V(z_{a,i})) to document action-averaging artifact; (c) action-only z_a vs. full video+action latent for LOC and Value MLP scoring.\\n\\n**Ablation Grid**: B ∈ {1, 4, 8} (B=1 is frozen WAM single-trajectory baseline); selection method: LOC KNN vs. LOC GMM (primary zero-training) vs. Value MLP hard argmax (primary trained) vs. MG-Select-style KL (VLA method applied to WAM, key comparison) vs. random selection (sanity check); T_noise fixed at 1.0 in primary ablation (1.5, 2.0 variants run in human-in-loop follow-up if diversity pilot shows issues); execution regime: (a) open-loop vs. (b) periodic replanning every K=5 action chunks.\\n\\n**Primary hypotheses**: (H1, tested in Step 1 LOC diagnostic) LOC achieves Spearman ρ > 0.3 and AUC > 0.6, confirming WAM success latents form an OOD-detectable distribution — this hypothesis is motivated but unproven; Step 1 is the first empirical test; (H2) LOC outperforms PCS and MG-Select-style KL in the diagnostic, with PCS showing AUC near 0.5 consistent with Cosmos Policy's finding; (H3) Value MLP achieves ≥10pp improvement over B=1 baseline on RoboCasa; (H4) LOC achieves ≥5pp improvement over B=1 with zero weight updates; (H5) Both methods outperform MG-Select-style KL applied to WAM and outperform KDPE-style Cartesian density applied to WAM outputs, confirming latent quality-discrimination advantages of WAM joint pretraining.\\n\\n**Standalone Value MLP contribution (applicable if LOC fails H1)**: If LOC AUC < 0.55 in the diagnostic, the paper's narrative shifts to Value MLP as the primary contribution with the following independent novelty argument: (a) vs. WAV — WAV trains a trajectory value module as a new architectural component from scratch, requiring architectural co-design; Value MLP is plug-in-compatible with any pretrained WAM, requiring only 3-layer MLP training on existing latent representations; (b) vs. RoVer — RoVer requires a 0.2B PRM trained on process labels; Value MLP uses a 3-layer MLP trained on binary success/failure labels; RoVer targets VLA action tokens lacking video-physics regularization, while Value MLP exploits WAM z_a's joint-pretraining geometry; (c) vs. Cosmos Policy — requires 1,536 H100-hours rollout fine-tuning; Value MLP requires ≤40 H100-hours; (d) vs. KDPE — KDPE operates in Cartesian action space with all training data; Value MLP uses WAM latent space with success/failure-labeled data; the central empirical claim becomes 'joint pretraining creates a latent space where success/failure are more linearly separable than in Cartesian action space, enabling a 3-layer MLP to achieve discriminative performance that requires larger models on VLA action tokens.' This standalone narrative is complete and does not depend on LOC succeeding.\\n\\n**Evaluation Benchmarks**: (a) Primary — RoboCasa: Cosmos Policy fine-tuned 67.1%; World2Act (Cosmos+World2Act) ~66%; frozen UWM expected 10–25% (validated in Step 0a); absolute target ≥10pp over frozen baseline. (b) Secondary — LIBERO-Long: near saturation for strong frozen WAMs (Fast-WAM 95.2%, Table 2); included to characterize gain profile vs. task difficulty. (c) Baselines: B=1 frozen WAM, random selection, MG-Select-style KL applied to WAM.\\n\\nDreamZero cross-WAM validation deferred to camera-ready. CoRL submission rests on UWM alone.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~140h H100\",\n      \"gpu_utilization\": \"HIGH idle (~35–55%): GPU waits while researcher implements LOC density estimator (KNN/GMM fitting), interprets LOC diagnostic results, debugs failure collection pipeline, and designs ablations.\",\n      \"timeline\": \"2–3 months\",\n      \"team\": \"1–2 researchers\",\n      \"estimated_gpu_cost\": \"~$350 (140h × $2.50/h blended Lambda/RunPod/Vast.ai H100 rate)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~165h H100\",\n      \"gpu_utilization\": \"MODERATE idle (~20–30%): agent handles code scaffolding, baseline validation, LOC diagnostic, failure collection, demo encoding, density estimator fitting, and experiment submission; human reviews Step 0a baseline and LOC diagnostic results at daily check-ins to make go/no-go decisions\",\n      \"timeline\": \"3–4 weeks\",\n      \"team\": \"1 researcher, ~30 min/day check-in\",\n      \"claude_api_cost\": \"$150–250 (~1,500–2,500 turns at mixed Sonnet/Opus rates)\",\n      \"estimated_gpu_cost\": \"~$413 (165h × $2.50/h)\",\n      \"risk_note\": \"Step 0a (frozen UWM RoboCasa baseline) and LOC diagnostic are hard sequential dependencies before main ablation. Sequential order: 0a baseline validation (2–3 H100-hours, Day 1–2) → LOC diagnostic (3–5 H100-hours, Day 2–4) → failure collection (15–20 H100-hours, Day 3–7, parallel with LOC) → demo encoding + density fitting (10–15 H100-hours, Day 5–9) → Value MLP training (3–5 H100-hours, Day 9–10) → main ablations (Day 10–18). RoboCasa simulation setup requires separate engineering effort from LIBERO. DreamZero cross-WAM deferred to camera-ready.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~185h H100 (revised from prior 320h estimate; ablation grid pruned to stay within ≤200h hard constraint)\",\n      \"gpu_budget_breakdown\": \"Step 0a frozen UWM baseline: ~3h; Steps 0b+0c in parallel (demo encoding + failure collection): ~32h billed (12h encoding + 20h failure collection running concurrently); Step 1 LOC diagnostic: ~4h; Step 3 Value MLP training: ~5h; Main ablation grid (B ∈ {1,4,8} × 5 methods × 3 seeds × 2 benchmarks = 90 runs × ~1.2h avg): ~108h; contingency/reruns: ~13h. Total: ~165h billed GPU-hours. With 4 GPUs running ablation batch concurrently: wall-clock ≈ 44h setup + 27h ablations = 71h wall-clock; billed = 44×1 + 27×4 = 152h billed. With overhead/reruns: ~180–190h billed GPU-hours ≤ 200h hard constraint.\",\n      \"gpu_utilization\": \"MINIMAL idle (~5–10%): agent pipelines baseline validation, LOC diagnostic, failure collection, demo encoding, density fitting, MLP training, and evaluation continuously.\",\n      \"timeline\": \"7–10 days with 4 H100 GPUs simultaneously\",\n      \"team\": \"0 (only initial repo setup and credential configuration)\",\n      \"claude_api_cost\": \"$200–350 (~2,500–4,000 turns at Opus rates)\",\n      \"estimated_gpu_cost\": \"~$463 (185h × $2.50/h)\",\n      \"ablation_grid_vs_prior\": \"Pruned from prior estimate: T_noise sweep ({1.0,1.5,2.0}) dropped from auto research grid — T_noise fixed at 1.0 unless diversity pilot (Step 2) shows mean cosine distance < 0.05, in which case T_noise=1.5 is tested in human-in-loop follow-up. B grid reduced from {1,2,4,8,16} to {1,4,8} (drop B=2 and B=16 as extreme values). PCS full ablation dropped from auto grid (retained only in Step 1 LOC diagnostic). These prunings reduce ablation runs from ~150 to ~90, bringing billed GPU-hours within the 200h hard constraint.\",\n      \"speed_bottleneck\": \"Step 0a baseline validation → LOC diagnostic → (parallel: failure collection + demo encoding) → density fitting (trivial) + Value MLP training is a 5-step sequential dependency spanning ~8 days minimum. RoboCasa evaluation rollouts: each ablation variant requires sequential per-task evaluation; with 4 GPUs running 4 variants concurrently, the full grid needs ~5–7 days.\",\n      \"risk_note\": \"LOC density estimation (KNN/GMM) is a standard sklearn/torch operation requiring no custom implementation. Main implementation risk: UWM action latent extraction in action-only mode (video timestep = T, action timestep = 0) — this mode is supported by UWM's architecture but may require engineering to extract z_a as a fixed-size vector for density estimation. If z_a is not directly accessible, the Action Decoder intermediate activations serve as a substitute latent representation.\"\n    }\n  },\n  \"target_venues\": [\n    \"CoRL 2026 (Abstract deadline: May 26, 2026; Full paper: May 29, 2026; Conference: Nov 9–12, Austin TX) — TIGHT but viable: 19 days from 2026-05-10. Step 0a RoboCasa baseline must run immediately (Day 1–2). Minimum viable submission: frozen UWM RoboCasa baseline validation + LOC diagnostic figure (including PCS comparison showing expected negative result) + LOC and/or Value MLP Best-of-N results (primary) + LIBERO-Long (secondary) + B/hard-argmax ablation + MG-Select-style KL baseline comparison. DreamZero cross-WAM deferred to camera-ready.\",\n    \"ICLR 2027 (deadline ~September–October 2026) — More feasible timeline for complete ablation grid, latent geometry analysis (success/failure separation in WAM vs. VLA latent spaces), DreamZero cross-WAM evaluation, and potential real-world experiments.\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning (arXiv 2601.16163, ICLR 2026) — CRITICAL PRIOR WORK: implements Best-of-N planning mode (15 forward passes per action via majority-mean aggregation of world model + value function queries); requires rollout fine-tuning because demo-only training 'cannot correctly predict failure states'; 1,536 H100-hours for RoboCasa; 98.5% LIBERO, 67.1% RoboCasa; our LOC requires zero rollout data and zero weight updates\",\n    \"KDPE: A Kernel Density Estimation Strategy for Diffusion Policy Trajectory Selection (arXiv 2508.10511, CoRL 2025) — NEWLY ADDED CRITICAL PRIOR WORK: applies manifold-aware KDE to Cartesian action trajectories (end-effector position/SO(3)-orientation/gripper) from Diffusion Policy; generates N=100 candidates; achieves 88.2% vs. 85% on RoboMimic/MimicGen; CRITICAL FINDING: KDPE-OOD (selecting most out-of-distribution trajectory) performs WORSE than KDPE (selecting most typical) — validates in-distribution selection direction for LOC; differentiates from LOC: (a) Cartesian action space vs. WAM action latent space; (b) all training data vs. success-only reference; (c) no WAM-specific joint pretraining regularization; (d) N=100 candidates vs. LOC's B=4–8\",\n    \"World2Act (arXiv 2603.10422, March 2026) — post-training framework achieving ~66% on RoboCasa using 50 real + 50 imagined demos; reports UWM achieves 60.8% on RoboCasa with 1,000-demo fine-tuning (confirming frozen UWM baseline is ~10–25%); differentiation: World2Act requires contrastive post-training to align VLA latents; LOC exploits WAM alignment inherited from joint pretraining\",\n    \"Fast-WAM: World Action Models without Test-Time Video (arXiv 2603.16666) — CRITICAL FRAMING: 97.6% LIBERO-avg (Table 2) and 91.8% RoboTwin (Table 1) at 190ms without video; single trajectory only; our method uses same action-only inference for candidate generation and adds LOC selection at B × 5ms overhead\",\n    \"FAIL-Detect: Failure Detection as OOD Detection for Robot Manipulation (arXiv 2503.08558, RSS 2025) — SUPPORTING WORK: proves OOD detection on success-only demonstration data reliably detects policy failures; uses flow-based density estimation on distilled policy signals; motivates LOC's use of KNN/GMM density on success demo latents; FAIL-Detect is execution-time monitoring, LOC is pre-execution candidate selection from a different inference mode — Step 1 LOC diagnostic is the first empirical test of whether this principle transfers to pre-execution WAM z_a\",\n    \"EVA: Aligning Video World Models with Executability (arXiv 2603.17808, 2026) — identifies 'executability gap' showing visually coherent world model rollouts can violate kinematic constraints; supports LOC over PCS: visual denoising error does not predict task success\",\n    \"RoVer: Robot Reward Model as Test-Time Verifier for Vision-Language-Action Models (arXiv 2510.10975, ICLR 2026) — CRITICAL PRIOR WORK: generates B VLA candidates, trains 0.2B PRM; differentiation: requires 0.2B model training vs. LOC's zero training and Value MLP's 3-layer MLP; VLA action tokens lack video-physics regularization\",\n    \"Verifier-free Test-Time Sampling / MG-Select (arXiv 2510.05681, ICLR 2026) — CRITICAL PRIOR WORK: training-free KL-from-masked-distribution scoring for frozen VLAs; 168% relative improvement on RoboCasa pick-and-place; differentiation: MG-Select measures action-space distributional uncertainty, LOC measures latent OOD membership relative to success demo distribution\",\n    \"World-Value-Action (WAV) Model (arXiv 2604.14732, April 2026) — trajectory value module requiring training from scratch, new architectural component; 99.6% LIBERO, 75.6% real-world; our method leaves all WAM weights frozen and is plug-in-compatible with pretrained WAMs; WAV requires architectural co-design\",\n    \"Compose Your Policies! / GPC (arXiv 2510.01068) — training-free distribution composition for multiple frozen policies; operates at distribution level, not discrete candidate selection from single WAM\",\n    \"Inference-Time Enhancement / GPC-RANK (arXiv 2502.00622, IEEE RAL 2025) — frozen policy + separately trained world model + hard argmax; our method uses WAM's own action latent space, no separate world model\",\n    \"Unified World Models / UWM (arXiv 2504.02792, RSS 2025) — primary backbone; independent per-modality timesteps support action-only inference; publicly available weights and code\",\n    \"Diffusion Policy (arXiv 2303.04137, RSS 2023 / IJRR 2024) — documents multi-modal action distribution handling; confirms averaging over manipulation action modes produces infeasible blended actions; justifies hard argmax over soft MPPI weighting\",\n    \"When to Trust Imagination (arXiv 2605.06222, May 2026) — CONCURRENT WORK: FFDC adaptively decides action chunk sizes; orthogonal to our pre-execution selection; combinable\",\n    \"World Action Models as Zero-shot Policies / DreamZero (arXiv 2602.15922) — 14B joint video+action DiT; secondary backbone for cross-WAM validation in camera-ready/ICLR version\",\n    \"OA-WAM (arXiv 2605.06481, May 2026) — concurrent work; different problem (object binding)\",\n    \"CKT-WAM (arXiv 2605.06247, May 2026) — concurrent work; different problem (cross-WAM knowledge transfer)\",\n    \"GigaBrain-0.5M* (arXiv 2602.12099) — RAMP RL loop requires 30%+ more training\",\n    \"H-WM (arXiv 2602.11291) — requires hierarchical architectural co-design\",\n    \"Latent Diffusion Planning (arXiv 2504.16925) — trains diffusion planner from scratch\"\n  ],\n  \"description\": \"Latent-Distribution Candidate Selection (LDCS) converts any pretrained video-diffusion World Action Model into a multi-candidate planner at inference time without modifying any WAM weight, exploiting WAM-specific latent structure through two complementary methods.\\n\\nThe key insight: Cosmos Policy's own finding that demonstration-trained video priors 'cannot correctly predict failure states' — and EVA's demonstration of an 'executability gap' — rules out video denoising error as a reliable zero-training quality signal. KDPE (CoRL 2025) demonstrates that density-based candidate selection in Cartesian action space improves performance, but critically, KDPE-OOD (selecting the most out-of-distribution trajectory) performs *worse* — confirming that the quality of the reference distribution matters and that in-distribution selection is the correct direction. LOC extends this principle into the WAM's action latent space using a success-only reference distribution, exploiting WAM-specific joint pretraining geometry unavailable to action-space-only methods.\\n\\n**Hypothesis H1 (tested empirically in Step 1 LOC diagnostic)**: WAM joint video-action pretraining regularizes z_a along physical plausibility dimensions, creating a success latent distribution where S_LOC(z_a) achieves AUC > 0.60 as a binary success predictor — more discriminative than video denoising error (PCS), action-space distributional uncertainty (MG-Select-style KL), and Cartesian-space density (KDPE). This hypothesis is motivated by FAIL-Detect's principle (OOD on success-only data detects failures) and KDPE's empirical confirmation (in-distribution selection outperforms outlier selection), but Step 1 is the first empirical test on pre-execution WAM z_a. If H1 fails (AUC < 0.55), LOC is reported as a negative result and Value MLP becomes the sole primary contribution.\\n\\n**Method 1 — Latent OOD Consistency Scoring (LOC, zero weight updates)**: Fit a KNN or GMM density estimator on WAM action latents {z_a^success} from LIBERO-90 success demos. At inference, sample B=4–8 action-only candidates and score each by nonconformity: S_LOC(z_{a,i}) = −log p̂(z_{a,i}). Select argmin (most in-distribution candidate). Overhead: B × ~5ms = 20–40ms for B=4–8.\\n\\nDifferentiated from KDPE: (a) action latent space z_a regularized by joint video-action pretraining, not Cartesian action space; (b) success-demonstrations-only reference distribution anchored to task quality, not all training data; (c) B=4–8 vs. KDPE's N=100. Differentiated from MG-Select: LOC scores latent OOD membership relative to labeled success data; MG-Select scores action-space distributional uncertainty from unconditional prior.\\n\\n**Method 2 — Action-Latent Value MLP (≤40 H100-hours)**: 3-layer MLP trained on {z_a^success} and explicitly collected failure latents. Hard argmax selection avoids multi-modal action-averaging artifact. Central hypothesis: joint pretraining geometry makes z_a more linearly separable between success/failure regimes than VLA action tokens or Cartesian representations. Standalone contribution if LOC fails: (a) plug-in-compatible with pretrained WAMs (vs. WAV's from-scratch architectural co-design); (b) 3-layer MLP (vs. RoVer's 0.2B PRM); (c) ≤40 H100-hours (vs. Cosmos Policy's 1,536 H100-hours rollout fine-tuning); (d) operates in WAM latent space regularized by joint pretraining (vs. KDPE's Cartesian space).\\n\\n**LOC Diagnostic (mandatory, Step 1)**: B=16 rollouts on 3 RoboCasa tasks, measuring AUC of S_LOC as binary success predictor (target H1: AUC > 0.6), compared against: (a) video denoising error S_PCS (expected negative result), (b) MG-Select-style KL applied to WAM, (c) KDPE-style Cartesian density as reference baseline.\\n\\nPrimary evaluation: RoboCasa (target ≥10pp absolute over frozen baseline; Cosmos Policy 67.1% / World2Act ~66% as upper references). Secondary: LIBERO-Long. Auto research ablation grid pruned to B ∈ {1,4,8} × 5 methods × 3 seeds × 2 benchmarks (~185 billed H100-hours ≤ 200h hard constraint). CoRL submission: UWM only; DreamZero cross-WAM deferred to camera-ready.\",\n  \"project_name\": \"frozen_wam_mppi\",\n  \"source\": \"web_research\"\n}\n\n## Reviewer feedback (round 6)\nIssues: [\"SIGNIFICANT — V-GPS (arXiv 2410.13816, 'Value-Guided Inference-Time Policy Steering', October 2024) is absent from the landscape and directly overlaps with the Value MLP method. V-GPS uses an offline RL-learned value function to re-rank B candidate actions from frozen generalist policies (Octo, RT-1X, OpenVLA), achieving +82.8% absolute real-world improvement. This is mechanistically identical to Value MLP at the paradigm level. The submission must cite V-GPS and differentiate: 'V-GPS trains a value function via offline RL on raw action representations from VLA action tokens lacking video-physics regularization; our Value MLP uses binary success/failure supervision on WAM z_a from joint video-action pretraining, which we hypothesize is more linearly separable between success/failure regimes than VLA action token representations. V-GPS demonstrates the paradigm works for VLAs; we ask whether WAM-specific latent geometry provides additional discriminative power.' This is the clearest gap remaining after 6 rounds.\", \"SIGNIFICANT — WAV performance numbers (99.6% LIBERO, 75.6% real-world) appear unverifiable and potentially incorrect. Independent verification of arXiv 2604.14732 found LIBERO overall average score of 98.1 (not 99.6%) and no 75.6% real-world figure in accessible content. If the Generator is citing wrong WAV metrics, this undermines the differentiation story and will be flagged by CoRL reviewers. Fetch the WAV paper PDF directly and correct the stated metrics with table references.\", \"MODERATE — The theoretical argument that UWM z_a in action-only mode (video timestep=T) retains video-physics regularization from joint training needs explicit acknowledgment of the inference-time tension. In action-only inference, video tokens are at full noise (T), meaning no video information conditions z_a at inference time. The current framing states z_a is 'regularized by joint video-action pretraining to encode physical plausibility' without clarifying this is a training-time property whose inference-time persistence is unproven. Revise to: 'We hypothesize that joint training causes z_a to learn quality-discriminative representations even when video is absent at inference time — tested empirically in Step 1. If this property does not transfer (AUC < 0.55), LOC reports a negative result and Value MLP becomes the primary contribution.'\", \"MODERATE — ALT Policy ('Demystifying Diffusion Policies via Action Lookup Tables', arXiv 2505.05787, May 2025) and UNISafe (arXiv 2505.00779, May 2025) should be briefly cited as adjacent work in the related work section. ALT Policy uses nearest-neighbor OOD detection in action latent space for frozen diffusion policies (different domain: observation latents for retrieval, not action latents for candidate scoring). UNISafe uses conformal prediction + world model uncertainty for OOD-based action filtering (different application: safety, not candidate selection). A single sentence each in related work suffices: these papers are distinct from LOC but demonstrate that latent-space OOD detection for robot policies is a published direction.\", \"MODERATE — Expected absolute RoboCasa performance (~20-35% after ≥10pp improvement from 10-25% frozen baseline) needs proactive framing against fine-tuned baselines. CoRL reviewers will note that Cosmos Policy achieves 67.1% and World2Act ~66%, making 20-35% look weak. Add one paragraph explicitly framing this: 'Our methods are orthogonal to fine-tuning — they extract planning value from existing pretrained WAMs in settings where domain-specific demonstration data is unavailable. The comparison target is B=1 frozen WAM inference, not fine-tuned models; we improve over the no-adaptation baseline by ≥10pp without any weight updates or rollout data collection.' This reframing prevents reviewers from misreading the target.\"]\nFeedback: Round 6 has closed all Round 5 issues (KDPE cited with strong differentiation, Fast-WAM numbers verified and table-referenced, auto research budget correctly computed to 152-185h billed ≤ 200h, LOC hypothesis framed as H1 with diagnostic gate, standalone Value MLP fallback narrative ready). Two new issues were found through independent search that require fixes before submission:\n\n**1. Add V-GPS (arXiv 2410.13816) to related work — 1 day.** V-GPS (October 2024) uses a learned value function to re-rank B candidates from frozen generalist policies on real robot tasks (+82.8% improvement). It is paradigmatically identical to Value MLP at the method level. Write in related work: 'V-GPS (2024) learns an offline RL value function to score and re-rank B candidate actions from frozen VLAs (Octo, RT-1X, OpenVLA), achieving +82.8% real-world improvement. Our Value MLP applies the same paradigm to WAM action latents z_a — specifically, we ask whether WAM-specific joint video-action pretraining creates a latent geometry where success/failure are more linearly separable than in VLA action token space, enabling a 3-layer MLP to match or exceed the discriminative power that V-GPS achieves via offline RL.' This turns a missing citation into a positive framing.\n\n**2. Verify and correct WAV metrics — 0.5 day.** Fetch the WAV paper PDF and find the exact LIBERO and real-world numbers with table references. If the LIBERO number is 98.1 (not 99.6%) and the real-world number differs from 75.6%, correct the manuscript. Citing wrong numbers for a concurrent paper will be caught in review.\n\n**3. Clarify the action-only mode z_a argument — 0.5 day.** The theoretical framing says z_a is 'regularized by joint pretraining to encode physical plausibility' — this is a training-time property. Add one sentence: 'In action-only inference, video tokens are at full noise (timestep T) and provide no inference-time conditioning; we hypothesize that the training-time alignment between z_a and video dynamics persists as a latent geometry property even without video input — which Step 1 empirically tests.' This makes the theoretical argument accurate and shows scientific awareness.\n\nWith these three fixes (2 days total), the paper is ready for CoRL submission. Minimum viable submission scope is correctly identified: frozen UWM RoboCasa baseline + LOC diagnostic (H1 test) + LOC and/or Value MLP Best-of-N results + LIBERO-Long secondary + B/hard-argmax ablation + MG-Select-style KL baseline comparison. DreamZero cross-WAM deferred to camera-ready is the right call.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.\n- Address each issue specifically.\n\n## 深度调研要求（每一轮修订都必须执行）\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。\n   - 搜索最新的相关论文（arXiv, conference proceedings）\n   - 搜索 benchmark/leaderboard 确认当前 SOTA\n   - 搜索可能遗漏的相关工作和 concurrent work\n\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，\n   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。\n\n3. **深度思考**：在修订之前，先独立思考以下问题：\n   - 这个 idea 的核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach 来解决同一个核心问题？\n   - 修订后的 idea 相比上一版有什么本质性的改进？\n\n4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，\n   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。\n\n## 针对 Review 意见的定向搜索\n\n对 reviewer 指出的每个问题，执行以下搜索流程：\n\n1. **如果 reviewer 说'已有类似工作'**：\n   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读\n   - 搜索该论文的 cited-by，找到后续跟进工作\n   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot\n\n2. **如果 reviewer 说'SOTA 过时'**：\n   - 用 Papers With Code 查看当前排行榜\n   - 搜索过去 6 个月的最新方法\n   - 更新你的 landscape 和 baseline\n\n3. **如果 reviewer 说'可行性有问题'**：\n   - 搜索类似规模实验的实际成本和时间线\n   - 搜索 GitHub 上是否有可复用的实现\n   - 搜索相关数据集/模型的可获取性\n\n4. **如果 reviewer 说'novelty 不足'**：\n   - 对核心方法尽量做 3-5 种不同关键词组合的搜索\n   - 搜索相邻领域是否有类似思路\n   - 如果确实 novelty 不足，考虑 major revision 或 pivot\n\n- Use WebSearch to find updated information if the reviewer flagged outdated claims.\n- You have full freedom in how much to change:\n  - Minor fix: if only specific details are wrong, correct them and keep everything else.\n  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.\n  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.\n- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.\n- In the output JSON, include a \"change_type\" field with one of: \"minor\", \"major\", or \"pivot\" to indicate the scope of your changes.\n- Output the revised idea as a COMPLETE JSON object (same schema as original, plus \"change_type\").\n\n## 停滞提醒\n这个 idea 已经经过 6 轮修订，近 3 轮的平均分从 3.2 到 3.2，没有明显改善。\n\n请认真思考：\n- 当前方向是否存在根本性的瓶颈？反复的 minor fix 是否在回避核心问题？\n- 如果你认为问题出在 approach 而非 framing，可以做 major revision。\n- 如果你认为 core problem 本身就有问题（gap 不存在、问题不够重要），pivot 到同一研究领域下的新方向可能是更好的选择。\n- 当然，如果你有信心这一轮修订能实现突破，继续改进也完全可以。\n\n最终由你判断——做你认为最能提升 idea 质量的选择。"
}
```

---

### Runtime record

_source line 2 · 2026-05-10T09:13:58.040Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T09:13:58.040Z",
  "sessionId": "4e26c6f2-72e3-4741-87ef-c0d8359a2540"
}
```

---

## Round 1

35 recorded events

### User

_source line 3 · 2026-05-10T09:13:58.079Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-10 (UTC).**

## Original idea
{
  "title": "Latent-Distribution Candidate Selection for Frozen World Action Models: OOD Consistency Scoring and Action-Latent Value Learning",
  "core_problem": "Pretrained WAMs generate a single action trajectory at inference and provide no mechanism to compare candidate futures. Adding planning capability currently requires one of three costly interventions: (1) full fine-tuning of the video model on robot demos (Cosmos Policy, ICLR 2026: 384–3,072 H100-hours); (2) training a separate action-conditioned world model alongside the frozen policy (GPC, RAL 2025); or (3) architectural co-design or RL loops (H-WM, GigaBrain RAMP, WAV). Fast-WAM (arXiv 2603.16666) demonstrates that action-only inference achieves 97.6% on LIBERO (Table 2) and 91.8% on RoboTwin (Table 1) at 190ms, motivating candidate generation from frozen WAM action-only inference rather than expensive video rollouts.\n\nThe VLA test-time compute literature (2025–2026) has addressed candidate selection for VLA architectures: RoVer (arXiv 2510.10975, ICLR 2026) trains a 0.2B Process Reward Model; MG-Select (arXiv 2510.05681, ICLR 2026) uses KL-divergence from a masked unconditional VLA distribution as a training-free confidence signal, achieving 168% relative improvement on RoboCasa pick-and-place; Cosmos Policy (ICLR 2026) implements Best-of-N in its planning mode by generating B candidates and scoring each via a fine-tuned value function — but crucially, Cosmos Policy's authors report that a model trained only on demonstrations 'cannot correctly predict failure states' and that rollout fine-tuning is required to enable effective planning. KDPE (arXiv 2508.10511, CoRL 2025) applies kernel density estimation in Cartesian action space (end-effector position, orientation, gripper state) to filter Diffusion Policy trajectory outputs, achieving 88.2% vs. 85% average on RoboMimic/MimicGen — but critically, KDPE-OOD (selecting the most out-of-distribution trajectory) performed *worse* than KDPE (selecting the most typical), and KDPE uses all training demonstrations rather than a success-specific reference distribution. None of these approaches exploit WAMs' unique property: joint video-action pretraining that regularizes action latents z_a to be consistent with physically plausible visual futures, forming a success-biased latent distribution.\n\nThe central unanswered question — which VLA and Cartesian-space approaches cannot answer — is: (1) Do WAM action latents z_a, regularized by joint video-action pretraining, form a latent success distribution that is more structured and separable from failure regimes than VLA action tokens or Cartesian action representations, enabling lightweight OOD-based candidate scoring without any rollout data? (2) Is this latent OOD signal more informative than action-space distributional uncertainty (MG-Select's KL signal) or Cartesian-space density (KDPE) for candidate selection? These questions are grounded in the FAIL-Detect (arXiv 2503.08558, RSS 2025) finding that OOD detection on success-only demonstrations reliably identifies failures — but have not been applied to WAM action latents or to pre-execution candidate selection. The companion question of whether video denoising error (as opposed to latent OOD scoring) is a reliable zero-training signal is answered negatively by Cosmos Policy's own finding and by EVA (arXiv 2603.17808), which demonstrates an 'executability gap' showing that visual coherence does not predict task success.\n\nNo existing work demonstrates Best-of-N candidate selection using WAM action latents' distributional structure — either zero-training (OOD scoring) or lightweight-trained (value MLP) — without modifying any WAM weights or requiring rollout data for the zero-training path.",
  "opportunity": "UWM's independent per-modality diffusion timestep architecture (RSS 2025) natively supports action-only inference (video timestep = T, action timestep = 0), producing action latents z_a jointly pretrained with video. This creates two complementary WAM-specific approaches to candidate selection, exploiting the distributional structure of the WAM's joint video-action pretraining:\n\n**Method 1 — Latent OOD Consistency Scoring (LOC, zero weight updates)**: Encode LIBERO-90 success demonstrations through frozen UWM in action-only mode to obtain a reference distribution {z_a^success}. Fit a lightweight density estimator — KNN-based nonconformity score (k=10) or Gaussian Mixture Model (k≤5 components) — on {z_a^success}. At inference, sample B=4–8 action-only candidates from frozen UWM, obtain latents {z_{a,1}, ..., z_{a,B}}, and score each: S_LOC(z_{a,i}) = −log p̂(z_{a,i}) (nonconformity score). Select a_{i*} = argmin_i S_LOC(z_{a,i}) (most in-distribution candidate). Total inference overhead: B × ~5ms = 20–40ms for B=4–8. Cost: ~30–60 minutes to fit density estimator on encoded latents; no WAM weight updates.\n\nTheoretical basis: (1) FAIL-Detect (RSS 2025) proves that OOD detection on success-only demonstration data reliably detects policy failures — the success-demo distribution implicitly excludes failure modes; (2) KDPE (CoRL 2025) demonstrates in Cartesian action space that selecting the most IN-distribution trajectory improves performance, while KDPE-OOD (selecting the most out-of-distribution trajectory) performs *worse* — validating the in-distribution selection direction for LOC; (3) z_a regularized by joint video-action pretraining encodes physical plausibility co-varying with video futures, creating a success-specific latent distribution with tighter quality-discriminative geometry than both Cartesian action space (KDPE) and VLA action tokens. LOC is WAM-specific in that this geometry is a direct consequence of joint video-action pretraining absent in VLAs and not present in action-space methods.\n\nKey differentiation from KDPE: (a) density estimation in WAM action latent space z_a, not Cartesian action space (position/orientation/gripper); (b) success-demonstrations-only reference distribution establishing a quality anchor, not all training data; (c) exploitation of WAM-specific joint pretraining regularization that aligns z_a with physical plausibility, unavailable in action-space methods; (d) B=4–8 candidates vs. KDPE's N=100, significantly cheaper inference. LOC implements success-mode selection; KDPE implements all-data-mode selection — these are mechanistically distinct quality signals.\n\nDifferentiation from MG-Select: LOC scores membership in the success demonstration distribution (latent OOD density); MG-Select measures KL divergence of task-conditioned output from masked unconditional distribution (action-space distributional uncertainty). One measures distributional membership relative to labeled success data, the other measures task-conditioning confidence.\n\nNote on Cosmos Policy planning mode: Cosmos Policy also implements Best-of-N — generates B actions, predicts future states and values, executes the highest-value action. However, (a) requires fine-tuning a value function on rollout data (1,536 H100-hours for RoboCasa) because demonstration-only training 'cannot correctly predict failure states'; (b) 15 total forward passes per candidate. LOC requires zero rollout data, zero weight updates, and ~5ms per candidate.\n\nNote on PCS: Video denoising error S_PCS = ||ε − ε_θ(x_{t*}, z_{a,i}, t*)||² is retained as a diagnostic comparison in Step 1, not as a primary method. Cosmos Policy's explicit finding and EVA's 'executability gap' provide strong prior evidence that denoising error is a weak candidate selection signal.\n\n**Method 2 — Action-Latent Value MLP (≤40 H100-hours training)**: A 3-layer MLP trained on WAM action latents z_a from LIBERO-90 success demonstrations AND explicitly collected failure trajectories scores each candidate via V(z_{a,i}) ∈ [0,1]. Hard argmax Best-of-N is the primary result. Key hypothesis: z_a regularized by joint video-action pretraining is more linearly separable between success and failure regimes than raw action outputs or VLA action tokens (the latent geometry argument). Failure demonstrations collected via frozen UWM rollouts in simulation (~15–20 H100-hours) plus Gaussian-perturbed synthetic failures (<1 H100-hour).\n\n**Comparison of LOC vs. Value MLP is itself a central contribution**: LOC requires zero training and no rollout data, but relies on the WAM's latent success distribution being well-separated from failure trajectories at inference; Value MLP requires failure demonstration collection but directly learns the task-specific quality function. Their empirical comparison characterizes when WAM latent OOD scoring is sufficient versus when labeled training adds necessary discriminative power — and whether this latent-space OOD approach outperforms action-space density estimation (KDPE-style) and distributional uncertainty (MG-Select-style KL).\n\n**Mandatory RoboCasa baseline validation before committing to targets**: World2Act (arXiv 2603.10422, March 2026) reports UWM achieving 60.8% on RoboCasa using 1,000 real demonstration fine-tuning. Since UWM was trained only on DROID data and has not been fine-tuned on RoboCasa tasks, the frozen UWM baseline (no RoboCasa demos) is expected to be substantially lower — likely 10–25%. Primary performance target: ≥10pp absolute improvement over the measured frozen baseline.",
  "landscape": "Cosmos Policy (arXiv 2601.16163, ICLR 2026) is the primary comparison point for absolute performance. Fully fine-tunes Cosmos-Predict2-2B on robot demos (384 H100-hours ALOHA, 1,536 RoboCasa, 3,072 LIBERO). Achieves 98.5% LIBERO and 67.1% RoboCasa. Its planning mode implements Best-of-N candidate selection: generates B candidate actions, predicts future states (3 queries to world model) and values (5 queries to value function per future state, 15 total predictions per action), and executes via majority-mean aggregation. Key distinction: Cosmos Policy's authors explicitly state that demo-only training 'cannot correctly predict failure states' — rollout fine-tuning is required for the planning value function. LOC requires zero rollout data and zero weight updates; Value MLP requires ≤40 H100-hours vs. 1,536 H100-hours.\n\nKDPE (arXiv 2508.10511, CoRL 2025) — NEWLY ADDED. Applies kernel density estimation to Cartesian action trajectories (end-effector position, orientation via SO(3) Lie group logarithm map, gripper state) generated by Diffusion Policy to filter multimodal outputs. Generates N=100 candidates and selects the trajectory with highest density (most typical). Achieves 88.2% vs. 85% average on RoboMimic/MimicGen tasks; real-robot evaluation on PickPlush, CubeSort, CoffeeMaking. Critical finding: KDPE-OOD (selecting the *most out-of-distribution* trajectory) performed *worse* than standard KDPE (selecting most typical) — confirming that in-distribution selection direction is correct and that the quality of the reference distribution matters. LOC differs from KDPE in three fundamental ways: (a) density estimation in the WAM's action latent space z_a rather than Cartesian action space — the latent space is regularized by joint video-action pretraining to encode physical plausibility, a quality signal absent from Cartesian position/orientation; (b) success-demonstrations-only reference distribution rather than all training data — LOC anchors the reference to task success, not behavioral frequency; (c) exploitation of WAM-specific joint pretraining that structures z_a along physical plausibility dimensions unavailable in action-space-only density methods. Additionally, LOC uses B=4–8 candidates vs. KDPE's N=100, providing a practical inference-cost advantage.\n\nWorld2Act (arXiv 2603.10422, March 2026) — Achieves ~66% on RoboCasa (Cosmos Policy + World2Act) using only 50 real + 50 imagined demos. Method: aligns VLA action latents with world model video dynamics via a contrastive matching objective. Reports UWM achieves 60.8% on RoboCasa with 1,000-demo fine-tuning (confirming frozen UWM baseline is substantially lower). Differentiation: World2Act requires contrastive post-training to align VLA action latents with video dynamics (modifies weights); our LOC method requires zero post-training — the alignment is inherited from UWM's joint pretraining.\n\nFast-WAM (arXiv 2603.16666) is the critical framing reference. Action-only inference achieves 97.6% LIBERO-avg (Table 2) and 91.8% RoboTwin (Table 1) at 190ms latency. Generates a single action trajectory with no candidate comparison. Complementary framing: Fast-WAM targets latency-critical deployment (single trajectory, fastest); our method targets success-critical tasks (B trajectories, select best via latent scoring at B × 5ms overhead).\n\nRoVer (arXiv 2510.10975, ICLR 2026) — Generates B candidate actions from frozen VLAs, trains a 0.2B Process Reward Model that scores candidates AND predicts refinement directions. Differentiation: (1) RoVer requires training a 0.2B PRM on process labels; LOC requires zero training and Value MLP requires only a 3-layer MLP; (2) RoVer applies to VLA action tokens lacking video-physics regularization; our methods target WAM action latents z_a jointly trained with video.\n\nVerifier-free / MG-Select (arXiv 2510.05681, ICLR 2026) — Training-free Best-of-N using KL-divergence from masked unconditional VLA distribution. 168% relative improvement on RoboCasa pick-and-place. Differentiation: MG-Select measures distributional uncertainty (how much task conditioning shifts the distribution from its unconditional prior) — an action-space confidence signal. LOC measures latent OOD membership (whether z_{a,i} is in-distribution relative to success demonstrations) — a latent-space quality signal. Mechanistically distinct and directly compared in ablation grid.\n\nFAIL-Detect (arXiv 2503.08558, RSS 2025) — Frames failure detection as sequential OOD detection using conformal prediction on success-only demonstration data. Demonstrates that OOD detection trained only on successes reliably detects failures at execution time. LOC applies the same OOD detection principle to WAM action latents z_a for pre-execution candidate selection. LOC differs: (1) pre-execution selection vs. execution monitoring; (2) WAM-specific latent structure from joint video-action pretraining; (3) direct density estimation in action latent space vs. distilled scalar signal. FAIL-Detect is cited as motivating the principle; Step 1 LOC diagnostic is the first empirical test of whether this principle transfers to pre-execution WAM z_a scoring.\n\nEVA (arXiv 2603.17808, 2026) — Identifies 'executability gap': visually coherent rollouts can violate kinematic constraints. Supports LOC over PCS: visual denoising error does not imply executable actions, while action latent OOD is more directly quality-relevant.\n\nWAV: World-Value-Action Model (arXiv 2604.14732, April 2026) — Integrates a trajectory value module as a new architectural component trained from scratch; iterative latent-space inference concentrating probability mass on high-value trajectories. 99.6% LIBERO, 75.6% real-world dual-arm. Differentiation: WAV modifies the architecture and trains from scratch; our method leaves all WAM weights frozen. WAV is plug-in-incompatible with pretrained WAMs; our method is plug-in-compatible with any pretrained WAM.\n\nCompose Your Policies! / GPC (arXiv 2510.01068) — Training-free convex composition of multiple frozen policy distributions. Different: operates at distribution level (combining score functions of multiple policies), not discrete candidate selection from a single frozen WAM.\n\nGPC-RANK (arXiv 2502.00622, IEEE RAL 2025): frozen policy + separately trained action-conditioned world model + hard argmax. Our method uses the WAM's own action latent space as the evaluation substrate — no separate world model.\n\nWhen to Trust Imagination (arXiv 2605.06222, May 2026): FFDC adaptively decides action chunk sizes during single-trajectory execution. Orthogonal and combinable with our pre-execution selection.",
  "approach": "Primary backbone: UWM (github.com/WEIRDLabUW/unified-world-model, RSS 2025), whose independent per-modality diffusion timestep architecture supports action-only inference (policy mode: video timestep = T, action timestep = 0). All WAM weights frozen throughout.\n\n**Step 0a — Frozen UWM Baseline Validation on RoboCasa (MANDATORY FIRST STEP)**: Run B=1 frozen UWM action-only inference on 50 episodes of representative RoboCasa tasks (kitchen manipulation subset). Expected baseline: 10–25% (UWM trained on DROID data only; World2Act reports 60.8% with 1,000-demo fine-tuning, confirming frozen baseline is substantially lower). Decision tree: if baseline ≥ 30%, proceed with current framing; if baseline 10–25%, confirm ≥10pp absolute improvement framing. Cost: ~2–3 H100-hours.\n\n**Step 0b — Reference Distribution Encoding for LOC**: Encode LIBERO-90 success demos through frozen UWM in action-only mode to obtain {z_a^success}. Fit density estimators: (a) KNN nonconformity model (k=10, Euclidean distance); (b) GMM (k=3,5 components, full covariance). Split latents 80/20 train/hold-out for AUC evaluation in Step 1. Cost: ~10–15 H100-hours encoding; ~30 minutes fitting density estimator. Steps 0b and 0c can run in parallel after Step 0a completes.\n\n**Step 0c — Failure Demonstration Collection (required for Value MLP)**: (a) Primary negatives: run frozen UWM (B=1) on LIBERO-Long and validated RoboCasa tasks; expected failure rate 30–50% on RoboCasa tasks, 5–15% on LIBERO-Long, yielding 500–2,000 failure trajectories. Cost: 15–20 H100-hours. (b) Synthetic supplement: Gaussian action perturbation (σ ∈ {0.05, 0.1}) on 20% of LIBERO-90 success demos, simulate in MuJoCo, flag truncated episodes as failures. Cost: <1 H100-hour. Combined: balanced 2,000–4,000 positive / 2,000–4,000 negative training set.\n\n**Step 1 — LOC Diagnostic (MANDATORY before main ablation)**: Empirically tests Hypothesis H1: 'WAM joint pretraining creates a latent success distribution where S_LOC(z_a) achieves AUC > 0.60 as a binary success predictor.' This hypothesis is motivated by FAIL-Detect's principle and KDPE's finding that in-distribution selection outperforms out-of-distribution selection in action space — but Step 1 is the first empirical test of whether WAM z_a, generated via action-only inference (not execution-time monitoring as in FAIL-Detect), shows the same property in the action latent space.\n\nProtocol: Sample B=16 action-only candidates from frozen UWM on 3 RoboCasa tasks, execute each in simulation (ground-truth success/failure), compute LOC and PCS scores.\n\nLOC metrics: (1) AUC of S_LOC as binary success predictor on held-out demos (target AUC > 0.60); (2) Spearman ρ of S_LOC with success labels (target ρ > 0.3); (3) compare KNN vs. GMM density estimators. Also compute S_PCS = ||ε − ε_θ(x_{t*}, z_{a,i}, t*)||² for the same candidates, varying t* ∈ {T/4, T/2, 3T/4} — expected to show lower AUC and ρ than LOC based on Cosmos Policy finding and EVA's executability gap evidence. Also compute MG-Select-style KL score as third comparison signal.\n\nExpected result: LOC AUC > PCS AUC ≈ MG-Select AUC, confirming latent OOD density is more informative than video denoising error or action-space distributional uncertainty.\n\nDecision tree for LOC: if AUC ≥ 0.60, LOC is reported as primary zero-training method; if LOC 0.55–0.60, both methods reported with LOC as secondary; if LOC < 0.55, LOC reported as negative result with informative comparison.\n\nThis diagnostic is itself a key scientific contribution: it empirically tests whether WAM joint pretraining creates a success latent distribution that is more quality-discriminative than video denoising error, distributional uncertainty, or action-space density (KDPE's domain).\n\n**Step 2 — Diversity Pilot (combined with LOC diagnostic)**: Same B=16 rollouts measure: pairwise cosine distance of action latents {z_{a,i}} (target mean > 0.05; if lower, increase noise temperature T_noise ∈ {1.5, 2.0}); LOC AUC conditional on latent diversity. Binary classification accuracy on held-out demo set as latent separability sanity check.\n\n**Step 3 — Value MLP Training**: 3-layer MLP (input: flattened z_a; output: scalar V ∈ [0,1]) trained via binary cross-entropy on balanced success/failure latents from Steps 0b and 0c. Report binary classification accuracy on held-out split (target > 75%). Cost: ~3–5 H100-hours.\n\n**Step 4 — Inference-Time Best-of-N Planning**: At each planning step, sample B=4–8 action-only trajectories from frozen UWM.\n\nPrimary results (two methods):\n- LOC selection: a_{i*} = argmin_i S_LOC(z_{a,i}) at best density estimator from diagnostic [zero weight updates, WAM-specific]\n- Value MLP selection: a_{i*} = argmax_i V(z_{a,i}) [lightweight training, WAM-specific]\n\nComparisons (required): MG-Select-style KL scoring applied to WAM action-only inference; random selection (B=4–8, sanity check); single-trajectory WAM B=1 (frozen baseline).\n\nAblation (secondary): (a) PCS denoising error selection at best t* from diagnostic (expected to underperform LOC); (b) soft MPPI w_i ∝ exp(β·V(z_{a,i})) to document action-averaging artifact; (c) action-only z_a vs. full video+action latent for LOC and Value MLP scoring.\n\n**Ablation Grid**: B ∈ {1, 4, 8} (B=1 is frozen WAM single-trajectory baseline); selection method: LOC KNN vs. LOC GMM (primary zero-training) vs. Value MLP hard argmax (primary trained) vs. MG-Select-style KL (VLA method applied to WAM, key comparison) vs. random selection (sanity check); T_noise fixed at 1.0 in primary ablation (1.5, 2.0 variants run in human-in-loop follow-up if diversity pilot shows issues); execution regime: (a) open-loop vs. (b) periodic replanning every K=5 action chunks.\n\n**Primary hypotheses**: (H1, tested in Step 1 LOC diagnostic) LOC achieves Spearman ρ > 0.3 and AUC > 0.6, confirming WAM success latents form an OOD-detectable distribution — this hypothesis is motivated but unproven; Step 1 is the first empirical test; (H2) LOC outperforms PCS and MG-Select-style KL in the diagnostic, with PCS showing AUC near 0.5 consistent with Cosmos Policy's finding; (H3) Value MLP achieves ≥10pp improvement over B=1 baseline on RoboCasa; (H4) LOC achieves ≥5pp improvement over B=1 with zero weight updates; (H5) Both methods outperform MG-Select-style KL applied to WAM and outperform KDPE-style Cartesian density applied to WAM outputs, confirming latent quality-discrimination advantages of WAM joint pretraining.\n\n**Standalone Value MLP contribution (applicable if LOC fails H1)**: If LOC AUC < 0.55 in the diagnostic, the paper's narrative shifts to Value MLP as the primary contribution with the following independent novelty argument: (a) vs. WAV — WAV trains a trajectory value module as a new architectural component from scratch, requiring architectural co-design; Value MLP is plug-in-compatible with any pretrained WAM, requiring only 3-layer MLP training on existing latent representations; (b) vs. RoVer — RoVer requires a 0.2B PRM trained on process labels; Value MLP uses a 3-layer MLP trained on binary success/failure labels; RoVer targets VLA action tokens lacking video-physics regularization, while Value MLP exploits WAM z_a's joint-pretraining geometry; (c) vs. Cosmos Policy — requires 1,536 H100-hours rollout fine-tuning; Value MLP requires ≤40 H100-hours; (d) vs. KDPE — KDPE operates in Cartesian action space with all training data; Value MLP uses WAM latent space with success/failure-labeled data; the central empirical claim becomes 'joint pretraining creates a latent space where success/failure are more linearly separable than in Cartesian action space, enabling a 3-layer MLP to achieve discriminative performance that requires larger models on VLA action tokens.' This standalone narrative is complete and does not depend on LOC succeeding.\n\n**Evaluation Benchmarks**: (a) Primary — RoboCasa: Cosmos Policy fine-tuned 67.1%; World2Act (Cosmos+World2Act) ~66%; frozen UWM expected 10–25% (validated in Step 0a); absolute target ≥10pp over frozen baseline. (b) Secondary — LIBERO-Long: near saturation for strong frozen WAMs (Fast-WAM 95.2%, Table 2); included to characterize gain profile vs. task difficulty. (c) Baselines: B=1 frozen WAM, random selection, MG-Select-style KL applied to WAM.\n\nDreamZero cross-WAM validation deferred to camera-ready. CoRL submission rests on UWM alone.",
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
      "gpu_budget_breakdown": "Step 0a frozen UWM baseline: ~3h; Steps 0b+0c in parallel (demo encoding + failure collection): ~32h billed (12h encoding + 20h failure collection running concurrently); Step 1 LOC diagnostic: ~4h; Step 3 Value MLP training: ~5h; Main ablation grid (B ∈ {1,4,8} × 5 methods × 3 seeds × 2 benchmarks = 90 runs × ~1.2h avg): ~108h; contingency/reruns: ~13h. Total: ~165h billed GPU-hours. With 4 GPUs running ablation batch concurrently: wall-clock ≈ 44h setup + 27h ablations = 71h wall-clock; billed = 44×1 + 27×4 = 152h billed. With overhead/reruns: ~180–190h billed GPU-hours ≤ 200h hard constraint.",
      "gpu_utilization": "MINIMAL idle (~5–10%): agent pipelines baseline validation, LOC diagnostic, failure collection, demo encoding, density fitting, MLP training, and evaluation continuously.",
      "timeline": "7–10 days with 4 H100 GPUs simultaneously",
      "team": "0 (only initial repo setup and credential configuration)",
      "claude_api_cost": "$200–350 (~2,500–4,000 turns at Opus rates)",
      "estimated_gpu_cost": "~$463 (185h × $2.50/h)",
      "ablation_grid_vs_prior": "Pruned from prior estimate: T_noise sweep ({1.0,1.5,2.0}) dropped from auto research grid — T_noise fixed at 1.0 unless diversity pilot (Step 2) shows mean cosine distance < 0.05, in which case T_noise=1.5 is tested in human-in-loop follow-up. B grid reduced from {1,2,4,8,16} to {1,4,8} (drop B=2 and B=16 as extreme values). PCS full ablation dropped from auto grid (retained only in Step 1 LOC diagnostic). These prunings reduce ablation runs from ~150 to ~90, bringing billed GPU-hours within the 200h hard constraint.",
      "speed_bottleneck": "Step 0a baseline validation → LOC diagnostic → (parallel: failure collection + demo encoding) → density fitting (trivial) + Value MLP training is a 5-step sequential dependency spanning ~8 days minimum. RoboCasa evaluation rollouts: each ablation variant requires sequential per-task evaluation; with 4 GPUs running 4 variants concurrently, the full grid needs ~5–7 days.",
      "risk_note": "LOC density estimation (KNN/GMM) is a standard sklearn/torch operation requiring no custom implementation. Main implementation risk: UWM action latent extraction in action-only mode (video timestep = T, action timestep = 0) — this mode is supported by UWM's architecture but may require engineering to extract z_a as a fixed-size vector for density estimation. If z_a is not directly accessible, the Action Decoder intermediate activations serve as a substitute latent representation."
    }
  },
  "target_venues": [
    "CoRL 2026 (Abstract deadline: May 26, 2026; Full paper: May 29, 2026; Conference: Nov 9–12, Austin TX) — TIGHT but viable: 19 days from 2026-05-10. Step 0a RoboCasa baseline must run immediately (Day 1–2). Minimum viable submission: frozen UWM RoboCasa baseline validation + LOC diagnostic figure (including PCS comparison showing expected negative result) + LOC and/or Value MLP Best-of-N results (primary) + LIBERO-Long (secondary) + B/hard-argmax ablation + MG-Select-style KL baseline comparison. DreamZero cross-WAM deferred to camera-ready.",
    "ICLR 2027 (deadline ~September–October 2026) — More feasible timeline for complete ablation grid, latent geometry analysis (success/failure separation in WAM vs. VLA latent spaces), DreamZero cross-WAM evaluation, and potential real-world experiments."
  ],
  "level": "solid",
  "key_references": [
    "Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning (arXiv 2601.16163, ICLR 2026) — CRITICAL PRIOR WORK: implements Best-of-N planning mode (15 forward passes per action via majority-mean aggregation of world model + value function queries); requires rollout fine-tuning because demo-only training 'cannot correctly predict failure states'; 1,536 H100-hours for RoboCasa; 98.5% LIBERO, 67.1% RoboCasa; our LOC requires zero rollout data and zero weight updates",
    "KDPE: A Kernel Density Estimation Strategy for Diffusion Policy Trajectory Selection (arXiv 2508.10511, CoRL 2025) — NEWLY ADDED CRITICAL PRIOR WORK: applies manifold-aware KDE to Cartesian action trajectories (end-effector position/SO(3)-orientation/gripper) from Diffusion Policy; generates N=100 candidates; achieves 88.2% vs. 85% on RoboMimic/MimicGen; CRITICAL FINDING: KDPE-OOD (selecting most out-of-distribution trajectory) performs WORSE than KDPE (selecting most typical) — validates in-distribution selection direction for LOC; differentiates from LOC: (a) Cartesian action space vs. WAM action latent space; (b) all training data vs. success-only reference; (c) no WAM-specific joint pretraining regularization; (d) N=100 candidates vs. LOC's B=4–8",
    "World2Act (arXiv 2603.10422, March 2026) — post-training framework achieving ~66% on RoboCasa using 50 real + 50 imagined demos; reports UWM achieves 60.8% on RoboCasa with 1,000-demo fine-tuning (confirming frozen UWM baseline is ~10–25%); differentiation: World2Act requires contrastive post-training to align VLA latents; LOC exploits WAM alignment inherited from joint pretraining",
    "Fast-WAM: World Action Models without Test-Time Video (arXiv 2603.16666) — CRITICAL FRAMING: 97.6% LIBERO-avg (Table 2) and 91.8% RoboTwin (Table 1) at 190ms without video; single trajectory only; our method uses same action-only inference for candidate generation and adds LOC selection at B × 5ms overhead",
    "FAIL-Detect: Failure Detection as OOD Detection for Robot Manipulation (arXiv 2503.08558, RSS 2025) — SUPPORTING WORK: proves OOD detection on success-only demonstration data reliably detects policy failures; uses flow-based density estimation on distilled policy signals; motivates LOC's use of KNN/GMM density on success demo latents; FAIL-Detect is execution-time monitoring, LOC is pre-execution candidate selection from a different inference mode — Step 1 LOC diagnostic is the first empirical test of whether this principle transfers to pre-execution WAM z_a",
    "EVA: Aligning Video World Models with Executability (arXiv 2603.17808, 2026) — identifies 'executability gap' showing visually coherent world model rollouts can violate kinematic constraints; supports LOC over PCS: visual denoising error does not predict task success",
    "RoVer: Robot Reward Model as Test-Time Verifier for Vision-Language-Action Models (arXiv 2510.10975, ICLR 2026) — CRITICAL PRIOR WORK: generates B VLA candidates, trains 0.2B PRM; differentiation: requires 0.2B model training vs. LOC's zero training and Value MLP's 3-layer MLP; VLA action tokens lack video-physics regularization",
    "Verifier-free Test-Time Sampling / MG-Select (arXiv 2510.05681, ICLR 2026) — CRITICAL PRIOR WORK: training-free KL-from-masked-distribution scoring for frozen VLAs; 168% relative improvement on RoboCasa pick-and-place; differentiation: MG-Select measures action-space distributional uncertainty, LOC measures latent OOD membership relative to success demo distribution",
    "World-Value-Action (WAV) Model (arXiv 2604.14732, April 2026) — trajectory value module requiring training from scratch, new architectural component; 99.6% LIBERO, 75.6% real-world; our method leaves all WAM weights frozen and is plug-in-compatible with pretrained WAMs; WAV requires architectural co-design",
    "Compose Your Policies! / GPC (arXiv 2510.01068) — training-free distribution composition for multiple frozen policies; operates at distribution level, not discrete candidate selection from single WAM",
    "Inference-Time Enhancement / GPC-RANK (arXiv 2502.00622, IEEE RAL 2025) — frozen policy + separately trained world model + hard argmax; our method uses WAM's own action latent space, no separate world model",
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
  "description": "Latent-Distribution Candidate Selection (LDCS) converts any pretrained video-diffusion World Action Model into a multi-candidate planner at inference time without modifying any WAM weight, exploiting WAM-specific latent structure through two complementary methods.\n\nThe key insight: Cosmos Policy's own finding that demonstration-trained video priors 'cannot correctly predict failure states' — and EVA's demonstration of an 'executability gap' — rules out video denoising error as a reliable zero-training quality signal. KDPE (CoRL 2025) demonstrates that density-based candidate selection in Cartesian action space improves performance, but critically, KDPE-OOD (selecting the most out-of-distribution trajectory) performs *worse* — confirming that the quality of the reference distribution matters and that in-distribution selection is the correct direction. LOC extends this principle into the WAM's action latent space using a success-only reference distribution, exploiting WAM-specific joint pretraining geometry unavailable to action-space-only methods.\n\n**Hypothesis H1 (tested empirically in Step 1 LOC diagnostic)**: WAM joint video-action pretraining regularizes z_a along physical plausibility dimensions, creating a success latent distribution where S_LOC(z_a) achieves AUC > 0.60 as a binary success predictor — more discriminative than video denoising error (PCS), action-space distributional uncertainty (MG-Select-style KL), and Cartesian-space density (KDPE). This hypothesis is motivated by FAIL-Detect's principle (OOD on success-only data detects failures) and KDPE's empirical confirmation (in-distribution selection outperforms outlier selection), but Step 1 is the first empirical test on pre-execution WAM z_a. If H1 fails (AUC < 0.55), LOC is reported as a negative result and Value MLP becomes the sole primary contribution.\n\n**Method 1 — Latent OOD Consistency Scoring (LOC, zero weight updates)**: Fit a KNN or GMM density estimator on WAM action latents {z_a^success} from LIBERO-90 success demos. At inference, sample B=4–8 action-only candidates and score each by nonconformity: S_LOC(z_{a,i}) = −log p̂(z_{a,i}). Select argmin (most in-distribution candidate). Overhead: B × ~5ms = 20–40ms for B=4–8.\n\nDifferentiated from KDPE: (a) action latent space z_a regularized by joint video-action pretraining, not Cartesian action space; (b) success-demonstrations-only reference distribution anchored to task quality, not all training data; (c) B=4–8 vs. KDPE's N=100. Differentiated from MG-Select: LOC scores latent OOD membership relative to labeled success data; MG-Select scores action-space distributional uncertainty from unconditional prior.\n\n**Method 2 — Action-Latent Value MLP (≤40 H100-hours)**: 3-layer MLP trained on {z_a^success} and explicitly collected failure latents. Hard argmax selection avoids multi-modal action-averaging artifact. Central hypothesis: joint pretraining geometry makes z_a more linearly separable between success/failure regimes than VLA action tokens or Cartesian representations. Standalone contribution if LOC fails: (a) plug-in-compatible with pretrained WAMs (vs. WAV's from-scratch architectural co-design); (b) 3-layer MLP (vs. RoVer's 0.2B PRM); (c) ≤40 H100-hours (vs. Cosmos Policy's 1,536 H100-hours rollout fine-tuning); (d) operates in WAM latent space regularized by joint pretraining (vs. KDPE's Cartesian space).\n\n**LOC Diagnostic (mandatory, Step 1)**: B=16 rollouts on 3 RoboCasa tasks, measuring AUC of S_LOC as binary success predictor (target H1: AUC > 0.6), compared against: (a) video denoising error S_PCS (expected negative result), (b) MG-Select-style KL applied to WAM, (c) KDPE-style Cartesian density as reference baseline.\n\nPrimary evaluation: RoboCasa (target ≥10pp absolute over frozen baseline; Cosmos Policy 67.1% / World2Act ~66% as upper references). Secondary: LIBERO-Long. Auto research ablation grid pruned to B ∈ {1,4,8} × 5 methods × 3 seeds × 2 benchmarks (~185 billed H100-hours ≤ 200h hard constraint). CoRL submission: UWM only; DreamZero cross-WAM deferred to camera-ready.",
  "project_name": "frozen_wam_mppi",
  "source": "web_research"
}

## Reviewer feedback (round 6)
Issues: ["SIGNIFICANT — V-GPS (arXiv 2410.13816, 'Value-Guided Inference-Time Policy Steering', October 2024) is absent from the landscape and directly overlaps with the Value MLP method. V-GPS uses an offline RL-learned value function to re-rank B candidate actions from frozen generalist policies (Octo, RT-1X, OpenVLA), achieving +82.8% absolute real-world improvement. This is mechanistically identical to Value MLP at the paradigm level. The submission must cite V-GPS and differentiate: 'V-GPS trains a value function via offline RL on raw action representations from VLA action tokens lacking video-physics regularization; our Value MLP uses binary success/failure supervision on WAM z_a from joint video-action pretraining, which we hypothesize is more linearly separable between success/failure regimes than VLA action token representations. V-GPS demonstrates the paradigm works for VLAs; we ask whether WAM-specific latent geometry provides additional discriminative power.' This is the clearest gap remaining after 6 rounds.", "SIGNIFICANT — WAV performance numbers (99.6% LIBERO, 75.6% real-world) appear unverifiable and potentially incorrect. Independent verification of arXiv 2604.14732 found LIBERO overall average score of 98.1 (not 99.6%) and no 75.6% real-world figure in accessible content. If the Generator is citing wrong WAV metrics, this undermines the differentiation story and will be flagged by CoRL reviewers. Fetch the WAV paper PDF directly and correct the stated metrics with table references.", "MODERATE — The theoretical argument that UWM z_a in action-only mode (video timestep=T) retains video-physics regularization from joint training needs explicit acknowledgment of the inference-time tension. In action-only inference, video tokens are at full noise (T), meaning no video information conditions z_a at inference time. The current framing states z_a is 'regularized by joint video-action pretraining to encode physical plausibility' without clarifying this is a training-time property whose inference-time persistence is unproven. Revise to: 'We hypothesize that joint training causes z_a to learn quality-discriminative representations even when video is absent at inference time — tested empirically in Step 1. If this property does not transfer (AUC < 0.55), LOC reports a negative result and Value MLP becomes the primary contribution.'", "MODERATE — ALT Policy ('Demystifying Diffusion Policies via Action Lookup Tables', arXiv 2505.05787, May 2025) and UNISafe (arXiv 2505.00779, May 2025) should be briefly cited as adjacent work in the related work section. ALT Policy uses nearest-neighbor OOD detection in action latent space for frozen diffusion policies (different domain: observation latents for retrieval, not action latents for candidate scoring). UNISafe uses conformal prediction + world model uncertainty for OOD-based action filtering (different application: safety, not candidate selection). A single sentence each in related work suffices: these papers are distinct from LOC but demonstrate that latent-space OOD detection for robot policies is a published direction.", "MODERATE — Expected absolute RoboCasa performance (~20-35% after ≥10pp improvement from 10-25% frozen baseline) needs proactive framing against fine-tuned baselines. CoRL reviewers will note that Cosmos Policy achieves 67.1% and World2Act ~66%, making 20-35% look weak. Add one paragraph explicitly framing this: 'Our methods are orthogonal to fine-tuning — they extract planning value from existing pretrained WAMs in settings where domain-specific demonstration data is unavailable. The comparison target is B=1 frozen WAM inference, not fine-tuned models; we improve over the no-adaptation baseline by ≥10pp without any weight updates or rollout data collection.' This reframing prevents reviewers from misreading the target."]
Feedback: Round 6 has closed all Round 5 issues (KDPE cited with strong differentiation, Fast-WAM numbers verified and table-referenced, auto research budget correctly computed to 152-185h billed ≤ 200h, LOC hypothesis framed as H1 with diagnostic gate, standalone Value MLP fallback narrative ready). Two new issues were found through independent search that require fixes before submission:

**1. Add V-GPS (arXiv 2410.13816) to related work — 1 day.** V-GPS (October 2024) uses a learned value function to re-rank B candidates from frozen generalist policies on real robot tasks (+82.8% improvement). It is paradigmatically identical to Value MLP at the method level. Write in related work: 'V-GPS (2024) learns an offline RL value function to score and re-rank B candidate actions from frozen VLAs (Octo, RT-1X, OpenVLA), achieving +82.8% real-world improvement. Our Value MLP applies the same paradigm to WAM action latents z_a — specifically, we ask whether WAM-specific joint video-action pretraining creates a latent geometry where success/failure are more linearly separable than in VLA action token space, enabling a 3-layer MLP to match or exceed the discriminative power that V-GPS achieves via offline RL.' This turns a missing citation into a positive framing.

**2. Verify and correct WAV metrics — 0.5 day.** Fetch the WAV paper PDF and find the exact LIBERO and real-world numbers with table references. If the LIBERO number is 98.1 (not 99.6%) and the real-world number differs from 75.6%, correct the manuscript. Citing wrong numbers for a concurrent paper will be caught in review.

**3. Clarify the action-only mode z_a argument — 0.5 day.** The theoretical framing says z_a is 'regularized by joint pretraining to encode physical plausibility' — this is a training-time property. Add one sentence: 'In action-only inference, video tokens are at full noise (timestep T) and provide no inference-time conditioning; we hypothesize that the training-time alignment between z_a and video dynamics persists as a latent geometry property even without video input — which Step 1 empirically tests.' This makes the theoretical argument accurate and shows scientific awareness.

With these three fixes (2 days total), the paper is ready for CoRL submission. Minimum viable submission scope is correctly identified: frozen UWM RoboCasa baseline + LOC diagnostic (H1 test) + LOC and/or Value MLP Best-of-N results + LIBERO-Long secondary + B/hard-argmax ablation + MG-Select-style KL baseline comparison. DreamZero cross-WAM deferred to camera-ready is the right call.

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
这个 idea 已经经过 6 轮修订，近 3 轮的平均分从 3.2 到 3.2，没有明显改善。

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
  "promptId": "d7b557eb-7415-4061-bbb7-58d07ac1d15d",
  "type": "user",
  "uuid": "50b8be0e-588f-481e-8ab1-88ef055998a0",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e26c6f2-72e3-4741-87ef-c0d8359a2540",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T09:13:58.076Z_

```json
{
  "parentUuid": "50b8be0e-588f-481e-8ab1-88ef055998a0",
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
  "uuid": "c3e9e725-b461-4340-a1ac-a5a0c169d8ac",
  "timestamp": "2026-05-10T09:13:58.076Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e26c6f2-72e3-4741-87ef-c0d8359a2540",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T09:13:58.076Z_

```json
{
  "parentUuid": "c3e9e725-b461-4340-a1ac-a5a0c169d8ac",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "da828cf8-11a5-44d0-9b44-7ed1994ef615",
  "timestamp": "2026-05-10T09:13:58.076Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e26c6f2-72e3-4741-87ef-c0d8359a2540",
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
  "leafUuid": "da828cf8-11a5-44d0-9b44-7ed1994ef615",
  "sessionId": "4e26c6f2-72e3-4741-87ef-c0d8359a2540"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "WAM latent-space value learning for frozen inference planning",
  "sessionId": "4e26c6f2-72e3-4741-87ef-c0d8359a2540"
}
```

---

### Assistant

_source line 8 · 2026-05-10T09:14:45.867Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze this situation carefully. This research idea has been through 6 rounds of revision with no meaningful improvement in scores (3.2 average). The reviewer feedback for Round 6 raises several issues that need to be addressed. Let me think about whether this needs a minor fix, major revision, or pivot.

**Current State of the Idea:**
The idea is about "Latent-Distribution Candidate Selection for Frozen World Action Models" - specifically using OOD detection on WAM action latents to select better candidates at inference time (LOC method) and training a lightweight value MLP on those latents (Value MLP method).

**Round 6 Issues:**
1. V-GPS (arXiv 2410.13816) is missing - directly overlaps with Value MLP method


2. I need to verify the WAV performance numbers and clarify the z_a regularization argument for action-only inference scenarios
3. ALT Policy and UNISafe are missing citations
4. The expected performance range needs better positioning relative to fine-tuned baselines

**Deeper Assessment:**

After 6 rounds with stagnant scores, I'm realizing the V-GPS overlap is a fundamental problem—it's been doing exactly what my Value MLP method proposes since October 2024, which means I'm not presenting a novel contribution at the paradigm level.

The differentiation claim that WAM's latent space outperforms VLA action tokens lacks empirical validation and feels speculative. On the LOC method side, the core idea about joint pretraining creating an OOD-detectable success distribution is interesting and novel to latent space (KDPE operates in Cartesian space), but FAIL-Detect already handles OOD detection on success demonstrations. The performance gap between my expected 20-35% and Cosmos Policy's 67.1% is substantial enough that reviewers will push back on practical utility even with the orthogonal-to-fine-tuning framing. There's also a fundamental issue in action-only mode where at video timestep T, there's no actual video to work with.

The claim that z_a encodes physical plausibility is really a training-time property, and whether that persists at inference time is unproven—that's a real theoretical gap. I'm wondering if I should reconsider the whole direction. The WAM-specific angle has merit, but the LOC method has this core tension that's hard to resolve. V-GPS already showed value function re-ranking works for frozen policies, so that's not novel. The main novel claim boils down to whether WAM latent space is actually better than VLA action tokens for discrimination, and I don't have the empirical evidence to back that up.

I could reframe this as an empirical study of what makes WAM action latents discriminative, using Best-of-N planning as the application—that's more scientifically sound. Or I could pivot toward a cross-architecture comparison instead.

Actually, there's a stronger theoretical angle here. Even in action-only inference, the diffusion process still relies on the pretrained video-action joint distribution as a prior, so z_a isn't truly unconditioned on video—it's conditioned through the learned prior from joint training. Let me think through what's actually happening in the action-only mode: the video diffusion starts at full noise while action diffusion is already clean, so the model is still leveraging that joint distribution it learned.

The real claim isn't about inference-time video conditioning, but about how joint training shapes the learned representations themselves. The model's weights encode a prior where z_a naturally aligns with physical plausibility and task success—that's a property of what the model learned during training, not something happening at inference. I need to reframe this more precisely.

Looking at the bigger picture though, after six rounds of incremental fixes with stagnant scores, I'm wondering if the core issue runs deeper than just these addressable points like adding V-GPS, verifying the WAV numbers, fixing the z_a framing, and adding the missing citations.

The fundamental problem might be that the idea itself feels incremental, especially since the strongest novel contribution—using WAM latent OOD for candidate selection—has this underlying uncertainty that I haven't fully resolved. And the V-GPS discovery actually undermines Value MLP's novelty claim significantly.

Maybe instead of patching these issues one by one, I should consider a more substantial reframing: consolidate the two separate methods into a unified framework centered on exploiting WAM's specific joint pretraining geometry for candidate selection, with the core novelty being an empirical analysis of why WAM latents are more discriminative than alternatives like VLA tokens or Cartesian space.

But stepping back, the reviewer feedback pattern shows consistent issues—V-GPS was a major prior work gap, WAV had metric errors, and earlier rounds caught KDPE and Fast-WAM problems. The stagnation over three rounds suggests I'm not addressing what's actually limiting the work's impact.

Looking at the landscape of recent methods—V-GPS for value-based re-ranking, KDPE for density-based selection, FAIL-Detect for OOD detection on success demos, MG-Select for KL-based training-free selection, and RoVer for PRM-based re-ranking—the core question becomes whether applying OOD detection or value learning specifically to WAM action latents rather than VLA tokens or Cartesian space is genuinely novel and significant enough for a top venue.

The real differentiator here is that WAM action latents benefit from joint pretraining geometry in ways that other action representations don't, making them a fundamentally better substrate for this kind of selection. Rather than trying to position everything as novel, I should lead with the LOC as the primary contribution, reframe the Value MLP as essentially V-GPS adapted to WAM latents—which actually validates the approach while highlighting what's unique about the WAM geometry—and then tighten the theoretical framing around z_a, verify the experimental numbers, fill in the citation gaps, and make a clearer case for why WAM latents are superior to alternatives for this task.

Now I need to pull the V-GPS paper, double-check the WAV metrics, review the ALT Policy and UNISafe papers to make sure I'm not missing anything important.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da828cf8-11a5-44d0-9b44-7ed1994ef615",
  "isSidechain": false,
  "requestId": "req_011CatdeQVK4ty9gJjbeT4XC",
  "type": "assistant",
  "uuid": "4f3edb6f-5549-4de4-ad86-227a7055d0c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e26c6f2-72e3-4741-87ef-c0d8359a2540",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Dvvq3ofb6kksMnQxyg38JX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19476,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1987,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19476,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1987,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 19476,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19476
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

_source line 9 · 2026-05-10T09:14:45.870Z_

Looking at this situation carefully: 6 rounds with stagnant scores suggests the patch-fixing approach isn't working. Before revising, I need to deeply research V-GPS, verify WAV numbers, and read ALT Policy and UNISafe. Let me do this in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f3edb6f-5549-4de4-ad86-227a7055d0c8",
  "isSidechain": false,
  "requestId": "req_011CatdeQVK4ty9gJjbeT4XC",
  "type": "assistant",
  "uuid": "b1ef0e79-6616-40bd-9ea5-2ba03929d3d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e26c6f2-72e3-4741-87ef-c0d8359a2540",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Dvvq3ofb6kksMnQxyg38JX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19476,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1987,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19476,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1987,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 19476,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19476
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

_source line 10 · 2026-05-10T09:14:45.983Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HTGziYUGmbQd46uSQjxt4Q`</summary>

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
  "parentUuid": "b1ef0e79-6616-40bd-9ea5-2ba03929d3d2",
  "isSidechain": false,
  "requestId": "req_011CatdeQVK4ty9gJjbeT4XC",
  "type": "assistant",
  "uuid": "b5a11d89-17dc-4d0a-934d-5d8f54664d18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e26c6f2-72e3-4741-87ef-c0d8359a2540",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Dvvq3ofb6kksMnQxyg38JX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19476,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1987,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19476,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1987,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 19476,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19476
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

_source line 11 · 2026-05-10T09:14:45.995Z_

<details><summary>↩ Tool result · `toolu_01HTGziYUGmbQd46uSQjxt4Q`</summary>

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
  "parentUuid": "b5a11d89-17dc-4d0a-934d-5d8f54664d18",
  "isSidechain": false,
  "promptId": "d7b557eb-7415-4061-bbb7-58d07ac1d15d",
  "type": "user",
  "uuid": "4b0fa2ac-389f-4dfa-a7f2-81b9f66491ff",
  "toolUseResult": {
    "matches": [
      "WebFetch",
      "WebSearch"
    ],
    "query": "select:WebFetch,WebSearch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "b5a11d89-17dc-4d0a-934d-5d8f54664d18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e26c6f2-72e3-4741-87ef-c0d8359a2540",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-10T09:14:48.451Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me run parallel research on all the papers I need to verify and read.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b0fa2ac-389f-4dfa-a7f2-81b9f66491ff",
  "isSidechain": false,
  "requestId": "req_011CatdhwBc99m94XmMVxiM2",
  "type": "assistant",
  "uuid": "916a9ab1-9057-4f92-930a-0d05e6378697",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e26c6f2-72e3-4741-87ef-c0d8359a2540",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_011e2LuaUZJunnyTapBjcNfp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3005,
      "cache_read_input_tokens": 31107,
      "output_tokens": 1063,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3005,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1063,
          "cache_read_input_tokens": 31107,
          "cache_creation_input_tokens": 3005,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3005
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

_source line 13 · 2026-05-10T09:14:49.298Z_

Now let me run parallel deep research on all four key issues simultaneously.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "916a9ab1-9057-4f92-930a-0d05e6378697",
  "isSidechain": false,
  "requestId": "req_011CatdhwBc99m94XmMVxiM2",
  "type": "assistant",
  "uuid": "e9491b5b-ad55-492a-a0fa-7155c08d8dfe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e26c6f2-72e3-4741-87ef-c0d8359a2540",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_011e2LuaUZJunnyTapBjcNfp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3005,
      "cache_read_input_tokens": 31107,
      "output_tokens": 1063,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3005,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1063,
          "cache_read_input_tokens": 31107,
          "cache_creation_input_tokens": 3005,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3005
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

_source line 14 · 2026-05-10T09:14:54.101Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01BRM9kHnero17KJauHCTisa`</summary>

```json
{
  "description": "Fetch V-GPS paper abstract and method",
  "prompt": "Fetch the V-GPS paper at https://arxiv.org/abs/2410.13816 and extract: (1) the exact title, (2) the abstract, (3) the core method description - specifically how the value function is trained, what policy architectures it applies to (Octo, RT-1X, OpenVLA?), what the +82.8% improvement claim refers to (which benchmark, which baseline), (4) how candidate actions are generated, (5) what action representation space the value function operates on. Report verbatim quotes where possible.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9491b5b-ad55-492a-a0fa-7155c08d8dfe",
  "isSidechain": false,
  "requestId": "req_011CatdhwBc99m94XmMVxiM2",
  "type": "assistant",
  "uuid": "5538bec1-031a-4caa-8722-04da17ab2429",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e26c6f2-72e3-4741-87ef-c0d8359a2540",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_011e2LuaUZJunnyTapBjcNfp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3005,
      "cache_read_input_tokens": 31107,
      "output_tokens": 1063,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3005,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1063,
          "cache_read_input_tokens": 31107,
          "cache_creation_input_tokens": 3005,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3005
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

_source line 15 · 2026-05-10T09:14:59.558Z_

<details open><summary>🔧 Tool call — Agent · `toolu_019XRHdJHE4WzJJbHRMu8viX`</summary>

```json
{
  "description": "Fetch WAV paper to verify metrics",
  "prompt": "Fetch the WAV (World-Value-Action Model) paper at https://arxiv.org/abs/2604.14732 and extract: (1) the exact LIBERO benchmark results - specifically which LIBERO split (LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-Long, LIBERO-90, overall average?) and what score (99.6%? 98.1%? something else?), with exact table reference; (2) any real-world robot experiment results - what percentage, which task, which table/figure; (3) the abstract text verbatim. The claim being checked: LIBERO = 99.6% and real-world = 75.6%. Report exactly what numbers appear in the paper and where.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5538bec1-031a-4caa-8722-04da17ab2429",
  "isSidechain": false,
  "requestId": "req_011CatdhwBc99m94XmMVxiM2",
  "type": "assistant",
  "uuid": "5e3f09d9-295a-48ea-96db-f3a0a31200d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e26c6f2-72e3-4741-87ef-c0d8359a2540",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_011e2LuaUZJunnyTapBjcNfp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3005,
      "cache_read_input_tokens": 31107,
      "output_tokens": 1063,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3005,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1063,
          "cache_read_input_tokens": 31107,
          "cache_creation_input_tokens": 3005,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3005
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

_source line 16 · 2026-05-10T09:15:04.468Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Hw4SfTZKiNcd2mztRTBJgt`</summary>

```json
{
  "description": "Fetch ALT Policy and UNISafe papers",
  "prompt": "Fetch two papers and summarize each briefly:\n\n1. ALT Policy (arXiv 2505.05787): https://arxiv.org/abs/2505.05787 - Extract the title, abstract, and specifically: does it use nearest-neighbor OOD detection in action latent space? What latent space does it use? How does it relate to candidate selection vs retrieval?\n\n2. UNISafe (arXiv 2505.00779): https://arxiv.org/abs/2505.00779 - Extract the title, abstract, and specifically: does it use conformal prediction + world model uncertainty for OOD-based action filtering? Is it for safety or candidate selection? What policy/model architecture?\n\nReport what each paper actually does so we can write accurate one-sentence citations.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e3f09d9-295a-48ea-96db-f3a0a31200d9",
  "isSidechain": false,
  "requestId": "req_011CatdhwBc99m94XmMVxiM2",
  "type": "assistant",
  "uuid": "25b7ee3c-f8e3-4d21-baa2-a2cf75fc8c20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e26c6f2-72e3-4741-87ef-c0d8359a2540",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_011e2LuaUZJunnyTapBjcNfp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3005,
      "cache_read_input_tokens": 31107,
      "output_tokens": 1063,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3005,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1063,
          "cache_read_input_tokens": 31107,
          "cache_creation_input_tokens": 3005,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3005
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

_source line 17 · 2026-05-10T09:15:10.097Z_

<details open><summary>🔧 Tool call — Agent · `toolu_013fpMKyYzqrqp3vhAWVw5Qg`</summary>

```json
{
  "description": "Search for recent WAM candidate selection and V-GPS follow-up work",
  "prompt": "Search for recent papers (2025-2026) on these topics to check if we're missing any important related work:\n\n1. Search \"V-GPS value guided policy steering robot\" to find the original paper and any follow-ups\n2. Search \"world action model candidate selection inference time 2026\"\n3. Search \"action latent space OOD detection robot manipulation 2026\"\n4. Search \"WAM world model action latent value function 2026\"\n\nFor each search, report: paper titles, arxiv IDs, brief descriptions of what each does. Flag anything that directly overlaps with: (a) using OOD detection on WAM/world-model action latents for candidate selection, or (b) value function re-ranking for frozen WAM policies specifically. We need to know if there's any work we're still missing that would weaken novelty claims.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25b7ee3c-f8e3-4d21-baa2-a2cf75fc8c20",
  "isSidechain": false,
  "requestId": "req_011CatdhwBc99m94XmMVxiM2",
  "type": "assistant",
  "uuid": "505b6aaf-6383-4181-866c-9ec6e7567592",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e26c6f2-72e3-4741-87ef-c0d8359a2540",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_011e2LuaUZJunnyTapBjcNfp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3005,
      "cache_read_input_tokens": 31107,
      "output_tokens": 1063,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3005,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1063,
          "cache_read_input_tokens": 31107,
          "cache_creation_input_tokens": 3005,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3005
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

_source line 18 · 2026-05-10T09:16:05.906Z_

<details><summary>↩ Tool result · `toolu_01Hw4SfTZKiNcd2mztRTBJgt`</summary>

```text
Here is what each paper actually does, based on the fetched content:

---

## Paper 1: ALT Policy (arXiv 2505.05787)

**Title:** "Demystifying Diffusion Policies: Action Memorization and Simple Lookup Table Alternatives"

**Abstract (reconstructed from fetch):** The paper argues that diffusion policies work by implicitly memorizing action lookup tables rather than learning to generalize. At runtime, they find the nearest training image in a contrastive latent space and retrieve the associated action sequence. The authors make this mechanism explicit with the Action Lookup Table (ALT) policy, which uses a contrastive image encoder as a hash function to index the closest training action sequence. ALT matches diffusion policy performance on small datasets while requiring far less compute.

**Answers to your specific questions:**
- **Nearest-neighbor OOD detection:** Yes, but in **image observation latent space**, not action latent space. A distance threshold in the contrastive image embedding flags OOD at runtime.
- **Latent space:** Image/observation embedding space (contrastive encoder over visual observations + pose). There is no separate action latent space.
- **Candidate selection vs. retrieval:** Pure retrieval — a single nearest-neighbor lookup over the training set returns a full memorized action trajectory. No candidate selection or ranking step exists; there is exactly one retrieved result.

---

## Paper 2: UNISafe (arXiv 2505.00779)

**Title:** "Uncertainty-aware Latent Safety Filters for Avoiding Out-of-Distribution Failures"

**Abstract summary:** The paper addresses failures of world-model-based safe control (specifically Hamilton-Jacobi reachability) on novel OOD scenarios. It proposes an uncertainty-aware latent safety filter that uses a generative world model's epistemic uncertainty as a proxy for unseen hazards. Conformal prediction calibrates the uncertainty threshold for OOD detection, and reachability analysis is then performed in an augmented state space (latent state + epistemic uncertainty) to synthesize a filter that safeguards arbitrary policies from both known and unknown hazards. Validated on vision-based robotic control with a Franka manipulator.

**Answers to your specific questions:**
- **Conformal prediction + world model uncertainty for OOD:** Yes, explicitly. Conformal prediction calibrates the uncertainty threshold; the world model's epistemic uncertainty is the OOD signal.
- **Safety or candidate selection:** Safety-focused. The filter "safeguards arbitrary policies" and steers the robot away from unsafe regions. It proposes safe in-distribution actions when the nominal policy would enter OOD territory — so it is safety intervention, not candidate selection for task performance.
- **Policy/model architecture:** The base policy is arbitrary (the filter is policy-agnostic). The world model is a generative latent dynamics model (likely RSSM/DreamerV3-style, given citations to Hafner et al., though not named explicitly in the abstract). The safety mechanism is Hamilton-Jacobi reachability in the latent+uncertainty augmented state space. The acronym "UNISafe" appears on the project website but is not prominently in the abstract.

---

## For accurate one-sentence citations:

**ALT Policy:** ALT [citation] demystifies diffusion policies as implicit nearest-neighbor lookup tables, explicitly replacing them with a contrastive image encoder that retrieves the closest training action trajectory in observation latent space and uses the retrieval distance as a runtime OOD detector.

**UNISafe:** UNISafe [citation] proposes a policy-agnostic latent safety filter that uses conformal prediction to calibrate a world model's epistemic uncertainty as an OOD threshold, then performs Hamilton-Jacobi reachability analysis in an augmented latent+uncertainty state space to steer any base policy away from known and unseen safety hazards.

agentId: a6688bd1f0583c624 (use SendMessage with to: 'a6688bd1f0583c624' to continue this agent)
&lt;usage>total_tokens: 13964
tool_uses: 7
duration_ms: 61435&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "25b7ee3c-f8e3-4d21-baa2-a2cf75fc8c20",
  "isSidechain": false,
  "promptId": "d7b557eb-7415-4061-bbb7-58d07ac1d15d",
  "type": "user",
  "uuid": "f990e909-e135-44c8-b144-aa814b67f0e7",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Fetch two papers and summarize each briefly:\n\n1. ALT Policy (arXiv 2505.05787): https://arxiv.org/abs/2505.05787 - Extract the title, abstract, and specifically: does it use nearest-neighbor OOD detection in action latent space? What latent space does it use? How does it relate to candidate selection vs retrieval?\n\n2. UNISafe (arXiv 2505.00779): https://arxiv.org/abs/2505.00779 - Extract the title, abstract, and specifically: does it use conformal prediction + world model uncertainty for OOD-based action filtering? Is it for safety or candidate selection? What policy/model architecture?\n\nReport what each paper actually does so we can write accurate one-sentence citations.",
    "agentId": "a6688bd1f0583c624",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is what each paper actually does, based on the fetched content:\n\n---\n\n## Paper 1: ALT Policy (arXiv 2505.05787)\n\n**Title:** \"Demystifying Diffusion Policies: Action Memorization and Simple Lookup Table Alternatives\"\n\n**Abstract (reconstructed from fetch):** The paper argues that diffusion policies work by implicitly memorizing action lookup tables rather than learning to generalize. At runtime, they find the nearest training image in a contrastive latent space and retrieve the associated action sequence. The authors make this mechanism explicit with the Action Lookup Table (ALT) policy, which uses a contrastive image encoder as a hash function to index the closest training action sequence. ALT matches diffusion policy performance on small datasets while requiring far less compute.\n\n**Answers to your specific questions:**\n- **Nearest-neighbor OOD detection:** Yes, but in **image observation latent space**, not action latent space. A distance threshold in the contrastive image embedding flags OOD at runtime.\n- **Latent space:** Image/observation embedding space (contrastive encoder over visual observations + pose). There is no separate action latent space.\n- **Candidate selection vs. retrieval:** Pure retrieval — a single nearest-neighbor lookup over the training set returns a full memorized action trajectory. No candidate selection or ranking step exists; there is exactly one retrieved result.\n\n---\n\n## Paper 2: UNISafe (arXiv 2505.00779)\n\n**Title:** \"Uncertainty-aware Latent Safety Filters for Avoiding Out-of-Distribution Failures\"\n\n**Abstract summary:** The paper addresses failures of world-model-based safe control (specifically Hamilton-Jacobi reachability) on novel OOD scenarios. It proposes an uncertainty-aware latent safety filter that uses a generative world model's epistemic uncertainty as a proxy for unseen hazards. Conformal prediction calibrates the uncertainty threshold for OOD detection, and reachability analysis is then performed in an augmented state space (latent state + epistemic uncertainty) to synthesize a filter that safeguards arbitrary policies from both known and unknown hazards. Validated on vision-based robotic control with a Franka manipulator.\n\n**Answers to your specific questions:**\n- **Conformal prediction + world model uncertainty for OOD:** Yes, explicitly. Conformal prediction calibrates the uncertainty threshold; the world model's epistemic uncertainty is the OOD signal.\n- **Safety or candidate selection:** Safety-focused. The filter \"safeguards arbitrary policies\" and steers the robot away from unsafe regions. It proposes safe in-distribution actions when the nominal policy would enter OOD territory — so it is safety intervention, not candidate selection for task performance.\n- **Policy/model architecture:** The base policy is arbitrary (the filter is policy-agnostic). The world model is a generative latent dynamics model (likely RSSM/DreamerV3-style, given citations to Hafner et al., though not named explicitly in the abstract). The safety mechanism is Hamilton-Jacobi reachability in the latent+uncertainty augmented state space. The acronym \"UNISafe\" appears on the project website but is not prominently in the abstract.\n\n---\n\n## For accurate one-sentence citations:\n\n**ALT Policy:** ALT [citation] demystifies diffusion policies as implicit nearest-neighbor lookup tables, explicitly replacing them with a contrastive image encoder that retrieves the closest training action trajectory in observation latent space and uses the retrieval distance as a runtime OOD detector.\n\n**UNISafe:** UNISafe [citation] proposes a policy-agnostic latent safety filter that uses conformal prediction to calibrate a world model's epistemic uncertainty as an OOD threshold, then performs Hamilton-Jacobi reachability analysis in an augmented latent+uncertainty state space to steer any base policy away from known and unseen safety hazards."
      }
    ],
    "totalDurationMs": 61435,
    "totalTokens": 13964,
    "totalToolUseCount": 7,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 452,
      "cache_read_input_tokens": 12622,
      "output_tokens": 889,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 452
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 889,
          "cache_read_input_tokens": 12622,
          "cache_creation_input_tokens": 452,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 452,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 7
    }
  },
  "sourceToolAssistantUUID": "25b7ee3c-f8e3-4d21-baa2-a2cf75fc8c20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e26c6f2-72e3-4741-87ef-c0d8359a2540",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 19_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Latent-Distribution Candidate Selection for Frozen World Action Models…",
  "leafUuid": "f990e909-e135-44c8-b144-aa814b67f0e7",
  "sessionId": "4e26c6f2-72e3-4741-87ef-c0d8359a2540"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "WAM latent-space value learning for frozen inference planning",
  "sessionId": "4e26c6f2-72e3-4741-87ef-c0d8359a2540"
}
```

---

### Tool result

_source line 21 · 2026-05-10T09:16:28.242Z_

<details><summary>↩ Tool result · `toolu_019XRHdJHE4WzJJbHRMu8viX`</summary>

```text
I now have all the information needed for a complete and accurate fact-check. Here is the full report:

---

## WAV Paper Findings — arxiv.org/abs/2604.14732

### (1) Abstract — Verbatim Text

"Vision–Language–Action (VLA) models have emerged as a promising paradigm for building embodied agents that ground perception and language into action. However, most existing approaches rely on direct action prediction, lacking the ability to reason over long-horizon trajectories and evaluate their consequences, which limits performance in complex decision-making tasks. In this work, we introduce World–Value–Action (WAV) model, a unified framework that enables implicit planning in VLA systems. Rather than performing explicit trajectory optimization, WAV model learn a structured latent representation of future trajectories conditioned on visual observations and language instructions. A learned world model predicts future states, while a trajectory value function evaluates their long-horizon utility. Action generation is then formulated as inference in this latent space, where the model progressively concentrates probability mass on high-value and dynamically feasible trajectories. We provide a theoretical perspective showing that planning directly in action space suffers from an exponential decay in the probability of feasible trajectories as the horizon increases. In contrast, latent-space inference reshapes the search distribution toward feasible regions, enabling efficient long-horizon decision making. Extensive simulations and real-world experiments demonstrate that the WAV model consistently outperforms state-of-the-art methods, achieving significant improvements in task success rate, generalization ability, and robustness, especially in long-horizon and compositional scenarios."

---

### (2) LIBERO Benchmark Results — Table 1

**Table 1 caption:** "Performance comparison on the LIBERO benchmark."

The table covers four LIBERO splits: **LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-Long**, and an **Avg.** column. There is **no LIBERO-90 column** in the table.

WAV (Ours) results (2.2B params):

| Split | Score |
|---|---|
| LIBERO-Spatial | **100.0%** |
| LIBERO-Object | **98.6%** |
| LIBERO-Goal | **94.4%** |
| LIBERO-Long | **98.1%** |
| **Avg.** | **99.6%** |

The **99.6% figure is the overall average** across those four splits, not a score on any single split. The ablation row ("W/o Latent Trajectory Planning") scores 99.6% on LIBERO-Spatial specifically, and 99.0% average — this is a potential source of confusion.

The **98.1% figure appears for LIBERO-Long**, not as an overall score.

---

### (3) Real-World Robot Experiment Results — Figure 2

**Figure 2 caption:** "Quantitative comparison between WAV model (Ours) and the GE-ACT (Baseline) on real-world tasks. Each result is averaged over 15 trials."

- WAV (Ours): **75.6%** average success rate
- GE-ACT (Baseline): **35.6%** average success rate

The real-world experiments are conducted on a **Piper dual-arm robot platform**. Results are presented as a **bar chart (Figure 2)**, not a table. No per-task breakdown percentages are given in the text — only the aggregate 75.6% average across all tasks. There is no Table 2 for real-world results.

---

### Verdict on the Claim

The claim "LIBERO = 99.6% and real-world = 75.6%" is **directionally correct** but needs precise framing:

- **99.6%** — CONFIRMED. This is WAV's **overall average** across four LIBERO splits (Spatial/Object/Goal/Long), per **Table 1**. It is not a score on a single split like LIBERO-90 (which does not appear in the paper's table at all).
- **75.6%** — CONFIRMED. This is WAV's **average real-world success rate** across all real-world tasks on a Piper dual-arm robot, from **Figure 2**, averaged over 15 trials per task, compared to a 35.6% baseline (GE-ACT).
- **98.1%** is WAV's score specifically on the **LIBERO-Long** split, not an overall figure.
- **LIBERO-90** does not appear in the paper's benchmark table at all.

agentId: a22c27b681a267bea (use SendMessage with to: 'a22c27b681a267bea' to continue this agent)
&lt;usage>total_tokens: 15245
tool_uses: 6
duration_ms: 88679&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e3f09d9-295a-48ea-96db-f3a0a31200d9",
  "isSidechain": false,
  "promptId": "d7b557eb-7415-4061-bbb7-58d07ac1d15d",
  "type": "user",
  "uuid": "01aa356a-e98c-481d-a74d-96eae210543f",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Fetch the WAV (World-Value-Action Model) paper at https://arxiv.org/abs/2604.14732 and extract: (1) the exact LIBERO benchmark results - specifically which LIBERO split (LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-Long, LIBERO-90, overall average?) and what score (99.6%? 98.1%? something else?), with exact table reference; (2) any real-world robot experiment results - what percentage, which task, which table/figure; (3) the abstract text verbatim. The claim being checked: LIBERO = 99.6% and real-world = 75.6%. Report exactly what numbers appear in the paper and where.",
    "agentId": "a22c27b681a267bea",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have all the information needed for a complete and accurate fact-check. Here is the full report:\n\n---\n\n## WAV Paper Findings — arxiv.org/abs/2604.14732\n\n### (1) Abstract — Verbatim Text\n\n\"Vision–Language–Action (VLA) models have emerged as a promising paradigm for building embodied agents that ground perception and language into action. However, most existing approaches rely on direct action prediction, lacking the ability to reason over long-horizon trajectories and evaluate their consequences, which limits performance in complex decision-making tasks. In this work, we introduce World–Value–Action (WAV) model, a unified framework that enables implicit planning in VLA systems. Rather than performing explicit trajectory optimization, WAV model learn a structured latent representation of future trajectories conditioned on visual observations and language instructions. A learned world model predicts future states, while a trajectory value function evaluates their long-horizon utility. Action generation is then formulated as inference in this latent space, where the model progressively concentrates probability mass on high-value and dynamically feasible trajectories. We provide a theoretical perspective showing that planning directly in action space suffers from an exponential decay in the probability of feasible trajectories as the horizon increases. In contrast, latent-space inference reshapes the search distribution toward feasible regions, enabling efficient long-horizon decision making. Extensive simulations and real-world experiments demonstrate that the WAV model consistently outperforms state-of-the-art methods, achieving significant improvements in task success rate, generalization ability, and robustness, especially in long-horizon and compositional scenarios.\"\n\n---\n\n### (2) LIBERO Benchmark Results — Table 1\n\n**Table 1 caption:** \"Performance comparison on the LIBERO benchmark.\"\n\nThe table covers four LIBERO splits: **LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-Long**, and an **Avg.** column. There is **no LIBERO-90 column** in the table.\n\nWAV (Ours) results (2.2B params):\n\n| Split | Score |\n|---|---|\n| LIBERO-Spatial | **100.0%** |\n| LIBERO-Object | **98.6%** |\n| LIBERO-Goal | **94.4%** |\n| LIBERO-Long | **98.1%** |\n| **Avg.** | **99.6%** |\n\nThe **99.6% figure is the overall average** across those four splits, not a score on any single split. The ablation row (\"W/o Latent Trajectory Planning\") scores 99.6% on LIBERO-Spatial specifically, and 99.0% average — this is a potential source of confusion.\n\nThe **98.1% figure appears for LIBERO-Long**, not as an overall score.\n\n---\n\n### (3) Real-World Robot Experiment Results — Figure 2\n\n**Figure 2 caption:** \"Quantitative comparison between WAV model (Ours) and the GE-ACT (Baseline) on real-world tasks. Each result is averaged over 15 trials.\"\n\n- WAV (Ours): **75.6%** average success rate\n- GE-ACT (Baseline): **35.6%** average success rate\n\nThe real-world experiments are conducted on a **Piper dual-arm robot platform**. Results are presented as a **bar chart (Figure 2)**, not a table. No per-task breakdown percentages are given in the text — only the aggregate 75.6% average across all tasks. There is no Table 2 for real-world results.\n\n---\n\n### Verdict on the Claim\n\nThe claim \"LIBERO = 99.6% and real-world = 75.6%\" is **directionally correct** but needs precise framing:\n\n- **99.6%** — CONFIRMED. This is WAV's **overall average** across four LIBERO splits (Spatial/Object/Goal/Long), per **Table 1**. It is not a score on a single split like LIBERO-90 (which does not appear in the paper's table at all).\n- **75.6%** — CONFIRMED. This is WAV's **average real-world success rate** across all real-world tasks on a Piper dual-arm robot, from **Figure 2**, averaged over 15 trials per task, compared to a 35.6% baseline (GE-ACT).\n- **98.1%** is WAV's score specifically on the **LIBERO-Long** split, not an overall figure.\n- **LIBERO-90** does not appear in the paper's benchmark table at all."
      }
    ],
    "totalDurationMs": 88679,
    "totalTokens": 15245,
    "totalToolUseCount": 6,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1014,
      "cache_read_input_tokens": 13158,
      "output_tokens": 1072,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1014
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1072,
          "cache_read_input_tokens": 13158,
          "cache_creation_input_tokens": 1014,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1014,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 6
    }
  },
  "sourceToolAssistantUUID": "5e3f09d9-295a-48ea-96db-f3a0a31200d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e26c6f2-72e3-4741-87ef-c0d8359a2540",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-10T09:16:39.997Z_

<details><summary>↩ Tool result · `toolu_01BRM9kHnero17KJauHCTisa`</summary>

```text
I now have comprehensive information. Here is the full extraction:

---

## V-GPS Paper: "Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance"

---

### (1) Exact Title

**"Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance"**

---

### (2) Abstract (verbatim)

"Large, general-purpose robotic policies trained on diverse demonstration datasets have been shown to be remarkably effective both for controlling a variety of robots in a range of different scenes, and for acquiring broad repertoires of manipulation skills. However, the data that such policies are trained on is generally of mixed quality – not only are human-collected demonstrations unlikely to perform the task perfectly, but the larger the dataset is, the harder it is to curate only the highest quality examples. It also remains unclear how optimal data from one embodiment is for training on another embodiment. In this paper, we present a general and broadly applicable approach that enhances the performance of such generalist robot policies at deployment time by re-ranking their actions according to a value function learned via offline RL. This approach, which we call Value-Guided Policy Steering (V-GPS), is compatible with a wide range of different generalist policies, without needing to fine-tune or even access the weights of the policy. We show that the same value function can improve the performance of five different state-of-the-art policies with different architectures, even though they were trained on distinct datasets, attaining consistent performance improvement on multiple robotic platforms across a total of 12 tasks."

---

### (3) Core Method: Value Function Training

**How the value function is trained:**
The value function is a language-conditioned Q-function trained using **Calibrated Q-Learning (Cal-QL)**, an offline RL algorithm. Key details:

- **Architecture:** ResNet-34 image encoder with FiLM language conditioning. The 7-dimensional action vector is concatenated with the final ResNet output and passed through two 256-unit hidden layers to predict a scalar Q-value.
- **Reward labels:** Trajectories are annotated with a sparse binary reward. "The last H transitions of a trajectory [are labeled] with a sparse binary reward value of +1 to indicate completion of the task" (H=3). All other transitions receive 0. The paper notes a shifted variant using 0 and -1 instead.
- **Objective (Cal-QL):** The training objective includes a calibrated conservative regularizer that penalizes out-of-distribution actions while compensating on in-distribution data:
  `J_Q(θ) = α[E max(Q_θ(s,a,l), Q_μ(s,a,l)) − E Q_θ(s,a,l)] + ½E[(Q_θ(s,a,l) − B^π Q_θ̄(s,a,l))²]`
- **Crucially, the value function does not require access to policy weights** — it is trained separately on offline data and applied at deployment time.

**Policy architectures it applies to (all five tested):**
1. **Octo-small** (27M parameters, ViT-S backbone)
2. **Octo-base** (93M parameters, ViT-B backbone)
3. **Octo-small-1.5** (updated Octo with augmented language)
4. **RT-1X** (35M parameter transformer policy)
5. **OpenVLA** (7B parameter vision-language-action model)

**The +82.8% improvement claim:**
- **Benchmark:** 6 real-world manipulation tasks across 3 scenes on a WidowX250 robot arm (e.g., "put pepper in pot," "put mushroom on cloth")
- **Baseline:** Octo-small-1.5 without V-GPS
- **Numbers:** Baseline average success rate = 0.24; V-GPS = 0.44; improvement = **+82.8%** (relative)
- Exact table entry: "Total Average | 0.24 | 0.44 | +82.8%"
- Decomposed by scene: "+55% in Scene A, +92% in Scene B, and +100% in Scene C"

---

### (4) How Candidate Actions Are Generated

Actions are sampled stochastically from the generalist policy itself — no separate proposal model is needed. The procedure (verbatim from the paper):

"Sample {a₁, …, aₖ} ~ π(a | sₜ, l)" — K actions are drawn from the policy's distribution at each timestep, given the current observation sₜ and language prompt l.

- K = **50** for real-world experiments; K ∈ {10, 50} in simulation sweeps.
- After sampling, the value function scores each candidate. The final action is selected either **greedily** (argmax over Q-values) or by **temperature-controlled softmax re-ranking**:
  `aₜ ~ Softmax(Q_θ(sₜ, a₁)/β, …, Q_θ(sₜ, aₖ)/β)`
  where β is a temperature parameter controlling how sharply to weight high-value actions.

---

### (5) Action Representation Space the Value Function Operates On

The value function operates on **7-dimensional action vectors** — the same format output by the generalist policies themselves. These 7 dimensions correspond to 6-DOF arm control (position + orientation, consistent with delta XYZ + RPY/Euler angles for a WidowX arm) plus a gripper open/close dimension. The paper does not explicitly label each dimension but states:

"The 7-dimensional actions are concatenated with the final output from the ResNet, then passed through two 256-unit hidden layers"

to produce the scalar Q-value. Critically, the value function operates in the **policy's native action space** — it takes a (state image, language, action candidate) tuple as input and returns a scalar value estimate. It does not operate in a latent or embedding space; it consumes the raw action vector directly.

agentId: ab3e476b93fb1a162 (use SendMessage with to: 'ab3e476b93fb1a162' to continue this agent)
&lt;usage>total_tokens: 14538
tool_uses: 6
duration_ms: 105892&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5538bec1-031a-4caa-8722-04da17ab2429",
  "isSidechain": false,
  "promptId": "d7b557eb-7415-4061-bbb7-58d07ac1d15d",
  "type": "user",
  "uuid": "c7bc3e7a-945f-4ca4-9184-3cbe4b65eb6f",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Fetch the V-GPS paper at https://arxiv.org/abs/2410.13816 and extract: (1) the exact title, (2) the abstract, (3) the core method description - specifically how the value function is trained, what policy architectures it applies to (Octo, RT-1X, OpenVLA?), what the +82.8% improvement claim refers to (which benchmark, which baseline), (4) how candidate actions are generated, (5) what action representation space the value function operates on. Report verbatim quotes where possible.",
    "agentId": "ab3e476b93fb1a162",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive information. Here is the full extraction:\n\n---\n\n## V-GPS Paper: \"Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance\"\n\n---\n\n### (1) Exact Title\n\n**\"Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance\"**\n\n---\n\n### (2) Abstract (verbatim)\n\n\"Large, general-purpose robotic policies trained on diverse demonstration datasets have been shown to be remarkably effective both for controlling a variety of robots in a range of different scenes, and for acquiring broad repertoires of manipulation skills. However, the data that such policies are trained on is generally of mixed quality – not only are human-collected demonstrations unlikely to perform the task perfectly, but the larger the dataset is, the harder it is to curate only the highest quality examples. It also remains unclear how optimal data from one embodiment is for training on another embodiment. In this paper, we present a general and broadly applicable approach that enhances the performance of such generalist robot policies at deployment time by re-ranking their actions according to a value function learned via offline RL. This approach, which we call Value-Guided Policy Steering (V-GPS), is compatible with a wide range of different generalist policies, without needing to fine-tune or even access the weights of the policy. We show that the same value function can improve the performance of five different state-of-the-art policies with different architectures, even though they were trained on distinct datasets, attaining consistent performance improvement on multiple robotic platforms across a total of 12 tasks.\"\n\n---\n\n### (3) Core Method: Value Function Training\n\n**How the value function is trained:**\nThe value function is a language-conditioned Q-function trained using **Calibrated Q-Learning (Cal-QL)**, an offline RL algorithm. Key details:\n\n- **Architecture:** ResNet-34 image encoder with FiLM language conditioning. The 7-dimensional action vector is concatenated with the final ResNet output and passed through two 256-unit hidden layers to predict a scalar Q-value.\n- **Reward labels:** Trajectories are annotated with a sparse binary reward. \"The last H transitions of a trajectory [are labeled] with a sparse binary reward value of +1 to indicate completion of the task\" (H=3). All other transitions receive 0. The paper notes a shifted variant using 0 and -1 instead.\n- **Objective (Cal-QL):** The training objective includes a calibrated conservative regularizer that penalizes out-of-distribution actions while compensating on in-distribution data:\n  `J_Q(θ) = α[E max(Q_θ(s,a,l), Q_μ(s,a,l)) − E Q_θ(s,a,l)] + ½E[(Q_θ(s,a,l) − B^π Q_θ̄(s,a,l))²]`\n- **Crucially, the value function does not require access to policy weights** — it is trained separately on offline data and applied at deployment time.\n\n**Policy architectures it applies to (all five tested):**\n1. **Octo-small** (27M parameters, ViT-S backbone)\n2. **Octo-base** (93M parameters, ViT-B backbone)\n3. **Octo-small-1.5** (updated Octo with augmented language)\n4. **RT-1X** (35M parameter transformer policy)\n5. **OpenVLA** (7B parameter vision-language-action model)\n\n**The +82.8% improvement claim:**\n- **Benchmark:** 6 real-world manipulation tasks across 3 scenes on a WidowX250 robot arm (e.g., \"put pepper in pot,\" \"put mushroom on cloth\")\n- **Baseline:** Octo-small-1.5 without V-GPS\n- **Numbers:** Baseline average success rate = 0.24; V-GPS = 0.44; improvement = **+82.8%** (relative)\n- Exact table entry: \"Total Average | 0.24 | 0.44 | +82.8%\"\n- Decomposed by scene: \"+55% in Scene A, +92% in Scene B, and +100% in Scene C\"\n\n---\n\n### (4) How Candidate Actions Are Generated\n\nActions are sampled stochastically from the generalist policy itself — no separate proposal model is needed. The procedure (verbatim from the paper):\n\n\"Sample {a₁, …, aₖ} ~ π(a | sₜ, l)\" — K actions are drawn from the policy's distribution at each timestep, given the current observation sₜ and language prompt l.\n\n- K = **50** for real-world experiments; K ∈ {10, 50} in simulation sweeps.\n- After sampling, the value function scores each candidate. The final action is selected either **greedily** (argmax over Q-values) or by **temperature-controlled softmax re-ranking**:\n  `aₜ ~ Softmax(Q_θ(sₜ, a₁)/β, …, Q_θ(sₜ, aₖ)/β)`\n  where β is a temperature parameter controlling how sharply to weight high-value actions.\n\n---\n\n### (5) Action Representation Space the Value Function Operates On\n\nThe value function operates on **7-dimensional action vectors** — the same format output by the generalist policies themselves. These 7 dimensions correspond to 6-DOF arm control (position + orientation, consistent with delta XYZ + RPY/Euler angles for a WidowX arm) plus a gripper open/close dimension. The paper does not explicitly label each dimension but states:\n\n\"The 7-dimensional actions are concatenated with the final output from the ResNet, then passed through two 256-unit hidden layers\"\n\nto produce the scalar Q-value. Critically, the value function operates in the **policy's native action space** — it takes a (state image, language, action candidate) tuple as input and returns a scalar value estimate. It does not operate in a latent or embedding space; it consumes the raw action vector directly."
      }
    ],
    "totalDurationMs": 105892,
    "totalTokens": 14538,
    "totalToolUseCount": 6,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 537,
      "cache_read_input_tokens": 12567,
      "output_tokens": 1433,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 537
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1433,
          "cache_read_input_tokens": 12567,
          "cache_creation_input_tokens": 537,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 537,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 6
    }
  },
  "sourceToolAssistantUUID": "5538bec1-031a-4caa-8722-04da17ab2429",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e26c6f2-72e3-4741-87ef-c0d8359a2540",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-10T09:17:05.546Z_

<details><summary>↩ Tool result · `toolu_013fpMKyYzqrqp3vhAWVw5Qg`</summary>

```text
I now have a comprehensive picture. Here is the full findings report:

---

## Related Work Search Report

### Search 1: V-GPS — Original Paper and Follow-ups

**Original Paper:**

- **"Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance" (V-GPS)**
  - ArXiv: [2410.13816](https://arxiv.org/abs/2410.13816) | CoRL 2024
  - What it does: Trains a value function via offline RL, then at inference samples multiple action candidates from a frozen generalist policy and re-ranks them by value. Works across five different policy architectures (Octo, etc.) without accessing policy weights. Gains up to +100% on some tasks.
  - **Overlap flag (b):** This is the primary prior art for value-function re-ranking of frozen policies. Any claim to novelty in that direction must differentiate from V-GPS explicitly.

**Direct Follow-ups Found:**

- **VLS: Steering Pretrained Robot Policies via Vision-Language Models**
  - ArXiv: [2602.03973](https://arxiv.org/abs/2602.03973) | Feb 2026
  - What it does: Training-free inference-time steering of frozen diffusion/flow-matching policies using a VLM to synthesize trajectory-differentiable reward functions that guide denoising. Addresses OOD spatial/semantic shifts. +31% on CALVIN, +13% on LIBERO-Pro.
  - **Overlap flag:** Uses inference-time guidance on frozen policies, but the steering mechanism is VLM-reward-gradient-based (not value-function re-ranking, not OOD on WAM latents). Differentiated.

No other direct V-GPS follow-ups that apply value re-ranking specifically to WAM/world-model policies were found.

---

### Search 2: World Action Model Candidate Selection / Inference-Time Compute

**Key papers found:**

- **GPC: Inference-Time Enhancement of Generative Robot Policies via Predictive World Modeling**
  - ArXiv: [2502.00622](https://arxiv.org/abs/2502.00622) | Updated March 2026
  - What it does: Augments a frozen diffusion policy with a separately trained action-conditioned world model. At inference, samples multiple action proposals from the frozen policy, rolls each through the world model, and selects the one with highest predicted reward (model-based look-ahead). Uses predicted future states — not latent-space OOD scores — as the selection criterion.
  - **Overlap flag (b):** High relevance — this is the closest existing work to value/world-model-guided candidate selection for frozen policies. Key distinction: GPC uses explicit world-model rollout + reward prediction, not OOD detection on action latents. The world model is separate from the policy, not a unified WAM.

- **Fast-WAM: Do World Action Models Need Test-time Future Imagination?**
  - ArXiv: [2603.16666](https://arxiv.org/abs/2603.16666) | March 2026
  - What it does: Asks whether WAMs actually need to generate future video at inference. Answer: no — retaining video co-training but skipping future generation at test-time achieves competitive results with 4x lower latency (190ms). Value is in training representations, not test-time rollouts.
  - **Overlap flag:** Not directly overlapping with OOD-based candidate selection. Relevant context for WAM design space.

- **"When to Trust Imagination": Adaptive Action Execution for World Action Models**
  - ArXiv: [2605.06222](https://arxiv.org/abs/2605.06222) | May 2026
  - What it does: Proposes FFDC — a lightweight verifier that checks whether the WAM's predicted future remains consistent with real observations, deciding when to replan vs. continue executing. Reduces forward passes by 69%, improves success rate by 2.54–35%. Framed as future-reality verification, not OOD on action latents.
  - **Overlap flag (a):** Moderate. This also uses the WAM's predicted future to make execution decisions, but the mechanism is checking visual consistency between predicted and real observations — not OOD detection on action latents for candidate selection at the start of inference.

- **World Action Models are Zero-shot Policies (DreamZero)**
  - ArXiv: [2602.15922](https://arxiv.org/abs/2602.15922) | Feb 2026
  - What it does: Uses WAMs as zero-shot policies by treating action generation as a planning problem through the world model's latent space.

---

### Search 3: Action Latent Space OOD Detection for Robot Manipulation

**Key papers found:**

- **UNISafe: Uncertainty-aware Latent Safety Filters for Avoiding Out-of-Distribution Failures**
  - ArXiv: [2505.00779](https://arxiv.org/abs/2505.00779) | CoRL 2025
  - What it does: Uses a latent world model's epistemic uncertainty (calibrated via conformal prediction) to detect OOD predictions and synthesize a safety filter that steers away from unsafe/unseen states. Policy-agnostic — works as a wrapper around arbitrary policies.
  - **Overlap flag (a):** This is the closest paper found to OOD detection on world-model latents in robotics. However, the purpose is safety filtering (avoiding hazardous states), not candidate selection/re-ranking among multiple action proposals. The latent space involved is the world model's state latent, not the action latent specifically. Scope is safety, not policy improvement.

- No papers were found that apply OOD detection directly to WAM action latents for the purpose of candidate selection/re-ranking.

---

### Search 4: WAM + Value Function (direct query)

**Key papers found:**

- **World-Value-Action (WAV) Model: Implicit Planning for Vision-Language-Action Systems**
  - ArXiv: [2604.14732](https://arxiv.org/abs/2604.14732) | April 2026
  - What it does: Trains a unified model combining a world model (predicts future states) and a value function (evaluates trajectory utility). Action generation is formulated as inference in a structured latent space, progressively concentrating probability on high-value, dynamically feasible trajectories. This is a jointly trained, end-to-end system — not a frozen WAM + separate OOD or value module.
  - **Overlap flag (b):** High relevance — explicitly combines world model + value function for action selection. Key distinction: WAV trains value and world model jointly from scratch; it does not apply OOD detection or value re-ranking to a frozen/pre-trained WAM.

- **Best-of-Q: Improving VLM Agents with Q-function Action Ranking at Inference**
  - ArXiv: [2601.22701](https://arxiv.org/abs/2601.22701) | Jan 2026
  - What it does: Keeps a frozen VLM policy as the candidate generator; trains a lightweight offline Q-function separately; at inference re-ranks candidates by Q-value. Designed for digital agents (web/OS control), not physical robot manipulation.
  - **Overlap flag (b):** The mechanism is nearly identical to V-GPS applied to VLM agents rather than robot policies. Not in the WAM/robot manipulation space.

---

## Summary: Novelty Threat Assessment

| Prior Work | Overlap with (a): OOD on WAM action latents for candidate selection | Overlap with (b): Value re-ranking for frozen WAM policies |
|---|---|---|
| V-GPS (2410.13816) | None | **High** — foundational method, but for generalist vision policies, not WAMs specifically |
| GPC (2502.00622) | Partial — uses world model to score candidates, but via reward prediction not OOD | **Moderate** — frozen policy + world model scoring; world model is separate, not WAM |
| WAV Model (2604.14732) | None | **Moderate** — combines value + world model, but jointly trained, not frozen WAM |
| Best-of-Q (2601.22701) | None | **Moderate** — Q-function re-ranking of frozen policy, but for VLM agents not robot WAMs |
| UNISafe (2505.00779) | **Moderate** — OOD on world model latents, but for safety not candidate selection | None |
| "When to Trust Imagination" (2605.06222) | **Low-Moderate** — WAM future verification, but visual consistency not action latent OOD | None |
| VLS (2602.03973) | None | None (different mechanism: VLM gradient steering) |
| Fast-WAM (2603.16666) | None | None (addresses inference latency, not candidate selection) |

**Bottom line:** No paper found combines both (a) and (b) — i.e., using OOD detection on WAM/world-model action latents specifically for candidate selection/re-ranking of a frozen WAM policy. The closest threats are V-GPS (value re-ranking, but not WAM-specific), GPC (world-model candidate scoring for frozen policies, but reward-prediction not OOD), and UNISafe (OOD on world-model latents, but for safety not candidate selection). The specific combination of WAM action latent OOD + frozen WAM + candidate selection appears unaddressed in the literature as of May 2026.

Sources:
- [Steering Your Generalists: V-GPS (2410.13816)](https://arxiv.org/abs/2410.13816)
- [VLS: Steering Pretrained Robot Policies via Vision-Language Models (2602.03973)](https://arxiv.org/abs/2602.03973)
- [Inference-Time Enhancement via Predictive World Modeling / GPC (2502.00622)](https://arxiv.org/abs/2502.00622)
- [Fast-WAM: Do World Action Models Need Test-time Future Imagination? (2603.16666)](https://arxiv.org/abs/2603.16666)
- [When to Trust Imagination: Adaptive Action Execution for WAMs (2605.06222)](https://arxiv.org/abs/2605.06222)
- [World Action Models are Zero-shot Policies / DreamZero (2602.15922)](https://arxiv.org/abs/2602.15922)
- [World-Value-Action Model: Implicit Planning for VLA Systems (2604.14732)](https://arxiv.org/abs/2604.14732)
- [Best-of-Q: Q-function Action Ranking at Inference (2601.22701)](https://arxiv.org/abs/2601.22701)
- [UNISafe: Uncertainty-aware Latent Safety Filters (2505.00779)](https://arxiv.org/abs/2505.00779)
- [V-GPS Project Page](https://nakamotoo.github.io/V-GPS/)

agentId: a70521f73551d71c7 (use SendMessage with to: 'a70521f73551d71c7' to continue this agent)
&lt;usage>total_tokens: 26458
tool_uses: 15
duration_ms: 115444&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "505b6aaf-6383-4181-866c-9ec6e7567592",
  "isSidechain": false,
  "promptId": "d7b557eb-7415-4061-bbb7-58d07ac1d15d",
  "type": "user",
  "uuid": "ebc933e7-90f9-43f1-bb64-2790fbd7bf0c",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for recent papers (2025-2026) on these topics to check if we're missing any important related work:\n\n1. Search \"V-GPS value guided policy steering robot\" to find the original paper and any follow-ups\n2. Search \"world action model candidate selection inference time 2026\"\n3. Search \"action latent space OOD detection robot manipulation 2026\"\n4. Search \"WAM world model action latent value function 2026\"\n\nFor each search, report: paper titles, arxiv IDs, brief descriptions of what each does. Flag anything that directly overlaps with: (a) using OOD detection on WAM/world-model action latents for candidate selection, or (b) value function re-ranking for frozen WAM policies specifically. We need to know if there's any work we're still missing that would weaken novelty claims.",
    "agentId": "a70521f73551d71c7",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have a comprehensive picture. Here is the full findings report:\n\n---\n\n## Related Work Search Report\n\n### Search 1: V-GPS — Original Paper and Follow-ups\n\n**Original Paper:**\n\n- **\"Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance\" (V-GPS)**\n  - ArXiv: [2410.13816](https://arxiv.org/abs/2410.13816) | CoRL 2024\n  - What it does: Trains a value function via offline RL, then at inference samples multiple action candidates from a frozen generalist policy and re-ranks them by value. Works across five different policy architectures (Octo, etc.) without accessing policy weights. Gains up to +100% on some tasks.\n  - **Overlap flag (b):** This is the primary prior art for value-function re-ranking of frozen policies. Any claim to novelty in that direction must differentiate from V-GPS explicitly.\n\n**Direct Follow-ups Found:**\n\n- **VLS: Steering Pretrained Robot Policies via Vision-Language Models**\n  - ArXiv: [2602.03973](https://arxiv.org/abs/2602.03973) | Feb 2026\n  - What it does: Training-free inference-time steering of frozen diffusion/flow-matching policies using a VLM to synthesize trajectory-differentiable reward functions that guide denoising. Addresses OOD spatial/semantic shifts. +31% on CALVIN, +13% on LIBERO-Pro.\n  - **Overlap flag:** Uses inference-time guidance on frozen policies, but the steering mechanism is VLM-reward-gradient-based (not value-function re-ranking, not OOD on WAM latents). Differentiated.\n\nNo other direct V-GPS follow-ups that apply value re-ranking specifically to WAM/world-model policies were found.\n\n---\n\n### Search 2: World Action Model Candidate Selection / Inference-Time Compute\n\n**Key papers found:**\n\n- **GPC: Inference-Time Enhancement of Generative Robot Policies via Predictive World Modeling**\n  - ArXiv: [2502.00622](https://arxiv.org/abs/2502.00622) | Updated March 2026\n  - What it does: Augments a frozen diffusion policy with a separately trained action-conditioned world model. At inference, samples multiple action proposals from the frozen policy, rolls each through the world model, and selects the one with highest predicted reward (model-based look-ahead). Uses predicted future states — not latent-space OOD scores — as the selection criterion.\n  - **Overlap flag (b):** High relevance — this is the closest existing work to value/world-model-guided candidate selection for frozen policies. Key distinction: GPC uses explicit world-model rollout + reward prediction, not OOD detection on action latents. The world model is separate from the policy, not a unified WAM.\n\n- **Fast-WAM: Do World Action Models Need Test-time Future Imagination?**\n  - ArXiv: [2603.16666](https://arxiv.org/abs/2603.16666) | March 2026\n  - What it does: Asks whether WAMs actually need to generate future video at inference. Answer: no — retaining video co-training but skipping future generation at test-time achieves competitive results with 4x lower latency (190ms). Value is in training representations, not test-time rollouts.\n  - **Overlap flag:** Not directly overlapping with OOD-based candidate selection. Relevant context for WAM design space.\n\n- **\"When to Trust Imagination\": Adaptive Action Execution for World Action Models**\n  - ArXiv: [2605.06222](https://arxiv.org/abs/2605.06222) | May 2026\n  - What it does: Proposes FFDC — a lightweight verifier that checks whether the WAM's predicted future remains consistent with real observations, deciding when to replan vs. continue executing. Reduces forward passes by 69%, improves success rate by 2.54–35%. Framed as future-reality verification, not OOD on action latents.\n  - **Overlap flag (a):** Moderate. This also uses the WAM's predicted future to make execution decisions, but the mechanism is checking visual consistency between predicted and real observations — not OOD detection on action latents for candidate selection at the start of inference.\n\n- **World Action Models are Zero-shot Policies (DreamZero)**\n  - ArXiv: [2602.15922](https://arxiv.org/abs/2602.15922) | Feb 2026\n  - What it does: Uses WAMs as zero-shot policies by treating action generation as a planning problem through the world model's latent space.\n\n---\n\n### Search 3: Action Latent Space OOD Detection for Robot Manipulation\n\n**Key papers found:**\n\n- **UNISafe: Uncertainty-aware Latent Safety Filters for Avoiding Out-of-Distribution Failures**\n  - ArXiv: [2505.00779](https://arxiv.org/abs/2505.00779) | CoRL 2025\n  - What it does: Uses a latent world model's epistemic uncertainty (calibrated via conformal prediction) to detect OOD predictions and synthesize a safety filter that steers away from unsafe/unseen states. Policy-agnostic — works as a wrapper around arbitrary policies.\n  - **Overlap flag (a):** This is the closest paper found to OOD detection on world-model latents in robotics. However, the purpose is safety filtering (avoiding hazardous states), not candidate selection/re-ranking among multiple action proposals. The latent space involved is the world model's state latent, not the action latent specifically. Scope is safety, not policy improvement.\n\n- No papers were found that apply OOD detection directly to WAM action latents for the purpose of candidate selection/re-ranking.\n\n---\n\n### Search 4: WAM + Value Function (direct query)\n\n**Key papers found:**\n\n- **World-Value-Action (WAV) Model: Implicit Planning for Vision-Language-Action Systems**\n  - ArXiv: [2604.14732](https://arxiv.org/abs/2604.14732) | April 2026\n  - What it does: Trains a unified model combining a world model (predicts future states) and a value function (evaluates trajectory utility). Action generation is formulated as inference in a structured latent space, progressively concentrating probability on high-value, dynamically feasible trajectories. This is a jointly trained, end-to-end system — not a frozen WAM + separate OOD or value module.\n  - **Overlap flag (b):** High relevance — explicitly combines world model + value function for action selection. Key distinction: WAV trains value and world model jointly from scratch; it does not apply OOD detection or value re-ranking to a frozen/pre-trained WAM.\n\n- **Best-of-Q: Improving VLM Agents with Q-function Action Ranking at Inference**\n  - ArXiv: [2601.22701](https://arxiv.org/abs/2601.22701) | Jan 2026\n  - What it does: Keeps a frozen VLM policy as the candidate generator; trains a lightweight offline Q-function separately; at inference re-ranks candidates by Q-value. Designed for digital agents (web/OS control), not physical robot manipulation.\n  - **Overlap flag (b):** The mechanism is nearly identical to V-GPS applied to VLM agents rather than robot policies. Not in the WAM/robot manipulation space.\n\n---\n\n## Summary: Novelty Threat Assessment\n\n| Prior Work | Overlap with (a): OOD on WAM action latents for candidate selection | Overlap with (b): Value re-ranking for frozen WAM policies |\n|---|---|---|\n| V-GPS (2410.13816) | None | **High** — foundational method, but for generalist vision policies, not WAMs specifically |\n| GPC (2502.00622) | Partial — uses world model to score candidates, but via reward prediction not OOD | **Moderate** — frozen policy + world model scoring; world model is separate, not WAM |\n| WAV Model (2604.14732) | None | **Moderate** — combines value + world model, but jointly trained, not frozen WAM |\n| Best-of-Q (2601.22701) | None | **Moderate** — Q-function re-ranking of frozen policy, but for VLM agents not robot WAMs |\n| UNISafe (2505.00779) | **Moderate** — OOD on world model latents, but for safety not candidate selection | None |\n| \"When to Trust Imagination\" (2605.06222) | **Low-Moderate** — WAM future verification, but visual consistency not action latent OOD | None |\n| VLS (2602.03973) | None | None (different mechanism: VLM gradient steering) |\n| Fast-WAM (2603.16666) | None | None (addresses inference latency, not candidate selection) |\n\n**Bottom line:** No paper found combines both (a) and (b) — i.e., using OOD detection on WAM/world-model action latents specifically for candidate selection/re-ranking of a frozen WAM policy. The closest threats are V-GPS (value re-ranking, but not WAM-specific), GPC (world-model candidate scoring for frozen policies, but reward-prediction not OOD), and UNISafe (OOD on world-model latents, but for safety not candidate selection). The specific combination of WAM action latent OOD + frozen WAM + candidate selection appears unaddressed in the literature as of May 2026.\n\nSources:\n- [Steering Your Generalists: V-GPS (2410.13816)](https://arxiv.org/abs/2410.13816)\n- [VLS: Steering Pretrained Robot Policies via Vision-Language Models (2602.03973)](https://arxiv.org/abs/2602.03973)\n- [Inference-Time Enhancement via Predictive World Modeling / GPC (2502.00622)](https://arxiv.org/abs/2502.00622)\n- [Fast-WAM: Do World Action Models Need Test-time Future Imagination? (2603.16666)](https://arxiv.org/abs/2603.16666)\n- [When to Trust Imagination: Adaptive Action Execution for WAMs (2605.06222)](https://arxiv.org/abs/2605.06222)\n- [World Action Models are Zero-shot Policies / DreamZero (2602.15922)](https://arxiv.org/abs/2602.15922)\n- [World-Value-Action Model: Implicit Planning for VLA Systems (2604.14732)](https://arxiv.org/abs/2604.14732)\n- [Best-of-Q: Q-function Action Ranking at Inference (2601.22701)](https://arxiv.org/abs/2601.22701)\n- [UNISafe: Uncertainty-aware Latent Safety Filters (2505.00779)](https://arxiv.org/abs/2505.00779)\n- [V-GPS Project Page](https://nakamotoo.github.io/V-GPS/)"
      }
    ],
    "totalDurationMs": 115444,
    "totalTokens": 26458,
    "totalToolUseCount": 15,
    "usage": {
      "input_tokens": 1779,
      "cache_creation_input_tokens": 1113,
      "cache_read_input_tokens": 20902,
      "output_tokens": 2664,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1113
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1779,
          "output_tokens": 2664,
          "cache_read_input_tokens": 20902,
          "cache_creation_input_tokens": 1113,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1113,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 15
    }
  },
  "sourceToolAssistantUUID": "505b6aaf-6383-4181-866c-9ec6e7567592",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e26c6f2-72e3-4741-87ef-c0d8359a2540",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Latent-Distribution Candidate Selection for Frozen World Action Models…",
  "leafUuid": "ebc933e7-90f9-43f1-bb64-2790fbd7bf0c",
  "sessionId": "4e26c6f2-72e3-4741-87ef-c0d8359a2540"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "WAM latent-space value learning for frozen inference planning",
  "sessionId": "4e26c6f2-72e3-4741-87ef-c0d8359a2540"
}
```

---

### Assistant

_source line 26 · 2026-05-10T09:19:13.836Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me synthesize the findings:

## Key Findings

### V-GPS (arXiv 2410.13816)
- Full title: "Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance"
- Published at CoRL 2024
- Method: Trains a Q-function via offline RL (Cal-QL) on sparse binary rewards from demonstration data
- Architecture: ResNet-34 + FiLM language conditioning + 2-layer MLP
- **Action space**: Operates on **7-dimensional raw action vectors** (Cartesian, delta XYZ + RPY + gripper) — NOT latent action representations


- Applies to multiple foundation models including Octo variants, RT-1X, and OpenVLA, achieving an 82.8% relative improvement on Octo-small-1.5 across 6 real-world tasks with K=50 candidates
- The value function is trained separately without using policy weights

The critical distinction here is that V-GPS works directly with raw 7-dimensional Cartesian action vectors rather than learned action latents, uses offline RL training instead of simple binary supervision, and applies this approach across various VLA architectures.

Our approach differs fundamentally in three ways: we operate on WAM action latents from joint video-action pretraining rather than raw Cartesian actions, we use binary success/failure signals for training instead of offline RL, and our architecture is a lightweight 3-layer MLP that doesn't need image inputs since the latent already captures visual-physical context from pretraining. This actually gives us a stronger differentiation story than just comparing latent spaces—we can highlight the contrast between learned action representations versus raw action vectors.

Now I'm verifying the WAV benchmark numbers: 99.6% is the 4-split LIBERO average, 98.1% is specifically Long, and 75.6% is the real-world dual-arm result. The original paper's claims check out, but I need to be precise that they tested on LIBERO-Spatial/Object/Goal/Long rather than LIBERO-90.

Looking at the related work, ALT uses OOD detection in observation space with pure nearest-neighbor retrieval rather than action-latent candidate scoring, which is a different approach. UNISafe combines conformal prediction with world model uncertainty for safety filtering to prevent hazardous states.

I've also found VLS, which uses VLM-reward gradients to guide frozen diffusion policies—a distinct mechanism from what we're doing. Best-of-Q applies Q-function re-ranking to VLM agents in digital domains, following a similar paradigm to V-GPS but for a different setting.

Given the stagnation issue and reviewer feedback, this seems like it needs a major revision that restructures the core framing rather than incremental fixes. The key insight is that our approach sits in a specific niche that these papers don't fully occupy.

Looking at the positioning more carefully, V-GPS actually operates in raw Cartesian action space without joint pretraining regularization, which means our differentiation is stronger than I initially thought. We're working with WAM action latents where the joint video-action pretraining creates a richer quality-discriminative geometry that neither the Cartesian approaches nor the VLA token-based methods achieve. The novelty of LOC is solid—no other work combines OOD detection on WAM action latents specifically for pre-execution candidate selection. The score stagnation is likely just a citation gap issue rather than a fundamental weakness in the core idea.

The research itself is actually quite strong for a CoRL submission. I need to reframe the opening around this three-level hierarchy: Cartesian space methods like V-GPS and KDPE at the base, VLA token approaches like MG-Select and RoVer in the middle, and our WAM latent approach at the top. I should also clarify that the z_a inference-time tension is really a training-time property. For the landscape section, I need to properly position V-GPS—it's a CoRL 2024 paper using raw 7D Cartesian vectors with a ResNet-34 encoder that requires both image and action at inference, whereas our Value MLP operates on WAM z_a alone without needing the image at inference time, using binary success/failure supervision. And I need to fix those WAV numbers to show the actual 99.6% average across the LIBERO splits. I'm seeing that V-GPS established value-function re-ranking works in Cartesian space, MG-Select showed it works for VLA action tokens, and the real question is whether WAM latent space offers advantages over these—this suggests a cleaner 3-level hierarchy framing that's stronger than the current approach. Given six rounds of stagnation from citation gaps and framing issues, I should consider whether a structural pivot on the problem statement itself would be more productive than incremental fixes.

The core novelty—using WAM action latent OOD for frozen policy candidate selection at inference time—genuinely hasn't been addressed in the literature, which suggests the idea is sound but the presentation needs work. I'm going to do a major revision that front-loads the 3-tier hierarchy (Cartesian → VLA tokens → WAM latents) to clarify the contributions, fixes the z_a framing to distinguish training-time from inference-time properties, and restructures the core problem statement around this clearer differentiation story.

Updating the JSON with these changes... Cartesian space (KDPE, V-GPS) → VLA action tokens (MG-Select, RoVer) → WAM latents (ours). Fix z_a framing.

2. **opportunity**: Fix z_a inference-time tension. Strengthen Value MLP differentiation from V-GPS (V-GPS: raw Cartesian + image, offline RL; ours: WAM z_a alone, binary supervision).

3. **landscape**: Add V-GPS section. Fix WAV description (clarify it's 4-split average). Add ALT Policy and UNISafe one-liners. Add VLS. Fix WAV numbers.

4. **approach**: Add proactive performance framing paragraph. Fix z_a inference-time tension language.

5. **key_references**: Add V-GPS, VLS, Best-of-Q (optional), ALT Policy, UNISafe.

Now I'm establishing the core framing: a three-tier hierarchy where Cartesian spaces like KDPE and V-GPS lack latent structure, VLA token methods like MG-Select and RoVer operate on architectures without joint video-action pretraining, and our WAM latents leverage that pretraining for quality-discriminative selection. The Value MLP operates purely on z_a without needing the image at inference time, since the latent already captures visual-physical context from joint pretraining—trained on binary success labels rather than offline RL. This is fundamentally different from V-GPS, which requires both image and action at inference. The real question is whether z_a's geometry, shaped by video-action co-variation during training, actually persists as a quality signal when video is absent at inference time.

The LOC diagnostic is my first empirical test of this. If it fails (AUC below 0.55), that's a negative result and Value MLP becomes the main contribution rather than a supporting finding.

For the WAV numbers, I need to be precise: 99.6% is the 4-split LIBERO average across Spatial, Object, Goal, and Long-horizon tasks (Table 1), and 75.6% is the real-world result on dual-arm Piper (Figure 2). The ALT Policy paper shows how diffusion policies function as implicit nearest-neighbor lookups in observation space, replacing them with contrastive image representations instead.

UNISafe takes a different angle—it uses conformal prediction to calibrate a world model's uncertainty for detecting out-of-distribution predictions, then applies Hamilton-Jacobi reachability in the combined latent and uncertainty space to create a safety filter. That's related to LOC's use of conformal prediction on world-model latents, but it's focused on state-space safety rather than action selection.

VLS is a more recent approach that leverages VLM-generated reward gradients to guide frozen diffusion policies during the denoising process toward semantically correct actions without requiring retraining.

Now I'm thinking through the structure of my response. I need to decide whether this is a major or minor revision. The additions here are substantial—V-GPS is a significant new component that changes how I'm positioning the Value MLP differentiation, the 3-tier hierarchy reframes the whole approach, and the z_a inference-time clarification resolves a theoretical tension. These aren't just incremental tweaks; they materially reshape the narrative. I'm calling this a major revision.

For the core problem section, I need to integrate V-GPS properly, establish the 3-tier hierarchy, and fix the z_a framing. For the opportunity section, I should clarify that z_a is a training-time property and address how that affects the inference-time dynamics.

The key differentiators between V-GPS and my Value MLP approach are worth spelling out clearly: V-GPS requires both images and 7D actions at inference, while my approach only needs z_a since the visual context is already encoded from joint pretraining. V-GPS uses offline RL with Cal-QL, whereas I'm using binary success/failure labels. And fundamentally, V-GPS validates the paradigm in Cartesian space with images, while my work asks whether the WAM latent space alone is sufficient for better discrimination.

For the landscape section, I need to add V-GPS as a critical prior work entry, fix the WAV description with proper references, and include ALT Policy, UNISafe, and VLS as concurrent work.

In the approach section, I'll fix the z_a framing in the theoretical basis and add a paragraph about proactive performance framing.

For references, I need to add V-GPS, VLS, ALT Policy, and UNISafe, plus fix the WAV description.

Now I'm ready to write out the full JSON with these modifications integrated throughout. I'm working through the JSON structure now, and I realize I need to systematically check what papers might still be missing from the landscape—there's a pattern of reviewers catching gaps that I should address proactively. Beyond the ones I'm already adding like V-GPS and ALT Policy, I should verify whether Best-of-Q and VLS deserve mentions, and think through whether there are any world model papers I'm overlooking.

The research agent confirmed there's no direct overlap with our specific approach of action latent OOD detection combined with frozen WAM inference and pre-execution candidate selection, so the core novelty holds. I also need to add an explicit framing paragraph to the approach section that clarifies we're extracting planning value from frozen pretrained models without fine-tuning or rollout data—comparing against the B=1 baseline and achieving 10+ percentage point improvements through adaptation alone.

Now I'm structuring the JSON revisions, starting with the core_problem field. I need to add V-GPS to the test-time compute literature section, positioning it alongside KDPE to establish that value-function re-ranking of frozen policies is already validated in Cartesian+image space. Then I'll organize the action representation tiers into a clear three-level hierarchy based on the space each method operates in.

For the opportunity section, I'm clarifying that z_a regularization emerges from joint video-action pretraining as a training-time property, and the key empirical question is whether this structure persists at inference time without video input as a quality-discriminative signal.

Now I'm differentiating our Value MLP approach from V-GPS: while V-GPS trains a Q-function on raw Cartesian actions paired with images, requiring both at inference time, our method operates directly on WAM action latents with only binary success labels—no image needed because z_a already captures visual-physical context from joint pretraining. This tests whether the latent space provides better linear separability for success/failure classification compared to the Cartesian+image paradigm V-GPS validates.

For the landscape section, I need to correct WAV's metrics to show 99.6% average across LIBERO's four splits and 98.1% on LIBERO-Long specifically, plus 75.6% on real-world dual-arm tasks. I'm also adding one-liners for ALT Policy, UNISafe, and VLS, then updating the references with V-GPS, VLS, and ALT Policy's arxiv identifiers. In the approach section, I should refine the theoretical framing around z_a and add a paragraph about proactive performance in the evaluation benchmarks.

I'm considering whether to include Best-of-Q as a related work in the digital agent space, though it's less central to robot manipulation. The description field will need updating to reflect the three-tier hierarchy. Let me now construct the full JSON with these targeted changes applied to the original structure.

The real insight here is that V-GPS reveals a cleaner three-tier competitive landscape: Cartesian action spaces like KDPE and V-GPS without pretrained latent structure, VLA action tokens like MG-Select and RoVer without video-physics co-training, and our WAM action latents from joint video-action pretraining. This framing is stronger than the paper's original positioning, and the key differentiator is that our Value MLP operates directly on learned action latents rather than requiring Cartesian coordinates or images.

Now I'm structuring the JSON output to capture these insights clearly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebc933e7-90f9-43f1-bb64-2790fbd7bf0c",
  "isSidechain": false,
  "requestId": "req_011CatdtEG3n2VR1SfDAbAJE",
  "type": "assistant",
  "uuid": "d4b0fb66-4737-481d-895b-21671b00e31a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e26c6f2-72e3-4741-87ef-c0d8359a2540",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_014JmGisKEsNcr959Ts6mBPb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7512,
      "cache_read_input_tokens": 34112,
      "output_tokens": 6464,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7512,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6464,
          "cache_read_input_tokens": 34112,
          "cache_creation_input_tokens": 7512,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7512
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

_source line 27 · 2026-05-10T09:19:23.749Z_

Research complete. Let me synthesize before revising:

**V-GPS critical finding**: V-GPS operates on **raw 7D Cartesian action vectors + ResNet-34 image embeddings** (not latent space). It requires both image AND action at inference, trained via offline RL (Cal-QL). This is actually a *stronger* differentiation story than the paper currently claims — our Value MLP needs only z_a at inference (no image, because z_a already encodes visual context from joint pretraining).

**WAV numbers**: 99.6% is the 4-split LIBERO average (Spatial/Object/Goal/Long, Table 1). 75.6% is real-world from Figure 2 (dual-arm Piper robot). Both numbers are correct but need better citation context.

**ALT Policy**: OOD detection in **observation** (image) latent space for single-trajectory retrieval — not action latents, not multi-candidate selection.

**UNISafe**: Conformal prediction + world model **state** latent epistemic uncertainty for **safety filtering** — not candidate selection for task performance.

**New paper found**: VLS (arXiv 2602.03973) — VLM-reward-gradient steering of frozen diffusion policies. Adjacent but different mechanism.

**Core structural insight from V-GPS**: The landscape now has a clear 3-tier hierarchy: Cartesian space (KDPE, V-GPS) → VLA tokens (MG-Select, RoVer) → WAM latents (ours). This is a materially stronger framing than the current paper. I'll restructure core_problem around this hierarchy and make this a **major revision**.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4b0fb66-4737-481d-895b-21671b00e31a",
  "isSidechain": false,
  "requestId": "req_011CatdtEG3n2VR1SfDAbAJE",
  "type": "assistant",
  "uuid": "2cd018b7-3594-4415-89bd-3cbd65aa21e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e26c6f2-72e3-4741-87ef-c0d8359a2540",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_014JmGisKEsNcr959Ts6mBPb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7512,
      "cache_read_input_tokens": 34112,
      "output_tokens": 6464,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7512,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6464,
          "cache_read_input_tokens": 34112,
          "cache_creation_input_tokens": 7512,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7512
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

_source line 28 · 2026-05-10T09:19:24.498Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ABEZp7WR3jbghF4H9SxU1q`</summary>

```json
{
  "query": "V-GPS \"value guided policy steering\" CoRL 2024 robot manipulation offline RL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2cd018b7-3594-4415-89bd-3cbd65aa21e7",
  "isSidechain": false,
  "requestId": "req_011CatdtEG3n2VR1SfDAbAJE",
  "type": "assistant",
  "uuid": "98d4e78f-4695-4128-a7c5-e20a55d9b59d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e26c6f2-72e3-4741-87ef-c0d8359a2540",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_014JmGisKEsNcr959Ts6mBPb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7512,
      "cache_read_input_tokens": 34112,
      "output_tokens": 6464,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7512,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6464,
          "cache_read_input_tokens": 34112,
          "cache_creation_input_tokens": 7512,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7512
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
  "leafUuid": "98d4e78f-4695-4128-a7c5-e20a55d9b59d",
  "sessionId": "4e26c6f2-72e3-4741-87ef-c0d8359a2540"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "WAM latent-space value learning for frozen inference planning",
  "sessionId": "4e26c6f2-72e3-4741-87ef-c0d8359a2540"
}
```

---

### Tool result

_source line 31 · 2026-05-10T09:19:31.155Z_

<details><summary>↩ Tool result · `toolu_01ABEZp7WR3jbghF4H9SxU1q`</summary>

```text
Web search results for query: "V-GPS "value guided policy steering" CoRL 2024 robot manipulation offline RL"

Links: [{"title":"V-GPS: Value-Guided Policy Steering","url":"https://nakamotoo.github.io/V-GPS/"},{"title":"GitHub - nakamotoo/V-GPS: official implementation for our paper Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance (CoRL 2024)","url":"https://github.com/nakamotoo/V-GPS"},{"title":"Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance | OpenReview","url":"https://openreview.net/forum?id=6FGlpzC9Po"},{"title":"Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance","url":"https://arxiv.org/html/2410.13816v1"},{"title":"[2410.13816] Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance","url":"https://arxiv.org/abs/2410.13816"},{"title":"[2410.13816v2] Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance","url":"https://arxiv.org/abs/2410.13816v2"},{"title":"Paper page - Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance","url":"https://huggingface.co/papers/2410.13816"},{"title":"Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance | Oier Mees","url":"https://www.oiermees.com/publication/vgps/"},{"title":"[PDF] Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Steering-Your-Generalists:-Improving-Robotic-Models-Nakamoto-Mees/5cde475c3b572cf81d9b14c4fd1163c1c2c19568"},{"title":"Mitsuhiko Nakamoto on X: \"Many generalist robot policies have been released, but they're not perfect. How can we make them better? Introducing V-GPS🚀: Value Guided Policy Steering, a simple approach to improve any off-the-shelf generalist policy at deployment time.🧵#CoRL2024 🌐https://t.co/uNxN6uxW20 https://t.co/Dx7vCA8fJD\" / X","url":"https://x.com/mitsuhiko_nm/status/1847088212885623025"}]

I found comprehensive results about V-GPS. Here's what the search revealed:

## Overview

V-GPS is a novel approach that improves the performance of pre-trained generalist robotic policies by re-ranking their actions at deployment time based on a value function learned via offline RL.

## Key Details

V-GPS enhances the performance of generalist robot policies at deployment time by re-ranking their actions according to a value function learned via offline RL. The same single value function can be combined with any off-the-shelf generalist policy in a plug-and-play manner, without the need to fine-tune or access the policy's weights.

## Motivation

Large, general-purpose robotic policies trained on diverse demonstration datasets are effective for controlling various robots, but the data is generally of mixed quality—human-collected demonstrations are unlikely to perform perfectly, and larger datasets are harder to curate for only high-quality examples.

## Authors and Publication

The paper is authored by Mitsuhiko Nakamoto, Oier Mees, Aviral Kumar, and Sergey Levine, and was published at the Conference on Robot Learning (CoRL) 2024.

## Experimental Results

V-GPS was evaluated on five generalist policies—Octo-small, Octo-base, Octo-small-1.5, RT1-X, and OpenVLA—in SIMPLER simulation environments across two robot platforms (WidowX and Google Robot), and improved the success rates of all five generalist policies.

The code and resources are available on [GitHub](https://github.com/nakamotoo/V-GPS) and the project page is at [nakamotoo.github.io/V-GPS](https://nakamotoo.github.io/V-GPS).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "98d4e78f-4695-4128-a7c5-e20a55d9b59d",
  "isSidechain": false,
  "promptId": "d7b557eb-7415-4061-bbb7-58d07ac1d15d",
  "type": "user",
  "uuid": "996e5f2f-dcac-41d4-9c07-671db3145914",
  "toolUseResult": {
    "query": "V-GPS \"value guided policy steering\" CoRL 2024 robot manipulation offline RL",
    "results": [
      {
        "tool_use_id": "srvtoolu_01ATw2FPrgR3ph91mnQH3ybu",
        "content": [
          {
            "title": "V-GPS: Value-Guided Policy Steering",
            "url": "https://nakamotoo.github.io/V-GPS/"
          },
          {
            "title": "GitHub - nakamotoo/V-GPS: official implementation for our paper Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance (CoRL 2024)",
            "url": "https://github.com/nakamotoo/V-GPS"
          },
          {
            "title": "Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance | OpenReview",
            "url": "https://openreview.net/forum?id=6FGlpzC9Po"
          },
          {
            "title": "Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance",
            "url": "https://arxiv.org/html/2410.13816v1"
          },
          {
            "title": "[2410.13816] Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance",
            "url": "https://arxiv.org/abs/2410.13816"
          },
          {
            "title": "[2410.13816v2] Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance",
            "url": "https://arxiv.org/abs/2410.13816v2"
          },
          {
            "title": "Paper page - Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance",
            "url": "https://huggingface.co/papers/2410.13816"
          },
          {
            "title": "Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance | Oier Mees",
            "url": "https://www.oiermees.com/publication/vgps/"
          },
          {
            "title": "[PDF] Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Steering-Your-Generalists:-Improving-Robotic-Models-Nakamoto-Mees/5cde475c3b572cf81d9b14c4fd1163c1c2c19568"
          },
          {
            "title": "Mitsuhiko Nakamoto on X: \"Many generalist robot policies have been released, but they're not perfect. How can we make them better? Introducing V-GPS🚀: Value Guided Policy Steering, a simple approach to improve any off-the-shelf generalist policy at deployment time.🧵#CoRL2024 🌐https://t.co/uNxN6uxW20 https://t.co/Dx7vCA8fJD\" / X",
            "url": "https://x.com/mitsuhiko_nm/status/1847088212885623025"
          }
        ]
      },
      "I found comprehensive results about V-GPS. Here's what the search revealed:\n\n## Overview\n\nV-GPS is a novel approach that improves the performance of pre-trained generalist robotic policies by re-ranking their actions at deployment time based on a value function learned via offline RL.\n\n## Key Details\n\nV-GPS enhances the performance of generalist robot policies at deployment time by re-ranking their actions according to a value function learned via offline RL. The same single value function can be combined with any off-the-shelf generalist policy in a plug-and-play manner, without the need to fine-tune or access the policy's weights.\n\n## Motivation\n\nLarge, general-purpose robotic policies trained on diverse demonstration datasets are effective for controlling various robots, but the data is generally of mixed quality—human-collected demonstrations are unlikely to perform perfectly, and larger datasets are harder to curate for only high-quality examples.\n\n## Authors and Publication\n\nThe paper is authored by Mitsuhiko Nakamoto, Oier Mees, Aviral Kumar, and Sergey Levine, and was published at the Conference on Robot Learning (CoRL) 2024.\n\n## Experimental Results\n\nV-GPS was evaluated on five generalist policies—Octo-small, Octo-base, Octo-small-1.5, RT1-X, and OpenVLA—in SIMPLER simulation environments across two robot platforms (WidowX and Google Robot), and improved the success rates of all five generalist policies.\n\nThe code and resources are available on [GitHub](https://github.com/nakamotoo/V-GPS) and the project page is at [nakamotoo.github.io/V-GPS](https://nakamotoo.github.io/V-GPS)."
    ],
    "durationSeconds": 6.6501730630000235
  },
  "sourceToolAssistantUUID": "98d4e78f-4695-4128-a7c5-e20a55d9b59d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e26c6f2-72e3-4741-87ef-c0d8359a2540",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-10T09:19:41.174Z_

<details><summary>Logged reasoning block</summary>

```text
Good, confirmed: V-GPS is CoRL 2024. Now I have all the information I need. Let me write the revised JSON.

Key changes for the major revision:

1. **core_problem**: 
   - Add V-GPS as an established method in the candidate selection literature
   - Add the 3-tier hierarchy framing (Cartesian → VLA tokens → WAM latents)
   - Fix z_a inference-time tension language
   
2. **opportunity**: 
   - Fix z_a framing (training-time property)
   - Strengthen Value MLP vs V-GPS differentiation
   - Add comparison note about inference-time image requirement

3. **landscape**:
   - Add full V-GPS section
   - Fix WAV numbers with proper table/figure references
   - Add ALT Policy one-liner
   - Add UNISafe one-liner  
   - Add VLS brief note
   
4. **approach**:
   - Fix z_a framing in theoretical basis
   - Add proactive performance framing paragraph
   
5. **key_references**:
   - Add V-GPS
   - Add VLS
   - Fix WAV description
   
6. **description**: Update to reflect 3-tier hierarchy framing

Now I'm drafting the complete JSON with all these revisions integrated.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "996e5f2f-dcac-41d4-9c07-671db3145914",
  "isSidechain": false,
  "requestId": "req_011Cate4x7WGUM4zUW1d7su5",
  "type": "assistant",
  "uuid": "99f287b4-886b-41ac-b8f5-2aaf77414391",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e26c6f2-72e3-4741-87ef-c0d8359a2540",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Bdb3fgWBJBGzwwfpnSzcSJ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7533,
      "cache_read_input_tokens": 41624,
      "output_tokens": 14335,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7533,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14335,
          "cache_read_input_tokens": 41624,
          "cache_creation_input_tokens": 7533,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7533
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

_source line 33 · 2026-05-10T09:25:13.454Z_

Good — V-GPS is confirmed CoRL 2024. Now I have everything needed. Let me synthesize the full picture and write the revised JSON.

**The major structural insight**: V-GPS validates value re-ranking in Cartesian+image space (K=50, offline RL, both image and action needed at inference). Our Value MLP asks whether WAM z_a alone (no image at inference — z_a encodes visual context from pretraining) enables better discrimination with simpler supervision. This is a genuinely stronger differentiation story. The 3-tier hierarchy (Cartesian → VLA tokens → WAM latents) should reorganize the entire core_problem framing.

```json
{
  "title": "Latent-Distribution Candidate Selection for Frozen World Action Models: OOD Consistency Scoring and Action-Latent Value Learning",
  "change_type": "major",
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
```

---

**Summary of changes (major revision):**

**Core structural improvement — 3-tier hierarchy**: The core_problem is reorganized around Cartesian (V-GPS, KDPE) → VLA tokens (MG-Select, RoVer) → WAM latents (ours). This is a materially stronger framing that positions the paper's contribution within a clear representational progression rather than as an ad-hoc comparison list.

**V-GPS integration**: Added as a full landscape entry with precise differentiation. The key insight from fetching the actual paper: V-GPS uses raw 7D Cartesian actions + ResNet-34 image embeddings and requires **both** at inference. Our Value MLP uses z_a alone — no image needed at inference because z_a encodes visual context from joint pretraining. This is a cleaner, more compelling differentiation than "WAM vs. VLA" alone.

**WAV numbers corrected**: 99.6% = LIBERO 4-split average (Spatial/Object/Goal/Long, Table 1); 98.1% = LIBERO-Long specifically; 75.6% = real-world Figure 2 (dual-arm Piper). All confirmed correct; added table/figure citations and clarification that WAV does not test on LIBERO-90.

**z_a inference-time tension fixed**: Now explicitly framed as a training-time property tested empirically in Step 1, not an inference-time video conditioning claim.

**ALT Policy and UNISafe**: Added with accurate one-sentence descriptions based on actual paper content (observation latent retrieval vs. action latent selection; safety vs. candidate scoring).

**Proactive performance framing**: Added full paragraph in approach explicitly distinguishing the zero-demonstration deployment target from fine-tuned model comparisons.

**New references**: V-GPS (CoRL 2024), VLS (Feb 2026), ALT Policy, UNISafe, Best-of-Q.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99f287b4-886b-41ac-b8f5-2aaf77414391",
  "isSidechain": false,
  "requestId": "req_011Cate4x7WGUM4zUW1d7su5",
  "type": "assistant",
  "uuid": "0e61c2f9-3c08-4a2f-bf29-56e3e44afc60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e26c6f2-72e3-4741-87ef-c0d8359a2540",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Bdb3fgWBJBGzwwfpnSzcSJ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7533,
      "cache_read_input_tokens": 41624,
      "output_tokens": 14335,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7533,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14335,
          "cache_read_input_tokens": 41624,
          "cache_creation_input_tokens": 7533,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7533
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

_source line 34_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Latent-Distribution Candidate Selection for Frozen World Action Models…",
  "leafUuid": "0e61c2f9-3c08-4a2f-bf29-56e3e44afc60",
  "sessionId": "4e26c6f2-72e3-4741-87ef-c0d8359a2540"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "WAM latent-space value learning for frozen inference planning",
  "sessionId": "4e26c6f2-72e3-4741-87ef-c0d8359a2540"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Latent-Distribution Candidate Selection for Frozen World Action Models…",
  "leafUuid": "0e61c2f9-3c08-4a2f-bf29-56e3e44afc60",
  "sessionId": "4e26c6f2-72e3-4741-87ef-c0d8359a2540"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "ai-title",
  "aiTitle": "WAM latent-space value learning for frozen inference planning",
  "sessionId": "4e26c6f2-72e3-4741-87ef-c0d8359a2540"
}
```

---
