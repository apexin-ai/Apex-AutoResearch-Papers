# ssh p2 failure taxonomy figure

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_p2-failure-taxonomy-figure_20260518T075703_result.json`
- **Structured JSON:** [`82f350143f02ea0c85fe.json`](../../sessions/82/82f350143f02ea0c85fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All figures are generated and saved on the server. Here's a summary of the results:

## Data Overview
- **133 episodes** from **25 tasks** in the prescreening dataset
- Internal (LLM) strategy: **74 deaths** (55.6%), **59 non-death**
- Deterministic strategy: **15 deaths** (11.3%), **118 non-death**

## Figure 1: `death_action_distribution.pdf/png` (2589x1314)
Two-panel layout showing Internal (LLM) strategy:

**Left panel** (stacked horizontal bars, full distribution):
| Category | Death (n=74) | Non-death (n=59) |
|---|---|---|
| connect [X] to [Y] | 86.7% | 78.6% |
| focus on [X] | 5.5% | 1.8% |
| observation | 5.3% | 3.2% |
| object interaction | 1.4% | 7.6% |
| disconnect [X] | 1.0% | 6.3% |
| other | 0.0% | 2.5% |

**Right panel** (zoomed grouped bar for non-connect categories): highlights that `focus on [X]` is **3x higher in death episodes** (5.5% vs 1.8%), with annotation.

## Figure 2: `death_action_timeline.pdf/png` (2965x926)
6 representative death episodes from different tasks, showing color-coded action sequences step-by-step with the fatal `focus on` step marked with black border and arrow.

## Figure 3: `death_action_comparison.pdf/png` (2973x1162)
Side-by-side comparison of non-connect action distributions for both Internal and Deterministic strategies.

## Key Findings

1. **ALL death episodes contain exactly 1 `focus on [X]` action** that triggers the -100 death penalty (74 focus actions across 74 death episodes in Internal strategy).

2. **Death episodes are dominated by unproductive `connect [X] to [Y]` loops** (86.7% vs 78.6%), indicating the agent gets stuck in repetitive connection patterns before making a fatal answer submission.

3. **Non-death episodes show more diverse, productive actions**: higher object interaction (7.6% vs 1.4%), more disconnect (6.3% vs 1.0%), suggesting non-death episodes involve actual task-solving behavior.

4. **Interesting pattern beyond `focus on`**: The most common death target is **`focus on workshop`** (33/74 = 44.6% of internal death episodes), suggesting a systematic LLM bias toward the workshop as an answer. Other targets include `focus on inventory` (8), `focus on kitchen` (8), `focus on living room` (4), `focus on fountain` (4).

## Suggested Figure Captions

**Figure 1**: "Action distribution comparison between death (score = -100) and non-death episodes under the Internal (LLM) strategy across 133 ScienceWorld episodes. Left: full distribution showing dominance of connect actions in both groups. Right: zoomed view of non-connect actions revealing that death episodes exhibit 3x higher focus on [X] (fatal answer submission) and significantly lower rates of productive actions (object interaction, disconnect)."

**Figure 2**: "Action sequences of six representative death episodes under the Internal strategy, color-coded by action category. The fatal focus on [X] step (black border, arrow) consistently follows extended sequences of unproductive connect actions, illustrating the stereotypical death pattern: the agent cycles through connection attempts before submitting an incorrect answer."

---
