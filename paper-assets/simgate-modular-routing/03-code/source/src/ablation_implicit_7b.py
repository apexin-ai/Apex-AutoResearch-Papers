"""Condition (c): 7B Implicit Router — Qwen2.5-7B-Instruct tool-use prompt.

No training required. Uses the pre-trained 7B model's instruction-following
ability to decide routing via a tool-use interface.

The model is given a "simulate" tool in its system prompt. At each step:
  - If it calls simulate(action=...) → route = deterministic, fork_and_lookahead
  - If it outputs an action directly   → route = internal

This tests whether a larger model can match or beat a trained 1.7B router
by leveraging in-context reasoning about when simulation helps.

Reviewer W4 concern: 7B implicit vs 1.7B explicit confounds architecture with
capacity. This condition + Condition (b) disentangle the two factors:
  (a) 1.7B explicit — small model, classification head
  (b) 1.7B implicit — small model, inline generation  ← controls for capacity
  (c) 7B implicit  — large model, tool-use prompt      ← controls for formulation

Usage:
  python src/ablation_implicit_7b.py --task_types "boil,melt" --gpu_id 0
"""

import argparse
import json
import os
import re
import sys
from typing import List, Tuple, Dict, Any, Optional

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from llm_agent import LLMAgent, find_model_path

MODEL_ID = "Qwen/Qwen2.5-7B-Instruct"

# ---------------------------------------------------------------------------
# Tool-use system prompt
# ---------------------------------------------------------------------------

TOOL_USE_SYSTEM_PROMPT = """\
You are an agent in a ScienceWorld text environment. Your goal is to complete the given task by choosing actions.

You have access to one tool:

## simulate
Run a deterministic forward simulation to evaluate an action before committing.
Use this when:
- The action involves irreversible state changes (heating, mixing, combining)
- You are uncertain whether the action will lead to a dead end
- The task requires precise physical/chemical processes

Usage: To use the tool, write:
<tool_call>simulate(action="your chosen action")</tool_call>

If you are confident in your action (e.g., navigation, looking around, simple interactions), output the action directly WITHOUT using the tool:
Action: your chosen action

Rules:
- Choose actions from the valid actions list only.
- Use simulate() when the action could cause irreversible harm or when you need to verify outcomes.
- Output directly when the action is low-risk (moving, looking, opening containers).
"""

TOOL_USER_TEMPLATE = """\
Current observation:
{observation}

Valid actions:
{valid_actions_str}

Previous actions: {history_str}

Choose your next action. Use simulate() if you think deterministic evaluation would help, or output directly."""


# ---------------------------------------------------------------------------
# Output parsing
# ---------------------------------------------------------------------------

def parse_tool_use_output(text: str, valid_actions: List[str]) -> Tuple[str, str]:
    """Parse 7B model output for tool call or direct action.

    Returns (action, route_decision).
    route_decision ∈ {"deterministic", "internal"}
    """
    text = text.strip()

    # Pattern 1: tool_call tag
    tool_match = re.search(
        r'<tool_call>\s*simulate\(\s*action\s*=\s*["\'](.+?)["\']\s*\)\s*</tool_call>',
        text, re.DOTALL
    )
    if tool_match:
        action = tool_match.group(1).strip()
        action = _snap_to_valid(action, valid_actions)
        return action, "deterministic"

    # Pattern 2: simulate(...) without tags
    sim_match = re.search(
        r'simulate\(\s*action\s*=\s*["\'](.+?)["\']\s*\)',
        text, re.DOTALL
    )
    if sim_match:
        action = sim_match.group(1).strip()
        action = _snap_to_valid(action, valid_actions)
        return action, "deterministic"

    # Pattern 3: direct "Action: ..."
    action_match = re.search(r'Action:\s*(.+?)(?:\n|$)', text, re.IGNORECASE)
    if action_match:
        action = action_match.group(1).strip().strip('"').strip("'")
        action = _snap_to_valid(action, valid_actions)
        return action, "internal"

    # Fallback: try to match any valid action mentioned in the text
    for va in valid_actions:
        if va.lower() in text.lower():
            return va, "internal"

    return valid_actions[0] if valid_actions else "", "internal"


def _snap_to_valid(action: str, valid_actions: List[str]) -> str:
    """Snap a parsed action string to the closest valid action."""
    if action in valid_actions:
        return action
    action_lower = action.lower().strip()
    for va in valid_actions:
        if va.lower().strip() == action_lower:
            return va
    return valid_actions[0] if valid_actions else action


def _format_actions(actions: List[str], max_show: int = 50) -> str:
    if len(actions) <= max_show:
        return "\n".join(f"  [{i}] {a}" for i, a in enumerate(actions))
    shown = actions[:max_show]
    return "\n".join(f"  [{i}] {a}" for i, a in enumerate(shown)) + \
           f"\n  ... and {len(actions) - max_show} more"


def _format_history(history: List[dict], last_k: int = 10) -> str:
    if not history:
        return "(none)"
    recent = history[-last_k:]
    return ", ".join(h.get("action", str(h)) for h in recent)


# ---------------------------------------------------------------------------
# Router class
# ---------------------------------------------------------------------------

class Implicit7BRouter:
    """7B tool-use router: wraps LLMAgent with tool-use system prompt."""

    def __init__(self, model_path: Optional[str] = None, gpu_id: int = 0, use_vllm: bool = True):
        self.agent = LLMAgent(
            model_path=model_path,
            use_vllm=use_vllm,
            gpu_id=gpu_id,
        )

    def __call__(
        self,
        observation: str,
        valid_actions: List[str],
        history: List[dict],
    ) -> Tuple[str, str]:
        """Router function compatible with ablation_eval_common.RouterFn.

        Sends tool-use prompt to 7B model, parses output for simulate() call.
        """
        messages = [
            {"role": "system", "content": TOOL_USE_SYSTEM_PROMPT},
            {"role": "user", "content": TOOL_USER_TEMPLATE.format(
                observation=observation,
                valid_actions_str=_format_actions(valid_actions),
                history_str=_format_history(history),
            )},
        ]

        raw_output = self.agent._generate(messages)
        action, route = parse_tool_use_output(raw_output, valid_actions)
        return action, route


# ---------------------------------------------------------------------------
# Standalone evaluation
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Condition (c): 7B Implicit Router evaluation"
    )
    from ablation_eval_common import add_eval_args
    add_eval_args(parser)
    parser.add_argument("--model_path", type=str, default=None,
                        help="Local path to Qwen2.5-7B-Instruct (auto-detected if omitted)")
    parser.add_argument("--use_vllm", action="store_true", default=True)
    parser.add_argument("--no_vllm", action="store_true")
    args = parser.parse_args()

    if args.no_vllm:
        args.use_vllm = False

    router = Implicit7BRouter(
        model_path=args.model_path,
        gpu_id=args.gpu_id,
        use_vllm=args.use_vllm,
    )

    from ablation_eval_common import run_ablation_eval, config_from_args
    config = config_from_args(args, condition_name="implicit_7b")
    results = run_ablation_eval(config, router_fn=router)

    print(f"\n=== Condition (c) Implicit 7B Results ===")
    print(f"Mean score: {results['episode_metrics']['mean_score']:.2f}")
    print(f"Death rate: {results['episode_metrics']['death_rate']:.1%}")
    print(f"Routing accuracy: {results['routing_accuracy']['accuracy']:.3f}")
    print(f"Route ratio det: {results['episode_metrics']['route_ratio_det']:.1%}")


if __name__ == "__main__":
    main()
