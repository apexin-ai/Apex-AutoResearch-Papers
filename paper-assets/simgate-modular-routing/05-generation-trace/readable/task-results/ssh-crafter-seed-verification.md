# ssh crafter seed verification

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_crafter-seed-verification_20260518T041127_result.json`
- **Structured JSON:** [`86e3e6ffad244e33c714.json`](../../sessions/86/86e3e6ffad244e33c714.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Monkey-patch 完全修复了问题。10/10 seeds 全部 deterministic。

---

## 结构化报告

### 1. Seed 控制结论：PARTIAL → 可修复为 FULL

**原始 Crafter**: PARTIAL。同 seed + 同 actions 在约 50% 的 seed 上产生不同 trajectory（不同 reward、不同存活长度）。

**Patch 后**: FULL。简单 monkey-patch 即可实现完全确定性。

### 2. 测试结果

| Test | 结果 |
|------|------|
| Test 1: 初始 obs/semantic/pos | 全部 identical ✓ |
| Test 2: 20 步 action sequence | obs/rewards identical，semantic 从 step 9 分叉 |
| Test 3: 不同 seed 不同 map | ✓ (map 不同，player_pos 相同因为固定在中心) |
| Test 4: 50 步确定性 | obs 0 mismatch, rewards match ✓ |
| 扩展: 10-seed 500 步压力测试 | **5/10 seed reward 分叉，5/10 trajectory 长度不同** |
| Patch 后 10-seed 测试 | **10/10 全部 deterministic** ✓ |

### 3. 源码分析

**随机源**: 单一 `np.random.RandomState(seed)`，存储在 `world.random`，所有组件共用。

**Seed 传递链**:
```
Env(seed=42) → env._seed=42
  → reset(): world.reset(seed=hash((42, episode)) % 2^31)
    → world.random = RandomState(derived_seed)
    → worldgen 用 world.random
    → mob spawn/AI 用 world.random
    → 渲染夜间噪声用 world.random
```

**根因**: `engine.World._chunks = collections.defaultdict(set)`

Python `set` 的迭代顺序依赖对象 `id()`（内存地址）。两个 env 实例的对象地址不同 → `_balance_chunk` 中 `[obj for obj in objs if isinstance(obj, cls)]` 顺序不同 → `random.randint(0, len(creatures))` 选中不同 mob 进行 despawn → 世界状态分叉。

触发条件: `self._step % 10 == 0`（每 10 步调用一次 `_balance_chunk`）。

### 4. 对实验设计的影响

**推荐方案**: 使用 monkey-patch 实现 FULL determinism，然后做 paired counterfactual。

**Patch 代码**（加在实验入口处）:

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

**有了 patch**: paired counterfactual 完全可行，N=50 足够。同 seed 同 actions = 完全相同 trajectory。

---
