# MATH-500 stratified sampling utility.
# Selects problems evenly across difficulty levels for balanced profiling.

from collections import defaultdict
from typing import Any, Dict, List
import random


def stratified_sample_math500(
    data: List[Dict[str, Any]],
    per_level: int = 10,
    seed: int = 42,
) -> List[Dict[str, Any]]:
    """Stratified sampling from MATH-500: 10 problems per difficulty level.

    MATH has 5 levels (1-5), yielding 50 problems total.
    The level field may be named "level", "difficulty", or "type".
    """
    by_level: Dict[Any, List[Dict]] = defaultdict(list)
    for item in data:
        lvl = item.get("level", item.get("difficulty", item.get("type")))
        if lvl is None:
            continue
        by_level[lvl].append(item)

    rng = random.Random(seed)
    sampled: List[Dict] = []
    for lvl in sorted(by_level.keys()):
        pool = by_level[lvl]
        k = min(per_level, len(pool))
        sampled.extend(rng.sample(pool, k))

    return sampled
