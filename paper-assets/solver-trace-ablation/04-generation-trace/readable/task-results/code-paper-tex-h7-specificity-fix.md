# code paper tex h7 specificity fix

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_paper-tex-h7-specificity-fix_20260515T155808_result.json`
- **Structured JSON:** [`2ea3e7178dd5a50c9b2b.json`](../../sessions/2e/2ea3e7178dd5a50c9b2b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 处修改完成。精确 diff：

**1. abstract.tex L7**
```
- 69.7\% conclusion duplication (H7) versus 0\% under matched random; the sole apparent ISR improvement
+ 69.7\% conclusion duplication (H7) versus 0\% under matched random at 500 steps (by 1000 steps, random converges to the same H7 mode, indicating ISR accelerates rather than exclusively causes tautological collapse); the sole apparent ISR improvement
```

**2. experiments.tex L68**
```
- The most striking number is H7: 69.7\% of proved samples under ISR ($n{=}161/231$) vs.\ \emph{zero} under random ($0/256$).
+ The most striking number at 500 steps is H7: 69.7\% of proved samples under ISR ($n{=}161/231$) vs.\ \emph{zero} under random ($0/256$); however, extended training to 1000 steps reveals random $\beta{=}0.1$ converges to $100\%$ H7, indicating ISR accelerates H7 onset rather than being its sole cause.
```

**3. conclusion.tex L5**
```
- At $\beta{=}0.1$, conclusion duplication exploits the LOO definition (69.7\% vs.\ 0\% under matched random),
+ At $\beta{=}0.1$, conclusion duplication exploits the LOO definition (69.7\% vs.\ 0\% under matched random at 500 steps; by 1000 steps random converges to the same H7 mode, so ISR accelerates rather than exclusively causes the collapse),
```

注意：experiments.tex L157 taxonomy 段落仍写 "H7 (conclusion duplication) is ISR-specific"，conclusion.tex L16 dose-response 段落仍写 "random $\beta{=}0.1$ produces $0\%$ H7 ($0/256$)"——这两处也含绝对声明，但任务限定只改 3 处，未动。如需一并修正可告知。

---
