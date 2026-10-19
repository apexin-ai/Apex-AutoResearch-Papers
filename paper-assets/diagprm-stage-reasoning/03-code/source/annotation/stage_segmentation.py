"""Stage segmentation: label each trajectory step as localize/diagnose/patch/other.

Uses LLM judge (Claude or GPT-4o). Supports --dry-run mock mode.
Input: Trajectory object.
Output: list[StageLabel] with per-step stage + reasoning.
"""

import json
import random
from dataclasses import dataclass
from typing import Optional

from .data_loader import Trajectory

STAGES = ["localize", "diagnose", "patch", "other"]

SEGMENTATION_PROMPT = """\
You are an expert code repair analyst. Given a trajectory of steps from an automated code repair agent, classify each step into one of four cognitive stages:

**Stages:**
- **localize**: Searching files, grepping code, reading source, analyzing error messages/stack traces — any action aimed at finding WHERE the bug is.
- **diagnose**: Analyzing root cause, reasoning about WHY the code fails, forming hypotheses about what's wrong, comparing expected vs actual behavior.
- **patch**: Writing or modifying code, generating diffs, applying fixes, creating new files as part of a solution.
- **other**: Environment setup, unrelated discussion, test execution without analysis, or actions that don't fit the above.

**Rules:**
- Steps can interleave stages (e.g., localize -> diagnose -> localize -> patch is normal).
- If a step contains both reading code AND reasoning about cause, prefer the dominant activity.
- Tool/system responses inherit the stage of the preceding assistant action.

**Output:** Return ONLY a JSON array (no markdown fences):
[{{"step_index": 0, "stage": "localize", "reasoning": "brief explanation"}}, ...]

**Trajectory steps:**
{steps_text}"""


@dataclass
class StageLabel:
    step_index: int
    stage: str
    reasoning: str


def _format_steps(trajectory: Trajectory) -> str:
    parts = []
    for s in trajectory.steps:
        content_preview = s.content[:500] if s.content else "(empty)"
        tc = f" [tool_calls: {len(s.tool_calls)}]" if s.tool_calls else ""
        parts.append(f"Step {s.index} [{s.role}]{tc}:\n{content_preview}")
    return "\n---\n".join(parts)


def _parse_judge_response(response_text: str) -> list[StageLabel]:
    """Parse JSON array from judge response."""
    text = response_text.strip()
    if "```" in text:
        for block in text.split("```"):
            block = block.strip()
            if block.startswith("json"):
                block = block[4:].strip()
            if block.startswith("["):
                text = block
                break

    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        start = text.find("[")
        end = text.rfind("]")
        if start != -1 and end != -1:
            data = json.loads(text[start : end + 1])
        else:
            raise ValueError(f"Could not parse JSON from response: {text[:200]}")

    return [
        StageLabel(
            step_index=item["step_index"],
            stage=item["stage"],
            reasoning=item.get("reasoning", ""),
        )
        for item in data
    ]


def _mock_segmentation(trajectory: Trajectory, seed: Optional[int] = None) -> list[StageLabel]:
    """Simulate realistic stage progression for dry-run."""
    rng = random.Random(seed)
    labels = []
    n = len(trajectory.steps)
    for s in trajectory.steps:
        progress = s.index / max(n - 1, 1)
        if progress < 0.35:
            weights = [0.6, 0.2, 0.05, 0.15]
        elif progress < 0.65:
            weights = [0.15, 0.5, 0.2, 0.15]
        else:
            weights = [0.05, 0.15, 0.65, 0.15]
        stage = rng.choices(STAGES, weights=weights, k=1)[0]
        labels.append(StageLabel(
            step_index=s.index, stage=stage,
            reasoning=f"mock: progress={progress:.2f}",
        ))
    return labels


def segment_trajectory(
    trajectory: Trajectory,
    judge: str = "claude",
    dry_run: bool = False,
) -> list[StageLabel]:
    """Segment a trajectory into cognitive stages.

    Args:
        trajectory: The trajectory to segment.
        judge: "claude" or "gpt4o".
        dry_run: If True, return mock labels without calling API.
    """
    if dry_run:
        return _mock_segmentation(
            trajectory, seed=hash((trajectory.instance_id, judge)) % 2**31
        )

    prompt = SEGMENTATION_PROMPT.format(steps_text=_format_steps(trajectory))

    if judge == "claude":
        import anthropic
        client = anthropic.Anthropic()
        resp = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            messages=[{"role": "user", "content": prompt}],
        )
        response_text = resp.content[0].text
    elif judge == "gpt4o":
        import openai
        client = openai.OpenAI()
        resp = client.chat.completions.create(
            model="gpt-4o",
            max_tokens=4096,
            messages=[{"role": "user", "content": prompt}],
        )
        response_text = resp.choices[0].message.content
    else:
        raise ValueError(f"Unknown judge: {judge}")

    return _parse_judge_response(response_text)
