from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
from pathlib import Path

from optimization_lab.adapters.kernelbench import KernelBenchAdapter
from optimization_lab.adapters.ssh_kernelbench import SSHKernelBenchAdapter
from optimization_lab.budget import ExperimentBudget
from optimization_lab.campaign import CampaignPlan
from optimization_lab.dashboard import Dashboard
from optimization_lab.registry import ExperimentRegistry
from optimization_lab.runner import ExperimentRunner
from optimization_lab.task_spec import TaskSpec


PINNED_KERNELBENCH_COMMIT = "423217d9fda91e0c2d67e4a43bf62f96f6d104f1"
KERNELBENCH_URL = "https://github.com/ScalingIntelligence/KernelBench.git"
PROTOCOLS = Path(__file__).resolve().parent / "protocols"
ACTIVE_TASKS = ("kernelbench_layernorm", "kernelbench_matmul_sigmoid_sum")


def _paths(artifact_root: Path) -> tuple[ExperimentRegistry, Dashboard]:
    root = artifact_root.resolve()
    return ExperimentRegistry(root), Dashboard(root / "dashboard.html")


def _event_id(prefix: str, payload: dict[str, object]) -> str:
    encoded = json.dumps(payload, ensure_ascii=False, sort_keys=True).encode()
    return f"{prefix}:{hashlib.sha256(encoded).hexdigest()[:16]}"


def _task(task_id: str) -> TaskSpec:
    mapping = {
        "kernelbench_layernorm": PROTOCOLS / "kernelbench_layernorm.json",
        "kernelbench_matmul_sigmoid_sum": PROTOCOLS
        / "kernelbench_matmul_sigmoid_sum.json",
        "kernelbench_matmul_fusion": PROTOCOLS / "kernelbench_matmul_fusion.json",
    }
    try:
        return TaskSpec.from_json(mapping[task_id])
    except KeyError as exc:
        raise SystemExit(f"unknown task: {task_id}") from exc


def _env_keys(project_root: Path) -> set[str]:
    keys = {key for key in os.environ if key.startswith("TOKENROUTER_")}
    path = project_root / ".env.local"
    if path.is_file():
        for line in path.read_text(encoding="utf-8").splitlines():
            if "=" in line and not line.lstrip().startswith("#"):
                keys.add(line.split("=", 1)[0].strip())
    return keys


def initialize(artifact_root: Path, project_root: Path) -> int:
    registry, dashboard = _paths(artifact_root)
    registry.append(
        "phase_changed",
        {"phase": "P0", "status": "in_progress", "detail": "本地合同与评分环境预检"},
        event_id="phase:P0:started",
    )
    required = {"TOKENROUTER_MODEL", "TOKENROUTER_BASE_URL", "TOKENROUTER_API_KEY"}
    api_ready = required <= _env_keys(project_root.resolve())
    resources = (
        {
            "name": "model_api",
            "status": "ready" if api_ready else "blocked",
            "detail": "TokenRouter 三项配置存在；P0不调用模型" if api_ready else "缺少 TokenRouter 配置",
        },
        {
            "name": "local_gpu",
            "status": "ready" if shutil.which("nvidia-smi") else "blocked",
            "detail": "本机 GPU 可见" if shutil.which("nvidia-smi") else "当前开发机没有 NVIDIA GPU",
        },
        {
            "name": "cloud_gpu",
            "status": "blocked",
            "detail": "等待运行 ssh-preflight；目标为 a100jump GPU 4 的 A100 80GB",
        },
    )
    for resource in resources:
        registry.append(
            "resource_checked",
            resource,
            event_id=_event_id("resource", resource),
        )
    dashboard.render(registry)
    print(dashboard.path)
    return 0


def bootstrap(artifact_root: Path, repository: Path | None) -> int:
    registry, dashboard = _paths(artifact_root)
    target = (repository or (artifact_root / "benchmark" / "KernelBench")).resolve()
    if target.exists():
        if not (target / ".git").is_dir():
            raise SystemExit(f"refusing to overwrite non-checkout: {target}")
    else:
        target.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(
            ["git", "clone", "--filter=blob:none", KERNELBENCH_URL, str(target)],
            check=True,
        )
    subprocess.run(
        ["git", "-C", str(target), "checkout", "--detach", PINNED_KERNELBENCH_COMMIT],
        check=True,
    )
    payload = {
        "name": "kernelbench_checkout",
        "status": "ready",
        "detail": f"{target} @ {PINNED_KERNELBENCH_COMMIT}",
    }
    registry.append("resource_checked", payload, event_id=_event_id("resource", payload))
    dashboard.render(registry)
    print(target)
    return 0


def prepare_campaign(
    *,
    artifact_root: Path,
    project_root: Path,
    executor_model: str | None,
    model_call_cap_per_lane: int | None,
    gpu_seconds_cap_per_lane: float | None,
    api_dollar_cap: float | None,
    gpu_dollar_cap: float | None,
) -> int:
    registry, dashboard = _paths(artifact_root)
    p0_clean_confirmed = any(
        event["event_type"] == "p0_clean_environment_confirmed"
        and event["payload"].get("status") == "ready"
        for event in registry.read_events()
    )
    plan = CampaignPlan.build(
        project_root=project_root,
        artifact_root=artifact_root,
        executor_model=executor_model,
        model_call_cap_per_lane=model_call_cap_per_lane,
        gpu_seconds_cap_per_lane=gpu_seconds_cap_per_lane,
        api_dollar_cap=api_dollar_cap,
        gpu_dollar_cap=gpu_dollar_cap,
        p0_clean_confirmed=p0_clean_confirmed,
    )
    plan_path = registry.root / "campaign_plan.json"
    plan.write(plan_path)
    payload = {
        "status": "ready" if plan.execution_ready else "blocked_pending_approval",
        "blockers": list(plan.blockers),
        "model_calls_consumed": 0,
        "gpu_seconds_consumed": 0.0,
        "detail": (
            "P1三种基线与P2两题各三条谱系已离线冻结；未调用模型或GPU"
            if not plan.execution_ready
            else "P1/P2 campaign合同已冻结并满足执行门禁"
        ),
    }
    registry.append(
        "campaign_prepared",
        payload,
        event_id=_event_id("campaign-prepared", plan.to_dict()),
    )
    dashboard.render(registry)
    print(plan_path)
    return 0


def preflight(
    artifact_root: Path,
    repository: Path,
    mode: str,
    check_executor: bool,
) -> int:
    registry, dashboard = _paths(artifact_root)
    adapter = KernelBenchAdapter(repository=repository, mode=mode)
    all_ready = True
    for task_id in ACTIVE_TASKS:
        for check in adapter.preflight(_task(task_id), check_executor=check_executor):
            payload = {
                "name": f"{task_id}:{check.name}",
                "status": check.status,
                "detail": check.detail,
            }
            registry.append(
                "resource_checked",
                payload,
                event_id=_event_id("preflight", payload),
            )
            all_ready = all_ready and check.ready
    dashboard.render(registry)
    print(dashboard.path)
    return 0 if all_ready else 2


def ssh_adapter(args: argparse.Namespace) -> SSHKernelBenchAdapter:
    return SSHKernelBenchAdapter(
        host=args.ssh_host,
        remote_repository=args.remote_repository,
        remote_root=args.remote_root,
        gpu_index=args.gpu_index,
        remote_uv=args.remote_uv,
    )


def ssh_preflight(artifact_root: Path, args: argparse.Namespace) -> int:
    registry, dashboard = _paths(artifact_root)
    adapter = ssh_adapter(args)
    all_ready = True
    for task_id in ACTIVE_TASKS:
        for check in adapter.preflight(_task(task_id)):
            payload = {
                "name": f"{task_id}:{check.name}",
                "status": check.status,
                "detail": check.detail,
            }
            registry.append(
                "resource_checked",
                payload,
                event_id=_event_id("ssh-preflight", payload),
            )
            all_ready = all_ready and check.ready
    cloud = {
        "name": "cloud_gpu",
        "status": "ready" if all_ready else "blocked",
        "detail": "a100jump GPU 4 · A100-SXM4 80GB" if all_ready else "SSH A100预检未通过",
    }
    registry.append("resource_checked", cloud, event_id=_event_id("resource", cloud))
    dashboard.render(registry)
    print(dashboard.path)
    return 0 if all_ready else 2


def evaluate(
    artifact_root: Path,
    repository: Path,
    mode: str,
    task_id: str,
    candidate: Path,
    candidate_id: str,
) -> int:
    registry, dashboard = _paths(artifact_root)
    used_gpu = sum(
        float(event["payload"]["feedback"].get("gpu_seconds", 0.0))
        for event in registry.read_events()
        if event["event_type"] == "candidate_evaluated"
    )
    budget = ExperimentBudget(
        max_gpu_seconds=12 * 60 * 60,
        max_model_calls=100,
        gpu_seconds_used=used_gpu,
    )
    runner = ExperimentRunner(
        registry=registry,
        adapter=KernelBenchAdapter(repository=repository, mode=mode),
        dashboard=dashboard,
        budget=budget,
    )
    feedback = runner.evaluate(_task(task_id), candidate, candidate_id=candidate_id)
    print(json.dumps(feedback.to_dict(), ensure_ascii=False, sort_keys=True))
    return 0 if feedback.valid_run else 2


def ssh_evaluate(artifact_root: Path, args: argparse.Namespace) -> int:
    registry, dashboard = _paths(artifact_root)
    used_gpu = sum(
        float(event["payload"]["feedback"].get("gpu_seconds", 0.0))
        for event in registry.read_events()
        if event["event_type"] == "candidate_evaluated"
    )
    runner = ExperimentRunner(
        registry=registry,
        adapter=ssh_adapter(args),
        dashboard=dashboard,
        budget=ExperimentBudget(
            max_gpu_seconds=12 * 60 * 60,
            max_model_calls=100,
            gpu_seconds_used=used_gpu,
        ),
    )
    feedback = runner.evaluate(
        _task(args.task), args.candidate, candidate_id=args.candidate_id
    )
    print(json.dumps(feedback.to_dict(), ensure_ascii=False, sort_keys=True))
    return 0 if feedback.valid_run else 2


def add_ssh_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--ssh-host", default="a100jump")
    parser.add_argument(
        "--remote-repository",
        default="/data3/chenzhuofan/moss-kernelbench-pilot/KernelBench",
    )
    parser.add_argument(
        "--remote-root", default="/data3/chenzhuofan/moss-kernelbench-pilot"
    )
    parser.add_argument("--gpu-index", type=int, default=4)
    parser.add_argument(
        "--remote-uv",
        default="/data3/chenzhuofan/moss-kernelbench-pilot/uv-pkg/bin/uv",
    )


def render(artifact_root: Path) -> int:
    registry, dashboard = _paths(artifact_root)
    dashboard.render(registry)
    print(dashboard.path)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="MOSS KernelBench optimization lab")
    sub = parser.add_subparsers(dest="command", required=True)
    init = sub.add_parser("init")
    init.add_argument("--artifact-root", type=Path, required=True)
    init.add_argument("--project-root", type=Path, required=True)
    boot = sub.add_parser("bootstrap")
    boot.add_argument("--artifact-root", type=Path, required=True)
    boot.add_argument("--repository", type=Path)
    campaign = sub.add_parser("prepare-campaign")
    campaign.add_argument("--artifact-root", type=Path, required=True)
    campaign.add_argument("--project-root", type=Path, required=True)
    campaign.add_argument("--executor-model")
    campaign.add_argument("--model-call-cap-per-lane", type=int)
    campaign.add_argument("--gpu-seconds-cap-per-lane", type=float)
    campaign.add_argument("--api-dollar-cap", type=float)
    campaign.add_argument("--gpu-dollar-cap", type=float)
    check = sub.add_parser("preflight")
    check.add_argument("--artifact-root", type=Path, required=True)
    check.add_argument("--repository", type=Path, required=True)
    check.add_argument("--mode", choices=("local", "modal"), default="modal")
    check.add_argument("--check-executor", action="store_true")
    ssh_check = sub.add_parser("ssh-preflight")
    ssh_check.add_argument("--artifact-root", type=Path, required=True)
    add_ssh_arguments(ssh_check)
    score = sub.add_parser("evaluate")
    score.add_argument("--artifact-root", type=Path, required=True)
    score.add_argument("--repository", type=Path, required=True)
    score.add_argument("--mode", choices=("local", "modal"), default="modal")
    score.add_argument(
        "--task",
        choices=ACTIVE_TASKS,
        required=True,
    )
    score.add_argument("--candidate", type=Path, required=True)
    score.add_argument("--candidate-id", required=True)
    ssh_score = sub.add_parser("ssh-evaluate")
    ssh_score.add_argument("--artifact-root", type=Path, required=True)
    ssh_score.add_argument(
        "--task",
        choices=ACTIVE_TASKS,
        required=True,
    )
    ssh_score.add_argument("--candidate", type=Path, required=True)
    ssh_score.add_argument("--candidate-id", required=True)
    add_ssh_arguments(ssh_score)
    show = sub.add_parser("render")
    show.add_argument("--artifact-root", type=Path, required=True)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "init":
        return initialize(args.artifact_root, args.project_root)
    if args.command == "bootstrap":
        return bootstrap(args.artifact_root, args.repository)
    if args.command == "prepare-campaign":
        return prepare_campaign(
            artifact_root=args.artifact_root,
            project_root=args.project_root,
            executor_model=args.executor_model,
            model_call_cap_per_lane=args.model_call_cap_per_lane,
            gpu_seconds_cap_per_lane=args.gpu_seconds_cap_per_lane,
            api_dollar_cap=args.api_dollar_cap,
            gpu_dollar_cap=args.gpu_dollar_cap,
        )
    if args.command == "preflight":
        return preflight(
            args.artifact_root,
            args.repository,
            args.mode,
            args.check_executor,
        )
    if args.command == "ssh-preflight":
        return ssh_preflight(args.artifact_root, args)
    if args.command == "evaluate":
        return evaluate(
            args.artifact_root,
            args.repository,
            args.mode,
            args.task,
            args.candidate,
            args.candidate_id,
        )
    if args.command == "ssh-evaluate":
        return ssh_evaluate(args.artifact_root, args)
    if args.command == "render":
        return render(args.artifact_root)
    raise AssertionError(args.command)
