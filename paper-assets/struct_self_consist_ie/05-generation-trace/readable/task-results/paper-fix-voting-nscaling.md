# paper fix voting nscaling

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fix_voting_nscaling_20260514T215950_result.json`
- **Structured JSON:** [`c0fa557202aa6d8242ba.json`](../../sessions/c0/c0fa557202aa6d8242ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Edit applied. The artifacts copy (`artifacts/_project/paper/experiments.tex`) does not contain this text — it's an older, shorter version (225 lines) that lacks the voting/logprob N-scaling claims.

---

**Results:**

### 1. Accurate Voting N-scaling values from server

| Setting | N=8 ρ | N=16 ρ | Δ | Source |
|---------|--------|---------|-----|--------|
| Qwen CoNLL | 0.424 | 0.429 | **+0.005** | n8/n16_5signal |
| LLaMA SciERC | 0.433 | 0.452 | **+0.018** | n8/n16_5signal (exp_007) |
| LLaMA CoNLL | 0.426 | 0.455 | **+0.030** | exp_017 n8_vs_n16_delta |
| Qwen SciERC | 0.502 | 0.422 | **-0.080** | exp_015_v2 (N=8) / exp_001 3-seed mean (N=16) |

The original "+0.018 on SciERC" came from LLaMA SciERC, not Qwen SciERC. Qwen SciERC actually shows a -0.080 decline (N=8 baseline may be inflated by max_tokens=512 issue in exp_012).

### 2. Modified paragraph (lines 248-249)

```latex
Voting confidence $N$-scaling is setting-dependent ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $-0.080$ on Qwen SciERC), while logprob is approximately $N$-invariant ($\Delta{\leq}0.021$).
SJ and EM scale consistently across all tested settings; FK and voting confidence show setting-dependent variation, suggesting that agreement-based structural signals are the most robust to $N$.
```

### 3. Modified file
`/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex` — lines 248-249. The artifacts copy does not contain this error.

---
