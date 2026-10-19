"""Data loader for SWE-bench/SWE-smith trajectories.

Reads JSONL, auto-detects field names (trajectory/messages/history),
returns unified Trajectory/Step dataclasses.
"""

import json
import random
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Step:
    index: int
    role: str
    content: str
    tool_calls: list = field(default_factory=list)


@dataclass
class Trajectory:
    instance_id: str
    steps: list[Step]
    resolved: bool
    metadata: dict = field(default_factory=dict)


_STEP_FIELD_NAMES = ["trajectory", "messages", "history"]
_RESOLVED_FIELD_NAMES = ["resolved", "is_resolved", "success"]


def _extract_steps(record: dict) -> list[Step]:
    """Auto-detect step field and parse into Step objects."""
    raw = None
    for name in _STEP_FIELD_NAMES:
        if name in record:
            raw = record[name]
            break
    if raw is None:
        raise ValueError(
            f"No step field found. Tried: {_STEP_FIELD_NAMES}. Keys: {list(record.keys())}"
        )

    steps = []
    for i, item in enumerate(raw):
        if isinstance(item, dict):
            role = item.get("role", "unknown")
            content = item.get("content", "") or ""
            tool_calls = item.get("tool_calls", []) or []
        elif isinstance(item, str):
            role = "assistant"
            content = item
            tool_calls = []
        else:
            continue
        steps.append(Step(index=i, role=role, content=content, tool_calls=tool_calls))
    return steps


def _extract_resolved(record: dict) -> bool:
    """Auto-detect resolved field."""
    for name in _RESOLVED_FIELD_NAMES:
        if name in record:
            return bool(record[name])
    return False


def load_trajectories(
    path: str, sample_size: Optional[int] = None
) -> list[Trajectory]:
    """Load trajectories from JSONL.

    Args:
        path: Path to JSONL file.
        sample_size: Randomly sample N trajectories (seed=42 for reproducibility).
    """
    trajectories = []
    skip_keys = {
        "instance_id", "id", "trajectory", "messages", "history",
        "resolved", "is_resolved", "success",
    }
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            record = json.loads(line)
            instance_id = record.get("instance_id", record.get("id", f"unknown_{len(trajectories)}"))
            steps = _extract_steps(record)
            resolved = _extract_resolved(record)
            metadata = {k: v for k, v in record.items() if k not in skip_keys}
            trajectories.append(Trajectory(
                instance_id=str(instance_id),
                steps=steps,
                resolved=resolved,
                metadata=metadata,
            ))

    if sample_size is not None and sample_size < len(trajectories):
        rng = random.Random(42)
        trajectories = rng.sample(trajectories, sample_size)

    return trajectories
