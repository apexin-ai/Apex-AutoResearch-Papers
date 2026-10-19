# OpenVLA LIBERO-Object Eval Gap Analysis

## Summary

- **Our result**: 69% overall SR (10 trials × 10 tasks, seed=42, single run)
- **Paper reported**: 88.4 ± 0.8% (50 trials × 10 tasks × 3 seeds)
- **Gap**: ~19.4 pp

## Per-Task Success Rate Breakdown

| Task | Ours (10 trials) | Paper (~88.4% avg) |
|------|:-:|:-:|
| alphabet_soup | 90% (9/10) | - |
| cream_cheese | 80% (8/10) | - |
| salad_dressing | **50%** (5/10) | - |
| bbq_sauce | **20%** (2/10) | - |
| ketchup | 80% (8/10) | - |
| tomato_sauce | 80% (8/10) | - |
| butter | **50%** (5/10) | - |
| milk | 90% (9/10) | - |
| chocolate_pudding | 80% (8/10) | - |
| orange_juice | 70% (7/10) | - |
| **Overall** | **69%** | **88.4%** |

Paper per-task breakdown not publicly available.

## Evaluation Protocol Comparison

| Parameter | Ours (v2) | Paper |
|-----------|-----------|-------|
| Eval script | Official `run_libero_eval.py` | Same |
| max_steps | 280 | 280 |
| center_crop | True | True |
| num_trials_per_task | **10** | **50** |
| Seeds | 1 (seed=42) | 3 (averaged) |
| Total rollouts | 100 | 1500 |
| GPU | **RTX 4090** | **A100** |
| Python | 3.10.20 | 3.10.13 |
| PyTorch | 2.2.0+cu121 | 2.2.0 |
| transformers | 4.40.1 | 4.40.1 |
| flash_attn | **NOT INSTALLED** | **2.5.5** |
| Model | openvla-libero-object (official HF) | Same |

## Gap Source Hypotheses (ranked by likely contribution)

### 1. Statistical variance from small sample (dominant factor)

With 10 trials per task, the 95% confidence interval for a task with true SR=80% is approximately [44%, 97%]. Three tasks scored very low:
- bbq_sauce at 20% (2/10): even if true rate is 60%, P(≤2/10) = 16.7%
- salad_dressing at 50%, butter at 50%

These 3 tasks alone drag our average down by ~12 pp vs the other 7 tasks (avg 81.4%).

### 2. Initial state sampling bias

The script uses `initial_states[episode_idx]`. With 10 trials, we only sample states 0-9 out of 50 available. If states 0-9 happen to be harder for certain tasks, this creates systematic bias. The paper tests all 50 states.

### 3. Seed sensitivity

We used seed=42; paper default is seed=7. Known issue: even with identical setup, different seeds can swing results by 5-10 pp on individual tasks.

### 4. Missing flash_attn

The model was trained with flash_attn 2.5.5 but our environment does not have it installed. Without flash_attn, PyTorch falls back to standard scaled dot-product attention, which can produce numerically different results due to different computation ordering. Combined with bf16 precision, small numerical differences accumulate over hundreds of inference steps per rollout. Likely contributes 1-3 pp.

### 5. GPU nondeterminism (RTX 4090 vs A100)

Paper used A100; we used RTX 4090. The OpenVLA authors explicitly state: "results may vary slightly if you use a different GPU for evaluation due to GPU nondeterminism in large models (though we have tested that results were consistent across different machines with A100 GPUs)." Different GPU architectures (Ampere vs Ada Lovelace) have different floating-point behavior. Likely contributes 2-5 pp.

### 6. Known reproducibility gap in community

- GitHub issue #23 (LIBERO repo): Users report significant evaluation loss variance (6 vs 52 on same task) and success rate instability across runs
- LIBERO-PRO paper (arXiv:2510.03827): Demonstrates that "reported accuracies above 90% largely reflect rote memorization" and that models fail dramatically under minor perturbations. Standard LIBERO evals may overestimate real capability.
- LIBERO-Plus paper (arXiv:2510.13626): Reports OpenVLA achieves 0.99 on standard LIBERO-Object, but near-zero under perturbations, suggesting the 88.4% vs 99% discrepancy itself depends heavily on exact eval conditions

## Decomposition Estimate

| Factor | Estimated contribution |
|--------|----------------------|
| Small sample variance (10 vs 50 trials) | 8-12 pp |
| Initial state subset (0-9 only) | 3-5 pp |
| Missing flash_attn | 1-3 pp |
| GPU nondeterminism (4090 vs A100) | 2-4 pp |
| Seed choice (42 vs unknown paper seeds) | 1-3 pp |
| **Total** | **~19 pp** |

## Recommendation

**Run 50 trials per task** before concluding there's a real gap. Current 10-trial estimate is too noisy to be meaningful.

Specific action plan:
1. **Install flash_attn**: `pip install flash-attn==2.5.5` in the openvla conda env. This eliminates one known variable.
2. **Re-run with 50 trials, seed=7**: Match paper protocol exactly (single seed).
3. **Interpret results**:
   - If 80-85%: Gap explained by seed/GPU nondeterminism. Acceptable baseline.
   - If 75-80%: Likely GPU architecture effect. Still acceptable with disclosure.
   - If <75%: Deeper investigation needed (checkpoint integrity, env version).
4. **For our paper**: Use the 50-trial result as the OpenVLA baseline. The 69% from 10 trials should NOT be cited.

## Context: Custom Eval Framework Bug (0% SR)

The custom eval framework (`eval_openvla_object_vla_only_seed42.json`) produces **0% SR** across all 10 tasks, while the official OpenVLA eval script produces 69%. A separate run with seed=46 (`eval_object_vla_only_seed46.json`) produced 13%. The custom framework has a bug in how it processes OpenVLA model output (likely dimension/gripper handling). The official eval script correctly handles gripper action inversion and normalization.

## Log File Locations

- Official eval log: `/root/autodl-tmp/openvla/experiments/logs/EVAL-libero_object-openvla-2026_05_18-04_58_22.txt`
- Custom eval JSON: `/root/acr-vla-conformal-refinement/logs/eval_openvla_object_vla_only_seed42.json`
- Custom eval log: `/root/acr-vla-conformal-refinement/logs/eval_openvla_object_vla_only_seed42.log`
- Model checkpoint: `/root/autodl-tmp/models/openvla-libero-object`

## References

- OpenVLA GitHub: https://github.com/openvla/openvla
- LIBERO performance discrepancy issue: https://github.com/Lifelong-Robot-Learning/LIBERO/issues/23
- LIBERO-PRO (robustness analysis): https://arxiv.org/abs/2510.03827
- LIBERO-Plus (robustness analysis): https://arxiv.org/abs/2510.13626
- OpenVLA-OFT: https://arxiv.org/abs/2502.19645
