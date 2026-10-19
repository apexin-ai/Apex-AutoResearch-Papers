"""Quality assessment: evaluate reasoning quality (sound/flawed) for each cognitive stage.

Uses LLM judge with stage-specific evaluation criteria.
Input: Trajectory + stage labels from segmentation.
Output: QualityLabel per stage (binary sound/flawed + reasoning).
"""

import json
import random
from dataclasses import dataclass
from typing import Optional

from .data_loader import Trajectory
from .stage_segmentation import StageLabel

STAGE_CRITERIA = {
    "localize": (
        "Evaluate the LOCALIZATION reasoning:\n"
        "- Does the reasoning correctly connect error evidence (stack traces, test failures) to candidate locations?\n"
        "- Is the search strategy reasonable (not random grepping)?\n"
        "- Are the identified locations plausible given the evidence?"
    ),
    "diagnose": (
        "Evaluate the DIAGNOSIS reasoning:\n"
        "- Does the root cause hypothesis logically explain the observed failure?\n"
        "- Are obvious alternative explanations considered or at least not contradicted?\n"
        "- Is the causal chain from symptom to root cause coherent?"
    ),
    "patch": (
        "Evaluate the PATCH reasoning:\n"
        "- Does the fix logically follow from the diagnosis?\n"
        "- Could the fix plausibly introduce new bugs or regressions?\n"
        "- Does the fix address the root cause rather than just the symptom?"
    ),
}

ASSESSMENT_PROMPT = """\
You are an expert code repair analyst evaluating the quality of reasoning in one stage of a code repair trajectory.

**Context from prior stages:**
{prior_context}

**Stage being evaluated: {stage_name}**
{stage_criteria}

**Content of this stage (merged steps):**
{stage_content}

**Task:** Assess whether the reasoning in this stage is SOUND or FLAWED.
- "sound": The reasoning is logically valid, evidence-based, and leads to reasonable conclusions.
- "flawed": The reasoning contains logical errors, ignores key evidence, makes unsupported leaps, or reaches incorrect conclusions.

**Output** ONLY a JSON object (no markdown fences):
{{"assessment": "sound" or "flawed", "reasoning": "brief explanation (1-2 sentences)"}}"""


@dataclass
class QualityLabel:
    stage: str
    assessment: str
    reasoning: str


def _merge_stage_content(
    trajectory: Trajectory, labels: list[StageLabel], stage: str
) -> str:
    """Merge all steps belonging to a given stage."""
    stage_indices = {l.step_index for l in labels if l.stage == stage}
    parts = []
    for s in trajectory.steps:
        if s.index in stage_indices:
            content = s.content[:1000] if s.content else "(empty)"
            parts.append(f"[Step {s.index}, {s.role}]: {content}")
    return "\n".join(parts) if parts else "(no steps in this stage)"


def _get_prior_context(
    trajectory: Trajectory, labels: list[StageLabel], current_stage: str
) -> str:
    """Summarize prior stages as context for the current assessment."""
    stage_order = ["localize", "diagnose", "patch"]
    current_idx = stage_order.index(current_stage) if current_stage in stage_order else -1
    if current_idx <= 0:
        return "(this is the first stage)"

    parts = []
    for prev_stage in stage_order[:current_idx]:
        content = _merge_stage_content(trajectory, labels, prev_stage)
        if content != "(no steps in this stage)":
            parts.append(f"[{prev_stage.upper()}]: {content[:500]}")
    return "\n".join(parts) if parts else "(no prior stages)"


def _parse_assessment_response(response_text: str) -> dict:
    """Parse JSON object from judge response."""
    text = response_text.strip()
    if "```" in text:
        for block in text.split("```"):
            block = block.strip()
            if block.startswith("json"):
                block = block[4:].strip()
            if block.startswith("{"):
                text = block
                break
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        start = text.find("{")
        end = text.rfind("}")
        if start != -1 and end != -1:
            return json.loads(text[start : end + 1])
        raise ValueError(f"Could not parse JSON from response: {text[:200]}")


def _mock_assessment(
    stage: str, trajectory: Trajectory, seed: Optional[int] = None
) -> QualityLabel:
    """Mock assessment biased toward partially-good pattern (early=sound, late=flawed)."""
    rng = random.Random(seed)
    p_sound = {"localize": 0.75, "diagnose": 0.55, "patch": 0.35}.get(stage, 0.5)
    assessment = "sound" if rng.random() < p_sound else "flawed"
    return QualityLabel(
        stage=stage,
        assessment=assessment,
        reasoning=f"mock: {stage} assessed as {assessment}",
    )


def assess_stage(
    trajectory: Trajectory,
    labels: list[StageLabel],
    stage: str,
    judge: str = "claude",
    dry_run: bool = False,
) -> QualityLabel:
    """Assess quality of a single stage's reasoning.

    Args:
        trajectory: Full trajectory for context.
        labels: Stage labels from segmentation.
        stage: Which stage to assess ("localize", "diagnose", or "patch").
        judge: "claude" or "gpt4o".
        dry_run: If True, return mock assessment.
    """
    if dry_run:
        return _mock_assessment(
            stage, trajectory,
            seed=hash((trajectory.instance_id, stage, judge)) % 2**31,
        )

    prompt = ASSESSMENT_PROMPT.format(
        prior_context=_get_prior_context(trajectory, labels, stage),
        stage_name=stage.upper(),
        stage_criteria=STAGE_CRITERIA.get(stage, "Evaluate the reasoning quality."),
        stage_content=_merge_stage_content(trajectory, labels, stage),
    )

    if judge == "claude":
        import anthropic
        client = anthropic.Anthropic()
        resp = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}],
        )
        response_text = resp.content[0].text
    elif judge == "gpt4o":
        import openai
        client = openai.OpenAI()
        resp = client.chat.completions.create(
            model="gpt-4o",
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}],
        )
        response_text = resp.choices[0].message.content
    else:
        raise ValueError(f"Unknown judge: {judge}")

    data = _parse_assessment_response(response_text)
    return QualityLabel(
        stage=stage,
        assessment=data["assessment"],
        reasoning=data.get("reasoning", ""),
    )
