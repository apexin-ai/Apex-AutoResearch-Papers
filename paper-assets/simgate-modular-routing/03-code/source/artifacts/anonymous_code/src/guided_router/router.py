"""Decomposition-Guided Router: routes based on task-type death risk.

Core insight: ~90% of routing signal comes from death avoidance (DAF).
This is a task-type level binary property -- tasks either have high internal
death rate or not.

Variants:
  - oracle: uses ground-truth death risk labels from counterfactual data
  - learned: infers death risk from task_desc/task_type string matching
"""

from .config import DEATH_RISK_TASKS, NON_DEATH_RISK_TASKS, DEATH_THRESHOLD, ALL_TASKS

DEATH_RISK_PATTERNS = [
    "freeze", "boil", "melt", "melting",
    "life-stage", "life stage", "lifespan",
    "inclined-plane", "inclined plane", "angle",
    "chemistry-mix", "chemistry mix", "chemical",
    "grow-fruit", "grow fruit",
    "find-animal", "find animal",
]

SAFE_PATTERNS = [
    "non-living", "non living", "nonliving", "inanimate",
]


class GuidedRouter:
    """Routes episodes to deterministic or internal based on task-type death risk.

    Oracle variant: uses ground-truth task-type labels.
    Learned variant: infers task-type death risk from task description/type string.
    """

    def __init__(self, variant="oracle"):
        assert variant in ("oracle", "learned"), f"Unknown variant: {variant}"
        self.variant = variant
        self.death_risk_tasks = set(DEATH_RISK_TASKS.keys())
        self.safe_tasks = set(NON_DEATH_RISK_TASKS.keys())

    def route(self, task_type, observation="", step_idx=0):
        """Return routing decision: 'deterministic' or 'internal'.

        Args:
            task_type: task type string (e.g. 'chemistry-mix')
            observation: current step observation text (used by learned variant)
            step_idx: current step index (unused for now)

        Returns:
            str: 'deterministic' or 'internal'
        """
        if self.variant == "oracle":
            return self._route_oracle(task_type)
        else:
            return self._route_learned(task_type, observation)

    def _route_oracle(self, task_type):
        if task_type in self.death_risk_tasks:
            return "deterministic"
        if task_type in self.safe_tasks:
            return "internal"
        rate = ALL_TASKS.get(task_type)
        if rate is not None and rate > DEATH_THRESHOLD:
            return "deterministic"
        return "internal"

    def _route_learned(self, task_type, observation=""):
        text = (task_type + " " + observation).lower()
        for pat in SAFE_PATTERNS:
            if pat in text:
                return "internal"
        for pat in DEATH_RISK_PATTERNS:
            if pat in text:
                return "deterministic"
        return "deterministic"

    def route_batch(self, task_types, observations=None):
        if observations is None:
            observations = [""] * len(task_types)
        return [self.route(t, o) for t, o in zip(task_types, observations)]
