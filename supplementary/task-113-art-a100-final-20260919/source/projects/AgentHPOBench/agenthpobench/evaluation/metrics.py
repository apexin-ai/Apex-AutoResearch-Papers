from __future__ import annotations

import math
from typing import Any


METRIC_ALIASES = {
    "llm_c_fineweb10b": ["val_loss", "fineweb10B_validation_loss"],
    "torch_conv_kan_cifar10": ["accuracy_percent", "accuracy"],
    "open_r1_math500": ["accuracy_percent", "math500_accuracy_percent"],
    "agent_lightning_room_selector": ["accuracy", "validation_accuracy"],
    "uni2ts_lsf_etth1": ["MSE[0.5]", "mse", "MSE"],
    "timesfm_etth1_long_horizon": ["wape", "WAPE"],
    "modernbert_mnli_accuracy": ["accuracy_percent", "validation_accuracy"],
    "cifar10_airbench94": ["accuracy_percent", "test_accuracy", "accuracy"],
    "noisygl_cora_uniform30_gcn": ["accuracy_percent", "test_accuracy", "accuracy"],
    "tabmini_molecular_biology_promoters_auc": ["auc", "test_auc", "roc_auc"],
    "binary_diffusion_adult_rf": [
        "test_accuracy_percent",
        "rf_accuracy_percent",
        "accuracy_percent",
        "accuracy",
    ],
    "xlstm_parity": ["scaled_accuracy", "validation_scaled_sequence_accuracy", "accuracy"],
    "vbll_yacht_rmse": ["test_rmse", "rmse"],
    "tabm_california_rmse": ["test_rmse", "rmse"],
    "timexer_pjm_168_24_mse": ["test_mse", "mse"],
    "ablkit_hwf_reasoning_accuracy": [
        "reasoning_accuracy_percent",
        "accuracy_percent",
        "accuracy",
    ],
    "tunedgnn_cora_gcn_accuracy": [
        "test_accuracy_percent_at_best_val",
        "accuracy_percent",
        "accuracy",
    ],
    "verl_grpo_gsm8k": ["accuracy_percent", "gsm8k_accuracy_percent", "accuracy"],
    "forest_diffusion_iris_f1fake": ["f1_fake", "F1_fake", "score"],
    "var_imagenet256": ["subset_diag_fid", "subset_fid", "fid"],
    "align_anything_ragen_bandit": ["success_rate", "score"],
    "chronos_t5_tiny_monash_weather_wql": ["WQL", "wql", "mean_wql"],
    "hyperboliccv_cifar100_accuracy": [
        "test_accuracy_percent",
        "accuracy_percent",
        "accuracy",
    ],
    "itransformer_ettm2_96_mse": ["test_mse", "mse"],
    "timemixer_ettm2_96_mse": ["test_mse", "mse"],
    "art_2048_win_rate": ["win_rate", "score"],
    "open_r1_multimodal_mathvista_accuracy": ["accuracy_percent", "accuracy"],
    "rankup_utkface_mae": ["MAE", "mae", "test_mae"],
    "sparsetsf_ettm1_96_mse": ["test_mse_at_best_val", "test_mse", "mse"],
    "simple_rl_reason_qwen25_05b_math500": [
        "math500_accuracy_percent",
        "accuracy_percent",
        "accuracy",
    ],
}

_FRACTIONAL_ACCURACY_TASKS = {
    "agent_lightning_room_selector",
    "xlstm_parity",
    "forest_diffusion_iris_f1fake",
    "align_anything_ragen_bandit",
}
_METRIC_CONTAINERS = (
    "metrics",
    "final_metrics",
    "baseline_metrics",
    "score",
    "agent_val",
)


def finite_number(value: Any) -> float | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)) and math.isfinite(float(value)):
        return float(value)
    return None


def metric_value(task: str, obj: Any) -> tuple[float | None, str | None]:
    """Return the task's declared target metric from a result fragment."""
    if task not in METRIC_ALIASES:
        raise KeyError(f"unknown task metric definition: {task}")
    if not isinstance(obj, dict):
        return None, None
    for key in METRIC_ALIASES[task]:
        value = finite_number(obj.get(key))
        if value is None:
            continue
        if (
            key in {"accuracy", "test_accuracy"}
            and abs(value) <= 1.0
            and task not in _FRACTIONAL_ACCURACY_TASKS
        ):
            value *= 100.0
        return value, key
    for key in _METRIC_CONTAINERS:
        value, metric = metric_value(task, obj.get(key))
        if value is not None:
            return value, metric
    return None, None
