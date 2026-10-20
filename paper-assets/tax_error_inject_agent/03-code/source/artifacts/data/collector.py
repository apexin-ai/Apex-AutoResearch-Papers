"""
TaxEI Trajectory Collector
==========================
Collects successful trajectories from ALFWorld using GPT-4o rollouts.
Expected: ~93% zero-shot success rate, ~17 steps/trajectory.

Output format (JSON per trajectory):
{
    "task_type": str,
    "task_description": str,
    "gamefile": str,
    "steps": [{"observation": str, "action": str, "think": str}],
    "success": bool,
    "num_steps": int
}
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional


class TrajectoryCollector:
    """Collect ALFWorld trajectories via GPT-4o rollout."""

    def __init__(
        self,
        api_key: [REDACTED] = None,
        model: str = "gpt-4o",
        max_steps: int = 50,
    ):
        self.api_key = [REDACTED]
        self.model = model
        self.max_steps = max_steps

    def collect(
        self,
        num_trajectories: int,
        task_types: Optional[List[str]] = None,
        output_path: str = "trajectories.json",
    ) -> List[Dict[str, Any]]:
        """Collect successful trajectories.

        Args:
            num_trajectories: target number of *successful* trajectories.
            task_types: ALFWorld task types to sample from.
                        None = all 6 types (pick, clean, heat, cool, examine, puttwo).
            output_path: where to write the JSON output.
        """
        if task_types is None:
            task_types = ["pick", "clean", "heat", "cool", "examine", "puttwo"]

        trajectories: List[Dict[str, Any]] = []

        # TODO: 等 API key — 以下为 rollout 伪代码
        # env = self._make_env(task_types)
        # while len(trajectories) < num_trajectories:
        #     obs, info = env.reset()
        #     steps = []
        #     for t in range(self.max_steps):
        #         prompt = self._build_prompt(obs, steps)
        #         response = self._call_llm(prompt)  # TODO: 等 API key
        #         think, action = self._parse_response(response)
        #         steps.append({"observation": obs, "action": action, "think": think})
        #         obs, reward, done, info = env.step(action)
        #         if done:
        #             break
        #     if info.get("success", False):
        #         trajectories.append({
        #             "task_type": info["task_type"],
        #             "task_description": info["task_desc"],
        #             "gamefile": info.get("gamefile", ""),
        #             "steps": steps,
        #             "success": True,
        #             "num_steps": len(steps),
        #         })

        if trajectories:
            Path(output_path).write_text(
                json.dumps(trajectories, indent=2, ensure_ascii=False)
            )

        return trajectories

    def _build_prompt(self, observation: str, history: List[Dict]) -> str:
        """Build the LLM prompt with current observation and history."""
        # TODO: 等 API key
        lines = []
        for i, step in enumerate(history, 1):
            lines.append(f"[Step {i}] Obs: {step['observation']}")
            lines.append(f"[Step {i}] Act: {step['action']}")
        lines.append(f"[Current] Obs: {observation}")
        lines.append("What is your next action? Think step by step, then output the action.")
        return "\n".join(lines)

    def _call_llm(self, prompt: str) -> str:
        """Call GPT-4o for action generation."""
        # TODO: 等 API key
        raise NotImplementedError("API key not configured")

    def _parse_response(self, response: str):
        """Extract think and action from LLM response."""
        # TODO: 等 API key
        return "", ""
