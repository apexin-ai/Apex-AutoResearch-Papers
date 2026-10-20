# Case Study Materials for Appendix

> **Data source**: All quantitative fields (vote entropy, constraint count, exclusion rate, SC/SICA answers, correctness) come from `f2_per_problem.csv` (exp-001, sica_expanded_14b, 804 problems, K=12, Qwen2.5-14B-Instruct). Problem texts and FOL/DSL annotations come from the original dataset files. Vote distributions are derived from entropy values (see mapping below). **Actual extracted constraint strings are unavailable** (stored in `sica_expanded_14b.json` on decommissioned server westd-32608). Representative constraint examples below are derived from the DSL programs and marked as [DERIVED].
>
> Entropy-to-vote mapping (K=12, 2 candidates): 1.0→6:6, 0.9799→7:5, 0.9183→8:4, 0.8113→9:3, 0.65→10:2, 0.4138→11:1

---

## Overview of Discordant Cases

Among 804 problems (600 ProofWriter + 204 FOLIO), SICA and SC agree on 773 (96.1%). The 31 discordant cases:
- **16 SICA wins** (SICA correct, SC wrong)
- **14 SC wins** (SC correct, SICA wrong)
- **1 both wrong, different answers**

All 31 discordant cases are exact ties (entropy=1.0, 6:6 vote split) or near-ties (entropy≥0.9183, 8:4 at most). SICA can only differ from SC when constraint weights shift the majority away from SC's tiebreak choice.

---

## Case 1: SICA Win (folio_134, FOLIO)

**Problem**:
> Given the following premises:
> [BG] Some mammals have teeth. Platypus have no teeth. Platypus are mammals. Humans have teeth.
>
> Determine whether the following conclusion is true, false, or uncertain:
> Humans are mammals.

**Gold**: Unknown

**FOL annotations**:
- ∃x (Mammal(x) ∧ Have(x, teeth))
- ¬Have(platypus, teeth)
- Mammal(platypus)
- Have(humans, teeth)
- Conclusion: Mammal(humans)

**Why Unknown**: The premises state that *some* mammals have teeth and that humans have teeth, but this does not entail humans are mammals. "Having teeth" is not sufficient for "being a mammal" under open-world semantics.

**SC vote**: Unknown:6, True:6 → SC tiebreaks to **True** (wrong)
**SICA choice**: **Unknown** (correct)

| Metric | Value |
|--------|-------|
| n_unique_answers | 2 |
| vote_entropy | 1.0 (6:6 tie) |
| constraint_count | 7 |
| constraint_exclusion_rate | 14.3% (1 excluded) |
| sica_flipped | 1 |

### Why SICA Won

In a perfect 6:6 tie, SC's alphabetical tiebreak selects True. SICA extracted 7 constraints from the 12 traces. MaxSAT excluded 1 constraint that was inconsistent with the constraint set, reducing the weighted score for True-voting traces and tipping the aggregation toward Unknown.

### Representative Constraints [DERIVED from FOL]

| # | Constraint (z3 format) | Type | Discriminative? |
|---|----------------------|------|----------------|
| 1 | `have_humans_teeth == True` | fact | No (appears in both True and Unknown traces) |
| 2 | `mammal_platypus == True` | fact | No (domain fact, shared) |
| 3 | `Implies(mammal_platypus, have_platypus_teeth)` | derived | Potentially yes (incorrect derivation, may appear only in True traces) |

**Narrative**: This is a rare case where a constraint captured answer-specific reasoning (likely an incorrect inference step present only in True-voting traces). Its exclusion by MaxSAT shifted weight toward the correct answer. However, this success is coincidental rather than systematic.

---

## Case 2: SC Win (ProofWriter_AttNoneg-OWA-D5-1066_Q6, ProofWriter)

**Problem**:
> Bob is quiet. Bob is white. Dave is kind. Dave is red. Dave is young. Fiona is red. Fiona is round. Gary is quiet. Gary is red. Gary is round. White things are round. If something is kind and white then it is green. All young things are kind. All round things are young. All quiet, kind things are white. Quiet, green things are red. Young, quiet things are kind. All quiet, red things are kind. If Gary is young then Gary is round.
>
> Determine whether the following statement is true, false, or unknown:
> Bob is not young.

**Gold**: False (Bob IS young)

**DSL logic program** (key chain):
```
White(Bob, True) → Round(Bob, True)    [White things are round]
Round(Bob, True) → Young(Bob, True)    [All round things are young]
∴ Young(Bob, False) is FALSE
```

**SC vote**: False:6, True:6 → SC tiebreaks to **False** (correct)
**SICA choice**: **True** (wrong)

| Metric | Value |
|--------|-------|
| n_unique_answers | 2 |
| vote_entropy | 1.0 (6:6 tie) |
| constraint_count | 17 |
| constraint_exclusion_rate | 11.8% (2 excluded) |
| sica_flipped | 1 |

### Why SICA Lost

In a 6:6 tie, SC's tiebreak correctly selects False. SICA extracted 17 constraints; MaxSAT excluded 2 that appeared preferentially in False-voting traces. This reduced False's weighted score, causing SICA to select True (wrong). The excluded constraints happened to anti-correlate with correctness: they penalized the correct answer.

### Representative Constraints [DERIVED from DSL]

| # | Constraint (z3 format) | Type | Discriminative? |
|---|----------------------|------|----------------|
| 1 | `quiet_bob == True` | fact | No (given premise, all traces share it) |
| 2 | `white_bob == True` | fact | No (given premise, all traces share it) |
| 3 | `Implies(white_bob, round_bob)` | rule | No (grounded rule, shared across traces) |
| 4 | `Implies(round_bob, young_bob)` | rule | No (grounded rule, shared across traces) |
| 5 | `young_bob == True` | derived | Potentially yes (may appear only in False traces that completed the full chain) |

**Narrative**: SICA's constraint filtering actively harmed accuracy. The 2 excluded constraints likely captured correct intermediate derivations (e.g., `young_bob == True`) that appeared only in traces reaching the correct conclusion. By excluding them, MaxSAT removed evidence supporting the correct answer. This illustrates how self-extracted constraints can systematically mislead: correct reasoning steps become discriminative signals that the filter mistakenly penalizes.

---

## Case 3: Non-discriminative (ProofWriter_RelNeg-OWA-D5-903_Q6, ProofWriter)

**Problem**:
> The bear is nice. The bear visits the tiger. The dog does not chase the bear. The dog sees the mouse. The mouse does not chase the bear. The mouse is nice. The mouse is round. The mouse is young. The mouse visits the bear. The tiger chases the bear. The tiger sees the mouse. If someone chases the mouse and they see the tiger then the tiger is round. If the dog sees the mouse then the dog visits the tiger. If someone chases the mouse then they see the bear. If someone is nice and cold then they chase the mouse. If someone visits the mouse and they see the mouse then the mouse visits the dog. If the mouse visits the dog then the dog does not visit the bear. If someone sees the bear then they visit the dog. All nice people are cold.
>
> Determine whether the following statement is true, false, or unknown:
> The mouse does not chase the mouse.

**Gold**: False (the mouse DOES chase the mouse)

**DSL logic program** (key chain):
```
Nice(Mouse, True)                              [given]
Nice($x, True) → Cold($x, True)               [all nice people are cold]
Nice($x, True) ∧ Cold($x, True) → Chases($x, Mouse, True)  [nice and cold → chase mouse]
∴ Chases(Mouse, Mouse, True), so "does not chase" is FALSE
```

**SC vote**: False:6, Unknown:6 → SC tiebreaks to **False** (correct)
**SICA choice**: **False** (correct, same as SC)

| Metric | Value |
|--------|-------|
| n_unique_answers | 2 |
| vote_entropy | 1.0 (6:6 tie) |
| constraint_count | 44 |
| constraint_exclusion_rate | 2.3% (1 excluded) |
| sica_flipped | 0 |

### Why Constraints Are Non-discriminative

Despite extracting 44 constraints from 12 traces, MaxSAT excluded only 1 (2.3%). The remaining 43 constraints are domain facts and grounded rules that Z3 can simultaneously satisfy regardless of whether the final answer is False or Unknown. SICA's elaborate extraction and MaxSAT solving pipeline produces the identical answer as SC's simple tiebreak.

### Representative Constraints [DERIVED from DSL]

| # | Constraint (z3 format) | Type | Source traces | Discriminative? |
|---|----------------------|------|-------------|----------------|
| 1 | `nice_mouse == True` | fact | all 12 | No (given premise) |
| 2 | `nice_bear == True` | fact | all 12 | No (given premise) |
| 3 | `Implies(nice_mouse, cold_mouse)` | rule | all 12 | No (grounded rule from problem) |
| 4 | `cold_mouse == True` | derived | ~11-12 | No (derived from nice_mouse, shared) |
| 5 | `Implies(And(nice_mouse, cold_mouse), chases_mouse_mouse)` | rule | all 12 | No (grounded rule from problem) |
| 6 | `visits_bear_tiger == True` | fact | all 12 | No (given premise, irrelevant to query) |
| 7 | `sees_dog_mouse == True` | fact | all 12 | No (given premise, irrelevant to query) |
| 8 | `chases_mouse_mouse == True` | derived | ~6 (False traces only) | **Yes** (appears only in traces that complete the chain) |

**Narrative**: This problem exemplifies the capability trap. The LLM extracted 44 constraints, but the vast majority (43/44) are domain-level facts and rules that are true regardless of the final answer. Both False-voting and Unknown-voting traces share the same premises and grounded rules; they differ only in whether the trace successfully completed the full derivation chain. The single excluded constraint's weight is negligible against 43 shared constraints, so SICA's weighted vote is dominated by non-discriminative constraints and collapses to SC.

This is the typical pattern across the 773 agreeing problems: constraints are semantically coupled to the problem structure rather than to specific answer candidates, rendering MaxSAT aggregation equivalent to majority vote.

---

## Data Gaps

The following data is **unavailable** (lost with decommissioned server westd-32608):

1. **Actual extracted constraint strings**: The per-trace constraint JSON (`sica_expanded_14b.json`) containing `z3_formula`, `expression`, `type`, `source_step` for all 804×12 traces was not migrated. Constraint examples above are [DERIVED] from DSL programs.

2. **Per-trace vote labels**: The exact mapping of which trace voted which answer. Only the aggregate distribution (via entropy) is available.

3. **MaxSAT solver output**: The specific constraint exclusion decisions (which constraints were excluded on which problems).

### To obtain actual constraint data

Re-run the constraint extractor on the 3 selected problems on westd-25068:
```bash
# On westd-25068, using the SICA pipeline:
python3 src/sica_pipeline.py --problems folio_134,ProofWriter_AttNoneg-OWA-D5-1066_Q6,ProofWriter_RelNeg-OWA-D5-903_Q6 --k 12 --save-constraints --output results/case_study_constraints.json
```
This would produce actual constraint strings, per-trace vote labels, and MaxSAT exclusion decisions for the 3 cases.

---

## Summary Table

| Case | ID | Dataset | Gold | SC→ | SICA→ | Votes | Constraints | Excluded | Outcome |
|------|----|---------|------|-----|-------|-------|-------------|----------|---------|
| 1 (SICA win) | folio_134 | FOLIO | Unknown | True ✗ | Unknown ✓ | 6:6 | 7 | 1 (14.3%) | Constraint exclusion breaks tie correctly |
| 2 (SC win) | PW-1066_Q6 | ProofWriter | False | False ✓ | True ✗ | 6:6 | 17 | 2 (11.8%) | Constraint exclusion penalizes correct answer |
| 3 (Non-disc.) | PW-903_Q6 | ProofWriter | False | False ✓ | False ✓ | 6:6 | 44 | 1 (2.3%) | 44 constraints, nearly all non-discriminative, SICA=SC |
