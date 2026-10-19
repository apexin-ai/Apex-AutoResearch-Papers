## 5.5 Method Boundaries

The preceding analyses identify specific conditions under which SDF-based collision avoidance succeeds or fails. Three boundaries emerge from the negative results, each supported by controlled experiments that isolate a single factor. These boundaries are not incidental failures; they delineate the structural limits of end-effector SDF integration in vision-language-action models and explain why training-time supervision is the only viable path among the approaches we evaluated.

### Boundary 1: Gradient correction fails on collapsed policies

Runtime SDF gradient correction assumes the base policy generates trajectories with sufficient displacement for the correction to redirect around obstacles. When the policy has collapsed into near-zero displacement, this assumption breaks down regardless of SDF quality. We test this directly by constructing ground-truth SDF oracles that replace the learned distance predictor with exact signed distances computed from known obstacle meshes (Section 5.3). If the failure of learned SDF refinement were attributable to prediction error, oracle performance should substantially exceed that of unrefined baselines.

The oracle results refute this hypothesis. All three gradient correction variants produce CAR below that of unrefined baselines:

| Experiment | Variant | CAR (%) |
|---|---|---|
| `oracle_true_gt_adaptive_alpha_v11` | Action-space, adaptive $\alpha$ | 75.0 |
| `oracle_true_gt_fixed_alpha_v11` | Action-space, fixed $\alpha$=0.005 | 73.1 |
| `oracle_true_gt_feature_object_v11` | Feature-space | 76.9 |
| LoRA baseline (no refine) | -- | 82.0 |
| Full-FT baseline (no refine) | -- | 83.0 |

The best oracle (feature-space, 76.9%) falls 5.1 pp below the LoRA baseline. The A3 model with a learned SDF head (`eval_a3_object_m024fix_v11`) exhibits a complementary failure: its SDF predictions never fall below the refinement threshold across 160 evaluation episodes, producing zero refinement steps (CAR = 77.1%). The learned network calibrates itself to avoid triggering the safety mechanism, effectively reducing the model to an unrefined baseline.

The failure is invariant to the gradient space (action vs. feature), step-size schedule (adaptive vs. fixed), and distance-field quality (perfect vs. learned). This convergence isolates the cause: gradient correction requires a policy with a viable trajectory manifold, and collapsed policies (frozen rate > 95%, TSR $\approx$ 0%) have none. Perturbations either stay within the collapsed region (no effect) or push actions off the learned distribution (erratic motion that increases collisions on the arm body).

The implication is direct. Post-hoc SDF correction cannot substitute for training-time integration. Any scheme that applies SDF gradients to actions produced by a collapsed policy will fail for reasons that are independent of the SDF representation itself.

### Boundary 2: Collision transfer in constrained geometries

SDF auxiliary training loss does not uniformly improve collision avoidance across task geometries. Per-task analysis of Pi0.5+A1 at the step-10K checkpoint reveals a failure mode we term *collision transfer*: the SDF gradient pushes the end-effector away from one obstacle and into another.

On Task 3 (bbq\_sauce), the end-effector trajectory passes through a corridor of approximately 40 cm between two obstacles (wine\_bottle on the right, red\_coffee\_mug on the left). The point-wise SDF gradient during training pushes the end-effector away from the nearest obstacle surface, which for most trajectories is wine\_bottle. This shifts the learned trajectory distribution leftward, increasing collisions with red\_coffee\_mug on the opposite side.

| Experiment | Task 3 $\Delta$CAR vs. baseline | Collision episodes with red\_coffee\_mug |
|---|---|---|
| `train_pi05_a1_obj_s0_l005` ($\lambda$=0.005) | $-$8 pp | 10 (baseline: 5) |
| `train_pi05_a1_obj_s0_l01` ($\lambda$=0.01) | $-$6 pp | 8 (baseline: 5) |

The collision count with red\_coffee\_mug doubles under $\lambda$=0.005. On the same models, Task 0 (orange\_juice), where a single dominant obstacle stands in open space (baseline CAR = 10%), the SDF loss improves CAR by 49 pp. The contrast is sharp: obstacle density determines whether point-wise SDF training helps or hurts.

This result defines a geometric applicability condition for point-wise SDF training. The SDF gradient provides a locally correct signal ("move away from the nearest surface") that is globally incomplete when multiple obstacles constrain the workspace from opposing directions. The boundary is predictable from workspace geometry: tasks with high free-space margin around the collision-prone region benefit from SDF training, while tasks with narrow passages between obstacles are susceptible to collision transfer. Full-body SDF monitoring or trajectory-level optimization that accounts for multiple constraint surfaces simultaneously would be needed to address this limitation.

### Boundary 3: Training-time integration is the only viable path

The two boundaries above converge on a single conclusion. Collapsed policies reject post-hoc gradient correction (Boundary 1), and point-wise gradients can redistribute collisions in constrained geometries (Boundary 2). Training-time SDF auxiliary loss on a capable base model is the only evaluated configuration that produces genuine collision avoidance behavior.

Pi0.5+A1 (Section 5.4) achieves displacement-filtered CAR$_\text{f}$ > 0 with zero frozen rate at the step-10K checkpoint, occupying a region of TSR-CAR space that no runtime correction, oracle, or Pi0-based configuration reaches. The mechanism differs qualitatively from runtime refinement: the SDF loss shapes the policy's action distribution during training, producing trajectories that incorporate obstacle geometry from generation rather than as a post-hoc perturbation. This sidesteps the collapsed-policy barrier (Pi0.5 is not collapsed; its TSR = 74.7% confirms a viable trajectory manifold) and partially mitigates collision transfer (the training process can balance SDF gradients from multiple obstacles over many gradient steps, unlike single-step runtime correction).

The conjunction of these three boundaries yields a practical prescription for future work on VLA collision avoidance: (1) ensure the base policy is capable before adding safety supervision, (2) integrate geometric signals during training rather than at inference, and (3) validate per-task to detect collision transfer in constrained scenes.
