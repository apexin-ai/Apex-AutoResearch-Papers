from __future__ import annotations

import argparse
import os
import shutil
import subprocess
from pathlib import Path

from optimization_lab.harness_builder.dual_harness import HarnessWorkspace
from optimization_lab.harness_builder.simpletes_scaling import (
    ClaimedGenerator,
    SIMPLETES_MODEL,
    SIMPLETES_PAPER_COMMIT,
    SIMPLETES_REPOSITORY,
    SIMPLETES_TASKS,
    SimpleTESHarnessEvolutionCampaign,
    SimpleTESPortfolioCampaign,
    SimpleTESScalingContract,
    SimpleTESScalingEvaluator,
)
from optimization_lab.openai_chat_generator import (
    OpenAIChatRequestConfig,
    OpenAICompatibleChatGenerator,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = PROJECT_ROOT / ".claude-manager" / "benchmark-envs" / "simpletes-scaling" / "SimpleTES"
DEFAULT_WORKSPACE = PROJECT_ROOT / "results" / "optimization_lab" / "simpletes-scaling" / "round-001"


def _source_head(source: Path) -> str:
    return subprocess.check_output(
        ["git", "-C", str(source), "rev-parse", "HEAD"],
        text=True,
    ).strip()


def prepare(source: Path) -> None:
    source = source.resolve()
    if source.exists():
        if not (source / ".git").is_dir():
            raise SystemExit(f"source exists but is not a Git checkout: {source}")
    else:
        source.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(
            ["git", "clone", "--filter=blob:none", SIMPLETES_REPOSITORY, str(source)],
            check=True,
        )
    subprocess.run(
        ["git", "-C", str(source), "checkout", "--detach", SIMPLETES_PAPER_COMMIT],
        check=True,
    )
    print(f"prepared {source} @ {_source_head(source)}", flush=True)


def preflight(*, source: Path, python_root: Path, site_packages: Path) -> None:
    source = source.resolve()
    if _source_head(source) != SIMPLETES_PAPER_COMMIT:
        raise SystemExit("SimpleTES source is not pinned to the paper commit")
    status = subprocess.check_output(
        ["git", "-C", str(source), "status", "--porcelain"],
        text=True,
    )
    if status.strip():
        raise SystemExit("SimpleTES source checkout is dirty")
    if shutil.which("bwrap") is None:
        raise SystemExit("bubblewrap is required for the label-blind evaluator")
    if not (python_root / "bin" / "python3.13").is_file():
        raise SystemExit("pinned Python 3.13 runtime is missing")
    if not (site_packages / "numpy").is_dir() or not (site_packages / "scipy").is_dir():
        raise SystemExit("scaling evaluator site-packages are incomplete")
    for relative in (
        "datasets/scaling_law/parallel_scaling_law/evaluator.py",
        "datasets/scaling_law/domain_mixture_scaling_law/evaluator.py",
        "datasets/scaling_law/lr_bsz_scaling_law/evaluator.py",
        "datasets/scaling_law/easy_question_scaling_law/evaluator.py",
        "best_results/data_science/parallel_scaling_law/parallel_scaling_law_best.py",
        "best_results/data_science/domain_mixture_scaling_law/domain_mixture_scaling_law_best.py",
        "best_results/data_science/learning_rate_and_batch_size_scaling_law/learning_rate_and_batch_size_scaling_law_best.py",
        "best_results/data_science/easy_question_u_shaped_scaling_law/easy_question_u_shaped_scaling_law_best.py",
    ):
        if not (source / relative).is_file():
            raise SystemExit(f"pinned source file is missing: {relative}")
    contract = SimpleTESScalingContract()
    print(f"preflight ready contract={contract.sha256}", flush=True)


def execute(args: argparse.Namespace) -> None:
    source = args.source.resolve()
    workspace_root = args.workspace.resolve()
    if args.command == "lineage":
        # Keep each task lineage's Harness, traces, and operation journal isolated.
        workspace_root = workspace_root / args.task
    preflight(
        source=source,
        python_root=args.python_root.resolve(),
        site_packages=args.site_packages.resolve(),
    )
    if not args.execute:
        raise SystemExit("formal calls require --execute")
    api_key = [REDACTED]
    if not api_key:
        parsed_loopback = args.api_base.startswith("http://127.0.0.1:") or args.api_base.startswith(
            "http://localhost:"
        )
        if parsed_loopback:
            api_key = "[REDACTED]"
        else:
            raise SystemExit(f"missing API key environment variable: {args.api_key_env}")
    workspace = HarnessWorkspace(workspace_root)
    # Keep the transport canary's claim/result ledger separate from the formal
    # lineage. A completed canary is not a round receipt and must not block the
    # first formal round as a pending operation.
    canary_workspace = HarnessWorkspace(workspace_root.parent / f"{workspace_root.name}-canary")
    canary_transport = OpenAICompatibleChatGenerator(
        OpenAIChatRequestConfig(
            base_url=args.api_base,
            api_key=[REDACTED],
            temperature=0.7,
            max_tokens=256,
            reasoning_effort="medium",
            timeout_seconds=120,
        )
    )
    canary = ClaimedGenerator(
        workspace=canary_workspace,
        generator=canary_transport,
        run_id=f"{args.run_id}-canary",
        stage="model",
        contract_sha256=SimpleTESScalingContract().sha256,
    ).generate("Reply with OK.", model=SIMPLETES_MODEL)
    print(f"MODEL_CANARY provider={canary.provider} usage={canary.usage}", flush=True)
    transport = OpenAICompatibleChatGenerator(
        OpenAIChatRequestConfig(
            base_url=args.api_base,
            api_key=[REDACTED],
            temperature=0.7,
            max_tokens=32_768,
            reasoning_effort="medium",
            timeout_seconds=3_000,
        )
    )
    evaluator = SimpleTESScalingEvaluator(
        source_root=source,
        python_root=args.python_root.resolve(),
        site_packages=args.site_packages.resolve(),
    )
    if args.command == "lineage":
        task = next(item for item in SIMPLETES_TASKS if item.label == args.task)
        campaign = SimpleTESHarnessEvolutionCampaign(
            workspace=workspace,
            source_root=source,
            generator=transport,
            evaluator=evaluator,
            task=task,
            reporter=lambda message: print(message, flush=True),
        )
        result = campaign.run_generic(run_id=args.run_id, max_rounds=args.rounds)
        print(
            "COMPLETE "
            f"task={args.task} rounds={len(result.rounds)} "
            f"best={result.best_harness_sha256} score={result.best_score!s} "
            f"champion={workspace.champion().sha256}",
            flush=True,
        )
        return
    campaign = SimpleTESPortfolioCampaign(
        workspace=workspace,
        source_root=source,
        generator=transport,
        evaluator=evaluator,
        reporter=lambda message: print(message, flush=True),
    )
    result = campaign.run(run_id=args.run_id)
    print(
        "COMPLETE "
        f"new_harnesses={len(result.scores)} "
        f"champion={result.portfolio.next_champion_sha256} "
        f"promoted={result.portfolio.promoted_proposal_id}",
        flush=True,
    )


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser()
    sub = result.add_subparsers(dest="command", required=True)
    prepare_parser = sub.add_parser("prepare")
    prepare_parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    preflight_parser = sub.add_parser("preflight")
    preflight_parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    preflight_parser.add_argument(
        "--python-root",
        type=Path,
        default=Path("/home/ubuntu/.local/share/uv/python/cpython-3.13.14-linux-x86_64-gnu"),
    )
    preflight_parser.add_argument(
        "--site-packages",
        type=Path,
        default=Path("/tmp/moss-simpletes-venv-task116/lib/python3.13/site-packages"),
    )
    run_parser = sub.add_parser("run")
    run_parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    run_parser.add_argument("--workspace", type=Path, default=DEFAULT_WORKSPACE)
    run_parser.add_argument("--run-id", default="simpletes-round-001")
    run_parser.add_argument("--api-base", default="https://api.apexin.ai/v1")
    run_parser.add_argument("--api-key-env", default="OPENAI_API_KEY")
    run_parser.add_argument(
        "--python-root",
        type=Path,
        default=Path("/home/ubuntu/.local/share/uv/python/cpython-3.13.14-linux-x86_64-gnu"),
    )
    run_parser.add_argument(
        "--site-packages",
        type=Path,
        default=Path("/tmp/moss-simpletes-venv-task116/lib/python3.13/site-packages"),
    )
    run_parser.add_argument("--execute", action="store_true")
    lineage_parser = sub.add_parser("lineage")
    lineage_parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    lineage_parser.add_argument(
        "--workspace",
        type=Path,
        default=PROJECT_ROOT / "results" / "optimization_lab" / "simpletes-scaling" / "lineage",
    )
    lineage_parser.add_argument("--run-id", default="simpletes-lineage-001")
    lineage_parser.add_argument("--task", choices=[task.label for task in SIMPLETES_TASKS], required=True)
    lineage_parser.add_argument("--api-base", default="https://api.apexin.ai/v1")
    lineage_parser.add_argument("--api-key-env", default="OPENAI_API_KEY")
    lineage_parser.add_argument(
        "--python-root",
        type=Path,
        default=Path("/home/ubuntu/.local/share/uv/python/cpython-3.13.14-linux-x86_64-gnu"),
    )
    lineage_parser.add_argument(
        "--site-packages",
        type=Path,
        default=Path("/tmp/moss-simpletes-venv-task116/lib/python3.13/site-packages"),
    )
    lineage_parser.add_argument("--rounds", type=int, default=8)
    lineage_parser.add_argument("--execute", action="store_true")
    return result


def main() -> int:
    args = parser().parse_args()
    if args.command == "prepare":
        prepare(args.source)
    elif args.command == "preflight":
        preflight(
            source=args.source,
            python_root=args.python_root,
            site_packages=args.site_packages,
        )
    else:
        execute(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
