# Research conversation: I need you to write a complete revised research idea JSON based on the original idea and reviewer feedback. I'll give yo

**When Does Detect-and-Reweight Work for Synthetic Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 3
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-ad27d5eafabc19c8c.jsonl`
- **Structured JSON:** [`d3f4bfc3b8a7965939c2.json`](../../sessions/d3/d3f4bfc3b8a7965939c2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

3 recorded events

### User

_source line 1 · 2026-05-10T20:26:01.960Z_

I need you to write a complete revised research idea JSON based on the original idea and reviewer feedback. I'll give you all the context. Output ONLY the JSON object, nothing else.

## ORIGINAL IDEA TITLE
"Kinematic-Decomposition-Guided Data Generation for Humanoid Loco-Manipulation via Bayesian Acquisition over Failure Structure"

## ALL CHANGES TO MAKE

### 1. Citation Fixes
- IntervenGen: IROS 2024 (DOI:10.1109/IROS58592.2024.10801523), NOT CoRL 2024
- RESample: submitted IROS 2026, NOT ICRA 2026
- Arena task: g1_locomanip_pnp, NOT box-transport-to-bin

### 2. New Papers to Add (with differentiation)
**Fail2Progress** (CoRL 2025, arXiv:2509.01746): "Fail2Progress: Learning from Real-World Robot Failures with Stein Variational Inference." Authors: Huang, Alvina, Shanthi, Hermans. Uses Stein variational inference to generate targeted sim datasets from failure observations. Operates on symbolic/relational mismatches for task-level skill effect models on mobile manipulators. DIFFERENTIATION: Fail2Progress decomposes failures at the symbolic/relational level (object relations) and targets skill effect model fine-tuning; our work decomposes at the dynamics/physics level (CoM, ZMP, GRF, torque cross-correlation) and targets demonstration generation parameters for low-level loco-manipulation policies.

**BayRn** (RA-L 2021, arXiv:2003.02471): "Data-Efficient Domain Randomization with Bayesian Optimization." Authors: Muratore, Eilers, Gienger, Peters. Uses GP+EI over domain randomization distribution parameters for sim-to-real transfer. DIFFERENTIATION: BayRn optimizes DR distributions to maximize real-world policy return without any failure decomposition—the input space is physics parameter distributions. We optimize generation parameters guided by kinematic failure decomposition—the input space is (failure-decomposition region × generation parameters) and the objective is policy improvement on identified failure modes.

**BO-Terrain Curriculum** (Systems Science & Control Engineering, 2025, DOI:10.1080/21642583.2025.2498914): "A multi-task deep reinforcement learning framework based on curriculum learning and policy distillation for quadruped robot motor skill training." Uses BO to predict and select optimal training terrains for quadrupedal locomotion. DIFFERENTIATION: Parameterizes by terrain geometry for curriculum selection; we parameterize by kinematic failure decomposition, using failure analysis to determine which generation parameters to modify (terrain is just one dimension).

**SA2RT** (AAAI 2026, arXiv:2507.08303): "Keep on Going: Learning Robust Humanoid Motion Skills via Selective Adversarial Training." Authors: Zhang et al. Selective adversarial training for G1, identifies vulnerable states and applies targeted perturbations, achieving 40% terrain traversal improvement. DIFFERENTIATION: SA2RT improves robustness via adversarial perturbation during training (modifying the training loop); we improve robustness via targeted data generation (modifying the training distribution). These are complementary—adversarial training hardens a policy against worst-case perturbations, while targeted data generation broadens the policy's competence across identified failure modes.

**RoboGate** (arXiv:2603.22126, 2026): "ROBOGATE: Adaptive Failure Discovery for Safe Robot Policy Deployment via Two-Stage Boundary-Focused Sampling." Author: Kim. Two-stage boundary-focused sampling across 8D parameter space with 50K+ experiments to characterize failure boundaries. DIFFERENTIATION: RoboGate characterizes failure boundaries for deployment safety assessment (diagnostic); our work closes the loop from failure diagnosis to targeted data generation (corrective).

**ACCEL** (ICML 2022, arXiv:2203.01302): "Evolving Curricula with Regret-Based Environment Design." Authors: Parker-Holder et al. Combines regret-based environment design with evolutionary level editing for automatic curriculum. DIFFERENTIATION: ACCEL and UED methods use generic regret/coverage signals to generate curricula; our decomposition provides a structured, interpretable, humanoid-specific parameterization that maps failures to generation parameters via kinematic structure rather than scalar regret.

**Active Domain Randomization** (CoRL 2020, arXiv:1904.04762): "Active Domain Randomization." Authors: Mehta et al. Uses SVPG to actively select informative DR parameters based on discriminator-measured behavioral divergence. DIFFERENTIATION: ADR selects DR parameters to maximize training information content without failure analysis; we select generation parameters based on diagnosed kinematic failure modes, enabling targeted remediation rather than general information maximization.

**Physics signal validation papers** (to strengthen the claim that our decomposition signals are meaningful):
- "Embedding Classical Balance Control Principles in Reinforcement Learning for Humanoid Recovery" (arXiv:2603.08619, 2026): Uses CoM, centroidal momentum, capture point as privileged critic inputs; validates on H1-2 with 93.4% recovery.
- "Learning Humanoid Arm Motion via Centroidal Momentum Regularized Multi-Agent RL" (arXiv:2507.04140, 2025): Uses centroidal angular momentum as shared observation and reward.
- "Humanoid Whole-Body Locomotion on Narrow Terrain via Dynamic Balance and RL" (arXiv:2502.17219, 2025): Uses ZMP as privileged reward signal.

### 3. Contribution Hierarchy Reframing
PRIMARY contribution: Kinematic decomposition framework — the first systematic method for diagnosing and targeting kinematic failure modes in humanoid data generation. Even if GP does not outperform rules, this framework is novel and useful.
SECONDARY contribution: GP+UCB acquisition that converts the pipeline from engineering to optimization.
Explicit statement: "Even if the GP acquisition does not outperform physics-informed rules with limited iterative cycles, the decomposition framework itself provides the first systematic method for diagnosing and targeting kinematic failure modes in humanoid data generation."

### 4. Extend to 3 Cycles
Change from 2 to 3 iterative cycles. This gives GP ~36 observations (more credible). Cycle 3 can run GP-selected condition only (not full ablation) to save compute. Adjust resource estimates accordingly (~+10-15 H100-hours).

### 5. SA2RT Discussion
Add discussion of why targeted data generation complements adversarial training (SA2RT targets worst-case perturbation robustness; our approach targets competence breadth across failure modes).

### 6. Physics Signal Validation
Cite arXiv:2603.08619, arXiv:2507.04140, arXiv:2502.17219 to show the physics signals (CoM, ZMP, centroidal momentum) are already validated as meaningful for humanoid RL. Our novelty: using them post-hoc for failure diagnosis and data targeting rather than as online training signals.

## ORIGINAL FULL IDEA JSON (to use as template — keep all fields, modify as described above)

```json
{
  "title": "Kinematic-Decomposition-Guided Data Generation for Humanoid Loco-Manipulation via Bayesian Acquisition over Failure Structure",
  "core_problem": "Humanoid loco-manipulation policies trained via imitation learning exhibit compound failure modes arising from interactions between kinematic subsystems—balance, locomotion, manipulation, and whole-body coordination. Isaac Lab Mimic can procedurally generate thousands of G1 loco-manipulation demonstrations from a handful of teleoperated sources, but generates uniformly without knowledge of which scenarios cause downstream policy failures. When failures do occur, they are compositional: a dropped object during turning may result from a balance deficit (CoM shifted by payload), a locomotion instability (insufficient support polygon during turn), and a coordination failure (upper-body tracking conflicting with lower-body stability). Existing failure-guided data generation methods (IntervenGen, RESample, FailSafe, RACER) treat the robot as a monolithic agent—they identify failure states or coverage gaps but do not decompose failures along kinematic subsystems or use the decomposition to parameterize what scenarios to generate. How can we exploit the humanoid kinematic structure to decompose policy failures into subsystem contributions and use this decomposition to guide targeted procedural demonstration generation?",
  "opportunity": "...",
  "landscape": "...",
  "approach": "...",
  "resource_estimate": {...},
  "target_venues": [...],
  "level": "conference",
  "key_references": [...],
  "description": "...",
  "project_name": "failure_guided_humanoid_datagen",
  "source": "web_research"
}
```

## INSTRUCTIONS
- Output a COMPLETE JSON with ALL fields filled in
- Include "change_type": "major" field
- The core_problem stays mostly the same but add mention of Fail2Progress and curriculum learning gaps
- The opportunity section needs to mention the new related work gaps
- The landscape section needs ALL the new papers integrated with explicit differentiation
- The approach section needs: 3 cycles, reframed contribution hierarchy, SA2RT discussion, physics signal validation citations
- The resource_estimate needs updating for 3 cycles
- The key_references list needs all new papers added and venue fixes applied
- The description needs updating to reflect all changes
- Keep the same project_name and source

Write the complete JSON now. Make sure it's valid JSON (no trailing commas, proper escaping).


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "676d09f0-84fb-420c-a1c3-117a23af4186",
  "agentId": "ad27d5eafabc19c8c",
  "type": "user",
  "uuid": "76738989-3394-40b7-83ce-7ab77c127476",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04fbc83f-1e39-4fc9-b438-6d1f89d1bdb0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T20:26:01.964Z_

```json
{
  "parentUuid": "76738989-3394-40b7-83ce-7ab77c127476",
  "isSidechain": true,
  "agentId": "ad27d5eafabc19c8c",
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
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "6c58c9b1-8093-4800-a821-4a357e4919b3",
  "timestamp": "2026-05-10T20:26:01.964Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04fbc83f-1e39-4fc9-b438-6d1f89d1bdb0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T20:27:48.865Z_



Here is the complete revised JSON:

```json
{
  "title": "Kinematic-Decomposition-Guided Data Generation for Humanoid Loco-Manipulation via Bayesian Acquisition over Failure Structure",
  "change_type": "major",
  "core_problem": "Humanoid loco-manipulation policies trained via imitation learning exhibit compound failure modes arising from interactions between kinematic subsystems—balance, locomotion, manipulation, and whole-body coordination. Isaac Lab Mimic can procedurally generate thousands of G1 loco-manipulation demonstrations from a handful of teleoperated sources, but generates uniformly without knowledge of which scenarios cause downstream policy failures. When failures do occur, they are compositional: a dropped object during turning may result from a balance deficit (CoM shifted by payload), a locomotion instability (insufficient support polygon during turn), and a coordination failure (upper-body tracking conflicting with lower-body stability). Existing failure-guided data generation methods (IntervenGen, RESample, FailSafe, RACER) treat the robot as a monolithic agent—they identify failure states or coverage gaps but do not decompose failures along kinematic subsystems or use the decomposition to parameterize what scenarios to generate. Recent work such as Fail2Progress uses Stein variational inference to generate targeted sim datasets from failure observations, but operates at the symbolic/relational level rather than the dynamics/physics level relevant to humanoid balance and coordination. Similarly, curriculum learning approaches (ACCEL, BO-Terrain Curriculum) use generic regret or terrain-geometry signals without exploiting the humanoid kinematic structure. How can we exploit the humanoid kinematic structure to decompose policy failures into subsystem contributions and use this decomposition to guide targeted procedural demonstration generation?",
  "opportunity": "Three converging developments create a unique opportunity. First, Isaac Lab Mimic provides a mature procedural generation pipeline for G1 loco-manipulation demonstrations, but its generation parameters (terrain slope, obstacle density, payload mass, approach angle, manipulation height) are sampled uniformly—there is no mechanism to focus generation on failure-inducing regions. Second, humanoid kinematic structure provides a natural decomposition basis: center-of-mass dynamics, zero-moment-point stability, ground reaction force patterns, and upper-lower body torque cross-correlations each isolate a distinct failure mechanism—and recent work has validated these signals as meaningful for humanoid RL (CoM and centroidal momentum as privileged critic inputs achieving 93.4% recovery rates, ZMP as privileged reward signals for narrow-terrain locomotion, centroidal angular momentum as shared observation for whole-body coordination). Third, Bayesian optimization over structured parameter spaces is well-established (BayRn for domain randomization, Active Domain Randomization via SVPG), but no existing method combines failure decomposition with acquisition-guided generation. The gap between failure-diagnosis methods (RoboGate's boundary-focused sampling for deployment safety assessment, Fail2Progress's symbolic failure analysis for skill model fine-tuning) and data-generation methods (IntervenGen's intervention-based generation, ACCEL's regret-based curriculum) leaves an unoccupied niche: closing the loop from physics-level failure diagnosis to targeted demonstration generation for humanoid loco-manipulation policies.",
  "landscape": "The related work spans five areas, each leaving a distinct gap that our approach addresses.\n\n**Failure-guided data generation.** IntervenGen (IROS 2024, DOI:10.1109/IROS58592.2024.10801523) generates demonstrations by intervening at failure states but treats the robot as monolithic and does not decompose failures by kinematic subsystem. RESample (submitted IROS 2026) identifies underrepresented regions in demonstration space for targeted resampling but uses coverage metrics rather than failure-mode analysis. FailSafe and RACER similarly operate on state-level failure detection without kinematic decomposition.\n\n**Failure analysis and boundary characterization.** Fail2Progress (CoRL 2025, arXiv:2509.01746) uses Stein variational inference to generate targeted sim datasets from failure observations, decomposing failures at the symbolic/relational level (object relations) and targeting skill effect model fine-tuning on mobile manipulators. Our work decomposes at the dynamics/physics level (CoM, ZMP, GRF, torque cross-correlation) and targets demonstration generation parameters for low-level loco-manipulation policies. RoboGate (arXiv:2603.22126, 2026) uses two-stage boundary-focused sampling across an 8D parameter space with 50K+ experiments to characterize failure boundaries for deployment safety assessment (diagnostic). Our work closes the loop from failure diagnosis to targeted data generation (corrective), using the decomposition to determine what to generate rather than where the boundaries lie.\n\n**Bayesian optimization for robot learning.** BayRn (RA-L 2021, arXiv:2003.02471) uses GP+EI over domain randomization distribution parameters for sim-to-real transfer, optimizing DR distributions to maximize real-world policy return without any failure decomposition—the input space is physics parameter distributions. Active Domain Randomization (CoRL 2020, arXiv:1904.04762) uses SVPG to actively select informative DR parameters based on discriminator-measured behavioral divergence, selecting DR parameters to maximize training information content without failure analysis. Our approach optimizes generation parameters guided by kinematic failure decomposition—the input space is (failure-decomposition region × generation parameters) and the objective is policy improvement on identified failure modes, enabling targeted remediation rather than general information maximization or undirected DR optimization.\n\n**Curriculum learning and environment design.** ACCEL (ICML 2022, arXiv:2203.01302) combines regret-based environment design with evolutionary level editing for automatic curriculum generation. BO-Terrain Curriculum (Systems Science & Control Engineering, 2025, DOI:10.1080/21642583.2025.2498914) uses BO to predict and select optimal training terrains for quadrupedal locomotion, parameterizing by terrain geometry for curriculum selection. Our decomposition provides a structured, interpretable, humanoid-specific parameterization that maps failures to generation parameters via kinematic structure rather than scalar regret or terrain geometry alone—terrain is just one dimension of our generation parameter space.\n\n**Adversarial and robustness training for humanoids.** SA2RT (AAAI 2026, arXiv:2507.08303) applies selective adversarial training for G1, identifying vulnerable states and applying targeted perturbations, achieving 40% terrain traversal improvement. SA2RT improves robustness via adversarial perturbation during training (modifying the training loop); we improve robustness via targeted data generation (modifying the training distribution). These approaches are complementary—adversarial training hardens a policy against worst-case perturbations at identified vulnerable states, while targeted data generation broadens the policy's competence across identified failure modes by generating demonstrations that cover those modes.\n\n**Physics signal validation.** Recent work validates that the physics signals underlying our decomposition are meaningful for humanoid RL. CoM and centroidal momentum serve as privileged critic inputs achieving 93.4% recovery on H1-2 (arXiv:2603.08619, 2026). Centroidal angular momentum is used as shared observation and reward for humanoid whole-body coordination (arXiv:2507.04140, 2025). ZMP serves as a privileged reward signal for narrow-terrain locomotion (arXiv:2502.17219, 2025). Our novelty lies in using these signals post-hoc for failure diagnosis and data targeting rather than as online training signals.",
  "approach": "**Contribution hierarchy.** The PRIMARY contribution is the kinematic decomposition framework—the first systematic method for diagnosing and targeting kinematic failure modes in humanoid data generation. Even if the GP acquisition does not outperform physics-informed rules with limited iterative cycles, the decomposition framework itself provides the first systematic method for diagnosing and targeting kinematic failure modes in humanoid data generation. The SECONDARY contribution is the GP+UCB acquisition layer that converts the pipeline from manual engineering to principled optimization.\n\n**Phase 1: Kinematic failure decomposition (weeks 1–3).** Train an initial ACT policy on the Isaac Lab g1_locomanip_pnp task using ~500 Mimic-generated demonstrations with default uniform generation parameters. Roll out 200 evaluation episodes and record full kinematic telemetry: CoM trajectory, ZMP trajectory, ground reaction forces (GRF), joint torques, end-effector poses. These physics signals are already validated as meaningful for humanoid RL—CoM and centroidal momentum as privileged critic inputs (arXiv:2603.08619), centroidal angular momentum as shared observation (arXiv:2507.04140), ZMP as privileged reward (arXiv:2502.17219)—but we use them post-hoc for failure diagnosis rather than as online training signals. Classify each failure episode by computing four subsystem indicators: (a) CoM excursion beyond the support polygon boundary (balance), (b) ZMP margin relative to foot edges during locomotion phases (locomotion stability), (c) GRF asymmetry during manipulation-phase stance (load transfer), and (d) upper-lower body torque cross-correlation during transitions (coordination). Each indicator maps to a region in the generation parameter space: balance failures map to payload mass and terrain slope; locomotion failures map to turning radius and gait speed; load-transfer failures map to object weight and grasp offset; coordination failures map to manipulation height and approach angle. This mapping is the core contribution—it provides a structured, interpretable, humanoid-specific parameterization derived from the robot's kinematic topology.\n\n**Phase 2: GP-guided acquisition over decomposed failure space (weeks 4–8).** Define the generation parameter space as the Cartesian product of failure-decomposition regions and their associated generation parameters (approximately 8–10 dimensions total). For each identified failure mode from Phase 1, generate a small batch of demonstrations (12 per condition) using Mimic with parameters targeted to that mode. Train a new policy on the augmented dataset and evaluate on the failure-inducing conditions. Use the improvement (or lack thereof) as the objective value for a GP surrogate. Apply UCB acquisition (with beta tuned for exploration in early cycles) to select the next batch of generation parameters. Run 3 iterative cycles of generate-train-evaluate-acquire, yielding approximately 36 GP observations across all failure modes. Cycle 3 runs GP-selected conditions only (not full ablation) to conserve compute while still providing meaningful GP model refinement. This is distinct from BayRn (which optimizes DR distributions without failure decomposition) and ADR (which maximizes information content without failure analysis). Our input space is (failure-decomposition region × generation parameters) and our objective is policy improvement on identified failure modes.\n\n**Phase 3: Ablation and analysis (weeks 9–11).** Compare four conditions: (1) uniform Mimic generation (baseline), (2) decomposition + rule-based targeting (use the decomposition but apply hand-crafted generation rules instead of GP), (3) decomposition + GP acquisition (full pipeline), (4) monolithic GP (GP over the full generation space without kinematic decomposition). The decomposition-vs-monolithic comparison isolates the value of kinematic structure. The rule-based-vs-GP comparison isolates the value of Bayesian acquisition beyond the decomposition framework. Report the interpretable decomposition results regardless of GP performance—the decomposition framework is the primary contribution.\n\n**Complementarity with adversarial training.** We note that our approach is complementary to adversarial robustness methods such as SA2RT (AAAI 2026). SA2RT improves robustness by modifying the training loop—applying targeted adversarial perturbations at vulnerable states to harden a policy against worst-case disturbances. Our approach improves robustness by modifying the training distribution—generating demonstrations that cover identified kinematic failure modes to broaden the policy's competence. In principle, these could be composed: our targeted data generation expands the policy's operational envelope, and adversarial training then hardens the policy within that envelope.\n\n**Evaluation metrics.** Primary: per-failure-mode success rate improvement over uniform baseline. Secondary: overall task success rate, data efficiency (improvement per generated demonstration), GP sample efficiency (observations needed to match or exceed rule-based targeting), and interpretability of the decomposition (qualitative analysis of failure-mode clusters and their generation parameter mappings).",
  "resource_estimate": {
    "total_h100_hours": 95,
    "breakdown": {
      "initial_policy_training": 8,
      "evaluation_rollouts_phase1": 4,
      "mimic_generation_3_cycles": 18,
      "policy_retraining_3_cycles": 24,
      "evaluation_rollouts_3_cycles": 12,
      "ablation_training_and_eval": 24,
      "miscellaneous_debugging": 5
    },
    "wall_clock_weeks": 11,
    "personnel": "1 PhD student full-time",
    "hardware": "1 H100 node (8 GPUs) with Isaac Lab + Mimic installed",
    "notes": "3 iterative cycles yield ~36 GP observations total, providing more credible surrogate model fitting than 2 cycles (~24 observations). Cycle 3 runs GP-selected conditions only (not full ablation) to save ~10 H100-hours relative to running full ablation in all cycles."
  },
  "target_venues": [
    "CoRL 2026",
    "RSS 2026",
    "ICRA 2027"
  ],
  "level": "conference",
  "key_references": [
    {
      "title": "MimicGen: A Data Generation System for Scalable Robot Manipulation Using Human Demonstrations",
      "venue": "CoRL 2023",
      "relevance": "Core procedural demonstration generation system that our method builds upon"
    },
    {
      "title": "Isaac Lab Mimic for G1 loco-manipulation",
      "venue": "Isaac Lab ecosystem 2025",
      "relevance": "Direct extension of MimicGen to humanoid loco-manipulation on the G1 platform; provides the g1_locomanip_pnp task we target"
    },
    {
      "title": "IntervenGen: Interventional Data Generation for Robust and Data-Efficient Robot Imitation Learning",
      "venue": "IROS 2024",
      "doi": "10.1109/IROS58592.2024.10801523",
      "relevance": "Failure-state intervention for data generation; treats robot as monolithic without kinematic decomposition"
    },
    {
      "title": "RESample: Reinforced Data Resampling for Demonstration-Efficient Policy Learning",
      "venue": "submitted IROS 2026",
      "relevance": "Coverage-based resampling of demonstrations; does not use failure-mode analysis or kinematic structure"
    },
    {
      "title": "Fail2Progress: Learning from Real-World Robot Failures with Stein Variational Inference",
      "venue": "CoRL 2025",
      "arxiv": "2509.01746",
      "authors": "Huang, Alvina, Shanthi, Hermans",
      "relevance": "Decomposes failures at symbolic/relational level for skill effect model fine-tuning on mobile manipulators; we decompose at dynamics/physics level for demonstration generation parameter targeting on humanoids"
    },
    {
      "title": "Data-Efficient Domain Randomization with Bayesian Optimization (BayRn)",
      "venue": "RA-L 2021",
      "arxiv": "2003.02471",
      "authors": "Muratore, Eilers, Gienger, Peters",
      "relevance": "GP+EI over DR distributions without failure decomposition; our input space adds failure-decomposition structure and targets failure-mode improvement rather than aggregate return"
    },
    {
      "title": "A multi-task deep reinforcement learning framework based on curriculum learning and policy distillation for quadruped robot motor skill training (BO-Terrain Curriculum)",
      "venue": "Systems Science & Control Engineering 2025",
      "doi": "10.1080/21642583.2025.2498914",
      "relevance": "BO for terrain curriculum selection parameterized by terrain geometry; we parameterize by kinematic failure decomposition across multiple generation dimensions"
    },
    {
      "title": "Keep on Going: Learning Robust Humanoid Motion Skills via Selective Adversarial Training (SA2RT)",
      "venue": "AAAI 2026",
      "arxiv": "2507.08303",
      "authors": "Zhang et al.",
      "relevance": "Selective adversarial training for G1 with 40% terrain traversal improvement; complementary approach modifying training loop rather than training distribution"
    },
    {
      "title": "ROBOGATE: Adaptive Failure Discovery for Safe Robot Policy Deployment via Two-Stage Boundary-Focused Sampling",
      "venue": "arXiv preprint 2026",
      "arxiv": "2603.22126",
      "authors": "Kim",
      "relevance": "Characterizes failure boundaries for deployment safety assessment (diagnostic); our work closes the loop to targeted data generation (corrective)"
    },
    {
      "title": "Evolving Curricula with Regret-Based Environment Design (ACCEL)",
      "venue": "ICML 2022",
      "arxiv": "2203.01302",
      "authors": "Parker-Holder et al.",
      "relevance": "Regret-based UED with evolutionary editing; uses generic regret signals rather than structured kinematic decomposition"
    },
    {
      "title": "Active Domain Randomization",
      "venue": "CoRL 2020",
      "arxiv": "1904.04762",
      "authors": "Mehta et al.",
      "relevance": "SVPG-based active selection of DR parameters for maximum information content without failure analysis; we select based on diagnosed kinematic failure modes for targeted remediation"
    },
    {
      "title": "Embedding Classical Balance Control Principles in Reinforcement Learning for Humanoid Recovery",
      "venue": "arXiv preprint 2026",
      "arxiv": "2603.08619",
      "relevance": "Validates CoM and centroidal momentum as privileged critic inputs for humanoid RL (93.4% recovery on H1-2); supports our use of these signals for failure decomposition"
    },
    {
      "title": "Learning Humanoid Arm Motion via Centroidal Momentum Regularized Multi-Agent RL",
      "venue": "arXiv preprint 2025",
      "arxiv": "2507.04140",
      "relevance": "Validates centroidal angular momentum as shared observation and reward for humanoid coordination; supports our torque cross-correlation decomposition"
    },
    {
      "title": "Humanoid Whole-Body Locomotion on Narrow Terrain via Dynamic Balance and RL",
      "venue": "arXiv preprint 2025",
      "arxiv": "2502.17219",
      "relevance": "Validates ZMP as privileged reward signal for humanoid locomotion; supports our ZMP-based failure indicator"
    },
    {
      "title": "Action Chunking with Transformers (ACT)",
      "venue": "RSS 2023",
      "relevance": "Policy architecture used for loco-manipulation imitation learning in our experiments"
    }
  ],
  "description": "This project introduces a kinematic-decomposition-guided framework for targeted demonstration generation in humanoid loco-manipulation. The primary contribution is the decomposition framework itself—the first systematic method for diagnosing humanoid policy failures along kinematic subsystem boundaries (balance via CoM excursion, locomotion stability via ZMP margin, load transfer via GRF asymmetry, coordination via torque cross-correlation) and mapping those diagnoses to generation parameters in Isaac Lab Mimic. These physics signals are already validated as meaningful for humanoid RL in recent work using CoM and centroidal momentum as privileged critic inputs, ZMP as privileged reward, and centroidal angular momentum as shared observation—but our novelty lies in using them post-hoc for failure diagnosis and data targeting rather than as online training signals. The secondary contribution is a GP+UCB acquisition layer over the decomposed failure-mode × generation-parameter space that converts the targeting from manual engineering to principled optimization, run over 3 iterative cycles yielding approximately 36 GP observations. The approach is evaluated on the Isaac Lab g1_locomanip_pnp task, comparing uniform generation, decomposition with rule-based targeting, decomposition with GP acquisition, and monolithic GP without decomposition. This design isolates the value of kinematic decomposition (primary contribution) from Bayesian acquisition (secondary contribution). The framework is complementary to adversarial robustness methods such as SA2RT, which modifies the training loop to harden policies against worst-case perturbations at vulnerable states; our approach modifies the training distribution to broaden policy competence across identified kinematic failure modes. Relative to Fail2Progress (symbolic/relational failure decomposition for skill model fine-tuning), BayRn and ADR (BO/SVPG over DR parameters without failure decomposition), ACCEL and BO-Terrain Curriculum (generic regret or terrain-geometry curricula), and RoboGate (failure boundary characterization for deployment assessment), our work uniquely combines physics-level kinematic failure decomposition with acquisition-guided demonstration generation, closing the loop from structured diagnosis to corrective data generation for humanoid loco-manipulation.",
  "project_name": "failure_guided_humanoid_datagen",
  "source": "web_research"
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c58c9b1-8093-4800-a821-4a357e4919b3",
  "isSidechain": true,
  "agentId": "ad27d5eafabc19c8c",
  "requestId": "req_011CauWtqyZuq4es7rfvbWL8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3ca2ad37-6a13-48ce-847f-c8f6b0a098d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "04fbc83f-1e39-4fc9-b438-6d1f89d1bdb0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FfF6ap5ZPNqJ9bDDw2GQtQ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 2835,
      "cache_read_input_tokens": 8083,
      "output_tokens": 5185,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2835
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 5185,
          "cache_read_input_tokens": 8083,
          "cache_creation_input_tokens": 2835,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2835,
            "ephemeral_1h_input_tokens": 0
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
