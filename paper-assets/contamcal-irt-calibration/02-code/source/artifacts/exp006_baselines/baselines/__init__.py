"""Baseline calibration methods for exp-006."""
from . import (
    dcr_fuzzy,
    emperor_mitigation,
    linear_regression,
    remove_rescore,
    vanilla_4pl,
    single_signal_2pl_gamma,
    raw_scores,
)

ALL_BASELINES = {
    "dcr_fuzzy": dcr_fuzzy.calibrate,
    "emperor_mitigation": emperor_mitigation.calibrate,
    "linear_regression": linear_regression.calibrate,
    "remove_rescore": remove_rescore.calibrate,
    "vanilla_4pl": vanilla_4pl.calibrate,
    "single_signal_2pl_gamma": single_signal_2pl_gamma.calibrate,
    "raw_scores": raw_scores.calibrate,
}
