# Shared utilities: logging, seeding, data I/O.

import json
import logging
import random
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict

import numpy as np


def setup_logging(name: str = "cert_eval", level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(
            logging.Formatter("[%(asctime)s %(levelname)s] %(name)s: %(message)s", datefmt="%H:%M:%S")
        )
        logger.addHandler(handler)
    logger.setLevel(level)
    return logger


def set_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    try:
        import torch
        torch.manual_seed(seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(seed)
    except ImportError:
        pass


def save_results(data: Any, path: Path, tag: str = "") -> Path:
    """Save dict/list to timestamped JSON."""
    path.parent.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    suffix = f"_{tag}" if tag else ""
    out_path = path / f"results{suffix}_{ts}.json"
    with open(out_path, "w") as f:
        json.dump(data, f, indent=2, default=str)
    return out_path


def load_results(path: Path) -> Dict:
    with open(path) as f:
        return json.load(f)


def timestamp_str() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
