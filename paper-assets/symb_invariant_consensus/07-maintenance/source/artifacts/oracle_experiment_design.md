# Oracle Extraction Experiment Design

## 1. FOLIO Gold FOL Format

`data/folio_full.json` contains 204 problems. Each has structured fields with human-annotated FOL:

| Field | Type | Description |
|-------|------|-------------|
| `premises` | list[str] | NL premise sentences |
| `conclusion` | str | NL conclusion sentence |
| `premises_fol` | list[str] | Per-premise FOL formulas (1:1 with `premises`) |
| `conclusion_fol` | str | FOL formula for the conclusion |
| `answer` | str | Gold label: True / False / Unknown |

FOL syntax uses Unicode quantifiers and connectives: `∀x`, `→`, `¬`, `∧`, `∨`, `⊕` (XOR), with `Predicate(entity)` notation.

**Example (folio_000):**
```
premises_fol:
  - ∀x (TalentShows(x) → Engaged(x))
  - ∀x (TalentShows(x) ∨ Inactive(x))
  - ∀x (Chaperone(x) → ¬Students(x))
  - ∀x (Inactive(x) → Chaperone(x))
  - ∀x (AcademicCareer(x) → Students(x))
  - (Engaged(bonnie) ∧ Students(bonnie)) ⊕ (¬Engaged(bonnie) ∧ ¬Students(bonnie))

conclusion_fol: Engaged(bonnie)
answer: Unknown
```

**Example (folio_003):**
```
premises_fol:
  - ∀x (Meeting(x) → AppearInCompany(x))
  - ∀x (LunchInCompany(x) → Meetings(x))
  - ∀x (LunchInCompany(x) ∨ LunchAtHome(x))
  - ∀x (LunchAtHome(x) → WorkRemotelyFromHome(x))
  - ∀x (InOtherCountries(x) → WorkRemotelyFromHome(x))
  - ∀x (Manager(x) → ¬WorkRemotelyFromHome(x))
  - Manager(james) ⊕ AppearInCompany(james)

conclusion_fol: LunchInCompany(james)
answer: Unknown
```

## 2. Three Oracle Schemes

### (a) Per-trace FOL Verification + MAX-SAT Aggregation

Each of k traces produces a candidate answer (True/False/Unknown). Gold FOL premises + conclusion are encoded into Z3. For each trace, check whether its candidate answer is logically consistent with the gold FOL:
- Answer "True" is consistent iff `premises ⊨ conclusion`
- Answer "False" is consistent iff `premises ⊨ ¬conclusion`
- Answer "Unknown" is consistent iff neither entailment holds

Each trace gets a binary consistency score (1 = consistent, 0 = inconsistent). MAX-SAT aggregation then selects the answer that maximizes total consistency-weighted support across traces.

- **Tests**: Whether constraint-based scoring with perfect constraints helps select better answers than raw majority vote.
- **Controls**: Extraction quality (replaced by gold FOL), isolating the aggregation mechanism.
- **SICA correspondence**: Replaces the "LLM constraint extraction" step; preserves per-trace scoring and MAX-SAT aggregation structure.
- **Answers core question**: Yes, directly. If gold-FOL+MAX-SAT > SC, aggregation adds value and the bottleneck is extraction. If gold-FOL+MAX-SAT = SC, aggregation itself is insufficient.

### (b) Shared Constraint Set (Direct FOL Solving)

Gold FOL premises + conclusion are fed to Z3 once to determine the correct label. All traces share this single oracle verdict.

- **Tests**: Whether gold FOL + Z3 can solve FOLIO (a prover ceiling, not an aggregation test).
- **Controls**: Everything (no LLM involved at inference).
- **SICA correspondence**: None. Eliminates both extraction AND aggregation. Changes SICA's core per-trace structure to a single global check.
- **Answers core question**: No. This bypasses aggregation entirely, so it cannot tell us whether aggregation adds value.

### (c) Per-trace Reasoning Chain Verification

Gold FOL is used to verify logical consistency of each trace's full reasoning chain (not just the final answer). Invalid traces are filtered before voting.

- **Tests**: Whether filtering logically invalid traces improves voting.
- **Controls**: Reasoning chain quality (verified by gold FOL).
- **SICA correspondence**: Closer to Logic-LM (single-trace verification) than SICA (cross-trace aggregation). Does not use MAX-SAT.
- **Answers core question**: Only partially. Tests trace filtering, not constraint aggregation.

## 3. Recommendation: Scheme (a)

Scheme (a) is the only design that isolates extraction quality while preserving SICA's aggregation mechanism. Scheme (b) solves the problem directly, bypassing aggregation entirely, making it useless for testing SICA's core claim. Scheme (c) tests trace filtering (a Logic-LM paradigm), not constraint aggregation (the SICA paradigm).

One subtlety: since gold FOL gives complete (not partial) constraints, scheme (a) provides an **upper bound** on what perfect extraction could achieve. Real extraction produces partial, noisy constraints, so oracle results represent the ceiling of the extraction-dependent pathway.

## 4. Input / Output / Evaluation Protocol

### Input
- **Gold FOL**: `data/folio_full.json` (fields: `premises_fol`, `conclusion_fol`, `answer`)
- **Trace data**: `results/sica_expanded_14b.json` — Qwen2.5-14B-Instruct traces from exp-001, FOLIO subset (k=12 traces per problem, n=204)
- Reuse exp-001's existing traces and candidate answers; only replace the constraint extraction + scoring step

### Output Metrics
- Accuracy per method
- Delta (pp) between methods with 95% CI (bootstrap)
- McNemar's test p-value for pairwise significance

### Three-way Comparison

| Condition | Extraction | Aggregation | Source |
|-----------|-----------|-------------|--------|
| SC (baseline) | N/A | Majority vote | exp-001 (sica_expanded_14b) |
| SICA (self-extracted) | LLM | MAX-SAT | exp-001 (sica_expanded_14b) |
| Oracle-SICA | Gold FOL + Z3 | MAX-SAT | New experiment |

### Interpretation Framework

| Outcome | Interpretation | Implication |
|---------|---------------|-------------|
| Oracle-SICA > SC | Aggregation mechanism works; extraction quality is the bottleneck | Improve extraction (better prompts, specialized models, hybrid approaches) |
| Oracle-SICA ≈ SC | Even perfect constraints do not make MAX-SAT beat voting | Aggregation mechanism needs redesign or the problem class doesn't benefit from symbolic aggregation |
| Oracle-SICA < SC | Gold FOL integration with trace answers has implementation issues | Debug Z3 encoding or FOL parsing before drawing conclusions |
