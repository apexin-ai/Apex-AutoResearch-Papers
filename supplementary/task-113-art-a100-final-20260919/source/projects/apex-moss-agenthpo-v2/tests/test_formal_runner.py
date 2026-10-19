"""Offline tests for the formal hidden-evaluation queue runner."""

import importlib.util
import json
import sys
import threading
import time
from pathlib import Path

import pytest


def _runner():
    path = Path(__file__).resolve().parent.parent / "scripts/formal_runner.py"
    spec = importlib.util.spec_from_file_location("formal_runner", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _valid_summary(tokens=100):
    return {
        "pass_rate_mean": 0.5,
        "total_tokens": tokens,
        "tampered_runs": 0,
        "contract_violations": 0,
        "n_infra_invalid": 0,
        "category_counts": {"passed": 1, "capability": 1},
    }


def test_smoke_can_limit_probe_to_models_used_by_the_experiment(monkeypatch):
    runner = _runner()
    seen = []
    client_options = {}

    class Messages:
        def create(self, *, model, max_tokens, messages):
            seen.append(model)
            return type("Response", (), {
                "content": [type("Block", (), {"text": "ok"})()],
            })()

    client = type("Client", (), {"messages": Messages()})()
    monkeypatch.setattr(runner.config, "load_env", lambda: None)

    def fake_client(**kwargs):
        client_options.update(kwargs)
        return client

    monkeypatch.setattr(runner.anthropic, "Anthropic", fake_client)

    runner.smoke(("executor-only",))

    assert seen == ["executor-only"]
    assert client_options == {"timeout": 60.0, "max_retries": 0}


def test_queue_runs_cells_in_order_and_records_ledger(tmp_path):
    runner = _runner()
    (tmp_path / "h1.py").write_text("# frozen")
    (tmp_path / "h2.py").write_text("# frozen")
    cells = [
        runner.Cell("one", "h1.py", "demo", "train", "one", 100),
        runner.Cell("two", "h2.py", "demo", "val", "two", 100),
    ]
    seen = []

    def fake_evaluate(harness, benchmark, repeats, concurrency, out_dir):
        seen.append((Path(harness).name, Path(benchmark).name, repeats, concurrency))
        summary = _valid_summary()
        out = Path(out_dir)
        out.mkdir(parents=True, exist_ok=True)
        (out / "summary.json").write_text(json.dumps(summary))
        return summary

    runner.run_queue(
        cells, root=tmp_path, budget_tokens=1_000,
        evaluate_fn=fake_evaluate, run_canary_fn=lambda cell: None,
    )

    assert seen == [("h1.py", "train", 3, 4), ("h2.py", "val", 3, 4)]
    lines = (tmp_path / "results/official/_ledger.jsonl").read_text().splitlines()
    assert [json.loads(line)["cell"] for line in lines] == ["one", "two"]


def test_infra_invalid_cell_is_isolated_and_pauses_queue(tmp_path):
    runner = _runner()
    (tmp_path / "h.py").write_text("# frozen")
    cell = runner.Cell("broken", "h.py", "demo", "train", "broken", 100)

    def fake_evaluate(harness, benchmark, repeats, concurrency, out_dir):
        summary = _valid_summary()
        summary["n_infra_invalid"] = 3
        summary["category_counts"] = {"env_error": 3}
        out = Path(out_dir)
        out.mkdir(parents=True, exist_ok=True)
        (out / "summary.json").write_text(json.dumps(summary))
        return summary

    with pytest.raises(runner.QueuePaused, match="broken"):
        runner.run_queue(
            [cell], root=tmp_path, budget_tokens=1_000,
            evaluate_fn=fake_evaluate, run_canary_fn=lambda cell: None,
        )

    review = tmp_path / "results/invalid/formal-broken/review.json"
    assert review.exists()
    assert json.loads(review.read_text())["classification"] == "infra_invalid"


def test_repeated_invalid_cells_get_separate_audit_directories(tmp_path):
    runner = _runner()
    (tmp_path / "h.py").write_text("# frozen")
    cell = runner.Cell("repeat", "h.py", "demo", "train", "repeat", 100)

    def fake_evaluate(harness, benchmark, repeats, concurrency, out_dir):
        summary = _valid_summary()
        summary["n_infra_invalid"] = 1
        out = Path(out_dir)
        out.mkdir(parents=True, exist_ok=True)
        (out / "summary.json").write_text(json.dumps(summary))
        return summary

    for _ in range(2):
        with pytest.raises(runner.QueuePaused):
            runner.run_queue([cell], root=tmp_path, budget_tokens=1_000,
                             evaluate_fn=fake_evaluate, run_canary_fn=lambda cell: None)

    assert (tmp_path / "results/invalid/formal-repeat/review.json").exists()
    second = tmp_path / "results/invalid/formal-repeat-attempt2/review.json"
    assert json.loads(second.read_text())["attempt"] == 2


def test_controlled_parallel_runs_one_cell_per_lane(tmp_path):
    runner = _runner()
    lanes = {
        "q1": [
            runner.Cell("q1-a", "q1.py", "demo", "train", "q1-a", 100),
            runner.Cell("q1-b", "q1.py", "demo", "val", "q1-b", 100),
        ],
        "q2": [
            runner.Cell("q2-a", "q2.py", "demo", "train", "q2-a", 100),
            runner.Cell("q2-b", "q2.py", "demo", "val", "q2-b", 100),
        ],
        "q3": [
            runner.Cell("q3-a", "q3.py", "demo", "train", "q3-a", 100),
            runner.Cell("q3-b", "q3.py", "demo", "val", "q3-b", 100),
        ],
    }
    for name in ("q1.py", "q2.py", "q3.py"):
        (tmp_path / name).write_text("# frozen")

    lock = threading.Lock()
    active = set()
    max_active = 0
    seen = []

    def fake_evaluate(harness, benchmark, repeats, concurrency, out_dir):
        nonlocal max_active
        lane = Path(harness).stem
        with lock:
            assert lane not in active
            active.add(lane)
            max_active = max(max_active, len(active))
            seen.append(Path(out_dir).name)
        time.sleep(0.02)
        summary = _valid_summary()
        out = Path(out_dir)
        out.mkdir(parents=True, exist_ok=True)
        (out / "summary.json").write_text(json.dumps(summary))
        with lock:
            active.remove(lane)
        return summary

    runner.run_parallel(
        lanes, root=tmp_path, budget_tokens=10_000,
        evaluate_fn=fake_evaluate, run_canary_fn=lambda cell: None,
        stagger_seconds=0, ledger_filename="_custom_ledger.jsonl",
        state_filename="_custom_state.json",
    )

    assert max_active == 3
    assert seen.index("q1-a") < seen.index("q1-b")
    assert seen.index("q2-a") < seen.index("q2-b")
    assert seen.index("q3-a") < seen.index("q3-b")
    state = json.loads(
        (tmp_path / "results" / "official" / "_custom_state.json").read_text()
    )
    assert state["status"] == "complete"
    assert (tmp_path / "results" / "official" / "_custom_ledger.jsonl").exists()
    assert not (tmp_path / "results" / "official" / "_ledger.jsonl").exists()


def test_controlled_parallel_counts_new_canary_tokens_in_budget(tmp_path):
    runner = _runner()
    (tmp_path / "h.py").write_text("# frozen")
    cell = runner.Cell(
        "with-canary", "h.py", "demo", "val", "with-canary", 100, True
    )

    def fake_evaluate(harness, benchmark, repeats, concurrency, out_dir):
        summary = _valid_summary(tokens=100)
        out = Path(out_dir)
        out.mkdir(parents=True, exist_ok=True)
        (out / "summary.json").write_text(json.dumps(summary))
        return summary

    runner.run_parallel(
        {"only": [cell]},
        root=tmp_path,
        budget_tokens=1_000,
        evaluate_fn=fake_evaluate,
        run_canary_fn=lambda candidate: 25,
        stagger_seconds=0,
        ledger_filename="_canary_ledger.jsonl",
        state_filename="_canary_state.json",
    )

    ledger = [
        json.loads(line)
        for line in (
            tmp_path / "results/official/_canary_ledger.jsonl"
        ).read_text().splitlines()
    ]
    assert [(entry["status"], entry["tokens"]) for entry in ledger] == [
        ("canary", 25),
        ("valid", 100),
    ]
    state = json.loads(
        (tmp_path / "results/official/_canary_state.json").read_text()
    )
    assert state["spent"] == 125


def test_budget_pause_state_names_the_blocked_cell(tmp_path):
    runner = _runner()
    (tmp_path / "h.py").write_text("# frozen")
    cells = [
        runner.Cell("first", "h.py", "demo", "train", "first", 100),
        runner.Cell("blocked", "h.py", "demo", "val", "blocked", 100),
    ]

    def fake_evaluate(harness, benchmark, repeats, concurrency, out_dir):
        summary = _valid_summary(tokens=260)
        out = Path(out_dir)
        out.mkdir(parents=True, exist_ok=True)
        (out / "summary.json").write_text(json.dumps(summary))
        return summary

    with pytest.raises(runner.QueuePaused, match="blocked"):
        runner.run_parallel(
            {"only": cells},
            root=tmp_path,
            budget_tokens=400,
            evaluate_fn=fake_evaluate,
            run_canary_fn=lambda candidate: 0,
            stagger_seconds=0,
            state_filename="_budget_state.json",
        )

    state = json.loads(
        (tmp_path / "results/official/_budget_state.json").read_text()
    )
    assert state["lanes"]["only"] == {
        "status": "paused",
        "cell": "blocked",
    }


def test_quota_fuse_stops_new_cells_in_all_lanes(tmp_path):
    runner = _runner()
    lanes = {
        "q1": [
            runner.Cell("q1-bad", "q1.py", "demo", "train", "q1-bad", 100),
            runner.Cell("q1-never", "q1.py", "demo", "val", "q1-never", 100),
        ],
        "q2": [
            runner.Cell("q2-first", "q2.py", "demo", "train", "q2-first", 100),
            runner.Cell("q2-never", "q2.py", "demo", "val", "q2-never", 100),
        ],
    }
    for name in ("q1.py", "q2.py"):
        (tmp_path / name).write_text("# frozen")
    first_round = threading.Barrier(2)
    seen = []

    def fake_evaluate(harness, benchmark, repeats, concurrency, out_dir):
        tag = Path(out_dir).name
        seen.append(tag)
        first_round.wait(timeout=1)
        if tag == "q2-first":
            time.sleep(0.05)
        summary = _valid_summary()
        out = Path(out_dir)
        out.mkdir(parents=True, exist_ok=True)
        if tag == "q1-bad":
            summary["n_infra_invalid"] = 3
            summary["category_counts"] = {"env_error": 3}
            for i in range(3):
                (out / f"task{i}.rep0.json").write_text(json.dumps({
                    "category": "env_error",
                    "error": "token quota is not enough",
                }))
        (out / "summary.json").write_text(json.dumps(summary))
        return summary

    with pytest.raises(runner.QueuePaused, match="q1"):
        runner.run_parallel(
            lanes, root=tmp_path, budget_tokens=10_000,
            evaluate_fn=fake_evaluate, run_canary_fn=lambda cell: None,
            stagger_seconds=0,
        )

    assert set(seen) == {"q1-bad", "q2-first"}
