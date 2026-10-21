"""Compute a_pre: the counterfactual action the agent would take without self-guidance.

During a VERIFY step, we need to compare:
  a_pre  = greedy action from a prompt WITHOUT self-guidance instruction
  a_post = the action the agent actually outputs after self-guidance

If a_pre != a_post, the verification was "informative" — it changed the agent's mind.
"""

import time
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from .verify_mechanism import build_no_guidance_prompt, extract_action_from_response
from .action_canonicalize import actions_equivalent


@dataclass
class PreActionProfiler:
    """Tracks a_pre generation latency for overhead quantification (D031 W2)."""

    _latencies: List[float] = field(default_factory=list)
    _main_latencies: List[float] = field(default_factory=list)

    def record_pre_action(self, latency_s: float):
        self._latencies.append(latency_s)

    def record_main_action(self, latency_s: float):
        self._main_latencies.append(latency_s)

    @property
    def n_samples(self) -> int:
        return len(self._latencies)

    @property
    def mean_pre_latency(self) -> float:
        return sum(self._latencies) / len(self._latencies) if self._latencies else 0.0

    @property
    def mean_main_latency(self) -> float:
        return sum(self._main_latencies) / len(self._main_latencies) if self._main_latencies else 0.0

    @property
    def overhead_ratio(self) -> float:
        """a_pre overhead as fraction of main action latency."""
        if not self._main_latencies or self.mean_main_latency == 0:
            return 0.0
        return self.mean_pre_latency / self.mean_main_latency

    def get_metrics(self) -> dict:
        return {
            "biavr/pre_action_latency_mean_s": self.mean_pre_latency,
            "biavr/main_action_latency_mean_s": self.mean_main_latency,
            "biavr/pre_action_overhead_ratio": self.overhead_ratio,
            "biavr/pre_action_n_samples": self.n_samples,
        }

    def summary(self) -> str:
        if not self._latencies:
            return "No a_pre samples recorded."
        return (
            f"a_pre overhead: {self.mean_pre_latency:.3f}s mean "
            f"({self.overhead_ratio:.1%} of main action), "
            f"n={self.n_samples}"
        )


def build_pre_action_messages(
    conversation_history: List[Dict[str, str]],
    current_observation: str,
) -> List[Dict[str, str]]:
    """Build the message list for counterfactual a_pre generation.

    Takes the existing conversation and replaces the system prompt with one that
    does NOT include self-guidance instructions. The user messages (observations)
    remain the same.

    Args:
        conversation_history: The current conversation as list of
            {"role": ..., "content": ...} dicts.
        current_observation: The current environment observation (user turn)
            that the agent needs to respond to.

    Returns:
        Messages list suitable for greedy decode without self-guidance.
    """
    no_guidance_system = build_no_guidance_prompt()

    messages = [{"role": "system", "content": no_guidance_system}]

    for msg in conversation_history:
        if msg["role"] == "system":
            continue
        messages.append(msg)

    if not messages or messages[-1].get("content") != current_observation:
        messages.append({"role": "user", "content": current_observation})

    return messages


def compare_actions(a_pre: Optional[str], a_post: Optional[str]) -> bool:
    """Check if a_pre and a_post differ (i.e., verification was informative).

    Returns:
        True if the actions are DIFFERENT (verification changed the action).
        False if the actions are the same or either is None.
    """
    if a_pre is None or a_post is None:
        return False
    return not actions_equivalent(a_pre, a_post)


def compute_pre_action_prompt(
    conversation_history: List[Dict[str, str]],
    current_observation: str,
) -> Dict:
    """Prepare the prompt dict for a_pre greedy decoding.

    Returns a dict with:
        - "messages": the formatted message list
        - "sampling_params": recommended params for greedy decode
    """
    messages = build_pre_action_messages(conversation_history, current_observation)
    return {
        "messages": messages,
        "sampling_params": {
            "temperature": 0.0,
            "top_k": 1,
            "max_tokens": 256,
        },
    }
