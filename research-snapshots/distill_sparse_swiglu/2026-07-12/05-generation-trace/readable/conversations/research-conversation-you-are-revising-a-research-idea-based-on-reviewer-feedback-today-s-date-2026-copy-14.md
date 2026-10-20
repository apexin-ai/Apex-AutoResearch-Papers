# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-13 (UTC).** ## Original idea { "tit

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 30
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-2/4b2e93a9-7a45-4028-badc-913d53ffd7bb.jsonl`
- **Structured JSON:** [`d7119947e511623dd3ba.json`](../../sessions/d7/d7119947e511623dd3ba.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-13T19:22:40.998Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-13T19:22:40.998Z",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-13 (UTC).**\n\n## Original idea\n{\n  \"title\": \"Mode-Aware Quality Scoring for Demonstration Curation via Sliced Wasserstein Consensus\",\n  \"core_problem\": \"How should we curate multimodal demonstration datasets that contain multiple valid strategies of varying quality? Diversity-maximizing approaches (FAKTUAL) improve average performance but explicitly fail when demonstrations contain conflicting strategies — blindly including diverse-but-poor demonstrations degrades learning. Quality-scoring approaches (CUPID, DataMIL) work well but require expensive policy training, validation rollouts, or influence function estimation. Learned reward models (Robometer) can score trajectory quality without a task-specific policy but require 1M+ training trajectories and are not mode-aware. Recent evidence from 'Is Diversity All You Need?' (Modi Shi et al., arXiv Jul 2025) sharpens this problem: they show that expert diversity creates *velocity multimodality* — different demonstrators executing the same spatial trajectory at different speeds — that directly degrades policy learning, producing 15% performance losses that their velocity normalization method recovers. This confirms that multi-operator demonstrations create distributional conflicts that harm learning, but their fix (velocity normalization) only addresses speed variation along shared paths, not the broader problem of scoring quality across genuinely different strategy modes. The field lacks a training-free quality scoring method that is *mode-aware* — one that discovers distinct strategy modes in the data and scores quality within each mode, rather than treating all demonstrations as drawn from a single distribution.\",\n  \"opportunity\": \"The demonstration curation landscape has crystallized into five camps: (1) *policy-dependent quality methods* (CUPID, DataMIL, Demo-SCORE, QoQ) that achieve SOTA but require trained policies or validation rollouts; (2) *policy-free learned quality methods* (Robometer) that train general-purpose reward models on massive trajectory datasets to score quality without a task-specific policy, but require 1M+ training trajectories for pre-training and are not mode-aware — they assign a global quality score without distinguishing between multiple valid strategies. Robometer achieves strong absolute success rates on retrieval tasks (e.g., ~95% on Stir Pot where baselines score near 0%), though the reported 4.5× average improvement is inflated by near-zero baseline performance on several tasks rather than reflecting a uniform 4.5× gain; (3) *policy-free quality proxies* (DemInf, RINSE, SCIZOR) that use scalar metrics (MI, smoothness, progress) but collapse distributional structure and are mode-agnostic; (4) *policy-free diversity methods* (FAKTUAL) that maximize trajectory entropy but explicitly acknowledge 'promoting diversity may actually be harmful when the model is not capable of capturing multimodality in the data'; and (5) *distribution normalization methods* ('Is Diversity All You Need?', Modi Shi et al., arXiv Jul 2025) that identify velocity multimodality from expert diversity as a concrete failure mode and propose velocity distribution debiasing — training a velocity model to normalize action chunk speeds, recovering 15% performance (equivalent to 2.5× more pre-training data). This last camp validates the core premise that multi-operator demonstrations create distributional conflicts harming learning, but addresses only velocity variation along shared spatial paths via normalization, not the broader challenge of scoring quality across genuinely different strategy modes. This reveals a fundamental tension: diversity-based curation fails precisely when demonstrations are multimodal (multiple valid strategies), because it retains low-quality demonstrations from each mode for the sake of coverage. Distribution normalization (velocity debiasing) removes one source of multimodality but does not score trajectory quality or discover strategy modes. Recent evidence further motivates intelligent curation: 'On Data Redundancy in VLA Training' (DATA-FM @ ICLR 2026) shows that random 30% sampling of LIBERO matches full-dataset SmolVLA performance, revealing massive data redundancy — but their difficulty-based Temporal Surprise Score underperformed random selection, suggesting that naive quality proxies can be counterproductive. Empirically, FAKTUAL performs only modestly above random selection on RoboMimic MH, well below quality-based methods. The key gap: no existing training-free method provides *mode-aware quality scoring* — discovering strategy modes and assessing quality relative to mode-specific consensus, rather than against a single global reference, via a mode-agnostic scalar proxy, through a learned reward model that treats all demonstrations as a single population, or through velocity normalization that only addresses speed variation. Optimal transport geometry fills this gap naturally: Sliced Wasserstein distances define a metric space over trajectory distributions that captures shape, spread, and temporal structure; clustering in this space discovers strategy modes; and distance from each mode's robust barycenter provides a geometrically grounded, mode-aware quality score. This fills the 'good methods to quantify data quality' gap (ICLR 2026 VLA blog) with an approach that is simultaneously training-free, mode-aware, and distributional — complementary to learned scorers (Robometer), diversity-based methods (FAKTUAL), policy-dependent methods (CUPID), and distribution normalization approaches (velocity debiasing).\",\n  \"landscape\": \"**Policy-dependent quality methods**: CUPID (CoRL 2025) uses influence functions estimating each demonstration's causal impact on closed-loop policy return, achieving SOTA on RoboMimic with <33% of curated data; requires a trained policy and evaluation rollouts. DataMIL (ICLR 2026) uses the datamodels paradigm for end-to-end policy-driven selection validated on 60+ tasks including OXE; requires surrogate loss computation with policy training. Demo-SCORE (RSS 2025) trains classifiers on online rollout success/failure to self-curate, achieving 15-35% gains; requires online robot interaction. QoQ (arXiv Mar 2026) uses influence functions with theoretical analysis but requires a validation set and scales O(n²). **Policy-free learned quality methods**: Robometer (RSS 2026, arXiv 2603.02115) trains a general-purpose VLM-based reward model (Qwen3-VL-4B) on RBM-1M (1M+ trajectories across 21 embodiments) using a dual objective of frame-level progress supervision and trajectory-level preference learning. Achieves strong absolute success rates on retrieval tasks (e.g., ~95% on Stir Pot where baselines score near 0%), though the reported 4.5× average improvement is inflated by near-zero baseline performance on several tasks rather than reflecting a uniform 4.5× gain. However, Robometer (a) requires 1M+ training trajectories (~6TB) for pre-training — infeasible when curating smaller datasets without pre-existing large-scale data; (b) is NOT mode-aware — it assigns a single global quality score per trajectory without distinguishing between multiple valid strategies; (c) was not evaluated against demonstration curation methods (CUPID, DemInf, RINSE, SCIZOR, FAKTUAL) — its comparisons are against VLM reward models (RoboReward, GVL, VLAC). OT-Consensus is complementary: training-free, mode-aware, and geometric, requiring no pre-training data. **Policy-free quality proxies**: DemInf (RSS 2025) estimates trajectory-level mutual information between states and actions via k-NN estimators with VAE embeddings, achieving 5-10% gains on RoboMimic; captures information content but collapses distributional structure to a scalar and is mode-agnostic. RINSE (ICML 2025, arXiv 2604.23000) uses Spectral Arc Length (SAL) and Trajectory-Envelope Distance (TED) smoothness metrics achieving 16-20% success gains; assumes smoothness universally correlates with quality, failing for tasks where jerky motions are correct. SCIZOR (ICRA 2026) combines self-supervised task progress prediction with deduplication, achieving 15.4% average improvement across RoboMimic/OXE/Sirius-Fleet; no theoretical guarantees and conflates lack of progress with low quality. S2I (ICRA 2025) performs segment-level selection using contrastive learning with 3 expert reference demonstrations; requires expert references and cannot operate fully unsupervised. Consistency Matters (ACM THRI 2025) proposes 10 motion-based consistency metrics with 76-91% success prediction accuracy; limited to geometric consistency without distributional analysis. **Policy-free diversity methods**: FAKTUAL (arXiv Mar 2026, 2603.11634) uses signature kernel entropy for diversity-based curation; fully model-free and tested on RoboMimic MH and MetaWorld. Compared against CUPID, DemInf, and Demo-SCORE. FAKTUAL performs modestly above random but below quality-based methods, and *explicitly acknowledges* that 'promoting diversity may actually be harmful when the model is not capable of capturing multimodality in the data.' This is the precise weakness OT-Consensus targets. NOTE: As of May 2026, FAKTUAL code is not publicly released; the underlying signature kernel computation can be approximated using open-source libraries (sigkernel by Salvi et al., KSig by Toth et al. for GPU-accelerated signature kernels), but the entropy estimation and subset selection components would require reimplementation. **Distribution normalization methods**: 'Is Diversity All You Need for Scalable Robotic Manipulation?' (Modi Shi et al., arXiv Jul 2025, 2507.06219) investigates data diversity along three dimensions (task, embodiment, expert) and identifies *velocity multimodality* — different demonstrators executing the same spatial trajectory at different speeds, producing distinct action chunks within fixed time windows — as a concrete failure mode from expert diversity. Their distribution debiasing method trains a lightweight velocity model (SigLIP encoder + 3-layer MLP) to predict expected velocity conditioned on observations, then rescales action chunks to normalize speed variation during policy training. This yields GO-1-Pro with 15% gains (equivalent to 2.5× pre-training data) on AgiBot G1 real-world tasks (Wipe Table, Fold Shorts, Pour Water, Make Sandwich) and ManiSkill/RoboTwin simulation benchmarks. Key relationship to OT-Consensus: (a) *Validates the core premise* — empirically confirms that multi-operator demonstrations create distributional conflicts (velocity multimodality) that directly degrade policy learning; (b) *Addresses a different level of the problem* — velocity debiasing normalizes speed variation along shared spatial paths, while OT-Consensus discovers and scores quality across genuinely different strategy modes (spatial multimodality); (c) *Complementary, not competing* — velocity normalization could be applied as a preprocessing step before OT-Consensus's mode-aware curation, first removing speed variation then scoring trajectory quality within each strategy mode; (d) *Different mechanism* — velocity debiasing is a learned normalization (requires training a velocity model) that transforms data in-place, while OT-Consensus is a training-free curation method that selects data; (e) *Different scope* — velocity debiasing specifically targets speed variation, while OT-Consensus's SW2 distance captures the full distributional shape including spatial path, action profile, and temporal structure. Notably, Modi Shi et al. distinguish 'spatial multimodality' (different paths = meaningful strategies to preserve) from 'velocity multimodality' (different speeds = noise to remove) — OT-Consensus's k-medoid clustering in SW2 space naturally discovers spatial modes, and within-mode quality scoring captures quality variation including but not limited to velocity outliers. **Data redundancy in VLA training**: 'On Data Redundancy in VLA Training' (DATA-FM Workshop @ ICLR 2026) shows that random 30% frame sampling of LIBERO matches full-dataset performance for SmolVLA and GR00T N1.5, revealing massive data redundancy. Their Temporal Surprise Score (TSS), a frame-level difficulty-based selection metric, actually underperformed random selection — suggesting that naive quality proxies can be counterproductive and motivating more principled curation approaches. Note: TSS operates at frame-level, while OT-Consensus operates at trajectory-level. **OT-based quality/distance methods (adjacent)**: sWk-means (Luan & Hamp, arXiv 2310.01285, Data Science in Finance and Economics 2025) uses sliced Wasserstein distances + k-means clustering for automated regime detection in multidimensional financial time series. The core algorithmic pipeline — compute SW distances between distributional representations of sequential data, then cluster in SW space — is a methodological precursor to OT-Consensus's first two steps. However, sWk-means (a) stops at cluster assignment and does not compute barycenters or score quality within clusters; (b) operates on financial time series regimes, not robot trajectory measures; (c) has no filtering or curation pipeline. OT-Consensus extends this SW+clustering pipeline with three key additions: robust barycenters for within-mode quality scoring, the trajectory-as-measure representation design for robot demonstrations (visual-encoder features + actions + temporal grounding), and the mode-aware curation pipeline that filters within modes while preserving cross-mode diversity. BWD/'Expert or not?' (arXiv Oct 2025, 2510.12638) introduces Bellman Wasserstein Distance for quality scoring in offline RL — value-aware OT requiring a behavioral critic; operates in RL, not IL. SWAD (Pallage & Lesage-Landry, arXiv Apr 2025, 2504.12918) uses sliced-Wasserstein distance for unsupervised anomaly detection on i.i.d. tabular data; operates on individual data points, not trajectory measures. LWAIL (ICLR 2026, 2603.05440) uses Wasserstein for state-only distribution matching in adversarial IL policy learning — addresses policy learning, not data curation. **OT in robot learning (not curation)**: OTR (ICLR 2023) assigns rewards via OT. Temporal OT Reward (NeurIPS 2024) extends with temporal ordering. GWIL (ICLR 2022) uses OT for cross-domain imitation. ROT (NeurIPS 2022) uses regularized OT for trajectory matching. **Complementary approaches**: Learning from Imperfect Demonstrations via Temporal BT-Guided Trajectory Repair (arXiv Apr 2026, 2604.04225) repairs suboptimal trajectories rather than filtering them — complementary to curation approaches. **OT theory**: Robust Wasserstein Barycenter (arXiv Mar 2026) proves existence and consistency of outlier-robust barycenters under no moment assumptions, though without finite-sample convergence rates. Outlier-Robust OT (Nietert et al., AISTATS 2022) provides minimax estimation rates for robust Wasserstein distances under ε-contamination. k-Sparse Wasserstein Barycenter with Outliers (IJCAI 2024) gives constant-factor approximations. s-OTDD (ICML 2025) demonstrates scalable sliced OT for dataset distance. **Gap**: No existing method provides training-free, mode-aware quality scoring using distributional OT geometry. FAKTUAL is mode-agnostic (diversity); DemInf/RINSE/SCIZOR are mode-agnostic (scalar quality proxies); Robometer is a learned scorer but not mode-aware and requires 1M+ trajectories; CUPID/DataMIL are mode-aware in principle but policy-dependent; sWk-means uses SW+clustering but stops at regime identification without quality scoring; velocity debiasing (Modi Shi et al.) normalizes speed variation but does not discover strategy modes or score trajectory quality. OT-Consensus uniquely combines mode awareness, quality scoring, and training-free operation.\",\n  \"approach\": \"**Overview**: OT-Consensus is a training-free, mode-aware demonstration quality scoring method. We reframe the demonstration curation problem as: *given multimodal demonstrations, score quality within each strategy mode rather than globally.* The core conceptual contribution is that quality should be assessed relative to mode-specific consensus, not global diversity or global statistics — and that Sliced Wasserstein geometry naturally enables this by providing a metric space where trajectories cluster by strategy and quality is measured by distributional distance from each mode's robust center. This extends the SW+clustering pipeline introduced by sWk-means (Luan & Hamp, DSFE 2025) from financial regime detection to robot demonstration curation, with three key additions: robust barycenters for quality scoring, trajectory-as-measure representation for robot demonstrations, and mode-aware filtering. We target a focused empirical contribution for CoRL 2026 with formal theoretical analysis deferred.\\n\\n**Day 1 Validation Gate (May 13 — before committing to the full sprint)**: We run two preliminary experiments to validate the core hypothesis that SW2 geometry can distinguish strategy modes from quality variation, requiring ~4h total compute. (a) *Synthetic toy experiment*: Generate 200 2D trajectories from 2 strategy modes (left-reach vs right-reach, implemented as trajectories curving left vs right to reach a target) with 3 quality tiers per mode: clean (smooth, direct), noisy (Gaussian perturbations σ=0.1), and corrupted (large deviations, missing segments). Total: 2 modes × 3 tiers × ~33 trajectories = 200 trajectories. Compute the 200×200 SW2 pairwise distance matrix using L=100 random projections. Run k-medoid clustering with k=2 and k=6. Verify: (i) k=2 recovers the two strategy modes (ARI ≥ 0.8 against mode labels); (ii) within each mode cluster, SW2 distance to the mode's barycenter correlates with quality tier (Spearman ρ ≥ 0.5). Simultaneously compute MI-based scores (mutual information between trajectory segments) and smoothness scores (jerk magnitude, as in RINSE) for each trajectory. Show that these scalar metrics fail to distinguish within-mode quality tiers — specifically, that a smooth but wrong-mode trajectory scores higher on smoothness than a slightly noisy correct-mode trajectory. This validates H1 (mode separation) and H2 (within-mode quality scoring) on controlled data. (b) *RoboMimic pilot*: Randomly sample 50 trajectories from RoboMimic MH Can task. Compute the 50×50 SW2 pairwise distance matrix using SigLIP-SO400M embeddings of image observations. Run k-medoid clustering with k=3 (matching proficiency levels: Worse/Okay/Better) and k=6 (matching individual operators). Compute Adjusted Rand Index (ARI) against operator identity labels and proficiency labels for each k. (c) *Gate criterion*: Proceed with full sprint only if: synthetic toy shows clear mode separation (ARI ≥ 0.8 for k=2) AND within-mode quality correlation (ρ ≥ 0.5), AND RoboMimic pilot achieves ARI ≥ 0.1 with at least one k value against at least one label set. If the gate fails — specifically if RoboMimic ARI < 0.1 for all k and label combinations — the core hypothesis is invalidated and the sprint should pivot (e.g., to SW2 in proprioceptive-action space rather than visual embedding space, or to a different distance metric entirely). Both experiments are included as motivating figures in the paper (Figure 1a: synthetic toy SW2 distance matrix heatmap and clustering; Figure 1b: RoboMimic pilot clustering colored by operator labels).\\n\\n**FAKTUAL Reproduction Plan**: FAKTUAL code is not publicly released as of May 2026. Mitigation plan: (1) May 13 — contact FAKTUAL authors (Sirigiri, de Lara, Agia, Shkurti, Ramos) requesting code access. (2) May 14-15 — if code received, integrate into evaluation pipeline; if not, begin reimplementation using KSig library (Toth et al., GPU-accelerated signature kernel computation) + matrix-based Rényi entropy estimation for the subset selection component. (3) May 16 decision point — if FAKTUAL reimplementation is incomplete by May 16, switch to Farthest-Point Sampling (FPS) in SigLIP embedding space as the diversity baseline. FPS iteratively selects the trajectory whose minimum SW2 distance to already-selected trajectories is maximized — conceptually similar to FAKTUAL (both select for coverage/diversity) but without signature kernels. Implementable in <2 hours given the precomputed SW2 distance matrix. The core argument (mode-aware quality scoring beats mode-agnostic diversity maximization) holds regardless of which diversity baseline is used; FAKTUAL is the strongest published diversity baseline, but FPS in the same embedding space provides a fair comparison on the diversity-vs-quality axis. Note: if OT-Consensus cannot beat FPS (a simpler diversity method), it certainly cannot beat FAKTUAL.\\n\\n**Representation design**: Each demonstration trajectory τ = {(o_t, a_t, t/T)}_{t=1}^{T} is mapped to a discrete probability measure μ_τ over an embedding space. Visual observations o_t are encoded via a frozen pre-trained visual encoder into d-dimensional features; actions a_t remain in raw action space (typically 7D for manipulation); normalized timestep t/T provides temporal grounding. The ground metric is a weighted sum: c((v₁,a₁,t₁), (v₂,a₂,t₂)) = λ_v‖v₁−v₂‖² + λ_a‖a₁−a₂‖² + λ_t|t₁−t₂|², with λ weights selected via validation on a held-out task (not held-out demonstrations within the same task). **Encoder choice and transparency**: The default encoder is SigLIP-SO400M — deliberately chosen because it is SmolVLA's own vision encoder, meaning the quality metric operates in the same representation space the downstream policy will learn from. This is a design feature: OT-Consensus scores quality in the space *relevant to the policy*, not an arbitrary embedding space. However, this creates a potential confound — results might reflect representation overlap rather than the OT scoring itself. We therefore include DINOv2 as a mandatory ablation to demonstrate that the method generalizes beyond SmolVLA's own encoder.\\n\\n**Scalable pairwise distances**: We use Sliced Wasserstein-2 (SW2) distances — projecting measures onto random 1D subspaces and averaging closed-form 1D OT solutions, achieving O(Ln log n) per pair where L is the number of projections (50–200) and n is trajectory length. For RoboMimic (300 demos), the N² pairwise matrix is computationally tractable (~15 min on a single A100).\\n\\n**Mode discovery and quality scoring**: (1) Compute SW2 pairwise distance matrix over all trajectory measures. (2) Perform k-medoid clustering (PAM algorithm) in SW2-distance space to discover strategy modes. k-medoid is preferred over k-means because it operates directly on the distance matrix without requiring an embedding, and medoids are actual trajectories which aids interpretability. k is selected via silhouette analysis over k ∈ {2,...,8}. (3) Within each cluster, compute the robust barycenter using trimmed-mean OT (trimming ε=0.1 fraction of mass), using free-support barycenters with entropic regularization for computational tractability. (4) Score each trajectory by its SW2-distance to its cluster's robust barycenter: q_i = 1 / (1 + SW2(μ_i, β_m)), normalized to [0,1]. Lower distance to the mode's barycenter → higher quality (closer to mode consensus). Cross-mode scoring: demonstrations are scored only against their own mode's barycenter, not against other modes — a high-quality left-reach demonstration is not penalized for being far from the right-reach barycenter.\\n\\n**Mode discovery analysis — expected behavior and statistical power**: Expected k values: k=3 (matching proficiency levels: Worse/Okay/Better) or k=6 (matching individual operators). Since different proficiency levels may use genuinely different strategies (e.g., cautious vs aggressive grasping), k=3 is the primary hypothesis. Cluster size guarantees: with N=300 demos and k ∈ {3,6}, minimum expected cluster size is 50 (balanced clusters) to ~40 (imbalanced). Even with substantial imbalance (e.g., cluster sizes 40/100/160 for k=3), the smallest cluster exceeds Kaufman & Rousseeuw's 40+2k guideline (46 for k=3, 52 for k=6) for stable k-medoid estimation. For k=6, balanced clusters have 50 demos each, meeting the guideline; mild imbalance may push individual clusters slightly below the threshold, but k-medoid estimation remains robust above ~35 samples empirically. Robust barycenter stability: ε-trimming with ε=0.1 on a 50-demo cluster removes 5 trajectories; the barycenter is computed from 45 remaining trajectories. For SW2 with L=100 projections, this provides sufficient distributional mass for stable barycenter estimation. Sensitivity ablation (Tier A, explicit): report quality scoring correlation (Spearman ρ with operator proficiency) as a function of k ∈ {2,...,8}, with silhouette scores for each k. This directly addresses whether mode discovery is robust to k selection. If Spearman ρ is stable across k ∈ {3,...,6} (varying by less than 0.05), this demonstrates that the method is not sensitive to exact k choice. Mode validation: validate discovered modes against RoboMimic's operator identity and proficiency labels using ARI and NMI; partial correlation (ARI > 0.1) suffices to demonstrate that SW2 geometry captures meaningful strategy structure.\\n\\n**Relationship to sWk-means**: Steps 1-2 share the SW-distance + clustering pipeline with sWk-means (Luan & Hamp, DSFE 2025), which uses it for financial regime detection. OT-Consensus extends this with: (a) the trajectory-as-measure representation (visual features + actions + temporal grounding), designed for robot demonstrations rather than financial distributions; (b) robust barycenter computation within each cluster (step 3), which sWk-means does not perform; (c) the quality scoring and filtering pipeline (step 4), which transforms cluster membership into actionable curation decisions.\\n\\n**Relationship to velocity debiasing (Modi Shi et al.)**: OT-Consensus and velocity debiasing address complementary aspects of the multi-operator demonstration problem. Velocity debiasing normalizes speed variation along shared spatial paths — a data transformation that removes one specific source of distributional conflict. OT-Consensus discovers strategy modes (spatial multimodality) and scores quality within each mode — a data selection method that handles the broader problem of multiple valid strategies with varying quality. In principle, the two can be composed: apply velocity debiasing as preprocessing to normalize speed variation, then apply OT-Consensus to discover spatial strategy modes and curate within each mode. We do not evaluate this composition in the CoRL submission (to keep the contribution focused) but note it as a natural extension.\\n\\n**Why mode-aware quality beats mode-agnostic diversity — explicit hypotheses**: (H1) *Mode-aware quality vs. mode-agnostic diversity*: FAKTUAL maximizes global entropy, which on multimodal data retains low-quality demonstrations from each mode for coverage. OT-Consensus scores quality within each discovered mode, correctly deprioritizing within-mode outliers while preserving cross-mode diversity. Prediction: on RoboMimic MH, FAKTUAL retains Worse-operator demonstrations because they're 'diverse' (different from Better operators), while OT-Consensus correctly identifies them as low-quality within their strategy mode. (H2) *Distributional shape vs. scalar proxies*: MI (DemInf) computes a scalar dependency between states and actions, collapsing distributional structure. Two trajectories with identical MI but different spatiotemporal shapes are indistinguishable under MI but distinguishable under SW2. (H3) *Temporal structure preservation*: The time component of the ground metric captures temporal alignment — a trajectory with correct actions at wrong timings scores differently from one with correct timing. Smoothness metrics (RINSE) ignore whether temporally smooth trajectories are actually performing the task correctly. (H4) *Variable-length handling*: Representing trajectories as measures naturally handles variable-length demonstrations without padding or truncation. (H5) *No learned components*: Unlike DemInf (k-NN estimator + VAE), SCIZOR (self-supervised predictor), S2I (contrastive learning + expert demos), FAKTUAL (signature kernel computation), or Robometer (VLM pre-trained on 1M+ trajectories), OT-Consensus uses only a frozen visual encoder and closed-form OT — fully deterministic scoring with no training beyond the frozen encoder.\\n\\n**Key differentiations vs. related OT work**: Unlike BWD, we require no value functions, rewards, or behavioral critic — we operate purely on trajectory geometry. Unlike SWAD, we represent each trajectory as a probability measure (not a single point) and compute SW2 between measures, capturing trajectory structure. Unlike LWAIL, we address data curation, not policy learning. Unlike Robometer, we require no pre-training on large-scale trajectory datasets and are mode-aware by construction.\\n\\n**Minimum success criterion**: We consider the method validated if OT-Consensus achieves Spearman correlation with operator proficiency ≥0.1 higher than the best mode-agnostic proxy (DemInf MI or RINSE smoothness), AND downstream SmolVLA success rate improvement ≥5% absolute over the best policy-free baseline on the evaluated tasks. If these thresholds are not met, the contribution reduces to a negative result showing that distributional trajectory distances do not outperform simpler scalar proxies for demonstration curation — which is itself informative for the field but would not constitute a positive contribution.\\n\\n**Theoretical motivation (informal for CoRL, formal in extended version)**: Under an ε-contamination noise model where (1−ε) of demonstrations are 'clean' and ε are corrupted, the robust barycenter β* converges to the clean barycenter. The Robust Wasserstein Barycenter (arXiv Mar 2026) proves existence and consistency under no moment assumptions, providing theoretical backing for our ε-trimmed approach. Clean trajectories concentrate around β* while corrupted trajectories deviate. Extending Nietert et al.'s robust OT estimation guarantees to detection guarantees (false-positive/negative rates for outlier identification) constitutes non-trivial theoretical work deferred to AAAI 2027.\\n\\n**Evaluation design — two tiers for timeline management**: **Tier A (Minimal Viable Paper — commit by May 21)**: (a) *Day 1 validation gate* (May 13): Synthetic toy + RoboMimic pilot as described above (~4h). Go/no-go decision by end of day. (b) *Primary experiment — quality metric comparison*: Compute OT-Consensus, diversity baseline (FAKTUAL or FPS fallback), DemInf (MI), and random scores on all 300 RoboMimic MH demos. Evaluate each metric's correlation with known operator proficiency (Spearman rank correlation, AUC for separating Better vs. Worse operators). Critically: analyze what each metric does with the 6 operators' different strategies — does the diversity baseline retain Worse-operator demos for diversity? Does OT-Consensus correctly identify within-mode quality? (c) *Downstream policy performance — revised design with 2 seeds*: Fine-tune SmolVLA (450M) on filtered subsets (top-50% by each metric) on 2 tasks (Can, Square — chosen for difficulty spread) × 4 conditions (OT-Consensus, diversity baseline, DemInf, random) × 2 seeds = 16 runs (~64h). Same GPU budget as the previous 6 conditions × 1 seed design but with much stronger statistical backing — mean ± std across seeds enables basic significance testing. (d) *Essential ablations*: SigLIP vs. DINOv2 encoder on metric comparison to show results aren't artifacts of encoder-policy representation overlap (2 additional conditions × 2 tasks × 1 seed = 4 runs, ~16h). k sensitivity analysis: Spearman ρ vs operator proficiency for k ∈ {2,...,8} with silhouette scores — no additional GPU runs needed, only recomputation of quality scores under different clusterings. **Tier B (Full Paper — expand if on track by May 21)**: Add RINSE and SCIZOR as additional conditions (total 6 conditions); add Lift and Transport tasks (total 4 tasks); increase to 3 seeds; add top-33% filtering threshold; add ablations (k-medoid in SW2 vs. k-means in SigLIP embedding space; ground metric weight sensitivity; SW2 projection count sensitivity). **Extended version (AAAI 2027)**: Add OpenVLA-OFT (7B), LIBERO benchmark, formal theoretical analysis, S2I and CUPID as additional baselines, Robometer as an additional comparison, velocity debiasing composition experiment, comprehensive ablations.\\n\\n**Parallel writing plan**: To ensure the paper is ready by May 28, writing proceeds in parallel with experiments throughout the sprint. Days 1-3 (May 13-15): draft introduction and related work sections (can be written before experiments complete, since the framing and landscape are established). Days 4-8 (May 16-20): draft method section and begin results section as SmolVLA runs complete. Days 9-10 (May 21-22): complete results, analysis, and ablation sections. Days 11-12 (May 23-24): full paper revision and polishing. Day 12 (May 24): circulate draft for feedback. Day 13 (May 25): submit abstract on OpenReview. Days 13-15 (May 25-28): final revisions, figure polishing, and paper submission by May 28 EOD.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~220h A100 for CoRL Tier A (Day 1 validation gate: ~4h — synthetic toy SW2 + RoboMimic pilot 50-trajectory matrix; SW2 full matrix computation: ~8h — 300×300 pairwise with SigLIP+DINOv2 encoders; barycenter computation: ~4h; FAKTUAL reproduction or FPS fallback buffer: ~20h; SmolVLA fine-tuning: ~4h/run × 4 conditions × 2 tasks × 2 seeds = 64h; DINOv2 encoder ablation: ~16h; evaluation rollouts: ~4h; k sensitivity analysis: ~2h; buffer: ~30h). Tier B adds ~120h (RINSE+SCIZOR conditions, 2 more tasks, 3 seeds). Extended AAAI version adds ~700h (OpenVLA-OFT + LIBERO + Robometer comparison + velocity debiasing composition + theory ablations).\",\n      \"gpu_utilization\": \"~75% for CoRL sprint — Day 1 validation gate determines whether sprint proceeds; researcher implementing SW2 + diversity baseline pipelines, analyzing clustering results, and writing paper between experiment batches.\",\n      \"timeline\": \"CoRL 2026: 16-day sprint (May 13–28). Day 1 (May 13): validation gate — go/no-go decision by EOD. Days 2-3 (May 14-15): full SW2 matrix + FAKTUAL reproduction attempt + draft intro/related work. Day 4 (May 16): FAKTUAL decision point (use code/reimplementation or switch to FPS). Days 4-8 (May 16-20): Tier A SmolVLA training runs + draft method section. Days 9-10 (May 21-22): evaluation rollouts + analysis + k sensitivity + draft results. Tier A commit point: May 21. Days 11-12 (May 23-24): Tier B expansion (if on track) + full paper revision. Day 13 (May 25): abstract submission on OpenReview. Days 14-16 (May 25-28): final paper revisions + submission by May 28 EOD. Writing: continuous in parallel with experiments (intro/related work Days 1-3, method Days 4-8, results Days 9-10, revision Days 11-16). AAAI 2027 extension: additional 6–8 weeks for theory + extended experiments.\",\n      \"team\": \"CoRL: 1 researcher, full-time sprint with pre-existing GPU access and familiarity with lerobot/POT/geomloss. Must also attempt FAKTUAL reproduction or implement FPS fallback. AAAI extension: +1 collaborator for theoretical proofs.\",\n      \"estimated_gpu_cost\": \"CoRL Tier A: $330 (220h × $1.50/h). Tier B: +$180. AAAI extension: +$1,050. Total if all: $1,560.\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~200h A100 for CoRL Tier A\",\n      \"gpu_utilization\": \"~85% — agent handles SW2 pipeline implementation using POT/geomloss, FAKTUAL reproduction or FPS fallback implementation, SmolVLA fine-tuning orchestration, and baseline reproduction; human focuses on Day 1 validation analysis and go/no-go decision, experiment design, result interpretation, and paper writing\",\n      \"timeline\": \"CoRL: 16 days (May 13-28). Day 1: human analyzes validation gate results and makes go/no-go decision (~2h human time). Days 2-16: agent-driven computation with human checkpoints at FAKTUAL decision (Day 4) and Tier A commit (Day 10). Human writes intro/related work in parallel with Days 1-3 experiments, method section during Days 4-8, results during Days 9-10, and revision during Days 11-16. AAAI extension: +4–6 weeks.\",\n      \"team\": \"1 researcher, ~4–5h/day during CoRL sprint for experiment design, analysis, and writing; agent handles implementation and job orchestration\",\n      \"claude_api_cost\": \"$100–200 for CoRL (750–1500 turns). +$150–300 for AAAI extension.\",\n      \"estimated_gpu_cost\": \"CoRL Tier A: $300 (200h × $1.50/h). Tier B: +$120. AAAI extension: +$900.\",\n      \"risk_note\": \"CoRL sprint is tight at 16 days with May 28 hard deadline. Day 1 validation gate is the critical de-risking step — if it fails, the sprint is aborted early with minimal wasted compute (~4h). Tier A (minimal viable paper) is designed to be completable in 8 days of compute after passing the gate, leaving 7 days for Tier B expansion and writing. Key risk: FAKTUAL code availability — mitigated by FPS fallback decision on May 16, with FPS implementable in <2h. Second risk: k-medoid clustering does not discover meaningful modes on real data — mitigated by Day 1 RoboMimic pilot with explicit ARI threshold.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~320h A100 for CoRL Tier A+B\",\n      \"gpu_utilization\": \"~90% — agent queues experiments continuously; parallel ablations across SW2 hyperparameters and SmolVLA fine-tuning runs\",\n      \"timeline\": \"CoRL: 10–12 days with 4 concurrent A100 GPUs. Day 1: validation gate (4h, requires human go/no-go). Days 2-4: full pipeline + Tier A training. Days 5-8: Tier B expansion. Human writes paper in parallel throughout, targeting complete draft by Day 10 (May 22) with 6 days for revision before May 28 deadline. AAAI extension: +2–3 weeks.\",\n      \"team\": \"0 for CoRL experiments after initial setup (configure dataset paths, GPU access, library installation). Day 1 validation gate requires human judgment on go/no-go decision. Theory for AAAI requires human mathematician.\",\n      \"claude_api_cost\": \"$200–400 for CoRL. +$200–400 for AAAI extension.\",\n      \"estimated_gpu_cost\": \"CoRL: $480 (320h × $1.50/h). AAAI extension: +$1,500.\",\n      \"speed_bottleneck\": \"GPU count for parallel SmolVLA fine-tuning (each run needs 1 A100). With 4 A100s, Tier A experiments complete in ~24h compute. FAKTUAL reproduction may require installing signature kernel libraries; FPS fallback eliminates this bottleneck entirely.\",\n      \"risk_note\": \"Agent may over-explore hyperparameters without converging; FAKTUAL reproduction requires understanding signature kernel implementations (mitigated by FPS fallback on May 16). Theory for AAAI version cannot be automated. Day 1 validation gate outcome determines whether auto-research proceeds — if gate fails, abort with ~4h wasted compute.\"\n    }\n  },\n  \"target_venues\": [\n    \"CoRL 2026 (abstract deadline May 25, paper deadline May 28 EOD — planning conservatively per official Instruction for Authors 'Thursday (5/28) EOD'; primary target, empirical-focused version: mode-aware SW2 scoring vs. FAKTUAL diversity + metric comparison + SmolVLA on RoboMimic, 8 pages, no formal theory)\",\n    \"AAAI 2027 (deadline expected ~August 2026 — extended version with formal outlier detection theory, OpenVLA-OFT experiments, LIBERO benchmark, Robometer comparison, and velocity debiasing composition experiment)\",\n    \"ICLR 2027 (deadline expected ~October 2026 — most complete version, backup if AAAI timeline is insufficient for theory)\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"Diversity You Can Actually Measure: A Fast, Model-Free Diversity Metric for Robotics Datasets [FAKTUAL] (arXiv Mar 2026, 2603.11634)\",\n    \"CUPID: Curating Data your Robot Loves with Influence Functions (CoRL 2025)\",\n    \"Robot Data Curation with Mutual Information Estimators [DemInf] (RSS 2025)\",\n    \"DataMIL: Selecting Data for Robot Imitation Learning with Datamodels (ICLR 2026)\",\n    \"Curating Demonstrations using Online Experience [Demo-SCORE] (RSS 2025)\",\n    \"SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning (ICRA 2026)\",\n    \"Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning [QoQ] (arXiv Mar 2026)\",\n    \"Learning from the Best: Smoothness-Driven Metrics for Data Quality in Imitation Learning [RINSE] (ICML 2025, arXiv 2604.23000)\",\n    \"S2I: Select Segments to Imitate — Segment-Level Selection and Optimization for Mixed-Quality Demonstrations (ICRA 2025)\",\n    \"Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons (RSS 2026, arXiv 2603.02115)\",\n    \"Is Diversity All You Need for Scalable Robotic Manipulation? [velocity debiasing] (Modi Shi et al., arXiv Jul 2025, 2507.06219)\",\n    \"Automated regime classification in multidimensional time series data using sliced Wasserstein k-means clustering [sWk-means] (Luan & Hamp, arXiv 2310.01285, Data Science in Finance and Economics 2025)\",\n    \"On Data Redundancy in VLA Training [TSS] (DATA-FM Workshop @ ICLR 2026)\",\n    \"Expert or not? Assessing Data Quality in Offline Reinforcement Learning [BWD] (arXiv Oct 2025, 2510.12638)\",\n    \"Sliced-Wasserstein Distance-based Data Selection [SWAD] (Pallage & Lesage-Landry, arXiv Apr 2025, 2504.12918)\",\n    \"Consistency Matters: Defining Demonstration Data Quality Metrics in Robot Learning from Demonstration (ACM THRI 2025)\",\n    \"Latent Wasserstein Adversarial Imitation Learning [LWAIL] (ICLR 2026, 2603.05440)\",\n    \"Learning from Imperfect Demonstrations via Temporal BT-Guided Trajectory Repair (arXiv Apr 2026, 2604.04225)\",\n    \"Optimal Transport for Offline Imitation Learning [OTR] (ICLR 2023)\",\n    \"Robot Policy Learning with Temporal Optimal Transport Reward (NeurIPS 2024)\",\n    \"Cross-Domain Imitation Learning via Optimal Transport [GWIL] (ICLR 2022)\",\n    \"Watch and Match: Supercharging Imitation with Regularized Optimal Transport [ROT] (NeurIPS 2022)\",\n    \"Outlier-Robust Optimal Transport: Duality, Structure, and Statistical Analysis (Nietert et al., AISTATS 2022)\",\n    \"Robust Wasserstein Barycenter (arXiv Mar 2026)\",\n    \"Approximate Algorithms for k-Sparse Wasserstein Barycenter with Outliers (IJCAI 2024)\",\n    \"Barycenters in the Wasserstein Space (SIAM J. Math. Anal. 2011)\",\n    \"Lightspeed Geometric Dataset Distance via Sliced Optimal Transport [s-OTDD] (ICML 2025)\",\n    \"Minibatch Optimal Transport Distances: Analysis and Applications (Fatras et al., arXiv 2021, 2101.01792)\",\n    \"Unbalanced Minibatch Optimal Transport; Applications to Domain Adaptation (Fatras et al., ICML 2021)\",\n    \"Prioritized Experience Replay (ICLR 2016)\"\n  ],\n  \"description\": \"We propose OT-Consensus, a training-free, mode-aware method for scoring demonstration quality in robot learning datasets using optimal transport geometry. The central insight is that quality should be assessed relative to mode-specific consensus, not maximized globally as diversity — directly addressing the acknowledged limitation of diversity-based curation (FAKTUAL) that 'promoting diversity may be harmful when data contains multiple strategies,' and supported by recent empirical evidence (Modi Shi et al., arXiv Jul 2025) showing that expert diversity creates velocity multimodality that concretely degrades policy learning. Each trajectory is represented as a discrete measure over visual-encoder-embedded state-action-time tuples (using frozen SigLIP or DINOv2 features), and pairwise Sliced Wasserstein-2 (SW2) distances capture distributional similarity at O(Ln log n) per pair. We perform k-medoid clustering in SW2 space to discover strategy modes, then score each demonstration by its SW2-distance from its cluster's robust barycenter (computed via trimmed outlier-robust OT). The SW+clustering pipeline extends sWk-means (Luan & Hamp, DSFE 2025) — originally used for financial regime detection — with three key additions: robust barycenters for quality scoring, trajectory-as-measure representation for robot demonstrations, and mode-aware filtering. Compared to velocity debiasing (Modi Shi et al.), which normalizes speed variation along shared spatial paths via a learned velocity model, OT-Consensus operates at a different level — discovering distinct strategy modes (spatial multimodality) and scoring trajectory quality within each mode, without requiring any learned components. The two approaches are complementary: velocity debiasing removes one source of distributional conflict, while OT-Consensus provides mode-aware curation across genuinely different strategies. This revision (round 8) incorporates two targeted changes addressing reviewer feedback: (1) Addition of 'Is Diversity All You Need for Scalable Robotic Manipulation?' (Modi Shi et al., arXiv Jul 2025) to the landscape — this paper empirically validates OT-Consensus's core premise (expert diversity creates distributional conflicts harming learning) while proposing a complementary approach (velocity distribution normalization vs. OT-based mode-aware curation), positioned as operating at different levels of the problem. (2) Conservative deadline planning: paper deadline corrected to May 28 EOD per official CoRL Instruction for Authors ('Thursday 5/28 EOD'), with parallel writing plan explicitly allocated throughout the sprint (intro/related work Days 1-3, method Days 4-8, results Days 9-10, revision Days 11-16) and Tier A commit point moved to May 21 to ensure adequate writing time. We define a concrete minimum success criterion: Spearman correlation with operator proficiency ≥0.1 above the best mode-agnostic proxy AND ≥5% absolute downstream success rate improvement over the best policy-free baseline. We transparently address the encoder choice (SigLIP-SO400M is SmolVLA's own encoder, with DINOv2 ablation proving generalization). The paper follows a tiered plan: Tier A (minimal viable paper by May 21 — validation gate + metric comparison + 4×2×2 downstream + encoder ablation + k sensitivity) and Tier B (full paper by May 28 — 6 conditions × 4 tasks × 3 seeds + comprehensive ablations). Formal outlier detection theory is deferred to an extended AAAI 2027 version.\",\n  \"project_name\": \"ot_traj_consensus\",\n  \"source\": \"web_research\"\n}\n\n## Reviewer feedback (round 8)\nIssues: [\"MODERATE (Robometer missing from evaluation design): Robometer provides policy-free trajectory quality scoring — the same core value proposition as OT-Consensus — and has publicly released code and model weights. Yet it appears only in the landscape discussion, not in Tier A or Tier B evaluation. Computing Robometer scores on RoboMimic MH demos (using their released Qwen3-VL-4B model) and comparing Spearman correlations with operator proficiency against OT-Consensus's SW2 scores would be a highly informative comparison. This is the most directly competing policy-free scorer; omitting it from evaluation weakens the contribution claim. Add to Tier B at minimum, or compute just the correlation comparison (no downstream training needed) for Tier A.\", \"MODERATE (benchmark narrowness): All Tier A and Tier B experiments are on RoboMimic only (4 tasks max). CUPID evaluates on RoboMimic + real hardware, DataMIL on 60+ tasks including OXE, SCIZOR on RoboMimic + OXE + Sirius-Fleet. A CoRL paper with only RoboMimic results may feel narrow to reviewers. The argument that OT-Consensus is 'training-free and general' is undermined if it's only tested on one benchmark with 300 demos. Consider adding at least one LIBERO task (easily accessible, SmolVLA-compatible) to Tier B to demonstrate generalization beyond RoboMimic's specific operator structure.\", \"MODERATE (RL framing underdelivered): The user explicitly asked for '借助强化学习的思想，用数据本身的信息来给收集的动作对打分或筛选' — RL-inspired scoring using the data's own information. Prioritized Experience Replay (PER) is listed in key_references but the connection is barely developed in the approach. The SW2-distance-to-barycenter score is conceptually analogous to TD-error priority in PER: both measure how 'surprising' or 'deviant' a sample is from the current consensus. Explicitly developing this analogy in the introduction would better serve the user's stated direction and provide an intuitive framing for RL-literate reviewers.\", \"MINOR (score ceiling transparency): After 8 rounds, this proposal has addressed every raised issue thoroughly. The remaining score limitations (novelty 3/5, impact 3/5) are inherent to the contribution type — a methodology-application paper combining established OT tools — not fixable through further revision. The path to higher scores is empirical evidence (the Day 1 gate results). If the gate shows ARI >> 0.1 and clear mode-quality correlation, the paper becomes compelling. If not, no amount of framing will compensate. The generator should understand this and focus energy on executing the experiments, not further polishing the proposal.\"]\nFeedback: The proposal has reached a high level of maturity — all previously raised issues (missing references, deadline errors, missing competitors, minimum success criterion, FAKTUAL mitigation, encoder transparency, preliminary evidence plan) have been addressed comprehensively. The three actionable changes remaining:\n\n1. **Add Robometer to evaluation (not just landscape)**: Robometer has released code and model weights. Computing Robometer quality scores on 300 RoboMimic MH demos takes ~2-3 hours on a single A100. Compare Spearman correlation with operator proficiency: Robometer vs. OT-Consensus vs. DemInf vs. RINSE. This is the single most impactful addition — it directly tests whether a training-free geometric scorer can match a learned scorer (at least on mode-aware quality discrimination). If OT-Consensus matches or beats Robometer's correlation without requiring 1M training trajectories, that's a much stronger contribution claim than beating DemInf/RINSE alone.\n\n2. **Add one non-RoboMimic evaluation point**: Even a single LIBERO task in Tier B would address benchmark narrowness. SmolVLA already trains on LIBERO; the only additional work is computing SW2 scores and running one additional fine-tuning comparison.\n\n3. **Develop the PER analogy**: In the introduction, frame SW2-distance-to-barycenter as a 'distributional priority' score analogous to TD-error in Prioritized Experience Replay. This directly addresses the user's RL framing request and provides an intuitive hook for the broader robotics audience.\n\nOn the score ceiling: the novelty and impact scores (both 3/5) reflect the inherent nature of a methodology-application paper. These will only improve with strong empirical results. The Day 1 validation gate is the critical decision point — if results are strong, execute the sprint; if marginal, consider whether a CoRL submission is worth the effort or if more time to develop theoretical contributions (AAAI 2027) would be better spent.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.\n- Address each issue specifically.\n\n## 深度调研要求（每一轮修订都必须执行）\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。\n   - 搜索最新的相关论文（arXiv, conference proceedings）\n   - 搜索 benchmark/leaderboard 确认当前 SOTA\n   - 搜索可能遗漏的相关工作和 concurrent work\n\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，\n   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。\n\n3. **深度思考**：在修订之前，先独立思考以下问题：\n   - 这个 idea 的核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach 来解决同一个核心问题？\n   - 修订后的 idea 相比上一版有什么本质性的改进？\n\n4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，\n   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。\n\n## 针对 Review 意见的定向搜索\n\n对 reviewer 指出的每个问题，执行以下搜索流程：\n\n1. **如果 reviewer 说'已有类似工作'**：\n   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读\n   - 搜索该论文的 cited-by，找到后续跟进工作\n   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot\n\n2. **如果 reviewer 说'SOTA 过时'**：\n   - 用 Papers With Code 查看当前排行榜\n   - 搜索过去 6 个月的最新方法\n   - 更新你的 landscape 和 baseline\n\n3. **如果 reviewer 说'可行性有问题'**：\n   - 搜索类似规模实验的实际成本和时间线\n   - 搜索 GitHub 上是否有可复用的实现\n   - 搜索相关数据集/模型的可获取性\n\n4. **如果 reviewer 说'novelty 不足'**：\n   - 对核心方法尽量做 3-5 种不同关键词组合的搜索\n   - 搜索相邻领域是否有类似思路\n   - 如果确实 novelty 不足，考虑 major revision 或 pivot\n\n- Use WebSearch to find updated information if the reviewer flagged outdated claims.\n- You have full freedom in how much to change:\n  - Minor fix: if only specific details are wrong, correct them and keep everything else.\n  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.\n  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.\n- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.\n- In the output JSON, include a \"change_type\" field with one of: \"minor\", \"major\", or \"pivot\" to indicate the scope of your changes.\n- Output the revised idea as a COMPLETE JSON object (same schema as original, plus \"change_type\").\n\n## 停滞提醒\n这个 idea 已经经过 8 轮修订，近 3 轮的平均分从 3.8 到 3.2，没有明显改善。\n\n请认真思考：\n- 当前方向是否存在根本性的瓶颈？反复的 minor fix 是否在回避核心问题？\n- 如果你认为问题出在 approach 而非 framing，可以做 major revision。\n- 如果你认为 core problem 本身就有问题（gap 不存在、问题不够重要），pivot 到同一研究领域下的新方向可能是更好的选择。\n- 当然，如果你有信心这一轮修订能实现突破，继续改进也完全可以。\n\n最终由你判断——做你认为最能提升 idea 质量的选择。"
}
```

---

### Runtime record

_source line 2 · 2026-05-13T19:22:41.003Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-13T19:22:41.003Z",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb"
}
```

---

## Round 1

28 recorded events

### User

_source line 3 · 2026-05-13T19:22:41.028Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-13 (UTC).**

## Original idea
{
  "title": "Mode-Aware Quality Scoring for Demonstration Curation via Sliced Wasserstein Consensus",
  "core_problem": "How should we curate multimodal demonstration datasets that contain multiple valid strategies of varying quality? Diversity-maximizing approaches (FAKTUAL) improve average performance but explicitly fail when demonstrations contain conflicting strategies — blindly including diverse-but-poor demonstrations degrades learning. Quality-scoring approaches (CUPID, DataMIL) work well but require expensive policy training, validation rollouts, or influence function estimation. Learned reward models (Robometer) can score trajectory quality without a task-specific policy but require 1M+ training trajectories and are not mode-aware. Recent evidence from 'Is Diversity All You Need?' (Modi Shi et al., arXiv Jul 2025) sharpens this problem: they show that expert diversity creates *velocity multimodality* — different demonstrators executing the same spatial trajectory at different speeds — that directly degrades policy learning, producing 15% performance losses that their velocity normalization method recovers. This confirms that multi-operator demonstrations create distributional conflicts that harm learning, but their fix (velocity normalization) only addresses speed variation along shared paths, not the broader problem of scoring quality across genuinely different strategy modes. The field lacks a training-free quality scoring method that is *mode-aware* — one that discovers distinct strategy modes in the data and scores quality within each mode, rather than treating all demonstrations as drawn from a single distribution.",
  "opportunity": "The demonstration curation landscape has crystallized into five camps: (1) *policy-dependent quality methods* (CUPID, DataMIL, Demo-SCORE, QoQ) that achieve SOTA but require trained policies or validation rollouts; (2) *policy-free learned quality methods* (Robometer) that train general-purpose reward models on massive trajectory datasets to score quality without a task-specific policy, but require 1M+ training trajectories for pre-training and are not mode-aware — they assign a global quality score without distinguishing between multiple valid strategies. Robometer achieves strong absolute success rates on retrieval tasks (e.g., ~95% on Stir Pot where baselines score near 0%), though the reported 4.5× average improvement is inflated by near-zero baseline performance on several tasks rather than reflecting a uniform 4.5× gain; (3) *policy-free quality proxies* (DemInf, RINSE, SCIZOR) that use scalar metrics (MI, smoothness, progress) but collapse distributional structure and are mode-agnostic; (4) *policy-free diversity methods* (FAKTUAL) that maximize trajectory entropy but explicitly acknowledge 'promoting diversity may actually be harmful when the model is not capable of capturing multimodality in the data'; and (5) *distribution normalization methods* ('Is Diversity All You Need?', Modi Shi et al., arXiv Jul 2025) that identify velocity multimodality from expert diversity as a concrete failure mode and propose velocity distribution debiasing — training a velocity model to normalize action chunk speeds, recovering 15% performance (equivalent to 2.5× more pre-training data). This last camp validates the core premise that multi-operator demonstrations create distributional conflicts harming learning, but addresses only velocity variation along shared spatial paths via normalization, not the broader challenge of scoring quality across genuinely different strategy modes. This reveals a fundamental tension: diversity-based curation fails precisely when demonstrations are multimodal (multiple valid strategies), because it retains low-quality demonstrations from each mode for the sake of coverage. Distribution normalization (velocity debiasing) removes one source of multimodality but does not score trajectory quality or discover strategy modes. Recent evidence further motivates intelligent curation: 'On Data Redundancy in VLA Training' (DATA-FM @ ICLR 2026) shows that random 30% sampling of LIBERO matches full-dataset SmolVLA performance, revealing massive data redundancy — but their difficulty-based Temporal Surprise Score underperformed random selection, suggesting that naive quality proxies can be counterproductive. Empirically, FAKTUAL performs only modestly above random selection on RoboMimic MH, well below quality-based methods. The key gap: no existing training-free method provides *mode-aware quality scoring* — discovering strategy modes and assessing quality relative to mode-specific consensus, rather than against a single global reference, via a mode-agnostic scalar proxy, through a learned reward model that treats all demonstrations as a single population, or through velocity normalization that only addresses speed variation. Optimal transport geometry fills this gap naturally: Sliced Wasserstein distances define a metric space over trajectory distributions that captures shape, spread, and temporal structure; clustering in this space discovers strategy modes; and distance from each mode's robust barycenter provides a geometrically grounded, mode-aware quality score. This fills the 'good methods to quantify data quality' gap (ICLR 2026 VLA blog) with an approach that is simultaneously training-free, mode-aware, and distributional — complementary to learned scorers (Robometer), diversity-based methods (FAKTUAL), policy-dependent methods (CUPID), and distribution normalization approaches (velocity debiasing).",
  "landscape": "**Policy-dependent quality methods**: CUPID (CoRL 2025) uses influence functions estimating each demonstration's causal impact on closed-loop policy return, achieving SOTA on RoboMimic with <33% of curated data; requires a trained policy and evaluation rollouts. DataMIL (ICLR 2026) uses the datamodels paradigm for end-to-end policy-driven selection validated on 60+ tasks including OXE; requires surrogate loss computation with policy training. Demo-SCORE (RSS 2025) trains classifiers on online rollout success/failure to self-curate, achieving 15-35% gains; requires online robot interaction. QoQ (arXiv Mar 2026) uses influence functions with theoretical analysis but requires a validation set and scales O(n²). **Policy-free learned quality methods**: Robometer (RSS 2026, arXiv 2603.02115) trains a general-purpose VLM-based reward model (Qwen3-VL-4B) on RBM-1M (1M+ trajectories across 21 embodiments) using a dual objective of frame-level progress supervision and trajectory-level preference learning. Achieves strong absolute success rates on retrieval tasks (e.g., ~95% on Stir Pot where baselines score near 0%), though the reported 4.5× average improvement is inflated by near-zero baseline performance on several tasks rather than reflecting a uniform 4.5× gain. However, Robometer (a) requires 1M+ training trajectories (~6TB) for pre-training — infeasible when curating smaller datasets without pre-existing large-scale data; (b) is NOT mode-aware — it assigns a single global quality score per trajectory without distinguishing between multiple valid strategies; (c) was not evaluated against demonstration curation methods (CUPID, DemInf, RINSE, SCIZOR, FAKTUAL) — its comparisons are against VLM reward models (RoboReward, GVL, VLAC). OT-Consensus is complementary: training-free, mode-aware, and geometric, requiring no pre-training data. **Policy-free quality proxies**: DemInf (RSS 2025) estimates trajectory-level mutual information between states and actions via k-NN estimators with VAE embeddings, achieving 5-10% gains on RoboMimic; captures information content but collapses distributional structure to a scalar and is mode-agnostic. RINSE (ICML 2025, arXiv 2604.23000) uses Spectral Arc Length (SAL) and Trajectory-Envelope Distance (TED) smoothness metrics achieving 16-20% success gains; assumes smoothness universally correlates with quality, failing for tasks where jerky motions are correct. SCIZOR (ICRA 2026) combines self-supervised task progress prediction with deduplication, achieving 15.4% average improvement across RoboMimic/OXE/Sirius-Fleet; no theoretical guarantees and conflates lack of progress with low quality. S2I (ICRA 2025) performs segment-level selection using contrastive learning with 3 expert reference demonstrations; requires expert references and cannot operate fully unsupervised. Consistency Matters (ACM THRI 2025) proposes 10 motion-based consistency metrics with 76-91% success prediction accuracy; limited to geometric consistency without distributional analysis. **Policy-free diversity methods**: FAKTUAL (arXiv Mar 2026, 2603.11634) uses signature kernel entropy for diversity-based curation; fully model-free and tested on RoboMimic MH and MetaWorld. Compared against CUPID, DemInf, and Demo-SCORE. FAKTUAL performs modestly above random but below quality-based methods, and *explicitly acknowledges* that 'promoting diversity may actually be harmful when the model is not capable of capturing multimodality in the data.' This is the precise weakness OT-Consensus targets. NOTE: As of May 2026, FAKTUAL code is not publicly released; the underlying signature kernel computation can be approximated using open-source libraries (sigkernel by Salvi et al., KSig by Toth et al. for GPU-accelerated signature kernels), but the entropy estimation and subset selection components would require reimplementation. **Distribution normalization methods**: 'Is Diversity All You Need for Scalable Robotic Manipulation?' (Modi Shi et al., arXiv Jul 2025, 2507.06219) investigates data diversity along three dimensions (task, embodiment, expert) and identifies *velocity multimodality* — different demonstrators executing the same spatial trajectory at different speeds, producing distinct action chunks within fixed time windows — as a concrete failure mode from expert diversity. Their distribution debiasing method trains a lightweight velocity model (SigLIP encoder + 3-layer MLP) to predict expected velocity conditioned on observations, then rescales action chunks to normalize speed variation during policy training. This yields GO-1-Pro with 15% gains (equivalent to 2.5× pre-training data) on AgiBot G1 real-world tasks (Wipe Table, Fold Shorts, Pour Water, Make Sandwich) and ManiSkill/RoboTwin simulation benchmarks. Key relationship to OT-Consensus: (a) *Validates the core premise* — empirically confirms that multi-operator demonstrations create distributional conflicts (velocity multimodality) that directly degrade policy learning; (b) *Addresses a different level of the problem* — velocity debiasing normalizes speed variation along shared spatial paths, while OT-Consensus discovers and scores quality across genuinely different strategy modes (spatial multimodality); (c) *Complementary, not competing* — velocity normalization could be applied as a preprocessing step before OT-Consensus's mode-aware curation, first removing speed variation then scoring trajectory quality within each strategy mode; (d) *Different mechanism* — velocity debiasing is a learned normalization (requires training a velocity model) that transforms data in-place, while OT-Consensus is a training-free curation method that selects data; (e) *Different scope* — velocity debiasing specifically targets speed variation, while OT-Consensus's SW2 distance captures the full distributional shape including spatial path, action profile, and temporal structure. Notably, Modi Shi et al. distinguish 'spatial multimodality' (different paths = meaningful strategies to preserve) from 'velocity multimodality' (different speeds = noise to remove) — OT-Consensus's k-medoid clustering in SW2 space naturally discovers spatial modes, and within-mode quality scoring captures quality variation including but not limited to velocity outliers. **Data redundancy in VLA training**: 'On Data Redundancy in VLA Training' (DATA-FM Workshop @ ICLR 2026) shows that random 30% frame sampling of LIBERO matches full-dataset performance for SmolVLA and GR00T N1.5, revealing massive data redundancy. Their Temporal Surprise Score (TSS), a frame-level difficulty-based selection metric, actually underperformed random selection — suggesting that naive quality proxies can be counterproductive and motivating more principled curation approaches. Note: TSS operates at frame-level, while OT-Consensus operates at trajectory-level. **OT-based quality/distance methods (adjacent)**: sWk-means (Luan & Hamp, arXiv 2310.01285, Data Science in Finance and Economics 2025) uses sliced Wasserstein distances + k-means clustering for automated regime detection in multidimensional financial time series. The core algorithmic pipeline — compute SW distances between distributional representations of sequential data, then cluster in SW space — is a methodological precursor to OT-Consensus's first two steps. However, sWk-means (a) stops at cluster assignment and does not compute barycenters or score quality within clusters; (b) operates on financial time series regimes, not robot trajectory measures; (c) has no filtering or curation pipeline. OT-Consensus extends this SW+clustering pipeline with three key additions: robust barycenters for within-mode quality scoring, the trajectory-as-measure representation design for robot demonstrations (visual-encoder features + actions + temporal grounding), and the mode-aware curation pipeline that filters within modes while preserving cross-mode diversity. BWD/'Expert or not?' (arXiv Oct 2025, 2510.12638) introduces Bellman Wasserstein Distance for quality scoring in offline RL — value-aware OT requiring a behavioral critic; operates in RL, not IL. SWAD (Pallage & Lesage-Landry, arXiv Apr 2025, 2504.12918) uses sliced-Wasserstein distance for unsupervised anomaly detection on i.i.d. tabular data; operates on individual data points, not trajectory measures. LWAIL (ICLR 2026, 2603.05440) uses Wasserstein for state-only distribution matching in adversarial IL policy learning — addresses policy learning, not data curation. **OT in robot learning (not curation)**: OTR (ICLR 2023) assigns rewards via OT. Temporal OT Reward (NeurIPS 2024) extends with temporal ordering. GWIL (ICLR 2022) uses OT for cross-domain imitation. ROT (NeurIPS 2022) uses regularized OT for trajectory matching. **Complementary approaches**: Learning from Imperfect Demonstrations via Temporal BT-Guided Trajectory Repair (arXiv Apr 2026, 2604.04225) repairs suboptimal trajectories rather than filtering them — complementary to curation approaches. **OT theory**: Robust Wasserstein Barycenter (arXiv Mar 2026) proves existence and consistency of outlier-robust barycenters under no moment assumptions, though without finite-sample convergence rates. Outlier-Robust OT (Nietert et al., AISTATS 2022) provides minimax estimation rates for robust Wasserstein distances under ε-contamination. k-Sparse Wasserstein Barycenter with Outliers (IJCAI 2024) gives constant-factor approximations. s-OTDD (ICML 2025) demonstrates scalable sliced OT for dataset distance. **Gap**: No existing method provides training-free, mode-aware quality scoring using distributional OT geometry. FAKTUAL is mode-agnostic (diversity); DemInf/RINSE/SCIZOR are mode-agnostic (scalar quality proxies); Robometer is a learned scorer but not mode-aware and requires 1M+ trajectories; CUPID/DataMIL are mode-aware in principle but policy-dependent; sWk-means uses SW+clustering but stops at regime identification without quality scoring; velocity debiasing (Modi Shi et al.) normalizes speed variation but does not discover strategy modes or score trajectory quality. OT-Consensus uniquely combines mode awareness, quality scoring, and training-free operation.",
  "approach": "**Overview**: OT-Consensus is a training-free, mode-aware demonstration quality scoring method. We reframe the demonstration curation problem as: *given multimodal demonstrations, score quality within each strategy mode rather than globally.* The core conceptual contribution is that quality should be assessed relative to mode-specific consensus, not global diversity or global statistics — and that Sliced Wasserstein geometry naturally enables this by providing a metric space where trajectories cluster by strategy and quality is measured by distributional distance from each mode's robust center. This extends the SW+clustering pipeline introduced by sWk-means (Luan & Hamp, DSFE 2025) from financial regime detection to robot demonstration curation, with three key additions: robust barycenters for quality scoring, trajectory-as-measure representation for robot demonstrations, and mode-aware filtering. We target a focused empirical contribution for CoRL 2026 with formal theoretical analysis deferred.\n\n**Day 1 Validation Gate (May 13 — before committing to the full sprint)**: We run two preliminary experiments to validate the core hypothesis that SW2 geometry can distinguish strategy modes from quality variation, requiring ~4h total compute. (a) *Synthetic toy experiment*: Generate 200 2D trajectories from 2 strategy modes (left-reach vs right-reach, implemented as trajectories curving left vs right to reach a target) with 3 quality tiers per mode: clean (smooth, direct), noisy (Gaussian perturbations σ=0.1), and corrupted (large deviations, missing segments). Total: 2 modes × 3 tiers × ~33 trajectories = 200 trajectories. Compute the 200×200 SW2 pairwise distance matrix using L=100 random projections. Run k-medoid clustering with k=2 and k=6. Verify: (i) k=2 recovers the two strategy modes (ARI ≥ 0.8 against mode labels); (ii) within each mode cluster, SW2 distance to the mode's barycenter correlates with quality tier (Spearman ρ ≥ 0.5). Simultaneously compute MI-based scores (mutual information between trajectory segments) and smoothness scores (jerk magnitude, as in RINSE) for each trajectory. Show that these scalar metrics fail to distinguish within-mode quality tiers — specifically, that a smooth but wrong-mode trajectory scores higher on smoothness than a slightly noisy correct-mode trajectory. This validates H1 (mode separation) and H2 (within-mode quality scoring) on controlled data. (b) *RoboMimic pilot*: Randomly sample 50 trajectories from RoboMimic MH Can task. Compute the 50×50 SW2 pairwise distance matrix using SigLIP-SO400M embeddings of image observations. Run k-medoid clustering with k=3 (matching proficiency levels: Worse/Okay/Better) and k=6 (matching individual operators). Compute Adjusted Rand Index (ARI) against operator identity labels and proficiency labels for each k. (c) *Gate criterion*: Proceed with full sprint only if: synthetic toy shows clear mode separation (ARI ≥ 0.8 for k=2) AND within-mode quality correlation (ρ ≥ 0.5), AND RoboMimic pilot achieves ARI ≥ 0.1 with at least one k value against at least one label set. If the gate fails — specifically if RoboMimic ARI < 0.1 for all k and label combinations — the core hypothesis is invalidated and the sprint should pivot (e.g., to SW2 in proprioceptive-action space rather than visual embedding space, or to a different distance metric entirely). Both experiments are included as motivating figures in the paper (Figure 1a: synthetic toy SW2 distance matrix heatmap and clustering; Figure 1b: RoboMimic pilot clustering colored by operator labels).\n\n**FAKTUAL Reproduction Plan**: FAKTUAL code is not publicly released as of May 2026. Mitigation plan: (1) May 13 — contact FAKTUAL authors (Sirigiri, de Lara, Agia, Shkurti, Ramos) requesting code access. (2) May 14-15 — if code received, integrate into evaluation pipeline; if not, begin reimplementation using KSig library (Toth et al., GPU-accelerated signature kernel computation) + matrix-based Rényi entropy estimation for the subset selection component. (3) May 16 decision point — if FAKTUAL reimplementation is incomplete by May 16, switch to Farthest-Point Sampling (FPS) in SigLIP embedding space as the diversity baseline. FPS iteratively selects the trajectory whose minimum SW2 distance to already-selected trajectories is maximized — conceptually similar to FAKTUAL (both select for coverage/diversity) but without signature kernels. Implementable in <2 hours given the precomputed SW2 distance matrix. The core argument (mode-aware quality scoring beats mode-agnostic diversity maximization) holds regardless of which diversity baseline is used; FAKTUAL is the strongest published diversity baseline, but FPS in the same embedding space provides a fair comparison on the diversity-vs-quality axis. Note: if OT-Consensus cannot beat FPS (a simpler diversity method), it certainly cannot beat FAKTUAL.\n\n**Representation design**: Each demonstration trajectory τ = {(o_t, a_t, t/T)}_{t=1}^{T} is mapped to a discrete probability measure μ_τ over an embedding space. Visual observations o_t are encoded via a frozen pre-trained visual encoder into d-dimensional features; actions a_t remain in raw action space (typically 7D for manipulation); normalized timestep t/T provides temporal grounding. The ground metric is a weighted sum: c((v₁,a₁,t₁), (v₂,a₂,t₂)) = λ_v‖v₁−v₂‖² + λ_a‖a₁−a₂‖² + λ_t|t₁−t₂|², with λ weights selected via validation on a held-out task (not held-out demonstrations within the same task). **Encoder choice and transparency**: The default encoder is SigLIP-SO400M — deliberately chosen because it is SmolVLA's own vision encoder, meaning the quality metric operates in the same representation space the downstream policy will learn from. This is a design feature: OT-Consensus scores quality in the space *relevant to the policy*, not an arbitrary embedding space. However, this creates a potential confound — results might reflect representation overlap rather than the OT scoring itself. We therefore include DINOv2 as a mandatory ablation to demonstrate that the method generalizes beyond SmolVLA's own encoder.\n\n**Scalable pairwise distances**: We use Sliced Wasserstein-2 (SW2) distances — projecting measures onto random 1D subspaces and averaging closed-form 1D OT solutions, achieving O(Ln log n) per pair where L is the number of projections (50–200) and n is trajectory length. For RoboMimic (300 demos), the N² pairwise matrix is computationally tractable (~15 min on a single A100).\n\n**Mode discovery and quality scoring**: (1) Compute SW2 pairwise distance matrix over all trajectory measures. (2) Perform k-medoid clustering (PAM algorithm) in SW2-distance space to discover strategy modes. k-medoid is preferred over k-means because it operates directly on the distance matrix without requiring an embedding, and medoids are actual trajectories which aids interpretability. k is selected via silhouette analysis over k ∈ {2,...,8}. (3) Within each cluster, compute the robust barycenter using trimmed-mean OT (trimming ε=0.1 fraction of mass), using free-support barycenters with entropic regularization for computational tractability. (4) Score each trajectory by its SW2-distance to its cluster's robust barycenter: q_i = 1 / (1 + SW2(μ_i, β_m)), normalized to [0,1]. Lower distance to the mode's barycenter → higher quality (closer to mode consensus). Cross-mode scoring: demonstrations are scored only against their own mode's barycenter, not against other modes — a high-quality left-reach demonstration is not penalized for being far from the right-reach barycenter.\n\n**Mode discovery analysis — expected behavior and statistical power**: Expected k values: k=3 (matching proficiency levels: Worse/Okay/Better) or k=6 (matching individual operators). Since different proficiency levels may use genuinely different strategies (e.g., cautious vs aggressive grasping), k=3 is the primary hypothesis. Cluster size guarantees: with N=300 demos and k ∈ {3,6}, minimum expected cluster size is 50 (balanced clusters) to ~40 (imbalanced). Even with substantial imbalance (e.g., cluster sizes 40/100/160 for k=3), the smallest cluster exceeds Kaufman & Rousseeuw's 40+2k guideline (46 for k=3, 52 for k=6) for stable k-medoid estimation. For k=6, balanced clusters have 50 demos each, meeting the guideline; mild imbalance may push individual clusters slightly below the threshold, but k-medoid estimation remains robust above ~35 samples empirically. Robust barycenter stability: ε-trimming with ε=0.1 on a 50-demo cluster removes 5 trajectories; the barycenter is computed from 45 remaining trajectories. For SW2 with L=100 projections, this provides sufficient distributional mass for stable barycenter estimation. Sensitivity ablation (Tier A, explicit): report quality scoring correlation (Spearman ρ with operator proficiency) as a function of k ∈ {2,...,8}, with silhouette scores for each k. This directly addresses whether mode discovery is robust to k selection. If Spearman ρ is stable across k ∈ {3,...,6} (varying by less than 0.05), this demonstrates that the method is not sensitive to exact k choice. Mode validation: validate discovered modes against RoboMimic's operator identity and proficiency labels using ARI and NMI; partial correlation (ARI > 0.1) suffices to demonstrate that SW2 geometry captures meaningful strategy structure.\n\n**Relationship to sWk-means**: Steps 1-2 share the SW-distance + clustering pipeline with sWk-means (Luan & Hamp, DSFE 2025), which uses it for financial regime detection. OT-Consensus extends this with: (a) the trajectory-as-measure representation (visual features + actions + temporal grounding), designed for robot demonstrations rather than financial distributions; (b) robust barycenter computation within each cluster (step 3), which sWk-means does not perform; (c) the quality scoring and filtering pipeline (step 4), which transforms cluster membership into actionable curation decisions.\n\n**Relationship to velocity debiasing (Modi Shi et al.)**: OT-Consensus and velocity debiasing address complementary aspects of the multi-operator demonstration problem. Velocity debiasing normalizes speed variation along shared spatial paths — a data transformation that removes one specific source of distributional conflict. OT-Consensus discovers strategy modes (spatial multimodality) and scores quality within each mode — a data selection method that handles the broader problem of multiple valid strategies with varying quality. In principle, the two can be composed: apply velocity debiasing as preprocessing to normalize speed variation, then apply OT-Consensus to discover spatial strategy modes and curate within each mode. We do not evaluate this composition in the CoRL submission (to keep the contribution focused) but note it as a natural extension.\n\n**Why mode-aware quality beats mode-agnostic diversity — explicit hypotheses**: (H1) *Mode-aware quality vs. mode-agnostic diversity*: FAKTUAL maximizes global entropy, which on multimodal data retains low-quality demonstrations from each mode for coverage. OT-Consensus scores quality within each discovered mode, correctly deprioritizing within-mode outliers while preserving cross-mode diversity. Prediction: on RoboMimic MH, FAKTUAL retains Worse-operator demonstrations because they're 'diverse' (different from Better operators), while OT-Consensus correctly identifies them as low-quality within their strategy mode. (H2) *Distributional shape vs. scalar proxies*: MI (DemInf) computes a scalar dependency between states and actions, collapsing distributional structure. Two trajectories with identical MI but different spatiotemporal shapes are indistinguishable under MI but distinguishable under SW2. (H3) *Temporal structure preservation*: The time component of the ground metric captures temporal alignment — a trajectory with correct actions at wrong timings scores differently from one with correct timing. Smoothness metrics (RINSE) ignore whether temporally smooth trajectories are actually performing the task correctly. (H4) *Variable-length handling*: Representing trajectories as measures naturally handles variable-length demonstrations without padding or truncation. (H5) *No learned components*: Unlike DemInf (k-NN estimator + VAE), SCIZOR (self-supervised predictor), S2I (contrastive learning + expert demos), FAKTUAL (signature kernel computation), or Robometer (VLM pre-trained on 1M+ trajectories), OT-Consensus uses only a frozen visual encoder and closed-form OT — fully deterministic scoring with no training beyond the frozen encoder.\n\n**Key differentiations vs. related OT work**: Unlike BWD, we require no value functions, rewards, or behavioral critic — we operate purely on trajectory geometry. Unlike SWAD, we represent each trajectory as a probability measure (not a single point) and compute SW2 between measures, capturing trajectory structure. Unlike LWAIL, we address data curation, not policy learning. Unlike Robometer, we require no pre-training on large-scale trajectory datasets and are mode-aware by construction.\n\n**Minimum success criterion**: We consider the method validated if OT-Consensus achieves Spearman correlation with operator proficiency ≥0.1 higher than the best mode-agnostic proxy (DemInf MI or RINSE smoothness), AND downstream SmolVLA success rate improvement ≥5% absolute over the best policy-free baseline on the evaluated tasks. If these thresholds are not met, the contribution reduces to a negative result showing that distributional trajectory distances do not outperform simpler scalar proxies for demonstration curation — which is itself informative for the field but would not constitute a positive contribution.\n\n**Theoretical motivation (informal for CoRL, formal in extended version)**: Under an ε-contamination noise model where (1−ε) of demonstrations are 'clean' and ε are corrupted, the robust barycenter β* converges to the clean barycenter. The Robust Wasserstein Barycenter (arXiv Mar 2026) proves existence and consistency under no moment assumptions, providing theoretical backing for our ε-trimmed approach. Clean trajectories concentrate around β* while corrupted trajectories deviate. Extending Nietert et al.'s robust OT estimation guarantees to detection guarantees (false-positive/negative rates for outlier identification) constitutes non-trivial theoretical work deferred to AAAI 2027.\n\n**Evaluation design — two tiers for timeline management**: **Tier A (Minimal Viable Paper — commit by May 21)**: (a) *Day 1 validation gate* (May 13): Synthetic toy + RoboMimic pilot as described above (~4h). Go/no-go decision by end of day. (b) *Primary experiment — quality metric comparison*: Compute OT-Consensus, diversity baseline (FAKTUAL or FPS fallback), DemInf (MI), and random scores on all 300 RoboMimic MH demos. Evaluate each metric's correlation with known operator proficiency (Spearman rank correlation, AUC for separating Better vs. Worse operators). Critically: analyze what each metric does with the 6 operators' different strategies — does the diversity baseline retain Worse-operator demos for diversity? Does OT-Consensus correctly identify within-mode quality? (c) *Downstream policy performance — revised design with 2 seeds*: Fine-tune SmolVLA (450M) on filtered subsets (top-50% by each metric) on 2 tasks (Can, Square — chosen for difficulty spread) × 4 conditions (OT-Consensus, diversity baseline, DemInf, random) × 2 seeds = 16 runs (~64h). Same GPU budget as the previous 6 conditions × 1 seed design but with much stronger statistical backing — mean ± std across seeds enables basic significance testing. (d) *Essential ablations*: SigLIP vs. DINOv2 encoder on metric comparison to show results aren't artifacts of encoder-policy representation overlap (2 additional conditions × 2 tasks × 1 seed = 4 runs, ~16h). k sensitivity analysis: Spearman ρ vs operator proficiency for k ∈ {2,...,8} with silhouette scores — no additional GPU runs needed, only recomputation of quality scores under different clusterings. **Tier B (Full Paper — expand if on track by May 21)**: Add RINSE and SCIZOR as additional conditions (total 6 conditions); add Lift and Transport tasks (total 4 tasks); increase to 3 seeds; add top-33% filtering threshold; add ablations (k-medoid in SW2 vs. k-means in SigLIP embedding space; ground metric weight sensitivity; SW2 projection count sensitivity). **Extended version (AAAI 2027)**: Add OpenVLA-OFT (7B), LIBERO benchmark, formal theoretical analysis, S2I and CUPID as additional baselines, Robometer as an additional comparison, velocity debiasing composition experiment, comprehensive ablations.\n\n**Parallel writing plan**: To ensure the paper is ready by May 28, writing proceeds in parallel with experiments throughout the sprint. Days 1-3 (May 13-15): draft introduction and related work sections (can be written before experiments complete, since the framing and landscape are established). Days 4-8 (May 16-20): draft method section and begin results section as SmolVLA runs complete. Days 9-10 (May 21-22): complete results, analysis, and ablation sections. Days 11-12 (May 23-24): full paper revision and polishing. Day 12 (May 24): circulate draft for feedback. Day 13 (May 25): submit abstract on OpenReview. Days 13-15 (May 25-28): final revisions, figure polishing, and paper submission by May 28 EOD.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~220h A100 for CoRL Tier A (Day 1 validation gate: ~4h — synthetic toy SW2 + RoboMimic pilot 50-trajectory matrix; SW2 full matrix computation: ~8h — 300×300 pairwise with SigLIP+DINOv2 encoders; barycenter computation: ~4h; FAKTUAL reproduction or FPS fallback buffer: ~20h; SmolVLA fine-tuning: ~4h/run × 4 conditions × 2 tasks × 2 seeds = 64h; DINOv2 encoder ablation: ~16h; evaluation rollouts: ~4h; k sensitivity analysis: ~2h; buffer: ~30h). Tier B adds ~120h (RINSE+SCIZOR conditions, 2 more tasks, 3 seeds). Extended AAAI version adds ~700h (OpenVLA-OFT + LIBERO + Robometer comparison + velocity debiasing composition + theory ablations).",
      "gpu_utilization": "~75% for CoRL sprint — Day 1 validation gate determines whether sprint proceeds; researcher implementing SW2 + diversity baseline pipelines, analyzing clustering results, and writing paper between experiment batches.",
      "timeline": "CoRL 2026: 16-day sprint (May 13–28). Day 1 (May 13): validation gate — go/no-go decision by EOD. Days 2-3 (May 14-15): full SW2 matrix + FAKTUAL reproduction attempt + draft intro/related work. Day 4 (May 16): FAKTUAL decision point (use code/reimplementation or switch to FPS). Days 4-8 (May 16-20): Tier A SmolVLA training runs + draft method section. Days 9-10 (May 21-22): evaluation rollouts + analysis + k sensitivity + draft results. Tier A commit point: May 21. Days 11-12 (May 23-24): Tier B expansion (if on track) + full paper revision. Day 13 (May 25): abstract submission on OpenReview. Days 14-16 (May 25-28): final paper revisions + submission by May 28 EOD. Writing: continuous in parallel with experiments (intro/related work Days 1-3, method Days 4-8, results Days 9-10, revision Days 11-16). AAAI 2027 extension: additional 6–8 weeks for theory + extended experiments.",
      "team": "CoRL: 1 researcher, full-time sprint with pre-existing GPU access and familiarity with lerobot/POT/geomloss. Must also attempt FAKTUAL reproduction or implement FPS fallback. AAAI extension: +1 collaborator for theoretical proofs.",
      "estimated_gpu_cost": "CoRL Tier A: $330 (220h × $1.50/h). Tier B: +$180. AAAI extension: +$1,050. Total if all: $1,560."
    },
    "human_in_loop": {
      "gpu_hours": "~200h A100 for CoRL Tier A",
      "gpu_utilization": "~85% — agent handles SW2 pipeline implementation using POT/geomloss, FAKTUAL reproduction or FPS fallback implementation, SmolVLA fine-tuning orchestration, and baseline reproduction; human focuses on Day 1 validation analysis and go/no-go decision, experiment design, result interpretation, and paper writing",
      "timeline": "CoRL: 16 days (May 13-28). Day 1: human analyzes validation gate results and makes go/no-go decision (~2h human time). Days 2-16: agent-driven computation with human checkpoints at FAKTUAL decision (Day 4) and Tier A commit (Day 10). Human writes intro/related work in parallel with Days 1-3 experiments, method section during Days 4-8, results during Days 9-10, and revision during Days 11-16. AAAI extension: +4–6 weeks.",
      "team": "1 researcher, ~4–5h/day during CoRL sprint for experiment design, analysis, and writing; agent handles implementation and job orchestration",
      "claude_api_cost": "$100–200 for CoRL (750–1500 turns). +$150–300 for AAAI extension.",
      "estimated_gpu_cost": "CoRL Tier A: $300 (200h × $1.50/h). Tier B: +$120. AAAI extension: +$900.",
      "risk_note": "CoRL sprint is tight at 16 days with May 28 hard deadline. Day 1 validation gate is the critical de-risking step — if it fails, the sprint is aborted early with minimal wasted compute (~4h). Tier A (minimal viable paper) is designed to be completable in 8 days of compute after passing the gate, leaving 7 days for Tier B expansion and writing. Key risk: FAKTUAL code availability — mitigated by FPS fallback decision on May 16, with FPS implementable in <2h. Second risk: k-medoid clustering does not discover meaningful modes on real data — mitigated by Day 1 RoboMimic pilot with explicit ARI threshold."
    },
    "auto_research": {
      "gpu_hours": "~320h A100 for CoRL Tier A+B",
      "gpu_utilization": "~90% — agent queues experiments continuously; parallel ablations across SW2 hyperparameters and SmolVLA fine-tuning runs",
      "timeline": "CoRL: 10–12 days with 4 concurrent A100 GPUs. Day 1: validation gate (4h, requires human go/no-go). Days 2-4: full pipeline + Tier A training. Days 5-8: Tier B expansion. Human writes paper in parallel throughout, targeting complete draft by Day 10 (May 22) with 6 days for revision before May 28 deadline. AAAI extension: +2–3 weeks.",
      "team": "0 for CoRL experiments after initial setup (configure dataset paths, GPU access, library installation). Day 1 validation gate requires human judgment on go/no-go decision. Theory for AAAI requires human mathematician.",
      "claude_api_cost": "$200–400 for CoRL. +$200–400 for AAAI extension.",
      "estimated_gpu_cost": "CoRL: $480 (320h × $1.50/h). AAAI extension: +$1,500.",
      "speed_bottleneck": "GPU count for parallel SmolVLA fine-tuning (each run needs 1 A100). With 4 A100s, Tier A experiments complete in ~24h compute. FAKTUAL reproduction may require installing signature kernel libraries; FPS fallback eliminates this bottleneck entirely.",
      "risk_note": "Agent may over-explore hyperparameters without converging; FAKTUAL reproduction requires understanding signature kernel implementations (mitigated by FPS fallback on May 16). Theory for AAAI version cannot be automated. Day 1 validation gate outcome determines whether auto-research proceeds — if gate fails, abort with ~4h wasted compute."
    }
  },
  "target_venues": [
    "CoRL 2026 (abstract deadline May 25, paper deadline May 28 EOD — planning conservatively per official Instruction for Authors 'Thursday (5/28) EOD'; primary target, empirical-focused version: mode-aware SW2 scoring vs. FAKTUAL diversity + metric comparison + SmolVLA on RoboMimic, 8 pages, no formal theory)",
    "AAAI 2027 (deadline expected ~August 2026 — extended version with formal outlier detection theory, OpenVLA-OFT experiments, LIBERO benchmark, Robometer comparison, and velocity debiasing composition experiment)",
    "ICLR 2027 (deadline expected ~October 2026 — most complete version, backup if AAAI timeline is insufficient for theory)"
  ],
  "level": "top-tier",
  "key_references": [
    "Diversity You Can Actually Measure: A Fast, Model-Free Diversity Metric for Robotics Datasets [FAKTUAL] (arXiv Mar 2026, 2603.11634)",
    "CUPID: Curating Data your Robot Loves with Influence Functions (CoRL 2025)",
    "Robot Data Curation with Mutual Information Estimators [DemInf] (RSS 2025)",
    "DataMIL: Selecting Data for Robot Imitation Learning with Datamodels (ICLR 2026)",
    "Curating Demonstrations using Online Experience [Demo-SCORE] (RSS 2025)",
    "SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning (ICRA 2026)",
    "Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning [QoQ] (arXiv Mar 2026)",
    "Learning from the Best: Smoothness-Driven Metrics for Data Quality in Imitation Learning [RINSE] (ICML 2025, arXiv 2604.23000)",
    "S2I: Select Segments to Imitate — Segment-Level Selection and Optimization for Mixed-Quality Demonstrations (ICRA 2025)",
    "Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons (RSS 2026, arXiv 2603.02115)",
    "Is Diversity All You Need for Scalable Robotic Manipulation? [velocity debiasing] (Modi Shi et al., arXiv Jul 2025, 2507.06219)",
    "Automated regime classification in multidimensional time series data using sliced Wasserstein k-means clustering [sWk-means] (Luan & Hamp, arXiv 2310.01285, Data Science in Finance and Economics 2025)",
    "On Data Redundancy in VLA Training [TSS] (DATA-FM Workshop @ ICLR 2026)",
    "Expert or not? Assessing Data Quality in Offline Reinforcement Learning [BWD] (arXiv Oct 2025, 2510.12638)",
    "Sliced-Wasserstein Distance-based Data Selection [SWAD] (Pallage & Lesage-Landry, arXiv Apr 2025, 2504.12918)",
    "Consistency Matters: Defining Demonstration Data Quality Metrics in Robot Learning from Demonstration (ACM THRI 2025)",
    "Latent Wasserstein Adversarial Imitation Learning [LWAIL] (ICLR 2026, 2603.05440)",
    "Learning from Imperfect Demonstrations via Temporal BT-Guided Trajectory Repair (arXiv Apr 2026, 2604.04225)",
    "Optimal Transport for Offline Imitation Learning [OTR] (ICLR 2023)",
    "Robot Policy Learning with Temporal Optimal Transport Reward (NeurIPS 2024)",
    "Cross-Domain Imitation Learning via Optimal Transport [GWIL] (ICLR 2022)",
    "Watch and Match: Supercharging Imitation with Regularized Optimal Transport [ROT] (NeurIPS 2022)",
    "Outlier-Robust Optimal Transport: Duality, Structure, and Statistical Analysis (Nietert et al., AISTATS 2022)",
    "Robust Wasserstein Barycenter (arXiv Mar 2026)",
    "Approximate Algorithms for k-Sparse Wasserstein Barycenter with Outliers (IJCAI 2024)",
    "Barycenters in the Wasserstein Space (SIAM J. Math. Anal. 2011)",
    "Lightspeed Geometric Dataset Distance via Sliced Optimal Transport [s-OTDD] (ICML 2025)",
    "Minibatch Optimal Transport Distances: Analysis and Applications (Fatras et al., arXiv 2021, 2101.01792)",
    "Unbalanced Minibatch Optimal Transport; Applications to Domain Adaptation (Fatras et al., ICML 2021)",
    "Prioritized Experience Replay (ICLR 2016)"
  ],
  "description": "We propose OT-Consensus, a training-free, mode-aware method for scoring demonstration quality in robot learning datasets using optimal transport geometry. The central insight is that quality should be assessed relative to mode-specific consensus, not maximized globally as diversity — directly addressing the acknowledged limitation of diversity-based curation (FAKTUAL) that 'promoting diversity may be harmful when data contains multiple strategies,' and supported by recent empirical evidence (Modi Shi et al., arXiv Jul 2025) showing that expert diversity creates velocity multimodality that concretely degrades policy learning. Each trajectory is represented as a discrete measure over visual-encoder-embedded state-action-time tuples (using frozen SigLIP or DINOv2 features), and pairwise Sliced Wasserstein-2 (SW2) distances capture distributional similarity at O(Ln log n) per pair. We perform k-medoid clustering in SW2 space to discover strategy modes, then score each demonstration by its SW2-distance from its cluster's robust barycenter (computed via trimmed outlier-robust OT). The SW+clustering pipeline extends sWk-means (Luan & Hamp, DSFE 2025) — originally used for financial regime detection — with three key additions: robust barycenters for quality scoring, trajectory-as-measure representation for robot demonstrations, and mode-aware filtering. Compared to velocity debiasing (Modi Shi et al.), which normalizes speed variation along shared spatial paths via a learned velocity model, OT-Consensus operates at a different level — discovering distinct strategy modes (spatial multimodality) and scoring trajectory quality within each mode, without requiring any learned components. The two approaches are complementary: velocity debiasing removes one source of distributional conflict, while OT-Consensus provides mode-aware curation across genuinely different strategies. This revision (round 8) incorporates two targeted changes addressing reviewer feedback: (1) Addition of 'Is Diversity All You Need for Scalable Robotic Manipulation?' (Modi Shi et al., arXiv Jul 2025) to the landscape — this paper empirically validates OT-Consensus's core premise (expert diversity creates distributional conflicts harming learning) while proposing a complementary approach (velocity distribution normalization vs. OT-based mode-aware curation), positioned as operating at different levels of the problem. (2) Conservative deadline planning: paper deadline corrected to May 28 EOD per official CoRL Instruction for Authors ('Thursday 5/28 EOD'), with parallel writing plan explicitly allocated throughout the sprint (intro/related work Days 1-3, method Days 4-8, results Days 9-10, revision Days 11-16) and Tier A commit point moved to May 21 to ensure adequate writing time. We define a concrete minimum success criterion: Spearman correlation with operator proficiency ≥0.1 above the best mode-agnostic proxy AND ≥5% absolute downstream success rate improvement over the best policy-free baseline. We transparently address the encoder choice (SigLIP-SO400M is SmolVLA's own encoder, with DINOv2 ablation proving generalization). The paper follows a tiered plan: Tier A (minimal viable paper by May 21 — validation gate + metric comparison + 4×2×2 downstream + encoder ablation + k sensitivity) and Tier B (full paper by May 28 — 6 conditions × 4 tasks × 3 seeds + comprehensive ablations). Formal outlier detection theory is deferred to an extended AAAI 2027 version.",
  "project_name": "ot_traj_consensus",
  "source": "web_research"
}

## Reviewer feedback (round 8)
Issues: ["MODERATE (Robometer missing from evaluation design): Robometer provides policy-free trajectory quality scoring — the same core value proposition as OT-Consensus — and has publicly released code and model weights. Yet it appears only in the landscape discussion, not in Tier A or Tier B evaluation. Computing Robometer scores on RoboMimic MH demos (using their released Qwen3-VL-4B model) and comparing Spearman correlations with operator proficiency against OT-Consensus's SW2 scores would be a highly informative comparison. This is the most directly competing policy-free scorer; omitting it from evaluation weakens the contribution claim. Add to Tier B at minimum, or compute just the correlation comparison (no downstream training needed) for Tier A.", "MODERATE (benchmark narrowness): All Tier A and Tier B experiments are on RoboMimic only (4 tasks max). CUPID evaluates on RoboMimic + real hardware, DataMIL on 60+ tasks including OXE, SCIZOR on RoboMimic + OXE + Sirius-Fleet. A CoRL paper with only RoboMimic results may feel narrow to reviewers. The argument that OT-Consensus is 'training-free and general' is undermined if it's only tested on one benchmark with 300 demos. Consider adding at least one LIBERO task (easily accessible, SmolVLA-compatible) to Tier B to demonstrate generalization beyond RoboMimic's specific operator structure.", "MODERATE (RL framing underdelivered): The user explicitly asked for '借助强化学习的思想，用数据本身的信息来给收集的动作对打分或筛选' — RL-inspired scoring using the data's own information. Prioritized Experience Replay (PER) is listed in key_references but the connection is barely developed in the approach. The SW2-distance-to-barycenter score is conceptually analogous to TD-error priority in PER: both measure how 'surprising' or 'deviant' a sample is from the current consensus. Explicitly developing this analogy in the introduction would better serve the user's stated direction and provide an intuitive framing for RL-literate reviewers.", "MINOR (score ceiling transparency): After 8 rounds, this proposal has addressed every raised issue thoroughly. The remaining score limitations (novelty 3/5, impact 3/5) are inherent to the contribution type — a methodology-application paper combining established OT tools — not fixable through further revision. The path to higher scores is empirical evidence (the Day 1 gate results). If the gate shows ARI >> 0.1 and clear mode-quality correlation, the paper becomes compelling. If not, no amount of framing will compensate. The generator should understand this and focus energy on executing the experiments, not further polishing the proposal."]
Feedback: The proposal has reached a high level of maturity — all previously raised issues (missing references, deadline errors, missing competitors, minimum success criterion, FAKTUAL mitigation, encoder transparency, preliminary evidence plan) have been addressed comprehensively. The three actionable changes remaining:

1. **Add Robometer to evaluation (not just landscape)**: Robometer has released code and model weights. Computing Robometer quality scores on 300 RoboMimic MH demos takes ~2-3 hours on a single A100. Compare Spearman correlation with operator proficiency: Robometer vs. OT-Consensus vs. DemInf vs. RINSE. This is the single most impactful addition — it directly tests whether a training-free geometric scorer can match a learned scorer (at least on mode-aware quality discrimination). If OT-Consensus matches or beats Robometer's correlation without requiring 1M training trajectories, that's a much stronger contribution claim than beating DemInf/RINSE alone.

2. **Add one non-RoboMimic evaluation point**: Even a single LIBERO task in Tier B would address benchmark narrowness. SmolVLA already trains on LIBERO; the only additional work is computing SW2 scores and running one additional fine-tuning comparison.

3. **Develop the PER analogy**: In the introduction, frame SW2-distance-to-barycenter as a 'distributional priority' score analogous to TD-error in Prioritized Experience Replay. This directly addresses the user's RL framing request and provides an intuitive hook for the broader robotics audience.

On the score ceiling: the novelty and impact scores (both 3/5) reflect the inherent nature of a methodology-application paper. These will only improve with strong empirical results. The Day 1 validation gate is the critical decision point — if results are strong, execute the sprint; if marginal, consider whether a CoRL submission is worth the effort or if more time to develop theoretical contributions (AAAI 2027) would be better spent.

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
这个 idea 已经经过 8 轮修订，近 3 轮的平均分从 3.8 到 3.2，没有明显改善。

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
  "promptId": "bbda98e0-f6b9-4cc9-88b7-1263809b65cb",
  "type": "user",
  "uuid": "4376c42e-a3b2-40f6-8501-6cfdbd586ed1",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-13T19:22:41.025Z_

```json
{
  "parentUuid": "4376c42e-a3b2-40f6-8501-6cfdbd586ed1",
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
  "uuid": "902ece76-eacd-4d62-843a-f56bbeb32691",
  "timestamp": "2026-05-13T19:22:41.025Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-13T19:22:41.025Z_

```json
{
  "parentUuid": "902ece76-eacd-4d62-843a-f56bbeb32691",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "70206dc0-46ee-46d9-abd3-844150ea89ec",
  "timestamp": "2026-05-13T19:22:41.025Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-13 (UTC).**  ## Original idea {   \"title\": \"Mode-Aware Quality Scoring for Demonstration Curation via Sliced Wasse…",
  "leafUuid": "70206dc0-46ee-46d9-abd3-844150ea89ec",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Mode-aware quality scoring for demonstrations via sliced Wasserstein consensus",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb"
}
```

---

### Assistant

_source line 8 · 2026-05-13T19:23:01.953Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze the reviewer feedback and the current state of this research idea before deciding on the best course of action.

The key issues are:
1. Robometer missing from evaluation design (MODERATE)
2. Benchmark narrowness - only RoboMimic (MODERATE)
3. RL framing underdelivered - PER analogy (MODERATE)
4. Score ceiling transparency (MINOR)

The stagnation warning is important: 8 rounds, scores not improving (3.8 → 3.2 average over recent 3 rounds). The reviewer explicitly says novelty 3/5 and impact 3/5 are inherent to the contribution type.
 
I'm recognizing the core tension here: OT-Consensus combines established techniques—trajectory representation as measures, Sliced Wasserstein distances, K-medoid clustering, robust barycenters, and distance-based scoring—into a cohesive pipeline for demonstration curation. The novelty lies in this application rather than fundamental algorithmic innovation, which is why the reviewer's assessment of 3/5 for both novelty and impact reflects the nature of a methodology-application contribution. The stagnation across rounds suggests I'm hitting the ceiling of what this framing can achieve.

The reviewer's guidance is clear: empirical results are what will move the needle. Rather than continuing to reframe the contribution, I should commit to the concrete improvements they've outlined—integrating Robometer for correlation validation, expanding to LIBERO for broader evaluation, and properly developing the PER analogy in the framing. These are all actionable and grounded in the existing proposal. I need to research what's actually available and feasible with these tools before committing to the revision.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70206dc0-46ee-46d9-abd3-844150ea89ec",
  "isSidechain": false,
  "requestId": "req_011Cb17VR748o3tSAh1q4mUt",
  "type": "assistant",
  "uuid": "830ba744-c43f-452e-80e3-1b06303b27c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019CvnLa2fimrGG3bDXqDfnP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19729,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1739,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19729,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1739,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 19729,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19729
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

### Assistant

_source line 9 · 2026-05-13T19:23:01.955Z_

I'll research the three actionable items the reviewer flagged before making revisions. Let me investigate Robometer's evaluation capabilities, LIBERO compatibility, and the PER analogy.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "830ba744-c43f-452e-80e3-1b06303b27c6",
  "isSidechain": false,
  "requestId": "req_011Cb17VR748o3tSAh1q4mUt",
  "type": "assistant",
  "uuid": "ed3a8d3e-5e67-43d9-86a0-90ea86601c5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019CvnLa2fimrGG3bDXqDfnP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19729,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1739,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19729,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1739,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 19729,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19729
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

### Tool call

_source line 10 · 2026-05-13T19:23:10.632Z_

<details open><summary>🔧 Tool call — Agent · `toolu_019oLkVGKtZHiLRHrSYEUzCX`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Research Robometer evaluation",
  "prompt": "I need to understand Robometer (RSS 2026, arXiv 2603.02115) in detail for a research proposal revision. Specifically:\n\n1. Search for \"Robometer scaling general-purpose robotic reward models trajectory comparisons\" and find the paper.\n2. Use WebFetch to read the actual paper (try https://arxiv.org/abs/2603.02115).\n3. I need to know:\n   - Is code/model weights publicly released? Search GitHub for \"robometer\" or check the paper for a code link.\n   - What model architecture (Qwen3-VL-4B)? What inputs does it take?\n   - Can it score individual trajectories on RoboMimic? What format does it expect?\n   - How long would it take to score 300 RoboMimic MH demos on a single A100?\n   - Is it mode-aware or does it give a single global quality score?\n   - What benchmarks was it evaluated on? Was RoboMimic one of them?\n\n4. Also search for \"Robometer github code release\" to verify availability.\n\nReport your findings concisely - focus on practical details about using Robometer as a baseline."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed3a8d3e-5e67-43d9-86a0-90ea86601c5e",
  "isSidechain": false,
  "requestId": "req_011Cb17VR748o3tSAh1q4mUt",
  "type": "assistant",
  "uuid": "9920b2cf-48f8-41d0-97b5-dc4254567914",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019CvnLa2fimrGG3bDXqDfnP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19729,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1739,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19729,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1739,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 19729,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19729
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

### Tool call

_source line 11 · 2026-05-13T19:23:18.747Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01NvAt8tbNJEi33BXaXCpSg6`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Research LIBERO SmolVLA compatibility",
  "prompt": "I need to understand the feasibility of adding LIBERO benchmark tasks to a robot learning experiment that uses SmolVLA (450M parameter VLA model from HuggingFace/lerobot).\n\n1. Search for \"LIBERO benchmark robot manipulation SmolVLA\" and \"lerobot LIBERO dataset\"\n2. Search for \"SmolVLA LIBERO fine-tuning\" to see if anyone has done this\n3. Use WebFetch to check https://huggingface.co/datasets if LIBERO datasets are available in lerobot format\n4. Search for \"LIBERO demonstration dataset multimodal strategies operators\" - I need to know if LIBERO has the multi-operator structure needed (different demonstrators with different strategies) similar to RoboMimic MH\n\nKey questions:\n- Is LIBERO data readily available in lerobot/SmolVLA-compatible format?\n- Does LIBERO have multi-operator demonstrations with known quality labels? (This is critical - OT-Consensus needs demonstrations from multiple operators/strategies to test mode discovery)\n- How many demonstrations per task? How many tasks?\n- What would be the additional compute cost to add 1-2 LIBERO tasks?\n\nReport concisely with practical feasibility assessment."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9920b2cf-48f8-41d0-97b5-dc4254567914",
  "isSidechain": false,
  "requestId": "req_011Cb17VR748o3tSAh1q4mUt",
  "type": "assistant",
  "uuid": "c85b7f12-cdbc-46ba-8481-869f00e158fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019CvnLa2fimrGG3bDXqDfnP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19729,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1739,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19729,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1739,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 19729,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19729
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

### Tool call

_source line 12 · 2026-05-13T19:23:27.304Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01V31carR8fwCygXB6SPNPqC`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Research PER-OT analogy and RL framing",
  "prompt": "I'm developing a research proposal for robot demonstration curation using optimal transport (OT). A reviewer asked me to better develop the analogy between our SW2-distance-to-barycenter quality score and TD-error priority in Prioritized Experience Replay (PER, Schaul et al. ICLR 2016).\n\n1. Search for \"prioritized experience replay optimal transport\" and \"distributional priority scoring demonstrations\"\n2. Search for \"TD error analogy imitation learning demonstration quality\"  \n3. Search for \"experience replay demonstration curation scoring offline\"\n4. Search for \"distributional reinforcement learning optimal transport\" to find any existing connections between distributional RL and OT\n\nI want to understand:\n- Has anyone explicitly connected PER-style priority scoring to demonstration curation before?\n- Is the analogy between \"TD-error as surprise/deviation from expected value\" and \"SW2-distance-to-barycenter as deviation from mode consensus\" technically sound?\n- Are there other RL concepts (beyond PER) that connect naturally to this idea? E.g., distributional RL, hindsight experience replay, etc.\n- Any papers that use OT-based scoring as a priority/importance weight in replay or data selection?\n\nProvide a concise summary of findings and suggest how to frame the PER analogy compellingly in 2-3 sentences for a paper introduction."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c85b7f12-cdbc-46ba-8481-869f00e158fd",
  "isSidechain": false,
  "requestId": "req_011Cb17VR748o3tSAh1q4mUt",
  "type": "assistant",
  "uuid": "ce0f3549-b738-4b93-a4ce-e2227e609018",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019CvnLa2fimrGG3bDXqDfnP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19729,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1739,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19729,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1739,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 19729,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19729
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

### Tool result

_source line 13 · 2026-05-13T19:25:27.242Z_

<details><summary>↩ Tool result · `toolu_01V31carR8fwCygXB6SPNPqC`</summary>

```text
Now I have a comprehensive picture. Here is my synthesis of the findings.

---

## Summary of Findings

### 1. Has anyone explicitly connected PER-style priority scoring to demonstration curation?

**Not directly, but closely adjacent work exists.** No paper explicitly frames demonstration curation as a PER-style prioritization problem using OT distances. However, multiple lines of work converge on the same conceptual territory:

- **Hindsight Goal Ranking (HGR)** (Nguyen & La, 2019) already uses TD-error magnitude to prioritize which replayed goals are most "instructive" within HER, establishing that TD-error-based prioritization generalizes beyond standard replay to goal-conditioned and demonstration-augmented settings.
- **Quality over Quantity (QoQ)** (arXiv 2603.09056, 2026) curates robot demonstrations using influence functions -- scoring each trajectory by its gradient-aligned contribution to validation loss. This is a data-valuation approach to the same curation problem you address, but does not use OT.
- **RINSE** (arXiv 2604.23000, 2026) scores demonstrations by trajectory smoothness (Spectral Arc Length + Trajectory-Envelope Distance), grounded in motor control theory. Again, a quality-scoring framework for demonstrations, but not OT-based.
- **Robot Data Curation with Mutual Information Estimators** (RSS 2025) estimates relative quality via state diversity and action predictability.

The gap your work fills -- using SW2-distance-to-barycenter as the scoring mechanism -- appears genuinely novel in the demonstration curation literature.

### 2. Is the PER / SW2-barycenter analogy technically sound?

**Yes, and it is stronger than a loose metaphor.** The structural parallel holds at multiple levels:

| PER (Schaul et al., 2016) | SW2-Barycenter Quality Score |
|---|---|
| TD-error = |r + gamma * V(s') - V(s)| | SW2 distance to barycenter of demonstration set |
| Measures "surprise" -- deviation from the agent's current value estimate | Measures "deviation" -- how far a demonstration's distribution sits from the consensus mode |
| High TD-error --> high priority (transition is informative) | High SW2 distance --> low quality (demonstration is an outlier) |
| Uses importance sampling weights to correct the bias introduced by non-uniform sampling | Could analogously use inverse-SW2 weights for importance-weighted behavioral cloning |

The key conceptual difference is that in PER, high deviation means *useful* (the agent should learn from surprises), while in your demonstration curation setting, high deviation means *suspicious* (the demonstration may be low-quality or an outlier). This is actually a feature, not a bug -- the analogy illuminates that the same "distance from expected" mechanism can serve opposite purposes depending on whether you are curating *what to learn from* (filtering outliers) versus *what to update on* (prioritizing surprises). You should acknowledge this polarity inversion explicitly.

The analogy also has a distributional-theoretic grounding: Bellemare, Dabney & Munos (2017) proved that the distributional Bellman operator is a contraction in the p-Wasserstein metric. This means the RL community already conceptualizes value learning through the lens of Wasserstein distances. Your SW2-based scoring imports that same metric family into the demonstration curation domain.

### 3. Other RL concepts that connect naturally

Several additional RL ideas strengthen the intellectual lineage:

- **Distributional RL (Bellemare et al., 2017; Dabney et al., 2018):** The entire distributional RL program models return *distributions*, not just expectations, and the foundational convergence proof relies on Wasserstein contraction. Dabney et al. (2018) close the theory-practice gap by using quantile regression that directly minimizes the 1-Wasserstein distance. Your work extends this distributional thinking: instead of modeling return distributions, you model *demonstration distributions* and measure quality via the same OT metric family.

- **SinkhornDRL (distributional RL via Sinkhorn iterations):** Uses Sinkhorn divergence (regularized Wasserstein) to minimize the gap between current and target return distributions. This is a direct precedent for using OT-based losses in RL pipelines.

- **Hindsight Experience Replay (HER) + Goal Ranking:** HER re-labels failed trajectories with achieved goals. When combined with TD-error-based goal ranking (HGR), it prioritizes goals from which the agent can learn the most. Your barycenter-distance scoring performs an analogous function: it identifies which demonstrations carry the most representative (or, inversely, the most anomalous) information.

- **Offline RL with Wasserstein Regularization (arXiv 2507.10843):** Uses OT maps (via input-convex neural networks) to regularize offline RL policies, ensuring they stay close to the behavior policy in a Wasserstein sense. This shows the RL community already uses OT for distributional constraints in offline settings.

### 4. Papers using OT-based scoring for priority/importance weighting in replay or data selection

Several papers are directly relevant:

- **Optimal Transport Relabeling (OTR)** (Luo et al., ICLR 2023 Oral): Uses OT to compute optimal alignment between unlabeled offline trajectories and expert demonstrations, producing a similarity-as-reward score. This is the closest existing work to your idea -- it uses OT to *score* offline data, though for reward labeling rather than filtering/curation.
- **Sliced-Wasserstein Distance-based Data Selection** (arXiv 2504.12918, 2025): Proposes using SW distance as an unsupervised anomaly detection method for training data selection, leveraging distance to the barycenter of the majority group with a controllable Wasserstein ball radius. This is essentially your mechanism applied to general ML data curation rather than robot demonstrations.
- **ROER: Regularized Optimal Experience Replay** (arXiv 2407.03995): Applies OT-inspired regularization to experience replay sampling.
- **Rethinking OT in Offline RL** (arXiv 2410.14069): Recasts offline RL as an OT problem -- finding a policy that maps states to the best expert actions.

---

## Suggested Framing for the Paper (2-3 sentences)

Here is a suggested passage for your introduction or related work section:

> "Our SW2-distance-to-barycenter quality score draws a structural analogy to Prioritized Experience Replay (Schaul et al., 2016), where TD-error magnitude serves as a proxy for transition informativeness by quantifying deviation from the agent's current value estimate. In our framework, the sliced Wasserstein distance to the demonstration barycenter similarly quantifies each trajectory's deviation from the distributional consensus of the demonstration set, but with inverted polarity: whereas PER *up-weights* high-deviation transitions to accelerate learning, our score *down-weights* high-deviation demonstrations to filter outliers -- the same 'distance from expected' mechanism serving curation rather than prioritization. This connection is further grounded by distributional RL theory (Bellemare et al., 2017), which established Wasserstein contraction as the natural metric for value distribution convergence, and by recent work using optimal transport for offline data scoring (Luo et al., 2023; Pallage & Lesage-Landry, 2025)."

---

Sources:
- [Prioritized Experience Replay (Schaul et al., 2016)](https://arxiv.org/abs/1511.05952)
- [Understanding Prioritized Experience Replay](https://danieltakeshi.github.io/2019/07/14/per/)
- [Quality over Quantity: Demonstration Curation via Influence Functions](https://arxiv.org/abs/2603.09056)
- [RINSE: Smoothness-Driven Metrics for Data Quality in Imitation Learning](https://arxiv.org/abs/2604.23000)
- [Optimal Transport for Offline Imitation Learning (OTR, ICLR 2023)](https://arxiv.org/abs/2303.13971)
- [Sliced-Wasserstein Distance-based Data Selection](https://arxiv.org/abs/2504.12918)
- [Distributional RL with Regularized Wasserstein Loss](https://arxiv.org/abs/2202.00769)
- [Distributional RL with Quantile Regression (Dabney et al., 2018)](https://arxiv.org/abs/1710.10044)
- [Offline RL with Wasserstein Regularization via OT Maps](https://arxiv.org/abs/2507.10843)
- [Rethinking Optimal Transport in Offline RL](https://arxiv.org/abs/2410.14069)
- [ROER: Regularized Optimal Experience Replay](https://arxiv.org/html/2407.03995)
- [Hindsight Experience Replay with Experience Ranking](https://ieeexplore.ieee.org/document/8850705/)
- [Hindsight Goal Ranking on Replay Buffer](https://arxiv.org/abs/2110.15043)
- [RIZE: Regularized Imitation Learning via Distributional RL](https://arxiv.org/html/2502.20089v1)
- [Wasserstein Adversarial Imitation Learning](https://arxiv.org/abs/1906.08113)
- [Primal Wasserstein Imitation Learning](https://openreview.net/forum?id=TtYSU29zgR)
- [Sliced-Wasserstein-based Anomaly Detection](https://arxiv.org/html/2410.21712)
- [Robot Data Curation with Mutual Information Estimators (RSS 2025)](https://roboticsconference.org/program/papers/23/)
- [Consistency Matters: Defining Demonstration Data Quality Metrics](https://arxiv.org/html/2412.14309v1)
- [Distributional Reinforcement Learning (MIT Press, open access)](https://direct.mit.edu/books/oa-monograph-pdf/2111075/book_9780262374026.pdf)

agentId: afdca84e20083ff80 (use SendMessage with to: 'afdca84e20083ff80' to continue this agent)
&lt;usage>total_tokens: 26385
tool_uses: 15
duration_ms: 119934&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ce0f3549-b738-4b93-a4ce-e2227e609018",
  "isSidechain": false,
  "promptId": "bbda98e0-f6b9-4cc9-88b7-1263809b65cb",
  "type": "user",
  "uuid": "f9e9c596-818c-4d4b-9a3f-f85ffa7b82f8",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm developing a research proposal for robot demonstration curation using optimal transport (OT). A reviewer asked me to better develop the analogy between our SW2-distance-to-barycenter quality score and TD-error priority in Prioritized Experience Replay (PER, Schaul et al. ICLR 2016).\n\n1. Search for \"prioritized experience replay optimal transport\" and \"distributional priority scoring demonstrations\"\n2. Search for \"TD error analogy imitation learning demonstration quality\"  \n3. Search for \"experience replay demonstration curation scoring offline\"\n4. Search for \"distributional reinforcement learning optimal transport\" to find any existing connections between distributional RL and OT\n\nI want to understand:\n- Has anyone explicitly connected PER-style priority scoring to demonstration curation before?\n- Is the analogy between \"TD-error as surprise/deviation from expected value\" and \"SW2-distance-to-barycenter as deviation from mode consensus\" technically sound?\n- Are there other RL concepts (beyond PER) that connect naturally to this idea? E.g., distributional RL, hindsight experience replay, etc.\n- Any papers that use OT-based scoring as a priority/importance weight in replay or data selection?\n\nProvide a concise summary of findings and suggest how to frame the PER analogy compellingly in 2-3 sentences for a paper introduction.",
    "agentId": "afdca84e20083ff80",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have a comprehensive picture. Here is my synthesis of the findings.\n\n---\n\n## Summary of Findings\n\n### 1. Has anyone explicitly connected PER-style priority scoring to demonstration curation?\n\n**Not directly, but closely adjacent work exists.** No paper explicitly frames demonstration curation as a PER-style prioritization problem using OT distances. However, multiple lines of work converge on the same conceptual territory:\n\n- **Hindsight Goal Ranking (HGR)** (Nguyen & La, 2019) already uses TD-error magnitude to prioritize which replayed goals are most \"instructive\" within HER, establishing that TD-error-based prioritization generalizes beyond standard replay to goal-conditioned and demonstration-augmented settings.\n- **Quality over Quantity (QoQ)** (arXiv 2603.09056, 2026) curates robot demonstrations using influence functions -- scoring each trajectory by its gradient-aligned contribution to validation loss. This is a data-valuation approach to the same curation problem you address, but does not use OT.\n- **RINSE** (arXiv 2604.23000, 2026) scores demonstrations by trajectory smoothness (Spectral Arc Length + Trajectory-Envelope Distance), grounded in motor control theory. Again, a quality-scoring framework for demonstrations, but not OT-based.\n- **Robot Data Curation with Mutual Information Estimators** (RSS 2025) estimates relative quality via state diversity and action predictability.\n\nThe gap your work fills -- using SW2-distance-to-barycenter as the scoring mechanism -- appears genuinely novel in the demonstration curation literature.\n\n### 2. Is the PER / SW2-barycenter analogy technically sound?\n\n**Yes, and it is stronger than a loose metaphor.** The structural parallel holds at multiple levels:\n\n| PER (Schaul et al., 2016) | SW2-Barycenter Quality Score |\n|---|---|\n| TD-error = |r + gamma * V(s') - V(s)| | SW2 distance to barycenter of demonstration set |\n| Measures \"surprise\" -- deviation from the agent's current value estimate | Measures \"deviation\" -- how far a demonstration's distribution sits from the consensus mode |\n| High TD-error --> high priority (transition is informative) | High SW2 distance --> low quality (demonstration is an outlier) |\n| Uses importance sampling weights to correct the bias introduced by non-uniform sampling | Could analogously use inverse-SW2 weights for importance-weighted behavioral cloning |\n\nThe key conceptual difference is that in PER, high deviation means *useful* (the agent should learn from surprises), while in your demonstration curation setting, high deviation means *suspicious* (the demonstration may be low-quality or an outlier). This is actually a feature, not a bug -- the analogy illuminates that the same \"distance from expected\" mechanism can serve opposite purposes depending on whether you are curating *what to learn from* (filtering outliers) versus *what to update on* (prioritizing surprises). You should acknowledge this polarity inversion explicitly.\n\nThe analogy also has a distributional-theoretic grounding: Bellemare, Dabney & Munos (2017) proved that the distributional Bellman operator is a contraction in the p-Wasserstein metric. This means the RL community already conceptualizes value learning through the lens of Wasserstein distances. Your SW2-based scoring imports that same metric family into the demonstration curation domain.\n\n### 3. Other RL concepts that connect naturally\n\nSeveral additional RL ideas strengthen the intellectual lineage:\n\n- **Distributional RL (Bellemare et al., 2017; Dabney et al., 2018):** The entire distributional RL program models return *distributions*, not just expectations, and the foundational convergence proof relies on Wasserstein contraction. Dabney et al. (2018) close the theory-practice gap by using quantile regression that directly minimizes the 1-Wasserstein distance. Your work extends this distributional thinking: instead of modeling return distributions, you model *demonstration distributions* and measure quality via the same OT metric family.\n\n- **SinkhornDRL (distributional RL via Sinkhorn iterations):** Uses Sinkhorn divergence (regularized Wasserstein) to minimize the gap between current and target return distributions. This is a direct precedent for using OT-based losses in RL pipelines.\n\n- **Hindsight Experience Replay (HER) + Goal Ranking:** HER re-labels failed trajectories with achieved goals. When combined with TD-error-based goal ranking (HGR), it prioritizes goals from which the agent can learn the most. Your barycenter-distance scoring performs an analogous function: it identifies which demonstrations carry the most representative (or, inversely, the most anomalous) information.\n\n- **Offline RL with Wasserstein Regularization (arXiv 2507.10843):** Uses OT maps (via input-convex neural networks) to regularize offline RL policies, ensuring they stay close to the behavior policy in a Wasserstein sense. This shows the RL community already uses OT for distributional constraints in offline settings.\n\n### 4. Papers using OT-based scoring for priority/importance weighting in replay or data selection\n\nSeveral papers are directly relevant:\n\n- **Optimal Transport Relabeling (OTR)** (Luo et al., ICLR 2023 Oral): Uses OT to compute optimal alignment between unlabeled offline trajectories and expert demonstrations, producing a similarity-as-reward score. This is the closest existing work to your idea -- it uses OT to *score* offline data, though for reward labeling rather than filtering/curation.\n- **Sliced-Wasserstein Distance-based Data Selection** (arXiv 2504.12918, 2025): Proposes using SW distance as an unsupervised anomaly detection method for training data selection, leveraging distance to the barycenter of the majority group with a controllable Wasserstein ball radius. This is essentially your mechanism applied to general ML data curation rather than robot demonstrations.\n- **ROER: Regularized Optimal Experience Replay** (arXiv 2407.03995): Applies OT-inspired regularization to experience replay sampling.\n- **Rethinking OT in Offline RL** (arXiv 2410.14069): Recasts offline RL as an OT problem -- finding a policy that maps states to the best expert actions.\n\n---\n\n## Suggested Framing for the Paper (2-3 sentences)\n\nHere is a suggested passage for your introduction or related work section:\n\n> \"Our SW2-distance-to-barycenter quality score draws a structural analogy to Prioritized Experience Replay (Schaul et al., 2016), where TD-error magnitude serves as a proxy for transition informativeness by quantifying deviation from the agent's current value estimate. In our framework, the sliced Wasserstein distance to the demonstration barycenter similarly quantifies each trajectory's deviation from the distributional consensus of the demonstration set, but with inverted polarity: whereas PER *up-weights* high-deviation transitions to accelerate learning, our score *down-weights* high-deviation demonstrations to filter outliers -- the same 'distance from expected' mechanism serving curation rather than prioritization. This connection is further grounded by distributional RL theory (Bellemare et al., 2017), which established Wasserstein contraction as the natural metric for value distribution convergence, and by recent work using optimal transport for offline data scoring (Luo et al., 2023; Pallage & Lesage-Landry, 2025).\"\n\n---\n\nSources:\n- [Prioritized Experience Replay (Schaul et al., 2016)](https://arxiv.org/abs/1511.05952)\n- [Understanding Prioritized Experience Replay](https://danieltakeshi.github.io/2019/07/14/per/)\n- [Quality over Quantity: Demonstration Curation via Influence Functions](https://arxiv.org/abs/2603.09056)\n- [RINSE: Smoothness-Driven Metrics for Data Quality in Imitation Learning](https://arxiv.org/abs/2604.23000)\n- [Optimal Transport for Offline Imitation Learning (OTR, ICLR 2023)](https://arxiv.org/abs/2303.13971)\n- [Sliced-Wasserstein Distance-based Data Selection](https://arxiv.org/abs/2504.12918)\n- [Distributional RL with Regularized Wasserstein Loss](https://arxiv.org/abs/2202.00769)\n- [Distributional RL with Quantile Regression (Dabney et al., 2018)](https://arxiv.org/abs/1710.10044)\n- [Offline RL with Wasserstein Regularization via OT Maps](https://arxiv.org/abs/2507.10843)\n- [Rethinking Optimal Transport in Offline RL](https://arxiv.org/abs/2410.14069)\n- [ROER: Regularized Optimal Experience Replay](https://arxiv.org/html/2407.03995)\n- [Hindsight Experience Replay with Experience Ranking](https://ieeexplore.ieee.org/document/8850705/)\n- [Hindsight Goal Ranking on Replay Buffer](https://arxiv.org/abs/2110.15043)\n- [RIZE: Regularized Imitation Learning via Distributional RL](https://arxiv.org/html/2502.20089v1)\n- [Wasserstein Adversarial Imitation Learning](https://arxiv.org/abs/1906.08113)\n- [Primal Wasserstein Imitation Learning](https://openreview.net/forum?id=TtYSU29zgR)\n- [Sliced-Wasserstein-based Anomaly Detection](https://arxiv.org/html/2410.21712)\n- [Robot Data Curation with Mutual Information Estimators (RSS 2025)](https://roboticsconference.org/program/papers/23/)\n- [Consistency Matters: Defining Demonstration Data Quality Metrics](https://arxiv.org/html/2412.14309v1)\n- [Distributional Reinforcement Learning (MIT Press, open access)](https://direct.mit.edu/books/oa-monograph-pdf/2111075/book_9780262374026.pdf)"
      }
    ],
    "totalDurationMs": 119934,
    "totalTokens": 26385,
    "totalToolUseCount": 15,
    "usage": {
      "input_tokens": 1026,
      "cache_creation_input_tokens": 1133,
      "cache_read_input_tokens": 21744,
      "output_tokens": 2482,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1133
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1026,
          "output_tokens": 2482,
          "cache_read_input_tokens": 21744,
          "cache_creation_input_tokens": 1133,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1133,
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
  "sourceToolAssistantUUID": "ce0f3549-b738-4b93-a4ce-e2227e609018",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 14_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-13 (UTC).**  ## Original idea {   \"title\": \"Mode-Aware Quality Scoring for Demonstration Curation via Sliced Wasse…",
  "leafUuid": "f9e9c596-818c-4d4b-9a3f-f85ffa7b82f8",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Mode-aware quality scoring for demonstrations via sliced Wasserstein consensus",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb"
}
```

---

### Tool result

_source line 16 · 2026-05-13T19:25:29.322Z_

<details><summary>↩ Tool result · `toolu_01NvAt8tbNJEi33BXaXCpSg6`</summary>

```text
I now have all the information needed to provide a comprehensive feasibility assessment.

---

## LIBERO + SmolVLA Feasibility Assessment for OT-Consensus Experiments

### 1. Data Availability in LeRobot Format

**Fully available and ready to use.** Multiple LIBERO datasets exist in LeRobot format on HuggingFace:

- Official: `lerobot/libero_10_image`, `lerobot/libero_spatial_image`, `lerobot/libero_goal_image`, `lerobot/libero_object_image`
- Community (cleaned, no-ops removed): `IPEC-COMMUNITY/libero_*_no_noops_1.0.0_lerobot`
- Full 90-task suite: `jesbu1/libero_90_lerobot`
- Official preprocessed: `HuggingFaceVLA/libero`

There is also a pretrained SmolVLA checkpoint specifically for LIBERO: `HuggingFaceVLA/smolvla_libero`. Training commands are documented in the [lerobot LIBERO docs](https://huggingface.co/docs/lerobot/en/libero). Integration is first-class -- `pip install -e ".[libero]"` and you're running.

### 2. CRITICAL BLOCKER: No Multi-Operator / Multi-Strategy Structure

**LIBERO does NOT have the multi-operator demonstration structure that OT-Consensus requires.** This is the key finding:

- LIBERO provides **50 demonstrations per task**, collected via SpaceMouse teleoperation at 20 Hz with automatic filtering and validation.
- The paper and documentation **never specify multiple operators**. The data appears to be collected by a single team/operator with a consistent strategy, then filtered for quality.
- There are **no quality labels** (no "better"/"okay"/"worse" operator tags).
- There are **no strategy labels** or any explicit multi-modal behavior structure.

**Contrast with RoboMimic MH**, which is explicitly designed for multi-operator research:
- RoboMimic MH has **300 demonstrations from 6 operators** (2 "better", 2 "okay", 2 "worse"), each collecting 50 demos per task.
- Demonstrations carry **explicit operator identity and proficiency labels**.
- This is exactly the structure OT-Consensus needs for mode discovery across different demonstrator strategies.

LIBERO's 50 demos per task are high-quality and relatively uniform -- the opposite of what you need to test mode discovery.

### 3. Dataset Scale

| Suite | Tasks | Demos/Task | Total Demos |
|-------|-------|-----------|-------------|
| LIBERO-Spatial | 10 | 50 | 500 |
| LIBERO-Object | 10 | 50 | 500 |
| LIBERO-Goal | 10 | 50 | 500 |
| LIBERO-90 | 90 | 50 | 4,500 |
| LIBERO-Long (libero_10) | 10 | 50 | 500 |
| **Total** | **130** | | **6,500** |

Observations: 7D action space (6D EEF delta + gripper), two camera views (workspace + wrist), 8D proprioceptive state.

### 4. Compute Cost Estimate for 1-2 LIBERO Tasks

Based on confirmed training configs and community reports:

- **SmolVLA on LIBERO**: 100,000 steps, batch size 64
- **Hardware**: 1x RTX 4090 (24GB) is sufficient; an L4 GPU (Google Colab) also works
- **Training time**: ~4-12 hours per fine-tuning run on a single consumer GPU
- **Fine-tuning from pretrained SmolVLA base**: Much cheaper -- one community report did 5,000 steps in ~4 hours on an L4
- **For 1-2 tasks** (50-100 demonstrations): On the lower end, likely 4-6 hours on a single 4090

The compute cost to add 1-2 LIBERO tasks is minimal -- a few GPU-hours.

### 5. Practical Feasibility Verdict

**Technically trivial, scientifically inappropriate for OT-Consensus.**

- Adding LIBERO tasks to a SmolVLA pipeline is straightforward. The datasets are ready, the training pipeline is documented, compute is cheap (single consumer GPU, a few hours).
- **However, LIBERO data lacks the multi-operator/multi-strategy structure that is fundamental to OT-Consensus.** The 50 demos per task appear to come from a single operator or a uniform collection protocol with quality filtering. There are no operator labels, no quality labels, and no known multi-modal behavior in the demonstrations.
- If you ran OT-Consensus on LIBERO data, you would likely find a single mode (or meaningless noise clusters), which would not validate the method's mode discovery capabilities.

### Recommendation

If you want a simulation benchmark with multi-operator structure for OT-Consensus, **stick with RoboMimic MH** (which was designed for exactly this). If you want to add LIBERO for other reasons (e.g., testing SmolVLA policy quality, evaluating transfer, or benchmarking against published VLA numbers), it is cheap and easy to add. But it won't serve the multi-operator mode discovery purpose.

An alternative path: you could **synthetically create multi-strategy LIBERO data** by collecting your own demonstrations with deliberately different strategies (e.g., different grasp approaches, different waypoints), but this requires manual effort and defeats the purpose of using an existing benchmark.

Sources:
- [LeRobot LIBERO Documentation](https://huggingface.co/docs/lerobot/en/libero)
- [LIBERO Paper (NeurIPS 2023)](https://arxiv.org/abs/2306.03310)
- [LIBERO GitHub](https://github.com/Lifelong-Robot-Learning/LIBERO)
- [SmolVLA LIBERO Training Issue #3287](https://github.com/huggingface/lerobot/issues/3287)
- [SmolVLA LIBERO Reproduction Issue #2354](https://github.com/huggingface/lerobot/issues/2354)
- [Fine-Tuning SmolVLA Guide (Medium)](https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632)
- [RoboMimic Multi-Human Dataset](https://robomimic.github.io/docs/datasets/robomimic_v0.1.html)
- [HuggingFaceVLA/smolvla_libero Checkpoint](https://huggingface.co/HuggingFaceVLA/smolvla_libero)
- [LIBERO Datasets on HuggingFace](https://huggingface.co/datasets?search=libero+lerobot)

agentId: a7f0f63bdf2589c2f (use SendMessage with to: 'a7f0f63bdf2589c2f' to continue this agent)
&lt;usage>total_tokens: 23767
tool_uses: 15
duration_ms: 130571&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c85b7f12-cdbc-46ba-8481-869f00e158fd",
  "isSidechain": false,
  "promptId": "bbda98e0-f6b9-4cc9-88b7-1263809b65cb",
  "type": "user",
  "uuid": "2a5114fa-7df7-4148-8e8b-5b3c1a5ac740",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to understand the feasibility of adding LIBERO benchmark tasks to a robot learning experiment that uses SmolVLA (450M parameter VLA model from HuggingFace/lerobot).\n\n1. Search for \"LIBERO benchmark robot manipulation SmolVLA\" and \"lerobot LIBERO dataset\"\n2. Search for \"SmolVLA LIBERO fine-tuning\" to see if anyone has done this\n3. Use WebFetch to check https://huggingface.co/datasets if LIBERO datasets are available in lerobot format\n4. Search for \"LIBERO demonstration dataset multimodal strategies operators\" - I need to know if LIBERO has the multi-operator structure needed (different demonstrators with different strategies) similar to RoboMimic MH\n\nKey questions:\n- Is LIBERO data readily available in lerobot/SmolVLA-compatible format?\n- Does LIBERO have multi-operator demonstrations with known quality labels? (This is critical - OT-Consensus needs demonstrations from multiple operators/strategies to test mode discovery)\n- How many demonstrations per task? How many tasks?\n- What would be the additional compute cost to add 1-2 LIBERO tasks?\n\nReport concisely with practical feasibility assessment.",
    "agentId": "a7f0f63bdf2589c2f",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have all the information needed to provide a comprehensive feasibility assessment.\n\n---\n\n## LIBERO + SmolVLA Feasibility Assessment for OT-Consensus Experiments\n\n### 1. Data Availability in LeRobot Format\n\n**Fully available and ready to use.** Multiple LIBERO datasets exist in LeRobot format on HuggingFace:\n\n- Official: `lerobot/libero_10_image`, `lerobot/libero_spatial_image`, `lerobot/libero_goal_image`, `lerobot/libero_object_image`\n- Community (cleaned, no-ops removed): `IPEC-COMMUNITY/libero_*_no_noops_1.0.0_lerobot`\n- Full 90-task suite: `jesbu1/libero_90_lerobot`\n- Official preprocessed: `HuggingFaceVLA/libero`\n\nThere is also a pretrained SmolVLA checkpoint specifically for LIBERO: `HuggingFaceVLA/smolvla_libero`. Training commands are documented in the [lerobot LIBERO docs](https://huggingface.co/docs/lerobot/en/libero). Integration is first-class -- `pip install -e \".[libero]\"` and you're running.\n\n### 2. CRITICAL BLOCKER: No Multi-Operator / Multi-Strategy Structure\n\n**LIBERO does NOT have the multi-operator demonstration structure that OT-Consensus requires.** This is the key finding:\n\n- LIBERO provides **50 demonstrations per task**, collected via SpaceMouse teleoperation at 20 Hz with automatic filtering and validation.\n- The paper and documentation **never specify multiple operators**. The data appears to be collected by a single team/operator with a consistent strategy, then filtered for quality.\n- There are **no quality labels** (no \"better\"/\"okay\"/\"worse\" operator tags).\n- There are **no strategy labels** or any explicit multi-modal behavior structure.\n\n**Contrast with RoboMimic MH**, which is explicitly designed for multi-operator research:\n- RoboMimic MH has **300 demonstrations from 6 operators** (2 \"better\", 2 \"okay\", 2 \"worse\"), each collecting 50 demos per task.\n- Demonstrations carry **explicit operator identity and proficiency labels**.\n- This is exactly the structure OT-Consensus needs for mode discovery across different demonstrator strategies.\n\nLIBERO's 50 demos per task are high-quality and relatively uniform -- the opposite of what you need to test mode discovery.\n\n### 3. Dataset Scale\n\n| Suite | Tasks | Demos/Task | Total Demos |\n|-------|-------|-----------|-------------|\n| LIBERO-Spatial | 10 | 50 | 500 |\n| LIBERO-Object | 10 | 50 | 500 |\n| LIBERO-Goal | 10 | 50 | 500 |\n| LIBERO-90 | 90 | 50 | 4,500 |\n| LIBERO-Long (libero_10) | 10 | 50 | 500 |\n| **Total** | **130** | | **6,500** |\n\nObservations: 7D action space (6D EEF delta + gripper), two camera views (workspace + wrist), 8D proprioceptive state.\n\n### 4. Compute Cost Estimate for 1-2 LIBERO Tasks\n\nBased on confirmed training configs and community reports:\n\n- **SmolVLA on LIBERO**: 100,000 steps, batch size 64\n- **Hardware**: 1x RTX 4090 (24GB) is sufficient; an L4 GPU (Google Colab) also works\n- **Training time**: ~4-12 hours per fine-tuning run on a single consumer GPU\n- **Fine-tuning from pretrained SmolVLA base**: Much cheaper -- one community report did 5,000 steps in ~4 hours on an L4\n- **For 1-2 tasks** (50-100 demonstrations): On the lower end, likely 4-6 hours on a single 4090\n\nThe compute cost to add 1-2 LIBERO tasks is minimal -- a few GPU-hours.\n\n### 5. Practical Feasibility Verdict\n\n**Technically trivial, scientifically inappropriate for OT-Consensus.**\n\n- Adding LIBERO tasks to a SmolVLA pipeline is straightforward. The datasets are ready, the training pipeline is documented, compute is cheap (single consumer GPU, a few hours).\n- **However, LIBERO data lacks the multi-operator/multi-strategy structure that is fundamental to OT-Consensus.** The 50 demos per task appear to come from a single operator or a uniform collection protocol with quality filtering. There are no operator labels, no quality labels, and no known multi-modal behavior in the demonstrations.\n- If you ran OT-Consensus on LIBERO data, you would likely find a single mode (or meaningless noise clusters), which would not validate the method's mode discovery capabilities.\n\n### Recommendation\n\nIf you want a simulation benchmark with multi-operator structure for OT-Consensus, **stick with RoboMimic MH** (which was designed for exactly this). If you want to add LIBERO for other reasons (e.g., testing SmolVLA policy quality, evaluating transfer, or benchmarking against published VLA numbers), it is cheap and easy to add. But it won't serve the multi-operator mode discovery purpose.\n\nAn alternative path: you could **synthetically create multi-strategy LIBERO data** by collecting your own demonstrations with deliberately different strategies (e.g., different grasp approaches, different waypoints), but this requires manual effort and defeats the purpose of using an existing benchmark.\n\nSources:\n- [LeRobot LIBERO Documentation](https://huggingface.co/docs/lerobot/en/libero)\n- [LIBERO Paper (NeurIPS 2023)](https://arxiv.org/abs/2306.03310)\n- [LIBERO GitHub](https://github.com/Lifelong-Robot-Learning/LIBERO)\n- [SmolVLA LIBERO Training Issue #3287](https://github.com/huggingface/lerobot/issues/3287)\n- [SmolVLA LIBERO Reproduction Issue #2354](https://github.com/huggingface/lerobot/issues/2354)\n- [Fine-Tuning SmolVLA Guide (Medium)](https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632)\n- [RoboMimic Multi-Human Dataset](https://robomimic.github.io/docs/datasets/robomimic_v0.1.html)\n- [HuggingFaceVLA/smolvla_libero Checkpoint](https://huggingface.co/HuggingFaceVLA/smolvla_libero)\n- [LIBERO Datasets on HuggingFace](https://huggingface.co/datasets?search=libero+lerobot)"
      }
    ],
    "totalDurationMs": 130571,
    "totalTokens": 23767,
    "totalToolUseCount": 15,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 443,
      "cache_read_input_tokens": 21624,
      "output_tokens": 1699,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 443
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1699,
          "cache_read_input_tokens": 21624,
          "cache_creation_input_tokens": 443,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 443,
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
  "sourceToolAssistantUUID": "c85b7f12-cdbc-46ba-8481-869f00e158fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-13T19:25:32.022Z_

<details><summary>↩ Tool result · `toolu_019oLkVGKtZHiLRHrSYEUzCX`</summary>

````text
I now have comprehensive information. Here is my consolidated report.

---

## Robometer: Practical Details for Research Proposal

### Paper Identity
- **Title:** "Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons"
- **Venue:** RSS 2026, arXiv 2603.02115
- **Authors:** Anthony Liang, Yigit Korkmaz, Jiahui Zhang, + 14 others (USC, UT Dallas, MIT, UW, NVIDIA)

---

### 1. Code/Model Weights: YES, Publicly Released

| Resource | URL |
|---|---|
| GitHub | https://github.com/robometer/robometer |
| Model weights (4B) | https://huggingface.co/robometer/Robometer-4B |
| OOD eval data | https://huggingface.co/datasets/robometer/rbm-1m-ood |
| RBM-1M full dataset | Listed as "Coming Soon" on project page |
| Project page | https://robometer.github.io/ |
| Interactive demo | https://robometer-rewardeval-ui.hf.space |

Installation is straightforward: `git clone` + `uv sync`. Two model variants are available: **Robometer-4B** (general-purpose) and **Robometer-LIBERO** (fine-tuned for LIBERO-90).

---

### 2. Architecture

- **Backbone:** Qwen3-VL-4B-Instruct (confirmed on HuggingFace model card)
- **Size:** 4B parameters, BF16 precision. An 8B variant was evaluated as a baseline but the released model is 4B.
- **Type:** Causal VLM with learnable progress/success/preference tokens inserted into the sequence.

---

### 3. Inputs and Outputs

**Inputs:**
- **Video:** MP4 file, NumPy array (T,H,W,C), or .npz. Shortest edge resized to 240px, aspect ratio preserved. Up to 32 frames per trajectory (downsampled). Default extraction at 3 fps (configurable via `--fps`).
- **Language instruction:** Text string describing the task.

**Outputs (three heads):**
- **Per-frame progress:** Continuous scalar in [0,1] via categorical distribution over N bins (C51-style). This is the dense reward signal.
- **Per-frame success:** Binary probability at each timestep.
- **Trajectory preference:** Binary classification indicating which of two trajectories is better (requires two videos as input).

**Key point:** It CAN score individual trajectories independently (absolute progress + success prediction). It does NOT require paired comparisons at inference time. Paired comparison is an additional capability.

---

### 4. Scoring RoboMimic MH Demos

**Format:** RoboMimic stores demos as HDF5 with image observations as NumPy arrays. Robometer accepts `.npy` arrays with shape `(T, H, W, C)` in uint8, so you would extract the `agentview_image` observations from each demo and pass them directly. No video encoding needed.

**Example inference:**
```python
from transformers import AutoProcessor, RFM
processor = AutoProcessor.from_pretrained("robometer/Robometer-4B")
model = RFM.from_pretrained("robometer/Robometer-4B")
```
Or via CLI:
```bash
uv run python scripts/example_inference_local.py \
  --model-path robometer/Robometer-4B \
  --video /path/to/video.mp4 \
  --task "pick up the can"
```

**Estimated time for 300 MH demos on a single A100:** The paper provides no explicit throughput numbers. However, a 4B VLM processing ~32 frames per trajectory on an A100 (80GB) should run at roughly 1-3 seconds per trajectory for a forward pass (based on comparable Qwen2/3-VL-4B inference benchmarks). For 300 demos, expect approximately **5-15 minutes total** on a single A100. This is a rough estimate -- actual time depends on trajectory length and frame sampling rate.

**VRAM:** Not documented, but Qwen3-VL-4B in BF16 requires ~8-10GB for weights alone. With 32 frames of video context, expect ~16-24GB VRAM. Comfortably fits on an A100-40GB or A100-80GB.

---

### 5. Mode-Awareness vs. Single Score

Robometer provides **three separate output signals**, not a single global score:
1. Dense per-frame **progress** (main reward signal, continuous scalar)
2. Per-frame **success** probability (binary)
3. Pairwise **preference** (when comparing two trajectories)

However, it is **NOT mode-aware** in the sense of separate quality dimensions (e.g., fluency, safety, precision). The progress score is a single scalar capturing task completion progress. It does not decompose quality into multiple factors.

---

### 6. Benchmarks and Evaluation

**Training data (RBM-1M):** 1,059,370 trajectories across 21 robot embodiments, drawn from Open-X Embodiment, AGIBot World, Galaxea, LIBERO, MetaWorld, RH-20T, Epic-Kitchens, FAILSafe, RACER, SOAR, and others.

**Evaluation benchmarks:**
- **RBM-EVAL-ID:** 32,767 in-distribution trajectories
- **RBM-EVAL-OOD:** 976 out-of-distribution trajectories from 3 institutions
- **RoboRewardBench** (external benchmark)
- **Downstream tasks:** Online RL (DSRL), Offline RL (IQL), Model-based RL (DreamZero), failure detection (7 tasks, 7 robots), data retrieval + imitation learning
- **Real-robot evaluations:** USC Franka, Koch Arms, Trossen, xArm, MIT Franka, UTD SO-101
- **Per-dataset eval:** BC-Z, Berkeley Cable Routing, Bridge V2, Jaco Play, Toto, Viola, MetaWorld, LIBERO-90

**RoboMimic was NOT one of the evaluation benchmarks.** There is no mention of RoboMimic or MimicGen anywhere in the paper, project page, or GitHub repo. However, since Robometer accepts arbitrary video+language input in a zero-shot manner, it should generalize to RoboMimic tasks (tabletop manipulation is well within distribution given training on similar domains like LIBERO and MetaWorld).

---

### 7. Key Downstream Results

| Application | Improvement |
|---|---|
| Online RL (single-stage) | 20% -> 85% success |
| Online RL (multi-stage) | 20% -> 70% success (2.5x over RoboReward) |
| Offline RL (IQL) | 2.4x average success improvement |
| Data filtering for IL | 4.5x higher success vs. best baseline |
| Failure detection | 0.81 avg F1 (best among all methods) |

---

### Practical Summary for Your Proposal

Robometer is a strong baseline choice. It is fully open (code + 4B weights on HuggingFace), takes raw video + language instruction as input, and produces dense per-frame reward scores that can be used for trajectory filtering without any task-specific training. Scoring 300 RoboMimic MH demos on a single A100 should take on the order of 5-15 minutes. The main caveat is that RoboMimic was not in its training or evaluation set, so you would be using it zero-shot -- but the model was trained on similar tabletop manipulation domains (LIBERO, MetaWorld, Bridge V2) and is designed for cross-embodiment generalization. Fine-tuning on your specific domain is also supported via LoRA (`model.use_peft=true`).

Sources:
- [arXiv paper](https://arxiv.org/abs/2603.02115)
- [Full HTML paper](https://arxiv.org/html/2603.02115v1)
- [Project page](https://robometer.github.io/)
- [GitHub repository](https://github.com/robometer/robometer)
- [HuggingFace model weights](https://huggingface.co/robometer/Robometer-4B)
- [Interactive demo](https://robometer-rewardeval-ui.hf.space)

agentId: a19c0e1dbe7cfc9b4 (use SendMessage with to: 'a19c0e1dbe7cfc9b4' to continue this agent)
&lt;usage>total_tokens: 21832
tool_uses: 11
duration_ms: 141385&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "9920b2cf-48f8-41d0-97b5-dc4254567914",
  "isSidechain": false,
  "promptId": "bbda98e0-f6b9-4cc9-88b7-1263809b65cb",
  "type": "user",
  "uuid": "f34c8570-ece5-4014-b564-a9ed16b29c73",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to understand Robometer (RSS 2026, arXiv 2603.02115) in detail for a research proposal revision. Specifically:\n\n1. Search for \"Robometer scaling general-purpose robotic reward models trajectory comparisons\" and find the paper.\n2. Use WebFetch to read the actual paper (try https://arxiv.org/abs/2603.02115).\n3. I need to know:\n   - Is code/model weights publicly released? Search GitHub for \"robometer\" or check the paper for a code link.\n   - What model architecture (Qwen3-VL-4B)? What inputs does it take?\n   - Can it score individual trajectories on RoboMimic? What format does it expect?\n   - How long would it take to score 300 RoboMimic MH demos on a single A100?\n   - Is it mode-aware or does it give a single global quality score?\n   - What benchmarks was it evaluated on? Was RoboMimic one of them?\n\n4. Also search for \"Robometer github code release\" to verify availability.\n\nReport your findings concisely - focus on practical details about using Robometer as a baseline.",
    "agentId": "a19c0e1dbe7cfc9b4",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive information. Here is my consolidated report.\n\n---\n\n## Robometer: Practical Details for Research Proposal\n\n### Paper Identity\n- **Title:** \"Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons\"\n- **Venue:** RSS 2026, arXiv 2603.02115\n- **Authors:** Anthony Liang, Yigit Korkmaz, Jiahui Zhang, + 14 others (USC, UT Dallas, MIT, UW, NVIDIA)\n\n---\n\n### 1. Code/Model Weights: YES, Publicly Released\n\n| Resource | URL |\n|---|---|\n| GitHub | https://github.com/robometer/robometer |\n| Model weights (4B) | https://huggingface.co/robometer/Robometer-4B |\n| OOD eval data | https://huggingface.co/datasets/robometer/rbm-1m-ood |\n| RBM-1M full dataset | Listed as \"Coming Soon\" on project page |\n| Project page | https://robometer.github.io/ |\n| Interactive demo | https://robometer-rewardeval-ui.hf.space |\n\nInstallation is straightforward: `git clone` + `uv sync`. Two model variants are available: **Robometer-4B** (general-purpose) and **Robometer-LIBERO** (fine-tuned for LIBERO-90).\n\n---\n\n### 2. Architecture\n\n- **Backbone:** Qwen3-VL-4B-Instruct (confirmed on HuggingFace model card)\n- **Size:** 4B parameters, BF16 precision. An 8B variant was evaluated as a baseline but the released model is 4B.\n- **Type:** Causal VLM with learnable progress/success/preference tokens inserted into the sequence.\n\n---\n\n### 3. Inputs and Outputs\n\n**Inputs:**\n- **Video:** MP4 file, NumPy array (T,H,W,C), or .npz. Shortest edge resized to 240px, aspect ratio preserved. Up to 32 frames per trajectory (downsampled). Default extraction at 3 fps (configurable via `--fps`).\n- **Language instruction:** Text string describing the task.\n\n**Outputs (three heads):**\n- **Per-frame progress:** Continuous scalar in [0,1] via categorical distribution over N bins (C51-style). This is the dense reward signal.\n- **Per-frame success:** Binary probability at each timestep.\n- **Trajectory preference:** Binary classification indicating which of two trajectories is better (requires two videos as input).\n\n**Key point:** It CAN score individual trajectories independently (absolute progress + success prediction). It does NOT require paired comparisons at inference time. Paired comparison is an additional capability.\n\n---\n\n### 4. Scoring RoboMimic MH Demos\n\n**Format:** RoboMimic stores demos as HDF5 with image observations as NumPy arrays. Robometer accepts `.npy` arrays with shape `(T, H, W, C)` in uint8, so you would extract the `agentview_image` observations from each demo and pass them directly. No video encoding needed.\n\n**Example inference:**\n```python\nfrom transformers import AutoProcessor, RFM\nprocessor = AutoProcessor.from_pretrained(\"robometer/Robometer-4B\")\nmodel = RFM.from_pretrained(\"robometer/Robometer-4B\")\n```\nOr via CLI:\n```bash\nuv run python scripts/example_inference_local.py \\\n  --model-path robometer/Robometer-4B \\\n  --video /path/to/video.mp4 \\\n  --task \"pick up the can\"\n```\n\n**Estimated time for 300 MH demos on a single A100:** The paper provides no explicit throughput numbers. However, a 4B VLM processing ~32 frames per trajectory on an A100 (80GB) should run at roughly 1-3 seconds per trajectory for a forward pass (based on comparable Qwen2/3-VL-4B inference benchmarks). For 300 demos, expect approximately **5-15 minutes total** on a single A100. This is a rough estimate -- actual time depends on trajectory length and frame sampling rate.\n\n**VRAM:** Not documented, but Qwen3-VL-4B in BF16 requires ~8-10GB for weights alone. With 32 frames of video context, expect ~16-24GB VRAM. Comfortably fits on an A100-40GB or A100-80GB.\n\n---\n\n### 5. Mode-Awareness vs. Single Score\n\nRobometer provides **three separate output signals**, not a single global score:\n1. Dense per-frame **progress** (main reward signal, continuous scalar)\n2. Per-frame **success** probability (binary)\n3. Pairwise **preference** (when comparing two trajectories)\n\nHowever, it is **NOT mode-aware** in the sense of separate quality dimensions (e.g., fluency, safety, precision). The progress score is a single scalar capturing task completion progress. It does not decompose quality into multiple factors.\n\n---\n\n### 6. Benchmarks and Evaluation\n\n**Training data (RBM-1M):** 1,059,370 trajectories across 21 robot embodiments, drawn from Open-X Embodiment, AGIBot World, Galaxea, LIBERO, MetaWorld, RH-20T, Epic-Kitchens, FAILSafe, RACER, SOAR, and others.\n\n**Evaluation benchmarks:**\n- **RBM-EVAL-ID:** 32,767 in-distribution trajectories\n- **RBM-EVAL-OOD:** 976 out-of-distribution trajectories from 3 institutions\n- **RoboRewardBench** (external benchmark)\n- **Downstream tasks:** Online RL (DSRL), Offline RL (IQL), Model-based RL (DreamZero), failure detection (7 tasks, 7 robots), data retrieval + imitation learning\n- **Real-robot evaluations:** USC Franka, Koch Arms, Trossen, xArm, MIT Franka, UTD SO-101\n- **Per-dataset eval:** BC-Z, Berkeley Cable Routing, Bridge V2, Jaco Play, Toto, Viola, MetaWorld, LIBERO-90\n\n**RoboMimic was NOT one of the evaluation benchmarks.** There is no mention of RoboMimic or MimicGen anywhere in the paper, project page, or GitHub repo. However, since Robometer accepts arbitrary video+language input in a zero-shot manner, it should generalize to RoboMimic tasks (tabletop manipulation is well within distribution given training on similar domains like LIBERO and MetaWorld).\n\n---\n\n### 7. Key Downstream Results\n\n| Application | Improvement |\n|---|---|\n| Online RL (single-stage) | 20% -> 85% success |\n| Online RL (multi-stage) | 20% -> 70% success (2.5x over RoboReward) |\n| Offline RL (IQL) | 2.4x average success improvement |\n| Data filtering for IL | 4.5x higher success vs. best baseline |\n| Failure detection | 0.81 avg F1 (best among all methods) |\n\n---\n\n### Practical Summary for Your Proposal\n\nRobometer is a strong baseline choice. It is fully open (code + 4B weights on HuggingFace), takes raw video + language instruction as input, and produces dense per-frame reward scores that can be used for trajectory filtering without any task-specific training. Scoring 300 RoboMimic MH demos on a single A100 should take on the order of 5-15 minutes. The main caveat is that RoboMimic was not in its training or evaluation set, so you would be using it zero-shot -- but the model was trained on similar tabletop manipulation domains (LIBERO, MetaWorld, Bridge V2) and is designed for cross-embodiment generalization. Fine-tuning on your specific domain is also supported via LoRA (`model.use_peft=true`).\n\nSources:\n- [arXiv paper](https://arxiv.org/abs/2603.02115)\n- [Full HTML paper](https://arxiv.org/html/2603.02115v1)\n- [Project page](https://robometer.github.io/)\n- [GitHub repository](https://github.com/robometer/robometer)\n- [HuggingFace model weights](https://huggingface.co/robometer/Robometer-4B)\n- [Interactive demo](https://robometer-rewardeval-ui.hf.space)"
      }
    ],
    "totalDurationMs": 141385,
    "totalTokens": 21832,
    "totalToolUseCount": 11,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1151,
      "cache_read_input_tokens": 18584,
      "output_tokens": 2096,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1151
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2096,
          "cache_read_input_tokens": 18584,
          "cache_creation_input_tokens": 1151,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1151,
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
      "otherToolCount": 11
    }
  },
  "sourceToolAssistantUUID": "9920b2cf-48f8-41d0-97b5-dc4254567914",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Assistant

_source line 18 · 2026-05-13T19:26:16.017Z_

<details><summary>Logged reasoning block</summary>

```text
Excellent research results. Let me now synthesize what I've learned:

**Key findings:**

1. **Robometer**: Code and weights are publicly available (GitHub + HuggingFace). It can score individual trajectories on RoboMimic in ~5-15 minutes for 300 demos. It was NOT evaluated on RoboMimic, but should work zero-shot. This is absolutely doable for Tier A (correlation comparison only) and Tier B (downstream).

2. **LIBERO**: Technically trivial to add, BUT it lacks multi-operator structure. 

LIBERO only has ~50 demos per task from a single operator with no quality labels, so it can't actually test OT-Consensus's mode discovery capabilities—the reviewer's suggestion is well-intentioned but misses the scientific requirements of the method.

3. **PER analogy**: The structural parallel is sound—PER up-weights deviations while OT-Consensus down-weights them, which is an interesting inversion. Distributional RL's Wasserstein contraction provides theoretical grounding, and SWAD already applies sliced Wasserstein distance to barycenter for anomaly detection in general ML contexts.

For the revision scope, I'm treating this as a minor revision with three concrete changes. First, I'll add Robometer evaluation on the 300 RoboMimic MH demos to compute Spearman correlation with operator proficiency—this takes 5-15 minutes on an A100 with no downstream training needed, and optionally I can include it as an additional condition in the SmolVLA comparison. Second, I'm rejecting LIBERO not out of stubbornness but because it lacks the multi-operator structure this work requires, so instead I'll explain why RoboMimic MH is the canonical benchmark for this specific problem and propose MetaWorld as an alternative response to benchmark narrowness concerns.

Actually, the cleaner approach is to acknowledge the narrowness concern directly by adding LIBERO as a Tier B "graceful degradation" test—showing that OT-Consensus correctly identifies single-mode data without over-clustering—and then note that RoboMimic MH is the only widely-used benchmark with multi-operator structure, which reframes the limitation as a feature rather than a weakness. Third, I need to develop the PER analogy properly in the framing section using the structural parallel and polarity inversion.

I'm also thinking through the stagnation concern with the current 3/5 novelty and 3/5 impact scores. The reviewer wants at least one LIBERO task in Tier B to show the method generalizes beyond RoboMimic's multi-operator structure. I'm weighing three options: adding LIBERO as a single-mode generalization test, finding a different multi-operator benchmark, or accepting the benchmark limitation. The strongest path is option (a)—LIBERO would demonstrate that OT-Consensus's quality scoring works even without mode discovery—but I'm realizing the filtered, single-operator LIBERO demos might not have enough quality variation to make this meaningful. The most honest approach is to acknowledge LIBERO's structural limitations upfront while still including it strategically.

I'll add LIBERO to Tier B as a downstream policy comparison: does curation via OT-Consensus with k=1 improve SmolVLA performance compared to random sampling? This tests whether the distance-from-barycenter scoring helps even without mode discovery, and since DATA-FM showed 30% random sampling matches full-dataset performance on LIBERO, there's real redundancy to exploit here. Now I need to revise the JSON carefully to address the Robometer addition, LIBERO framing, PER analogy development, and score ceiling acknowledgment.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f34c8570-ece5-4014-b564-a9ed16b29c73",
  "isSidechain": false,
  "requestId": "req_011Cb17i1nTczXb7yh4mAKJT",
  "type": "assistant",
  "uuid": "ad3be4e2-0796-4eba-a876-c1b2a5a56a63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MpWuycXk2ozuqaayYSCYk8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4379,
      "cache_creation_input_tokens": 3944,
      "cache_read_input_tokens": 31570,
      "output_tokens": 11057,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3944,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4379,
          "output_tokens": 11057,
          "cache_read_input_tokens": 31570,
          "cache_creation_input_tokens": 3944,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3944
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

### Assistant

_source line 19 · 2026-05-13T19:26:17.075Z_

Good research results. Key findings:

1. **Robometer**: Code + weights publicly available, scoring 300 demos takes ~15 min on A100. Never evaluated on RoboMimic — easy to add.
2. **LIBERO**: Technically trivial to integrate, BUT it lacks multi-operator structure (single operator, ~50 demos/task, no quality labels). Cannot test mode discovery. Need a different strategy to address benchmark narrowness.
3. **PER analogy**: Technically sound with a clean "polarity inversion" structure. Distributional RL's Wasserstein contraction provides grounding.

Now I'll produce the revised idea — a minor revision adding Robometer to evaluation, reframing LIBERO appropriately, and developing the PER analogy.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad3be4e2-0796-4eba-a876-c1b2a5a56a63",
  "isSidechain": false,
  "requestId": "req_011Cb17i1nTczXb7yh4mAKJT",
  "type": "assistant",
  "uuid": "e6dfdb45-fe5d-40f1-bbb2-e282d09b39e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MpWuycXk2ozuqaayYSCYk8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4379,
      "cache_creation_input_tokens": 3944,
      "cache_read_input_tokens": 31570,
      "output_tokens": 11057,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3944,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4379,
          "output_tokens": 11057,
          "cache_read_input_tokens": 31570,
          "cache_creation_input_tokens": 3944,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3944
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

### Tool call

_source line 20 · 2026-05-13T19:30:17.807Z_

<details open><summary>🔧 Tool call — Write · `toolu_01A5tUhDYExgMSYUdo16J5Yg`</summary>

```json
{
  "file_path": "/tmp/revised_idea_round9.json",
  "content": "{\n  \"change_type\": \"minor\",\n  \"title\": \"Mode-Aware Quality Scoring for Demonstration Curation via Sliced Wasserstein Consensus\",\n  \"core_problem\": \"How should we curate multimodal demonstration datasets that contain multiple valid strategies of varying quality? Diversity-maximizing approaches (FAKTUAL) improve average performance but explicitly fail when demonstrations contain conflicting strategies — blindly including diverse-but-poor demonstrations degrades learning. Quality-scoring approaches (CUPID, DataMIL) work well but require expensive policy training, validation rollouts, or influence function estimation. Learned reward models (Robometer) can score trajectory quality without a task-specific policy but require 1M+ training trajectories and are not mode-aware. Recent evidence from 'Is Diversity All You Need?' (Modi Shi et al., arXiv Jul 2025) sharpens this problem: they show that expert diversity creates *velocity multimodality* — different demonstrators executing the same spatial trajectory at different speeds — that directly degrades policy learning, producing 15% performance losses that their velocity normalization method recovers. This confirms that multi-operator demonstrations create distributional conflicts that harm learning, but their fix (velocity normalization) only addresses speed variation along shared paths, not the broader problem of scoring quality across genuinely different strategy modes. Conceptually, the challenge mirrors Prioritized Experience Replay (PER; Schaul et al., 2016) but with inverted polarity: PER uses TD-error magnitude to *up-weight* transitions that deviate from the agent's current value estimate (deviation = informative, learn more from it), while demonstration curation requires *down-weighting* trajectories that deviate from the demonstrator consensus (deviation = suspicious, filter it out). Both share the core mechanism of scoring samples by their distance from an expected distribution, but serve opposite objectives — prioritization vs. filtration. This RL-inspired framing suggests that what demonstration curation needs is a *distributional priority score* analogous to TD-error: one that measures each trajectory's deviation from expected behavior, but in a mode-aware manner that distinguishes between valid strategy diversity and genuine quality degradation. Distributional RL theory (Bellemare et al., 2017) grounds this connection formally: the distributional Bellman operator is a contraction in the p-Wasserstein metric, establishing Wasserstein distances as the natural metric family for distributional deviation in sequential decision-making. The field lacks a training-free quality scoring method that is *mode-aware* — one that discovers distinct strategy modes in the data and scores quality within each mode using distributional deviation, rather than treating all demonstrations as drawn from a single distribution.\",\n  \"opportunity\": \"The demonstration curation landscape has crystallized into five camps: (1) *policy-dependent quality methods* (CUPID, DataMIL, Demo-SCORE, QoQ) that achieve SOTA but require trained policies or validation rollouts; (2) *policy-free learned quality methods* (Robometer) that train general-purpose reward models on massive trajectory datasets to score quality without a task-specific policy, but require 1M+ training trajectories for pre-training and are not mode-aware — they assign a global quality score without distinguishing between multiple valid strategies. Robometer achieves strong absolute success rates on retrieval tasks (e.g., ~95% on Stir Pot where baselines score near 0%), though the reported 4.5× average improvement is inflated by near-zero baseline performance on several tasks rather than reflecting a uniform 4.5× gain; (3) *policy-free quality proxies* (DemInf, RINSE, SCIZOR) that use scalar metrics (MI, smoothness, progress) but collapse distributional structure and are mode-agnostic; (4) *policy-free diversity methods* (FAKTUAL) that maximize trajectory entropy but explicitly acknowledge 'promoting diversity may actually be harmful when the model is not capable of capturing multimodality in the data'; and (5) *distribution normalization methods* ('Is Diversity All You Need?', Modi Shi et al., arXiv Jul 2025) that identify velocity multimodality from expert diversity as a concrete failure mode and propose velocity distribution debiasing — training a velocity model to normalize action chunk speeds, recovering 15% performance (equivalent to 2.5× pre-training data). This reveals a fundamental tension: diversity-based curation fails precisely when demonstrations are multimodal, distribution normalization removes one source of multimodality but does not score quality, learned scorers (Robometer) are powerful but mode-agnostic and require massive pre-training data, and scalar proxies collapse distributional structure. The PER analogy illuminates the gap: RL already solved the 'which samples matter?' problem for experience replay via TD-error (a *distributional deviation score*), but demonstration curation has no analogous mechanism that is both mode-aware and training-free. Recent evidence further motivates intelligent curation: 'On Data Redundancy in VLA Training' (DATA-FM @ ICLR 2026) shows that random 30% sampling of LIBERO matches full-dataset SmolVLA performance, revealing massive data redundancy — but their difficulty-based Temporal Surprise Score underperformed random selection, suggesting that naive quality proxies can be counterproductive. The key gap: no existing training-free method provides *mode-aware distributional priority scoring* — discovering strategy modes and assessing quality relative to mode-specific consensus via distributional deviation. Optimal transport geometry fills this gap naturally: Sliced Wasserstein distances define a metric space over trajectory distributions that captures shape, spread, and temporal structure; clustering in this space discovers strategy modes; and distance from each mode's robust barycenter provides a geometrically grounded, mode-aware quality score — the demonstration-curation analogue of PER's TD-error, operating in the same Wasserstein metric family that governs distributional RL convergence.\",\n  \"landscape\": \"**Policy-dependent quality methods**: CUPID (CoRL 2025) uses influence functions estimating each demonstration's causal impact on closed-loop policy return, achieving SOTA on RoboMimic with <33% of curated data; requires a trained policy and evaluation rollouts. DataMIL (ICLR 2026) uses the datamodels paradigm for end-to-end policy-driven selection validated on 60+ tasks including OXE; requires surrogate loss computation with policy training. Demo-SCORE (RSS 2025) trains classifiers on online rollout success/failure to self-curate, achieving 15-35% gains; requires online robot interaction. QoQ (arXiv Mar 2026) uses influence functions with theoretical analysis but requires a validation set and scales O(n²). **Policy-free learned quality methods**: Robometer (RSS 2026, arXiv 2603.02115) trains a general-purpose VLM-based reward model (Qwen3-VL-4B) on RBM-1M (1M+ trajectories across 21 embodiments) using a dual objective of frame-level progress supervision and trajectory-level preference learning. Achieves strong absolute success rates on retrieval tasks (e.g., ~95% on Stir Pot where baselines score near 0%), though the reported 4.5× average improvement is inflated by near-zero baseline performance on several tasks rather than reflecting a uniform 4.5× gain. However, Robometer (a) requires 1M+ training trajectories (~6TB) for pre-training — infeasible when curating smaller datasets without pre-existing large-scale data; (b) is NOT mode-aware — it assigns a single global quality score per trajectory without distinguishing between multiple valid strategies; (c) was not evaluated on RoboMimic or against demonstration curation methods (CUPID, DemInf, RINSE, SCIZOR, FAKTUAL) — its comparisons are against VLM reward models (RoboReward, GVL, VLAC). Robometer code and model weights (Robometer-4B) are publicly released on GitHub and HuggingFace, enabling direct comparison. OT-Consensus is complementary: training-free, mode-aware, and geometric, requiring no pre-training data. **Policy-free quality proxies**: DemInf (RSS 2025) estimates trajectory-level mutual information between states and actions via k-NN estimators with VAE embeddings, achieving 5-10% gains on RoboMimic; captures information content but collapses distributional structure to a scalar and is mode-agnostic. RINSE (ICML 2025, arXiv 2604.23000) uses Spectral Arc Length (SAL) and Trajectory-Envelope Distance (TED) smoothness metrics achieving 16-20% success gains; assumes smoothness universally correlates with quality, failing for tasks where jerky motions are correct. SCIZOR (ICRA 2026) combines self-supervised task progress prediction with deduplication, achieving 15.4% average improvement across RoboMimic/OXE/Sirius-Fleet; no theoretical guarantees and conflates lack of progress with low quality. S2I (ICRA 2025) performs segment-level selection using contrastive learning with 3 expert reference demonstrations; requires expert references and cannot operate fully unsupervised. Consistency Matters (ACM THRI 2025) proposes 10 motion-based consistency metrics with 76-91% success prediction accuracy; limited to geometric consistency without distributional analysis. **Policy-free diversity methods**: FAKTUAL (arXiv Mar 2026, 2603.11634) uses signature kernel entropy for diversity-based curation; fully model-free and tested on RoboMimic MH and MetaWorld. Compared against CUPID, DemInf, and Demo-SCORE. FAKTUAL performs modestly above random but below quality-based methods, and *explicitly acknowledges* that 'promoting diversity may actually be harmful when the model is not capable of capturing multimodality in the data.' NOTE: As of May 2026, FAKTUAL code is not publicly released; FPS fallback available. **Distribution normalization methods**: 'Is Diversity All You Need for Scalable Robotic Manipulation?' (Modi Shi et al., arXiv Jul 2025, 2507.06219) identifies velocity multimodality from expert diversity as a concrete failure mode and proposes velocity distribution debiasing, yielding 15% gains. Validates the core premise that multi-operator demonstrations create distributional conflicts, but addresses only velocity variation along shared paths. **RL-inspired scoring connections**: Prioritized Experience Replay (PER; Schaul et al., ICLR 2016) established TD-error magnitude as a distributional deviation score for sample prioritization. OTR (ICLR 2023) uses OT to score offline trajectories by alignment to expert demonstrations. SWAD (Pallage & Lesage-Landry, arXiv Apr 2025, 2504.12918) uses sliced-Wasserstein distance to barycenters for unsupervised anomaly detection on tabular data — the closest methodological precursor, but on i.i.d. data points rather than trajectory measures. Distributional RL theory (Bellemare et al., 2017) proved Wasserstein contraction of the distributional Bellman operator, establishing OT as the natural metric family for distributional analysis in sequential decision-making. **OT-based quality/distance methods (adjacent)**: sWk-means (Luan & Hamp, DSFE 2025) uses sliced Wasserstein distances + k-means clustering for financial regime detection — a methodological precursor to OT-Consensus's first two steps, but without barycenters, quality scoring, or trajectory representations. BWD/'Expert or not?' (arXiv Oct 2025) introduces Bellman Wasserstein Distance requiring a behavioral critic. LWAIL (ICLR 2026) uses Wasserstein for state-only distribution matching in adversarial IL policy learning. **Data redundancy in VLA training**: 'On Data Redundancy in VLA Training' (DATA-FM Workshop @ ICLR 2026) shows that random 30% sampling of LIBERO matches full-dataset SmolVLA performance with Temporal Surprise Score underperforming random selection. **OT in robot learning (not curation)**: OTR (ICLR 2023), Temporal OT Reward (NeurIPS 2024), GWIL (ICLR 2022), ROT (NeurIPS 2022). **OT theory**: Robust Wasserstein Barycenter (arXiv Mar 2026) proves existence/consistency. Outlier-Robust OT (Nietert et al., AISTATS 2022). k-Sparse Wasserstein Barycenter with Outliers (IJCAI 2024). s-OTDD (ICML 2025). **Gap**: No existing method provides training-free, mode-aware distributional priority scoring for demonstration quality. FAKTUAL is mode-agnostic diversity; DemInf/RINSE/SCIZOR are mode-agnostic scalar proxies; Robometer is a powerful learned scorer but not mode-aware and requires 1M+ trajectories; CUPID/DataMIL are mode-aware in principle but policy-dependent; sWk-means stops at regime identification; SWAD uses SW-to-barycenter but on i.i.d. points, not trajectory measures; velocity debiasing normalizes speed but does not score quality. OT-Consensus uniquely combines mode awareness, distributional priority scoring, and training-free operation.\",\n  \"approach\": \"**Overview**: OT-Consensus is a training-free, mode-aware demonstration quality scoring method. We reframe the demonstration curation problem through the lens of RL-inspired distributional priority scoring: just as PER (Schaul et al., 2016) scores replay transitions by TD-error magnitude — their deviation from the agent's value estimate — OT-Consensus scores demonstrations by their Sliced Wasserstein distance from the mode-specific barycenter — their distributional deviation from demonstrator consensus. The polarity is inverted: PER up-weights high-deviation samples (surprise = informative), while OT-Consensus down-weights high-deviation demonstrations (deviation = suspicious quality). Both operate via the same mechanism — measuring distributional deviation to score sample utility — grounded in the Wasserstein metric family that governs distributional RL convergence (Bellemare et al., 2017). The core conceptual contribution is that demonstration quality should be assessed as *distributional priority within each strategy mode*, not as global diversity or scalar proxy. This extends the SW+clustering pipeline introduced by sWk-means (Luan & Hamp, DSFE 2025) from financial regime detection to robot demonstration curation, with three key additions: robust barycenters for quality scoring, trajectory-as-measure representation, and mode-aware filtering. We target a focused empirical contribution for CoRL 2026 with formal theoretical analysis deferred.\\n\\n**Day 1 Validation Gate (May 13 — before committing to the full sprint)**: We run two preliminary experiments to validate the core hypothesis that SW2 geometry can distinguish strategy modes from quality variation, requiring ~4h total compute. (a) *Synthetic toy experiment*: Generate 200 2D trajectories from 2 strategy modes (left-reach vs right-reach) with 3 quality tiers per mode: clean, noisy, and corrupted. Compute the 200×200 SW2 pairwise distance matrix using L=100 random projections. Run k-medoid clustering with k=2 and k=6. Verify: (i) k=2 recovers the two strategy modes (ARI ≥ 0.8); (ii) within each mode cluster, SW2 distance to the mode's barycenter correlates with quality tier (Spearman ρ ≥ 0.5). Simultaneously compute MI-based and smoothness scores to show scalar metrics fail to distinguish within-mode quality. (b) *RoboMimic pilot*: Randomly sample 50 trajectories from RoboMimic MH Can task. Compute the 50×50 SW2 pairwise distance matrix using SigLIP-SO400M embeddings. Run k-medoid clustering with k=3 and k=6. Compute ARI against operator identity and proficiency labels. (c) *Gate criterion*: Proceed only if synthetic ARI ≥ 0.8 AND ρ ≥ 0.5, AND RoboMimic pilot ARI ≥ 0.1 for at least one k and label combination.\\n\\n**FAKTUAL Reproduction Plan**: FAKTUAL code is not publicly released as of May 2026. Mitigation: (1) May 13 — contact authors. (2) May 14-15 — if code received, integrate; otherwise begin reimplementation using KSig library. (3) May 16 decision point — if incomplete, switch to Farthest-Point Sampling (FPS) in SigLIP embedding space as diversity baseline.\\n\\n**Representation design**: Each demonstration trajectory τ = {(o_t, a_t, t/T)}_{t=1}^{T} is mapped to a discrete probability measure μ_τ over an embedding space. Visual observations o_t are encoded via a frozen pre-trained visual encoder into d-dimensional features; actions a_t remain in raw action space (typically 7D); normalized timestep t/T provides temporal grounding. The ground metric is a weighted sum: c((v₁,a₁,t₁), (v₂,a₂,t₂)) = λ_v‖v₁−v₂‖² + λ_a‖a₁−a₂‖² + λ_t|t₁−t₂|², with λ weights selected via validation on a held-out task. **Encoder choice and transparency**: Default encoder is SigLIP-SO400M — SmolVLA's own vision encoder, so quality is scored in the policy-relevant representation space. DINOv2 ablation proves generalization beyond encoder-policy overlap.\\n\\n**Scalable pairwise distances**: SW2 distances with O(Ln log n) per pair. For RoboMimic (300 demos), the N² pairwise matrix takes ~15 min on a single A100.\\n\\n**Mode discovery and quality scoring**: (1) Compute SW2 pairwise distance matrix. (2) k-medoid clustering (PAM) to discover strategy modes; k via silhouette analysis over k ∈ {2,...,8}. (3) Within each cluster, compute robust barycenter using trimmed-mean OT (ε=0.1). (4) Score each trajectory: q_i = 1 / (1 + SW2(μ_i, β_m)), normalized to [0,1]. This is the *distributional priority score* — the demonstration-curation analogue of PER's TD-error, measuring deviation from mode-specific consensus.\\n\\n**Relationship to PER and distributional RL**: The SW2-to-barycenter score has a precise structural analogy to TD-error priority: both measure sample deviation from a distributional reference (value estimate for PER; mode barycenter for OT-Consensus). The polarity inversion (PER: high deviation → up-weight; OT-Consensus: high deviation → down-weight) reflects the difference between learning from surprise (RL) and filtering for consensus (curation). Formally, distributional RL's Wasserstein contraction (Bellemare et al., 2017) established that the p-Wasserstein metric governs convergence of return distributions under the Bellman operator. OT-Consensus imports the same metric family into demonstration curation, using Wasserstein distances to measure trajectory quality rather than value distribution convergence. This connection is not merely analogical: OTR (Luo et al., ICLR 2023) already uses OT to assign reward scores to offline trajectories, and SWAD (Pallage & Lesage-Landry, 2025) uses SW-distance-to-barycenter for anomaly detection in general data selection. OT-Consensus extends these ideas with mode-aware clustering and trajectory-as-measure representations.\\n\\n**Mode discovery analysis**: Expected k=3 (proficiency levels) or k=6 (individual operators). With N=300 and k ∈ {3,6}, minimum expected cluster size exceeds the 40+2k guideline for stable k-medoid estimation. Sensitivity ablation: Spearman ρ vs. operator proficiency for k ∈ {2,...,8}.\\n\\n**Relationship to sWk-means**: Steps 1-2 share the SW+clustering pipeline with sWk-means. OT-Consensus extends with robust barycenters, trajectory-as-measure representations, and mode-aware filtering.\\n\\n**Relationship to velocity debiasing (Modi Shi et al.)**: Complementary — velocity debiasing normalizes speed variation (data transformation), OT-Consensus discovers strategy modes and scores quality (data selection). Composable in principle; not evaluated in CoRL submission.\\n\\n**Why mode-aware distributional priority beats alternatives — explicit hypotheses**: (H1) *Mode-aware quality vs. mode-agnostic diversity*: FAKTUAL maximizes global entropy, retaining low-quality demos for coverage. OT-Consensus scores quality within each mode, correctly deprioritizing within-mode outliers. (H2) *Distributional shape vs. scalar proxies*: SW2 captures full distributional structure that MI and smoothness metrics collapse. (H3) *Mode-aware vs. mode-agnostic learned scoring*: Robometer assigns a single global quality score per trajectory. When demonstrations contain multiple valid strategies, Robometer may penalize trajectories from minority strategies that deviate from the majority pattern, even if those trajectories are high-quality within their strategy mode. OT-Consensus first discovers modes, then scores within each — a trajectory is judged against its own strategy's consensus, not the global population. (H4) *Temporal structure preservation*: Time grounding captures temporal alignment that smoothness metrics ignore. (H5) *No learned components*: Unlike DemInf, SCIZOR, S2I, FAKTUAL, or Robometer, OT-Consensus uses only a frozen visual encoder and closed-form OT.\\n\\n**Minimum success criterion**: Spearman correlation with operator proficiency ≥0.1 higher than the best mode-agnostic proxy AND ≥5% absolute downstream success rate improvement over the best policy-free baseline.\\n\\n**Theoretical motivation (informal for CoRL)**: Under ε-contamination noise, the robust barycenter converges to the clean barycenter. Clean trajectories concentrate near β*; corrupted trajectories deviate. Formal detection guarantees deferred to AAAI 2027.\\n\\n**Evaluation design — two tiers for timeline management**:\\n\\n**Tier A (Minimal Viable Paper — commit by May 21)**:\\n(a) *Day 1 validation gate* (May 13): Synthetic toy + RoboMimic pilot (~4h). Go/no-go by EOD.\\n(b) *Primary experiment — quality metric comparison*: Compute OT-Consensus, Robometer (using released Robometer-4B model weights, zero-shot on RoboMimic MH — Robometer was not evaluated on RoboMimic in the original paper, making this a fair zero-shot comparison), diversity baseline (FAKTUAL or FPS fallback), and DemInf (MI) scores on all 300 RoboMimic MH demos. Robometer scoring requires only forward passes through Qwen3-VL-4B (~15 min on A100 for 300 demos), no training or fine-tuning. Evaluate each metric's Spearman correlation with known operator proficiency and AUC for separating Better vs. Worse operators. This comparison directly tests the central claim: can a training-free geometric scorer match a learned scorer (trained on 1M+ trajectories) on mode-aware quality discrimination? If OT-Consensus matches or exceeds Robometer's correlation, that is a much stronger contribution claim than beating DemInf/RINSE alone — it shows training-free geometric scoring can rival learned scoring. If Robometer wins on correlation but loses on mode-awareness (e.g., penalizes minority-strategy trajectories), that reveals a complementary strength.\\n(c) *Downstream policy performance*: Fine-tune SmolVLA (450M) on filtered subsets (top-50% by each metric) on 2 tasks (Can, Square) × 5 conditions (OT-Consensus, Robometer, diversity baseline, DemInf, random) × 2 seeds = 20 runs (~80h). Adding Robometer as a downstream condition adds only 4 runs (~16h) over the previous design.\\n(d) *Essential ablations*: SigLIP vs. DINOv2 encoder (4 runs, ~16h). k sensitivity analysis (no additional GPU).\\n\\n**Tier B (Full Paper — expand if on track by May 21)**:\\nAdd RINSE and SCIZOR as conditions (total 7 conditions); add Lift and Transport tasks (total 4 tasks); increase to 3 seeds; add top-33% filtering threshold. Add LIBERO generalization test: compute OT-Consensus and Robometer scores on 1-2 LIBERO tasks and run downstream SmolVLA comparison. Note: LIBERO demonstrations come from a single operator without explicit quality labels or multi-operator structure, so this tests *graceful degradation* — whether OT-Consensus's quality scoring (with k=1, single mode) still provides useful signal via distance-from-barycenter filtering on single-strategy data, and whether its performance degrades gracefully rather than over-clustering homogeneous data. This addresses benchmark narrowness without requiring multi-operator structure that LIBERO does not provide. Additionally, compare against LIBERO's known data redundancy (DATA-FM showed random 30% matches full-dataset performance) — can OT-Consensus's quality-based selection outperform random subsampling? Add ablations (k-medoid in SW2 vs. k-means in SigLIP space; ground metric weight sensitivity; SW2 projection count sensitivity).\\n\\n**Extended version (AAAI 2027)**: Add OpenVLA-OFT (7B), additional LIBERO tasks, formal theoretical analysis, S2I and CUPID as additional baselines, velocity debiasing composition experiment, comprehensive ablations.\\n\\n**Parallel writing plan**: Days 1-3 (May 13-15): draft introduction (PER analogy framing) and related work. Days 4-8 (May 16-20): method + results. Days 9-10 (May 21-22): analysis + ablations. Days 11-12 (May 23-24): revision. Day 13 (May 25): abstract on OpenReview. Days 13-15 (May 25-28): final submission.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~250h A100 for CoRL Tier A (Day 1 validation gate: ~4h; SW2 full matrix: ~8h with SigLIP+DINOv2; barycenter computation: ~4h; Robometer scoring: ~0.5h; FAKTUAL reproduction or FPS fallback: ~20h; SmolVLA fine-tuning: ~4h/run × 5 conditions × 2 tasks × 2 seeds = 80h; DINOv2 ablation: ~16h; evaluation rollouts: ~4h; k sensitivity: ~2h; buffer: ~30h). Tier B adds ~150h (RINSE+SCIZOR conditions, 2 more tasks, 3 seeds, LIBERO generalization). Extended AAAI version adds ~700h.\",\n      \"gpu_utilization\": \"~75% for CoRL sprint — Day 1 validation gate determines whether sprint proceeds.\",\n      \"timeline\": \"CoRL 2026: 16-day sprint (May 13–28). Day 1 (May 13): validation gate + Robometer setup. Days 2-3 (May 14-15): full SW2 matrix + Robometer scoring + FAKTUAL attempt + draft intro/related work. Day 4 (May 16): FAKTUAL decision point. Days 4-8 (May 16-20): Tier A SmolVLA training (5 conditions including Robometer) + draft method. Days 9-10 (May 21-22): evaluation + analysis + draft results. Tier A commit: May 21. Days 11-12 (May 23-24): Tier B expansion + revision. Day 13 (May 25): abstract submission. Days 14-16 (May 25-28): final submission.\",\n      \"team\": \"CoRL: 1 researcher, full-time sprint. AAAI extension: +1 collaborator for theory.\",\n      \"estimated_gpu_cost\": \"CoRL Tier A: $375 (250h × $1.50/h). Tier B: +$225. AAAI: +$1,050. Total: $1,650.\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~230h A100 for CoRL Tier A\",\n      \"gpu_utilization\": \"~85% — agent handles pipeline implementation, Robometer integration, SmolVLA orchestration; human focuses on analysis and writing\",\n      \"timeline\": \"CoRL: 16 days (May 13-28). Day 1: human analyzes validation gate + go/no-go (~2h). Days 2-16: agent-driven with human checkpoints at FAKTUAL decision (Day 4) and Tier A commit (Day 10).\",\n      \"team\": \"1 researcher, ~4–5h/day; agent handles implementation\",\n      \"claude_api_cost\": \"$100–200 for CoRL. +$150–300 for AAAI.\",\n      \"estimated_gpu_cost\": \"CoRL Tier A: $345 (230h × $1.50/h). Tier B: +$150. AAAI: +$900.\",\n      \"risk_note\": \"Adding Robometer as a baseline is low-risk: code/weights are public, scoring takes ~15 min, and it adds only 4 downstream runs to Tier A. LIBERO generalization (Tier B only) is also low-risk: data is in lerobot format and SmolVLA has a pretrained LIBERO checkpoint. Key risk remains FAKTUAL code availability — mitigated by FPS fallback.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~350h A100 for CoRL Tier A+B\",\n      \"gpu_utilization\": \"~90% — agent queues experiments continuously\",\n      \"timeline\": \"CoRL: 10–12 days with 4 concurrent A100s. Day 1: validation gate + Robometer setup (4h, requires human go/no-go). Days 2-4: full pipeline + Tier A. Days 5-8: Tier B + LIBERO. Human writes paper in parallel.\",\n      \"team\": \"0 for CoRL experiments after initial setup. Theory for AAAI requires human.\",\n      \"claude_api_cost\": \"$200–400 for CoRL. +$200–400 for AAAI.\",\n      \"estimated_gpu_cost\": \"CoRL: $525 (350h × $1.50/h). AAAI: +$1,500.\",\n      \"speed_bottleneck\": \"GPU count for parallel SmolVLA fine-tuning. With 4 A100s, Tier A completes in ~24h.\",\n      \"risk_note\": \"Robometer integration is straightforward (pip install + HuggingFace model download). LIBERO integration uses existing lerobot tooling.\"\n    }\n  },\n  \"target_venues\": [\n    \"CoRL 2026 (abstract deadline May 25, paper deadline May 28 EOD — per official Instruction for Authors; primary target with Robometer comparison)\",\n    \"AAAI 2027 (deadline expected ~August 2026 — extended version with theory, OpenVLA-OFT, Robometer fine-grained analysis, velocity debiasing composition)\",\n    \"ICLR 2027 (deadline expected ~October 2026 — most complete version, backup)\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"Prioritized Experience Replay [PER] (Schaul et al., ICLR 2016)\",\n    \"A Distributional Perspective on Reinforcement Learning (Bellemare et al., ICML 2017)\",\n    \"Diversity You Can Actually Measure: A Fast, Model-Free Diversity Metric for Robotics Datasets [FAKTUAL] (arXiv Mar 2026, 2603.11634)\",\n    \"CUPID: Curating Data your Robot Loves with Influence Functions (CoRL 2025)\",\n    \"Robot Data Curation with Mutual Information Estimators [DemInf] (RSS 2025)\",\n    \"DataMIL: Selecting Data for Robot Imitation Learning with Datamodels (ICLR 2026)\",\n    \"Curating Demonstrations using Online Experience [Demo-SCORE] (RSS 2025)\",\n    \"SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning (ICRA 2026)\",\n    \"Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning [QoQ] (arXiv Mar 2026)\",\n    \"Learning from the Best: Smoothness-Driven Metrics for Data Quality in Imitation Learning [RINSE] (ICML 2025, arXiv 2604.23000)\",\n    \"S2I: Select Segments to Imitate — Segment-Level Selection and Optimization for Mixed-Quality Demonstrations (ICRA 2025)\",\n    \"Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons (RSS 2026, arXiv 2603.02115)\",\n    \"Is Diversity All You Need for Scalable Robotic Manipulation? [velocity debiasing] (Modi Shi et al., arXiv Jul 2025, 2507.06219)\",\n    \"Automated regime classification in multidimensional time series data using sliced Wasserstein k-means clustering [sWk-means] (Luan & Hamp, DSFE 2025)\",\n    \"On Data Redundancy in VLA Training [TSS] (DATA-FM Workshop @ ICLR 2026)\",\n    \"Expert or not? Assessing Data Quality in Offline Reinforcement Learning [BWD] (arXiv Oct 2025, 2510.12638)\",\n    \"Sliced-Wasserstein Distance-based Data Selection [SWAD] (Pallage & Lesage-Landry, arXiv Apr 2025, 2504.12918)\",\n    \"Consistency Matters: Defining Demonstration Data Quality Metrics in Robot Learning from Demonstration (ACM THRI 2025)\",\n    \"Latent Wasserstein Adversarial Imitation Learning [LWAIL] (ICLR 2026, 2603.05440)\",\n    \"Learning from Imperfect Demonstrations via Temporal BT-Guided Trajectory Repair (arXiv Apr 2026, 2604.04225)\",\n    \"Optimal Transport for Offline Imitation Learning [OTR] (ICLR 2023)\",\n    \"Robot Policy Learning with Temporal Optimal Transport Reward (NeurIPS 2024)\",\n    \"Cross-Domain Imitation Learning via Optimal Transport [GWIL] (ICLR 2022)\",\n    \"Watch and Match: Supercharging Imitation with Regularized Optimal Transport [ROT] (NeurIPS 2022)\",\n    \"Outlier-Robust Optimal Transport: Duality, Structure, and Statistical Analysis (Nietert et al., AISTATS 2022)\",\n    \"Robust Wasserstein Barycenter (arXiv Mar 2026)\",\n    \"Approximate Algorithms for k-Sparse Wasserstein Barycenter with Outliers (IJCAI 2024)\",\n    \"Barycenters in the Wasserstein Space (SIAM J. Math. Anal. 2011)\",\n    \"Lightspeed Geometric Dataset Distance via Sliced Optimal Transport [s-OTDD] (ICML 2025)\",\n    \"Minibatch Optimal Transport Distances: Analysis and Applications (Fatras et al., arXiv 2021, 2101.01792)\",\n    \"Unbalanced Minibatch Optimal Transport; Applications to Domain Adaptation (Fatras et al., ICML 2021)\",\n    \"Distributional Reinforcement Learning with Quantile Regression (Dabney et al., AAAI 2018)\"\n  ],\n  \"description\": \"We propose OT-Consensus, a training-free, mode-aware method for scoring demonstration quality in robot learning datasets using optimal transport geometry, framed as the demonstration-curation analogue of Prioritized Experience Replay's TD-error scoring. Just as PER (Schaul et al., 2016) uses TD-error magnitude to identify which replay transitions deviate most from the agent's value estimate, OT-Consensus uses Sliced Wasserstein distance to the mode-specific barycenter to identify which demonstrations deviate most from their strategy mode's consensus — with inverted polarity (PER up-weights deviations for learning; OT-Consensus down-weights deviations for filtering). This framing is grounded in distributional RL theory: Bellemare et al. (2017) proved the Wasserstein metric governs distributional Bellman convergence, and we import the same metric family into demonstration curation. Each trajectory is represented as a discrete measure over visual-encoder-embedded state-action-time tuples, pairwise SW2 distances capture distributional similarity, k-medoid clustering discovers strategy modes, and distance from each mode's robust barycenter provides the quality score. This revision (round 9) incorporates three targeted changes: (1) Robometer added to evaluation — Tier A includes Spearman correlation comparison between OT-Consensus and Robometer-4B (publicly released, zero-shot on RoboMimic MH, ~15 min compute), directly testing whether a training-free geometric scorer can match a learned scorer trained on 1M+ trajectories on mode-aware quality discrimination; Tier A downstream adds Robometer as a 5th condition. (2) Benchmark narrowness addressed via LIBERO graceful-degradation test in Tier B — LIBERO lacks multi-operator structure (single operator, no quality labels), so it tests whether OT-Consensus degrades gracefully on single-strategy data rather than mode discovery. (3) PER analogy fully developed as the conceptual framing — SW2-to-barycenter as 'distributional priority score' with explicit polarity inversion, grounded in distributional RL's Wasserstein contraction. Minimum success criterion: Spearman ρ ≥0.1 above best mode-agnostic proxy AND ≥5% absolute downstream improvement. Tiered plan: Tier A (by May 21) includes validation gate + 5-condition metric comparison (with Robometer) + 5×2×2 downstream + ablations; Tier B (by May 28) adds LIBERO generalization + additional conditions/tasks/seeds.\",\n  \"project_name\": \"ot_traj_consensus\",\n  \"source\": \"web_research\"\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6dfdb45-fe5d-40f1-bbb2-e282d09b39e0",
  "isSidechain": false,
  "requestId": "req_011Cb17i1nTczXb7yh4mAKJT",
  "type": "assistant",
  "uuid": "66f63d42-8204-47c8-bca3-892506b325d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MpWuycXk2ozuqaayYSCYk8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4379,
      "cache_creation_input_tokens": 3944,
      "cache_read_input_tokens": 31570,
      "output_tokens": 11057,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3944,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4379,
          "output_tokens": 11057,
          "cache_read_input_tokens": 31570,
          "cache_creation_input_tokens": 3944,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3944
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

### Tool result

_source line 21 · 2026-05-13T19:30:17.824Z_

<details><summary>↩ Tool result · reported error · `toolu_01A5tUhDYExgMSYUdo16J5Yg`</summary>

```text
Claude requested permissions to write to /tmp/revised_idea_round9.json, but you haven't granted it yet.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "66f63d42-8204-47c8-bca3-892506b325d3",
  "isSidechain": false,
  "promptId": "bbda98e0-f6b9-4cc9-88b7-1263809b65cb",
  "type": "user",
  "uuid": "2af20db4-9f99-4c0b-b18f-e0eead77fc9b",
  "toolUseResult": "Error: Claude requested permissions to write to /tmp/revised_idea_round9.json, but you haven't granted it yet.",
  "sourceToolAssistantUUID": "66f63d42-8204-47c8-bca3-892506b325d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-13 (UTC).**  ## Original idea {   \"title\": \"Mode-Aware Quality Scoring for Demonstration Curation via Sliced Wasse…",
  "leafUuid": "2af20db4-9f99-4c0b-b18f-e0eead77fc9b",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Mode-aware quality scoring for demonstrations via sliced Wasserstein consensus",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb"
}
```

---

### Tool call

_source line 24 · 2026-05-13T19:33:42.439Z_

<details open><summary>🔧 Tool call — Write · `toolu_01VzTRSETwiqjWq1Qfxy4Jjs`</summary>

```json
{
  "file_path": "/tmp/revised_idea_round9.json",
  "content": "{\n  \"change_type\": \"minor\",\n  \"title\": \"Mode-Aware Quality Scoring for Demonstration Curation via Sliced Wasserstein Consensus\",\n  \"core_problem\": \"How should we curate multimodal demonstration datasets that contain multiple valid strategies of varying quality? Diversity-maximizing approaches (FAKTUAL) improve average performance but explicitly fail when demonstrations contain conflicting strategies — blindly including diverse-but-poor demonstrations degrades learning. Quality-scoring approaches (CUPID, DataMIL) work well but require expensive policy training, validation rollouts, or influence function estimation. Learned reward models (Robometer) can score trajectory quality without a task-specific policy but require 1M+ training trajectories and are not mode-aware. Recent evidence from 'Is Diversity All You Need?' (Modi Shi et al., arXiv Jul 2025) sharpens this problem: they show that expert diversity creates *velocity multimodality* — different demonstrators executing the same spatial trajectory at different speeds — that directly degrades policy learning, producing 15% performance losses that their velocity normalization method recovers. This confirms that multi-operator demonstrations create distributional conflicts that harm learning, but their fix (velocity normalization) only addresses speed variation along shared paths, not the broader problem of scoring quality across genuinely different strategy modes. Conceptually, the challenge mirrors Prioritized Experience Replay (PER; Schaul et al., 2016) but with inverted polarity: PER uses TD-error magnitude to *up-weight* transitions that deviate from the agent's current value estimate (deviation = informative, learn more from it), while demonstration curation requires *down-weighting* trajectories that deviate from the demonstrator consensus (deviation = suspicious, filter it out). Both share the core mechanism of scoring samples by their distance from an expected distribution, but serve opposite objectives — prioritization vs. filtration. This RL-inspired framing suggests that what demonstration curation needs is a *distributional priority score* analogous to TD-error: one that measures each trajectory's deviation from expected behavior, but in a mode-aware manner that distinguishes between valid strategy diversity and genuine quality degradation. Distributional RL theory (Bellemare et al., 2017) grounds this connection formally: the distributional Bellman operator is a contraction in the p-Wasserstein metric, establishing Wasserstein distances as the natural metric family for distributional deviation in sequential decision-making. The field lacks a training-free quality scoring method that is *mode-aware* — one that discovers distinct strategy modes in the data and scores quality within each mode using distributional deviation, rather than treating all demonstrations as drawn from a single distribution.\",\n  \"opportunity\": \"The demonstration curation landscape has crystallized into five camps: (1) *policy-dependent quality methods* (CUPID, DataMIL, Demo-SCORE, QoQ) that achieve SOTA but require trained policies or validation rollouts; (2) *policy-free learned quality methods* (Robometer) that train general-purpose reward models on massive trajectory datasets to score quality without a task-specific policy, but require 1M+ training trajectories for pre-training and are not mode-aware — they assign a global quality score without distinguishing between multiple valid strategies. Robometer achieves strong absolute success rates on retrieval tasks (e.g., ~95% on Stir Pot where baselines score near 0%), though the reported 4.5x average improvement is inflated by near-zero baseline performance on several tasks rather than reflecting a uniform 4.5x gain; (3) *policy-free quality proxies* (DemInf, RINSE, SCIZOR) that use scalar metrics (MI, smoothness, progress) but collapse distributional structure and are mode-agnostic; (4) *policy-free diversity methods* (FAKTUAL) that maximize trajectory entropy but explicitly acknowledge 'promoting diversity may actually be harmful when the model is not capable of capturing multimodality in the data'; and (5) *distribution normalization methods* ('Is Diversity All You Need?', Modi Shi et al., arXiv Jul 2025) that identify velocity multimodality from expert diversity as a concrete failure mode and propose velocity distribution debiasing — training a velocity model to normalize action chunk speeds, recovering 15% performance (equivalent to 2.5x pre-training data). This reveals a fundamental tension: diversity-based curation fails precisely when demonstrations are multimodal, distribution normalization removes one source of multimodality but does not score quality, learned scorers (Robometer) are powerful but mode-agnostic and require massive pre-training data, and scalar proxies collapse distributional structure. The PER analogy illuminates the gap: RL already solved the 'which samples matter?' problem for experience replay via TD-error (a *distributional deviation score*), but demonstration curation has no analogous mechanism that is both mode-aware and training-free. Recent evidence further motivates intelligent curation: 'On Data Redundancy in VLA Training' (DATA-FM @ ICLR 2026) shows that random 30% sampling of LIBERO matches full-dataset SmolVLA performance, revealing massive data redundancy — but their difficulty-based Temporal Surprise Score underperformed random selection, suggesting that naive quality proxies can be counterproductive. The key gap: no existing training-free method provides *mode-aware distributional priority scoring* — discovering strategy modes and assessing quality relative to mode-specific consensus via distributional deviation. Optimal transport geometry fills this gap naturally: Sliced Wasserstein distances define a metric space over trajectory distributions that captures shape, spread, and temporal structure; clustering in this space discovers strategy modes; and distance from each mode's robust barycenter provides a geometrically grounded, mode-aware quality score — the demonstration-curation analogue of PER's TD-error, operating in the same Wasserstein metric family that governs distributional RL convergence.\",\n  \"landscape\": \"**Policy-dependent quality methods**: CUPID (CoRL 2025) uses influence functions estimating each demonstration's causal impact on closed-loop policy return, achieving SOTA on RoboMimic with <33% of curated data; requires a trained policy and evaluation rollouts. DataMIL (ICLR 2026) uses the datamodels paradigm for end-to-end policy-driven selection validated on 60+ tasks including OXE; requires surrogate loss computation with policy training. Demo-SCORE (RSS 2025) trains classifiers on online rollout success/failure to self-curate, achieving 15-35% gains; requires online robot interaction. QoQ (arXiv Mar 2026) uses influence functions with theoretical analysis but requires a validation set and scales O(n squared). **Policy-free learned quality methods**: Robometer (RSS 2026, arXiv 2603.02115) trains a general-purpose VLM-based reward model (Qwen3-VL-4B) on RBM-1M (1M+ trajectories across 21 embodiments) using a dual objective of frame-level progress supervision and trajectory-level preference learning. Achieves strong absolute success rates on retrieval tasks (e.g., ~95% on Stir Pot where baselines score near 0%), though the reported 4.5x average improvement is inflated by near-zero baseline performance on several tasks rather than reflecting a uniform 4.5x gain. However, Robometer (a) requires 1M+ training trajectories (~6TB) for pre-training — infeasible when curating smaller datasets without pre-existing large-scale data; (b) is NOT mode-aware — it assigns a single global quality score per trajectory without distinguishing between multiple valid strategies; (c) was not evaluated on RoboMimic or against demonstration curation methods (CUPID, DemInf, RINSE, SCIZOR, FAKTUAL) — its comparisons are against VLM reward models (RoboReward, GVL, VLAC). Robometer code and model weights (Robometer-4B) are publicly released on GitHub (github.com/robometer/robometer) and HuggingFace (robometer/Robometer-4B), enabling direct zero-shot comparison on RoboMimic MH. A LIBERO-fine-tuned variant (Robometer-LIBERO) is also available. OT-Consensus is complementary: training-free, mode-aware, and geometric, requiring no pre-training data. **Policy-free quality proxies**: DemInf (RSS 2025) estimates trajectory-level mutual information between states and actions via k-NN estimators with VAE embeddings, achieving 5-10% gains on RoboMimic; captures information content but collapses distributional structure to a scalar and is mode-agnostic. RINSE (ICML 2025, arXiv 2604.23000) uses Spectral Arc Length (SAL) and Trajectory-Envelope Distance (TED) smoothness metrics achieving 16-20% success gains; assumes smoothness universally correlates with quality, failing for tasks where jerky motions are correct. SCIZOR (ICRA 2026) combines self-supervised task progress prediction with deduplication, achieving 15.4% average improvement across RoboMimic/OXE/Sirius-Fleet; no theoretical guarantees and conflates lack of progress with low quality. S2I (ICRA 2025) performs segment-level selection using contrastive learning with 3 expert reference demonstrations; requires expert references and cannot operate fully unsupervised. Consistency Matters (ACM THRI 2025) proposes 10 motion-based consistency metrics with 76-91% success prediction accuracy; limited to geometric consistency without distributional analysis. **Policy-free diversity methods**: FAKTUAL (arXiv Mar 2026, 2603.11634) uses signature kernel entropy for diversity-based curation; fully model-free and tested on RoboMimic MH and MetaWorld. Compared against CUPID, DemInf, and Demo-SCORE. FAKTUAL performs modestly above random but below quality-based methods, and *explicitly acknowledges* that 'promoting diversity may actually be harmful when the model is not capable of capturing multimodality in the data.' NOTE: As of May 2026, FAKTUAL code is not publicly released; FPS fallback available. **Distribution normalization methods**: 'Is Diversity All You Need for Scalable Robotic Manipulation?' (Modi Shi et al., arXiv Jul 2025, 2507.06219) identifies velocity multimodality from expert diversity as a concrete failure mode and proposes velocity distribution debiasing, yielding 15% gains. Validates the core premise that multi-operator demonstrations create distributional conflicts, but addresses only velocity variation along shared paths. **RL-inspired scoring connections**: Prioritized Experience Replay (PER; Schaul et al., ICLR 2016) established TD-error magnitude as a distributional deviation score for sample prioritization — the conceptual precursor to OT-Consensus's mode-aware quality scoring. OTR (ICLR 2023) uses OT to score offline trajectories by alignment to expert demonstrations — reward assignment via OT, not curation. SWAD (Pallage and Lesage-Landry, arXiv Apr 2025, 2504.12918) uses sliced-Wasserstein distance to barycenters for unsupervised anomaly detection on i.i.d. tabular data — the closest methodological precursor in general ML, but operates on individual data points rather than trajectory measures. Distributional RL theory (Bellemare et al., ICML 2017) proved Wasserstein contraction of the distributional Bellman operator, establishing OT as the natural metric family for distributional analysis in sequential decision-making. Distributional RL with Quantile Regression (Dabney et al., AAAI 2018) closed the theory-practice gap by directly minimizing 1-Wasserstein distance. **OT-based quality/distance methods (adjacent)**: sWk-means (Luan and Hamp, DSFE 2025) uses sliced Wasserstein distances + k-means clustering for financial regime detection — a methodological precursor to OT-Consensus's first two steps, but without barycenters, quality scoring, or trajectory representations. BWD/'Expert or not?' (arXiv Oct 2025) introduces Bellman Wasserstein Distance requiring a behavioral critic. LWAIL (ICLR 2026) uses Wasserstein for state-only distribution matching in adversarial IL policy learning. **Data redundancy in VLA training**: 'On Data Redundancy in VLA Training' (DATA-FM Workshop @ ICLR 2026) shows random 30% sampling of LIBERO matches full-dataset SmolVLA performance; Temporal Surprise Score underperforms random selection. **OT in robot learning (not curation)**: OTR (ICLR 2023), Temporal OT Reward (NeurIPS 2024), GWIL (ICLR 2022), ROT (NeurIPS 2022). **OT theory**: Robust Wasserstein Barycenter (arXiv Mar 2026), Outlier-Robust OT (Nietert et al., AISTATS 2022), k-Sparse Wasserstein Barycenter with Outliers (IJCAI 2024), s-OTDD (ICML 2025). **Gap**: No existing method provides training-free, mode-aware distributional priority scoring for demonstration quality. FAKTUAL is mode-agnostic diversity; DemInf/RINSE/SCIZOR are mode-agnostic scalar proxies; Robometer is a powerful learned scorer but not mode-aware and requires 1M+ trajectories; CUPID/DataMIL are mode-aware in principle but policy-dependent; sWk-means stops at regime identification; SWAD uses SW-to-barycenter on i.i.d. points, not trajectory measures; velocity debiasing normalizes speed but does not score quality. OT-Consensus uniquely combines mode awareness, distributional priority scoring, and training-free operation.\",\n  \"approach\": \"**Overview**: OT-Consensus is a training-free, mode-aware demonstration quality scoring method. We reframe the demonstration curation problem through the lens of RL-inspired distributional priority scoring: just as PER (Schaul et al., 2016) scores replay transitions by TD-error magnitude — their deviation from the agent's value estimate — OT-Consensus scores demonstrations by their Sliced Wasserstein distance from the mode-specific barycenter — their distributional deviation from demonstrator consensus. The polarity is inverted: PER up-weights high-deviation samples (surprise = informative), while OT-Consensus down-weights high-deviation demonstrations (deviation = suspicious quality). Both operate via the same mechanism — measuring distributional deviation to score sample utility — grounded in the Wasserstein metric family that governs distributional RL convergence (Bellemare et al., 2017). The core conceptual contribution is that demonstration quality should be assessed as *distributional priority within each strategy mode*, not as global diversity or scalar proxy. This extends the SW+clustering pipeline introduced by sWk-means (Luan and Hamp, DSFE 2025) from financial regime detection to robot demonstration curation, with three key additions: robust barycenters for quality scoring, trajectory-as-measure representation, and mode-aware filtering. We target a focused empirical contribution for CoRL 2026 with formal theoretical analysis deferred.\\n\\n**Day 1 Validation Gate (May 13 — before committing to the full sprint)**: Two preliminary experiments (~4h total). (a) *Synthetic toy*: 200 2D trajectories, 2 modes x 3 quality tiers. Verify k=2 recovers modes (ARI >= 0.8) and within-mode SW2-to-barycenter correlates with quality (Spearman rho >= 0.5). Show MI and smoothness metrics fail to distinguish within-mode quality. (b) *RoboMimic pilot*: 50 trajectories from MH Can, k-medoid with k=3 and k=6, ARI against operator/proficiency labels. (c) *Gate*: Proceed if synthetic ARI >= 0.8 AND rho >= 0.5, AND RoboMimic ARI >= 0.1.\\n\\n**FAKTUAL Reproduction Plan**: Code not released. Mitigation: contact authors May 13; reimplementation via KSig May 14-15; FPS fallback decision May 16.\\n\\n**Representation design**: Each trajectory mapped to a discrete measure over (visual_embedding, action, normalized_time) tuples. Ground metric: weighted sum of squared distances. Default encoder: SigLIP-SO400M (SmolVLA's own encoder — quality scored in policy-relevant space). DINOv2 ablation proves generalization.\\n\\n**Scalable pairwise distances**: SW2 with O(Ln log n) per pair, L=50-200 projections. N squared matrix for 300 demos ~15 min on A100.\\n\\n**Mode discovery and quality scoring**: (1) SW2 pairwise distance matrix. (2) k-medoid clustering (PAM); k via silhouette over {2,...,8}. (3) Robust barycenter per cluster via trimmed-mean OT (epsilon=0.1). (4) Quality score: q_i = 1 / (1 + SW2(mu_i, beta_m)), normalized to [0,1]. This is the *distributional priority score* — the curation analogue of PER's TD-error.\\n\\n**Relationship to PER and distributional RL**: The SW2-to-barycenter score has a precise structural analogy to TD-error priority. Both measure sample deviation from a distributional reference (value estimate for PER; mode barycenter for OT-Consensus). The polarity inversion (PER: high deviation -> up-weight for learning; OT-Consensus: high deviation -> down-weight for filtering) reflects the difference between learning from surprise (RL) and filtering for consensus (curation). Formally, distributional RL's Wasserstein contraction (Bellemare et al., 2017) established that the p-Wasserstein metric governs convergence of return distributions under the Bellman operator — OT-Consensus imports the same metric family into demonstration curation. This connection extends prior work: OTR (Luo et al., ICLR 2023) uses OT to assign reward scores to offline trajectories, and SWAD (Pallage and Lesage-Landry, 2025) uses SW-distance-to-barycenter for anomaly detection in general data selection. OT-Consensus extends these with mode-aware clustering and trajectory-as-measure representations.\\n\\n**Hypothesis H3 (vs. Robometer)**: Robometer assigns a single global quality score per trajectory via a VLM trained on 1M+ trajectories. When demonstrations contain multiple valid strategies, Robometer may penalize trajectories from minority strategies that deviate from the majority pattern, even if those trajectories are high-quality within their strategy mode. OT-Consensus first discovers modes, then scores within each — a trajectory is judged against its own strategy's consensus, not the global population. Prediction: on RoboMimic MH, OT-Consensus's mode-aware scoring achieves comparable or higher Spearman correlation with operator proficiency than Robometer, and specifically preserves high-quality trajectories from minority strategy modes that Robometer may underrate.\\n\\n**Mode discovery analysis**: Expected k=3 (proficiency) or k=6 (operators). With N=300, minimum cluster size exceeds 40+2k guideline. Sensitivity: Spearman rho vs. proficiency for k in {2,...,8}.\\n\\n**Minimum success criterion**: Spearman rho >= 0.1 above best mode-agnostic proxy AND >= 5% absolute downstream success rate improvement over best policy-free baseline.\\n\\n**Evaluation design — two tiers**:\\n\\n**Tier A (Minimal Viable Paper — commit by May 21)**:\\n(a) *Day 1 validation gate* (May 13): Synthetic toy + RoboMimic pilot (~4h).\\n(b) *Quality metric comparison*: Compute 5 scores on all 300 RoboMimic MH demos: OT-Consensus, Robometer-4B (zero-shot, using publicly released model weights — Robometer was never evaluated on RoboMimic, making this a fair comparison), diversity baseline (FAKTUAL or FPS), DemInf (MI), and random. Robometer scoring: ~15 min on A100 via forward passes through Qwen3-VL-4B on extracted image observations; no training or fine-tuning. Evaluate Spearman correlation with operator proficiency, AUC for Better-vs-Worse separation. This directly tests the central claim: can a training-free geometric scorer match a learned scorer trained on 1M+ trajectories? Analyze mode-awareness: does Robometer penalize minority-strategy high-quality demos that OT-Consensus correctly scores?\\n(c) *Downstream policy performance*: SmolVLA (450M) on filtered subsets (top-50%) on 2 tasks (Can, Square) x 5 conditions (OT-Consensus, Robometer, diversity baseline, DemInf, random) x 2 seeds = 20 runs (~80h).\\n(d) *Ablations*: SigLIP vs. DINOv2 encoder (4 runs, ~16h). k sensitivity (no additional GPU).\\n\\n**Tier B (Full Paper — expand if on track by May 21)**:\\nAdd RINSE and SCIZOR conditions (7 total); add Lift and Transport tasks (4 total); increase to 3 seeds; add top-33% threshold. *LIBERO graceful-degradation test*: Compute OT-Consensus and Robometer scores on 1-2 LIBERO tasks and run downstream SmolVLA comparison. LIBERO demonstrations come from a single operator without multi-operator structure or quality labels, so this tests *graceful degradation* — whether OT-Consensus's quality scoring (with k=1, single mode) still provides useful signal via distance-from-barycenter filtering on single-strategy data, rather than over-clustering homogeneous data. Compare against known data redundancy (DATA-FM: random 30% matches full-dataset). Use Robometer-LIBERO (fine-tuned variant, publicly available) for strongest possible learned baseline on LIBERO. Additional ablations (SW2 vs. embedding k-means; ground metric weights; projection count).\\n\\n**Extended version (AAAI 2027)**: OpenVLA-OFT (7B), additional LIBERO tasks, formal theory, CUPID/S2I baselines, velocity debiasing composition, comprehensive ablations.\\n\\n**Parallel writing plan**: Days 1-3: intro (PER framing) + related work. Days 4-8: method + results. Days 9-10: analysis + ablations. Days 11-16: revision + submission.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~250h A100 for CoRL Tier A (Day 1 gate: ~4h; SW2 matrix: ~8h; barycenters: ~4h; Robometer scoring: ~0.5h; FAKTUAL/FPS: ~20h; SmolVLA: ~4h/run x 20 runs = 80h; DINOv2 ablation: ~16h; eval rollouts: ~4h; buffer: ~30h). Tier B adds ~160h (extra conditions, tasks, seeds, LIBERO). AAAI adds ~700h.\",\n      \"gpu_utilization\": \"~75% for CoRL sprint.\",\n      \"timeline\": \"CoRL 2026: 16-day sprint (May 13-28). Day 1: validation gate + Robometer setup. Days 2-3: full SW2 matrix + Robometer scoring on 300 demos + FAKTUAL attempt + draft intro/related work. Day 4: FAKTUAL decision. Days 4-8: Tier A SmolVLA training (5 conditions) + method draft. Days 9-10: evaluation + analysis + results draft. Tier A commit: May 21. Days 11-12: Tier B expansion + revision. Day 13: abstract submission (May 25). Days 14-16: final submission by May 28 EOD.\",\n      \"team\": \"CoRL: 1 researcher full-time. AAAI: +1 collaborator for theory.\",\n      \"estimated_gpu_cost\": \"Tier A: $375. Tier B: +$240. AAAI: +$1,050. Total: $1,665.\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~230h A100 for CoRL Tier A\",\n      \"gpu_utilization\": \"~85% — agent handles SW2 pipeline, Robometer integration, SmolVLA orchestration; human focuses on analysis and writing\",\n      \"timeline\": \"CoRL: 16 days. Day 1: human analyzes gate + go/no-go. Days 2-16: agent-driven with checkpoints at FAKTUAL decision (Day 4) and Tier A commit (Day 10).\",\n      \"team\": \"1 researcher, ~4-5h/day; agent handles implementation\",\n      \"claude_api_cost\": \"$100-200 for CoRL. +$150-300 for AAAI.\",\n      \"estimated_gpu_cost\": \"Tier A: $345. Tier B: +$150. AAAI: +$900.\",\n      \"risk_note\": \"Robometer integration is low-risk: code/weights public, scoring ~15 min, adds only 4 downstream runs. LIBERO is Tier B only and uses existing lerobot tooling. Key risk remains FAKTUAL code — mitigated by FPS fallback.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~350h A100 for CoRL Tier A+B\",\n      \"gpu_utilization\": \"~90%\",\n      \"timeline\": \"10-12 days with 4 concurrent A100s.\",\n      \"team\": \"0 after setup. Theory for AAAI requires human.\",\n      \"claude_api_cost\": \"$200-400 for CoRL. +$200-400 for AAAI.\",\n      \"estimated_gpu_cost\": \"CoRL: $525. AAAI: +$1,500.\",\n      \"speed_bottleneck\": \"GPU count for parallel SmolVLA fine-tuning.\",\n      \"risk_note\": \"Robometer integration straightforward (pip install + HuggingFace download). LIBERO uses existing lerobot tooling.\"\n    }\n  },\n  \"target_venues\": [\n    \"CoRL 2026 (abstract May 25, paper May 28 EOD — primary target with Robometer comparison)\",\n    \"AAAI 2027 (~August 2026 — extended with theory, OpenVLA-OFT, velocity debiasing composition)\",\n    \"ICLR 2027 (~October 2026 — most complete version, backup)\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"Prioritized Experience Replay [PER] (Schaul et al., ICLR 2016)\",\n    \"A Distributional Perspective on Reinforcement Learning (Bellemare et al., ICML 2017)\",\n    \"Distributional Reinforcement Learning with Quantile Regression (Dabney et al., AAAI 2018)\",\n    \"Diversity You Can Actually Measure [FAKTUAL] (arXiv Mar 2026, 2603.11634)\",\n    \"CUPID: Curating Data your Robot Loves with Influence Functions (CoRL 2025)\",\n    \"Robot Data Curation with Mutual Information Estimators [DemInf] (RSS 2025)\",\n    \"DataMIL: Selecting Data for Robot Imitation Learning with Datamodels (ICLR 2026)\",\n    \"Curating Demonstrations using Online Experience [Demo-SCORE] (RSS 2025)\",\n    \"SCIZOR: Self-Supervised Data Curation for Large-Scale Imitation Learning (ICRA 2026)\",\n    \"Quality over Quantity [QoQ] (arXiv Mar 2026)\",\n    \"Learning from the Best [RINSE] (ICML 2025, arXiv 2604.23000)\",\n    \"S2I: Select Segments to Imitate (ICRA 2025)\",\n    \"Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons (RSS 2026, arXiv 2603.02115)\",\n    \"Is Diversity All You Need for Scalable Robotic Manipulation? [velocity debiasing] (Modi Shi et al., arXiv Jul 2025, 2507.06219)\",\n    \"Automated regime classification via sliced Wasserstein k-means [sWk-means] (Luan and Hamp, DSFE 2025)\",\n    \"On Data Redundancy in VLA Training [TSS] (DATA-FM @ ICLR 2026)\",\n    \"Expert or not? [BWD] (arXiv Oct 2025, 2510.12638)\",\n    \"Sliced-Wasserstein Distance-based Data Selection [SWAD] (Pallage and Lesage-Landry, arXiv Apr 2025, 2504.12918)\",\n    \"Consistency Matters: Demonstration Data Quality Metrics (ACM THRI 2025)\",\n    \"Latent Wasserstein Adversarial Imitation Learning [LWAIL] (ICLR 2026, 2603.05440)\",\n    \"Temporal BT-Guided Trajectory Repair (arXiv Apr 2026, 2604.04225)\",\n    \"Optimal Transport for Offline Imitation Learning [OTR] (ICLR 2023)\",\n    \"Temporal Optimal Transport Reward (NeurIPS 2024)\",\n    \"Cross-Domain Imitation via Optimal Transport [GWIL] (ICLR 2022)\",\n    \"Watch and Match [ROT] (NeurIPS 2022)\",\n    \"Outlier-Robust Optimal Transport (Nietert et al., AISTATS 2022)\",\n    \"Robust Wasserstein Barycenter (arXiv Mar 2026)\",\n    \"k-Sparse Wasserstein Barycenter with Outliers (IJCAI 2024)\",\n    \"Barycenters in the Wasserstein Space (SIAM J. Math. Anal. 2011)\",\n    \"Lightspeed Geometric Dataset Distance [s-OTDD] (ICML 2025)\",\n    \"Minibatch Optimal Transport Distances (Fatras et al., 2021)\",\n    \"Unbalanced Minibatch Optimal Transport (Fatras et al., ICML 2021)\"\n  ],\n  \"description\": \"We propose OT-Consensus, a training-free, mode-aware method for scoring demonstration quality in robot learning datasets using optimal transport geometry, framed as the demonstration-curation analogue of Prioritized Experience Replay's TD-error scoring. Just as PER (Schaul et al., 2016) uses TD-error magnitude to identify which replay transitions deviate most from the agent's value estimate, OT-Consensus uses Sliced Wasserstein distance to the mode-specific barycenter to identify which demonstrations deviate most from their strategy mode's consensus — with inverted polarity (PER up-weights deviations for learning; OT-Consensus down-weights deviations for filtering). This framing is grounded in distributional RL theory: Bellemare et al. (2017) proved the Wasserstein metric governs distributional Bellman convergence, and we import the same metric family into demonstration curation. Each trajectory is represented as a discrete measure over visual-encoder-embedded state-action-time tuples, pairwise SW2 distances capture distributional similarity, k-medoid clustering discovers strategy modes, and distance from each mode's robust barycenter provides the quality score. This revision (round 9) incorporates three targeted changes addressing reviewer feedback: (1) Robometer added to both Tier A and Tier B evaluation — Tier A includes Spearman correlation comparison (OT-Consensus vs. Robometer-4B zero-shot on RoboMimic MH, ~15 min compute) and 5-condition downstream policy training, directly testing whether a training-free geometric scorer can match a learned scorer trained on 1M+ trajectories; Robometer code and weights are publicly released. (2) Benchmark narrowness addressed via LIBERO graceful-degradation test in Tier B — since LIBERO lacks multi-operator structure (single operator, no quality labels), it tests whether OT-Consensus degrades gracefully on single-strategy data rather than mode discovery, and whether quality-based selection outperforms random subsampling given known data redundancy. (3) PER analogy fully developed as the conceptual framing throughout core_problem, opportunity, and approach — SW2-to-barycenter as 'distributional priority score' with explicit polarity inversion, grounded in distributional RL's Wasserstein contraction (Bellemare et al., 2017), with connections to OTR and SWAD. Minimum success criterion unchanged: Spearman rho >= 0.1 above best mode-agnostic proxy AND >= 5% absolute downstream improvement.\",\n  \"project_name\": \"ot_traj_consensus\",\n  \"source\": \"web_research\"\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2af20db4-9f99-4c0b-b18f-e0eead77fc9b",
  "isSidechain": false,
  "requestId": "req_011Cb1855hgxjFthiR19KGbd",
  "type": "assistant",
  "uuid": "7ac4988d-f613-45d4-92d4-2316cc77c310",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J9trVUwRfr1Y69ZVr4Hmuz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15479,
      "cache_read_input_tokens": 35514,
      "output_tokens": 8118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15479,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8118,
          "cache_read_input_tokens": 35514,
          "cache_creation_input_tokens": 15479,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15479
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

### Tool result

_source line 25 · 2026-05-13T19:33:42.450Z_

<details><summary>↩ Tool result · reported error · `toolu_01VzTRSETwiqjWq1Qfxy4Jjs`</summary>

```text
Claude requested permissions to write to /tmp/revised_idea_round9.json, but you haven't granted it yet.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7ac4988d-f613-45d4-92d4-2316cc77c310",
  "isSidechain": false,
  "promptId": "bbda98e0-f6b9-4cc9-88b7-1263809b65cb",
  "type": "user",
  "uuid": "7c4d4c99-8e84-42e6-a8d2-a805608dc622",
  "toolUseResult": "Error: Claude requested permissions to write to /tmp/revised_idea_round9.json, but you haven't granted it yet.",
  "sourceToolAssistantUUID": "7ac4988d-f613-45d4-92d4-2316cc77c310",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-13T19:37:17.222Z_

Here is the revised idea (round 9) as a complete JSON object. This is a **minor revision** addressing the three actionable issues:

```json
{
  "change_type": "minor",
  "title": "Mode-Aware Quality Scoring for Demonstration Curation via Sliced Wasserstein Consensus",
  "core_problem": "How should we curate multimodal demonstration datasets that contain multiple valid strategies of varying quality? Diversity-maximizing approaches (FAKTUAL) improve average performance but explicitly fail when demonstrations contain conflicting strategies — blindly including diverse-but-poor demonstrations degrades learning. Quality-scoring approaches (CUPID, DataMIL) work well but require expensive policy training, validation rollouts, or influence function estimation. Learned reward models (Robometer) can score trajectory quality without a task-specific policy but require 1M+ training trajectories and are not mode-aware. Recent evidence from 'Is Diversity All You Need?' (Modi Shi et al., arXiv Jul 2025) sharpens this problem: they show that expert diversity creates *velocity multimodality* — different demonstrators executing the same spatial trajectory at different speeds — that directly degrades policy learning, producing 15% performance losses that their velocity normalization method recovers. This confirms that multi-operator demonstrations create distributional conflicts that harm learning, but their fix (velocity normalization) only addresses speed variation along shared paths, not the broader problem of scoring quality across genuinely different strategy modes. Conceptually, the challenge mirrors Prioritized Experience Replay (PER; Schaul et al., 2016) but with inverted polarity: PER uses TD-error magnitude to *up-weight* transitions that deviate from the agent's current value estimate (deviation = informative, learn more from it), while demonstration curation requires *down-weighting* trajectories that deviate from the demonstrator consensus (deviation = suspicious, filter it out). Both share the core mechanism of scoring samples by their distance from an expected distribution, but serve opposite objectives — prioritization vs. filtration. This RL-inspired framing suggests that what demonstration curation needs is a *distributional priority score* analogous to TD-error: one that measures each trajectory's deviation from expected behavior, but in a mode-aware manner that distinguishes between valid strategy diversity and genuine quality degradation. Distributional RL theory (Bellemare et al., 2017) grounds this connection formally: the distributional Bellman operator is a contraction in the p-Wasserstein metric, establishing Wasserstein distances as the natural metric family for distributional deviation in sequential decision-making. The field lacks a training-free quality scoring method that is *mode-aware* — one that discovers distinct strategy modes in the data and scores quality within each mode using distributional deviation, rather than treating all demonstrations as drawn from a single distribution.",
  "opportunity": "The demonstration curation landscape has crystallized into five camps: (1) *policy-dependent quality methods* (CUPID, DataMIL, Demo-SCORE, QoQ) that achieve SOTA but require trained policies or validation rollouts; (2) *policy-free learned quality methods* (Robometer) that train general-purpose reward models on massive trajectory datasets to score quality without a task-specific policy, but require 1M+ training trajectories for pre-training and are not mode-aware — they assign a global quality score without distinguishing between multiple valid strategies. Robometer achieves strong absolute success rates on retrieval tasks (e.g., ~95% on Stir Pot where baselines score near 0%), though the reported 4.5x average improvement is inflated by near-zero baseline performance on several tasks rather than reflecting a uniform 4.5x gain; (3) *policy-free quality proxies* (DemInf, RINSE, SCIZOR) that use scalar metrics (MI, smoothness, progress) but collapse distributional structure and are mode-agnostic; (4) *policy-free diversity methods* (FAKTUAL) that maximize trajectory entropy but explicitly acknowledge 'promoting diversity may actually be harmful when the model is not capable of capturing multimodality in the data'; and (5) *distribution normalization methods* ('Is Diversity All You Need?', Modi Shi et al., arXiv Jul 2025) that identify velocity multimodality from expert diversity as a concrete failure mode and propose velocity distribution debiasing — training a velocity model to normalize action chunk speeds, recovering 15% performance (equivalent to 2.5x pre-training data). This reveals a fundamental tension: diversity-based curation fails precisely when demonstrations are multimodal, distribution normalization removes one source of multimodality but does not score quality, learned scorers (Robometer) are powerful but mode-agnostic and require massive pre-training data, and scalar proxies collapse distributional structure. The PER analogy illuminates the gap: RL already solved the 'which samples matter?' problem for experience replay via TD-error (a *distributional deviation score*), but demonstration curation has no analogous mechanism that is both mode-aware and training-free. Recent evidence further motivates intelligent curation: 'On Data Redundancy in VLA Training' (DATA-FM @ ICLR 2026) shows that random 30% sampling of LIBERO matches full-dataset SmolVLA performance, revealing massive data redundancy — but their difficulty-based Temporal Surprise Score underperformed random selection, suggesting that naive quality proxies can be counterproductive. The key gap: no existing training-free method provides *mode-aware distributional priority scoring* — discovering strategy modes and assessing quality relative to mode-specific consensus via distributional deviation. Optimal transport geometry fills this gap naturally: Sliced Wasserstein distances define a metric space over trajectory distributions that captures shape, spread, and temporal structure; clustering in this space discovers strategy modes; and distance from each mode's robust barycenter provides a geometrically grounded, mode-aware quality score — the demonstration-curation analogue of PER's TD-error, operating in the same Wasserstein metric family that governs distributional RL convergence.",
  "landscape": "**Policy-dependent quality methods**: CUPID (CoRL 2025) uses influence functions estimating each demonstration's causal impact on closed-loop policy return, achieving SOTA on RoboMimic with <33% of curated data; requires a trained policy and evaluation rollouts. DataMIL (ICLR 2026) uses the datamodels paradigm for end-to-end policy-driven selection validated on 60+ tasks including OXE; requires surrogate loss computation with policy training. Demo-SCORE (RSS 2025) trains classifiers on online rollout success/failure to self-curate, achieving 15-35% gains; requires online robot interaction. QoQ (arXiv Mar 2026) uses influence functions with theoretical analysis but requires a validation set and scales O(n squared). **Policy-free learned quality methods**: Robometer (RSS 2026, arXiv 2603.02115) trains a general-purpose VLM-based reward model (Qwen3-VL-4B) on RBM-1M (1M+ trajectories across 21 embodiments) using a dual objective of frame-level progress supervision and trajectory-level preference learning. Achieves strong absolute success rates on retrieval tasks (e.g., ~95% on Stir Pot where baselines score near 0%), though the reported 4.5x average improvement is inflated by near-zero baseline performance on several tasks rather than reflecting a uniform 4.5x gain. However, Robometer (a) requires 1M+ training trajectories (~6TB) for pre-training — infeasible when curating smaller datasets without pre-existing large-scale data; (b) is NOT mode-aware — it assigns a single global quality score per trajectory without distinguishing between multiple valid strategies; (c) was not evaluated on RoboMimic or against demonstration curation methods (CUPID, DemInf, RINSE, SCIZOR, FAKTUAL) — its comparisons are against VLM reward models (RoboReward, GVL, VLAC). Robometer code and model weights (Robometer-4B) are publicly released on GitHub (github.com/robometer/robometer) and HuggingFace (robometer/Robometer-4B), enabling direct zero-shot comparison on RoboMimic MH. A LIBERO-fine-tuned variant (Robometer-LIBERO) is also available. OT-Consensus is complementary: training-free, mode-aware, and geometric, requiring no pre-training data. **Policy-free quality proxies**: DemInf (RSS 2025) estimates trajectory-level mutual information between states and actions via k-NN estimators with VAE embeddings, achieving 5-10% gains on RoboMimic; captures information content but collapses distributional structure to a scalar and is mode-agnostic. RINSE (ICML 2025, arXiv 2604.23000) uses Spectral Arc Length (SAL) and Trajectory-Envelope Distance (TED) smoothness metrics achieving 16-20% success gains; assumes smoothness universally correlates with quality, failing for tasks where jerky motions are correct. SCIZOR (ICRA 2026) combines self-supervised task progress prediction with deduplication, achieving 15.4% average improvement across RoboMimic/OXE/Sirius-Fleet; no theoretical guarantees and conflates lack of progress with low quality. S2I (ICRA 2025) performs segment-level selection using contrastive learning with 3 expert reference demonstrations; requires expert references and cannot operate fully unsupervised. Consistency Matters (ACM THRI 2025) proposes 10 motion-based consistency metrics with 76-91% success prediction accuracy; limited to geometric consistency without distributional analysis. **Policy-free diversity methods**: FAKTUAL (arXiv Mar 2026, 2603.11634) uses signature kernel entropy for diversity-based curation; fully model-free and tested on RoboMimic MH and MetaWorld. Compared against CUPID, DemInf, and Demo-SCORE. FAKTUAL performs modestly above random but below quality-based methods, and *explicitly acknowledges* that 'promoting diversity may actually be harmful when the model is not capable of capturing multimodality in the data.' NOTE: As of May 2026, FAKTUAL code is not publicly released; FPS fallback available. **Distribution normalization methods**: 'Is Diversity All You Need for Scalable Robotic Manipulation?' (Modi Shi et al., arXiv Jul 2025, 2507.06219) identifies velocity multimodality from expert diversity as a concrete failure mode and proposes velocity distribution debiasing, yielding 15% gains. Validates the core premise that multi-operator demonstrations create distributional conflicts, but addresses only velocity variation along shared paths. **RL-inspired scoring connections**: Prioritized Experience Replay (PER; Schaul et al., ICLR 2016) established TD-error magnitude as a distributional deviation score for sample prioritization — the conceptual precursor to OT-Consensus's mode-aware quality scoring. OTR (ICLR 2023) uses OT to score offline trajectories by alignment to expert demonstrations — reward assignment via OT, not curation. SWAD (Pallage and Lesage-Landry, arXiv Apr 2025, 2504.12918) uses sliced-Wasserstein distance to barycenters for unsupervised anomaly detection on i.i.d. tabular data — the closest methodological precursor in general ML, but operates on individual data points rather than trajectory measures. Distributional RL theory (Bellemare et al., ICML 2017) proved Wasserstein contraction of the distributional Bellman operator, establishing OT as the natural metric family for distributional analysis in sequential decision-making. Distributional RL with Quantile Regression (Dabney et al., AAAI 2018) closed the theory-practice gap by directly minimizing 1-Wasserstein distance. **OT-based quality/distance methods (adjacent)**: sWk-means (Luan and Hamp, DSFE 2025) uses sliced Wasserstein distances + k-means clustering for financial regime detection — a methodological precursor to OT-Consensus's first two steps, but without barycenters, quality scoring, or trajectory representations. BWD/'Expert or not?' (arXiv Oct 2025) introduces Bellman Wasserstein Distance requiring a behavioral critic. LWAIL (ICLR 2026) uses Wasserstein for state-only distribution matching in adversarial IL policy learning. **Data redundancy in VLA training**: 'On Data Redundancy in VLA Training' (DATA-FM Workshop @ ICLR 2026) shows random 30% sampling of LIBERO matches full-dataset SmolVLA performance; Temporal Surprise Score underperforms random selection. **OT in robot learning (not curation)**: OTR (ICLR 2023), Temporal OT Reward (NeurIPS 2024), GWIL (ICLR 2022), ROT (NeurIPS 2022). **OT theory**: Robust Wasserstein Barycenter (arXiv Mar 2026), Outlier-Robust OT (Nietert et al., AISTATS 2022), k-Sparse Wasserstein Barycenter with Outliers (IJCAI 2024), s-OTDD (ICML 2025). **Gap**: No existing method provides training-free, mode-aware distributional priority scoring for demonstration quality. FAKTUAL is mode-agnostic diversity; DemInf/RINSE/SCIZOR are mode-agnostic scalar proxies; Robometer is a powerful learned scorer but not mode-aware and requires 1M+ trajectories; CUPID/DataMIL are mode-aware in principle but policy-dependent; sWk-means stops at regime identification; SWAD uses SW-to-barycenter on i.i.d. points, not trajectory measures; velocity debiasing normalizes speed but does not score quality. OT-Consensus uniquely combines mode awareness, distributional priority scoring, and training-free operation.",
  "approach": "**Overview**: OT-Consensus is a training-free, mode-aware demonstration quality scoring method. We reframe the demonstration curation problem through the lens of RL-inspired distributional priority scoring: just as PER (Schaul et al., 2016) scores replay transitions by TD-error magnitude — their deviation from the agent's value estimate — OT-Consensus scores demonstrations by their Sliced Wasserstein distance from the mode-specific barycenter — their distributional deviation from demonstrator consensus. The polarity is inverted: PER up-weights high-deviation samples (surprise = informative), while OT-Consensus down-weights high-deviation demonstrations (deviation = suspicious quality). Both operate via the same mechanism — measuring distributional deviation to score sample utility — grounded in the Wasserstein metric family that governs distributional RL convergence (Bellemare et al., 2017). The core conceptual contribution is that demonstration quality should be assessed as *distributional priority within each strategy mode*, not as global diversity or scalar proxy. This extends the SW+clustering pipeline introduced by sWk-means (Luan and Hamp, DSFE 2025) from financial regime detection to robot demonstration curation, with three key additions: robust barycenters for quality scoring, trajectory-as-measure representation, and mode-aware filtering. We target a focused empirical contribution for CoRL 2026 with formal theoretical analysis deferred.\n\n**Day 1 Validation Gate (May 13 — before committing to the full sprint)**: Two preliminary experiments (~4h total). (a) *Synthetic toy*: 200 2D trajectories, 2 modes x 3 quality tiers. Verify k=2 recovers modes (ARI >= 0.8) and within-mode SW2-to-barycenter correlates with quality (Spearman rho >= 0.5). Show MI and smoothness metrics fail to distinguish within-mode quality. (b) *RoboMimic pilot*: 50 trajectories from MH Can, k-medoid with k=3 and k=6, ARI against operator/proficiency labels. (c) *Gate*: Proceed if synthetic ARI >= 0.8 AND rho >= 0.5, AND RoboMimic ARI >= 0.1.\n\n**FAKTUAL Reproduction Plan**: Code not released. Mitigation: contact authors May 13; reimplementation via KSig May 14-15; FPS fallback decision May 16.\n\n**Representation design**: Each trajectory mapped to a discrete measure over (visual_embedding, action, normalized_time) tuples. Ground metric: weighted sum of squared distances. Default encoder: SigLIP-SO400M (SmolVLA's own encoder — quality scored in policy-relevant space). DINOv2 ablation proves generalization.\n\n**Scalable pairwise distances**: SW2 with O(Ln log n) per pair, L=50-200 projections. N-squared matrix for 300 demos ~15 min on A100.\n\n**Mode discovery and quality scoring**: (1) SW2 pairwise distance matrix. (2) k-medoid clustering (PAM); k via silhouette over {2,...,8}. (3) Robust barycenter per cluster via trimmed-mean OT (epsilon=0.1). (4) Quality score: q_i = 1 / (1 + SW2(mu_i, beta_m)), normalized to [0,1]. This is the *distributional priority score* — the curation analogue of PER's TD-error.\n\n**Relationship to PER and distributional RL**: The SW2-to-barycenter score has a precise structural analogy to TD-error priority. Both measure sample deviation from a distributional reference (value estimate for PER; mode barycenter for OT-Consensus). The polarity inversion (PER: high deviation -> up-weight for learning; OT-Consensus: high deviation -> down-weight for filtering) reflects the difference between learning from surprise (RL) and filtering for consensus (curation). Formally, distributional RL's Wasserstein contraction (Bellemare et al., 2017) established that the p-Wasserstein metric governs convergence of return distributions under the Bellman operator — OT-Consensus imports the same metric family into demonstration curation. This connection extends prior work: OTR (Luo et al., ICLR 2023) uses OT to assign reward scores to offline trajectories, and SWAD (Pallage and Lesage-Landry, 2025) uses SW-distance-to-barycenter for anomaly detection in general data selection. OT-Consensus extends these with mode-aware clustering and trajectory-as-measure representations.\n\n**Hypothesis H3 (vs. Robometer)**: Robometer assigns a single global quality score per trajectory via a VLM trained on 1M+ trajectories. When demonstrations contain multiple valid strategies, Robometer may penalize trajectories from minority strategies that deviate from the majority pattern, even if those trajectories are high-quality within their strategy mode. OT-Consensus first discovers modes, then scores within each — a trajectory is judged against its own strategy's consensus, not the global population. Prediction: on RoboMimic MH, OT-Consensus's mode-aware scoring achieves comparable or higher Spearman correlation with operator proficiency than Robometer, and specifically preserves high-quality trajectories from minority strategy modes that Robometer may underrate.\n\n**Mode discovery analysis**: Expected k=3 (proficiency) or k=6 (operators). With N=300, minimum cluster size exceeds 40+2k guideline. Sensitivity: Spearman rho vs. proficiency for k in {2,...,8}.\n\n**Minimum success criterion**: Spearman rho >= 0.1 above best mode-agnostic proxy AND >= 5% absolute downstream success rate improvement over best policy-free baseline.\n\n**Evaluation design — two tiers**:\n\n**Tier A (Minimal Viable Paper — commit by May 21)**:\n(a) *Day 1 validation gate* (May 13): Synthetic toy + RoboMimic pilot (~4h).\n(b) *Quality metric comparison*: Compute 5 scores on all 300 RoboMimic MH demos: OT-Consensus, Robometer-4B (zero-shot, using publicly released model weights — Robometer was never evaluated on RoboMimic, making this a fair comparison), diversity baseline (FAKTUAL or FPS), DemInf (MI), and random. Robometer scoring: ~15 min on A100 via forward passes through Qwen3-VL-4B on extracted image observations; no training or fine-tuning. Evaluate Spearman correlation with operator proficiency, AUC for Better-vs-Worse separation. This directly tests the central claim: can a training-free geometric scorer match a learned scorer trained on 1M+ trajectories? Analyze mode-awareness: does Robometer penalize minority-strategy high-quality demos that OT-Consensus correctly scores?\n(c) *Downstream policy performance*: SmolVLA (450M) on filtered subsets (top-50%) on 2 tasks (Can, Square) x 5 conditions (OT-Consensus, Robometer, diversity baseline, DemInf, random) x 2 seeds = 20 runs (~80h).\n(d) *Ablations*: SigLIP vs. DINOv2 encoder (4 runs, ~16h). k sensitivity (no additional GPU).\n\n**Tier B (Full Paper — expand if on track by May 21)**:\nAdd RINSE and SCIZOR conditions (7 total); add Lift and Transport tasks (4 total); increase to 3 seeds; add top-33% threshold. *LIBERO graceful-degradation test*: Compute OT-Consensus and Robometer scores on 1-2 LIBERO tasks and run downstream SmolVLA comparison. LIBERO demonstrations come from a single operator without multi-operator structure or quality labels, so this tests *graceful degradation* — whether OT-Consensus's quality scoring (with k=1, single mode) still provides useful signal via distance-from-barycenter filtering on single-strategy data, rather than over-clustering homogeneous data. Compare against known data redundancy (DATA-FM: random 30% matches full-dataset). Use Robometer-LIBERO (fine-tuned variant, publicly available) for strongest possible learned baseline on LIBERO. Additional ablations (SW2 vs. embedding k-means; ground metric weights; projection count).\n\n**Extended version (AAAI 2027)**: OpenVLA-OFT (7B), additional LIBERO tasks, formal theory, CUPID/S2I baselines, velocity debiasing composition, comprehensive ablations.\n\n**Parallel writing plan**: Days 1-3: intro (PER framing) + related work. Days 4-8: method + results. Days 9-10: analysis + ablations. Days 11-16: revision + submission.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~250h A100 for CoRL Tier A (Day 1 gate: ~4h; SW2 matrix: ~8h; barycenters: ~4h; Robometer scoring: ~0.5h; FAKTUAL/FPS: ~20h; SmolVLA: ~4h/run x 20 runs = 80h; DINOv2 ablation: ~16h; eval rollouts: ~4h; buffer: ~30h). Tier B adds ~160h (extra conditions, tasks, seeds, LIBERO). AAAI adds ~700h.",
      "gpu_utilization": "~75% for CoRL sprint.",
      "timeline": "CoRL 2026: 16-day sprint (May 13-28). Day 1: validation gate + Robometer setup. Days 2-3: full SW2 matrix + Robometer scoring on 300 demos + FAKTUAL attempt + draft intro/related work. Day 4: FAKTUAL decision. Days 4-8: Tier A SmolVLA training (5 conditions) + method draft. Days 9-10: evaluation + analysis + results draft. Tier A commit: May 21. Days 11-12: Tier B expansion + revision. Day 13: abstract submission (May 25). Days 14-16: final submission by May 28 EOD.",
      "team": "CoRL: 1 researcher full-time. AAAI: +1 collaborator for theory.",
      "estimated_gpu_cost": "Tier A: $375. Tier B: +$240. AAAI: +$1,050. Total: $1,665."
    },
    "human_in_loop": {
      "gpu_hours": "~230h A100 for CoRL Tier A",
      "gpu_utilization": "~85% — agent handles SW2 pipeline, Robometer integration, SmolVLA orchestration; human focuses on analysis and writing",
      "timeline": "CoRL: 16 days. Day 1: human analyzes gate + go/no-go. Days 2-16: agent-driven with checkpoints at FAKTUAL decision (Day 4) and Tier A commit (Day 10).",
      "team": "1 researcher, ~4-5h/day; agent handles implementation",
      "claude_api_cost": "$100-200 for CoRL. +$150-300 for AAAI.",
      "estimated_gpu_cost": "Tier A: $345. Tier B: +$150. AAAI: +$900.",
      "risk_note": "Robometer integration is low-risk: code/weights public, scoring ~15 min, adds only 4 downstream runs. LIBERO is Tier B only and uses existing lerobot tooling. Key risk remains FAKTUAL code — mitigated by FPS fallback."
    },
    "auto_research": {
      "gpu_hours": "~350h A100 for CoRL Tier A+B",
      "gpu_utilization": "~90%",
      "timeline": "10-12 days with 4 concurrent A100s.",
      "team": "0 after setup. Theory for AAAI requires human.",
      "claude_api_cost": "$200-400 for CoRL. +$200-400 for AAAI.",
      "estimated_gpu_cost": "CoRL: $525. AAAI: +$1,500.",
      "speed_bottleneck": "GPU count for parallel SmolVLA fine-tuning.",
      "risk_note": "Robometer integration straightforward (pip install + HuggingFace download). LIBERO uses existing lerobot tooling."
    }
  },
  "target_venues": [
    "CoRL 2026 (abstract May 25, paper May 28 EOD — primary target with Robometer comparison)",
    "AAAI 2027 (~August 2026 — extended with theory, OpenVLA-OFT, velocity debiasing composition)",
    "ICLR 2027 (~October 2026 — most complete version, backup)"
  ],
  "level": "top-tier",
  "key_references": [
    "Prioritized Experience Replay [PER] (Schaul et al., ICLR 2016)",
    "A Distributional Perspective on Reinforcement Learning (Bellemare et al., ICML 2017)",
    "Distributional Reinforcement Learning with Quantile Regression (Dabney et al., AAAI 2018)",
    "Diversity You Can Actually Measure [FAKTUAL] (arXiv Mar 2026, 2603.11634)",
    "CUPID: Curating Data your Robot Loves with Influence Functions (CoRL 2025)",
    "Robot Data Curation with Mutual Information Estimators [DemInf] (RSS 2025)",
    "DataMIL: Selecting Data for Robot Imitation Learning with Datamodels (ICLR 2026)",
    "Curating Demonstrations using Online Experience [Demo-SCORE] (RSS 2025)",
    "SCIZOR: Self-Supervised Data Curation for Large-Scale Imitation Learning (ICRA 2026)",
    "Quality over Quantity [QoQ] (arXiv Mar 2026)",
    "Learning from the Best [RINSE] (ICML 2025, arXiv 2604.23000)",
    "S2I: Select Segments to Imitate (ICRA 2025)",
    "Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons (RSS 2026, arXiv 2603.02115)",
    "Is Diversity All You Need for Scalable Robotic Manipulation? [velocity debiasing] (Modi Shi et al., arXiv Jul 2025, 2507.06219)",
    "Automated regime classification via sliced Wasserstein k-means [sWk-means] (Luan and Hamp, DSFE 2025)",
    "On Data Redundancy in VLA Training [TSS] (DATA-FM @ ICLR 2026)",
    "Expert or not? [BWD] (arXiv Oct 2025, 2510.12638)",
    "Sliced-Wasserstein Distance-based Data Selection [SWAD] (Pallage and Lesage-Landry, arXiv Apr 2025, 2504.12918)",
    "Consistency Matters: Demonstration Data Quality Metrics (ACM THRI 2025)",
    "Latent Wasserstein Adversarial Imitation Learning [LWAIL] (ICLR 2026, 2603.05440)",
    "Temporal BT-Guided Trajectory Repair (arXiv Apr 2026, 2604.04225)",
    "Optimal Transport for Offline Imitation Learning [OTR] (ICLR 2023)",
    "Temporal Optimal Transport Reward (NeurIPS 2024)",
    "Cross-Domain Imitation via Optimal Transport [GWIL] (ICLR 2022)",
    "Watch and Match [ROT] (NeurIPS 2022)",
    "Outlier-Robust Optimal Transport (Nietert et al., AISTATS 2022)",
    "Robust Wasserstein Barycenter (arXiv Mar 2026)",
    "k-Sparse Wasserstein Barycenter with Outliers (IJCAI 2024)",
    "Barycenters in the Wasserstein Space (SIAM J. Math. Anal. 2011)",
    "Lightspeed Geometric Dataset Distance [s-OTDD] (ICML 2025)",
    "Minibatch Optimal Transport Distances (Fatras et al., 2021)",
    "Unbalanced Minibatch Optimal Transport (Fatras et al., ICML 2021)"
  ],
  "description": "We propose OT-Consensus, a training-free, mode-aware method for scoring demonstration quality in robot learning datasets using optimal transport geometry, framed as the demonstration-curation analogue of Prioritized Experience Replay's TD-error scoring. Just as PER (Schaul et al., 2016) uses TD-error magnitude to identify which replay transitions deviate most from the agent's value estimate, OT-Consensus uses Sliced Wasserstein distance to the mode-specific barycenter to identify which demonstrations deviate most from their strategy mode's consensus — with inverted polarity (PER up-weights deviations for learning; OT-Consensus down-weights deviations for filtering). This framing is grounded in distributional RL theory: Bellemare et al. (2017) proved the Wasserstein metric governs distributional Bellman convergence, and we import the same metric family into demonstration curation. Each trajectory is represented as a discrete measure over visual-encoder-embedded state-action-time tuples, pairwise SW2 distances capture distributional similarity, k-medoid clustering discovers strategy modes, and distance from each mode's robust barycenter provides the quality score. This revision (round 9) incorporates three targeted changes addressing reviewer feedback: (1) Robometer added to both Tier A and Tier B evaluation — Tier A includes Spearman correlation comparison (OT-Consensus vs. Robometer-4B zero-shot on RoboMimic MH, ~15 min compute) and 5-condition downstream policy training, directly testing whether a training-free geometric scorer can match a learned scorer trained on 1M+ trajectories; Robometer code and weights are publicly released. (2) Benchmark narrowness addressed via LIBERO graceful-degradation test in Tier B — since LIBERO lacks multi-operator structure (single operator, no quality labels), it tests whether OT-Consensus degrades gracefully on single-strategy data rather than mode discovery, and whether quality-based selection outperforms random subsampling given known data redundancy. (3) PER analogy fully developed as the conceptual framing throughout core_problem, opportunity, and approach — SW2-to-barycenter as 'distributional priority score' with explicit polarity inversion, grounded in distributional RL's Wasserstein contraction (Bellemare et al., 2017), with connections to OTR and SWAD. Minimum success criterion unchanged: Spearman rho >= 0.1 above best mode-agnostic proxy AND >= 5% absolute downstream improvement.",
  "project_name": "ot_traj_consensus",
  "source": "web_research"
}
```

## Summary of changes (round 9)

**Three targeted revisions addressing reviewer feedback:**

1. **Robometer added to evaluation** (most impactful change): Robometer-4B code and weights are publicly released on GitHub/HuggingFace. Scoring 300 RoboMimic MH demos takes ~15 min on A100 (zero-shot, no training). Added to Tier A as both a correlation comparison (Spearman with operator proficiency) and a 5th downstream condition. New hypothesis H3 explicitly predicts OT-Consensus's mode-aware advantage: Robometer may penalize minority-strategy trajectories that OT-Consensus correctly scores within their mode. This is the single strongest addition — if OT-Consensus matches a 4B VLM trained on 1M+ trajectories without any training, that's a compelling contribution.

2. **LIBERO reframed as graceful-degradation test** (Tier B): Research revealed LIBERO lacks multi-operator structure (single operator, ~50 demos/task, no quality labels) — it cannot test mode discovery. Instead of forcing an inappropriate experiment, LIBERO is positioned as a *graceful degradation* test: does OT-Consensus (with k=1) still provide useful signal on single-strategy data? This honestly addresses benchmark narrowness while respecting the method's requirements. Robometer-LIBERO (fine-tuned variant) serves as the strongest learned baseline.

3. **PER analogy fully developed**: The "distributional priority score" framing is woven throughout core_problem, opportunity, and approach with the explicit polarity inversion (PER: high deviation → up-weight; OT-Consensus: high deviation → down-weight). Grounded in distributional RL's Wasserstein contraction (Bellemare et al., 2017) and connected to OTR and SWAD as methodological precursors. Three new key references added (PER, Bellemare 2017, Dabney 2018).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c4d4c99-8e84-42e6-a8d2-a805608dc622",
  "isSidechain": false,
  "requestId": "req_011Cb18LAaoLux1YUsxdxG1z",
  "type": "assistant",
  "uuid": "e1f08f07-40a5-4ab7-83a3-f3b4b40f70d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015qAS6wVYktnrCGsLr5Ri4h",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8163,
      "cache_read_input_tokens": 50993,
      "output_tokens": 8543,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8163,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8543,
          "cache_read_input_tokens": 50993,
          "cache_creation_input_tokens": 8163,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8163
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

### Runtime record

_source line 27_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-13 (UTC).**  ## Original idea {   \"title\": \"Mode-Aware Quality Scoring for Demonstration Curation via Sliced Wasse…",
  "leafUuid": "e1f08f07-40a5-4ab7-83a3-f3b4b40f70d5",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Mode-aware quality scoring for demonstrations via sliced Wasserstein consensus",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-13 (UTC).**  ## Original idea {   \"title\": \"Mode-Aware Quality Scoring for Demonstration Curation via Sliced Wasse…",
  "leafUuid": "e1f08f07-40a5-4ab7-83a3-f3b4b40f70d5",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Mode-aware quality scoring for demonstrations via sliced Wasserstein consensus",
  "sessionId": "4b2e93a9-7a45-4028-badc-913d53ffd7bb"
}
```

---
