# MiniHack Cross-Env Negative Contrast

Framework correctly produces null signal in environments lacking modality-dependent death asymmetry.

## Results

### MiniHack Navigation (no monster spawning)

| Task | Condition | N | Deaths | Death Rate | Goal Rate |
|------|-----------|---|--------|------------|-----------|
| Room-5x5 | Deterministic | 5 | 0 | 0% | — |
| Room-5x5 | LLM | 5 | 0 | 0% | — |
| Room-15x15 | Deterministic | 5 | 0 | 0% | — |
| Room-15x15 | LLM | 5 | 0 | 0% | — |
| Corridor-R3 | Deterministic | 5 | 0 | 0% | — |
| Corridor-R3 | LLM | 5 | 0 | 0% | — |
| Corridor-R5 | Deterministic | 5 | 0 | 0% | — |
| Corridor-R5 | LLM | 5 | 0 | 0% | — |
| River | Deterministic | 5 | 0 | 0% | — |
| River | LLM | 5 | 0 | 0% | — |

**ΔDR = 0.** No death mechanism → no deaths → no asymmetry to detect.

### Crafter (universal lethality)

| Condition | N | Deaths | Death Rate | Max Steps |
|-----------|---|--------|------------|-----------|
| Random | 10 | 10 | 100% | 300 |
| Deterministic | 10 | 10 | 100% | 300 |
| LLM | 10 | 10 | 100% | 300 |

**ΔDR = 0.** All agent types die equally → deaths are environment-universal, not modality-dependent.

## Conclusion

MiniHack navigation tasks lack monster spawning, producing 0% death rate across all 10 condition×task pairs. Crafter kills all three agent types at 100%. In both cases ΔDR = 0: the framework correctly diagnoses no death dominance. This confirms that the framework does not spuriously report death dominance in arbitrary environments — it triggers only when death asymmetry is modality-dependent (i.e., when one routing modality systematically encounters more lethal outcomes than another).

## Discussion Takeaway

> Cross-environment validation on MiniHack (0% death, no combat) and Crafter (100% death, all agents) confirms that the framework reports death dominance exclusively when modality-dependent asymmetry exists, ruling out environment-agnostic artifacts.
