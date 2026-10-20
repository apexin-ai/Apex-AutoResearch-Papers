# ssh minihack death bug fix

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_minihack-death-bug-fix_20260519T115954_result.json`
- **Structured JSON:** [`c8b42004c7b0d6597747.json`](../../sessions/c8/c8b42004c7b0d6597747.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the full report:

---

```
=== DEATH BUG FIX VERIFICATION ===
Corridor-R3 det before fix: 3/5 died (BUGGY — all were timeouts with negative step penalty)
Corridor-R3 det after fix:  0/5 died (CORRECT — end_status=0 for timeouts, end_status=2 for wins)

Fix applied to:
  - minihack_episode_runner.py:155 — died = end_status == 1
  - minihack_episode_runner.py:156 — goal_reached = end_status in (2, 3)
  - minihack_det_agent.py:415-416 — same changes
  Both files now include end_status in result dict.

=== EPISODE DETAILS ===

--- Room-15x15 det ---
ep0  seed=42  steps=14   score=+1.0  end_status=2  GOAL
ep1  seed=43  steps=14   score=+1.0  end_status=2  GOAL
ep2  seed=44  steps=14   score=+1.0  end_status=2  GOAL
ep3  seed=45  steps=14   score=+1.0  end_status=2  GOAL
ep4  seed=46  steps=14   score=+1.0  end_status=2  GOAL

--- Room-15x15 internal ---
ep0  seed=42  steps=14   score=+1.0  end_status=2  GOAL  parse_fail=0/14
ep1  seed=43  steps=14   score=+1.0  end_status=2  GOAL  parse_fail=0/14
ep2  seed=44  steps=14   score=+1.0  end_status=2  GOAL  parse_fail=0/14
ep3  seed=45  steps=14   score=+1.0  end_status=2  GOAL  parse_fail=0/14
ep4  seed=46  steps=14   score=+1.0  end_status=2  GOAL  parse_fail=0/14

--- Corridor-R3 det ---
ep0  seed=42  steps=500  score=-3.6  end_status=0  TIMEOUT
ep1  seed=43  steps=160  score=+1.0  end_status=2  GOAL
ep2  seed=44  steps=500  score=-3.8  end_status=0  TIMEOUT
ep3  seed=45  steps=500  score=-3.2  end_status=0  TIMEOUT
ep4  seed=46  steps=27   score=+1.0  end_status=2  GOAL

--- Corridor-R3 internal ---
ep0  seed=42  steps=500  score=+0.0  end_status=0  TIMEOUT  parse_fail=0/500
ep1  seed=43  steps=500  score=-5.0  end_status=0  TIMEOUT  parse_fail=500/500
ep2  seed=44  steps=500  score=+0.0  end_status=0  TIMEOUT  parse_fail=0/500
ep3  seed=45  steps=500  score=+0.0  end_status=0  TIMEOUT  parse_fail=0/500
ep4  seed=46  steps=500  score=-5.0  end_status=0  TIMEOUT  parse_fail=0/500

--- Corridor-R5 det ---
ep0  seed=42  steps=162  score=+1.0  end_status=2  GOAL
ep1  seed=43  steps=500  score=-3.7  end_status=0  TIMEOUT
ep2  seed=44  steps=500  score=-3.8  end_status=0  TIMEOUT
ep3  seed=45  steps=19   score=+1.0  end_status=2  GOAL
ep4  seed=46  steps=135  score=+1.0  end_status=2  GOAL

--- Corridor-R5 internal ---
ep0  seed=42  steps=500  score=-5.0  end_status=0  TIMEOUT  parse_fail=0/500
ep1  seed=43  steps=500  score=-5.0  end_status=0  TIMEOUT  parse_fail=0/500
ep2  seed=44  steps=500  score=-5.0  end_status=0  TIMEOUT  parse_fail=0/500
ep3  seed=45  steps=500  score=-5.0  end_status=0  TIMEOUT  parse_fail=0/500
ep4  seed=46  steps=500  score=+0.0  end_status=0  TIMEOUT  parse_fail=0/500

--- River det ---
ep0  seed=42  steps=350  score=-2.7  end_status=-1  TIMEOUT
ep1  seed=43  steps=350  score=+0.0  end_status=-1  TIMEOUT
ep2  seed=44  steps=350  score=+0.0  end_status=-1  TIMEOUT
ep3  seed=45  steps=350  score=+0.0  end_status=-1  TIMEOUT
ep4  seed=46  steps=350  score=+0.0  end_status=-1  TIMEOUT

--- River internal ---
ep0  seed=42  steps=350  score=-3.5  end_status=-1  TIMEOUT  parse_fail=0/350
ep1  seed=43  steps=350  score=+0.0  end_status=-1  TIMEOUT  parse_fail=0/350
ep2  seed=44  steps=350  score=+0.0  end_status=-1  TIMEOUT  parse_fail=0/350
ep3  seed=45  steps=350  score=-3.5  end_status=-1  TIMEOUT  parse_fail=0/350
ep4  seed=46  steps=350  score=-3.5  end_status=-1  TIMEOUT  parse_fail=0/350

=== ALL HARDER TASK PILOTS (post-fix) ===
Task            | Strategy | N | Deaths | DR   | Wins | WR   | Avg Steps | Notes
----------------|----------|---|--------|------|------|------|-----------|------
Room-15x15      | det      | 5 | 0      | 0%   | 5    | 100% | 14.0      | trivial
Room-15x15      | internal | 5 | 0      | 0%   | 5    | 100% | 14.0      | trivial
Corridor-R3     | det      | 5 | 0      | 0%   | 2    | 40%  | 337.4     |
Corridor-R3     | internal | 5 | 0      | 0%   | 0    | 0%   | 500.0     | ep1: 100% parse fail
Corridor-R5     | det      | 5 | 0      | 0%   | 3    | 60%  | 263.2     |
Corridor-R5     | internal | 5 | 0      | 0%   | 0    | 0%   | 500.0     |
River           | det      | 5 | 0      | 0%   | 0    | 0%   | 350.0     | env caps at 350 steps; end_status=-1
River           | internal | 5 | 0      | 0%   | 0    | 0%   | 350.0     | env caps at 350 steps; end_status=-1

=== DECISION POINT SUMMARY ===
Task            | Int WR | Det WR | Δ WR   | Verdict
----------------|--------|--------|--------|--------
Room-15x15      | 100%   | 100%   | 0pp    | too easy (both solve in 14 steps)
Corridor-R3     | 0%     | 40%    | -40pp  | feasible (clear det>int gap)
Corridor-R5     | 0%     | 60%    | -60pp  | feasible (clear det>int gap)
River           | 0%     | 0%     | 0pp    | too hard (neither solves; env 350-step cap, no end_status)
```

Key observations:
- **Zero actual deaths across all 40 episodes** post-fix. Every non-win is a timeout. The old `total_reward < 0` check was 100% false positives.
- **Death rate is useless as a metric** for these tasks. Win rate / goal_reached is the meaningful comparison.
- **River** has an unusual env: 350-step hard cap, no `end_status` in info dict (returns -1). Neither agent can cross the river.
- **Corridor-R3/R5** show the clearest det vs. internal gap (40-60pp win rate difference), making them ideal experiment tasks.
- **Room-15x15** is trivially solved by both agents in 14 steps.

---
