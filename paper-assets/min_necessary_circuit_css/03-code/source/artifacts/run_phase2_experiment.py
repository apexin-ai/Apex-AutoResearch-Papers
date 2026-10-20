"""Phase 2 实验框架：多模型 × 多任务 × 多方法的 CSS circuit discovery。

复用 run_circus.py 的 pipeline + analyze_mvp_results.py 的分析，
支持配置化批量实验。

Usage:
    python run_phase2_experiment.py --config phase2_configs.yaml --experiment gpt2_ioi
    python run_phase2_experiment.py --config phase2_configs.yaml --all
    python run_phase2_experiment.py --config phase2_configs.yaml --priority 2
    python run_phase2_experiment.py --list  # 列出所有候选实验
    python run_phase2_experiment.py --status  # 查看已完成/待运行状态
"""

import os
# GPU guard: 必须在 torch import 之前设置 (D007)
_GPU_ID = os.environ.get("CUDA_VISIBLE_DEVICES", "5")
os.environ["CUDA_VISIBLE_DEVICES"] = _GPU_ID

import argparse
import hashlib
import json
import logging
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Set

import yaml

CANONICAL_VERSION = "v2"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("phase2")


# ---------------------------------------------------------------------------
# Config dataclasses
# ---------------------------------------------------------------------------

@dataclass
class ExperimentConfig:
    """单个实验的配置。"""
    name: str
    model: str
    task: str
    methods: List[str]
    backend: str  # "transformerlens" | "huggingface"
    priority: int = 3
    model_path: Optional[str] = None
    K: int = 3
    num_samples: int = 50
    gpu_id: str = "0"
    seed: int = 42
    eap_ig_steps: int = 5
    edge_pruning_epochs: int = 100
    edge_pruning_lambda: float = 1e-2
    ifr_threshold: float = 0.1
    css_threshold: float = 0.67
    circus_B: int = 10
    binarize: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    thresholds: Dict[str, List[float]] = field(default_factory=dict)
    notes: str = ""

    def __post_init__(self):
        if not self.binarize:
            self.binarize = {
                "eap_ig": {"strategy": "topn", "n": 200},
                "edge_pruning": {"strategy": "topn", "n": 200},
                "ifr": {"strategy": "unique_score_rank", "n": 50},  # D010
                "acdc": {"strategy": "threshold", "threshold": 0.05},
            }

    @property
    def model_slug(self) -> str:
        return self.model.replace("/", "_").replace("-", "_")

    @property
    def output_dir(self) -> Path:
        return Path("results") / f"{self.model_slug}_{self.task}"

    @property
    def cache_dir(self) -> Path:
        return Path("cache") / self.model_slug / self.task

    def to_run_circus_config(self) -> Dict[str, Any]:
        """转换为 run_circus.py 的 config dict 格式。"""
        cfg = {
            "model": self.model_path or self.model,
            "task": self.task,
            "methods": self.methods,
            "K": self.K,
            "num_samples": self.num_samples,
            "gpu_id": self.gpu_id,
            "seed": self.seed,
            "eap_ig_steps": self.eap_ig_steps,
            "edge_pruning_epochs": self.edge_pruning_epochs,
            "edge_pruning_lambda": self.edge_pruning_lambda,
            "ifr_threshold": self.ifr_threshold,
            "css_threshold": self.css_threshold,
            "circus_B": self.circus_B,
            "binarize": {m: v for m, v in self.binarize.items() if m in self.methods},
            "device": "cuda",
            "output_dir": str(self.output_dir),
            "cache_dir": str(self.cache_dir),
        }
        return cfg


# ---------------------------------------------------------------------------
# Config loading
# ---------------------------------------------------------------------------

def load_experiment_matrix(config_path: str) -> Dict[str, ExperimentConfig]:
    """从 YAML 加载实验矩阵。"""
    path = Path(config_path)
    if not path.exists():
        raise FileNotFoundError(f"Config not found: {config_path}")

    with open(path) as f:
        raw = yaml.safe_load(f)

    defaults = raw.get("defaults", {})
    experiments = {}

    for name, exp_cfg in raw.get("experiments", {}).items():
        merged = {**defaults, **exp_cfg}
        experiments[name] = ExperimentConfig(name=name, **merged)

    return experiments


def list_experiments(experiments: Dict[str, ExperimentConfig]) -> None:
    """打印实验列表。"""
    by_priority: Dict[int, List[ExperimentConfig]] = {}
    for exp in experiments.values():
        by_priority.setdefault(exp.priority, []).append(exp)

    for pri in sorted(by_priority):
        label = {1: "MVP (已跑/在跑)", 2: "MVP 后立即跑", 3: "有空再跑"}.get(pri, f"P{pri}")
        print(f"\n=== Priority {pri}: {label} ===")
        for exp in sorted(by_priority[pri], key=lambda e: e.name):
            methods_str = ", ".join(exp.methods)
            print(f"  {exp.name:30s}  {exp.model:30s}  {exp.task:15s}  [{methods_str}]")

    total = len(experiments)
    counts = {p: len(exps) for p, exps in by_priority.items()}
    print(f"\nTotal: {total} experiments | " + " | ".join(f"P{p}={c}" for p, c in sorted(counts.items())))


# ---------------------------------------------------------------------------
# Cache management
# ---------------------------------------------------------------------------

def _cache_key(exp: ExperimentConfig, method: str) -> str:
    """生成缓存文件名，绑定 CANONICAL_VERSION + 超参哈希。"""
    params = {
        "model": exp.model,
        "task": exp.task,
        "method": method,
        "num_samples": exp.num_samples,
        "seed": exp.seed,
    }
    if method == "eap_ig":
        params["steps"] = exp.eap_ig_steps
    elif method == "edge_pruning":
        params["epochs"] = exp.edge_pruning_epochs
        params["lambda"] = exp.edge_pruning_lambda
    elif method == "ifr":
        params["threshold"] = exp.ifr_threshold
    elif method == "acdc":
        params["thresholds"] = exp.thresholds.get("acdc", [0.05])

    h = hashlib.md5(json.dumps(params, sort_keys=True).encode()).hexdigest()[:16]
    return f"{method}_{CANONICAL_VERSION}_{h}.json"


def check_cache(exp: ExperimentConfig) -> Dict[str, bool]:
    """检查每个方法的缓存状态。"""
    status = {}
    for method in exp.methods:
        cache_file = exp.cache_dir / _cache_key(exp, method)
        status[method] = cache_file.exists()
    return status


def load_cached_scores(exp: ExperimentConfig, method: str) -> Optional[Dict[str, float]]:
    """加载已缓存的 edge scores。"""
    cache_file = exp.cache_dir / _cache_key(exp, method)
    if not cache_file.exists():
        return None
    with open(cache_file) as f:
        data = json.load(f)
    if data.get("canonical_version") != CANONICAL_VERSION:
        logger.warning("Cache version mismatch for %s/%s, will recompute", exp.name, method)
        return None
    return data.get("scores", {})


def save_cached_scores(exp: ExperimentConfig, method: str, scores: Dict[str, float]) -> None:
    """保存 edge scores 到缓存。"""
    exp.cache_dir.mkdir(parents=True, exist_ok=True)
    cache_file = exp.cache_dir / _cache_key(exp, method)
    data = {
        "canonical_version": CANONICAL_VERSION,
        "model": exp.model,
        "task": exp.task,
        "method": method,
        "n_edges": len(scores),
        "scores": scores,
    }
    with open(cache_file, "w") as f:
        json.dump(data, f, indent=2)
    logger.info("Cached %d edges → %s", len(scores), cache_file)


# ---------------------------------------------------------------------------
# Experiment runner
# ---------------------------------------------------------------------------

def run_single_experiment(exp: ExperimentConfig, force: bool = False) -> Dict[str, Any]:
    """运行单个实验：调用 run_circus pipeline，支持断点续跑。

    Returns:
        run_circus.run_pipeline() 的完整输出 dict，包含
        method_edge_counts, css_distribution, cross_table 等。
    """
    logger.info("=" * 60)
    logger.info("Starting experiment: %s", exp.name)
    logger.info("  Model: %s (%s backend)", exp.model, exp.backend)
    logger.info("  Task: %s | Methods: %s | K=%d", exp.task, exp.methods, exp.K)
    logger.info("=" * 60)

    # 断点续跑：检查哪些方法已有缓存
    cache_status = check_cache(exp)
    if not force:
        cached = [m for m, done in cache_status.items() if done]
        pending = [m for m, done in cache_status.items() if not done]
        if cached:
            logger.info("Cached methods (skip): %s", cached)
        if not pending:
            logger.info("All methods cached, running CSS/CIRCUS aggregation only")
    else:
        pending = exp.methods
        logger.info("Force mode: recomputing all methods")

    # 构建 run_circus config
    circus_cfg = exp.to_run_circus_config()
    exp.output_dir.mkdir(parents=True, exist_ok=True)

    # 调用 run_circus pipeline
    # TODO: 当前直接调用 run_pipeline，未来可拆分为：
    #   1. run_methods_only(circus_cfg, skip=cached) → 仅跑 scoring
    #   2. run_aggregation(circus_cfg, all_scores) → CSS + CIRCUS + cross-tab
    # 以支持更细粒度的断点续跑
    try:
        from run_circus import run_pipeline
        results = run_pipeline(config=circus_cfg)
    except ImportError:
        logger.error("run_circus.py not found in sys.path. Add artifacts/ to PYTHONPATH.")
        raise
    except Exception as e:
        logger.error("Experiment %s failed: %s", exp.name, e)
        raise

    # 保存实验元信息
    meta = {
        "experiment_name": exp.name,
        "priority": exp.priority,
        "backend": exp.backend,
        "canonical_version": CANONICAL_VERSION,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
    }
    results["phase2_meta"] = meta

    output_file = exp.output_dir / f"{exp.model_slug}_{exp.task}_K{exp.K}.json"
    with open(output_file, "w") as f:
        json.dump(results, f, indent=2, default=str)
    logger.info("Results → %s", output_file)

    return results


def run_analysis_for_experiment(exp: ExperimentConfig) -> Optional[Dict[str, Any]]:
    """实验完成后调用 analyze_mvp_results 的分析逻辑。"""
    try:
        from analyze_mvp_results import run_analysis
    except ImportError:
        logger.warning("analyze_mvp_results.py not importable, skipping analysis")
        return None

    analysis_dir = exp.output_dir / "analysis"
    analysis_dir.mkdir(parents=True, exist_ok=True)

    # run_analysis 从 cache dir 加载 per-method scores
    results = run_analysis(
        results_dir=exp.cache_dir.parent.parent,  # results/ 根
        output_dir=analysis_dir,
        top_n=200,
    )
    logger.info("Analysis → %s", analysis_dir)
    return results


# ---------------------------------------------------------------------------
# Batch runner
# ---------------------------------------------------------------------------

def run_batch(
    experiments: Dict[str, ExperimentConfig],
    names: Optional[List[str]] = None,
    max_priority: Optional[int] = None,
    force: bool = False,
) -> Dict[str, Dict[str, Any]]:
    """批量运行实验。

    Args:
        experiments: 完整实验矩阵
        names: 指定运行的实验名（None=全部）
        max_priority: 只运行 priority <= 此值的实验
        force: 忽略缓存，强制重算
    """
    selected = _select_experiments(experiments, names, max_priority)

    # 按 priority 排序
    ordered = sorted(selected.values(), key=lambda e: (e.priority, e.name))
    logger.info("Running %d experiments (sorted by priority)", len(ordered))

    all_results = {}
    for i, exp in enumerate(ordered, 1):
        logger.info("[%d/%d] %s (priority=%d)", i, len(ordered), exp.name, exp.priority)
        t0 = time.time()

        try:
            results = run_single_experiment(exp, force=force)
            analysis = run_analysis_for_experiment(exp)
            if analysis:
                results["analysis"] = analysis

            elapsed = time.time() - t0
            results["elapsed_sec"] = elapsed
            all_results[exp.name] = results
            logger.info("✓ %s completed in %.1f sec", exp.name, elapsed)

        except Exception as e:
            logger.error("✗ %s failed: %s", exp.name, e)
            all_results[exp.name] = {"error": str(e)}

    _save_batch_summary(all_results)
    return all_results


def _select_experiments(
    experiments: Dict[str, ExperimentConfig],
    names: Optional[List[str]] = None,
    max_priority: Optional[int] = None,
) -> Dict[str, ExperimentConfig]:
    """筛选实验子集。"""
    selected = experiments
    if names:
        missing = set(names) - set(experiments)
        if missing:
            raise ValueError(f"Unknown experiments: {missing}")
        selected = {n: experiments[n] for n in names}
    if max_priority is not None:
        selected = {n: e for n, e in selected.items() if e.priority <= max_priority}
    if not selected:
        raise ValueError("No experiments match the filter criteria")
    return selected


def _save_batch_summary(all_results: Dict[str, Dict[str, Any]]) -> None:
    """保存批量运行摘要。"""
    summary_path = Path("results") / "phase2_batch_summary.json"
    summary_path.parent.mkdir(parents=True, exist_ok=True)

    summary = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "canonical_version": CANONICAL_VERSION,
        "experiments": {},
    }
    for name, res in all_results.items():
        entry = {"status": "error" if "error" in res else "ok"}
        if "error" in res:
            entry["error"] = res["error"]
        else:
            entry["elapsed_sec"] = res.get("elapsed_sec")
            if "cross_table" in res:
                entry["off_diagonal_pct"] = res["cross_table"].get("off_diagonal_pct")
            if "css_distribution" in res:
                entry["css_distribution"] = res["css_distribution"]
        summary["experiments"][name] = entry

    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)
    logger.info("Batch summary → %s", summary_path)


# ---------------------------------------------------------------------------
# Status check
# ---------------------------------------------------------------------------

def show_status(experiments: Dict[str, ExperimentConfig]) -> None:
    """显示每个实验的完成状态。"""
    print(f"\n{'Experiment':30s} {'Model':25s} {'Task':12s} {'Cached Methods':40s} {'Result'}")
    print("-" * 120)

    for name in sorted(experiments, key=lambda n: (experiments[n].priority, n)):
        exp = experiments[name]
        cache = check_cache(exp)
        cached_str = " ".join(f"{'✓' if v else '✗'}{m}" for m, v in cache.items())

        result_file = exp.output_dir / f"{exp.model_slug}_{exp.task}_K{exp.K}.json"
        result_str = "✓" if result_file.exists() else "—"

        print(f"  P{exp.priority} {name:28s} {exp.model:25s} {exp.task:12s} {cached_str:40s} {result_str}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Phase 2 experiment runner")
    parser.add_argument("--config", type=str, default="phase2_configs.yaml",
                        help="实验矩阵 YAML 路径")
    parser.add_argument("--experiment", type=str, nargs="+",
                        help="运行指定实验（空格分隔多个）")
    parser.add_argument("--all", action="store_true",
                        help="运行全部实验")
    parser.add_argument("--priority", type=int,
                        help="只运行 priority <= N 的实验")
    parser.add_argument("--list", action="store_true",
                        help="列出所有实验")
    parser.add_argument("--status", action="store_true",
                        help="显示完成状态")
    parser.add_argument("--force", action="store_true",
                        help="忽略缓存强制重算")
    parser.add_argument("--gpu", type=str, default=None,
                        help="覆盖 CUDA_VISIBLE_DEVICES")
    return parser.parse_args()


def main():
    args = parse_args()

    if args.gpu:
        os.environ["CUDA_VISIBLE_DEVICES"] = args.gpu
        logger.info("GPU override: CUDA_VISIBLE_DEVICES=%s", args.gpu)

    experiments = load_experiment_matrix(args.config)

    if args.list:
        list_experiments(experiments)
        return

    if args.status:
        show_status(experiments)
        return

    if args.experiment:
        run_batch(experiments, names=args.experiment, force=args.force)
    elif args.all:
        run_batch(experiments, max_priority=args.priority, force=args.force)
    elif args.priority:
        run_batch(experiments, max_priority=args.priority, force=args.force)
    else:
        parser = argparse.ArgumentParser()
        parser.print_help()
        print("\nHint: use --list to see experiments, --experiment NAME to run one")


if __name__ == "__main__":
    main()
