# fix caption and narrative correction

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_caption-and-narrative-correction_20260523T001013_result.json`
- **Structured JSON:** [`c31480f4c7a499dcbd90.json`](../../sessions/c3/c31480f4c7a499dcbd90.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译通过，27 页，0 error。

**Diff 汇总：**

**appendix.tex L1089** — `\caption` 内：
```diff
- Three of four conditions show consistent $\Delta \leq 0$ across all seeds; Mistral-7B $\times$ FOLIO is the exception ($+0.16 \pm 2.70$\,pp).
+ Two of four conditions (Mistral-7B $\times$ PW, Qwen2.5-14B $\times$ FOLIO) show $\Delta \leq 0$ across all seeds; the remaining two show mixed signs with negative means ($+0.16 \pm 2.70$, $-0.98 \pm 2.25$\,pp).
```

**experiments.tex L57** — 多种子叙事：
```diff
- Four-seed replication on Mistral-7B $\times$ ProofWriter ($\bar{\Delta}{=}{-}2.38 \pm 1.12$\,pp, 4/4 seeds $\Delta \leq 0$) and three-seed replication on LLaMA-3.1-8B $\times$ FOLIO ($\bar{\Delta}{=}{-}0.98 \pm 2.25$\,pp) confirm that the SICA${\leq}$SC pattern is stable across seeds, models, and datasets (Table~\ref{tab:multi-seed}). Four-seed replication on Qwen2.5-14B $\times$ FOLIO confirms the single-seed pattern: $\Delta \in [0.00, -2.01]$\,pp (mean $-1.24 \pm 0.86$; Table~\ref{tab:multi-seed}).
+ Multi-seed replication confirms robustness: Mistral-7B $\times$ ProofWriter (4 seeds, $\bar\Delta=-2.38\pm1.12$\,pp, all $\Delta\leq0$) and Qwen2.5-14B $\times$ FOLIO (4 seeds, $\bar\Delta=-1.79\pm0.25$\,pp, all $\Delta\leq0$) show uniformly non-positive $\Delta$; the remaining two conditions yield near-zero means with mixed signs (Table~\ref{tab:multi-seed}).
```

---
