# paper round11 step1 step2

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_round11_step1_step2_20260522T081645_result.json`
- **Structured JSON:** [`0ef30470d7e7c8a9b28b.json`](../../sessions/0e/0ef30470d7e7c8a9b28b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits complete. Summary of changes:

**Step 1A (auth_scope 52pp downgrade):**
- `introduction.tex:19` — 52pp now qualified as "upper bound with substantial measurement uncertainty ($\kappa = 0.385$, below fair agreement)"
- `experiments.tex:57` (heatmap caption) — added "$\kappa = 0.385$" caveat after 52pp
- `experiments.tex:63` (§5.4 body) — added "though this range is an upper bound with substantial measurement uncertainty ($\kappa = 0.385$)"
- `experiments.tex:65` (§5.4 end) — new sentence: removing auth_scope eliminates C4 interaction ($p = 0.97$; Appendix~\ref{app:c4_sans_auth})
- `abstract.tex` / `conclusion.tex` — no 52pp mentions, skipped

**Step 1B (tier hierarchy → gradient):**
- `abstract.tex:2` — "cluster into a lower tier, though tier cohesion is margin-dependent" → "show a risk gradient rather than sharp tiers"
- `experiments.tex:34` (§5.2) — three-tier TOST language replaced with ±15pp full / ±10pp partial equivalence framing, "risk gradient rather than discrete tiers"
- `experiments.tex:41` (forest plot caption) — "three-tier hierarchy" → "consistent upper bound; remaining types show a risk gradient"
- `conclusion.tex` — no tier language, skipped

**Step 2 (mitigation paragraph):**
- `discussion.tex:7-8` — new `\paragraph{Prompt-based mitigation.}` inserted before Practical implications (~110 words). All numbers verified against `mitigation_v2_results.json`.

**Page budget:**
- DN paragraph compressed from ~5 rendered lines to ~3 (removed P1/P2 predictions and old mitigation numbers). Net addition ~4-5 lines ≈ 0.12-0.15 page.

---
