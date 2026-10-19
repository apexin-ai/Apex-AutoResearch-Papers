---
name: diagnose-goal-blockers
description: Diagnose and recover persistent goals that appear stalled, paused, silently stopped, or repeatedly need user prompting. Use before restarting long-running experiments, builds, monitors, services, or benchmark campaigns when progress stops, a goal/monitor changes state, an operation remains started, reports are missing, or process and artifact evidence disagree.
---

# Diagnose Goal Blockers

Diagnose the control plane, execution plane, durable artifacts, and recovery contract before taking recovery action. Preserve completed work and never treat a status label as sufficient evidence by itself.

## Required order

1. Read the current goal and user stop/continuation instructions. Record the objective, status, elapsed time, and completion criteria.
2. Read the managed monitor state. Create or replace a failed/cancelled monitor through the approved monitor system; do not implement a shell polling loop.
3. Establish artifact truth. Count sealed units, inspect the newest durable timestamp, validate required reports, and identify the exact last terminal operation.
4. Establish process truth. Check the declared supervisor first, then its journal and child process tree. Distinguish `active`, clean exit, explicit stop, crash, and an unobservable service bus.
5. Establish operation truth. Reconcile every relevant `reserved`, `started`, `completed`, and `failed` event with its bound artifact.
6. Check revision and authority bindings: source commit/hash, staging snapshot, budget, credentials, remote environment, and Git working tree.
7. Classify the blocker using the decision table below. Take the narrowest recovery that preserves immutable receipts, spent budget, stream order, and test-then-learn boundaries.
8. Verify renewed growth with one new durable milestone. Re-establish managed monitoring and report exact progress, revision, branch, and push result.

For Moss benchmark campaigns, read [references/moss-recurring-blockers.md](references/moss-recurring-blockers.md) before recovery.

## Decision table

| Evidence | Classification | Action |
|---|---|---|
| Process alive and artifacts growing | Healthy | Do not restart; keep managed monitoring. |
| Process alive, within declared operation timeout | Possibly healthy | Wait through the managed monitor. |
| Process dead, no unfinished operation | Recoverable interruption | Resume the same immutable segment. |
| `started` plus valid bound artifact | Replayable interruption | Complete/replay through the trusted controller; do not re-execute. |
| `started` without bound artifact | Abandoned operation | Charge its reservation and never retry that operation ID. Use the experiment's explicit terminal-round recovery. |
| No terminal-round recovery exists | Code blocker | Add a red recovery test, implement the smallest contract-preserving fix, and start a clean revision segment if source binding prevents in-place recovery. Never hand-edit a ledger or forge a receipt. |
| Source/staging/gate hash changed | Binding mismatch | Do not resume the old segment with new code. Preserve it and create a newly named clean segment. |
| Monitor failed but workload is alive | Observability blocker | Recreate only the managed monitor; do not restart the workload. |
| Supervisor explicitly stopped and artifacts stopped | Execution blocker | Find who/what stopped it, reconcile in-flight work, then restart under a persistent supervisor. |
| Permission, secret, quota, or external authority is missing | External blocker | Exhaust read-only checks and safe parallel work; request only the minimum new authority. |

## Invariants

- Never rerun a completed operation or a started operation lacking its trusted result artifact.
- Never infer success from a live PID or infer failure from an inaccessible service bus.
- Never overwrite, delete, or manually repair append-only ledgers and sealed receipts.
- Never change a live segment's source revision, staging plan, evaluator gate, budget, arm order, or learning boundary.
- Never broaden authority because the goal says “continue” or “do not stop.”
- Do not mark the goal complete until every declared count and report validates.
- If a code or documentation checkpoint is required, stage only relevant files; follow the repository's sync/push rules and exclude secrets, runtime state, caches, and large experiment artifacts.

## Status report

Report: blocker classification and evidence; last durable milestone; exact completed/total counts; current operation; recovery taken; monitor ID/state; source revision; Git branch/commit/push result; and full artifact/report paths. Explicitly state what remains.
