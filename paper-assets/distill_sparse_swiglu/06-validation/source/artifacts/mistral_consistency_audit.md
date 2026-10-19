# Mistral Cross-Architecture Text Consistency Audit

**Date**: 2026-05-19
**Ground truth**: KL wins 6/7 metrics (PPL + 5/6 downstream); GSM8K sole reversal (11.1% vs 15.9%).
**Data source**: exp_id: mistral_kl30_downstream, mistral_kl30_hellaswag_piqa, mistral_teal30_downstream.

---

## Issue 1 (P1): abstract.tex:6 — "downstream advantages hold" overstates

**Current text**:
```
Both PPL and downstream advantages hold across architectures (Mistral-7B: ARC +9.0pp,
WinoGrande +5.6pp vs.\ TEAL at 30\%)
```

**Problem**: "downstream advantages hold" implies all tasks. GSM8K reverses (-4.8pp). Only 2 of 6 downstream tasks cited, omitting HellaSwag (+8.8pp), PIQA (+3.1pp), MMLU (+0.6pp), and the GSM8K loss.

**Suggested replacement**:
```
PPL and downstream advantages hold on most tasks across architectures (Mistral-7B: KL wins
5 of 6 downstream tasks vs.\ TEAL at 30\%, largest ARC +9.0pp; GSM8K reverses)
```

**Rationale**: Adds accurate task count, acknowledges GSM8K exception. Stays within abstract space constraints. Drops WinoGrande detail to fit GSM8K caveat.

---

## Issue 2 (P1): introduction.tex:16 — Same "both advantages hold" overstatement

**Current text**:
```
On Mistral-7B-v0.3~\cite{jiang2023mistral}, both PPL and downstream advantages hold
(ARC +9.0pp, WG +5.6pp vs.\ TEAL at 30\%)
```

**Problem**: Same as Issue 1. Cherry-picks 2 largest wins without acknowledging GSM8K reversal or full task count.

**Suggested replacement**:
```
On Mistral-7B-v0.3~\cite{jiang2023mistral}, KL wins on PPL and 5 of 6 downstream tasks
(ARC +9.0pp, HellaSwag +8.8pp, WG +5.6pp vs.\ TEAL at 30\%; GSM8K reverses)
```

**Rationale**: Accurate count, adds HellaSwag (the actual largest downstream delta), acknowledges exception.

---

## Issue 3 (P0): experiments.tex:228 — "consistent" claim is false given GSM8K reversal

**Current text**:
```
On Mistral-7B-v0.3~\cite{jiang2023mistral}, KL's downstream advantage is consistent:
HellaSwag +8.8pp, ARC +9.0pp, WG +5.6pp vs.\ TEAL at 30\%, with PPL 6.77 vs.\ 8.38
```

**Problem**:
1. "KL's downstream advantage is consistent" is factually wrong: GSM8K reverses (-4.8pp).
2. Lists only 3 of 6 downstream tasks. PIQA (+3.1pp) and MMLU (+0.6pp) are additional wins.
3. No mention of GSM8K exception. A reviewer comparing with Table 16 (appendix) will see the discrepancy.

**Suggested replacement**:
```
On Mistral-7B-v0.3~\cite{jiang2023mistral}, KL outperforms TEAL on 5 of 6 downstream
tasks at 30\% (HellaSwag +8.8pp, ARC +9.0pp, WG +5.6pp, PIQA +3.1pp, MMLU +0.6pp),
with PPL 6.77 vs.\ 8.38; GSM8K is the sole reversal (11.1\% vs.\ 15.9\%,
Table~\ref{tab:mistral_downstream})
```

**Rationale**: Accurate 5/6 count matching appendix Table 16 caption. All deltas traceable to exp_id: mistral_kl30_downstream, mistral_teal30_downstream. Cross-references the appendix table for full details.

---

## Issue 4 (P2): appendix.tex:364 — "generalizes" without caveat

**Current text**:
```
Table~\ref{tab:mistral_downstream} reports downstream task accuracy at 30\% sparsity on
Mistral-7B-v0.3, confirming that KL's downstream advantage generalizes across architectures.
```

**Problem**: "generalizes" without qualification. The table itself correctly says "5 of 6 tasks" with GSM8K as sole reversal, but this introductory sentence is unconditional.

**Suggested replacement**:
```
Table~\ref{tab:mistral_downstream} reports downstream task accuracy at 30\% sparsity on
Mistral-7B-v0.3, confirming that KL's downstream advantage generalizes on 5 of 6 tasks;
GSM8K is the sole reversal.
```

---

## Issue 5 (P1): limitations.tex — Mistral GSM8K reversal not acknowledged

**Current text**: No mention of Mistral GSM8K anywhere in Limitations.

**Problem**: The paper acknowledges the Qwen-14B MMLU reversal (line 5) but not the Mistral GSM8K reversal. This is a limitation that should be disclosed. A reviewer who notices the appendix table will flag this omission.

**Suggested addition** (after line 5, before the OOD paragraph):
```
On Mistral-7B, KL wins 5 of 6 downstream tasks at 30\% but GSM8K reverses (11.1\% vs.\
TEAL's 15.9\%), consistent with GSM8K's sensitivity to the sparsity objective: reasoning
tasks may require different optimization targets than knowledge and commonsense benchmarks.
```

---

## Issue 6 (P2): ethics.tex:3 — Benchmark list incomplete

**Current text**:
```
standard benchmarks (WikiText-2, WikiText-103, C4, ARC, WinoGrande, MMLU, GSM8K)
```

**Problem**: HellaSwag and PIQA are used in both LLaMA appendix (Table 12) and Mistral evaluation (Table 16) but not listed.

**Suggested replacement**:
```
standard benchmarks (WikiText-2, WikiText-103, C4, ARC, WinoGrande, HellaSwag, PIQA, MMLU, GSM8K)
```

---

## Issue 7 (P2): ethics.tex:32 — Few-shot protocols incomplete

**Current text**:
```
ARC 25-shot, WinoGrande 5-shot, MMLU 5-shot, GSM8K 8-shot
```

**Problem**: Missing HellaSwag (10-shot) and PIQA (0-shot) protocols. These are specified in appendix Table 12 caption.

**Suggested replacement**:
```
ARC 25-shot, WinoGrande 5-shot, HellaSwag 10-shot, PIQA 0-shot, MMLU 5-shot, GSM8K 8-shot
```

---

## Verified: No Issues Found

| Location | Text | Status |
|---|---|---|
| appendix.tex:368 (Table 16 caption) | "5 of 6 tasks...GSM8K is the sole reversal" | Correct |
| appendix.tex:377-378 (Table 16 data) | All 7 columns match provided ground truth | Correct |
| appendix.tex:356 (Table 15 PPL) | Mistral PPL 6.77 vs 8.38 at 30% | Correct |
| conclusion.tex:6 | "halves TEAL's perplexity across 7--14B" | OK (PPL claim only, no downstream task count) |
| experiments.tex:228 exp_id comments | mistral_kl30_downstream, mistral_teal30_downstream | Correct |

---

## Priority Summary

| Priority | Count | Files |
|---|---|---|
| P0 (factually wrong) | 1 | experiments.tex:228 |
| P1 (overstated/missing) | 3 | abstract.tex:6, introduction.tex:16, limitations.tex (missing GSM8K) |
| P2 (minor incomplete) | 3 | appendix.tex:364, ethics.tex:3, ethics.tex:32 |
