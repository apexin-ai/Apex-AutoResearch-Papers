"""Extract full singular value distributions from Pythia-410M r=0 (pure collapse).

Re-runs Gen 0 (base model) and 2 generations of recursive training to get Gen 2,
then saves complete SV vectors for both.
"""
import sys
import os
sys.path.insert(0, "/root/spectral_collapse_ews")

import json
import torch
import numpy as np
from transformers import AutoModelForCausalLM, AutoTokenizer

from src.config import Config
from src.rankme import compute_effective_rank
from src.generate import generate_synthetic_data
from src.pipeline import create_dataloader, train_one_epoch

from torch.optim import AdamW
from transformers import get_linear_schedule_with_warmup


def extract_full_svd(model, spectral_samples, device, batch_size=32):
    """Same as compute_effective_rank but returns the full SV vector."""
    eff_rank, singular_values, log_det = compute_effective_rank(
        model, spectral_samples, device, batch_size=batch_size
    )
    return {
        "effective_rank": float(eff_rank),
        "log_det": float(log_det),
        "singular_values": singular_values.tolist(),
        "sigma_1": float(singular_values[0]),
        "sigma_min": float(singular_values[-1]) if len(singular_values) > 0 else 0.0,
        "num_sv": len(singular_values),
    }


def main():
    config = Config()
    config.real_data_ratio = 0.0
    config.num_generations = 2  # We only need gen 0, 1, 2

    torch.manual_seed(config.seed)
    torch.cuda.manual_seed_all(config.seed)
    device = torch.device(config.device)

    print("Loading base model...")
    tokenizer = AutoTokenizer.from_pretrained(
        config.model_name, cache_dir=config.model_cache_dir
    )
    model = AutoModelForCausalLM.from_pretrained(
        config.model_name, cache_dir=config.model_cache_dir
    ).to(device)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    print("Loading spectral data (1k samples)...")
    spectral_samples = torch.load(config.spectral_path)[:config.num_spectral_samples]

    results = {}

    # Gen 0: base model SVD
    print("\n=== Gen 0: Base model SVD ===")
    sv_data = extract_full_svd(model, spectral_samples, device)
    results["gen_0"] = sv_data
    print(f"  eff_rank={sv_data['effective_rank']:.2f}, σ₁={sv_data['sigma_1']:.2f}, "
          f"σ_min={sv_data['sigma_min']:.6f}, n_sv={sv_data['num_sv']}")

    # Load real training data
    real_train_data = torch.load(config.train_real_path)

    for gen in range(1, 3):  # Gen 1 and Gen 2
        print(f"\n=== Gen {gen}: Generating synthetic data ===")
        num_synth = config.num_synthetic_samples
        synthetic_data = generate_synthetic_data(
            model, tokenizer,
            num_samples=num_synth,
            max_length=config.max_length,
            temperature=config.temperature,
            top_k=config.top_k,
            device=device,
            batch_size=config.gen_batch_size,
        )
        print(f"  Generated {len(synthetic_data)} synthetic samples")

        train_data = synthetic_data  # r=0, pure synthetic
        print(f"  Training on {len(train_data)} samples...")

        dataloader = create_dataloader(train_data, config.batch_size, shuffle=True)
        num_training_steps = len(dataloader) // config.gradient_accumulation_steps
        num_warmup_steps = int(num_training_steps * config.warmup_ratio)

        optimizer = AdamW(model.parameters(), lr=config.learning_rate, weight_decay=0.01)
        scheduler = get_linear_schedule_with_warmup(optimizer, num_warmup_steps, num_training_steps)

        avg_loss = train_one_epoch(
            model, dataloader, optimizer, scheduler, device, config.gradient_accumulation_steps
        )
        print(f"  Training loss: {avg_loss:.4f}")

        print(f"  Computing full SVD...")
        sv_data = extract_full_svd(model, spectral_samples, device)
        sv_data["train_loss"] = float(avg_loss)
        results[f"gen_{gen}"] = sv_data
        print(f"  eff_rank={sv_data['effective_rank']:.2f}, σ₁={sv_data['sigma_1']:.2f}, "
              f"σ_min={sv_data['sigma_min']:.6f}, n_sv={sv_data['num_sv']}")

    # Save
    out_path = "/root/spectral_collapse_ews/results/sv_distributions.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nFull SV distributions saved to {out_path}")

    # Quick summary
    g0 = results["gen_0"]
    g2 = results["gen_2"]
    print(f"\n=== Summary ===")
    print(f"Gen 0: eff_rank={g0['effective_rank']:.2f}, σ₁={g0['sigma_1']:.2f}, n_sv={g0['num_sv']}")
    print(f"Gen 2: eff_rank={g2['effective_rank']:.2f}, σ₁={g2['sigma_1']:.2f}, n_sv={g2['num_sv']}")
    print(f"σ₁ change: {g0['sigma_1']:.2f} → {g2['sigma_1']:.2f} ({(g2['sigma_1']-g0['sigma_1'])/g0['sigma_1']*100:.1f}%)")
    print(f"eff_rank change: {g0['effective_rank']:.2f} → {g2['effective_rank']:.2f}")


if __name__ == "__main__":
    main()
