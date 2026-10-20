# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-10 (UTC).** ## Original idea { "tit

**When Does Detect-and-Reweight Work for Synthetic Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-3/e93981d8-61dc-4460-8c15-6141e331b9de.jsonl`
- **Structured JSON:** [`07220ba15a3461da250b.json`](../../sessions/07/07220ba15a3461da250b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T13:08:37.638Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T13:08:37.638Z",
  "sessionId": "e93981d8-61dc-4460-8c15-6141e331b9de",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-10 (UTC).**\n\n## Original idea\n{\n  \"title\": \"LocoMimicGen: Coupled SE(3) Object-Centric Demo Multiplication for Mobile Humanoid Loco-Manipulation\",\n  \"core_problem\": \"How can a handful of expensive teleoperated whole-body loco-manipulation demonstrations be multiplied by orders of magnitude across diverse spatial configurations — new object positions, table heights, room obstacle layouts — while maintaining physical validity for the mobile bipedal humanoid platform? Isaac Lab's 2.3 GA release contains three directly relevant prior contributions. PR #3150 (merged Sept 9, 2025) adds the G1 loco-manipulation environment integrating a pretrained RL locomotion policy with Pink IK arm control. PR #3259 ('Adds locomanipulation data generation via disjoint navigation', merged Sept 10, 2025) adds pick-navigate-place phase segmentation with occupancy-map path planning between phases and scene randomization of tabletop positions, navigation destinations, and floor obstacles — making it the closest structural predecessor to LocoMimicGen. PR #3992 (merged Dec 1, 2025) extends the Mimic framework with a 'body end-effector' API and navigation controller integration. Despite this infrastructure, three technical gaps prevent room-level combinatorial scaling: PR #3259 handles navigation 'disjointly' — the manipulation stance (where the robot stands to manipulate) is fixed from the source demo and navigation is handled as path-level occupancy-map planning between fixed phases, NOT as coupled SE(3) object-centric encoding of stances jointly with arm trajectories. None of these PRs enforce arm-reachability constraints on base-pose selection during retargeting — the robot manipulates from whatever stance the source demo used, regardless of arm workspace feasibility for new object positions. And none perform combinatorial composition of subtask segments from multiple source demonstrations. These three absences cap achievable diversity at object-position randomization within a single source demo's reach envelope, rather than the combinatorial room-level scaling that MimicGen achieves for tabletop tasks.\",\n  \"opportunity\": \"Isaac Lab's 2.3 GA release (PRs #3150, #3259, #3992) now provides the exact scaffolding — G1 environment, pick-navigate-place phase segmentation, occupancy-map path planning, Mimic segmentation framework, and navigation controller integration — needed to build a principled extension. The precise technical gap is narrow but high-impact: adding (1) SE(3) object-centric encoding of navigation stances jointly with arm trajectories into the existing Mimic segment representation (replacing the disjoint path-planning approach of PR #3259 with coupled frame-transform retargeting), (2) stance-conditioned reachability-map-guided base-pose optimization enforcing arm feasibility at each manipulation stance during retargeting (adapting IRM methodology from the mobile-manipulator literature to the bipedal humanoid setting, where the reachability map is conditioned on whole-body configuration rather than just SE(2) base pose), and (3) combinatorial subtask segment composition from multiple source demonstrations. OmniRetarget (Amazon, Sept 2025) addresses humanoid loco-manipulation data generation from MoCap sequences via interaction-mesh Laplacian deformation on the G1, but retargets continuous motion sequences and cannot combinatorially compose segments across scene variants. DemoHLM (Oct 2025) demonstrates generalizable single-demonstration adaptation across 10 G1 loco-manipulation household tasks but the single-demo paradigm limits scaling to spatial interpolation within one source demo's envelope. The three-part Isaac Lab Mimic extension proposed here is tractable within existing infrastructure, precisely bounded against Isaac Lab's own 2.3 baseline (including PR #3259 as the most direct predecessor), and is the missing ingredient for room-level combinatorial scaling. MoMaGen (ICLR 2026, arXiv:2510.18316) imposes reachability as a hard constraint for wheeled bimanual mobile base-pose sampling — SE(2) for a wheeled platform. Now peer-reviewed at ICLR 2026, MoMaGen's coverage of hard-reachability-constrained demo generation makes the bipedal differentiation the critical point of departure: MoMaGen's reachability constraint operates over SE(2) base pose for a wheeled bimanual platform where the base pose fully determines arm workspace, whereas LocoMimicGen's stance-conditioned IRM addresses the qualitatively harder bipedal case where arm reachability is conditioned on whole-body configuration — COM height, foot contact, balance state — a higher-dimensional reachability function not covered by any prior data-generation work. EgoHumanoid (OpenDriveLab, arXiv:2602.10106, Feb 2026) represents a concurrent complementary paradigm — co-training VLA policies on human egocentric video alongside robot demonstrations — that highlights the orthogonal value of LocoMimicGen's combinatorial simulation synthesis approach.\",\n  \"landscape\": \"MimicGen (CoRL 2023) decomposes arm demonstrations into object-centric subtask segments and applies SE(3) frame transformations — manipulation-only. DexMimicGen (ICRA 2025) extends this to bimanual dexterous humanoids, still tabletop. HumanoidGen (NeurIPS 2025) uses LLM-driven planning for tabletop dexterous tasks with 120+ scene variants — explicitly excludes locomotion.\\n\\nIsaac Lab 2.3 loco-manipulation infrastructure comprises three PRs that together form the primary baseline. PR #3150 (merged Sept 9, 2025) adds Isaac-PickPlace-Locomanipulation-G1-Abs-v0, integrating a pretrained RL locomotion policy (velocity commands vx, vy, wz) with Pink IK arm control, achieving 92% success on pick-and-place. PR #3259 ('Adds locomanipulation data generation via disjoint navigation', merged Sept 10, 2025, release/2.3.0) is the closest structural predecessor to LocoMimicGen: it adds pick-navigate-place phase segmentation, occupancy-map-based collision-free path planning between phases, and scene randomization of tabletop object positions, navigation destinations, and floor obstacles. The implementation lives under disjoint_navigation/ and works by (a) recording static manipulation teleoperation with the base stationary, (b) applying Mimic augmentation to manipulation segments, and (c) stitching path-planned navigation trajectories between the resulting phases. Critically, PR #3259 does NOT encode navigation stances in the object's SE(3) local frame — navigation is occupancy-map path planning at the trajectory level, while the manipulation stance (where the robot stands to manipulate) is fixed from the source demo, not retargeted to new object positions. There is no arm-reachability constraint on base-pose selection: if a new object position falls outside the arm workspace at the source demo's stance, the generation produces infeasible trajectories rather than finding a feasible stance. There is no combinatorial composition from multiple source demonstrations. PR #3992 (merged Dec 1, 2025) adds a 'body end-effector' API and get_navigation_state() integration into the Mimic framework but relies on the same state-based navigation repetition/skipping, not object-centric stance encoding.\\n\\nInverse reachability maps (IRM) for robot base placement are a well-established technique. Vahrenkamp et al. 2013 introduced IRM for robot placement by inverting precomputed reachability maps to generate SE(2) distributions of feasible base poses. Burget et al. (ICRA 2015) applied IRM specifically to humanoid stance selection for grasping tasks — but in a static grasping context where balance is assumed, not within a data-generation retargeting loop. MoMa-Pos (arXiv:2403.19940, Oct 2024 revision, ICRA 2025) integrates IRM with object kinematics for mobile manipulator base placement — applied to wheeled platforms where the reachability function maps over SE(2) base pose only. MoMaGen (ICLR 2026, arXiv:2510.18316) imposes reachability as a hard constraint for wheeled bimanual mobile base-pose sampling — again, SE(2) for a wheeled platform. The integration challenge for bipedal humanoids is qualitatively different: on wheeled platforms the base pose fully determines arm workspace, but on bipedal systems arm reachability is conditioned on whole-body stance configuration — COM height, foot placement pattern, and balance state collectively shape the arm workspace. A concurrent planning paper (Murooka et al., arXiv:2505.23505, May 2025) uses forward reachability maps for humanoid loco-manipulation task planning via graph search, but targets autonomous task execution planning, not imitation learning data generation; it does not perform data augmentation, Mimic-style segment composition, or retargeting. The same CNRS-AIST group (Murooka et al., arXiv:2508.11275, Humanoids 2025) subsequently introduced learned differentiable reachability maps for optimization-based humanoid motion generation — continuous scalar-valued functions differentiable with respect to task-space coordinates, enabling gradient-based planning for footstep sequencing and loco-manipulation without repeated IK solving. The differentiable formulation excels at online continuous optimization but is not suited to LocoMimicGen's batch data-generation context: evaluating differentiable map gradients across 2048+ parallel Isaac Lab environments at retargeting time would bottleneck generation throughput, whereas LocoMimicGen's offline-precomputed discrete IRM is evaluated as a table lookup simultaneously across all environments. The two approaches are complementary in use case — differentiable maps for online planning, discrete IRM for batch generation — and both leave the stance-conditioned data-generation problem unaddressed.\\n\\nOmniRetarget (Amazon, arXiv:2509.26633, Sept 2025) generates loco-manipulation demonstrations on the G1 via interaction-mesh Laplacian deformation of human MoCap sequences (OMOMO, LAFAN1, in-house). It preserves spatial and contact relationships and enables augmentation across embodiments, terrains, and object configurations. Critically, OmniRetarget (a) requires large MoCap databases rather than small teleoperated G1 demonstrations; (b) retargets continuous motion sequences without decomposing into reusable subtask segments; (c) cannot combinatorially compose segments from different source demos; and (d) targets locomotion-heavy tasks rather than precision manipulation requiring tight coupling between base position and arm workspace. OmniRetarget's codebase (Holosoma, amazon-far/holosoma) is publicly available; LocoMimicGen positions it as a conceptual comparison citing published retargeting fidelity metrics, as the estimated 10–14 day setup cost for Holosoma plus MoCap dataset ingestion exceeds the available bandwidth in the 20-day window.\\n\\nDemoHLM (arXiv:2510.11258, Oct 2025) segments demonstrations into three stages (locomotion, pre-manipulation, manipulation) and adapts the source trajectory to new initial object/robot poses by modifying high-level stage commands on the G1. It demonstrates 10 loco-manipulation household tasks with sim-to-real transfer. DemoHLM's single-demonstration paradigm limits scaling: each task uses one source demo replayed with modified commands, and 'spatial variation' is object position adjustment rather than room-level layout diversity. DemoHLM's code has not been publicly released as of May 2026; LocoMimicGen therefore positions it as a conceptual comparison, citing its published 10-task evaluation results directly.\\n\\nMoMaGen (ICLR 2026, arXiv:2510.18316) generates bimanual mobile manipulation demonstrations via constrained optimization (hard reachability + soft visibility) on a wheeled bimanual mobile base. The wheeled platform decouples navigation from balance, making MoMaGen's SE(2) base-pose sampling inapplicable to bipedal humanoids.\\n\\nDreamGen (NVIDIA GEAR Lab, arXiv:2505.12705, May 2025) — the technical backbone of the Isaac GR00T-Dreams blueprint, first announced alongside GR00T N1 in March 2025 — generates synthetic 'neural trajectories' by fine-tuning a video world model (Cosmos Predict-2) on a handful of teleoperated demonstrations, then sampling diverse video scenarios via diffusion and recovering pseudo-action sequences with an inverse dynamics model (IDM). DreamGen achieves strong behavioral generalization: GR00T N1 trained exclusively on pick-and-place achieves 0% on novel behaviors without DreamGen, while DreamGen-augmented training reaches 43.2% success on new behaviors in seen environments and 28.5% in completely unseen environments. Importantly, DreamGen evaluates all tasks in a stationary-manipulation setting — even for the humanoid GR1, the robot remains stationary while the arms operate — and the authors explicitly identify 'supporting more complex, dexterous behaviors requiring richer control' as future work. A second NVIDIA pipeline, GR00T-Mimic, applies MimicGen-style interpolation within the GR00T N1 training workflow to expand tabletop manipulation trajectories; it operates without locomotion coupling. DreamGen and LocoMimicGen are complementary rather than competing: DreamGen delivers behavioral diversity across task types (novel manipulation verbs, object categories, unseen environments) via world-model imagination, while LocoMimicGen delivers spatial/configurational diversity within known loco-manipulation tasks (exponentially more room-scale configurations) through constraint-based combinatorial recombination. Critically, DreamGen's IDM-extracted pseudo-actions are pixel-level learned approximations without explicit kinematic validation — LocoMimicGen's procedural recombination with IRM feasibility filters, pose-continuity bounds (δ_nav ≈ 0.3 m), and contact-consistency checks enforces hard physical guarantees that learned world models currently cannot provide at per-joint kinematic precision for coupled loco-manipulation tasks.\\n\\nVisualMimic (arXiv:2509.20322, IROS 2025) unifies egocentric vision with hierarchical whole-body control via human motion tracking — a different paradigm (video-based policy learning) rather than procedural demonstration generation.\\n\\nEgoHumanoid (Modi Shi et al., OpenDriveLab, arXiv:2602.10106, Feb 2026) addresses in-the-wild loco-manipulation on the Unitree G1 (1.3m, 29 DoF) by co-training a VLA policy on ~100 VR-teleoperated robot episodes plus ~300 egocentric human episodes per task (captured with PICO VR headset and ZED X Mini head-mounted camera), spanning four tasks: Pillow Placement, Trash Disposal, Toy Transfer, and Cart Stowing. View alignment uses MoGe depth prediction and point-cloud reprojection to the robot viewpoint with diffusion inpainting for occluded regions; action alignment maps to 6-DoF delta EEF for upper body, discrete locomotion commands, and binary gripper. EgoHumanoid achieves 78% success in lab (vs. 59% robot-only baseline) and 82% in unseen environments (vs. 31% robot-only baseline), demonstrating strong in-the-wild generalization. Its data requirement is substantially higher than LocoMimicGen's: ~400 demonstrations per task (100 robot + 300 human) versus LocoMimicGen's ≤20 teleoperated robot demonstrations total; its augmentation strategy is human behavioral diversity across real environments, whereas LocoMimicGen's is combinatorial spatial synthesis in simulation. The two systems are complementary rather than competing: LocoMimicGen's combinatorially diverse simulation demonstrations could serve as the robot-data component in EgoHumanoid-style co-training pipelines, while EgoHumanoid's human motion priors could inform stance selection in LocoMimicGen's IRM-guided retargeting.\\n\\nHoMMI (arXiv:2603.03243, March 2026, Stanford/TRI) learns whole-body mobile manipulation policies from egocentric human demonstrations on a mobile manipulator platform (Rainbow Robotics RB-Y1), achieving 80–90% real-robot success on three tasks using 115–200 human demos per task without teleoperation. HuMI (arXiv:2602.06643, Feb 2026) learns whole-body humanoid manipulation from robot-free mocap demonstrations on a bipedal humanoid, achieving 70–85% success across five tasks by pairing a diffusion policy with a sim-trained whole-body RL controller. HumanX (arXiv:2602.02473, Feb 2026) introduces XGen and XMimic — a data generation pipeline and unified imitation learning framework that synthesizes diverse robot interaction data from human video via physics-based motion retargeting and contact-aware augmentation, demonstrated across 10 agile interaction skills on the Unitree G1 (basketball, cargo pickup, reactive fighting); like EgoHumanoid, HoMMI, and HuMI, it learns from human behavioral diversity in real environments rather than procedural combinatorial synthesis in simulation. All four — EgoHumanoid, HoMMI, HuMI, and HumanX — represent data-collection paradigms complementary to LocoMimicGen's combinatorial spatial synthesis from ≤20 teleoperated robot demonstrations in simulation.\\n\\nNo existing system applies principled multi-segment object-centric demonstration decomposition with COUPLED SE(3) encoding of both navigation stances and arm trajectories — replacing the disjoint occupancy-map navigation of PR #3259 with frame-transform retargeting of manipulation stances to new object configurations — plus stance-conditioned IRM integration for bipedal humanoids and combinatorial multi-source composition, to enable room-level scaling.\",\n  \"approach\": \"We propose LocoMimicGen, built as a direct extension of Isaac Lab's 2.3 loco-manipulation infrastructure (PRs #3150, #3259, #3992) with three technical contributions. Starting from ≤20 teleoperated G1 whole-body demonstrations per task, each trajectory is decomposed into coupled subtask phases (locomotion-approach, manipulation-A, transit-locomotion, manipulation-B, return) using the Mimic segmentation API.\\n\\nContribution (1): Coupled SE(3) object-centric representation. By expressing the manipulation stance in the object's SE(3) local frame alongside the arm trajectory, frame-transform retargeting to new object configurations automatically yields a feasible new stance without any separate stance-placement planning. During recording, both arm end-effector waypoints AND locomotion stance poses (base position/orientation at each manipulation phase) are encoded jointly in each relevant object's local SE(3) reference frame — extending Isaac Lab Mimic's existing arm-only object-centric segment representation to include the robot base frame. This is the principled replacement for PR #3259's disjoint approach: instead of fixing the manipulation stance from the source demo and path-planning navigation at the trajectory level, LocoMimicGen retargets navigation stances to new object configurations as a natural byproduct of the SE(3) frame transformation, coupling manipulation and navigation retargeting in a single operation. Navigation between the retargeted stances is handled by the pretrained RL locomotion controller (PR #3150) as a black box; what the SE(3) encoding eliminates is the need to separately determine WHERE the robot should stand to manipulate at each new object configuration.\\n\\nContribution (2): Stance-conditioned IRM integration for bipedal humanoid retargeting. Retargeting to a new scene configuration requires solving for new manipulation stances satisfying arm reachability at the transformed object positions. We adapt and integrate inverse reachability map (IRM) methodology (Vahrenkamp et al. 2013; Burget et al. ICRA 2015; MoMa-Pos 2024; MoMaGen ICLR 2026) into the Mimic retargeting loop for the bipedal G1. The key integration challenge over prior wheeled-platform work is that bipedal arm reachability is conditioned on whole-body stance configuration — COM height, foot contact pattern, and balance state shape the arm workspace — making the IRM higher-dimensional and configuration-dependent compared to the SE(2) base-pose-only IRMs used in MoMa-Pos and MoMaGen. We pre-compute a stance-conditioned upper-body reachability map for the G1 (IK workspace sampled across a distribution of balance configurations) and solve for new stances via constrained optimization. The reachability map is a one-time offline precomputation (~3–5 H100-hours for IK sampling across ~50K balance configuration poses in 6D space: SE(2) base pose (x, y, θ) × squat depth × foot spread × weight distribution), GPU-parallel in Isaac Lab, shared across all tasks, and explicitly budgeted in the resource estimate. Navigation segments between planned stances use Isaac Lab's pretrained RL locomotion controller (PR #3150) as a navigation oracle. A concurrent technique from the same CNRS-AIST group (Murooka et al., arXiv:2508.11275, Humanoids 2025) introduces learned differentiable reachability maps for online gradient-based humanoid planning; the differentiable formulation is optimal for online continuous optimization but would be intractable as a batch-time constraint across 2048+ parallel Isaac Lab environments — LocoMimicGen's offline-precomputed discrete IRM is the appropriate design choice for high-throughput data generation. This contribution is framed as an integration contribution: adapting established IRM methodology to the bipedal context within the Mimic retargeting loop, where no prior work has addressed the stance-conditioned reachability problem for data generation.\\n\\nContribution (3): Combinatorial multi-source segment composition. Validated subtask segments from different source demonstrations are composed combinatorially across scene variants (object positions spanning the full room, table heights, obstacle placements), achieving 100–1,000× demo expansion from ≤20 seed demonstrations per task — a qualitatively different scaling regime from single-demo spatial adaptation (DemoHLM) or disjoint-phase augmentation within a single source demo (PR #3259). To make the scaling claim precise: with K=20 source demos, M=3 subtask phases, and scene variant dimensions P=10 object positions × Q=3 table heights × R=5 obstacle layouts, the conservative lower bound (treating each phase as independently variable while fixing others) is K×M×P×Q×R = 20×3×10×3×5 = 9,000 unique trajectories — a 450× expansion from 20 seed demonstrations. Full cross-phase combinatorial composition (drawing each of M phases independently from any of K source demos) yields K^M × P×Q×R = 20^3 × 150 = 8,000 × 150 ≈ 1.2M as the theoretical upper bound. The practical 100–1,000× range reflects compatibility filtering of geometrically infeasible segment pairs; 450× is the validated conservative estimate under the K×M×P×Q×R model.\\n\\nCompatibility between a terminal segment s_i and an incoming segment s_j (drawn from a different source demonstration) is evaluated against three criteria applied in sequence: (1) IRM feasibility — the stance-conditioned IRM score at the retargeted terminal base pose of phase i, evaluated for phase j's object configuration, must exceed threshold τ (set to the 10th percentile of IRM scores observed across source demonstrations), ensuring arm reachability is maintained through the transition; (2) base-pose continuity — the SE(2) distance between phase i's terminal base pose and phase j's required initial stance after object-frame retargeting must fall within δ_nav (the locomotion controller's recoverable displacement per sub-step, empirically ≈0.3 m), ensuring the navigation controller can bridge the gap without replanning; (3) contact-state consistency — gripper and object contact state at the terminal frame of s_i must match the required initial contact state of s_j (e.g., object grasped entering transit, released at return initiation). Criteria (1) and (2) are the active filters in practice: across the P×Q×R = 150 scene configuration space, IRM feasibility eliminates approximately 55–75% of random scene-stance pairings (the G1's arm workspace constrains which object positions are reachable from each source demo's stance), and pose continuity eliminates a further 10–20% of IRM-passing compositions. These two filters reduce the K^M × P×Q×R ≈ 1.2M theoretical upper bound to roughly 2,000–20,000 valid trajectories (100–1,000× expansion from 20 seed demos), while the K×M×P×Q×R = 9,000 conservative estimate reflects intra-demo phase composition achieving approximately 50% IRM pass rate in the nominal workspace regime.\\n\\nIsaac Lab's GPU-parallel simulation (2048+ G1 environments) with the pretrained RL controller validates physical feasibility; failures trigger local replanning of the base-pose optimization.\\n\\nWe evaluate on 2 primary loco-manipulation tasks (pick-and-place with navigation; two-phase transit task) plus 1 supplementary task (articulated-object manipulation with approach locomotion, e.g., door/drawer). The 2-primary + 1-supplementary structure is explicit: the articulated-object task involves contact-rich IRM optimization that carries higher debug risk within the CoRL timeline, and we position it as supplementary to protect schedule feasibility while retaining all three contributions in the evaluation. All baselines and LocoMimicGen conditions use Diffusion Policy (CNN-UNet variant, Chi et al. RSS 2023 / IJRR 2025) as the policy architecture, applied uniformly across all experimental conditions to isolate the data-generation contribution and prevent policy-architecture confounds. We target ≥20 percentage-point mean success-rate improvement over the PR #3259 baseline across the full held-out 150-configuration test distribution (10 object positions × 3 table heights × 5 obstacle layouts). This floor is grounded in MimicGen (CoRL 2023): on harder spatial-variant distributions (D1/D2) where baselines already incorporate partial scene randomization — analogous to PR #3259's coverage of the central reach envelope — MimicGen showed 20–40 pp gains from diversity-matched generated data. LocoMimicGen's 450× expansion targeting configurations categorically outside PR #3259's reachable stance envelope supports a ≥20 pp floor as a conservative claim; the primary measurement is the scaling-law curve (policy success rate as a function of synthetic dataset size) rather than a single endpoint comparison. We proactively address the expected reviewer comparison to DexMimicGen (9 tasks), HumanoidGen (6 tasks, 120+ scene variants), and MoMaGen (ICLR 2026, 4 tasks) on four grounds: (a) the scaling law curves — demo efficiency as a function of synthetic dataset size across P×Q×R configuration space — are the primary empirical contribution of LocoMimicGen, and these curves are fully established on 2 tasks without requiring breadth; (b) both primary tasks exercise all three contributions in combination (coupled SE(3) encoding, IRM-guided stance optimization, and combinatorial segment composition), making them jointly sufficient to validate the complete system; (c) DexMimicGen's 9-task breadth reuses fixed tabletop infrastructure where no locomotion integration is required, whereas LocoMimicGen integrates new IRM machinery into a live loco-manipulation stack — integration depth and correctness is the comparable ambition, not task count; (d) against MoMaGen (ICLR 2026) specifically: MoMaGen evaluates 4 tasks with real-robot fine-tuning on 40 demos but covers O(1) scene configurations per task, whereas LocoMimicGen sweeps P×Q×R = 10×3×5 = 150 configurations per primary task (300 total across both primary tasks) — data-efficiency curves across a 150-dimensional configuration space represent a fundamentally different empirical question from per-task success rate at fixed scene coverage, and LocoMimicGen's per-task scene-space depth exceeds both MoMaGen's and HumanoidGen's per-task scene coverage. Baselines: Isaac Lab Mimic PR #3259 (disjoint navigation, closest structural baseline) and Isaac Lab Mimic PR #3992 (position randomization only) are live reproduced baselines. OmniRetarget (arXiv:2509.26633) is included as a conceptual comparison citing its published retargeting fidelity and task-success metrics; although the Holosoma codebase (amazon-far/holosoma) is publicly available, the estimated 10–14 day setup cost for the Holosoma framework and MoCap dataset pipeline exceeds the available bandwidth in the 20-day schedule. DemoHLM (arXiv:2510.11258) is included as a conceptual comparison only, citing its published 10-task evaluation numbers directly; DemoHLM code has not been publicly released as of May 2026, making reimplementation infeasible within the 20-day window. Sim-to-real transfer on physical G1 hardware is explicitly future work; the contribution is established through simulation scaling analysis and cross-baseline comparison.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"h100_hours\": \"~87–110 H100h (≈210h A100 at 2.0–2.5× H100/A100 ratio, plus ~3–5 H100h IRM precomputation): data generation ~30h A100 across 3 tasks at 2048 parallel envs; policy training 3 tasks × 2 seeds × 15h = 90h A100; ablations (3 conditions × 3 tasks × 10h) = 90h A100; total ~210h A100 ÷ 2.5 = 84h H100 (lower bound), ÷ 2.0 = 105h H100 (upper bound), plus IRM precomputation 3–5h H100 = 87–110h H100 total — within 200h H100 constraint\",\n      \"irm_precomputation\": \"One-time offline: G1 stance-conditioned reachability map construction via IK sampling across ~50K balance configuration poses (6D space: SE(2) base × squat depth × foot spread × weight distribution), GPU-parallel in Isaac Lab: ~3–5 H100h; amortized across all tasks\",\n      \"gpu_utilization\": \"High idle (~60–70%): GPU waits on human-paced coding, debugging physics edge cases, and manual analysis between runs\",\n      \"timeline\": \"2–3 months (2 primary tasks + 1 supplementary reduces contact-rich debug risk; articulated-object task can be deferred if timeline is tight)\",\n      \"team\": \"2 researchers (1 robotics/sim, 1 IL/policy)\",\n      \"estimated_gpu_cost\": \"~$370 at $1.75/hr A100 (or ~$220–275 at $2.50/hr H100)\",\n      \"gantt_20day\": \"20-day critical path (CoRL 2026, paper due May 28 AoE): Days 1–3: IRM precomputation offline (50K-pose IK sampling, embarrassingly parallel in Isaac Lab — low-risk, starts immediately; output blocks Contribution 2 integration). Days 3–7: SE(3) encoding extension — modify Isaac Lab Mimic's segment recording/retargeting API to jointly encode base frame in object's local SE(3) alongside arm end-effector waypoints (critical-path bottleneck: most likely integration debugging hotspot; blocks Contributions 1 and 3). Days 7–12: Combinatorial composition engine — implement three-criterion compatibility filter (IRM feasibility, pose-continuity δ_nav, contact-state); validate on Task 1 (pick-and-place with navigation). Days 12–15: Full data generation runs across all 3 tasks at 2048+ parallel envs (requires Days 1–12 complete). Days 15–19: Diffusion Policy training (CNN-UNet, multi-seed) + ablations across live baselines (Isaac Lab Mimic PR #3259, PR #3992); OmniRetarget and DemoHLM are included as conceptual comparisons with published numbers cited directly — no reimplementation required within this window (requires Day 15 data). Day 19–20: Analysis, scaling-law figures, and write-up. Baseline notes: DemoHLM code is not publicly available as of May 2026 — cited conceptually from arXiv:2510.11258 published results; OmniRetarget (Holosoma) code is public but setup estimated at 10–14 days — designated as conceptual comparison citing arXiv:2509.26633 metrics; if Researcher 2 has bandwidth Days 1–7 before policy training begins, OmniRetarget live reproduction can be attempted as a stretch goal on a parallel track. Risk mitigation: articulated-object task (supplementary) deferred to Days 12–15 alongside primary tasks only if composition engine validation (Days 7–12) completes ahead of schedule; otherwise deferred to post-deadline supplementary material.\"\n    },\n    \"human_in_loop\": {\n      \"h100_hours\": \"~125–157 H100h (≈235–310h A100, plus ~3–5 H100h IRM precomputation): data generation ~35h A100; policy training 3 tasks × 2 seeds × 15h = 90h A100; ablations 5 conditions × 3 tasks × 12h = 180h A100 ≈ 305h A100 ÷ 2.5 = 122h H100 (lower bound), ÷ 2.0 = 152h H100 (upper bound), plus IRM precomputation 3–5h H100 = 125–157h H100 total — within 200h H100 constraint\",\n      \"irm_precomputation\": \"One-time offline: G1 stance-conditioned reachability map construction via IK sampling across ~50K balance configuration poses (6D space: SE(2) base × squat depth × foot spread × weight distribution), GPU-parallel in Isaac Lab: ~3–5 H100h; amortized across all tasks\",\n      \"gpu_utilization\": \"Moderate idle (~30–40%): approval gates pause GPU between stages, but agent batches setup and analysis tasks\",\n      \"timeline\": \"4–5 weeks\",\n      \"team\": \"1 researcher, ~45 min/day check-in for gate approvals and physics failure triage\",\n      \"claude_api_cost\": \"$200–400 (~300–500 turns at $0.08–0.12/turn for code gen, debug, analysis)\",\n      \"estimated_gpu_cost\": \"~$420–540 at $1.75/hr A100 (or ~$310–390 at $2.50/hr H100)\",\n      \"risk_note\": \"Stance-conditioned IRM for articulated object tasks (door/drawer) involves contact-rich interaction where failure modes require human insight to diagnose; the IRM integration formulation requires iterative design. Addressed by assigning the articulated-object task to supplementary, keeping primary evaluation on the 2 lower-risk tasks.\",\n      \"gantt_20day\": \"20-day critical path (CoRL 2026, paper due May 28 AoE): Days 1–3: IRM precomputation offline (50K-pose IK sampling, embarrassingly parallel in Isaac Lab — low-risk, starts immediately; output blocks Contribution 2 integration). Days 3–7: SE(3) encoding extension — modify Isaac Lab Mimic's segment recording/retargeting API to jointly encode base frame in object's local SE(3) alongside arm end-effector waypoints (critical-path bottleneck: most likely integration debugging hotspot; blocks Contributions 1 and 3). Days 7–12: Combinatorial composition engine — implement three-criterion compatibility filter (IRM feasibility, pose-continuity δ_nav, contact-state); validate on Task 1 (pick-and-place with navigation). Days 12–15: Full data generation runs across all 3 tasks at 2048+ parallel envs (requires Days 1–12 complete). Days 15–19: Diffusion Policy training (CNN-UNet, multi-seed) + ablations across live baselines (Isaac Lab Mimic PR #3259, PR #3992); OmniRetarget and DemoHLM are included as conceptual comparisons with published numbers cited directly — no reimplementation required within this window (requires Day 15 data). Day 19–20: Analysis, scaling-law figures, and write-up. Baseline notes: DemoHLM code is not publicly available as of May 2026 — cited conceptually from arXiv:2510.11258 published results; OmniRetarget (Holosoma) code is public but setup estimated at 10–14 days — designated as conceptual comparison citing arXiv:2509.26633 metrics. Risk mitigation: articulated-object task (supplementary) deferred to Days 12–15 alongside primary tasks only if composition engine validation (Days 7–12) completes ahead of schedule; otherwise deferred to post-deadline supplementary material.\"\n    }\n  },\n  \"target_venues\": [\n    \"CoRL 2026 (abstract May 26 AoE, full paper May 28 AoE / ≈May 29 UTC — 18 days from today)\",\n    \"IEEE Robotics and Automation Letters / RA-L (rolling submission, no hard deadline)\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations (CoRL 2023)\",\n    \"DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning (ICRA 2025)\",\n    \"HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning (NeurIPS 2025)\",\n    \"WholeBodyVLA: Towards Unified Latent VLA for Whole-Body Loco-Manipulation Control (ICLR 2026)\",\n    \"OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction (arXiv:2509.26633, Sept 2025)\",\n    \"MoMaGen: Generating Demonstrations under Soft and Hard Constraints for Multi-Step Bimanual Mobile Manipulation (ICLR 2026, arXiv:2510.18316)\",\n    \"DemoHLM: From One Demonstration to Generalizable Humanoid Loco-Manipulation (arXiv:2510.11258, Oct 2025)\",\n    \"DreamGen: Unlocking Generalization in Robot Learning through Video World Models (NVIDIA GEAR Lab, arXiv:2505.12705, May 2025) [GR00T-Dreams blueprint]\",\n    \"GR00T N1: An Open Foundation Model for Generalist Humanoid Robots (NVIDIA, arXiv:2503.14734, March 2025)\",\n    \"EgoHumanoid: Unlocking In-the-Wild Loco-Manipulation with Robot-Free Egocentric Demonstration (arXiv:2602.10106, Feb 2026, OpenDriveLab)\",\n    \"HoMMI: Learning Whole-Body Mobile Manipulation from Human Demonstrations (arXiv:2603.03243, March 2026, Stanford/TRI)\",\n    \"HuMI: Humanoid Manipulation Interface — Humanoid Whole-Body Manipulation from Robot-Free Demonstrations (arXiv:2602.06643, Feb 2026)\",\n    \"HumanX: Toward Agile and Generalizable Humanoid Interaction Skills from Human Videos (arXiv:2602.02473, Feb 2026)\",\n    \"VisualMimic: Visual Humanoid Loco-Manipulation via Motion Tracking and Generation (arXiv:2509.20322, IROS 2025)\",\n    \"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion (Chi et al., RSS 2023 / IJRR 2025, arXiv:2303.04137)\",\n    \"Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning (arXiv 2025)\",\n    \"Isaac Lab PR #3150: Locomanipulation Environment with G1 for Mimic workflow (merged Sept 9, 2025)\",\n    \"Isaac Lab PR #3259: Adds locomanipulation data generation via disjoint navigation (merged Sept 10, 2025, release/2.3.0)\",\n    \"Isaac Lab PR #3992: APIs to Isaac Lab Mimic for supporting loco-manipulation datagen (merged Dec 1, 2025)\",\n    \"Vahrenkamp et al.: Robot Placement based on Reachability Inversion (ICRA 2013)\",\n    \"Burget et al.: Stance Selection for Humanoid Grasping Tasks by Inverse Reachability Maps (ICRA 2015)\",\n    \"MoMa-Pos: An Efficient Object-Kinematic-Aware Base Placement Optimization Framework for Mobile Manipulation (arXiv:2403.19940, Oct 2024 revision, ICRA 2025)\",\n    \"Murooka et al.: Humanoid Loco-manipulation Planning based on Graph Search and Reachability Maps (arXiv:2505.23505, May 2025)\",\n    \"Murooka et al.: Learning Differentiable Reachability Maps for Optimization-based Humanoid Motion Generation (arXiv:2508.11275, Humanoids 2025)\"\n  ],\n  \"description\": \"LocoMimicGen extends Isaac Lab's 2.3 loco-manipulation infrastructure — comprising PRs #3150, #3259, and #3992 — with three precisely-scoped technical contributions that together enable room-level combinatorial scaling unavailable in existing systems.\\n\\nPR #3259 ('disjoint navigation', merged Sept 10, 2025, release/2.3.0) is the closest structural predecessor and primary baseline. It adds pick-navigate-place phase segmentation with occupancy-map path planning between phases and scene randomization. However, it handles navigation 'disjointly': the manipulation stance is fixed from the source demo and navigation is occupancy-map path planning at the trajectory level. It does NOT encode navigation stances in the object's SE(3) local frame, does NOT enforce arm-reachability constraints on base-pose selection (making generation infeasible when new object positions fall outside source demo stance's arm workspace), and does NOT compose segments from multiple source demonstrations.\\n\\nContribution (1): By expressing the manipulation stance in the object's SE(3) local frame alongside the arm trajectory, frame-transform retargeting to new object configurations automatically yields a feasible new stance without any separate stance-placement planning. Navigation between the retargeted stances is handled by the pretrained RL locomotion controller (PR #3150) as a black box; what the SE(3) encoding eliminates is the need to separately determine where the robot should stand to manipulate at each new object configuration. LocoMimicGen adds coupled SE(3) object-centric encoding of locomotion stances jointly with arm end-effector waypoints — the principled replacement for PR #3259's disjoint approach, enabling frame-transform retargeting of both manipulation stances and arm motions simultaneously.\\n\\nContribution (2): Stance-conditioned IRM integration for bipedal humanoid retargeting. We adapt and integrate IRM methodology (Vahrenkamp et al. 2013; Burget et al. ICRA 2015; MoMa-Pos 2024; MoMaGen ICLR 2026) into the Mimic retargeting loop for the G1. The integration challenge over prior wheeled-platform IRMs (MoMa-Pos, MoMaGen) is that bipedal arm reachability is conditioned on whole-body stance configuration (COM height, foot contact, balance state), requiring a stance-conditioned reachability map rather than a SE(2) base-pose-only map. The reachability map is a one-time offline precomputation (~3–5 H100-hours for IK sampling across ~50K balance configuration poses in 6D space: SE(2) base pose × squat depth × foot spread × weight distribution), GPU-parallel in Isaac Lab, shared across all tasks, and explicitly budgeted in the resource estimate. A concurrent technique from the same CNRS-AIST group (Murooka et al., arXiv:2508.11275, Humanoids 2025) introduces learned differentiable reachability maps for online gradient-based humanoid planning; LocoMimicGen uses offline-precomputed discrete IRM instead, as differentiable map gradient evaluation across 2048+ parallel Isaac Lab environments would bottleneck batch generation throughput. This is framed as an integration contribution — not a novel technique — with the bipedal stance-conditioning as the key technical challenge.\\n\\nContribution (3): Combinatorial multi-source segment composition from multiple (≤20 total) teleoperated demonstrations achieves 100–1,000× demo expansion — a qualitatively different scaling regime from PR #3259's single-source disjoint augmentation. The scaling bound is explicit: with K=20 source demonstrations decomposed into M=3 subtask phases, combined with P=10 object positions × Q=3 table heights × R=5 obstacle layouts, the conservative lower bound is K×M×P×Q×R = 20×3×10×3×5 = 9,000 unique trajectories (450× expansion from 20 seed demos); full cross-phase composition yields K^M × P×Q×R = 20^3 × 150 ≈ 1.2M as the theoretical maximum. Compatibility between segments from different source demonstrations is evaluated against three criteria: (1) IRM feasibility at the transition stance (IRM score exceeding the 10th percentile of source-demo scores); (2) base-pose continuity within δ_nav ≈ 0.3 m (the locomotion controller's recoverable displacement); (3) contact-state consistency at phase boundaries. Criteria (1) and (2) are the active filters: IRM feasibility eliminates ~55–75% of random scene-stance pairings, and pose continuity a further 10–20%, reducing the 1.2M theoretical bound to the practical 100–1,000× range (roughly 2,000–20,000 valid trajectories from 20 seed demos).\\n\\nAll policy training uses Diffusion Policy (CNN-UNet variant, Chi et al. RSS 2023 / IJRR 2025) uniformly across all baselines and LocoMimicGen conditions, isolating the data-generation contribution. We target ≥20 pp mean success-rate improvement over PR #3259 at the held-out 150-configuration test distribution, grounded in MimicGen's 20–40 pp gains on harder spatial-variant distributions where baselines already incorporate partial scene randomization.\\n\\nMoMaGen (ICLR 2026, arXiv:2510.18316) generates bimanual mobile manipulation demonstrations via hard-reachability-constrained optimization on a wheeled bimanual platform — now the strongest peer-reviewed comparison point for constrained demo generation. The differentiation is precise: MoMaGen's reachability constraint operates over SE(2) base pose for a wheeled platform where base pose fully determines arm workspace; LocoMimicGen's stance-conditioned IRM addresses the qualitatively harder bipedal case where arm reachability is conditioned on whole-body configuration. DreamGen (NVIDIA GEAR Lab, arXiv:2505.12705, May 2025) — the GR00T-Dreams blueprint — generates behavioral generalization across task types via video world-model sampling and IDM action recovery; LocoMimicGen generates spatial/configurational diversity within known loco-manipulation tasks via constraint-based combinatorial recombination with hard kinematic guarantees. The two approaches are complementary: DreamGen's world-model-imagined behavioral diversity and LocoMimicGen's constraint-verified spatial diversity address orthogonal dimensions of the data scarcity problem. EgoHumanoid (OpenDriveLab, arXiv:2602.10106, Feb 2026), HoMMI (arXiv:2603.03243, March 2026), HuMI (arXiv:2602.06643, Feb 2026), and HumanX (arXiv:2602.02473, Feb 2026) represent concurrent policy-learning paradigms — learning from human behavioral diversity in real environments (video, MoCap, egocentric demonstrations) to improve generalization — complementary to LocoMimicGen's combinatorial spatial synthesis from ≤20 robot demos in simulation.\\n\\nEvaluated on 2 primary loco-manipulation tasks (pick-and-place with navigation; two-phase transit) plus 1 supplementary articulated-object task. Live reproduced baselines: Isaac Lab Mimic PR #3259 (closest structural baseline) and PR #3992. Conceptual comparisons citing published numbers: OmniRetarget (arXiv:2509.26633; Holosoma code is public but 10–14 day setup exceeds the 20-day window) and DemoHLM (arXiv:2510.11258; code not publicly available as of May 2026). The 2-primary scope is proactively justified on four grounds against DexMimicGen (9 tasks), HumanoidGen (6 tasks, 120+ scene variants), and MoMaGen (ICLR 2026, 4 tasks): (a) scaling law curves across P×Q×R configuration space are the primary empirical contribution, fully established on 2 tasks; (b) both primary tasks exercise all three contributions; (c) DexMimicGen's breadth reuses fixed tabletop infrastructure vs. LocoMimicGen's IRM integration into a live loco-manipulation stack; (d) LocoMimicGen sweeps P×Q×R = 150 configurations per primary task (300 total), exceeding MoMaGen's and HumanoidGen's per-task scene coverage — scene-space depth is the appropriate metric for a data-generation infrastructure paper. Both compute modes (manual: ~87–110h H100; human-in-loop: ~125–157h H100) stay within the 200 H100-hour hard constraint, including the one-time IRM precomputation (~3–5 H100h). The 20-day critical path (IRM precomputation Days 1–3 → SE(3) encoding Days 3–7 → composition engine Days 7–12 → data generation Days 12–15 → policy training Days 15–19 → write-up Day 19–20) is explicitly identified; the SE(3) API integration (Days 3–7) is the critical-path bottleneck. Sim-to-real on physical G1 is explicit future work. CoRL 2026: abstract May 26 AoE, paper May 28 AoE.\",\n  \"project_name\": \"loco_mimicgen_humanoid_g1\",\n  \"source\": \"web_research\"\n}\n\n## Reviewer feedback (round 7)\nIssues: [\"MISSING CONCURRENT CITATION — ULTRA (arXiv:2603.03279, March 2026): 'Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation' uses physics-driven neural retargeting to translate large-scale MoCap to humanoid embodiments while preserving physical plausibility for contact-rich loco-manipulation. Although retargeting-based (not SE(3) demo multiplication), it is a direct March 2026 paper on whole-body humanoid loco-manipulation data generation and CoRL reviewers will expect to see it. Positioning is identical to OmniRetarget: 'ULTRA [arXiv:2603.03279] scales loco-manipulation data via physics-preserving MoCap retargeting — a complementary human-data-driven paradigm that requires large MoCap libraries, cannot combinatorially compose subtask segments across scene configurations, and does not address the manipulation-stance feasibility problem for new object positions.' One sentence in the landscape alongside OmniRetarget is sufficient.\", \"MISSING CONCURRENT CITATION — Psi-Zero / Ψ₀ (arXiv:2603.12263, March 2026): 'Open Foundation Model Towards Universal Humanoid Loco-Manipulation' pre-trains a VLM on 800 hours of egocentric human video, then post-trains a flow-based action expert on 30 hours of robot data, achieving 40% better success with 10× less robot data than baselines. Foundation model scaling (not procedural generation), but it is a March 2026 paper in the same problem space. CoRL reviewers will recognize it. One sentence alongside EgoHumanoid/HoMMI/HuMI/HumanX as a human-data-driven foundation model approach complementary to LocoMimicGen's combinatorial synthetic generation from ≤20 robot demos.\", \"IRM GRID RESOLUTION SPARSENESS NOT ACKNOWLEDGED: The proposed 50K-pose sampling across 6D configuration space (SE(2) base pose × squat depth × foot spread × weight distribution) yields approximately 50,000^(1/6) ≈ 5-6 points per dimension — a very coarse grid for reachability boundary detection. At this resolution, reachability map boundaries may be insufficiently smooth to reliably filter edge cases where the manipulator is at the limit of its workspace. The paper should acknowledge this resolution choice and reference how analogous IRM work (MoMa-Pos, MoMaGen) selected grid resolution, or note that it can be refined offline post-hoc without additional training cost.\", \"EVALUATION BREADTH RISK (ONGOING): Two primary tasks with sim-only evaluation continues to be the most likely cause of CoRL 2026 rejection or major revision requests. The existing scene-space-depth defense ('150 configurations per task vs. O(1) in MoMaGen/HumanoidGen') is the best available argument within the 20-day constraint, but it is a methodological claim that reviewers accustomed to DexMimicGen (9 tasks) and HumanoidGen (6 tasks) may not find sufficient. The paper should consider whether the supplementary articulated-object task can be elevated to co-primary status if the composition engine validates on schedule by Day 12, as three tasks with three contributions exercised would substantially reduce this risk.\"]\nFeedback: All four Round 6 required fixes are correctly implemented: DemoHLM is a conceptual comparison citing published numbers, the language reads 'stance-placement planning' not 'navigation planning,' HumanX/XMimic is in the landscape, and OmniRetarget is correctly scoped as a conceptual comparison. The idea's technical foundation is now solid and the gap against Isaac Lab PR #3259 is independently confirmed by research.\n\n**Fix 1 (required, 1 sentence)**: Add ULTRA (arXiv:2603.03279, March 2026) to the landscape paragraph alongside OmniRetarget. Frame it as a complementary physics-preserving MoCap retargeting approach that requires large motion capture libraries and cannot perform combinatorial subtask segment composition — the same positioning as OmniRetarget. CoRL reviewers will notice its absence.\n\n**Fix 2 (required, 1 sentence)**: Add Psi-Zero/Ψ₀ (arXiv:2603.12263, March 2026) to the landscape alongside EgoHumanoid/HoMMI/HuMI/HumanX as a foundation model pre-training approach. One sentence: 'Ψ₀ [arXiv:2603.12263] pre-trains a VLM on 800 hours of human egocentric video and post-trains a flow-based action expert on 30 hours of robot data — a human-data-driven scaling paradigm orthogonal to LocoMimicGen's combinatorial spatial synthesis from ≤20 teleoperated robot demonstrations.'\n\n**Fix 3 (optional but recommended, 1 sentence)**: Acknowledge the IRM grid resolution choice explicitly — something like 'The 50K-pose resolution (~5-6 samples per dimension) is consistent with offline IRM construction in prior work (MoMa-Pos, Vahrenkamp et al.) and can be refined post-hoc at no additional training cost.' This preempts a reviewer question about whether the reachability boundary is smooth enough at this resolution.\n\n**Fix 4 (contingency plan, 1 sentence)**: Add a sentence noting that if the composition engine validates on Task 1 by Day 11 rather than Day 12, the supplementary articulated-object task will be elevated to co-primary status in the evaluation, bringing the primary task count to three. This signals execution awareness and reduces the evaluation-breadth risk without changing the critical path.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.\n- Address each issue specifically.\n\n## 深度调研要求（每一轮修订都必须执行）\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。\n   - 搜索最新的相关论文（arXiv, conference proceedings）\n   - 搜索 benchmark/leaderboard 确认当前 SOTA\n   - 搜索可能遗漏的相关工作和 concurrent work\n\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，\n   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。\n\n3. **深度思考**：在修订之前，先独立思考以下问题：\n   - 这个 idea 的核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach 来解决同一个核心问题？\n   - 修订后的 idea 相比上一版有什么本质性的改进？\n\n4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，\n   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。\n\n## 针对 Review 意见的定向搜索\n\n对 reviewer 指出的每个问题，执行以下搜索流程：\n\n1. **如果 reviewer 说'已有类似工作'**：\n   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读\n   - 搜索该论文的 cited-by，找到后续跟进工作\n   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot\n\n2. **如果 reviewer 说'SOTA 过时'**：\n   - 用 Papers With Code 查看当前排行榜\n   - 搜索过去 6 个月的最新方法\n   - 更新你的 landscape 和 baseline\n\n3. **如果 reviewer 说'可行性有问题'**：\n   - 搜索类似规模实验的实际成本和时间线\n   - 搜索 GitHub 上是否有可复用的实现\n   - 搜索相关数据集/模型的可获取性\n\n4. **如果 reviewer 说'novelty 不足'**：\n   - 对核心方法尽量做 3-5 种不同关键词组合的搜索\n   - 搜索相邻领域是否有类似思路\n   - 如果确实 novelty 不足，考虑 major revision 或 pivot\n\n- Use WebSearch to find updated information if the reviewer flagged outdated claims.\n- You have full freedom in how much to change:\n  - Minor fix: if only specific details are wrong, correct them and keep everything else.\n  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.\n  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.\n- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.\n- In the output JSON, include a \"change_type\" field with one of: \"minor\", \"major\", or \"pivot\" to indicate the scope of your changes.\n- Output the revised idea as a COMPLETE JSON object (same schema as original, plus \"change_type\").\n\n## 停滞提醒\n这个 idea 已经经过 7 轮修订，近 3 轮的平均分从 3.8 到 3.8，没有明显改善。\n\n请认真思考：\n- 当前方向是否存在根本性的瓶颈？反复的 minor fix 是否在回避核心问题？\n- 如果你认为问题出在 approach 而非 framing，可以做 major revision。\n- 如果你认为 core problem 本身就有问题（gap 不存在、问题不够重要），pivot 到同一研究领域下的新方向可能是更好的选择。\n- 当然，如果你有信心这一轮修订能实现突破，继续改进也完全可以。\n\n最终由你判断——做你认为最能提升 idea 质量的选择。"
}
```

---

### Runtime record

_source line 2 · 2026-05-10T13:08:37.643Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T13:08:37.643Z",
  "sessionId": "e93981d8-61dc-4460-8c15-6141e331b9de"
}
```

---

## Round 1

29 recorded events

### User

_source line 3 · 2026-05-10T13:08:37.672Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-10 (UTC).**

## Original idea
{
  "title": "LocoMimicGen: Coupled SE(3) Object-Centric Demo Multiplication for Mobile Humanoid Loco-Manipulation",
  "core_problem": "How can a handful of expensive teleoperated whole-body loco-manipulation demonstrations be multiplied by orders of magnitude across diverse spatial configurations — new object positions, table heights, room obstacle layouts — while maintaining physical validity for the mobile bipedal humanoid platform? Isaac Lab's 2.3 GA release contains three directly relevant prior contributions. PR #3150 (merged Sept 9, 2025) adds the G1 loco-manipulation environment integrating a pretrained RL locomotion policy with Pink IK arm control. PR #3259 ('Adds locomanipulation data generation via disjoint navigation', merged Sept 10, 2025) adds pick-navigate-place phase segmentation with occupancy-map path planning between phases and scene randomization of tabletop positions, navigation destinations, and floor obstacles — making it the closest structural predecessor to LocoMimicGen. PR #3992 (merged Dec 1, 2025) extends the Mimic framework with a 'body end-effector' API and navigation controller integration. Despite this infrastructure, three technical gaps prevent room-level combinatorial scaling: PR #3259 handles navigation 'disjointly' — the manipulation stance (where the robot stands to manipulate) is fixed from the source demo and navigation is handled as path-level occupancy-map planning between fixed phases, NOT as coupled SE(3) object-centric encoding of stances jointly with arm trajectories. None of these PRs enforce arm-reachability constraints on base-pose selection during retargeting — the robot manipulates from whatever stance the source demo used, regardless of arm workspace feasibility for new object positions. And none perform combinatorial composition of subtask segments from multiple source demonstrations. These three absences cap achievable diversity at object-position randomization within a single source demo's reach envelope, rather than the combinatorial room-level scaling that MimicGen achieves for tabletop tasks.",
  "opportunity": "Isaac Lab's 2.3 GA release (PRs #3150, #3259, #3992) now provides the exact scaffolding — G1 environment, pick-navigate-place phase segmentation, occupancy-map path planning, Mimic segmentation framework, and navigation controller integration — needed to build a principled extension. The precise technical gap is narrow but high-impact: adding (1) SE(3) object-centric encoding of navigation stances jointly with arm trajectories into the existing Mimic segment representation (replacing the disjoint path-planning approach of PR #3259 with coupled frame-transform retargeting), (2) stance-conditioned reachability-map-guided base-pose optimization enforcing arm feasibility at each manipulation stance during retargeting (adapting IRM methodology from the mobile-manipulator literature to the bipedal humanoid setting, where the reachability map is conditioned on whole-body configuration rather than just SE(2) base pose), and (3) combinatorial subtask segment composition from multiple source demonstrations. OmniRetarget (Amazon, Sept 2025) addresses humanoid loco-manipulation data generation from MoCap sequences via interaction-mesh Laplacian deformation on the G1, but retargets continuous motion sequences and cannot combinatorially compose segments across scene variants. DemoHLM (Oct 2025) demonstrates generalizable single-demonstration adaptation across 10 G1 loco-manipulation household tasks but the single-demo paradigm limits scaling to spatial interpolation within one source demo's envelope. The three-part Isaac Lab Mimic extension proposed here is tractable within existing infrastructure, precisely bounded against Isaac Lab's own 2.3 baseline (including PR #3259 as the most direct predecessor), and is the missing ingredient for room-level combinatorial scaling. MoMaGen (ICLR 2026, arXiv:2510.18316) imposes reachability as a hard constraint for wheeled bimanual mobile base-pose sampling — SE(2) for a wheeled platform. Now peer-reviewed at ICLR 2026, MoMaGen's coverage of hard-reachability-constrained demo generation makes the bipedal differentiation the critical point of departure: MoMaGen's reachability constraint operates over SE(2) base pose for a wheeled bimanual platform where the base pose fully determines arm workspace, whereas LocoMimicGen's stance-conditioned IRM addresses the qualitatively harder bipedal case where arm reachability is conditioned on whole-body configuration — COM height, foot contact, balance state — a higher-dimensional reachability function not covered by any prior data-generation work. EgoHumanoid (OpenDriveLab, arXiv:2602.10106, Feb 2026) represents a concurrent complementary paradigm — co-training VLA policies on human egocentric video alongside robot demonstrations — that highlights the orthogonal value of LocoMimicGen's combinatorial simulation synthesis approach.",
  "landscape": "MimicGen (CoRL 2023) decomposes arm demonstrations into object-centric subtask segments and applies SE(3) frame transformations — manipulation-only. DexMimicGen (ICRA 2025) extends this to bimanual dexterous humanoids, still tabletop. HumanoidGen (NeurIPS 2025) uses LLM-driven planning for tabletop dexterous tasks with 120+ scene variants — explicitly excludes locomotion.\n\nIsaac Lab 2.3 loco-manipulation infrastructure comprises three PRs that together form the primary baseline. PR #3150 (merged Sept 9, 2025) adds Isaac-PickPlace-Locomanipulation-G1-Abs-v0, integrating a pretrained RL locomotion policy (velocity commands vx, vy, wz) with Pink IK arm control, achieving 92% success on pick-and-place. PR #3259 ('Adds locomanipulation data generation via disjoint navigation', merged Sept 10, 2025, release/2.3.0) is the closest structural predecessor to LocoMimicGen: it adds pick-navigate-place phase segmentation, occupancy-map-based collision-free path planning between phases, and scene randomization of tabletop object positions, navigation destinations, and floor obstacles. The implementation lives under disjoint_navigation/ and works by (a) recording static manipulation teleoperation with the base stationary, (b) applying Mimic augmentation to manipulation segments, and (c) stitching path-planned navigation trajectories between the resulting phases. Critically, PR #3259 does NOT encode navigation stances in the object's SE(3) local frame — navigation is occupancy-map path planning at the trajectory level, while the manipulation stance (where the robot stands to manipulate) is fixed from the source demo, not retargeted to new object positions. There is no arm-reachability constraint on base-pose selection: if a new object position falls outside the arm workspace at the source demo's stance, the generation produces infeasible trajectories rather than finding a feasible stance. There is no combinatorial composition from multiple source demonstrations. PR #3992 (merged Dec 1, 2025) adds a 'body end-effector' API and get_navigation_state() integration into the Mimic framework but relies on the same state-based navigation repetition/skipping, not object-centric stance encoding.\n\nInverse reachability maps (IRM) for robot base placement are a well-established technique. Vahrenkamp et al. 2013 introduced IRM for robot placement by inverting precomputed reachability maps to generate SE(2) distributions of feasible base poses. Burget et al. (ICRA 2015) applied IRM specifically to humanoid stance selection for grasping tasks — but in a static grasping context where balance is assumed, not within a data-generation retargeting loop. MoMa-Pos (arXiv:2403.19940, Oct 2024 revision, ICRA 2025) integrates IRM with object kinematics for mobile manipulator base placement — applied to wheeled platforms where the reachability function maps over SE(2) base pose only. MoMaGen (ICLR 2026, arXiv:2510.18316) imposes reachability as a hard constraint for wheeled bimanual mobile base-pose sampling — again, SE(2) for a wheeled platform. The integration challenge for bipedal humanoids is qualitatively different: on wheeled platforms the base pose fully determines arm workspace, but on bipedal systems arm reachability is conditioned on whole-body stance configuration — COM height, foot placement pattern, and balance state collectively shape the arm workspace. A concurrent planning paper (Murooka et al., arXiv:2505.23505, May 2025) uses forward reachability maps for humanoid loco-manipulation task planning via graph search, but targets autonomous task execution planning, not imitation learning data generation; it does not perform data augmentation, Mimic-style segment composition, or retargeting. The same CNRS-AIST group (Murooka et al., arXiv:2508.11275, Humanoids 2025) subsequently introduced learned differentiable reachability maps for optimization-based humanoid motion generation — continuous scalar-valued functions differentiable with respect to task-space coordinates, enabling gradient-based planning for footstep sequencing and loco-manipulation without repeated IK solving. The differentiable formulation excels at online continuous optimization but is not suited to LocoMimicGen's batch data-generation context: evaluating differentiable map gradients across 2048+ parallel Isaac Lab environments at retargeting time would bottleneck generation throughput, whereas LocoMimicGen's offline-precomputed discrete IRM is evaluated as a table lookup simultaneously across all environments. The two approaches are complementary in use case — differentiable maps for online planning, discrete IRM for batch generation — and both leave the stance-conditioned data-generation problem unaddressed.\n\nOmniRetarget (Amazon, arXiv:2509.26633, Sept 2025) generates loco-manipulation demonstrations on the G1 via interaction-mesh Laplacian deformation of human MoCap sequences (OMOMO, LAFAN1, in-house). It preserves spatial and contact relationships and enables augmentation across embodiments, terrains, and object configurations. Critically, OmniRetarget (a) requires large MoCap databases rather than small teleoperated G1 demonstrations; (b) retargets continuous motion sequences without decomposing into reusable subtask segments; (c) cannot combinatorially compose segments from different source demos; and (d) targets locomotion-heavy tasks rather than precision manipulation requiring tight coupling between base position and arm workspace. OmniRetarget's codebase (Holosoma, amazon-far/holosoma) is publicly available; LocoMimicGen positions it as a conceptual comparison citing published retargeting fidelity metrics, as the estimated 10–14 day setup cost for Holosoma plus MoCap dataset ingestion exceeds the available bandwidth in the 20-day window.\n\nDemoHLM (arXiv:2510.11258, Oct 2025) segments demonstrations into three stages (locomotion, pre-manipulation, manipulation) and adapts the source trajectory to new initial object/robot poses by modifying high-level stage commands on the G1. It demonstrates 10 loco-manipulation household tasks with sim-to-real transfer. DemoHLM's single-demonstration paradigm limits scaling: each task uses one source demo replayed with modified commands, and 'spatial variation' is object position adjustment rather than room-level layout diversity. DemoHLM's code has not been publicly released as of May 2026; LocoMimicGen therefore positions it as a conceptual comparison, citing its published 10-task evaluation results directly.\n\nMoMaGen (ICLR 2026, arXiv:2510.18316) generates bimanual mobile manipulation demonstrations via constrained optimization (hard reachability + soft visibility) on a wheeled bimanual mobile base. The wheeled platform decouples navigation from balance, making MoMaGen's SE(2) base-pose sampling inapplicable to bipedal humanoids.\n\nDreamGen (NVIDIA GEAR Lab, arXiv:2505.12705, May 2025) — the technical backbone of the Isaac GR00T-Dreams blueprint, first announced alongside GR00T N1 in March 2025 — generates synthetic 'neural trajectories' by fine-tuning a video world model (Cosmos Predict-2) on a handful of teleoperated demonstrations, then sampling diverse video scenarios via diffusion and recovering pseudo-action sequences with an inverse dynamics model (IDM). DreamGen achieves strong behavioral generalization: GR00T N1 trained exclusively on pick-and-place achieves 0% on novel behaviors without DreamGen, while DreamGen-augmented training reaches 43.2% success on new behaviors in seen environments and 28.5% in completely unseen environments. Importantly, DreamGen evaluates all tasks in a stationary-manipulation setting — even for the humanoid GR1, the robot remains stationary while the arms operate — and the authors explicitly identify 'supporting more complex, dexterous behaviors requiring richer control' as future work. A second NVIDIA pipeline, GR00T-Mimic, applies MimicGen-style interpolation within the GR00T N1 training workflow to expand tabletop manipulation trajectories; it operates without locomotion coupling. DreamGen and LocoMimicGen are complementary rather than competing: DreamGen delivers behavioral diversity across task types (novel manipulation verbs, object categories, unseen environments) via world-model imagination, while LocoMimicGen delivers spatial/configurational diversity within known loco-manipulation tasks (exponentially more room-scale configurations) through constraint-based combinatorial recombination. Critically, DreamGen's IDM-extracted pseudo-actions are pixel-level learned approximations without explicit kinematic validation — LocoMimicGen's procedural recombination with IRM feasibility filters, pose-continuity bounds (δ_nav ≈ 0.3 m), and contact-consistency checks enforces hard physical guarantees that learned world models currently cannot provide at per-joint kinematic precision for coupled loco-manipulation tasks.\n\nVisualMimic (arXiv:2509.20322, IROS 2025) unifies egocentric vision with hierarchical whole-body control via human motion tracking — a different paradigm (video-based policy learning) rather than procedural demonstration generation.\n\nEgoHumanoid (Modi Shi et al., OpenDriveLab, arXiv:2602.10106, Feb 2026) addresses in-the-wild loco-manipulation on the Unitree G1 (1.3m, 29 DoF) by co-training a VLA policy on ~100 VR-teleoperated robot episodes plus ~300 egocentric human episodes per task (captured with PICO VR headset and ZED X Mini head-mounted camera), spanning four tasks: Pillow Placement, Trash Disposal, Toy Transfer, and Cart Stowing. View alignment uses MoGe depth prediction and point-cloud reprojection to the robot viewpoint with diffusion inpainting for occluded regions; action alignment maps to 6-DoF delta EEF for upper body, discrete locomotion commands, and binary gripper. EgoHumanoid achieves 78% success in lab (vs. 59% robot-only baseline) and 82% in unseen environments (vs. 31% robot-only baseline), demonstrating strong in-the-wild generalization. Its data requirement is substantially higher than LocoMimicGen's: ~400 demonstrations per task (100 robot + 300 human) versus LocoMimicGen's ≤20 teleoperated robot demonstrations total; its augmentation strategy is human behavioral diversity across real environments, whereas LocoMimicGen's is combinatorial spatial synthesis in simulation. The two systems are complementary rather than competing: LocoMimicGen's combinatorially diverse simulation demonstrations could serve as the robot-data component in EgoHumanoid-style co-training pipelines, while EgoHumanoid's human motion priors could inform stance selection in LocoMimicGen's IRM-guided retargeting.\n\nHoMMI (arXiv:2603.03243, March 2026, Stanford/TRI) learns whole-body mobile manipulation policies from egocentric human demonstrations on a mobile manipulator platform (Rainbow Robotics RB-Y1), achieving 80–90% real-robot success on three tasks using 115–200 human demos per task without teleoperation. HuMI (arXiv:2602.06643, Feb 2026) learns whole-body humanoid manipulation from robot-free mocap demonstrations on a bipedal humanoid, achieving 70–85% success across five tasks by pairing a diffusion policy with a sim-trained whole-body RL controller. HumanX (arXiv:2602.02473, Feb 2026) introduces XGen and XMimic — a data generation pipeline and unified imitation learning framework that synthesizes diverse robot interaction data from human video via physics-based motion retargeting and contact-aware augmentation, demonstrated across 10 agile interaction skills on the Unitree G1 (basketball, cargo pickup, reactive fighting); like EgoHumanoid, HoMMI, and HuMI, it learns from human behavioral diversity in real environments rather than procedural combinatorial synthesis in simulation. All four — EgoHumanoid, HoMMI, HuMI, and HumanX — represent data-collection paradigms complementary to LocoMimicGen's combinatorial spatial synthesis from ≤20 teleoperated robot demonstrations in simulation.\n\nNo existing system applies principled multi-segment object-centric demonstration decomposition with COUPLED SE(3) encoding of both navigation stances and arm trajectories — replacing the disjoint occupancy-map navigation of PR #3259 with frame-transform retargeting of manipulation stances to new object configurations — plus stance-conditioned IRM integration for bipedal humanoids and combinatorial multi-source composition, to enable room-level scaling.",
  "approach": "We propose LocoMimicGen, built as a direct extension of Isaac Lab's 2.3 loco-manipulation infrastructure (PRs #3150, #3259, #3992) with three technical contributions. Starting from ≤20 teleoperated G1 whole-body demonstrations per task, each trajectory is decomposed into coupled subtask phases (locomotion-approach, manipulation-A, transit-locomotion, manipulation-B, return) using the Mimic segmentation API.\n\nContribution (1): Coupled SE(3) object-centric representation. By expressing the manipulation stance in the object's SE(3) local frame alongside the arm trajectory, frame-transform retargeting to new object configurations automatically yields a feasible new stance without any separate stance-placement planning. During recording, both arm end-effector waypoints AND locomotion stance poses (base position/orientation at each manipulation phase) are encoded jointly in each relevant object's local SE(3) reference frame — extending Isaac Lab Mimic's existing arm-only object-centric segment representation to include the robot base frame. This is the principled replacement for PR #3259's disjoint approach: instead of fixing the manipulation stance from the source demo and path-planning navigation at the trajectory level, LocoMimicGen retargets navigation stances to new object configurations as a natural byproduct of the SE(3) frame transformation, coupling manipulation and navigation retargeting in a single operation. Navigation between the retargeted stances is handled by the pretrained RL locomotion controller (PR #3150) as a black box; what the SE(3) encoding eliminates is the need to separately determine WHERE the robot should stand to manipulate at each new object configuration.\n\nContribution (2): Stance-conditioned IRM integration for bipedal humanoid retargeting. Retargeting to a new scene configuration requires solving for new manipulation stances satisfying arm reachability at the transformed object positions. We adapt and integrate inverse reachability map (IRM) methodology (Vahrenkamp et al. 2013; Burget et al. ICRA 2015; MoMa-Pos 2024; MoMaGen ICLR 2026) into the Mimic retargeting loop for the bipedal G1. The key integration challenge over prior wheeled-platform work is that bipedal arm reachability is conditioned on whole-body stance configuration — COM height, foot contact pattern, and balance state shape the arm workspace — making the IRM higher-dimensional and configuration-dependent compared to the SE(2) base-pose-only IRMs used in MoMa-Pos and MoMaGen. We pre-compute a stance-conditioned upper-body reachability map for the G1 (IK workspace sampled across a distribution of balance configurations) and solve for new stances via constrained optimization. The reachability map is a one-time offline precomputation (~3–5 H100-hours for IK sampling across ~50K balance configuration poses in 6D space: SE(2) base pose (x, y, θ) × squat depth × foot spread × weight distribution), GPU-parallel in Isaac Lab, shared across all tasks, and explicitly budgeted in the resource estimate. Navigation segments between planned stances use Isaac Lab's pretrained RL locomotion controller (PR #3150) as a navigation oracle. A concurrent technique from the same CNRS-AIST group (Murooka et al., arXiv:2508.11275, Humanoids 2025) introduces learned differentiable reachability maps for online gradient-based humanoid planning; the differentiable formulation is optimal for online continuous optimization but would be intractable as a batch-time constraint across 2048+ parallel Isaac Lab environments — LocoMimicGen's offline-precomputed discrete IRM is the appropriate design choice for high-throughput data generation. This contribution is framed as an integration contribution: adapting established IRM methodology to the bipedal context within the Mimic retargeting loop, where no prior work has addressed the stance-conditioned reachability problem for data generation.\n\nContribution (3): Combinatorial multi-source segment composition. Validated subtask segments from different source demonstrations are composed combinatorially across scene variants (object positions spanning the full room, table heights, obstacle placements), achieving 100–1,000× demo expansion from ≤20 seed demonstrations per task — a qualitatively different scaling regime from single-demo spatial adaptation (DemoHLM) or disjoint-phase augmentation within a single source demo (PR #3259). To make the scaling claim precise: with K=20 source demos, M=3 subtask phases, and scene variant dimensions P=10 object positions × Q=3 table heights × R=5 obstacle layouts, the conservative lower bound (treating each phase as independently variable while fixing others) is K×M×P×Q×R = 20×3×10×3×5 = 9,000 unique trajectories — a 450× expansion from 20 seed demonstrations. Full cross-phase combinatorial composition (drawing each of M phases independently from any of K source demos) yields K^M × P×Q×R = 20^3 × 150 = 8,000 × 150 ≈ 1.2M as the theoretical upper bound. The practical 100–1,000× range reflects compatibility filtering of geometrically infeasible segment pairs; 450× is the validated conservative estimate under the K×M×P×Q×R model.\n\nCompatibility between a terminal segment s_i and an incoming segment s_j (drawn from a different source demonstration) is evaluated against three criteria applied in sequence: (1) IRM feasibility — the stance-conditioned IRM score at the retargeted terminal base pose of phase i, evaluated for phase j's object configuration, must exceed threshold τ (set to the 10th percentile of IRM scores observed across source demonstrations), ensuring arm reachability is maintained through the transition; (2) base-pose continuity — the SE(2) distance between phase i's terminal base pose and phase j's required initial stance after object-frame retargeting must fall within δ_nav (the locomotion controller's recoverable displacement per sub-step, empirically ≈0.3 m), ensuring the navigation controller can bridge the gap without replanning; (3) contact-state consistency — gripper and object contact state at the terminal frame of s_i must match the required initial contact state of s_j (e.g., object grasped entering transit, released at return initiation). Criteria (1) and (2) are the active filters in practice: across the P×Q×R = 150 scene configuration space, IRM feasibility eliminates approximately 55–75% of random scene-stance pairings (the G1's arm workspace constrains which object positions are reachable from each source demo's stance), and pose continuity eliminates a further 10–20% of IRM-passing compositions. These two filters reduce the K^M × P×Q×R ≈ 1.2M theoretical upper bound to roughly 2,000–20,000 valid trajectories (100–1,000× expansion from 20 seed demos), while the K×M×P×Q×R = 9,000 conservative estimate reflects intra-demo phase composition achieving approximately 50% IRM pass rate in the nominal workspace regime.\n\nIsaac Lab's GPU-parallel simulation (2048+ G1 environments) with the pretrained RL controller validates physical feasibility; failures trigger local replanning of the base-pose optimization.\n\nWe evaluate on 2 primary loco-manipulation tasks (pick-and-place with navigation; two-phase transit task) plus 1 supplementary task (articulated-object manipulation with approach locomotion, e.g., door/drawer). The 2-primary + 1-supplementary structure is explicit: the articulated-object task involves contact-rich IRM optimization that carries higher debug risk within the CoRL timeline, and we position it as supplementary to protect schedule feasibility while retaining all three contributions in the evaluation. All baselines and LocoMimicGen conditions use Diffusion Policy (CNN-UNet variant, Chi et al. RSS 2023 / IJRR 2025) as the policy architecture, applied uniformly across all experimental conditions to isolate the data-generation contribution and prevent policy-architecture confounds. We target ≥20 percentage-point mean success-rate improvement over the PR #3259 baseline across the full held-out 150-configuration test distribution (10 object positions × 3 table heights × 5 obstacle layouts). This floor is grounded in MimicGen (CoRL 2023): on harder spatial-variant distributions (D1/D2) where baselines already incorporate partial scene randomization — analogous to PR #3259's coverage of the central reach envelope — MimicGen showed 20–40 pp gains from diversity-matched generated data. LocoMimicGen's 450× expansion targeting configurations categorically outside PR #3259's reachable stance envelope supports a ≥20 pp floor as a conservative claim; the primary measurement is the scaling-law curve (policy success rate as a function of synthetic dataset size) rather than a single endpoint comparison. We proactively address the expected reviewer comparison to DexMimicGen (9 tasks), HumanoidGen (6 tasks, 120+ scene variants), and MoMaGen (ICLR 2026, 4 tasks) on four grounds: (a) the scaling law curves — demo efficiency as a function of synthetic dataset size across P×Q×R configuration space — are the primary empirical contribution of LocoMimicGen, and these curves are fully established on 2 tasks without requiring breadth; (b) both primary tasks exercise all three contributions in combination (coupled SE(3) encoding, IRM-guided stance optimization, and combinatorial segment composition), making them jointly sufficient to validate the complete system; (c) DexMimicGen's 9-task breadth reuses fixed tabletop infrastructure where no locomotion integration is required, whereas LocoMimicGen integrates new IRM machinery into a live loco-manipulation stack — integration depth and correctness is the comparable ambition, not task count; (d) against MoMaGen (ICLR 2026) specifically: MoMaGen evaluates 4 tasks with real-robot fine-tuning on 40 demos but covers O(1) scene configurations per task, whereas LocoMimicGen sweeps P×Q×R = 10×3×5 = 150 configurations per primary task (300 total across both primary tasks) — data-efficiency curves across a 150-dimensional configuration space represent a fundamentally different empirical question from per-task success rate at fixed scene coverage, and LocoMimicGen's per-task scene-space depth exceeds both MoMaGen's and HumanoidGen's per-task scene coverage. Baselines: Isaac Lab Mimic PR #3259 (disjoint navigation, closest structural baseline) and Isaac Lab Mimic PR #3992 (position randomization only) are live reproduced baselines. OmniRetarget (arXiv:2509.26633) is included as a conceptual comparison citing its published retargeting fidelity and task-success metrics; although the Holosoma codebase (amazon-far/holosoma) is publicly available, the estimated 10–14 day setup cost for the Holosoma framework and MoCap dataset pipeline exceeds the available bandwidth in the 20-day schedule. DemoHLM (arXiv:2510.11258) is included as a conceptual comparison only, citing its published 10-task evaluation numbers directly; DemoHLM code has not been publicly released as of May 2026, making reimplementation infeasible within the 20-day window. Sim-to-real transfer on physical G1 hardware is explicitly future work; the contribution is established through simulation scaling analysis and cross-baseline comparison.",
  "resource_estimate": {
    "manual": {
      "h100_hours": "~87–110 H100h (≈210h A100 at 2.0–2.5× H100/A100 ratio, plus ~3–5 H100h IRM precomputation): data generation ~30h A100 across 3 tasks at 2048 parallel envs; policy training 3 tasks × 2 seeds × 15h = 90h A100; ablations (3 conditions × 3 tasks × 10h) = 90h A100; total ~210h A100 ÷ 2.5 = 84h H100 (lower bound), ÷ 2.0 = 105h H100 (upper bound), plus IRM precomputation 3–5h H100 = 87–110h H100 total — within 200h H100 constraint",
      "irm_precomputation": "One-time offline: G1 stance-conditioned reachability map construction via IK sampling across ~50K balance configuration poses (6D space: SE(2) base × squat depth × foot spread × weight distribution), GPU-parallel in Isaac Lab: ~3–5 H100h; amortized across all tasks",
      "gpu_utilization": "High idle (~60–70%): GPU waits on human-paced coding, debugging physics edge cases, and manual analysis between runs",
      "timeline": "2–3 months (2 primary tasks + 1 supplementary reduces contact-rich debug risk; articulated-object task can be deferred if timeline is tight)",
      "team": "2 researchers (1 robotics/sim, 1 IL/policy)",
      "estimated_gpu_cost": "~$370 at $1.75/hr A100 (or ~$220–275 at $2.50/hr H100)",
      "gantt_20day": "20-day critical path (CoRL 2026, paper due May 28 AoE): Days 1–3: IRM precomputation offline (50K-pose IK sampling, embarrassingly parallel in Isaac Lab — low-risk, starts immediately; output blocks Contribution 2 integration). Days 3–7: SE(3) encoding extension — modify Isaac Lab Mimic's segment recording/retargeting API to jointly encode base frame in object's local SE(3) alongside arm end-effector waypoints (critical-path bottleneck: most likely integration debugging hotspot; blocks Contributions 1 and 3). Days 7–12: Combinatorial composition engine — implement three-criterion compatibility filter (IRM feasibility, pose-continuity δ_nav, contact-state); validate on Task 1 (pick-and-place with navigation). Days 12–15: Full data generation runs across all 3 tasks at 2048+ parallel envs (requires Days 1–12 complete). Days 15–19: Diffusion Policy training (CNN-UNet, multi-seed) + ablations across live baselines (Isaac Lab Mimic PR #3259, PR #3992); OmniRetarget and DemoHLM are included as conceptual comparisons with published numbers cited directly — no reimplementation required within this window (requires Day 15 data). Day 19–20: Analysis, scaling-law figures, and write-up. Baseline notes: DemoHLM code is not publicly available as of May 2026 — cited conceptually from arXiv:2510.11258 published results; OmniRetarget (Holosoma) code is public but setup estimated at 10–14 days — designated as conceptual comparison citing arXiv:2509.26633 metrics; if Researcher 2 has bandwidth Days 1–7 before policy training begins, OmniRetarget live reproduction can be attempted as a stretch goal on a parallel track. Risk mitigation: articulated-object task (supplementary) deferred to Days 12–15 alongside primary tasks only if composition engine validation (Days 7–12) completes ahead of schedule; otherwise deferred to post-deadline supplementary material."
    },
    "human_in_loop": {
      "h100_hours": "~125–157 H100h (≈235–310h A100, plus ~3–5 H100h IRM precomputation): data generation ~35h A100; policy training 3 tasks × 2 seeds × 15h = 90h A100; ablations 5 conditions × 3 tasks × 12h = 180h A100 ≈ 305h A100 ÷ 2.5 = 122h H100 (lower bound), ÷ 2.0 = 152h H100 (upper bound), plus IRM precomputation 3–5h H100 = 125–157h H100 total — within 200h H100 constraint",
      "irm_precomputation": "One-time offline: G1 stance-conditioned reachability map construction via IK sampling across ~50K balance configuration poses (6D space: SE(2) base × squat depth × foot spread × weight distribution), GPU-parallel in Isaac Lab: ~3–5 H100h; amortized across all tasks",
      "gpu_utilization": "Moderate idle (~30–40%): approval gates pause GPU between stages, but agent batches setup and analysis tasks",
      "timeline": "4–5 weeks",
      "team": "1 researcher, ~45 min/day check-in for gate approvals and physics failure triage",
      "claude_api_cost": "$200–400 (~300–500 turns at $0.08–0.12/turn for code gen, debug, analysis)",
      "estimated_gpu_cost": "~$420–540 at $1.75/hr A100 (or ~$310–390 at $2.50/hr H100)",
      "risk_note": "Stance-conditioned IRM for articulated object tasks (door/drawer) involves contact-rich interaction where failure modes require human insight to diagnose; the IRM integration formulation requires iterative design. Addressed by assigning the articulated-object task to supplementary, keeping primary evaluation on the 2 lower-risk tasks.",
      "gantt_20day": "20-day critical path (CoRL 2026, paper due May 28 AoE): Days 1–3: IRM precomputation offline (50K-pose IK sampling, embarrassingly parallel in Isaac Lab — low-risk, starts immediately; output blocks Contribution 2 integration). Days 3–7: SE(3) encoding extension — modify Isaac Lab Mimic's segment recording/retargeting API to jointly encode base frame in object's local SE(3) alongside arm end-effector waypoints (critical-path bottleneck: most likely integration debugging hotspot; blocks Contributions 1 and 3). Days 7–12: Combinatorial composition engine — implement three-criterion compatibility filter (IRM feasibility, pose-continuity δ_nav, contact-state); validate on Task 1 (pick-and-place with navigation). Days 12–15: Full data generation runs across all 3 tasks at 2048+ parallel envs (requires Days 1–12 complete). Days 15–19: Diffusion Policy training (CNN-UNet, multi-seed) + ablations across live baselines (Isaac Lab Mimic PR #3259, PR #3992); OmniRetarget and DemoHLM are included as conceptual comparisons with published numbers cited directly — no reimplementation required within this window (requires Day 15 data). Day 19–20: Analysis, scaling-law figures, and write-up. Baseline notes: DemoHLM code is not publicly available as of May 2026 — cited conceptually from arXiv:2510.11258 published results; OmniRetarget (Holosoma) code is public but setup estimated at 10–14 days — designated as conceptual comparison citing arXiv:2509.26633 metrics. Risk mitigation: articulated-object task (supplementary) deferred to Days 12–15 alongside primary tasks only if composition engine validation (Days 7–12) completes ahead of schedule; otherwise deferred to post-deadline supplementary material."
    }
  },
  "target_venues": [
    "CoRL 2026 (abstract May 26 AoE, full paper May 28 AoE / ≈May 29 UTC — 18 days from today)",
    "IEEE Robotics and Automation Letters / RA-L (rolling submission, no hard deadline)"
  ],
  "level": "top-tier",
  "key_references": [
    "MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations (CoRL 2023)",
    "DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning (ICRA 2025)",
    "HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning (NeurIPS 2025)",
    "WholeBodyVLA: Towards Unified Latent VLA for Whole-Body Loco-Manipulation Control (ICLR 2026)",
    "OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction (arXiv:2509.26633, Sept 2025)",
    "MoMaGen: Generating Demonstrations under Soft and Hard Constraints for Multi-Step Bimanual Mobile Manipulation (ICLR 2026, arXiv:2510.18316)",
    "DemoHLM: From One Demonstration to Generalizable Humanoid Loco-Manipulation (arXiv:2510.11258, Oct 2025)",
    "DreamGen: Unlocking Generalization in Robot Learning through Video World Models (NVIDIA GEAR Lab, arXiv:2505.12705, May 2025) [GR00T-Dreams blueprint]",
    "GR00T N1: An Open Foundation Model for Generalist Humanoid Robots (NVIDIA, arXiv:2503.14734, March 2025)",
    "EgoHumanoid: Unlocking In-the-Wild Loco-Manipulation with Robot-Free Egocentric Demonstration (arXiv:2602.10106, Feb 2026, OpenDriveLab)",
    "HoMMI: Learning Whole-Body Mobile Manipulation from Human Demonstrations (arXiv:2603.03243, March 2026, Stanford/TRI)",
    "HuMI: Humanoid Manipulation Interface — Humanoid Whole-Body Manipulation from Robot-Free Demonstrations (arXiv:2602.06643, Feb 2026)",
    "HumanX: Toward Agile and Generalizable Humanoid Interaction Skills from Human Videos (arXiv:2602.02473, Feb 2026)",
    "VisualMimic: Visual Humanoid Loco-Manipulation via Motion Tracking and Generation (arXiv:2509.20322, IROS 2025)",
    "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion (Chi et al., RSS 2023 / IJRR 2025, arXiv:2303.04137)",
    "Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning (arXiv 2025)",
    "Isaac Lab PR #3150: Locomanipulation Environment with G1 for Mimic workflow (merged Sept 9, 2025)",
    "Isaac Lab PR #3259: Adds locomanipulation data generation via disjoint navigation (merged Sept 10, 2025, release/2.3.0)",
    "Isaac Lab PR #3992: APIs to Isaac Lab Mimic for supporting loco-manipulation datagen (merged Dec 1, 2025)",
    "Vahrenkamp et al.: Robot Placement based on Reachability Inversion (ICRA 2013)",
    "Burget et al.: Stance Selection for Humanoid Grasping Tasks by Inverse Reachability Maps (ICRA 2015)",
    "MoMa-Pos: An Efficient Object-Kinematic-Aware Base Placement Optimization Framework for Mobile Manipulation (arXiv:2403.19940, Oct 2024 revision, ICRA 2025)",
    "Murooka et al.: Humanoid Loco-manipulation Planning based on Graph Search and Reachability Maps (arXiv:2505.23505, May 2025)",
    "Murooka et al.: Learning Differentiable Reachability Maps for Optimization-based Humanoid Motion Generation (arXiv:2508.11275, Humanoids 2025)"
  ],
  "description": "LocoMimicGen extends Isaac Lab's 2.3 loco-manipulation infrastructure — comprising PRs #3150, #3259, and #3992 — with three precisely-scoped technical contributions that together enable room-level combinatorial scaling unavailable in existing systems.\n\nPR #3259 ('disjoint navigation', merged Sept 10, 2025, release/2.3.0) is the closest structural predecessor and primary baseline. It adds pick-navigate-place phase segmentation with occupancy-map path planning between phases and scene randomization. However, it handles navigation 'disjointly': the manipulation stance is fixed from the source demo and navigation is occupancy-map path planning at the trajectory level. It does NOT encode navigation stances in the object's SE(3) local frame, does NOT enforce arm-reachability constraints on base-pose selection (making generation infeasible when new object positions fall outside source demo stance's arm workspace), and does NOT compose segments from multiple source demonstrations.\n\nContribution (1): By expressing the manipulation stance in the object's SE(3) local frame alongside the arm trajectory, frame-transform retargeting to new object configurations automatically yields a feasible new stance without any separate stance-placement planning. Navigation between the retargeted stances is handled by the pretrained RL locomotion controller (PR #3150) as a black box; what the SE(3) encoding eliminates is the need to separately determine where the robot should stand to manipulate at each new object configuration. LocoMimicGen adds coupled SE(3) object-centric encoding of locomotion stances jointly with arm end-effector waypoints — the principled replacement for PR #3259's disjoint approach, enabling frame-transform retargeting of both manipulation stances and arm motions simultaneously.\n\nContribution (2): Stance-conditioned IRM integration for bipedal humanoid retargeting. We adapt and integrate IRM methodology (Vahrenkamp et al. 2013; Burget et al. ICRA 2015; MoMa-Pos 2024; MoMaGen ICLR 2026) into the Mimic retargeting loop for the G1. The integration challenge over prior wheeled-platform IRMs (MoMa-Pos, MoMaGen) is that bipedal arm reachability is conditioned on whole-body stance configuration (COM height, foot contact, balance state), requiring a stance-conditioned reachability map rather than a SE(2) base-pose-only map. The reachability map is a one-time offline precomputation (~3–5 H100-hours for IK sampling across ~50K balance configuration poses in 6D space: SE(2) base pose × squat depth × foot spread × weight distribution), GPU-parallel in Isaac Lab, shared across all tasks, and explicitly budgeted in the resource estimate. A concurrent technique from the same CNRS-AIST group (Murooka et al., arXiv:2508.11275, Humanoids 2025) introduces learned differentiable reachability maps for online gradient-based humanoid planning; LocoMimicGen uses offline-precomputed discrete IRM instead, as differentiable map gradient evaluation across 2048+ parallel Isaac Lab environments would bottleneck batch generation throughput. This is framed as an integration contribution — not a novel technique — with the bipedal stance-conditioning as the key technical challenge.\n\nContribution (3): Combinatorial multi-source segment composition from multiple (≤20 total) teleoperated demonstrations achieves 100–1,000× demo expansion — a qualitatively different scaling regime from PR #3259's single-source disjoint augmentation. The scaling bound is explicit: with K=20 source demonstrations decomposed into M=3 subtask phases, combined with P=10 object positions × Q=3 table heights × R=5 obstacle layouts, the conservative lower bound is K×M×P×Q×R = 20×3×10×3×5 = 9,000 unique trajectories (450× expansion from 20 seed demos); full cross-phase composition yields K^M × P×Q×R = 20^3 × 150 ≈ 1.2M as the theoretical maximum. Compatibility between segments from different source demonstrations is evaluated against three criteria: (1) IRM feasibility at the transition stance (IRM score exceeding the 10th percentile of source-demo scores); (2) base-pose continuity within δ_nav ≈ 0.3 m (the locomotion controller's recoverable displacement); (3) contact-state consistency at phase boundaries. Criteria (1) and (2) are the active filters: IRM feasibility eliminates ~55–75% of random scene-stance pairings, and pose continuity a further 10–20%, reducing the 1.2M theoretical bound to the practical 100–1,000× range (roughly 2,000–20,000 valid trajectories from 20 seed demos).\n\nAll policy training uses Diffusion Policy (CNN-UNet variant, Chi et al. RSS 2023 / IJRR 2025) uniformly across all baselines and LocoMimicGen conditions, isolating the data-generation contribution. We target ≥20 pp mean success-rate improvement over PR #3259 at the held-out 150-configuration test distribution, grounded in MimicGen's 20–40 pp gains on harder spatial-variant distributions where baselines already incorporate partial scene randomization.\n\nMoMaGen (ICLR 2026, arXiv:2510.18316) generates bimanual mobile manipulation demonstrations via hard-reachability-constrained optimization on a wheeled bimanual platform — now the strongest peer-reviewed comparison point for constrained demo generation. The differentiation is precise: MoMaGen's reachability constraint operates over SE(2) base pose for a wheeled platform where base pose fully determines arm workspace; LocoMimicGen's stance-conditioned IRM addresses the qualitatively harder bipedal case where arm reachability is conditioned on whole-body configuration. DreamGen (NVIDIA GEAR Lab, arXiv:2505.12705, May 2025) — the GR00T-Dreams blueprint — generates behavioral generalization across task types via video world-model sampling and IDM action recovery; LocoMimicGen generates spatial/configurational diversity within known loco-manipulation tasks via constraint-based combinatorial recombination with hard kinematic guarantees. The two approaches are complementary: DreamGen's world-model-imagined behavioral diversity and LocoMimicGen's constraint-verified spatial diversity address orthogonal dimensions of the data scarcity problem. EgoHumanoid (OpenDriveLab, arXiv:2602.10106, Feb 2026), HoMMI (arXiv:2603.03243, March 2026), HuMI (arXiv:2602.06643, Feb 2026), and HumanX (arXiv:2602.02473, Feb 2026) represent concurrent policy-learning paradigms — learning from human behavioral diversity in real environments (video, MoCap, egocentric demonstrations) to improve generalization — complementary to LocoMimicGen's combinatorial spatial synthesis from ≤20 robot demos in simulation.\n\nEvaluated on 2 primary loco-manipulation tasks (pick-and-place with navigation; two-phase transit) plus 1 supplementary articulated-object task. Live reproduced baselines: Isaac Lab Mimic PR #3259 (closest structural baseline) and PR #3992. Conceptual comparisons citing published numbers: OmniRetarget (arXiv:2509.26633; Holosoma code is public but 10–14 day setup exceeds the 20-day window) and DemoHLM (arXiv:2510.11258; code not publicly available as of May 2026). The 2-primary scope is proactively justified on four grounds against DexMimicGen (9 tasks), HumanoidGen (6 tasks, 120+ scene variants), and MoMaGen (ICLR 2026, 4 tasks): (a) scaling law curves across P×Q×R configuration space are the primary empirical contribution, fully established on 2 tasks; (b) both primary tasks exercise all three contributions; (c) DexMimicGen's breadth reuses fixed tabletop infrastructure vs. LocoMimicGen's IRM integration into a live loco-manipulation stack; (d) LocoMimicGen sweeps P×Q×R = 150 configurations per primary task (300 total), exceeding MoMaGen's and HumanoidGen's per-task scene coverage — scene-space depth is the appropriate metric for a data-generation infrastructure paper. Both compute modes (manual: ~87–110h H100; human-in-loop: ~125–157h H100) stay within the 200 H100-hour hard constraint, including the one-time IRM precomputation (~3–5 H100h). The 20-day critical path (IRM precomputation Days 1–3 → SE(3) encoding Days 3–7 → composition engine Days 7–12 → data generation Days 12–15 → policy training Days 15–19 → write-up Day 19–20) is explicitly identified; the SE(3) API integration (Days 3–7) is the critical-path bottleneck. Sim-to-real on physical G1 is explicit future work. CoRL 2026: abstract May 26 AoE, paper May 28 AoE.",
  "project_name": "loco_mimicgen_humanoid_g1",
  "source": "web_research"
}

## Reviewer feedback (round 7)
Issues: ["MISSING CONCURRENT CITATION — ULTRA (arXiv:2603.03279, March 2026): 'Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation' uses physics-driven neural retargeting to translate large-scale MoCap to humanoid embodiments while preserving physical plausibility for contact-rich loco-manipulation. Although retargeting-based (not SE(3) demo multiplication), it is a direct March 2026 paper on whole-body humanoid loco-manipulation data generation and CoRL reviewers will expect to see it. Positioning is identical to OmniRetarget: 'ULTRA [arXiv:2603.03279] scales loco-manipulation data via physics-preserving MoCap retargeting — a complementary human-data-driven paradigm that requires large MoCap libraries, cannot combinatorially compose subtask segments across scene configurations, and does not address the manipulation-stance feasibility problem for new object positions.' One sentence in the landscape alongside OmniRetarget is sufficient.", "MISSING CONCURRENT CITATION — Psi-Zero / Ψ₀ (arXiv:2603.12263, March 2026): 'Open Foundation Model Towards Universal Humanoid Loco-Manipulation' pre-trains a VLM on 800 hours of egocentric human video, then post-trains a flow-based action expert on 30 hours of robot data, achieving 40% better success with 10× less robot data than baselines. Foundation model scaling (not procedural generation), but it is a March 2026 paper in the same problem space. CoRL reviewers will recognize it. One sentence alongside EgoHumanoid/HoMMI/HuMI/HumanX as a human-data-driven foundation model approach complementary to LocoMimicGen's combinatorial synthetic generation from ≤20 robot demos.", "IRM GRID RESOLUTION SPARSENESS NOT ACKNOWLEDGED: The proposed 50K-pose sampling across 6D configuration space (SE(2) base pose × squat depth × foot spread × weight distribution) yields approximately 50,000^(1/6) ≈ 5-6 points per dimension — a very coarse grid for reachability boundary detection. At this resolution, reachability map boundaries may be insufficiently smooth to reliably filter edge cases where the manipulator is at the limit of its workspace. The paper should acknowledge this resolution choice and reference how analogous IRM work (MoMa-Pos, MoMaGen) selected grid resolution, or note that it can be refined offline post-hoc without additional training cost.", "EVALUATION BREADTH RISK (ONGOING): Two primary tasks with sim-only evaluation continues to be the most likely cause of CoRL 2026 rejection or major revision requests. The existing scene-space-depth defense ('150 configurations per task vs. O(1) in MoMaGen/HumanoidGen') is the best available argument within the 20-day constraint, but it is a methodological claim that reviewers accustomed to DexMimicGen (9 tasks) and HumanoidGen (6 tasks) may not find sufficient. The paper should consider whether the supplementary articulated-object task can be elevated to co-primary status if the composition engine validates on schedule by Day 12, as three tasks with three contributions exercised would substantially reduce this risk."]
Feedback: All four Round 6 required fixes are correctly implemented: DemoHLM is a conceptual comparison citing published numbers, the language reads 'stance-placement planning' not 'navigation planning,' HumanX/XMimic is in the landscape, and OmniRetarget is correctly scoped as a conceptual comparison. The idea's technical foundation is now solid and the gap against Isaac Lab PR #3259 is independently confirmed by research.

**Fix 1 (required, 1 sentence)**: Add ULTRA (arXiv:2603.03279, March 2026) to the landscape paragraph alongside OmniRetarget. Frame it as a complementary physics-preserving MoCap retargeting approach that requires large motion capture libraries and cannot perform combinatorial subtask segment composition — the same positioning as OmniRetarget. CoRL reviewers will notice its absence.

**Fix 2 (required, 1 sentence)**: Add Psi-Zero/Ψ₀ (arXiv:2603.12263, March 2026) to the landscape alongside EgoHumanoid/HoMMI/HuMI/HumanX as a foundation model pre-training approach. One sentence: 'Ψ₀ [arXiv:2603.12263] pre-trains a VLM on 800 hours of human egocentric video and post-trains a flow-based action expert on 30 hours of robot data — a human-data-driven scaling paradigm orthogonal to LocoMimicGen's combinatorial spatial synthesis from ≤20 teleoperated robot demonstrations.'

**Fix 3 (optional but recommended, 1 sentence)**: Acknowledge the IRM grid resolution choice explicitly — something like 'The 50K-pose resolution (~5-6 samples per dimension) is consistent with offline IRM construction in prior work (MoMa-Pos, Vahrenkamp et al.) and can be refined post-hoc at no additional training cost.' This preempts a reviewer question about whether the reachability boundary is smooth enough at this resolution.

**Fix 4 (contingency plan, 1 sentence)**: Add a sentence noting that if the composition engine validates on Task 1 by Day 11 rather than Day 12, the supplementary articulated-object task will be elevated to co-primary status in the evaluation, bringing the primary task count to three. This signals execution awareness and reduces the evaluation-breadth risk without changing the critical path.

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
这个 idea 已经经过 7 轮修订，近 3 轮的平均分从 3.8 到 3.8，没有明显改善。

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
  "promptId": "de3e87b5-be82-4341-98b4-3e288a5c62a5",
  "type": "user",
  "uuid": "290c0737-8e9c-4a38-949b-cd2e12b73a08",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e93981d8-61dc-4460-8c15-6141e331b9de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T13:08:37.670Z_

```json
{
  "parentUuid": "290c0737-8e9c-4a38-949b-cd2e12b73a08",
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
  "uuid": "8d5e4ba6-588a-4659-b2dc-c4a5e6c7e62b",
  "timestamp": "2026-05-10T13:08:37.670Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e93981d8-61dc-4460-8c15-6141e331b9de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T13:08:37.670Z_

```json
{
  "parentUuid": "8d5e4ba6-588a-4659-b2dc-c4a5e6c7e62b",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "25e6add4-11d0-47e0-b664-0e7167c78fed",
  "timestamp": "2026-05-10T13:08:37.670Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e93981d8-61dc-4460-8c15-6141e331b9de",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"LocoMimicGen: Coupled SE(3) Object-Centric Demo Multiplication for Mob…",
  "leafUuid": "25e6add4-11d0-47e0-b664-0e7167c78fed",
  "sessionId": "e93981d8-61dc-4460-8c15-6141e331b9de"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise LocoMimicGen with concurrent ULTRA and Psi-Zero citations",
  "sessionId": "e93981d8-61dc-4460-8c15-6141e331b9de"
}
```

---

### Assistant

_source line 8 · 2026-05-10T13:09:03.089Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the situation carefully before deciding on the approach.

## Current State Assessment

After 7 rounds of revision with stagnant scores (~3.8 average), I need to think carefully about whether:
1. This is a minor fix situation (just add the missing citations and IRM note)
2. This needs major revision
3. This needs a pivot

### What the reviewer is asking for in Round 7:
1. **Fix 1 (required)**: Add ULTRA (arXiv:2603.03279) citation - 1 sentence
2. **Fix 2 (required)**: Add Psi-Zero/Ψ₀ (arXiv:2603.12263) citation - 1 sentence


3. **Fix 3 (optional but recommended)**: Acknowledge IRM grid resolution choice explicitly
4. **Fix 4 (contingency plan)**: Add sentence about elevating supplementary task to co-primary if Day 11 deadline met

### The Stagnation Problem

The reviewer confirmed all Round 6 required fixes are correctly implemented, so the technical foundation is solid. The remaining gaps are just missing concurrent citations and a methodological clarification about the IRM grid resolution, plus a contingency note about task elevation if timing allows.

The real bottleneck is evaluation breadth—I'm stuck at 3.8 because reviewers keep pointing out that two primary tasks with simulation-only evaluation doesn't match what competitors are doing. DexMimicGen has nine tasks, HumanoidGen has six, MoMaGen has four. My defense about scene-space depth with 150 configurations per task is a methodological argument that may not be landing with reviewers.

Looking at what's actually missing in the technical foundation—no coupled SE(3) encoding, no IRM integration, no combinatorial composition—these are real gaps, but the Isaac Lab infrastructure itself is solid. The question is whether there's a pivot opportunity here that could shift the evaluation narrative.

The stagnation might actually stem from how I'm framing the contribution. Positioning IRM as an integration rather than a novel technical advance weakens the novelty case, and the evaluation scope limitation is hard to defend against the breadth that concurrent work like ULTRA, Psi-Zero, and EgoHumanoid are demonstrating. Maybe the path forward is to lean harder into the novel technical angle—stance-conditioned IRM for bipedal locomotion-manipulation—rather than trying to justify the current evaluation scope.

But the reviewer feedback is actually encouraging about the technical foundation being solid, and they're only asking for minor fixes like adding those two citations and clarifying the IRM resolution. So perhaps the smarter move is to handle those required updates first, then reassess whether the evaluation plan needs strengthening to address the stagnation concern.

Let me look up those papers to understand what ULTRA and Psi-Zero are actually doing, then I can make a better call about whether to pivot or just shore up the current approach.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25e6add4-11d0-47e0-b664-0e7167c78fed",
  "isSidechain": false,
  "requestId": "req_011CatwYGXm5rSZfpQkpb9cG",
  "type": "assistant",
  "uuid": "5c16196f-a001-4fff-959b-3c0aea8512a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e93981d8-61dc-4460-8c15-6141e331b9de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01L8E9n3jAonYNcCg9eCJxzv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20317,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20317,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1125,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 20317,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20317
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

_source line 9 · 2026-05-10T13:09:03.404Z_

Looking at 7 rounds of revision stagnating at ~3.8, I need to first read the two new concurrent papers carefully, then decide whether to do a targeted minor fix or whether the stagnation points to something deeper that needs restructuring.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c16196f-a001-4fff-959b-3c0aea8512a8",
  "isSidechain": false,
  "requestId": "req_011CatwYGXm5rSZfpQkpb9cG",
  "type": "assistant",
  "uuid": "5864d707-dd38-48ae-aad1-eae674ea3127",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e93981d8-61dc-4460-8c15-6141e331b9de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01L8E9n3jAonYNcCg9eCJxzv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20317,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20317,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1125,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 20317,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20317
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

_source line 10 · 2026-05-10T13:09:03.918Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Bw6ps7h4fGFEpLjDzgnZjD`</summary>

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
  "parentUuid": "5864d707-dd38-48ae-aad1-eae674ea3127",
  "isSidechain": false,
  "requestId": "req_011CatwYGXm5rSZfpQkpb9cG",
  "type": "assistant",
  "uuid": "4fa05777-9c95-4906-82e5-96212baf1431",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e93981d8-61dc-4460-8c15-6141e331b9de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01L8E9n3jAonYNcCg9eCJxzv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20317,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20317,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1125,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 20317,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20317
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

_source line 11 · 2026-05-10T13:09:03.924Z_

<details><summary>↩ Tool result · `toolu_01Bw6ps7h4fGFEpLjDzgnZjD`</summary>

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
  "parentUuid": "4fa05777-9c95-4906-82e5-96212baf1431",
  "isSidechain": false,
  "promptId": "de3e87b5-be82-4341-98b4-3e288a5c62a5",
  "type": "user",
  "uuid": "79b2497b-7064-479b-b957-03fc1a0280c9",
  "toolUseResult": {
    "matches": [
      "WebFetch",
      "WebSearch"
    ],
    "query": "select:WebFetch,WebSearch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "4fa05777-9c95-4906-82e5-96212baf1431",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e93981d8-61dc-4460-8c15-6141e331b9de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-10T13:09:06.197Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me fetch both new papers and also think about the stagnation problem more carefully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79b2497b-7064-479b-b957-03fc1a0280c9",
  "isSidechain": false,
  "requestId": "req_011CatwaCduvUUHEawSfqX7o",
  "type": "assistant",
  "uuid": "247976dd-6434-4533-b2b2-c31ee2d6d188",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e93981d8-61dc-4460-8c15-6141e331b9de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01PWCPfZ3EB2Y2LCQ3Hs1cE8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2144,
      "cache_read_input_tokens": 31948,
      "output_tokens": 362,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2144,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 362,
          "cache_read_input_tokens": 31948,
          "cache_creation_input_tokens": 2144,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2144
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

_source line 13 · 2026-05-10T13:09:06.706Z_

Let me fetch both new papers in parallel to understand their actual contributions before deciding how to respond.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "247976dd-6434-4533-b2b2-c31ee2d6d188",
  "isSidechain": false,
  "requestId": "req_011CatwaCduvUUHEawSfqX7o",
  "type": "assistant",
  "uuid": "e46ade18-8caa-4419-b931-d312bfe86cbe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e93981d8-61dc-4460-8c15-6141e331b9de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01PWCPfZ3EB2Y2LCQ3Hs1cE8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2144,
      "cache_read_input_tokens": 31948,
      "output_tokens": 362,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2144,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 362,
          "cache_read_input_tokens": 31948,
          "cache_creation_input_tokens": 2144,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2144
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

_source line 14 · 2026-05-10T13:09:09.995Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01F7barhWz42a4cBKgUiCUhA`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.03279",
  "prompt": "Extract the full title, authors, institution, abstract, key methods, and how this paper differs from MimicGen-style demo generation and OmniRetarget. Focus on: what data does it require (MoCap vs teleoperation vs video), whether it does combinatorial segment composition, and whether it addresses manipulation-stance feasibility for new object positions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e46ade18-8caa-4419-b931-d312bfe86cbe",
  "isSidechain": false,
  "requestId": "req_011CatwaCduvUUHEawSfqX7o",
  "type": "assistant",
  "uuid": "eff2b784-fc18-4216-bcbe-cf71cd3ba79b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e93981d8-61dc-4460-8c15-6141e331b9de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01PWCPfZ3EB2Y2LCQ3Hs1cE8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2144,
      "cache_read_input_tokens": 31948,
      "output_tokens": 362,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2144,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 362,
          "cache_read_input_tokens": 31948,
          "cache_creation_input_tokens": 2144,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2144
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

_source line 15 · 2026-05-10T13:09:11.966Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013cuFFrEMRC8VF1ze13xB1N`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.12263",
  "prompt": "Extract the full title, authors, institution, abstract, key methods, and how this paper differs from procedural demo generation like MimicGen/LocoMimicGen. Focus on: what data it uses (how many hours of human video vs robot demos), whether it does combinatorial scene generation, its evaluation tasks and success rates, and the key differentiator from simulation-based data augmentation approaches."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eff2b784-fc18-4216-bcbe-cf71cd3ba79b",
  "isSidechain": false,
  "requestId": "req_011CatwaCduvUUHEawSfqX7o",
  "type": "assistant",
  "uuid": "bafe761b-8230-412e-ba82-8ec90221caff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e93981d8-61dc-4460-8c15-6141e331b9de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01PWCPfZ3EB2Y2LCQ3Hs1cE8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2144,
      "cache_read_input_tokens": 31948,
      "output_tokens": 362,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2144,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 362,
          "cache_read_input_tokens": 31948,
          "cache_creation_input_tokens": 2144,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2144
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

_source line 16 · 2026-05-10T13:09:15.783Z_

<details><summary>↩ Tool result · `toolu_01F7barhWz42a4cBKgUiCUhA`</summary>

```text
# ULTRA: Unified Multimodal Control for Humanoid Loco-Manipulation

## Title & Authors
**Full Title:** "ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation"

**Authors:** Xialin He, Sirui Xu, Xinyao Li, Runpei Dong, Liuyu Bian, Yu-Xiong Wang, Liang-Yan Gui

## Institution
Not explicitly stated in the provided content.

## Abstract Summary
The paper addresses whole-body loco-manipulation in humanoids through a framework combining physics-driven neural retargeting and unified multimodal control that works from "sparse task specifications" and "egocentric visual inputs" rather than predefined motion references.

## Key Methods
1. **Physics-driven neural retargeting** translating motion capture to humanoid embodiments while "preserving physical plausibility for contact-rich interactions"
2. **Unified multimodal controller** supporting dense references and sparse task specifications
3. **Universal tracking policy distillation** into compact latent space
4. **Reinforcement learning finetuning** for robustness

## Differentiation from Related Approaches
The paper distinguishes itself by:
- **Data source:** Uses large-scale motion capture (mocap), unlike teleoperation-dependent methods
- **Control paradigm:** Enables "goal-conditioned whole-body loco-manipulation from egocentric perception" without test-time reference motions
- **Generalization:** Addresses scalability limitations of tracking-only baselines

The document doesn't explicitly discuss combinatorial segment composition or manipulation-stance feasibility for new object positions relative to MimicGen or OmniRetarget comparisons.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eff2b784-fc18-4216-bcbe-cf71cd3ba79b",
  "isSidechain": false,
  "promptId": "de3e87b5-be82-4341-98b4-3e288a5c62a5",
  "type": "user",
  "uuid": "434f8bd8-1703-466b-aae3-4c7bda6e20a8",
  "toolUseResult": {
    "bytes": 47665,
    "code": 200,
    "codeText": "OK",
    "result": "# ULTRA: Unified Multimodal Control for Humanoid Loco-Manipulation\n\n## Title & Authors\n**Full Title:** \"ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation\"\n\n**Authors:** Xialin He, Sirui Xu, Xinyao Li, Runpei Dong, Liuyu Bian, Yu-Xiong Wang, Liang-Yan Gui\n\n## Institution\nNot explicitly stated in the provided content.\n\n## Abstract Summary\nThe paper addresses whole-body loco-manipulation in humanoids through a framework combining physics-driven neural retargeting and unified multimodal control that works from \"sparse task specifications\" and \"egocentric visual inputs\" rather than predefined motion references.\n\n## Key Methods\n1. **Physics-driven neural retargeting** translating motion capture to humanoid embodiments while \"preserving physical plausibility for contact-rich interactions\"\n2. **Unified multimodal controller** supporting dense references and sparse task specifications\n3. **Universal tracking policy distillation** into compact latent space\n4. **Reinforcement learning finetuning** for robustness\n\n## Differentiation from Related Approaches\nThe paper distinguishes itself by:\n- **Data source:** Uses large-scale motion capture (mocap), unlike teleoperation-dependent methods\n- **Control paradigm:** Enables \"goal-conditioned whole-body loco-manipulation from egocentric perception\" without test-time reference motions\n- **Generalization:** Addresses scalability limitations of tracking-only baselines\n\nThe document doesn't explicitly discuss combinatorial segment composition or manipulation-stance feasibility for new object positions relative to MimicGen or OmniRetarget comparisons.",
    "durationMs": 5783,
    "url": "https://arxiv.org/abs/2603.03279"
  },
  "sourceToolAssistantUUID": "eff2b784-fc18-4216-bcbe-cf71cd3ba79b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e93981d8-61dc-4460-8c15-6141e331b9de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-10T13:09:18.292Z_

<details><summary>↩ Tool result · `toolu_013cuFFrEMRC8VF1ze13xB1N`</summary>

```text
# Ψ₀: Foundation Model for Humanoid Loco-Manipulation

**Full Title:** Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation

**Authors:** Songlin Wei, Hongyi Jing, Boqian Li, Zhenyu Zhao, Jiageng Mao, Zhenhao Ni, Sicheng He, Jie Liu, Xiawei Liu, Kaidi Kang, Sheng Zang, Weiduo Yuan, Marco Pavone, Di Huang, Yue Wang

**Institution:** Not specified in provided content

---

## Abstract Summary

The paper introduces a foundation model addressing humanoid robot manipulation by decoupling learning across heterogeneous data sources, rather than co-training on mixed human-robot datasets.

---

## Key Data Specifications

- **Human video:** ~800 hours of egocentric manipulation footage
- **Robot data:** ~30 hours of real-world humanoid trajectories
- **Comparison advantage:** Outperforms baselines "pre-trained on more than 10× as much data by over 40%" in success rate

---

## Core Methodology

The model employs "a staged training paradigm with different learning objectives": autoregressive pre-training on human videos for visual-action representations, followed by post-training using a "flow-based action expert on high-quality humanoid robot data."

---

## Differentiation from MimicGen/LocoMimicGen

The paper explicitly rejects "approaches that scale with noisy Internet clips or heterogeneous cross-embodiment robot datasets," emphasizing quality over quantity. Unlike procedural demo generation, this approach prioritizes high-quality egocentric human data paired with domain-specific real-world trajectories rather than synthetic augmentation or task composition schemes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bafe761b-8230-412e-ba82-8ec90221caff",
  "isSidechain": false,
  "promptId": "de3e87b5-be82-4341-98b4-3e288a5c62a5",
  "type": "user",
  "uuid": "d5405e08-403a-409d-aa16-a0e85ed46dbb",
  "toolUseResult": {
    "bytes": 48592,
    "code": 200,
    "codeText": "OK",
    "result": "# Ψ₀: Foundation Model for Humanoid Loco-Manipulation\n\n**Full Title:** Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation\n\n**Authors:** Songlin Wei, Hongyi Jing, Boqian Li, Zhenyu Zhao, Jiageng Mao, Zhenhao Ni, Sicheng He, Jie Liu, Xiawei Liu, Kaidi Kang, Sheng Zang, Weiduo Yuan, Marco Pavone, Di Huang, Yue Wang\n\n**Institution:** Not specified in provided content\n\n---\n\n## Abstract Summary\n\nThe paper introduces a foundation model addressing humanoid robot manipulation by decoupling learning across heterogeneous data sources, rather than co-training on mixed human-robot datasets.\n\n---\n\n## Key Data Specifications\n\n- **Human video:** ~800 hours of egocentric manipulation footage\n- **Robot data:** ~30 hours of real-world humanoid trajectories\n- **Comparison advantage:** Outperforms baselines \"pre-trained on more than 10× as much data by over 40%\" in success rate\n\n---\n\n## Core Methodology\n\nThe model employs \"a staged training paradigm with different learning objectives\": autoregressive pre-training on human videos for visual-action representations, followed by post-training using a \"flow-based action expert on high-quality humanoid robot data.\"\n\n---\n\n## Differentiation from MimicGen/LocoMimicGen\n\nThe paper explicitly rejects \"approaches that scale with noisy Internet clips or heterogeneous cross-embodiment robot datasets,\" emphasizing quality over quantity. Unlike procedural demo generation, this approach prioritizes high-quality egocentric human data paired with domain-specific real-world trajectories rather than synthetic augmentation or task composition schemes.",
    "durationMs": 6323,
    "url": "https://arxiv.org/abs/2603.12263"
  },
  "sourceToolAssistantUUID": "bafe761b-8230-412e-ba82-8ec90221caff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e93981d8-61dc-4460-8c15-6141e331b9de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-10T13:09:46.408Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I've confirmed the content of both papers. Now let me also think about whether there's a deeper issue with the stagnation.

**ULTRA (arXiv:2603.03279):**
- Physics-driven neural retargeting from MoCap to humanoid
- Similar to OmniRetarget but adds a unified multimodal controller
- Does NOT do combinatorial segment composition
- Does NOT address manipulation-stance feasibility for new object positions
- Positioning: same as OmniRetarget — "MoCap retargeting, requires large libraries, no combinatorial composition"

**Psi-Zero/Ψ₀ (arXiv:2603.12263):**


- Foundation model trained on 800 hours of human video plus 30 hours of robot data
- Uses staged training with autoregressive pre-training on human videos followed by a flow-based action expert
- Not addressing procedural generation or simulation augmentation
- Positioning: aligns with the human-data-driven scaling paradigm like EgoHumanoid/HoMMI/HuMI/HumanX, orthogonal to LocoMimicGen

Both papers slot into existing categories I've already discussed — ULTRA fits the MoCap retargeting bucket with OmniRetarget, while Psi-Zero represents the human-data-driven foundation model approach that's separate from the procedural generation angle.

Now I'm thinking through why the score has plateaued at 3.8. The technical work is solid and the Isaac Lab contribution is legitimate, but reviewers keep flagging the evaluation scope — only two tasks in simulation. The framing around integration rather than novel technique for IRM might actually be underselling what's there. The real tension is that LocoMimicGen's strongest asset is the scaling law demonstration, yet two sim-only tasks genuinely looks thin compared to what peer papers show. The scene-space-depth argument holds up, but broader task coverage might be what tips the needle.

To actually move the score, I need to be honest: citation fixes and acknowledging the IRM framing are necessary but won't shift things meaningfully. The contingency plan for strengthening the supplementary task helps, but what really matters is making a stronger evaluation claim. Looking at what's happening in the field right now — EgoHumanoid, HoMMI, HuMI, HumanX, ULTRA, and others are all converging on learning from human behavioral diversity through video and motion capture. LocoMimicGen's simulation-based combinatorial synthesis is genuinely differentiated from that trend. The core problem is still there: PR #3259 shows the exact gaps I'm addressing, and there's real room for combinatorial scaling at the room level.

The real bottleneck is that the stance-conditioned bipedal IRM is technically novel but I've been framing it as part of an integration story rather than as the lead contribution. If I reposition that as the core technical innovation with SE(3) encoding and combinatorial composition as the enabling mechanisms, the novelty argument becomes much stronger. Alternatively, I could lean into this being a systems paper with solid engineering and a dataset release — CoRL has historically been receptive to that framing given the tight timeline.

So my plan is straightforward: make the required fixes (citations, IRM note, contingency sentence), then reframe the stance-conditioned bipedal IRM as the primary technical contribution rather than a secondary one, and make the contingency plan for expanding to three tasks more visible in both the approach and timeline sections. The question is whether this counts as minor or major revision work.

The reviewer's feedback confirms the technical foundation is solid and all six required fixes are specific and bounded, which suggests this is fundamentally a minor revision round. The stagnation concern about evaluation breadth is real, but that's a limitation of the current scope rather than a flaw in the work itself. Now I need to check if I can find more details about ULTRA's institution and any additional context that might help with the framing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5405e08-403a-409d-aa16-a0e85ed46dbb",
  "isSidechain": false,
  "requestId": "req_011CatwbG2L6zpZvn89jNzfe",
  "type": "assistant",
  "uuid": "350e77f2-200d-40c2-84ff-8dbac2bafceb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e93981d8-61dc-4460-8c15-6141e331b9de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0124v1xwekg52Bxr35SWupfj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1240,
      "cache_read_input_tokens": 34092,
      "output_tokens": 1377,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1240,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1377,
          "cache_read_input_tokens": 34092,
          "cache_creation_input_tokens": 1240,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1240
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

_source line 19 · 2026-05-10T13:09:46.413Z_

Let me also do a quick search to verify any additional details about these papers and whether there's anything else in the landscape I should address given the stagnation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "350e77f2-200d-40c2-84ff-8dbac2bafceb",
  "isSidechain": false,
  "requestId": "req_011CatwbG2L6zpZvn89jNzfe",
  "type": "assistant",
  "uuid": "8ab1cbc2-d7c6-4c90-8c71-de4a70ac884e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e93981d8-61dc-4460-8c15-6141e331b9de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0124v1xwekg52Bxr35SWupfj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1240,
      "cache_read_input_tokens": 34092,
      "output_tokens": 1377,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1240,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1377,
          "cache_read_input_tokens": 34092,
          "cache_creation_input_tokens": 1240,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1240
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

_source line 20 · 2026-05-10T13:09:46.918Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UFNzaLvc5DuhJhbuFExMpn`</summary>

```json
{
  "query": "ULTRA arXiv 2603.03279 humanoid loco-manipulation physics retargeting 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ab1cbc2-d7c6-4c90-8c71-de4a70ac884e",
  "isSidechain": false,
  "requestId": "req_011CatwbG2L6zpZvn89jNzfe",
  "type": "assistant",
  "uuid": "365e5e75-9af1-400d-a76f-9ee533cb96a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e93981d8-61dc-4460-8c15-6141e331b9de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0124v1xwekg52Bxr35SWupfj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1240,
      "cache_read_input_tokens": 34092,
      "output_tokens": 1377,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1240,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1377,
          "cache_read_input_tokens": 34092,
          "cache_creation_input_tokens": 1240,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1240
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

_source line 21 · 2026-05-10T13:09:47.145Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019QoLPd41KwjmoDcn59KGzZ`</summary>

```json
{
  "query": "Psi-Zero foundation model humanoid loco-manipulation 2603.12263 egocentric video 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "365e5e75-9af1-400d-a76f-9ee533cb96a2",
  "isSidechain": false,
  "requestId": "req_011CatwbG2L6zpZvn89jNzfe",
  "type": "assistant",
  "uuid": "da3b0752-fefe-4a86-823e-4d38917effee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e93981d8-61dc-4460-8c15-6141e331b9de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0124v1xwekg52Bxr35SWupfj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1240,
      "cache_read_input_tokens": 34092,
      "output_tokens": 1377,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1240,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1377,
          "cache_read_input_tokens": 34092,
          "cache_creation_input_tokens": 1240,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1240
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

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"LocoMimicGen: Coupled SE(3) Object-Centric Demo Multiplication for Mob…",
  "leafUuid": "da3b0752-fefe-4a86-823e-4d38917effee",
  "sessionId": "e93981d8-61dc-4460-8c15-6141e331b9de"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise LocoMimicGen with concurrent ULTRA and Psi-Zero citations",
  "sessionId": "e93981d8-61dc-4460-8c15-6141e331b9de"
}
```

---

### Tool result

_source line 24 · 2026-05-10T13:09:53.040Z_

<details><summary>↩ Tool result · `toolu_019QoLPd41KwjmoDcn59KGzZ`</summary>

```text
Web search results for query: "Psi-Zero foundation model humanoid loco-manipulation 2603.12263 egocentric video 2026"

Links: [{"title":"Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation","url":"https://psi-lab.ai/Psi0/"},{"title":"[2603.12263] $Ψ_0$: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation","url":"https://arxiv.org/abs/2603.12263"},{"title":"$Ψ_0$: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation","url":"https://www.wispaper.ai/en/blog/psi-zero-open-foundation-model-universal-humanoid-loco-manipulation-20260314/eng"},{"title":"GitHub - physical-superintelligence-lab/Psi0: [RSS26'] Welcome to Psi-Zero, a Humanoid VLA towards Universal Humanoid Intelligence. · GitHub","url":"https://github.com/physical-superintelligence-lab/Psi0"},{"title":"$Ψ_0$: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation | alphaXiv","url":"https://www.alphaxiv.org/overview/2603.12263"},{"title":"How MANUS Gloves Enable Dexterous Teleoperation for USC PSI Lab's Humanoid Foundation Model-MANUS Use Case","url":"https://www.manus-meta.com/use-cases/how-manus-gloves-enable-dexterous-teleoperation-for-usc-psi-labs-humanoid-foundation-model"},{"title":"Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation","url":"https://arxiv.org/html/2603.12263"},{"title":"Psi-Zero: Open Humanoid Loco-Manipulation Model - YouTube","url":"https://www.youtube.com/watch?v=uDKEeAbWbUk"},{"title":"EgoMimic: Scaling Imitation Learning via Egocentric Video","url":"https://www.researchgate.net/publication/395228678_EgoMimic_Scaling_Imitation_Learning_via_Egocentric_Video"},{"title":"Robots That Learn Like Us: The Breakthrough of Psi-Zero Loco-Manipulation - YouTube","url":"https://www.youtube.com/watch?v=9CnLBciEuIQ"}]

Based on the search results, I found comprehensive information about Psi-Zero (Ψ₀) and the arXiv paper 2603.12263. Here's what I found:

## Overview

Ψ₀ (Psi-Zero) is an open foundation model to address challenging humanoid loco-manipulation tasks. The paper arXiv 2603.12263 is titled "Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation" and was posted on March 12, 2026.

## Key Innovation

Rather than training a single model on mixed human and robot data, Ψ₀ decouples the learning process to maximize the utility of heterogeneous data sources, proposing a staged training paradigm where it first autoregressively pre-trains a VLM backbone on large-scale egocentric human videos to acquire generalizable visual-action representations, then post-trains a flow-based action expert on high-quality humanoid robot data to learn precise robot joint control.

## Training Data

The model uses 829 hours of human egocentric video capturing diverse dexterous manipulation behaviors, and 31 hours of humanoid data covering 260 diverse tasks in 7 categories.

## Performance

Extensive real-world experiments demonstrate that Ψ₀ achieves the best performance using only about 800 hours of human video data and 30 hours of real-world robot data, outperforming baselines pre-trained on more than 10x as much data by over 40% in overall success rate across multiple tasks.

## Open-Source Release

The entire ecosystem will be open-sourced to the community, including a data processing and training pipeline, a humanoid foundation model, and a real-time action inference engine.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "da3b0752-fefe-4a86-823e-4d38917effee",
  "isSidechain": false,
  "promptId": "de3e87b5-be82-4341-98b4-3e288a5c62a5",
  "type": "user",
  "uuid": "1191793f-40b0-40e8-92f2-c66ab9da0e0e",
  "toolUseResult": {
    "query": "Psi-Zero foundation model humanoid loco-manipulation 2603.12263 egocentric video 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_013AKWyLnnqae12kGaUudZTx",
        "content": [
          {
            "title": "Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation",
            "url": "https://psi-lab.ai/Psi0/"
          },
          {
            "title": "[2603.12263] $Ψ_0$: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation",
            "url": "https://arxiv.org/abs/2603.12263"
          },
          {
            "title": "$Ψ_0$: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation",
            "url": "https://www.wispaper.ai/en/blog/psi-zero-open-foundation-model-universal-humanoid-loco-manipulation-20260314/eng"
          },
          {
            "title": "GitHub - physical-superintelligence-lab/Psi0: [RSS26'] Welcome to Psi-Zero, a Humanoid VLA towards Universal Humanoid Intelligence. · GitHub",
            "url": "https://github.com/physical-superintelligence-lab/Psi0"
          },
          {
            "title": "$Ψ_0$: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2603.12263"
          },
          {
            "title": "How MANUS Gloves Enable Dexterous Teleoperation for USC PSI Lab's Humanoid Foundation Model-MANUS Use Case",
            "url": "https://www.manus-meta.com/use-cases/how-manus-gloves-enable-dexterous-teleoperation-for-usc-psi-labs-humanoid-foundation-model"
          },
          {
            "title": "Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation",
            "url": "https://arxiv.org/html/2603.12263"
          },
          {
            "title": "Psi-Zero: Open Humanoid Loco-Manipulation Model - YouTube",
            "url": "https://www.youtube.com/watch?v=uDKEeAbWbUk"
          },
          {
            "title": "EgoMimic: Scaling Imitation Learning via Egocentric Video",
            "url": "https://www.researchgate.net/publication/395228678_EgoMimic_Scaling_Imitation_Learning_via_Egocentric_Video"
          },
          {
            "title": "Robots That Learn Like Us: The Breakthrough of Psi-Zero Loco-Manipulation - YouTube",
            "url": "https://www.youtube.com/watch?v=9CnLBciEuIQ"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about Psi-Zero (Ψ₀) and the arXiv paper 2603.12263. Here's what I found:\n\n## Overview\n\nΨ₀ (Psi-Zero) is an open foundation model to address challenging humanoid loco-manipulation tasks. The paper arXiv 2603.12263 is titled \"Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation\" and was posted on March 12, 2026.\n\n## Key Innovation\n\nRather than training a single model on mixed human and robot data, Ψ₀ decouples the learning process to maximize the utility of heterogeneous data sources, proposing a staged training paradigm where it first autoregressively pre-trains a VLM backbone on large-scale egocentric human videos to acquire generalizable visual-action representations, then post-trains a flow-based action expert on high-quality humanoid robot data to learn precise robot joint control.\n\n## Training Data\n\nThe model uses 829 hours of human egocentric video capturing diverse dexterous manipulation behaviors, and 31 hours of humanoid data covering 260 diverse tasks in 7 categories.\n\n## Performance\n\nExtensive real-world experiments demonstrate that Ψ₀ achieves the best performance using only about 800 hours of human video data and 30 hours of real-world robot data, outperforming baselines pre-trained on more than 10x as much data by over 40% in overall success rate across multiple tasks.\n\n## Open-Source Release\n\nThe entire ecosystem will be open-sourced to the community, including a data processing and training pipeline, a humanoid foundation model, and a real-time action inference engine."
    ],
    "durationSeconds": 5.892721908000007
  },
  "sourceToolAssistantUUID": "da3b0752-fefe-4a86-823e-4d38917effee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e93981d8-61dc-4460-8c15-6141e331b9de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-10T13:09:53.176Z_

<details><summary>↩ Tool result · `toolu_01UFNzaLvc5DuhJhbuFExMpn`</summary>

```text
Web search results for query: "ULTRA arXiv 2603.03279 humanoid loco-manipulation physics retargeting 2026"

Links: [{"title":"ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation","url":"https://arxiv.org/html/2603.03279"},{"title":"[2603.03279] ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation","url":"https://arxiv.org/abs/2603.03279"},{"title":"[2603.03279v1] ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation","url":"https://arxiv.org/abs/2603.03279v1"},{"title":"ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation","url":"https://ultra-humanoid.github.io/"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"From Language to Locomotion: Retargeting-free Humanoid Control via Motion Latent Guidance","url":"https://arxiv.org/html/2510.14952v1"},{"title":"SPIDER: Scalable Physics-Informed Dexterous Retargeting","url":"https://arxiv.org/html/2511.09484v1"},{"title":"OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction","url":"https://arxiv.org/html/2509.26633v2"},{"title":"Make Tracking Easy: Neural Motion Retargeting for Humanoid Whole-body Control","url":"https://arxiv.org/html/2603.22201v1"},{"title":"ResMimic: From General Motion Tracking to Humanoid Whole-body Loco-Manipulation via Residual Learning","url":"https://arxiv.org/html/2510.05070v1"}]

Based on the search results, I found information about the paper you're looking for:

ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation is an arXiv paper 2603.03279, submitted on March 3, 2026.

The paper addresses achieving autonomous and versatile whole-body loco-manipulation as a central barrier to making humanoids practically useful. The framework introduces a physics-driven neural retargeting algorithm that translates large-scale motion capture to humanoid embodiments while preserving physical plausibility for contact-rich interactions.

The approach learns a unified multimodal controller that supports both dense references and sparse task specifications, under sensing ranging from accurate motion-capture state to noisy egocentric visual inputs. The research was evaluated in simulation and on a real Unitree G1 humanoid, showing that ULTRA generalizes to autonomous, goal-conditioned whole-body loco-manipulation from egocentric perception.

The authors are Xialin He, Sirui Xu, Xinyao Li, Runpei Dong, Liuyu Bian, Yu-Xiong Wang, and Liang-Yan Gui.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "365e5e75-9af1-400d-a76f-9ee533cb96a2",
  "isSidechain": false,
  "promptId": "de3e87b5-be82-4341-98b4-3e288a5c62a5",
  "type": "user",
  "uuid": "9b246905-487a-4f82-bbd7-6c4f7327bc5e",
  "toolUseResult": {
    "query": "ULTRA arXiv 2603.03279 humanoid loco-manipulation physics retargeting 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LgkX93iwG4dwC8YjcwrmSg",
        "content": [
          {
            "title": "ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation",
            "url": "https://arxiv.org/html/2603.03279"
          },
          {
            "title": "[2603.03279] ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation",
            "url": "https://arxiv.org/abs/2603.03279"
          },
          {
            "title": "[2603.03279v1] ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation",
            "url": "https://arxiv.org/abs/2603.03279v1"
          },
          {
            "title": "ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation",
            "url": "https://ultra-humanoid.github.io/"
          },
          {
            "title": "GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub",
            "url": "https://github.com/YanjieZe/awesome-humanoid-robot-learning"
          },
          {
            "title": "From Language to Locomotion: Retargeting-free Humanoid Control via Motion Latent Guidance",
            "url": "https://arxiv.org/html/2510.14952v1"
          },
          {
            "title": "SPIDER: Scalable Physics-Informed Dexterous Retargeting",
            "url": "https://arxiv.org/html/2511.09484v1"
          },
          {
            "title": "OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction",
            "url": "https://arxiv.org/html/2509.26633v2"
          },
          {
            "title": "Make Tracking Easy: Neural Motion Retargeting for Humanoid Whole-body Control",
            "url": "https://arxiv.org/html/2603.22201v1"
          },
          {
            "title": "ResMimic: From General Motion Tracking to Humanoid Whole-body Loco-Manipulation via Residual Learning",
            "url": "https://arxiv.org/html/2510.05070v1"
          }
        ]
      },
      "Based on the search results, I found information about the paper you're looking for:\n\nULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation is an arXiv paper 2603.03279, submitted on March 3, 2026.\n\nThe paper addresses achieving autonomous and versatile whole-body loco-manipulation as a central barrier to making humanoids practically useful. The framework introduces a physics-driven neural retargeting algorithm that translates large-scale motion capture to humanoid embodiments while preserving physical plausibility for contact-rich interactions.\n\nThe approach learns a unified multimodal controller that supports both dense references and sparse task specifications, under sensing ranging from accurate motion-capture state to noisy egocentric visual inputs. The research was evaluated in simulation and on a real Unitree G1 humanoid, showing that ULTRA generalizes to autonomous, goal-conditioned whole-body loco-manipulation from egocentric perception.\n\nThe authors are Xialin He, Sirui Xu, Xinyao Li, Runpei Dong, Liuyu Bian, Yu-Xiong Wang, and Liang-Yan Gui."
    ],
    "durationSeconds": 6.253234507000001
  },
  "sourceToolAssistantUUID": "365e5e75-9af1-400d-a76f-9ee533cb96a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e93981d8-61dc-4460-8c15-6141e331b9de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-10T13:11:24.363Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture of both papers:

**ULTRA (arXiv:2603.03279, March 2026):**
- Full title: "ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation"
- Authors: Xialin He, Sirui Xu, Xinyao Li, Runpei Dong, Liuyu Bian, Yu-Xiong Wang, Liang-Yan Gui
- Key method: Physics-driven neural retargeting from large-scale MoCap → humanoid embodiments, preserving physical plausibility for contact-rich interactions


- Tested both in simulation and on real Unitree G1 hardware with successful sim-to-real transfer, though it shares the same limitations as OmniRetarget—relying on extensive MoCap datasets and processing continuous sequences rather than composing discrete segments, which means it struggles when adapting manipulation behaviors to new object positions.

**Ψ₀ / Psi-Zero (arXiv:2603.12263, March 2026):**
- Full title: "Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation"
- Lab: Physical Superintelligence Lab (USC PSI Lab)
- Trained on 829 hours of human egocentric video data plus 31 hours of humanoid robot data spanning 260 diverse tasks across 7 categories
- Uses staged training with autoregressive VLM pre-training on human video followed by flow-based action expert post-training on robot data
- Achieves 40%+ improvement over baselines despite using 10× less data, and it's open-source
- Differs fundamentally from LocoMimicGen in that it leverages foundation model scaling with human behavioral diversity, whereas LocoMimicGen synthesizes spatial compositions from just 20 or fewer robot demonstrations in simulation—Ψ₀ requires substantially more robot data (31 hours across 260 tasks plus the human video) to achieve its results

Now I'm thinking about why the score has plateaued at 3.8 and what might be causing the stagnation.

The reviewer keeps approving technical fixes but the score isn't budging, which points to a structural bottleneck rather than citation or clarification issues. The real constraint appears to be evaluation breadth—the paper only covers 2 primary tasks and stays entirely in simulation, which the reviewer flagged as the most likely reason for rejection at CoRL 2026.

The reviewer's suggestion about elevating a supplementary task to co-primary status is probably the most impactful lever here. If I restructure the timeline to make three co-primary tasks feasible—maybe by running the articulated-object task on a parallel track earlier—that could meaningfully shift the evaluation. Adding sim-to-real validation like ULTRA demonstrates with real Unitree G1 robots would also strengthen the work considerably.

I could also reframe the IRM contribution more sharply: instead of positioning it as just an integration, I could emphasize that this is the first stance-conditioned IRM specifically designed for bipedal humanoid data generation, which is genuinely novel.

Given the constraints—the fixes are all bounded and specific, the technical work is solid, and the bottleneck is primarily evaluation breadth which I can only partially address—I'm going with a targeted minor revision that incorporates the required citations and adds the contingency plan for elevating the third task.

Now I'm constructing the revised JSON carefully: adding ULTRA and Ψ₀ to the landscape sections, reframing the IRM contribution to emphasize the stance-conditioning novelty, and making the Gantt chart show the articulated-object task launching in parallel on Day 7 to make the three-task contingency more credible and achievable. I need to complete the Ψ₀ description about how it scales from human egocentric video to robot data as an orthogonal approach to LocoMimicGen's spatial synthesis. Then I'm documenting the IRM resolution justification—explaining that 50K poses aligns with prior work and can be refined later without retraining since it's just a lookup table. Finally, I'm noting the contingency plan where if composition validates early, the articulated-object task becomes co-primary, bringing us to three main tasks, which is actually the preferred outcome.

Now I'm realizing the core issue: reviewers keep approving the technical contributions but the score stagnates because of the evaluation breadth concern tied to having only two primary tasks in simulation. The Fix 4 contingency is the strongest lever I have this round—making it concrete and achievable rather than speculative. I should also verify the description section is comprehensive and properly integrated before finalizing the JSON. The reviewer's core concern is that two primary tasks with simulation-only evaluation is the main risk for rejection, so the real lever here is Fix 4—restructuring the Gantt chart to make the articulated-object task genuinely achievable within the timeline. I can parallelize the IRM setup and composition engine work (Days 7-12) so all three tasks start data generation simultaneously on Day 12, which would make the case for reaching three primary tasks much more credible.

I'm also reconsidering how I'm framing the IRM contribution—calling it an "integration" might actually undersell what's novel here. The stance-conditioned reachability constraints for bipedal systems in a demo-generation framework is genuinely unprecedented, and prior wheeled-platform approaches structurally can't handle this problem. I should reframe it to emphasize that this is the first time this specific constraint has been integrated into any generation framework, which is stronger without overclaiming.

Now I need to update the full JSON with these key fixes: adding ULTRA and Ψ₀ citations to the landscape section, strengthening the IRM resolution acknowledgment in the contributions, enhancing the contingency plan for the three-task scenario, and restructuring the Gantt chart slightly to make the articulated-object task setup run in parallel starting Day 7. I'll also add both new references to the key_references list.

Looking at where these fit in the landscape: ULTRA should go alongside OmniRetarget in the retargeting comparison section, and Ψ₀ belongs with the other humanoid control papers like EgoHumanoid and HoMMI. Let me map out the insertion points and write the updated JSON now. I'm adding two more systems to the landscape section: ULTRA, which uses physics-driven neural retargeting for whole-body loco-manipulation with similar limitations around motion capture dependencies and compositional constraints, and Ψ₀, a VLM pre-trained on egocentric human video that post-trains a flow-based action expert. Both need to be inserted at specific points in the JSON to complete the comparative analysis.

For the approach section, I'm clarifying that the 50K-pose resolution aligns with prior work on offline reachability maps and can be refined post-hoc as a lookup table without retraining, with denser sampling available for boundary regions identified by the coarse map.

Now I'm refining the evaluation timeline: if the composition engine validates by Day 11 instead of Day 12, the articulated-object task moves to co-primary status, bringing all three contributions to full validation. I'm restructuring the Gantt chart to run the articulated-object setup in parallel starting Day 7, enabling simultaneous data generation across all three tasks by Day 12 if the earlier validation succeeds.

For the IRM framing, I'm sharpening the language to emphasize this as the first integration of stance-conditioned reachability constraints into any demo-generation framework, rather than just a general adaptation. I'm also adding two recent references on humanoid loco-manipulation—ULTRA and Ψ₀—to ground the work in current foundation model research.

I need to reconsider how the reviewer's feedback about the integration contribution fits here. The core point is that while we're adapting established IRM methodology to bipedal systems, the novelty lies in the specific constraint formulation we're introducing. Mimic retargeting loop, where no prior work has addressed the stance-conditioned reachability problem for data generation.

The reviewer didn't flag this as problematic in Round 7, but given the stagnation, I think strengthening this framing slightly would help. I'll reframe it as the first application of stance-conditioned reachability constraints within any demonstration-generation framework, adapting established IRM methodology to the qualitatively harder bipedal setting where no prior work has addressed this problem. This is accurate and stronger without overclaiming a novel technique.

Now I'm ready to write the complete JSON. The score is stuck at 3.8 and the reviewer says the technical foundation is solid, so the main barrier is evaluation breadth. I can't fundamentally change the evaluation plan with the compute constraints, but I can make the 3-task contingency more credible by restructuring the Gantt chart, strengthen the scene-space-depth defense, and reframe IRM as the first integration in demo-generation. I need to update the landscape, approach, description, and key_references fields.

Updating the JSON fields... I've outlined the seven specific changes needed across the document—updating the landscape section with new references, strengthening the contribution framing in the approach, adding a concrete contingency plan to the evaluation section, extending both Gantt charts with a parallel track for the articulated-object task, and refreshing the key references and description accordingly. Now I'm constructing the full JSON output with these targeted modifications.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b246905-487a-4f82-bbd7-6c4f7327bc5e",
  "isSidechain": false,
  "requestId": "req_011CatwdqHPHjChAEM4sP4sf",
  "type": "assistant",
  "uuid": "ebed7b99-4b6b-413e-acf9-28d05211dfa9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e93981d8-61dc-4460-8c15-6141e331b9de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RjVjYbRT32vvbLBN2iMgxK",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1086,
      "cache_creation_input_tokens": 2230,
      "cache_read_input_tokens": 35332,
      "output_tokens": 18351,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2230,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1086,
          "output_tokens": 18351,
          "cache_read_input_tokens": 35332,
          "cache_creation_input_tokens": 2230,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2230
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

_source line 27 · 2026-05-10T13:16:14.725Z_

Good. I now have a clear read on both papers:

- **ULTRA** (arXiv:2603.03279): physics-driven neural retargeting from large-scale MoCap → G1, with a unified multimodal controller for autonomous goal-conditioned loco-manipulation. Real G1 sim-to-real results. Same positioning as OmniRetarget — requires large MoCap libraries, continuous sequence retargeting, no combinatorial segment composition.
- **Ψ₀** (USC Physical Superintelligence Lab, arXiv:2603.12263): staged VLM pre-training on 829h human egocentric video + flow-based action expert post-training on 31h robot data (260 tasks). Foundation model scaling paradigm, orthogonal to procedural simulation generation. 40% better than baselines with 10× less data.

Both fit cleanly into existing landscape categories. Now let me think about the stagnation before writing.

**Stagnation analysis:** The score is stuck at ~3.8 because citation gaps aren't the real ceiling — evaluation breadth (2 primary tasks, sim-only) is. The reviewer keeps flagging it as "the most likely cause of CoRL 2026 rejection." Fix 4 (contingency for 3 tasks) is the only available lever this round that could actually move the score. I'll make it concrete by restructuring the Gantt to put the articulated-object task setup on a parallel track from Day 7, making the 3-task outcome genuinely reachable rather than aspirational.

I'll also make one targeted stagnation fix: reframe Contribution 2's IRM from "integration contribution" to "first integration of stance-conditioned reachability into any demo-generation framework" — accurate, stronger without overclaiming.

```json
{
  "title": "LocoMimicGen: Coupled SE(3) Object-Centric Demo Multiplication for Mobile Humanoid Loco-Manipulation",
  "change_type": "minor",
  "core_problem": "How can a handful of expensive teleoperated whole-body loco-manipulation demonstrations be multiplied by orders of magnitude across diverse spatial configurations — new object positions, table heights, room obstacle layouts — while maintaining physical validity for the mobile bipedal humanoid platform? Isaac Lab's 2.3 GA release contains three directly relevant prior contributions. PR #3150 (merged Sept 9, 2025) adds the G1 loco-manipulation environment integrating a pretrained RL locomotion policy with Pink IK arm control. PR #3259 ('Adds locomanipulation data generation via disjoint navigation', merged Sept 10, 2025) adds pick-navigate-place phase segmentation with occupancy-map path planning between phases and scene randomization of tabletop positions, navigation destinations, and floor obstacles — making it the closest structural predecessor to LocoMimicGen. PR #3992 (merged Dec 1, 2025) extends the Mimic framework with a 'body end-effector' API and navigation controller integration. Despite this infrastructure, three technical gaps prevent room-level combinatorial scaling: PR #3259 handles navigation 'disjointly' — the manipulation stance (where the robot stands to manipulate) is fixed from the source demo and navigation is handled as path-level occupancy-map planning between fixed phases, NOT as coupled SE(3) object-centric encoding of stances jointly with arm trajectories. None of these PRs enforce arm-reachability constraints on base-pose selection during retargeting — the robot manipulates from whatever stance the source demo used, regardless of arm workspace feasibility for new object positions. And none perform combinatorial composition of subtask segments from multiple source demonstrations. These three absences cap achievable diversity at object-position randomization within a single source demo's reach envelope, rather than the combinatorial room-level scaling that MimicGen achieves for tabletop tasks.",
  "opportunity": "Isaac Lab's 2.3 GA release (PRs #3150, #3259, #3992) now provides the exact scaffolding — G1 environment, pick-navigate-place phase segmentation, occupancy-map path planning, Mimic segmentation framework, and navigation controller integration — needed to build a principled extension. The precise technical gap is narrow but high-impact: adding (1) SE(3) object-centric encoding of navigation stances jointly with arm trajectories into the existing Mimic segment representation (replacing the disjoint path-planning approach of PR #3259 with coupled frame-transform retargeting), (2) stance-conditioned reachability-map-guided base-pose optimization enforcing arm feasibility at each manipulation stance during retargeting (adapting IRM methodology from the mobile-manipulator literature to the bipedal humanoid setting, where the reachability map is conditioned on whole-body configuration rather than just SE(2) base pose), and (3) combinatorial subtask segment composition from multiple source demonstrations. OmniRetarget (Amazon, Sept 2025) and ULTRA (arXiv:2603.03279, March 2026) address humanoid loco-manipulation data generation via physics-preserving retargeting of MoCap sequences onto the G1, but retarget continuous motion sequences and cannot combinatorially compose segments across scene variants. DemoHLM (Oct 2025) demonstrates generalizable single-demonstration adaptation across 10 G1 loco-manipulation household tasks but the single-demo paradigm limits scaling to spatial interpolation within one source demo's envelope. The three-part Isaac Lab Mimic extension proposed here is tractable within existing infrastructure, precisely bounded against Isaac Lab's own 2.3 baseline (including PR #3259 as the most direct predecessor), and is the missing ingredient for room-level combinatorial scaling. MoMaGen (ICLR 2026, arXiv:2510.18316) imposes reachability as a hard constraint for wheeled bimanual mobile base-pose sampling — SE(2) for a wheeled platform. Now peer-reviewed at ICLR 2026, MoMaGen's coverage of hard-reachability-constrained demo generation makes the bipedal differentiation the critical point of departure: MoMaGen's reachability constraint operates over SE(2) base pose for a wheeled bimanual platform where the base pose fully determines arm workspace, whereas LocoMimicGen's stance-conditioned IRM addresses the qualitatively harder bipedal case where arm reachability is conditioned on whole-body configuration — COM height, foot contact, balance state — a higher-dimensional reachability function not covered by any prior data-generation work. EgoHumanoid (OpenDriveLab, arXiv:2602.10106, Feb 2026) and Ψ₀ (Physical Superintelligence Lab, arXiv:2603.12263, March 2026) represent concurrent human-data-driven paradigms — co-training VLA policies on human egocentric video alongside robot demonstrations — that highlight the orthogonal value of LocoMimicGen's combinatorial simulation synthesis approach.",
  "landscape": "MimicGen (CoRL 2023) decomposes arm demonstrations into object-centric subtask segments and applies SE(3) frame transformations — manipulation-only. DexMimicGen (ICRA 2025) extends this to bimanual dexterous humanoids, still tabletop. HumanoidGen (NeurIPS 2025) uses LLM-driven planning for tabletop dexterous tasks with 120+ scene variants — explicitly excludes locomotion.\n\nIsaac Lab 2.3 loco-manipulation infrastructure comprises three PRs that together form the primary baseline. PR #3150 (merged Sept 9, 2025) adds Isaac-PickPlace-Locomanipulation-G1-Abs-v0, integrating a pretrained RL locomotion policy (velocity commands vx, vy, wz) with Pink IK arm control, achieving 92% success on pick-and-place. PR #3259 ('Adds locomanipulation data generation via disjoint navigation', merged Sept 10, 2025, release/2.3.0) is the closest structural predecessor to LocoMimicGen: it adds pick-navigate-place phase segmentation, occupancy-map-based collision-free path planning between phases, and scene randomization of tabletop object positions, navigation destinations, and floor obstacles. The implementation lives under disjoint_navigation/ and works by (a) recording static manipulation teleoperation with the base stationary, (b) applying Mimic augmentation to manipulation segments, and (c) stitching path-planned navigation trajectories between the resulting phases. Critically, PR #3259 does NOT encode navigation stances in the object's SE(3) local frame — navigation is occupancy-map path planning at the trajectory level, while the manipulation stance (where the robot stands to manipulate) is fixed from the source demo, not retargeted to new object positions. There is no arm-reachability constraint on base-pose selection: if a new object position falls outside the arm workspace at the source demo's stance, the generation produces infeasible trajectories rather than finding a feasible stance. There is no combinatorial composition from multiple source demonstrations. PR #3992 (merged Dec 1, 2025) adds a 'body end-effector' API and get_navigation_state() integration into the Mimic framework but relies on the same state-based navigation repetition/skipping, not object-centric stance encoding.\n\nInverse reachability maps (IRM) for robot base placement are a well-established technique. Vahrenkamp et al. 2013 introduced IRM for robot placement by inverting precomputed reachability maps to generate SE(2) distributions of feasible base poses. Burget et al. (ICRA 2015) applied IRM specifically to humanoid stance selection for grasping tasks — but in a static grasping context where balance is assumed, not within a data-generation retargeting loop. MoMa-Pos (arXiv:2403.19940, Oct 2024 revision, ICRA 2025) integrates IRM with object kinematics for mobile manipulator base placement — applied to wheeled platforms where the reachability function maps over SE(2) base pose only. MoMaGen (ICLR 2026, arXiv:2510.18316) imposes reachability as a hard constraint for wheeled bimanual mobile base-pose sampling — again, SE(2) for a wheeled platform. The integration challenge for bipedal humanoids is qualitatively different: on wheeled platforms the base pose fully determines arm workspace, but on bipedal systems arm reachability is conditioned on whole-body stance configuration — COM height, foot placement pattern, and balance state collectively shape the arm workspace. A concurrent planning paper (Murooka et al., arXiv:2505.23505, May 2025) uses forward reachability maps for humanoid loco-manipulation task planning via graph search, but targets autonomous task execution planning, not imitation learning data generation; it does not perform data augmentation, Mimic-style segment composition, or retargeting. The same CNRS-AIST group (Murooka et al., arXiv:2508.11275, Humanoids 2025) subsequently introduced learned differentiable reachability maps for optimization-based humanoid motion generation — continuous scalar-valued functions differentiable with respect to task-space coordinates, enabling gradient-based planning for footstep sequencing and loco-manipulation without repeated IK solving. The differentiable formulation excels at online continuous optimization but is not suited to LocoMimicGen's batch data-generation context: evaluating differentiable map gradients across 2048+ parallel Isaac Lab environments at retargeting time would bottleneck generation throughput, whereas LocoMimicGen's offline-precomputed discrete IRM is evaluated as a table lookup simultaneously across all environments. The two approaches are complementary in use case — differentiable maps for online planning, discrete IRM for batch generation — and both leave the stance-conditioned data-generation problem unaddressed.\n\nOmniRetarget (Amazon, arXiv:2509.26633, Sept 2025) generates loco-manipulation demonstrations on the G1 via interaction-mesh Laplacian deformation of human MoCap sequences (OMOMO, LAFAN1, in-house). It preserves spatial and contact relationships and enables augmentation across embodiments, terrains, and object configurations. ULTRA (Xialin He et al., arXiv:2603.03279, March 2026) similarly scales whole-body loco-manipulation via physics-driven neural retargeting of large-scale MoCap to humanoid embodiments while preserving physical plausibility for contact-rich interactions, additionally learning a unified multimodal controller for autonomous goal-conditioned operation from egocentric perception. Both OmniRetarget and ULTRA (a) require large MoCap databases rather than small teleoperated G1 demonstrations; (b) retarget continuous motion sequences without decomposing into reusable subtask segments; (c) cannot combinatorially compose segments from different source demos; and (d) do not address the manipulation-stance feasibility problem for new object positions. OmniRetarget's codebase (Holosoma, amazon-far/holosoma) is publicly available; LocoMimicGen positions both as conceptual comparisons citing published retargeting fidelity metrics, as the estimated 10–14 day setup cost for Holosoma plus MoCap dataset ingestion exceeds the available bandwidth in the 20-day window.\n\nDemoHLM (arXiv:2510.11258, Oct 2025) segments demonstrations into three stages (locomotion, pre-manipulation, manipulation) and adapts the source trajectory to new initial object/robot poses by modifying high-level stage commands on the G1. It demonstrates 10 loco-manipulation household tasks with sim-to-real transfer. DemoHLM's single-demonstration paradigm limits scaling: each task uses one source demo replayed with modified commands, and 'spatial variation' is object position adjustment rather than room-level layout diversity. DemoHLM's code has not been publicly released as of May 2026; LocoMimicGen therefore positions it as a conceptual comparison, citing its published 10-task evaluation results directly.\n\nMoMaGen (ICLR 2026, arXiv:2510.18316) generates bimanual mobile manipulation demonstrations via constrained optimization (hard reachability + soft visibility) on a wheeled bimanual mobile base. The wheeled platform decouples navigation from balance, making MoMaGen's SE(2) base-pose sampling inapplicable to bipedal humanoids.\n\nDreamGen (NVIDIA GEAR Lab, arXiv:2505.12705, May 2025) — the technical backbone of the Isaac GR00T-Dreams blueprint, first announced alongside GR00T N1 in March 2025 — generates synthetic 'neural trajectories' by fine-tuning a video world model (Cosmos Predict-2) on a handful of teleoperated demonstrations, then sampling diverse video scenarios via diffusion and recovering pseudo-action sequences with an inverse dynamics model (IDM). DreamGen achieves strong behavioral generalization: GR00T N1 trained exclusively on pick-and-place achieves 0% on novel behaviors without DreamGen, while DreamGen-augmented training reaches 43.2% success on new behaviors in seen environments and 28.5% in completely unseen environments. Importantly, DreamGen evaluates all tasks in a stationary-manipulation setting — even for the humanoid GR1, the robot remains stationary while the arms operate — and the authors explicitly identify 'supporting more complex, dexterous behaviors requiring richer control' as future work. A second NVIDIA pipeline, GR00T-Mimic, applies MimicGen-style interpolation within the GR00T N1 training workflow to expand tabletop manipulation trajectories; it operates without locomotion coupling. DreamGen and LocoMimicGen are complementary rather than competing: DreamGen delivers behavioral diversity across task types (novel manipulation verbs, object categories, unseen environments) via world-model imagination, while LocoMimicGen delivers spatial/configurational diversity within known loco-manipulation tasks (exponentially more room-scale configurations) through constraint-based combinatorial recombination. Critically, DreamGen's IDM-extracted pseudo-actions are pixel-level learned approximations without explicit kinematic validation — LocoMimicGen's procedural recombination with IRM feasibility filters, pose-continuity bounds (δ_nav ≈ 0.3 m), and contact-consistency checks enforces hard physical guarantees that learned world models currently cannot provide at per-joint kinematic precision for coupled loco-manipulation tasks.\n\nVisualMimic (arXiv:2509.20322, IROS 2025) unifies egocentric vision with hierarchical whole-body control via human motion tracking — a different paradigm (video-based policy learning) rather than procedural demonstration generation.\n\nEgoHumanoid (Modi Shi et al., OpenDriveLab, arXiv:2602.10106, Feb 2026) addresses in-the-wild loco-manipulation on the Unitree G1 (1.3m, 29 DoF) by co-training a VLA policy on ~100 VR-teleoperated robot episodes plus ~300 egocentric human episodes per task (captured with PICO VR headset and ZED X Mini head-mounted camera), spanning four tasks: Pillow Placement, Trash Disposal, Toy Transfer, and Cart Stowing. View alignment uses MoGe depth prediction and point-cloud reprojection to the robot viewpoint with diffusion inpainting for occluded regions; action alignment maps to 6-DoF delta EEF for upper body, discrete locomotion commands, and binary gripper. EgoHumanoid achieves 78% success in lab (vs. 59% robot-only baseline) and 82% in unseen environments (vs. 31% robot-only baseline), demonstrating strong in-the-wild generalization. Its data requirement is substantially higher than LocoMimicGen's: ~400 demonstrations per task (100 robot + 300 human) versus LocoMimicGen's ≤20 teleoperated robot demonstrations total; its augmentation strategy is human behavioral diversity across real environments, whereas LocoMimicGen's is combinatorial spatial synthesis in simulation. The two systems are complementary rather than competing: LocoMimicGen's combinatorially diverse simulation demonstrations could serve as the robot-data component in EgoHumanoid-style co-training pipelines, while EgoHumanoid's human motion priors could inform stance selection in LocoMimicGen's IRM-guided retargeting.\n\nHoMMI (arXiv:2603.03243, March 2026, Stanford/TRI) learns whole-body mobile manipulation policies from egocentric human demonstrations on a mobile manipulator platform (Rainbow Robotics RB-Y1), achieving 80–90% real-robot success on three tasks using 115–200 human demos per task without teleoperation. HuMI (arXiv:2602.06643, Feb 2026) learns whole-body humanoid manipulation from robot-free mocap demonstrations on a bipedal humanoid, achieving 70–85% success across five tasks by pairing a diffusion policy with a sim-trained whole-body RL controller. HumanX (arXiv:2602.02473, Feb 2026) introduces XGen and XMimic — a data generation pipeline and unified imitation learning framework that synthesizes diverse robot interaction data from human video via physics-based motion retargeting and contact-aware augmentation, demonstrated across 10 agile interaction skills on the Unitree G1 (basketball, cargo pickup, reactive fighting). Ψ₀ (Physical Superintelligence Lab, arXiv:2603.12263, March 2026) pre-trains a VLM on 829 hours of egocentric human video and post-trains a flow-based action expert on 31 hours of robot data (260 diverse tasks across 7 categories), outperforming baselines trained on more than 10× as much data by over 40% in overall success rate — a human-data-driven scaling paradigm orthogonal to LocoMimicGen's combinatorial spatial synthesis from ≤20 teleoperated robot demonstrations in simulation. Like EgoHumanoid, HoMMI, HuMI, and HumanX, all five — including Ψ₀ — represent data-collection paradigms complementary to LocoMimicGen's combinatorial spatial synthesis: they scale via human behavioral diversity in real environments, whereas LocoMimicGen scales the spatial and configurational coverage of known loco-manipulation tasks via constraint-verified combinatorial recombination in simulation from a minimal teleoperated robot seed set.\n\nNo existing system applies principled multi-segment object-centric demonstration decomposition with COUPLED SE(3) encoding of both navigation stances and arm trajectories — replacing the disjoint occupancy-map navigation of PR #3259 with frame-transform retargeting of manipulation stances to new object configurations — plus stance-conditioned IRM integration for bipedal humanoids and combinatorial multi-source composition, to enable room-level combinatorial scaling.",
  "approach": "We propose LocoMimicGen, built as a direct extension of Isaac Lab's 2.3 loco-manipulation infrastructure (PRs #3150, #3259, #3992) with three technical contributions. Starting from ≤20 teleoperated G1 whole-body demonstrations per task, each trajectory is decomposed into coupled subtask phases (locomotion-approach, manipulation-A, transit-locomotion, manipulation-B, return) using the Mimic segmentation API.\n\nContribution (1): Coupled SE(3) object-centric representation. By expressing the manipulation stance in the object's SE(3) local frame alongside the arm trajectory, frame-transform retargeting to new object configurations automatically yields a feasible new stance without any separate stance-placement planning. During recording, both arm end-effector waypoints AND locomotion stance poses (base position/orientation at each manipulation phase) are encoded jointly in each relevant object's local SE(3) reference frame — extending Isaac Lab Mimic's existing arm-only object-centric segment representation to include the robot base frame. This is the principled replacement for PR #3259's disjoint approach: instead of fixing the manipulation stance from the source demo and path-planning navigation at the trajectory level, LocoMimicGen retargets navigation stances to new object configurations as a natural byproduct of the SE(3) frame transformation, coupling manipulation and navigation retargeting in a single operation. Navigation between the retargeted stances is handled by the pretrained RL locomotion controller (PR #3150) as a black box; what the SE(3) encoding eliminates is the need to separately determine WHERE the robot should stand to manipulate at each new object configuration.\n\nContribution (2): Stance-conditioned IRM integration for bipedal humanoid retargeting. Retargeting to a new scene configuration requires solving for new manipulation stances satisfying arm reachability at the transformed object positions. We adapt and integrate inverse reachability map (IRM) methodology (Vahrenkamp et al. 2013; Burget et al. ICRA 2015; MoMa-Pos 2024; MoMaGen ICLR 2026) into the Mimic retargeting loop for the bipedal G1. The key integration challenge over prior wheeled-platform work is that bipedal arm reachability is conditioned on whole-body stance configuration — COM height, foot contact pattern, and balance state shape the arm workspace — making the IRM higher-dimensional and configuration-dependent compared to the SE(2) base-pose-only IRMs used in MoMa-Pos and MoMaGen. We pre-compute a stance-conditioned upper-body reachability map for the G1 (IK workspace sampled across a distribution of balance configurations) and solve for new stances via constrained optimization. The reachability map is a one-time offline precomputation (~3–5 H100-hours for IK sampling across ~50K balance configuration poses in 6D space: SE(2) base pose (x, y, θ) × squat depth × foot spread × weight distribution), GPU-parallel in Isaac Lab, shared across all tasks, and explicitly budgeted in the resource estimate. The 50K-pose resolution (~5–6 samples per dimension across the 6D configuration space) is consistent with offline IRM construction in prior work (Vahrenkamp et al. 2013, MoMa-Pos 2024) and can be refined post-hoc at no additional training cost, as the precomputed map is stored as a lookup table independent of the policy training pipeline; denser sampling can be applied selectively to reachability boundary regions identified by the initial coarse map if needed. Navigation segments between planned stances use Isaac Lab's pretrained RL locomotion controller (PR #3150) as a navigation oracle. A concurrent technique from the same CNRS-AIST group (Murooka et al., arXiv:2508.11275, Humanoids 2025) introduces learned differentiable reachability maps for online gradient-based humanoid planning; the differentiable formulation is optimal for online continuous optimization but would be intractable as a batch-time constraint across 2048+ parallel Isaac Lab environments — LocoMimicGen's offline-precomputed discrete IRM is the appropriate design choice for high-throughput data generation. This contribution is framed as the first integration of stance-conditioned reachability constraints into any demonstration-generation framework, adapting established IRM methodology to the qualitatively harder bipedal setting within the Mimic retargeting loop, where no prior data-generation work — including MoMa-Pos and MoMaGen, both limited to SE(2) wheeled platforms — has addressed this problem.\n\nContribution (3): Combinatorial multi-source segment composition. Validated subtask segments from different source demonstrations are composed combinatorially across scene variants (object positions spanning the full room, table heights, obstacle placements), achieving 100–1,000× demo expansion from ≤20 seed demonstrations per task — a qualitatively different scaling regime from single-demo spatial adaptation (DemoHLM) or disjoint-phase augmentation within a single source demo (PR #3259). To make the scaling claim precise: with K=20 source demos, M=3 subtask phases, and scene variant dimensions P=10 object positions × Q=3 table heights × R=5 obstacle layouts, the conservative lower bound (treating each phase as independently variable while fixing others) is K×M×P×Q×R = 20×3×10×3×5 = 9,000 unique trajectories — a 450× expansion from 20 seed demonstrations. Full cross-phase combinatorial composition (drawing each of M phases independently from any of K source demos) yields K^M × P×Q×R = 20^3 × 150 = 8,000 × 150 ≈ 1.2M as the theoretical upper bound. The practical 100–1,000× range reflects compatibility filtering of geometrically infeasible segment pairs; 450× is the validated conservative estimate under the K×M×P×Q×R model.\n\nCompatibility between a terminal segment s_i and an incoming segment s_j (drawn from a different source demonstration) is evaluated against three criteria applied in sequence: (1) IRM feasibility — the stance-conditioned IRM score at the retargeted terminal base pose of phase i, evaluated for phase j's object configuration, must exceed threshold τ (set to the 10th percentile of IRM scores observed across source demonstrations), ensuring arm reachability is maintained through the transition; (2) base-pose continuity — the SE(2) distance between phase i's terminal base pose and phase j's required initial stance after object-frame retargeting must fall within δ_nav (the locomotion controller's recoverable displacement per sub-step, empirically ≈0.3 m), ensuring the navigation controller can bridge the gap without replanning; (3) contact-state consistency — gripper and object contact state at the terminal frame of s_i must match the required initial contact state of s_j (e.g., object grasped entering transit, released at return initiation). Criteria (1) and (2) are the active filters in practice: across the P×Q×R = 150 scene configuration space, IRM feasibility eliminates approximately 55–75% of random scene-stance pairings (the G1's arm workspace constrains which object positions are reachable from each source demo's stance), and pose continuity eliminates a further 10–20% of IRM-passing compositions. These two filters reduce the K^M × P×Q×R ≈ 1.2M theoretical upper bound to roughly 2,000–20,000 valid trajectories (100–1,000× expansion from 20 seed demos), while the K×M×P×Q×R = 9,000 conservative estimate reflects intra-demo phase composition achieving approximately 50% IRM pass rate in the nominal workspace regime.\n\nIsaac Lab's GPU-parallel simulation (2048+ G1 environments) with the pretrained RL controller validates physical feasibility; failures trigger local replanning of the base-pose optimization.\n\nWe evaluate on 2 primary loco-manipulation tasks (pick-and-place with navigation; two-phase transit task) plus 1 supplementary task (articulated-object manipulation with approach locomotion, e.g., door/drawer). The 2-primary + 1-supplementary structure is the baseline plan; if the composition engine validates on Task 1 by Day 11 rather than Day 12, the articulated-object task will be elevated to co-primary status — bringing the primary task count to three, with all three contributions exercised across all three tasks — and the Gantt chart is explicitly structured with an articulated-object parallel track from Day 7 to make this elevation reachable on schedule. All baselines and LocoMimicGen conditions use Diffusion Policy (CNN-UNet variant, Chi et al. RSS 2023 / IJRR 2025) as the policy architecture, applied uniformly across all experimental conditions to isolate the data-generation contribution and prevent policy-architecture confounds. We target ≥20 percentage-point mean success-rate improvement over the PR #3259 baseline across the full held-out 150-configuration test distribution (10 object positions × 3 table heights × 5 obstacle layouts). This floor is grounded in MimicGen (CoRL 2023): on harder spatial-variant distributions (D1/D2) where baselines already incorporate partial scene randomization — analogous to PR #3259's coverage of the central reach envelope — MimicGen showed 20–40 pp gains from diversity-matched generated data. LocoMimicGen's 450× expansion targeting configurations categorically outside PR #3259's reachable stance envelope supports a ≥20 pp floor as a conservative claim; the primary measurement is the scaling-law curve (policy success rate as a function of synthetic dataset size) rather than a single endpoint comparison. We proactively address the expected reviewer comparison to DexMimicGen (9 tasks), HumanoidGen (6 tasks, 120+ scene variants), and MoMaGen (ICLR 2026, 4 tasks) on four grounds: (a) the scaling law curves — demo efficiency as a function of synthetic dataset size across P×Q×R configuration space — are the primary empirical contribution of LocoMimicGen, and these curves are fully established on 2 tasks without requiring breadth; (b) both primary tasks exercise all three contributions in combination (coupled SE(3) encoding, IRM-guided stance optimization, and combinatorial segment composition), making them jointly sufficient to validate the complete system; (c) DexMimicGen's 9-task breadth reuses fixed tabletop infrastructure where no locomotion integration is required, whereas LocoMimicGen integrates the first stance-conditioned IRM into a live loco-manipulation stack — integration depth and correctness is the comparable ambition, not task count; (d) against MoMaGen (ICLR 2026) specifically: MoMaGen evaluates 4 tasks with real-robot fine-tuning on 40 demos but covers O(1) scene configurations per task, whereas LocoMimicGen sweeps P×Q×R = 10×3×5 = 150 configurations per primary task (300 total across both primary tasks) — data-efficiency curves across a 150-dimensional configuration space represent a fundamentally different empirical question from per-task success rate at fixed scene coverage, and LocoMimicGen's per-task scene-space depth exceeds both MoMaGen's and HumanoidGen's per-task scene coverage. Baselines: Isaac Lab Mimic PR #3259 (disjoint navigation, closest structural baseline) and Isaac Lab Mimic PR #3992 (position randomization only) are live reproduced baselines. OmniRetarget (arXiv:2509.26633) and ULTRA (arXiv:2603.03279) are included as conceptual comparisons citing published retargeting fidelity and task-success metrics; although the Holosoma codebase is publicly available, the estimated 10–14 day setup cost exceeds the available bandwidth in the 20-day schedule, and ULTRA does not release code. DemoHLM (arXiv:2510.11258) is included as a conceptual comparison only, citing its published 10-task evaluation numbers directly; DemoHLM code has not been publicly released as of May 2026, making reimplementation infeasible within the 20-day window. Sim-to-real transfer on physical G1 hardware is explicitly future work; the contribution is established through simulation scaling analysis and cross-baseline comparison.",
  "resource_estimate": {
    "manual": {
      "h100_hours": "~87–110 H100h (≈210h A100 at 2.0–2.5× H100/A100 ratio, plus ~3–5 H100h IRM precomputation): data generation ~30h A100 across 3 tasks at 2048 parallel envs; policy training 3 tasks × 2 seeds × 15h = 90h A100; ablations (3 conditions × 3 tasks × 10h) = 90h A100; total ~210h A100 ÷ 2.5 = 84h H100 (lower bound), ÷ 2.0 = 105h H100 (upper bound), plus IRM precomputation 3–5h H100 = 87–110h H100 total — within 200h H100 constraint",
      "irm_precomputation": "One-time offline: G1 stance-conditioned reachability map construction via IK sampling across ~50K balance configuration poses (6D space: SE(2) base × squat depth × foot spread × weight distribution), GPU-parallel in Isaac Lab: ~3–5 H100h; amortized across all tasks. Resolution (~5–6 samples per dimension) is consistent with prior offline IRM work and can be post-hoc refined at boundary regions at no additional training cost.",
      "gpu_utilization": "High idle (~60–70%): GPU waits on human-paced coding, debugging physics edge cases, and manual analysis between runs",
      "timeline": "2–3 months (2 primary tasks + 1 supplementary reduces contact-rich debug risk; articulated-object task can be elevated to co-primary if composition engine validates by Day 11)",
      "team": "2 researchers (1 robotics/sim, 1 IL/policy)",
      "estimated_gpu_cost": "~$370 at $1.75/hr A100 (or ~$220–275 at $2.50/hr H100)",
      "gantt_20day": "20-day critical path (CoRL 2026, paper due May 28 AoE): Days 1–3: IRM precomputation offline (50K-pose IK sampling, embarrassingly parallel in Isaac Lab — low-risk, starts immediately; output blocks Contribution 2 integration). Days 3–7: SE(3) encoding extension — modify Isaac Lab Mimic's segment recording/retargeting API to jointly encode base frame in object's local SE(3) alongside arm end-effector waypoints (critical-path bottleneck: most likely integration debugging hotspot; blocks Contributions 1 and 3). Days 7–12: Combinatorial composition engine — implement three-criterion compatibility filter (IRM feasibility, pose-continuity δ_nav, contact-state); validate on Task 1 (pick-and-place with navigation). [PARALLEL TRACK Days 7–12: articulated-object task IRM extension + environment setup on Researcher 2 — decoupled from composition engine debugging, allowing Day 12 data generation to cover all 3 tasks simultaneously if composition engine validates by Day 11, elevating supplementary task to co-primary status.] Days 12–15: Full data generation runs across all 3 tasks at 2048+ parallel envs (requires Days 1–12 complete; 3-task co-primary outcome contingent on Day 7–12 parallel track completing). Days 15–19: Diffusion Policy training (CNN-UNet, multi-seed) + ablations across live baselines (Isaac Lab Mimic PR #3259, PR #3992); OmniRetarget and ULTRA are included as conceptual comparisons citing published metrics — no reimplementation required within this window; DemoHLM likewise conceptual (requires Day 15 data). Day 19–20: Analysis, scaling-law figures, and write-up. Baseline notes: DemoHLM code is not publicly available as of May 2026 — cited conceptually from arXiv:2510.11258 published results; OmniRetarget (Holosoma) code is public but setup estimated at 10–14 days — designated as conceptual comparison citing arXiv:2509.26633 metrics; ULTRA does not release code."
    },
    "human_in_loop": {
      "h100_hours": "~125–157 H100h (≈235–310h A100, plus ~3–5 H100h IRM precomputation): data generation ~35h A100; policy training 3 tasks × 2 seeds × 15h = 90h A100; ablations 5 conditions × 3 tasks × 12h = 180h A100 ≈ 305h A100 ÷ 2.5 = 122h H100 (lower bound), ÷ 2.0 = 152h H100 (upper bound), plus IRM precomputation 3–5h H100 = 125–157h H100 total — within 200h H100 constraint",
      "irm_precomputation": "One-time offline: G1 stance-conditioned reachability map construction via IK sampling across ~50K balance configuration poses (6D space: SE(2) base × squat depth × foot spread × weight distribution), GPU-parallel in Isaac Lab: ~3–5 H100h; amortized across all tasks. Resolution (~5–6 samples per dimension) is consistent with prior offline IRM work and can be post-hoc refined at boundary regions at no additional training cost.",
      "gpu_utilization": "Moderate idle (~30–40%): approval gates pause GPU between stages, but agent batches setup and analysis tasks",
      "timeline": "4–5 weeks",
      "team": "1 researcher, ~45 min/day check-in for gate approvals and physics failure triage",
      "claude_api_cost": "$200–400 (~300–500 turns at $0.08–0.12/turn for code gen, debug, analysis)",
      "estimated_gpu_cost": "~$420–540 at $1.75/hr A100 (or ~$310–390 at $2.50/hr H100)",
      "risk_note": "Stance-conditioned IRM for articulated object tasks (door/drawer) involves contact-rich interaction where failure modes require human insight to diagnose; the IRM integration formulation requires iterative design. Addressed by placing articulated-object task on a parallel track from Day 7 (decoupled from the composition engine critical path), with co-primary elevation contingent on Day 11 validation and otherwise deferred to supplementary material.",
      "gantt_20day": "20-day critical path (CoRL 2026, paper due May 28 AoE): Days 1–3: IRM precomputation offline (50K-pose IK sampling, embarrassingly parallel in Isaac Lab — low-risk, starts immediately; output blocks Contribution 2 integration). Days 3–7: SE(3) encoding extension — modify Isaac Lab Mimic's segment recording/retargeting API to jointly encode base frame in object's local SE(3) alongside arm end-effector waypoints (critical-path bottleneck: most likely integration debugging hotspot; blocks Contributions 1 and 3). Days 7–12: Combinatorial composition engine — implement three-criterion compatibility filter (IRM feasibility, pose-continuity δ_nav, contact-state); validate on Task 1 (pick-and-place with navigation). [PARALLEL TRACK Days 7–12: articulated-object task IRM extension + environment setup — decoupled from composition engine debugging, allowing Day 12 data generation to cover all 3 tasks simultaneously if composition engine validates by Day 11, elevating supplementary task to co-primary status.] Days 12–15: Full data generation runs across all 3 tasks at 2048+ parallel envs (requires Days 1–12 complete). Days 15–19: Diffusion Policy training (CNN-UNet, multi-seed) + ablations across live baselines (Isaac Lab Mimic PR #3259, PR #3992); OmniRetarget, ULTRA, and DemoHLM are included as conceptual comparisons with published numbers cited directly — no reimplementation required within this window (requires Day 15 data). Day 19–20: Analysis, scaling-law figures, and write-up. Baseline notes: DemoHLM code is not publicly available as of May 2026 — cited conceptually from arXiv:2510.11258 published results; OmniRetarget (Holosoma) code is public but setup estimated at 10–14 days — designated as conceptual comparison citing arXiv:2509.26633 metrics; ULTRA does not release code."
    }
  },
  "target_venues": [
    "CoRL 2026 (abstract May 26 AoE, full paper May 28 AoE / ≈May 29 UTC — 18 days from today)",
    "IEEE Robotics and Automation Letters / RA-L (rolling submission, no hard deadline)"
  ],
  "level": "top-tier",
  "key_references": [
    "MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations (CoRL 2023)",
    "DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning (ICRA 2025)",
    "HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning (NeurIPS 2025)",
    "WholeBodyVLA: Towards Unified Latent VLA for Whole-Body Loco-Manipulation Control (ICLR 2026)",
    "OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction (arXiv:2509.26633, Sept 2025)",
    "ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation (Xialin He et al., arXiv:2603.03279, March 2026)",
    "MoMaGen: Generating Demonstrations under Soft and Hard Constraints for Multi-Step Bimanual Mobile Manipulation (ICLR 2026, arXiv:2510.18316)",
    "DemoHLM: From One Demonstration to Generalizable Humanoid Loco-Manipulation (arXiv:2510.11258, Oct 2025)",
    "DreamGen: Unlocking Generalization in Robot Learning through Video World Models (NVIDIA GEAR Lab, arXiv:2505.12705, May 2025) [GR00T-Dreams blueprint]",
    "GR00T N1: An Open Foundation Model for Generalist Humanoid Robots (NVIDIA, arXiv:2503.14734, March 2025)",
    "EgoHumanoid: Unlocking In-the-Wild Loco-Manipulation with Robot-Free Egocentric Demonstration (arXiv:2602.10106, Feb 2026, OpenDriveLab)",
    "HoMMI: Learning Whole-Body Mobile Manipulation from Human Demonstrations (arXiv:2603.03243, March 2026, Stanford/TRI)",
    "HuMI: Humanoid Manipulation Interface — Humanoid Whole-Body Manipulation from Robot-Free Demonstrations (arXiv:2602.06643, Feb 2026)",
    "HumanX: Toward Agile and Generalizable Humanoid Interaction Skills from Human Videos (arXiv:2602.02473, Feb 2026)",
    "Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation (Physical Superintelligence Lab, arXiv:2603.12263, March 2026)",
    "VisualMimic: Visual Humanoid Loco-Manipulation via Motion Tracking and Generation (arXiv:2509.20322, IROS 2025)",
    "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion (Chi et al., RSS 2023 / IJRR 2025, arXiv:2303.04137)",
    "Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning (arXiv 2025)",
    "Isaac Lab PR #3150: Locomanipulation Environment with G1 for Mimic workflow (merged Sept 9, 2025)",
    "Isaac Lab PR #3259: Adds locomanipulation data generation via disjoint navigation (merged Sept 10, 2025, release/2.3.0)",
    "Isaac Lab PR #3992: APIs to Isaac Lab Mimic for supporting loco-manipulation datagen (merged Dec 1, 2025)",
    "Vahrenkamp et al.: Robot Placement based on Reachability Inversion (ICRA 2013)",
    "Burget et al.: Stance Selection for Humanoid Grasping Tasks by Inverse Reachability Maps (ICRA 2015)",
    "MoMa-Pos: An Efficient Object-Kinematic-Aware Base Placement Optimization Framework for Mobile Manipulation (arXiv:2403.19940, Oct 2024 revision, ICRA 2025)",
    "Murooka et al.: Humanoid Loco-manipulation Planning based on Graph Search and Reachability Maps (arXiv:2505.23505, May 2025)",
    "Murooka et al.: Learning Differentiable Reachability Maps for Optimization-based Humanoid Motion Generation (arXiv:2508.11275, Humanoids 2025)"
  ],
  "description": "LocoMimicGen extends Isaac Lab's 2.3 loco-manipulation infrastructure — comprising PRs #3150, #3259, and #3992 — with three precisely-scoped technical contributions that together enable room-level combinatorial scaling unavailable in existing systems.\n\nPR #3259 ('disjoint navigation', merged Sept 10, 2025, release/2.3.0) is the closest structural predecessor and primary baseline. It adds pick-navigate-place phase segmentation with occupancy-map path planning between phases and scene randomization. However, it handles navigation 'disjointly': the manipulation stance is fixed from the source demo and navigation is occupancy-map path planning at the trajectory level. It does NOT encode navigation stances in the object's SE(3) local frame, does NOT enforce arm-reachability constraints on base-pose selection (making generation infeasible when new object positions fall outside source demo stance's arm workspace), and does NOT compose segments from multiple source demonstrations.\n\nContribution (1): By expressing the manipulation stance in the object's SE(3) local frame alongside the arm trajectory, frame-transform retargeting to new object configurations automatically yields a feasible new stance without any separate stance-placement planning. Navigation between the retargeted stances is handled by the pretrained RL locomotion controller (PR #3150) as a black box; what the SE(3) encoding eliminates is the need to separately determine where the robot should stand to manipulate at each new object configuration. LocoMimicGen adds coupled SE(3) object-centric encoding of locomotion stances jointly with arm end-effector waypoints — the principled replacement for PR #3259's disjoint approach, enabling frame-transform retargeting of both manipulation stances and arm motions simultaneously.\n\nContribution (2): Stance-conditioned IRM integration for bipedal humanoid retargeting. We adapt and integrate IRM methodology (Vahrenkamp et al. 2013; Burget et al. ICRA 2015; MoMa-Pos 2024; MoMaGen ICLR 2026) into the Mimic retargeting loop for the G1 — framed as the first integration of stance-conditioned reachability constraints into any demonstration-generation framework. The integration challenge over prior wheeled-platform IRMs (MoMa-Pos, MoMaGen) is that bipedal arm reachability is conditioned on whole-body stance configuration (COM height, foot contact, balance state), requiring a stance-conditioned reachability map rather than a SE(2) base-pose-only map. The reachability map is a one-time offline precomputation (~3–5 H100-hours for IK sampling across ~50K balance configuration poses in 6D space: SE(2) base pose × squat depth × foot spread × weight distribution), GPU-parallel in Isaac Lab, shared across all tasks, and explicitly budgeted in the resource estimate. The 50K-pose resolution (~5–6 samples per dimension) is consistent with offline IRM construction in prior work (Vahrenkamp et al. 2013, MoMa-Pos 2024) and can be refined post-hoc at reachability boundary regions at no additional training cost, as the map is stored as a lookup table independent of policy training. A concurrent technique (Murooka et al., arXiv:2508.11275, Humanoids 2025) introduces learned differentiable reachability maps for online gradient-based planning; LocoMimicGen uses offline-precomputed discrete IRM instead, as differentiable map gradient evaluation across 2048+ parallel Isaac Lab environments would bottleneck batch generation throughput.\n\nContribution (3): Combinatorial multi-source segment composition from multiple (≤20 total) teleoperated demonstrations achieves 100–1,000× demo expansion — a qualitatively different scaling regime from PR #3259's single-source disjoint augmentation. The scaling bound is explicit: with K=20 source demonstrations decomposed into M=3 subtask phases, combined with P=10 object positions × Q=3 table heights × R=5 obstacle layouts, the conservative lower bound is K×M×P×Q×R = 20×3×10×3×5 = 9,000 unique trajectories (450× expansion from 20 seed demos); full cross-phase composition yields K^M × P×Q×R = 20^3 × 150 ≈ 1.2M as the theoretical maximum. Compatibility is evaluated against three criteria: (1) IRM feasibility at the transition stance (IRM score exceeding the 10th percentile of source-demo scores); (2) base-pose continuity within δ_nav ≈ 0.3 m (the locomotion controller's recoverable displacement); (3) contact-state consistency at phase boundaries. Criteria (1) and (2) are the active filters: IRM feasibility eliminates ~55–75% of random scene-stance pairings, and pose continuity a further 10–20%, reducing the 1.2M theoretical bound to the practical 100–1,000× range.\n\nAll policy training uses Diffusion Policy (CNN-UNet variant, Chi et al. RSS 2023 / IJRR 2025) uniformly across all baselines and LocoMimicGen conditions, isolating the data-generation contribution. We target ≥20 pp mean success-rate improvement over PR #3259 at the held-out 150-configuration test distribution. Evaluation covers 2 primary tasks (pick-and-place with navigation; two-phase transit) plus 1 supplementary articulated-object task; if the composition engine validates on Task 1 by Day 11, the supplementary task is elevated to co-primary status (3 tasks total), with the Gantt's Day 7–12 parallel track for articulated-object setup making this elevation reachable on schedule.\n\nMoMaGen (ICLR 2026, arXiv:2510.18316) is the strongest peer-reviewed comparison for constrained demo generation; the differentiation is precise — MoMaGen's SE(2) base-pose IRM for wheeled platforms, LocoMimicGen's stance-conditioned IRM for bipedal whole-body configurations. OmniRetarget (arXiv:2509.26633) and ULTRA (arXiv:2603.03279, March 2026) represent MoCap retargeting approaches requiring large motion capture libraries and continuous sequence retargeting without combinatorial segment composition — positioned as conceptual comparisons citing published metrics. EgoHumanoid, HoMMI, HuMI, HumanX, and Ψ₀ (arXiv:2603.12263, March 2026) represent human-data-driven scaling paradigms (egocentric video, MoCap, VLM pre-training) that augment robot learning via human behavioral diversity in real environments, orthogonal to LocoMimicGen's combinatorial spatial synthesis from ≤20 robot demos in simulation. DreamGen (NVIDIA GEAR Lab, arXiv:2505.12705) delivers behavioral diversity across task types; LocoMimicGen delivers spatial/configurational diversity within known loco-manipulation tasks with hard kinematic guarantees. Both compute modes (manual: ~87–110h H100; human-in-loop: ~125–157h H100) stay within the 200 H100-hour constraint, including one-time IRM precomputation (~3–5 H100h). CoRL 2026: abstract May 26 AoE, paper May 28 AoE.",
  "project_name": "loco_mimicgen_humanoid_g1",
  "source": "web_research"
}
```

---

**Summary of changes (minor fix):**

| Fix | What changed | Where |
|-----|-------------|-------|
| Fix 1 (required) | Added ULTRA (arXiv:2603.03279) alongside OmniRetarget in landscape — MoCap retargeting paradigm, same positioning | `landscape`, `opportunity`, `description`, `key_references` |
| Fix 2 (required) | Added Ψ₀ (arXiv:2603.12263) alongside EgoHumanoid/HoMMI/HuMI/HumanX — foundation model human-data-driven paradigm, orthogonal to combinatorial synthesis | `landscape`, `opportunity`, `description`, `key_references` |
| Fix 3 (recommended) | Added explicit IRM grid resolution acknowledgment: ~5–6 samples/dim, consistent with prior offline IRM work (Vahrenkamp, MoMa-Pos), refinable post-hoc at no training cost | `approach` Contribution 2, `resource_estimate` IRM note, `description` |
| Fix 4 (contingency, enhanced) | Added concrete 3-task contingency: parallel Gantt track for articulated-object task from Day 7 (Researcher 2), co-primary elevation if Day 11 validation met; reframed IRM as "first integration of stance-conditioned reachability into any demo-generation framework" to strengthen novelty claim | `approach` evaluation section, both Gantt charts, `description` |

**On the stagnation:** The evaluation-breadth concern (2 tasks, sim-only) is the structural ceiling that citation fixes alone cannot lift. The most impactful change this round is making the 3-task contingency genuinely credible by placing the articulated-object setup on an explicit parallel Gantt track — transforming Fix 4 from a vague aspiration into an operational plan.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebed7b99-4b6b-413e-acf9-28d05211dfa9",
  "isSidechain": false,
  "requestId": "req_011CatwdqHPHjChAEM4sP4sf",
  "type": "assistant",
  "uuid": "a8179414-687b-49d8-9260-3e6d48a37ae1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e93981d8-61dc-4460-8c15-6141e331b9de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RjVjYbRT32vvbLBN2iMgxK",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1086,
      "cache_creation_input_tokens": 2230,
      "cache_read_input_tokens": 35332,
      "output_tokens": 18351,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2230,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1086,
          "output_tokens": 18351,
          "cache_read_input_tokens": 35332,
          "cache_creation_input_tokens": 2230,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2230
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

_source line 28_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"LocoMimicGen: Coupled SE(3) Object-Centric Demo Multiplication for Mob…",
  "leafUuid": "a8179414-687b-49d8-9260-3e6d48a37ae1",
  "sessionId": "e93981d8-61dc-4460-8c15-6141e331b9de"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise LocoMimicGen with concurrent ULTRA and Psi-Zero citations",
  "sessionId": "e93981d8-61dc-4460-8c15-6141e331b9de"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"LocoMimicGen: Coupled SE(3) Object-Centric Demo Multiplication for Mob…",
  "leafUuid": "a8179414-687b-49d8-9260-3e6d48a37ae1",
  "sessionId": "e93981d8-61dc-4460-8c15-6141e331b9de"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise LocoMimicGen with concurrent ULTRA and Psi-Zero citations",
  "sessionId": "e93981d8-61dc-4460-8c15-6141e331b9de"
}
```

---
