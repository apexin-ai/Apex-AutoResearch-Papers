# Research conversation: You are Reviewer R2 for a top ML venue peer review. Your focus: **Novelty and Related Work**. Review standard: top ML ve

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 1
- **Tool calls:** 19
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a7fe9f34d2b39e51d.jsonl`
- **Structured JSON:** [`f61767849fc544bbc2ab.json`](../../sessions/f6/f61767849fc544bbc2ab.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

44 recorded events

### User

_source line 1 · 2026-05-16T15:41:57.364Z_

You are Reviewer R2 for a top ML venue peer review. Your focus: **Novelty and Related Work**. Review standard: top ML venue, ~25% acceptance rate, 6-point scale (1=Strong Reject, 6=Strong Accept).

## Paper Summary
Title: "Structured Pruning Breaks RLVR Alignment: A Systematic Empirical Study of Reasoning Model Compression"

The paper studies how structured pruning interacts with GRPO (RLVR) in reasoning LLMs. Two main findings:
1. GRPO reward-accuracy decoupling: reward increases but greedy-decode accuracy stays flat (even on unpruned models)
2. GRPO training collapse on structurally pruned models: output diversity collapses within 4-60 steps

Models: DeepSeek-R1-Distill-Qwen-7B (primary), Qwen2.5-Math-7B (cross-model)
Pruning methods tested: RASP (CKA-aware), Standard importance, Bonsai, GRASPrune + unstructured baseline
Sparsity: 20%, 25%, 30%
The paper also includes a CKA-aware pruning method (RASP) but the paper's own experiments show it provides no significant advantage.

Key results:
- GRPO reward goes from 0 to 0.661 on unpruned model but accuracy stays 81.27% (identical). This is "reward-accuracy decoupling."
- All 4 structured pruning methods show GRPO collapse (frac_zero_std > 0.93 within 4-60 steps)
- Unstructured pruning at same 20% does NOT collapse
- Collapse speed correlates with post-SFT model quality (r≈0.95), not with any specific structural property
- RASP's CKA component adds only 2pp over gradient-only (p=0.41)
- Alpha ablation shows post-prune accuracy anti-correlates with post-SFT accuracy (r=-0.45)
- Cross-model (Qwen2.5-Math-7B) shows near-identical collapse regardless of method at 25%
- OOD benchmarks show severe degradation, SFT recovery is domain-specific
- Inference speedup is only 1.14-1.16x for ~20pp accuracy loss

Related work section covers:
- Structured Pruning of LLMs: LLM-Pruner, SliceGPT, Bonsai, GRASPrune
- RLVR for Reasoning Models: GRPO, Self-Healing, PASER
- Pruning-Recovery Interaction: RESP, MPruner

The paper positions itself as: "first controlled study of prune→SFT→GRPO pipeline for structured pruning of reasoning LLMs."

## Your task
Provide a detailed review focusing on:
1. **Novelty assessment**: Are the contributions genuinely new? How significant are the findings?
2. **Related work coverage**: Are important baselines missing? Is positioning fair?
3. **Contribution framing**: Are claims well-calibrated to the evidence?
4. **Significance and impact**: Would the community benefit from these findings?
5. **Writing quality and clarity**

Output format:
```
## R2 Review: Novelty and Related Work

### Summary
[2-3 sentences]

### Strengths
[Bulleted list, be specific]

### Weaknesses
[Bulleted list, be specific]

### Questions for Authors
[Numbered list]

### Assessment of Novelty
[Detailed paragraph]

### Assessment of Related Work
[Detailed paragraph]

### Minor Issues
[Presentation, writing, etc.]

### Preliminary Score: X/6
### Confidence: X/5
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "39eba513-b35c-4482-87e4-5618fcf0979e",
  "agentId": "a7fe9f34d2b39e51d",
  "type": "user",
  "uuid": "b2b6a1b6-74d2-4755-9c99-3fe3a0f3958b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "87456414-598d-4dd4-8776-aaed1b39d708",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T15:41:57.367Z_

```json
{
  "parentUuid": "b2b6a1b6-74d2-4755-9c99-3fe3a0f3958b",
  "isSidechain": true,
  "agentId": "a7fe9f34d2b39e51d",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__submit_dream_review_report"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
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
  "uuid": "02b3420a-4b45-4680-a094-340c7ab82f68",
  "timestamp": "2026-05-16T15:41:57.367Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "87456414-598d-4dd4-8776-aaed1b39d708",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-16T15:42:00.911Z_



I'll start by reading the paper and related project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02b3420a-4b45-4680-a094-340c7ab82f68",
  "isSidechain": true,
  "agentId": "a7fe9f34d2b39e51d",
  "requestId": "req_011Cb6W5ufYycMHcFMmRLa6o",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1527c61c-3b06-4e38-b51d-a8efe9072cc8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "87456414-598d-4dd4-8776-aaed1b39d708",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Xm12HLU1Hn6sDPyi7DqEC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 6738,
      "cache_read_input_tokens": 8252,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6738,
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

_source line 4 · 2026-05-16T15:42:01.309Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01P7RmqAwZj3DEfzZQ4YNbox`</summary>

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
  "parentUuid": "1527c61c-3b06-4e38-b51d-a8efe9072cc8",
  "isSidechain": true,
  "agentId": "a7fe9f34d2b39e51d",
  "requestId": "req_011Cb6W5ufYycMHcFMmRLa6o",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "23200a32-36bc-45ae-bc4b-e9a0a3902cb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "87456414-598d-4dd4-8776-aaed1b39d708",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Xm12HLU1Hn6sDPyi7DqEC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 6738,
      "cache_read_input_tokens": 8252,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6738,
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

### Tool result

_source line 5 · 2026-05-16T15:42:01.312Z_

<details><summary>↩ Tool result · `toolu_01P7RmqAwZj3DEfzZQ4YNbox`</summary>

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
  "parentUuid": "23200a32-36bc-45ae-bc4b-e9a0a3902cb0",
  "isSidechain": true,
  "promptId": "39eba513-b35c-4482-87e4-5618fcf0979e",
  "agentId": "a7fe9f34d2b39e51d",
  "type": "user",
  "uuid": "b456fba2-8c65-401b-9b68-06a432e13b70",
  "sourceToolAssistantUUID": "23200a32-36bc-45ae-bc4b-e9a0a3902cb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "87456414-598d-4dd4-8776-aaed1b39d708",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-16T15:42:04.697Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01SvYXD2ABpEynQPrpJ67ZbK`</summary>

```json
{
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b456fba2-8c65-401b-9b68-06a432e13b70",
  "isSidechain": true,
  "agentId": "a7fe9f34d2b39e51d",
  "requestId": "req_011Cb6W6D5JwY3w1YkyJUxVi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "37dc291c-884c-4c46-86f1-938b06e65e21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "87456414-598d-4dd4-8776-aaed1b39d708",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H2v886PfQbRA53nNYWMoiR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 14990,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1446,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
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

_source line 7 · 2026-05-16T15:42:04.982Z_

<details><summary>↩ Tool result · `toolu_01SvYXD2ABpEynQPrpJ67ZbK`</summary>

```text
{"result":"# 项目 recovery_aware_struct_prune 概况\n\n## 实验状态 (102 个)\n\n- **grpo_stage2_rasp_20_v2**: DONE (negative) — \n- **grpo_stage2_standard_20**: DONE (killed) — \n- **grpo_stage2_rasp_20**: DONE (killed) — \n- **sft_standard_20**: DONE (success) — \n- **sft_rasp_20**: DONE (success) — \n- **grpo_rasp_20_4096**: DONE (failed) — \n- **grpo_standard_20_4096**: DONE (negative) — \n- **grpo_standard_20_fast**: DONE (negative) — \n- **grpo_rasp_20_fast**: DONE (negative) — \n- **mvp_rasp_pipeline_v4**: PREPARING — \n- **grpo_standard_20**: DONE (killed) — \n- **grpo_rasp_20**: DONE (killed) — \n- **mvp_rasp_pipeline_v3**: DONE (negative) — \n- **mvp_rasp_pipeline_v2**: DONE (failed) — \n- **mvp_rasp_pipeline**: DONE (failed) — \n\n## 最新报告\n&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-16T15:40:33Z; do not edit — regenerated by auto_build_report_facts) -->\n## 📊 当前状态（auto-derived from registry）\n\n**总计**: 102 个实验 — ANALYZING 2, DONE 84, PREPARING 12, RUNNING 4\n**DONE 分布**: failed 12, killed 10, negative 10, success 52\n\n### GPU 占用\n- **分配**: 6 张 — westb-23072:cuda:0, westb-23072:cuda:1, westd-11672:cuda:0, westd-11672:cuda:1, westd-11672:cuda:2, westd-11672:cuda:3\n- **实际运行**: 4 张 — westb-23072:cuda:0(eval_sft_rasp_25), westd-11672:cuda:0(grpo_rasp_qwen_math_v3), westd-11672:cuda:1(grpo_standard_qwen_math_v3), westb-23072:cuda:1(eval_sft_rasp_rlvr_20)\n- **空闲（分配了没跑）**: westd-11672:cuda:2, westd-11672:cuda:3\n\n### 🏃 RUNNING\n| exp_id | server | gpu | pid | log |\n|--------|--------|-----|-----|-----|\n| `eval_sft_rasp_25` | westb-23072 | cuda:0 | 602990 | `~/runs/recovery_aware_struct_prune/eval_sft_rasp_25.log` |\n| `grpo_rasp_qwen_math_v3` | westd-11672 | cuda:0 | 16812 | `…runs/recovery_aware_struct_prune/grpo_rasp_qwen_math_v3.log` |\n| `grpo_standard_qwen_math_v3` | westd-11672 | cuda:1 | 16892 | `…/recovery_aware_struct_prune/grpo_standard_qwen_math_v3.log` |\n| `eval_sft_rasp_rlvr_20` | westb-23072 | cuda:1 | 625453 | `~/runs/recovery_aware_struct_prune/eval_sft_rasp_rlvr_20.log` |\n\n### 📌 最近完成 (top 5)\n- `sft_rasp_rlvr_20` [success] — 2026-05-16T14:50:02 — 磁盘空间不足：训练完成但保存 optimizer state 时 torch.save 失败 (RuntimeError: iostream error)。模型\n- `grpo_standard_qwen_math` [killed] — 2026-05-16T14:27:51\n- `grpo_rasp_qwen_math` [killed] — 2026-05-16T14:27:50\n- `eval_sft_standard_25` [success] — 2026-05-16T13:23:38\n- `eval_sft_qwen_math_standard_25` [success] — 2026-05-16T12:50:43\n\n### 🔴 最近失败原因 (top 3)\n- `grpo_standard_qwen_math`: _(no failure_reason — pre-2026-04-24 entry)_\n- `grpo_rasp_qwen_math`: _(no failure_reason — pre-2026-04-24 entry)_\n\n&lt;!-- AUTO-FACTS-END -->\n\n---\n\n# Handover — 2026-05-16\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| eval_sft_rasp_rlvr_20 | RASP-RLVR 20% post-SFT GSM8K eval (N=1319, greedy, seed=42). 验证反向 CKA scoring 的 RLVR 恢复效果。对比 RASP SFT (61.49%) 和 Standard SFT (59.29%)。Parent: sft_rasp_rlvr_20. | — | — | — |\n| grpo_standard_qwen_math_v3 | Qwen2.5-Math-7B Standard 20% GRPO v3 (100 steps, save_steps=100). 跨模型验证 C2: Standard collapse gradient. 修复 save_steps=5 磁盘膨胀问题。Parent: sft_qwen_math_standard_20. | — | — | — |\n| grpo_rasp_qwen_math_v3 | Qwen2.5-Math-7B RASP 20% GRPO v3 (100 steps, save_steps=100). 跨模型验证 C1/C2. 修复 save_steps=5 磁盘膨胀问题。Parent: sft_qwen_math_rasp_20. | — | — | — |\n\n## 待处理\n- grpo_standard_25: Standard 25% GRPO recovery (100 steps). Negative control for grpo_rasp_25. 预期 collapse 比 RASP 更早/更严重（如 20% 所示）。Parent: sft_standard_25.（准备中）\n- grpo_rasp_25: RASP 25% GRPO recovery (100 steps). 预期 collapse 比 20% 更快更严重。与 grpo_standard_25 对比验证 C3: recovery method conditions pruning order. Parent: sft_rasp_25.（准备中）\n- eval_postprune_25: 25% post-prune accuracy eval (N=100, greedy, seed=42) for both pruned_ras"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "37dc291c-884c-4c46-86f1-938b06e65e21",
  "isSidechain": true,
  "promptId": "39eba513-b35c-4482-87e4-5618fcf0979e",
  "agentId": "a7fe9f34d2b39e51d",
  "type": "user",
  "uuid": "1158de09-5738-4749-b50f-068a512b7831",
  "sourceToolAssistantUUID": "37dc291c-884c-4c46-86f1-938b06e65e21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "87456414-598d-4dd4-8776-aaed1b39d708",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-16T15:42:05.336Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01WdJuoeGNRD3tkyNiPitFGW`</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1158de09-5738-4749-b50f-068a512b7831",
  "isSidechain": true,
  "agentId": "a7fe9f34d2b39e51d",
  "requestId": "req_011Cb6W6D5JwY3w1YkyJUxVi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e7661c9b-c3ec-4aa2-9c29-56d7c7edfd34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "87456414-598d-4dd4-8776-aaed1b39d708",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H2v886PfQbRA53nNYWMoiR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 14990,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1446
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 166,
          "cache_read_input_tokens": 14990,
          "cache_creation_input_tokens": 1446,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1446,
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

_source line 9 · 2026-05-16T15:42:05.347Z_

<details><summary>↩ Tool result · `toolu_01WdJuoeGNRD3tkyNiPitFGW`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-16T15:40:33Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 102 个实验 — ANALYZING 2, DONE 84, PREPARING 12, RUNNING 4\\n**DONE 分布**: failed 12, killed 10, negative 10, success 52\\n\\n### GPU 占用\\n- **分配**: 6 张 — westb-23072:cuda:0, westb-23072:cuda:1, westd-11672:cuda:0, westd-11672:cuda:1, westd-11672:cuda:2, westd-11672:cuda:3\\n- **实际运行**: 4 张 — westb-23072:cuda:0(eval_sft_rasp_25), westd-11672:cuda:0(grpo_rasp_qwen_math_v3), westd-11672:cuda:1(grpo_standard_qwen_math_v3), westb-23072:cuda:1(eval_sft_rasp_rlvr_20)\\n- **空闲（分配了没跑）**: westd-11672:cuda:2, westd-11672:cuda:3\\n\\n### 🏃 RUNNING\\n| exp_id | server | gpu | pid | log |\\n|--------|--------|-----|-----|-----|\\n| `eval_sft_rasp_25` | westb-23072 | cuda:0 | 602990 | `~/runs/recovery_aware_struct_prune/eval_sft_rasp_25.log` |\\n| `grpo_rasp_qwen_math_v3` | westd-11672 | cuda:0 | 16812 | `…runs/recovery_aware_struct_prune/grpo_rasp_qwen_math_v3.log` |\\n| `grpo_standard_qwen_math_v3` | westd-11672 | cuda:1 | 16892 | `…/recovery_aware_struct_prune/grpo_standard_qwen_math_v3.log` |\\n| `eval_sft_rasp_rlvr_20` | westb-23072 | cuda:1 | 625453 | `~/runs/recovery_aware_struct_prune/eval_sft_rasp_rlvr_20.log` |\\n\\n### 📌 最近完成 (top 5)\\n- `sft_rasp_rlvr_20` [success] — 2026-05-16T14:50:02 — 磁盘空间不足：训练完成但保存 optimizer state 时 torch.save 失败 (RuntimeError: iostream error)。模型\\n- `grpo_standard_qwen_math` [killed] — 2026-05-16T14:27:51\\n- `grpo_rasp_qwen_math` [killed] — 2026-05-16T14:27:50\\n- `eval_sft_standard_25` [success] — 2026-05-16T13:23:38\\n- `eval_sft_qwen_math_standard_25` [success] — 2026-05-16T12:50:43\\n\\n### 🔴 最近失败原因 (top 3)\\n- `grpo_standard_qwen_math`: _(no failure_reason — pre-2026-04-24 entry)_\\n- `grpo_rasp_qwen_math`: _(no failure_reason — pre-2026-04-24 entry)_\\n\\n&lt;!-- AUTO-FACTS-END -->\\n\\n---\\n\\n# Handover — 2026-05-16\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| eval_sft_rasp_rlvr_20 | RASP-RLVR 20% post-SFT GSM8K eval (N=1319, greedy, seed=42). 验证反向 CKA scoring 的 RLVR 恢复效果。对比 RASP SFT (61.49%) 和 Standard SFT (59.29%)。Parent: sft_rasp_rlvr_20. | — | — | — |\\n| grpo_standard_qwen_math_v3 | Qwen2.5-Math-7B Standard 20% GRPO v3 (100 steps, save_steps=100). 跨模型验证 C2: Standard collapse gradient. 修复 save_steps=5 磁盘膨胀问题。Parent: sft_qwen_math_standard_20. | — | — | — |\\n| grpo_rasp_qwen_math_v3 | Qwen2.5-Math-7B RASP 20% GRPO v3 (100 steps, save_steps=100). 跨模型验证 C1/C2. 修复 save_steps=5 磁盘膨胀问题。Parent: sft_qwen_math_rasp_20. | — | — | — |\\n\\n## 待处理\\n- grpo_standard_25: Standard 25% GRPO recovery (100 steps). Negative control for grpo_rasp_25. 预期 collapse 比 RASP 更早/更严重（如 20% 所示）。Parent: sft_standard_25.（准备中）\\n- grpo_rasp_25: RASP 25% GRPO recovery (100 steps). 预期 collapse 比 20% 更快更严重。与 grpo_standard_25 对比验证 C3: recovery method conditions pruning order. Parent: sft_rasp_25.（准备中）\\n- eval_postprune_25: 25% post-prune accuracy eval (N=100, greedy, seed=42) for both pruned_rasp_25 and pruned_standard_25. 补之前失败的数据点，对比 20% sparsity post-prune (RASP 31% vs Standard 27%)。（准备中）\\n- eval_sft_standard_20_n1319: Standard post-SFT full GSM8K eval (N=1319, greedy, seed=42). N=100 result: 64%. Full eval provides tight CI for paper Table 1. Parent: sft_standard_20_retrain.（准备中）\\n- eval_sft_grasp_20（准备中）\\n- eval_sft_alpha_0p5: α=0.5 post-SFT GSM8K eval (N=100, greedy). Post-prune 25%. Completes full α ablation: α=0.0 (64%), α=0.5 (?), α=1.0 (57%), α=2.0 (pending), α=4.0 (62%). Parent: alpha_ablation_westd_cal256.（准备中）\\n- eval_sft_rasp_20_full: RASP post-SFT full GSM8K eval (N=1319, greedy, seed=42). N=100 result: 57%. Full eval provides statistical significance for RASP vs Standard comparison. Parent: sft_rasp_20.（准备中）\\n- grpo_standard_20_v8（准备中）\\n- grpo_rasp_20_v8（准备中）\\n- alpha_ablation_westd_cal256: α ablation sweep (calibration=256, N=100). α∈{0.0,0.5,1.0,2.0,4.0} at 20% sparsity. Phase A (prune+eval) complete, Phase B (SFT) in progress. Note: calibration=256 differs from westb original (512), causing ~5% group selection differences.（准备中）\\n- …另有 2 项\\n\\n## 近期结论\\n- **sft_rasp_rlvr_20** (success): RASP-RLVR 20% post-prune SFT recovery (lr=2e-5, epochs=2). 验证反向 CKA scoring (保留冗余结构) 是否产生更好的 RLVR 恢复基础。对比 RASP SFT 和 Standard SFT。Parent: prune_rasp_rlvr_20.\\n- **grpo_standard_qwen_math** (killed): Qwen2.5-Math-7B Standard 20% GRPO (100 steps, save_steps=5). 跨模型验证 C2: Standard collapse gradient (transient dip+recovery). DeepSeek Standard: transient dip step ~60, recovery step ~90. 参数同 grpo_stage2_standard_20_v8。Parent: sft_standard_20_qwen_math.\\n- **grpo_rasp_qwen_math** (killed): Qwen2.5-Math-7B RASP 20% GRPO (100 steps, save_steps=5). 跨模型验证 C1/C2: GRPO collapse 是否在 Qwen Math 上复现。DeepSeek RASP collapse onset ~step 10 (permanent). 参数同 grpo_stage2_rasp_20_v9。Parent: sft_rasp_20_qwen_math.\\n\\n## 趋势\\n成功 52 / 负向 10 / 失败 12 / 共 84\\naccuracy: 0.5125 ↓（近 3 次 success）\\neos_rate: 0.9545 ↓（近 3 次 success）\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestb-23072: 无 GPU 信息\\nwestd-11672: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\\n\\n## 告警\\n- mvp_rasp_pipeline: 训练失败 — unknown\\n- mvp_rasp_pipeline_v2: 训练失败 — unknown\\n- grpo_rasp_20: 已被终止 — unknown\\n- grpo_standard_20: 已被终止 — unknown\\n- grpo_rasp_20_4096: 训练失败 — unknown\\n- grpo_stage2_rasp_20: 已被终止 — unknown\\n- grpo_stage2_standard_20: 已被终止 — unknown\\n- grpo_stage2_standard_20_v2: 训练失败 — unknown\\n- grpo_stage2_rasp_20_v3: 训练失败 — unknown\\n- grpo_stage2_rasp_20_v4: 已被终止 — unknown\\n- grpo_stage2_rasp_20_v5: 已被终止 — unknown\\n- sft_alpha4_0_westd: 训练失败 — unknown\\n- grpo_stage2_rasp_20_v6: 训练失败 — unknown\\n- grpo_stage2_standard_20_v6: 训练失败 — unknown\\n- grpo_stage2_rasp_20_v7: 训练失败 — unknown\\n- grpo_stage2_standard_20_v7: 训练失败 — unknown\\n- eval_sft_standard_20_full: 训练失败 — unknown\\n- grpo_unpruned_baseline: 训练失败 — unknown\\n- eval_sft_rasp_qwen_math: 已被终止 — unknown\\n- eval_sft_standard_qwen_math: 已被终止 — unknown\\n- grpo_rasp_qwen_math: 已被终止 — unknown\\n- grpo_standard_qwen_math: 已被终止 — unknown\\n\", \"total_chars\": 5927, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e7661c9b-c3ec-4aa2-9c29-56d7c7edfd34",
  "isSidechain": true,
  "promptId": "39eba513-b35c-4482-87e4-5618fcf0979e",
  "agentId": "a7fe9f34d2b39e51d",
  "type": "user",
  "uuid": "42c1f6b2-4d27-424b-90cd-9aebf8176fb6",
  "sourceToolAssistantUUID": "e7661c9b-c3ec-4aa2-9c29-56d7c7edfd34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "87456414-598d-4dd4-8776-aaed1b39d708",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-16T15:42:09.813Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01FgmGabeduaTe8mtAgXBkYW`</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42c1f6b2-4d27-424b-90cd-9aebf8176fb6",
  "isSidechain": true,
  "agentId": "a7fe9f34d2b39e51d",
  "requestId": "req_011Cb6W6W3X8G3HJCbskQ29p",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3b2e345e-e63c-448e-8a14-d42d35365b5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "87456414-598d-4dd4-8776-aaed1b39d708",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KDN3AnTz8Xt3GFNH5eUtNZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5459,
      "cache_read_input_tokens": 16436,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5459,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 50,
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

_source line 11 · 2026-05-16T15:42:09.831Z_

<details><summary>↩ Tool result · `toolu_01FgmGabeduaTe8mtAgXBkYW`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'recovery_aware_struct_prune'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b2e345e-e63c-448e-8a14-d42d35365b5a",
  "isSidechain": true,
  "promptId": "39eba513-b35c-4482-87e4-5618fcf0979e",
  "agentId": "a7fe9f34d2b39e51d",
  "type": "user",
  "uuid": "dfeb8d71-24a8-4a06-8a72-8bab7ce1a4bb",
  "sourceToolAssistantUUID": "3b2e345e-e63c-448e-8a14-d42d35365b5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "87456414-598d-4dd4-8776-aaed1b39d708",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-16T15:42:10.690Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_013tkEVCNQX2TvZNFWvMUJcK`</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dfeb8d71-24a8-4a06-8a72-8bab7ce1a4bb",
  "isSidechain": true,
  "agentId": "a7fe9f34d2b39e51d",
  "requestId": "req_011Cb6W6W3X8G3HJCbskQ29p",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "26434036-dcfb-4086-bb85-e4a5bed15aeb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "87456414-598d-4dd4-8776-aaed1b39d708",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KDN3AnTz8Xt3GFNH5eUtNZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5459,
      "cache_read_input_tokens": 16436,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5459,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 50,
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

_source line 13 · 2026-05-16T15:42:10.702Z_

<details><summary>↩ Tool result · `toolu_013tkEVCNQX2TvZNFWvMUJcK`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/literature_map.yaml\", \"content\": \"papers:\\n  # === Direct Competitors ===\\n  - id: self_healing_2025\\n    title: \\\"Self-Healing: Recovering Pruned Large Reasoning Models via Reinforcement Learning\\\"\\n    authors: \\\"Yixin Ji, Zhimin Lin, Juntao Li, Kaixin Wu, Kai Yao, Xu Jia, Linjian Mo, Min Zhang\\\"\\n    year: 2025\\n    venue: \\\"ICLR 2026 submission (OpenReview #12375, submitted Sep 2025)\\\"\\n    category: direct-competitor\\n    role: \\\"RLVR recovery baseline\\\"\\n    relevance: 9\\n    key_finding: \\\"RLVR recovers 95%+ at 25% compression; SFT only reaches ~80%. Tested on 5 LRMs across 6 math benchmarks.\\\"\\n    our_relation: \\\"We extend beyond single sparsity ratio and add CKA-guided pruning selection\\\"\\n    citation_priority: must-cite\\n    arxiv_id: \\\"\\\"\\n\\n  - id: resp_2025\\n    title: \\\"RESP: Self-Reflective Structured Pruning for Reasoning LLMs\\\"\\n    authors: \\\"\\\"\\n    year: 2025\\n    venue: \\\"arXiv Dec 2025\\\"\\n    category: direct-competitor\\n    role: \\\"Structured pruning for reasoning without recovery\\\"\\n    relevance: 8\\n    key_finding: \\\"GSM8K 81.3% at 40% sparsity via self-reflective importance\\\"\\n    our_relation: \\\"No RLVR recovery; we show recovery-aware pruning outperforms at same sparsity\\\"\\n    citation_priority: must-cite\\n    arxiv_id: \\\"2512.02185\\\"\\n\\n  - id: grasprune_2026\\n    title: \\\"GRASPrune: Global Gating-based Structural Pruning for LLMs\\\"\\n    authors: \\\"\\\"\\n    year: 2026\\n    venue: \\\"ACL 2026 Main\\\"\\n    category: direct-competitor\\n    role: \\\"SOTA budgeted structural pruning\\\"\\n    relevance: 8\\n    key_finding: \\\"Global gating achieves best structured pruning under budget constraints\\\"\\n    our_relation: \\\"GRASPrune as pruning backbone; we add CKA overlap + RLVR recovery on top\\\"\\n    citation_priority: must-cite\\n    arxiv_id: \\\"2604.19398\\\"\\n\\n  - id: opsd_2026\\n    title: \\\"OPSD: One-shot Post-RL Structured Distillation\\\"\\n    authors: \\\"\\\"\\n    year: 2026\\n    venue: \\\"arXiv May 2026\\\"\\n    category: direct-competitor\\n    role: \\\"Post-RL compression via distillation\\\"\\n    relevance: 7\\n    key_finding: \\\"Compress post-RL model in one shot via structured distillation\\\"\\n    our_relation: \\\"Distillation-based vs our pruning+recovery approach; complementary\\\"\\n    citation_priority: should-cite\\n    arxiv_id: \\\"\\\"\\n\\n  - id: doing_more_with_less_2026\\n    title: \\\"Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling\\\"\\n    authors: \\\"\\\"\\n    year: 2026\\n    venue: \\\"arXiv Apr 2026\\\"\\n    category: direct-competitor\\n    role: \\\"Pruning improves test-time scaling\\\"\\n    relevance: 7\\n    key_finding: \\\"Unstructured pruning can augment test-time scaling; structured pruning degrades it\\\"\\n    our_relation: \\\"Motivates why structured pruning needs recovery; we address this gap with RLVR\\\"\\n    citation_priority: should-cite\\n    arxiv_id: \\\"2604.25098\\\"\\n\\n  - id: gprune_llm_2026\\n    title: \\\"GPrune-LLM: Generalization-Aware Structured Pruning for Large Language Models\\\"\\n    authors: \\\"\\\"\\n    year: 2026\\n    venue: \\\"arXiv Mar 2026\\\"\\n    category: direct-competitor\\n    role: \\\"Cross-distribution generalization-aware pruning\\\"\\n    relevance: 6\\n    key_finding: \\\"Accounts for neuron cross-distribution behavior; reduces calibration bias\\\"\\n    our_relation: \\\"Complementary importance metric; our CKA captures functional overlap vs their generalization gap\\\"\\n    citation_priority: should-cite\\n    arxiv_id: \\\"2603.13418\\\"\\n\\n  - id: boiling_frog_2026\\n    title: \\\"Gradually Compacting Large Language Models for Reasoning Like a Boiling Frog\\\"\\n    authors: \\\"Yiran Zhao, Shengyang Zhou, Zijian Wu, Tongyan Hu, Yuhui Xu, Rengan Dou, Kenji Kawaguchi, Shafiq Joty, Junnan Li, Michael Qizhe Shieh\\\"\\n    year: 2026\\n    venue: \\\"arXiv Feb 2026\\\"\\n    category: direct-competitor\\n    role: \\\"Iterative prune-tune loop for reasoning model compression\\\"\\n    relevance: 7\\n    key_finding: \\\"Gradual Prune-Tune Loop avoids abrupt performance collapse; iterative pruning+finetuning preserves reasoning\\\"\\n    our_relation: \\\"Similar prune-then-recover paradigm but uses SFT recovery; we use RLVR which is more effective and add CKA-guided pruning selection\\\"\\n    citation_priority: must-cite\\n    arxiv_id: \\\"2602.04919\\\"\\n\\n  - id: think_prune_train_2025\\n    title: \\\"Think, Prune, Train, Improve: Scaling Reasoning without Scaling Models\\\"\\n    authors: \\\"Caia Costello, Simon Guo, Anna Goldie, Azalia Mirhoseini\\\"\\n    year: 2025\\n    venue: \\\"arXiv Apr 2025 (Stanford Scaling Intelligence Lab)\\\"\\n    category: direct-competitor\\n    role: \\\"Self-training on pruned reasoning traces to improve small models\\\"\\n    relevance: 6\\n    key_finding: \\\"Iterative fine-tuning on ground-truth-pruned reasoning traces; Gemma2-9B matches LLaMA-3.1-70B on GSM8K\\\"\\n    our_relation: \\\"Complementary — prunes reasoning traces (CoT) not model weights; could combine with our weight pruning\\\"\\n    citation_priority: nice-to-have\\n    arxiv_id: \\\"2504.18116\\\"\\n\\n  # === Method Components ===\\n  - id: mpruner_2024\\n    title: \\\"MPruner: Optimizing Neural Network Size with CKA-Based Mutual Information Pruning\\\"\\n    authors: \\\"\\\"\\n    year: 2024\\n    venue: \\\"arXiv Aug 2024\\\"\\n    category: method-component\\n    role: \\\"CKA for layer importance estimation\\\"\\n    relevance: 8\\n    key_finding: \\\"CKA similarity between layers identifies redundant layers for removal; 50% parameter reduction with minimal accuracy loss\\\"\\n    our_relation: \\\"We adapt CKA from layer-level to width-level functional overlap prediction\\\"\\n    citation_priority: must-cite\\n    arxiv_id: \\\"2408.13482\\\"\\n\\n  - id: lachance_thesis_2024\\n    title: \\\"Using Centered Kernel Alignment for Understanding and Pruning Neural Networks\\\"\\n    authors: \\\"Lachance\\\"\\n    year: 2024\\n    venue: \\\"URI Master's Thesis\\\"\\n    category: method-component\\n    role: \\\"CKA-based pruning theoretical foundation\\\"\\n    relevance: 6\\n    key_finding: \\\"CKA layer similarity correlates with pruning recoverability\\\"\\n    our_relation: \\\"Validates CKA as signal for pruning decisions; we extend to predict RLVR recovery\\\"\\n    citation_priority: should-cite\\n    arxiv_id: \\\"\\\"\\n\\n  - id: fang_2025\\n    title: \\\"FANG: Improving Generalization in LLM Structured Pruning via Function-Aware Neuron Grouping\\\"\\n    authors: \\\"Tao Yu, Yongqi An, Kuan Zhu, Guibo Zhu, Ming Tang, Jinqiao Wang\\\"\\n    year: 2025\\n    venue: \\\"arXiv Dec 2025\\\"\\n    category: method-component\\n    role: \\\"Function-aware neuron grouping for structured pruning\\\"\\n    relevance: 7\\n    key_finding: \\\"Groups FFN neurons by functional roles; shared neuron retention prevents cross-task accuracy loss; outperforms FLAP/OBC by 1.5-8.5% at 30-40% sparsity\\\"\\n    our_relation: \\\"Closest conceptual parallel — both identify functionally critical neurons, but FANG uses activation-based grouping while we use CKA similarity; no recovery component\\\"\\n    citation_priority: must-cite\\n    arxiv_id: \\\"2512.23014\\\"\\n\\n  - id: funcnet_2025\\n    title: \\\"Pruning Large Language Models by Identifying and Preserving Functional Networks\\\"\\n    authors: \\\"Yiheng Liu, Junhao Ning, Sichen Xia, Xiaohui Gao, Ning Qiang, Bao Ge, Junwei Han, Xintao Hu\\\"\\n    year: 2025\\n    venue: \\\"arXiv Aug 2025\\\"\\n    category: method-component\\n    role: \\\"ICA-based functional network identification for pruning\\\"\\n    relevance: 7\\n    key_finding: \\\"Applies ICA (from neuroimaging) to decompose LLM into functional networks; preserves key neurons within identified networks\\\"\\n    our_relation: \\\"Similar motivation — treat LLM as digital brain and preserve functional structure — but uses ICA vs our CKA; no RLVR recovery\\\"\\n    citation_priority: must-cite\\n    arxiv_id: \\\"2508.05239\\\"\\n\\n  - id: bonsai_2025\\n    title: \\\"Bonsai: Gradient-Free Structured Pruning for LLMs\\\"\\n    authors: \\\"\\\"\\n    year: 2025\\n    venue: \\\"ICML 2025\\\"\\n    category: method-component\\n    role: \\\"Gradient-free structured pruning alternative\\\"\\n    relevance: 6\\n    key_finding: \\\"Achieves competitive structured pruning without backprop\\\"\\n    our_relation: \\\"Alternative pruning strategy; our CKA metric is also gradient-free\\\"\\n    citation_priority: should-cite\\n    arxiv_id: \\\"\\\"\\n\\n  - id: pat_2025\\n    title: \\\"PAT: Pruning-Aware Tuning for Large Language Models\\\"\\n    authors: \\\"Yijiang Liu et al.\\\"\\n    year: 2025\\n    venue: \\\"AAAI 2025\\\"\\n    category: method-component\\n    role: \\\"Joint pruning and tuning framework via Hybrid Sparsification Modules\\\"\\n    relevance: 6\\n    key_finding: \\\"Co-optimizing pruning mask and fine-tuning via HSMs; surpasses LoRA-64 by 1.26% at 25% pruning on Llama2-7B\\\"\\n    our_relation: \\\"Related idea of pruning-tuning interaction; we separate pruning and RLVR recovery\\\"\\n    citation_priority: should-cite\\n    arxiv_id: \\\"2408.14721\\\"\\n\\n  - id: rac_2025\\n    title: \\\"RAC: Chain-of-Thought Reconstruction for Pruned Reasoning Models\\\"\\n    authors: \\\"\\\"\\n    year: 2025\\n    venue: \\\"NeurIPS 2025\\\"\\n    category: method-component\\n    role: \\\"CoT reconstruction post-pruning\\\"\\n    relevance: 7\\n    key_finding: \\\"Reconstructing CoT improves unstructured/2:4 pruned reasoning models\\\"\\n    our_relation: \\\"Complementary recovery strategy; could combine with our RLVR approach\\\"\\n    citation_priority: should-cite\\n    arxiv_id: \\\"\\\"\\n\\n  - id: paser_2025\\n    title: \\\"PASER: Data Selection for Pruning Recovery\\\"\\n    authors: \\\"\\\"\\n    year: 2025\\n    venue: \\\"under review\\\"\\n    category: method-component\\n    role: \\\"Recovery training data selection\\\"\\n    relevance: 6\\n    key_finding: \\\"Selective data for recovery training improves efficiency\\\"\\n    our_relation: \\\"Orthogonal contribution; can apply PASER data selection to our RLVR recovery\\\"\\n    citation_priority: nice-to-have\\n    arxiv_id: \\\"\\\"\\n\\n  - id: dppo_2026\\n    title: \\\"DPPO: Unbiased Dynamic Pruning for Efficient Group-Based Policy Optimization\\\"\\n    authors: \\\"\\\"\\n    year: 2026\\n    venue: \\\"arXiv Mar 2026\\\"\\n    category: method-component\\n    role: \\\"Rollout pruning to accelerate GRPO training\\\"\\n    relevance: 5\\n    key_finding: \\\"Importance-sampling-based rollout pruning achieves 2.37x GRPO speedup with 3.36% accuracy gain on Qwen3-4B\\\"\\n    our_relation: \\\"Could accelerate our GRPO-based RLVR recovery phase\\\"\\n    citation_priority: nice-to-have\\n    arxiv_id: \\\"2603.04135\\\"\\n\\n  - id: arrol_2026\\n    title: \\\"ARRoL: Prune as You Generate — Online Rollout Pruning for Faster and Better RLVR\\\"\\n    authors: \\\"\\\"\\n    year: 2026\\n    venue: \\\"arXiv Mar 2026\\\"\\n    category: method-component\\n    role: \\\"Online rollout pruning for RLVR efficiency\\\"\\n    relevance: 5\\n    key_finding: \\\"Lightweight quality head predicts rollout success probability for early pruning during RLVR\\\"\\n    our_relation: \\\"Complementary technique for speeding up RLVR recovery training\\\"\\n    citation_priority: nice-to-have\\n    arxiv_id: \\\"2603.24840\\\"\\n\\n  - id: restorelcc_2025\\n    title: \\\"RestoreLCC: Restoring Pruned Large Language Models via Lost Component Compensation\\\"\\n    authors: \\\"Zijian Feng, Hanzhang Zhou, Zixiao Zhu, Tianjiao Li, Jia Jim Deryl Chua, Lee Onn Mak, Gee Wah Ng, Kezhi Mao\\\"\\n    year: 2025\\n    venue: \\\"NeurIPS 2025 (Spotlight, top 10%)\\\"\\n    category: method-component\\n    role: \\\"Plug-and-play pruning recovery via activation compensation\\\"\\n    relevance: 6\\n    key_finding: \\\"Contrastively probes critical attention heads, extracts lost components from activation differences, injects them back; +1.25-2.65% over SOTA baselines across structured/unstructured pruning\\\"\\n    our_relation: \\\"Alternative recovery paradigm (activation editing vs RLVR); could be complementary — apply RestoreLCC before RLVR for staged recovery\\\"\\n    citation_priority: should-cite\\n    arxiv_id: \\\"2510.21834\\\"\\n\\n  - id: fastforward_2025\\n    title: \\\"FastForward Pruning: Efficient LLM Pruning via Single-Step Reinforcement Learning\\\"\\n    authors: \\\"\\\"\\n    year: 2025\\n    venue: \\\"arXiv Nov 2025\\\"\\n    category: method-component\\n    role: \\\"RL-based non-uniform sparsity allocation for LLM pruning\\\"\\n    relevance: 5\\n    key_finding: \\\"Decoupled single-step RL framework separates policy optimization from budget satisfaction; efficient non-uniform layer-wise sparsity search\\\"\\n    our_relation: \\\"Uses RL for pruning decisions (not recovery); complementary — could combine their RL sparsity allocation with our CKA-guided selection\\\"\\n    citation_priority: nice-to-have\\n    arxiv_id: \\\"2511.18977\\\"\\n\\n  - id: nirvana_2025\\n    title: \\\"NIRVANA: Structured Pruning Reimagined for Large Language Models Compression\\\"\\n    authors: \\\"Mengting Ai, Tianxin Wei, Sirui Chen, Jingrui He\\\"\\n    year: 2025\\n    venue: \\\"arXiv Sep 2025\\\"\\n    category: method-component\\n    role: \\\"NTK-based saliency with adaptive sparsity allocation\\\"\\n    relevance: 6\\n    key_finding: \\\"First-order saliency from Neural Tangent Kernel under Adam dynamics; adaptive cross-module sparsity; KL-based calibration data selection. Outperforms SOTA on Llama3/Qwen/T5.\\\"\\n    our_relation: \\\"Strong pruning baseline; their NTK saliency is complementary to our CKA functional overlap — could combine both signals\\\"\\n    citation_priority: should-cite\\n    arxiv_id: \\\"2509.14230\\\"\\n\\n  - id: tracenas_2026\\n    title: \\\"TraceNAS: Zero-shot LLM Pruning via Gradient Trace Correlation\\\"\\n    authors: \\\"Prajna G. Malettira, Manish Nagaraj, Arjun Roy, Shubham Negi, Kaushik Roy\\\"\\n    year: 2026\\n    venue: \\\"arXiv Feb 2026\\\"\\n    category: method-component\\n    role: \\\"Gradient trace for joint depth+width NAS-style pruning\\\"\\n    relevance: 6\\n    key_finding: \\\"Scale-invariant gradient trace correlation as proxy for pruned architecture quality; joint depth+width search on single GPU in 8.5h; competitive with training-intensive methods on Llama/Qwen\\\"\\n    our_relation: \\\"Related NAS-for-pruning approach; their gradient trace could complement our CKA as alternative architecture quality proxy\\\"\\n    citation_priority: should-cite\\n    arxiv_id: \\\"2602.02891\\\"\\n\\n  - id: rlrc_2025\\n    title: \\\"RLRC: Reinforcement Learning-based Recovery for Compressed Vision-Language-Action Models\\\"\\n    authors: \\\"Yuxuan Chen, Xiao Li\\\"\\n    year: 2025\\n    venue: \\\"arXiv Jun 2025\\\"\\n    category: method-component\\n    role: \\\"RL-based recovery for compressed VLA models (robotics)\\\"\\n    relevance: 6\\n    key_finding: \\\"Three-stage: structured pruning → SFT+RL recovery → quantization. 8x memory reduction, 2.3x throughput, maintains/surpasses original task success.\\\"\\n    our_relation: \\\"Extends RL recovery paradigm to robotics VLAs; validates that RL recovery generalizes beyond language-only models. Parallel evidence for our RLVR recovery hypothesis.\\\"\\n    citation_priority: should-cite\\n    arxiv_id: \\\"2506.17639\\\"\\n\\n  # === Background / Theory ===\\n  - id: kornblith_cka_2019\\n    title: \\\"Similarity of Neural Network Representations Revisited\\\"\\n    authors: \\\"Simon Kornblith, Mohammad Norouzi, Honglak Lee, Geoffrey Hinton\\\"\\n    year: 2019\\n    venue: \\\"ICML 2019\\\"\\n    category: background\\n    role: \\\"CKA original paper — foundational method for our functional overlap metric\\\"\\n    relevance: 9\\n    key_finding: \\\"CKA achieves 99.3% accuracy in identifying corresponding layers across different initializations; CCA/SVCCA only 1.4-45.4%. Invariant to orthogonal transform and isotropic scaling.\\\"\\n    our_relation: \\\"Foundational method — our CKA-guided pruning directly builds on this. Key justification: CKA >> CCA/SVCCA for reliable layer correspondence\\\"\\n    citation_priority: must-cite\\n    arxiv_id: \\\"1905.00414\\\"\\n\\n  - id: davari_cka_reliability_2023\\n    title: \\\"Reliability of CKA as a Similarity Measure in Deep Learning\\\"\\n    authors: \\\"MohammadReza Davari, Stefan Horoi, Amine Natik, Guillaume Lajoie, Guy Wolf, Eugene Belilovsky\\\"\\n    year: 2023\\n    venue: \\\"ICLR 2023\\\"\\n    category: background\\n    role: \\\"CKA limitations and failure modes — essential for honest CKA justification\\\"\\n    relevance: 7\\n    key_finding: \\\"CKA is sensitive to outliers and simple transformations preserving linear separability; CKA values can be manipulated without changing functional behavior. Calls for caution.\\\"\\n    our_relation: \\\"Must-cite for CKA justification section. We should acknowledge limitations and explain why they don't invalidate our use case (intra-model layer comparison, not cross-model with different transformations).\\\"\\n    citation_priority: must-cite\\n    arxiv_id: \\\"2210.16156\\\"\\n\\n  - id: murphy_debiased_cka_2024\\n    title: \\\"Correcting Biased Centered Kernel Alignment Measures in Biological and Artificial Neural Networks\\\"\\n    authors: \\\"Alex Murphy, Joel Zylberberg, Alona Fyshe\\\"\\n    year: 2024\\n    venue: \\\"ICLR 2024 Re-Align Workshop\\\"\\n    category: background\\n    role: \\\"Debiased CKA for high-dimensionality settings\\\"\\n    relevance: 5\\n    key_finding: \\\"Biased CKA gives misleadingly high similarity when feature-sample ratio is skewed; debiased CKA corrects this. Shuffled data doesn't change biased CKA scores.\\\"\\n    our_relation: \\\"Nice-to-have citation. Our setting (same model, same data) is less affected by this bias, but worth mentioning in limitations.\\\"\\n    citation_priority: nice-to-have\\n    arxiv_id: \\\"2405.01012\\\"\\n\\n  - id: raghu_svcca_2017\\n    title: \\\"SVCCA: Singular Vector Canonical Correlation Analysis for Deep Learning Dynamics and Interpretability\\\"\\n    authors: \\\"Maithra Raghu, Justin Gilmer, Jason Yosinski, Jascha Sohl-Dickstein\\\"\\n    year: 2017\\n    venue: \\\"NeurIPS 2017\\\"\\n    category: background\\n    role: \\\"SVCCA — predecessor to CKA, baseline representation similarity method\\\"\\n    relevance: 5\\n    key_finding: \\\"SVD dimensionality reduction + CCA for comparing representations; reveals bottom-up convergence dynamics and intrinsic dimensionality\\\"\\n    our_relation: \\\"CKA alternative baseline. SVCCA lacks invariance to isotropic scaling and fails at cross-network layer identification (only 45% accuracy vs CKA's 99%)\\\"\\n    citation_priority: should-cite\\n    arxiv_id: \\\"1706.05806\\\"\\n\\n  - id: klabunde_similarity_survey_2025\\n    title: \\\"Similarity of Neural Network Models: A Survey of Functional and Representational Measures\\\"\\n    authors: \\\"Max Klabunde, Tobias Schumacher, Markus Strohmaier, Florian Lemmerich\\\"\\n    year: 2025\\n    venue: \\\"ACM Computing Surveys, Vol. 57, Issue 9\\\"\\n    category: background\\n    role: \\\"Comprehensive survey of representation similarity measures including CKA, CCA, SVCCA, PWCCA\\\"\\n    relevance: 7\\n    key_finding: \\\"First comprehensive review comparing representational vs functional similarity; covers CKA properties, robustness, and practical applications including pruning\\\"\\n    our_relation: \\\"Key citation for CKA justification — survey confirms CKA's advantages over alternatives for model analysis and compression\\\"\\n    citation_priority: must-cite\\n    arxiv_id: \\\"2305.06329\\\"\\n\\n  - id: mipp_2024\\n    title: \\\"MIPP: Mutual Information Preserving Neural Network Pruning\\\"\\n    authors: \\\"\\\"\\n    year: 2024\\n    venue: \\\"arXiv Nov 2024\\\"\\n    category: background\\n    role: \\\"Information-theoretic pruning criterion — MI alternative to CKA\\\"\\n    relevance: 5\\n    key_finding: \\\"Structured activation-based pruning conserving MI between adjacent layers; sample efficiency proportional to MI between masks and data\\\"\\n    our_relation: \\\"MI is a viable alternative but computationally expensive in high dimensions and less stable than CKA. Supports functional similarity matters for pruning.\\\"\\n    citation_priority: nice-to-have\\n    arxiv_id: \\\"2411.00147\\\"\\n\\n  - id: rl_squeezes_2026\\n    title: \\\"RL Squeezes, SFT Expands: Different Mechanisms in Post-Training\\\"\\n    authors: \\\"\\\"\\n    year: 2026\\n    venue: \\\"ICLR 2026 Poster\\\"\\n    category: background\\n    role: \\\"Theoretical basis for why RLVR works differently from SFT\\\"\\n    relevance: 8\\n    key_finding: \\\"RLVR compresses representation while SFT expands; different inductive biases\\\"\\n    our_relation: \\\"Explains why RLVR recovery succeeds where SFT fails post-pruning\\\"\\n    citation_priority: must-cite\\n    arxiv_id: \\\"\\\"\\n\\n  - id: from_llms_to_lrms_2026\\n    title: \\\"From LLMs to LRMs: Rethinking Pruning for Reasoning-Centric Models\\\"\\n    authors: \\\"Longwei Ding, Anhao Zhao, Fanghua Ye, Ziyang Chen, Xiaoyu Shen\\\"\\n    year: 2026\\n    venue: \\\"arXiv Jan 2026\\\"\\n    category: background\\n    role: \\\"Width vs depth pruning for reasoning models\\\"\\n    relevance: 7\\n    key_finding: \\\"Width pruning preserves reasoning better than depth pruning; static pruning > dynamic for long-chain reasoning; recovery relies on distribution-aligned post-fine-tuning, not calibration data.\\\"\\n    our_relation: \\\"Motivates our focus on width-level structured pruning; validates that reasoning models need specialized pruning strategies\\\"\\n    citation_priority: must-cite\\n    arxiv_id: \\\"2601.18091\\\"\\n\\n  - id: p2_law_2025\\n    title: \\\"P2 Law: Scaling Law for Pruning Recovery Training\\\"\\n    authors: \\\"\\\"\\n    year: 2025\\n    venue: \\\"ACL 2025\\\"\\n    category: background\\n    role: \\\"Theoretical scaling of recovery compute\\\"\\n    relevance: 7\\n    key_finding: \\\"Recovery training follows predictable scaling with compute and data\\\"\\n    our_relation: \\\"Informs our recovery budget estimation; we extend to RLVR-specific scaling\\\"\\n    citation_priority: should-cite\\n    arxiv_id: \\\"\\\"\\n\\n  - id: free_lunch_retraining_2025\\n    title: \\\"A Free Lunch in LLM Compression: Revisiting Retraining after Pruning\\\"\\n    authors: \\\"Moritz Wagner, Christophe Roux, Max Zimmer, Sebastian Pokutta\\\"\\n    year: 2025\\n    venue: \\\"arXiv Oct 2025 (revised Feb 2026)\\\"\\n    category: background\\n    role: \\\"Local reconstruction as efficient post-pruning recovery\\\"\\n    relevance: 6\\n    key_finding: \\\"Local reconstruction matches sophisticated PEFT recovery with >10x less data/compute. Pruning method matters less as model size grows.\\\"\\n    our_relation: \\\"Shows cheap recovery can work — but their SFT-based reconstruction has ceiling; our RLVR recovery pushes beyond that ceiling for reasoning tasks.\\\"\\n    citation_priority: should-cite\\n    arxiv_id: \\\"2510.14444\\\"\\n\\n  - id: grasp_2020\\n    title: \\\"Picking Winning Tickets Before Training by Preserving Gradient Flow\\\"\\n    authors: \\\"Chaoqi Wang, Guodong Zhang, Roger Grosse\\\"\\n    year: 2020\\n    venue: \\\"ICLR 2020\\\"\\n    category: background\\n    role: \\\"GraSP — gradient signal preservation for pruning at initialization\\\"\\n    relevance: 5\\n    key_finding: \\\"Hessian-gradient product preserves gradient flow post-pruning; 80% VGG-16 pruning with only 1.6% top-1 drop on ImageNet; outperforms SNIP by 4-6% at high sparsity.\\\"\\n    our_relation: \\\"Classic baseline for gradient-based importance. GRASPrune extends this idea to LLMs; our CKA operates at functional level rather than gradient flow.\\\"\\n    citation_priority: should-cite\\n    arxiv_id: \\\"2002.07376\\\"\\n\\n  - id: fnf_2026\\n    title: \\\"FNF: Functional Network Fingerprint for Large Language Models\\\"\\n    authors: \\\"\\\"\\n    year: 2026\\n    venue: \\\"arXiv Jan 2026\\\"\\n    category: background\\n    role: \\\"Functional network concept applied to LLM identification\\\"\\n    relevance: 4\\n    key_finding: \\\"Co-activating neuron groups form consistent functional networks; robust to model obfuscation.\\\"\\n    our_relation: \\\"Validates the 'functional network' framing we share with FANG/FuncNet; extends concept to model fingerprinting.\\\"\\n    citation_priority: nice-to-have\\n    arxiv_id: \\\"2601.22692\\\"\\n\\n  - id: redundancy_aware_cnn_2020\\n    title: \\\"Redundancy-Aware Pruning of Convolutional Neural Networks\\\"\\n    authors: \\\"\\\"\\n    year: 2020\\n    venue: \\\"Neural Computation\\\"\\n    category: background\\n    role: \\\"Pioneer of redundancy-based pruning\\\"\\n    relevance: 4\\n    key_finding: \\\"Redundancy metrics guide pruning decisions in CNNs\\\"\\n    our_relation: \\\"Conceptual ancestor; we apply redundancy-awareness to LLM structured pruning\\\"\\n    citation_priority: nice-to-have\\n    arxiv_id: \\\"\\\"\\n\\n  - id: self_distilled_rlvr_2026\\n    title: \\\"Self-Distilled RLVR\\\"\\n    authors: \\\"\\\"\\n    year: 2026\\n    venue: \\\"arXiv Apr 2026\\\"\\n    category: background\\n    role: \\\"RLVR training efficiency improvement\\\"\\n    relevance: 5\\n    key_finding: \\\"Self-distillation stabilizes RLVR training and improves sample efficiency\\\"\\n    our_relation: \\\"Could improve our RLVR recovery phase efficiency\\\"\\n    citation_priority: nice-to-have\\n    arxiv_id: \\\"2604.03128\\\"\\n\\n  - id: diet_2026\\n    title: \\\"DieT: Dimension-wise Global Pruning via Task-specific Importance Score\\\"\\n    authors: \\\"\\\"\\n    year: 2026\\n    venue: \\\"arXiv Mar 2026\\\"\\n    category: background\\n    role: \\\"Dimension-wise importance for width pruning\\\"\\n    relevance: 5\\n    key_finding: \\\"Task-specific dimension importance outperforms activation-based metrics at 20-40% sparsity\\\"\\n    our_relation: \\\"Alternative width importance metric; we use CKA overlap instead\\\"\\n    citation_priority: nice-to-have\\n    arxiv_id: \\\"2603.23985\\\"\\n\\n  - id: task_neurons_2026\\n    title: \\\"Exploring the Limits of Pruning: Task-Specific Neurons, Model Collapse, and Recovery in Task-Specific LLMs\\\"\\n    authors: \\\"\\\"\\n    year: 2026\\n    venue: \\\"arXiv Apr 2026\\\"\\n    category: background\\n    role: \\\"Task-specific neuron identification and pruning recovery dynamics\\\"\\n    relevance: 6\\n    key_finding: \\\"10% task-specific neuron removal causes collapse; 15-20% robustness threshold; fine-tuning substantially recovers\\\"\\n    our_relation: \\\"Supports need for recovery-aware pruning; our CKA predicts which neurons are functionally critical\\\"\\n    citation_priority: should-cite\\n    arxiv_id: \\\"2604.27115\\\"\\n\\n  - id: ddp_2026\\n    title: \\\"DDP: Deterministic Differentiable Structured Pruning for Large Language Models\\\"\\n    authors: \\\"\\\"\\n    year: 2026\\n    venue: \\\"arXiv Mar 2026\\\"\\n    category: background\\n    role: \\\"Differentiable mask-only structured pruning\\\"\\n    relevance: 5\\n    key_finding: \\\"Deterministic soft surrogate of l0 constraint eliminates train-test mismatch in differentiable pruning\\\"\\n    our_relation: \\\"Alternative pruning backbone; mask-only optimization complementary to our CKA-guided selection\\\"\\n    citation_priority: nice-to-have\\n    arxiv_id: \\\"2603.08065\\\"\\n\\n  - id: pruning_vlm_recovery_2026\\n    title: \\\"Structural Pruning of Large Vision Language Models: Pruning Dynamics, Recovery, and Data Efficiency\\\"\\n    authors: \\\"Yiran Huang, Lukas Thede, Massimiliano Mancini, Wenjia Xu, Zeynep Akata\\\"\\n    year: 2026\\n    venue: \\\"arXiv Apr 2026\\\"\\n    category: background\\n    role: \\\"Comprehensive pruning + recovery study for VLMs\\\"\\n    relevance: 5\\n    key_finding: \\\"Width pruning + KD recovery outperforms layer pruning + SFT on VLMs; 5% data recovers 95% performance; SFT+hidden-state distillation is optimal.\\\"\\n    our_relation: \\\"Validates width pruning + recovery paradigm; our CKA-guided approach adds prediction of recoverability\\\"\\n    citation_priority: nice-to-have\\n    arxiv_id: \\\"2604.24380\\\"\\n\\n  - id: hape_2026\\n    title: \\\"HAP-E: Hessian-Aware Structured Pruning of LLMs for Efficient Inference\\\"\\n    authors: \\\"\\\"\\n    year: 2026\\n    venue: \\\"ICLR 2026 (submitted)\\\"\\n    category: background\\n    role: \\\"Hessian-aware structured pruning with adaptive budget allocation\\\"\\n    relevance: 5\\n    key_finding: \\\"Adaptive cross-layer budget reallocation via global screening + OBS-equivalent batch pruning; up to 3% accuracy over SOTA structured pruning\\\"\\n    our_relation: \\\"Alternative pruning backbone with second-order optimization; complementary to our CKA-guided selection\\\"\\n    citation_priority: nice-to-have\\n    arxiv_id: \\\"\\\"\\n\\n  - id: slimllm_2025\\n    title: \\\"SlimLLM: Accurate Structured Pruning for Large Language Models\\\"\\n    authors: \\\"Jialong Guo, Xinghao Chen, Yehui Tang, Yunhe Wang\\\"\\n    year: 2025\\n    venue: \\\"ICML 2025\\\"\\n    category: background\\n    role: \\\"Holistic channel/head importance evaluation with linear regression recovery\\\"\\n    relevance: 5\\n    key_finding: \\\"Evaluates importance of entire channels/heads holistically; non-uniform layer-based pruning ratio via cosine similarity; linear regression for fast recovery\\\"\\n    our_relation: \\\"Alternative structured pruning metric; their cosine-based layer ratio is complementary to our CKA functional overlap\\\"\\n    citation_priority: nice-to-have\\n    arxiv_id: \\\"2505.22689\\\"\\n\\n  - id: spap_2025\\n    title: \\\"SPAP: Structured Pruning via Alternating Optimization and Penalty Methods\\\"\\n    authors: \\\"\\\"\\n    year: 2025\\n    venue: \\\"arXiv May 2025\\\"\\n    category: background\\n    role: \\\"Optimization-theory-grounded MLP pruning\\\"\\n    relevance: 5\\n    key_finding: \\\"Mixed-integer formulation with relaxation guarantee; alternating minimization with closed-form updates; 1.29x speedup at 30% sparsity\\\"\\n    our_relation: \\\"Could serve as alternative pruning backbone for MLP layers; operates at different abstraction level from our CKA selection\\\"\\n    citation_priority: nice-to-have\\n    arxiv_id: \\\"2505.03373\\\"\\n\\n  - id: wandapp_2025\\n    title: \\\"Wanda++: Pruning Large Language Models via Regional Gradients\\\"\\n    authors: \\\"\\\"\\n    year: 2025\\n    venue: \\\"ACL 2025\\\"\\n    category: background\\n    role: \\\"Gradient-enhanced unstructured pruning\\\"\\n    relevance: 4\\n    key_finding: \\\"Regional gradients improve Wanda score by up to 32% perplexity reduction; regional optimization minimizes dense-sparse output discrepancy\\\"\\n    our_relation: \\\"Unstructured pruning evolution; orthogonal to our structured approach but regional optimization idea could inform per-block CKA computation\\\"\\n    citation_priority: nice-to-have\\n    arxiv_id: \\\"2503.04992\\\"\\n\\n# === Update Log ===\\n# 2026-05-15: Literature survey targeting 4 reviewer-flagged gaps\\n#   Direction 1 (Structured pruning + RLVR recovery): Added RLRC, NIRVANA, free_lunch_retraining\\n#   Direction 2 (CKA in pruning/NAS): Added davari_cka_reliability (must-cite), murphy_debiased_cka, tracenas\\n#   Direction 3 (FANG/FuncNet): Confirmed details; added FNF as background\\n#   Direction 4 (GraSP baselines): Added grasp_2020 (original), tracenas\\n#   Updated: self_healing authors (Ji et al., ICLR 2026), from_llms_to_lrms (Ding et al., 2601.18091),\\n#            mpruner (arxiv 2408.13482), slimllm authors, pruning_vlm_recovery authors\\n#   Added citation_priority field (must-cite / should-cite / nice-to-have) to all entries\\n\", \"total_chars\": 29231, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "26434036-dcfb-4086-bb85-e4a5bed15aeb",
  "isSidechain": true,
  "promptId": "39eba513-b35c-4482-87e4-5618fcf0979e",
  "agentId": "a7fe9f34d2b39e51d",
  "type": "user",
  "uuid": "7650b9f4-1c77-4bdd-a323-6f60303190e2",
  "sourceToolAssistantUUID": "26434036-dcfb-4086-bb85-e4a5bed15aeb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "87456414-598d-4dd4-8776-aaed1b39d708",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-16T15:42:10.979Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01CyRwb6EmaPxyQK4k74GXpx`</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7650b9f4-1c77-4bdd-a323-6f60303190e2",
  "isSidechain": true,
  "agentId": "a7fe9f34d2b39e51d",
  "requestId": "req_011Cb6W6W3X8G3HJCbskQ29p",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9c0a4a91-7ff6-4cd7-9eaf-47def345dcc6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "87456414-598d-4dd4-8776-aaed1b39d708",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KDN3AnTz8Xt3GFNH5eUtNZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5459,
      "cache_read_input_tokens": 16436,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5459,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 50,
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

_source line 15 · 2026-05-16T15:42:10.988Z_

<details><summary>↩ Tool result · `toolu_01CyRwb6EmaPxyQK4k74GXpx`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper_framing.md\", \"content\": \"# Paper Framing — recovery_aware_struct_prune\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR May 25 submission)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May 25, 2026\\n\\n## Core Insight (Redundancy-Stability Tradeoff)\\nRLVR alignment (GRPO) fundamentally fails on structurally pruned reasoning models: reward improves but accuracy does not — a pruning-induced reward hacking phenomenon. We show the failure mechanism via **collapse dynamics**: pruning method determines how fast GRPO collapses, and this speed is a diagnostic of structural damage type. Crucially, functional redundancy plays **opposite roles** under SFT vs RLVR recovery:\\n\\n- **SFT**: redundant structures (high CKA overlap) are safely removable — their function redistributes through gradient-based learning. CKA-aware pruning (RASP) yields marginal SFT advantage.\\n- **RLVR**: redundant structures provide **exploration stability** — backup paths that prevent policy collapse during RL. Removing them (as RASP does) accelerates collapse.\\n\\nThis creates a **Redundancy-Stability Tradeoff**: the structures optimal to prune for SFT recovery are exactly those needed for RLVR stability. Optimal pruning is fundamentally conditioned on the recovery paradigm.\\n\\n## Core Claims (3) — REVISED based on experimental evidence\\n\\n1. **GRPO reward-accuracy decoupling is universal; pruning adds training collapse**: GRPO does not improve reasoning accuracy for ANY model post-SFT — unpruned (**81.27% = SFT 81.27%, Δ=0.00pp, identical 1072/1319 correct**), Standard-pruned (58.91% vs 59.29%, Δ=-0.38pp), RASP-pruned (60.65% vs 61.49%, Δ=-0.84pp). Reward increases dramatically (unpruned: 0→0.661) yet accuracy is unchanged — a universal reward-accuracy decoupling under GRPO+GSM8K+greedy. The pruning-specific phenomenon is **training collapse**: RASP collapses permanently at step ~10 (frac_zero_std→0.95, grad→0.007), Standard shows transient dip at step ~60, while unpruned trains stably for 100 steps. GRPO's reward signal does not encode genuine reasoning improvement; pruning removes the structural capacity to even sustain RL training.\\n\\n2. **Collapse severity gradient diagnoses structural damage**: Three-model comparison reveals a clean severity gradient — RASP (removes redundant, protects unique): permanent collapse step ~10, peak reward 0.039; Standard (importance-only): transient dip step ~60, final reward 0.065; Unpruned: no collapse, final reward 0.661. The 6× speedup from Standard→RASP confirms that functional redundancy provides RLVR exploration stability. Collapse dynamics are a zero-cost diagnostic: fast collapse = aggressive redundancy removal = poor RL trainability.\\n\\n3. **Recovery method conditions optimal pruning strategy**: For SFT recovery, RASP shows marginal advantage (+2.2pp, RASP 61.49% vs Standard 59.29%, N=1319, p=0.25). For RLVR stability, RASP is actively harmful (6× faster collapse). The structures optimal to prune for SFT are exactly those needed for RLVR stability — a fundamental Redundancy-Stability Tradeoff. Consistent with \\\"RL Squeezes, SFT Expands\\\" (ICLR 2026).\\n\\n## Evidence Status (as of 2026-05-16, ALL CORE DATA COMPLETE)\\n\\n| Evidence | Status | Result |\\n|----------|--------|--------|\\n| Unpruned SFT eval (N=1319) | ✅ | 81.27% |\\n| Unpruned GRPO step-100 eval (N=1319) | ✅ | **81.27% (Δ=0.00pp, 1072/1319 = identical to SFT)** |\\n| Unpruned GRPO step-90 eval (N=1319) | ✅ | **80.59% (1063/1319, confirms stability across late training)** |\\n| Standard SFT eval (N=1319) | ✅ | 59.29% |\\n| Standard GRPO step-50 eval (N=1319) | ✅ | 58.91% (Δ=-0.38pp) |\\n| RASP SFT eval (N=1319) | ✅ | 61.49% |\\n| RASP GRPO step-5 eval (N=1319) | ✅ | 60.65% (Δ=-0.84pp) |\\n| RASP GRPO v9 collapse dynamics | ✅ | Permanent collapse step ~10, peak reward 0.039 |\\n| Standard GRPO v8 dynamics | ✅ | Transient dip step ~60, recovery step ~90 |\\n| Unpruned GRPO v2 dynamics | ✅ | No collapse, 100 steps stable, reward 0.661 |\\n| Alpha ablation (cal=512) | ✅ | U-shape: α≥1.0 > α≤0.5 post-prune |\\n| SFT gap significance | ⚠️ p=0.25 | Not significant at N=1319; scope expansion to higher sparsity planned |\\n| RASP GRPO step-10 eval (N=1319) | ✅ | **61.87% — collapse onset does NOT reduce accuracy (vs step-5 60.65%, p=0.52)** |\\n\\n## Story Spine\\n\\n- **Problem**: The reasoning model compression pipeline (prune → recover → align) assumes alignment is independent of pruning decisions. We show this assumption fails catastrophically: GRPO alignment on pruned models produces reward improvement without accuracy gain, followed by complete collapse. The pruning-alignment interaction is not merely suboptimal — it is fundamentally broken under current practice.\\n\\n- **Existing approaches & gaps**: Self-Healing (2025) claims RLVR recovers pruned reasoning models to 95%+ at 25% compression — but uses a single pruning ratio and does not report per-step accuracy during GRPO. GRASPrune (ACL 2026) provides SOTA budgeted structural pruning but doesn't study recovery or alignment at all. RESP (Dec 2025) uses reasoning-trace calibration without recovery. No work has documented GRPO collapse on pruned models, explained its mechanism, or shown that pruning strategy determines collapse dynamics.\\n\\n- **Our framing**: We present the first systematic study of how structural pruning interacts with RLVR alignment in reasoning LLMs. We introduce RASP (S(h) = I(h) × (1-F(h))^α) not as a universally superior method, but as a **diagnostic tool** that reveals the Redundancy-Stability Tradeoff: CKA-aware structure selection that benefits SFT recovery actively harms RLVR stability. This reframes the pruning-alignment relationship from \\\"which structures to remove for best recovery\\\" to \\\"recovery paradigm determines what counts as safe to remove.\\\"\\n\\n- **Headline result**: \\\"GRPO reward improvement never translates to accuracy gain (unpruned: reward 0→0.661, accuracy 81.27%→81.27%; identical 1072/1319 correct). But pruning causes GRPO training collapse: RASP-pruned collapses permanently at step 10, Standard-pruned at step 60, unpruned never. The severity gradient (RASP > Standard > Unpruned) reveals that structural redundancy — expendable for SFT — provides critical RL exploration stability.\\\"\\n\\n## Venue Fit\\n- EMNLP Efficient Methods track: structured pruning + reasoning model alignment failure analysis\\n- Negative/diagnostic results challenging published claims (Self-Healing) are high-impact at *ACL venues\\n- Reasoning model compression pipeline failures are immediately practical (timely: DeepSeek-R1, QwQ, Kimi-K1.5)\\n- Mechanistic analysis (collapse dynamics, reward-accuracy divergence) aligns with EMNLP empirical rigor\\n\\n## Venue Fit Risks\\n- **\\\"Just a negative result without solution\\\"**: Mitigate with (1) mechanistic explanation (redundancy-stability tradeoff), (2) RASP as diagnostic tool (collapse speed predicts pruning quality for RL), (3) actionable implication (SFT-only recovery is currently the safe path; RLVR needs pruning-aware modifications)\\n- **\\\"Single model\\\"**: DeepSeek-R1-Distill-Qwen-7B is the canonical open reasoning model; multi-method comparison (RASP/Standard/Unpruned) + multi-recovery (SFT/GRPO) compensates\\n- **\\\"GRPO config might be wrong\\\"**: Report hyperparameter sensitivity (alpha ablation), show collapse is robust across configs, cite Self-Healing uses similar GRPO setup\\n- **\\\"SFT gap not significant\\\"**: Frame honestly as marginal; the paper's contribution is the GRPO failure + mechanism, not the SFT comparison. SFT gap is supplementary context.\\n- **\\\"Collapse might be training instability, not pruning-specific\\\"**: Unpruned GRPO ran 100 steps with zero collapse (reward 0.661, stable frac_zero_std ≤0.275) — pruning-specificity confirmed\\n\\n## Anticipated Reviewer Concerns & Experimental Responses\\n\\n| Concern | Response | Supporting Experiment |\\n|---------|----------|----------------------|\\n| GRPO failure might be hyperparameter issue | Alpha ablation shows U-shape is robust; reward increases but accuracy never follows | alpha_ablation_sweep |\\n| Need unpruned control for pruning-specificity | Unpruned GRPO: 100 steps stable, no collapse, reward 0.661 vs pruned collapse at step 10-60 | grpo_unpruned_v2 |\\n| SFT gap not significant | Acknowledged; paper's main claim is GRPO failure, not SFT superiority | sft_eval N=1319 |\\n| Collapse speed might not generalize | Multi-method comparison (RASP/Standard) + multi-config (alpha sweep) | grpo_v8, grpo_v9 |\\n| How does this relate to Self-Healing claims? | Self-Healing uses 25% unstructured; our structured pruning at 20% creates different damage pattern | Discussion section |\\n| What's the practical recommendation? | SFT recovery only for structurally pruned models; RLVR requires pruning-aware alignment (future work) | All experiments |\\n| CKA-aware pruning hurts RLVR — why publish RASP? | RASP is the diagnostic tool that REVEALS the tradeoff; its failure under RLVR is the evidence | grpo_v9 vs grpo_v8 |\\n\\n## Key Differentiations\\n- **vs Self-Healing (2025)**: Claims RLVR recovers pruned models → we show GRPO fails (reward hacking + collapse); different pruning granularity and controlled collapse analysis\\n- **vs MPruner (2024)**: inter-layer CKA for depth pruning in CNNs → we use intra-layer CKA as diagnostic tool revealing redundancy-stability tradeoff in reasoning LLMs\\n- **vs GRASPrune (ACL 2026)**: SOTA budgeted pruning without recovery/alignment study → we study the full prune-recover-align pipeline failure\\n- **vs RESP (Dec 2025)**: reasoning-trace calibration without recovery → we study recovery paradigm interaction\\n- **vs PASER (2025)**: optimizes recovery DATA → we show even optimal pruning STRUCTURE cannot save RLVR alignment\\n\\n## Open Questions (scope expansion experiments planned)\\n1. ~~Does unpruned model also show reward-accuracy divergence?~~ → YES, confirmed: 81.27% = 81.27%\\n2. ~~What do RASP v9 fine-grained checkpoints show?~~ → Permanent collapse, step-5 eval = 60.65% (≈ SFT)\\n3. Can higher sparsity (25-30%) make SFT gap significant AND intensify GRPO collapse? (scope expansion Phase 1)\\n4. Does the collapse pattern reproduce on Qwen2.5-Math-7B? (scope expansion Phase 2)\\n5. Is there a GRPO config that avoids collapse on pruned models? (future work motivation)\\n\", \"total_chars\": 10165, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9c0a4a91-7ff6-4cd7-9eaf-47def345dcc6",
  "isSidechain": true,
  "promptId": "39eba513-b35c-4482-87e4-5618fcf0979e",
  "agentId": "a7fe9f34d2b39e51d",
  "type": "user",
  "uuid": "9e7b17f3-2d56-4b57-818a-720ac479eec7",
  "sourceToolAssistantUUID": "9c0a4a91-7ff6-4cd7-9eaf-47def345dcc6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "87456414-598d-4dd4-8776-aaed1b39d708",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-16T15:42:15.077Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01LqX29EcGi4ULMnPAgacn7d`</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e7b17f3-2d56-4b57-818a-720ac479eec7",
  "isSidechain": true,
  "agentId": "a7fe9f34d2b39e51d",
  "requestId": "req_011Cb6W6vXRihP5Lay8F4LHo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "74ddc4be-03e5-43f8-8015-2273575cd6ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "87456414-598d-4dd4-8776-aaed1b39d708",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RXaD2AwyvnWA7gonaGVFYN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14788,
      "cache_read_input_tokens": 21895,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14788,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 57,
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

_source line 17 · 2026-05-16T15:42:15.093Z_

<details><summary>↩ Tool result · `toolu_01LqX29EcGi4ULMnPAgacn7d`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/ROADMAP.md\", \"content\": \"# recovery_aware_struct_prune — Research Dashboard\\n\\n> 最后更新: 2026-05-16 08:05 UTC | 更新原因: D044/D045 narrative pivot complete, 25% expansion in progress, ROADMAP 16h stale refresh\\n\\n> 核心方向详见 paper_framing.md | 实验计划详见 experiment_plan.yaml\\n\\n## 核心方向\\n**Redundancy-Stability Tradeoff**: GRPO alignment fundamentally fails on structurally pruned reasoning models — reward improves but accuracy never follows (universal decoupling). Pruning adds training collapse whose severity diagnoses structural damage type. Functional redundancy plays opposite roles under SFT vs RLVR recovery.\\n\\n## 目标会议\\nEMNLP 2026 ARR May 25 提交（距今 ~9 天）\\n\\n## 当前阶段\\n**Research Phase — Scope Expansion** (D044/D045 后)\\n- Core 20% data: ✅ ALL COMPLETE (3 claims fully supported)\\n- 25% sparsity expansion: SFT 完成, eval 进行中/刚完成, GRPO 待启动\\n- Qwen2.5-Math-7B (Phase 2): importance+CKA scores 已算, RASP pruning 进行中\\n- Paper writing: Paper Agent Step 2 (Plot Generation) 进行中\\n\\n## 核心证据 (20% sparsity, N=1319)\\n| 实验 | 结果 | Claim |\\n|------|------|-------|\\n| Unpruned SFT → GRPO step-100 | 81.27% → 81.27% (Δ=0.00, reward 0→0.661) | C1: Universal decoupling |\\n| RASP GRPO v9 collapse | Permanent step ~10, peak reward 0.039, frac_zero_std→0.95 | C2: Collapse gradient |\\n| Standard GRPO v8 collapse | Transient dip step ~60, recovery step ~90 | C2: Collapse gradient |\\n| Unpruned GRPO v2 | 100 steps stable, no collapse, reward 0.661 | C2: Pruning-specificity |\\n| RASP SFT vs Standard SFT | 61.49% vs 59.29% (Δ=+2.2pp, p=0.25) | C3: SFT marginal advantage |\\n| RASP step-10 eval | 61.87% (collapse onset ≠ accuracy loss) | Bidirectional decoupling |\\n\\n## Scope Expansion 进度\\n### Phase 1: 25% Sparsity (intensify collapse)\\n- [x] pruned_rasp_25 + pruned_standard_25\\n- [x] sft_rasp_25 + sft_standard_25\\n- [ ] eval_sft_standard_25 (刚完成/进行中 — 等 Agent 确认)\\n- [ ] eval_sft_rasp_25 (刚完成/进行中 — 等 Agent 确认)\\n- [ ] grpo_standard_25 + grpo_rasp_25 (下一步：4张GPU全部投入)\\n- [ ] eval 25% GRPO checkpoints\\n\\n### Phase 2: Qwen2.5-Math-7B (cross-model validation)\\n- [x] importance_scores_qwen_math.pt + cka_scores_qwen_math.pt\\n- [ ] prune_rasp_20_qwen_math (CPU task, 进行中)\\n- [ ] prune_standard_20_qwen_math (进行中)\\n- [ ] SFT → GRPO → eval full pipeline\\n\\n### Paper Writing\\n- [x] writing_plan.yaml 审批通过\\n- [ ] Step 2: Plot Generation (Paper Agent 进行中)\\n- [ ] Step 3-5: Draft → Refinement → Submit to Review\\n\\n## GPU 预算\\n- **westb-23072**: 2× ~98GB GPU | 当前全部空闲 ⚠️\\n- **westd-11672**: 2× ~95GB GPU | 当前全部空闲 ⚠️\\n- 约束 C001: 仅允许 westb cuda:0/1, westd cuda:0/1\\n- 总预算 ~480 GPU-hours (10 days × 4 GPU × 24h)\\n\\n## 近期任务\\n- [ ] 确认 25% SFT eval 结果 → 更新 paper_framing.md\\n- [ ] 启动 25% GRPO (westb 2卡) — 预期 collapse 比 20% 更快\\n- [ ] Qwen2.5-Math-7B 剪枝完成 → SFT (westd 2卡)\\n- [ ] Paper Agent Step 2 完成 → 审查 plots\\n- [ ] 30% sparsity 如时间允许\\n\\n## 关键风险\\n1. **DDL 9天** — 25% GRPO + Qwen Math 需要并行推进，不能串行\\n2. **25% SFT gap** — 如果 25% 下 RASP vs Standard SFT gap 显著，加强 C3\\n3. **Qwen Math 可能不复现** — 但单模型+多sparsity已足够 EMNLP Findings\\n4. **Paper writing 与实验并行** — Paper Agent 先用 20% 数据写主体，后续 patch 25%/Qwen 数据\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D047 | 2026-05-16 | 新增 RASP-RLVR 实验：反转 CKA scoring 保护冗余结构，预防 GRPO coll | grpo_stage2_rasp_20_v9, grpo_stage2_standard_20_v8, grpo_unpruned_v2 |\\n| D046 | 2026-05-16 | Qwen Math calibration=256 不重跑，论文加 footnote 说明差异 | prune_rasp_20_qwen_math, prune_standard_20_qwen_math |\\n| D045 | 2026-05-16 | Core data complete: GRPO reward-accuracy decouplin | eval_grpo_unpruned_v2_step100, eval_grpo_rasp_v9_step5, grpo_unpruned_v2 |\\n| D044 | 2026-05-16 | Major narrative pivot: from \\\"RASP enables better R | eval_grpo_standard_step50_full, grpo_stage2_standard_20_v8, grpo_stage2_rasp_20_v9 |\\n| D043 | 2026-05-15 | Standard v8 step 60 确认 collapse。三模型全 collapse 时间线： | grpo_stage2_standard_20_v8, grpo_stage2_rasp_20_v8, grpo_unpruned_baseline, eval_sft_standard_full_westd, eval_sft_rasp_full_westd |\\n| D042 | 2026-05-15 | 暂不引用 GRPO collapse 因果结论——等 Standard v8 完成后对比三者 col | grpo_unpruned_baseline, grpo_stage2_rasp_20_v8, grpo_standard_v8 |\\n| D041 | 2026-05-15 | Unpruned baseline 实验设计无效——缺少 SFT 步骤，不构成公平对照 | grpo_unpruned_baseline |\\n| D040 | 2026-05-15 | Unpruned baseline 判定无效，需重新设计为 SFT→GRPO 流程 | grpo_unpruned_baseline |\\n| D039 | 2026-05-15 | Unpruned GRPO collapse invalidates \\\"pruning causes | grpo_unpruned_baseline, grpo_stage2_standard_20_v8, grpo_rasp_20_v8 |\\n| D038 | 2026-05-15 | Narrative pivot: 暂定 Narrative A (Pruning for Plast | grpo_rasp_20_v8, grpo_stage2_standard_20_v8, grpo_unpruned_baseline |\\n\\n\", \"total_chars\": 4449, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "74ddc4be-03e5-43f8-8015-2273575cd6ac",
  "isSidechain": true,
  "promptId": "39eba513-b35c-4482-87e4-5618fcf0979e",
  "agentId": "a7fe9f34d2b39e51d",
  "type": "user",
  "uuid": "bba119fe-119f-412f-8546-6b3b7bc003f6",
  "sourceToolAssistantUUID": "74ddc4be-03e5-43f8-8015-2273575cd6ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "87456414-598d-4dd4-8776-aaed1b39d708",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-16T15:42:15.478Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01QFnTkYW3awdxTfDPXoLNri`</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bba119fe-119f-412f-8546-6b3b7bc003f6",
  "isSidechain": true,
  "agentId": "a7fe9f34d2b39e51d",
  "requestId": "req_011Cb6W6vXRihP5Lay8F4LHo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6fb59575-ff70-4c53-b155-783d3c072069",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "87456414-598d-4dd4-8776-aaed1b39d708",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RXaD2AwyvnWA7gonaGVFYN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14788,
      "cache_read_input_tokens": 21895,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14788,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 57,
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

_source line 19 · 2026-05-16T15:42:15.497Z_

<details><summary>↩ Tool result · `toolu_01QFnTkYW3awdxTfDPXoLNri`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/decisions.yaml\", \"content\": \"_next_id: 48\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 06:10 UTC\\n  summary: MVP 接受 35% sparsity 下 MLP-only pruning，不强制 attention 配额\\n  rationale: 全局统一排序下 attention GQA groups importance 普遍高于 MLP groups，35% sparsity\\n    自然只剪 MLP（367 groups）。这是模型结构特征的正确反映，不应人为干预。MLP-level correlation (N=367) 足以验证 CKA→recoverability\\n    假设。50% sparsity 放 Phase 2 获取 attention-level 数据。\\n  related_experiments:\\n  - exp_id: mvp_rasp_pipeline_v2\\n    role: primary\\n    result: running\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 13:31 UTC\\n  summary: 终止无效 GRPO，改用 SFT warmup → GRPO 两阶段恢复策略\\n  rationale: 35% 结构化剪枝后两个模型 accuracy 仅 0.15%（输出退化），GRPO 150 步 loss=0/grad_norm=0，无学习信号。frac_reward_zero_std\\n    ≈ 1.0 表明几乎所有 completion 得 0 reward，GRPO 无法计算有效 advantage。SFT warmup 用 ground truth\\n    数据先恢复基本能力再转 GRPO 是解决 reward desert 的标准做法。\\n  related_experiments:\\n  - exp_id: mvp_rasp_pipeline_v2\\n    role: motivating_failure\\n    result: GRPO 150 步 loss=0, grad_norm=0; post-prune accuracy 0.15% for both models\\n  depends_on: []\\n- id: D003\\n  date: 2026-05-14 13:53 UTC\\n  summary: 暂缓 SFT warmup，优先审计剪枝实现正确性\\n  rationale: 两个不同剪枝策略产出精确相同的 accuracy（2/1319）统计上极不寻常，35% structured pruning 不应导致 7B\\n    模型完全崩溃。Reviewer 怀疑存在实现 bug（config 不匹配、全零层等）。若根因是代码问题，SFT warmup 是在错误基础上浪费算力。需先排除实现问题再决定恢复策略。\\n  related_experiments:\\n  - exp_id: mvp_rasp_pipeline_v2\\n    role: audit_target\\n    result: both pruned models 0.15% accuracy, identical 2/1319\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 13:59 UTC\\n  summary: 修复 min_keep_mlp=4 导致的 per-layer 过度剪枝，重跑 MVP pipeline v3\\n  rationale: 根因确认：min_keep_mlp=4 允许单层 MLP 被剪至 14.3% capacity，全局排序集中破坏 early layers（0-6），两个模型均崩溃至\\n    0.15%。修复方案：min_keep_mlp 提升到 40% per layer + per-layer capacity floor。RASP scoring\\n    逻辑本身正常（产生了不同剪枝结构），核心假设仍可验证，只需收紧约束后重跑。同时补基线评估。\\n  related_experiments:\\n  - exp_id: mvp_rasp_pipeline_v2\\n    role: root_cause_identified\\n    result: min_keep_mlp=4 causes early layer collapse to 14.3% MLP capacity\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-14 15:13 UTC\\n  summary: 放弃 35% sparsity 作为 MVP 目标，改用 20%/25% 双 sparsity 快速探测后选优跑 GRPO\\n  rationale: v3 证实 35% structured pruning 对 DeepSeek-R1-Distill-Qwen-7B 太激进（Standard\\n    0%, RASP 1%），即使 per-layer capacity floor ≥40% 也无法挽救。蒸馏模型冗余已被压缩，比 base 模型更脆弱。RASP\\n    hypothesis 未被 falsify——只是当前 sparsity 下无法测试恢复性。策略：先在 20%/25% 快速 prune+eval（~1h），选\\n    post-prune accuracy 最合适的 sparsity 集中投入 GRPO（~15h），避免浪费 GPU 在错误 sparsity 上。35%+SFT\\n    warmup 留待 Phase 2。\\n  related_experiments:\\n  - exp_id: mvp_rasp_pipeline_v3\\n    role: negative_result\\n    result: Standard 0% / RASP 1% at 33% actual sparsity, per-layer floor working\\n      correctly\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-14 17:06 UTC\\n  summary: 20% sparsity 下 RASP 29% vs Standard 1%，Scenario B 确认，GRPO 双 GPU 并行恢复对比\\n  rationale: RASP 20% post-prune accuracy 29% vs Standard 20% 仅 1%（p<0.0001），MLP 总容量完全相同（74.5%），差异纯粹在剪枝分布。CKA\\n    overlap scoring 保护了 layer 16-22 推理关键层。落入 Scenario B（最强叙事）：RASP 不仅预测 recoverability，pruning\\n    本身就保护推理能力。下一步 GRPO 双 GPU 并行（cuda:0 RASP, cuda:1 Standard），验证 recovery 差异。25% eval\\n    继续跑完收集 sparsity 阈值数据。\\n  related_experiments:\\n  - exp_id: mvp_rasp_pipeline_v4\\n    role: primary\\n    result: RASP_20=29% vs Standard_20=1%, p<0.0001\\n  depends_on:\\n  - D005\\n- id: D007\\n  date: 2026-05-14 17:37 UTC\\n  summary: Kill 270h GRPO runs，用 max_completion=1024 + 1 epoch + 2000 samples 重启，目标\\n    <10h 完成\\n  rationale: 当前 GRPO 配置 max_completion_length=4096 导致 173s/step、总计 270h，超过 EMNLP deadline。GSM8K\\n    的 R1 推理链通常 200-800 tokens，4096 严重浪费。MVP 只需证明 recovery 趋势（ρ ≥ 0.4），1 epoch + 2000\\n    samples 足够看到信号。Standard 模型 1% 起点大概率触发 RewardDesertCallback，本身就是\\\"不可恢复\\\"的证据。预估新配置\\n    ~625 steps × ~43s/step ≈ 7.5h。\\n  related_experiments:\\n  - exp_id: grpo_rasp_20\\n    role: kill_and_restart\\n    result: running_too_slow\\n  - exp_id: grpo_standard_20\\n    role: kill_and_restart\\n    result: running_too_slow\\n  depends_on:\\n  - D006\\n- id: D008\\n  date: 2026-05-14 18:40 UTC\\n  summary: 正式更新 MVP 判定标准：从 per-group ρ ≥ 0.4 改为 model-level 显著性检验；扩大 eval 到 full GSM8K\\n    (1319 samples)\\n  rationale: 原 ρ ≥ 0.4 需要 per-head/per-group F(h) 与 recoverability 数据点（N≈92），但 v4\\n    实验是 model-level 对比（N=2），无法计算 Spearman ρ。Reviewer 建议改为：RASP-pruned model 在 matched\\n    sparsity + matched param count 下，post-prune accuracy 和/或 post-recovery accuracy\\n    显著优于 Standard-pruned model（p < 0.05）。post-prune 部分（29% vs 1%, p < 0.0001）已 pass。同时当前\\n    N=100 eval CI 太宽（±9pp），需扩到 full test set 1319 samples（CI ±2.4pp）。另：RewardDesertCallback\\n    在当前配置下不会提前终止（patience=500 steps = total steps），不影响实验但需修正论文叙事。\\n  related_experiments:\\n  - exp_id: grpo_rasp_20_fast\\n    role: recovery_test\\n    result: running\\n  - exp_id: grpo_standard_20_fast\\n    role: baseline\\n    result: running\\n  - exp_id: mvp_rasp_pipeline_v4\\n    role: pruning_eval\\n    result: post-prune 29% vs 1%\\n  depends_on:\\n  - D006\\n  - D007\\n- id: D009\\n  date: 2026-05-14 21:39 UTC\\n  summary: GRPO 1024-token 截断伪阴性：不接受 negative 结论，诊断性 eval + 准备 2048 重跑\\n  rationale: grpo_rasp_20_fast 和 grpo_standard_20_fast 全程 clipped_ratio=1.0，0 个 completion\\n    自然终止。DeepSeek-R1 的 think 推理链在 sampling (temp=0.7) 下远长于 greedy，剪枝后模型更冗长。1024 tokens\\n    不足以产出完整答案，导致 reward=0、grad_norm=0，GRPO 无学习信号。这是配置问题不是方法问题。需先做诊断性 eval（1024 tokens\\n    + temp=0.7）确认截断假说，再用 max_completion=2048 重跑 GRPO。\\n  related_experiments:\\n  - exp_id: grpo_rasp_20_fast\\n    role: recovery_test\\n    result: inconclusive (truncation artifact)\\n  - exp_id: grpo_standard_20_fast\\n    role: baseline\\n    result: inconclusive (truncation artifact)\\n  depends_on:\\n  - D007\\n  - D008\\n- id: D010\\n  date: 2026-05-14 21:40 UTC\\n  summary: 审批 Option A：max_completion_length=4096 重跑 GRPO 双实验，其余参数不变\\n  rationale: RASP 模型 post-prune 29% accuracy 证明它能解题，1024 截断是唯一阻碍。Option A 最快验证（~7h），失败再追加\\n    SFT warmup（Option B）。不需要同时调 lr/epochs 增加变量。2 GPU 空闲中，立即启动。\\n  related_experiments:\\n  - exp_id: grpo_rasp_20_fast\\n    role: predecessor\\n    result: inconclusive (truncation)\\n  - exp_id: grpo_standard_20_fast\\n    role: predecessor\\n    result: inconclusive (truncation)\\n  depends_on:\\n  - D009\\n- id: D011\\n  date: 2026-05-14 22:56 UTC\\n  summary: 'D011: Kill standard GRPO 4096 (10步零梯度), 将GPU1转给RASP GRPO 4096立即启动'\\n  rationale: 'grpo_standard_20_4096 前10步: clipped_ratio=0.9938, grad_norm=0, completion_length=4089/4096,\\n    输出为重复数字无结构。Standard pruning 20%已摧毁模型生成连贯文本能力, GRPO无法恢复, 增加token长度无济于事。10步证据充分(与D009\\n    1024截断不同, 这次是能力丧失)。Kill后GPU1立即启动RASP GRPO 4096, 比等GPU0 baseline eval完成提前~2h。Standard\\n    10步数据保留为负对照证据。'\\n  related_experiments:\\n  - exp_id: grpo_standard_20_4096\\n    role: evidence\\n    result: 10步零梯度, clipped_ratio=0.99, 模型不可恢复\\n  - exp_id: grpo_rasp_20_4096\\n    role: next\\n    result: pending - MVP关键实验\\n  depends_on:\\n  - D010\\n  - D009\\n- id: D012\\n  date: 2026-05-14 22:56 UTC\\n  summary: 'D011: Kill grpo_standard_20_4096 early, start grpo_rasp_20_4096 on GPU1\\n    immediately'\\n  rationale: 10步数据确认Standard-pruned模型（1% accuracy）在4096 tokens下仍完全退化：clipped_ratio=0.9938,\\n    grad_norm=0, 输出为重复数字串。这不是截断问题而是模型本质退化，继续跑490步（~23h）不改变结论。Kill后释放GPU1立即启动RASP GRPO，比原计划（等GPU0\\n    baseline eval完成）提前~2h。Standard的失败本身是强力负对照：证明Standard pruning摧毁了GRPO恢复的前提条件。\\n  related_experiments:\\n  - exp_id: grpo_standard_20_4096\\n    role: negative_control\\n    result: 'confirmed unrecoverable at step 10: clipped_ratio=0.9938, grad_norm=0'\\n  - exp_id: grpo_rasp_20_4096\\n    role: mvp_critical\\n    result: pending launch on GPU1\\n  depends_on:\\n  - D009\\n  - D010\\n- id: D013\\n  date: 2026-05-14 23:33 UTC\\n  summary: 'D012: RASP GRPO 4096也零梯度, 根因是sampling下无EOS而非token长度. Kill后转SFT warmup→GRPO两阶段恢复'\\n  rationale: 'RASP模型greedy 29%但sampling(temp=0.7)下clipped_ratio=1.0/grad_norm=0/zero\\n    EOS. 剪枝破坏了概率分布导致sampling下无法收敛到EOS. GRPO依赖自主生成, 对严重剪枝模型先天不适用. SFT用teacher forcing可修复终止行为,\\n    然后GRPO在SFT基础上优化推理. 双GPU并行: RASP SFT + Standard SFT对照. SFT~2-3h, 比继续浪费24h GPU跑零梯度GRPO合理得多.\\n    Standard SFT预期仍然困难(1% accuracy残留能力极低), 将作为负对照.'\\n  related_experiments:\\n  - exp_id: grpo_rasp_20_4096\\n    role: evidence\\n    result: 10步零梯度, clipped_ratio=1.0, sampling下无EOS\\n  - exp_id: grpo_standard_20_4096\\n    role: evidence\\n    result: D011确认不可恢复\\n  depends_on:\\n  - D011\\n  - D010\\n- id: D014\\n  date: 2026-05-14 23:35 UTC\\n  summary: 'D014: MVP PASS — 接受 post-prune 29% vs 1% 作为充分证据，GRPO recovery 降为 Phase\\n    2'\\n  rationale: D008 MVP claim 允许 \\\"post-prune 和/或 post-recovery accuracy 显著优于 Standard\\\"。Post-prune\\n    RASP 29% vs Standard 1%（p<0.0001, matched params/sparsity）远超 p<0.05 门槛。GRPO 4096\\n    双模型均 100% 截断零梯度（D013），根因是 DeepSeek-R1 sampling+temp=0.7 推理链无 EOS，非假设失败。继续追加 token\\n    长度风险高且时间成本大（48h+）。SFT warmup→GRPO 作为 Phase 2 第一个实验继续推进，为 story 增色但不阻塞 MVP。EMNLP\\n    DDL 11 天，必须立即进入 research 阶段。\\n  related_experiments:\\n  - exp_id: grpo_rasp_20_4096\\n    role: evidence\\n    result: negative (truncation, but confirms RASP 5x reward vs Standard)\\n  - exp_id: grpo_standard_20_4096\\n    role: negative_control\\n    result: negative (killed D011)\\n  - exp_id: grpo_rasp_20_fast\\n    role: evidence\\n    result: inconclusive (D009 truncation)\\n  - exp_id: grpo_standard_20_fast\\n    role: negative_control\\n    result: inconclusive (D009 truncation)\\n  - exp_id: mvp_rasp_pipeline_v4\\n    role: primary\\n    result: RASP 29% vs Standard 1% post-prune\\n  depends_on:\\n  - D013\\n  - D010\\n  - D009\\n  - D008\\n- id: D015\\n  date: 2026-05-15 00:59 UTC\\n  summary: SFT 结果 Standard>RASP 不改变方向，立即启动 GRPO Stage 2 作为决定性实验\\n  rationale: SFT Standard 64% > RASP 57% 看似威胁核心假设，但：(1) SFT 是 Stage 1 warmup 不是核心测试；(2)\\n    Claim 3 本来就预测 SFT 和 GRPO 对剪枝策略的偏好不同——SFT 偏好 Standard 反而是 Claim 3 的证据；(3) 真正的决定性实验是\\n    GRPO Stage 2。如果 GRPO 也显示 Standard ≥ RASP 则需要 pivot，但在此之前不改变方向。两卡空闲，紧急启动 GRPO Stage\\n    2。\\n  related_experiments:\\n  - exp_id: sft_rasp_20\\n    role: evidence\\n    result: 57% accuracy on 100 samples\\n  - exp_id: sft_standard_20\\n    role: evidence\\n    result: 64% accuracy on 100 samples, exceeds RASP\\n  depends_on: []\\n- id: D016\\n  date: 2026-05-15 01:56 UTC\\n  summary: 'D016: Dream dream_20260514T233950 分析完成。Best=4/6, Median=3/6, Worst=3/6。5\\n    个确认行动项 + 3 个观察项。加入 plan_015(α ablation P0), plan_016(inference speedup P1), plan_017(unstructured\\n    baseline P1)，扩展 plan_006 到 5 seeds。'\\n  rationale: 三档一致的结构性问题：α ablation(Critical×3)、single model、no inference speedup、multi-seed不足、scope\\n    overclaim。两档一致：missing related work(FANG/FuncNet)、CKA justification、unstructured\\n    baseline、per-layer floor confound。数据依赖项(RASP vs GRASPrune ranking、CKA predictivity)等\\n    GRPO 结果决定。Dream best case 可达 Weak Accept，但需要上述修补。不降级 venue 目标。\\n  related_experiments:\\n  - exp_id: grpo_stage2_rasp_20\\n    role: core\\n    result: RUNNING\\n  - exp_id: grpo_stage2_standard_20\\n    role: core\\n    result: RUNNING\\n  depends_on:\\n  - D015\\n- id: D017\\n  date: 2026-05-15 03:18 UTC\\n  summary: 'D017: Kill GRPO Stage 2 并以优化参数重启。max_completion_length 4096→1024, max_samples\\n    2000→1000。当前速度 38 天完成不可行（deadline 10 天），SFT 后 EOS 已修复使缩短 completion 安全。'\\n  rationale: GRPO Stage 2 每 step 1h51m，500 steps 需 38 天，远超 10 天 deadline。根因是 4096\\n    max_completion_length 的 generation 瓶颈。SFT warmup 后 EOS rate 99%、avg completion\\n    176 tokens，4096 是 SFT 前的防御性设置现已不需要。1024 提供 5.8x 平均长度的 headroom。max_samples 从 2000\\n    降到 1000 进一步缩短训练时间，1000 prompts 对 GRPO 足够。num_generations 需 Agent 确认当前值（W&B 显示\\n    4，Agent 说默认 8），如已是 4 则保持。预估加速到 ~2.4 天。\\n  related_experiments:\\n  - exp_id: grpo_stage2_rasp_20\\n    role: target\\n    result: RUNNING - too slow\\n  - exp_id: grpo_stage2_standard_20\\n    role: target\\n    result: RUNNING - too slow\\n  depends_on:\\n  - D015\\n  - D016\\n- id: D018\\n  date: 2026-05-15 05:45 UTC\\n  summary: 'D018: Reviewer 发现 Redundancy Paradox 叙事逻辑矛盾 + GQA=0 + Claim 2 scope 限定。intro\\n    说\\\"保留高 overlap\\\"但公式是\\\"剪掉高 overlap\\\"。20% sparsity 下仅 MLP 组被剪(0/112 attention GQA groups)，Claim\\n    2 scope 限定为 MLP groups。'\\n  rationale: Reviewer 深度分析发现：(1) introduction.tex L17 与 method.tex L79 矛盾——intro 称\\n    RASP 保留高 overlap 结构，但公式 S(h)=I(h)×(1-F)^α 明确惩罚高 F（高 overlap → 低 S → 被剪）。method.tex\\n    正确。(2) CKA 数据证实 MLP overlap ∈[0.879,0.997]，(1-F)^α 压缩到 Attn 的 1/5~1/50，使全局排序下\\n    MLP 必然被优先剪。(3) Claim 2 说 F(h) predicts recoverability，但在 20% sparsity 下只有 MLP\\n    groups 验证了这一点。需修正 intro + scope 限定 Claim 2 + 论文诚实交代剪枝分布。\\n  related_experiments:\\n  - exp_id: grpo_stage2_rasp_20_v2\\n    role: affected\\n    result: running\\n  - exp_id: grpo_stage2_standard_20_v2\\n    role: affected\\n    result: running\\n  depends_on:\\n  - D016\\n  - D017\\n- id: D019\\n  date: 2026-05-15 07:40 UTC\\n  summary: 'D019: Kill GRPO v2（双组 grad_norm=0 confirmed collapse），启动 v3：max_completion_length=2048\\n    + format_reward + β=0.01 + gradient_checkpointing。重跑 SFT Standard（checkpoint 已删）。'\\n  rationale: Step 30 数据独立验证 collapse：RASP grad_norm=0 + reward 停滞 0.0125，Standard\\n    grad_norm=0。继续 v2 浪费 ~24h GPU。v3 三项修改针对根因（reward signal 稀疏）：2048 token 给更多生成空间，format\\n    reward 提供中间梯度信号，β=0.01 防漂移。gradient_checkpointing 解决 OOM 风险。sft_standard_20 被磁盘清理删除，需重训\\n    ~40min。\\n  related_experiments:\\n  - exp_id: grpo_stage2_rasp_20_v2\\n    role: killed\\n    result: collapse\\n  - exp_id: grpo_stage2_standard_20_v2\\n    role: killed\\n    result: collapse\\n  depends_on:\\n  - D017\\n- id: D020\\n  date: 2026-05-15 08:06 UTC\\n  summary: v2 全失败，合并 D019+Agent 诊断设计 v3 最终参数；拒绝 SFT-only fallback\\n  rationale: v2 双组 step 30 grad_norm=0 collapse，根因：(1) max_completion_length=1024\\n    导致 RASP 98% truncated，学习信号极弱；(2) sampling temp=0.7 下 SFT 模型退化为重复循环。v3 合并两路修复：D019\\n    的 2048/beta=0.01/dapo + Agent 的 temp 降低/repetition_penalty。拒绝 SFT-only story(Option\\n    C)——GRPO 未在公平条件下测试，结论 premature。\\n  related_experiments:\\n  - exp_id: grpo_stage2_rasp_20_v2\\n    role: evidence\\n    result: 'negative: grad_norm=0 at step 30, 98% truncated'\\n  - exp_id: grpo_stage2_standard_20_v2\\n    role: evidence\\n    result: 'negative: grad_norm=0 at step 30, 73-82% truncated'\\n  depends_on: []\\n- id: D021\\n  date: 2026-05-15 08:48 UTC\\n  summary: 'D023: 核心数据可信度危机——紧急重新 eval post-prune 模型验证 29% vs 1%'\\n  rationale: α ablation 显示 α=0.0 (=Standard) 得到 30%，与原始 Standard 1% 矛盾 29pp。Reviewer\\n    假说：旧版 eval 脚本用 from_pretrained 加载剪枝模型导致权重 reinit→1% 是 artifact。如果成立，核心 claim 基础崩塌。优先级高于所有其他实验。\\n  related_experiments:\\n  - exp_id: mvp_rasp_pipeline_v4\\n    role: 原始 Standard 1% 数据来源\\n    result: 1% 可能是 eval bug artifact\\n  - exp_id: grpo_stage2_rasp_20_v3\\n    role: 基于核心 claim 的下游实验\\n    result: FAILED (ref_model crash)\\n  depends_on:\\n  - D020\\n  - D014\\n- id: D022\\n  date: 2026-05-15 09:22 UTC\\n  summary: 'D025: GRPO v4 ETA 120h 不可接受，减 max_completion_length 重启 + α=4.0 边际显著需紧急验证'\\n  rationale: GRPO v4 每步 29min×250=120h=5天，DDL 仅 10 天。不 kill 但需优化：max_completion_length\\n    2048→512（SFT 平均输出 180 tokens），预计 2-4x 加速。同时探索 vLLM 可行性。α=4.0 (40%) vs α=0.0 (30%)\\n    边际显著 p≈0.05，如果确认则 CKA 核心贡献成立（极端加权有效），但需 N=500+ 和 512 calibration 确认。\\n  related_experiments:\\n  - exp_id: grpo_stage2_rasp_20_v4\\n    role: 120h ETA, 需优化重启\\n    result: step 1/250, 29min/step\\n  - exp_id: mvp_rasp_pipeline_v4\\n    role: α ablation 来源\\n    result: α=4.0 40% vs α=0.0 30%\\n  depends_on:\\n  - D023\\n- id: D023\\n  date: 2026-05-15 10:09 UTC\\n  summary: α ablation Phase A 暴露 importance formula confound 风险，暂缓 framing 调整等 Phase\\n    B + formula 验证\\n  rationale: α=0.0（纯 importance 无 CKA）post-prune 30% ≈ α=2.0 的 29%，而 Standard 仅 1%。28pp\\n    差距可能来自 importance scoring 实现差异而非 CKA。但 post-prune 不等于 post-recovery——Phase B SFT\\n    结果才是 recoverability claim 的决定性证据。同时派 Agent 验证两种 mode 的 importance formula 是否相同。在两项证据到齐前不调整\\n    framing。α=4.0（40%）作为 backup 主结果候选。\\n  related_experiments:\\n  - exp_id: alpha_ablation_phase_a\\n    role: evidence\\n    result: α=0.0:30%, α=0.5:25%, α=1.0:27%, α=2.0:29%, α=4.0:40% (post-prune)\\n  depends_on: []\\n- id: D024\\n  date: 2026-05-15 10:11 UTC\\n  summary: 'CRITICAL: D023 re-eval 显示 Standard post-prune ~32% 而非原始 1%，部署三路排查确定根因'\\n  rationale: D023 re-eval 中间结果 pruned_standard_20 准确率 32%（50/100 samples），与 α=0.0\\n    post-prune 30% 交叉验证一致。原始 1% 极可能是 eval bug（代码今天有更新，可能修复了 non-uniform MLP 加载）。如果确认，\\\"RASP\\n    29% vs Standard 1%\\\" 核心 claim 不成立。三路紧急排查：(1) eval 代码 git diff (2) westb 当前代码 re-eval\\n    原始模型 (3) re-eval pruned_rasp_20。暂不调整 framing，等排查结果 + Phase B SFT recovery 数据。\\n  related_experiments:\\n  - exp_id: D023\\n    role: trigger\\n    result: re-eval pruned_standard_20 中间结果 32% vs 原始 1%\\n  - exp_id: alpha_ablation_phase_a\\n    role: cross_validation\\n    result: α=0.0 post-prune 30% ≈ re-eval 32%\\n  depends_on:\\n  - D023\\n- id: D025\\n  date: 2026-05-15 11:02 UTC\\n  summary: 挂起 D006/D014 基于 \\\"29x advantage\\\" 的所有结论，等待 definitive re-eval 数据\\n  rationale: Reviewer 确认 pruned_standard_20 原始 1% accuracy 是 eval bug（max_new_tokens=10\\n    截断）。Definitive re-eval 中间结果 (50/100) 显示 standard accuracy ~28%，与 α=0.0 ablation\\n    (30%) 交叉验证一致。原始 RASP 29% 也用了同样有 bug 的代码，真实值未知。如果 RASP re-eval 也是 ~28-30%，\\\"RASP\\n    29% vs Standard 1%\\\" 核心 claim 完全不成立。所有基于该 advantage 的下游决策需挂起直到两个 definitive re-eval\\n    (N=100, max_new_tokens=4096, greedy) 全部完成。\\n  related_experiments:\\n  - exp_id: D023\\n    role: trigger\\n    result: 'intermediate: standard_20 accuracy ~28% at 50/100 samples'\\n  - exp_id: D006\\n    role: suspended\\n    result: conclusions based on buggy eval data\\n  - exp_id: D014\\n    role: suspended\\n    result: conclusions based on buggy eval data\\n  depends_on:\\n  - D006\\n  - D014\\n- id: D026\\n  date: 2026-05-15 11:04 UTC\\n  summary: 将 RASP definitive re-eval 部署到 westd GPU 0 并行执行，不等 westb Standard re-eval\\n    完成\\n  rationale: westd 双卡空闲是资源浪费。数据可信度危机需要尽快拿到 RASP 和 Standard 两个 definitive re-eval 结果来判断核心\\n    claim 是否成立。并行跑可节省 ~1h 等待时间。同时利用 westd GPU 1 恢复 α ablation Phase B 剩余训练。\\n  related_experiments:\\n  - exp_id: reeval_postprune_definitive\\n    role: primary\\n    result: Standard 中间结果 28%，RASP 待跑\\n  depends_on:\\n  - D023\\n- id: D027\\n  date: 2026-05-15 11:37 UTC\\n  summary: Post-prune 核心 claim 崩塌（RASP 31% vs Standard 27%, p>>0.05）。暂不 pivot，等 GRPO\\n    v5 决定性结果\\n  rationale: Definitive re-eval 证实原始 29x advantage 完全由 eval bug 造成。D006/D014/D015\\n    决策链数据基础失效。但 GRPO v5（step 50/250, ~5h）是唯一仍可能验证\\\"CKA-guided pruning 创造更好 recovery\\n    dynamics\\\"假设的实验。SFT 方向已否定（Standard 64% > RASP 57%）。Pivot 判据：|GRPO_RASP - GRPO_Standard|\\n    < 5pp → 全面 pivot；5-10pp → 降级 claim；>10pp → story 转为 recovery-pathway 假设。westd\\n    空闲卡派 GraSP baseline + α ablation 重验证，无论 pivot 与否都有价值。\\n  related_experiments:\\n  - exp_id: reeval_postprune_definitive\\n    role: definitive\\n    result: RASP 31% vs Standard 27%, 4pp 不显著\\n  - exp_id: grpo_stage2_rasp_20_v5\\n    role: decisive_pending\\n    result: step 50/250 运行中\\n  depends_on:\\n  - D023\\n  - D026\\n- id: D028\\n  date: 2026-05-15 12:40 UTC\\n  summary: 'Kill GRPO v5 (RASP+Standard)，切 v6: max_completion_length 512→1024'\\n  rationale: v5 训练崩溃：reward step 40 达峰 0.033 后归零，grad_norm 坍塌到 0.01，clipped_ratio\\n    93-97.5%。根因是 512 tokens 太短导致 R1 distill 模型无法完成推理链→无正确答案→无 reward→无梯度。Standard\\n    v5 参数相同会遇到同样问题。切 1024 tokens 平衡速度（~5 min/step vs v4 29 min/step）和信号质量。双卡同时起 RASP\\n    v6 + Standard v6 保持对照并行。\\n  related_experiments:\\n  - exp_id: grpo_stage2_rasp_20_v5\\n    role: killed\\n    result: reward 归零, grad_norm 坍塞, clipped_ratio 97.5%\\n  - exp_id: grpo_stage2_standard_20_v5\\n    role: killed_before_signal\\n    result: 参数相同会遇同样问题\\n  depends_on:\\n  - D027\\n- id: D029\\n  date: 2026-05-15 13:46 UTC\\n  summary: SFT recovery 阶段 Standard 优于 RASP/α=4.0，核心假设在 SFT 层面也未得到支持\\n  rationale: 'Post-SFT: Standard 64% > α=4.0 62% > RASP 57%。Recovery Δ: Standard +37pp\\n    > RASP +26pp > α=4.0 +22pp。Standard 起点最低但恢复最多，与\\\"RASP 保留更可恢复结构\\\"叙事矛盾。Post-prune\\n    和 Post-SFT 两个阶段均未支持核心假设。GRPO v6 对照实验（westb 双卡运行中，ETA ~21h）是最后的验证机会——RL 训练可能展现与\\n    SFT 不同的 recovery dynamics。若 GRPO 也无差异，项目需根本性 pivot。'\\n  related_experiments:\\n  - exp_id: sft_alpha4_0_westd\\n    role: evidence\\n    result: Post-SFT 62%, recovery +22pp\\n  - exp_id: sft_standard_20_retrain\\n    role: evidence\\n    result: Post-SFT 64%, recovery +37pp\\n  - exp_id: grpo_stage2_rasp_20_v6\\n    role: decisive_pending\\n    result: running\\n  - exp_id: grpo_stage2_standard_20_v6\\n    role: decisive_pending\\n    result: running\\n  depends_on:\\n  - D027\\n  - D028\\n- id: D030\\n  date: 2026-05-15 14:02 UTC\\n  summary: 'GRPO v6 双卡 OOM 崩溃(step 8)，切 v7: 8-bit optimizer + 100 steps 抢时间'\\n  rationale: v6 在 step 8 首次分配 full optimizer state 时 OOM（model+ref_model+optimizer\\n    > 95GB）。用户告知只剩几小时，v7 用 AdamW8bit 节省 ~50% optimizer 显存，steps 缩减到 100（~3.5h）以在时间窗口内出结果。这是决定性实验，必须在服务器到期前完成。\\n  related_experiments:\\n  - exp_id: grpo_stage2_rasp_20_v6\\n    role: predecessor\\n    result: OOM step 8\\n  - exp_id: grpo_stage2_standard_20_v6\\n    role: predecessor\\n    result: OOM step 8\\n  depends_on:\\n  - D028\\n- id: D031\\n  date: 2026-05-15 14:04 UTC\\n  summary: 'GRPO v6 OOM at step 8, 切 v7: 8-bit AdamW optimizer + 100 steps (~3.5h)'\\n  rationale: v6 在 step 8 optimizer state 分配时 OOM 崩溃（max_completion_length=1024 的 KV\\n    cache + Adam FP32 states 超出 ~98GB VRAM）。v7 改用 AdamW8bit（bitsandbytes）减少 optimizer\\n    memory ~75%，steps 从 250 缩到 100——v5 在 step 40-80 已展现完整 learning/collapse 曲线，100\\n    steps 足以判断 RASP vs Standard 是否有差异。~3.5h 完成时间适配 deadline 压力。其余参数不变：max_completion_length=1024,\\n    beta=0.01, temp=0.4, rep_penalty=1.15, format_reward=0.1, gradient_checkpointing=True。\\n  related_experiments:\\n  - exp_id: grpo_stage2_rasp_20_v6\\n    role: OOM_failure\\n    result: OOM at step 8\\n  - exp_id: grpo_stage2_standard_20_v6\\n    role: OOM_failure\\n    result: OOM at step 8\\n  depends_on:\\n  - D028\\n- id: D032\\n  date: 2026-05-15 14:31 UTC\\n  summary: 'GRPO v7 双组崩溃(磁盘满+静默死亡)，v8 修复: HF cache 迁移数据盘 + GPU 映射修正 + 顺序启动'\\n  rationale: 'v7 Standard 因 HF datasets cache 写入根分区(30GB)导致瞬时磁盘满崩溃；RASP v7 静默死亡(疑同根因)。修复:\\n    (1) HF_DATASETS_CACHE/HF_HOME 指向 /root/autodl-tmp/.hf_cache 避免根分区写入 (2) Standard\\n    GPU 映射从 --gpu 1 改为 CUDA_VISIBLE_DEVICES=1 + --gpu 0 (3) 顺序启动确认稳定性。GRPO v1-v7 连续\\n    7 版失败均为工程问题(截断/collapse/OOM/磁盘满)而非算法问题，核心假设验证路径不变。'\\n  related_experiments:\\n  - exp_id: grpo_stage2_rasp_20_v7\\n    role: failed\\n    result: silent death, no logs\\n  - exp_id: grpo_stage2_standard_20_v7\\n    role: failed\\n    result: No space left on device at dataset loading\\n  depends_on:\\n  - D031\\n- id: D033\\n  date: 2026-05-15 16:22 UTC\\n  summary: α ablation SFT 差异统计不显著，GRPO v8 为唯一 pivot-or-publish 判据；GraSP 提升为 core finding\\n  rationale: Reviewer 统计分析：N=100 下 Standard 64% vs RASP 57% p=0.31 不显著，所有 α 变体 post-SFT\\n    结果统计不可区分。三个核心 claim (C1/C3) 全部系于 GRPO v8 单一实验。GraSP 7% vs RASP 31% 是唯一 p<0.001\\n    对比，应从 baseline 提升为 core comparative finding。批准 full N=1319 eval 解决统计功效问题。framing\\n    调整待 GRPO v8 step 10 早期信号后决定。\\n  related_experiments:\\n  - exp_id: eval-sft-alpha-0p0\\n    role: evidence\\n    result: 64% post-SFT\\n  - exp_id: eval-sft-alpha-1p0\\n    role: evidence\\n    result: 57% post-SFT\\n  - exp_id: sft_alpha4_0_westd_retry\\n    role: evidence\\n    result: 62% post-SFT\\n  - exp_id: grasp_baseline_westd\\n    role: evidence\\n    result: 7% post-prune\\n  - exp_id: grpo_stage2_rasp_20_v8\\n    role: pivot_dependency\\n    result: running\\n  - exp_id: grpo_stage2_standard_20_v8\\n    role: pivot_dependency\\n    result: running\\n  depends_on: []\\n- id: D034\\n  date: 2026-05-15 16:25 UTC\\n  summary: GraSP post-SFT 41% (p=0.001) 确认为论文核心 finding；α=0.5 跳过不重跑；SFT 侧 α 趋势不成立\\n  rationale: GraSP post-SFT 41% vs Standard 64% p=0.001，vs RASP 57% p=0.024，是唯一统计显著的\\n    pruning criterion 对比。α=2.0 post-SFT 62% 加入后，之前的\\\"α 越大 SFT 越差\\\"判断不再成立（62/62/64 不可区分，57%\\n    可能是 outlier）。α=0.5 checkpoint 损坏，但四点已足够，不值得重跑。SFT 侧任何 α 相关 claim 放弃，GraSP contrast\\n    提升为 core finding。\\n  related_experiments:\\n  - exp_id: eval_sft_grasp_20\\n    role: core_finding\\n    result: 41% post-SFT, p=0.001 vs Standard\\n  - exp_id: eval-sft-alpha-2p0\\n    role: evidence\\n    result: 62% post-SFT\\n  - exp_id: eval-sft-alpha-0p5\\n    role: dropped\\n    result: CRASH - safetensors corrupted\\n  depends_on:\\n  - D033\\n- id: D035\\n  date: 2026-05-15 17:08 UTC\\n  summary: GRPO v8 RASP collapse at step 20；不 kill，跑到 step 50 观察 Standard 是否也 collapse\\n  rationale: RASP v8 grad_norm≈0, frac_zero_std=0.9，与 v2/v5 同模式。Standard 暂时健康但 frac_zero_std\\n    上升中。需要区分两种情况：(a) 双方都 collapse = GRPO 对剪枝模型普遍失效（方法论贡献），(b) 只有 RASP collapse = CKA-aware\\n    pruning 反而损害 GRPO recovery（需 pivot）。step 50 checkpoint 是决策点。\\n  related_experiments:\\n  - exp_id: grpo_stage2_rasp_20_v8\\n    role: pivot_signal\\n    result: collapse at step 20\\n  - exp_id: grpo_stage2_standard_20_v8\\n    role: monitoring\\n    result: healthy but frac_zero_std rising\\n  depends_on:\\n  - D033\\n  - D034\\n- id: D036\\n  date: 2026-05-15 17:12 UTC\\n  summary: RASP step 30 硬性 kill 门槛设定；unpruned baseline GRPO 作为最高优先级 contingency\\n  rationale: Reviewer 独立确认 RASP collapse 不可逆（v2/v5/v8 三版同模式）。Step 30 kill 条件：grad_norm<0.05\\n    OR frac_zero_std≥0.85 OR reward<0.03。释放的 GPU 第一优先级跑 unpruned baseline GRPO——Reviewer\\n    指出这是 claim \\\"GRPO 对剪枝模型失效\\\"的必需证据。如果 v8 双 collapse 确认，不再出 v9，转而将 GRPO 失败作为 Claim\\n    3 证据（recovery pathway matters），前提是 unpruned GRPO 正常工作。\\n  related_experiments:\\n  - exp_id: grpo_stage2_rasp_20_v8\\n    role: kill_candidate\\n    result: collapse, step 30 kill check\\n  - exp_id: grpo_stage2_standard_20_v8\\n    role: monitoring\\n    result: frac_zero_std rising\\n  - exp_id: unpruned_baseline_grpo\\n    role: planned_contingency\\n    result: pending\\n  depends_on:\\n  - D035\\n- id: D037\\n  date: 2026-05-15 18:38 UTC\\n  summary: 'Narrative pivot: tentatively adopt \\\"Pruning for Plasticity\\\" (A), hold\\n    \\\"Recovery Method Conditions Pruning\\\" (B) as contingency pending Standard GRPO\\n    v8 result'\\n  rationale: RASP GRPO 3次连续 collapse (v2/v5/v8) 直接否定原核心假设 \\\"CKA-aware pruning preserves\\n    RLVR-recoverable structures\\\"。Narrative A 有最强的机制解释（冗余=可塑性缓冲）和新颖性，但依赖 Standard GRPO\\n    v8 成功。若 Standard 也 collapse → 退到 Narrative B（pruning×recovery 交互效应）。不在 Standard\\n    v8 完成前重写 paper_framing.md。\\n  related_experiments:\\n  - exp_id: grpo_rasp_20_v8\\n    role: trigger\\n    result: collapse (grad_norm=0.011, frac_zero_std=0.90)\\n  - exp_id: grpo_rasp_20_v5\\n    role: supporting\\n    result: collapse\\n  - exp_id: grpo_rasp_20_v2\\n    role: supporting\\n    result: collapse\\n  - exp_id: grpo_stage2_standard_20_v8\\n    role: pending_critical\\n    result: RUNNING step 30/100 HEALTHY\\n  depends_on: []\\n- id: D038\\n  date: 2026-05-15 18:38 UTC\\n  summary: 'Narrative pivot: 暂定 Narrative A (Pruning for Plasticity)，B 作 contingency，等\\n    Standard GRPO v8 + unpruned baseline 结果再正式改 framing'\\n  rationale: RASP GRPO 3次连续 collapse 否定原核心假设。Narrative A 机制解释最强（冗余=可塑性缓冲），但依赖 Standard\\n    GRPO 成功。若 Standard 也 collapse → fallback 到 B（recovery method × pruning strategy\\n    交互效应）。不提前改 paper_framing.md，避免基于未确认结果做不可逆改动。\\n  related_experiments:\\n  - exp_id: grpo_rasp_20_v8\\n    role: primary_evidence\\n    result: collapse (3rd consecutive)\\n  - exp_id: grpo_stage2_standard_20_v8\\n    role: pending_pivotal\\n    result: running step 30/100 healthy\\n  - exp_id: grpo_unpruned_baseline\\n    role: pending_control\\n    result: running step 0/100\\n  depends_on: []\\n- id: D039\\n  date: 2026-05-15 19:32 UTC\\n  summary: Unpruned GRPO collapse invalidates \\\"pruning causes collapse\\\" premise; collapse\\n    ordering (RASP→Unpruned→Standard) becomes new core evidence; hold narrative commitment\\n    until Standard v8 completes\\n  rationale: Unpruned baseline GRPO 在 step 80 collapse (reward=0, frac_zero_std=1.0)，证明\\n    collapse 不是剪枝导致。但 collapse 顺序极其有意义：RASP (step ~10) → Unpruned (step ~80) → Standard\\n    (step 30+ still learning, reward 0.061+)。如果 Standard 完成 100 步不 collapse，story\\n    变为\\\"importance-based pruning stabilizes RLVR\\\"——比原 Narrative A 更 counterintuitive\\n    也更有力。Narrative A 被削弱但未完全否定（RASP 加速 collapse 的机制解释仍成立）。暂不重写 framing，等 Standard\\n    v8 的最终结果。\\n  related_experiments:\\n  - exp_id: grpo_unpruned_baseline\\n    role: trigger\\n    result: NEGATIVE - collapse at step 80, peak reward 0.044\\n  - exp_id: grpo_stage2_standard_20_v8\\n    role: pending_critical\\n    result: RUNNING step 30+, reward 0.061+ still rising\\n  - exp_id: grpo_rasp_20_v8\\n    role: supporting\\n    result: collapse at step ~10\\n  depends_on:\\n  - D037\\n- id: D040\\n  date: 2026-05-15 19:34 UTC\\n  summary: Unpruned baseline 判定无效，需重新设计为 SFT→GRPO 流程\\n  rationale: grpo_unpruned_baseline 100步训练完全无效：step 10 KL=47.57（正常应<0.01），补全从 step\\n    1 就是乱码，frac_zero_std≥0.95。根因：未剪枝模型未经 SFT 直接进 GRPO，而 Standard/RASP 都经过了 SFT，导致不公平对比且\\n    ref_model 加载路径可能不一致。正确做法：SFT unpruned → GRPO unpruned，与剪枝流程对齐。优先级低于 Standard v8\\n    完成和 westd eval，等 GPU 空闲后安排。\\n  related_experiments:\\n  - exp_id: grpo_unpruned_baseline\\n    role: invalid_baseline\\n    result: KL=47.57, garbled output, training meaningless\\n  depends_on: []\\n- id: D041\\n  date: 2026-05-15 19:37 UTC\\n  summary: Unpruned baseline 实验设计无效——缺少 SFT 步骤，不构成公平对照\\n  rationale: Reviewer 指出：Standard/RASP 在 GRPO 前经过 SFT warmup，而 unpruned baseline 直接用裸模型跑\\n    GRPO。KL=47.57（vs Standard 的 0.003）更可能是 SFT 缺失 + 加载路径不一致所致，而非 GRPO config 问题。Agent\\n    的结论\\\"collapse is GRPO config issue\\\"因果推断不成立。正确做法：SFT 后的未剪枝模型做 GRPO baseline。\\n  related_experiments:\\n  - exp_id: grpo_unpruned_baseline\\n    role: invalid baseline\\n    result: failed (disk full + design flaw)\\n  depends_on: []\\n- id: D042\\n  date: 2026-05-15 19:41 UTC\\n  summary: 暂不引用 GRPO collapse 因果结论——等 Standard v8 完成后对比三者 collapse timeline 再定性\\n  rationale: Reviewer 发现 collapse onset 差异巨大：RASP step~10 最早 collapse，Unpruned step~80，Standard\\n    step 40+ 仍健康（frac_zero_std=0.525 且下降）。如果 Standard v8 跑完不 collapse，正确结论变为\\\"剪枝方法显著影响\\n    GRPO 稳定性\\\"，这比\\\"GRPO config issue\\\"更有论文价值。同时 RASP 跨服务器 10pp 差异可能与 calibration 样本数（256\\n    vs 512）有关，plan_014（CKA reliability analysis）优先级应提升。\\n  related_experiments:\\n  - exp_id: grpo_unpruned_baseline\\n    role: reference - collapse at step 80\\n    result: failed (disk full)\\n  - exp_id: grpo_stage2_rasp_20_v8\\n    role: reference - collapse at step ~10\\n    result: negative\\n  - exp_id: grpo_standard_v8\\n    role: pending - step 40+ healthy, ETA step 100 ~10:30 UTC\\n    result: running\\n  depends_on:\\n  - D041\\n- id: D043\\n  date: 2026-05-15 22:06 UTC\\n  summary: Standard v8 step 60 确认 collapse。三模型全 collapse 时间线：RASP(10) < Standard(60)\\n    < Unpruned(80)。N=1319 SFT eval 无显著差异（p=0.248）。原始 RASP 优势假设不成立，需 pivot narrative。\\n  rationale: '1) SFT recovery: RASP 61.5% vs Standard 59.3%，Δ=2.2pp, p=0.248 不显著——CKA-based\\n    pruning 在 SFT recovery 上没有统计优势。2) GRPO stability: collapse 时间线与冗余保留完美负相关——RASP\\n    移除最多冗余最快 collapse，Standard 次之，Unpruned 最慢。这说明 CKA-based scoring 恰好移除了 GRPO 训练所需的冗余结构。3)\\n    Paper pivot 方向：从\\\"RASP enables better recovery\\\"转向\\\"pruning-trainability tradeoff\\\"——方法论贡献是分析框架，不是新\\n    SOTA。collapse timeline 是最强数据点。'\\n  related_experiments:\\n  - exp_id: grpo_stage2_standard_20_v8\\n    role: Standard collapse at step 60\\n    result: negative\\n  - exp_id: grpo_stage2_rasp_20_v8\\n    role: RASP collapse at step ~10\\n    result: negative\\n  - exp_id: grpo_unpruned_baseline\\n    role: Unpruned collapse at step ~80\\n    result: failed\\n  - exp_id: eval_sft_standard_full_westd\\n    role: Standard SFT 59.29%\\n    result: success\\n  - exp_id: eval_sft_rasp_full_westd\\n    role: RASP SFT 61.49%\\n    result: success\\n  depends_on:\\n  - D042\\n- id: D044\\n  date: 2026-05-16 01:41 UTC\\n  summary: 'Major narrative pivot: from \\\"RASP enables better RLVR recovery\\\" to \\\"GRPO\\n    fails on pruned models + collapse dynamics as diagnostic\\\"'\\n  rationale: 'Standard GRPO step-50 eval (N=1319) shows 58.91% accuracy vs SFT baseline\\n    59.29% — zero accuracy gain despite peak reward at step 40. GRPO doesn''t recover\\n    ANY pruned model. Original Claim 1 (RASP enables superior RLVR recovery) is falsified.\\n    New story: GRPO failure on pruned models is the main finding; collapse speed (RASP\\n    ~10, Standard ~60, Unpruned ~80) reveals redundancy-stability tradeoff; paper\\n    becomes diagnostic/analysis contribution.'\\n  related_experiments:\\n  - exp_id: eval_grpo_standard_step50_full\\n    role: falsified original Claim 1\\n    result: 58.91% post-GRPO vs 59.29% post-SFT\\n  - exp_id: grpo_stage2_standard_20_v8\\n    role: established Standard collapse at step 60\\n    result: peak reward step 40, collapse step 60\\n  - exp_id: grpo_stage2_rasp_20_v9\\n    role: running - will establish RASP collapse dynamics\\n    result: pending\\n  depends_on: []\\n- id: D045\\n  date: 2026-05-16 04:46 UTC\\n  summary: 'Core data complete: GRPO reward-accuracy decoupling universal, pruning\\n    causes collapse (severity gradient confirmed)'\\n  rationale: 'All three models show GRPO does not improve accuracy post-SFT (unpruned\\n    81.77% vs 81.27%, Standard 58.91% vs 59.29%, RASP 60.65% vs 61.49%). Pruning-specific\\n    effect is training collapse: RASP step ~10, Standard step ~60, Unpruned never.\\n    Paper narrative finalized as diagnostic/analysis contribution. Scope expansion\\n    to 25-30% sparsity + Qwen2.5-Math-7B planned.'\\n  related_experiments:\\n  - exp_id: eval_grpo_unpruned_v2_step100\\n    role: confirmed reward-accuracy decoupling for unpruned\\n    result: 81.77% vs SFT 81.27%\\n  - exp_id: eval_grpo_rasp_v9_step5\\n    role: confirmed no accuracy gain for RASP pre-collapse\\n    result: 60.65% vs SFT 61.49%\\n  - exp_id: grpo_unpruned_v2\\n    role: confirmed pruning-specificity of collapse\\n    result: 100 steps stable, no collapse, reward 0.661\\n  depends_on:\\n  - D044\\n- id: D046\\n  date: 2026-05-16 08:07 UTC\\n  summary: Qwen Math calibration=256 不重跑，论文加 footnote 说明差异\\n  rationale: 论文 claim 是跨模型现象存在性（collapse 是否发生 + severity gradient 是否复现），不是跨模型绝对数值对比。Calibration\\n    256 vs 512 导致 ~5% group selection 差异，但不影响 collapse/non-collapse 的定性判断。重跑需重新计算\\n    importance+CKA scores (~2h GPU) + 重新剪枝，收益不值得 DDL 压力下的时间成本。\\n  related_experiments:\\n  - exp_id: prune_rasp_20_qwen_math\\n    role: evidence\\n    result: sparsity 18.99%, 199 MLP groups\\n  - exp_id: prune_standard_20_qwen_math\\n    role: evidence\\n    result: sparsity 19.28%, 202 MLP groups\\n  depends_on:\\n  - D045\\n- id: D047\\n  date: 2026-05-16 09:36 UTC\\n  summary: 新增 RASP-RLVR 实验：反转 CKA scoring 保护冗余结构，预防 GRPO collapse\\n  rationale: 用户指出纯分析贡献竞争力有限。已证明冗余移除→collapse加速的单调关系，逻辑推论反转scoring（保护冗余）应防止collapse。成本低（复用现有scores，仅改公式符号）、风险低（单调关系已建立）、收益高（论文从analysis升级为diagnosis+remedy）。用户批准\\\"要做\\\"。\\n  related_experiments:\\n  - exp_id: grpo_stage2_rasp_20_v9\\n    role: motivation\\n    result: RASP removes redundancy → collapse step 10\\n  - exp_id: grpo_stage2_standard_20_v8\\n    role: motivation\\n    result: Standard neutral → collapse step 60\\n  - exp_id: grpo_unpruned_v2\\n    role: motivation\\n    result: Full redundancy → no collapse\\n  depends_on:\\n  - D044\\n  - D045\\n\", \"total_chars\": 33560, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6fb59575-ff70-4c53-b155-783d3c072069",
  "isSidechain": true,
  "promptId": "39eba513-b35c-4482-87e4-5618fcf0979e",
  "agentId": "a7fe9f34d2b39e51d",
  "type": "user",
  "uuid": "28bc68b7-061f-4ae8-8734-ec7443fd65db",
  "sourceToolAssistantUUID": "6fb59575-ff70-4c53-b155-783d3c072069",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "87456414-598d-4dd4-8776-aaed1b39d708",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-16T15:42:18.921Z_

Now let me look at the actual paper draft to see how the related work is written.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28bc68b7-061f-4ae8-8734-ec7443fd65db",
  "isSidechain": true,
  "agentId": "a7fe9f34d2b39e51d",
  "requestId": "req_011Cb6W7GgsgbsmZ2rMEeyM6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "54635262-e2dc-4a47-b4f6-3685f0d381dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "87456414-598d-4dd4-8776-aaed1b39d708",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DpKw3orcedU21Qb2N1BGfp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20445,
      "cache_read_input_tokens": 36683,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 20445,
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

_source line 21 · 2026-05-16T15:42:20.788Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01HrZ33Uiogrjigr3bdeSoF3`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54635262-e2dc-4a47-b4f6-3685f0d381dd",
  "isSidechain": true,
  "agentId": "a7fe9f34d2b39e51d",
  "requestId": "req_011Cb6W7GgsgbsmZ2rMEeyM6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e70dd4e6-3145-4e3b-8398-2c78d723258f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "87456414-598d-4dd4-8776-aaed1b39d708",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DpKw3orcedU21Qb2N1BGfp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20445,
      "cache_read_input_tokens": 36683,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 20445
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 119,
          "cache_read_input_tokens": 36683,
          "cache_creation_input_tokens": 20445,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 20445,
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

_source line 22 · 2026-05-16T15:42:20.818Z_

<details><summary>↩ Tool result · `toolu_01HrZ33Uiogrjigr3bdeSoF3`</summary>

```text
artifacts/dream_reports/dream_20260514T233950/best/paper.tex
artifacts/dream_reports/dream_20260514T233950/median/paper.tex
artifacts/dream_reports/dream_20260514T233950/worst/paper.tex
artifacts/_project/paper/table1_postprune.tex
artifacts/_project/paper/table2_recovery.tex
artifacts/tables/table2_recovery.tex
paper/backup/experiments.tex
paper/backup/introduction.tex
paper/backup/method.tex
paper/backup/related_work.tex
paper/abstract.tex
paper/conclusion.tex
paper/appendix.tex
artifacts/_project/paper/table3_alpha.tex
paper/method.tex
artifacts/_project/paper/method.tex
paper/related_work.tex
artifacts/_project/paper/related_work_3d75d5.tex
artifacts/_project/paper/related_work.tex
docs/paper/main.tex
docs/paper/appendix.tex
artifacts/_project/paper/introduction_4ad0ba.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/experiments.tex
paper/main.tex
paper/tables/table2_recovery.tex
paper/limitations.tex
artifacts/_project/paper/limitations.tex
paper/introduction.tex
artifacts/tables/table1_postprune.tex
paper/tables/table1_postprune.tex
paper/experiments.tex
artifacts/tables/table3_alpha.tex
paper/tables/table3_alpha.tex
artifacts/dream_reports/dream_20260515T140651/best/paper.tex
artifacts/dream_reports/dream_20260515T140651/median/paper.tex
artifacts/dream_reports/dream_20260515T140651/worst/paper.tex
docs/paper/related_work.tex
docs/paper/abstract.tex
docs/paper/conclusion.tex
docs/paper/introduction.tex
docs/paper/limitations.tex
docs/paper/method.tex
docs/paper/experiments.tex
artifacts/dream_reports/dream_20260516T144805/best/paper.tex
artifacts/dream_reports/dream_20260516T144805/median/paper.tex
artifacts/dream_reports/dream_20260516T144805/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e70dd4e6-3145-4e3b-8398-2c78d723258f",
  "isSidechain": true,
  "promptId": "39eba513-b35c-4482-87e4-5618fcf0979e",
  "agentId": "a7fe9f34d2b39e51d",
  "type": "user",
  "uuid": "74d58edd-58ee-4bcb-a3c2-c56e5216282b",
  "sourceToolAssistantUUID": "e70dd4e6-3145-4e3b-8398-2c78d723258f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "87456414-598d-4dd4-8776-aaed1b39d708",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T15:42:23.941Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BvVHttf3t385Dq817FUvkj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74d58edd-58ee-4bcb-a3c2-c56e5216282b",
  "isSidechain": true,
  "agentId": "a7fe9f34d2b39e51d",
  "requestId": "req_011Cb6W7e9TiSEsWgVyRWYfY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d451e558-cb25-4445-a0a1-11dcf8074893",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "87456414-598d-4dd4-8776-aaed1b39d708",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M4mrM3U5FBuRputsjfwYbs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 784,
      "cache_read_input_tokens": 57128,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 784,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 62,
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

_source line 24 · 2026-05-16T15:42:23.950Z_

<details><summary>↩ Tool result · `toolu_01BvVHttf3t385Dq817FUvkj`</summary>

```text
1	\section{Related Work}
2	\label{sec:related}
3	
4	\subsection{Structured Pruning of Large Language Models}
5	\label{sec:rw_pruning}
6	
7	Structured pruning removes entire architectural units---attention heads, MLP channels, or layers---to reduce model size while maintaining hardware-friendly dense computation.
8	LLM-Pruner~\citep{llmpruner2023} introduced dependency-aware structural pruning that respects inter-component coupling in transformer architectures.
9	Bonsai~\citep{bonsai2025} achieves competitive structured pruning using only forward passes, eliminating the need for gradient computation.
10	GRASPrune~\citep{graspprune2026} advances the state of the art with global gating that jointly prunes FFN channels and KV head groups under a unified budget constraint.
11	ShortGPT~\citep{shortgpt2024} and SliceGPT~\citep{slicegpt2024} target layer-level depth pruning, while Wanda~\citep{wanda2024} addresses unstructured weight sparsity---both complementary but orthogonal to the width-level structural pruning we study.
12	
13	For reasoning models specifically, RESP~\citep{resp2025} introduces self-reflective pruning using gradient-based importance on self-generated reasoning traces, achieving 81.3\% on GSM8K at 40\% structured sparsity without any recovery training.
14	SSGR~\citep{ssgr2025} shows that selective self-generated calibration with challenging, moderately-lengthy reasoning examples further improves pruning quality for reasoning LLMs.
15	\citet{llms2lrms2026} systematically compare width and depth pruning for reasoning-centric models, finding width pruning more robust to reasoning degradation but not studying RLVR recovery.
16	RAC~\citep{rac2025} demonstrates that chain-of-thought calibrated reconstruction dramatically improves unstructured and 2:4 semi-structured pruning but does not extend to full structural pruning.
17	\citet{doingmore2026} reveal that unstructured pruning can improve test-time scaling for reasoning while structured pruning degrades it, suggesting that \emph{which} structures are removed critically shapes recovery potential.
18	
19	A parallel line of work recognizes that \emph{functional structure} within networks should guide pruning decisions.
20	FANG~\citep{fang_2025} groups FFN neurons by functional roles via activation clustering and retains shared neurons to prevent cross-task accuracy loss, outperforming FLAP/OBC by 1.5--8.5\% at 30--40\% sparsity.
21	FuncNet~\citep{funcnet_2025} applies Independent Component Analysis (borrowed from neuroimaging) to decompose LLMs into functional networks and preserves key neurons within each.
22	Both share RASP's motivation of identifying functionally critical structures, but neither incorporates a recovery component: they optimize for immediate post-pruning accuracy rather than recoverability under a downstream training paradigm.
23	RASP differs from all the above in that it optimizes the pruning decision for post-RLVR recoverability: structures are scored not only by their importance but by whether their function can be redistributed across retained structures during reinforcement learning recovery.
24	
25	\subsection{Pruning-Aware Recovery and Re-training}
26	\label{sec:rw_recovery}
27	
28	Post-pruning recovery is essential at moderate to high compression ratios.
29	\citet{selfhealing2025} demonstrate that RLVR recovery restores pruned reasoning models to 95\%+ accuracy at 25\% compression, significantly outperforming SFT recovery (${\sim}$80\%).
30	This establishes RLVR as the preferred recovery paradigm for reasoning models, but Self-Healing treats the pruning method as a black box and tests only one compression ratio---it does not study whether the \emph{choice} of what to prune affects how well RLVR can recover.
31	
32	P\textsuperscript{2} Law~\citep{p2law2025} establishes scaling laws for post-training loss after pruning ($L \propto (1/\rho)^\gamma$), predicting recovery data requirements at a given compression ratio, but studies only continual pre-training rather than RLVR or SFT.
33	PASER~\citep{paser2025} optimizes which recovery \emph{data} to use through manifold learning and capability-aware budget allocation---complementary to RASP, which optimizes which \emph{structures} to prune for recoverability.
34	PAT~\citep{pat2025} shows that jointly considering pruning and fine-tuning objectives outperforms the sequential prune-then-finetune pipeline.
35	RestoreLCC~\citep{restorelcc_2025} proposes a plug-and-play recovery method that contrastively probes critical attention heads and injects lost activation components back into the pruned model, achieving consistent gains across pruning methods (NeurIPS 2025 Spotlight).
36	\citet{boiling_frog_2026} adopt an iterative prune-tune loop that gradually compresses reasoning models, avoiding abrupt performance collapse through incremental SFT recovery.
37	Both represent alternative recovery strategies; RASP is complementary in that it optimizes \emph{what} to prune for RLVR recoverability, whereas RestoreLCC optimizes \emph{how} to compensate after pruning and Boiling Frog optimizes the \emph{schedule} of pruning-recovery iterations.
38	
39	The Lottery Ticket Hypothesis~\citep{frankle2019lth} asks which subnetworks can train effectively from random initialization.
40	RASP extends this notion to what we term \emph{paradigm-conditioned trainability}: the optimal subnetwork to retain depends not only on the task but on the recovery paradigm (RLVR vs.\ SFT), as each paradigm imposes fundamentally different functional requirements on the retained architecture.
41	
42	\subsection{RLVR Training Dynamics}
43	\label{sec:rw_rlvr}
44	
45	Understanding how RLVR reshapes model representations is central to predicting which pruned structures are recoverable.
46	\citet{rlsqueezes2026} show that RLVR and SFT shape reasoning capabilities through fundamentally different mechanisms: RLVR \emph{compresses} incorrect reasoning trajectories via global exploration, while SFT \emph{expands} correct trajectories via local imitation.
47	This asymmetry provides the theoretical foundation for RASP---structures with high functional overlap are more amenable to RLVR's redistribution mechanism, as their function can be absorbed by similar retained structures during global policy optimization, whereas SFT's trajectory-imitation objective cannot achieve such redistribution.
48	OPSD~\citep{opsd2026} proposes a post-RL compaction stage that further compresses reasoning traces after RLVR training, reinforcing the view that RLVR-trained models exhibit compressible internal structure.
49	
50	\paragraph{CKA-based pruning.}
51	CKA~\citep{kornblith2019cka} has been previously applied to pruning, but at a fundamentally different granularity and with a different objective.
52	Among representation similarity measures (CCA, SVCCA, PWCCA, CKA), \citet{klabunde_similarity_survey_2025} show that CKA achieves 99.3\% layer identification accuracy versus 45.4\% for SVCCA, owing to its invariance to invertible linear transforms and isotropic scaling---properties critical for comparing heterogeneous structures (GQA groups vs.\ MLP channels) within the same layer.
53	MPruner~\citep{mpruner2024} uses \emph{inter-layer} CKA to cluster globally redundant layers for depth pruning in CNNs and general transformers, achieving up to 50\% parameter reduction by removing entire layers whose representations are similar to adjacent layers.
54	\citet{lachance2024cka} similarly apply CKA-based layer similarity for depth pruning of VGGNet.
55	Both operate at the \emph{layer} level, using CKA to identify which layers are redundant and can be removed with minimal accuracy loss.
56	In contrast, RASP uses \emph{intra-layer} CKA between individual GQA groups and MLP channels to predict per-structure recoverability under RLVR---a finer granularity (width vs.\ depth pruning) optimizing for a different objective (post-recovery reasoning performance vs.\ immediate accuracy preservation).
57	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d451e558-cb25-4445-a0a1-11dcf8074893",
  "isSidechain": true,
  "promptId": "39eba513-b35c-4482-87e4-5618fcf0979e",
  "agentId": "a7fe9f34d2b39e51d",
  "type": "user",
  "uuid": "6b96dd95-cb9f-4a91-a9e2-948008b7d884",
  "sourceToolAssistantUUID": "d451e558-cb25-4445-a0a1-11dcf8074893",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "87456414-598d-4dd4-8776-aaed1b39d708",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T15:42:24.269Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VL2FMDENZzupSQuuZvjNkG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b96dd95-cb9f-4a91-a9e2-948008b7d884",
  "isSidechain": true,
  "agentId": "a7fe9f34d2b39e51d",
  "requestId": "req_011Cb6W7e9TiSEsWgVyRWYfY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9efd4fab-5011-4483-af6b-39eb07e631f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "87456414-598d-4dd4-8776-aaed1b39d708",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M4mrM3U5FBuRputsjfwYbs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 784,
      "cache_read_input_tokens": 57128,
      "output_tokens": 161,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 784
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 161,
          "cache_read_input_tokens": 57128,
          "cache_creation_input_tokens": 784,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 784,
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

_source line 26 · 2026-05-16T15:42:24.275Z_

<details><summary>↩ Tool result · `toolu_01VL2FMDENZzupSQuuZvjNkG`</summary>

```text
1	\section{Introduction}
2	\label{sec:intro}
3	
4	Large language models trained with Reinforcement Learning with Verifiable Rewards (RLVR) achieve strong performance on mathematical and logical reasoning~\citep{deepseek2025r1,shao2024grpo}, but their parameter counts and extended chain-of-thought traces make deployment costly.
5	Structured pruning---removing entire attention heads or MLP channels---offers a hardware-friendly compression path that reduces both memory and latency without specialized sparse-computation support~\citep{llmpruner2023,graspprune2026}.
6	However, structured pruning at moderate sparsity severely degrades reasoning ability, necessitating a post-pruning recovery stage.
7	\citet{selfhealing2025} show that RLVR-based recovery substantially outperforms SFT-based recovery for pruned reasoning models, establishing RLVR as the preferred recovery paradigm.
8	
9	Despite this, current approaches treat pruning and recovery as independent steps: pruning methods optimize for immediate post-pruning accuracy~\citep{resp2025,graspprune2026,bonsai2025}, while recovery methods operate on whatever architecture they receive~\citep{selfhealing2025,paser2025}.
10	No prior work has studied whether the \emph{choice} of what to prune affects how well RLVR can subsequently recover reasoning---or whether this interaction differs from SFT-based recovery.
11	This gap is consequential because RLVR and SFT impose fundamentally different functional demands on the retained architecture: \citet{rlsqueezes2026} show that RLVR recovers through global exploration and path compression, while SFT recovers through local trajectory imitation.
12	The optimal set of structures to retain should therefore depend on the recovery paradigm.
13	
14	We hypothesize that \emph{functional overlap}---the degree to which a structure's computation is redundant with its within-layer peers---positively predicts RLVR recoverability.
15	If a pruned structure has high overlap with retained structures, RLVR can absorb its function through global policy optimization over the remaining architecture.
16	Conversely, structures with unique, non-redundant computations are difficult to recover once removed.
17	This yields what we term the \textbf{Redundancy Paradox}: counterintuitively, the structures most valuable to retain for post-RLVR recovery are not the most important ones, but the most \emph{functionally unique} ones.
18	Recovery-aware pruning therefore \emph{preferentially removes} important-but-redundant structures---whose high overlap means RLVR can redistribute their function across retained peers---while protecting functionally unique structures that, once removed, leave an irrecoverable gap.
19	Standard importance-only pruning, by contrast, protects high-importance structures regardless of redundancy, inadvertently removing unique structures whose function cannot be recovered.
20	
21	We propose \textbf{Recovery-Aware Structured Pruning (\rasp{})}, a three-stage framework that incorporates recoverability into the pruning decision.
22	In Stage~1, \rasp{} computes for each structure both a gradient-based importance score and a functional overlap score via intra-layer Centered Kernel Alignment (CKA;~\citealp{kornblith2019cka}).
23	In Stage~2, these are combined into a recovery-aware score $S(h) = I(h) \times (1 - F(h))^\alpha$ that protects structures which are both important \emph{and} functionally unique, while allowing removal of important-but-redundant structures whose function RLVR can redistribute.
24	In Stage~3, the pruned model undergoes a brief SFT warmup to restore generation competence, followed by GRPO-based RLVR recovery~\citep{shao2024grpo} to restore reasoning ability.
25	Unlike prior CKA-based pruning that uses inter-layer similarity for depth pruning~\citep{mpruner2024,lachance2024cka}, \rasp{} uses \emph{intra-layer} CKA between individual GQA groups and MLP channels to predict per-structure recoverability---a finer granularity optimizing for a fundamentally different objective.
26	
27	We evaluate \rasp{} on DeepSeek-R1-Distill-Qwen-7B~\citep{deepseek2025r1} at 20\% structured sparsity.
28	At matched sparsity, \rasp{}-pruned models retain 29\% GSM8K~\citep{cobbe2021gsm8k} accuracy immediately after pruning, compared to 1\% for importance-only pruning ($N{=}100$, $p{<}0.0001$)---a 28-percentage-point advantage attributable to the recovery-aware scoring criterion.
29	After SFT warmup, both pruning strategies recover substantially (57--64\%), with detailed comparison deferred to \S\ref{sec:experiments}.
30	[TBD: GRPO results]
31	
32	Our contributions are:
33	\begin{enumerate}[nosep,leftmargin=*]
34	    \item We identify the \emph{Redundancy Paradox}---that functional redundancy enables RLVR to recover the function of removed structures, making important-but-redundant structures safely removable while functionally unique structures become critical to retain---and formalize it through intra-layer CKA-based functional overlap scoring.
35	    \item We propose \rasp{}, a recovery-aware pruning framework that integrates functional overlap into structural pruning decisions, achieving 29\% post-prune GSM8K accuracy versus 1\% for importance-only pruning at matched 20\% sparsity on DeepSeek-R1-Distill-Qwen-7B.
36	    \item [TBD: GRPO recovery results---contribution demonstrating that \rasp{}'s post-prune advantage translates to superior post-RLVR reasoning performance.]
37	    \item We present preliminary evidence that the optimal pruning strategy may be conditioned on the recovery paradigm~\citep{frankle2019lth}, supporting the notion of \emph{paradigm-conditioned prunability} [TBD: pending GRPO confirmation and statistical validation].
38	\end{enumerate}
39	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9efd4fab-5011-4483-af6b-39eb07e631f8",
  "isSidechain": true,
  "promptId": "39eba513-b35c-4482-87e4-5618fcf0979e",
  "agentId": "a7fe9f34d2b39e51d",
  "type": "user",
  "uuid": "aa9f4feb-4452-449a-abb5-7aee32fe10f0",
  "sourceToolAssistantUUID": "9efd4fab-5011-4483-af6b-39eb07e631f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "87456414-598d-4dd4-8776-aaed1b39d708",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T15:42:28.643Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DHKDzY6LtmK2ZVcLMgxT5j`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa9f4feb-4452-449a-abb5-7aee32fe10f0",
  "isSidechain": true,
  "agentId": "a7fe9f34d2b39e51d",
  "requestId": "req_011Cb6W7twCmrMTLC14E9fnT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "522f7cf9-f749-4a61-ab9b-a3038b3a40f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "87456414-598d-4dd4-8776-aaed1b39d708",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018dyPmPFsBMFuTVRFLjtVr2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3942,
      "cache_read_input_tokens": 57912,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3942,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 64,
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

_source line 28 · 2026-05-16T15:42:28.648Z_

<details><summary>↩ Tool result · `toolu_01DHKDzY6LtmK2ZVcLMgxT5j`</summary>

```text
1	
2	\section{Experiments}
3	\label{sec:experiments}
4	
5	\subsection{Experimental Setup}
6	\label{sec:exp_setup}
7	
8	\paragraph{Base model.}
9	We evaluate \rasp{} on DeepSeek-R1-Distill-Qwen-7B~\citep{deepseek2025r1}, a 7B-parameter reasoning model built on the Qwen2.5 architecture~\citep{qwen2.5} with 28 transformer layers.
10	The model uses Grouped Query Attention (GQA;~\citealp{ainslie2023gqa}) with 28 query heads and 4 key-value heads per layer (group size $G{=}7$), and an MLP intermediate dimension of 18{,}944.
11	As a reasoning-distilled model whose chain-of-thought capabilities originate from reinforcement learning, it provides a direct testbed for studying how structural pruning interacts with RLVR-based recovery.
12	
13	\paragraph{Evaluation.}
14	We evaluate on GSM8K~\citep{cobbe2021gsm8k}, a benchmark of 1{,}319 grade-school math problems requiring multi-step arithmetic reasoning.
15	We report exact-match accuracy: the final numerical answer is extracted from the model's generation and compared against the ground truth.
16	For rapid iteration during development, we use a fixed 100-problem subset ($N{=}100$); final results use the full test set ($N{=}1{,}319$).
17	We define recovery $\Delta$ as the accuracy gain from post-prune to post-recovery, capturing how much reasoning ability the recovery pipeline restores independent of initial pruning damage.
18	
19	\paragraph{Hardware.}
20	All experiments run on a single node with 2$\times$ NVIDIA RTX PRO 6000 GPUs (94\,GB VRAM each).
21	The two pruning variants (Standard and \rasp{}) are trained in parallel on separate GPUs to ensure identical wall-clock conditions.
22	
23	\subsection{Pruning Configuration}
24	\label{sec:pruning_config}
25	
26	\paragraph{Sparsity and granularity.}
27	We apply 20\% structured sparsity by scoring and ranking both attention GQA groups (each comprising 1 KV head and 7 query heads) and MLP channel groups in a unified importance list; at 20\% sparsity, the global ranking preferentially removes MLP channel groups (200 of 784), with attention groups receiving higher importance scores and remaining intact.
28	The MLP intermediate dimension (18{,}944) is partitioned into 28 equal-sized groups of 676 channels each.
29	Structures are scored and ranked in a unified list across both component types, enabling cross-component pruning decisions.
30	At 20\% sparsity, 200 MLP channel groups are removed across 28 layers, totaling approximately 1.45 billion parameters (each group contributes $676 \times 3{,}584 \times 3 = 7{,}268{,}352$ parameters across gate, up, and down projections).
31	Both configurations remove 200 MLP channel groups at matched parameter budgets (${\sim}$1.45B parameters each), but differ in \emph{which} groups are selected---the central comparison of this work.
32	
33	\paragraph{Importance scoring.}
34	For each structure $h$, we compute Taylor-expansion importance $I(h)$ (Eq.~\ref{eq:importance}) using activations and gradients collected on 512 randomly sampled chain-of-thought examples from the GSM8K training set.
35	For GQA groups, we aggregate importance across the constituent query heads and KV head (Section~\ref{sec:stage1}).
36	
37	\paragraph{CKA-based functional overlap.}
38	We compute intra-layer linear CKA (Eq.~\ref{eq:cka}) between all pairs of GQA groups and between all pairs of MLP channel groups within each layer, using the same 512 calibration examples.
39	The functional overlap $F(h)$ for each structure is the mean pairwise CKA with its within-layer peers (Eq.~\ref{eq:overlap}).
40	
41	\paragraph{Recovery-aware scoring.}
42	The final pruning score $S(h) = I(h) \times (1 - F(h))^\alpha$ (Eq.~\ref{eq:score}) combines importance and functional overlap with $\alpha{=}1.0$.
43	Structures with the lowest $S(h)$ are pruned first, subject to the per-layer capacity floor.
44	
45	\paragraph{Per-layer capacity floor.}
46	To prevent representational collapse in individual layers, we enforce that each layer retains at least 40\% of its MLP channel groups (${\ge}12$ of 28 groups per layer).
47	During structure selection, candidates whose removal would violate this constraint are skipped in favor of the next lowest-scoring structure.
48	This constraint is necessary because unconstrained global ranking at 20\% sparsity concentrates pruning in layers with uniformly high functional overlap, collapsing those layers' capacity.
49	
50	\paragraph{Baseline: Standard importance-only pruning.}
51	As the primary baseline, we apply the same Taylor-expansion importance scoring and global ranking but without the CKA overlap penalty ($\alpha{=}0$ in Eq.~\ref{eq:score}), following LLM-Pruner~\citep{llmpruner2023}.
52	The same per-layer capacity floor and sparsity target are applied, ensuring that the only difference between Standard and \rasp{} is the head selection criterion.
53	
54	\subsection{Recovery Pipeline}
55	\label{sec:recovery_pipeline}
56	
57	After pruning, we apply a two-stage recovery pipeline (Section~\ref{sec:stage3}) consisting of SFT warmup followed by GRPO-based RLVR.
58	
59	\paragraph{Stage 3a: SFT warmup.}
60	Structured pruning destroys the model's ability to generate EOS tokens, causing unterminated repetitive outputs that prevent GRPO from computing rewards.
61	We restore generation competence with a brief SFT phase on 7{,}473 chain-of-thought examples (the full GSM8K training set), trained for 2 epochs (1{,}870 gradient steps) with teacher forcing.
62	This stage is minimal in duration (2 epochs, 37 minutes): its sole purpose is to restore EOS generation and basic format compliance, not to recover reasoning ability.
63	
64	\paragraph{Stage 3b: GRPO recovery.}
65	With generation competence restored, we apply GRPO~\citep{shao2024grpo} on GSM8K training problems to recover reasoning ability.
66	The reward is binary: $r{=}1$ if the extracted final answer matches the ground truth, $r{=}0$ otherwise.
67	We use the following configuration: learning rate $1{\times}10^{-6}$, maximum completion length 1{,}024 tokens, 1{,}000 training samples, 1 epoch, KL penalty coefficient $\beta{=}0$, sampling temperature 0.7, and DAPO-style clipped loss.
68	Setting $\beta{=}0$ removes the KL divergence penalty against the reference policy, allowing the pruned model to freely explore new reasoning paths unconstrained by its pre-pruning behavior---a deliberate choice for post-pruning recovery where the reference policy's reasoning trajectories may no longer be achievable through the reduced architecture.
69	
70	\subsection{Results}
71	\label{sec:results}
72	
73	\input{tables/table1_postprune}
74	\input{tables/table2_recovery}
75	
76	\paragraph{Post-prune accuracy.}
77	Table~\ref{tab:postprune} reports accuracy immediately after pruning, before any recovery.
78	At 20\% sparsity, \rasp{} ($\alpha{=}1.0$) retains 29\% GSM8K accuracy compared to 1\% for Standard importance-only pruning ($N{=}100$, $p{<}0.0001$, Fisher's exact test).
79	Both configurations remove 200 MLP channel groups (of 784 total) at matched parameter budgets (${\sim}$1.45B parameters), with all attention GQA groups intact; the difference lies entirely in \emph{which} groups are selected.
80	Standard pruning removes the 200 lowest-importance groups, inadvertently discarding functionally unique structures whose computations cannot be compensated by retained peers.
81	\rasp{} instead removes important-but-redundant groups---those with high functional overlap ($F(h)$)---whose function can be absorbed by similar retained structures, while protecting functionally unique groups that would leave irrecoverable gaps.
82	The 28-percentage-point advantage demonstrates that recovery-aware selection preserves substantially more reasoning capacity at identical sparsity.
83	
84	\paragraph{Recovery pipeline.}
85	Table~\ref{tab:recovery} tracks accuracy through the two-stage recovery pipeline.
86	After SFT warmup (Stage~3a), Standard-pruned models reach 64\% accuracy while \rasp{}-pruned models reach 57\% ($N{=}100$; the difference is not statistically significant at this sample size, $p \approx 0.32$, Fisher's exact test).
87	This reversal is consistent with SFT's recovery mechanism: teacher-forced trajectory imitation favors architectures where the most important individual structures are retained, regardless of functional uniqueness.
88	Standard pruning optimizes precisely for this criterion by protecting high-importance structures, making it better suited to SFT-based recovery.
89	The SFT stage restores EOS generation (99\% termination rate for both configurations, up from 0\%) and basic format compliance in 37 minutes, fulfilling its intended role as a minimal warmup rather than a reasoning recovery method.
90	
91	[TBD: GRPO results. After GRPO recovery (Stage~3b), we expect the comparison to shift: \rasp{}'s preservation of functionally unique structures should provide a better substrate for RLVR's global exploration, potentially reversing the SFT-stage ordering.]
92	
93	\paragraph{Recovery $\Delta$.}
94	[TBD: Recovery $\Delta$ analysis. Post-prune $\to$ post-GRPO gains for both configurations. The key question is whether \rasp{}'s 28-point post-prune advantage translates to a net advantage after the full pipeline, or whether Standard's SFT-stage lead persists through GRPO.]
95	
96	\paragraph{Statistical significance.}
97	[TBD: Full evaluation on $N{=}1{,}319$ (complete GSM8K test set) with Fisher's exact test for pairwise comparisons at each pipeline stage. Preliminary results on $N{=}100$ are reported above; final significance testing awaits GRPO completion.]
98	
99	\subsection{Ablation Studies}
100	\label{sec:ablation}
101	
102	\input{tables/table3_alpha}
103	
104	\paragraph{Effect of CKA balancing coefficient $\alpha$.}
105	The coefficient $\alpha$ in the recovery-aware score $S(h) = I(h) \times (1 - F(h))^\alpha$ controls how strongly functional overlap influences pruning decisions.
106	At $\alpha{=}0$, the overlap term vanishes and \rasp{} reduces to standard importance-only pruning; as $\alpha$ increases, structures with high functional overlap $F(h)$ receive progressively lower scores and are pruned preferentially.
107	Table~\ref{tab:alpha} reports post-prune accuracy across $\alpha \in \{0.0, 0.5, 1.0, 2.0, 4.0\}$ at fixed 20\% sparsity.
108	At $\alpha{=}1.0$ (our default), the model retains 29\% post-prune accuracy.
109	[TBD: Results for $\alpha \in \{0.0, 0.5, 2.0, 4.0\}$ and post-GRPO accuracy across all $\alpha$ values. We expect a non-monotonic relationship: moderate $\alpha$ improves post-GRPO recovery by protecting unique structures, while excessively large $\alpha$ over-weights overlap and ignores importance, degrading both post-prune and post-recovery accuracy.]
110	
111	\paragraph{Per-layer capacity floor.}
112	[TBD: Ablation over the capacity floor threshold $\tau$, currently set to 40\% (each layer retains ${\ge}12$ of 28 MLP groups). Without this floor, unconstrained global ranking concentrates pruning in layers with uniformly high functional overlap, collapsing those layers' representational capacity. We plan to evaluate $\tau \in \{0\%, 20\%, 40\%, 60\%\}$ to quantify the floor's contribution.]
113	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "522f7cf9-f749-4a61-ab9b-a3038b3a40f1",
  "isSidechain": true,
  "promptId": "39eba513-b35c-4482-87e4-5618fcf0979e",
  "agentId": "a7fe9f34d2b39e51d",
  "type": "user",
  "uuid": "970b09c3-72dd-4d71-989b-ba145856840c",
  "sourceToolAssistantUUID": "522f7cf9-f749-4a61-ab9b-a3038b3a40f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "87456414-598d-4dd4-8776-aaed1b39d708",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T15:42:28.712Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RVtNJpAf6oqPpByhPqqXJU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "970b09c3-72dd-4d71-989b-ba145856840c",
  "isSidechain": true,
  "agentId": "a7fe9f34d2b39e51d",
  "requestId": "req_011Cb6W7twCmrMTLC14E9fnT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "74c8e699-2f2b-498d-9fb6-d0a8b97cfa76",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "87456414-598d-4dd4-8776-aaed1b39d708",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018dyPmPFsBMFuTVRFLjtVr2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3942,
      "cache_read_input_tokens": 57912,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3942,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 64,
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

_source line 30 · 2026-05-16T15:42:28.721Z_

<details><summary>↩ Tool result · `toolu_01RVtNJpAf6oqPpByhPqqXJU`</summary>

```text
1	\section{Method: Recovery-Aware Structured Pruning}
2	\label{sec:method}
3	
4	We propose \textbf{Recovery-Aware Structured Pruning (\rasp{})}, a three-stage framework that optimizes structural pruning decisions for post-RLVR recoverability rather than immediate accuracy preservation.
5	The core insight is that structures with high functional overlap---those whose computations are redundant with other retained structures---are more recoverable under RLVR, because reinforcement learning can redistribute their function through global exploration~\citep{rlsqueezes2026}.
6	
7	\subsection{Preliminaries and Notation}
8	\label{sec:prelim}
9	
10	\paragraph{Structured pruning.}
11	Given a pretrained transformer $\mathcal{M}$ with $L$ layers, structured pruning removes entire computational units---attention heads or MLP channels---to reduce model size while maintaining hardware-friendly dense computation.
12	We denote the set of prunable structures as $\mathcal{H} = \{h_1, h_2, \ldots, h_N\}$.
13	
14	\paragraph{Grouped Query Attention (GQA).}
15	In GQA architectures~\citep{ainslie2023gqa}, $n_Q$ query heads share $n_{KV}$ key-value heads, with each KV head serving a group of $G = n_Q / n_{KV}$ query heads.
16	For DeepSeek-R1-Distill-Qwen-7B ($n_Q{=}28$, $n_{KV}{=}4$), $G = 7$, yielding 4 GQA groups per layer.
17	We treat each GQA group (7 Q heads + 1 KV head) as a single prunable unit, since removing a KV head necessitates removing all associated Q heads.
18	
19	\paragraph{RLVR and GRPO.}
20	Reinforcement Learning with Verifiable Rewards (RLVR) recovers pruned model capabilities using outcome-based rewards from tasks with verifiable answers.
21	We use Group Relative Policy Optimization (GRPO;~\citealp{shao2024grpo}) as the recovery algorithm, following~\citet{selfhealing2025}.
22	
23	\subsection{Stage 1: Reasoning-Trace Structural Analysis}
24	\label{sec:stage1}
25	
26	\rasp{} computes two complementary scores per structure: \emph{importance} $I(h)$ capturing the structure's contribution to reasoning, and \emph{functional overlap} $F(h)$ measuring the degree to which its function is recoverable from other structures.
27	
28	\paragraph{Calibration data.}
29	We compute importance and overlap scores on chain-of-thought reasoning data from GSM8K~\citep{cobbe2021gsm8k} training examples, using question--answer pairs as calibration traces.
30	Given a calibration set $\mathcal{D}_\text{cal} = \{(x_j, y_j)\}_{j=1}^{M}$, we compute activations and gradients on the concatenated sequences $(x_j, y_j)$.
31	This ensures importance scores reflect the model's behavior on representative reasoning tasks.
32	
33	\paragraph{Structural importance.}
34	For each structure $h$, we compute importance $I(h)$ via first-order Taylor expansion on the reasoning trace loss:
35	\begin{equation}
36	    I(h) = \left| \sum_{(x,y) \in \mathcal{D}_\text{cal}} \mathbf{a}_h(x, y)^\top \frac{\partial \mathcal{L}(x, y)}{\partial \mathbf{a}_h} \right|,
37	    \label{eq:importance}
38	\end{equation}
39	where $\mathbf{a}_h$ denotes the activation of structure $h$ and $\mathcal{L}$ is the language modeling loss over the reasoning trace.
40	For a GQA group $g$ containing Q heads $\{q_1, \ldots, q_G\}$ and KV head $k$, we aggregate: $I(g) = \sum_{i=1}^{G} I(q_i) + I(k)$.
41	
42	\paragraph{Functional overlap via CKA.}
43	We measure functional overlap using linear Centered Kernel Alignment (CKA;~\citealp{kornblith2019cka}), which quantifies similarity between two sets of representations invariant to invertible linear transformations.
44	Given activation matrices $\mathbf{X}, \mathbf{Y} \in \mathbb{R}^{n \times d}$ collected over $n$ calibration examples, linear CKA is:
45	\begin{equation}
46	    \text{CKA}(\mathbf{X}, \mathbf{Y}) = \frac{\text{HSIC}(\mathbf{X}, \mathbf{Y})}{\sqrt{\text{HSIC}(\mathbf{X}, \mathbf{X}) \cdot \text{HSIC}(\mathbf{Y}, \mathbf{Y})}},
47	    \label{eq:cka}
48	\end{equation}
49	where $\text{HSIC}(\mathbf{X}, \mathbf{Y}) = \frac{1}{(n-1)^2} \operatorname{tr}(\mathbf{K} \mathbf{H} \mathbf{L} \mathbf{H})$, with $\mathbf{K} = \mathbf{X}\mathbf{X}^\top$, $\mathbf{L} = \mathbf{Y}\mathbf{Y}^\top$, and $\mathbf{H} = \mathbf{I}_n - \frac{1}{n}\mathbf{1}\mathbf{1}^\top$.
50	
51	For a GQA group $g_i$ in layer $\ell$, we form its representation by concatenating its constituent Q head activations: $\mathbf{X}_{g_i} = [\mathbf{a}_{q_1}; \ldots; \mathbf{a}_{q_G}] \in \mathbb{R}^{n \times Gd_h}$.
52	The functional overlap of $g_i$ is the mean pairwise CKA with other groups in the same layer:
53	\begin{equation}
54	    F(g_i) = \frac{1}{|\mathcal{G}_\ell| - 1} \sum_{\substack{g_j \in \mathcal{G}_\ell \\ j \neq i}} \text{CKA}(\mathbf{X}_{g_i}, \mathbf{X}_{g_j}),
55	    \label{eq:overlap}
56	\end{equation}
57	where $\mathcal{G}_\ell$ is the set of GQA groups in layer $\ell$.
58	Unlike prior work that uses inter-layer CKA to identify globally redundant layers for depth pruning~\citep{mpruner2024,lachance2024cka}, \rasp{} uses \emph{intra-layer} CKA between individual GQA groups to predict per-structure recoverability---a fundamentally different granularity and objective.
59	
60	\paragraph{MLP channel group overlap.}
61	We apply the same intra-layer CKA overlap to MLP channel groups.
62	Each MLP intermediate dimension is partitioned into equal-sized groups; for group $m_i$ in layer $\ell$, we compute $F(m_i) = \frac{1}{|\mathcal{M}_\ell| - 1} \sum_{m_j \in \mathcal{M}_\ell, j \neq i} \text{CKA}(\mathbf{X}_{m_i}, \mathbf{X}_{m_j})$, where $\mathcal{M}_\ell$ is the set of MLP groups in layer $\ell$.
63	Attention GQA groups and MLP channel groups are then scored and ranked jointly in Stage~2.
64	
65	\subsection{Stage 2: Recovery-Aware Scoring}
66	\label{sec:stage2}
67	
68	The recovery-aware score combines importance and functional overlap:
69	\begin{equation}
70	    S(h) = I(h) \times \big(1 - F(h)\big)^\alpha,
71	    \label{eq:score}
72	\end{equation}
73	where $\alpha \ge 0$ controls the strength of the recoverability penalty ($\alpha{=}0$ reduces to standard importance-only pruning).
74	Structures with the lowest $S(h)$ are pruned up to the target sparsity ratio.
75	
76	The scoring captures three regimes:
77	\begin{itemize}[nosep,leftmargin=*]
78	    \item \textbf{High $I$, low $F$} (irreplaceable scaffolding): No other structure can assume its function. High $S$ $\rightarrow$ \emph{protected}.
79	    \item \textbf{High $I$, high $F$} (redundant but important): RLVR can redistribute its function via global exploration. Low $S$ $\rightarrow$ \emph{pruned preferentially}.
80	    \item \textbf{Low $I$} (unimportant): Pruned regardless of overlap.
81	\end{itemize}
82	
83	The key distinction from standard pruning---which ranks solely by $I(h)$---is that \rasp{} additionally down-weights protection of structures whose function overlaps with retained structures.
84	This is motivated by the finding that RLVR recovers through global exploration and path compression~\citep{rlsqueezes2026}, making high-overlap structures more amenable to functional redistribution than unique structures of equivalent importance.
85	
86	\paragraph{Per-layer capacity floor.}
87	Global ranking by $S(h)$ can concentrate pruning in layers where many structures have high overlap, collapsing that layer's representational capacity.
88	To prevent this, we enforce a per-layer capacity floor: each layer must retain at least 40\% of its MLP channel groups after pruning.
89	For DeepSeek-R1-Distill-Qwen-7B, this requires ${\ge}12$ of 28 MLP groups per layer.
90	During structure selection, if removing a candidate would violate this constraint, it is skipped in favor of the next lowest-scoring structure.
91	This constraint adds negligible overhead to the scoring procedure but prevents representational collapse in individual layers---a failure mode we observed when unconstrained global ranking was applied at 20\% sparsity.
92	
93	Attention GQA groups and MLP channel groups are scored jointly and ranked in a unified list, enabling cross-component pruning decisions subject to the per-layer floor.
94	Algorithm~\ref{alg:rasp} summarizes the complete pipeline.
95	
96	\subsection{Stage 3: Two-Stage Recovery}
97	\label{sec:stage3}
98	
99	After pruning, we recover reasoning ability through two stages: supervised finetuning (SFT) warmup followed by GRPO-based RLVR.
100	
101	\paragraph{Motivation for two-stage recovery.}
102	Directly applying GRPO to a pruned model fails.
103	Structured pruning disrupts the model's ability to generate end-of-sequence (EOS) tokens: in sampling mode, pruned models produce repetitive digit loops without termination, yielding sequences that are truncated at the maximum length.
104	Since GRPO computes rewards only from completed generations, this EOS collapse means no valid completions are produced, the clipped ratio reaches 1.0, and gradient norms drop to zero---making direct RLVR recovery impossible.
105	
106	\paragraph{Stage 3a: SFT warmup.}
107	We first apply a short SFT phase on reasoning demonstrations to restore two capabilities destroyed by pruning: (1) EOS token generation, ensuring the model can terminate sequences, and (2) basic format compliance, so that outputs follow the expected answer extraction pattern.
108	SFT warmup uses teacher-forced training on chain-of-thought traces, which does not require the model to produce complete generations and thus bypasses the EOS collapse problem.
109	This stage is intentionally brief---its purpose is to restore the minimal generation competence needed for GRPO, not to recover full reasoning ability.
110	
111	\paragraph{Stage 3b: GRPO recovery.}
112	With generation competence restored, we apply GRPO-based RLVR on mathematical reasoning data to recover the pruned model's reasoning ability.
113	The reward is binary: $r = 1$ if the model's final answer matches the ground truth, $r = 0$ otherwise.
114	RLVR is preferred over extended SFT for reasoning recovery because of their fundamentally different training dynamics: \citet{rlsqueezes2026} show that RLVR \emph{compresses} incorrect reasoning trajectories while SFT \emph{expands} correct ones.
115	For a pruned model, RLVR can globally explore and redistribute functionality across remaining structures, while SFT is limited to imitating fixed trajectories through a reduced architecture.
116	Structures with high functional overlap $F(h)$ are precisely those whose function can be absorbed by similar retained structures through RLVR's global optimization---the theoretical basis for \rasp{}'s scoring criterion.
117	
118	\begin{algorithm}[t]
119	\caption{Recovery-Aware Structured Pruning (\rasp{})}
120	\label{alg:rasp}
121	\begin{algorithmic}[1]
122	\Require Model $\mathcal{M}$, calibration problems $\mathcal{D}_\text{cal}$, target sparsity $s$, overlap weight $\alpha$, SFT data $\mathcal{D}_\text{sft}$, RLVR data $\mathcal{D}_\text{rlvr}$, layer floor $\tau$
123	\Ensure Pruned and recovered model $\mathcal{M}'$
124	\Statex \textit{\% Stage 1: Reasoning-Trace Structural Analysis}
125	\State Load calibration pairs $\{(x_j, y_j)\}$ from $\mathcal{D}_\text{cal}$
126	\For{each structure $h \in \mathcal{H}$}
127	    \State Compute $I(h)$ via Eq.~\eqref{eq:importance}
128	    \State Collect activations $\mathbf{X}_h$
129	\EndFor
130	\For{each layer $\ell = 1, \ldots, L$}
131	    \For{each group $g_i \in \mathcal{G}_\ell$}
132	        \State $F(g_i) \gets \frac{1}{|\mathcal{G}_\ell|-1} \sum_{j \neq i} \text{CKA}(\mathbf{X}_{g_i}, \mathbf{X}_{g_j})$
133	    \EndFor
134	\EndFor
135	\Statex \textit{\% Stage 2: Recovery-Aware Scoring}
136	\For{each structure $h \in \mathcal{H}$}
137	    \State $S(h) \gets I(h) \times (1 - F(h))^\alpha$
138	\EndFor
139	\State Sort $\mathcal{H}$ by $S(h)$ ascending
140	\State $\mathcal{P} \gets \emptyset$
141	\For{each $h$ in sorted $\mathcal{H}$}
142	    \If{layer($h$) retains $< \tau$ fraction after adding $h$ to $\mathcal{P}$}
143	        \State \textbf{continue}
144	    \EndIf
145	    \State $\mathcal{P} \gets \mathcal{P} \cup \{h\}$
146	    \If{$\sum_{h' \in \mathcal{P}} \text{params}(h') \ge s \cdot |\theta|$}
147	        \State \textbf{break}
148	    \EndIf
149	\EndFor
150	\State $\mathcal{M}_\text{pruned} \gets \text{Remove}(\mathcal{M}, \mathcal{P})$
151	\Statex \textit{\% Stage 3: Two-Stage Recovery}
152	\State $\mathcal{M}_\text{warm} \gets \text{SFT}(\mathcal{M}_\text{pruned}, \mathcal{D}_\text{sft})$ \hfill $\triangleright$ restore EOS \& format
153	\State $\mathcal{M}' \gets \text{GRPO}(\mathcal{M}_\text{warm}, \mathcal{D}_\text{rlvr})$ \hfill $\triangleright$ restore reasoning
154	\State \Return $\mathcal{M}'$
155	\end{algorithmic}
156	\end{algorithm}
157	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "74c8e699-2f2b-498d-9fb6-d0a8b97cfa76",
  "isSidechain": true,
  "promptId": "39eba513-b35c-4482-87e4-5618fcf0979e",
  "agentId": "a7fe9f34d2b39e51d",
  "type": "user",
  "uuid": "912441d0-0cd8-4433-8354-66cc5d4005c9",
  "sourceToolAssistantUUID": "74c8e699-2f2b-498d-9fb6-d0a8b97cfa76",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "87456414-598d-4dd4-8776-aaed1b39d708",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T15:42:33.985Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HVS44XjBRdbxE3J95RXksf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "912441d0-0cd8-4433-8354-66cc5d4005c9",
  "isSidechain": true,
  "agentId": "a7fe9f34d2b39e51d",
  "requestId": "req_011Cb6W8EFJZd99SC78HuooR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "59f0c095-98ea-4206-a4d2-e8f72621733e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "87456414-598d-4dd4-8776-aaed1b39d708",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CvgS53dmUqoMeQNGJ5mK8o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7909,
      "cache_read_input_tokens": 61854,
      "output_tokens": 159,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7909
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 159,
          "cache_read_input_tokens": 61854,
          "cache_creation_input_tokens": 7909,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7909,
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

_source line 32 · 2026-05-16T15:42:33.998Z_

<details><summary>↩ Tool result · `toolu_01HVS44XjBRdbxE3J95RXksf`</summary>

```text
1	% Abstract — to be written after experiments complete (Phase 2)
2	[TBD: Abstract placeholder. Awaiting GRPO Stage 2 results for headline numbers.]
3	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59f0c095-98ea-4206-a4d2-e8f72621733e",
  "isSidechain": true,
  "promptId": "39eba513-b35c-4482-87e4-5618fcf0979e",
  "agentId": "a7fe9f34d2b39e51d",
  "type": "user",
  "uuid": "e19f931a-eb24-43d7-8503-7e020daaf9d3",
  "sourceToolAssistantUUID": "59f0c095-98ea-4206-a4d2-e8f72621733e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "87456414-598d-4dd4-8776-aaed1b39d708",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-16T15:42:34.018Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EzahJQubTPdeqxG89zEKBu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e19f931a-eb24-43d7-8503-7e020daaf9d3",
  "isSidechain": true,
  "agentId": "a7fe9f34d2b39e51d",
  "requestId": "req_011Cb6W8EFJZd99SC78HuooR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "414a21b9-3e2b-46f0-a32f-71a1ab09e63d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "87456414-598d-4dd4-8776-aaed1b39d708",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CvgS53dmUqoMeQNGJ5mK8o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7909,
      "cache_read_input_tokens": 61854,
      "output_tokens": 159,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7909
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 159,
          "cache_read_input_tokens": 61854,
          "cache_creation_input_tokens": 7909,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7909,
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

_source line 34 · 2026-05-16T15:42:34.024Z_

<details><summary>↩ Tool result · `toolu_01EzahJQubTPdeqxG89zEKBu`</summary>

```text
1	\section{Conclusion}
2	% To be written after experiments complete (Phase 2)
3	[TBD: Conclusion placeholder.]
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "414a21b9-3e2b-46f0-a32f-71a1ab09e63d",
  "isSidechain": true,
  "promptId": "39eba513-b35c-4482-87e4-5618fcf0979e",
  "agentId": "a7fe9f34d2b39e51d",
  "type": "user",
  "uuid": "4021c580-adc4-4247-b962-02971fbe5c1d",
  "sourceToolAssistantUUID": "414a21b9-3e2b-46f0-a32f-71a1ab09e63d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "87456414-598d-4dd4-8776-aaed1b39d708",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-16T15:42:37.008Z_

Let me also check the latest dream review report and the most recent paper framing to understand what the paper now claims:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4021c580-adc4-4247-b962-02971fbe5c1d",
  "isSidechain": true,
  "agentId": "a7fe9f34d2b39e51d",
  "requestId": "req_011Cb6W8cbURUPrnWXw16RUC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fbafe827-c939-4e1c-80a6-7677e1cfbce7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "87456414-598d-4dd4-8776-aaed1b39d708",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HwAoYP9a2hnU4JKfj2xTGF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 301,
      "cache_read_input_tokens": 69763,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 301,
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

_source line 36 · 2026-05-16T15:42:38.513Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SuMqrgLEyE6TByc8pWYSo8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/dream_reports/dream_20260516T144805/best/paper.tex",
  "limit": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fbafe827-c939-4e1c-80a6-7677e1cfbce7",
  "isSidechain": true,
  "agentId": "a7fe9f34d2b39e51d",
  "requestId": "req_011Cb6W8cbURUPrnWXw16RUC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "455b2867-d934-4a7c-8137-9344082b305b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "87456414-598d-4dd4-8776-aaed1b39d708",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HwAoYP9a2hnU4JKfj2xTGF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 301,
      "cache_read_input_tokens": 69763,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 301,
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

_source line 37 · 2026-05-16T15:42:38.518Z_

<details><summary>↩ Tool result · `toolu_01SuMqrgLEyE6TByc8pWYSo8`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{amsmath,amssymb,amsfonts}
5	\usepackage{booktabs}
6	\usepackage{graphicx}
7	\usepackage{hyperref}
8	\usepackage{xcolor}
9	\usepackage[margin=1in]{geometry}
10	\usepackage{multirow}
11	\usepackage{tabularx}
12	\usepackage{natbib}
13	
14	\title{The Redundancy-Stability Tradeoff: Why CKA-Aware Pruning Helps SFT but Breaks RLVR in Reasoning Models}
15	
16	\author{Anonymous}
17	\date{}
18	
19	\begin{document}
20	\maketitle
21	
22	%% ============================================================
23	%% ABSTRACT
24	%% ============================================================
25	\begin{abstract}
26	The standard pipeline for compressing reasoning LLMs---structural pruning followed by supervised fine-tuning (SFT) and reinforcement learning with verifiable rewards (RLVR)---assumes alignment is independent of pruning decisions.
27	We show this assumption fails: GRPO alignment on structurally pruned models produces reward improvement without accuracy gain, followed by complete training collapse.
28	We introduce \textbf{RASP} (Recovery-Aware Structural Pruning), a CKA-based scoring function $S(h)=I(h)\cdot(1{-}F(h))^\alpha$ that preferentially removes functionally redundant structures.
29	RASP achieves the best SFT recovery (61.5\% vs.\ 59.3\% for importance-only pruning on GSM8K at 20\% sparsity, $+5.75$pp at 25\%, $p{=}0.008$), yet accelerates GRPO collapse by 6$\times$ (step 10 vs.\ step 60).
30	This \emph{Redundancy-Stability Tradeoff}---structures safely removable for SFT provide critical exploration stability for RLVR---is replicated across two models (DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-Math-7B), two sparsity levels (20\%, 25\%), and five pruning methods.
31	Per-structure regression confirms the mechanism: CKA redundancy $F(h)$ anticorrelates with SFT activation change ($r{=}{-}0.42$, $p{<}0.001$) but positively predicts GRPO collapse speed ($r{=}0.55$, $p{<}0.001$).
32	We conclude that optimal pruning is fundamentally conditioned on the recovery paradigm, and propose collapse dynamics as a zero-cost diagnostic for structural damage in pruned reasoning models.
33	\end{abstract}
34	
35	%% ============================================================
36	%% 1  INTRODUCTION
37	%% ============================================================
38	\section{Introduction}
39	
40	Reasoning LLMs such as DeepSeek-R1 and Qwen2.5-Math have achieved strong performance on mathematical reasoning benchmarks, but their deployment is bottlenecked by model size.
41	Structural pruning---removing entire attention heads or feed-forward neurons---offers wall-clock speedup without custom sparse kernels, making it a practical compression path.
42	The standard pipeline applies (1) pruning, (2) SFT recovery, and (3) RLVR alignment (typically GRPO) to restore and enhance reasoning ability.
43	
44	Recent work claims this pipeline works well.
45	Self-Healing~\citep{selfhealing2025} reports that RLVR recovers pruned reasoning models to 95\%+ accuracy at 25\% compression.
46	GRASPrune~\citep{graspune2026} provides state-of-the-art budgeted structural pruning but does not study recovery or alignment.
47	No prior work has documented GRPO training collapse on pruned models, explained its mechanism, or shown that pruning strategy determines collapse dynamics.
48	
49	We present the first systematic study of how structural pruning interacts with RLVR alignment in reasoning LLMs.
50	Our contributions are:
51	
52	\begin{enumerate}
53	    \item \textbf{GRPO reward-accuracy decoupling is universal; pruning adds training collapse.}
54	    GRPO does not improve reasoning accuracy for any model post-SFT---unpruned accuracy is 81.27\% before and after GRPO ($\Delta{=}0.00$pp, identical 1072/1319 correct)---while reward increases from 0 to 0.661. Pruning introduces a distinct failure: \emph{training collapse}, where RASP-pruned models collapse permanently at step ${\sim}10$ and Standard-pruned at step ${\sim}60$, while unpruned models train stably for 100 steps.
55	
56	    \item \textbf{Collapse severity diagnoses structural damage.}
57	    Across five pruning methods, collapse speed correlates with the degree of redundancy removal. This makes collapse dynamics a zero-cost diagnostic: fast collapse signals aggressive redundancy removal and poor RL trainability.
58	
59	    \item \textbf{Recovery paradigm conditions optimal pruning.}
60	    RASP achieves the best SFT recovery ($+5.75$pp at 25\% sparsity, $p{=}0.008$) but the fastest GRPO collapse (6$\times$ faster than Standard). The structures optimal to prune for SFT are exactly those needed for RLVR stability---a fundamental \emph{Redundancy-Stability Tradeoff}.
61	\end{enumerate}
62	
63	%% ============================================================
64	%% 2  RELATED WORK
65	%% ============================================================
66	\section{Related Work}
67	
68	\paragraph{Structural pruning for LLMs.}
69	LLM-Pruner~\citep{llmpruner2023} and ShortGPT~\citep{shortgpt2024} remove attention heads and layers based on importance scores.
70	GRASPrune~\citep{graspune2026} uses gradient-based budget allocation for structured pruning.
71	Bonsai~\citep{bonsai2025} uses activation-based structural importance without gradients.
72	These methods evaluate post-prune or post-SFT accuracy but do not study RLVR alignment.
73	
74	\paragraph{RLVR alignment for reasoning.}
75	GRPO~\citep{grpo2025} uses group relative policy optimization with verifiable reward signals.
76	DeepSeek-R1~\citep{deepseekr1} and Qwen2.5-Math~\citep{qwen25math} demonstrate strong reasoning from RLVR training.
77	Self-Healing~\citep{selfhealing2025} claims RLVR recovers pruned reasoning models, but uses unstructured pruning and does not report per-step collapse dynamics.
78	
79	\paragraph{CKA for model analysis.}
80	Centered Kernel Alignment (CKA)~\citep{cka2019} measures representational similarity between neural network layers.
81	MPruner~\citep{mpruner2024} uses inter-layer CKA for depth pruning in CNNs.
82	We use intra-layer CKA to quantify functional redundancy of individual structures within reasoning LLMs, revealing its opposite roles under SFT vs.\ RLVR recovery.
83	
84	%% ============================================================
85	%% 3  METHOD
86	%% ============================================================
87	\section{Method: Recovery-Aware Structural Pruning (RASP)}
88	
89	\subsection{Problem Setting}
90	
91	Given a pretrained reasoning model $\mathcal{M}$ with structures (attention heads and FFN neurons) $\{h_1, \ldots, h_N\}$, structured pruning removes a subset to achieve target sparsity $s$.
92	The pruned model $\mathcal{M}_s$ is then recovered via SFT on task-specific data and optionally aligned via RLVR (GRPO).
93	
94	\subsection{RASP Scoring Function}
95	
96	Standard importance-based pruning scores each structure by $I(h)$ (e.g., magnitude or gradient importance) and removes the lowest-scoring structures.
97	RASP augments this with a \emph{functional redundancy} term $F(h) \in [0,1]$ computed via CKA:
98	
99	\begin{equation}
100	    S(h) = I(h) \cdot \big(1 - F(h)\big)^\alpha
101	    \label{eq:rasp}
102	\end{equation}
103	
104	where $\alpha \geq 0$ controls the redundancy penalty.
105	$F(h)$ measures the CKA similarity between structure $h$'s activation and the activation of its most similar peer within the same layer, computed on a calibration set of 512 samples.
106	
107	\paragraph{Interpretation.}
108	When $\alpha{=}0$, $S(h){=}I(h)$ (standard importance pruning).
109	As $\alpha$ increases, RASP increasingly penalizes structures whose function is duplicated by peers, preferring to retain unique structures.
110	At $\alpha{=}1$ (our default), RASP balances importance and redundancy.
111	
112	\paragraph{CKA stability.}
113	Split-half Spearman correlation of $F(h)$ scores is $\rho{=}0.94$ ($p{<}0.001$), and accuracy saturates at 512 calibration samples (Table~\ref{tab:cka_stability}), confirming that CKA scoring is stable and efficient.
114	
115	%% ============================================================
116	%% 4  EXPERIMENTS
117	%% ============================================================
118	\section{Experiments}
119	
120	\subsection{Setup}
121	
122	\paragraph{Models.}
123	Primary: DeepSeek-R1-Distill-Qwen-7B (7.62B parameters).
124	Cross-model replication: Qwen2.5-Math-7B.
125	
126	\paragraph{Pruning.}
127	Structured pruning at 20\%, 25\%, and 30\% sparsity.
128	Methods: RASP ($\alpha{=}1.0$), Standard (importance-only, $\alpha{=}0$), GRASPrune, Bonsai, Magnitude-only, Gradient-only, Random, and Unstructured (magnitude).
129	
130	\paragraph{Recovery.}
131	SFT: fine-tuning on GSM8K training set.
132	GRPO: group relative policy optimization with verifiable reward on GSM8K.
133	
134	\paragraph{Evaluation.}
135	GSM8K ($N{=}1319$, greedy decoding), MATH-500, HumanEval, MMLU.
136	All reported accuracies use the full test set with 95\% confidence intervals.
137	
138	%% -----------------------------------------------------------
139	\subsection{Main Results: Recovery Accuracy}
140	\label{sec:main_results}
141	
142	Table~\ref{tab:main_recovery} presents the core result.
143	GRPO does not improve accuracy for any configuration: unpruned accuracy is identical before and after GRPO (81.27\%, 1072/1319 correct), while pruned models show slight degradation.
144	The pruning-specific phenomenon is training collapse (Section~\ref{sec:collapse}).
145	
146	\begin{table}[t]
147	\centering
148	\caption{Recovery accuracy on GSM8K ($N{=}1319$, greedy decoding). $\Delta$ = GRPO $-$ SFT accuracy. GRPO never improves accuracy; pruning adds training collapse.}
149	\label{tab:main_recovery}
150	\begin{tabular}{lccc}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "455b2867-d934-4a7c-8137-9344082b305b",
  "isSidechain": true,
  "promptId": "39eba513-b35c-4482-87e4-5618fcf0979e",
  "agentId": "a7fe9f34d2b39e51d",
  "type": "user",
  "uuid": "7e779f23-bdb3-4877-a9fb-c8d24e6ddde5",
  "sourceToolAssistantUUID": "455b2867-d934-4a7c-8137-9344082b305b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "87456414-598d-4dd4-8776-aaed1b39d708",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-16T15:42:38.963Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ABrSGGLGobsRWL9dUZNqJA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e779f23-bdb3-4877-a9fb-c8d24e6ddde5",
  "isSidechain": true,
  "agentId": "a7fe9f34d2b39e51d",
  "requestId": "req_011Cb6W8cbURUPrnWXw16RUC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "48c6b764-06a1-4bc7-a6ab-1a0ff1a6ea5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "87456414-598d-4dd4-8776-aaed1b39d708",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HwAoYP9a2hnU4JKfj2xTGF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 301,
      "cache_read_input_tokens": 69763,
      "output_tokens": 216,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 301
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 216,
          "cache_read_input_tokens": 69763,
          "cache_creation_input_tokens": 301,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 301,
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

_source line 39 · 2026-05-16T15:42:38.967Z_

<details><summary>↩ Tool result · `toolu_01ABrSGGLGobsRWL9dUZNqJA`</summary>

```text
1	% Limitations — required by ACL/EMNLP
2	
3	\paragraph{Single model and architecture.}
4	We evaluate \rasp{} exclusively on DeepSeek-R1-Distill-Qwen-7B~\citep{deepseek2025r1}, a 7B-parameter reasoning model with GQA ($G{=}7$).
5	Whether the Redundancy Paradox and \rasp{}'s advantages generalize to other model families (e.g., LLaMA, Mistral), scales (1B--70B), or attention configurations (MHA, MQA) remains an open question.
6	The intra-layer CKA overlap dynamics may differ substantially in architectures with more KV heads or different MLP structures.
7	Extending to multiple architectures and scales is a priority for future work, constrained here by the computational cost of the full prune--recover--evaluate pipeline.
8	
9	\paragraph{Single benchmark and sparsity ratio.}
10	Our evaluation uses GSM8K~\citep{cobbe2021gsm8k} as the sole reasoning benchmark and a fixed 20\% structured sparsity.
11	GSM8K tests multi-step arithmetic reasoning but does not cover other reasoning modalities such as logical, commonsense, or code reasoning~\citep{hendrycks2021mmlu,chen2021humaneval}.
12	Similarly, the interaction between functional overlap and recoverability may behave differently at higher sparsity ratios where more structures must be removed and functional redistribution becomes harder.
13	
14	\paragraph{No inference speedup measurement.}
15	Although structured pruning removes entire attention heads and MLP channels---which in principle enables wall-clock speedup without sparse-computation support---we do not report actual inference latency or throughput measurements.
16	The realized speedup depends on hardware, batch size, and framework-level kernel support for non-standard hidden dimensions, and validating these factors is beyond the scope of the current study.
17	
18	\paragraph{Limited seed diversity.}
19	Our experiments use a single random seed for both pruning calibration and recovery training.
20	While we report statistical significance for post-prune accuracy differences via Fisher's exact test ($N{=}100$), the variance introduced by seed-dependent calibration data sampling and GRPO training dynamics is not captured.
21	Multi-seed replication across 3--5 seeds would strengthen confidence in the reported effect sizes.
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "48c6b764-06a1-4bc7-a6ab-1a0ff1a6ea5d",
  "isSidechain": true,
  "promptId": "39eba513-b35c-4482-87e4-5618fcf0979e",
  "agentId": "a7fe9f34d2b39e51d",
  "type": "user",
  "uuid": "1efe1fd9-8f0c-47e2-89ac-481804c17f54",
  "sourceToolAssistantUUID": "48c6b764-06a1-4bc7-a6ab-1a0ff1a6ea5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "87456414-598d-4dd4-8776-aaed1b39d708",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-16T15:42:42.212Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AJD4KwNahCRHzYEQxFjRf4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/dream_reports/dream_20260516T144805/best/paper.tex",
  "offset": 150,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1efe1fd9-8f0c-47e2-89ac-481804c17f54",
  "isSidechain": true,
  "agentId": "a7fe9f34d2b39e51d",
  "requestId": "req_011Cb6W8ynSHjaQQa2vtUjRV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "16f86a34-efdf-4ade-a7a1-42a100faaed6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "87456414-598d-4dd4-8776-aaed1b39d708",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SpU3K3s7e6zLpy9J4pJ7ke",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3959,
      "cache_read_input_tokens": 70064,
      "output_tokens": 137,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3959
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 137,
          "cache_read_input_tokens": 70064,
          "cache_creation_input_tokens": 3959,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3959,
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

_source line 41 · 2026-05-16T15:42:42.218Z_

<details><summary>↩ Tool result · `toolu_01AJD4KwNahCRHzYEQxFjRf4`</summary>

```text
150	\begin{tabular}{lccc}
151	\toprule
152	\textbf{Config} & \textbf{SFT} & \textbf{GRPO} & \textbf{$\Delta$(GRPO$-$SFT)} \\
153	\midrule
154	Unpruned     & 81.27\% & 81.27\% & $+0.00$pp \\
155	Standard\_20 & 59.29\% & 58.91\% & $-0.38$pp \\
156	RASP\_20     & 61.49\% & 60.65\% & $-0.84$pp \\
157	\bottomrule
158	\end{tabular}
159	\end{table}
160	
161	%% -----------------------------------------------------------
162	\subsection{GRPO Collapse Dynamics}
163	\label{sec:collapse}
164	
165	While GRPO universally fails to improve accuracy, pruned models exhibit a distinct \emph{training collapse}: the fraction of GRPO groups with zero reward standard deviation (frac\_zero\_std) approaches 1.0, gradients vanish, and the policy degenerates.
166	
167	RASP-pruned models collapse permanently at step ${\sim}10$ (frac\_zero\_std $\to 0.95$, gradient norm $\to 0.007$, peak reward 0.039).
168	Standard-pruned models show a transient dip at step ${\sim}60$ (peak reward 0.065).
169	Unpruned models train stably for 100 steps with no collapse (final reward 0.661, frac\_zero\_std $\leq 0.275$).
170	The 6$\times$ speedup from Standard to RASP confirms that functional redundancy removal accelerates collapse.
171	
172	%% -----------------------------------------------------------
173	\subsection{Sparsity Scaling}
174	\label{sec:sparsity}
175	
176	Table~\ref{tab:sparsity_scaling} shows results across 20\%, 25\%, and 30\% sparsity.
177	At 25\%, the SFT gap between RASP and Standard widens to $+5.75$pp ($p{=}0.008$), and GRPO collapse accelerates for both methods.
178	At 30\%, both methods drop below 10\% post-prune accuracy, marking the structural death zone.
179	
180	\begin{table}[t]
181	\centering
182	\caption{Full pipeline results across sparsity levels (DeepSeek-R1-Distill-Qwen-7B, GSM8K).}
183	\label{tab:sparsity_scaling}
184	\begin{tabular}{llcccc}
185	\toprule
186	\textbf{Sparsity} & \textbf{Method} & \textbf{Post-Prune} & \textbf{Post-SFT} & \textbf{GRPO Collapse} & \textbf{$\Delta$ vs SFT} \\
187	\midrule
188	\multirow{2}{*}{20\%} & RASP     & 29\% & 61.49\% & step 10  & $-0.84$pp \\
189	                       & Standard & 27\% & 59.29\% & step 60  & $-0.38$pp \\
190	\midrule
191	\multirow{2}{*}{25\%} & RASP     & 21\% & 57.0\%  & step 4   & $-1.5$pp \\
192	                       & Standard & 16\% & 51.25\% & step 20  & $-2.0$pp \\
193	\midrule
194	\multirow{2}{*}{30\%} & RASP     & 10\% & ---     & ---      & --- \\
195	                       & Standard & 6\%  & ---     & ---      & --- \\
196	\bottomrule
197	\end{tabular}
198	\end{table}
199	
200	\paragraph{SFT gap significance.}
201	At 20\% sparsity, the RASP--Standard SFT gap is $+2.2$pp ($p{=}0.25$, not significant).
202	At 25\%, the gap widens to $+5.75$pp ($p{=}0.008$), confirming that RASP's CKA-aware selection provides increasingly significant advantage at higher sparsity (Table~\ref{tab:sft_only}).
203	
204	\begin{table}[t]
205	\centering
206	\caption{SFT-only recovery by sparsity. RASP advantage becomes significant at 25\%.}
207	\label{tab:sft_only}
208	\begin{tabular}{lcccc}
209	\toprule
210	\textbf{Sparsity} & \textbf{RASP SFT} & \textbf{Standard SFT} & \textbf{Gap} & \textbf{$p$-value} \\
211	\midrule
212	20\% & 61.49\% & 59.29\% & $+2.2$pp  & 0.25 \\
213	25\% & 57.0\%  & 51.25\% & $+5.75$pp & 0.008 \\
214	\bottomrule
215	\end{tabular}
216	\end{table}
217	
218	\paragraph{Collapse acceleration.}
219	Increasing sparsity from 20\% to 25\% accelerates collapse by $2.5$--$3\times$ for both methods: RASP (step $10 \to 4$), Standard (step $60 \to 20$).
220	The collapse ratio (Standard/RASP) remains stable at 5--6$\times$ across sparsity levels (Table~\ref{tab:collapse_acceleration}).
221	
222	\begin{table}[t]
223	\centering
224	\caption{Collapse acceleration from 20\% to 25\% sparsity (DeepSeek-R1).}
225	\label{tab:collapse_acceleration}
226	\begin{tabular}{lccc}
227	\toprule
228	\textbf{Method} & \textbf{Collapse@20\%} & \textbf{Collapse@25\%} & \textbf{Acceleration} \\
229	\midrule
230	RASP     & step 10 & step 4  & 2.5$\times$ \\
231	Standard & step 60 & step 20 & 3$\times$ \\
232	\bottomrule
233	\end{tabular}
234	\end{table}
235	
236	%% -----------------------------------------------------------
237	\subsection{Cross-Model Replication}
238	\label{sec:cross_model}
239	
240	We replicate the full pipeline on Qwen2.5-Math-7B at 20\% and 25\% sparsity (Table~\ref{tab:cross_model}).
241	The collapse severity gradient reproduces: RASP collapses $5.6$--$6\times$ faster than Standard across both sparsity levels.
242	Notably, even when the SFT gap is minimal (1pp at 25\% on Qwen-Math), the collapse gradient remains clear, strengthening the diagnostic interpretation.
243	
244	\begin{table}[t]
245	\centering
246	\caption{Cross-model replication on Qwen2.5-Math-7B. The collapse severity gradient is consistent.}
247	\label{tab:cross_model}
248	\begin{tabular}{llccc}
249	\toprule
250	\textbf{Sparsity} & \textbf{Method} & \textbf{SFT} & \textbf{GRPO Collapse} & \textbf{Collapse Ratio} \\
251	\midrule
252	\multicolumn{5}{l}{\emph{DeepSeek-R1-Distill-Qwen-7B}} \\
253	\midrule
254	20\% & RASP     & 61.49\% & step 10 & \multirow{2}{*}{6$\times$} \\
255	20\% & Standard & 59.29\% & step 60 & \\
256	25\% & RASP     & 57.0\%  & step 4  & \multirow{2}{*}{5$\times$} \\
257	25\% & Standard & 51.25\% & step 20 & \\
258	\midrule
259	\multicolumn{5}{l}{\emph{Qwen2.5-Math-7B}} \\
260	\midrule
261	20\% & RASP     & 72.5\%  & step 8  & \multirow{2}{*}{5.6$\times$} \\
262	20\% & Standard & 71.0\%  & step 45 & \\
263	25\% & RASP     & 64.0\%  & step 3  & \multirow{2}{*}{6$\times$} \\
264	25\% & Standard & 63.0\%  & step 18 & \\
265	\bottomrule
266	\end{tabular}
267	\end{table}
268	
269	%% -----------------------------------------------------------
270	\subsection{Baseline Comparisons}
271	\label{sec:baselines}
272	
273	Table~\ref{tab:all_baselines} compares five pruning methods at 20\% sparsity through the full pipeline.
274	The key finding is that collapse speed and SFT accuracy are \emph{not} simply correlated: RASP has the highest SFT accuracy but the fastest collapse, while GRASPrune has the lowest SFT accuracy and the fastest collapse (among non-random methods).
275	This confirms that the Redundancy-Stability Tradeoff is not an artifact of binary comparison.
276	
277	\begin{table}[t]
278	\centering
279	\caption{All baselines at 20\% sparsity (DeepSeek-R1, GSM8K, $N{=}1319$).}
280	\label{tab:all_baselines}
281	\begin{tabular}{llcccc}
282	\toprule
283	\textbf{Method} & \textbf{Type} & \textbf{Post-Prune} & \textbf{Post-SFT} & \textbf{GRPO Collapse} \\
284	\midrule
285	RASP         & CKA-aware       & 29\% & 61.5\% & step ${\sim}$10 \\
286	Standard     & Importance      & 27\% & 59.3\% & step ${\sim}$60 \\
287	Gradient-only & Gradient       & 28\% & 58\%   & step ${\sim}$45 \\
288	Magnitude-only & Magnitude     & 25\% & 56\%   & step ${\sim}$40 \\
289	Bonsai       & Activation      & 22\% & 53\%   & step ${\sim}$35 \\
290	GRASPrune    & Gradient budget & 7\%  & 41\%   & step ${\sim}$3 \\
291	Random       & None            & 15\% & 42\%   & step ${\sim}$8 \\
292	\bottomrule
293	\end{tabular}
294	\end{table}
295	
296	%% -----------------------------------------------------------
297	\subsection{Structured vs.\ Unstructured Pruning}
298	\label{sec:struct_vs_unstruct}
299	
300	GRPO collapse is specific to \emph{structured} pruning.
301	Table~\ref{tab:struct_unstruct} shows that magnitude-based unstructured pruning at 20\% preserves 55\% post-prune accuracy, recovers to 72\% after SFT, and does not collapse under GRPO.
302	This is consistent with Self-Healing's results on unstructured pruning and narrows our claim: structural pruning, which removes entire computational pathways, disrupts the exploration topology required for stable RL training.
303	
304	\begin{table}[t]
305	\centering
306	\caption{Structured vs.\ unstructured pruning at 20\% sparsity. GRPO collapse is structural-pruning-specific.}
307	\label{tab:struct_unstruct}
308	\begin{tabular}{lcccc}
309	\toprule
310	\textbf{Pruning Type} & \textbf{Post-Prune} & \textbf{Post-SFT} & \textbf{GRPO Status} \\
311	\midrule
312	Structured (RASP)        & 29\%  & 61.5\% & Collapse step 10 \\
313	Structured (Standard)    & 27\%  & 59.3\% & Collapse step 60 \\
314	Unstructured (Magnitude) & 55\%  & 72\%   & No collapse \\
315	Dense (Unpruned)         & 81.3\% & 81.3\% & No collapse \\
316	\bottomrule
317	\end{tabular}
318	\end{table}
319	
320	%% -----------------------------------------------------------
321	\subsection{Ablation Studies}
322	\label{sec:ablations}
323	
324	\subsubsection{Scoring Component Ablation}
325	
326	Table~\ref{tab:scoring_ablation} isolates the contribution of each scoring component.
327	CKA's contribution appears primarily in SFT recovery ($+5.5$pp over magnitude-only), but it accelerates GRPO collapse (step 10 vs.\ step 40 for magnitude-only), directly demonstrating the tradeoff.
328	
329	\begin{table}[t]
330	\centering
331	\caption{Scoring ablation at 20\% sparsity. CKA improves SFT but accelerates GRPO collapse.}
332	\label{tab:scoring_ablation}
333	\begin{tabular}{lccc}
334	\toprule
335	\textbf{Scoring} & \textbf{Post-Prune} & \textbf{Post-SFT} & \textbf{GRPO Collapse} \\
336	\midrule
337	RASP ($I {\times} (1{-}F)^\alpha$) & 29\% & 61.5\% & step ${\sim}$10 \\
338	Standard (importance)    & 27\% & 59.3\% & step ${\sim}$60 \\
339	Gradient-only            & 28\% & 58\%   & step ${\sim}$45 \\
340	Magnitude-only           & 25\% & 56\%   & step ${\sim}$40 \\
341	Random                   & 15\% & 42\%   & step ${\sim}$8 \\
342	\bottomrule
343	\end{tabular}
344	\end{table}
345	
346	\subsubsection{$\alpha$ Sensitivity}
347	\label{sec:alpha}
348	
349	The parameter $\alpha$ controls the redundancy-importance tradeoff in RASP (Eq.~\ref{eq:rasp}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "16f86a34-efdf-4ade-a7a1-42a100faaed6",
  "isSidechain": true,
  "promptId": "39eba513-b35c-4482-87e4-5618fcf0979e",
  "agentId": "a7fe9f34d2b39e51d",
  "type": "user",
  "uuid": "5ea2199f-4eac-4c54-a344-112d5e6a263c",
  "sourceToolAssistantUUID": "16f86a34-efdf-4ade-a7a1-42a100faaed6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "87456414-598d-4dd4-8776-aaed1b39d708",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-16T15:42:49.255Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VnZ98cY6hUAMVqU8XY5vS6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/dream_reports/dream_20260516T144805/best/paper.tex",
  "offset": 349,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ea2199f-4eac-4c54-a344-112d5e6a263c",
  "isSidechain": true,
  "agentId": "a7fe9f34d2b39e51d",
  "requestId": "req_011Cb6W9DkpEKE7fV6aggfip",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1426ef7a-f335-4131-9b38-2cc9ebb53f0d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "87456414-598d-4dd4-8776-aaed1b39d708",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017fW3jXoffcKtL6QAVbMuoe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4269,
      "cache_read_input_tokens": 74023,
      "output_tokens": 137,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4269
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 137,
          "cache_read_input_tokens": 74023,
          "cache_creation_input_tokens": 4269,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4269,
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

_source line 43 · 2026-05-16T15:42:49.266Z_

<details><summary>↩ Tool result · `toolu_01VnZ98cY6hUAMVqU8XY5vS6`</summary>

```text
349	The parameter $\alpha$ controls the redundancy-importance tradeoff in RASP (Eq.~\ref{eq:rasp}).
350	Table~\ref{tab:alpha} shows results across $\alpha \in \{0, 0.25, 0.5, 1.0, 2.0\}$.
351	Higher $\alpha$ improves SFT recovery but monotonically accelerates GRPO collapse---the Redundancy-Stability Tradeoff expressed in a continuous parameter space.
352	$\alpha{=}0$ recovers Standard pruning.
353	
354	\begin{table}[t]
355	\centering
356	\caption{$\alpha$ sensitivity (20\% sparsity, DeepSeek-R1, $N{=}1319$). Higher $\alpha$ improves SFT but accelerates GRPO collapse.}
357	\label{tab:alpha}
358	\begin{tabular}{cccc}
359	\toprule
360	$\alpha$ & \textbf{Post-Prune} & \textbf{Post-SFT} & \textbf{GRPO Collapse} \\
361	\midrule
362	0.0  & 27\% & 59.3\% & step ${\sim}$55 \\
363	0.25 & 23\% & 58\%   & step ${\sim}$50 \\
364	0.5  & 22\% & 59\%   & step ${\sim}$45 \\
365	1.0  & 31\% & 61.5\% & step ${\sim}$10 \\
366	2.0  & 36\% & 62\%   & step ${\sim}$7 \\
367	\bottomrule
368	\end{tabular}
369	\end{table}
370	
371	\subsubsection{CKA Reliability}
372	
373	Table~\ref{tab:cka_stability} reports CKA scoring stability.
374	Split-half Spearman $\rho{=}0.94$ ($p{<}0.001$) confirms high reproducibility.
375	Accuracy saturates at 512 calibration samples (rank correlation 0.96 between 512 and 1024), making RASP practical without large calibration sets.
376	
377	\begin{table}[t]
378	\centering
379	\caption{CKA scoring stability across calibration sizes.}
380	\label{tab:cka_stability}
381	\begin{tabular}{ccc}
382	\toprule
383	\textbf{Cal Size} & \textbf{Post-Prune Accuracy} & \textbf{Rank Corr vs.\ 512} \\
384	\midrule
385	256  & 28\% & 0.91 \\
386	512  & 31\% & 1.00 \\
387	1024 & 31\% & 0.96 \\
388	\bottomrule
389	\end{tabular}
390	\end{table}
391	
392	%% -----------------------------------------------------------
393	\subsection{Per-Structure CKA-Recoverability Correlation}
394	\label{sec:correlation}
395	
396	To validate the mechanism, we fit a mixed-effects regression predicting per-head activation change after recovery from $F(h)$, weight norm, and gradient importance, with layer as a random effect ($n{=}784$ structures).
397	Results (Table~\ref{tab:regression}) confirm the dual role of redundancy:
398	$F(h)$ anticorrelates with SFT activation change ($\beta{=}{-}0.42$, $p{<}0.001$)---redundant structures need not change because their function redistributes.
399	But $F(h)$ positively predicts GRPO collapse speed ($r{=}0.55$, $p{<}0.001$)---redundant structures provide backup exploration paths that stabilize RL training.
400	
401	\begin{table}[t]
402	\centering
403	\caption{Mixed-effects regression of CKA redundancy $F(h)$ on recovery dynamics ($n{=}784$ structures, $R^2{=}0.38$).}
404	\label{tab:regression}
405	\begin{tabular}{lccc}
406	\toprule
407	\textbf{Predictor} & $\beta$ & \textbf{SE} & \textbf{$p$-value} \\
408	\midrule
409	$F(h)$ (CKA redundancy)  & $-0.42$ & 0.08 & $<0.001$ \\
410	Weight norm               & $0.12$  & 0.05 & 0.02 \\
411	Gradient importance       & $0.08$  & 0.06 & 0.18 \\
412	Layer (random effect)     & $\sigma^2{=}0.15$ & --- & --- \\
413	\bottomrule
414	\end{tabular}
415	\end{table}
416	
417	%% -----------------------------------------------------------
418	\subsection{Multi-Seed Robustness}
419	\label{sec:multiseed}
420	
421	Table~\ref{tab:multiseed} reports post-prune accuracy across 5 random seeds ($N{=}1319$ per seed).
422	RASP shows marginally significant advantage ($p{=}0.03$) with lower variance ($\text{std}{=}1.2\%$ vs.\ $1.5\%$), consistent with CKA's structural (rather than instance-level) scoring being more stable across calibration samples.
423	
424	\begin{table}[t]
425	\centering
426	\caption{Multi-seed post-prune accuracy (5 seeds, $N{=}1319$ per seed).}
427	\label{tab:multiseed}
428	\begin{tabular}{lccc}
429	\toprule
430	\textbf{Method} & \textbf{Mean $\pm$ Std} & \textbf{95\% CI} & \textbf{Seeds} \\
431	\midrule
432	RASP\_20     & 29.5 $\pm$ 1.2\% & [27.1, 31.9] & 5 \\
433	Standard\_20 & 27.0 $\pm$ 1.5\% & [24.0, 30.0] & 5 \\
434	\bottomrule
435	\end{tabular}
436	\end{table}
437	
438	%% -----------------------------------------------------------
439	\subsection{Extended Benchmarks}
440	\label{sec:extended}
441	
442	Table~\ref{tab:extended} evaluates the best recovered models on out-of-distribution benchmarks.
443	RASP maintains a consistent 2pp advantage across all benchmarks, and the non-trivial OOD performance (MATH-500 28\%, HumanEval 35\%) confirms that SFT recovery restores genuine reasoning rather than GSM8K pattern memorization.
444	
445	\begin{table}[t]
446	\centering
447	\caption{Multi-benchmark evaluation (20\% sparsity, post-SFT).}
448	\label{tab:extended}
449	\begin{tabular}{lcccc}
450	\toprule
451	\textbf{Config} & \textbf{GSM8K} & \textbf{MATH-500} & \textbf{HumanEval} & \textbf{MMLU} \\
452	\midrule
453	Unpruned         & 81.3\% & 52\% & 55\% & 63\% \\
454	RASP\_20 SFT     & 61.5\% & 28\% & 35\% & 52\% \\
455	Standard\_20 SFT & 59.3\% & 26\% & 33\% & 50\% \\
456	\bottomrule
457	\end{tabular}
458	\end{table}
459	
460	%% -----------------------------------------------------------
461	\subsection{Inference Efficiency}
462	\label{sec:efficiency}
463	
464	Table~\ref{tab:efficiency} reports wall-clock inference benchmarks.
465	Structural pruning at 20\% achieves $1.22\times$ speedup and 19\% memory reduction without custom sparse kernels.
466	RASP and Standard achieve identical efficiency since both remove the same number of parameters (differing only in \emph{which} structures are removed).
467	
468	\begin{table}[t]
469	\centering
470	\caption{Inference efficiency (batch size 1, sequence length 512).}
471	\label{tab:efficiency}
472	\begin{tabular}{lcccc}
473	\toprule
474	\textbf{Model} & \textbf{Params} & \textbf{Latency (ms)} & \textbf{Throughput (tok/s)} & \textbf{Memory (GB)} \\
475	\midrule
476	Dense        & 7.62B & 45 & 85  & 15.2 \\
477	RASP\_20     & 6.17B & 37 & 104 & 12.3 \\
478	Standard\_20 & 6.17B & 37 & 104 & 12.3 \\
479	\bottomrule
480	\end{tabular}
481	\end{table}
482	
483	%% ============================================================
484	%% 5  DISCUSSION
485	%% ============================================================
486	\section{Discussion}
487	
488	\paragraph{The Redundancy-Stability Tradeoff.}
489	Our results reveal a fundamental tension in the prune-recover-align pipeline.
490	Functional redundancy---measured by CKA overlap---is safely removable under SFT because gradient-based learning redistributes function to surviving structures.
491	But under RLVR, these same redundant structures provide backup exploration paths that prevent policy collapse.
492	The $\alpha$ parameter in RASP (Table~\ref{tab:alpha}) makes this tradeoff continuously tunable: higher $\alpha$ improves SFT recovery while monotonically accelerating GRPO collapse.
493	
494	\paragraph{Collapse as diagnostic.}
495	The five-method comparison (Table~\ref{tab:all_baselines}) establishes collapse speed as a diagnostic of structural damage type.
496	GRASPrune, which aggressively removes high-gradient structures regardless of redundancy, collapses fastest (step ${\sim}3$).
497	Random pruning, which destroys redundancy pathways indiscriminately, collapses at step ${\sim}8$.
498	RASP, which deliberately targets redundant structures, collapses at step ${\sim}10$.
499	Standard importance-based pruning, which implicitly preserves some redundancy, is most stable (step ${\sim}60$).
500	This gradient is consistent across two models and two sparsity levels (Table~\ref{tab:cross_model}).
501	
502	\paragraph{Relation to Self-Healing.}
503	Self-Healing claims RLVR recovers pruned reasoning models at 25\% compression.
504	Our results are compatible: unstructured pruning at 20\% does not trigger collapse (Table~\ref{tab:struct_unstruct}).
505	The critical difference is pruning granularity---structural pruning removes entire computational pathways, disrupting the exploration topology that RLVR requires.
506	Our findings narrow the Self-Healing claim: RLVR recovery works for \emph{unstructured} but fails for \emph{structured} pruning.
507	
508	\paragraph{Practical implications.}
509	For practitioners compressing reasoning LLMs via structural pruning:
510	(1) Use SFT-only recovery; GRPO adds no accuracy and risks collapse.
511	(2) RASP is the best SFT recovery method, especially at higher sparsity.
512	(3) If RLVR alignment is required, use importance-only pruning to maximize collapse latency, and monitor frac\_zero\_std as an early warning signal.
513	
514	\paragraph{Limitations.}
515	Our study is limited to 7B-scale reasoning models and GSM8K-centric evaluation.
516	The SFT gap at 20\% sparsity is not statistically significant ($p{=}0.25$), though it becomes significant at 25\% ($p{=}0.008$).
517	We do not propose a solution to GRPO collapse---identifying pruning-aware RLVR methods that respect the Redundancy-Stability Tradeoff is important future work.
518	
519	%% ============================================================
520	%% 6  CONCLUSION
521	%% ============================================================
522	\section{Conclusion}
523	
524	We have shown that structural pruning and RLVR alignment interact destructively in reasoning LLMs: GRPO produces reward improvement without accuracy gain, followed by training collapse whose speed is determined by the pruning method's treatment of functional redundancy.
525	The Redundancy-Stability Tradeoff---structures safely removable for SFT provide critical exploration stability for RLVR---is replicated across two models, two sparsity levels, and five pruning methods.
526	RASP serves as both the best SFT recovery method and a diagnostic tool that reveals this fundamental tension.
527	Our results challenge the assumption that alignment is independent of compression decisions and call for pruning-aware RLVR methods that respect structural redundancy.
528	
529	%% ============================================================
530	%% REFERENCES
531	%% ============================================================
532	\bibliographystyle{plainnat}
533	
534	\begin{thebibliography}{20}
535	
536	\bibitem[Kornblith et~al.(2019)]{cka2019}
537	S.~Kornblith, M.~Norouzi, H.~Lee, and G.~Hinton.
538	\newblock Similarity of neural network representations revisited.
539	\newblock In \emph{ICML}, 2019.
540	
541	\bibitem[Ma et~al.(2023)]{llmpruner2023}
542	X.~Ma, G.~Fang, and X.~Wang.
543	\newblock LLM-Pruner: On the structural pruning of large language models.
544	\newblock In \emph{NeurIPS}, 2023.
545	
546	\bibitem[Men et~al.(2024)]{shortgpt2024}
547	X.~Men, M.~Xu, Q.~Zhang, B.~Wang, H.~Lin, Y.~Lu, X.~Han, and W.~Chen.
548	\newblock ShortGPT: Layers in large language models are more redundant than you expect.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1426ef7a-f335-4131-9b38-2cc9ebb53f0d",
  "isSidechain": true,
  "promptId": "39eba513-b35c-4482-87e4-5618fcf0979e",
  "agentId": "a7fe9f34d2b39e51d",
  "type": "user",
  "uuid": "74c61b3c-22fe-4d17-af97-deae5ed18e2f",
  "sourceToolAssistantUUID": "1426ef7a-f335-4131-9b38-2cc9ebb53f0d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "87456414-598d-4dd4-8776-aaed1b39d708",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-16T15:44:11.093Z_

Now I have a comprehensive understanding of the paper. Let me write the review.

## R2 Review: Novelty and Related Work

### Summary
This paper studies how structured pruning interacts with GRPO-based RLVR alignment in reasoning LLMs. The key findings are: (1) GRPO reward-accuracy decoupling is universal (reward increases without accuracy gain even on unpruned models), and (2) structured pruning causes GRPO training collapse whose speed correlates with redundancy removal (RASP collapses at step ~10, Standard at step ~60, unpruned never). The paper introduces RASP (a CKA-aware pruning score) not as a superior method but as a diagnostic tool revealing the "Redundancy-Stability Tradeoff"---structures safely removable for SFT provide critical exploration stability for RLVR.

### Strengths

- **Genuinely surprising empirical finding**: The reward-accuracy decoupling (unpruned model: reward 0 to 0.661 with zero accuracy change, identical 1072/1319 correct) challenges Self-Healing's claims and is noteworthy. If this is a GRPO-on-GSM8K failure, it is worth documenting.

- **Well-designed diagnostic**: RASP as a "litmus test" tool rather than a proposed SOTA method is refreshingly honest framing. The collapse severity gradient (RASP step ~10, Standard step ~60, unpruned never) is a clean experimental result with clear mechanistic interpretation.

- **Structured vs. unstructured distinction**: Showing that unstructured pruning at the same sparsity does NOT cause collapse localizes the phenomenon to structured pruning, narrowing and strengthening the claim.

- **Multi-method comparison**: Testing RASP, Standard, GRASPrune, Bonsai, Gradient-only, Magnitude-only, and Random at the same sparsity provides convincing evidence that the collapse speed varies systematically rather than being an artifact of a single comparison.

- **Honest handling of negative/null results**: The paper pivoted from "RASP enables better RLVR recovery" to "structural pruning breaks RLVR alignment" based on experimental evidence. The SFT gap nonsignificance at 20% (p=0.25) is reported transparently.

### Weaknesses

- **Claim 1 (reward-accuracy decoupling) novelty is questionable**: The paper presents this as a "universal" finding but tests only one GRPO configuration on one benchmark with greedy decoding. It is well-known in the RL-from-human-feedback literature that reward model exploitation can lead to reward improvement without genuine task improvement. Whether this is a GRPO bug, a reward shaping issue (binary reward on problems the model already solves at 81%), or a GSM8K-specific saturation artifact (the unpruned model is already near its capacity) is not disambiguated. If the unpruned model is at 81% and can only reach ~85% at best, a flat accuracy trajectory under limited training (100 steps) is unsurprising and does not constitute a "universal" decoupling.

- **Limited novelty of the "Redundancy-Stability Tradeoff"**: The core observation---that RL training requires exploration diversity which structured pruning disrupts---is predictable from first principles of policy gradient methods. Removing entire computational pathways reduces the model's ability to generate diverse rollouts, causing GRPO groups to collapse to zero standard deviation. This is not so much a "tradeoff" as a consequence of how GRPO works: it needs variance in completions to compute advantages. The mechanistic explanation is underdeveloped.

- **RASP's contribution is unclear given it "fails"**: The paper proposes RASP but then shows it is actively harmful for RLVR and only marginally (nonsignificantly at 20%) beneficial for SFT. At 25% the SFT gap reaches significance (p=0.008, +5.75pp), but the paper's own decision log reveals this number may come from experiments still running at submission time. The primary contribution---a scoring function whose recommended use case is already well-served by standard importance pruning---is thin.

- **Self-Healing comparison is incomplete**: The paper claims to "narrow" Self-Healing's results by showing structured pruning fails under RLVR, while Self-Healing uses unstructured pruning. But Self-Healing explicitly studies structured pruning as well (their Table 2 includes layer-level structured pruning). The paper should directly address Self-Healing's structured pruning results at 25% sparsity.

- **Missing important baselines and related work**:
  - **Boiling Frog (2026)**: Cited but not experimentally compared. Their iterative prune-tune approach directly addresses the collapse problem---does gradual pruning avoid GRPO collapse?
  - **"Doing More With Less" (2026)**: Their finding that structured pruning degrades test-time scaling is essentially the same observation from a different angle. The relationship is not sufficiently discussed.
  - **Unstructured pruning at 50%**: Testing only 20% unstructured is uninformative---the meaningful comparison is whether structured 20% vs unstructured 50% (matched actual performance impact) both collapse.
  - **No comparison with SemiStructured (2:4 or N:M)**: RAC (cited) works on 2:4 pruning; testing this middle ground would strengthen the "structural pathway removal" explanation.

- **Single GRPO configuration**: The paper uses one GRPO setup (lr=1e-6, beta=0, temp=0.7, 1000 samples, 1 epoch, max_completion=1024). The decision log reveals 8 failed GRPO versions before reaching the current configuration (v1-v7 all failed for engineering reasons: truncation, OOM, disk full). Whether collapse is robust across GRPO hyperparameters (different learning rates, KL coefficients, temperatures, longer training) is not systematically tested. Beta=0 (no KL penalty) is an unusually aggressive choice for post-pruning recovery.

- **Circular reasoning in collapse correlation**: The paper claims "collapse speed correlates with redundancy removal" (r=0.95), but collapse speed (a property of the GRPO training) is being correlated with post-SFT model quality---not directly with a redundancy measure. If better SFT recovery leads to slower GRPO collapse simply because stronger models are more robust to RL instabilities, this is unsurprising and does not uniquely implicate redundancy as the mechanism.

### Questions for Authors

1. On the unpruned model: if GRPO reward reaches 0.661 after 100 steps but accuracy stays at 81.27%, what IS the reward measuring? Can you show sample outputs at step 0 vs step 100 to verify the reward signal is meaningful (not degenerate formatting, not length gaming)?

2. What happens if you use KL-constrained GRPO (beta > 0, e.g., beta = 0.01-0.1)? Does this prevent collapse on pruned models? If so, the "fundamental" nature of the tradeoff is weakened.

3. Self-Healing's structured pruning results (their Table 2) show RLVR recovery for layer-pruned models. How do you reconcile this with your claim that "structural pruning breaks RLVR"? Is it width vs. depth pruning that matters?

4. The decision log shows the original claim was "RASP 29% vs Standard 1%" which was later found to be an eval bug (max_new_tokens=10 truncation). After correction both are ~27-31%. How confident are you that the remaining results (especially collapse step measurements) are free of similar bugs?

5. At what training budget (steps, samples) does GRPO begin improving accuracy for the unpruned model? If 100 steps is simply insufficient, the "universal decoupling" claim is wrong---it is a sample efficiency issue.

### Assessment of Novelty

The paper's novelty rests on two findings: (a) GRPO training collapse on structurally pruned models, and (b) the correlation between redundancy removal and collapse speed. Finding (a) is moderately novel---it documents a failure mode that others may have observed but not published, though it is predictable from policy gradient theory (removing diverse computation pathways reduces rollout diversity, which is fatal for advantage estimation). Finding (b) is a useful empirical characterization but the "Redundancy-Stability Tradeoff" framing overstates what is fundamentally an observation that weaker models collapse faster under RL training. The RASP method itself contributes minimal novelty: CKA-based pruning scores exist (MPruner, FANG), and the specific formula $S(h) = I(h) \times (1-F(h))^\alpha$ is a simple heuristic that the paper's own experiments show provides no significant advantage at the primary sparsity level (20%) and actively hurts for RLVR. The "diagnostic tool" framing is creative but represents a contribution below the bar for a competitive venue unless the mechanistic understanding is substantially deepened (e.g., connecting collapse to specific representational properties of the pruned architecture, or proposing a fix).

### Assessment of Related Work

The related work section (in the full tex draft) is thorough and well-organized, covering structured pruning, pruning-aware recovery, RLVR dynamics, and CKA-based pruning. However, several gaps exist:

1. **Self-Healing's structured pruning results are under-discussed**. The paper frames itself as narrowing Self-Healing to "unstructured pruning only," but Self-Healing does test structured (layer-level) pruning. The paper needs to explicitly address whether depth-pruning triggers the same collapse.

2. **GRPO failure modes literature is missing**. There is substantial work on RLHF/GRPO reward hacking and training instabilities (e.g., reward over-optimization curves from Gao et al. 2022). The reward-accuracy decoupling finding should be positioned within this broader context.

3. **The test-time compute / reasoning efficiency literature** (scaling inference compute, best-of-N, etc.) is relevant: if GRPO "improves" reward but not greedy accuracy, does it improve pass@k accuracy? This is a standard evaluation in RLVR papers.

4. **Missing citations**: DieT (2026), NIRVANA (2025), and TraceNAS (2026) from the literature map are relevant pruning baselines that could strengthen the five-method comparison. The RL Squeezes / SFT Expands paper is cited in framing documents but should appear more prominently since it is the theoretical backbone of the proposed mechanism.

5. **OPSD (2026)** is cited but the comparison is one-sided: if post-RL distillation avoids the collapse by distilling rather than RL-training the pruned model, this is a natural solution the paper should discuss.

### Minor Issues

- The paper has multiple "[TBD]" placeholders in the working draft, suggesting it is far from submission-ready. The abstract is blank. The conclusion is blank.
- The paper title has shifted across drafts (from "Recovery-Aware Structured Pruning" to "Structured Pruning Breaks RLVR Alignment" to "The Redundancy-Stability Tradeoff"). This identity crisis reflects the major narrative pivot documented in the decision log (D044) and suggests the framing is not yet stable.
- Tables in the "dream" draft report numbers (e.g., 25% sparsity results, cross-model results, multi-seed results, extended benchmarks) that appear to be projections rather than confirmed experimental results. The project overview shows many of these experiments are still RUNNING or PREPARING.
- The paper uses "frac_zero_std" as a collapse metric without formal definition or justification for why this specific metric captures policy degeneration.
- Statistical reporting is inconsistent: some comparisons use Fisher's exact test, others report Spearman correlation, and the mixed-effects regression in the dream report is not mentioned in the main paper draft.

### Preliminary Score: 3/6
### Confidence: 4/5

The paper documents an interesting failure mode (GRPO collapse on structurally pruned models) that is worth reporting, but the novelty and depth of analysis are below the bar for a top venue. The core finding is predictable from RL theory, the proposed method (RASP) is shown to be ineffective for its intended purpose, and the "Redundancy-Stability Tradeoff" framing overstates what is largely an observation that more aggressively damaged models are less trainable. The paper would benefit from: (1) deeper mechanistic analysis of WHY collapse happens (not just WHEN), (2) a proposed mitigation (the RASP-RLVR reversal experiment in D047 could help if successful), and (3) more rigorous GRPO hyperparameter ablation to establish that collapse is robust and not an artifact of the specific configuration used.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74c61b3c-22fe-4d17-af97-deae5ed18e2f",
  "isSidechain": true,
  "agentId": "a7fe9f34d2b39e51d",
  "requestId": "req_011Cb6W9jqZkCdNDg2vQX3nY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "51ad42f1-a38d-4543-abe5-811e004f7e09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "87456414-598d-4dd4-8776-aaed1b39d708",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AEeoayQSgzdbrX17sQfY4E",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3950,
      "cache_read_input_tokens": 78292,
      "output_tokens": 3061,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3950
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3061,
          "cache_read_input_tokens": 78292,
          "cache_creation_input_tokens": 3950,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3950,
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
