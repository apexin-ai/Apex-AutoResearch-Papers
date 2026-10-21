---
dream_id: dream_20260526T023936
tier: best
overall_score: marginal reject (5/10)
timestamp: 2026-05-26T03:39:33.112880+00:00
---

## R2 Review: Novelty and Related Work

### Summary
This paper identifies that Collision Avoidance Rate (CAR) in VLA safety evaluation is systematically contaminated by action collapse (frozen robots registering as "safe"), proposes displacement-filtered CAR (dfCAR) as a corrective metric, and demonstrates through ablation that collision avoidance in fine-tuned VLAs originates from implicit demonstration signals rather than explicit SDF geometric supervision. The paper has pivoted from a method paper to a diagnostic/negative-finding paper, and its novelty rests primarily on the empirical observation that CAR is unreliable and the decomposition of avoidance sources.

### Strengths

- **The "fake safety" observation is well-documented and impactful.** The 91.5% CAR / 0% TSR / 99.6% frozen-episode finding on A1 is a striking empirical result. Even if action collapse is conceptually unsurprising, demonstrating that it inflates a widely-used safety metric by this magnitude is a genuine contribution to the VLA safety evaluation community. The 800-episode analysis is thorough.

- **dfCAR threshold robustness is convincing.** The bimodal gap (>200mm between frozen and active episodes) that renders dfCAR invariant across delta in [2, 200] mm is a clean result. This eliminates the obvious reviewer objection about threshold sensitivity. The metric is simple, principled, and immediately usable by practitioners.

- **The SDF redundancy finding is well-controlled.** The 4-point lambda dose-response curve (0, 0.005, 0.01, 0.1), cross-scene validation (object_pudding + spatial_bowl with opposite-sign deltas), and Phase 2 persistence ablation constitute a thorough negative result. The flat curve with R^2=0.12 across a 20x lambda range is convincing evidence of structural redundancy, not merely poor tuning.

- **Honest and detailed limitation disclosure.** The paper acknowledges restricted scope (2 model families, 2 scenes, OpenVLA blocked), low seed counts, and the distinction between conservative behavior and genuine safety awareness. This intellectual honesty is refreshing and appropriate for a diagnostic paper.

- **Per-task breakdown reveals mechanistic insight.** The consistent per-task CAR pattern across all seeds and conditions (task geometry dominates, not SDF strength) provides mechanistic understanding beyond aggregate numbers.

- **The related_work_v2.tex draft (not compiled into the dream paper) demonstrates awareness of the relevant literature landscape.** The three-way taxonomy (post-hoc correction / constrained optimization / inference-time guidance) for collision-safe VLA methods is well-organized.

### Weaknesses

- **Action collapse as a failure mode is not novel; the novelty is in documenting its metric contamination.** Action collapse / mode collapse is extensively documented in RL (degenerate policies), generative modeling (mode collapse in GANs/diffusion), and imitation learning (behavioral cloning averaging over multimodal demonstrations; Chi et al., RSS 2023). The paper's own literature map includes Dong et al. (2025) on "loss collapse" in diffusion policies — essentially the same phenomenon. The contribution is therefore narrower than the title "Rethinking VLA Safety Evaluation" suggests: it is "CAR does not account for action collapse," which, while useful, is closer to a benchmark/metrics paper than a conceptual advance.

- **The bibliography in the compiled dream paper is severely incomplete and partially fabricated.** The best-tier paper.tex contains 12 references, of which at least 4 are placeholder entries with "{Authors}" as the author field (sdf_safety2024, safe_diffusion2025, neural_sdf2023, diff_sdf2024, safety_metrics2023). These are not real papers — they appear to be invented citations. This is a critical deficiency. The project's own literature_map.yaml identifies 25+ real papers that should be cited but are not. A CoRL submission with fabricated bibliography entries would be desk-rejected.

- **dfCAR is conceptually simple — it is displacement thresholding + CAR.** While simplicity is a virtue, the intellectual contribution of "filter out frozen episodes before computing a rate" is modest. The bimodal gap that makes it threshold-robust is a property of this specific benchmark/model combination, not a guaranteed property of all VLA evaluations — the paper does not discuss what happens when the gap is not bimodal (partial collapse, slow-moving policies).

- **The SDF redundancy negative finding has limited scope for generalization.** The SDF loss is EE-only, applied to a specific VLA family (Pi0.5), on a specific benchmark (SafeLIBERO), with LoRA fine-tuning. The paper's own analysis identifies the structural limitation (EE-only SDF misses arm-body collisions), meaning the negative finding is partially expected from first principles. A full-body SDF or C-space distance field (Li et al., RSS 2024) might yield different results. The paper frames SDF redundancy as a general conclusion ("implicit demonstration signals, not explicit geometric supervision, drive collision avoidance"), which overgeneralizes from EE-only SDF to all geometric supervision.

- **The "decomposition" into implicit (demo) vs. explicit (SDF) is a two-condition ablation, not a framework.** Calling it a "decomposition" or "framework" overstates the methodological contribution. A genuine decomposition framework would need to disentangle multiple sources (data distribution, model capacity, training procedure, geometric signal) more systematically.

- **Only 2 model families tested, both from the Pi0 lineage.** The blocked OpenVLA experiment is a significant gap for a paper claiming to "rethink VLA safety evaluation" — the claim of generality is currently unsupported beyond the Pi0 family.

- **The TSR collapse (73% to 6%) under LoRA fine-tuning is not adequately analyzed.** The paper does not distinguish between the model learning to be conservative (safety-relevant) and the model losing task capability due to distribution shift (a fine-tuning artifact). Without this distinction, the claim that "fine-tuning produces genuine collision avoidance" is weakened.

### Questions for Authors

1. **On dfCAR generality:** The bimodal gap arises because action collapse in Pi0 produces near-zero displacement. What happens with models that exhibit partial collapse (slow but not frozen movement)? Is dfCAR robust in that regime?

2. **On the negative finding scope:** You conclude that "implicit demonstration signals, not explicit geometric supervision, drive collision avoidance." But your geometric supervision is EE-only SDF, which you identify as structurally limited. Would you expect the same conclusion for full-body SDF or C-space distance fields?

3. **On the TSR collapse mechanism:** Can you provide evidence that the 73% to 6% TSR drop reflects learned conservatism rather than catastrophic forgetting? Do fine-tuned models approach obstacles and retreat, or fail to reach task regions entirely?

4. **On cross-model generalization:** Your title claims "Rethinking VLA Safety Evaluation," but all results are on the Pi0 family. Can you provide any evidence that fake safety is not Pi0-specific?

5. **On CAR-TSR anti-correlation:** The observation that models attempting more tasks collide more is near-tautological. What would constitute a surprising violation of this pattern?

### Missing Related Work

- **Safe RL foundations:** CPO (Achiam et al., ICML 2017), Lagrangian methods for constrained MDPs. SafeVLA (Zhang et al., NeurIPS 2025 Spotlight) gets only one sentence.
- **Action collapse / mode collapse:** Diffusion Policy (Chi et al., RSS 2023), Dong et al. (2025) on loss collapse in diffusion policies.
- **Other geometric representations:** C-space distance fields (Li et al., RSS 2024), full-body SDF (Zhu et al., 2024), Neural NMPC with SDF (Jacquet et al., IJRR 2025).
- **Metric validity in ML:** Goodhart's law literature, benchmark saturation (Gururangan et al., 2018).
- **VLA foundations:** RT-2, OpenVLA, Octo, LIBERO benchmark proper citation.
- **Runtime safety methods:** RAIL, TamedPUMA, APEX — all in the project's literature map but absent from the paper.
- **Spatial/3D-aware VLAs:** Spatial Forcing (ICLR 2026), QDepth-VLA — relevant as geometric auxiliary losses similar in spirit.

### Minor Issues

- Title mismatch across drafts; should settle on one.
- Fabricated bibliography entries ({Authors}) must be replaced with real citations.
- Welch t-test with df~3 has extremely low power; "SDF contributes 0 pp" should be hedged as "no detectable effect at our sample size."
- 8 tables in 7 pages is dense; some could be consolidated or moved to appendix.
- Discussion section is thin — missing comparison to concurrent work, implications for VLA architecture design, connection to safe RL theory.

### Scores
- Originality: 2 (fair) — Action collapse is known; dfCAR is simple thresholding; SDF redundancy partially expected from EE-only limitation. Useful empirical combination but no single highly novel component.
- Significance: 2 (fair) — Metric contamination finding is practically useful but scope is narrow (1 benchmark, 2 model families, 2 scenes) for the breadth of claims.
- Clarity: 3 (good) — Well-written, logically structured, appropriately hedged. Main issue is fabricated/placeholder references.
- Overall: 5 (marginal reject) — Valid empirical contribution but incremental novelty, narrow scope for the claims, critically incomplete bibliography with fabricated entries, and "framework" framing overstates a two-condition ablation. Below CoRL acceptance bar in current form. Fixable with proper references, scoped claims, and additional model families.
- Confidence: 4 (high) — Familiar with VLA safety, SDF-in-robotics, and safe RL literatures.