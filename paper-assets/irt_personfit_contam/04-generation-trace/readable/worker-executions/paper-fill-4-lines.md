# paper fill 4 lines

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/workers/worker_paper_fill-4-lines_20260524T090848.log`
- **Structured JSON:** [`deaa4e6421d04195d66d.json`](../../sessions/de/deaa4e6421d04195d66d.json)

## Before a recorded user message

25 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "session_id": "6cb93ad6-7096-44a6-89f2-a775409efa19",
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
    "mcp__agent-ml-research__clone_repo",
    "mcp__agent-ml-research__detect_image",
    "mcp__agent-ml-research__kill_job",
    "mcp__agent-ml-research__list_repo_tree",
    "mcp__agent-ml-research__read_repo_file",
    "mcp__agent-ml-research__search_repo",
    "mcp__agent-ml-research__ssh_execute",
    "mcp__agent-ml-research__ssh_read_only",
    "mcp__agent-ml-research__sync_code_to_remote"
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
  "uuid": "ff761593-d15f-4d50-9fa6-8d9d3d31544e",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0519-3-projects-irt-personfit-contam/memory/"
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
    "resetsAt": 1779631200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "f4a35e72-262b-407f-b2ad-30d4184910e2",
  "session_id": "6cb93ad6-7096-44a6-89f2-a775409efa19"
}
```

---

### Assistant

_source line 4_

I'll start by compiling the paper to check the current state, and reading the relevant tex files to find expansion points.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6cb93ad6-7096-44a6-89f2-a775409efa19",
  "uuid": "f5f75a03-ad94-4d70-8b31-fb56f191d88b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HXvhK38UqFK88y6HATMxZL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12551,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12551
      },
      "output_tokens": 2,
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

_source line 5_

<details open><summary>🔧 Tool call — Bash · `toolu_01QSty2f9GnAP2BTvyMXYzz5`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/ && pdflatex -interaction=nonstopmode main.tex > /dev/null 2>&1 && bibtex main > /dev/null 2>&1 && pdflatex -interaction=nonstopmode main.tex > /dev/null 2>&1 && pdflatex -interaction=nonstopmode main.tex > /dev/null 2>&1 && pdfinfo main.pdf | grep Pages",
  "description": "Compile paper and check page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6cb93ad6-7096-44a6-89f2-a775409efa19",
  "uuid": "bb1ef6bd-6706-4f16-b914-2b46c603e00e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HXvhK38UqFK88y6HATMxZL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12551,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12551
      },
      "output_tokens": 2,
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

<details open><summary>🔧 Tool call — Bash · `toolu_01GJEQtf1xcqbD4dEoigL7KD`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/_anonymous_repo.json 2>/dev/null",
  "description": "Check anonymous repo config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6cb93ad6-7096-44a6-89f2-a775409efa19",
  "uuid": "e2e4ba95-d215-476f-9127-c51c94d6c5de",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HXvhK38UqFK88y6HATMxZL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12551,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12551
      },
      "output_tokens": 2,
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

_source line 7_

<details open><summary>🔧 Tool call — Glob · `toolu_014k8T82SLHydLcnTgpEWd3P`</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6cb93ad6-7096-44a6-89f2-a775409efa19",
  "uuid": "400d17ab-8db9-461d-ba93-14d37be6b754",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HXvhK38UqFK88y6HATMxZL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12551,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12551
      },
      "output_tokens": 2,
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

### System

_source line 8_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "b69q1kboo",
  "tool_use_id": "toolu_01QSty2f9GnAP2BTvyMXYzz5",
  "description": "Compile paper and check page count",
  "task_type": "local_bash",
  "uuid": "e8fb98c0-e7f4-4167-b13e-4017fefbd991",
  "session_id": "6cb93ad6-7096-44a6-89f2-a775409efa19"
}
```

---

### System

_source line 9_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "b69q1kboo",
  "tool_use_id": "toolu_01QSty2f9GnAP2BTvyMXYzz5",
  "status": "completed",
  "output_file": "",
  "summary": "Compile paper and check page count",
  "uuid": "847df794-c39c-4d85-8082-9782a0407582",
  "session_id": "6cb93ad6-7096-44a6-89f2-a775409efa19"
}
```

---

### Tool result

_source line 10 · 2026-05-24T09:09:12.518Z_

<details><summary>↩ Tool result · `toolu_01QSty2f9GnAP2BTvyMXYzz5`</summary>

```text
Pages:           16
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6cb93ad6-7096-44a6-89f2-a775409efa19",
  "uuid": "ac882daf-dc4d-4e75-b6bd-65d69b6b2131",
  "tool_use_result": {
    "stdout": "Pages:           16",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-24T09:09:12.565Z_

<details><summary>↩ Tool result · `toolu_014k8T82SLHydLcnTgpEWd3P`</summary>

```text
sections/experiments.tex
sections/background.tex
sections/sec_empirical.tex
sections/sec_simulation.tex
sections/sec_setup.tex
sections/sec_ctrl_contam.tex
sections/related_work.tex
sections/introduction.tex
sections/limitations.tex
sections/conclusion.tex
main.tex
sections/abstract.tex
sections/discussion.tex
sections/results.tex
sections/method.tex
sections/appendix.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6cb93ad6-7096-44a6-89f2-a775409efa19",
  "uuid": "c085d19d-dc55-4f05-9619-1afaf90afd06",
  "tool_use_result": {
    "filenames": [
      "sections/experiments.tex",
      "sections/background.tex",
      "sections/sec_empirical.tex",
      "sections/sec_simulation.tex",
      "sections/sec_setup.tex",
      "sections/sec_ctrl_contam.tex",
      "sections/related_work.tex",
      "sections/introduction.tex",
      "sections/limitations.tex",
      "sections/conclusion.tex",
      "main.tex",
      "sections/abstract.tex",
      "sections/discussion.tex",
      "sections/results.tex",
      "sections/method.tex",
      "sections/appendix.tex"
    ],
    "durationMs": 21,
    "numFiles": 16,
    "truncated": false
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-24T09:09:12.630Z_

<details><summary>↩ Tool result · `toolu_01GJEQtf1xcqbD4dEoigL7KD`</summary>

```text
{
  "repo_public": "https://github.com/anonymous-nlp-2026-2/irt_personfit_contam",
  "push_url": "https://[REDACTED]@github.com/anonymous-nlp-2026-2/irt_personfit_contam.git",
  "github_user": "anonymous-nlp-2026-2",
  "repo_name": "irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6cb93ad6-7096-44a6-89f2-a775409efa19",
  "uuid": "5fc517b4-2d28-4640-9942-1432d755c754",
  "tool_use_result": {
    "stdout": "{\n  \"repo_public\": \"https://github.com/anonymous-nlp-2026-2/irt_personfit_contam\",\n  \"push_url\": \"https://[REDACTED]@github.com/anonymous-nlp-2026-2/irt_personfit_contam.git\",\n  \"github_user\": \"anonymous-nlp-2026-2\",\n  \"repo_name\": \"irt_personfit_contam\"\n}",
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

_source line 13_

<details><summary>Logged reasoning block</summary>

```text
16 pages total - that includes references and appendix. I need to check where the main text ends (page 8) and how much space is left. Let me look at the PDF more carefully and read the relevant tex files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6cb93ad6-7096-44a6-89f2-a775409efa19",
  "uuid": "4e338758-373f-4e88-ab3e-8cefdeadf676",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011nPBXgPtdaLmX4w6MucE1g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 139,
      "cache_creation_input_tokens": 631,
      "cache_read_input_tokens": 24392,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 631
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

_source line 14_

16 pages total (includes references + appendix). Let me check where the main text ends and read the candidate expansion files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6cb93ad6-7096-44a6-89f2-a775409efa19",
  "uuid": "775725a8-6010-45fa-8d00-e2570a015153",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011nPBXgPtdaLmX4w6MucE1g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 139,
      "cache_creation_input_tokens": 631,
      "cache_read_input_tokens": 24392,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 631
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

_source line 15_

<details open><summary>🔧 Tool call — Bash · `toolu_013e9ebZ1CVU4KSUWTarC8qJ`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/ && pdftotext main.pdf - 2>/dev/null | head -n 500 | tail -n 100",
  "description": "Check text near page boundaries"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6cb93ad6-7096-44a6-89f2-a775409efa19",
  "uuid": "b1c0772f-cd45-4e52-acdd-e4081613667c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011nPBXgPtdaLmX4w6MucE1g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 139,
      "cache_creation_input_tokens": 631,
      "cache_read_input_tokens": 24392,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 631
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

_source line 16 · 2026-05-24T09:09:17.908Z_

<details><summary>↩ Tool result · `toolu_013e9ebZ1CVU4KSUWTarC8qJ`</summary>

```text
215
216
217
218
219
220
221

2022), but require full corpus access unavailable
for closed models. Membership inference attacks (MIA) use token-level log-probabilities to
distinguish training from unseen examples (Shi
et al., 2024; Deng et al., 2024). Generation-based
probes elicit benchmark content via prompting
(Golchin and Surdeanu, 2024a,b; Oren et al., 2024).
Performance-based methods compare accuracy on
target and reference sets (Dekoninck et al., 2024;
Zhang et al., 2024; Zawalski et al., 2026), requiring
multiple evaluations or in-context learning passes.
Zhou et al. (2023) and Sainz et al. (2023) argue
for systematic contamination measurement, Jacovi
et al. (2023) propose mitigation strategies, and
Bordt et al. (2025) show that contamination can be
“forgotten” under sufficient continued training. Han
et al. (2026) quantify contamination in psychometric evaluations of LLMs, demonstrating that memorization effects extend beyond standard benchmarks. Kattamuri et al. (2025) take a mechanistic
interpretability approach, using activation patterns
to distinguish recall-based from reasoning-based
responses; our work instead operates purely on behavioral response patterns without access to model
internals. Fu et al. (2025) systematically evaluate
detection method assumptions, finding that most
methods degrade under realistic conditions; our
work contributes a psychometric perspective to this
ongoing evaluation.
A critical limitation unites all token-level methods: Wang et al. (2025) show that RL post-training
renders MIA-based detectors no better than random
across 10 methods and 4 benchmarks, because RL
reshapes token distributions while largely preserving binary correctness patterns. Tao et al. (2026)
and Zhang et al. (2026) propose RL-specific solutions but require generation-level access. Our approach requires no access to model weights, logits,
or training data—only binary response patterns and
externally calibrated item parameters from PSNIRT (Zhou et al., 2026).

that IRT-informed item weighting improves leaderboard rankings over raw accuracy. Polo et al.
(2024) used IRT-based item selection to reduce
benchmark sizes by 100× while preserving model
rankings, and Li et al. (2025) developed adaptive
testing procedures for efficient LLM evaluation.
Most directly relevant, Zhou et al. (2026) calibrated
4PL item parameters for over 13,000 models across
11 benchmarks, providing the item bank our framework builds on. All of these works use IRT for
ability estimation or benchmark efficiency; none
apply person-fit statistics for contamination detection.

IRT for LLM evaluation. Item Response Theory has seen growing adoption in NLP and ML
evaluation. Martínez-Plumed et al. (2019) applied
IRT to analyze machine learning classifiers at the
instance level, establishing that item difficulty and
discrimination parameters capture meaningful variation across models. Lalor et al. (2019) proposed
estimating IRT parameters from DNN-generated
response patterns, removing the need for human
annotators. Rodriguez et al. (2021) demonstrated

223
224
225
226
227
228
229
230
231
232
233
234

Person-fit statistics in psychometrics. Personfit analysis has a long history in educational measurement for detecting aberrant test-taking behavior (see Embretson and Reise, 2000, for a textbook
treatment). Levine and Drasgow (1988) formalized optimal appropriateness measurement; Drasgow et al. (1985) introduced ℓz , a standardized
log-likelihood residual; Snijders (2001) derived the
corrected ℓ∗z that accounts for ability estimation uncertainty. Karabatsos (2003) compared 36 personfit statistics and found ℓz among the most powerful
for detecting cheating; Sinharay (2017b) revisited
these simulations and confirmed comparable power
between parametric and nonparametric statistics.
We select ℓ∗z for its theoretical grounding and HT
(Van der Flier, 1982) as a nonparametric complement, following their top-ranked performance in
that comparison. Reise (1990) and Meijer and
Sijtsma (2001) provide systematic evaluations of
person-fit methodology. Sinharay (2017a) showed
that ℓ∗z is particularly effective when the set of compromised items is known, a setting analogous to
benchmark contamination where memorized items
constitute the compromised set. Our work transfers
this psychometric toolkit to LLM evaluation, treating each model as an examinee whose item-level
response pattern may reveal memorization.

235

3

Method

262

3.1
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6cb93ad6-7096-44a6-89f2-a775409efa19",
  "uuid": "28fe01b6-bd8f-4bcc-81bb-201b093844d4",
  "tool_use_result": {
    "stdout": "215\n216\n217\n218\n219\n220\n221\n\n2022), but require full corpus access unavailable\nfor closed models. Membership inference attacks (MIA) use token-level log-probabilities to\ndistinguish training from unseen examples (Shi\net al., 2024; Deng et al., 2024). Generation-based\nprobes elicit benchmark content via prompting\n(Golchin and Surdeanu, 2024a,b; Oren et al., 2024).\nPerformance-based methods compare accuracy on\ntarget and reference sets (Dekoninck et al., 2024;\nZhang et al., 2024; Zawalski et al., 2026), requiring\nmultiple evaluations or in-context learning passes.\nZhou et al. (2023) and Sainz et al. (2023) argue\nfor systematic contamination measurement, Jacovi\net al. (2023) propose mitigation strategies, and\nBordt et al. (2025) show that contamination can be\n“forgotten” under sufficient continued training. Han\net al. (2026) quantify contamination in psychometric evaluations of LLMs, demonstrating that memorization effects extend beyond standard benchmarks. Kattamuri et al. (2025) take a mechanistic\ninterpretability approach, using activation patterns\nto distinguish recall-based from reasoning-based\nresponses; our work instead operates purely on behavioral response patterns without access to model\ninternals. Fu et al. (2025) systematically evaluate\ndetection method assumptions, finding that most\nmethods degrade under realistic conditions; our\nwork contributes a psychometric perspective to this\nongoing evaluation.\nA critical limitation unites all token-level methods: Wang et al. (2025) show that RL post-training\nrenders MIA-based detectors no better than random\nacross 10 methods and 4 benchmarks, because RL\nreshapes token distributions while largely preserving binary correctness patterns. Tao et al. (2026)\nand Zhang et al. (2026) propose RL-specific solutions but require generation-level access. Our approach requires no access to model weights, logits,\nor training data—only binary response patterns and\nexternally calibrated item parameters from PSNIRT (Zhou et al., 2026).\n\nthat IRT-informed item weighting improves leaderboard rankings over raw accuracy. Polo et al.\n(2024) used IRT-based item selection to reduce\nbenchmark sizes by 100× while preserving model\nrankings, and Li et al. (2025) developed adaptive\ntesting procedures for efficient LLM evaluation.\nMost directly relevant, Zhou et al. (2026) calibrated\n4PL item parameters for over 13,000 models across\n11 benchmarks, providing the item bank our framework builds on. All of these works use IRT for\nability estimation or benchmark efficiency; none\napply person-fit statistics for contamination detection.\n\nIRT for LLM evaluation. Item Response Theory has seen growing adoption in NLP and ML\nevaluation. Martínez-Plumed et al. (2019) applied\nIRT to analyze machine learning classifiers at the\ninstance level, establishing that item difficulty and\ndiscrimination parameters capture meaningful variation across models. Lalor et al. (2019) proposed\nestimating IRT parameters from DNN-generated\nresponse patterns, removing the need for human\nannotators. Rodriguez et al. (2021) demonstrated\n\n223\n224\n225\n226\n227\n228\n229\n230\n231\n232\n233\n234\n\nPerson-fit statistics in psychometrics. Personfit analysis has a long history in educational measurement for detecting aberrant test-taking behavior (see Embretson and Reise, 2000, for a textbook\ntreatment). Levine and Drasgow (1988) formalized optimal appropriateness measurement; Drasgow et al. (1985) introduced ℓz , a standardized\nlog-likelihood residual; Snijders (2001) derived the\ncorrected ℓ∗z that accounts for ability estimation uncertainty. Karabatsos (2003) compared 36 personfit statistics and found ℓz among the most powerful\nfor detecting cheating; Sinharay (2017b) revisited\nthese simulations and confirmed comparable power\nbetween parametric and nonparametric statistics.\nWe select ℓ∗z for its theoretical grounding and HT\n(Van der Flier, 1982) as a nonparametric complement, following their top-ranked performance in\nthat comparison. Reise (1990) and Meijer and\nSijtsma (2001) provide systematic evaluations of\nperson-fit methodology. Sinharay (2017a) showed\nthat ℓ∗z is particularly effective when the set of compromised items is known, a setting analogous to\nbenchmark contamination where memorized items\nconstitute the compromised set. Our work transfers\nthis psychometric toolkit to LLM evaluation, treating each model as an examinee whose item-level\nresponse pattern may reveal memorization.\n\n235\n\n3\n\nMethod\n\n262\n\n3.1",
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

_source line 17_

<details open><summary>🔧 Tool call — Bash · `toolu_01VZdMQerLdQpzvZ3RQbDJrK`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/ && python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', '-layout', '-f', '7', '-l', '9', 'main.pdf', '-'], capture_output=True, text=True)\nprint(result.stdout)\n\"",
  "description": "Extract pages 7-9 to see where main text ends"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6cb93ad6-7096-44a6-89f2-a775409efa19",
  "uuid": "2b3fd8b2-588f-4b45-b6c8-c823ee98f6e1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011nPBXgPtdaLmX4w6MucE1g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 139,
      "cache_creation_input_tokens": 631,
      "cache_read_input_tokens": 24392,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 631
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

_source line 18 · 2026-05-24T09:09:19.771Z_

<details><summary>↩ Tool result · `toolu_01VZdMQerLdQpzvZ3RQbDJrK`</summary>

```text
                    10                                                                                Table 3: Detection-diagnosis tradeoff on MMLU: Co-
                               5% contam.
                               15% contam.                                                            hen’s |d| across three statistics. Simpler statistics detect
                               25% contam.
                                                                 Qwen
                               50% contam.                                                            more powerfully; ℓ∗z provides unique diagnostic capabil-
                     8
                                                                                       ceiling
                                                                                       reversal
                                                                                                      ities (§4.3).
                                                                                      Qwen
                                                                                      ARC-C
                     6                                                                                Model        Statistic               |d| (15%)                |d| (50%)

      Cohen's |d|
                                                                                                      Qwen†        ℓ∗z                5.36 (±1.10)              5.08 (±3.02)
                         Mistral
                                                                                                                   HT                 5.83 (±1.30)              5.29 (±3.41)
                     4                             Llama                                                           Acc. z              45.0 (±2.5)               70.0 (±1.1)
                                                                                                      Llama        ℓ∗z             2.11 [1.4, 4.8]           2.33 [1.6, 5.1]
                     2                                                                                             HT              2.45 [1.5, 4.3]           3.07 [1.9, 5.3]
                                                                     -shift
                                                                    absorption                                     Acc. z        22.5 [13.6, 47.0]         32.8 [19.8, 68.6]
                         large effect (0.8)
                                                                                                      Mistral      ℓ∗z              2.64 [1.5, 7.3]           3.50 [2.1, 9.4]
                     0                                                                                             HT               4.36 [1.2, 7.0]           5.89 [1.9, 9.4]
                                 50           60            70              80   90
                                                     Baseline Accuracy (%)                                         Acc. z          7.81 [4.4, 14.4]          16.6 [9.7, 34.6]
                                                                                                      †
                                                                                                       Qwen values are means across n=3 independent seeds (42, 123, 456);
                                                                                                      per-seed values in Appendix L. Llama and Mistral are single-seed with
      Figure 3: Baseline accuracy vs. Cohen’s |d| for all                                             bootstrap CIs.
      model-benchmark combinations (single-seed values;
      multi-seed means in Table 1). Diamonds: 5%; triangles:
      15%; squares: 25%; circles: 50%. ARC-C reversal re-                                             findings in the LLM domain; nonparametric alter-                          534
      flects a ceiling effect.                                                                        natives (Tendeiro and Meijer, 2014) may comple-                           535
                                                                                                      ment ℓ∗z where 4PL calibration is unavailable.                            536
                                                                                                         In practice, a two-stage workflow follows:                             537
503   seed accuracy variance is near-zero in controlled                                               screen using accuracy z-scores (Table 3), then ap-                        538
504   settings. HT generally exceeds ℓ∗z in detection                                                 ply ℓ∗z to characterize whether the signal reflects                       539
505   strength, since HT is not attenuated by the Sni-                                                θ-shift absorption (indicating fixed-θ anchoring is                       540
506   jders correction for θ estimation uncertainty. Both                                             needed) or uniform aberrance (suggesting direct                           541
507   person-fit statistics exhibit seed-dependent non-                                               memorization).                                                            542
508   monotonicity under free-θ estimation (Table 3),                                                    Within the IRT family, the 4PL specification mat-                      543
509   confirming that θ-shift absorption affects all statis-                                          ters: simulation ablations show a mean +27.3pp                            544
510   tics conditioned on ability, not ℓ∗z specifically.                                              power gain over 3PL on MMLU, because 46% of                               545
511      Yet the diagnostic power reverses. Full IRT pa-                                              MMLU items have upper asymptote d < 0.95,                                 546
512   rameterization is unnecessary for mere detection,                                               and the 3PL model (which assumes d=1) misat-                              547
513   but the value of ℓ∗z lies in three capabilities that                                            tributes slip-related response patterns as aberrance                      548
514   HT and z-scores lack: (a) seen/unseen decomposi-                                                (Appendix B).                                                             549
515   tion: ℓ∗z can be computed separately on seen and
516   unseen item subsets, though item-level detection is                                             4.4    Ability-Dependent Non-Monotonic                                    550

517   near-random (AUROC ≈ 0.53; Appendix F), con-                                                           Dose-Response                                                      551

518   firming that the contamination signal is diffuse and                                            As an exploratory observation, the free-θ dose-                           552
519   requires model-level aggregation; (b) θ-shift mech-                                             response is non-monotonic for Qwen. The multi-                            553
520   anism: the ability parameter exposes why detec-                                                 seed mean trajectory (|d|: 4.15 → 5.36 → 7.44 →                           554
521   tion sensitivity depends on model ability (§4.2), a                                             5.08 at 5%/15%/25%/50%; Appendix L) shows                                 555
522   mechanistic insight inaccessible to non-parametric                                              signal peaking at 25% before declining at 50%,                            556
523   statistics; (c) structural sensitivity: on real leader-                                         but the decline is attenuated relative to single-seed                     557
524   board data, ℓ∗z flags 57/60 model-benchmark cells                                               estimates and the inter-seed variance at 50% is                           558
525   as aberrant—evidence of systematic IRT assump-                                                  high (CV=60%, range [1.90, 7.91]). This non-                              559
526   tion violations that motivates the ∆ℓ∗z matched-                                                monotonicity is a θ-estimation artifact: fixed-θ                          560
527   difference design (§3.2; Appendix E). Accuracy z-                                               analysis eliminates the inverted-U and reveals a                          561
528   scores flag only 4/60 cells, making them insensitive                                            strong positive dose-response (mean |d|: 5.89 at                          562
529   to the response-pattern structure that ℓ∗z exploits                                             25% vs. 12.32 at 50%, no seed-level overlap),                             563
530   for within-model diagnosis. While such patterns                                                 while reducing the 50% CV to 19%. Llama shows                             564
531   have theoretical antecedents in person-fit literature                                           an approximately flat dose-response (|d|=2.11 →                           565
532   (St-Onge et al., 2011), the specific magnitude and                                              1.99 → 2.33), consistent with its near-zero ℓ∗z base-                     566
533   model-dependence we observe are new empirical                                                   line (+0.26 vs. +8.68 for Qwen) despite compa-                            567


                                                                                                  7
568   rable θ-shift (∆θ=0.52 vs. 0.47). The mechanism              Scope and calibration. Universal baseline mis-          616
569   is predictable from simulation (Appendix A): at              fit (57/60 cells flagged) confirms systematic IRT       617
570   moderate contamination, aberrant responses dom-              violations; the ∆ℓ∗z design turns this into a feature   618
571   inate; at high contamination, inflated θ̂ absorbs            through within-model differencing. PSN-IRT pro-         619
572   the anomaly—but the magnitude is highly seed-                vides pre-calibrated 4PL parameters (Zhou et al.,       620
573   dependent.                                                   2026), but classical calibration fails on contami-      621
574      A simulated power analysis corroborates these             nated data (ra =0.127; Appendix I); the calibration     622
575   findings: two-sided testing (flagging both large neg-        sample (13,000+ models) may itself include con-         623
576   ative and large positive ℓ∗z ) achieves >93% power           taminated ones, though individual contamination         624
577   on MMLU at all contamination levels, with the the-           effects are diluted across models. The robustness       625
578   oretical power function yielding R2 =0.957 against           analysis (Appendix G.2) provides partial reassur-       626
579   simulated values (Appendix A).                               ance (±10% noise tolerance).                            627


580   5   Discussion                                               Information requirements and method position-           628
                                                                   ing. ℓ∗z sits below MIA (logits; Shi et al., 2024)      629
581   Our findings reveal both the strengths and bound-            and ConStat (multi-benchmark scores; Dekoninck          630
582   aries of IRT person-fit for contamination detection:         et al., 2024) in an information-requirements hier-      631
583   ℓ∗z reliably detects SFT-stage contamination across          archy, needing only single-benchmark binary pat-        632
584   model families, but three boundary conditions con-           terns and an external item bank—suited to retro-        633
585   strain its practical utility.                                spective audits where logits are unavailable. Our       634
                                                                   GRPO pilot directly confirms this advantage: Min-       635
586   Characterization over tool. The detection-                   K% AUC degrades from 0.611 (SFT) to 0.493               636
587   diagnosis tradeoff (§4.3) shows that simpler statis-         (post-RL), indistinguishable from chance, while         637
588   tics detect contamination more powerfully than ℓ∗z :         ℓ∗z signal persists (∼3.3; Figure 4; Appendix J),       638
589   accuracy z-scores yield |d| values several-fold to           demonstrating that response-pattern anomalies sur-      639
590   over an order of magnitude larger, and HT gener-             vive RL alignment that eliminates memorization-         640
591   ally exceeds ℓ∗z . The value of the IRT framework            based features (Wang et al., 2025).                     641
592   lies not in detection power but in mechanistic under-
593   standing: the θ-shift analysis reveals why detection         6   Conclusion                                          642
594   sensitivity varies across models and contamination
595   levels, the seen/unseen decomposition identifies             We characterized IRT person-fit statistics for LLM      643
596   what fraction of items are memorized, and the 4PL            contamination detection across three 7–8B model         644
597   parameterization captures item-level ceiling effects         families, establishing reliable SFT-stage detection     645
598   that 3PL misattributes as aberrance. These diagnos-          while identifying boundary conditions: θ-shift ab-      646
599   tic capabilities are invisible to accuracy z-scores or       sorption necessitating θ-anchored estimation for        647
600   HT. Findings 1–2 are theoretically predictable from          high-ability models, a detection-diagnosis trade-       648
601   IRT principles; our contribution lies in quantifying         off, and non-monotonic dose-response as a θ-            649
602   these effects in the LLM setting, where the mag-             estimation artifact. For practitioners, we recom-       650
603   nitude and boundary conditions are not derivable             mend a two-stage workflow: accuracy z-scores            651
604   from theory alone.                                           for efficient screening, followed by ℓ∗z analy-         652
                                                                   sis when mechanistic understanding is needed—           653
605   Practical implications. Two results have imme-               distinguishing which items drive aberrance rather       654
606   diate consequences. Free-θ estimation produces               than merely flagging contamination. Beyond de-          655
607   seed-dependent dose-response curves (CV up to                tection, our characterization reveals that person-fit   656
608   60%); anchoring θ to a pre-contamination base-               statistics capture structural response-pattern anoma-   657
609   line stabilizes detection and amplifies the signal for       lies that persist even after RL post-training erases    658
610   models whose clean ℓ∗z departs substantially from            memorization-based signals, suggesting a comple-        659
611   zero. The benchmark size boundary means ℓ∗z is               mentary role to logit-based methods in the eval-        660
612   most informative for large benchmarks (n ≈ 8,000             uation integrity toolkit. Future work should ad-        661
613   items for 80% power at 15% contamination); on                dress pretraining-stage signatures, broader model       662
614   small benchmarks like ARC-C (295 items), detec-              scales, and cross-benchmark generalization with         663
615   tion relies on concentrated contamination effects.           larger item banks.                                      664


                                                               8
665   Limitations                                                  C. Deng, Y. Zhao, X. Tang, M. Gerstein, and A. Cohan.      714
                                                                      2024. Investigating data contamination in modern        715
666   Our controlled experiments cover three 7–8B                     benchmarks for large language models. In Proceed-       716
667   model families with QLoRA fine-tuning; general-                 ings of the 2024 Conference of the North American       717
668   ization to larger scales, mixture-of-experts architec-          Chapter of the Association for Computational Lin-       718
                                                                      guistics (NAACL).                                       719
669   tures, full-parameter fine-tuning, and pretraining-
670   stage contamination remains untested. Most con-              J. Dodge, M. Sap, A. Marasović, W. Agnew, G. Ilharco,     720
671   tamination conditions use a single training run,                D. Groeneveld, M. Mitchell, and M. Gardner. 2021.       721
672   and multi-seed replication (available for Qwen) re-             Documenting large webtext corpora: A case study on      722
                                                                      the colossal clean crawled corpus. In Proceedings       723
673   veals high seed dependence at 50% contamination                 of the 2021 Conference on Empirical Methods in          724
674   (CV=60%), partially resolved by θ-anchoring; the                Natural Language Processing (EMNLP).                    725
675   post-RL characterization is N =1. The framework
676   depends on pre-calibrated 4PL item parameters                F. Drasgow, M. V. Levine, and E. A. Williams. 1985.        726
677   from PSN-IRT, whose calibration sample may in-                  Appropriateness measurement with polychotomous          727
                                                                      item response models and standardized indices.          728
678   clude contaminated models, and we do not provide                British Journal of Mathematical and Statistical Psy-    729
679   head-to-head comparison with logit-based methods                chology, 38(1):67–86.                                   730
680   (MIA, ConStat) that operate at a different informa-
681   tion level.                                                  Susan E. Embretson and Steven P. Reise. 2000. Item Re-     731
                                                                     sponse Theory for Psychologists. Lawrence Erlbaum        732
                                                                     Associates, Mahwah, NJ.                                  733
682   Reproducibility Statement
683   Code and response data will be released upon ac-             Yujuan Fu, Ozlem Uzuner, Meliha Yetisgen, and Fei          734
                                                                     Xia. 2025. Does data contamination detection work        735
684   ceptance. Bootstrap confidence intervals use the               (well) for LLMs? A survey and evaluation on detec-       736
685   percentile method with 10,000 resamples. All                   tion assumptions. In Findings of the Association for     737
686   three model families use clean baseline seeds 0–9              Computational Linguistics: NAACL 2025.                   738
687   (n=10 per family). Pre-calibrated 4PL item param-
688   eters are from the publicly available PSN-IRT item           S. Golchin and M. Surdeanu. 2024a. Time travel in          739
                                                                      LLMs: Tracing data contamination in large language      740
689   bank (Zhou et al., 2026). Training used PyTorch                 models. In Proceedings of the 12th International        741
690   2.8.0, Transformers 5.8.1, PEFT 0.19.1, and Bit-                Conference on Learning Representations (ICLR).          742
691   sAndBytes 0.49.2. Both benchmarks are publicly
692   available under permissive licenses (MMLU: MIT;              Shahriar Golchin and Mihai Surdeanu. 2024b. Data           743
                                                                     contamination quiz: A tool to detect and estimate        744
693   ARC-Challenge: CC-BY-SA).                                      contamination in large language models. Transac-         745
                                                                     tions of the Association for Computational Linguis-      746
                                                                     tics (TACL).                                             747
694   References
                                                                   Jongwook Han, Woojung Song, Jonggeun Lee, and              748
695   Sebastian Bordt, Suraj Srinivas, Valentyn Boreiko, and
                                                                     Yohan Jo. 2026. Quantifying data contamination           749
696     Ulrike von Luxburg. 2025. How much can we forget
                                                                     in psychometric evaluations of LLMs. In Findings of      750
697     about data contamination? In Proceedings of the
                                                                     the European Chapter of the Association for Compu-       751
698     42nd International Conference on Machine Learning
                                                                     tational Linguistics (EACL).                             752
699     (ICML).

700   Y. Chang, X. Wang, J. Wang, Y. Wu, L. Yang, K. Zhu,          Larry V. Hedges. 1981. Distribution theory for Glass’s     753
701      H. Chen, X. Yi, C. Wang, Y. Wang, W. Ye, Y. Zhang,          estimator of effect size and related estimators. Jour-   754
702      Y. Chang, P. S. Yu, Q. Yang, and X. Xie. 2024. A            nal of Educational Statistics, 6(2):107–128.             755
703      survey on evaluation of large language models. ACM
704      Transactions on Intelligent Systems and Technology.       D. Hendrycks, C. Burns, S. Basart, A. Zou, M. Mazeika,     756
                                                                      D. Song, and J. Steinhardt. 2021. Measuring massive     757
705   Peter Clark, Isaac Cowhey, Oren Etzioni, Tushar Khot,           multitask language understanding. In Proceedings of     758
706     Ashish Sabharwal, Carissa Schoenick, and Oyvind               the 9th International Conference on Learning Repre-     759
707     Tafjord. 2018. Think you have solved question an-             sentations (ICLR).                                      760
708     swering? try ARC, the AI2 reasoning challenge.
709     arXiv preprint arXiv:1803.05457.                           A. Jacovi, A. Caciularu, O. Goldman, and Y. Goldberg.      761
                                                                     2023. Stop uploading test data in plain text: Prac-      762
710   J. Dekoninck, M. Müller, and M. Vechev. 2024. Con-             tical strategies for mitigating data contamination by    763
711      Stat: Performance-based contamination detection in          evaluation benchmarks. In Proceedings of the 2023        764
712      large language models. In Advances in Neural Infor-         Conference on Empirical Methods in Natural Lan-          765
713      mation Processing Systems (NeurIPS).                        guage Processing (EMNLP).                                766


                                                               9
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6cb93ad6-7096-44a6-89f2-a775409efa19",
  "uuid": "f8d82afc-d4d4-4efc-84b4-a9bb639b895d",
  "tool_use_result": {
    "stdout": "                    10                                                                                Table 3: Detection-diagnosis tradeoff on MMLU: Co-\n                               5% contam.\n                               15% contam.                                                            hen’s |d| across three statistics. Simpler statistics detect\n                               25% contam.\n                                                                 Qwen\n                               50% contam.                                                            more powerfully; ℓ∗z provides unique diagnostic capabil-\n                     8\n                                                                                       ceiling\n                                                                                       reversal\n                                                                                                      ities (§4.3).\n                                                                                      Qwen\n                                                                                      ARC-C\n                     6                                                                                Model        Statistic               |d| (15%)                |d| (50%)\n\n      Cohen's |d|\n                                                                                                      Qwen†        ℓ∗z                5.36 (±1.10)              5.08 (±3.02)\n                         Mistral\n                                                                                                                   HT                 5.83 (±1.30)              5.29 (±3.41)\n                     4                             Llama                                                           Acc. z              45.0 (±2.5)               70.0 (±1.1)\n                                                                                                      Llama        ℓ∗z             2.11 [1.4, 4.8]           2.33 [1.6, 5.1]\n                     2                                                                                             HT              2.45 [1.5, 4.3]           3.07 [1.9, 5.3]\n                                                                     -shift\n                                                                    absorption                                     Acc. z        22.5 [13.6, 47.0]         32.8 [19.8, 68.6]\n                         large effect (0.8)\n                                                                                                      Mistral      ℓ∗z              2.64 [1.5, 7.3]           3.50 [2.1, 9.4]\n                     0                                                                                             HT               4.36 [1.2, 7.0]           5.89 [1.9, 9.4]\n                                 50           60            70              80   90\n                                                     Baseline Accuracy (%)                                         Acc. z          7.81 [4.4, 14.4]          16.6 [9.7, 34.6]\n                                                                                                      †\n                                                                                                       Qwen values are means across n=3 independent seeds (42, 123, 456);\n                                                                                                      per-seed values in Appendix L. Llama and Mistral are single-seed with\n      Figure 3: Baseline accuracy vs. Cohen’s |d| for all                                             bootstrap CIs.\n      model-benchmark combinations (single-seed values;\n      multi-seed means in Table 1). Diamonds: 5%; triangles:\n      15%; squares: 25%; circles: 50%. ARC-C reversal re-                                             findings in the LLM domain; nonparametric alter-                          534\n      flects a ceiling effect.                                                                        natives (Tendeiro and Meijer, 2014) may comple-                           535\n                                                                                                      ment ℓ∗z where 4PL calibration is unavailable.                            536\n                                                                                                         In practice, a two-stage workflow follows:                             537\n503   seed accuracy variance is near-zero in controlled                                               screen using accuracy z-scores (Table 3), then ap-                        538\n504   settings. HT generally exceeds ℓ∗z in detection                                                 ply ℓ∗z to characterize whether the signal reflects                       539\n505   strength, since HT is not attenuated by the Sni-                                                θ-shift absorption (indicating fixed-θ anchoring is                       540\n506   jders correction for θ estimation uncertainty. Both                                             needed) or uniform aberrance (suggesting direct                           541\n507   person-fit statistics exhibit seed-dependent non-                                               memorization).                                                            542\n508   monotonicity under free-θ estimation (Table 3),                                                    Within the IRT family, the 4PL specification mat-                      543\n509   confirming that θ-shift absorption affects all statis-                                          ters: simulation ablations show a mean +27.3pp                            544\n510   tics conditioned on ability, not ℓ∗z specifically.                                              power gain over 3PL on MMLU, because 46% of                               545\n511      Yet the diagnostic power reverses. Full IRT pa-                                              MMLU items have upper asymptote d < 0.95,                                 546\n512   rameterization is unnecessary for mere detection,                                               and the 3PL model (which assumes d=1) misat-                              547\n513   but the value of ℓ∗z lies in three capabilities that                                            tributes slip-related response patterns as aberrance                      548\n514   HT and z-scores lack: (a) seen/unseen decomposi-                                                (Appendix B).                                                             549\n515   tion: ℓ∗z can be computed separately on seen and\n516   unseen item subsets, though item-level detection is                                             4.4    Ability-Dependent Non-Monotonic                                    550\n\n517   near-random (AUROC ≈ 0.53; Appendix F), con-                                                           Dose-Response                                                      551\n\n518   firming that the contamination signal is diffuse and                                            As an exploratory observation, the free-θ dose-                           552\n519   requires model-level aggregation; (b) θ-shift mech-                                             response is non-monotonic for Qwen. The multi-                            553\n520   anism: the ability parameter exposes why detec-                                                 seed mean trajectory (|d|: 4.15 → 5.36 → 7.44 →                           554\n521   tion sensitivity depends on model ability (§4.2), a                                             5.08 at 5%/15%/25%/50%; Appendix L) shows                                 555\n522   mechanistic insight inaccessible to non-parametric                                              signal peaking at 25% before declining at 50%,                            556\n523   statistics; (c) structural sensitivity: on real leader-                                         but the decline is attenuated relative to single-seed                     557\n524   board data, ℓ∗z flags 57/60 model-benchmark cells                                               estimates and the inter-seed variance at 50% is                           558\n525   as aberrant—evidence of systematic IRT assump-                                                  high (CV=60%, range [1.90, 7.91]). This non-                              559\n526   tion violations that motivates the ∆ℓ∗z matched-                                                monotonicity is a θ-estimation artifact: fixed-θ                          560\n527   difference design (§3.2; Appendix E). Accuracy z-                                               analysis eliminates the inverted-U and reveals a                          561\n528   scores flag only 4/60 cells, making them insensitive                                            strong positive dose-response (mean |d|: 5.89 at                          562\n529   to the response-pattern structure that ℓ∗z exploits                                             25% vs. 12.32 at 50%, no seed-level overlap),                             563\n530   for within-model diagnosis. While such patterns                                                 while reducing the 50% CV to 19%. Llama shows                             564\n531   have theoretical antecedents in person-fit literature                                           an approximately flat dose-response (|d|=2.11 →                           565\n532   (St-Onge et al., 2011), the specific magnitude and                                              1.99 → 2.33), consistent with its near-zero ℓ∗z base-                     566\n533   model-dependence we observe are new empirical                                                   line (+0.26 vs. +8.68 for Qwen) despite compa-                            567\n\n\n                                                                                                  7\n\f568   rable θ-shift (∆θ=0.52 vs. 0.47). The mechanism              Scope and calibration. Universal baseline mis-          616\n569   is predictable from simulation (Appendix A): at              fit (57/60 cells flagged) confirms systematic IRT       617\n570   moderate contamination, aberrant responses dom-              violations; the ∆ℓ∗z design turns this into a feature   618\n571   inate; at high contamination, inflated θ̂ absorbs            through within-model differencing. PSN-IRT pro-         619\n572   the anomaly—but the magnitude is highly seed-                vides pre-calibrated 4PL parameters (Zhou et al.,       620\n573   dependent.                                                   2026), but classical calibration fails on contami-      621\n574      A simulated power analysis corroborates these             nated data (ra =0.127; Appendix I); the calibration     622\n575   findings: two-sided testing (flagging both large neg-        sample (13,000+ models) may itself include con-         623\n576   ative and large positive ℓ∗z ) achieves >93% power           taminated ones, though individual contamination         624\n577   on MMLU at all contamination levels, with the the-           effects are diluted across models. The robustness       625\n578   oretical power function yielding R2 =0.957 against           analysis (Appendix G.2) provides partial reassur-       626\n579   simulated values (Appendix A).                               ance (±10% noise tolerance).                            627\n\n\n580   5   Discussion                                               Information requirements and method position-           628\n                                                                   ing. ℓ∗z sits below MIA (logits; Shi et al., 2024)      629\n581   Our findings reveal both the strengths and bound-            and ConStat (multi-benchmark scores; Dekoninck          630\n582   aries of IRT person-fit for contamination detection:         et al., 2024) in an information-requirements hier-      631\n583   ℓ∗z reliably detects SFT-stage contamination across          archy, needing only single-benchmark binary pat-        632\n584   model families, but three boundary conditions con-           terns and an external item bank—suited to retro-        633\n585   strain its practical utility.                                spective audits where logits are unavailable. Our       634\n                                                                   GRPO pilot directly confirms this advantage: Min-       635\n586   Characterization over tool. The detection-                   K% AUC degrades from 0.611 (SFT) to 0.493               636\n587   diagnosis tradeoff (§4.3) shows that simpler statis-         (post-RL), indistinguishable from chance, while         637\n588   tics detect contamination more powerfully than ℓ∗z :         ℓ∗z signal persists (∼3.3; Figure 4; Appendix J),       638\n589   accuracy z-scores yield |d| values several-fold to           demonstrating that response-pattern anomalies sur-      639\n590   over an order of magnitude larger, and HT gener-             vive RL alignment that eliminates memorization-         640\n591   ally exceeds ℓ∗z . The value of the IRT framework            based features (Wang et al., 2025).                     641\n592   lies not in detection power but in mechanistic under-\n593   standing: the θ-shift analysis reveals why detection         6   Conclusion                                          642\n594   sensitivity varies across models and contamination\n595   levels, the seen/unseen decomposition identifies             We characterized IRT person-fit statistics for LLM      643\n596   what fraction of items are memorized, and the 4PL            contamination detection across three 7–8B model         644\n597   parameterization captures item-level ceiling effects         families, establishing reliable SFT-stage detection     645\n598   that 3PL misattributes as aberrance. These diagnos-          while identifying boundary conditions: θ-shift ab-      646\n599   tic capabilities are invisible to accuracy z-scores or       sorption necessitating θ-anchored estimation for        647\n600   HT. Findings 1–2 are theoretically predictable from          high-ability models, a detection-diagnosis trade-       648\n601   IRT principles; our contribution lies in quantifying         off, and non-monotonic dose-response as a θ-            649\n602   these effects in the LLM setting, where the mag-             estimation artifact. For practitioners, we recom-       650\n603   nitude and boundary conditions are not derivable             mend a two-stage workflow: accuracy z-scores            651\n604   from theory alone.                                           for efficient screening, followed by ℓ∗z analy-         652\n                                                                   sis when mechanistic understanding is needed—           653\n605   Practical implications. Two results have imme-               distinguishing which items drive aberrance rather       654\n606   diate consequences. Free-θ estimation produces               than merely flagging contamination. Beyond de-          655\n607   seed-dependent dose-response curves (CV up to                tection, our characterization reveals that person-fit   656\n608   60%); anchoring θ to a pre-contamination base-               statistics capture structural response-pattern anoma-   657\n609   line stabilizes detection and amplifies the signal for       lies that persist even after RL post-training erases    658\n610   models whose clean ℓ∗z departs substantially from            memorization-based signals, suggesting a comple-        659\n611   zero. The benchmark size boundary means ℓ∗z is               mentary role to logit-based methods in the eval-        660\n612   most informative for large benchmarks (n ≈ 8,000             uation integrity toolkit. Future work should ad-        661\n613   items for 80% power at 15% contamination); on                dress pretraining-stage signatures, broader model       662\n614   small benchmarks like ARC-C (295 items), detec-              scales, and cross-benchmark generalization with         663\n615   tion relies on concentrated contamination effects.           larger item banks.                                      664\n\n\n                                                               8\n\f665   Limitations                                                  C. Deng, Y. Zhao, X. Tang, M. Gerstein, and A. Cohan.      714\n                                                                      2024. Investigating data contamination in modern        715\n666   Our controlled experiments cover three 7–8B                     benchmarks for large language models. In Proceed-       716\n667   model families with QLoRA fine-tuning; general-                 ings of the 2024 Conference of the North American       717\n668   ization to larger scales, mixture-of-experts architec-          Chapter of the Association for Computational Lin-       718\n                                                                      guistics (NAACL).                                       719\n669   tures, full-parameter fine-tuning, and pretraining-\n670   stage contamination remains untested. Most con-              J. Dodge, M. Sap, A. Marasović, W. Agnew, G. Ilharco,     720\n671   tamination conditions use a single training run,                D. Groeneveld, M. Mitchell, and M. Gardner. 2021.       721\n672   and multi-seed replication (available for Qwen) re-             Documenting large webtext corpora: A case study on      722\n                                                                      the colossal clean crawled corpus. In Proceedings       723\n673   veals high seed dependence at 50% contamination                 of the 2021 Conference on Empirical Methods in          724\n674   (CV=60%), partially resolved by θ-anchoring; the                Natural Language Processing (EMNLP).                    725\n675   post-RL characterization is N =1. The framework\n676   depends on pre-calibrated 4PL item parameters                F. Drasgow, M. V. Levine, and E. A. Williams. 1985.        726\n677   from PSN-IRT, whose calibration sample may in-                  Appropriateness measurement with polychotomous          727\n                                                                      item response models and standardized indices.          728\n678   clude contaminated models, and we do not provide                British Journal of Mathematical and Statistical Psy-    729\n679   head-to-head comparison with logit-based methods                chology, 38(1):67–86.                                   730\n680   (MIA, ConStat) that operate at a different informa-\n681   tion level.                                                  Susan E. Embretson and Steven P. Reise. 2000. Item Re-     731\n                                                                     sponse Theory for Psychologists. Lawrence Erlbaum        732\n                                                                     Associates, Mahwah, NJ.                                  733\n682   Reproducibility Statement\n683   Code and response data will be released upon ac-             Yujuan Fu, Ozlem Uzuner, Meliha Yetisgen, and Fei          734\n                                                                     Xia. 2025. Does data contamination detection work        735\n684   ceptance. Bootstrap confidence intervals use the               (well) for LLMs? A survey and evaluation on detec-       736\n685   percentile method with 10,000 resamples. All                   tion assumptions. In Findings of the Association for     737\n686   three model families use clean baseline seeds 0–9              Computational Linguistics: NAACL 2025.                   738\n687   (n=10 per family). Pre-calibrated 4PL item param-\n688   eters are from the publicly available PSN-IRT item           S. Golchin and M. Surdeanu. 2024a. Time travel in          739\n                                                                      LLMs: Tracing data contamination in large language      740\n689   bank (Zhou et al., 2026). Training used PyTorch                 models. In Proceedings of the 12th International        741\n690   2.8.0, Transformers 5.8.1, PEFT 0.19.1, and Bit-                Conference on Learning Representations (ICLR).          742\n691   sAndBytes 0.49.2. Both benchmarks are publicly\n692   available under permissive licenses (MMLU: MIT;              Shahriar Golchin and Mihai Surdeanu. 2024b. Data           743\n                                                                     contamination quiz: A tool to detect and estimate        744\n693   ARC-Challenge: CC-BY-SA).                                      contamination in large language models. Transac-         745\n                                                                     tions of the Association for Computational Linguis-      746\n                                                                     tics (TACL).                                             747\n694   References\n                                                                   Jongwook Han, Woojung Song, Jonggeun Lee, and              748\n695   Sebastian Bordt, Suraj Srinivas, Valentyn Boreiko, and\n                                                                     Yohan Jo. 2026. Quantifying data contamination           749\n696     Ulrike von Luxburg. 2025. How much can we forget\n                                                                     in psychometric evaluations of LLMs. In Findings of      750\n697     about data contamination? In Proceedings of the\n                                                                     the European Chapter of the Association for Compu-       751\n698     42nd International Conference on Machine Learning\n                                                                     tational Linguistics (EACL).                             752\n699     (ICML).\n\n700   Y. Chang, X. Wang, J. Wang, Y. Wu, L. Yang, K. Zhu,          Larry V. Hedges. 1981. Distribution theory for Glass’s     753\n701      H. Chen, X. Yi, C. Wang, Y. Wang, W. Ye, Y. Zhang,          estimator of effect size and related estimators. Jour-   754\n702      Y. Chang, P. S. Yu, Q. Yang, and X. Xie. 2024. A            nal of Educational Statistics, 6(2):107–128.             755\n703      survey on evaluation of large language models. ACM\n704      Transactions on Intelligent Systems and Technology.       D. Hendrycks, C. Burns, S. Basart, A. Zou, M. Mazeika,     756\n                                                                      D. Song, and J. Steinhardt. 2021. Measuring massive     757\n705   Peter Clark, Isaac Cowhey, Oren Etzioni, Tushar Khot,           multitask language understanding. In Proceedings of     758\n706     Ashish Sabharwal, Carissa Schoenick, and Oyvind               the 9th International Conference on Learning Repre-     759\n707     Tafjord. 2018. Think you have solved question an-             sentations (ICLR).                                      760\n708     swering? try ARC, the AI2 reasoning challenge.\n709     arXiv preprint arXiv:1803.05457.                           A. Jacovi, A. Caciularu, O. Goldman, and Y. Goldberg.      761\n                                                                     2023. Stop uploading test data in plain text: Prac-      762\n710   J. Dekoninck, M. Müller, and M. Vechev. 2024. Con-             tical strategies for mitigating data contamination by    763\n711      Stat: Performance-based contamination detection in          evaluation benchmarks. In Proceedings of the 2023        764\n712      large language models. In Advances in Neural Infor-         Conference on Empirical Methods in Natural Lan-          765\n713      mation Processing Systems (NeurIPS).                        guage Processing (EMNLP).                                766\n\n\n                                                               9",
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

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_01UrDfeRBd2ZRWULnsGTfMwg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6cb93ad6-7096-44a6-89f2-a775409efa19",
  "uuid": "c905c4de-fc30-49fc-8e93-966689a952b2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011nPBXgPtdaLmX4w6MucE1g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 139,
      "cache_creation_input_tokens": 631,
      "cache_read_input_tokens": 24392,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 631
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

_source line 20 · 2026-05-24T09:09:20.200Z_

<details><summary>↩ Tool result · `toolu_01UrDfeRBd2ZRWULnsGTfMwg`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Detection Signal Across Model Families}
5	\label{sec:detection}
6	
7	Table~\ref{tab:cohens_d} presents Cohen's $d$ effect sizes for $\ell_z^*$ across three model families and two benchmarks.
8	All confidence intervals exclude zero, confirming that $\Delta\ell_z^*$ reliably separates contaminated from clean models at both contamination levels.
9	
10	On MMLU, effect sizes range from $|d|{=}1.99$ (Llama at 25\%) to $|d|{=}7.44$ (Qwen at 25\%), with Qwen at 5\% ($|d|{=}4.15$) confirming detection at the lowest contamination level tested. Llama ($|d|{=}2.11$/$1.99$/$2.33$) and Mistral ($|d|{=}2.64$/$3.50$) show comparable magnitudes.
11	On ARC-C (295 items), Qwen yields $|d|{=}3.16$ at 15\% and $|d|{=}5.30$ at 50\%, demonstrating that detection remains feasible even on small benchmarks when contamination is sufficiently concentrated.
12	
13	Clean-model $\ell_z^*$ baselines diverge substantially across families: Qwen ${+}8.68$ ($\text{SD}{=}0.74$), Mistral ${+}4.02$ ($\text{SD}{=}2.05$), Llama ${+}0.26$ ($\text{SD}{=}1.54$), and ARC-C Qwen ${-}5.42$ ($\text{SD}{=}0.16$); this divergence reflects difficulty-ordering consistency rather than accuracy level (Appendix~\ref{app:baseline_meaning}).
14	Absolute $\ell_z^*$ thresholds would produce contradictory results: Qwen's contaminated $\ell_z^*$ at 15\% (${+}3.8$) is still positive.
15	The $\Delta\ell_z^*$ design normalizes these divergent baselines: Cohen's $d$ yields comparable effect sizes ($|d|{=}1.99$--$7.44$) despite order-of-magnitude differences.
16	Figure~\ref{fig:heatmap} provides a visual summary.
17	
18	\begin{table}[t]
19	\centering
20	\caption{Cohen's $d$ for $\Delta\ell_z^*$ across model families ($n{=}10$ clean seeds). Single-seed conditions: percentile bootstrap 95\% CI (10,000 resamples) reflecting clean-seed variability. Qwen MMLU 15\%/25\%/50\%: multi-seed mean $\pm$ SD ($n{=}3$ independent contamination runs). All 95\% CIs exclude zero.}
21	\label{tab:cohens_d}
22	\footnotesize
23	\resizebox{\columnwidth}{!}{%
24	\begin{tabular}{@{}llrrrr@{}}
25	\toprule
26	Model & Bench. & $d$ (5\%) [CI] & $d$ (15\%) [CI] & $d$ (25\%) [CI] & $d$ (50\%) [CI] \\
27	\midrule
28	Qwen$^{\dagger}$ & MMLU & $-4.15$ [$-9.9$, $-2.7$] & $-5.36$ ($\pm$1.10) & $-7.44$ ($\pm$1.86) & $-5.08$ ($\pm$3.02) \\
29	Llama & MMLU & --- & $-2.11$ [$-4.8$, $-1.4$] & $-1.99$ [$-4.4$, $-1.3$] & $-2.33$ [$-5.1$, $-1.6$] \\
30	Mistral & MMLU & --- & $-2.64$ [$-7.3$, $-1.5$] & --- & $-3.50$ [$-9.4$, $-2.1$] \\
31	Qwen$^{\dagger}$ & ARC-C & --- & $+3.16$ [$2.0$, $9.5$] & --- & $+5.30$ [$3.6$, $15.2$] \\
32	\bottomrule
33	\multicolumn{6}{@{}l}{\scriptsize $^{\dagger}$15\%/25\%/50\%: multi-seed means ($n{=}3$ QLoRA runs); 5\%: single seed. Per-seed values in Appendix~\ref{app:reproducibility}.}
34	\end{tabular}}
35	\end{table}
36	
37	\begin{figure*}[t]
38	  \centering
39	  \includegraphics[width=\textwidth]{fig_heatmap.pdf}
40	  \caption{Cohen's $|d|$ heatmap (single-seed values; multi-seed means in Table~\ref{tab:cohens_d}). Blue intensity reflects effect-size magnitude. Grey cells: conditions not tested. Rows indicate model families; columns indicate contamination levels on MMLU (left) and ARC-C (right).}
41	  \label{fig:heatmap}
42	\end{figure*}
43	
44	\subsection{Model-Specific $\theta$-Shift Dynamics}
45	\label{sec:theta_dynamics}
46	
47	The cross-family variation in Table~\ref{tab:cohens_d}---Qwen's $|d|$ declining from 25\% to 50\% while Llama's remains flat---suggests detection sensitivity depends on more than contamination dose.
48	Contamination raises overall accuracy, which inflates $\hat{\theta}_{\text{MLE}}$; a higher $\hat{\theta}$ ``explains away'' anomalous successes on hard items, absorbing the contamination signal into the ability estimate.
49	We term this \emph{$\theta$-shift absorption}.
50	The magnitude of $\theta$-shift is comparable across families---Qwen ($\Delta\theta{=}0.47$ at 50\%) and Llama ($\Delta\theta{=}0.52$)---yet their fixed-$\theta$ amplification diverges markedly (Table~\ref{tab:theta_fixed}), indicating that $\theta$-shift magnitude alone does not predict fixed-$\theta$ benefit.
51	Figure~\ref{fig:theta_scatter} plots baseline accuracy against Cohen's $|d|$ for all model-benchmark combinations.
52	
53	$\theta$-shift absorption is the dominant source of detection variability for high-ability models at high contamination:
54	(i) fixed-$\theta$ estimation amplifies Qwen's multi-seed $|d|$ by 2.4$\times$ at 50\% ($5.08 \to 12.32$; Table~\ref{tab:theta_fixed}), while Llama shows no amplification ($0.4\times$);
55	(ii) $\theta$-anchoring reduces Qwen's inter-seed CV from 60\% to 19\%, confirming that training-run variance is driven by $\theta$-shift stochasticity rather than true signal variance;
56	(iii) the cross-model ranking under free-$\theta$ is seed-dependent at 50\%, making $\theta$-anchoring a necessary condition for reliable detection of high-ability models at high contamination.
57	
58	ARC-C reverses this pattern.
59	Despite Qwen's high baseline accuracy on ARC-C (89.7\%), contamination produces larger, not smaller, effect sizes ($|d|{=}3.16$ at 15\%, $|d|{=}5.30$ at 50\%).
60	This reversal reflects a ceiling effect: with only 295 items and 89.7\% baseline accuracy, the already-correct items offer minimal room for further $\theta$ inflation, so contamination manifests primarily as anomalous successes on the few remaining hard items.
61	The small item count amplifies this concentration, producing a disproportionately large $\ell_z^*$ shift per contaminated item.
62	
63	The baseline $\ell_z^*$ for ARC-C is negative ($-5.42$), reflecting the 4PL model's expectation of near-perfect performance; contamination pushes $\ell_z^*$ toward zero, producing the positive Cohen's $d$ values in Table~\ref{tab:cohens_d}.
64	
65	These findings indicate that detection sensitivity is not a fixed property of $\ell_z^*$ but depends on the interaction between model ability and benchmark characteristics, a consideration absent from standard person-fit applications.
66	
67	\paragraph{Fixed-$\theta$ estimation.}
68	Table~\ref{tab:theta_fixed} compares free-$\theta$ and fixed-$\theta$ Cohen's $d$ across all three families.
69	The benefit of fixed-$\theta$ is modulated by baseline $\ell_z^*$ level rather than $\theta$-shift magnitude.
70	Qwen (67.8\% accuracy, $\Delta\theta{=}0.47$, baseline $\ell_z^*{=}{+}8.68$) shows 2.4$\times$ amplification at 50\%: its large baseline departure from the IRT null provides substantial signal that free-$\theta$ absorption erodes, which $\theta$-anchoring recovers (multi-seed mean ${\ell_z^*}_{\text{fixed}} {=} 14.5$ vs.\ clean $7.35$).
71	Mistral (52.4\%, baseline $\ell_z^*{=}{+}4.02$) shows 1.7$\times$ at 50\%.
72	Llama (59.4\%, $\Delta\theta{=}0.39$ at 15\%, $0.52$ at 50\%) shows 0.4$\times$ at 50\% despite comparable $\theta$-shift: its near-zero baseline $\ell_z^*$ ($+0.26$) indicates that the clean response pattern conforms to IRT expectations, leaving no absorbed signal for $\theta$-anchoring to recover.
73	The amplification ratio tracks baseline $|\ell_z^*|$ monotonically ($8.68 {\to} 2.4{\times}$; $4.02 {\to} 1.7{\times}$; $0.26 {\to} 0.4{\times}$ at 50\%), making fixed-$\theta$ a targeted remedy for models with substantial baseline misfit, not a universal one.
74	
75	\begin{table}[t]
76	\centering
77	\caption{Free-$\theta$ vs.\ fixed-$\theta$ Cohen's $|d|$ on MMLU (bootstrap 95\% CI). Fixed-$\theta$ anchors $\hat{\theta}$ at the clean-model mean, eliminating $\theta$-shift absorption.}
78	\label{tab:theta_fixed}
79	\footnotesize
80	\resizebox{\columnwidth}{!}{%
81	\begin{tabular}{@{}lcccc@{}}
82	\toprule
83	Model & $|d_{\text{free}}|$ & $|d_{\text{fixed}}|$ & Ratio (fixed/free) & Fixed CI \\
84	\midrule
85	\multicolumn{5}{@{}l}{\textit{5\% contamination}} \\
86	Qwen & 4.15 & 3.52 & 0.8$\times$ & [2.9, 5.7] \\
87	\addlinespace
88	\multicolumn{5}{@{}l}{\textit{15\% contamination}} \\
89	Qwen$^{\S}$ & 5.36 & 6.85 & 1.3$\times$ & ($\pm$1.80) \\
90	Llama & 2.11 & 0.58 & 0.3$\times$ & [0, 2.37]$^{\dagger}$ \\
91	Mistral$^{\ddagger}$ & 2.64 & 2.69 & 1.0$\times$ & [1.53, 9.06] \\
92	\addlinespace
93	\multicolumn{5}{@{}l}{\textit{50\% contamination}} \\
94	Qwen$^{\S}$ & 5.08 & 12.32 & 2.4$\times$ & ($\pm$2.38) \\
95	Llama & 2.33 & 0.84 & 0.4$\times$ & [0.17, 2.97] \\
96	Mistral$^{\ddagger}$ & 3.50 & 5.80 & 1.7$\times$ & [3.87, 18.45] \\
97	\bottomrule
98	\multicolumn{5}{@{}l}{\scriptsize $^{\dagger}$CI includes zero.} \\
99	\multicolumn{5}{@{}l}{\scriptsize $^{\S}$Multi-seed mean ($n{=}3$); CI column shows $\pm$SD of fixed-$\theta$ $|d|$.} \\
100	\multicolumn{5}{@{}l}{\scriptsize $^{\ddagger}$Fixed-$\theta$: 6 seeds (4--7 response vectors not retained in pipeline); free-$\theta$ uses all 10.}
101	\end{tabular}}
102	\end{table}
103	
104	\begin{figure}[t]
105	  \centering
106	  \includegraphics[width=\columnwidth]{fig_theta_scatter.pdf}
107	  \caption{Baseline accuracy vs.\ Cohen's $|d|$ for all model-benchmark combinations (single-seed values; multi-seed means in Table~\ref{tab:cohens_d}). Diamonds: 5\%; triangles: 15\%; squares: 25\%; circles: 50\%. ARC-C reversal reflects a ceiling effect.}
108	  \label{fig:theta_scatter}
109	\end{figure}
110	
111	\subsection{Detection-Diagnosis Tradeoff}
112	\label{sec:degradation}
113	
114	Having established that $\theta$-shift complicates detection, we ask whether the full 4PL framework is necessary, or whether simpler statistics suffice.
115	Table~\ref{tab:degradation} compares three statistics at decreasing levels of information access: $\ell_z^*$ (requires 4PL parameters $a, b, c, d$), the HT statistic (requires only difficulty $b$), and an accuracy $z$-score (requires no item parameters).
116	
117	The comparison reveals a detection-diagnosis tradeoff.
118	For pure detection, simpler statistics are more powerful: accuracy $z$-scores yield $|d|$ values several-fold to over an order of magnitude larger than person-fit statistics (Table~\ref{tab:degradation}), because cross-seed accuracy variance is near-zero in controlled settings.
119	HT generally exceeds $\ell_z^*$ in detection strength, since HT is not attenuated by the Snijders correction for $\theta$ estimation uncertainty.
120	Both person-fit statistics exhibit seed-dependent non-monotonicity under free-$\theta$ estimation (Table~\ref{tab:degradation}), confirming that $\theta$-shift absorption affects all statistics conditioned on ability, not $\ell_z^*$ specifically.
121	
122	Yet the diagnostic power reverses.
123	Full IRT parameterization is unnecessary for mere detection, but the value of $\ell_z^*$ lies in three capabilities that HT and $z$-scores lack:
124	(a) \emph{seen/unseen decomposition}: $\ell_z^*$ can be computed separately on seen and unseen item subsets, though item-level detection is near-random (AUROC $\approx 0.53$; Appendix~\ref{app:item_auroc}), confirming that the contamination signal is diffuse and requires model-level aggregation;
125	(b) \emph{$\theta$-shift mechanism}: the ability parameter exposes why detection sensitivity depends on model ability (\S\ref{sec:theta_dynamics}), a mechanistic insight inaccessible to non-parametric statistics;
126	(c) \emph{structural sensitivity}: on real leaderboard data, $\ell_z^*$ flags 57/60 model-benchmark cells as aberrant---evidence of systematic IRT assumption violations that motivates the $\Delta\ell_z^*$ matched-difference design (\S\ref{sec:did}; Appendix~\ref{app:leaderboard_aberrance}).
127	Accuracy $z$-scores flag only 4/60 cells, making them insensitive to the response-pattern structure that $\ell_z^*$ exploits for within-model diagnosis.
128	While such patterns have theoretical antecedents in person-fit literature \citep{stonge2011}, the specific magnitude and model-dependence we observe are new empirical findings in the LLM domain; nonparametric alternatives \citep{tendeiro2014} may complement $\ell_z^*$ where 4PL calibration is unavailable.
129	
130	In practice, a two-stage workflow follows: screen using accuracy $z$-scores (Table~\ref{tab:degradation}), then apply $\ell_z^*$ to characterize whether the signal reflects $\theta$-shift absorption (indicating fixed-$\theta$ anchoring is needed) or uniform aberrance (suggesting direct memorization).
131	
132	Within the IRT family, the 4PL specification matters: simulation ablations show a mean $+$27.3pp power gain over 3PL on MMLU, because 46\% of MMLU items have upper asymptote $d < 0.95$, and the 3PL model (which assumes $d{=}1$) misattributes slip-related response patterns as aberrance (Appendix~\ref{app:4pl_ablation}).
133	
134	\begin{table}[t]
135	\centering
136	\caption{Detection-diagnosis tradeoff on MMLU: Cohen's $|d|$ across three statistics. Simpler statistics detect more powerfully; $\ell_z^*$ provides unique diagnostic capabilities (\S\ref{sec:degradation}).}
137	\label{tab:degradation}
138	\footnotesize
139	\begin{tabular}{@{}llrr@{}}
140	\toprule
141	Model & Statistic & $|d|$ (15\%) & $|d|$ (50\%) \\
142	\midrule
143	Qwen$^\dagger$ & $\ell_z^*$ & $5.36$ ($\pm$1.10) & $5.08$ ($\pm$3.02) \\
144	     & HT & $5.83$ ($\pm$1.30) & $5.29$ ($\pm$3.41) \\
145	     & Acc.\ $z$ & $45.0$ ($\pm$2.5) & $70.0$ ($\pm$1.1) \\
146	\addlinespace
147	Llama & $\ell_z^*$ & $2.11$ [$1.4$, $4.8$] & $2.33$ [$1.6$, $5.1$] \\
148	      & HT & $2.45$ [$1.5$, $4.3$] & $3.07$ [$1.9$, $5.3$] \\
149	      & Acc.\ $z$ & $22.5$ [$13.6$, $47.0$] & $32.8$ [$19.8$, $68.6$] \\
150	\addlinespace
151	Mistral & $\ell_z^*$ & $2.64$ [$1.5$, $7.3$] & $3.50$ [$2.1$, $9.4$] \\
152	      & HT & $4.36$ [$1.2$, $7.0$] & $5.89$ [$1.9$, $9.4$] \\
153	      & Acc.\ $z$ & $7.81$ [$4.4$, $14.4$] & $16.6$ [$9.7$, $34.6$] \\
154	\bottomrule
155	\multicolumn{4}{@{}p{0.9\columnwidth}}{\scriptsize $^\dagger$Qwen values are means across $n{=}3$ independent seeds (42, 123, 456); per-seed values in Appendix~\ref{app:reproducibility}. Llama and Mistral are single-seed with bootstrap CIs.}
156	\end{tabular}
157	\end{table}
158	
159	\subsection{Ability-Dependent Non-Monotonic Dose-Response}
160	\label{sec:inverted_u}
161	
162	As an exploratory observation, the free-$\theta$ dose-response is non-monotonic for Qwen.
163	The multi-seed mean trajectory ($|d|$: $4.15 \to 5.36 \to 7.44 \to 5.08$ at 5\%/15\%/25\%/50\%; Appendix~\ref{app:reproducibility}) shows signal peaking at 25\% before declining at 50\%, but the decline is attenuated relative to single-seed estimates and the inter-seed variance at 50\% is high (CV${=}$60\%, range $[1.90, 7.91]$).
164	This non-monotonicity is a $\theta$-estimation artifact: fixed-$\theta$ analysis eliminates the inverted-U and reveals a strong positive dose-response (mean $|d|$: $5.89$ at 25\% vs.\ $12.32$ at 50\%, no seed-level overlap), while reducing the 50\% CV to 19\%.
165	Llama shows an approximately flat dose-response ($|d|{=}2.11 \to 1.99 \to 2.33$), consistent with its near-zero $\ell_z^*$ baseline ($+0.26$ vs.\ ${+}8.68$ for Qwen) despite comparable $\theta$-shift ($\Delta\theta{=}0.52$ vs.\ $0.47$).
166	The mechanism is predictable from simulation (Appendix~\ref{app:simulation}): at moderate contamination, aberrant responses dominate; at high contamination, inflated $\hat{\theta}$ absorbs the anomaly---but the magnitude is highly seed-dependent.
167	
168	A simulated power analysis corroborates these findings: two-sided testing (flagging both large negative and large positive $\ell_z^*$) achieves ${>}$93\% power on MMLU at all contamination levels, with the theoretical power function yielding $R^2 {=} 0.957$ against simulated values (Appendix~\ref{app:simulation}).
169	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6cb93ad6-7096-44a6-89f2-a775409efa19",
  "uuid": "e7ae939f-8733-4644-8138-c441f2429048",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/results.tex",
      "content": "\\section{Results}\n\\label{sec:results}\n\n\\subsection{Detection Signal Across Model Families}\n\\label{sec:detection}\n\nTable~\\ref{tab:cohens_d} presents Cohen's $d$ effect sizes for $\\ell_z^*$ across three model families and two benchmarks.\nAll confidence intervals exclude zero, confirming that $\\Delta\\ell_z^*$ reliably separates contaminated from clean models at both contamination levels.\n\nOn MMLU, effect sizes range from $|d|{=}1.99$ (Llama at 25\\%) to $|d|{=}7.44$ (Qwen at 25\\%), with Qwen at 5\\% ($|d|{=}4.15$) confirming detection at the lowest contamination level tested. Llama ($|d|{=}2.11$/$1.99$/$2.33$) and Mistral ($|d|{=}2.64$/$3.50$) show comparable magnitudes.\nOn ARC-C (295 items), Qwen yields $|d|{=}3.16$ at 15\\% and $|d|{=}5.30$ at 50\\%, demonstrating that detection remains feasible even on small benchmarks when contamination is sufficiently concentrated.\n\nClean-model $\\ell_z^*$ baselines diverge substantially across families: Qwen ${+}8.68$ ($\\text{SD}{=}0.74$), Mistral ${+}4.02$ ($\\text{SD}{=}2.05$), Llama ${+}0.26$ ($\\text{SD}{=}1.54$), and ARC-C Qwen ${-}5.42$ ($\\text{SD}{=}0.16$); this divergence reflects difficulty-ordering consistency rather than accuracy level (Appendix~\\ref{app:baseline_meaning}).\nAbsolute $\\ell_z^*$ thresholds would produce contradictory results: Qwen's contaminated $\\ell_z^*$ at 15\\% (${+}3.8$) is still positive.\nThe $\\Delta\\ell_z^*$ design normalizes these divergent baselines: Cohen's $d$ yields comparable effect sizes ($|d|{=}1.99$--$7.44$) despite order-of-magnitude differences.\nFigure~\\ref{fig:heatmap} provides a visual summary.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cohen's $d$ for $\\Delta\\ell_z^*$ across model families ($n{=}10$ clean seeds). Single-seed conditions: percentile bootstrap 95\\% CI (10,000 resamples) reflecting clean-seed variability. Qwen MMLU 15\\%/25\\%/50\\%: multi-seed mean $\\pm$ SD ($n{=}3$ independent contamination runs). All 95\\% CIs exclude zero.}\n\\label{tab:cohens_d}\n\\footnotesize\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llrrrr@{}}\n\\toprule\nModel & Bench. & $d$ (5\\%) [CI] & $d$ (15\\%) [CI] & $d$ (25\\%) [CI] & $d$ (50\\%) [CI] \\\\\n\\midrule\nQwen$^{\\dagger}$ & MMLU & $-4.15$ [$-9.9$, $-2.7$] & $-5.36$ ($\\pm$1.10) & $-7.44$ ($\\pm$1.86) & $-5.08$ ($\\pm$3.02) \\\\\nLlama & MMLU & --- & $-2.11$ [$-4.8$, $-1.4$] & $-1.99$ [$-4.4$, $-1.3$] & $-2.33$ [$-5.1$, $-1.6$] \\\\\nMistral & MMLU & --- & $-2.64$ [$-7.3$, $-1.5$] & --- & $-3.50$ [$-9.4$, $-2.1$] \\\\\nQwen$^{\\dagger}$ & ARC-C & --- & $+3.16$ [$2.0$, $9.5$] & --- & $+5.30$ [$3.6$, $15.2$] \\\\\n\\bottomrule\n\\multicolumn{6}{@{}l}{\\scriptsize $^{\\dagger}$15\\%/25\\%/50\\%: multi-seed means ($n{=}3$ QLoRA runs); 5\\%: single seed. Per-seed values in Appendix~\\ref{app:reproducibility}.}\n\\end{tabular}}\n\\end{table}\n\n\\begin{figure*}[t]\n  \\centering\n  \\includegraphics[width=\\textwidth]{fig_heatmap.pdf}\n  \\caption{Cohen's $|d|$ heatmap (single-seed values; multi-seed means in Table~\\ref{tab:cohens_d}). Blue intensity reflects effect-size magnitude. Grey cells: conditions not tested. Rows indicate model families; columns indicate contamination levels on MMLU (left) and ARC-C (right).}\n  \\label{fig:heatmap}\n\\end{figure*}\n\n\\subsection{Model-Specific $\\theta$-Shift Dynamics}\n\\label{sec:theta_dynamics}\n\nThe cross-family variation in Table~\\ref{tab:cohens_d}---Qwen's $|d|$ declining from 25\\% to 50\\% while Llama's remains flat---suggests detection sensitivity depends on more than contamination dose.\nContamination raises overall accuracy, which inflates $\\hat{\\theta}_{\\text{MLE}}$; a higher $\\hat{\\theta}$ ``explains away'' anomalous successes on hard items, absorbing the contamination signal into the ability estimate.\nWe term this \\emph{$\\theta$-shift absorption}.\nThe magnitude of $\\theta$-shift is comparable across families---Qwen ($\\Delta\\theta{=}0.47$ at 50\\%) and Llama ($\\Delta\\theta{=}0.52$)---yet their fixed-$\\theta$ amplification diverges markedly (Table~\\ref{tab:theta_fixed}), indicating that $\\theta$-shift magnitude alone does not predict fixed-$\\theta$ benefit.\nFigure~\\ref{fig:theta_scatter} plots baseline accuracy against Cohen's $|d|$ for all model-benchmark combinations.\n\n$\\theta$-shift absorption is the dominant source of detection variability for high-ability models at high contamination:\n(i) fixed-$\\theta$ estimation amplifies Qwen's multi-seed $|d|$ by 2.4$\\times$ at 50\\% ($5.08 \\to 12.32$; Table~\\ref{tab:theta_fixed}), while Llama shows no amplification ($0.4\\times$);\n(ii) $\\theta$-anchoring reduces Qwen's inter-seed CV from 60\\% to 19\\%, confirming that training-run variance is driven by $\\theta$-shift stochasticity rather than true signal variance;\n(iii) the cross-model ranking under free-$\\theta$ is seed-dependent at 50\\%, making $\\theta$-anchoring a necessary condition for reliable detection of high-ability models at high contamination.\n\nARC-C reverses this pattern.\nDespite Qwen's high baseline accuracy on ARC-C (89.7\\%), contamination produces larger, not smaller, effect sizes ($|d|{=}3.16$ at 15\\%, $|d|{=}5.30$ at 50\\%).\nThis reversal reflects a ceiling effect: with only 295 items and 89.7\\% baseline accuracy, the already-correct items offer minimal room for further $\\theta$ inflation, so contamination manifests primarily as anomalous successes on the few remaining hard items.\nThe small item count amplifies this concentration, producing a disproportionately large $\\ell_z^*$ shift per contaminated item.\n\nThe baseline $\\ell_z^*$ for ARC-C is negative ($-5.42$), reflecting the 4PL model's expectation of near-perfect performance; contamination pushes $\\ell_z^*$ toward zero, producing the positive Cohen's $d$ values in Table~\\ref{tab:cohens_d}.\n\nThese findings indicate that detection sensitivity is not a fixed property of $\\ell_z^*$ but depends on the interaction between model ability and benchmark characteristics, a consideration absent from standard person-fit applications.\n\n\\paragraph{Fixed-$\\theta$ estimation.}\nTable~\\ref{tab:theta_fixed} compares free-$\\theta$ and fixed-$\\theta$ Cohen's $d$ across all three families.\nThe benefit of fixed-$\\theta$ is modulated by baseline $\\ell_z^*$ level rather than $\\theta$-shift magnitude.\nQwen (67.8\\% accuracy, $\\Delta\\theta{=}0.47$, baseline $\\ell_z^*{=}{+}8.68$) shows 2.4$\\times$ amplification at 50\\%: its large baseline departure from the IRT null provides substantial signal that free-$\\theta$ absorption erodes, which $\\theta$-anchoring recovers (multi-seed mean ${\\ell_z^*}_{\\text{fixed}} {=} 14.5$ vs.\\ clean $7.35$).\nMistral (52.4\\%, baseline $\\ell_z^*{=}{+}4.02$) shows 1.7$\\times$ at 50\\%.\nLlama (59.4\\%, $\\Delta\\theta{=}0.39$ at 15\\%, $0.52$ at 50\\%) shows 0.4$\\times$ at 50\\% despite comparable $\\theta$-shift: its near-zero baseline $\\ell_z^*$ ($+0.26$) indicates that the clean response pattern conforms to IRT expectations, leaving no absorbed signal for $\\theta$-anchoring to recover.\nThe amplification ratio tracks baseline $|\\ell_z^*|$ monotonically ($8.68 {\\to} 2.4{\\times}$; $4.02 {\\to} 1.7{\\times}$; $0.26 {\\to} 0.4{\\times}$ at 50\\%), making fixed-$\\theta$ a targeted remedy for models with substantial baseline misfit, not a universal one.\n\n\\begin{table}[t]\n\\centering\n\\caption{Free-$\\theta$ vs.\\ fixed-$\\theta$ Cohen's $|d|$ on MMLU (bootstrap 95\\% CI). Fixed-$\\theta$ anchors $\\hat{\\theta}$ at the clean-model mean, eliminating $\\theta$-shift absorption.}\n\\label{tab:theta_fixed}\n\\footnotesize\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nModel & $|d_{\\text{free}}|$ & $|d_{\\text{fixed}}|$ & Ratio (fixed/free) & Fixed CI \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{5\\% contamination}} \\\\\nQwen & 4.15 & 3.52 & 0.8$\\times$ & [2.9, 5.7] \\\\\n\\addlinespace\n\\multicolumn{5}{@{}l}{\\textit{15\\% contamination}} \\\\\nQwen$^{\\S}$ & 5.36 & 6.85 & 1.3$\\times$ & ($\\pm$1.80) \\\\\nLlama & 2.11 & 0.58 & 0.3$\\times$ & [0, 2.37]$^{\\dagger}$ \\\\\nMistral$^{\\ddagger}$ & 2.64 & 2.69 & 1.0$\\times$ & [1.53, 9.06] \\\\\n\\addlinespace\n\\multicolumn{5}{@{}l}{\\textit{50\\% contamination}} \\\\\nQwen$^{\\S}$ & 5.08 & 12.32 & 2.4$\\times$ & ($\\pm$2.38) \\\\\nLlama & 2.33 & 0.84 & 0.4$\\times$ & [0.17, 2.97] \\\\\nMistral$^{\\ddagger}$ & 3.50 & 5.80 & 1.7$\\times$ & [3.87, 18.45] \\\\\n\\bottomrule\n\\multicolumn{5}{@{}l}{\\scriptsize $^{\\dagger}$CI includes zero.} \\\\\n\\multicolumn{5}{@{}l}{\\scriptsize $^{\\S}$Multi-seed mean ($n{=}3$); CI column shows $\\pm$SD of fixed-$\\theta$ $|d|$.} \\\\\n\\multicolumn{5}{@{}l}{\\scriptsize $^{\\ddagger}$Fixed-$\\theta$: 6 seeds (4--7 response vectors not retained in pipeline); free-$\\theta$ uses all 10.}\n\\end{tabular}}\n\\end{table}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_theta_scatter.pdf}\n  \\caption{Baseline accuracy vs.\\ Cohen's $|d|$ for all model-benchmark combinations (single-seed values; multi-seed means in Table~\\ref{tab:cohens_d}). Diamonds: 5\\%; triangles: 15\\%; squares: 25\\%; circles: 50\\%. ARC-C reversal reflects a ceiling effect.}\n  \\label{fig:theta_scatter}\n\\end{figure}\n\n\\subsection{Detection-Diagnosis Tradeoff}\n\\label{sec:degradation}\n\nHaving established that $\\theta$-shift complicates detection, we ask whether the full 4PL framework is necessary, or whether simpler statistics suffice.\nTable~\\ref{tab:degradation} compares three statistics at decreasing levels of information access: $\\ell_z^*$ (requires 4PL parameters $a, b, c, d$), the HT statistic (requires only difficulty $b$), and an accuracy $z$-score (requires no item parameters).\n\nThe comparison reveals a detection-diagnosis tradeoff.\nFor pure detection, simpler statistics are more powerful: accuracy $z$-scores yield $|d|$ values several-fold to over an order of magnitude larger than person-fit statistics (Table~\\ref{tab:degradation}), because cross-seed accuracy variance is near-zero in controlled settings.\nHT generally exceeds $\\ell_z^*$ in detection strength, since HT is not attenuated by the Snijders correction for $\\theta$ estimation uncertainty.\nBoth person-fit statistics exhibit seed-dependent non-monotonicity under free-$\\theta$ estimation (Table~\\ref{tab:degradation}), confirming that $\\theta$-shift absorption affects all statistics conditioned on ability, not $\\ell_z^*$ specifically.\n\nYet the diagnostic power reverses.\nFull IRT parameterization is unnecessary for mere detection, but the value of $\\ell_z^*$ lies in three capabilities that HT and $z$-scores lack:\n(a) \\emph{seen/unseen decomposition}: $\\ell_z^*$ can be computed separately on seen and unseen item subsets, though item-level detection is near-random (AUROC $\\approx 0.53$; Appendix~\\ref{app:item_auroc}), confirming that the contamination signal is diffuse and requires model-level aggregation;\n(b) \\emph{$\\theta$-shift mechanism}: the ability parameter exposes why detection sensitivity depends on model ability (\\S\\ref{sec:theta_dynamics}), a mechanistic insight inaccessible to non-parametric statistics;\n(c) \\emph{structural sensitivity}: on real leaderboard data, $\\ell_z^*$ flags 57/60 model-benchmark cells as aberrant---evidence of systematic IRT assumption violations that motivates the $\\Delta\\ell_z^*$ matched-difference design (\\S\\ref{sec:did}; Appendix~\\ref{app:leaderboard_aberrance}).\nAccuracy $z$-scores flag only 4/60 cells, making them insensitive to the response-pattern structure that $\\ell_z^*$ exploits for within-model diagnosis.\nWhile such patterns have theoretical antecedents in person-fit literature \\citep{stonge2011}, the specific magnitude and model-dependence we observe are new empirical findings in the LLM domain; nonparametric alternatives \\citep{tendeiro2014} may complement $\\ell_z^*$ where 4PL calibration is unavailable.\n\nIn practice, a two-stage workflow follows: screen using accuracy $z$-scores (Table~\\ref{tab:degradation}), then apply $\\ell_z^*$ to characterize whether the signal reflects $\\theta$-shift absorption (indicating fixed-$\\theta$ anchoring is needed) or uniform aberrance (suggesting direct memorization).\n\nWithin the IRT family, the 4PL specification matters: simulation ablations show a mean $+$27.3pp power gain over 3PL on MMLU, because 46\\% of MMLU items have upper asymptote $d < 0.95$, and the 3PL model (which assumes $d{=}1$) misattributes slip-related response patterns as aberrance (Appendix~\\ref{app:4pl_ablation}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Detection-diagnosis tradeoff on MMLU: Cohen's $|d|$ across three statistics. Simpler statistics detect more powerfully; $\\ell_z^*$ provides unique diagnostic capabilities (\\S\\ref{sec:degradation}).}\n\\label{tab:degradation}\n\\footnotesize\n\\begin{tabular}{@{}llrr@{}}\n\\toprule\nModel & Statistic & $|d|$ (15\\%) & $|d|$ (50\\%) \\\\\n\\midrule\nQwen$^\\dagger$ & $\\ell_z^*$ & $5.36$ ($\\pm$1.10) & $5.08$ ($\\pm$3.02) \\\\\n     & HT & $5.83$ ($\\pm$1.30) & $5.29$ ($\\pm$3.41) \\\\\n     & Acc.\\ $z$ & $45.0$ ($\\pm$2.5) & $70.0$ ($\\pm$1.1) \\\\\n\\addlinespace\nLlama & $\\ell_z^*$ & $2.11$ [$1.4$, $4.8$] & $2.33$ [$1.6$, $5.1$] \\\\\n      & HT & $2.45$ [$1.5$, $4.3$] & $3.07$ [$1.9$, $5.3$] \\\\\n      & Acc.\\ $z$ & $22.5$ [$13.6$, $47.0$] & $32.8$ [$19.8$, $68.6$] \\\\\n\\addlinespace\nMistral & $\\ell_z^*$ & $2.64$ [$1.5$, $7.3$] & $3.50$ [$2.1$, $9.4$] \\\\\n      & HT & $4.36$ [$1.2$, $7.0$] & $5.89$ [$1.9$, $9.4$] \\\\\n      & Acc.\\ $z$ & $7.81$ [$4.4$, $14.4$] & $16.6$ [$9.7$, $34.6$] \\\\\n\\bottomrule\n\\multicolumn{4}{@{}p{0.9\\columnwidth}}{\\scriptsize $^\\dagger$Qwen values are means across $n{=}3$ independent seeds (42, 123, 456); per-seed values in Appendix~\\ref{app:reproducibility}. Llama and Mistral are single-seed with bootstrap CIs.}\n\\end{tabular}\n\\end{table}\n\n\\subsection{Ability-Dependent Non-Monotonic Dose-Response}\n\\label{sec:inverted_u}\n\nAs an exploratory observation, the free-$\\theta$ dose-response is non-monotonic for Qwen.\nThe multi-seed mean trajectory ($|d|$: $4.15 \\to 5.36 \\to 7.44 \\to 5.08$ at 5\\%/15\\%/25\\%/50\\%; Appendix~\\ref{app:reproducibility}) shows signal peaking at 25\\% before declining at 50\\%, but the decline is attenuated relative to single-seed estimates and the inter-seed variance at 50\\% is high (CV${=}$60\\%, range $[1.90, 7.91]$).\nThis non-monotonicity is a $\\theta$-estimation artifact: fixed-$\\theta$ analysis eliminates the inverted-U and reveals a strong positive dose-response (mean $|d|$: $5.89$ at 25\\% vs.\\ $12.32$ at 50\\%, no seed-level overlap), while reducing the 50\\% CV to 19\\%.\nLlama shows an approximately flat dose-response ($|d|{=}2.11 \\to 1.99 \\to 2.33$), consistent with its near-zero $\\ell_z^*$ baseline ($+0.26$ vs.\\ ${+}8.68$ for Qwen) despite comparable $\\theta$-shift ($\\Delta\\theta{=}0.52$ vs.\\ $0.47$).\nThe mechanism is predictable from simulation (Appendix~\\ref{app:simulation}): at moderate contamination, aberrant responses dominate; at high contamination, inflated $\\hat{\\theta}$ absorbs the anomaly---but the magnitude is highly seed-dependent.\n\nA simulated power analysis corroborates these findings: two-sided testing (flagging both large negative and large positive $\\ell_z^*$) achieves ${>}$93\\% power on MMLU at all contamination levels, with the theoretical power function yielding $R^2 {=} 0.957$ against simulated values (Appendix~\\ref{app:simulation}).\n",
      "numLines": 169,
      "startLine": 1,
      "totalLines": 169
    }
  }
}
```

</details>

---

### Assistant

_source line 21_

<details><summary>Logged reasoning block</summary>

```text
Now I can see the paper layout. The main text ends at page 8, with Limitations starting on page 8 and References starting on page 9. Let me look more carefully at what's on page 8. From the pdftotext output, page 8 ends after the Conclusion section (line 664 in the PDF). The Limitations section starts on page 8 too (line 665), and the Reproducibility Statement is also on page 8.

Wait, let me re-read the output more carefully. Looking at the page numbers:
- Page 7 ends after line 573 roughly


- Page 8 contains the rest of the dose-response section, the Discussion, Conclusion, Limitations, and Reproducibility Statement (lines 574-693)
- Page 9 starts with References

So the main text already fills 8 pages, but the user mentioned it's about 4 lines short. Let me check where the blank space is at the bottom of page 8. Looking at the pdftotext output, page 8 ends after line 693 with the Reproducibility Statement, and then References begins on page 9.

There's roughly 4 lines of blank space at the bottom of page 8 before the References section starts. Now I need to look at the discussion, conclusion, and limitations files to find the best place to add content that would naturally fill that gap.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6cb93ad6-7096-44a6-89f2-a775409efa19",
  "uuid": "9380e45a-c003-4257-9f08-19db67795598",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UyQ5XuqVmiLJyhdwf3zpF8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13250,
      "cache_read_input_tokens": 25023,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13250
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

_source line 22_

Main text is already 8 pages with some blank space at the bottom. Let me read the discussion and limitations files to find the best expansion point.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6cb93ad6-7096-44a6-89f2-a775409efa19",
  "uuid": "e25082ce-70f6-4974-8b13-46dfe180424b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UyQ5XuqVmiLJyhdwf3zpF8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13250,
      "cache_read_input_tokens": 25023,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13250
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

_source line 23_

<details open><summary>🔧 Tool call — Read · `toolu_01CLbNGv1i1ye9mBJd5ySCyC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6cb93ad6-7096-44a6-89f2-a775409efa19",
  "uuid": "ec15bfc0-4042-4adc-bd2e-3f6bff20c3f8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UyQ5XuqVmiLJyhdwf3zpF8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13250,
      "cache_read_input_tokens": 25023,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13250
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

_source line 24 · 2026-05-24T09:09:34.158Z_

<details><summary>↩ Tool result · `toolu_01CLbNGv1i1ye9mBJd5ySCyC`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	Our findings reveal both the strengths and boundaries of IRT person-fit for contamination detection: $\ell_z^*$ reliably detects SFT-stage contamination across model families, but three boundary conditions constrain its practical utility.
4	
5	\paragraph{Characterization over tool.}
6	The detection-diagnosis tradeoff (\S\ref{sec:degradation}) shows that simpler statistics detect contamination more powerfully than $\ell_z^*$: accuracy $z$-scores yield $|d|$ values several-fold to over an order of magnitude larger, and HT generally exceeds $\ell_z^*$.
7	The value of the IRT framework lies not in detection power but in mechanistic understanding: the $\theta$-shift analysis reveals \emph{why} detection sensitivity varies across models and contamination levels, the seen/unseen decomposition identifies \emph{what fraction} of items are memorized, and the 4PL parameterization captures item-level ceiling effects that 3PL misattributes as aberrance.
8	These diagnostic capabilities are invisible to accuracy $z$-scores or HT.
9	Findings~1--2 are theoretically predictable from IRT principles; our contribution lies in quantifying these effects in the LLM setting, where the magnitude and boundary conditions are not derivable from theory alone.
10	
11	\paragraph{Practical implications.}
12	Two results have immediate consequences.
13	Free-$\theta$ estimation produces seed-dependent dose-response curves (CV up to 60\%); anchoring $\theta$ to a pre-contamination baseline stabilizes detection and amplifies the signal for models whose clean $\ell_z^*$ departs substantially from zero.
14	The benchmark size boundary means $\ell_z^*$ is most informative for large benchmarks ($n \approx 8{,}000$ items for 80\% power at 15\% contamination); on small benchmarks like ARC-C (295 items), detection relies on concentrated contamination effects.
15	
16	\paragraph{Scope and calibration.}
17	Universal baseline misfit (57/60 cells flagged) confirms systematic IRT violations; the $\Delta\ell_z^*$ design turns this into a feature through within-model differencing.
18	PSN-IRT provides pre-calibrated 4PL parameters \citep{psnirt2026}, but classical calibration fails on contaminated data ($r_a{=}0.127$; Appendix~\ref{app:mml_em}); the calibration sample (13,000+ models) may itself include contaminated ones, though individual contamination effects are diluted across models.
19	The robustness analysis (Appendix~\ref{app:param_perturb}) provides partial reassurance (${\pm}10\%$ noise tolerance).
20	\paragraph{Information requirements and method positioning.}
21	$\ell_z^*$ sits below MIA \citep[logits;][]{minkprob2024} and ConStat \citep[multi-benchmark scores;][]{constat2024} in an information-requirements hierarchy, needing only single-benchmark binary patterns and an external item bank---suited to retrospective audits where logits are unavailable. Our GRPO pilot directly confirms this advantage: Min-K\% AUC degrades from $0.611$ (SFT) to $0.493$ (post-RL), indistinguishable from chance, while $\ell_z^*$ signal persists (${\sim}3.3$; Figure~\ref{fig:grpo}; Appendix~\ref{app:post_rl}), demonstrating that response-pattern anomalies survive RL alignment that eliminates memorization-based features \citep{wang2025fragility}.
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6cb93ad6-7096-44a6-89f2-a775409efa19",
  "uuid": "63f24e3c-a680-4ba3-8151-2475f5b82fdc",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/discussion.tex",
      "content": "\\section{Discussion}\\label{sec:discussion}\n\nOur findings reveal both the strengths and boundaries of IRT person-fit for contamination detection: $\\ell_z^*$ reliably detects SFT-stage contamination across model families, but three boundary conditions constrain its practical utility.\n\n\\paragraph{Characterization over tool.}\nThe detection-diagnosis tradeoff (\\S\\ref{sec:degradation}) shows that simpler statistics detect contamination more powerfully than $\\ell_z^*$: accuracy $z$-scores yield $|d|$ values several-fold to over an order of magnitude larger, and HT generally exceeds $\\ell_z^*$.\nThe value of the IRT framework lies not in detection power but in mechanistic understanding: the $\\theta$-shift analysis reveals \\emph{why} detection sensitivity varies across models and contamination levels, the seen/unseen decomposition identifies \\emph{what fraction} of items are memorized, and the 4PL parameterization captures item-level ceiling effects that 3PL misattributes as aberrance.\nThese diagnostic capabilities are invisible to accuracy $z$-scores or HT.\nFindings~1--2 are theoretically predictable from IRT principles; our contribution lies in quantifying these effects in the LLM setting, where the magnitude and boundary conditions are not derivable from theory alone.\n\n\\paragraph{Practical implications.}\nTwo results have immediate consequences.\nFree-$\\theta$ estimation produces seed-dependent dose-response curves (CV up to 60\\%); anchoring $\\theta$ to a pre-contamination baseline stabilizes detection and amplifies the signal for models whose clean $\\ell_z^*$ departs substantially from zero.\nThe benchmark size boundary means $\\ell_z^*$ is most informative for large benchmarks ($n \\approx 8{,}000$ items for 80\\% power at 15\\% contamination); on small benchmarks like ARC-C (295 items), detection relies on concentrated contamination effects.\n\n\\paragraph{Scope and calibration.}\nUniversal baseline misfit (57/60 cells flagged) confirms systematic IRT violations; the $\\Delta\\ell_z^*$ design turns this into a feature through within-model differencing.\nPSN-IRT provides pre-calibrated 4PL parameters \\citep{psnirt2026}, but classical calibration fails on contaminated data ($r_a{=}0.127$; Appendix~\\ref{app:mml_em}); the calibration sample (13,000+ models) may itself include contaminated ones, though individual contamination effects are diluted across models.\nThe robustness analysis (Appendix~\\ref{app:param_perturb}) provides partial reassurance (${\\pm}10\\%$ noise tolerance).\n\\paragraph{Information requirements and method positioning.}\n$\\ell_z^*$ sits below MIA \\citep[logits;][]{minkprob2024} and ConStat \\citep[multi-benchmark scores;][]{constat2024} in an information-requirements hierarchy, needing only single-benchmark binary patterns and an external item bank---suited to retrospective audits where logits are unavailable. Our GRPO pilot directly confirms this advantage: Min-K\\% AUC degrades from $0.611$ (SFT) to $0.493$ (post-RL), indistinguishable from chance, while $\\ell_z^*$ signal persists (${\\sim}3.3$; Figure~\\ref{fig:grpo}; Appendix~\\ref{app:post_rl}), demonstrating that response-pattern anomalies survive RL alignment that eliminates memorization-based features \\citep{wang2025fragility}.\n",
      "numLines": 22,
      "startLine": 1,
      "totalLines": 22
    }
  }
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Read · `toolu_01HmWLZokadwHudsUJcKxwog`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6cb93ad6-7096-44a6-89f2-a775409efa19",
  "uuid": "9e79ea7b-d6bc-4c19-93fc-bc6c6b65e28d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UyQ5XuqVmiLJyhdwf3zpF8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13250,
      "cache_read_input_tokens": 25023,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13250
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
