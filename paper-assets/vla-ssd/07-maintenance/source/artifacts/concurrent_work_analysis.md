# Concurrent Work Analysis

## 1. Fang et al. 2026 — "When Vision Overrides Language: Evaluating and Mitigating Counterfactual Failures in VLAs"

**arXiv:** 2602.17659 (February 19, 2026)
**Authors:** Yu Fang, Yuchun Feng, Dong Jing, Jiaqi Liu, Yue Yang, Zhenyu Wei, Daniel Szafir, Mingyu Ding (UNC Chapel Hill)

### Summary

This paper identifies and addresses **counterfactual failures** in VLAs — models act based on vision shortcuts induced by dataset biases rather than faithfully following language instructions. Key contributions:

1. **LIBERO-CF Benchmark**: A counterfactual evaluation benchmark with 4 suites:
   - CF-Spatial (15 tasks): targets background objects as new manipulation targets
   - CF-Object (10 tasks): alternative object-centric instructions
   - CF-Long (10 tasks): multi-step instructions with new targets
   - CF-OOD (15 tasks): entirely unseen objects during finetuning
   - Metrics: grounding rate (gripper contact with target) + success rate (task completion)

2. **Counterfactual Action Guidance (CAG)**: A dual-branch inference scheme:
   - π_CAG(a|o,l) = π_uncond(a|o,∅) + ω·(π_cond(a|o,l) − π_uncond(a|o,∅))
   - Guidance scale ω controls language conditioning strength
   - Two variants: Training-Free (drop language at inference) and Vision-Action (train separate vision-only model)

3. **Evaluated VLAs**: OpenVLA-OFT (7B), π₀ (3B), π₀.₅, X-VLA (0.9B)

4. **Results**: CAG improves language-following by 9.7% (training-free) to 15.5% (with VA model); real-world: +17.2% success, −9.4% counterfactual failures.

### Overlap with Our Work

| Dimension | Fang et al. | Our VLA-SSD |
|-----------|------------|-------------|
| **Dataset** | LIBERO (Spatial, Object, Goal, Long) | LIBERO (same 4 suites) |
| **Core concept** | Counterfactual instruction perturbation | Counterfactual instruction perturbation |
| **Perturbation types** | Alternative feasible instructions (CF-Spatial/Object/Long/OOD) | 4 systematic conditions: empty/shuffled/wrong/paraphrased |
| **VLA architectures** | OpenVLA-OFT, π₀, π₀.₅, X-VLA | OpenVLA, TracVLA, NORA |
| **Analysis level** | Behavioral (success rate, grounding rate) | Representational (Cohen's d on internal features) |
| **Goal** | Mitigate failures via inference-time intervention | Understand how fine-tuning reorganizes representations |

**Specific overlaps:**
- Both use LIBERO as the primary evaluation platform
- Both study what happens when VLAs receive instructions that don't match the training distribution
- Both demonstrate that VLAs are biased toward vision-driven shortcuts over language grounding
- OpenVLA is a shared architecture across both studies

### Key Differentiation

1. **Behavioral vs. Representational**: Fang et al. measure whether the robot executes the correct task (behavioral output). We measure how internal representations change (Cohen's d) when instructions are perturbed — a fundamentally different analysis level.

2. **Perturbation design philosophy**: Their LIBERO-CF uses semantically valid alternative instructions that are feasible in the scene (e.g., "pick up the bowl" instead of "pick up the cup" when both are present). Our 4 conditions are systematic ablations of instruction content (empty = no language, shuffled = disrupted syntax, wrong = incorrect task, paraphrased = semantic preservation) — designed to probe which aspects of language the representations encode, not to test behavioral correctness.

3. **Mitigation vs. Understanding**: They propose CAG to fix counterfactual failures at inference time. We characterize how fine-tuning changes the representational sensitivity to language — our goal is mechanistic understanding, not a fix.

4. **Trained vs. untrained comparison**: Our core analysis compares trained vs. untrained VLAs under the same perturbations to reveal what fine-tuning changes. Fang et al. only evaluate fine-tuned models.

5. **Cross-architecture validation**: We test 3 architecturally distinct VLAs (autoregressive OpenVLA, TracVLA, diffusion-based NORA) to show generality of representational phenomena. They test 4 VLAs but focus on behavioral patterns.

### Suggested Citation Approach

Cite as complementary concurrent work. Our paper provides the representational explanation for *why* counterfactual failures occur (fine-tuning creates vision-dominant representations that are insufficiently sensitive to language). Their paper demonstrates the behavioral consequences and proposes a practical fix. Suggested framing:

> "Concurrent work by Fang et al. (2026) independently identifies counterfactual failures in VLAs on LIBERO and proposes an inference-time mitigation (CAG). Our analysis complements this finding by revealing the representational mechanism: fine-tuned VLAs show asymmetric sensitivity to instruction perturbations (Section 4.3), with empty and wrong instructions producing the largest representational shifts (high Cohen's d) while paraphrased instructions produce minimal shifts — suggesting that fine-tuning develops coarse language-presence detection rather than fine-grained instruction grounding, which explains the vision-override failures they observe behaviorally."

### BibTeX

```bibtex
@article{fang2026vision,
  title={When Vision Overrides Language: Evaluating and Mitigating Counterfactual Failures in {VLA}s},
  author={Fang, Yu and Feng, Yuchun and Jing, Dong and Liu, Jiaqi and Yang, Yue and Wei, Zhenyu and Szafir, Daniel and Ding, Mingyu},
  journal={arXiv preprint arXiv:2602.17659},
  year={2026}
}
```

---

## 2. Buurmeijer et al. 2026 — "Observing and Controlling Features in Vision-Language-Action Models"

**arXiv:** 2603.05487 (March 5, 2026)
**Authors:** Hugo Buurmeijer, Carmen Amo Alonso, Aiden Swann, Marco Pavone (Stanford)

### Summary

This paper applies mechanistic interpretability to VLAs, introducing two formal concepts:

1. **Feature-observability**: A feature ζ is observable at layer ℓ if a linear mapping f_ℓ(x_ℓ) = ζ can recover it from activations. They train linear probes (W_ℓx + b_ℓ) at every layer to classify/regress robot state features (position x/y/z, orientation, gripper aperture).

2. **Feature-controllability**: A feature is controllable if a minimal perturbation u to the activations can steer the output. They derive a closed-form optimal control solution: u_ℓ = (ζ_max − ζ_ℓ)W_ℓ / ‖W_ℓ‖² when the feature is out of desired bounds.

3. **Tested on**: π₀.₅ and OpenVLA, using 10 tasks from LIBERO Spatial suite (10 rollouts per task).

4. **Results**: Gripper control achieves near-perfect constraint satisfaction with >90% task success. Height and speed constraints also controllable. Negligible inference overhead.

5. **Scope limitation**: Only probes robot state/action features. Explicitly defers "more abstract semantic features such as object affordances, relational predicates, and task-level goals to future work."

### Overlap with Our Work

| Dimension | Buurmeijer et al. | Our VLA-SSD |
|-----------|-------------------|-------------|
| **Core method** | Linear probes on VLA hidden states | Linear probes on VLA hidden states |
| **Dataset** | LIBERO Spatial | LIBERO (4 suites) |
| **VLA architectures** | π₀.₅, OpenVLA | OpenVLA, TracVLA, NORA |
| **Layer analysis** | Probe every layer, select best | Probe across layers, analyze layer-wise patterns |
| **What is probed** | Robot state (position, orientation, gripper) | Task-relevant features, counterfactual sensitivity |
| **Goal** | Inference-time behavioral control | Understanding fine-tuning's representational effects |

**Specific overlaps:**
- Both use linear probing as the primary analytical tool on VLA internal representations
- Both test on LIBERO with OpenVLA
- Both demonstrate that VLA representations contain linearly decodable task-relevant information
- Both analyze multiple layers to find optimal probe placement

### Key Differentiation

1. **State features vs. task semantics**: They probe low-level robot state (x/y/z, gripper). We probe higher-level task semantics — how representations encode language instructions and respond to counterfactual perturbations.

2. **Control vs. Understanding**: Their goal is to steer VLA behavior at inference time via representation intervention. Our goal is to understand how fine-tuning reorganizes representations (trained vs. untrained comparison).

3. **Static vs. dynamic analysis**: They analyze a single model checkpoint (pretrained or fine-tuned). We compare trained vs. untrained models under matched conditions to reveal what fine-tuning changes.

4. **Scope of features**: They explicitly limit to motor features and defer semantic features. Our counterfactual analysis directly probes semantic/linguistic features — what they leave as future work, we address.

5. **Architecture breadth**: They test 2 architectures (π₀.₅, OpenVLA). We test 3 architecturally diverse VLAs (autoregressive, tracking-augmented, diffusion-based) for cross-architecture generalization.

6. **Formal framework**: They introduce a formal observability/controllability framework from control theory. We use established psychometric tools (Cohen's d, RSA) from cognitive neuroscience adapted to VLA analysis.

### Suggested Citation Approach

Cite as concurrent work on VLA mechanistic interpretability with complementary scope. Their work establishes that low-level motor features are linearly observable/controllable; our work extends to higher-level semantic features and studies how these representations change through fine-tuning.

> "Buurmeijer et al. (2026) concurrently demonstrate that VLA representations linearly encode robot state features and can be steered via minimal interventions. Our work is complementary: while they probe motor-level features (position, gripper state), we probe semantic-level features — specifically, how fine-tuning reshapes representational sensitivity to language instructions (Section 3.3). Together, these studies establish that VLA internal representations are interpretable across multiple levels of abstraction."

### BibTeX

```bibtex
@article{buurmeijer2026observing,
  title={Observing and Controlling Features in Vision-Language-Action Models},
  author={Buurmeijer, Hugo and Amo Alonso, Carmen and Swann, Aiden and Pavone, Marco},
  journal={arXiv preprint arXiv:2603.05487},
  year={2026}
}
```

---

## Summary: Positioning Our Work

| Aspect | Fang et al. | Buurmeijer et al. | **Ours (VLA-SSD)** |
|--------|-------------|--------------------|--------------------|
| Analysis level | Behavioral | Representational (motor) | **Representational (semantic)** |
| Counterfactual? | Yes (behavioral) | No | **Yes (representational)** |
| Probing? | No | Yes (state features) | **Yes (task/language features)** |
| Trained vs. untrained? | No | No | **Yes** |
| Cross-architecture? | 4 VLAs | 2 VLAs | **3 VLAs** |
| LIBERO? | Yes | Yes (Spatial only) | **Yes (4 suites)** |
| Goal | Mitigate failures | Control behavior | **Understand fine-tuning** |

Our work occupies a unique position: we combine the counterfactual perturbation approach (shared with Fang et al.) with the linear probing methodology (shared with Buurmeijer et al.) to answer a question neither addresses — how does VLA fine-tuning reorganize internal representations' sensitivity to language? This positions our contribution as providing the mechanistic explanation that bridges behavioral observations (Fang) and representational tools (Buurmeijer).
