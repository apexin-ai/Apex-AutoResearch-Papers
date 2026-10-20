"""D-study projections for G-theory variance decomposition.

Given the estimated variance components from the G-study, computes the
generalizability coefficient (G) for different measurement designs by
varying the number of replications of each random facet.

Partition rule
--------------
* σ²_τ  (universe score): components involving *only* fixed facets
  (precision, temperature and their interactions).
* σ²_δ  (relative error): components involving ≥1 random facet, each
  divided by the product of the sample sizes of the random facets in
  that component.
* G = σ²_τ / (σ²_τ + σ²_δ)

Input:  ``variance_components.json`` from ``variance_decomposition.py``.
Output: ``d_study_results.json`` — current G, per-facet sweep, minimum
        replications for target G thresholds.
"""

import argparse
import json
from pathlib import Path

FIXED_FACETS = {"precision", "temperature"}
RANDOM_FACETS = ["prompt_template", "seed", "ordering", "item_id"]

MVP_LEVELS = {
    "prompt_template": 3,
    "seed": 3,
    "ordering": 2,
    "item_id": 50,
}


def compute_g_coefficient(
    variance_components: dict,
    random_n: dict[str, int],
) -> tuple[float, float, float]:
    """Compute G for a given D-study design.

    Args:
        variance_components: Keys are component names (e.g. ``"seed"``,
            ``"precision:prompt_template"``), values are dicts with an
            ``"estimate"`` key **or** plain floats.
        random_n: Number of replications for each random facet.

    Returns:
        (G, σ²_τ, σ²_δ).
    """
    sigma_tau = 0.0
    sigma_delta = 0.0

    for component, info in variance_components.items():
        est = info["estimate"] if isinstance(info, dict) else info

        if component == "residual":
            divisor = 1
            for f in RANDOM_FACETS:
                divisor *= random_n.get(f, 1)
            sigma_delta += est / divisor
            continue

        facets_in = component.split(":")
        random_in = [f for f in facets_in if f not in FIXED_FACETS]

        if len(random_in) == 0:
            sigma_tau += est
        else:
            divisor = 1
            for f in random_in:
                divisor *= random_n.get(f, 1)
            sigma_delta += est / divisor

    total = sigma_tau + sigma_delta
    g = sigma_tau / total if total > 0 else 0.0
    return g, sigma_tau, sigma_delta


def find_min_replications(
    vc: dict,
    target_g: float,
    target_facet: str,
    base_levels: dict[str, int],
    max_n: int = 100,
) -> int | None:
    """Binary-search the minimum *n* for ``target_facet`` to reach ``target_g``.

    Other facets stay at ``base_levels``.  Returns ``None`` if not reachable
    within ``max_n``.
    """
    for n in range(1, max_n + 1):
        levels = base_levels.copy()
        levels[target_facet] = n
        g, _, _ = compute_g_coefficient(vc, levels)
        if g >= target_g:
            return n
    return None


def run_d_study(input_path: str, output_path: str) -> dict:
    """Run full D-study analysis.

    Args:
        input_path: Path to ``variance_components.json``.
        output_path: Destination JSON.

    Returns:
        Results dict.
    """
    with open(input_path) as f:
        data = json.load(f)

    vc = data["variance_components"]

    g_current, tau, delta = compute_g_coefficient(vc, MVP_LEVELS)

    # --- per-facet sweeps (1 … 20) ---
    sweeps: dict[str, list[dict]] = {}
    for facet in RANDOM_FACETS:
        sweep = []
        for n in range(1, 21):
            levels = MVP_LEVELS.copy()
            levels[facet] = n
            g, _, _ = compute_g_coefficient(vc, levels)
            sweep.append({"n": n, "g": round(g, 6)})
        sweeps[facet] = sweep

    # --- minimum replications for target thresholds ---
    targets = [0.90, 0.95, 0.99]
    min_reps: dict[str, dict[str, int | None]] = {}
    for target in targets:
        min_reps[str(target)] = {}
        for facet in RANDOM_FACETS:
            min_reps[str(target)][facet] = find_min_replications(
                vc, target, facet, MVP_LEVELS
            )

    results = {
        "current_design": {
            "levels": MVP_LEVELS,
            "g_coefficient": round(g_current, 6),
            "sigma_tau": round(tau, 8),
            "sigma_delta": round(delta, 8),
        },
        "sweeps": sweeps,
        "min_replications": min_reps,
    }

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)

    # --- print summary ---
    print(f"D-study Results  (current G = {g_current:.4f})")
    print(f"\nMinimum replications for target G:")
    print(f"{'Facet':<20} {'G≥0.90':>8} {'G≥0.95':>8} {'G≥0.99':>8}")
    print("-" * 48)
    for facet in RANDOM_FACETS:
        vals = [min_reps[str(t)].get(facet) for t in targets]
        strs = [str(v) if v is not None else ">100" for v in vals]
        print(f"{facet:<20} {strs[0]:>8} {strs[1]:>8} {strs[2]:>8}")

    print(f"\n→ {output_path}")
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="G-theory D-study projections"
    )
    parser.add_argument(
        "--input", required=True, help="Path to variance_components.json"
    )
    parser.add_argument("--output", default="results/d_study_results.json")
    args = parser.parse_args()
    run_d_study(args.input, args.output)
