# ApexTune × AIF360 historical structure trajectories

This archive preserves seven completed historical diagnostic runs across four
implementation generations. `code-v1` ran two independent rounds, `code-v2` and
`code-v3` one round each, and `code-v4` — the QD search architecture described
in `ARCHITECTURE_QD_V4.md` — completed the full three-round protocol
(round/seed = 1/0, 2/1, 3/2). All runs used `gpt-5.6-sol` against a
reconstructed AIF360 checkout, so they are explicitly non-comparable and
leaderboard-ineligible.

| Code | Round | Run | LLM requests | Validated structures | Generation failures | Validations | HPO variants | Final AOD ↓ | Accuracy | Score ↑ |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| code-v1 | 1 | `aif360-r1-gpt56sol-20260906` | 429 | 100 | 329 | 100 | 0 | 0.012598005817510527 | 0.630297565374211 | 0.22726459004654495 |
| code-v1 | 2 | `aif360-r2-gpt56sol-20260907` | 211 | 100 | 111 | 100 | 0 | 0.011120493106355073 | 0.6429215509467989 | 0.2287421027577004 |
| code-v2 | 1 | `aif360-integration-gpt56sol-r1-datasetfix-20260909` | 29 | 29 | 0 | 100 | 71 | 0.021053621638746994 | 0.6257889990982868 | 0.21880897422530848 |
| code-v3 | 1 | `aif360-gpt56sol-structurefirst-v3-r1-20260909` | 130 | 98 | 23 | 100 | 2 | 0.05288121545398486 | 0.6348061316501352 | 0.18698138041007062 |
| code-v4 | 1 | `aif360-gpt56sol-qd-v4-r1-20260911` | 111 | 91 | 20 | 100 | 9 | 0.011120493106355073 | 0.6429215509467989 | 0.2287421027577004 |
| code-v4 | 2 | `aif360-gpt56sol-qd-v4-r2-20260912` | 103 | 80 | 23 | 100 | 20 | 0.05288121545398486 | 0.6348061316501352 | 0.18698138041007062 |
| code-v4 | 3 | `aif360-gpt56sol-qd-v4-r3-20260912` | 118 | 94 | 24 | 100 | 6 | 0.012598005817510527 | 0.630297565374211 | 0.22726459004654495 |

## code-v4 three-round aggregate

`code-v4/three_rounds_qd_v4.json` is the auditable three-round aggregate produced by
`apextune-fml-report` (per-round `audit_errors=[]`): normalized score mean
`0.21432935773810532` ± sample std `0.023695562008611056` (min `0.18698138041007062` /
max `0.2287421027577004`). The aggregate reports `complete=false` solely for the
expected protocol-identity reasons (diagnostic model `gpt-5.6-sol`, reconstructed
checkout); every per-round budget and evidence audit passes.

## Structure identity

Every logical LLM request receives a stable run-local ID of the form
`aif360-code-vN-rR-apextune-structure-NNNN`. This is the authoritative grouping
key in the added indexes:

- `APEXTUNE_STRUCTURE_INDEX.jsonl`: one record per LLM request, including requests rejected before validation.
- `APEXTUNE_VALIDATION_TRAJECTORY.jsonl`: one record per full evaluator execution.
- `variant_kind=structure_default`: the first/default code snapshot for that LLM request.
- `variant_kind=hpo_variant`: a locally materialized knob setting sharing the same LLM-proposed structure.
- `code-v4` rows additionally carry `archive_cell` (behaviour-axis cell), `ast_structure_bucket` (audit-only AST bucket), `admission_kind`, and `pooled`.

The original run state, manifests, seed code, and all step snapshots are copied
without modification. Added labels and indexes are derived views; `SHA256SUMS`
files make the uploaded bytes independently verifiable.

## Metric interpretation

The optimization metric is absolute average odds difference (`abs_aod_mean`),
lower is better. Accuracy is a hard validity constraint. The final normalized
score is `max(0, 0.23986259586405548 - abs_aod)` and is therefore higher when
final AOD is lower. Validation and final-test accuracy thresholds differ
according to the preserved benchmark protocol.

## QD-v4 provenance

Implementation commits on `feat/fml-apextune-integration` (agent-ml-research):
{
  "audit_fix_failed_steps": "c5e2b303c",
  "baseline_freeze": "384bc6c4570e6b4bb2e76efc53cbd47e53e7bdca",
  "batch_bandit": "4ece41477",
  "behaviour_axes": "841b0104c",
  "epsilon_elite_pool": "a1440296c",
  "stall_response": "2da4922df"
}

The audit fix (`c5e2b303c`) is part of this collection's provenance: the round
auditor previously demanded the primary metric on failed validation steps, so
the first real three-round aggregation (containing honest evaluator failures)
reported incomplete; the presence requirement is now gated on
`val_result.success is true`, matching every other per-step audit rule.
