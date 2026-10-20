# ssh deploy heuristic v9

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_deploy-heuristic-v9_20260518T052921_result.json`
- **Structured JSON:** [`ce3e56806e6d1f758f49.json`](../../sessions/ce/ce3e56806e6d1f758f49.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here are the complete results.

---

## v9 Heuristic Agent Results

### v9 Changes Applied

| Fix | v8 (before) | v9 (after) |
|-----|-------------|------------|
| **Monster flee** | `close3` (dist ≤ 3), flee only when 2+ converging | `close4` (dist ≤ 4), flee ANY monster within 4 tiles |
| **P3 zombie flee** | Separate rule for zombies ≤ 3 tiles when unarmed | Removed (subsumed by expanded P2.5) |
| **Sleep safety** | Radius 10, forced sleep at energy=0 | Radius 12, NO forced sleep at energy=0 |
| **Flee direction** | Away from danger centroid only | Biased toward nearest water among top flee candidates |
| **Food search (P12)** | Cow ≤ 6 tiles, plant ≤ 4 tiles | Cow ≤ 10 tiles, plant ≤ 8 tiles |

### 5-Episode Results

| Episode | Steps | Death | Final Health | Achievements |
|---------|-------|-------|--------------|--------------|
| 0 | 450 | Yes | 0 | 6: collect_drink, collect_wood, defeat_zombie, eat_cow, make_wood_sword, place_table |
| 1 | 258 | Yes | 0 | 6: (same set) |
| 2 | 218 | Yes | 0 | 5: (no defeat_zombie) |
| 3 | 290 | Yes | 0 | 6: (same as ep0) |
| 4 | 250 | Yes | 0 | 6: (same as ep0) |

### Comparison

| Metric | Heuristic v9 | v8 (reported) | Random |
|--------|-------------|---------------|--------|
| Avg steps | **293.2** | ~353 | 151.4 |
| Death rate | 100% | 100% | 100% |
| Avg achievements | 5.8 | N/A | 2.4 |

**v9 is worse than v8 on survival time** (293 vs ~353 avg steps).

### Death Cause Analysis

Action distribution: 92% movement, 0.5% sleep (only 7 sleeps in 1466 total steps), 6.8% interaction.

**Root cause: sleep starvation → energy depletion → no health regeneration → death spiral.**

1. The "flee ALL within 4 tiles" policy keeps the agent running constantly, leaving almost no time for resource gathering.
2. The sleep safety radius of 12 tiles is too large; monsters are ubiquitous, so the agent almost never finds a safe sleep zone.
3. Removing forced sleep at energy=0 means the agent's energy depletes to 0 and stays there. Without energy (and not sleeping), health cannot regenerate.
4. Each zombie contact does 2 damage. With 34 hp-drop events across 1466 steps (~1 hit every 43 steps) and zero recovery, health steadily drops to 0.

**Typical episode pattern:** Health=9 maintained for ~150 steps → first monster hit → health declines → energy depletes to 0 → can't sleep (monsters too close) → health never recovers → cumulative hits → death.

### v10 Recommendations

1. **Restore emergency sleep with moderate radius**: Sleep at energy ≤ 1 if no monster within **5-6 tiles** (not 12). Getting hit once during sleep costs 2hp, but never sleeping costs all recovery ability. This was the most damaging v9 change.
2. **Conditional flee, not universal**: Only flee when unarmed OR health ≤ 4 OR 2+ monsters within 4. Armed agent with health ≥ 5 should fight isolated monsters to clear threats rather than perpetually running.
3. **Active monster clearing**: When healthy (hp ≥ 6) and armed, engage isolated zombies within 2-3 tiles. Killing them removes the persistent threat that prevents sleep.
4. **Tighter water-camp strategy**: The water-camping behavior works well for drink but the agent wanders too far for food. Consider prioritizing food sources nearer to water.

---
