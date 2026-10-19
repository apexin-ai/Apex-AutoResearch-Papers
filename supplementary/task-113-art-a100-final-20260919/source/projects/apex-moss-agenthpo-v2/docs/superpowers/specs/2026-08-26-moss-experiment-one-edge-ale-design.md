# Moss Experiment One: EdgeBench and ALE-Bench Design

## Goal

Run a reproducible test of instance-specific Harness specialization on official,
locally scoreable benchmarks. Every benchmark uses the same immutable experiment
contract: three instances A/B/C start from byte-identical Task Harnesses, evolve in
fully isolated workspaces for eight scored rounds, freeze the best accepted Harness
per lineage, and then run a no-evolution 3x3 cross matrix.

This experiment tests Harness specialization. It does not claim an official
leaderboard result because it uses a fixed eight-round budget rather than each
benchmark's full official time budget.

ALE-Bench currently exposes 40 tasks, including a 10-task Lite subset. Its official
paper comparison budget is at most four hours per problem. EdgeBench exposes 51 tasks
and uses a 12-hour official budget. The formal pair below is a Moss mechanism test,
while any later leaderboard campaign must use those separate official time budgets.

## Frozen Scope

- Moss source baseline: `a75f4dc3e6f29754690af2a10b146e57de4d8dd1` plus the
  experiment-one implementation commit.
- Builder model: `gpt-5.6-sol`, Responses API, reasoning effort `high`.
- Solver model: `gpt-5.6-sol`, Responses API, reasoning effort `high`.
- EdgeBench source: `a87350ab80eeb320b13cb71d1b0c3ffcc20a670f`.
- EdgeBench task data: `6cc5a7f1b3288ce52484ad828177b8cc86b05b75`.
- EdgeBench A/B/C are `apple_incremental_game`, `molecular_self_assembly`, and
  `treant_forest`, respectively.
- ALE-Bench source: `f7d927906dc1dcd860ee086e4560d576438b1354`.
- ALE-Bench task data: `0f426173b4e4e73b09b2b3631ae0490f66b75f99`.
- ALE-Bench A/B/C are `ahc024`, `ahc026`, and `ahc011`, respectively. The evaluator
  canary task `ahc027` is ineligible.
- Evolution budget: eight valid or terminal scored rounds per lineage.
- Replication seed IDs are exactly `S1`, `S2`, and `S3`, shared unchanged with
  Experiment 1B. Run `S1` first; if all nine cells are valid, repeat the complete
  experiment for `S2` and `S3`. A single-seed result is labelled preliminary.

## Immutable Experiment Contract

The following rules are benchmark-independent and cannot be changed to accommodate
an individual benchmark:

- exactly three formal instances, named A, B, and C;
- byte-identical `H_0`, model identities, reasoning effort, and eight-round budget;
- isolated Harness, Memory, candidate, score, and operation journals per lineage;
- one frozen native Harness per lineage: `H_A`, `H_B`, and `H_C`;
- nine fresh no-Builder cross cells: every frozen Harness on every target;
- one `H0BaselineReceipt` per target and seed from a fresh root, with no Builder
  construction or call,
  `upper_model_configuration_hash == lower_model_configuration_hash`, Builder calls
  `0`, Solver calls `1`, and official evaluator calls `1`;
- target IDs, submission paths, evaluator commands, and score direction remain in
  controller-owned target bindings, never in the transferable Harness;
- each cross cell has no target history and performs one Solver generation followed
  by one official evaluation;
- native scores are reported per benchmark; scores from different benchmarks are
  never pooled into one mean.

For `H0BaselineReceipt`, `upper_model_configuration_hash` identifies the formal
upper-layer Builder Harness model configuration even though H0 never calls the
Builder. `lower_model_configuration_hash` identifies the formal lower-layer Task
Harness/Solver model configuration. Their canonical payload contains only provider,
API family and transport, model, `reasoning_effort`, `max_output_tokens`, sampling
parameters, and tool permission policy. It excludes prompt text, Harness content,
operation ID, and task binding. The hashes must be equal, proving both layers are
configured as `gpt-5.6-sol` with effort `high`; these are two configured layer roles,
not two Solver calls. The H0 call ledger remains Builder calls `0` and Solver calls
`1`.

### Change-Control Rule

Adding or replacing a benchmark may change only the three pinned instance IDs, the
official evaluator adapter, the score direction/scale, and the declared machine
resource envelope. It may not change the A/B/C design, `H_0`, model settings,
eight-round budget, isolation boundary, Builder-visible information, freeze rule,
no-Builder 3x3 cross-test, seed policy, or success criterion. If a benchmark cannot
run under this contract, it is excluded rather than given a benchmark-specific
experiment setting.

The matrix is always interpreted target by target:

- on target A, compare `H_A -> A` with `H_B -> A` and `H_C -> A`;
- on target B, compare `H_B -> B` with `H_A -> B` and `H_C -> B`;
- on target C, compare `H_C -> C` with `H_A -> C` and `H_B -> C`.

Thus every comparison uses the same target and the same official scoring rule. A
high native score for `H_B -> B` is produced by B's independent eight-round
evolution from `H_0`; it is not obtained by adapting `H_A` to B. Rescuing a poor
transferred Harness on a new target belongs to Experiment Two, not Experiment One.

## What Changes During Evolution

The fixed Python controller does not write arbitrary agent code. The Builder Harness
may propose a new typed Task Harness by changing the ordered model/tool nodes, their
roles, bounded instructions, allowed memory input, and verification flow. The
controller validates the proposal and either commits it as `H_(t+1)` or keeps `H_t`.

The candidate answer is a separate artifact. EdgeBench candidates are target-bound
file bundles. ALE-Bench candidates are target-bound source-code submissions. Output
contracts, target identifiers, evaluator commands, and hidden judge data are fixed
   outside the evolving Harness, so a cross-test cannot fail merely because a source
   Harness contains its native submission path or problem identifier.

## Information Boundary

During an evolution round the Builder may see:

- the current and historical Task Harness structures;
- each prior public score;
- an allowlisted public status and short feedback summary;
- candidate structural summaries such as file count, language, code size, or compile
  status;
- parent/child Harness hashes and whether a proposal was accepted or rolled back.

The Builder may not see hidden expected outputs, private inputs, reference solutions,
private seeds, raw judge logs, stack traces containing private paths, or final private
rank/performance. Raw candidate answers remain in the private experiment archive and
are not copied into Builder memory as free-form text.

ALE-Bench evolution, H0 baselines, and all frozen cross cells use the official
`public_eval` numeric score. A fresh cross candidate cannot legally reuse the
freeze authorization bound to a different candidate SHA, so private evaluation is
not part of the 3x3 matrix and no private rank or hidden-test claim is made.
EdgeBench follows its official repeated hidden judge interface during evolution,
but cross cells are one-shot `sforge eval` calls with no feedback loop.

## Experiment Flow

1. Preflight pins source, task data, Docker image digests, model route, CPU/memory,
   disk, and the execution contract.
2. Evaluator canaries run reference/known-invalid artifacts without model calls.
3. For each benchmark, create A, B, and C workspaces with byte-identical `H_0`.
4. Run A, B, and C independently for eight rounds. Each round executes the current Task
   Harness, validates the candidate, scores it, records public feedback, runs the
   Builder Harness, and commits or rolls back the proposed next Harness.
5. Freeze each lineage's best-scoring accepted Harness using a deterministic rule:
   highest normalized score, then earliest round, then lexical Harness SHA. A valid
   `FreezeReceipt` may be issued only when the selected Harness has a valid numeric
   score from the official evaluator; a missing, invalid, or non-numeric score cannot
   authorize a valid freeze.
6. Create nine fresh cross workspaces. For each source Harness and target instance,
   generate one target-valid candidate with no prior target history and no Builder
   call, then score it once.
7. For each target and seed, create a fresh root and issue one `H0BaselineReceipt`
   after exactly one `H0` Solver call and one official evaluator call, with no Builder
   call and equal `upper_model_configuration_hash` and
   `lower_model_configuration_hash` values.
8. Report the native 3x3 score matrix, diagonal-minus-off-diagonal differences,
   reciprocal specialization, validity, and all Harness/candidate/evaluator hashes.

## Required Evidence

Every formal result must bind:

- benchmark/source/task/image digests;
- Moss revision and clean tracked-tree digest;
- model, transport, reasoning effort, API base host hash, and usage;
- task, lineage, round, seed, current Harness SHA, candidate SHA, and parent SHA;
- public result plus SHA of private evaluator evidence;
- freeze decision, valid numeric official score, and complete Harness ancestry;
- cross-test proof that no Builder was constructed or called;
- `H0BaselineReceipt` target/seed identity, fresh-root proof, no-Builder proof,
  canonical upper-/lower-layer model configuration payloads and equal hashes, plus
  Builder/Solver/evaluator call counts of `0`/`1`/`1`;
- append-only operation journal head and recovery status.

Canary, fixture, compile-only, and failed setup events are stored separately and never
reported as formal experiment rounds.

## Success Criteria

The mechanism is supported on a benchmark when each native Harness beats both
transferred Harnesses on its own target, all nine cross cells are valid, and every
target's diagonal advantage has the same sign across three seeds. A one-seed or
one-/two-target effect is reported as preliminary evidence only. If contract failures
dominate, the benchmark is invalid for the specialization claim and must not be
interpreted as overfitting.
