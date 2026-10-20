"""H1/H2/H3 gate evaluator for DemoCalib MVP experiments.

Evaluates whether behavioral calibration prompting (BCP) achieves
three sequential hypothesis gates:
  H1: Uncalibrated LLM user simulators exhibit measurable behavioral bias.
  H2: BCP narrows the gap between simulator and target user behavior.
  H3: BCP does not degrade task completion performance.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class GateResult:
    gate: str
    passed: bool
    detail: dict


@dataclass
class H1Input:
    mean_question_rate: float
    mean_politeness_rate: float
    std_question_rate: float = 0.0
    std_politeness_rate: float = 0.0


@dataclass
class H2Input:
    variant_name: str
    target_question_rate: float
    target_politeness_rate: float
    measured_question_rate: float
    measured_politeness_rate: float


@dataclass
class H3Input:
    variant_name: str
    calibrated_task_completion_rate: float
    baseline_task_completion_rate: float


@dataclass
class EvalReport:
    h1: GateResult
    h2: GateResult
    h3: Optional[GateResult]
    all_passed: bool


class HGateEvaluator:
    """Evaluate H1/H2/H3 gates with configurable thresholds."""

    def __init__(
        self,
        h1_question_rate_threshold: float = 0.15,
        h1_politeness_rate_threshold: float = 0.30,
        h2_relative_improvement_threshold: float = 0.30,
        h3_retention_ratio: float = 0.80,
    ):
        self.h1_question_rate_threshold = h1_question_rate_threshold
        self.h1_politeness_rate_threshold = h1_politeness_rate_threshold
        self.h2_relative_improvement_threshold = h2_relative_improvement_threshold
        self.h3_retention_ratio = h3_retention_ratio

    def evaluate_h1(self, baseline: H1Input) -> GateResult:
        """H1: uncalibrated politeness_rate >= threshold (primary gate).

        question_rate is computed and reported as a secondary metric
        but does not affect pass/fail.
        """
        p_pass = baseline.mean_politeness_rate >= self.h1_politeness_rate_threshold
        return GateResult(
            gate="H1",
            passed=p_pass,
            detail={
                "mean_politeness_rate": baseline.mean_politeness_rate,
                "std_politeness_rate": baseline.std_politeness_rate,
                "politeness_rate_threshold": self.h1_politeness_rate_threshold,
                "politeness_rate_passed": p_pass,
                "secondary_metric": {
                    "mean_question_rate": baseline.mean_question_rate,
                    "std_question_rate": baseline.std_question_rate,
                    "question_rate_threshold": self.h1_question_rate_threshold,
                    "question_rate_above_threshold": baseline.mean_question_rate >= self.h1_question_rate_threshold,
                },
            },
        )

    def evaluate_h2(
        self, baseline: H1Input, variants: list[H2Input]
    ) -> GateResult:
        """H2: at least one BCP variant reduces politeness gap by >= threshold (relative).

        question_rate gap reduction is computed and reported as a secondary
        metric but does not affect pass/fail.
        """
        variant_results = []
        any_passed = False

        for v in variants:
            baseline_q_gap = abs(baseline.mean_question_rate - v.target_question_rate)
            baseline_p_gap = abs(baseline.mean_politeness_rate - v.target_politeness_rate)
            calibrated_q_gap = abs(v.measured_question_rate - v.target_question_rate)
            calibrated_p_gap = abs(v.measured_politeness_rate - v.target_politeness_rate)

            q_improvement = (
                (baseline_q_gap - calibrated_q_gap) / baseline_q_gap
                if baseline_q_gap > 1e-9
                else 0.0
            )
            p_improvement = (
                (baseline_p_gap - calibrated_p_gap) / baseline_p_gap
                if baseline_p_gap > 1e-9
                else 0.0
            )

            p_passed = p_improvement >= self.h2_relative_improvement_threshold
            if p_passed:
                any_passed = True

            variant_results.append({
                "variant": v.variant_name,
                "target_politeness_rate": v.target_politeness_rate,
                "measured_politeness_rate": v.measured_politeness_rate,
                "baseline_politeness_gap": baseline_p_gap,
                "calibrated_politeness_gap": calibrated_p_gap,
                "politeness_improvement_pct": p_improvement,
                "passed": p_passed,
                "secondary_metric": {
                    "target_question_rate": v.target_question_rate,
                    "measured_question_rate": v.measured_question_rate,
                    "baseline_question_gap": baseline_q_gap,
                    "calibrated_question_gap": calibrated_q_gap,
                    "question_improvement_pct": q_improvement,
                },
            })

        return GateResult(
            gate="H2",
            passed=any_passed,
            detail={
                "relative_improvement_threshold": self.h2_relative_improvement_threshold,
                "variants": variant_results,
            },
        )

    def evaluate_h3(self, variants: list[H3Input]) -> GateResult:
        """H3: BCP-calibrated task completion >= retention_ratio * baseline."""
        variant_results = []
        all_retained = True

        for v in variants:
            threshold = self.h3_retention_ratio * v.baseline_task_completion_rate
            retained = v.calibrated_task_completion_rate >= threshold
            if not retained:
                all_retained = False
            variant_results.append({
                "variant": v.variant_name,
                "calibrated_completion": v.calibrated_task_completion_rate,
                "baseline_completion": v.baseline_task_completion_rate,
                "retention_threshold": threshold,
                "retained": retained,
            })

        return GateResult(
            gate="H3",
            passed=all_retained,
            detail={
                "retention_ratio": self.h3_retention_ratio,
                "variants": variant_results,
            },
        )

    def evaluate_all(
        self,
        baseline: H1Input,
        h2_variants: list[H2Input],
        h3_variants: Optional[list[H3Input]] = None,
    ) -> EvalReport:
        """Run all gates sequentially. H3 is optional (requires task completion data)."""
        h1 = self.evaluate_h1(baseline)
        h2 = self.evaluate_h2(baseline, h2_variants)
        h3 = self.evaluate_h3(h3_variants) if h3_variants else None
        all_passed = h1.passed and h2.passed and (h3.passed if h3 else True)
        return EvalReport(h1=h1, h2=h2, h3=h3, all_passed=all_passed)

    def to_dict(self, report: EvalReport) -> dict:
        """Serialize EvalReport to a JSON-compatible dict."""
        result = {
            "h1": {"gate": "H1", "passed": report.h1.passed, "detail": report.h1.detail},
            "h2": {"gate": "H2", "passed": report.h2.passed, "detail": report.h2.detail},
            "all_passed": report.all_passed,
        }
        if report.h3 is not None:
            result["h3"] = {"gate": "H3", "passed": report.h3.passed, "detail": report.h3.detail}
        return result
