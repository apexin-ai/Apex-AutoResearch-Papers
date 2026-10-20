# CIVO: Conditioning-Induced Value Overestimation in DreamerV3
## Supplementary Code & Data

### Overview
This repository contains the code, analysis scripts, and data for reproducing the experiments in "Diagnosing and Mitigating Conditioning-Induced Value Overestimation in Model-Based Reinforcement Learning" (CoRL 2026).

### Requirements
```
pip install -r requirements.txt
```

### Key Experiments

#### CIVO Trigger (Walker Walk, trained dt_emb)
```bash
python dreamer.py --configs defaults dmc_proprio \
    --task dmc_walker_walk --steps 210000 --seed 1 \
    --gate_enabled True --gate_fixed_dt 2 \
    --gate_subsample_max_dt 2 --imag_horizon 8 \
    --compile False --checkpoint_every 25000 \
    --logdir logdir/civo_trigger_walker_s1
```

#### Frozen dt_emb Diagnostic (Walker Walk)
```bash
python dreamer.py --configs defaults dmc_proprio \
    --task dmc_walker_walk --steps 210000 --seed 0 \
    --gate_enabled True --gate_fixed_dt 2 \
    --gate_subsample_max_dt 2 --imag_horizon 8 \
    --dt_emb_freeze True --compile False \
    --checkpoint_every 25000 \
    --logdir logdir/frozen_walker_s0
```

#### ManiSkill Manipulation (PegInsertion)
```bash
python dreamer.py --configs maniskill_peginsertion \
    --task maniskill_PegInsertionSide-v1 --steps 210000 --seed 0 \
    --gate_enabled True --gate_fixed_dt 2 \
    --gate_subsample_max_dt 2 --imag_horizon 8 \
    --compile False --checkpoint_every 25000 \
    --logdir logdir/peginsertion_s0
```

### Analysis Scripts
- `scripts/civo_detector.py` — Online CIVO detector (NVE-based)
- `scripts/compute_gradient_decomposition.py` — Gradient pathway decomposition (Figure 5)
- `scripts/nve_threshold_analysis_v3.py` — NVE threshold ROC analysis (AUROC computation)

### Data Files
- `analysis/gradient_decomposition_008d_corrected.json` — Gradient decomposition raw data
- `analysis/baseline_4seed_mean_ve_ratio.csv` — Baseline ve_ratio profiles for NVE normalization
- `analysis/bootstrap_cis.json` — Bootstrap confidence intervals

### Base Code
This codebase is built on [NM512/dreamerv3-torch](https://github.com/NM512/dreamerv3-torch). The `minecraft.sh` script references the upstream [NM512/minerl](https://github.com/NM512/minerl) repository.

### License
MIT License (see LICENSE file)
