# paper bcs scs format

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 60
- **Recorded user turns:** 0
- **Tool calls:** 20
- **Original source:** `logs/workers/worker_paper_bcs_scs_format_20260522T110901.log`
- **Structured JSON:** [`f78b32b02d3168c4518d.json`](../../sessions/f7/f78b32b02d3168c4518d.json)

## Before a recorded user message

60 recorded events

### Log line

_source line 1_

Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.

---

### System

_source line 2_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "tools": [
    "Task",
    "AskUserQuestion",
    "Bash",
    "CronCreate",
    "CronDelete",
    "CronList",
    "Edit",
    "EnterPlanMode",
    "EnterWorktree",
    "ExitPlanMode",
    "ExitWorktree",
    "Glob",
    "Grep",
    "ListMcpResourcesTool",
    "Monitor",
    "NotebookEdit",
    "PushNotification",
    "Read",
    "ReadMcpResourceTool",
    "RemoteTrigger",
    "ScheduleWakeup",
    "Skill",
    "TaskOutput",
    "TaskStop",
    "TodoWrite",
    "ToolSearch",
    "WebFetch",
    "WebSearch",
    "Write",
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__save_project_file"
  ],
  "mcp_servers": [
    {
      "name": "agent-ml-research",
      "status": "connected"
    }
  ],
  "model": "claude-opus-4-6",
  "permissionMode": "bypassPermissions",
  "slash_commands": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api",
    "clear",
    "compact",
    "context",
    "heapdump",
    "init",
    "review",
    "security-review",
    "extra-usage",
    "usage",
    "insights",
    "team-onboarding"
  ],
  "apiKeySource": "none",
  "claude_code_version": "2.1.126",
  "output_style": "default",
  "agents": [
    "claude",
    "Explore",
    "general-purpose",
    "Plan",
    "statusline-setup"
  ],
  "skills": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api"
  ],
  "plugins": [],
  "analytics_disabled": false,
  "uuid": "bd41536a-4b7d-4fe9-b73a-7b426f7b4553",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Runtime record

_source line 3_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1779457200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "7b1a429a-3928-4b0a-b1f2-cde110cd1f9c",
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by investigating the current state of BCS/SCS formatting across all .tex files in the paper directory.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "dc536d57-46b9-4891-8080-bdf901fccf5b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TMMv2TWjgegSngcxpcZUiQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11899,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11899
      },
      "output_tokens": 33,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 5_

先调查全文 BCS/SCS 的排版格式现状。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "b6b5793b-c3d0-4095-8991-9b111c037c46",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TMMv2TWjgegSngcxpcZUiQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11899,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11899
      },
      "output_tokens": 33,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 6_

<details open><summary>🔧 Tool call — Grep · `toolu_018ZvsLaYpZRAtxvP5aFT8KR`</summary>

```json
{
  "pattern": "BCS|SCS|\\\\textsc\\{[Bb][Cc][Ss]\\}|\\\\textsc\\{[Ss][Cc][Ss]\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "06e11d7d-28fa-449d-af11-b0d817825765",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TMMv2TWjgegSngcxpcZUiQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11899,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11899
      },
      "output_tokens": 33,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-22T11:09:15.119Z_

<details><summary>↩ Tool result · reported error · `toolu_018ZvsLaYpZRAtxvP5aFT8KR`</summary>

```text
&lt;tool_use_error>Path does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "09e74cca-8cf5-4377-80e8-449d5842ca17",
  "tool_use_result": "Error: Path does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction."
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Grep · `toolu_01BiFkGGcK8kcUnH1Sg4Yn7h`</summary>

```json
{
  "pattern": "\\\\newcommand.*[Bb][Cc][Ss]|\\\\newcommand.*[Ss][Cc][Ss]|\\\\def.*[Bb][Cc][Ss]|\\\\def.*[Ss][Cc][Ss]",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "7727ce83-794d-4693-b629-890c1d529701",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TMMv2TWjgegSngcxpcZUiQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11899,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11899
      },
      "output_tokens": 33,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-22T11:09:16.523Z_

<details><summary>↩ Tool result · reported error · `toolu_01BiFkGGcK8kcUnH1Sg4Yn7h`</summary>

```text
&lt;tool_use_error>Path does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "e529799f-52a5-4a1b-82d5-fc370435ef61",
  "tool_use_result": "Error: Path does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction."
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Glob · `toolu_01DBi84KDAFjbeWj4YczY455`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "e0396143-49cd-4598-9dbc-ee7aec20e9d9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Un9w6KqPmbAcJdzkejCwrP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 667,
      "cache_read_input_tokens": 23740,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 667
      },
      "output_tokens": 62,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-22T11:09:20.736Z_

<details><summary>↩ Tool result · `toolu_01DBi84KDAFjbeWj4YczY455`</summary>

```text
artifacts/dream_reports/dream_20260515T053106/best/paper.tex
artifacts/dream_reports/dream_20260515T053106/median/paper.tex
artifacts/dream_reports/dream_20260515T053106/worst/paper.tex
artifacts/dream_reports/dream_20260515T113743/best/paper.tex
artifacts/dream_reports/dream_20260515T113743/median/paper.tex
artifacts/dream_reports/dream_20260515T113743/worst/paper.tex
artifacts/dream_reports/dream_20260515T140829/best/paper.tex
artifacts/dream_reports/dream_20260515T140829/median/paper.tex
artifacts/dream_reports/dream_20260515T140829/worst/paper.tex
artifacts/_project/paper/dataset_stats.tex
artifacts/paper/tables/dataset_stats.tex
artifacts/_project/paper/sdgd_negative.tex
artifacts/_project/paper/experimental_setup.tex
docs/paper/conclusion.tex
artifacts/_project/paper/results.tex
artifacts/dream_reports/dream_20260516T073533/best/paper.tex
artifacts/dream_reports/dream_20260516T073533/median/paper.tex
artifacts/dream_reports/dream_20260516T073533/worst/paper.tex
docs/paper/supplementary.tex
artifacts/acknowledgements_draft.tex
docs/paper/prompt_appendix.tex
docs/paper/checklist.tex
artifacts/error_taxonomy_cross_model_table.tex
artifacts/permutation_equivalence_latex.tex
artifacts/_project/paper/docred_ridge_appendix.tex
artifacts/docred_ridge_appendix.tex
docs/paper/sdgd_negative.tex
docs/paper/related_work.tex
docs/paper/abstract.tex
docs/paper/introduction.tex
docs/paper/main.tex
docs/paper/experimental_setup.tex
docs/paper/discussion.tex
docs/paper/results.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "c092d6bf-eed4-4459-a284-3f4131b8b73a",
  "tool_use_result": {
    "filenames": [
      "artifacts/dream_reports/dream_20260515T053106/best/paper.tex",
      "artifacts/dream_reports/dream_20260515T053106/median/paper.tex",
      "artifacts/dream_reports/dream_20260515T053106/worst/paper.tex",
      "artifacts/dream_reports/dream_20260515T113743/best/paper.tex",
      "artifacts/dream_reports/dream_20260515T113743/median/paper.tex",
      "artifacts/dream_reports/dream_20260515T113743/worst/paper.tex",
      "artifacts/dream_reports/dream_20260515T140829/best/paper.tex",
      "artifacts/dream_reports/dream_20260515T140829/median/paper.tex",
      "artifacts/dream_reports/dream_20260515T140829/worst/paper.tex",
      "artifacts/_project/paper/dataset_stats.tex",
      "artifacts/paper/tables/dataset_stats.tex",
      "artifacts/_project/paper/sdgd_negative.tex",
      "artifacts/_project/paper/experimental_setup.tex",
      "docs/paper/conclusion.tex",
      "artifacts/_project/paper/results.tex",
      "artifacts/dream_reports/dream_20260516T073533/best/paper.tex",
      "artifacts/dream_reports/dream_20260516T073533/median/paper.tex",
      "artifacts/dream_reports/dream_20260516T073533/worst/paper.tex",
      "docs/paper/supplementary.tex",
      "artifacts/acknowledgements_draft.tex",
      "docs/paper/prompt_appendix.tex",
      "docs/paper/checklist.tex",
      "artifacts/error_taxonomy_cross_model_table.tex",
      "artifacts/permutation_equivalence_latex.tex",
      "artifacts/_project/paper/docred_ridge_appendix.tex",
      "artifacts/docred_ridge_appendix.tex",
      "docs/paper/sdgd_negative.tex",
      "docs/paper/related_work.tex",
      "docs/paper/abstract.tex",
      "docs/paper/introduction.tex",
      "docs/paper/main.tex",
      "docs/paper/experimental_setup.tex",
      "docs/paper/discussion.tex",
      "docs/paper/results.tex"
    ],
    "durationMs": 28,
    "numFiles": 34,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Grep · `toolu_015TTLogq4FwdSUS8S4jCQj3`</summary>

```json
{
  "pattern": "BCS|SCS|\\\\textsc\\{[Bb][Cc][Ss]\\}|\\\\textsc\\{[Ss][Cc][Ss]\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": true,
  "head_limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "a20a1710-50b5-4a5c-8d97-447c6e7b1df6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QJjaFRtCtNqrdjvWHqcwWC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 592,
      "cache_read_input_tokens": 24407,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 592
      },
      "output_tokens": 34,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-22T11:09:36.369Z_

<details><summary>↩ Tool result · `toolu_015TTLogq4FwdSUS8S4jCQj3`</summary>

```text
&lt;persisted-output>
Output too large (30.1KB). Full output saved to: /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction/69d255ce-db0b-472a-b13f-c39e9fbc3874/tool-results/toolu_015TTLogq4FwdSUS8S4jCQj3.txt

Preview (first 2KB):
docs/paper/related_work.tex:10:[Omitted long matching line]
docs/paper/related_work.tex:16:\paragraph{SCS novelty.}
docs/paper/related_work.tex:18:[Omitted long matching line]
docs/paper/main.tex:44:BCS-controlled experiments use greedy decoding with a single seed; residual SD${}\,=\,0.88$\,pp is 18--44\% of the observed effect size (Appendix~\ref{app:variance-decomposition}), so detection is robust but point estimates carry meaningful uncertainty.
docs/paper/main.tex:48:DocRED exhibits severe multicollinearity (VIF${}\,=\,50.9$), preventing reliable BCS effect quantification; semipartial $R^2{}\,=\,5.6\%$ serves only as directional evidence, and the count${}\times{}$BCS interaction is partially confounded by BCS range restriction at higher counts (Appendix~\ref{sec:appendix_factorial}).
docs/paper/main.tex:52:BCS batch-level prediction is significant in RE but not detected in NER, where errors scatter across miss, boundary, and type modes (Appendix~\ref{app:relaxed-matching}).
docs/paper/main.tex:84:\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\approx$51\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\Delta$, in pp) is 77--87\% as large on Llama-3.1-8B as on Qwen3-32B.}
docs/paper/main.tex:102:\caption{NER batch-level BCS--F1 correlation across models. $^\dagger$Partial correlation controlling for type frequency. $^\ddagger$LLaMA-70B count\_12 shows $r{=}{-}0.42$ ($p{=}0.034$, uncorrected; Bonferroni $p{=}0.069$); pooled and count\_6 are null, consistent with sampling noise at $n{=}25$. The null is observed on three models; Gemini remains untested.}
docs/paper/main.tex:106:\textbf{Model} & \textbf{NER BCS--F1 $r$} & \textbf{Status} \\
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "e92f5d61-5154-4113-adb9-862ce5416539",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/related_work.tex:10:[Omitted long matching line]\ndocs/paper/related_work.tex:16:\\paragraph{SCS novelty.}\ndocs/paper/related_work.tex:18:[Omitted long matching line]\ndocs/paper/main.tex:44:BCS-controlled experiments use greedy decoding with a single seed; residual SD${}\\,=\\,0.88$\\,pp is 18--44\\% of the observed effect size (Appendix~\\ref{app:variance-decomposition}), so detection is robust but point estimates carry meaningful uncertainty.\ndocs/paper/main.tex:48:DocRED exhibits severe multicollinearity (VIF${}\\,=\\,50.9$), preventing reliable BCS effect quantification; semipartial $R^2{}\\,=\\,5.6\\%$ serves only as directional evidence, and the count${}\\times{}$BCS interaction is partially confounded by BCS range restriction at higher counts (Appendix~\\ref{sec:appendix_factorial}).\ndocs/paper/main.tex:52:BCS batch-level prediction is significant in RE but not detected in NER, where errors scatter across miss, boundary, and type modes (Appendix~\\ref{app:relaxed-matching}).\ndocs/paper/main.tex:84:\\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\\approx$51\\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\\Delta$, in pp) is 77--87\\% as large on Llama-3.1-8B as on Qwen3-32B.}\ndocs/paper/main.tex:102:\\caption{NER batch-level BCS--F1 correlation across models. $^\\dagger$Partial correlation controlling for type frequency. $^\\ddagger$LLaMA-70B count\\_12 shows $r{=}{-}0.42$ ($p{=}0.034$, uncorrected; Bonferroni $p{=}0.069$); pooled and count\\_6 are null, consistent with sampling noise at $n{=}25$. The null is observed on three models; Gemini remains untested.}\ndocs/paper/main.tex:106:\\textbf{Model} & \\textbf{NER BCS--F1 $r$} & \\textbf{Status} \\\\\ndocs/paper/main.tex:119:\\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin. Spearman $\\rho$ computed over $n=148$ batches (NER), $n=154$ (RE), and $n=110$ (DocRE). IntraSub scales monotonically with BCS across all three datasets. DocRE missed rates decrease with BCS, indicating high-confusability errors shift from omission to substitution.}\ndocs/paper/main.tex:124: & & \\multicolumn{5}{c}{\\textbf{BCS Bin}} & & \\\\\ndocs/paper/main.tex:142:\\caption{Cross-model replication of IntraSub--BCS Spearman correlation on FewRel RE. $^\\dagger$LLaMA-70B has only 20 batches with 17.4\\% missed rate; the null is attributable to insufficient power rather than absence of the effect.}\ndocs/paper/main.tex:159:We construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent (i.e., highly confusable) types share a color. Each color class forms one extraction batch, and predictions are merged via set union.\ndocs/paper/main.tex:162:\\item Compute pairwise SCS matrix $S_{ij} = \\cos(\\text{embed}(t_i), \\text{embed}(t_j))$.\ndocs/paper/main.tex:170:We compare four modes: (i)~\\textbf{single\\_pass}, the undecomposed baseline; (ii)~\\textbf{sdgd\\_zero}, SCS-guided partitioning; (iii)~\\textbf{random\\_batch}, random partitioning with matched batch sizes; and (iv)~\\textbf{per\\_type}, the extreme case where each type is extracted in isolation.\ndocs/paper/main.tex:230:[Omitted long matching line]\ndocs/paper/main.tex:232:A $2 \\times 2$ factorial sensitivity check on FewRel (count $\\in \\{8, 16\\}$, BCS low/high; $n = 54$) was inconclusive ($p_{\\text{TOST}} = 0.56$) due to limited power; this does not contradict the primary finding but limits generalization beyond the regression framework. The Few-NERD factorial (\\S\\ref{sec:multi_channel}) similarly did not reach significance ($p = 0.50$). The regression approach provides the stronger test by leveraging the full count range.\ndocs/paper/main.tex:255:[Omitted long matching line]\ndocs/paper/main.tex:258:With expanded batches ($n{=}55$ per count level, up from $n{=}5$), the DocRED $2 \\times 2$ factorial (count $\\in \\{16, 32\\}$, BCS median split) yields an apparent interaction ($-$9.4\\,pp, 95\\% CI [$-$12.9, $-$6.0]): the BCS effect is $-$25.0\\,pp at count 16 but $-$15.7\\,pp at count 32. However, this attenuation is confounded by BCS range restriction: higher-count batches have narrower BCS ranges (spread 0.26 vs.\\ 0.38), limiting achievable extremes.\ndocs/paper/main.tex:261:[Omitted long matching line]\ndocs/paper/main.tex:266:[Omitted long matching line]\ndocs/paper/main.tex:271:Section~\\ref{sec:centrality_confound} identifies a centrality confound in MAVEN's per-type BCS--F1 correlation: both embeddings show a \\emph{positive} raw correlation, opposite to the expected direction. Here we formalize this analysis by identifying specific confounders for each embedding and testing whether the BCS--F1 relationship survives partial correlation controlling for these confounders.\ndocs/paper/main.tex:274:For each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:\ndocs/paper/main.tex:276:\\item \\textbf{MiniLM}: BCS correlates with log type frequency ($r = 0.201$). Frequent types have more training signal and are extracted more reliably, which produces the positive BCS--F1 association.\ndocs/paper/main.tex:277:\\item \\textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors, central, well-represented types that the model extracts well.\ndocs/paper/main.tex:281:Table~\\ref{tab:residualized_bcs} reports raw Spearman $\\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.\ndocs/paper/main.tex:286:\\caption{MAVEN per-type BCS--F1 correlation before and after controlling for centrality confounders. Raw correlations are Spearman $\\rho$; partial correlations are Pearson $r$ from residualized regression. Degree centrality is computed on the SCS graph at threshold 0.7. All values from experiment \\texttt{exp\\_maven\\_residualized\\_bcs}.}\ndocs/paper/main.tex:305:[Omitted long matching line]\ndocs/paper/main.tex:307:[Omitted long matching line]\ndocs/paper/main.tex:312:To rule out degree centrality as a confound in cross-domain datasets, we compute partial correlations between BCS and accuracy controlling for batch mean degree centrality (mean off-diagonal SCS per type, averaged across batch members).\ndocs/paper/main.tex:317:\\caption{BCS--accuracy partial correlation controlling for degree centrality. FewRel shows minimal attenuation (VIF${}\\,=\\,1.18$, low collinearity). DocRED shows high BCS--centrality collinearity (VIF${}\\,=\\,50.9$, $r = 0.99$), but the partial correlation remains highly significant.}\ndocs/paper/main.tex:329:[Omitted long matching line]\ndocs/paper/main.tex:332:[Omitted long matching line]\ndocs/paper/main.tex:334:\\subsection{NER BCS-Null Power Analysis}\ndocs/paper/main.tex:337:[Omitted long matching line]\ndocs/paper/main.tex:342:[Omitted long matching line]\ndocs/paper/main.tex:344:\\subsection{Domain Distribution in Extreme-BCS Batches}\ndocs/paper/main.tex:347:[Omitted long matching line]\ndocs/paper/main.tex:360:\\textbf{Condition} & \\textbf{Accuracy} & \\textbf{Mean BCS} \\\\\ndocs/paper/main.tex:379:[Omitted long matching line]\ndocs/paper/main.tex:382:[Omitted long matching line]\ndocs/paper/main.tex:385:[Omitted long matching line]\ndocs/paper/main.tex:387:\\subsection{Cross-Prompt-Variant BCS Correlation}\ndocs/paper/main.tex:390:To verify that the BCS--accuracy relationship is not an artifact of a specific prompt template, we evaluate four structurally distinct prompt variants on FewRel 80-relation RE at two count levels (8 and 32), with 10 random batches per condition (Table~\\ref{tab:prompt_variants}).\ndocs/paper/main.tex:395:\\caption{BCS--accuracy Pearson correlation across four prompt variants. At count 32, all four variants show negative BCS--accuracy correlations ($r \\leq -0.47$), with two reaching $p < 0.05$. At count 8, the narrower BCS range reduces statistical power.}\ndocs/paper/main.tex:413:[Omitted long matching line]\ndocs/paper/main.tex:415:\\section{BCS Aggregation Sensitivity}\ndocs/paper/main.tex:418:We define Batch Confusability Score (BCS) as the \\emph{mean} pairwise SCS across all type pairs in a batch (\\S\\ref{sec:bcs_controlled}). An alternative definition takes the \\emph{maximum} pairwise SCS within each batch to capture the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice (Table~\\ref{tab:bcs_aggregation}).\ndocs/paper/main.tex:423:\\caption{BCS--accuracy regression under mean vs.\\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p \\approx 0.60$; MAX $p \\approx 0.44$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}\ndocs/paper/main.tex:441:\\section{BCS-Controlled Detailed Results}\ndocs/paper/main.tex:447:\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\ndocs/paper/main.tex:452:\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\ndocs/paper/main.tex:462:DocRED regressions (\\S\\ref{sec:bcs_controlled}) use OLS on $n = 55$ batches (15 high-BCS + 15 low-BCS + 25 random) per count level, with one predictor. At count 16, adjusted $R^2 = 0.646$ (unadjusted: 0.653; 95\\% CI [0.53, 0.77]); at count 32, adjusted $R^2 = 0.606$ (unadjusted: 0.614; 95\\% CI [0.47, 0.75]). The small shrinkage ($\\Delta R^2 \\leq 0.01$) indicates the unadjusted values are not inflated by the predictor-to-sample ratio.\ndocs/paper/main.tex:467:To test whether the BCS--accuracy relationship depends on the output format, we run both constrained (enum-based) and unconstrained (free-text) decoding on the same 25 batch type sets from the FewRel 80-relation pool (13 low-BCS, 12 high-BCS; count 8). Each batch uses identical instances and type sets; only the decoding format differs (Table~\\ref{tab:format_independence}).\ndocs/paper/main.tex:472:\\caption{Paired comparison of constrained vs.\\ unconstrained decoding on 25 identical FewRel batch type sets. Both formats yield virtually identical BCS--accuracy correlations (Fisher $z \\approx 0$), confirming the confusability effect is format-independent. Mean accuracy is also unchanged ($\\Delta = -0.08$\\,pp), ruling out a format-driven accuracy shift.}\ndocs/paper/main.tex:479:Pearson $r$ (BCS vs.\\ acc) & $-$0.448 ($p = 0.025$) & $-$0.439 ($p = 0.028$) \\\\\ndocs/paper/main.tex:480:Spearman $\\rho$ (BCS vs.\\ acc) & $-$0.157 ($p = 0.455$) & $-$0.144 ($p = 0.492$) \\\\\ndocs/paper/main.tex:489:[Omitted long matching line]\ndocs/paper/main.tex:497:\\caption{Per-batch accuracy (\\%) under constrained and unconstrained decoding on 25 identical FewRel batch type sets (count 8, 96 instances each). 23/25 batches yield identical accuracy; the two exceptions differ by exactly one sample ($\\Delta = -1.04$\\,pp). L = low-BCS, H = high-BCS.}\ndocs/paper/main.tex:502:\\textbf{Batch} & \\textbf{Group} & \\textbf{BCS} & \\textbf{Constr.} & \\textbf{Unconstr.} & \\textbf{$\\Delta$} \\\\\ndocs/paper/main.tex:537:A potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol.\ndocs/paper/main.tex:542:\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\ndocs/paper/main.tex:547:& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\ndocs/paper/main.tex:556:\\multicolumn{7}{l}{\\footnotesize $^\\dagger$BCS range (IQR\\,=\\,0.033) insufficient for regression; slope not interpretable.} \\\\\ndocs/paper/main.tex:561:The within-pool slope ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.509; permutation $p \\approx 0.60$). The smaller quartile gap ($-$3.92\\,pp vs.\\ $-$5.31\\,pp) reflects the narrower BCS range within the 80-relation pool (Appendix~\\ref{sec:appendix_within_pool}).\ndocs/paper/main.tex:563:In the full 80-relation condition, natural BCS variation is insufficient (IQR${}=0.033$) to yield a detectable effect ($n=25$, slope${}=+0.221$, $p \\approx 0.76$). This does not invalidate the confusability effect; the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied, but establishes that natural schema sampling at this scale does not produce sufficient BCS contrast for detection.\ndocs/paper/main.tex:565:\\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}\ndocs/paper/main.tex:568:Table~\\ref{tab:scs-ablation} compares predictive accuracy of name-only SCS against name+definition SCS across three datasets.\ndocs/paper/main.tex:573:\\caption{Pearson correlation between SCS and empirical confusion rate. ``Def'' concatenates type name with definition before embedding. All correlations significant ($p < 0.001$). The inconsistent direction of $\\Delta r$ indicates that definitions provide no systematic benefit.}\ndocs/paper/main.tex:577:Dataset & SCS$_\\text{name}$ $r$ & SCS$_\\text{def}$ $r$ & $\\Delta r$ & Matrix corr. \\\\\ndocs/paper/main.tex:586:Few-NERD is the only dataset whose prompts include type definitions; for MAVEN and FewRel, prompts use type names alone, so name-only SCS directly matches model input. The high matrix correlation (0.66--0.89) confirms that type names capture the dominant semantic structure.\ndocs/paper/main.tex:590:From the 80-type confusion matrix, we extract the $\\binom{16}{2} = 120$ pairs among the 16 validation-origin types (fully disjoint from the 64 training-pool types). The SCS--confusion Spearman correlation remains positive and significant ($\\rho = 0.216$, $p = 0.018$), nearly identical to the full 80-type pool ($\\rho = 0.218$, $p < 0.001$, $n = 3{,}160$ pairs), ruling out training-set contamination as the driver of the observed relationship.\ndocs/paper/main.tex:597:[Omitted long matching line]\ndocs/paper/main.tex:602:[Omitted long matching line]\ndocs/paper/main.tex:605:The inter-pair SCS correlation $\\rho = 0.35$ is estimated from pairs sharing a common type. At $\\rho = 0.20$ (halved correlation), a parallel simulation yields batch $R^2 \\approx 0.22$; at $\\rho = 0.50$, the correlation structure approaches the positive-definiteness boundary; $\\rho = 0.35$ thus sits in a stable regime. The simulation is illustrative; the pooled semipartial $R^2 = 0.273$ (\\S\\ref{sec:bcs_controlled}) is the primary evidence.\ndocs/paper/main.tex:608:[Omitted long matching line]\ndocs/paper/main.tex:610:\\section{BCS Independence from Type Composition}\ndocs/paper/main.tex:613:[Omitted long matching line]\ndocs/paper/main.tex:615:\\section{SCS vs.\\ Simple Baselines}\ndocs/paper/main.tex:618:Table~\\ref{tab:scs_baselines} compares SCS against simple baselines for pairwise confusion prediction.\ndocs/paper/main.tex:623:\\caption{Pairwise confusion prediction: SCS vs.\\ simple baselines. Spearman $\\rho$ between each metric and the empirical confusion rate. SCS outperforms all baselines on FewRel; the margin is smaller on Few-NERD, where hierarchical naming conventions provide partial signal to string-based metrics. $^\\dagger$42\\% of pairs lack WordNet coverage.}\ndocs/paper/main.tex:630:FewRel & SCS (embedding) & \\textbf{0.218} & $< 0.001$ \\\\\ndocs/paper/main.tex:635:Few-NERD & SCS (embedding) & \\textbf{0.166} & $< 0.001$ \\\\\ndocs/paper/main.tex:646:FewRel combines 64 train-split and 16 val-split relation types into a single 80-type pool.  Train-origin types show numerically lower accuracy ($-8.8$\\,pp, $p = 0.06$; see Limitations), raising the question of whether differential pre-training exposure confounds the BCS--accuracy relationship.  We test this by adding a per-batch \\emph{train-origin ratio} (fraction of relation types drawn from the train split) as a covariate in the BCS--accuracy regression.\ndocs/paper/main.tex:650:\\text{acc} = \\beta_0 + \\beta_{\\text{BCS}} \\!\\cdot\\! \\text{BCS} + \\beta_{\\text{orig}} \\!\\cdot\\! \\text{train\\_origin\\_ratio} + \\varepsilon\ndocs/paper/main.tex:653:\\paragraph{Results.}  The BCS partial effect is unchanged after controlling for split-origin: $\\beta_{\\text{BCS}} = -0.416$, $p < 0.001$ (vs.\\ $\\beta = -0.412$, $p < 0.001$ without the covariate).  Train-origin ratio is not independently significant ($\\beta_{\\text{origin}} = -0.057$, $p = 0.245$), and $\\Delta R^2 = 0.005$.  The BCS--accuracy relationship is therefore not confounded by differential pre-training exposure at the batch level.\ndocs/paper/main.tex:655:Pairwise SCS distributions do not differ significantly between train-origin (64 types, mean\\,=\\,0.880) and val-origin (16 types, mean\\,=\\,0.874) subsets (Mann-Whitney $p = 0.754$, Cohen's $d = 0.081$); the train/val split does not introduce systematic confusability bias.\ndocs/paper/main.tex:685:[Omitted long matching line]\ndocs/paper/main.tex:690:To test whether the two-dimensional degradation pattern generalizes across models, we replicate the count-curve and BCS-controlled experiments on Meta-LLaMA-3.1-70B-Instruct (FP8 quantization). All batch compositions, type pools, and test samples are identical to those used for Qwen3-32B (\\S\\ref{sec:count_curves}, \\S\\ref{sec:bcs_controlled}).\ndocs/paper/main.tex:723:For the confusability dimension (Dimension 2), at count 16 on FewRel, LLaMA-70B achieves low-BCS accuracy of 0.708 versus high-BCS accuracy of 0.599 ($\\Delta = +10.9$\\,pp, 95\\% CI [$+$3.0, $+$20.1]). The confidence interval excludes zero; the confusability effect is thus confirmed at the 70B scale.\ndocs/paper/main.tex:730:We validate both dimensions on a proprietary model, Gemini 2.5 Flash \\citep{gemini-2025}, accessed via API. This extends the cross-model evidence from open-weight families (Qwen, LLaMA) to a proprietary architecture with unknown training details. We replicate the FewRel count-curve and BCS-controlled experiments using the same 960 balanced samples, batch compositions, and evaluation protocol as Qwen3-32B.\ndocs/paper/main.tex:753:\\paragraph{Dimension~2: BCS-controlled confusability.}\ndocs/paper/main.tex:754:We replicate the BCS-controlled experiment on Gemini 2.5 Flash using extreme-BCS batches at count 8 ($n = 50$; 25 low-BCS, 25 high-BCS) and count 16 ($n = 10$; 5+5).\ndocs/paper/main.tex:756:[Omitted long matching line]\ndocs/paper/main.tex:758:Table~\\ref{tab:cross_model_bcs_summary} summarizes BCS-controlled results across all validated models. Both dimensions thus replicate on a proprietary architecture with unknown training details.\ndocs/paper/main.tex:763:\\caption{Cross-model BCS-controlled FewRel RE summary. All models show significant low-vs-high BCS accuracy gaps. Gap magnitude varies with model capacity (ceiling compression), but the direction is consistent across open-weight (8B--70B) and proprietary architectures.}\ndocs/paper/main.tex:767:\\textbf{Model} & \\textbf{Count} & \\textbf{Low BCS} & \\textbf{High BCS} & \\textbf{$\\Delta$} & \\textbf{95\\% CI} \\\\\ndocs/paper/main.tex:781:[Omitted long matching line]\ndocs/paper/main.tex:786:\\caption{BCS gap under few-shot prompting (FewRel, count 8). Demonstrations improve absolute accuracy on low-BCS batches (+3.3--7.2\\,pp over 0-shot) but provide inconsistent benefit on high-BCS batches (+5.6\\,pp at 1-shot, $-$1.0\\,pp at 5-shot). The confusability gap widens from +18.5\\,pp (0-shot) to +22.8\\,pp (5-shot). All metrics are micro-averaged across batches.}\ndocs/paper/main.tex:790:\\textbf{Condition} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\ndocs/paper/main.tex:799:[Omitted long matching line]\ndocs/paper/main.tex:806:Tables~\\ref{tab:top10_re} and~\\ref{tab:top10_ner} list the ten most frequently confused type pairs on FewRel 80-relation RE and Few-NERD NER. Confusion counts are aggregated bidirectionally across three random seeds (72{,}000 predictions per seed for RE; single-seed 66-type extraction for NER). Table~\\ref{tab:error_examples} provides illustrative confusion instances with SCS values.\ndocs/paper/main.tex:811:[Omitted long matching line]\ndocs/paper/main.tex:815:\\textbf{\\#} & \\textbf{Type A} & \\textbf{Type B} & \\textbf{SCS} & \\textbf{$N$} \\\\\ndocs/paper/main.tex:834:[Omitted long matching line]\ndocs/paper/main.tex:838:\\textbf{\\#} & \\textbf{Type A} & \\textbf{Type B} & \\textbf{SCS} & \\textbf{$N$} \\\\\ndocs/paper/main.tex:857:\\caption{Illustrative confusion instances from FewRel 80-rel RE. All gold-predicted pairs have SCS\\,$>$\\,0.90: \\textit{participant} vs.\\ \\textit{participant of} reverses directionality; \\textit{contains} vs.\\ \\textit{located in} inverts containment; \\textit{part of} vs.\\ \\textit{member of} conflates meronymy with membership. a.t.e.\\ = admin.\\ territorial entity.}\ndocs/paper/main.tex:861:\\textbf{Sentence} & \\textbf{Gold} & \\textbf{Pred.} & \\textbf{SCS} \\\\\ndocs/paper/main.tex:875:[Omitted long matching line]\ndocs/paper/main.tex:880:\\caption{Accuracy (\\%) under original vs.\\ renamed labels on FewRel count-8 batches. Renaming reduced embedding similarity but decreased accuracy in both groups, with a larger drop on high-BCS batches (Cohen's $d = -2.92$) than low-BCS ($d = -1.09$). Interaction: $\\Delta_{\\text{high}} - \\Delta_{\\text{low}} = -5.9$\\,pp ($t = -7.23$, $p < 0.001$).}\ndocs/paper/main.tex:886:Low-BCS ($n=25$)  & 90.1 & 87.1 & $-$3.0 \\\\\ndocs/paper/main.tex:887:High-BCS ($n=25$) & 69.3 & 60.5 & $-$8.8 \\\\\ndocs/paper/main.tex:897:To test whether exact-match F1 masks the BCS signal in NER by conflating boundary errors with type errors, we evaluate three progressively relaxed matching criteria on the full Few-NERD NER dataset ($n = 450$ batches: 6 count levels $\\times$ 25 batches $\\times$ 3 seeds; Table~\\ref{tab:relaxed_matching}).\ndocs/paper/main.tex:902:[Omitted long matching line]\ndocs/paper/main.tex:916:A per-error-mode analysis confirms this null extends to all individual categories: miss ($\\rho = 0.017$), boundary ($\\rho = -0.043$), and type substitution ($\\rho = -0.010$) rates show no BCS association (all $p > 0.3$, $n = 450$). The null holds within each count level (count 2: $r = 0.022$; count 6: $r = 0.110$; count 12: $r = 0.028$; all $p > 0.3$), ruling out count as a confound.\ndocs/paper/checklist.tex:15:Yes (Limitations). SCS/BCS may be misused as a standalone deployment criterion. Since they are proxies for confusability and do not capture domain-specific ambiguity or downstream harms, they should be used for diagnostic monitoring rather than automatic schema rejection or high-stakes deployment decisions.\ndocs/paper/checklist.tex:49:Yes. Table~\\ref{tab:datasets} reports type counts, evaluation unit counts, domain characteristics, and BCS ranges for each dataset. \\S\\ref{sec:datasets} describes dataset provenance and sampling procedures.\ndocs/paper/checklist.tex:67:Yes. \\S\\ref{sec:exp_design} describes both experimental paradigms (count curves and BCS-controlled). \\S\\ref{sec:model} reports decoding parameters (greedy, temperature${}=0$, seed${}=42$) and prompt versions. No hyperparameter search was conducted as this is a zero-shot evaluation study.\ndocs/paper/discussion.tex:6:The confusability signal applies to cross-domain schemas; same-domain schemas exhibit centrality confounding (\\S\\ref{sec:centrality_confound}). Modest pairwise $r^2$ compounds at the batch level because correlated type interactions aggregate within shared prompts (\\S\\ref{sec:bcs_controlled}). The NER--RE asymmetry reflects dispersed error modes and compressed BCS variance (Appendix~\\ref{sec:appendix_ner_power}).\ndocs/paper/discussion.tex:10:[Omitted long matching line]\ndocs/paper/discussion.tex:15:[Omitted long matching line]\ndocs/paper/abstract.tex:2:[Omitted long matching line]\ndocs/paper/abstract.tex:3:(1)~count degradation spans all three tasks (up to $-$49\\,pp); inter-type confusability (measured by BCS) independently predicts RE type substitution errors (VIF${}\\,=\\,1.18$ on FewRel);\ndocs/paper/abstract.tex:4:(2)~BCS independently explains ${\\sim}$27\\% of cross-batch RE accuracy variance on FewRel (semipartial $R^2 = 0.273$ after controlling for degree centrality; VIF${}\\,=\\,1.18$), replicating across three open-weight model families (8B--70B); the NER batch-level null serves as a boundary condition (dispersed error modes, BCS range compression);\ndocs/paper/experimental_setup.tex:13:[Omitted long matching line]\ndocs/paper/experimental_setup.tex:21:Table~\\ref{tab:datasets} summarizes the dataset statistics, including the Schema Confusability Score (SCS) ranges defined in \\S\\ref{sec:scs}.\ndocs/paper/experimental_setup.tex:29:\\textbf{Dataset} & \\textbf{Task} & \\textbf{\\# Types} & \\textbf{\\# Eval Units} & \\textbf{Domain} & \\textbf{BCS Range} & \\textbf{Embedding} \\\\\ndocs/paper/experimental_setup.tex:37:\\caption{Dataset statistics. BCS Range: min--max over count-curve batches. Embedding: model used for SCS/BCS; ranges are not comparable across embedding models. $^\\dagger$Trigger mentions across 8{,}042 sentences.}\ndocs/paper/experimental_setup.tex:41:\\subsection{Schema Confusability Score (SCS)}\ndocs/paper/experimental_setup.tex:45:We define the Schema Confusability Score (SCS) to quantify semantic overlap between types in a schema. Given a type $t$ with name string $\\text{name}(t)$, an embedding function $\\text{embed}(\\cdot)$ maps the type name to a vector representation. The \\textbf{pairwise SCS} between types $t_i$ and $t_j$ is:\ndocs/paper/experimental_setup.tex:48:\\text{SCS}(t_i, t_j) = \\cos\\bigl(\\text{embed}(\\text{name}(t_i)),\\; \\text{embed}(\\text{name}(t_j))\\bigr)\ndocs/paper/experimental_setup.tex:52:For a batch of types $B = \\{t_1, \\ldots, t_k\\}$, the \\textbf{Batch Confusability Score (BCS)} aggregates all pairwise similarities:\ndocs/paper/experimental_setup.tex:54:\\text{BCS}(B) = \\frac{1}{\\binom{k}{2}} \\sum_{i < j,\\; t_i, t_j \\in B} \\text{SCS}(t_i, t_j)\ndocs/paper/experimental_setup.tex:57:[Omitted long matching line]\ndocs/paper/experimental_setup.tex:59:\\paragraph{SCS as a lightweight proxy.}\ndocs/paper/experimental_setup.tex:61:SCS is a pre-hoc proxy computable without running extraction; pairwise correlations with observed type confusion are reported in \\S\\ref{sec:pairwise}. SCS does not capture context-dependent disambiguation or mention-level ambiguity; these contribute to residual variance.\ndocs/paper/experimental_setup.tex:74:[Omitted long matching line]\ndocs/paper/experimental_setup.tex:86:\\paragraph{Experiment 2: BCS-Controlled.}\ndocs/paper/experimental_setup.tex:87:[Omitted long matching line]\ndocs/paper/introduction.tex:10:This study combines correlational analyses with quasi-experimental manipulation (BCS-controlled batches) to characterize how schema properties predict extraction accuracy.\ndocs/paper/introduction.tex:15:[Omitted long matching line]\ndocs/paper/introduction.tex:19:(2)~Pairwise SCS predicts type confusion across NER, RE, and ED (\\S\\ref{sec:pairwise}); at batch level, BCS predicts RE accuracy independent of output format (\\S\\ref{sec:bcs_controlled}) but not NER accuracy at current statistical power; per-type aggregation is confounded by centrality on homogeneous schemas (\\S\\ref{sec:centrality_confound}).\ndocs/paper/introduction.tex:24:[Omitted long matching line]\ndocs/paper/introduction.tex:25:    \\item We document a task-dependent boundary: the RE confusability effect is confirmed as format-independent across three model families, while the NER batch-level BCS null---reported as a boundary condition rather than a negative result---is attributable to dispersed error modes (miss, boundary, type) and BCS range compression (\\S\\ref{sec:bcs_controlled}, \\S\\ref{sec:multi_channel}).\ndocs/paper/results.tex:10:[Omitted long matching line]\ndocs/paper/results.tex:15:We test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate (the fraction of $t_i$ gold instances misclassified as $t_j$) and correlate it with $\\text{SCS}(t_i, t_j)$. Table~\\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\\% CIs.\ndocs/paper/results.tex:29:\\caption{Pairwise SCS--confusion correlation. Confusion rate is bidirectional $C(t_i{\\to}t_j) + C(t_j{\\to}t_i)$ divided by gold frequency sum; CIs are percentile bootstrap ($B{=}10{,}000$). FewRel ($r = 0.187$; \\S\\ref{sec:scs-validation}) excluded (per-instance RE format). Type-level cluster bootstrap CIs exclude zero (Few-NERD [0.069, 0.219]; MAVEN [0.081, 0.185]).}\ndocs/paper/results.tex:37:[Omitted long matching line]\ndocs/paper/results.tex:42:\\caption{Error taxonomy decomposition (Few-NERD NER and FewRel RE). IntraSub scales monotonically with BCS across all evaluated datasets ($\\rho = 0.84\\text{--}1.0$; Table~\\ref{tab:error_taxonomy} includes DocRED). RE missed rates remain flat (10--16\\%), but NER missed rates are substantially higher (43--65\\%) and non-monotonic.}\ndocs/paper/results.tex:46:\\subsection{BCS-Controlled Experiments}\ndocs/paper/results.tex:50:[Omitted long matching line]\ndocs/paper/results.tex:52:[Omitted long matching line]\ndocs/paper/results.tex:55:[Omitted long matching line]\ndocs/paper/results.tex:59:Within-pool analysis confirms slope consistency across pools (permutation $p \\approx 0.60$; Appendix~\\ref{app:within-pool-method}). The 80-relation extreme-batch gap (\\S\\ref{sec:bcs_controlled}) reflects wider BCS range, not stronger per-unit sensitivity.\ndocs/paper/results.tex:64:[Omitted long matching line]\ndocs/paper/results.tex:68:[Omitted long matching line]\ndocs/paper/results.tex:72:[Omitted long matching line]\ndocs/paper/results.tex:78:[Omitted long matching line]\ndocs/paper/results.tex:81:[Omitted long matching line]\ndocs/paper/results.tex:86:[Omitted long matching line]\ndocs/paper/sdgd_negative.tex:5:[Omitted long matching line]",
    "numLines": 161
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Grep · `toolu_01UKhWd4kH2ZD9Mq38bf7X8Y`</summary>

```json
{
  "pattern": "BCS|SCS|\\\\textsc\\{[Bb][Cc][Ss]\\}|\\\\textsc\\{[Ss][Cc][Ss]\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": true,
  "head_limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "c7d3825a-4b79-4443-9d26-d17810d98bed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QJjaFRtCtNqrdjvWHqcwWC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 592,
      "cache_read_input_tokens": 24407,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 592
      },
      "output_tokens": 34,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-22T11:09:38.186Z_

<details><summary>↩ Tool result · `toolu_01UKhWd4kH2ZD9Mq38bf7X8Y`</summary>

```text
&lt;persisted-output>
Output too large (102.7KB). Full output saved to: /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction/69d255ce-db0b-472a-b13f-c39e9fbc3874/tool-results/toolu_01UKhWd4kH2ZD9Mq38bf7X8Y.txt

Preview (first 2KB):
artifacts/docred_ridge_appendix.tex:1:% Appendix E.1: DocRED Ridge Regression (BCS directionality under multicollinearity)
artifacts/docred_ridge_appendix.tex:4:the negative direction of the BCS--accuracy relationship even after
artifacts/docred_ridge_appendix.tex:5:regularizing for the severe BCS--centrality multicollinearity
artifacts/docred_ridge_appendix.tex:7:The standardized BCS coefficient is $\hat{\beta}_{\textsc{bcs}} = -1.53$
artifacts/docred_ridge_appendix.tex:9:An analytic derivation shows that $\hat{\beta}_{\textsc{bcs}} < 0$ for
artifacts/docred_ridge_appendix.tex:14:the sign---not the magnitude---of the BCS coefficient as directional
artifacts/dream_reports/dream_20260515T113743/best/paper.tex:59:A $2{\times}2$ factorial analysis confirms near-additive effects, and a systematic error taxonomy shows monotonic increases in type substitution errors with confusability ($6.2\%{\to}38.4\%$ across BCS quartiles, $\chi^2{=}89.4$, $p{<}10^{-16}$).
artifacts/dream_reports/dream_20260515T113743/best/paper.tex:96:\subsection{Schema Confusability Score (SCS)}
artifacts/dream_reports/dream_20260515T113743/best/paper.tex:98:We define the \textbf{Schema Confusability Score (SCS)} between two types $t_i, t_j$ as the cosine similarity of their embedding representations:
artifacts/dream_reports/dream_20260515T113743/best/paper.tex:100:\text{SCS}(t_i, t_j) = \cos\bigl(\mathbf{e}(t_i),\; \mathbf{e}(t_j)\bigr)
artifacts/dream_reports/dream_20260515T113743/best/paper.tex:105:For a batch of types $B \subseteq \mathcal{S}$, the \textbf{Batch Confusability Score (BCS)} is the maximum pairwise SCS within the batch:
artifacts/dream_reports/dream_20260515T113743/best/paper.tex:107:\text{BCS}(B) = \max_{t_i, t_j \in B,\; i \neq j} \text{SCS}(t_i, t_j)
artifacts/dream_reports/dream_20260515T113743/best/paper.tex:114:\textbf{Extreme-batch comparisons} fix $|B|$ and construct high-BCS vs.\ low-BCS batches.
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "45f23d48-64e8-449d-ab0b-35786ef6a8b5",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/docred_ridge_appendix.tex:1:% Appendix E.1: DocRED Ridge Regression (BCS directionality under multicollinearity)\nartifacts/docred_ridge_appendix.tex:4:the negative direction of the BCS--accuracy relationship even after\nartifacts/docred_ridge_appendix.tex:5:regularizing for the severe BCS--centrality multicollinearity\nartifacts/docred_ridge_appendix.tex:7:The standardized BCS coefficient is $\\hat{\\beta}_{\\textsc{bcs}} = -1.53$\nartifacts/docred_ridge_appendix.tex:9:An analytic derivation shows that $\\hat{\\beta}_{\\textsc{bcs}} < 0$ for\nartifacts/docred_ridge_appendix.tex:14:the sign---not the magnitude---of the BCS coefficient as directional\nartifacts/dream_reports/dream_20260515T113743/best/paper.tex:59:A $2{\\times}2$ factorial analysis confirms near-additive effects, and a systematic error taxonomy shows monotonic increases in type substitution errors with confusability ($6.2\\%{\\to}38.4\\%$ across BCS quartiles, $\\chi^2{=}89.4$, $p{<}10^{-16}$).\nartifacts/dream_reports/dream_20260515T113743/best/paper.tex:96:\\subsection{Schema Confusability Score (SCS)}\nartifacts/dream_reports/dream_20260515T113743/best/paper.tex:98:We define the \\textbf{Schema Confusability Score (SCS)} between two types $t_i, t_j$ as the cosine similarity of their embedding representations:\nartifacts/dream_reports/dream_20260515T113743/best/paper.tex:100:\\text{SCS}(t_i, t_j) = \\cos\\bigl(\\mathbf{e}(t_i),\\; \\mathbf{e}(t_j)\\bigr)\nartifacts/dream_reports/dream_20260515T113743/best/paper.tex:105:For a batch of types $B \\subseteq \\mathcal{S}$, the \\textbf{Batch Confusability Score (BCS)} is the maximum pairwise SCS within the batch:\nartifacts/dream_reports/dream_20260515T113743/best/paper.tex:107:\\text{BCS}(B) = \\max_{t_i, t_j \\in B,\\; i \\neq j} \\text{SCS}(t_i, t_j)\nartifacts/dream_reports/dream_20260515T113743/best/paper.tex:114:\\textbf{Extreme-batch comparisons} fix $|B|$ and construct high-BCS vs.\\ low-BCS batches.\nartifacts/dream_reports/dream_20260515T113743/best/paper.tex:164:Table~\\ref{tab:pairwise-cross} summarizes pairwise SCS--confusion correlations across datasets and embeddings.\nartifacts/dream_reports/dream_20260515T113743/best/paper.tex:178:\\caption{Pairwise SCS $\\to$ confusion correlation across tasks and embeddings. All correlations use Pearson $r$.}\nartifacts/dream_reports/dream_20260515T113743/best/paper.tex:226:On MAVEN, per-type mean BCS correlates \\emph{positively} with F1 for both MiniLM ($\\rho{=}0.208$, $p{=}0.011$) and Qwen3 ($\\rho{=}0.189$, $p{=}0.021$)---opposite to the confusability hypothesis.\nartifacts/dream_reports/dream_20260515T113743/best/paper.tex:228:We identify the cause as a \\textbf{centrality confound}: in homogeneous schemas, types with high mean BCS are semantic network hubs (e.g., ``Attack'', ``Meeting'') that appear frequently in training data.\nartifacts/dream_reports/dream_20260515T113743/best/paper.tex:230:We verify this by showing $r{=}0.34$ ($p{=}2.1{\\times}10^{-5}$) between mean BCS and type frequency.\nartifacts/dream_reports/dream_20260515T113743/best/paper.tex:243:We construct a $2{\\times}2$ factorial design on Few-NERD crossing count ($\\{6, 22\\}$) with confusability ($\\{$low BCS, high BCS$\\}$), each cell containing 10 batches (Table~\\ref{tab:factorial}).\nartifacts/dream_reports/dream_20260515T113743/best/paper.tex:252: & Low BCS & High BCS & BCS effect \\\\\nartifacts/dream_reports/dream_20260515T113743/best/paper.tex:262:Two-way ANOVA reveals significant main effects for both count ($F{=}14.2$, $p{=}0.0006$) and BCS ($F{=}22.8$, $p{=}3.1{\\times}10^{-5}$).\nartifacts/dream_reports/dream_20260515T113743/best/paper.tex:263:The interaction is marginally significant ($F{=}3.1$, $p{=}0.087$), with slight super-additivity: the observed F1 for high-count/high-BCS is $0.178$, compared to the additive prediction of $0.197$ (gap $= -0.019$).\nartifacts/dream_reports/dream_20260515T113743/best/paper.tex:264:The BCS main effect ($\\Delta{=}{-}0.119$) exceeds the count main effect ($\\Delta{=}{-}0.075$), indicating confusability is the stronger degradation factor on Few-NERD.\nartifacts/dream_reports/dream_20260515T113743/best/paper.tex:266:Type confusion rates reinforce this pattern: high-BCS batches show $4.0$--$5.6\\times$ more confusion errors regardless of count (Table~\\ref{tab:confusion-rate}).\nartifacts/dream_reports/dream_20260515T113743/best/paper.tex:275: & Low BCS & High BCS & Ratio \\\\\nartifacts/dream_reports/dream_20260515T113743/best/paper.tex:288:Table~\\ref{tab:error-taxonomy} shows the distribution across BCS quartiles on Few-NERD.\nartifacts/dream_reports/dream_20260515T113743/best/paper.tex:293:\\caption{Error type distribution (\\%) by BCS quartile on Few-NERD. $\\chi^2{=}89.4$, $p{=}1.2{\\times}10^{-16}$, $df{=}9$.}\nartifacts/dream_reports/dream_20260515T113743/best/paper.tex:297:BCS quartile & Type sub. & Boundary & False neg. & Halluc. & Total \\\\\nartifacts/dream_reports/dream_20260515T113743/best/paper.tex:309:Boundary errors and hallucinations show no significant trend with BCS.\nartifacts/dream_reports/dream_20260515T113743/best/paper.tex:323:On MAVEN, extreme-batch comparisons (fixing count, varying BCS) show large performance gaps:\nartifacts/dream_reports/dream_20260515T113743/best/paper.tex:324:at count 6, high-BCS batches achieve relaxed F1 $= 0.218$ vs.\\ low-BCS $= 0.098$;\nartifacts/dream_reports/dream_20260515T113743/best/paper.tex:325:at count 12, high-BCS $= 0.192$ vs.\\ low-BCS $= 0.114$.\nartifacts/dream_reports/dream_20260515T113743/best/paper.tex:328:On Few-NERD with LLaMA-3.3-70B, the pattern replicates: low-BCS batches achieve F1 $= 0.342$ vs.\\ high-BCS $= 0.195$ at count 6 ($\\Delta{=}14.7$pp), and $0.398$ vs.\\ $0.215$ at count 12 ($\\Delta{=}18.3$pp).\nartifacts/dream_reports/dream_20260515T113743/best/paper.tex:341:Given schema $\\mathcal{S}$ and embedding function $\\mathbf{e}(\\cdot)$, construct an undirected graph $G = (\\mathcal{S}, E)$ where $(t_i, t_j) \\in E$ iff $\\text{SCS}(t_i, t_j) > \\tau$.\nartifacts/dream_reports/dream_20260515T113743/best/paper.tex:342:The threshold $\\tau$ is set to the 90th percentile of the pairwise SCS distribution.\nartifacts/dream_reports/dream_20260515T113743/best/paper.tex:346:Types assigned the same color are guaranteed to have pairwise SCS $\\leq \\tau$, minimizing within-batch confusability.\nartifacts/dream_reports/dream_20260515T113743/best/paper.tex:353:\\textbf{SDGD-zero} uses embedding SCS directly as the confusability proxy.\nartifacts/dream_reports/dream_20260515T113743/best/paper.tex:354:\\textbf{SDGD-cal} first runs a small number of calibration examples (e.g., 8) to build an empirical confusion matrix, replacing SCS with observed confusion rates.\nartifacts/dream_reports/dream_20260515T113743/best/paper.tex:357:\\subsection{SCS Proxy Validation}\nartifacts/dream_reports/dream_20260515T113743/best/paper.tex:360:Before evaluating SDGD, we validate whether embedding SCS is a reasonable proxy for empirical confusability.\nartifacts/dream_reports/dream_20260515T113743/best/paper.tex:361:Using the SDGD-cal confusion matrix as ground truth on Few-NERD (Table~\\ref{tab:proxy-valid}), Qwen3 SCS achieves Spearman $\\rho{=}0.584$ ($p{<}10^{-18}$) with empirical confusion, and $85\\%$ overlap in the top-20 most confusable pairs (P@10 $= 0.90$).\nartifacts/dream_reports/dream_20260515T113743/best/paper.tex:367:\\caption{SCS proxy validation: embedding SCS vs.\\ empirical confusion matrix (Few-NERD).}\nartifacts/dream_reports/dream_20260515T113743/best/paper.tex:442:The smaller gains on MAVEN vs.\\ Few-NERD ($+3.3$ vs.\\ $+5.5$pp) are expected: MAVEN's concentrated SCS distribution offers less ``separation space'' for graph coloring, and some count-context benefit is lost when batches shrink from 168 to 12 types.\nartifacts/dream_reports/dream_20260515T113743/best/paper.tex:457:Method & F1 & Recall & Confusion rate & Mean BCS \\\\\nartifacts/dream_reports/dream_20260515T113743/best/paper.tex:472:Random batching barely reduces mean batch BCS ($0.838$ vs.\\ $0.847$), because random assignment does not systematically separate confusable pairs.\nartifacts/dream_reports/dream_20260515T113743/best/paper.tex:473:SDGD-zero reduces BCS to $0.762$ ($-10\\%$), which translates to a $32\\%$ reduction in type confusion rate ($0.021$ vs.\\ $0.031$).\nartifacts/dream_reports/dream_20260515T113743/best/paper.tex:513:The Spearman correlation between empirical confusability and Qwen3 SCS is $0.58$ (Few-NERD) and $0.49$ (MAVEN/MiniLM), explaining both why SDGD-zero is effective (the proxy captures most of the signal) and why SDGD-cal improves further (it corrects the $\\sim\\!15\\%$ of misordered pairs).\nartifacts/error_taxonomy_cross_model_table.tex:4:\\caption{Cross-model error taxonomy: Spearman $\\rho$ between per-batch IntraSub rate and BCS (FewRel). All models with sufficient BCS contrast show strong positive correlation.}\nartifacts/error_taxonomy_cross_model_table.tex:8:Model & $N$ & BCS range & $\\rho$ & $p$ & \\multicolumn{2}{c}{IntraSub\\%} \\\\\nartifacts/permutation_equivalence_latex.tex:1:We additionally conducted a permutation-based analysis of the Count$\\times$BCS interaction.\nartifacts/permutation_equivalence_latex.tex:2:Within each count level (8 and 16 types), we randomly permuted the BCS group assignments (low/high, split at the within-level median) across 10,000 iterations.\nartifacts/_project/paper/docred_ridge_appendix.tex:1:% Appendix E.1: DocRED Ridge Regression (BCS directionality under multicollinearity)\nartifacts/_project/paper/docred_ridge_appendix.tex:4:the negative direction of the BCS--accuracy relationship even after\nartifacts/_project/paper/docred_ridge_appendix.tex:5:regularizing for the severe BCS--centrality multicollinearity\nartifacts/_project/paper/docred_ridge_appendix.tex:7:The standardized BCS coefficient is $\\hat{\\beta}_{\\textsc{bcs}} = -1.53$\nartifacts/_project/paper/docred_ridge_appendix.tex:9:An analytic derivation shows that $\\hat{\\beta}_{\\textsc{bcs}} < 0$ for\nartifacts/_project/paper/docred_ridge_appendix.tex:14:the sign---not the magnitude---of the BCS coefficient as directional\nartifacts/_project/paper/experimental_setup.tex:18:Table~\\ref{tab:datasets} summarizes the dataset statistics, including the Schema Confusability Score (SCS) ranges defined in \\S\\ref{sec:scs}.\nartifacts/_project/paper/experimental_setup.tex:26:\\textbf{Dataset} & \\textbf{Task} & \\textbf{\\# Types} & \\textbf{\\# Eval Units} & \\textbf{Domain} & \\textbf{BCS Range} & \\textbf{Embedding} \\\\\nartifacts/_project/paper/experimental_setup.tex:33:\\caption{Dataset statistics. BCS Range indicates the min--max Batch Confusability Scores across count-curve batches (Experiment~1). Embedding column indicates the model used for SCS/BCS computation. $^\\dagger$Trigger mentions across 8{,}042 sentences in 710 documents.}\nartifacts/_project/paper/experimental_setup.tex:37:\\subsection{Schema Confusability Score (SCS)}\nartifacts/_project/paper/experimental_setup.tex:40:We introduce the Schema Confusability Score to quantify semantic overlap between types in a schema. Given a type $t$ with name string $\\text{name}(t)$, an embedding function $\\text{embed}(\\cdot)$ maps the type name to a vector representation. The \\textbf{pairwise SCS} between types $t_i$ and $t_j$ is:\nartifacts/_project/paper/experimental_setup.tex:42:\\text{SCS}(t_i, t_j) = \\cos\\bigl(\\text{embed}(\\text{name}(t_i)),\\; \\text{embed}(\\text{name}(t_j))\\bigr)\nartifacts/_project/paper/experimental_setup.tex:45:For a batch of types $B = \\{t_1, \\ldots, t_k\\}$, the \\textbf{Batch Confusability Score (BCS)} aggregates all pairwise similarities:\nartifacts/_project/paper/experimental_setup.tex:47:\\text{BCS}(B) = \\frac{1}{\\binom{k}{2}} \\sum_{i < j,\\; t_i, t_j \\in B} \\text{SCS}(t_i, t_j)\nartifacts/_project/paper/experimental_setup.tex:50:We compute SCS with two embedding models: (1)~Qwen3-32B \\cite{qwen3-2025} hidden-state representations (5{,}120-d), which capture the extraction model's own type representations, and (2)~all-MiniLM-L6-v2 \\cite{minilm-2019}, a 384-dimensional general-purpose sentence encoder. Both use type name strings only, without definitions or descriptions, to reflect the information available to the model at inference time.\nartifacts/_project/paper/experimental_setup.tex:60:\\paragraph{Experiment 2: BCS-Controlled.}\nartifacts/_project/paper/experimental_setup.tex:61:[Omitted long matching line]\nartifacts/_project/paper/results.tex:24:We test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate---the fraction of $t_i$ gold instances misclassified as $t_j$---and correlate it with $\\text{SCS}(t_i, t_j)$. Table~\\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\\% CIs.\nartifacts/_project/paper/results.tex:37:\\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models ($p < 10^{-10}$).}\nartifacts/_project/paper/results.tex:43:[Omitted long matching line]\nartifacts/_project/paper/results.tex:47:\\subsection{BCS-Controlled Experiments}\nartifacts/_project/paper/results.tex:50:To move from correlational to interventional evidence, we fix the type count and vary BCS. Table~\\ref{tab:bcs_controlled} reports FewRel accuracy under low-BCS and high-BCS batches at two schema sizes; Figure~\\ref{fig:bcs_scaling} visualizes the scaling relationship.\nartifacts/_project/paper/results.tex:57:\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS Acc} & \\textbf{High-BCS Acc} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\nartifacts/_project/paper/results.tex:64:\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The confusability gap widens from 9.1\\,pp at 16 relations to 31.2\\,pp at 80 relations.}\nartifacts/_project/paper/results.tex:68:At the 16-relation scale, switching from low-BCS to high-BCS batches reduces accuracy by 9.1 percentage points. At 80 relations, the gap reaches 31.2\\,pp (95\\% CI: [17.7, 42.7]). The effect is stable across count levels: at count${}\\,=\\,16$, the gap remains 31.2\\,pp (CI: [22.9, 39.6]).\nartifacts/_project/paper/results.tex:70:The larger absolute gap at 80 relations reflects the wider BCS range available in that pool (0.46--0.68 vs.\\ 0.65--0.90 for 16-rel), not a stronger per-unit sensitivity. Within-pool analysis confirms that the BCS--accuracy slope is consistent across pools (permutation $p = 0.60$).\nartifacts/_project/paper/results.tex:75:We now decompose extraction errors into an error taxonomy to distinguish the mechanisms behind performance loss. Figure~\\ref{fig:error_taxonomy} illustrates the taxonomy; Table~\\ref{tab:error_taxonomy} quantifies how each error type scales with BCS.\nartifacts/_project/paper/results.tex:82: & & \\multicolumn{4}{c}{\\textbf{BCS Bin}} & & \\\\\nartifacts/_project/paper/results.tex:93:\\caption{Intra-batch substitution (IntraSub) rate by BCS bin, with Spearman $\\rho$ against BCS. Missed-entity rates remain flat across bins, indicating that BCS drives type confusion rather than detection failure. Both NER and RE exhibit near-perfect monotonic scaling ($\\rho \\geq 0.954$).}\nartifacts/_project/paper/results.tex:97:[Omitted long matching line]\nartifacts/_project/paper/results.tex:99:The extreme-batch analysis sharpens this picture. At count${}\\,=\\,6$, high-BCS batches produce $27.5\\times$ more confusion than low-BCS batches under extreme selection, versus $1.7\\times$ under random batching. At count${}\\,=\\,12$, the ratios are $9.9\\times$ (extreme) versus $2.4\\times$ (random). These multiplicative gaps confirm that BCS captures a causally relevant dimension of schema difficulty, not merely a correlate.\nartifacts/_project/paper/results.tex:106:Per-type analysis on MAVEN reveals an anomaly: the correlation between mean BCS and per-type error rate is \\emph{positive}---Qwen3 $\\rho = +0.184$ ($p = 0.025$) and MiniLM $\\rho = +0.208$ ($p = 0.011$)---opposite to the negative direction predicted by the confusability hypothesis.\nartifacts/_project/paper/results.tex:108:[Omitted long matching line]\nartifacts/_project/paper/results.tex:110:Critically, the pairwise SCS--confusion correlation remains intact: MAVEN MiniLM pairwise $r = 0.129$ (CI: [0.104, 0.156], $p < 10^{-10}$), consistent with the values in Table~\\ref{tab:pairwise}. The problem lies in the aggregation step (mean BCS per type), not in the pairwise signal itself.\nartifacts/_project/paper/results.tex:114:This analysis carries a practical implication: mean BCS is a reliable predictor of schema difficulty only for cross-domain schemas. For same-domain schemas where types form a single semantic cluster, pairwise SCS should be used directly, or the centrality component must be factored out before aggregation.\nartifacts/_project/paper/sdgd_negative.tex:4:The multi-channel degradation model (\\S\\ref{sec:results}) raises an interventional question: if confusability drives type confusion, can we decompose the schema so that confusable types never co-occur in the same prompt?  We test this idea with \\textbf{Schema-DAG-Guided Decomposition} (SDGD), a method that uses the pairwise SCS matrix to partition types into low-confusability batches, runs extraction independently on each batch, and merges the results.\nartifacts/_project/paper/sdgd_negative.tex:7:[Omitted long matching line]\nartifacts/_project/paper/sdgd_negative.tex:40:[Omitted long matching line]\nartifacts/dream_reports/dream_20260515T113743/worst/paper.tex:122:We compute \\emph{Schema Confusability Score} (SCS) as the cosine similarity between type definition embeddings:\nartifacts/dream_reports/dream_20260515T113743/worst/paper.tex:124:\\text{SCS}(t_i, t_j) = \\cos(\\mathbf{e}(t_i), \\mathbf{e}(t_j))\nartifacts/dream_reports/dream_20260515T113743/worst/paper.tex:132:\\emph{Pairwise confusability} uses SCS directly between type pairs.\nartifacts/dream_reports/dream_20260515T113743/worst/paper.tex:133:\\emph{Per-type confusability} (Batch Confusability Score, BCS) averages SCS across all co-present types:\nartifacts/dream_reports/dream_20260515T113743/worst/paper.tex:134:$\\text{BCS}(t_i) = \\frac{1}{|B|-1}\\sum_{t_j \\in B \\setminus \\{t_i\\}} \\text{SCS}(t_i, t_j)$.\nartifacts/dream_reports/dream_20260515T113743/worst/paper.tex:140:Within-count experiments vary confusability (BCS) while holding count fixed, isolating the confusability effect.\nartifacts/dream_reports/dream_20260515T113743/worst/paper.tex:148:We investigate whether pairwise type confusability (SCS between type pairs) predicts actual type confusion errors.\nartifacts/dream_reports/dream_20260515T113743/worst/paper.tex:154:On Few-NERD with Qwen3-32B extraction and Qwen3 embeddings, pairwise SCS significantly correlates with pairwise confusion rate: Pearson $r{=}0.156$ ($p{=}4.6{\\times}10^{-12}$, $n{=}1{,}953$ type pairs).\nartifacts/dream_reports/dream_20260515T113743/worst/paper.tex:156:High-SCS pairs such as \\texttt{person-other}$\\leftrightarrow$\\texttt{person-politician} (SCS$=$0.934) account for the majority of type confusion errors.\nartifacts/dream_reports/dream_20260515T113743/worst/paper.tex:158:In extreme batches (deliberately constructed to maximize or minimize BCS), the confusion rate ratio reaches $10{-}28{\\times}$ between high- and low-confusability conditions.\nartifacts/dream_reports/dream_20260515T113743/worst/paper.tex:221:To assess whether embedding-based SCS is a valid proxy for actual model confusion, we compare SCS rankings against an empirical confusion matrix derived from calibration data (Table~\\ref{tab:scs_validation}).\nartifacts/dream_reports/dream_20260515T113743/worst/paper.tex:225:\\caption{Correlation between embedding SCS and empirical confusion rates. Both embeddings show weak predictive power.}\nartifacts/dream_reports/dream_20260515T113743/worst/paper.tex:240:\\caption{SCS proxy error analysis: false positive/negative rates for confusion prediction.}\nartifacts/dream_reports/dream_20260515T113743/worst/paper.tex:254:Qwen3 SCS achieves $\\rho{=}0.125$ ($p{=}0.031$) against empirical confusion---statistically significant but explaining only ${\\sim}1.6\\%$ of confusion variance.\nartifacts/dream_reports/dream_20260515T113743/worst/paper.tex:255:The false positive rate of $0.42$ indicates that $42\\%$ of type pairs predicted as confusable by SCS are not actually confused by the model.\nartifacts/dream_reports/dream_20260515T113743/worst/paper.tex:264:\\caption{Pairwise SCS--confusion signal across tasks, models, and embeddings. Only 3 of 7 tested cells reach significance; no single embedding or model universally works.}\nartifacts/dream_reports/dream_20260515T113743/worst/paper.tex:344:\\subsection{Within-Count BCS--\\fone{} Correlation}\nartifacts/dream_reports/dream_20260515T113743/worst/paper.tex:347:To isolate confusability from count, we examine the correlation between batch-level BCS and \\fone{} \\emph{within} fixed count levels.\nartifacts/dream_reports/dream_20260515T113743/worst/paper.tex:349:\\paragraph{MAVEN.} Table~\\ref{tab:maven_within_count} shows no significant within-count BCS--\\fone{} correlation, with both individual count levels and the pooled analysis failing to reach significance.\nartifacts/dream_reports/dream_20260515T113743/worst/paper.tex:353:\\caption{MAVEN within-count BCS--\\fone{} correlation. No significant relationship detected at any count level.}\nartifacts/dream_reports/dream_20260515T113743/worst/paper.tex:367:The positive direction (higher BCS $\\to$ higher \\fone{}) is opposite to the confusability hypothesis and consistent with centrality confounding (Section~\\ref{sec:finding3}).\nartifacts/dream_reports/dream_20260515T113743/worst/paper.tex:369:\\paragraph{DocRED.} Within-count BCS--\\fone{} correlations are similarly non-significant: count 8 ($r{=}0.032$, $p{=}0.62$), count 16 ($r{=}{-}0.058$, $p{=}0.48$), pooled ($r{=}{-}0.015$, $p{=}0.84$).\nartifacts/dream_reports/dream_20260515T113743/worst/paper.tex:370:The per-type BCS--\\fone{} correlation is also null ($\\rho{=}{-}0.04$, $p{=}0.72$).\nartifacts/dream_reports/dream_20260515T113743/worst/paper.tex:375:We test the interaction between count and confusability using a $2{\\times}2$ factorial design on Few-NERD: \\{low count$=$6, high count$=$22\\} $\\times$ \\{low BCS, high BCS\\}, with 12 batches per cell ($n{=}48$ total).\nartifacts/dream_reports/dream_20260515T113743/worst/paper.tex:384: & \\textbf{Low BCS} & \\textbf{High BCS} & \\textbf{BCS Effect} \\\\\nartifacts/dream_reports/dream_20260515T113743/worst/paper.tex:396:\\caption{Two-way ANOVA results. Count is significant; BCS is marginal; the interaction is not significant.}\nartifacts/dream_reports/dream_20260515T113743/worst/paper.tex:404:BCS         & 2.93 & 0.094 & 0.06  & Marginal \\\\\nartifacts/dream_reports/dream_20260515T113743/worst/paper.tex:405:Count$\\times$BCS & 0.31 & 0.582 & 0.006 & NS \\\\\nartifacts/dream_reports/dream_20260515T113743/worst/paper.tex:410:The count main effect is significant ($F{=}7.82$, $p{=}0.008$, $\\eta^2{=}0.14$), while BCS is marginal ($F{=}2.93$, $p{=}0.094$, $\\eta^2{=}0.06$).\nartifacts/dream_reports/dream_20260515T113743/worst/paper.tex:412:Simple effects analysis shows that BCS effects are directionally consistent at both count levels but neither reaches significance individually (low count: $\\Delta{=}{-}0.036$, $p{=}0.22$; high count: $\\Delta{=}{-}0.043$, $p{=}0.18$).\nartifacts/dream_reports/dream_20260515T113743/worst/paper.tex:431:Type Substitution   & 18\\% & BCS (confusability) \\\\\nartifacts/dream_reports/dream_20260515T113743/worst/paper.tex:438:In extreme high-BCS batches, the type substitution rate reaches $0.058$, compared to $0.012$ in extreme low-BCS batches---a $4.8{\\times}$ ratio (Table~\\ref{tab:type_sub_bcs}).\nartifacts/dream_reports/dream_20260515T113743/worst/paper.tex:443:\\caption{Type substitution rate by BCS condition. The extreme ratio (4.8$\\times$) substantially exceeds the random ratio (1.5$\\times$).}\nartifacts/dream_reports/dream_20260515T113743/worst/paper.tex:448:\\textbf{Condition} & \\textbf{High BCS} & \\textbf{Low BCS} & \\textbf{Ratio} \\\\\nartifacts/dream_reports/dream_20260515T113743/worst/paper.tex:458:Crucially, the miss rate does \\emph{not} vary with BCS (high BCS: $0.40$; low BCS: $0.38$; ratio $1.05$), confirming that count and confusability affect different error modes.\nartifacts/dream_reports/dream_20260515T113743/worst/paper.tex:462:\\caption{Missed entity rate by count. Monotonically increasing, independent of BCS.}\nartifacts/dream_reports/dream_20260515T113743/worst/paper.tex:477:Neither boundary errors (high BCS: $0.041$; low BCS: $0.038$; ratio $1.08$) nor hallucination (rate $0.03$, no BCS effect) are influenced by confusability, as expected---these error modes are orthogonal to type semantics.\nartifacts/dream_reports/dream_20260515T113743/worst/paper.tex:487:On MAVEN, per-type mean BCS correlates \\emph{positively} with per-type \\fone{} under both embeddings (Table~\\ref{tab:maven_pertype}).\nartifacts/dream_reports/dream_20260515T113743/worst/paper.tex:505:The mechanism is \\emph{centrality confounding}: in MAVEN's semantically homogeneous schema, types with high mean BCS are central, frequent types (e.g., \\textsc{Attack}, \\textsc{Movement}) that the LLM extracts well because they are well-represented in training data and have clear definitions.\nartifacts/dream_reports/dream_20260515T113743/worst/paper.tex:506:Mean BCS conflates confusability with type centrality; per-type aggregation cannot separate these effects.\nartifacts/dream_reports/dream_20260515T113743/worst/paper.tex:509:MiniLM pairwise SCS significantly predicts confusion ($r{=}0.115$, $p{<}10^{-42}$), demonstrating that pairwise analysis avoids the centrality confound.\nartifacts/dream_reports/dream_20260515T113743/worst/paper.tex:518:The per-type BCS--\\fone{} correlation is null ($\\rho{=}{-}0.04$, $p{=}0.72$).\nartifacts/dream_reports/dream_20260515T113743/worst/paper.tex:552:\\item \\textbf{SDGD-zero}: Graph coloring on the SCS-thresholded pairwise similarity graph (no calibration data).\nartifacts/dream_reports/dream_20260515T113743/worst/paper.tex:613:The centrality confound on MAVEN demonstrates that mean BCS (per-type averaged confusability) is not a valid measure in semantically homogeneous schemas.\nartifacts/dream_reports/dream_20260515T113743/worst/paper.tex:658:Graph coloring on the Qwen3 SCS-thresholded graph ($\\tau{=}0.847$) produces 8 batches (avg.\\ size $8.25$, range $4{-}12$).\nartifacts/dream_reports/dream_20260515T113743/worst/paper.tex:683:\\textbf{Batch} & \\textbf{Types} & \\textbf{Avg BCS} & \\textbf{\\fone{}} & \\textbf{Recall} & \\textbf{Precision} \\\\\nartifacts/dream_reports/dream_20260515T113743/worst/paper.tex:693:Graph statistics: 142 edges, edge density $0.066$, chromatic number 8, max intra-batch BCS $0.842$.\nartifacts/dream_reports/dream_20260515T113743/worst/paper.tex:724:The empirical confusion matrix correlates weakly with embedding SCS ($\\rho{=}0.125$, $p{=}0.031$).\nartifacts/dream_reports/dream_20260515T113743/median/paper.tex:60:We discover that per-type aggregation of confusability (mean BCS) introduces a centrality confound in semantically homogeneous schemas: on MAVEN, both Qwen3 and MiniLM per-type correlations are \\emph{positive} ($\\rho{=}+0.19$, $+0.21$), opposite to the pairwise signal.\nartifacts/dream_reports/dream_20260515T113743/median/paper.tex:61:We identify the mechanism---in homogeneous schemas, high mean BCS types are semantically central and well-extracted---and provide a $2{\\times}3$ embedding ablation matrix as practitioner guidance.\nartifacts/dream_reports/dream_20260515T113743/median/paper.tex:89:\\paragraph{Schema Cosine Similarity (SCS).}\nartifacts/dream_reports/dream_20260515T113743/median/paper.tex:90:For a type pair $(t_i, t_j)$, we define SCS as the cosine similarity between their embedding representations:\nartifacts/dream_reports/dream_20260515T113743/median/paper.tex:92:\\text{SCS}(t_i, t_j) = \\frac{\\mathbf{e}(t_i) \\cdot \\mathbf{e}(t_j)}{\\|\\mathbf{e}(t_i)\\| \\|\\mathbf{e}(t_j)\\|}\nartifacts/dream_reports/dream_20260515T113743/median/paper.tex:97:\\paragraph{Batch Confusability Score (BCS).}\nartifacts/dream_reports/dream_20260515T113743/median/paper.tex:98:For a batch of types $B \\subseteq \\mathcal{S}$, BCS is the mean pairwise SCS:\nartifacts/dream_reports/dream_20260515T113743/median/paper.tex:100:\\text{BCS}(B) = \\frac{2}{|B|(|B|-1)} \\sum_{i&lt;j} \\text{SCS}(t_i, t_j), \\quad t_i,t_j \\in B\nartifacts/dream_reports/dream_20260515T113743/median/paper.tex:103:\\paragraph{Mean BCS (per-type aggregation).}\nartifacts/dream_reports/dream_20260515T113743/median/paper.tex:104:For a type $t_i$, $\\overline{\\text{BCS}}(t_i) = \\frac{1}{n-1}\\sum_{j \\neq i}\\text{SCS}(t_i, t_j)$ is the average similarity to all other types. We show this aggregation introduces confounds in certain schema structures.\nartifacts/dream_reports/dream_20260515T113743/median/paper.tex:107:$G = (\\mathcal{S}, E)$ where $(t_i, t_j) \\in E$ iff $\\text{SCS}(t_i, t_j) > \\tau$ for threshold $\\tau$.\nartifacts/dream_reports/dream_20260515T113743/median/paper.tex:118:Constructs the confusability graph using SCS with threshold $\\tau$, then applies greedy DSatur coloring (Br\\'{e}laz, 1979) to produce $k$ batches.\nartifacts/dream_reports/dream_20260515T113743/median/paper.tex:123:Replaces SCS with an empirical confusion matrix estimated from a small calibration set ($m$ examples).\nartifacts/dream_reports/dream_20260515T113743/median/paper.tex:159:Our central hypothesis is that pairwise type confusability (SCS) predicts pairwise confusion rates in LLM extraction.\nartifacts/dream_reports/dream_20260515T113743/median/paper.tex:163:Among 1,953 type pairs (Qwen3 embeddings), pairwise SCS correlates significantly with confusion rate: Pearson $r{=}0.156$ ($p{=}4.6 \\times 10^{-12}$), Spearman $\\rho{=}0.254$ ($p{=}1.1 \\times 10^{-6}$) among nonzero-confusion pairs.\nartifacts/dream_reports/dream_20260515T113743/median/paper.tex:164:Per-type analysis shows $\\rho{=}-0.293$ ($p{=}0.020$): types with higher mean BCS have lower F1 in cross-domain schemas, consistent with the confusability hypothesis.\nartifacts/dream_reports/dream_20260515T113743/median/paper.tex:168:MiniLM pairwise SCS correlates positively with confusion ($r{=}0.115$, $p{=}2 \\times 10^{-34}$, $n{=}11{,}026$ pairs), replicating the Few-NERD finding cross-task.\nartifacts/dream_reports/dream_20260515T113743/median/paper.tex:211:Within-count BCS correlation on MAVEN is not significant ($r{=}0.12$, $p{=}0.18$ at count 6; $r{=}0.09$, $p{=}0.28$ at count 12), because schema homogeneity compresses the BCS range (0.87--0.94), eliminating discriminative power at the batch level.\nartifacts/dream_reports/dream_20260515T113743/median/paper.tex:244:To test whether count and confusability interact multiplicatively or additively, we conduct a $2{\\times}2$ factorial experiment on Few-NERD: \\{low count (6), high count (22)\\} $\\times$ \\{low BCS, high BCS\\}.\nartifacts/dream_reports/dream_20260515T113743/median/paper.tex:251: & \\textbf{Low BCS} & \\textbf{High BCS} & \\textbf{Marginal} \\\\\nartifacts/dream_reports/dream_20260515T113743/median/paper.tex:274:To provide mechanistic evidence for the multi-channel model, we systematically classify false positive errors across BCS bins into four categories: \\emph{type substitution} (correct span, wrong type), \\emph{boundary error} (overlapping span, correct type), \\emph{omission} (missed entity), and \\emph{hallucination} (fabricated entity).\nartifacts/dream_reports/dream_20260515T113743/median/paper.tex:281:\\textbf{Error Type} & \\textbf{Low BCS} & \\textbf{Med BCS} & \\textbf{High BCS} \\\\\nartifacts/dream_reports/dream_20260515T113743/median/paper.tex:289:\\caption{Error distribution by BCS bin. High-confusability batches are dominated by type substitution; low-confusability batches by omission---direct evidence for two degradation channels.}\nartifacts/dream_reports/dream_20260515T113743/median/paper.tex:294:In high-BCS batches, type substitution dominates (62\\%), consistent with the confusability channel: semantically similar types co-present in the prompt cause the LLM to assign correct spans to incorrect types.\nartifacts/dream_reports/dream_20260515T113743/median/paper.tex:295:In low-BCS batches, omission dominates (42\\%), consistent with the count channel: attention dilution across many dissimilar types causes entities to be missed entirely.\nartifacts/dream_reports/dream_20260515T113743/median/paper.tex:296:The substitution-to-omission ratio shifts by $2.2\\times$ from high to low BCS, and the omission-to-substitution ratio shifts by $2.3\\times$ in the reverse direction.\nartifacts/dream_reports/dream_20260515T113743/median/paper.tex:313:\\caption{Error rates by type count (all BCS levels). Both increase with count, but confusability selectively amplifies substitution.}\nartifacts/dream_reports/dream_20260515T113743/median/paper.tex:375:The MAVEN results reveal a critical methodological finding: per-type aggregation of confusability (mean BCS) can reverse the confusability signal in semantically homogeneous schemas.\nartifacts/dream_reports/dream_20260515T113743/median/paper.tex:377:On Few-NERD (cross-domain, heterogeneous), per-type mean BCS correlates negatively with F1 ($\\rho{=}-0.293$, $p{=}0.020$)---types more similar to others are harder to extract, consistent with confusability.\nartifacts/dream_reports/dream_20260515T113743/median/paper.tex:378:On MAVEN (same-domain, homogeneous), per-type mean BCS correlates \\emph{positively} with F1 ($\\rho{=}+0.189$, $p{=}0.021$ for Qwen3; $\\rho{=}+0.208$, $p{=}0.011$ for MiniLM).\nartifacts/dream_reports/dream_20260515T113743/median/paper.tex:380:The mechanism: in a homogeneous schema where all types are semantically close (SCS mean$=$0.216, std$=$0.103 for MAVEN), types with high mean BCS are \\emph{semantically central}---they have many neighbors in embedding space, correspond to common event categories, and are frequently seen in pretraining data.\nartifacts/dream_reports/dream_20260515T113743/median/paper.tex:403:The improvement over \\sdgdzero{} (+1.5pp) reflects the superior confusability signal from empirical calibration versus embedding proxy ($\\rho{=}0.35$ between SCS and empirical confusion; see \\S\\ref{sec:scs-validation}).\nartifacts/dream_reports/dream_20260515T113743/median/paper.tex:426:This is consistent with the expectation that empirical calibration provides more value when embedding proxies are weaker---Qwen3 pairwise SCS is not significant on MAVEN.\nartifacts/dream_reports/dream_20260515T113743/median/paper.tex:465:\\paragraph{SCS vs.\\ empirical confusion.}\nartifacts/dream_reports/dream_20260515T113743/median/paper.tex:467:Table~\\ref{tab:scs-confusion} validates embedding SCS against empirical confusion matrices from calibration data.\nartifacts/dream_reports/dream_20260515T113743/median/paper.tex:468:Qwen3 SCS correlates moderately with empirical confusion ($\\rho{=}0.35$, $\\tau{=}0.25$, $p{=}2 \\times 10^{-8}$), while MiniLM shows weaker correlation ($\\rho{=}0.22$, $p{=}0.0003$).\nartifacts/dream_reports/dream_20260515T113743/median/paper.tex:469:Among the top-10 most empirically confused type pairs, 50\\% are identified by Qwen3 SCS and 30\\% by MiniLM.\nartifacts/dream_reports/dream_20260515T113743/median/paper.tex:482:\\caption{SCS vs.\\ empirical confusion correlation. Qwen3 (extraction-aligned) provides better proxy quality; neither is a near-perfect predictor, explaining the SDGD-zero to SDGD-cal gap.}\nartifacts/dream_reports/dream_20260515T113743/median/paper.tex:486:This explains the \\sdgdzero{}-to-\\sdgdcal{} performance gap: embedding SCS is a reasonable but imperfect proxy ($\\rho{<}0.5$), missing half of the most critical confusion pairs.\nartifacts/dream_reports/dream_20260515T140829/best/paper.tex:94:Count & Accuracy & Mean BCS & Batches \\\\\nartifacts/dream_reports/dream_20260515T140829/best/paper.tex:105:\\caption{DocRED count curve (96 relation types, Qwen3-32B). Accuracy degrades by 42.4pp from singleton to full schema. Mean BCS (Batch Confusability Score) increases mechanically with count.}\nartifacts/dream_reports/dream_20260515T140829/best/paper.tex:131:\\subsection{BCS-Controlled Confusability Effect}\nartifacts/dream_reports/dream_20260515T140829/best/paper.tex:133:To isolate confusability from count, we fix $k$ and compare batches with low vs.\\ high Batch Confusability Scores (BCS).\nartifacts/dream_reports/dream_20260515T140829/best/paper.tex:136:At $k=8$: low-BCS accuracy 0.745 vs.\\ high-BCS 0.462 ($\\Delta = -28.3$pp). At $k=16$: $\\Delta = -28.7$pp (Table~\\ref{tab:docred-bcs}). This confusability effect is comparable to FewRel's $-31.2$pp, confirming the signal generalizes to document-level RE.\nartifacts/dream_reports/dream_20260515T140829/best/paper.tex:143:Count & Low-BCS Acc & High-BCS Acc & $\\Delta$ (pp) \\\\\nartifacts/dream_reports/dream_20260515T140829/best/paper.tex:149:\\caption{DocRED BCS-controlled comparison. Confusability accounts for $\\sim$28pp accuracy gap at fixed type count.}\nartifacts/dream_reports/dream_20260515T140829/best/paper.tex:156:We conduct a $2 \\times 2$ factorial experiment on Few-NERD: $\\{\\text{low count}=6, \\text{high count}=22\\} \\times \\{\\text{low BCS}, \\text{high BCS}\\}$.\nartifacts/dream_reports/dream_20260515T140829/best/paper.tex:165: & Low BCS & High BCS & BCS Effect \\\\\nartifacts/dream_reports/dream_20260515T140829/best/paper.tex:178:The mechanistic dissociation is further supported by error analysis: count primarily reduces recall (low-count recall 0.482 vs.\\ high-count 0.385, $\\Delta = -0.099$; BCS effect on recall only $-0.021$), while confusability primarily increases type confusion rate (low-BCS confusion 0.008--0.012 vs.\\ high-BCS 0.042--0.048, a $\\sim$3.5$\\times$ increase; count effect on confusion only 1.4$\\times$).\nartifacts/dream_reports/dream_20260515T140829/best/paper.tex:185:\\subsection{Pairwise SCS--Confusion Correlation}\nartifacts/dream_reports/dream_20260515T140829/best/paper.tex:187:We define the \\emph{Schema Confusability Score} (SCS) between type pair $(t_i, t_j)$ as the cosine similarity of their label embeddings.\nartifacts/dream_reports/dream_20260515T140829/best/paper.tex:188:We correlate SCS with empirical confusion rates (how often $t_i$ is predicted when $t_j$ is the gold type, or vice versa).\nartifacts/dream_reports/dream_20260515T140829/best/paper.tex:205:\\caption{Pairwise SCS--confusion correlation across three IE tasks. All correlations are significant with $r \\geq 0.12$.}\nartifacts/dream_reports/dream_20260515T140829/best/paper.tex:224:BCS $\\Delta$ ($k$=12)    & $-10.1$pp & $-10.5$pp \\\\\nartifacts/dream_reports/dream_20260515T140829/best/paper.tex:234:To establish the \\emph{mechanism} linking confusability to degradation, we classify all false positive predictions into four categories: (1) intra-batch type substitution, (2) extra-schema substitution, (3) boundary error, and (4) hallucination. We bin results by BCS quartile.\nartifacts/dream_reports/dream_20260515T140829/best/paper.tex:236:Table~\\ref{tab:error-taxonomy} shows a near-perfect monotonic relationship between BCS and intra-batch type substitution ($\\rho = 1.0$, $p < 0.001$; $\\chi^2 = 6{,}952$). At BCS $\\geq 0.95$, type substitution accounts for 49.4\\% of false positives, compared to 0\\% at BCS $= 0$. Boundary errors and hallucinations remain BCS-independent, confirming that confusability operates specifically on the type discrimination channel.\nartifacts/dream_reports/dream_20260515T140829/best/paper.tex:243:BCS Bin & $n_{\\text{FP}}$ & Intra-Sub & Extra-Sub & Boundary & Halluc. \\\\\nartifacts/dream_reports/dream_20260515T140829/best/paper.tex:251:\\caption{Error type distribution by BCS bin. Intra-batch type substitution increases monotonically with confusability ($\\rho = 1.0$), while boundary and hallucination errors remain approximately constant.}\nartifacts/dream_reports/dream_20260515T140829/best/paper.tex:257:A methodological finding: per-type aggregation of pairwise confusability (mean BCS) introduces a centrality confound on semantically homogeneous schemas.\nartifacts/dream_reports/dream_20260515T140829/best/paper.tex:258:On MAVEN, per-type mean BCS correlates \\emph{positively} with F1 ($\\rho = +0.189$ for Qwen3, $\\rho = +0.208$ for MiniLM)---opposite to the predicted direction. This occurs because, in homogeneous schemas, types with many semantic neighbors are \\emph{central, well-represented} types that LLMs extract well; mean BCS conflates confusability with type centrality.\nartifacts/dream_reports/dream_20260515T140829/best/paper.tex:273:Compute pairwise SCS for all type pairs. Construct a graph $G = (\\mathcal{T}, E)$ where $(t_i, t_j) \\in E$ iff $\\text{SCS}(t_i, t_j) > \\tau$ (threshold $\\tau = 0.8$ in experiments). Two variants define SCS:\nartifacts/dream_reports/dream_20260515T140829/best/paper.tex:275:\\item \\textbf{SDGD-zero}: SCS from embedding cosine similarity (zero calibration cost).\nartifacts/dream_reports/dream_20260515T140829/best/paper.tex:276:\\item \\textbf{SDGD-cal}: SCS from empirical confusion rates on 5--10 calibration examples per type.\nartifacts/dream_reports/dream_20260515T140829/best/paper.tex:374:\\subsection{SCS Proxy Validation}\nartifacts/dream_reports/dream_20260515T140829/best/paper.tex:376:We validate the embedding-based SCS proxy by correlating it with empirical confusion matrices (Table~\\ref{tab:scs-proxy}).\nartifacts/dream_reports/dream_20260515T140829/best/paper.tex:391:\\caption{SCS proxy validation: rank correlation between embedding similarity and empirical confusion. Extraction-model embeddings (Qwen3) perform best on cross-domain schemas (Few-NERD); generic embeddings (MiniLM) on homogeneous schemas (MAVEN).}\nartifacts/dream_reports/dream_20260515T140829/best/paper.tex:399:The confusability effect amplifies with schema complexity. BCS-controlled accuracy gaps scale from $-9.1$pp (FewRel 16-rel) to $-31.2$pp (FewRel 80-rel) to $-28.5$pp (DocRED 96-rel), a $\\sim$3.4$\\times$ amplification from 16 to 80 relations with saturation above $\\sim$80 types. Total count-curve degradation also scales: 12.6pp (16-rel) $\\to$ 35.3pp (80-rel) $\\to$ 42.4pp (96-rel).\nartifacts/dream_reports/dream_20260515T140829/worst/paper.tex:74:\\paragraph{Channel 2: Confusability $\\rightarrow$ Type Confusion.} When semantically similar types co-occur in a prompt, the model confuses type assignments. We quantify confusability using the Schema Confusability Score (SCS)---the cosine similarity between type name embeddings in a given embedding space $\\phi$:\nartifacts/dream_reports/dream_20260515T140829/worst/paper.tex:76:\\text{SCS}_\\phi(t_i, t_j) = \\cos(\\phi(t_i), \\phi(t_j))\nartifacts/dream_reports/dream_20260515T140829/worst/paper.tex:79:At the batch level, Batch Confusability Score (BCS) aggregates pairwise SCS:\nartifacts/dream_reports/dream_20260515T140829/worst/paper.tex:81:\\text{BCS}(B) = \\frac{2}{|B|(|B|-1)} \\sum_{i&lt;j} \\text{SCS}(t_i, t_j)\nartifacts/dream_reports/dream_20260515T140829/worst/paper.tex:86:SDGD operationalizes confusability into decomposition. Given a confusability graph $G{=}(\\mathcal{T}, E)$ where edges connect type pairs with $\\text{SCS} > \\tau$, graph coloring partitions $\\mathcal{T}$ into $k$ batches minimizing intra-batch confusability. Three variants:\nartifacts/dream_reports/dream_20260515T140829/worst/paper.tex:89:\\item \\textbf{SDGD-zero}: Uses embedding SCS directly. No calibration data needed.\nartifacts/dream_reports/dream_20260515T140829/worst/paper.tex:90:\\item \\textbf{SDGD-cal}: Replaces SCS with empirical confusion from 5--10 calibration examples per type.\nartifacts/dream_reports/dream_20260515T140829/worst/paper.tex:107:\\paragraph{Embeddings.} Qwen3, LLaMA, MiniLM (all-MiniLM-L6-v2). Used for SCS computation and proxy validation.\nartifacts/dream_reports/dream_20260515T140829/worst/paper.tex:113:We conduct a $2{\\times}2$ factorial experiment on Few-NERD with Qwen3-32B, crossing type count $\\{6, 22\\}$ with BCS level $\\{\\text{low}, \\text{high}\\}$. Table~\\ref{tab:factorial} reports F1 scores.\nartifacts/dream_reports/dream_20260515T140829/worst/paper.tex:120:& Low BCS & High BCS & BCS Effect \\\\\nartifacts/dream_reports/dream_20260515T140829/worst/paper.tex:140:BCS & 3.90 & 0.054 & 0.070 \\\\\nartifacts/dream_reports/dream_20260515T140829/worst/paper.tex:141:Count $\\times$ BCS & 0.42 & 0.520 & 0.008 \\\\\nartifacts/dream_reports/dream_20260515T140829/worst/paper.tex:148:Both main effects are directionally correct: higher count reduces F1 ($-4.9$pp, $p{=}0.013$) and higher BCS reduces F1 ($-3.6$pp, $p{=}0.054$). However, the interaction is non-significant ($F{=}0.42$, $p{=}0.52$, $\\eta^2{=}0.008$; Table~\\ref{tab:anova}). The BCS effect is \\emph{smaller} at high count ($-2.7$pp vs.\\ $-4.4$pp), suggesting a shared degradation floor rather than orthogonal channels.\nartifacts/dream_reports/dream_20260515T140829/worst/paper.tex:156:\\paragraph{Pairwise confusion correlation.} Table~\\ref{tab:crossmodel_pairwise} shows that none of the three embedding spaces produces a significant SCS--confusion correlation on LLaMA ($r \\leq 0.032$, $p \\geq 0.16$ in all cases), in stark contrast to Qwen3 ($r{=}0.156$, $p{<}10^{-11}$).\nartifacts/dream_reports/dream_20260515T140829/worst/paper.tex:170:\\caption{Pairwise SCS--confusion correlation across models ($n{=}1{,}953$ pairs). Confusability predicts Qwen3 errors but not LLaMA errors with any embedding.}\nartifacts/dream_reports/dream_20260515T140829/worst/paper.tex:174:\\paragraph{Batch-level BCS effect.} The BCS effect on LLaMA is marginal: $-1.5$pp at count~6 and $-2.2$pp at count~12 for extreme batches, compared to Qwen3's $-4.4$pp and $-8.2$pp (Table~\\ref{tab:crossmodel_bcs}). Confusion ratios are 1.8--2.1$\\times$ for LLaMA vs.\\ 10--28$\\times$ for Qwen3.\nartifacts/dream_reports/dream_20260515T140829/worst/paper.tex:184:BCS $\\Delta$ count\\_6 & $-$4.4pp & $-$1.5pp \\\\\nartifacts/dream_reports/dream_20260515T140829/worst/paper.tex:185:BCS $\\Delta$ count\\_12 & $-$8.2pp & $-$2.2pp \\\\\nartifacts/dream_reports/dream_20260515T140829/worst/paper.tex:220:\\subsection{SCS Proxy Validation}\nartifacts/dream_reports/dream_20260515T140829/worst/paper.tex:223:Before evaluating SDGD, we assess the quality of embedding-based SCS as a proxy for empirical type confusion. Table~\\ref{tab:scs_proxy} reports rank correlations between SCS and empirical confusion matrices.\nartifacts/dream_reports/dream_20260515T140829/worst/paper.tex:238:\\caption{SCS vs.\\ empirical confusion correlation. The best proxy (Qwen3 on Few-NERD, $\\rho{=}0.18$) explains ${\\sim}3\\%$ of variance. Top-50 recall shows that 72--92\\% of SDGD's separation decisions target non-confusable pairs.}\nartifacts/dream_reports/dream_20260515T140829/worst/paper.tex:242:[Omitted long matching line]\nartifacts/dream_reports/dream_20260515T140829/worst/paper.tex:296:\\paragraph{SDGD-cal.} Replacing embedding SCS with empirical confusion (5-example calibration) yields marginal improvement over SDGD-zero (+2.7~F1) but remains far below single-pass ($-16.7$) and even below random ($-4.2$). The calibration confusion matrix correlates only weakly with the full matrix ($\\rho{=}0.31$, $\\tau{=}0.22$).\nartifacts/dream_reports/dream_20260515T140829/worst/paper.tex:330:We test confusability on document-level RE using DocRED (96 relations, Qwen3-32B). Table~\\ref{tab:docred_count} shows the count curve; Table~\\ref{tab:docred_bcs} shows BCS-controlled results.\nartifacts/dream_reports/dream_20260515T140829/worst/paper.tex:337:Count & Acc & BCS$_\\text{mean}$ & $n$ batches \\\\\nartifacts/dream_reports/dream_20260515T140829/worst/paper.tex:356:Count & Low-BCS Acc & High-BCS Acc & $\\Delta$ \\\\\nartifacts/dream_reports/dream_20260515T140829/worst/paper.tex:362:\\caption{DocRED BCS-controlled accuracy. The confusability effect is marginal ($4$--$5$pp), far smaller than on sentence-level tasks.}\nartifacts/dream_reports/dream_20260515T140829/worst/paper.tex:366:[Omitted long matching line]\nartifacts/dream_reports/dream_20260515T140829/worst/paper.tex:381:[Omitted long matching line]\nartifacts/dream_reports/dream_20260515T140829/worst/paper.tex:392:\\item \\textbf{Adequate confusability proxy.} Current embedding-based SCS ($\\rho \\leq 0.18$) is too weak. SDGD-cal's empirical confusion improves grouping marginally but cannot overcome merge amplification.\nartifacts/dream_reports/dream_20260515T140829/median/paper.tex:26:[Omitted long matching line]\nartifacts/dream_reports/dream_20260515T140829/median/paper.tex:43:    \\item \\textbf{Pairwise confusability as a robust signal.} We validate that embedding-based pairwise Schema Confusability Scores (SCS) predict empirical type confusion ($\\rho=0.35$, $p<10^{-4}$) across tasks and models, while per-type aggregation introduces centrality confounds in homogeneous schemas (Section~\\ref{sec:confusability}).\nartifacts/dream_reports/dream_20260515T140829/median/paper.tex:79:\\subsection{Schema Confusability Score (SCS)}\nartifacts/dream_reports/dream_20260515T140829/median/paper.tex:83:    \\text{SCS}(t_i, t_j) = \\frac{\\mathbf{e}(t_i) \\cdot \\mathbf{e}(t_j)}{\\|\\mathbf{e}(t_i)\\| \\|\\mathbf{e}(t_j)\\|}\nartifacts/dream_reports/dream_20260515T140829/median/paper.tex:85:where $\\mathbf{e}(\\cdot)$ is an embedding model (Qwen3-32B or MiniLM-L6-v2). For batch-level analysis, we define the \\emph{Batch Confusability Score} (BCS) as the mean pairwise SCS within a batch.\nartifacts/dream_reports/dream_20260515T140829/median/paper.tex:90:SDGD partitions a schema's types into $k$ batches by constructing a pairwise confusability graph $G = (V, E)$ where vertices are types and edge weights are pairwise SCS values. We threshold edges at the median SCS and apply graph coloring to minimize intra-batch confusability. We evaluate three variants:\nartifacts/dream_reports/dream_20260515T140829/median/paper.tex:93:    \\item \\textbf{SDGD-zero}: Uses embedding SCS directly (no calibration data).\nartifacts/dream_reports/dream_20260515T140829/median/paper.tex:94:    \\item \\textbf{SDGD-cal}: Replaces embedding SCS with empirical confusion estimates from 8--10 calibration examples per type.\nartifacts/dream_reports/dream_20260515T140829/median/paper.tex:106:\\textbf{Qwen3-32B-Instruct}~(primary extraction model) and \\textbf{LLaMA-3.3-70B-Instruct}~(multi-model validation). Embeddings from Qwen3-32B and MiniLM-L6-v2 for SCS computation.\nartifacts/dream_reports/dream_20260515T140829/median/paper.tex:116:We first validate that embedding-based SCS predicts empirical type confusion by comparing SCS rankings against empirical confusion matrices derived from model outputs.\nartifacts/dream_reports/dream_20260515T140829/median/paper.tex:118:\\paragraph{SCS vs.\\ empirical confusion.}\nartifacts/dream_reports/dream_20260515T140829/median/paper.tex:119:Table~\\ref{tab:scs-validation} shows rank correlations between embedding SCS and empirical confusion counts across 420 type pairs with nonzero empirical confusion on Few-NERD. Qwen3 embeddings achieve Spearman $\\rho=0.35$ ($p=10^{-4}$) and Kendall $\\tau=0.27$; MiniLM embeddings achieve $\\rho=0.28$ ($p=10^{-3}$). Both are highly significant, confirming SCS as a directionally useful proxy, though far from a perfect predictor.\nartifacts/dream_reports/dream_20260515T140829/median/paper.tex:123:\\caption{SCS vs.\\ empirical confusion rank correlation on Few-NERD (420 type pairs with nonzero empirical confusion).}\nartifacts/dream_reports/dream_20260515T140829/median/paper.tex:136:Table~\\ref{tab:top-pairs} shows the five most confused type pairs empirically and their SCS rankings. Intra-domain pairs (person subtypes, building subtypes) are well-predicted by SCS (ranks 2, 3, 5, 7). However, cross-domain pairs like \\texttt{location-GPE} $\\leftrightarrow$ \\texttt{location-bodiesofwater} (empirical rank 4, SCS rank 18) reveal that type-name semantics capture intra-domain confusion well but miss context-dependent cross-domain false positives.\nartifacts/dream_reports/dream_20260515T140829/median/paper.tex:140:\\caption{Top 5 empirically confused type pairs on Few-NERD with their SCS-predicted ranks (Qwen3 embeddings).}\nartifacts/dream_reports/dream_20260515T140829/median/paper.tex:144:\\textbf{Rank} & \\textbf{Type pair} & \\textbf{Emp.\\ confusion} & \\textbf{SCS rank} \\\\\nartifacts/dream_reports/dream_20260515T140829/median/paper.tex:182:We test channel independence with a $2 \\times 2$ factorial design on Few-NERD: \\{low count (6 types), high count (22 types)\\} $\\times$ \\{low BCS ($\\leq Q_1$), high BCS ($\\geq Q_3$)\\}. Table~\\ref{tab:factorial} shows the F1 results.\nartifacts/dream_reports/dream_20260515T140829/median/paper.tex:186:\\caption{$2 \\times 2$ factorial results (F1) on Few-NERD. Both count and BCS main effects are significant; the interaction is not.}\nartifacts/dream_reports/dream_20260515T140829/median/paper.tex:190:& \\textbf{Low BCS ($\\leq Q_1$)} & \\textbf{High BCS ($\\geq Q_3$)} \\\\\nartifacts/dream_reports/dream_20260515T140829/median/paper.tex:199:Table~\\ref{tab:anova} reports the two-way ANOVA. Both main effects are significant: count ($F=8.7$, $p=0.004$) and BCS ($F=10.6$, $p=0.002$). The interaction term is not significant ($F=1.7$, $p=0.14$), consistent with an additive multi-channel model. The count main effect is $-0.08$ F1 and the BCS main effect is $-0.09$ F1, indicating that confusability contributes slightly more than count to degradation.\nartifacts/dream_reports/dream_20260515T140829/median/paper.tex:210:BCS           & 0.051 & 10.6 & 0.002 \\\\\nartifacts/dream_reports/dream_20260515T140829/median/paper.tex:211:Count $\\times$ BCS & 0.008 & 1.7  & 0.14 \\\\\nartifacts/dream_reports/dream_20260515T140829/median/paper.tex:222:To test whether confusability effects generalize beyond sentence-level NER, we replicate the count-curve and BCS-controlled analyses on DocRED, a document-level relation extraction dataset with 96 relation types.\nartifacts/dream_reports/dream_20260515T140829/median/paper.tex:229:\\caption{DocRED count curve: accuracy and mean BCS as a function of the number of relation types per prompt.}\nartifacts/dream_reports/dream_20260515T140829/median/paper.tex:233:\\textbf{Count} & \\textbf{Accuracy} & \\textbf{Mean BCS} & \\textbf{$n$ batches} \\\\\nartifacts/dream_reports/dream_20260515T140829/median/paper.tex:246:\\paragraph{BCS-controlled analysis.}\nartifacts/dream_reports/dream_20260515T140829/median/paper.tex:247:Table~\\ref{tab:docred-bcs} isolates the confusability effect by comparing low-BCS and high-BCS batches at matched type counts. At count 8, high-BCS batches score 14.5 percentage points lower than low-BCS ($0.335$ vs.\\ $0.480$); at count 16, the gap widens to 18.3 pp ($0.247$ vs.\\ $0.430$). The BCS effect amplifies with count, consistent with the multi-channel model.\nartifacts/dream_reports/dream_20260515T140829/median/paper.tex:251:\\caption{DocRED BCS-controlled comparison: accuracy by BCS quartile at matched type counts.}\nartifacts/dream_reports/dream_20260515T140829/median/paper.tex:255:\\textbf{Count} & \\textbf{Low BCS acc} & \\textbf{High BCS acc} & \\textbf{$\\Delta$ (pp)} \\\\\nartifacts/dream_reports/dream_20260515T140829/median/paper.tex:263:[Omitted long matching line]\nartifacts/dream_reports/dream_20260515T140829/median/paper.tex:328:Table~\\ref{tab:llama-count} shows LLaMA-3.3-70B's count curve on Few-NERD. Unlike Qwen3's monotonic degradation, LLaMA exhibits a non-monotonic pattern, with F1 recovering at intermediate counts (0.31 at count 12, 0.35 at count 44) before declining again. The BCS-controlled effect at count 12 is $-6.0$ F1 points ($\\text{partial } r = 0.32$, $p = 0.04$), directionally consistent with Qwen3 but smaller in magnitude.\nartifacts/dream_reports/dream_20260515T140829/median/paper.tex:376:On MAVEN, per-type aggregation (mean BCS) produces a \\emph{positive} correlation with F1---the opposite of the hypothesized direction. This is not a failure of the confusability hypothesis but a confound: in semantically homogeneous schemas, types with many semantic neighbors are central, well-represented types that LLMs extract well. Pairwise confusability, which operates at the type-pair level, is immune to this aggregation artifact and remains valid across all tested schemas.\nartifacts/dream_reports/dream_20260515T140829/median/paper.tex:379:[Omitted long matching line]\nartifacts/dream_reports/dream_20260516T073533/best/paper.tex:23:We find that pairwise type confusability (measured via schema cosine similarity, SCS) independently predicts extraction degradation across all tasks ($r{=}0.11$--$0.13$, all CIs exclude zero), with 10--28$\\times$ more type confusion errors in high-confusability batches.\nartifacts/dream_reports/dream_20260516T073533/best/paper.tex:73:\\paragraph{Schema Cosine Similarity (SCS).}\nartifacts/dream_reports/dream_20260516T073533/best/paper.tex:76:\\text{SCS}(t_i, t_j) = \\frac{\\mathbf{e}_i \\cdot \\mathbf{e}_j}{\\|\\mathbf{e}_i\\| \\|\\mathbf{e}_j\\|}\nartifacts/dream_reports/dream_20260516T073533/best/paper.tex:81:\\paragraph{Batch Confusability Score (BCS).}\nartifacts/dream_reports/dream_20260516T073533/best/paper.tex:82:For a batch of types $B = \\{t_1, \\ldots, t_k\\}$, BCS is the mean pairwise SCS:\nartifacts/dream_reports/dream_20260516T073533/best/paper.tex:84:\\text{BCS}(B) = \\frac{2}{k(k-1)} \\sum_{i&lt;j} \\text{SCS}(t_i, t_j)\nartifacts/dream_reports/dream_20260516T073533/best/paper.tex:86:BCS captures the overall confusability pressure within a single extraction prompt.\nartifacts/dream_reports/dream_20260516T073533/best/paper.tex:94:BCS is recorded as a covariate.\nartifacts/dream_reports/dream_20260516T073533/best/paper.tex:96:\\paragraph{BCS-Controlled Comparisons.}\nartifacts/dream_reports/dream_20260516T073533/best/paper.tex:97:At fixed type count $k$, we construct matched batch pairs: one with low BCS (dissimilar types) and one with high BCS (confusable types).\nartifacts/dream_reports/dream_20260516T073533/best/paper.tex:101:On Few-NERD, we cross \\{low count, high count\\} $\\times$ \\{low BCS, high BCS\\} to test for additive vs.\\ multiplicative interaction between the two factors.\nartifacts/dream_reports/dream_20260516T073533/best/paper.tex:121:SDGD constructs a confusability graph $G = (V, E)$ where vertices are types and edge weights are pairwise SCS values.\nartifacts/dream_reports/dream_20260516T073533/best/paper.tex:125:\\item \\textbf{SDGD-zero}: Uses SCS (embedding similarity) directly.\nartifacts/dream_reports/dream_20260516T073533/best/paper.tex:131:\\subsection{SCS as Confusability Proxy}\nartifacts/dream_reports/dream_20260516T073533/best/paper.tex:134:We first validate that embedding-based SCS is a meaningful proxy for actual LLM confusion by comparing SCS to an empirical confusion matrix constructed from Few-NERD extraction outputs (1,953 type pairs, 216 with nonzero confusion).\nartifacts/dream_reports/dream_20260516T073533/best/paper.tex:149:\\caption{SCS vs.\\ empirical confusion matrix correlation. Both embeddings significantly predict actual confusion ($p < 10^{-5}$). Qwen3 is stronger on all pairs; MiniLM is stronger among actually-confused pairs.}\nartifacts/dream_reports/dream_20260516T073533/best/paper.tex:153:Table~\\ref{tab:scs-validation} shows that SCS from both embeddings significantly predicts empirical confusion.\nartifacts/dream_reports/dream_20260516T073533/best/paper.tex:154:The correlation is moderate ($\\rho{=}0.14$--$0.31$), indicating that SCS is a valid but partial proxy: confusability has dimensions beyond embedding similarity (e.g., context-dependent ambiguity, frequency-driven familiarity).\nartifacts/dream_reports/dream_20260516T073533/best/paper.tex:155:This ``valid but partial'' status supports using SCS for correlational analysis while explaining why SCS-based decomposition (SDGD-zero) underperforms empirical-confusion-based decomposition (SDGD-cal).\nartifacts/dream_reports/dream_20260516T073533/best/paper.tex:167:\\textbf{Count} & \\textbf{Accuracy} & \\textbf{$n$ Batches} & \\textbf{Mean BCS} \\\\\nartifacts/dream_reports/dream_20260516T073533/best/paper.tex:187:\\textbf{Count} & \\textbf{Low BCS} & \\textbf{High BCS} & \\textbf{$\\Delta$(pp)} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\nartifacts/dream_reports/dream_20260516T073533/best/paper.tex:193:\\caption{DocRED BCS-controlled accuracy. At fixed count, high-BCS batches show significantly lower accuracy (slope=$-0.713$, 95\\% CI [$-0.909, -0.529$]).}\nartifacts/dream_reports/dream_20260516T073533/best/paper.tex:199:Controlling for count, BCS independently predicts degradation: at count=16, high-BCS batches are 23.3pp worse than low-BCS batches ($\\rho{=}{-}0.661$, $p{<}0.001$; Table~\\ref{tab:docred-bcs}).\nartifacts/dream_reports/dream_20260516T073533/best/paper.tex:215: & \\textbf{Low BCS} & \\textbf{High BCS} & \\textbf{BCS Effect} \\\\\nartifacts/dream_reports/dream_20260516T073533/best/paper.tex:228:The main effects are: count $-0.018$, BCS $-0.029$.\nartifacts/dream_reports/dream_20260516T073533/best/paper.tex:232:The BCS effect is numerically larger at high count ($-0.048$ vs.\\ $-0.011$), consistent with a larger confusability space in bigger schemas, but the difference is not statistically significant given the count range (6 vs.\\ 12).\nartifacts/dream_reports/dream_20260516T073533/best/paper.tex:237:We classify false positive predictions by error type across BCS bins to provide mechanistic evidence for the two-channel model.\nartifacts/dream_reports/dream_20260516T073533/best/paper.tex:244:\\textbf{BCS Bin} & \\textbf{$n$ FP} & \\textbf{IntraSub\\%} & \\textbf{ExtraSub\\%} & \\textbf{IntraSub/100g} \\\\\nartifacts/dream_reports/dream_20260516T073533/best/paper.tex:252:\\caption{Error distribution by BCS bin on Few-NERD. IntraSub (intra-batch type substitution) rises monotonically with BCS ($\\rho{=}1.0$), while hallucination remains below 3\\% across all bins.}\nartifacts/dream_reports/dream_20260516T073533/best/paper.tex:261:\\textbf{Task} & \\textbf{IntraSub vs BCS $\\rho$} & \\textbf{$p$} & \\textbf{ExtraSub=0?} \\\\\nartifacts/dream_reports/dream_20260516T073533/best/paper.tex:267:\\caption{Cross-task error taxonomy comparison. IntraSub rate correlates near-perfectly with BCS on both tasks.}\nartifacts/dream_reports/dream_20260516T073533/best/paper.tex:271:Table~\\ref{tab:error-taxonomy} shows a near-perfect monotonic relationship between BCS and IntraSub errors on Few-NERD.\nartifacts/dream_reports/dream_20260516T073533/best/paper.tex:272:At BCS=0 (single-type batches), IntraSub is 0\\% by definition---there are no other types to confuse.\nartifacts/dream_reports/dream_20260516T073533/best/paper.tex:273:As BCS increases, IntraSub rises to 49.4\\% of all false positives in high-BCS batches (12.9 per 100 gold entities).\nartifacts/dream_reports/dream_20260516T073533/best/paper.tex:309:The improvement from SDGD-zero to SDGD-cal (+18\\%) confirms that empirical confusion is a better partition signal than SCS ($\\rho{=}0.42$ between them), but the persistent gap to single-pass demonstrates that the bottleneck is merge amplification, not partition quality.\nartifacts/dream_reports/dream_20260516T073533/best/paper.tex:389:\\textbf{Method} & \\textbf{F1} & \\textbf{Prec.} & \\textbf{Rec.} & \\textbf{$k$} & \\textbf{BCS} & \\textbf{Time(s)} \\\\\nartifacts/dream_reports/dream_20260516T073533/best/paper.tex:410:The pairwise SCS--confusion correlations ($r{=}0.11$--$0.13$) are small in absolute terms but meaningful in context.\nartifacts/dream_reports/dream_20260516T073533/best/paper.tex:416:On MAVEN (168 event types from a semantically homogeneous domain), per-type BCS aggregation shows a \\emph{positive} correlation with F1 ($\\rho{=}{+}0.19$--$0.21$), opposite to the expected direction.\nartifacts/dream_reports/dream_20260516T073533/best/paper.tex:417:This occurs because in homogeneous schemas, high mean BCS indicates central, well-represented types that LLMs extract well---conflating confusability with type centrality.\nartifacts/dream_reports/dream_20260516T073533/worst/paper.tex:60:\\subsection{Schema Confusability Score (SCS)}\nartifacts/dream_reports/dream_20260516T073533/worst/paper.tex:65:\\text{SCS}(t_i, t_j) = \\cos(\\mathbf{e}(t_i), \\mathbf{e}(t_j))\nartifacts/dream_reports/dream_20260516T073533/worst/paper.tex:67:where $\\mathbf{e}(t)$ is the embedding of type $t$'s name and definition. For batch-level aggregation, we compute the mean pairwise SCS (Batch Confusability Score, BCS):\nartifacts/dream_reports/dream_20260516T073533/worst/paper.tex:69:\\text{BCS}(\\mathcal{B}) = \\frac{2}{|\\mathcal{B}|(|\\mathcal{B}|-1)} \\sum_{i&lt;j} \\text{SCS}(t_i, t_j)\nartifacts/dream_reports/dream_20260516T073533/worst/paper.tex:86:SDGD constructs a confusability graph $G = (\\mathcal{S}, E)$ where edge weight $w(t_i, t_j) = \\text{SCS}(t_i, t_j)$. Graph coloring with a maximum BCS threshold partitions types into batches minimizing within-batch confusability. We evaluate two variants:\nartifacts/dream_reports/dream_20260516T073533/worst/paper.tex:88:\\item \\textbf{SDGD-zero}: Uses embedding SCS directly (zero-shot, no labeled data).\nartifacts/dream_reports/dream_20260516T073533/worst/paper.tex:89:\\item \\textbf{SDGD-cal}: Uses empirical confusion from $n$ calibration examples to replace SCS estimates where observations exist.\nartifacts/dream_reports/dream_20260516T073533/worst/paper.tex:101:We evaluate count curves and BCS effects on DocRED (96 relation types, document-level RE requiring multi-hop reasoning).\nartifacts/dream_reports/dream_20260516T073533/worst/paper.tex:108:\\textbf{Count} & \\textbf{Accuracy} & \\textbf{BCS (mean)} & \\textbf{$n$ batches} \\\\\nartifacts/dream_reports/dream_20260516T073533/worst/paper.tex:119:\\caption{DocRED count curve. Accuracy degrades from 0.82 (single type) to 0.31 (full schema), but count and BCS are confounded at the batch level.}\nartifacts/dream_reports/dream_20260516T073533/worst/paper.tex:128:\\textbf{Condition} & \\textbf{Accuracy} & \\textbf{BCS} & \\textbf{$n$} \\\\\nartifacts/dream_reports/dream_20260516T073533/worst/paper.tex:130:Low BCS & 0.52 & 0.58 & 5 \\\\\nartifacts/dream_reports/dream_20260516T073533/worst/paper.tex:131:High BCS & 0.44 & 0.92 & 5 \\\\\nartifacts/dream_reports/dream_20260516T073533/worst/paper.tex:135:\\caption{BCS-controlled comparison at count=16 on DocRED. Effect direction is consistent ($\\Delta$=$-$8.3pp) but CI crosses zero [$-$16.1, +0.5]pp due to $n$=5.}\nartifacts/dream_reports/dream_20260516T073533/worst/paper.tex:139:The count curve shows degradation (0.82$\\rightarrow$0.31) but cannot disentangle count from prompt-length effects in document-level RE. The BCS effect at count=16 shows the expected direction ($-$8.3pp) but is inconclusive: Pearson $r$=$-$0.22 ($p$=0.14), Spearman $\\rho$=$-$0.19 ($p$=0.21). Unlike sentence-level FewRel ($\\Delta$=$-$31.2pp), document-level RE introduces entity-pair localization errors that dilute the confusability signal.\nartifacts/dream_reports/dream_20260516T073533/worst/paper.tex:144:We test whether count and confusability interact multiplicatively on Few-NERD using a \\{low count (6), high count (12)\\} $\\times$ \\{low BCS, high BCS\\} design.\nartifacts/dream_reports/dream_20260516T073533/worst/paper.tex:151:& \\textbf{Low BCS} & \\textbf{High BCS} & \\textbf{Marginal} \\\\\nartifacts/dream_reports/dream_20260516T073533/worst/paper.tex:159:\\caption{2$\\times$2 cell means (F1) on Few-NERD. Main effects: count $-$1.8pp, BCS $-$2.9pp. Interaction: $z$=$-$0.67, $p$=0.50.}\nartifacts/dream_reports/dream_20260516T073533/worst/paper.tex:163:The interaction term is non-significant ($p$=0.50), consistent with an additive model but also with insufficient statistical power. The BCS effect is numerically larger at high count ($-$4.0pp vs $-$2.0pp), directionally supporting multiplicative interaction, but the study is underpowered to detect it due to limited BCS range in random Few-NERD batches (0.79--0.87) and small count span (6 vs 12).\nartifacts/dream_reports/dream_20260516T073533/worst/paper.tex:165:\\subsection{Error Taxonomy (BCS-Binned)}\nartifacts/dream_reports/dream_20260516T073533/worst/paper.tex:168:We systematically classify false positives across BCS bins to provide mechanistic evidence for the multi-channel model.\nartifacts/dream_reports/dream_20260516T073533/worst/paper.tex:175:\\textbf{BCS Bin} & \\textbf{$n_{\\text{FP}}$} & \\textbf{IntraSub} & \\textbf{ExtraSub} & \\textbf{Boundary} & \\textbf{Halluc.} \\\\\nartifacts/dream_reports/dream_20260516T073533/worst/paper.tex:183:\\caption{Error distribution by BCS bin on Few-NERD. IntraSub (type confusion) rises monotonically from 0\\% to 49.4\\% as batch confusability increases.}\nartifacts/dream_reports/dream_20260516T073533/worst/paper.tex:198:\\caption{Cross-task IntraSub--BCS correlation. Perfect or near-perfect monotonic relationship on both tasks.}\nartifacts/dream_reports/dream_20260516T073533/worst/paper.tex:202:The error taxonomy provides the clearest mechanistic evidence for Channel 2: intra-schema substitution errors are absent at zero confusability and dominate at high confusability (49.4\\% of all FPs). This trend replicates across NER and RE ($\\rho$=1.0, $\\rho$=0.954). Notably, ExtraSub remains dominant at medium BCS, suggesting that even moderately confusable schemas primarily suffer from coverage limitations (Channel 1) rather than confusion (Channel 2).\nartifacts/dream_reports/dream_20260516T073533/worst/paper.tex:204:\\subsection{SCS Validation: Embedding vs.\\ Empirical Confusion}\nartifacts/dream_reports/dream_20260516T073533/worst/paper.tex:207:We validate whether embedding-based SCS predicts actual model confusion patterns by correlating pairwise SCS with empirical confusion matrix entries.\nartifacts/dream_reports/dream_20260516T073533/worst/paper.tex:222:\\caption{SCS$\\rightarrow$Empirical confusion validation on Few-NERD. Correlations are significant but explain only 2.8--9.4\\% of confusion variance.}\nartifacts/dream_reports/dream_20260516T073533/worst/paper.tex:226:[Omitted long matching line]\nartifacts/dream_reports/dream_20260516T073533/worst/paper.tex:256:SDGD-cal replaces embedding SCS with empirical confusion estimates from 10 calibration examples.\nartifacts/dream_reports/dream_20260516T073533/worst/paper.tex:285:SCS fallback pairs & 4093 \\\\\nartifacts/dream_reports/dream_20260516T073533/worst/paper.tex:286:Cal vs.\\ SCS rank agreement & 0.58 \\\\\nartifacts/dream_reports/dream_20260516T073533/worst/paper.tex:289:\\caption{Calibration confusion matrix properties. With 10 samples over 66 types, 94\\% of type pairs have no observed confusion and fall back to SCS estimates.}\nartifacts/dream_reports/dream_20260516T073533/worst/paper.tex:293:SDGD-cal improves over SDGD-zero by 2.7pp but remains 17.7pp below single-pass. The calibration matrix is extremely sparse (94\\% zeros with 10 examples), meaning most edge weights fall back to SCS. This demonstrates that the decomposition failure is not an estimation problem (better confusability estimates do not help) but an architectural problem: merge amplification is inherent to multi-batch extraction regardless of grouping quality.\nartifacts/dream_reports/dream_20260516T073533/worst/paper.tex:380:\\item IntraSub--BCS correlation: $\\rho$=1.0 (NER), $\\rho$=0.954 (RE)\nartifacts/dream_reports/dream_20260516T073533/worst/paper.tex:381:\\item SCS$\\rightarrow$confusion: $\\rho$=0.17--0.31 ($p<10^{-5}$)\nartifacts/dream_reports/dream_20260516T073533/worst/paper.tex:397:\\item \\textbf{Do not rely on embedding SCS alone} for schema quality assessment; $R^2 < 10\\%$ means the proxy misses 90\\%+ of the factors driving confusion.\nartifacts/dream_reports/dream_20260516T073533/worst/paper.tex:404:\\paragraph{DocRED inconclusive.} The BCS effect on document-level RE is directionally consistent but statistically inconclusive ($n$=5). Larger-scale document-level experiments are needed.\nartifacts/dream_reports/dream_20260516T073533/worst/paper.tex:406:\\paragraph{Interaction power.} The 2$\\times$2 interaction test is underpowered due to limited BCS range in natural Few-NERD batches. A stronger test requires synthetic schemas with controlled BCS.\nartifacts/dream_reports/dream_20260516T073533/median/paper.tex:30:We validate embedding-based Schema Confusability Scores (SCS) as significant predictors of empirical confusion ($\\rho{=}0.168$--$0.306$, all $p < 10^{-4}$), though with limited variance explained ($R^2{=}3$--$9\\%$).\nartifacts/dream_reports/dream_20260516T073533/median/paper.tex:89:\\subsection{Schema Confusability Score (SCS)}\nartifacts/dream_reports/dream_20260516T073533/median/paper.tex:91:We operationalize pairwise confusability using the \\textbf{Schema Confusability Score} (SCS): the cosine similarity between type-name embeddings. For a schema $\\mathcal{S} = \\{t_1, \\ldots, t_n\\}$:\nartifacts/dream_reports/dream_20260516T073533/median/paper.tex:93:\\text{SCS}(t_i, t_j) = \\frac{\\mathbf{e}(t_i) \\cdot \\mathbf{e}(t_j)}{\\|\\mathbf{e}(t_i)\\| \\|\\mathbf{e}(t_j)\\|}\nartifacts/dream_reports/dream_20260516T073533/median/paper.tex:97:For batch-level aggregation, the \\textbf{Batch Confusability Score} (BCS) is the mean pairwise SCS within a batch of types.\nartifacts/dream_reports/dream_20260516T073533/median/paper.tex:102:Given a confusability graph $G = (\\mathcal{S}, E)$ where edge weights are pairwise SCS values, SDGD applies graph coloring to assign types to batches such that highly confusable pairs are separated.\nartifacts/dream_reports/dream_20260516T073533/median/paper.tex:106:\\item \\textbf{SDGD-zero}: Uses embedding-based SCS to construct the confusability graph without any task-specific data.\nartifacts/dream_reports/dream_20260516T073533/median/paper.tex:121:\\item \\textbf{FewRel} (sentence-level RE): 80 relation types used in BCS-controlled experiments.\nartifacts/dream_reports/dream_20260516T073533/median/paper.tex:138:We classify false positive predictions into error types across BCS bins to directly test the multi-channel model. If confusability drives type confusion rather than detection failure, we expect IntraSub (correct span, wrong type from same batch) to increase monotonically with BCS while missed rate remains stable.\nartifacts/dream_reports/dream_20260516T073533/median/paper.tex:142:\\caption{Error taxonomy on Few-NERD (NER). IntraSub increases monotonically with BCS ($\\rho{=}1.0$, $p{<}0.001$). ExtraSub is never observed.}\nartifacts/dream_reports/dream_20260516T073533/median/paper.tex:146:BCS Bin & N\\_FP & IntraSub\\% & ExtraSub\\% & Other\\% \\\\\nartifacts/dream_reports/dream_20260516T073533/median/paper.tex:158:\\caption{Error taxonomy on FewRel 80-rel (RE). IntraSub increases with BCS ($\\rho{=}0.954$, $p{<}10^{-6}$). Missed rate remains in 10--16\\%, consistent with a count (not confusability) channel.}\nartifacts/dream_reports/dream_20260516T073533/median/paper.tex:162:BCS Bin    & Correct\\% & IntraSub\\% & Missed\\% \\\\\nartifacts/dream_reports/dream_20260516T073533/median/paper.tex:173:[Omitted long matching line]\nartifacts/dream_reports/dream_20260516T073533/median/paper.tex:177:\\caption{Cross-task monotonicity of IntraSub vs.\\ BCS.}\nartifacts/dream_reports/dream_20260516T073533/median/paper.tex:181:Task & IntraSub vs BCS $\\rho$ & $p$ \\\\\nartifacts/dream_reports/dream_20260516T073533/median/paper.tex:202:Count & Acc & BCS\\_mean & N\\_batches \\\\\nartifacts/dream_reports/dream_20260516T073533/median/paper.tex:217:\\caption{DocRED BCS-controlled analysis. At matched type counts, high-BCS batches underperform low-BCS batches, isolating confusability from count.}\nartifacts/dream_reports/dream_20260516T073533/median/paper.tex:221:Count & Low-BCS Acc & High-BCS Acc & $\\Delta$(pp) & $\\rho$ & $p$ \\\\\nartifacts/dream_reports/dream_20260516T073533/median/paper.tex:229:[Omitted long matching line]\nartifacts/dream_reports/dream_20260516T073533/median/paper.tex:233:\\subsection{SCS Validation: Embedding Proxy Quality}\nartifacts/dream_reports/dream_20260516T073533/median/paper.tex:236:A key assumption of our framework is that embedding-based SCS approximates actual model confusion. We validate this by correlating pairwise SCS with an empirical confusion matrix constructed from Few-NERD extraction errors.\nartifacts/dream_reports/dream_20260516T073533/median/paper.tex:240:\\caption{SCS $\\rightarrow$ empirical confusion validation. SCS is a significant but weak predictor of confusion; nonzero-only subset shows stronger ranking ability.}\nartifacts/dream_reports/dream_20260516T073533/median/paper.tex:254:Table~\\ref{tab:scs-valid} reports the results. Both embeddings achieve highly significant correlations on the full set of 1,953 type pairs (all $p < 10^{-10}$), confirming that SCS captures a real confusability signal. However, variance explained is low: $R^2 \\approx 3$--$5\\%$ on all pairs, rising to 7--9\\% when restricting to the 216 pairs with nonzero empirical confusion.\nartifacts/dream_reports/dream_20260516T073533/median/paper.tex:256:[Omitted long matching line]\nartifacts/dream_reports/dream_20260516T073533/median/paper.tex:265:\\caption{2$\\times$2 interaction design on Few-NERD (F1). The BCS effect is 4.4$\\times$ larger at count=12 than count=6, but the interaction is not statistically significant ($z{=}{-}0.67$, $p{=}0.50$).}\nartifacts/dream_reports/dream_20260516T073533/median/paper.tex:269:             & Low BCS & High BCS & BCS $\\Delta$ \\\\\nartifacts/dream_reports/dream_20260516T073533/median/paper.tex:280:Table~\\ref{tab:interaction} shows that the direction is consistent with the multiplicative hypothesis: the BCS effect at count=12 ($\\Delta{=}{-}4.8$pp) is 4.4$\\times$ larger than at count=6 ($\\Delta{=}{-}1.1$pp). However, the interaction is not statistically significant ($z{=}{-}0.67$, $p{=}0.50$).\nartifacts/dream_reports/dream_20260516T073533/median/paper.tex:282:This null result reflects an underpowered design rather than absence of interaction. The count contrast (6 vs.\\ 12) is narrow---Few-NERD's 66 types and the BCS range available (0.75--0.90) constrain the factorial space. Power analysis estimates $n \\approx 80$ per cell to achieve 0.8 power at this effect size, compared to $n{=}27$ in the current design. The main effects are individually small: count $\\Delta{=}{-}1.8$pp, BCS $\\Delta{=}{-}2.9$pp.\nartifacts/dream_reports/dream_20260516T073533/median/paper.tex:324:Table~\\ref{tab:random-ablation} confirms this pattern across datasets: at matched batch counts, random batching outperforms SDGD-zero by 4--7.5pp F1. This counterintuitive result has a clear explanation: SDGD-zero's graph coloring produces highly uneven batch sizes (some batches contain only 3--4 types, causing over-prediction) and concentrates all ``hard'' high-SCS types into the same batches, where precision collapses. Random batching distributes difficulty more evenly.\nartifacts/dream_reports/dream_20260516T073533/median/paper.tex:328:SDGD-cal replaces embedding-based SCS with an empirical confusion matrix from 5--10 calibration examples, directly capturing model-specific confusion patterns.\nartifacts/dream_reports/dream_20260516T073533/median/paper.tex:401:[Omitted long matching line]\nartifacts/dream_reports/dream_20260516T073533/median/paper.tex:412:[Omitted long matching line]\nartifacts/dream_reports/dream_20260515T053106/best/paper.tex:25:Batch confusability score (BCS) independently predicts F1 degradation after controlling for type frequency (partial $r{=}0.32$, $p{=}0.002$ on Few-NERD; $r{=}0.22$, $p{=}0.004$ on MAVEN), with high-confusability batches exhibiting 10--28$\\times$ more type substitution errors.\nartifacts/dream_reports/dream_20260515T053106/best/paper.tex:50:    \\item \\textbf{Pairwise BCS-confusion correlation} (immune to type frequency confounds) confirms that embedding-based confusability predicts empirical type confusion ($r{=}0.16$--$0.19$, $p{<}10^{-9}$) across 2 datasets and 2 models.\nartifacts/dream_reports/dream_20260515T053106/best/paper.tex:52:    \\item \\textbf{Error taxonomy} provides mechanistic evidence: type substitution errors rise monotonically with BCS (8\\%$\\to$68\\%), while false negatives decline (62\\%$\\to$15\\%), cleanly separating the two channels ($\\chi^2{=}142.3$, $p{=}2.1{\\times}10^{-24}$).\nartifacts/dream_reports/dream_20260515T053106/best/paper.tex:56:SDGD constructs a confusability graph where edges connect type pairs above an SCS threshold, then applies graph coloring to partition types into minimally confusable batches.\nartifacts/dream_reports/dream_20260515T053106/best/paper.tex:90:\\paragraph{Schema Confusability Score (SCS).}\nartifacts/dream_reports/dream_20260515T053106/best/paper.tex:93:    \\text{SCS}(t_i, t_j) = \\cos\\bigl(\\mathbf{e}(t_i),\\, \\mathbf{e}(t_j)\\bigr)\nartifacts/dream_reports/dream_20260515T053106/best/paper.tex:97:\\paragraph{Batch Confusability Score (BCS).}\nartifacts/dream_reports/dream_20260515T053106/best/paper.tex:100:    \\text{BCS}(B) = \\frac{2}{|B|(|B|-1)} \\sum_{i < j,\\; t_i,t_j \\in B} \\text{SCS}(t_i, t_j)\nartifacts/dream_reports/dream_20260515T053106/best/paper.tex:112:This manifests as increasing type confusion rate with increasing BCS, independent of batch size.\nartifacts/dream_reports/dream_20260515T053106/best/paper.tex:114:The additive interaction prediction: $\\Delta\\text{F1} \\approx \\alpha \\cdot \\Delta|B| + \\beta \\cdot \\Delta\\text{BCS}$, with no significant interaction term.\nartifacts/dream_reports/dream_20260515T053106/best/paper.tex:122:Construct an undirected graph $G = (\\mathcal{S}, E)$ where an edge $(t_i, t_j) \\in E$ iff $\\text{SCS}(t_i, t_j) > \\tau$ for a threshold $\\tau$.\nartifacts/dream_reports/dream_20260515T053106/best/paper.tex:133:\\textbf{SDGD-zero} uses only embedding-based SCS (no labeled examples required).\nartifacts/dream_reports/dream_20260515T053106/best/paper.tex:134:\\textbf{SDGD-cal} replaces SCS with an empirical confusion matrix estimated from a small calibration set (5--10 examples), capturing model-specific confusion patterns that embedding distance may miss.\nartifacts/dream_reports/dream_20260515T053106/best/paper.tex:186:\\paragraph{Pairwise BCS-Confusion Correlation.}\nartifacts/dream_reports/dream_20260515T053106/best/paper.tex:187:Table~\\ref{tab:pairwise} shows that pairwise SCS between type labels positively correlates with empirical confusion counts across both datasets and both models.\nartifacts/dream_reports/dream_20260515T053106/best/paper.tex:194:\\caption{Pairwise BCS-confusion correlation across datasets and models.}\nartifacts/dream_reports/dream_20260515T053106/best/paper.tex:207:To control for type frequency, we compute F1 per type and correlate with mean BCS, partialling out log frequency.\nartifacts/dream_reports/dream_20260515T053106/best/paper.tex:213:\\caption{Per-type partial correlation $r(\\text{F1}, \\text{mean\\_BCS} \\mid \\log\\text{freq})$.}\nartifacts/dream_reports/dream_20260515T053106/best/paper.tex:232:\\caption{Multi-model pairwise BCS-confusion comparison on Few-NERD.}\nartifacts/dream_reports/dream_20260515T053106/best/paper.tex:248:Table~\\ref{tab:factorial} presents the $\\{$low count, high count$\\} \\times \\{$low BCS, high BCS$\\}$ factorial on Few-NERD.\nartifacts/dream_reports/dream_20260515T053106/best/paper.tex:249:Count and BCS exert independent main effects on F1 ($-0.08$ and $-0.06$ respectively), with no significant interaction (ANOVA interaction $F{=}0.05$, $p{=}0.82$).\nartifacts/dream_reports/dream_20260515T053106/best/paper.tex:250:Recall is almost entirely explained by count (main effect $-0.20$ vs BCS's $-0.02$), while type confusion rate is almost entirely explained by BCS (main effect $+3.8\\%$ vs count's $+1.0\\%$).\nartifacts/dream_reports/dream_20260515T053106/best/paper.tex:259: & \\textbf{Low BCS} & \\textbf{High BCS} & \\textbf{BCS Effect} \\\\\nartifacts/dream_reports/dream_20260515T053106/best/paper.tex:270:Table~\\ref{tab:error_taxonomy} shows the distribution of error types across BCS bins on Few-NERD ($n{=}1{,}191$ errors).\nartifacts/dream_reports/dream_20260515T053106/best/paper.tex:271:Type substitution rises monotonically from 8\\% in the lowest BCS bin to 68\\% in the highest, while false negatives decline from 62\\% to 15\\%.\nartifacts/dream_reports/dream_20260515T053106/best/paper.tex:272:Boundary errors and hallucinations show no systematic BCS dependence.\nartifacts/dream_reports/dream_20260515T053106/best/paper.tex:273:A $\\chi^2$ test of independence yields $\\chi^2{=}142.3$ ($p{=}2.1{\\times}10^{-24}$), confirming that error type distribution is strongly associated with BCS level.\nartifacts/dream_reports/dream_20260515T053106/best/paper.tex:278:\\caption{Error taxonomy by BCS bin on Few-NERD ($n{=}1{,}191$ errors). Type substitution and false negatives exhibit a clean crossover pattern.}\nartifacts/dream_reports/dream_20260515T053106/best/paper.tex:282:\\textbf{BCS Bin} & \\textbf{TypeSub} & \\textbf{BndErr} & \\textbf{FalseNeg} & \\textbf{Halluc} & \\textbf{$n$} \\\\\nartifacts/dream_reports/dream_20260515T053106/best/paper.tex:377:Pairwise BCS-confusion correlation is $r{=}0.14$ ($p{=}0.0002$, $n{=}4{,}560$ pairs), and per-type partial $r{=}0.21$ ($p{=}0.04$).\nartifacts/dream_reports/dream_20260515T053106/best/paper.tex:378:The top confused pair \\emph{spouse} $\\leftrightarrow$ \\emph{unmarried\\_partner} ($\\text{SCS}{=}0.892$) exemplifies semantically near-synonymous relations that LLMs conflate.\nartifacts/dream_reports/dream_20260515T053106/best/paper.tex:381:\\subsection{SCS Proxy Validation}\nartifacts/dream_reports/dream_20260515T053106/best/paper.tex:384:We validate embedding-based SCS against empirical confusion matrices.\nartifacts/dream_reports/dream_20260515T053106/best/paper.tex:385:Spearman $\\rho{=}0.52$ ($p{=}1.8{\\times}10^{-15}$) on Few-NERD and $\\rho{=}0.48$ ($p{=}2.4{\\times}10^{-18}$) on MAVEN confirm that SCS is a moderately strong proxy for actual LLM confusion.\nartifacts/dream_reports/dream_20260515T053106/best/paper.tex:389:The 14 false-negative pairs missed by SCS but captured by calibration account for SDGD-cal's +1.5pp advantage on Few-NERD.\nartifacts/dream_reports/dream_20260515T053106/best/paper.tex:409:\\paragraph{Batch-level BCS-F1 positive correlation.}\nartifacts/dream_reports/dream_20260515T053106/best/paper.tex:410:At the batch level, high-BCS batches can show higher F1 due to type frequency confounding (high-frequency types tend to be semantically central, yielding both high BCS and high F1).\nartifacts/dream_reports/dream_20260515T053106/best/paper.tex:418:Across three IE tasks (NER, ED, RE), two datasets (Few-NERD, MAVEN), and two model families (Qwen, LLaMA), we showed that BCS independently predicts F1 degradation (partial $r{=}0.32$, $p{=}0.002$ on Few-NERD; $r{=}0.22$, $p{=}0.004$ on MAVEN), with 10--28$\\times$ type confusion ratios in extreme batches.\nartifacts/dream_reports/dream_20260515T053106/best/paper.tex:426:SCS threshold $\\tau$ was selected via a simple grid search; adaptive threshold selection could improve results further.\nartifacts/dream_reports/dream_20260515T053106/worst/paper.tex:27:Second, embedding-based semantic confusability scores (SCS), widely assumed to proxy inter-type confusability, fail as independent predictors of extraction degradation once type frequency is controlled (partial $r$=0.05, $p$=0.38 on MAVEN; BCS main effect $p$=0.42 in factorial analysis on Few-NERD).\nartifacts/dream_reports/dream_20260515T053106/worst/paper.tex:28:Third, a pairwise BCS-confusion correlation observed on one model (Qwen3-32B, $r$=0.156, $p$=4.6e-12) fails to replicate on a second model (LLaMA-3.3-70B, $r$=0.05, $p$=0.08), indicating model-specificity rather than a general phenomenon.\nartifacts/dream_reports/dream_20260515T053106/worst/paper.tex:57:\\item We report a rigorous \\textbf{negative result on embedding SCS as a confusability proxy}: SCS achieves AUC=0.56 for predicting actual type confusion (near random), and confusability-aware decomposition provides no benefit over random batching.\nartifacts/dream_reports/dream_20260515T053106/worst/paper.tex:95:\\paragraph{Schema Confusability Score (SCS).}\nartifacts/dream_reports/dream_20260515T053106/worst/paper.tex:97:The Batch Confusability Score (BCS) of a type set $T$ is the mean pairwise SCS:\nartifacts/dream_reports/dream_20260515T053106/worst/paper.tex:99:\\text{BCS}(T) = \\frac{2}{|T|(|T|-1)} \\sum_{i&lt;j} \\text{SCS}(t_i, t_j)\nartifacts/dream_reports/dream_20260515T053106/worst/paper.tex:111:\\textbf{Factorial analysis}: 2$\\times$2 design crossing \\{low count, high count\\} $\\times$ \\{low BCS, high BCS\\} to test for main effects and interaction.\nartifacts/dream_reports/dream_20260515T053106/worst/paper.tex:113:\\textbf{Pairwise analysis}: Correlate pairwise SCS with pairwise empirical confusion counts. Immune to batch-level frequency confounds.\nartifacts/dream_reports/dream_20260515T053106/worst/paper.tex:198:We conduct a 2$\\times$2 factorial experiment crossing type count (low/high) with BCS (low/high) on Few-NERD (Table~\\ref{tab:factorial}).\nartifacts/dream_reports/dream_20260515T053106/worst/paper.tex:205:         & Low BCS & High BCS & $\\Delta$(BCS) \\\\\nartifacts/dream_reports/dream_20260515T053106/worst/paper.tex:213:\\caption{2$\\times$2 factorial F1 results on Few-NERD (Qwen3-32B). BCS has negligible effect ($\\Delta$=0.01) compared to count ($\\Delta$=0.03).}\nartifacts/dream_reports/dream_20260515T053106/worst/paper.tex:218:The count main effect is marginally significant ($\\eta^2$=0.08, $p$=0.04), but the BCS main effect is not significant ($\\eta^2$=0.01, $p$=0.42).\nartifacts/dream_reports/dream_20260515T053106/worst/paper.tex:229:BCS       & 0.0022 & 1 & 0.52 & 0.420 & 0.010 \\\\\nartifacts/dream_reports/dream_20260515T053106/worst/paper.tex:230:Count$\\times$BCS & 0.0002 & 1 & 0.05 & 0.880 & 0.001 \\\\\nartifacts/dream_reports/dream_20260515T053106/worst/paper.tex:234:\\caption{Two-way ANOVA. BCS main effect is not significant after controlling for count. The interaction is zero, indicating confusability is not an independent factor.}\nartifacts/dream_reports/dream_20260515T053106/worst/paper.tex:238:\\subsection{Within-Count BCS Correlation on MAVEN}\nartifacts/dream_reports/dream_20260515T053106/worst/paper.tex:240:On MAVEN, within-count BCS--F1 correlations are uniformly non-significant (Table~\\ref{tab:maven_bcs}).\nartifacts/dream_reports/dream_20260515T053106/worst/paper.tex:248:Count & $r$(F1,BCS) & $p$ & $n$ & Verdict \\\\\nartifacts/dream_reports/dream_20260515T053106/worst/paper.tex:255:\\caption{MAVEN within-count BCS--F1 correlation. No evidence for confusability independence on event detection.}\nartifacts/dream_reports/dream_20260515T053106/worst/paper.tex:259:\\subsection{Pairwise BCS--Confusion Analysis}\nartifacts/dream_reports/dream_20260515T053106/worst/paper.tex:276:\\caption{Pairwise BCS--confusion correlations. The Few-NERD/Qwen3 result ($r$=0.156) does not replicate across models or tasks. $\\rho_{\\text{nz}}$: Spearman $\\rho$ on nonzero confusion pairs.}\nartifacts/dream_reports/dream_20260515T053106/worst/paper.tex:285:If confusability drives a distinct error channel (type substitution), we should observe more type substitution errors in high-BCS conditions after controlling for frequency.\nartifacts/dream_reports/dream_20260515T053106/worst/paper.tex:286:Table~\\ref{tab:errors} shows the error taxonomy across BCS bins with frequency controlled.\nartifacts/dream_reports/dream_20260515T053106/worst/paper.tex:293:Error Type & High BCS & Low BCS & Ratio & $\\chi^2$ $p$ \\\\\nartifacts/dream_reports/dream_20260515T053106/worst/paper.tex:301:\\caption{Error taxonomy by BCS bin (Few-NERD, frequency-controlled). No significant difference in type substitution between high- and low-BCS conditions.}\nartifacts/dream_reports/dream_20260515T053106/worst/paper.tex:305:None of the error type proportions differ significantly between BCS bins.\nartifacts/dream_reports/dream_20260515T053106/worst/paper.tex:311:We directly evaluate embedding SCS as a proxy for empirical LLM confusion (Table~\\ref{tab:scs_validation}).\nartifacts/dream_reports/dream_20260515T053106/worst/paper.tex:320:Spearman $\\rho$ (SCS vs.\\ empirical confusion) & 0.12 ($p$=0.03) \\\\\nartifacts/dream_reports/dream_20260515T053106/worst/paper.tex:326:\\caption{SCS vs.\\ empirical confusion. Despite weak statistical significance ($p$<0.05 due to large $n$), practical predictive value is near-random (AUC=0.56).}\nartifacts/dream_reports/dream_20260515T053106/worst/paper.tex:338:Rank & Top Empirical Confusion Pair & In Top-10 SCS? \\\\\nartifacts/dream_reports/dream_20260515T053106/worst/paper.tex:352:\\caption{Top-10 empirically confused type pairs. Only 2/10 overlap with top-10 SCS pairs. Confusion is driven by ``-other'' label ambiguity, not embedding similarity.}\nartifacts/dream_reports/dream_20260515T053106/worst/paper.tex:439:High-frequency types in Few-NERD tend to be fine-grained subtypes within the same coarse category (e.g., multiple \\texttt{person-*} types), which naturally have high pairwise SCS.\nartifacts/dream_reports/dream_20260515T053106/worst/paper.tex:441:The result is a spurious positive correlation between BCS and batch F1---the opposite of the confusability hypothesis prediction.\nartifacts/dream_reports/dream_20260515T053106/worst/paper.tex:444:\\paragraph{Why embedding SCS fails as a confusability proxy.}\nartifacts/dream_reports/dream_20260515T053106/worst/paper.tex:445:SCS captures semantic proximity in label embedding space, but LLM type confusion is driven by different mechanisms:\nartifacts/dream_reports/dream_20260515T053106/worst/paper.tex:464:First, our SCS measure uses a single sentence embedding model (all-MiniLM-L6-v2); alternative embeddings (e.g., from the target LLM itself) might yield better confusability proxies.\nartifacts/dream_reports/dream_20260515T053106/worst/paper.tex:487:Pairwise BCS--confusion correlation is not significant ($r$=0.02, $p$=0.35).\nartifacts/dream_reports/dream_20260515T053106/worst/paper.tex:489:The confusion ratio between extreme BCS batches is 1.1$\\times$, indicating no confusability effect.\nartifacts/dream_reports/dream_20260515T053106/median/paper.tex:45:To test this hypothesis, we design controlled experiments that isolate confusability from count. We construct type batches of fixed size but varying confusability, measured by Schema Confusability Score (SCS)---the cosine similarity between type name embeddings. We validate across two IE tasks (NER on Few-NERD, Event Detection on MAVEN), two model families (Qwen3-32B, LLaMA-3.3-70B), and multiple analysis granularities (batch-level, per-type, and pairwise).\nartifacts/dream_reports/dream_20260515T053106/median/paper.tex:78:\\subsection{Schema Confusability Score (SCS)}\nartifacts/dream_reports/dream_20260515T053106/median/paper.tex:82:    \\text{SCS}(t_i, t_j) = \\cos\\bigl(\\mathbf{e}(t_i),\\; \\mathbf{e}(t_j)\\bigr)\nartifacts/dream_reports/dream_20260515T053106/median/paper.tex:86:    \\text{BCS}(B) = \\max_{t_i, t_j \\in B,\\; i \\neq j} \\text{SCS}(t_i, t_j)\nartifacts/dream_reports/dream_20260515T053106/median/paper.tex:89:We validate SCS as a proxy for empirical confusion using calibration data (\\S\\ref{sec:scs_validation}). The overall rank correlation between SCS and empirical confusion frequency is $\\rho=0.38$ ($p<10^{-5}$), confirming SCS is a useful but imperfect proxy.\nartifacts/dream_reports/dream_20260515T053106/median/paper.tex:93:To isolate confusability from count, we construct type batches with a $\\text{count} \\times \\text{BCS}$ factorial design. For each count level $c \\in \\{1, 6, 12, 22, \\ldots\\}$, we create batches of size $c$ from $\\mathcal{T}$. Within each count level, we vary BCS by selecting either semantically distant types (low BCS) or semantically similar types (high BCS).\nartifacts/dream_reports/dream_20260515T053106/median/paper.tex:101:    \\item \\textbf{Graph construction}: Build a confusability graph $G = (\\mathcal{T}, E)$ where $(t_i, t_j) \\in E$ iff $\\text{SCS}(t_i, t_j) > \\tau$ (threshold $\\tau$).\nartifacts/dream_reports/dream_20260515T053106/median/paper.tex:103:    \\item \\textbf{Batch assignment}: Types with the same color form a batch. Each batch $B_i$ satisfies $\\max_{t_a, t_b \\in B_i} \\text{SCS}(t_a, t_b) \\leq \\tau$.\nartifacts/dream_reports/dream_20260515T053106/median/paper.tex:109:    \\item \\textbf{SDGD-zero}: Uses embedding-based SCS with no calibration data.\nartifacts/dream_reports/dream_20260515T053106/median/paper.tex:110:    \\item \\textbf{SDGD-cal}: Replaces SCS with an empirical confusion matrix estimated from a small calibration set (5--10 examples).\nartifacts/dream_reports/dream_20260515T053106/median/paper.tex:158:\\subsection{Pairwise BCS--Confusion Analysis}\nartifacts/dream_reports/dream_20260515T053106/median/paper.tex:160:To isolate confusability from count, we analyze at the type-pair level. For each pair $(t_i, t_j)$, we compute SCS and count how often $t_i$ predictions appear in $t_j$ gold spans (and vice versa). This analysis is immune to the type frequency confound that afflicts batch-level analysis.\nartifacts/dream_reports/dream_20260515T053106/median/paper.tex:167:\\caption{Pairwise BCS--confusion correlations. The confusability--confusion relationship holds across datasets, tasks, and models.}\nartifacts/dream_reports/dream_20260515T053106/median/paper.tex:184:The most confused type pairs confirm the mechanistic link. On Few-NERD, the top pair is \\emph{person-other} $\\leftrightarrow$ \\emph{person-politician} (SCS$=0.934$). On MAVEN, top pairs are FrameNet siblings: \\emph{Giving} $\\leftrightarrow$ \\emph{Sending} (SCS$=0.784$), \\emph{Attack} $\\leftrightarrow$ \\emph{Hostile\\_encounter} (SCS$=0.761$).\nartifacts/dream_reports/dream_20260515T053106/median/paper.tex:188:We construct extreme batches: the top-$k$ highest-SCS types vs.\\ bottom-$k$ (at fixed count). On MAVEN, high-BCS batches produce $3.2\\times$ the type confusion rate of low-BCS batches at count$=14$, and $2.8\\times$ at count$=28$ (Table~\\ref{tab:confusion_ratio}).\nartifacts/dream_reports/dream_20260515T053106/median/paper.tex:193:\\caption{Confusion rate ratio between extreme high-BCS and low-BCS batches on MAVEN.}\nartifacts/dream_reports/dream_20260515T053106/median/paper.tex:197:Count & High-BCS Rate & Low-BCS Rate & Ratio \\\\\nartifacts/dream_reports/dream_20260515T053106/median/paper.tex:207:[Omitted long matching line]\nartifacts/dream_reports/dream_20260515T053106/median/paper.tex:212:\\caption{Cross-model comparison of pairwise BCS--confusion analysis on Few-NERD. Direction is consistent; effect size varies.}\nartifacts/dream_reports/dream_20260515T053106/median/paper.tex:231:Batch-level analysis (F1 vs.\\ BCS within fixed count) yields a \\emph{positive} correlation ($r=0.19$, $p=0.24$ on MAVEN)---opposite to the naive prediction. This is a frequency confound: high-frequency types tend to have both high BCS (more semantic neighbors) and high F1 (more training signal in pretraining). The progression from batch-level to pairwise analysis---which is immune to this confound---demonstrates the importance of appropriate analysis granularity.\nartifacts/dream_reports/dream_20260515T053106/median/paper.tex:240:We test the additivity of count and confusability using a $\\{\\text{count}=6, \\text{count}=22\\} \\times \\{\\text{low BCS}, \\text{high BCS}\\}$ factorial design on Few-NERD (Table~\\ref{tab:factorial}).\nartifacts/dream_reports/dream_20260515T053106/median/paper.tex:249: & Low BCS & High BCS & BCS Effect \\\\\nartifacts/dream_reports/dream_20260515T053106/median/paper.tex:259:Two-way ANOVA (Table~\\ref{tab:anova}) reveals significant main effects for both count ($F=8.2$, $p=0.006$, $\\eta^2=0.12$) and BCS ($F=5.1$, $p=0.028$, $\\eta^2=0.08$), but no significant interaction ($F=2.3$, $p=0.135$, $\\eta^2=0.04$). The additive prediction for the high-count/high-BCS cell (0.250) closely matches the observed value (0.245), with a residual of only $-0.005$.\nartifacts/dream_reports/dream_20260515T053106/median/paper.tex:264:\\caption{Two-way ANOVA results. Count and BCS are independently significant; their interaction is not, supporting the additive multi-channel model.}\nartifacts/dream_reports/dream_20260515T053106/median/paper.tex:271:BCS (main) & 5.1 & .028 & .08 & Significant \\\\\nartifacts/dream_reports/dream_20260515T053106/median/paper.tex:272:Count $\\times$ BCS & 2.3 & .135 & .04 & Not sig. \\\\\nartifacts/dream_reports/dream_20260515T053106/median/paper.tex:277:Channel decomposition is clear: count primarily affects recall ($\\Delta=-0.160$), while BCS primarily affects precision ($\\Delta=-0.081$). However, confusability also has a secondary recall effect ($\\Delta=-0.043$), suggesting that when the model is uncertain between confusable types, it sometimes chooses to output nothing.\nartifacts/dream_reports/dream_20260515T053106/median/paper.tex:279:\\subsection{Error Taxonomy by BCS Bin}\nartifacts/dream_reports/dream_20260515T053106/median/paper.tex:281:We classify all false positives and false negatives into four error categories and stratify by BCS bin (Table~\\ref{tab:error_taxonomy}).\nartifacts/dream_reports/dream_20260515T053106/median/paper.tex:286:\\caption{Error distribution by BCS bin on Few-NERD. Type substitution increases monotonically with BCS ($\\chi^2$ $p=0.001$); false negatives decrease.}\nartifacts/dream_reports/dream_20260515T053106/median/paper.tex:290:BCS Bin & TypeSub & Boundary & FalseNeg & Halluc. \\\\\nartifacts/dream_reports/dream_20260515T053106/median/paper.tex:300:Type substitution errors increase monotonically from 18\\% (low BCS) to 52\\% (high BCS), while false negatives decrease from 55\\% to 28\\%. This directly confirms the multi-channel model: confusability drives type confusion (Channel~2) while count/attention dilution drives entity omission (Channel~1). The association between type substitution rate and BCS bin is statistically significant ($\\chi^2=18.4$, $p=0.001$).\nartifacts/dream_reports/dream_20260515T053106/median/paper.tex:302:Boundary errors remain approximately flat across BCS bins (11--15\\%), confirming they are driven by surface-form ambiguity rather than type confusability. Hallucination rates show a slight decrease (12\\% to 7\\%) that is not monotonic and not significant ($p=0.18$). We characterize these as the \\emph{dominant error modes shifting} with confusability, rather than exclusive channels.\nartifacts/dream_reports/dream_20260515T053106/median/paper.tex:381:On MAVEN, the SDGD-specific contribution ($+2.0$ over random) is significant ($p=0.018$) and equals the batch-reduction contribution ($+2.0$ from single to random). SDGD reduces mean within-batch BCS by 38--41\\% compared to random batching (0.145 vs.\\ 0.235 on MAVEN).\nartifacts/dream_reports/dream_20260515T053106/median/paper.tex:383:On Few-NERD, the SDGD-specific contribution ($+1.4$) is marginal ($p=0.08$), consistent with fewer high-SCS pairs in a 66-type schema.\nartifacts/dream_reports/dream_20260515T053106/median/paper.tex:391:SDGD-cal replaces embedding SCS with an empirical confusion matrix estimated from 8 calibration examples. On MAVEN, this yields $+1.7$ F1 over SDGD-zero ($p=0.045$), discovering 128 empirical confusion pairs with only 48\\% overlap with SCS top-100 predictions (Table~\\ref{tab:sdgd_cal}).\nartifacts/dream_reports/dream_20260515T053106/median/paper.tex:396:\\caption{SDGD-cal vs.\\ SDGD-zero. Calibration provides larger gains on MAVEN where SCS is less accurate ($\\rho=0.34$ vs.\\ $0.42$ on Few-NERD).}\nartifacts/dream_reports/dream_20260515T053106/median/paper.tex:415:The gain is larger on MAVEN because SCS is a weaker proxy for FrameNet event types ($\\rho=0.34$) than for NER types ($\\rho=0.42$): frame-semantic distinctions (e.g., \\emph{Giving} vs.\\ \\emph{Commerce\\_sell}) are poorly captured by name embeddings.\nartifacts/dream_reports/dream_20260515T053106/median/paper.tex:418:\\section{SCS Validation}\nartifacts/dream_reports/dream_20260515T053106/median/paper.tex:422:We validate the SCS proxy by comparing embedding-based similarities against empirical confusion matrices from calibration runs (Table~\\ref{tab:scs_valid}).\nartifacts/dream_reports/dream_20260515T053106/median/paper.tex:427:\\caption{SCS validation: embedding similarity vs.\\ empirical confusion. SCS is a moderate proxy ($\\rho=0.38$), stronger on Few-NERD than MAVEN.}\nartifacts/dream_reports/dream_20260515T053106/median/paper.tex:441:SCS overestimates confusability for type pairs with distinctive lexical cues (e.g., \\emph{org-religion} $\\leftrightarrow$ \\emph{org-political}, SCS$=0.72$ but 0 empirical confusion---entity mentions like ``Church of X'' vs.\\ ``X Party'' are easily distinguished). SCS underestimates confusion for pairs sharing entity surface forms (e.g., \\emph{art-film} $\\leftrightarrow$ \\emph{art-broadcastprogram}, SCS$=0.38$ but 12 confusions---titles like ``Breaking Bad'' can be either).\nartifacts/dream_reports/dream_20260515T053106/median/paper.tex:443:These failure modes explain why SDGD-cal improves over SDGD-zero: calibration corrects both false positives (35 overestimates) and false negatives (28 underestimates) in the SCS ranking.\nartifacts/dream_reports/dream_20260515T053106/median/paper.tex:458:The pairwise BCS--confusion correlation varies from $r=0.156$ (Few-NERD, Qwen3-32B) to $r=0.09$ (MAVEN; LLaMA-3.3-70B). This reflects two factors: (1) larger schemas dilute per-pair confusion rates, reducing correlation magnitude, and (2) different models' internal representations align differently with static embedding SCS. The consistent \\emph{direction} across all conditions---positive correlation, same top confused pairs---is more informative than the varying magnitude.\nartifacts/dream_reports/dream_20260515T053106/median/paper.tex:469:(3) SCS as a confusability proxy has moderate accuracy ($\\rho=0.38$); better confusability measures (e.g., LLM-internal representations) could improve SDGD.",
    "numLines": 500
  }
}
```

</details>

---

### Assistant

_source line 16_

<details><summary>Logged reasoning block</summary>

```text
Let me read the full output files to understand the complete picture, and also check for macro definitions in main.tex.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "67ef2cbc-2912-4b7f-9b41-7bfb53ab1364",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Dycb4Fi8BwYEUxx61EyfV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2002,
      "cache_read_input_tokens": 24999,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2002
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 17_

Let me check for macro definitions and get a clearer picture of the formatting patterns in the main paper files (docs/paper/).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "d569b3df-6ea9-406d-b5e4-1931e11a15a7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Dycb4Fi8BwYEUxx61EyfV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2002,
      "cache_read_input_tokens": 24999,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2002
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Grep · `toolu_014UFYyFVa29F2MPCXv1yyG1`</summary>

```json
{
  "pattern": "\\\\newcommand.*[Bb][Cc][Ss]|\\\\newcommand.*[Ss][Cc][Ss]|\\\\def.*[Bb][Cc][Ss]|\\\\def.*[Ss][Cc][Ss]",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "829751bc-0f95-4064-b7fe-420029b06297",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Dycb4Fi8BwYEUxx61EyfV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2002,
      "cache_read_input_tokens": 24999,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2002
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-22T11:09:44.015Z_

<details><summary>↩ Tool result · `toolu_014UFYyFVa29F2MPCXv1yyG1`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "540fae1a-c249-4cf4-bb0b-1e45b51a8ecb",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Read · `toolu_01TVUxQccTnAjno2RuBAmMrt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "limit": 60
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "bcf25ff6-ddee-4166-8d62-a907be30cad5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Dycb4Fi8BwYEUxx61EyfV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2002,
      "cache_read_input_tokens": 24999,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2002
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-22T11:09:44.670Z_

<details><summary>↩ Tool result · `toolu_01TVUxQccTnAjno2RuBAmMrt`</summary>

```text
1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	\usepackage{enumitem}
14	\usepackage[normalem]{ulem}
15	\usepackage{listings}
16	
17	\title{How Does Schema Complexity Predict Performance\\in Training-Free LLM Information Extraction?}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\input{abstract}
25	
26	\input{introduction}
27	
28	\input{related_work}
29	
30	\input{experimental_setup}
31	
32	\input{results}
33	
34	\input{sdgd_negative}
35	
36	\input{discussion}
37	
38	\section*{Limitations}
39	
40	Our findings are subject to three main limitations.
41	\textbf{(1)~Model and statistical scope.}
42	Primary experiments use Qwen3-32B; cross-model validation (LLaMA-8B/70B, Gemini Flash) covers Dimensions~1--2 but not secondary analyses such as TOST factorial interaction (\S\ref{sec:multi_channel}) or SDGD failure analysis (\S\ref{sec:sdgd}), and proprietary-model generalization remains open.
43	TOST dimensional separability holds on the probability scale but logit-scale evidence is inconclusive, reflecting the inflated variance of logit-transformed proportions in the 0.37--0.86 accuracy range rather than a qualitative divergence from the linear-scale finding; the interaction point estimate (0.47\,pp) falls within the $\pm 3$\,pp equivalence margin.
44	BCS-controlled experiments use greedy decoding with a single seed; residual SD${}\,=\,0.88$\,pp is 18--44\% of the observed effect size (Appendix~\ref{app:variance-decomposition}), so detection is robust but point estimates carry meaningful uncertainty.
45	All evidence is correlational with controlled stratification; mechanistic confirmation at the attention or logit level remains future work.
46	%
47	\textbf{(2)~DocRED VIF confounding.}
48	DocRED exhibits severe multicollinearity (VIF${}\,=\,50.9$), preventing reliable BCS effect quantification; semipartial $R^2{}\,=\,5.6\%$ serves only as directional evidence, and the count${}\times{}$BCS interaction is partially confounded by BCS range restriction at higher counts (Appendix~\ref{sec:appendix_factorial}).
49	%
50	\textbf{(3)~Experimental scope.}
51	Evaluations cover four English-language Wikipedia/Wikidata-derived datasets in a training-free zero-shot setting; few-shot, fine-tuned, domain-specific (e.g., biomedical, legal), and non-English scenarios remain untested.
52	BCS batch-level prediction is significant in RE but not detected in NER, where errors scatter across miss, boundary, and type modes (Appendix~\ref{app:relaxed-matching}).
53	Batches share prompt template and LLM but type composition is independently sampled; cross-dataset consistency is treated as converging evidence rather than independent replication \citep{rothman-1990}, and core claims are robust to Bonferroni correction (all $p < 0.001$) \citep{dror-2018-significance}.
54	
55	% \input{checklist}  % EMNLP 2026: checklist goes in OpenReview form, not PDF
56	
57	\bibliography{references}
58	
59	\appendix
60	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "3f7fcf5c-054b-4b84-954b-330d8edede52",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{enumitem}\n\\usepackage[normalem]{ulem}\n\\usepackage{listings}\n\n\\title{How Does Schema Complexity Predict Performance\\\\in Training-Free LLM Information Extraction?}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{experimental_setup}\n\n\\input{results}\n\n\\input{sdgd_negative}\n\n\\input{discussion}\n\n\\section*{Limitations}\n\nOur findings are subject to three main limitations.\n\\textbf{(1)~Model and statistical scope.}\nPrimary experiments use Qwen3-32B; cross-model validation (LLaMA-8B/70B, Gemini Flash) covers Dimensions~1--2 but not secondary analyses such as TOST factorial interaction (\\S\\ref{sec:multi_channel}) or SDGD failure analysis (\\S\\ref{sec:sdgd}), and proprietary-model generalization remains open.\nTOST dimensional separability holds on the probability scale but logit-scale evidence is inconclusive, reflecting the inflated variance of logit-transformed proportions in the 0.37--0.86 accuracy range rather than a qualitative divergence from the linear-scale finding; the interaction point estimate (0.47\\,pp) falls within the $\\pm 3$\\,pp equivalence margin.\nBCS-controlled experiments use greedy decoding with a single seed; residual SD${}\\,=\\,0.88$\\,pp is 18--44\\% of the observed effect size (Appendix~\\ref{app:variance-decomposition}), so detection is robust but point estimates carry meaningful uncertainty.\nAll evidence is correlational with controlled stratification; mechanistic confirmation at the attention or logit level remains future work.\n%\n\\textbf{(2)~DocRED VIF confounding.}\nDocRED exhibits severe multicollinearity (VIF${}\\,=\\,50.9$), preventing reliable BCS effect quantification; semipartial $R^2{}\\,=\\,5.6\\%$ serves only as directional evidence, and the count${}\\times{}$BCS interaction is partially confounded by BCS range restriction at higher counts (Appendix~\\ref{sec:appendix_factorial}).\n%\n\\textbf{(3)~Experimental scope.}\nEvaluations cover four English-language Wikipedia/Wikidata-derived datasets in a training-free zero-shot setting; few-shot, fine-tuned, domain-specific (e.g., biomedical, legal), and non-English scenarios remain untested.\nBCS batch-level prediction is significant in RE but not detected in NER, where errors scatter across miss, boundary, and type modes (Appendix~\\ref{app:relaxed-matching}).\nBatches share prompt template and LLM but type composition is independently sampled; cross-dataset consistency is treated as converging evidence rather than independent replication \\citep{rothman-1990}, and core claims are robust to Bonferroni correction (all $p < 0.001$) \\citep{dror-2018-significance}.\n\n% \\input{checklist}  % EMNLP 2026: checklist goes in OpenReview form, not PDF\n\n\\bibliography{references}\n\n\\appendix\n",
      "numLines": 60,
      "startLine": 1,
      "totalLines": 919
    }
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Read · `toolu_01XWdKth4t5vCHGkrm7KGZBg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": 60
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "bc04b196-248d-44dc-ae5b-8aefd1d42ccb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014mYwBp3osXbM34bAif3qwU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1457,
      "cache_read_input_tokens": 27001,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1457
      },
      "output_tokens": 35,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-22T11:09:48.997Z_

<details><summary>↩ Tool result · reported error · `toolu_01XWdKth4t5vCHGkrm7KGZBg`</summary>

```text
File content (25612 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "bdb5ae6e-958b-4e1f-a225-9039f40e8470",
  "tool_use_result": "Error: File content (25612 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Read · `toolu_01CwPLiECYM3H1As42pMDYvG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": 60,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "44d03ea5-ebe9-42a4-9f0c-fef17defa629",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LX6bhC6BKHnQkFQGftFh1u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 269,
      "cache_read_input_tokens": 28458,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 269
      },
      "output_tokens": 65,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-22T11:09:51.447Z_

<details><summary>↩ Tool result · `toolu_01CwPLiECYM3H1As42pMDYvG`</summary>

```text
60	
61	\section{Additional Figures}
62	\label{sec:appendix_figures}
63	
64	\begin{table}[h]
65	\centering
66	\small
67	\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\S\ref{sec:model}) for fair cross-model comparison; the count-curve results in \S\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\ 0.64 at count${}\,=\,1$) due to over-prediction under v1.}
68	\label{tab:cross_model}
69	\begin{tabular}{lrr}
70	\toprule
71	\textbf{Count} & \textbf{Llama-3.1-8B} & \textbf{Qwen3-32B} \\
72	\midrule
73	1 & 0.702 & 0.640 \\
74	64 & 0.273 & 0.304 \\
75	\midrule
76	Decline & $-$43\,pp & $-$34\,pp \\
77	\bottomrule
78	\end{tabular}
79	\end{table}
80	
81	\begin{table}[h]
82	\centering
83	\small
84	\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\approx$51\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\Delta$, in pp) is 77--87\% as large on Llama-3.1-8B as on Qwen3-32B.}
85	\label{tab:cross_model_bcs}
86	\resizebox{\columnwidth}{!}{%
87	\begin{tabular}{crrrrrr}
88	\toprule
89	& \multicolumn{3}{c}{\textbf{Llama-3.1-8B}} & \multicolumn{3}{c}{\textbf{Qwen3-32B}} \\
90	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
91	\textbf{Count} & \textbf{Low} & \textbf{High} & \textbf{$\Delta$} & \textbf{Low} & \textbf{High} & \textbf{$\Delta$} \\
92	\midrule
93	8 & 78.1\% & 51.0\% & $-$27.1 & 82.3\% & 51.0\% & $-$31.2 \\
94	16 & 75.5\% & 51.6\% & $-$23.9 & 82.8\% & 51.6\% & $-$31.2 \\
95	\bottomrule
96	\end{tabular}}
97	\end{table}
98	
99	\begin{table}[h]
100	\centering
101	\small
102	\caption{NER batch-level BCS--F1 correlation across models. $^\dagger$Partial correlation controlling for type frequency. $^\ddagger$LLaMA-70B count\_12 shows $r{=}{-}0.42$ ($p{=}0.034$, uncorrected; Bonferroni $p{=}0.069$); pooled and count\_6 are null, consistent with sampling noise at $n{=}25$. The null is observed on three models; Gemini remains untested.}
103	\label{tab:cross_model_ner_null}
104	\begin{tabular}{lcl}
105	\toprule
106	\textbf{Model} & \textbf{NER BCS--F1 $r$} & \textbf{Status} \\
107	\midrule
108	Qwen3-32B & $0.004$ ($p = 0.94$) & Null \\
109	LLaMA-3.1-8B & $-0.12$ ($p = 0.29$)\rlap{$^\dagger$} & Null \\
110	LLaMA-3.1-70B & $-0.13$ ($p = 0.36$)\rlap{$^\ddagger$} & Null \\
111	Gemini 2.5 Flash & --- & Not tested \\
112	\bottomrule
113	\end{tabular}
114	\end{table}
115	
116	\begin{table}[h]
117	\centering
118	\small
119	\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin. Spearman $\rho$ computed over $n=148$ batches (NER), $n=154$ (RE), and $n=110$ (DocRE). IntraSub scales monotonically with BCS across all three datasets. DocRE missed rates decrease with BCS, indicating high-confusability errors shift from omission to substitution.}
120	\label{tab:error_taxonomy}
121	\resizebox{\columnwidth}{!}{%
122	\begin{tabular}{llrrrrrrr}
123	\toprule
124	 & & \multicolumn{5}{c}{\textbf{BCS Bin}} & & \\
125	\cmidrule(lr){3-7}
126	\textbf{Task} & \textbf{Error} & \textbf{Solo} & \textbf{Low} & \textbf{Mid} & \textbf{High} & \textbf{V.High} & \textbf{$\rho$} & \textbf{$p$} \\
127	\midrule
128	NER & IntraSub & 0\% & 1.6\% & 10.6\% & 49.4\% & --- & 1.000 & ${<}0.001$ \\
129	RE  & IntraSub & 0\% & 4.2\% & 13.0\% & 20.3\% & 32.3\% & 0.954 & ${<}\,0.001$ \\
130	DocRE & IntraSub & --- & 4.8\% & 22.4\% & 37.0\% & 41.9\% & 0.843 & ${<}\,0.001$ \\
131	\midrule
132	NER & Missed & --- & 42.8\% & 64.8\% & 49.9\% & --- & --- & --- \\
133	RE  & Missed & --- & 10.4\% & 11.3\% & 13.1\% & 15.7\% & --- & --- \\
134	DocRE & Missed & --- & 28.1\% & 22.6\% & 21.6\% & 16.2\% & --- & --- \\
135	\bottomrule
136	\end{tabular}}
137	\end{table}
138	
139	\begin{table}[t]
140	\centering
141	\small
142	\caption{Cross-model replication of IntraSub--BCS Spearman correlation on FewRel RE. $^\dagger$LLaMA-70B has only 20 batches with 17.4\% missed rate; the null is attributable to insufficient power rather than absence of the effect.}
143	\label{tab:cross_model_error_taxonomy}
144	\begin{tabular}{lrcc}
145	\toprule
146	\textbf{Model} & $n$ & $\rho$ & $p$ \\
147	\midrule
148	Qwen3-32B & 154 & 0.954 & ${<}\,0.001$ \\
149	Gemini 2.5 Flash & 60 & 0.821 & ${<}\,0.001$ \\
150	LLaMA-3.1-8B & 54 & 0.430 & 0.001 \\
151	LLaMA-3.1-70B$^\dagger$ & 20 & $-$0.086 & 0.719 \\
152	\bottomrule
153	\end{tabular}
154	\end{table}
155	
156	\section{SDGD Full Protocol and Results}
157	\label{sec:appendix_sdgd}
158	
159	We construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\text{SCS}(t_i, t_j) > \tau$. Greedy graph coloring (\textsc{largest\_first}) assigns each type to a color such that no two adjacent (i.e., highly confusable) types share a color. Each color class forms one extraction batch, and predictions are merged via set union.
160	
161	\begin{enumerate}[leftmargin=*,itemsep=2pt]
162	\item Compute pairwise SCS matrix $S_{ij} = \cos(\text{embed}(t_i), \text{embed}(t_j))$.
163	\item Construct graph $G$: add edge $(t_i, t_j)$ iff $S_{ij} > \tau$.
164	\item Apply greedy graph coloring (\textsc{largest\_first}) to assign each type a color $c(t)$.
165	\item For each color $k$, form batch $B_k = \{t : c(t) = k\}$ and run extraction on all test instances.
166	\item Merge: union of per-batch predictions (v1) or confidence-gated selection (v2).
167	\end{enumerate}
168	Oracle routing (Table~\ref{tab:routing_strategies}) recovers substantial accuracy (72.4\% vs.\ 50.4\% single-pass), confirming the sub-schemas contain correct predictions; the failure lies in routing, not decomposition quality.
169	
170	We compare four modes: (i)~\textbf{single\_pass}, the undecomposed baseline; (ii)~\textbf{sdgd\_zero}, SCS-guided partitioning; (iii)~\textbf{random\_batch}, random partitioning with matched batch sizes; and (iv)~\textbf{per\_type}, the extreme case where each type is extracted in isolation.
171	
172	Single-pass extraction achieves F1\,=\,0.445 (P\,=\,0.563, R\,=\,0.368). SDGD obtains F1\,=\,0.251 (P\,=\,0.210, R\,=\,0.314), a 44\% relative drop. Random batching reaches F1\,=\,0.320 (P\,=\,0.249, R\,=\,0.446), and per-type extraction yields F1\,=\,0.292 (P\,=\,0.194, R\,=\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\ref{tab:sdgd_results}).
173	
174	\begin{table}[h]
175	\centering
176	\small
177	\caption{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \texttt{min\_batch\_size=8} (reducing 8$\to$4 batches for sdgd\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt.}
178	\label{tab:sdgd_results}
179	\resizebox{\columnwidth}{!}{%
180	\begin{tabular}{lrccc}
181	\toprule
182	\textbf{Mode} & \textbf{\# Batches} & \textbf{Precision} & \textbf{Recall} & \textbf{F1} \\
183	\midrule
184	single\_pass & 1 & 0.563 & 0.368 & 0.445 \\
185	\midrule
186	sdgd\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\
187	random\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\
188	per\_type & 66 & 0.194 & 0.586 & 0.292 \\
189	\midrule
190	sdgd\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\
191	random\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\
192	\bottomrule
193	\end{tabular}}
194	\end{table}
195	
196	Decomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions. Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions and inflates false positives.
197	
198	Our v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\_zero: 0.210$\to$0.324; random\_batch: 0.249$\to$0.331), but at the cost of disproportionate recall loss (0.314$\to$0.191; 0.446$\to$0.276), and both modes produce lower F1 (sdgd\_zero: 0.251$\to$0.241; random\_batch: 0.320$\to$0.301).
199	
200	\subsection{Practical Routing Strategies on RE}
201	\label{sec:appendix_routing}
202	
203	We evaluate five non-oracle routing strategies on FewRel 80-relation RE using graph-coloring sub-schema decomposition (same grouping as Table~\ref{tab:batch_composition}). Each strategy selects a single sub-schema for each test instance and returns that sub-schema's prediction.
204	
205	\begin{table}[h]
206	\centering
207	\small
208	\caption{Routing strategy comparison on FewRel 80-relation RE with graph-coloring sub-schema decomposition. Oracle requires gold labels. All practical (non-oracle) strategies perform below the single-pass baseline. The failure stems from constrained decoding (enum constraint), which forces confident predictions in every sub-schema: 73.4\% of instances receive positive predictions from 3--5 sub-schemas simultaneously, with per-sub-schema none-rates of only 20--40\%.}
209	\label{tab:routing_strategies}
210	\resizebox{\columnwidth}{!}{\begin{tabular}{@{}lrr@{}}
211	\toprule
212	\textbf{Strategy} & \textbf{Accuracy} & \textbf{$\Delta$ vs.\ Single-Pass} \\
213	\midrule
214	Oracle (gold label) & 72.4\% & +22.0\,pp \\
215	\midrule
216	Max-conf (positive only) & 36.5\% & $-$14.0\,pp \\
217	None-aware & 36.5\% & $-$14.0\,pp \\
218	Margin (positive only) & 35.9\% & $-$14.5\,pp \\
219	Max-conf (all) & 27.7\% & $-$22.7\,pp \\
220	Random & 14.7\% & $-$35.7\,pp \\
221	\midrule
222	Single-pass (no decomposition) & 50.4\% & --- \\
223	\bottomrule
224	\end{tabular}}
225	\end{table}
226	
227	\section{Factorial Analysis and Separability Test}
228	\label{sec:appendix_factorial}
229	
230	To formally test whether count and confusability effects are additive, we fit a multiple regression (accuracy $\sim$ $\log_2$\,count $+$ BCS $+$ count$\times$BCS) across 69 batches from FewRel spanning five count levels ($k \in \{4, 8, 16, 32, 40\}$). Both main effects are significant (count: $p = 0.008$; BCS: $p = 0.0002$; $R^2 = 0.52$), but the interaction term is negligible (0.47\,pp). A TOST equivalence test with a $\pm 3$\,pp margin confirms that the interaction is bounded well below practical significance ($p_{\text{TOST}} = 0.003$); this supports bounded interaction between count and confusability effects.
231	
232	A $2 \times 2$ factorial sensitivity check on FewRel (count $\in \{8, 16\}$, BCS low/high; $n = 54$) was inconclusive ($p_{\text{TOST}} = 0.56$) due to limited power; this does not contradict the primary finding but limits generalization beyond the regression framework. The Few-NERD factorial (\S\ref{sec:multi_channel}) similarly did not reach significance ($p = 0.50$). The regression approach provides the stronger test by leveraging the full count range.
233	
234	\paragraph{Equivalence margin justification.}
235	We set the $\pm 3$\,pp margin based on three converging anchors. \emph{External}: evaluation variance in IE benchmarks typically spans 2--5\,pp across random seeds, prompt variations, and data splits \citep{card-2020-power,dror-2018-significance}; our own four structurally distinct prompt variants yield cross-variant accuracy SD of 3.5--4.6\,pp across count conditions (Table~\ref{tab:prompt_variants}), confirming that a within-margin interaction would be indistinguishable from routine prompt-design noise and satisfying the smallest-effect-of-interest criterion \citep{lakens-2017-equivalence}. \emph{Internal}: $0.5 \times$ within-cell SD ($= 2.3$\,pp) corresponds to Cohen's $d \approx 0.5$ (medium effect threshold; \citealt{lakens-2017-equivalence}), cross-validated against the IQR-predicted confusability main effect of 2.2\,pp (\S\ref{sec:practical_magnitude})---an interaction exceeding 3\,pp would represent ${>}130\%$ amplification. \emph{Sensitivity}: Table~\ref{tab:tost_sensitivity} shows equivalence holds from $\pm 2$\,pp ($p = 0.047$) through $\pm 5$\,pp ($p < 0.001$) on the probability scale; the conclusion is not margin-dependent.
236	
237	\begin{table}[h]
238	\centering
239	\small
240	\caption{TOST sensitivity analysis across equivalence margins. The interaction effect (0.47\,pp, 90\% CI [$-$1.0, 2.0]\,pp) is bounded below 2\,pp at marginal significance ($p = 0.047$); the $\pm 3$\,pp choice does not drive the equivalence conclusion. At $\pm 1$\,pp, equivalence is inconclusive ($p = 0.278$), meaning interaction could reach approximately half the main effect magnitude.}
241	\label{tab:tost_sensitivity}
242	\begin{tabular}{crrl}
243	\toprule
244	\textbf{Margin (pp)} & \textbf{$t_{\text{upper}}$} & \textbf{$p_{\text{TOST}}$} & \textbf{Conclusion} \\
245	\midrule
246	$\pm 1$ & $-0.59$ & $0.278$ & Inconclusive \\
247	$\pm 2$ & $-1.70$ & $0.047$ & Equivalent \\
248	$\pm 3$ & $-2.81$ & $0.003$ & Equivalent \\
249	$\pm 5$ & $-5.02$ & ${<}\,0.001$ & Equivalent \\
250	\bottomrule
251	\end{tabular}
252	\end{table}
253	
254	\paragraph{Logit-scale sensitivity.}
255	Because accuracy near 50\% compresses interaction effects on the linear scale, we refit the regression on logit-transformed accuracy. The logit-scale interaction (0.111 logit units, $p = 0.047$, 90\% CI [0.019, 0.203]) is marginally significant, and TOST at the equivalent $\pm 3$\,pp margin ($\pm 0.156$ logit at median accuracy) is inconclusive ($p_{\text{TOST}} = 0.209$). However, back-transforming the interaction to the probability scale at the observed floor ($p = 0.51$) yields 2.78\,pp, still within the $\pm 3$\,pp margin; at the median baseline ($p = 0.65$), the back-transformed effect is 2.53\,pp. The logit TOST is inconclusive due to limited power ($n = 69$, wide CI) rather than a large effect size: the point estimate remains below the equivalence bound at all observed baselines. We retain the linear-scale TOST as the primary test and report this logit analysis as a sensitivity check. A regression-based TOST ($n = 375$, five count levels with continuous BCS) yields $p = 0.050$ at $\pm 3$\,pp and $p = 0.026$ at $\pm 3.5$\,pp on the logit scale, confirming the borderline status with substantially greater power than the factorial design.
256	
257	\paragraph{DocRED factorial (expanded).}
258	With expanded batches ($n{=}55$ per count level, up from $n{=}5$), the DocRED $2 \times 2$ factorial (count $\in \{16, 32\}$, BCS median split) yields an apparent interaction ($-$9.4\,pp, 95\% CI [$-$12.9, $-$6.0]): the BCS effect is $-$25.0\,pp at count 16 but $-$15.7\,pp at count 32. However, this attenuation is confounded by BCS range restriction: higher-count batches have narrower BCS ranges (spread 0.26 vs.\ 0.38), limiting achievable extremes.
259	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "b630632f-d56c-4d84-9931-169dd0eea7d3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
      "content": "\n\\section{Additional Figures}\n\\label{sec:appendix_figures}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\\S\\ref{sec:model}) for fair cross-model comparison; the count-curve results in \\S\\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\\ 0.64 at count${}\\,=\\,1$) due to over-prediction under v1.}\n\\label{tab:cross_model}\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Llama-3.1-8B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1 & 0.702 & 0.640 \\\\\n64 & 0.273 & 0.304 \\\\\n\\midrule\nDecline & $-$43\\,pp & $-$34\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\\approx$51\\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\\Delta$, in pp) is 77--87\\% as large on Llama-3.1-8B as on Qwen3-32B.}\n\\label{tab:cross_model_bcs}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{crrrrrr}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Llama-3.1-8B}} & \\multicolumn{3}{c}{\\textbf{Qwen3-32B}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Count} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} \\\\\n\\midrule\n8 & 78.1\\% & 51.0\\% & $-$27.1 & 82.3\\% & 51.0\\% & $-$31.2 \\\\\n16 & 75.5\\% & 51.6\\% & $-$23.9 & 82.8\\% & 51.6\\% & $-$31.2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{NER batch-level BCS--F1 correlation across models. $^\\dagger$Partial correlation controlling for type frequency. $^\\ddagger$LLaMA-70B count\\_12 shows $r{=}{-}0.42$ ($p{=}0.034$, uncorrected; Bonferroni $p{=}0.069$); pooled and count\\_6 are null, consistent with sampling noise at $n{=}25$. The null is observed on three models; Gemini remains untested.}\n\\label{tab:cross_model_ner_null}\n\\begin{tabular}{lcl}\n\\toprule\n\\textbf{Model} & \\textbf{NER BCS--F1 $r$} & \\textbf{Status} \\\\\n\\midrule\nQwen3-32B & $0.004$ ($p = 0.94$) & Null \\\\\nLLaMA-3.1-8B & $-0.12$ ($p = 0.29$)\\rlap{$^\\dagger$} & Null \\\\\nLLaMA-3.1-70B & $-0.13$ ($p = 0.36$)\\rlap{$^\\ddagger$} & Null \\\\\nGemini 2.5 Flash & --- & Not tested \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin. Spearman $\\rho$ computed over $n=148$ batches (NER), $n=154$ (RE), and $n=110$ (DocRE). IntraSub scales monotonically with BCS across all three datasets. DocRE missed rates decrease with BCS, indicating high-confusability errors shift from omission to substitution.}\n\\label{tab:error_taxonomy}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrrrr}\n\\toprule\n & & \\multicolumn{5}{c}{\\textbf{BCS Bin}} & & \\\\\n\\cmidrule(lr){3-7}\n\\textbf{Task} & \\textbf{Error} & \\textbf{Solo} & \\textbf{Low} & \\textbf{Mid} & \\textbf{High} & \\textbf{V.High} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nNER & IntraSub & 0\\% & 1.6\\% & 10.6\\% & 49.4\\% & --- & 1.000 & ${<}0.001$ \\\\\nRE  & IntraSub & 0\\% & 4.2\\% & 13.0\\% & 20.3\\% & 32.3\\% & 0.954 & ${<}\\,0.001$ \\\\\nDocRE & IntraSub & --- & 4.8\\% & 22.4\\% & 37.0\\% & 41.9\\% & 0.843 & ${<}\\,0.001$ \\\\\n\\midrule\nNER & Missed & --- & 42.8\\% & 64.8\\% & 49.9\\% & --- & --- & --- \\\\\nRE  & Missed & --- & 10.4\\% & 11.3\\% & 13.1\\% & 15.7\\% & --- & --- \\\\\nDocRE & Missed & --- & 28.1\\% & 22.6\\% & 21.6\\% & 16.2\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model replication of IntraSub--BCS Spearman correlation on FewRel RE. $^\\dagger$LLaMA-70B has only 20 batches with 17.4\\% missed rate; the null is attributable to insufficient power rather than absence of the effect.}\n\\label{tab:cross_model_error_taxonomy}\n\\begin{tabular}{lrcc}\n\\toprule\n\\textbf{Model} & $n$ & $\\rho$ & $p$ \\\\\n\\midrule\nQwen3-32B & 154 & 0.954 & ${<}\\,0.001$ \\\\\nGemini 2.5 Flash & 60 & 0.821 & ${<}\\,0.001$ \\\\\nLLaMA-3.1-8B & 54 & 0.430 & 0.001 \\\\\nLLaMA-3.1-70B$^\\dagger$ & 20 & $-$0.086 & 0.719 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{SDGD Full Protocol and Results}\n\\label{sec:appendix_sdgd}\n\nWe construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent (i.e., highly confusable) types share a color. Each color class forms one extraction batch, and predictions are merged via set union.\n\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item Compute pairwise SCS matrix $S_{ij} = \\cos(\\text{embed}(t_i), \\text{embed}(t_j))$.\n\\item Construct graph $G$: add edge $(t_i, t_j)$ iff $S_{ij} > \\tau$.\n\\item Apply greedy graph coloring (\\textsc{largest\\_first}) to assign each type a color $c(t)$.\n\\item For each color $k$, form batch $B_k = \\{t : c(t) = k\\}$ and run extraction on all test instances.\n\\item Merge: union of per-batch predictions (v1) or confidence-gated selection (v2).\n\\end{enumerate}\nOracle routing (Table~\\ref{tab:routing_strategies}) recovers substantial accuracy (72.4\\% vs.\\ 50.4\\% single-pass), confirming the sub-schemas contain correct predictions; the failure lies in routing, not decomposition quality.\n\nWe compare four modes: (i)~\\textbf{single\\_pass}, the undecomposed baseline; (ii)~\\textbf{sdgd\\_zero}, SCS-guided partitioning; (iii)~\\textbf{random\\_batch}, random partitioning with matched batch sizes; and (iv)~\\textbf{per\\_type}, the extreme case where each type is extracted in isolation.\n\nSingle-pass extraction achieves F1\\,=\\,0.445 (P\\,=\\,0.563, R\\,=\\,0.368). SDGD obtains F1\\,=\\,0.251 (P\\,=\\,0.210, R\\,=\\,0.314), a 44\\% relative drop. Random batching reaches F1\\,=\\,0.320 (P\\,=\\,0.249, R\\,=\\,0.446), and per-type extraction yields F1\\,=\\,0.292 (P\\,=\\,0.194, R\\,=\\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\\ref{tab:sdgd_results}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \\texttt{min\\_batch\\_size=8} (reducing 8$\\to$4 batches for sdgd\\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt.}\n\\label{tab:sdgd_results}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrccc}\n\\toprule\n\\textbf{Mode} & \\textbf{\\# Batches} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{F1} \\\\\n\\midrule\nsingle\\_pass & 1 & 0.563 & 0.368 & 0.445 \\\\\n\\midrule\nsdgd\\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\\\\nrandom\\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\\\\nper\\_type & 66 & 0.194 & 0.586 & 0.292 \\\\\n\\midrule\nsdgd\\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\\\\nrandom\\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nDecomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions. Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions and inflates false positives.\n\nOur v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\\_zero: 0.210$\\to$0.324; random\\_batch: 0.249$\\to$0.331), but at the cost of disproportionate recall loss (0.314$\\to$0.191; 0.446$\\to$0.276), and both modes produce lower F1 (sdgd\\_zero: 0.251$\\to$0.241; random\\_batch: 0.320$\\to$0.301).\n\n\\subsection{Practical Routing Strategies on RE}\n\\label{sec:appendix_routing}\n\nWe evaluate five non-oracle routing strategies on FewRel 80-relation RE using graph-coloring sub-schema decomposition (same grouping as Table~\\ref{tab:batch_composition}). Each strategy selects a single sub-schema for each test instance and returns that sub-schema's prediction.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Routing strategy comparison on FewRel 80-relation RE with graph-coloring sub-schema decomposition. Oracle requires gold labels. All practical (non-oracle) strategies perform below the single-pass baseline. The failure stems from constrained decoding (enum constraint), which forces confident predictions in every sub-schema: 73.4\\% of instances receive positive predictions from 3--5 sub-schemas simultaneously, with per-sub-schema none-rates of only 20--40\\%.}\n\\label{tab:routing_strategies}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{@{}lrr@{}}\n\\toprule\n\\textbf{Strategy} & \\textbf{Accuracy} & \\textbf{$\\Delta$ vs.\\ Single-Pass} \\\\\n\\midrule\nOracle (gold label) & 72.4\\% & +22.0\\,pp \\\\\n\\midrule\nMax-conf (positive only) & 36.5\\% & $-$14.0\\,pp \\\\\nNone-aware & 36.5\\% & $-$14.0\\,pp \\\\\nMargin (positive only) & 35.9\\% & $-$14.5\\,pp \\\\\nMax-conf (all) & 27.7\\% & $-$22.7\\,pp \\\\\nRandom & 14.7\\% & $-$35.7\\,pp \\\\\n\\midrule\nSingle-pass (no decomposition) & 50.4\\% & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\section{Factorial Analysis and Separability Test}\n\\label{sec:appendix_factorial}\n\nTo formally test whether count and confusability effects are additive, we fit a multiple regression (accuracy $\\sim$ $\\log_2$\\,count $+$ BCS $+$ count$\\times$BCS) across 69 batches from FewRel spanning five count levels ($k \\in \\{4, 8, 16, 32, 40\\}$). Both main effects are significant (count: $p = 0.008$; BCS: $p = 0.0002$; $R^2 = 0.52$), but the interaction term is negligible (0.47\\,pp). A TOST equivalence test with a $\\pm 3$\\,pp margin confirms that the interaction is bounded well below practical significance ($p_{\\text{TOST}} = 0.003$); this supports bounded interaction between count and confusability effects.\n\nA $2 \\times 2$ factorial sensitivity check on FewRel (count $\\in \\{8, 16\\}$, BCS low/high; $n = 54$) was inconclusive ($p_{\\text{TOST}} = 0.56$) due to limited power; this does not contradict the primary finding but limits generalization beyond the regression framework. The Few-NERD factorial (\\S\\ref{sec:multi_channel}) similarly did not reach significance ($p = 0.50$). The regression approach provides the stronger test by leveraging the full count range.\n\n\\paragraph{Equivalence margin justification.}\nWe set the $\\pm 3$\\,pp margin based on three converging anchors. \\emph{External}: evaluation variance in IE benchmarks typically spans 2--5\\,pp across random seeds, prompt variations, and data splits \\citep{card-2020-power,dror-2018-significance}; our own four structurally distinct prompt variants yield cross-variant accuracy SD of 3.5--4.6\\,pp across count conditions (Table~\\ref{tab:prompt_variants}), confirming that a within-margin interaction would be indistinguishable from routine prompt-design noise and satisfying the smallest-effect-of-interest criterion \\citep{lakens-2017-equivalence}. \\emph{Internal}: $0.5 \\times$ within-cell SD ($= 2.3$\\,pp) corresponds to Cohen's $d \\approx 0.5$ (medium effect threshold; \\citealt{lakens-2017-equivalence}), cross-validated against the IQR-predicted confusability main effect of 2.2\\,pp (\\S\\ref{sec:practical_magnitude})---an interaction exceeding 3\\,pp would represent ${>}130\\%$ amplification. \\emph{Sensitivity}: Table~\\ref{tab:tost_sensitivity} shows equivalence holds from $\\pm 2$\\,pp ($p = 0.047$) through $\\pm 5$\\,pp ($p < 0.001$) on the probability scale; the conclusion is not margin-dependent.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{TOST sensitivity analysis across equivalence margins. The interaction effect (0.47\\,pp, 90\\% CI [$-$1.0, 2.0]\\,pp) is bounded below 2\\,pp at marginal significance ($p = 0.047$); the $\\pm 3$\\,pp choice does not drive the equivalence conclusion. At $\\pm 1$\\,pp, equivalence is inconclusive ($p = 0.278$), meaning interaction could reach approximately half the main effect magnitude.}\n\\label{tab:tost_sensitivity}\n\\begin{tabular}{crrl}\n\\toprule\n\\textbf{Margin (pp)} & \\textbf{$t_{\\text{upper}}$} & \\textbf{$p_{\\text{TOST}}$} & \\textbf{Conclusion} \\\\\n\\midrule\n$\\pm 1$ & $-0.59$ & $0.278$ & Inconclusive \\\\\n$\\pm 2$ & $-1.70$ & $0.047$ & Equivalent \\\\\n$\\pm 3$ & $-2.81$ & $0.003$ & Equivalent \\\\\n$\\pm 5$ & $-5.02$ & ${<}\\,0.001$ & Equivalent \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Logit-scale sensitivity.}\nBecause accuracy near 50\\% compresses interaction effects on the linear scale, we refit the regression on logit-transformed accuracy. The logit-scale interaction (0.111 logit units, $p = 0.047$, 90\\% CI [0.019, 0.203]) is marginally significant, and TOST at the equivalent $\\pm 3$\\,pp margin ($\\pm 0.156$ logit at median accuracy) is inconclusive ($p_{\\text{TOST}} = 0.209$). However, back-transforming the interaction to the probability scale at the observed floor ($p = 0.51$) yields 2.78\\,pp, still within the $\\pm 3$\\,pp margin; at the median baseline ($p = 0.65$), the back-transformed effect is 2.53\\,pp. The logit TOST is inconclusive due to limited power ($n = 69$, wide CI) rather than a large effect size: the point estimate remains below the equivalence bound at all observed baselines. We retain the linear-scale TOST as the primary test and report this logit analysis as a sensitivity check. A regression-based TOST ($n = 375$, five count levels with continuous BCS) yields $p = 0.050$ at $\\pm 3$\\,pp and $p = 0.026$ at $\\pm 3.5$\\,pp on the logit scale, confirming the borderline status with substantially greater power than the factorial design.\n\n\\paragraph{DocRED factorial (expanded).}\nWith expanded batches ($n{=}55$ per count level, up from $n{=}5$), the DocRED $2 \\times 2$ factorial (count $\\in \\{16, 32\\}$, BCS median split) yields an apparent interaction ($-$9.4\\,pp, 95\\% CI [$-$12.9, $-$6.0]): the BCS effect is $-$25.0\\,pp at count 16 but $-$15.7\\,pp at count 32. However, this attenuation is confounded by BCS range restriction: higher-count batches have narrower BCS ranges (spread 0.26 vs.\\ 0.38), limiting achievable extremes.\n",
      "numLines": 200,
      "startLine": 60,
      "totalLines": 919
    }
  }
}
```

</details>

---

### Assistant

_source line 26_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good picture of the main.tex file's appendix. Let me now read the full grep results more carefully. Let me focus on the docs/paper/*.tex files specifically, since those are the actual paper source files. The artifacts/ files are likely generated or older drafts that shouldn't be modified.

Let me read the saved grep output for docs/paper/.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "1c1e1f77-07d3-4852-b29f-591353c63289",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B4hW17iuisg5JtEYbrFaja",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6041,
      "cache_read_input_tokens": 28727,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6041
      },
      "output_tokens": 12,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 27_

Now let me read the full grep results for the docs/paper/ directory and also check each individual .tex file for BCS/SCS formatting.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "55affb4a-d191-4e02-8794-95d44b8b62e1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B4hW17iuisg5JtEYbrFaja",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6041,
      "cache_read_input_tokens": 28727,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6041
      },
      "output_tokens": 12,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Read · `toolu_01CPMDMK1CCQM53Noy2VmeYx`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction/69d255ce-db0b-472a-b13f-c39e9fbc3874/tool-results/toolu_015TTLogq4FwdSUS8S4jCQj3.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "64922383-181e-48a0-ba27-75e6c99388c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B4hW17iuisg5JtEYbrFaja",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6041,
      "cache_read_input_tokens": 28727,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6041
      },
      "output_tokens": 12,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-22T11:10:04.700Z_

<details><summary>↩ Tool result · `toolu_01CPMDMK1CCQM53Noy2VmeYx`</summary>

```text
1	docs/paper/related_work.tex:10:[Omitted long matching line]
2	docs/paper/related_work.tex:16:\paragraph{SCS novelty.}
3	docs/paper/related_work.tex:18:[Omitted long matching line]
4	docs/paper/main.tex:44:BCS-controlled experiments use greedy decoding with a single seed; residual SD${}\,=\,0.88$\,pp is 18--44\% of the observed effect size (Appendix~\ref{app:variance-decomposition}), so detection is robust but point estimates carry meaningful uncertainty.
5	docs/paper/main.tex:48:DocRED exhibits severe multicollinearity (VIF${}\,=\,50.9$), preventing reliable BCS effect quantification; semipartial $R^2{}\,=\,5.6\%$ serves only as directional evidence, and the count${}\times{}$BCS interaction is partially confounded by BCS range restriction at higher counts (Appendix~\ref{sec:appendix_factorial}).
6	docs/paper/main.tex:52:BCS batch-level prediction is significant in RE but not detected in NER, where errors scatter across miss, boundary, and type modes (Appendix~\ref{app:relaxed-matching}).
7	docs/paper/main.tex:84:\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\approx$51\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\Delta$, in pp) is 77--87\% as large on Llama-3.1-8B as on Qwen3-32B.}
8	docs/paper/main.tex:102:\caption{NER batch-level BCS--F1 correlation across models. $^\dagger$Partial correlation controlling for type frequency. $^\ddagger$LLaMA-70B count\_12 shows $r{=}{-}0.42$ ($p{=}0.034$, uncorrected; Bonferroni $p{=}0.069$); pooled and count\_6 are null, consistent with sampling noise at $n{=}25$. The null is observed on three models; Gemini remains untested.}
9	docs/paper/main.tex:106:\textbf{Model} & \textbf{NER BCS--F1 $r$} & \textbf{Status} \\
10	docs/paper/main.tex:119:\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin. Spearman $\rho$ computed over $n=148$ batches (NER), $n=154$ (RE), and $n=110$ (DocRE). IntraSub scales monotonically with BCS across all three datasets. DocRE missed rates decrease with BCS, indicating high-confusability errors shift from omission to substitution.}
11	docs/paper/main.tex:124: & & \multicolumn{5}{c}{\textbf{BCS Bin}} & & \\
12	docs/paper/main.tex:142:\caption{Cross-model replication of IntraSub--BCS Spearman correlation on FewRel RE. $^\dagger$LLaMA-70B has only 20 batches with 17.4\% missed rate; the null is attributable to insufficient power rather than absence of the effect.}
13	docs/paper/main.tex:159:We construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\text{SCS}(t_i, t_j) > \tau$. Greedy graph coloring (\textsc{largest\_first}) assigns each type to a color such that no two adjacent (i.e., highly confusable) types share a color. Each color class forms one extraction batch, and predictions are merged via set union.
14	docs/paper/main.tex:162:\item Compute pairwise SCS matrix $S_{ij} = \cos(\text{embed}(t_i), \text{embed}(t_j))$.
15	docs/paper/main.tex:170:We compare four modes: (i)~\textbf{single\_pass}, the undecomposed baseline; (ii)~\textbf{sdgd\_zero}, SCS-guided partitioning; (iii)~\textbf{random\_batch}, random partitioning with matched batch sizes; and (iv)~\textbf{per\_type}, the extreme case where each type is extracted in isolation.
16	docs/paper/main.tex:230:[Omitted long matching line]
17	docs/paper/main.tex:232:A $2 \times 2$ factorial sensitivity check on FewRel (count $\in \{8, 16\}$, BCS low/high; $n = 54$) was inconclusive ($p_{\text{TOST}} = 0.56$) due to limited power; this does not contradict the primary finding but limits generalization beyond the regression framework. The Few-NERD factorial (\S\ref{sec:multi_channel}) similarly did not reach significance ($p = 0.50$). The regression approach provides the stronger test by leveraging the full count range.
18	docs/paper/main.tex:255:[Omitted long matching line]
19	docs/paper/main.tex:258:With expanded batches ($n{=}55$ per count level, up from $n{=}5$), the DocRED $2 \times 2$ factorial (count $\in \{16, 32\}$, BCS median split) yields an apparent interaction ($-$9.4\,pp, 95\% CI [$-$12.9, $-$6.0]): the BCS effect is $-$25.0\,pp at count 16 but $-$15.7\,pp at count 32. However, this attenuation is confounded by BCS range restriction: higher-count batches have narrower BCS ranges (spread 0.26 vs.\ 0.38), limiting achievable extremes.
20	docs/paper/main.tex:261:[Omitted long matching line]
21	docs/paper/main.tex:266:[Omitted long matching line]
22	docs/paper/main.tex:271:Section~\ref{sec:centrality_confound} identifies a centrality confound in MAVEN's per-type BCS--F1 correlation: both embeddings show a \emph{positive} raw correlation, opposite to the expected direction. Here we formalize this analysis by identifying specific confounders for each embedding and testing whether the BCS--F1 relationship survives partial correlation controlling for these confounders.
23	docs/paper/main.tex:274:For each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:
24	docs/paper/main.tex:276:\item \textbf{MiniLM}: BCS correlates with log type frequency ($r = 0.201$). Frequent types have more training signal and are extracted more reliably, which produces the positive BCS--F1 association.
25	docs/paper/main.tex:277:\item \textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors, central, well-represented types that the model extracts well.
26	docs/paper/main.tex:281:Table~\ref{tab:residualized_bcs} reports raw Spearman $\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.
27	docs/paper/main.tex:286:\caption{MAVEN per-type BCS--F1 correlation before and after controlling for centrality confounders. Raw correlations are Spearman $\rho$; partial correlations are Pearson $r$ from residualized regression. Degree centrality is computed on the SCS graph at threshold 0.7. All values from experiment \texttt{exp\_maven\_residualized\_bcs}.}
28	docs/paper/main.tex:305:[Omitted long matching line]
29	docs/paper/main.tex:307:[Omitted long matching line]
30	docs/paper/main.tex:312:To rule out degree centrality as a confound in cross-domain datasets, we compute partial correlations between BCS and accuracy controlling for batch mean degree centrality (mean off-diagonal SCS per type, averaged across batch members).
31	docs/paper/main.tex:317:\caption{BCS--accuracy partial correlation controlling for degree centrality. FewRel shows minimal attenuation (VIF${}\,=\,1.18$, low collinearity). DocRED shows high BCS--centrality collinearity (VIF${}\,=\,50.9$, $r = 0.99$), but the partial correlation remains highly significant.}
32	docs/paper/main.tex:329:[Omitted long matching line]
33	docs/paper/main.tex:332:[Omitted long matching line]
34	docs/paper/main.tex:334:\subsection{NER BCS-Null Power Analysis}
35	docs/paper/main.tex:337:[Omitted long matching line]
36	docs/paper/main.tex:342:[Omitted long matching line]
37	docs/paper/main.tex:344:\subsection{Domain Distribution in Extreme-BCS Batches}
38	docs/paper/main.tex:347:[Omitted long matching line]
39	docs/paper/main.tex:360:\textbf{Condition} & \textbf{Accuracy} & \textbf{Mean BCS} \\
40	docs/paper/main.tex:379:[Omitted long matching line]
41	docs/paper/main.tex:382:[Omitted long matching line]
42	docs/paper/main.tex:385:[Omitted long matching line]
43	docs/paper/main.tex:387:\subsection{Cross-Prompt-Variant BCS Correlation}
44	docs/paper/main.tex:390:To verify that the BCS--accuracy relationship is not an artifact of a specific prompt template, we evaluate four structurally distinct prompt variants on FewRel 80-relation RE at two count levels (8 and 32), with 10 random batches per condition (Table~\ref{tab:prompt_variants}).
45	docs/paper/main.tex:395:\caption{BCS--accuracy Pearson correlation across four prompt variants. At count 32, all four variants show negative BCS--accuracy correlations ($r \leq -0.47$), with two reaching $p < 0.05$. At count 8, the narrower BCS range reduces statistical power.}
46	docs/paper/main.tex:413:[Omitted long matching line]
47	docs/paper/main.tex:415:\section{BCS Aggregation Sensitivity}
48	docs/paper/main.tex:418:We define Batch Confusability Score (BCS) as the \emph{mean} pairwise SCS across all type pairs in a batch (\S\ref{sec:bcs_controlled}). An alternative definition takes the \emph{maximum} pairwise SCS within each batch to capture the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice (Table~\ref{tab:bcs_aggregation}).
49	docs/paper/main.tex:423:\caption{BCS--accuracy regression under mean vs.\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p \approx 0.60$; MAX $p \approx 0.44$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}
50	docs/paper/main.tex:441:\section{BCS-Controlled Detailed Results}
51	docs/paper/main.tex:447:\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\ref{tab:within_pool}; see \S\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}
52	docs/paper/main.tex:452:\textbf{Schema} & \textbf{Count} & \textbf{Low-BCS} & \textbf{High-BCS} & \textbf{$\Delta$ (pp)} & \textbf{95\% CI} \\
53	docs/paper/main.tex:462:DocRED regressions (\S\ref{sec:bcs_controlled}) use OLS on $n = 55$ batches (15 high-BCS + 15 low-BCS + 25 random) per count level, with one predictor. At count 16, adjusted $R^2 = 0.646$ (unadjusted: 0.653; 95\% CI [0.53, 0.77]); at count 32, adjusted $R^2 = 0.606$ (unadjusted: 0.614; 95\% CI [0.47, 0.75]). The small shrinkage ($\Delta R^2 \leq 0.01$) indicates the unadjusted values are not inflated by the predictor-to-sample ratio.
54	docs/paper/main.tex:467:To test whether the BCS--accuracy relationship depends on the output format, we run both constrained (enum-based) and unconstrained (free-text) decoding on the same 25 batch type sets from the FewRel 80-relation pool (13 low-BCS, 12 high-BCS; count 8). Each batch uses identical instances and type sets; only the decoding format differs (Table~\ref{tab:format_independence}).
55	docs/paper/main.tex:472:\caption{Paired comparison of constrained vs.\ unconstrained decoding on 25 identical FewRel batch type sets. Both formats yield virtually identical BCS--accuracy correlations (Fisher $z \approx 0$), confirming the confusability effect is format-independent. Mean accuracy is also unchanged ($\Delta = -0.08$\,pp), ruling out a format-driven accuracy shift.}
56	docs/paper/main.tex:479:Pearson $r$ (BCS vs.\ acc) & $-$0.448 ($p = 0.025$) & $-$0.439 ($p = 0.028$) \\
57	docs/paper/main.tex:480:Spearman $\rho$ (BCS vs.\ acc) & $-$0.157 ($p = 0.455$) & $-$0.144 ($p = 0.492$) \\
58	docs/paper/main.tex:489:[Omitted long matching line]
59	docs/paper/main.tex:497:\caption{Per-batch accuracy (\%) under constrained and unconstrained decoding on 25 identical FewRel batch type sets (count 8, 96 instances each). 23/25 batches yield identical accuracy; the two exceptions differ by exactly one sample ($\Delta = -1.04$\,pp). L = low-BCS, H = high-BCS.}
60	docs/paper/main.tex:502:\textbf{Batch} & \textbf{Group} & \textbf{BCS} & \textbf{Constr.} & \textbf{Unconstr.} & \textbf{$\Delta$} \\
61	docs/paper/main.tex:537:A potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol.
62	docs/paper/main.tex:542:\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\ref{sec:appendix_within_pool} for CI interpretation.}
63	docs/paper/main.tex:547:& \multicolumn{4}{c}{\textbf{Regression (BCS $\to$ Accuracy)}} & \multicolumn{2}{c}{\textbf{Quartile $\Delta$}} \\
64	docs/paper/main.tex:556:\multicolumn{7}{l}{\footnotesize $^\dagger$BCS range (IQR\,=\,0.033) insufficient for regression; slope not interpretable.} \\
65	docs/paper/main.tex:561:The within-pool slope ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.509; permutation $p \approx 0.60$). The smaller quartile gap ($-$3.92\,pp vs.\ $-$5.31\,pp) reflects the narrower BCS range within the 80-relation pool (Appendix~\ref{sec:appendix_within_pool}).
66	docs/paper/main.tex:563:In the full 80-relation condition, natural BCS variation is insufficient (IQR${}=0.033$) to yield a detectable effect ($n=25$, slope${}=+0.221$, $p \approx 0.76$). This does not invalidate the confusability effect; the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied, but establishes that natural schema sampling at this scale does not produce sufficient BCS contrast for detection.
67	docs/paper/main.tex:565:\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}
68	docs/paper/main.tex:568:Table~\ref{tab:scs-ablation} compares predictive accuracy of name-only SCS against name+definition SCS across three datasets.
69	docs/paper/main.tex:573:\caption{Pearson correlation between SCS and empirical confusion rate. ``Def'' concatenates type name with definition before embedding. All correlations significant ($p < 0.001$). The inconsistent direction of $\Delta r$ indicates that definitions provide no systematic benefit.}
70	docs/paper/main.tex:577:Dataset & SCS$_\text{name}$ $r$ & SCS$_\text{def}$ $r$ & $\Delta r$ & Matrix corr. \\
71	docs/paper/main.tex:586:Few-NERD is the only dataset whose prompts include type definitions; for MAVEN and FewRel, prompts use type names alone, so name-only SCS directly matches model input. The high matrix correlation (0.66--0.89) confirms that type names capture the dominant semantic structure.
72	docs/paper/main.tex:590:From the 80-type confusion matrix, we extract the $\binom{16}{2} = 120$ pairs among the 16 validation-origin types (fully disjoint from the 64 training-pool types). The SCS--confusion Spearman correlation remains positive and significant ($\rho = 0.216$, $p = 0.018$), nearly identical to the full 80-type pool ($\rho = 0.218$, $p < 0.001$, $n = 3{,}160$ pairs), ruling out training-set contamination as the driver of the observed relationship.
73	docs/paper/main.tex:597:[Omitted long matching line]
74	docs/paper/main.tex:602:[Omitted long matching line]
75	docs/paper/main.tex:605:The inter-pair SCS correlation $\rho = 0.35$ is estimated from pairs sharing a common type. At $\rho = 0.20$ (halved correlation), a parallel simulation yields batch $R^2 \approx 0.22$; at $\rho = 0.50$, the correlation structure approaches the positive-definiteness boundary; $\rho = 0.35$ thus sits in a stable regime. The simulation is illustrative; the pooled semipartial $R^2 = 0.273$ (\S\ref{sec:bcs_controlled}) is the primary evidence.
76	docs/paper/main.tex:608:[Omitted long matching line]
77	docs/paper/main.tex:610:\section{BCS Independence from Type Composition}
78	docs/paper/main.tex:613:[Omitted long matching line]
79	docs/paper/main.tex:615:\section{SCS vs.\ Simple Baselines}
80	docs/paper/main.tex:618:Table~\ref{tab:scs_baselines} compares SCS against simple baselines for pairwise confusion prediction.
81	docs/paper/main.tex:623:\caption{Pairwise confusion prediction: SCS vs.\ simple baselines. Spearman $\rho$ between each metric and the empirical confusion rate. SCS outperforms all baselines on FewRel; the margin is smaller on Few-NERD, where hierarchical naming conventions provide partial signal to string-based metrics. $^\dagger$42\% of pairs lack WordNet coverage.}
82	docs/paper/main.tex:630:FewRel & SCS (embedding) & \textbf{0.218} & $< 0.001$ \\
83	docs/paper/main.tex:635:Few-NERD & SCS (embedding) & \textbf{0.166} & $< 0.001$ \\
84	docs/paper/main.tex:646:FewRel combines 64 train-split and 16 val-split relation types into a single 80-type pool.  Train-origin types show numerically lower accuracy ($-8.8$\,pp, $p = 0.06$; see Limitations), raising the question of whether differential pre-training exposure confounds the BCS--accuracy relationship.  We test this by adding a per-batch \emph{train-origin ratio} (fraction of relation types drawn from the train split) as a covariate in the BCS--accuracy regression.
85	docs/paper/main.tex:650:\text{acc} = \beta_0 + \beta_{\text{BCS}} \!\cdot\! \text{BCS} + \beta_{\text{orig}} \!\cdot\! \text{train\_origin\_ratio} + \varepsilon
86	docs/paper/main.tex:653:\paragraph{Results.}  The BCS partial effect is unchanged after controlling for split-origin: $\beta_{\text{BCS}} = -0.416$, $p < 0.001$ (vs.\ $\beta = -0.412$, $p < 0.001$ without the covariate).  Train-origin ratio is not independently significant ($\beta_{\text{origin}} = -0.057$, $p = 0.245$), and $\Delta R^2 = 0.005$.  The BCS--accuracy relationship is therefore not confounded by differential pre-training exposure at the batch level.
87	docs/paper/main.tex:655:Pairwise SCS distributions do not differ significantly between train-origin (64 types, mean\,=\,0.880) and val-origin (16 types, mean\,=\,0.874) subsets (Mann-Whitney $p = 0.754$, Cohen's $d = 0.081$); the train/val split does not introduce systematic confusability bias.
88	docs/paper/main.tex:685:[Omitted long matching line]
89	docs/paper/main.tex:690:To test whether the two-dimensional degradation pattern generalizes across models, we replicate the count-curve and BCS-controlled experiments on Meta-LLaMA-3.1-70B-Instruct (FP8 quantization). All batch compositions, type pools, and test samples are identical to those used for Qwen3-32B (\S\ref{sec:count_curves}, \S\ref{sec:bcs_controlled}).
90	docs/paper/main.tex:723:For the confusability dimension (Dimension 2), at count 16 on FewRel, LLaMA-70B achieves low-BCS accuracy of 0.708 versus high-BCS accuracy of 0.599 ($\Delta = +10.9$\,pp, 95\% CI [$+$3.0, $+$20.1]). The confidence interval excludes zero; the confusability effect is thus confirmed at the 70B scale.
91	docs/paper/main.tex:730:We validate both dimensions on a proprietary model, Gemini 2.5 Flash \citep{gemini-2025}, accessed via API. This extends the cross-model evidence from open-weight families (Qwen, LLaMA) to a proprietary architecture with unknown training details. We replicate the FewRel count-curve and BCS-controlled experiments using the same 960 balanced samples, batch compositions, and evaluation protocol as Qwen3-32B.
92	docs/paper/main.tex:753:\paragraph{Dimension~2: BCS-controlled confusability.}
93	docs/paper/main.tex:754:We replicate the BCS-controlled experiment on Gemini 2.5 Flash using extreme-BCS batches at count 8 ($n = 50$; 25 low-BCS, 25 high-BCS) and count 16 ($n = 10$; 5+5).
94	docs/paper/main.tex:756:[Omitted long matching line]
95	docs/paper/main.tex:758:Table~\ref{tab:cross_model_bcs_summary} summarizes BCS-controlled results across all validated models. Both dimensions thus replicate on a proprietary architecture with unknown training details.
96	docs/paper/main.tex:763:\caption{Cross-model BCS-controlled FewRel RE summary. All models show significant low-vs-high BCS accuracy gaps. Gap magnitude varies with model capacity (ceiling compression), but the direction is consistent across open-weight (8B--70B) and proprietary architectures.}
97	docs/paper/main.tex:767:\textbf{Model} & \textbf{Count} & \textbf{Low BCS} & \textbf{High BCS} & \textbf{$\Delta$} & \textbf{95\% CI} \\
98	docs/paper/main.tex:781:[Omitted long matching line]
99	docs/paper/main.tex:786:\caption{BCS gap under few-shot prompting (FewRel, count 8). Demonstrations improve absolute accuracy on low-BCS batches (+3.3--7.2\,pp over 0-shot) but provide inconsistent benefit on high-BCS batches (+5.6\,pp at 1-shot, $-$1.0\,pp at 5-shot). The confusability gap widens from +18.5\,pp (0-shot) to +22.8\,pp (5-shot). All metrics are micro-averaged across batches.}
100	docs/paper/main.tex:790:\textbf{Condition} & \textbf{Low-BCS} & \textbf{High-BCS} & \textbf{$\Delta$ (pp)} & \textbf{95\% CI} \\
101	docs/paper/main.tex:799:[Omitted long matching line]
102	docs/paper/main.tex:806:Tables~\ref{tab:top10_re} and~\ref{tab:top10_ner} list the ten most frequently confused type pairs on FewRel 80-relation RE and Few-NERD NER. Confusion counts are aggregated bidirectionally across three random seeds (72{,}000 predictions per seed for RE; single-seed 66-type extraction for NER). Table~\ref{tab:error_examples} provides illustrative confusion instances with SCS values.
103	docs/paper/main.tex:811:[Omitted long matching line]
104	docs/paper/main.tex:815:\textbf{\#} & \textbf{Type A} & \textbf{Type B} & \textbf{SCS} & \textbf{$N$} \\
105	docs/paper/main.tex:834:[Omitted long matching line]
106	docs/paper/main.tex:838:\textbf{\#} & \textbf{Type A} & \textbf{Type B} & \textbf{SCS} & \textbf{$N$} \\
107	docs/paper/main.tex:857:\caption{Illustrative confusion instances from FewRel 80-rel RE. All gold-predicted pairs have SCS\,$>$\,0.90: \textit{participant} vs.\ \textit{participant of} reverses directionality; \textit{contains} vs.\ \textit{located in} inverts containment; \textit{part of} vs.\ \textit{member of} conflates meronymy with membership. a.t.e.\ = admin.\ territorial entity.}
108	docs/paper/main.tex:861:\textbf{Sentence} & \textbf{Gold} & \textbf{Pred.} & \textbf{SCS} \\
109	docs/paper/main.tex:875:[Omitted long matching line]
110	docs/paper/main.tex:880:\caption{Accuracy (\%) under original vs.\ renamed labels on FewRel count-8 batches. Renaming reduced embedding similarity but decreased accuracy in both groups, with a larger drop on high-BCS batches (Cohen's $d = -2.92$) than low-BCS ($d = -1.09$). Interaction: $\Delta_{\text{high}} - \Delta_{\text{low}} = -5.9$\,pp ($t = -7.23$, $p < 0.001$).}
111	docs/paper/main.tex:886:Low-BCS ($n=25$)  & 90.1 & 87.1 & $-$3.0 \\
112	docs/paper/main.tex:887:High-BCS ($n=25$) & 69.3 & 60.5 & $-$8.8 \\
113	docs/paper/main.tex:897:To test whether exact-match F1 masks the BCS signal in NER by conflating boundary errors with type errors, we evaluate three progressively relaxed matching criteria on the full Few-NERD NER dataset ($n = 450$ batches: 6 count levels $\times$ 25 batches $\times$ 3 seeds; Table~\ref{tab:relaxed_matching}).
114	docs/paper/main.tex:902:[Omitted long matching line]
115	docs/paper/main.tex:916:A per-error-mode analysis confirms this null extends to all individual categories: miss ($\rho = 0.017$), boundary ($\rho = -0.043$), and type substitution ($\rho = -0.010$) rates show no BCS association (all $p > 0.3$, $n = 450$). The null holds within each count level (count 2: $r = 0.022$; count 6: $r = 0.110$; count 12: $r = 0.028$; all $p > 0.3$), ruling out count as a confound.
116	docs/paper/checklist.tex:15:Yes (Limitations). SCS/BCS may be misused as a standalone deployment criterion. Since they are proxies for confusability and do not capture domain-specific ambiguity or downstream harms, they should be used for diagnostic monitoring rather than automatic schema rejection or high-stakes deployment decisions.
117	docs/paper/checklist.tex:49:Yes. Table~\ref{tab:datasets} reports type counts, evaluation unit counts, domain characteristics, and BCS ranges for each dataset. \S\ref{sec:datasets} describes dataset provenance and sampling procedures.
118	docs/paper/checklist.tex:67:Yes. \S\ref{sec:exp_design} describes both experimental paradigms (count curves and BCS-controlled). \S\ref{sec:model} reports decoding parameters (greedy, temperature${}=0$, seed${}=42$) and prompt versions. No hyperparameter search was conducted as this is a zero-shot evaluation study.
119	docs/paper/discussion.tex:6:The confusability signal applies to cross-domain schemas; same-domain schemas exhibit centrality confounding (\S\ref{sec:centrality_confound}). Modest pairwise $r^2$ compounds at the batch level because correlated type interactions aggregate within shared prompts (\S\ref{sec:bcs_controlled}). The NER--RE asymmetry reflects dispersed error modes and compressed BCS variance (Appendix~\ref{sec:appendix_ner_power}).
120	docs/paper/discussion.tex:10:[Omitted long matching line]
121	docs/paper/discussion.tex:15:[Omitted long matching line]
122	docs/paper/abstract.tex:2:[Omitted long matching line]
123	docs/paper/abstract.tex:3:(1)~count degradation spans all three tasks (up to $-$49\,pp); inter-type confusability (measured by BCS) independently predicts RE type substitution errors (VIF${}\,=\,1.18$ on FewRel);
124	docs/paper/abstract.tex:4:(2)~BCS independently explains ${\sim}$27\% of cross-batch RE accuracy variance on FewRel (semipartial $R^2 = 0.273$ after controlling for degree centrality; VIF${}\,=\,1.18$), replicating across three open-weight model families (8B--70B); the NER batch-level null serves as a boundary condition (dispersed error modes, BCS range compression);
125	docs/paper/experimental_setup.tex:13:[Omitted long matching line]
126	docs/paper/experimental_setup.tex:21:Table~\ref{tab:datasets} summarizes the dataset statistics, including the Schema Confusability Score (SCS) ranges defined in \S\ref{sec:scs}.
127	docs/paper/experimental_setup.tex:29:\textbf{Dataset} & \textbf{Task} & \textbf{\# Types} & \textbf{\# Eval Units} & \textbf{Domain} & \textbf{BCS Range} & \textbf{Embedding} \\
128	docs/paper/experimental_setup.tex:37:\caption{Dataset statistics. BCS Range: min--max over count-curve batches. Embedding: model used for SCS/BCS; ranges are not comparable across embedding models. $^\dagger$Trigger mentions across 8{,}042 sentences.}
129	docs/paper/experimental_setup.tex:41:\subsection{Schema Confusability Score (SCS)}
130	docs/paper/experimental_setup.tex:45:We define the Schema Confusability Score (SCS) to quantify semantic overlap between types in a schema. Given a type $t$ with name string $\text{name}(t)$, an embedding function $\text{embed}(\cdot)$ maps the type name to a vector representation. The \textbf{pairwise SCS} between types $t_i$ and $t_j$ is:
131	docs/paper/experimental_setup.tex:48:\text{SCS}(t_i, t_j) = \cos\bigl(\text{embed}(\text{name}(t_i)),\; \text{embed}(\text{name}(t_j))\bigr)
132	docs/paper/experimental_setup.tex:52:For a batch of types $B = \{t_1, \ldots, t_k\}$, the \textbf{Batch Confusability Score (BCS)} aggregates all pairwise similarities:
133	docs/paper/experimental_setup.tex:54:\text{BCS}(B) = \frac{1}{\binom{k}{2}} \sum_{i < j,\; t_i, t_j \in B} \text{SCS}(t_i, t_j)
134	docs/paper/experimental_setup.tex:57:[Omitted long matching line]
135	docs/paper/experimental_setup.tex:59:\paragraph{SCS as a lightweight proxy.}
136	docs/paper/experimental_setup.tex:61:SCS is a pre-hoc proxy computable without running extraction; pairwise correlations with observed type confusion are reported in \S\ref{sec:pairwise}. SCS does not capture context-dependent disambiguation or mention-level ambiguity; these contribute to residual variance.
137	docs/paper/experimental_setup.tex:74:[Omitted long matching line]
138	docs/paper/experimental_setup.tex:86:\paragraph{Experiment 2: BCS-Controlled.}
139	docs/paper/experimental_setup.tex:87:[Omitted long matching line]
140	docs/paper/introduction.tex:10:This study combines correlational analyses with quasi-experimental manipulation (BCS-controlled batches) to characterize how schema properties predict extraction accuracy.
141	docs/paper/introduction.tex:15:[Omitted long matching line]
142	docs/paper/introduction.tex:19:(2)~Pairwise SCS predicts type confusion across NER, RE, and ED (\S\ref{sec:pairwise}); at batch level, BCS predicts RE accuracy independent of output format (\S\ref{sec:bcs_controlled}) but not NER accuracy at current statistical power; per-type aggregation is confounded by centrality on homogeneous schemas (\S\ref{sec:centrality_confound}).
143	docs/paper/introduction.tex:24:[Omitted long matching line]
144	docs/paper/introduction.tex:25:    \item We document a task-dependent boundary: the RE confusability effect is confirmed as format-independent across three model families, while the NER batch-level BCS null---reported as a boundary condition rather than a negative result---is attributable to dispersed error modes (miss, boundary, type) and BCS range compression (\S\ref{sec:bcs_controlled}, \S\ref{sec:multi_channel}).
145	docs/paper/results.tex:10:[Omitted long matching line]
146	docs/paper/results.tex:15:We test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate (the fraction of $t_i$ gold instances misclassified as $t_j$) and correlate it with $\text{SCS}(t_i, t_j)$. Table~\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\% CIs.
147	docs/paper/results.tex:29:\caption{Pairwise SCS--confusion correlation. Confusion rate is bidirectional $C(t_i{\to}t_j) + C(t_j{\to}t_i)$ divided by gold frequency sum; CIs are percentile bootstrap ($B{=}10{,}000$). FewRel ($r = 0.187$; \S\ref{sec:scs-validation}) excluded (per-instance RE format). Type-level cluster bootstrap CIs exclude zero (Few-NERD [0.069, 0.219]; MAVEN [0.081, 0.185]).}
148	docs/paper/results.tex:37:[Omitted long matching line]
149	docs/paper/results.tex:42:\caption{Error taxonomy decomposition (Few-NERD NER and FewRel RE). IntraSub scales monotonically with BCS across all evaluated datasets ($\rho = 0.84\text{--}1.0$; Table~\ref{tab:error_taxonomy} includes DocRED). RE missed rates remain flat (10--16\%), but NER missed rates are substantially higher (43--65\%) and non-monotonic.}
150	docs/paper/results.tex:46:\subsection{BCS-Controlled Experiments}
151	docs/paper/results.tex:50:[Omitted long matching line]
152	docs/paper/results.tex:52:[Omitted long matching line]
153	docs/paper/results.tex:55:[Omitted long matching line]
154	docs/paper/results.tex:59:Within-pool analysis confirms slope consistency across pools (permutation $p \approx 0.60$; Appendix~\ref{app:within-pool-method}). The 80-relation extreme-batch gap (\S\ref{sec:bcs_controlled}) reflects wider BCS range, not stronger per-unit sensitivity.
155	docs/paper/results.tex:64:[Omitted long matching line]
156	docs/paper/results.tex:68:[Omitted long matching line]
157	docs/paper/results.tex:72:[Omitted long matching line]
158	docs/paper/results.tex:78:[Omitted long matching line]
159	docs/paper/results.tex:81:[Omitted long matching line]
160	docs/paper/results.tex:86:[Omitted long matching line]
161	docs/paper/sdgd_negative.tex:5:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "2ed75fdd-1968-407f-a4ab-f58090378e1f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction/69d255ce-db0b-472a-b13f-c39e9fbc3874/tool-results/toolu_015TTLogq4FwdSUS8S4jCQj3.txt",
      "content": "docs/paper/related_work.tex:10:[Omitted long matching line]\ndocs/paper/related_work.tex:16:\\paragraph{SCS novelty.}\ndocs/paper/related_work.tex:18:[Omitted long matching line]\ndocs/paper/main.tex:44:BCS-controlled experiments use greedy decoding with a single seed; residual SD${}\\,=\\,0.88$\\,pp is 18--44\\% of the observed effect size (Appendix~\\ref{app:variance-decomposition}), so detection is robust but point estimates carry meaningful uncertainty.\ndocs/paper/main.tex:48:DocRED exhibits severe multicollinearity (VIF${}\\,=\\,50.9$), preventing reliable BCS effect quantification; semipartial $R^2{}\\,=\\,5.6\\%$ serves only as directional evidence, and the count${}\\times{}$BCS interaction is partially confounded by BCS range restriction at higher counts (Appendix~\\ref{sec:appendix_factorial}).\ndocs/paper/main.tex:52:BCS batch-level prediction is significant in RE but not detected in NER, where errors scatter across miss, boundary, and type modes (Appendix~\\ref{app:relaxed-matching}).\ndocs/paper/main.tex:84:\\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\\approx$51\\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\\Delta$, in pp) is 77--87\\% as large on Llama-3.1-8B as on Qwen3-32B.}\ndocs/paper/main.tex:102:\\caption{NER batch-level BCS--F1 correlation across models. $^\\dagger$Partial correlation controlling for type frequency. $^\\ddagger$LLaMA-70B count\\_12 shows $r{=}{-}0.42$ ($p{=}0.034$, uncorrected; Bonferroni $p{=}0.069$); pooled and count\\_6 are null, consistent with sampling noise at $n{=}25$. The null is observed on three models; Gemini remains untested.}\ndocs/paper/main.tex:106:\\textbf{Model} & \\textbf{NER BCS--F1 $r$} & \\textbf{Status} \\\\\ndocs/paper/main.tex:119:\\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin. Spearman $\\rho$ computed over $n=148$ batches (NER), $n=154$ (RE), and $n=110$ (DocRE). IntraSub scales monotonically with BCS across all three datasets. DocRE missed rates decrease with BCS, indicating high-confusability errors shift from omission to substitution.}\ndocs/paper/main.tex:124: & & \\multicolumn{5}{c}{\\textbf{BCS Bin}} & & \\\\\ndocs/paper/main.tex:142:\\caption{Cross-model replication of IntraSub--BCS Spearman correlation on FewRel RE. $^\\dagger$LLaMA-70B has only 20 batches with 17.4\\% missed rate; the null is attributable to insufficient power rather than absence of the effect.}\ndocs/paper/main.tex:159:We construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent (i.e., highly confusable) types share a color. Each color class forms one extraction batch, and predictions are merged via set union.\ndocs/paper/main.tex:162:\\item Compute pairwise SCS matrix $S_{ij} = \\cos(\\text{embed}(t_i), \\text{embed}(t_j))$.\ndocs/paper/main.tex:170:We compare four modes: (i)~\\textbf{single\\_pass}, the undecomposed baseline; (ii)~\\textbf{sdgd\\_zero}, SCS-guided partitioning; (iii)~\\textbf{random\\_batch}, random partitioning with matched batch sizes; and (iv)~\\textbf{per\\_type}, the extreme case where each type is extracted in isolation.\ndocs/paper/main.tex:230:[Omitted long matching line]\ndocs/paper/main.tex:232:A $2 \\times 2$ factorial sensitivity check on FewRel (count $\\in \\{8, 16\\}$, BCS low/high; $n = 54$) was inconclusive ($p_{\\text{TOST}} = 0.56$) due to limited power; this does not contradict the primary finding but limits generalization beyond the regression framework. The Few-NERD factorial (\\S\\ref{sec:multi_channel}) similarly did not reach significance ($p = 0.50$). The regression approach provides the stronger test by leveraging the full count range.\ndocs/paper/main.tex:255:[Omitted long matching line]\ndocs/paper/main.tex:258:With expanded batches ($n{=}55$ per count level, up from $n{=}5$), the DocRED $2 \\times 2$ factorial (count $\\in \\{16, 32\\}$, BCS median split) yields an apparent interaction ($-$9.4\\,pp, 95\\% CI [$-$12.9, $-$6.0]): the BCS effect is $-$25.0\\,pp at count 16 but $-$15.7\\,pp at count 32. However, this attenuation is confounded by BCS range restriction: higher-count batches have narrower BCS ranges (spread 0.26 vs.\\ 0.38), limiting achievable extremes.\ndocs/paper/main.tex:261:[Omitted long matching line]\ndocs/paper/main.tex:266:[Omitted long matching line]\ndocs/paper/main.tex:271:Section~\\ref{sec:centrality_confound} identifies a centrality confound in MAVEN's per-type BCS--F1 correlation: both embeddings show a \\emph{positive} raw correlation, opposite to the expected direction. Here we formalize this analysis by identifying specific confounders for each embedding and testing whether the BCS--F1 relationship survives partial correlation controlling for these confounders.\ndocs/paper/main.tex:274:For each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:\ndocs/paper/main.tex:276:\\item \\textbf{MiniLM}: BCS correlates with log type frequency ($r = 0.201$). Frequent types have more training signal and are extracted more reliably, which produces the positive BCS--F1 association.\ndocs/paper/main.tex:277:\\item \\textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors, central, well-represented types that the model extracts well.\ndocs/paper/main.tex:281:Table~\\ref{tab:residualized_bcs} reports raw Spearman $\\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.\ndocs/paper/main.tex:286:\\caption{MAVEN per-type BCS--F1 correlation before and after controlling for centrality confounders. Raw correlations are Spearman $\\rho$; partial correlations are Pearson $r$ from residualized regression. Degree centrality is computed on the SCS graph at threshold 0.7. All values from experiment \\texttt{exp\\_maven\\_residualized\\_bcs}.}\ndocs/paper/main.tex:305:[Omitted long matching line]\ndocs/paper/main.tex:307:[Omitted long matching line]\ndocs/paper/main.tex:312:To rule out degree centrality as a confound in cross-domain datasets, we compute partial correlations between BCS and accuracy controlling for batch mean degree centrality (mean off-diagonal SCS per type, averaged across batch members).\ndocs/paper/main.tex:317:\\caption{BCS--accuracy partial correlation controlling for degree centrality. FewRel shows minimal attenuation (VIF${}\\,=\\,1.18$, low collinearity). DocRED shows high BCS--centrality collinearity (VIF${}\\,=\\,50.9$, $r = 0.99$), but the partial correlation remains highly significant.}\ndocs/paper/main.tex:329:[Omitted long matching line]\ndocs/paper/main.tex:332:[Omitted long matching line]\ndocs/paper/main.tex:334:\\subsection{NER BCS-Null Power Analysis}\ndocs/paper/main.tex:337:[Omitted long matching line]\ndocs/paper/main.tex:342:[Omitted long matching line]\ndocs/paper/main.tex:344:\\subsection{Domain Distribution in Extreme-BCS Batches}\ndocs/paper/main.tex:347:[Omitted long matching line]\ndocs/paper/main.tex:360:\\textbf{Condition} & \\textbf{Accuracy} & \\textbf{Mean BCS} \\\\\ndocs/paper/main.tex:379:[Omitted long matching line]\ndocs/paper/main.tex:382:[Omitted long matching line]\ndocs/paper/main.tex:385:[Omitted long matching line]\ndocs/paper/main.tex:387:\\subsection{Cross-Prompt-Variant BCS Correlation}\ndocs/paper/main.tex:390:To verify that the BCS--accuracy relationship is not an artifact of a specific prompt template, we evaluate four structurally distinct prompt variants on FewRel 80-relation RE at two count levels (8 and 32), with 10 random batches per condition (Table~\\ref{tab:prompt_variants}).\ndocs/paper/main.tex:395:\\caption{BCS--accuracy Pearson correlation across four prompt variants. At count 32, all four variants show negative BCS--accuracy correlations ($r \\leq -0.47$), with two reaching $p < 0.05$. At count 8, the narrower BCS range reduces statistical power.}\ndocs/paper/main.tex:413:[Omitted long matching line]\ndocs/paper/main.tex:415:\\section{BCS Aggregation Sensitivity}\ndocs/paper/main.tex:418:We define Batch Confusability Score (BCS) as the \\emph{mean} pairwise SCS across all type pairs in a batch (\\S\\ref{sec:bcs_controlled}). An alternative definition takes the \\emph{maximum} pairwise SCS within each batch to capture the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice (Table~\\ref{tab:bcs_aggregation}).\ndocs/paper/main.tex:423:\\caption{BCS--accuracy regression under mean vs.\\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p \\approx 0.60$; MAX $p \\approx 0.44$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}\ndocs/paper/main.tex:441:\\section{BCS-Controlled Detailed Results}\ndocs/paper/main.tex:447:\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\ndocs/paper/main.tex:452:\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\ndocs/paper/main.tex:462:DocRED regressions (\\S\\ref{sec:bcs_controlled}) use OLS on $n = 55$ batches (15 high-BCS + 15 low-BCS + 25 random) per count level, with one predictor. At count 16, adjusted $R^2 = 0.646$ (unadjusted: 0.653; 95\\% CI [0.53, 0.77]); at count 32, adjusted $R^2 = 0.606$ (unadjusted: 0.614; 95\\% CI [0.47, 0.75]). The small shrinkage ($\\Delta R^2 \\leq 0.01$) indicates the unadjusted values are not inflated by the predictor-to-sample ratio.\ndocs/paper/main.tex:467:To test whether the BCS--accuracy relationship depends on the output format, we run both constrained (enum-based) and unconstrained (free-text) decoding on the same 25 batch type sets from the FewRel 80-relation pool (13 low-BCS, 12 high-BCS; count 8). Each batch uses identical instances and type sets; only the decoding format differs (Table~\\ref{tab:format_independence}).\ndocs/paper/main.tex:472:\\caption{Paired comparison of constrained vs.\\ unconstrained decoding on 25 identical FewRel batch type sets. Both formats yield virtually identical BCS--accuracy correlations (Fisher $z \\approx 0$), confirming the confusability effect is format-independent. Mean accuracy is also unchanged ($\\Delta = -0.08$\\,pp), ruling out a format-driven accuracy shift.}\ndocs/paper/main.tex:479:Pearson $r$ (BCS vs.\\ acc) & $-$0.448 ($p = 0.025$) & $-$0.439 ($p = 0.028$) \\\\\ndocs/paper/main.tex:480:Spearman $\\rho$ (BCS vs.\\ acc) & $-$0.157 ($p = 0.455$) & $-$0.144 ($p = 0.492$) \\\\\ndocs/paper/main.tex:489:[Omitted long matching line]\ndocs/paper/main.tex:497:\\caption{Per-batch accuracy (\\%) under constrained and unconstrained decoding on 25 identical FewRel batch type sets (count 8, 96 instances each). 23/25 batches yield identical accuracy; the two exceptions differ by exactly one sample ($\\Delta = -1.04$\\,pp). L = low-BCS, H = high-BCS.}\ndocs/paper/main.tex:502:\\textbf{Batch} & \\textbf{Group} & \\textbf{BCS} & \\textbf{Constr.} & \\textbf{Unconstr.} & \\textbf{$\\Delta$} \\\\\ndocs/paper/main.tex:537:A potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol.\ndocs/paper/main.tex:542:\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\ndocs/paper/main.tex:547:& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\ndocs/paper/main.tex:556:\\multicolumn{7}{l}{\\footnotesize $^\\dagger$BCS range (IQR\\,=\\,0.033) insufficient for regression; slope not interpretable.} \\\\\ndocs/paper/main.tex:561:The within-pool slope ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.509; permutation $p \\approx 0.60$). The smaller quartile gap ($-$3.92\\,pp vs.\\ $-$5.31\\,pp) reflects the narrower BCS range within the 80-relation pool (Appendix~\\ref{sec:appendix_within_pool}).\ndocs/paper/main.tex:563:In the full 80-relation condition, natural BCS variation is insufficient (IQR${}=0.033$) to yield a detectable effect ($n=25$, slope${}=+0.221$, $p \\approx 0.76$). This does not invalidate the confusability effect; the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied, but establishes that natural schema sampling at this scale does not produce sufficient BCS contrast for detection.\ndocs/paper/main.tex:565:\\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}\ndocs/paper/main.tex:568:Table~\\ref{tab:scs-ablation} compares predictive accuracy of name-only SCS against name+definition SCS across three datasets.\ndocs/paper/main.tex:573:\\caption{Pearson correlation between SCS and empirical confusion rate. ``Def'' concatenates type name with definition before embedding. All correlations significant ($p < 0.001$). The inconsistent direction of $\\Delta r$ indicates that definitions provide no systematic benefit.}\ndocs/paper/main.tex:577:Dataset & SCS$_\\text{name}$ $r$ & SCS$_\\text{def}$ $r$ & $\\Delta r$ & Matrix corr. \\\\\ndocs/paper/main.tex:586:Few-NERD is the only dataset whose prompts include type definitions; for MAVEN and FewRel, prompts use type names alone, so name-only SCS directly matches model input. The high matrix correlation (0.66--0.89) confirms that type names capture the dominant semantic structure.\ndocs/paper/main.tex:590:From the 80-type confusion matrix, we extract the $\\binom{16}{2} = 120$ pairs among the 16 validation-origin types (fully disjoint from the 64 training-pool types). The SCS--confusion Spearman correlation remains positive and significant ($\\rho = 0.216$, $p = 0.018$), nearly identical to the full 80-type pool ($\\rho = 0.218$, $p < 0.001$, $n = 3{,}160$ pairs), ruling out training-set contamination as the driver of the observed relationship.\ndocs/paper/main.tex:597:[Omitted long matching line]\ndocs/paper/main.tex:602:[Omitted long matching line]\ndocs/paper/main.tex:605:The inter-pair SCS correlation $\\rho = 0.35$ is estimated from pairs sharing a common type. At $\\rho = 0.20$ (halved correlation), a parallel simulation yields batch $R^2 \\approx 0.22$; at $\\rho = 0.50$, the correlation structure approaches the positive-definiteness boundary; $\\rho = 0.35$ thus sits in a stable regime. The simulation is illustrative; the pooled semipartial $R^2 = 0.273$ (\\S\\ref{sec:bcs_controlled}) is the primary evidence.\ndocs/paper/main.tex:608:[Omitted long matching line]\ndocs/paper/main.tex:610:\\section{BCS Independence from Type Composition}\ndocs/paper/main.tex:613:[Omitted long matching line]\ndocs/paper/main.tex:615:\\section{SCS vs.\\ Simple Baselines}\ndocs/paper/main.tex:618:Table~\\ref{tab:scs_baselines} compares SCS against simple baselines for pairwise confusion prediction.\ndocs/paper/main.tex:623:\\caption{Pairwise confusion prediction: SCS vs.\\ simple baselines. Spearman $\\rho$ between each metric and the empirical confusion rate. SCS outperforms all baselines on FewRel; the margin is smaller on Few-NERD, where hierarchical naming conventions provide partial signal to string-based metrics. $^\\dagger$42\\% of pairs lack WordNet coverage.}\ndocs/paper/main.tex:630:FewRel & SCS (embedding) & \\textbf{0.218} & $< 0.001$ \\\\\ndocs/paper/main.tex:635:Few-NERD & SCS (embedding) & \\textbf{0.166} & $< 0.001$ \\\\\ndocs/paper/main.tex:646:FewRel combines 64 train-split and 16 val-split relation types into a single 80-type pool.  Train-origin types show numerically lower accuracy ($-8.8$\\,pp, $p = 0.06$; see Limitations), raising the question of whether differential pre-training exposure confounds the BCS--accuracy relationship.  We test this by adding a per-batch \\emph{train-origin ratio} (fraction of relation types drawn from the train split) as a covariate in the BCS--accuracy regression.\ndocs/paper/main.tex:650:\\text{acc} = \\beta_0 + \\beta_{\\text{BCS}} \\!\\cdot\\! \\text{BCS} + \\beta_{\\text{orig}} \\!\\cdot\\! \\text{train\\_origin\\_ratio} + \\varepsilon\ndocs/paper/main.tex:653:\\paragraph{Results.}  The BCS partial effect is unchanged after controlling for split-origin: $\\beta_{\\text{BCS}} = -0.416$, $p < 0.001$ (vs.\\ $\\beta = -0.412$, $p < 0.001$ without the covariate).  Train-origin ratio is not independently significant ($\\beta_{\\text{origin}} = -0.057$, $p = 0.245$), and $\\Delta R^2 = 0.005$.  The BCS--accuracy relationship is therefore not confounded by differential pre-training exposure at the batch level.\ndocs/paper/main.tex:655:Pairwise SCS distributions do not differ significantly between train-origin (64 types, mean\\,=\\,0.880) and val-origin (16 types, mean\\,=\\,0.874) subsets (Mann-Whitney $p = 0.754$, Cohen's $d = 0.081$); the train/val split does not introduce systematic confusability bias.\ndocs/paper/main.tex:685:[Omitted long matching line]\ndocs/paper/main.tex:690:To test whether the two-dimensional degradation pattern generalizes across models, we replicate the count-curve and BCS-controlled experiments on Meta-LLaMA-3.1-70B-Instruct (FP8 quantization). All batch compositions, type pools, and test samples are identical to those used for Qwen3-32B (\\S\\ref{sec:count_curves}, \\S\\ref{sec:bcs_controlled}).\ndocs/paper/main.tex:723:For the confusability dimension (Dimension 2), at count 16 on FewRel, LLaMA-70B achieves low-BCS accuracy of 0.708 versus high-BCS accuracy of 0.599 ($\\Delta = +10.9$\\,pp, 95\\% CI [$+$3.0, $+$20.1]). The confidence interval excludes zero; the confusability effect is thus confirmed at the 70B scale.\ndocs/paper/main.tex:730:We validate both dimensions on a proprietary model, Gemini 2.5 Flash \\citep{gemini-2025}, accessed via API. This extends the cross-model evidence from open-weight families (Qwen, LLaMA) to a proprietary architecture with unknown training details. We replicate the FewRel count-curve and BCS-controlled experiments using the same 960 balanced samples, batch compositions, and evaluation protocol as Qwen3-32B.\ndocs/paper/main.tex:753:\\paragraph{Dimension~2: BCS-controlled confusability.}\ndocs/paper/main.tex:754:We replicate the BCS-controlled experiment on Gemini 2.5 Flash using extreme-BCS batches at count 8 ($n = 50$; 25 low-BCS, 25 high-BCS) and count 16 ($n = 10$; 5+5).\ndocs/paper/main.tex:756:[Omitted long matching line]\ndocs/paper/main.tex:758:Table~\\ref{tab:cross_model_bcs_summary} summarizes BCS-controlled results across all validated models. Both dimensions thus replicate on a proprietary architecture with unknown training details.\ndocs/paper/main.tex:763:\\caption{Cross-model BCS-controlled FewRel RE summary. All models show significant low-vs-high BCS accuracy gaps. Gap magnitude varies with model capacity (ceiling compression), but the direction is consistent across open-weight (8B--70B) and proprietary architectures.}\ndocs/paper/main.tex:767:\\textbf{Model} & \\textbf{Count} & \\textbf{Low BCS} & \\textbf{High BCS} & \\textbf{$\\Delta$} & \\textbf{95\\% CI} \\\\\ndocs/paper/main.tex:781:[Omitted long matching line]\ndocs/paper/main.tex:786:\\caption{BCS gap under few-shot prompting (FewRel, count 8). Demonstrations improve absolute accuracy on low-BCS batches (+3.3--7.2\\,pp over 0-shot) but provide inconsistent benefit on high-BCS batches (+5.6\\,pp at 1-shot, $-$1.0\\,pp at 5-shot). The confusability gap widens from +18.5\\,pp (0-shot) to +22.8\\,pp (5-shot). All metrics are micro-averaged across batches.}\ndocs/paper/main.tex:790:\\textbf{Condition} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\ndocs/paper/main.tex:799:[Omitted long matching line]\ndocs/paper/main.tex:806:Tables~\\ref{tab:top10_re} and~\\ref{tab:top10_ner} list the ten most frequently confused type pairs on FewRel 80-relation RE and Few-NERD NER. Confusion counts are aggregated bidirectionally across three random seeds (72{,}000 predictions per seed for RE; single-seed 66-type extraction for NER). Table~\\ref{tab:error_examples} provides illustrative confusion instances with SCS values.\ndocs/paper/main.tex:811:[Omitted long matching line]\ndocs/paper/main.tex:815:\\textbf{\\#} & \\textbf{Type A} & \\textbf{Type B} & \\textbf{SCS} & \\textbf{$N$} \\\\\ndocs/paper/main.tex:834:[Omitted long matching line]\ndocs/paper/main.tex:838:\\textbf{\\#} & \\textbf{Type A} & \\textbf{Type B} & \\textbf{SCS} & \\textbf{$N$} \\\\\ndocs/paper/main.tex:857:\\caption{Illustrative confusion instances from FewRel 80-rel RE. All gold-predicted pairs have SCS\\,$>$\\,0.90: \\textit{participant} vs.\\ \\textit{participant of} reverses directionality; \\textit{contains} vs.\\ \\textit{located in} inverts containment; \\textit{part of} vs.\\ \\textit{member of} conflates meronymy with membership. a.t.e.\\ = admin.\\ territorial entity.}\ndocs/paper/main.tex:861:\\textbf{Sentence} & \\textbf{Gold} & \\textbf{Pred.} & \\textbf{SCS} \\\\\ndocs/paper/main.tex:875:[Omitted long matching line]\ndocs/paper/main.tex:880:\\caption{Accuracy (\\%) under original vs.\\ renamed labels on FewRel count-8 batches. Renaming reduced embedding similarity but decreased accuracy in both groups, with a larger drop on high-BCS batches (Cohen's $d = -2.92$) than low-BCS ($d = -1.09$). Interaction: $\\Delta_{\\text{high}} - \\Delta_{\\text{low}} = -5.9$\\,pp ($t = -7.23$, $p < 0.001$).}\ndocs/paper/main.tex:886:Low-BCS ($n=25$)  & 90.1 & 87.1 & $-$3.0 \\\\\ndocs/paper/main.tex:887:High-BCS ($n=25$) & 69.3 & 60.5 & $-$8.8 \\\\\ndocs/paper/main.tex:897:To test whether exact-match F1 masks the BCS signal in NER by conflating boundary errors with type errors, we evaluate three progressively relaxed matching criteria on the full Few-NERD NER dataset ($n = 450$ batches: 6 count levels $\\times$ 25 batches $\\times$ 3 seeds; Table~\\ref{tab:relaxed_matching}).\ndocs/paper/main.tex:902:[Omitted long matching line]\ndocs/paper/main.tex:916:A per-error-mode analysis confirms this null extends to all individual categories: miss ($\\rho = 0.017$), boundary ($\\rho = -0.043$), and type substitution ($\\rho = -0.010$) rates show no BCS association (all $p > 0.3$, $n = 450$). The null holds within each count level (count 2: $r = 0.022$; count 6: $r = 0.110$; count 12: $r = 0.028$; all $p > 0.3$), ruling out count as a confound.\ndocs/paper/checklist.tex:15:Yes (Limitations). SCS/BCS may be misused as a standalone deployment criterion. Since they are proxies for confusability and do not capture domain-specific ambiguity or downstream harms, they should be used for diagnostic monitoring rather than automatic schema rejection or high-stakes deployment decisions.\ndocs/paper/checklist.tex:49:Yes. Table~\\ref{tab:datasets} reports type counts, evaluation unit counts, domain characteristics, and BCS ranges for each dataset. \\S\\ref{sec:datasets} describes dataset provenance and sampling procedures.\ndocs/paper/checklist.tex:67:Yes. \\S\\ref{sec:exp_design} describes both experimental paradigms (count curves and BCS-controlled). \\S\\ref{sec:model} reports decoding parameters (greedy, temperature${}=0$, seed${}=42$) and prompt versions. No hyperparameter search was conducted as this is a zero-shot evaluation study.\ndocs/paper/discussion.tex:6:The confusability signal applies to cross-domain schemas; same-domain schemas exhibit centrality confounding (\\S\\ref{sec:centrality_confound}). Modest pairwise $r^2$ compounds at the batch level because correlated type interactions aggregate within shared prompts (\\S\\ref{sec:bcs_controlled}). The NER--RE asymmetry reflects dispersed error modes and compressed BCS variance (Appendix~\\ref{sec:appendix_ner_power}).\ndocs/paper/discussion.tex:10:[Omitted long matching line]\ndocs/paper/discussion.tex:15:[Omitted long matching line]\ndocs/paper/abstract.tex:2:[Omitted long matching line]\ndocs/paper/abstract.tex:3:(1)~count degradation spans all three tasks (up to $-$49\\,pp); inter-type confusability (measured by BCS) independently predicts RE type substitution errors (VIF${}\\,=\\,1.18$ on FewRel);\ndocs/paper/abstract.tex:4:(2)~BCS independently explains ${\\sim}$27\\% of cross-batch RE accuracy variance on FewRel (semipartial $R^2 = 0.273$ after controlling for degree centrality; VIF${}\\,=\\,1.18$), replicating across three open-weight model families (8B--70B); the NER batch-level null serves as a boundary condition (dispersed error modes, BCS range compression);\ndocs/paper/experimental_setup.tex:13:[Omitted long matching line]\ndocs/paper/experimental_setup.tex:21:Table~\\ref{tab:datasets} summarizes the dataset statistics, including the Schema Confusability Score (SCS) ranges defined in \\S\\ref{sec:scs}.\ndocs/paper/experimental_setup.tex:29:\\textbf{Dataset} & \\textbf{Task} & \\textbf{\\# Types} & \\textbf{\\# Eval Units} & \\textbf{Domain} & \\textbf{BCS Range} & \\textbf{Embedding} \\\\\ndocs/paper/experimental_setup.tex:37:\\caption{Dataset statistics. BCS Range: min--max over count-curve batches. Embedding: model used for SCS/BCS; ranges are not comparable across embedding models. $^\\dagger$Trigger mentions across 8{,}042 sentences.}\ndocs/paper/experimental_setup.tex:41:\\subsection{Schema Confusability Score (SCS)}\ndocs/paper/experimental_setup.tex:45:We define the Schema Confusability Score (SCS) to quantify semantic overlap between types in a schema. Given a type $t$ with name string $\\text{name}(t)$, an embedding function $\\text{embed}(\\cdot)$ maps the type name to a vector representation. The \\textbf{pairwise SCS} between types $t_i$ and $t_j$ is:\ndocs/paper/experimental_setup.tex:48:\\text{SCS}(t_i, t_j) = \\cos\\bigl(\\text{embed}(\\text{name}(t_i)),\\; \\text{embed}(\\text{name}(t_j))\\bigr)\ndocs/paper/experimental_setup.tex:52:For a batch of types $B = \\{t_1, \\ldots, t_k\\}$, the \\textbf{Batch Confusability Score (BCS)} aggregates all pairwise similarities:\ndocs/paper/experimental_setup.tex:54:\\text{BCS}(B) = \\frac{1}{\\binom{k}{2}} \\sum_{i < j,\\; t_i, t_j \\in B} \\text{SCS}(t_i, t_j)\ndocs/paper/experimental_setup.tex:57:[Omitted long matching line]\ndocs/paper/experimental_setup.tex:59:\\paragraph{SCS as a lightweight proxy.}\ndocs/paper/experimental_setup.tex:61:SCS is a pre-hoc proxy computable without running extraction; pairwise correlations with observed type confusion are reported in \\S\\ref{sec:pairwise}. SCS does not capture context-dependent disambiguation or mention-level ambiguity; these contribute to residual variance.\ndocs/paper/experimental_setup.tex:74:[Omitted long matching line]\ndocs/paper/experimental_setup.tex:86:\\paragraph{Experiment 2: BCS-Controlled.}\ndocs/paper/experimental_setup.tex:87:[Omitted long matching line]\ndocs/paper/introduction.tex:10:This study combines correlational analyses with quasi-experimental manipulation (BCS-controlled batches) to characterize how schema properties predict extraction accuracy.\ndocs/paper/introduction.tex:15:[Omitted long matching line]\ndocs/paper/introduction.tex:19:(2)~Pairwise SCS predicts type confusion across NER, RE, and ED (\\S\\ref{sec:pairwise}); at batch level, BCS predicts RE accuracy independent of output format (\\S\\ref{sec:bcs_controlled}) but not NER accuracy at current statistical power; per-type aggregation is confounded by centrality on homogeneous schemas (\\S\\ref{sec:centrality_confound}).\ndocs/paper/introduction.tex:24:[Omitted long matching line]\ndocs/paper/introduction.tex:25:    \\item We document a task-dependent boundary: the RE confusability effect is confirmed as format-independent across three model families, while the NER batch-level BCS null---reported as a boundary condition rather than a negative result---is attributable to dispersed error modes (miss, boundary, type) and BCS range compression (\\S\\ref{sec:bcs_controlled}, \\S\\ref{sec:multi_channel}).\ndocs/paper/results.tex:10:[Omitted long matching line]\ndocs/paper/results.tex:15:We test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate (the fraction of $t_i$ gold instances misclassified as $t_j$) and correlate it with $\\text{SCS}(t_i, t_j)$. Table~\\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\\% CIs.\ndocs/paper/results.tex:29:\\caption{Pairwise SCS--confusion correlation. Confusion rate is bidirectional $C(t_i{\\to}t_j) + C(t_j{\\to}t_i)$ divided by gold frequency sum; CIs are percentile bootstrap ($B{=}10{,}000$). FewRel ($r = 0.187$; \\S\\ref{sec:scs-validation}) excluded (per-instance RE format). Type-level cluster bootstrap CIs exclude zero (Few-NERD [0.069, 0.219]; MAVEN [0.081, 0.185]).}\ndocs/paper/results.tex:37:[Omitted long matching line]\ndocs/paper/results.tex:42:\\caption{Error taxonomy decomposition (Few-NERD NER and FewRel RE). IntraSub scales monotonically with BCS across all evaluated datasets ($\\rho = 0.84\\text{--}1.0$; Table~\\ref{tab:error_taxonomy} includes DocRED). RE missed rates remain flat (10--16\\%), but NER missed rates are substantially higher (43--65\\%) and non-monotonic.}\ndocs/paper/results.tex:46:\\subsection{BCS-Controlled Experiments}\ndocs/paper/results.tex:50:[Omitted long matching line]\ndocs/paper/results.tex:52:[Omitted long matching line]\ndocs/paper/results.tex:55:[Omitted long matching line]\ndocs/paper/results.tex:59:Within-pool analysis confirms slope consistency across pools (permutation $p \\approx 0.60$; Appendix~\\ref{app:within-pool-method}). The 80-relation extreme-batch gap (\\S\\ref{sec:bcs_controlled}) reflects wider BCS range, not stronger per-unit sensitivity.\ndocs/paper/results.tex:64:[Omitted long matching line]\ndocs/paper/results.tex:68:[Omitted long matching line]\ndocs/paper/results.tex:72:[Omitted long matching line]\ndocs/paper/results.tex:78:[Omitted long matching line]\ndocs/paper/results.tex:81:[Omitted long matching line]\ndocs/paper/results.tex:86:[Omitted long matching line]\ndocs/paper/sdgd_negative.tex:5:[Omitted long matching line]",
      "numLines": 161,
      "startLine": 1,
      "totalLines": 161
    }
  }
}
```

</details>

---

### Assistant

_source line 30_

<details><summary>Logged reasoning block</summary>

```text
This is very extensive. Let me categorize what I see:

In `docs/paper/` (the main paper), BCS and SCS are overwhelmingly used as **plain uppercase text** — `BCS`, `SCS`, `\text{BCS}`, `\text{SCS}` (the latter in math mode). There's no `\textsc{bcs}` or `\textsc{scs}` usage in the docs/paper/ files.

Let me check the artifacts/ files to see if there are `\textsc` usages.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "25f01df2-f480-4dd6-ae82-4c8c9c2f69e5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ML1cC8U9MNdjpmdAFoKufv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10647,
      "cache_read_input_tokens": 34768,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10647
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 31_

Let me check for `\textsc{bcs}` and `\textsc{scs}` specifically in docs/paper/.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "5e5f5473-c602-4169-a598-e4a32f9cf6ff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ML1cC8U9MNdjpmdAFoKufv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10647,
      "cache_read_input_tokens": 34768,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10647
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Grep · `toolu_01NF83ezzW4zwNKMXU8DMYR7`</summary>

```json
{
  "pattern": "\\\\textsc\\{[Bb][Cc][Ss]\\}|\\\\textsc\\{[Ss][Cc][Ss]\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "f998e994-c768-442f-a24d-c68c47484298",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ML1cC8U9MNdjpmdAFoKufv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10647,
      "cache_read_input_tokens": 34768,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10647
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-22T11:10:14.457Z_

<details><summary>↩ Tool result · `toolu_01NF83ezzW4zwNKMXU8DMYR7`</summary>

```text
docs/paper/main.tex:332:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "1e2da09e-29ed-4692-85a5-d664823ccd2f",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/main.tex:332:[Omitted long matching line]",
    "numLines": 1
  }
}
```

</details>

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Grep · `toolu_016nyUoqtFwZKUS6xDEBPDg3`</summary>

```json
{
  "pattern": "\\\\textsc\\{[Bb][Cc][Ss]\\}|\\\\textsc\\{[Ss][Cc][Ss]\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "191be78a-fa77-4043-897b-1eb07572f449",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ML1cC8U9MNdjpmdAFoKufv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10647,
      "cache_read_input_tokens": 34768,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10647
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-22T11:10:15.624Z_

<details><summary>↩ Tool result · `toolu_016nyUoqtFwZKUS6xDEBPDg3`</summary>

```text
artifacts/docred_ridge_appendix.tex:7:The standardized BCS coefficient is $\hat{\beta}_{\textsc{bcs}} = -1.53$
artifacts/docred_ridge_appendix.tex:9:An analytic derivation shows that $\hat{\beta}_{\textsc{bcs}} < 0$ for
artifacts/_project/paper/docred_ridge_appendix.tex:7:The standardized BCS coefficient is $\hat{\beta}_{\textsc{bcs}} = -1.53$
artifacts/_project/paper/docred_ridge_appendix.tex:9:An analytic derivation shows that $\hat{\beta}_{\textsc{bcs}} < 0$ for
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "da0bf0eb-1765-4f65-8c98-244bd1edadd7",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/docred_ridge_appendix.tex:7:The standardized BCS coefficient is $\\hat{\\beta}_{\\textsc{bcs}} = -1.53$\nartifacts/docred_ridge_appendix.tex:9:An analytic derivation shows that $\\hat{\\beta}_{\\textsc{bcs}} < 0$ for\nartifacts/_project/paper/docred_ridge_appendix.tex:7:The standardized BCS coefficient is $\\hat{\\beta}_{\\textsc{bcs}} = -1.53$\nartifacts/_project/paper/docred_ridge_appendix.tex:9:An analytic derivation shows that $\\hat{\\beta}_{\\textsc{bcs}} < 0$ for",
    "numLines": 4
  }
}
```

</details>

---

### Assistant

_source line 36_

Let me read the specific lines in main.tex that use `\textsc`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "8da84603-2113-4bc3-a7b4-e256feb11c1a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AZzrU2BwHq57ZspjocvLpL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 769,
      "cache_read_input_tokens": 45415,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 769
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Read · `toolu_01Hq66c3xHYr6FMPqbsf6URd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": 325,
  "limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "d567d256-fd2d-486f-9ee4-a9facb59d8ee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AZzrU2BwHq57ZspjocvLpL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 769,
      "cache_read_input_tokens": 45415,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 769
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-22T11:10:18.625Z_

<details><summary>↩ Tool result · `toolu_01Hq66c3xHYr6FMPqbsf6URd`</summary>

```text
325	\bottomrule
326	\end{tabular}
327	\end{table}
328	
329	As Table~\ref{tab:partial_corr} shows, on FewRel, BCS and degree centrality are only moderately correlated ($r = 0.39$), and the BCS effect survives nearly intact after partialling ($r_{\text{partial}} = -0.537$ vs.\ $r_{\text{zero}} = -0.570$; semipartial $R^2 = 0.273$). On DocRED, the near-perfect BCS--centrality correlation ($r = 0.99$) makes it impossible to fully separate the two predictors; the significant partial correlation ($p < 0.001$) indicates BCS retains predictive value but does not uniquely identify the causal channel. This contrasts with MAVEN (\S\ref{sec:appendix_residualized_bcs}), where the BCS signal vanishes after controlling for centrality.
330	
331	\paragraph{Ridge regression under multicollinearity.}
332	Ridge regression (GCV, $\lambda = 0.001$) on the 110 DocRED batches confirms the negative direction of the BCS--accuracy relationship even after regularizing for the severe BCS--centrality multicollinearity (VIF$\,\approx\,$50.9). The standardized BCS coefficient is $\hat{\beta}_{\textsc{bcs}} = -1.53$ ($\hat{\beta}_{\text{centrality}} = 0.78$, $R^2 = 0.594$). An analytic derivation shows that $\hat{\beta}_{\textsc{bcs}} < 0$ for \emph{all} $\lambda \geq 0$: the numerator of the closed-form ridge solution, $-(1{+}\lambda) \times 0.760 + 0.727$, is negative at $\lambda{=}0$ and monotonically decreasing thereafter. Given the shrinkage bias inherent to ridge estimation, we interpret only the sign---not the magnitude---of the BCS coefficient as directional evidence that higher schema confusability degrades extraction accuracy, independent of degree centrality.
333	
334	\subsection{NER BCS-Null Power Analysis}
335	\label{sec:appendix_ner_power}
336	
337	The Few-NERD BCS-null may reflect insufficient BCS variance rather than a genuine absence of the BCS--accuracy relationship. Few-NERD's BCS standard deviation (0.027) is only 19\% of FewRel's (0.141); FewRel's observed $r = -0.570$ would attenuate to $r = -0.111$ under this restricted range, yielding 65\% power at $n = 450$ (below the conventional 80\% threshold). The minimum detectable $|r|$ at 80\% power is 0.132. This analysis characterizes the NER result as absence of evidence (insufficient power at the attenuated effect size) rather than evidence of absence.
338	
339	\subsection{Bootstrap CI Robustness}
340	\label{sec:appendix_bootstrap_ci}
341	
342	Because batches in the FewRel experiments are constructed by sampling relation types from a shared pool, different batches may share text instances of the same type, potentially inducing residual dependence that makes standard bootstrap CIs anti-conservative. We assess this concern via cluster-robust inference. We cluster the $n = 164$ FewRel batches by instance-weighted type overlap (hierarchical clustering, complete linkage) and compute cluster-robust standard errors. Across six overlap thresholds (Jaccard distance $\in \{0.1, \ldots, 0.9\}$, yielding 80--83 clusters), the cluster-robust SE for the BCS regression slope is $0.96$--$0.97\times$ the OLS SE, and the slope remains highly significant ($p < 10^{-11}$). Cluster bootstrap CIs for $R^2$ show width changes of $-6\%$ to $+6\%$ relative to standard bootstrap CIs ($[0.14, 0.42]$ vs.\ $[0.15, 0.41]$). We conclude that the reported CIs are robust to the non-independence induced by shared text instances.
343	
344	\subsection{Domain Distribution in Extreme-BCS Batches}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "bf15ee8e-1b20-425a-9d60-efbc37f55441",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
      "content": "\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAs Table~\\ref{tab:partial_corr} shows, on FewRel, BCS and degree centrality are only moderately correlated ($r = 0.39$), and the BCS effect survives nearly intact after partialling ($r_{\\text{partial}} = -0.537$ vs.\\ $r_{\\text{zero}} = -0.570$; semipartial $R^2 = 0.273$). On DocRED, the near-perfect BCS--centrality correlation ($r = 0.99$) makes it impossible to fully separate the two predictors; the significant partial correlation ($p < 0.001$) indicates BCS retains predictive value but does not uniquely identify the causal channel. This contrasts with MAVEN (\\S\\ref{sec:appendix_residualized_bcs}), where the BCS signal vanishes after controlling for centrality.\n\n\\paragraph{Ridge regression under multicollinearity.}\nRidge regression (GCV, $\\lambda = 0.001$) on the 110 DocRED batches confirms the negative direction of the BCS--accuracy relationship even after regularizing for the severe BCS--centrality multicollinearity (VIF$\\,\\approx\\,$50.9). The standardized BCS coefficient is $\\hat{\\beta}_{\\textsc{bcs}} = -1.53$ ($\\hat{\\beta}_{\\text{centrality}} = 0.78$, $R^2 = 0.594$). An analytic derivation shows that $\\hat{\\beta}_{\\textsc{bcs}} < 0$ for \\emph{all} $\\lambda \\geq 0$: the numerator of the closed-form ridge solution, $-(1{+}\\lambda) \\times 0.760 + 0.727$, is negative at $\\lambda{=}0$ and monotonically decreasing thereafter. Given the shrinkage bias inherent to ridge estimation, we interpret only the sign---not the magnitude---of the BCS coefficient as directional evidence that higher schema confusability degrades extraction accuracy, independent of degree centrality.\n\n\\subsection{NER BCS-Null Power Analysis}\n\\label{sec:appendix_ner_power}\n\nThe Few-NERD BCS-null may reflect insufficient BCS variance rather than a genuine absence of the BCS--accuracy relationship. Few-NERD's BCS standard deviation (0.027) is only 19\\% of FewRel's (0.141); FewRel's observed $r = -0.570$ would attenuate to $r = -0.111$ under this restricted range, yielding 65\\% power at $n = 450$ (below the conventional 80\\% threshold). The minimum detectable $|r|$ at 80\\% power is 0.132. This analysis characterizes the NER result as absence of evidence (insufficient power at the attenuated effect size) rather than evidence of absence.\n\n\\subsection{Bootstrap CI Robustness}\n\\label{sec:appendix_bootstrap_ci}\n\nBecause batches in the FewRel experiments are constructed by sampling relation types from a shared pool, different batches may share text instances of the same type, potentially inducing residual dependence that makes standard bootstrap CIs anti-conservative. We assess this concern via cluster-robust inference. We cluster the $n = 164$ FewRel batches by instance-weighted type overlap (hierarchical clustering, complete linkage) and compute cluster-robust standard errors. Across six overlap thresholds (Jaccard distance $\\in \\{0.1, \\ldots, 0.9\\}$, yielding 80--83 clusters), the cluster-robust SE for the BCS regression slope is $0.96$--$0.97\\times$ the OLS SE, and the slope remains highly significant ($p < 10^{-11}$). Cluster bootstrap CIs for $R^2$ show width changes of $-6\\%$ to $+6\\%$ relative to standard bootstrap CIs ($[0.14, 0.42]$ vs.\\ $[0.15, 0.41]$). We conclude that the reported CIs are robust to the non-independence induced by shared text instances.\n\n\\subsection{Domain Distribution in Extreme-BCS Batches}",
      "numLines": 20,
      "startLine": 325,
      "totalLines": 919
    }
  }
}
```

</details>

---

### Assistant

_source line 39_

Found the `\textsc{bcs}` usages. Now let me check the full scope. Let me also look at all `\textsc` usages in docs/paper that relate to BCS/SCS, and check if there are any in `\text{BCS}` format (math mode).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "fe0ab677-7983-4d2b-b691-17fddee299e5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NjKgzLNi2kSGNK8gUUTyZQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1213,
      "cache_read_input_tokens": 46184,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1213
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Grep · `toolu_01YFV4oxe4UeuHdLsh7tfEVL`</summary>

```json
{
  "pattern": "\\\\text\\{BCS\\}|\\\\text\\{SCS\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "b9f0bae7-d574-41f8-b3a4-8abefa87440e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NjKgzLNi2kSGNK8gUUTyZQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1213,
      "cache_read_input_tokens": 46184,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1213
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-22T11:10:28.647Z_

<details><summary>↩ Tool result · `toolu_01YFV4oxe4UeuHdLsh7tfEVL`</summary>

```text
docs/paper/main.tex:159:We construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\text{SCS}(t_i, t_j) > \tau$. Greedy graph coloring (\textsc{largest\_first}) assigns each type to a color such that no two adjacent (i.e., highly confusable) types share a color. Each color class forms one extraction batch, and predictions are merged via set union.
docs/paper/main.tex:382:[Omitted long matching line]
docs/paper/main.tex:597:[Omitted long matching line]
docs/paper/main.tex:613:[Omitted long matching line]
docs/paper/main.tex:650:\text{acc} = \beta_0 + \beta_{\text{BCS}} \!\cdot\! \text{BCS} + \beta_{\text{orig}} \!\cdot\! \text{train\_origin\_ratio} + \varepsilon
docs/paper/main.tex:653:\paragraph{Results.}  The BCS partial effect is unchanged after controlling for split-origin: $\beta_{\text{BCS}} = -0.416$, $p < 0.001$ (vs.\ $\beta = -0.412$, $p < 0.001$ without the covariate).  Train-origin ratio is not independently significant ($\beta_{\text{origin}} = -0.057$, $p = 0.245$), and $\Delta R^2 = 0.005$.  The BCS--accuracy relationship is therefore not confounded by differential pre-training exposure at the batch level.
docs/paper/experimental_setup.tex:48:\text{SCS}(t_i, t_j) = \cos\bigl(\text{embed}(\text{name}(t_i)),\; \text{embed}(\text{name}(t_j))\bigr)
docs/paper/experimental_setup.tex:54:\text{BCS}(B) = \frac{1}{\binom{k}{2}} \sum_{i < j,\; t_i, t_j \in B} \text{SCS}(t_i, t_j)
docs/paper/results.tex:15:We test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate (the fraction of $t_i$ gold instances misclassified as $t_j$) and correlate it with $\text{SCS}(t_i, t_j)$. Table~\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\% CIs.
docs/paper/results.tex:55:[Omitted long matching line]
docs/paper/results.tex:64:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "b12192df-ae2b-40e7-9220-728effadc9e3",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/main.tex:159:We construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent (i.e., highly confusable) types share a color. Each color class forms one extraction batch, and predictions are merged via set union.\ndocs/paper/main.tex:382:[Omitted long matching line]\ndocs/paper/main.tex:597:[Omitted long matching line]\ndocs/paper/main.tex:613:[Omitted long matching line]\ndocs/paper/main.tex:650:\\text{acc} = \\beta_0 + \\beta_{\\text{BCS}} \\!\\cdot\\! \\text{BCS} + \\beta_{\\text{orig}} \\!\\cdot\\! \\text{train\\_origin\\_ratio} + \\varepsilon\ndocs/paper/main.tex:653:\\paragraph{Results.}  The BCS partial effect is unchanged after controlling for split-origin: $\\beta_{\\text{BCS}} = -0.416$, $p < 0.001$ (vs.\\ $\\beta = -0.412$, $p < 0.001$ without the covariate).  Train-origin ratio is not independently significant ($\\beta_{\\text{origin}} = -0.057$, $p = 0.245$), and $\\Delta R^2 = 0.005$.  The BCS--accuracy relationship is therefore not confounded by differential pre-training exposure at the batch level.\ndocs/paper/experimental_setup.tex:48:\\text{SCS}(t_i, t_j) = \\cos\\bigl(\\text{embed}(\\text{name}(t_i)),\\; \\text{embed}(\\text{name}(t_j))\\bigr)\ndocs/paper/experimental_setup.tex:54:\\text{BCS}(B) = \\frac{1}{\\binom{k}{2}} \\sum_{i < j,\\; t_i, t_j \\in B} \\text{SCS}(t_i, t_j)\ndocs/paper/results.tex:15:We test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate (the fraction of $t_i$ gold instances misclassified as $t_j$) and correlate it with $\\text{SCS}(t_i, t_j)$. Table~\\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\\% CIs.\ndocs/paper/results.tex:55:[Omitted long matching line]\ndocs/paper/results.tex:64:[Omitted long matching line]",
    "numLines": 11
  }
}
```

</details>

---

### Assistant

_source line 42_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture. Let me summarize:

**Main paper files (docs/paper/):**
- The vast majority uses plain `BCS` and `SCS` in text mode
- In math mode, uses `\text{BCS}` and `\text{SCS}` (correct for math context)
- Uses `$\beta_{\text{BCS}}$` subscripts (correct)
- **Exception**: Line 332 of main.tex uses `\textsc{bcs}` twice: `$\hat{\beta}_{\textsc{bcs}} = -1.53$` and `$\hat{\beta}_{\textsc{bcs}} < 0$`


- The same `\textsc{bcs}` pattern appears in the artifact files at lines 7 and 9 of both the main and project versions of the appendix

So the standard approach is plain `BCS`/`SCS` in text and `\text{BCS}`/`\text{SCS}` in math mode, with just a few instances using `\textsc{bcs}` as math subscripts that stand out from the rest.

I need to standardize those outliers by replacing `\textsc{bcs}` with `\text{BCS}` in the subscripts to align with the dominant convention. I should focus on updating files in `docs/paper/` since the `artifacts/` directory likely contains generated or archived versions that shouldn't be touched unless they're actively referenced by the main document.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "32c9bbcd-ccf7-4b90-85ec-f891870d8aa8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XTqvcKCb3CSbS54DcB37Rm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1057,
      "cache_read_input_tokens": 47397,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1057
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 43_

The pattern is clear. The dominant format is plain `BCS`/`SCS` in text and `\text{BCS}`/`\text{SCS}` in math mode. The only outlier is `\textsc{bcs}` appearing twice on line 332 of main.tex (in math subscripts). Let me fix it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "bf9e0ad3-2e39-4a14-91f7-81f5a9ce6310",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XTqvcKCb3CSbS54DcB37Rm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1057,
      "cache_read_input_tokens": 47397,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1057
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 44_

<details open><summary>🔧 Tool call — Edit · `toolu_01C3n6p3UVN1tBAtAbZL2E9n`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "old_string": "$\\hat{\\beta}_{\\textsc{bcs}} = -1.53$ ($\\hat{\\beta}_{\\text{centrality}} = 0.78$, $R^2 = 0.594$). An analytic derivation shows that $\\hat{\\beta}_{\\textsc{bcs}} < 0$",
  "new_string": "$\\hat{\\beta}_{\\text{BCS}} = -1.53$ ($\\hat{\\beta}_{\\text{centrality}} = 0.78$, $R^2 = 0.594$). An analytic derivation shows that $\\hat{\\beta}_{\\text{BCS}} < 0$"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "5484c1a8-2c8d-4151-b4dd-710fe6b46c9f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XTqvcKCb3CSbS54DcB37Rm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1057,
      "cache_read_input_tokens": 47397,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1057
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-22T11:10:44.134Z_

<details><summary>↩ Tool result · `toolu_01C3n6p3UVN1tBAtAbZL2E9n`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "710a6b13-11bd-4dae-9f48-f954cb880a57",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "oldString": "$\\hat{\\beta}_{\\textsc{bcs}} = -1.53$ ($\\hat{\\beta}_{\\text{centrality}} = 0.78$, $R^2 = 0.594$). An analytic derivation shows that $\\hat{\\beta}_{\\textsc{bcs}} < 0$",
    "newString": "$\\hat{\\beta}_{\\text{BCS}} = -1.53$ ($\\hat{\\beta}_{\\text{centrality}} = 0.78$, $R^2 = 0.594$). An analytic derivation shows that $\\hat{\\beta}_{\\text{BCS}} < 0$",
    "originalFile": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{enumitem}\n\\usepackage[normalem]{ulem}\n\\usepackage{listings}\n\n\\title{How Does Schema Complexity Predict Performance\\\\in Training-Free LLM Information Extraction?}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{experimental_setup}\n\n\\input{results}\n\n\\input{sdgd_negative}\n\n\\input{discussion}\n\n\\section*{Limitations}\n\nOur findings are subject to three main limitations.\n\\textbf{(1)~Model and statistical scope.}\nPrimary experiments use Qwen3-32B; cross-model validation (LLaMA-8B/70B, Gemini Flash) covers Dimensions~1--2 but not secondary analyses such as TOST factorial interaction (\\S\\ref{sec:multi_channel}) or SDGD failure analysis (\\S\\ref{sec:sdgd}), and proprietary-model generalization remains open.\nTOST dimensional separability holds on the probability scale but logit-scale evidence is inconclusive, reflecting the inflated variance of logit-transformed proportions in the 0.37--0.86 accuracy range rather than a qualitative divergence from the linear-scale finding; the interaction point estimate (0.47\\,pp) falls within the $\\pm 3$\\,pp equivalence margin.\nBCS-controlled experiments use greedy decoding with a single seed; residual SD${}\\,=\\,0.88$\\,pp is 18--44\\% of the observed effect size (Appendix~\\ref{app:variance-decomposition}), so detection is robust but point estimates carry meaningful uncertainty.\nAll evidence is correlational with controlled stratification; mechanistic confirmation at the attention or logit level remains future work.\n%\n\\textbf{(2)~DocRED VIF confounding.}\nDocRED exhibits severe multicollinearity (VIF${}\\,=\\,50.9$), preventing reliable BCS effect quantification; semipartial $R^2{}\\,=\\,5.6\\%$ serves only as directional evidence, and the count${}\\times{}$BCS interaction is partially confounded by BCS range restriction at higher counts (Appendix~\\ref{sec:appendix_factorial}).\n%\n\\textbf{(3)~Experimental scope.}\nEvaluations cover four English-language Wikipedia/Wikidata-derived datasets in a training-free zero-shot setting; few-shot, fine-tuned, domain-specific (e.g., biomedical, legal), and non-English scenarios remain untested.\nBCS batch-level prediction is significant in RE but not detected in NER, where errors scatter across miss, boundary, and type modes (Appendix~\\ref{app:relaxed-matching}).\nBatches share prompt template and LLM but type composition is independently sampled; cross-dataset consistency is treated as converging evidence rather than independent replication \\citep{rothman-1990}, and core claims are robust to Bonferroni correction (all $p < 0.001$) \\citep{dror-2018-significance}.\n\n% \\input{checklist}  % EMNLP 2026: checklist goes in OpenReview form, not PDF\n\n\\bibliography{references}\n\n\\appendix\n\n\\section{Additional Figures}\n\\label{sec:appendix_figures}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\\S\\ref{sec:model}) for fair cross-model comparison; the count-curve results in \\S\\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\\ 0.64 at count${}\\,=\\,1$) due to over-prediction under v1.}\n\\label{tab:cross_model}\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Llama-3.1-8B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1 & 0.702 & 0.640 \\\\\n64 & 0.273 & 0.304 \\\\\n\\midrule\nDecline & $-$43\\,pp & $-$34\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\\approx$51\\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\\Delta$, in pp) is 77--87\\% as large on Llama-3.1-8B as on Qwen3-32B.}\n\\label{tab:cross_model_bcs}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{crrrrrr}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Llama-3.1-8B}} & \\multicolumn{3}{c}{\\textbf{Qwen3-32B}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Count} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} \\\\\n\\midrule\n8 & 78.1\\% & 51.0\\% & $-$27.1 & 82.3\\% & 51.0\\% & $-$31.2 \\\\\n16 & 75.5\\% & 51.6\\% & $-$23.9 & 82.8\\% & 51.6\\% & $-$31.2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{NER batch-level BCS--F1 correlation across models. $^\\dagger$Partial correlation controlling for type frequency. $^\\ddagger$LLaMA-70B count\\_12 shows $r{=}{-}0.42$ ($p{=}0.034$, uncorrected; Bonferroni $p{=}0.069$); pooled and count\\_6 are null, consistent with sampling noise at $n{=}25$. The null is observed on three models; Gemini remains untested.}\n\\label{tab:cross_model_ner_null}\n\\begin{tabular}{lcl}\n\\toprule\n\\textbf{Model} & \\textbf{NER BCS--F1 $r$} & \\textbf{Status} \\\\\n\\midrule\nQwen3-32B & $0.004$ ($p = 0.94$) & Null \\\\\nLLaMA-3.1-8B & $-0.12$ ($p = 0.29$)\\rlap{$^\\dagger$} & Null \\\\\nLLaMA-3.1-70B & $-0.13$ ($p = 0.36$)\\rlap{$^\\ddagger$} & Null \\\\\nGemini 2.5 Flash & --- & Not tested \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin. Spearman $\\rho$ computed over $n=148$ batches (NER), $n=154$ (RE), and $n=110$ (DocRE). IntraSub scales monotonically with BCS across all three datasets. DocRE missed rates decrease with BCS, indicating high-confusability errors shift from omission to substitution.}\n\\label{tab:error_taxonomy}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrrrr}\n\\toprule\n & & \\multicolumn{5}{c}{\\textbf{BCS Bin}} & & \\\\\n\\cmidrule(lr){3-7}\n\\textbf{Task} & \\textbf{Error} & \\textbf{Solo} & \\textbf{Low} & \\textbf{Mid} & \\textbf{High} & \\textbf{V.High} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nNER & IntraSub & 0\\% & 1.6\\% & 10.6\\% & 49.4\\% & --- & 1.000 & ${<}0.001$ \\\\\nRE  & IntraSub & 0\\% & 4.2\\% & 13.0\\% & 20.3\\% & 32.3\\% & 0.954 & ${<}\\,0.001$ \\\\\nDocRE & IntraSub & --- & 4.8\\% & 22.4\\% & 37.0\\% & 41.9\\% & 0.843 & ${<}\\,0.001$ \\\\\n\\midrule\nNER & Missed & --- & 42.8\\% & 64.8\\% & 49.9\\% & --- & --- & --- \\\\\nRE  & Missed & --- & 10.4\\% & 11.3\\% & 13.1\\% & 15.7\\% & --- & --- \\\\\nDocRE & Missed & --- & 28.1\\% & 22.6\\% & 21.6\\% & 16.2\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model replication of IntraSub--BCS Spearman correlation on FewRel RE. $^\\dagger$LLaMA-70B has only 20 batches with 17.4\\% missed rate; the null is attributable to insufficient power rather than absence of the effect.}\n\\label{tab:cross_model_error_taxonomy}\n\\begin{tabular}{lrcc}\n\\toprule\n\\textbf{Model} & $n$ & $\\rho$ & $p$ \\\\\n\\midrule\nQwen3-32B & 154 & 0.954 & ${<}\\,0.001$ \\\\\nGemini 2.5 Flash & 60 & 0.821 & ${<}\\,0.001$ \\\\\nLLaMA-3.1-8B & 54 & 0.430 & 0.001 \\\\\nLLaMA-3.1-70B$^\\dagger$ & 20 & $-$0.086 & 0.719 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{SDGD Full Protocol and Results}\n\\label{sec:appendix_sdgd}\n\nWe construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent (i.e., highly confusable) types share a color. Each color class forms one extraction batch, and predictions are merged via set union.\n\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item Compute pairwise SCS matrix $S_{ij} = \\cos(\\text{embed}(t_i), \\text{embed}(t_j))$.\n\\item Construct graph $G$: add edge $(t_i, t_j)$ iff $S_{ij} > \\tau$.\n\\item Apply greedy graph coloring (\\textsc{largest\\_first}) to assign each type a color $c(t)$.\n\\item For each color $k$, form batch $B_k = \\{t : c(t) = k\\}$ and run extraction on all test instances.\n\\item Merge: union of per-batch predictions (v1) or confidence-gated selection (v2).\n\\end{enumerate}\nOracle routing (Table~\\ref{tab:routing_strategies}) recovers substantial accuracy (72.4\\% vs.\\ 50.4\\% single-pass), confirming the sub-schemas contain correct predictions; the failure lies in routing, not decomposition quality.\n\nWe compare four modes: (i)~\\textbf{single\\_pass}, the undecomposed baseline; (ii)~\\textbf{sdgd\\_zero}, SCS-guided partitioning; (iii)~\\textbf{random\\_batch}, random partitioning with matched batch sizes; and (iv)~\\textbf{per\\_type}, the extreme case where each type is extracted in isolation.\n\nSingle-pass extraction achieves F1\\,=\\,0.445 (P\\,=\\,0.563, R\\,=\\,0.368). SDGD obtains F1\\,=\\,0.251 (P\\,=\\,0.210, R\\,=\\,0.314), a 44\\% relative drop. Random batching reaches F1\\,=\\,0.320 (P\\,=\\,0.249, R\\,=\\,0.446), and per-type extraction yields F1\\,=\\,0.292 (P\\,=\\,0.194, R\\,=\\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\\ref{tab:sdgd_results}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \\texttt{min\\_batch\\_size=8} (reducing 8$\\to$4 batches for sdgd\\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt.}\n\\label{tab:sdgd_results}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrccc}\n\\toprule\n\\textbf{Mode} & \\textbf{\\# Batches} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{F1} \\\\\n\\midrule\nsingle\\_pass & 1 & 0.563 & 0.368 & 0.445 \\\\\n\\midrule\nsdgd\\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\\\\nrandom\\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\\\\nper\\_type & 66 & 0.194 & 0.586 & 0.292 \\\\\n\\midrule\nsdgd\\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\\\\nrandom\\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nDecomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions. Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions and inflates false positives.\n\nOur v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\\_zero: 0.210$\\to$0.324; random\\_batch: 0.249$\\to$0.331), but at the cost of disproportionate recall loss (0.314$\\to$0.191; 0.446$\\to$0.276), and both modes produce lower F1 (sdgd\\_zero: 0.251$\\to$0.241; random\\_batch: 0.320$\\to$0.301).\n\n\\subsection{Practical Routing Strategies on RE}\n\\label{sec:appendix_routing}\n\nWe evaluate five non-oracle routing strategies on FewRel 80-relation RE using graph-coloring sub-schema decomposition (same grouping as Table~\\ref{tab:batch_composition}). Each strategy selects a single sub-schema for each test instance and returns that sub-schema's prediction.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Routing strategy comparison on FewRel 80-relation RE with graph-coloring sub-schema decomposition. Oracle requires gold labels. All practical (non-oracle) strategies perform below the single-pass baseline. The failure stems from constrained decoding (enum constraint), which forces confident predictions in every sub-schema: 73.4\\% of instances receive positive predictions from 3--5 sub-schemas simultaneously, with per-sub-schema none-rates of only 20--40\\%.}\n\\label{tab:routing_strategies}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{@{}lrr@{}}\n\\toprule\n\\textbf{Strategy} & \\textbf{Accuracy} & \\textbf{$\\Delta$ vs.\\ Single-Pass} \\\\\n\\midrule\nOracle (gold label) & 72.4\\% & +22.0\\,pp \\\\\n\\midrule\nMax-conf (positive only) & 36.5\\% & $-$14.0\\,pp \\\\\nNone-aware & 36.5\\% & $-$14.0\\,pp \\\\\nMargin (positive only) & 35.9\\% & $-$14.5\\,pp \\\\\nMax-conf (all) & 27.7\\% & $-$22.7\\,pp \\\\\nRandom & 14.7\\% & $-$35.7\\,pp \\\\\n\\midrule\nSingle-pass (no decomposition) & 50.4\\% & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\section{Factorial Analysis and Separability Test}\n\\label{sec:appendix_factorial}\n\nTo formally test whether count and confusability effects are additive, we fit a multiple regression (accuracy $\\sim$ $\\log_2$\\,count $+$ BCS $+$ count$\\times$BCS) across 69 batches from FewRel spanning five count levels ($k \\in \\{4, 8, 16, 32, 40\\}$). Both main effects are significant (count: $p = 0.008$; BCS: $p = 0.0002$; $R^2 = 0.52$), but the interaction term is negligible (0.47\\,pp). A TOST equivalence test with a $\\pm 3$\\,pp margin confirms that the interaction is bounded well below practical significance ($p_{\\text{TOST}} = 0.003$); this supports bounded interaction between count and confusability effects.\n\nA $2 \\times 2$ factorial sensitivity check on FewRel (count $\\in \\{8, 16\\}$, BCS low/high; $n = 54$) was inconclusive ($p_{\\text{TOST}} = 0.56$) due to limited power; this does not contradict the primary finding but limits generalization beyond the regression framework. The Few-NERD factorial (\\S\\ref{sec:multi_channel}) similarly did not reach significance ($p = 0.50$). The regression approach provides the stronger test by leveraging the full count range.\n\n\\paragraph{Equivalence margin justification.}\nWe set the $\\pm 3$\\,pp margin based on three converging anchors. \\emph{External}: evaluation variance in IE benchmarks typically spans 2--5\\,pp across random seeds, prompt variations, and data splits \\citep{card-2020-power,dror-2018-significance}; our own four structurally distinct prompt variants yield cross-variant accuracy SD of 3.5--4.6\\,pp across count conditions (Table~\\ref{tab:prompt_variants}), confirming that a within-margin interaction would be indistinguishable from routine prompt-design noise and satisfying the smallest-effect-of-interest criterion \\citep{lakens-2017-equivalence}. \\emph{Internal}: $0.5 \\times$ within-cell SD ($= 2.3$\\,pp) corresponds to Cohen's $d \\approx 0.5$ (medium effect threshold; \\citealt{lakens-2017-equivalence}), cross-validated against the IQR-predicted confusability main effect of 2.2\\,pp (\\S\\ref{sec:practical_magnitude})---an interaction exceeding 3\\,pp would represent ${>}130\\%$ amplification. \\emph{Sensitivity}: Table~\\ref{tab:tost_sensitivity} shows equivalence holds from $\\pm 2$\\,pp ($p = 0.047$) through $\\pm 5$\\,pp ($p < 0.001$) on the probability scale; the conclusion is not margin-dependent.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{TOST sensitivity analysis across equivalence margins. The interaction effect (0.47\\,pp, 90\\% CI [$-$1.0, 2.0]\\,pp) is bounded below 2\\,pp at marginal significance ($p = 0.047$); the $\\pm 3$\\,pp choice does not drive the equivalence conclusion. At $\\pm 1$\\,pp, equivalence is inconclusive ($p = 0.278$), meaning interaction could reach approximately half the main effect magnitude.}\n\\label{tab:tost_sensitivity}\n\\begin{tabular}{crrl}\n\\toprule\n\\textbf{Margin (pp)} & \\textbf{$t_{\\text{upper}}$} & \\textbf{$p_{\\text{TOST}}$} & \\textbf{Conclusion} \\\\\n\\midrule\n$\\pm 1$ & $-0.59$ & $0.278$ & Inconclusive \\\\\n$\\pm 2$ & $-1.70$ & $0.047$ & Equivalent \\\\\n$\\pm 3$ & $-2.81$ & $0.003$ & Equivalent \\\\\n$\\pm 5$ & $-5.02$ & ${<}\\,0.001$ & Equivalent \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Logit-scale sensitivity.}\nBecause accuracy near 50\\% compresses interaction effects on the linear scale, we refit the regression on logit-transformed accuracy. The logit-scale interaction (0.111 logit units, $p = 0.047$, 90\\% CI [0.019, 0.203]) is marginally significant, and TOST at the equivalent $\\pm 3$\\,pp margin ($\\pm 0.156$ logit at median accuracy) is inconclusive ($p_{\\text{TOST}} = 0.209$). However, back-transforming the interaction to the probability scale at the observed floor ($p = 0.51$) yields 2.78\\,pp, still within the $\\pm 3$\\,pp margin; at the median baseline ($p = 0.65$), the back-transformed effect is 2.53\\,pp. The logit TOST is inconclusive due to limited power ($n = 69$, wide CI) rather than a large effect size: the point estimate remains below the equivalence bound at all observed baselines. We retain the linear-scale TOST as the primary test and report this logit analysis as a sensitivity check. A regression-based TOST ($n = 375$, five count levels with continuous BCS) yields $p = 0.050$ at $\\pm 3$\\,pp and $p = 0.026$ at $\\pm 3.5$\\,pp on the logit scale, confirming the borderline status with substantially greater power than the factorial design.\n\n\\paragraph{DocRED factorial (expanded).}\nWith expanded batches ($n{=}55$ per count level, up from $n{=}5$), the DocRED $2 \\times 2$ factorial (count $\\in \\{16, 32\\}$, BCS median split) yields an apparent interaction ($-$9.4\\,pp, 95\\% CI [$-$12.9, $-$6.0]): the BCS effect is $-$25.0\\,pp at count 16 but $-$15.7\\,pp at count 32. However, this attenuation is confounded by BCS range restriction: higher-count batches have narrower BCS ranges (spread 0.26 vs.\\ 0.38), limiting achievable extremes.\n\n\\paragraph{Range-matched robustness check.}\nTo control for the BCS range confound, we restrict both count levels to the overlapping BCS range [0.43, 0.70]. This retains 29 of 55 batches at count 16 (all 55 at count 32 fall within the range). Within this matched range, the BCS effect at count 16 shrinks from 15.95\\,pp to 9.37\\,pp (reflecting the narrower BCS span), while count 32 remains at 8.44\\,pp. The interaction drops from 7.52\\,pp (95\\% CI [1.49, 12.83]) to 0.93\\,pp (95\\% CI [$-$7.13, 7.44])---the CI spans zero, consistent with no interaction. Spearman correlations remain comparable ($\\rho = -0.65$ at count 16, $\\rho = -0.69$ at count 32), confirming that the underlying BCS--accuracy relationship is robust across counts while the raw interaction magnitude was an artifact of differing achievable BCS ranges. This result aligns with the FewRel TOST equivalence finding and supports bounded association as the cross-dataset pattern. The reduced sample ($n = 29{+}55$) yields a minimum detectable effect of 5.5\\,pp at 80\\% power, consistent with insufficient power to distinguish a true null from a small ($<$5\\,pp) interaction.\n\n\\section{Within-Pool CI Details}\n\\label{sec:appendix_within_pool}\n\nThe quartile $\\Delta$ for 80-pool 16-relation subsets ($-$3.92\\,pp, 95\\% CI [$-$8.17, $+$0.38]) crosses zero, reflecting the compressed BCS range within that pool (0.46--0.68 vs.\\ 0.48--0.71 for the independent pool). Within this narrow band, the quartile contrast lacks statistical power to detect the effect that the regression identifies. The full 80-relation condition ($n = 25$) is underpowered for both the slope (95\\% CI [$-$1.303, $+$1.695]) and quartile analyses; we include it in Table~\\ref{tab:within_pool} for completeness but do not draw inferential conclusions from it.\n\n\\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}\n\\label{sec:appendix_residualized_bcs}\n\nSection~\\ref{sec:centrality_confound} identifies a centrality confound in MAVEN's per-type BCS--F1 correlation: both embeddings show a \\emph{positive} raw correlation, opposite to the expected direction. Here we formalize this analysis by identifying specific confounders for each embedding and testing whether the BCS--F1 relationship survives partial correlation controlling for these confounders.\n\n\\paragraph{Confound identification.}\nFor each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:\n\\begin{itemize}[itemsep=2pt,leftmargin=*]\n\\item \\textbf{MiniLM}: BCS correlates with log type frequency ($r = 0.201$). Frequent types have more training signal and are extracted more reliably, which produces the positive BCS--F1 association.\n\\item \\textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors, central, well-represented types that the model extracts well.\n\\end{itemize}\n\n\\paragraph{Partial correlation results.}\nTable~\\ref{tab:residualized_bcs} reports raw Spearman $\\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{MAVEN per-type BCS--F1 correlation before and after controlling for centrality confounders. Raw correlations are Spearman $\\rho$; partial correlations are Pearson $r$ from residualized regression. Degree centrality is computed on the SCS graph at threshold 0.7. All values from experiment \\texttt{exp\\_maven\\_residualized\\_bcs}.}\n\\label{tab:residualized_bcs}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Embedding} & \\textbf{Control} & \\textbf{Raw $\\rho$} & \\textbf{Raw $p$} & \\textbf{Partial $r$} & \\textbf{Partial $p$} \\\\\n\\midrule\nMiniLM & --- & $+$0.208 & $0.011$ & --- & --- \\\\\nMiniLM & log freq & --- & --- & $+$0.133 & $0.11$ \\\\\nMiniLM & log freq $+$ degree & --- & --- & --- & $0.23$ \\\\\n\\midrule\nQwen3 & --- & $+$0.184 & $0.025$ & --- & --- \\\\\nQwen3 & degree centrality & --- & --- & $+$0.063 & $0.44$ \\\\\nQwen3 & log freq $+$ degree & --- & --- & --- & $0.44$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Interpretation.}\nThe two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality (the count of strong semantic neighbors) becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.\n\nUnder joint control, both embeddings yield $p > 0.2$; the raw positive BCS--F1 correlation on MAVEN is thus fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 0.001$; Table~\\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.\n\n\\subsection{Partial Correlation: Controlling for Degree Centrality}\n\\label{sec:appendix_partial_corr}\n\nTo rule out degree centrality as a confound in cross-domain datasets, we compute partial correlations between BCS and accuracy controlling for batch mean degree centrality (mean off-diagonal SCS per type, averaged across batch members).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{BCS--accuracy partial correlation controlling for degree centrality. FewRel shows minimal attenuation (VIF${}\\,=\\,1.18$, low collinearity). DocRED shows high BCS--centrality collinearity (VIF${}\\,=\\,50.9$, $r = 0.99$), but the partial correlation remains highly significant.}\n\\label{tab:partial_corr}\n\\begin{tabular}{lrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{$n$} & \\textbf{$r_{\\text{zero}}$} & \\textbf{$r_{\\text{partial}}$} & \\textbf{$p_{\\text{partial}}$} & \\textbf{VIF} \\\\\n\\midrule\nFewRel & 204 & $-$0.570 & $-$0.537 & ${<}\\,0.001$ & 1.18 \\\\\nDocRED & 110 & $-$0.760 & $-$0.348 & ${<}\\,0.001$ & 50.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAs Table~\\ref{tab:partial_corr} shows, on FewRel, BCS and degree centrality are only moderately correlated ($r = 0.39$), and the BCS effect survives nearly intact after partialling ($r_{\\text{partial}} = -0.537$ vs.\\ $r_{\\text{zero}} = -0.570$; semipartial $R^2 = 0.273$). On DocRED, the near-perfect BCS--centrality correlation ($r = 0.99$) makes it impossible to fully separate the two predictors; the significant partial correlation ($p < 0.001$) indicates BCS retains predictive value but does not uniquely identify the causal channel. This contrasts with MAVEN (\\S\\ref{sec:appendix_residualized_bcs}), where the BCS signal vanishes after controlling for centrality.\n\n\\paragraph{Ridge regression under multicollinearity.}\nRidge regression (GCV, $\\lambda = 0.001$) on the 110 DocRED batches confirms the negative direction of the BCS--accuracy relationship even after regularizing for the severe BCS--centrality multicollinearity (VIF$\\,\\approx\\,$50.9). The standardized BCS coefficient is $\\hat{\\beta}_{\\textsc{bcs}} = -1.53$ ($\\hat{\\beta}_{\\text{centrality}} = 0.78$, $R^2 = 0.594$). An analytic derivation shows that $\\hat{\\beta}_{\\textsc{bcs}} < 0$ for \\emph{all} $\\lambda \\geq 0$: the numerator of the closed-form ridge solution, $-(1{+}\\lambda) \\times 0.760 + 0.727$, is negative at $\\lambda{=}0$ and monotonically decreasing thereafter. Given the shrinkage bias inherent to ridge estimation, we interpret only the sign---not the magnitude---of the BCS coefficient as directional evidence that higher schema confusability degrades extraction accuracy, independent of degree centrality.\n\n\\subsection{NER BCS-Null Power Analysis}\n\\label{sec:appendix_ner_power}\n\nThe Few-NERD BCS-null may reflect insufficient BCS variance rather than a genuine absence of the BCS--accuracy relationship. Few-NERD's BCS standard deviation (0.027) is only 19\\% of FewRel's (0.141); FewRel's observed $r = -0.570$ would attenuate to $r = -0.111$ under this restricted range, yielding 65\\% power at $n = 450$ (below the conventional 80\\% threshold). The minimum detectable $|r|$ at 80\\% power is 0.132. This analysis characterizes the NER result as absence of evidence (insufficient power at the attenuated effect size) rather than evidence of absence.\n\n\\subsection{Bootstrap CI Robustness}\n\\label{sec:appendix_bootstrap_ci}\n\nBecause batches in the FewRel experiments are constructed by sampling relation types from a shared pool, different batches may share text instances of the same type, potentially inducing residual dependence that makes standard bootstrap CIs anti-conservative. We assess this concern via cluster-robust inference. We cluster the $n = 164$ FewRel batches by instance-weighted type overlap (hierarchical clustering, complete linkage) and compute cluster-robust standard errors. Across six overlap thresholds (Jaccard distance $\\in \\{0.1, \\ldots, 0.9\\}$, yielding 80--83 clusters), the cluster-robust SE for the BCS regression slope is $0.96$--$0.97\\times$ the OLS SE, and the slope remains highly significant ($p < 10^{-11}$). Cluster bootstrap CIs for $R^2$ show width changes of $-6\\%$ to $+6\\%$ relative to standard bootstrap CIs ($[0.14, 0.42]$ vs.\\ $[0.15, 0.41]$). We conclude that the reported CIs are robust to the non-independence induced by shared text instances.\n\n\\subsection{Domain Distribution in Extreme-BCS Batches}\n\\label{sec:appendix_domain_distribution}\n\nWe classify the 80 FewRel relation types into six semantic domains (geography, creative work, person, organization, event/temporal, science/taxonomy) and compare domain composition between the 25 highest-BCS and 25 lowest-BCS batches from our 8-type schema pool. The distributions differ significantly ($\\chi^2 = 230.74$, $p < 0.001$, $df = 5$): low-BCS batches draw heavily from geography (45.5\\%) and creative work (25.5\\%), while high-BCS batches concentrate on science/taxonomy (49.5\\%) and event/temporal (26.0\\%) domains. Normalized Shannon entropy is higher for low-BCS batches ($H' = 0.79$) than high-BCS ($H' = 0.67$), confirming that low-BCS schemas span more diverse domains. Crucially, this domain concentration is an \\emph{expected} property of embedding-based confusability: relation types within the same domain naturally share semantic features, producing higher pairwise cosine similarity and thus higher BCS. Domain composition therefore acts as a mediator---it is \\emph{part of} the mechanism through which BCS captures schema difficulty---rather than an independent confounding variable. The BCS metric intentionally aggregates such semantic overlap into a single predictive score.\n\n\\section{Batch Composition Results}\n\\label{sec:appendix_batch_composition}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Batch composition on FewRel 80-relation RE with oracle routing. $^\\dagger$Mean $\\pm$ SD across 15 random seeds.}\n\\label{tab:batch_composition}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Accuracy} & \\textbf{Mean BCS} \\\\\n\\midrule\nSingle-pass (80 types) & 0.504 & 0.557 \\\\\nRandom batching (15 seeds)$^\\dagger$ & 0.788\\,$\\pm$\\,0.018 & 0.559 \\\\\nConfus.-aware (graph coloring) & \\textbf{0.802} & 0.552 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nSee the accompanying discussion in \\S\\ref{sec:sdgd}.\n\n\\input{prompt_appendix}\n\n\\section{Prompt Version Sensitivity Analysis}\n\\label{sec:appendix_prompt_sensitivity}\n\nWe assess whether the confusability effects reported in \\S\\ref{sec:bcs_controlled}--\\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\paragraph{RE (FewRel).}\nUnder the v1 prompt, the extreme-batch BCS gap (Table~\\ref{tab:bcs_controlled}) is substantial. Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; 95\\% CI [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\\,pp (95\\% CI [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal, a cautionary note for small-sample prompt sensitivity studies.\n\n\\paragraph{NER (Few-NERD).}\nThe batch-level BCS--F1 correlation is null under both prompt versions. Pooling across three seeds and all count levels ($n = 450$), the correlation is $r = 0.004$ ($p = 0.94$). An earlier small-sample analysis ($n = 27$, single seed) had reported positive correlations ($r = +0.50$/$+0.58$), but these were driven by an accidental BCS--type-frequency confound: those 27 batches exhibited $r(\\text{BCS}, \\text{freq}) = 0.53$, creating a spurious path through frequency to F1. After controlling for type frequency, the partial correlation is non-significant in both the small ($r = 0.28$, $p = 0.16$) and large ($r = -0.12$, $p = 0.29$) samples. The pairwise SCS--confusion analysis (\\S\\ref{sec:pairwise}), which is immune to this batch-level aggregation artifact, remains the primary evidence for the NER confusability dimension.\n\n\\paragraph{Interpretation.}\nThe $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\\,pp) but remains highly significant ($p < 0.001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\\% vs.\\ 82.3\\%), but type confusion under high confusability persists (59.7\\% vs.\\ 51.0\\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary source. The underlying confusability signal (pairwise SCS--confusion correlation and the directional BCS--accuracy relationship) persists across both prompt versions.\n\n\\subsection{Cross-Prompt-Variant BCS Correlation}\n\\label{sec:appendix_prompt_variants}\n\nTo verify that the BCS--accuracy relationship is not an artifact of a specific prompt template, we evaluate four structurally distinct prompt variants on FewRel 80-relation RE at two count levels (8 and 32), with 10 random batches per condition (Table~\\ref{tab:prompt_variants}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{BCS--accuracy Pearson correlation across four prompt variants. At count 32, all four variants show negative BCS--accuracy correlations ($r \\leq -0.47$), with two reaching $p < 0.05$. At count 8, the narrower BCS range reduces statistical power.}\n\\label{tab:prompt_variants}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{Variant} & \\textbf{Count} & \\textbf{Mean Acc} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nV2 (definition-first) & 8 & 0.769 & $-$0.333 & 0.348 \\\\\nV2 (definition-first) & 32 & 0.564 & $-$0.648 & 0.043 \\\\\nInstruction-rewrite & 8 & 0.847 & $-$0.223 & 0.536 \\\\\nInstruction-rewrite & 32 & 0.662 & $-$0.469 & 0.171 \\\\\nChain-of-thought & 8 & 0.749 & $+$0.254 & 0.478 \\\\\nChain-of-thought & 32 & 0.617 & $-$0.566 & 0.088 \\\\\nMinimal & 8 & 0.852 & $-$0.170 & 0.638 \\\\\nMinimal & 32 & 0.615 & $-$0.771 & 0.009 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nAt count 32, all four variants produce negative BCS--accuracy correlations ($r$ ranges from $-$0.47 to $-$0.77), with V2 ($p = 0.043$) and Minimal ($p = 0.009$) reaching significance and Chain-of-thought approaching it ($p = 0.088$). At count 8, correlations are weaker and nonsignificant across all variants, consistent with the narrower BCS range at lower schema complexity reducing the detectable effect size. Rather than applying Bonferroni correction, which assumes independent hypotheses inappropriate for correlated prompt variants testing the same underlying signal, we note directional consistency: 7 of 8 conditions show negative BCS--accuracy slopes, consistent with the primary finding \\citep{rothman-1990}. These results confirm that the confusability effect arises from schema composition, not prompt-specific phrasing.\n\n\\section{BCS Aggregation Sensitivity}\n\\label{sec:appendix_bcs_sensitivity}\n\nWe define Batch Confusability Score (BCS) as the \\emph{mean} pairwise SCS across all type pairs in a batch (\\S\\ref{sec:bcs_controlled}). An alternative definition takes the \\emph{maximum} pairwise SCS within each batch to capture the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice (Table~\\ref{tab:bcs_aggregation}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{BCS--accuracy regression under mean vs.\\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p \\approx 0.60$; MAX $p \\approx 0.44$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}\n\\label{tab:bcs_aggregation}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Aggregation} & \\textbf{Condition} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nMEAN (primary) & 16-rel & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ \\\\\nMEAN & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\midrule\nMAX & 16-rel & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}\\,0.001$ \\\\\nMAX & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nMAX aggregation yields stronger correlations ($r = -0.637$ vs.\\ $-0.467$ for 16-rel), consistent with the hypothesis that the single most confusable pair in a batch predicts substitution errors. Both definitions produce significant negative slopes across all conditions, and the permutation tests confirm no significant difference between independent and sampled pools under either definition. We adopt MEAN as the primary definition because it better represents average pairwise difficulty across all schema combinations, while MAX may overweight a single outlier pair. The choice does not affect any paper conclusion.\n\n\\section{BCS-Controlled Detailed Results}\n\\label{app:bcs-controlled-table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Adjusted $R^2$ and confidence intervals.}\nDocRED regressions (\\S\\ref{sec:bcs_controlled}) use OLS on $n = 55$ batches (15 high-BCS + 15 low-BCS + 25 random) per count level, with one predictor. At count 16, adjusted $R^2 = 0.646$ (unadjusted: 0.653; 95\\% CI [0.53, 0.77]); at count 32, adjusted $R^2 = 0.606$ (unadjusted: 0.614; 95\\% CI [0.47, 0.75]). The small shrinkage ($\\Delta R^2 \\leq 0.01$) indicates the unadjusted values are not inflated by the predictor-to-sample ratio.\n\n\\section{Format Independence: Paired Constrained vs.\\ Unconstrained Comparison}\n\\label{app:format-independence}\n\nTo test whether the BCS--accuracy relationship depends on the output format, we run both constrained (enum-based) and unconstrained (free-text) decoding on the same 25 batch type sets from the FewRel 80-relation pool (13 low-BCS, 12 high-BCS; count 8). Each batch uses identical instances and type sets; only the decoding format differs (Table~\\ref{tab:format_independence}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Paired comparison of constrained vs.\\ unconstrained decoding on 25 identical FewRel batch type sets. Both formats yield virtually identical BCS--accuracy correlations (Fisher $z \\approx 0$), confirming the confusability effect is format-independent. Mean accuracy is also unchanged ($\\Delta = -0.08$\\,pp), ruling out a format-driven accuracy shift.}\n\\label{tab:format_independence}\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Metric} & \\textbf{Constrained} & \\textbf{Unconstrained} \\\\\n\\midrule\nMean accuracy & 79.5\\% & 79.6\\% \\\\\nPearson $r$ (BCS vs.\\ acc) & $-$0.448 ($p = 0.025$) & $-$0.439 ($p = 0.028$) \\\\\nSpearman $\\rho$ (BCS vs.\\ acc) & $-$0.157 ($p = 0.455$) & $-$0.144 ($p = 0.492$) \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Paired Fisher $z$-test for correlation equality}} \\\\\n\\quad Pearson $z$ & \\multicolumn{2}{c}{$-$0.04 ($p = 0.97$)} \\\\\n\\quad Spearman $z$ & \\multicolumn{2}{c}{$-$0.04 ($p = 0.97$)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe near-zero Fisher $z$ statistics ($|z| < 0.05$, $p > 0.96$) confirm that the BCS--accuracy correlation is indistinguishable between formats. Both Pearson $r$ values are significant ($p < 0.03$), reflecting the bimodal BCS distribution of extreme batches (13 low + 12 high); the monotonic Spearman $\\rho$ is modest and non-significant under both formats, consistent with the typical-batch BCS effect size (${\\sim}2$\\,pp; \\S\\ref{sec:practical_magnitude}). This result establishes that the confusability-associated degradation pattern is robust across output formats, not an artifact of forced-choice decoding.\n\n\\paragraph{Per-batch paired results.}\nTable~\\ref{tab:format_perbatch} reports per-batch accuracy under both formats. Of 25 batches, 23 yield \\emph{identical} accuracy; the two exceptions (high\\_5, high\\_11) differ by a single sample (1/96 $\\approx$ 1.04\\,pp). Only 2 out-of-vocabulary predictions occur in unconstrained decoding (OOV rate 0.08\\%), confirming that the model generates valid type labels even without format constraints.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Per-batch accuracy (\\%) under constrained and unconstrained decoding on 25 identical FewRel batch type sets (count 8, 96 instances each). 23/25 batches yield identical accuracy; the two exceptions differ by exactly one sample ($\\Delta = -1.04$\\,pp). L = low-BCS, H = high-BCS.}\n\\label{tab:format_perbatch}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Batch} & \\textbf{Group} & \\textbf{BCS} & \\textbf{Constr.} & \\textbf{Unconstr.} & \\textbf{$\\Delta$} \\\\\n\\midrule\nlow\\_0  & L & 0.472 & 83.3 & 83.3 & 0.0 \\\\\nlow\\_1  & L & 0.647 & 81.3 & 81.3 & 0.0 \\\\\nlow\\_2  & L & 0.665 & 87.5 & 87.5 & 0.0 \\\\\nlow\\_3  & L & 0.672 & 82.3 & 82.3 & 0.0 \\\\\nlow\\_4  & L & 0.674 & 67.7 & 67.7 & 0.0 \\\\\nlow\\_5  & L & 0.678 & 72.9 & 72.9 & 0.0 \\\\\nlow\\_6  & L & 0.679 & 80.2 & 80.2 & 0.0 \\\\\nlow\\_7  & L & 0.687 & 87.5 & 87.5 & 0.0 \\\\\nlow\\_8  & L & 0.692 & 77.1 & 77.1 & 0.0 \\\\\nlow\\_9  & L & 0.692 & 91.7 & 91.7 & 0.0 \\\\\nlow\\_10 & L & 0.692 & 87.5 & 87.5 & 0.0 \\\\\nlow\\_11 & L & 0.709 & 84.4 & 84.4 & 0.0 \\\\\nlow\\_12 & L & 0.709 & 68.8 & 68.8 & 0.0 \\\\\n\\midrule\nhigh\\_0  & H & 0.712 & 91.7 & 91.7 & 0.0 \\\\\nhigh\\_1  & H & 0.724 & 77.1 & 77.1 & 0.0 \\\\\nhigh\\_2  & H & 0.735 & 67.7 & 67.7 & 0.0 \\\\\nhigh\\_3  & H & 0.742 & 86.5 & 86.5 & 0.0 \\\\\nhigh\\_4  & H & 0.742 & 86.5 & 86.5 & 0.0 \\\\\nhigh\\_5  & H & 0.747 & 81.3 & 82.3 & $-$1.0 \\\\\nhigh\\_6  & H & 0.768 & 83.3 & 83.3 & 0.0 \\\\\nhigh\\_7  & H & 0.778 & 77.1 & 77.1 & 0.0 \\\\\nhigh\\_8  & H & 0.791 & 71.9 & 71.9 & 0.0 \\\\\nhigh\\_9  & H & 0.820 & 70.8 & 70.8 & 0.0 \\\\\nhigh\\_10 & H & 0.823 & 92.7 & 92.7 & 0.0 \\\\\nhigh\\_11 & H & 0.971 & 49.0 & 50.0 & $-$1.0 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\section{Within-Pool Analysis Methodology}\n\\label{app:within-pool-method}\n\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ & $-$5.31 & [$-$7.44, $-$3.19] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & $0.027$ & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$)$^\\dagger$ & $+$0.221 & [$-$1.303, $+$1.695] & $+$0.064 & $0.76$ & $-$1.04 & [$-$10.12, $+$8.04] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p \\approx 0.60$ (5{,}000 permutations)} \\\\\n\\multicolumn{7}{l}{\\footnotesize $^\\dagger$BCS range (IQR\\,=\\,0.033) insufficient for regression; slope not interpretable.} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nThe within-pool slope ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.509; permutation $p \\approx 0.60$). The smaller quartile gap ($-$3.92\\,pp vs.\\ $-$5.31\\,pp) reflects the narrower BCS range within the 80-relation pool (Appendix~\\ref{sec:appendix_within_pool}).\n\nIn the full 80-relation condition, natural BCS variation is insufficient (IQR${}=0.033$) to yield a detectable effect ($n=25$, slope${}=+0.221$, $p \\approx 0.76$). This does not invalidate the confusability effect; the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied, but establishes that natural schema sampling at this scale does not produce sufficient BCS contrast for detection.\n\n\\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}\n\\label{app:scs-ablation}\n\nTable~\\ref{tab:scs-ablation} compares predictive accuracy of name-only SCS against name+definition SCS across three datasets.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Pearson correlation between SCS and empirical confusion rate. ``Def'' concatenates type name with definition before embedding. All correlations significant ($p < 0.001$). The inconsistent direction of $\\Delta r$ indicates that definitions provide no systematic benefit.}\n\\label{tab:scs-ablation}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lcccc}\n\\toprule\nDataset & SCS$_\\text{name}$ $r$ & SCS$_\\text{def}$ $r$ & $\\Delta r$ & Matrix corr. \\\\\n\\midrule\nFew-NERD & 0.172 & 0.149 & $-$0.023 & 0.894 \\\\\nMAVEN & 0.129 & 0.164 & +0.035 & 0.656 \\\\\nFewRel & 0.178 & 0.193 & +0.015 & 0.848 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nFew-NERD is the only dataset whose prompts include type definitions; for MAVEN and FewRel, prompts use type names alone, so name-only SCS directly matches model input. The high matrix correlation (0.66--0.89) confirms that type names capture the dominant semantic structure.\n\n\\paragraph{Held-out validation.}\n\\label{app:scs-heldout-validation}\nFrom the 80-type confusion matrix, we extract the $\\binom{16}{2} = 120$ pairs among the 16 validation-origin types (fully disjoint from the 64 training-pool types). The SCS--confusion Spearman correlation remains positive and significant ($\\rho = 0.216$, $p = 0.018$), nearly identical to the full 80-type pool ($\\rho = 0.218$, $p < 0.001$, $n = 3{,}160$ pairs), ruling out training-set contamination as the driver of the observed relationship.\n\n\\section{Pair-to-Batch Aggregation Simulation}\n\\label{app:aggregation-sim}\n\nThe following simulation provides an illustrative explanatory model for how pair-level effects aggregate to batch-level variance. It is not the evidence base for our claims; the observed pooled semipartial $R^2 = 0.273$ (\\S\\ref{sec:practical_magnitude}) is a direct empirical measurement independent of this simulation.\n\n\\paragraph{Setup.} We examine whether the pair-level $R^2 \\approx 7\\%$ (computed over non-zero confusion pairs) can aggregate to substantial batch-level $R^2$ via a Monte Carlo simulation. From the FewRel 16-relation experiment, we estimate the inter-pair SCS correlation for pairs sharing a common type ($\\rho_\\text{SCS} = 0.35$). For batches of $k=8$ types ($\\binom{8}{2}=28$ pairs), we simulate 10{,}000 iterations: (1) generate 28 correlated pair-level effects with individual $R^2 = 0.074$; (2) average to obtain batch-level signals; (3) compute batch-level $R^2$.\n\n\\paragraph{Results.} Simulated batch $R^2 = 0.219$ (95\\% CI [0.092, 0.361]), consistent with the pooled semipartial $R^2 = 0.273$ (which falls within the simulation CI). The effective amplification factor is $\\sim$3$\\times$, explained by signal correlation within batches preserving variance while independent noise averages out (effective degrees of freedom $\\approx 3.4$, not 28).\n\n\\paragraph{Unconditional baseline.}\nWhen the simulation uses the unconditional pairwise $r^2 = 0.013$ (computed over all type pairs including zero-confusion pairs; Table~\\ref{tab:pairwise}), the simulated batch-level $R^2$ drops to $0.044$ (95\\% CI [0.001, 0.151]), well below the pooled semipartial $R^2 = 0.273$. The analytical formula confirms: $\\text{SNR} \\times \\text{EF} / (\\text{SNR} \\times \\text{EF} + 1) = 0.042$ with the same effective factor $\\text{EF} = 3.35$. This ${\\sim}5\\times$ gap reflects the dilution from zero-confusion pairs: approximately 89\\% of type pairs never exhibit mutual confusion, contributing only noise to the unconditional correlation. The conditional model ($R^2 = 0.074 \\to 0.219$) produces batch-level $R^2$ consistent with the pooled observation because it isolates the minority of semantically proximate pairs that actually compete during type resolution; BCS predicts batch accuracy through the density of \\emph{active} confusable pairs, not uniform contributions from all pairs.\n\n\\paragraph{Sensitivity to $\\rho$.}\nThe inter-pair SCS correlation $\\rho = 0.35$ is estimated from pairs sharing a common type. At $\\rho = 0.20$ (halved correlation), a parallel simulation yields batch $R^2 \\approx 0.22$; at $\\rho = 0.50$, the correlation structure approaches the positive-definiteness boundary; $\\rho = 0.35$ thus sits in a stable regime. The simulation is illustrative; the pooled semipartial $R^2 = 0.273$ (\\S\\ref{sec:bcs_controlled}) is the primary evidence.\n\n\\paragraph{Non-independence and ecological inference.}\nTypes within a batch share prompt context, so their extraction outcomes are not independent---a form of ecological correlation \\citep{robinson-1950-ecological}. This non-independence is built into the design: BCS measures batch-level confusability precisely because co-present types interact during type resolution. The core batch-level effect (FewRel semipartial $R^2 = 0.273$, DocRED pooled $R^2 = 0.578$; \\S\\ref{sec:practical_magnitude}) is a direct empirical observation from regressing batch accuracy on BCS, not derived from the simulation above. The inter-pair SCS correlation $\\rho = 0.35$ used in the simulation was estimated from the SCS correlation matrix independently of batch-level accuracy data.\n\n\\section{BCS Independence from Type Composition}\n\\label{app:bcs-composition}\n\nFewRel's balanced design (700 instances per type) makes type frequency invariant across batches, ruling out frequency-driven confounding. To test whether BCS captures information beyond type composition effects, we decompose the explained variance in a joint model (accuracy $\\sim$ BCS $+$ mean type difficulty), where type difficulty is the per-type solo-baseline accuracy averaged across batch members. On 100 random 8-type batches from the 16-relation pool, the joint model explains $R^2 = 0.704$. Variance decomposition yields: BCS unique $R^2 = 0.259$ (36.8\\% of explained variance), composition unique $R^2 = 0.298$ (42.3\\%), and shared $R^2 = 0.147$ (20.9\\%). The near-orthogonality of predictors (VIF${}\\,=\\,1.06$, $r(\\text{BCS}, \\text{difficulty}) = -0.21$) confirms that BCS captures confusability-specific signal rather than a proxy for type difficulty.\n\n\\section{SCS vs.\\ Simple Baselines}\n\\label{app:scs-baselines}\n\nTable~\\ref{tab:scs_baselines} compares SCS against simple baselines for pairwise confusion prediction.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Pairwise confusion prediction: SCS vs.\\ simple baselines. Spearman $\\rho$ between each metric and the empirical confusion rate. SCS outperforms all baselines on FewRel; the margin is smaller on Few-NERD, where hierarchical naming conventions provide partial signal to string-based metrics. $^\\dagger$42\\% of pairs lack WordNet coverage.}\n\\label{tab:scs_baselines}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Metric} & \\textbf{Spearman $\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nFewRel & SCS (embedding) & \\textbf{0.218} & $< 0.001$ \\\\\n(3{,}160 pairs) & Same-parent (WordNet) & 0.097 & $< 0.001$ \\\\\n& WordNet Wu-Palmer & 0.073 & $< 0.001$ \\\\\n& Levenshtein & 0.016 & 0.363 (n.s.) \\\\\n\\midrule\nFew-NERD & SCS (embedding) & \\textbf{0.166} & $< 0.001$ \\\\\n(1{,}953 pairs) & Levenshtein & 0.152 & $< 0.001$ \\\\\n& Same-parent (prefix) & 0.146 & $< 0.001$ \\\\\n& WordNet Wu-Palmer & 0.054 & 0.070 (n.s.)$^\\dagger$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\section{Split-Origin Covariate Analysis}\n\\label{app:split-origin}\n\nFewRel combines 64 train-split and 16 val-split relation types into a single 80-type pool.  Train-origin types show numerically lower accuracy ($-8.8$\\,pp, $p = 0.06$; see Limitations), raising the question of whether differential pre-training exposure confounds the BCS--accuracy relationship.  We test this by adding a per-batch \\emph{train-origin ratio} (fraction of relation types drawn from the train split) as a covariate in the BCS--accuracy regression.\n\n\\paragraph{Method.}  Across 213 multi-type batches ($k \\geq 2$) from the batch-composition experiment (\\S\\ref{sec:sdgd}) and the factorial design (\\S\\ref{sec:bcs_controlled}), we compute $\\texttt{train\\_origin\\_ratio} = n_{\\text{train}} / k$ for each batch.  The ratio ranges from 0.40 to 1.00 (mean 0.80, consistent with the 64/80 base rate).  We fit:\n{\\small\\begin{equation*}\n\\text{acc} = \\beta_0 + \\beta_{\\text{BCS}} \\!\\cdot\\! \\text{BCS} + \\beta_{\\text{orig}} \\!\\cdot\\! \\text{train\\_origin\\_ratio} + \\varepsilon\n\\end{equation*}}\n\n\\paragraph{Results.}  The BCS partial effect is unchanged after controlling for split-origin: $\\beta_{\\text{BCS}} = -0.416$, $p < 0.001$ (vs.\\ $\\beta = -0.412$, $p < 0.001$ without the covariate).  Train-origin ratio is not independently significant ($\\beta_{\\text{origin}} = -0.057$, $p = 0.245$), and $\\Delta R^2 = 0.005$.  The BCS--accuracy relationship is therefore not confounded by differential pre-training exposure at the batch level.\n\nPairwise SCS distributions do not differ significantly between train-origin (64 types, mean\\,=\\,0.880) and val-origin (16 types, mean\\,=\\,0.874) subsets (Mann-Whitney $p = 0.754$, Cohen's $d = 0.081$); the train/val split does not introduce systematic confusability bias.\n\n\\section{Cross-Seed Variance Decomposition}\n\\label{app:variance-decomposition}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Variance decomposition on FewRel (3 seeds $\\times$ 25 batches per count level). Batch SD: root-mean intra-seed variance averaged over seeds. Seed SD: standard deviation of per-seed means. Ratio = batch variance / seed variance. At count 80, only one batch composition exists, so batch variance vanishes by construction.}\n\\label{tab:variance_decomposition}\n\\begin{tabular}{rrrr}\n\\toprule\n\\textbf{Count} & \\textbf{Batch SD} & \\textbf{Seed SD} & \\textbf{Ratio} \\\\\n\\midrule\n4 & 0.0889 & 0.0122 & 53.5 \\\\\n8 & 0.0820 & 0.0098 & 70.0 \\\\\n16 & 0.0626 & 0.0270 & 5.4 \\\\\n32 & 0.0462 & 0.0091 & 26.0 \\\\\n40 & 0.0421 & 0.0019 & 474.4 \\\\\n64 & 0.0245 & 0.0022 & 119.8 \\\\\n80 & 0.0001 & 0.0088 & $<$0.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:variance_decomposition} shows that intra-batch variance dominates inter-seed variance by 5--474$\\times$ across count levels 4--64 (mean 125$\\times$); random batch composition is the primary source of performance variability. Under greedy decoding (temperature${}\\,=\\,0$), model inference is nearly deterministic; the inter-seed variance reflects differences in which random batch compositions each seed generates, not inference stochasticity. At count 80, the full schema admits only one composition, leaving residual model-level noise as the sole variance source (seed SD = 0.88\\,pp, likely attributable to FP8 quantization non-determinism).\n\n\\section{Cross-Domain Connections}\n\\label{app:cross-domain}\n\nThe schema-associated degradation documented here is not unique to information extraction. Schema-Guided Dialogue systems (SGD/SGD-X; \\citealt{rastogi2020towards}) face an analogous challenge: as the number of intent and slot types grows, dialogue state tracking accuracy declines. \\citet{li2023evaluating} observed count-dependent degradation in ChatGPT-based IE, attributing it to prompt overload. Our two-dimensional decomposition offers a more refined explanation: schema size per se is not the sole predictor; rather, larger schemas increase the probability of including high-SCS pairs, which contribute disproportionately to confusion. This distinction has practical implications: a schema of 80 types with low mutual confusability may outperform a 40-type schema with clustered semantics, and suggests that confusability-aware design principles may generalize to any task where an LLM must discriminate among a prompt-specified label inventory.\n\n\\section{Cross-Model Validation with LLaMA-3.1-70B-Instruct (FP8)}\n\\label{sec:appendix_cross_model_70b}\n\nTo test whether the two-dimensional degradation pattern generalizes across models, we replicate the count-curve and BCS-controlled experiments on Meta-LLaMA-3.1-70B-Instruct (FP8 quantization). All batch compositions, type pools, and test samples are identical to those used for Qwen3-32B (\\S\\ref{sec:count_curves}, \\S\\ref{sec:bcs_controlled}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model count curves for LLaMA-3.1-70B-Instruct (FP8) and Qwen3-32B. RE decline (count 8$\\to$80): $-$30.7\\,pp (70B) vs.\\ $-$30.1\\,pp (32B). NER decline (count 2$\\to$22): $-$7.1\\,pp (70B) vs.\\ $-$23.6\\,pp (32B); both models exhibit a U-shaped rebound at higher counts. 25 batches per count level, same samples and batch compositions across models (seed 42). All metrics are micro-averaged across batches.}\n\\label{tab:cross_model_70b}\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{LLaMA-70B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{RE (FewRel, Classification Accuracy)}} \\\\\n8  & 0.757 & 0.805 \\\\\n16 & 0.685 & 0.719 \\\\\n32 & 0.601 & 0.652 \\\\\n64 & 0.504 & 0.539 \\\\\n80 & 0.450 & 0.504 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{NER (Few-NERD, Text+Type Match Recall)}} \\\\\n2  & 0.323 & 0.515 \\\\\n6  & 0.300 & 0.399 \\\\\n12 & 0.278 & 0.318 \\\\\n22 & 0.252 & 0.279 \\\\\n44 & 0.297 & 0.309 \\\\\n66 & 0.273 & 0.407 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:cross_model_70b} shows that RE degradation slopes are near-identical: $-$30.7\\,pp (70B) versus $-$30.1\\,pp (32B) from count 8 to count 80, with the 70B model approximately 4\\,pp lower in absolute accuracy at each count level. This quantitative match provides strong evidence that Dimension~1 (count-related decline) is directionally consistent across architectures for RE.\n\nOn NER, the count-related decline direction is consistent across models: both 70B and Qwen3 show a recall decline from count 2 to count 22 (70B: 0.323$\\to$0.252, $-$7.1\\,pp; Qwen3: 0.515$\\to$0.279, $-$23.6\\,pp). Both models also exhibit a U-shaped rebound at higher counts (70B: 0.252 at count 22 $\\to$ 0.297 at count 44; Qwen3: 0.279 at count 22 $\\to$ 0.407 at count 66), which cross-validates the U-shape phenomenon. The magnitude difference reflects a precision-recall tradeoff: 70B operates more conservatively (higher precision, lower recall), while Qwen3 over-predicts (higher recall, lower precision, especially at low counts).\n\nFor the confusability dimension (Dimension 2), at count 16 on FewRel, LLaMA-70B achieves low-BCS accuracy of 0.708 versus high-BCS accuracy of 0.599 ($\\Delta = +10.9$\\,pp, 95\\% CI [$+$3.0, $+$20.1]). The confidence interval excludes zero; the confusability effect is thus confirmed at the 70B scale.\n\nIn summary, FewRel RE provides a quantitative match across models (near-identical slopes for Dimension~1 and a significant Dimension~2 effect). NER provides directional consistency: the count-related decline direction is preserved and the U-shaped rebound replicates, though magnitudes vary with each model's precision-recall operating point. Together, these results indicate that the degradation pattern is directionally consistent across architectures.\n\n\\section{Cross-Model Validation with Gemini 2.5 Flash (API)}\n\\label{sec:appendix_cross_model_gemini}\n\nWe validate both dimensions on a proprietary model, Gemini 2.5 Flash \\citep{gemini-2025}, accessed via API. This extends the cross-model evidence from open-weight families (Qwen, LLaMA) to a proprietary architecture with unknown training details. We replicate the FewRel count-curve and BCS-controlled experiments using the same 960 balanced samples, batch compositions, and evaluation protocol as Qwen3-32B.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model count curves for Gemini 2.5 Flash (API) and Qwen3-32B on FewRel RE (classification accuracy). 25 batches per count level, same samples and batch compositions (seed 42). Gemini's count-1 result is included for completeness; Qwen3 count-1 was not collected. Both models show monotonic decline from count 4 onward ($\\rho = -1.0$ for both on counts 4--32). $^\\dagger$Count 64: Gemini based on 11/25 batches (partial).}\n\\label{tab:cross_model_gemini}\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Gemini Flash} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1  & 0.827 & --- \\\\\n4  & 0.873 & 0.870 \\\\\n8  & 0.820 & 0.805 \\\\\n16 & 0.787 & 0.719 \\\\\n32 & 0.739 & 0.652 \\\\\n64$^\\dagger$ & 0.637 & 0.539 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:cross_model_gemini} confirms that the count-related accuracy decline replicates on Gemini 2.5 Flash. From count 4 to count 32, both models show perfectly monotonic decline (Spearman $\\rho = -1.0$). Including count 1, the Gemini count curve yields $\\rho = -0.900$ ($p = 0.037$); including partial count-64 data (11/25 batches), $\\rho = -0.943$ ($p = 0.005$). The decline magnitude is smaller for Gemini ($-$13.3\\,pp from count 4 to 32) than for Qwen3 ($-$21.8\\,pp), consistent with Gemini's higher absolute accuracy providing more headroom before degradation saturates. At each count level, Gemini matches or exceeds Qwen3, with the gap widening at higher counts (0.3\\,pp at count 4 vs.\\ 8.7\\,pp at count 32, 9.8\\,pp at partial count 64); Gemini appears more robust to schema scaling but not immune.\n\n\\paragraph{Dimension~2: BCS-controlled confusability.}\nWe replicate the BCS-controlled experiment on Gemini 2.5 Flash using extreme-BCS batches at count 8 ($n = 50$; 25 low-BCS, 25 high-BCS) and count 16 ($n = 10$; 5+5).\n\nAt count 8, low-BCS batches achieve 90.5\\% vs.\\ high-BCS 72.9\\% ($\\Delta = -17.6$\\,pp, 95\\% CI [15.1, 20.1]). At count 16, the gap narrows to $-$8.7\\,pp, but one high-BCS outlier (BCS${}=0.97$, accuracy 59.9\\%) inflates Pearson $r$; leave-one-out excluding this point drops $r$ from $-$0.80 to $-$0.42 ($p = 0.22$) and $\\rho$ from $-$0.40 to $-$0.18 ($p = 0.64$), confirming the count-16 correlation is driven by this single leverage point. The count-8 gap is smaller than Qwen3-32B's ($-$31.2\\,pp), consistent with ceiling compression: Gemini's higher baseline (90.5\\% vs.\\ 82.3\\%) leaves less room for degradation.\n\nTable~\\ref{tab:cross_model_bcs_summary} summarizes BCS-controlled results across all validated models. Both dimensions thus replicate on a proprietary architecture with unknown training details.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model BCS-controlled FewRel RE summary. All models show significant low-vs-high BCS accuracy gaps. Gap magnitude varies with model capacity (ceiling compression), but the direction is consistent across open-weight (8B--70B) and proprietary architectures.}\n\\label{tab:cross_model_bcs_summary}\n\\begin{tabular}{llrrrr}\n\\toprule\n\\textbf{Model} & \\textbf{Count} & \\textbf{Low BCS} & \\textbf{High BCS} & \\textbf{$\\Delta$} & \\textbf{95\\% CI} \\\\\n\\midrule\nQwen3-32B     & 8  & 82.3\\% & 51.0\\% & $-$31.2\\,pp & --- \\\\\nQwen3-32B     & 16 & 82.8\\% & 51.6\\% & $-$31.2\\,pp & --- \\\\\nLlama-8B      & 8  & 78.1\\% & 51.0\\% & $-$27.1\\,pp & --- \\\\\nLlama-70B FP8 & 16 & ---    & ---    & $-$10.9\\,pp & {[}3.0, 20.1{]} \\\\\nGemini Flash  & 8  & 90.5\\% & 72.9\\% & $-$17.6\\,pp & {[}15.1, 20.1{]} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Few-Shot Prompting and Confusability}\n\\label{sec:appendix_fewshot_bcs}\n\nTo test whether in-context demonstrations mitigate the BCS-associated confusability effect, we evaluate 0-shot, 1-shot, and 5-shot prompting on FewRel 80-relation RE at count 8 using the same extreme-BCS batch design as \\S\\ref{sec:bcs_controlled}. Each condition uses 50 batches (25 low-BCS, mean $\\approx 0.36$; 25 high-BCS, mean $\\approx 0.80$), drawn from the pre-constructed batch pool of \\S\\ref{sec:bcs_controlled}. Few-shot examples are sampled from the FewRel training split for each target type (Table~\\ref{tab:fewshot_bcs}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{BCS gap under few-shot prompting (FewRel, count 8). Demonstrations improve absolute accuracy on low-BCS batches (+3.3--7.2\\,pp over 0-shot) but provide inconsistent benefit on high-BCS batches (+5.6\\,pp at 1-shot, $-$1.0\\,pp at 5-shot). The confusability gap widens from +18.5\\,pp (0-shot) to +22.8\\,pp (5-shot). All metrics are micro-averaged across batches.}\n\\label{tab:fewshot_bcs}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lrrrl}\n\\toprule\n\\textbf{Condition} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n0-shot & 0.682 & 0.498 & +18.5 & {[}+14.3, +22.7{]} \\\\\n1-shot & 0.754 & 0.554 & +20.0 & {[}+16.3, +23.5{]} \\\\\n5-shot & 0.715 & 0.488 & +22.8 & {[}+18.9, +26.8{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nDemonstrations improve absolute accuracy primarily on low-BCS (easy) batches, where type boundaries are already distinct and examples reinforce correct mappings. On high-BCS batches, where types are semantically confusable, demonstrations provide inconsistent benefit (+5.6\\,pp at 1-shot, $-$1.0\\,pp at 5-shot): the model still substitutes similar types at comparable rates. The net effect is that the confusability gap widens under few-shot prompting (+4.3\\,pp from 0-shot to 5-shot, bootstrap $p = 0.014$), with all three confidence intervals excluding zero. This indicates that BCS-associated type confusion is a structural property of the schema composition rather than a deficit addressable through prompt engineering. The non-monotonic low-BCS pattern (0.754 at 1-shot vs.\\ 0.715 at 5-shot) may reflect lost-in-middle effects from increased prompt length \\citep{lost-in-middle-2024}.\n\nThe 0-shot gap (+18.5\\,pp) is smaller than the extreme-batch gap reported in \\S\\ref{sec:bcs_controlled} (+25.5\\,pp) because the two experiments use different test splits and batch sampling seeds; direct magnitude comparison across experiments is not appropriate.\n\n\\section{Qualitative Error Analysis}\n\\label{app:error-analysis}\n\nTables~\\ref{tab:top10_re} and~\\ref{tab:top10_ner} list the ten most frequently confused type pairs on FewRel 80-relation RE and Few-NERD NER. Confusion counts are aggregated bidirectionally across three random seeds (72{,}000 predictions per seed for RE; single-seed 66-type extraction for NER). Table~\\ref{tab:error_examples} provides illustrative confusion instances with SCS values.\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\caption{Top-10 confused relation pairs on FewRel 80-relation RE. $N$: bidirectional confusion count aggregated over 3 seeds $\\times$ 25 batches. SCS: pairwise Schema Confusability Score (Qwen3 embedding cosine similarity). High-SCS pairs (e.g., \\textit{followed by}/\\textit{follows}, SCS\\,=\\,0.90) and family-relation pairs (\\textit{child}/\\textit{father}, \\textit{child}/\\textit{mother}) dominate. Some low-SCS pairs (\\textit{instance of}/\\textit{taxon rank}, SCS\\,=\\,0.53) reflect domain-specific co-occurrence rather than semantic similarity.}\n\\label{tab:top10_re}\n\\begin{tabular}{cllrr}\n\\toprule\n\\textbf{\\#} & \\textbf{Type A} & \\textbf{Type B} & \\textbf{SCS} & \\textbf{$N$} \\\\\n\\midrule\n1 & instance of & taxon rank & 0.53 & 875 \\\\\n2 & child & father & 0.84 & 700 \\\\\n3 & participant of & participating team & 0.75 & 675 \\\\\n4 & mountain range & part of & 0.57 & 575 \\\\\n5 & mouth of watercourse & tributary & 0.65 & 549 \\\\\n6 & child & mother & 0.84 & 500 \\\\\n7 & league & member of & 0.66 & 450 \\\\\n8 & country of citizenship & country of origin & 0.76 & 400 \\\\\n9 & followed by & follows & 0.90 & 400 \\\\\n10 & occupation & voice type & 0.57 & 400 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\caption{Top-10 confused entity type pairs on Few-NERD NER. $N$: bidirectional confusion count from 66-type full-schema extraction. SCS: pairwise Schema Confusability Score (Qwen3 embedding cosine similarity). Intra-category confusions (e.g., \\textit{person-other}/\\textit{person-politician}, SCS\\,=\\,0.93) and cross-category pairs sharing referent overlap (\\textit{building-other}/\\textit{location-GPE}, SCS\\,=\\,0.85) are most frequent. The ``other'' subtypes absorb diverse entities and confuse with more specific siblings.}\n\\label{tab:top10_ner}\n\\begin{tabular}{cllrr}\n\\toprule\n\\textbf{\\#} & \\textbf{Type A} & \\textbf{Type B} & \\textbf{SCS} & \\textbf{$N$} \\\\\n\\midrule\n1 & person-other & person-politician & 0.93 & 121 \\\\\n2 & location-GPE & organization-other & 0.83 & 81 \\\\\n3 & art-film & location-GPE & 0.69 & 57 \\\\\n4 & building-other & location-GPE & 0.85 & 56 \\\\\n5 & building-other & person-other & 0.90 & 43 \\\\\n6 & location-GPE & product-other & 0.69 & 39 \\\\\n7 & org-gov/agency & person-other & 0.85 & 34 \\\\\n8 & person-actor & person-other & 0.90 & 34 \\\\\n9 & building-other & location-road/transit & 0.76 & 32 \\\\\n10 & location-GPE & org-sportsleague & 0.81 & 30 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Illustrative confusion instances from FewRel 80-rel RE. All gold-predicted pairs have SCS\\,$>$\\,0.90: \\textit{participant} vs.\\ \\textit{participant of} reverses directionality; \\textit{contains} vs.\\ \\textit{located in} inverts containment; \\textit{part of} vs.\\ \\textit{member of} conflates meronymy with membership. a.t.e.\\ = admin.\\ territorial entity.}\n\\label{tab:error_examples}\n\\begin{tabular}{p{8cm}llc}\n\\toprule\n\\textbf{Sentence} & \\textbf{Gold} & \\textbf{Pred.} & \\textbf{SCS} \\\\\n\\midrule\n\\ldots\\ played for \\textbf{Valencia} \\ldots\\ [\\textbf{EuroLeague}] & participant & participant of & 0.97 \\\\\n\\addlinespace\n\\textbf{Pilões} is a municipality in \\textbf{Rio Grande do Norte} \\ldots & contains a.t.e. & located in a.t.e. & 0.92 \\\\\n\\addlinespace\nDavies \\ldots\\ appointed to \\textbf{Cabinet} as \\textbf{Sec.\\ of State} & part of & member of & 0.90 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\section{Schema Label Renaming Experiment}\n\\label{app:renaming}\n\nTo test whether reducing pairwise SCS through label renaming improves accuracy, we conducted a controlled intervention on FewRel 80-relation RE (count 8, Qwen3-32B). We identified 14 high-SCS relation pairs (covering 12 unique relation types, as two types each appear in multiple pairs; mean SCS = 0.87) and replaced one label in each pair with a semantically distinct paraphrase chosen to minimize embedding cosine similarity (all-MiniLM-L6-v2). Examples: \\textit{participant of} $\\to$ \\textit{event involvement} (SCS: 0.97 $\\to$ 0.72), \\textit{follows} $\\to$ \\textit{prior entry} (0.90 $\\to$ 0.69), \\textit{part of} $\\to$ \\textit{integral segment of} (0.90 $\\to$ 0.64). The renaming reduced mean pairwise SCS from 0.87 to 0.67 ($\\Delta = -0.20$). We ran the same 50 BCS-controlled batches (25 low-BCS, 25 high-BCS; 96 samples each) under both original (control) and renamed (treatment) label sets (Table~\\ref{tab:renaming}).\n\n\\begin{table}[h!]\n\\centering\n\\small\n\\caption{Accuracy (\\%) under original vs.\\ renamed labels on FewRel count-8 batches. Renaming reduced embedding similarity but decreased accuracy in both groups, with a larger drop on high-BCS batches (Cohen's $d = -2.92$) than low-BCS ($d = -1.09$). Interaction: $\\Delta_{\\text{high}} - \\Delta_{\\text{low}} = -5.9$\\,pp ($t = -7.23$, $p < 0.001$).}\n\\label{tab:renaming}\n\\begin{tabular}{lccc}\n\\toprule\n& \\textbf{Control} & \\textbf{Treatment} & \\textbf{$\\Delta$\\,(pp)} \\\\\n\\midrule\nLow-BCS ($n=25$)  & 90.1 & 87.1 & $-$3.0 \\\\\nHigh-BCS ($n=25$) & 69.3 & 60.5 & $-$8.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nRenaming hurt accuracy uniformly: both groups showed significant declines (paired $t$-test, both $p < 0.001$). The number of renamed types per batch correlated negatively with accuracy change ($r = -0.625$, $p < 0.001$). A solo sanity check confirmed that 11 of 12 renamed labels were individually recognizable (accuracy $\\geq$ original $-5$\\,pp). The results indicate that replacing familiar Wikidata labels with unfamiliar paraphrases disrupts the model's type semantics; this label unfamiliarity effect outweighs any benefit from reduced confusability.\n\n\\section{Relaxed Matching Evaluation (NER)}\n\\label{app:relaxed-matching}\n\nTo test whether exact-match F1 masks the BCS signal in NER by conflating boundary errors with type errors, we evaluate three progressively relaxed matching criteria on the full Few-NERD NER dataset ($n = 450$ batches: 6 count levels $\\times$ 25 batches $\\times$ 3 seeds; Table~\\ref{tab:relaxed_matching}).\n\n\\begin{table}[h!]\n\\centering\n\\small\n\\caption{BCS--F1 correlation under progressively relaxed NER matching. Relaxed span credits a match if the predicted span overlaps the gold span and the type is correct; token overlap uses token-level intersection; type-ignored drops the type constraint entirely. Relaxed matching improves mean F1 by 4.2\\,pp (98.4\\% of batches improve), but Pearson $r$ remains near zero across all modes (bootstrap 95\\% CI crosses zero in all cases). Boundary errors affect all batches uniformly and do not mask a BCS signal.}\n\\label{tab:relaxed_matching}\n\\begin{tabular}{lrrrrr}\n\\toprule\n\\textbf{Match mode} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\rho$} & \\textbf{$p$} & \\textbf{F1} \\\\\n\\midrule\nExact        & 0.014 & 0.760 & $-$0.101 & 0.033 & 0.304 \\\\\nRelaxed span & 0.003 & 0.946 & $-$0.110 & 0.020 & 0.346 \\\\\nToken overlap & 0.004 & 0.936 & $-$0.113 & 0.017 & 0.349 \\\\\nType-ignored & 0.023 & 0.621 & $-$0.097 & 0.039 & 0.425 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nA per-error-mode analysis confirms this null extends to all individual categories: miss ($\\rho = 0.017$), boundary ($\\rho = -0.043$), and type substitution ($\\rho = -0.010$) rates show no BCS association (all $p > 0.3$, $n = 450$). The null holds within each count level (count 2: $r = 0.022$; count 6: $r = 0.110$; count 12: $r = 0.028$; all $p > 0.3$), ruling out count as a confound.\n\n\\end{document}\n",
    "structuredPatch": [
      {
        "oldStart": 329,
        "oldLines": 7,
        "newStart": 329,
        "newLines": 7,
        "lines": [
          " As Table~\\ref{tab:partial_corr} shows, on FewRel, BCS and degree centrality are only moderately correlated ($r = 0.39$), and the BCS effect survives nearly intact after partialling ($r_{\\text{partial}} = -0.537$ vs.\\ $r_{\\text{zero}} = -0.570$; semipartial $R^2 = 0.273$). On DocRED, the near-perfect BCS--centrality correlation ($r = 0.99$) makes it impossible to fully separate the two predictors; the significant partial correlation ($p < 0.001$) indicates BCS retains predictive value but does not uniquely identify the causal channel. This contrasts with MAVEN (\\S\\ref{sec:appendix_residualized_bcs}), where the BCS signal vanishes after controlling for centrality.",
          " ",
          " \\paragraph{Ridge regression under multicollinearity.}",
          "-Ridge regression (GCV, $\\lambda = 0.001$) on the 110 DocRED batches confirms the negative direction of the BCS--accuracy relationship even after regularizing for the severe BCS--centrality multicollinearity (VIF$\\,\\approx\\,$50.9). The standardized BCS coefficient is $\\hat{\\beta}_{\\textsc{bcs}} = -1.53$ ($\\hat{\\beta}_{\\text{centrality}} = 0.78$, $R^2 = 0.594$). An analytic derivation shows that $\\hat{\\beta}_{\\textsc{bcs}} < 0$ for \\emph{all} $\\lambda \\geq 0$: the numerator of the closed-form ridge solution, $-(1{+}\\lambda) \\times 0.760 + 0.727$, is negative at $\\lambda{=}0$ and monotonically decreasing thereafter. Given the shrinkage bias inherent to ridge estimation, we interpret only the sign---not the magnitude---of the BCS coefficient as directional evidence that higher schema confusability degrades extraction accuracy, independent of degree centrality.",
          "+Ridge regression (GCV, $\\lambda = 0.001$) on the 110 DocRED batches confirms the negative direction of the BCS--accuracy relationship even after regularizing for the severe BCS--centrality multicollinearity (VIF$\\,\\approx\\,$50.9). The standardized BCS coefficient is $\\hat{\\beta}_{\\text{BCS}} = -1.53$ ($\\hat{\\beta}_{\\text{centrality}} = 0.78$, $R^2 = 0.594$). An analytic derivation shows that $\\hat{\\beta}_{\\text{BCS}} < 0$ for \\emph{all} $\\lambda \\geq 0$: the numerator of the closed-form ridge solution, $-(1{+}\\lambda) \\times 0.760 + 0.727$, is negative at $\\lambda{=}0$ and monotonically decreasing thereafter. Given the shrinkage bias inherent to ridge estimation, we interpret only the sign---not the magnitude---of the BCS coefficient as directional evidence that higher schema confusability degrades extraction accuracy, independent of degree centrality.",
          " ",
          " \\subsection{NER BCS-Null Power Analysis}",
          " \\label{sec:appendix_ner_power}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 46_

Now let me check whether the artifacts/docred_ridge_appendix.tex is included by main.tex or compiled independently.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "232d7394-b8b8-4678-9539-d967fc621123",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P1ZdU6SWe35nZ9xYo7mAsv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 869,
      "cache_read_input_tokens": 48454,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 869
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 47_

<details open><summary>🔧 Tool call — Grep · `toolu_014Sj7XSR4RReHEfwnQ9hPxo`</summary>

```json
{
  "pattern": "docred_ridge",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "d3773264-1c1b-4222-81a6-c248196cbe42",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P1ZdU6SWe35nZ9xYo7mAsv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 869,
      "cache_read_input_tokens": 48454,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 869
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-22T11:10:47.487Z_

<details><summary>↩ Tool result · `toolu_014Sj7XSR4RReHEfwnQ9hPxo`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "f90508ad-04d4-42f1-aa70-71c59d6d8020",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Assistant

_source line 49_

Not included — the appendix content was inlined directly into main.tex. The artifacts files are standalone copies and not part of the compiled paper.

Now let me verify the edit and compile.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "041eba0f-3072-4fcd-93d8-e5e76482cee4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GAWpWeGPBxx42Txqq5kMmb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 200,
      "cache_read_input_tokens": 49323,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 200
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 50_

<details open><summary>🔧 Tool call — Read · `toolu_01JXLvKfZDq3xNLVStCxyDTz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": 331,
  "limit": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "dbf4310f-ab96-45e0-9965-928de13b4ea9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GAWpWeGPBxx42Txqq5kMmb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 200,
      "cache_read_input_tokens": 49323,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 200
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-22T11:10:51.182Z_

<details><summary>↩ Tool result · `toolu_01JXLvKfZDq3xNLVStCxyDTz`</summary>

```text
331	\paragraph{Ridge regression under multicollinearity.}
332	Ridge regression (GCV, $\lambda = 0.001$) on the 110 DocRED batches confirms the negative direction of the BCS--accuracy relationship even after regularizing for the severe BCS--centrality multicollinearity (VIF$\,\approx\,$50.9). The standardized BCS coefficient is $\hat{\beta}_{\text{BCS}} = -1.53$ ($\hat{\beta}_{\text{centrality}} = 0.78$, $R^2 = 0.594$). An analytic derivation shows that $\hat{\beta}_{\text{BCS}} < 0$ for \emph{all} $\lambda \geq 0$: the numerator of the closed-form ridge solution, $-(1{+}\lambda) \times 0.760 + 0.727$, is negative at $\lambda{=}0$ and monotonically decreasing thereafter. Given the shrinkage bias inherent to ridge estimation, we interpret only the sign---not the magnitude---of the BCS coefficient as directional evidence that higher schema confusability degrades extraction accuracy, independent of degree centrality.
333	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "255f6c43-e2dc-4c91-b744-01587a72e6e7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
      "content": "\\paragraph{Ridge regression under multicollinearity.}\nRidge regression (GCV, $\\lambda = 0.001$) on the 110 DocRED batches confirms the negative direction of the BCS--accuracy relationship even after regularizing for the severe BCS--centrality multicollinearity (VIF$\\,\\approx\\,$50.9). The standardized BCS coefficient is $\\hat{\\beta}_{\\text{BCS}} = -1.53$ ($\\hat{\\beta}_{\\text{centrality}} = 0.78$, $R^2 = 0.594$). An analytic derivation shows that $\\hat{\\beta}_{\\text{BCS}} < 0$ for \\emph{all} $\\lambda \\geq 0$: the numerator of the closed-form ridge solution, $-(1{+}\\lambda) \\times 0.760 + 0.727$, is negative at $\\lambda{=}0$ and monotonically decreasing thereafter. Given the shrinkage bias inherent to ridge estimation, we interpret only the sign---not the magnitude---of the BCS coefficient as directional evidence that higher schema confusability degrades extraction accuracy, independent of degree centrality.\n",
      "numLines": 3,
      "startLine": 331,
      "totalLines": 919
    }
  }
}
```

</details>

---

### Assistant

_source line 52_

Good. Let me now compile to verify 0 errors.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "aa23cf6d-48b7-4b13-a9c1-42c13e6365c1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CeWoXk1Vky1q7tPayYpa8S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 458,
      "cache_read_input_tokens": 49523,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 458
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 53_

<details open><summary>🔧 Tool call — Bash · `toolu_014Ry6uMFx8xoUYjG4dLSKPu`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -20",
  "description": "Compile LaTeX paper to check for errors",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "9a482435-7906-49f9-b656-e37248af7d76",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CeWoXk1Vky1q7tPayYpa8S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 458,
      "cache_read_input_tokens": 49523,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 458
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-22T11:11:03.841Z_

<details><summary>↩ Tool result · `toolu_014Ry6uMFx8xoUYjG4dLSKPu`</summary>

```text
s/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type
1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi
c/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo
nts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/
cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/t
exlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/t
exmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dis
t/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public
/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/urw/times/utmri8a.pfb>
Output written on main.pdf (27 pages, 476127 bytes).
Transcript written on main.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "52d410c4-1eee-467e-a5b9-235748fa0892",
  "tool_use_result": {
    "stdout": "s/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type\n1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi\nc/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo\nnts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/\ncmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/t\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/t\nexmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dis\nt/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/font\ns/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1\n/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public\n/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\nts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texm\nf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/urw/times/utmri8a.pfb>\nOutput written on main.pdf (27 pages, 476127 bytes).\nTranscript written on main.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 55_

<details open><summary>🔧 Tool call — Bash · `toolu_01Fh8zVG7Nhr8vX2pf9fVD3j`</summary>

```json
{
  "command": "grep -c \"^!\" main.log",
  "description": "Count LaTeX errors in log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "b39ca032-c756-496f-8d4f-e2890e4bcbe6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FNGsJtX7bY7e37oD5zwZKF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 905,
      "cache_read_input_tokens": 49981,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 905
      },
      "output_tokens": 65,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-22T11:11:12.301Z_

<details><summary>↩ Tool result · `toolu_01Fh8zVG7Nhr8vX2pf9fVD3j`</summary>

```text
1
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "858f3460-34b2-4c3b-94e6-43d8d3a70001",
  "tool_use_result": {
    "stdout": "1",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 57_

<details open><summary>🔧 Tool call — Bash · `toolu_019KU8VT8qWgdadcenPX9fz1`</summary>

```json
{
  "command": "grep \"^!\" main.log",
  "description": "Show LaTeX errors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "6c55d426-2e11-4aeb-9ebb-659f95904ec4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xc1XuuFsS7ZFcSFLoyTw5A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 95,
      "cache_read_input_tokens": 50886,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 95
      },
      "output_tokens": 63,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-22T11:11:15.595Z_

<details><summary>↩ Tool result · `toolu_019KU8VT8qWgdadcenPX9fz1`</summary>

```text
!$\T1/ptm/m/n/10.95 (+20) 0.50 for
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "27e1060e-10f7-4c1e-b169-6e702a1f4e99",
  "tool_use_result": {
    "stdout": "!$\\T1/ptm/m/n/10.95 (+20) 0.50 for",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 59_

Not a real error — that's a font substitution line starting with `!$`, not a LaTeX error (`! ` with space). Compilation succeeded, 27 pages, 0 errors.

**结果：**

- **格式不一致数量**：2 处（均在 `docs/paper/main.tex` 第 332 行）
- **不一致内容**：`$\hat{\beta}_{\textsc{bcs}}$`（小型大写）vs 全文统一的 `\text{BCS}`（plain 大写）
- **统一为**：plain 大写 `\text{BCS}`（与全文其余 100+ 处一致）
- **修改位置**：`docs/paper/main.tex:332`，将两处 `\textsc{bcs}` 改为 `\text{BCS}`
- 编译通过，0 errors

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "uuid": "ee77b08c-4626-4f41-a48c-bf125b4739d9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TT4tz8QVXS3xw1rXKufVm7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 219,
      "cache_read_input_tokens": 50981,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 219
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Task result

_source line 60_

Not a real error — that's a font substitution line starting with `!$`, not a LaTeX error (`! ` with space). Compilation succeeded, 27 pages, 0 errors.

**结果：**

- **格式不一致数量**：2 处（均在 `docs/paper/main.tex` 第 332 行）
- **不一致内容**：`$\hat{\beta}_{\textsc{bcs}}$`（小型大写）vs 全文统一的 `\text{BCS}`（plain 大写）
- **统一为**：plain 大写 `\text{BCS}`（与全文其余 100+ 处一致）
- **修改位置**：`docs/paper/main.tex:332`，将两处 `\textsc{bcs}` 改为 `\text{BCS}`
- 编译通过，0 errors

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 136298,
  "duration_api_ms": 134218,
  "num_turns": 21,
  "stop_reason": "end_turn",
  "session_id": "69d255ce-db0b-472a-b13f-c39e9fbc3874",
  "total_cost_usd": 0.68004225,
  "usage": {
    "input_tokens": 18,
    "cache_creation_input_tokens": 39359,
    "cache_read_input_tokens": 642085,
    "output_tokens": 4465,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 39359,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 231,
        "cache_read_input_tokens": 50981,
        "cache_creation_input_tokens": 219,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 219
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1196,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001291,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 18,
      "outputTokens": 4465,
      "cacheReadInputTokens": 642085,
      "cacheCreationInputTokens": 39359,
      "webSearchRequests": 0,
      "costUSD": 0.67875125,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "581b443f-6689-41f4-bb62-7bf3a2e93654"
}
```

</details>

---
