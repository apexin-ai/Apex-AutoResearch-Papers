# Crafter Seed Determinism Verification Report

## Conclusion: PARTIAL → FULL (with monkey-patch)

### Original Crafter
- PARTIAL determinism: same seed + same actions diverge in ~50% of seeds
- Root cause: `engine.World._chunks = collections.defaultdict(set)` — Python `set` iteration order depends on object `id()` (memory address)
- Trigger: `self._step % 10 == 0` calls `_balance_chunk`, iterating the set in non-deterministic order → different mob despawn → world state divergence

### Monkey-Patch Fix
Replace `set` with `OrderedSet` in `_chunks`:

```python
import collections
import numpy as np
import crafter.engine as engine

class OrderedSet:
    def __init__(self):
        self._items = []
    def add(self, item):
        if item not in self._items:
            self._items.append(item)
    def remove(self, item):
        self._items.remove(item)
    def __iter__(self):
        return iter(self._items)
    def __len__(self):
        return len(self._items)
    def __contains__(self, item):
        return item in self._items

original_reset = engine.World.reset
def patched_reset(self, seed=None):
    self.random = np.random.RandomState(seed)
    self.daylight = 0.0
    self._chunks = collections.defaultdict(OrderedSet)
    self._objects = [None]
    self._mat_map = np.zeros(self.area, np.uint8)
    self._obj_map = np.zeros(self.area, np.uint32)
engine.World.reset = patched_reset
```

### Verification Results

| Test | Result |
|------|--------|
| Initial obs/semantic/pos | Identical ✓ |
| 20-step action sequence | Diverges at step 9 (pre-patch) |
| 50-step determinism (post-patch) | 0 mismatches ✓ |
| 10-seed 500-step stress test (pre-patch) | 5/10 diverge |
| 10-seed 500-step stress test (post-patch) | **10/10 deterministic ✓** |

### Impact on Experiment Design
- Paired counterfactual fully feasible with patch
- Same seed + same actions = identical trajectory
- N=50 episodes sufficient for statistical power