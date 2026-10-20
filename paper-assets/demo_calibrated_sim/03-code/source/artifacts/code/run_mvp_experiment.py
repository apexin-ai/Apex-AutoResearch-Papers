"""DemoCalib MVP experiment runner.

Integrates tau-Bench framework with BCP user simulator prompts and
behavioral fingerprint extraction. Runs uncalibrated baseline and
BCP variant experiments, extracts fingerprints, evaluates H1/H2/H3 gates.

Usage:
    python run_mvp_experiment.py --model-path /root/autodl-tmp/models/Qwen/Qwen2.5-7B-Instruct
    python run_mvp_experiment.py --end-index 5 --variants aave_target,overcorrected
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import signal
import subprocess
import sys
import time
from pathlib import Path
from typing import List, Optional

import requests

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("democalib")

SCRIPT_DIR = Path(__file__).resolve().parent
PROMPTS_DIR_DEFAULT = str(SCRIPT_DIR / "prompts")
SERVED_MODEL_NAME = "democalib-qwen"

sys.path.insert(0, str(SCRIPT_DIR))
from behavioral_fingerprint import BehavioralFingerprint, analyze_traces, BatchResult
from h_gate_evaluator import HGateEvaluator, H1Input, H2Input, H3Input, EvalReport

from prompt_loader import PromptLoader


# ---------------------------------------------------------------------------
# vLLM server management
# ---------------------------------------------------------------------------

def start_vllm_server(
    model_path: str,
    port: int = 8000,
    gpu_id: int = 0,
    max_model_len: int = 16384,
) -> subprocess.Popen:
    """Launch vLLM OpenAI-compatible API server."""
    env = os.environ.copy()
    env["CUDA_VISIBLE_DEVICES"] = str(gpu_id)
    # vLLM 0.18.1 + PyTorch 2.10 torch._inductor compat workaround
    env["TORCHDYNAMO_DISABLE"] = "1"
    env["VLLM_USE_V1"] = "0"
    cmd = [
        sys.executable, "-m", "vllm.entrypoints.openai.api_server",
        "--model", model_path,
        "--port", str(port),
        "--max-model-len", str(max_model_len),
        "--trust-remote-code",
        "--dtype", "auto",
        "--enforce-eager",
        "--served-model-name", SERVED_MODEL_NAME,
        "--enable-auto-tool-choice",
        "--tool-call-parser", "hermes",
    ]
    log.info("Starting vLLM server: %s", " ".join(cmd))
    proc = subprocess.Popen(
        cmd, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )
    return proc


def wait_for_vllm(base_url: str, timeout: int = 300, poll_interval: int = 5) -> bool:
    """Block until vLLM /v1/models endpoint responds or timeout."""
    url = f"{base_url}/v1/models"
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            r = requests.get(url, timeout=3)
            if r.status_code == 200:
                log.info("vLLM server ready.")
                return True
        except requests.ConnectionError:
            pass
        time.sleep(poll_interval)
    log.error("vLLM server did not become ready within %ds.", timeout)
    return False


def stop_vllm_server(proc: subprocess.Popen) -> None:
    """Gracefully stop the vLLM server."""
    if proc.poll() is None:
        proc.send_signal(signal.SIGTERM)
        try:
            proc.wait(timeout=15)
        except subprocess.TimeoutExpired:
            proc.kill()
        log.info("vLLM server stopped.")


# ---------------------------------------------------------------------------
# tau-Bench monkey-patch
# ---------------------------------------------------------------------------

def patch_tau_bench_user_simulator(prompt_text: str) -> callable:
    """Monkey-patch LLMUserSimulationEnv.build_system_prompt to return custom prompt.

    The original signature is build_system_prompt(self, instruction=None).
    instruction is the task description string passed from reset().
    Returns the original method so it can be restored.
    """
    from tau_bench.envs.user import LLMUserSimulationEnv

    original_method = LLMUserSimulationEnv.build_system_prompt

    def patched_build_system_prompt(self, instruction=None):
        task_desc = instruction or ""
        return prompt_text.replace("{task_description}", task_desc)

    LLMUserSimulationEnv.build_system_prompt = patched_build_system_prompt
    return original_method


def restore_tau_bench_user_simulator(original_method) -> None:
    """Restore the original build_system_prompt method."""
    from tau_bench.envs.user import LLMUserSimulationEnv
    LLMUserSimulationEnv.build_system_prompt = original_method


# ---------------------------------------------------------------------------
# tau-Bench experiment runner
# ---------------------------------------------------------------------------

def run_tau_bench_experiment(
    model_name: str,
    agent_model_name: str,
    end_index: int,
    num_trials: int,
    task_split: str = "dev",
    log_dir: str = "/root/democalib/results",
) -> List:
    """Run tau-Bench with RunConfig and return List[EnvRunResult]."""
    from tau_bench.run import run as tau_run
    from tau_bench.types import RunConfig

    config = RunConfig(
        model_provider="openai",
        user_model_provider="openai",
        model=agent_model_name,
        user_model=model_name,
        env="retail",
        num_trials=num_trials,
        task_split=task_split,
        start_index=0,
        end_index=end_index,
        log_dir=log_dir,
        max_concurrency=1,
        temperature=0.0,
        user_strategy="llm",
    )
    return tau_run(config)


def extract_traces_from_results(results: List) -> list[list[dict]]:
    """Extract conversation traces from tau-Bench List[EnvRunResult].

    Each EnvRunResult has .traj (List[Dict]) containing the full message history.
    We extract user-role messages for behavioral fingerprinting.
    """
    traces = []
    for result in results:
        traj = None
        if hasattr(result, "traj"):
            traj = result.traj
        elif isinstance(result, dict):
            traj = result.get("traj", [])

        if not traj:
            continue

        trace = []
        for msg in traj:
            if isinstance(msg, dict):
                role = msg.get("role", "")
                content = msg.get("content", "")
            else:
                role = getattr(msg, "role", "")
                content = getattr(msg, "content", "")
            if role in ("user", "assistant"):
                trace.append({"role": role, "content": content or ""})

        if trace:
            traces.append(trace)

    return traces


def compute_task_completion_rate(results: List) -> float:
    """Compute fraction of tasks where the agent succeeded (reward >= 1.0)."""
    if not results:
        return 0.0
    total = len(results)
    passed = 0
    for result in results:
        reward = (
            getattr(result, "reward", None)
            if hasattr(result, "reward")
            else result.get("reward") if isinstance(result, dict)
            else None
        )
        if reward is not None and reward >= 1.0 - 1e-6:
            passed += 1
    return passed / total


# ---------------------------------------------------------------------------
# Context overflow filtering
# ---------------------------------------------------------------------------

def _is_context_overflow(result) -> bool:
    info = (
        getattr(result, "info", None)
        if hasattr(result, "info")
        else result.get("info") if isinstance(result, dict) else None
    )
    if info is None:
        return False
    info_str = str(info)
    return "ContextWindowExceededError" in info_str or "context_length_exceeded" in info_str


def filter_context_overflow(results: List, label: str = "") -> tuple[List, int]:
    valid = []
    skipped = 0
    for i, r in enumerate(results):
        if _is_context_overflow(r):
            task_id = getattr(r, "task_id", i)
            log.warning("⚠️ Task %s skipped: context window overflow%s", task_id, f" ({label})" if label else "")
            skipped += 1
        else:
            valid.append(r)
    return valid, skipped


# ---------------------------------------------------------------------------
# Variant definitions
# ---------------------------------------------------------------------------

BCP_VARIANTS_WITH_TARGETS = {
    "aave_target": {"question_rate": 10, "politeness_rate": 20},
    "indian_english_target": {"question_rate": 10, "politeness_rate": 20},
    "overcorrected": {"question_rate": 5, "politeness_rate": 10},
    "single_dim_question": {"question_rate": 10, "politeness_rate": None},
    "single_dim_politeness": {"question_rate": None, "politeness_rate": 20},
}

ALL_VARIANT_NAMES = list(BCP_VARIANTS_WITH_TARGETS.keys())


# ---------------------------------------------------------------------------
# Main experiment
# ---------------------------------------------------------------------------

def run_experiment(args: argparse.Namespace) -> dict:
    """Run the full MVP experiment pipeline."""

    base_url = f"http://localhost:{args.vllm_port}"
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Set litellm env vars so tau-Bench's openai provider hits local vLLM
    os.environ["OPENAI_API_KEY"] = "EMPTY"
    os.environ["OPENAI_API_BASE"] = f"{base_url}/v1"

    prompt_loader = PromptLoader(args.prompts_dir)

    model_name = SERVED_MODEL_NAME
    agent_model_name = args.agent_model or model_name
    variants_to_run = (
        args.variants.split(",") if args.variants else ALL_VARIANT_NAMES
    )

    vllm_proc = None
    if not args.skip_vllm:
        vllm_proc = start_vllm_server(
            args.model_path, args.vllm_port, args.gpu
        )
        if not wait_for_vllm(base_url):
            if vllm_proc:
                stop_vllm_server(vllm_proc)
            raise RuntimeError("vLLM server failed to start")

    all_results = {}
    baseline_batch: Optional[BatchResult] = None
    baseline_completion_rate = 0.0

    try:
        # ---- Phase 1: Uncalibrated baseline ----
        log.info("=== Phase 1: Uncalibrated baseline ===")
        base_prompt = prompt_loader.load_base(
            task_description="{task_description}"
        )
        original_method = patch_tau_bench_user_simulator(base_prompt)

        try:
            raw_results = run_tau_bench_experiment(
                model_name=model_name,
                agent_model_name=agent_model_name,
                end_index=args.end_index,
                num_trials=args.num_trials,
                task_split=args.task_split,
                log_dir=args.output_dir,
            )
        finally:
            restore_tau_bench_user_simulator(original_method)

        raw_results, baseline_skipped = filter_context_overflow(raw_results, "baseline")
        if baseline_skipped:
            log.info("Baseline: %d/%d tasks skipped (context overflow)", baseline_skipped, baseline_skipped + len(raw_results))

        baseline_traces = extract_traces_from_results(raw_results)
        baseline_batch = analyze_traces(baseline_traces)
        baseline_completion_rate = compute_task_completion_rate(raw_results)

        all_results["uncalibrated_baseline"] = {
            "mean_question_rate": baseline_batch.mean_question_rate,
            "std_question_rate": baseline_batch.std_question_rate,
            "mean_politeness_rate": baseline_batch.mean_politeness_rate,
            "std_politeness_rate": baseline_batch.std_politeness_rate,
            "num_traces": baseline_batch.num_traces,
            "task_completion_rate": baseline_completion_rate,
        }
        log.info(
            "Baseline: question_rate=%.3f (std=%.3f), politeness_rate=%.3f (std=%.3f), "
            "completion=%.2f, traces=%d",
            baseline_batch.mean_question_rate, baseline_batch.std_question_rate,
            baseline_batch.mean_politeness_rate, baseline_batch.std_politeness_rate,
            baseline_completion_rate, baseline_batch.num_traces,
        )

        # ---- Phase 2: BCP variants ----
        log.info("=== Phase 2: BCP variants ===")

        for vname in variants_to_run:
            log.info("--- Running variant: %s ---", vname)
            variant_prompt = prompt_loader.load_variant(
                vname, task_description="{task_description}"
            )
            original_method = patch_tau_bench_user_simulator(variant_prompt)

            try:
                raw_results = run_tau_bench_experiment(
                    model_name=model_name,
                    agent_model_name=agent_model_name,
                    end_index=args.end_index,
                    num_trials=args.num_trials,
                    task_split=args.task_split,
                    log_dir=args.output_dir,
                )
            finally:
                restore_tau_bench_user_simulator(original_method)

            raw_results, variant_skipped = filter_context_overflow(raw_results, vname)
            if variant_skipped:
                log.info("Variant %s: %d/%d tasks skipped (context overflow)", vname, variant_skipped, variant_skipped + len(raw_results))

            variant_traces = extract_traces_from_results(raw_results)
            variant_batch = analyze_traces(variant_traces)
            variant_completion = compute_task_completion_rate(raw_results)

            all_results[vname] = {
                "mean_question_rate": variant_batch.mean_question_rate,
                "std_question_rate": variant_batch.std_question_rate,
                "mean_politeness_rate": variant_batch.mean_politeness_rate,
                "std_politeness_rate": variant_batch.std_politeness_rate,
                "num_traces": variant_batch.num_traces,
                "task_completion_rate": variant_completion,
            }
            log.info(
                "Variant %s: question_rate=%.3f, politeness_rate=%.3f, completion=%.2f",
                vname, variant_batch.mean_question_rate,
                variant_batch.mean_politeness_rate, variant_completion,
            )

        # ---- Phase 3: H-gate evaluation ----
        log.info("=== Phase 3: H-gate evaluation ===")

        evaluator = HGateEvaluator()

        h1_input = H1Input(
            mean_question_rate=baseline_batch.mean_question_rate,
            mean_politeness_rate=baseline_batch.mean_politeness_rate,
            std_question_rate=baseline_batch.std_question_rate,
            std_politeness_rate=baseline_batch.std_politeness_rate,
        )

        h2_inputs = []
        for vname in variants_to_run:
            targets = BCP_VARIANTS_WITH_TARGETS.get(vname, {})
            tq = targets.get("question_rate")
            tp = targets.get("politeness_rate")
            if tq is None or tp is None:
                continue
            vr = all_results[vname]
            h2_inputs.append(H2Input(
                variant_name=vname,
                target_question_rate=tq / 100.0,
                target_politeness_rate=tp / 100.0,
                measured_question_rate=vr["mean_question_rate"],
                measured_politeness_rate=vr["mean_politeness_rate"],
            ))

        h3_inputs = []
        for vname in variants_to_run:
            targets = BCP_VARIANTS_WITH_TARGETS.get(vname, {})
            if targets.get("question_rate") is None or targets.get("politeness_rate") is None:
                continue
            vr = all_results[vname]
            h3_inputs.append(H3Input(
                variant_name=vname,
                calibrated_task_completion_rate=vr["task_completion_rate"],
                baseline_task_completion_rate=baseline_completion_rate,
            ))

        report = evaluator.evaluate_all(h1_input, h2_inputs, h3_variants=h3_inputs)

        gate_results = evaluator.to_dict(report)
        all_results["gate_evaluation"] = gate_results

        log.info("H1 passed: %s", report.h1.passed)
        log.info("H2 passed: %s", report.h2.passed)
        if report.h3:
            log.info("H3 passed: %s", report.h3.passed)
        log.info("All gates passed: %s", report.all_passed)

    finally:
        if vllm_proc:
            stop_vllm_server(vllm_proc)

    # ---- Save results ----
    output_file = output_dir / "mvp_results.json"
    with open(output_file, "w") as f:
        json.dump(all_results, f, indent=2, default=str)
    log.info("Results saved to %s", output_file)

    return all_results


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="DemoCalib MVP experiment: BCP user simulator calibration on tau-Bench"
    )
    p.add_argument(
        "--model-path", default="/root/autodl-tmp/models/Qwen/Qwen2.5-7B-Instruct",
        help="Path to the LLM for vLLM (default: /root/autodl-tmp/models/Qwen/Qwen2.5-7B-Instruct)",
    )
    p.add_argument(
        "--gpu", "--gpu-id", type=int, default=0, dest="gpu",
        help="GPU ID for vLLM server (default: 0)",
    )
    p.add_argument(
        "--end-index", "--num-tasks", type=int, default=20, dest="end_index",
        help="Number of tau-Bench tasks to evaluate, 0-indexed end (default: 20)",
    )
    p.add_argument(
        "--num-trials", type=int, default=1,
        help="Number of trials per task (default: 1)",
    )
    p.add_argument(
        "--task-split", default="dev",
        help="Task split: train/dev/test (default: dev)",
    )
    p.add_argument(
        "--output-dir", "--log-dir", default="/root/democalib/results", dest="output_dir",
        help="Directory for experiment output (default: /root/democalib/results)",
    )
    p.add_argument(
        "--prompts-dir", default=PROMPTS_DIR_DEFAULT,
        help="Directory containing prompt templates (default: %(default)s)",
    )
    p.add_argument(
        "--variants", default=None,
        help="Comma-separated variant names to run (default: all)",
    )
    p.add_argument(
        "--vllm-port", "--port", type=int, default=8000, dest="vllm_port",
        help="Port for vLLM OpenAI-compatible server (default: 8000)",
    )
    p.add_argument(
        "--agent-model", default=None,
        help="Model name for the agent side (default: same as user simulator)",
    )
    p.add_argument(
        "--skip-vllm", action="store_true",
        help="Skip vLLM server launch (assume already running)",
    )
    return p.parse_args()


if __name__ == "__main__":
    results = run_experiment(parse_args())
    passed = results.get("gate_evaluation", {}).get("all_passed", False)
    sys.exit(0 if passed else 1)
