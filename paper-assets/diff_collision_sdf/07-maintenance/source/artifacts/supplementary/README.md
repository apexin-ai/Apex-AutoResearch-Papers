# Supplementary Material: ColliForce-VLA

Differentiable collision-aware action generation for Vision-Language-Action models via learned workspace Signed Distance Fields (SDF). This supplementary package provides code for reproducing the main experiments and figures reported in the paper.

## Dependencies

- Python >= 3.10
- PyTorch >= 2.1 (with CUDA support)
- transformers >= 4.40
- numpy, scipy, matplotlib
- [openpi](https://github.com/Physical-Intelligence/openpi) (base VLA training framework)
- MuJoCo >= 3.0
- robosuite >= 1.4
- LIBERO (task suite)
- SafeLIBERO (collision-annotated variant; see below)

Install core dependencies:
```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
pip install transformers accelerate einops scipy matplotlib
```

## Dataset

**SafeLIBERO**: A collision-annotated extension of the LIBERO benchmark for evaluating manipulation safety. SafeLIBERO adds per-timestep collision detection (obstacle displacement tracking) across two task suites:
- `safelibero_spatial` — spatial reasoning tasks with environmental obstacles
- `safelibero_object` — object manipulation tasks with nearby obstacles

SafeLIBERO is built on top of LIBERO and uses the same demonstration datasets. The collision detection layer monitors obstacle body displacements in the MuJoCo simulator at each control step.

**SDF Ground Truth**: Per-scene `.npz` files containing precomputed signed distance fields:
- `query_points`: [N, 3] xyz coordinates in workspace frame
- `sdf_values`: [N] signed distance values (negative = inside obstacle)
- Generated using `pysdf` from scene mesh geometry

## Code Structure

```
code/
├── src/                        # Core ColliForce modules
│   ├── sdf_decoder.py          # SDF MLP decoder (predicts SDF from action features)
│   ├── sdf_gradient_refiner.py # SDF gradient-guided action refinement
│   ├── sdf_data.py             # SDF ground-truth data loading
│   └── train_colliforce.py     # Full ColliForce training pipeline
│
├── training/                   # Training entry points
│   ├── train_a1_hook.py        # A1: pi0 + SDF auxiliary training (hook-based)
│   ├── train_a1_sdf_aux_pi05.py# A1: pi0.5 + SDF auxiliary training
│   ├── train_pi05_lora_baseline.py # LoRA-only baseline (no SDF, control experiment)
│   └── train_baseline.py       # Full fine-tuning baseline
│
├── eval/                       # Evaluation scripts
│   ├── eval_safelibero.py      # SafeLIBERO evaluation (pi0 checkpoints)
│   ├── eval_pi05_safelibero.py # SafeLIBERO evaluation (pi0.5, websocket client)
│   └── eval_openvla_safelibero.py # OpenVLA zero-shot evaluation
│
├── analysis/                   # Statistical analysis
│   ├── analyze_displacement.py # Displacement-filtered CAR (dfCAR) computation
│   ├── analyze_d012_results.py # Cross-seed result aggregation
│   └── permutation_test.py     # Exact permutation test for significance
│
└── figures/                    # Figure generation
    ├── fig1_teaser_v2.py       # Fig 1: Teaser diagram
    ├── plot_fig2.py            # Fig 2: EE displacement distribution
    ├── plot_fig3_combined.py   # Fig 3: CAR inflation scatter + oracle bar chart
    ├── plot_fig5_combined.py   # Fig 5: lambda-CAR/TSR curve + per-task fingerprint
    ├── plot_threshold_sensitivity.py # Appendix: delta vs dfCAR sensitivity
    ├── gen_fig_displacement_hist.py  # Displacement histogram
    ├── gen_scatter.py          # TSR-CAR scatter plot
    └── threshold_sensitivity_v2.csv  # Data for threshold sensitivity figure
```

## Reproducing Experiments

### 1. Training

**LoRA-only baseline** (Table 1, "LoRA-only"):
```bash
python code/training/train_pi05_lora_baseline.py \
    --scene spatial_bowl --seed 0 --gpu 0
```

**ColliForce (SDF auxiliary)** (Table 1, "ColliForce"):
```bash
python code/training/train_a1_sdf_aux_pi05.py \
    --scene spatial_bowl --seed 0 --gpu 0 --lambda_sdf 0.1
```

Key hyperparameters:
- Learning rate: 2.5e-5 (Phase 2, LoRA unfrozen)
- LoRA rank: 32, alpha: 32 (action expert); 16, alpha: 16 (PaliGemma vision encoder)
- SDF loss weight (lambda_sdf): 0.1 (best), ablated over {0.005, 0.01, 0.1}
- Training steps: 30,000 (Phase 1: 3,000 warmup, Phase 2: 27,000)
- Batch size: 32

### 2. Evaluation

Evaluation requires a running policy server (via openpi's `serve_policy.py`):

```bash
# Start policy server
python -m openpi.serve_policy --checkpoint ./checkpoints/<run_name>

# Run SafeLIBERO evaluation
python code/eval/eval_pi05_safelibero.py \
    --suite safelibero_spatial \
    --safety_level II \
    --task_id 0 \
    --n_episodes 50
```

Metrics reported:
- **CAR** (Collision Avoidance Rate): fraction of episodes with zero obstacle displacement > threshold
- **dfCAR** (displacement-filtered CAR): CAR excluding frozen/collapsed episodes (EE displacement < 5mm)
- **TSR** (Task Success Rate): fraction of episodes reaching the goal

### 3. Figure Reproduction

All figure scripts are self-contained with embedded data (no external data files needed, except `threshold_sensitivity_v2.csv` which is included):

```bash
cd code/figures/
python fig1_teaser_v2.py        # -> Fig 1
python plot_fig2.py             # -> Fig 2
python plot_fig3_combined.py    # -> Fig 3
python plot_fig5_combined.py    # -> Fig 5
python plot_threshold_sensitivity.py  # -> Appendix threshold sensitivity
```

## Notes

- The paper appendix is included in the main submission PDF (not a separate file).
- This is an anonymous submission. No author-identifying information is included.
- Model weights and training data are not included due to size constraints.
