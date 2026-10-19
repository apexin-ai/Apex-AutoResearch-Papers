# ACIB Perturbation Evaluation Guide

## Files

- `/root/acib/scripts/perturbation_wrapper.py` — visual perturbation implementations + VectorEnv wrapper
- `/root/acib/scripts/eval_acib_perturbed.py` — eval script (drop-in replacement for eval_acib.py with perturbation support)

## Perturbation Types

| Type | Default Strength | Description |
|------|-----------------|-------------|
| `gaussian_noise` | 0.05 | Additive Gaussian noise N(0, sigma^2) on normalized [0,1] images |
| `color_jitter` | 0.3 | Random brightness/contrast/saturation (±strength) + hue shift |
| `spatial_jitter` | 1.0 | Translation ±5px + rotation ±5° (uses cv2 if available) |
| `sensor_noise` | 1.0 | Poisson noise + 0.1% dead pixels (hot/cold) |

## Usage

### Single perturbation eval
```bash
cd /root/acib
python3 scripts/eval_acib_perturbed.py \
    --checkpoint_dir /root/acib/outputs/acib_v5_div_reg \
    --base_model lerobot/smolvla_libero \
    --suites libero_spatial libero_object libero_goal libero_10 \
    --perturbation gaussian_noise \
    --perturbation_strength 0.05 \
    --gpu 0 --n_episodes 50 --seed 42 \
    --out_dir /root/acib/outputs/acib_v5_perturbed_eval/gaussian_noise_0.05
```

### Quick dry-run (1 episode)
```bash
python3 scripts/eval_acib_perturbed.py \
    --checkpoint_dir /root/acib/outputs/acib_v5_div_reg \
    --base_model lerobot/smolvla_libero \
    --suites libero_spatial \
    --n_episodes 1 \
    --perturbation gaussian_noise \
    --perturbation_strength 0.05 \
    --gpu 0 --seed 42 \
    --out_dir /tmp/acib_perturb_dryrun
```

### Full robustness eval matrix
```bash
for pert in gaussian_noise color_jitter spatial_jitter sensor_noise; do
    python3 scripts/eval_acib_perturbed.py \
        --checkpoint_dir /root/acib/outputs/acib_v5_div_reg \
        --base_model lerobot/smolvla_libero \
        --suites libero_spatial libero_object libero_goal libero_10 \
        --perturbation $pert \
        --gpu 0 --n_episodes 50 --seed 42 \
        --out_dir /root/acib/outputs/acib_v5_perturbed_eval/${pert}
done
```

### Baseline comparison (SmolVLA without ACIB)
Use standard `lerobot-eval` with the same perturbation wrapper by importing `PerturbedVectorEnvWrapper` and monkey-patching `make_env` similarly.

## Args

| Arg | Default | Description |
|-----|---------|-------------|
| `--checkpoint_dir` | required | ACIB training output dir |
| `--checkpoint_step` | latest | Specific checkpoint step |
| `--base_model` | `lerobot/smolvla_libero` | Base SmolVLA model |
| `--suites` | all 4 LIBERO suites | Space-separated suite names |
| `--perturbation` | required | One of: gaussian_noise, color_jitter, spatial_jitter, sensor_noise |
| `--perturbation_strength` | type-specific | Override default strength |
| `--gpu` | 0 | GPU index |
| `--n_episodes` | 50 | Episodes per task |
| `--seed` | 42 | Random seed (perturbation + eval) |
| `--out_dir` | required | Output directory for results |

## Output

- `{out_dir}/run_info.json` — run configuration including perturbation params
- `{out_dir}/{suite}/eval_info.json` — per-suite detailed results
- `{out_dir}/summary.json` — aggregated success rates per suite

## Architecture

The perturbation is injected by monkey-patching `make_env` in lerobot's eval pipeline. `PerturbedVectorEnvWrapper` wraps each gymnasium VectorEnv, intercepting `step()` and `reset()` to perturb only the `pixels` sub-dict (uint8 images). State/proprioception observations are passed through unchanged.
