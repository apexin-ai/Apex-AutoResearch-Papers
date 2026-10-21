# paper introduction fix v2

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 30
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/workers/worker_paper_introduction-fix-v2_20260515T143951.log`
- **Structured JSON:** [`5725b83f48760e6e12bc.json`](../../sessions/57/5725b83f48760e6e12bc.json)

## Before a recorded user message

30 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "session_id": "066b9dae-ab21-4272-be08-6477f0f4d275",
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
  "uuid": "8213fdd6-d046-4e02-9a36-d6be340c2d03",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/memory/"
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
    "resetsAt": 1778873400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "2bb07195-6014-4faf-9d16-2ee3cd767f38",
  "session_id": "066b9dae-ab21-4272-be08-6477f0f4d275"
}
```

---

### Assistant

_source line 4_

Let me start by reading the current introduction.tex file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "066b9dae-ab21-4272-be08-6477f0f4d275",
  "uuid": "3cbd776d-a239-4660-9a17-6df7f74de26a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LxkTMybz9NR5WjMANFu2ez",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11726,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11726
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

<details open><summary>🔧 Tool call — Read · `toolu_01GvtMEnczbUoCGBjnXN68qm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "066b9dae-ab21-4272-be08-6477f0f4d275",
  "uuid": "dc864d9d-bfec-401f-8ab3-e1db27aeb33c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LxkTMybz9NR5WjMANFu2ez",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11726,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11726
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

### Tool result

_source line 6 · 2026-05-15T14:40:03.797Z_

<details><summary>↩ Tool result · `toolu_01GvtMEnczbUoCGBjnXN68qm`</summary>

```text
1	% Introduction draft — generated 2026-05-15, numbers from registry
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Test-time compute scaling has emerged as a powerful paradigm for improving LLM-based code repair: rather than relying on a single generation, systems produce many candidate patches and select the best one through verification~\citep{snell2024scaling}. The bottleneck in this pipeline is the verifier. Full execution---running each candidate against the test suite in a sandboxed environment---is reliable but expensive, costing \$1--3 and several minutes per candidate on repository-level benchmarks~\citep{jimenez2024swebench}. Execution-free verification eliminates this cost, but existing approaches face a fundamental tradeoff between accuracy and diagnostic granularity.
7	
8	On one end, trajectory-level reward models such as SWE-RM~\citep{zhang2025swerm} score candidate patches as a whole, achieving strong binary accept/reject accuracy but discarding information about \emph{which} tests a patch fails. This coarse signal limits downstream applications: when a candidate is rejected, the repair system has no guidance for targeted re-repair. On the other end, Code World Models (CWM)~\citep{meta2025cwm,ding2025selfexecution} predict execution outputs per test, preserving diagnostic granularity---but formulate the task as open-ended generation, requiring the model to reproduce exact output strings token by token.
9	
10	This generation formulation creates an inherent fragility. When applied to repository-level code with long execution traces, complex return types, and verbose output formatting, CWM predictions encounter two systematic failure modes: \emph{token-budget exhaustion}, where the expected output exceeds the generation budget and exact-match necessarily fails, and \emph{string-value prediction errors}, where a single character mismatch in a floating-point number, nested data structure, or formatted string invalidates the prediction regardless of semantic correctness. On SWE-bench Verified instances, we find that 53.7--67.2\% of CWM predictions are unparseable at the 4B model scale, rendering the generation approach effectively unusable for repository-level verification.
11	
12	We argue that these failure modes are not inherent to execution simulation---they are artifacts of the generation formulation. Our key insight is that the verification task requires only a binary pass/fail verdict per test, not a reconstruction of the execution output. We reformulate execution simulation as \emph{per-test binary classification} (CLS): given a code context and a test case, the model predicts a single token---\textsc{Pass} or \textsc{Fail}---sidestepping token-budget exhaustion and string-value prediction entirely (Figure~\ref{fig:reformulation}).
13	
14	This reformulation advantage is \emph{complexity-dependent}. On function-level benchmarks where execution outputs are short and simple, CWM failure modes rarely trigger, and the two formulations achieve near-equivalent accuracy: CLS attains 88.43$\pm$0.78\% and CWM 87.19$\pm$0.37\% across five random seeds (gap: 1.24 percentage points). However, as code complexity increases, the advantage amplifies along two dimensions. First, scaling model size from 4B to 8B widens the gap: CLS reaches 89.39\% versus CWM at 86.96\% (gap: 2.43pp, three seeds, $p = 0.008$), suggesting that additional capacity benefits classification but yields diminishing returns for generation. Second, at repository-level complexity on SWE-bench Verified, the gap grows dramatically: CLS achieves 83.63\% accuracy versus CWM at 58.04\%, a 25.59 percentage-point advantage at matched 4B model scale and seed.
15	
16	Crucially, this per-test formulation does not sacrifice patch-level accuracy for granularity. A TOST equivalence test confirms that per-test CLS, aggregated to patch-level verdicts, achieves statistically equivalent accuracy to a trajectory-level classifier ($p = 0.007$ at a $\pm$2pp margin), while additionally providing per-test diagnostic signals that trajectory-level verifiers discard. These diagnostics are most valuable when they are most needed: the per-test advantage concentrates in instances with multiple fail-to-pass tests ($T \geq 2$), which constitute 31\% of SWE-bench Verified instances but account for 55\% of the accuracy advantage. Furthermore, CLS and CWM exhibit complementary error patterns---CLS errors skew toward missed bugs while CWM errors skew toward false alarms---enabling an oracle ensemble accuracy of 90.63\%, pointing toward formulation diversity as a verification strategy.
17	
18	We also establish that zero-shot LLM-as-judge baselines substantially underperform fine-tuned models (8B zero-shot: 64.40\%; 32B NF4 zero-shot: 71.69\%), confirming that task-specific fine-tuning remains essential for execution simulation regardless of formulation.
19	
20	Our contributions are threefold:
21	\begin{enumerate}
22	    \item We identify a \textbf{complexity-dependent reformulation advantage}: classification and generation achieve equivalent accuracy on simple function-level code, but classification scales better with model size and to repository-level complexity where generation failure modes dominate (25.59pp gap at 4B scale on SWE-bench Verified).
23	    \item We demonstrate that per-test classification provides \textbf{diagnostic granularity at equivalent accuracy}: per-test CLS matches trajectory-level accuracy (TOST $p = 0.007$) while preserving actionable per-test failure information.
24	    \item We characterize the \textbf{accuracy-utility frontier}, showing that per-test advantage concentrates in multi-fail-to-pass instances and that CLS/CWM error complementarity (oracle ensemble: 90.63\%) motivates formulation diversity for verification pipelines.
25	\end{enumerate}
26	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "066b9dae-ab21-4272-be08-6477f0f4d275",
  "uuid": "d2978964-1233-4359-aaa8-39b830bb8693",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/_project/paper/introduction.tex",
      "content": "% Introduction draft — generated 2026-05-15, numbers from registry\n\n\\section{Introduction}\n\\label{sec:introduction}\n\nTest-time compute scaling has emerged as a powerful paradigm for improving LLM-based code repair: rather than relying on a single generation, systems produce many candidate patches and select the best one through verification~\\citep{snell2024scaling}. The bottleneck in this pipeline is the verifier. Full execution---running each candidate against the test suite in a sandboxed environment---is reliable but expensive, costing \\$1--3 and several minutes per candidate on repository-level benchmarks~\\citep{jimenez2024swebench}. Execution-free verification eliminates this cost, but existing approaches face a fundamental tradeoff between accuracy and diagnostic granularity.\n\nOn one end, trajectory-level reward models such as SWE-RM~\\citep{zhang2025swerm} score candidate patches as a whole, achieving strong binary accept/reject accuracy but discarding information about \\emph{which} tests a patch fails. This coarse signal limits downstream applications: when a candidate is rejected, the repair system has no guidance for targeted re-repair. On the other end, Code World Models (CWM)~\\citep{meta2025cwm,ding2025selfexecution} predict execution outputs per test, preserving diagnostic granularity---but formulate the task as open-ended generation, requiring the model to reproduce exact output strings token by token.\n\nThis generation formulation creates an inherent fragility. When applied to repository-level code with long execution traces, complex return types, and verbose output formatting, CWM predictions encounter two systematic failure modes: \\emph{token-budget exhaustion}, where the expected output exceeds the generation budget and exact-match necessarily fails, and \\emph{string-value prediction errors}, where a single character mismatch in a floating-point number, nested data structure, or formatted string invalidates the prediction regardless of semantic correctness. On SWE-bench Verified instances, we find that 53.7--67.2\\% of CWM predictions are unparseable at the 4B model scale, rendering the generation approach effectively unusable for repository-level verification.\n\nWe argue that these failure modes are not inherent to execution simulation---they are artifacts of the generation formulation. Our key insight is that the verification task requires only a binary pass/fail verdict per test, not a reconstruction of the execution output. We reformulate execution simulation as \\emph{per-test binary classification} (CLS): given a code context and a test case, the model predicts a single token---\\textsc{Pass} or \\textsc{Fail}---sidestepping token-budget exhaustion and string-value prediction entirely (Figure~\\ref{fig:reformulation}).\n\nThis reformulation advantage is \\emph{complexity-dependent}. On function-level benchmarks where execution outputs are short and simple, CWM failure modes rarely trigger, and the two formulations achieve near-equivalent accuracy: CLS attains 88.43$\\pm$0.78\\% and CWM 87.19$\\pm$0.37\\% across five random seeds (gap: 1.24 percentage points). However, as code complexity increases, the advantage amplifies along two dimensions. First, scaling model size from 4B to 8B widens the gap: CLS reaches 89.39\\% versus CWM at 86.96\\% (gap: 2.43pp, three seeds, $p = 0.008$), suggesting that additional capacity benefits classification but yields diminishing returns for generation. Second, at repository-level complexity on SWE-bench Verified, the gap grows dramatically: CLS achieves 83.63\\% accuracy versus CWM at 58.04\\%, a 25.59 percentage-point advantage at matched 4B model scale and seed.\n\nCrucially, this per-test formulation does not sacrifice patch-level accuracy for granularity. A TOST equivalence test confirms that per-test CLS, aggregated to patch-level verdicts, achieves statistically equivalent accuracy to a trajectory-level classifier ($p = 0.007$ at a $\\pm$2pp margin), while additionally providing per-test diagnostic signals that trajectory-level verifiers discard. These diagnostics are most valuable when they are most needed: the per-test advantage concentrates in instances with multiple fail-to-pass tests ($T \\geq 2$), which constitute 31\\% of SWE-bench Verified instances but account for 55\\% of the accuracy advantage. Furthermore, CLS and CWM exhibit complementary error patterns---CLS errors skew toward missed bugs while CWM errors skew toward false alarms---enabling an oracle ensemble accuracy of 90.63\\%, pointing toward formulation diversity as a verification strategy.\n\nWe also establish that zero-shot LLM-as-judge baselines substantially underperform fine-tuned models (8B zero-shot: 64.40\\%; 32B NF4 zero-shot: 71.69\\%), confirming that task-specific fine-tuning remains essential for execution simulation regardless of formulation.\n\nOur contributions are threefold:\n\\begin{enumerate}\n    \\item We identify a \\textbf{complexity-dependent reformulation advantage}: classification and generation achieve equivalent accuracy on simple function-level code, but classification scales better with model size and to repository-level complexity where generation failure modes dominate (25.59pp gap at 4B scale on SWE-bench Verified).\n    \\item We demonstrate that per-test classification provides \\textbf{diagnostic granularity at equivalent accuracy}: per-test CLS matches trajectory-level accuracy (TOST $p = 0.007$) while preserving actionable per-test failure information.\n    \\item We characterize the \\textbf{accuracy-utility frontier}, showing that per-test advantage concentrates in multi-fail-to-pass instances and that CLS/CWM error complementarity (oracle ensemble: 90.63\\%) motivates formulation diversity for verification pipelines.\n\\end{enumerate}\n",
      "numLines": 26,
      "startLine": 1,
      "totalLines": 26
    }
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Now I need to:

1. **Fix (a)**: Para 2 (lines 10-11) has specific numbers "53.7–67.2% unparseable" and "parseable accuracy 42–43%" — wait, I don't see "parseable accuracy 42–43%" in the text. Let me re-read. The text says "53.7--67.2\% of CWM predictions are unparseable at the 4B model scale". I need to:
   - Remove these specific numbers from para 2
   - Keep only the qualitative description of failure modes
   - Move the numbers to a later paragraph with proper qualification

2. **Fix (b)**: C1 contribution doesn't mention the zero-shot baseline. The zero-shot info is in para 5 (line 18) as a standalone paragraph. I need to add a sentence to C1 about this.

For the edits, I'm going to strip out the quantitative details from paragraph 2 where it discusses the generation formulation's fragility, replacing them with more general language about the parsing failures. Then I'll relocate those specific percentages to a later section where they can be properly contextualized. I also need to integrate the zero-shot baseline information into the C1 contribution statement. I'm revising the paper to make the quantitative claims more precise. For the first fix, I'll soften the language in paragraph 2 to be qualitative rather than citing specific percentages, then move those exact numbers (53.7-67.2% unparseable) to paragraph 4 where they fit better with the SWE-bench results discussion. For the second fix, I need to add a sentence to C1 about how the zero-shot baseline underperforms, which should go at the end of that bullet point about the complexity-dependent reformulation advantage. I need to append a sentence to the C1 section about how zero-shot LLM-as-judge baselines significantly underperform compared to fine-tuned models, which demonstrates why fine-tuning is essential.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "066b9dae-ab21-4272-be08-6477f0f4d275",
  "uuid": "240db1bf-c12b-4964-a985-2ba1ff70bdcc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012taSDXRVsgvqpoNan1MvE3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1562,
      "cache_read_input_tokens": 23173,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1562
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

_source line 8_

I see the issues. Let me make both fixes.

**Fix (a)**: Remove "53.7–67.2%" from para 2, replace with qualitative language, and relocate the number to para 4 with proper qualification.

**Fix (b)**: Add zero-shot baseline mention to C1.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "066b9dae-ab21-4272-be08-6477f0f4d275",
  "uuid": "08b485d6-18ae-4970-aa52-9e487bc5c8c8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012taSDXRVsgvqpoNan1MvE3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1562,
      "cache_read_input_tokens": 23173,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1562
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

_source line 9_

<details open><summary>🔧 Tool call — Edit · `toolu_01FvF6CC3emxUzngKPEaNJgp`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/_project/paper/introduction.tex",
  "old_string": "On SWE-bench Verified instances, we find that 53.7--67.2\\% of CWM predictions are unparseable at the 4B model scale, rendering the generation approach effectively unusable for repository-level verification.",
  "new_string": "On repository-level benchmarks with long execution traces, the majority of CWM predictions become unparseable, rendering the generation approach effectively unusable for real-world verification."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "066b9dae-ab21-4272-be08-6477f0f4d275",
  "uuid": "ac38dd71-b64b-430f-a907-d50a13882b72",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012taSDXRVsgvqpoNan1MvE3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1562,
      "cache_read_input_tokens": 23173,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1562
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

_source line 10 · 2026-05-15T14:40:25.489Z_

<details><summary>↩ Tool result · `toolu_01FvF6CC3emxUzngKPEaNJgp`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/_project/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "066b9dae-ab21-4272-be08-6477f0f4d275",
  "uuid": "8d20fb31-6f31-4139-a458-6138afc240c7",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/_project/paper/introduction.tex",
    "oldString": "On SWE-bench Verified instances, we find that 53.7--67.2\\% of CWM predictions are unparseable at the 4B model scale, rendering the generation approach effectively unusable for repository-level verification.",
    "newString": "On repository-level benchmarks with long execution traces, the majority of CWM predictions become unparseable, rendering the generation approach effectively unusable for real-world verification.",
    "originalFile": "% Introduction draft — generated 2026-05-15, numbers from registry\n\n\\section{Introduction}\n\\label{sec:introduction}\n\nTest-time compute scaling has emerged as a powerful paradigm for improving LLM-based code repair: rather than relying on a single generation, systems produce many candidate patches and select the best one through verification~\\citep{snell2024scaling}. The bottleneck in this pipeline is the verifier. Full execution---running each candidate against the test suite in a sandboxed environment---is reliable but expensive, costing \\$1--3 and several minutes per candidate on repository-level benchmarks~\\citep{jimenez2024swebench}. Execution-free verification eliminates this cost, but existing approaches face a fundamental tradeoff between accuracy and diagnostic granularity.\n\nOn one end, trajectory-level reward models such as SWE-RM~\\citep{zhang2025swerm} score candidate patches as a whole, achieving strong binary accept/reject accuracy but discarding information about \\emph{which} tests a patch fails. This coarse signal limits downstream applications: when a candidate is rejected, the repair system has no guidance for targeted re-repair. On the other end, Code World Models (CWM)~\\citep{meta2025cwm,ding2025selfexecution} predict execution outputs per test, preserving diagnostic granularity---but formulate the task as open-ended generation, requiring the model to reproduce exact output strings token by token.\n\nThis generation formulation creates an inherent fragility. When applied to repository-level code with long execution traces, complex return types, and verbose output formatting, CWM predictions encounter two systematic failure modes: \\emph{token-budget exhaustion}, where the expected output exceeds the generation budget and exact-match necessarily fails, and \\emph{string-value prediction errors}, where a single character mismatch in a floating-point number, nested data structure, or formatted string invalidates the prediction regardless of semantic correctness. On SWE-bench Verified instances, we find that 53.7--67.2\\% of CWM predictions are unparseable at the 4B model scale, rendering the generation approach effectively unusable for repository-level verification.\n\nWe argue that these failure modes are not inherent to execution simulation---they are artifacts of the generation formulation. Our key insight is that the verification task requires only a binary pass/fail verdict per test, not a reconstruction of the execution output. We reformulate execution simulation as \\emph{per-test binary classification} (CLS): given a code context and a test case, the model predicts a single token---\\textsc{Pass} or \\textsc{Fail}---sidestepping token-budget exhaustion and string-value prediction entirely (Figure~\\ref{fig:reformulation}).\n\nThis reformulation advantage is \\emph{complexity-dependent}. On function-level benchmarks where execution outputs are short and simple, CWM failure modes rarely trigger, and the two formulations achieve near-equivalent accuracy: CLS attains 88.43$\\pm$0.78\\% and CWM 87.19$\\pm$0.37\\% across five random seeds (gap: 1.24 percentage points). However, as code complexity increases, the advantage amplifies along two dimensions. First, scaling model size from 4B to 8B widens the gap: CLS reaches 89.39\\% versus CWM at 86.96\\% (gap: 2.43pp, three seeds, $p = 0.008$), suggesting that additional capacity benefits classification but yields diminishing returns for generation. Second, at repository-level complexity on SWE-bench Verified, the gap grows dramatically: CLS achieves 83.63\\% accuracy versus CWM at 58.04\\%, a 25.59 percentage-point advantage at matched 4B model scale and seed.\n\nCrucially, this per-test formulation does not sacrifice patch-level accuracy for granularity. A TOST equivalence test confirms that per-test CLS, aggregated to patch-level verdicts, achieves statistically equivalent accuracy to a trajectory-level classifier ($p = 0.007$ at a $\\pm$2pp margin), while additionally providing per-test diagnostic signals that trajectory-level verifiers discard. These diagnostics are most valuable when they are most needed: the per-test advantage concentrates in instances with multiple fail-to-pass tests ($T \\geq 2$), which constitute 31\\% of SWE-bench Verified instances but account for 55\\% of the accuracy advantage. Furthermore, CLS and CWM exhibit complementary error patterns---CLS errors skew toward missed bugs while CWM errors skew toward false alarms---enabling an oracle ensemble accuracy of 90.63\\%, pointing toward formulation diversity as a verification strategy.\n\nWe also establish that zero-shot LLM-as-judge baselines substantially underperform fine-tuned models (8B zero-shot: 64.40\\%; 32B NF4 zero-shot: 71.69\\%), confirming that task-specific fine-tuning remains essential for execution simulation regardless of formulation.\n\nOur contributions are threefold:\n\\begin{enumerate}\n    \\item We identify a \\textbf{complexity-dependent reformulation advantage}: classification and generation achieve equivalent accuracy on simple function-level code, but classification scales better with model size and to repository-level complexity where generation failure modes dominate (25.59pp gap at 4B scale on SWE-bench Verified).\n    \\item We demonstrate that per-test classification provides \\textbf{diagnostic granularity at equivalent accuracy}: per-test CLS matches trajectory-level accuracy (TOST $p = 0.007$) while preserving actionable per-test failure information.\n    \\item We characterize the \\textbf{accuracy-utility frontier}, showing that per-test advantage concentrates in multi-fail-to-pass instances and that CLS/CWM error complementarity (oracle ensemble: 90.63\\%) motivates formulation diversity for verification pipelines.\n\\end{enumerate}\n",
    "structuredPatch": [
      {
        "oldStart": 7,
        "oldLines": 7,
        "newStart": 7,
        "newLines": 7,
        "lines": [
          " ",
          " On one end, trajectory-level reward models such as SWE-RM~\\citep{zhang2025swerm} score candidate patches as a whole, achieving strong binary accept/reject accuracy but discarding information about \\emph{which} tests a patch fails. This coarse signal limits downstream applications: when a candidate is rejected, the repair system has no guidance for targeted re-repair. On the other end, Code World Models (CWM)~\\citep{meta2025cwm,ding2025selfexecution} predict execution outputs per test, preserving diagnostic granularity---but formulate the task as open-ended generation, requiring the model to reproduce exact output strings token by token.",
          " ",
          "-This generation formulation creates an inherent fragility. When applied to repository-level code with long execution traces, complex return types, and verbose output formatting, CWM predictions encounter two systematic failure modes: \\emph{token-budget exhaustion}, where the expected output exceeds the generation budget and exact-match necessarily fails, and \\emph{string-value prediction errors}, where a single character mismatch in a floating-point number, nested data structure, or formatted string invalidates the prediction regardless of semantic correctness. On SWE-bench Verified instances, we find that 53.7--67.2\\% of CWM predictions are unparseable at the 4B model scale, rendering the generation approach effectively unusable for repository-level verification.",
          "+This generation formulation creates an inherent fragility. When applied to repository-level code with long execution traces, complex return types, and verbose output formatting, CWM predictions encounter two systematic failure modes: \\emph{token-budget exhaustion}, where the expected output exceeds the generation budget and exact-match necessarily fails, and \\emph{string-value prediction errors}, where a single character mismatch in a floating-point number, nested data structure, or formatted string invalidates the prediction regardless of semantic correctness. On repository-level benchmarks with long execution traces, the majority of CWM predictions become unparseable, rendering the generation approach effectively unusable for real-world verification.",
          " ",
          " We argue that these failure modes are not inherent to execution simulation---they are artifacts of the generation formulation. Our key insight is that the verification task requires only a binary pass/fail verdict per test, not a reconstruction of the execution output. We reformulate execution simulation as \\emph{per-test binary classification} (CLS): given a code context and a test case, the model predicts a single token---\\textsc{Pass} or \\textsc{Fail}---sidestepping token-budget exhaustion and string-value prediction entirely (Figure~\\ref{fig:reformulation}).",
          " "
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

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Edit · `toolu_01EdBgjAM3ZzJMponZznt7N6`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/_project/paper/introduction.tex",
  "old_string": "a 25.59 percentage-point advantage at matched 4B model scale and seed.",
  "new_string": "a 25.59 percentage-point advantage at matched 4B model scale and seed. This gap is driven by the generation failure modes identified above: in our controlled 4B experiments (\\S\\ref{sec:analysis}), 53.7--67.2\\% of CWM predictions on SWE-bench Verified are unparseable due to token-budget exhaustion or string-value errors."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "066b9dae-ab21-4272-be08-6477f0f4d275",
  "uuid": "a07d03ab-1877-4316-98fd-08323cfd4cde",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011tLuuF3Untf3MazzJCUXew",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1398,
      "cache_read_input_tokens": 24735,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1398
      },
      "output_tokens": 69,
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

_source line 12 · 2026-05-15T14:40:29.485Z_

<details><summary>↩ Tool result · `toolu_01EdBgjAM3ZzJMponZznt7N6`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/_project/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "066b9dae-ab21-4272-be08-6477f0f4d275",
  "uuid": "e88adf32-7175-41e5-9ac1-6d20507fad05",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/_project/paper/introduction.tex",
    "oldString": "a 25.59 percentage-point advantage at matched 4B model scale and seed.",
    "newString": "a 25.59 percentage-point advantage at matched 4B model scale and seed. This gap is driven by the generation failure modes identified above: in our controlled 4B experiments (\\S\\ref{sec:analysis}), 53.7--67.2\\% of CWM predictions on SWE-bench Verified are unparseable due to token-budget exhaustion or string-value errors.",
    "originalFile": "% Introduction draft — generated 2026-05-15, numbers from registry\n\n\\section{Introduction}\n\\label{sec:introduction}\n\nTest-time compute scaling has emerged as a powerful paradigm for improving LLM-based code repair: rather than relying on a single generation, systems produce many candidate patches and select the best one through verification~\\citep{snell2024scaling}. The bottleneck in this pipeline is the verifier. Full execution---running each candidate against the test suite in a sandboxed environment---is reliable but expensive, costing \\$1--3 and several minutes per candidate on repository-level benchmarks~\\citep{jimenez2024swebench}. Execution-free verification eliminates this cost, but existing approaches face a fundamental tradeoff between accuracy and diagnostic granularity.\n\nOn one end, trajectory-level reward models such as SWE-RM~\\citep{zhang2025swerm} score candidate patches as a whole, achieving strong binary accept/reject accuracy but discarding information about \\emph{which} tests a patch fails. This coarse signal limits downstream applications: when a candidate is rejected, the repair system has no guidance for targeted re-repair. On the other end, Code World Models (CWM)~\\citep{meta2025cwm,ding2025selfexecution} predict execution outputs per test, preserving diagnostic granularity---but formulate the task as open-ended generation, requiring the model to reproduce exact output strings token by token.\n\nThis generation formulation creates an inherent fragility. When applied to repository-level code with long execution traces, complex return types, and verbose output formatting, CWM predictions encounter two systematic failure modes: \\emph{token-budget exhaustion}, where the expected output exceeds the generation budget and exact-match necessarily fails, and \\emph{string-value prediction errors}, where a single character mismatch in a floating-point number, nested data structure, or formatted string invalidates the prediction regardless of semantic correctness. On repository-level benchmarks with long execution traces, the majority of CWM predictions become unparseable, rendering the generation approach effectively unusable for real-world verification.\n\nWe argue that these failure modes are not inherent to execution simulation---they are artifacts of the generation formulation. Our key insight is that the verification task requires only a binary pass/fail verdict per test, not a reconstruction of the execution output. We reformulate execution simulation as \\emph{per-test binary classification} (CLS): given a code context and a test case, the model predicts a single token---\\textsc{Pass} or \\textsc{Fail}---sidestepping token-budget exhaustion and string-value prediction entirely (Figure~\\ref{fig:reformulation}).\n\nThis reformulation advantage is \\emph{complexity-dependent}. On function-level benchmarks where execution outputs are short and simple, CWM failure modes rarely trigger, and the two formulations achieve near-equivalent accuracy: CLS attains 88.43$\\pm$0.78\\% and CWM 87.19$\\pm$0.37\\% across five random seeds (gap: 1.24 percentage points). However, as code complexity increases, the advantage amplifies along two dimensions. First, scaling model size from 4B to 8B widens the gap: CLS reaches 89.39\\% versus CWM at 86.96\\% (gap: 2.43pp, three seeds, $p = 0.008$), suggesting that additional capacity benefits classification but yields diminishing returns for generation. Second, at repository-level complexity on SWE-bench Verified, the gap grows dramatically: CLS achieves 83.63\\% accuracy versus CWM at 58.04\\%, a 25.59 percentage-point advantage at matched 4B model scale and seed.\n\nCrucially, this per-test formulation does not sacrifice patch-level accuracy for granularity. A TOST equivalence test confirms that per-test CLS, aggregated to patch-level verdicts, achieves statistically equivalent accuracy to a trajectory-level classifier ($p = 0.007$ at a $\\pm$2pp margin), while additionally providing per-test diagnostic signals that trajectory-level verifiers discard. These diagnostics are most valuable when they are most needed: the per-test advantage concentrates in instances with multiple fail-to-pass tests ($T \\geq 2$), which constitute 31\\% of SWE-bench Verified instances but account for 55\\% of the accuracy advantage. Furthermore, CLS and CWM exhibit complementary error patterns---CLS errors skew toward missed bugs while CWM errors skew toward false alarms---enabling an oracle ensemble accuracy of 90.63\\%, pointing toward formulation diversity as a verification strategy.\n\nWe also establish that zero-shot LLM-as-judge baselines substantially underperform fine-tuned models (8B zero-shot: 64.40\\%; 32B NF4 zero-shot: 71.69\\%), confirming that task-specific fine-tuning remains essential for execution simulation regardless of formulation.\n\nOur contributions are threefold:\n\\begin{enumerate}\n    \\item We identify a \\textbf{complexity-dependent reformulation advantage}: classification and generation achieve equivalent accuracy on simple function-level code, but classification scales better with model size and to repository-level complexity where generation failure modes dominate (25.59pp gap at 4B scale on SWE-bench Verified).\n    \\item We demonstrate that per-test classification provides \\textbf{diagnostic granularity at equivalent accuracy}: per-test CLS matches trajectory-level accuracy (TOST $p = 0.007$) while preserving actionable per-test failure information.\n    \\item We characterize the \\textbf{accuracy-utility frontier}, showing that per-test advantage concentrates in multi-fail-to-pass instances and that CLS/CWM error complementarity (oracle ensemble: 90.63\\%) motivates formulation diversity for verification pipelines.\n\\end{enumerate}\n",
    "structuredPatch": [
      {
        "oldStart": 11,
        "oldLines": 7,
        "newStart": 11,
        "newLines": 7,
        "lines": [
          " ",
          " We argue that these failure modes are not inherent to execution simulation---they are artifacts of the generation formulation. Our key insight is that the verification task requires only a binary pass/fail verdict per test, not a reconstruction of the execution output. We reformulate execution simulation as \\emph{per-test binary classification} (CLS): given a code context and a test case, the model predicts a single token---\\textsc{Pass} or \\textsc{Fail}---sidestepping token-budget exhaustion and string-value prediction entirely (Figure~\\ref{fig:reformulation}).",
          " ",
          "-This reformulation advantage is \\emph{complexity-dependent}. On function-level benchmarks where execution outputs are short and simple, CWM failure modes rarely trigger, and the two formulations achieve near-equivalent accuracy: CLS attains 88.43$\\pm$0.78\\% and CWM 87.19$\\pm$0.37\\% across five random seeds (gap: 1.24 percentage points). However, as code complexity increases, the advantage amplifies along two dimensions. First, scaling model size from 4B to 8B widens the gap: CLS reaches 89.39\\% versus CWM at 86.96\\% (gap: 2.43pp, three seeds, $p = 0.008$), suggesting that additional capacity benefits classification but yields diminishing returns for generation. Second, at repository-level complexity on SWE-bench Verified, the gap grows dramatically: CLS achieves 83.63\\% accuracy versus CWM at 58.04\\%, a 25.59 percentage-point advantage at matched 4B model scale and seed.",
          "+This reformulation advantage is \\emph{complexity-dependent}. On function-level benchmarks where execution outputs are short and simple, CWM failure modes rarely trigger, and the two formulations achieve near-equivalent accuracy: CLS attains 88.43$\\pm$0.78\\% and CWM 87.19$\\pm$0.37\\% across five random seeds (gap: 1.24 percentage points). However, as code complexity increases, the advantage amplifies along two dimensions. First, scaling model size from 4B to 8B widens the gap: CLS reaches 89.39\\% versus CWM at 86.96\\% (gap: 2.43pp, three seeds, $p = 0.008$), suggesting that additional capacity benefits classification but yields diminishing returns for generation. Second, at repository-level complexity on SWE-bench Verified, the gap grows dramatically: CLS achieves 83.63\\% accuracy versus CWM at 58.04\\%, a 25.59 percentage-point advantage at matched 4B model scale and seed. This gap is driven by the generation failure modes identified above: in our controlled 4B experiments (\\S\\ref{sec:analysis}), 53.7--67.2\\% of CWM predictions on SWE-bench Verified are unparseable due to token-budget exhaustion or string-value errors.",
          " ",
          " Crucially, this per-test formulation does not sacrifice patch-level accuracy for granularity. A TOST equivalence test confirms that per-test CLS, aggregated to patch-level verdicts, achieves statistically equivalent accuracy to a trajectory-level classifier ($p = 0.007$ at a $\\pm$2pp margin), while additionally providing per-test diagnostic signals that trajectory-level verifiers discard. These diagnostics are most valuable when they are most needed: the per-test advantage concentrates in instances with multiple fail-to-pass tests ($T \\geq 2$), which constitute 31\\% of SWE-bench Verified instances but account for 55\\% of the accuracy advantage. Furthermore, CLS and CWM exhibit complementary error patterns---CLS errors skew toward missed bugs while CWM errors skew toward false alarms---enabling an oracle ensemble accuracy of 90.63\\%, pointing toward formulation diversity as a verification strategy.",
          " "
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

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Edit · `toolu_01BeEEhiyzypSsqjeAmqxF5d`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/_project/paper/introduction.tex",
  "old_string": "    \\item We identify a \\textbf{complexity-dependent reformulation advantage}: classification and generation achieve equivalent accuracy on simple function-level code, but classification scales better with model size and to repository-level complexity where generation failure modes dominate (25.59pp gap at 4B scale on SWE-bench Verified).",
  "new_string": "    \\item We identify a \\textbf{complexity-dependent reformulation advantage}: classification and generation achieve equivalent accuracy on simple function-level code, but classification scales better with model size and to repository-level complexity where generation failure modes dominate (25.59pp gap at 4B scale on SWE-bench Verified). Furthermore, zero-shot LLM-as-judge baselines substantially underperform fine-tuned models (32B NF4: 71.69\\% vs.\\ fine-tuned 4B: 88.43\\%), confirming that task-specific fine-tuning remains essential."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "066b9dae-ab21-4272-be08-6477f0f4d275",
  "uuid": "f6988bdb-78d5-4352-86b1-b8937300df18",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fc7Z112r5k4MUhKHy4cvJH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 313,
      "cache_read_input_tokens": 26133,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 313
      },
      "output_tokens": 69,
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

_source line 14 · 2026-05-15T14:40:34.583Z_

<details><summary>↩ Tool result · `toolu_01BeEEhiyzypSsqjeAmqxF5d`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/_project/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "066b9dae-ab21-4272-be08-6477f0f4d275",
  "uuid": "b1469c27-4eac-4c5f-9fa6-5667b30ff132",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/_project/paper/introduction.tex",
    "oldString": "    \\item We identify a \\textbf{complexity-dependent reformulation advantage}: classification and generation achieve equivalent accuracy on simple function-level code, but classification scales better with model size and to repository-level complexity where generation failure modes dominate (25.59pp gap at 4B scale on SWE-bench Verified).",
    "newString": "    \\item We identify a \\textbf{complexity-dependent reformulation advantage}: classification and generation achieve equivalent accuracy on simple function-level code, but classification scales better with model size and to repository-level complexity where generation failure modes dominate (25.59pp gap at 4B scale on SWE-bench Verified). Furthermore, zero-shot LLM-as-judge baselines substantially underperform fine-tuned models (32B NF4: 71.69\\% vs.\\ fine-tuned 4B: 88.43\\%), confirming that task-specific fine-tuning remains essential.",
    "originalFile": "% Introduction draft — generated 2026-05-15, numbers from registry\n\n\\section{Introduction}\n\\label{sec:introduction}\n\nTest-time compute scaling has emerged as a powerful paradigm for improving LLM-based code repair: rather than relying on a single generation, systems produce many candidate patches and select the best one through verification~\\citep{snell2024scaling}. The bottleneck in this pipeline is the verifier. Full execution---running each candidate against the test suite in a sandboxed environment---is reliable but expensive, costing \\$1--3 and several minutes per candidate on repository-level benchmarks~\\citep{jimenez2024swebench}. Execution-free verification eliminates this cost, but existing approaches face a fundamental tradeoff between accuracy and diagnostic granularity.\n\nOn one end, trajectory-level reward models such as SWE-RM~\\citep{zhang2025swerm} score candidate patches as a whole, achieving strong binary accept/reject accuracy but discarding information about \\emph{which} tests a patch fails. This coarse signal limits downstream applications: when a candidate is rejected, the repair system has no guidance for targeted re-repair. On the other end, Code World Models (CWM)~\\citep{meta2025cwm,ding2025selfexecution} predict execution outputs per test, preserving diagnostic granularity---but formulate the task as open-ended generation, requiring the model to reproduce exact output strings token by token.\n\nThis generation formulation creates an inherent fragility. When applied to repository-level code with long execution traces, complex return types, and verbose output formatting, CWM predictions encounter two systematic failure modes: \\emph{token-budget exhaustion}, where the expected output exceeds the generation budget and exact-match necessarily fails, and \\emph{string-value prediction errors}, where a single character mismatch in a floating-point number, nested data structure, or formatted string invalidates the prediction regardless of semantic correctness. On repository-level benchmarks with long execution traces, the majority of CWM predictions become unparseable, rendering the generation approach effectively unusable for real-world verification.\n\nWe argue that these failure modes are not inherent to execution simulation---they are artifacts of the generation formulation. Our key insight is that the verification task requires only a binary pass/fail verdict per test, not a reconstruction of the execution output. We reformulate execution simulation as \\emph{per-test binary classification} (CLS): given a code context and a test case, the model predicts a single token---\\textsc{Pass} or \\textsc{Fail}---sidestepping token-budget exhaustion and string-value prediction entirely (Figure~\\ref{fig:reformulation}).\n\nThis reformulation advantage is \\emph{complexity-dependent}. On function-level benchmarks where execution outputs are short and simple, CWM failure modes rarely trigger, and the two formulations achieve near-equivalent accuracy: CLS attains 88.43$\\pm$0.78\\% and CWM 87.19$\\pm$0.37\\% across five random seeds (gap: 1.24 percentage points). However, as code complexity increases, the advantage amplifies along two dimensions. First, scaling model size from 4B to 8B widens the gap: CLS reaches 89.39\\% versus CWM at 86.96\\% (gap: 2.43pp, three seeds, $p = 0.008$), suggesting that additional capacity benefits classification but yields diminishing returns for generation. Second, at repository-level complexity on SWE-bench Verified, the gap grows dramatically: CLS achieves 83.63\\% accuracy versus CWM at 58.04\\%, a 25.59 percentage-point advantage at matched 4B model scale and seed. This gap is driven by the generation failure modes identified above: in our controlled 4B experiments (\\S\\ref{sec:analysis}), 53.7--67.2\\% of CWM predictions on SWE-bench Verified are unparseable due to token-budget exhaustion or string-value errors.\n\nCrucially, this per-test formulation does not sacrifice patch-level accuracy for granularity. A TOST equivalence test confirms that per-test CLS, aggregated to patch-level verdicts, achieves statistically equivalent accuracy to a trajectory-level classifier ($p = 0.007$ at a $\\pm$2pp margin), while additionally providing per-test diagnostic signals that trajectory-level verifiers discard. These diagnostics are most valuable when they are most needed: the per-test advantage concentrates in instances with multiple fail-to-pass tests ($T \\geq 2$), which constitute 31\\% of SWE-bench Verified instances but account for 55\\% of the accuracy advantage. Furthermore, CLS and CWM exhibit complementary error patterns---CLS errors skew toward missed bugs while CWM errors skew toward false alarms---enabling an oracle ensemble accuracy of 90.63\\%, pointing toward formulation diversity as a verification strategy.\n\nWe also establish that zero-shot LLM-as-judge baselines substantially underperform fine-tuned models (8B zero-shot: 64.40\\%; 32B NF4 zero-shot: 71.69\\%), confirming that task-specific fine-tuning remains essential for execution simulation regardless of formulation.\n\nOur contributions are threefold:\n\\begin{enumerate}\n    \\item We identify a \\textbf{complexity-dependent reformulation advantage}: classification and generation achieve equivalent accuracy on simple function-level code, but classification scales better with model size and to repository-level complexity where generation failure modes dominate (25.59pp gap at 4B scale on SWE-bench Verified).\n    \\item We demonstrate that per-test classification provides \\textbf{diagnostic granularity at equivalent accuracy}: per-test CLS matches trajectory-level accuracy (TOST $p = 0.007$) while preserving actionable per-test failure information.\n    \\item We characterize the \\textbf{accuracy-utility frontier}, showing that per-test advantage concentrates in multi-fail-to-pass instances and that CLS/CWM error complementarity (oracle ensemble: 90.63\\%) motivates formulation diversity for verification pipelines.\n\\end{enumerate}\n",
    "structuredPatch": [
      {
        "oldStart": 19,
        "oldLines": 7,
        "newStart": 19,
        "newLines": 7,
        "lines": [
          " ",
          " Our contributions are threefold:",
          " \\begin{enumerate}",
          "-    \\item We identify a \\textbf{complexity-dependent reformulation advantage}: classification and generation achieve equivalent accuracy on simple function-level code, but classification scales better with model size and to repository-level complexity where generation failure modes dominate (25.59pp gap at 4B scale on SWE-bench Verified).",
          "+    \\item We identify a \\textbf{complexity-dependent reformulation advantage}: classification and generation achieve equivalent accuracy on simple function-level code, but classification scales better with model size and to repository-level complexity where generation failure modes dominate (25.59pp gap at 4B scale on SWE-bench Verified). Furthermore, zero-shot LLM-as-judge baselines substantially underperform fine-tuned models (32B NF4: 71.69\\% vs.\\ fine-tuned 4B: 88.43\\%), confirming that task-specific fine-tuning remains essential.",
          "     \\item We demonstrate that per-test classification provides \\textbf{diagnostic granularity at equivalent accuracy}: per-test CLS matches trajectory-level accuracy (TOST $p = 0.007$) while preserving actionable per-test failure information.",
          "     \\item We characterize the \\textbf{accuracy-utility frontier}, showing that per-test advantage concentrates in multi-fail-to-pass instances and that CLS/CWM error complementarity (oracle ensemble: 90.63\\%) motivates formulation diversity for verification pipelines.",
          " \\end{enumerate}"
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

_source line 15_

Now let me verify the section label reference is correct — checking if `sec:analysis` exists, or if I need a different label.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "066b9dae-ab21-4272-be08-6477f0f4d275",
  "uuid": "0d552f0a-5160-4ecb-a317-e157a139d950",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011pwrZ95F5kfWohzJcEMj2U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 410,
      "cache_read_input_tokens": 26446,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 410
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

_source line 16_

<details open><summary>🔧 Tool call — Grep · `toolu_01MVC2YiL61r32WQzDzxrAPi`</summary>

```json
{
  "pattern": "\\\\label\\{sec:",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/_project/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "066b9dae-ab21-4272-be08-6477f0f4d275",
  "uuid": "657e6d13-cf16-4145-a167-835cc23492f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011pwrZ95F5kfWohzJcEMj2U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 410,
      "cache_read_input_tokens": 26446,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 410
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

_source line 17 · 2026-05-15T14:40:38.768Z_

<details><summary>↩ Tool result · `toolu_01MVC2YiL61r32WQzDzxrAPi`</summary>

```text
artifacts/_project/paper/related_work.tex:2:\label{sec:related_work}
artifacts/_project/paper/introduction_304198.tex:4:\label{sec:introduction}
artifacts/_project/paper/method.tex:6:\label{sec:method}
artifacts/_project/paper/introduction.tex:4:\label{sec:introduction}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "066b9dae-ab21-4272-be08-6477f0f4d275",
  "uuid": "8df1be6d-b7dd-494c-a76d-37def0f8b2b4",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/_project/paper/related_work.tex:2:\\label{sec:related_work}\nartifacts/_project/paper/introduction_304198.tex:4:\\label{sec:introduction}\nartifacts/_project/paper/method.tex:6:\\label{sec:method}\nartifacts/_project/paper/introduction.tex:4:\\label{sec:introduction}",
    "numLines": 4
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Grep · `toolu_01HB4KC1C83a5uQ8kKpoNjWk`</summary>

```json
{
  "pattern": "\\\\label\\{sec:",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/_project/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "head_limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "066b9dae-ab21-4272-be08-6477f0f4d275",
  "uuid": "d49a2997-24bf-44ab-8b37-56e662e2d850",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015oD8G2qgxnVYDvGetJXfJa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 249,
      "cache_read_input_tokens": 26856,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 249
      },
      "output_tokens": 69,
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

_source line 19 · 2026-05-15T14:40:42.247Z_

<details><summary>↩ Tool result · `toolu_01HB4KC1C83a5uQ8kKpoNjWk`</summary>

```text
artifacts/_project/paper/related_work.tex:2:\label{sec:related_work}
artifacts/_project/paper/introduction_304198.tex:4:\label{sec:introduction}
artifacts/_project/paper/method.tex:6:\label{sec:method}
artifacts/_project/paper/introduction.tex:4:\label{sec:introduction}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "066b9dae-ab21-4272-be08-6477f0f4d275",
  "uuid": "44a10f05-a710-49b3-92d0-b0462fef4bd4",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/_project/paper/related_work.tex:2:\\label{sec:related_work}\nartifacts/_project/paper/introduction_304198.tex:4:\\label{sec:introduction}\nartifacts/_project/paper/method.tex:6:\\label{sec:method}\nartifacts/_project/paper/introduction.tex:4:\\label{sec:introduction}",
    "numLines": 4
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Glob · `toolu_015h7YHCpT1Y4imzQXRKmnAX`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "066b9dae-ab21-4272-be08-6477f0f4d275",
  "uuid": "c42ef694-6253-4d87-a4af-b60a4c75e5e2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y7CT9XbNCGDSNK2GyNoTHL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 257,
      "cache_read_input_tokens": 27105,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 257
      },
      "output_tokens": 66,
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

_source line 21 · 2026-05-15T14:40:45.141Z_

<details><summary>↩ Tool result · `toolu_015h7YHCpT1Y4imzQXRKmnAX`</summary>

```text
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/method.tex
artifacts/_project/paper/introduction_304198.tex
artifacts/_project/paper/introduction.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "066b9dae-ab21-4272-be08-6477f0f4d275",
  "uuid": "26fadd1f-3abf-4685-9682-5c3abf82e219",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/related_work.tex",
      "artifacts/_project/paper/method.tex",
      "artifacts/_project/paper/introduction_304198.tex",
      "artifacts/_project/paper/introduction.tex"
    ],
    "durationMs": 9,
    "numFiles": 4,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 22_

<details><summary>Logged reasoning block</summary>

```text
There's no `sec:analysis` label in the existing tex files. The writing plan mentioned "§3.6" — let me check if there's a section 3.6 reference pattern used. Since the paper structure may not be fully written yet, I should use a more robust reference. Let me check what section the CWM parseability analysis is expected to be in.

Actually, the task says the numbers are from "§3.6" in the writing plan. But since the labels aren't defined yet, I should use a hardcoded section reference like `\S3.6` instead of `\S\ref{sec:analysis}`. 

I could just reference section 3 generally, or better yet, use `\S\ref{sec:method}` since that's the label I found in method.tex. Let me go with a safe reference that won't break.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "066b9dae-ab21-4272-be08-6477f0f4d275",
  "uuid": "c5f5e042-50ee-4648-8953-969636765d8f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AGVjLB1KTNsH9Ybfrdkjss",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 265,
      "cache_read_input_tokens": 27362,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 265
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

_source line 23_

No `sec:analysis` label exists. Let me fix the reference to point to the method section instead.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "066b9dae-ab21-4272-be08-6477f0f4d275",
  "uuid": "43a83df1-53b7-439c-aab8-188739cdc0d7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AGVjLB1KTNsH9Ybfrdkjss",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 265,
      "cache_read_input_tokens": 27362,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 265
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

_source line 24_

<details open><summary>🔧 Tool call — Edit · `toolu_01DjBE12Ug41iPzRnzKaFJDE`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/_project/paper/introduction.tex",
  "old_string": "in our controlled 4B experiments (\\S\\ref{sec:analysis})",
  "new_string": "in our controlled 4B experiments (\\S\\ref{sec:method})"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "066b9dae-ab21-4272-be08-6477f0f4d275",
  "uuid": "55bf0aec-8044-4a9d-9691-e8a0572fd000",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AGVjLB1KTNsH9Ybfrdkjss",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 265,
      "cache_read_input_tokens": 27362,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 265
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

_source line 25 · 2026-05-15T14:40:58.314Z_

<details><summary>↩ Tool result · `toolu_01DjBE12Ug41iPzRnzKaFJDE`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/_project/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "066b9dae-ab21-4272-be08-6477f0f4d275",
  "uuid": "69dfd8bb-e7dd-42b4-ad57-b6a53ddbbd40",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/_project/paper/introduction.tex",
    "oldString": "in our controlled 4B experiments (\\S\\ref{sec:analysis})",
    "newString": "in our controlled 4B experiments (\\S\\ref{sec:method})",
    "originalFile": "% Introduction draft — generated 2026-05-15, numbers from registry\n\n\\section{Introduction}\n\\label{sec:introduction}\n\nTest-time compute scaling has emerged as a powerful paradigm for improving LLM-based code repair: rather than relying on a single generation, systems produce many candidate patches and select the best one through verification~\\citep{snell2024scaling}. The bottleneck in this pipeline is the verifier. Full execution---running each candidate against the test suite in a sandboxed environment---is reliable but expensive, costing \\$1--3 and several minutes per candidate on repository-level benchmarks~\\citep{jimenez2024swebench}. Execution-free verification eliminates this cost, but existing approaches face a fundamental tradeoff between accuracy and diagnostic granularity.\n\nOn one end, trajectory-level reward models such as SWE-RM~\\citep{zhang2025swerm} score candidate patches as a whole, achieving strong binary accept/reject accuracy but discarding information about \\emph{which} tests a patch fails. This coarse signal limits downstream applications: when a candidate is rejected, the repair system has no guidance for targeted re-repair. On the other end, Code World Models (CWM)~\\citep{meta2025cwm,ding2025selfexecution} predict execution outputs per test, preserving diagnostic granularity---but formulate the task as open-ended generation, requiring the model to reproduce exact output strings token by token.\n\nThis generation formulation creates an inherent fragility. When applied to repository-level code with long execution traces, complex return types, and verbose output formatting, CWM predictions encounter two systematic failure modes: \\emph{token-budget exhaustion}, where the expected output exceeds the generation budget and exact-match necessarily fails, and \\emph{string-value prediction errors}, where a single character mismatch in a floating-point number, nested data structure, or formatted string invalidates the prediction regardless of semantic correctness. On repository-level benchmarks with long execution traces, the majority of CWM predictions become unparseable, rendering the generation approach effectively unusable for real-world verification.\n\nWe argue that these failure modes are not inherent to execution simulation---they are artifacts of the generation formulation. Our key insight is that the verification task requires only a binary pass/fail verdict per test, not a reconstruction of the execution output. We reformulate execution simulation as \\emph{per-test binary classification} (CLS): given a code context and a test case, the model predicts a single token---\\textsc{Pass} or \\textsc{Fail}---sidestepping token-budget exhaustion and string-value prediction entirely (Figure~\\ref{fig:reformulation}).\n\nThis reformulation advantage is \\emph{complexity-dependent}. On function-level benchmarks where execution outputs are short and simple, CWM failure modes rarely trigger, and the two formulations achieve near-equivalent accuracy: CLS attains 88.43$\\pm$0.78\\% and CWM 87.19$\\pm$0.37\\% across five random seeds (gap: 1.24 percentage points). However, as code complexity increases, the advantage amplifies along two dimensions. First, scaling model size from 4B to 8B widens the gap: CLS reaches 89.39\\% versus CWM at 86.96\\% (gap: 2.43pp, three seeds, $p = 0.008$), suggesting that additional capacity benefits classification but yields diminishing returns for generation. Second, at repository-level complexity on SWE-bench Verified, the gap grows dramatically: CLS achieves 83.63\\% accuracy versus CWM at 58.04\\%, a 25.59 percentage-point advantage at matched 4B model scale and seed. This gap is driven by the generation failure modes identified above: in our controlled 4B experiments (\\S\\ref{sec:analysis}), 53.7--67.2\\% of CWM predictions on SWE-bench Verified are unparseable due to token-budget exhaustion or string-value errors.\n\nCrucially, this per-test formulation does not sacrifice patch-level accuracy for granularity. A TOST equivalence test confirms that per-test CLS, aggregated to patch-level verdicts, achieves statistically equivalent accuracy to a trajectory-level classifier ($p = 0.007$ at a $\\pm$2pp margin), while additionally providing per-test diagnostic signals that trajectory-level verifiers discard. These diagnostics are most valuable when they are most needed: the per-test advantage concentrates in instances with multiple fail-to-pass tests ($T \\geq 2$), which constitute 31\\% of SWE-bench Verified instances but account for 55\\% of the accuracy advantage. Furthermore, CLS and CWM exhibit complementary error patterns---CLS errors skew toward missed bugs while CWM errors skew toward false alarms---enabling an oracle ensemble accuracy of 90.63\\%, pointing toward formulation diversity as a verification strategy.\n\nWe also establish that zero-shot LLM-as-judge baselines substantially underperform fine-tuned models (8B zero-shot: 64.40\\%; 32B NF4 zero-shot: 71.69\\%), confirming that task-specific fine-tuning remains essential for execution simulation regardless of formulation.\n\nOur contributions are threefold:\n\\begin{enumerate}\n    \\item We identify a \\textbf{complexity-dependent reformulation advantage}: classification and generation achieve equivalent accuracy on simple function-level code, but classification scales better with model size and to repository-level complexity where generation failure modes dominate (25.59pp gap at 4B scale on SWE-bench Verified). Furthermore, zero-shot LLM-as-judge baselines substantially underperform fine-tuned models (32B NF4: 71.69\\% vs.\\ fine-tuned 4B: 88.43\\%), confirming that task-specific fine-tuning remains essential.\n    \\item We demonstrate that per-test classification provides \\textbf{diagnostic granularity at equivalent accuracy}: per-test CLS matches trajectory-level accuracy (TOST $p = 0.007$) while preserving actionable per-test failure information.\n    \\item We characterize the \\textbf{accuracy-utility frontier}, showing that per-test advantage concentrates in multi-fail-to-pass instances and that CLS/CWM error complementarity (oracle ensemble: 90.63\\%) motivates formulation diversity for verification pipelines.\n\\end{enumerate}\n",
    "structuredPatch": [
      {
        "oldStart": 11,
        "oldLines": 7,
        "newStart": 11,
        "newLines": 7,
        "lines": [
          " ",
          " We argue that these failure modes are not inherent to execution simulation---they are artifacts of the generation formulation. Our key insight is that the verification task requires only a binary pass/fail verdict per test, not a reconstruction of the execution output. We reformulate execution simulation as \\emph{per-test binary classification} (CLS): given a code context and a test case, the model predicts a single token---\\textsc{Pass} or \\textsc{Fail}---sidestepping token-budget exhaustion and string-value prediction entirely (Figure~\\ref{fig:reformulation}).",
          " ",
          "-This reformulation advantage is \\emph{complexity-dependent}. On function-level benchmarks where execution outputs are short and simple, CWM failure modes rarely trigger, and the two formulations achieve near-equivalent accuracy: CLS attains 88.43$\\pm$0.78\\% and CWM 87.19$\\pm$0.37\\% across five random seeds (gap: 1.24 percentage points). However, as code complexity increases, the advantage amplifies along two dimensions. First, scaling model size from 4B to 8B widens the gap: CLS reaches 89.39\\% versus CWM at 86.96\\% (gap: 2.43pp, three seeds, $p = 0.008$), suggesting that additional capacity benefits classification but yields diminishing returns for generation. Second, at repository-level complexity on SWE-bench Verified, the gap grows dramatically: CLS achieves 83.63\\% accuracy versus CWM at 58.04\\%, a 25.59 percentage-point advantage at matched 4B model scale and seed. This gap is driven by the generation failure modes identified above: in our controlled 4B experiments (\\S\\ref{sec:analysis}), 53.7--67.2\\% of CWM predictions on SWE-bench Verified are unparseable due to token-budget exhaustion or string-value errors.",
          "+This reformulation advantage is \\emph{complexity-dependent}. On function-level benchmarks where execution outputs are short and simple, CWM failure modes rarely trigger, and the two formulations achieve near-equivalent accuracy: CLS attains 88.43$\\pm$0.78\\% and CWM 87.19$\\pm$0.37\\% across five random seeds (gap: 1.24 percentage points). However, as code complexity increases, the advantage amplifies along two dimensions. First, scaling model size from 4B to 8B widens the gap: CLS reaches 89.39\\% versus CWM at 86.96\\% (gap: 2.43pp, three seeds, $p = 0.008$), suggesting that additional capacity benefits classification but yields diminishing returns for generation. Second, at repository-level complexity on SWE-bench Verified, the gap grows dramatically: CLS achieves 83.63\\% accuracy versus CWM at 58.04\\%, a 25.59 percentage-point advantage at matched 4B model scale and seed. This gap is driven by the generation failure modes identified above: in our controlled 4B experiments (\\S\\ref{sec:method}), 53.7--67.2\\% of CWM predictions on SWE-bench Verified are unparseable due to token-budget exhaustion or string-value errors.",
          " ",
          " Crucially, this per-test formulation does not sacrifice patch-level accuracy for granularity. A TOST equivalence test confirms that per-test CLS, aggregated to patch-level verdicts, achieves statistically equivalent accuracy to a trajectory-level classifier ($p = 0.007$ at a $\\pm$2pp margin), while additionally providing per-test diagnostic signals that trajectory-level verifiers discard. These diagnostics are most valuable when they are most needed: the per-test advantage concentrates in instances with multiple fail-to-pass tests ($T \\geq 2$), which constitute 31\\% of SWE-bench Verified instances but account for 55\\% of the accuracy advantage. Furthermore, CLS and CWM exhibit complementary error patterns---CLS errors skew toward missed bugs while CWM errors skew toward false alarms---enabling an oracle ensemble accuracy of 90.63\\%, pointing toward formulation diversity as a verification strategy.",
          " "
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

_source line 26_

Now let me verify the final file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "066b9dae-ab21-4272-be08-6477f0f4d275",
  "uuid": "462c135a-7d61-403c-898e-2da7f16d4c0e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WMxyuYP9tzWgv6PqnmCdAB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 687,
      "cache_read_input_tokens": 27627,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 687
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

_source line 27_

<details open><summary>🔧 Tool call — Read · `toolu_011V5QvgdffBQDjztLNKZF6C`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "066b9dae-ab21-4272-be08-6477f0f4d275",
  "uuid": "0b4ce9dc-7b3d-4ef9-8ce9-563c96bb7301",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WMxyuYP9tzWgv6PqnmCdAB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 687,
      "cache_read_input_tokens": 27627,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 687
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

_source line 28 · 2026-05-15T14:41:01.129Z_

<details><summary>↩ Tool result · `toolu_011V5QvgdffBQDjztLNKZF6C`</summary>

```text
1	% Introduction draft — generated 2026-05-15, numbers from registry
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Test-time compute scaling has emerged as a powerful paradigm for improving LLM-based code repair: rather than relying on a single generation, systems produce many candidate patches and select the best one through verification~\citep{snell2024scaling}. The bottleneck in this pipeline is the verifier. Full execution---running each candidate against the test suite in a sandboxed environment---is reliable but expensive, costing \$1--3 and several minutes per candidate on repository-level benchmarks~\citep{jimenez2024swebench}. Execution-free verification eliminates this cost, but existing approaches face a fundamental tradeoff between accuracy and diagnostic granularity.
7	
8	On one end, trajectory-level reward models such as SWE-RM~\citep{zhang2025swerm} score candidate patches as a whole, achieving strong binary accept/reject accuracy but discarding information about \emph{which} tests a patch fails. This coarse signal limits downstream applications: when a candidate is rejected, the repair system has no guidance for targeted re-repair. On the other end, Code World Models (CWM)~\citep{meta2025cwm,ding2025selfexecution} predict execution outputs per test, preserving diagnostic granularity---but formulate the task as open-ended generation, requiring the model to reproduce exact output strings token by token.
9	
10	This generation formulation creates an inherent fragility. When applied to repository-level code with long execution traces, complex return types, and verbose output formatting, CWM predictions encounter two systematic failure modes: \emph{token-budget exhaustion}, where the expected output exceeds the generation budget and exact-match necessarily fails, and \emph{string-value prediction errors}, where a single character mismatch in a floating-point number, nested data structure, or formatted string invalidates the prediction regardless of semantic correctness. On repository-level benchmarks with long execution traces, the majority of CWM predictions become unparseable, rendering the generation approach effectively unusable for real-world verification.
11	
12	We argue that these failure modes are not inherent to execution simulation---they are artifacts of the generation formulation. Our key insight is that the verification task requires only a binary pass/fail verdict per test, not a reconstruction of the execution output. We reformulate execution simulation as \emph{per-test binary classification} (CLS): given a code context and a test case, the model predicts a single token---\textsc{Pass} or \textsc{Fail}---sidestepping token-budget exhaustion and string-value prediction entirely (Figure~\ref{fig:reformulation}).
13	
14	This reformulation advantage is \emph{complexity-dependent}. On function-level benchmarks where execution outputs are short and simple, CWM failure modes rarely trigger, and the two formulations achieve near-equivalent accuracy: CLS attains 88.43$\pm$0.78\% and CWM 87.19$\pm$0.37\% across five random seeds (gap: 1.24 percentage points). However, as code complexity increases, the advantage amplifies along two dimensions. First, scaling model size from 4B to 8B widens the gap: CLS reaches 89.39\% versus CWM at 86.96\% (gap: 2.43pp, three seeds, $p = 0.008$), suggesting that additional capacity benefits classification but yields diminishing returns for generation. Second, at repository-level complexity on SWE-bench Verified, the gap grows dramatically: CLS achieves 83.63\% accuracy versus CWM at 58.04\%, a 25.59 percentage-point advantage at matched 4B model scale and seed. This gap is driven by the generation failure modes identified above: in our controlled 4B experiments (\S\ref{sec:method}), 53.7--67.2\% of CWM predictions on SWE-bench Verified are unparseable due to token-budget exhaustion or string-value errors.
15	
16	Crucially, this per-test formulation does not sacrifice patch-level accuracy for granularity. A TOST equivalence test confirms that per-test CLS, aggregated to patch-level verdicts, achieves statistically equivalent accuracy to a trajectory-level classifier ($p = 0.007$ at a $\pm$2pp margin), while additionally providing per-test diagnostic signals that trajectory-level verifiers discard. These diagnostics are most valuable when they are most needed: the per-test advantage concentrates in instances with multiple fail-to-pass tests ($T \geq 2$), which constitute 31\% of SWE-bench Verified instances but account for 55\% of the accuracy advantage. Furthermore, CLS and CWM exhibit complementary error patterns---CLS errors skew toward missed bugs while CWM errors skew toward false alarms---enabling an oracle ensemble accuracy of 90.63\%, pointing toward formulation diversity as a verification strategy.
17	
18	We also establish that zero-shot LLM-as-judge baselines substantially underperform fine-tuned models (8B zero-shot: 64.40\%; 32B NF4 zero-shot: 71.69\%), confirming that task-specific fine-tuning remains essential for execution simulation regardless of formulation.
19	
20	Our contributions are threefold:
21	\begin{enumerate}
22	    \item We identify a \textbf{complexity-dependent reformulation advantage}: classification and generation achieve equivalent accuracy on simple function-level code, but classification scales better with model size and to repository-level complexity where generation failure modes dominate (25.59pp gap at 4B scale on SWE-bench Verified). Furthermore, zero-shot LLM-as-judge baselines substantially underperform fine-tuned models (32B NF4: 71.69\% vs.\ fine-tuned 4B: 88.43\%), confirming that task-specific fine-tuning remains essential.
23	    \item We demonstrate that per-test classification provides \textbf{diagnostic granularity at equivalent accuracy}: per-test CLS matches trajectory-level accuracy (TOST $p = 0.007$) while preserving actionable per-test failure information.
24	    \item We characterize the \textbf{accuracy-utility frontier}, showing that per-test advantage concentrates in multi-fail-to-pass instances and that CLS/CWM error complementarity (oracle ensemble: 90.63\%) motivates formulation diversity for verification pipelines.
25	\end{enumerate}
26	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "066b9dae-ab21-4272-be08-6477f0f4d275",
  "uuid": "505ffbb6-8f58-4bee-8c24-ec79cff03e12",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/_project/paper/introduction.tex",
      "content": "% Introduction draft — generated 2026-05-15, numbers from registry\n\n\\section{Introduction}\n\\label{sec:introduction}\n\nTest-time compute scaling has emerged as a powerful paradigm for improving LLM-based code repair: rather than relying on a single generation, systems produce many candidate patches and select the best one through verification~\\citep{snell2024scaling}. The bottleneck in this pipeline is the verifier. Full execution---running each candidate against the test suite in a sandboxed environment---is reliable but expensive, costing \\$1--3 and several minutes per candidate on repository-level benchmarks~\\citep{jimenez2024swebench}. Execution-free verification eliminates this cost, but existing approaches face a fundamental tradeoff between accuracy and diagnostic granularity.\n\nOn one end, trajectory-level reward models such as SWE-RM~\\citep{zhang2025swerm} score candidate patches as a whole, achieving strong binary accept/reject accuracy but discarding information about \\emph{which} tests a patch fails. This coarse signal limits downstream applications: when a candidate is rejected, the repair system has no guidance for targeted re-repair. On the other end, Code World Models (CWM)~\\citep{meta2025cwm,ding2025selfexecution} predict execution outputs per test, preserving diagnostic granularity---but formulate the task as open-ended generation, requiring the model to reproduce exact output strings token by token.\n\nThis generation formulation creates an inherent fragility. When applied to repository-level code with long execution traces, complex return types, and verbose output formatting, CWM predictions encounter two systematic failure modes: \\emph{token-budget exhaustion}, where the expected output exceeds the generation budget and exact-match necessarily fails, and \\emph{string-value prediction errors}, where a single character mismatch in a floating-point number, nested data structure, or formatted string invalidates the prediction regardless of semantic correctness. On repository-level benchmarks with long execution traces, the majority of CWM predictions become unparseable, rendering the generation approach effectively unusable for real-world verification.\n\nWe argue that these failure modes are not inherent to execution simulation---they are artifacts of the generation formulation. Our key insight is that the verification task requires only a binary pass/fail verdict per test, not a reconstruction of the execution output. We reformulate execution simulation as \\emph{per-test binary classification} (CLS): given a code context and a test case, the model predicts a single token---\\textsc{Pass} or \\textsc{Fail}---sidestepping token-budget exhaustion and string-value prediction entirely (Figure~\\ref{fig:reformulation}).\n\nThis reformulation advantage is \\emph{complexity-dependent}. On function-level benchmarks where execution outputs are short and simple, CWM failure modes rarely trigger, and the two formulations achieve near-equivalent accuracy: CLS attains 88.43$\\pm$0.78\\% and CWM 87.19$\\pm$0.37\\% across five random seeds (gap: 1.24 percentage points). However, as code complexity increases, the advantage amplifies along two dimensions. First, scaling model size from 4B to 8B widens the gap: CLS reaches 89.39\\% versus CWM at 86.96\\% (gap: 2.43pp, three seeds, $p = 0.008$), suggesting that additional capacity benefits classification but yields diminishing returns for generation. Second, at repository-level complexity on SWE-bench Verified, the gap grows dramatically: CLS achieves 83.63\\% accuracy versus CWM at 58.04\\%, a 25.59 percentage-point advantage at matched 4B model scale and seed. This gap is driven by the generation failure modes identified above: in our controlled 4B experiments (\\S\\ref{sec:method}), 53.7--67.2\\% of CWM predictions on SWE-bench Verified are unparseable due to token-budget exhaustion or string-value errors.\n\nCrucially, this per-test formulation does not sacrifice patch-level accuracy for granularity. A TOST equivalence test confirms that per-test CLS, aggregated to patch-level verdicts, achieves statistically equivalent accuracy to a trajectory-level classifier ($p = 0.007$ at a $\\pm$2pp margin), while additionally providing per-test diagnostic signals that trajectory-level verifiers discard. These diagnostics are most valuable when they are most needed: the per-test advantage concentrates in instances with multiple fail-to-pass tests ($T \\geq 2$), which constitute 31\\% of SWE-bench Verified instances but account for 55\\% of the accuracy advantage. Furthermore, CLS and CWM exhibit complementary error patterns---CLS errors skew toward missed bugs while CWM errors skew toward false alarms---enabling an oracle ensemble accuracy of 90.63\\%, pointing toward formulation diversity as a verification strategy.\n\nWe also establish that zero-shot LLM-as-judge baselines substantially underperform fine-tuned models (8B zero-shot: 64.40\\%; 32B NF4 zero-shot: 71.69\\%), confirming that task-specific fine-tuning remains essential for execution simulation regardless of formulation.\n\nOur contributions are threefold:\n\\begin{enumerate}\n    \\item We identify a \\textbf{complexity-dependent reformulation advantage}: classification and generation achieve equivalent accuracy on simple function-level code, but classification scales better with model size and to repository-level complexity where generation failure modes dominate (25.59pp gap at 4B scale on SWE-bench Verified). Furthermore, zero-shot LLM-as-judge baselines substantially underperform fine-tuned models (32B NF4: 71.69\\% vs.\\ fine-tuned 4B: 88.43\\%), confirming that task-specific fine-tuning remains essential.\n    \\item We demonstrate that per-test classification provides \\textbf{diagnostic granularity at equivalent accuracy}: per-test CLS matches trajectory-level accuracy (TOST $p = 0.007$) while preserving actionable per-test failure information.\n    \\item We characterize the \\textbf{accuracy-utility frontier}, showing that per-test advantage concentrates in multi-fail-to-pass instances and that CLS/CWM error complementarity (oracle ensemble: 90.63\\%) motivates formulation diversity for verification pipelines.\n\\end{enumerate}\n",
      "numLines": 26,
      "startLine": 1,
      "totalLines": 26
    }
  }
}
```

</details>

---

### Assistant

_source line 29_

三处修改完成：

1. **Para 2 (line 10)**：删除了具体数字 "53.7–67.2%"，改为定性描述 "the majority of CWM predictions become unparseable"
2. **Para 4 (line 14 末尾)**：将数字移至此处，加限定语 "in our controlled 4B experiments (§Method)"，明确这是我们特定实验的观测而非范式的固有缺陷
3. **C1 (line 22 末尾)**：补充了 zero-shot baseline 对比句 "32B NF4: 71.69% vs. fine-tuned 4B: 88.43%"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "066b9dae-ab21-4272-be08-6477f0f4d275",
  "uuid": "30d82058-283d-4297-ac65-d59c57725dc6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AQ49N1YFufACwppqCDgMQQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1676,
      "cache_read_input_tokens": 28314,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1676
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

_source line 30_

三处修改完成：

1. **Para 2 (line 10)**：删除了具体数字 "53.7–67.2%"，改为定性描述 "the majority of CWM predictions become unparseable"
2. **Para 4 (line 14 末尾)**：将数字移至此处，加限定语 "in our controlled 4B experiments (§Method)"，明确这是我们特定实验的观测而非范式的固有缺陷
3. **C1 (line 22 末尾)**：补充了 zero-shot baseline 对比句 "32B NF4: 71.69% vs. fine-tuned 4B: 88.43%"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 65818,
  "duration_api_ms": 66860,
  "num_turns": 10,
  "stop_reason": "end_turn",
  "session_id": "066b9dae-ab21-4272-be08-6477f0f4d275",
  "total_cost_usd": 0.32641475000000003,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 18543,
    "cache_read_input_tokens": 249198,
    "output_tokens": 3385,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 18543,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 189,
        "cache_read_input_tokens": 28314,
        "cache_creation_input_tokens": 1676,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1676
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1172,
      "outputTokens": 14,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001242,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 11,
      "outputTokens": 3385,
      "cacheReadInputTokens": 249198,
      "cacheCreationInputTokens": 18543,
      "webSearchRequests": 0,
      "costUSD": 0.32517275,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "285f9c0c-4005-4e32-9ac4-7be3be545c5d"
}
```

</details>

---
