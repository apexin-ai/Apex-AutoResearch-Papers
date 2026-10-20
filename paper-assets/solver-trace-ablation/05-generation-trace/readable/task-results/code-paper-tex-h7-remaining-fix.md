# code paper tex h7 remaining fix

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_paper-tex-h7-remaining-fix_20260515T160120_result.json`
- **Structured JSON:** [`42c892c366f9abb51433.json`](../../sessions/42/42c892c366f9abb51433.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两处修改完成。精确 diff：

**1. experiments.tex L157**
- old: `\textbf{H7} (conclusion duplication) is ISR-specific at $69.7\%$ combined vs.\ $0\%$ in random controls;`
- new: `\textbf{H7} (conclusion duplication) is ISR-accelerated at 500 steps ($69.7\%$ combined vs.\ $0\%$ under random), though random $\beta{=}0.1$ converges to $100\%$ H7 by 1000 steps;`

**2. conclusion.tex L16–17**
- old: `random $\beta{=}0.1$ produces $0\%$ H7 ($0/256$)` → new: `at 500 steps, random $\beta{=}0.1$ produces $0\%$ H7 ($0/256$)` ... `by 1000 steps, however, random $\beta{=}0.1$ converges to $100\%$ H7 ($97/97$).`
- old: `The gradient suggests H7 is primarily ISR-induced but not ISR-exclusive: high-variance reward bonuses at $\beta{=}0.3$ can induce low-frequency H7 even without ISR signal, while ISR at any dose amplifies it by orders of magnitude.` → new: `The gradient suggests ISR accelerates H7 onset rather than being its sole cause: random training reaches the same mode given sufficient steps, while ISR at any dose amplifies early convergence by orders of magnitude.`

---
