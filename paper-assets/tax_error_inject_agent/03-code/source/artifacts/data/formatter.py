"""
TaxEI SFT Data Formatter
=========================
Converts raw + injected ALFWorld trajectories into ms-swift multi-turn SFT format.

ms-swift format:
{"messages": [
    {"role": "user", "content": "<observation>"},
    {"role": "assistant", "content": "<think>...</think>\n<action>...</action>"},
    ...
]}

Each ALFWorld step becomes one user-assistant turn.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional


def format_for_sft(
    trajectories: List[Dict[str, Any]],
    injected_trajectories: Optional[List[Dict[str, Any]]] = None,
    output_path: str = "sft_data.jsonl",
) -> List[Dict[str, Any]]:
    """Convert trajectories to ms-swift multi-turn SFT format.

    Args:
        trajectories: original successful trajectories (from collector).
        injected_trajectories: trajectories with injected errors.
            Each entry should have an extra "injection_info" field.
        output_path: output JSONL path.

    Returns:
        list of ms-swift formatted examples.
    """
    all_trajs = list(trajectories)
    if injected_trajectories:
        all_trajs.extend(injected_trajectories)

    formatted: List[Dict[str, Any]] = []

    for traj in all_trajs:
        messages: List[Dict[str, str]] = []
        steps = traj.get("steps", [])

        # First turn: task description as system-like user message
        task_desc = traj.get("task_description", "") or traj.get("task_desc", "")
        if task_desc:
            messages.append({"role": "user", "content": task_desc})

        for step in steps:
            obs = step.get("observation", "")
            think = step.get("think", "")
            action = step.get("action", "")

            messages.append({"role": "user", "content": obs})

            assistant_parts = []
            if think:
                assistant_parts.append(f"<think>{think}</think>")
            if action:
                assistant_parts.append(f"<action>{action}</action>")
            messages.append({
                "role": "assistant",
                "content": "\n".join(assistant_parts) if assistant_parts else action,
            })

        if messages:
            formatted.append({"messages": messages})

    for item in formatted:
        for msg in item.get("messages", []):
            content = msg.get("content", "")
            if "[DRY_RUN]" in content:
                raise ValueError(
                    f"DRY_RUN placeholder detected in SFT data. "
                    f"Use non-dry-run mode to generate real recovery demonstrations. "
                    f"Content: {content[:100]}"
                )
            if "API_ERROR" in content or "Error code:" in content:
                raise ValueError(
                    f"API error content detected in SFT data. "
                    f"Content: {content[:100]}"
                )

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        for item in formatted:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")

    return formatted
