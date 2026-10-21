# analysis failure unification table

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 5
- **Recorded user turns:** 0
- **Tool calls:** 2
- **Original source:** `logs/chats/worker_analysis_failure_unification_table_20260517T051130.jsonl`
- **Structured JSON:** [`aebf5d8f7e05943b5627.json`](../../sessions/ae/aebf5d8f7e05943b5627.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

5 recorded events

### Tool call

_source line 1 · 2026-05-17T05:12:17.092675+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_failure_unification_table_20260517T051130",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-17T05:12:17.093146+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_failure_unification_table_20260517T051130",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T05:12:17.093476+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-17606",
  "command": "mkdir -p /root/cost-verify-agent-rl/analysis && cat > /root/cost-verify-agent-rl/analysis/failure_unification_table.md << 'ENDOFFILE'\n# Failure Mode Unification: Step-Independent Credit Assignment as Root Cause\n\n## Summary\n\nAll four negative GRPO experiments (exp013f, exp020b, exp026, exp027) exhibit distinct surface symptoms (reward gaming, policy collapse, catastrophic forgetting) yet share a single root cause: step-independent optimization fundamentally cannot assign credit across multi-turn trajectories. The attempted fixes (bonus ratio tuning, KL constraints, LR reduction, entropy bonuses) addressed symptoms without resolving the structural inability to propagate task-level signal through sequential decisions. Episode-level training (exp029) with the same SFT checkpoint achieved 28.125% stable success, confirming the diagnosis.\n\n## Unification Table\n\n| Experiment | Surface Symptom | Attempted Fix | Actual Root Cause | Key Evidence |\n|------------|----------------|---------------|-------------------|--------------|\n| exp013f | Reward gaming: action_is_valid 60%→97.5%, task success 0% | Reduce bonus ratio (1:67→1:1000), success-gated reward | Step-independent optimization maximizes per-step bonus without requiring task completion | Cumulative bonus (29×0.15=4.5) dominated sparse success reward (10.0); episode-level constrains bonus optimization to full trajectories |\n| exp020b | Policy collapse: success 20%→4.69%, entropy collapse 61%, pass@16 75%→25% | Increase KL constraint, fix response_mask, adjust LR | Per-step GRPO destroys inter-step correlations learned by SFT | Entropy 0.107→0.042; model collapsed to \"safe\" per-step actions, losing sequential planning ability |\n| exp026 | Catastrophic collapse: train success peaks 32.81% (step 2) then drops to 0% (step 4) | exp027: increase env_groups (4→8), lower LR (1e-6→5e-7), lower KL, add entropy bonus | gamma^(T-h) decay makes long-horizon credit impossible; gamma^45≈10% signal strength | Model learned locally valid actions (action_is_valid ~72%) but lost task completion; exp029 (episode-level) reached 28.125% stable |\n| exp027 | Same collapse pattern: peak 35.94% (step 1) then decay to 10.16% (step 2-3), Ray OOM crash | Recipe gap analysis → concluded mini-batch/LR/steps mismatch | Still step-independent (h=5); larger rollouts delayed but did not prevent collapse | D045 recipe gap analysis was wrong: the \"62pp gap\" was not about parameter tuning but about fundamental credit assignment mode |\n\n## Diagnostic Timeline\n\n1. **exp013f** (early): Observed reward gaming. Hypothesized bonus ratio was too large. Proposed ratio reduction and success-gating as fixes.\n2. **exp020b** (mid): Observed policy collapse from SFT baseline. Hypothesized KL/LR misconfiguration. Attempted constraint tuning.\n3. **exp026** (late-mid): Observed catastrophic collapse after initial improvement. Hypothesized insufficient rollout diversity and aggressive updates.\n4. **exp027** (late): Applied conventional recipe fixes (more data, lower LR, entropy bonus). Same collapse pattern persisted, plus infrastructure crash.\n5. **D045 recipe gap analysis**: Systematically compared our hyperparameters against published GRPO recipes. Concluded a \"62pp gap\" from parameter mismatch. This diagnosis was incorrect.\n6. **Insight**: Recognized that all failures shared a common structure: the model could learn locally optimal per-step behavior but could not maintain or improve multi-step coherence. The distinguishing variable was not hyperparameters but the granularity of credit assignment.\n7. **exp029 (episode-level)**: Same SFT checkpoint, same task, episode-level training. Achieved 28.125% stable success, confirming that the credit assignment mode was the true bottleneck.\n\n## Implications\n\n- **Community value**: Multi-turn agent training with GRPO is increasingly popular, but published recipes assume single-turn or short-horizon settings. This unification demonstrates that step-independent GRPO has a structural limitation in long-horizon tasks (avg ~50 steps), not merely a tuning challenge. Practitioners attempting multi-turn agent RL should default to episode-level credit assignment rather than iterating on per-step hyperparameters.\n- **Paper placement**: This table belongs in the Experiments section as an analysis subsection (e.g., \"Analysis: Unifying Failure Modes\"). It serves as evidence that episode-level training is not merely one design choice among equals but a necessary condition for multi-turn success. The diagnostic timeline supports the narrative arc: surface-level fixes failed repeatedly until the structural root cause was identified.\n\n## Counter-evidence: Independent Failure Modes\n\n- **exp021 (data quality)**: Failed due to insufficient evaluation episodes (4-episode eval showed 25% but 16-episode eval showed 6.25%). This is a measurement/data quality issue unrelated to step-independent credit assignment.\n- **exp028_prereq (zero-shot diagnostic)**: A diagnostic experiment testing base model capability without RL training. Not a training failure and thus outside the scope of this analysis.\n- **Scope of the claim**: Step-independent credit assignment is the dominant failure mode for GRPO in multi-turn ALFWorld (4/4 training failures), but it is not a universal explanation for all negative results. Infrastructure issues (Ray OOM), evaluation methodology (insufficient episodes), and data quality remain independent failure sources. The unification claim is specific: when GRPO training itself fails to improve task success in long-horizon settings, the credit assignment granularity is the first variable to examine.\nENDOFFILE",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_failure_unification_table_20260517T051130",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-17606",
    "command": "mkdir -p /root/cost-verify-agent-rl/analysis && cat > /root/cost-verify-agent-rl/analysis/failure_unification_table.md << 'ENDOFFILE'\n# Failure Mode Unification: Step-Independent Credit Assignment as Root Cause\n\n## Summary\n\nAll four negative GRPO experiments (exp013f, exp020b, exp026, exp027) exhibit distinct surface symptoms (reward gaming, policy collapse, catastrophic forgetting) yet share a single root cause: step-independent optimization fundamentally cannot assign credit across multi-turn trajectories. The attempted fixes (bonus ratio tuning, KL constraints, LR reduction, entropy bonuses) addressed symptoms without resolving the structural inability to propagate task-level signal through sequential decisions. Episode-level training (exp029) with the same SFT checkpoint achieved 28.125% stable success, confirming the diagnosis.\n\n## Unification Table\n\n| Experiment | Surface Symptom | Attempted Fix | Actual Root Cause | Key Evidence |\n|------------|----------------|---------------|-------------------|--------------|\n| exp013f | Reward gaming: action_is_valid 60%→97.5%, task success 0% | Reduce bonus ratio (1:67→1:1000), success-gated reward | Step-independent optimization maximizes per-step bonus without requiring task completion | Cumulative bonus (29×0.15=4.5) dominated sparse success reward (10.0); episode-level constrains bonus optimization to full trajectories |\n| exp020b | Policy collapse: success 20%→4.69%, entropy collapse 61%, pass@16 75%→25% | Increase KL constraint, fix response_mask, adjust LR | Per-step GRPO destroys inter-step correlations learned by SFT | Entropy 0.107→0.042; model collapsed to \"safe\" per-step actions, losing sequential planning ability |\n| exp026 | Catastrophic collapse: train success peaks 32.81% (step 2) then drops to 0% (step 4) | exp027: increase env_groups (4→8), lower LR (1e-6→5e-7), lower KL, add entropy bonus | gamma^(T-h) decay makes long-horizon credit impossible; gamma^45≈10% signal strength | Model learned locally valid actions (action_is_valid ~72%) but lost task completion; exp029 (episode-level) reached 28.125% stable |\n| exp027 | Same collapse pattern: peak 35.94% (step 1) then decay to 10.16% (step 2-3), Ray OOM crash | Recipe gap analysis → concluded mini-batch/LR/steps mismatch | Still step-independent (h=5); larger rollouts delayed but did not prevent collapse | D045 recipe gap analysis was wrong: the \"62pp gap\" was not about parameter tuning but about fundamental credit assignment mode |\n\n## Diagnostic Timeline\n\n1. **exp013f** (early): Observed reward gaming. Hypothesized bonus ratio was too large. Proposed ratio reduction and success-gating as fixes.\n2. **exp020b** (mid): Observed policy collapse from SFT baseline. Hypothesized KL/LR misconfiguration. Attempted constraint tuning.\n3. **exp026** (late-mid): Observed catastrophic collapse after initial improvement. Hypothesized insufficient rollout diversity and aggressive updates.\n4. **exp027** (late): Applied conventional recipe fixes (more data, lower LR, entropy bonus). Same collapse pattern persisted, plus infrastructure crash.\n5. **D045 recipe gap analysis**: Systematically compared our hyperparameters against published GRPO recipes. Concluded a \"62pp gap\" from parameter mismatch. This diagnosis was incorrect.\n6. **Insight**: Recognized that all failures shared a common structure: the model could learn locally optimal per-step behavior but could not maintain or improve multi-step coherence. The distinguishing variable was not hyperparameters but the granularity of credit assignment.\n7. **exp029 (episode-level)**: Same SFT checkpoint, same task, episode-level training. Achieved 28.125% stable success, confirming that the credit assignment mode was the true bottleneck.\n\n## Implications\n\n- **Community value**: Multi-turn agent training with GRPO is increasingly popular, but published recipes assume single-turn or short-horizon settings. This unification demonstrates that step-independent GRPO has a structural limitation in long-horizon tasks (avg ~50 steps), not merely a tuning challenge. Practitioners attempting multi-turn agent RL should default to episode-level credit assignment rather than iterating on per-step hyperparameters.\n- **Paper placement**: This table belongs in the Experiments section as an analysis subsection (e.g., \"Analysis: Unifying Failure Modes\"). It serves as evidence that episode-level training is not merely one design choice among equals but a necessary condition for multi-turn success. The diagnostic timeline supports the narrative arc: surface-level fixes failed repeatedly until the structural root cause was identified.\n\n## Counter-evidence: Independent Failure Modes\n\n- **exp021 (data quality)**: Failed due to insufficient evaluation episodes (4-episode eval showed 25% but 16-episode eval showed 6.25%). This is a measurement/data quality issue unrelated to step-independent credit assignment.\n- **exp028_prereq (zero-shot diagnostic)**: A diagnostic experiment testing base model capability without RL training. Not a training failure and thus outside the scope of this analysis.\n- **Scope of the claim**: Step-independent credit assignment is the dominant failure mode for GRPO in multi-turn ALFWorld (4/4 training failures), but it is not a universal explanation for all negative results. Infrastructure issues (Ray OOM), evaluation methodology (insufficient episodes), and data quality remain independent failure sources. The unification claim is specific: when GRPO training itself fails to improve task success in long-horizon settings, the credit assignment granularity is the first variable to examine.\nENDOFFILE",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T05:12:17.093874+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.28}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_failure_unification_table_20260517T051130",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-17T05:12:17.094137+00:00_

文件已写入 `/root/cost-verify-agent-rl/analysis/failure_unification_table.md`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_failure_unification_table_20260517T051130"
}
```

</details>

---
