"""Circuit faithfulness evaluation.
Measures how well a discovered circuit preserves model behavior (CPR/CMD metrics).
"""

from typing import Dict, Set, List, Any, Optional
from dataclasses import dataclass


@dataclass
class CircuitEvalResult:
    """Evaluation result for a single circuit."""
    name: str
    num_edges: int
    cpr: float  # Circuit Performance Recovery: how much of original performance the circuit retains
    cmd: float  # Circuit Metric Difference: absolute difference from full model

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "num_edges": self.num_edges,
            "cpr": round(self.cpr, 4),
            "cmd": round(self.cmd, 4),
        }


def evaluate_circuit(
    model,
    circuit_edges: Set[str],
    dataset,
    metric,
) -> CircuitEvalResult:
    """Evaluate faithfulness of a circuit.

    Runs the model with only circuit_edges active (ablating everything else)
    and measures how well the circuit preserves the original metric.

    Args:
        model: HookedTransformer instance
        circuit_edges: set of edge names defining the circuit
        dataset: evaluation dataset
        metric: callable returning a scalar metric (e.g. logit difference)

    Returns:
        CircuitEvalResult with CPR and CMD scores
    """
    # TODO: implement ablation-based evaluation
    # 1. Run full model to get baseline metric value
    # baseline = metric(model, dataset)
    #
    # 2. Run model with only circuit_edges active
    #    (zero-ablate or mean-ablate all other edges)
    # circuit_metric = run_with_circuit(model, circuit_edges, dataset, metric)
    #
    # 3. Compute CPR = circuit_metric / baseline
    #    Compute CMD = |baseline - circuit_metric|

    # Placeholder
    return CircuitEvalResult(
        name="",
        num_edges=len(circuit_edges),
        cpr=0.0,
        cmd=0.0,
    )


def evaluate_all_circuits(
    model,
    circuits: Dict[str, Set[str]],
    dataset,
    metric,
) -> List[CircuitEvalResult]:
    """Evaluate multiple circuits for comparison.

    Args:
        model: HookedTransformer instance
        circuits: name -> edge set for each circuit variant
        dataset: evaluation dataset
        metric: callable metric

    Returns:
        List of CircuitEvalResult, one per circuit
    """
    results = []
    for name, edges in circuits.items():
        print(f"Evaluating circuit: {name} ({len(edges)} edges)")
        result = evaluate_circuit(model, edges, dataset, metric)
        result.name = name
        results.append(result)

    return results


def print_eval_table(results: List[CircuitEvalResult]) -> None:
    """Pretty-print evaluation results as a comparison table."""
    print(f"\n{'Circuit':<30} {'Edges':>6} {'CPR':>8} {'CMD':>8}")
    print("-" * 54)
    for r in sorted(results, key=lambda x: x.cpr, reverse=True):
        print(f"{r.name:<30} {r.num_edges:>6} {r.cpr:>8.4f} {r.cmd:>8.4f}")
    print()
