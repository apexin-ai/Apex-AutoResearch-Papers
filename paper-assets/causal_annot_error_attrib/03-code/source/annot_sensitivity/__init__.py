"""annot_sensitivity: Annotation-error sensitivity analysis for causal inference.

Computes how LLM annotation misclassification propagates bias through
7 DAG topologies, with ASV sensitivity measures and 5 correction methods.
"""

from .bias import compute_bias, clear_cache
from .asv import compute_asv
from .correction import (
    recommend_correction,
    correct_naive_plugin,
    correct_dsl,
    correct_ppi,
    correct_mcsimex,
    correct_mla,
    METHODS,
)
from .confusion import (
    validate_confusion_matrix,
    random_confusion_matrix,
    interpolate_confusion,
    predefined_matrices,
    delta_range,
)
from .dgp import generate_data, TOPOLOGIES, DEFAULT_PARAMS, GEN_FUNCS
from .utils import ols, ols_with_se, make_dummies, softmax_sample, misclassify

__all__ = [
    "compute_bias",
    "compute_asv",
    "recommend_correction",
    "correct_naive_plugin",
    "correct_dsl",
    "correct_ppi",
    "correct_mcsimex",
    "correct_mla",
    "validate_confusion_matrix",
    "random_confusion_matrix",
    "interpolate_confusion",
    "predefined_matrices",
    "delta_range",
    "generate_data",
    "clear_cache",
    "TOPOLOGIES",
    "DEFAULT_PARAMS",
    "METHODS",
    "GEN_FUNCS",
    "ols",
    "ols_with_se",
    "make_dummies",
    "softmax_sample",
    "misclassify",
]
