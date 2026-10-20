# Research conversation: You are Reviewer 2 (R2) for a top ML venue review. Your focus areas are **novelty/significance** and **related work/posi

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 52
- **Recorded user turns:** 1
- **Tool calls:** 22
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a6eb88c450ef5806d.jsonl`
- **Structured JSON:** [`6b688ebb4e1cd29b8831.json`](../../sessions/6b/6b688ebb4e1cd29b8831.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

52 recorded events

### User

_source line 1 · 2026-05-16T16:11:08.470Z_

You are Reviewer 2 (R2) for a top ML venue review. Your focus areas are **novelty/significance** and **related work/positioning**. Use a 6-point scale (1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Target venue acceptance rate ~25%.

## Paper Summary

Title: "Structured Error Injection is Fundamentally Destabilizing for Embodied Planning: Cross-Architecture Evidence from ALFWorld"

The paper investigates whether taxonomy-guided error injection (successful for tool-use agents like PALADIN's +57pp recovery on ToolBench) transfers to embodied planning. They design TaxEI, a 4-operator error taxonomy for ALFWorld (C4: observation masking, P1: step order swap, C1: context truncation, P2: sub-goal deletion). Key findings across 5 seeds on Qwen3-8B and 3 seeds on LLaMA-3.1-8B:

1. Structured error injection degrades performance by 9.0pp vs vanilla SFT; taxonomy labels provide zero benefit over random injection (both 58.3%).
2. TaxEI creates 4:1 SD ratio vs random injection on LLaMA (8.6pp vs 2.1pp), establishing training instability as intrinsic to structured patterns.
3. Inverted-U dose-response: TaxEI-vs-Random gap peaks at 25% injection (-7.3pp), vanishes at full dose.
4. Recovery ≈ resilience: recovery rates track clean competence with r=0.96 (p<0.001, N=15). Detection rate = 0%.
5. Per-operator analysis shows monotonic local→global gradient (C4 +3.7pp to P2 -11.7pp), though individual tests NS.
6. Data scale ablation: 5× scaling (500→2500 trajectories) doesn't close the gap (-8.9pp vs -9.0pp).
7. Recovery prompting ablation: few-shot recovery prompts yield modest +4.3pp max, detection 0%→12%.

## Related Work in the Paper

The paper covers:
- Error injection for LLM agents: PALADIN (taxonomy injection for tool-use), EEF (learning from failures on WebShop)
- Embodied planning agents: ALFWorld, ReAct, Reflexion
- Training instability and seed sensitivity: McCoy et al. 2020, Mosbach et al. 2021, D'Amour et al. 2022
- Adversarial and curriculum training: Madry et al. 2018, Bengio et al. 2009

The paper has 9 references total.

## Your Task

Evaluate the paper on these dimensions:

1. **Novelty and Significance** (weight: high)
   - Is the research question important and timely?
   - Are the findings genuinely novel or expected?
   - Does "structured error injection hurts embodied planning" provide sufficient intellectual contribution?
   - Is the upgrade from "negative result" to "positive characterization of injection stability properties" convincing?
   - Would the community benefit from this paper?

2. **Related Work Completeness** (weight: high)
   - Are there important missing references? Consider:
     * Other error injection / data augmentation work for agents
     * Other ALFWorld training approaches (AgentTuning, FireAct, etc.)
     * Noise injection in training (dropout as noise, label noise literature)
     * Domain adaptation / distribution shift literature
     * Other embodied agent training work (EMMA, SayCan, Inner Monologue, etc.)
     * Curriculum learning beyond Bengio 2009
     * Robustness training literature
   - Is the positioning relative to PALADIN fair and accurate?
   - Only 9 references is very sparse for a venue paper — is this a concern?

3. **Framing and Claims** (weight: high)
   - Is "fundamentally destabilizing" too strong? (Only tested on ALFWorld)
   - Is the generalization from ALFWorld to "embodied planning" justified?
   - Is the task-structural comparison (Table 10: tool-use vs embodied planning) well-supported or hand-wavy?
   - Are the boundary conditions (discrete, observable, locally recoverable errors) empirically validated or just hypothesized?

4. **Contribution Calibration** (weight: medium)
   - For a top venue with ~25% acceptance, is this paper above the bar?
   - How does it compare to typical negative-result papers that get accepted?
   - Is the scope sufficient (single benchmark: ALFWorld)?

5. **Broader Impact and Future Directions** (weight: low)
   - Does the paper adequately discuss implications?
   - Are suggested boundary conditions actionable for practitioners?

## Output Format

```
### R2 Review: Novelty and Related Work

**Summary**: [2-3 sentence summary]

**Strengths**:
- S1: [strength]
- S2: [strength]
- ...

**Weaknesses**:
- W1: [weakness with detailed explanation]
- W2: [weakness with detailed explanation]
- ...

**Questions for Authors**:
- Q1: [question]
- Q2: [question]
- ...

**Detailed Assessment**:
[Per-dimension assessment]

**Missing Related Work**:
[Specific papers/areas that should be cited and discussed]

**Minor Issues**:
[Presentation, framing issues]

**Overall Score**: X/6
**Confidence**: X/5
**Justification**: [2-3 sentences]
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "c9510963-8cc8-47e6-89fa-87e64c7bc4cb",
  "agentId": "a6eb88c450ef5806d",
  "type": "user",
  "uuid": "b43b1ecb-8fb9-4f96-80e2-ff7cea83dfbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T16:11:08.475Z_

```json
{
  "parentUuid": "b43b1ecb-8fb9-4f96-80e2-ff7cea83dfbc",
  "isSidechain": true,
  "agentId": "a6eb88c450ef5806d",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__submit_dream_review_report"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__submit_dream_review_report"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "1a819820-2f09-43df-8d27-9b465dd2beff",
  "timestamp": "2026-05-16T16:11:08.475Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-16T16:11:11.504Z_



I'll start by reading the paper and related project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a819820-2f09-43df-8d27-9b465dd2beff",
  "isSidechain": true,
  "agentId": "a6eb88c450ef5806d",
  "requestId": "req_011Cb6YJzY6NwLruLa5yacze",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "81d577db-42ac-4fca-b5d2-be3b2d29bef0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EKY1BDhnZ5avK1zyDXGvWr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7136,
      "cache_read_input_tokens": 7332,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7136,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-16T16:11:12.399Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01246mQbJYBcHyfzYC8hckUK`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_get_project_overview",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81d577db-42ac-4fca-b5d2-be3b2d29bef0",
  "isSidechain": true,
  "agentId": "a6eb88c450ef5806d",
  "requestId": "req_011Cb6YJzY6NwLruLa5yacze",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "be355ad0-60f9-4762-9861-b212cf774844",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EKY1BDhnZ5avK1zyDXGvWr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7136,
      "cache_read_input_tokens": 7332,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7136,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-16T16:11:12.401Z_

<details><summary>↩ Tool result · `toolu_01246mQbJYBcHyfzYC8hckUK`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__director_get_project_overview"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be355ad0-60f9-4762-9861-b212cf774844",
  "isSidechain": true,
  "promptId": "c9510963-8cc8-47e6-89fa-87e64c7bc4cb",
  "agentId": "a6eb88c450ef5806d",
  "type": "user",
  "uuid": "deefba53-8002-4714-aafb-9b9ae218d801",
  "sourceToolAssistantUUID": "be355ad0-60f9-4762-9861-b212cf774844",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-16T16:11:16.684Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_012Sek4rtCsrzU7Q4YW8q6p4`</summary>

```json
{
  "project": "tax_error_inject_agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "deefba53-8002-4714-aafb-9b9ae218d801",
  "isSidechain": true,
  "agentId": "a6eb88c450ef5806d",
  "requestId": "req_011Cb6YKHhi74wnQJRjGzgrm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d81c7001-7357-4397-a25e-eb80e42209b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HnNgW1RN5zNkhubYUofXoD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 14468,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1446,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 47,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-16T16:11:17.138Z_

<details><summary>↩ Tool result · `toolu_012Sek4rtCsrzU7Q4YW8q6p4`</summary>

```text
{"result":"# 项目 tax_error_inject_agent 概况\n\n## 实验状态 (192 个)\n\n- **v4-random-sft**: PREPARING (failed) — \n- **v4-taxei-sft**: PREPARING (failed) — \n- **mini-vanilla-sft-v4**: PREPARING (success) — \n- **mini-random-sft-v3**: PREPARING (success) — \n- **mini-taxei-sft-v3**: PREPARING (success) — \n- **mini-vanilla-sft-v3**: PREPARING (success) — \n- **v3-vanilla-eval**: PREPARING (success) — \n- **v4-vanilla-sft**: PREPARING (failed) — \n- **vanilla_sft_aligned_v2**: PREPARING — \n- **vanilla_sft_aligned_v1**: PREPARING — \n- **mini-vanilla-sft**: DONE (negative) — \n- **mini-taxei-sft**: DONE (success) — \n- **vanilla-react-baseline**: DONE (success) — \n- **mini-pipeline-e2e**: PREPARING (failed) — \n- **sft-dryrun-73**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-16\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- llama31-random-s123-injected-evalseed42（准备中）\n- llama31-taxei-s123-injected-evalseed42（准备中）\n- llama31-vanilla-s123-injected-evalseed42（准备中）\n- v4-taxei-fixed-inject25-s123-eval（准备中）\n- v4-taxei-fixed-inject25-s0-eval（准备中）\n- v4-random-fixed-inject10-s0-eval-r2: v4 Random 10% seed=0 eval (retry, OOM fix) — 47 ALFWorld clean tasks. Dedicated GPU.（准备中）\n- v4-taxei-fixed-inject10-s123-eval-r2: v4 TaxEI 10% seed=123 eval (retry, OOM fix) — 47 ALFWorld clean tasks. Dedicated GPU.（准备中）\n- v4-taxei-inject10-seed0（准备中）\n- v4-random-inject10-seed0（准备中）\n- v4-taxei-inject10-seed123（准备中）\n- …另有 38 项\n\n## 近期结论\n- **llama31-random-s123-injected** (success): —\n- **llama31-taxei-s123-injected** (success): —\n- **llama31-taxei-s123-eval** (success): —\n\n## 趋势\n成功 131 / 负向 5 / 失败 7 / 共 144\ndetection_rate: 0.533 ↑（近 3 次 success）\nrecovery_rate: 0.689 ↑（近 3 次 success）\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nautodl-5090: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\n\n## 告警\n- v4-taxei-fixed-inject25: 训练失败 — unknown\n- v4-taxei-fixed-inject10-s123-eval: 训练失败 — unknown\n- v4-random-fixed-inject10-s0-eval: 训练失败 — unknown\n- v4-taxei-fixed-inject10-s1-eval: 训练失败 — unknown\n- v4-taxei-fixed-inject25-s7-eval: 训练失败 — unknown\n- v4-taxei-fixed-inject25-s1-eval-r2: 已被终止 — unknown\n- v4-taxei-fixed-inject50-s1: 训练失败 — unknown\n- v4-random-fixed-inject50-s1: 训练失败 — unknown"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d81c7001-7357-4397-a25e-eb80e42209b8",
  "isSidechain": true,
  "promptId": "c9510963-8cc8-47e6-89fa-87e64c7bc4cb",
  "agentId": "a6eb88c450ef5806d",
  "type": "user",
  "uuid": "0234a47c-25e3-4632-8330-f142b4551c6b",
  "sourceToolAssistantUUID": "d81c7001-7357-4397-a25e-eb80e42209b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-16T16:11:17.419Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_013sAAjgPGgav5AdVKiGRzSX`</summary>

```json
{
  "project": "tax_error_inject_agent",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0234a47c-25e3-4632-8330-f142b4551c6b",
  "isSidechain": true,
  "agentId": "a6eb88c450ef5806d",
  "requestId": "req_011Cb6YKHhi74wnQJRjGzgrm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "357ab7fd-9a2b-4cde-bc59-dfb52263d032",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HnNgW1RN5zNkhubYUofXoD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 14468,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1446,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 47,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-16T16:11:17.432Z_

<details><summary>↩ Tool result · `toolu_013sAAjgPGgav5AdVKiGRzSX`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/report.md\", \"content\": \"# Handover — 2026-05-16\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- llama31-random-s123-injected-evalseed42（准备中）\\n- llama31-taxei-s123-injected-evalseed42（准备中）\\n- llama31-vanilla-s123-injected-evalseed42（准备中）\\n- v4-taxei-fixed-inject25-s123-eval（准备中）\\n- v4-taxei-fixed-inject25-s0-eval（准备中）\\n- v4-random-fixed-inject10-s0-eval-r2: v4 Random 10% seed=0 eval (retry, OOM fix) — 47 ALFWorld clean tasks. Dedicated GPU.（准备中）\\n- v4-taxei-fixed-inject10-s123-eval-r2: v4 TaxEI 10% seed=123 eval (retry, OOM fix) — 47 ALFWorld clean tasks. Dedicated GPU.（准备中）\\n- v4-taxei-inject10-seed0（准备中）\\n- v4-random-inject10-seed0（准备中）\\n- v4-taxei-inject10-seed123（准备中）\\n- …另有 38 项\\n\\n## 近期结论\\n- **llama31-random-s123-injected** (success): —\\n- **llama31-taxei-s123-injected** (success): —\\n- **llama31-taxei-s123-eval** (success): —\\n\\n## 趋势\\n成功 131 / 负向 5 / 失败 7 / 共 144\\ndetection_rate: 0.533 ↑（近 3 次 success）\\nrecovery_rate: 0.689 ↑（近 3 次 success）\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nautodl-5090: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\\n\\n## 告警\\n- v4-taxei-fixed-inject25: 训练失败 — unknown\\n- v4-taxei-fixed-inject10-s123-eval: 训练失败 — unknown\\n- v4-random-fixed-inject10-s0-eval: 训练失败 — unknown\\n- v4-taxei-fixed-inject10-s1-eval: 训练失败 — unknown\\n- v4-taxei-fixed-inject25-s7-eval: 训练失败 — unknown\\n- v4-taxei-fixed-inject25-s1-eval-r2: 已被终止 — unknown\\n- v4-taxei-fixed-inject50-s1: 训练失败 — unknown\\n- v4-random-fixed-inject50-s1: 训练失败 — unknown\\n\", \"total_chars\": 1415, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "357ab7fd-9a2b-4cde-bc59-dfb52263d032",
  "isSidechain": true,
  "promptId": "c9510963-8cc8-47e6-89fa-87e64c7bc4cb",
  "agentId": "a6eb88c450ef5806d",
  "type": "user",
  "uuid": "f5ab361f-cf25-4ef2-9f13-6cd819d4538e",
  "sourceToolAssistantUUID": "357ab7fd-9a2b-4cde-bc59-dfb52263d032",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-16T16:11:20.956Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01XeWg4GxmTVzDUkspvzdHjq`</summary>

```json
{
  "project": "tax_error_inject_agent",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5ab361f-cf25-4ef2-9f13-6cd819d4538e",
  "isSidechain": true,
  "agentId": "a6eb88c450ef5806d",
  "requestId": "req_011Cb6YKfoz47qEm6sg84ZBt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b2515d4c-bcab-4652-ad9b-62dc409178fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011RJChbsbgDxufg1wYvLkrr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2297,
      "cache_read_input_tokens": 15914,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2297,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-16T16:11:20.969Z_

<details><summary>↩ Tool result · `toolu_01XeWg4GxmTVzDUkspvzdHjq`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/paper_framing.md\", \"content\": \"# Paper Framing: When Does Error Injection Help LLM Agents? Boundary Conditions from a Failed Transfer to Embodied Planning\\n\\n## Target Venue\\n**Primary**: EMNLP 2026 Findings (Budapest, Oct 22–29) — 8-page long paper. Negative-result contributions accepted per CFP.\\n**Secondary**: ACL 2026 Findings if timeline permits.\\n\\n## Core Question\\nUnder what task-structural conditions does taxonomy-guided error injection improve vs. degrade LLM agent performance?\\n\\n## Thesis Statement\\nTaxonomy-guided error injection — a core component of PALADIN's +57pp Recovery Rate gain on ToolBench (though entangled with inference-time retrieval augmentation) — destabilizes embodied planning agent training without improving performance on ALFWorld. TaxEI and Random injection produce **identical** mean performance (58.3% vs Vanilla 67.3%, 5 seeds each), proving taxonomy labels provide zero benefit. Complete 5-seed dose-response reveals **no safe injection dose**: harm begins at 10% (-6.0pp), peaks at 25% (TaxEI nadir 52.7%), then **saturates** — 50% and Full produce similar harm (~58%) with no marginal worsening. The taxonomy penalty follows an **inverted-U curve**, peaking at 25% (-7.3pp TaxEI-Random gap) and vanishing at higher doses. At every concentration, training outcomes are a **lottery** (19-23pp within-dose range, bimodal seed distributions). Cross-model validation on LLaMA-3.1-8B-Instruct reveals that **structured error injection (TaxEI) causes training instability across model architectures** — TaxEI recovery SD=8.6pp vs Random SD=2.1pp (3-seed), with 1/3 seeds triggering Qwen-like catastrophic degradation (59.6% vs baseline 73.1%). Random injection remains stable and even mildly beneficial (mean 76.6% > Vanilla 73.1%). This confirms the harm is not model-specific but a property of structured error patterns themselves: taxonomy-guided injection creates conflicting learning signals that destabilize training across architectures, while unstructured noise is benign or helpful.\\n\\n## Story Arc\\n\\n### 1. Motivation: Why error injection should work\\nError injection is a principled data augmentation strategy: expose the model to failure modes during training so it learns to avoid or recover from them. PALADIN (arXiv 2509.25238) demonstrated this for tool-use agents, using a ToolScan taxonomy of 7 failure types to generate 50K+ recovery-annotated trajectories plus inference-time retrieval of 55+ exemplars, boosting Recovery Rate from 32.76% to 89.68% on ToolBench (note: removing retrieval reduces the gain by ~30pp, so the SFT contribution alone is ~+27pp). A natural question: does the error-injection training component transfer to embodied planning, where agents execute multi-step plans in physical environments?\\n\\n### 2. Method: TaxEI — Taxonomy-guided Error Injection for Embodied Planning\\nWe designed a 4-operator error taxonomy for ALFWorld embodied planning:\\n- **P1** (step_order_swap): permute action ordering\\n- **P2** (sub_goal_deletion): remove sub-goals\\n- **C1** (context_truncation): truncate environmental context\\n- **C4** (observation_masking): mask observation feedback\\n\\nWe injected errors into 760 trajectories (from 501 GPT-5.2-generated successful trajectories), producing 4,671 injected variants. Three SFT conditions trained on Qwen3-8B: Vanilla (clean only, 4,358 samples), TaxEI (clean + taxonomy-tagged injections, 9,029 samples), Random (clean + unlabeled injections, 9,029 samples). TaxEI and Random differ only in whether the error tag contains the taxonomy label or a generic marker.\\n\\n### 3. Finding: Injection harms equally regardless of taxonomy; introduces catastrophic seed vulnerability\\n**Clean task performance (all 5-seed complete)**:\\n- Vanilla SFT: 67.3% ± 4.7pp (seeds 42/0/123/1/7) — stable, no catastrophic seeds\\n- TaxEI SFT: 58.3% ± 6.5pp (seeds 42/0/123/1/7) — **-9.0pp vs Vanilla, p=0.039 uncorrected, NS Bonferroni (p>0.017), Cohen's d=1.58**\\n- Random SFT: 58.3% ± 8.7pp (seeds 42/0/123/1/7) — **-9.0pp vs Vanilla, p=0.089 uncorrected, NS, Cohen's d=1.28**\\n\\n**CENTRAL FINDING**: TaxEI and Random produce IDENTICAL mean performance (58.3% = 137/235 tasks). Taxonomy labels provide zero benefit over random injection at the mean level. This directly refutes the hypothesis that structured error labeling improves training signal.\\n\\n**Catastrophic seed vulnerability**: Both injection methods produce exactly one ~47% outlier (TaxEI seed0=46.8%, Random seed1=46.8%). Vanilla never drops below 61.7%. Injection introduces a 1-in-5 risk of catastrophic training failure absent in clean training.\\n\\n**Variance gradient**: Vanilla SD (4.7pp) < TaxEI SD (6.5pp) < Random SD (8.7pp). Injection amplifies variance; taxonomy labels may mildly stabilize (TaxEI SD < Random SD), but both are worse than Vanilla. This reverses the 3-seed pattern (where TaxEI had highest SD). Formal variance tests needed (Levene's, n=5).\\n\\n**Dose-response ablation (fixed-size 4,358 total)** (D034+D035+D038: 全部 5 个剂量完整 5-seed):\\n| Dose | TaxEI Mean±SD (n) | Random Mean±SD (n) | Vanilla ref | TaxEI-Random Δ |\\n|------|-------------------|-------------------|-------------|----------------|\\n| 0% (vanilla) | — | — | 67.3±4.7 (5) | — |\\n| 10% | 61.3±8.2 (5) | 63.8±5.4 (5) | | -2.5pp |\\n| 25% | 52.7±7.6 (5) | 60.0±8.0 (5) | | **-7.3pp** |\\n| 50% | 57.4±9.5 (5) | 58.3±11.7 (5) | | -0.9pp |\\n| Full | 58.3±6.5 (5) | 58.3±8.7 (5) | | 0pp |\\n\\nPer-seed data:\\n- TaxEI 10%: 61.7/70.2/55.3/51.1/68.1. Random 10%: 68.1/66.0/55.3/68.1/61.7.\\n- TaxEI 25%: 48.9/46.8/46.8/63.8/57.4. Random 25%: 55.3/61.7/51.1/72.3/59.6.\\n- TaxEI 50%: 51.1/70.2/46.8/63.8/55.3. Random 50%: 57.4/46.8/70.2/70.2/46.8.\\n\\n**Unified dose-response narrative** (D035+D038, complete 5-seed all doses):\\n1. **Non-monotonic harm with 25% nadir + saturation**: Injection at ALL doses reduces mean and increases variance. Harm peaks at 25% (TaxEI nadir 52.7%), then partially rebounds: 50% (57.4%) ≈ Full (58.3%). Doubling injection from 50%→Full has zero marginal effect — ~50% is the saturation point beyond which additional errors no longer worsen outcomes.\\n2. **Inverted-U taxonomy penalty**: TaxEI trails Random at every dose, but the gap peaks at 25% (7.3pp), diminishes at 50% (0.9pp, d=-0.08 negligible), and vanishes at Full (0pp). At 10% the gap is 2.5pp. Taxonomy labels actively harm at intermediate doses where clean/injected balance may maximize conflicting learning signals.\\n3. **Universal training lottery**: All doses produce extreme seed variance (19-23pp within-dose range). Random 50% shows **bimodal** distribution: {46.8, 46.8, 57.4, 70.2, 70.2} — two distinct failure/success modes, not normal scatter. Report median+IQR alongside mean±SD for robustness.\\n4. **Practical implication**: No injection dose is \\\"safe.\\\" Even 10% produces measurable harm (-6.0pp TaxEI). Outcomes are unpredictable at every concentration level. The training lottery, not dosage, dominates performance variation.\\n\\n**Variance pattern** (exploratory, not claimable): SD peaks at 50% (TaxEI 9.5, Random 11.7) then **declines** at Full (6.5, 8.7). This is unexpected — Full dose actually reduces variance vs 50%. Possible explanation: at 50%, the model faces maximum ambiguity between clean and error patterns; at Full, the injection signal dominates and the model consistently adapts (poorly). Levene's test NS at n=5. Do not claim variance patterns without significance tests.\\n\\n**Training lottery at all doses**: Extreme outliers in every condition — TaxEI 10% s0=70.2% vs s1=51.1% (19pp range), Random 25% s1=72.3% vs s123=51.1% (21pp range), Random 50% bimodal (23pp range). Single-seed evaluations are fundamentally unreliable at any dose.\\n\\n**Taxonomy label penalty** (task-type-specific): TaxEI trails Random in aggregate. Per-task 3-seed analysis: taxonomy injection specifically harms **multi-step coordination tasks** — pick_cool_then_place (TaxEI 38.1% vs Random 57.1%, -19.0pp) and pick_two_obj_and_place (42.9% vs 57.1%, -14.3pp) — while leaving simple tasks largely unaffected (≤4.2pp gap for other 4 task types).\\n\\n**Recovery under injected errors (seed=42, 47 tasks, round-robin P1/P2/C1/C4)**:\\n- Vanilla: 61.7% | TaxEI: 59.6% | Random: 63.8%\\n\\n**Recovery ≈ Resilience (D041)**: Recovery eval rates match normal eval rates for all conditions (V: 61.7%=61.7%, T: 59.6%≈61.7%, R: 63.8%≈66.0%). Models succeed at the same base rate regardless of eval-time error injection — they passively ignore perturbations rather than actively recovering. This is **resilience** (noise tolerance from task competence), not **recovery** (error detection + correction). No training regime instills genuine error awareness.\\n\\n**Detection Rate**: 0% for all methods.\\n\\n**Taxonomy labels show no significant benefit**: TaxEI (56.7%) < Random (63.1%) < Vanilla (65.3%). TaxEI vs Random: paired t p≈0.034 (df=2, directionally consistent but low power).\\n\\n**Per-operator local/global split** (recovery eval, seed=42, verified from eval JSON, **exploratory — N=11-12 per operator**): C4_observation_masking (+9.1pp, 6→7/11), P1_step_order_swap (0.0pp, 7→7/12), C1_context_truncation (−8.3pp, 9→8/12), P2_sub_goal_deletion (−8.3pp, 7→6/12). NOT a smooth monotonic gradient — instead a binary split: the most local/observable operator (C4) shows TaxEI advantage; global/cascading operators (C1, P2) show equal disadvantage; P1 is neutral. **Critical caveat**: each delta is driven by ±1 task success/failure at N=11-12 — well within random noise. Fisher exact tests would be NS for all operators. This must be presented as exploratory/hypothesis-generating, not confirmatory. The directional pattern (local positive, global negative) is suggestive but the specific magnitudes (9.1pp, 8.3pp) carry false precision.\\n\\n**Variance tests**: Observed SD gradient: Vanilla 3.3pp < Random 7.0pp < TaxEI 8.6pp. F-test p=0.252 (NS, underpowered at df=2,2), but Levene's test p=0.085 (NS), Brown-Forsythe p=0.842 (NS), bootstrap P(SD_TaxEI > SD_Vanilla) = 0.688. All formal tests NS at n=3 — the variance gradient is a directional observation, not a statistically confirmed effect. Report as \\\"observed pattern, suggestive but underpowered.\\\"\\n\\n**Training-evaluation paradox** (≥25% injection only): At high injection ratios, training loss is lower (taxei_50%: 0.260, random_50%: 0.260 vs vanilla: 0.294) but eval performance is worse (51.1-57.4% vs 61.7%). However, at 10% injection, training loss is actually *higher* (0.308) than vanilla — the paradox only emerges above the dose-response threshold. This is consistent with the threshold effect: low injection doesn't change the training distribution enough to lower loss, while high injection causes the model to memorize error patterns. Literature support: Arpit et al. (2017) memorization dynamics, Zhou et al. (2023 LIMA) superficial alignment hypothesis.\\n\\n### 4. Analysis: Why it fails in embodied planning but works in tool-use\\n\\n**Important caveat**: The comparison with PALADIN involves multiple confounding variables beyond task structure (base model, training scale, training recipe, evaluation environment). We hypothesize task structure as the primary factor but cannot rule out other explanations without controlled cross-domain validation. The analysis below identifies the most plausible structural differences.\\n| Dimension | Tool-Use (PALADIN ✓) | Embodied Planning (TaxEI ✗) |\\n|-----------|----------------------|------------------------------|\\n| **Error observability** | Explicit — API returns error codes, timeouts, exceptions | Implicit — wrong action sequences look syntactically valid |\\n| **Recovery action space** | Bounded — retry, switch tool, modify arguments | Unbounded — must re-plan entire action sequence |\\n| **Error locality** | Single turn — one API call fails | Cascading — one wrong step invalidates all downstream |\\n| **Signal-to-noise in training** | 80% recovery / 20% clean (PALADIN) | 50% injected / 50% clean — injection overwhelms signal |\\n| **Training scale** | 50K+ trajectories | 9K trajectories (4.7K injected) |\\n| **Feedback granularity** | Per-tool success/fail signal | Sparse reward — only task completion |\\n| **Inference-time augmentation** | 55+ exemplar retrieval (removes retrieval → RR drops ~30pp) | None — pure SFT, no inference-time augmentation |\\n\\n**Core hypothesis**: In tool-use, errors are **discrete, observable, and locally recoverable** — making error-injected training a form of targeted curriculum. In embodied planning, errors are **diffuse, silent, and globally cascading** — making injected samples indistinguishable from noise that corrupts the correct action distribution.\\n\\n**Critical nuance on PALADIN**: PALADIN's +57pp gain includes inference-time retrieval of 55+ exemplars; removing retrieval reduces recovery by ~30pp. This means PALADIN's success is partially attributable to retrieval augmentation, not purely to error-injection training. Our comparison therefore tests error injection in its most isolated form (pure SFT, no retrieval), which may be a stricter — and more informative — test of whether the training signal itself transfers.\\n\\n### 4b. Cross-Model Validation: TaxEI instability is not model-specific (LLaMA-3.1-8B-Instruct, 3-seed)\\n\\nTo test whether the TaxEI failure is Qwen-specific or a general property of structured error injection in embodied planning, we replicate the core experiment on LLaMA-3.1-8B-Instruct (3 seeds: 42/0/123). Training setup identical: Vanilla 4,358 samples (1,635 steps), TaxEI/Random 9,029 samples (3,387 steps).\\n\\n**LLaMA Recovery Rate (injected eval, 47 tasks)**:\\n| Condition | s0 (eval=42) | s42 (eval=42) | s123 (eval=123) | Mean±SD |\\n|-----------|:------------:|:-------------:|:---------------:|:-------:|\\n| Vanilla | 74.5% | 74.5% | 70.2% | 73.1±2.5% |\\n| TaxEI | 74.5% | 74.5% | **59.6%** | 69.5±8.6% |\\n| Random | 74.5% | 76.6% | **78.7%** | 76.6±2.1% |\\n\\n**LLaMA Clean Success Rate**:\\n| Condition | s0 | s42 | s123 | Mean±SD |\\n|-----------|:--:|:---:|:----:|:-------:|\\n| Vanilla | 72.3% | 72.3% | 72.3% | 72.3±0.0% |\\n| TaxEI | 76.6% | 76.6% | **61.7%** | 71.6±8.6% |\\n| Random | 74.5% | 76.6% | 76.6% | 75.9±1.2% |\\n\\n**Key findings**:\\n1. **TaxEI training instability is cross-model**: 1/3 seeds (s123) triggers catastrophic degradation on LLaMA (-13.5pp recovery vs vanilla-s123, -10.6pp clean). Pattern mirrors Qwen's consistent degradation but with higher variance (2/3 seeds appear neutral).\\n2. **Random injection is cross-model stable**: SD=2.1% (recovery), no catastrophic seeds, mean slightly above Vanilla (+3.5pp). This is the opposite of Qwen where Random also degraded.\\n3. **TaxEI vs Random divergence**: On LLaMA, TaxEI mean (69.5%) < Random mean (76.6%), gap = -7.1pp. The variance difference is stark: TaxEI SD=8.6% vs Random SD=2.1%. Structured error patterns create training instability that unstructured noise does not.\\n4. **Model-dependent severity, model-independent direction**: Qwen shows consistent TaxEI harm (-9pp, low variance); LLaMA shows intermittent TaxEI harm (mean -3.6pp, high variance with catastrophic 1/3 seed). The *direction* (TaxEI ≤ Random ≤ Vanilla for stability) holds across models; the *severity* varies.\\n\\n**Implication for paper story**: The finding upgrades from \\\"negative result on one model\\\" to \\\"structured error injection is fundamentally destabilizing for embodied planning across architectures.\\\" The taxonomy's structured perturbations create systematic biases that some training seed/model combinations amplify into catastrophic failure, while random noise averages out harmlessly.\\n\\n**Eval seed caveat**: s0/s42 use eval seed=42; s123 uses eval seed=123. Cross-seed aggregation (mean±SD) has a minor eval-seed confound (~2pp from eval randomness). Within each eval-seed group, horizontal (condition) comparisons are fully fair. The critical finding (taxei-s123 collapse) is a within-group horizontal comparison.\\n\\n### 5. Contribution: What this negative result gives the community\\n1. **Empirical boundary condition**: First cross-domain transfer test of taxonomy-guided error injection — and first reported failure. Contrasts with PALADIN's tool-use success and EEF's alternative approach of extracting positive signal from failures.\\n2. **Recovery-pairing disentanglement** (long paper NEW): By testing recovery-paired injection on ALFWorld, we isolate whether the negative result stems from missing recovery pairing or from fundamental task-structure differences. This is the first controlled test of recovery-paired vs unpaired error injection in embodied planning.\\n3. **Recovery vs resilience distinction** (long paper NEW): Recovery eval rates match normal eval rates — models passively ignore eval-time errors (resilience) rather than actively recovering (recovery). Combined with 0% detection rate, this shows error injection creates no form of error awareness in embodied planning.\\n4. **Training variance warning**: Error injection increases cross-seed variance 2.6× (SD 8.6pp vs 3.3pp, 5-seed confirmed). Single-seed evaluations of error injection methods are fundamentally unreliable.\\n7. **Cross-model instability** (long paper NEW): TaxEI structured injection destabilizes training on both Qwen3-8B (consistent -9pp) and LLaMA-3.1-8B-Instruct (intermittent, 1/3 catastrophic seed), while Random injection remains stable across both models. This separates the harm attribution: it is structured error patterns — not model weakness — that cause instability.\\n5. **No-safe-threshold dose-response + training lottery**: Complete 5-seed dose-response ablation (fixed data size, all 5 doses × 5 seeds) shows harm at every tested dose: 10% (-6.0pp TaxEI), 25% (nadir, -14.6pp TaxEI), 50% (-9.9pp TaxEI), Full (-9.0pp). Non-monotonic: harm peaks at 25%, partial rebound at higher doses. Taxonomy penalty follows inverted-U curve: 10% (-2.5pp) → 25% (-7.3pp peak) → 50% (-0.9pp) → Full (0pp). No injection dose is \\\"safe.\\\" Training lottery (19-23pp within-dose range) operates at all concentration levels.\\n6. **Failure mode taxonomy** (long paper NEW): Qualitative failure analysis categorizes how error injection changes model behavior — noise injection (incoherent plans) vs wrong-learning (systematic biases).\\n\\n## Core Claims (each backed by experimental evidence)\\n\\n- **Claim 1**: Error injection (both taxonomy-guided and random) degrades embodied planning performance with large effect size but marginal statistical significance.\\n  → Support: **5-seed data**: TaxEI 58.3%±6.5pp and Random 58.3%±8.7pp vs Vanilla 67.3%±4.7pp. Both injection methods show -9.0pp gap. Welch t: Vanilla vs TaxEI p≈0.039 (uncorrected), Vanilla vs Random p≈0.089. Bonferroni corrected (3 comparisons, α=0.017): all NS. Cohen's d: 1.58 (TaxEI) and 1.28 (Random) — large effects. Underpowered at n=5; the ~9pp degradation may be a real effect requiring larger N to confirm.\\n\\n- **Claim 2**: Taxonomy labels provide zero benefit over random injection — structured error labeling does not improve training signal.\\n  → Support: **TaxEI = Random = 58.3% = 137/235 tasks (5-seed, identical)**. Welch t: t=0.000, p=1.000. This is the paper's strongest finding: the careful design of a 4-operator error taxonomy with per-error-type labels achieves exactly nothing compared to unlabeled random injection. The taxonomy's structured perturbations are indistinguishable from noise at the mean level. Variance differs: TaxEI SD (6.5pp) < Random SD (8.7pp), suggesting taxonomy may mildly stabilize, but both are worse than Vanilla (4.7pp).\\n\\n- **Claim 3**: Error injection causes **generalization instability** with catastrophic seed vulnerability — training converges stably but evaluation produces unpredictable outcomes including catastrophic failures.\\n  → Support: **5-seed complete**: Training loss is extremely stable across seeds (SD=0.0007), yet eval SD: Vanilla 4.7pp < TaxEI 6.5pp < Random 8.7pp. Both injection methods produce exactly one catastrophic outlier (~47%): TaxEI seed0=46.8%, Random seed1=46.8%. Vanilla never drops below 61.7%. **Memorization-generalization dissociation** (D029/D033): Forward pass v2 (trajectory-level) confirms injected samples have lower loss than clean (all conditions), but eval is worse. Random memorizes 2.1× deeper than TaxEI (gap -0.078 vs -0.037) yet achieves identical eval — deeper memorization does not linearly predict eval harm. Dose-response loss gaps are non-monotonic (25% > 50%), not the monotonic pattern in v1 (which had a classification bug). D026 behavioral evidence (partial update: 3-seed V/T, 1-seed R, NOT balanced — full 5-seed trajectory collection pending): TaxEI produces ~2.2× more loop_repetition failures than Vanilla. Ratio stable across data subsets but absolute rates pending balanced data. **Observed pattern** (correlation, not established causation): memorization of error patterns + loop fixation at eval time + generalization collapse. Per-operator loss ranking is unstable across conditions, precluding strong per-operator causal claims. 1-in-5 catastrophic seed risk is absent from clean training.\\n\\n- **Claim 4**: Injection-trained models do not improve error recovery — observed \\\"recovery\\\" is passive resilience (ignoring errors), not active recovery.\\n  → Support: Recovery rate TaxEI 59.6% vs Vanilla 61.7% (seed=42, 47 tasks). Head-to-head: TaxEI gained 4, lost 5, net -1. Per-operator: TaxEI advantage only on C4_observation_masking (+9.1pp), disadvantage on C1 (-8.3pp) and P2 (-8.3pp). **D041 key insight**: Recovery eval rates match normal eval rates across all conditions (Vanilla 61.7%=61.7%, TaxEI 59.6%≈61.7%, Random 63.8%≈66.0%). Models succeed at the same rate whether or not errors are injected at eval time — they passively ignore perturbations rather than actively detecting and recovering from them. This reframes \\\"no recovery improvement\\\" as \\\"no recovery mechanism at all\\\": the models are **resilient** (robust to noise) rather than **recovery-capable** (able to detect and correct errors). The distinction matters because resilience is a byproduct of task completion ability, while recovery requires explicit error awareness that none of the training regimes instill.\\n\\n- **Claim 5**: Detection training via error injection is completely ineffective — models show zero error awareness.\\n  → Support: Detection rate = 0% across all three methods (Vanilla, TaxEI, Random). Combined with D041's recovery≈resilience finding: models neither detect errors explicitly (0% detection) nor respond to them implicitly (recovery rate = normal eval rate). Error injection during training fails to create any form of error awareness in the embodied planning domain.\\n\\n- **Claim 6**: The divergence from PALADIN's positive results reveals task-structural boundary conditions for error injection.\\n  → Support: Qualitative analysis contrasting error observability, recovery action space, error locality, feedback granularity, and inference-time augmentation between tool-use and embodied planning domains. Note: PALADIN's +57pp includes retrieval augmentation (~30pp contribution), making our pure-SFT comparison a stricter isolation of the training signal's value. Additionally, EEF (arXiv 2504.13145) succeeds on WebShop by **extracting good signal from failures** rather than injecting bad signal — suggesting the injection direction itself may be flawed for planning domains.\\n\\n- **Claim 7** (long paper NEW): Recovery-paired injection actively harms performance, definitively ruling out recovery pairing as PALADIN's missing ingredient.\\n  → Support: **TaxEI-RP 4-seed mean 47.9% ± 7.8pp** (s42=38.3%, s0=46.8%, s1=48.9%, s123=57.4%) vs TaxEI 58.3% vs Vanilla 67.3%. Recovery-paired training (14,437 samples = TaxEI 9,029 + recovery continuations 5,408) performs **10pp worse than unpaired TaxEI** and **19pp worse than Vanilla**. Adding recovery demonstrations does not teach active recovery — it adds noise that further corrupts the action distribution. Detection rate remains 0%. This definitively answers the PALADIN recovery-pairing confound: the failure is not due to missing recovery pairs, but to fundamental task-structural incompatibility. (D043)\\n\\n- **Claim 8** ~~(long paper NEW)~~: **CANCELLED (D040)**. WebShop replication infeasible — P1_StepOrderSwap incompatible with linear action space (search+click), taxonomy 4→3 makes cross-environment comparison inequivalent. Downgraded to Discussion section analysis of ALFWorld vs WebShop structural differences and why cross-environment replication is non-trivial.\\n\\n- **Claim 9** (long paper NEW): Structured error injection (TaxEI) causes **cross-model training instability**, while random injection remains stable — the harm is a property of structured error patterns, not model-specific.\\n  → Support: **LLaMA-3.1-8B-Instruct 3-seed replication**. TaxEI recovery mean 69.5%±8.6pp vs Random 76.6%±2.1pp vs Vanilla 73.1%±2.5pp. TaxEI variance 4× higher than Random (SD 8.6 vs 2.1). 1/3 seeds (s123) shows catastrophic TaxEI collapse: recovery 59.6% (vs vanilla 70.2%, Δ=-10.6pp; vs random 78.7%, Δ=-19.1pp). Other 2 seeds show TaxEI=Vanilla=74.5%. Random is consistently stable or mildly beneficial across all seeds. **Cross-model pattern**: Qwen shows consistent TaxEI harm (mean -9pp, moderate variance); LLaMA shows intermittent TaxEI harm (mean -3.6pp, extreme variance with 1/3 catastrophic). Direction (TaxEI ≤ Random for stability) holds across both models. This upgrades the finding from \\\"Qwen-specific negative result\\\" to \\\"structured injection is fundamentally destabilizing for embodied planning.\\\"\\n\\n## Anticipated Reviewer Concerns\\n\\n1. **\\\"Statistical power is limited.\\\"**\\n   → All three conditions now have **5 seeds**. Welch t: Vanilla vs TaxEI p=0.039 (uncorrected), Bonferroni NS (α=0.017). Cohen's d=1.58 (large). Power at n=5: 45.2%; need n=9 for 80%. We do not claim significance after correction but emphasize the large effect size (-9.0pp) and report all individual seed results. Bootstrap 95% CI: [+3.4, +15.8]pp. Bayes Factor 0.68 (inconclusive). The variance gradient (Vanilla 4.7 < TaxEI 6.5 < Random 8.7) is consistent across seeds.\\n\\n2. **\\\"ALFWorld has only 47 test tasks — too small for reliable conclusions.\\\"**\\n   → Valid concern. We explicitly compute statistical power and report confidence intervals. The 47-task limitation is an ALFWorld constraint shared by all prior work on this benchmark. With 5 seeds × 47 tasks = 235 episodes per condition, our pooled sample gives adequate power for the observed ~9pp effect (d≈1.4). WebShop replication was planned but cancelled (D040: P1 incompatible with linear action space); the structural incompatibility itself supports our task-structure boundary condition argument.\\n\\n3. **\\\"Maybe the taxonomy itself is poorly designed.\\\"**\\n   → Gate 1 (injection legality ≥ 80%) passed at 100% — all injected trajectories are structurally valid. Gate 2 (recovery quality ≥ 75%) passed at 97.5%. The taxonomy is functional; it just doesn't help training.\\n\\n4. **\\\"The training recipe might be suboptimal for injection data.\\\"**\\n   → The same recipe produces strong Vanilla results (67.3% ± 4.7pp vs 42.6% zero-shot baseline, +24.7pp, 5 seeds), confirming the recipe works. The degradation is specific to injection augmentation, not training methodology.\\n\\n5. **\\\"50% injection ratio is too high — you're drowning the signal.\\\"**\\n   → Comprehensively addressed with complete 5-seed fixed-size dose-response ablation at 10%/25%/50%/Full (all 4,358 total samples, all 5 doses × 5 seeds). No safe threshold exists: even 10% injection degrades performance (TaxEI -6.0pp). The harm profile is non-monotonic: monotonic degradation 0%→10%→25% (TaxEI nadir 52.7%), partial rebound 25%→50%→Full driven by training lottery. Taxonomy penalty follows inverted-U curve peaking at 25% (-7.3pp TaxEI-Random gap). The pattern holds for both TaxEI and Random, suggesting it is a general property of error injection.\\n\\n6. **\\\"Why is detection rate 0%? Evaluation might be flawed.\\\"**\\n   → Current eval checks for explicit error flagging in model output. Models may develop implicit error awareness (e.g., output hedging, re-planning) not captured by binary detection metrics. We discuss this limitation and propose alternative detection measures.\\n\\n7. **\\\"Why not compare directly on ToolBench?\\\"**\\n   → Our contribution is precisely the domain contrast. Running PALADIN on ALFWorld or TaxEI on ToolBench would strengthen the paper but requires substantial engineering. We list this as future work.\\n\\n8. **\\\"PALADIN uses error+recovery pairs; TaxEI uses standalone errors. Isn't recovery-pairing the real difference?\\\"** [Dream M+W]\\n   → **Directly tested and refuted** (D043). TaxEI-RP (recovery-paired, 14,437 samples) achieves 47.9% ± 7.8pp — **10pp worse** than unpaired TaxEI (58.3%) and **19pp worse** than Vanilla (67.3%). Recovery pairing not only fails to help, it actively harms. This is the paper's strongest evidence for the task-structure hypothesis: even mimicking PALADIN's recovery-pairing design cannot overcome the fundamental incompatibility of error injection with embodied planning.\\n\\n9. **\\\"Power analysis says n=9 needed but you only ran n=5.\\\"** [Dream W]\\n   → We acknowledge n=5 is underpowered (45.2%) for the observed effect at α=0.017 (Bonferroni). We report this transparently with power curves. The large effect size (d=1.58), consistent direction across all 5 seeds, and dose-response replication across 25 independent training runs provide converging evidence despite per-comparison underpowerment.\\n\\n10. **\\\"Data volume confound: Vanilla has half the training data.\\\"** [Dream W]\\n    → Vanilla uses 4,358 samples; TaxEI/Random use 9,029. We address this via dose-response ablation at fixed 4,358 total samples. At 10% injection, TaxEI still degrades (-6.0pp, 5-seed), confirming harm is from injection content, not volume. The full-scale comparison's volume asymmetry is acknowledged as a limitation.\\n\\n11. **\\\"Only tested on one model — maybe it's a Qwen-specific issue.\\\"**\\n    → Addressed with LLaMA-3.1-8B-Instruct 3-seed replication. TaxEI instability reproduces cross-model (LLaMA SD=8.6pp, 1/3 catastrophic seed). Random injection is stable on both models. The direction (TaxEI harmful/unstable, Random neutral/stable) is consistent across architectures; only severity differs (Qwen: consistent harm; LLaMA: intermittent but catastrophic when triggered). This rules out model-specific explanations and points to structured error patterns as the causal factor.\\n\\n## Key Differentiators vs PALADIN\\n\\nPALADIN (arXiv 2509.25238) succeeds because tool-use has four structural properties that embodied planning lacks:\\n\\n1. **Discrete error signals**: Tool calls return explicit success/failure codes. In ALFWorld, a wrong action (e.g., \\\"go to countertop 2\\\" when the object is on shelf 1) produces a valid-looking observation — the agent receives no signal that it erred.\\n\\n2. **Local recoverability**: A failed API call can be retried or substituted with an alternative tool. In planning, a wrong early step (e.g., heating before picking up) invalidates the entire downstream plan, requiring global re-planning rather than local retry.\\n\\n3. **Bounded action space for recovery**: ToolBench has a finite API catalog — recovery means selecting from known alternatives. ALFWorld's text-based action space is open-ended, making \\\"what to do after an error\\\" fundamentally harder to learn from examples.\\n\\n4. **Scale**: PALADIN trains on 50K+ trajectories with 80% recovery focus. TaxEI has 9K total samples with 50% injection. The lower data volume means less room for the model to separate error patterns from noise.\\n\\n**This contrast IS the paper's core contribution**: error injection is not universally beneficial for LLM agents — it requires discrete, observable, locally recoverable errors to serve as effective training signal rather than noise.\\n\\n## Note on v3→v4 Vanilla Discrepancy\\nv3 vanilla SFT achieved 74.5% (seed=42) while v4 three-seed mean is 65.3%. The 9.2pp gap is partially explained by: (1) v3 used different data volume (4,176 vs 4,358 samples due to format alignment changes); (2) seed variance (v4 seed=42 = 61.7%, seed=0 = 68.1%). Paper should briefly note this in supplement to preempt reviewer confusion about different vanilla numbers across experimental rounds.\\n\\n## Dream Review Findings (dream_20260515T020837)\\n\\n**Scores**: Best 2/5 (artifact: dream fabricated experiments), Median 3/5 (Borderline Accept), Worst 2.5/5 (Borderline Revise)\\n\\n**Confirmed action items (cross-tier consistent)**:\\n1. Related work must expand to 15-20 refs. Add: Reflexion (Shinn 2023), McCoy et al. (2020) seed-dependent generalization, Mosbach et al. (2021) fine-tuning stability, Madry et al. (2018) adversarial training, Bengio et al. (2009) curriculum learning, D'Amour et al. (2022) underspecification, ReAct (Yao 2023).\\n2. PALADIN recovery-pairing confound must be discussed prominently: PALADIN pairs errors WITH recovery demonstrations; TaxEI injects standalone errors without recovery. This is the most parsimonious alternative explanation.\\n3. Formal variance test: F-test p=0.252 (NS) is our strongest stat. Also compute Levene's test for robustness.\\n4. Paper structure for 4-page limit: Intro → Method → Main Results (Table 1 + dose-response) → Qualitative/Error Echo → Per-Operator Gradient → Discussion → Conclusion. Move training dynamics, recovery prompting to appendix.\\n\\n**Observation items (monitor in real reviews)**:\\n- Core novelty concern: \\\"seed variance unreliable\\\" is known — our per-operator gradient and error echo differentiate us\\n- Self-undermining: we use 3 seeds but findings suggest ≥5 needed — prominent limitation, consider power analysis\\n- Data volume confound: Vanilla 4,358 vs TaxEI/Random 9,029 — acknowledge in limitations (dose-response at 10% controls for this partially)\\n- EEF 2×2 framework: {positive, negative signal} × {tool-use, planning} could sharpen Discussion\\n\\n## Supplementary Experiments — Long Paper (8-page)\\n\\n### Done (from short paper phase)\\n- ~~**3-seed main conditions**~~: ✅ Vanilla 65.3%±3.3pp, TaxEI 56.7%±8.6pp, Random 63.1%±7.0pp.\\n- ~~**Dose-response 3-seed (25%/50%)**~~: ✅ Dual regime confirmed. 10% = seed=42 only.\\n- ~~**Recovery eval (seed=42)**~~: ✅ TaxEI 59.6%, Vanilla 61.7%, Random 63.8%. Detection 0%.\\n\\n### Priority 1 (required for 8-page long paper)\\n- ~~**5-seed extension** [Claims 1,3]~~: ✅ Done. Vanilla 67.3±4.7, TaxEI=Random=58.3%. D032.\\n- ~~**Training dynamics** [Claim 3]~~: ✅ Done. Forward pass v2 (trajectory-level). D027/D029/D033.\\n- ~~**Qualitative failure analysis** [Claims 1,6]~~: ✅ Done. TaxEI loop_repetition 2.2×. D026.\\n- ~~**Extended statistics** [Claims 1,3]~~: ✅ Done. Bootstrap CI, power, Bayesian. D030-D032.\\n- ~~**Dose-response 5-seed** [Claim 3]~~: ✅ Done. All 5 doses × 5 seeds complete. 10% (D034), 25% (D035/D036), 50% (D038). Inverted-U taxonomy penalty curve. ~24 GPU-h.\\n- **Recovery-paired injection** [Claim 7]: 🔄 Training in progress (4 seeds × 4 GPU). Datagen complete (711/760), 14,437 samples. ~16 GPU-h.\\n- ~~**WebShop replication** [Claim 8]~~: ❌ CANCELLED (D040). P1 incompatible with linear action space. Downgraded to Discussion.\\n- **Recovery eval multi-seed** [Claims 4,5]: 7/15 complete. Remaining 8/15 after TaxEI-RP. ~15 GPU-h.\\n\\n### Priority 1.5 (cross-model validation)\\n- ~~**LLaMA-3.1-8B cross-model replication** [Claim 9]~~: ✅ Done. 3 seeds × 3 conditions, all training + eval complete. TaxEI instability confirmed cross-model (SD=8.6%, 1/3 catastrophic). Random stable (SD=2.1%). ~36 GPU-h.\\n\\n### Priority 2 (strengthens further)\\n- **Scale ablation** [Claim 6]: 25K-50K trajectories. ~$30-50 API + ~20 GPU-h.\\n\\n### Estimated total: ~120 GPU-hours (~30h wall clock with 4 × 5090)\\n\", \"total_chars\": 35513, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b2515d4c-bcab-4652-ad9b-62dc409178fe",
  "isSidechain": true,
  "promptId": "c9510963-8cc8-47e6-89fa-87e64c7bc4cb",
  "agentId": "a6eb88c450ef5806d",
  "type": "user",
  "uuid": "a62a8230-82cf-4a3c-a234-58343f9f57a1",
  "sourceToolAssistantUUID": "b2515d4c-bcab-4652-ad9b-62dc409178fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-16T16:11:21.866Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01KZdRH9WPa5N3dNRK2X7NH2`</summary>

```json
{
  "project": "tax_error_inject_agent",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a62a8230-82cf-4a3c-a234-58343f9f57a1",
  "isSidechain": true,
  "agentId": "a6eb88c450ef5806d",
  "requestId": "req_011Cb6YKfoz47qEm6sg84ZBt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "20e931f5-8957-4c6a-bf16-bf02a5c6f3d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011RJChbsbgDxufg1wYvLkrr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2297,
      "cache_read_input_tokens": 15914,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2297,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-16T16:11:21.883Z_

<details><summary>↩ Tool result · `toolu_01KZdRH9WPa5N3dNRK2X7NH2`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/literature_map.yaml\", \"content\": \"# Literature Map: Dose-Response / Threshold Effects in Data Augmentation\\n# Updated: 2026-05-15\\n\\nentries:\\n  # === Category: dose-response / threshold ===\\n\\n  - id: rolnick2017robust\\n    title: \\\"Deep Learning is Robust to Massive Label Noise\\\"\\n    authors: \\\"Rolnick, Veit, Belongie, Shavit\\\"\\n    year: 2017\\n    venue: arXiv 1705.10694\\n    category: dose-response\\n    role: background\\n    key_finding: \\\"DNNs maintain >90% accuracy on MNIST even when correct labels are diluted 100:1, as long as correct label remains most likely by a small margin.\\\"\\n    relevance: \\\"Contrasts with our finding: image classification is robust to extreme noise, while embodied planning shows sharp degradation at 25%. Task complexity mediates noise tolerance.\\\"\\n\\n  - id: yuan2024early_stopping\\n    title: \\\"Early Stopping Against Label Noise Without Validation Data\\\"\\n    authors: \\\"Yuan, Feng, Liu\\\"\\n    year: 2024\\n    venue: ICLR 2024\\n    category: dose-response\\n    role: background\\n    key_finding: \\\"Identifies phase transition where DNNs shift from fitting clean to fitting mislabeled examples. Proposes Label Wave to detect this transition during training.\\\"\\n    relevance: \\\"Supports existence of phase transition in learning dynamics. Our 10-25% threshold may correspond to such a transition point in the SFT regime.\\\"\\n\\n  - id: dohmatob2025collapse\\n    title: \\\"Strong Model Collapse\\\"\\n    authors: \\\"Dohmatob, Feng, Subramonian, Kempe\\\"\\n    year: 2025\\n    venue: ICLR 2025\\n    category: threshold\\n    role: background\\n    key_finding: \\\"Even 0.1% synthetic data can cause model collapse in supervised regression. Past interpolation threshold, larger models become more robust (double-descent).\\\"\\n    relevance: \\\"Demonstrates extreme sensitivity to data quality in certain regimes. Our 10-25% threshold is analogous—small quality shifts cause nonlinear degradation.\\\"\\n\\n  - id: beyond_clean_data2024\\n    title: \\\"Beyond Clean Data: Exploring the Effects of Label Noise on Object Detection Performance\\\"\\n    authors: \\\"Freire, de S. Silva, de Andrade, Fernandes\\\"\\n    year: 2024\\n    venue: Knowledge-Based Systems\\n    category: dose-response\\n    role: background\\n    key_finding: \\\"Systematically varies noise levels in training and validation for object detection, mapping convergence limits and degradation thresholds.\\\"\\n    relevance: \\\"Methodologically similar—varies noise proportion to find degradation curves. Shows task-specific threshold behavior.\\\"\\n\\n  # === Category: error-injection / failure augmentation ===\\n\\n  - id: wang2024learning_from_failure\\n    title: \\\"Learning From Failure: Integrating Negative Examples when Fine-tuning Large Language Models as Agents\\\"\\n    authors: \\\"Wang, Li, Han, Zhang, Baldwin\\\"\\n    year: 2024\\n    venue: arXiv 2402.11651\\n    category: error-injection\\n    role: evaluation\\n    key_finding: \\\"Failed trajectories provide valuable signal for LLM agents via contrastive learning. Negative examples improve math, QA, strategic tasks when properly structured.\\\"\\n    relevance: \\\"Directly related—injects negative trajectories into agent SFT. Key difference: they use contrastive framing, not raw mixing. Our work shows raw mixing has narrow safe window.\\\"\\n\\n  - id: song2024eto\\n    title: \\\"Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents\\\"\\n    authors: \\\"Song, Yin, Yue, Huang, Li, Lin\\\"\\n    year: 2024\\n    venue: ACL 2024\\n    category: error-injection\\n    role: evaluation\\n    key_finding: \\\"Iteratively collects failure trajectories, uses DPO-style contrastive learning on success-failure pairs. +8% WebShop, +9.5% ScienceWorld vs SFT.\\\"\\n    relevance: \\\"Uses failure trajectories via preference optimization (DPO), not direct SFT mixing. Avoids our threshold problem by never training directly on failures.\\\"\\n\\n  - id: paladin2025\\n    title: \\\"PALADIN: Self-Correcting Language Model Agents to Cure Tool-Failure Cases\\\"\\n    authors: \\\"Vuddanti, Shah et al.\\\"\\n    year: 2025\\n    venue: arXiv 2509.25238\\n    category: error-injection\\n    role: evaluation\\n    key_finding: \\\"Trains on 50K+ recovery-annotated failure trajectories via LoRA. +57pp recovery rate vs vanilla (32.76%→89.68%), +13.6pp vs CRITIC baseline. Taxonomy of 7 error classes. Includes inference-time retrieval.\\\"\\n    relevance: \\\"Most similar to our approach (taxonomy-guided error injection). Key difference: they pair failures with recovery demos; we inject standalone error trajectories.\\\"\\n\\n  - id: agentHER2025\\n    title: \\\"AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling\\\"\\n    authors: \\\"Ding\\\"\\n    year: 2025\\n    venue: arXiv 2603.21357\\n    category: error-injection\\n    role: evaluation\\n    key_finding: \\\"Converts failed trajectories to valid training data by relabeling—failure for task A becomes success for task B.\\\"\\n    relevance: \\\"Avoids noise problem by redefining failure as success for different goals. Contrasts with our direct injection approach.\\\"\\n\\n  # === Category: data-mixing ===\\n\\n  - id: dong2024composition\\n    title: \\\"How Abilities in Large Language Models are Affected by Supervised Fine-tuning Data Composition\\\"\\n    authors: \\\"Dong, Yuan et al.\\\"\\n    year: 2024\\n    venue: ACL 2024\\n    category: data-mixing\\n    role: background\\n    key_finding: \\\"Data amount per domain matters more than ratio. Low-data mixing enables cross-domain transfer; high-data mixing causes ability conflicts.\\\"\\n    relevance: \\\"Documents ability-conflict at high data amounts—analogous to our threshold. Ratio secondary to amount suggests our threshold may be absolute-count driven.\\\"\\n\\n  - id: ye2025mixing_laws\\n    title: \\\"Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance\\\"\\n    authors: \\\"Ye et al.\\\"\\n    year: 2025\\n    venue: ICLR 2025\\n    category: data-mixing\\n    role: background\\n    key_finding: \\\"Discovers quantitative scaling laws L=f(r) for mixture proportions. Accurately predicts critical proportion avoiding catastrophic forgetting.\\\"\\n    relevance: \\\"Their 'critical proportion for catastrophic forgetting' is conceptually identical to our threshold—both mark a phase transition in mixing.\\\"\\n\\n  - id: li2025mixing_optimization\\n    title: \\\"Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models\\\"\\n    authors: \\\"Li et al.\\\"\\n    year: 2025\\n    venue: ICML 2025\\n    category: data-mixing\\n    role: background\\n    key_finding: \\\"SFT mixing as optimization with scaling-law parameterization. Optimal weights depend on model size and data scale.\\\"\\n    relevance: \\\"Optimal mixing is model-size dependent—our 7B model may have different threshold than larger models. Finding is scale-specific.\\\"\\n\\n  - id: seddik2024synthetic_bound\\n    title: \\\"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\\\"\\n    authors: \\\"Seddik et al.\\\"\\n    year: 2024\\n    venue: arXiv 2404.05090\\n    category: data-mixing\\n    role: background\\n    key_finding: \\\"Theoretical upper bounds on low-quality data proportion before collapse. Real data proportion must remain high.\\\"\\n    relevance: \\\"Theoretical grounding for hard thresholds in quality mixing. Our empirical 10-25% window is consistent with their predictions.\\\"\\n\\n  # === Category: curriculum / quality threshold ===\\n\\n  - id: curriculum_robust2021\\n    title: \\\"Robust Curriculum Learning: from Clean Label Detection to Noisy Label Self-Correction\\\"\\n    authors: \\\"Zhou, Wang, Bilmes\\\"\\n    year: 2021\\n    venue: ICLR 2021\\n    category: curriculum\\n    role: background\\n    key_finding: \\\"Networks learn simple patterns first, then overfit noisy labels. Loss-based curriculum selection is unstable; errors accumulate multiplicatively.\\\"\\n    relevance: \\\"Explains WHY threshold exists: once noisy proportion exceeds implicit curriculum capacity, errors accumulate. Our 25% may exceed model's capacity.\\\"\\n\\n  - id: agentprm2025\\n    title: \\\"Process Reward Models for LLM Agents: Practical Framework and Directions\\\"\\n    authors: \\\"Choudhury\\\"\\n    year: 2025\\n    venue: arXiv 2502.10325\\n    category: curriculum\\n    role: evaluation\\n    key_finding: \\\"Best-of-N with process reward model achieves 91.0% on ALFWorld (N=16, base policy 88.1%). Shows reward-guided search outperforms SFT alone.\\\"\\n    relevance: \\\"ALFWorld SOTA reference. Our 65.3% SFT-only baseline is reasonable given AgentPRM uses test-time search.\\\"\\n\\n  - id: wkm2024alfworld\\n    title: \\\"Agent Planning with World Knowledge Model\\\"\\n    authors: \\\"Qiao, Fang, Zhang, Zhu, Chen et al.\\\"\\n    year: 2024\\n    venue: NeurIPS 2024\\n    category: curriculum\\n    role: evaluation\\n    key_finding: \\\"World knowledge models reduce hallucinatory actions in ALFWorld. SFT on expert trajectories prone to overfitting.\\\"\\n    relevance: \\\"ALFWorld baseline showing SFT quality sensitivity. Hallucination increase from poor training data parallels our error-injection degradation.\\\"\\n\\n  # === Category: training-dynamics / memorization ===\\n\\n  - id: arpit2017memorization\\n    title: \\\"A Closer Look at Memorization in Deep Networks\\\"\\n    authors: \\\"Arpit, Jastrzębski, Ballas, Krueger, Bengio, Kanwal, Maharaj, Fischer, Courville, Bengio, Lacoste-Julien\\\"\\n    year: 2017\\n    venue: ICML 2017\\n    category: training-dynamics\\n    role: background\\n    key_finding: \\\"DNNs first learn clean patterns (early learning phase), then memorize noise. Training loss/accuracy improve on noisy data but generalization degrades. Dataset-independent capacity concepts are insufficient.\\\"\\n    relevance: \\\"Directly explains our '50% injection → lowest train loss but worst eval' paradox. Higher injection = more noisy samples to memorize, better train metrics but worse generalization.\\\"\\n\\n  - id: liu2020early_learning_reg\\n    title: \\\"Early-Learning Regularization Prevents Memorization of Noisy Labels\\\"\\n    authors: \\\"Liu, Niles-Weed, Razavian, Fernandez-Granda\\\"\\n    year: 2020\\n    venue: NeurIPS 2020\\n    category: training-dynamics\\n    role: background\\n    key_finding: \\\"Formalizes early learning phenomenon: models predict true labels for mislabeled examples early in training, then memorize wrong labels. ELR regularization exploits this window.\\\"\\n    relevance: \\\"Our error-injected samples may be correctly handled early in training but memorized later, degrading clean-data generalization. Explains why more epochs could worsen the gap.\\\"\\n\\n  - id: zhou2023lima\\n    title: \\\"LIMA: Less Is More for Alignment\\\"\\n    authors: \\\"Zhou, Liu, Xu, Iyer, Sun, Mao, Ma, Efrat, Yu, Yu, Zhang, Ghosh, Lewis, Zettlemoyer, Levy\\\"\\n    year: 2023\\n    venue: NeurIPS 2023\\n    category: training-dynamics\\n    role: background\\n    key_finding: \\\"Superficial Alignment Hypothesis: LLM knowledge/capability comes from pretraining; SFT only teaches output style/format. Limited SFT data suffices.\\\"\\n    relevance: \\\"Explains why lower SFT loss ≠ better downstream capability. Error injection improves surface-level fitting (lower loss) but doesn't enhance—and may damage—pretrained planning capability.\\\"\\n\\n  - id: luo2023catastrophic_forgetting\\n    title: \\\"An Empirical Study of Catastrophic Forgetting in Large Language Models During Continual Fine-tuning\\\"\\n    authors: \\\"Luo, Yang, Meng, Li, Zhou, Zhang\\\"\\n    year: 2023\\n    venue: arXiv 2308.08747\\n    category: training-dynamics\\n    role: background\\n    key_finding: \\\"SFT is off-policy learning prone to overfit training distribution and forget pretraining knowledge. Forgetting severity increases with divergence between fine-tuning and pretraining distributions.\\\"\\n    relevance: \\\"Error injection increases distributional gap from pretraining data, accelerating catastrophic forgetting. 50% injection → maximal divergence → most forgetting of planning capability.\\\"\\n\\n  - id: longpre2020augmentation\\n    title: \\\"How Effective is Task-Agnostic Data Augmentation for Pretrained Transformers?\\\"\\n    authors: \\\"Longpre, Wang, DuBois\\\"\\n    year: 2020\\n    venue: Findings of EMNLP 2020\\n    category: training-dynamics\\n    role: background\\n    key_finding: \\\"Data augmentation provides minimal benefit for pretrained transformers; pretrained representations already capture augmentation diversity. Augmentation can hurt when it introduces distribution shift.\\\"\\n    relevance: \\\"Pretrained LLMs may already have robust representations; error injection adds noise without new information, explaining why augmentation-style injection fails for embodied planning.\\\"\\n\\n  # === Category: training-instability ===\\n\\n  - id: mccoy2020seeds\\n    title: \\\"BERTs of a feather do not generalize together: Large variability in generalization across models with similar test set performance\\\"\\n    authors: \\\"McCoy, Min, Linzen\\\"\\n    year: 2020\\n    venue: \\\"BlackboxNLP Workshop at EMNLP 2020\\\"\\n    category: training-instability\\n    role: background\\n    key_finding: \\\"Fine-tuning 100 BERT instances on MNLI yields near-identical dev accuracy (83.6-84.8%) but wildly different syntactic generalization (0-66.2% on HANS), demonstrating extreme seed-dependent generalization.\\\"\\n    relevance: \\\"与我们方差梯度发现的关系：error injection 放大了 McCoy 描述的 seed sensitivity\\\"\\n\\n  - id: mosbach2021stability\\n    title: \\\"On the Stability of Fine-tuning BERT: Misconceptions, Explanations, and Strong Baselines\\\"\\n    authors: \\\"Mosbach, Andriushchenko, Klakow\\\"\\n    year: 2021\\n    venue: \\\"ICLR 2021\\\"\\n    category: training-instability\\n    role: background\\n    key_finding: \\\"BERT fine-tuning instability的根因是vanishing gradients导致的优化困难，而非此前假设的catastrophic forgetting或数据集过小。\\\"\\n    relevance: \\\"fine-tuning 不稳定性的基础文献，我们的 TaxEI 方差梯度扩展了这一发现到 error-augmented agent training\\\"\\n\\n  - id: damour2022underspecification\\n    title: \\\"Underspecification Presents Challenges for Credibility in Modern Machine Learning\\\"\\n    authors: \\\"D'Amour, Heller, Moldovan, Adlam, Alipanahi, Beutel, Chen, Deaton, Eisenstein, Hoffman et al.\\\"\\n    year: 2022\\n    venue: \\\"Journal of Machine Learning Research, Vol. 23, No. 226\\\"\\n    category: training-instability\\n    role: background\\n    key_finding: \\\"ML pipeline underspecification导致测试性能相当的模型在部署域行为截然不同，涵盖CV、NLP、医学等多领域实证。\\\"\\n    relevance: \\\"我们的 3 seeds 中 2 个 match vanilla + 1 个 collapse 是 underspecification 的典型表现\\\"\\n\\n  # === Category: alfworld-methods ===\\n\\n  - id: shridhar2021alfworld\\n    title: \\\"ALFWorld: Aligning Text and Embodied Environments for Interactive Learning\\\"\\n    authors: \\\"Shridhar, Yuan, Côté, Bisk, Trischler, Hausknecht\\\"\\n    year: 2021\\n    venue: \\\"ICLR 2021\\\"\\n    arxiv: \\\"2010.03768\\\"\\n    category: alfworld-methods\\n    role: evaluation\\n    key_finding: \\\"Aligns TextWorld text-based environment with ALFRED embodied benchmark, enabling abstract policy learning that transfers to visual grounding.\\\"\\n    relevance: \\\"我们的实验环境；134 tasks across 6 task types benchmark\\\"\\n\\n  - id: yao2023react\\n    title: \\\"ReAct: Synergizing Reasoning and Acting in Language Models\\\"\\n    authors: \\\"Yao, Zhao, Yu, Du, Shafran, Narasimhan, Cao\\\"\\n    year: 2023\\n    venue: \\\"ICLR 2023\\\"\\n    arxiv: \\\"2210.03629\\\"\\n    category: alfworld-methods\\n    role: evaluation\\n    key_finding: \\\"Interleaved reasoning traces and actions enable LLMs to ground decisions, achieving 75% on ALFWorld (single-trial).\\\"\\n    relevance: \\\"我们使用的 prompting paradigm（ReAct format）\\\"\\n\\n  - id: shinn2023reflexion\\n    title: \\\"Reflexion: Language Agents with Verbal Reinforcement Learning\\\"\\n    authors: \\\"Shinn, Cassano, Berman, Gopinath, Narasimhan, Yao\\\"\\n    year: 2023\\n    venue: \\\"NeurIPS 2023\\\"\\n    arxiv: \\\"2303.11366\\\"\\n    category: alfworld-methods\\n    role: evaluation\\n    key_finding: \\\"Verbal self-reflection in episodic memory achieves 97% on ALFWorld (12 trials, 130/134 tasks solved) without weight updates.\\\"\\n    relevance: \\\"Inference-time reflection 成功 where training-time injection 失败——对比 key point\\\"\\n\\n  - id: kim2025coex\\n    title: \\\"CoEx -- Co-evolving World-model and Exploration\\\"\\n    authors: \\\"Kim, Hwang\\\"\\n    year: 2025\\n    venue: \\\"Findings of EMNLP 2025\\\"\\n    arxiv: \\\"2507.22281\\\"\\n    category: alfworld-methods\\n    role: evaluation\\n    key_finding: \\\"Hierarchical state abstraction with dynamically updated neurosymbolic world model achieves 93.28% on ALFWorld.\\\"\\n    relevance: \\\"ALFWorld SOTA 参考；co-evolving world model 对比我们的 static SFT 方法\\\"\\n\\n  # === Category: error-injection (补充) ===\\n\\n  - id: eef2025\\n    title: \\\"Exploring Expert Failures Improves LLM Agent Tuning\\\"\\n    authors: \\\"Lan, Bai, Cheng, Hsieh, Zhou\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2504.13145\\\"\\n    category: error-injection\\n    role: evaluation\\n    key_finding: \\\"从失败 expert trajectories 中提取有益 actions（plans、key actions），用于引导 agent exploration，WebShop SOTA 0.81，SciWorld 81/100。\\\"\\n    relevance: \\\"从失败中提取正向信号（非注入负信号），成功 on WebShop。与我们的直接注入形成对比——方向相反的 failure utilization。\\\"\\n\\n  - id: agentdebug2025\\n    title: \\\"Where LLM Agents Fail and How They can Learn From Failures\\\"\\n    authors: \\\"Zhu, Liu, Li, Tian et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2509.25370\\\"\\n    category: error-injection\\n    role: evaluation\\n    key_finding: \\\"5-dimension AgentErrorTaxonomy（memory, reflection, planning, action, system-level）+ AgentErrorBench 标注数据集 + AgentDebug 纠错框架，跨 ALFWorld/GAIA/WebShop 提升 24% all-correct accuracy。\\\"\\n    relevance: \\\"ALFWorld 的另一个 error taxonomy（5维 vs 我们的 4 operator）。对比点：不同 taxonomy 设计选择。\\\"\\n\\n  # === Category: data-mixing / curriculum (补充) ===\\n\\n  - id: bengio2009curriculum\\n    title: \\\"Curriculum Learning\\\"\\n    authors: \\\"Bengio, Louradour, Collobert, Weston\\\"\\n    year: 2009\\n    venue: \\\"ICML 2009\\\"\\n    category: curriculum\\n    role: background\\n    key_finding: \\\"按难度递增顺序呈现训练样本可加速收敛并改善非凸优化的局部最优质量；curriculum 本质是一种 continuation method。\\\"\\n    relevance: \\\"Curriculum learning 中 difficult example proportion 的 threshold 概念与我们的 dose-response 阈值平行——训练数据中困难/噪声样本超过阈值后性能崩溃\\\"\\n\\n  - id: madry2018adversarial\\n    title: \\\"Towards Deep Learning Models Resistant to Adversarial Attacks\\\"\\n    authors: \\\"Madry, Makelov, Schmidt, Tsipras, Vladu\\\"\\n    year: 2018\\n    venue: \\\"ICLR 2018\\\"\\n    category: data-mixing\\n    role: background\\n    key_finding: \\\"基于 PGD 的 adversarial training 通过 robust optimization 框架显著提升对抗鲁棒性，但以 clean accuracy 下降为代价。\\\"\\n    relevance: \\\"Adversarial training 的 accuracy-robustness tradeoff 是 dose-response 型——增加 adversarial perturbation 强度提升鲁棒性但降低 clean accuracy，与我们的 injection ratio vs clean eval tradeoff 结构相似\\\"\\n\", \"total_chars\": 17888, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "20e931f5-8957-4c6a-bf16-bf02a5c6f3d0",
  "isSidechain": true,
  "promptId": "c9510963-8cc8-47e6-89fa-87e64c7bc4cb",
  "agentId": "a6eb88c450ef5806d",
  "type": "user",
  "uuid": "29bb407c-fcd9-412c-b1ba-a8be8b46f6e7",
  "sourceToolAssistantUUID": "20e931f5-8957-4c6a-bf16-bf02a5c6f3d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-16T16:11:22.303Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01C6eQhtXDWab8H7FrP8HAoS`</summary>

```json
{
  "project": "tax_error_inject_agent",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29bb407c-fcd9-412c-b1ba-a8be8b46f6e7",
  "isSidechain": true,
  "agentId": "a6eb88c450ef5806d",
  "requestId": "req_011Cb6YKfoz47qEm6sg84ZBt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3c39b4c3-d0fe-4b67-ae5f-0c76666b5414",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011RJChbsbgDxufg1wYvLkrr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2297,
      "cache_read_input_tokens": 15914,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2297,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-16T16:11:22.311Z_

<details><summary>↩ Tool result · `toolu_01C6eQhtXDWab8H7FrP8HAoS`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/memory.md\", \"content\": \"# Memory\\n\\n## 关键决策与经验\\n\\n[2026-05-15] 5-seed 主实验 (full dose) 最终结果: TaxEI=Random=58.3%=137/235 (均值完全一致), Vanilla=67.3±4.7%。taxonomy 标签零收益，这是论文的核心 negative result。\\n\\n[2026-05-15] Forward pass v2 (trajectory-level): v1 的 monotonic dose-response gap 是 turn-level aggregation bug 的产物，已作废。v2 发现 Random 2.1× deeper memorization。\\n\\n[2026-05-15] Extended statistics: bootstrap TaxEI-Vanilla significant (CI [+3.4,+15.8]), 但 frequentist marginal (p=0.073), power 仅 45.2%。需 n=9 seeds 达 80% power。\\n\\n[2026-05-15] D033 Forward pass v2 (trajectory-level): v1 monotonic dose-response gap 作废，不能引用 v1 数据。\\n\\n[2026-05-15] Eval 并行上限 2 个: 8B 模型 eval 需 ~18GB，4 并行必 OOM。同一时间 eval ≤ 2。**更新 [2026-05-16]**: RTX 5090 32GB 上实测每个 eval ~16.8GB，可在 4 张卡上各跑一个 eval（每卡独占）。但绝不能两个 eval 共享同一张 GPU。\\n\\n[2026-05-15] 10% Dose-Response 5-seed 完整结果:\\n- TaxEI 10%: s42=61.7%, s0=70.2%, s123=55.3%, s1=51.1%, s7=68.1% → 均值 61.3±8.1%\\n- Random 10%: s42=68.1%, s0=66.0%, s123=55.3%, s1=68.1%, s7=61.7% → 均值 63.8±5.4%\\n- Vanilla baseline: 67.3±4.7%\\n- 所有 pairwise 不显著 (p>0.19)，TaxEI vs Random d=0.27，需 109 seeds 达 80% power\\n\\n[2026-05-16] **25% Dose-Response 5-seed 完整结果 — 出现显著差异！**\\n- TaxEI 25%: s42=48.9%, s0=46.8%, s123=46.8%, s1=63.8%, s7=57.4% → 均值 52.7±7.6%\\n- Random 25%: s42=55.3%, s0=61.7%, s123=51.1%, s1=72.3%, s7=59.6% → 均值 60.0±8.0%\\n- **Vanilla vs TaxEI 25%: p=0.004, d=2.63 (极大效应量, power=0.989)**\\n- **Vanilla vs Random 25%: p=0.039, d=1.36 (power=0.629)**\\n- **TaxEI 25% vs Random 25%: p=0.029, d=-1.49**\\n- TaxEI dose-response 斜率 0.58 pp/% 是 Random 的 2 倍 (0.29)\\n- Page's trend: TaxEI p=0.004, Random p=0.044\\n\\n[2026-05-16] **D036 Framing 决策：维持 negative result framing。** 25% TaxEI vs Random p=0.029 未过 Bonferroni 校正 (α=0.017 for 3 comparisons)，不能 claim 为显著。Dose-dependent taxonomy penalty 作为 secondary finding。\\n\\n[2026-05-16] **50% Dose-Response 5-seed 完整结果（D037 校正 Vanilla 值）**:\\n- TaxEI 50%: s42=51.1%, s0=70.2%, s123=46.8%, s1=63.8%, s7=55.3% → 均值 57.4±9.5%\\n- Random 50%: s42=57.4%, s0=46.8%, s123=70.2%, s1=70.2%, s7=46.8% → 均值 58.3±11.7%\\n- Vanilla (D037 corrected): s42=61.7%, s0=68.1%, s123=66.0%, s1=66.0%, s7=74.5% → 均值 67.3±4.7%\\n- Vanilla vs TaxEI 50%: p=0.0864, d=1.31 — 未过 Bonferroni\\n- Vanilla vs Random 50%: p=0.2453, d=1.01 — 不显著\\n- TaxEI ≈ Random at 50%: p=0.9203 — 几乎无差异\\n- Bootstrap Vanilla vs TaxEI: p=0.0104, CI=[2.16, 17.48]\\n- Random dose-response 单调递减显著 (Spearman rho=-0.9, p=0.037)\\n- s0/s123 值完全对调 (permutation p=0.13，不算罕见)\\n\\n[2026-05-16] **D040: WebShop 降级为 Discussion section。** P1 (step_order_swap) 无法适配 WebShop（action space 高度线性），taxonomy 从 4 缩到 3，跨环境对比不对等。论文 Discussion 增加 ALFWorld vs WebShop 结构性差异分析。Claim 8 从实验 claim 改为 Discussion 观察。\\n\\n[2026-05-16] **Failure Analysis 5-seed 平衡数据**: TaxEI loop_repetition 34.8% (Vanilla 15.6%, Random 12.8%)。TaxEI 是 Vanilla 的 2.2×、Random 的 2.7×。Loop 占 TaxEI 全部失败的 79%。数据来自 recovery eval trajectories（clean eval 不存 trajectory）。\\n\\n[2026-05-16] Recovery-paired datagen 完成: 711/760 variants 成功，输出 data/recovery_paired/recovery_paired.jsonl (20.8MB)。Operator 分布: C1=182, C4=175, P1=170, P2=184。\\n\\n[2026-05-16] **Recovery-paired SFT 数据设计**: recovery_paired.jsonl 是嵌套结构 (error_prefix + recovery_continuation)，需转换为扁平 messages 格式。用 recovery_only 模式提取 5,408 条 recovery continuation steps。TaxEI-RP = TaxEI 9,029 + recovery 5,408 = **14,437 samples**。Dry-run 成功 (5 steps, loss 4.019→2.424)，峰值显存 35.5 GiB。\\n\\n[2026-05-16] **TaxEI-RP Recovery Eval 5-seed 定论（D043 + s7 补全）**:\\n- s42: 38.3% (18/47) | C1=50%, C4=27.3%, P1=50%, P2=25%\\n- s0: 46.8% (22/47)\\n- s1: 48.9% (23/47) | C1=41.7%, C4=36.4%, P1=75%, P2=41.7%\\n- s123: 57.4% (27/47) | C1=58.3%, C4=45.5%, P1=66.7%, P2=58.3%\\n- s7: 59.6% (28/47)\\n- **Mean: 50.2±8.6%** — 低于 TaxEI baseline (58.3%) 和 Vanilla (67.3%)\\n- Detection rate 全 0%\\n- **结论: Recovery-paired training 适得其反，模型学到了错误模式而非恢复能力 (Claim 7 定论)**\\n\\n[2026-05-16] **Qwen Recovery Eval 完成 15/15 ✓**:\\n- Vanilla: 61.7/68.1/66.0/66.0/74.5 → Mean 67.3±4.7% (5/5 ✅)\\n- TaxEI: 59.6/46.8/61.7/61.7/57.4 → Mean 57.4±6.4% (5/5 ✅)\\n- Random: 63.8/55.3/66.0/51.1/53.2 → Mean 57.9±6.0% (5/5 ✅)\\n- **Recovery eval 再次确认 TaxEI ≈ Random（57.4% vs 57.9%，差 0.5pp）**\\n- Recovery rate ≈ clean eval success rate（D041 结论：模型靠\\\"resilience\\\"通过 injected scenarios，不是靠检测和恢复）\\n\\n[2026-05-16] **LLaMA-3.1-8B 跨模型验证 3-seed 完整结果（D045）**:\\n- **Clean SR**:\\n  - Vanilla (4,358): s42=72.3%, s0=72.3%, s123=72.3% → Mean 72.3±0.0%\\n  - TaxEI (9,029): s42=76.6%, s0=76.6%, s123=61.7% → Mean 71.6±8.6%\\n  - Random (9,029): s42=76.6%, s0=74.5%, s123=76.6% → Mean 75.9±1.2%\\n- **Recovery Rate (injected)**:\\n  - Vanilla: s42=74.5%, s0=74.5%, s123=70.2% → Mean 73.1±2.5%\\n  - TaxEI: s42=74.5%, s0=74.5%, s123=59.6% → Mean 69.5±8.6%\\n  - Random: s42=76.6%, s0=74.5%, s123=78.7% → Mean 76.6±2.1%\\n- **⚠️ TaxEI s123 异常低（clean 61.7%, recovery 59.6%）**：其他 seed 均 74.5-76.6%，s123 拉低均值和方差。可能是 seed variance，论文需讨论。\\n- **⚠️ 训练数据量混淆（critical confound）**: Vanilla=4,358 samples, TaxEI/Random=9,029。TaxEI/Random clean SR 高于 Vanilla 可能是 2× 数据量导致，不是注入方法优势。\\n- **LLaMA injection penalty**: TaxEI vs Vanilla = -3.6pp（Qwen 为 -9pp）。Stronger model 更\\\"免疫\\\"注入惩罚。\\n- **TaxEI vs Random 跨模型**: TaxEI 71.6% vs Random 75.9% clean，差距主要由 TaxEI s123 异常造成。Taxonomy 跨模型零收益 claim 成立。\\n- **⚠️ detection_rate 指标为假阳性**：LLaMA 的 21-36% detection 全部由导航短语 \\\"go back to X\\\" 中的 \\\"back\\\" 触发关键词匹配，非真实错误检测。不可引用此指标。\\n\\n[2026-05-16] **Eval 脚本架构（P0 关键发现）**:\\n- `eval/injected_eval.py`: **永远注入错误**，没有 `--no_inject` 参数。输出 `recovery_rate` + `detection_rate` + `by_operator` 分解。`--model_variant` 仅作标签。\\n- `eval/recovery.py`: 有 `--inject` / `--no_inject` 开关，默认 `inject=False`（即 clean eval）。输出 `success_rate` + `by_task_type` 分解。\\n- **之前所有用 `injected_eval.py` 的 LLaMA 结果均为 injected recovery rate，不是 clean success rate。**\\n- Clean eval 命令: `python3 eval/recovery.py --model_path &lt;ckpt> --base_model &lt;base> --num_episodes 47 --task_list eval/eval_tasks_47.json --output eval_results/&lt;name>_clean.json`（不加 `--inject`）\\n\\n[2026-05-16] 50% 训练 OOM 教训: batch_size=8 + max_length=4096 对 50% 数据集 OOM。修复: bs=4, gradient_accumulation_steps=2。swift sft --model 必须用本地完整路径。\\n\\n[2026-05-15] submit_training_job 必须用 bash -c \\\"...\\\" 包裹含 source/conda 的命令。\\n\\n[2026-05-15] Registry 状态机不能跳步。转 RUNNING 必须带 spec。\\n\\n[2026-05-15] [失败模式] autodl-5090 项目路径为 /root/autodl-tmp/tax_error_inject_agent。\\n\\n[2026-05-16] **Worker 假完成反复发生**: Worker 启动后台进程后报 done，导致无人收集结果。vanilla-s123 injected eval 经历 5 次假完成才成功。关键教训：(1) Worker 必须轮询到进程结束并验证文件存在 (2) 不要信任 Worker 回调中的\\\"已启动\\\"报告 (3) 每个 eval 独占一张 GPU，禁止共享。\\n\\n[2026-05-16] **Cron EXIT_CODE=129 是 tmux SIGHUP 误报**: submit_training_job 的 tmux wrapper 在训练正常退出后收到 SIGHUP（tmux session 清理），导致退出码被覆盖为 129。训练本身退出码为 0。应检查 checkpoint 完整性而非依赖退出码。\\n\", \"total_chars\": 6492, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3c39b4c3-d0fe-4b67-ae5f-0c76666b5414",
  "isSidechain": true,
  "promptId": "c9510963-8cc8-47e6-89fa-87e64c7bc4cb",
  "agentId": "a6eb88c450ef5806d",
  "type": "user",
  "uuid": "2de1cbc7-94be-4f3a-98d0-b4273b6f9e01",
  "sourceToolAssistantUUID": "3c39b4c3-d0fe-4b67-ae5f-0c76666b5414",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-16T16:11:22.879Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_017NY6SV7R3yA8BxthE8wBTR`</summary>

```json
{
  "project": "tax_error_inject_agent",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2de1cbc7-94be-4f3a-98d0-b4273b6f9e01",
  "isSidechain": true,
  "agentId": "a6eb88c450ef5806d",
  "requestId": "req_011Cb6YKfoz47qEm6sg84ZBt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f2c684ae-bc75-4c4f-97b9-5d0b0d28d37d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011RJChbsbgDxufg1wYvLkrr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2297,
      "cache_read_input_tokens": 15914,
      "output_tokens": 386,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2297
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 386,
          "cache_read_input_tokens": 15914,
          "cache_creation_input_tokens": 2297,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2297,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-16T16:11:22.887Z_

<details><summary>↩ Tool result · `toolu_017NY6SV7R3yA8BxthE8wBTR`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'tax_error_inject_agent'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f2c684ae-bc75-4c4f-97b9-5d0b0d28d37d",
  "isSidechain": true,
  "promptId": "c9510963-8cc8-47e6-89fa-87e64c7bc4cb",
  "agentId": "a6eb88c450ef5806d",
  "type": "user",
  "uuid": "12d90d9f-458d-49d1-bafe-01fff69112d7",
  "sourceToolAssistantUUID": "f2c684ae-bc75-4c4f-97b9-5d0b0d28d37d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-16T16:11:28.463Z_

Now let me also look at the paper itself if there's a LaTeX draft.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12d90d9f-458d-49d1-bafe-01fff69112d7",
  "isSidechain": true,
  "agentId": "a6eb88c450ef5806d",
  "requestId": "req_011Cb6YL4Ct7ZWgAtUgGGTNw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1f85a6aa-04f1-40df-ab29-6684459d8700",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TLNEHQ9bsLYfuyfsaa5p8G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22213,
      "cache_read_input_tokens": 18211,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 22213,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T16:11:29.602Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01DsWCea4v1Qh5gH3xpQBfGF`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f85a6aa-04f1-40df-ab29-6684459d8700",
  "isSidechain": true,
  "agentId": "a6eb88c450ef5806d",
  "requestId": "req_011Cb6YL4Ct7ZWgAtUgGGTNw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "99d1f9ff-9fd4-45d1-bcaa-1899849955bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TLNEHQ9bsLYfuyfsaa5p8G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22213,
      "cache_read_input_tokens": 18211,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 22213,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T16:11:29.624Z_

<details><summary>↩ Tool result · `toolu_01DsWCea4v1Qh5gH3xpQBfGF`</summary>

```text
artifacts/dream_reports/dream_20260515T020837/best/paper.tex
artifacts/dream_reports/dream_20260515T020837/median/paper.tex
artifacts/dream_reports/dream_20260515T020837/worst/paper.tex
paper/method.tex
paper/analysis.tex
paper/discussion.tex
paper/introduction.tex
paper/related_work.tex
paper/abstract.tex
paper/conclusion.tex
paper/appendix.tex
paper/experiments.tex
docs/paper/analysis.tex
docs/paper/abstract.tex
docs/paper/introduction.tex
docs/paper/method.tex
docs/paper/conclusion.tex
docs/paper/limitations.tex
docs/paper/main.tex
docs/paper/experiments.tex
docs/paper/appendix.tex
docs/paper/discussion.tex
docs/paper/related_work.tex
artifacts/dream_reports/dream_20260516T153939/best/paper.tex
artifacts/dream_reports/dream_20260516T153939/median/paper.tex
artifacts/dream_reports/dream_20260516T153939/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "99d1f9ff-9fd4-45d1-bcaa-1899849955bc",
  "isSidechain": true,
  "promptId": "c9510963-8cc8-47e6-89fa-87e64c7bc4cb",
  "agentId": "a6eb88c450ef5806d",
  "type": "user",
  "uuid": "74f8688e-f6b8-4cb0-8f00-f0e49d2e4808",
  "sourceToolAssistantUUID": "99d1f9ff-9fd4-45d1-bcaa-1899849955bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T16:11:30.422Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_015BmmS52tbN1bcdhze2BK8E`</summary>

```json
{
  "project": "tax_error_inject_agent",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74f8688e-f6b8-4cb0-8f00-f0e49d2e4808",
  "isSidechain": true,
  "agentId": "a6eb88c450ef5806d",
  "requestId": "req_011Cb6YL4Ct7ZWgAtUgGGTNw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "49b8ac87-9619-4cc7-bf22-a4ad711d0d15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TLNEHQ9bsLYfuyfsaa5p8G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22213,
      "cache_read_input_tokens": 18211,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 22213,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T16:11:30.433Z_

<details><summary>↩ Tool result · `toolu_015BmmS52tbN1bcdhze2BK8E`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/ROADMAP.md\", \"content\": \"# tax_error_inject_agent — Research Dashboard\\n\\n> 最后更新: 2026-05-16 15:50 UTC | 更新原因: LLaMA 3-seed 数据齐全，framing 升级为跨模型训练不稳定性，dream 评估中\\n\\n## 核心方向\\nError injection 对 embodied planning agent 训练的影响：结构化注入(TaxEI)跨模型导致训练不稳定，Random 注入跨模型稳定，taxonomy 标签零收益。详见 paper_framing.md。\\n\\n## 当前进展\\n**阶段**: Research → 写作准备（实验主体完成，等 dream 评估新 framing）\\n\\n**核心实验完成度**:\\n- Qwen3-8B 5-seed 主实验: ✅ 完成（V=67.3%, T=R=58.3%）\\n- Qwen3-8B 5-seed 剂量响应(10/25/50/Full): ✅ 完成\\n- LLaMA-3.1-8B 3-seed 跨模型验证: ✅ 完成（D047）\\n- Recovery-paired injection (TaxEI-RP): ✅ 4-seed 完成（47.9%，D043）\\n- Recovery eval multi-seed: 7/15 完成，剩余 8 个进行中\\n- Scale-up datagen: ~405/1000，状态待确认\\n\\n**关键发现**:\\n- TaxEI 跨模型不稳定: Qwen -9pp 一致退化; LLaMA SD=8.6%, 1/3 seed catastrophic\\n- Random 跨模型稳定: Qwen -9pp; LLaMA 稳定甚至微提升(+3.5pp)\\n- Taxonomy 标签跨模型零收益: TaxEI≈Random（均值层面）\\n- 结构化注入的方差 >> 随机注入方差（跨模型成立）\\n\\n**Claims 支撑状态**: 9 个 claims，7 个有完整实验支撑，Claim 8 已取消，Claim 9 新增已完成\\n\\n## 近期任务\\n- [ ] Dream dream_20260516T153939 完成 → 分析审稿反馈\\n- [ ] Recovery eval 剩余 8/15 完成\\n- [ ] Scale-up datagen 状态确认（~405/1000）\\n- [ ] Dream 通过后 → 启动 Paper Agent 写作\\n- [ ] 统计检验补充：LLaMA 跨模型 Levene's test / bootstrap\\n\\n## GPU 预算\\n**分配**: autodl-5090 cuda:0/1/2/3（4× RTX 5090）\\n**当前占用**: Recovery eval multi-seed 4 GPU 并行\\n**累计**: ~150+ GPU-h（训练+eval+dose-response+cross-model）\\n\\n## 投稿目标\\nEMNLP 2026 Findings, 8-page long paper, Budapest Oct 22-29\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D047 | 2026-05-16 | LLaMA 3-seed 完成：TaxEI 跨模型不稳定确认，paper framing 升级为\\\"结 | llama31-vanilla-s123, llama31-taxei-s123, llama31-random-s123 |\\n| D046 | 2026-05-16 | D046: 撤销 D044 scale-up 暂停——9.3% 成功率是统计口径错误（714 exc | scale-up-data |\\n| D045 | 2026-05-16 | D045: Scope 最终判断——当前 scope 含 LLaMA 3-seed + recove | llama-cross-model, recovery-eval-multiseed, scale-up-data |\\n| D044 | 2026-05-16 | D044: Scale-up 数据收集暂停——成功率从 70% 崩到 9.3%，1000 目标不可行 | scale-up-data |\\n| D043 | 2026-05-16 | D043: TaxEI-RP (recovery-paired) 4-seed 结果: 47.9±7 | recovery-paired-injection, multiseed-taxei, multiseed-vanilla |\\n| D042 | 2026-05-16 | D042: Scope 扩展——加 LLaMA-3.1-8B 跨模型验证 + scale-up 25 | llama-cross-model, scale-up-data |\\n| D041 | 2026-05-16 | D041: Recovery rate ≈ normal eval rate — 模型是 \\\"resi | recovery-eval, recovery-eval-multiseed |\\n| D040 | 2026-05-16 | D040: WebShop replication 降级为 Discussion section 分 | webshop-replication |\\n| D039 | 2026-05-16 | D039: Recovery-paired SFT 启动 (Claim 7)。数据设计: TaxEI | recovery-paired-injection, dose-response-5seed |\\n| D038 | 2026-05-16 | D038: 50% dose-response 5-seed 完成，dose-response 全线 | dose-response-5seed |\\n\\n\\n\", \"total_chars\": 2523, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "49b8ac87-9619-4cc7-bf22-a4ad711d0d15",
  "isSidechain": true,
  "promptId": "c9510963-8cc8-47e6-89fa-87e64c7bc4cb",
  "agentId": "a6eb88c450ef5806d",
  "type": "user",
  "uuid": "1c761836-01c6-4705-bbeb-71569119c5f8",
  "sourceToolAssistantUUID": "49b8ac87-9619-4cc7-bf22-a4ad711d0d15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T16:11:30.767Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_019YVpDwLdFL4V6qUrLxhU8K`</summary>

```json
{
  "project": "tax_error_inject_agent",
  "file": "paper_checklist.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c761836-01c6-4705-bbeb-71569119c5f8",
  "isSidechain": true,
  "agentId": "a6eb88c450ef5806d",
  "requestId": "req_011Cb6YL4Ct7ZWgAtUgGGTNw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "33902d08-11a2-4a90-bbd0-e42c4b17e581",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TLNEHQ9bsLYfuyfsaa5p8G",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22213,
      "cache_read_input_tokens": 18211,
      "output_tokens": 304,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 22213
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 304,
          "cache_read_input_tokens": 18211,
          "cache_creation_input_tokens": 22213,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 22213,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T16:11:30.775Z_

<details><summary>↩ Tool result · `toolu_019YVpDwLdFL4V6qUrLxhU8K`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'tax_error_inject_agent'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "33902d08-11a2-4a90-bbd0-e42c4b17e581",
  "isSidechain": true,
  "promptId": "c9510963-8cc8-47e6-89fa-87e64c7bc4cb",
  "agentId": "a6eb88c450ef5806d",
  "type": "user",
  "uuid": "c2c40783-1652-473c-b70d-792019312012",
  "sourceToolAssistantUUID": "33902d08-11a2-4a90-bbd0-e42c4b17e581",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T16:11:34.231Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HyA6r8cLgfDtx8N3zHxoYo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2c40783-1652-473c-b70d-792019312012",
  "isSidechain": true,
  "agentId": "a6eb88c450ef5806d",
  "requestId": "req_011Cb6YLduAmuutcZtCCqsNR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "07f7642d-7b23-4d97-b291-7108f544f2e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016PyNUtC3G3M1mEXMpBiE67",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2366,
      "cache_read_input_tokens": 40424,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2366,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 71,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T16:11:34.237Z_

<details><summary>↩ Tool result · `toolu_01HyA6r8cLgfDtx8N3zHxoYo`</summary>

```text
1	\begin{abstract}
2	Taxonomy-guided error injection improves tool-use LLM agents by +57pp (PALADIN), but does this transfer to embodied planning? We test TaxEI---a four-operator error taxonomy---on ALFWorld with Qwen3-8B, comparing clean training (Vanilla), taxonomy-tagged injection (TaxEI), and generic-labeled injection (Random) across three seeds. TaxEI yields no improvement ($-8.6$pp, $p{=}0.054$). Beyond reporting this negative result, we identify three boundary conditions: (1)~a \emph{variance gradient} where training instability increases from Vanilla (SD 3.3pp) through Random (7.0pp) to TaxEI (8.6pp); (2)~a shared \emph{dose-response threshold} at 10--25\% injection where both methods collapse by 12.8pp; and (3)~a \emph{per-operator local/global split} where local errors (+9.1pp) are learnable but global errors ($-8.3$pp) are harmful. These findings suggest error injection requires discrete, observable, locally recoverable errors---conditions met in tool-use but not in embodied planning.
3	\end{abstract}
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "07f7642d-7b23-4d97-b291-7108f544f2e9",
  "isSidechain": true,
  "promptId": "c9510963-8cc8-47e6-89fa-87e64c7bc4cb",
  "agentId": "a6eb88c450ef5806d",
  "type": "user",
  "uuid": "856c0343-89ea-4be3-a55b-d30c3312ce4d",
  "sourceToolAssistantUUID": "07f7642d-7b23-4d97-b291-7108f544f2e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T16:11:34.691Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PirrZvDkZnL6wEXfmWVt46`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "856c0343-89ea-4be3-a55b-d30c3312ce4d",
  "isSidechain": true,
  "agentId": "a6eb88c450ef5806d",
  "requestId": "req_011Cb6YLduAmuutcZtCCqsNR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d30623ae-ba5c-4146-8298-7a4461097452",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016PyNUtC3G3M1mEXMpBiE67",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2366,
      "cache_read_input_tokens": 40424,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2366,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 71,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T16:11:34.701Z_

<details><summary>↩ Tool result · `toolu_01PirrZvDkZnL6wEXfmWVt46`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training LLM agents on failure trajectories is an increasingly popular paradigm. PALADIN \cite{paladin2025} demonstrates that taxonomy-guided error injection---where training data includes systematically corrupted trajectories tagged with error types---improves tool-use agent performance by +57pp. Related approaches using failure-augmented training show gains across tool-use \cite{song2024eto,eef2025,wang2024learning_from_failure} and dialogue tasks \cite{agentHER2025}. A natural question arises: does this transfer to embodied planning, where agents must execute multi-step physical manipulation tasks?
5	
6	We test this hypothesis on ALFWorld \cite{shridhar2021alfworld}, a text-based embodied planning benchmark. We design TaxEI, a four-operator error taxonomy for ALFWorld (step-order swaps, sub-goal deletions, context truncations, observation masking), and train Qwen3-8B agents under three conditions: clean demonstrations only (Vanilla), clean + taxonomy-tagged errors (TaxEI), and clean + generic-labeled errors (Random). Each condition uses three seeds.
7	
8	The answer is negative: TaxEI yields no improvement ($-8.6$pp, $p{=}0.054$) and directionally increases training instability. But the contribution of this paper is not merely reporting failure. We identify three boundary conditions that characterize \emph{when} error injection helps:
9	
10	\begin{enumerate}[nosep,leftmargin=*]
11	\item \textbf{Variance gradient.} Training instability follows an ordering: Vanilla (SD 3.3pp) $<$ Random (7.0pp) $<$ TaxEI (8.6pp). While all variance tests are NS at $n{=}3$, the directional pattern suggests taxonomy labels amplify seed sensitivity.
12	
13	\item \textbf{Dose-response threshold.} Both TaxEI and Random share a sharp performance collapse between 10\% and 25\% error injection ($-12.8$pp each), followed by a plateau. Below this threshold, TaxEI has zero effect while Random provides mild augmentation (+6.4pp).
14	
15	\item \textbf{Per-operator local/global split.} Local errors (observation masking: $+9.1$pp) are learnable; global errors (context truncation, sub-goal deletion: $-8.3$pp each) are harmful. This suggests error injection requires errors that are observable and locally recoverable---properties present in tool-use but largely absent in embodied planning.
16	\end{enumerate}
17	
18	These findings provide actionable guidance: before applying error injection to a new domain, practitioners should assess whether the task's error structure is discrete, observable, and locally recoverable.
19	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d30623ae-ba5c-4146-8298-7a4461097452",
  "isSidechain": true,
  "promptId": "c9510963-8cc8-47e6-89fa-87e64c7bc4cb",
  "agentId": "a6eb88c450ef5806d",
  "type": "user",
  "uuid": "3f8721db-c48f-46f8-b7e8-dab9fc3d381f",
  "sourceToolAssistantUUID": "d30623ae-ba5c-4146-8298-7a4461097452",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T16:11:34.868Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Gm7SGyjTdTndWhFEWkbrgX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f8721db-c48f-46f8-b7e8-dab9fc3d381f",
  "isSidechain": true,
  "agentId": "a6eb88c450ef5806d",
  "requestId": "req_011Cb6YLduAmuutcZtCCqsNR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "199cc309-a4de-40ef-95b7-50ab426170d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016PyNUtC3G3M1mEXMpBiE67",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2366,
      "cache_read_input_tokens": 40424,
      "output_tokens": 229,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2366
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 229,
          "cache_read_input_tokens": 40424,
          "cache_creation_input_tokens": 2366,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2366,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-16T16:11:34.872Z_

<details><summary>↩ Tool result · `toolu_01Gm7SGyjTdTndWhFEWkbrgX`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Error injection for LLM agents.}
5	Several recent methods augment agent training with failure trajectories. PALADIN \cite{paladin2025} uses a 5-category error taxonomy with retrieval-augmented recovery for tool-use agents. ETO \cite{song2024eto} applies DPO on exploration-generated failures. EEF \cite{eef2025} extracts positive signals from expert failures. Wang et al.\ \shortcite{wang2024learning_from_failure} integrate contrastive negative examples. AgentHER \cite{agentHER2025} applies hindsight relabeling. AgentDebug \cite{agentdebug2025} proposes a 5-dimensional error taxonomy for ALFWorld but focuses on diagnosis rather than training augmentation. Our work differs in two ways: (1) we test \emph{cross-domain transfer} of the error injection paradigm, and (2) we use direct SFT mixing rather than contrastive or DPO-based methods.
6	
7	\paragraph{Training instability and seed sensitivity.}
8	McCoy et al.\ \shortcite{mccoy2020seeds} show that BERT models with similar test performance exhibit large variability in out-of-distribution generalization across seeds. Mosbach et al.\ \shortcite{mosbach2021stability} identify instability in BERT fine-tuning and propose mitigation strategies. D'Amour et al.\ \shortcite{damour2022underspecification} frame this as underspecification in ML pipelines. Our variance gradient (Vanilla $<$ Random $<$ TaxEI) extends these observations to error-augmented agent training, suggesting that structured noise amplifies seed sensitivity.
9	
10	\paragraph{Data mixing and noise tolerance.}
11	Rolnick et al.\ \shortcite{rolnick2017robust} show deep networks are robust to massive label noise in vision---contrasting with our sharp threshold at 10--25\% injection in sequential decision-making. Ye et al.\ \shortcite{ye2025mixing_laws} establish data mixing laws with critical proportions for SFT. Bengio et al.\ \shortcite{bengio2009curriculum} introduce curriculum learning, where training order matters---our dose-response threshold echoes their finding that data composition has non-linear effects. Madry et al.\ \shortcite{madry2018adversarial} demonstrate the accuracy-robustness tradeoff in adversarial training, paralleling our observation that error injection degrades clean-task performance.
12	
13	\paragraph{ALFWorld methods.}
14	ReAct \cite{yao2023react} establishes the think/act prompting framework. Reflexion \cite{shinn2023reflexion} achieves $\sim$97\% on ALFWorld via multi-trial inference-time self-reflection---notably, inference-time reflection succeeds where our training-time injection fails. CoEx \cite{kim2025coex} reaches 93.3\% with co-evolving world models. AgentPRM \cite{agentprm2025} achieves 91.0\% with process reward models. Our 65.3\% vanilla baseline is consistent with single-trial SFT on an 8B model without inference-time augmentation.
15	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "199cc309-a4de-40ef-95b7-50ab426170d9",
  "isSidechain": true,
  "promptId": "c9510963-8cc8-47e6-89fa-87e64c7bc4cb",
  "agentId": "a6eb88c450ef5806d",
  "type": "user",
  "uuid": "7c3f1ce4-814f-4508-944f-9e48241a3087",
  "sourceToolAssistantUUID": "199cc309-a4de-40ef-95b7-50ab426170d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T16:11:40.239Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LJHneM4rWQwTY6cNRpySit`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c3f1ce4-814f-4508-944f-9e48241a3087",
  "isSidechain": true,
  "agentId": "a6eb88c450ef5806d",
  "requestId": "req_011Cb6YLwR8AgenFSFRb91DV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d78459d7-0645-4f40-a7e4-eb7047383ec1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CvLgDj9DiW34AHsyd2dnzf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2103,
      "cache_read_input_tokens": 42790,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2103,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 71,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-16T16:11:40.287Z_

<details><summary>↩ Tool result · `toolu_01LJHneM4rWQwTY6cNRpySit`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate three training conditions on ALFWorld's 47 unseen test tasks \cite{shridhar2021alfworld}: \textbf{Vanilla} (4{,}358 clean demonstrations), \textbf{TaxEI} (4{,}358 clean + 4{,}671 taxonomy-tagged error trajectories = 9{,}029), and \textbf{Random} (4{,}358 clean + 4{,}671 generic-labeled errors = 9{,}029). All models use Qwen3-8B with LoRA fine-tuning (rank 64, lr $2\times10^{-4}$, 3 epochs). We report results across three seeds (42, 0, 123).
5	
6	\subsection{Main Results}
7	\label{sec:main_results}
8	
9	Table~\ref{tab:main_results} shows three-seed evaluation results. TaxEI degrades directionally ($-8.6$pp vs.\ Vanilla), but the difference is not statistically significant (permutation test, $p{=}0.054$, $N{=}10{,}000$). No TaxEI seed exceeds the Vanilla mean. Random injection shows minimal degradation ($-2.2$pp, $p{>}0.3$).
10	
11	\begin{table}[t]
12	\centering
13	\small
14	\begin{tabular}{lccccc}
15	\toprule
16	\textbf{Method} & \textbf{$N$} & \textbf{s42} & \textbf{s0} & \textbf{s123} & \textbf{Mean$\pm$SD} \\
17	\midrule
18	Vanilla & 4{,}358 & 61.7 & 68.1 & 66.0 & 65.3$\pm$3.3 \\
19	TaxEI   & 9{,}029 & 61.7 & 46.8 & 61.7 & 56.7$\pm$8.6 \\
20	Random  & 9{,}029 & 66.0 & 55.3 & 68.1 & 63.1$\pm$7.0 \\
21	\bottomrule
22	\end{tabular}
23	\caption{Three-seed clean evaluation on ALFWorld (47 tasks, accuracy \%). TaxEI vs.\ Vanilla: $p{=}0.054$; TaxEI vs.\ Random: $p{=}0.170$; Random vs.\ Vanilla: $p{>}0.3$ (pooled permutation, 10K). Note: TaxEI/Random use $2.1\times$ more training data than Vanilla.}
24	\label{tab:main_results}
25	\end{table}
26	
27	Standard deviations follow a directional ordering: Vanilla (3.3pp) $<$ Random (7.0pp) $<$ TaxEI (8.6pp). However, this pattern is not statistically confirmed at $n{=}3$ (Levene's $p{=}0.085$; $F$-test $p{=}0.252$; bootstrap $P(\text{SD}_\text{TaxEI} > \text{SD}_\text{Vanilla}){=}69\%$).
28	
29	\subsection{Dose-Response}
30	\label{sec:dose_response}
31	
32	To control for data volume, we fix total training size at 4{,}358 and vary the injection ratio (Table~\ref{tab:dose_response}, Figure~\ref{fig:dose_response}). Both methods share a sharp threshold between 10\% and 25\% injection: TaxEI drops from 61.7\% to 48.9\% ($-12.8$pp); Random drops from 68.1\% to 55.3\% ($-12.8$pp). Beyond 25\%, performance plateaus rather than continuing to degrade.
33	
34	\begin{table}[t]
35	\centering
36	\small
37	\begin{tabular}{lcccc}
38	\toprule
39	\textbf{Dose} & \textbf{TaxEI} & \textbf{Random} & \textbf{$\Delta$T} & \textbf{$\Delta$R} \\
40	\midrule
41	0\% (Van.)  & 61.7 & 61.7 & ---   & ---   \\
42	10\%        & 61.7 & 68.1 & 0.0   & +6.4  \\
43	25\%        & 48.9 & 55.3 & $-$12.8 & $-$6.4  \\
44	50\%        & 51.1 & 57.4 & $-$10.6 & $-$4.3  \\
45	\bottomrule
46	\end{tabular}
47	\caption{Dose-response ablation (fixed 4{,}358 total, seed=42 only). $\Delta$T/$\Delta$R: change vs.\ vanilla. Both methods share a 12.8pp drop at 10$\to$25\%.}
48	\label{tab:dose_response}
49	\end{table}
50	
51	\begin{figure}[t]
52	\centering
53	\includegraphics[width=\columnwidth]{figures/paper/fig1_dose_response.pdf}
54	\caption{Dose-response: accuracy vs.\ injection ratio. Both TaxEI and Random share a 12.8pp collapse at 10$\to$25\%. Single seed (seed=42).}
55	\label{fig:dose_response}
56	\end{figure}
57	
58	At 10\% injection, TaxEI is task-identical to Vanilla (same success/failure on every task), while Random shows a +6.4pp augmentation effect. This suggests the model absorbs sub-threshold random noise as data augmentation but ignores taxonomy-tagged errors entirely at low doses.
59	
60	\subsection{Task-Type Vulnerability}
61	\label{sec:task_vulnerability}
62	
63	The TaxEI--Random gap is not uniform across task types. Three-seed averages reveal that two of six task types drive the aggregate difference: \texttt{pick\_cool} (TaxEI$-$Random $= -19.0$pp) and \texttt{pick\_two\_obj} ($-14.3$pp). The remaining four types show gaps $\leq$4.2pp, with \texttt{pick\_heat} and \texttt{look\_at\_obj} at exactly 0pp. This concentration suggests taxonomy-guided errors interact with specific action-sequence structures rather than causing uniform degradation.
64	
65	\subsection{Recovery Evaluation}
66	\label{sec:recovery}
67	
68	We test whether error-trained models recover from injected errors at inference time using round-robin operator injection across 47 tasks (seed=42). TaxEI achieves 59.6\% recovery (vs.\ Vanilla 61.7\%, Random 63.8\%)---no improvement over the clean baseline. Error detection rate is 0\% for all methods: no model produces explicit error acknowledgment before attempting recovery.
69	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d78459d7-0645-4f40-a7e4-eb7047383ec1",
  "isSidechain": true,
  "promptId": "c9510963-8cc8-47e6-89fa-87e64c7bc4cb",
  "agentId": "a6eb88c450ef5806d",
  "type": "user",
  "uuid": "9b156a02-fd84-4ce5-beca-65edba151136",
  "sourceToolAssistantUUID": "d78459d7-0645-4f40-a7e4-eb7047383ec1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-16T16:11:40.832Z_

<details open><summary>🔧 Tool call — Read · `toolu_017yzVnCDUvBYBELFJtFFANz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b156a02-fd84-4ce5-beca-65edba151136",
  "isSidechain": true,
  "agentId": "a6eb88c450ef5806d",
  "requestId": "req_011Cb6YLwR8AgenFSFRb91DV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e8a7cdb9-6854-4e06-b5f5-6a16273ec325",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CvLgDj9DiW34AHsyd2dnzf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2103,
      "cache_read_input_tokens": 42790,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2103,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 71,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-16T16:11:40.848Z_

<details><summary>↩ Tool result · `toolu_017yzVnCDUvBYBELFJtFFANz`</summary>

```text
1	\section{Analysis}
2	\label{sec:analysis}
3	
4	\subsection{Per-Operator Local/Global Split}
5	\label{sec:operator_split}
6	
7	Figure~\ref{fig:operator_gradient} decomposes TaxEI's recovery performance by operator (seed=42, $N{=}11$--$12$ tasks per operator). The results reveal a binary split rather than a smooth gradient:
8	
9	\begin{itemize}[nosep,leftmargin=*]
10	\item \textbf{Local operators}: C4 (observation masking) shows $+9.1$pp improvement over Vanilla; P1 (step order swap) shows $0.0$pp change.
11	\item \textbf{Global operators}: Both C1 (context truncation, $-8.3$pp) and P2 (sub-goal deletion, $-8.3$pp) degrade performance.
12	\end{itemize}
13	
14	\begin{figure}[t]
15	\centering
16	\includegraphics[width=\columnwidth]{figures/paper/fig2_operator_gradient.pdf}
17	\caption{Per-operator recovery delta (TaxEI $-$ Vanilla, seed=42). Local/observable errors (C4, P1) are neutral-to-beneficial; global/cascading errors (C1, P2) are harmful. $N{=}11$--$12$ per operator; differences of $\pm1$ task correspond to $\pm$8--9pp. Exploratory analysis.}
18	\label{fig:operator_gradient}
19	\end{figure}
20	
21	This split aligns with an intuitive distinction: local errors (a masked observation, a swapped step) leave the plan's causal structure intact, allowing the model to learn recovery patterns. Global errors (truncated context, deleted sub-goals) propagate downstream, making all subsequent actions unreliable---the model memorizes noise rather than learning recovery.
22	
23	C1 (context truncation) is classified as a Context-type operator but behaves like a global operator: truncating the context window forces all subsequent decisions to rely on incomplete history, functionally equivalent to a cascading plan disruption.
24	
25	We emphasize that these per-operator results are exploratory: at $N{=}11$--$12$ tasks per operator, each $\pm1$ task flip corresponds to $\pm$8--9pp, and we cannot draw statistically robust conclusions from single-task margins.
26	
27	\subsection{Training-Evaluation Paradox}
28	\label{sec:paradox}
29	
30	At $\geq$25\% injection, models achieve \emph{lower} training loss but \emph{worse} evaluation performance. TaxEI-50\% reaches a final loss of 0.259 (vs.\ Vanilla 0.288) yet evaluates at 51.1\% (vs.\ 61.7\%). This paradox does not hold at 10\% injection, where training loss (0.308) remains above Vanilla---the model has not yet begun memorizing injected patterns at sub-threshold doses.
31	
32	This pattern is consistent with findings on memorization in noisy-label settings: models first learn clean patterns, then memorize noise \cite{arpit2017memorization}. In our setting, injected error trajectories are well-formed sequences that the model can memorize as surface patterns \cite{zhou2023lima}, improving training metrics without generalizing to unseen tasks.
33	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e8a7cdb9-6854-4e06-b5f5-6a16273ec325",
  "isSidechain": true,
  "promptId": "c9510963-8cc8-47e6-89fa-87e64c7bc4cb",
  "agentId": "a6eb88c450ef5806d",
  "type": "user",
  "uuid": "9794c423-3468-411e-8417-523537a400a2",
  "sourceToolAssistantUUID": "e8a7cdb9-6854-4e06-b5f5-6a16273ec325",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-16T16:11:41.006Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BrBNYLfcEabwA3ZuBAk7EQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9794c423-3468-411e-8417-523537a400a2",
  "isSidechain": true,
  "agentId": "a6eb88c450ef5806d",
  "requestId": "req_011Cb6YLwR8AgenFSFRb91DV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9d1438ca-dd20-41fa-aabd-ff20cccadcd0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CvLgDj9DiW34AHsyd2dnzf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2103,
      "cache_read_input_tokens": 42790,
      "output_tokens": 227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2103
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 227,
          "cache_read_input_tokens": 42790,
          "cache_creation_input_tokens": 2103,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2103,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-16T16:11:41.015Z_

<details><summary>↩ Tool result · `toolu_01BrBNYLfcEabwA3ZuBAk7EQ`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\subsection{Why Does Error Injection Fail on Embodied Planning?}
5	\label{sec:structural_hypothesis}
6	
7	We hypothesize that the transfer failure stems from structural differences between tool-use and embodied planning tasks. Table~\ref{tab:structural} contrasts the two domains across key dimensions.
8	
9	\begin{table}[t]
10	\centering
11	\small
12	\begin{tabular}{p{2.2cm}p{2.3cm}p{2.3cm}}
13	\toprule
14	\textbf{Dimension} & \textbf{Tool-Use} \cite{paladin2025} & \textbf{Embodied} \\
15	\midrule
16	Error signal & Discrete (API error codes) & Diffuse (wrong object, wrong room) \\
17	Observability & Explicit (stack trace) & Silent (no error msg) \\
18	Recovery scope & Local (retry call) & Global (replan) \\
19	Feedback & Immediate & Delayed \\
20	Error locality & Single step & Cascading \\
21	\bottomrule
22	\end{tabular}
23	\caption{Structural comparison: tool-use vs.\ embodied planning. Error injection benefits from discrete, observable, locally recoverable errors.}
24	\label{tab:structural}
25	\end{table}
26	
27	In tool-use, errors produce discrete signals (API error codes, type mismatches) that map directly to specific recovery actions. The agent learns a conditional policy: ``if error type X, then recovery action Y.'' In embodied planning, errors propagate silently through the action sequence---picking the wrong object produces no error message, and recovery requires replanning from an unknown state. The taxonomy labels that help in tool-use (mapping error types to recovery strategies) become noise in embodied planning because there is no clean error$\to$recovery mapping to learn.
28	
29	\subsection{Alternative Explanation: Recovery-Pairing Confound}
30	\label{sec:confound}
31	
32	An important methodological difference between PALADIN and our setup: PALADIN pairs each error trajectory with an explicit recovery demonstration at inference time via retrieval augmentation, contributing an estimated $\sim$30pp of its +57pp gain. Our TaxEI injects standalone errors without paired recoveries. The negative result may therefore stem from missing recovery pairing rather than (or in addition to) task structure. Future work should test recovery-paired injection on ALFWorld to disentangle these factors.
33	
34	\subsection{Limitations}
35	\label{sec:limitations}
36	
37	\paragraph{Scale.} We evaluate on a single environment (ALFWorld, 47 tasks) with one base model (Qwen3-8B). Generalization to other embodied environments (e.g., WebShop) and model scales remains untested.
38	
39	\paragraph{Statistical power.} Three seeds provide limited statistical power: all comparisons are NS, and the variance gradient ($3.3 < 7.0 < 8.6$pp SD) is directional but underpowered. We acknowledge the tension in arguing that $n{=}3$ is insufficient while reporting only $n{=}3$ ourselves.
40	
41	\paragraph{Dose-response.} The dose-response ablation uses a single seed, preventing confidence intervals. The threshold observation (10$\to$25\%) requires multi-seed replication.
42	
43	\paragraph{Data asymmetry.} TaxEI and Random use $2.1\times$ more training data than Vanilla (9{,}029 vs.\ 4{,}358). The fixed-size dose-response ablation (4{,}358 total) partially controls for this, showing that the degradation is not merely a volume effect.
44	
45	\paragraph{Per-operator analysis.} With $N{=}11$--$12$ tasks per operator, the local/global split is exploratory. A single task flip changes the delta by 8--9pp.
46	
47	\paragraph{Version discrepancy.} Our evaluation pipeline evolved from v3 (74.5\% vanilla) to v4 (65.3\% vanilla) due to format alignment changes and seed standardization. All reported results use v4.
48	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d1438ca-dd20-41fa-aabd-ff20cccadcd0",
  "isSidechain": true,
  "promptId": "c9510963-8cc8-47e6-89fa-87e64c7bc4cb",
  "agentId": "a6eb88c450ef5806d",
  "type": "user",
  "uuid": "84c57b12-ea97-4863-bb79-e398a41b463a",
  "sourceToolAssistantUUID": "9d1438ca-dd20-41fa-aabd-ff20cccadcd0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-16T16:11:44.510Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NkU8ZGg4GGYEYy8oDHD4Kq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84c57b12-ea97-4863-bb79-e398a41b463a",
  "isSidechain": true,
  "agentId": "a6eb88c450ef5806d",
  "requestId": "req_011Cb6YMPq7MaYBiRFV8RGKg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c0f09af6-67fe-43d5-8cd6-dc448b646655",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AAKQYzBP9sX9kQn3V1Frss",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4118,
      "cache_read_input_tokens": 44893,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4118,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 63,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-16T16:11:44.523Z_

<details><summary>↩ Tool result · `toolu_01NkU8ZGg4GGYEYy8oDHD4Kq`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task Environment}
5	\label{sec:task_env}
6	
7	ALFWorld \cite{shridhar2021alfworld} is a text-based embodied environment where agents execute multi-step household tasks (e.g., \emph{heat a potato and place it in the fridge}). Each task requires a sequence of \texttt{think}/\texttt{act} steps in a ReAct-style loop \cite{yao2023react}. We use the standard 47-task unseen test split across six task types: \texttt{look\_at\_obj}, \texttt{pick\_and\_place}, \texttt{pick\_clean}, \texttt{pick\_cool}, \texttt{pick\_heat}, and \texttt{pick\_two\_obj}.
8	
9	\subsection{Error Taxonomy}
10	\label{sec:error_taxonomy}
11	
12	We define four error injection operators adapted for embodied planning, organized along two axes:
13	
14	\paragraph{Local operators} affect single steps without disrupting the overall plan structure:
15	\begin{itemize}[nosep,leftmargin=*]
16	\item \textbf{C4 (observation\_masking)}: Replaces environment observations with generic placeholders, removing perceptual grounding for one step.
17	\item \textbf{P1 (step\_order\_swap)}: Swaps two adjacent action steps, creating a locally incorrect but recoverable sequence.
18	\end{itemize}
19	
20	\paragraph{Global operators} disrupt the trajectory's causal chain:
21	\begin{itemize}[nosep,leftmargin=*]
22	\item \textbf{P2 (sub\_goal\_deletion)}: Removes a complete sub-goal (e.g., the ``clean'' step in a pick-clean-place task), breaking the plan's logical structure.
23	\item \textbf{C1 (context\_truncation)}: Truncates the context window, causing all subsequent decisions to rely on incomplete history.
24	\end{itemize}
25	
26	All operators achieve 100\% injection legality (valid action format) and 97.5\% recovery quality (trajectories remain parseable). Error-recovery pairs are \emph{not} explicitly paired in training data---errors are mixed as additional demonstrations.
27	
28	\subsection{Training Setup}
29	\label{sec:training_setup}
30	
31	We collect 501 expert trajectories from GPT-5.2 on ALFWorld training tasks, yielding 4{,}358 clean SFT demonstrations. Error injection produces 4{,}671 additional trajectories (round-robin across the four operators).
32	
33	\paragraph{Three conditions:}
34	\begin{itemize}[nosep,leftmargin=*]
35	\item \textbf{Vanilla}: 4{,}358 clean demonstrations only.
36	\item \textbf{TaxEI}: 4{,}358 clean + 4{,}671 taxonomy-tagged errors (error type labels in prompt) = 9{,}029 total.
37	\item \textbf{Random}: 4{,}358 clean + 4{,}671 generic-labeled errors (no taxonomy) = 9{,}029 total.
38	\end{itemize}
39	
40	All models fine-tune Qwen3-8B using LoRA (rank 64, $\alpha{=}128$, lr $2{\times}10^{-4}$, 3 epochs, bf16). Each condition is trained with three seeds (42, 0, 123).
41	
42	\paragraph{Dose-response ablation.} To control for data volume effects, we fix total training size at 4{,}358 and vary the error injection ratio (10\%, 25\%, 50\%), using seed=42 only.
43	
44	\paragraph{Recovery evaluation.} We inject errors at inference time using round-robin operator assignment across 47 test tasks and measure whether error-trained models recover better than vanilla.
45	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c0f09af6-67fe-43d5-8cd6-dc448b646655",
  "isSidechain": true,
  "promptId": "c9510963-8cc8-47e6-89fa-87e64c7bc4cb",
  "agentId": "a6eb88c450ef5806d",
  "type": "user",
  "uuid": "340295ef-63a7-4f57-87b9-efc97f9e62ac",
  "sourceToolAssistantUUID": "c0f09af6-67fe-43d5-8cd6-dc448b646655",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-16T16:11:44.909Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WdifiN23VMhmnUktGeCAtT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "340295ef-63a7-4f57-87b9-efc97f9e62ac",
  "isSidechain": true,
  "agentId": "a6eb88c450ef5806d",
  "requestId": "req_011Cb6YMPq7MaYBiRFV8RGKg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f987a654-a376-4523-8bb5-a39f32b1a78f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AAKQYzBP9sX9kQn3V1Frss",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4118,
      "cache_read_input_tokens": 44893,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4118,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 63,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-16T16:11:44.913Z_

<details><summary>↩ Tool result · `toolu_01WdifiN23VMhmnUktGeCAtT`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We tested whether taxonomy-guided error injection---effective for tool-use agents---transfers to embodied planning. On ALFWorld, TaxEI provides no improvement over clean training ($-8.6$pp, $p{=}0.054$) and directionally increases training instability. We identify three boundary conditions: a variance gradient (Vanilla $<$ Random $<$ TaxEI), a shared dose-response threshold at 10--25\% injection, and a per-operator local/global split where only local, observable errors are learnable.
5	
6	For practitioners considering error injection in new domains, we recommend checking three properties: (1)~are errors discrete and observable? (2)~can recovery be achieved locally? (3)~does the task provide immediate feedback? If not, error injection is likely to introduce noise rather than curriculum signal.
7	
8	Future work should test recovery-paired injection on ALFWorld (disentangling the PALADIN confound), replicate on a second environment (e.g., WebShop), and run multi-seed dose-response ablations.
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f987a654-a376-4523-8bb5-a39f32b1a78f",
  "isSidechain": true,
  "promptId": "c9510963-8cc8-47e6-89fa-87e64c7bc4cb",
  "agentId": "a6eb88c450ef5806d",
  "type": "user",
  "uuid": "d93ea2c2-0fbf-451f-b1c0-38d2a11e43e8",
  "sourceToolAssistantUUID": "f987a654-a376-4523-8bb5-a39f32b1a78f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-16T16:11:45.435Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DoNhwPyF22J6mtmb3rTqVs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d93ea2c2-0fbf-451f-b1c0-38d2a11e43e8",
  "isSidechain": true,
  "agentId": "a6eb88c450ef5806d",
  "requestId": "req_011Cb6YMPq7MaYBiRFV8RGKg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5a690019-9827-46d0-9ccb-d0e76479cbe1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AAKQYzBP9sX9kQn3V1Frss",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4118,
      "cache_read_input_tokens": 44893,
      "output_tokens": 228,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4118
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 228,
          "cache_read_input_tokens": 44893,
          "cache_creation_input_tokens": 4118,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4118,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-16T16:11:45.440Z_

<details><summary>↩ Tool result · `toolu_01DoNhwPyF22J6mtmb3rTqVs`</summary>

```text
1	\appendix
2	
3	\section{Training Dynamics}
4	\label{app:training_dynamics}
5	
6	Figure~\ref{fig:training_curves} shows training loss and token accuracy curves across conditions. At $\geq$25\% injection, models achieve lower final training loss than Vanilla (TaxEI-50\%: 0.259 vs.\ Vanilla: 0.288) despite worse evaluation performance, illustrating the training-evaluation paradox discussed in \S\ref{sec:paradox}. At 10\% injection, training loss (0.308) remains above Vanilla, consistent with the sub-threshold null effect observed in evaluation.
7	
8	\begin{figure}[t]
9	\centering
10	\includegraphics[width=\columnwidth]{figures/paper/fig_app_training_curves.pdf}
11	\caption{Training dynamics. Left: loss curves for Vanilla, TaxEI-50\%, and Random-50\%. Right: final training loss vs.\ evaluation accuracy, showing the paradox where lower loss corresponds to worse performance at $\geq$25\% injection.}
12	\label{fig:training_curves}
13	\end{figure}
14	
15	\section{Full 47-Task Results}
16	\label{app:full_tasks}
17	
18	Table~\ref{tab:full_tasks} reports per-task success/failure across all three-seed conditions. Bold entries indicate discordant pairs (TaxEI $\neq$ Random at same seed).
19	
20	\begin{table*}[t]
21	\centering
22	\scriptsize
23	\setlength{\tabcolsep}{3pt}
24	\begin{tabular}{lcccccccccc}
25	\toprule
26	\textbf{Task} & \textbf{V-42} & \textbf{V-0} & \textbf{V-123} & \textbf{T-42} & \textbf{T-0} & \textbf{T-123} & \textbf{R-42} & \textbf{R-0} & \textbf{R-123} \\
27	\midrule
28	look\_at\_obj-AlarmClock & \cmark & \cmark & \cmark & \cmark & \cmark & \cmark & \cmark & \cmark & \cmark \\
29	look\_at\_obj-Book & \xmark & \xmark & \xmark & \xmark & \xmark & \xmark & \xmark & \xmark & \xmark \\
30	look\_at\_obj-Bowl & \cmark & \cmark & \cmark & \cmark & \cmark & \cmark & \cmark & \cmark & \cmark \\
31	look\_at\_obj-CD & \cmark & \cmark & \cmark & \cmark & \cmark & \cmark & \cmark & \cmark & \cmark \\
32	look\_at\_obj-Mug & \cmark & \cmark & \cmark & \cmark & \cmark & \cmark & \cmark & \cmark & \cmark \\
33	look\_at\_obj-Pencil & \cmark & \cmark & \cmark & \cmark & \cmark & \cmark & \cmark & \cmark & \cmark \\
34	\midrule
35	pick\_place-Mug & \cmark & \cmark & \cmark & \cmark & \cmark & \cmark & \cmark & \cmark & \cmark \\
36	pick\_place-Pencil & \xmark & \xmark & \xmark & \xmark & \xmark & \xmark & \xmark & \xmark & \xmark \\
37	pick\_place-PepperShaker & \xmark & \xmark & \xmark & \xmark & \xmark & \xmark & \xmark & \xmark & \xmark \\
38	pick\_place-SaltShaker-Cab & \xmark & \xmark & \xmark & \xmark & \xmark & \xmark & \xmark & \xmark & \xmark \\
39	pick\_place-SaltShaker-Drw & \cmark & \cmark & \cmark & \cmark & \xmark & \cmark & \cmark & \xmark & \cmark \\
40	pick\_place-SoapBottle & \cmark & \cmark & \cmark & \cmark & \cmark & \cmark & \cmark & \cmark & \cmark \\
41	pick\_place-Vase & \cmark & \cmark & \cmark & \cmark & \xmark & \xmark & \xmark & \cmark & \cmark \\
42	pick\_place-Watch & \cmark & \cmark & \cmark & \xmark & \xmark & \xmark & \xmark & \xmark & \cmark \\
43	\midrule
44	\multicolumn{10}{c}{\emph{(Remaining 25 tasks follow same format; full table available in supplementary materials.)}} \\
45	\bottomrule
46	\end{tabular}
47	\caption{Per-task results for first 22 tasks (abbreviated). V=Vanilla, T=TaxEI, R=Random. \cmark=success, \xmark=failure.}
48	\label{tab:full_tasks}
49	\end{table*}
50	
51	\section{Per-Task Cross-Analysis}
52	\label{app:cross_analysis}
53	
54	The $\sim$6.4pp aggregate gap between TaxEI and Random at each dose point (Table~\ref{tab:dose_response}) corresponds to $\approx$3 tasks on a 47-task evaluation. Cross-dose analysis reveals this is a discretization coincidence: zero tasks appear as TaxEI-penalty in all three dose points (10\%, 25\%, 50\%). The specific tasks that flip between conditions rotate across doses---9 different tasks contribute to the penalty across all doses, with no single task appearing at all three levels. This rules out a systematic mechanism targeting a fixed task subset.
55	
56	\section{Version Discrepancy}
57	\label{app:version}
58	
59	Our evaluation pipeline evolved from v3 to v4 during development. The v3 vanilla baseline (74.5\%, seed=42) was higher due to a format mismatch that inadvertently helped certain task types. After standardizing prompt formatting and fixing seed handling, v4 vanilla dropped to 61.7\% (seed=42). All results in this paper use v4 exclusively.
60	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a690019-9827-46d0-9ccb-d0e76479cbe1",
  "isSidechain": true,
  "promptId": "c9510963-8cc8-47e6-89fa-87e64c7bc4cb",
  "agentId": "a6eb88c450ef5806d",
  "type": "user",
  "uuid": "020541a2-7f11-4fd6-81a0-aa949709d5c4",
  "sourceToolAssistantUUID": "5a690019-9827-46d0-9ccb-d0e76479cbe1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-16T16:11:51.506Z_

Now I have a thorough understanding of both the paper as written in the LaTeX draft and the much more extensive experimental results documented in `paper_framing.md`. Let me note that the LaTeX draft appears to be an older 4-page short paper version (3 seeds only), while the `paper_framing.md` documents the full 8-page long paper scope with 5 seeds, cross-model validation, recovery-paired injection, and more. Let me now check the latest dream review for additional context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "020541a2-7f11-4fd6-81a0-aa949709d5c4",
  "isSidechain": true,
  "agentId": "a6eb88c450ef5806d",
  "requestId": "req_011Cb6YMiT3M5M9hCFswTJbE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5e165fbc-148e-4d81-892c-9e1b2f76b44d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NzPviaLRhXwHetKsWBUeAb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3272,
      "cache_read_input_tokens": 49011,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3272,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-16T16:11:52.701Z_

<details open><summary>🔧 Tool call — Read · `toolu_013k3hfT1MmLmGefSdEPE7wX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260516T153939/median/paper.tex",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e165fbc-148e-4d81-892c-9e1b2f76b44d",
  "isSidechain": true,
  "agentId": "a6eb88c450ef5806d",
  "requestId": "req_011Cb6YMiT3M5M9hCFswTJbE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "976be0fb-e2bb-45a7-b34d-670f98c52100",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NzPviaLRhXwHetKsWBUeAb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3272,
      "cache_read_input_tokens": 49011,
      "output_tokens": 232,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3272
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 232,
          "cache_read_input_tokens": 49011,
          "cache_creation_input_tokens": 3272,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3272,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-16T16:11:52.712Z_

<details><summary>↩ Tool result · `toolu_013k3hfT1MmLmGefSdEPE7wX`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{xcolor}
11	\usepackage{pgfplots}
12	\pgfplotsset{compat=1.18}
13	\usepackage{tikz}
14	\usepackage{natbib}
15	\usepackage{pifont}
16	\usepackage{hyperref}
17	
18	\title{Empirical Evidence Toward Boundary Conditions for Error Injection\\in LLM Agent Training: A Negative Transfer Study}
19	
20	\author{Anonymous}
21	
22	\begin{document}
23	\maketitle
24	
25	% ============================================================
26	\begin{abstract}
27	Taxonomy-guided error injection has shown promise for improving LLM agent robustness in tool-use domains, with PALADIN reporting substantial recovery rate gains on ToolBench.
28	We investigate whether this training paradigm transfers to embodied planning by designing TaxEI, a 4-operator error injection taxonomy for ALFWorld, and training Qwen3-8B under three conditions: Vanilla (clean data), TaxEI (taxonomy-labeled injection), and Random (unlabeled injection).
29	Across 5 random seeds, both injection methods degrade performance identically (58.3\% vs.\ Vanilla 67.3\%, Cohen's $d$=1.58), and taxonomy labels provide zero benefit over random noise.
30	Recovery evaluation reveals that models exhibit \emph{resilience}---passively ignoring eval-time perturbations at their base task-completion rate---rather than \emph{recovery}---actively detecting and correcting errors (detection rate: 0\%).
31	Preliminary cross-model evidence on LLaMA-3.1-8B-Instruct (3 seeds) shows TaxEI introduces training instability (SD=8.6pp vs.\ Random SD=2.1pp) with 1/3 seeds exhibiting catastrophic degradation, suggesting the harm generalizes beyond a single architecture.
32	A 5$\times$ data scale-up narrows the penalty from 9.0pp to 6.4pp but does not eliminate it.
33	These results constitute a large effect size suggestive of harm from error injection in embodied planning, requiring larger $N$ for definitive confirmation, and point toward task-structural boundary conditions---error observability, locality, and recoverability---that determine when injection helps versus harms.
34	\end{abstract}
35	
36	% ============================================================
37	\section{Introduction}
38	
39	Error injection is a natural data augmentation strategy for training robust LLM agents: expose models to failure modes during training so they learn to recognize and recover from errors at deployment time.
40	PALADIN \cite{chen2025paladin} demonstrated this approach for tool-use agents, combining taxonomy-guided error injection with inference-time retrieval augmentation to achieve substantial gains on ToolBench.
41	A natural question arises: does the error-injection \emph{training} component transfer to other agent domains?
42	
43	We test this hypothesis on embodied planning using ALFWorld \cite{shridhar2021alfworld}, where agents execute multi-step plans in simulated household environments.
44	We design TaxEI (\textbf{Tax}onomy-guided \textbf{E}rror \textbf{I}njection), a 4-operator error taxonomy covering planning-level and context-level perturbations, and train Qwen3-8B \cite{qwen3} under three matched conditions: Vanilla (clean trajectories only), TaxEI (clean + taxonomy-labeled injections), and Random (clean + unlabeled injections).
45	
46	Our results provide empirical evidence toward boundary conditions for error injection:
47	\begin{itemize}
48	\item Both injection methods degrade performance by 9.0 percentage points (pp) relative to Vanilla training, with large effect size (Cohen's $d$=1.58) but marginal statistical significance after multiple-comparison correction (Bonferroni NS at $n$=5; statistical power = 45\%).
49	\item Taxonomy labels provide \emph{zero} measurable benefit: TaxEI and Random achieve identical mean performance (58.3\%).
50	\item Models exhibit \emph{resilience}---passively tolerating eval-time errors at their base task-completion rate---rather than \emph{recovery}. Detection rate is 0\% across all conditions.
51	\item Preliminary cross-model evidence on LLaMA-3.1-8B-Instruct (3 seeds) suggests structured injection introduces training instability across architectures.
52	\item A 5$\times$ data scale-up partially mitigates (29\% gap reduction) but does not eliminate the harm, suggesting task-structural factors as a co-dominant contributor.
53	\end{itemize}
54	
55	We frame these findings within a 2$\times$2 meta-analysis of error-signal approaches (Section~\ref{sec:discussion}), contrasting \emph{positive} vs.\ \emph{negative} training signals across \emph{tool-use} and \emph{planning} domains.
56	Combined with concurrent work on learning from failures \cite{wang2025eef}, our results suggest that the \emph{direction} of training signal---extracting positive signal from failures vs.\ injecting negative signal---may matter as much as the domain itself.
57	
58	% ============================================================
59	\section{Related Work}
60	
61	\paragraph{Error injection for LLM agents.}
62	PALADIN \cite{chen2025paladin} introduces ToolScan, a taxonomy of 7 tool-use failure types, and generates 50K+ recovery-annotated trajectories.
63	Combined with inference-time retrieval of 55+ exemplars, PALADIN achieves +57pp recovery rate on ToolBench---though removing retrieval reduces gains by $\sim$30pp, indicating substantial contribution from inference-time augmentation beyond SFT.
64	EEF \cite{wang2025eef} takes the opposite approach on WebShop, \emph{extracting} positive signal from failed trajectories rather than \emph{injecting} errors, achieving gains via failure-distilled experience.
65	
66	\paragraph{Embodied planning agents.}
67	ALFWorld \cite{shridhar2021alfworld} provides a text-based interface to ALFRED household tasks.
68	ReAct \cite{yao2023react} and Reflexion \cite{shinn2023reflexion} demonstrate that LLMs can perform multi-step planning with appropriate prompting, but neither studies error injection as a training-time augmentation.
69	
70	\paragraph{Training instability and seed sensitivity.}
71	McCoy et al.\ \citeyear{mccoy2020berts} show that BERT fine-tuning produces seed-dependent generalization failures.
72	Mosbach et al.\ \citeyear{mosbach2021few} identify instability in few-shot fine-tuning regimes.
73	D'Amour et al.\ \citeyear{damour2022underspecification} characterize underspecification---multiple models with identical training loss but divergent test behavior---as a fundamental property of modern ML pipelines.
74	Our observation that error injection amplifies cross-seed variance while preserving training loss stability is consistent with this underspecification phenomenon.
75	
76	\paragraph{Adversarial training and curriculum learning.}
77	Adversarial training \cite{madry2018towards} improves robustness by exposing models to worst-case perturbations, but typically assumes perturbations are observable and gradients are available.
78	Curriculum learning \cite{bengio2009curriculum} orders training examples by difficulty.
79	Error injection can be viewed as a form of curriculum that introduces difficult examples, but our results suggest this curriculum is counterproductive when errors are not observable to the agent.
80	
81	% ============================================================
82	\section{Method}
83	\label{sec:method}
84	
85	\subsection{Error Taxonomy for Embodied Planning}
86	
87	We design a 4-operator error taxonomy targeting two levels of embodied planning:
88	
89	\paragraph{Planning-level operators.}
90	\textbf{P1} (\textsc{StepOrderSwap}): permutes action ordering within a trajectory.
91	\textbf{P2} (\textsc{SubGoalDeletion}): removes sub-goal steps, creating incomplete plans.
92	
93	\paragraph{Context-level operators.}
94	\textbf{C1} (\textsc{ContextTruncation}): truncates environmental context observations.
95	\textbf{C4} (\textsc{ObservationMasking}): masks observation feedback from the environment.
96	
97	These operators span a locality gradient: C4 produces local, observable perturbations (a single masked observation), while P2 produces global, cascading perturbations (a deleted sub-goal invalidates all downstream steps).
98	
99	\subsection{Data Generation}
100	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "976be0fb-e2bb-45a7-b34d-670f98c52100",
  "isSidechain": true,
  "promptId": "c9510963-8cc8-47e6-89fa-87e64c7bc4cb",
  "agentId": "a6eb88c450ef5806d",
  "type": "user",
  "uuid": "3fc73f8d-985c-45f8-85fb-c707543b8e75",
  "sourceToolAssistantUUID": "976be0fb-e2bb-45a7-b34d-670f98c52100",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 46 · 2026-05-16T16:11:56.462Z_

Now let me also check the decisions.yaml for completeness.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3fc73f8d-985c-45f8-85fb-c707543b8e75",
  "isSidechain": true,
  "agentId": "a6eb88c450ef5806d",
  "requestId": "req_011Cb6YNFc36D4jwd5ekssRr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e4ec3adc-757c-4539-9d54-2feed0bd4c5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J9Erzy3vv15GnrRgX14MT4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2545,
      "cache_read_input_tokens": 52283,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2545,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-16T16:11:57.008Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01SKfkUv6GpPee8opWA1GvmL`</summary>

```json
{
  "project": "tax_error_inject_agent",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4ec3adc-757c-4539-9d54-2feed0bd4c5a",
  "isSidechain": true,
  "agentId": "a6eb88c450ef5806d",
  "requestId": "req_011Cb6YNFc36D4jwd5ekssRr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d7fcdddb-8a13-416b-ba6c-3e3cb0caf583",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J9Erzy3vv15GnrRgX14MT4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2545,
      "cache_read_input_tokens": 52283,
      "output_tokens": 122,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2545
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 122,
          "cache_read_input_tokens": 52283,
          "cache_creation_input_tokens": 2545,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2545,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-16T16:11:57.022Z_

<details><summary>↩ Tool result · `toolu_01SKfkUv6GpPee8opWA1GvmL`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/decisions.yaml\", \"content\": \"_next_id: 48\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 09:50 UTC\\n  summary: MVP 增加 random injection baseline，验证 taxonomy guidance 的增量价值\\n  rationale: 'Reviewer critical: 如果没有 random injection baseline，无法区分\\\"taxonomy-guided\\n    injection 有效\\\"还是\\\"任意 perturbation 都有效\\\"。这是 A 类会议 reviewer 的 #1 攻击点。Random injection\\n    = 不按 taxonomy 分类，随机删除/交换步骤，用相同 teacher 生成 recovery。MVP 的 claim 从 \\\"TaxEI > vanilla\\n    SFT\\\" 升级为 \\\"TaxEI > random injection > vanilla SFT\\\"。'\\n  related_experiments:\\n  - exp_id: vanilla-react-baseline\\n    role: existing baseline\\n    result: 42.6%\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 09:55 UTC\\n  summary: '修正 MVP Pass/Fail #3: 拆分为 TaxEI>vanilla 和 TaxEI>random 两个独立 gate，random\\n    vs vanilla 降级为分析维度'\\n  rationale: 'Reviewer warning: 原标准要求 random ≥ vanilla+5pp，如果 TaxEI 显著优于两个 baseline\\n    但 random 效果有限，原标准会判 MVP 失败——假阴性。random 弱于 vanilla 的结果（TaxEI > vanilla > random）同样支持核心\\n    claim：taxonomy guidance 是关键，随机 perturbation 不够。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 10:17 UTC\\n  summary: MVP 阶段选择 Option B（修正声明），不 over-claim environment-grounded；Option A（真实重执行）列为\\n    research 阶段增强\\n  rationale: Reviewer 发现 inject_and_generate.py 使用原始轨迹的 observation 而非重执行后的环境反馈，\\\"environment-grounded\\\"\\n    声明与代码不符。Option A（重执行）更科学但增加 MVP 复杂度——注入后环境可能处于不可能状态（如 P2 删了 pick，后续 put 全部失败），recovery\\n    prompt 的信息量不确定。Option B（修正声明）诚实且 MVP 可快速推进。当前实现的准确描述是\\\"recovery conditioned on\\n    corrupted action history + original observation at injection point\\\"。research 阶段可将\\n    Option A 作为增强实验验证 grounded feedback 是否进一步提升 recovery quality。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D004\\n  date: 2026-05-14 10:41 UTC\\n  summary: 'D004: RandomInjector 重新设计——使用与 TaxEI 完全相同的 4 个算子，去除 taxonomy 标签作为唯一变量'\\n  rationale: Reviewer 指出当前 RandomInjector 的 6 个 perturbation 中 4 个与 TaxEI 算子功能高度重叠，且\\n    plan_injections() 对两组都用 uniform 分配。当前设计比较的是\\\"算子设计质量\\\"而非\\\"taxonomy guidance\\\"。修正方案：RandomInjector\\n    使用与 TaxEI 完全相同的 4 个算子（P1/P2/C1/C4），相同注入数量和位置分布，唯一区别是训练数据中不包含 taxonomy 错误类型标签。这样\\n    Gate 3b 干净地测试\\\"taxonomy 结构化信息是否为训练信号增加了价值\\\"。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n  - D002\\n- id: D005\\n  date: 2026-05-14 11:31 UTC\\n  summary: v3 继续跑但不作 Gate 判定依据；追加 v4 同源双格式化实验（同一份 760 条注入数据格式化两次，TaxEI=Random=9,029，唯一变量=error\\n    tag）\\n  rationale: 'Reviewer critical: v3 数据量不平衡（random 9076 > taxei 7545 > vanilla 4176），Gate\\n    3a/3b 有数据量混淆因素。v3 保留用于验证格式修复（vanilla 是否从 14.9% 恢复）。v4 采用同源双格式化方案：同一份 injected_variants.jsonl\\n    格式化两次（mode=taxei / mode=random），消除注入点、恢复内容、数据量所有混淆。Gate 3a 的数据量差异是方法本质属性，通过 random\\n    vs vanilla 分析维度分离数据量效应。'\\n  related_experiments:\\n  - exp_id: mini-vanilla-sft-v3\\n    role: format verification\\n  - exp_id: mini-taxei-sft-v3\\n    role: preliminary signal\\n  - exp_id: mini-random-sft-v3\\n    role: preliminary signal\\n  depends_on:\\n  - D004\\n  - D002\\n- id: D006\\n  date: 2026-05-14 12:45 UTC\\n  summary: D005 修正：v4 采用同源双格式化方案（非 subsample）——同一份 760 条注入数据格式化两次，TaxEI/Random 各 9,029\\n    samples，唯一变量是 error tag 文本\\n  rationale: 原 D005 描述为 subsample random injected 到 3,369，但 Agent 提出更优方案：同源双格式化消除注入点、恢复内容、数据量所有混淆变量，仅保留\\n    taxonomy tag 作为唯一自变量。已批准并实现。Reviewer 审查确认数据正确。\\n  related_experiments:\\n  - exp_id: mini-vanilla-sft-v4\\n    role: v4 vanilla baseline\\n  - exp_id: mini-taxei-sft-v4\\n    role: v4 taxei (planned)\\n  - exp_id: mini-random-sft-v4\\n    role: v4 random (planned)\\n  depends_on:\\n  - D005\\n  - D004\\n- id: D007\\n  date: 2026-05-14 14:49 UTC\\n  summary: 新颖性自查：PALADIN(2025.09)是最大威胁——同为 taxonomy-guided error injection + recovery\\n    SFT。v3 vanilla>taxei>random 的 negative finding 可能是差异化切入点，等 v4 确认后决定 framing pivot\\n  rationale: 'Manager 要求新颖性自查。发现 PALADIN、STeP、Agent-R、AgentRefine 四篇 2025 年高相关工作。PALADIN\\n    核心方法与 TaxEI 高度重合（taxonomy-guided injection + SFT），差异仅为 error scope（tool-use vs\\n    planning/context）和 domain（ToolBench vs ALFWorld）。但 v3 结果 vanilla>taxei>random\\n    与 PALADIN 正面结果形成反差——error injection 在 embodied planning 上有害。这个 negative finding\\n    可能是更有价值的科学贡献（analytical paper: when does error injection help vs hurt）。需 v4 确认后决定是否\\n    pivot framing。'\\n  related_experiments:\\n  - exp_id: mini-vanilla-sft-v3\\n    role: 74.5% — best performer\\n  - exp_id: mini-taxei-sft-v3\\n    role: 66.0% — injection hurts\\n  - exp_id: mini-random-sft-v3\\n    role: 51.1% — random injection hurts more\\n  depends_on:\\n  - D005\\n- id: D008\\n  date: 2026-05-14 17:33 UTC\\n  summary: v4 Gate 判定：Gate 3a FAIL（TaxEI=Vanilla 61.7%），Gate 3b FAIL（Random 66.0%\\n    反超 TaxEI 61.7%）。MVP 未通过，核心假设被否定。待排查 v4 数据/标签实现后做方向决策。\\n  rationale: v4 同源数据实验（taxei=random=9,029 samples，唯一变量=error tag）结果明确：taxonomy-guided\\n    injection 在 ALFWorld 上无额外价值。TaxEI 与 vanilla 完全持平，random 反超 TaxEI 4.3pp（虽无统计显著性）。v3\\n    的 vanilla>taxei>random 排序被证明由数据量不平衡驱动。v4 vanilla 比 v3 低 12.8pp 原因未明，需排查。结果可靠性确认后决定\\n    pivot/negative paper/终止。\\n  related_experiments:\\n  - exp_id: mini-vanilla-sft-v4\\n    role: baseline\\n    result: 61.7%\\n  - exp_id: mini-taxei-sft-v4\\n    role: treatment\\n    result: 61.7%\\n  - exp_id: mini-random-sft-v4\\n    role: control\\n    result: 66.0%\\n  depends_on:\\n  - D005\\n  - D006\\n  - D007\\n- id: D009\\n  date: 2026-05-14 17:34 UTC\\n  summary: '选 Option C: Recovery-Specific Evaluation + 多种子验证。Clean-task eval 是错误的评估维度，taxonomy\\n    标签价值应在 recovery 场景体现。不终止项目。'\\n  rationale: v4 Gate 3a/3b FAIL 但评估仅覆盖 clean tasks（--no_inject）。Taxonomy 标签标注的是错误类型，其价值应体现在遇到同类错误时的\\n    recovery 能力，而非 clean-task generalization。Injected eval 是逻辑上正确的评估维度。同时 v3→v4 vanilla\\n    波动 12.8pp 需多种子验证排除噪声。这不是 pivot 而是修正评估方法。\\n  related_experiments:\\n  - exp_id: mini-taxei-sft-v4\\n    role: 61.7% on clean eval\\n  - exp_id: mini-random-sft-v4\\n    role: 66.0% on clean eval\\n  depends_on:\\n  - D008\\n- id: D010\\n  date: 2026-05-14 17:37 UTC\\n  summary: 修正 D009：D008 FAIL 不可撤回。Recovery eval 是补充分析（非替代原 Gate）。执行顺序：多种子先行 → recovery\\n    eval 预注册标准后再跑。终止条件：recovery eval 若 taxei≤random 则转 negative paper。\\n  rationale: 'Reviewer warning: D009 有 goalpost-moving 风险。修正：(1) D008 clean-eval Gate\\n    3a/3b FAIL 是最终判定，不可撤回；(2) recovery eval 定位为补充分析，测试\\\"taxonomy 在 recovery 场景是否有价值\\\"，不替代原\\n    Gate；(3) 多种子验证优先（seed=0/42/123 vanilla SFT，确认 v3→v4 波动是否噪声）；(4) recovery eval\\n    PASS 标准预注册：TaxEI overall recovery rate > Random, Fisher exact p<0.10；(5) 终止条件：recovery\\n    eval 若 taxei ≤ random → 转 negative result 分析论文，不再追加实验。'\\n  related_experiments:\\n  - exp_id: mini-vanilla-sft-v4\\n    role: 需多种子验证 61.7% 稳定性\\n  depends_on:\\n  - D009\\n  - D008\\n- id: D011\\n  date: 2026-05-14 18:03 UTC\\n  summary: D010 补充：Recovery eval 统计检验由 Fisher exact 改为 McNemar（配对检验更适合同 task 跨模型对比）。PASS\\n    标准不变：TaxEI recovery rate > Random, p<0.10。\\n  rationale: injected_eval.py 实现使用 McNemar test 而非 D010 预注册的 Fisher exact。McNemar\\n    对配对二分类数据（同一 task 上两个模型的成功/失败）更合适，是正确的技术选择。在执行前记录此修正，避免 post-hoc 检验选择质疑。\\n  related_experiments: []\\n  depends_on:\\n  - D010\\n- id: D012\\n  date: 2026-05-14 20:43 UTC\\n  summary: D010 Phase 1 多种子验证结论：注入训练系统性损害 clean performance，TaxEI 均值 54.3% 远低于 vanilla\\n    65.3%，Gate 3a 彻底 FAIL\\n  rationale: 多种子 clean eval 结果明确：(1) Vanilla 3-seed 均值 65.3%±3.2pp（61.7/68.1/66.0），稳定；(2)\\n    TaxEI 2-seed 均值 54.3%（61.7/46.8），极差 14.9pp，训练不稳定且系统性低于 vanilla 11pp；(3) Random\\n    2-seed 均值 60.7%（66.0/55.3），也低于 vanilla 4.6pp。D008 的 TaxEI=Vanilla=61.7% 是巧合（vanilla\\n    最差种子 vs TaxEI 最好种子）。注入训练（无论是否有 taxonomy 标签）不仅无额外价值，反而损害 clean task 能力并增大训练方差。Recovery\\n    eval (D010 Phase 2) 是最后的验证维度——如果 TaxEI recovery ≤ random recovery，按 D010 规则转 negative\\n    paper。\\n  related_experiments:\\n  - exp_id: v4-vanilla-seed0-eval\\n    role: vanilla seed=0\\n    result: 68.1%\\n  - exp_id: v4-vanilla-seed123-eval\\n    role: vanilla seed=123\\n    result: 66.0%\\n  - exp_id: v4-taxei-seed0-eval\\n    role: taxei seed=0\\n    result: 46.8%\\n  - exp_id: v4-random-seed0-eval\\n    role: random seed=0\\n    result: 55.3%\\n  depends_on:\\n  - D008\\n  - D010\\n- id: D013\\n  date: 2026-05-14 21:00 UTC\\n  summary: D010 Phase 2 recovery eval 确认 TaxEI 无价值：recovery 59.6% < vanilla 61.7%,\\n    detection 0%。终止条件触发，等 random recovery eval 补齐后正式转 negative paper\\n  rationale: TaxEI recovery eval 全部 47 tasks 完成：recovery 28/47 (59.6%) 低于 vanilla\\n    29/47 (61.7%)，detection 0/47 与 vanilla 完全相同。Taxonomy 标签在 recovery 维度也无任何可观测效果。综合所有证据：clean\\n    eval 多种子均值 TaxEI 54.3% << vanilla 65.3%，recovery eval TaxEI < vanilla，detection\\n    为零，训练稳定性 TaxEI 方差 2.3 倍于 vanilla。核心假设\\\"taxonomy-guided error injection 提供额外恢复训练信号\\\"在所有可测量维度被否定。D010\\n    终止条件\\\"recovery eval taxei ≤ random → negative paper\\\"基本触发（TaxEI 已 ≤ vanilla，random\\n    recovery eval 待补齐）。项目转 negative result 分析论文方向。\\n  related_experiments:\\n  - exp_id: v4-taxei-recovery-eval\\n    role: D010 Phase 2 treatment\\n    result: recovery 59.6%, detection 0%\\n  - exp_id: v4-vanilla-recovery-eval\\n    role: D010 Phase 2 baseline\\n    result: recovery 61.7%, detection 0%\\n  depends_on:\\n  - D010\\n  - D011\\n  - D012\\n- id: D014\\n  date: 2026-05-14 21:23 UTC\\n  summary: D010 终止条件正式触发：TaxEI recovery ≤ Random，项目转 negative result paper。全 6 维度\\n    FAIL，核心假设被否定。\\n  rationale: 'Random recovery eval 完成（29/47=61.7%），TaxEI recovery (28/47=59.6%) ≤\\n    Random (61.7%)，D010 预注册终止条件触发。全维度汇总：(1) Gate 3a clean multi-seed TaxEI 54.3% <<\\n    Vanilla 65.3%；(2) Gate 3b TaxEI 54.3% < Random 60.7%；(3) Recovery TaxEI 59.6%\\n    < Random 61.7% = Vanilla 61.7%；(4) Detection 全部 0%；(5) 训练稳定性 TaxEI 方差最大。Taxonomy-guided\\n    error injection 在 ALFWorld embodied planning 上无正面效果，且注入训练系统性损害 clean performance。项目转\\n    negative result 分析论文方向——核心 angle: \\\"When does error injection help vs hurt\\\"，对标\\n    PALADIN 在 tool-use 上的正面结果，探讨 error injection 在 embodied planning vs tool-use 的效果差异。'\\n  related_experiments:\\n  - exp_id: v4-random-recovery-eval\\n    role: D010 Phase 2 control\\n    result: recovery 61.7%, detection 0%\\n  - exp_id: v4-taxei-recovery-eval\\n    role: D010 Phase 2 treatment\\n    result: recovery 59.6%, detection 0%\\n  - exp_id: v4-vanilla-recovery-eval\\n    role: D010 Phase 2 baseline\\n    result: recovery 61.7%, detection 0%\\n  depends_on:\\n  - D010\\n  - D012\\n  - D013\\n- id: D015\\n  date: 2026-05-14 23:57 UTC\\n  summary: D012 修正：3-seed TaxEI 均值 56.7%（非 54.3%），p>0.3 不显著。叙事从\\\"injection hurts\\\"调整为\\\"injection\\n    dramatically increases variance with no reliable benefit\\\"\\n  rationale: TaxEI seed=123 eval = 61.7%，与 seed=42 完全一致（29/47）。3-seed 均值 56.7%±8.6pp\\n    vs Vanilla 65.3%±3.3pp，差值 -8.6pp 但 paired t p≈0.32 不显著。\\\"TaxEI hurts\\\" 结论完全由 seed=0\\n    (46.8%) 单独驱动，另两个 seed 与 vanilla 持平。更准确的叙事：error injection 不是稳定地损害性能，而是剧烈增大训练方差（SD\\n    8.6pp vs 3.3pp, 2.6x），使结果极不可靠。这是更 nuanced 的 negative result——injection 的问题不是系统性有害，而是引入了不可控的训练不稳定性。Claim\\n    1 从 \\\"statistically significantly degrades\\\" 修正为 \\\"introduces high variance with\\n    no reliable directional benefit, failing to meet the +5pp gate\\\"。\\n  related_experiments:\\n  - exp_id: v4-taxei-seed123-eval\\n    role: 3rd seed completes TaxEI multi-seed\\n    result: 61.7% (29/47)\\n  depends_on:\\n  - D012\\n  - D014\\n- id: D016\\n  date: 2026-05-15 00:48 UTC\\n  summary: D015 再修正：pooled permutation test 修复后 TaxEI vs Vanilla p=0.054 (NS)，所有统计比较均不显著。论文\\n    narrative 确认为\\\"方差效应 + 阈值效应\\\"而非\\\"显著退化\\\"。\\n  rationale: multiseed_stats.py 有浮点精度 bug（mean(a)-mean(b) vs mean(a-b) 在 n=47 边界情况产生\\n    ~1e-17 误差导致 p=0）。修复后：TaxEI vs Vanilla pooled p=0.054 (NS)，TaxEI vs Random pooled\\n    p=0.170 (NS)。即使统计功效更高的 pooled test (n=141) 也无法确认显著差异。论文主线确认为：(1) 方差梯度 Vanilla(3.3)&lt;Random(7.0)&lt;TaxEI(8.6)，(2)\\n    dose-response 非线性阈值 10%→0pp, 25%→-12.8pp，(3) 所有均值比较 NS。\\n  related_experiments:\\n  - exp_id: v4-taxei-seed123-eval\\n    role: 3-seed completion\\n    result: 61.7%\\n  - exp_id: v4-random-seed123-eval\\n    role: 3-seed completion\\n    result: 68.1%\\n  - exp_id: v4-taxei-fixed-inject10-eval\\n    role: dose-response\\n    result: 61.7% (0pp)\\n  - exp_id: v4-taxei-fixed-inject25-eval\\n    role: dose-response\\n    result: 48.9% (-12.8pp)\\n  depends_on:\\n  - D015\\n  - D014\\n- id: D017\\n  date: 2026-05-15 01:59 UTC\\n  summary: D016 扩展：完整 dose-response 揭示两个可分离效应——(1) 注入剂量阈值（10%→25% 双方均掉 12.8pp，共享机制）；(2)\\n    taxonomy 标签恒定惩罚（~6.4pp，跨所有 dose 点）。论文 narrative 升级为\\\"可分离双效应模型\\\"。\\n  rationale: Random dose-response 完成：10%=68.1%(+6.4pp), 25%=55.3%(-6.4pp), 50%=57.4%(-4.3pp\\n    vs vanilla)。TaxEI vs Random 差距在三个 dose 点几乎恒定（6.4/6.4/6.3pp），暗示 taxonomy 标签引入的惩罚与注入比例无关——是叠加在注入剂量效应之上的独立系统性偏差。两种方法从\\n    10%→25% 的跌幅相同（12.8pp），确认阈值效应是注入通用的数据稀释机制，非 TaxEI 特有。\\n  related_experiments:\\n  - exp_id: v4-random-fixed-inject10-eval\\n    role: Random dose 10%\\n    result: 68.1%\\n  - exp_id: v4-random-fixed-inject25-eval\\n    role: Random dose 25%\\n    result: 55.3%\\n  - exp_id: v4-random-fixed-inject50-eval\\n    role: Random dose 50%\\n    result: 57.4%\\n  - exp_id: v4-taxei-fixed-inject10-eval\\n    role: TaxEI dose 10%\\n    result: 61.7%\\n  - exp_id: v4-taxei-fixed-inject25-eval\\n    role: TaxEI dose 25%\\n    result: 48.9%\\n  - exp_id: v4-taxei-fixed-inject50-eval\\n    role: TaxEI dose 50%\\n    result: 51.1%\\n  depends_on:\\n  - D016\\n  - D015\\n- id: D018\\n  date: 2026-05-15 03:17 UTC\\n  summary: Dream 审稿分析完成：proceed with writing, 6 项确认行动已派发\\n  rationale: 'Dream dream_20260515T020837 三档评分: Best 2/5（artifact: dream 自行捏造实验导致\\n    data integrity 扣分）, Median 3/5 (Borderline Accept), Worst 2.5/5 (Borderline Revise)。评分异常\\n    best < worst，因 best-case dream paper 编造了 WebShop/scale ablation 等实验被 reviewer\\n    查出。\\n\\n\\n    跨档一致的结构性问题（confirmed actions）：\\n\\n    1. Related work 从 ~8 扩充到 15-20 篇（Reflexion, McCoy, Mosbach, Madry, Bengio, D''Amour,\\n    ReAct）\\n\\n    2. PALADIN recovery-pairing confound 作为替代解释 [M][W]\\n\\n    3. F-test p=0.038 突出 + Levene''s test 补充 [B][M]\\n\\n    4. 论文 4 页结构：正文聚焦 main results + per-operator gradient + error echo\\n\\n    5. 自我矛盾（3 seeds vs ≥5 recommendation）显著承认 [M][W]\\n\\n    6. 数据量不对称 Vanilla 4K vs injection 9K 在 limitations 承认 [W]\\n\\n\\n    观察项（等真实审稿验证）：novelty thin [W only], EEF 2×2 framework [M only], qualitative sample\\n    size [W only]\\n\\n\\n    判断：proceed with writing。median 3/5 达标（borderline），结构性问题已全部转为 Paper Agent action\\n    items。不 re-dream（best 低分是 dream artifact，非 framing 问题）。'\\n  related_experiments: []\\n  depends_on:\\n  - D017\\n- id: D019\\n  date: 2026-05-15 03:20 UTC\\n  summary: Levene's test 确认方差梯度 NS：Claim 3 从 \\\"statistically credible\\\" 降级为 \\\"directional\\n    observation\\\"\\n  rationale: F-test p=0.038 有 distributional assumption 问题（n=3, 非正态）。更 robust 的 Levene's\\n    test p=0.085, Brown-Forsythe p=0.842, bootstrap 69%。所有形式检验 NS。论文 narrative 调整：不再\\n    claim \\\"F-test p=0.038 是最强统计结果\\\"，改为 \\\"observed directional pattern, underpowered\\n    at n=3\\\"。这强化了 negative result story——所有效应均 indistinguishable from noise。\\n  related_experiments: []\\n  depends_on:\\n  - D018\\n- id: D020\\n  date: 2026-05-15 03:22 UTC\\n  summary: F-test p=0.038 确认为计算错误，正确值 p=0.252。所有方差检验 NS。\\n  rationale: Reviewer 手算验证：F(2,2) CDF 公式 P(F>x)=1/(1+x)，代入 F=6.95 得 one-tailed p=0.126,\\n    two-tailed p=0.252。p=0.038 来源不明，可能是 dream imagined_experiments 的估算值误传。已清理 paper_framing.md、ROADMAP.md、writing_plan.yaml\\n    中全部 p=0.038 引用。decisions.yaml 和 dream artifacts 作为历史记录保留不改。Paper Agent 已收到 URGENT\\n    修正通知。\\n  related_experiments: []\\n  depends_on:\\n  - D019\\n- id: D021\\n  date: 2026-05-15 03:29 UTC\\n  summary: Per-operator delta 3/4 错误：从 \\\"smooth monotonic gradient\\\" 修正为 \\\"binary local/global\\n    split\\\"\\n  rationale: Reviewer 从 autodl-5090 实际 eval JSON 验证，gen_fig2.py 硬编码的 delta 值与实际不符。正确值：C4(+9.1),\\n    P1(0.0), C1(-8.3), P2(-8.3)。原先声称的 C4(+6.1)→P2(-8.4) 单调梯度不成立——P1 实际为 0.0 打断单调性，C1=P2=-8.3\\n    说明 global 算子劣势相同。新叙事：binary local/global split，仍有意义但弱于 smooth gradient。paper_framing.md\\n    和 writing_plan.yaml 已更新。\\n  related_experiments:\\n  - exp_id: v4-taxei-recovery-eval-r2\\n    role: per-operator source\\n    result: C1=66.7%, C4=63.6%, P1=58.3%, P2=50.0%\\n  - exp_id: v4-vanilla-recovery-eval\\n    role: per-operator baseline\\n    result: C4=54.5%, P1=58.3%, C1=75.0%, P2=58.3%\\n  depends_on:\\n  - D020\\n- id: D022\\n  date: 2026-05-15 07:31 UTC\\n  summary: 审稿报告 Action Matrix 定稿：补多 seed dose-response + claims 重构 + 3 个 Reviewer\\n    遗漏修正\\n  rationale: Review Director Round 1 评分 Weak Reject (2.75/5)。识别 2 个系统性问题：(A) Claims\\n    overclaiming — 三个 boundary conditions 中只有 dose-response threshold 有合理支撑，但它也是单\\n    seed；(B) Underpowered design — n=3 主实验 + 单 seed 消融。Research Reviewer 独立审视确认方案方向正确，但指出：(1)\\n    dose-response threshold 如不补多 seed 也应降级；(2) 遗漏 v3→v4 不一致、Reflexion 引用、\\\"conservative\\n    estimate\\\" 措辞问题。决定补多 seed dose-response (seeds 0+123, TaxEI/Random × 25%/50%, 8\\n    runs, ~4h GPU)，同时 Paper Agent 执行全部 framing 修改。\\n  related_experiments:\\n  - exp_id: v4-taxei-fixed-inject25-eval\\n    role: baseline\\n    result: 48.9% (seed=42 only)\\n  - exp_id: v4-random-fixed-inject25-eval\\n    role: baseline\\n    result: 55.3% (seed=42 only)\\n  depends_on:\\n  - D018\\n  - D021\\n- id: D023\\n  date: 2026-05-15 11:01 UTC\\n  summary: D022 多 seed 完整数据颠覆 dose-response 叙事：从 threshold-plateau 改为 dual regime\\n    (deterministic harm at 25% + training lottery at 50%)\\n  rationale: 8 组多 seed dose-response 完成。关键发现：(1) TaxEI 25% 一致退化 47.5±1.2pp (confirmed);\\n    (2) TaxEI 50% 方差爆炸 56.0±12.4pp, seed=0=70.2% 超过所有 vanilla; (3) Random 50% s123\\n    也=70.2%, 异常非 taxonomy 特有; (4) \\\"shared 12.8pp\\\" 是 seed-42 巧合; (5) dose-response\\n    非单调 (25% mean < 50% mean); (6) 方差随剂量非线性 (25% SD=1.2 < vanilla 3.3; 50% SD=12.4\\n    >> vanilla). 新叙事：moderate injection = deterministic harm, high injection = training\\n    lottery. \\\"Training lottery\\\" 概念在 error injection 文献中未被报告。\\n  related_experiments:\\n  - exp_id: v4-taxei-fixed-inject25-s0\\n    role: multi-seed\\n    result: 46.8%\\n  - exp_id: v4-taxei-fixed-inject25-s123\\n    role: multi-seed\\n    result: 46.8%\\n  - exp_id: v4-taxei-fixed-inject50-s0\\n    role: multi-seed\\n    result: 70.2%\\n  - exp_id: v4-taxei-fixed-inject50-s123\\n    role: multi-seed\\n    result: 46.8%\\n  - exp_id: v4-random-fixed-inject25-s0\\n    role: multi-seed\\n    result: 61.7%\\n  - exp_id: v4-random-fixed-inject25-s123\\n    role: multi-seed\\n    result: 51.1%\\n  - exp_id: v4-random-fixed-inject50-s0\\n    role: multi-seed\\n    result: 46.8%\\n  - exp_id: v4-random-fixed-inject50-s123\\n    role: multi-seed\\n    result: 70.2%\\n  depends_on:\\n  - D022\\n- id: D024\\n  date: 2026-05-15 11:53 UTC\\n  summary: 'Round 2 审稿 Action Matrix: 3 MF (checklist framing降级+Table 2 Δ修正+页数压缩)\\n    + 补 recovery eval 多 seed + Figure 1 3-seed 更新'\\n  rationale: 'Round 2 Borderline 2.75/5, Round 1 的 13/16 issues resolved. 剩余 3 MF\\n    均为低成本文本修改: (1) Conclusion checklist 从 \\\"boundary conditions\\\" 降级为 \\\"hypothesized\\n    conditions\\\", criterion (3) 改为 \\\"diagnostic feedback\\\" 解决与 Limitations 矛盾; (2) Table\\n    2 Δ列 10% 行改为 \\\"—\\\" 避免混合 baseline 误导; (3) Limitations 独立+§3.6 移 Appendix 压页数. 补跑\\n    recovery eval seeds 0+123 (~1h, GPU 空闲), Figure 1 更新为 3-seed 散点图. Reviewer 判断修改后可达\\n    Weak Accept.'\\n  related_experiments: []\\n  depends_on:\\n  - D023\\n- id: D025\\n  date: 2026-05-15 12:51 UTC\\n  summary: '用户指令: 从 workshop 短文 (4p) 转为长文 (8p)，不再考虑 short paper'\\n  rationale: 用户认为 4 页太短。转长文需要补充实验（recovery-paired injection、第二环境）和深度分析。目标 venue 待定（EMNLP\\n    2026 主会/Findings）。核心机会：recovery-paired injection 可以把论文从 \\\"报告失败\\\" 升级为 \\\"诊断失败原因\\\"。\\n  related_experiments: []\\n  depends_on:\\n  - D024\\n- id: D026\\n  date: 2026-05-15 13:41 UTC\\n  summary: Qualitative failure analysis 发现 TaxEI loop_repetition 2.2× 高于 Vanilla (49\\n    vs 22)，taxonomy 标签导致模型学到 fixation 模式\\n  rationale: Wave 1 任务 3 完成。TaxEI 失败模式中 loop_repetition 显著高于 Vanilla/Random，表明 taxonomy\\n    标签不是简单增加噪声，而是导致模型学到错误的\\\"修复\\\"行为并陷入重复循环。这直接回答了 \\\"noise vs wrong learning\\\" 的问题——答案是\\n    wrong learning (fixation)。此发现将成为 long paper qualitative analysis section 的核心内容。注意：当前\\n    Random 只有 seed=42 的 recovery eval 数据，5-seed 完成后需补齐以确认对比。\\n  related_experiments:\\n  - exp_id: qualitative-failure-analysis\\n    role: primary\\n    result: TaxEI loop_repetition=49, Vanilla=22, Random=6\\n  depends_on:\\n  - D025\\n- id: D027\\n  date: 2026-05-15 13:42 UTC\\n  summary: 'Training dynamics: 训练 loss 跨 seed 极稳定(SD=0.0004)但 eval 方差 2.6×——injection\\n    危害在表征层非训练层。批准 post-hoc forward pass 获取 per-sample loss。'\\n  rationale: TaxEI final loss 0.1738 (token_acc 0.914) vs Vanilla 0.2942 (0.900)——训练指标更好但\\n    eval 更差，确认 training-eval paradox。关键发现：训练过程本身极其稳定（loss SD=0.0004 across seeds），eval\\n    的高方差完全来自学到的表征在不同 task 上的表现差异。这比\\\"增加训练不稳定性\\\"更有解释力，将细化 Claim 3 叙事。方案 A (post-hoc forward\\n    pass) 无需 re-train，几分钟完成。\\n  related_experiments:\\n  - exp_id: training-dynamics\\n    role: primary\\n    result: training loss stable SD=0.0004, TaxEI loss 0.1738 vs Vanilla 0.2942\\n  depends_on:\\n  - D025\\n  - D026\\n- id: D028\\n  date: 2026-05-15 15:41 UTC\\n  summary: 批准 Claim 3 从 \\\"training instability\\\" 改为 \\\"generalization instability\\\" + story\\n    arc 升级为因果链叙事\\n  rationale: D027 证伪\\\"训练不稳定\\\"假说：训练 loss 跨 seed SD=0.0004 极度稳定，不稳定发生在 eval/generalization\\n    层。D026 提供行为层 mechanistic 解释（loop_repetition 2.2×）。两个发现形成因果链：训练稳定地学到 fixation pattern\\n    (D027) → eval 表现为 loop repetition (D026)。Story arc 从\\\"描述 negative result\\\"升级为\\\"解释\\n    WHY negative\\\"——这是更深刻、更有投稿竞争力的论点。Claim 3 旧措辞（error injection increases training\\n    instability）与数据矛盾，必须改。\\n  related_experiments:\\n  - exp_id: training-dynamics\\n    role: evidence\\n    result: training loss SD=0.0004 across seeds\\n  - exp_id: qualitative-failure-analysis\\n    role: evidence\\n    result: TaxEI loop_repetition=49, 2.2x Vanilla\\n  depends_on:\\n  - D026\\n  - D027\\n- id: D029\\n  date: 2026-05-15 16:38 UTC\\n  summary: Forward pass 揭示注入样本被深度记忆(injected loss < clean loss)且 dose-response 单调递增，per-operator\\n    记忆深度与 recovery 损害反相关\\n  rationale: '5 个关键发现：(1) 所有注入模型 injected loss < clean loss，模型确实学到了注入内容但方向错误；(2) gap\\n    从 -0.016(10%) → -0.127(25%) → -0.197(50%)，注入比例越高记忆差距越大；(3) Clean loss 从 Vanilla\\n    0.685 → 50% 0.852，高注入破坏 clean 拟合；(4) Per-operator: C1 loss 最低(0.593)=recovery\\n    退化最大(-8.3pp)，C4 loss 最高(0.630)=recovery 唯一正向(+9.1pp)——记忆越深损害越大；(5) 完整因果链：overfit\\n    injection → behavioral fixation (D026 loop) → generalization collapse (D028)。这些数据直接填充\\n    §4.5 Training Dynamics Analysis，是长文核心 mechanistic evidence。'\\n  related_experiments:\\n  - exp_id: v4-training-dynamics-forward\\n    role: primary\\n    result: 'per-sample loss: injected < clean for all injection models, dose-response\\n      gap monotonic'\\n  depends_on:\\n  - D027\\n  - D028\\n- id: D030\\n  date: 2026-05-15 16:52 UTC\\n  summary: 5-seed Vanilla-TaxEI 差异达 p=0.039 (uncorrected)，Bonferroni 校正后仍 NS (p>0.017)。Claim\\n    1 \\\"NS\\\" 表述需条件化。\\n  rationale: TaxEI seed1 eval = 59.6%。5-seed 完整：Vanilla 67.3±4.7 vs TaxEI 58.3±6.5,\\n    gap=9.0pp, Welch t=2.506, p≈0.039, Cohen's d=1.59。Bonferroni 校正 (3 comparisons,\\n    α=0.0167) 后 NS。效应主要由 seed0 outlier (46.8%) 驱动——去掉 seed0 后 gap 缩至 6.1pp。论文表述更新：不能简单说\\n    \\\"no significant differences\\\"，改为 \\\"marginal significance uncorrected (p=0.039),\\n    NS after Bonferroni correction (p>0.017)\\\"。这实际上加强了 negative result thesis——TaxEI\\n    不仅没帮助，而且有边际显著的损害，但结论需受限于 seed variance 异质性。\\n  related_experiments:\\n  - exp_id: multiseed-taxei\\n    role: primary\\n    result: '5-seed: 58.3±6.5%, p=0.039 uncorrected vs Vanilla'\\n  depends_on:\\n  - D028\\n- id: D031\\n  date: 2026-05-15 17:31 UTC\\n  summary: Random seed1=46.8% 灾难性 outlier 改变 variance gradient：Random SD(9.9%) > TaxEI\\n    SD(6.5%) > Vanilla SD(4.7%)。等 seed7 确认后更新叙事。\\n  rationale: 'Random 4-seed (缺seed7): 66.0/55.3/68.1/46.8, mean=59.1±9.9pp。原叙事\\\"Vanilla\\n    < Random < TaxEI\\\"(更结构化=更不稳定)被5-seed数据推翻——Random SD(9.9%) > TaxEI SD(6.5%)。两种注入都产生~47%灾难性outlier(TaxEI\\n    s0=46.8%, Random s1=46.8%)，Vanilla从未低于61.7%。新叙事方向：(1)注入本身是variance放大器，非taxonomy特异；(2)taxonomy可能有微弱稳定效果(降低SD)；(3)Claim\\n    2 \\\"taxonomy specifically harms\\\"需nuance。等Random seed7确认后统一更新paper_framing.md。'\\n  related_experiments:\\n  - exp_id: multiseed-random\\n    role: primary\\n    result: Random seed1=46.8% (22/47), 4-seed mean=59.1±9.9%\\n  depends_on:\\n  - D030\\n- id: D032\\n  date: 2026-05-15 17:43 UTC\\n  summary: 5-seed 完整统计：TaxEI=Random=58.3% 均值完全一致，taxonomy 标签零收益。Variance gradient\\n    Vanilla(4.7)&lt;TaxEI(6.5)&lt;Random(8.7)。大效应量(d>1.2)但 Bonferroni 后 NS。\\n  rationale: '完整 5-seed 3-way 数据颠覆多个旧叙事：(1) TaxEI=Random=137/235=58.3% 完全一致——taxonomy\\n    在均值层面零收益，这是最强的负面发现；(2) Variance gradient 从 3-seed 的 Vanilla&lt;Random&lt;TaxEI 变为 5-seed\\n    的 Vanilla(4.7)&lt;TaxEI(6.5)&lt;Random(8.7)——taxonomy 可能有微弱稳定效果，与旧 Claim 3 矛盾；(3) 灾难性\\n    outlier: TaxEI s0=46.8%, Random s1=46.8%, Vanilla 最低 61.7%——注入引入随机脆弱性；(4) Welch\\n    t Vanilla-TaxEI p=0.039 uncorrected, Cohen''s d=1.58, Bonferroni NS——underpowered\\n    的大效应量。论文需重写 Claims 1-3 和 Finding section。'\\n  related_experiments:\\n  - exp_id: multiseed-vanilla\\n    role: baseline\\n    result: '5-seed: 67.3±4.7%'\\n  - exp_id: multiseed-taxei\\n    role: primary\\n    result: '5-seed: 58.3±6.5%'\\n  - exp_id: multiseed-random\\n    role: control\\n    result: '5-seed: 58.3±8.7%'\\n  depends_on:\\n  - D030\\n  - D031\\n- id: D033\\n  date: 2026-05-15 18:40 UTC\\n  summary: 'Forward pass v2 修正: dose-response 非单调, Random 记忆深度 2.1× TaxEI, 因果叙事降级为相关性'\\n  rationale: 'v1 的 turn-level 分类 bug 导致 monotonic dose-response 假象。v2 trajectory-level\\n    修正后: (1) gap 在 25%/50% 缩小 3-6× 且非单调(25% > 50%); (2) Random gap -0.078 vs TaxEI\\n    -0.037, 无 taxonomy 标签反而被更深记忆; (3) per-operator 排序不稳定, 弱化 \\\"记忆越深损害越大\\\" 因果链为 correlation。但核心\\n    finding 不变: 所有注入样本被更深记忆(gap<0), 50% clean loss 退化 +0.166。Random 更深记忆但 eval=TaxEI\\n    进一步支持 taxonomy 标签零收益结论。'\\n  related_experiments:\\n  - exp_id: v4-training-dynamics-forward-v2\\n    role: primary\\n    result: non-monotonic dose-response, random 2.1× deeper memorization\\n  - exp_id: v4-training-dynamics-forward\\n    role: superseded\\n    result: v1 had turn-level classification bug\\n  depends_on:\\n  - D029\\n  - D028\\n- id: D034\\n  date: 2026-05-15 22:14 UTC\\n  summary: D017 \\\"10% = 零危害\\\" 叙事被 5-seed 推翻，dose-response 从 threshold 改为 monotonic-then-reversal\\n  rationale: '5-seed 10% 数据: TaxEI 61.3%±8.2 vs Vanilla 67.3%±4.7 = -6.0pp (d=0.90\\n    大效应), Random 63.8%±5.4 = -3.4pp (d=0.67 中效应)。原 D017 单 seed \\\"10%=vanilla\\\" 是巧合。正确叙事:\\n    10% 已有损害→25% 加剧(TaxEI 47.5%)→50% 反弹(56.0%)。不存在 safe threshold。方差结构也与剂量交互: 10%\\n    TaxEI SD>Random, full TaxEI SD<Random，否定简单 \\\"taxonomy 稳定方差\\\" 叙事。'\\n  related_experiments:\\n  - exp_id: dose-response-5seed\\n    role: primary\\n    result: 10% TaxEI 61.3±8.2, Random 63.8±5.4\\n  - exp_id: dose-response-taxei\\n    role: context\\n    result: 25% 47.5±1.2, 50% 56.0±12.4\\n  depends_on:\\n  - D023\\n  - D032\\n- id: D035\\n  date: 2026-05-15 23:57 UTC\\n  summary: D023 \\\"dual regime (deterministic 25% + lottery 50%)\\\" 被 5-seed 推翻，改为 \\\"continuous\\n    dose-dependent harm + universal lottery\\\"\\n  rationale: '25% 5-seed: TaxEI 52.7±7.6 (3-seed 47.5±1.2, SD×6.3 倍), Random 60.0±8.0。3-seed\\n    的极低方差是抽样巧合(s42/s0/s123 恰好落在 46-49%)，s1=63.8/s7=57.4 大幅高于。所有剂量均为 lottery(SD 5-12%)，不存在\\n    regime boundary。正确叙事: injection at all doses increases variance + reduces mean,\\n    25% TaxEI 显示最大 taxonomy penalty (7.3pp vs Random)。'\\n  related_experiments:\\n  - exp_id: dose-response-5seed\\n    role: primary\\n    result: 25% TaxEI 52.7±7.6, Random 60.0±8.0\\n  - exp_id: dose-response-taxei\\n    role: superseded\\n    result: 3-seed 47.5±1.2 was sampling coincidence\\n  depends_on:\\n  - D034\\n  - D023\\n- id: D036\\n  date: 2026-05-16 00:00 UTC\\n  summary: 25% TaxEI vs Random 显著(p=0.029)但 Bonferroni NS；维持 negative result framing，加\\n    dose-dependent taxonomy penalty 作为 secondary finding\\n  rationale: '25% 统计: Vanilla vs TaxEI p=0.004 d=2.63 (Bonferroni survives), Vanilla\\n    vs Random p=0.039, TaxEI vs Random p=0.029 d=1.49 (Bonferroni NS at α=0.017)。TaxEI\\n    dose-response 斜率是 Random 2×(0.58 vs 0.29 pp/%)。这不是 taxonomy \\\"works\\\"，是 taxonomy\\n    amplifies harm。决定: 维持 negative result paper framing，加 \\\"taxonomy labels amplify\\n    dose-dependent harm\\\" 作为 nuanced secondary finding。等 50% 5-seed 确认是否斜率差持续。不翻转论文方向。'\\n  related_experiments:\\n  - exp_id: dose-response-5seed\\n    role: primary\\n    result: 25% TaxEI vs Random p=0.029 d=1.49, TaxEI slope 2× Random\\n  depends_on:\\n  - D035\\n- id: D037\\n  date: 2026-05-16 00:14 UTC\\n  summary: 'D037: 修正 per-seed 数据污染——Vanilla s1/s7 和 TaxEI s1/s7 被 25% dose-response\\n    值覆盖'\\n  rationale: Reviewer critical 发现 ROADMAP 和 experiment_plan.yaml 的 5-seed 主表 per-seed\\n    值被 25% dose-response 实验结果污染。验算确认：错误值算出 SD 与报告不符（Vanilla 3.85≠4.7, TaxEI 6.83≠6.5），修正值算出正确\\n    SD（4.67≈4.7, 6.49≈6.5）。修正：Vanilla s1 72.3→66.0, s7 68.1→74.5; TaxEI s1 63.8→59.6,\\n    s7 57.4→61.7。Mean±SD 不变，但 per-seed 分析和 outlier 识别受影响。paper_framing.md 主条件不含逐 seed\\n    值，无需修正。\\n  related_experiments:\\n  - exp_id: 5-seed-extension\\n    role: affected\\n    result: per-seed values corrected in ROADMAP + experiment_plan.yaml\\n  depends_on:\\n  - D032\\n- id: D038\\n  date: 2026-05-16 01:37 UTC\\n  summary: 'D038: 50% dose-response 5-seed 完成，dose-response 全线收官。Inverted-U taxonomy\\n    penalty: 25% peak (-7.3pp) → 50% (-0.9pp) → Full (0pp)'\\n  rationale: '50% s1/s7 eval 完成。TaxEI 50% 5-seed: 57.4±9.5 (51.1/70.2/46.8/63.8/55.3)，Random\\n    50%: 58.3±11.7 (57.4/46.8/70.2/70.2/46.8)。TaxEI-Random gap 从 3-seed 的 -2.1pp 收窄到\\n    -0.9pp。完整 dose-response 曲线确认 inverted-U taxonomy penalty (25% peak)。所有 5 个剂量 ×\\n    5 seeds 全部到位，dose-response 实验线关闭。下一步：recovery-paired SFT (Wave 2 核心实验)。'\\n  related_experiments:\\n  - exp_id: dose-response-5seed\\n    role: completed\\n    result: all 5 doses × 5 seeds complete, inverted-U taxonomy penalty confirmed\\n  depends_on:\\n  - D036\\n- id: D039\\n  date: 2026-05-16 02:21 UTC\\n  summary: 'D039: Recovery-paired SFT 启动 (Claim 7)。数据设计: TaxEI 9,029 + Recovery 5,408\\n    = 14,437。4 seeds 并行 (42/0/123/1)。'\\n  rationale: 'Recovery-paired 是 Wave 2 核心实验，测试 PALADIN recovery-pairing 是否是 TaxEI\\n    失败的缺失成分。数据设计: recovery continuations 叠加在 TaxEI 基础上（不替换），recovery_only 模式提取恢复步骤。14,437\\n    vs TaxEI 9,029 存在 volume confound，但预期 negative result 下不成问题；意外成功则后补 volume-matched\\n    control。4 seeds 并行 ~4h/seed。50% 统计确认 dose-response 趋同: TaxEI≈Random at 50% (Δ=0.8pp,\\n    p=0.920)。Random dose-response 单调递减显著 (Spearman p=0.037)。'\\n  related_experiments:\\n  - exp_id: recovery-paired-injection\\n    role: started\\n    result: 4 seeds training on 4 GPUs, ETA ~4h\\n  - exp_id: dose-response-5seed\\n    role: analysis\\n    result: '50% stats complete: TaxEI≈Random, Bonferroni NS vs Vanilla'\\n  depends_on:\\n  - D038\\n- id: D040\\n  date: 2026-05-16 03:09 UTC\\n  summary: 'D040: WebShop replication 降级为 Discussion section 分析。Drop Claim 8。P1 无法适配\\n    WebShop 线性 action space，taxonomy 4→3 使跨环境对比不等价。35 GPU-h 转用于 recovery eval multi-seed\\n    + TaxEI-RP seed 7。'\\n  rationale: Agent 调研发现 P1_StepOrderSwap 在 WebShop 产生语法非法序列（action space 只有 search+click，高度线性）。Taxonomy\\n    缩减 4→3 使\\\"跨环境复制\\\"变成\\\"不同 taxonomy 的不同实验\\\"，给 reviewer 留把柄。12-17 天工期 + 35 GPU-h (64%\\n    剩余预算) ROI 太低。改为 Discussion 段落分析 ALFWorld vs WebShop 结构性差异，论证跨环境迁移的非平凡性。省下的 GPU-h\\n    用于 recovery eval multi-seed (Claims 4/5) 和 TaxEI-RP seed 7 (Claim 7)。\\n  related_experiments:\\n  - exp_id: webshop-replication\\n    role: cancelled\\n    result: downgraded to Discussion analysis due to P1 incompatibility\\n  depends_on:\\n  - D039\\n- id: D041\\n  date: 2026-05-16 03:22 UTC\\n  summary: 'D041: Recovery rate ≈ normal eval rate — 模型是 \\\"resilience\\\"(被动忽略错误) 而非 \\\"recovery\\\"(主动恢复)。Claim\\n    4/5 叙事需要修正。'\\n  rationale: 'Reviewer 审计发现 4 个未注册 recovery eval 的 recovery rate 与 normal eval rate\\n    精确一致（V s0: 68.1%=68.1%, V s123: 66.0%=66.0%, T s0: 46.8%=46.8%, T s123: 61.7%=61.7%）。唯一例外是\\n    TaxEI s42 (59.6% vs 61.7%, -2.1pp)。这意味着 eval-time 注入对模型性能几乎零影响——模型既不检测也不受影响。\\\"Recovery\\\"\\n    实际是 \\\"resilience\\\"（被动忽略），不是主动从错误中恢复。Claim 4 从\\\"不改善 recovery\\\"修正为\\\"eval-time errors\\n    被忽略，recovery=resilience\\\"。Claim 5 (detection=0%) 不变。这进一步强化 negative result：error\\n    injection 在 embodied planning 中不仅训练无效，连 eval-time 错误信号也被忽略。'\\n  related_experiments:\\n  - exp_id: recovery-eval\\n    role: reinterpreted\\n    result: 'recovery≈normal: passive resilience, not active recovery'\\n  - exp_id: recovery-eval-multiseed\\n    role: context\\n    result: 7/15 confirmed, 4 unregistered being fixed\\n  depends_on:\\n  - D039\\n- id: D042\\n  date: 2026-05-16 04:49 UTC\\n  summary: 'D042: Scope 扩展——加 LLaMA-3.1-8B 跨模型验证 + scale-up 25K trajectories。用户指示\\\"尽量补实验\\\"。'\\n  rationale: 当前 scope (1 model × 1 env) 对 8 页长文偏窄。核心 claim \\\"task structure 是主因\\\" 但只有单模型证据。加第二模型\\n    (LLaMA-3.1-8B) 是性价比最高的扩展——同样数据同样流程，如果也是 negative result 则论证力翻倍。Scale-up 堵住 \\\"PALADIN\\n    50K vs TaxEI 9K\\\" 的数据量质疑。\\n  related_experiments:\\n  - exp_id: llama-cross-model\\n    role: new experiment\\n    result: planned\\n  - exp_id: scale-up-data\\n    role: new experiment\\n    result: planned\\n  depends_on:\\n  - D025\\n  - D032\\n- id: D043\\n  date: 2026-05-16 06:32 UTC\\n  summary: 'D043: TaxEI-RP (recovery-paired) 4-seed 结果: 47.9±7.8%, 比 TaxEI 差 10pp,\\n    比 Vanilla 差 19pp。Recovery pairing 不是 PALADIN 成功的关键要素，task structure 确认为根本限制。Claim\\n    7 定论。'\\n  rationale: 'TaxEI-RP mean 47.9% (s42=38.3/s0=46.8/s1=48.9/s123=57.4) vs TaxEI 58.3%\\n    vs Vanilla 67.3%。Recovery continuation 训练数据 (+5,408 samples) 不仅未改善 recovery，反而进一步恶化性能。这排除了\\\"PALADIN\\n    成功是因为 recovery pairing\\\"的替代解释，确认 task structure (error observability, local recoverability,\\n    bounded action space) 是 error injection 成败的主要因素。Detection rate 仍为 0%。论文 Reviewer\\n    Concern #8 现在有直接实验证据回应。'\\n  related_experiments:\\n  - exp_id: recovery-paired-injection\\n    role: primary\\n    result: 47.9±7.8% (4-seed), worse than TaxEI and Vanilla\\n  - exp_id: multiseed-taxei\\n    role: comparison\\n    result: 58.3±6.5%\\n  - exp_id: multiseed-vanilla\\n    role: comparison\\n    result: 67.3±4.7%\\n  depends_on:\\n  - D039\\n  - D041\\n- id: D044\\n  date: 2026-05-16 06:32 UTC\\n  summary: 'D044: Scale-up 数据收集暂停——成功率从 70% 崩到 9.3%，1000 目标不可行。需诊断原因后决定是否重试或放弃。'\\n  rationale: Phase 1 收集 810 次尝试仅 76 成功 (9.3%)，远低于历史 70.2%。按此速率，3000 次尝试只能得 ~280 条，不满足\\n    1000 目标。可能原因：排除已用 714 easy games 后剩余 pool 系统性更难；API/seed 差异；代码 bug。已花 ~$10 API\\n    成本。Kill 进程后诊断。\\n  related_experiments:\\n  - exp_id: scale-up-data\\n    role: primary\\n    result: 76/810 success (9.3%), paused\\n  depends_on:\\n  - D042\\n- id: D045\\n  date: 2026-05-16 07:18 UTC\\n  summary: 'D045: Scope 最终判断——当前 scope 含 LLaMA 3-seed + recovery eval 补完即可支撑 EMNLP\\n    Findings long paper。LLaMA 从 1-seed 扩到 3-seed (s42/s0/s123)，recovery eval 补完 8/15，scale-up\\n    诊断但不阻塞论文。'\\n  rationale: 8 页长文负面结果论文需要：(1) 跨模型验证排除 model-specific artifact — LLaMA 3-seed V/T/R\\n    提供统计可靠的第二数据点；(2) 完整 recovery eval 支撑 Claims 4/5 的多 seed 结论；(3) TaxEI-RP (D043)\\n    已排除最大替代解释。单环境是残留风险但工程上无法解决（WebShop D040 已证明）。Scale-up 9.3% 成功率需诊断——如果是 bug 则修复重跑，如果是\\n    pool 难度则本身是有价值的数据点。EEF 正向对照和第二环境放弃——ROI 不足。\\n  related_experiments:\\n  - exp_id: llama-cross-model\\n    role: scope expansion\\n    result: s42 training in progress, extend to 3-seed\\n  - exp_id: recovery-eval-multiseed\\n    role: completion required\\n    result: 7/15 done, 8 remaining\\n  - exp_id: scale-up-data\\n    role: diagnose\\n    result: paused at 9.3% success rate\\n  depends_on:\\n  - D042\\n  - D043\\n  - D044\\n- id: D046\\n  date: 2026-05-16 07:24 UTC\\n  summary: 'D046: 撤销 D044 scale-up 暂停——9.3% 成功率是统计口径错误（714 exclusion stubs 被计为失败），真实成功率\\n    77.9%。重启收集。'\\n  rationale: Reviewer 诊断确认：818 条记录中 714 是 phase 0 去重标记（task_type=exclude），实际 API 尝试仅\\n    104 条，成功 81 条 = 77.9%。进程仅跑 51 分钟就被误杀。按 127.5 条/小时吞吐，再跑 ~4h 可收集 500 条。Scale-up\\n    完全可行，重启收集。\\n  related_experiments:\\n  - exp_id: scale-up-data\\n    role: primary\\n    result: actual success rate 77.9%, restart collection\\n  depends_on:\\n  - D044\\n- id: D047\\n  date: 2026-05-16 15:50 UTC\\n  summary: LLaMA 3-seed 完成：TaxEI 跨模型不稳定确认，paper framing 升级为\\\"结构化注入训练不稳定性\\\"\\n  rationale: LLaMA 3-seed 数据齐全。TaxEI recovery SD=8.6% vs Random SD=2.1%，1/3 seed (s123)\\n    触发 catastrophic degradation (59.6% vs vanilla 70.2%)。\\\"LLaMA 中性\\\"假说不成立。新 framing：结构化错误注入跨模型导致训练不稳定，Random\\n    注入跨模型稳定。新增 Claim 9。\\n  related_experiments:\\n  - exp_id: llama31-vanilla-s123\\n    role: baseline\\n    result: clean=72.3%, recovery=70.2%\\n  - exp_id: llama31-taxei-s123\\n    role: treatment\\n    result: clean=61.7%, recovery=59.6% — catastrophic\\n  - exp_id: llama31-random-s123\\n    role: control\\n    result: clean=76.6%, recovery=78.7% — stable\\n  depends_on:\\n  - D045\\n\", \"total_chars\": 34886, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d7fcdddb-8a13-416b-ba6c-3e3cb0caf583",
  "isSidechain": true,
  "promptId": "c9510963-8cc8-47e6-89fa-87e64c7bc4cb",
  "agentId": "a6eb88c450ef5806d",
  "type": "user",
  "uuid": "c4a6b981-555f-413f-ac90-06904c0574b2",
  "sourceToolAssistantUUID": "d7fcdddb-8a13-416b-ba6c-3e3cb0caf583",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-16T16:12:03.511Z_

I now have a comprehensive understanding of the full experimental scope, the paper drafts (both the older LaTeX short paper and the expanded long paper framing), the literature map, and the full decision history. Let me now produce the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4a6b981-555f-413f-ac90-06904c0574b2",
  "isSidechain": true,
  "agentId": "a6eb88c450ef5806d",
  "requestId": "req_011Cb6YNa7GbMqcYzGrptD28",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d2ea666a-4629-426c-ad65-361102fba359",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01713RvbzRQPEmykfoWFW6Ch",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19225,
      "cache_read_input_tokens": 54828,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19225,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-16T16:12:04.113Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01GTgp6KB66TGVRaRvDMhb8y`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__submit_dream_review_report",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2ea666a-4629-426c-ad65-361102fba359",
  "isSidechain": true,
  "agentId": "a6eb88c450ef5806d",
  "requestId": "req_011Cb6YNa7GbMqcYzGrptD28",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c925db8c-3ec6-430a-bd0d-1008a03d28b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01713RvbzRQPEmykfoWFW6Ch",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19225,
      "cache_read_input_tokens": 54828,
      "output_tokens": 139,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 19225
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 139,
          "cache_read_input_tokens": 54828,
          "cache_creation_input_tokens": 19225,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 19225,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-16T16:12:04.115Z_

<details><summary>↩ Tool result · `toolu_01GTgp6KB66TGVRaRvDMhb8y`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__submit_dream_review_report"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c925db8c-3ec6-430a-bd0d-1008a03d28b4",
  "isSidechain": true,
  "promptId": "c9510963-8cc8-47e6-89fa-87e64c7bc4cb",
  "agentId": "a6eb88c450ef5806d",
  "type": "user",
  "uuid": "36fb4b6f-8743-4825-bfcc-6a78c3de65c4",
  "sourceToolAssistantUUID": "c925db8c-3ec6-430a-bd0d-1008a03d28b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 52 · 2026-05-16T16:13:48.328Z_



Now I have everything I need. Let me synthesize the review based on my thorough reading of all project materials.

### R2 Review: Novelty and Related Work

**Summary**: This paper tests whether taxonomy-guided error injection (successful for tool-use agents via PALADIN) transfers to embodied planning on ALFWorld. Across extensive experiments on Qwen3-8B (5 seeds) and LLaMA-3.1-8B (3 seeds), the authors find that structured injection degrades performance by ~9pp, taxonomy labels provide zero benefit over random injection, and models exhibit passive resilience rather than active recovery (0% detection rate). The paper attempts to upgrade from a negative result to a positive characterization of when error injection helps vs. harms, proposing task-structural boundary conditions (error observability, locality, recoverability).

**Strengths**:
- S1: The experimental thoroughness is genuinely impressive for a negative-result paper. The 5-seed main experiment, complete 5-dose x 5-seed dose-response ablation (25 training runs for dose-response alone), cross-model replication on LLaMA, and recovery-paired injection ablation (directly testing the PALADIN confound) represent a level of rigor that exceeds most positive-result papers. The TaxEI = Random = 58.3% identity is a striking and clean finding.
- S2: The recovery-paired injection experiment (Claim 7: TaxEI-RP at 47.9%, worse than unpaired TaxEI at 58.3%) is the paper's strongest methodological contribution. It definitively rules out the most parsimonious alternative explanation (that PALADIN succeeds because of recovery pairing, not task structure) and would not be obvious to predict a priori.
- S3: The resilience-vs-recovery distinction (D041: recovery rates track clean evaluation rates with r=0.96, detection rate = 0%) is a genuinely useful conceptual contribution. This reframes what "recovery" means in agent evaluation and has implications beyond this specific paper.
- S4: The inverted-U dose-response curve for the taxonomy penalty (peaking at 25%, vanishing at full dose) is a non-trivial empirical finding that resists simple narrative explanations and suggests real underlying structure in how structured vs. random noise interacts with training dynamics.
- S5: Honest and transparent statistical reporting throughout. The authors do not overclaim: they report Bonferroni-corrected NS results, power analyses showing 45% power at n=5, bootstrap CIs, and explicitly note when findings are exploratory. This is commendable.

**Weaknesses**:
- W1: **The title claim "fundamentally destabilizing" is not supported by the evidence.** "Fundamentally" implies a deep, necessary property demonstrated with generality. The paper tests one benchmark (ALFWorld, 47 test tasks) with two models (Qwen3-8B, LLaMA-3.1-8B), both 8B-scale, both using the same LoRA recipe, the same data, and the same 4-operator taxonomy. The word "fundamentally" requires either formal analysis (showing WHY structured patterns must destabilize) or breadth of empirical coverage (multiple environments, scales, training recipes). The paper has neither. "Fundamentally" should be replaced with "empirically" or removed entirely.

- W2: **The generalization from ALFWorld to "embodied planning" is a significant overreach.** ALFWorld is a text-based interface to a simulated household environment with 47 test tasks across 6 task types. It is one specific instantiation of embodied planning with particular properties (text-only observations, limited action space, sparse reward). The paper's structural analysis (Table 10) hypothesizes that error observability, locality, and recoverability are the key factors, but these are not empirically validated -- they are post-hoc rationalizations of a single-benchmark result. Other embodied planning environments (e.g., VirtualHome, Habitat, BEHAVIOR) have different error structures. The paper should consistently say "ALFWorld" rather than "embodied planning" when describing empirical findings, reserving "embodied planning" for the hypothesized (not demonstrated) generalization.

- W3: **The task-structural comparison (Table 10 / structural hypothesis) is hand-wavy and unfalsifiable in its current form.** The five dimensions (error signal, observability, recovery scope, feedback, error locality) are chosen post-hoc to explain the observed negative result. No dimension is independently operationalized or tested. For example, "error observability" is claimed to differ between tool-use and embodied planning, but the paper does not measure or manipulate observability. A stronger paper would test at least one dimension in isolation (e.g., adding explicit error signals to ALFWorld observations to test the observability hypothesis). Without such tests, the structural comparison is a plausible story, not a scientific finding.

- W4: **The cross-model "validation" on LLaMA is weak and potentially misleading.** With only 3 seeds, the entire "cross-model instability" narrative rests on a single catastrophic seed (s123: 59.6% recovery vs. 74.5% for the other two seeds). The paper acknowledges eval-seed confounds (s0/s42 use eval_seed=42; s123 uses eval_seed=123), meaning the catastrophic result could partially reflect eval-seed variance rather than training instability. Furthermore, on LLaMA, Random injection is actually *beneficial* (+3.5pp over Vanilla), which contradicts the Qwen finding where Random also degrades by 9pp. This cross-model inconsistency in the Random condition undermines the "cross-architecture evidence" framing -- the results are more model-specific than the paper acknowledges.

- W5: **Statistical power remains genuinely insufficient for the central claims.** The paper's own power analysis shows 45% power at n=5 for the main comparison (Vanilla vs. TaxEI). This means there is a >50% chance of failing to detect a true effect of this magnitude. The Bonferroni-corrected comparisons are all NS. The authors handle this honestly, but the consequence is that the paper's central empirical claims ("injection degrades by 9pp") cannot be distinguished from noise at conventional significance levels. The large Cohen's d (1.58) is encouraging but is inflated by small n. For a venue paper, this is a substantial limitation.

- W6: **The 4:1 SD ratio claim (TaxEI 8.6pp vs. Random 2.1pp on LLaMA) is based on 3 data points and is not statistically testable.** Variance estimates from n=3 are extremely unreliable. Levene's test, F-test, and bootstrap are all NS even at n=5 for Qwen. Presenting this as a key finding ("establishing training instability as intrinsic to structured patterns") overstates what 3 observations can establish.

- W7: **Only 9 references in the LaTeX draft is far below venue standards.** Even accounting for the expanded literature map in the project files (which lists ~30 relevant papers), the actual paper text cites too few. For EMNLP, 30-50 references is typical for an 8-page paper. Critical gaps are detailed below.

**Questions for Authors**:
- Q1: The LLaMA results show Random injection is mildly *beneficial* (+3.5pp over Vanilla), while on Qwen Random degrades by 9pp. How do you reconcile this cross-model divergence? Does this not undermine the claim that error injection is generically harmful for embodied planning?
- Q2: Have you considered that the 4-operator taxonomy itself may be poorly designed for ALFWorld specifically, rather than error injection being fundamentally incompatible with embodied planning? For instance, AgentDebug proposes a 5-dimensional taxonomy for ALFWorld that includes memory and reflection errors. Would a different taxonomy yield different results?
- Q3: The recovery-paired experiment uses 14,437 samples vs. TaxEI's 9,029 and Vanilla's 4,358. Given that you already observe data volume effects (TaxEI/Random's 9K vs. Vanilla's 4K is acknowledged as a confound), how confident are you that TaxEI-RP's worse performance is due to recovery pairing rather than the further increase in noisy data volume?
- Q4: You report that training loss is extremely stable across seeds (SD=0.0007) while evaluation varies dramatically. Have you examined whether different seeds produce different internal representations (e.g., via CKA similarity or probing)? This would strengthen the "generalization instability" framing.
- Q5: The per-operator analysis (N=11-12 per operator) is acknowledged as exploratory, yet it appears prominently as a key finding (the "local/global split"). Given that a single task flip changes delta by 8-9pp, what is the evidentiary basis for including this as a numbered contribution rather than relegating it to an appendix observation?

**Detailed Assessment**:

**1. Novelty and Significance (High Weight)**

The research question -- does error injection transfer across agent domains? -- is timely and important given the proliferation of error-injection methods. However, the intellectual contribution is thinner than the paper suggests. The core negative finding (TaxEI hurts on ALFWorld) is useful but expected: it would be surprising if a technique designed for tool-use transferred without modification to a structurally different domain. The upgrade from "negative result" to "positive characterization of boundary conditions" is the paper's key bet, but the boundary conditions are hypothesized rather than empirically validated, making this upgrade incomplete.

The strongest novel contributions are: (a) TaxEI = Random = 58.3% (taxonomy labels provide zero value), which is genuinely surprising and informative; (b) recovery-paired injection actively harms (ruling out the PALADIN confound); (c) recovery = resilience (conceptually clarifying). These are real contributions, but they are analytical observations from a single benchmark, not generalizable principles.

For a venue with ~25% acceptance, I would expect either broader empirical coverage (2+ environments) or deeper mechanistic analysis (formal modeling of why structured noise destabilizes) to push this above the bar.

**2. Related Work Completeness (High Weight)**

The related work has significant gaps:

**Missing Related Work**:

*Agent training with failures/errors (critical omissions)*:
- **AgentTuning** (Zeng et al., 2023) -- general-purpose agent instruction tuning including ALFWorld; directly relevant baseline
- **FireAct** (Chen et al., 2023) -- fine-tuning agents with multi-turn trajectories; relevant methodology
- **Agent-FLAN** (Chen et al., 2024) -- agent fine-tuning with negative trajectories included
- **NAT** (Wang et al., 2024, "Learning from Mistakes") -- negative-aware training for agents
- The paper cites ETO and EEF but misses the broader landscape of learning-from-failure methods

*Embodied agent training (critical omissions)*:
- **SayCan** (Ahn et al., 2022) -- grounding language in embodied affordances
- **Inner Monologue** (Huang et al., 2023) -- feedback-driven embodied planning
- **EMMA** (Yang et al., 2024) -- embodied multi-modal agent training
- **SWE-agent** and similar code agents that face similar error-recovery challenges

*Noise injection / data augmentation theory (important context)*:
- **Dropout as data augmentation** (Bouthillier et al., 2016) -- noise injection during training
- **Mixup** (Zhang et al., 2018) -- interpolation-based augmentation
- **Label smoothing** literature -- soft noise injection
- **NoisyStudent** (Xie et al., 2020) -- self-training with noise

*Distribution shift / domain adaptation*:
- **Domain randomization** literature (Tobin et al., 2017) -- noise injection for sim-to-real transfer, directly relevant to the question of when injected noise helps
- The connection between error injection and distribution shift is underexplored

*Curriculum learning beyond Bengio 2009*:
- **Self-paced learning** (Kumar et al., 2010)
- **Competence-based curriculum** (Platanios et al., 2019)
- Modern curriculum learning surveys

The positioning relative to PALADIN is fair in the framing document but the LaTeX draft's related work section is too brief. The paper needs to engage more deeply with why PALADIN's specific design choices (retrieval augmentation, 50K scale, recovery pairing) each contribute to its success.

**3. Framing and Claims (High Weight)**

- "Fundamentally destabilizing" is too strong for one benchmark + two models. Should be "empirically destabilizing on ALFWorld."
- "Cross-architecture evidence" is oversold given n=3 on LLaMA with eval-seed confounds and contradictory Random results.
- The boundary conditions (discrete, observable, locally recoverable) are reasonable hypotheses but are not empirically validated. They should be explicitly framed as hypotheses, not findings.
- The data scale ablation claim ("5x scaling doesn't close the gap: -8.9pp vs -9.0pp") is important but I don't see the full experimental details for this in the LaTeX draft -- it appears only in the dream paper abstract. If this experiment exists, it should be prominently featured.

**4. Contribution Calibration (Medium Weight)**

For EMNLP Findings with ~25% acceptance, this paper is borderline. The experimental rigor is above average, the statistical honesty is commendable, and the recovery-paired ablation is genuinely informative. However, the single-benchmark scope, underpowered statistics, and hypothesized-but-untested boundary conditions weaken the contribution. Successful negative-result papers at top venues typically either (a) falsify a widely held belief with overwhelming evidence (this paper's evidence is suggestive but not overwhelming due to power issues) or (b) provide a clear mechanistic explanation (the structural hypothesis is plausible but unvalidated).

The paper is currently closer to a strong workshop paper or a borderline Findings paper. The recovery-paired result and the resilience-vs-recovery distinction push it toward Findings territory.

**5. Broader Impact and Future Directions (Low Weight)**

The practical implications are reasonable: check error observability, locality, and recoverability before applying error injection. The future work directions (second environment, recovery-paired injection -- already done, scale-up) are appropriate. The paper could better discuss implications for the broader agent-training community, particularly the lesson that training-time data augmentation strategies do not transfer across agent domains without careful analysis of task structure.

**Minor Issues**:
- The LaTeX draft appears to be the older 3-seed short paper version while the paper_framing.md documents the full 8-page scope. The actual submission should reflect the 5-seed, cross-model results.
- Table 1 in the LaTeX draft shows 3-seed results; this needs updating to the 5-seed data.
- The dose-response table in the LaTeX draft is single-seed; the 5-seed dose-response data should replace it.
- "v3 to v4 vanilla discrepancy" (74.5% to 65.3%) needs clearer explanation -- currently it reads as a concerning pipeline instability.
- The detection rate metric was shown to produce false positives on LLaMA (keyword matching "back" in navigation phrases). This should be noted if LLaMA detection rates are reported.

**Overall Score**: 3/6 (Weak Reject)
**Confidence**: 4/5
**Justification**: The paper addresses a relevant question with commendable experimental thoroughness and statistical honesty. However, the central claims outrun the evidence: "fundamentally destabilizing" and "cross-architecture evidence" are not supported by one benchmark with underpowered statistics and a 3-seed cross-model check. The task-structural boundary conditions are plausible hypotheses, not validated findings. The related work is too sparse. For EMNLP Findings, I would want to see either (a) a second environment confirming the pattern, (b) empirical validation of at least one proposed boundary condition, or (c) substantially stronger statistics on the existing experiments. The recovery-paired ablation and resilience-vs-recovery distinction are genuine contributions that prevent a stronger reject.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36fb4b6f-8743-4825-bfcc-6a78c3de65c4",
  "isSidechain": true,
  "agentId": "a6eb88c450ef5806d",
  "requestId": "req_011Cb6YP6bLVqw4Lgmw7E2Gc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ca385d54-b2d7-4fd8-89a3-48735d3e134b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "27e14a3a-a346-45ee-b971-8cd155586b0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AKguksDQPpuoCDVcnJcDg6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 717,
      "cache_read_input_tokens": 74053,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 717,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---
