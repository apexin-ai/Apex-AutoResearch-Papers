#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import time
from pathlib import Path
from typing import Any

import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from _budget_agent_common import (
    AGENT_LABEL,
    MODEL_PATH,
    RESULT_FILE_AGENT_NAME,
    ROOT,
    decide_config,
    dump_json,
    load_manifest_record,
    maybe_dry_run,
    result_root,
    run_shell,
    utc_now,
)


TASK_ID = "torch_conv_kan_cifar10"
RESULT_DIRNAME = "torch_conv_kan_cifar10"
REPO_DIR = ROOT / "repositories/torch-conv-kan"
DATA_ROOT = ROOT / "data/paper_exact/torch_conv_kan_cifar10"
BASE_CONFIG = {
    "learning_rate": 0.0005,
    "batch_size": 128,
    "weight_decay": 0.0001,
    "label_smoothing": 0.05,
}
SEARCH_SPACE = {
    "learning_rate": [5e-05, 0.0002, 0.0005, 0.001, 0.002],
    "batch_size": [64, 128, 256],
    "weight_decay": [0.0, 0.0001, 0.001],
    "label_smoothing": [0.0, 0.05, 0.1],
}
import os as _space_os
import sys as _space_sys
from pathlib import Path as _SpacePath
_space_sys.path.insert(0, str(_SpacePath(__file__).resolve().parents[1]))
from space_ablation_backend_full30 import apply_space_variant as _apply_space_variant
SEARCH_SPACE = _apply_space_variant(
    "torch_conv_kan_cifar10", SEARCH_SPACE, BASE_CONFIG, _space_os.environ.get("AUTOREP_SPACE_VARIANT", "original")
)

ALIASES = {
    "lr": "learning_rate",
    "train_batch_size": "batch_size",
    "adam_weight_decay": "weight_decay",
    "wd": "weight_decay",
}



def _apply_experiment_seed() -> None:
    raw_seed = os.environ.get("AUTOREP_PROCESS_SEED")
    if raw_seed is None:
        return
    seed = int(raw_seed)
    import random
    random.seed(seed)
    try:
        import numpy as np
        np.random.seed(seed % (2**32 - 1))
    except Exception:
        pass
    try:
        import torch
        torch.manual_seed(seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(seed)
    except Exception:
        pass


_apply_experiment_seed()

def ensure_data_link() -> None:
    if not DATA_ROOT.exists():
        raise FileNotFoundError(DATA_ROOT)
    repo_data = REPO_DIR / "data"
    if (repo_data / "cifar-10-batches-py").exists():
        return
    if repo_data.exists() or repo_data.is_symlink():
        if repo_data.is_symlink() or not any(repo_data.iterdir()):
            repo_data.unlink() if repo_data.is_symlink() else repo_data.rmdir()
        else:
            raise RuntimeError(f"non-empty data directory is not CIFAR-10: {repo_data}")
    repo_data.symlink_to(DATA_ROOT)


def parse_wandb_run(run_file: Path) -> dict[str, Any]:
    from wandb.proto import wandb_internal_pb2
    from wandb.sdk.internal.datastore import DataStore

    store = DataStore()
    store.open_for_scan(str(run_file))
    last: dict[str, Any] = {}
    rows = 0
    while True:
        data = store.scan_data()
        if data is None:
            break
        record = wandb_internal_pb2.Record()
        record.ParseFromString(data)
        if record.history.item:
            rows += 1
            for item in record.history.item:
                key = item.key or "/".join(item.nested_key)
                if item.value_json:
                    try:
                        last[key] = json.loads(item.value_json)
                    except Exception:
                        last[key] = item.value_json
    interesting = {
        "accuracy": last.get("accuracy"),
        "accuracy_top5": last.get("accuracy, top5"),
        "loss": last.get("loss"),
        "lr": last.get("lr"),
        "f1_score_macro": last.get("f1_score, macro"),
        "train_acc": last.get("train_acc"),
        "train_acc_top5": last.get("train_acc_top5"),
    }
    return {"history_rows": rows, "path": str(run_file), "metrics": {k: v for k, v in interesting.items() if v is not None}}


def newest_wandb_file(wandb_dir: Path) -> Path:
    candidates = sorted(wandb_dir.glob("**/run-*.wandb"), key=lambda p: p.stat().st_mtime)
    if not candidates:
        raise FileNotFoundError(f"no wandb run found under {wandb_dir}")
    return candidates[-1]


def training_log(manifest: dict[str, Any]) -> str:
    return "\n".join(
        [
            "Task: CIFAR-10 classification with torch-conv-kan ResKANet.",
            "Metric: accuracy_percent, higher is better.",
            f"Official shortened budget baseline: {manifest.get('official_budget_baseline', 28.97)} percent at 10 epochs.",
            f"Paper anchor: {manifest.get('paper_anchor', 84.17)} percent.",
            f"Current baseline config: {BASE_CONFIG}.",
            "Choose one configuration for a single 10-epoch budget run.",
        ]
    )


def main() -> int:
    if not REPO_DIR.exists():
        raise FileNotFoundError(REPO_DIR)
    manifest = load_manifest_record(TASK_ID)
    epochs = int(os.environ.get("TORCH_CONV_KAN_EPOCHS", "10"))
    run_id = os.environ.get("RUN_ID") or f"{TASK_ID}_{AGENT_LABEL.lower().replace('-', '_')}_{epochs}ep_{utc_now().replace(':', '').replace('+', '_')}"
    result_dir = result_root(RESULT_DIRNAME)
    run_dir = result_dir / "runs" / run_id
    output_dir = run_dir / "outputs"
    logging_dir = run_dir / "train_logs"
    wandb_dir = run_dir / "wandb"
    result_file = result_dir / f"{TASK_ID}_{RESULT_FILE_AGENT_NAME}_results.json"
    maybe_dry_run({"task_id": TASK_ID, "run_id": run_id, "epochs": epochs, "result_file": str(result_file)})

    ensure_data_link()
    decision = decide_config(
        task_name=TASK_ID,
        current_config=BASE_CONFIG,
        search_space=SEARCH_SPACE,
        aliases=ALIASES,
        training_log=training_log(manifest),
        budget_remaining=1,
        total_budget=1,
        decision_number=0,
    )
    config = decision["new_config"]

    env = os.environ.copy()
    env["CUDA_VISIBLE_DEVICES"] = os.environ.get("TORCH_CONV_KAN_CUDA_VISIBLE_DEVICES", env.get("CUDA_VISIBLE_DEVICES", "1"))
    env["WANDB_MODE"] = "offline"
    env["WANDB_DIR"] = str(wandb_dir)
    existing_pythonpath = [
        item
        for item in env.get("PYTHONPATH", "").split(":")
        if item and item != str(ROOT / ".python_deps")
    ]
    env["PYTHONPATH"] = ":".join([str(ROOT), *existing_pythonpath])
    output_dir.mkdir(parents=True, exist_ok=True)
    logging_dir.mkdir(parents=True, exist_ok=True)
    wandb_dir.mkdir(parents=True, exist_ok=True)
    started = time.time()
    cmd = " ".join(
        [
            "source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh",
            "&& conda activate autorep-vlm2vec",
            "&& accelerate launch cifar.py",
            f"output_dir={output_dir}",
            f"logging_dir={logging_dir}",
            f"epochs={epochs}",
            f"train_batch_size={config['batch_size']}",
            "val_batch_size=256",
            f"dataloader_num_workers={os.environ.get('TORCH_CONV_KAN_NUM_WORKERS', '8')}",
            f"optim.learning_rate={config['learning_rate']}",
            f"optim.adam_weight_decay={config['weight_decay']}",
            f"loss.label_smoothing={config['label_smoothing']}",
            "+save_checkpoints=false",
        ]
    )
    seconds = run_shell(cmd, cwd=REPO_DIR, env=env, log_path=run_dir / "train.log")
    wandb_payload = parse_wandb_run(newest_wandb_file(wandb_dir))
    metrics = wandb_payload["metrics"]
    if "accuracy" not in metrics:
        raise RuntimeError(f"missing accuracy in wandb metrics: {wandb_payload}")
    accuracy_percent = float(metrics["accuracy"]) * 100.0
    payload = {
        "experiment_name": f"{TASK_ID}_{RESULT_FILE_AGENT_NAME}",
        "benchmark_name": TASK_ID,
        "agent_name": AGENT_LABEL,
        "agent_model": str(MODEL_PATH),
        "created_at": utc_now(),
        "success": True,
        "agent_success": True,
        "direction": "higher_is_better",
        "metric": "accuracy_percent",
        "agent_budget_result": accuracy_percent,
        "agent_final_config": config,
        "agent_decisions_made": 1,
        "agent_internal_baseline": manifest.get("secondary_metrics", {}).get("accuracy"),
        "official_budget_baseline": manifest.get("official_budget_baseline", 28.97),
        "paper_anchor": manifest.get("paper_anchor", 84.17),
        "decision": decision,
        "final_config": config,
        "final_metrics": metrics,
        "baseline_metrics": {"accuracy": manifest.get("official_budget_baseline", 28.97) / 100.0},
        "total_epochs": epochs,
        "total_time": round(time.time() - started, 3),
        "seconds": seconds,
        "wandb": wandb_payload,
        "run_dir": str(run_dir),
        "run_id": run_id,
    }
    dump_json(result_file, payload)
    print(result_file)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
