# Moss Experiment 1B: Cross-Benchmark Frozen-Harness Stress Test

## Status and Relationship to Experiment 1A

This document adds a second, separately interpreted layer to the frozen
Experiment 1A contract. It does not modify Experiment 1A's within-benchmark A/B/C
lineages, eight-round budget, freeze rule, no-Builder 3x3 matrices, seed policy,
or success criterion.

Experiment 1A remains the confirmatory test of instance-conditioned Harness
specialization. Experiment 1B reuses the already frozen Harnesses to measure
whether their working structure transfers across EdgeBench and ALE-Bench.

## Research Question

When a Solver Harness evolved on one benchmark is frozen and rebound to a valid
target on the other benchmark, does it retain performance without Builder
adaptation?

Experiment 1B may support a claim of limited cross-benchmark compatibility or
cross-environment Harness mismatch. It may not, by itself, support a claim of
single-instance specialization because benchmark identity and instance identity
change together.

## Preregistered Transfer Pairs

The source and target pairs are fixed before any formal Experiment 1B model call.
They are selected by the A/B/C manifest positions, not by observed transfer score.
These are the same immutable mappings used by Experiment 1A: EdgeBench A/B/C are
`apple_incremental_game`/`molecular_self_assembly`/`treant_forest`, and ALE-Bench
A/B/C are `ahc024`/`ahc026`/`ahc011`.

| Pair | Frozen source Harness | Target |
|---|---|---|
| `edge-a-to-ale-a` | EdgeBench `apple_incremental_game` | ALE-Bench `ahc024` |
| `ale-a-to-edge-a` | ALE-Bench `ahc024` | EdgeBench `apple_incremental_game` |
| `edge-b-to-ale-b` | EdgeBench `molecular_self_assembly` | ALE-Bench `ahc026` |
| `ale-b-to-edge-b` | ALE-Bench `ahc026` | EdgeBench `molecular_self_assembly` |
| `edge-c-to-ale-c` | EdgeBench `treant_forest` | ALE-Bench `ahc011` |
| `ale-c-to-edge-c` | ALE-Bench `ahc011` | EdgeBench `treant_forest` |

The production JSON contains exactly these six immutable pair templates and the
allowed seed IDs `S1`, `S2`, and `S3`. It contains no not-yet-created freeze receipt
SHA, full Harness SHA, or H0 receipt locator. After the complete Experiment 1A gate
passes for one seed, the controller materializes a separate runtime binding receipt
or manifest for that seed with exactly six concrete pair entries. Each entry contains
its six-field source locator, target binding, and H0 receipt locator. Thus the static
manifest has six templates, not eighteen prebound SHA entries; `S1`, `S2`, and `S3`
produce separate six-entry runtime bindings when eligible.

No pair may be removed, replaced, or promoted because its pilot score is lower or
its later rescue headroom is larger. Any additional pair is exploratory until it
is confirmed in a new preregistered seed or target set.

## What Is Frozen and What Is Rebound

The source Harness is immutable. The transfer preserves its roles, Memory views,
parent-selection policy, abstract tool choices, workflow order, scheduler mode,
recovery mode, and Builder guidance already compiled into the frozen Harness.

The controller separately supplies the target binding:

- target task statement and public task data;
- target candidate codec and output contract;
- target implementation of registered abstract tools;
- target evaluator, score direction, timeout, and public feedback projection;
- fresh target workspace and operation IDs.

The controller must not copy source candidates, source target history, source
scores, source feedback, source paths, or source benchmark instructions into the
target attempt. Rebinding the target contract is not counted as Harness evolution.
If a frozen Harness names a component that cannot be implemented under the target
registry, the cell is invalid and is reported as a portability-contract failure,
not as low task performance.

## Execution Contract

For each shared Experiment 1A/1B seed ID (`S1`, `S2`, or `S3`) that produces valid
frozen Harnesses:

1. Verify the six pair identities against the static template manifest and verify all
   six frozen source receipts. A source receipt is eligible only when it is a valid
   `FreezeReceipt` backed by a valid numeric official score.
2. Materialize the seed's six-entry runtime binding receipt or manifest from verified
   Experiment 1A artifacts; do not mutate the static production JSON.
3. Create a new target workspace with no target history and no candidate reuse.
4. Do not construct, call, or emulate a Builder.
5. Perform exactly one Solver generation from the frozen source Harness.
6. Parse the candidate with the target codec and evaluate it once with the target
   official evaluator.
7. Store the candidate, codec receipt, evaluator receipt, model-call audit, target
   binding hash, and frozen Harness ancestry under the pair and seed root.
8. Never feed Experiment 1B outcomes back into Experiment 1A or use them to select
   which formal pairs are reported.

For a given seed, Experiment 1B begins only after both benchmarks have completed all
three Experiment 1A eight-round evolution lineages, issued their valid numeric-score
freeze receipts, and completed their formal 3x3 matrices for that same seed. It adds
no new eight-round evolution lineage.

Within a seed's runtime binding, every frozen source is referenced by a canonical
source locator binding exactly `benchmark`, `position`, `instance`, `seed`,
`freeze_receipt_sha`, and `full_harness_sha`. All six fields must match the verified
Experiment 1A artifacts; no path-only, receipt-only, or Harness-only locator is valid.

## Validity Gates

Every pair is classified before score interpretation:

- `valid_scored`: target codec accepted the candidate and the official evaluator
  returned a numeric score;
- `candidate_invalid`: the Solver output violated the target answer contract;
- `harness_incompatible`: the frozen Harness referenced a component unavailable
  under the target registry;
- `evaluator_failed`: the official evaluator failed without a benchmark-defined
  terminal task result;
- `audit_failed`: required receipts, hashes, or operation records are missing or
  inconsistent.

Candidate-invalid and Harness-incompatible cells are reported separately. They
must not be silently converted into a numeric floor and used as the main evidence
of task-performance specialization.

## H0 Baseline Contract

The target-local H0 comparison uses the Experiment 1A `H0BaselineReceipt` for the
same target and shared seed ID. Each receipt comes from its own fresh target/seed
root, and no Builder is constructed or called. Its
`upper_model_configuration_hash` identifies the formal upper-layer Builder
Harness model configuration, configured but not called in H0; its
`lower_model_configuration_hash` identifies the formal lower-layer Task
Harness/Solver model configuration. Each canonical payload contains only provider,
API family and transport, model, `reasoning_effort`, `max_output_tokens`, sampling
parameters, and tool permission policy, excluding prompt, Harness content, operation
ID, and task binding. The hashes must be equal to prove both layers use
`gpt-5.6-sol` with effort `high`. This does not represent two Solver calls: the call
ledger must record Builder calls `0`, Solver calls `1`, and official evaluator calls
`1`. A receipt that reuses a formal pair root, has unequal hashes, or has any other
call count is invalid.

## Analysis

Raw EdgeBench and ALE-Bench scores are never subtracted from each other or pooled
into one mean. Analysis is target-local.

For each target, compare the cross-benchmark transferred Harness with:

- the Experiment 1A target-native frozen Harness evaluated on that target;
- the common `H0` one-shot baseline evaluated under the same target binding, model,
  effort, token limit, and evaluator budget.

Report:

- valid-scored rate and each invalidity category;
- target-local native-minus-transfer score difference;
- target-local transfer-minus-H0 score difference;
- rank of native, transferred, and H0 within each target;
- direction consistency across the three declared seeds.

The six transfer cells are not six independent benchmarks. Seed repeats measure
model-run stability, not new task diversity.

## Interpretation Rules

Experiment 1B supports limited cross-benchmark compatibility when preregistered,
valid-scored transferred Harnesses consistently underperform the target-native
Harness on the same target.

If invalidity dominates, the result is an interface-portability finding, not a
performance-specialization finding. If transferred Harnesses match or beat native
Harnesses, that is evidence against broad cross-benchmark mismatch for these
pairs and must be reported without pair replacement.

Experiment 2 may start Builder rescue from these exact frozen pair roots, but its
outcomes belong to a separate experiment. Experiment 1B itself never adapts a
Harness.

## Required Evidence

Each formal pair receipt binds:

- its seed-specific six-entry runtime binding receipt or manifest and corresponding
  immutable pair template;
- the canonical source locator fields `benchmark`, `position`, `instance`, `seed`,
  `freeze_receipt_sha`, and `full_harness_sha`;
- source and target benchmark IDs, instance IDs, shared seed ID, and A/B/C positions;
- target codec, evaluator, dataset, source revision, image, timeout, and score
  direction digests;
- model, provider, reasoning effort, prompt/response hashes, token usage, and
  operation ID;
- candidate SHA and structural summary without answer text;
- private evaluator evidence SHA and allowlisted public result;
- proof that no Builder was constructed or called;
- fresh workspace identity and absence of target history.

Each reported H0 comparison additionally binds its valid `H0BaselineReceipt`, fresh
target/seed root, no-Builder-construction proof, canonical upper/lower model
configuration payloads and equal hashes, and audited Builder/Solver/official-evaluator
call counts of `0`/`1`/`1`.

Canaries, adapter fixtures, failed setup, and Experiment 2 rescue attempts are kept
outside the formal Experiment 1B roots.
