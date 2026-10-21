"""ALFWorld action canonicalization for comparing a_pre vs a_post."""

import re
from typing import Optional, Tuple


def canonicalize_action(action_str: str) -> Tuple[str, Optional[str], Optional[str]]:
    """Parse an ALFWorld action into (verb, object, receptacle).

    Handles all standard ALFWorld action formats:
      "go to desk 1"           -> ("go", "desk 1", None)
      "take lamp 1 from desk 1" -> ("take", "lamp 1", "desk 1")
      "put lamp 1 in/on desk 1" -> ("put", "lamp 1", "desk 1")
      "open fridge 1"          -> ("open", "fridge 1", None)
      "close drawer 1"        -> ("close", "drawer 1", None)
      "use desklamp 1"        -> ("use", "desklamp 1", None)
      "heat apple 1 with microwave 1" -> ("heat", "apple 1", "microwave 1")
      "cool apple 1 with fridge 1"    -> ("cool", "apple 1", "fridge 1")
      "clean mug 1 with sinkbasin 1"  -> ("clean", "mug 1", "sinkbasin 1")
      "examine mirror 1"      -> ("examine", "mirror 1", None)
      "inventory"              -> ("inventory", None, None)
      "look"                   -> ("look", None, None)
    """
    action_str = " ".join(action_str.strip().lower().split())

    if action_str in ("inventory", "look"):
        return (action_str, None, None)

    two_arg_patterns = [
        (r"^(take)\s+(.+?)\s+from\s+(.+)$",),
        (r"^(put)\s+(.+?)\s+(?:in|on)\s+(.+)$",),
        (r"^(heat|cool|clean|slice)\s+(.+?)\s+with\s+(.+)$",),
    ]
    for (pattern,) in two_arg_patterns:
        m = re.match(pattern, action_str)
        if m:
            verb, obj, recep = m.group(1), m.group(2).strip(), m.group(3).strip()
            return (verb, obj, recep)

    one_arg_patterns = [
        r"^(go\s+to)\s+(.+)$",
        r"^(open|close|toggle|use|examine)\s+(.+)$",
    ]
    for pattern in one_arg_patterns:
        m = re.match(pattern, action_str)
        if m:
            verb, obj = m.group(1), m.group(2).strip()
            if verb == "go to":
                verb = "go"
            return (verb, obj, None)

    parts = action_str.split(maxsplit=1)
    if len(parts) == 2:
        return (parts[0], parts[1], None)
    return (action_str, None, None)


def actions_equivalent(action_a: str, action_b: str) -> bool:
    """Check if two ALFWorld actions are semantically equivalent."""
    return canonicalize_action(action_a) == canonicalize_action(action_b)
