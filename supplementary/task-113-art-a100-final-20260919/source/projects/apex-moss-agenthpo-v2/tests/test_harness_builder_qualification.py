from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest

from optimization_lab.harness_builder.qualification import (
    DEFAULT_QUALIFICATION_MANIFEST,
    QualificationContractError,
    canonical_qualification_bytes,
    selector_digest,
    verify_benchmark_qualification,
)


def _payload() -> dict[str, object]:
    return json.loads(DEFAULT_QUALIFICATION_MANIFEST.read_text(encoding="utf-8"))


def _write(tmp_path: Path, payload: object, *, canonical: bool = True) -> Path:
    path = tmp_path / "qualification.json"
    if canonical:
        path.write_bytes(canonical_qualification_bytes(payload))
    else:
        path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return path


def _benchmark(payload: dict[str, object], benchmark_id: str) -> dict[str, object]:
    benchmarks = payload["benchmarks"]
    assert isinstance(benchmarks, list)
    return next(
        benchmark
        for benchmark in benchmarks
        if isinstance(benchmark, dict)
        and benchmark["benchmark_id"] == benchmark_id
    )


def test_checked_in_qualification_is_static_blocked_and_cluster_disjoint() -> None:
    payload = verify_benchmark_qualification()
    assert payload["execution_authority"] == "NOT_GRANTED"
    assert not any(payload["execution_entitlement"].values())

    benchmarks = {
        item["benchmark_id"]: item for item in payload["benchmarks"]
    }
    agent = benchmarks["agenthpobench"]
    assert agent["source"]["git_commit"] == (
        "6d8d90071cdb16b06f0db866480ecaae48880fba"
    )
    assert agent["evaluator_mode"] == "no_gold"
    assert agent["capability"]["status"] == "BLOCKED_CAPABILITY"
    assert agent["selection"]["split_sizes"] == {
        "Q_qual": 7,
        "D_bank": 11,
        "T_fresh": 12,
        "T_final": 0,
    }
    assert agent["selection"]["algorithm"] == (
        "category_stratified_sha256_q7_then_lexicographic_v1"
    )
    assert agent["selection"]["category_source"] == {
        "path": "configs/scoring_reference.tsv",
        "sha256": "c17ad42d27aee047611ab824446dae539724d09b61bf9fa945932bfb17201308",
    }
    assert agent["selection"]["splits"]["Q_qual"] == [
        "modernbert_mnli_accuracy",
        "cifar10_airbench94",
        "sparsetsf_ettm1_96_mse",
        "noisygl_cora_uniform30_gcn",
        "art_2048_win_rate",
        "simple_rl_reason_qwen25_05b_math500",
        "vbll_yacht_rmse",
    ]

    gdpevo = benchmarks["gdpevo"]
    assert gdpevo["source"]["git_commit"] == (
        "0999c0d1e6f59b1cb8464cac4e5ed856b5dcb9e4"
    )
    assert gdpevo["evaluator_mode"] == (
        "public_evaluator_gold_model_isolated"
    )
    assert gdpevo["capability"]["status"] == "BLOCKED_CAPABILITY"
    assert gdpevo["selection"]["split_sizes"] == {
        "Q_qual": 6,
        "D_bank": 6,
        "T_fresh": 6,
        "T_final": 6,
    }

    bird = benchmarks["bird-interact"]
    assert bird["source"]["git_commit"] == (
        "451fe2c3518ee1cf908d8139e2913483bd519381"
    )
    assert bird["source"]["dataset_revision"] == (
        "f7881a9c2b9630cc4fc13b0c39279740b0a2fd87"
    )
    assert bird["capability"]["status"] == "BLOCKED_PRIVATE_BUNDLE"
    assert sum(bird["selection"]["split_sizes"].values()) == 0
    assert not any(bird["entitlement"].values())

    for benchmark in benchmarks.values():
        split_members = list(benchmark["selection"]["splits"].values())
        flattened = [member for split in split_members for member in split]
        assert len(flattened) == len(set(flattened))


def test_unknown_field_and_noncanonical_encoding_fail(tmp_path: Path) -> None:
    payload = _payload()
    payload["unexpected"] = True
    with pytest.raises(QualificationContractError, match="schema differs"):
        verify_benchmark_qualification(_write(tmp_path, payload))

    with pytest.raises(QualificationContractError, match="not canonical"):
        verify_benchmark_qualification(
            _write(tmp_path, _payload(), canonical=False)
        )


def test_source_drift_fails_even_when_observed_separately() -> None:
    payload = verify_benchmark_qualification()
    observed = {
        item["benchmark_id"]: {
            "dataset_revision": item["source"]["dataset_revision"],
            "git_commit": item["source"]["git_commit"],
        }
        for item in payload["benchmarks"]
    }
    verify_benchmark_qualification(observed_source_pins=observed)
    observed["gdpevo"]["git_commit"] = "0" * 40
    with pytest.raises(QualificationContractError, match="observed source drifted"):
        verify_benchmark_qualification(observed_source_pins=observed)


@pytest.mark.parametrize("benchmark_id", ["agenthpobench", "gdpevo"])
def test_selector_digest_and_assignment_drift_fail(
    tmp_path: Path, benchmark_id: str
) -> None:
    payload = _payload()
    selection = _benchmark(payload, benchmark_id)["selection"]
    assert isinstance(selection, dict)
    selection["salt"] = str(selection["salt"]) + "-drift"
    selection["selector_digest"] = selector_digest(selection)
    with pytest.raises(QualificationContractError, match="selector salt differs"):
        verify_benchmark_qualification(_write(tmp_path, payload))


def test_cluster_crossing_and_wrong_split_fail(tmp_path: Path) -> None:
    payload = _payload()
    selection = _benchmark(payload, "gdpevo")["selection"]
    assert isinstance(selection, dict)
    splits = selection["splits"]
    assert isinstance(splits, dict)
    splits["D_bank"][0] = splits["Q_qual"][0]
    selection["selector_digest"] = selector_digest(selection)
    with pytest.raises(QualificationContractError, match="cluster crosses"):
        verify_benchmark_qualification(_write(tmp_path, payload))

    payload = _payload()
    selection = _benchmark(payload, "agenthpobench")["selection"]
    assert isinstance(selection, dict)
    splits = selection["splits"]
    assert isinstance(splits, dict)
    splits["Q_qual"][0], splits["D_bank"][0] = (
        splits["D_bank"][0],
        splits["Q_qual"][0],
    )
    selection["selector_digest"] = selector_digest(selection)
    with pytest.raises(QualificationContractError, match="assignment differs"):
        verify_benchmark_qualification(_write(tmp_path, payload))


def test_old_results_and_nonempty_history_are_rejected(tmp_path: Path) -> None:
    with pytest.raises(QualificationContractError, match="prior Moss results"):
        verify_benchmark_qualification(
            prior_result_references=[
                Path("results/optimization_lab/hb-three-arm-live-v1r9")
            ]
        )

    payload = _payload()
    history = payload["history_boundary"]
    assert isinstance(history, dict)
    history["experience_bank_initial_state"] = "IMPORTED_V1R9"
    with pytest.raises(QualificationContractError, match="boundary differs"):
        verify_benchmark_qualification(_write(tmp_path, payload))


def test_blocked_or_zero_entitlement_manifest_cannot_execute(tmp_path: Path) -> None:
    with pytest.raises(QualificationContractError, match="no execution authority"):
        verify_benchmark_qualification(request_execution=True)

    payload = _payload()
    payload["execution_authority"] = "GRANTED"
    with pytest.raises(QualificationContractError, match="execution authority differs"):
        verify_benchmark_qualification(
            _write(tmp_path, payload), request_execution=["gdpevo"]
        )


def test_forged_ready_without_entitlement_fails_before_execution(tmp_path: Path) -> None:
    payload = copy.deepcopy(_payload())
    payload["execution_authority"] = "GRANTED"
    gdpevo = _benchmark(payload, "gdpevo")
    capability = gdpevo["capability"]
    assert isinstance(capability, dict)
    capability.update({"blockers": [], "execution_ready": True, "status": "READY"})
    with pytest.raises(QualificationContractError, match="execution authority differs"):
        verify_benchmark_qualification(
            _write(tmp_path, payload), request_execution=["gdpevo"]
        )
