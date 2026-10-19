---
name: validate-generated-artifacts
description: Validate model-generated code, configs, prompts, harnesses, and other executable artifacts before costly, official, or irreversible runs. Use when a workflow extracts code from model output, relies on tool/API contracts, evaluates generated agents, resumes cached or budgeted experiments, runs partial decision matrices, or could confuse infrastructure failures with capability results.
---

# Validate Generated Artifacts

Treat generated artifacts as untrusted build output. Do not send them directly into a
full experiment.

## Keep execution and design separate

Start in execution mode when following an accepted plan.

Before inventing a new implementation path, architecture, mechanism, or non-obvious
tradeoff:

1. Stop editing.
2. Send the user a self-contained handoff prompt with these fields: project goal,
   current context, completed work, key evidence/data, reason for leaving the plan,
   design question, immutable constraints, and expected output.
3. Tell the user that the work is leaving the current plan and entering design mode.
4. Wait for the user to decide whether to switch to a stronger model.

Keep obvious typo fixes, already-specified contract fixes, and regression tests in
execution mode. Escalate when a local fix grows into a new mechanism.

## Write the contract first

Specify every boundary in machine-checkable terms:

- Required files, symbols, signatures, and frozen values.
- Allowed imports and side effects.
- Tool input keys and argument shape.
- Tool return types and fields.
- Expected result schema and error policy.
- Environment/config precedence when the process may inherit unrelated credentials
  or endpoints; verify the resolved values before starting workers.

Include the exact contract in the generator prompt. Do not rely on function names or
natural-language summaries to imply types.

## Apply gates in order

1. Preserve the raw generator response for diagnosis.
2. Extract the outer artifact robustly. If generated source may contain Markdown
   fences in its own strings, pair the first opening fence with the last closing
   fence; never stop at the first inner fence.
3. Parse or compile the complete artifact.
4. Statically validate the contract, including tool argument keys and return-value
   use.
5. Run an offline contract smoke test with fake tools/API responses when practical.
6. Run one cheap canary task.
7. Only then start the full official run.

Turn each discovered boundary failure into a regression test before rerunning.

## Protect experiment validity

Treat a run as infrastructure-invalid when any candidate has import errors, contract
exceptions, missing result files, implausible zero steps/tokens, or uniform near-zero
latency inconsistent with real execution.

- Do not interpret infrastructure-invalid scores as model capability.
- Move invalid outputs outside the official result path; preserve them for audit.
- Invalidate affected checkpoints and caches explicitly.
- Regenerate using only the original allowed inputs plus contract errors. Never feed
  benchmark items, validation traces, or scores back into a zero-shot generator.
- Do not change benchmarks, scoring rules, repeats, or thresholds during recovery.
- Require zero harness errors before accepting an official summary.

After completion, inspect representative per-run records as well as aggregate scores.
Confirm normal steps, tokens, elapsed time, no tampering, and no hidden exceptions.

## Make budget and recovery auditable

- Count every model call in the experiment budget: valid runs, invalid attempts,
  canaries, probes, repairs, and interrupted calls when usage is known. Mark unknown
  interrupted usage explicitly; never silently treat it as zero.
- Write canary usage to the same restart-safe ledger as formal cells. On resume,
  reuse a valid cached canary without charging it twice.
- Distinguish provider rate-window headers from prepaid balance. A successful probe
  proves reachability, not monetary credit, unless the provider exposes that field.
- Key cached results by the artifact content hash as well as the version label.
  When a generated candidate changes, isolate or invalidate every old canary/result
  derived from the previous hash before rerunning.
- Persist the cell about to run before starting it. On any pause, record the cell
  that was blocked or failed, not the previously completed cell.
- Separate matrix completeness from decision completeness. A pre-registered
  low-value cell may be omitted by a budget rule only when the frozen decision is
  already identifiable; report both the missing cells and `decision_complete`.
- Treat a one-task canary as a contract/infra gate, not a capability selector.
  Capability failure may be valid, and canary score must not choose a version.

## Turn failures into durable prevention

For every failure or repeated inefficiency:

1. Preserve and classify the raw artifact/result before changing code.
2. Decide whether it is instance-specific or a reusable boundary failure.
3. Write a regression test that fails for the observed case before applying the fix.
4. If the lesson crosses scripts or experiment rounds, add the concise prevention
   rule to this Skill. Put instance evidence, cost, and commit IDs in `PROGRESS.md`;
   put architecture/contract changes in `CLAUDE.md`.
5. Re-run the narrow regression, then the full offline suite before any new model
   call.

Do not put benchmark-specific task IDs, scores, hidden traces, or one-off repair text
in this Skill. Store only transferable process rules.

## Finish the loop

Run the full test suite, record invalid attempts separately in the report, and state
which conclusions are valid, invalid, or blocked by ceiling effects. Add the failure,
fix, prevention rule, and final commit ID to the project's progress log.
