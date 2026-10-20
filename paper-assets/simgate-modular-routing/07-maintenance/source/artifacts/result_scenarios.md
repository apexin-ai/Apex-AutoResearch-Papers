# Result Scenario Analysis

Pre-analysis of how pending experimental results affect paper claims.

## Scenarios

| Scenario | Gemma ScienceWorld | Llama ALFWorld | Paper Impact |
|----------|-------------------|----------------|-------------|
| **Best** | Death dominance confirmed (DAF > 80%, ΔDR > 20pp) | Information asymmetry confirmed (~25% det-pref, 0% death labels) | Upgrade C1 to "3 model families"; upgrade C3 to "cross-model × cross-environment"; Discussion adds "framework generalizes across both axes" |
| **Median** | Death dominance directionally consistent but weaker (DAF 50-80%, ΔDR 10-20pp) | Information asymmetry confirmed | C1 unchanged ("2+ families"), Gemma as "supporting evidence with reduced effect size" in Appendix; C3 upgrade for ALFWorld cross-model |
| **Worst** | No death dominance or reversed direction | Results inconsistent with Qwen | Discuss model-dependency as limitation; reduce C1 claim strength but add depth analyzing why Gemma differs; if ALFWorld also inconsistent, add "model-specific" caveat to C3 |

## Response Plans

### Best case actions
- Expand cross-model table to 3x2 matrix (3 models x 2 environments)
- Strengthen Abstract/Intro language: "across three independent model families"
- Add Gemma row to Table 3 in main text (not just appendix)

### Median case actions
- Add Gemma to Appendix cross-model table with effect size discussion
- Main text mentions "two primary + one supporting model family"
- ALFWorld subsection gets Llama cross-model data

### Worst case actions
- Reframe as "model-dependent phenomenon" -- still a valid diagnostic finding
- Add analysis: what about Gemma's architecture/training makes it different?
- Consider whether Gemma's behavior reveals a limitation of the framework or of the model
- Do NOT suppress negative results -- present them honestly with analysis
