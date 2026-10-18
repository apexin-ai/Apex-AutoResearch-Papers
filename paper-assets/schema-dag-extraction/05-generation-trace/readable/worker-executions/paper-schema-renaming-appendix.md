# paper schema renaming appendix

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 0
- **Tool calls:** 15
- **Original source:** `logs/workers/worker_paper_schema_renaming_appendix_20260518T213448.log`
- **Structured JSON:** [`1c559126620952f4c814.json`](../../sessions/1c/1c559126620952f4c814.json)

## Before a recorded user message

45 recorded events

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
  "session_id": "e8c6b2a1-3665-4eeb-aad0-d119dd87428b",
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
    "mcp__agent-ml-research__detect_image",
    "mcp__agent-ml-research__kill_job",
    "mcp__agent-ml-research__ssh_execute",
    "mcp__agent-ml-research__ssh_read_only"
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
  "uuid": "ce96b168-d765-4081-86d5-4e304d4f06c9",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction/memory/"
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
    "resetsAt": 1779155400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "a08ff88e-972c-4c66-8e4c-a9ba3acfd20b",
  "session_id": "e8c6b2a1-3665-4eeb-aad0-d119dd87428b"
}
```

---

### Assistant

_source line 4_

I'll start by SSH-ing to the server to find experiment details, and simultaneously read the current main.tex to understand the existing structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c6b2a1-3665-4eeb-aad0-d119dd87428b",
  "uuid": "2ae72a68-a6e2-4a4c-a2dc-493b0b5609dc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Napv2owmHsFDpsG7ujugH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13796,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13796
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01FYv9Da3XFMkaiYYdFxicMU`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c6b2a1-3665-4eeb-aad0-d119dd87428b",
  "uuid": "72d60543-fa9e-4d80-8367-0140a664df5f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Napv2owmHsFDpsG7ujugH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13796,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13796
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

_source line 6 · 2026-05-18T21:35:01.016Z_

<details><summary>↩ Tool result · `toolu_01FYv9Da3XFMkaiYYdFxicMU`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_execute"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e8c6b2a1-3665-4eeb-aad0-d119dd87428b",
  "uuid": "fb0aded2-81ce-42ce-ace9-4ed4c04b8679",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_execute"
    ],
    "query": "select:mcp__agent-ml-research__ssh_execute",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Now let me SSH to find experiment details and read the current main.tex in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c6b2a1-3665-4eeb-aad0-d119dd87428b",
  "uuid": "9f09e4da-c5ba-4120-ba4e-e581162ad95b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vkya6RAbgcGzQce9tanVZC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 376,
      "cache_read_input_tokens": 25637,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 376
      },
      "output_tokens": 26,
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

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01FjxGZBmQG55mgVDLfCDPh1`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "cd /root/schema-dag-extraction && find results/ artifacts/ src/ -name \"*rename*\" -o -name \"*intervention*\" -o -name \"*schema_intervention*\" 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c6b2a1-3665-4eeb-aad0-d119dd87428b",
  "uuid": "f92be737-3f6e-4dd5-ba75-419ec0616509",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vkya6RAbgcGzQce9tanVZC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 376,
      "cache_read_input_tokens": 25637,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 376
      },
      "output_tokens": 26,
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

<details open><summary>🔧 Tool call — Read · `toolu_014x1CHpe9xGPVEuhgH4gm3G`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": 580,
  "limit": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c6b2a1-3665-4eeb-aad0-d119dd87428b",
  "uuid": "997e383e-82be-4455-8002-edbbb772e57f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vkya6RAbgcGzQce9tanVZC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 376,
      "cache_read_input_tokens": 25637,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 376
      },
      "output_tokens": 26,
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

_source line 10 · 2026-05-18T21:35:07.039Z_

<details><summary>↩ Tool result · `toolu_01FjxGZBmQG55mgVDLfCDPh1`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"artifacts/scs_renaming_intervention.json\\nartifacts/exp_schema_intervention\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.48}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e8c6b2a1-3665-4eeb-aad0-d119dd87428b",
  "uuid": "59253881-0e35-4857-ae19-3e2a8cbb6b4c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"artifacts/scs_renaming_intervention.json\\\\nartifacts/exp_schema_intervention\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.48}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"artifacts/scs_renaming_intervention.json\\nartifacts/exp_schema_intervention\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.48}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-18T21:35:07.064Z_

<details><summary>↩ Tool result · `toolu_014x1CHpe9xGPVEuhgH4gm3G`</summary>

```text
580	
581	Table~\ref{tab:cross_model_gemini} confirms that the count-related accuracy decline replicates on Gemini 2.5 Flash. From count 4 to count 32, both models show perfectly monotonic decline (Spearman $\rho = -1.0$). Including count 1, the Gemini count curve yields $\rho = -0.900$ ($p = 0.037$); including partial count-64 data (11/25 batches), $\rho = -0.943$ ($p = 0.005$). The decline magnitude is smaller for Gemini ($-$13.3\,pp from count 4 to 32) than for Qwen3 ($-$21.8\,pp), consistent with Gemini's higher absolute accuracy providing more headroom before degradation saturates. At each count level, Gemini matches or exceeds Qwen3, with the gap widening at higher counts (0.3\,pp at count 4 vs.\ 8.7\,pp at count 32, 9.8\,pp at partial count 64); Gemini appears more robust to schema scaling but not immune. Dimension~2 (BCS-controlled confusability) has not been tested on proprietary models; cross-architecture Dimension~2 validation remains for future work.
582	
583	\section{Few-Shot Prompting and Confusability}
584	\label{sec:appendix_fewshot_bcs}
585	
586	To test whether in-context demonstrations mitigate the BCS-associated confusability effect, we evaluate 0-shot, 1-shot, and 5-shot prompting on FewRel 80-relation RE at count 8 using the same extreme-BCS batch design as \S\ref{sec:bcs_controlled}. Each condition uses 50 batches (25 low-BCS, mean $\approx 0.36$; 25 high-BCS, mean $\approx 0.80$), drawn from the pre-constructed batch pool of \S\ref{sec:bcs_controlled}. Few-shot examples are sampled from the FewRel training split for each target type.
587	
588	\begin{table}[h]
589	\centering
590	\small
591	\resizebox{\columnwidth}{!}{\begin{tabular}{lrrrl}
592	\toprule
593	\textbf{Condition} & \textbf{Low-BCS} & \textbf{High-BCS} & \textbf{$\Delta$ (pp)} & \textbf{95\% CI} \\
594	\midrule
595	0-shot & 0.682 & 0.498 & +18.5 & {[}+14.3, +22.7{]} \\
596	1-shot & 0.754 & 0.554 & +20.0 & {[}+16.3, +23.5{]} \\
597	5-shot & 0.715 & 0.488 & +22.8 & {[}+18.9, +26.8{]} \\
598	\bottomrule
599	\end{tabular}}
600	\caption{BCS gap under few-shot prompting (FewRel, count 8). Demonstrations improve absolute accuracy on low-BCS batches (+3.3--7.2\,pp over 0-shot) but provide inconsistent benefit on high-BCS batches (+5.6\,pp at 1-shot, $-$1.0\,pp at 5-shot). The confusability gap widens from +18.5\,pp (0-shot) to +22.8\,pp (5-shot). All metrics are micro-averaged across batches.}
601	\label{tab:fewshot_bcs}
602	\end{table}
603	
604	Demonstrations improve absolute accuracy primarily on low-BCS (easy) batches, where type boundaries are already distinct and examples reinforce correct mappings. On high-BCS batches, where types are semantically confusable, demonstrations provide inconsistent benefit (+5.6\,pp at 1-shot, $-$1.0\,pp at 5-shot): the model still substitutes similar types at comparable rates. The net effect is that the confusability gap widens under few-shot prompting (+4.3\,pp from 0-shot to 5-shot, bootstrap $p = 0.014$), with all three confidence intervals excluding zero. This indicates that BCS-associated type confusion is a structural property of the schema composition rather than a deficit addressable through prompt engineering. The non-monotonic low-BCS pattern (0.754 at 1-shot vs.\ 0.715 at 5-shot) may reflect lost-in-middle effects from increased prompt length \cite{lost-in-middle-2024}.
605	
606	The 0-shot gap (+18.5\,pp) is smaller than the extreme-batch gap reported in \S\ref{sec:bcs_controlled} (+25.5\,pp) because the two experiments use different test splits and batch sampling seeds; direct magnitude comparison across experiments is not appropriate.
607	
608	\section{Qualitative Error Analysis}
609	\label{app:error-analysis}
610	
611	Tables~\ref{tab:top10_re} and~\ref{tab:top10_ner} list the ten most frequently confused type pairs on FewRel 80-relation RE and Few-NERD NER. Confusion counts are aggregated bidirectionally across three random seeds (72{,}000 predictions per seed for RE; single-seed 66-type extraction for NER).
612	
613	\begin{table}[h]
614	\centering
615	\footnotesize
616	\begin{tabular}{clllr}
617	\toprule
618	\textbf{\#} & \textbf{Type A} & \textbf{Type B} & \textbf{SCS} & \textbf{$N$} \\
619	\midrule
620	1 & instance of & taxon rank & 0.53 & 875 \\
621	2 & child & father & 0.84 & 700 \\
622	3 & participant of & participating team & 0.75 & 675 \\
623	4 & mountain range & part of & 0.57 & 575 \\
624	5 & mouth of watercourse & tributary & 0.65 & 549 \\
625	6 & child & mother & 0.84 & 500 \\
626	7 & league & member of & 0.66 & 450 \\
627	8 & country of citizenship & country of origin & 0.76 & 400 \\
628	9 & followed by & follows & 0.90 & 400 \\
629	10 & occupation & voice type & 0.57 & 400 \\
630	\bottomrule
631	\end{tabular}
632	\caption{Top-10 confused relation pairs on FewRel 80-relation RE. $N$: bidirectional confusion count aggregated over 3 seeds $\times$ 25 batches. SCS: pairwise Schema Confusability Score (Qwen3 embedding cosine similarity). High-SCS pairs (e.g., \textit{followed by}/\textit{follows}, SCS\,=\,0.90) and family-relation pairs (\textit{child}/\textit{father}, \textit{child}/\textit{mother}) dominate. Some low-SCS pairs (\textit{instance of}/\textit{taxon rank}, SCS\,=\,0.53) reflect domain-specific co-occurrence rather than semantic similarity.}
633	\label{tab:top10_re}
634	\end{table}
635	
636	\begin{table}[h]
637	\centering
638	\footnotesize
639	\begin{tabular}{clllr}
640	\toprule
641	\textbf{\#} & \textbf{Type A} & \textbf{Type B} & \textbf{SCS} & \textbf{$N$} \\
642	\midrule
643	1 & person-other & person-politician & 0.93 & 121 \\
644	2 & location-GPE & organization-other & 0.83 & 81 \\
645	3 & art-film & location-GPE & 0.69 & 57 \\
646	4 & building-other & location-GPE & 0.85 & 56 \\
647	5 & building-other & person-other & 0.90 & 43 \\
648	6 & location-GPE & product-other & 0.69 & 39 \\
649	7 & org-gov/agency & person-other & 0.85 & 34 \\
650	8 & person-actor & person-other & 0.90 & 34 \\
651	9 & building-other & location-road/transit & 0.76 & 32 \\
652	10 & location-GPE & org-sportsleague & 0.81 & 30 \\
653	\bottomrule
654	\end{tabular}
655	\caption{Top-10 confused entity type pairs on Few-NERD NER. $N$: bidirectional confusion count from 66-type full-schema extraction. SCS: pairwise Schema Confusability Score (Qwen3 embedding cosine similarity). Intra-category confusions (e.g., \textit{person-other}/\textit{person-politician}, SCS\,=\,0.93) and cross-category pairs sharing referent overlap (\textit{building-other}/\textit{location-GPE}, SCS\,=\,0.85) are most frequent. The ``other'' subtypes absorb diverse entities and confuse with more specific siblings.}
656	\label{tab:top10_ner}
657	\end{table}
658	
659	\paragraph{Illustrative error instances.}
660	Table~\ref{tab:error_examples} shows three FewRel instances where the model predicted a semantically adjacent relation. All gold-predicted pairs have SCS\,$>$\,0.90.
661	
662	\begin{table}[h]
663	\centering
664	\footnotesize
665	\resizebox{\columnwidth}{!}{%
666	\begin{tabular}{p{5.8cm}llc}
667	\toprule
668	\textbf{Sentence (abridged)} & \textbf{Gold} & \textbf{Predicted} & \textbf{SCS} \\
669	\midrule
670	Over five EuroLeague games he played for \textbf{Valencia}, he averaged 8 points \ldots\  [\textbf{EuroLeague}, \textbf{Valencia}] & participant & participant of & 0.97 \\
671	\addlinespace
672	\textbf{Pilões} is a municipality in the state of \textbf{Rio Grande do Norte} in the Northeast region of Brazil. & contains admin.\ terr.\ entity & located in admin.\ terr.\ entity & 0.92 \\
673	\addlinespace
674	In May 1997 Davies was appointed \ldots\ to the \textbf{Cabinet} as \textbf{Secretary of State for Wales}. & part of & member of & 0.90 \\
675	\bottomrule
676	\end{tabular}}
677	\caption{Representative confusion instances from FewRel 80-relation RE (Qwen3-32B, count\,=\,80). Head and tail entities are bolded. In each case, the gold and predicted relations are semantically close (SCS\,$>$\,0.90): \textit{participant} vs.\ \textit{participant of} reverses argument directionality; \textit{contains} vs.\ \textit{located in} inverts the containment relation; \textit{part of} vs.\ \textit{member of} conflates meronymy with membership. These confusions are consistent with the pairwise SCS--confusion correlation reported in \S\ref{sec:pairwise}.}
678	\label{tab:error_examples}
679	\end{table}
680	
681	\end{document}
682	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e8c6b2a1-3665-4eeb-aad0-d119dd87428b",
  "uuid": "54e33ea9-127d-4249-a65c-59b6f68ef0bb",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
      "content": "\nTable~\\ref{tab:cross_model_gemini} confirms that the count-related accuracy decline replicates on Gemini 2.5 Flash. From count 4 to count 32, both models show perfectly monotonic decline (Spearman $\\rho = -1.0$). Including count 1, the Gemini count curve yields $\\rho = -0.900$ ($p = 0.037$); including partial count-64 data (11/25 batches), $\\rho = -0.943$ ($p = 0.005$). The decline magnitude is smaller for Gemini ($-$13.3\\,pp from count 4 to 32) than for Qwen3 ($-$21.8\\,pp), consistent with Gemini's higher absolute accuracy providing more headroom before degradation saturates. At each count level, Gemini matches or exceeds Qwen3, with the gap widening at higher counts (0.3\\,pp at count 4 vs.\\ 8.7\\,pp at count 32, 9.8\\,pp at partial count 64); Gemini appears more robust to schema scaling but not immune. Dimension~2 (BCS-controlled confusability) has not been tested on proprietary models; cross-architecture Dimension~2 validation remains for future work.\n\n\\section{Few-Shot Prompting and Confusability}\n\\label{sec:appendix_fewshot_bcs}\n\nTo test whether in-context demonstrations mitigate the BCS-associated confusability effect, we evaluate 0-shot, 1-shot, and 5-shot prompting on FewRel 80-relation RE at count 8 using the same extreme-BCS batch design as \\S\\ref{sec:bcs_controlled}. Each condition uses 50 batches (25 low-BCS, mean $\\approx 0.36$; 25 high-BCS, mean $\\approx 0.80$), drawn from the pre-constructed batch pool of \\S\\ref{sec:bcs_controlled}. Few-shot examples are sampled from the FewRel training split for each target type.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lrrrl}\n\\toprule\n\\textbf{Condition} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n0-shot & 0.682 & 0.498 & +18.5 & {[}+14.3, +22.7{]} \\\\\n1-shot & 0.754 & 0.554 & +20.0 & {[}+16.3, +23.5{]} \\\\\n5-shot & 0.715 & 0.488 & +22.8 & {[}+18.9, +26.8{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS gap under few-shot prompting (FewRel, count 8). Demonstrations improve absolute accuracy on low-BCS batches (+3.3--7.2\\,pp over 0-shot) but provide inconsistent benefit on high-BCS batches (+5.6\\,pp at 1-shot, $-$1.0\\,pp at 5-shot). The confusability gap widens from +18.5\\,pp (0-shot) to +22.8\\,pp (5-shot). All metrics are micro-averaged across batches.}\n\\label{tab:fewshot_bcs}\n\\end{table}\n\nDemonstrations improve absolute accuracy primarily on low-BCS (easy) batches, where type boundaries are already distinct and examples reinforce correct mappings. On high-BCS batches, where types are semantically confusable, demonstrations provide inconsistent benefit (+5.6\\,pp at 1-shot, $-$1.0\\,pp at 5-shot): the model still substitutes similar types at comparable rates. The net effect is that the confusability gap widens under few-shot prompting (+4.3\\,pp from 0-shot to 5-shot, bootstrap $p = 0.014$), with all three confidence intervals excluding zero. This indicates that BCS-associated type confusion is a structural property of the schema composition rather than a deficit addressable through prompt engineering. The non-monotonic low-BCS pattern (0.754 at 1-shot vs.\\ 0.715 at 5-shot) may reflect lost-in-middle effects from increased prompt length \\cite{lost-in-middle-2024}.\n\nThe 0-shot gap (+18.5\\,pp) is smaller than the extreme-batch gap reported in \\S\\ref{sec:bcs_controlled} (+25.5\\,pp) because the two experiments use different test splits and batch sampling seeds; direct magnitude comparison across experiments is not appropriate.\n\n\\section{Qualitative Error Analysis}\n\\label{app:error-analysis}\n\nTables~\\ref{tab:top10_re} and~\\ref{tab:top10_ner} list the ten most frequently confused type pairs on FewRel 80-relation RE and Few-NERD NER. Confusion counts are aggregated bidirectionally across three random seeds (72{,}000 predictions per seed for RE; single-seed 66-type extraction for NER).\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\begin{tabular}{clllr}\n\\toprule\n\\textbf{\\#} & \\textbf{Type A} & \\textbf{Type B} & \\textbf{SCS} & \\textbf{$N$} \\\\\n\\midrule\n1 & instance of & taxon rank & 0.53 & 875 \\\\\n2 & child & father & 0.84 & 700 \\\\\n3 & participant of & participating team & 0.75 & 675 \\\\\n4 & mountain range & part of & 0.57 & 575 \\\\\n5 & mouth of watercourse & tributary & 0.65 & 549 \\\\\n6 & child & mother & 0.84 & 500 \\\\\n7 & league & member of & 0.66 & 450 \\\\\n8 & country of citizenship & country of origin & 0.76 & 400 \\\\\n9 & followed by & follows & 0.90 & 400 \\\\\n10 & occupation & voice type & 0.57 & 400 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Top-10 confused relation pairs on FewRel 80-relation RE. $N$: bidirectional confusion count aggregated over 3 seeds $\\times$ 25 batches. SCS: pairwise Schema Confusability Score (Qwen3 embedding cosine similarity). High-SCS pairs (e.g., \\textit{followed by}/\\textit{follows}, SCS\\,=\\,0.90) and family-relation pairs (\\textit{child}/\\textit{father}, \\textit{child}/\\textit{mother}) dominate. Some low-SCS pairs (\\textit{instance of}/\\textit{taxon rank}, SCS\\,=\\,0.53) reflect domain-specific co-occurrence rather than semantic similarity.}\n\\label{tab:top10_re}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\begin{tabular}{clllr}\n\\toprule\n\\textbf{\\#} & \\textbf{Type A} & \\textbf{Type B} & \\textbf{SCS} & \\textbf{$N$} \\\\\n\\midrule\n1 & person-other & person-politician & 0.93 & 121 \\\\\n2 & location-GPE & organization-other & 0.83 & 81 \\\\\n3 & art-film & location-GPE & 0.69 & 57 \\\\\n4 & building-other & location-GPE & 0.85 & 56 \\\\\n5 & building-other & person-other & 0.90 & 43 \\\\\n6 & location-GPE & product-other & 0.69 & 39 \\\\\n7 & org-gov/agency & person-other & 0.85 & 34 \\\\\n8 & person-actor & person-other & 0.90 & 34 \\\\\n9 & building-other & location-road/transit & 0.76 & 32 \\\\\n10 & location-GPE & org-sportsleague & 0.81 & 30 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Top-10 confused entity type pairs on Few-NERD NER. $N$: bidirectional confusion count from 66-type full-schema extraction. SCS: pairwise Schema Confusability Score (Qwen3 embedding cosine similarity). Intra-category confusions (e.g., \\textit{person-other}/\\textit{person-politician}, SCS\\,=\\,0.93) and cross-category pairs sharing referent overlap (\\textit{building-other}/\\textit{location-GPE}, SCS\\,=\\,0.85) are most frequent. The ``other'' subtypes absorb diverse entities and confuse with more specific siblings.}\n\\label{tab:top10_ner}\n\\end{table}\n\n\\paragraph{Illustrative error instances.}\nTable~\\ref{tab:error_examples} shows three FewRel instances where the model predicted a semantically adjacent relation. All gold-predicted pairs have SCS\\,$>$\\,0.90.\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{p{5.8cm}llc}\n\\toprule\n\\textbf{Sentence (abridged)} & \\textbf{Gold} & \\textbf{Predicted} & \\textbf{SCS} \\\\\n\\midrule\nOver five EuroLeague games he played for \\textbf{Valencia}, he averaged 8 points \\ldots\\  [\\textbf{EuroLeague}, \\textbf{Valencia}] & participant & participant of & 0.97 \\\\\n\\addlinespace\n\\textbf{Pilões} is a municipality in the state of \\textbf{Rio Grande do Norte} in the Northeast region of Brazil. & contains admin.\\ terr.\\ entity & located in admin.\\ terr.\\ entity & 0.92 \\\\\n\\addlinespace\nIn May 1997 Davies was appointed \\ldots\\ to the \\textbf{Cabinet} as \\textbf{Secretary of State for Wales}. & part of & member of & 0.90 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Representative confusion instances from FewRel 80-relation RE (Qwen3-32B, count\\,=\\,80). Head and tail entities are bolded. In each case, the gold and predicted relations are semantically close (SCS\\,$>$\\,0.90): \\textit{participant} vs.\\ \\textit{participant of} reverses argument directionality; \\textit{contains} vs.\\ \\textit{located in} inverts the containment relation; \\textit{part of} vs.\\ \\textit{member of} conflates meronymy with membership. These confusions are consistent with the pairwise SCS--confusion correlation reported in \\S\\ref{sec:pairwise}.}\n\\label{tab:error_examples}\n\\end{table}\n\n\\end{document}\n",
      "numLines": 103,
      "startLine": 580,
      "totalLines": 682
    }
  }
}
```

</details>

---

### Assistant

_source line 12_

<details><summary>Logged reasoning block</summary>

```text
Now I need to explore the experiment details on the server. Let me look at the two files found.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c6b2a1-3665-4eeb-aad0-d119dd87428b",
  "uuid": "922e44a5-4e4b-494a-943f-5248289e78c6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NfmtvdGEYfyzbhGVc1NwwN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3539,
      "cache_read_input_tokens": 26013,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3539
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

_source line 13_

Found the experiment files. Let me explore them and also find the Limitations section in main.tex.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c6b2a1-3665-4eeb-aad0-d119dd87428b",
  "uuid": "b2df9163-d39e-4c22-bee2-50a6b0ece859",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NfmtvdGEYfyzbhGVc1NwwN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3539,
      "cache_read_input_tokens": 26013,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3539
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

_source line 14_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01L27ZMWq3STHjQVvPd91Bz1`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "cd /root/schema-dag-extraction && head -c 3000 artifacts/scs_renaming_intervention.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c6b2a1-3665-4eeb-aad0-d119dd87428b",
  "uuid": "d79976ed-6d50-4450-818c-9edd28b89c8b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NfmtvdGEYfyzbhGVc1NwwN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3539,
      "cache_read_input_tokens": 26013,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3539
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

_source line 15 · 2026-05-18T21:35:12.041Z_

<details><summary>↩ Tool result · `toolu_01L27ZMWq3STHjQVvPd91Bz1`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"embedding_model\\\": \\\"all-MiniLM-L6-v2\\\",\\n  \\\"prompt_template\\\": \\\"Relation type: {}\\\",\\n  \\\"final_renamings\\\": [\\n    {\\n      \\\"type_a\\\": \\\"participant\\\",\\n      \\\"type_b_original\\\": \\\"participant of\\\",\\n      \\\"type_b_renamed\\\": \\\"event involvement\\\",\\n      \\\"original_scs\\\": 0.9706,\\n      \\\"new_scs\\\": 0.72,\\n      \\\"delta\\\": -0.2506\\n    },\\n    {\\n      \\\"type_a\\\": \\\"contains administrative territorial entity\\\",\\n      \\\"type_b_original\\\": \\\"located in the administrative territorial entity\\\",\\n      \\\"type_b_renamed\\\": \\\"situated within governing region\\\",\\n      \\\"original_scs\\\": 0.9179,\\n      \\\"new_scs\\\": 0.7878,\\n      \\\"delta\\\": -0.1302\\n    },\\n    {\\n      \\\"type_a\\\": \\\"country\\\",\\n      \\\"type_b_original\\\": \\\"country of origin\\\",\\n      \\\"type_b_renamed\\\": \\\"homeland provenance\\\",\\n      \\\"original_scs\\\": 0.9051,\\n      \\\"new_scs\\\": 0.6367,\\n      \\\"delta\\\": -0.2684\\n    },\\n    {\\n      \\\"type_a\\\": \\\"member of\\\",\\n      \\\"type_b_original\\\": \\\"part of\\\",\\n      \\\"type_b_renamed\\\": \\\"integral segment of\\\",\\n      \\\"original_scs\\\": 0.9002,\\n      \\\"new_scs\\\": 0.6375,\\n      \\\"delta\\\": -0.2627\\n    },\\n    {\\n      \\\"type_a\\\": \\\"followed by\\\",\\n      \\\"type_b_original\\\": \\\"follows\\\",\\n      \\\"type_b_renamed\\\": \\\"prior entry\\\",\\n      \\\"original_scs\\\": 0.8969,\\n      \\\"new_scs\\\": 0.686,\\n      \\\"delta\\\": -0.2108\\n    },\\n    {\\n      \\\"type_a\\\": \\\"has part\\\",\\n      \\\"type_b_original\\\": \\\"part of\\\",\\n      \\\"type_b_renamed\\\": \\\"integral segment of\\\",\\n      \\\"original_scs\\\": 0.8806,\\n      \\\"new_scs\\\": 0.5813,\\n      \\\"delta\\\": -0.2994\\n    },\\n    {\\n      \\\"type_a\\\": \\\"instance of\\\",\\n      \\\"type_b_original\\\": \\\"member of\\\",\\n      \\\"type_b_renamed\\\": \\\"affiliated with\\\",\\n      \\\"original_scs\\\": 0.8657,\\n      \\\"new_scs\\\": 0.6603,\\n      \\\"delta\\\": -0.2054\\n    },\\n    {\\n      \\\"type_a\\\": \\\"father\\\",\\n      \\\"type_b_original\\\": \\\"mother\\\",\\n      \\\"type_b_renamed\\\": \\\"female progenitor\\\",\\n      \\\"original_scs\\\": 0.8565,\\n      \\\"new_scs\\\": 0.6165,\\n      \\\"delta\\\": -0.24\\n    },\\n    {\\n      \\\"type_a\\\": \\\"child\\\",\\n      \\\"type_b_original\\\": \\\"mother\\\",\\n      \\\"type_b_renamed\\\": \\\"female progenitor\\\",\\n      \\\"original_scs\\\": 0.8405,\\n      \\\"new_scs\\\": 0.6347,\\n      \\\"delta\\\": -0.2059\\n    },\\n    {\\n      \\\"type_a\\\": \\\"participating team\\\",\\n      \\\"type_b_original\\\": \\\"position played on team\\\",\\n      \\\"type_b_renamed\\\": \\\"athletic role on roster\\\",\\n      \\\"original_scs\\\": 0.8371,\\n      \\\"new_scs\\\": 0.6913,\\n      \\\"delta\\\": -0.1458\\n    },\\n    {\\n      \\\"type_a\\\": \\\"country\\\",\\n      \\\"type_b_original\\\": \\\"country of citizenship\\\",\\n      \\\"type_b_renamed\\\": \\\"citizenship allegiance\\\",\\n      \\\"original_scs\\\": 0.8292,\\n      \\\"new_scs\\\": 0.6125,\\n      \\\"delta\\\": -0.2167\\n    },\\n    {\\n      \\\"type_a\\\": \\\"military branch\\\",\\n      \\\"type_b_original\\\": \\\"military rank\\\",\\n      \\\"type_b_renamed\\\": \\\"service rank designation\\\",\\n      \\\"original_scs\\\": 0.8226,\\n      \\\"new_scs\\\": 0.6264,\\n      \\\"delta\\\": -0.1963\\n    },\\n    {\\n      \\\"type_a\\\": \\\"child\\\",\\n      \\\"type_b_original\\\": \\\"father\\\",\\n      \\\"type_b_renamed\\\": \\\"paternal figure\\\",\\n      \\\"original_scs\\\": 0.8361,\\n      \\\"new_scs\\\": 0.684,\\n      \\\"delta\\\": -0.1522\\n    },\\n    {\\n      \\\"type_a\\\": \\\"competition class\\\",\\n      \\\"type_b_original\\\": \\\"winner\\\",\\n      \\\"type_b_renamed\\\": \\\"contest victor\\\",\\n    \", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e8c6b2a1-3665-4eeb-aad0-d119dd87428b",
  "uuid": "ec9a6b29-591f-43f5-9bdf-09c5e088dbe2",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"embedding_model\\\\\\\": \\\\\\\"all-MiniLM-L6-v2\\\\\\\",\\\\n  \\\\\\\"prompt_template\\\\\\\": \\\\\\\"Relation type: {}\\\\\\\",\\\\n  \\\\\\\"final_renamings\\\\\\\": [\\\\n    {\\\\n      \\\\\\\"type_a\\\\\\\": \\\\\\\"participant\\\\\\\",\\\\n      \\\\\\\"type_b_original\\\\\\\": \\\\\\\"participant of\\\\\\\",\\\\n      \\\\\\\"type_b_renamed\\\\\\\": \\\\\\\"event involvement\\\\\\\",\\\\n      \\\\\\\"original_scs\\\\\\\": 0.9706,\\\\n      \\\\\\\"new_scs\\\\\\\": 0.72,\\\\n      \\\\\\\"delta\\\\\\\": -0.2506\\\\n    },\\\\n    {\\\\n      \\\\\\\"type_a\\\\\\\": \\\\\\\"contains administrative territorial entity\\\\\\\",\\\\n      \\\\\\\"type_b_original\\\\\\\": \\\\\\\"located in the administrative territorial entity\\\\\\\",\\\\n      \\\\\\\"type_b_renamed\\\\\\\": \\\\\\\"situated within governing region\\\\\\\",\\\\n      \\\\\\\"original_scs\\\\\\\": 0.9179,\\\\n      \\\\\\\"new_scs\\\\\\\": 0.7878,\\\\n      \\\\\\\"delta\\\\\\\": -0.1302\\\\n    },\\\\n    {\\\\n      \\\\\\\"type_a\\\\\\\": \\\\\\\"country\\\\\\\",\\\\n      \\\\\\\"type_b_original\\\\\\\": \\\\\\\"country of origin\\\\\\\",\\\\n      \\\\\\\"type_b_renamed\\\\\\\": \\\\\\\"homeland provenance\\\\\\\",\\\\n      \\\\\\\"original_scs\\\\\\\": 0.9051,\\\\n      \\\\\\\"new_scs\\\\\\\": 0.6367,\\\\n      \\\\\\\"delta\\\\\\\": -0.2684\\\\n    },\\\\n    {\\\\n      \\\\\\\"type_a\\\\\\\": \\\\\\\"member of\\\\\\\",\\\\n      \\\\\\\"type_b_original\\\\\\\": \\\\\\\"part of\\\\\\\",\\\\n      \\\\\\\"type_b_renamed\\\\\\\": \\\\\\\"integral segment of\\\\\\\",\\\\n      \\\\\\\"original_scs\\\\\\\": 0.9002,\\\\n      \\\\\\\"new_scs\\\\\\\": 0.6375,\\\\n      \\\\\\\"delta\\\\\\\": -0.2627\\\\n    },\\\\n    {\\\\n      \\\\\\\"type_a\\\\\\\": \\\\\\\"followed by\\\\\\\",\\\\n      \\\\\\\"type_b_original\\\\\\\": \\\\\\\"follows\\\\\\\",\\\\n      \\\\\\\"type_b_renamed\\\\\\\": \\\\\\\"prior entry\\\\\\\",\\\\n      \\\\\\\"original_scs\\\\\\\": 0.8969,\\\\n      \\\\\\\"new_scs\\\\\\\": 0.686,\\\\n      \\\\\\\"delta\\\\\\\": -0.2108\\\\n    },\\\\n    {\\\\n      \\\\\\\"type_a\\\\\\\": \\\\\\\"has part\\\\\\\",\\\\n      \\\\\\\"type_b_original\\\\\\\": \\\\\\\"part of\\\\\\\",\\\\n      \\\\\\\"type_b_renamed\\\\\\\": \\\\\\\"integral segment of\\\\\\\",\\\\n      \\\\\\\"original_scs\\\\\\\": 0.8806,\\\\n      \\\\\\\"new_scs\\\\\\\": 0.5813,\\\\n      \\\\\\\"delta\\\\\\\": -0.2994\\\\n    },\\\\n    {\\\\n      \\\\\\\"type_a\\\\\\\": \\\\\\\"instance of\\\\\\\",\\\\n      \\\\\\\"type_b_original\\\\\\\": \\\\\\\"member of\\\\\\\",\\\\n      \\\\\\\"type_b_renamed\\\\\\\": \\\\\\\"affiliated with\\\\\\\",\\\\n      \\\\\\\"original_scs\\\\\\\": 0.8657,\\\\n      \\\\\\\"new_scs\\\\\\\": 0.6603,\\\\n      \\\\\\\"delta\\\\\\\": -0.2054\\\\n    },\\\\n    {\\\\n      \\\\\\\"type_a\\\\\\\": \\\\\\\"father\\\\\\\",\\\\n      \\\\\\\"type_b_original\\\\\\\": \\\\\\\"mother\\\\\\\",\\\\n      \\\\\\\"type_b_renamed\\\\\\\": \\\\\\\"female progenitor\\\\\\\",\\\\n      \\\\\\\"original_scs\\\\\\\": 0.8565,\\\\n      \\\\\\\"new_scs\\\\\\\": 0.6165,\\\\n      \\\\\\\"delta\\\\\\\": -0.24\\\\n    },\\\\n    {\\\\n      \\\\\\\"type_a\\\\\\\": \\\\\\\"child\\\\\\\",\\\\n      \\\\\\\"type_b_original\\\\\\\": \\\\\\\"mother\\\\\\\",\\\\n      \\\\\\\"type_b_renamed\\\\\\\": \\\\\\\"female progenitor\\\\\\\",\\\\n      \\\\\\\"original_scs\\\\\\\": 0.8405,\\\\n      \\\\\\\"new_scs\\\\\\\": 0.6347,\\\\n      \\\\\\\"delta\\\\\\\": -0.2059\\\\n    },\\\\n    {\\\\n      \\\\\\\"type_a\\\\\\\": \\\\\\\"participating team\\\\\\\",\\\\n      \\\\\\\"type_b_original\\\\\\\": \\\\\\\"position played on team\\\\\\\",\\\\n      \\\\\\\"type_b_renamed\\\\\\\": \\\\\\\"athletic role on roster\\\\\\\",\\\\n      \\\\\\\"original_scs\\\\\\\": 0.8371,\\\\n      \\\\\\\"new_scs\\\\\\\": 0.6913,\\\\n      \\\\\\\"delta\\\\\\\": -0.1458\\\\n    },\\\\n    {\\\\n      \\\\\\\"type_a\\\\\\\": \\\\\\\"country\\\\\\\",\\\\n      \\\\\\\"type_b_original\\\\\\\": \\\\\\\"country of citizenship\\\\\\\",\\\\n      \\\\\\\"type_b_renamed\\\\\\\": \\\\\\\"citizenship allegiance\\\\\\\",\\\\n      \\\\\\\"original_scs\\\\\\\": 0.8292,\\\\n      \\\\\\\"new_scs\\\\\\\": 0.6125,\\\\n      \\\\\\\"delta\\\\\\\": -0.2167\\\\n    },\\\\n    {\\\\n      \\\\\\\"type_a\\\\\\\": \\\\\\\"military branch\\\\\\\",\\\\n      \\\\\\\"type_b_original\\\\\\\": \\\\\\\"military rank\\\\\\\",\\\\n      \\\\\\\"type_b_renamed\\\\\\\": \\\\\\\"service rank designation\\\\\\\",\\\\n      \\\\\\\"original_scs\\\\\\\": 0.8226,\\\\n      \\\\\\\"new_scs\\\\\\\": 0.6264,\\\\n      \\\\\\\"delta\\\\\\\": -0.1963\\\\n    },\\\\n    {\\\\n      \\\\\\\"type_a\\\\\\\": \\\\\\\"child\\\\\\\",\\\\n      \\\\\\\"type_b_original\\\\\\\": \\\\\\\"father\\\\\\\",\\\\n      \\\\\\\"type_b_renamed\\\\\\\": \\\\\\\"paternal figure\\\\\\\",\\\\n      \\\\\\\"original_scs\\\\\\\": 0.8361,\\\\n      \\\\\\\"new_scs\\\\\\\": 0.684,\\\\n      \\\\\\\"delta\\\\\\\": -0.1522\\\\n    },\\\\n    {\\\\n      \\\\\\\"type_a\\\\\\\": \\\\\\\"competition class\\\\\\\",\\\\n      \\\\\\\"type_b_original\\\\\\\": \\\\\\\"winner\\\\\\\",\\\\n      \\\\\\\"type_b_renamed\\\\\\\": \\\\\\\"contest victor\\\\\\\",\\\\n    \\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.37}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"embedding_model\\\": \\\"all-MiniLM-L6-v2\\\",\\n  \\\"prompt_template\\\": \\\"Relation type: {}\\\",\\n  \\\"final_renamings\\\": [\\n    {\\n      \\\"type_a\\\": \\\"participant\\\",\\n      \\\"type_b_original\\\": \\\"participant of\\\",\\n      \\\"type_b_renamed\\\": \\\"event involvement\\\",\\n      \\\"original_scs\\\": 0.9706,\\n      \\\"new_scs\\\": 0.72,\\n      \\\"delta\\\": -0.2506\\n    },\\n    {\\n      \\\"type_a\\\": \\\"contains administrative territorial entity\\\",\\n      \\\"type_b_original\\\": \\\"located in the administrative territorial entity\\\",\\n      \\\"type_b_renamed\\\": \\\"situated within governing region\\\",\\n      \\\"original_scs\\\": 0.9179,\\n      \\\"new_scs\\\": 0.7878,\\n      \\\"delta\\\": -0.1302\\n    },\\n    {\\n      \\\"type_a\\\": \\\"country\\\",\\n      \\\"type_b_original\\\": \\\"country of origin\\\",\\n      \\\"type_b_renamed\\\": \\\"homeland provenance\\\",\\n      \\\"original_scs\\\": 0.9051,\\n      \\\"new_scs\\\": 0.6367,\\n      \\\"delta\\\": -0.2684\\n    },\\n    {\\n      \\\"type_a\\\": \\\"member of\\\",\\n      \\\"type_b_original\\\": \\\"part of\\\",\\n      \\\"type_b_renamed\\\": \\\"integral segment of\\\",\\n      \\\"original_scs\\\": 0.9002,\\n      \\\"new_scs\\\": 0.6375,\\n      \\\"delta\\\": -0.2627\\n    },\\n    {\\n      \\\"type_a\\\": \\\"followed by\\\",\\n      \\\"type_b_original\\\": \\\"follows\\\",\\n      \\\"type_b_renamed\\\": \\\"prior entry\\\",\\n      \\\"original_scs\\\": 0.8969,\\n      \\\"new_scs\\\": 0.686,\\n      \\\"delta\\\": -0.2108\\n    },\\n    {\\n      \\\"type_a\\\": \\\"has part\\\",\\n      \\\"type_b_original\\\": \\\"part of\\\",\\n      \\\"type_b_renamed\\\": \\\"integral segment of\\\",\\n      \\\"original_scs\\\": 0.8806,\\n      \\\"new_scs\\\": 0.5813,\\n      \\\"delta\\\": -0.2994\\n    },\\n    {\\n      \\\"type_a\\\": \\\"instance of\\\",\\n      \\\"type_b_original\\\": \\\"member of\\\",\\n      \\\"type_b_renamed\\\": \\\"affiliated with\\\",\\n      \\\"original_scs\\\": 0.8657,\\n      \\\"new_scs\\\": 0.6603,\\n      \\\"delta\\\": -0.2054\\n    },\\n    {\\n      \\\"type_a\\\": \\\"father\\\",\\n      \\\"type_b_original\\\": \\\"mother\\\",\\n      \\\"type_b_renamed\\\": \\\"female progenitor\\\",\\n      \\\"original_scs\\\": 0.8565,\\n      \\\"new_scs\\\": 0.6165,\\n      \\\"delta\\\": -0.24\\n    },\\n    {\\n      \\\"type_a\\\": \\\"child\\\",\\n      \\\"type_b_original\\\": \\\"mother\\\",\\n      \\\"type_b_renamed\\\": \\\"female progenitor\\\",\\n      \\\"original_scs\\\": 0.8405,\\n      \\\"new_scs\\\": 0.6347,\\n      \\\"delta\\\": -0.2059\\n    },\\n    {\\n      \\\"type_a\\\": \\\"participating team\\\",\\n      \\\"type_b_original\\\": \\\"position played on team\\\",\\n      \\\"type_b_renamed\\\": \\\"athletic role on roster\\\",\\n      \\\"original_scs\\\": 0.8371,\\n      \\\"new_scs\\\": 0.6913,\\n      \\\"delta\\\": -0.1458\\n    },\\n    {\\n      \\\"type_a\\\": \\\"country\\\",\\n      \\\"type_b_original\\\": \\\"country of citizenship\\\",\\n      \\\"type_b_renamed\\\": \\\"citizenship allegiance\\\",\\n      \\\"original_scs\\\": 0.8292,\\n      \\\"new_scs\\\": 0.6125,\\n      \\\"delta\\\": -0.2167\\n    },\\n    {\\n      \\\"type_a\\\": \\\"military branch\\\",\\n      \\\"type_b_original\\\": \\\"military rank\\\",\\n      \\\"type_b_renamed\\\": \\\"service rank designation\\\",\\n      \\\"original_scs\\\": 0.8226,\\n      \\\"new_scs\\\": 0.6264,\\n      \\\"delta\\\": -0.1963\\n    },\\n    {\\n      \\\"type_a\\\": \\\"child\\\",\\n      \\\"type_b_original\\\": \\\"father\\\",\\n      \\\"type_b_renamed\\\": \\\"paternal figure\\\",\\n      \\\"original_scs\\\": 0.8361,\\n      \\\"new_scs\\\": 0.684,\\n      \\\"delta\\\": -0.1522\\n    },\\n    {\\n      \\\"type_a\\\": \\\"competition class\\\",\\n      \\\"type_b_original\\\": \\\"winner\\\",\\n      \\\"type_b_renamed\\\": \\\"contest victor\\\",\\n    \", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01VcP6pzNQdtGBMRWnHEQtXc`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "cd /root/schema-dag-extraction && ls -la artifacts/exp_schema_intervention/ && echo \"---\" && head -c 3000 artifacts/exp_schema_intervention/README.md 2>/dev/null || head -c 3000 artifacts/exp_schema_intervention/*.md 2>/dev/null || echo \"no readme\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c6b2a1-3665-4eeb-aad0-d119dd87428b",
  "uuid": "2e7d227d-1b3a-4970-b91d-06d8d4083006",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NfmtvdGEYfyzbhGVc1NwwN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3539,
      "cache_read_input_tokens": 26013,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3539
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

_source line 17_

<details open><summary>🔧 Tool call — Grep · `toolu_01Uw52iQgg7zbiJHfXsR1h96`</summary>

```json
{
  "pattern": "\\\\section\\{Limitations|\\\\subsection\\{Limitations|Limitations",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
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
  "session_id": "e8c6b2a1-3665-4eeb-aad0-d119dd87428b",
  "uuid": "cb73f8a5-eee2-46ec-8bbb-46d79330f4f3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NfmtvdGEYfyzbhGVc1NwwN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3539,
      "cache_read_input_tokens": 26013,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3539
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

_source line 18 · 2026-05-18T21:35:14.306Z_

<details><summary>↩ Tool result · `toolu_01VcP6pzNQdtGBMRWnHEQtXc`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 68\\ndrwxr-xr-x  2 root root  4096 May 18 00:07 .\\ndrwxr-xr-x 58 root root  4096 May 19 03:45 ..\\n-rw-r--r--  1 root root  1364 May 18 00:11 analysis.json\\n-rw-r--r--  1 root root  4545 May 17 23:55 qwen3_scs_verification.json\\n-rw-r--r--  1 root root 14099 May 18 00:11 results.json\\n-rw-r--r--  1 root root 13267 May 18 00:47 results_incremental.jsonl\\n-rw-r--r--  1 root root  7611 May 18 00:11 run_v2_final.log\\n-rw-r--r--  1 root root  2502 May 18 00:08 solo_sanity_check.json\\n---\\nno readme\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e8c6b2a1-3665-4eeb-aad0-d119dd87428b",
  "uuid": "7b780d7f-8191-4f06-99ba-a52ad15fbb61",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"total 68\\\\ndrwxr-xr-x  2 root root  4096 May 18 00:07 .\\\\ndrwxr-xr-x 58 root root  4096 May 19 03:45 ..\\\\n-rw-r--r--  1 root root  1364 May 18 00:11 analysis.json\\\\n-rw-r--r--  1 root root  4545 May 17 23:55 qwen3_scs_verification.json\\\\n-rw-r--r--  1 root root 14099 May 18 00:11 results.json\\\\n-rw-r--r--  1 root root 13267 May 18 00:47 results_incremental.jsonl\\\\n-rw-r--r--  1 root root  7611 May 18 00:11 run_v2_final.log\\\\n-rw-r--r--  1 root root  2502 May 18 00:08 solo_sanity_check.json\\\\n---\\\\nno readme\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.39}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"total 68\\ndrwxr-xr-x  2 root root  4096 May 18 00:07 .\\ndrwxr-xr-x 58 root root  4096 May 19 03:45 ..\\n-rw-r--r--  1 root root  1364 May 18 00:11 analysis.json\\n-rw-r--r--  1 root root  4545 May 17 23:55 qwen3_scs_verification.json\\n-rw-r--r--  1 root root 14099 May 18 00:11 results.json\\n-rw-r--r--  1 root root 13267 May 18 00:47 results_incremental.jsonl\\n-rw-r--r--  1 root root  7611 May 18 00:11 run_v2_final.log\\n-rw-r--r--  1 root root  2502 May 18 00:08 solo_sanity_check.json\\n---\\nno readme\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-18T21:35:14.326Z_

<details><summary>↩ Tool result · `toolu_01Uw52iQgg7zbiJHfXsR1h96`</summary>

```text
38:\section*{Limitations}
476:FewRel combines 64 train-split and 16 val-split relation types into a single 80-type pool.  Train-origin types show numerically lower accuracy ($-8.8$\,pp, $p = 0.06$; see Limitations), raising the question of whether differential pre-training exposure confounds the BCS--accuracy relationship.  We test this by adding a per-batch \emph{train-origin ratio} (fraction of relation types drawn from the train split) as a covariate in the BCS--accuracy regression.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e8c6b2a1-3665-4eeb-aad0-d119dd87428b",
  "uuid": "f4b8b73c-ee3f-4884-b234-93e12ef90189",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "38:\\section*{Limitations}\n476:FewRel combines 64 train-split and 16 val-split relation types into a single 80-type pool.  Train-origin types show numerically lower accuracy ($-8.8$\\,pp, $p = 0.06$; see Limitations), raising the question of whether differential pre-training exposure confounds the BCS--accuracy relationship.  We test this by adding a per-batch \\emph{train-origin ratio} (fraction of relation types drawn from the train split) as a covariate in the BCS--accuracy regression.",
    "numLines": 2
  }
}
```

</details>

---

### Assistant

_source line 20_

<details><summary>Logged reasoning block</summary>

```text
Let me get the analysis.json and also read the Limitations section of main.tex.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c6b2a1-3665-4eeb-aad0-d119dd87428b",
  "uuid": "b01ded21-245e-4482-b1db-994f6a3f2cfa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PcZpNsFMMXrPjXwaMFsj2L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2894,
      "cache_read_input_tokens": 29552,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2894
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

_source line 21_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01BwGw93bkGXnNBZsHPtiZQE`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "cd /root/schema-dag-extraction && cat artifacts/exp_schema_intervention/analysis.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c6b2a1-3665-4eeb-aad0-d119dd87428b",
  "uuid": "6cdcd9c9-6a06-40de-ac13-7eaa84653303",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PcZpNsFMMXrPjXwaMFsj2L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2894,
      "cache_read_input_tokens": 29552,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2894
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

_source line 22 · 2026-05-18T21:35:18.432Z_

<details><summary>↩ Tool result · `toolu_01BwGw93bkGXnNBZsHPtiZQE`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"high_bcs_group\\\": {\\n    \\\"n\\\": 25,\\n    \\\"mean_control_acc\\\": 0.6933,\\n    \\\"mean_treatment_acc\\\": 0.605,\\n    \\\"mean_delta\\\": -0.0883,\\n    \\\"std_delta\\\": 0.0302,\\n    \\\"paired_ttest_t\\\": -14.6094,\\n    \\\"paired_ttest_p\\\": 0.0,\\n    \\\"cohens_d\\\": -2.9222\\n  },\\n  \\\"low_bcs_group\\\": {\\n    \\\"n\\\": 25,\\n    \\\"mean_control_acc\\\": 0.9008,\\n    \\\"mean_treatment_acc\\\": 0.8712,\\n    \\\"mean_delta\\\": -0.0296,\\n    \\\"std_delta\\\": 0.0272,\\n    \\\"paired_ttest_t\\\": -5.4451,\\n    \\\"paired_ttest_p\\\": 1.4e-05,\\n    \\\"cohens_d\\\": -1.0882\\n  },\\n  \\\"interaction\\\": {\\n    \\\"high_mean_delta\\\": -0.0883,\\n    \\\"low_mean_delta\\\": -0.0296,\\n    \\\"difference\\\": -0.0588,\\n    \\\"ttest_t\\\": -7.2263,\\n    \\\"ttest_p\\\": 0.0\\n  },\\n  \\\"per_type_effect\\\": {\\n    \\\"country of citizenship\\\": {\\n      \\\"mean_delta\\\": -0.037,\\n      \\\"n_batches\\\": 20\\n    },\\n    \\\"follows\\\": {\\n      \\\"mean_delta\\\": -0.0883,\\n      \\\"n_batches\\\": 25\\n    },\\n    \\\"member of\\\": {\\n      \\\"mean_delta\\\": -0.089,\\n      \\\"n_batches\\\": 24\\n    },\\n    \\\"military rank\\\": {\\n      \\\"mean_delta\\\": -0.0208,\\n      \\\"n_batches\\\": 3\\n    },\\n    \\\"part of\\\": {\\n      \\\"mean_delta\\\": -0.0883,\\n      \\\"n_batches\\\": 25\\n    },\\n    \\\"participant of\\\": {\\n      \\\"mean_delta\\\": -0.0816,\\n      \\\"n_batches\\\": 6\\n    }\\n  },\\n  \\\"rename_count_correlation\\\": {\\n    \\\"pearson_r\\\": -0.6254,\\n    \\\"p_value\\\": 3e-06\\n  },\\n  \\\"total_time_s\\\": 210.4,\\n  \\\"solo_sanity_check\\\": {\\n    \\\"n_pass\\\": 11,\\n    \\\"n_total\\\": 12,\\n    \\\"failed_types\\\": [\\n      \\\"mother\\\"\\n    ]\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e8c6b2a1-3665-4eeb-aad0-d119dd87428b",
  "uuid": "eb68bb0f-cc08-4778-bab2-f630a4f95112",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"high_bcs_group\\\\\\\": {\\\\n    \\\\\\\"n\\\\\\\": 25,\\\\n    \\\\\\\"mean_control_acc\\\\\\\": 0.6933,\\\\n    \\\\\\\"mean_treatment_acc\\\\\\\": 0.605,\\\\n    \\\\\\\"mean_delta\\\\\\\": -0.0883,\\\\n    \\\\\\\"std_delta\\\\\\\": 0.0302,\\\\n    \\\\\\\"paired_ttest_t\\\\\\\": -14.6094,\\\\n    \\\\\\\"paired_ttest_p\\\\\\\": 0.0,\\\\n    \\\\\\\"cohens_d\\\\\\\": -2.9222\\\\n  },\\\\n  \\\\\\\"low_bcs_group\\\\\\\": {\\\\n    \\\\\\\"n\\\\\\\": 25,\\\\n    \\\\\\\"mean_control_acc\\\\\\\": 0.9008,\\\\n    \\\\\\\"mean_treatment_acc\\\\\\\": 0.8712,\\\\n    \\\\\\\"mean_delta\\\\\\\": -0.0296,\\\\n    \\\\\\\"std_delta\\\\\\\": 0.0272,\\\\n    \\\\\\\"paired_ttest_t\\\\\\\": -5.4451,\\\\n    \\\\\\\"paired_ttest_p\\\\\\\": 1.4e-05,\\\\n    \\\\\\\"cohens_d\\\\\\\": -1.0882\\\\n  },\\\\n  \\\\\\\"interaction\\\\\\\": {\\\\n    \\\\\\\"high_mean_delta\\\\\\\": -0.0883,\\\\n    \\\\\\\"low_mean_delta\\\\\\\": -0.0296,\\\\n    \\\\\\\"difference\\\\\\\": -0.0588,\\\\n    \\\\\\\"ttest_t\\\\\\\": -7.2263,\\\\n    \\\\\\\"ttest_p\\\\\\\": 0.0\\\\n  },\\\\n  \\\\\\\"per_type_effect\\\\\\\": {\\\\n    \\\\\\\"country of citizenship\\\\\\\": {\\\\n      \\\\\\\"mean_delta\\\\\\\": -0.037,\\\\n      \\\\\\\"n_batches\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"follows\\\\\\\": {\\\\n      \\\\\\\"mean_delta\\\\\\\": -0.0883,\\\\n      \\\\\\\"n_batches\\\\\\\": 25\\\\n    },\\\\n    \\\\\\\"member of\\\\\\\": {\\\\n      \\\\\\\"mean_delta\\\\\\\": -0.089,\\\\n      \\\\\\\"n_batches\\\\\\\": 24\\\\n    },\\\\n    \\\\\\\"military rank\\\\\\\": {\\\\n      \\\\\\\"mean_delta\\\\\\\": -0.0208,\\\\n      \\\\\\\"n_batches\\\\\\\": 3\\\\n    },\\\\n    \\\\\\\"part of\\\\\\\": {\\\\n      \\\\\\\"mean_delta\\\\\\\": -0.0883,\\\\n      \\\\\\\"n_batches\\\\\\\": 25\\\\n    },\\\\n    \\\\\\\"participant of\\\\\\\": {\\\\n      \\\\\\\"mean_delta\\\\\\\": -0.0816,\\\\n      \\\\\\\"n_batches\\\\\\\": 6\\\\n    }\\\\n  },\\\\n  \\\\\\\"rename_count_correlation\\\\\\\": {\\\\n    \\\\\\\"pearson_r\\\\\\\": -0.6254,\\\\n    \\\\\\\"p_value\\\\\\\": 3e-06\\\\n  },\\\\n  \\\\\\\"total_time_s\\\\\\\": 210.4,\\\\n  \\\\\\\"solo_sanity_check\\\\\\\": {\\\\n    \\\\\\\"n_pass\\\\\\\": 11,\\\\n    \\\\\\\"n_total\\\\\\\": 12,\\\\n    \\\\\\\"failed_types\\\\\\\": [\\\\n      \\\\\\\"mother\\\\\\\"\\\\n    ]\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.38}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"high_bcs_group\\\": {\\n    \\\"n\\\": 25,\\n    \\\"mean_control_acc\\\": 0.6933,\\n    \\\"mean_treatment_acc\\\": 0.605,\\n    \\\"mean_delta\\\": -0.0883,\\n    \\\"std_delta\\\": 0.0302,\\n    \\\"paired_ttest_t\\\": -14.6094,\\n    \\\"paired_ttest_p\\\": 0.0,\\n    \\\"cohens_d\\\": -2.9222\\n  },\\n  \\\"low_bcs_group\\\": {\\n    \\\"n\\\": 25,\\n    \\\"mean_control_acc\\\": 0.9008,\\n    \\\"mean_treatment_acc\\\": 0.8712,\\n    \\\"mean_delta\\\": -0.0296,\\n    \\\"std_delta\\\": 0.0272,\\n    \\\"paired_ttest_t\\\": -5.4451,\\n    \\\"paired_ttest_p\\\": 1.4e-05,\\n    \\\"cohens_d\\\": -1.0882\\n  },\\n  \\\"interaction\\\": {\\n    \\\"high_mean_delta\\\": -0.0883,\\n    \\\"low_mean_delta\\\": -0.0296,\\n    \\\"difference\\\": -0.0588,\\n    \\\"ttest_t\\\": -7.2263,\\n    \\\"ttest_p\\\": 0.0\\n  },\\n  \\\"per_type_effect\\\": {\\n    \\\"country of citizenship\\\": {\\n      \\\"mean_delta\\\": -0.037,\\n      \\\"n_batches\\\": 20\\n    },\\n    \\\"follows\\\": {\\n      \\\"mean_delta\\\": -0.0883,\\n      \\\"n_batches\\\": 25\\n    },\\n    \\\"member of\\\": {\\n      \\\"mean_delta\\\": -0.089,\\n      \\\"n_batches\\\": 24\\n    },\\n    \\\"military rank\\\": {\\n      \\\"mean_delta\\\": -0.0208,\\n      \\\"n_batches\\\": 3\\n    },\\n    \\\"part of\\\": {\\n      \\\"mean_delta\\\": -0.0883,\\n      \\\"n_batches\\\": 25\\n    },\\n    \\\"participant of\\\": {\\n      \\\"mean_delta\\\": -0.0816,\\n      \\\"n_batches\\\": 6\\n    }\\n  },\\n  \\\"rename_count_correlation\\\": {\\n    \\\"pearson_r\\\": -0.6254,\\n    \\\"p_value\\\": 3e-06\\n  },\\n  \\\"total_time_s\\\": 210.4,\\n  \\\"solo_sanity_check\\\": {\\n    \\\"n_pass\\\": 11,\\n    \\\"n_total\\\": 12,\\n    \\\"failed_types\\\": [\\n      \\\"mother\\\"\\n    ]\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_016gY63hmhStPSDhjRYfpRcs`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "cd /root/schema-dag-extraction && python3 -c \"\nimport json\nwith open('artifacts/scs_renaming_intervention.json') as f:\n    data = json.load(f)\n# Print keys and summary info\nfor k in data:\n    if k != 'final_renamings':\n        print(f'{k}: {data[k]}')\nprint(f'Number of renamings: {len(data.get(\\\"final_renamings\\\", []))}')\n\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c6b2a1-3665-4eeb-aad0-d119dd87428b",
  "uuid": "5b438f2e-e42d-4ad5-9932-646605cc5e46",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PcZpNsFMMXrPjXwaMFsj2L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2894,
      "cache_read_input_tokens": 29552,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2894
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

_source line 24 · 2026-05-18T21:35:20.396Z_

<details><summary>↩ Tool result · `toolu_016gY63hmhStPSDhjRYfpRcs`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"embedding_model: all-MiniLM-L6-v2\\nprompt_template: Relation type: {}\\ncandidate_analysis: {'follows': {'selected': 'prior entry', 'max_scs': 0.686, 'n_above_07': 0}, 'part of': {'selected': 'integral segment of', 'max_scs': 0.649, 'n_above_07': 0}, 'mother': {'selected': 'female progenitor', 'max_scs': 0.6451, 'n_above_07': 0}, 'followed by': {'selected': 'next in sequence', 'max_scs': 0.6432, 'n_above_07': 0}, 'military rank': {'selected': 'service rank designation', 'max_scs': 0.6566, 'n_above_07': 0}, 'country of citizenship': {'selected': 'citizenship allegiance', 'max_scs': 0.6125, 'n_above_07': 0}, 'participant of': {'selected': 'event involvement', 'max_scs': 0.72, 'n_above_07': 1}}\\nsummary: {'n_pairs': 14, 'mean_delta': -0.2019, 'mean_original_scs': 0.8695, 'mean_new_scs': 0.6677, 'n_reduced': 14}\\nNumber of renamings: 14\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e8c6b2a1-3665-4eeb-aad0-d119dd87428b",
  "uuid": "930af9a0-76fc-47b2-8580-bc6dbd6425fe",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"embedding_model: all-MiniLM-L6-v2\\\\nprompt_template: Relation type: {}\\\\ncandidate_analysis: {'follows': {'selected': 'prior entry', 'max_scs': 0.686, 'n_above_07': 0}, 'part of': {'selected': 'integral segment of', 'max_scs': 0.649, 'n_above_07': 0}, 'mother': {'selected': 'female progenitor', 'max_scs': 0.6451, 'n_above_07': 0}, 'followed by': {'selected': 'next in sequence', 'max_scs': 0.6432, 'n_above_07': 0}, 'military rank': {'selected': 'service rank designation', 'max_scs': 0.6566, 'n_above_07': 0}, 'country of citizenship': {'selected': 'citizenship allegiance', 'max_scs': 0.6125, 'n_above_07': 0}, 'participant of': {'selected': 'event involvement', 'max_scs': 0.72, 'n_above_07': 1}}\\\\nsummary: {'n_pairs': 14, 'mean_delta': -0.2019, 'mean_original_scs': 0.8695, 'mean_new_scs': 0.6677, 'n_reduced': 14}\\\\nNumber of renamings: 14\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.46}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"embedding_model: all-MiniLM-L6-v2\\nprompt_template: Relation type: {}\\ncandidate_analysis: {'follows': {'selected': 'prior entry', 'max_scs': 0.686, 'n_above_07': 0}, 'part of': {'selected': 'integral segment of', 'max_scs': 0.649, 'n_above_07': 0}, 'mother': {'selected': 'female progenitor', 'max_scs': 0.6451, 'n_above_07': 0}, 'followed by': {'selected': 'next in sequence', 'max_scs': 0.6432, 'n_above_07': 0}, 'military rank': {'selected': 'service rank designation', 'max_scs': 0.6566, 'n_above_07': 0}, 'country of citizenship': {'selected': 'citizenship allegiance', 'max_scs': 0.6125, 'n_above_07': 0}, 'participant of': {'selected': 'event involvement', 'max_scs': 0.72, 'n_above_07': 1}}\\nsummary: {'n_pairs': 14, 'mean_delta': -0.2019, 'mean_original_scs': 0.8695, 'mean_new_scs': 0.6677, 'n_reduced': 14}\\nNumber of renamings: 14\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Read · `toolu_01D1N1u5NC7rtwB5d9hD8yi4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": 30,
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c6b2a1-3665-4eeb-aad0-d119dd87428b",
  "uuid": "9b6c4ec0-8608-4b9a-acb9-55837b90ffaa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PcZpNsFMMXrPjXwaMFsj2L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2894,
      "cache_read_input_tokens": 29552,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2894
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

_source line 26 · 2026-05-18T21:35:20.567Z_

<details><summary>↩ Tool result · `toolu_01D1N1u5NC7rtwB5d9hD8yi4`</summary>

```text
30	\input{experimental_setup}
31	
32	\input{results}
33	
34	\input{sdgd_negative}
35	
36	\input{discussion}
37	
38	\section*{Limitations}
39	\begin{enumerate}[leftmargin=*,itemsep=2pt]
40	\item \textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B, 70B-Instruct (FP8), and Gemini 2.5 Flash (API). Dimension~1 has been validated across all four models including a proprietary one; Dimension~2 has been verified only on open-weight models and was not robustly detectable on NER at 8B scale, likely due to floor effects.
41	
42	\item \textbf{Effect size and statistical design.} Pairwise SCS explains 1.3--1.7\% of type confusion variance; entity frequency, prompt position, and mention ambiguity likely account for the remainder. The count $\times$ BCS interaction is bounded under the linear specification (TOST $p = 0.003$ at $\pm 3$\,pp) but inconclusive on the logit scale ($p = 0.209$; Appendix~\ref{sec:appendix_factorial}). BCS-controlled experiments use a single seed with greedy decoding; the residual SD of 0.88\,pp (Appendix~\ref{app:variance-decomposition}) supports robustness but precise magnitudes may vary.
43	
44	\item \textbf{Task format dependency.} BCS batch-level prediction is demonstrated only under RE's forced-choice classification format. An unconstrained decoding ablation ($n = 25$) confirms this: removing the enum constraint eliminates the BCS--accuracy correlation ($\rho = -0.14$, $p = 0.49$), establishing that the batch-level signal is specific to forced-choice RE. NER exact-match evaluation conflates boundary and type errors, and relaxed matching may yield different confusability effect sizes.
45	
46	\item \textbf{Causal mechanism.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway. A post-hoc schema label renaming experiment was inconclusive due to label unfamiliarity confounds.
47	
48	\item \textbf{Data contamination.} FewRel (2018) may appear in pretraining corpora, but train-origin relations show numerically lower accuracy than val-origin ($-8.8$\,pp, $p = 0.06$, n.s.), opposite to the contamination hypothesis. The monotonic degradation curve cannot be explained by uniform contamination. DocRED (2019) provides a lower-contamination-risk replication with consistent BCS--accuracy slopes ($R^2 = 0.53$). Adding train-origin ratio as a covariate leaves the BCS partial effect unchanged ($p = 0.245$; Appendix~\ref{app:split-origin}).
49	\end{enumerate}
50	
51	\paragraph{Multiple comparisons.} Cross-dataset comparisons (FewRel, DocRED, Few-NERD, MAVEN) serve as independent replications of the same hypothesis and do not require family-wise correction \citep{rothman-1990}. Within-dataset secondary analyses (e.g., quartile comparisons, slope sensitivity checks) involve multiple looks at the same data; we report individual $p$-values and note that core claims rest on effects reaching $p < 0.001$ \citep{dror-2018-significance,card-2020-power}.
52	
53	\input{checklist}
54	
55	\bibliography{references}
56	
57	\appendix
58	
59	\section{Additional Figures}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e8c6b2a1-3665-4eeb-aad0-d119dd87428b",
  "uuid": "496204fd-6893-468a-b7ad-bca7ea7be688",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
      "content": "\\input{experimental_setup}\n\n\\input{results}\n\n\\input{sdgd_negative}\n\n\\input{discussion}\n\n\\section*{Limitations}\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B, 70B-Instruct (FP8), and Gemini 2.5 Flash (API). Dimension~1 has been validated across all four models including a proprietary one; Dimension~2 has been verified only on open-weight models and was not robustly detectable on NER at 8B scale, likely due to floor effects.\n\n\\item \\textbf{Effect size and statistical design.} Pairwise SCS explains 1.3--1.7\\% of type confusion variance; entity frequency, prompt position, and mention ambiguity likely account for the remainder. The count $\\times$ BCS interaction is bounded under the linear specification (TOST $p = 0.003$ at $\\pm 3$\\,pp) but inconclusive on the logit scale ($p = 0.209$; Appendix~\\ref{sec:appendix_factorial}). BCS-controlled experiments use a single seed with greedy decoding; the residual SD of 0.88\\,pp (Appendix~\\ref{app:variance-decomposition}) supports robustness but precise magnitudes may vary.\n\n\\item \\textbf{Task format dependency.} BCS batch-level prediction is demonstrated only under RE's forced-choice classification format. An unconstrained decoding ablation ($n = 25$) confirms this: removing the enum constraint eliminates the BCS--accuracy correlation ($\\rho = -0.14$, $p = 0.49$), establishing that the batch-level signal is specific to forced-choice RE. NER exact-match evaluation conflates boundary and type errors, and relaxed matching may yield different confusability effect sizes.\n\n\\item \\textbf{Causal mechanism.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway. A post-hoc schema label renaming experiment was inconclusive due to label unfamiliarity confounds.\n\n\\item \\textbf{Data contamination.} FewRel (2018) may appear in pretraining corpora, but train-origin relations show numerically lower accuracy than val-origin ($-8.8$\\,pp, $p = 0.06$, n.s.), opposite to the contamination hypothesis. The monotonic degradation curve cannot be explained by uniform contamination. DocRED (2019) provides a lower-contamination-risk replication with consistent BCS--accuracy slopes ($R^2 = 0.53$). Adding train-origin ratio as a covariate leaves the BCS partial effect unchanged ($p = 0.245$; Appendix~\\ref{app:split-origin}).\n\\end{enumerate}\n\n\\paragraph{Multiple comparisons.} Cross-dataset comparisons (FewRel, DocRED, Few-NERD, MAVEN) serve as independent replications of the same hypothesis and do not require family-wise correction \\citep{rothman-1990}. Within-dataset secondary analyses (e.g., quartile comparisons, slope sensitivity checks) involve multiple looks at the same data; we report individual $p$-values and note that core claims rest on effects reaching $p < 0.001$ \\citep{dror-2018-significance,card-2020-power}.\n\n\\input{checklist}\n\n\\bibliography{references}\n\n\\appendix\n\n\\section{Additional Figures}",
      "numLines": 30,
      "startLine": 30,
      "totalLines": 682
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
Now I have all the details. Let me also get the experiment details about which batches were used, the count level, etc.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c6b2a1-3665-4eeb-aad0-d119dd87428b",
  "uuid": "c0279ec0-9a30-4f71-8326-65f01e911bea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DmNLP8acPMFbhk1sNKSm2Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 35463,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 35463
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

_source line 28_

Let me get the remaining experiment details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c6b2a1-3665-4eeb-aad0-d119dd87428b",
  "uuid": "00da3300-7464-48d4-8716-838fe66c08e6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DmNLP8acPMFbhk1sNKSm2Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 35463,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 35463
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01HXuKWSB9g1fGjE9fRmhJF8`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "cd /root/schema-dag-extraction && head -c 3000 artifacts/exp_schema_intervention/results.json | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\n# Print top-level keys\nfor k in data:\n    if isinstance(data[k], (str, int, float, bool)):\n        print(f'{k}: {data[k]}')\n    elif isinstance(data[k], dict):\n        print(f'{k}: {list(data[k].keys())[:10]}')\n    elif isinstance(data[k], list):\n        print(f'{k}: list of {len(data[k])} items')\n\" 2>/dev/null || head -c 2000 artifacts/exp_schema_intervention/results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c6b2a1-3665-4eeb-aad0-d119dd87428b",
  "uuid": "66774248-3ce8-4d70-b6a7-72cfa4ac0071",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DmNLP8acPMFbhk1sNKSm2Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 35463,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 35463
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

_source line 30 · 2026-05-18T21:35:28.274Z_

<details><summary>↩ Tool result · `toolu_01HXuKWSB9g1fGjE9fRmhJF8`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"[\\n  {\\n    \\\"batch_id\\\": \\\"low_0\\\",\\n    \\\"group\\\": \\\"low\\\",\\n    \\\"bcs\\\": 0.3562733248940536,\\n    \\\"n_samples\\\": 96,\\n    \\\"n_types_renamed\\\": 1,\\n    \\\"renamed_types\\\": [\\n      \\\"country of citizenship\\\"\\n    ],\\n    \\\"control_acc\\\": 0.9271,\\n    \\\"treatment_acc\\\": 0.8646,\\n    \\\"delta\\\": -0.0625\\n  },\\n  {\\n    \\\"batch_id\\\": \\\"low_1\\\",\\n    \\\"group\\\": \\\"low\\\",\\n    \\\"bcs\\\": 0.3576922571020467,\\n    \\\"n_samples\\\": 96,\\n    \\\"n_types_renamed\\\": 1,\\n    \\\"renamed_types\\\": [\\n      \\\"country of citizenship\\\"\\n    ],\\n    \\\"control_acc\\\": 0.9271,\\n    \\\"treatment_acc\\\": 0.8958,\\n    \\\"delta\\\": -0.0312\\n  },\\n  {\\n    \\\"batch_id\\\": \\\"low_2\\\",\\n    \\\"group\\\": \\\"low\\\",\\n    \\\"bcs\\\": 0.3578861765563488,\\n    \\\"n_samples\\\": 96,\\n    \\\"n_types_renamed\\\": 1,\\n    \\\"renamed_types\\\": [\\n      \\\"country of citizenship\\\"\\n    ],\\n    \\\"control_acc\\\": 0.9375,\\n    \\\"treatment_acc\\\": 0.8958,\\n    \\\"delta\\\": -0.0417\\n  },\\n  {\\n    \\\"batch_id\\\": \\\"low_3\\\",\\n    \\\"group\\\": \\\"low\\\",\\n    \\\"bcs\\\": 0.35802880621382166,\\n    \\\"n_samples\\\": 96,\\n    \\\"n_types_renamed\\\": 1,\\n    \\\"renamed_types\\\": [\\n      \\\"country of citizenship\\\"\\n    ],\\n    \\\"control_acc\\\": 0.875,\\n    \\\"treatment_acc\\\": 0.8333,\\n    \\\"delta\\\": -0.0417\\n  },\\n  {\\n    \\\"batch_id\\\": \\\"low_4\\\",\\n    \\\"group\\\": \\\"low\\\",\\n    \\\"bcs\\\": 0.3584075351910932,\\n    \\\"n_samples\\\": 96,\\n    \\\"n_types_renamed\\\": 1,\\n    \\\"renamed_types\\\": [\\n      \\\"country of citizenship\\\"\\n    ],\\n    \\\"control_acc\\\": 0.9688,\\n    \\\"treatment_acc\\\": 0.9167,\\n    \\\"delta\\\": -0.0521\\n  },\\n  {\\n    \\\"batch_id\\\": \\\"low_5\\\",\\n    \\\"group\\\": \\\"low\\\",\\n    \\\"bcs\\\": 0.3584426896912711,\\n    \\\"n_samples\\\": 96,\\n    \\\"n_types_renamed\\\": 1,\\n    \\\"renamed_types\\\": [\\n      \\\"country of citizenship\\\"\\n    ],\\n    \\\"control_acc\\\": 0.9375,\\n    \\\"treatment_acc\\\": 0.9271,\\n    \\\"delta\\\": -0.0104\\n  },\\n  {\\n    \\\"batch_id\\\": \\\"low_6\\\",\\n    \\\"group\\\": \\\"low\\\",\\n    \\\"bcs\\\": 0.3590553951050554,\\n    \\\"n_samples\\\": 96,\\n    \\\"n_types_renamed\\\": 0,\\n    \\\"renamed_types\\\": [],\\n    \\\"control_acc\\\": 0.9271,\\n    \\\"treatment_acc\\\": 0.9271,\\n    \\\"delta\\\": 0.0\\n  },\\n  {\\n    \\\"batch_id\\\": \\\"low_7\\\",\\n    \\\"group\\\": \\\"low\\\",\\n    \\\"bcs\\\": 0.3590933025947639,\\n    \\\"n_samples\\\": 96,\\n    \\\"n_types_renamed\\\": 0,\\n    \\\"renamed_types\\\": \", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e8c6b2a1-3665-4eeb-aad0-d119dd87428b",
  "uuid": "f177ecfa-01d2-45fa-a567-291e96d92933",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"[\\\\n  {\\\\n    \\\\\\\"batch_id\\\\\\\": \\\\\\\"low_0\\\\\\\",\\\\n    \\\\\\\"group\\\\\\\": \\\\\\\"low\\\\\\\",\\\\n    \\\\\\\"bcs\\\\\\\": 0.3562733248940536,\\\\n    \\\\\\\"n_samples\\\\\\\": 96,\\\\n    \\\\\\\"n_types_renamed\\\\\\\": 1,\\\\n    \\\\\\\"renamed_types\\\\\\\": [\\\\n      \\\\\\\"country of citizenship\\\\\\\"\\\\n    ],\\\\n    \\\\\\\"control_acc\\\\\\\": 0.9271,\\\\n    \\\\\\\"treatment_acc\\\\\\\": 0.8646,\\\\n    \\\\\\\"delta\\\\\\\": -0.0625\\\\n  },\\\\n  {\\\\n    \\\\\\\"batch_id\\\\\\\": \\\\\\\"low_1\\\\\\\",\\\\n    \\\\\\\"group\\\\\\\": \\\\\\\"low\\\\\\\",\\\\n    \\\\\\\"bcs\\\\\\\": 0.3576922571020467,\\\\n    \\\\\\\"n_samples\\\\\\\": 96,\\\\n    \\\\\\\"n_types_renamed\\\\\\\": 1,\\\\n    \\\\\\\"renamed_types\\\\\\\": [\\\\n      \\\\\\\"country of citizenship\\\\\\\"\\\\n    ],\\\\n    \\\\\\\"control_acc\\\\\\\": 0.9271,\\\\n    \\\\\\\"treatment_acc\\\\\\\": 0.8958,\\\\n    \\\\\\\"delta\\\\\\\": -0.0312\\\\n  },\\\\n  {\\\\n    \\\\\\\"batch_id\\\\\\\": \\\\\\\"low_2\\\\\\\",\\\\n    \\\\\\\"group\\\\\\\": \\\\\\\"low\\\\\\\",\\\\n    \\\\\\\"bcs\\\\\\\": 0.3578861765563488,\\\\n    \\\\\\\"n_samples\\\\\\\": 96,\\\\n    \\\\\\\"n_types_renamed\\\\\\\": 1,\\\\n    \\\\\\\"renamed_types\\\\\\\": [\\\\n      \\\\\\\"country of citizenship\\\\\\\"\\\\n    ],\\\\n    \\\\\\\"control_acc\\\\\\\": 0.9375,\\\\n    \\\\\\\"treatment_acc\\\\\\\": 0.8958,\\\\n    \\\\\\\"delta\\\\\\\": -0.0417\\\\n  },\\\\n  {\\\\n    \\\\\\\"batch_id\\\\\\\": \\\\\\\"low_3\\\\\\\",\\\\n    \\\\\\\"group\\\\\\\": \\\\\\\"low\\\\\\\",\\\\n    \\\\\\\"bcs\\\\\\\": 0.35802880621382166,\\\\n    \\\\\\\"n_samples\\\\\\\": 96,\\\\n    \\\\\\\"n_types_renamed\\\\\\\": 1,\\\\n    \\\\\\\"renamed_types\\\\\\\": [\\\\n      \\\\\\\"country of citizenship\\\\\\\"\\\\n    ],\\\\n    \\\\\\\"control_acc\\\\\\\": 0.875,\\\\n    \\\\\\\"treatment_acc\\\\\\\": 0.8333,\\\\n    \\\\\\\"delta\\\\\\\": -0.0417\\\\n  },\\\\n  {\\\\n    \\\\\\\"batch_id\\\\\\\": \\\\\\\"low_4\\\\\\\",\\\\n    \\\\\\\"group\\\\\\\": \\\\\\\"low\\\\\\\",\\\\n    \\\\\\\"bcs\\\\\\\": 0.3584075351910932,\\\\n    \\\\\\\"n_samples\\\\\\\": 96,\\\\n    \\\\\\\"n_types_renamed\\\\\\\": 1,\\\\n    \\\\\\\"renamed_types\\\\\\\": [\\\\n      \\\\\\\"country of citizenship\\\\\\\"\\\\n    ],\\\\n    \\\\\\\"control_acc\\\\\\\": 0.9688,\\\\n    \\\\\\\"treatment_acc\\\\\\\": 0.9167,\\\\n    \\\\\\\"delta\\\\\\\": -0.0521\\\\n  },\\\\n  {\\\\n    \\\\\\\"batch_id\\\\\\\": \\\\\\\"low_5\\\\\\\",\\\\n    \\\\\\\"group\\\\\\\": \\\\\\\"low\\\\\\\",\\\\n    \\\\\\\"bcs\\\\\\\": 0.3584426896912711,\\\\n    \\\\\\\"n_samples\\\\\\\": 96,\\\\n    \\\\\\\"n_types_renamed\\\\\\\": 1,\\\\n    \\\\\\\"renamed_types\\\\\\\": [\\\\n      \\\\\\\"country of citizenship\\\\\\\"\\\\n    ],\\\\n    \\\\\\\"control_acc\\\\\\\": 0.9375,\\\\n    \\\\\\\"treatment_acc\\\\\\\": 0.9271,\\\\n    \\\\\\\"delta\\\\\\\": -0.0104\\\\n  },\\\\n  {\\\\n    \\\\\\\"batch_id\\\\\\\": \\\\\\\"low_6\\\\\\\",\\\\n    \\\\\\\"group\\\\\\\": \\\\\\\"low\\\\\\\",\\\\n    \\\\\\\"bcs\\\\\\\": 0.3590553951050554,\\\\n    \\\\\\\"n_samples\\\\\\\": 96,\\\\n    \\\\\\\"n_types_renamed\\\\\\\": 0,\\\\n    \\\\\\\"renamed_types\\\\\\\": [],\\\\n    \\\\\\\"control_acc\\\\\\\": 0.9271,\\\\n    \\\\\\\"treatment_acc\\\\\\\": 0.9271,\\\\n    \\\\\\\"delta\\\\\\\": 0.0\\\\n  },\\\\n  {\\\\n    \\\\\\\"batch_id\\\\\\\": \\\\\\\"low_7\\\\\\\",\\\\n    \\\\\\\"group\\\\\\\": \\\\\\\"low\\\\\\\",\\\\n    \\\\\\\"bcs\\\\\\\": 0.3590933025947639,\\\\n    \\\\\\\"n_samples\\\\\\\": 96,\\\\n    \\\\\\\"n_types_renamed\\\\\\\": 0,\\\\n    \\\\\\\"renamed_types\\\\\\\": \\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.47}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"[\\n  {\\n    \\\"batch_id\\\": \\\"low_0\\\",\\n    \\\"group\\\": \\\"low\\\",\\n    \\\"bcs\\\": 0.3562733248940536,\\n    \\\"n_samples\\\": 96,\\n    \\\"n_types_renamed\\\": 1,\\n    \\\"renamed_types\\\": [\\n      \\\"country of citizenship\\\"\\n    ],\\n    \\\"control_acc\\\": 0.9271,\\n    \\\"treatment_acc\\\": 0.8646,\\n    \\\"delta\\\": -0.0625\\n  },\\n  {\\n    \\\"batch_id\\\": \\\"low_1\\\",\\n    \\\"group\\\": \\\"low\\\",\\n    \\\"bcs\\\": 0.3576922571020467,\\n    \\\"n_samples\\\": 96,\\n    \\\"n_types_renamed\\\": 1,\\n    \\\"renamed_types\\\": [\\n      \\\"country of citizenship\\\"\\n    ],\\n    \\\"control_acc\\\": 0.9271,\\n    \\\"treatment_acc\\\": 0.8958,\\n    \\\"delta\\\": -0.0312\\n  },\\n  {\\n    \\\"batch_id\\\": \\\"low_2\\\",\\n    \\\"group\\\": \\\"low\\\",\\n    \\\"bcs\\\": 0.3578861765563488,\\n    \\\"n_samples\\\": 96,\\n    \\\"n_types_renamed\\\": 1,\\n    \\\"renamed_types\\\": [\\n      \\\"country of citizenship\\\"\\n    ],\\n    \\\"control_acc\\\": 0.9375,\\n    \\\"treatment_acc\\\": 0.8958,\\n    \\\"delta\\\": -0.0417\\n  },\\n  {\\n    \\\"batch_id\\\": \\\"low_3\\\",\\n    \\\"group\\\": \\\"low\\\",\\n    \\\"bcs\\\": 0.35802880621382166,\\n    \\\"n_samples\\\": 96,\\n    \\\"n_types_renamed\\\": 1,\\n    \\\"renamed_types\\\": [\\n      \\\"country of citizenship\\\"\\n    ],\\n    \\\"control_acc\\\": 0.875,\\n    \\\"treatment_acc\\\": 0.8333,\\n    \\\"delta\\\": -0.0417\\n  },\\n  {\\n    \\\"batch_id\\\": \\\"low_4\\\",\\n    \\\"group\\\": \\\"low\\\",\\n    \\\"bcs\\\": 0.3584075351910932,\\n    \\\"n_samples\\\": 96,\\n    \\\"n_types_renamed\\\": 1,\\n    \\\"renamed_types\\\": [\\n      \\\"country of citizenship\\\"\\n    ],\\n    \\\"control_acc\\\": 0.9688,\\n    \\\"treatment_acc\\\": 0.9167,\\n    \\\"delta\\\": -0.0521\\n  },\\n  {\\n    \\\"batch_id\\\": \\\"low_5\\\",\\n    \\\"group\\\": \\\"low\\\",\\n    \\\"bcs\\\": 0.3584426896912711,\\n    \\\"n_samples\\\": 96,\\n    \\\"n_types_renamed\\\": 1,\\n    \\\"renamed_types\\\": [\\n      \\\"country of citizenship\\\"\\n    ],\\n    \\\"control_acc\\\": 0.9375,\\n    \\\"treatment_acc\\\": 0.9271,\\n    \\\"delta\\\": -0.0104\\n  },\\n  {\\n    \\\"batch_id\\\": \\\"low_6\\\",\\n    \\\"group\\\": \\\"low\\\",\\n    \\\"bcs\\\": 0.3590553951050554,\\n    \\\"n_samples\\\": 96,\\n    \\\"n_types_renamed\\\": 0,\\n    \\\"renamed_types\\\": [],\\n    \\\"control_acc\\\": 0.9271,\\n    \\\"treatment_acc\\\": 0.9271,\\n    \\\"delta\\\": 0.0\\n  },\\n  {\\n    \\\"batch_id\\\": \\\"low_7\\\",\\n    \\\"group\\\": \\\"low\\\",\\n    \\\"bcs\\\": 0.3590933025947639,\\n    \\\"n_samples\\\": 96,\\n    \\\"n_types_renamed\\\": 0,\\n    \\\"renamed_types\\\": \", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01YJBvFCDpnwnQZUH6p4Lns5`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "cd /root/schema-dag-extraction && head -60 artifacts/exp_schema_intervention/run_v2_final.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c6b2a1-3665-4eeb-aad0-d119dd87428b",
  "uuid": "36e6e2bb-f31d-465a-a231-ad236f6bd3b4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DmNLP8acPMFbhk1sNKSm2Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 35463,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 35463
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

_source line 32 · 2026-05-18T21:35:28.738Z_

<details><summary>↩ Tool result · `toolu_01YJBvFCDpnwnQZUH6p4Lns5`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-18 00:07:39,320 INFO Using model: /root/autodl-tmp/.hf_cache/qwen3-32b-fp8/\\n2026-05-18 00:08:00,201 INFO Loaded 960 balanced samples (80 relations)\\n2026-05-18 00:08:00,232 INFO ======================================================================\\n2026-05-18 00:08:00,232 INFO PHASE 2: Solo Accuracy Sanity Check\\n2026-05-18 00:08:00,232 INFO ======================================================================\\n2026-05-18 00:08:01,696 INFO   [OK] country of citizenship -> nationality: orig=0.833 renamed=0.833 (Δ=+0.000, n=12)\\n2026-05-18 00:08:03,003 INFO   [OK] country of origin -> land of origin: orig=0.667 renamed=0.667 (Δ=+0.000, n=12)\\n2026-05-18 00:08:04,161 INFO   [OK] father -> paternal figure: orig=1.000 renamed=1.000 (Δ=+0.000, n=12)\\n2026-05-18 00:08:05,479 INFO   [OK] follows -> comes after: orig=0.833 renamed=0.917 (Δ=+0.083, n=12)\\n2026-05-18 00:08:07,021 INFO   [OK] located in the administrative territorial entity -> situated within governing region: orig=1.000 renamed=1.000 (Δ=+0.000, n=12)\\n2026-05-18 00:08:08,266 INFO   [OK] member of -> affiliated with: orig=1.000 renamed=1.000 (Δ=+0.000, n=12)\\n2026-05-18 00:08:09,598 INFO   [OK] military rank -> service rank designation: orig=1.000 renamed=1.000 (Δ=+0.000, n=12)\\n2026-05-18 00:08:11,239 INFO   [FAIL] mother -> maternal parent: orig=0.833 renamed=0.750 (Δ=-0.083, n=12)\\n2026-05-18 00:08:12,510 INFO   [OK] part of -> integral segment of: orig=1.000 renamed=1.000 (Δ=+0.000, n=12)\\n2026-05-18 00:08:13,657 INFO   [OK] participant of -> event involvement: orig=1.000 renamed=1.000 (Δ=+0.000, n=12)\\n2026-05-18 00:08:15,325 INFO   [OK] position played on team -> athletic role on roster: orig=1.000 renamed=1.000 (Δ=+0.000, n=12)\\n2026-05-18 00:08:16,645 INFO   [OK] winner -> contest victor: orig=0.917 renamed=0.917 (Δ=+0.000, n=12)\\n2026-05-18 00:08:16,646 INFO Solo check: 11/12 passed (Δ >= -5pp)\\n2026-05-18 00:08:16,647 INFO Saved to /root/schema-dag-extraction/artifacts/exp_schema_intervention/solo_sanity_check.json\\n2026-05-18 00:08:16,648 WARNING FAILED solo checks: ['mother']\\n2026-05-18 00:08:16,649 WARNING Proceeding anyway (will note in analysis)\\n2026-05-18 00:08:16,649 INFO ======================================================================\\n2026-05-18 00:08:16,649 INFO PHASE 3: Formal BCS-Controlled Experiment\\n2026-05-18 00:08:16,649 INFO ======================================================================\\n2026-05-18 00:08:16,650 INFO Loaded 25 low + 25 high batches\\n2026-05-18 00:08:22,712 INFO   low_0: ctrl=0.9271 treat=0.8646 Δ=-0.0625 (renamed=1)\\n2026-05-18 00:08:27,625 INFO   low_1: ctrl=0.9271 treat=0.8958 Δ=-0.0312 (renamed=1)\\n2026-05-18 00:08:32,399 INFO   low_2: ctrl=0.9375 treat=0.8958 Δ=-0.0417 (renamed=1)\\n2026-05-18 00:08:36,705 INFO   low_3: ctrl=0.8750 treat=0.8333 Δ=-0.0417 (renamed=1)\\n2026-05-18 00:08:41,441 INFO   low_4: ctrl=0.9688 treat=0.9167 Δ=-0.0521 (renamed=1)\\n2026-05-18 00:08:45,959 INFO   low_5: ctrl=0.9375 treat=0.9271 Δ=-0.0104 (renamed=1)\\n2026-05-18 00:08:48,184 INFO   low_6: ctrl=0.9271 treat=0.9271 Δ=+0.0000 (renamed=0)\\n2026-05-18 00:08:50,546 INFO   low_7: ctrl=0.9062 treat=0.9062 Δ=+0.0000 (renamed=0)\\n2026-05-18 00:08:55,141 INFO   low_8: ctrl=0.9271 treat=0.8958 Δ=-0.0312 (renamed=1)\\n2026-05-18 00:08:59,660 INFO   low_9: ctrl=0.8333 treat=0.8438 Δ=+0.0104 (renamed=1)\\n2026-05-18 00:09:04,178 INFO   low_10: ctrl=0.8333 treat=0.8229 Δ=-0.0104 (renamed=1)\\n2026-05-18 00:09:08,288 INFO   low_11: ctrl=0.8438 treat=0.8333 Δ=-0.0104 (renamed=1)\\n2026-05-18 00:09:10,389 INFO   low_12: ctrl=0.8854 treat=0.8854 Δ=+0.0000 (renamed=0)\\n2026-05-18 00:09:15,526 INFO   low_13: ctrl=0.9167 treat=0.8958 Δ=-0.0208 (renamed=1)\\n2026-05-18 00:09:20,165 INFO   low_14: ctrl=0.9375 treat=0.8854 Δ=-0.0521 (renamed=2)\\n2026-05-18 00:09:24,933 INFO   low_15: ctrl=0.8958 treat=0.8021 Δ=-0.0938 (renamed=1)\\n2026-05-18 00:09:29,380 INFO   low_16: ctrl=0.8750 treat=0.8125 Δ=-0.0625 (renamed=1)\\n2026-05-18 00:09:34,102 INFO   low_17: ctrl=0.9688 treat=0.9271 Δ=-0.0417 (renamed=1)\\n2026-05-18 00:09:36,573 INFO   low_18: ctrl=0.8542 treat=0.8542 Δ=+0.0000 (renamed=0)\\n2026-05-18 00:09:41,200 INFO   low_19: ctrl=0.9167 treat=0.9062 Δ=-0.0104 (renamed=2)\\n2026-05-18 00:09:45,885 INFO   low_20: ctrl=0.8750 treat=0.8229 Δ=-0.0521 (renamed=1)\\n2026-05-18 00:09:50,353 INFO   low_21: ctrl=0.9167 treat=0.9167 Δ=+0.0000 (renamed=1)\\n2026-05-18 00:09:55,130 INFO   low_22: ctrl=0.8958 treat=0.8854 Δ=-0.0104 (renamed=1)\\n2026-05-18 00:10:00,337 INFO   low_23: ctrl=0.8854 treat=0.8229 Δ=-0.0625 (renamed=1)\\n2026-05-18 00:10:04,980 INFO   low_24: ctrl=0.8542 treat=0.8021 Δ=-0.0521 (renamed=1)\\n2026-05-18 00:10:09,742 INFO   high_0: ctrl=0.6979 treat=0.5521 Δ=-0.1458 (renamed=3)\\n2026-05-18 00:10:14,088 INFO   high_1: ctrl=0.7083 treat=0.6667 Δ=-0.0417 (renamed=3)\\n2026-05-18 00:10:18,508 INFO   high_2: ctrl=0.7188 treat=0.6667 Δ=-0.0521 (renamed=4)\\n2026-05-18 00:10:22,509 INFO   high_3: ctrl=0.6667 treat=0.5729 Δ=-0.0938 (renamed=3)\\n2026-05-18 00:10:26,756 INFO   high_4: ctrl=0.6250 treat=0.5521 Δ=-0.0729 (renamed=2)\\n2026-05-18 00:10:30,700 INFO   high_5: ctrl=0.8438 treat=0.7188 Δ=-0.1250 (renamed=3)\\n2026-05-18 00:10:34,354 INFO   high_6: ctrl=0.7188 treat=0.6771 Δ=-0.0417 (renamed=4)\\n2026-05-18 00:10:38,146 INFO   high_7: ctrl=0.6354 treat=0.5208 Δ=-0.1146 (renamed=3)\\n2026-05-18 00:10:42,268 INFO   high_8: ctrl=0.8333 treat=0.7604 Δ=-0.0729 (renamed=4)\\n2026-05-18 00:10:46,739 INFO   high_9: ctrl=0.6562 treat=0.5521 Δ=-0.1042 (renamed=4)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e8c6b2a1-3665-4eeb-aad0-d119dd87428b",
  "uuid": "a46c6cfb-4da0-4990-9900-759e803edc81",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"2026-05-18 00:07:39,320 INFO Using model: /root/autodl-tmp/.hf_cache/qwen3-32b-fp8/\\\\n2026-05-18 00:08:00,201 INFO Loaded 960 balanced samples (80 relations)\\\\n2026-05-18 00:08:00,232 INFO ======================================================================\\\\n2026-05-18 00:08:00,232 INFO PHASE 2: Solo Accuracy Sanity Check\\\\n2026-05-18 00:08:00,232 INFO ======================================================================\\\\n2026-05-18 00:08:01,696 INFO   [OK] country of citizenship -> nationality: orig=0.833 renamed=0.833 (Δ=+0.000, n=12)\\\\n2026-05-18 00:08:03,003 INFO   [OK] country of origin -> land of origin: orig=0.667 renamed=0.667 (Δ=+0.000, n=12)\\\\n2026-05-18 00:08:04,161 INFO   [OK] father -> paternal figure: orig=1.000 renamed=1.000 (Δ=+0.000, n=12)\\\\n2026-05-18 00:08:05,479 INFO   [OK] follows -> comes after: orig=0.833 renamed=0.917 (Δ=+0.083, n=12)\\\\n2026-05-18 00:08:07,021 INFO   [OK] located in the administrative territorial entity -> situated within governing region: orig=1.000 renamed=1.000 (Δ=+0.000, n=12)\\\\n2026-05-18 00:08:08,266 INFO   [OK] member of -> affiliated with: orig=1.000 renamed=1.000 (Δ=+0.000, n=12)\\\\n2026-05-18 00:08:09,598 INFO   [OK] military rank -> service rank designation: orig=1.000 renamed=1.000 (Δ=+0.000, n=12)\\\\n2026-05-18 00:08:11,239 INFO   [FAIL] mother -> maternal parent: orig=0.833 renamed=0.750 (Δ=-0.083, n=12)\\\\n2026-05-18 00:08:12,510 INFO   [OK] part of -> integral segment of: orig=1.000 renamed=1.000 (Δ=+0.000, n=12)\\\\n2026-05-18 00:08:13,657 INFO   [OK] participant of -> event involvement: orig=1.000 renamed=1.000 (Δ=+0.000, n=12)\\\\n2026-05-18 00:08:15,325 INFO   [OK] position played on team -> athletic role on roster: orig=1.000 renamed=1.000 (Δ=+0.000, n=12)\\\\n2026-05-18 00:08:16,645 INFO   [OK] winner -> contest victor: orig=0.917 renamed=0.917 (Δ=+0.000, n=12)\\\\n2026-05-18 00:08:16,646 INFO Solo check: 11/12 passed (Δ >= -5pp)\\\\n2026-05-18 00:08:16,647 INFO Saved to /root/schema-dag-extraction/artifacts/exp_schema_intervention/solo_sanity_check.json\\\\n2026-05-18 00:08:16,648 WARNING FAILED solo checks: ['mother']\\\\n2026-05-18 00:08:16,649 WARNING Proceeding anyway (will note in analysis)\\\\n2026-05-18 00:08:16,649 INFO ======================================================================\\\\n2026-05-18 00:08:16,649 INFO PHASE 3: Formal BCS-Controlled Experiment\\\\n2026-05-18 00:08:16,649 INFO ======================================================================\\\\n2026-05-18 00:08:16,650 INFO Loaded 25 low + 25 high batches\\\\n2026-05-18 00:08:22,712 INFO   low_0: ctrl=0.9271 treat=0.8646 Δ=-0.0625 (renamed=1)\\\\n2026-05-18 00:08:27,625 INFO   low_1: ctrl=0.9271 treat=0.8958 Δ=-0.0312 (renamed=1)\\\\n2026-05-18 00:08:32,399 INFO   low_2: ctrl=0.9375 treat=0.8958 Δ=-0.0417 (renamed=1)\\\\n2026-05-18 00:08:36,705 INFO   low_3: ctrl=0.8750 treat=0.8333 Δ=-0.0417 (renamed=1)\\\\n2026-05-18 00:08:41,441 INFO   low_4: ctrl=0.9688 treat=0.9167 Δ=-0.0521 (renamed=1)\\\\n2026-05-18 00:08:45,959 INFO   low_5: ctrl=0.9375 treat=0.9271 Δ=-0.0104 (renamed=1)\\\\n2026-05-18 00:08:48,184 INFO   low_6: ctrl=0.9271 treat=0.9271 Δ=+0.0000 (renamed=0)\\\\n2026-05-18 00:08:50,546 INFO   low_7: ctrl=0.9062 treat=0.9062 Δ=+0.0000 (renamed=0)\\\\n2026-05-18 00:08:55,141 INFO   low_8: ctrl=0.9271 treat=0.8958 Δ=-0.0312 (renamed=1)\\\\n2026-05-18 00:08:59,660 INFO   low_9: ctrl=0.8333 treat=0.8438 Δ=+0.0104 (renamed=1)\\\\n2026-05-18 00:09:04,178 INFO   low_10: ctrl=0.8333 treat=0.8229 Δ=-0.0104 (renamed=1)\\\\n2026-05-18 00:09:08,288 INFO   low_11: ctrl=0.8438 treat=0.8333 Δ=-0.0104 (renamed=1)\\\\n2026-05-18 00:09:10,389 INFO   low_12: ctrl=0.8854 treat=0.8854 Δ=+0.0000 (renamed=0)\\\\n2026-05-18 00:09:15,526 INFO   low_13: ctrl=0.9167 treat=0.8958 Δ=-0.0208 (renamed=1)\\\\n2026-05-18 00:09:20,165 INFO   low_14: ctrl=0.9375 treat=0.8854 Δ=-0.0521 (renamed=2)\\\\n2026-05-18 00:09:24,933 INFO   low_15: ctrl=0.8958 treat=0.8021 Δ=-0.0938 (renamed=1)\\\\n2026-05-18 00:09:29,380 INFO   low_16: ctrl=0.8750 treat=0.8125 Δ=-0.0625 (renamed=1)\\\\n2026-05-18 00:09:34,102 INFO   low_17: ctrl=0.9688 treat=0.9271 Δ=-0.0417 (renamed=1)\\\\n2026-05-18 00:09:36,573 INFO   low_18: ctrl=0.8542 treat=0.8542 Δ=+0.0000 (renamed=0)\\\\n2026-05-18 00:09:41,200 INFO   low_19: ctrl=0.9167 treat=0.9062 Δ=-0.0104 (renamed=2)\\\\n2026-05-18 00:09:45,885 INFO   low_20: ctrl=0.8750 treat=0.8229 Δ=-0.0521 (renamed=1)\\\\n2026-05-18 00:09:50,353 INFO   low_21: ctrl=0.9167 treat=0.9167 Δ=+0.0000 (renamed=1)\\\\n2026-05-18 00:09:55,130 INFO   low_22: ctrl=0.8958 treat=0.8854 Δ=-0.0104 (renamed=1)\\\\n2026-05-18 00:10:00,337 INFO   low_23: ctrl=0.8854 treat=0.8229 Δ=-0.0625 (renamed=1)\\\\n2026-05-18 00:10:04,980 INFO   low_24: ctrl=0.8542 treat=0.8021 Δ=-0.0521 (renamed=1)\\\\n2026-05-18 00:10:09,742 INFO   high_0: ctrl=0.6979 treat=0.5521 Δ=-0.1458 (renamed=3)\\\\n2026-05-18 00:10:14,088 INFO   high_1: ctrl=0.7083 treat=0.6667 Δ=-0.0417 (renamed=3)\\\\n2026-05-18 00:10:18,508 INFO   high_2: ctrl=0.7188 treat=0.6667 Δ=-0.0521 (renamed=4)\\\\n2026-05-18 00:10:22,509 INFO   high_3: ctrl=0.6667 treat=0.5729 Δ=-0.0938 (renamed=3)\\\\n2026-05-18 00:10:26,756 INFO   high_4: ctrl=0.6250 treat=0.5521 Δ=-0.0729 (renamed=2)\\\\n2026-05-18 00:10:30,700 INFO   high_5: ctrl=0.8438 treat=0.7188 Δ=-0.1250 (renamed=3)\\\\n2026-05-18 00:10:34,354 INFO   high_6: ctrl=0.7188 treat=0.6771 Δ=-0.0417 (renamed=4)\\\\n2026-05-18 00:10:38,146 INFO   high_7: ctrl=0.6354 treat=0.5208 Δ=-0.1146 (renamed=3)\\\\n2026-05-18 00:10:42,268 INFO   high_8: ctrl=0.8333 treat=0.7604 Δ=-0.0729 (renamed=4)\\\\n2026-05-18 00:10:46,739 INFO   high_9: ctrl=0.6562 treat=0.5521 Δ=-0.1042 (renamed=4)\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"2026-05-18 00:07:39,320 INFO Using model: /root/autodl-tmp/.hf_cache/qwen3-32b-fp8/\\n2026-05-18 00:08:00,201 INFO Loaded 960 balanced samples (80 relations)\\n2026-05-18 00:08:00,232 INFO ======================================================================\\n2026-05-18 00:08:00,232 INFO PHASE 2: Solo Accuracy Sanity Check\\n2026-05-18 00:08:00,232 INFO ======================================================================\\n2026-05-18 00:08:01,696 INFO   [OK] country of citizenship -> nationality: orig=0.833 renamed=0.833 (Δ=+0.000, n=12)\\n2026-05-18 00:08:03,003 INFO   [OK] country of origin -> land of origin: orig=0.667 renamed=0.667 (Δ=+0.000, n=12)\\n2026-05-18 00:08:04,161 INFO   [OK] father -> paternal figure: orig=1.000 renamed=1.000 (Δ=+0.000, n=12)\\n2026-05-18 00:08:05,479 INFO   [OK] follows -> comes after: orig=0.833 renamed=0.917 (Δ=+0.083, n=12)\\n2026-05-18 00:08:07,021 INFO   [OK] located in the administrative territorial entity -> situated within governing region: orig=1.000 renamed=1.000 (Δ=+0.000, n=12)\\n2026-05-18 00:08:08,266 INFO   [OK] member of -> affiliated with: orig=1.000 renamed=1.000 (Δ=+0.000, n=12)\\n2026-05-18 00:08:09,598 INFO   [OK] military rank -> service rank designation: orig=1.000 renamed=1.000 (Δ=+0.000, n=12)\\n2026-05-18 00:08:11,239 INFO   [FAIL] mother -> maternal parent: orig=0.833 renamed=0.750 (Δ=-0.083, n=12)\\n2026-05-18 00:08:12,510 INFO   [OK] part of -> integral segment of: orig=1.000 renamed=1.000 (Δ=+0.000, n=12)\\n2026-05-18 00:08:13,657 INFO   [OK] participant of -> event involvement: orig=1.000 renamed=1.000 (Δ=+0.000, n=12)\\n2026-05-18 00:08:15,325 INFO   [OK] position played on team -> athletic role on roster: orig=1.000 renamed=1.000 (Δ=+0.000, n=12)\\n2026-05-18 00:08:16,645 INFO   [OK] winner -> contest victor: orig=0.917 renamed=0.917 (Δ=+0.000, n=12)\\n2026-05-18 00:08:16,646 INFO Solo check: 11/12 passed (Δ >= -5pp)\\n2026-05-18 00:08:16,647 INFO Saved to /root/schema-dag-extraction/artifacts/exp_schema_intervention/solo_sanity_check.json\\n2026-05-18 00:08:16,648 WARNING FAILED solo checks: ['mother']\\n2026-05-18 00:08:16,649 WARNING Proceeding anyway (will note in analysis)\\n2026-05-18 00:08:16,649 INFO ======================================================================\\n2026-05-18 00:08:16,649 INFO PHASE 3: Formal BCS-Controlled Experiment\\n2026-05-18 00:08:16,649 INFO ======================================================================\\n2026-05-18 00:08:16,650 INFO Loaded 25 low + 25 high batches\\n2026-05-18 00:08:22,712 INFO   low_0: ctrl=0.9271 treat=0.8646 Δ=-0.0625 (renamed=1)\\n2026-05-18 00:08:27,625 INFO   low_1: ctrl=0.9271 treat=0.8958 Δ=-0.0312 (renamed=1)\\n2026-05-18 00:08:32,399 INFO   low_2: ctrl=0.9375 treat=0.8958 Δ=-0.0417 (renamed=1)\\n2026-05-18 00:08:36,705 INFO   low_3: ctrl=0.8750 treat=0.8333 Δ=-0.0417 (renamed=1)\\n2026-05-18 00:08:41,441 INFO   low_4: ctrl=0.9688 treat=0.9167 Δ=-0.0521 (renamed=1)\\n2026-05-18 00:08:45,959 INFO   low_5: ctrl=0.9375 treat=0.9271 Δ=-0.0104 (renamed=1)\\n2026-05-18 00:08:48,184 INFO   low_6: ctrl=0.9271 treat=0.9271 Δ=+0.0000 (renamed=0)\\n2026-05-18 00:08:50,546 INFO   low_7: ctrl=0.9062 treat=0.9062 Δ=+0.0000 (renamed=0)\\n2026-05-18 00:08:55,141 INFO   low_8: ctrl=0.9271 treat=0.8958 Δ=-0.0312 (renamed=1)\\n2026-05-18 00:08:59,660 INFO   low_9: ctrl=0.8333 treat=0.8438 Δ=+0.0104 (renamed=1)\\n2026-05-18 00:09:04,178 INFO   low_10: ctrl=0.8333 treat=0.8229 Δ=-0.0104 (renamed=1)\\n2026-05-18 00:09:08,288 INFO   low_11: ctrl=0.8438 treat=0.8333 Δ=-0.0104 (renamed=1)\\n2026-05-18 00:09:10,389 INFO   low_12: ctrl=0.8854 treat=0.8854 Δ=+0.0000 (renamed=0)\\n2026-05-18 00:09:15,526 INFO   low_13: ctrl=0.9167 treat=0.8958 Δ=-0.0208 (renamed=1)\\n2026-05-18 00:09:20,165 INFO   low_14: ctrl=0.9375 treat=0.8854 Δ=-0.0521 (renamed=2)\\n2026-05-18 00:09:24,933 INFO   low_15: ctrl=0.8958 treat=0.8021 Δ=-0.0938 (renamed=1)\\n2026-05-18 00:09:29,380 INFO   low_16: ctrl=0.8750 treat=0.8125 Δ=-0.0625 (renamed=1)\\n2026-05-18 00:09:34,102 INFO   low_17: ctrl=0.9688 treat=0.9271 Δ=-0.0417 (renamed=1)\\n2026-05-18 00:09:36,573 INFO   low_18: ctrl=0.8542 treat=0.8542 Δ=+0.0000 (renamed=0)\\n2026-05-18 00:09:41,200 INFO   low_19: ctrl=0.9167 treat=0.9062 Δ=-0.0104 (renamed=2)\\n2026-05-18 00:09:45,885 INFO   low_20: ctrl=0.8750 treat=0.8229 Δ=-0.0521 (renamed=1)\\n2026-05-18 00:09:50,353 INFO   low_21: ctrl=0.9167 treat=0.9167 Δ=+0.0000 (renamed=1)\\n2026-05-18 00:09:55,130 INFO   low_22: ctrl=0.8958 treat=0.8854 Δ=-0.0104 (renamed=1)\\n2026-05-18 00:10:00,337 INFO   low_23: ctrl=0.8854 treat=0.8229 Δ=-0.0625 (renamed=1)\\n2026-05-18 00:10:04,980 INFO   low_24: ctrl=0.8542 treat=0.8021 Δ=-0.0521 (renamed=1)\\n2026-05-18 00:10:09,742 INFO   high_0: ctrl=0.6979 treat=0.5521 Δ=-0.1458 (renamed=3)\\n2026-05-18 00:10:14,088 INFO   high_1: ctrl=0.7083 treat=0.6667 Δ=-0.0417 (renamed=3)\\n2026-05-18 00:10:18,508 INFO   high_2: ctrl=0.7188 treat=0.6667 Δ=-0.0521 (renamed=4)\\n2026-05-18 00:10:22,509 INFO   high_3: ctrl=0.6667 treat=0.5729 Δ=-0.0938 (renamed=3)\\n2026-05-18 00:10:26,756 INFO   high_4: ctrl=0.6250 treat=0.5521 Δ=-0.0729 (renamed=2)\\n2026-05-18 00:10:30,700 INFO   high_5: ctrl=0.8438 treat=0.7188 Δ=-0.1250 (renamed=3)\\n2026-05-18 00:10:34,354 INFO   high_6: ctrl=0.7188 treat=0.6771 Δ=-0.0417 (renamed=4)\\n2026-05-18 00:10:38,146 INFO   high_7: ctrl=0.6354 treat=0.5208 Δ=-0.1146 (renamed=3)\\n2026-05-18 00:10:42,268 INFO   high_8: ctrl=0.8333 treat=0.7604 Δ=-0.0729 (renamed=4)\\n2026-05-18 00:10:46,739 INFO   high_9: ctrl=0.6562 treat=0.5521 Δ=-0.1042 (renamed=4)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 33_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture of the experiment. Let me summarize:

**Rename strategy**: For 14 high-SCS relation pairs in FewRel 80-relation RE, one member of each pair was replaced with a semantically distinct paraphrase (e.g., "participant of" → "event involvement", "follows" → "prior entry", "part of" → "integral segment of", "mother" → "female progenitor"). The replacements were chosen to minimize embedding similarity (all-MiniLM-L6-v2), reducing mean pairwise SCS from 0.870 to 0.668 (mean Δ = -0.202).


I'm using the same 25 low-BCS and 25 high-BCS batches from before, running each twice with both original and renamed labels. The low-BCS batches contain 0-2 renamed types while high-BCS batches have 2-4 since they naturally have more confusable pairs. I'm testing this with Qwen3-32B F.

Now I need to locate the Limitations section and the end of the document to add a new appendix section. I can see the Limitations start around line 46, and the document ends at line 681. The appendix should be inserted after the Qualitative Error Analysis table and before the closing tag.

Looking at line 46 in the Limitations, I need to update it to reference the new appendix about the schema label renaming experiment. I'll add a reference to Appendix~\ref{app:renaming} and then create the appendix section itself with details about the controlled intervention we ran on the FewRel task, where we tested whether reducing semantic similarity between relation labels through strategic paraphrasing could improve model accuracy. Now I'm looking at the accuracy results comparing the original and renamed label conditions across both low and high-BCS batches. The renaming caused performance to drop in both groups, but the effect was substantially larger for high-BCS batches, with nearly a threefold difference in effect size between the two conditions. The unfamiliarity of the paraphrased labels appears to be the dominant factor disrupting the model's understanding of types, overshadowing any potential gains from reduced confusion between similar labels. I'm verifying the text meets the formatting constraints—no em-dashes, no -ing endings, self-contained—and checking that the appendix reference will work correctly since the new section needs to go before the document closes. Now I'll apply both edits to the file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c6b2a1-3665-4eeb-aad0-d119dd87428b",
  "uuid": "21552423-03f4-4c78-89a5-f36aeed480f2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VrMCeKJgWQjcCvEvtQJNMQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4827,
      "cache_read_input_tokens": 35463,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4827
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

_source line 34_

Now I have all the experiment details. Let me make both edits to main.tex.

**Experiment summary**:
- 14 high-SCS FewRel relation pairs renamed to semantically distinct paraphrases (e.g., "participant of" → "event involvement", "follows" → "prior entry")
- Embedding model: all-MiniLM-L6-v2; mean SCS reduced from 0.87 to 0.67
- 50 BCS-controlled batches (25 low, 25 high), count=8, 96 samples each, Qwen3-32B
- High-BCS batches had 2-4 renamed types; low-BCS had 0-2

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c6b2a1-3665-4eeb-aad0-d119dd87428b",
  "uuid": "569e9cf6-bd0d-4c5c-8889-12d35a42be0a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VrMCeKJgWQjcCvEvtQJNMQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4827,
      "cache_read_input_tokens": 35463,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4827
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

_source line 35_

<details open><summary>🔧 Tool call — Edit · `toolu_01NdwA137Bxzt3SQrtimqyjT`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "old_string": "\\item \\textbf{Causal mechanism.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway. A post-hoc schema label renaming experiment was inconclusive due to label unfamiliarity confounds.",
  "new_string": "\\item \\textbf{Causal mechanism.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway. A post-hoc renaming experiment (Appendix~\\ref{app:renaming}) confirms this concern: replacing high-SCS labels with semantically distinct paraphrases reduced pairwise embedding similarity but decreased accuracy by 3--9\\,pp, as label unfamiliarity introduced errors that outweighed any confusability reduction."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c6b2a1-3665-4eeb-aad0-d119dd87428b",
  "uuid": "8155152b-3065-4f25-8c22-6d1516a9ba0d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VrMCeKJgWQjcCvEvtQJNMQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4827,
      "cache_read_input_tokens": 35463,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4827
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

_source line 36 · 2026-05-18T21:36:15.694Z_

<details><summary>↩ Tool result · `toolu_01NdwA137Bxzt3SQrtimqyjT`</summary>

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
  "session_id": "e8c6b2a1-3665-4eeb-aad0-d119dd87428b",
  "uuid": "1efa5443-0147-4502-924f-758e6b0559fa",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "oldString": "\\item \\textbf{Causal mechanism.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway. A post-hoc schema label renaming experiment was inconclusive due to label unfamiliarity confounds.",
    "newString": "\\item \\textbf{Causal mechanism.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway. A post-hoc renaming experiment (Appendix~\\ref{app:renaming}) confirms this concern: replacing high-SCS labels with semantically distinct paraphrases reduced pairwise embedding similarity but decreased accuracy by 3--9\\,pp, as label unfamiliarity introduced errors that outweighed any confusability reduction.",
    "originalFile": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{enumitem}\n\\usepackage[normalem]{ulem}\n\\usepackage{listings}\n\n\\title{How Does Schema Complexity Predict Performance\\\\in Training-Free LLM Information Extraction?}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{experimental_setup}\n\n\\input{results}\n\n\\input{sdgd_negative}\n\n\\input{discussion}\n\n\\section*{Limitations}\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B, 70B-Instruct (FP8), and Gemini 2.5 Flash (API). Dimension~1 has been validated across all four models including a proprietary one; Dimension~2 has been verified only on open-weight models and was not robustly detectable on NER at 8B scale, likely due to floor effects.\n\n\\item \\textbf{Effect size and statistical design.} Pairwise SCS explains 1.3--1.7\\% of type confusion variance; entity frequency, prompt position, and mention ambiguity likely account for the remainder. The count $\\times$ BCS interaction is bounded under the linear specification (TOST $p = 0.003$ at $\\pm 3$\\,pp) but inconclusive on the logit scale ($p = 0.209$; Appendix~\\ref{sec:appendix_factorial}). BCS-controlled experiments use a single seed with greedy decoding; the residual SD of 0.88\\,pp (Appendix~\\ref{app:variance-decomposition}) supports robustness but precise magnitudes may vary.\n\n\\item \\textbf{Task format dependency.} BCS batch-level prediction is demonstrated only under RE's forced-choice classification format. An unconstrained decoding ablation ($n = 25$) confirms this: removing the enum constraint eliminates the BCS--accuracy correlation ($\\rho = -0.14$, $p = 0.49$), establishing that the batch-level signal is specific to forced-choice RE. NER exact-match evaluation conflates boundary and type errors, and relaxed matching may yield different confusability effect sizes.\n\n\\item \\textbf{Causal mechanism.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway. A post-hoc schema label renaming experiment was inconclusive due to label unfamiliarity confounds.\n\n\\item \\textbf{Data contamination.} FewRel (2018) may appear in pretraining corpora, but train-origin relations show numerically lower accuracy than val-origin ($-8.8$\\,pp, $p = 0.06$, n.s.), opposite to the contamination hypothesis. The monotonic degradation curve cannot be explained by uniform contamination. DocRED (2019) provides a lower-contamination-risk replication with consistent BCS--accuracy slopes ($R^2 = 0.53$). Adding train-origin ratio as a covariate leaves the BCS partial effect unchanged ($p = 0.245$; Appendix~\\ref{app:split-origin}).\n\\end{enumerate}\n\n\\paragraph{Multiple comparisons.} Cross-dataset comparisons (FewRel, DocRED, Few-NERD, MAVEN) serve as independent replications of the same hypothesis and do not require family-wise correction \\citep{rothman-1990}. Within-dataset secondary analyses (e.g., quartile comparisons, slope sensitivity checks) involve multiple looks at the same data; we report individual $p$-values and note that core claims rest on effects reaching $p < 0.001$ \\citep{dror-2018-significance,card-2020-power}.\n\n\\input{checklist}\n\n\\bibliography{references}\n\n\\appendix\n\n\\section{Additional Figures}\n\\label{sec:appendix_figures}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Llama-3.1-8B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1 & 0.702 & 0.640 \\\\\n64 & 0.273 & 0.304 \\\\\n\\midrule\nDecline & $-$43\\,pp & $-$34\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\\S\\ref{sec:model}) for fair cross-model comparison; the count-curve results in \\S\\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\\ 0.64 at count${}\\,=\\,1$) due to over-prediction under v1.}\n\\label{tab:cross_model}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{crrrrrr}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Llama-3.1-8B}} & \\multicolumn{3}{c}{\\textbf{Qwen3-32B}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Count} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} \\\\\n\\midrule\n8 & 78.1\\% & 51.0\\% & $-$27.1 & 82.3\\% & 51.0\\% & $-$31.2 \\\\\n16 & 75.5\\% & 51.6\\% & $-$23.9 & 82.8\\% & 51.6\\% & $-$31.2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\\approx$51\\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\\Delta$, in pp) is 77--87\\% as large on Llama-3.1-8B as on Qwen3-32B.}\n\\label{tab:cross_model_bcs}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrrrr}\n\\toprule\n & & \\multicolumn{5}{c}{\\textbf{BCS Bin}} & & \\\\\n\\cmidrule(lr){3-7}\n\\textbf{Task} & \\textbf{Error} & \\textbf{Solo} & \\textbf{Low} & \\textbf{Mid} & \\textbf{High} & \\textbf{V.High} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nNER & IntraSub & 0\\% & 1.6\\% & 10.6\\% & 49.4\\% & --- & 1.000 & ${<}0.001$ \\\\\nRE  & IntraSub & 0\\% & 4.2\\% & 13.0\\% & 20.3\\% & 32.3\\% & 0.954 & ${<}\\,0.001$ \\\\\n\\midrule\nNER & Missed & --- & 42.8\\% & 64.8\\% & 49.9\\% & --- & --- & --- \\\\\nRE  & Missed & --- & 10.4\\% & 11.3\\% & 13.1\\% & 15.7\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin, with Spearman $\\rho$ computed over $n=154$ individual batches (RE) and $n=148$ batches (NER). NER has 4 BCS bins; RE has 5.}\n\\label{tab:error_taxonomy}\n\\end{table}\n\n\\section{SDGD Full Protocol and Results}\n\\label{sec:appendix_sdgd}\n\nWe construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent (i.e., highly confusable) types share a color. Each color class forms one extraction batch, and predictions are merged via set union. We compare four modes: (i)~\\textbf{single\\_pass}, the undecomposed baseline; (ii)~\\textbf{sdgd\\_zero}, SCS-guided partitioning; (iii)~\\textbf{random\\_batch}, random partitioning with matched batch sizes; and (iv)~\\textbf{per\\_type}, the extreme case where each type is extracted in isolation.\n\nSingle-pass extraction achieves F1\\,=\\,0.445 (P\\,=\\,0.563, R\\,=\\,0.368). SDGD obtains F1\\,=\\,0.251 (P\\,=\\,0.210, R\\,=\\,0.314), a 44\\% relative drop. Random batching reaches F1\\,=\\,0.320 (P\\,=\\,0.249, R\\,=\\,0.446), and per-type extraction yields F1\\,=\\,0.292 (P\\,=\\,0.194, R\\,=\\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\\ref{tab:sdgd_results}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrccc}\n\\toprule\n\\textbf{Mode} & \\textbf{\\# Batches} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{F1} \\\\\n\\midrule\nsingle\\_pass & 1 & 0.563 & 0.368 & 0.445 \\\\\n\\midrule\nsdgd\\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\\\\nrandom\\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\\\\nper\\_type & 66 & 0.194 & 0.586 & 0.292 \\\\\n\\midrule\nsdgd\\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\\\\nrandom\\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \\texttt{min\\_batch\\_size=8} (reducing 8$\\to$4 batches for sdgd\\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt.}\n\\label{tab:sdgd_results}\n\\end{table}\n\nDecomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions. Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions and inflates false positives.\n\nOur v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\\_zero: 0.210$\\to$0.324; random\\_batch: 0.249$\\to$0.331), but at the cost of disproportionate recall loss (0.314$\\to$0.191; 0.446$\\to$0.276), and both modes produce lower F1 (sdgd\\_zero: 0.251$\\to$0.241; random\\_batch: 0.320$\\to$0.301).\n\n\\subsection{Practical Routing Strategies on RE}\n\\label{sec:appendix_routing}\n\nWe evaluate five non-oracle routing strategies on FewRel 80-relation RE using graph-coloring sub-schema decomposition (same grouping as Table~\\ref{tab:batch_composition}). Each strategy selects a single sub-schema for each test instance and returns that sub-schema's prediction.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{@{}lrr@{}}\n\\toprule\n\\textbf{Strategy} & \\textbf{Accuracy} & \\textbf{$\\Delta$ vs.\\ Single-Pass} \\\\\n\\midrule\nOracle (gold label) & 72.4\\% & +22.0\\,pp \\\\\n\\midrule\nMax-conf (positive only) & 36.5\\% & $-$14.0\\,pp \\\\\nNone-aware & 36.5\\% & $-$14.0\\,pp \\\\\nMargin (positive only) & 35.9\\% & $-$14.5\\,pp \\\\\nMax-conf (all) & 27.7\\% & $-$22.7\\,pp \\\\\nRandom & 14.7\\% & $-$35.7\\,pp \\\\\n\\midrule\nSingle-pass (no decomposition) & 50.4\\% & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Routing strategy comparison on FewRel 80-relation RE with graph-coloring sub-schema decomposition. Oracle requires gold labels. All practical (non-oracle) strategies perform below the single-pass baseline. The failure stems from constrained decoding (enum constraint), which forces confident predictions in every sub-schema: 73.4\\% of instances receive positive predictions from 3--5 sub-schemas simultaneously, with per-sub-schema none-rates of only 20--40\\%.}\n\\label{tab:routing_strategies}\n\\end{table}\n\n\\section{Factorial Analysis and Separability Test}\n\\label{sec:appendix_factorial}\n\nTo formally test whether count and confusability effects are additive, we fit a multiple regression (accuracy $\\sim$ $\\log_2$\\,count $+$ BCS $+$ count$\\times$BCS) across 69 batches from FewRel spanning five count levels ($k \\in \\{4, 8, 16, 32, 40\\}$). Both main effects are significant (count: $p = 0.008$; BCS: $p = 0.0002$; $R^2 = 0.52$), but the interaction term is negligible (0.47\\,pp). A TOST equivalence test with a $\\pm 3$\\,pp margin confirms that the interaction is bounded well below practical significance ($p_{\\text{TOST}} = 0.003$); this supports bounded interaction between count and confusability effects.\n\nA $2 \\times 2$ factorial sensitivity check on FewRel (count $\\in \\{8, 16\\}$, BCS low/high; $n = 54$) was inconclusive ($p_{\\text{TOST}} = 0.56$) due to limited power; this does not contradict the primary finding but limits generalization beyond the regression framework. The Few-NERD factorial (\\S\\ref{sec:multi_channel}) similarly did not reach significance ($p = 0.50$). The regression approach provides the stronger test by leveraging the full count range.\n\n\\paragraph{Equivalence margin justification.}\nWe set the $\\pm 3$\\,pp margin based on three converging anchors. \\emph{Empirical}: typical random-batch confusability variation produces 2--5\\,pp accuracy differences (batch SD $\\approx 4.6$\\,pp at count 32). \\emph{Practical}: a ${<}3$\\,pp accuracy difference falls below deployment-relevant thresholds. \\emph{Statistical}: 3\\,pp $\\approx 0.5 \\times$ batch SD, equivalent to Cohen's $d \\approx 0.5$ (medium effect threshold; \\citealt{lakens-2017-equivalence}). A 3\\,pp interaction atop the 2.2\\,pp confusability main effect would represent ${>}130\\%$ amplification, fundamentally changing whether confusability warrants mitigation. At $\\pm 2$\\,pp (marginally equivalent, $p = 0.047$), interaction remains bounded below the main effect itself.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{crrl}\n\\toprule\n\\textbf{Margin (pp)} & \\textbf{$t_{\\text{upper}}$} & \\textbf{$p_{\\text{TOST}}$} & \\textbf{Conclusion} \\\\\n\\midrule\n$\\pm 1$ & $-0.59$ & $0.278$ & Inconclusive \\\\\n$\\pm 2$ & $-1.70$ & $0.047$ & Equivalent \\\\\n$\\pm 3$ & $-2.81$ & $0.003$ & Equivalent \\\\\n$\\pm 5$ & $-5.02$ & ${<}\\,0.001$ & Equivalent \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{TOST sensitivity analysis across equivalence margins. The interaction effect (0.47\\,pp, 90\\% CI [$-$1.0, 2.0]\\,pp) is bounded below 2\\,pp at marginal significance ($p = 0.047$); the $\\pm 3$\\,pp choice does not drive the equivalence conclusion. At $\\pm 1$\\,pp, equivalence is inconclusive ($p = 0.278$), meaning interaction could reach approximately half the main effect magnitude.}\n\\label{tab:tost_sensitivity}\n\\end{table}\n\n\\paragraph{Logit-scale sensitivity.}\nBecause accuracy near 50\\% compresses interaction effects on the linear scale, we refit the regression on logit-transformed accuracy. The logit-scale interaction (0.111 logit units, $p = 0.047$, 90\\% CI [0.019, 0.203]) is marginally significant, and TOST at the equivalent $\\pm 3$\\,pp margin ($\\pm 0.156$ logit at median accuracy) is inconclusive ($p_{\\text{TOST}} = 0.209$). However, back-transforming the interaction to the probability scale at the observed floor ($p = 0.51$) yields 2.78\\,pp, still within the $\\pm 3$\\,pp margin; at the median baseline ($p = 0.65$), the back-transformed effect is 2.53\\,pp. The logit TOST is inconclusive due to limited power ($n = 69$, wide CI) rather than a large effect size: the point estimate remains below the equivalence bound at all observed baselines. We retain the linear-scale TOST as the primary test and report this logit analysis as a sensitivity check.\n\n\\section{Within-Pool CI Details}\n\\label{sec:appendix_within_pool}\n\nThe quartile $\\Delta$ for 80-pool 16-relation subsets ($-$3.92\\,pp, 95\\% CI [$-$8.17, $+$0.38]) crosses zero, reflecting the compressed BCS range within that pool (0.46--0.68 vs.\\ 0.48--0.71 for the independent pool). Within this narrow band, the quartile contrast lacks statistical power to detect the effect that the regression identifies. The full 80-relation condition ($n = 25$) is underpowered for both the slope (CI: [$-$1.303, $+$1.695]) and quartile analyses; we include it in Table~\\ref{tab:within_pool} for completeness but do not draw inferential conclusions from it.\n\n\\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}\n\\label{sec:appendix_residualized_bcs}\n\nSection~\\ref{sec:centrality_confound} identifies a centrality confound in MAVEN's per-type BCS--F1 correlation: both embeddings show a \\emph{positive} raw correlation, opposite to the expected direction. Here we formalize this analysis by identifying specific confounders for each embedding and testing whether the BCS--F1 relationship survives partial correlation controlling for these confounders.\n\n\\paragraph{Confound identification.}\nFor each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:\n\\begin{itemize}[itemsep=2pt,leftmargin=*]\n\\item \\textbf{MiniLM}: BCS correlates with log type frequency ($r = 0.201$). Frequent types have more training signal and are extracted more reliably, which produces the positive BCS--F1 association.\n\\item \\textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors, central, well-represented types that the model extracts well.\n\\end{itemize}\n\n\\paragraph{Partial correlation results.}\nTable~\\ref{tab:residualized_bcs} reports raw Spearman $\\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Embedding} & \\textbf{Control} & \\textbf{Raw $\\rho$} & \\textbf{Raw $p$} & \\textbf{Partial $r$} & \\textbf{Partial $p$} \\\\\n\\midrule\nMiniLM & --- & $+$0.208 & $0.011$ & --- & --- \\\\\nMiniLM & log freq & --- & --- & $+$0.133 & $0.11$ \\\\\nMiniLM & log freq $+$ degree & --- & --- & --- & $0.23$ \\\\\n\\midrule\nQwen3 & --- & $+$0.184 & $0.025$ & --- & --- \\\\\nQwen3 & degree centrality & --- & --- & $+$0.063 & $0.44$ \\\\\nQwen3 & log freq $+$ degree & --- & --- & --- & $0.44$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{MAVEN per-type BCS--F1 correlation before and after controlling for centrality confounders. Raw correlations are Spearman $\\rho$; partial correlations are Pearson $r$ from residualized regression. Degree centrality is computed on the SCS graph at threshold 0.7. All values from experiment \\texttt{exp\\_maven\\_residualized\\_bcs}.}\n\\label{tab:residualized_bcs}\n\\end{table}\n\n\\paragraph{Interpretation.}\nThe two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality (the count of strong semantic neighbors) becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.\n\nUnder joint control, both embeddings yield $p > 0.2$; the raw positive BCS--F1 correlation on MAVEN is thus fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 0.001$; Table~\\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.\n\n\\section{Batch Composition Results}\n\\label{sec:appendix_batch_composition}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Accuracy} & \\textbf{Mean BCS} \\\\\n\\midrule\nSingle-pass (80 types) & 0.504 & 0.557 \\\\\nRandom batching (15 seeds)$^\\dagger$ & 0.788\\,$\\pm$\\,0.018 & 0.559 \\\\\nConfus.-aware (graph coloring) & \\textbf{0.802} & 0.552 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Batch composition on FewRel 80-relation RE with oracle routing. $^\\dagger$Mean $\\pm$ SD across 15 random seeds.}\n\\label{tab:batch_composition}\n\\end{table}\n\nSee the accompanying discussion in \\S\\ref{sec:sdgd}.\n\n\\input{prompt_appendix}\n\n\\section{Prompt Version Sensitivity Analysis}\n\\label{sec:appendix_prompt_sensitivity}\n\nWe assess whether the confusability effects reported in \\S\\ref{sec:bcs_controlled}--\\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\paragraph{RE (FewRel).}\nUnder the v1 prompt, the extreme-batch BCS gap (Table~\\ref{tab:bcs_controlled}) is substantial. Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; 95\\% CI: [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\\,pp (CI: [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal, a cautionary note for small-sample prompt sensitivity studies.\n\n\\paragraph{NER (Few-NERD).}\nThe batch-level BCS--F1 correlation is null under both prompt versions. Pooling across three seeds and all count levels ($n = 450$), the correlation is $r = 0.004$ ($p = 0.94$). An earlier small-sample analysis ($n = 27$, single seed) had reported positive correlations ($r = +0.50$/$+0.58$), but these were driven by an accidental BCS--type-frequency confound: those 27 batches exhibited $r(\\text{BCS}, \\text{freq}) = 0.53$, creating a spurious path through frequency to F1. After controlling for type frequency, the partial correlation is non-significant in both the small ($r = 0.28$, $p = 0.16$) and large ($r = -0.12$, $p = 0.29$) samples. The pairwise SCS--confusion analysis (\\S\\ref{sec:pairwise}), which is immune to this batch-level aggregation artifact, remains the primary evidence for the NER confusability dimension.\n\n\\paragraph{Interpretation.}\nThe $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\\,pp) but remains highly significant ($p < 0.001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\\% vs.\\ 82.3\\%), but type confusion under high confusability persists (59.7\\% vs.\\ 51.0\\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary source. The underlying confusability signal (pairwise SCS--confusion correlation and the directional BCS--accuracy relationship) persists across both prompt versions.\n\n\\subsection{Cross-Prompt-Variant BCS Correlation}\n\\label{sec:appendix_prompt_variants}\n\nTo verify that the BCS--accuracy relationship is not an artifact of a specific prompt template, we evaluate four structurally distinct prompt variants on FewRel 80-relation RE at two count levels (8 and 32), with 10 random batches per condition.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{llrrrr}\n\\toprule\n\\textbf{Variant} & \\textbf{Count} & \\textbf{Mean Acc} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nV2 (definition-first) & 8 & 0.769 & $-$0.333 & 0.348 \\\\\nV2 (definition-first) & 32 & 0.564 & $-$0.648 & 0.043 \\\\\nInstruction-rewrite & 8 & 0.847 & $-$0.223 & 0.536 \\\\\nInstruction-rewrite & 32 & 0.662 & $-$0.469 & 0.171 \\\\\nChain-of-thought & 8 & 0.749 & $+$0.254 & 0.478 \\\\\nChain-of-thought & 32 & 0.617 & $-$0.566 & 0.088 \\\\\nMinimal & 8 & 0.852 & $-$0.170 & 0.638 \\\\\nMinimal & 32 & 0.615 & $-$0.771 & 0.009 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS--accuracy Pearson correlation across four prompt variants. At count 32, all four variants show negative BCS--accuracy correlations ($r \\leq -0.47$), with two reaching $p < 0.05$. At count 8, the narrower BCS range reduces statistical power.}\n\\label{tab:prompt_variants}\n\\end{table}\n\nAt count 32, all four variants produce negative BCS--accuracy correlations ($r$ ranges from $-$0.47 to $-$0.77), with V2 ($p = 0.043$) and Minimal ($p = 0.009$) reaching significance and Chain-of-thought approaching it ($p = 0.088$). At count 8, correlations are weaker and nonsignificant across all variants, consistent with the narrower BCS range at lower schema complexity reducing the detectable effect size. Rather than applying Bonferroni correction, which assumes independent hypotheses inappropriate for correlated prompt variants testing the same underlying signal, we note directional consistency: 7 of 8 conditions show negative BCS--accuracy slopes, consistent with the primary finding \\citep{rothman-1990}. These results confirm that the confusability effect arises from schema composition, not prompt-specific phrasing.\n\n\\section{BCS Aggregation Sensitivity}\n\\label{sec:appendix_bcs_sensitivity}\n\nWe define Batch Confusability Score (BCS) as the \\emph{mean} pairwise SCS across all type pairs in a batch (\\S\\ref{sec:bcs_controlled}). An alternative definition takes the \\emph{maximum} pairwise SCS within each batch to capture the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Aggregation} & \\textbf{Condition} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nMEAN (primary) & 16-rel & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ \\\\\nMEAN & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\midrule\nMAX & 16-rel & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}\\,0.001$ \\\\\nMAX & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS--accuracy regression under mean vs.\\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p \\approx 0.60$; MAX $p \\approx 0.44$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}\n\\label{tab:bcs_aggregation}\n\\end{table}\n\nMAX aggregation yields stronger correlations ($r = -0.637$ vs.\\ $-0.467$ for 16-rel), consistent with the hypothesis that the single most confusable pair in a batch predicts substitution errors. Both definitions produce significant negative slopes across all conditions, and the permutation tests confirm no significant difference between independent and sampled pools under either definition. We adopt MEAN as the primary definition because it better represents average pairwise difficulty across all schema combinations, while MAX may overweight a single outlier pair. The choice does not affect any paper conclusion.\n\n\\section{BCS-Controlled Detailed Results}\n\\label{app:bcs-controlled-table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\n\\paragraph{Adjusted $R^2$ and confidence intervals.}\nDocRED regressions (\\S\\ref{sec:bcs_controlled}) use OLS on $n = 35$ batches (5 high-BCS + 5 low-BCS + 25 random) with one predictor. At count 16, adjusted $R^2 = 0.511$ (unadjusted: 0.525; 95\\% CI via Fisher $z$-transformation: [0.27, 0.73]); at count 32, adjusted $R^2 = 0.426$ (unadjusted: 0.443; CI: [0.18, 0.67]). The small shrinkage ($\\Delta R^2 \\leq 0.02$) indicates the unadjusted values are not inflated by the predictor-to-sample ratio.\n\n\\section{Within-Pool Analysis Methodology}\n\\label{app:within-pool-method}\n\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ & $-$5.31 & [$-$7.44, $-$3.19] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & $0.027$ & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$)$^\\dagger$ & $+$0.221 & [$-$1.303, $+$1.695] & $+$0.064 & $0.76$ & $-$1.04 & [$-$10.12, $+$8.04] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p \\approx 0.60$ (5{,}000 permutations)} \\\\\n\\multicolumn{7}{l}{\\footnotesize $^\\dagger$BCS range (IQR\\,=\\,0.033) insufficient for regression; slope not interpretable.} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\end{table}\n\nThe within-pool slope ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.509; permutation $p \\approx 0.60$). The smaller quartile gap ($-$3.92\\,pp vs.\\ $-$5.31\\,pp) reflects the narrower BCS range within the 80-relation pool (Appendix~\\ref{sec:appendix_within_pool}).\n\nIn the full 80-relation condition, natural BCS variation is insufficient (IQR${}=0.033$) to yield a detectable effect ($n=25$, slope${}=+0.221$, $p \\approx 0.76$). This does not invalidate the confusability effect; the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied, but establishes that natural schema sampling at this scale does not produce sufficient BCS contrast for detection.\n\n\\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}\n\\label{app:scs-ablation}\n\nTable~\\ref{tab:scs-ablation} compares predictive accuracy of name-only SCS against name+definition SCS across three datasets.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lcccc}\n\\toprule\nDataset & SCS$_\\text{name}$ $r$ & SCS$_\\text{def}$ $r$ & $\\Delta r$ & Matrix corr. \\\\\n\\midrule\nFew-NERD & 0.172 & 0.149 & $-$0.023 & 0.894 \\\\\nMAVEN & 0.129 & 0.164 & +0.035 & 0.656 \\\\\nFewRel & 0.178 & 0.193 & +0.015 & 0.848 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pearson correlation between SCS and empirical confusion rate. ``Def'' concatenates type name with definition before embedding. All correlations significant ($p < 0.001$). The inconsistent direction of $\\Delta r$ indicates that definitions provide no systematic benefit.}\n\\label{tab:scs-ablation}\n\\end{table}\n\nFew-NERD is the only dataset whose prompts include type definitions; for MAVEN and FewRel, prompts use type names alone, so name-only SCS directly matches model input. The high matrix correlation (0.66--0.89) confirms that type names capture the dominant semantic structure.\n\n\\paragraph{Held-out validation.}\n\\label{app:scs-heldout-validation}\nFrom the 80-type confusion matrix, we extract the $\\binom{16}{2} = 120$ pairs among the 16 validation-origin types (fully disjoint from the 64 training-pool types). The SCS--confusion Spearman correlation remains positive and significant ($\\rho = 0.216$, $p = 0.018$), nearly identical to the full 80-type pool ($\\rho = 0.218$, $p < 10^{-34}$, $n = 3{,}160$ pairs), ruling out training-set contamination as the driver of the observed relationship.\n\n\\section{Pair-to-Batch Aggregation Simulation}\n\\label{app:aggregation-sim}\n\nThe following simulation provides an illustrative explanatory model for how pair-level effects aggregate to batch-level variance. It is not the evidence base for our claims; the observed batch-level $R^2 = 0.218$ (\\S\\ref{sec:practical_magnitude}) is a direct empirical measurement independent of this simulation.\n\n\\paragraph{Setup.} We examine whether the pair-level $R^2 \\approx 7\\%$ (computed over non-zero confusion pairs) can aggregate to the observed batch-level $R^2 \\approx 22\\%$ via a Monte Carlo simulation. From the FewRel 16-relation experiment, we estimate the inter-pair SCS correlation for pairs sharing a common type ($\\rho_\\text{SCS} = 0.35$). For batches of $k=8$ types ($\\binom{8}{2}=28$ pairs), we simulate 10{,}000 iterations: (1) generate 28 correlated pair-level effects with individual $R^2 = 0.074$; (2) average to obtain batch-level signals; (3) compute batch-level $R^2$.\n\n\\paragraph{Results.} Simulated batch $R^2 = 0.219$ [95\\% CI: 0.092--0.361], matching the observed value of 0.218. The effective amplification factor is $\\sim$3$\\times$, explained by signal correlation within batches preserving variance while independent noise averages out (effective degrees of freedom $\\approx 3.4$, not 28).\n\n\\paragraph{Unconditional baseline.}\nWhen the simulation uses the unconditional pairwise $r^2 = 0.013$ (computed over all type pairs including zero-confusion pairs; Table~\\ref{tab:pairwise}), the simulated batch-level $R^2$ drops to $0.044$ [95\\% CI: 0.001--0.151], well below the observed $R^2 = 0.218$. The analytical formula confirms: $\\text{SNR} \\times \\text{EF} / (\\text{SNR} \\times \\text{EF} + 1) = 0.042$ with the same effective factor $\\text{EF} = 3.35$. This ${\\sim}5\\times$ gap reflects the dilution from zero-confusion pairs: approximately 89\\% of type pairs never exhibit mutual confusion, contributing only noise to the unconditional correlation. The conditional model ($R^2 = 0.074 \\to 0.219$) matches the observed value because it isolates the minority of semantically proximate pairs that actually compete during type resolution; BCS predicts batch accuracy through the density of \\emph{active} confusable pairs, not uniform contributions from all pairs.\n\n\\paragraph{Sensitivity to $\\rho$.}\nThe inter-pair SCS correlation $\\rho = 0.35$ is estimated from pairs sharing a common type. At $\\rho = 0.20$ (halved correlation), a parallel simulation yields batch $R^2 \\approx 0.22$, still matching the observed value; at $\\rho = 0.50$, the correlation structure approaches the positive-definiteness boundary; $\\rho = 0.35$ thus sits in a stable regime. The simulation is illustrative; the observed batch $R^2 = 0.218$ is the primary evidence.\n\n\\section{BCS Independence from Type Composition}\n\\label{app:bcs-composition}\n\nFewRel's balanced design (700 instances per type) makes type frequency invariant across batches, ruling out frequency-driven confounding. To test whether BCS captures information beyond type composition effects, we decompose the explained variance in a joint model (accuracy $\\sim$ BCS $+$ mean type difficulty), where type difficulty is the per-type solo-baseline accuracy averaged across batch members. On 100 random 8-type batches from the 16-relation pool, the joint model explains $R^2 = 0.704$. Variance decomposition yields: BCS unique $R^2 = 0.259$ (36.8\\% of explained variance), composition unique $R^2 = 0.298$ (42.3\\%), and shared $R^2 = 0.147$ (20.9\\%). The near-orthogonality of predictors (VIF${}\\,=\\,1.06$, $r(\\text{BCS}, \\text{difficulty}) = -0.21$) confirms that BCS captures confusability-specific signal rather than a proxy for type difficulty.\n\n\\section{SCS vs.\\ Simple Baselines}\n\\label{app:scs-baselines}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Metric} & \\textbf{Spearman $\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nFewRel & SCS (embedding) & \\textbf{0.218} & $2.2 \\times 10^{-35}$ \\\\\n(3{,}160 pairs) & Same-parent (WordNet) & 0.097 & $5.4 \\times 10^{-8}$ \\\\\n& WordNet Wu-Palmer & 0.073 & $4.3 \\times 10^{-5}$ \\\\\n& Levenshtein & 0.016 & 0.363 (n.s.) \\\\\n\\midrule\nFew-NERD & SCS (embedding) & \\textbf{0.166} & $1.5 \\times 10^{-13}$ \\\\\n(1{,}953 pairs) & Levenshtein & 0.152 & $1.4 \\times 10^{-11}$ \\\\\n& Same-parent (prefix) & 0.146 & $7.8 \\times 10^{-11}$ \\\\\n& WordNet Wu-Palmer & 0.054 & 0.070 (n.s.)$^\\dagger$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise confusion prediction: SCS vs.\\ simple baselines. Spearman $\\rho$ between each metric and the empirical confusion rate. SCS outperforms all baselines on FewRel; the margin is smaller on Few-NERD, where hierarchical naming conventions provide partial signal to string-based metrics. $^\\dagger$42\\% of pairs lack WordNet coverage.}\n\\label{tab:scs_baselines}\n\\end{table}\n\n\\section{Split-Origin Covariate Analysis}\n\\label{app:split-origin}\n\nFewRel combines 64 train-split and 16 val-split relation types into a single 80-type pool.  Train-origin types show numerically lower accuracy ($-8.8$\\,pp, $p = 0.06$; see Limitations), raising the question of whether differential pre-training exposure confounds the BCS--accuracy relationship.  We test this by adding a per-batch \\emph{train-origin ratio} (fraction of relation types drawn from the train split) as a covariate in the BCS--accuracy regression.\n\n\\paragraph{Method.}  Across 213 multi-type batches ($k \\geq 2$) from the batch-composition experiment (\\S\\ref{sec:sdgd}) and the factorial design (\\S\\ref{sec:bcs_controlled}), we compute $\\texttt{train\\_origin\\_ratio} = n_{\\text{train}} / k$ for each batch.  The ratio ranges from 0.40 to 1.00 (mean 0.80, consistent with the 64/80 base rate).  We fit:\n{\\small\\begin{equation*}\n\\text{acc} = \\beta_0 + \\beta_{\\text{BCS}} \\!\\cdot\\! \\text{BCS} + \\beta_{\\text{orig}} \\!\\cdot\\! \\text{train\\_origin\\_ratio} + \\varepsilon\n\\end{equation*}}\n\n\\paragraph{Results.}  The BCS partial effect is unchanged after controlling for split-origin: $\\beta_{\\text{BCS}} = -0.416$, $p < 10^{-16}$ (vs.\\ $\\beta = -0.412$, $p < 10^{-16}$ without the covariate).  Train-origin ratio is not independently significant ($\\beta_{\\text{origin}} = -0.057$, $p = 0.245$), and $\\Delta R^2 = 0.005$.  The BCS--accuracy relationship is therefore not confounded by differential pre-training exposure at the batch level.\n\nPairwise SCS distributions do not differ significantly between train-origin (64 types, mean\\,=\\,0.880) and val-origin (16 types, mean\\,=\\,0.874) subsets (Mann-Whitney $p = 0.754$, Cohen's $d = 0.081$); the train/val split does not introduce systematic confusability bias.\n\n\\section{Cross-Seed Variance Decomposition}\n\\label{app:variance-decomposition}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{rrrr}\n\\toprule\n\\textbf{Count} & \\textbf{Batch SD} & \\textbf{Seed SD} & \\textbf{Ratio} \\\\\n\\midrule\n4 & 0.0889 & 0.0122 & 53.5 \\\\\n8 & 0.0820 & 0.0098 & 70.0 \\\\\n16 & 0.0626 & 0.0270 & 5.4 \\\\\n32 & 0.0462 & 0.0091 & 26.0 \\\\\n40 & 0.0421 & 0.0019 & 474.4 \\\\\n64 & 0.0245 & 0.0022 & 119.8 \\\\\n80 & 0.0001 & 0.0088 & $<$0.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Variance decomposition on FewRel (3 seeds $\\times$ 25 batches per count level). Batch SD: root-mean intra-seed variance averaged over seeds. Seed SD: standard deviation of per-seed means. Ratio = batch variance / seed variance. At count 80, only one batch composition exists, so batch variance vanishes by construction.}\n\\label{tab:variance_decomposition}\n\\end{table}\n\nIntra-batch variance dominates inter-seed variance by 5--474$\\times$ across count levels 4--64 (mean 125$\\times$); random batch composition is the primary source of performance variability. Under greedy decoding (temperature${}\\,=\\,0$), model inference is nearly deterministic; the inter-seed variance reflects differences in which random batch compositions each seed generates, not inference stochasticity. At count 80, the full schema admits only one composition, leaving residual model-level noise as the sole variance source (seed SD = 0.88\\,pp, likely attributable to FP8 quantization non-determinism).\n\n\\section{Cross-Domain Connections}\n\\label{app:cross-domain}\n\nThe schema-associated degradation documented here is not unique to information extraction. Schema-Guided Dialogue systems (SGD/SGD-X; \\citealt{rastogi2020towards}) face an analogous challenge: as the number of intent and slot types grows, dialogue state tracking accuracy declines. \\citet{li2023evaluating} observed count-dependent degradation in ChatGPT-based IE, attributing it to prompt overload. Our two-dimensional decomposition offers a more refined explanation: schema size per se is not the sole predictor; rather, larger schemas increase the probability of including high-SCS pairs, which contribute disproportionately to confusion. This distinction has practical implications: a schema of 80 types with low mutual confusability may outperform a 40-type schema with clustered semantics, and suggests that confusability-aware design principles may generalize to any task where an LLM must discriminate among a prompt-specified label inventory.\n\n\\section{Cross-Model Validation with LLaMA-3.1-70B-Instruct (FP8)}\n\\label{sec:appendix_cross_model_70b}\n\nTo test whether the two-dimensional degradation pattern generalizes across model families, we replicate the count-curve and BCS-controlled experiments on Meta-LLaMA-3.1-70B-Instruct (FP8 quantization). All batch compositions, type pools, and test samples are identical to those used for Qwen3-32B (\\S\\ref{sec:count_curves}, \\S\\ref{sec:bcs_controlled}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{LLaMA-70B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{RE (FewRel, Classification Accuracy)}} \\\\\n8  & 0.757 & 0.805 \\\\\n16 & 0.685 & 0.719 \\\\\n32 & 0.601 & 0.652 \\\\\n64 & 0.504 & 0.539 \\\\\n80 & 0.450 & 0.504 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{NER (Few-NERD, Text+Type Match Recall)}} \\\\\n2  & 0.323 & 0.515 \\\\\n6  & 0.300 & 0.399 \\\\\n12 & 0.278 & 0.318 \\\\\n22 & 0.252 & 0.279 \\\\\n44 & 0.297 & 0.309 \\\\\n66 & 0.273 & 0.407 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count curves for LLaMA-3.1-70B-Instruct (FP8) and Qwen3-32B. RE decline (count 8$\\to$80): $-$30.7\\,pp (70B) vs.\\ $-$30.1\\,pp (32B). NER decline (count 2$\\to$22): $-$7.1\\,pp (70B) vs.\\ $-$23.6\\,pp (32B); both models exhibit a U-shaped rebound at higher counts. 25 batches per count level, same samples and batch compositions across models (seed 42). All metrics are micro-averaged across batches.}\n\\label{tab:cross_model_70b}\n\\end{table}\n\nTable~\\ref{tab:cross_model_70b} shows that RE degradation slopes are near-identical: $-$30.7\\,pp (70B) versus $-$30.1\\,pp (32B) from count 8 to count 80, with the 70B model approximately 4\\,pp lower in absolute accuracy at each count level. This quantitative match provides strong evidence that Dimension~1 (count-related decline) is directionally consistent across architectures for RE.\n\nOn NER, the count-related decline direction is consistent across models: both 70B and Qwen3 show a recall decline from count 2 to count 22 (70B: 0.323$\\to$0.252, $-$7.1\\,pp; Qwen3: 0.515$\\to$0.279, $-$23.6\\,pp). Both models also exhibit a U-shaped rebound at higher counts (70B: 0.252 at count 22 $\\to$ 0.297 at count 44; Qwen3: 0.279 at count 22 $\\to$ 0.407 at count 66), which cross-validates the U-shape phenomenon. The magnitude difference reflects a precision-recall tradeoff: 70B operates more conservatively (higher precision, lower recall), while Qwen3 over-predicts (higher recall, lower precision, especially at low counts).\n\nFor the confusability dimension (Dimension 2), at count 16 on FewRel, LLaMA-70B achieves low-BCS accuracy of 0.708 versus high-BCS accuracy of 0.599 ($\\Delta = +10.9$\\,pp, 95\\% CI: [$+$3.0, $+$20.1]). The confidence interval excludes zero; the confusability effect is thus confirmed at the 70B scale.\n\nIn summary, FewRel RE provides a quantitative match across models (near-identical slopes for Dimension~1 and a significant Dimension~2 effect). NER provides directional consistency: the count-related decline direction is preserved and the U-shaped rebound replicates, though magnitudes vary with each model's precision-recall operating point. Together, these results indicate that the degradation pattern is directionally consistent across architectures.\n\n\\section{Cross-Model Validation with Gemini 2.5 Flash (API)}\n\\label{sec:appendix_cross_model_gemini}\n\nWe further validate Dimension~1 on a proprietary model, Gemini 2.5 Flash \\citep{gemini-2025}, accessed via API. This extends the cross-model evidence from open-weight families (Qwen, LLaMA) to a proprietary architecture with unknown training details. We replicate the FewRel count-curve experiment using the same 960 balanced samples, batch compositions, and evaluation protocol as Qwen3-32B.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Gemini Flash} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1  & 0.827 & --- \\\\\n4  & 0.873 & 0.870 \\\\\n8  & 0.820 & 0.805 \\\\\n16 & 0.787 & 0.719 \\\\\n32 & 0.739 & 0.652 \\\\\n64$^\\dagger$ & 0.637 & 0.539 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count curves for Gemini 2.5 Flash (API) and Qwen3-32B on FewRel RE (classification accuracy). 25 batches per count level, same samples and batch compositions (seed 42). Gemini's count-1 result is included for completeness; Qwen3 count-1 was not collected. Both models show monotonic decline from count 4 onward ($\\rho = -1.0$ for both on counts 4--32). $^\\dagger$Count 64: Gemini based on 11/25 batches (partial).}\n\\label{tab:cross_model_gemini}\n\\end{table}\n\nTable~\\ref{tab:cross_model_gemini} confirms that the count-related accuracy decline replicates on Gemini 2.5 Flash. From count 4 to count 32, both models show perfectly monotonic decline (Spearman $\\rho = -1.0$). Including count 1, the Gemini count curve yields $\\rho = -0.900$ ($p = 0.037$); including partial count-64 data (11/25 batches), $\\rho = -0.943$ ($p = 0.005$). The decline magnitude is smaller for Gemini ($-$13.3\\,pp from count 4 to 32) than for Qwen3 ($-$21.8\\,pp), consistent with Gemini's higher absolute accuracy providing more headroom before degradation saturates. At each count level, Gemini matches or exceeds Qwen3, with the gap widening at higher counts (0.3\\,pp at count 4 vs.\\ 8.7\\,pp at count 32, 9.8\\,pp at partial count 64); Gemini appears more robust to schema scaling but not immune. Dimension~2 (BCS-controlled confusability) has not been tested on proprietary models; cross-architecture Dimension~2 validation remains for future work.\n\n\\section{Few-Shot Prompting and Confusability}\n\\label{sec:appendix_fewshot_bcs}\n\nTo test whether in-context demonstrations mitigate the BCS-associated confusability effect, we evaluate 0-shot, 1-shot, and 5-shot prompting on FewRel 80-relation RE at count 8 using the same extreme-BCS batch design as \\S\\ref{sec:bcs_controlled}. Each condition uses 50 batches (25 low-BCS, mean $\\approx 0.36$; 25 high-BCS, mean $\\approx 0.80$), drawn from the pre-constructed batch pool of \\S\\ref{sec:bcs_controlled}. Few-shot examples are sampled from the FewRel training split for each target type.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lrrrl}\n\\toprule\n\\textbf{Condition} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n0-shot & 0.682 & 0.498 & +18.5 & {[}+14.3, +22.7{]} \\\\\n1-shot & 0.754 & 0.554 & +20.0 & {[}+16.3, +23.5{]} \\\\\n5-shot & 0.715 & 0.488 & +22.8 & {[}+18.9, +26.8{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS gap under few-shot prompting (FewRel, count 8). Demonstrations improve absolute accuracy on low-BCS batches (+3.3--7.2\\,pp over 0-shot) but provide inconsistent benefit on high-BCS batches (+5.6\\,pp at 1-shot, $-$1.0\\,pp at 5-shot). The confusability gap widens from +18.5\\,pp (0-shot) to +22.8\\,pp (5-shot). All metrics are micro-averaged across batches.}\n\\label{tab:fewshot_bcs}\n\\end{table}\n\nDemonstrations improve absolute accuracy primarily on low-BCS (easy) batches, where type boundaries are already distinct and examples reinforce correct mappings. On high-BCS batches, where types are semantically confusable, demonstrations provide inconsistent benefit (+5.6\\,pp at 1-shot, $-$1.0\\,pp at 5-shot): the model still substitutes similar types at comparable rates. The net effect is that the confusability gap widens under few-shot prompting (+4.3\\,pp from 0-shot to 5-shot, bootstrap $p = 0.014$), with all three confidence intervals excluding zero. This indicates that BCS-associated type confusion is a structural property of the schema composition rather than a deficit addressable through prompt engineering. The non-monotonic low-BCS pattern (0.754 at 1-shot vs.\\ 0.715 at 5-shot) may reflect lost-in-middle effects from increased prompt length \\cite{lost-in-middle-2024}.\n\nThe 0-shot gap (+18.5\\,pp) is smaller than the extreme-batch gap reported in \\S\\ref{sec:bcs_controlled} (+25.5\\,pp) because the two experiments use different test splits and batch sampling seeds; direct magnitude comparison across experiments is not appropriate.\n\n\\section{Qualitative Error Analysis}\n\\label{app:error-analysis}\n\nTables~\\ref{tab:top10_re} and~\\ref{tab:top10_ner} list the ten most frequently confused type pairs on FewRel 80-relation RE and Few-NERD NER. Confusion counts are aggregated bidirectionally across three random seeds (72{,}000 predictions per seed for RE; single-seed 66-type extraction for NER).\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\begin{tabular}{clllr}\n\\toprule\n\\textbf{\\#} & \\textbf{Type A} & \\textbf{Type B} & \\textbf{SCS} & \\textbf{$N$} \\\\\n\\midrule\n1 & instance of & taxon rank & 0.53 & 875 \\\\\n2 & child & father & 0.84 & 700 \\\\\n3 & participant of & participating team & 0.75 & 675 \\\\\n4 & mountain range & part of & 0.57 & 575 \\\\\n5 & mouth of watercourse & tributary & 0.65 & 549 \\\\\n6 & child & mother & 0.84 & 500 \\\\\n7 & league & member of & 0.66 & 450 \\\\\n8 & country of citizenship & country of origin & 0.76 & 400 \\\\\n9 & followed by & follows & 0.90 & 400 \\\\\n10 & occupation & voice type & 0.57 & 400 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Top-10 confused relation pairs on FewRel 80-relation RE. $N$: bidirectional confusion count aggregated over 3 seeds $\\times$ 25 batches. SCS: pairwise Schema Confusability Score (Qwen3 embedding cosine similarity). High-SCS pairs (e.g., \\textit{followed by}/\\textit{follows}, SCS\\,=\\,0.90) and family-relation pairs (\\textit{child}/\\textit{father}, \\textit{child}/\\textit{mother}) dominate. Some low-SCS pairs (\\textit{instance of}/\\textit{taxon rank}, SCS\\,=\\,0.53) reflect domain-specific co-occurrence rather than semantic similarity.}\n\\label{tab:top10_re}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\begin{tabular}{clllr}\n\\toprule\n\\textbf{\\#} & \\textbf{Type A} & \\textbf{Type B} & \\textbf{SCS} & \\textbf{$N$} \\\\\n\\midrule\n1 & person-other & person-politician & 0.93 & 121 \\\\\n2 & location-GPE & organization-other & 0.83 & 81 \\\\\n3 & art-film & location-GPE & 0.69 & 57 \\\\\n4 & building-other & location-GPE & 0.85 & 56 \\\\\n5 & building-other & person-other & 0.90 & 43 \\\\\n6 & location-GPE & product-other & 0.69 & 39 \\\\\n7 & org-gov/agency & person-other & 0.85 & 34 \\\\\n8 & person-actor & person-other & 0.90 & 34 \\\\\n9 & building-other & location-road/transit & 0.76 & 32 \\\\\n10 & location-GPE & org-sportsleague & 0.81 & 30 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Top-10 confused entity type pairs on Few-NERD NER. $N$: bidirectional confusion count from 66-type full-schema extraction. SCS: pairwise Schema Confusability Score (Qwen3 embedding cosine similarity). Intra-category confusions (e.g., \\textit{person-other}/\\textit{person-politician}, SCS\\,=\\,0.93) and cross-category pairs sharing referent overlap (\\textit{building-other}/\\textit{location-GPE}, SCS\\,=\\,0.85) are most frequent. The ``other'' subtypes absorb diverse entities and confuse with more specific siblings.}\n\\label{tab:top10_ner}\n\\end{table}\n\n\\paragraph{Illustrative error instances.}\nTable~\\ref{tab:error_examples} shows three FewRel instances where the model predicted a semantically adjacent relation. All gold-predicted pairs have SCS\\,$>$\\,0.90.\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{p{5.8cm}llc}\n\\toprule\n\\textbf{Sentence (abridged)} & \\textbf{Gold} & \\textbf{Predicted} & \\textbf{SCS} \\\\\n\\midrule\nOver five EuroLeague games he played for \\textbf{Valencia}, he averaged 8 points \\ldots\\  [\\textbf{EuroLeague}, \\textbf{Valencia}] & participant & participant of & 0.97 \\\\\n\\addlinespace\n\\textbf{Pilões} is a municipality in the state of \\textbf{Rio Grande do Norte} in the Northeast region of Brazil. & contains admin.\\ terr.\\ entity & located in admin.\\ terr.\\ entity & 0.92 \\\\\n\\addlinespace\nIn May 1997 Davies was appointed \\ldots\\ to the \\textbf{Cabinet} as \\textbf{Secretary of State for Wales}. & part of & member of & 0.90 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Representative confusion instances from FewRel 80-relation RE (Qwen3-32B, count\\,=\\,80). Head and tail entities are bolded. In each case, the gold and predicted relations are semantically close (SCS\\,$>$\\,0.90): \\textit{participant} vs.\\ \\textit{participant of} reverses argument directionality; \\textit{contains} vs.\\ \\textit{located in} inverts the containment relation; \\textit{part of} vs.\\ \\textit{member of} conflates meronymy with membership. These confusions are consistent with the pairwise SCS--confusion correlation reported in \\S\\ref{sec:pairwise}.}\n\\label{tab:error_examples}\n\\end{table}\n\n\\end{document}\n",
    "structuredPatch": [
      {
        "oldStart": 43,
        "oldLines": 7,
        "newStart": 43,
        "newLines": 7,
        "lines": [
          " ",
          " \\item \\textbf{Task format dependency.} BCS batch-level prediction is demonstrated only under RE's forced-choice classification format. An unconstrained decoding ablation ($n = 25$) confirms this: removing the enum constraint eliminates the BCS--accuracy correlation ($\\rho = -0.14$, $p = 0.49$), establishing that the batch-level signal is specific to forced-choice RE. NER exact-match evaluation conflates boundary and type errors, and relaxed matching may yield different confusability effect sizes.",
          " ",
          "-\\item \\textbf{Causal mechanism.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway. A post-hoc schema label renaming experiment was inconclusive due to label unfamiliarity confounds.",
          "+\\item \\textbf{Causal mechanism.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway. A post-hoc renaming experiment (Appendix~\\ref{app:renaming}) confirms this concern: replacing high-SCS labels with semantically distinct paraphrases reduced pairwise embedding similarity but decreased accuracy by 3--9\\,pp, as label unfamiliarity introduced errors that outweighed any confusability reduction.",
          " ",
          " \\item \\textbf{Data contamination.} FewRel (2018) may appear in pretraining corpora, but train-origin relations show numerically lower accuracy than val-origin ($-8.8$\\,pp, $p = 0.06$, n.s.), opposite to the contamination hypothesis. The monotonic degradation curve cannot be explained by uniform contamination. DocRED (2019) provides a lower-contamination-risk replication with consistent BCS--accuracy slopes ($R^2 = 0.53$). Adding train-origin ratio as a covariate leaves the BCS partial effect unchanged ($p = 0.245$; Appendix~\\ref{app:split-origin}).",
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

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Edit · `toolu_01UyAsAWp143iD6AYuNtLHPZ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "old_string": "\\label{tab:error_examples}\n\\end{table}\n\n\\end{document}",
  "new_string": "\\label{tab:error_examples}\n\\end{table}\n\n\\section{Schema Label Renaming Experiment}\n\\label{app:renaming}\n\nTo test whether reducing pairwise SCS through label renaming improves accuracy, we conducted a controlled intervention on FewRel 80-relation RE (count 8, Qwen3-32B). We identified 14 high-SCS relation pairs (mean SCS = 0.87) and replaced one label in each pair with a semantically distinct paraphrase chosen to minimize embedding cosine similarity (all-MiniLM-L6-v2). Examples: \\textit{participant of} $\\to$ \\textit{event involvement} (SCS: 0.97 $\\to$ 0.72), \\textit{follows} $\\to$ \\textit{prior entry} (0.90 $\\to$ 0.69), \\textit{part of} $\\to$ \\textit{integral segment of} (0.90 $\\to$ 0.64). The renaming reduced mean pairwise SCS from 0.87 to 0.67 ($\\Delta = -0.20$). We ran the same 50 BCS-controlled batches (25 low-BCS, 25 high-BCS; 96 samples each) under both original (control) and renamed (treatment) label sets.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n& \\textbf{Control} & \\textbf{Treatment} & \\textbf{$\\Delta$\\,(pp)} \\\\\n\\midrule\nLow-BCS ($n=25$)  & 90.1 & 87.1 & $-$3.0 \\\\\nHigh-BCS ($n=25$) & 69.3 & 60.5 & $-$8.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Accuracy (\\%) under original vs.\\ renamed labels on FewRel count-8 batches. Renaming reduced embedding similarity but decreased accuracy in both groups, with a larger drop on high-BCS batches (Cohen's $d = -2.92$) than low-BCS ($d = -1.09$). Interaction: $\\Delta_{\\text{high}} - \\Delta_{\\text{low}} = -5.9$\\,pp ($t = -7.23$, $p < 0.001$).}\n\\label{tab:renaming}\n\\end{table}\n\nRenaming hurt accuracy uniformly: both groups showed significant declines (paired $t$-test, both $p < 0.001$). The number of renamed types per batch correlated negatively with accuracy change ($r = -0.625$, $p < 0.001$). A solo sanity check confirmed that 11 of 12 renamed labels were individually recognizable (accuracy $\\geq$ original $-5$\\,pp). The results indicate that replacing familiar Wikidata labels with unfamiliar paraphrases disrupts the model's type semantics; this label unfamiliarity effect outweighs any benefit from reduced confusability.\n\n\\end{document}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c6b2a1-3665-4eeb-aad0-d119dd87428b",
  "uuid": "58821e50-40d3-4b1f-940f-6867c4d2f3b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VrMCeKJgWQjcCvEvtQJNMQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4827,
      "cache_read_input_tokens": 35463,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4827
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

_source line 38 · 2026-05-18T21:36:22.864Z_

<details><summary>↩ Tool result · `toolu_01UyAsAWp143iD6AYuNtLHPZ`</summary>

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
  "session_id": "e8c6b2a1-3665-4eeb-aad0-d119dd87428b",
  "uuid": "41bd5f8c-30e8-48aa-9a68-264deaf7e5da",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "oldString": "\\label{tab:error_examples}\n\\end{table}\n\n\\end{document}",
    "newString": "\\label{tab:error_examples}\n\\end{table}\n\n\\section{Schema Label Renaming Experiment}\n\\label{app:renaming}\n\nTo test whether reducing pairwise SCS through label renaming improves accuracy, we conducted a controlled intervention on FewRel 80-relation RE (count 8, Qwen3-32B). We identified 14 high-SCS relation pairs (mean SCS = 0.87) and replaced one label in each pair with a semantically distinct paraphrase chosen to minimize embedding cosine similarity (all-MiniLM-L6-v2). Examples: \\textit{participant of} $\\to$ \\textit{event involvement} (SCS: 0.97 $\\to$ 0.72), \\textit{follows} $\\to$ \\textit{prior entry} (0.90 $\\to$ 0.69), \\textit{part of} $\\to$ \\textit{integral segment of} (0.90 $\\to$ 0.64). The renaming reduced mean pairwise SCS from 0.87 to 0.67 ($\\Delta = -0.20$). We ran the same 50 BCS-controlled batches (25 low-BCS, 25 high-BCS; 96 samples each) under both original (control) and renamed (treatment) label sets.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n& \\textbf{Control} & \\textbf{Treatment} & \\textbf{$\\Delta$\\,(pp)} \\\\\n\\midrule\nLow-BCS ($n=25$)  & 90.1 & 87.1 & $-$3.0 \\\\\nHigh-BCS ($n=25$) & 69.3 & 60.5 & $-$8.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Accuracy (\\%) under original vs.\\ renamed labels on FewRel count-8 batches. Renaming reduced embedding similarity but decreased accuracy in both groups, with a larger drop on high-BCS batches (Cohen's $d = -2.92$) than low-BCS ($d = -1.09$). Interaction: $\\Delta_{\\text{high}} - \\Delta_{\\text{low}} = -5.9$\\,pp ($t = -7.23$, $p < 0.001$).}\n\\label{tab:renaming}\n\\end{table}\n\nRenaming hurt accuracy uniformly: both groups showed significant declines (paired $t$-test, both $p < 0.001$). The number of renamed types per batch correlated negatively with accuracy change ($r = -0.625$, $p < 0.001$). A solo sanity check confirmed that 11 of 12 renamed labels were individually recognizable (accuracy $\\geq$ original $-5$\\,pp). The results indicate that replacing familiar Wikidata labels with unfamiliar paraphrases disrupts the model's type semantics; this label unfamiliarity effect outweighs any benefit from reduced confusability.\n\n\\end{document}",
    "originalFile": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{enumitem}\n\\usepackage[normalem]{ulem}\n\\usepackage{listings}\n\n\\title{How Does Schema Complexity Predict Performance\\\\in Training-Free LLM Information Extraction?}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{experimental_setup}\n\n\\input{results}\n\n\\input{sdgd_negative}\n\n\\input{discussion}\n\n\\section*{Limitations}\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B, 70B-Instruct (FP8), and Gemini 2.5 Flash (API). Dimension~1 has been validated across all four models including a proprietary one; Dimension~2 has been verified only on open-weight models and was not robustly detectable on NER at 8B scale, likely due to floor effects.\n\n\\item \\textbf{Effect size and statistical design.} Pairwise SCS explains 1.3--1.7\\% of type confusion variance; entity frequency, prompt position, and mention ambiguity likely account for the remainder. The count $\\times$ BCS interaction is bounded under the linear specification (TOST $p = 0.003$ at $\\pm 3$\\,pp) but inconclusive on the logit scale ($p = 0.209$; Appendix~\\ref{sec:appendix_factorial}). BCS-controlled experiments use a single seed with greedy decoding; the residual SD of 0.88\\,pp (Appendix~\\ref{app:variance-decomposition}) supports robustness but precise magnitudes may vary.\n\n\\item \\textbf{Task format dependency.} BCS batch-level prediction is demonstrated only under RE's forced-choice classification format. An unconstrained decoding ablation ($n = 25$) confirms this: removing the enum constraint eliminates the BCS--accuracy correlation ($\\rho = -0.14$, $p = 0.49$), establishing that the batch-level signal is specific to forced-choice RE. NER exact-match evaluation conflates boundary and type errors, and relaxed matching may yield different confusability effect sizes.\n\n\\item \\textbf{Causal mechanism.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway. A post-hoc renaming experiment (Appendix~\\ref{app:renaming}) confirms this concern: replacing high-SCS labels with semantically distinct paraphrases reduced pairwise embedding similarity but decreased accuracy by 3--9\\,pp, as label unfamiliarity introduced errors that outweighed any confusability reduction.\n\n\\item \\textbf{Data contamination.} FewRel (2018) may appear in pretraining corpora, but train-origin relations show numerically lower accuracy than val-origin ($-8.8$\\,pp, $p = 0.06$, n.s.), opposite to the contamination hypothesis. The monotonic degradation curve cannot be explained by uniform contamination. DocRED (2019) provides a lower-contamination-risk replication with consistent BCS--accuracy slopes ($R^2 = 0.53$). Adding train-origin ratio as a covariate leaves the BCS partial effect unchanged ($p = 0.245$; Appendix~\\ref{app:split-origin}).\n\\end{enumerate}\n\n\\paragraph{Multiple comparisons.} Cross-dataset comparisons (FewRel, DocRED, Few-NERD, MAVEN) serve as independent replications of the same hypothesis and do not require family-wise correction \\citep{rothman-1990}. Within-dataset secondary analyses (e.g., quartile comparisons, slope sensitivity checks) involve multiple looks at the same data; we report individual $p$-values and note that core claims rest on effects reaching $p < 0.001$ \\citep{dror-2018-significance,card-2020-power}.\n\n\\input{checklist}\n\n\\bibliography{references}\n\n\\appendix\n\n\\section{Additional Figures}\n\\label{sec:appendix_figures}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Llama-3.1-8B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1 & 0.702 & 0.640 \\\\\n64 & 0.273 & 0.304 \\\\\n\\midrule\nDecline & $-$43\\,pp & $-$34\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\\S\\ref{sec:model}) for fair cross-model comparison; the count-curve results in \\S\\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\\ 0.64 at count${}\\,=\\,1$) due to over-prediction under v1.}\n\\label{tab:cross_model}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{crrrrrr}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Llama-3.1-8B}} & \\multicolumn{3}{c}{\\textbf{Qwen3-32B}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Count} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} \\\\\n\\midrule\n8 & 78.1\\% & 51.0\\% & $-$27.1 & 82.3\\% & 51.0\\% & $-$31.2 \\\\\n16 & 75.5\\% & 51.6\\% & $-$23.9 & 82.8\\% & 51.6\\% & $-$31.2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\\approx$51\\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\\Delta$, in pp) is 77--87\\% as large on Llama-3.1-8B as on Qwen3-32B.}\n\\label{tab:cross_model_bcs}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrrrr}\n\\toprule\n & & \\multicolumn{5}{c}{\\textbf{BCS Bin}} & & \\\\\n\\cmidrule(lr){3-7}\n\\textbf{Task} & \\textbf{Error} & \\textbf{Solo} & \\textbf{Low} & \\textbf{Mid} & \\textbf{High} & \\textbf{V.High} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nNER & IntraSub & 0\\% & 1.6\\% & 10.6\\% & 49.4\\% & --- & 1.000 & ${<}0.001$ \\\\\nRE  & IntraSub & 0\\% & 4.2\\% & 13.0\\% & 20.3\\% & 32.3\\% & 0.954 & ${<}\\,0.001$ \\\\\n\\midrule\nNER & Missed & --- & 42.8\\% & 64.8\\% & 49.9\\% & --- & --- & --- \\\\\nRE  & Missed & --- & 10.4\\% & 11.3\\% & 13.1\\% & 15.7\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin, with Spearman $\\rho$ computed over $n=154$ individual batches (RE) and $n=148$ batches (NER). NER has 4 BCS bins; RE has 5.}\n\\label{tab:error_taxonomy}\n\\end{table}\n\n\\section{SDGD Full Protocol and Results}\n\\label{sec:appendix_sdgd}\n\nWe construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent (i.e., highly confusable) types share a color. Each color class forms one extraction batch, and predictions are merged via set union. We compare four modes: (i)~\\textbf{single\\_pass}, the undecomposed baseline; (ii)~\\textbf{sdgd\\_zero}, SCS-guided partitioning; (iii)~\\textbf{random\\_batch}, random partitioning with matched batch sizes; and (iv)~\\textbf{per\\_type}, the extreme case where each type is extracted in isolation.\n\nSingle-pass extraction achieves F1\\,=\\,0.445 (P\\,=\\,0.563, R\\,=\\,0.368). SDGD obtains F1\\,=\\,0.251 (P\\,=\\,0.210, R\\,=\\,0.314), a 44\\% relative drop. Random batching reaches F1\\,=\\,0.320 (P\\,=\\,0.249, R\\,=\\,0.446), and per-type extraction yields F1\\,=\\,0.292 (P\\,=\\,0.194, R\\,=\\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\\ref{tab:sdgd_results}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrccc}\n\\toprule\n\\textbf{Mode} & \\textbf{\\# Batches} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{F1} \\\\\n\\midrule\nsingle\\_pass & 1 & 0.563 & 0.368 & 0.445 \\\\\n\\midrule\nsdgd\\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\\\\nrandom\\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\\\\nper\\_type & 66 & 0.194 & 0.586 & 0.292 \\\\\n\\midrule\nsdgd\\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\\\\nrandom\\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \\texttt{min\\_batch\\_size=8} (reducing 8$\\to$4 batches for sdgd\\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt.}\n\\label{tab:sdgd_results}\n\\end{table}\n\nDecomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions. Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions and inflates false positives.\n\nOur v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\\_zero: 0.210$\\to$0.324; random\\_batch: 0.249$\\to$0.331), but at the cost of disproportionate recall loss (0.314$\\to$0.191; 0.446$\\to$0.276), and both modes produce lower F1 (sdgd\\_zero: 0.251$\\to$0.241; random\\_batch: 0.320$\\to$0.301).\n\n\\subsection{Practical Routing Strategies on RE}\n\\label{sec:appendix_routing}\n\nWe evaluate five non-oracle routing strategies on FewRel 80-relation RE using graph-coloring sub-schema decomposition (same grouping as Table~\\ref{tab:batch_composition}). Each strategy selects a single sub-schema for each test instance and returns that sub-schema's prediction.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{@{}lrr@{}}\n\\toprule\n\\textbf{Strategy} & \\textbf{Accuracy} & \\textbf{$\\Delta$ vs.\\ Single-Pass} \\\\\n\\midrule\nOracle (gold label) & 72.4\\% & +22.0\\,pp \\\\\n\\midrule\nMax-conf (positive only) & 36.5\\% & $-$14.0\\,pp \\\\\nNone-aware & 36.5\\% & $-$14.0\\,pp \\\\\nMargin (positive only) & 35.9\\% & $-$14.5\\,pp \\\\\nMax-conf (all) & 27.7\\% & $-$22.7\\,pp \\\\\nRandom & 14.7\\% & $-$35.7\\,pp \\\\\n\\midrule\nSingle-pass (no decomposition) & 50.4\\% & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Routing strategy comparison on FewRel 80-relation RE with graph-coloring sub-schema decomposition. Oracle requires gold labels. All practical (non-oracle) strategies perform below the single-pass baseline. The failure stems from constrained decoding (enum constraint), which forces confident predictions in every sub-schema: 73.4\\% of instances receive positive predictions from 3--5 sub-schemas simultaneously, with per-sub-schema none-rates of only 20--40\\%.}\n\\label{tab:routing_strategies}\n\\end{table}\n\n\\section{Factorial Analysis and Separability Test}\n\\label{sec:appendix_factorial}\n\nTo formally test whether count and confusability effects are additive, we fit a multiple regression (accuracy $\\sim$ $\\log_2$\\,count $+$ BCS $+$ count$\\times$BCS) across 69 batches from FewRel spanning five count levels ($k \\in \\{4, 8, 16, 32, 40\\}$). Both main effects are significant (count: $p = 0.008$; BCS: $p = 0.0002$; $R^2 = 0.52$), but the interaction term is negligible (0.47\\,pp). A TOST equivalence test with a $\\pm 3$\\,pp margin confirms that the interaction is bounded well below practical significance ($p_{\\text{TOST}} = 0.003$); this supports bounded interaction between count and confusability effects.\n\nA $2 \\times 2$ factorial sensitivity check on FewRel (count $\\in \\{8, 16\\}$, BCS low/high; $n = 54$) was inconclusive ($p_{\\text{TOST}} = 0.56$) due to limited power; this does not contradict the primary finding but limits generalization beyond the regression framework. The Few-NERD factorial (\\S\\ref{sec:multi_channel}) similarly did not reach significance ($p = 0.50$). The regression approach provides the stronger test by leveraging the full count range.\n\n\\paragraph{Equivalence margin justification.}\nWe set the $\\pm 3$\\,pp margin based on three converging anchors. \\emph{Empirical}: typical random-batch confusability variation produces 2--5\\,pp accuracy differences (batch SD $\\approx 4.6$\\,pp at count 32). \\emph{Practical}: a ${<}3$\\,pp accuracy difference falls below deployment-relevant thresholds. \\emph{Statistical}: 3\\,pp $\\approx 0.5 \\times$ batch SD, equivalent to Cohen's $d \\approx 0.5$ (medium effect threshold; \\citealt{lakens-2017-equivalence}). A 3\\,pp interaction atop the 2.2\\,pp confusability main effect would represent ${>}130\\%$ amplification, fundamentally changing whether confusability warrants mitigation. At $\\pm 2$\\,pp (marginally equivalent, $p = 0.047$), interaction remains bounded below the main effect itself.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{crrl}\n\\toprule\n\\textbf{Margin (pp)} & \\textbf{$t_{\\text{upper}}$} & \\textbf{$p_{\\text{TOST}}$} & \\textbf{Conclusion} \\\\\n\\midrule\n$\\pm 1$ & $-0.59$ & $0.278$ & Inconclusive \\\\\n$\\pm 2$ & $-1.70$ & $0.047$ & Equivalent \\\\\n$\\pm 3$ & $-2.81$ & $0.003$ & Equivalent \\\\\n$\\pm 5$ & $-5.02$ & ${<}\\,0.001$ & Equivalent \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{TOST sensitivity analysis across equivalence margins. The interaction effect (0.47\\,pp, 90\\% CI [$-$1.0, 2.0]\\,pp) is bounded below 2\\,pp at marginal significance ($p = 0.047$); the $\\pm 3$\\,pp choice does not drive the equivalence conclusion. At $\\pm 1$\\,pp, equivalence is inconclusive ($p = 0.278$), meaning interaction could reach approximately half the main effect magnitude.}\n\\label{tab:tost_sensitivity}\n\\end{table}\n\n\\paragraph{Logit-scale sensitivity.}\nBecause accuracy near 50\\% compresses interaction effects on the linear scale, we refit the regression on logit-transformed accuracy. The logit-scale interaction (0.111 logit units, $p = 0.047$, 90\\% CI [0.019, 0.203]) is marginally significant, and TOST at the equivalent $\\pm 3$\\,pp margin ($\\pm 0.156$ logit at median accuracy) is inconclusive ($p_{\\text{TOST}} = 0.209$). However, back-transforming the interaction to the probability scale at the observed floor ($p = 0.51$) yields 2.78\\,pp, still within the $\\pm 3$\\,pp margin; at the median baseline ($p = 0.65$), the back-transformed effect is 2.53\\,pp. The logit TOST is inconclusive due to limited power ($n = 69$, wide CI) rather than a large effect size: the point estimate remains below the equivalence bound at all observed baselines. We retain the linear-scale TOST as the primary test and report this logit analysis as a sensitivity check.\n\n\\section{Within-Pool CI Details}\n\\label{sec:appendix_within_pool}\n\nThe quartile $\\Delta$ for 80-pool 16-relation subsets ($-$3.92\\,pp, 95\\% CI [$-$8.17, $+$0.38]) crosses zero, reflecting the compressed BCS range within that pool (0.46--0.68 vs.\\ 0.48--0.71 for the independent pool). Within this narrow band, the quartile contrast lacks statistical power to detect the effect that the regression identifies. The full 80-relation condition ($n = 25$) is underpowered for both the slope (CI: [$-$1.303, $+$1.695]) and quartile analyses; we include it in Table~\\ref{tab:within_pool} for completeness but do not draw inferential conclusions from it.\n\n\\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}\n\\label{sec:appendix_residualized_bcs}\n\nSection~\\ref{sec:centrality_confound} identifies a centrality confound in MAVEN's per-type BCS--F1 correlation: both embeddings show a \\emph{positive} raw correlation, opposite to the expected direction. Here we formalize this analysis by identifying specific confounders for each embedding and testing whether the BCS--F1 relationship survives partial correlation controlling for these confounders.\n\n\\paragraph{Confound identification.}\nFor each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:\n\\begin{itemize}[itemsep=2pt,leftmargin=*]\n\\item \\textbf{MiniLM}: BCS correlates with log type frequency ($r = 0.201$). Frequent types have more training signal and are extracted more reliably, which produces the positive BCS--F1 association.\n\\item \\textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors, central, well-represented types that the model extracts well.\n\\end{itemize}\n\n\\paragraph{Partial correlation results.}\nTable~\\ref{tab:residualized_bcs} reports raw Spearman $\\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Embedding} & \\textbf{Control} & \\textbf{Raw $\\rho$} & \\textbf{Raw $p$} & \\textbf{Partial $r$} & \\textbf{Partial $p$} \\\\\n\\midrule\nMiniLM & --- & $+$0.208 & $0.011$ & --- & --- \\\\\nMiniLM & log freq & --- & --- & $+$0.133 & $0.11$ \\\\\nMiniLM & log freq $+$ degree & --- & --- & --- & $0.23$ \\\\\n\\midrule\nQwen3 & --- & $+$0.184 & $0.025$ & --- & --- \\\\\nQwen3 & degree centrality & --- & --- & $+$0.063 & $0.44$ \\\\\nQwen3 & log freq $+$ degree & --- & --- & --- & $0.44$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{MAVEN per-type BCS--F1 correlation before and after controlling for centrality confounders. Raw correlations are Spearman $\\rho$; partial correlations are Pearson $r$ from residualized regression. Degree centrality is computed on the SCS graph at threshold 0.7. All values from experiment \\texttt{exp\\_maven\\_residualized\\_bcs}.}\n\\label{tab:residualized_bcs}\n\\end{table}\n\n\\paragraph{Interpretation.}\nThe two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality (the count of strong semantic neighbors) becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.\n\nUnder joint control, both embeddings yield $p > 0.2$; the raw positive BCS--F1 correlation on MAVEN is thus fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 0.001$; Table~\\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.\n\n\\section{Batch Composition Results}\n\\label{sec:appendix_batch_composition}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Accuracy} & \\textbf{Mean BCS} \\\\\n\\midrule\nSingle-pass (80 types) & 0.504 & 0.557 \\\\\nRandom batching (15 seeds)$^\\dagger$ & 0.788\\,$\\pm$\\,0.018 & 0.559 \\\\\nConfus.-aware (graph coloring) & \\textbf{0.802} & 0.552 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Batch composition on FewRel 80-relation RE with oracle routing. $^\\dagger$Mean $\\pm$ SD across 15 random seeds.}\n\\label{tab:batch_composition}\n\\end{table}\n\nSee the accompanying discussion in \\S\\ref{sec:sdgd}.\n\n\\input{prompt_appendix}\n\n\\section{Prompt Version Sensitivity Analysis}\n\\label{sec:appendix_prompt_sensitivity}\n\nWe assess whether the confusability effects reported in \\S\\ref{sec:bcs_controlled}--\\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\paragraph{RE (FewRel).}\nUnder the v1 prompt, the extreme-batch BCS gap (Table~\\ref{tab:bcs_controlled}) is substantial. Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; 95\\% CI: [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\\,pp (CI: [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal, a cautionary note for small-sample prompt sensitivity studies.\n\n\\paragraph{NER (Few-NERD).}\nThe batch-level BCS--F1 correlation is null under both prompt versions. Pooling across three seeds and all count levels ($n = 450$), the correlation is $r = 0.004$ ($p = 0.94$). An earlier small-sample analysis ($n = 27$, single seed) had reported positive correlations ($r = +0.50$/$+0.58$), but these were driven by an accidental BCS--type-frequency confound: those 27 batches exhibited $r(\\text{BCS}, \\text{freq}) = 0.53$, creating a spurious path through frequency to F1. After controlling for type frequency, the partial correlation is non-significant in both the small ($r = 0.28$, $p = 0.16$) and large ($r = -0.12$, $p = 0.29$) samples. The pairwise SCS--confusion analysis (\\S\\ref{sec:pairwise}), which is immune to this batch-level aggregation artifact, remains the primary evidence for the NER confusability dimension.\n\n\\paragraph{Interpretation.}\nThe $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\\,pp) but remains highly significant ($p < 0.001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\\% vs.\\ 82.3\\%), but type confusion under high confusability persists (59.7\\% vs.\\ 51.0\\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary source. The underlying confusability signal (pairwise SCS--confusion correlation and the directional BCS--accuracy relationship) persists across both prompt versions.\n\n\\subsection{Cross-Prompt-Variant BCS Correlation}\n\\label{sec:appendix_prompt_variants}\n\nTo verify that the BCS--accuracy relationship is not an artifact of a specific prompt template, we evaluate four structurally distinct prompt variants on FewRel 80-relation RE at two count levels (8 and 32), with 10 random batches per condition.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{llrrrr}\n\\toprule\n\\textbf{Variant} & \\textbf{Count} & \\textbf{Mean Acc} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nV2 (definition-first) & 8 & 0.769 & $-$0.333 & 0.348 \\\\\nV2 (definition-first) & 32 & 0.564 & $-$0.648 & 0.043 \\\\\nInstruction-rewrite & 8 & 0.847 & $-$0.223 & 0.536 \\\\\nInstruction-rewrite & 32 & 0.662 & $-$0.469 & 0.171 \\\\\nChain-of-thought & 8 & 0.749 & $+$0.254 & 0.478 \\\\\nChain-of-thought & 32 & 0.617 & $-$0.566 & 0.088 \\\\\nMinimal & 8 & 0.852 & $-$0.170 & 0.638 \\\\\nMinimal & 32 & 0.615 & $-$0.771 & 0.009 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS--accuracy Pearson correlation across four prompt variants. At count 32, all four variants show negative BCS--accuracy correlations ($r \\leq -0.47$), with two reaching $p < 0.05$. At count 8, the narrower BCS range reduces statistical power.}\n\\label{tab:prompt_variants}\n\\end{table}\n\nAt count 32, all four variants produce negative BCS--accuracy correlations ($r$ ranges from $-$0.47 to $-$0.77), with V2 ($p = 0.043$) and Minimal ($p = 0.009$) reaching significance and Chain-of-thought approaching it ($p = 0.088$). At count 8, correlations are weaker and nonsignificant across all variants, consistent with the narrower BCS range at lower schema complexity reducing the detectable effect size. Rather than applying Bonferroni correction, which assumes independent hypotheses inappropriate for correlated prompt variants testing the same underlying signal, we note directional consistency: 7 of 8 conditions show negative BCS--accuracy slopes, consistent with the primary finding \\citep{rothman-1990}. These results confirm that the confusability effect arises from schema composition, not prompt-specific phrasing.\n\n\\section{BCS Aggregation Sensitivity}\n\\label{sec:appendix_bcs_sensitivity}\n\nWe define Batch Confusability Score (BCS) as the \\emph{mean} pairwise SCS across all type pairs in a batch (\\S\\ref{sec:bcs_controlled}). An alternative definition takes the \\emph{maximum} pairwise SCS within each batch to capture the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Aggregation} & \\textbf{Condition} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nMEAN (primary) & 16-rel & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ \\\\\nMEAN & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\midrule\nMAX & 16-rel & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}\\,0.001$ \\\\\nMAX & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS--accuracy regression under mean vs.\\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p \\approx 0.60$; MAX $p \\approx 0.44$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}\n\\label{tab:bcs_aggregation}\n\\end{table}\n\nMAX aggregation yields stronger correlations ($r = -0.637$ vs.\\ $-0.467$ for 16-rel), consistent with the hypothesis that the single most confusable pair in a batch predicts substitution errors. Both definitions produce significant negative slopes across all conditions, and the permutation tests confirm no significant difference between independent and sampled pools under either definition. We adopt MEAN as the primary definition because it better represents average pairwise difficulty across all schema combinations, while MAX may overweight a single outlier pair. The choice does not affect any paper conclusion.\n\n\\section{BCS-Controlled Detailed Results}\n\\label{app:bcs-controlled-table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\n\\paragraph{Adjusted $R^2$ and confidence intervals.}\nDocRED regressions (\\S\\ref{sec:bcs_controlled}) use OLS on $n = 35$ batches (5 high-BCS + 5 low-BCS + 25 random) with one predictor. At count 16, adjusted $R^2 = 0.511$ (unadjusted: 0.525; 95\\% CI via Fisher $z$-transformation: [0.27, 0.73]); at count 32, adjusted $R^2 = 0.426$ (unadjusted: 0.443; CI: [0.18, 0.67]). The small shrinkage ($\\Delta R^2 \\leq 0.02$) indicates the unadjusted values are not inflated by the predictor-to-sample ratio.\n\n\\section{Within-Pool Analysis Methodology}\n\\label{app:within-pool-method}\n\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ & $-$5.31 & [$-$7.44, $-$3.19] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & $0.027$ & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$)$^\\dagger$ & $+$0.221 & [$-$1.303, $+$1.695] & $+$0.064 & $0.76$ & $-$1.04 & [$-$10.12, $+$8.04] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p \\approx 0.60$ (5{,}000 permutations)} \\\\\n\\multicolumn{7}{l}{\\footnotesize $^\\dagger$BCS range (IQR\\,=\\,0.033) insufficient for regression; slope not interpretable.} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\end{table}\n\nThe within-pool slope ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.509; permutation $p \\approx 0.60$). The smaller quartile gap ($-$3.92\\,pp vs.\\ $-$5.31\\,pp) reflects the narrower BCS range within the 80-relation pool (Appendix~\\ref{sec:appendix_within_pool}).\n\nIn the full 80-relation condition, natural BCS variation is insufficient (IQR${}=0.033$) to yield a detectable effect ($n=25$, slope${}=+0.221$, $p \\approx 0.76$). This does not invalidate the confusability effect; the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied, but establishes that natural schema sampling at this scale does not produce sufficient BCS contrast for detection.\n\n\\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}\n\\label{app:scs-ablation}\n\nTable~\\ref{tab:scs-ablation} compares predictive accuracy of name-only SCS against name+definition SCS across three datasets.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lcccc}\n\\toprule\nDataset & SCS$_\\text{name}$ $r$ & SCS$_\\text{def}$ $r$ & $\\Delta r$ & Matrix corr. \\\\\n\\midrule\nFew-NERD & 0.172 & 0.149 & $-$0.023 & 0.894 \\\\\nMAVEN & 0.129 & 0.164 & +0.035 & 0.656 \\\\\nFewRel & 0.178 & 0.193 & +0.015 & 0.848 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pearson correlation between SCS and empirical confusion rate. ``Def'' concatenates type name with definition before embedding. All correlations significant ($p < 0.001$). The inconsistent direction of $\\Delta r$ indicates that definitions provide no systematic benefit.}\n\\label{tab:scs-ablation}\n\\end{table}\n\nFew-NERD is the only dataset whose prompts include type definitions; for MAVEN and FewRel, prompts use type names alone, so name-only SCS directly matches model input. The high matrix correlation (0.66--0.89) confirms that type names capture the dominant semantic structure.\n\n\\paragraph{Held-out validation.}\n\\label{app:scs-heldout-validation}\nFrom the 80-type confusion matrix, we extract the $\\binom{16}{2} = 120$ pairs among the 16 validation-origin types (fully disjoint from the 64 training-pool types). The SCS--confusion Spearman correlation remains positive and significant ($\\rho = 0.216$, $p = 0.018$), nearly identical to the full 80-type pool ($\\rho = 0.218$, $p < 10^{-34}$, $n = 3{,}160$ pairs), ruling out training-set contamination as the driver of the observed relationship.\n\n\\section{Pair-to-Batch Aggregation Simulation}\n\\label{app:aggregation-sim}\n\nThe following simulation provides an illustrative explanatory model for how pair-level effects aggregate to batch-level variance. It is not the evidence base for our claims; the observed batch-level $R^2 = 0.218$ (\\S\\ref{sec:practical_magnitude}) is a direct empirical measurement independent of this simulation.\n\n\\paragraph{Setup.} We examine whether the pair-level $R^2 \\approx 7\\%$ (computed over non-zero confusion pairs) can aggregate to the observed batch-level $R^2 \\approx 22\\%$ via a Monte Carlo simulation. From the FewRel 16-relation experiment, we estimate the inter-pair SCS correlation for pairs sharing a common type ($\\rho_\\text{SCS} = 0.35$). For batches of $k=8$ types ($\\binom{8}{2}=28$ pairs), we simulate 10{,}000 iterations: (1) generate 28 correlated pair-level effects with individual $R^2 = 0.074$; (2) average to obtain batch-level signals; (3) compute batch-level $R^2$.\n\n\\paragraph{Results.} Simulated batch $R^2 = 0.219$ [95\\% CI: 0.092--0.361], matching the observed value of 0.218. The effective amplification factor is $\\sim$3$\\times$, explained by signal correlation within batches preserving variance while independent noise averages out (effective degrees of freedom $\\approx 3.4$, not 28).\n\n\\paragraph{Unconditional baseline.}\nWhen the simulation uses the unconditional pairwise $r^2 = 0.013$ (computed over all type pairs including zero-confusion pairs; Table~\\ref{tab:pairwise}), the simulated batch-level $R^2$ drops to $0.044$ [95\\% CI: 0.001--0.151], well below the observed $R^2 = 0.218$. The analytical formula confirms: $\\text{SNR} \\times \\text{EF} / (\\text{SNR} \\times \\text{EF} + 1) = 0.042$ with the same effective factor $\\text{EF} = 3.35$. This ${\\sim}5\\times$ gap reflects the dilution from zero-confusion pairs: approximately 89\\% of type pairs never exhibit mutual confusion, contributing only noise to the unconditional correlation. The conditional model ($R^2 = 0.074 \\to 0.219$) matches the observed value because it isolates the minority of semantically proximate pairs that actually compete during type resolution; BCS predicts batch accuracy through the density of \\emph{active} confusable pairs, not uniform contributions from all pairs.\n\n\\paragraph{Sensitivity to $\\rho$.}\nThe inter-pair SCS correlation $\\rho = 0.35$ is estimated from pairs sharing a common type. At $\\rho = 0.20$ (halved correlation), a parallel simulation yields batch $R^2 \\approx 0.22$, still matching the observed value; at $\\rho = 0.50$, the correlation structure approaches the positive-definiteness boundary; $\\rho = 0.35$ thus sits in a stable regime. The simulation is illustrative; the observed batch $R^2 = 0.218$ is the primary evidence.\n\n\\section{BCS Independence from Type Composition}\n\\label{app:bcs-composition}\n\nFewRel's balanced design (700 instances per type) makes type frequency invariant across batches, ruling out frequency-driven confounding. To test whether BCS captures information beyond type composition effects, we decompose the explained variance in a joint model (accuracy $\\sim$ BCS $+$ mean type difficulty), where type difficulty is the per-type solo-baseline accuracy averaged across batch members. On 100 random 8-type batches from the 16-relation pool, the joint model explains $R^2 = 0.704$. Variance decomposition yields: BCS unique $R^2 = 0.259$ (36.8\\% of explained variance), composition unique $R^2 = 0.298$ (42.3\\%), and shared $R^2 = 0.147$ (20.9\\%). The near-orthogonality of predictors (VIF${}\\,=\\,1.06$, $r(\\text{BCS}, \\text{difficulty}) = -0.21$) confirms that BCS captures confusability-specific signal rather than a proxy for type difficulty.\n\n\\section{SCS vs.\\ Simple Baselines}\n\\label{app:scs-baselines}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Metric} & \\textbf{Spearman $\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nFewRel & SCS (embedding) & \\textbf{0.218} & $2.2 \\times 10^{-35}$ \\\\\n(3{,}160 pairs) & Same-parent (WordNet) & 0.097 & $5.4 \\times 10^{-8}$ \\\\\n& WordNet Wu-Palmer & 0.073 & $4.3 \\times 10^{-5}$ \\\\\n& Levenshtein & 0.016 & 0.363 (n.s.) \\\\\n\\midrule\nFew-NERD & SCS (embedding) & \\textbf{0.166} & $1.5 \\times 10^{-13}$ \\\\\n(1{,}953 pairs) & Levenshtein & 0.152 & $1.4 \\times 10^{-11}$ \\\\\n& Same-parent (prefix) & 0.146 & $7.8 \\times 10^{-11}$ \\\\\n& WordNet Wu-Palmer & 0.054 & 0.070 (n.s.)$^\\dagger$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise confusion prediction: SCS vs.\\ simple baselines. Spearman $\\rho$ between each metric and the empirical confusion rate. SCS outperforms all baselines on FewRel; the margin is smaller on Few-NERD, where hierarchical naming conventions provide partial signal to string-based metrics. $^\\dagger$42\\% of pairs lack WordNet coverage.}\n\\label{tab:scs_baselines}\n\\end{table}\n\n\\section{Split-Origin Covariate Analysis}\n\\label{app:split-origin}\n\nFewRel combines 64 train-split and 16 val-split relation types into a single 80-type pool.  Train-origin types show numerically lower accuracy ($-8.8$\\,pp, $p = 0.06$; see Limitations), raising the question of whether differential pre-training exposure confounds the BCS--accuracy relationship.  We test this by adding a per-batch \\emph{train-origin ratio} (fraction of relation types drawn from the train split) as a covariate in the BCS--accuracy regression.\n\n\\paragraph{Method.}  Across 213 multi-type batches ($k \\geq 2$) from the batch-composition experiment (\\S\\ref{sec:sdgd}) and the factorial design (\\S\\ref{sec:bcs_controlled}), we compute $\\texttt{train\\_origin\\_ratio} = n_{\\text{train}} / k$ for each batch.  The ratio ranges from 0.40 to 1.00 (mean 0.80, consistent with the 64/80 base rate).  We fit:\n{\\small\\begin{equation*}\n\\text{acc} = \\beta_0 + \\beta_{\\text{BCS}} \\!\\cdot\\! \\text{BCS} + \\beta_{\\text{orig}} \\!\\cdot\\! \\text{train\\_origin\\_ratio} + \\varepsilon\n\\end{equation*}}\n\n\\paragraph{Results.}  The BCS partial effect is unchanged after controlling for split-origin: $\\beta_{\\text{BCS}} = -0.416$, $p < 10^{-16}$ (vs.\\ $\\beta = -0.412$, $p < 10^{-16}$ without the covariate).  Train-origin ratio is not independently significant ($\\beta_{\\text{origin}} = -0.057$, $p = 0.245$), and $\\Delta R^2 = 0.005$.  The BCS--accuracy relationship is therefore not confounded by differential pre-training exposure at the batch level.\n\nPairwise SCS distributions do not differ significantly between train-origin (64 types, mean\\,=\\,0.880) and val-origin (16 types, mean\\,=\\,0.874) subsets (Mann-Whitney $p = 0.754$, Cohen's $d = 0.081$); the train/val split does not introduce systematic confusability bias.\n\n\\section{Cross-Seed Variance Decomposition}\n\\label{app:variance-decomposition}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{rrrr}\n\\toprule\n\\textbf{Count} & \\textbf{Batch SD} & \\textbf{Seed SD} & \\textbf{Ratio} \\\\\n\\midrule\n4 & 0.0889 & 0.0122 & 53.5 \\\\\n8 & 0.0820 & 0.0098 & 70.0 \\\\\n16 & 0.0626 & 0.0270 & 5.4 \\\\\n32 & 0.0462 & 0.0091 & 26.0 \\\\\n40 & 0.0421 & 0.0019 & 474.4 \\\\\n64 & 0.0245 & 0.0022 & 119.8 \\\\\n80 & 0.0001 & 0.0088 & $<$0.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Variance decomposition on FewRel (3 seeds $\\times$ 25 batches per count level). Batch SD: root-mean intra-seed variance averaged over seeds. Seed SD: standard deviation of per-seed means. Ratio = batch variance / seed variance. At count 80, only one batch composition exists, so batch variance vanishes by construction.}\n\\label{tab:variance_decomposition}\n\\end{table}\n\nIntra-batch variance dominates inter-seed variance by 5--474$\\times$ across count levels 4--64 (mean 125$\\times$); random batch composition is the primary source of performance variability. Under greedy decoding (temperature${}\\,=\\,0$), model inference is nearly deterministic; the inter-seed variance reflects differences in which random batch compositions each seed generates, not inference stochasticity. At count 80, the full schema admits only one composition, leaving residual model-level noise as the sole variance source (seed SD = 0.88\\,pp, likely attributable to FP8 quantization non-determinism).\n\n\\section{Cross-Domain Connections}\n\\label{app:cross-domain}\n\nThe schema-associated degradation documented here is not unique to information extraction. Schema-Guided Dialogue systems (SGD/SGD-X; \\citealt{rastogi2020towards}) face an analogous challenge: as the number of intent and slot types grows, dialogue state tracking accuracy declines. \\citet{li2023evaluating} observed count-dependent degradation in ChatGPT-based IE, attributing it to prompt overload. Our two-dimensional decomposition offers a more refined explanation: schema size per se is not the sole predictor; rather, larger schemas increase the probability of including high-SCS pairs, which contribute disproportionately to confusion. This distinction has practical implications: a schema of 80 types with low mutual confusability may outperform a 40-type schema with clustered semantics, and suggests that confusability-aware design principles may generalize to any task where an LLM must discriminate among a prompt-specified label inventory.\n\n\\section{Cross-Model Validation with LLaMA-3.1-70B-Instruct (FP8)}\n\\label{sec:appendix_cross_model_70b}\n\nTo test whether the two-dimensional degradation pattern generalizes across model families, we replicate the count-curve and BCS-controlled experiments on Meta-LLaMA-3.1-70B-Instruct (FP8 quantization). All batch compositions, type pools, and test samples are identical to those used for Qwen3-32B (\\S\\ref{sec:count_curves}, \\S\\ref{sec:bcs_controlled}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{LLaMA-70B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{RE (FewRel, Classification Accuracy)}} \\\\\n8  & 0.757 & 0.805 \\\\\n16 & 0.685 & 0.719 \\\\\n32 & 0.601 & 0.652 \\\\\n64 & 0.504 & 0.539 \\\\\n80 & 0.450 & 0.504 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{NER (Few-NERD, Text+Type Match Recall)}} \\\\\n2  & 0.323 & 0.515 \\\\\n6  & 0.300 & 0.399 \\\\\n12 & 0.278 & 0.318 \\\\\n22 & 0.252 & 0.279 \\\\\n44 & 0.297 & 0.309 \\\\\n66 & 0.273 & 0.407 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count curves for LLaMA-3.1-70B-Instruct (FP8) and Qwen3-32B. RE decline (count 8$\\to$80): $-$30.7\\,pp (70B) vs.\\ $-$30.1\\,pp (32B). NER decline (count 2$\\to$22): $-$7.1\\,pp (70B) vs.\\ $-$23.6\\,pp (32B); both models exhibit a U-shaped rebound at higher counts. 25 batches per count level, same samples and batch compositions across models (seed 42). All metrics are micro-averaged across batches.}\n\\label{tab:cross_model_70b}\n\\end{table}\n\nTable~\\ref{tab:cross_model_70b} shows that RE degradation slopes are near-identical: $-$30.7\\,pp (70B) versus $-$30.1\\,pp (32B) from count 8 to count 80, with the 70B model approximately 4\\,pp lower in absolute accuracy at each count level. This quantitative match provides strong evidence that Dimension~1 (count-related decline) is directionally consistent across architectures for RE.\n\nOn NER, the count-related decline direction is consistent across models: both 70B and Qwen3 show a recall decline from count 2 to count 22 (70B: 0.323$\\to$0.252, $-$7.1\\,pp; Qwen3: 0.515$\\to$0.279, $-$23.6\\,pp). Both models also exhibit a U-shaped rebound at higher counts (70B: 0.252 at count 22 $\\to$ 0.297 at count 44; Qwen3: 0.279 at count 22 $\\to$ 0.407 at count 66), which cross-validates the U-shape phenomenon. The magnitude difference reflects a precision-recall tradeoff: 70B operates more conservatively (higher precision, lower recall), while Qwen3 over-predicts (higher recall, lower precision, especially at low counts).\n\nFor the confusability dimension (Dimension 2), at count 16 on FewRel, LLaMA-70B achieves low-BCS accuracy of 0.708 versus high-BCS accuracy of 0.599 ($\\Delta = +10.9$\\,pp, 95\\% CI: [$+$3.0, $+$20.1]). The confidence interval excludes zero; the confusability effect is thus confirmed at the 70B scale.\n\nIn summary, FewRel RE provides a quantitative match across models (near-identical slopes for Dimension~1 and a significant Dimension~2 effect). NER provides directional consistency: the count-related decline direction is preserved and the U-shaped rebound replicates, though magnitudes vary with each model's precision-recall operating point. Together, these results indicate that the degradation pattern is directionally consistent across architectures.\n\n\\section{Cross-Model Validation with Gemini 2.5 Flash (API)}\n\\label{sec:appendix_cross_model_gemini}\n\nWe further validate Dimension~1 on a proprietary model, Gemini 2.5 Flash \\citep{gemini-2025}, accessed via API. This extends the cross-model evidence from open-weight families (Qwen, LLaMA) to a proprietary architecture with unknown training details. We replicate the FewRel count-curve experiment using the same 960 balanced samples, batch compositions, and evaluation protocol as Qwen3-32B.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Gemini Flash} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1  & 0.827 & --- \\\\\n4  & 0.873 & 0.870 \\\\\n8  & 0.820 & 0.805 \\\\\n16 & 0.787 & 0.719 \\\\\n32 & 0.739 & 0.652 \\\\\n64$^\\dagger$ & 0.637 & 0.539 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count curves for Gemini 2.5 Flash (API) and Qwen3-32B on FewRel RE (classification accuracy). 25 batches per count level, same samples and batch compositions (seed 42). Gemini's count-1 result is included for completeness; Qwen3 count-1 was not collected. Both models show monotonic decline from count 4 onward ($\\rho = -1.0$ for both on counts 4--32). $^\\dagger$Count 64: Gemini based on 11/25 batches (partial).}\n\\label{tab:cross_model_gemini}\n\\end{table}\n\nTable~\\ref{tab:cross_model_gemini} confirms that the count-related accuracy decline replicates on Gemini 2.5 Flash. From count 4 to count 32, both models show perfectly monotonic decline (Spearman $\\rho = -1.0$). Including count 1, the Gemini count curve yields $\\rho = -0.900$ ($p = 0.037$); including partial count-64 data (11/25 batches), $\\rho = -0.943$ ($p = 0.005$). The decline magnitude is smaller for Gemini ($-$13.3\\,pp from count 4 to 32) than for Qwen3 ($-$21.8\\,pp), consistent with Gemini's higher absolute accuracy providing more headroom before degradation saturates. At each count level, Gemini matches or exceeds Qwen3, with the gap widening at higher counts (0.3\\,pp at count 4 vs.\\ 8.7\\,pp at count 32, 9.8\\,pp at partial count 64); Gemini appears more robust to schema scaling but not immune. Dimension~2 (BCS-controlled confusability) has not been tested on proprietary models; cross-architecture Dimension~2 validation remains for future work.\n\n\\section{Few-Shot Prompting and Confusability}\n\\label{sec:appendix_fewshot_bcs}\n\nTo test whether in-context demonstrations mitigate the BCS-associated confusability effect, we evaluate 0-shot, 1-shot, and 5-shot prompting on FewRel 80-relation RE at count 8 using the same extreme-BCS batch design as \\S\\ref{sec:bcs_controlled}. Each condition uses 50 batches (25 low-BCS, mean $\\approx 0.36$; 25 high-BCS, mean $\\approx 0.80$), drawn from the pre-constructed batch pool of \\S\\ref{sec:bcs_controlled}. Few-shot examples are sampled from the FewRel training split for each target type.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lrrrl}\n\\toprule\n\\textbf{Condition} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n0-shot & 0.682 & 0.498 & +18.5 & {[}+14.3, +22.7{]} \\\\\n1-shot & 0.754 & 0.554 & +20.0 & {[}+16.3, +23.5{]} \\\\\n5-shot & 0.715 & 0.488 & +22.8 & {[}+18.9, +26.8{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS gap under few-shot prompting (FewRel, count 8). Demonstrations improve absolute accuracy on low-BCS batches (+3.3--7.2\\,pp over 0-shot) but provide inconsistent benefit on high-BCS batches (+5.6\\,pp at 1-shot, $-$1.0\\,pp at 5-shot). The confusability gap widens from +18.5\\,pp (0-shot) to +22.8\\,pp (5-shot). All metrics are micro-averaged across batches.}\n\\label{tab:fewshot_bcs}\n\\end{table}\n\nDemonstrations improve absolute accuracy primarily on low-BCS (easy) batches, where type boundaries are already distinct and examples reinforce correct mappings. On high-BCS batches, where types are semantically confusable, demonstrations provide inconsistent benefit (+5.6\\,pp at 1-shot, $-$1.0\\,pp at 5-shot): the model still substitutes similar types at comparable rates. The net effect is that the confusability gap widens under few-shot prompting (+4.3\\,pp from 0-shot to 5-shot, bootstrap $p = 0.014$), with all three confidence intervals excluding zero. This indicates that BCS-associated type confusion is a structural property of the schema composition rather than a deficit addressable through prompt engineering. The non-monotonic low-BCS pattern (0.754 at 1-shot vs.\\ 0.715 at 5-shot) may reflect lost-in-middle effects from increased prompt length \\cite{lost-in-middle-2024}.\n\nThe 0-shot gap (+18.5\\,pp) is smaller than the extreme-batch gap reported in \\S\\ref{sec:bcs_controlled} (+25.5\\,pp) because the two experiments use different test splits and batch sampling seeds; direct magnitude comparison across experiments is not appropriate.\n\n\\section{Qualitative Error Analysis}\n\\label{app:error-analysis}\n\nTables~\\ref{tab:top10_re} and~\\ref{tab:top10_ner} list the ten most frequently confused type pairs on FewRel 80-relation RE and Few-NERD NER. Confusion counts are aggregated bidirectionally across three random seeds (72{,}000 predictions per seed for RE; single-seed 66-type extraction for NER).\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\begin{tabular}{clllr}\n\\toprule\n\\textbf{\\#} & \\textbf{Type A} & \\textbf{Type B} & \\textbf{SCS} & \\textbf{$N$} \\\\\n\\midrule\n1 & instance of & taxon rank & 0.53 & 875 \\\\\n2 & child & father & 0.84 & 700 \\\\\n3 & participant of & participating team & 0.75 & 675 \\\\\n4 & mountain range & part of & 0.57 & 575 \\\\\n5 & mouth of watercourse & tributary & 0.65 & 549 \\\\\n6 & child & mother & 0.84 & 500 \\\\\n7 & league & member of & 0.66 & 450 \\\\\n8 & country of citizenship & country of origin & 0.76 & 400 \\\\\n9 & followed by & follows & 0.90 & 400 \\\\\n10 & occupation & voice type & 0.57 & 400 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Top-10 confused relation pairs on FewRel 80-relation RE. $N$: bidirectional confusion count aggregated over 3 seeds $\\times$ 25 batches. SCS: pairwise Schema Confusability Score (Qwen3 embedding cosine similarity). High-SCS pairs (e.g., \\textit{followed by}/\\textit{follows}, SCS\\,=\\,0.90) and family-relation pairs (\\textit{child}/\\textit{father}, \\textit{child}/\\textit{mother}) dominate. Some low-SCS pairs (\\textit{instance of}/\\textit{taxon rank}, SCS\\,=\\,0.53) reflect domain-specific co-occurrence rather than semantic similarity.}\n\\label{tab:top10_re}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\begin{tabular}{clllr}\n\\toprule\n\\textbf{\\#} & \\textbf{Type A} & \\textbf{Type B} & \\textbf{SCS} & \\textbf{$N$} \\\\\n\\midrule\n1 & person-other & person-politician & 0.93 & 121 \\\\\n2 & location-GPE & organization-other & 0.83 & 81 \\\\\n3 & art-film & location-GPE & 0.69 & 57 \\\\\n4 & building-other & location-GPE & 0.85 & 56 \\\\\n5 & building-other & person-other & 0.90 & 43 \\\\\n6 & location-GPE & product-other & 0.69 & 39 \\\\\n7 & org-gov/agency & person-other & 0.85 & 34 \\\\\n8 & person-actor & person-other & 0.90 & 34 \\\\\n9 & building-other & location-road/transit & 0.76 & 32 \\\\\n10 & location-GPE & org-sportsleague & 0.81 & 30 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Top-10 confused entity type pairs on Few-NERD NER. $N$: bidirectional confusion count from 66-type full-schema extraction. SCS: pairwise Schema Confusability Score (Qwen3 embedding cosine similarity). Intra-category confusions (e.g., \\textit{person-other}/\\textit{person-politician}, SCS\\,=\\,0.93) and cross-category pairs sharing referent overlap (\\textit{building-other}/\\textit{location-GPE}, SCS\\,=\\,0.85) are most frequent. The ``other'' subtypes absorb diverse entities and confuse with more specific siblings.}\n\\label{tab:top10_ner}\n\\end{table}\n\n\\paragraph{Illustrative error instances.}\nTable~\\ref{tab:error_examples} shows three FewRel instances where the model predicted a semantically adjacent relation. All gold-predicted pairs have SCS\\,$>$\\,0.90.\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{p{5.8cm}llc}\n\\toprule\n\\textbf{Sentence (abridged)} & \\textbf{Gold} & \\textbf{Predicted} & \\textbf{SCS} \\\\\n\\midrule\nOver five EuroLeague games he played for \\textbf{Valencia}, he averaged 8 points \\ldots\\  [\\textbf{EuroLeague}, \\textbf{Valencia}] & participant & participant of & 0.97 \\\\\n\\addlinespace\n\\textbf{Pilões} is a municipality in the state of \\textbf{Rio Grande do Norte} in the Northeast region of Brazil. & contains admin.\\ terr.\\ entity & located in admin.\\ terr.\\ entity & 0.92 \\\\\n\\addlinespace\nIn May 1997 Davies was appointed \\ldots\\ to the \\textbf{Cabinet} as \\textbf{Secretary of State for Wales}. & part of & member of & 0.90 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Representative confusion instances from FewRel 80-relation RE (Qwen3-32B, count\\,=\\,80). Head and tail entities are bolded. In each case, the gold and predicted relations are semantically close (SCS\\,$>$\\,0.90): \\textit{participant} vs.\\ \\textit{participant of} reverses argument directionality; \\textit{contains} vs.\\ \\textit{located in} inverts the containment relation; \\textit{part of} vs.\\ \\textit{member of} conflates meronymy with membership. These confusions are consistent with the pairwise SCS--confusion correlation reported in \\S\\ref{sec:pairwise}.}\n\\label{tab:error_examples}\n\\end{table}\n\n\\end{document}\n",
    "structuredPatch": [
      {
        "oldStart": 678,
        "oldLines": 4,
        "newStart": 678,
        "newLines": 26,
        "lines": [
          " \\label{tab:error_examples}",
          " \\end{table}",
          " ",
          "+\\section{Schema Label Renaming Experiment}",
          "+\\label{app:renaming}",
          "+",
          "+To test whether reducing pairwise SCS through label renaming improves accuracy, we conducted a controlled intervention on FewRel 80-relation RE (count 8, Qwen3-32B). We identified 14 high-SCS relation pairs (mean SCS = 0.87) and replaced one label in each pair with a semantically distinct paraphrase chosen to minimize embedding cosine similarity (all-MiniLM-L6-v2). Examples: \\textit{participant of} $\\to$ \\textit{event involvement} (SCS: 0.97 $\\to$ 0.72), \\textit{follows} $\\to$ \\textit{prior entry} (0.90 $\\to$ 0.69), \\textit{part of} $\\to$ \\textit{integral segment of} (0.90 $\\to$ 0.64). The renaming reduced mean pairwise SCS from 0.87 to 0.67 ($\\Delta = -0.20$). We ran the same 50 BCS-controlled batches (25 low-BCS, 25 high-BCS; 96 samples each) under both original (control) and renamed (treatment) label sets.",
          "+",
          "+\\begin{table}[h]",
          "+\\centering",
          "+\\small",
          "+\\begin{tabular}{lccc}",
          "+\\toprule",
          "+& \\textbf{Control} & \\textbf{Treatment} & \\textbf{$\\Delta$\\,(pp)} \\\\",
          "+\\midrule",
          "+Low-BCS ($n=25$)  & 90.1 & 87.1 & $-$3.0 \\\\",
          "+High-BCS ($n=25$) & 69.3 & 60.5 & $-$8.8 \\\\",
          "+\\bottomrule",
          "+\\end{tabular}",
          "+\\caption{Accuracy (\\%) under original vs.\\ renamed labels on FewRel count-8 batches. Renaming reduced embedding similarity but decreased accuracy in both groups, with a larger drop on high-BCS batches (Cohen's $d = -2.92$) than low-BCS ($d = -1.09$). Interaction: $\\Delta_{\\text{high}} - \\Delta_{\\text{low}} = -5.9$\\,pp ($t = -7.23$, $p < 0.001$).}",
          "+\\label{tab:renaming}",
          "+\\end{table}",
          "+",
          "+Renaming hurt accuracy uniformly: both groups showed significant declines (paired $t$-test, both $p < 0.001$). The number of renamed types per batch correlated negatively with accuracy change ($r = -0.625$, $p < 0.001$). A solo sanity check confirmed that 11 of 12 renamed labels were individually recognizable (accuracy $\\geq$ original $-5$\\,pp). The results indicate that replacing familiar Wikidata labels with unfamiliar paraphrases disrupts the model's type semantics; this label unfamiliarity effect outweighs any benefit from reduced confusability.",
          "+",
          " \\end{document}"
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

_source line 39_

Let me verify both edits.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c6b2a1-3665-4eeb-aad0-d119dd87428b",
  "uuid": "94961997-6c4e-40f6-88c3-643be968deda",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013YWs4zgFavYEUPhPCg69CQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3515,
      "cache_read_input_tokens": 40290,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3515
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

<details open><summary>🔧 Tool call — Read · `toolu_011d8VG79MfnPQ4d2R6BXrdy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": 44,
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c6b2a1-3665-4eeb-aad0-d119dd87428b",
  "uuid": "c5e9fa44-90dd-41df-b5e7-360c2edfe9e9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013YWs4zgFavYEUPhPCg69CQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3515,
      "cache_read_input_tokens": 40290,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3515
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

_source line 41 · 2026-05-18T21:36:26.620Z_

<details><summary>↩ Tool result · `toolu_011d8VG79MfnPQ4d2R6BXrdy`</summary>

```text
44	\item \textbf{Task format dependency.} BCS batch-level prediction is demonstrated only under RE's forced-choice classification format. An unconstrained decoding ablation ($n = 25$) confirms this: removing the enum constraint eliminates the BCS--accuracy correlation ($\rho = -0.14$, $p = 0.49$), establishing that the batch-level signal is specific to forced-choice RE. NER exact-match evaluation conflates boundary and type errors, and relaxed matching may yield different confusability effect sizes.
45	
46	\item \textbf{Causal mechanism.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway. A post-hoc renaming experiment (Appendix~\ref{app:renaming}) confirms this concern: replacing high-SCS labels with semantically distinct paraphrases reduced pairwise embedding similarity but decreased accuracy by 3--9\,pp, as label unfamiliarity introduced errors that outweighed any confusability reduction.
47	
48	\item \textbf{Data contamination.} FewRel (2018) may appear in pretraining corpora, but train-origin relations show numerically lower accuracy than val-origin ($-8.8$\,pp, $p = 0.06$, n.s.), opposite to the contamination hypothesis. The monotonic degradation curve cannot be explained by uniform contamination. DocRED (2019) provides a lower-contamination-risk replication with consistent BCS--accuracy slopes ($R^2 = 0.53$). Adding train-origin ratio as a covariate leaves the BCS partial effect unchanged ($p = 0.245$; Appendix~\ref{app:split-origin}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e8c6b2a1-3665-4eeb-aad0-d119dd87428b",
  "uuid": "e44626d2-cd87-46b3-b401-46e72753ea38",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
      "content": "\\item \\textbf{Task format dependency.} BCS batch-level prediction is demonstrated only under RE's forced-choice classification format. An unconstrained decoding ablation ($n = 25$) confirms this: removing the enum constraint eliminates the BCS--accuracy correlation ($\\rho = -0.14$, $p = 0.49$), establishing that the batch-level signal is specific to forced-choice RE. NER exact-match evaluation conflates boundary and type errors, and relaxed matching may yield different confusability effect sizes.\n\n\\item \\textbf{Causal mechanism.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway. A post-hoc renaming experiment (Appendix~\\ref{app:renaming}) confirms this concern: replacing high-SCS labels with semantically distinct paraphrases reduced pairwise embedding similarity but decreased accuracy by 3--9\\,pp, as label unfamiliarity introduced errors that outweighed any confusability reduction.\n\n\\item \\textbf{Data contamination.} FewRel (2018) may appear in pretraining corpora, but train-origin relations show numerically lower accuracy than val-origin ($-8.8$\\,pp, $p = 0.06$, n.s.), opposite to the contamination hypothesis. The monotonic degradation curve cannot be explained by uniform contamination. DocRED (2019) provides a lower-contamination-risk replication with consistent BCS--accuracy slopes ($R^2 = 0.53$). Adding train-origin ratio as a covariate leaves the BCS partial effect unchanged ($p = 0.245$; Appendix~\\ref{app:split-origin}).",
      "numLines": 5,
      "startLine": 44,
      "totalLines": 704
    }
  }
}
```

</details>

---

### Tool call

_source line 42_

<details open><summary>🔧 Tool call — Read · `toolu_011542RQGYvQ9UdRLvFquhZn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": 679,
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c6b2a1-3665-4eeb-aad0-d119dd87428b",
  "uuid": "5b09c4ce-7a83-4e28-bf4c-5902640a0bfd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013YWs4zgFavYEUPhPCg69CQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3515,
      "cache_read_input_tokens": 40290,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3515
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

_source line 43 · 2026-05-18T21:36:27.234Z_

<details><summary>↩ Tool result · `toolu_011542RQGYvQ9UdRLvFquhZn`</summary>

```text
679	\end{table}
680	
681	\section{Schema Label Renaming Experiment}
682	\label{app:renaming}
683	
684	To test whether reducing pairwise SCS through label renaming improves accuracy, we conducted a controlled intervention on FewRel 80-relation RE (count 8, Qwen3-32B). We identified 14 high-SCS relation pairs (mean SCS = 0.87) and replaced one label in each pair with a semantically distinct paraphrase chosen to minimize embedding cosine similarity (all-MiniLM-L6-v2). Examples: \textit{participant of} $\to$ \textit{event involvement} (SCS: 0.97 $\to$ 0.72), \textit{follows} $\to$ \textit{prior entry} (0.90 $\to$ 0.69), \textit{part of} $\to$ \textit{integral segment of} (0.90 $\to$ 0.64). The renaming reduced mean pairwise SCS from 0.87 to 0.67 ($\Delta = -0.20$). We ran the same 50 BCS-controlled batches (25 low-BCS, 25 high-BCS; 96 samples each) under both original (control) and renamed (treatment) label sets.
685	
686	\begin{table}[h]
687	\centering
688	\small
689	\begin{tabular}{lccc}
690	\toprule
691	& \textbf{Control} & \textbf{Treatment} & \textbf{$\Delta$\,(pp)} \\
692	\midrule
693	Low-BCS ($n=25$)  & 90.1 & 87.1 & $-$3.0 \\
694	High-BCS ($n=25$) & 69.3 & 60.5 & $-$8.8 \\
695	\bottomrule
696	\end{tabular}
697	\caption{Accuracy (\%) under original vs.\ renamed labels on FewRel count-8 batches. Renaming reduced embedding similarity but decreased accuracy in both groups, with a larger drop on high-BCS batches (Cohen's $d = -2.92$) than low-BCS ($d = -1.09$). Interaction: $\Delta_{\text{high}} - \Delta_{\text{low}} = -5.9$\,pp ($t = -7.23$, $p < 0.001$).}
698	\label{tab:renaming}
699	\end{table}
700	
701	Renaming hurt accuracy uniformly: both groups showed significant declines (paired $t$-test, both $p < 0.001$). The number of renamed types per batch correlated negatively with accuracy change ($r = -0.625$, $p < 0.001$). A solo sanity check confirmed that 11 of 12 renamed labels were individually recognizable (accuracy $\geq$ original $-5$\,pp). The results indicate that replacing familiar Wikidata labels with unfamiliar paraphrases disrupts the model's type semantics; this label unfamiliarity effect outweighs any benefit from reduced confusability.
702	
703	\end{document}
704	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e8c6b2a1-3665-4eeb-aad0-d119dd87428b",
  "uuid": "684180de-b410-4093-87ce-5f2d65116e2b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
      "content": "\\end{table}\n\n\\section{Schema Label Renaming Experiment}\n\\label{app:renaming}\n\nTo test whether reducing pairwise SCS through label renaming improves accuracy, we conducted a controlled intervention on FewRel 80-relation RE (count 8, Qwen3-32B). We identified 14 high-SCS relation pairs (mean SCS = 0.87) and replaced one label in each pair with a semantically distinct paraphrase chosen to minimize embedding cosine similarity (all-MiniLM-L6-v2). Examples: \\textit{participant of} $\\to$ \\textit{event involvement} (SCS: 0.97 $\\to$ 0.72), \\textit{follows} $\\to$ \\textit{prior entry} (0.90 $\\to$ 0.69), \\textit{part of} $\\to$ \\textit{integral segment of} (0.90 $\\to$ 0.64). The renaming reduced mean pairwise SCS from 0.87 to 0.67 ($\\Delta = -0.20$). We ran the same 50 BCS-controlled batches (25 low-BCS, 25 high-BCS; 96 samples each) under both original (control) and renamed (treatment) label sets.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n& \\textbf{Control} & \\textbf{Treatment} & \\textbf{$\\Delta$\\,(pp)} \\\\\n\\midrule\nLow-BCS ($n=25$)  & 90.1 & 87.1 & $-$3.0 \\\\\nHigh-BCS ($n=25$) & 69.3 & 60.5 & $-$8.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Accuracy (\\%) under original vs.\\ renamed labels on FewRel count-8 batches. Renaming reduced embedding similarity but decreased accuracy in both groups, with a larger drop on high-BCS batches (Cohen's $d = -2.92$) than low-BCS ($d = -1.09$). Interaction: $\\Delta_{\\text{high}} - \\Delta_{\\text{low}} = -5.9$\\,pp ($t = -7.23$, $p < 0.001$).}\n\\label{tab:renaming}\n\\end{table}\n\nRenaming hurt accuracy uniformly: both groups showed significant declines (paired $t$-test, both $p < 0.001$). The number of renamed types per batch correlated negatively with accuracy change ($r = -0.625$, $p < 0.001$). A solo sanity check confirmed that 11 of 12 renamed labels were individually recognizable (accuracy $\\geq$ original $-5$\\,pp). The results indicate that replacing familiar Wikidata labels with unfamiliar paraphrases disrupts the model's type semantics; this label unfamiliarity effect outweighs any benefit from reduced confusability.\n\n\\end{document}\n",
      "numLines": 26,
      "startLine": 679,
      "totalLines": 704
    }
  }
}
```

</details>

---

### Assistant

_source line 44_

Both edits applied correctly.

**产出汇报：**

1. **Appendix `\ref{app:renaming}`** (L681-701): 实验设计描述 + 2×3 结果表 + 解释段落，约 0.4 页
2. **Limitations 第 4 点** (L46): 更新为引用 Appendix，含具体数据 (3--9 pp)

**实验细节发现：**
- **Rename 策略**：对 14 对高 SCS 关系对（mean SCS=0.87），将其中一个 label 替换为语义不同的 paraphrase，用 all-MiniLM-L6-v2 embedding 选择使 cosine similarity 最小的替代名（mean new SCS=0.67，$\Delta$=-0.20）
- **具体例子**：`participant of` → `event involvement`, `follows` → `prior entry`, `mother` → `female progenitor`, `part of` → `integral segment of`
- **Batches**：复用 BCS-controlled 实验的 50 个 batch（25 low + 25 high），FewRel count=8，每 batch 96 samples
- **低 BCS batch 含 0-2 个被 rename 的 type；高 BCS batch 含 2-4 个**（高 BCS batch 天然包含更多 confusable pairs，因此 rename 更多）
- **Solo sanity check**：12 个被 rename 的 label 中 11 个单独可识别（仅 `mother` → `maternal parent` 失败），排除了"模型完全不认识新 label"的解释

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c6b2a1-3665-4eeb-aad0-d119dd87428b",
  "uuid": "3c04029e-7f10-43d2-bc1e-9e8df6043bbb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014QdM67p5nznm24TD7gSTUE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1522,
      "cache_read_input_tokens": 43805,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1522
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

_source line 45_

Both edits applied correctly.

**产出汇报：**

1. **Appendix `\ref{app:renaming}`** (L681-701): 实验设计描述 + 2×3 结果表 + 解释段落，约 0.4 页
2. **Limitations 第 4 点** (L46): 更新为引用 Appendix，含具体数据 (3--9 pp)

**实验细节发现：**
- **Rename 策略**：对 14 对高 SCS 关系对（mean SCS=0.87），将其中一个 label 替换为语义不同的 paraphrase，用 all-MiniLM-L6-v2 embedding 选择使 cosine similarity 最小的替代名（mean new SCS=0.67，$\Delta$=-0.20）
- **具体例子**：`participant of` → `event involvement`, `follows` → `prior entry`, `mother` → `female progenitor`, `part of` → `integral segment of`
- **Batches**：复用 BCS-controlled 实验的 50 个 batch（25 low + 25 high），FewRel count=8，每 batch 96 samples
- **低 BCS batch 含 0-2 个被 rename 的 type；高 BCS batch 含 2-4 个**（高 BCS batch 天然包含更多 confusable pairs，因此 rename 更多）
- **Solo sanity check**：12 个被 rename 的 label 中 11 个单独可识别（仅 `mother` → `maternal parent` 失败），排除了"模型完全不认识新 label"的解释

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 101850,
  "duration_api_ms": 101984,
  "num_turns": 16,
  "stop_reason": "end_turn",
  "session_id": "e8c6b2a1-3665-4eeb-aad0-d119dd87428b",
  "total_cost_usd": 0.6663024999999999,
  "usage": {
    "input_tokens": 12,
    "cache_creation_input_tokens": 65932,
    "cache_read_input_tokens": 212601,
    "output_tokens": 5827,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 65932,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 452,
        "cache_read_input_tokens": 43805,
        "cache_creation_input_tokens": 1522,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1522
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2112,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0021920000000000004,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 12,
      "outputTokens": 5827,
      "cacheReadInputTokens": 212601,
      "cacheCreationInputTokens": 65932,
      "webSearchRequests": 0,
      "costUSD": 0.6641104999999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "a5a27d5e-b3cb-4f35-89b0-dadb60f95cbc"
}
```

</details>

---
