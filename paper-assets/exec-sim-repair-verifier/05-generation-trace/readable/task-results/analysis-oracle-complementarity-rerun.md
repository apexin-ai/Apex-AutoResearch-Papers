# analysis oracle complementarity rerun

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_oracle-complementarity-rerun_20260519T153835_result.json`
- **Structured JSON:** [`010889b8442f90be92e8.json`](../../sessions/01/010889b8442f90be92e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Comprehensive results. Here's the full analysis:

---

## Findings

### 1. Oracle 90.63% — arithmetically correct

| | Value |
|---|---|
| n | 1890 |
| both_correct | 1601 |
| cls_only_wrong | 53 |
| cwm_only_wrong | 59 |
| both_wrong | 177 |
| **Oracle** | **1713/1890 = 90.63%** ✓ |

This is per-sample function-level. The overlap counts are internally consistent with CLS accuracy 87.83% (errors=230) and CWM accuracy 87.51% (errors=236).

### 2. "CLS 75.5% FN, CWM 83.1% FP" — WRONG

From the verified per-class F1 data in `paper_materials.md` (978 pass, 912 fail):

| Model | FN (FAIL→PASS) | FP (PASS→FAIL) | FN% | FP% | Paper claim |
|-------|----------------|-----------------|-----|-----|-------------|
| CLS seed42 | 100 | 130 | **43.5%** | **56.5%** | "75.5% FN" |
| CWM seed42 | 70 | 166 | **29.7%** | **70.3%** | "83.1% FP" |

Both models have **FP-dominant** errors (over-predict failure). The paper claims they have **opposite** patterns — that's wrong.

### 3. Mathematical proof of inconsistency

If the paper's FN/FP claims were true:
- CLS would have 174 FN + 56 FP
- CWM would have 40 FN + 196 FP  
- Max possible both_wrong = min(56,196) + min(174,40) = **96**
- Actual both_wrong = **177** → **impossible** (177 > 96)

### 4. Root cause: `predictions_cls_seed42.jsonl` is wrong or mislabeled

This file has accuracy **87.51%** (matching CWM seed42), not 87.83% (true CLS seed42). From it:
- 75.4% of errors are PASS→FAIL (FP)
- Someone read this as "75.5% FN" — **inverting the direction label**

### 5. Correct error complementarity narrative

Both models over-predict failure. CWM does so more aggressively (70.3% FP vs CLS 56.5% FP). There IS real complementarity:
- Oracle gain: +2.80pp over CLS, +3.12pp over CWM
- 177 shared errors out of 230+236 total errors → meaningful diversity
  
But "structurally opposite error patterns" is an overstatement. The correct framing: CWM has a stronger fail-bias than CLS, creating partial complementarity.

### Corrected numbers for the paper

| Metric | Paper value | Correct value |
|--------|------------|---------------|
| Oracle accuracy | 90.63% | **90.63%** (correct) |
| CLS dominant error direction | 75.5% FN | **56.5% FP** (PASS→FAIL) |
| CWM dominant error direction | 83.1% FP | **70.3% FP** (PASS→FAIL) |
| Error pattern description | "opposite" | "same direction, different degree" |

### Key files
- Oracle data: `artifacts/error_overlap_matched_seed.json`
- Per-class F1: `artifacts/paper_materials.md` §1.1
- Overlap script: `analysis_error_overlap.py` (remote)
- Suspect prediction file: `predictions_cls_seed42.jsonl` (acc=87.51%, likely wrong checkpoint or mislabeled)

---
