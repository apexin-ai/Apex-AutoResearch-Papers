"""Dose-response profile classifier for contamination calibration.

Classifies a model's accuracy trajectory across contamination dosages
into one of five canonical patterns: Immune, U-collapse, V-recovery,
Benefit, or Benefit-saturation.
"""

from __future__ import annotations

DOSAGES = ("d000", "d005", "d025", "d050", "d100")
PATTERNS = ("Immune", "U-collapse", "V-recovery", "Benefit", "Benefit-sat")


def classify_profile(
    accuracies: dict[str, float],
    *,
    noise_threshold: float = 1.0,
    severe_threshold: float = 5.0,
    saturation_ratio: float = 0.3,
    late_gain_floor: float = 0.5,
) -> dict:
    """Classify a dose-response accuracy profile into a canonical pattern.

    Args:
        accuracies: Mapping from dosage key to accuracy (percentage points),
            e.g. {"d000": 76.44, "d005": 76.56, "d025": 76.50,
                   "d050": 76.02, "d100": 76.27}.
        noise_threshold: Maximum |delta| (pp) to be considered noise (Immune).
        severe_threshold: Minimum |delta| (pp) for severe degradation (U-collapse).
        saturation_ratio: If second-half gain < first-half gain * ratio,
            the benefit is saturating.
        late_gain_floor: If d100 - d050 < this value, late gain has stalled.

    Returns:
        {"pattern": str, "confidence": float, "delta": float, "reasoning": str}
    """
    for d in DOSAGES:
        if d not in accuracies:
            raise ValueError(f"Missing dosage key: {d}")

    a = {d: float(accuracies[d]) for d in DOSAGES}
    delta = a["d100"] - a["d000"]
    mid_vals = [a["d005"], a["d025"], a["d050"]]
    mid_min = min(mid_vals)

    # ── Decision tree ────────────────────────────────────────────────

    if abs(delta) <= noise_threshold:
        margin = noise_threshold - abs(delta)
        return _result(
            "Immune", delta, margin, noise_threshold,
            f"|delta|={abs(delta):.2f}pp <= {noise_threshold}pp noise band"
        )

    if delta < -noise_threshold:
        if delta <= -severe_threshold:
            margin = abs(delta) - severe_threshold
            return _result(
                "U-collapse", delta, margin, severe_threshold,
                f"delta={delta:+.2f}pp <= -{severe_threshold}pp (severe monotonic decline)"
            )

        v_dip = mid_min < a["d100"] and mid_min < a["d000"]
        if v_dip:
            recovery = a["d100"] - mid_min
            margin = min(a["d000"] - mid_min, a["d100"] - mid_min)
            return _result(
                "V-recovery", delta, margin, severe_threshold,
                f"delta={delta:+.2f}pp, mid-dosage trough at {mid_min:.2f}% "
                f"with {recovery:+.2f}pp partial recovery"
            )

        margin = abs(delta) - noise_threshold
        return _result(
            "U-collapse", delta, margin, severe_threshold,
            f"delta={delta:+.2f}pp, moderate decline without V-shaped recovery"
        )

    # delta > noise_threshold (positive)
    first_half = a["d025"] - a["d000"]
    second_half = a["d100"] - a["d025"]
    late_gain = a["d100"] - a["d050"]

    saturating = (
        (first_half > 0 and second_half < first_half * saturation_ratio)
        or late_gain < late_gain_floor
    )

    if saturating:
        if late_gain < late_gain_floor:
            margin = late_gain_floor - late_gain
            reason = (f"delta={delta:+.2f}pp (positive), late gain "
                      f"d050->d100={late_gain:+.2f}pp < {late_gain_floor}pp floor")
        else:
            margin = first_half * saturation_ratio - second_half
            reason = (f"delta={delta:+.2f}pp (positive), second-half gain "
                      f"({second_half:.2f}) < {saturation_ratio:.0%} of "
                      f"first-half ({first_half:.2f})")
        return _result("Benefit-sat", delta, margin, noise_threshold, reason)

    margin = delta - noise_threshold
    return _result(
        "Benefit", delta, margin, noise_threshold,
        f"delta={delta:+.2f}pp, monotonic improvement without saturation"
    )


def _result(
    pattern: str, delta: float, margin: float, scale: float, reasoning: str
) -> dict:
    confidence = min(1.0, 0.5 + 0.5 * margin / scale)
    return {
        "pattern": pattern,
        "confidence": round(confidence, 3),
        "delta": round(delta, 4),
        "reasoning": reasoning,
    }


def classify_profiles_batch(
    profiles: dict[str, dict[str, float]], **kwargs
) -> dict[str, dict]:
    """Classify multiple profiles. Keys are model names."""
    return {name: classify_profile(accs, **kwargs) for name, accs in profiles.items()}


# ── CLI validation ───────────────────────────────────────────────────

if __name__ == "__main__":
    test_cases = {
        "Phi-4 (expect Immune)": {
            "accs": {"d000": 76.44, "d005": 76.56, "d025": 76.50,
                     "d050": 76.02, "d100": 76.27},
            "expected": "Immune",
        },
        "Qwen-14B (expect U-collapse)": {
            "accs": {"d000": 69.44, "d005": 68.36, "d025": 64.07,
                     "d050": 59.41, "d100": 60.07},
            "expected": "U-collapse",
        },
        "Qwen-7B (expect V-recovery)": {
            "accs": {"d000": 66.11, "d005": 65.04, "d025": 63.01,
                     "d050": 63.56, "d100": 64.33},
            "expected": "V-recovery",
        },
        "Gemma-2 (expect Benefit)": {
            "accs": {"d000": 61.86, "d005": 62.89, "d025": 63.54,
                     "d050": 64.71, "d100": 65.62},
            "expected": "Benefit",
        },
        "OLMo-2 (expect Benefit-sat)": {
            "accs": {"d000": 53.79, "d005": 55.08, "d025": 56.19,
                     "d050": 57.00, "d100": 57.00},
            "expected": "Benefit-sat",
        },
    }

    all_pass = True
    for name, tc in test_cases.items():
        result = classify_profile(tc["accs"])
        ok = result["pattern"] == tc["expected"]
        mark = "PASS" if ok else "FAIL"
        print(f"[{mark}] {name}")
        print(f"       -> {result['pattern']}  (conf={result['confidence']:.3f})")
        print(f"       {result['reasoning']}")
        if not ok:
            all_pass = False

    print(f"\n{'All tests passed.' if all_pass else 'SOME TESTS FAILED.'}")
