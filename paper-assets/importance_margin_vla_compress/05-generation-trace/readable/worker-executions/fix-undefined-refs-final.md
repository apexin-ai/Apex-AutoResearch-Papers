# fix undefined refs final

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 55
- **Recorded user turns:** 0
- **Tool calls:** 19
- **Original source:** `logs/workers/worker_fix_undefined_refs_final_20260528T181802.log`
- **Structured JSON:** [`be91a334dabd0532b731.json`](../../sessions/be/be91a334dabd0532b731.json)

## Before a recorded user message

55 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress",
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
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
  "uuid": "acd75fa8-8521-4508-b17d-79741dfedeeb",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/memory/"
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
    "resetsAt": 1780004400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "a0f267e3-b8c3-4f79-9182-376e8e1c1e0f",
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by compiling the paper and finding all undefined references.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "uuid": "8941e320-fdef-4853-9380-ef27a4f37222",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UUtTUarhiYJ62SyeNmYMWy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12836,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12836
      },
      "output_tokens": 9,
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

先编译论文，找出所有 undefined references。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "uuid": "9c1da69a-bb0e-435e-81e4-a77892d5bbd0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UUtTUarhiYJ62SyeNmYMWy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12836,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12836
      },
      "output_tokens": 9,
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

<details open><summary>🔧 Tool call — Bash · `toolu_011aReZAR5AkLPex4ZnAHQW4`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper && latexmk -pdf -interaction=nonstopmode main.tex 2>&1 | tail -10",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "uuid": "ad409910-6b78-477d-b59c-981e59cb90d7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UUtTUarhiYJ62SyeNmYMWy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12836,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12836
      },
      "output_tokens": 9,
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

_source line 7 · 2026-05-28T18:18:18.783Z_

<details><summary>↩ Tool result · `toolu_011aReZAR5AkLPex4ZnAHQW4`</summary>

```text
  ./references.bib
Latexmk: Summary of warnings from last run of *latex:
  Latex failed to resolve 4 reference(s)
Latexmk: ====Undefined refs and citations with line #s in .tex file:
  Reference `sec:openvla_results' on page 4 undefined on input line 64
  Reference `sec:scaling_law' on page 4 undefined on input line 66
  Reference `sec:scaling_law' on page 6 undefined on input line 98
  Reference `tab:taxonomy' on page 6 undefined on input line 101
Latexmk: All targets (main.pdf) are up-to-date
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "uuid": "36299e8c-0ed8-4f16-9b8c-4ebb02d42ab5",
  "tool_use_result": {
    "stdout": "  ./references.bib\nLatexmk: Summary of warnings from last run of *latex:\n  Latex failed to resolve 4 reference(s)\nLatexmk: ====Undefined refs and citations with line #s in .tex file:\n  Reference `sec:openvla_results' on page 4 undefined on input line 64\n  Reference `sec:scaling_law' on page 4 undefined on input line 66\n  Reference `sec:scaling_law' on page 6 undefined on input line 98\n  Reference `tab:taxonomy' on page 6 undefined on input line 101\nLatexmk: All targets (main.pdf) are up-to-date",
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

_source line 8_

4 个 undefined refs：`sec:openvla_results`、`sec:scaling_law`（2处）、`tab:taxonomy`。现在找出引用位置和是否有对应 label。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "uuid": "4c1ecee8-0ef6-43a9-87c0-402447f947a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qz4HeipWTiKJBtQbamk6hx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 354,
      "cache_read_input_tokens": 24681,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 354
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

_source line 9_

<details open><summary>🔧 Tool call — Bash · `toolu_01TgYi8eY5sGHxYyY4nfd6W9`</summary>

```json
{
  "command": "grep -rn 'ref{sec:openvla_results}\\|ref{sec:scaling_law}\\|ref{tab:taxonomy}' *.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "uuid": "e99c9939-6c68-49e6-9686-4a03d43bc06a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qz4HeipWTiKJBtQbamk6hx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 354,
      "cache_read_input_tokens": 24681,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 354
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

_source line 10 · 2026-05-28T18:18:27.658Z_

<details><summary>↩ Tool result · `toolu_01TgYi8eY5sGHxYyY4nfd6W9`</summary>

```text
experimental_setup.tex:7:Seven VLA architectures spanning three vision connector families provide the testbed (Table~\ref{tab:taxonomy}).
method.tex:64:Random selection provides the null hypothesis that all post-connector tokens are interchangeable. If L2 scoring cannot outperform random, the token norm distribution carries no exploitable signal. Random selection also preserves the spatial distribution of the original token set in expectation, making it the natural baseline for spatially uniform architectures. Its primary limitation is sampling variance across episodes, which we control through multi-seed evaluation (Section~\ref{sec:openvla_results}).
method.tex:66:The \emph{importance margin} at ratio $k$ is defined as $\Delta(k) = \text{SR}_{\text{L2}}(k) - \text{SR}_{\text{Random}}(k)$. A positive margin indicates that the norm distribution contains exploitable importance structure. A negative margin indicates that L2 selection is actively harmful, typically because spatial clustering outweighs the benefit of importance ranking. The sign and magnitude of the importance margin vary systematically with both connector CV and $k$ (Section~\ref{sec:scaling_law}).
method.tex:98:CV also predicts the \emph{optimal pruning strategy}, not only the tolerance ceiling. When CV is low ($< 0.15$), L2-norm ranking captures spatial artifacts rather than genuine importance differences, and random selection outperforms L2 by preserving spatial coverage. When CV is high ($> 0.20$), L2-norm ranking exploits real importance differentiation and outperforms random. The importance margin $\Delta(\text{L2} - \text{Random})$ increases monotonically with CV at both $k = 0.5$ and $k = 0.7$ across three closed-loop models ($\pi_{0.5}$, X-VLA, OpenVLA), confirming that CV captures a structural property of the connector rather than an artifact of a particular retention ratio (Section~\ref{sec:scaling_law}).
method.tex:101:Attention entropy, defined as the mean Shannon entropy of the LLM's attention weight distribution over vision tokens, provides a complementary but less discriminative signal. Entropy measures how uniformly the LLM attends across vision tokens: high entropy indicates distributed attention, low entropy indicates selective focus. Three models with qualitatively different pruning behaviors, however, cluster within a narrow entropy band: $\pi_{0.5}$ (0.666), X-VLA (0.614), and OpenVLA (0.661) span only 0.05 in entropy despite spanning 0.055 to 0.215 in CV and exhibiting uniformly critical, threshold-graded, and smooth graded pruning responses respectively. SmolVLA's entropy (0.952) is near-maximal, yet it is the least pruning-tolerant model. The discrepancy arises because entropy reflects the LLM's \emph{reading pattern} (how attention is distributed across tokens), while CV reflects the connector's \emph{writing pattern} (how information is distributed into tokens). The connector's output structure, not the downstream attention allocation, determines pruning robustness. We report entropy values alongside CV in our taxonomy (Table~\ref{tab:taxonomy}) as a mechanistic supplement, but use CV as the primary diagnostic throughout.
results.tex:9:Table~\ref{tab:taxonomy} organizes seven models into four response classes. The taxonomy reveals that effective vision-to-LLM pipeline complexity, not the nominal connector label or model scale, is strongly associated with pruning tolerance. Token importance CV tracks this ordering continuously across an 8$\times$ parameter range (450M to 7B): uniformly critical models cluster at CV $< 0.06$, threshold-graded at $\sim$0.15, smooth graded at $\sim$0.22, and catastrophic cliff at $>$0.3. A pairwise comparison between $\pi_0$ and OpenVLA (both consuming 256 SigLIP-based~\cite{zhai2023siglip} tokens but differing in connector, backbone, and encoder fusion) yields a 63\,pp gap at $k{=}0.1$; this gap is consistent with the monotonic CV-degradation pattern across all seven models (Section~\ref{sec:linear_results}).
results_v2.tex:9:Table~\ref{tab:taxonomy} organizes seven models into four response classes. The taxonomy reveals that effective vision-to-LLM pipeline complexity, not the nominal connector label or model scale, determines pruning tolerance. Token importance CV tracks this ordering continuously across an 8$\times$ parameter range (450M to 7B): uniformly critical models cluster at CV $< 0.06$, threshold-graded at $\sim$0.15, smooth graded at $\sim$0.22, and catastrophic cliff at $>$0.3. A controlled comparison between $\pi_0$ and OpenVLA (both using 256 SigLIP~\cite{zhai2023siglip} tokens, differing only in connector) yields a 63\,pp gap at $k{=}0.1$, isolating the pipeline as causal (Section~\ref{sec:linear_results}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "uuid": "ebd163a8-7b3a-404f-9efa-72a91a2cee63",
  "tool_use_result": {
    "stdout": "experimental_setup.tex:7:Seven VLA architectures spanning three vision connector families provide the testbed (Table~\\ref{tab:taxonomy}).\nmethod.tex:64:Random selection provides the null hypothesis that all post-connector tokens are interchangeable. If L2 scoring cannot outperform random, the token norm distribution carries no exploitable signal. Random selection also preserves the spatial distribution of the original token set in expectation, making it the natural baseline for spatially uniform architectures. Its primary limitation is sampling variance across episodes, which we control through multi-seed evaluation (Section~\\ref{sec:openvla_results}).\nmethod.tex:66:The \\emph{importance margin} at ratio $k$ is defined as $\\Delta(k) = \\text{SR}_{\\text{L2}}(k) - \\text{SR}_{\\text{Random}}(k)$. A positive margin indicates that the norm distribution contains exploitable importance structure. A negative margin indicates that L2 selection is actively harmful, typically because spatial clustering outweighs the benefit of importance ranking. The sign and magnitude of the importance margin vary systematically with both connector CV and $k$ (Section~\\ref{sec:scaling_law}).\nmethod.tex:98:CV also predicts the \\emph{optimal pruning strategy}, not only the tolerance ceiling. When CV is low ($< 0.15$), L2-norm ranking captures spatial artifacts rather than genuine importance differences, and random selection outperforms L2 by preserving spatial coverage. When CV is high ($> 0.20$), L2-norm ranking exploits real importance differentiation and outperforms random. The importance margin $\\Delta(\\text{L2} - \\text{Random})$ increases monotonically with CV at both $k = 0.5$ and $k = 0.7$ across three closed-loop models ($\\pi_{0.5}$, X-VLA, OpenVLA), confirming that CV captures a structural property of the connector rather than an artifact of a particular retention ratio (Section~\\ref{sec:scaling_law}).\nmethod.tex:101:Attention entropy, defined as the mean Shannon entropy of the LLM's attention weight distribution over vision tokens, provides a complementary but less discriminative signal. Entropy measures how uniformly the LLM attends across vision tokens: high entropy indicates distributed attention, low entropy indicates selective focus. Three models with qualitatively different pruning behaviors, however, cluster within a narrow entropy band: $\\pi_{0.5}$ (0.666), X-VLA (0.614), and OpenVLA (0.661) span only 0.05 in entropy despite spanning 0.055 to 0.215 in CV and exhibiting uniformly critical, threshold-graded, and smooth graded pruning responses respectively. SmolVLA's entropy (0.952) is near-maximal, yet it is the least pruning-tolerant model. The discrepancy arises because entropy reflects the LLM's \\emph{reading pattern} (how attention is distributed across tokens), while CV reflects the connector's \\emph{writing pattern} (how information is distributed into tokens). The connector's output structure, not the downstream attention allocation, determines pruning robustness. We report entropy values alongside CV in our taxonomy (Table~\\ref{tab:taxonomy}) as a mechanistic supplement, but use CV as the primary diagnostic throughout.\nresults.tex:9:Table~\\ref{tab:taxonomy} organizes seven models into four response classes. The taxonomy reveals that effective vision-to-LLM pipeline complexity, not the nominal connector label or model scale, is strongly associated with pruning tolerance. Token importance CV tracks this ordering continuously across an 8$\\times$ parameter range (450M to 7B): uniformly critical models cluster at CV $< 0.06$, threshold-graded at $\\sim$0.15, smooth graded at $\\sim$0.22, and catastrophic cliff at $>$0.3. A pairwise comparison between $\\pi_0$ and OpenVLA (both consuming 256 SigLIP-based~\\cite{zhai2023siglip} tokens but differing in connector, backbone, and encoder fusion) yields a 63\\,pp gap at $k{=}0.1$; this gap is consistent with the monotonic CV-degradation pattern across all seven models (Section~\\ref{sec:linear_results}).\nresults_v2.tex:9:Table~\\ref{tab:taxonomy} organizes seven models into four response classes. The taxonomy reveals that effective vision-to-LLM pipeline complexity, not the nominal connector label or model scale, determines pruning tolerance. Token importance CV tracks this ordering continuously across an 8$\\times$ parameter range (450M to 7B): uniformly critical models cluster at CV $< 0.06$, threshold-graded at $\\sim$0.15, smooth graded at $\\sim$0.22, and catastrophic cliff at $>$0.3. A controlled comparison between $\\pi_0$ and OpenVLA (both using 256 SigLIP~\\cite{zhai2023siglip} tokens, differing only in connector) yields a 63\\,pp gap at $k{=}0.1$, isolating the pipeline as causal (Section~\\ref{sec:linear_results}).",
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

_source line 11_

<details open><summary>🔧 Tool call — Bash · `toolu_01RRiBmE2wn5MrMTZAwyAWZT`</summary>

```json
{
  "command": "grep -rn 'label{sec:openvla_results}\\|label{sec:scaling_law}\\|label{tab:taxonomy}' *.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "uuid": "f434f0b2-56cc-4c99-a382-68bc812a6e28",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qz4HeipWTiKJBtQbamk6hx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 354,
      "cache_read_input_tokens": 24681,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 354
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

_source line 12 · 2026-05-28T18:18:28.602Z_

<details><summary>↩ Tool result · `toolu_01RRiBmE2wn5MrMTZAwyAWZT`</summary>

```text
results.tex:17:\label{tab:taxonomy}
results.tex:41:\label{sec:openvla_results}
results.tex:100:\label{sec:scaling_law}
results_v2.tex:17:\label{tab:taxonomy}
results_v2.tex:41:\label{sec:openvla_results}
results_v2.tex:100:\label{sec:scaling_law}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "uuid": "de7b3bc6-f4d2-4a4b-9b00-24798a956df6",
  "tool_use_result": {
    "stdout": "results.tex:17:\\label{tab:taxonomy}\nresults.tex:41:\\label{sec:openvla_results}\nresults.tex:100:\\label{sec:scaling_law}\nresults_v2.tex:17:\\label{tab:taxonomy}\nresults_v2.tex:41:\\label{sec:openvla_results}\nresults_v2.tex:100:\\label{sec:scaling_law}",
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

_source line 13_

<details open><summary>🔧 Tool call — Bash · `toolu_01PFcjJpSsRzBUE9Do9m2G5S`</summary>

```json
{
  "command": "ls *.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "uuid": "59cf5d3a-dc97-4ecf-be6a-0a54d89c7762",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qz4HeipWTiKJBtQbamk6hx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 354,
      "cache_read_input_tokens": 24681,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 354
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

_source line 14 · 2026-05-28T18:18:28.921Z_

<details><summary>↩ Tool result · `toolu_01PFcjJpSsRzBUE9Do9m2G5S`</summary>

```text
abstract.tex
analysis.tex
appendix.tex
background.tex
conclusion.tex
discussion.tex
experimental_setup.tex
experiments.tex
experiments_deprecated.tex
introduction.tex
limitations.tex
main.tex
method.tex
related_work.tex
results.tex
results_v2.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "uuid": "15034727-f6ba-4b03-af54-da2601c23c9d",
  "tool_use_result": {
    "stdout": "abstract.tex\nanalysis.tex\nappendix.tex\nbackground.tex\nconclusion.tex\ndiscussion.tex\nexperimental_setup.tex\nexperiments.tex\nexperiments_deprecated.tex\nintroduction.tex\nlimitations.tex\nmain.tex\nmethod.tex\nrelated_work.tex\nresults.tex\nresults_v2.tex",
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

_source line 15_

Labels 存在于 `results.tex` 和 `results_v2.tex` 中。问题是 `main.tex` 可能没有 `\input{results}`。检查 main.tex 的 input 结构。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "uuid": "f81302df-9314-4940-9c8f-063fba0d84f9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NC7NNih7yr7hS7PLhtaMeP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1718,
      "cache_read_input_tokens": 25035,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1718
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

<details open><summary>🔧 Tool call — Bash · `toolu_01FvBXCohbaxo7JAg6UB3gtc`</summary>

```json
{
  "command": "grep -n 'input{' /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "uuid": "5b0a4b9e-a8f6-4fef-9717-42b89b99b9a1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NC7NNih7yr7hS7PLhtaMeP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1718,
      "cache_read_input_tokens": 25035,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1718
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

_source line 17 · 2026-05-28T18:18:33.875Z_

<details><summary>↩ Tool result · `toolu_01FvBXCohbaxo7JAg6UB3gtc`</summary>

```text
26:\input{abstract}
30:\input{introduction}
32:\input{related_work}
34:\input{method}
36:\input{experiments}
38:\input{conclusion}
40:\input{limitations}
44:\input{appendix}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "uuid": "4ffec8a1-d56f-44ea-9bb7-d5c6217ab479",
  "tool_use_result": {
    "stdout": "26:\\input{abstract}\n30:\\input{introduction}\n32:\\input{related_work}\n34:\\input{method}\n36:\\input{experiments}\n38:\\input{conclusion}\n40:\\input{limitations}\n44:\\input{appendix}",
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

_source line 18_

`main.tex` 包含的是 `experiments.tex`，不是 `results.tex`。Labels 在 `results.tex` 中定义但没被编译。检查 `experiments.tex` 中是否有对应的 section 可以添加 label。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "uuid": "8822c345-ca59-4a8c-9617-760ed8c8a785",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AAKURpTAzKe6FuNSKmSkU5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 230,
      "cache_read_input_tokens": 26753,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 230
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

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_01PxAidzwA4R8DwYSDZUSKcM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "uuid": "f5ea348d-a52c-449e-be9b-84d1261f8728",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AAKURpTAzKe6FuNSKmSkU5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 230,
      "cache_read_input_tokens": 26753,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 230
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

_source line 20 · 2026-05-28T18:18:40.698Z_

<details><summary>↩ Tool result · `toolu_01PxAidzwA4R8DwYSDZUSKcM`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:exp_setup}
6	
7	\paragraph{Benchmark.} We evaluate on LIBERO~\cite{liu2023libero}, a simulated tabletop manipulation benchmark comprising four task suites of increasing complexity. \textbf{Object} (10 tasks) requires discriminating among visually similar objects at identical locations. \textbf{Spatial} (10 tasks) requires understanding relative spatial layouts (e.g., ``pick the bowl on the left of the plate''), where critical information is distributed across the visual field. \textbf{Goal} (10 tasks) involves goal-conditioned manipulation with varied target configurations. \textbf{Long} (10 tasks) chains 3--5 manipulation primitives into multi-step sequences, where token loss at any step can cascade through the remainder of the trajectory. Each task provides 50 demonstration episodes for fine-tuning and 50 evaluation episodes, yielding 500 episodes per suite.
8	
9	\paragraph{Models.} Four VLAs are evaluated in closed-loop control: $\pi_{0.5}$~\cite{black2025pi05} (4B, linear projection, 768 tokens, CV$\,{=}\,$0.055), X-VLA~\cite{zheng2025xvla} (0.9B, linear + 12-layer BART encoder, 50 tokens, CV$\,{=}\,$0.151), OpenVLA~\cite{kim2024openvla} (7B, 3-layer MLP, 256 tokens, CV$\,{=}\,$0.215), and SmolVLA~\cite{shukor2025smolvla} (450M, pixel-shuffle $4{\times}4$, 128 tokens, CV$\,{=}\,$0.314). Two additional models ($\pi_{0}$~\cite{black2024pi0}, OFT~\cite{kim2025openoft}) contribute to the CV diagnostic via offline metrics only. Table~\ref{tab:model_properties} summarizes all six architectures.
10	
11	\paragraph{Protocol.} We prune at $k \in \{0.3, 0.5, 0.7, 0.75, 0.85, 0.9, 0.95\}$ and report mean success rate (SR) over 500 episodes in strict evaluation mode (episodes run to completion regardless of intermediate failures). Multi-seed results ($\pi_{0.5}$ Long: five seeds, 42--46; VTR: three seeds, 42--44) report mean $\pm$ standard deviation with per-seed breakdowns in the appendix. Single-seed results report Wilson 95\% confidence intervals.
12	
13	\subsection{Two-Axis Framework Overview}
14	\label{sec:two_axis}
15	
16	\begin{figure}[t]
17	\centering
18	\includegraphics[width=0.75\linewidth]{figures/paper/fig_pruning_overview.pdf}
19	\caption{Pruning degradation on LIBERO-Object (L2 norm scoring). $\pi_{0.5}$ maintains ${\geq}$98\% through $k{=}0.85$, OpenVLA degrades linearly, X-VLA cliffs at $k{=}0.7$, SmolVLA collapses to 0\% at $k{=}0.95$.}
20	\label{fig:pruning_overview}
21	\end{figure}
22	
23	Three qualitatively distinct response patterns emerge across the connector spectrum (Table~\ref{tab:main_results}; Figure~\ref{fig:pruning_overview}); a fourth (OpenVLA, MLP connector) is detailed in Appendix Table~\ref{tab:full_results}.
24	
25	\textbf{$\pi_{0.5}$ (linear, CV$\,{=}\,$0.055).} Low-CV models are \emph{uniformly critical}: which tokens are removed matters more than how many. On Object, L2 maintains ${\geq}$98.0\% through $k{=}0.85$ (Appendix Table~\ref{tab:full_results}), while random at $k{=}0.9$ collapses to 9.0\%, an 89\,pp method gap from identical removal fractions.
26	
27	\textbf{X-VLA (BART encoder, CV$\,{=}\,$0.151).} Method-insensitive but task-sensitive: at $k{=}0.9$ on Object, L2 and random differ by 0.4\,pp, yet the same model drops 27.4\,pp on Goal. Removing 3 of 50 tokens ($k{=}0.95$) halves Long SR regardless of method.
28	
29	\textbf{OpenVLA (MLP, CV$\,{=}\,$0.215).} OpenVLA exhibits scoring crossover: L2 outperforms random on Object but the ranking inverts on Spatial and Goal at $k{=}0.9$ (Appendix Table~\ref{tab:full_results}; Section~\ref{sec:analysis}).
30	
31	\textbf{SmolVLA (pixel-shuffle, CV$\,{=}\,$0.314).} Removing 6 of 128 tokens ($k{=}0.95$) collapses SR to ${\leq}$6.6\% across all suites and methods, a catastrophic cliff detailed in Section~\ref{sec:pixel_shuffle}.
32	
33	\begin{table*}[t]
34	\centering
35	\small
36	\caption{Closed-loop success rates (\%) on LIBERO under L2 norm (L2) and random (R) token pruning. SmolVLA collapses to ${\leq}$6.6\% across all conditions. $\pi_{0.5}$ Long: five-seed mean ($n{=}5$; per-seed in Appendix Table~\ref{tab:pi05_long_multiseed}). Full results including OpenVLA in Appendix Table~\ref{tab:full_results}.}
37	\label{tab:main_results}
38	\begin{tabular}{llcccc}
39	\toprule
40	Model & Suite & Baseline & $k{=}0.95$ (L2 / R) & $k{=}0.9$ (L2 / R) & $k{=}0.5$ (L2 / R) \\
41	\midrule
42	\multirow{4}{*}{$\pi_{0.5}$}
43	& Object  & \textbf{98.2} & 98.2 / 74.0 & \textbf{98.2} / 9.0 & 33.4 / 69.4 \\
44	& Spatial & \textbf{97.2} & \textbf{97.8} / 76.4 & 95.0 / 54.6 & 55.6 / 71.6 \\
45	& Goal    & \textbf{96.4} & 89.4 / 84.0 & 90.6 / 62.2 & 59.2 / 73.6 \\
46	& Long    & \textbf{91.6} & 86.8 / 61.2 & 80.4 / 33.6 & 51.7 / 50.4 \\
47	\midrule
48	\multirow{4}{*}{X-VLA}
49	& Object  & \textbf{99.2} & 99.0 / 98.8 & 97.6 / 97.8 & 43.4 / 70.6 \\
50	& Spatial & \textbf{93.0} & 71.6 / 70.2 & 78.8 / 77.8 & 58.8 / 71.4 \\
51	& Goal    & \textbf{98.4} & 53.8 / 54.0 & 70.2 / 70.6 & 59.0 / 67.2 \\
52	& Long    & \textbf{94.0} & 47.0 / 48.2 & 27.5 / 29.6 & 45.0 / 61.6 \\
53	\midrule
54	\multirow{4}{*}{SmolVLA}
55	& Object  & \textbf{59.2} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\
56	& Spatial & \textbf{44.6} & 6.6 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 \\
57	& Goal    & \textbf{60.8} & 3.4 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 \\
58	& Long    & \textbf{36.6} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\
59	\bottomrule
60	\end{tabular}
61	\end{table*}
62	
63	\subsection{Pixel-Shuffle Entanglement}
64	\label{sec:pixel_shuffle}
65	
66	\begin{figure*}[t]
67	\centering
68	\begin{subfigure}[t]{0.495\textwidth}
69	\centering
70	\includegraphics[width=\linewidth]{figures/paper/fig_pixel_shuffle.pdf}
71	\caption{}\label{fig:pixel_shuffle}
72	\end{subfigure}
73	\hfill
74	\begin{subfigure}[t]{0.495\textwidth}
75	\centering
76	\includegraphics[width=\linewidth]{figures/paper/fig_method_gap.pdf}
77	\caption{}\label{fig:method_gap}
78	\end{subfigure}
79	\caption{Token entanglement and scoring sensitivity. \textbf{(a)}~Pixel-shuffle $4{\times}4$ folding: each 16-patch block is channel-concatenated into one token; removing any token eliminates a non-overlapping receptive field. \textbf{(b)}~Method gap $|\text{SR(L2)} - \text{SR(Random)}|$ at $k{=}0.95$: $\pi_{0.5}$'s Object gap (24.2\,pp) exceeds X-VLA's maximum (1.4\,pp) by $17{\times}$ (single seed except $\pi_{0.5}$ Long, $n{=}5$).}
80	\label{fig:entanglement_scoring}
81	\end{figure*}
82	
83	SmolVLA's pixel-shuffle $4{\times}4$ folding concatenates 16 patches per token (Figure~\ref{fig:pixel_shuffle}), creating non-overlapping receptive fields that collapse SR to ${\leq}$6.6\% at $k{=}0.95$ across all suites and methods (verified on two checkpoints). No scoring function can identify dispensable tokens because all carry spatially entangled information.
84	
85	\subsection{Position Disruption vs.\ Information Loss}
86	\label{sec:zeromask}
87	
88	$\pi_{0.5}$'s random pruning at $k{=}0.9$ collapses to 9.0\% on Object despite removing only 10\% of tokens. We compare hard pruning (removes tokens, re-indexes positions) with zero-masking (zeros embeddings, preserves positions): zero-masking preserves 98.0\% SR while hard pruning collapses to 9.0\%. The 89\,pp gap is entirely attributable to position disruption: $\pi_{0.5}$'s linear connector tolerates complete signal destruction but not index shifts.
89	
90	\subsection{Scoring Method Sensitivity and CV Diagnostic}
91	\label{sec:cv_sensitivity}
92	
93	CV predicts where scoring method choice becomes critical (Figure~\ref{fig:method_gap}). $\pi_{0.5}$'s Object gap at $k{=}0.95$ reaches 24.2\,pp, exceeding X-VLA's maximum (1.4\,pp) by $17{\times}$. At $k{=}0.5$, the importance margin on Object is $\Delta{=}{-}36.0$\,pp ($\pi_{0.5}$) and ${-}27.2$\,pp (X-VLA): L2 scoring clusters spatially correlated tokens at the cost of spatial diversity.
94	
95	\textbf{Architecture-dependent scoring.} The optimal scoring method depends on the connector (Table~\ref{tab:attention_pruning}). On X-VLA at $k{=}0.5$, attention recovers ${\geq}$92.8\% while L2 falls 8--27\,pp below random; on $\pi_{0.5}$, attention is catastrophically harmful on Object ($-$30.4\,pp). On Long, attention cliffs $-$26.5\,pp from $k{=}0.95$ to $k{=}0.85$, then plateaus (Figure~\ref{fig:cliff_highlight}).
96	
97	\textbf{Cliff vs.\ graded degradation.} The divergent response patterns in the cliff zone ($k \in [0.85, 0.95]$) reflect a statistical distinction between the two scoring methods. Random removal samples a different token subset at each control step; in this interval, the probability of destroying at least one critical token combination transitions from low to near-certain, which produces a binary collapse. L2 scoring deterministically retains the same high-norm subset at every step. This determinism explains the 93\,pp gap at $k{=}0.85$ on Object (L2 98.0\% vs.\ random 5.0\%; Appendix Table~\ref{tab:full_results}).
98	
99	\textbf{Inverted-U importance margin.} The importance margin $\Delta$ on $\pi_{0.5}$ Long follows an inverted-U profile across retention ratios (Figure~\ref{fig:cliff_highlight}; Appendix Figure~\ref{fig:margin_profile}). The margin peaks at $k{=}0.9$ ($\Delta{=}+$46.9\,pp: L2 80.4\% vs.\ random 33.6\%), the retention ratio where importance-aware selection provides maximum value. Above this peak ($k{=}0.95$, $\Delta{=}+$25.6\,pp), both methods retain enough tokens for adequate performance and the advantage of targeted selection diminishes. Below it ($k{=}0.5$, $\Delta{\approx}+$1.3\,pp), both methods lose enough information that their strategies become equally inadequate. Near $k{\approx}0.7$, the ranking inverts: random surpasses L2 (64.6\% vs.\ 63.2\%; Appendix Table~\ref{tab:full_results}) because L2 concentrates retained tokens in a single high-activation region at the cost of the spatial coverage that multi-step tasks require. The V-shaped random recovery at lower $k$ arises from position aliasing under scattered removal (Section~\ref{sec:analysis}).
100	
101	\begin{figure}[t]
102	\centering
103	\includegraphics[width=0.75\linewidth]{figures/paper/fig_cliff_highlight.pdf}
104	\caption{Scoring method determines cliff behavior on $\pi_{0.5}$ Long (five-seed mean $\pm$ s.d.\ shaded; $n{=}5$). L2 degrades monotonically; attention exhibits a sharp cliff from $k{=}0.95$ to $k{=}0.85$ ($-$26.5\,pp), then plateaus; random exhibits a V-shape with collapse at $k{=}0.9$ (46.9\,pp gap vs.\ L2) and recovery at $k{\leq}0.7$.}
105	\label{fig:cliff_highlight}
106	\end{figure}
107	
108	\textbf{Importance margin gradient.} L2's advantage shrinks with task complexity on $\pi_{0.5}$ at $k{=}0.85$ (Appendix Table~\ref{tab:full_results}): Object $\Delta{=}+$93\,pp $>$ Goal $+$35.2\,pp $>$ Long $+$33.2\,pp. Multi-step tasks distribute critical information across tokens with more heterogeneous norm profiles, which reduces the effectiveness of magnitude-based selection.
109	
110	\subsection{VTR Recovery}
111	\label{sec:vtr_recovery}
112	
113	VTR uses $M$ learned queries cross-attending over all 128 source tokens (${\sim}$22M parameters, ${\sim}$5\% of SmolVLA). At 75\% compression, VTR achieves 60.1 $\pm$ 1.3\% SR ($M{=}32$, 3 seeds; Table~\ref{tab:vtr_main}), exceeding the unpruned LoRA baseline (44.8\%) by 15.3\,pp. An extended training control (100K steps, identical recipe, no compressor) reaches only 45.0\% ($p > 0.9$ vs.\ baseline; Appendix~\ref{app:smart_compress_details}), which rules out additional optimization as the source of improvement. The re-encoding module provides a beneficial inductive bias: by restructuring entangled pixel-shuffle tokens, VTR produces a representation that is both more compact and more effective than the original. A parameter-matched MLP adapter achieves 63.4 $\pm$ 2.6\% ($p{=}0.15$), which indicates the benefit stems from re-encoding itself, not the cross-attention mechanism. Cross-suite generalization confirms the pattern: Spatial 53.2\%, Goal 56.4\%, both recovered from 0.0\% under hard pruning.
114	
115	\begin{table}[t]
116	\centering
117	\small
118	\caption{VTR re-encoding on SmolVLA (LIBERO-Object). Hard pruning collapses all configurations to 0\%; VTR achieves ${\geq}$57\% at up to 87.5\% compression, exceeding the unpruned baseline. Baseline (44.8\%) is our LoRA reproduction with smaller batch size; the official SmolVLA checkpoint achieves 59.2\% (Table~\ref{tab:main_results}). See Appendix~\ref{app:smart_compress_details} for training details.}
119	\label{tab:vtr_main}
120	\begin{tabular}{lccr}
121	\toprule
122	Configuration & $M$ & Compress.\ & SR (\%) \\
123	\midrule
124	\textit{Baseline (unpruned)} & 128 & 0\% & 44.8 \\
125	\textit{Hard pruning (any)} & -- & 5--50\% & 0.0 \\
126	\midrule
127	Cross-attn VTR & 32 & 75\% & 60.1 $\pm$ 1.3 \\
128	Cross-attn VTR & 16 & 87.5\% & 56.9 $\pm$ 1.3 \\
129	MLP adapter & 32 & 75\% & 63.4 $\pm$ 2.6 \\
130	\bottomrule
131	\end{tabular}
132	\end{table}
133	
134	\textbf{Efficiency.}\label{sec:efficiency} For $\pi_{0.5}$, $k{=}0.9$ cuts attention FLOPs by ${\sim}$16\% while preserving full SR; VTR at $M{=}16$ achieves 87.5\% compression with ${\leq}$1.1\,pp below passthrough.
135	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "uuid": "6b5cd794-3db7-4237-a10e-d634aa23114c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:exp_setup}\n\n\\paragraph{Benchmark.} We evaluate on LIBERO~\\cite{liu2023libero}, a simulated tabletop manipulation benchmark comprising four task suites of increasing complexity. \\textbf{Object} (10 tasks) requires discriminating among visually similar objects at identical locations. \\textbf{Spatial} (10 tasks) requires understanding relative spatial layouts (e.g., ``pick the bowl on the left of the plate''), where critical information is distributed across the visual field. \\textbf{Goal} (10 tasks) involves goal-conditioned manipulation with varied target configurations. \\textbf{Long} (10 tasks) chains 3--5 manipulation primitives into multi-step sequences, where token loss at any step can cascade through the remainder of the trajectory. Each task provides 50 demonstration episodes for fine-tuning and 50 evaluation episodes, yielding 500 episodes per suite.\n\n\\paragraph{Models.} Four VLAs are evaluated in closed-loop control: $\\pi_{0.5}$~\\cite{black2025pi05} (4B, linear projection, 768 tokens, CV$\\,{=}\\,$0.055), X-VLA~\\cite{zheng2025xvla} (0.9B, linear + 12-layer BART encoder, 50 tokens, CV$\\,{=}\\,$0.151), OpenVLA~\\cite{kim2024openvla} (7B, 3-layer MLP, 256 tokens, CV$\\,{=}\\,$0.215), and SmolVLA~\\cite{shukor2025smolvla} (450M, pixel-shuffle $4{\\times}4$, 128 tokens, CV$\\,{=}\\,$0.314). Two additional models ($\\pi_{0}$~\\cite{black2024pi0}, OFT~\\cite{kim2025openoft}) contribute to the CV diagnostic via offline metrics only. Table~\\ref{tab:model_properties} summarizes all six architectures.\n\n\\paragraph{Protocol.} We prune at $k \\in \\{0.3, 0.5, 0.7, 0.75, 0.85, 0.9, 0.95\\}$ and report mean success rate (SR) over 500 episodes in strict evaluation mode (episodes run to completion regardless of intermediate failures). Multi-seed results ($\\pi_{0.5}$ Long: five seeds, 42--46; VTR: three seeds, 42--44) report mean $\\pm$ standard deviation with per-seed breakdowns in the appendix. Single-seed results report Wilson 95\\% confidence intervals.\n\n\\subsection{Two-Axis Framework Overview}\n\\label{sec:two_axis}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\linewidth]{figures/paper/fig_pruning_overview.pdf}\n\\caption{Pruning degradation on LIBERO-Object (L2 norm scoring). $\\pi_{0.5}$ maintains ${\\geq}$98\\% through $k{=}0.85$, OpenVLA degrades linearly, X-VLA cliffs at $k{=}0.7$, SmolVLA collapses to 0\\% at $k{=}0.95$.}\n\\label{fig:pruning_overview}\n\\end{figure}\n\nThree qualitatively distinct response patterns emerge across the connector spectrum (Table~\\ref{tab:main_results}; Figure~\\ref{fig:pruning_overview}); a fourth (OpenVLA, MLP connector) is detailed in Appendix Table~\\ref{tab:full_results}.\n\n\\textbf{$\\pi_{0.5}$ (linear, CV$\\,{=}\\,$0.055).} Low-CV models are \\emph{uniformly critical}: which tokens are removed matters more than how many. On Object, L2 maintains ${\\geq}$98.0\\% through $k{=}0.85$ (Appendix Table~\\ref{tab:full_results}), while random at $k{=}0.9$ collapses to 9.0\\%, an 89\\,pp method gap from identical removal fractions.\n\n\\textbf{X-VLA (BART encoder, CV$\\,{=}\\,$0.151).} Method-insensitive but task-sensitive: at $k{=}0.9$ on Object, L2 and random differ by 0.4\\,pp, yet the same model drops 27.4\\,pp on Goal. Removing 3 of 50 tokens ($k{=}0.95$) halves Long SR regardless of method.\n\n\\textbf{OpenVLA (MLP, CV$\\,{=}\\,$0.215).} OpenVLA exhibits scoring crossover: L2 outperforms random on Object but the ranking inverts on Spatial and Goal at $k{=}0.9$ (Appendix Table~\\ref{tab:full_results}; Section~\\ref{sec:analysis}).\n\n\\textbf{SmolVLA (pixel-shuffle, CV$\\,{=}\\,$0.314).} Removing 6 of 128 tokens ($k{=}0.95$) collapses SR to ${\\leq}$6.6\\% across all suites and methods, a catastrophic cliff detailed in Section~\\ref{sec:pixel_shuffle}.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Closed-loop success rates (\\%) on LIBERO under L2 norm (L2) and random (R) token pruning. SmolVLA collapses to ${\\leq}$6.6\\% across all conditions. $\\pi_{0.5}$ Long: five-seed mean ($n{=}5$; per-seed in Appendix Table~\\ref{tab:pi05_long_multiseed}). Full results including OpenVLA in Appendix Table~\\ref{tab:full_results}.}\n\\label{tab:main_results}\n\\begin{tabular}{llcccc}\n\\toprule\nModel & Suite & Baseline & $k{=}0.95$ (L2 / R) & $k{=}0.9$ (L2 / R) & $k{=}0.5$ (L2 / R) \\\\\n\\midrule\n\\multirow{4}{*}{$\\pi_{0.5}$}\n& Object  & \\textbf{98.2} & 98.2 / 74.0 & \\textbf{98.2} / 9.0 & 33.4 / 69.4 \\\\\n& Spatial & \\textbf{97.2} & \\textbf{97.8} / 76.4 & 95.0 / 54.6 & 55.6 / 71.6 \\\\\n& Goal    & \\textbf{96.4} & 89.4 / 84.0 & 90.6 / 62.2 & 59.2 / 73.6 \\\\\n& Long    & \\textbf{91.6} & 86.8 / 61.2 & 80.4 / 33.6 & 51.7 / 50.4 \\\\\n\\midrule\n\\multirow{4}{*}{X-VLA}\n& Object  & \\textbf{99.2} & 99.0 / 98.8 & 97.6 / 97.8 & 43.4 / 70.6 \\\\\n& Spatial & \\textbf{93.0} & 71.6 / 70.2 & 78.8 / 77.8 & 58.8 / 71.4 \\\\\n& Goal    & \\textbf{98.4} & 53.8 / 54.0 & 70.2 / 70.6 & 59.0 / 67.2 \\\\\n& Long    & \\textbf{94.0} & 47.0 / 48.2 & 27.5 / 29.6 & 45.0 / 61.6 \\\\\n\\midrule\n\\multirow{4}{*}{SmolVLA}\n& Object  & \\textbf{59.2} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Spatial & \\textbf{44.6} & 6.6 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Goal    & \\textbf{60.8} & 3.4 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Long    & \\textbf{36.6} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\subsection{Pixel-Shuffle Entanglement}\n\\label{sec:pixel_shuffle}\n\n\\begin{figure*}[t]\n\\centering\n\\begin{subfigure}[t]{0.495\\textwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_pixel_shuffle.pdf}\n\\caption{}\\label{fig:pixel_shuffle}\n\\end{subfigure}\n\\hfill\n\\begin{subfigure}[t]{0.495\\textwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_method_gap.pdf}\n\\caption{}\\label{fig:method_gap}\n\\end{subfigure}\n\\caption{Token entanglement and scoring sensitivity. \\textbf{(a)}~Pixel-shuffle $4{\\times}4$ folding: each 16-patch block is channel-concatenated into one token; removing any token eliminates a non-overlapping receptive field. \\textbf{(b)}~Method gap $|\\text{SR(L2)} - \\text{SR(Random)}|$ at $k{=}0.95$: $\\pi_{0.5}$'s Object gap (24.2\\,pp) exceeds X-VLA's maximum (1.4\\,pp) by $17{\\times}$ (single seed except $\\pi_{0.5}$ Long, $n{=}5$).}\n\\label{fig:entanglement_scoring}\n\\end{figure*}\n\nSmolVLA's pixel-shuffle $4{\\times}4$ folding concatenates 16 patches per token (Figure~\\ref{fig:pixel_shuffle}), creating non-overlapping receptive fields that collapse SR to ${\\leq}$6.6\\% at $k{=}0.95$ across all suites and methods (verified on two checkpoints). No scoring function can identify dispensable tokens because all carry spatially entangled information.\n\n\\subsection{Position Disruption vs.\\ Information Loss}\n\\label{sec:zeromask}\n\n$\\pi_{0.5}$'s random pruning at $k{=}0.9$ collapses to 9.0\\% on Object despite removing only 10\\% of tokens. We compare hard pruning (removes tokens, re-indexes positions) with zero-masking (zeros embeddings, preserves positions): zero-masking preserves 98.0\\% SR while hard pruning collapses to 9.0\\%. The 89\\,pp gap is entirely attributable to position disruption: $\\pi_{0.5}$'s linear connector tolerates complete signal destruction but not index shifts.\n\n\\subsection{Scoring Method Sensitivity and CV Diagnostic}\n\\label{sec:cv_sensitivity}\n\nCV predicts where scoring method choice becomes critical (Figure~\\ref{fig:method_gap}). $\\pi_{0.5}$'s Object gap at $k{=}0.95$ reaches 24.2\\,pp, exceeding X-VLA's maximum (1.4\\,pp) by $17{\\times}$. At $k{=}0.5$, the importance margin on Object is $\\Delta{=}{-}36.0$\\,pp ($\\pi_{0.5}$) and ${-}27.2$\\,pp (X-VLA): L2 scoring clusters spatially correlated tokens at the cost of spatial diversity.\n\n\\textbf{Architecture-dependent scoring.} The optimal scoring method depends on the connector (Table~\\ref{tab:attention_pruning}). On X-VLA at $k{=}0.5$, attention recovers ${\\geq}$92.8\\% while L2 falls 8--27\\,pp below random; on $\\pi_{0.5}$, attention is catastrophically harmful on Object ($-$30.4\\,pp). On Long, attention cliffs $-$26.5\\,pp from $k{=}0.95$ to $k{=}0.85$, then plateaus (Figure~\\ref{fig:cliff_highlight}).\n\n\\textbf{Cliff vs.\\ graded degradation.} The divergent response patterns in the cliff zone ($k \\in [0.85, 0.95]$) reflect a statistical distinction between the two scoring methods. Random removal samples a different token subset at each control step; in this interval, the probability of destroying at least one critical token combination transitions from low to near-certain, which produces a binary collapse. L2 scoring deterministically retains the same high-norm subset at every step. This determinism explains the 93\\,pp gap at $k{=}0.85$ on Object (L2 98.0\\% vs.\\ random 5.0\\%; Appendix Table~\\ref{tab:full_results}).\n\n\\textbf{Inverted-U importance margin.} The importance margin $\\Delta$ on $\\pi_{0.5}$ Long follows an inverted-U profile across retention ratios (Figure~\\ref{fig:cliff_highlight}; Appendix Figure~\\ref{fig:margin_profile}). The margin peaks at $k{=}0.9$ ($\\Delta{=}+$46.9\\,pp: L2 80.4\\% vs.\\ random 33.6\\%), the retention ratio where importance-aware selection provides maximum value. Above this peak ($k{=}0.95$, $\\Delta{=}+$25.6\\,pp), both methods retain enough tokens for adequate performance and the advantage of targeted selection diminishes. Below it ($k{=}0.5$, $\\Delta{\\approx}+$1.3\\,pp), both methods lose enough information that their strategies become equally inadequate. Near $k{\\approx}0.7$, the ranking inverts: random surpasses L2 (64.6\\% vs.\\ 63.2\\%; Appendix Table~\\ref{tab:full_results}) because L2 concentrates retained tokens in a single high-activation region at the cost of the spatial coverage that multi-step tasks require. The V-shaped random recovery at lower $k$ arises from position aliasing under scattered removal (Section~\\ref{sec:analysis}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\linewidth]{figures/paper/fig_cliff_highlight.pdf}\n\\caption{Scoring method determines cliff behavior on $\\pi_{0.5}$ Long (five-seed mean $\\pm$ s.d.\\ shaded; $n{=}5$). L2 degrades monotonically; attention exhibits a sharp cliff from $k{=}0.95$ to $k{=}0.85$ ($-$26.5\\,pp), then plateaus; random exhibits a V-shape with collapse at $k{=}0.9$ (46.9\\,pp gap vs.\\ L2) and recovery at $k{\\leq}0.7$.}\n\\label{fig:cliff_highlight}\n\\end{figure}\n\n\\textbf{Importance margin gradient.} L2's advantage shrinks with task complexity on $\\pi_{0.5}$ at $k{=}0.85$ (Appendix Table~\\ref{tab:full_results}): Object $\\Delta{=}+$93\\,pp $>$ Goal $+$35.2\\,pp $>$ Long $+$33.2\\,pp. Multi-step tasks distribute critical information across tokens with more heterogeneous norm profiles, which reduces the effectiveness of magnitude-based selection.\n\n\\subsection{VTR Recovery}\n\\label{sec:vtr_recovery}\n\nVTR uses $M$ learned queries cross-attending over all 128 source tokens (${\\sim}$22M parameters, ${\\sim}$5\\% of SmolVLA). At 75\\% compression, VTR achieves 60.1 $\\pm$ 1.3\\% SR ($M{=}32$, 3 seeds; Table~\\ref{tab:vtr_main}), exceeding the unpruned LoRA baseline (44.8\\%) by 15.3\\,pp. An extended training control (100K steps, identical recipe, no compressor) reaches only 45.0\\% ($p > 0.9$ vs.\\ baseline; Appendix~\\ref{app:smart_compress_details}), which rules out additional optimization as the source of improvement. The re-encoding module provides a beneficial inductive bias: by restructuring entangled pixel-shuffle tokens, VTR produces a representation that is both more compact and more effective than the original. A parameter-matched MLP adapter achieves 63.4 $\\pm$ 2.6\\% ($p{=}0.15$), which indicates the benefit stems from re-encoding itself, not the cross-attention mechanism. Cross-suite generalization confirms the pattern: Spatial 53.2\\%, Goal 56.4\\%, both recovered from 0.0\\% under hard pruning.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VTR re-encoding on SmolVLA (LIBERO-Object). Hard pruning collapses all configurations to 0\\%; VTR achieves ${\\geq}$57\\% at up to 87.5\\% compression, exceeding the unpruned baseline. Baseline (44.8\\%) is our LoRA reproduction with smaller batch size; the official SmolVLA checkpoint achieves 59.2\\% (Table~\\ref{tab:main_results}). See Appendix~\\ref{app:smart_compress_details} for training details.}\n\\label{tab:vtr_main}\n\\begin{tabular}{lccr}\n\\toprule\nConfiguration & $M$ & Compress.\\ & SR (\\%) \\\\\n\\midrule\n\\textit{Baseline (unpruned)} & 128 & 0\\% & 44.8 \\\\\n\\textit{Hard pruning (any)} & -- & 5--50\\% & 0.0 \\\\\n\\midrule\nCross-attn VTR & 32 & 75\\% & 60.1 $\\pm$ 1.3 \\\\\nCross-attn VTR & 16 & 87.5\\% & 56.9 $\\pm$ 1.3 \\\\\nMLP adapter & 32 & 75\\% & 63.4 $\\pm$ 2.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Efficiency.}\\label{sec:efficiency} For $\\pi_{0.5}$, $k{=}0.9$ cuts attention FLOPs by ${\\sim}$16\\% while preserving full SR; VTR at $M{=}16$ achieves 87.5\\% compression with ${\\leq}$1.1\\,pp below passthrough.\n",
      "numLines": 135,
      "startLine": 1,
      "totalLines": 135
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
Now I understand the situation:

1. `sec:openvla_results` - label exists in `results.tex:41` but not in `experiments.tex` (which is what's compiled)
2. `sec:scaling_law` - label exists in `results.tex:100` but not in `experiments.tex`
3. `tab:taxonomy` - label exists in `results.tex:17` but not in `experiments.tex`

The references in `method.tex` and `experimental_setup.tex` point to labels that exist in `results.tex` but `experiments.tex` is what's included in `main.tex`.


I need to check what's actually in `experiments.tex` to see if these sections exist there under different labels, or if the references need to be updated. Looking at the context of each reference—the multi-seed evaluation discussion, the scaling law analysis, and the taxonomy table—I should see whether `experiments.tex` has corresponding content that just needs the labels added.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "uuid": "405637cf-20c3-4a49-8cdd-420ebec5fb0f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CCuXxu7epGF4Dgnt58fUUS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5443,
      "cache_read_input_tokens": 26983,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5443
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

现在查看 `experiments.tex` 中已有的 label，以及 `experimental_setup.tex` 和 `method.tex` 中引用的上下文，确定如何映射。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "uuid": "099b99bd-8422-4909-9193-ae1c383844e4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CCuXxu7epGF4Dgnt58fUUS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5443,
      "cache_read_input_tokens": 26983,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5443
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

<details open><summary>🔧 Tool call — Bash · `toolu_015AjWLJFMDAhg2onifrNvb4`</summary>

```json
{
  "command": "grep -n 'label{' /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "uuid": "d12c7801-62b7-4bbd-b270-ee7fb1619c8d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CCuXxu7epGF4Dgnt58fUUS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5443,
      "cache_read_input_tokens": 26983,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5443
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

_source line 24 · 2026-05-28T18:18:57.592Z_

<details><summary>↩ Tool result · `toolu_015AjWLJFMDAhg2onifrNvb4`</summary>

```text
2:\label{sec:experiments}
5:\label{sec:exp_setup}
14:\label{sec:two_axis}
20:\label{fig:pruning_overview}
37:\label{tab:main_results}
64:\label{sec:pixel_shuffle}
71:\caption{}\label{fig:pixel_shuffle}
77:\caption{}\label{fig:method_gap}
80:\label{fig:entanglement_scoring}
86:\label{sec:zeromask}
91:\label{sec:cv_sensitivity}
105:\label{fig:cliff_highlight}
111:\label{sec:vtr_recovery}
119:\label{tab:vtr_main}
134:\textbf{Efficiency.}\label{sec:efficiency} For $\pi_{0.5}$, $k{=}0.9$ cuts attention FLOPs by ${\sim}$16\% while preserving full SR; VTR at $M{=}16$ achieves 87.5\% compression with ${\leq}$1.1\,pp below passthrough.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "uuid": "6f835192-269c-4791-ad64-29ffa9823304",
  "tool_use_result": {
    "stdout": "2:\\label{sec:experiments}\n5:\\label{sec:exp_setup}\n14:\\label{sec:two_axis}\n20:\\label{fig:pruning_overview}\n37:\\label{tab:main_results}\n64:\\label{sec:pixel_shuffle}\n71:\\caption{}\\label{fig:pixel_shuffle}\n77:\\caption{}\\label{fig:method_gap}\n80:\\label{fig:entanglement_scoring}\n86:\\label{sec:zeromask}\n91:\\label{sec:cv_sensitivity}\n105:\\label{fig:cliff_highlight}\n111:\\label{sec:vtr_recovery}\n119:\\label{tab:vtr_main}\n134:\\textbf{Efficiency.}\\label{sec:efficiency} For $\\pi_{0.5}$, $k{=}0.9$ cuts attention FLOPs by ${\\sim}$16\\% while preserving full SR; VTR at $M{=}16$ achieves 87.5\\% compression with ${\\leq}$1.1\\,pp below passthrough.",
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

_source line 25_

<details open><summary>🔧 Tool call — Read · `toolu_01Do8cynanwidKb7mJ9m8ExR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "uuid": "ab2c1702-b14e-4059-ba43-a5f7198eab73",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CCuXxu7epGF4Dgnt58fUUS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5443,
      "cache_read_input_tokens": 26983,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5443
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

_source line 26 · 2026-05-28T18:18:57.825Z_

<details><summary>↩ Tool result · `toolu_01Do8cynanwidKb7mJ9m8ExR`</summary>

```text
1	\section{Methods and Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	\subsection{Architectures and Benchmark}
5	\label{sec:setup_overview}
6	
7	Seven VLA architectures spanning three vision connector families provide the testbed (Table~\ref{tab:taxonomy}).
8	
9	\textbf{Linear projection.} $\pi_0$~\cite{black2024pi0} (3.3B, 256 tokens) maps SigLIP~\cite{zhai2023siglip} patches through a single linear layer; $\pi_0.5$~\cite{black2025pi05} (4B, 768 tokens from three cameras) adds a learned $\times\!\sqrt{d}$ scaling; X-VLA~\cite{zheng2025xvla} (880M, 50 tokens) augments its linear projection with a 12-layer BART encoder~\cite{lewis2020bart} that introduces cross-token mixing. \textbf{MLP projector.} OpenVLA~\cite{kim2024openvla} (7B, 256 tokens) fuses DINOv2~\cite{oquab2023dinov2} and SigLIP through a three-layer MLP; OFT~\cite{kim2025openoft} shares this connector (entropy comparison only); CogACT~\cite{li2024cogact} retains 74.2\% SR under 78\% pruning per EfficientVLA~\cite{yang2025efficientvla} (literature corroboration, not our evaluation). \textbf{Spatial folding.} SmolVLA~\cite{shukor2025smolvla} (450M, 128 tokens) applies pixel-shuffle ($4{\times}4$ folding) so each token encodes 16 contiguous patches.
10	
11	We evaluate on LIBERO~\cite{liu2023libero} (Object: 10 tasks $\times$ 50 episodes = 500 total; Spatial and Goal for cross-suite validation). Closed-loop success rate (SR) with Wilson 95\% CIs is the primary metric; multi-seed results report mean $\pm$ std. Baselines: SmolVLA 44.8\%, OpenVLA 74.0\%, X-VLA 99.2\%, $\pi_0.5$ 98.2\%.
12	
13	\subsection{Pruning Protocol}
14	\label{sec:pruning_protocol}
15	
16	Two methods bracket robustness. \textbf{L2 norm-based removal} ranks tokens by L2 norm and physically removes the lowest-norm fraction, providing a favorable test. \textbf{Random removal} selects tokens uniformly at random, providing a conservative lower bound. Both physically remove tokens (not zero-masking); remaining tokens retain spatial ordering with re-indexed position IDs. Per-model retention ratios and cross-architecture comparison details appear in Appendix~\ref{app:pruning_details}.
17	
18	\subsection{Vision Token Re-encoder (VTR)}
19	\label{sec:smart_compress_setup}
20	
21	A cross-attention module (22.2M parameters, $\sim$5\% of SmolVLA) is inserted between the pixel-shuffle connector and the LLM backbone. $M$ learned queries attend over 128 source tokens, producing $M$ compressed representations ($M \in \{16, 32, 64, 96, 128\}$; $M{=}128$ = passthrough control). A parameter-matched MLP adapter (22.14M) serves as architecture control. Both train from SmolVLA-Base for 100K steps with identical hyperparameters; an extended training control without the compressor achieves 45.0\% SR ($p > 0.9$ vs.\ 44.8\% baseline). Training details in Appendix~\ref{app:smart_compress_details}.
22	
23	\subsection{Diagnostic Metrics}
24	\label{sec:diagnostic_metrics}
25	
26	\textbf{Token importance CV} (coefficient of variation of L2 norms) tracks pruning tolerance continuously: uniformly critical at CV $< 0.06$, threshold-graded at $\sim$0.15, smooth graded at $\sim$0.22, catastrophic cliff at $> 0.3$. \textbf{Attention entropy ratio} (normalized Shannon entropy of attention weights over vision tokens) provides a complementary view: OFT and OpenVLA share nearly identical entropy (0.667 vs.\ 0.661), confirming the connector is associated with token utilization patterns independent of action head.
27	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "uuid": "a5563b20-5d3a-4ed0-be26-0ba5a9e4e7b5",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex",
      "content": "\\section{Methods and Experimental Setup}\n\\label{sec:experimental_setup}\n\n\\subsection{Architectures and Benchmark}\n\\label{sec:setup_overview}\n\nSeven VLA architectures spanning three vision connector families provide the testbed (Table~\\ref{tab:taxonomy}).\n\n\\textbf{Linear projection.} $\\pi_0$~\\cite{black2024pi0} (3.3B, 256 tokens) maps SigLIP~\\cite{zhai2023siglip} patches through a single linear layer; $\\pi_0.5$~\\cite{black2025pi05} (4B, 768 tokens from three cameras) adds a learned $\\times\\!\\sqrt{d}$ scaling; X-VLA~\\cite{zheng2025xvla} (880M, 50 tokens) augments its linear projection with a 12-layer BART encoder~\\cite{lewis2020bart} that introduces cross-token mixing. \\textbf{MLP projector.} OpenVLA~\\cite{kim2024openvla} (7B, 256 tokens) fuses DINOv2~\\cite{oquab2023dinov2} and SigLIP through a three-layer MLP; OFT~\\cite{kim2025openoft} shares this connector (entropy comparison only); CogACT~\\cite{li2024cogact} retains 74.2\\% SR under 78\\% pruning per EfficientVLA~\\cite{yang2025efficientvla} (literature corroboration, not our evaluation). \\textbf{Spatial folding.} SmolVLA~\\cite{shukor2025smolvla} (450M, 128 tokens) applies pixel-shuffle ($4{\\times}4$ folding) so each token encodes 16 contiguous patches.\n\nWe evaluate on LIBERO~\\cite{liu2023libero} (Object: 10 tasks $\\times$ 50 episodes = 500 total; Spatial and Goal for cross-suite validation). Closed-loop success rate (SR) with Wilson 95\\% CIs is the primary metric; multi-seed results report mean $\\pm$ std. Baselines: SmolVLA 44.8\\%, OpenVLA 74.0\\%, X-VLA 99.2\\%, $\\pi_0.5$ 98.2\\%.\n\n\\subsection{Pruning Protocol}\n\\label{sec:pruning_protocol}\n\nTwo methods bracket robustness. \\textbf{L2 norm-based removal} ranks tokens by L2 norm and physically removes the lowest-norm fraction, providing a favorable test. \\textbf{Random removal} selects tokens uniformly at random, providing a conservative lower bound. Both physically remove tokens (not zero-masking); remaining tokens retain spatial ordering with re-indexed position IDs. Per-model retention ratios and cross-architecture comparison details appear in Appendix~\\ref{app:pruning_details}.\n\n\\subsection{Vision Token Re-encoder (VTR)}\n\\label{sec:smart_compress_setup}\n\nA cross-attention module (22.2M parameters, $\\sim$5\\% of SmolVLA) is inserted between the pixel-shuffle connector and the LLM backbone. $M$ learned queries attend over 128 source tokens, producing $M$ compressed representations ($M \\in \\{16, 32, 64, 96, 128\\}$; $M{=}128$ = passthrough control). A parameter-matched MLP adapter (22.14M) serves as architecture control. Both train from SmolVLA-Base for 100K steps with identical hyperparameters; an extended training control without the compressor achieves 45.0\\% SR ($p > 0.9$ vs.\\ 44.8\\% baseline). Training details in Appendix~\\ref{app:smart_compress_details}.\n\n\\subsection{Diagnostic Metrics}\n\\label{sec:diagnostic_metrics}\n\n\\textbf{Token importance CV} (coefficient of variation of L2 norms) tracks pruning tolerance continuously: uniformly critical at CV $< 0.06$, threshold-graded at $\\sim$0.15, smooth graded at $\\sim$0.22, catastrophic cliff at $> 0.3$. \\textbf{Attention entropy ratio} (normalized Shannon entropy of attention weights over vision tokens) provides a complementary view: OFT and OpenVLA share nearly identical entropy (0.667 vs.\\ 0.661), confirming the connector is associated with token utilization patterns independent of action head.\n",
      "numLines": 27,
      "startLine": 1,
      "totalLines": 27
    }
  }
}
```

</details>

---

### Assistant

_source line 27_

<details><summary>Logged reasoning block</summary>

```text
Now I understand the full picture:

1. **`tab:taxonomy`** - Referenced in `experimental_setup.tex:7` and `method.tex:101`. In `results.tex:17` there's `\label{tab:taxonomy}` but `results.tex` isn't compiled. I need to check if there's a table in `experiments.tex` that serves the same purpose. Looking at `experiments.tex`, there's `tab:main_results` (line 37) and `tab:vtr_main` (line 119). The `tab:model_properties` is referenced in `experiments.tex:9` but is it defined? Let me check.


2. **`sec:openvla_results`** - Referenced in `method.tex:64` about multi-seed evaluation, and defined in `results.tex:41`, but there's no matching section in `experiments.tex`. The reference to controlling evaluation through multiple seeds might need to be reframed or point to a different section.
3. **`sec:scaling_law`** - Referenced in `method.tex:66,98` regarding how importance margin varies with CV and k, which conceptually aligns with `sec:cv_sensitivity`.

Now I'm checking whether `tab:model_properties` and `tab:taxonomy` are actually defined. I notice `experimental_setup.tex` references `tab:taxonomy` on line 7, but since `main.tex` only includes `experiments.tex` and not `experimental_setup.tex`, that file isn't being compiled. The undefined reference for `tab:taxonomy` appears on page 6 line 101 according to the log, so I need to trace where that's actually coming from in the compiled files.

Looking at the latexmk output more carefully, the undefined references are all pointing to `method.tex`: `sec:openvla_results` at line 64, `sec:scaling_law` at lines 66 and 98, and `tab:taxonomy` at line 101. Since `main.tex` only includes abstract, introduction, related_work, method, experiments, conclusion, limitations, and appendix—not `experimental_setup.tex` or `results.tex`—all these missing references must be defined in `method.tex` but are being referenced before they're actually created.

For the fixes: the `sec:openvla_results` reference in method.tex:64 mentions multi-seed evaluation, but there's no dedicated OpenVLA results section in experiments.tex—the multi-seed information is just mentioned in the experiment setup section, so I should either point to that or remove the reference entirely. The `sec:scaling_law` references at lines 66 and 98 both discuss how importance margin varies with cross-validation, which actually corresponds to `sec:cv_sensitivity` in experiments.tex. For `tab:taxonomy` at line 101, I need to find where this table is actually defined—experiments.tex has `tab:main_results` for results but nothing that looks like a taxonomy table, so I should check if `tab:model_properties` exists elsewhere.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "uuid": "e81a53a8-9a23-4ce2-afc2-0f035caed4e8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019NJwit6gM5aW5Tijm7CM89",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2163,
      "cache_read_input_tokens": 32426,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2163
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

_source line 28_

<details open><summary>🔧 Tool call — Bash · `toolu_01LG7nJkQ1xFihSPszBgSNby`</summary>

```json
{
  "command": "grep -rn 'label{tab:model_properties}\\|ref{tab:model_properties}' /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "uuid": "ded96110-854b-455e-8f62-de66fab9b4c2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019NJwit6gM5aW5Tijm7CM89",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2163,
      "cache_read_input_tokens": 32426,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2163
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

_source line 29_

<details open><summary>🔧 Tool call — Bash · `toolu_014Ue6fNGPxmrji5pGeXtt6m`</summary>

```json
{
  "command": "grep -rn 'label{tab:taxonomy}' /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "uuid": "92695584-563d-4ed6-a9e8-e7bd3286d9f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019NJwit6gM5aW5Tijm7CM89",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2163,
      "cache_read_input_tokens": 32426,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2163
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

_source line 30 · 2026-05-28T18:19:25.753Z_

<details><summary>↩ Tool result · `toolu_014Ue6fNGPxmrji5pGeXtt6m`</summary>

```text
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/results.tex:17:\label{tab:taxonomy}
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/results_v2.tex:17:\label{tab:taxonomy}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "uuid": "16a8e0a7-56d3-481d-92b0-94e632d93ac2",
  "tool_use_result": {
    "stdout": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/results.tex:17:\\label{tab:taxonomy}\n/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/results_v2.tex:17:\\label{tab:taxonomy}",
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

_source line 31 · 2026-05-28T18:19:25.759Z_

<details><summary>↩ Tool result · `toolu_01LG7nJkQ1xFihSPszBgSNby`</summary>

```text
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex:739:The six-architecture taxonomy (Table~\ref{tab:model_properties}) spans a continuous spectrum of token independence structures, each associated with the vision-to-LLM connector rather than model scale or action head design.
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex:9:\paragraph{Models.} Four VLAs are evaluated in closed-loop control: $\pi_{0.5}$~\cite{black2025pi05} (4B, linear projection, 768 tokens, CV$\,{=}\,$0.055), X-VLA~\cite{zheng2025xvla} (0.9B, linear + 12-layer BART encoder, 50 tokens, CV$\,{=}\,$0.151), OpenVLA~\cite{kim2024openvla} (7B, 3-layer MLP, 256 tokens, CV$\,{=}\,$0.215), and SmolVLA~\cite{shukor2025smolvla} (450M, pixel-shuffle $4{\times}4$, 128 tokens, CV$\,{=}\,$0.314). Two additional models ($\pi_{0}$~\cite{black2024pi0}, OFT~\cite{kim2025openoft}) contribute to the CV diagnostic via offline metrics only. Table~\ref{tab:model_properties} summarizes all six architectures.
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex:7:We evaluate token pruning across six VLA architectures spanning three vision connector families (Table~\ref{tab:model_properties}; Figure~\ref{fig:architecture}). These connectors differ in whether they process ViT patches independently or create cross-token dependencies.
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex:28:\label{tab:model_properties}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "uuid": "905d2a42-cacb-4f22-9935-1a62b6252e8f",
  "tool_use_result": {
    "stdout": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex:739:The six-architecture taxonomy (Table~\\ref{tab:model_properties}) spans a continuous spectrum of token independence structures, each associated with the vision-to-LLM connector rather than model scale or action head design.\n/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex:9:\\paragraph{Models.} Four VLAs are evaluated in closed-loop control: $\\pi_{0.5}$~\\cite{black2025pi05} (4B, linear projection, 768 tokens, CV$\\,{=}\\,$0.055), X-VLA~\\cite{zheng2025xvla} (0.9B, linear + 12-layer BART encoder, 50 tokens, CV$\\,{=}\\,$0.151), OpenVLA~\\cite{kim2024openvla} (7B, 3-layer MLP, 256 tokens, CV$\\,{=}\\,$0.215), and SmolVLA~\\cite{shukor2025smolvla} (450M, pixel-shuffle $4{\\times}4$, 128 tokens, CV$\\,{=}\\,$0.314). Two additional models ($\\pi_{0}$~\\cite{black2024pi0}, OFT~\\cite{kim2025openoft}) contribute to the CV diagnostic via offline metrics only. Table~\\ref{tab:model_properties} summarizes all six architectures.\n/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex:7:We evaluate token pruning across six VLA architectures spanning three vision connector families (Table~\\ref{tab:model_properties}; Figure~\\ref{fig:architecture}). These connectors differ in whether they process ViT patches independently or create cross-token dependencies.\n/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex:28:\\label{tab:model_properties}",
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

_source line 32_

<details><summary>Logged reasoning block</summary>

```text
Now I see: `tab:model_properties` exists in `method.tex:28` and is correctly referenced. The `tab:taxonomy` in `results.tex` is not compiled. The reference to `tab:taxonomy` in `method.tex:101` should be changed to `tab:model_properties`.

Let me now plan the fixes:

1. **`tab:taxonomy`** in `method.tex:101`: Change to `tab:model_properties` (which exists in method.tex:28)
2. **`sec:scaling_law`** in `method.tex:66,98`: Change to `sec:cv_sensitivity` (which exists in experiments.tex:91)


3. **`sec:openvla_results`** in `method.tex:64`: The reference is about multi-seed evaluation, which is actually described in the experimental setup section. I should change this to `sec:exp_setup` since that's where the multi-seed protocol is documented.

I also notice `experimental_setup.tex:7` references `tab:taxonomy`, but this file isn't included in the compilation path anyway, so it won't trigger a warning.

Now I'm updating the references in `method.tex`: changing line 64 to point to `sec:exp_setup` instead of `sec:openvla_results`, updating lines 66 and 98 to reference `sec:cv_sensitivity` instead of `sec:scaling_law`, and fixing line 101 to use `tab:model_properties` instead of `tab:taxonomy`.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "uuid": "4be0480a-cd52-429c-9eb7-aa19ea8c874e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CM2jBPfk1FcRsXWT2XBUiG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 131,
      "cache_creation_input_tokens": 1724,
      "cache_read_input_tokens": 34589,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1724
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

_source line 33_

定位完毕。所有 4 个 undefined refs 都在 `method.tex` 中，引用了 `results.tex` 中的 label，但 `results.tex` 不在编译路径中。`experiments.tex` 有对应的 label 可以替换：

| undefined label | 出现位置 | 替换为 |
|---|---|---|
| `sec:openvla_results` | method.tex:64 | `sec:exp_setup` |
| `sec:scaling_law` | method.tex:66, 98 | `sec:cv_sensitivity` |
| `tab:taxonomy` | method.tex:101 | `tab:model_properties` |

注意 `experiments.tex` 可能被另一个 Worker 编辑，这里只改 `method.tex`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "uuid": "2059100a-2a62-4b3d-b39d-f822efc26d0d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CM2jBPfk1FcRsXWT2XBUiG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 131,
      "cache_creation_input_tokens": 1724,
      "cache_read_input_tokens": 34589,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1724
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

_source line 34_

<details open><summary>🔧 Tool call — Read · `toolu_01AVQWVWVKxRNRNAqesHeoDC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
  "offset": 60,
  "limit": 45
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "uuid": "539a76e4-7b5a-4b59-ae9c-cd86d9daca61",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CM2jBPfk1FcRsXWT2XBUiG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 131,
      "cache_creation_input_tokens": 1724,
      "cache_read_input_tokens": 34589,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1724
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

_source line 35 · 2026-05-28T18:19:50.603Z_

<details><summary>↩ Tool result · `toolu_01AVQWVWVKxRNRNAqesHeoDC`</summary>

```text
60	\begin{equation}
61	s_{\text{rand}}(t_i) \sim \mathcal{U}(0, 1)\,.
62	\label{eq:random_score}
63	\end{equation}
64	Random selection provides the null hypothesis that all post-connector tokens are interchangeable. If L2 scoring cannot outperform random, the token norm distribution carries no exploitable signal. Random selection also preserves the spatial distribution of the original token set in expectation, making it the natural baseline for spatially uniform architectures. Its primary limitation is sampling variance across episodes, which we control through multi-seed evaluation (Section~\ref{sec:openvla_results}).
65	
66	The \emph{importance margin} at ratio $k$ is defined as $\Delta(k) = \text{SR}_{\text{L2}}(k) - \text{SR}_{\text{Random}}(k)$. A positive margin indicates that the norm distribution contains exploitable importance structure. A negative margin indicates that L2 selection is actively harmful, typically because spatial clustering outweighs the benefit of importance ranking. The sign and magnitude of the importance margin vary systematically with both connector CV and $k$ (Section~\ref{sec:scaling_law}).
67	
68	\paragraph{Attention-based alternatives.}
69	Attention-based scoring functions estimate token importance from the LLM's internal attention weights. Three principal variants exist: (i)~\emph{column-sum scoring} sums each vision token's received attention weight in the last transformer layer, capturing direct query-key dependencies at the final processing stage; (ii)~\emph{cross-layer mean scoring} averages column-sum scores across all layers, aggregating importance signals over the full transformer stack; (iii)~\emph{attention rollout} multiplies attention matrices layer by layer (adding identity matrices for residual connections) to approximate cumulative information flow from input tokens to the output. These methods rest on the premise that tokens receiving more attention contribute more to the model's prediction. Their primary limitation is computational: they require a full LLM forward pass and are backbone-specific. We focus on L2-norm and random scoring because they operate solely on the connector output, are backbone-agnostic, and suffice to reveal the connector-dependent importance structure that is our primary object of study. Attention entropy enters our analysis as a diagnostic metric (Section~\ref{sec:cv_diagnostic}), not as a pruning criterion.
70	
71	\paragraph{Retention ratio design space.}
72	We evaluate $k \in \{0.30, 0.50, 0.70, 0.75, 0.85, 0.90, 0.95\}$, spanning from extreme compression (retaining 30\% of tokens) to conservative trimming (retaining 95\%). This range captures the full degradation profile of each connector type. At one end, $k = 0.95$ tests whether even minimal removal is tolerable (e.g., 6 of 128 tokens for SmolVLA). At the other, $k = 0.30$ probes behavior under severe information loss (e.g., 15 of 50 tokens for X-VLA). The intermediate values are chosen to identify \emph{cliff zones}: narrow $k$ intervals where success rate drops discontinuously rather than degrading proportionally. A cliff zone indicates a critical token density below which the model's visual representation breaks down. Different connector architectures exhibit cliffs at qualitatively different retention ratios: pixel-shuffle connectors cliff at $k = 0.95$ (the most conservative ratio tested), BART-encoded connectors near $k \approx 0.85$, and MLP connectors degrade without a sharp cliff at any tested ratio. For targeted models where initial results indicate a cliff, we add finer-grained ratios ($k \in \{0.80, 0.925\}$) to localize the transition boundary (Section~\ref{sec:two_axis}).
73	
74	\subsection{Compressibility Diagnostic: Importance CV}
75	\label{sec:cv_diagnostic}
76	
77	We seek a zero-cost diagnostic that predicts a model's pruning tolerance without running closed-loop evaluation. The coefficient of variation (CV) of post-connector token L2 norms provides this:
78	\begin{equation}
79	\text{CV} = \frac{\sigma\!\left(\{\|t_i\|_2\}_{i=1}^{N}\right)}{\mu\!\left(\{\|t_i\|_2\}_{i=1}^{N}\right)}
80	\label{eq:cv}
81	\end{equation}
82	where $\sigma$ and $\mu$ denote the standard deviation and mean over all $N$ post-connector tokens from a single forward pass. CV requires no labeled data, no downstream task evaluation, and no access to the LLM backbone.
83	
84	\paragraph{The CV spectrum.}
85	CV captures a continuous ordering across six models and three connector families:
86	\begin{equation}
87	\begin{split}
88	\underbrace{\pi_0\,(0.038) \;<\; \pi_{0.5}\,(0.055)}_{\text{linear proj.}} &\;<\; \underbrace{\text{X-VLA}\,(0.151)}_{\text{linear + BART}} \\
89	&\;<\; \underbrace{\text{OpenVLA}\,(0.215) \;\approx\; \text{OFT}\,(0.219)}_{\text{MLP proj.}} \;<\; \underbrace{\text{SmolVLA}\,(0.314)}_{\text{pixel-shuffle}}
90	\end{split}
91	\label{eq:cv_spectrum}
92	\end{equation}
93	This ordering reflects the degree of cross-token mixing in each connector. Pure linear projections process patches independently, producing near-uniform norms (CV$\,{<}\,$0.06). MLP projectors apply nonlinear transformations per token, amplifying norm variance through activation functions and layered composition (CV$\,{\approx}\,$0.22). Pixel-shuffle folds $4 \times 4$ patch blocks into single tokens by channel concatenation, creating maximal cross-patch entanglement and the highest norm heterogeneity (CV$\,{=}\,$0.314). X-VLA occupies an intermediate position: its linear projection is followed by a 12-layer BART encoder~\cite{lewis2020bart} that introduces cross-token attention, raising CV from what a pure linear projection would produce (${\sim}$0.04) to 0.151.
94	
95	\paragraph{CV as pruning tolerance predictor.}
96	CV measures the dispersion of token importance under the L2-norm proxy. High CV indicates that some tokens carry substantially larger norms than others; these high-norm tokens can be identified and retained while low-norm tokens are removed with limited information loss. Low CV indicates near-uniform norms: no token subset is dispensable because all tokens contribute comparably. Pruning a low-CV model is equivalent to downsampling a uniform signal, where the spatial pattern of removal matters more than which specific tokens are selected by importance.
97	
98	CV also predicts the \emph{optimal pruning strategy}, not only the tolerance ceiling. When CV is low ($< 0.15$), L2-norm ranking captures spatial artifacts rather than genuine importance differences, and random selection outperforms L2 by preserving spatial coverage. When CV is high ($> 0.20$), L2-norm ranking exploits real importance differentiation and outperforms random. The importance margin $\Delta(\text{L2} - \text{Random})$ increases monotonically with CV at both $k = 0.5$ and $k = 0.7$ across three closed-loop models ($\pi_{0.5}$, X-VLA, OpenVLA), confirming that CV captures a structural property of the connector rather than an artifact of a particular retention ratio (Section~\ref{sec:scaling_law}).
99	
100	\paragraph{Complementary role of attention entropy.}
101	Attention entropy, defined as the mean Shannon entropy of the LLM's attention weight distribution over vision tokens, provides a complementary but less discriminative signal. Entropy measures how uniformly the LLM attends across vision tokens: high entropy indicates distributed attention, low entropy indicates selective focus. Three models with qualitatively different pruning behaviors, however, cluster within a narrow entropy band: $\pi_{0.5}$ (0.666), X-VLA (0.614), and OpenVLA (0.661) span only 0.05 in entropy despite spanning 0.055 to 0.215 in CV and exhibiting uniformly critical, threshold-graded, and smooth graded pruning responses respectively. SmolVLA's entropy (0.952) is near-maximal, yet it is the least pruning-tolerant model. The discrepancy arises because entropy reflects the LLM's \emph{reading pattern} (how attention is distributed across tokens), while CV reflects the connector's \emph{writing pattern} (how information is distributed into tokens). The connector's output structure, not the downstream attention allocation, determines pruning robustness. We report entropy values alongside CV in our taxonomy (Table~\ref{tab:taxonomy}) as a mechanistic supplement, but use CV as the primary diagnostic throughout.
102	
103	\subsection{Vision Token Re-encoder (VTR)}
104	\label{sec:vtr}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "uuid": "f9ed0066-c3da-43f5-b2a8-fef02025dc92",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
      "content": "\\begin{equation}\ns_{\\text{rand}}(t_i) \\sim \\mathcal{U}(0, 1)\\,.\n\\label{eq:random_score}\n\\end{equation}\nRandom selection provides the null hypothesis that all post-connector tokens are interchangeable. If L2 scoring cannot outperform random, the token norm distribution carries no exploitable signal. Random selection also preserves the spatial distribution of the original token set in expectation, making it the natural baseline for spatially uniform architectures. Its primary limitation is sampling variance across episodes, which we control through multi-seed evaluation (Section~\\ref{sec:openvla_results}).\n\nThe \\emph{importance margin} at ratio $k$ is defined as $\\Delta(k) = \\text{SR}_{\\text{L2}}(k) - \\text{SR}_{\\text{Random}}(k)$. A positive margin indicates that the norm distribution contains exploitable importance structure. A negative margin indicates that L2 selection is actively harmful, typically because spatial clustering outweighs the benefit of importance ranking. The sign and magnitude of the importance margin vary systematically with both connector CV and $k$ (Section~\\ref{sec:scaling_law}).\n\n\\paragraph{Attention-based alternatives.}\nAttention-based scoring functions estimate token importance from the LLM's internal attention weights. Three principal variants exist: (i)~\\emph{column-sum scoring} sums each vision token's received attention weight in the last transformer layer, capturing direct query-key dependencies at the final processing stage; (ii)~\\emph{cross-layer mean scoring} averages column-sum scores across all layers, aggregating importance signals over the full transformer stack; (iii)~\\emph{attention rollout} multiplies attention matrices layer by layer (adding identity matrices for residual connections) to approximate cumulative information flow from input tokens to the output. These methods rest on the premise that tokens receiving more attention contribute more to the model's prediction. Their primary limitation is computational: they require a full LLM forward pass and are backbone-specific. We focus on L2-norm and random scoring because they operate solely on the connector output, are backbone-agnostic, and suffice to reveal the connector-dependent importance structure that is our primary object of study. Attention entropy enters our analysis as a diagnostic metric (Section~\\ref{sec:cv_diagnostic}), not as a pruning criterion.\n\n\\paragraph{Retention ratio design space.}\nWe evaluate $k \\in \\{0.30, 0.50, 0.70, 0.75, 0.85, 0.90, 0.95\\}$, spanning from extreme compression (retaining 30\\% of tokens) to conservative trimming (retaining 95\\%). This range captures the full degradation profile of each connector type. At one end, $k = 0.95$ tests whether even minimal removal is tolerable (e.g., 6 of 128 tokens for SmolVLA). At the other, $k = 0.30$ probes behavior under severe information loss (e.g., 15 of 50 tokens for X-VLA). The intermediate values are chosen to identify \\emph{cliff zones}: narrow $k$ intervals where success rate drops discontinuously rather than degrading proportionally. A cliff zone indicates a critical token density below which the model's visual representation breaks down. Different connector architectures exhibit cliffs at qualitatively different retention ratios: pixel-shuffle connectors cliff at $k = 0.95$ (the most conservative ratio tested), BART-encoded connectors near $k \\approx 0.85$, and MLP connectors degrade without a sharp cliff at any tested ratio. For targeted models where initial results indicate a cliff, we add finer-grained ratios ($k \\in \\{0.80, 0.925\\}$) to localize the transition boundary (Section~\\ref{sec:two_axis}).\n\n\\subsection{Compressibility Diagnostic: Importance CV}\n\\label{sec:cv_diagnostic}\n\nWe seek a zero-cost diagnostic that predicts a model's pruning tolerance without running closed-loop evaluation. The coefficient of variation (CV) of post-connector token L2 norms provides this:\n\\begin{equation}\n\\text{CV} = \\frac{\\sigma\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}{\\mu\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}\n\\label{eq:cv}\n\\end{equation}\nwhere $\\sigma$ and $\\mu$ denote the standard deviation and mean over all $N$ post-connector tokens from a single forward pass. CV requires no labeled data, no downstream task evaluation, and no access to the LLM backbone.\n\n\\paragraph{The CV spectrum.}\nCV captures a continuous ordering across six models and three connector families:\n\\begin{equation}\n\\begin{split}\n\\underbrace{\\pi_0\\,(0.038) \\;<\\; \\pi_{0.5}\\,(0.055)}_{\\text{linear proj.}} &\\;<\\; \\underbrace{\\text{X-VLA}\\,(0.151)}_{\\text{linear + BART}} \\\\\n&\\;<\\; \\underbrace{\\text{OpenVLA}\\,(0.215) \\;\\approx\\; \\text{OFT}\\,(0.219)}_{\\text{MLP proj.}} \\;<\\; \\underbrace{\\text{SmolVLA}\\,(0.314)}_{\\text{pixel-shuffle}}\n\\end{split}\n\\label{eq:cv_spectrum}\n\\end{equation}\nThis ordering reflects the degree of cross-token mixing in each connector. Pure linear projections process patches independently, producing near-uniform norms (CV$\\,{<}\\,$0.06). MLP projectors apply nonlinear transformations per token, amplifying norm variance through activation functions and layered composition (CV$\\,{\\approx}\\,$0.22). Pixel-shuffle folds $4 \\times 4$ patch blocks into single tokens by channel concatenation, creating maximal cross-patch entanglement and the highest norm heterogeneity (CV$\\,{=}\\,$0.314). X-VLA occupies an intermediate position: its linear projection is followed by a 12-layer BART encoder~\\cite{lewis2020bart} that introduces cross-token attention, raising CV from what a pure linear projection would produce (${\\sim}$0.04) to 0.151.\n\n\\paragraph{CV as pruning tolerance predictor.}\nCV measures the dispersion of token importance under the L2-norm proxy. High CV indicates that some tokens carry substantially larger norms than others; these high-norm tokens can be identified and retained while low-norm tokens are removed with limited information loss. Low CV indicates near-uniform norms: no token subset is dispensable because all tokens contribute comparably. Pruning a low-CV model is equivalent to downsampling a uniform signal, where the spatial pattern of removal matters more than which specific tokens are selected by importance.\n\nCV also predicts the \\emph{optimal pruning strategy}, not only the tolerance ceiling. When CV is low ($< 0.15$), L2-norm ranking captures spatial artifacts rather than genuine importance differences, and random selection outperforms L2 by preserving spatial coverage. When CV is high ($> 0.20$), L2-norm ranking exploits real importance differentiation and outperforms random. The importance margin $\\Delta(\\text{L2} - \\text{Random})$ increases monotonically with CV at both $k = 0.5$ and $k = 0.7$ across three closed-loop models ($\\pi_{0.5}$, X-VLA, OpenVLA), confirming that CV captures a structural property of the connector rather than an artifact of a particular retention ratio (Section~\\ref{sec:scaling_law}).\n\n\\paragraph{Complementary role of attention entropy.}\nAttention entropy, defined as the mean Shannon entropy of the LLM's attention weight distribution over vision tokens, provides a complementary but less discriminative signal. Entropy measures how uniformly the LLM attends across vision tokens: high entropy indicates distributed attention, low entropy indicates selective focus. Three models with qualitatively different pruning behaviors, however, cluster within a narrow entropy band: $\\pi_{0.5}$ (0.666), X-VLA (0.614), and OpenVLA (0.661) span only 0.05 in entropy despite spanning 0.055 to 0.215 in CV and exhibiting uniformly critical, threshold-graded, and smooth graded pruning responses respectively. SmolVLA's entropy (0.952) is near-maximal, yet it is the least pruning-tolerant model. The discrepancy arises because entropy reflects the LLM's \\emph{reading pattern} (how attention is distributed across tokens), while CV reflects the connector's \\emph{writing pattern} (how information is distributed into tokens). The connector's output structure, not the downstream attention allocation, determines pruning robustness. We report entropy values alongside CV in our taxonomy (Table~\\ref{tab:taxonomy}) as a mechanistic supplement, but use CV as the primary diagnostic throughout.\n\n\\subsection{Vision Token Re-encoder (VTR)}\n\\label{sec:vtr}",
      "numLines": 45,
      "startLine": 60,
      "totalLines": 113
    }
  }
}
```

</details>

---

### Assistant

_source line 36_

现在执行所有 4 处替换。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "uuid": "f89fd425-9cfc-4a41-9c17-51be6053a781",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ptj67rpSVcT4hTuBHfMumD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3453,
      "cache_read_input_tokens": 36313,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3453
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

_source line 37_

<details open><summary>🔧 Tool call — Edit · `toolu_01TfvPyacP2ndUs17sawvFQv`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
  "old_string": "(Section~\\ref{sec:openvla_results})",
  "new_string": "(Section~\\ref{sec:exp_setup})"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "uuid": "232d4553-f34f-43da-8791-8ef4675a21f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ptj67rpSVcT4hTuBHfMumD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3453,
      "cache_read_input_tokens": 36313,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3453
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

_source line 38 · 2026-05-28T18:19:56.295Z_

<details><summary>↩ Tool result · `toolu_01TfvPyacP2ndUs17sawvFQv`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "uuid": "7982c4e7-129c-4382-9a8e-fef1797f3c7f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
    "oldString": "(Section~\\ref{sec:openvla_results})",
    "newString": "(Section~\\ref{sec:exp_setup})",
    "originalFile": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Models and Connectors}\n\\label{sec:models}\n\nWe evaluate token pruning across six VLA architectures spanning three vision connector families (Table~\\ref{tab:model_properties}; Figure~\\ref{fig:architecture}). These connectors differ in whether they process ViT patches independently or create cross-token dependencies.\n\n\\textbf{Linear projection} applies a single matrix multiplication per patch. $\\pi_{0}$~\\cite{black2024pi0} projects 256 patches through a linear layer; $\\pi_{0.5}$~\\cite{black2025pi05} uses a $\\times\\!\\sqrt{d}$-scaled linear projection across 768 tokens from three image slots (two active cameras in LIBERO; CV$\\,{<}\\,$0.06).\n\n\\textbf{MLP projector} maps each patch independently through a multi-layer perceptron. OpenVLA~\\cite{kim2024openvla} uses a three-layer MLP (256 tokens; CV$\\,{=}\\,$0.215); OFT~\\cite{kim2025openoft} shares the same connector (512 tokens; CV$\\,{=}\\,$0.219).\n\n\\textbf{Token-entangling connectors} introduce cross-token dependencies. X-VLA~\\cite{zheng2025xvla} feeds tokens through a 12-layer BART encoder~\\cite{lewis2020bart} (50 tokens). SmolVLA~\\cite{shukor2025smolvla} applies pixel-shuffle $4{\\times}4$ folding, concatenating 16 contiguous patches per output token (128 tokens).\n\nWe classify coupling as \\emph{independent} when each output token depends on a single input patch, and \\emph{entangling} when output tokens encode information from multiple patches. Four models are evaluated in closed-loop control on LIBERO~\\cite{liu2023libero}; $\\pi_{0}$ and OFT contribute to the CV diagnostic only.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/paper/fig_architecture_v4.pdf}\n\\caption{Vision connector architectures across four closed-loop VLAs, ordered by increasing compressibility fragility. Token-independent connectors ($\\pi_{0.5}$: linear; OpenVLA: MLP) yield low CV. Token-entangling connectors (X-VLA: BART encoder; SmolVLA: pixel-shuffle) create cross-token dependencies and higher CV, predicting threshold-graded or catastrophic pruning failure.}\n\\label{fig:architecture}\n\\end{figure*}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VLA models evaluated. Coupling indicates independent vs.\\ cross-token processing. $N$ = vision tokens input to the LLM. $^\\dagger$OFT is an OpenVLA fine-tuning variant, included for CV calibration (offline metrics only).}\n\\label{tab:model_properties}\n\\begin{tabular}{lrlcrll}\n\\toprule\nModel & Params & Connector & $N$ & CV & Coupling & Eval \\\\\n\\midrule\n$\\pi_{0.5}$ & 4B & Linear ($\\times\\!\\sqrt{d}$) & 768 & 0.055 & Indep.\\ & Closed-loop \\\\\nX-VLA & 0.9B & Linear + BART & 50 & 0.151 & Entangling & Closed-loop \\\\\nOpenVLA & 7B & 3-layer MLP & 256 & 0.215 & Indep.\\ & Closed-loop \\\\\nSmolVLA & 450M & Pixel-shuffle $4{\\times}4$ & 128 & 0.314 & Entangling & Closed-loop \\\\\n\\midrule\n$\\pi_{0}$ & 3.3B & Linear & 256 & 0.038 & Indep.\\ & Offline \\\\\nOFT$^\\dagger$ & 7B & 3-layer MLP & 512 & 0.219 & Indep.\\ & Offline \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Pruning Protocol}\n\\label{sec:pruning_protocol}\n\nGiven $N$ post-connector vision tokens $\\{t_1, \\ldots, t_N\\}$ with $t_i \\in \\mathbb{R}^d$, token pruning selects a subset of size $\\lfloor k \\cdot N \\rfloor$ for retention ratio $k \\in (0, 1]$ and discards the rest. Unselected tokens are physically removed and position IDs are re-indexed to close gaps. We prune between the vision connector output and the LLM backbone input to isolate the connector's effect on token information structure: pruning before the connector would alter its input distribution, confounding architectural analysis with input perturbation.\n\n\\paragraph{Importance scoring functions.}\nA scoring function $s\\colon \\mathbb{R}^d \\to \\mathbb{R}$ assigns each token an importance score; the top-$\\lfloor kN \\rfloor$ tokens by score are retained. We evaluate two strategies that bracket expected performance.\n\n\\textbf{L2-norm scoring} assigns each token its activation magnitude:\n\\begin{equation}\ns_{\\text{L2}}(t_i) = \\|t_i\\|_2\\,.\n\\label{eq:l2_score}\n\\end{equation}\nThe L2 norm serves as a proxy for information density: tokens with larger norms carry stronger activations that exert greater influence on downstream attention computation. This proxy is architecture-agnostic and requires no access to the LLM backbone. L2 scoring introduces a spatial bias, however, because nearby patches share visual content and produce correlated norms. Under aggressive pruning, L2 selection can concentrate retained tokens in a single high-activation region at the cost of spatial coverage. This bias is benign at high retention ratios but becomes pathological at low $k$ for models with near-uniform norm distributions (Section~\\ref{sec:cv_sensitivity}).\n\n\\textbf{Random subsampling} draws $\\lfloor kN \\rfloor$ tokens uniformly at random:\n\\begin{equation}\ns_{\\text{rand}}(t_i) \\sim \\mathcal{U}(0, 1)\\,.\n\\label{eq:random_score}\n\\end{equation}\nRandom selection provides the null hypothesis that all post-connector tokens are interchangeable. If L2 scoring cannot outperform random, the token norm distribution carries no exploitable signal. Random selection also preserves the spatial distribution of the original token set in expectation, making it the natural baseline for spatially uniform architectures. Its primary limitation is sampling variance across episodes, which we control through multi-seed evaluation (Section~\\ref{sec:openvla_results}).\n\nThe \\emph{importance margin} at ratio $k$ is defined as $\\Delta(k) = \\text{SR}_{\\text{L2}}(k) - \\text{SR}_{\\text{Random}}(k)$. A positive margin indicates that the norm distribution contains exploitable importance structure. A negative margin indicates that L2 selection is actively harmful, typically because spatial clustering outweighs the benefit of importance ranking. The sign and magnitude of the importance margin vary systematically with both connector CV and $k$ (Section~\\ref{sec:scaling_law}).\n\n\\paragraph{Attention-based alternatives.}\nAttention-based scoring functions estimate token importance from the LLM's internal attention weights. Three principal variants exist: (i)~\\emph{column-sum scoring} sums each vision token's received attention weight in the last transformer layer, capturing direct query-key dependencies at the final processing stage; (ii)~\\emph{cross-layer mean scoring} averages column-sum scores across all layers, aggregating importance signals over the full transformer stack; (iii)~\\emph{attention rollout} multiplies attention matrices layer by layer (adding identity matrices for residual connections) to approximate cumulative information flow from input tokens to the output. These methods rest on the premise that tokens receiving more attention contribute more to the model's prediction. Their primary limitation is computational: they require a full LLM forward pass and are backbone-specific. We focus on L2-norm and random scoring because they operate solely on the connector output, are backbone-agnostic, and suffice to reveal the connector-dependent importance structure that is our primary object of study. Attention entropy enters our analysis as a diagnostic metric (Section~\\ref{sec:cv_diagnostic}), not as a pruning criterion.\n\n\\paragraph{Retention ratio design space.}\nWe evaluate $k \\in \\{0.30, 0.50, 0.70, 0.75, 0.85, 0.90, 0.95\\}$, spanning from extreme compression (retaining 30\\% of tokens) to conservative trimming (retaining 95\\%). This range captures the full degradation profile of each connector type. At one end, $k = 0.95$ tests whether even minimal removal is tolerable (e.g., 6 of 128 tokens for SmolVLA). At the other, $k = 0.30$ probes behavior under severe information loss (e.g., 15 of 50 tokens for X-VLA). The intermediate values are chosen to identify \\emph{cliff zones}: narrow $k$ intervals where success rate drops discontinuously rather than degrading proportionally. A cliff zone indicates a critical token density below which the model's visual representation breaks down. Different connector architectures exhibit cliffs at qualitatively different retention ratios: pixel-shuffle connectors cliff at $k = 0.95$ (the most conservative ratio tested), BART-encoded connectors near $k \\approx 0.85$, and MLP connectors degrade without a sharp cliff at any tested ratio. For targeted models where initial results indicate a cliff, we add finer-grained ratios ($k \\in \\{0.80, 0.925\\}$) to localize the transition boundary (Section~\\ref{sec:two_axis}).\n\n\\subsection{Compressibility Diagnostic: Importance CV}\n\\label{sec:cv_diagnostic}\n\nWe seek a zero-cost diagnostic that predicts a model's pruning tolerance without running closed-loop evaluation. The coefficient of variation (CV) of post-connector token L2 norms provides this:\n\\begin{equation}\n\\text{CV} = \\frac{\\sigma\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}{\\mu\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}\n\\label{eq:cv}\n\\end{equation}\nwhere $\\sigma$ and $\\mu$ denote the standard deviation and mean over all $N$ post-connector tokens from a single forward pass. CV requires no labeled data, no downstream task evaluation, and no access to the LLM backbone.\n\n\\paragraph{The CV spectrum.}\nCV captures a continuous ordering across six models and three connector families:\n\\begin{equation}\n\\begin{split}\n\\underbrace{\\pi_0\\,(0.038) \\;<\\; \\pi_{0.5}\\,(0.055)}_{\\text{linear proj.}} &\\;<\\; \\underbrace{\\text{X-VLA}\\,(0.151)}_{\\text{linear + BART}} \\\\\n&\\;<\\; \\underbrace{\\text{OpenVLA}\\,(0.215) \\;\\approx\\; \\text{OFT}\\,(0.219)}_{\\text{MLP proj.}} \\;<\\; \\underbrace{\\text{SmolVLA}\\,(0.314)}_{\\text{pixel-shuffle}}\n\\end{split}\n\\label{eq:cv_spectrum}\n\\end{equation}\nThis ordering reflects the degree of cross-token mixing in each connector. Pure linear projections process patches independently, producing near-uniform norms (CV$\\,{<}\\,$0.06). MLP projectors apply nonlinear transformations per token, amplifying norm variance through activation functions and layered composition (CV$\\,{\\approx}\\,$0.22). Pixel-shuffle folds $4 \\times 4$ patch blocks into single tokens by channel concatenation, creating maximal cross-patch entanglement and the highest norm heterogeneity (CV$\\,{=}\\,$0.314). X-VLA occupies an intermediate position: its linear projection is followed by a 12-layer BART encoder~\\cite{lewis2020bart} that introduces cross-token attention, raising CV from what a pure linear projection would produce (${\\sim}$0.04) to 0.151.\n\n\\paragraph{CV as pruning tolerance predictor.}\nCV measures the dispersion of token importance under the L2-norm proxy. High CV indicates that some tokens carry substantially larger norms than others; these high-norm tokens can be identified and retained while low-norm tokens are removed with limited information loss. Low CV indicates near-uniform norms: no token subset is dispensable because all tokens contribute comparably. Pruning a low-CV model is equivalent to downsampling a uniform signal, where the spatial pattern of removal matters more than which specific tokens are selected by importance.\n\nCV also predicts the \\emph{optimal pruning strategy}, not only the tolerance ceiling. When CV is low ($< 0.15$), L2-norm ranking captures spatial artifacts rather than genuine importance differences, and random selection outperforms L2 by preserving spatial coverage. When CV is high ($> 0.20$), L2-norm ranking exploits real importance differentiation and outperforms random. The importance margin $\\Delta(\\text{L2} - \\text{Random})$ increases monotonically with CV at both $k = 0.5$ and $k = 0.7$ across three closed-loop models ($\\pi_{0.5}$, X-VLA, OpenVLA), confirming that CV captures a structural property of the connector rather than an artifact of a particular retention ratio (Section~\\ref{sec:scaling_law}).\n\n\\paragraph{Complementary role of attention entropy.}\nAttention entropy, defined as the mean Shannon entropy of the LLM's attention weight distribution over vision tokens, provides a complementary but less discriminative signal. Entropy measures how uniformly the LLM attends across vision tokens: high entropy indicates distributed attention, low entropy indicates selective focus. Three models with qualitatively different pruning behaviors, however, cluster within a narrow entropy band: $\\pi_{0.5}$ (0.666), X-VLA (0.614), and OpenVLA (0.661) span only 0.05 in entropy despite spanning 0.055 to 0.215 in CV and exhibiting uniformly critical, threshold-graded, and smooth graded pruning responses respectively. SmolVLA's entropy (0.952) is near-maximal, yet it is the least pruning-tolerant model. The discrepancy arises because entropy reflects the LLM's \\emph{reading pattern} (how attention is distributed across tokens), while CV reflects the connector's \\emph{writing pattern} (how information is distributed into tokens). The connector's output structure, not the downstream attention allocation, determines pruning robustness. We report entropy values alongside CV in our taxonomy (Table~\\ref{tab:taxonomy}) as a mechanistic supplement, but use CV as the primary diagnostic throughout.\n\n\\subsection{Vision Token Re-encoder (VTR)}\n\\label{sec:vtr}\n\nHard pruning fails for token-entangling connectors because removing any token destroys spatially distributed information. VTR addresses this through learned re-encoding rather than deletion.\n\n\\paragraph{Architecture.}\nVTR inserts a 2-layer cross-attention module between the vision connector output and the LLM backbone input. Each layer uses 12 attention heads with dropout 0.1. A set of $M$ learned query vectors attends over all $N$ source tokens via standard multi-head cross-attention, producing $M$ compressed tokens as input to the LLM. The compression ratio is controlled by $M \\in \\{16, 32, 64, 96, 128\\}$; $M{=}N$ serves as a passthrough control.\n\n\\paragraph{Training and cost.}\nThe module adds ${\\sim}$22M trainable parameters ($<$5\\% of SmolVLA, the smallest VLA tested) and is trained end-to-end: compressor and action head parameters are jointly optimized. Architecture and training hyperparameters are detailed in Appendix~\\ref{app:smart_compress_details}.\n",
    "structuredPatch": [
      {
        "oldStart": 61,
        "oldLines": 7,
        "newStart": 61,
        "newLines": 7,
        "lines": [
          " s_{\\text{rand}}(t_i) \\sim \\mathcal{U}(0, 1)\\,.",
          " \\label{eq:random_score}",
          " \\end{equation}",
          "-Random selection provides the null hypothesis that all post-connector tokens are interchangeable. If L2 scoring cannot outperform random, the token norm distribution carries no exploitable signal. Random selection also preserves the spatial distribution of the original token set in expectation, making it the natural baseline for spatially uniform architectures. Its primary limitation is sampling variance across episodes, which we control through multi-seed evaluation (Section~\\ref{sec:openvla_results}).",
          "+Random selection provides the null hypothesis that all post-connector tokens are interchangeable. If L2 scoring cannot outperform random, the token norm distribution carries no exploitable signal. Random selection also preserves the spatial distribution of the original token set in expectation, making it the natural baseline for spatially uniform architectures. Its primary limitation is sampling variance across episodes, which we control through multi-seed evaluation (Section~\\ref{sec:exp_setup}).",
          " ",
          " The \\emph{importance margin} at ratio $k$ is defined as $\\Delta(k) = \\text{SR}_{\\text{L2}}(k) - \\text{SR}_{\\text{Random}}(k)$. A positive margin indicates that the norm distribution contains exploitable importance structure. A negative margin indicates that L2 selection is actively harmful, typically because spatial clustering outweighs the benefit of importance ranking. The sign and magnitude of the importance margin vary systematically with both connector CV and $k$ (Section~\\ref{sec:scaling_law}).",
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

_source line 39_

<details open><summary>🔧 Tool call — Edit · `toolu_018GQE1WUNvPhz7R91WM2AGc`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
  "old_string": "(Table~\\ref{tab:taxonomy})",
  "new_string": "(Table~\\ref{tab:model_properties})"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "uuid": "42189aba-6035-4835-bca3-fd46e234ed48",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ptj67rpSVcT4hTuBHfMumD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3453,
      "cache_read_input_tokens": 36313,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3453
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

_source line 40 · 2026-05-28T18:19:57.355Z_

<details><summary>↩ Tool result · `toolu_018GQE1WUNvPhz7R91WM2AGc`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "uuid": "1ad5f1e7-aba0-4080-a029-7e9b07be679b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
    "oldString": "(Table~\\ref{tab:taxonomy})",
    "newString": "(Table~\\ref{tab:model_properties})",
    "originalFile": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Models and Connectors}\n\\label{sec:models}\n\nWe evaluate token pruning across six VLA architectures spanning three vision connector families (Table~\\ref{tab:model_properties}; Figure~\\ref{fig:architecture}). These connectors differ in whether they process ViT patches independently or create cross-token dependencies.\n\n\\textbf{Linear projection} applies a single matrix multiplication per patch. $\\pi_{0}$~\\cite{black2024pi0} projects 256 patches through a linear layer; $\\pi_{0.5}$~\\cite{black2025pi05} uses a $\\times\\!\\sqrt{d}$-scaled linear projection across 768 tokens from three image slots (two active cameras in LIBERO; CV$\\,{<}\\,$0.06).\n\n\\textbf{MLP projector} maps each patch independently through a multi-layer perceptron. OpenVLA~\\cite{kim2024openvla} uses a three-layer MLP (256 tokens; CV$\\,{=}\\,$0.215); OFT~\\cite{kim2025openoft} shares the same connector (512 tokens; CV$\\,{=}\\,$0.219).\n\n\\textbf{Token-entangling connectors} introduce cross-token dependencies. X-VLA~\\cite{zheng2025xvla} feeds tokens through a 12-layer BART encoder~\\cite{lewis2020bart} (50 tokens). SmolVLA~\\cite{shukor2025smolvla} applies pixel-shuffle $4{\\times}4$ folding, concatenating 16 contiguous patches per output token (128 tokens).\n\nWe classify coupling as \\emph{independent} when each output token depends on a single input patch, and \\emph{entangling} when output tokens encode information from multiple patches. Four models are evaluated in closed-loop control on LIBERO~\\cite{liu2023libero}; $\\pi_{0}$ and OFT contribute to the CV diagnostic only.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/paper/fig_architecture_v4.pdf}\n\\caption{Vision connector architectures across four closed-loop VLAs, ordered by increasing compressibility fragility. Token-independent connectors ($\\pi_{0.5}$: linear; OpenVLA: MLP) yield low CV. Token-entangling connectors (X-VLA: BART encoder; SmolVLA: pixel-shuffle) create cross-token dependencies and higher CV, predicting threshold-graded or catastrophic pruning failure.}\n\\label{fig:architecture}\n\\end{figure*}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VLA models evaluated. Coupling indicates independent vs.\\ cross-token processing. $N$ = vision tokens input to the LLM. $^\\dagger$OFT is an OpenVLA fine-tuning variant, included for CV calibration (offline metrics only).}\n\\label{tab:model_properties}\n\\begin{tabular}{lrlcrll}\n\\toprule\nModel & Params & Connector & $N$ & CV & Coupling & Eval \\\\\n\\midrule\n$\\pi_{0.5}$ & 4B & Linear ($\\times\\!\\sqrt{d}$) & 768 & 0.055 & Indep.\\ & Closed-loop \\\\\nX-VLA & 0.9B & Linear + BART & 50 & 0.151 & Entangling & Closed-loop \\\\\nOpenVLA & 7B & 3-layer MLP & 256 & 0.215 & Indep.\\ & Closed-loop \\\\\nSmolVLA & 450M & Pixel-shuffle $4{\\times}4$ & 128 & 0.314 & Entangling & Closed-loop \\\\\n\\midrule\n$\\pi_{0}$ & 3.3B & Linear & 256 & 0.038 & Indep.\\ & Offline \\\\\nOFT$^\\dagger$ & 7B & 3-layer MLP & 512 & 0.219 & Indep.\\ & Offline \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Pruning Protocol}\n\\label{sec:pruning_protocol}\n\nGiven $N$ post-connector vision tokens $\\{t_1, \\ldots, t_N\\}$ with $t_i \\in \\mathbb{R}^d$, token pruning selects a subset of size $\\lfloor k \\cdot N \\rfloor$ for retention ratio $k \\in (0, 1]$ and discards the rest. Unselected tokens are physically removed and position IDs are re-indexed to close gaps. We prune between the vision connector output and the LLM backbone input to isolate the connector's effect on token information structure: pruning before the connector would alter its input distribution, confounding architectural analysis with input perturbation.\n\n\\paragraph{Importance scoring functions.}\nA scoring function $s\\colon \\mathbb{R}^d \\to \\mathbb{R}$ assigns each token an importance score; the top-$\\lfloor kN \\rfloor$ tokens by score are retained. We evaluate two strategies that bracket expected performance.\n\n\\textbf{L2-norm scoring} assigns each token its activation magnitude:\n\\begin{equation}\ns_{\\text{L2}}(t_i) = \\|t_i\\|_2\\,.\n\\label{eq:l2_score}\n\\end{equation}\nThe L2 norm serves as a proxy for information density: tokens with larger norms carry stronger activations that exert greater influence on downstream attention computation. This proxy is architecture-agnostic and requires no access to the LLM backbone. L2 scoring introduces a spatial bias, however, because nearby patches share visual content and produce correlated norms. Under aggressive pruning, L2 selection can concentrate retained tokens in a single high-activation region at the cost of spatial coverage. This bias is benign at high retention ratios but becomes pathological at low $k$ for models with near-uniform norm distributions (Section~\\ref{sec:cv_sensitivity}).\n\n\\textbf{Random subsampling} draws $\\lfloor kN \\rfloor$ tokens uniformly at random:\n\\begin{equation}\ns_{\\text{rand}}(t_i) \\sim \\mathcal{U}(0, 1)\\,.\n\\label{eq:random_score}\n\\end{equation}\nRandom selection provides the null hypothesis that all post-connector tokens are interchangeable. If L2 scoring cannot outperform random, the token norm distribution carries no exploitable signal. Random selection also preserves the spatial distribution of the original token set in expectation, making it the natural baseline for spatially uniform architectures. Its primary limitation is sampling variance across episodes, which we control through multi-seed evaluation (Section~\\ref{sec:exp_setup}).\n\nThe \\emph{importance margin} at ratio $k$ is defined as $\\Delta(k) = \\text{SR}_{\\text{L2}}(k) - \\text{SR}_{\\text{Random}}(k)$. A positive margin indicates that the norm distribution contains exploitable importance structure. A negative margin indicates that L2 selection is actively harmful, typically because spatial clustering outweighs the benefit of importance ranking. The sign and magnitude of the importance margin vary systematically with both connector CV and $k$ (Section~\\ref{sec:scaling_law}).\n\n\\paragraph{Attention-based alternatives.}\nAttention-based scoring functions estimate token importance from the LLM's internal attention weights. Three principal variants exist: (i)~\\emph{column-sum scoring} sums each vision token's received attention weight in the last transformer layer, capturing direct query-key dependencies at the final processing stage; (ii)~\\emph{cross-layer mean scoring} averages column-sum scores across all layers, aggregating importance signals over the full transformer stack; (iii)~\\emph{attention rollout} multiplies attention matrices layer by layer (adding identity matrices for residual connections) to approximate cumulative information flow from input tokens to the output. These methods rest on the premise that tokens receiving more attention contribute more to the model's prediction. Their primary limitation is computational: they require a full LLM forward pass and are backbone-specific. We focus on L2-norm and random scoring because they operate solely on the connector output, are backbone-agnostic, and suffice to reveal the connector-dependent importance structure that is our primary object of study. Attention entropy enters our analysis as a diagnostic metric (Section~\\ref{sec:cv_diagnostic}), not as a pruning criterion.\n\n\\paragraph{Retention ratio design space.}\nWe evaluate $k \\in \\{0.30, 0.50, 0.70, 0.75, 0.85, 0.90, 0.95\\}$, spanning from extreme compression (retaining 30\\% of tokens) to conservative trimming (retaining 95\\%). This range captures the full degradation profile of each connector type. At one end, $k = 0.95$ tests whether even minimal removal is tolerable (e.g., 6 of 128 tokens for SmolVLA). At the other, $k = 0.30$ probes behavior under severe information loss (e.g., 15 of 50 tokens for X-VLA). The intermediate values are chosen to identify \\emph{cliff zones}: narrow $k$ intervals where success rate drops discontinuously rather than degrading proportionally. A cliff zone indicates a critical token density below which the model's visual representation breaks down. Different connector architectures exhibit cliffs at qualitatively different retention ratios: pixel-shuffle connectors cliff at $k = 0.95$ (the most conservative ratio tested), BART-encoded connectors near $k \\approx 0.85$, and MLP connectors degrade without a sharp cliff at any tested ratio. For targeted models where initial results indicate a cliff, we add finer-grained ratios ($k \\in \\{0.80, 0.925\\}$) to localize the transition boundary (Section~\\ref{sec:two_axis}).\n\n\\subsection{Compressibility Diagnostic: Importance CV}\n\\label{sec:cv_diagnostic}\n\nWe seek a zero-cost diagnostic that predicts a model's pruning tolerance without running closed-loop evaluation. The coefficient of variation (CV) of post-connector token L2 norms provides this:\n\\begin{equation}\n\\text{CV} = \\frac{\\sigma\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}{\\mu\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}\n\\label{eq:cv}\n\\end{equation}\nwhere $\\sigma$ and $\\mu$ denote the standard deviation and mean over all $N$ post-connector tokens from a single forward pass. CV requires no labeled data, no downstream task evaluation, and no access to the LLM backbone.\n\n\\paragraph{The CV spectrum.}\nCV captures a continuous ordering across six models and three connector families:\n\\begin{equation}\n\\begin{split}\n\\underbrace{\\pi_0\\,(0.038) \\;<\\; \\pi_{0.5}\\,(0.055)}_{\\text{linear proj.}} &\\;<\\; \\underbrace{\\text{X-VLA}\\,(0.151)}_{\\text{linear + BART}} \\\\\n&\\;<\\; \\underbrace{\\text{OpenVLA}\\,(0.215) \\;\\approx\\; \\text{OFT}\\,(0.219)}_{\\text{MLP proj.}} \\;<\\; \\underbrace{\\text{SmolVLA}\\,(0.314)}_{\\text{pixel-shuffle}}\n\\end{split}\n\\label{eq:cv_spectrum}\n\\end{equation}\nThis ordering reflects the degree of cross-token mixing in each connector. Pure linear projections process patches independently, producing near-uniform norms (CV$\\,{<}\\,$0.06). MLP projectors apply nonlinear transformations per token, amplifying norm variance through activation functions and layered composition (CV$\\,{\\approx}\\,$0.22). Pixel-shuffle folds $4 \\times 4$ patch blocks into single tokens by channel concatenation, creating maximal cross-patch entanglement and the highest norm heterogeneity (CV$\\,{=}\\,$0.314). X-VLA occupies an intermediate position: its linear projection is followed by a 12-layer BART encoder~\\cite{lewis2020bart} that introduces cross-token attention, raising CV from what a pure linear projection would produce (${\\sim}$0.04) to 0.151.\n\n\\paragraph{CV as pruning tolerance predictor.}\nCV measures the dispersion of token importance under the L2-norm proxy. High CV indicates that some tokens carry substantially larger norms than others; these high-norm tokens can be identified and retained while low-norm tokens are removed with limited information loss. Low CV indicates near-uniform norms: no token subset is dispensable because all tokens contribute comparably. Pruning a low-CV model is equivalent to downsampling a uniform signal, where the spatial pattern of removal matters more than which specific tokens are selected by importance.\n\nCV also predicts the \\emph{optimal pruning strategy}, not only the tolerance ceiling. When CV is low ($< 0.15$), L2-norm ranking captures spatial artifacts rather than genuine importance differences, and random selection outperforms L2 by preserving spatial coverage. When CV is high ($> 0.20$), L2-norm ranking exploits real importance differentiation and outperforms random. The importance margin $\\Delta(\\text{L2} - \\text{Random})$ increases monotonically with CV at both $k = 0.5$ and $k = 0.7$ across three closed-loop models ($\\pi_{0.5}$, X-VLA, OpenVLA), confirming that CV captures a structural property of the connector rather than an artifact of a particular retention ratio (Section~\\ref{sec:scaling_law}).\n\n\\paragraph{Complementary role of attention entropy.}\nAttention entropy, defined as the mean Shannon entropy of the LLM's attention weight distribution over vision tokens, provides a complementary but less discriminative signal. Entropy measures how uniformly the LLM attends across vision tokens: high entropy indicates distributed attention, low entropy indicates selective focus. Three models with qualitatively different pruning behaviors, however, cluster within a narrow entropy band: $\\pi_{0.5}$ (0.666), X-VLA (0.614), and OpenVLA (0.661) span only 0.05 in entropy despite spanning 0.055 to 0.215 in CV and exhibiting uniformly critical, threshold-graded, and smooth graded pruning responses respectively. SmolVLA's entropy (0.952) is near-maximal, yet it is the least pruning-tolerant model. The discrepancy arises because entropy reflects the LLM's \\emph{reading pattern} (how attention is distributed across tokens), while CV reflects the connector's \\emph{writing pattern} (how information is distributed into tokens). The connector's output structure, not the downstream attention allocation, determines pruning robustness. We report entropy values alongside CV in our taxonomy (Table~\\ref{tab:taxonomy}) as a mechanistic supplement, but use CV as the primary diagnostic throughout.\n\n\\subsection{Vision Token Re-encoder (VTR)}\n\\label{sec:vtr}\n\nHard pruning fails for token-entangling connectors because removing any token destroys spatially distributed information. VTR addresses this through learned re-encoding rather than deletion.\n\n\\paragraph{Architecture.}\nVTR inserts a 2-layer cross-attention module between the vision connector output and the LLM backbone input. Each layer uses 12 attention heads with dropout 0.1. A set of $M$ learned query vectors attends over all $N$ source tokens via standard multi-head cross-attention, producing $M$ compressed tokens as input to the LLM. The compression ratio is controlled by $M \\in \\{16, 32, 64, 96, 128\\}$; $M{=}N$ serves as a passthrough control.\n\n\\paragraph{Training and cost.}\nThe module adds ${\\sim}$22M trainable parameters ($<$5\\% of SmolVLA, the smallest VLA tested) and is trained end-to-end: compressor and action head parameters are jointly optimized. Architecture and training hyperparameters are detailed in Appendix~\\ref{app:smart_compress_details}.\n",
    "structuredPatch": [
      {
        "oldStart": 98,
        "oldLines": 7,
        "newStart": 98,
        "newLines": 7,
        "lines": [
          " CV also predicts the \\emph{optimal pruning strategy}, not only the tolerance ceiling. When CV is low ($< 0.15$), L2-norm ranking captures spatial artifacts rather than genuine importance differences, and random selection outperforms L2 by preserving spatial coverage. When CV is high ($> 0.20$), L2-norm ranking exploits real importance differentiation and outperforms random. The importance margin $\\Delta(\\text{L2} - \\text{Random})$ increases monotonically with CV at both $k = 0.5$ and $k = 0.7$ across three closed-loop models ($\\pi_{0.5}$, X-VLA, OpenVLA), confirming that CV captures a structural property of the connector rather than an artifact of a particular retention ratio (Section~\\ref{sec:scaling_law}).",
          " ",
          " \\paragraph{Complementary role of attention entropy.}",
          "-Attention entropy, defined as the mean Shannon entropy of the LLM's attention weight distribution over vision tokens, provides a complementary but less discriminative signal. Entropy measures how uniformly the LLM attends across vision tokens: high entropy indicates distributed attention, low entropy indicates selective focus. Three models with qualitatively different pruning behaviors, however, cluster within a narrow entropy band: $\\pi_{0.5}$ (0.666), X-VLA (0.614), and OpenVLA (0.661) span only 0.05 in entropy despite spanning 0.055 to 0.215 in CV and exhibiting uniformly critical, threshold-graded, and smooth graded pruning responses respectively. SmolVLA's entropy (0.952) is near-maximal, yet it is the least pruning-tolerant model. The discrepancy arises because entropy reflects the LLM's \\emph{reading pattern} (how attention is distributed across tokens), while CV reflects the connector's \\emph{writing pattern} (how information is distributed into tokens). The connector's output structure, not the downstream attention allocation, determines pruning robustness. We report entropy values alongside CV in our taxonomy (Table~\\ref{tab:taxonomy}) as a mechanistic supplement, but use CV as the primary diagnostic throughout.",
          "+Attention entropy, defined as the mean Shannon entropy of the LLM's attention weight distribution over vision tokens, provides a complementary but less discriminative signal. Entropy measures how uniformly the LLM attends across vision tokens: high entropy indicates distributed attention, low entropy indicates selective focus. Three models with qualitatively different pruning behaviors, however, cluster within a narrow entropy band: $\\pi_{0.5}$ (0.666), X-VLA (0.614), and OpenVLA (0.661) span only 0.05 in entropy despite spanning 0.055 to 0.215 in CV and exhibiting uniformly critical, threshold-graded, and smooth graded pruning responses respectively. SmolVLA's entropy (0.952) is near-maximal, yet it is the least pruning-tolerant model. The discrepancy arises because entropy reflects the LLM's \\emph{reading pattern} (how attention is distributed across tokens), while CV reflects the connector's \\emph{writing pattern} (how information is distributed into tokens). The connector's output structure, not the downstream attention allocation, determines pruning robustness. We report entropy values alongside CV in our taxonomy (Table~\\ref{tab:model_properties}) as a mechanistic supplement, but use CV as the primary diagnostic throughout.",
          " ",
          " \\subsection{Vision Token Re-encoder (VTR)}",
          " \\label{sec:vtr}"
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

_source line 41_

<details open><summary>🔧 Tool call — Edit · `toolu_01LPs2QihkodRBt4GtNGGCuK`</summary>

```json
{
  "replace_all": true,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
  "old_string": "(Section~\\ref{sec:scaling_law})",
  "new_string": "(Section~\\ref{sec:cv_sensitivity})"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "uuid": "6dbfb5a0-c0e0-41a9-b636-6e8198e2ed0d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KEkMdnUQ7HSRr612aCDuDb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 594,
      "cache_read_input_tokens": 39766,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 594
      },
      "output_tokens": 71,
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

_source line 42 · 2026-05-28T18:20:00.663Z_

<details><summary>↩ Tool result · `toolu_01LPs2QihkodRBt4GtNGGCuK`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex has been updated. All occurrences were successfully replaced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "uuid": "c4d46d7b-dca1-4c70-b1cb-71e6165a79bb",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
    "oldString": "(Section~\\ref{sec:scaling_law})",
    "newString": "(Section~\\ref{sec:cv_sensitivity})",
    "originalFile": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Models and Connectors}\n\\label{sec:models}\n\nWe evaluate token pruning across six VLA architectures spanning three vision connector families (Table~\\ref{tab:model_properties}; Figure~\\ref{fig:architecture}). These connectors differ in whether they process ViT patches independently or create cross-token dependencies.\n\n\\textbf{Linear projection} applies a single matrix multiplication per patch. $\\pi_{0}$~\\cite{black2024pi0} projects 256 patches through a linear layer; $\\pi_{0.5}$~\\cite{black2025pi05} uses a $\\times\\!\\sqrt{d}$-scaled linear projection across 768 tokens from three image slots (two active cameras in LIBERO; CV$\\,{<}\\,$0.06).\n\n\\textbf{MLP projector} maps each patch independently through a multi-layer perceptron. OpenVLA~\\cite{kim2024openvla} uses a three-layer MLP (256 tokens; CV$\\,{=}\\,$0.215); OFT~\\cite{kim2025openoft} shares the same connector (512 tokens; CV$\\,{=}\\,$0.219).\n\n\\textbf{Token-entangling connectors} introduce cross-token dependencies. X-VLA~\\cite{zheng2025xvla} feeds tokens through a 12-layer BART encoder~\\cite{lewis2020bart} (50 tokens). SmolVLA~\\cite{shukor2025smolvla} applies pixel-shuffle $4{\\times}4$ folding, concatenating 16 contiguous patches per output token (128 tokens).\n\nWe classify coupling as \\emph{independent} when each output token depends on a single input patch, and \\emph{entangling} when output tokens encode information from multiple patches. Four models are evaluated in closed-loop control on LIBERO~\\cite{liu2023libero}; $\\pi_{0}$ and OFT contribute to the CV diagnostic only.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/paper/fig_architecture_v4.pdf}\n\\caption{Vision connector architectures across four closed-loop VLAs, ordered by increasing compressibility fragility. Token-independent connectors ($\\pi_{0.5}$: linear; OpenVLA: MLP) yield low CV. Token-entangling connectors (X-VLA: BART encoder; SmolVLA: pixel-shuffle) create cross-token dependencies and higher CV, predicting threshold-graded or catastrophic pruning failure.}\n\\label{fig:architecture}\n\\end{figure*}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VLA models evaluated. Coupling indicates independent vs.\\ cross-token processing. $N$ = vision tokens input to the LLM. $^\\dagger$OFT is an OpenVLA fine-tuning variant, included for CV calibration (offline metrics only).}\n\\label{tab:model_properties}\n\\begin{tabular}{lrlcrll}\n\\toprule\nModel & Params & Connector & $N$ & CV & Coupling & Eval \\\\\n\\midrule\n$\\pi_{0.5}$ & 4B & Linear ($\\times\\!\\sqrt{d}$) & 768 & 0.055 & Indep.\\ & Closed-loop \\\\\nX-VLA & 0.9B & Linear + BART & 50 & 0.151 & Entangling & Closed-loop \\\\\nOpenVLA & 7B & 3-layer MLP & 256 & 0.215 & Indep.\\ & Closed-loop \\\\\nSmolVLA & 450M & Pixel-shuffle $4{\\times}4$ & 128 & 0.314 & Entangling & Closed-loop \\\\\n\\midrule\n$\\pi_{0}$ & 3.3B & Linear & 256 & 0.038 & Indep.\\ & Offline \\\\\nOFT$^\\dagger$ & 7B & 3-layer MLP & 512 & 0.219 & Indep.\\ & Offline \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Pruning Protocol}\n\\label{sec:pruning_protocol}\n\nGiven $N$ post-connector vision tokens $\\{t_1, \\ldots, t_N\\}$ with $t_i \\in \\mathbb{R}^d$, token pruning selects a subset of size $\\lfloor k \\cdot N \\rfloor$ for retention ratio $k \\in (0, 1]$ and discards the rest. Unselected tokens are physically removed and position IDs are re-indexed to close gaps. We prune between the vision connector output and the LLM backbone input to isolate the connector's effect on token information structure: pruning before the connector would alter its input distribution, confounding architectural analysis with input perturbation.\n\n\\paragraph{Importance scoring functions.}\nA scoring function $s\\colon \\mathbb{R}^d \\to \\mathbb{R}$ assigns each token an importance score; the top-$\\lfloor kN \\rfloor$ tokens by score are retained. We evaluate two strategies that bracket expected performance.\n\n\\textbf{L2-norm scoring} assigns each token its activation magnitude:\n\\begin{equation}\ns_{\\text{L2}}(t_i) = \\|t_i\\|_2\\,.\n\\label{eq:l2_score}\n\\end{equation}\nThe L2 norm serves as a proxy for information density: tokens with larger norms carry stronger activations that exert greater influence on downstream attention computation. This proxy is architecture-agnostic and requires no access to the LLM backbone. L2 scoring introduces a spatial bias, however, because nearby patches share visual content and produce correlated norms. Under aggressive pruning, L2 selection can concentrate retained tokens in a single high-activation region at the cost of spatial coverage. This bias is benign at high retention ratios but becomes pathological at low $k$ for models with near-uniform norm distributions (Section~\\ref{sec:cv_sensitivity}).\n\n\\textbf{Random subsampling} draws $\\lfloor kN \\rfloor$ tokens uniformly at random:\n\\begin{equation}\ns_{\\text{rand}}(t_i) \\sim \\mathcal{U}(0, 1)\\,.\n\\label{eq:random_score}\n\\end{equation}\nRandom selection provides the null hypothesis that all post-connector tokens are interchangeable. If L2 scoring cannot outperform random, the token norm distribution carries no exploitable signal. Random selection also preserves the spatial distribution of the original token set in expectation, making it the natural baseline for spatially uniform architectures. Its primary limitation is sampling variance across episodes, which we control through multi-seed evaluation (Section~\\ref{sec:exp_setup}).\n\nThe \\emph{importance margin} at ratio $k$ is defined as $\\Delta(k) = \\text{SR}_{\\text{L2}}(k) - \\text{SR}_{\\text{Random}}(k)$. A positive margin indicates that the norm distribution contains exploitable importance structure. A negative margin indicates that L2 selection is actively harmful, typically because spatial clustering outweighs the benefit of importance ranking. The sign and magnitude of the importance margin vary systematically with both connector CV and $k$ (Section~\\ref{sec:scaling_law}).\n\n\\paragraph{Attention-based alternatives.}\nAttention-based scoring functions estimate token importance from the LLM's internal attention weights. Three principal variants exist: (i)~\\emph{column-sum scoring} sums each vision token's received attention weight in the last transformer layer, capturing direct query-key dependencies at the final processing stage; (ii)~\\emph{cross-layer mean scoring} averages column-sum scores across all layers, aggregating importance signals over the full transformer stack; (iii)~\\emph{attention rollout} multiplies attention matrices layer by layer (adding identity matrices for residual connections) to approximate cumulative information flow from input tokens to the output. These methods rest on the premise that tokens receiving more attention contribute more to the model's prediction. Their primary limitation is computational: they require a full LLM forward pass and are backbone-specific. We focus on L2-norm and random scoring because they operate solely on the connector output, are backbone-agnostic, and suffice to reveal the connector-dependent importance structure that is our primary object of study. Attention entropy enters our analysis as a diagnostic metric (Section~\\ref{sec:cv_diagnostic}), not as a pruning criterion.\n\n\\paragraph{Retention ratio design space.}\nWe evaluate $k \\in \\{0.30, 0.50, 0.70, 0.75, 0.85, 0.90, 0.95\\}$, spanning from extreme compression (retaining 30\\% of tokens) to conservative trimming (retaining 95\\%). This range captures the full degradation profile of each connector type. At one end, $k = 0.95$ tests whether even minimal removal is tolerable (e.g., 6 of 128 tokens for SmolVLA). At the other, $k = 0.30$ probes behavior under severe information loss (e.g., 15 of 50 tokens for X-VLA). The intermediate values are chosen to identify \\emph{cliff zones}: narrow $k$ intervals where success rate drops discontinuously rather than degrading proportionally. A cliff zone indicates a critical token density below which the model's visual representation breaks down. Different connector architectures exhibit cliffs at qualitatively different retention ratios: pixel-shuffle connectors cliff at $k = 0.95$ (the most conservative ratio tested), BART-encoded connectors near $k \\approx 0.85$, and MLP connectors degrade without a sharp cliff at any tested ratio. For targeted models where initial results indicate a cliff, we add finer-grained ratios ($k \\in \\{0.80, 0.925\\}$) to localize the transition boundary (Section~\\ref{sec:two_axis}).\n\n\\subsection{Compressibility Diagnostic: Importance CV}\n\\label{sec:cv_diagnostic}\n\nWe seek a zero-cost diagnostic that predicts a model's pruning tolerance without running closed-loop evaluation. The coefficient of variation (CV) of post-connector token L2 norms provides this:\n\\begin{equation}\n\\text{CV} = \\frac{\\sigma\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}{\\mu\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}\n\\label{eq:cv}\n\\end{equation}\nwhere $\\sigma$ and $\\mu$ denote the standard deviation and mean over all $N$ post-connector tokens from a single forward pass. CV requires no labeled data, no downstream task evaluation, and no access to the LLM backbone.\n\n\\paragraph{The CV spectrum.}\nCV captures a continuous ordering across six models and three connector families:\n\\begin{equation}\n\\begin{split}\n\\underbrace{\\pi_0\\,(0.038) \\;<\\; \\pi_{0.5}\\,(0.055)}_{\\text{linear proj.}} &\\;<\\; \\underbrace{\\text{X-VLA}\\,(0.151)}_{\\text{linear + BART}} \\\\\n&\\;<\\; \\underbrace{\\text{OpenVLA}\\,(0.215) \\;\\approx\\; \\text{OFT}\\,(0.219)}_{\\text{MLP proj.}} \\;<\\; \\underbrace{\\text{SmolVLA}\\,(0.314)}_{\\text{pixel-shuffle}}\n\\end{split}\n\\label{eq:cv_spectrum}\n\\end{equation}\nThis ordering reflects the degree of cross-token mixing in each connector. Pure linear projections process patches independently, producing near-uniform norms (CV$\\,{<}\\,$0.06). MLP projectors apply nonlinear transformations per token, amplifying norm variance through activation functions and layered composition (CV$\\,{\\approx}\\,$0.22). Pixel-shuffle folds $4 \\times 4$ patch blocks into single tokens by channel concatenation, creating maximal cross-patch entanglement and the highest norm heterogeneity (CV$\\,{=}\\,$0.314). X-VLA occupies an intermediate position: its linear projection is followed by a 12-layer BART encoder~\\cite{lewis2020bart} that introduces cross-token attention, raising CV from what a pure linear projection would produce (${\\sim}$0.04) to 0.151.\n\n\\paragraph{CV as pruning tolerance predictor.}\nCV measures the dispersion of token importance under the L2-norm proxy. High CV indicates that some tokens carry substantially larger norms than others; these high-norm tokens can be identified and retained while low-norm tokens are removed with limited information loss. Low CV indicates near-uniform norms: no token subset is dispensable because all tokens contribute comparably. Pruning a low-CV model is equivalent to downsampling a uniform signal, where the spatial pattern of removal matters more than which specific tokens are selected by importance.\n\nCV also predicts the \\emph{optimal pruning strategy}, not only the tolerance ceiling. When CV is low ($< 0.15$), L2-norm ranking captures spatial artifacts rather than genuine importance differences, and random selection outperforms L2 by preserving spatial coverage. When CV is high ($> 0.20$), L2-norm ranking exploits real importance differentiation and outperforms random. The importance margin $\\Delta(\\text{L2} - \\text{Random})$ increases monotonically with CV at both $k = 0.5$ and $k = 0.7$ across three closed-loop models ($\\pi_{0.5}$, X-VLA, OpenVLA), confirming that CV captures a structural property of the connector rather than an artifact of a particular retention ratio (Section~\\ref{sec:scaling_law}).\n\n\\paragraph{Complementary role of attention entropy.}\nAttention entropy, defined as the mean Shannon entropy of the LLM's attention weight distribution over vision tokens, provides a complementary but less discriminative signal. Entropy measures how uniformly the LLM attends across vision tokens: high entropy indicates distributed attention, low entropy indicates selective focus. Three models with qualitatively different pruning behaviors, however, cluster within a narrow entropy band: $\\pi_{0.5}$ (0.666), X-VLA (0.614), and OpenVLA (0.661) span only 0.05 in entropy despite spanning 0.055 to 0.215 in CV and exhibiting uniformly critical, threshold-graded, and smooth graded pruning responses respectively. SmolVLA's entropy (0.952) is near-maximal, yet it is the least pruning-tolerant model. The discrepancy arises because entropy reflects the LLM's \\emph{reading pattern} (how attention is distributed across tokens), while CV reflects the connector's \\emph{writing pattern} (how information is distributed into tokens). The connector's output structure, not the downstream attention allocation, determines pruning robustness. We report entropy values alongside CV in our taxonomy (Table~\\ref{tab:model_properties}) as a mechanistic supplement, but use CV as the primary diagnostic throughout.\n\n\\subsection{Vision Token Re-encoder (VTR)}\n\\label{sec:vtr}\n\nHard pruning fails for token-entangling connectors because removing any token destroys spatially distributed information. VTR addresses this through learned re-encoding rather than deletion.\n\n\\paragraph{Architecture.}\nVTR inserts a 2-layer cross-attention module between the vision connector output and the LLM backbone input. Each layer uses 12 attention heads with dropout 0.1. A set of $M$ learned query vectors attends over all $N$ source tokens via standard multi-head cross-attention, producing $M$ compressed tokens as input to the LLM. The compression ratio is controlled by $M \\in \\{16, 32, 64, 96, 128\\}$; $M{=}N$ serves as a passthrough control.\n\n\\paragraph{Training and cost.}\nThe module adds ${\\sim}$22M trainable parameters ($<$5\\% of SmolVLA, the smallest VLA tested) and is trained end-to-end: compressor and action head parameters are jointly optimized. Architecture and training hyperparameters are detailed in Appendix~\\ref{app:smart_compress_details}.\n",
    "structuredPatch": [
      {
        "oldStart": 63,
        "oldLines": 7,
        "newStart": 63,
        "newLines": 7,
        "lines": [
          " \\end{equation}",
          " Random selection provides the null hypothesis that all post-connector tokens are interchangeable. If L2 scoring cannot outperform random, the token norm distribution carries no exploitable signal. Random selection also preserves the spatial distribution of the original token set in expectation, making it the natural baseline for spatially uniform architectures. Its primary limitation is sampling variance across episodes, which we control through multi-seed evaluation (Section~\\ref{sec:exp_setup}).",
          " ",
          "-The \\emph{importance margin} at ratio $k$ is defined as $\\Delta(k) = \\text{SR}_{\\text{L2}}(k) - \\text{SR}_{\\text{Random}}(k)$. A positive margin indicates that the norm distribution contains exploitable importance structure. A negative margin indicates that L2 selection is actively harmful, typically because spatial clustering outweighs the benefit of importance ranking. The sign and magnitude of the importance margin vary systematically with both connector CV and $k$ (Section~\\ref{sec:scaling_law}).",
          "+The \\emph{importance margin} at ratio $k$ is defined as $\\Delta(k) = \\text{SR}_{\\text{L2}}(k) - \\text{SR}_{\\text{Random}}(k)$. A positive margin indicates that the norm distribution contains exploitable importance structure. A negative margin indicates that L2 selection is actively harmful, typically because spatial clustering outweighs the benefit of importance ranking. The sign and magnitude of the importance margin vary systematically with both connector CV and $k$ (Section~\\ref{sec:cv_sensitivity}).",
          " ",
          " \\paragraph{Attention-based alternatives.}",
          " Attention-based scoring functions estimate token importance from the LLM's internal attention weights. Three principal variants exist: (i)~\\emph{column-sum scoring} sums each vision token's received attention weight in the last transformer layer, capturing direct query-key dependencies at the final processing stage; (ii)~\\emph{cross-layer mean scoring} averages column-sum scores across all layers, aggregating importance signals over the full transformer stack; (iii)~\\emph{attention rollout} multiplies attention matrices layer by layer (adding identity matrices for residual connections) to approximate cumulative information flow from input tokens to the output. These methods rest on the premise that tokens receiving more attention contribute more to the model's prediction. Their primary limitation is computational: they require a full LLM forward pass and are backbone-specific. We focus on L2-norm and random scoring because they operate solely on the connector output, are backbone-agnostic, and suffice to reveal the connector-dependent importance structure that is our primary object of study. Attention entropy enters our analysis as a diagnostic metric (Section~\\ref{sec:cv_diagnostic}), not as a pruning criterion."
        ]
      },
      {
        "oldStart": 95,
        "oldLines": 7,
        "newStart": 95,
        "newLines": 7,
        "lines": [
          " \\paragraph{CV as pruning tolerance predictor.}",
          " CV measures the dispersion of token importance under the L2-norm proxy. High CV indicates that some tokens carry substantially larger norms than others; these high-norm tokens can be identified and retained while low-norm tokens are removed with limited information loss. Low CV indicates near-uniform norms: no token subset is dispensable because all tokens contribute comparably. Pruning a low-CV model is equivalent to downsampling a uniform signal, where the spatial pattern of removal matters more than which specific tokens are selected by importance.",
          " ",
          "-CV also predicts the \\emph{optimal pruning strategy}, not only the tolerance ceiling. When CV is low ($< 0.15$), L2-norm ranking captures spatial artifacts rather than genuine importance differences, and random selection outperforms L2 by preserving spatial coverage. When CV is high ($> 0.20$), L2-norm ranking exploits real importance differentiation and outperforms random. The importance margin $\\Delta(\\text{L2} - \\text{Random})$ increases monotonically with CV at both $k = 0.5$ and $k = 0.7$ across three closed-loop models ($\\pi_{0.5}$, X-VLA, OpenVLA), confirming that CV captures a structural property of the connector rather than an artifact of a particular retention ratio (Section~\\ref{sec:scaling_law}).",
          "+CV also predicts the \\emph{optimal pruning strategy}, not only the tolerance ceiling. When CV is low ($< 0.15$), L2-norm ranking captures spatial artifacts rather than genuine importance differences, and random selection outperforms L2 by preserving spatial coverage. When CV is high ($> 0.20$), L2-norm ranking exploits real importance differentiation and outperforms random. The importance margin $\\Delta(\\text{L2} - \\text{Random})$ increases monotonically with CV at both $k = 0.5$ and $k = 0.7$ across three closed-loop models ($\\pi_{0.5}$, X-VLA, OpenVLA), confirming that CV captures a structural property of the connector rather than an artifact of a particular retention ratio (Section~\\ref{sec:cv_sensitivity}).",
          " ",
          " \\paragraph{Complementary role of attention entropy.}",
          " Attention entropy, defined as the mean Shannon entropy of the LLM's attention weight distribution over vision tokens, provides a complementary but less discriminative signal. Entropy measures how uniformly the LLM attends across vision tokens: high entropy indicates distributed attention, low entropy indicates selective focus. Three models with qualitatively different pruning behaviors, however, cluster within a narrow entropy band: $\\pi_{0.5}$ (0.666), X-VLA (0.614), and OpenVLA (0.661) span only 0.05 in entropy despite spanning 0.055 to 0.215 in CV and exhibiting uniformly critical, threshold-graded, and smooth graded pruning responses respectively. SmolVLA's entropy (0.952) is near-maximal, yet it is the least pruning-tolerant model. The discrepancy arises because entropy reflects the LLM's \\emph{reading pattern} (how attention is distributed across tokens), while CV reflects the connector's \\emph{writing pattern} (how information is distributed into tokens). The connector's output structure, not the downstream attention allocation, determines pruning robustness. We report entropy values alongside CV in our taxonomy (Table~\\ref{tab:model_properties}) as a mechanistic supplement, but use CV as the primary diagnostic throughout."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": true
  }
}
```

</details>

---

### Assistant

_source line 43_

4 处全部替换完成。重新编译验证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "uuid": "71f06e5e-b77c-43c9-95b8-1c0c6ba38310",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rypav4weSYPFuaHpKmWWcc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 236,
      "cache_read_input_tokens": 40360,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 236
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

_source line 44_

<details open><summary>🔧 Tool call — Bash · `toolu_014CKMqsoREGBhNM8gL81oir`</summary>

```json
{
  "command": "latexmk -pdf -interaction=nonstopmode main.tex 2>&1 | tail -15",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "uuid": "1241c0d9-a008-401d-bea7-5c57f13f2cfe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rypav4weSYPFuaHpKmWWcc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 236,
      "cache_read_input_tokens": 40360,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 236
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

_source line 45 · 2026-05-28T18:20:07.218Z_

<details><summary>↩ Tool result · `toolu_014CKMqsoREGBhNM8gL81oir`</summary>

```text
sr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texliv
e/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on main.pdf (33 pages, 1304061 bytes).
Transcript written on main.log.
Latexmk: Getting log file 'main.log'
Latexmk: Examining 'main.fls'
Latexmk: Examining 'main.log'
Latexmk: Found input bbl file 'main.bbl'
Latexmk: Log file says output to 'main.pdf'
Latexmk: Using bibtex to make bibliography file(s).
  ===Source file 'main.bbl' for 'pdflatex'
Latexmk: Found bibliography file(s):
  ./references.bib
Latexmk: All targets (main.pdf) are up-to-date
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "uuid": "1332dda7-1530-42e3-8013-f61adda671fd",
  "tool_use_result": {
    "stdout": "sr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texliv\ne/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on main.pdf (33 pages, 1304061 bytes).\nTranscript written on main.log.\nLatexmk: Getting log file 'main.log'\nLatexmk: Examining 'main.fls'\nLatexmk: Examining 'main.log'\nLatexmk: Found input bbl file 'main.bbl'\nLatexmk: Log file says output to 'main.pdf'\nLatexmk: Using bibtex to make bibliography file(s).\n  ===Source file 'main.bbl' for 'pdflatex'\nLatexmk: Found bibliography file(s):\n  ./references.bib\nLatexmk: All targets (main.pdf) are up-to-date",
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

_source line 46_

<details open><summary>🔧 Tool call — Bash · `toolu_018AR9e3tkWDp6T8agBxba47`</summary>

```json
{
  "command": "grep -i \"undefined\\|multiply defined\" main.log | grep -v \"Font\\|pdf\" | sort -u"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "uuid": "d4c0e2fa-e8ff-4e2d-a568-f51e6d12d901",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VhCcHkbSSHryntSPxwHwt6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 383,
      "cache_read_input_tokens": 40596,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 383
      },
      "output_tokens": 38,
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

_source line 47 · 2026-05-28T18:20:10.777Z_

<details><summary>↩ Tool result · `toolu_018AR9e3tkWDp6T8agBxba47`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "uuid": "8b01cc8c-29bc-413f-b66c-5eb61c7df354",
  "tool_use_result": {
    "stdout": "",
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

_source line 48_

<details open><summary>🔧 Tool call — Bash · `toolu_014NCdEPU8Ymx6wrRZUUE8JV`</summary>

```json
{
  "command": "grep -c \"LaTeX Warning.*undefined\" main.log; grep -c \"??\" main.pdf 2>/dev/null || pdftotext main.pdf - 2>/dev/null | grep -c \"??\" || echo \"pdftotext not available\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "uuid": "3c0017da-c23a-43ff-b908-bbada25214f4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VhCcHkbSSHryntSPxwHwt6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 383,
      "cache_read_input_tokens": 40596,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 383
      },
      "output_tokens": 38,
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

_source line 49 · 2026-05-28T18:20:12.089Z_

<details><summary>↩ Tool result · `toolu_014NCdEPU8Ymx6wrRZUUE8JV`</summary>

```text
0
25
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "uuid": "812d668c-d7bb-4953-9dcb-adde6b2c54b6",
  "tool_use_result": {
    "stdout": "0\n25",
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

_source line 50_

<details open><summary>🔧 Tool call — Bash · `toolu_01RmKSbNptVsLacgCJhAct9L`</summary>

```json
{
  "command": "pdftotext main.pdf - 2>/dev/null | grep -n \"??\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "uuid": "87f95083-5224-468c-900d-cc9a54868e32",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011eKykDBoZG1zGWaCQ7pABQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 243,
      "cache_read_input_tokens": 40979,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 243
      },
      "output_tokens": 54,
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

_source line 51 · 2026-05-28T18:20:15.355Z_

<details><summary>↩ Tool result · `toolu_01RmKSbNptVsLacgCJhAct9L`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "uuid": "eee2c949-a704-4b92-877f-ffc0c162b1a3",
  "tool_use_result": {
    "stdout": "",
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

_source line 52_

<details open><summary>🔧 Tool call — Bash · `toolu_01Dev8bd4RN42CDu12WsRqrM`</summary>

```json
{
  "command": "pdftotext main.pdf /tmp/main_check.txt 2>/dev/null && grep \"??\" /tmp/main_check.txt | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "uuid": "93fc869e-52b8-44a4-9875-e604662536f0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017woGTePryHE4GMBJoMKv2b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 94,
      "cache_read_input_tokens": 41222,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 94
      },
      "output_tokens": 42,
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

_source line 53 · 2026-05-28T18:20:18.802Z_

<details><summary>↩ Tool result · `toolu_01Dev8bd4RN42CDu12WsRqrM`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "uuid": "15615acc-ea9d-4ed3-875d-228ad3b1d2b4",
  "tool_use_result": {
    "stdout": "",
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

_source line 54_

0 个 undefined reference warnings，PDF 中无 `??` 残留。33 页，1.3MB。

结果：
- `sec:openvla_results` → `sec:exp_setup`（method.tex:64）
- `sec:scaling_law` × 2 → `sec:cv_sensitivity`（method.tex:66, 98）
- `tab:taxonomy` → `tab:model_properties`（method.tex:101）

所有修改在 `method.tex`，未触碰 `experiments.tex`。编译干净，0 个 undefined reference。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "uuid": "caa6d7b2-0b16-4f7a-a24b-83939af6a273",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CCrR9QFrGC3XaLSdQEgMc1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 107,
      "cache_read_input_tokens": 41316,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 107
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

_source line 55_

0 个 undefined reference warnings，PDF 中无 `??` 残留。33 页，1.3MB。

结果：
- `sec:openvla_results` → `sec:exp_setup`（method.tex:64）
- `sec:scaling_law` × 2 → `sec:cv_sensitivity`（method.tex:66, 98）
- `tab:taxonomy` → `tab:model_properties`（method.tex:101）

所有修改在 `method.tex`，未触碰 `experiments.tex`。编译干净，0 个 undefined reference。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 132133,
  "duration_api_ms": 128125,
  "num_turns": 20,
  "stop_reason": "end_turn",
  "session_id": "e581efcd-7bff-40ac-bbd5-f451301ef019",
  "total_cost_usd": 0.5415785,
  "usage": {
    "input_tokens": 146,
    "cache_creation_input_tokens": 29578,
    "cache_read_input_tokens": 462864,
    "output_tokens": 4880,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 29578,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 151,
        "cache_read_input_tokens": 41316,
        "cache_creation_input_tokens": 107,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 107
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2479,
      "outputTokens": 15,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002554,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 146,
      "outputTokens": 4880,
      "cacheReadInputTokens": 462864,
      "cacheCreationInputTokens": 29578,
      "webSearchRequests": 0,
      "costUSD": 0.5390244999999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "36f47dc3-3e6a-45cb-8263-ee05c28825ac"
}
```

</details>

---
