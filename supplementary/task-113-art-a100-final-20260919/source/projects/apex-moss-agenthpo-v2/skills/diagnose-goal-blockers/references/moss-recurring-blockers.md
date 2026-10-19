# Moss recurring goal blockers

Use this catalog only for Moss long-running benchmark and harness goals. Re-check current artifacts; historical examples are diagnostic patterns, not current facts.

## Control-plane drift

- The persistent goal may be `paused` while a systemd workload is still running, or it may remain `active` after the workload disappeared.
- A CCM monitor may be `failed`, `cancelled`, or have zero checks even while the workload grows.
- User-session lifecycle actions can explicitly stop a transient user service. Confirm with `journalctl --user`; a vanished transient unit alone does not show why it ended.

Treat goal, monitor, service, and artifact states as four independent signals. The durable artifact ledger is the progress authority; the trusted supervisor journal is the process-lifecycle authority.

## Service observability

- User systemd checks may require `XDG_RUNTIME_DIR=/run/user/1000` and `DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus`.
- A sandboxed monitor may receive `Failed to connect to bus` or see no matching PID. Record this as unobservable, not dead.
- When the unit was explicitly stopped, journal entries `Stopping` and `Stopped` plus no process and no artifact growth establish an execution stop.

## Append-only operation recovery

- Reconcile the trusted operation journal before restarting.
- `completed`: replay only.
- `started` with the exact bound result artifact: complete/replay without calling the provider/evaluator again.
- `started` without a result artifact: permanently abandoned and conservatively charged. Never retry the same operation ID.
- `reserved` without start: follow the frozen controller's documented recovery; do not assume it was consumed.
- If an abandoned planner, solution, or evaluator operation leaves its round unsealable, the runner lacks a required recovery transition. Write a red test and implement an explicit zero-score terminal outcome; do not synthesize JSON receipts or append ledger events by hand.

## Revision and segment binding

- Formal staging binds the Git revision and source/gate hashes. Editing bound source during a live segment invalidates recovery.
- Preserve a stopped segment as evidence. If a recovery implementation changes bound source, use a new clean revision segment and document which prior operations were consumed but not reused.
- Keep live outputs under `results/` and control state under `.claude-manager/` out of Git unless the user explicitly requests otherwise.

## Repeated Moss contract failures

- Model JSON can omit required top-level fields despite valid inner content. Fix the task card with a literal complete template; do not weaken the strict codec.
- Planner decisions can compile to no operational change or violate the Harness schema. Seal these as contract-rejected zero-score rounds, preserve the consumed planner call, and skip solution/evaluator calls.
- Old canary failures can coexist with a valid newer segment. Bind diagnoses to the exact segment and revision.
- Remote evaluator capability can be unavailable while local artifacts remain healthy. Use the frozen gate and trusted controller result, not candidate stdout or inferred remote state.

## Recovery proof

After recovery, require at least one newly sealed round/arm/instance or a newly terminal operation. Then confirm stream order, cell entitlement, checkpoint/bank hashes, and learning boundary are unchanged before declaring the workload healthy.
