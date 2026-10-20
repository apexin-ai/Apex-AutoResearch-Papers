"""Evaluation configuration — default parameters and MVP pass/kill thresholds."""

from dataclasses import dataclass, field
from typing import List


@dataclass
class EvalConfig:
    model_name: str = "meta-llama/Llama-3.1-8B-Instruct"
    template_name: str = "llama3"
    compression_ratios: List[float] = field(default_factory=lambda: [0.7, 0.85])
    beta: float = 0.5
    max_new_tokens: int = 128
    ppl_target_tokens: int = 128
    traces_path: str = "data/synthetic_traces/traces.json"
    output_csv: str = "eval/results.csv"
    output_summary: str = "eval/summary.json"
    device: str = "cuda"


@dataclass
class MVPThresholds:
    """Pass/kill criteria for the MVP evaluation."""
    # Pass: KIRR(TurnKV) - KIRR(Uniform) >= this value (percentage points)
    kirr_diff_pass_pp: float = 10.0
    # Pass: TurnKV KIRR must be at least this value
    kirr_min_pass: float = 0.90
    # Pass: ppl(TurnKV) / ppl(Uniform) must be at most this value
    ppl_ratio_max: float = 1.02
    # Kill: KIRR diff below this at ALL compression ratios
    kirr_diff_kill_pp: float = 5.0
