"""DemoCalib MVP experiment runner.

Integrates tau-Bench framework with BCP user simulator prompts and
behavioral fingerprint extraction. Runs uncalibrated baseline and
BCP variant experiments, extracts fingerprints, evaluates H1/H2 gates.

Usage:
    python run_mvp_experiment.py --model-path /root/models/Qwen2.5-7B-Instruct
    python run_mvp_experiment.py --num-tasks 5 --variants aave_target,overcorrected
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
from dataclasses import asdict
from pathlib import Path
from typing import Optional

import requests

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("democalib")

SCRIPT_DIR = Path(__file__).resolve().parent
PROMPTS_DIR_DEFAULT = str(SCRIPT_DIR.parent / "prompts")

sys.path.insert(0, str(SCRIPT_DIR))
from behavioral_fingerprint import BehavioralFingerprint, analyze_traces, BatchResult
from h_gate_evaluator import HGateEvaluator, H1Input, H2Input, EvalReport

sys.path.insert(0, str(SCRIPT_DIR.parent / "prompts"))
from prompt_loader import PromptLoader


# ---------------------------------------------------------------------------
# vLLM server management
# ---------------------------------------------------------------------------

def start_vllm_server(
    model_path: str,
    port: int = 8000,
    gpu_id: int = 0,
    max_model_len: int = 4096,
) -> subprocess.Popen:
    """Launch vLLM OpenAI-compatible API server."""
    env = os.environ.copy()
    env["CUDA_VISIBLE_DEVICES"] = str(gpu_id)
    cmd = [
        sys.executable, "-m", "vllm.entrypoints.openai.api_server",
        "--model", model_path,
        "--port", str(port),
        "--max-model-len", str(max_model_len),
        "--trust-remote-code",
        "--dtype", "auto",
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

    Returns the original method so it can be restored.
    """
    from tau_bench.envs.user import LLMUserSimulationEnv

    original_method = LLMUserSimulationEnv.build_system_prompt

    def patched_build_system_prompt(self):
        task_desc = ""
        if hasattr(self, "task") and self.task is not None:
            task_desc = getattr(self.task, "instruction", "")
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
    env_name: str,
    user_model: str,
    agent_model: str,
    base_url: str,
    num_tasks: int,
    num_trials: int,
) -> dict:
    """Run tau-Bench and return results dict with traces and task outcomes."""
    from tau_bench.run import run as tau_run

    results = tau_run(
        env=env_name,
        model=agent_model,
        user_model=user_model,
        user_model_provider="openai",
        model_provider="openai",
        num_tasks=num_tasks,
        num_trials=num_trials,
        api_key="[REDACTED]",
        user_api_key="[REDACTED]",
        base_url=base_url,
        user_base_url=base_url,
    )
    return results


def extract_traces_from_results(results) -> list[list[dict]]:
    """Extract conversation traces from tau-Bench results object.

    tau-Bench stores results per task per trial. Each result contains
    a conversation history. We normalize role names: tau-Bench uses
    "assistant" for agent turns, but our fingerprint expects "user" which
    tau-Bench already uses for the simulator's turns.
    """
    traces = []
    if hasattr(results, "results"):
        for task_results in results.results:
            if isinstance(task_results, list):
                for trial_result in task_results:
                    trace = _extract_single_trace(trial_result)
                    if trace:
                        traces.append(trace)
            else:
                trace = _extract_single_trace(task_results)
                if trace:
                    traces.append(trace)
    elif isinstance(results, dict) and "results" in results:
        for task_results in results["results"]:
            if isinstance(task_results, list):
                for trial_result in task_results:
                    trace = _extract_single_trace(trial_result)
                    if trace:
                        traces.append(trace)
            else:
                trace = _extract_single_trace(task_results)
                if trace:
                    traces.append(trace)
    return traces


def _extract_single_trace(result) -> Optional[list[dict]]:
    """Pull conversation history from a single trial result."""
    history = None
    if hasattr(result, "history"):
        history = result.history
    elif hasattr(result, "chat_history"):
        history = result.chat_history
    elif isinstance(result, dict):
        history = result.get("history") or result.get("chat_history")

    if not history:
        return None

    trace = []
    for msg in history:
        if isinstance(msg, dict):
            role = msg.get("role", "")
            content = msg.get("content", "")
        else:
            role = getattr(msg, "role", "")
            content = getattr(msg, "content", "")
        if role in ("user", "assistant"):
            trace.append({"role": role, "content": content or ""})
    return trace if trace else None


def compute_task_completion_rate(results) -> float:
    """Compute fraction of tasks where the agent succeeded."""
    total = 0
    passed = 0
    task_list = (
        results.results if hasattr(results, "results")
        else results.get("results", []) if isinstance(results, dict)
        else []
    )
    for task_results in task_list:
        items = task_results if isinstance(task_results, list) else [task_results]
        for item in items:
            total += 1
            reward = (
                getattr(item, "reward", None)
                if hasattr(item, "reward")
                else item.get("reward") if isinstance(item, dict)
                else None
            )
            if reward is not None and reward >= 1.0:
                passed += 1
    return passed / total if total > 0 else 0.0


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

    prompt_loader = PromptLoader(args.prompts_dir)
    fingerprinter = BehavioralFingerprint()

    model_name = Path(args.model_path).name
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
                env_name="retail",
                user_model=model_name,
                agent_model=args.agent_model or model_name,
                base_url=base_url,
                num_tasks=args.num_tasks,
                num_trials=args.num_trials,
            )
        finally:
            restore_tau_bench_user_simulator(original_method)

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
                    env_name="retail",
                    user_model=model_name,
                    agent_model=args.agent_model or model_name,
                    base_url=base_url,
                    num_tasks=args.num_tasks,
                    num_trials=args.num_trials,
                )
            finally:
                restore_tau_bench_user_simulator(original_method)

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

        report = evaluator.evaluate_all(h1_input, h2_inputs)

        gate_results = evaluator.to_dict(report)
        all_results["gate_evaluation"] = gate_results

        log.info("H1 passed: %s", report.h1.passed)
        log.info("H2 passed: %s", report.h2.passed)
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
        "--model-path", default="/root/models/Qwen2.5-7B-Instruct",
        help="Path to the LLM for vLLM (default: /root/models/Qwen2.5-7B-Instruct)",
    )
    p.add_argument(
        "--gpu", type=int, default=0,
        help="GPU ID for vLLM server (default: 0)",
    )
    p.add_argument(
        "--num-tasks", type=int, default=20,
        help="Number of tau-Bench tasks to evaluate (default: 20)",
    )
    p.add_argument(
        "--num-trials", type=int, default=1,
        help="Number of trials per task (default: 1)",
    )
    p.add_argument(
        "--output-dir", default="/root/democalib/results",
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
        "--vllm-port", type=int, default=8000,
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
