"""StructFuse MVP main pipeline.
Runs K=3 circuit discovery methods on GPT-2 Small / IOI,
computes CSS and CIRCUS, generates cross-tabulation, evaluates faithfulness.
"""

import json
from pathlib import Path

from config import MVP_CONFIG
from circuit_discovery import run_all_methods
from circus import run_circus
from css import compute_css, threshold_css, binarize_scores, css_summary
from cross_tabulate import cross_tabulate, compute_off_diagonal, print_cross_table
from evaluation import evaluate_all_circuits, print_eval_table


def load_model_and_data(config):
    """Load GPT-2 Small and IOI dataset via TransformerLens."""
    from transformer_lens import HookedTransformer

    print(f"Loading model: {config.model_name}")
    model = HookedTransformer.from_pretrained(config.model_name)

    # TODO: use proper IOI dataset
    # from transformer_lens.evals import IOIDataset
    # dataset = IOIDataset(tokenizer=model.tokenizer, num_samples=config.num_samples)
    dataset = None  # placeholder

    return model, dataset


def logit_diff_metric(logits, tokens):
    """IOI logit difference metric: logit(IO) - logit(S)."""
    # TODO: implement proper IOI metric
    pass


def main():
    config = MVP_CONFIG
    print(f"StructFuse MVP: model={config.model_name}, task={config.task}, K={config.K}")
    print(f"Methods: {config.methods}")
    print()

    # Step 1: Load model + data
    model, dataset = load_model_and_data(config)

    # Step 2: Run K=3 circuit discovery methods
    all_scores = run_all_methods(model, dataset, logit_diff_metric, config)

    # Step 3: Binarize each method's scores to get edge sets
    method_circuits = {}
    for method, scores in all_scores.items():
        method_circuits[method] = binarize_scores(scores, top_n=config.eap_ig_topn)
        print(f"{method}: {len(method_circuits[method])} edges selected")

    # Step 4: CIRCUS config-bagging on EAP-IG
    print("\n--- CIRCUS (EAP-IG) ---")
    eap_stability, circus_tiers = run_circus(all_scores["eap_ig"], config)

    # Step 5: CSS across K=3 methods
    print("\n--- CSS (K=3) ---")
    css_scores = compute_css(method_circuits, K=config.K)
    print(f"CSS distribution: {css_summary(css_scores, config.K)}")

    css_circuit = threshold_css(css_scores, config.css_default_threshold)
    print(f"CSS circuit (>= {config.css_default_threshold}): {len(css_circuit)} edges")

    # Step 6: Cross-tabulation
    print("\n--- Cross-Tabulation ---")
    table = cross_tabulate(circus_tiers, css_scores, config.css_default_threshold)
    print_cross_table(table)

    off_diag = compute_off_diagonal(table)
    print(f"Off-diagonal %: {off_diag*100:.1f}%")

    # Step 7: Evaluate all circuit variants
    print("\n--- Evaluation ---")
    circuits_to_eval = {}

    # Individual method circuits
    for method, edges in method_circuits.items():
        circuits_to_eval[f"method_{method}"] = edges

    # CSS circuits at various thresholds
    for thr in config.css_thresholds:
        if thr > 0:
            css_edges = threshold_css(css_scores, thr)
            circuits_to_eval[f"css_{thr:.2f}"] = css_edges

    # CIRCUS-core circuit
    from circus import get_tier_sets
    tier_sets = get_tier_sets(circus_tiers)
    circuits_to_eval["circus_core"] = tier_sets["core"]

    # Stable-core (CIRCUS-core AND CSS-high)
    circuits_to_eval["stable_core"] = table.stable_core

    eval_results = evaluate_all_circuits(model, circuits_to_eval, dataset, logit_diff_metric)
    print_eval_table(eval_results)

    # Step 8: MVP gate (graduated per ROADMAP D001-D003)
    print("\n" + "=" * 50)
    print("MVP GATE ASSESSMENT")
    print("=" * 50)
    pct = off_diag * 100
    if pct >= 10:
        gate_verdict = "PASS_MAIN"
        gate_msg = f"Off-diagonal {pct:.1f}% >= 10% → Main track, proceed to full experiments"
    elif pct >= 5:
        gate_verdict = "PASS_FINDINGS"
        gate_msg = f"Off-diagonal {pct:.1f}% in [5-10%) → Findings default, add Arithmetic task to confirm"
    elif pct >= 2:
        gate_verdict = "MARGINAL"
        gate_msg = f"Off-diagonal {pct:.1f}% in [2-5%) → Findings track, needs confirmation"
    else:
        gate_verdict = "KILL"
        gate_msg = f"Off-diagonal {pct:.1f}% < 2% → Kill project (if ΔF also not significant)"
    print(f"Off-diagonal %: {pct:.1f}%")
    print(f"Verdict: {gate_verdict}")
    print(f"Action: {gate_msg}")

    # Save results
    output = {
        "config": {
            "model": config.model_name,
            "task": config.task,
            "K": config.K,
            "methods": config.methods,
        },
        "cross_table": table.summary(),
        "off_diagonal_pct": off_diag,
        "css_distribution": css_summary(css_scores, config.K),
        "circus_tier_counts": {
            t: sum(1 for v in circus_tiers.values() if v == t)
            for t in ["core", "contingent", "noise"]
        },
        "evaluation": [r.to_dict() for r in eval_results],
        "gate_verdict": gate_verdict,
    }

    output_path = Path(__file__).parent / "mvp_results.json"
    with open(output_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to {output_path}")


if __name__ == "__main__":
    main()
