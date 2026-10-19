#!/usr/bin/env python3
from __future__ import annotations
import math
import os
import random
from typing import Any

LOWER_HINTS = ("loss", "mse", "rmse", "mae", "fid", "wql", "wape", "error", "nll")


def _choices(spec: Any) -> list[Any]:
    if isinstance(spec, dict) and "choices" in spec:
        return list(spec.get("choices") or [])
    if isinstance(spec, (list, tuple)):
        return list(spec)
    return []


def normalize_search_space(search_space: dict[str, Any]) -> dict[str, list[Any]]:
    return {str(k): _choices(v) for k, v in (search_space or {}).items() if _choices(v)}


def _isnum(x: Any) -> bool:
    return isinstance(x, (int, float)) and not isinstance(x, bool) and math.isfinite(float(x))


def infer_direction(task_name: str, training_log: str | None = None) -> str:
    text = " ".join([str(task_name or ""), str(training_log or "")]).lower()
    if "lower is better" in text or "lower_is_better" in text:
        return "lower"
    if "higher is better" in text or "higher_is_better" in text:
        return "higher"
    return "lower" if any(h in text for h in LOWER_HINTS) else "higher"


def metric_from_dict(metrics: dict[str, Any], task_name: str = "", direction: str = "higher") -> float | None:
    if not isinstance(metrics, dict):
        return None
    preferred = [
        "validation_accuracy", "accuracy_percent", "test_accuracy_percent",
        "math500_accuracy_percent", "reasoning_accuracy_percent",
        "validation_scaled_sequence_accuracy", "scaled_accuracy", "test_auc",
        "roc_auc", "f1_fake", "success_rate", "win_rate", "expected_reward",
        "score", "val_loss", "fineweb10B_validation_loss", "MSE[0.5]",
        "test_mse", "mse", "test_rmse", "rmse", "wape", "wql", "WQL",
        "weighted_quantile_loss", "subset_diag_fid", "subset_fid", "mae",
        "test_mae",
    ]
    lt = str(task_name).lower()
    if "llm_c" in lt:
        preferred = ["val_loss", *preferred]
    if "uni2ts" in lt:
        preferred = ["MSE[0.5]", *preferred]
    if "timesfm" in lt:
        preferred = ["wape", *preferred]
    if "chronos" in lt:
        preferred = ["wql", "WQL", *preferred]
    if "var_" in lt:
        preferred = ["subset_diag_fid", "subset_fid", *preferred]
    for key in preferred:
        if _isnum(metrics.get(key)):
            return float(metrics[key])
    numeric = [(k, float(v)) for k, v in metrics.items() if _isnum(v)]
    for k, v in numeric:
        lk = str(k).lower()
        if not lk.startswith("num_") and "seconds" not in lk and "time" not in lk:
            return v
    return numeric[0][1] if numeric else None


def _extract_observations(history: Any, task_name: str, direction: str) -> list[dict[str, Any]]:
    obs = []
    if not isinstance(history, list):
        return obs
    for item in history:
        config = None
        value = None
        if isinstance(item, dict):
            config = item.get("config") or item.get("final_config") or item.get("agent_final_config")
            value = float(item["value"]) if _isnum(item.get("value")) else None
            if value is None:
                value = metric_from_dict(item.get("metrics") or item.get("final_metrics") or item, task_name, direction)
        elif isinstance(item, (list, tuple)):
            if len(item) >= 4:
                metric_obj = item[1]
                config = item[2] if isinstance(item[2], dict) else None
                value = metric_from_dict(metric_obj, task_name, direction) if isinstance(metric_obj, dict) else (float(metric_obj) if _isnum(metric_obj) else None)
            elif len(item) >= 2 and isinstance(item[1], dict):
                value = metric_from_dict(item[1], task_name, direction)
        if isinstance(config, dict) and value is not None and math.isfinite(value):
            obs.append({"config": config, "value": float(value)})
    return obs


def _rank_observations(obs: list[dict[str, Any]], direction: str) -> list[dict[str, Any]]:
    return sorted(obs, key=lambda o: float(o["value"]) if direction == "higher" else -float(o["value"]), reverse=True)


def _density_choice(key: str, values: list[Any], good: list[dict[str, Any]], bad: list[dict[str, Any]], rng: random.Random) -> Any:
    alpha = float(os.environ.get("AUTOREP_BOHB_ALPHA", "1.0"))
    weights = []
    for choice in values:
        g = alpha + sum(1 for item in good if item["config"].get(key) == choice)
        b = alpha + sum(1 for item in bad if item["config"].get(key) == choice)
        weights.append(max(1e-9, g / b))
    threshold = rng.random() * sum(weights)
    acc = 0.0
    selected = values[-1]
    for choice, weight in zip(values, weights):
        acc += weight
        if acc >= threshold:
            selected = choice
            break
    return selected


def propose_tpe_config(
    *,
    task_name: str,
    current_config: dict[str, Any] | None,
    search_space: dict[str, Any],
    history: Any = None,
    training_log: str | None = None,
    direction: str | None = None,
    seed: str | int = "0",
    decision_number: int = 0,
    gamma: float | None = None,
    explore_prob: float | None = None,
) -> dict[str, Any]:
    """Fixed-budget BOHB-style policy with the same call signature as TPE.

    The benchmark gives each intervention the same task-specific budget, so this
    policy cannot allocate true multi-fidelity resources. Instead it mimics BOHB
    behavior under the fixed budget: early trials explore randomly; later trials
    promote configurations from the best observed rung and mutate them with a
    TPE-style good/bad density ratio.
    """
    space = normalize_search_space(search_space)
    current = dict(current_config or {})
    if not space:
        return current
    direction = direction or infer_direction(task_name, training_log=training_log)
    rng = random.Random(f"{seed}:{task_name}:{decision_number}:bohb")
    obs = _extract_observations(history, task_name, direction)
    explore_steps = int(os.environ.get("AUTOREP_BOHB_EXPLORE_STEPS", "2"))
    if len(obs) < explore_steps:
        return {k: rng.choice(v) for k, v in space.items() if v}

    ranked = _rank_observations(obs, direction)
    eta = max(2, int(os.environ.get("AUTOREP_BOHB_ETA", "3")))
    n_good = max(1, math.ceil(len(ranked) / eta))
    good = ranked[:n_good]
    bad = ranked[n_good:] or ranked[:]
    mutation_prob = float(os.environ.get("AUTOREP_BOHB_MUTATION_PROB", str(explore_prob if explore_prob is not None else 0.35)))
    density_prob = float(os.environ.get("AUTOREP_BOHB_DENSITY_PROB", "0.50"))

    # Successive-halving style promotion: choose one of the best observed configs,
    # with a mild rank bias, then mutate selected dimensions.
    parent_weights = [1.0 / (rank + 1) for rank in range(len(good))]
    parent = rng.choices(good, weights=parent_weights, k=1)[0]["config"] if good else current
    proposal = {}
    for key, values in space.items():
        parent_value = parent.get(key, current.get(key))
        keep_parent = parent_value in values and rng.random() >= mutation_prob
        if keep_parent:
            proposal[key] = parent_value
        elif rng.random() < density_prob:
            proposal[key] = _density_choice(key, values, good, bad, rng)
        else:
            proposal[key] = rng.choice(values)
    return proposal


def _pick_current(local_vars: dict[str, Any], global_vars: dict[str, Any]) -> dict[str, Any]:
    for name in ("current_config", "current", "config", "BASE_CONFIG"):
        val = local_vars.get(name, global_vars.get(name))
        if isinstance(val, dict):
            return dict(val)
    return {}


def tpe_decision_from_call(task_name: str, local_vars: dict[str, Any], global_vars: dict[str, Any]) -> dict[str, Any]:
    seed = os.environ.get("AUTOREP_RANDOM_SEED", os.environ.get("AUTOREP_TPE_SEED", "0"))
    decision_number = int(local_vars.get("decision_number", local_vars.get("trial_idx", len(local_vars.get("history", []) or []))))
    search_space = global_vars.get("SEARCH_SPACE") or local_vars.get("search_space") or local_vars.get("SEARCH_SPACE") or {}
    current = _pick_current(local_vars, global_vars)
    history = local_vars.get("history") or local_vars.get("metrics_history") or []
    training_log = ""
    for name in ("training_log", "format_training_log"):
        fn = global_vars.get(name)
        if callable(fn):
            try:
                training_log = fn(history, current)
            except Exception:
                try:
                    training_log = fn(history, local_vars.get("baseline", 0.0))
                except Exception:
                    training_log = ""
            break
    raw = propose_tpe_config(
        task_name=task_name,
        current_config=current,
        search_space=search_space,
        history=history,
        training_log=training_log,
        seed=seed,
        decision_number=decision_number,
    )
    clamp = global_vars.get("clamp_config")
    merged = {**current, **raw}
    if callable(clamp):
        try:
            new_config = clamp(merged)
        except Exception:
            try:
                new_config = clamp(raw)
            except Exception:
                new_config = merged
    else:
        new_config = merged
    return {
        "new_config": new_config,
        "raw_new_config": raw,
        "reasoning": "BOHB-style fixed-budget baseline promoted strong observed configurations and mutated them within the allowed discrete intervention space.",
        "confidence": 0.0,
        "raw_response": "BOHB-style fixed-budget baseline selected a configuration from the allowed discrete intervention space.",
        "metadata": {
            "backend": "bohb_style_fixed_budget",
            "seed": str(seed),
            "decision_number": decision_number,
            "search_space_keys": sorted(normalize_search_space(search_space)),
            "history_size": len(_extract_observations(history, task_name, infer_direction(task_name, training_log=training_log))),
            "eta": int(os.environ.get("AUTOREP_BOHB_ETA", "3")),
            "explore_steps": int(os.environ.get("AUTOREP_BOHB_EXPLORE_STEPS", "2")),
        },
    }
