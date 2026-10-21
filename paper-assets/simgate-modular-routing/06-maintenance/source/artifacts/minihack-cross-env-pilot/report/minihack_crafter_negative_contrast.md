# Cross-Environment Negative Contrast Summary

**Experiment**: minihack-cross-env-pilot (DONE, negative)
**Date**: 2026-05-19
**Purpose**: Validate death dominance framework beyond ScienceWorld using permadeath environments

---

## MiniHack Navigation Tasks (Post Bug-Fix M010)

Bug M010: original `died = total_reward < 0 or end_status == 1` misclassified timeouts as deaths (per-step penalty accumulates to ~-3.5 over 500 steps). Fixed to `died = end_status == 1`.

| Task | Condition | N | Death Rate | Goal Rate | Avg Steps | Notes |
|------|-----------|---|-----------|-----------|-----------|-------|
| Room-5x5 | Deterministic (BFS) | 5 | 0% | 100% | 4 | Trivial: 4 steps to goal |
| Room-5x5 | LLM (Qwen-7B) | 5 | 0% | 100% | 4 | Also trivial for LLM |
| Room-15x15 | Deterministic | 5 | 0% | — | — | No deaths, longer paths |
| Room-15x15 | LLM | 5 | 0% | — | — | No deaths |
| Corridor-R3 | Deterministic | 5 | 0% | — | — | Post-fix: was 60% with bug |
| Corridor-R3 | LLM | 5 | 0% | — | — | |
| Corridor-R5 | Deterministic | 5 | 0% | — | — | |
| Corridor-R5 | LLM | 5 | 0% | — | — | |
| River | Deterministic | 5 | 0% | — | — | |
| River | LLM | 5 | 0% | — | — | |

**ΔDR = 0 pp** across all tasks.

**Root cause**: MiniHack navigation tasks (Room, Corridor, River) do not spawn monsters in their standard configurations. Death is only possible through starvation after very long episodes (>>500 steps). The tasks test pathfinding, not survival.

## Crafter (Survival Game)

| Condition | N | Death Rate | Avg Steps | Achievements | Notes |
|-----------|---|-----------|-----------|-------------|-------|
| Random | 5 | 100% | ~150 | ~2 | Dies to zombies/skeletons |
| Deterministic (heuristic) | 10 | 100% | ~200 | ~3 | Slightly longer survival |
| LLM (Qwen-7B) | 10 | 100% | ~100 | 0 | Worse than random; only used movement actions |

**ΔDR = 0 pp** (all agents die).

**Root cause**: Crafter's survival loop (food + rest + combat) is beyond current LLM agent capabilities. The LLM agent failed to use any non-movement actions (craft, place, eat), making it functionally a random walker. Even the heuristic agent with programmed survival rules died in all episodes within 300 steps.

## Discussion Framing Value

These negative results strengthen the paper's narrative in two ways:

1. **Death dominance requires a specific regime**: Not all permadeath environments produce death asymmetry. The environment must sit in a "Goldilocks zone" where (a) death is possible but not universal, and (b) the deterministic modality has meaningfully lower death risk than the LLM modality.

2. **ScienceWorld occupies this zone**: ScienceWorld's task-specific failure modes (not HP-based combat) combined with its text-based action space create conditions where deterministic execution reliably avoids catastrophic failure while LLM agents face ~42% death rates. This is not trivial to replicate.

3. **Practitioner Decision Framework validation**: The 50-episode pilot protocol (§5 / Appendix) would correctly diagnose both environments:
   - MiniHack: ΔDR < 5pp → "No death dominance, no routing signal from death"
   - Crafter: ΔDR = 0pp (both 100%) → "No death asymmetry, environment too lethal for meaningful comparison"
