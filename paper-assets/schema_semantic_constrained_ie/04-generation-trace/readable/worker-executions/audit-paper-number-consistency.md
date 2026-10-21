# audit paper number consistency

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 126
- **Recorded user turns:** 1
- **Tool calls:** 41
- **Original source:** `logs/workers/worker_audit_paper_number_consistency_20260522T040852.log`
- **Structured JSON:** [`b3adc87b37f4c2180b11.json`](../../sessions/b3/b3adc87b37f4c2180b11.json)

## Before a recorded user message

59 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
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
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__update_registry"
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
  "uuid": "618d5568-c6a0-4f9a-8383-ba2c0b760b3c",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/memory/"
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
    "resetsAt": 1779433200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "b263acc3-a6ad-4892-b44a-bda0edbc0696",
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d"
}
```

---

### Assistant

_source line 4_

我来执行这个审计任务。先并行读取论文文件和 registry。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "b97d3716-bf17-418b-a8a8-a9e7cde97535",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FbsjvGNkQtDSv9NXZaDCLC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11973,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11973
      },
      "output_tokens": 4,
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

<details open><summary>🔧 Tool call — Read · `toolu_01KFsK7wbBXficSSxaaqycDq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "3d719ee3-de78-418f-95d6-a24a83ce97ce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FbsjvGNkQtDSv9NXZaDCLC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11973,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11973
      },
      "output_tokens": 4,
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

_source line 6 · 2026-05-22T04:09:01.851Z_

<details><summary>↩ Tool result · `toolu_01KFsK7wbBXficSSxaaqycDq`</summary>

```text
1	% Runtime overhead (inline paragraph, no subsection header to save space)
2	
3	\paragraph{Runtime overhead.}
4	\label{sec:runtime}
5	S1 overhead is $+$13.1\% on SciERC and $+$2.43\% on DocRED (amortized over longer sequences); under LoRA, $+$10.0\% with 37\% lower absolute latency.
6	Constraint compilation is one-time $<$0.5\,s; scaling benchmarks confirm constant overhead (2--3\%) up to 200 entity types and 1{,}000 relations (Appendix~\ref{app:scalability}).
7	
8	\paragraph{Beam search compatibility.}
9	\label{sec:beam-results}
10	Beam search ($k{=}4$)~\cite{anderson2017guided} explores paths satisfying both layers jointly.
11	With LoRA, beam S1 eliminates all four violation types on SciERC (R-F1 44--47); zero-shot beam achieves DR${=}$0\% on both datasets (998-doc DocRED; CF response is model-dependent; Appendix~\ref{app:beam-search}).
12	Total latency: 1.54$\times$ (beam 1.32$\times$ $+$ constraint 1.17$\times$; Table~\ref{tab:beam-latency}).
13	
14	% exp_ids: r16_70b_scierc_zs_s1, 70b_lora_scierc, 70b_lora_docred_200
15	\paragraph{70B evaluation.}
16	\label{sec:70b-results}
17	On Llama-3.3-70B-Instruct (AWQ INT4), zero-shot S1 eliminates DR on SciERC (6.41\%\,$\to$\,0\%; R-F1 11.24, $+$0.09\,pp) with CF 3.50\% (from 0\% unconstrained).
18	% TODO: 待 70B LoRA 结果回填（SciERC 551 docs, DocRED 200-doc subset）
19	LoRA fine-tuning confirms scale-independent composability: SciERC DR XX.XX\%\,$\to$\,XX.XX\% (R-F1 XX.XX); DocRED (200-document subset) DR XX.XX\%\,$\to$\,XX.XX\% (R-F1 XX.XX); CF drops to XX.XX--XX.XX\%, consistent with the 8B pattern (9.90\%\,$\to$\,1.18\%; \S\ref{sec:composability}).
20	
21	% exp_ids: trie_qwen_ft_scierc, trie_qwen_zs_scierc, trie_llama_ft_scierc, trie_llama_zs_scierc
22	\paragraph{Comparison with grammar-constrained approaches.}
23	\label{sec:constrained-baselines}
24	Our grammar-only ablation (Table~\ref{tab:scierc-ablation}, row~2) implements the same class of constraints---vocabulary membership via context-free grammars---as GCD~\cite{geng2023gcd} and the grammar component of BoostCD~\cite{boostcd2025}, achieving RV/ET$\to$0\% but only 24\% DR reduction vs.\ Full S1's 94\%.
25	Without JSON structural enforcement, trie-only vocabulary constraints (GCD-equivalent) are counterproductive: DR rises to 15--96\% (vs.\ 1--15\% unconstrained) because models omit type fields or produce malformed JSON without grammar-level structure (Appendix~\ref{app:trie-baseline}), confirming both layers are necessary.
26	BoostCD's boosting of constrained and unconstrained decoding is complementary and potentially integrable with OntoCoDec's semantic layer.
27	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "8005f9d5-aca8-45a8-91e3-92c478b5c12f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex",
      "content": "% Runtime overhead (inline paragraph, no subsection header to save space)\n\n\\paragraph{Runtime overhead.}\n\\label{sec:runtime}\nS1 overhead is $+$13.1\\% on SciERC and $+$2.43\\% on DocRED (amortized over longer sequences); under LoRA, $+$10.0\\% with 37\\% lower absolute latency.\nConstraint compilation is one-time $<$0.5\\,s; scaling benchmarks confirm constant overhead (2--3\\%) up to 200 entity types and 1{,}000 relations (Appendix~\\ref{app:scalability}).\n\n\\paragraph{Beam search compatibility.}\n\\label{sec:beam-results}\nBeam search ($k{=}4$)~\\cite{anderson2017guided} explores paths satisfying both layers jointly.\nWith LoRA, beam S1 eliminates all four violation types on SciERC (R-F1 44--47); zero-shot beam achieves DR${=}$0\\% on both datasets (998-doc DocRED; CF response is model-dependent; Appendix~\\ref{app:beam-search}).\nTotal latency: 1.54$\\times$ (beam 1.32$\\times$ $+$ constraint 1.17$\\times$; Table~\\ref{tab:beam-latency}).\n\n% exp_ids: r16_70b_scierc_zs_s1, 70b_lora_scierc, 70b_lora_docred_200\n\\paragraph{70B evaluation.}\n\\label{sec:70b-results}\nOn Llama-3.3-70B-Instruct (AWQ INT4), zero-shot S1 eliminates DR on SciERC (6.41\\%\\,$\\to$\\,0\\%; R-F1 11.24, $+$0.09\\,pp) with CF 3.50\\% (from 0\\% unconstrained).\n% TODO: 待 70B LoRA 结果回填（SciERC 551 docs, DocRED 200-doc subset）\nLoRA fine-tuning confirms scale-independent composability: SciERC DR XX.XX\\%\\,$\\to$\\,XX.XX\\% (R-F1 XX.XX); DocRED (200-document subset) DR XX.XX\\%\\,$\\to$\\,XX.XX\\% (R-F1 XX.XX); CF drops to XX.XX--XX.XX\\%, consistent with the 8B pattern (9.90\\%\\,$\\to$\\,1.18\\%; \\S\\ref{sec:composability}).\n\n% exp_ids: trie_qwen_ft_scierc, trie_qwen_zs_scierc, trie_llama_ft_scierc, trie_llama_zs_scierc\n\\paragraph{Comparison with grammar-constrained approaches.}\n\\label{sec:constrained-baselines}\nOur grammar-only ablation (Table~\\ref{tab:scierc-ablation}, row~2) implements the same class of constraints---vocabulary membership via context-free grammars---as GCD~\\cite{geng2023gcd} and the grammar component of BoostCD~\\cite{boostcd2025}, achieving RV/ET$\\to$0\\% but only 24\\% DR reduction vs.\\ Full S1's 94\\%.\nWithout JSON structural enforcement, trie-only vocabulary constraints (GCD-equivalent) are counterproductive: DR rises to 15--96\\% (vs.\\ 1--15\\% unconstrained) because models omit type fields or produce malformed JSON without grammar-level structure (Appendix~\\ref{app:trie-baseline}), confirming both layers are necessary.\nBoostCD's boosting of constrained and unconstrained decoding is complementary and potentially integrable with OntoCoDec's semantic layer.\n",
      "numLines": 27,
      "startLine": 1,
      "totalLines": 27
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01CWCdKKdZMcARyPDJo7pMbV`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry",
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
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "73ec0243-cf77-4abf-a351-d77612229e35",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FbsjvGNkQtDSv9NXZaDCLC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11973,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11973
      },
      "output_tokens": 4,
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

_source line 8 · 2026-05-22T04:09:02.611Z_

<details><summary>↩ Tool result · `toolu_01CWCdKKdZMcARyPDJo7pMbV`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_registry"
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
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "bdd46b73-7e70-40a8-b684-e30f7ec9f029",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry"
    ],
    "query": "select:mcp__agent-ml-research__read_registry",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Assistant

_source line 9_

<details><summary>Logged reasoning block</summary>

```text
Now let me extract the exp_ids mentioned in the file and read the registry. The exp_ids mentioned are:
- r16_70b_scierc_zs_s1
- 70b_lora_scierc
- 70b_lora_docred_200
- trie_qwen_ft_scierc
- trie_qwen_zs_scierc
- trie_llama_ft_scierc
- trie_llama_zs_scierc

But there are also numbers in the file that don't have explicit exp_id comments - the runtime overhead numbers in the first paragraph and beam search numbers. Let me first read the full registry to find all relevant experiments.


I'll need to access the registry to look up all the experiment details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "4668b930-196c-4601-898b-9ecf089ea8a7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013CZUFiCPTsm1MziTsYmk27",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1605,
      "cache_read_input_tokens": 23814,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1605
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

_source line 10_

Now let me read the registry to find all relevant experiments. I'll also need to check for runtime/beam-related experiments that aren't explicitly tagged with exp_ids.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "74e66014-a707-4f43-b6fe-c7f6793fe533",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013CZUFiCPTsm1MziTsYmk27",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1605,
      "cache_read_input_tokens": 23814,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1605
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

_source line 11_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_012WaS4HZzd72ZytWSZ8crTd`</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "limit": 0,
  "fields": [
    "*"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "b0dfd889-e4b1-4876-b3fd-2a6240bd125f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013CZUFiCPTsm1MziTsYmk27",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1605,
      "cache_read_input_tokens": 23814,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1605
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

_source line 12 · 2026-05-22T04:09:11.097Z_

<details><summary>↩ Tool result · `toolu_012WaS4HZzd72ZytWSZ8crTd`</summary>

```text
Error: result (257,849 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/06688fc2-d26c-40b0-8ebe-68d505b40c0d/tool-results/mcp-agent-ml-research-read_registry-1779422951081.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/06688fc2-d26c-40b0-8ebe-68d505b40c0d/tool-results/mcp-agent-ml-research-read_registry-1779422951081.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "bc2f03ba-e2f4-468b-a9d6-deb27ae17bdb",
  "tool_use_result": {
    "content": "Error: result (257,849 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/06688fc2-d26c-40b0-8ebe-68d505b40c0d/tool-results/mcp-agent-ml-research-read_registry-1779422951081.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/06688fc2-d26c-40b0-8ebe-68d505b40c0d/tool-results/mcp-agent-ml-research-read_registry-1779422951081.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"d066_sweep_llama_beam8_unc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T12:06:56.291Z\", \"updated_at\": \"2026-05-22T04:07:12.776Z\", \"hypothesis\": \"d066 DocRED beam sweep sub-task: Llama beam8 unconstrained on 200-doc subset (westd-16980 GPU1). Part of d066_beam_sweep parent experiment.\", \"parent\": \"d066_beam_sweep\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode unconstrained --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --decoding_strategy beam --num_beams 8 --max_new_tokens 4096 --max_samples 200 --seed 42 --output_file /root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_200_beam8_unconstrained.jsonl\", \"server\": \"westd-16980 GPU1\", \"data_path\": \"data/docred/dev.json (200-doc subset)\", \"data_count\": 200, \"model_name\": \"Llama-3.1-8B LoRA DocRED (merged)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json (200-doc subset)\", \"note\": \"PID 755444. Relay from Llama beam2 s1 (success).\", \"checkpoint_path\": \"westd-16980:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_200_beam8_unconstrained.jsonl\", \"log_path\": \"westd-16980:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_beam8_unc.log\"}, \"conclusion\": \"success\", \"metrics\": {\"E_F1\": 85.77, \"E_P\": 85.7, \"E_R\": 85.84, \"R_F1\": 51.97, \"R_P\": 49.76, \"R_R\": 54.38, \"DR_pct\": 0, \"CF_pct\": 0.05, \"ET_pct\": 0, \"RV_pct\": 0.07, \"parse_fail_pct\": 0.5, \"total_samples\": 200, \"total_entities_pred\": 3788, \"total_relations_pred\": 2779}, \"completed_at\": \"2026-05-20T13:22:18.037Z\"}, \"d066_sweep_llama_beam2_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:07:25.146Z\", \"updated_at\": \"2026-05-22T04:07:10.538Z\", \"hypothesis\": \"d066 DocRED beam sweep sub-task: Llama beam2 constrained (full_s1) on 200-doc subset (westd-16980 GPU1). Part of d066_beam_sweep parent experiment.\", \"parent\": \"d066_beam_sweep\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 nohup python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --decoding_strategy beam --num_beams 2 --max_new_tokens 4096 --max_samples 200 --seed 42\", \"server\": \"westd-16980 GPU1\", \"data_path\": \"data/docred/dev.json (200-doc subset)\", \"data_count\": 200, \"model_name\": \"Llama-3.1-8B LoRA DocRED (merged)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json (200-doc subset)\", \"note\": \"PID 750801. Relay from Llama beam2 unc (success).\", \"checkpoint_path\": \"westd-16980:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_200_beam2_full_s1.jsonl\", \"log_path\": \"westd-16980:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_beam2_s1.log\"}, \"conclusion\": \"success\", \"metrics\": {\"E_F1\": 85.6, \"E_P\": 85.29, \"E_R\": 85.92, \"R_F1\": 51.17, \"R_P\": 48.51, \"R_R\": 54.14, \"DR_pct\": 0, \"CF_pct\": 0, \"ET_pct\": 0, \"RV_pct\": 0, \"parse_fail_pct\": 0.5, \"total_samples\": 200, \"total_entities_pred\": 3814, \"total_relations_pred\": 2839}, \"completed_at\": \"2026-05-20T12:06:48.878Z\"}, \"eval_70b_lora_docred_200_unconstrained\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T04:06:11.811Z\", \"updated_at\": \"2026-05-22T04:06:49.514Z\", \"hypothesis\": \"70B LoRA-finetuned model (r16, Llama-3.1-70B-AWQ-INT4) will achieve higher R-F1 than 8B models on DocRED 200-doc subset unconstrained extraction, serving as the unconstrained baseline for S1 comparison at 70B scale\", \"parent\": \"r16_70b_lora_docred\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 -c 'import peft.import_utils as _piu; _piu.is_gptqmodel_available = lambda: False; import runpy, sys; sys.argv=[...]; runpy.run_path(\\\"run_constrained_extraction.py\\\", run_name=\\\"__main__\\\")'\", \"server\": \"westd-16980\", \"data_path\": \"data/docred/dev.json\", \"data_count\": \"998 (truncated to 200)\", \"model_name\": \"Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-1146)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\", \"eval_data\": \"DocRED dev (200-doc subset)\"}}, \"d066_sweep_llama_docred_beam4_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T15:01:45.514Z\", \"updated_at\": \"2026-05-22T04:03:52.952Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_200_beam4_constrained.jsonl\", \"log_path\": \"/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_beam4_s1.log\", \"metrics\": {\"E-F1\": 85.61, \"E-P\": 85.48, \"E-R\": 85.73, \"R-F1\": 51.89, \"R-P\": 51.59, \"R-R\": 52.2, \"DR%\": 0, \"CF%\": 0, \"PF%\": 0.5, \"ET%\": 0, \"RV%\": 0, \"samples\": 200, \"parse_fail\": 1}, \"command\": \"d066 beam sweep llama docred beam4 s1 (completed, retroactive fix)\", \"server\": \"westd-16980\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 200, \"model_name\": \"Llama-3.1-8B-Instruct + LoRA\", \"seed\": 42}, \"conclusion\": \"success\", \"metrics\": {\"E-F1\": 85.61, \"E-P\": 85.48, \"E-R\": 85.73, \"R-F1\": 51.89, \"R-P\": 51.59, \"R-R\": 52.2, \"DR_pct\": 0, \"CF_pct\": 0, \"PF_pct\": 0.5, \"ET_pct\": 0, \"RV_pct\": 0, \"samples\": 200, \"parse_fail\": 1}, \"hypothesis\": \"Beam search k=4 with Full S1 constraints on Llama DocRED 200-doc will achieve DR=0% and CF near 0%, completing the beam sweep Pareto analysis across all beam widths for the DocRED dataset\", \"completed_at\": \"2026-05-22T04:03:52.952Z\"}, \"r16_70b_lora_scierc_eval\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T02:32:17.414Z\", \"updated_at\": \"2026-05-22T02:32:17.415Z\", \"hypothesis\": \"70B AWQ INT4 LoRA fine-tuned on SciERC will achieve higher R-F1 than 8B FT (Qwen 47.15, Llama 46.13) and S1 constraints will maintain DR→0% at 70B scale\"}, \"eval_70b_lora_scierc_unconstrained\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T02:21:50.531Z\", \"updated_at\": \"2026-05-22T02:22:16.274Z\", \"hypothesis\": \"70B LoRA-finetuned model (r16, Llama-3.1-70B-AWQ-INT4) will achieve higher R-F1 than 8B models (Qwen FT R-F1=47.15, Llama FT R-F1=46.13) on SciERC unconstrained extraction due to larger model capacity\", \"parent\": \"r16_70b_lora_scierc\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py --mode unconstrained --dataset scierc --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --data_path data/processed_data/test.json --output_path /root/autodl-tmp/schema_outputs/r16_70b_lora_scierc/scierc_unconstrained.jsonl --max_new_tokens 4096 --seed 42\", \"server\": \"westd-16980\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-AWQ-INT4 + LoRA r16\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"eval_data\": \"scierc test (551 sentences)\"}}, \"r16_70b_lora_docred\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T12:04:39.980Z\", \"updated_at\": \"2026-05-22T02:11:31.447Z\", \"hypothesis\": \"70B AWQ INT4 + LoRA fine-tuning on DocRED will achieve higher R-F1 than 8B FT models, and S1 constraints will maintain DR→0% at 70B scale with fine-tuning, confirming scale-independent constraint effectiveness across datasets\", \"parent\": \"r16_70b_scierc_zs_s1\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 scripts/train_lora_70b_docred.py\", \"server\": \"westd-16980\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/docred/sft_train_llama.jsonl\", \"data_count\": 3053, \"model_name\": \"Meta-Llama-3.1-70B-Instruct-AWQ-INT4\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/\", \"log_path\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/train.log\", \"checkpoint_source\": \"from_scratch\", \"eval_data\": \"/root/schema_semantic_constrained_ie/data/docred/sft_dev_llama.jsonl\", \"pid\": 839375, \"gpu_ids\": [1], \"note\": \"Restarted from scratch (previous run killed, empty checkpoint dir). LoRA r=16 alpha=32 on q/k/v/o_proj. bs=1 grad_accum=8 lr=2e-5 3epochs. ~10.4h ETA.\"}, \"notes\": \"Restarted with tensorboard. Step 10: loss=0.1472, grad_norm=0.1431. Step 20: loss=0.1499, grad_norm=0.1574. Warmup phase (LR ramping up), loss stable, gradients healthy. AWQ+LoRA working correctly.\", \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T02:08:00.797Z\", \"metrics\": {\"eval_loss\": 0.0635, \"token_acc\": 97.94, \"steps_completed\": 1146, \"epochs\": 3, \"train_loss_start\": 0.147, \"train_loss_end\": 0.056}}, \"r16_70b_lora_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T12:00:09.608Z\", \"updated_at\": \"2026-05-22T02:11:30.415Z\", \"hypothesis\": \"70B AWQ INT4 + LoRA fine-tuning on SciERC will achieve higher R-F1 than 8B FT models, and S1 constraints will maintain DR→0% at 70B scale with fine-tuning\", \"spec\": {\"command\": \"python3 train_70b_lora.py --dataset scierc --model_path /root/autodl-tmp/models/Llama-3.3-70B-Instruct-AWQ-INT4 --output_dir /root/autodl-tmp/checkpoints/70b_lora_scierc --epochs 3 --lr 2e-4 --lora_r 16 --lora_alpha 32\", \"server\": \"westd-16980\", \"data_path\": \"data/sft/scierc_sft_train.jsonl\", \"data_count\": 1762, \"model_name\": \"Llama-3.3-70B-Instruct-AWQ-INT4\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/\", \"log_path\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/train.log\", \"pid\": 836206, \"gpu_ids\": [0, 1]}, \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T02:07:56.630Z\", \"metrics\": {\"eval_loss\": 0.0611, \"token_acc\": 97.78, \"steps_completed\": 663, \"epochs\": 3, \"train_loss_start\": 0.183, \"train_loss_end\": 0.041}}, \"r16_70b_docred_zs_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T05:03:19.394Z\", \"updated_at\": \"2026-05-22T02:07:51.929Z\", \"hypothesis\": \"Llama-3.1-70B-Instruct-AWQ-INT4 with Full S1 constrained decoding on DocRED ZS will achieve DR→0% with R-F1 stable vs unconstrained, extending 70B SciERC results to DocRED and confirming scale-independent constraint effectiveness across datasets\", \"spec\": {\"command\": \"bash /root/schema_semantic_constrained_ie/run_70b_docred_zs.sh\", \"server\": \"westd-21461\", \"gpu\": \"cuda:1\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4\", \"model_path\": \"/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/autodl-tmp/schema_outputs/r16_70b_docred_zs_s1.log\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-22T02:07:51.929Z\"}, \"r16_70b_scierc_zs_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:11:52.091Z\", \"updated_at\": \"2026-05-21T07:09:31.198Z\", \"hypothesis\": \"Llama-3.1-70B-Instruct-AWQ-INT4 with Full S1 constrained decoding on SciERC ZS will achieve DR→0% with R-F1 stable vs unconstrained, extending 70B DocRED results to SciERC and confirming scale-independent constraint effectiveness\", \"spec\": {\"command\": \"bash /root/schema_semantic_constrained_ie/run_70b_scierc_zs.sh\", \"server\": \"westd-16980\", \"gpu\": \"cuda:1\", \"pid\": 808988, \"data_path\": \"SciERC test set (551 sentences)\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4\", \"model_path\": \"/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4\", \"seed\": 42, \"checkpoint_path\": \"N/A (ZS eval)\", \"log_path\": \"/root/schema_semantic_constrained_ie/outputs/r16_70b_scierc_zs_s1.log\"}, \"metrics\": {\"E_F1\": 35.19, \"R_F1\": 11.24, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 3.5, \"parse_fail_pct\": 0, \"samples\": 551, \"baseline_unc_E_F1\": 35.21, \"baseline_unc_R_F1\": 11.15, \"baseline_unc_DR_pct\": 6.41, \"baseline_unc_RV_pct\": 0.61, \"baseline_unc_CF_pct\": 0}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T07:09:31.199Z\"}, \"r14_qwen_docred_beam4_998\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T20:20:43.999Z\", \"updated_at\": \"2026-05-21T05:43:45.941Z\", \"hypothesis\": \"Beam=4 S1 constrained on full DocRED 998-doc test set will show consistent DR elimination and R-F1 stability compared to 50-doc subset, addressing reviewer concern about subset representativeness\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path /root/autodl-tmp/schema_outputs/r14_qwen_docred_beam4_998.jsonl --device cuda:0 --max_new_tokens 4096 --seed 42 --decoding_strategy beam --num_beams 4 --skip_on_error\", \"server\": \"westd-21461\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"Qwen3-8B (zero-shot)\", \"seed\": 42, \"checkpoint_source\": \"N/A (zero-shot)\", \"log_path\": \"/root/autodl-tmp/schema_outputs/r14_qwen_docred_beam4_998.log\", \"checkpoint_path\": \"N/A\"}, \"metrics\": {\"E_F1\": 58.19, \"R_F1\": 8.72, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 4.94, \"parse_fail_pct\": 3.51, \"samples\": 998, \"success\": 963, \"fail\": 35}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T05:43:45.941Z\"}, \"r16_trie_llama_zs_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:44:40.697Z\", \"updated_at\": \"2026-05-21T04:59:53.422Z\", \"hypothesis\": \"Trie-only vocabulary constraint (GCD-equivalent, no JSON structure) on Llama ZS SciERC will show high DR, proving grammar layer is prerequisite for vocabulary membership enforcement\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode trie_only --dataset scierc (Llama ZS)\", \"server\": \"westd-21461\", \"gpu\": \"cuda:1\", \"pid\": 241846, \"data_path\": \"data/scierc/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-8B-Instruct (zero-shot)\", \"seed\": 42, \"checkpoint_path\": \"N/A (trie eval)\", \"log_path\": \"/root/autodl-tmp/schema_outputs/r16_trie_llama_zs.log\"}, \"metrics\": {\"E_F1\": 23.23, \"R_F1\": 2.9, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 84.4, \"CF_pct\": 0.36, \"parse_fail_pct\": 0, \"samples\": 551}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T04:59:53.422Z\"}, \"r16_trie_llama_ft_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:44:39.235Z\", \"updated_at\": \"2026-05-21T04:59:50.515Z\", \"hypothesis\": \"Trie-only vocabulary constraint (GCD-equivalent, no JSON structure) on Llama FT SciERC will show high DR, proving grammar layer is prerequisite for vocabulary membership enforcement\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode trie_only --dataset scierc (Llama FT)\", \"server\": \"westd-21461\", \"gpu\": \"cuda:1\", \"pid\": 241846, \"data_path\": \"data/scierc/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-8B-Instruct (fine-tuned)\", \"seed\": 42, \"checkpoint_path\": \"N/A (trie eval)\", \"log_path\": \"/root/autodl-tmp/schema_outputs/r16_trie_llama_ft.log\"}, \"metrics\": {\"E_F1\": 65.37, \"R_F1\": 41.42, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 15.2, \"CF_pct\": 0, \"parse_fail_pct\": 50.8, \"samples\": 551}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T04:59:50.516Z\"}, \"r16_trie_qwen_zs_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:44:37.808Z\", \"updated_at\": \"2026-05-21T04:59:47.872Z\", \"hypothesis\": \"Trie-only vocabulary constraint (GCD-equivalent, no JSON structure) on Qwen ZS SciERC will show high DR, proving grammar layer is prerequisite for vocabulary membership enforcement\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode trie_only --dataset scierc (Qwen ZS)\", \"server\": \"westd-21461\", \"gpu\": \"cuda:1\", \"pid\": 241846, \"data_path\": \"data/scierc/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B (zero-shot)\", \"seed\": 42, \"checkpoint_path\": \"N/A (trie eval)\", \"log_path\": \"/root/autodl-tmp/schema_outputs/r16_trie_qwen_zs.log\"}, \"metrics\": {\"E_F1\": 30.97, \"R_F1\": 8.64, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 29.3, \"CF_pct\": 0, \"parse_fail_pct\": 0, \"samples\": 551}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T04:59:47.872Z\"}, \"r16_trie_qwen_ft_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:44:36.469Z\", \"updated_at\": \"2026-05-21T04:59:46.097Z\", \"hypothesis\": \"Trie-only vocabulary constraint (GCD-equivalent, no JSON structure) on Qwen FT SciERC will show high DR (comparable to or worse than unconstrained), proving grammar layer is prerequisite for vocabulary membership enforcement\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode trie_only --dataset scierc (Qwen FT)\", \"server\": \"westd-21461\", \"gpu\": \"cuda:1\", \"pid\": 241846, \"data_path\": \"data/scierc/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B (fine-tuned)\", \"seed\": 42, \"checkpoint_path\": \"N/A (trie eval)\", \"log_path\": \"/root/autodl-tmp/schema_outputs/r16_trie_qwen_ft.log\"}, \"metrics\": {\"E_F1\": 66.73, \"R_F1\": 42.57, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 95.5, \"CF_pct\": 0.09, \"parse_fail_pct\": 9.1, \"samples\": 551}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T04:59:46.097Z\"}, \"r14_llama_docred_beam4_998\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T21:47:34.166Z\", \"updated_at\": \"2026-05-21T04:50:39.829Z\", \"hypothesis\": \"Beam=4 S1 constrained on full DocRED 998-doc with Llama-3.1-8B will confirm DR elimination and R-F1 stability seen in 50-doc subset, providing second model evidence for SF3\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/docred/dev.json --output_path /root/autodl-tmp/schema_outputs/r14_llama_docred_beam4_998.jsonl --max_new_tokens 4096 --seed 42 --decoding_strategy beam --num_beams 4 --skip_on_error\", \"server\": \"westd-16980\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"Llama-3.1-8B-Instruct (zero-shot)\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/autodl-tmp/schema_outputs/r14_llama_docred_beam4_998.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T04:50:35.683Z\", \"metrics\": {\"R_F1\": 8.83, \"E_F1\": 57.81, \"DR_pct\": 0, \"CF_pct\": 1, \"ET_pct\": 0, \"RV_pct\": 0, \"parse_fail_pct\": 3.91, \"samples\": 998, \"success\": 959, \"fail\": 39, \"baseline_ZS_greedy_R_F1\": 6.27, \"baseline_ZS_greedy_E_F1\": 54.93, \"baseline_ZS_greedy_DR_pct\": 2.55, \"baseline_ZS_greedy_CF_pct\": 8.54}}, \"d066_sweep_llama_scierc_beam8_s1_551\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T15:38:34.783Z\", \"updated_at\": \"2026-05-20T16:47:28.821Z\", \"hypothesis\": \"d066 SciERC beam sweep: Llama beam8 constrained (full_s1) on 551-sentence test set. Last Llama SciERC config.\", \"parent\": \"d066_beam_sweep\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/checkpoints/llama_lora_scierc_merged --decoding_strategy beam --num_beams 8 --max_new_tokens 4096 --seed 42 --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path /root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_551_beam8_full_s1.jsonl\", \"server\": \"westd-16980\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"llama_lora_scierc_merged\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_scierc_merged\", \"eval_data\": \"scierc test set (551 sentences)\"}, \"reproduce\": {\"finished_at\": \"2026-05-20T16:35:37.041Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T16:35:38.984Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T16:35:47.195455+00:00\"}]}, \"metrics\": {\"E-F1\": 67.51, \"E-P\": 64.99, \"E-R\": 70.23, \"R-F1\": 44.95, \"R-P\": 40.1, \"R-R\": 51.13, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0, \"PF_pct\": 0, \"samples\": 551, \"note\": \"Reconcile false positive corrected. Eval with --dataset scierc confirmed.\"}}, \"d066_sweep_llama_scierc_beam4_s1_551\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T15:04:24.318Z\", \"updated_at\": \"2026-05-20T16:42:22.936Z\", \"conclusion\": \"success\", \"metrics\": {\"E-F1\": 68.06, \"E-P\": 65.96, \"E-R\": 70.29, \"R-F1\": 46.18, \"R-P\": 42.1, \"R-R\": 51.13, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0, \"parse_fail\": 0, \"samples\": 551, \"note\": \"ET/RV corrected from 100→0: original eval used hardcoded DocRED ontology, re-evaled with --dataset scierc\"}, \"log_path\": \"/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_beam4_s1_551.log\", \"checkpoint_path\": \"/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_551_beam4_full_s1.jsonl\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/checkpoints/llama_lora_scierc_merged --decoding_strategy beam --num_beams 4 --max_new_tokens 4096 --seed 42 --data_path data/processed_data/test.json --output_path /root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_551_beam4_full_s1.jsonl\", \"server\": \"westd-21461\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"llama_lora_scierc_merged\", \"seed\": 42}, \"hypothesis\": \"d066 SciERC beam sweep: Llama beam4 constrained (full_s1) on 551-sentence test set. Beam width k=4 with schema constraints should eliminate all four violation types (ET/RV/DR/CF=0) while maintaining R-F1 within ±1pp of unconstrained.\", \"completed_at\": \"2026-05-20T16:42:22.936Z\"}, \"d066_sweep_llama_docred_beam4_unc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T13:22:24.187Z\", \"updated_at\": \"2026-05-20T16:41:02.850Z\", \"hypothesis\": \"d066 DocRED beam sweep sub-task: Llama beam4 unconstrained on 200-doc subset (westd-16980 GPU1). Part of d066_beam_sweep. DocRED data needed for Pareto dual-panel figure.\", \"parent\": \"d066_beam_sweep\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode unconstrained --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --decoding_strategy beam --num_beams 4 --max_new_tokens 4096 --max_samples 200 --seed 42 --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path /root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_200_beam4_unconstrained.jsonl\", \"server\": \"westd-16980 GPU1\", \"data_path\": \"data/docred/dev.json (200-doc subset)\", \"data_count\": 200, \"model_name\": \"Llama-3.1-8B LoRA DocRED (merged)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json (200-doc subset)\", \"note\": \"PID 761033. Relay from Llama beam8 unc (success).\"}, \"checkpoint_path\": \"/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_beam4_unc.jsonl\", \"log_path\": \"/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_beam4_unc.log\", \"metrics\": {\"E-F1\": 85.67, \"R-F1\": 52.65, \"DR_pct\": 0.04, \"CF_pct\": 0.08, \"PF_pct\": 0.5, \"samples\": 200}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T16:41:02.851Z\"}, \"d066_sweep_llama_docred_beam1_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T13:18:07.824Z\", \"updated_at\": \"2026-05-20T16:41:01.414Z\", \"hypothesis\": \"d066 DocRED beam sweep sub-task: Llama beam1 (greedy) constrained (full_s1) on 200-doc subset (westd-21461 GPU1). Part of d066_beam_sweep. DocRED data needed for Pareto dual-panel figure.\", \"parent\": \"d066_beam_sweep\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --decoding_strategy beam --num_beams 1 --max_new_tokens 4096 --max_samples 200 --seed 42 --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json\", \"server\": \"westd-21461 GPU1\", \"data_path\": \"data/docred/dev.json (200-doc subset)\", \"data_count\": 200, \"model_name\": \"Llama-3.1-8B LoRA DocRED (merged)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json (200-doc subset)\", \"note\": \"PID 209444. Relay from beam1 unc (success).\"}, \"checkpoint_path\": \"/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_beam1_full_s1.jsonl\", \"log_path\": \"/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_beam1_s1.log\", \"metrics\": {\"E-F1\": 85.43, \"R-F1\": 47.35, \"DR_pct\": 0, \"CF_pct\": 0.19, \"PF_pct\": 2, \"samples\": 200}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T16:41:01.414Z\"}, \"d066_sweep_llama_beam8_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T12:17:06.965Z\", \"updated_at\": \"2026-05-20T16:40:59.767Z\", \"hypothesis\": \"d066 DocRED beam sweep sub-task: Llama beam8 constrained (full_s1) on 200-doc subset (westd-16980 GPU0). Part of d066_beam_sweep parent experiment.\", \"parent\": \"d066_beam_sweep\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --decoding_strategy beam --num_beams 8 --max_new_tokens 4096 --max_samples 200 --seed 42 --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json\", \"server\": \"westd-16980 GPU0\", \"data_path\": \"data/docred/dev.json (200-doc subset)\", \"data_count\": 200, \"model_name\": \"Llama-3.1-8B LoRA DocRED (merged)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json (200-doc subset)\", \"note\": \"PID 756540. Relay after GPU0 freed.\"}, \"checkpoint_path\": \"/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_beam8_full_s1.jsonl\", \"log_path\": \"/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_beam8_s1.log\", \"metrics\": {\"E-F1\": 85.76, \"R-F1\": 51.74, \"DR_pct\": 0, \"CF_pct\": 0, \"PF_pct\": 0.5, \"samples\": 200}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T16:40:59.767Z\"}, \"d065_qwen_greedy_4096_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:58:53.058Z\", \"updated_at\": \"2026-05-20T16:40:58.219Z\", \"hypothesis\": \"Qwen3-8B LoRA on full DocRED dev (998 docs) with greedy 4096 tokens will show comparable DR elimination under constrained decoding as seen in SciERC, confirming schema-semantic constraints generalize to high-cardinality relation extraction (96 types). Rerun after dual-process data corruption.\", \"parent\": \"d065_qwen_greedy_4096\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 nohup python3 run_constrained_extraction.py --mode full_s1 --dataset docred --decoding_strategy greedy --max_new_tokens 4096 --model_path /root/autodl-tmp/checkpoints/qwen_lora_docred_merged --output_file /root/autodl-tmp/schema_outputs/d065_qwen_docred_greedy_con_4096_rerun.jsonl --seed 42\", \"server\": \"westd-21461 GPU0\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"Qwen3-8B LoRA DocRED (merged)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json (998 docs, constrained decoding inference)\", \"note\": \"Rerun after dual-process corruption. PID 194615.\"}, \"checkpoint_path\": \"/root/autodl-tmp/schema_outputs/d065_qwen_greedy_con_r2.jsonl\", \"log_path\": \"/root/autodl-tmp/schema_outputs/d065_qwen_greedy_con_r2.log\", \"metrics\": {\"E-F1\": 81.87, \"R-F1\": 40.79, \"DR_pct\": 0, \"CF_pct\": 0.22, \"ET_pct\": 0, \"RV_pct\": 0, \"PF_pct\": 8.52, \"samples\": 998}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T16:40:58.219Z\"}, \"d066_sweep_llama_scierc_beam2_s1_551\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T15:04:53.443Z\", \"updated_at\": \"2026-05-20T16:37:54.940Z\", \"hypothesis\": \"d066 SciERC beam sweep: Llama beam2 constrained (full_s1) on 551-sentence test set.\", \"parent\": \"d066_beam_sweep\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/checkpoints/llama_lora_scierc_merged --decoding_strategy beam --num_beams 2 --max_new_tokens 4096 --seed 42 --data_path data/processed_data/test.json --output_path /root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_551_beam2_full_s1.jsonl\", \"server\": \"westd-16980\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"llama_lora_scierc_merged\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_scierc_merged\", \"eval_data\": \"scierc test set (551 sentences)\"}, \"conclusion\": \"success\", \"metrics\": {\"entity_f1\": 68.34, \"entity_p\": 66.59, \"entity_r\": 70.17, \"relation_f1\": 46.12, \"relation_p\": 42.73, \"relation_r\": 50.1, \"parse_fail_pct\": 0, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0.17, \"note\": \"ET/RV corrected from 100→0: original eval used hardcoded DocRED ontology, re-evaled with --dataset scierc\"}, \"checkpoint_path\": \"/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_551_beam2_full_s1.jsonl\", \"log_path\": \"/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_beam2_s1_551.log\", \"completed_at\": \"2026-05-20T15:37:46.989Z\"}, \"d066_sweep_llama_scierc_beam1_unc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T12:13:08.565Z\", \"updated_at\": \"2026-05-20T13:52:26.684Z\", \"hypothesis\": \"d066 SciERC beam sweep sub-task: Llama beam1 (greedy) unconstrained on 551-doc full set (westd-21461 GPU1). Part of d066_beam_sweep. Extends Qwen-only SciERC sweep to Llama model family.\", \"parent\": \"d066_beam_sweep\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode unconstrained --dataset scierc --model_path /root/autodl-tmp/checkpoints/llama_lora_scierc_merged --decoding_strategy beam --num_beams 1 --max_new_tokens 4096 --seed 42\", \"server\": \"westd-21461 GPU1\", \"data_path\": \"data/scierc/test.json (551 docs)\", \"data_count\": 551, \"model_name\": \"Llama-3.1-8B LoRA SciERC (merged)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_scierc_merged\", \"eval_data\": \"data/scierc/test.json\", \"note\": \"PID 205314. Relay from Qwen beam8 s1 SciERC (success).\", \"checkpoint_path\": \"westd-21461:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_beam1_unconstrained.jsonl\", \"log_path\": \"westd-21461:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_beam1_unc.log\"}, \"conclusion\": \"failed\", \"metrics\": {\"total\": 275, \"success\": 275, \"fail\": 0, \"output_file\": \"llama_scierc_beam1_unconstrained.jsonl\", \"note\": \"INVALIDATED: Used dev set (275 docs) instead of test set (551 docs). Not comparable with other beam sweep results. Llama SciERC beam sweep deprioritized — must use scripts/d066_beam_sweep_scierc.sh with --data_path data/processed_data/test.json if rerun.\"}, \"completed_at\": \"2026-05-20T12:27:51.420Z\"}, \"d066_sweep_llama_docred_beam1_unc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T12:27:58.317Z\", \"updated_at\": \"2026-05-20T13:18:06.388Z\", \"hypothesis\": \"d066 DocRED beam sweep sub-task: Llama beam1 (greedy) unconstrained on 200-doc subset (westd-21461 GPU1). Part of d066_beam_sweep. DocRED data needed for Pareto dual-panel figure.\", \"parent\": \"d066_beam_sweep\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode unconstrained --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --decoding_strategy beam --num_beams 1 --max_new_tokens 4096 --max_samples 200 --seed 42 --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json\", \"server\": \"westd-21461 GPU1\", \"data_path\": \"data/docred/dev.json (200-doc subset)\", \"data_count\": 200, \"model_name\": \"Llama-3.1-8B LoRA DocRED (merged)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json (200-doc subset)\", \"note\": \"PID 206397. Relay from Llama SciERC beam1 unc. DocRED priority per Director.\", \"checkpoint_path\": \"westd-21461:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_200_beam1_unconstrained.jsonl\", \"log_path\": \"westd-21461:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_beam1_unc.log\"}, \"conclusion\": \"success\", \"metrics\": {\"total\": 200, \"success\": 196, \"fail\": 4, \"output_file\": \"llama_docred_200_beam1_unconstrained.jsonl\"}, \"completed_at\": \"2026-05-20T13:18:06.388Z\"}, \"d066_sweep_21461_gpu1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:01:12.415Z\", \"updated_at\": \"2026-05-20T12:13:00.737Z\", \"hypothesis\": \"d066 DocRED beam sweep sub-task: Qwen beam8 constrained (full_s1) on 200-doc subset (westd-21461 GPU1). Part of d066_beam_sweep parent experiment.\", \"parent\": \"d066_beam_sweep\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 nohup python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path qwen_lora_docred_merged --decoding_strategy beam --num_beams 8 --max_docs 200\", \"server\": \"westd-21461 GPU1\", \"data_path\": \"data/docred/dev.json (200-doc subset)\", \"data_count\": 200, \"model_name\": \"Qwen3-8B LoRA DocRED (merged)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json (200-doc subset)\", \"checkpoint_path\": \"westd-21461:/root/autodl-tmp/schema_outputs/d066_beam_sweep/qwen_scierc_beam8_full_s1.jsonl\", \"log_path\": \"westd-21461:/root/autodl-tmp/schema_outputs/d066_beam_sweep/d066_qwen_beam8_s1_21461.log\"}, \"conclusion\": \"success\", \"metrics\": {\"total\": 551, \"E_F1\": 66.36, \"R_F1\": 43.65, \"DR_pct\": 0, \"CF_pct\": 0, \"ET_pct\": 0, \"RV_pct\": 0, \"avg_time_s\": 5.058, \"output_file\": \"qwen_scierc_beam8_full_s1.jsonl\", \"note\": \"Actually ran on SciERC 551 docs (not DocRED 200 as originally recorded in hypothesis)\"}, \"completed_at\": \"2026-05-20T12:13:00.737Z\"}, \"w5_llama_docred_lora_constrained_eval\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-15T19:58:10.837Z\", \"updated_at\": \"2026-05-20T11:59:24.791Z\", \"hypothesis\": \"Fine-tuned Llama-3.1-8B DocRED LoRA + OntoCoDec constrained eval — 验证 composability：约束解码在 fine-tuned Llama DocRED 上是否仍能消除残余 DR 且不损 R-F1\", \"parent\": \"w5_llama_docred_lora_training\", \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-16T00:22:01.892Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w5_llama_docred_lora_constrained_eval.jsonl --batch_size 1 --max_new_tokens 4096\\\"\", \"finished_at\": \"2026-05-16T04:51:37.138Z\", \"training_hours\": 4.49}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"completed_at\": \"2026-05-16T00:26:15.420Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T00:26:16.832346+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T04:51:38.893721+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w5_llama_docred_lora_constrained_eval.jsonl --batch_size 1 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"gpu\": 0, \"pid\": 317464, \"log_path\": \"~/runs/schema_semantic_constrained_ie/w5_llama_docred_lora_constrained_eval.log\", \"model_name\": \"llama_lora_docred_merged\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json\", \"checkpoint_path\": \"N/A\"}, \"notes\": \"重提交后 PID 317464 (wrapper) / 317469 (GPU subprocess) 在 cuda:0 正常运行。EXIT_CODE=143 来自 wrapper 层误报，非推理进程故障。Grammar 编译 96 relation types 耗时 ~9min（长初始化触发 wrapper 超时报警）。11/998 at ~14s/sample, ETA ~3.8h。脚本支持 --resume，如被 kill 可恢复。\", \"metrics\": {\"total\": 998, \"parse_failures\": 25, \"parse_fail_rate\": 2.51, \"entities\": 19077, \"relations\": 16074, \"entity_f1\": 83.94, \"entity_precision\": 85, \"entity_recall\": 84.13, \"relation_f1_all_set\": 43.78, \"relation_precision_all_set\": 38.79, \"relation_recall_all_set\": 50.81, \"et_violations\": 0, \"et_violation_rate\": 0, \"rv_violations\": 0, \"rv_violation_rate\": 0, \"dr_violations\": 33, \"dr_violation_rate\": 0.21, \"CF_pct\": 0.21, \"delta_vs_unconstrained\": {\"delta_e_f1\": 0.01, \"delta_r_f1\": 0.06, \"delta_dr\": -0.28, \"note\": \"Authoritative values from eval_d064.py on w5_llama_docred_lora_constrained_eval.jsonl (998 lines). Updated 2026-05-20.\"}, \"provenance\": \"eval_d064.py on westd-16980:/root/schema_semantic_constrained_ie/outputs/w5_llama_docred_lora_constrained_eval.jsonl, 2026-05-20. P/R corrected 2026-05-20 per Director.\"}, \"conclusion\": \"success\"}, \"d066_sweep_16980_gpu1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:01:11.031Z\", \"updated_at\": \"2026-05-20T11:23:11.984Z\", \"hypothesis\": \"d066 DocRED beam sweep sub-task: Llama beam2 unconstrained on 200-doc subset (westd-16980 GPU1). Part of d066_beam_sweep parent experiment.\", \"parent\": \"d066_beam_sweep\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 nohup python3 run_constrained_extraction.py --mode unconstrained --dataset docred --model_path llama_lora_docred_merged --decoding_strategy beam --num_beams 2 --max_docs 200\", \"server\": \"westd-16980 GPU1\", \"data_path\": \"data/docred/dev.json (200-doc subset)\", \"data_count\": 200, \"model_name\": \"Llama-3.1-8B LoRA DocRED (merged)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json (200-doc subset)\"}, \"reproduce\": {\"finished_at\": \"2026-05-20T11:21:34.505Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T11:21:35.106Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T11:21:41.240328+00:00\"}]}, \"notes\": \"Cron 误判：进程正常完成（200/200 samples, success=198, fail=2），但因无 W&B metrics 被 auto-resolved as failed。日志确认完整完成。输出: llama_docred_200_beam2_unconstrained.jsonl。待 eval 获取 metrics。\"}, \"d066_beam_sweep\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T23:44:23.637Z\", \"updated_at\": \"2026-05-20T10:59:13.956Z\", \"hypothesis\": \"Beam width k∈{1,2,4,8} on SciERC (LoRA, Qwen3-8B) will show monotonic DR/CF reduction with diminishing returns past k=4, establishing the cost-effectiveness trade-off for the beam search appendix Pareto analysis.\", \"spec\": {\"command\": \"d066 DocRED beam sweep (k=1,2,4,8 x unc/s1 x Qwen/Llama, 200 docs each)\", \"server\": \"westd-16980 + westd-21461\", \"data_path\": \"data/docred/dev.json (200-doc subset)\", \"data_count\": 200, \"model_name\": \"Qwen3-8B + Llama-3.1-8B LoRA DocRED (merged)\", \"seed\": 42, \"note\": \"ANALYZING->RUNNING transition blocked. Actual status: DocRED sweep actively running on both servers. SciERC sweep complete.\"}, \"notes\": \"全部 8 配置完成 + eval 齐全。beam8 con: E-F1=66.36, R-F1=43.65, DR=0%, CF=0%, avg_time=5.058s。Pareto optimal: k=2 con (E-F1=67.71, R-F1=44.60, DR=0%)。k=8 相比 k=2 F1 下降 ~1.3pp 且推理慢 46%，收益递减明确。可入稿。\", \"metrics\": {\"scierc_qwen3_8b\": {\"k1_unc\": {\"E_F1\": 66.88, \"R_F1\": 42.95, \"DR_pct\": 2.11, \"CF_pct\": 0, \"avg_time\": 2.494}, \"k1_con\": {\"E_F1\": 66.88, \"R_F1\": 42.95, \"DR_pct\": 0, \"CF_pct\": 0.5, \"avg_time\": 2.932}, \"k2_unc\": {\"E_F1\": 67.79, \"R_F1\": 44.75, \"DR_pct\": 1.54, \"CF_pct\": 0, \"avg_time\": 2.954}, \"k2_con\": {\"E_F1\": 67.71, \"R_F1\": 44.6, \"DR_pct\": 0, \"CF_pct\": 0.11, \"avg_time\": 3.463}, \"k4_unc\": {\"E_F1\": 67.49, \"R_F1\": 43.72, \"DR_pct\": 1.89, \"CF_pct\": 0, \"avg_time\": 3.485}, \"k4_con\": {\"E_F1\": 67.22, \"R_F1\": 43.6, \"DR_pct\": 0, \"CF_pct\": 0, \"avg_time\": 4.069}, \"k8_unc\": {\"E_F1\": 66.4, \"R_F1\": 43.17, \"DR_pct\": 1.77, \"CF_pct\": 0, \"avg_time\": 4.194}, \"k8_con\": {\"E_F1\": 66.36, \"R_F1\": 43.65, \"DR_pct\": 0, \"CF_pct\": 0, \"avg_time\": 5.058}}, \"pareto_optimal\": \"k=2 con\", \"best_E_F1\": {\"config\": \"k=2 unc\", \"value\": 67.79}, \"best_R_F1\": {\"config\": \"k=2 unc\", \"value\": 44.75}}}, \"d065_qwen_greedy_4096\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T03:15:26.700Z\", \"updated_at\": \"2026-05-20T08:24:26.139Z\", \"hypothesis\": \"Qwen3-8B LoRA on full DocRED dev (998 docs) with greedy 4096 tokens will show comparable DR elimination under constrained decoding as seen in SciERC, confirming schema-semantic constraints generalize to high-cardinality relation extraction (96 types).\", \"spec\": {\"command\": \"bash scripts/d065_qwen_greedy_4096_21461.sh (unc then con, sequential)\", \"server\": \"westd-21461 GPU0\", \"data_path\": \"data/docred/dev.json (998 docs)\", \"data_count\": 998, \"model_name\": \"Qwen3-8B LoRA DocRED (merged)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen_lora_docred_merged\", \"checkpoint_path\": \"westd-21461:/root/autodl-tmp/schema_outputs/d065_qwen_docred_greedy_*_4096.jsonl\", \"log_path\": \"westd-21461:/root/autodl-tmp/schema_outputs/d065_qwen_greedy_4096.log\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-20T03:24:19.389Z\", \"notes\": \"Llama 4096 eval 完成。unc: E-F1=84.77, R-F1=44.55, DR=0.49%, CF=0.08%; con: E-F1=84.71, R-F1=44.70, DR=0.00%, CF=0.26%。vs w5: E-F1 +1.3pp (PF% 从 ~5%→~2.5%), R-F1 持平。Qwen 仍在跑: unc 887/998 ETA ~09:00, con 707/998 ETA ~10:10。\"}, \"d066_docred_beam_sweep\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T02:42:56.730Z\", \"updated_at\": \"2026-05-20T03:02:27.736Z\", \"hypothesis\": \"DocRED beam width sweep (k=2,8) on Qwen LoRA 200-doc subset will show the same Pareto pattern as SciERC — k=2 as sweet spot with diminishing returns at k=8 — confirming the beam width recommendation generalizes across datasets with different schema complexity (DocRED: 96 relation types vs SciERC: 7).\", \"spec\": {\"command\": \"python run_constrained_extraction.py --dataset docred --decoding_strategy beam --num_beams {2,8} --mode {unconstrained,full_s1} (4 runs serial)\", \"server\": \"westd-21461 GPU0\", \"data_path\": \"data/docred/dev.json (200-doc subset)\", \"data_count\": 200, \"model_name\": \"Qwen3-8B LoRA DocRED (merged)\", \"seed\": 42, \"claim\": \"Claim 3 + deployment guidance\", \"paper_usage\": \"DocRED Pareto curve in appendix\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-20T03:02:27.736Z\"}, \"d067_seed_variance\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T23:44:45.500Z\", \"updated_at\": \"2026-05-20T02:42:31.802Z\", \"hypothesis\": \"Varying random seed (42,123,456) across models (Qwen,Llama) and datasets (SciERC,DocRED) under constrained vs unconstrained decoding will show low F1 variance (σ<1pp), confirming that reported improvements from constraint decoding are robust and not seed-dependent.\", \"spec\": {\"command\": \"bash scripts/d067_run_all.sh (3 configs × 2 seeds × unc/con, 12 runs serial)\", \"server\": \"westd-21461 GPU0\", \"data_path\": \"data/processed_data/test.json (SciERC) + data/docred/dev.json (DocRED)\", \"data_count\": 551, \"model_name\": \"Qwen3-8B LoRA SciERC + Llama-3.1-8B LoRA SciERC + Qwen3-8B LoRA DocRED\", \"seed\": \"123, 456\", \"checkpoint_path\": \"westd-21461:/root/autodl-tmp/schema_outputs/d067_*\", \"log_path\": \"westd-21461:/root/autodl-tmp/schema_outputs/d067_run_all.log\"}, \"metrics\": {\"qwen_scierc_unc\": {\"E_F1\": \"66.94 ± 0.08\", \"R_F1\": \"43.25 ± 0.43\", \"DR\": \"2.06 ± 0.08\", \"CF\": \"0.00 ± 0.00\"}, \"qwen_scierc_con\": {\"E_F1\": \"66.94 ± 0.08\", \"R_F1\": \"43.22 ± 0.39\", \"DR\": \"0.00 ± 0.00\", \"CF\": \"0.48 ± 0.02\"}, \"llama_scierc_unc\": {\"E_F1\": \"67.99 ± 0.16\", \"R_F1\": \"45.38 ± 0.05\", \"DR\": \"1.04 ± 0.05\", \"CF\": \"0.00 ± 0.00\"}, \"llama_scierc_con\": {\"E_F1\": \"67.99 ± 0.16\", \"R_F1\": \"45.40 ± 0.05\", \"DR\": \"0.03 ± 0.04\", \"CF\": \"0.26 ± 0.02\"}, \"max_sigma_pp\": 0.43, \"greedy_deterministic\": true, \"snr_dr_improvement\": \">12x\", \"qwen_docred_status\": \"pending (not started)\", \"llama_scierc_seed456_con_status\": \"running (407/551)\"}, \"conclusion\": \"success\", \"notes\": \"Greedy decoding is deterministic; constraint effects (DR↓2pp) have SNR > 12× vs hardware variance (σ < 0.5pp). Seeds 123/456 produce byte-identical outputs on same hardware. Cross-server float noise is the only variance source. All σ < 0.5pp. DocRED Qwen not run (greedy determinism confirmed, not worth GPU). Error bars strategy: no error bars, appendix note greedy determinism.\", \"completed_at\": \"2026-05-20T02:42:31.802Z\"}, \"d068_constraint_guided_beam_pilot\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T16:38:01.430Z\", \"updated_at\": \"2026-05-19T16:49:55.045Z\", \"hypothesis\": \"Constraint-guided beam scoring (score = logP - β×violations) reduces CF without degrading DR/F1, by penalizing beams with more constraint violations during search\", \"spec\": {\"command\": \"python run_constrained_extraction.py --constraint_penalty {0.0,0.5,1.0,2.0} --decoding_strategy beam --num_beams 4 --constraint_mode full_s1\", \"server\": \"westd-16980 + westd-21461\", \"data_path\": \"data/processed_data/test.json (SciERC 551 samples)\", \"data_count\": 551, \"model_name\": \"Qwen3-8B LoRA SciERC (qwen3_8b_lora_scierc_merged)\", \"seed\": 42, \"parameters\": {\"beta\": [0, 0.5, 1, 2], \"beam\": 4, \"mode\": \"full_s1\"}, \"claim\": \"Claim 3 + method enhancement\", \"code_location\": \"run_constrained_extraction.py:746-808 run_single_pass_beam()\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged\", \"log_path\": \"outputs/d068_guided_beam/ on both servers\", \"partial_result\": \"all violations 0% at ~20% completion - penalty has no effect on LoRA model\", \"negative_reason\": \"LoRA model beam candidates already 0% violations; penalty term always 0; F1 drops 0.3-5.3pp due to multi-sequence decoding noise. Director decided No-Go, killed at ~20% completion.\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-19T16:49:55.045Z\"}, \"d064_docred_full_beam\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T09:03:41.626Z\", \"updated_at\": \"2026-05-19T14:40:11.790Z\", \"hypothesis\": \"Expanding DocRED beam search (k=4, LoRA+S1) from 50-doc subset to full 998-doc dev set will maintain zero violations (DR=0, RV=0, ET=0) while narrowing the confidence interval upper bound from 5.8% to ~0.3%, strengthening the zero-violation claim for the paper.\", \"spec\": {\"actual_status\": \"STILL RUNNING - startup recovery falsely marked DONE/failed\", \"status_override\": \"2026-05-19T14:40 UTC: Director confirmed processes still running on both servers. d064 will be re-registered as success when all 6 runs complete.\", \"servers\": {\"westd-21461\": \"Qwen beam-4 unc/con + Llama greedy unc/con (cascade)\", \"westd-16980\": \"Llama beam-4 unc + con (Option C: will add Llama greedy unc/con after beam)\"}, \"checkpoint_policy\": \"All Llama results use w5 checkpoint (16980). 21461 Llama greedy (d064 checkpoint) kept as internal reference only.\", \"command\": \"cascade inference scripts on both servers\", \"server\": \"westd-21461 + westd-16980\", \"data_path\": \"/root/autodl-tmp/OntoCoDec/data/docred/\", \"data_count\": 998, \"model_name\": \"Qwen-2.5-7B-Instruct + Llama-3.1-8B-Instruct (LoRA)\", \"seed\": 42}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-19T12:44:24.620Z\"}, \"d065_tcr_full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T11:43:23.631Z\", \"updated_at\": \"2026-05-19T11:44:17.092Z\", \"hypothesis\": \"TCR's CF elimination generalizes across datasets (DocRED 96 rels, Mistral, 70B) and fine-tuning settings, but effectiveness is inversely correlated with mean schema constraint tightness (κ̄): higher κ̄ (more restrictive schemas like DocRED) produces more fundamental conflicts where no single entity type satisfies all relational contexts, causing DR to increase when CF is forcibly resolved.\", \"parent\": \"d065_tcr_pilot\", \"conclusion\": \"success\", \"metrics\": {\"configs_tested\": 10, \"all_cf_eliminated\": true, \"scierc_all_dr_delta_max\": 0.28, \"docred_lora_dr_delta_max\": 0.14, \"docred_zs_llama_dr_delta\": 9.38, \"docred_zs_70b_dr_delta\": 4.2, \"docred_zs_qwen_dr_delta\": 1.53, \"fund_conflict_scierc_max\": 2.04, \"fund_conflict_docred_zs_max\": 22.78, \"fund_conflict_docred_lora_max\": 12.16, \"lora_ef1_cost_max\": 0.0075, \"zs_docred_ef1_cost_max\": 0.0598}, \"checkpoint_path\": \"outputs/tcr/\", \"log_path\": \"d065_tcr_full_results.md\", \"completed_at\": \"2026-05-19T11:44:17.092Z\"}, \"d065_tcr_pilot\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T11:26:25.109Z\", \"updated_at\": \"2026-05-19T11:41:36.624Z\", \"hypothesis\": \"Post-hoc Type Consistency Resolution (TCR) can reduce CF violations by ≥30% in zero-shot and ≥50% in LoRA settings without increasing DR, by resolving cross-triple entity type conflicts using global relation constraint satisfaction scoring. During-decoding consensus failed (100% skip rate) due to lack of global information; post-hoc TCR has full document context and should succeed where per-token approaches cannot.\", \"conclusion\": \"success\", \"metrics\": {\"scierc_zs_qwen\": {\"cf_before\": 9.75, \"cf_after\": 0, \"dr_before\": 0.93, \"dr_after\": 1.21, \"ef1_delta\": -0.0129, \"fund_pct\": 2.04}, \"scierc_zs_llama\": {\"cf_before\": 6.4, \"cf_after\": 0, \"dr_before\": 0.08, \"dr_after\": 0.3, \"ef1_delta\": -0.0178, \"fund_pct\": 1.85}, \"scierc_lora_qwen\": {\"cf_before\": 1.19, \"cf_after\": 0, \"dr_before\": 0, \"dr_after\": 0, \"ef1_delta\": -0.0075, \"fund_pct\": 0}, \"scierc_lora_llama\": {\"cf_before\": 0.46, \"cf_after\": 0, \"dr_before\": 0.09, \"dr_after\": 0.09, \"ef1_delta\": -0.0018, \"fund_pct\": 0}, \"scierc_zs_mistral\": {\"cf_before\": 0.67, \"cf_after\": 0, \"dr_before\": 13.36, \"dr_after\": 12.87, \"ef1_delta\": 0.0005, \"fund_pct\": 0}, \"docred_zs_qwen\": {\"cf_before\": 13.11, \"cf_after\": 0, \"dr_before\": 10.21, \"dr_after\": 11.74, \"ef1_delta\": -0.0344, \"fund_pct\": 13.52}, \"docred_zs_llama\": {\"cf_before\": 23.71, \"cf_after\": 0, \"dr_before\": 2.55, \"dr_after\": 11.93, \"ef1_delta\": -0.0521, \"fund_pct\": 22.78}, \"docred_zs_70b\": {\"cf_before\": 11.61, \"cf_after\": 0, \"dr_before\": 0, \"dr_after\": 4.2, \"ef1_delta\": -0.0598, \"fund_pct\": 18.26}, \"docred_lora_qwen\": {\"cf_before\": 0.42, \"cf_after\": 0, \"dr_before\": 0.01, \"dr_after\": 0.14, \"ef1_delta\": -0.0016, \"fund_pct\": 12.16}, \"docred_lora_llama\": {\"cf_before\": 0.36, \"cf_after\": 0, \"dr_before\": 0.21, \"dr_after\": 0.2, \"ef1_delta\": -0.0017, \"fund_pct\": 11.59}, \"total_configs\": 10, \"all_cf_eliminated\": true}, \"checkpoint_path\": \"outputs/tcr/\", \"log_path\": \"scripts/tcr_resolver.py\", \"completed_at\": \"2026-05-19T11:32:42.343Z\"}, \"d063_gollie_violation_rate\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T09:03:40.297Z\", \"updated_at\": \"2026-05-19T10:13:00.612Z\", \"hypothesis\": \"GoLLIE's code-generation IE approach (dataclass instantiation with type annotations) will still produce schema violations (DR/RV/ET) because its type annotations are soft hints in the prompt, not hard token-level constraints during decoding. This demonstrates OntoCoDec's complementary value even for schema-aware IE systems.\", \"conclusion\": \"success\", \"metrics\": {\"gollie_DR\": 0, \"gollie_RV\": 0, \"gollie_ET\": 0, \"gollie_CF\": 0.67, \"gollie_entities\": 300, \"gollie_relations\": 7, \"gollie_empty_docs_pct\": 45, \"docs_tested\": 100}, \"checkpoint_path\": \"outputs/gollie_scierc/violation_results.json\", \"log_path\": \"outputs/gollie_scierc/raw_outputs.jsonl\", \"completed_at\": \"2026-05-19T10:13:00.612Z\"}, \"d062_full_ft_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T03:15:32.642Z\", \"updated_at\": \"2026-05-19T05:11:24.604Z\", \"hypothesis\": \"Full fine-tuning Qwen3-8B on SciERC (all parameters, not just LoRA adapters) will yield higher extraction F1 than LoRA FT, and the unconstrained model will still produce schema violations (DR > 0%), confirming OntoCoDec constraints remain necessary even with stronger fine-tuning.\", \"spec\": {\"command\": \"bash scripts/run_d062_full_ft_scierc.sh\", \"server\": \"westd-21461\", \"gpu\": \"cuda:0\", \"data_path\": \"data/sft/scierc_sft_train.jsonl\", \"data_count\": 1762, \"model_name\": \"Qwen3-8B (full fine-tuning)\", \"seed\": 42, \"training_method\": \"full_fine_tuning\", \"hyperparams\": {\"lr\": \"2e-4\", \"epochs\": 3, \"batch_size\": 16, \"gradient_checkpointing\": true, \"bf16\": true, \"warmup_ratio\": 0.1, \"optimizer\": \"AdamW\", \"schedule\": \"cosine\"}}, \"reproduce\": {\"finished_at\": \"2026-05-19T04:50:16.081Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-19T04:50:14.990Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T04:50:21.524569+00:00\"}]}, \"metrics\": {\"unconstrained\": {\"entity_f1\": 0.6478, \"relation_f1\": 0.3789, \"DR_pct\": 2.74, \"RV_pct\": 0.18, \"ET_pct\": 0, \"CF_pct\": 0}, \"constrained\": {\"entity_f1\": 0.6478, \"relation_f1\": 0.3789, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 1.31}, \"training\": {\"eval_loss_final\": 0.09459, \"epochs\": 3, \"total_steps\": 333, \"training_time\": \"21m49s\"}}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/qwen_full_ft_scierc/\", \"log_path\": \"/root/autodl-tmp/d062_full_ft_scierc.log\"}, \"d062_beam_latency\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T03:15:35.458Z\", \"updated_at\": \"2026-05-19T04:30:54.166Z\", \"hypothesis\": \"Beam search (k=4) with constrained decoding will have higher latency overhead relative to greedy than unconstrained beam search, because the constraint processor must independently track and validate grammar/semantic state for each of the 4 beams at every decoding step.\", \"spec\": {\"command\": \"bash scripts/run_d062_beam_latency.sh\", \"server\": \"westd-21461\", \"gpu\": \"cuda:1\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B LoRA FT (SciERC merged)\", \"seed\": 42}, \"conclusion\": \"success\", \"checkpoint_path\": \"n/a\", \"log_path\": \"/root/autodl-tmp/schema_outputs/d062_beam_latency.log\", \"completed_at\": \"2026-05-19T04:30:49.036Z\", \"metrics\": {\"beam4_unconstrained_s_per_doc\": 3.446, \"beam4_constrained_s_per_doc\": 4.013, \"beam4_unconstrained_total_s\": 1898.7, \"beam4_constrained_total_s\": 2211, \"beam_greedy_ratio_unconstrained\": 1.319, \"beam_greedy_ratio_constrained\": 1.397, \"constraint_overhead_beam\": 1.165, \"constraint_overhead_greedy\": 1.1, \"greedy_unconstrained_s_per_doc\": 2.612, \"greedy_constrained_s_per_doc\": 2.873}}, \"d062_ontology_scalability\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T04:10:38.904Z\", \"updated_at\": \"2026-05-19T04:28:16.233Z\", \"hypothesis\": \"OntoCoDec's grammar compilation and per-token constraint overhead scale sub-linearly with ontology size (relations and entity types), because the prefix map grows linearly with entity type count but per-token masking only checks the active prefix path, not all types. Compile time may scale super-linearly due to CFG complexity, but inference overhead should remain bounded.\", \"spec\": {\"command\": \"python3 scripts/ontology_scalability_benchmark.py\", \"server\": \"westd-16980\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/\", \"data_count\": 40, \"model_name\": \"Qwen3-8B\", \"seed\": 42}, \"conclusion\": \"success\", \"metrics\": {\"compile_small_total_s\": 0.334, \"compile_medium_total_s\": 0.322, \"compile_large_total_s\": 0.345, \"compile_xlarge_total_s\": 0.42, \"grammar_small_s\": 0.333, \"grammar_xlarge_s\": 0.365, \"semantic_small_s\": 0.0004, \"semantic_xlarge_s\": 0.017, \"overhead_small\": 1.02, \"overhead_medium\": 1.03, \"overhead_large\": 1.03, \"overhead_xlarge\": 1.03, \"failures\": 0}, \"log_path\": \"/root/autodl-tmp/d062_benchmark.log\", \"checkpoint_path\": \"n/a\", \"completed_at\": \"2026-05-19T04:28:16.233Z\"}, \"d062_cf_majority_voting\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T03:15:34.085Z\", \"updated_at\": \"2026-05-19T03:23:41.243Z\", \"hypothesis\": \"Majority voting over entity types within each document can reduce CF violations without significantly increasing DR violations, because the most frequent type assignment for each entity is likely the ontology-consistent one.\", \"spec\": {\"command\": \"python3 scripts/cf_majority_voting.py\", \"server\": \"westd-16980\", \"data_path\": \"/root/schema_semantic_constrained_ie/outputs/\", \"data_count\": 8, \"model_name\": \"n/a (post-hoc)\", \"seed\": 0, \"checkpoint_source\": \"n/a\", \"checkpoint_path\": \"n/a\", \"log_path\": \"outputs/cf_correction_report_*.json\"}, \"metrics\": {\"qwen_scierc_zs\": {\"cf_before\": 245, \"cf_after\": 201, \"dr_rate_before\": 0.0093, \"dr_rate_after\": 0.0324}, \"llama_scierc_zs\": {\"cf_before\": 162, \"cf_after\": 123, \"dr_rate_before\": 0.0008, \"dr_rate_after\": 0.0236}, \"qwen_docred_zs\": {\"cf_before\": 518, \"cf_after\": 21, \"dr_rate_before\": 0.1021, \"dr_rate_after\": 0.1466}, \"llama_docred_zs\": {\"cf_before\": 1358, \"cf_after\": 107, \"dr_rate_before\": 0.0255, \"dr_rate_after\": 0.1665}, \"qwen_scierc_ft\": {\"cf_before\": 21, \"cf_after\": 12, \"dr_rate_before\": 0, \"dr_rate_after\": 0.0071}, \"llama_scierc_ft\": {\"cf_before\": 8, \"cf_after\": 4, \"dr_rate_before\": 0.0009, \"dr_rate_after\": 0.0037}, \"qwen_docred_ft\": {\"cf_before\": 48, \"cf_after\": 3, \"dr_rate_before\": 0.0001, \"dr_rate_after\": 0.0044}, \"llama_docred_ft\": {\"cf_before\": 41, \"cf_after\": 2, \"dr_rate_before\": 0.0021, \"dr_rate_after\": 0.005}}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-19T03:23:41.243Z\"}, \"p1_ee_ft_llama_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T23:28:30.109Z\", \"updated_at\": \"2026-05-19T00:06:31.547Z\", \"hypothesis\": \"After fixing schema mismatch (entities not required in EE JSON schema) and adding repetition_penalty=1.2, Llama-3.1-8B FT on WikiEvents EE will produce parseable constrained output with RoV/AC violations eliminated, validating dual-model composability on event extraction.\", \"parent\": \"p1_ee_ft_llama\", \"metrics\": {\"parse_rate_unconstrained\": 1, \"parse_rate_constrained\": 1, \"trigger_f1_unconstrained\": 0.2752, \"trigger_f1_constrained\": 0.2691, \"argument_f1_unconstrained\": 0.0998, \"argument_f1_constrained\": 0.0891, \"entity_f1\": 0, \"rov_rate_unconstrained\": 0.088, \"rov_rate_constrained\": 0, \"ac_rate_unconstrained\": 0.035, \"ac_rate_constrained\": 0.008, \"go_nogo_unconstrained\": 0.122, \"go_nogo_constrained\": 0.0078}, \"conclusion\": \"success\", \"spec\": {\"command\": \"run_constrained_extraction.py (unconstrained + full_s1)\", \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"data_path\": \"data/wikievents/test.jsonl\", \"data_count\": 20, \"model_name\": \"Llama-3.1-8B-Instruct LoRA FT merged\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_8b_lora_wikievents_merged\", \"eval_data\": \"data/wikievents/test.jsonl (20 docs)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/llama_8b_lora_wikievents_merged\", \"log_path\": \"/root/schema_semantic_constrained_ie/logs/unconstrained_r2.log\", \"fixes\": [\"schema required entities->events only\", \"repetition_penalty=1.2\", \"peft AWQ monkey-patch\"]}, \"completed_at\": \"2026-05-18T23:45:05.884Z\"}, \"p1_ee_ft_composability_r5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T23:28:28.790Z\", \"updated_at\": \"2026-05-19T00:06:27.494Z\", \"hypothesis\": \"After fixing schema mismatch (entities not required in EE JSON schema) and adding repetition_penalty=1.2, Qwen3-8B FT on WikiEvents EE will produce parseable constrained output with RoV/AC violations eliminated, validating composability on event extraction.\", \"parent\": \"p1_ee_ft_composability_r4\", \"metrics\": {\"unconstrained\": {\"parse_rate\": 0.85, \"trigger_f1\": 0.3208, \"argument_f1\": 0.0785, \"rov_rate\": 0.3831, \"ac_rate\": 0.0268, \"go_nogo\": 0.41}, \"full_s1\": {\"parse_rate\": 0.95, \"trigger_f1\": 0.2672, \"argument_f1\": 0.0818, \"rov_rate\": 0, \"ac_rate\": 0, \"go_nogo\": 0}}, \"spec\": {\"command\": \"bash run_r5_all.sh\", \"server\": \"westd-21461\", \"gpu\": \"cuda:0\", \"data_path\": \"data/wikievents/test.jsonl\", \"data_count\": 20, \"model_name\": \"Qwen3-8B LoRA FT merged\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen3_8b_lora_wikievents_merged\", \"eval_data\": \"data/wikievents/test.jsonl\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/qwen3_8b_lora_wikievents_merged\", \"log_path\": \"/root/schema_semantic_constrained_ie/logs/r5_all.log\", \"fixes\": [\"schema required entities->events only\", \"repetition_penalty=1.2\"]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T23:56:34.434Z\"}, \"p1_ee_ft_llama\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T21:57:43.193Z\", \"updated_at\": \"2026-05-18T23:23:46.294Z\", \"hypothesis\": \"LoRA fine-tuning Llama-3.1-8B-Instruct on WikiEvents EE (same config as Qwen) will produce a model whose unconstrained output has schema violations that are reduced by constrained decoding (full_s1), providing dual-model validation of OntoCoDec composability with fine-tuned models.\", \"parent\": \"p1_ee_ft_composability_r4\", \"spec\": {\"command\": \"bash /root/schema_semantic_constrained_ie/scripts/run_p1_ee_ft_llama.sh\", \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"pid\": 588752, \"log_path\": \"~/runs/schema_semantic_constrained_ie/p1_ee_ft_llama.log\", \"submitted_at\": \"2026-05-18T21:58:17.999Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/sft/wikievents_sft_train_llama.jsonl (generated by Step 0)\", \"data_count\": 194, \"model_name\": \"Meta-Llama-3.1-8B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"self (LoRA training from base)\", \"eval_data\": \"/root/schema_semantic_constrained_ie/data/wikievents/test.jsonl\", \"hyperparams\": {\"lora_r\": 16, \"lora_alpha\": 32, \"lora_dropout\": 0.05, \"lr\": 0.0002, \"epochs\": 3, \"batch_size\": 4, \"grad_accum\": 4}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/llama_8b_lora_wikievents_merged/\", \"wall_clock_seconds\": 5128.3, \"gpu_hours\": 1.42}, \"conclusion\": \"failed\", \"notes\": \"parse rate 15% constrained, same failure as Qwen\", \"completed_at\": \"2026-05-18T23:23:46.294Z\"}, \"p1_ee_ft_composability_r4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T21:50:56.983Z\", \"updated_at\": \"2026-05-18T23:23:35.581Z\", \"hypothesis\": \"LoRA fine-tuning Qwen3-8B on WikiEvents EE with correct train/dev/test splits (no data leakage) will produce a model whose unconstrained output has schema violations that are reduced by constrained decoding (full_s1), demonstrating composability of schema constraints with fine-tuned models.\", \"parent\": \"p1_ee_ft_composability_r3\", \"spec\": {\"command\": \"bash /root/schema_semantic_constrained_ie/scripts/run_p1_ee_ft.sh\", \"server\": \"westd-21461\", \"gpu\": \"cuda:0\", \"pid\": 61838, \"log_path\": \"~/runs/schema_semantic_constrained_ie/p1_ee_ft_composability_r4.log\", \"submitted_at\": \"2026-05-18T21:51:25.516Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/sft/wikievents_sft_train.jsonl\", \"data_count\": 194, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 42, \"checkpoint_source\": \"self (LoRA training from base)\", \"eval_data\": \"/root/schema_semantic_constrained_ie/data/wikievents/test.jsonl\", \"hyperparams\": {\"lora_r\": 16, \"lora_alpha\": 32, \"lora_dropout\": 0.05, \"lr\": 0.0002, \"epochs\": 3, \"batch_size\": 1, \"grad_accum\": 8}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/qwen3_8b_lora_wikievents_merged/\", \"wall_clock_seconds\": 5008.7, \"gpu_hours\": 1.39}, \"metrics\": {\"unconstrained\": {\"entity_f1\": 0, \"trigger_f1\": 0.4598, \"argument_f1\": 0.1581, \"rov\": 0.251, \"ac\": 0.06, \"cf\": 0, \"parse_rate\": 0.25}, \"full_s1\": {\"entity_f1\": 0.5823, \"trigger_f1\": 0.6, \"argument_f1\": 0.4667, \"rov\": 0, \"ac\": 0, \"cf\": 0.03, \"parse_rate\": 0.1}}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-18T23:14:54.256Z\", \"notes\": \"parse rate 10% constrained, FT breaks generation termination calibration\"}, \"p1_llama_ee_ft\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:21:21.236Z\", \"updated_at\": \"2026-05-18T22:25:10.485Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && bash /root/schema_semantic_constrained_ie/scripts/run_p1_ee_ft_llama.sh\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"593696\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/p1_llama_ee_ft.log\", \"submitted_at\": \"2026-05-18T22:25:10.185Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"w9_qwen_docred_zs_sampling_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T19:56:42.483Z\", \"updated_at\": \"2026-05-18T21:59:17.743Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/.cache/huggingface/hub/models--Qwen--Qwen3-8B/snapshots/b968826d9c46dd6066d109eabc6255188de91218 --data_path /root/autodl-tmp/schema_outputs/w9_docred_remaining.json --constraints_path data/docred/ontology_constraints_docred.json --output_path /root/autodl-tmp/schema_outputs/w9_qwen_docred_zs_sampling_r2.jsonl --batch_size 1 --max_new_tokens 4096 --temperature 0.7 --top_p 0.9 --skip_on_error --device cuda:0\", \"server\": \"westd-21461\", \"gpu\": [\"cuda:1\"], \"pid\": \"383602\", \"log_path\": \"/root/autodl-tmp/schema_outputs/w9_docred_r2.log\", \"submitted_at\": \"2026-05-16T19:56:51.235Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/schema_outputs/w9_docred_remaining.json\", \"data_count\": 892, \"model_name\": \"Qwen3-8B\", \"seed\": null, \"checkpoint_path\": \"/root/autodl-tmp/schema_outputs/w9_qwen_docred_zs_sampling_r2.jsonl\", \"checkpoint_source\": \"Qwen3-8B pretrained (zero-shot)\", \"eval_data\": \"DocRED dev set (remaining 892 docs from index 106)\", \"tmux_session\": \"w9_docred_r2\", \"wall_clock_seconds\": 179718.7, \"gpu_hours\": 49.92}, \"conclusion\": \"success\", \"hypothesis\": \"Continuation of w9 DocRED sampling from doc 106, testing OntoCoDec full_s1 with temperature sampling (T=0.7) on remaining 892 DocRED documents\", \"parent\": \"w9_qwen_docred_zs_sampling\", \"completed_at\": \"2026-05-18T21:52:09.956Z\"}, \"70b_docred_constrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T12:43:03.053Z\", \"updated_at\": \"2026-05-18T21:47:50.088Z\", \"hypothesis\": \"OntoCoDec constrained decoding (full_s1 mode) on 70B AWQ-INT4 model eliminates all schema violations (ET, RV, DR) on DocRED without degrading extraction F1, demonstrating scalability to larger models and cross-sentence RE datasets.\", \"parent\": \"70b_scierc_constrained\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --dataset docred --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path /root/autodl-tmp/schema_outputs/70b_docred_constrained.jsonl --mode full_s1 --max_new_tokens 4096 --skip_on_error\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:1\"], \"pid\": \"556631\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/70b_docred_constrained.log\", \"submitted_at\": \"2026-05-18T12:48:47.766Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"Meta-Llama-3.1-70B-Instruct-AWQ-INT4\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4\", \"eval_data\": \"data/docred/dev.json\", \"wall_clock_seconds\": 32228.7, \"gpu_hours\": 8.95}, \"reproduce\": {\"finished_at\": \"2026-05-18T21:42:12.715Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T21:42:16.440666+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/schema_outputs/70b_docred_constrained.jsonl\", \"metrics\": {\"ET_violation\": 0, \"RV_violation\": 0, \"DR_violation\": 0, \"CF_violation\": 7.01, \"entity_f1\": 69.05, \"entity_precision\": 75.03, \"entity_recall\": 63.95, \"relation_f1\": 13.07, \"relation_precision\": 12.54, \"relation_recall\": 13.64, \"parse_failures\": 1, \"docs_processed\": 997, \"total_docs\": 998, \"unique_entities\": 12207, \"total_triples\": 13249}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T21:45:56.501Z\"}, \"70b_docred_unconstrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T12:43:01.940Z\", \"updated_at\": \"2026-05-18T21:45:38.925Z\", \"hypothesis\": \"70B AWQ-INT4 model without constrained decoding serves as baseline to measure unconstrained violation rates on DocRED, establishing the gap that OntoCoDec constrained decoding eliminates.\", \"parent\": \"70b_scierc_constrained\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --dataset docred --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path /root/autodl-tmp/schema_outputs/70b_docred_unconstrained.jsonl --mode unconstrained --max_new_tokens 4096 --skip_on_error\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"556552\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/70b_docred_unconstrained.log\", \"submitted_at\": \"2026-05-18T12:48:47.766Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"Meta-Llama-3.1-70B-Instruct-AWQ-INT4\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4\", \"eval_data\": \"data/docred/dev.json\", \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 32101.9, \"gpu_hours\": 8.92}, \"reproduce\": {\"finished_at\": \"2026-05-18T21:39:02.986Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T21:39:06.770468+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"entity_f1\": 69.03, \"entity_precision\": 75.03, \"entity_recall\": 63.92, \"relation_f1\": 13.03, \"relation_precision\": 12.43, \"relation_recall\": 13.69, \"ET_violation\": 0.02, \"RV_violation\": 7.8, \"DR_violation\": 15, \"CF_violation\": 0.07, \"parse_failures\": 0, \"docs_processed\": 998}, \"completed_at\": \"2026-05-18T21:43:49.621Z\"}, \"p1_ee_ft_composability_r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T20:21:22.047Z\", \"updated_at\": \"2026-05-18T21:44:36.846Z\", \"hypothesis\": \"LoRA fine-tuning Qwen3-8B on WikiEvents EE with correct train/dev/test splits (no data leakage) will produce a model whose unconstrained output has schema violations that are reduced by constrained decoding (full_s1), demonstrating composability of schema constraints with fine-tuned models.\", \"parent\": \"p1_ee_ft_composability_r2\", \"spec\": {\"command\": \"bash /root/schema_semantic_constrained_ie/scripts/run_p1_ee_ft.sh\", \"server\": \"westd-21461\", \"gpu\": [\"cuda:0\"], \"pid\": \"58432\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/p1_ee_ft_composability_r3.log\", \"submitted_at\": \"2026-05-18T20:40:57.989Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A\", \"failure_reason\": \"RuntimeError: WandbCallback requires wandb to be installed. transformers 5.8.1 ignores WANDB_DISABLED=true, needs report_to=none in TrainingArguments\", \"wall_clock_seconds\": 3818.9, \"gpu_hours\": 1.06}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-18T21:44:36.846Z\"}, \"p1_ee_ft_composability_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:47:21.742Z\", \"updated_at\": \"2026-05-18T19:55:16.374Z\", \"hypothesis\": \"LoRA fine-tuning Qwen3-8B on WikiEvents EE with correct train/dev/test splits (no data leakage) will produce a model whose unconstrained output has schema violations that are reduced by constrained decoding (full_s1), demonstrating composability of schema constraints with fine-tuned models.\", \"parent\": \"p1_ee_ft_composability\", \"spec\": {\"command\": \"bash -c \\\"set -eo pipefail && source /root/miniconda3/bin/activate && cd /root/schema_semantic_constrained_ie && export WANDB_DISABLED=true && export CUDA_VISIBLE_DEVICES=0 && echo '=== Step 1: LoRA Training ===' && python scripts/train_lora_wikievents.py 2>&1 | tee /root/autodl-tmp/schema_outputs/p1_ee_ft_train_r2.log && echo '=== Step 2: Unconstrained Inference ===' && python run_constrained_extraction.py --dataset wikievents --mode unconstrained --model_path checkpoints/qwen3_8b_lora_wikievents_merged --data_path data/wikievents/test.jsonl --output_path outputs/ee_qwen_ft_wikievents_unconstrained.jsonl --device cuda:0 2>&1 | tee /root/autodl-tmp/schema_outputs/p1_ee_ft_unc_infer_r2.log && echo '=== Step 3: Constrained Inference ===' && python run_constrained_extraction.py --dataset wikievents --mode full_s1 --model_path checkpoints/qwen3_8b_lora_wikievents_merged --data_path data/wikievents/test.jsonl --output_path outputs/ee_qwen_ft_wikievents_full_s1.jsonl --device cuda:0 2>&1 | tee /root/autodl-tmp/schema_outputs/p1_ee_ft_con_infer_r2.log && echo '=== Step 4: Evaluation ===' && python eval_event_extraction.py --input_path outputs/ee_qwen_ft_wikievents_unconstrained.jsonl 2>&1 | tee /root/autodl-tmp/schema_outputs/p1_ee_ft_eval_unc_r2.log && python eval_event_extraction.py --input_path outputs/ee_qwen_ft_wikievents_full_s1.jsonl 2>&1 | tee /root/autodl-tmp/schema_outputs/p1_ee_ft_eval_con_r2.log && echo '=== Step 5: Violation Check ===' && python violation_checker_wikievents.py --input_path outputs/ee_qwen_ft_wikievents_unconstrained.jsonl --constraints_path data/wikievents/ontology_constraints_wikievents.json 2>&1 | tee /root/autodl-tmp/schema_outputs/p1_ee_ft_viol_unc_r2.log && python violation_checker_wikievents.py --input_path outputs/ee_qwen_ft_wikievents_full_s1.jsonl --constraints_path data/wikievents/ontology_constraints_wikievents.json 2>&1 | tee /root/autodl-tmp/schema_outputs/p1_ee_ft_viol_con_r2.log && echo '=== ALL DONE ===' | tee /root/autodl-tmp/schema_outputs/p1_ee_ft_COMPLETE_r2\\\"\", \"server\": \"westd-21461\", \"gpu\": [\"cuda:0\"], \"pid\": \"55824\", \"log_path\": \"/root/autodl-tmp/schema_outputs/p1_ee_ft_train_r2.log\", \"submitted_at\": \"2026-05-18T19:49:03.306Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A\", \"failure_reason\": \"source activate + python may have hung on model download; Director confirmed third failure\", \"wall_clock_seconds\": 373.1, \"gpu_hours\": 0.1}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-18T19:55:16.374Z\"}, \"p1_ee_ft_composability\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:21:54.303Z\", \"updated_at\": \"2026-05-18T19:47:11.788Z\", \"server\": \"westd-21461\", \"gpu\": \"cuda:0\", \"reproduce\": {\"server\": \"westd-21461\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-18T19:23:43.507Z\", \"finished_at\": \"2026-05-18T19:45:36.540Z\", \"training_hours\": 0.36}, \"spec\": {\"command\": \"bash -c \\\"cd /root/schema_semantic_constrained_ie && export WANDB_DISABLED=true && export CUDA_VISIBLE_DEVICES=0 && echo '=== Step 1: LoRA Training ===' && python scripts/train_lora_wikievents.py 2>&1 | tee /root/autodl-tmp/schema_outputs/p1_ee_ft_train.log && echo '=== Step 2: Unconstrained Inference ===' && python run_constrained_extraction.py --dataset wikievents --mode unconstrained --model_path checkpoints/qwen3_8b_lora_wikievents_merged --data_path data/wikievents/test.jsonl --output_path outputs/ee_qwen_ft_wikievents_unconstrained.jsonl --device cuda:0 2>&1 | tee /root/autodl-tmp/schema_outputs/p1_ee_ft_unc_infer.log && echo '=== Step 3: Constrained Inference ===' && python run_constrained_extraction.py --dataset wikievents --mode full_s1 --model_path checkpoints/qwen3_8b_lora_wikievents_merged --data_path data/wikievents/test.jsonl --output_path outputs/ee_qwen_ft_wikievents_full_s1.jsonl --device cuda:0 2>&1 | tee /root/autodl-tmp/schema_outputs/p1_ee_ft_con_infer.log && echo '=== Step 4: Evaluation ===' && python eval_event_extraction.py --input_path outputs/ee_qwen_ft_wikievents_unconstrained.jsonl 2>&1 | tee /root/autodl-tmp/schema_outputs/p1_ee_ft_eval_unc.log && python eval_event_extraction.py --input_path outputs/ee_qwen_ft_wikievents_full_s1.jsonl 2>&1 | tee /root/autodl-tmp/schema_outputs/p1_ee_ft_eval_con.log && echo '=== Step 5: Violation Check ===' && python violation_checker_wikievents.py --input_path outputs/ee_qwen_ft_wikievents_unconstrained.jsonl --constraints_path data/wikievents/ontology_constraints_wikievents.json 2>&1 | tee /root/autodl-tmp/schema_outputs/p1_ee_ft_viol_unc.log && python violation_checker_wikievents.py --input_path outputs/ee_qwen_ft_wikievents_full_s1.jsonl --constraints_path data/wikievents/ontology_constraints_wikievents.json 2>&1 | tee /root/autodl-tmp/schema_outputs/p1_ee_ft_viol_con.log && echo '=== ALL DONE ===' | tee /root/autodl-tmp/schema_outputs/p1_ee_ft_COMPLETE\\\"\", \"server\": \"westd-21461\", \"gpu\": [\"cuda:0\"], \"pid\": \"unknown\", \"log_path\": \"/root/autodl-tmp/schema_outputs/p1_ee_ft_train.log\", \"submitted_at\": \"2026-05-18T19:42:39.343Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A\", \"failure_reason\": \"python: command not found - tmux PATH lacks python binary, need absolute path /root/miniconda3/bin/python\", \"wall_clock_seconds\": 272.4, \"gpu_hours\": 0.08}, \"hypothesis\": \"LoRA fine-tuning Qwen3-8B on WikiEvents EE with correct train/dev/test splits (no data leakage) will produce a model whose unconstrained output has schema violations that are reduced by constrained decoding (full_s1), demonstrating composability of schema constraints with fine-tuned models.\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T19:45:43.143726+00:00\"}]}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-18T19:47:11.788Z\"}, \"p8c_ft_scierc_latency\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T18:43:08.206Z\", \"updated_at\": \"2026-05-18T19:04:35.630Z\", \"metrics\": {\"unconstrained_mean_s\": 2.612, \"constrained_mean_s\": 2.873, \"unconstrained_median_s\": 2.355, \"constrained_median_s\": 2.624, \"overhead_mean_pct\": 10, \"overhead_median_pct\": 11.42, \"per_doc_ratio_mean\": 1.205, \"per_doc_ratio_median\": 1.117, \"num_docs\": 551, \"unconstrained_total_s\": 1439, \"constrained_total_s\": 1582.9}, \"hypothesis\": \"OntoCoDec constrained decoding on fine-tuned Qwen3-8B SciERC has low latency overhead (~10%), confirming practical deployability for fine-tuned models\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py unconstrained+full_s1 then analyze_latency.py (FT Qwen3-8B SciERC)\", \"server\": \"westd-21461\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B-LoRA-SciERC-FT\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen_lora_scierc_merged\", \"eval_data\": \"data/processed_data/test.json\"}, \"checkpoint_path\": \"/root/autodl-tmp/schema_outputs/p8c_timing_ft_constrained.jsonl\", \"log_path\": \"/root/autodl-tmp/schema_outputs/p8c_latency_report.json\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T18:45:18.087Z\"}, \"p8b_docred_latency\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:14:28.888Z\", \"updated_at\": \"2026-05-18T17:48:57.349Z\", \"hypothesis\": \"OntoCoDec constrained decoding overhead on Qwen3-8B DocRED (200-doc subset) measured on same GPU as P8 SciERC will confirm moderate overhead (<2x), providing consistent timing data for paper\", \"parent\": \"p8_latency_overhead\", \"spec\": {\"command\": \"run_constrained_extraction.py unconstrained+full_s1 then analyze_latency.py\", \"server\": \"westd-21461\", \"data_path\": \"/root/autodl-tmp/schema_outputs/docred_timing_subset_200.json\", \"data_count\": 200, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_source\": \"Qwen/Qwen3-8B (base, no fine-tuning)\", \"eval_data\": \"DocRED dev subset 200 docs\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-18T17:48:57.349Z\"}, \"w9_qwen_docred_zs_sampling\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T19:28:21.393Z\", \"updated_at\": \"2026-05-18T15:49:26.958Z\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/.cache/huggingface/hub/models--Qwen--Qwen3-8B/snapshots/b968826d9c46dd6066d109eabc6255188de91218 --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path /root/autodl-tmp/schema_outputs/w9_qwen_docred_zs_sampling.jsonl --batch_size 1 --max_new_tokens 4096 --temperature 0.7 --top_p 0.9 --skip_on_error --device cuda:0\", \"server\": \"westd-21461\", \"gpu\": \"cuda:1\", \"pid\": \"40367\", \"log_path\": \"/root/autodl-tmp/schema_outputs/w9_qwen_docred_zs_sampling.log\", \"submitted_at\": \"2026-05-16T19:29:57.448Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"Qwen3-8B\", \"seed\": \"N/A (sampling)\", \"tmux_session\": \"w9_qwen_docred_zs_sampling\", \"checkpoint_path\": \"/root/autodl-tmp/schema_outputs/w9_qwen_docred_zs_sampling.jsonl\", \"wall_clock_seconds\": 157505.5, \"gpu_hours\": 43.75, \"kill_reason\": \"Director decision: DocRED sampling ROI too low. SciERC sampling sufficient.\"}, \"conclusion\": \"failed\", \"hypothesis\": \"Temperature sampling (T=0.7, top_p=0.9) with OntoCoDec full_s1 on Qwen3-8B DocRED will maintain low violation rates while exploring output diversity on cross-sentence RE with 96 relation types\", \"reproduce\": {\"finished_at\": \"2026-05-18T15:15:00.468Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-18T15:15:02.928Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T15:15:06.410317+00:00\"}]}}, \"w9_qwen_scierc_zs_sampling\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T19:28:19.627Z\", \"updated_at\": \"2026-05-18T15:11:59.448Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/w9_qwen_scierc_zs_sampling.jsonl --batch_size 1 --max_new_tokens 4096 --temperature 0.7 --top_p 0.9\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"382074\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w9_qwen_scierc_zs_sampling.log\", \"submitted_at\": \"2026-05-16T19:29:55.453Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 157324.0, \"gpu_hours\": 43.7}, \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.75, \"CF_pct\": 9.9, \"E_F1\": 31.28, \"R_F1\": 7.42, \"parse_fail_rate\": 0, \"total_samples\": 551, \"note\": \"F1 computed by v2 checker; greedy baseline with same checker: E_F1=30.98, R_F1=8.36\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"outputs/w9_qwen_scierc_zs_sampling.jsonl\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w9_qwen_scierc_zs_sampling.log\", \"hypothesis\": \"Temperature sampling (T=0.7, top_p=0.9) with OntoCoDec full_s1 on Qwen3-8B SciERC will maintain low violation rates while potentially improving F1 through output diversity compared to greedy decoding\", \"completed_at\": \"2026-05-18T15:11:59.448Z\"}, \"p8_latency_overhead\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T13:40:32.126Z\", \"updated_at\": \"2026-05-18T15:09:46.707Z\", \"hypothesis\": \"OntoCoDec constrained decoding overhead on Qwen3-8B SciERC is moderate (<2x), demonstrating practical deployability\", \"spec\": {\"command\": \"bash -c \\\"cd /root/schema_semantic_constrained_ie && export HF_HUB_OFFLINE=1 && export CUDA_VISIBLE_DEVICES=1 && /root/miniconda3/bin/python3.12 run_constrained_extraction.py --mode unconstrained --dataset scierc --model_path /root/.cache/huggingface/hub/models--Qwen--Qwen3-8B/snapshots/b968826d9c46dd6066d109eabc6255188de91218 --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path /root/autodl-tmp/schema_outputs/p8_timing_unconstrained.jsonl --max_new_tokens 4096 --skip_on_error --device cuda:0 && echo '=== UNCONSTRAINED DONE ===' && /root/miniconda3/bin/python3.12 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/.cache/huggingface/hub/models--Qwen--Qwen3-8B/snapshots/b968826d9c46dd6066d109eabc6255188de91218 --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path /root/autodl-tmp/schema_outputs/p8_timing_constrained.jsonl --max_new_tokens 4096 --skip_on_error --device cuda:0 && echo '=== CONSTRAINED DONE ===' && /root/miniconda3/bin/python3.12 analyze_latency.py /root/autodl-tmp/schema_outputs/p8_timing_unconstrained.jsonl /root/autodl-tmp/schema_outputs/p8_timing_constrained.jsonl\\\"\", \"server\": \"westd-21461\", \"gpu\": [\"cuda:1\"], \"pid\": \"30982\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/p8_latency_overhead.log\", \"submitted_at\": \"2026-05-18T13:43:58.889Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 5147.8, \"gpu_hours\": 1.43}, \"reproduce\": {\"finished_at\": \"2026-05-18T15:07:41.806Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T15:07:45.438951+00:00\"}]}, \"metrics\": {\"samples\": 551, \"unconstrained_mean_s\": 4.163, \"unconstrained_median_s\": 4.106, \"unconstrained_total_s\": 2293.7, \"constrained_mean_s\": 4.71, \"constrained_median_s\": 4.644, \"constrained_total_s\": 2595, \"overhead_ratio_mean\": 1.131, \"overhead_ratio_median\": 1.131, \"overhead_ratio_p95_perdoc\": 1.262, \"overhead_pct\": 13.1}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/schema_outputs/p8_timing_constrained.jsonl\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/p8_latency_overhead.log\", \"completed_at\": \"2026-05-18T15:09:46.707Z\"}, \"q1_llama_lora_scierc_beam4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T13:38:41.024Z\", \"updated_at\": \"2026-05-18T14:20:12.077Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/schema_semantic_constrained_ie && python run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/checkpoints/llama_lora_scierc_merged --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --decoding_strategy beam --num_beams 4 --output_path /root/autodl-tmp/schema_outputs/q1_llama_lora_scierc_beam4.jsonl --max_new_tokens 4096 --skip_on_error --device cuda:0\\\"\", \"server\": \"westd-21461\", \"gpu\": [\"cuda:0\"], \"pid\": \"30426\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/q1_llama_lora_scierc_beam4.log\", \"submitted_at\": \"2026-05-18T13:39:49.737Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-8B-Instruct-LoRA-SciERC\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_scierc_merged\", \"eval_data\": \"data/processed_data/test.json\", \"wall_clock_seconds\": 2422.3, \"gpu_hours\": 0.67}, \"hypothesis\": \"Llama-3.1-8B LoRA fine-tuned + beam search k=4 with OntoCoDec full_s1 on SciERC will achieve zero violations (ET=0%, RV=0%, DR=0%, CF=0%), replicating w10_qwen_scierc_ft_beam_4 results on a second model and strengthening the 'zero violations' Abstract claim\", \"parent\": \"w10_qwen_scierc_ft_beam_4\", \"reproduce\": {\"finished_at\": \"2026-05-18T14:12:22.985Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T14:12:31.003769+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/schema_outputs/q1_llama_lora_scierc_beam4.jsonl\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/q1_llama_lora_scierc_beam4.log\", \"conclusion\": \"success\", \"metrics\": {\"ET_violation_rate\": 0, \"RV_violation_rate\": 0, \"DR_violation_rate\": 0, \"CF_violation_rate\": 0, \"entity_f1\": 67.94, \"relation_f1\": 46.11, \"samples\": 551, \"total_entities\": 1853, \"total_relations\": 727}, \"completed_at\": \"2026-05-18T14:20:12.077Z\"}, \"70b_scierc_unconstrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T12:25:09.814Z\", \"updated_at\": \"2026-05-18T13:34:48.000Z\", \"hypothesis\": \"70B AWQ-INT4 model on SciERC unconstrained baseline will establish violation rates and F1 for large model, testing whether model scale alone reduces ontology violations without constrained decoding\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --dataset scierc --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path /root/autodl-tmp/schema_outputs/70b_scierc_unconstrained.jsonl --mode unconstrained --max_new_tokens 4096 --skip_on_error\", \"server\": \"westd-21461\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Meta-Llama-3.1-70B-Instruct-AWQ-INT4\", \"seed\": \"default\", \"gpu\": \"cuda:0\", \"pid\": 24552, \"gpu_model\": \"NVIDIA RTX PRO 6000 Blackwell 98GB\", \"log_path\": \"westd-21461:/tmp/70b_unconstrained.log\", \"checkpoint_path\": \"westd-21461:/root/autodl-tmp/schema_outputs/70b_scierc_unconstrained.jsonl\"}, \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0.6, \"DR_pct\": 6.5, \"CF_count\": 0, \"CF_pct\": 0, \"E_F1\": 0.3517, \"E_P\": 0.3009, \"E_R\": 0.4232, \"R_F1\": 0.1122, \"R_P\": 0.0929, \"R_R\": 0.1417, \"total_entities\": 2353, \"total_relations\": 1485, \"parse_failures\": 0, \"samples\": 551}, \"conclusion\": \"success\", \"notes\": \"70B unconstrained baseline on SciERC: ET=0% (model scale eliminates entity type errors), RV=0.6%, DR=6.5%, CF=0. E_F1=0.3517, R_F1=0.1122. 551/551 completed, 0 parse failures.\", \"completed_at\": \"2026-05-18T13:34:48.000Z\"}, \"70b_scierc_constrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T12:25:10.903Z\", \"updated_at\": \"2026-05-18T13:34:41.438Z\", \"hypothesis\": \"70B AWQ-INT4 model with OntoCoDec constrained decoding (full_s1) on SciERC will achieve 0% ET/RV violations while maintaining or improving F1 vs unconstrained, demonstrating OntoCoDec scales to 70B models\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --dataset scierc --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path /root/autodl-tmp/schema_outputs/70b_scierc_constrained.jsonl --mode full_s1 --max_new_tokens 4096 --skip_on_error\", \"server\": \"westd-21461\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Meta-Llama-3.1-70B-Instruct-AWQ-INT4\", \"seed\": \"default\", \"gpu\": \"cuda:1\", \"pid\": 24703, \"gpu_model\": \"NVIDIA RTX PRO 6000 Blackwell 98GB\", \"log_path\": \"westd-21461:/tmp/70b_constrained.log\", \"checkpoint_path\": \"westd-21461:/root/autodl-tmp/schema_outputs/70b_scierc_constrained.jsonl\"}, \"reproduce\": {\"finished_at\": \"2026-05-18T13:32:04.555Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T13:32:06.135Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T13:32:11.810517+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/schema_outputs/70b_scierc_constrained.jsonl\", \"notes\": \"70B + OntoCoDec on SciERC: ET=0%, RV=0%, DR=0% (all structural violations eliminated). F1 virtually identical to unconstrained (E_F1=0.3514 vs 0.3517, R_F1=0.1124 vs 0.1122). 86 CF violations (3.66%). Confirms OntoCoDec scales to 70B with zero F1 cost. Cron 之前误标 failed，实际 551/551 完成。\", \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_count\": 86, \"CF_pct\": 3.66, \"E_F1\": 0.3514, \"E_P\": 0.3007, \"E_R\": 0.4226, \"R_F1\": 0.1124, \"R_P\": 0.0932, \"R_R\": 0.1417, \"total_entities\": 2351, \"total_relations\": 1481, \"parse_failures\": 0, \"samples\": 551}}, \"ee_mistral_wikievents_grammar_only_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T10:55:33.279Z\", \"updated_at\": \"2026-05-18T10:57:01.896Z\", \"hypothesis\": \"Grammar-only mode (no semantic constraints) on Mistral with fixed 938-line code will show high RoV/AC as ablation baseline, confirming semantic layer is essential for constraint compliance\", \"spec\": {\"command\": \"python run_constrained_extraction.py --dataset wikievents --model_path Mistral-7B-Instruct-v0.3 --mode grammar_only --data_path data/wikievents/all.jsonl --output_path outputs/ee_mistral_wikievents_grammar_only_v3.jsonl --max_new_tokens 16384 --skip_on_error\", \"server\": \"westd-16980\", \"data_path\": \"data/wikievents/all.jsonl\", \"data_count\": 246, \"model_name\": \"Mistral-7B-Instruct-v0.3\", \"seed\": \"default\", \"checkpoint_path\": \"westd-16980:/root/schema_semantic_constrained_ie/outputs/ee_mistral_wikievents_grammar_only_v3.jsonl\", \"log_path\": \"westd-16980:/root/schema_semantic_constrained_ie/outputs/violation_report_mistral_grammar_only_v3.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T10:56:03.323Z\", \"metrics\": {\"parse_success\": \"218/246 (88.6%)\", \"parse_failures\": 28, \"ET\": 0, \"EV\": 0, \"RoV\": 64, \"AC\": 13.8, \"CF\": 1.1, \"go_no_go\": 77.73, \"entity_f1\": 0.1192, \"trigger_f1\": 0.0337, \"argument_f1\": 0.0027, \"code_version\": \"938-line (collision+exact-match fix)\", \"mode\": \"grammar_only\"}}, \"ee_mistral_wikievents_constrained_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T10:55:31.905Z\", \"updated_at\": \"2026-05-18T10:56:59.824Z\", \"hypothesis\": \"938-line fixed code with collision group continuation mask will reduce Mistral AC from 16.6% to near 0% by disambiguating SentencePiece entity type collisions at second+ token steps\", \"spec\": {\"command\": \"python run_constrained_extraction.py --dataset wikievents --model_path Mistral-7B-Instruct-v0.3 --mode full_s1 --data_path data/wikievents/all.jsonl --output_path outputs/ee_mistral_wikievents_constrained_v3_full.jsonl --max_new_tokens 16384 --skip_on_error\", \"server\": \"westd-21461\", \"data_path\": \"data/wikievents/all.jsonl\", \"data_count\": 246, \"model_name\": \"Mistral-7B-Instruct-v0.3\", \"seed\": \"default\", \"checkpoint_path\": \"westd-21461:/root/schema_semantic_constrained_ie/outputs/ee_mistral_wikievents_constrained_v3_full.jsonl\", \"log_path\": \"westd-21461:/root/schema_semantic_constrained_ie/outputs/violation_report_mistral_v3.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T10:56:02.188Z\", \"metrics\": {\"parse_success\": \"218/246 (88.6%)\", \"parse_failures\": 28, \"ET\": 0, \"EV\": 0, \"RoV\": 0, \"AC\": 1.3, \"CF\": 14.9, \"go_no_go\": 1.26, \"entity_f1\": 0.1171, \"trigger_f1\": 0.0387, \"argument_f1\": 0.0031, \"code_version\": \"938-line (collision+exact-match fix)\", \"posthoc_args_removed\": 86, \"posthoc_ac_after\": 0}}, \"ee_llama_wikievents_constrained_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T10:52:02.423Z\", \"updated_at\": \"2026-05-18T10:52:28.084Z\", \"hypothesis\": \"938-line fixed code (collision group + exact-match fix) will maintain RoV=0% and reduce AC for Llama on WikiEvents full 246 docs, confirming cross-model generalization of the fix\", \"spec\": {\"command\": \"python run_constrained_extraction.py --dataset wikievents --model_path Meta-Llama-3.1-8B-Instruct --mode full_s1 --data_path data/wikievents/all.jsonl --output_path outputs/ee_llama_wikievents_constrained_v3_full.jsonl --max_new_tokens 16384 --skip_on_error\", \"server\": \"westd-21461\", \"data_path\": \"data/wikievents/all.jsonl\", \"data_count\": 246, \"model_name\": \"Meta-Llama-3.1-8B-Instruct\", \"seed\": \"default\", \"checkpoint_path\": \"westd-21461:/root/schema_semantic_constrained_ie/outputs/ee_llama_wikievents_constrained_v3_full.jsonl\", \"log_path\": \"westd-21461:/root/schema_semantic_constrained_ie/outputs/\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T10:52:25.562Z\", \"metrics\": {\"parse_success\": \"207/246 (84.1%)\", \"parse_failures\": 39, \"ET\": 0, \"EV\": 0, \"RoV\": 0, \"AC\": 3.8, \"CF\": 17.2, \"go_no_go\": 3.8, \"entity_f1\": 0.1763, \"trigger_f1\": 0.0748, \"argument_f1\": 0.0118, \"code_version\": \"938-line (collision+exact-match fix)\", \"posthoc_args_removed\": 173, \"posthoc_arg_f1\": 0.0118}}, \"ee_qwen_wikievents_constrained_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T10:29:11.628Z\", \"updated_at\": \"2026-05-18T10:29:44.522Z\", \"hypothesis\": \"938-line fixed code (collision group + exact-match fix) will maintain RoV=0% and reduce AC from 2.1% to near 0% for Qwen on WikiEvents full 246 docs, confirming the fix generalizes across the full test set\", \"spec\": {\"command\": \"python run_constrained_extraction.py --dataset wikievents --model_path Qwen3-8B --mode full_s1 --data_path data/wikievents/all.jsonl --output_path outputs/ee_qwen_wikievents_constrained_v3_full.jsonl --max_new_tokens 16384 --skip_on_error\", \"server\": \"westd-16980\", \"data_path\": \"data/wikievents/all.jsonl\", \"data_count\": 246, \"model_name\": \"Qwen3-8B\", \"seed\": \"default\", \"checkpoint_path\": \"westd-16980:/root/schema_semantic_constrained_ie/outputs/ee_qwen_wikievents_constrained_v3_full.jsonl\", \"log_path\": \"westd-16980:/root/schema_semantic_constrained_ie/outputs/violation_report_qwen_v3.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T10:29:37.217Z\", \"metrics\": {\"parse_success\": \"206/246 (83.7%)\", \"parse_failures\": 40, \"ET\": 0, \"EV\": 0, \"RoV\": 0, \"AC\": 2.1, \"CF\": 21.1, \"go_no_go\": 2.05, \"entity_f1\": 0.1409, \"trigger_f1\": 0.1339, \"argument_f1\": 0.0168, \"code_version\": \"938-line (collision+exact-match fix)\", \"posthoc_args_removed\": 109, \"posthoc_arg_f1\": 0.017, \"cf_voting_fix_rate\": \"15.9%\", \"cf_voting_entity_f1\": 0.1352}}, \"ee_mistral_wikievents_constrained_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T21:42:15.493Z\", \"updated_at\": \"2026-05-18T01:42:46.453Z\", \"hypothesis\": \"WikiEvents constrained decoding with fixed tokenizer-agnostic continuation masking (full_s1 + vocab-scan prefix map) will eliminate EV (37.3%→0%) and RoV (63.9%→0%) for Mistral-7B, confirming the fix generalizes OntoCoDec across all three tokenizer families (byte-level BPE + SentencePiece)\", \"parent\": \"ee_mistral_wikievents_constrained\", \"spec\": {\"command\": \"HF_HUB_OFFLINE=1 CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python run_constrained_extraction.py --mode full_s1 --dataset wikievents --model_path /root/autodl-tmp/.ms_cache/mistralai/Mistral-7B-Instruct-v0___3/ --constraints_path data/wikievents/ontology_constraints_wikievents.json --data_path data/wikievents/all.jsonl --output_path outputs/ee_mistral_wikievents_constrained_v2_full.jsonl --skip_on_error --resume\", \"server\": \"westd-21461\", \"data_path\": \"data/wikievents/all.jsonl\", \"data_count\": 246, \"model_name\": \"Mistral-7B-Instruct-v0.3\", \"seed\": \"default\", \"gpu\": \"cuda:0\", \"pid\": 40830, \"checkpoint_source\": \"base_model:Mistral-7B-Instruct-v0.3\", \"eval_data\": \"data/wikievents/all.jsonl\", \"checkpoint_path\": \"outputs/ee_mistral_wikievents_constrained_v2_full.jsonl\", \"log_path\": \"logs/mistral_constrained_v2_full.log\"}, \"metrics\": {\"parse_success\": \"178/246 (72.4%)\", \"ET\": 0, \"EV\": 0, \"RoV\": 0.1, \"AC\": 16.6, \"CF\": 13.9, \"trigger_f1\": 0.0508, \"argument_f1\": 0.0047, \"entity_f1\": 0.1245, \"parse_failures\": 68, \"go_no_go\": 16.7}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T01:42:46.453Z\"}, \"ee_qwen_wikievents_constrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T19:49:18.898Z\", \"updated_at\": \"2026-05-18T01:42:39.692Z\", \"hypothesis\": \"WikiEvents constrained decoding (full_s1 + continuation masking v2) will eliminate EV violations (24%→0%) and dramatically reduce RoV (74.9%→near 0%) with minimal F1 impact, demonstrating cross-task generalizability of OntoCoDec from RE to EE\", \"spec\": {\"command\": \"python run_constrained_extraction.py --model_name Qwen/Qwen3-8B --dataset wikievents --data_path data/wikievents/all.jsonl --constraint_mode full_s1 --ontology_path data/wikievents/ontology_constraints_wikievents.json --output_file outputs/wikievents_qwen_constrained_full.jsonl --max_new_tokens 4096\", \"server\": \"westd-16980\", \"data_path\": \"data/wikievents/all.jsonl\", \"data_count\": 246, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": \"default\", \"checkpoint_path\": \"outputs/wikievents_qwen_constrained_full.jsonl\", \"log_path\": \"logs/qwen_constrained_full.log\"}, \"metrics\": {\"parse_success\": \"206/246 (83.7%)\", \"ET\": 0, \"EV\": 0, \"RoV\": 0.3, \"AC\": 2.1, \"CF\": 21.1, \"trigger_f1\": 0.1339, \"argument_f1\": 0.0168, \"entity_f1\": 0.1409, \"parse_failures\": 40, \"go_no_go\": 2.4, \"note\": \"after retry with max_new_tokens=8192\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T22:24:23.672Z\"}, \"ee_mistral_wikievents_constrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T20:51:11.907Z\", \"updated_at\": \"2026-05-17T23:52:50.557Z\", \"hypothesis\": \"WikiEvents constrained decoding (full_s1 + continuation masking v2) will eliminate EV violations (37.3%→0%) and dramatically reduce RoV (63.9%→near 0%) with minimal F1 impact, demonstrating cross-task generalizability of OntoCoDec from RE to EE\", \"spec\": {\"command\": \"HF_HUB_OFFLINE=1 CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python run_constrained_extraction.py --mode full_s1 --dataset wikievents --model_path /root/autodl-tmp/.ms_cache/mistralai/Mistral-7B-Instruct-v0___3/ --constraints_path data/wikievents/ontology_constraints_wikievents.json --data_path data/wikievents/all.jsonl --output_path outputs/mistral_constrained_full.jsonl --resume\", \"server\": \"westd-21461\", \"data_path\": \"data/wikievents/all.jsonl\", \"data_count\": 246, \"model_name\": \"Mistral-7B-Instruct-v0.3\", \"seed\": \"default\", \"checkpoint_path\": \"outputs/mistral_constrained_full.jsonl\", \"log_path\": \"logs/mistral_constrained_full.log\"}, \"conclusion\": \"success\", \"metrics\": {\"parse_success\": \"184/246 (74.8%)\", \"ET\": 0, \"EV\": 0, \"RoV\": 54.8, \"AC\": 19.2, \"CF\": 0.7, \"note\": \"grammar_only baseline (old code without semantic mask fix)\"}, \"completed_at\": \"2026-05-17T23:52:50.557Z\"}, \"ee_llama_wikievents_constrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T19:49:20.228Z\", \"updated_at\": \"2026-05-17T23:52:42.652Z\", \"hypothesis\": \"WikiEvents constrained decoding (full_s1 + continuation masking v2) will eliminate EV violations (10.5%→0%) and dramatically reduce RoV (88.8%→near 0%) with minimal F1 impact, demonstrating cross-task generalizability of OntoCoDec from RE to EE\", \"spec\": {\"command\": \"python run_constrained_extraction.py --model_name meta-llama/Llama-3.1-8B-Instruct --dataset wikievents --data_path data/wikievents/all.jsonl --constraint_mode full_s1 --ontology_path data/wikievents/ontology_constraints_wikievents.json --output_file outputs/wikievents_llama_constrained_full.jsonl --max_new_tokens 4096\", \"server\": \"westd-16980\", \"data_path\": \"data/wikievents/all.jsonl\", \"data_count\": 246, \"model_name\": \"meta-llama/Llama-3.1-8B-Instruct\", \"seed\": \"default\", \"checkpoint_path\": \"outputs/wikievents_llama_constrained_full.jsonl\", \"log_path\": \"logs/llama_constrained_full.log\"}, \"metrics\": {\"parse_success\": \"215/246 (87.4%)\", \"ET\": 0, \"EV\": 0, \"RoV\": 0, \"AC\": 3.4, \"CF\": 15.5, \"trigger_f1\": 0.078, \"argument_f1\": 0.011, \"entity_f1\": 0.178, \"parse_failures\": 31, \"go_no_go\": 3.4, \"note\": \"after retry with max_new_tokens=8192\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T22:24:24.731Z\"}, \"ee_mistral_wikievents_unconstrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T20:51:09.310Z\", \"updated_at\": \"2026-05-17T20:52:08.375Z\", \"hypothesis\": \"WikiEvents zero-shot unconstrained baseline: Mistral-7B-Instruct-v0.3 will produce significant EV and RoV violations due to lack of schema constraints, establishing baseline violation rates for cross-task generalizability evaluation\", \"spec\": {\"command\": \"HF_HUB_OFFLINE=1 CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python run_constrained_extraction.py --mode unconstrained --dataset wikievents --model_path /root/autodl-tmp/.ms_cache/mistralai/Mistral-7B-Instruct-v0___3/ --data_path data/wikievents/all.jsonl --output_path outputs/mistral_unconstrained_full.jsonl\", \"server\": \"westd-21461\", \"data_path\": \"data/wikievents/all.jsonl\", \"data_count\": 246, \"model_name\": \"Mistral-7B-Instruct-v0.3\", \"seed\": \"default\", \"checkpoint_path\": \"outputs/mistral_unconstrained_full.jsonl\", \"log_path\": \"logs/mistral_restart.log\"}, \"conclusion\": \"success\", \"metrics\": {\"parse_success\": \"194/246 (78.9%)\", \"ET\": 0, \"EV\": 37.3, \"RoV\": 63.9, \"AC\": 0, \"CF\": 0, \"trigger_f1\": 0.0241, \"argument_f1\": 0, \"entity_f1\": 0}, \"completed_at\": \"2026-05-17T20:52:08.375Z\"}, \"ee_llama_wikievents_unconstrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T19:35:35.416Z\", \"updated_at\": \"2026-05-17T19:36:23.547Z\", \"hypothesis\": \"WikiEvents zero-shot unconstrained baseline: Llama-3.1-8B will produce significant EV and RoV violations due to lack of schema constraints, establishing baseline violation rates for cross-task generalizability evaluation\", \"spec\": {\"command\": \"python run_constrained_extraction.py --model_name meta-llama/Llama-3.1-8B-Instruct --dataset wikievents --data_path data/wikievents/all.jsonl --constraint_mode unconstrained --ontology_path data/wikievents/ontology_constraints_wikievents.json --output_file outputs/wikievents_llama_unconstrained_full.jsonl --max_new_tokens 4096\", \"server\": \"westd-16980\", \"data_path\": \"data/wikievents/all.jsonl\", \"data_count\": 246, \"model_name\": \"meta-llama/Llama-3.1-8B-Instruct\", \"seed\": \"default\", \"checkpoint_path\": \"N/A\", \"log_path\": \"outputs/wikievents_llama_unconstrained_full.jsonl\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T19:36:15.874Z\", \"metrics\": {\"parse_success\": \"226/246 (91.9%)\", \"ET\": 0, \"EV\": 10.5, \"RoV\": 88.8, \"AC\": 0.1, \"CF\": 0, \"trigger_f1\": 0.0572, \"argument_f1\": 0, \"entity_f1\": 0}}, \"ee_qwen_wikievents_unconstrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T19:35:34.282Z\", \"updated_at\": \"2026-05-17T19:36:21.800Z\", \"hypothesis\": \"WikiEvents zero-shot unconstrained baseline: Qwen3-8B will produce significant EV and RoV violations due to lack of schema constraints, establishing baseline violation rates for cross-task generalizability evaluation\", \"spec\": {\"command\": \"python run_constrained_extraction.py --model_name Qwen/Qwen3-8B --dataset wikievents --data_path data/wikievents/all.jsonl --constraint_mode unconstrained --ontology_path data/wikievents/ontology_constraints_wikievents.json --output_file outputs/wikievents_qwen_unconstrained_full.jsonl --max_new_tokens 4096\", \"server\": \"westd-16980\", \"data_path\": \"data/wikievents/all.jsonl\", \"data_count\": 246, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": \"default\", \"checkpoint_path\": \"N/A\", \"log_path\": \"outputs/wikievents_qwen_unconstrained_full.jsonl\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T19:36:14.859Z\", \"metrics\": {\"parse_success\": \"218/246 (88.6%)\", \"ET\": 0, \"EV\": 24, \"RoV\": 74.9, \"AC\": 0.3, \"CF\": 0, \"trigger_f1\": 0.1184, \"argument_f1\": 0.0009, \"entity_f1\": 0}}, \"r4_prompt_detailed\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T12:33:16.258Z\", \"updated_at\": \"2026-05-17T17:02:29.748Z\", \"spec\": {\"command\": \"python run_prompt_sensitivity.py --prompt_variant detailed\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:1\"], \"pid\": \"443521\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/r4_prompt_detailed.log\", \"submitted_at\": \"2026-05-17T12:33:16.038Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_path\": \"outputs/r4_detailed_full_s1.jsonl\", \"wall_clock_seconds\": 16153.7, \"gpu_hours\": 4.49}, \"hypothesis\": \"OntoCoDec constraint enforcement is robust to prompt variation: a detailed prompt (with type definitions and extraction guidelines) should achieve similar DR reduction as the default prompt\", \"metrics\": {\"unconstrained\": {\"ET_pct\": 0.22, \"RV_pct\": 0.45, \"DR_pct\": 11.07, \"E_F1\": 33.55, \"R_F1\": 10.48}, \"constrained\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.64, \"E_F1\": 33.56, \"R_F1\": 10.48}, \"DR_reduction_pct\": 94.2, \"delta_R_F1_pp\": 0, \"delta_E_F1_pp\": 0.01}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T17:02:29.748Z\"}, \"r4_prompt_minimal\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T12:33:14.503Z\", \"updated_at\": \"2026-05-17T17:02:28.635Z\", \"spec\": {\"command\": \"python run_prompt_sensitivity.py --prompt_variant minimal\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"443445\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/r4_prompt_minimal.log\", \"submitted_at\": \"2026-05-17T12:33:14.278Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_path\": \"outputs/r4_minimal_full_s1.jsonl\", \"wall_clock_seconds\": 16154.4, \"gpu_hours\": 4.49}, \"hypothesis\": \"OntoCoDec constraint enforcement is robust to prompt variation: a minimal prompt (listing only entity/relation types) should achieve similar DR reduction as the default prompt\", \"metrics\": {\"unconstrained\": {\"ET_pct\": 0.58, \"RV_pct\": 1.16, \"DR_pct\": 16.91, \"E_F1\": 31.98, \"R_F1\": 7.91}, \"constrained\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.92, \"E_F1\": 31.99, \"R_F1\": 7.85}, \"DR_reduction_pct\": 94.6, \"delta_R_F1_pp\": -0.06, \"delta_E_F1_pp\": 0.01}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T17:02:28.635Z\"}, \"w10_qwen_scierc_ft_beam_4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T09:47:48.852Z\", \"updated_at\": \"2026-05-17T10:27:12.254Z\", \"hypothesis\": \"FT+beam composability: Qwen3-8B SciERC LoRA FT + beam k=4 + full_s1 constraints will reduce residual DR from FT greedy (0.20%) to 0%, demonstrating that beam search eliminates the last constraint-search failures even in fine-tuned models. Validates full-stack OntoCoDec+FT+beam composability.\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path checkpoints/qwen3_8b_lora_scierc_merged --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/w10_qwen_scierc_ft_beam_k4.jsonl --decoding_strategy beam --num_beams 4 --device cuda:0 --batch_size 1 --max_new_tokens 2048 --max_samples 551\", \"server\": \"westd-16980\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B-LoRA-SciERC (FT)\", \"seed\": 42}, \"metrics\": {\"DR\": 0, \"CF\": 0, \"total_violation_rate\": 0, \"entity_type_violation_rate\": 0, \"relation_vocab_violation_rate\": 0, \"domain_range_violation_rate\": 0, \"cross_field_consistency_violation_rate\": 0, \"E_F1\": 66.88, \"E_P\": 64.69, \"E_R\": 69.22, \"R_F1\": 44.23, \"R_P\": 39.41, \"R_R\": 50.41, \"total_samples\": 551, \"json_parse_failures\": 0, \"total_entities\": 1802, \"total_relations\": 1246, \"vs_ft_greedy\": {\"baseline\": \"w5_lora_scierc_constrained_eval\", \"DR_delta\": \"0% → 0% (same)\", \"CF_delta\": \"1.18% → 0.0% (eliminated all violations)\", \"E_F1_delta\": \"67.05 → 66.88 (-0.17, negligible)\", \"R_F1_delta\": \"43.77 → 44.23 (+0.46, slight improvement)\"}, \"vs_zs_beam_k4\": {\"DR_delta\": \"0% → 0% (same)\", \"CF_delta\": \"0.53% → 0.0% (eliminated)\", \"E_F1_delta\": \"32.00 → 66.88 (+34.88)\", \"R_F1_delta\": \"8.56 → 44.23 (+35.67)\"}}, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/w10_qwen_scierc_ft_beam_k4.jsonl\", \"log_path\": \"/root/schema_semantic_constrained_ie/logs/w10_qwen_scierc_ft_beam_k4.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T10:27:12.254Z\"}, \"w10_beam_ablation_k8\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T08:31:56.573Z\", \"updated_at\": \"2026-05-17T09:46:19.797Z\", \"hypothesis\": \"Beam search k=8 on Qwen3-8B SciERC (551 docs) will match or marginally improve on k=4 (DR=0%, CF=0.53%), testing whether larger beam width yields diminishing returns for constraint satisfaction once DR is already eliminated.\", \"spec\": {\"command\": \"cd /root/schema_semantic_constrained_ie && python run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/scierc_qwen_beam_k8_551.jsonl --decoding_strategy beam --num_beams 8 --device cuda:1 --max_samples 551\", \"server\": \"westd-16980\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B (ZS)\", \"seed\": 42}, \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0.08, \"CF_count\": 2, \"E_F1\": 32.18, \"R_F1\": 8.39, \"E_P\": 26.95, \"E_R\": 39.93, \"R_P\": 6.54, \"R_R\": 11.7, \"parse_failures\": 0, \"total_samples\": 551, \"total_triples\": 1744, \"total_entities\": 2483, \"vs_greedy\": {\"DR_delta\": -0.93, \"CF_delta\": -9.82, \"E_F1_delta\": 1.2, \"R_F1_delta\": 0.03}, \"vs_beam_k4\": {\"DR_delta\": 0, \"CF_delta\": -0.45, \"E_F1_delta\": 0.18, \"R_F1_delta\": -0.17}}, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/scierc_qwen_beam_k8_551.jsonl\", \"log_path\": \"N/A - submit_training_job tmux\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T09:46:19.797Z\"}, \"w9_mistral_docred_beam_50\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T09:40:36.971Z\", \"updated_at\": \"2026-05-17T09:42:22.695Z\", \"hypothesis\": \"Beam search (k=4) on Mistral-7B DocRED (50 docs) will reduce DR from greedy baseline (33.21%) through broader token exploration, but entity type misclassification limits improvement. Boundary condition for beam search effectiveness.\", \"spec\": {\"command\": \"python run_constrained_extraction.py --mode full_s1 --dataset docred --model_path mistralai/Mistral-7B-Instruct-v0.3 --decoding_strategy beam --num_beams 4 --max_samples 50\", \"server\": \"westd-21461\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 50, \"model_name\": \"Mistral-7B-Instruct-v0.3 (ZS)\", \"seed\": 42}, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/w9_mistral_docred_beam4_full_s1.jsonl\", \"log_path\": \"N/A - retroactive registration\", \"metrics\": {\"ET_violation_rate\": 0, \"RV_violation_rate\": 0, \"DR_violation_rate\": 21.37, \"CF_violations\": 1, \"total_triples\": 524, \"total_entities\": 597, \"docs_checked\": 49, \"parse_failures\": 1, \"E_F1\": 51.78, \"E_P\": 65.2, \"E_R\": 42.94, \"R_F1\": 5.7, \"R_P\": 6.49, \"R_R\": 5.08, \"R_tp\": 34, \"R_gold\": 669, \"R_pred\": 524}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T09:42:22.695Z\"}, \"w10_beam_ablation_k2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T08:31:55.361Z\", \"updated_at\": \"2026-05-17T09:32:16.894Z\", \"hypothesis\": \"Beam search k=2 on Qwen3-8B SciERC (551 docs) will partially reduce DR and CF compared to greedy (DR=0.93%, CF=9.90%), but less effectively than k=4 (DR=0%, CF=0.53%). Establishes the lower bound of the beam size-constraint satisfaction curve.\", \"spec\": {\"command\": \"cd /root/schema_semantic_constrained_ie && python run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/scierc_qwen_beam_k2_551.jsonl --decoding_strategy beam --num_beams 2 --device cuda:0 --max_samples 551\", \"server\": \"westd-16980\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B (ZS)\", \"seed\": 42}, \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.35, \"CF_count\": 71, \"CF_pct\": 4.12, \"E_F1\": 31.54, \"R_F1\": 8.75, \"parse_failures\": 0, \"total_samples\": 551, \"total_triples\": 1724, \"vs_greedy\": {\"DR_delta\": -0.58, \"CF_delta\": -5.78, \"E_F1_delta\": 0.56, \"R_F1_delta\": 0.39, \"note\": \"Greedy: DR=0.93%, CF=9.90%, E_F1=30.98, R_F1=8.36\"}, \"vs_beam_k4\": {\"DR_delta\": 0.35, \"CF_delta\": 3.59, \"E_F1_delta\": -0.46, \"R_F1_delta\": 0.19, \"note\": \"k=4: DR=0%, CF=0.53%, E_F1=32.00, R_F1=8.56\"}}, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/scierc_qwen_beam_k2_551.jsonl\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w10_beam_ablation_k2.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T09:32:16.894Z\"}, \"w10_mistral_scierc_beam_551\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T07:24:10.347Z\", \"updated_at\": \"2026-05-17T08:33:57.080Z\", \"hypothesis\": \"Beam search (k=4) on Mistral SciERC will reduce DR from greedy baseline (13.4%) through broader token-level exploration, but entity type misclassification may limit improvement compared to calibrated models (Qwen/Llama achieve DR=0% with beam). Completes the 3x2 beam search matrix.\", \"spec\": {\"command\": \"python run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/Mistral-7B-Instruct-v0.3 --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/scierc_mistral_beam_551.jsonl --decoding_strategy beam --num_beams 4 --device cuda:0\", \"server\": \"westd-21461\", \"gpu\": [\"cuda:0\"], \"pid\": \"5112\", \"model_name\": \"Mistral-7B-Instruct-v0.3 (ZS)\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"seed\": 42, \"notes\": \"No fix_mistral_regex. Completes 3x2 beam matrix.\"}, \"metrics\": {\"total_samples\": 551, \"parse_failures\": 1, \"parse_rate\": 0.9982, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 13.79, \"CF_pct\": 0.57, \"E_P\": 23.04, \"E_R\": 31.64, \"E_F1\": 26.66, \"R_P\": 3.13, \"R_R\": 7.22, \"R_F1\": 4.37, \"total_entities\": 2294, \"total_triples\": 2241, \"vs_greedy\": {\"baseline\": \"w6_mistral_scierc_constrained\", \"greedy_DR\": 13.4, \"greedy_CF\": 1.27, \"greedy_E_F1\": 27.46, \"greedy_R_F1\": 3.67, \"delta_DR\": \"+0.39pp\", \"delta_CF\": \"-0.70pp\", \"delta_E_F1\": \"-0.80pp\", \"delta_R_F1\": \"+0.70pp\"}}, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/scierc_mistral_beam_551.jsonl\", \"log_path\": \"/root/runs/schema_semantic_constrained_ie/w10_mistral_scierc_beam_551.log\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-17T08:33:53.672Z\", \"analysis\": \"Beam search (k=4) on Mistral SciERC shows mixed results vs greedy. R_F1 improved (+0.70pp, 4.37 vs 3.67) and CF violations halved (0.57% vs 1.27%), but DR slightly worse (13.79% vs 13.4%) and E_F1 slightly worse (26.66 vs 27.46). Hypothesis partially falsified: beam search did not reduce DR violations. Consistent with finding that Mistral entity type misclassification is the bottleneck, not token-level exploration breadth.\"}, \"w10_llama_docred_beam_50\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T07:11:24.746Z\", \"updated_at\": \"2026-05-17T07:56:15.809Z\", \"hypothesis\": \"Beam search (k=4) on Llama DocRED will reduce DR and CF violations, completing the beam search matrix (3rd model-dataset combination). Llama's weaker entity typing on DocRED may limit DR elimination compared to Qwen.\", \"spec\": {\"command\": \"python run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/docred_llama_beam_50.jsonl --decoding_strategy beam --num_beams 4 --device cuda:0 --max_samples 50\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"424211\", \"model_name\": \"Llama-3.1-8B-Instruct (ZS)\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 50, \"seed\": 42}, \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0.94, \"E_F1\": 55.62, \"R_F1\": 9.47, \"parse_failures\": 3, \"parse_fail_rate\": 6, \"total_samples\": 50, \"vs_greedy_full_s1\": {\"DR_delta\": -2.57, \"CF_delta\": -11.19, \"E_F1_delta\": 0.61, \"R_F1_delta\": 3.2, \"note\": \"Greedy baseline: DR=2.57%, CF=12.13%, E_F1=55.01, R_F1=6.27\"}, \"checker_note\": \"Must use violation_checker_docred.py for DocRED (not violation_checker.py)\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/docred_llama_beam_50.jsonl\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w10_llama_docred_beam_50.log\", \"completed_at\": \"2026-05-17T07:37:38.035Z\"}, \"w10_type_consensus_docred_50\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T06:06:56.659Z\", \"updated_at\": \"2026-05-17T07:09:42.510Z\", \"hypothesis\": \"GTC Layer 3 on DocRED (96 relation types, complex schema) will reduce CF violations while maintaining DR through DR-aware skip mechanism; skip frequency expected higher than SciERC due to more type ambiguity in fine-grained ontology\", \"spec\": {\"command\": \"python run_constrained_extraction.py --mode full_s1 --dataset docred --type_consensus --max_samples 50 --device cuda:0\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:1\"], \"pid\": \"419622\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w10_type_consensus_docred_50.log\", \"submitted_at\": \"2026-05-17T06:07:17.194Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen3-8B\", \"data_path\": \"data/processed_data/docred_test.json\", \"data_count\": 50, \"seed\": 42, \"notes\": \"GTC Layer 3 v2 on DocRED 96-type schema. Testing skip frequency under complex ontology.\", \"wall_clock_seconds\": 3745.3, \"gpu_hours\": 1.04}, \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 8.69, \"CF_pct\": 2.4, \"E_F1\": 59.08, \"R_F1\": 8.33, \"gtc_skip_total\": 601, \"gtc_skip_unique_entities\": 213, \"gtc_effective_corrections\": 0, \"delta_DR\": 0, \"delta_CF\": 0}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/docred_full_s1_consensus_50.jsonl\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w10_type_consensus_docred_50.log\", \"completed_at\": \"2026-05-17T07:09:42.510Z\"}, \"w10_type_consensus_prototype\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T05:07:18.638Z\", \"updated_at\": \"2026-05-17T07:09:41.619Z\", \"hypothesis\": \"Document-level type consensus constraint (forcing same entity text to receive identical type across all relation triples) will eliminate CF violations caused by inconsistent type assignment, reducing CF from ~9.90% toward 0% on SciERC without increasing DR\", \"spec\": {\"command\": \"python run_constrained_extraction.py --mode full_s1 --dataset scierc --type_consensus --device cuda:0\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"417859\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w10_type_consensus_prototype.log\", \"submitted_at\": \"2026-05-17T05:34:19.247Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen3-8B\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"seed\": 42, \"notes\": \"GTC Layer 3 v2 (DR-aware skip). Kill switch: DR>2% → abort.\", \"wall_clock_seconds\": 5722.4, \"gpu_hours\": 1.59}, \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.93, \"CF_pct\": 9.9, \"E_F1\": 30.98, \"R_F1\": 8.36, \"gtc_skip_total\": 672, \"gtc_skip_unique_entities\": 258, \"gtc_effective_corrections\": 0, \"delta_DR\": 0, \"delta_CF\": 0}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/scierc_full_s1_consensus_v2.jsonl\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w10_type_consensus_prototype.log\", \"completed_at\": \"2026-05-17T07:09:41.619Z\"}, \"w9_qwen_scierc_stability_3seeds\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T02:55:58.164Z\", \"updated_at\": \"2026-05-17T05:05:28.139Z\", \"hypothesis\": \"Greedy full_s1 constraint results on SciERC are stable across random seeds: DR should remain in 0.7-1.2% range (near the 0.93% baseline), demonstrating that the single-run result is not an outlier\", \"spec\": {\"command\": \"bash run_stability_test.sh (seeds 123,456,789 sequential)\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"406710\", \"model_name\": \"Qwen3-8B\", \"data_path\": \"data/scierc/test.json\", \"data_count\": 551, \"seed\": \"123,456,789\"}, \"metrics\": {\"seed_123\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.93, \"CF_pct\": 9.9, \"E_F1\": 30.98, \"R_F1\": 8.36}, \"seed_456\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.93, \"CF_pct\": 9.9, \"E_F1\": 30.98, \"R_F1\": 8.36}, \"seed_789\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.93, \"CF_pct\": 9.9, \"E_F1\": 30.98, \"R_F1\": 8.36}, \"cross_seed_DR_std\": 0, \"cross_seed_DR_range\": 0, \"conclusion_note\": \"Greedy decoding is fully deterministic - seed has no effect on output. All metrics identical across 3 seeds.\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/stability_seed123.jsonl\", \"log_path\": \"/root/schema_semantic_constrained_ie/outputs/stability_test.log\", \"completed_at\": \"2026-05-17T05:05:28.139Z\"}, \"w9_qwen_docred_beam_50\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T03:48:50.746Z\", \"updated_at\": \"2026-05-17T04:50:39.890Z\", \"hypothesis\": \"Beam search (k=4) on Qwen3-8B DocRED 50 docs with full_s1: DR should decrease from greedy baseline 10.21% but likely not reach 0% due to DocRED's tighter schema (96 types, avg 5.68 valid pairs). Tests whether beam exploration can find legal paths in a complex constraint space.\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --decoding_strategy beam --num_beams 4 --max_samples 50 --output_path outputs/w9_qwen_docred_beam_50.jsonl\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"412229\", \"model_name\": \"Qwen3-8B\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 50, \"seed\": 42}, \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0.55, \"E_F1\": 58.64, \"R_F1\": 9.37, \"total_samples\": 50, \"parse_failures\": 3, \"parse_fail_rate\": 6, \"vs_greedy_full_s1\": {\"DR_delta\": -10.21, \"CF_delta\": -2.02, \"E_F1_delta\": -0.73, \"R_F1_delta\": 1.14, \"note\": \"Greedy full_s1 998 docs: DR=10.21%, CF=2.57%, E_F1=59.37, R_F1=8.23. Beam eliminates ALL DR on DocRED 96-type schema.\"}}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/w9_qwen_docred_beam_50.jsonl\", \"log_path\": \"/root/schema_semantic_constrained_ie/outputs/w9_qwen_docred_beam_50.log\", \"completed_at\": \"2026-05-17T04:50:39.891Z\"}, \"w9_llama_scierc_beam_551\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T03:18:21.758Z\", \"updated_at\": \"2026-05-17T03:45:51.748Z\", \"hypothesis\": \"Beam search (k=4) with full_s1 constraints on Llama-3.1-8B SciERC 551 docs will show DR reduction similar to Qwen (0.93%→0%), confirming beam search compatibility is model-agnostic\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --beam_size 4 --output_path outputs/llama_scierc_beam_full_s1_551.jsonl\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"406047\", \"model_name\": \"Llama-3.1-8B-Instruct\", \"data_path\": \"data/scierc/test.json\", \"data_count\": 551, \"seed\": 42}, \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0.93, \"CF_count\": 15, \"E_F1\": 25.04, \"E_P\": 21.27, \"E_R\": 30.42, \"R_F1\": 3.33, \"R_P\": 2.68, \"R_R\": 4.41, \"total_entities\": 2398, \"total_relations\": 1606, \"parse_fail_rate\": 0, \"total_samples\": 551, \"vs_greedy_full_s1\": {\"DR_delta\": -0.08, \"CF_delta\": -5.63, \"E_F1_delta\": 1.55, \"R_F1_delta\": 0.79, \"note\": \"Greedy: DR=0.08%, CF=6.56%, E_F1=23.49%, R_F1=2.54%\"}}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/schema_constrained_ie/outputs/llama_scierc_beam_full_s1_551.jsonl\", \"log_path\": \"/root/autodl-tmp/schema_constrained_ie/outputs/llama_scierc_beam_full_s1_551.log\", \"completed_at\": \"2026-05-17T03:45:51.748Z\"}, \"posthoc_filtering_baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:46:07.823Z\", \"updated_at\": \"2026-05-17T02:56:24.306Z\", \"spec\": {\"hypothesis\": \"Post-hoc filtering baseline: generate unconstrained triples then remove DR/RV/ET violations. Comparison with OntoCoDec decoding-time enforcement on precision, recall, coverage, and residual violations.\", \"command\": \"python posthoc_filter.py\", \"server\": \"westd-16980\", \"data_path\": \"/root/schema_semantic_constrained_ie/outputs/\", \"data_count\": 2, \"model_name\": \"Qwen3-8B (unconstrained outputs)\", \"seed\": 42, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/posthoc_report_docred.json\", \"log_path\": \"/root/schema_semantic_constrained_ie/outputs/posthoc_report_scierc.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T18:46:23.429Z\", \"metrics\": {\"docred_f1_before\": 7.74, \"docred_f1_after\": 9.61, \"docred_precision_before\": 6.55, \"docred_precision_after\": 11.22, \"docred_recall_before\": 9.46, \"docred_recall_after\": 8.4, \"docred_rejection_rate\": 0.481, \"docred_tp_before\": 1137, \"docred_tp_after\": 1010, \"docred_tp_lost\": 127, \"docred_et_residual\": 0.0247, \"scierc_f1_before\": 8.23, \"scierc_f1_after\": 8.63, \"scierc_rejection_rate\": 0.168, \"scierc_recall_before\": 11.4, \"scierc_recall_after\": 10.68, \"scierc_tp_before\": 111, \"scierc_tp_after\": 104}, \"hypothesis\": \"Zero-shot unconstrained output 上跑 post-hoc filtering（规则删除违规三元组）作为 constrained decoding 的替代方案。预期 post-hoc 能消除 DR 但丢失有效三元组导致 recall 下降，证明解码时约束优于后处理。\", \"parent\": \"phase2_scierc_unconstrained\"}, \"phase2_scierc_full_s2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T00:36:35.941Z\", \"updated_at\": \"2026-05-17T02:56:23.629Z\", \"spec\": {\"command\": \"bash -c \\\"tmux kill-session -t phase2_scierc_full_s2 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s2 --dataset scierc --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/phase2_scierc_full_s2.jsonl --device cuda:0 --batch_size 1 --resume\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:1\"], \"pid\": \"unknown\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/phase2_scierc_full_s2.log\", \"submitted_at\": \"2026-05-14T01:07:00.401Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 368.6, \"gpu_hours\": 0.1}, \"hypothesis\": \"S2 两通道约束解码全量验证 — Grammar (Pass 1) + Semantic (Pass 2) 分离式约束。S2 pilot50 已验证 D/R violation=0%，全量运行检验 F1 稳定性和 per-relation 效果。与 S1 对比验证两种架构的 F1-violation trade-off。\", \"notes\": \"✅ 全量完成 551/551 via --resume. S2 两通道约束解码结果。DR=0.97% (vs S1 0.93%), RV=0%, ET=0%, R-F1=0.0803, E-F1=0.319.\", \"server\": \"westd-16980\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-16980\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-14T01:06:58.685Z\", \"command\": \"bash -c \\\"tmux kill-session -t phase2_scierc_full_s2 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s2 --dataset scierc --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/phase2_scierc_full_s2.jsonl --device cuda:0 --batch_size 1 --resume\\\"\", \"finished_at\": \"2026-05-14T01:13:08.809Z\", \"training_hours\": 0.1}, \"pid\": 144858, \"log_path\": \"~/runs/schema_semantic_constrained_ie/phase2_scierc_full_s2.log\", \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T01:13:09.036Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T01:13:12.640712+00:00\"}]}, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/phase2_scierc_full_s2.jsonl\", \"metrics\": {\"total_samples\": 551, \"total_triples\": 1644, \"total_entities\": 2228, \"json_parse_rate\": 1, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0, \"domain_range_violation_rate\": 0.0097, \"cross_field_consistency_violation_rate\": 0.0803, \"entity_precision\": 0.2797, \"entity_recall\": 0.3712, \"entity_f1\": 0.319, \"relation_precision\": 0.064, \"relation_recall\": 0.1078, \"relation_f1\": 0.0803, \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}, \"parent\": \"phase2_s2_pilot50\"}, \"llama_docred_unconstrained_mt6144\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T08:17:33.154Z\", \"updated_at\": \"2026-05-17T02:56:22.209Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode unconstrained --dataset docred --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/llama_docred_unconstrained_mt6144.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 6144\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"246947\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/llama_docred_unconstrained_mt6144.log\", \"submitted_at\": \"2026-05-15T08:19:27.565Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 20932.1, \"gpu_hours\": 5.81}, \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"pid\": \"246947\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/llama_docred_unconstrained_mt6144.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode unconstrained --dataset docred --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/llama_docred_unconstrained_mt6144.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 6144\\\"\", \"finished_at\": \"2026-05-15T13:59:24.508Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T13:59:25.767053+00:00\"}]}, \"metrics\": {\"ET_rate\": 0.13, \"RV_rate\": 15.89, \"DR_rate\": 26.18, \"DR_rate_eligible\": 31.15, \"CF_rate\": 0.17, \"entity_precision\": 61.19, \"entity_recall\": 51.06, \"entity_f1\": 55.67, \"relation_precision\": 5.18, \"relation_recall\": 7, \"relation_f1\": 5.95, \"parse_failures\": 67, \"documents_checked\": 931, \"total_documents\": 998, \"unique_entities\": 11534, \"total_triples\": 16584, \"dr_eligible_triples\": 13936, \"fuzzy_relation_matches\": 121}, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/llama_docred_unconstrained_mt6144.jsonl\", \"notes\": \"mt6144 vs mt4096 对比: parse_failures 68→67 (-1, 几乎无变化); unique_entities 11525→11534 (+9); triples 16437→16584 (+147, +0.9%); E-F1 55.65%→55.67% (+0.02pp); R-F1 5.98%→5.95% (-0.03pp); DR 26.07%→26.18% (+0.11pp); RV 16.03%→15.89% (-0.14pp); ET/CF 不变. 67 个 FAIL 中绝大多数 inference time ~96s (仍触发 max_tokens cap), 说明这些失败主要源于模型陷入重复循环直到 token 上限, 而非文档过长. 增加 max_new_tokens 不能挽救此类失败. 训练 wall clock 约 5h39m, 比 mt4096 (~5h02m) 多约 37 分钟. 结论: max_new_tokens 4096→6144 对 unconstrained 生成无实质影响, 不建议采用作为后续 baseline.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T14:08:19.680Z\", \"hypothesis\": \"Llama DocRED unconstrained max_tokens=6144 重跑，消除输出截断。预期三元组产出量增加，violation profile 可能因完整输出而变化，为 constrained 对比提供公平 baseline。\", \"parent\": \"llama_docred_unconstrained\"}, \"llama_docred_full_s1_mt6144\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-15T08:17:36.675Z\", \"updated_at\": \"2026-05-17T02:56:21.312Z\", \"server\": \"westd-16980\", \"gpu\": \"cuda:1\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/llama_docred_full_s1_mt6144.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 6144\\\"\", \"finished_at\": \"2026-05-15T14:59:20.782Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-15T08:19:51.861Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T08:19:53.379823+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T14:59:25.181921+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/llama_docred_full_s1_mt6144.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 6144\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:1\"], \"pid\": \"247487\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/llama_docred_full_s1_mt6144.log\", \"submitted_at\": \"2026-05-15T08:22:03.222Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 24176.2, \"gpu_hours\": 6.72}, \"pid\": \"247487\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/llama_docred_full_s1_mt6144.log\", \"notes\": \"⚠️ 变量混淆：此实验同时包含 CF fallback 代码修改 + max_tokens 6144（两个变量）。CF 数据可作为 'Llama DocRED with fallback + mt6144' 参考点，但不能用于纯 CF ablation 对比。纯 CF ablation 必须控制 max_tokens=4096。unconstrained_mt6144 不受影响（不走 semantic layer）。\", \"metrics\": {\"DR_rate_pct\": 2.57, \"RV_rate_pct\": 0, \"ET_rate_pct\": 0, \"CF_rate_pct\": 12.13, \"R_F1\": 6.25, \"R_precision\": 5.45, \"R_recall\": 7.32, \"E_F1\": 55.04, \"E_precision\": 61.41, \"E_recall\": 49.87, \"documents_total\": 998, \"documents_checked\": 908, \"parse_failures\": 90, \"triples\": 16471, \"unique_entities\": 11307, \"fallback_events\": 67911, \"wall_clock_seconds\": 23926, \"vs_unconstrained_mt6144\": {\"DR_delta_pp\": -23.61, \"DR_reduction_pct\": -90.2, \"R_F1_delta_pp\": 0.3, \"E_F1_delta_pp\": -0.63}, \"vs_full_s1_mt4096\": {\"DR_delta_pp\": 0.02, \"R_F1_delta_pp\": -0.02, \"E_F1_delta_pp\": 0.03, \"CF_delta_pp\": 0.11, \"parse_fail_delta\": -1}}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/llama_docred_full_s1_mt6144.jsonl\", \"hypothesis\": \"Llama DocRED full_s1 max_tokens=6144 重跑，消除原实验输出截断。若截断导致丢失有效三元组，预期 R-F1 提升；DR 应维持近 0%。\", \"parent\": \"llama_docred_full_s1\"}, \"beam_search_scierc_full_551\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T00:42:41.314Z\", \"updated_at\": \"2026-05-17T02:56:20.332Z\", \"hypothesis\": \"Beam search (size=4) with OntoCoDec constraints on SciERC full set will maintain DR≈0% (as seen in 50-doc dry-run) while improving F1 over greedy, demonstrating decoding-strategy-agnostic constraint enforcement\", \"spec\": {\"command\": \"python run_constrained_extraction.py --decoding_strategy beam --num_beams 4 --constraint_mode full_s1 (SciERC 551 docs)\", \"server\": \"westd-16980\", \"data_path\": \"SciERC test set\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"gpu\": \"cuda:0\", \"pid\": \"399097\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"westd-16980:/root/schema_semantic_constrained_ie/outputs/beam_search_scierc_full_551.jsonl\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T01:43:45.104Z\", \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0.53, \"E_F1\": 32, \"R_F1\": 8.56, \"E_P\": 26.83, \"E_R\": 39.63, \"R_P\": 6.69, \"R_R\": 11.91, \"parse_fail_rate\": 0, \"total_entities\": 2476, \"total_relations\": 1737}, \"parent\": \"phase2_scierc_full_s1\"}, \"w8_llama_docred_ft_grammar_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T06:34:25.909Z\", \"updated_at\": \"2026-05-17T02:56:19.388Z\", \"hypothesis\": \"FT Llama DocRED + grammar_only eval: FT 后 DR 残留 0.49%，grammar_only 能消除多少？如果 grammar_only 已足够则 semantic 层在 FT regime 边际价值小；如果不够则两层在 FT 后仍互补。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode grammar_only --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w8_llama_docred_ft_grammar_only.jsonl --batch_size 1 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"llama_lora_docred_merged\", \"seed\": 42, \"checkpoint_source\": \"w5_llama_docred_lora\", \"eval_data\": \"docred_dev_998\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"log_path\": \"/tmp/w8_llama_docred_ft_grammar_only.log\", \"completed_at\": \"2026-05-16T12:31:33.933Z\", \"metrics\": {\"E_F1\": 84.04, \"R_F1\": 43.77, \"entity_precision\": 84.99, \"entity_recall\": 83.11, \"relation_precision\": 38.6, \"relation_recall\": 50.53, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.51, \"CF_pct\": 0.12, \"parse_fail_rate\": 2.3, \"total_samples\": 998, \"total_relations\": 16199, \"unique_entities\": 13225, \"parse_failures\": 23}, \"parent\": \"w5_llama_docred_lora_training\"}, \"w7_llama_scierc_ft_semantic_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T05:47:04.863Z\", \"updated_at\": \"2026-05-17T02:56:17.967Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py --mode semantic_only --dataset scierc --model_path /root/autodl-tmp/checkpoints/llama_lora_scierc_merged --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/w7_llama_scierc_ft_semantic_only.jsonl --batch_size 1 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"gpu\": 0, \"model_name\": \"Llama-3.1-8B-LoRA-SciERC\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_scierc_merged\", \"pid\": 344026, \"log_path\": \"/tmp/w7_llama_scierc_ft_semantic_only.log\"}, \"hypothesis\": \"FT Llama + semantic-only ablation on SciERC: isolate semantic layer contribution in FT regime. Semantic层单独能否消除DR? 与grammar_only对比揭示两层各自贡献。\", \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.65, \"CF_count\": 2, \"E_F1\": 67.76, \"E_P\": 66.47, \"E_R\": 69.1, \"R_F1\": 45.47, \"R_P\": 43.24, \"R_R\": 47.95, \"total_entities\": 1757, \"total_relations\": 1081, \"json_parse_failures\": 0}, \"checkpoint_path\": \"outputs/w7_llama_scierc_ft_semantic_only.jsonl\", \"notes\": \"551/551 完成。Semantic-only 在 FT Llama 上: DR=0.65% (vs unconstrained 1.11%, grammar_only 1.11%, full_s1 0.09%)。Semantic 约束单独将 DR 降低 42%，但不如 full_s1 的 grammar+semantic 联合约束。R_F1=45.47% 与 baseline 持平，无质量损失。CF=2 是新增的 cross-field 一致性问题。\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T08:32:01.872Z\", \"parent\": \"w5_llama_lora_scierc_unconstrained_eval\"}, \"w7_llama_scierc_ft_grammar_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T05:47:02.522Z\", \"updated_at\": \"2026-05-17T02:56:17.093Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py --mode grammar_only --dataset scierc --model_path /root/autodl-tmp/checkpoints/llama_lora_scierc_merged --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/w7_llama_scierc_ft_grammar_only.jsonl --batch_size 1 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"gpu\": 0, \"model_name\": \"Llama-3.1-8B-LoRA-SciERC\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_scierc_merged\", \"pid\": 342707, \"log_path\": \"/tmp/w7_llama_scierc_ft_grammar_only.log\"}, \"hypothesis\": \"FT Llama + grammar-only ablation on SciERC: isolate grammar layer contribution in FT regime. FT已修复RV/ET(均0%), DR残留1.11%. Grammar-only能否消除DR?\", \"metrics\": {\"total_samples\": 551, \"json_parse_failures\": 0, \"total_entities\": 1757, \"total_relations\": 1082, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0, \"domain_range_violation_rate\": 0.0111, \"cross_field_consistency_violation_rate\": 0, \"entity_f1\": {\"precision\": 0.6647, \"recall\": 0.691, \"f1\": 0.6776}, \"relation_f1\": {\"precision\": 0.432, \"recall\": 0.4795, \"f1\": 0.4545}}, \"checkpoint_path\": \"outputs/w7_llama_scierc_ft_grammar_only.jsonl\", \"log_path\": \"/tmp/w7_llama_scierc_ft_grammar_only.log\", \"notes\": \"551/551 complete. As expected, grammar_only does not reduce DR (1.11% same as unconstrained FT baseline). ET=0%, RV=0%, CF=0% all clean. F1 slightly better than Qwen FT grammar_only (E_F1=0.6776 vs 0.6705, R_F1=0.4545 vs 0.4386).\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T07:49:15.016Z\", \"parent\": \"w5_llama_lora_scierc_unconstrained_eval\"}, \"w7_qwen_scierc_ft_semantic_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T05:46:59.364Z\", \"updated_at\": \"2026-05-17T02:56:16.228Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py --mode semantic_only --dataset scierc --model_path /root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/w7_qwen_scierc_ft_semantic_only.jsonl --batch_size 1 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"gpu\": 0, \"model_name\": \"Qwen3-8B-LoRA-SciERC\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged\", \"pid\": 340898, \"log_path\": \"/tmp/w7_qwen_scierc_ft_semantic_only.log\"}, \"hypothesis\": \"FT Qwen + semantic-only ablation on SciERC: isolate semantic layer contribution in FT regime. Semantic层单独能否消除DR? 与grammar_only对比揭示两层各自贡献。\", \"conclusion\": \"success\", \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.6, \"CF_count\": 15, \"parse_fail_rate\": 0, \"total_samples\": 551, \"total_entities\": 1784, \"total_relations\": 1128, \"E_P\": 0.6523, \"E_R\": 0.6898, \"E_F1\": 0.6705, \"R_P\": 0.4073, \"R_R\": 0.4713, \"R_F1\": 0.4369, \"DR_violations\": 7, \"delta_vs_grammar_only\": {\"DR_delta\": -1.3, \"note\": \"semantic_only DR=0.6% vs grammar_only DR=1.9%, semantic layer reduces DR by 68%\"}, \"delta_vs_unconstrained\": {\"DR_delta\": -1.35, \"note\": \"unconstrained DR=1.95% → semantic_only 0.6%\"}}, \"checkpoint_path\": \"outputs/w7_qwen_scierc_ft_semantic_only.jsonl\", \"completed_at\": \"2026-05-16T07:25:31.487Z\", \"notes\": \"551/551 完成。Semantic-only 在 FT Qwen 上: DR 1.95%→0.6% (−68%), ET/RV=0%。CF=15（grammar 层对 CF 有抑制作用）。F1 与 grammar_only 几乎一致 (R_F1=0.4369 vs 0.4386)。Ablation 结论: grammar 层消除 RV/ET，semantic 层消除 DR。两层互补，缺一不可——grammar_only DR=1.9%(未降)，semantic_only DR=0.6%(降68%)，full_s1 DR=0%(完全消除)。\", \"parent\": \"w5_lora_scierc_unconstrained_eval\"}, \"w7_qwen_scierc_ft_grammar_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T05:46:56.566Z\", \"updated_at\": \"2026-05-17T02:56:15.201Z\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode grammar_only --dataset scierc --model_path /root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/w7_qwen_scierc_ft_grammar_only.jsonl --batch_size 1 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"gpu\": 0, \"model_name\": \"Qwen3-8B-LoRA-SciERC\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged\", \"pid\": 337069, \"log_path\": \"~/runs/schema_semantic_constrained_ie/w7_qwen_scierc_ft_grammar_only.log\"}, \"hypothesis\": \"FT Qwen + grammar-only ablation on SciERC: isolate grammar layer contribution in FT regime. FT已修复RV/ET(均0%), DR残留1.95%. Grammar-only能否消除DR?\", \"reproduce\": {\"finished_at\": \"2026-05-16T06:41:42.468Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T06:41:43.361Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T06:41:45.053980+00:00\"}]}, \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 1.9, \"CF_pct\": 0, \"parse_fail_rate\": 0, \"total_samples\": 551, \"total_entities\": 1784, \"total_relations\": 1128, \"E_P\": 0.6523, \"E_R\": 0.6898, \"E_F1\": 0.6705, \"R_P\": 0.4087, \"R_R\": 0.4733, \"R_F1\": 0.4386, \"DR_violations\": 22, \"tokenizer_warning\": \"false_positive_transformers_4.57.6\"}, \"notes\": \"551/551 完成。Grammar-only 在 FT Qwen 上: ET/RV/CF 全部清零，DR 残留 1.9% (22/1128)——与 unconstrained (1.95%) 几乎一致，说明 grammar 层不约束 DR，DR 消除完全依赖 semantic 层。E_F1=0.6705, R_F1=0.4386 与 unconstrained 持平。Tokenizer regex 警告为 transformers 4.57.6 false positive (Reviewer PASS)。\", \"parent\": \"w5_lora_scierc_unconstrained_eval\"}, \"w5_llama_lora_scierc_unconstrained_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:33:40.179Z\", \"updated_at\": \"2026-05-17T02:56:13.750Z\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode unconstrained --dataset scierc --model_path checkpoints/llama_lora_scierc_merged --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/w5_llama_lora_scierc_unconstrained.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"287667\", \"log_path\": \"/root/schema_semantic_constrained_ie/outputs/w5_llama_lora_scierc_unconstrained.jsonl\", \"submitted_at\": \"2026-05-15T17:19:48.001Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 100, \"model_name\": \"Meta-Llama-3.1-8B-Instruct-LoRA-SciERC\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_scierc_merged\", \"eval_data\": \"data/processed_data/test.json\", \"parent\": \"w5_llama_lora_scierc_training\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/llama_lora_scierc_merged\", \"wall_clock_seconds\": 271.9, \"gpu_hours\": 0.08}, \"hypothesis\": \"Fine-tuned Llama-3.1-8B SciERC unconstrained eval — 验证 LoRA 后残余 DR 是否仍 >2%，决定 OntoCoDec 在 fine-tuned Llama 上的 composability 价值。\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T17:24:19.934Z\", \"metrics\": {\"total_samples\": 551, \"total_entities\": 1757, \"total_relations\": 1082, \"json_parse_rate\": 1, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0, \"domain_range_violation_rate\": 0.0111, \"cross_field_consistency_violation_rate\": 0, \"total_violation_rate\": 0.0042, \"entity_precision\": 0.6647, \"entity_recall\": 0.691, \"entity_f1\": 0.6776, \"relation_precision\": 0.432, \"relation_recall\": 0.4795, \"relation_f1\": 0.4545}, \"parent\": \"w5_llama_lora_scierc_training\"}, \"w5_llama_lora_scierc_constrained_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:33:42.462Z\", \"updated_at\": \"2026-05-17T02:56:12.734Z\", \"spec\": {\"command\": \"cd /root/schema_semantic_constrained_ie && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/checkpoints/llama_lora_scierc_merged --data_path data/processed_data/test.json --constraint_path ontology_constraints.json --output_path outputs/w5_llama_lora_scierc_constrained.jsonl --mode full_s1\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:1\"], \"pid\": \"290317\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w5_llama_lora_scierc_constrained_eval.log\", \"submitted_at\": \"2026-05-15T17:38:56.723Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"llama-3.1-8b-instruct-lora-scierc-merged\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_scierc_merged\", \"eval_data\": \"SciERC test set (551 samples)\", \"wall_clock_seconds\": 2003.1, \"gpu_hours\": 0.56}, \"hypothesis\": \"Fine-tuned Llama-3.1-8B + OntoCoDec constrained eval on SciERC — composability 验证：约束解码在 fine-tuned Llama 上仍有效且不损 F1。完成 Llama SciERC 2×2 matrix。\", \"reproduce\": {\"finished_at\": \"2026-05-15T17:59:25.871Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:59:27.794917+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"domain_range_violation_rate\": 0.0009, \"relation_vocabulary_violation_rate\": 0, \"entity_type_violation_rate\": 0, \"cross_field_consistency_violation_rate\": 0.0046, \"relation_f1\": 0.4547, \"relation_precision\": 0.432, \"relation_recall\": 0.4795, \"entity_f1\": 0.6776, \"entity_precision\": 0.6647, \"entity_recall\": 0.691, \"total_relations\": 1081, \"total_entities\": 1757, \"total_samples\": 551, \"parse_failures\": 0}, \"checkpoint_path\": \"outputs/w5_llama_lora_scierc_constrained.jsonl\", \"completed_at\": \"2026-05-15T18:12:19.787Z\", \"parent\": \"w5_llama_lora_scierc_training\"}, \"w5_lora_scierc_constrained_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:57:42.154Z\", \"updated_at\": \"2026-05-17T02:56:11.350Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path checkpoints/qwen3_8b_lora_scierc_merged --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/w5_lora_scierc_full_s1_eval.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 2048\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"282127\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w5_lora_scierc_constrained_eval.log\", \"submitted_at\": \"2026-05-15T15:58:03.052Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1664.8, \"gpu_hours\": 0.46}, \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"pid\": \"282127\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w5_lora_scierc_constrained_eval.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path checkpoints/qwen3_8b_lora_scierc_merged --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/w5_lora_scierc_full_s1_eval.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 2048\\\"\", \"finished_at\": \"2026-05-15T16:22:21.690Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:22:23.113142+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"json_parse_rate\": 1, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0, \"domain_range_violation_rate\": 0, \"cross_field_consistency_violation_rate\": 0.0118, \"entity_f1\": 0.6705, \"entity_precision\": 0.6523, \"entity_recall\": 0.6898, \"relation_f1\": 0.4377, \"relation_precision\": 0.4078, \"relation_recall\": 0.4723, \"total_entities\": 1784, \"total_relations\": 1128, \"total_samples\": 551, \"cross_field_consistency_violations\": 21}, \"hypothesis\": \"Fine-tuning + constrained decoding composability: 约束解码在 fine-tuned 模型上仍有效，且不显著损害 F1\", \"checkpoint_path\": \"checkpoints/qwen3_8b_lora_scierc_merged\", \"completed_at\": \"2026-05-15T16:25:47.858Z\", \"parent\": \"w5_lora_scierc_training\"}, \"w1_cf_fallback_scierc_pilot\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:32:48.425Z\", \"updated_at\": \"2026-05-17T02:56:05.216Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/w1_cf_fallback_scierc_pilot.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 2048\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"270088\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w1_cf_fallback_scierc_pilot.log\", \"submitted_at\": \"2026-05-15T14:07:14.512Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 2999.4, \"gpu_hours\": 0.83}, \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"pid\": \"270088\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w1_cf_fallback_scierc_pilot.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/w1_cf_fallback_scierc_pilot.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 2048\\\"\", \"finished_at\": \"2026-05-15T14:47:53.690Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T14:47:54.986519+00:00\"}]}, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/w1_cf_fallback_scierc_pilot.jsonl\", \"metrics\": {\"ET\": 0, \"RV\": 0, \"DR\": 0.1478, \"CF\": 0.0004, \"R_F1\": 0.0823, \"R_P\": 0.0643, \"R_R\": 0.114, \"E_F1\": 0.3098, \"E_P\": 0.2598, \"E_R\": 0.3837, \"entities\": 2474, \"relations\": 1725, \"samples\": 551, \"grammar_first_fallback_rate\": 0.3664, \"cf_registry_fallback_rate\": 0.0448, \"total_mask_calls\": 17024, \"violation_budget_DR_CF\": 0.1482}, \"notes\": \"CF fallback 实验在 SciERC + Qwen3-8B 上的 pilot 结果：CF 从 9.90% 下降到 0.04% (-9.86pp)，但 DR 从 0.93% 上升到 14.78% (+13.85pp)。DR+CF budget 净增 +3.99pp。F1 几乎不变 (E-F1=30.98% 与 baseline 完全一致；R-F1=8.23%, -0.13pp)。Grammar-first fallback 触发率 36.64% (6237/17024 mask calls)，CF-registry fallback 4.48%。判定：成功降低 CF 但代价是 DR 大幅恶化，违规没有真正减少，只是从 CF 转移到 DR。建议改进方向：(1) 仅在 CF-registry 命中时回退，保留 DR enforcement；(2) rebuttal 中诚实呈现这是 violation re-routing 而非 reduction。详细报告见 artifact w1_cf_fallback_scierc_pilot_analysis。\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T14:57:13.885Z\", \"hypothesis\": \"Constrained fallback (CF) 策略 SciERC pilot：约束解码产生空输出时回退至 unconstrained 生成，预期降低空输出率同时维持 violation 控制。若 fallback 频率过高则 CF 策略不可行。\"}, \"w5_lora_scierc_training\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-15T14:56:20.233Z\", \"updated_at\": \"2026-05-17T02:55:56.797Z\", \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"command\": \"bash -c \\\"export WANDB_MODE=disabled && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 scripts/train_lora_scierc.py\\\"\", \"finished_at\": \"2026-05-15T15:16:50.985Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-15T14:58:56.873Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T14:58:58.618383+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T15:16:52.498789+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"bash -c \\\"export WANDB_MODE=disabled && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 scripts/train_lora_scierc.py\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"276523\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w5_lora_scierc_training.log\", \"submitted_at\": \"2026-05-15T15:02:11.699Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/checkpoints/qwen3_8b_lora_scierc\", \"wall_clock_seconds\": 1068.6, \"gpu_hours\": 0.3}, \"pid\": \"276523\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w5_lora_scierc_training.log\", \"metrics\": {\"train_loss\": 0.0634, \"eval_loss\": 0.0586, \"eval_token_accuracy\": 0.9816, \"eval_entropy\": 0.9635, \"train_runtime_sec\": 688.4, \"epochs\": 3, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/checkpoints/qwen3_8b_lora_scierc\", \"merged_model_path\": \"/root/schema_semantic_constrained_ie/checkpoints/qwen3_8b_lora_scierc_merged\"}, \"conclusion\": \"success\", \"hypothesis\": \"Qwen3-8B LoRA fine-tune on SciERC 建立 fine-tuned baseline，用于 composability 验证。预期 E-F1/R-F1 大幅提升但残余 DR>0%，证明 FT 后 OntoCoDec 约束解码仍有价值。\"}, \"w8_llama_docred_ft_semantic_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T10:54:02.910Z\", \"updated_at\": \"2026-05-16T16:55:22.088Z\", \"hypothesis\": \"FT Llama DocRED + semantic_only eval: 与 grammar_only 配对，验证 semantic 层在 FT+DocRED regime 下能否独立降低 DR。预期 DR 从 0.49% 降至 ~0.2-0.3%（参照 SciERC 模式：semantic_only 降 DR 42%）。完成后 DocRED FT ablation 有 Llama 双模式数据，2 模型 ×2 模式全部完备。\", \"parent\": \"w5_llama_docred_lora_training\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode semantic_only --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w8_llama_docred_ft_semantic_only.jsonl --batch_size 1 --max_new_tokens 4096\\\"\", \"server\": \"westd-16980\", \"gpu\": 1, \"pid\": 361202, \"model_name\": \"Llama-3.1-8B-LoRA-DocRED\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T16:49:59.199Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T16:50:01.253379+00:00\"}]}, \"metrics\": {\"E_F1\": 84.02, \"E_P\": 85.01, \"E_R\": 83.06, \"R_F1\": 43.9, \"R_P\": 38.89, \"R_R\": 50.4, \"ET_pct\": 0, \"RV_pct\": 0.15, \"DR_pct\": 0.3, \"CF_pct\": 0.16, \"parse_fail_rate\": 2.4, \"total_samples\": 998, \"parse_failures\": 24, \"documents_checked\": 974, \"total_entities\": 19099, \"total_relations\": 16038, \"DR_violations\": 48, \"RV_violations\": 24, \"ET_violations\": 0, \"CF_violations\": 31}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"log_path\": \"outputs/w8_llama_docred_ft_semantic_only.jsonl\", \"completed_at\": \"2026-05-16T16:55:22.088Z\"}, \"w8_qwen_docred_ft_semantic_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T10:08:59.297Z\", \"updated_at\": \"2026-05-16T16:22:28.075Z\", \"hypothesis\": \"FT Qwen DocRED + semantic_only eval: 与 grammar_only 配对，验证 semantic 层在 FT+DocRED regime 下能否独立降低 DR。预期 DR 从 0.76% 降至 ~0.3-0.5%（参照 SciERC 模式：semantic_only 降 DR 68%��。完成后 DocRED FT ablation 有 Qwen 双模式数据。\", \"parent\": \"w5_qwen_docred_lora_training\", \"spec\": {\"command\": \"python run_constrained_extraction.py --mode semantic_only --dataset docred --model /root/autodl-tmp/checkpoints/qwen_lora_docred_merged\", \"server\": \"westd-21461\", \"data_path\": \"data/docred\", \"data_count\": 998, \"model_name\": \"qwen_lora_docred_merged\", \"seed\": 42, \"checkpoint_source\": \"qwen_lora_docred_merged\", \"eval_data\": \"docred_test_998\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/qwen_lora_docred_merged\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w8_qwen_docred_ft_semantic_only.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T16:18:27.113Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T16:18:29.130284+00:00\"}]}, \"metrics\": {\"E_F1\": 82.15, \"E_P\": 85.58, \"E_R\": 78.99, \"R_F1\": 40.89, \"R_P\": 36.35, \"R_R\": 46.73, \"ET_pct\": 0, \"RV_pct\": 0.23, \"DR_pct\": 0.21, \"CF_pct\": 0.27, \"parse_fail_rate\": 7.52, \"total_samples\": 998, \"parse_failures\": 75, \"documents_checked\": 923, \"total_entities\": 18025, \"total_triples\": 15909, \"DR_violations\": 34, \"RV_violations\": 37, \"ET_violations\": 0, \"CF_violations\": 49}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T16:22:28.075Z\"}, \"w8_qwen_docred_ft_grammar_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T09:13:03.945Z\", \"updated_at\": \"2026-05-16T15:25:52.761Z\", \"hypothesis\": \"FT Qwen DocRED + grammar_only eval: FT 后 DR 残留 0.76%，grammar_only 能消除多少？与 w8_llama_docred_ft_grammar_only 配对，补全 DocRED FT ablation 两模型对比。预期 DR≈0.76%（与 SciERC 模式一致：grammar 层不约束 DR）。\", \"parent\": \"w5_qwen_docred_lora_training\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode grammar_only --dataset docred --model_path /root/autodl-tmp/checkpoints/qwen_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w8_qwen_docred_ft_grammar_only.jsonl --batch_size 1 --max_new_tokens 4096\\\"\", \"server\": \"westd-21461\", \"gpu\": 0, \"pid\": 18555, \"log_path\": \"~/runs/schema_semantic_constrained_ie/w8_qwen_docred_ft_grammar_only.log\", \"submitted_at\": \"2026-05-16T09:27:52.393Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen3-8B-LoRA-DocRED\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/qwen_lora_docred_merged\", \"log_path_final\": \"~/runs/schema_semantic_constrained_ie/w8_qwen_docred_ft_grammar_only.log\", \"wall_clock_seconds\": 21480.4, \"gpu_hours\": 5.97}, \"reproduce\": {\"finished_at\": \"2026-05-16T15:20:38.652Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T15:20:40.840918+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"E_F1\": 82.19, \"E_P\": 85.47, \"E_R\": 79.16, \"R_F1\": 40.85, \"R_P\": 36.27, \"R_R\": 46.77, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.61, \"CF_pct\": 0.11, \"parse_fail_rate\": 7.01, \"total_samples\": 998, \"parse_failures\": 70}, \"completed_at\": \"2026-05-16T15:25:52.761Z\"}, \"w6_mistral_scierc_unconstrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T02:59:02.565Z\", \"updated_at\": \"2026-05-16T10:41:37.382Z\", \"hypothesis\": \"Mistral (3rd model) SciERC unconstrained baseline — 获取 zero-shot violation profile (DR/RV/ET) 和 F1，验证 OntoCoDec 三模型泛化性\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode unconstrained --dataset scierc --model_path /root/autodl-tmp/models/Mistral-7B-Instruct-v0.3 --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/w6_mistral_scierc_unconstrained.jsonl --batch_size 1 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"gpu\": 0, \"pid\": 332156, \"log_path\": \"~/runs/schema_semantic_constrained_ie/w6_mistral_scierc_unconstrained.log\", \"submitted_at\": \"2026-05-16T04:53:56.502Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Mistral-7B-Instruct-v0.3\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"seed\": 42, \"wall_clock_seconds\": 2104.7, \"gpu_hours\": 0.58, \"checkpoint_path\": \"N/A\"}, \"notes\": \"Mistral-7B unconstrained SciERC: E_F1=0.2728, R_F1=0.0366. 0% parse failures. 56.94% dangling relations, 1.5% ET violations, 0% RV violations. Poor IE performance typical of unconstrained 7B model on SciERC.\", \"reproduce\": {\"finished_at\": \"2026-05-16T05:27:35.554Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T05:27:39.086911+00:00\"}]}, \"metrics\": {\"E_P\": 0.2402, \"E_R\": 0.3156, \"E_F1\": 0.2728, \"R_P\": 0.0295, \"R_R\": 0.0483, \"R_F1\": 0.0366, \"ET_pct\": 1.5, \"RV_pct\": 0, \"DR_pct\": 56.94, \"CF_pct\": 56.87, \"parse_fail_rate\": 0, \"total_samples\": 551, \"total_pred_entities\": 2202, \"total_pred_relations\": 1593}, \"conclusion\": \"success\", \"checkpoint_path\": \"outputs/w6_mistral_scierc_unconstrained.jsonl\", \"completed_at\": \"2026-05-16T05:29:01.251Z\"}, \"w6_mistral_scierc_constrained\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-16T02:59:03.181Z\", \"updated_at\": \"2026-05-16T10:40:00.429Z\", \"hypothesis\": \"Mistral-7B constrained SciERC (full_s1 mode) - test if schema constraints reduce violations and improve F1 vs unconstrained baseline (E_F1=0.2728, R_F1=0.0366, DR=56.94%)\", \"failure_reason\": \"TypeError: xgrammar.GrammarMatcher.accept_token expected int but got ffi.Tensor. xgrammar/tvm version mismatch on westd-21461. Crashed 10s after start.\", \"completed_at\": \"2026-05-16T05:28:06.343Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/Mistral-7B-Instruct-v0.3 --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/w6_mistral_scierc_constrained.jsonl --batch_size 1 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"gpu\": 0, \"model_name\": \"Mistral-7B-Instruct-v0.3\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"seed\": 42, \"pid\": 334606, \"log_path\": \"~/runs/schema_semantic_constrained_ie/w6_mistral_scierc_constrained.log\"}, \"metrics\": {\"E_P\": 0.2437, \"E_R\": 0.3144, \"E_F1\": 0.2746, \"R_P\": 0.0292, \"R_R\": 0.0493, \"R_F1\": 0.0367, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 13.4, \"CF_pct\": 1.27, \"CF_count\": 21, \"parse_fail_rate\": 0, \"total_samples\": 551, \"total_pred_entities\": 2162, \"total_pred_relations\": 1647, \"delta_vs_unconstrained\": {\"delta_E_F1\": 0.0018, \"delta_R_F1\": 0.0001, \"delta_ET\": -1.5, \"delta_RV\": 0, \"delta_DR\": -43.54, \"note\": \"Constrained - unconstrained. Baseline: E_F1=0.2728, R_F1=0.0366, DR=56.94%, ET=1.5%, RV=0%\"}}, \"notes\": \"Mistral-7B constrained SciERC: 551/551 complete, 0 failures. OntoCoDec eliminated ET (1.5%→0%) and RV (0%→0%), reduced DR massively (56.94%→13.4%, -43.54pp). F1 unchanged (E_F1=0.2746 vs 0.2728, R_F1=0.0367 vs 0.0366). Residual DR 13.4% much higher than FT models (~1-2%), consistent with zero-shot regime needing stronger semantic constraints.\", \"conclusion\": \"success\", \"checkpoint_path\": \"N/A\"}, \"w8_ft_posthoc_baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T06:34:25.203Z\", \"updated_at\": \"2026-05-16T09:35:31.720Z\", \"hypothesis\": \"FT 后 DR<2%，post-hoc filtering 能否替代 OntoCoDec？对 4 组 FT unconstrained output 跑 posthoc_filter.py，量化 recall 损失和 coverage 代价。预期：post-hoc 过滤虽消除 DR 但丢失 TP（recall 下降），证明 constrained decoding 的 generation-time 优势。\", \"conclusion\": \"success\", \"metrics\": {\"ft_regime\": {\"qwen_scierc\": {\"R_F1_before\": 43.86, \"R_F1_posthoc\": 43.94, \"R_F1_constrained\": 43.77, \"reject_rate_pct\": 1.95, \"TP_lost\": 4}, \"llama_scierc\": {\"R_F1_before\": 45.45, \"R_F1_posthoc\": 45.23, \"R_F1_constrained\": 45.47, \"reject_rate_pct\": 1.11, \"TP_lost\": 5}, \"qwen_docred\": {\"R_F1_before\": 40.91, \"R_F1_posthoc\": 41.11, \"R_F1_constrained\": \"TBD\", \"reject_rate_pct\": 1.03, \"TP_lost\": 1}, \"llama_docred\": {\"R_F1_before\": 43.77, \"R_F1_posthoc\": 43.92, \"R_F1_constrained\": 44.23, \"reject_rate_pct\": 0.64, \"TP_lost\": 1}}, \"zs_regime\": {\"mistral_scierc\": {\"triples\": 1584, \"reject_pct\": 20.27, \"R_F1_before\": 0.0376, \"R_F1_posthoc\": 0.0394, \"R_F1_constrained\": 0.0367, \"TP_before\": 48, \"TP_after\": 44, \"TP_lost\": 4}, \"qwen_scierc\": {\"triples\": 1724, \"reject_pct\": 16.76, \"R_F1_before\": 0.0823, \"R_F1_posthoc\": 0.0863, \"R_F1_constrained\": 0.0836, \"TP_before\": 111, \"TP_after\": 104, \"TP_lost\": 7}, \"llama_scierc\": {\"triples\": 1274, \"reject_pct\": 13.89, \"R_F1_before\": 0.0268, \"R_F1_posthoc\": 0.0271, \"R_F1_constrained\": 0.0254, \"TP_before\": 30, \"TP_after\": 28, \"TP_lost\": 2}, \"qwen_docred\": {\"triples\": 17497, \"reject_pct\": 48.12, \"R_F1_before\": 0.0774, \"R_F1_posthoc\": 0.0961, \"R_F1_constrained\": 0.0823, \"TP_before\": 1137, \"TP_after\": 1010, \"TP_lost\": 127}, \"llama_docred\": {\"triples\": 16437, \"reject_pct\": 42.18, \"R_F1_before\": 0.0598, \"R_F1_posthoc\": 0.0744, \"R_F1_constrained\": 0.0627, \"TP_before\": 850, \"TP_after\": 802, \"TP_lost\": 48}, \"mistral_docred\": {\"triples\": 11836, \"reject_pct\": 73.73, \"R_F1_before\": 0.0434, \"R_F1_posthoc\": 0.0385, \"R_F1_constrained\": 0.0552, \"TP_before\": 518, \"TP_after\": 292, \"TP_lost\": 226, \"removed_RV\": 4172, \"removed_ET\": 3382, \"removed_DR\": 1173, \"note\": \"Only ZS case where posthoc HURTS R_F1 — 73.7% rejection rate loses 43.6% of TPs\"}}, \"key_finding\": \"ZS: post-hoc R_F1 >= constrained R_F1 in 5/6 groups. Exception: Mistral DocRED where extreme rejection rate (73.7%) causes net F1 loss. Constrained decoding value is in structural guarantee (0% violations) and composability, not F1 preservation.\"}, \"notes\": \"零样本 + FT 两组 post-hoc baseline 完成。关键发现：ZS 下 post-hoc R_F1 在全部 5 组中 ≥ constrained R_F1（Qwen DocRED 差距最大 +1.38pp）。原因：post-hoc 删除大量 FP 提升 precision，recall 损失有限（TP_lost 仅占 rejected 的 1-2%）。constrained decoding 在 ZS 下强制约束干扰模型分布，总体 F1 反而略低。论文论点需调整：constrained decoding 的 ZS 价值不在 \\\"F1 保留\\\" 而在 \\\"生成时硬保证 0% violations + composability\\\"。\", \"checkpoint_path\": \"N/A (CPU-only analysis, no checkpoint)\", \"log_path\": \"N/A (CPU-only analysis)\", \"completed_at\": \"2026-05-16T09:35:31.720Z\"}, \"w6_mistral_docred_unconstrained\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-16T02:59:03.876Z\", \"updated_at\": \"2026-05-16T09:28:49.721Z\", \"hypothesis\": \"Mistral (3rd model) DocRED unconstrained baseline — 获取复杂 schema (96 relations) 下的 violation profile，与 Qwen/Llama 对比\", \"notes\": \"PID 5571 on cuda:0 via nohup. Model loaded from symlink /root/autodl-tmp/models/Mistral-7B-Instruct-v0.3 -> ms_cache. 2x RTX PRO 6000 Blackwell 98GB. Log at /tmp/w6_mistral_docred_unconstrained.log.\", \"failure_reason\": \"\", \"completed_at\": \"2026-05-16T05:28:07.908Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"PID 5571 on cuda:0 via nohup. Model loaded from symlink /root/autodl-tmp/models/Mistral-7B-Instruct-v0.3 -> ms_cache. 2x RTX PRO 6000 Blackwell 98GB. Log at /tmp/w6_mistral_docred_unconstrained.log.\"}, \"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T08:36:47.316246+00:00\"}]}, \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode unconstrained --dataset docred --model_path /root/autodl-tmp/models/Mistral-7B-Instruct-v0.3 --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w6_mistral_docred_unconstrained.jsonl --batch_size 1 --max_new_tokens 4096\", \"server\": \"westd-21461\", \"gpu\": 0, \"pid\": 7740, \"log_path\": \"~/runs/schema_semantic_constrained_ie/w6_mistral_docred_unconstrained.log\", \"model_name\": \"Mistral-7B-Instruct-v0.3\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"seed\": 42}, \"reproduce\": {\"finished_at\": \"2026-05-16T08:36:44.102Z\"}, \"conclusion\": \"success\", \"metrics\": {\"total_samples\": 998, \"parse_failures\": 7, \"parse_fail_rate\": 0.7, \"total_pred_entities\": 12580, \"total_pred_relations\": 11879, \"ET_pct\": 7.58, \"RV_pct\": 42.35, \"DR_pct\": 57.42, \"CF_pct\": 24.78, \"E_P\": 0.6221, \"E_R\": 0.3975, \"E_F1\": 0.4851, \"R_P\": 0.0447, \"R_R\": 0.0432, \"R_F1\": 0.0434, \"f1_method\": \"fuzzy_normalized\", \"f1_note\": \"Relation matching uses case-insensitive normalization with token-overlap >80% and edit-distance ≤2 fallback. Strict R_F1=3.50% (delta +0.84pp from 98 additional TPs via fuzzy matching of Mistral underscore/abbreviation variants).\"}}, \"w6_mistral_docred_constrained\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-16T03:19:37.979Z\", \"updated_at\": \"2026-05-16T09:10:49.476Z\", \"hypothesis\": \"Mistral (3rd model) + OntoCoDec constrained eval on DocRED — 验证约束解码在第三模型+复杂 schema 上的泛化性\", \"notes\": \"Constrained decoding eliminates ET/RV violations completely (0%), reduces DR from 57.42%→33.20% (-24.22pp). E_F1 +2.08pp, R_F1 +2.02pp vs unconstrained. DR残余33%来自semantic constraint未覆盖的domain-range组合。\", \"failure_reason\": \"Process killed by fix worker (pkill) during orphan cleanup. Had 15/998 samples before kill.\", \"completed_at\": \"2026-05-16T05:31:30.251Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"PID 6789 on cuda:1 via nohup. Patched xgrammar 0.2.0 hf.py (accept_token .item() fix for transformers 5.8.1 compat). Model loaded from symlink. Log at /tmp/w6_mistral_docred_constrained.log.\"}}, \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/models/Mistral-7B-Instruct-v0.3 --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w6_mistral_docred_constrained.jsonl --batch_size 1 --max_new_tokens 4096\", \"server\": \"westd-21461\", \"gpu\": 1, \"pid\": 8347, \"log_path\": \"~/runs/schema_semantic_constrained_ie/w6_mistral_docred_constrained.log\", \"model_name\": \"Mistral-7B-Instruct-v0.3\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"seed\": 42}, \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 33.2, \"CF_pct\": 0.19, \"E_P\": 65.02, \"E_R\": 41.4, \"E_F1\": 50.59, \"R_P\": 5.67, \"R_R\": 5.37, \"R_F1\": 5.52, \"parse_fail_rate\": 0.8, \"total_samples\": 998, \"total_pred_entities\": 12535, \"total_pred_relations\": 11554, \"delta_vs_unconstrained\": {\"ET_pct\": -7.58, \"RV_pct\": -42.35, \"DR_pct\": -24.22, \"CF_pct\": -24.59, \"E_F1\": 2.08, \"R_F1\": 2.02}}, \"checkpoint_path\": \"outputs/w6_mistral_docred_constrained.jsonl\", \"conclusion\": \"success\"}, \"w5_qwen_docred_lora_constrained_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:03:33.642Z\", \"updated_at\": \"2026-05-16T08:10:01.206Z\", \"hypothesis\": \"Fine-tuned Qwen3-8B DocRED LoRA + OntoCoDec constrained eval — 验证 composability：约束解码在 fine-tuned Qwen DocRED 上是否仍能消除残余 DR 且不损 R-F1\", \"parent\": \"w5_qwen_docred_lora_training\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/checkpoints/qwen_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w5_qwen_docred_lora_constrained_eval.jsonl --batch_size 1 --max_new_tokens 4096\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:1\"], \"pid\": \"321568\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w5_qwen_docred_lora_constrained_eval.log\", \"model_name\": \"Qwen3-8B-LoRA-DocRED\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json\"}, \"notes\": \"由另一个 worker 提交，本次确认进程正常运行。PID 321568 (GPU subprocess), wrapper PID 321563, tmux session. CUDA_VISIBLE_DEVICES=1 由 wrapper 控制。模型已加载，2/998 开始推理。Grammar 编译 96 relation types 后开始生成。ETA ~5-6h (参考 unconstrained 5.82h, constrained 更慢)。\", \"reproduce\": {\"finished_at\": \"2026-05-16T08:05:39.680Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T08:05:41.651478+00:00\"}]}, \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.01, \"CF_pct\": 0.41, \"E_F1\": 81.43, \"E_P\": 85.41, \"E_R\": 77.81, \"R_F1\": 40.56, \"R_P\": 36.35, \"R_R\": 45.86, \"parse_fail_rate\": 8.52, \"total_samples\": 998, \"success_samples\": 913, \"fail_samples\": 85, \"total_entities_pred\": 17799, \"total_relations_pred\": 15563, \"E_F1_excl_fail\": 85.69, \"R_F1_excl_fail\": 42.23, \"delta_vs_unconstrained\": {\"delta_DR\": -0.75, \"delta_RV\": -0.27, \"delta_R_F1\": -0.3, \"delta_R_F1_excl_fail\": 0.03, \"DR_reduction_pct\": 98.7, \"note\": \"Constrained - unconstrained. Unconstrained: DR=0.76%, R_F1=40.86, R_F1_excl_fail=42.20\"}}, \"conclusion\": \"success\", \"checkpoint_path\": \"outputs/w5_qwen_docred_lora_constrained_eval.jsonl\", \"completed_at\": \"2026-05-16T08:10:01.206Z\"}, \"w5_llama_docred_sft_data_gen\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:07:32.770Z\", \"updated_at\": \"2026-05-16T03:21:57.320Z\", \"hypothesis\": \"Generate Llama-3.1-8B-Instruct format DocRED SFT train/dev JSONL — prerequisite for Llama DocRED LoRA fine-tune (composability matrix Llama×DocRED cell)\", \"conclusion\": \"success\", \"metrics\": {\"train_samples\": 3053, \"dev_samples\": 998, \"train_size_mb\": 19, \"dev_size_mb\": 6.1}, \"spec\": {\"checkpoint_path\": \"N/A (data gen)\", \"log_path\": \"N/A (data gen)\", \"command\": \"python3 prepare_sft_data_docred_llama.py\", \"server\": \"westd-16980\", \"data_path\": \"data/docred/\", \"data_count\": 4051, \"model_name\": \"N/A\", \"seed\": 42}, \"completed_at\": \"2026-05-16T03:20:06.742Z\"}, \"w1_cf_fallback_llama_docred\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:33:00.998Z\", \"updated_at\": \"2026-05-16T03:21:56.516Z\", \"spec\": {\"hypothesis\": \"W1 CF fallback 在 Llama DocRED 上的效果。Llama DocRED full_s1 原 CF=12.02%（最高），预期 fallback 大幅降低。Phase 3 实验。\", \"parent\": \"llama_docred_full_s1\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w1_cf_fallback_llama_docred.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 4096\\\"\", \"server\": \"westd-16980\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"Meta-Llama-3.1-8B-Instruct\", \"seed\": \"default\", \"gpu\": \"cuda:0\"}, \"conclusion\": \"killed\", \"notes\": \"D020: 取消。CF fallback 改为 Analytical Finding 方案，仅用 SciERC pilot 数据。D027 确认 Qwen DocRED CF fallback 代码未生效（实际跑 full_s1）。Analytical finding 结论跨模型适用——CF↔DR 根本性张力不依赖模型选择。最终状态: killed。\", \"completed_at\": \"2026-05-16T03:19:55.843Z\"}, \"w1_cf_fallback_llama_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:32:57.470Z\", \"updated_at\": \"2026-05-16T03:21:55.322Z\", \"spec\": {\"hypothesis\": \"W1 CF fallback 在 Llama SciERC 上的跨模型验证。Llama SciERC full_s1 原 CF=6.56%，预期显著降低。Phase 2 实验。\", \"parent\": \"llama_scierc_full_s1\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/w1_cf_fallback_llama_scierc.jsonl --device cuda:1 --batch_size 1 --max_new_tokens 4096\\\"\", \"server\": \"westd-16980\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Meta-Llama-3.1-8B-Instruct\", \"seed\": \"default\", \"gpu\": \"cuda:1\"}, \"conclusion\": \"killed\", \"notes\": \"D020: 取消。CF fallback 改为 Analytical Finding 方案，仅用 SciERC pilot 数据。Qwen SciERC pilot 已充分证明 CF↔DR re-routing（CF -9.86pp 但 DR +13.85pp，budget +3.99pp）。跨模型重复无额外信息量。最终状态: killed。\", \"completed_at\": \"2026-05-16T03:19:54.869Z\"}, \"w5_qwen_docred_lora_unconstrained_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:03:32.625Z\", \"updated_at\": \"2026-05-16T01:55:03.824Z\", \"hypothesis\": \"Fine-tuned Qwen3-8B DocRED LoRA unconstrained eval — 获取 fine-tuned baseline DR/R-F1，与 constrained eval 对比计算 composability delta\", \"parent\": \"w5_qwen_docred_lora_training\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode unconstrained --dataset docred --model_path /root/autodl-tmp/checkpoints/qwen_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w5_qwen_docred_lora_unconstrained_eval.jsonl --batch_size 1 --max_new_tokens 4096\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:1\"], \"pid\": \"304006\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w5_qwen_docred_lora_unconstrained_eval.log\", \"submitted_at\": \"2026-05-15T20:03:48.762Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"Qwen3-8B-LoRA-DocRED\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json\", \"wall_clock_seconds\": 20941.5, \"gpu_hours\": 5.82}, \"reproduce\": {\"finished_at\": \"2026-05-16T01:49:51.884Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T01:49:53.877179+00:00\"}]}, \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0.27, \"DR_pct\": 0.76, \"CF_pct\": 0.12, \"E_F1\": 82.15, \"E_P\": 85.44, \"E_R\": 79.11, \"R_F1\": 40.86, \"R_P\": 36.41, \"R_R\": 46.56, \"parse_fail_rate\": 7.11, \"total_samples\": 998, \"success_samples\": 927, \"fail_samples\": 71, \"total_entities_pred\": 18091, \"total_relations_pred\": 15870, \"ET_pct_excl_fail\": 0, \"RV_pct_excl_fail\": 0.27, \"DR_pct_excl_fail\": 0.76, \"CF_pct_excl_fail\": 0.12, \"E_F1_excl_fail\": 85.72, \"E_P_excl_fail\": 85.44, \"E_R_excl_fail\": 86, \"R_F1_excl_fail\": 42.2, \"R_P_excl_fail\": 36.41, \"R_R_excl_fail\": 50.17}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/qwen_lora_docred_merged\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w5_qwen_docred_lora_unconstrained_eval.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T01:52:50.220Z\", \"notes\": \"998/998 完成, 927 success / 71 fail. 两组指标已计算. parse_fail_rate=7.11% 高于 Llama(2.3%), Qwen 在长文档上更易超时. R_F1=40.86 略低于 Llama(43.72), E_F1=82.15 略低于 Llama(83.93). DR_pct=0.76% 高于 Llama(0.49%), 说明 Qwen LoRA 残留更多 domain-range 违规.\"}, \"w5_llama_docred_lora_unconstrained_eval\": {\"status\": \"DONE\", \"retry_count\": 2, \"created_at\": \"2026-05-15T19:58:07.956Z\", \"updated_at\": \"2026-05-16T00:22:57.512Z\", \"hypothesis\": \"Fine-tuned Llama-3.1-8B DocRED LoRA unconstrained eval — 获取 fine-tuned baseline DR/R-F1，与 constrained eval 对比计算 composability delta\", \"parent\": \"w5_llama_docred_lora_training\", \"reproduce\": {\"finished_at\": \"2026-05-16T00:11:58.831Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"completed_at\": \"2026-05-15T23:14:38.851Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T23:14:41.289164+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T00:12:00.360157+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"失败原因: SIGTERM (exit 143) — 外部 kill，非 OOM/崩溃。日志尾部无 Traceback，正常生成中被终止。运行 3.27h (998 samples, batch=1, max_tokens=4096)。已有 ops worker (ops:llama_eval_timeout_fix) 在处理修复重提。| 已有成果: 可能有部分输出 (outputs/w5_llama_docred_lora_unconstrained_eval.jsonl) | 建议: 等 ops worker 完成后确认重提结果\"}}, \"notes\": \"Process received SIGTERM (exit 143) after completing all 998/998 samples. Output file verified complete. Log shows 776 pad_token_id warnings (batch_size=1, some samples produce multiple warnings). No OOM, no traceback. SIGTERM likely from job scheduler timeout, but all inference output was already written. Diagnosed and reclassified from failed→success on 2026-05-16.\", \"spec\": {\"command\": \"nohup python3 run_constrained_extraction.py --mode unconstrained --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w5_llama_docred_lora_unconstrained_eval.jsonl --batch_size 1 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"312930\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"Meta-Llama-3.1-8B-Instruct-LoRA-DocRED\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json\"}, \"conclusion\": \"success\", \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0.15, \"DR_pct\": 0.49, \"E_F1\": 83.93, \"E_P\": 84.93, \"E_R\": 82.96, \"R_F1\": 43.72, \"R_P\": 38.59, \"R_R\": 50.41, \"parse_fail_rate\": 2.3, \"total_samples\": 998, \"total_entities_pred\": 19106, \"total_relations_pred\": 16171}}, \"w5_qwen_docred_lora_training\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:48:52.649Z\", \"updated_at\": \"2026-05-15T20:02:42.106Z\", \"hypothesis\": \"Qwen3-8B LoRA fine-tune on DocRED — 填补 Qwen DocRED composability 2×2 matrix 的 FT 行。预期：(1) LoRA 后 E-F1/R-F1 大幅提升；(2) 残余 DR > 0% 证明 OntoCoDec 在 DocRED FT 上仍有 composability 价值。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && WANDB_MODE=disabled python3 scripts/train_lora_docred.py\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:1\"], \"pid\": \"298245\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w5_qwen_docred_lora_training.log\", \"submitted_at\": \"2026-05-15T18:22:06Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 6015.9, \"gpu_hours\": 1.67}, \"reproduce\": {\"finished_at\": \"2026-05-15T20:01:28.494Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:55:53.910959+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T20:01:30.155403+00:00\"}]}, \"notes\": \"Retry #4 (PID 298245, cuda:1): 级联故障修复后由 ops worker 重提交。前次失败原因: GPU 0 幽灵进程争抢显存 + 命令中 CUDA_VISIBLE_DEVICES 硬编码覆盖 wrapper。修复后 wrapper 统一控制 CUDA_VISIBLE_DEVICES。双卡 99% util 已确认。ETA ~2h on RTX PRO 6000。\", \"completed_at\": \"2026-05-15T20:02:21.920Z\", \"metrics\": {\"eval_loss\": 0.0614, \"eval_mean_token_accuracy\": 0.9804, \"eval_entropy\": 0.715, \"train_loss\": 0.0682, \"train_runtime_s\": 5825.6, \"epochs\": 3, \"adapter_path\": \"/root/schema_semantic_constrained_ie/checkpoints/qwen_lora_docred\", \"merged_path\": \"/root/autodl-tmp/checkpoints/qwen_lora_docred_merged\"}}, \"w5_llama_docred_lora_training\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:15:19.269Z\", \"updated_at\": \"2026-05-15T19:57:16.365Z\", \"hypothesis\": \"Llama-3.1-8B-Instruct LoRA fine-tune on DocRED — 填补 Llama DocRED composability 2×2 matrix 的 FT 行。预期：(1) LoRA 后 E-F1/R-F1 大幅提升；(2) 残余 DR > 0% 证明 OntoCoDec 在 DocRED FT 上仍有 composability 价值。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && WANDB_MODE=disabled python3 scripts/train_lora_docred_llama.py\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"298323\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w5_llama_docred_lora_training.log\", \"submitted_at\": \"2026-05-15T18:23:07Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/docred/sft_train_llama.jsonl\", \"data_count\": 3053, \"model_name\": \"Meta-Llama-3.1-8B-Instruct\", \"seed\": \"default\", \"wall_clock_seconds\": 5649.4, \"gpu_hours\": 1.57}, \"notes\": \"Retry #1 (PID 298323, cuda:0): 级联故障修复后重提。首次提交(PID 297434)因幽灵进程占满 cuda:0 显存导致 OOM。修复: 移除命令中 CUDA_VISIBLE_DEVICES 硬编码，由 wrapper 统一控制。参数对齐 Llama SciERC LoRA: rank=16, alpha=32, lr=2e-4, 3 epochs, bs=2, grad_accum=8, max_length=4096。ETA ~80-90min on RTX PRO 6000。输出: checkpoints/llama_lora_docred/ (adapter) + /root/autodl-tmp/checkpoints/llama_lora_docred_merged/ (merged)。\", \"reproduce\": {\"finished_at\": \"2026-05-15T19:54:59.123Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T19:55:00.912384+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.0572, \"eval_loss\": 0.0624, \"token_acc\": 98.06}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged/\", \"completed_at\": \"2026-05-15T19:57:16.365Z\"}, \"w5_docred_sft_data_gen\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:51:09.748Z\", \"updated_at\": \"2026-05-15T18:01:39.032Z\", \"hypothesis\": \"Generate DocRED SFT train/dev JSONL from train_annotated.json + dev.json — prerequisite for Qwen/Llama DocRED LoRA fine-tune\", \"spec\": {\"command\": \"python3 scripts/prepare_sft_data_docred.py\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"292314\", \"log_path\": \"N/A\", \"submitted_at\": \"2026-05-15T17:51:19.316Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/docred/\", \"data_count\": 4051, \"model_name\": \"Qwen3-8B\", \"seed\": null, \"wall_clock_seconds\": 379.5, \"gpu_hours\": 0.11, \"checkpoint_path\": \"N/A\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T17:51:44.980Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:51:46.380733+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"train_samples\": 3053, \"dev_samples\": 998, \"train_entities\": 59493, \"train_relations\": 38180, \"dev_entities\": 19528, \"dev_relations\": 12275}, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/data/docred/sft_train.jsonl,/root/schema_semantic_constrained_ie/data/docred/sft_dev.jsonl\", \"completed_at\": \"2026-05-15T17:57:38.825Z\", \"notes\": \"数据质量验证完成：4051行全部JSON解析通过，0损坏。Prompt用Qwen3 chat模板（含think tag），6实体类型+96关系类型。Completion为合法JSON（entities+relations）。数据可直接用于SFT训练。Train: 3053样本/19M, Dev: 998样本/6.0M。\"}, \"w5_llama_lora_scierc_training\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:33:38.168Z\", \"updated_at\": \"2026-05-15T17:24:38.949Z\", \"spec\": {\"hypothesis\": \"Llama-3.1-8B-Instruct LoRA fine-tune on SciERC, extending Claim 3 composability to cross-model. Mirrors Qwen3-8B LoRA config (r=16, alpha=32, lr=2e-4, 3 epochs).\", \"parent\": \"w5_lora_scierc_training\", \"model_name\": \"Meta-Llama-3.1-8B-Instruct\", \"dataset\": \"SciERC\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/llama_lora_scierc_merged\", \"log_path\": \"logs/w5_llama_lora_scierc_training.log\", \"adapter_path\": \"checkpoints/llama_lora_scierc\", \"base_model\": \"/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct\"}, \"hypothesis\": \"Llama-3.1-8B-Instruct LoRA fine-tune on SciERC — 扩展 composability 验证到跨模型。预期：(1) LoRA 训练后 E-F1/R-F1 大幅提升（对标 Qwen LoRA +36pp/+36pp）；(2) 为 Llama SciERC 2×2 composability matrix 提供 fine-tuned baseline。\", \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-15T17:17:30.599Z\"}, \"conclusion\": \"success\", \"metrics\": {\"eval_loss\": 0.0595, \"eval_mean_token_accuracy\": 0.9817, \"eval_entropy\": 1.0565, \"train_loss\": 0.0501, \"train_runtime_sec\": 654.23, \"epochs\": 3, \"train_samples_per_second\": 8.08}, \"completed_at\": \"2026-05-15T17:18:45.275Z\"}, \"w1_cf_fallback_docred\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-15T10:32:53.234Z\", \"updated_at\": \"2026-05-15T16:55:58.012Z\", \"server\": \"westd-16980\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"command\": \"bash -c \\\"rm -f /root/schema_semantic_constrained_ie/outputs/w1_cf_fallback_docred.jsonl && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w1_cf_fallback_docred.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 4096\\\"\"}, \"notes\": \"Reviewer #12 三次确认: 实际运行 --mode full_s1 (非 CF fallback), 与 phase2_docred_full_s1 重复。CF fallback 代码恢复失败或未生效。命令行明确显示 --mode full_s1。PID 283824 已 kill。W1 CF fallback 整体定论: SciERC pilot (analytical finding) 已充分, DocRED 不再重跑。\", \"completed_at\": \"2026-05-15T15:47:59.075Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"killed\", \"notes\": \"D020: Director 取消全部 CF fallback 实验。改用 Analytical Finding 方案——pilot negative 本身作为论文素材。仅跑约 30s 即被终止。\"}}, \"spec\": {\"command\": \"bash -c \\\"rm -f /root/schema_semantic_constrained_ie/outputs/w1_cf_fallback_docred.jsonl && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w1_cf_fallback_docred.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 4096\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:1\"], \"pid\": \"283824\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w1_cf_fallback_docred.log\", \"submitted_at\": \"2026-05-15T16:26:41.953Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (killed - ran wrong code)\", \"wall_clock_seconds\": 1756.1, \"gpu_hours\": 0.49}, \"pid\": \"283824\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w1_cf_fallback_docred.log\", \"conclusion\": \"killed\"}, \"w5_lora_scierc_unconstrained_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:23:25.030Z\", \"updated_at\": \"2026-05-15T16:01:58.250Z\", \"hypothesis\": \"Fine-tuned Qwen3-8B still produces >2% decode rate violations on SciERC unconstrained, justifying OntoCoDec constraint application\", \"parent\": \"w5_lora_scierc_training\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode unconstrained --dataset scierc --model_path /root/schema_semantic_constrained_ie/checkpoints/qwen3_8b_lora_scierc_merged --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/w5_lora_scierc_unconstrained_eval.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"pid\": 278380, \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"data_count_note\": \"551 per-sentence samples derived from 100 SciERC test documents (matches phase2_scierc_unconstrained sample count)\", \"model_name\": \"Qwen3-8B-LoRA-SciERC\", \"model_path\": \"/root/schema_semantic_constrained_ie/checkpoints/qwen3_8b_lora_scierc_merged\", \"seed\": null, \"checkpoint_source\": \"/root/schema_semantic_constrained_ie/checkpoints/qwen3_8b_lora_scierc_merged\", \"eval_data\": \"SciERC test set (551 samples)\", \"constraints_path\": \"/root/schema_semantic_constrained_ie/ontology_constraints.json\", \"output_path\": \"/root/schema_semantic_constrained_ie/outputs/w5_lora_scierc_unconstrained_eval.jsonl\", \"log_path\": \"/root/schema_semantic_constrained_ie/outputs/w5_lora_scierc_unconstrained_eval.log\", \"mode\": \"unconstrained\", \"max_new_tokens\": 4096, \"batch_size\": 1, \"path_note\": \"Task spec called for data/scierc/test.json + data/scierc/ontology_constraints_scierc.json which do not exist on this server; substituted the actual paths used by all prior phase2_scierc_* experiments.\"}, \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"pid\": 278385, \"conclusion\": \"success\", \"metrics\": {\"json_parse_rate\": 1, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0, \"domain_range_violation_rate\": 0.0195, \"cross_field_consistency_violation_rate\": 0, \"entity_f1\": 0.6705, \"entity_precision\": 0.6523, \"entity_recall\": 0.6898, \"relation_f1\": 0.4386, \"relation_precision\": 0.4087, \"relation_recall\": 0.4733, \"total_entities\": 1784, \"total_relations\": 1128, \"domain_range_violations\": 22, \"go_nogo_metric\": 0.0195, \"dr_gate\": \"FAILED\"}, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/w5_lora_scierc_unconstrained_eval.jsonl\", \"completed_at\": \"2026-05-15T15:55:17.802Z\", \"notes\": \"LoRA fine-tuned Qwen3-8B unconstrained eval on SciERC: 聚合 DR=1.95% 略低于 2% gate 阈值，但按关系类型拆分后 Evaluate-for DR=13.13%（99 个三元组中 13 个违规）、Part-of 5.8%、Compare 5.0%。表明 tight-constraint 关系是 fine-tuning 无法覆盖的长尾——OntoCoDec 的互补价值在于消除这些 schema-ambiguous relation 的残余 DR。Quality: R-F1=43.9% (+35.7pp vs base), E-F1=67.1% (+36.1pp vs base). ET/RV/CF 全部清零。\"}, \"llama_docred_full_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T10:42:59.855Z\", \"updated_at\": \"2026-05-14T20:29:59.744Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/llama_docred_full_s1.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 4096\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"194295\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/llama_docred_full_s1.log\", \"submitted_at\": \"2026-05-14T14:41:22.992Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 20912.7, \"gpu_hours\": 5.81}, \"hypothesis\": \"Llama-3.1-8B-Instruct + Grammar+Semantic 双层约束 (S1) 在 DocRED (96 relations) 上的效果。与 Qwen3-8B DocRED full_s1 (DR 10.19%) 对比，验证约束解码在不同模型+复杂 schema 上的泛化性。\", \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T14:39:33.737Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/llama_docred_full_s1.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 4096\\\"\", \"finished_at\": \"2026-05-14T20:24:03.061Z\", \"training_hours\": 5.74}, \"pid\": \"194295\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/llama_docred_full_s1.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T20:24:04.262279+00:00\"}]}, \"checkpoint_path\": \"outputs/llama_docred_full_s1.jsonl\", \"completed_at\": \"2026-05-14T20:24:03Z\", \"metrics\": {\"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\", \"f1_method\": \"all_set\", \"violations\": {\"ET\": 0, \"RV\": 0, \"DR\": 2.55, \"CF\": 12.02}, \"f1\": {\"entity_f1\": 55.01, \"entity_precision\": 61.41, \"entity_recall\": 49.82, \"relation_f1\": 6.27, \"relation_precision\": 5.49, \"relation_recall\": 7.32}, \"counts\": {\"documents\": 998, \"documents_checked\": 907, \"parse_failures\": 91, \"unique_entities\": 11296, \"triples\": 16368}}, \"conclusion\": \"success\", \"notes\": \"ET/RV→0%, DR 26.07%→2.55% (优于Qwen的10.19%)。但CF从0.17%暴涨至12.02%，说明Llama的entity type预测更容易被约束扰动。F1基本持平(E-F1 -0.64pp, R-F1 +0.29pp)。Parse failures从68增至91。Grammar-first fallback频繁触发。\"}, \"llama_docred_unconstrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T10:42:58.719Z\", \"updated_at\": \"2026-05-14T19:45:08.201Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode unconstrained --dataset docred --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/llama_docred_unconstrained.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 4096\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:1\"], \"pid\": \"193605\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/llama_docred_unconstrained.log\", \"submitted_at\": \"2026-05-14T14:35:57.755Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 18533.7, \"gpu_hours\": 5.15}, \"hypothesis\": \"Llama-3.1-8B-Instruct 在 DocRED unconstrained baseline。与 Qwen3-8B DocRED unconstrained 对比 violation 分布。验证不同模型在复杂 schema (96 relations) 上的 violation 模式差异。\", \"server\": \"westd-16980\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-16980\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-14T14:15:03.413Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode unconstrained --dataset docred --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/llama_docred_unconstrained.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 4096\\\"\", \"finished_at\": \"2026-05-14T19:39:03.154Z\", \"training_hours\": 5.4}, \"pid\": \"193605\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/llama_docred_unconstrained.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T19:39:05.142651+00:00\"}]}, \"metrics\": {\"checker_version\": \"fixed_20260514_v2\", \"f1_method\": \"all_set\", \"documents\": 998, \"documents_checked\": 930, \"parse_failures\": 68, \"unique_entities\": 11525, \"total_triples\": 16437, \"dr_eligible_triples\": 13789, \"ET_rate_pct\": 0.13, \"RV_rate_pct\": 16.03, \"DR_rate_pct\": 26.07, \"CF_rate_pct\": 0.17, \"entity_precision\": 61.22, \"entity_recall\": 51.02, \"entity_f1\": 55.65, \"relation_precision\": 5.22, \"relation_recall\": 7, \"relation_f1\": 5.98, \"fuzzy_relation_matches\": 121}, \"conclusion\": \"success\", \"notes\": \"v2 checker (unique_et dedup) + all_set F1。930/998 docs parsed (68 parse failures, 6.8% vs Qwen 1.2%)。Violation profile 与 Qwen3-8B 显著不同：RV 大幅降低 (16.03% vs 29.66%，-13.6pp，Llama 更倾向使用标准关系名) 但 DR 更高 (26.07% vs 18.46%，+7.6pp，即使关系名正确 head/tail 类型约束违反更多)。ET 极低 (0.13% vs 2.48%，-2.35pp)，CF 接近 (0.17% vs 0.10%)。F1 弱于 Qwen: R-F1 5.98% vs 7.74% (-1.76pp)，E-F1 55.65% vs 58.15% (-2.50pp)。DR 26.07% 为约束解码提供更大改进空间。\", \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/llama_docred_unconstrained.jsonl\", \"completed_at\": \"2026-05-14T19:44:51.441Z\"}, \"phase2_docred_grammar_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T01:55:50.031Z\", \"updated_at\": \"2026-05-14T18:52:55.527Z\", \"hypothesis\": \"Grammar-only constrained decoding 在 DocRED (96 relation types) 上能否消除 RV violations (28.9%) 和 ET violations (7.5%)？与 SciERC grammar_only (RV 1.4%→0%, ET 0.4%→0%) 对比，验证 grammar 层在复杂 schema 上的泛化性。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 nohup python3 run_constrained_extraction.py --mode grammar_only --dataset docred --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/docred_grammar_only.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"150766\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"log_path\": \"/root/runs/schema_semantic_constrained_ie/docred_grammar_only.log\"}, \"conclusion\": \"success\", \"metrics\": {\"documents_checked\": 985, \"parse_failures\": 13, \"total_entities\": 20150, \"total_triples\": 17341, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0.0003, \"domain_range_violation_rate\": 0.2617, \"cross_field_consistency_violation_rate\": 0.0007, \"relation_f1\": 8.31, \"relation_precision\": 7.06, \"relation_recall\": 10.12, \"entity_f1\": 59.38, \"entity_precision\": 58.47, \"entity_recall\": 60.32, \"unrecognized_relations\": 5, \"f1_method\": \"all_set\", \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/docred_grammar_only.jsonl\", \"completed_at\": \"2026-05-14T07:40:10.382Z\"}, \"llama_scierc_full_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T10:42:56.936Z\", \"updated_at\": \"2026-05-14T18:31:43.217Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/llama_scierc_full_s1.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 2048\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"190648\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/llama_scierc_full_s1.log\", \"submitted_at\": \"2026-05-14T13:50:35.755Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-8B-Instruct\", \"seed\": 42, \"wall_clock_seconds\": 1249.5, \"gpu_hours\": 0.35}, \"hypothesis\": \"Llama-3.1-8B-Instruct + Grammar+Semantic 双层约束 (S1) 在 SciERC 上的效果。与 Qwen3-8B full_s1 (DR 0.93%) 对比，验证 OntoCoDec 的 model-agnostic 特性。零代码修改。D009 cross-model 验证核心实验。\", \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T13:50:33.979Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/llama_scierc_full_s1.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 2048\\\"\", \"finished_at\": \"2026-05-14T14:11:24.215Z\", \"training_hours\": 0.35}, \"pid\": \"190648\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/llama_scierc_full_s1.log\", \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T14:11:25.248Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T14:11:26.755217+00:00\"}]}, \"metrics\": {\"samples\": 550, \"entities_extracted\": 2469, \"relations_extracted\": 1315, \"domain_range_violation_rate\": 0.0008, \"relation_vocab_violation_rate\": 0, \"entity_type_violation_rate\": 0, \"cross_field_consistency_violation_rate\": 0.0656, \"total_violation_rate\": 0.0431, \"entity_f1\": 0.2349, \"entity_precision\": 0.1972, \"entity_recall\": 0.2902, \"relation_f1\": 0.0254, \"relation_precision\": 0.0221, \"relation_recall\": 0.0298, \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/llama_scierc_full_s1.jsonl\", \"notes\": \"550/551 samples (1 corrupt line from duplicate PID removed). DR 0.08% — 约束合规性极好，优于 Qwen3-8B full_s1 (0.93%)。但 E-F1=23.49% (vs Qwen 30.98%), R-F1=2.54% (vs Qwen 8.36%)，Llama 在 IE 质量上显著弱于 Qwen。对比 Llama unconstrained: DR 13.3%→0.08% (约束生效), E-F1 23.56%→23.49% (持平), R-F1 2.68%→2.54% (微降)。约束大幅降低违规率但未提升抽取质量。Cross-field consistency violations 较高 (6.56%)。\"}, \"llama_scierc_unconstrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T10:42:55.421Z\", \"updated_at\": \"2026-05-14T18:31:40.240Z\", \"spec\": {\"data_path\": \"scierc_test\", \"data_count\": 551, \"model_name\": \"Llama-3.1-8B-Instruct\", \"seed\": 42, \"command\": \"python3 run_extraction.py --config configs/llama_scierc_unconstrained.yaml\", \"server\": \"westd-16980\"}, \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T13:19:48.866Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode unconstrained --dataset scierc --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/llama_scierc_unconstrained.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 2048\\\"\", \"finished_at\": \"2026-05-14T13:46:24.376Z\", \"training_hours\": 0.44}, \"pid\": \"188367\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/llama_scierc_unconstrained.log\", \"hypothesis\": \"Llama-3.1-8B-Instruct 在 SciERC unconstrained baseline — 验证 OntoCoDec 跨模型泛化性。零代码修改，与 Qwen3-8B unconstrained 对比 violation 分布差异。预期 DR~15%, RV~1.4%, ET~0.4%（Llama instruction-following 可能更好）。D009 cross-model 验证的第一步。\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T13:46:25.548989+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/llama_scierc_unconstrained.jsonl\", \"metrics\": {\"entity_type_violation_rate\": 0, \"relation_vocab_violation_rate\": 0.0055, \"domain_range_violation_rate\": 0.1334, \"cross_field_consistency_violations\": 6, \"entity_f1\": 0.2356, \"entity_precision\": 0.1983, \"entity_recall\": 0.2902, \"relation_f1\": 0.0268, \"relation_precision\": 0.0236, \"relation_recall\": 0.031, \"total_entities\": 2451, \"total_relations\": 1274, \"json_parse_failures\": 1, \"samples\": 551, \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}, \"completed_at\": \"2026-05-14T13:49:13.425Z\", \"notes\": \"Llama-3.1-8B-Instruct SciERC unconstrained baseline 完成。551 样本（550成功/1失败）。Violation: ET=0%, RV=0.5%, DR=13.3%。F1: E-F1=23.56%, R-F1=2.68%。与 Qwen3-8B unconstrained 对比：Llama violation 略低（DR 13.3% vs 15.4%），但 F1 明显更差（E-F1 低7.5pp, R-F1 低5.5pp）。Llama 更倾向保守提取——提取数量少、violation 低但 recall 也低。Qwen3 在 unconstrained 设定下提取质量优于 Llama。\"}, \"phase2_scierc_full_s1\": {\"status\": \"DONE\", \"retry_count\": 2, \"created_at\": \"2026-05-13T21:48:44.785Z\", \"updated_at\": \"2026-05-14T18:31:34.603Z\", \"hypothesis\": \"Grammar + Semantic 双层约束 (S1 单通道) 能否同时消除 rv + dr violations？F1 变化是关键：<2pp 降=完美，2-5pp=可接受 trade-off，>5pp=需要 S2 策略\", \"notes\": \"✅ _v2 干净数据全量完成 551/551. DR violation = 0.93% (baseline 15.37%, -14.44pp). ET=0%, RV=0%. 数据来源: phase2_scierc_full_s1_v2.jsonl\", \"server\": \"westd-16980\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-16980\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-13T23:49:56.383Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && which python3 && python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/phase2_scierc_full_s1.jsonl --device cuda:0 --batch_size 1\\\"\", \"finished_at\": \"2026-05-14T00:33:47.489Z\", \"training_hours\": 0.73}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"completed_at\": \"2026-05-13T23:45:41.906Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:45:42.821098+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T00:33:48.999924+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"诊断完成: EXIT_CODE=127, bash: line 1: python3: command not found。Root cause: submit_training_job 未在命令前加 conda 环境激活。修复方案: 命令前缀加 source /root/miniconda3/etc/profile.d/conda.sh && conda activate base。retry_count=0, 自动重试中。\"}}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 run_constrained_extraction.py --mode full_s1 ...\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:1\"], \"data_path\": \"/root/schema_semantic_constrained_ie/data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"note\": \"retry #2: bash -c wrapping fixes EXIT_CODE=127\"}, \"pid\": \"134593\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/phase2_scierc_full_s1.log\", \"conclusion\": \"success\", \"metrics\": {\"total_samples\": 551, \"total_triples\": 1729, \"total_entities\": 2474, \"json_parse_rate\": 1, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0, \"domain_range_violation_rate\": 0.0093, \"cross_field_consistency_violation_rate\": 0.099, \"entity_f1\": 0.3098, \"entity_precision\": 0.2598, \"entity_recall\": 0.3837, \"relation_f1\": 0.0836, \"relation_precision\": 0.0654, \"relation_recall\": 0.116, \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/phase2_scierc_full_s1_v2.jsonl\"}, \"phase2_scierc_semantic_only\": {\"status\": \"DONE\", \"retry_count\": 2, \"created_at\": \"2026-05-13T21:48:44.427Z\", \"updated_at\": \"2026-05-14T18:31:31.811Z\", \"hypothesis\": \"Semantic-only constrained decoding (TypeConstraintProcessor) 能否消除 domain/range violations？预期 dr_violation→0%，但可能影响 F1（约束过强导致生成偏移）\", \"notes\": \"✅ _v2 干净数据全量完成 551/551. DR violation = 11.65% (baseline 15.37%, -3.72pp). ET=0.4%, RV=1.51%.\", \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-13T23:49:33.935Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && which python3 && python3 run_constrained_extraction.py --mode semantic_only --dataset scierc --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/phase2_scierc_semantic_only.jsonl --device cuda:0 --batch_size 1\\\"\", \"finished_at\": \"2026-05-14T00:33:32.617Z\", \"training_hours\": 0.73}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"completed_at\": \"2026-05-13T23:45:39.272Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:45:40.115539+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T00:33:34.349694+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"诊断完成: EXIT_CODE=127, bash: line 1: python3: command not found。Root cause: 同 phase2_scierc_full_s1, submit 未激活 conda。修复方案同上。retry_count=0, 自动重试中。\"}}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 run_constrained_extraction.py --mode semantic_only ...\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"data_path\": \"/root/schema_semantic_constrained_ie/data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"note\": \"retry #2: bash -c wrapping fixes EXIT_CODE=127\"}, \"pid\": \"134202\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/phase2_scierc_semantic_only.log\", \"conclusion\": \"success\", \"metrics\": {\"total_samples\": 551, \"total_triples\": 1726, \"total_entities\": 2474, \"json_parse_rate\": 1, \"entity_type_violation_rate\": 0.004, \"relation_vocabulary_violation_rate\": 0.0151, \"domain_range_violation_rate\": 0.1165, \"cross_field_consistency_violation_rate\": 0.0271, \"entity_f1\": 0.3101, \"entity_precision\": 0.2605, \"entity_recall\": 0.3831, \"relation_f1\": 0.0815, \"relation_precision\": 0.0637, \"relation_recall\": 0.1129, \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/phase2_scierc_semantic_only_v2.jsonl\"}, \"phase2_scierc_grammar_only\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-13T21:48:43.487Z\", \"updated_at\": \"2026-05-14T18:31:29.442Z\", \"hypothesis\": \"Grammar-only constrained decoding (XGrammar JSON schema + enum) 能否消除 relation vocabulary violations 同时不影响 F1？预期 rv_violation→0%, dr_violation 不变\", \"reproduce\": {\"finished_at\": \"2026-05-13T23:39:02.641Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-13T22:38:46.650Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T22:38:47.328842+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:39:03.395560+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"诊断中: 进程到 176/551 无 traceback 静默退出。cron 追踪 stale PID 导致 5× dead 判定。已派 Worker diagnose:phase2_scierc_grammar_only 深查。\"}}, \"notes\": \"进程从未崩溃。原 'crash' 判定是 cron 追踪 stale PID 123425（已杀的 batch script）导致 5× dead 误报。实际进程 PID 126473 一直在 GPU 1 正常运行。nvidia-smi 确认: GPU 1 上 grammar_only(126473) + unconstrained(126948) 共享，各占 ~16.5GB，利用率 92%。\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode grammar_only --dataset scierc --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/phase2_scierc_grammar_only.jsonl --device cuda:0 --batch_size 1\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:1\"], \"pid\": \"126473\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"log_path\": \"~/runs/schema_semantic_constrained_ie/phase2_scierc_grammar_only.log\", \"note\": \"CUDA_VISIBLE_DEVICES=1 by submit_training_job. 进程从未崩溃 — 'crash' 是 cron 追踪 stale PID 123425 的误报。PID 126473 一直在跑。两个 Phase 2 实验共享 GPU 1（各 ~16.5GB），利用率 92%。\"}, \"metrics\": {\"total_samples\": 551, \"total_triples\": 1725, \"total_entities\": 2474, \"json_parse_rate\": 1, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0, \"domain_range_violation_rate\": 0.1484, \"cross_field_consistency_violation_rate\": 0.0008, \"entity_f1\": 0.3098, \"entity_precision\": 0.2598, \"entity_recall\": 0.3837, \"relation_f1\": 0.0823, \"relation_precision\": 0.0643, \"relation_recall\": 0.114, \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/phase2_scierc_grammar_only.jsonl\", \"conclusion\": \"success\"}, \"phase2_scierc_unconstrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:19:07.120Z\", \"updated_at\": \"2026-05-14T18:31:26.645Z\", \"hypothesis\": \"Phase 2 unconstrained baseline — 使用与 constrained 实验完全相同的代码路径和 prompt，确保 F1 对比公平。预期结果接近 Phase 0 (entity_f1=0.31, relation_f1=0.08)\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode unconstrained --dataset scierc --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/phase2_scierc_unconstrained.jsonl --device cuda:0 --batch_size 1\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:1\"], \"pid\": \"126948\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/phase2_scierc_unconstrained.log\", \"submitted_at\": \"2026-05-13T22:20:28.660Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"note\": \"CUDA_VISIBLE_DEVICES=1 injected by submit_training_job. Progress 353/551 at 23:10 UTC\", \"wall_clock_seconds\": 5186.0, \"gpu_hours\": 1.44}, \"reproduce\": {\"finished_at\": \"2026-05-13T23:44:02.820Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:44:06.470330+00:00\"}]}, \"metrics\": {\"json_parse_rate\": 1, \"entity_f1\": 0.3101, \"entity_precision\": 0.2605, \"entity_recall\": 0.3831, \"relation_f1\": 0.0823, \"relation_precision\": 0.0644, \"relation_recall\": 0.114, \"entity_type_violation_rate\": 0.004, \"relation_vocabulary_violation_rate\": 0.0139, \"domain_range_violation_rate\": 0.1537, \"cross_field_consistency_violation_rate\": 0.0008, \"total_triples\": 1724, \"total_entities\": 2474, \"total_samples\": 551, \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/phase2_scierc_unconstrained.jsonl\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/phase2_scierc_unconstrained.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T23:46:54.651Z\"}, \"phase2_docred_full_s1\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-14T02:07:20.166Z\", \"updated_at\": \"2026-05-14T18:31:19.721Z\", \"hypothesis\": \"Grammar+Semantic 双层约束 (S1) 在 DocRED (96 relations) 上能否复现 SciERC 的 DR 消除效果 (15.37%→0.93%)？DocRED 约束更紧 (avg 5.68 valid pairs)，DR baseline 更高 (18.7%)，验证 OntoCoDec 在复杂 schema 上的泛化性。\", \"notes\": \"DR 18.46%→10.19% (↓44.8%). RV 29.66%→0.03% (↓99.9%), ET 8.18%→0% (↓100%). R-F1 7.74%→8.23% (+0.49pp), E-F1 58.15%→59.37% (+1.22pp). F1 method: all_set (OOV predictions included in denominator). 之前 recognized_set 方法 (R-F1=9.33%→8.17%, -1.16pp) 是错误的——它过滤了 unconstrained 的 5189 个 OOV predictions，人为抬高 precision。Grammar-only DR 上升(18.46→26.17%)是审稿必问点：grammar 强制 valid relation name 后 entity type 与新 relation 的 domain/range 不匹配加剧，恰好证明 semantic 层必要性。\", \"completed_at\": \"2026-05-14T02:55:47.271Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"修复后重启 (PID 157042, tmux: phase2_docred_full_s1, cuda:1)。根因: TypeConstraintProcessor._apply_type_mask 在 allowed_types 与 grammar-valid tokens 无交集时，把所有 grammar-valid tokens 设为 -inf，导致 argmax 选中 grammar-invalid token (logit=-1e10 > -inf)。修复: _apply_type_mask 增加安全检查，若无 semantically-allowed type 有非 grammar-masked logit，跳过 semantic masking 交由 grammar 控制。Dry-run 验证 doc 88(原崩溃点)+7 docs 全部通过。--resume 从 87 继续，当前 89/998。\"}, \"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T08:29:08.943533+00:00\"}]}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/docred_full_s1.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 4096 --resume\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:1\"], \"pid\": \"157042\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"log_path\": \"~/runs/schema_semantic_constrained_ie/phase2_docred_full_s1.log\", \"fix_applied\": \"type_mask_processor.py: semantic mask safety check — skip semantic masking when allowed_types have no non-grammar-masked logits\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T08:29:07.765Z\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/docred_full_s1.jsonl\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/phase2_docred_full_s1.log\", \"metrics\": {\"documents_checked\": 987, \"parse_failures\": 11, \"total_entities\": 20187, \"total_triples\": 17341, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0.0003, \"domain_range_violation_rate\": 0.1021, \"cross_field_consistency_violation_rate\": 0.0257, \"entity_f1\": 59.37, \"entity_precision\": 58.45, \"entity_recall\": 59.63, \"relation_f1\": 8.23, \"relation_precision\": 6.99, \"relation_recall\": 10.01, \"unrecognized_relations\": 5, \"f1_method\": \"all_set\", \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}}, \"phase2_docred_semantic_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T04:40:51.107Z\", \"updated_at\": \"2026-05-14T18:31:13.783Z\", \"hypothesis\": \"Semantic-only constrained decoding 在 DocRED (96 relations, avg 5.68 valid pairs) 上的 DR 降低幅度。SciERC semantic_only DR↓24% (15.37→11.65%)，DocRED 约束更紧预期效果更明显。关键验证 Claim 3 enabling dependency：semantic_only 无法消除 RV/ET（需 grammar），证明两层互补非替代。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode semantic_only --dataset docred --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/docred_semantic_only.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 4096\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:1\"], \"pid\": \"172859\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/phase2_docred_semantic_only.log\", \"submitted_at\": \"2026-05-14T08:30:43.644Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 21989.5, \"gpu_hours\": 6.11}, \"server\": \"westd-16980\", \"gpu\": \"cuda:1\", \"pid\": \"172859\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/phase2_docred_semantic_only.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode semantic_only --dataset docred --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/docred_semantic_only.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 4096\\\"\", \"finished_at\": \"2026-05-14T14:13:58.319Z\"}, \"notes\": \"DocRED semantic-only（checker 修复后定稿数字）。ET 10.44% (修复前 18.44%, -8pp: strip 修 507 假阳性 + PERSON alias 修 1108 假阳性)。DR 13.84% (修复前 15.05%, -1.21pp: normalize 也修正了 DR pair 匹配)。CF 1.05% (修复前 2.29%)。残余 ET 2107 violations 是真实退化：WORK(823)/EVENT(743)/ETHNIC_GROUP(137) 等非标类型。F1 无变化。998 lines, 0 duplicates。\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T14:13:59.612547+00:00\"}]}, \"metrics\": {\"documents_checked\": 987, \"parse_failures\": 11, \"total_entities\": 20185, \"total_triples\": 17571, \"entity_type_violation_rate\": 0.0422, \"relation_vocabulary_violation_rate\": 0.2987, \"domain_range_violation_rate\": 0.1384, \"cross_field_consistency_violation_rate\": 0.0105, \"entity_f1\": 57.81, \"entity_precision\": 57.27, \"entity_recall\": 58.37, \"relation_f1\": 7.7, \"relation_precision\": 6.54, \"relation_recall\": 9.37, \"f1_method\": \"all_set\", \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\", \"et_v1\": 0.1044, \"et_fix_note\": \"v1 triple-counted ET across entity_list + relation head/tail; v2 deduplicates by (text, normalized_type)\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/docred_semantic_only.jsonl\", \"completed_at\": \"2026-05-14T14:37:13.158Z\"}, \"phase2_docred_unconstrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T04:40:50.853Z\", \"updated_at\": \"2026-05-14T18:31:10.378Z\", \"hypothesis\": \"DocRED Phase 2 unconstrained baseline — 使用与 constrained 实验完全相同的 Phase 2 pipeline 和 prompt，确保消融表 F1/violation 对比公平。预期 DR~18.7%, RV~28.9%, ET~7.5%（接近 Phase 0）。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode unconstrained --dataset docred --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/docred_unconstrained.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 4096\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"170502\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/phase2_docred_unconstrained.log\", \"submitted_at\": \"2026-05-14T07:40:49.115Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 20601.7, \"gpu_hours\": 5.72}, \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"pid\": \"170502\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/phase2_docred_unconstrained.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode unconstrained --dataset docred --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/docred_unconstrained.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 4096\\\"\", \"finished_at\": \"2026-05-14T13:10:49.905Z\"}, \"notes\": \"✅ Phase 2 重新分析完成。998 lines, 0 duplicates — 文件干净无残留。正确值: DR=18.5%, RV=29.7%, ET=8.2%, E-F1=58.15%, R-F1=7.74%。F1 method: all_set (Reviewer 2026-05-14 确认正确)。论文可 claim: constrained decoding 不损失 R-F1。\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T13:10:51.383206+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"documents_checked\": 986, \"parse_failures\": 12, \"total_entities\": 20171, \"total_triples\": 17497, \"entity_type_violation_rate\": 0.0248, \"relation_vocabulary_violation_rate\": 0.2966, \"domain_range_violation_rate\": 0.1846, \"cross_field_consistency_violation_rate\": 0.001, \"entity_f1\": 58.15, \"entity_precision\": 57.26, \"entity_recall\": 58.32, \"relation_f1\": 7.74, \"relation_precision\": 6.55, \"relation_recall\": 9.46, \"unrecognized_relations\": 5189, \"f1_method\": \"all_set (includes OOV predictions in denominator)\", \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\", \"et_v1\": 0.0818, \"et_fix_note\": \"v1 triple-counted ET across entity_list + relation head/tail; v2 deduplicates by (text, normalized_type)\"}, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/docred_unconstrained.jsonl\", \"completed_at\": \"2026-05-14T13:24:10.838Z\"}, \"mvp_phase0_docred_schema_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T00:36:06.125Z\", \"updated_at\": \"2026-05-14T02:56:53.324Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_extraction_docred.py --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/docred/dev.json --output_path outputs/raw_outputs_docred_schema.jsonl --device cuda:0 --constraints_path data/docred/ontology_constraints_docred.json --prompt_mode schema_informed --batch_size 4 --resume\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"data_path\": \"/root/schema_semantic_constrained_ie/data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"note\": \"Resume from killed mvp_phase0_docred_schema. Original ran ~3.5h before being killed by cleanup Worker.\"}, \"hypothesis\": \"Schema-informed prompt 在 DocRED (96 relation types) 上的违规率降低幅度是否小于 SciERC (7 types)？验证约束空间越大 prompt 级干预越力不从心。（从被误杀的 mvp_phase0_docred_schema 恢复，--resume）\", \"notes\": \"归档：mvp_phase0_docred_schema 已完成全量 998/998 并有完整 metrics，此 r2 续跑实验不再需要。\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T02:56:53.324Z\"}, \"phase2_s2_pilot50\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:25:10.566Z\", \"updated_at\": \"2026-05-14T02:04:44.195Z\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode full_s2 --dataset scierc --num_samples 50 --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --device cuda:0\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"data_path\": \"/root/schema_semantic_constrained_ie/data/processed_data/test.json\", \"data_count\": 50, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/phase2_s2_pilot50.jsonl\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/phase2_s2_pilot50.log\", \"note\": \"S2 50-sample pilot run. D/R violation=0% verified. relation_f1=0.0 root cause under investigation by Worker analysis:s2_relation_f1_rootcause.\"}, \"hypothesis\": \"S2 两通道约束解码 50 样本 pilot — 验证 PositionDetector 修复后 D/R violation=0%，评估 relation_f1 质量\", \"conclusion\": \"success\", \"metrics\": {\"domain_range_violation_rate\": 0.0205, \"relation_vocabulary_violation_rate\": 0, \"relation_f1\": 0.1008, \"samples\": 50, \"predicted_relations\": 146, \"true_positives\": 13, \"gold_relations\": 112, \"entity_f1_approx\": 0.29, \"note\": \"DR 修正: 原值 0 来自 dryrun (n=25 triples)。实际 pilot50 DR=3/146=2.05% (来自 violation_report_s2_pilot50.json)。\"}, \"completed_at\": \"2026-05-13T23:26:16.718Z\", \"notes\": \"S2 pilot 实际 relation_f1=0.1008（非此前误报的 0.0）。根因：原 F1=0 来自 10 样本 dryrun 的 violation_report，不是 pilot50 评估结果。S2 架构无问题，F1 与 unconstrained 持平。FP 分析: entity span 质量差是主因(52.6% head+tail 都不匹配 gold)。改进方向: few-shot entity prompt / 编号引用格式 / 阻止自引用。\"}, \"mvp_phase0_docred_schema\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T17:58:18.184Z\", \"updated_at\": \"2026-05-14T01:49:57.097Z\", \"hypothesis\": \"Schema-informed prompt 在 DocRED (96 relation types) 上的违规率降低幅度是否小于 SciERC (7 types)？验证约束空间越大 prompt 级干预越力不从心\", \"spec\": {\"command\": \"python3 run_extraction_docred.py --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/docred/dev.json --output_path outputs/raw_outputs_docred_schema.jsonl --device cuda:0 --constraints_path data/docred/ontology_constraints_docred.json --prompt_mode schema_informed --batch_size 4\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"116365\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/mvp_phase0_docred_schema.log\", \"submitted_at\": \"2026-05-13T20:13:18.695Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"wall_clock_seconds\": 13513.6, \"gpu_hours\": 3.75}, \"reproduce\": {\"finished_at\": \"2026-05-13T23:58:31.565Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T23:58:32.325Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:58:33.241310+00:00\"}]}, \"notes\": \"Resume 完成 998/998 docs. Schema-informed prompt 结果: ET=0.61% (baseline 7.5%, Δ-6.89%), RV=18.4% (baseline 28.9%, Δ-10.5%), DR=12.8% (baseline 18.7%, Δ-5.9%). 全维度显著改善。\", \"metrics\": {\"total_documents\": 998, \"documents_checked\": 943, \"parse_failures\": 55, \"json_parse_rate\": 0.9449, \"total_entities\": 19524, \"total_triples\": 16782, \"entity_type_violations\": 119, \"entity_type_violation_rate\": 0.0061, \"relation_vocabulary_violations\": 3090, \"relation_vocabulary_violation_rate\": 0.1841, \"relation_fuzzy_matches\": 85, \"domain_range_violations\": 2154, \"domain_range_violation_rate\": 0.1284, \"cross_field_consistency_violations\": 29, \"cross_field_consistency_violation_rate\": 0.0015, \"total_violations_any\": 5392, \"total_violation_rate\": 0.1485, \"go_nogo_metric_dr\": 0.1284}, \"checkpoint_path\": \"outputs/raw_outputs_docred_schema.jsonl\"}, \"mvp_phase0_violation_rate_docred\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T17:38:05.075Z\", \"updated_at\": \"2026-05-13T21:46:35.193Z\", \"hypothesis\": \"DocRED 有 96 relation types，约束空间远大于 SciERC (7 types)，预期 unconstrained LLM 的 per-triple violation rate 显著高于 SciERC，验证违规率与约束空间复杂度正相关\", \"spec\": {\"command\": \"python3 run_extraction_docred.py --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/docred/dev.json --output_path outputs/raw_outputs_docred.jsonl --device cuda:0 --batch_size 4 --resume\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:1\"], \"data_path\": \"/root/schema_semantic_constrained_ie/data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"pid\": 113148, \"resumed_from_doc\": 265, \"batch_size\": 4, \"current_progress\": 281, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/raw_outputs_docred.jsonl\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/mvp_phase0_violation_rate_docred.log\"}, \"metrics\": {\"total_docs\": 998, \"parsed_docs\": 962, \"json_parse_rate\": 0.964, \"total_entities\": 19099, \"total_triples\": 16540, \"entity_type_violation_rate\": 0.075, \"relation_vocabulary_violation_rate\": 0.289, \"domain_range_violation_rate\": 0.187, \"cross_field_consistency_violation_rate\": 0.0008, \"go_nogo_metric\": 0.187, \"fuzzy_matches\": 126, \"top_dr_violations_by_rate\": {\"P35_head_of_state\": 1, \"P710_participant\": 0.919, \"P172_ethnic_group\": 0.875}, \"top_dr_violations_by_count\": {\"P31_instance_of\": {\"violations\": 322, \"total\": 533, \"rate\": 0.604}, \"P1001_applies_to_jurisdiction\": {\"violations\": 264, \"total\": 594, \"rate\": 0.444}, \"P1344_participant_in\": {\"violations\": 194, \"total\": 312, \"rate\": 0.622}}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T21:46:35.193Z\"}, \"mvp_phase0_scierc_schema\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T17:58:17.259Z\", \"updated_at\": \"2026-05-13T20:58:13.410Z\", \"hypothesis\": \"Schema-informed prompt（显式给出 domain/range 约束）能否降低违规率？与 minimal prompt 对比，若违规率仍 >5% 则证明 prompt 级干预不足以替代 decoding-time enforcement\", \"spec\": {\"command\": \"python3 run_extraction.py --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/processed_data/test.json --output_path outputs/raw_outputs_schema.jsonl --backend transformers --prompt_mode schema_informed --constraints_path ontology_constraints.json\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"110676\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/mvp_phase0_scierc_schema.log\", \"submitted_at\": \"2026-05-13T19:11:32.249Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/raw_outputs_schema.jsonl\", \"wall_clock_seconds\": 3650.3, \"gpu_hours\": 1.01}, \"metrics\": {\"domain_range_violation_rate\": 0.0578, \"relation_vocabulary_violation_rate\": 0.003, \"entity_type_violation_rate\": 0, \"total_violation_rate\": 0.0253, \"go_nogo_metric\": 0.0578, \"total_triples\": 1661, \"vs_minimal_dr_reduction\": -0.624, \"per_relation\": {\"Used-for\": {\"rate\": \"TBD\"}, \"Feature-of\": {\"delta_pp\": -22.3}, \"Part-of\": {\"delta_pp\": -22.5}, \"Compare\": {\"delta_pp\": -14.8}, \"Evaluate-for\": {\"delta_pp\": 5.8}}, \"mcnemar_all_significant\": true}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T20:12:22.502Z\"}, \"mvp_phase0_violation_rate\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T17:35:38.680Z\", \"updated_at\": \"2026-05-13T19:13:34.510Z\", \"hypothesis\": \"Unconstrained LLM (Qwen3-8B) 在 SciERC zero-shot IE 任务上的本体类型约束违反率 >5%，证明解码时约束强制的必要性\", \"spec\": {\"command\": \"python3 run_extraction.py --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/processed_data/test.json --output_path outputs/raw_outputs.jsonl --backend transformers\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"106528\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/mvp_phase0_violation_rate.log\", \"submitted_at\": \"2026-05-13T18:05:45.748Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/raw_outputs.jsonl\", \"wall_clock_seconds\": 4068.8, \"gpu_hours\": 1.13}, \"metrics\": {\"total_triples\": 1724, \"total_entities\": 2474, \"json_parse_rate\": 1, \"entity_type_violation_rate\": 0.004, \"relation_vocabulary_violation_rate\": 0.0139, \"domain_range_violation_rate\": 0.1537, \"cross_field_consistency_violation_rate\": 0.0008, \"go_nogo_metric\": 0.1537, \"entity_f1\": 0.3101, \"relation_f1\": 0.0823, \"per_relation\": {\"Used-for\": {\"total\": 787, \"dr_violations\": 6, \"rate\": 0.0076}, \"Conjunction\": {\"total\": 32, \"dr_violations\": 0, \"rate\": 0}, \"Hyponym-of\": {\"total\": 124, \"dr_violations\": 18, \"rate\": 0.1452}, \"Evaluate-for\": {\"total\": 133, \"dr_violations\": 32, \"rate\": 0.2406}, \"Part-of\": {\"total\": 72, \"dr_violations\": 18, \"rate\": 0.25}, \"Feature-of\": {\"total\": 486, \"dr_violations\": 163, \"rate\": 0.3354}, \"Compare\": {\"total\": 66, \"dr_violations\": 28, \"rate\": 0.4242}}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T19:13:34.510Z\"}}, \"count\": 137, \"total\": 137, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4772}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 13_

<details><summary>Logged reasoning block</summary>

```text
The registry is too large. Let me filter for just the specific exp_ids mentioned in the paper, and also search for runtime/beam related experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "02f38ee2-9285-4c68-8ba3-b656e5c91e0c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VvrU6TTiBLoUuKoafQfsnH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 708,
      "cache_read_input_tokens": 25419,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 708
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

Registry is large. Let me query the specific exp_ids mentioned in the paper, plus search for runtime and beam experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "bf309dbe-e9de-4304-909d-5b9229261a96",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VvrU6TTiBLoUuKoafQfsnH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 708,
      "cache_read_input_tokens": 25419,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 708
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01D8xQrb11BaeiqcPhBfbSkE`</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "filters": {
    "exp_id": "r16_70b_scierc_zs_s1"
  },
  "fields": [
    "*"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "88600327-b248-40ba-a440-34af47d094b8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VvrU6TTiBLoUuKoafQfsnH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 708,
      "cache_read_input_tokens": 25419,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 708
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

_source line 16 · 2026-05-22T04:09:15.805Z_

<details><summary>↩ Tool result · `toolu_01D8xQrb11BaeiqcPhBfbSkE`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4053}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "603b6070-f1f2-4a47-91fe-064261e870e2",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4053}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4053}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01VPw3Q9HfLjK5XMbVFspyk6`</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "filters": {
    "exp_id": "70b_lora_scierc"
  },
  "fields": [
    "*"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "34a341e3-4077-4d1f-a734-2356c01d7b44",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VvrU6TTiBLoUuKoafQfsnH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 708,
      "cache_read_input_tokens": 25419,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 708
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

_source line 18 · 2026-05-22T04:09:16.346Z_

<details><summary>↩ Tool result · `toolu_01VPw3Q9HfLjK5XMbVFspyk6`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4334}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "7d9d3ec7-76e4-440d-b3f3-4f05ac11be00",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4334}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4334}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01FbvhswXUC4pSTJsGdnnrEi`</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "filters": {
    "exp_id": "70b_lora_docred_200"
  },
  "fields": [
    "*"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "b0becfde-79bc-4781-8650-a182334b326d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VvrU6TTiBLoUuKoafQfsnH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 708,
      "cache_read_input_tokens": 25419,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 708
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

_source line 20 · 2026-05-22T04:09:17.248Z_

<details><summary>↩ Tool result · `toolu_01FbvhswXUC4pSTJsGdnnrEi`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3882}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "30dfa19d-db57-4d5c-8329-c3374ee03bfe",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.3882}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3882}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01MZuSiSTvcSeuQAaMptdcha`</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "filters": {
    "exp_id": "trie_qwen_ft_scierc"
  },
  "fields": [
    "*"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "ef149c3b-c8d9-4414-8dce-ce6883ad9180",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VvrU6TTiBLoUuKoafQfsnH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 708,
      "cache_read_input_tokens": 25419,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 708
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

_source line 22 · 2026-05-22T04:09:18.183Z_

<details><summary>↩ Tool result · `toolu_01MZuSiSTvcSeuQAaMptdcha`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3957}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "a5216326-214c-47e8-8ce0-6848ce22c929",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.3957}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3957}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01LHBuB5y2zpuDQEstwnvCeS`</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "filters": {
    "exp_id": "trie_qwen_zs_scierc"
  },
  "fields": [
    "*"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "e57cbc5c-c8d2-4f38-87cb-520bcf21e340",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VvrU6TTiBLoUuKoafQfsnH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 708,
      "cache_read_input_tokens": 25419,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 708
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

_source line 24 · 2026-05-22T04:09:18.675Z_

<details><summary>↩ Tool result · `toolu_01LHBuB5y2zpuDQEstwnvCeS`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4033}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "3e12cc21-078b-417c-8056-31574cd9ca40",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4033}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4033}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01Bd5AA4k8VkEwo6YCRFuBP6`</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "filters": {
    "exp_id": "trie_llama_ft_scierc"
  },
  "fields": [
    "*"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "53d5eac7-406c-47a2-97fd-a916f7e9d217",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VvrU6TTiBLoUuKoafQfsnH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 708,
      "cache_read_input_tokens": 25419,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 708
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

_source line 26 · 2026-05-22T04:09:19.661Z_

<details><summary>↩ Tool result · `toolu_01Bd5AA4k8VkEwo6YCRFuBP6`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4385}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "7b388466-62fc-42ae-80dd-d0ea3ee59459",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4385}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4385}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_011jWHLuzqD6Zt71C5KEHoyC`</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "filters": {
    "exp_id": "trie_llama_zs_scierc"
  },
  "fields": [
    "*"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "b650fb14-cfe5-4e4f-aae5-f370a8658553",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VvrU6TTiBLoUuKoafQfsnH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 708,
      "cache_read_input_tokens": 25419,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 708
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

_source line 28 · 2026-05-22T04:09:20.410Z_

<details><summary>↩ Tool result · `toolu_011jWHLuzqD6Zt71C5KEHoyC`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4707}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "4543ec2f-fec8-48a1-a7b8-77d6572c7eb5",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4707}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4707}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 29_

<details><summary>Logged reasoning block</summary>

```text
All 7 exp_ids returned 0 results. The exact exp_id filter might not be matching. Let me try to search the registry differently - maybe the field name isn't "exp_id" or the values are slightly different. Let me look at the raw registry file to understand its structure, or try a broader query.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "5136f868-dd69-4416-a674-1deb6a2c1825",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014JvmMQFG9q7NfCsRCmk9yx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1636,
      "cache_read_input_tokens": 26127,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1636
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

_source line 30_

All 7 exp_ids returned 0 results. The exp_id field name might differ. Let me check the registry structure and search for these experiments by name/keyword.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "3dce26e1-c100-4fd4-8586-7eafc0e245c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014JvmMQFG9q7NfCsRCmk9yx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1636,
      "cache_read_input_tokens": 26127,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1636
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

_source line 31_

<details open><summary>🔧 Tool call — Bash · `toolu_012vbR9wJHuyzzyCPi4FR9iU`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/06688fc2-d26c-40b0-8ebe-68d505b40c0d/tool-results/mcp-agent-ml-research-read_registry-1779422951081.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n# Show first experiment's keys to understand structure\nfor eid in list(exps.keys())[:3]:\n    print(f'=== {eid} ===')\n    print(json.dumps(list(exps[eid].keys())))\n    print()\n\"",
  "description": "Inspect registry structure - first 3 experiments' keys"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "41376e89-6613-4ec7-8c5b-e7793c3edeb5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014JvmMQFG9q7NfCsRCmk9yx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1636,
      "cache_read_input_tokens": 26127,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1636
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

_source line 32 · 2026-05-22T04:09:32.846Z_

<details><summary>↩ Tool result · `toolu_012vbR9wJHuyzzyCPi4FR9iU`</summary>

```text
=== d066_sweep_llama_beam8_unc ===
["status", "retry_count", "created_at", "updated_at", "hypothesis", "parent", "spec", "conclusion", "metrics", "completed_at"]

=== d066_sweep_llama_beam2_s1 ===
["status", "retry_count", "created_at", "updated_at", "hypothesis", "parent", "spec", "conclusion", "metrics", "completed_at"]

=== eval_70b_lora_docred_200_unconstrained ===
["status", "retry_count", "created_at", "updated_at", "hypothesis", "parent", "spec"]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "9a0caf66-6fe1-449b-9a6c-9b2b13b47c21",
  "tool_use_result": {
    "stdout": "=== d066_sweep_llama_beam8_unc ===\n[\"status\", \"retry_count\", \"created_at\", \"updated_at\", \"hypothesis\", \"parent\", \"spec\", \"conclusion\", \"metrics\", \"completed_at\"]\n\n=== d066_sweep_llama_beam2_s1 ===\n[\"status\", \"retry_count\", \"created_at\", \"updated_at\", \"hypothesis\", \"parent\", \"spec\", \"conclusion\", \"metrics\", \"completed_at\"]\n\n=== eval_70b_lora_docred_200_unconstrained ===\n[\"status\", \"retry_count\", \"created_at\", \"updated_at\", \"hypothesis\", \"parent\", \"spec\"]",
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

_source line 33_

<details><summary>Logged reasoning block</summary>

```text
The experiment IDs are the keys of the experiments dict, not a field. Let me search for the exp_ids from the paper. The registry uses the experiment ID as the key. The paper references `r16_70b_scierc_zs_s1`, `70b_lora_scierc`, `70b_lora_docred_200`, etc. Let me search for these as keys, and also find runtime/beam related experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "3f0121e6-68b2-4f5e-b3c1-ec98ee4b218b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Evgh8xDAD8FmzS94isTdre",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 578,
      "cache_read_input_tokens": 27763,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 578
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

The experiment IDs are the dictionary keys. Let me search for all relevant experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "ca86dfcc-f092-46ff-b30b-a14aedf5e209",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Evgh8xDAD8FmzS94isTdre",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 578,
      "cache_read_input_tokens": 27763,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 578
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

<details open><summary>🔧 Tool call — Bash · `toolu_01WXegjir6TS9UPoX6kqEPKJ`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/06688fc2-d26c-40b0-8ebe-68d505b40c0d/tool-results/mcp-agent-ml-research-read_registry-1779422951081.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n\n# Search for exp_ids referenced in the paper\npaper_ids = ['r16_70b_scierc_zs_s1', '70b_lora_scierc', '70b_lora_docred_200',\n             'trie_qwen_ft_scierc', 'trie_qwen_zs_scierc', 'trie_llama_ft_scierc', 'trie_llama_zs_scierc']\n\nprint('=== EXACT MATCHES ===')\nfor pid in paper_ids:\n    if pid in exps:\n        print(f'FOUND: {pid}')\n        print(json.dumps(exps[pid], indent=2))\n    else:\n        print(f'NOT FOUND: {pid}')\n\nprint()\nprint('=== PARTIAL MATCHES ===')\n# Search for keys containing relevant substrings\nkeywords = ['70b', 'trie', 'runtime', 'beam', 'latency', 'overhead']\nfor kw in keywords:\n    matches = [k for k in exps.keys() if kw in k.lower()]\n    if matches:\n        print(f'--- Keyword: {kw} ({len(matches)} matches) ---')\n        for m in matches:\n            print(f'  {m}  status={exps[m].get(\\\"status\\\",\\\"?\\\")}')\n\"",
  "description": "Search registry for paper-referenced exp_ids and related experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "82ddf334-a387-401e-9284-48c4401b201e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Evgh8xDAD8FmzS94isTdre",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 578,
      "cache_read_input_tokens": 27763,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 578
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

_source line 36 · 2026-05-22T04:09:44.277Z_

<details><summary>↩ Tool result · `toolu_01WXegjir6TS9UPoX6kqEPKJ`</summary>

```text
=== EXACT MATCHES ===
FOUND: r16_70b_scierc_zs_s1
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-21T04:11:52.091Z",
  "updated_at": "2026-05-21T07:09:31.198Z",
  "hypothesis": "Llama-3.1-70B-Instruct-AWQ-INT4 with Full S1 constrained decoding on SciERC ZS will achieve DR\u21920% with R-F1 stable vs unconstrained, extending 70B DocRED results to SciERC and confirming scale-independent constraint effectiveness",
  "spec": {
    "command": "bash /root/schema_semantic_constrained_ie/run_70b_scierc_zs.sh",
    "server": "westd-16980",
    "gpu": "cuda:1",
    "pid": 808988,
    "data_path": "SciERC test set (551 sentences)",
    "data_count": 551,
    "model_name": "Llama-3.1-70B-Instruct-AWQ-INT4",
    "model_path": "/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4",
    "seed": 42,
    "checkpoint_path": "N/A (ZS eval)",
    "log_path": "/root/schema_semantic_constrained_ie/outputs/r16_70b_scierc_zs_s1.log"
  },
  "metrics": {
    "E_F1": 35.19,
    "R_F1": 11.24,
    "DR_pct": 0,
    "RV_pct": 0,
    "ET_pct": 0,
    "CF_pct": 3.5,
    "parse_fail_pct": 0,
    "samples": 551,
    "baseline_unc_E_F1": 35.21,
    "baseline_unc_R_F1": 11.15,
    "baseline_unc_DR_pct": 6.41,
    "baseline_unc_RV_pct": 0.61,
    "baseline_unc_CF_pct": 0
  },
  "conclusion": "success",
  "completed_at": "2026-05-21T07:09:31.199Z"
}
NOT FOUND: 70b_lora_scierc
NOT FOUND: 70b_lora_docred_200
NOT FOUND: trie_qwen_ft_scierc
NOT FOUND: trie_qwen_zs_scierc
NOT FOUND: trie_llama_ft_scierc
NOT FOUND: trie_llama_zs_scierc

=== PARTIAL MATCHES ===
--- Keyword: 70b (11 matches) ---
  eval_70b_lora_docred_200_unconstrained  status=RUNNING
  r16_70b_lora_scierc_eval  status=PREPARING
  eval_70b_lora_scierc_unconstrained  status=RUNNING
  r16_70b_lora_docred  status=DONE
  r16_70b_lora_scierc  status=DONE
  r16_70b_docred_zs_s1  status=DONE
  r16_70b_scierc_zs_s1  status=DONE
  70b_docred_constrained  status=DONE
  70b_docred_unconstrained  status=DONE
  70b_scierc_unconstrained  status=DONE
  70b_scierc_constrained  status=DONE
--- Keyword: trie (4 matches) ---
  r16_trie_llama_zs_scierc  status=DONE
  r16_trie_llama_ft_scierc  status=DONE
  r16_trie_qwen_zs_scierc  status=DONE
  r16_trie_qwen_ft_scierc  status=DONE
--- Keyword: beam (28 matches) ---
  d066_sweep_llama_beam8_unc  status=DONE
  d066_sweep_llama_beam2_s1  status=DONE
  d066_sweep_llama_docred_beam4_s1  status=DONE
  r14_qwen_docred_beam4_998  status=DONE
  r14_llama_docred_beam4_998  status=DONE
  d066_sweep_llama_scierc_beam8_s1_551  status=DONE
  d066_sweep_llama_scierc_beam4_s1_551  status=DONE
  d066_sweep_llama_docred_beam4_unc  status=DONE
  d066_sweep_llama_docred_beam1_s1  status=DONE
  d066_sweep_llama_beam8_s1  status=DONE
  d066_sweep_llama_scierc_beam2_s1_551  status=DONE
  d066_sweep_llama_scierc_beam1_unc  status=DONE
  d066_sweep_llama_docred_beam1_unc  status=DONE
  d066_beam_sweep  status=ANALYZING
  d066_docred_beam_sweep  status=DONE
  d068_constraint_guided_beam_pilot  status=DONE
  d064_docred_full_beam  status=DONE
  d062_beam_latency  status=DONE
  q1_llama_lora_scierc_beam4  status=DONE
  w10_qwen_scierc_ft_beam_4  status=DONE
  w10_beam_ablation_k8  status=DONE
  w9_mistral_docred_beam_50  status=DONE
  w10_beam_ablation_k2  status=DONE
  w10_mistral_scierc_beam_551  status=DONE
  w10_llama_docred_beam_50  status=DONE
  w9_qwen_docred_beam_50  status=DONE
  w9_llama_scierc_beam_551  status=DONE
  beam_search_scierc_full_551  status=DONE
--- Keyword: latency (4 matches) ---
  d062_beam_latency  status=DONE
  p8c_ft_scierc_latency  status=DONE
  p8b_docred_latency  status=DONE
  p8_latency_overhead  status=DONE
--- Keyword: overhead (1 matches) ---
  p8_latency_overhead  status=DONE
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "57bd0a81-b881-4aa7-92c3-0e02b011d0ea",
  "tool_use_result": {
    "stdout": "=== EXACT MATCHES ===\nFOUND: r16_70b_scierc_zs_s1\n{\n  \"status\": \"DONE\",\n  \"retry_count\": 0,\n  \"created_at\": \"2026-05-21T04:11:52.091Z\",\n  \"updated_at\": \"2026-05-21T07:09:31.198Z\",\n  \"hypothesis\": \"Llama-3.1-70B-Instruct-AWQ-INT4 with Full S1 constrained decoding on SciERC ZS will achieve DR\\u21920% with R-F1 stable vs unconstrained, extending 70B DocRED results to SciERC and confirming scale-independent constraint effectiveness\",\n  \"spec\": {\n    \"command\": \"bash /root/schema_semantic_constrained_ie/run_70b_scierc_zs.sh\",\n    \"server\": \"westd-16980\",\n    \"gpu\": \"cuda:1\",\n    \"pid\": 808988,\n    \"data_path\": \"SciERC test set (551 sentences)\",\n    \"data_count\": 551,\n    \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4\",\n    \"model_path\": \"/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4\",\n    \"seed\": 42,\n    \"checkpoint_path\": \"N/A (ZS eval)\",\n    \"log_path\": \"/root/schema_semantic_constrained_ie/outputs/r16_70b_scierc_zs_s1.log\"\n  },\n  \"metrics\": {\n    \"E_F1\": 35.19,\n    \"R_F1\": 11.24,\n    \"DR_pct\": 0,\n    \"RV_pct\": 0,\n    \"ET_pct\": 0,\n    \"CF_pct\": 3.5,\n    \"parse_fail_pct\": 0,\n    \"samples\": 551,\n    \"baseline_unc_E_F1\": 35.21,\n    \"baseline_unc_R_F1\": 11.15,\n    \"baseline_unc_DR_pct\": 6.41,\n    \"baseline_unc_RV_pct\": 0.61,\n    \"baseline_unc_CF_pct\": 0\n  },\n  \"conclusion\": \"success\",\n  \"completed_at\": \"2026-05-21T07:09:31.199Z\"\n}\nNOT FOUND: 70b_lora_scierc\nNOT FOUND: 70b_lora_docred_200\nNOT FOUND: trie_qwen_ft_scierc\nNOT FOUND: trie_qwen_zs_scierc\nNOT FOUND: trie_llama_ft_scierc\nNOT FOUND: trie_llama_zs_scierc\n\n=== PARTIAL MATCHES ===\n--- Keyword: 70b (11 matches) ---\n  eval_70b_lora_docred_200_unconstrained  status=RUNNING\n  r16_70b_lora_scierc_eval  status=PREPARING\n  eval_70b_lora_scierc_unconstrained  status=RUNNING\n  r16_70b_lora_docred  status=DONE\n  r16_70b_lora_scierc  status=DONE\n  r16_70b_docred_zs_s1  status=DONE\n  r16_70b_scierc_zs_s1  status=DONE\n  70b_docred_constrained  status=DONE\n  70b_docred_unconstrained  status=DONE\n  70b_scierc_unconstrained  status=DONE\n  70b_scierc_constrained  status=DONE\n--- Keyword: trie (4 matches) ---\n  r16_trie_llama_zs_scierc  status=DONE\n  r16_trie_llama_ft_scierc  status=DONE\n  r16_trie_qwen_zs_scierc  status=DONE\n  r16_trie_qwen_ft_scierc  status=DONE\n--- Keyword: beam (28 matches) ---\n  d066_sweep_llama_beam8_unc  status=DONE\n  d066_sweep_llama_beam2_s1  status=DONE\n  d066_sweep_llama_docred_beam4_s1  status=DONE\n  r14_qwen_docred_beam4_998  status=DONE\n  r14_llama_docred_beam4_998  status=DONE\n  d066_sweep_llama_scierc_beam8_s1_551  status=DONE\n  d066_sweep_llama_scierc_beam4_s1_551  status=DONE\n  d066_sweep_llama_docred_beam4_unc  status=DONE\n  d066_sweep_llama_docred_beam1_s1  status=DONE\n  d066_sweep_llama_beam8_s1  status=DONE\n  d066_sweep_llama_scierc_beam2_s1_551  status=DONE\n  d066_sweep_llama_scierc_beam1_unc  status=DONE\n  d066_sweep_llama_docred_beam1_unc  status=DONE\n  d066_beam_sweep  status=ANALYZING\n  d066_docred_beam_sweep  status=DONE\n  d068_constraint_guided_beam_pilot  status=DONE\n  d064_docred_full_beam  status=DONE\n  d062_beam_latency  status=DONE\n  q1_llama_lora_scierc_beam4  status=DONE\n  w10_qwen_scierc_ft_beam_4  status=DONE\n  w10_beam_ablation_k8  status=DONE\n  w9_mistral_docred_beam_50  status=DONE\n  w10_beam_ablation_k2  status=DONE\n  w10_mistral_scierc_beam_551  status=DONE\n  w10_llama_docred_beam_50  status=DONE\n  w9_qwen_docred_beam_50  status=DONE\n  w9_llama_scierc_beam_551  status=DONE\n  beam_search_scierc_full_551  status=DONE\n--- Keyword: latency (4 matches) ---\n  d062_beam_latency  status=DONE\n  p8c_ft_scierc_latency  status=DONE\n  p8b_docred_latency  status=DONE\n  p8_latency_overhead  status=DONE\n--- Keyword: overhead (1 matches) ---\n  p8_latency_overhead  status=DONE",
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

_source line 37_

<details><summary>Logged reasoning block</summary>

```text
Now I can see the actual registry keys. The paper uses abbreviated exp_ids but the registry has prefixed versions:
- `r16_70b_scierc_zs_s1` → FOUND (exact match)
- `70b_lora_scierc` → actual key is `r16_70b_lora_scierc` (DONE)
- `70b_lora_docred_200` → actual key is `r16_70b_lora_docred` (DONE)


- `trie_qwen_ft_scierc` → actual key is `r16_trie_qwen_ft_scierc` (DONE)
- `trie_qwen_zs_scierc` → actual key is `r16_trie_qwen_zs_scierc` (DONE)
- `trie_llama_ft_scierc` → actual key is `r16_trie_llama_ft_scierc` (DONE)
- `trie_llama_zs_scierc` → actual key is `r16_trie_llama_zs_scierc` (DONE)

Now I need to pull the results for all these experiments along with the runtime and latency metrics.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "d9913d62-ceb5-4903-b931-446d0fec2f90",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QEtED8zvzkgMaiGz2kXjpJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2451,
      "cache_read_input_tokens": 28341,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2451
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

_source line 38_

Found the experiments — the registry uses `r16_` prefix. Let me now fetch the detailed metrics for all relevant experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "0e27d54f-4f96-45ba-90f4-a169f20d74d6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QEtED8zvzkgMaiGz2kXjpJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2451,
      "cache_read_input_tokens": 28341,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2451
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

_source line 39_

<details open><summary>🔧 Tool call — Bash · `toolu_01Vn6ZEpq9akQtDrjAArYnSX`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/06688fc2-d26c-40b0-8ebe-68d505b40c0d/tool-results/mcp-agent-ml-research-read_registry-1779422951081.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n\n# All experiments we need\ntargets = [\n    'r16_70b_scierc_zs_s1',\n    'r16_70b_lora_scierc', 'r16_70b_lora_docred',\n    'r16_trie_qwen_ft_scierc', 'r16_trie_qwen_zs_scierc',\n    'r16_trie_llama_ft_scierc', 'r16_trie_llama_zs_scierc',\n    'p8_latency_overhead', 'p8b_docred_latency', 'p8c_ft_scierc_latency',\n    'd062_beam_latency',\n    # Also check for the beam search key experiments\n    'q1_llama_lora_scierc_beam4',\n    'beam_search_scierc_full_551',\n    'd066_sweep_llama_scierc_beam4_s1_551',\n    'd066_sweep_llama_docred_beam4_s1',\n    'r14_qwen_docred_beam4_998', 'r14_llama_docred_beam4_998',\n]\n\nfor t in targets:\n    if t in exps:\n        e = exps[t]\n        print(f'=== {t} === (status={e.get(\\\"status\\\")}, conclusion={e.get(\\\"conclusion\\\",\\\"N/A\\\")})')\n        if 'metrics' in e:\n            print(json.dumps(e['metrics'], indent=2))\n        else:\n            print('  NO METRICS')\n        print()\n    else:\n        print(f'=== {t} === NOT IN REGISTRY')\n        print()\n\"",
  "description": "Fetch detailed metrics for all relevant experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "9d9d7eaa-1013-4f70-8c54-1239a7896310",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QEtED8zvzkgMaiGz2kXjpJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2451,
      "cache_read_input_tokens": 28341,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2451
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

_source line 40 · 2026-05-22T04:10:02.369Z_

<details><summary>↩ Tool result · `toolu_01Vn6ZEpq9akQtDrjAArYnSX`</summary>

```text
=== r16_70b_scierc_zs_s1 === (status=DONE, conclusion=success)
{
  "E_F1": 35.19,
  "R_F1": 11.24,
  "DR_pct": 0,
  "RV_pct": 0,
  "ET_pct": 0,
  "CF_pct": 3.5,
  "parse_fail_pct": 0,
  "samples": 551,
  "baseline_unc_E_F1": 35.21,
  "baseline_unc_R_F1": 11.15,
  "baseline_unc_DR_pct": 6.41,
  "baseline_unc_RV_pct": 0.61,
  "baseline_unc_CF_pct": 0
}

=== r16_70b_lora_scierc === (status=DONE, conclusion=success)
{
  "eval_loss": 0.0611,
  "token_acc": 97.78,
  "steps_completed": 663,
  "epochs": 3,
  "train_loss_start": 0.183,
  "train_loss_end": 0.041
}

=== r16_70b_lora_docred === (status=DONE, conclusion=success)
{
  "eval_loss": 0.0635,
  "token_acc": 97.94,
  "steps_completed": 1146,
  "epochs": 3,
  "train_loss_start": 0.147,
  "train_loss_end": 0.056
}

=== r16_trie_qwen_ft_scierc === (status=DONE, conclusion=success)
{
  "E_F1": 66.73,
  "R_F1": 42.57,
  "ET_pct": 0,
  "RV_pct": 0,
  "DR_pct": 95.5,
  "CF_pct": 0.09,
  "parse_fail_pct": 9.1,
  "samples": 551
}

=== r16_trie_qwen_zs_scierc === (status=DONE, conclusion=success)
{
  "E_F1": 30.97,
  "R_F1": 8.64,
  "ET_pct": 0,
  "RV_pct": 0,
  "DR_pct": 29.3,
  "CF_pct": 0,
  "parse_fail_pct": 0,
  "samples": 551
}

=== r16_trie_llama_ft_scierc === (status=DONE, conclusion=success)
{
  "E_F1": 65.37,
  "R_F1": 41.42,
  "ET_pct": 0,
  "RV_pct": 0,
  "DR_pct": 15.2,
  "CF_pct": 0,
  "parse_fail_pct": 50.8,
  "samples": 551
}

=== r16_trie_llama_zs_scierc === (status=DONE, conclusion=success)
{
  "E_F1": 23.23,
  "R_F1": 2.9,
  "ET_pct": 0,
  "RV_pct": 0,
  "DR_pct": 84.4,
  "CF_pct": 0.36,
  "parse_fail_pct": 0,
  "samples": 551
}

=== p8_latency_overhead === (status=DONE, conclusion=success)
{
  "samples": 551,
  "unconstrained_mean_s": 4.163,
  "unconstrained_median_s": 4.106,
  "unconstrained_total_s": 2293.7,
  "constrained_mean_s": 4.71,
  "constrained_median_s": 4.644,
  "constrained_total_s": 2595,
  "overhead_ratio_mean": 1.131,
  "overhead_ratio_median": 1.131,
  "overhead_ratio_p95_perdoc": 1.262,
  "overhead_pct": 13.1
}

=== p8b_docred_latency === (status=DONE, conclusion=failed)
  NO METRICS

=== p8c_ft_scierc_latency === (status=DONE, conclusion=success)
{
  "unconstrained_mean_s": 2.612,
  "constrained_mean_s": 2.873,
  "unconstrained_median_s": 2.355,
  "constrained_median_s": 2.624,
  "overhead_mean_pct": 10,
  "overhead_median_pct": 11.42,
  "per_doc_ratio_mean": 1.205,
  "per_doc_ratio_median": 1.117,
  "num_docs": 551,
  "unconstrained_total_s": 1439,
  "constrained_total_s": 1582.9
}

=== d062_beam_latency === (status=DONE, conclusion=success)
{
  "beam4_unconstrained_s_per_doc": 3.446,
  "beam4_constrained_s_per_doc": 4.013,
  "beam4_unconstrained_total_s": 1898.7,
  "beam4_constrained_total_s": 2211,
  "beam_greedy_ratio_unconstrained": 1.319,
  "beam_greedy_ratio_constrained": 1.397,
  "constraint_overhead_beam": 1.165,
  "constraint_overhead_greedy": 1.1,
  "greedy_unconstrained_s_per_doc": 2.612,
  "greedy_constrained_s_per_doc": 2.873
}

=== q1_llama_lora_scierc_beam4 === (status=DONE, conclusion=success)
{
  "ET_violation_rate": 0,
  "RV_violation_rate": 0,
  "DR_violation_rate": 0,
  "CF_violation_rate": 0,
  "entity_f1": 67.94,
  "relation_f1": 46.11,
  "samples": 551,
  "total_entities": 1853,
  "total_relations": 727
}

=== beam_search_scierc_full_551 === (status=DONE, conclusion=success)
{
  "ET_pct": 0,
  "RV_pct": 0,
  "DR_pct": 0,
  "CF_pct": 0.53,
  "E_F1": 32,
  "R_F1": 8.56,
  "E_P": 26.83,
  "E_R": 39.63,
  "R_P": 6.69,
  "R_R": 11.91,
  "parse_fail_rate": 0,
  "total_entities": 2476,
  "total_relations": 1737
}

=== d066_sweep_llama_scierc_beam4_s1_551 === (status=DONE, conclusion=success)
{
  "E-F1": 68.06,
  "E-P": 65.96,
  "E-R": 70.29,
  "R-F1": 46.18,
  "R-P": 42.1,
  "R-R": 51.13,
  "ET_pct": 0,
  "RV_pct": 0,
  "DR_pct": 0,
  "CF_pct": 0,
  "parse_fail": 0,
  "samples": 551,
  "note": "ET/RV corrected from 100\u21920: original eval used hardcoded DocRED ontology, re-evaled with --dataset scierc"
}

=== d066_sweep_llama_docred_beam4_s1 === (status=DONE, conclusion=success)
{
  "E-F1": 85.61,
  "E-P": 85.48,
  "E-R": 85.73,
  "R-F1": 51.89,
  "R-P": 51.59,
  "R-R": 52.2,
  "DR_pct": 0,
  "CF_pct": 0,
  "PF_pct": 0.5,
  "ET_pct": 0,
  "RV_pct": 0,
  "samples": 200,
  "parse_fail": 1
}

=== r14_qwen_docred_beam4_998 === (status=DONE, conclusion=success)
{
  "E_F1": 58.19,
  "R_F1": 8.72,
  "DR_pct": 0,
  "RV_pct": 0,
  "ET_pct": 0,
  "CF_pct": 4.94,
  "parse_fail_pct": 3.51,
  "samples": 998,
  "success": 963,
  "fail": 35
}

=== r14_llama_docred_beam4_998 === (status=DONE, conclusion=success)
{
  "R_F1": 8.83,
  "E_F1": 57.81,
  "DR_pct": 0,
  "CF_pct": 1,
  "ET_pct": 0,
  "RV_pct": 0,
  "parse_fail_pct": 3.91,
  "samples": 998,
  "success": 959,
  "fail": 39,
  "baseline_ZS_greedy_R_F1": 6.27,
  "baseline_ZS_greedy_E_F1": 54.93,
  "baseline_ZS_greedy_DR_pct": 2.55,
  "baseline_ZS_greedy_CF_pct": 8.54
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "1511725e-6984-4549-aec1-8a56a915345e",
  "tool_use_result": {
    "stdout": "=== r16_70b_scierc_zs_s1 === (status=DONE, conclusion=success)\n{\n  \"E_F1\": 35.19,\n  \"R_F1\": 11.24,\n  \"DR_pct\": 0,\n  \"RV_pct\": 0,\n  \"ET_pct\": 0,\n  \"CF_pct\": 3.5,\n  \"parse_fail_pct\": 0,\n  \"samples\": 551,\n  \"baseline_unc_E_F1\": 35.21,\n  \"baseline_unc_R_F1\": 11.15,\n  \"baseline_unc_DR_pct\": 6.41,\n  \"baseline_unc_RV_pct\": 0.61,\n  \"baseline_unc_CF_pct\": 0\n}\n\n=== r16_70b_lora_scierc === (status=DONE, conclusion=success)\n{\n  \"eval_loss\": 0.0611,\n  \"token_acc\": 97.78,\n  \"steps_completed\": 663,\n  \"epochs\": 3,\n  \"train_loss_start\": 0.183,\n  \"train_loss_end\": 0.041\n}\n\n=== r16_70b_lora_docred === (status=DONE, conclusion=success)\n{\n  \"eval_loss\": 0.0635,\n  \"token_acc\": 97.94,\n  \"steps_completed\": 1146,\n  \"epochs\": 3,\n  \"train_loss_start\": 0.147,\n  \"train_loss_end\": 0.056\n}\n\n=== r16_trie_qwen_ft_scierc === (status=DONE, conclusion=success)\n{\n  \"E_F1\": 66.73,\n  \"R_F1\": 42.57,\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 95.5,\n  \"CF_pct\": 0.09,\n  \"parse_fail_pct\": 9.1,\n  \"samples\": 551\n}\n\n=== r16_trie_qwen_zs_scierc === (status=DONE, conclusion=success)\n{\n  \"E_F1\": 30.97,\n  \"R_F1\": 8.64,\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 29.3,\n  \"CF_pct\": 0,\n  \"parse_fail_pct\": 0,\n  \"samples\": 551\n}\n\n=== r16_trie_llama_ft_scierc === (status=DONE, conclusion=success)\n{\n  \"E_F1\": 65.37,\n  \"R_F1\": 41.42,\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 15.2,\n  \"CF_pct\": 0,\n  \"parse_fail_pct\": 50.8,\n  \"samples\": 551\n}\n\n=== r16_trie_llama_zs_scierc === (status=DONE, conclusion=success)\n{\n  \"E_F1\": 23.23,\n  \"R_F1\": 2.9,\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 84.4,\n  \"CF_pct\": 0.36,\n  \"parse_fail_pct\": 0,\n  \"samples\": 551\n}\n\n=== p8_latency_overhead === (status=DONE, conclusion=success)\n{\n  \"samples\": 551,\n  \"unconstrained_mean_s\": 4.163,\n  \"unconstrained_median_s\": 4.106,\n  \"unconstrained_total_s\": 2293.7,\n  \"constrained_mean_s\": 4.71,\n  \"constrained_median_s\": 4.644,\n  \"constrained_total_s\": 2595,\n  \"overhead_ratio_mean\": 1.131,\n  \"overhead_ratio_median\": 1.131,\n  \"overhead_ratio_p95_perdoc\": 1.262,\n  \"overhead_pct\": 13.1\n}\n\n=== p8b_docred_latency === (status=DONE, conclusion=failed)\n  NO METRICS\n\n=== p8c_ft_scierc_latency === (status=DONE, conclusion=success)\n{\n  \"unconstrained_mean_s\": 2.612,\n  \"constrained_mean_s\": 2.873,\n  \"unconstrained_median_s\": 2.355,\n  \"constrained_median_s\": 2.624,\n  \"overhead_mean_pct\": 10,\n  \"overhead_median_pct\": 11.42,\n  \"per_doc_ratio_mean\": 1.205,\n  \"per_doc_ratio_median\": 1.117,\n  \"num_docs\": 551,\n  \"unconstrained_total_s\": 1439,\n  \"constrained_total_s\": 1582.9\n}\n\n=== d062_beam_latency === (status=DONE, conclusion=success)\n{\n  \"beam4_unconstrained_s_per_doc\": 3.446,\n  \"beam4_constrained_s_per_doc\": 4.013,\n  \"beam4_unconstrained_total_s\": 1898.7,\n  \"beam4_constrained_total_s\": 2211,\n  \"beam_greedy_ratio_unconstrained\": 1.319,\n  \"beam_greedy_ratio_constrained\": 1.397,\n  \"constraint_overhead_beam\": 1.165,\n  \"constraint_overhead_greedy\": 1.1,\n  \"greedy_unconstrained_s_per_doc\": 2.612,\n  \"greedy_constrained_s_per_doc\": 2.873\n}\n\n=== q1_llama_lora_scierc_beam4 === (status=DONE, conclusion=success)\n{\n  \"ET_violation_rate\": 0,\n  \"RV_violation_rate\": 0,\n  \"DR_violation_rate\": 0,\n  \"CF_violation_rate\": 0,\n  \"entity_f1\": 67.94,\n  \"relation_f1\": 46.11,\n  \"samples\": 551,\n  \"total_entities\": 1853,\n  \"total_relations\": 727\n}\n\n=== beam_search_scierc_full_551 === (status=DONE, conclusion=success)\n{\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 0,\n  \"CF_pct\": 0.53,\n  \"E_F1\": 32,\n  \"R_F1\": 8.56,\n  \"E_P\": 26.83,\n  \"E_R\": 39.63,\n  \"R_P\": 6.69,\n  \"R_R\": 11.91,\n  \"parse_fail_rate\": 0,\n  \"total_entities\": 2476,\n  \"total_relations\": 1737\n}\n\n=== d066_sweep_llama_scierc_beam4_s1_551 === (status=DONE, conclusion=success)\n{\n  \"E-F1\": 68.06,\n  \"E-P\": 65.96,\n  \"E-R\": 70.29,\n  \"R-F1\": 46.18,\n  \"R-P\": 42.1,\n  \"R-R\": 51.13,\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 0,\n  \"CF_pct\": 0,\n  \"parse_fail\": 0,\n  \"samples\": 551,\n  \"note\": \"ET/RV corrected from 100\\u21920: original eval used hardcoded DocRED ontology, re-evaled with --dataset scierc\"\n}\n\n=== d066_sweep_llama_docred_beam4_s1 === (status=DONE, conclusion=success)\n{\n  \"E-F1\": 85.61,\n  \"E-P\": 85.48,\n  \"E-R\": 85.73,\n  \"R-F1\": 51.89,\n  \"R-P\": 51.59,\n  \"R-R\": 52.2,\n  \"DR_pct\": 0,\n  \"CF_pct\": 0,\n  \"PF_pct\": 0.5,\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"samples\": 200,\n  \"parse_fail\": 1\n}\n\n=== r14_qwen_docred_beam4_998 === (status=DONE, conclusion=success)\n{\n  \"E_F1\": 58.19,\n  \"R_F1\": 8.72,\n  \"DR_pct\": 0,\n  \"RV_pct\": 0,\n  \"ET_pct\": 0,\n  \"CF_pct\": 4.94,\n  \"parse_fail_pct\": 3.51,\n  \"samples\": 998,\n  \"success\": 963,\n  \"fail\": 35\n}\n\n=== r14_llama_docred_beam4_998 === (status=DONE, conclusion=success)\n{\n  \"R_F1\": 8.83,\n  \"E_F1\": 57.81,\n  \"DR_pct\": 0,\n  \"CF_pct\": 1,\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"parse_fail_pct\": 3.91,\n  \"samples\": 998,\n  \"success\": 959,\n  \"fail\": 39,\n  \"baseline_ZS_greedy_R_F1\": 6.27,\n  \"baseline_ZS_greedy_E_F1\": 54.93,\n  \"baseline_ZS_greedy_DR_pct\": 2.55,\n  \"baseline_ZS_greedy_CF_pct\": 8.54\n}",
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

_source line 41_

<details><summary>Logged reasoning block</summary>

```text
Now let me also get the DocRED latency data and find the runtime overhead numbers for DocRED. The `p8b_docred_latency` has no metrics but status=failed. Let me search for other DocRED latency experiments.

Also, I need to trace additional claims in the paper. Let me also look at specific numbers:

1. **Line 5**: "+13.1% on SciERC" → p8_latency_overhead.overhead_pct = 13.1 ✓
2. **Line 5**: "+2.43% on DocRED" → Need to find this. 

The DocRED latency experiment failed without producing metrics, so I'm moving on to verify the remaining claims. I need to check the LoRA overhead percentage against the 37% latency improvement claim, locate the scalability benchmarks showing constant 2-3% overhead across entity and relation type ranges, and find the R-F1 scores mentioned around line 11. Continuing to verify the remaining claims against the experimental data, particularly the 8B composability pattern and the trie-only DR results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "a7d9f20b-6bc7-4326-b48b-2f71db108245",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JBgHaKVjCFKj61PJMZRTPx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3625,
      "cache_read_input_tokens": 30792,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3625
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

_source line 42_

Now let me find the DocRED latency data and the 8B composability reference, plus verify the trie DR range claim.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "b698abb0-83f3-4e86-a116-9c59269639a2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JBgHaKVjCFKj61PJMZRTPx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3625,
      "cache_read_input_tokens": 30792,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3625
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

_source line 43_

<details open><summary>🔧 Tool call — Bash · `toolu_011MTieVPx9UDrUiAHEfiCfA`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/06688fc2-d26c-40b0-8ebe-68d505b40c0d/tool-results/mcp-agent-ml-research-read_registry-1779422951081.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n\n# 1. Find DocRED latency experiments\nprint('=== DocRED latency experiments ===')\nfor k in exps:\n    if 'docred' in k.lower() and ('latency' in k.lower() or 'overhead' in k.lower()):\n        e = exps[k]\n        print(f'{k}: status={e[\\\"status\\\"]}, metrics={json.dumps(e.get(\\\"metrics\\\",\\\"NONE\\\"), indent=2)}')\n        print()\n\n# 2. Find composability / 8B DR experiments (looking for 9.90 -> 1.18 pattern)\nprint('=== Searching for 8B composability (9.90 -> 1.18) ===')\nfor k in exps:\n    m = exps[k].get('metrics', {})\n    if isinstance(m, dict):\n        dr = m.get('DR_pct') or m.get('DR_violation_rate')\n        if dr is not None and (abs(float(dr) - 9.90) < 0.01 or abs(float(dr) - 1.18) < 0.01):\n            print(f'{k}: DR={dr}, metrics={json.dumps(m, indent=2)[:300]}')\n            print()\n\n# 3. Scalability experiments\nprint('=== Scalability experiments ===')\nfor k in exps:\n    if 'scal' in k.lower() or 'compile' in k.lower():\n        e = exps[k]\n        print(f'{k}: status={e[\\\"status\\\"]}, metrics={json.dumps(e.get(\\\"metrics\\\",\\\"NONE\\\"))}')\n        print()\n\n# 4. R-F1 44-47 range for beam S1 on SciERC LoRA\nprint('=== Beam S1 LoRA SciERC R-F1 ===')\nfor k in exps:\n    if 'beam' in k.lower() and 'scierc' in k.lower():\n        m = exps[k].get('metrics', {})\n        if isinstance(m, dict):\n            rf1 = m.get('R_F1') or m.get('R-F1') or m.get('relation_f1')\n            if rf1 is not None and 40 <= float(rf1) <= 50:\n                print(f'{k}: R-F1={rf1}')\n\" 2>&1 | head -80",
  "description": "Find DocRED latency, 8B composability, scalability, and beam R-F1 data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "a6fa144e-c9af-48d5-8b78-d7154aa5c6d5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JBgHaKVjCFKj61PJMZRTPx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3625,
      "cache_read_input_tokens": 30792,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3625
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

_source line 44 · 2026-05-22T04:10:35.469Z_

<details><summary>↩ Tool result · `toolu_011MTieVPx9UDrUiAHEfiCfA`</summary>

```text
=== DocRED latency experiments ===
p8b_docred_latency: status=DONE, metrics="NONE"

=== Searching for 8B composability (9.90 -> 1.18) ===
=== Scalability experiments ===
d062_ontology_scalability: status=DONE, metrics={"compile_small_total_s": 0.334, "compile_medium_total_s": 0.322, "compile_large_total_s": 0.345, "compile_xlarge_total_s": 0.42, "grammar_small_s": 0.333, "grammar_xlarge_s": 0.365, "semantic_small_s": 0.0004, "semantic_xlarge_s": 0.017, "overhead_small": 1.02, "overhead_medium": 1.03, "overhead_large": 1.03, "overhead_xlarge": 1.03, "failures": 0}

=== Beam S1 LoRA SciERC R-F1 ===
d066_sweep_llama_scierc_beam8_s1_551: R-F1=44.95
d066_sweep_llama_scierc_beam4_s1_551: R-F1=46.18
d066_sweep_llama_scierc_beam2_s1_551: R-F1=46.12
q1_llama_lora_scierc_beam4: R-F1=46.11
w10_qwen_scierc_ft_beam_4: R-F1=44.23
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "6577ffb3-3ed4-4159-a5cc-b851470c3cf7",
  "tool_use_result": {
    "stdout": "=== DocRED latency experiments ===\np8b_docred_latency: status=DONE, metrics=\"NONE\"\n\n=== Searching for 8B composability (9.90 -> 1.18) ===\n=== Scalability experiments ===\nd062_ontology_scalability: status=DONE, metrics={\"compile_small_total_s\": 0.334, \"compile_medium_total_s\": 0.322, \"compile_large_total_s\": 0.345, \"compile_xlarge_total_s\": 0.42, \"grammar_small_s\": 0.333, \"grammar_xlarge_s\": 0.365, \"semantic_small_s\": 0.0004, \"semantic_xlarge_s\": 0.017, \"overhead_small\": 1.02, \"overhead_medium\": 1.03, \"overhead_large\": 1.03, \"overhead_xlarge\": 1.03, \"failures\": 0}\n\n=== Beam S1 LoRA SciERC R-F1 ===\nd066_sweep_llama_scierc_beam8_s1_551: R-F1=44.95\nd066_sweep_llama_scierc_beam4_s1_551: R-F1=46.18\nd066_sweep_llama_scierc_beam2_s1_551: R-F1=46.12\nq1_llama_lora_scierc_beam4: R-F1=46.11\nw10_qwen_scierc_ft_beam_4: R-F1=44.23",
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

_source line 45_

<details><summary>Logged reasoning block</summary>

```text
Let me also look for:
1. DocRED latency overhead (2.43%) - need to find where this comes from
2. The 37% lower absolute latency under LoRA
3. The 8B composability pattern (9.90% → 1.18%)
4. The "24% DR reduction" for grammar-only ablation
5. The "1-15% unconstrained" DR range for context of trie comparison
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "514736b6-aeaa-43ef-8f9a-90f4bf4d432e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015nt4BvEbmHEZsC3AST6Fu8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2000,
      "cache_read_input_tokens": 34417,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2000
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

_source line 46_

<details open><summary>🔧 Tool call — Bash · `toolu_012eUyU474aMZbzUXC2hd2nQ`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/06688fc2-d26c-40b0-8ebe-68d505b40c0d/tool-results/mcp-agent-ml-research-read_registry-1779422951081.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n\n# 1. DocRED latency - check p8b_docred_latency full entry & spec\nprint('=== p8b_docred_latency FULL ===')\nprint(json.dumps(exps.get('p8b_docred_latency', {}), indent=2))\nprint()\n\n# 2. Look for DocRED overhead 2.43% anywhere\nprint('=== Search for 2.43 in any metrics ===')\nfor k in exps:\n    m = exps[k].get('metrics', {})\n    if isinstance(m, dict):\n        for mk, mv in m.items():\n            if isinstance(mv, (int, float)) and abs(float(mv) - 2.43) < 0.01:\n                print(f'{k}.{mk} = {mv}')\n\n# Also search conclusion/hypothesis for 2.43\nfor k in exps:\n    for field in ['conclusion', 'hypothesis']:\n        val = exps[k].get(field, '')\n        if isinstance(val, str) and '2.43' in val:\n            print(f'{k}.{field} mentions 2.43')\n\nprint()\n\n# 3. Search for 37% or 0.37 related to lower latency\nprint('=== Search for 37% lower latency ===')\n# Compare p8_latency_overhead (ZS SciERC) and p8c_ft_scierc_latency (LoRA SciERC)\np8 = exps['p8_latency_overhead']['metrics']\np8c = exps['p8c_ft_scierc_latency']['metrics']\nprint(f'ZS constrained mean: {p8[\\\"constrained_mean_s\\\"]}s')\nprint(f'LoRA constrained mean: {p8c[\\\"constrained_mean_s\\\"]}s')\nratio = (p8[\\\"constrained_mean_s\\\"] - p8c[\\\"constrained_mean_s\\\"]) / p8[\\\"constrained_mean_s\\\"] * 100\nprint(f'LoRA is {ratio:.1f}% lower absolute latency than ZS constrained')\nprint()\n\n# 4. Search for composability 9.90 and 1.18\nprint('=== Search for CF 9.90 or 1.18 ===')\nfor k in exps:\n    m = exps[k].get('metrics', {})\n    if isinstance(m, dict):\n        cf = m.get('CF_pct') or m.get('CF_violation_rate')\n        if cf is not None and (abs(float(cf) - 9.90) < 0.05 or abs(float(cf) - 1.18) < 0.05):\n            print(f'{k}: CF={cf}')\n            dr = m.get('DR_pct') or m.get('DR_violation_rate')\n            print(f'  DR={dr}, R_F1={m.get(\\\"R_F1\\\") or m.get(\\\"R-F1\\\") or m.get(\\\"relation_f1\\\")}')\n            print()\n\n# 5. Grammar-only ablation 24% DR reduction\nprint('=== Search for ablation / grammar-only ===')\nfor k in exps:\n    if 'ablat' in k.lower() or 'grammar' in k.lower():\n        print(f'{k}: {json.dumps(exps[k].get(\\\"metrics\\\", {}), indent=2)[:400]}')\n        print()\n\" 2>&1",
  "description": "Find DocRED latency, 37% latency, composability CF, and grammar ablation data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "18ddefd7-903a-4601-bef2-d2aed4fadead",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015nt4BvEbmHEZsC3AST6Fu8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2000,
      "cache_read_input_tokens": 34417,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2000
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

_source line 47 · 2026-05-22T04:10:57.055Z_

<details><summary>↩ Tool result · `toolu_012eUyU474aMZbzUXC2hd2nQ`</summary>

```text
=== p8b_docred_latency FULL ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-18T15:14:28.888Z",
  "updated_at": "2026-05-18T17:48:57.349Z",
  "hypothesis": "OntoCoDec constrained decoding overhead on Qwen3-8B DocRED (200-doc subset) measured on same GPU as P8 SciERC will confirm moderate overhead (<2x), providing consistent timing data for paper",
  "parent": "p8_latency_overhead",
  "spec": {
    "command": "run_constrained_extraction.py unconstrained+full_s1 then analyze_latency.py",
    "server": "westd-21461",
    "data_path": "/root/autodl-tmp/schema_outputs/docred_timing_subset_200.json",
    "data_count": 200,
    "model_name": "Qwen3-8B",
    "seed": 42,
    "checkpoint_source": "Qwen/Qwen3-8B (base, no fine-tuning)",
    "eval_data": "DocRED dev subset 200 docs"
  },
  "failure_reason": "startup recovery: RUNNING with no cron and no server/pid info",
  "conclusion": "failed",
  "completed_at": "2026-05-18T17:48:57.349Z"
}

=== Search for 2.43 in any metrics ===

=== Search for 37% lower latency ===
ZS constrained mean: 4.71s
LoRA constrained mean: 2.873s
LoRA is 39.0% lower absolute latency than ZS constrained

=== Search for CF 9.90 or 1.18 ===
w9_qwen_scierc_zs_sampling: CF=9.9
  DR=0.75, R_F1=7.42

w10_type_consensus_prototype: CF=9.9
  DR=0.93, R_F1=8.36

=== Search for ablation / grammar-only ===
ee_mistral_wikievents_grammar_only_v3: {
  "parse_success": "218/246 (88.6%)",
  "parse_failures": 28,
  "ET": 0,
  "EV": 0,
  "RoV": 64,
  "AC": 13.8,
  "CF": 1.1,
  "go_no_go": 77.73,
  "entity_f1": 0.1192,
  "trigger_f1": 0.0337,
  "argument_f1": 0.0027,
  "code_version": "938-line (collision+exact-match fix)",
  "mode": "grammar_only"
}

w10_beam_ablation_k8: {
  "ET_pct": 0,
  "RV_pct": 0,
  "DR_pct": 0,
  "CF_pct": 0.08,
  "CF_count": 2,
  "E_F1": 32.18,
  "R_F1": 8.39,
  "E_P": 26.95,
  "E_R": 39.93,
  "R_P": 6.54,
  "R_R": 11.7,
  "parse_failures": 0,
  "total_samples": 551,
  "total_triples": 1744,
  "total_entities": 2483,
  "vs_greedy": {
    "DR_delta": -0.93,
    "CF_delta": -9.82,
    "E_F1_delta": 1.2,
    "R_F1_delta": 0.03
  },
  "vs_beam_

w10_beam_ablation_k2: {
  "ET_pct": 0,
  "RV_pct": 0,
  "DR_pct": 0.35,
  "CF_count": 71,
  "CF_pct": 4.12,
  "E_F1": 31.54,
  "R_F1": 8.75,
  "parse_failures": 0,
  "total_samples": 551,
  "total_triples": 1724,
  "vs_greedy": {
    "DR_delta": -0.58,
    "CF_delta": -5.78,
    "E_F1_delta": 0.56,
    "R_F1_delta": 0.39,
    "note": "Greedy: DR=0.93%, CF=9.90%, E_F1=30.98, R_F1=8.36"
  },
  "vs_beam_k4": {
    "DR_del

w8_llama_docred_ft_grammar_only: {
  "E_F1": 84.04,
  "R_F1": 43.77,
  "entity_precision": 84.99,
  "entity_recall": 83.11,
  "relation_precision": 38.6,
  "relation_recall": 50.53,
  "ET_pct": 0,
  "RV_pct": 0,
  "DR_pct": 0.51,
  "CF_pct": 0.12,
  "parse_fail_rate": 2.3,
  "total_samples": 998,
  "total_relations": 16199,
  "unique_entities": 13225,
  "parse_failures": 23
}

w7_llama_scierc_ft_grammar_only: {
  "total_samples": 551,
  "json_parse_failures": 0,
  "total_entities": 1757,
  "total_relations": 1082,
  "entity_type_violation_rate": 0,
  "relation_vocabulary_violation_rate": 0,
  "domain_range_violation_rate": 0.0111,
  "cross_field_consistency_violation_rate": 0,
  "entity_f1": {
    "precision": 0.6647,
    "recall": 0.691,
    "f1": 0.6776
  },
  "relation_f1": {
    "precision": 0.432,

w7_qwen_scierc_ft_grammar_only: {
  "ET_pct": 0,
  "RV_pct": 0,
  "DR_pct": 1.9,
  "CF_pct": 0,
  "parse_fail_rate": 0,
  "total_samples": 551,
  "total_entities": 1784,
  "total_relations": 1128,
  "E_P": 0.6523,
  "E_R": 0.6898,
  "E_F1": 0.6705,
  "R_P": 0.4087,
  "R_R": 0.4733,
  "R_F1": 0.4386,
  "DR_violations": 22,
  "tokenizer_warning": "false_positive_transformers_4.57.6"
}

w8_qwen_docred_ft_grammar_only: {
  "E_F1": 82.19,
  "E_P": 85.47,
  "E_R": 79.16,
  "R_F1": 40.85,
  "R_P": 36.27,
  "R_R": 46.77,
  "ET_pct": 0,
  "RV_pct": 0,
  "DR_pct": 0.61,
  "CF_pct": 0.11,
  "parse_fail_rate": 7.01,
  "total_samples": 998,
  "parse_failures": 70
}

phase2_docred_grammar_only: {
  "documents_checked": 985,
  "parse_failures": 13,
  "total_entities": 20150,
  "total_triples": 17341,
  "entity_type_violation_rate": 0,
  "relation_vocabulary_violation_rate": 0.0003,
  "domain_range_violation_rate": 0.2617,
  "cross_field_consistency_violation_rate": 0.0007,
  "relation_f1": 8.31,
  "relation_precision": 7.06,
  "relation_recall": 10.12,
  "entity_f1": 59.38,
  "entity_prec

phase2_scierc_grammar_only: {
  "total_samples": 551,
  "total_triples": 1725,
  "total_entities": 2474,
  "json_parse_rate": 1,
  "entity_type_violation_rate": 0,
  "relation_vocabulary_violation_rate": 0,
  "domain_range_violation_rate": 0.1484,
  "cross_field_consistency_violation_rate": 0.0008,
  "entity_f1": 0.3098,
  "entity_precision": 0.2598,
  "entity_recall": 0.3837,
  "relation_f1": 0.0823,
  "relation_precision":
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "4ed1ce08-fa9b-4098-8871-badbe3800083",
  "tool_use_result": {
    "stdout": "=== p8b_docred_latency FULL ===\n{\n  \"status\": \"DONE\",\n  \"retry_count\": 0,\n  \"created_at\": \"2026-05-18T15:14:28.888Z\",\n  \"updated_at\": \"2026-05-18T17:48:57.349Z\",\n  \"hypothesis\": \"OntoCoDec constrained decoding overhead on Qwen3-8B DocRED (200-doc subset) measured on same GPU as P8 SciERC will confirm moderate overhead (<2x), providing consistent timing data for paper\",\n  \"parent\": \"p8_latency_overhead\",\n  \"spec\": {\n    \"command\": \"run_constrained_extraction.py unconstrained+full_s1 then analyze_latency.py\",\n    \"server\": \"westd-21461\",\n    \"data_path\": \"/root/autodl-tmp/schema_outputs/docred_timing_subset_200.json\",\n    \"data_count\": 200,\n    \"model_name\": \"Qwen3-8B\",\n    \"seed\": 42,\n    \"checkpoint_source\": \"Qwen/Qwen3-8B (base, no fine-tuning)\",\n    \"eval_data\": \"DocRED dev subset 200 docs\"\n  },\n  \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\",\n  \"conclusion\": \"failed\",\n  \"completed_at\": \"2026-05-18T17:48:57.349Z\"\n}\n\n=== Search for 2.43 in any metrics ===\n\n=== Search for 37% lower latency ===\nZS constrained mean: 4.71s\nLoRA constrained mean: 2.873s\nLoRA is 39.0% lower absolute latency than ZS constrained\n\n=== Search for CF 9.90 or 1.18 ===\nw9_qwen_scierc_zs_sampling: CF=9.9\n  DR=0.75, R_F1=7.42\n\nw10_type_consensus_prototype: CF=9.9\n  DR=0.93, R_F1=8.36\n\n=== Search for ablation / grammar-only ===\nee_mistral_wikievents_grammar_only_v3: {\n  \"parse_success\": \"218/246 (88.6%)\",\n  \"parse_failures\": 28,\n  \"ET\": 0,\n  \"EV\": 0,\n  \"RoV\": 64,\n  \"AC\": 13.8,\n  \"CF\": 1.1,\n  \"go_no_go\": 77.73,\n  \"entity_f1\": 0.1192,\n  \"trigger_f1\": 0.0337,\n  \"argument_f1\": 0.0027,\n  \"code_version\": \"938-line (collision+exact-match fix)\",\n  \"mode\": \"grammar_only\"\n}\n\nw10_beam_ablation_k8: {\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 0,\n  \"CF_pct\": 0.08,\n  \"CF_count\": 2,\n  \"E_F1\": 32.18,\n  \"R_F1\": 8.39,\n  \"E_P\": 26.95,\n  \"E_R\": 39.93,\n  \"R_P\": 6.54,\n  \"R_R\": 11.7,\n  \"parse_failures\": 0,\n  \"total_samples\": 551,\n  \"total_triples\": 1744,\n  \"total_entities\": 2483,\n  \"vs_greedy\": {\n    \"DR_delta\": -0.93,\n    \"CF_delta\": -9.82,\n    \"E_F1_delta\": 1.2,\n    \"R_F1_delta\": 0.03\n  },\n  \"vs_beam_\n\nw10_beam_ablation_k2: {\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 0.35,\n  \"CF_count\": 71,\n  \"CF_pct\": 4.12,\n  \"E_F1\": 31.54,\n  \"R_F1\": 8.75,\n  \"parse_failures\": 0,\n  \"total_samples\": 551,\n  \"total_triples\": 1724,\n  \"vs_greedy\": {\n    \"DR_delta\": -0.58,\n    \"CF_delta\": -5.78,\n    \"E_F1_delta\": 0.56,\n    \"R_F1_delta\": 0.39,\n    \"note\": \"Greedy: DR=0.93%, CF=9.90%, E_F1=30.98, R_F1=8.36\"\n  },\n  \"vs_beam_k4\": {\n    \"DR_del\n\nw8_llama_docred_ft_grammar_only: {\n  \"E_F1\": 84.04,\n  \"R_F1\": 43.77,\n  \"entity_precision\": 84.99,\n  \"entity_recall\": 83.11,\n  \"relation_precision\": 38.6,\n  \"relation_recall\": 50.53,\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 0.51,\n  \"CF_pct\": 0.12,\n  \"parse_fail_rate\": 2.3,\n  \"total_samples\": 998,\n  \"total_relations\": 16199,\n  \"unique_entities\": 13225,\n  \"parse_failures\": 23\n}\n\nw7_llama_scierc_ft_grammar_only: {\n  \"total_samples\": 551,\n  \"json_parse_failures\": 0,\n  \"total_entities\": 1757,\n  \"total_relations\": 1082,\n  \"entity_type_violation_rate\": 0,\n  \"relation_vocabulary_violation_rate\": 0,\n  \"domain_range_violation_rate\": 0.0111,\n  \"cross_field_consistency_violation_rate\": 0,\n  \"entity_f1\": {\n    \"precision\": 0.6647,\n    \"recall\": 0.691,\n    \"f1\": 0.6776\n  },\n  \"relation_f1\": {\n    \"precision\": 0.432,\n\nw7_qwen_scierc_ft_grammar_only: {\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 1.9,\n  \"CF_pct\": 0,\n  \"parse_fail_rate\": 0,\n  \"total_samples\": 551,\n  \"total_entities\": 1784,\n  \"total_relations\": 1128,\n  \"E_P\": 0.6523,\n  \"E_R\": 0.6898,\n  \"E_F1\": 0.6705,\n  \"R_P\": 0.4087,\n  \"R_R\": 0.4733,\n  \"R_F1\": 0.4386,\n  \"DR_violations\": 22,\n  \"tokenizer_warning\": \"false_positive_transformers_4.57.6\"\n}\n\nw8_qwen_docred_ft_grammar_only: {\n  \"E_F1\": 82.19,\n  \"E_P\": 85.47,\n  \"E_R\": 79.16,\n  \"R_F1\": 40.85,\n  \"R_P\": 36.27,\n  \"R_R\": 46.77,\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 0.61,\n  \"CF_pct\": 0.11,\n  \"parse_fail_rate\": 7.01,\n  \"total_samples\": 998,\n  \"parse_failures\": 70\n}\n\nphase2_docred_grammar_only: {\n  \"documents_checked\": 985,\n  \"parse_failures\": 13,\n  \"total_entities\": 20150,\n  \"total_triples\": 17341,\n  \"entity_type_violation_rate\": 0,\n  \"relation_vocabulary_violation_rate\": 0.0003,\n  \"domain_range_violation_rate\": 0.2617,\n  \"cross_field_consistency_violation_rate\": 0.0007,\n  \"relation_f1\": 8.31,\n  \"relation_precision\": 7.06,\n  \"relation_recall\": 10.12,\n  \"entity_f1\": 59.38,\n  \"entity_prec\n\nphase2_scierc_grammar_only: {\n  \"total_samples\": 551,\n  \"total_triples\": 1725,\n  \"total_entities\": 2474,\n  \"json_parse_rate\": 1,\n  \"entity_type_violation_rate\": 0,\n  \"relation_vocabulary_violation_rate\": 0,\n  \"domain_range_violation_rate\": 0.1484,\n  \"cross_field_consistency_violation_rate\": 0.0008,\n  \"entity_f1\": 0.3098,\n  \"entity_precision\": 0.2598,\n  \"entity_recall\": 0.3837,\n  \"relation_f1\": 0.0823,\n  \"relation_precision\":",
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

_source line 48_

<details><summary>Logged reasoning block</summary>

```text
Now I need to find:
1. DocRED latency 2.43% - the p8b experiment failed. Let me search for where this number comes from.
2. The 37% lower absolute latency claim - my calculation shows 39.0%, not 37%. This is a potential mismatch.
3. The 8B pattern 9.90% → 1.18% CF drop - need to find the 1.18% side
4. The "24% DR reduction" for grammar-only - need to compare grammar-only DR vs unconstrained DR on the right dataset


5. I also need to track down the "1-15% unconstrained" and "15-96%" trie-only DR claims - let me dig through the data to verify these ranges.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "39a4bed3-9e49-42bb-a71b-ceac73b2d907",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B2kXsemiEgg1ybkUVjmA6a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3606,
      "cache_read_input_tokens": 36417,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3606
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

_source line 49_

<details open><summary>🔧 Tool call — Bash · `toolu_01KFGppTRSfnY6gndr42ZYZ8`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/06688fc2-d26c-40b0-8ebe-68d505b40c0d/tool-results/mcp-agent-ml-research-read_registry-1779422951081.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n\n# 1. Search for DocRED latency 2.43 in any experiment's hypothesis/conclusion/metrics\nprint('=== DocRED overhead 2.43% source ===')\nfor k in exps:\n    e = exps[k]\n    text = json.dumps(e)\n    if '2.43' in text:\n        print(f'{k}: found 2.43')\n        if 'metrics' in e and e['metrics']:\n            print(f'  metrics: {json.dumps(e[\\\"metrics\\\"])}')\n        print()\n\n# 2. Search for DocRED overhead experiments with actual latency data\nprint('=== DocRED constrained vs unconstrained latency ===')\nfor k in exps:\n    if 'docred' in k.lower():\n        m = exps[k].get('metrics', {})\n        if isinstance(m, dict) and ('overhead' in str(m).lower() or 'latency' in str(m).lower() or 'unconstrained_mean' in str(m)):\n            print(f'{k}: {json.dumps(m, indent=2)[:400]}')\n            print()\n\n# 3. Find CF_pct close to 1.18\nprint('=== CF ~1.18% ===')\nfor k in exps:\n    m = exps[k].get('metrics', {})\n    if isinstance(m, dict):\n        cf = m.get('CF_pct') or m.get('CF_violation_rate') or m.get('cross_field_consistency_violation_rate')\n        if cf is not None:\n            try:\n                cfv = float(cf)\n                if 1.0 <= cfv <= 1.3:\n                    print(f'{k}: CF={cf}')\n            except: pass\n\n# 4. The ablation table reference - grammar-only DR reduction claim\n# Paper says grammar-only achieves 'only 24% DR reduction vs Full S1 94%'\n# Need to find the ablation table experiments for SciERC ft\nprint()\nprint('=== SciERC FT full S1 DR reduction ===')\nfor k in exps:\n    if 'scierc' in k.lower() and ('ft' in k.lower() or 'lora' in k.lower() or 'full' in k.lower()):\n        m = exps[k].get('metrics', {})\n        if isinstance(m, dict):\n            dr = m.get('DR_pct')\n            if dr is not None:\n                print(f'{k}: DR_pct={dr}')\n\" 2>&1",
  "description": "Find DocRED 2.43%, CF 1.18%, and ablation DR data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "5fc0da98-4441-476b-8713-f79154014c6a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B2kXsemiEgg1ybkUVjmA6a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3606,
      "cache_read_input_tokens": 36417,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3606
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

_source line 50 · 2026-05-22T04:11:21.277Z_

<details><summary>↩ Tool result · `toolu_01KFGppTRSfnY6gndr42ZYZ8`</summary>

```text
=== DocRED overhead 2.43% source ===
70b_docred_unconstrained: found 2.43
  metrics: {"entity_f1": 69.03, "entity_precision": 75.03, "entity_recall": 63.92, "relation_f1": 13.03, "relation_precision": 12.43, "relation_recall": 13.69, "ET_violation": 0.02, "RV_violation": 7.8, "DR_violation": 15, "CF_violation": 0.07, "parse_failures": 0, "docs_processed": 998}

=== DocRED constrained vs unconstrained latency ===
=== CF ~1.18% ===
r14_llama_docred_beam4_998: CF=1
w6_mistral_scierc_constrained: CF=1.27

=== SciERC FT full S1 DR reduction ===
r16_trie_llama_ft_scierc: DR_pct=15.2
r16_trie_qwen_ft_scierc: DR_pct=95.5
beam_search_scierc_full_551: DR_pct=0
w7_llama_scierc_ft_semantic_only: DR_pct=0.65
w7_qwen_scierc_ft_semantic_only: DR_pct=0.6
w7_qwen_scierc_ft_grammar_only: DR_pct=1.9
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "aaf1a63e-e5a6-4718-916f-c2bdd0333492",
  "tool_use_result": {
    "stdout": "=== DocRED overhead 2.43% source ===\n70b_docred_unconstrained: found 2.43\n  metrics: {\"entity_f1\": 69.03, \"entity_precision\": 75.03, \"entity_recall\": 63.92, \"relation_f1\": 13.03, \"relation_precision\": 12.43, \"relation_recall\": 13.69, \"ET_violation\": 0.02, \"RV_violation\": 7.8, \"DR_violation\": 15, \"CF_violation\": 0.07, \"parse_failures\": 0, \"docs_processed\": 998}\n\n=== DocRED constrained vs unconstrained latency ===\n=== CF ~1.18% ===\nr14_llama_docred_beam4_998: CF=1\nw6_mistral_scierc_constrained: CF=1.27\n\n=== SciERC FT full S1 DR reduction ===\nr16_trie_llama_ft_scierc: DR_pct=15.2\nr16_trie_qwen_ft_scierc: DR_pct=95.5\nbeam_search_scierc_full_551: DR_pct=0\nw7_llama_scierc_ft_semantic_only: DR_pct=0.65\nw7_qwen_scierc_ft_semantic_only: DR_pct=0.6\nw7_qwen_scierc_ft_grammar_only: DR_pct=1.9",
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

_source line 51_

<details><summary>Logged reasoning block</summary>

```text
The 2.43% appears in the 70b_docred_unconstrained experiment, but that's the relation precision value (12.43), not latency. Let me search more specifically.

Let me search for the DocRED latency 2.43%. Maybe there's a separate file or the computation was done outside the registry. Let me also check what happened with p8b_docred_latency and look for docred timing files.

Also, I found that the CF 1.18% is not in the registry. The closest CF values are 1.0 (r14_llama_docred_beam4_998) and 1.27 (w6_mistral_scierc_constrained).


Now I'm looking at the SciERC grammar-only ablation results to understand the 24% DR reduction claim. I see the grammar-only variants show much lower domain range violation rates compared to the full model, so I need to find what the unconstrained baseline actually was to verify what "24% reduction" means.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "2a210967-d986-45dd-91f4-0ba9c7efd6cc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0127wpG62R1YFP8U9xTwCVrd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1529,
      "cache_read_input_tokens": 40023,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1529
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

_source line 52_

<details open><summary>🔧 Tool call — Bash · `toolu_01BAYAN1NvDShSrKoebTJVWq`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/06688fc2-d26c-40b0-8ebe-68d505b40c0d/tool-results/mcp-agent-ml-research-read_registry-1779422951081.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n\n# 1. Find SciERC FT unconstrained baseline (for DR reduction calculation)\nprint('=== SciERC FT unconstrained baselines ===')\nfor k in exps:\n    if 'scierc' in k.lower() and ('ft' in k.lower() or 'lora' in k.lower()) and 'unc' in k.lower():\n        m = exps[k].get('metrics', {})\n        if isinstance(m, dict):\n            dr = m.get('DR_pct') or m.get('DR_violation_rate') or m.get('domain_range_violation_rate')\n            print(f'{k}: DR={dr}, metrics_keys={list(m.keys())[:10]}')\n\nprint()\n# 2. Find SciERC FT full S1 experiments\nprint('=== SciERC FT full S1 ===')\nfor k in exps:\n    if 'scierc' in k.lower() and ('ft' in k.lower() or 'lora' in k.lower()) and ('full' in k.lower() or 's1' in k.lower()):\n        m = exps[k].get('metrics', {})\n        if isinstance(m, dict):\n            dr = m.get('DR_pct') or m.get('DR_violation_rate')\n            print(f'{k}: DR={dr}')\n\nprint()\n# 3. All experiments with 'unconstrained' and 'scierc' \nprint('=== All SciERC unconstrained experiments ===')\nfor k in exps:\n    if 'scierc' in k.lower() and 'unconstrained' in k.lower():\n        m = exps[k].get('metrics', {})\n        dr = None\n        if isinstance(m, dict):\n            dr = m.get('DR_pct') or m.get('DR_violation_rate') or m.get('domain_range_violation_rate')\n        print(f'{k}: status={exps[k][\\\"status\\\"]}, DR={dr}')\n\nprint()\n# 4. DocRED ZS constrained latency data - search broadly\nprint('=== Any DocRED timing/overhead data ===')\nfor k in exps:\n    if 'docred' in k.lower():\n        m = exps[k].get('metrics', {})\n        if isinstance(m, dict):\n            mstr = json.dumps(m)\n            if any(x in mstr.lower() for x in ['overhead', 'latency', 'timing', 'total_s', '_mean_s']):\n                print(f'{k}: {json.dumps(m, indent=2)[:500]}')\n                print()\n\" 2>&1",
  "description": "Find SciERC unconstrained baselines, full S1, and DocRED timing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "e081fd05-be51-4b81-a750-725fae16342b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0127wpG62R1YFP8U9xTwCVrd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1529,
      "cache_read_input_tokens": 40023,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1529
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

_source line 53 · 2026-05-22T04:11:46.141Z_

<details><summary>↩ Tool result · `toolu_01BAYAN1NvDShSrKoebTJVWq`</summary>

```text
=== SciERC FT unconstrained baselines ===
eval_70b_lora_scierc_unconstrained: DR=None, metrics_keys=[]
w5_llama_lora_scierc_unconstrained_eval: DR=0.0111, metrics_keys=['total_samples', 'total_entities', 'total_relations', 'json_parse_rate', 'entity_type_violation_rate', 'relation_vocabulary_violation_rate', 'domain_range_violation_rate', 'cross_field_consistency_violation_rate', 'total_violation_rate', 'entity_precision']
w5_lora_scierc_unconstrained_eval: DR=0.0195, metrics_keys=['json_parse_rate', 'entity_type_violation_rate', 'relation_vocabulary_violation_rate', 'domain_range_violation_rate', 'cross_field_consistency_violation_rate', 'entity_f1', 'entity_precision', 'entity_recall', 'relation_f1', 'relation_precision']

=== SciERC FT full S1 ===
d062_full_ft_scierc: DR=None

=== All SciERC unconstrained experiments ===
eval_70b_lora_scierc_unconstrained: status=RUNNING, DR=None
70b_scierc_unconstrained: status=DONE, DR=6.5
w5_llama_lora_scierc_unconstrained_eval: status=DONE, DR=0.0111
w6_mistral_scierc_unconstrained: status=DONE, DR=56.94
w5_lora_scierc_unconstrained_eval: status=DONE, DR=0.0195
llama_scierc_unconstrained: status=DONE, DR=0.1334
phase2_scierc_unconstrained: status=DONE, DR=0.1537

=== Any DocRED timing/overhead data ===
w10_llama_docred_beam_50: {
  "ET_pct": 0,
  "RV_pct": 0,
  "DR_pct": 0,
  "CF_pct": 0.94,
  "E_F1": 55.62,
  "R_F1": 9.47,
  "parse_failures": 3,
  "parse_fail_rate": 6,
  "total_samples": 50,
  "vs_greedy_full_s1": {
    "DR_delta": -2.57,
    "CF_delta": -11.19,
    "E_F1_delta": 0.61,
    "R_F1_delta": 3.2,
    "note": "Greedy baseline: DR=2.57%, CF=12.13%, E_F1=55.01, R_F1=6.27"
  },
  "checker_note": "Must use violation_checker_docred.py for DocRED (not violation_checker.py)"
}

w9_qwen_docred_beam_50: {
  "ET_pct": 0,
  "RV_pct": 0,
  "DR_pct": 0,
  "CF_pct": 0.55,
  "E_F1": 58.64,
  "R_F1": 9.37,
  "total_samples": 50,
  "parse_failures": 3,
  "parse_fail_rate": 6,
  "vs_greedy_full_s1": {
    "DR_delta": -10.21,
    "CF_delta": -2.02,
    "E_F1_delta": -0.73,
    "R_F1_delta": 1.14,
    "note": "Greedy full_s1 998 docs: DR=10.21%, CF=2.57%, E_F1=59.37, R_F1=8.23. Beam eliminates ALL DR on DocRED 96-type schema."
  }
}

w8_llama_docred_ft_grammar_only: {
  "E_F1": 84.04,
  "R_F1": 43.77,
  "entity_precision": 84.99,
  "entity_recall": 83.11,
  "relation_precision": 38.6,
  "relation_recall": 50.53,
  "ET_pct": 0,
  "RV_pct": 0,
  "DR_pct": 0.51,
  "CF_pct": 0.12,
  "parse_fail_rate": 2.3,
  "total_samples": 998,
  "total_relations": 16199,
  "unique_entities": 13225,
  "parse_failures": 23
}

w8_llama_docred_ft_semantic_only: {
  "E_F1": 84.02,
  "E_P": 85.01,
  "E_R": 83.06,
  "R_F1": 43.9,
  "R_P": 38.89,
  "R_R": 50.4,
  "ET_pct": 0,
  "RV_pct": 0.15,
  "DR_pct": 0.3,
  "CF_pct": 0.16,
  "parse_fail_rate": 2.4,
  "total_samples": 998,
  "parse_failures": 24,
  "documents_checked": 974,
  "total_entities": 19099,
  "total_relations": 16038,
  "DR_violations": 48,
  "RV_violations": 24,
  "ET_violations": 0,
  "CF_violations": 31
}

w8_qwen_docred_ft_semantic_only: {
  "E_F1": 82.15,
  "E_P": 85.58,
  "E_R": 78.99,
  "R_F1": 40.89,
  "R_P": 36.35,
  "R_R": 46.73,
  "ET_pct": 0,
  "RV_pct": 0.23,
  "DR_pct": 0.21,
  "CF_pct": 0.27,
  "parse_fail_rate": 7.52,
  "total_samples": 998,
  "parse_failures": 75,
  "documents_checked": 923,
  "total_entities": 18025,
  "total_triples": 15909,
  "DR_violations": 34,
  "RV_violations": 37,
  "ET_violations": 0,
  "CF_violations": 49
}

w8_qwen_docred_ft_grammar_only: {
  "E_F1": 82.19,
  "E_P": 85.47,
  "E_R": 79.16,
  "R_F1": 40.85,
  "R_P": 36.27,
  "R_R": 46.77,
  "ET_pct": 0,
  "RV_pct": 0,
  "DR_pct": 0.61,
  "CF_pct": 0.11,
  "parse_fail_rate": 7.01,
  "total_samples": 998,
  "parse_failures": 70
}

w6_mistral_docred_unconstrained: {
  "total_samples": 998,
  "parse_failures": 7,
  "parse_fail_rate": 0.7,
  "total_pred_entities": 12580,
  "total_pred_relations": 11879,
  "ET_pct": 7.58,
  "RV_pct": 42.35,
  "DR_pct": 57.42,
  "CF_pct": 24.78,
  "E_P": 0.6221,
  "E_R": 0.3975,
  "E_F1": 0.4851,
  "R_P": 0.0447,
  "R_R": 0.0432,
  "R_F1": 0.0434,
  "f1_method": "fuzzy_normalized",
  "f1_note": "Relation matching uses case-insensitive normalization with token-overlap >80% and edit-distance \u22642 fallback. Strict R_F1=3.50% 

w6_mistral_docred_constrained: {
  "ET_pct": 0,
  "RV_pct": 0,
  "DR_pct": 33.2,
  "CF_pct": 0.19,
  "E_P": 65.02,
  "E_R": 41.4,
  "E_F1": 50.59,
  "R_P": 5.67,
  "R_R": 5.37,
  "R_F1": 5.52,
  "parse_fail_rate": 0.8,
  "total_samples": 998,
  "total_pred_entities": 12535,
  "total_pred_relations": 11554,
  "delta_vs_unconstrained": {
    "ET_pct": -7.58,
    "RV_pct": -42.35,
    "DR_pct": -24.22,
    "CF_pct": -24.59,
    "E_F1": 2.08,
    "R_F1": 2.02
  }
}

w5_qwen_docred_lora_constrained_eval: {
  "ET_pct": 0,
  "RV_pct": 0,
  "DR_pct": 0.01,
  "CF_pct": 0.41,
  "E_F1": 81.43,
  "E_P": 85.41,
  "E_R": 77.81,
  "R_F1": 40.56,
  "R_P": 36.35,
  "R_R": 45.86,
  "parse_fail_rate": 8.52,
  "total_samples": 998,
  "success_samples": 913,
  "fail_samples": 85,
  "total_entities_pred": 17799,
  "total_relations_pred": 15563,
  "E_F1_excl_fail": 85.69,
  "R_F1_excl_fail": 42.23,
  "delta_vs_unconstrained": {
    "delta_DR": -0.75,
    "delta_RV": -0.27,
    "delta_R_F1": -0.3,
    "delta_R_F1_

w5_qwen_docred_lora_unconstrained_eval: {
  "ET_pct": 0,
  "RV_pct": 0.27,
  "DR_pct": 0.76,
  "CF_pct": 0.12,
  "E_F1": 82.15,
  "E_P": 85.44,
  "E_R": 79.11,
  "R_F1": 40.86,
  "R_P": 36.41,
  "R_R": 46.56,
  "parse_fail_rate": 7.11,
  "total_samples": 998,
  "success_samples": 927,
  "fail_samples": 71,
  "total_entities_pred": 18091,
  "total_relations_pred": 15870,
  "ET_pct_excl_fail": 0,
  "RV_pct_excl_fail": 0.27,
  "DR_pct_excl_fail": 0.76,
  "CF_pct_excl_fail": 0.12,
  "E_F1_excl_fail": 85.72,
  "E_P_excl_fail": 85.44,
  "E_

w5_llama_docred_lora_unconstrained_eval: {
  "ET_pct": 0,
  "RV_pct": 0.15,
  "DR_pct": 0.49,
  "E_F1": 83.93,
  "E_P": 84.93,
  "E_R": 82.96,
  "R_F1": 43.72,
  "R_P": 38.59,
  "R_R": 50.41,
  "parse_fail_rate": 2.3,
  "total_samples": 998,
  "total_entities_pred": 19106,
  "total_relations_pred": 16171
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "bf573c78-d371-4865-bb01-5c0cbca41ba0",
  "tool_use_result": {
    "stdout": "=== SciERC FT unconstrained baselines ===\neval_70b_lora_scierc_unconstrained: DR=None, metrics_keys=[]\nw5_llama_lora_scierc_unconstrained_eval: DR=0.0111, metrics_keys=['total_samples', 'total_entities', 'total_relations', 'json_parse_rate', 'entity_type_violation_rate', 'relation_vocabulary_violation_rate', 'domain_range_violation_rate', 'cross_field_consistency_violation_rate', 'total_violation_rate', 'entity_precision']\nw5_lora_scierc_unconstrained_eval: DR=0.0195, metrics_keys=['json_parse_rate', 'entity_type_violation_rate', 'relation_vocabulary_violation_rate', 'domain_range_violation_rate', 'cross_field_consistency_violation_rate', 'entity_f1', 'entity_precision', 'entity_recall', 'relation_f1', 'relation_precision']\n\n=== SciERC FT full S1 ===\nd062_full_ft_scierc: DR=None\n\n=== All SciERC unconstrained experiments ===\neval_70b_lora_scierc_unconstrained: status=RUNNING, DR=None\n70b_scierc_unconstrained: status=DONE, DR=6.5\nw5_llama_lora_scierc_unconstrained_eval: status=DONE, DR=0.0111\nw6_mistral_scierc_unconstrained: status=DONE, DR=56.94\nw5_lora_scierc_unconstrained_eval: status=DONE, DR=0.0195\nllama_scierc_unconstrained: status=DONE, DR=0.1334\nphase2_scierc_unconstrained: status=DONE, DR=0.1537\n\n=== Any DocRED timing/overhead data ===\nw10_llama_docred_beam_50: {\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 0,\n  \"CF_pct\": 0.94,\n  \"E_F1\": 55.62,\n  \"R_F1\": 9.47,\n  \"parse_failures\": 3,\n  \"parse_fail_rate\": 6,\n  \"total_samples\": 50,\n  \"vs_greedy_full_s1\": {\n    \"DR_delta\": -2.57,\n    \"CF_delta\": -11.19,\n    \"E_F1_delta\": 0.61,\n    \"R_F1_delta\": 3.2,\n    \"note\": \"Greedy baseline: DR=2.57%, CF=12.13%, E_F1=55.01, R_F1=6.27\"\n  },\n  \"checker_note\": \"Must use violation_checker_docred.py for DocRED (not violation_checker.py)\"\n}\n\nw9_qwen_docred_beam_50: {\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 0,\n  \"CF_pct\": 0.55,\n  \"E_F1\": 58.64,\n  \"R_F1\": 9.37,\n  \"total_samples\": 50,\n  \"parse_failures\": 3,\n  \"parse_fail_rate\": 6,\n  \"vs_greedy_full_s1\": {\n    \"DR_delta\": -10.21,\n    \"CF_delta\": -2.02,\n    \"E_F1_delta\": -0.73,\n    \"R_F1_delta\": 1.14,\n    \"note\": \"Greedy full_s1 998 docs: DR=10.21%, CF=2.57%, E_F1=59.37, R_F1=8.23. Beam eliminates ALL DR on DocRED 96-type schema.\"\n  }\n}\n\nw8_llama_docred_ft_grammar_only: {\n  \"E_F1\": 84.04,\n  \"R_F1\": 43.77,\n  \"entity_precision\": 84.99,\n  \"entity_recall\": 83.11,\n  \"relation_precision\": 38.6,\n  \"relation_recall\": 50.53,\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 0.51,\n  \"CF_pct\": 0.12,\n  \"parse_fail_rate\": 2.3,\n  \"total_samples\": 998,\n  \"total_relations\": 16199,\n  \"unique_entities\": 13225,\n  \"parse_failures\": 23\n}\n\nw8_llama_docred_ft_semantic_only: {\n  \"E_F1\": 84.02,\n  \"E_P\": 85.01,\n  \"E_R\": 83.06,\n  \"R_F1\": 43.9,\n  \"R_P\": 38.89,\n  \"R_R\": 50.4,\n  \"ET_pct\": 0,\n  \"RV_pct\": 0.15,\n  \"DR_pct\": 0.3,\n  \"CF_pct\": 0.16,\n  \"parse_fail_rate\": 2.4,\n  \"total_samples\": 998,\n  \"parse_failures\": 24,\n  \"documents_checked\": 974,\n  \"total_entities\": 19099,\n  \"total_relations\": 16038,\n  \"DR_violations\": 48,\n  \"RV_violations\": 24,\n  \"ET_violations\": 0,\n  \"CF_violations\": 31\n}\n\nw8_qwen_docred_ft_semantic_only: {\n  \"E_F1\": 82.15,\n  \"E_P\": 85.58,\n  \"E_R\": 78.99,\n  \"R_F1\": 40.89,\n  \"R_P\": 36.35,\n  \"R_R\": 46.73,\n  \"ET_pct\": 0,\n  \"RV_pct\": 0.23,\n  \"DR_pct\": 0.21,\n  \"CF_pct\": 0.27,\n  \"parse_fail_rate\": 7.52,\n  \"total_samples\": 998,\n  \"parse_failures\": 75,\n  \"documents_checked\": 923,\n  \"total_entities\": 18025,\n  \"total_triples\": 15909,\n  \"DR_violations\": 34,\n  \"RV_violations\": 37,\n  \"ET_violations\": 0,\n  \"CF_violations\": 49\n}\n\nw8_qwen_docred_ft_grammar_only: {\n  \"E_F1\": 82.19,\n  \"E_P\": 85.47,\n  \"E_R\": 79.16,\n  \"R_F1\": 40.85,\n  \"R_P\": 36.27,\n  \"R_R\": 46.77,\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 0.61,\n  \"CF_pct\": 0.11,\n  \"parse_fail_rate\": 7.01,\n  \"total_samples\": 998,\n  \"parse_failures\": 70\n}\n\nw6_mistral_docred_unconstrained: {\n  \"total_samples\": 998,\n  \"parse_failures\": 7,\n  \"parse_fail_rate\": 0.7,\n  \"total_pred_entities\": 12580,\n  \"total_pred_relations\": 11879,\n  \"ET_pct\": 7.58,\n  \"RV_pct\": 42.35,\n  \"DR_pct\": 57.42,\n  \"CF_pct\": 24.78,\n  \"E_P\": 0.6221,\n  \"E_R\": 0.3975,\n  \"E_F1\": 0.4851,\n  \"R_P\": 0.0447,\n  \"R_R\": 0.0432,\n  \"R_F1\": 0.0434,\n  \"f1_method\": \"fuzzy_normalized\",\n  \"f1_note\": \"Relation matching uses case-insensitive normalization with token-overlap >80% and edit-distance \\u22642 fallback. Strict R_F1=3.50% \n\nw6_mistral_docred_constrained: {\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 33.2,\n  \"CF_pct\": 0.19,\n  \"E_P\": 65.02,\n  \"E_R\": 41.4,\n  \"E_F1\": 50.59,\n  \"R_P\": 5.67,\n  \"R_R\": 5.37,\n  \"R_F1\": 5.52,\n  \"parse_fail_rate\": 0.8,\n  \"total_samples\": 998,\n  \"total_pred_entities\": 12535,\n  \"total_pred_relations\": 11554,\n  \"delta_vs_unconstrained\": {\n    \"ET_pct\": -7.58,\n    \"RV_pct\": -42.35,\n    \"DR_pct\": -24.22,\n    \"CF_pct\": -24.59,\n    \"E_F1\": 2.08,\n    \"R_F1\": 2.02\n  }\n}\n\nw5_qwen_docred_lora_constrained_eval: {\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 0.01,\n  \"CF_pct\": 0.41,\n  \"E_F1\": 81.43,\n  \"E_P\": 85.41,\n  \"E_R\": 77.81,\n  \"R_F1\": 40.56,\n  \"R_P\": 36.35,\n  \"R_R\": 45.86,\n  \"parse_fail_rate\": 8.52,\n  \"total_samples\": 998,\n  \"success_samples\": 913,\n  \"fail_samples\": 85,\n  \"total_entities_pred\": 17799,\n  \"total_relations_pred\": 15563,\n  \"E_F1_excl_fail\": 85.69,\n  \"R_F1_excl_fail\": 42.23,\n  \"delta_vs_unconstrained\": {\n    \"delta_DR\": -0.75,\n    \"delta_RV\": -0.27,\n    \"delta_R_F1\": -0.3,\n    \"delta_R_F1_\n\nw5_qwen_docred_lora_unconstrained_eval: {\n  \"ET_pct\": 0,\n  \"RV_pct\": 0.27,\n  \"DR_pct\": 0.76,\n  \"CF_pct\": 0.12,\n  \"E_F1\": 82.15,\n  \"E_P\": 85.44,\n  \"E_R\": 79.11,\n  \"R_F1\": 40.86,\n  \"R_P\": 36.41,\n  \"R_R\": 46.56,\n  \"parse_fail_rate\": 7.11,\n  \"total_samples\": 998,\n  \"success_samples\": 927,\n  \"fail_samples\": 71,\n  \"total_entities_pred\": 18091,\n  \"total_relations_pred\": 15870,\n  \"ET_pct_excl_fail\": 0,\n  \"RV_pct_excl_fail\": 0.27,\n  \"DR_pct_excl_fail\": 0.76,\n  \"CF_pct_excl_fail\": 0.12,\n  \"E_F1_excl_fail\": 85.72,\n  \"E_P_excl_fail\": 85.44,\n  \"E_\n\nw5_llama_docred_lora_unconstrained_eval: {\n  \"ET_pct\": 0,\n  \"RV_pct\": 0.15,\n  \"DR_pct\": 0.49,\n  \"E_F1\": 83.93,\n  \"E_P\": 84.93,\n  \"E_R\": 82.96,\n  \"R_F1\": 43.72,\n  \"R_P\": 38.59,\n  \"R_R\": 50.41,\n  \"parse_fail_rate\": 2.3,\n  \"total_samples\": 998,\n  \"total_entities_pred\": 19106,\n  \"total_relations_pred\": 16171\n}",
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

<details><summary>Logged reasoning block</summary>

```text
Now let me also find the DocRED ZS latency overhead data. The paper claims "+2.43% on DocRED". Let me search more specifically.

Also, I need to find:
1. The "24% DR reduction" for grammar-only - I need to look at the ablation table.
2. The 1.18% CF in 8B composability
3. The "15-96%" DR range for trie-only 
4. The "1-15% unconstrained" DR for comparison

Let me also look at the ablation table and related experiment data for composability.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "41256d25-b715-4c93-add5-59378942b1a2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AEmkX4pevdTrPdUXtRx8nk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4507,
      "cache_read_input_tokens": 41552,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4507
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

_source line 55_

<details open><summary>🔧 Tool call — Bash · `toolu_016bLgf1QUGpKzA4bxV4Rehb`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/06688fc2-d26c-40b0-8ebe-68d505b40c0d/tool-results/mcp-agent-ml-research-read_registry-1779422951081.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n\n# 1. DocRED ZS latency - check the r16 70B DocRED ZS experiment and also any docred timing data\nprint('=== r16_70b_docred_zs_s1 ===')\ne = exps.get('r16_70b_docred_zs_s1', {})\nprint(json.dumps(e, indent=2)[:1000])\n\nprint()\n# 2. 70b_docred_constrained and unconstrained\nprint('=== 70b_docred_constrained ===')\nprint(json.dumps(exps.get('70b_docred_constrained', {}).get('metrics', {}), indent=2))\nprint()\nprint('=== 70b_docred_unconstrained ===')\nprint(json.dumps(exps.get('70b_docred_unconstrained', {}).get('metrics', {}), indent=2))\n\n# 3. Look at section5 ablation table experiments\nprint()\nprint('=== Composability / section cross-references ===')\n# The paper mentions 9.90% → 1.18% as 8B pattern  \n# 9.90 was found in w9_qwen_scierc_zs_sampling and w10_type_consensus_prototype\n# Need to look at section composability for the actual experiments\n\n# 4. Look for any experiment with 'composab' or 'compos'\nfor k in exps:\n    if 'compos' in k.lower():\n        m = exps[k].get('metrics', {})\n        print(f'{k}: {json.dumps(m, indent=2)[:300]}')\n        print()\n\" 2>&1",
  "description": "Find 70B DocRED data and composability experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "cb97e6fe-4d30-49a6-aac7-edf8f46091e2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AEmkX4pevdTrPdUXtRx8nk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4507,
      "cache_read_input_tokens": 41552,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4507
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

_source line 56 · 2026-05-22T04:12:11.906Z_

<details><summary>↩ Tool result · `toolu_016bLgf1QUGpKzA4bxV4Rehb`</summary>

```text
=== r16_70b_docred_zs_s1 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-21T05:03:19.394Z",
  "updated_at": "2026-05-22T02:07:51.929Z",
  "hypothesis": "Llama-3.1-70B-Instruct-AWQ-INT4 with Full S1 constrained decoding on DocRED ZS will achieve DR\u21920% with R-F1 stable vs unconstrained, extending 70B SciERC results to DocRED and confirming scale-independent constraint effectiveness across datasets",
  "spec": {
    "command": "bash /root/schema_semantic_constrained_ie/run_70b_docred_zs.sh",
    "server": "westd-21461",
    "gpu": "cuda:1",
    "data_path": "data/docred/dev.json",
    "data_count": 998,
    "model_name": "Llama-3.1-70B-Instruct-AWQ-INT4",
    "model_path": "/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4",
    "seed": 42,
    "checkpoint_path": "N/A",
    "log_path": "/root/autodl-tmp/schema_outputs/r16_70b_docred_zs_s1.log"
  },
  "failure_reason": "startup recovery: RUNNING with no cron and no server/pid info",
  "conclusion": "failed",
  "com

=== 70b_docred_constrained ===
{
  "ET_violation": 0,
  "RV_violation": 0,
  "DR_violation": 0,
  "CF_violation": 7.01,
  "entity_f1": 69.05,
  "entity_precision": 75.03,
  "entity_recall": 63.95,
  "relation_f1": 13.07,
  "relation_precision": 12.54,
  "relation_recall": 13.64,
  "parse_failures": 1,
  "docs_processed": 997,
  "total_docs": 998,
  "unique_entities": 12207,
  "total_triples": 13249
}

=== 70b_docred_unconstrained ===
{
  "entity_f1": 69.03,
  "entity_precision": 75.03,
  "entity_recall": 63.92,
  "relation_f1": 13.03,
  "relation_precision": 12.43,
  "relation_recall": 13.69,
  "ET_violation": 0.02,
  "RV_violation": 7.8,
  "DR_violation": 15,
  "CF_violation": 0.07,
  "parse_failures": 0,
  "docs_processed": 998
}

=== Composability / section cross-references ===
p1_ee_ft_composability_r5: {
  "unconstrained": {
    "parse_rate": 0.85,
    "trigger_f1": 0.3208,
    "argument_f1": 0.0785,
    "rov_rate": 0.3831,
    "ac_rate": 0.0268,
    "go_nogo": 0.41
  },
  "full_s1": {
    "parse_rate": 0.95,
    "trigger_f1": 0.2672,
    "argument_f1": 0.0818,
    "rov_rate": 0,
    "ac_rate": 0,

p1_ee_ft_composability_r4: {
  "unconstrained": {
    "entity_f1": 0,
    "trigger_f1": 0.4598,
    "argument_f1": 0.1581,
    "rov": 0.251,
    "ac": 0.06,
    "cf": 0,
    "parse_rate": 0.25
  },
  "full_s1": {
    "entity_f1": 0.5823,
    "trigger_f1": 0.6,
    "argument_f1": 0.4667,
    "rov": 0,
    "ac": 0,
    "cf": 0.

p1_ee_ft_composability_r3: {}

p1_ee_ft_composability_r2: {}

p1_ee_ft_composability: {}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "3bfe071e-2256-4993-9402-253e7aef032e",
  "tool_use_result": {
    "stdout": "=== r16_70b_docred_zs_s1 ===\n{\n  \"status\": \"DONE\",\n  \"retry_count\": 0,\n  \"created_at\": \"2026-05-21T05:03:19.394Z\",\n  \"updated_at\": \"2026-05-22T02:07:51.929Z\",\n  \"hypothesis\": \"Llama-3.1-70B-Instruct-AWQ-INT4 with Full S1 constrained decoding on DocRED ZS will achieve DR\\u21920% with R-F1 stable vs unconstrained, extending 70B SciERC results to DocRED and confirming scale-independent constraint effectiveness across datasets\",\n  \"spec\": {\n    \"command\": \"bash /root/schema_semantic_constrained_ie/run_70b_docred_zs.sh\",\n    \"server\": \"westd-21461\",\n    \"gpu\": \"cuda:1\",\n    \"data_path\": \"data/docred/dev.json\",\n    \"data_count\": 998,\n    \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4\",\n    \"model_path\": \"/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4\",\n    \"seed\": 42,\n    \"checkpoint_path\": \"N/A\",\n    \"log_path\": \"/root/autodl-tmp/schema_outputs/r16_70b_docred_zs_s1.log\"\n  },\n  \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\",\n  \"conclusion\": \"failed\",\n  \"com\n\n=== 70b_docred_constrained ===\n{\n  \"ET_violation\": 0,\n  \"RV_violation\": 0,\n  \"DR_violation\": 0,\n  \"CF_violation\": 7.01,\n  \"entity_f1\": 69.05,\n  \"entity_precision\": 75.03,\n  \"entity_recall\": 63.95,\n  \"relation_f1\": 13.07,\n  \"relation_precision\": 12.54,\n  \"relation_recall\": 13.64,\n  \"parse_failures\": 1,\n  \"docs_processed\": 997,\n  \"total_docs\": 998,\n  \"unique_entities\": 12207,\n  \"total_triples\": 13249\n}\n\n=== 70b_docred_unconstrained ===\n{\n  \"entity_f1\": 69.03,\n  \"entity_precision\": 75.03,\n  \"entity_recall\": 63.92,\n  \"relation_f1\": 13.03,\n  \"relation_precision\": 12.43,\n  \"relation_recall\": 13.69,\n  \"ET_violation\": 0.02,\n  \"RV_violation\": 7.8,\n  \"DR_violation\": 15,\n  \"CF_violation\": 0.07,\n  \"parse_failures\": 0,\n  \"docs_processed\": 998\n}\n\n=== Composability / section cross-references ===\np1_ee_ft_composability_r5: {\n  \"unconstrained\": {\n    \"parse_rate\": 0.85,\n    \"trigger_f1\": 0.3208,\n    \"argument_f1\": 0.0785,\n    \"rov_rate\": 0.3831,\n    \"ac_rate\": 0.0268,\n    \"go_nogo\": 0.41\n  },\n  \"full_s1\": {\n    \"parse_rate\": 0.95,\n    \"trigger_f1\": 0.2672,\n    \"argument_f1\": 0.0818,\n    \"rov_rate\": 0,\n    \"ac_rate\": 0,\n\np1_ee_ft_composability_r4: {\n  \"unconstrained\": {\n    \"entity_f1\": 0,\n    \"trigger_f1\": 0.4598,\n    \"argument_f1\": 0.1581,\n    \"rov\": 0.251,\n    \"ac\": 0.06,\n    \"cf\": 0,\n    \"parse_rate\": 0.25\n  },\n  \"full_s1\": {\n    \"entity_f1\": 0.5823,\n    \"trigger_f1\": 0.6,\n    \"argument_f1\": 0.4667,\n    \"rov\": 0,\n    \"ac\": 0,\n    \"cf\": 0.\n\np1_ee_ft_composability_r3: {}\n\np1_ee_ft_composability_r2: {}\n\np1_ee_ft_composability: {}",
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

_source line 57_

<details><summary>Logged reasoning block</summary>

```text
Now I need to find:
1. DocRED latency overhead 2.43% - p8b_docred_latency failed with no metrics. I need to check if there's other data, or if this number was computed separately outside the registry. Let me check the ablation/section tables.

2. The "37% lower absolute latency" under LoRA - my calculation shows 39.0% based on constrained means (4.71 vs 2.873). The difference might be because the paper uses a different calculation basis.

3. The "24% DR reduction" for grammar-only - Need to calculate: unconstrained DR vs grammar-only DR on the appropriate dataset.


4. The "15-96%" DR range for trie-only and "1-15%" for unconstrained - I need to verify these numbers against the data.
5. The CF pattern showing 9.90% → 1.18% - checking if this holds across the metrics. Let me look at the section files and ablation table to trace where these values come from, particularly the 24% figure and the composability section reference.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "50268f42-eadf-48b5-928d-5a03b706cae9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DhCPQvtdTDtbxp6Lfxx7Rm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1977,
      "cache_read_input_tokens": 46059,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1977
      },
      "output_tokens": 10,
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

_source line 58_

<details open><summary>🔧 Tool call — Agent · `toolu_01CA4Q1cfQkVV53LnHsJprUE`</summary>

```json
{
  "description": "Find ablation table and composability data",
  "subagent_type": "Explore",
  "prompt": "In the directory /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/, find:\n1. The ablation table file (likely table with \"ablation\" in filename or containing \\label{tab:scierc-ablation})\n2. Any file containing the composability section (section ref sec:composability or mentions \"9.90\" and \"1.18\")\n3. The beam latency table (containing \\label{tab:beam-latency})\n4. Any file mentioning \"2.43\" as a latency/overhead percentage\n\nSearch breadth: medium. Report the file paths and the relevant content lines."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "e8c07a46-71e6-4200-8c13-4b64a491e724",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DhCPQvtdTDtbxp6Lfxx7Rm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1977,
      "cache_read_input_tokens": 46059,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1977
      },
      "output_tokens": 10,
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

_source line 59_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "afa4f506883d7ac8a",
  "tool_use_id": "toolu_01CA4Q1cfQkVV53LnHsJprUE",
  "description": "Find ablation table and composability data",
  "task_type": "local_agent",
  "prompt": "In the directory /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/, find:\n1. The ablation table file (likely table with \"ablation\" in filename or containing \\label{tab:scierc-ablation})\n2. Any file containing the composability section (section ref sec:composability or mentions \"9.90\" and \"1.18\")\n3. The beam latency table (containing \\label{tab:beam-latency})\n4. Any file mentioning \"2.43\" as a latency/overhead percentage\n\nSearch breadth: medium. Report the file paths and the relevant content lines.",
  "uuid": "9bce10b0-0553-4c24-b10e-8c79a4656bfa",
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d"
}
```

---

## Round 1

67 recorded events

### User

_source line 60 · 2026-05-22T04:12:27.022Z_

In the directory /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/, find:
1. The ablation table file (likely table with "ablation" in filename or containing \label{tab:scierc-ablation})
2. Any file containing the composability section (section ref sec:composability or mentions "9.90" and "1.18")
3. The beam latency table (containing \label{tab:beam-latency})
4. Any file mentioning "2.43" as a latency/overhead percentage

Search breadth: medium. Report the file paths and the relevant content lines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CA4Q1cfQkVV53LnHsJprUE",
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "7a5ee7cb-de73-4ee7-a9ca-ae3c82c37296"
}
```

</details>

---

### System

_source line 61_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "afa4f506883d7ac8a",
  "tool_use_id": "toolu_01CA4Q1cfQkVV53LnHsJprUE",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_050…",
  "usage": {
    "total_tokens": 19361,
    "tool_uses": 1,
    "duration_ms": 3114
  },
  "last_tool_name": "Bash",
  "uuid": "8b63c7b4-6ffa-495d-b144-73699a824e70",
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d"
}
```

---

### Tool call

_source line 62_

<details open><summary>🔧 Tool call — Bash · `toolu_01JfAsnTaGvH7tsVZYcqHX2N`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/ -type f -name \"*.tex\" -o -name \"*.txt\" -o -name \"*.md\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CA4Q1cfQkVV53LnHsJprUE",
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "eca228ef-b9bd-400c-bf55-de1013bc38ed",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ScT2ZT29u5XfUAWjq8zVWs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19346,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19346,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 63 · 2026-05-22T04:12:30.216Z_

<details><summary>↩ Tool result · `toolu_01JfAsnTaGvH7tsVZYcqHX2N`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_case_studies.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/case_study_kappa_dr.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract_fd4b26.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract_d3264e.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/r12_fallback_cascade_text.txt
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/paper_tables_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft_4796e8.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_scalability.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per_relation.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompt_sensitivity.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CA4Q1cfQkVV53LnHsJprUE",
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "1e3dac1d-6234-4fe9-90f8-77be666b37b2"
}
```

</details>

---

### System

_source line 64_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "afa4f506883d7ac8a",
  "tool_use_id": "toolu_01CA4Q1cfQkVV53LnHsJprUE",
  "description": "Searching for ablation|tab:scierc-ablation",
  "usage": {
    "total_tokens": 21288,
    "tool_uses": 2,
    "duration_ms": 5574
  },
  "last_tool_name": "Grep",
  "uuid": "0a906529-d8c7-4f51-bd18-9401d5c3290a",
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d"
}
```

---

### Tool call

_source line 65_

<details open><summary>🔧 Tool call — Grep · `toolu_01ThoLLZLtWubPyazFSHM8PZ`</summary>

```json
{
  "pattern": "ablation|tab:scierc-ablation",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CA4Q1cfQkVV53LnHsJprUE",
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "e0aa6a76-bdaf-432e-bb1d-620ac82b4115",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XL8qenyg12E6qShFJHYzwq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1923,
      "cache_read_input_tokens": 19346,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1923,
        "ephemeral_1h_input_tokens": 0
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

_source line 66 · 2026-05-22T04:12:32.620Z_

<details><summary>↩ Tool result · `toolu_01ThoLLZLtWubPyazFSHM8PZ`</summary>

```text
Found 13 files
artifacts/_project/paper/main.aux
artifacts/_project/paper/main.tex
artifacts/_project/paper/section1_introduction_draft.tex
artifacts/_project/paper/section5_runtime.tex
artifacts/_project/paper/appendix_beam_search.tex
artifacts/_project/paper/appendix_discussion.tex
artifacts/_project/paper/section5_docred_draft.tex
artifacts/_project/paper/section5_scierc_draft.tex
artifacts/_project/paper/appendix_related_work.tex
artifacts/_project/paper/section3_method_draft.tex
artifacts/_project/paper/section5_docred_draft_9b84f1.tex
artifacts/_project/paper/paper_tables_draft.tex
artifacts/_project/paper/section5_scierc_draft_4796e8.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CA4Q1cfQkVV53LnHsJprUE",
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "644339db-6b6d-40af-833d-6be50ee1e65f"
}
```

</details>

---

### System

_source line 67_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "afa4f506883d7ac8a",
  "tool_use_id": "toolu_01CA4Q1cfQkVV53LnHsJprUE",
  "description": "Searching for sec:composability|9\\.90.*1\\.18|1\\.18.*9\\.90",
  "usage": {
    "total_tokens": 21289,
    "tool_uses": 3,
    "duration_ms": 6185
  },
  "last_tool_name": "Grep",
  "uuid": "58c37775-2228-4c36-87f3-857492d81954",
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d"
}
```

---

### Tool call

_source line 68_

<details open><summary>🔧 Tool call — Grep · `toolu_01Vk2q7kyAJSoHMr41zcwyWn`</summary>

```json
{
  "pattern": "sec:composability|9\\.90.*1\\.18|1\\.18.*9\\.90",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CA4Q1cfQkVV53LnHsJprUE",
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "a6fc0c02-b61b-423d-b1bd-5549cb5536ec",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XL8qenyg12E6qShFJHYzwq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1923,
      "cache_read_input_tokens": 19346,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1923,
        "ephemeral_1h_input_tokens": 0
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

_source line 69 · 2026-05-22T04:12:33.232Z_

<details><summary>↩ Tool result · `toolu_01Vk2q7kyAJSoHMr41zcwyWn`</summary>

```text
Found 6 files
artifacts/_project/paper/main.aux
artifacts/_project/paper/section5_runtime.tex
artifacts/_project/paper/appendix_discussion.tex
artifacts/_project/paper/section5_crossmodel_draft.tex
artifacts/_project/paper/section5_scierc_draft.tex
artifacts/_project/paper/section3_violation_landscape.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CA4Q1cfQkVV53LnHsJprUE",
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "8145aaab-befb-4c95-aa5e-6d9e6ae20389"
}
```

</details>

---

### System

_source line 70_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "afa4f506883d7ac8a",
  "tool_use_id": "toolu_01CA4Q1cfQkVV53LnHsJprUE",
  "description": "Searching for tab:beam-latency",
  "usage": {
    "total_tokens": 21290,
    "tool_uses": 4,
    "duration_ms": 6605
  },
  "last_tool_name": "Grep",
  "uuid": "4973b2f8-6425-4bda-be75-42a8517c8a7d",
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d"
}
```

---

### Tool call

_source line 71_

<details open><summary>🔧 Tool call — Grep · `toolu_01Qg16WCzjQELMH87hFGvwCR`</summary>

```json
{
  "pattern": "tab:beam-latency",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CA4Q1cfQkVV53LnHsJprUE",
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "dfdf997c-29df-4126-a86b-5603bb09f8ec",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XL8qenyg12E6qShFJHYzwq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1923,
      "cache_read_input_tokens": 19346,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1923,
        "ephemeral_1h_input_tokens": 0
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

_source line 72 · 2026-05-22T04:12:33.648Z_

<details><summary>↩ Tool result · `toolu_01Qg16WCzjQELMH87hFGvwCR`</summary>

```text
Found 3 files
artifacts/_project/paper/main.aux
artifacts/_project/paper/section5_runtime.tex
artifacts/_project/paper/appendix_beam_search.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CA4Q1cfQkVV53LnHsJprUE",
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "402753bc-12de-4b91-89b9-926398ec7cd4"
}
```

</details>

---

### System

_source line 73_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "afa4f506883d7ac8a",
  "tool_use_id": "toolu_01CA4Q1cfQkVV53LnHsJprUE",
  "description": "Searching for 2\\.43",
  "usage": {
    "total_tokens": 21291,
    "tool_uses": 5,
    "duration_ms": 6990
  },
  "last_tool_name": "Grep",
  "uuid": "07bf6528-9481-4dd1-8326-5d04607b0c1b",
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d"
}
```

---

### Tool call

_source line 74_

<details open><summary>🔧 Tool call — Grep · `toolu_0123XS9MXrLCTDtvsPE5bfXB`</summary>

```json
{
  "pattern": "2\\.43",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CA4Q1cfQkVV53LnHsJprUE",
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "91b7dd79-7d0c-4e21-9feb-12eabbdf2502",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XL8qenyg12E6qShFJHYzwq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1923,
      "cache_read_input_tokens": 19346,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1923,
        "ephemeral_1h_input_tokens": 0
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

_source line 75 · 2026-05-22T04:12:34.031Z_

<details><summary>↩ Tool result · `toolu_0123XS9MXrLCTDtvsPE5bfXB`</summary>

```text
Found 3 files
artifacts/_project/paper/section5_runtime.tex
artifacts/_project/paper/appendix_discussion.tex
artifacts/_project/paper/appendix_reproducibility.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CA4Q1cfQkVV53LnHsJprUE",
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "58450cb7-a1e5-4de5-a59e-d06e27637ad6"
}
```

</details>

---

### System

_source line 76_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "afa4f506883d7ac8a",
  "tool_use_id": "toolu_01CA4Q1cfQkVV53LnHsJprUE",
  "description": "Searching for ablation|tab:scierc-ablation",
  "usage": {
    "total_tokens": 22289,
    "tool_uses": 6,
    "duration_ms": 9425
  },
  "last_tool_name": "Grep",
  "uuid": "df307666-58ae-4f6d-8229-2005a8e2796f",
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d"
}
```

---

### Tool call

_source line 77_

<details open><summary>🔧 Tool call — Grep · `toolu_01UVTVsBj43bq7NZqiWjEYwH`</summary>

```json
{
  "pattern": "ablation|tab:scierc-ablation",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
  "output_mode": "content",
  "context": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CA4Q1cfQkVV53LnHsJprUE",
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "57d9110c-62c6-4329-9395-ab447df1418b",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LrmDL3aT6nKfbTaAu67pzM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 995,
      "cache_read_input_tokens": 21269,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 995,
        "ephemeral_1h_input_tokens": 0
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

_source line 78 · 2026-05-22T04:12:36.474Z_

<details><summary>↩ Tool result · `toolu_01UVTVsBj43bq7NZqiWjEYwH`</summary>

```text
7-\subsection{Ablation and Composability with Fine-Tuning}
8-\label{sec:scierc-results}
9-
10:Table~\ref{tab:scierc-ablation} presents the five-way ablation on SciERC (Qwen3-8B, zero-shot, 551 documents); only the active constraint layers differ across rows.
11-
12-% ──────────────────────────────────────────
13:%  Table: SciERC five-way ablation
14-% ──────────────────────────────────────────
15-\begin{table}[t]
16-\centering
--
54-  & 8.03  & \textbf{31.90} \\
55-\bottomrule
56-\end{tabular}}%
57:\caption{Five-way ablation on SciERC (551 docs, Qwen3-8B, zero-shot).
58-$\Delta$DR: relative change vs.\ unconstrained.
59-Tot.\ = DR + CF (total type-violation burden).
60-Best per column in \textbf{bold} (CF excluded; Tot.\ included).
--
62-CF: same entity assigned conflicting types across triples.
63-S1 = single-pass (\S\ref{sec:strategies}), S2 = two-pass (\S\ref{sec:s2}).
64-Grammar-only represents the ceiling of grammar-constrained decoding~\cite{geng2023gcd}: vocabulary membership is enforced but cross-field semantic constraints are not.}
65:\label{tab:scierc-ablation}
66-\end{table}
67-
68-% ──────────────────────────────────────────
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CA4Q1cfQkVV53LnHsJprUE",
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "c12bdb85-3c82-448f-bfcb-eb768072dcd6"
}
```

</details>

---

### System

_source line 79_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "afa4f506883d7ac8a",
  "tool_use_id": "toolu_01CA4Q1cfQkVV53LnHsJprUE",
  "description": "Searching for sec:composability",
  "usage": {
    "total_tokens": 22290,
    "tool_uses": 7,
    "duration_ms": 9808
  },
  "last_tool_name": "Grep",
  "uuid": "afe77cb7-dc77-4988-948b-09cc589863e6",
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d"
}
```

---

### Tool call

_source line 80_

<details open><summary>🔧 Tool call — Grep · `toolu_01VPzFkUWgTmWL8KAN4mQMJe`</summary>

```json
{
  "pattern": "sec:composability",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex",
  "output_mode": "content",
  "context": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CA4Q1cfQkVV53LnHsJprUE",
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "d5f66ba2-82a6-41bb-a588-1803b3589866",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LrmDL3aT6nKfbTaAu67pzM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 995,
      "cache_read_input_tokens": 21269,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 995,
        "ephemeral_1h_input_tokens": 0
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

_source line 81 · 2026-05-22T04:12:36.861Z_

<details><summary>↩ Tool result · `toolu_01VPzFkUWgTmWL8KAN4mQMJe`</summary>

```text
14-% exp_ids: r16_70b_scierc_zs_s1, 70b_lora_scierc, 70b_lora_docred_200
15-\paragraph{70B evaluation.}
16-\label{sec:70b-results}
17-On Llama-3.3-70B-Instruct (AWQ INT4), zero-shot S1 eliminates DR on SciERC (6.41\%\,$\to$\,0\%; R-F1 11.24, $+$0.09\,pp) with CF 3.50\% (from 0\% unconstrained).
18-% TODO: 待 70B LoRA 结果回填（SciERC 551 docs, DocRED 200-doc subset）
19:LoRA fine-tuning confirms scale-independent composability: SciERC DR XX.XX\%\,$\to$\,XX.XX\% (R-F1 XX.XX); DocRED (200-document subset) DR XX.XX\%\,$\to$\,XX.XX\% (R-F1 XX.XX); CF drops to XX.XX--XX.XX\%, consistent with the 8B pattern (9.90\%\,$\to$\,1.18\%; \S\ref{sec:composability}).
20-
21-% exp_ids: trie_qwen_ft_scierc, trie_qwen_zs_scierc, trie_llama_ft_scierc, trie_llama_zs_scierc
22-\paragraph{Comparison with grammar-constrained approaches.}
23-\label{sec:constrained-baselines}
24-Our grammar-only ablation (Table~\ref{tab:scierc-ablation}, row~2) implements the same class of constraints---vocabulary membership via context-free grammars---as GCD~\cite{geng2023gcd} and the grammar component of BoostCD~\cite{boostcd2025}, achieving RV/ET$\to$0\% but only 24\% DR reduction vs.\ Full S1's 94\%.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CA4Q1cfQkVV53LnHsJprUE",
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "4f409590-88d3-4ec2-a03d-6b1a4dbaaa6c"
}
```

</details>

---

### System

_source line 82_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "afa4f506883d7ac8a",
  "tool_use_id": "toolu_01CA4Q1cfQkVV53LnHsJprUE",
  "description": "Searching for 9\\.90|1\\.18",
  "usage": {
    "total_tokens": 22291,
    "tool_uses": 8,
    "duration_ms": 9950
  },
  "last_tool_name": "Grep",
  "uuid": "23a0561b-bc02-4e9a-b908-80669ef09b87",
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d"
}
```

---

### Tool call

_source line 83_

<details open><summary>🔧 Tool call — Grep · `toolu_01T85cdTtji2wVzpYoGMhsVf`</summary>

```json
{
  "pattern": "9\\.90|1\\.18",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex",
  "output_mode": "content",
  "context": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CA4Q1cfQkVV53LnHsJprUE",
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "e522293d-69fe-4ba4-bafe-0ad6eed49b09",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LrmDL3aT6nKfbTaAu67pzM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 995,
      "cache_read_input_tokens": 21269,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 995,
        "ephemeral_1h_input_tokens": 0
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

_source line 84 · 2026-05-22T04:12:36.992Z_

<details><summary>↩ Tool result · `toolu_01T85cdTtji2wVzpYoGMhsVf`</summary>

```text
16-\label{sec:70b-results}
17-On Llama-3.3-70B-Instruct (AWQ INT4), zero-shot S1 eliminates DR on SciERC (6.41\%\,$\to$\,0\%; R-F1 11.24, $+$0.09\,pp) with CF 3.50\% (from 0\% unconstrained).
18-% TODO: 待 70B LoRA 结果回填（SciERC 551 docs, DocRED 200-doc subset）
19:LoRA fine-tuning confirms scale-independent composability: SciERC DR XX.XX\%\,$\to$\,XX.XX\% (R-F1 XX.XX); DocRED (200-document subset) DR XX.XX\%\,$\to$\,XX.XX\% (R-F1 XX.XX); CF drops to XX.XX--XX.XX\%, consistent with the 8B pattern (9.90\%\,$\to$\,1.18\%; \S\ref{sec:composability}).
20-
21-% exp_ids: trie_qwen_ft_scierc, trie_qwen_zs_scierc, trie_llama_ft_scierc, trie_llama_zs_scierc
22-\paragraph{Comparison with grammar-constrained approaches.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CA4Q1cfQkVV53LnHsJprUE",
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "64fc3ad8-b294-48b7-85a3-d75e8cc98023"
}
```

</details>

---

### System

_source line 85_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "afa4f506883d7ac8a",
  "tool_use_id": "toolu_01CA4Q1cfQkVV53LnHsJprUE",
  "description": "Searching for tab:beam-latency",
  "usage": {
    "total_tokens": 22292,
    "tool_uses": 9,
    "duration_ms": 10380
  },
  "last_tool_name": "Grep",
  "uuid": "b714bd22-8c4a-492f-b801-82c3f2a1ae79",
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d"
}
```

---

### Tool call

_source line 86_

<details open><summary>🔧 Tool call — Grep · `toolu_016DprHDYSBbU8UiVsRiwaH4`</summary>

```json
{
  "pattern": "tab:beam-latency",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex",
  "output_mode": "content",
  "context": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CA4Q1cfQkVV53LnHsJprUE",
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "8dbdeec7-f096-452f-94e0-aaeb6c3acb0c",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LrmDL3aT6nKfbTaAu67pzM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 995,
      "cache_read_input_tokens": 21269,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 995,
        "ephemeral_1h_input_tokens": 0
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

_source line 87 · 2026-05-22T04:12:37.414Z_

<details><summary>↩ Tool result · `toolu_016DprHDYSBbU8UiVsRiwaH4`</summary>

```text
186-Llama-3.1-8B achieves zero violations across all four metrics (ET, RV, DR, CF = 0\%) on DocRED with LoRA + beam-4, extending the zero-violation result from SciERC to the high-$\bar{\kappa}$ regime.
187-Qwen3-8B achieves DR=0\% with near-zero CF (0.01\%); R-F1 is preserved ($\pm$0.06\,pp).
188-Combined with the sampling robustness results (Appendix~\ref{app:sampling}), these findings confirm that OntoCoDec's constraint enforcement is compatible with greedy, sampling, and beam search decoding without modification to the core constraint logic.
189-
190-\paragraph{Latency overhead.}
191:Table~\ref{tab:beam-latency} reports wall-clock latency for greedy and beam search ($k{=}4$) under LoRA fine-tuning.
192-
193-\begin{table}[h]
194-\centering
195-\small
196-\begin{tabular}{@{}lrr@{}}
--
202-Beam-4 unconstrained   & 3.446 & 1.32$\times$ \\
203-Beam-4 constrained (S1)& 4.013 & 1.54$\times$ \\
204-\bottomrule
205-\end{tabular}
206-\caption{Latency per document (SciERC, 551 docs, Qwen3-8B LoRA FT, RTX PRO 6000 Blackwell). Overhead relative to greedy unconstrained.}
207:\label{tab:beam-latency}
208-\end{table}
209-
210-Beam search itself adds 32\% latency (4 beams); constraint overhead increases from 10\% (greedy) to 16.5\% (beam) because each beam independently maintains grammar and semantic state.
211-The total 1.54$\times$ overhead is acceptable for offline batch IE; \texttt{early\_stopping} limits additional compute to partial-sequence exploration.
212-
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CA4Q1cfQkVV53LnHsJprUE",
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "4c722054-4485-4cf8-8bd9-93675085d15b"
}
```

</details>

---

### System

_source line 88_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "afa4f506883d7ac8a",
  "tool_use_id": "toolu_01CA4Q1cfQkVV53LnHsJprUE",
  "description": "Searching for 2\\.43",
  "usage": {
    "total_tokens": 22293,
    "tool_uses": 10,
    "duration_ms": 10820
  },
  "last_tool_name": "Grep",
  "uuid": "0231ecf8-3e8e-4a27-b0e0-1305200848e2",
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d"
}
```

---

### Tool call

_source line 89_

<details open><summary>🔧 Tool call — Grep · `toolu_01T6QYyQHHtjCzwXZdz8LsNq`</summary>

```json
{
  "pattern": "2\\.43",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex",
  "output_mode": "content",
  "context": 4
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CA4Q1cfQkVV53LnHsJprUE",
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "5791bdde-4b33-42c0-b6b8-72e5dcbc4dc4",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LrmDL3aT6nKfbTaAu67pzM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 995,
      "cache_read_input_tokens": 21269,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 995,
        "ephemeral_1h_input_tokens": 0
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

_source line 90 · 2026-05-22T04:12:37.864Z_

<details><summary>↩ Tool result · `toolu_01T6QYyQHHtjCzwXZdz8LsNq`</summary>

```text
1-% Runtime overhead (inline paragraph, no subsection header to save space)
2-
3-\paragraph{Runtime overhead.}
4-\label{sec:runtime}
5:S1 overhead is $+$13.1\% on SciERC and $+$2.43\% on DocRED (amortized over longer sequences); under LoRA, $+$10.0\% with 37\% lower absolute latency.
6-Constraint compilation is one-time $<$0.5\,s; scaling benchmarks confirm constant overhead (2--3\%) up to 200 entity types and 1{,}000 relations (Appendix~\ref{app:scalability}).
7-
8-\paragraph{Beam search compatibility.}
9-\label{sec:beam-results}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CA4Q1cfQkVV53LnHsJprUE",
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "c32cf2ef-5c85-4f79-b357-9eb868004b4a"
}
```

</details>

---

### System

_source line 91_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "afa4f506883d7ac8a",
  "tool_use_id": "toolu_01CA4Q1cfQkVV53LnHsJprUE",
  "description": "Reading artifacts/_project/paper/section5_runtime.tex",
  "usage": {
    "total_tokens": 25277,
    "tool_uses": 11,
    "duration_ms": 13618
  },
  "last_tool_name": "Read",
  "uuid": "4630ea05-7317-4f92-a46a-5e200b8168a7",
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d"
}
```

---

### Tool call

_source line 92_

<details open><summary>🔧 Tool call — Read · `toolu_01D7w2o83iLrZu3Fg1QPidZQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CA4Q1cfQkVV53LnHsJprUE",
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "1613df8f-ce38-48cb-a127-7b961c136f81",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01YYxh2bpxoDgYXPiTdnb6hQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2982,
      "cache_read_input_tokens": 22264,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2982,
        "ephemeral_1h_input_tokens": 0
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

_source line 93 · 2026-05-22T04:12:40.649Z_

<details><summary>↩ Tool result · `toolu_01D7w2o83iLrZu3Fg1QPidZQ`</summary>

```text
1	% Runtime overhead (inline paragraph, no subsection header to save space)
2	
3	\paragraph{Runtime overhead.}
4	\label{sec:runtime}
5	S1 overhead is $+$13.1\% on SciERC and $+$2.43\% on DocRED (amortized over longer sequences); under LoRA, $+$10.0\% with 37\% lower absolute latency.
6	Constraint compilation is one-time $<$0.5\,s; scaling benchmarks confirm constant overhead (2--3\%) up to 200 entity types and 1{,}000 relations (Appendix~\ref{app:scalability}).
7	
8	\paragraph{Beam search compatibility.}
9	\label{sec:beam-results}
10	Beam search ($k{=}4$)~\cite{anderson2017guided} explores paths satisfying both layers jointly.
11	With LoRA, beam S1 eliminates all four violation types on SciERC (R-F1 44--47); zero-shot beam achieves DR${=}$0\% on both datasets (998-doc DocRED; CF response is model-dependent; Appendix~\ref{app:beam-search}).
12	Total latency: 1.54$\times$ (beam 1.32$\times$ $+$ constraint 1.17$\times$; Table~\ref{tab:beam-latency}).
13	
14	% exp_ids: r16_70b_scierc_zs_s1, 70b_lora_scierc, 70b_lora_docred_200
15	\paragraph{70B evaluation.}
16	\label{sec:70b-results}
17	On Llama-3.3-70B-Instruct (AWQ INT4), zero-shot S1 eliminates DR on SciERC (6.41\%\,$\to$\,0\%; R-F1 11.24, $+$0.09\,pp) with CF 3.50\% (from 0\% unconstrained).
18	% TODO: 待 70B LoRA 结果回填（SciERC 551 docs, DocRED 200-doc subset）
19	LoRA fine-tuning confirms scale-independent composability: SciERC DR XX.XX\%\,$\to$\,XX.XX\% (R-F1 XX.XX); DocRED (200-document subset) DR XX.XX\%\,$\to$\,XX.XX\% (R-F1 XX.XX); CF drops to XX.XX--XX.XX\%, consistent with the 8B pattern (9.90\%\,$\to$\,1.18\%; \S\ref{sec:composability}).
20	
21	% exp_ids: trie_qwen_ft_scierc, trie_qwen_zs_scierc, trie_llama_ft_scierc, trie_llama_zs_scierc
22	\paragraph{Comparison with grammar-constrained approaches.}
23	\label{sec:constrained-baselines}
24	Our grammar-only ablation (Table~\ref{tab:scierc-ablation}, row~2) implements the same class of constraints---vocabulary membership via context-free grammars---as GCD~\cite{geng2023gcd} and the grammar component of BoostCD~\cite{boostcd2025}, achieving RV/ET$\to$0\% but only 24\% DR reduction vs.\ Full S1's 94\%.
25	Without JSON structural enforcement, trie-only vocabulary constraints (GCD-equivalent) are counterproductive: DR rises to 15--96\% (vs.\ 1--15\% unconstrained) because models omit type fields or produce malformed JSON without grammar-level structure (Appendix~\ref{app:trie-baseline}), confirming both layers are necessary.
26	BoostCD's boosting of constrained and unconstrained decoding is complementary and potentially integrable with OntoCoDec's semantic layer.
27	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CA4Q1cfQkVV53LnHsJprUE",
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "363f2545-33ac-44e2-be87-eee77f13b3b5"
}
```

</details>

---

### System

_source line 94_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "afa4f506883d7ac8a",
  "tool_use_id": "toolu_01CA4Q1cfQkVV53LnHsJprUE",
  "status": "completed",
  "output_file": "",
  "summary": "Find ablation table and composability data",
  "usage": {
    "total_tokens": 26438,
    "tool_uses": 11,
    "duration_ms": 19792
  },
  "uuid": "5a0d060d-2001-430e-b74d-ab929709b67c",
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d"
}
```

---

### Tool result

_source line 95 · 2026-05-22T04:12:46.816Z_

<details><summary>↩ Tool result · `toolu_01CA4Q1cfQkVV53LnHsJprUE`</summary>

```text
Perfect! I have found all the requested files and content. Here's my report:

## Summary of Findings

**1. Ablation Table File**
- **File path:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex`
- **Label:** `\label{tab:scierc-ablation}` (line 65)
- **Relevant content:** Table definition begins at line 15, with caption at line 57: "Five-way ablation on SciERC (551 docs, Qwen3-8B, zero-shot)"

**2. Composability Section**
- **File path:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex`
- **Section reference:** `\S\ref{sec:composability}` (line 19)
- **Values mentioned:** "9.90%→1.18%" (line 19) - described as the 8B pattern showing CF drops in composability testing
- **Relevant line 19:** "LoRA fine-tuning confirms scale-independent composability... CF drops to XX.XX--XX.XX%, consistent with the 8B pattern (9.90%\,$\to$\,1.18\%; \S\ref{sec:composability})."

**3. Beam Latency Table**
- **File path:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex`
- **Label:** `\label{tab:beam-latency}` (line 207)
- **Reference in runtime section:** Line 12 mentions "Table~\ref{tab:beam-latency}"

**4. File Mentioning "2.43%"**
- **File path:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex`
- **Content location:** Line 5
- **Exact text:** "S1 overhead is $+$13.1\% on SciERC and $+$2.43\% on DocRED (amortized over longer sequences)"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "fc11c53b-3ebe-4281-8842-0373e7db4750",
  "tool_use_result": {
    "status": "completed",
    "prompt": "In the directory /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/, find:\n1. The ablation table file (likely table with \"ablation\" in filename or containing \\label{tab:scierc-ablation})\n2. Any file containing the composability section (section ref sec:composability or mentions \"9.90\" and \"1.18\")\n3. The beam latency table (containing \\label{tab:beam-latency})\n4. Any file mentioning \"2.43\" as a latency/overhead percentage\n\nSearch breadth: medium. Report the file paths and the relevant content lines.",
    "agentId": "afa4f506883d7ac8a",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! I have found all the requested files and content. Here's my report:\n\n## Summary of Findings\n\n**1. Ablation Table File**\n- **File path:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex`\n- **Label:** `\\label{tab:scierc-ablation}` (line 65)\n- **Relevant content:** Table definition begins at line 15, with caption at line 57: \"Five-way ablation on SciERC (551 docs, Qwen3-8B, zero-shot)\"\n\n**2. Composability Section**\n- **File path:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex`\n- **Section reference:** `\\S\\ref{sec:composability}` (line 19)\n- **Values mentioned:** \"9.90%→1.18%\" (line 19) - described as the 8B pattern showing CF drops in composability testing\n- **Relevant line 19:** \"LoRA fine-tuning confirms scale-independent composability... CF drops to XX.XX--XX.XX%, consistent with the 8B pattern (9.90%\\,$\\to$\\,1.18\\%; \\S\\ref{sec:composability}).\"\n\n**3. Beam Latency Table**\n- **File path:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex`\n- **Label:** `\\label{tab:beam-latency}` (line 207)\n- **Reference in runtime section:** Line 12 mentions \"Table~\\ref{tab:beam-latency}\"\n\n**4. File Mentioning \"2.43%\"**\n- **File path:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex`\n- **Content location:** Line 5\n- **Exact text:** \"S1 overhead is $+$13.1\\% on SciERC and $+$2.43\\% on DocRED (amortized over longer sequences)\""
      }
    ],
    "totalDurationMs": 19793,
    "totalTokens": 26996,
    "totalToolUseCount": 11,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1161,
      "cache_read_input_tokens": 25246,
      "output_tokens": 584,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1161
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 584,
          "cache_read_input_tokens": 25246,
          "cache_creation_input_tokens": 1161,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1161,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 1,
      "searchCount": 9,
      "bashCount": 1,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
```

</details>

---

### Tool call

_source line 96_

<details open><summary>🔧 Tool call — Read · `toolu_01NLcZ6tB2hHRbYM2n5Cxe68`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
  "offset": 15,
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
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "586e4eeb-eb54-440d-b614-40b01b70d532",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hn4jtTRH84RTh68qkVQMD6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1089,
      "cache_read_input_tokens": 48036,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1089
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

_source line 97 · 2026-05-22T04:12:49.529Z_

<details><summary>↩ Tool result · `toolu_01NLcZ6tB2hHRbYM2n5Cxe68`</summary>

```text
15	\begin{table}[t]
16	\centering
17	\small
18	\setlength{\tabcolsep}{3.6pt}
19	\resizebox{\columnwidth}{!}{%
20	\begin{tabular}{@{}l rrrrrr rr@{}}
21	\toprule
22	& \multicolumn{6}{c}{\textbf{Violation Rates (\%)}}
23	& \multicolumn{2}{c}{\textbf{F1}} \\
24	\cmidrule(lr){2-7} \cmidrule(l){8-9}
25	\textbf{Mode}
26	  & DR\,$\downarrow$ & $\Delta$DR
27	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF & Tot.\,$\downarrow$
28	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
29	\midrule
30	Unconstrained
31	  & 15.37 & ---
32	  & 1.39  & 0.40
33	  & 0.08  & 15.45
34	  & 8.23  & 31.01 \\
35	Grammar
36	  & 14.84 & $\downarrow$3\%
37	  & \textbf{0} & \textbf{0}
38	  & 0.08  & 14.92
39	  & 8.23  & 30.98 \\
40	Semantic
41	  & 11.65 & $\downarrow$24\%
42	  & 1.51  & 0.40
43	  & 2.71  & 14.36
44	  & 8.15  & 31.01 \\
45	Full (S1)
46	  & \textbf{0.93} & $\downarrow$\textbf{94\%}
47	  & \textbf{0} & \textbf{0}
48	  & 9.90  & \textbf{10.83}
49	  & \textbf{8.36} & 30.98 \\
50	Full (S2)
51	  & 0.97  & $\downarrow$94\%
52	  & \textbf{0} & \textbf{0}
53	  & 8.03  & \textbf{9.00}
54	  & 8.03  & \textbf{31.90} \\
55	\bottomrule
56	\end{tabular}}%
57	\caption{Five-way ablation on SciERC (551 docs, Qwen3-8B, zero-shot).
58	$\Delta$DR: relative change vs.\ unconstrained.
59	Tot.\ = DR + CF (total type-violation burden).
60	Best per column in \textbf{bold} (CF excluded; Tot.\ included).
61	F1 $\times$100. Bootstrap: 10{,}000 iterations.
62	CF: same entity assigned conflicting types across triples.
63	S1 = single-pass (\S\ref{sec:strategies}), S2 = two-pass (\S\ref{sec:s2}).
64	Grammar-only represents the ceiling of grammar-constrained decoding~\cite{geng2023gcd}: vocabulary membership is enforced but cross-field semantic constraints are not.}
65	\label{tab:scierc-ablation}
66	\end{table}
67	
68	% ──────────────────────────────────────────
69	%  (a) Core result
70	% ──────────────────────────────────────────
71	\paragraph{Zero-shot diagnostic.}
72	% phase2_scierc_unconstrained: DR=0.1537; phase2_scierc_full_s1: DR=0.0093
73	% phase2_scierc_unconstrained: R-F1=0.0823; phase2_scierc_full_s1: R-F1=0.0836
74	% bootstrap: delta=+0.13pp, CI=[-0.24,+0.58], p=0.5824
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "27b06105-3cfa-48e4-8157-38e91c2956fa",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
      "content": "\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3.6pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}l rrrrrr rr@{}}\n\\toprule\n& \\multicolumn{6}{c}{\\textbf{Violation Rates (\\%)}}\n& \\multicolumn{2}{c}{\\textbf{F1}} \\\\\n\\cmidrule(lr){2-7} \\cmidrule(l){8-9}\n\\textbf{Mode}\n  & DR\\,$\\downarrow$ & $\\Delta$DR\n  & RV\\,$\\downarrow$ & ET\\,$\\downarrow$ & CF & Tot.\\,$\\downarrow$\n  & Rel.\\,$\\uparrow$ & Ent.\\,$\\uparrow$ \\\\\n\\midrule\nUnconstrained\n  & 15.37 & ---\n  & 1.39  & 0.40\n  & 0.08  & 15.45\n  & 8.23  & 31.01 \\\\\nGrammar\n  & 14.84 & $\\downarrow$3\\%\n  & \\textbf{0} & \\textbf{0}\n  & 0.08  & 14.92\n  & 8.23  & 30.98 \\\\\nSemantic\n  & 11.65 & $\\downarrow$24\\%\n  & 1.51  & 0.40\n  & 2.71  & 14.36\n  & 8.15  & 31.01 \\\\\nFull (S1)\n  & \\textbf{0.93} & $\\downarrow$\\textbf{94\\%}\n  & \\textbf{0} & \\textbf{0}\n  & 9.90  & \\textbf{10.83}\n  & \\textbf{8.36} & 30.98 \\\\\nFull (S2)\n  & 0.97  & $\\downarrow$94\\%\n  & \\textbf{0} & \\textbf{0}\n  & 8.03  & \\textbf{9.00}\n  & 8.03  & \\textbf{31.90} \\\\\n\\bottomrule\n\\end{tabular}}%\n\\caption{Five-way ablation on SciERC (551 docs, Qwen3-8B, zero-shot).\n$\\Delta$DR: relative change vs.\\ unconstrained.\nTot.\\ = DR + CF (total type-violation burden).\nBest per column in \\textbf{bold} (CF excluded; Tot.\\ included).\nF1 $\\times$100. Bootstrap: 10{,}000 iterations.\nCF: same entity assigned conflicting types across triples.\nS1 = single-pass (\\S\\ref{sec:strategies}), S2 = two-pass (\\S\\ref{sec:s2}).\nGrammar-only represents the ceiling of grammar-constrained decoding~\\cite{geng2023gcd}: vocabulary membership is enforced but cross-field semantic constraints are not.}\n\\label{tab:scierc-ablation}\n\\end{table}\n\n% ──────────────────────────────────────────\n%  (a) Core result\n% ──────────────────────────────────────────\n\\paragraph{Zero-shot diagnostic.}\n% phase2_scierc_unconstrained: DR=0.1537; phase2_scierc_full_s1: DR=0.0093\n% phase2_scierc_unconstrained: R-F1=0.0823; phase2_scierc_full_s1: R-F1=0.0836\n% bootstrap: delta=+0.13pp, CI=[-0.24,+0.58], p=0.5824",
      "numLines": 60,
      "startLine": 15,
      "totalLines": 152
    }
  }
}
```

</details>

---

### Tool call

_source line 98_

<details open><summary>🔧 Tool call — Read · `toolu_013Q4KKzgovnAUtAUuCUP32D`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex",
  "offset": 195,
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
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "fbbd66fb-5d0e-402e-a24b-9927db8111fa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hn4jtTRH84RTh68qkVQMD6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1089,
      "cache_read_input_tokens": 48036,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1089
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

_source line 99 · 2026-05-22T04:12:50.145Z_

<details><summary>↩ Tool result · `toolu_013Q4KKzgovnAUtAUuCUP32D`</summary>

```text
195	\small
196	\begin{tabular}{@{}lrr@{}}
197	\toprule
198	\textbf{Condition} & \textbf{s/doc} & \textbf{Overhead} \\
199	\midrule
200	Greedy unconstrained   & 2.612 & 1.00$\times$ \\
201	Greedy constrained (S1)& 2.873 & 1.10$\times$ \\
202	Beam-4 unconstrained   & 3.446 & 1.32$\times$ \\
203	Beam-4 constrained (S1)& 4.013 & 1.54$\times$ \\
204	\bottomrule
205	\end{tabular}
206	\caption{Latency per document (SciERC, 551 docs, Qwen3-8B LoRA FT, RTX PRO 6000 Blackwell). Overhead relative to greedy unconstrained.}
207	\label{tab:beam-latency}
208	\end{table}
209	
210	Beam search itself adds 32\% latency (4 beams); constraint overhead increases from 10\% (greedy) to 16.5\% (beam) because each beam independently maintains grammar and semantic state.
211	The total 1.54$\times$ overhead is acceptable for offline batch IE; \texttt{early\_stopping} limits additional compute to partial-sequence exploration.
212	
213	We also explored a type-consensus constraint that forces identical entity types across all relations within a document.
214	However, CF violations occur precisely where the consensus type conflicts with domain-range constraints, creating a fundamental CF$\leftrightarrow$DR trade-off.
215	With DR-aware enforcement (skipping consensus when it would violate domain-range), the layer becomes a no-op (100\% skip rate on 551 SciERC documents and 50 DocRED documents).
216	This confirms that beam search resolves the CF$\leftrightarrow$DR tension through a fundamentally different mechanism: token-level exploration of paths satisfying both constraints simultaneously.
217	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "ba13a1f1-0e28-4bd5-95f3-076242c00bc9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex",
      "content": "\\small\n\\begin{tabular}{@{}lrr@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{s/doc} & \\textbf{Overhead} \\\\\n\\midrule\nGreedy unconstrained   & 2.612 & 1.00$\\times$ \\\\\nGreedy constrained (S1)& 2.873 & 1.10$\\times$ \\\\\nBeam-4 unconstrained   & 3.446 & 1.32$\\times$ \\\\\nBeam-4 constrained (S1)& 4.013 & 1.54$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Latency per document (SciERC, 551 docs, Qwen3-8B LoRA FT, RTX PRO 6000 Blackwell). Overhead relative to greedy unconstrained.}\n\\label{tab:beam-latency}\n\\end{table}\n\nBeam search itself adds 32\\% latency (4 beams); constraint overhead increases from 10\\% (greedy) to 16.5\\% (beam) because each beam independently maintains grammar and semantic state.\nThe total 1.54$\\times$ overhead is acceptable for offline batch IE; \\texttt{early\\_stopping} limits additional compute to partial-sequence exploration.\n\nWe also explored a type-consensus constraint that forces identical entity types across all relations within a document.\nHowever, CF violations occur precisely where the consensus type conflicts with domain-range constraints, creating a fundamental CF$\\leftrightarrow$DR trade-off.\nWith DR-aware enforcement (skipping consensus when it would violate domain-range), the layer becomes a no-op (100\\% skip rate on 551 SciERC documents and 50 DocRED documents).\nThis confirms that beam search resolves the CF$\\leftrightarrow$DR tension through a fundamentally different mechanism: token-level exploration of paths satisfying both constraints simultaneously.\n",
      "numLines": 23,
      "startLine": 195,
      "totalLines": 217
    }
  }
}
```

</details>

---

### Assistant

_source line 100_

<details><summary>Logged reasoning block</summary>

```text
Now I have most of the data. Let me also find the composability section to verify the 9.90% → 1.18% CF claim, and understand the DocRED latency 2.43% source.

Let me look for the composability section.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "48483120-fdae-495b-a02d-f1362016c673",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01373ZCwEbrU7GE5d3CLRMWs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1922,
      "cache_read_input_tokens": 49125,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1922
      },
      "output_tokens": 10,
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

_source line 101_

<details open><summary>🔧 Tool call — Grep · `toolu_017bQEmUkQHiYUz9xVVssYkW`</summary>

```json
{
  "pattern": "sec:composability|composability",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "3b5a5546-c63f-4494-8958-7f39c9049efe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01373ZCwEbrU7GE5d3CLRMWs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1922,
      "cache_read_input_tokens": 49125,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1922
      },
      "output_tokens": 10,
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

_source line 102 · 2026-05-22T04:12:56.040Z_

<details><summary>↩ Tool result · `toolu_017bQEmUkQHiYUz9xVVssYkW`</summary>

```text
artifacts/_project/paper/main.tex:83:Zero-shot evaluation covers three 8B-class and one 70B-class model; fine-tuning composability is validated on 8B-class (two models, full datasets) and 70B-class models (one model; SciERC full, DocRED 200-document subset).
artifacts/_project/paper/main.tex:86:WikiEvents fine-tuning composability is preliminary (20-document test set, the full official split).
artifacts/_project/paper/main.tex:95:Fine-tuning composability was validated exclusively with LoRA; full fine-tuning with an untuned learning rate underperforms LoRA (R-F1 37.89 vs.\ 43.77 on SciERC) but confirms that constraints remain effective (DR 2.74\%\,$\to$\,0\%; Appendix~\ref{app:full-ft}); other fine-tuning methods may exhibit different constraint interaction patterns and warrant further investigation.
artifacts/_project/paper/section5_crossmodel_draft.tex:58:CF direction depends on calibration: S1 introduces CF for calibrated models (up to 12.02\%; \S\ref{sec:discussion}) but reduces it for Mistral (56.87\%\,$\to$\,1.27\%); fine-tuning resolves both (\S\ref{sec:composability}).
artifacts/_project/paper/appendix_discussion.tex:113:(i)~\emph{Reduce the baseline conflict rate.} Composing OntoCoDec with LoRA fine-tuning on SciERC reduces CF by 88\% relative to the zero-shot setting (9.90\%\,$\to$\,1.18\%; Table~\ref{tab:composability}), because the fine-tuned model's per-slot type predictions agree more often with the entity registry, so the per-relation mask and the registry intersect more frequently.
artifacts/_project/paper/appendix_discussion.tex:160:Even after LoRA fine-tuning, residual DR of 1--2\% persists on tight-constraint relations (Table~\ref{tab:composability}); constraints remain necessary at deployment-grade quality.
artifacts/_project/paper/appendix_discussion.tex:163:The contribution of this work is the constraint enforcement method itself; the zero-shot setting stress-tests constraint robustness under maximum model uncertainty, while composability with fine-tuning (\S\ref{sec:composability}) validates practical deployment value.
artifacts/_project/paper/section5_docred_draft.tex:71:Residual DR (10.21\% vs.\ 0.93\% on SciERC) reflects high $\bar{\kappa}$ (0.842) and \textsc{Generic}$\leftrightarrow$X ambiguity; fine-tuning narrows DR to $\leq$\,0.09\% (Table~\ref{tab:composability}), with the 36 residual violations decomposing into entity type errors (39\%), schema coverage gaps (33\%), incorrect relation selection (17\%), and direction reversal (11\%; Appendix~\ref{app:residual-dr-analysis}).
artifacts/_project/paper/section5_runtime.tex:19:LoRA fine-tuning confirms scale-independent composability: SciERC DR XX.XX\%\,$\to$\,XX.XX\% (R-F1 XX.XX); DocRED (200-document subset) DR XX.XX\%\,$\to$\,XX.XX\% (R-F1 XX.XX); CF drops to XX.XX--XX.XX\%, consistent with the 8B pattern (9.90\%\,$\to$\,1.18\%; \S\ref{sec:composability}).
artifacts/_project/paper/section5_scierc_draft.tex:103:\label{sec:composability}
artifacts/_project/paper/section5_scierc_draft.tex:104:Fine-tuning alone reduces DR to 1--2\% but leaves residual violations (Table~\ref{tab:composability}); adding S1 yields DR\,$\leq$\,0.09\% with R-F1 within $\pm$0.6\,pp (removed triples are 97.6--100\% false positives).
artifacts/_project/paper/section5_scierc_draft.tex:138:\caption{Fine-tuning composability: LoRA $\times$ unconstrained vs.\ S1 on SciERC (551 docs) and DocRED (998 dev docs).
artifacts/_project/paper/section5_scierc_draft.tex:142:\label{tab:composability}
artifacts/_project/paper/section4_composition_draft.tex:31:Type signatures are non-rectangular (0/7 SciERC, 23/96 DocRED rectangular); independent enforcement is a sound over-approximation admitting 33--37\% spurious pairs; fine-tuning eliminates all residual DR (Table~\ref{tab:composability}).
artifacts/_project/paper/section3_violation_landscape.tex:7:We evaluate OntoCoDec in two deployment configurations: LoRA + greedy S1 (\S\ref{sec:composability}), near-eliminating DR (DR\,$\leq$\,0.09\%) with minimal overhead; and LoRA + beam S1 (\S\ref{sec:beam-results}), achieving zero total violations on SciERC under favorable conditions (1.54$\times$ latency).
artifacts/_project/paper/section3_violation_landscape.tex:16:Primary model: Qwen3-8B~\cite{qwen2025qwen3}, zero-shot greedy decoding; cross-model validation in \S\ref{sec:cross-model}, composability with fine-tuning in \S\ref{sec:composability}.
artifacts/_project/paper/appendix_beam_search.tex:161:Table~\ref{tab:beam-docred-lora} reports LoRA + beam-4 results on the full DocRED dev set (998 documents), extending the fine-tuning composability evaluation from SciERC to the higher-$\bar{\kappa}$ regime.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "a596ec41-11c7-44ae-9447-ab5ce9a27fd5",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/_project/paper/main.tex:83:Zero-shot evaluation covers three 8B-class and one 70B-class model; fine-tuning composability is validated on 8B-class (two models, full datasets) and 70B-class models (one model; SciERC full, DocRED 200-document subset).\nartifacts/_project/paper/main.tex:86:WikiEvents fine-tuning composability is preliminary (20-document test set, the full official split).\nartifacts/_project/paper/main.tex:95:Fine-tuning composability was validated exclusively with LoRA; full fine-tuning with an untuned learning rate underperforms LoRA (R-F1 37.89 vs.\\ 43.77 on SciERC) but confirms that constraints remain effective (DR 2.74\\%\\,$\\to$\\,0\\%; Appendix~\\ref{app:full-ft}); other fine-tuning methods may exhibit different constraint interaction patterns and warrant further investigation.\nartifacts/_project/paper/section5_crossmodel_draft.tex:58:CF direction depends on calibration: S1 introduces CF for calibrated models (up to 12.02\\%; \\S\\ref{sec:discussion}) but reduces it for Mistral (56.87\\%\\,$\\to$\\,1.27\\%); fine-tuning resolves both (\\S\\ref{sec:composability}).\nartifacts/_project/paper/appendix_discussion.tex:113:(i)~\\emph{Reduce the baseline conflict rate.} Composing OntoCoDec with LoRA fine-tuning on SciERC reduces CF by 88\\% relative to the zero-shot setting (9.90\\%\\,$\\to$\\,1.18\\%; Table~\\ref{tab:composability}), because the fine-tuned model's per-slot type predictions agree more often with the entity registry, so the per-relation mask and the registry intersect more frequently.\nartifacts/_project/paper/appendix_discussion.tex:160:Even after LoRA fine-tuning, residual DR of 1--2\\% persists on tight-constraint relations (Table~\\ref{tab:composability}); constraints remain necessary at deployment-grade quality.\nartifacts/_project/paper/appendix_discussion.tex:163:The contribution of this work is the constraint enforcement method itself; the zero-shot setting stress-tests constraint robustness under maximum model uncertainty, while composability with fine-tuning (\\S\\ref{sec:composability}) validates practical deployment value.\nartifacts/_project/paper/section5_docred_draft.tex:71:Residual DR (10.21\\% vs.\\ 0.93\\% on SciERC) reflects high $\\bar{\\kappa}$ (0.842) and \\textsc{Generic}$\\leftrightarrow$X ambiguity; fine-tuning narrows DR to $\\leq$\\,0.09\\% (Table~\\ref{tab:composability}), with the 36 residual violations decomposing into entity type errors (39\\%), schema coverage gaps (33\\%), incorrect relation selection (17\\%), and direction reversal (11\\%; Appendix~\\ref{app:residual-dr-analysis}).\nartifacts/_project/paper/section5_runtime.tex:19:LoRA fine-tuning confirms scale-independent composability: SciERC DR XX.XX\\%\\,$\\to$\\,XX.XX\\% (R-F1 XX.XX); DocRED (200-document subset) DR XX.XX\\%\\,$\\to$\\,XX.XX\\% (R-F1 XX.XX); CF drops to XX.XX--XX.XX\\%, consistent with the 8B pattern (9.90\\%\\,$\\to$\\,1.18\\%; \\S\\ref{sec:composability}).\nartifacts/_project/paper/section5_scierc_draft.tex:103:\\label{sec:composability}\nartifacts/_project/paper/section5_scierc_draft.tex:104:Fine-tuning alone reduces DR to 1--2\\% but leaves residual violations (Table~\\ref{tab:composability}); adding S1 yields DR\\,$\\leq$\\,0.09\\% with R-F1 within $\\pm$0.6\\,pp (removed triples are 97.6--100\\% false positives).\nartifacts/_project/paper/section5_scierc_draft.tex:138:\\caption{Fine-tuning composability: LoRA $\\times$ unconstrained vs.\\ S1 on SciERC (551 docs) and DocRED (998 dev docs).\nartifacts/_project/paper/section5_scierc_draft.tex:142:\\label{tab:composability}\nartifacts/_project/paper/section4_composition_draft.tex:31:Type signatures are non-rectangular (0/7 SciERC, 23/96 DocRED rectangular); independent enforcement is a sound over-approximation admitting 33--37\\% spurious pairs; fine-tuning eliminates all residual DR (Table~\\ref{tab:composability}).\nartifacts/_project/paper/section3_violation_landscape.tex:7:We evaluate OntoCoDec in two deployment configurations: LoRA + greedy S1 (\\S\\ref{sec:composability}), near-eliminating DR (DR\\,$\\leq$\\,0.09\\%) with minimal overhead; and LoRA + beam S1 (\\S\\ref{sec:beam-results}), achieving zero total violations on SciERC under favorable conditions (1.54$\\times$ latency).\nartifacts/_project/paper/section3_violation_landscape.tex:16:Primary model: Qwen3-8B~\\cite{qwen2025qwen3}, zero-shot greedy decoding; cross-model validation in \\S\\ref{sec:cross-model}, composability with fine-tuning in \\S\\ref{sec:composability}.\nartifacts/_project/paper/appendix_beam_search.tex:161:Table~\\ref{tab:beam-docred-lora} reports LoRA + beam-4 results on the full DocRED dev set (998 documents), extending the fine-tuning composability evaluation from SciERC to the higher-$\\bar{\\kappa}$ regime.",
    "numLines": 17
  }
}
```

</details>

---

### Tool call

_source line 103_

<details open><summary>🔧 Tool call — Read · `toolu_015JZHBEqHLQCunAzHkbqoSg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
  "offset": 103,
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "63f36524-22e4-4b3f-bae9-a8a138da799e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JSA6hdPCR8K1BXQcTArTaE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1738,
      "cache_read_input_tokens": 51047,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1738
      },
      "output_tokens": 36,
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

_source line 104 · 2026-05-22T04:13:03.829Z_

<details><summary>↩ Tool result · `toolu_015JZHBEqHLQCunAzHkbqoSg`</summary>

```text
103	\label{sec:composability}
104	Fine-tuning alone reduces DR to 1--2\% but leaves residual violations (Table~\ref{tab:composability}); adding S1 yields DR\,$\leq$\,0.09\% with R-F1 within $\pm$0.6\,pp (removed triples are 97.6--100\% false positives).
105	CF drops from $+$9.82\,pp (zero-shot) to $+$1.18\,pp (fine-tuned; Appendix~\ref{app:cf-distribution}); beam ($k{=}4$) with LoRA eliminates all four violation types on SciERC (R-F1 43.60, 46.18; \S\ref{sec:beam-results}).
106	
107	\begin{table}[t]
108	\centering
109	\small
110	\setlength{\tabcolsep}{3pt}
111	\resizebox{\columnwidth}{!}{%
112	\begin{tabular}{@{}lll rrrr r@{}}
113	\toprule
114	\textbf{Model} & \textbf{Dataset} & \textbf{Mode}
115	  & \textbf{DR\,$\downarrow$} & \textbf{CF}
116	  & \textbf{R-F1\,$\uparrow$} & \textbf{E-F1\,$\uparrow$}
117	  & \textbf{$\Delta$DR} \\
118	\midrule
119	\multirow{4}{*}{Qwen3-8B}
120	  & \multirow{2}{*}{SciERC}
121	    & Unconstr.\ &  1.95 & 0    & 43.86 & 67.05 & --- \\
122	  & & Full S1    & \textbf{0} & 1.18 & 43.77 & 67.05 & $\downarrow$100\% \\
123	\cmidrule(l){2-8}
124	  & \multirow{2}{*}{DocRED}
125	    & Unconstr.\ &  0.56 & 0.08 & 40.89 & 82.35 & --- \\
126	  & & Full S1    & \textbf{0.00} & 0.22 & 40.79 & 81.87 & $\downarrow$100\% \\
127	\midrule
128	\multirow{4}{*}{\shortstack[l]{Llama\\3.1-8B}}
129	  & \multirow{2}{*}{SciERC}
130	    & Unconstr.\ &  1.11 & 0    & 45.45 & 67.76 & --- \\
131	  & & Full S1    &  0.09 & 0.46 & 45.47 & 67.76 & $\downarrow$92\% \\
132	\cmidrule(l){2-8}
133	  & \multirow{2}{*}{DocRED}
134	    & Unconstr.\ &  0.49 & 0.08 & 44.55 & 84.77 & --- \\
135	  & & Full S1    &  0.00 & 0.26 & 44.70 & 84.71 & $\downarrow$100\% \\
136	\bottomrule
137	\end{tabular}}%
138	\caption{Fine-tuning composability: LoRA $\times$ unconstrained vs.\ S1 on SciERC (551 docs) and DocRED (998 dev docs).
139	F1\,$\times$100.
140	Paired bootstrap (B${=}$10{,}000, document-level): $\Delta$R-F1 between constrained and unconstrained is not significant ($p{>}0.05$; largest $|\Delta|{=}0.31$\,pp, $p{=}0.056$), while DR reduction is significant in all settings ($p{<}0.001$).
141	E-F1 includes parse-failure documents (Qwen PF: 7--8\%; Llama PF: 2--3\%).}
142	\label{tab:composability}
143	\end{table}
144	
145	% ──────────────────────────────────────────
146	%  (f) Downstream impact of DR elimination
147	%  exp_ids: task_e_lucky_violation_analysis
148	% ──────────────────────────────────────────
149	\paragraph{Downstream impact.}
150	\label{sec:downstream-impact}
151	Among constraint-removed triples, only 0.49\% match gold labels on average (``lucky violations''), confirming $<$0.5\% recall cost; on Llama SciERC all five are recovered via legal type paths (zero churn; Appendix~\ref{app:lucky-violations}).
152	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "c347980e-2b9f-4ec8-b3e9-0286f451b144",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
      "content": "\\label{sec:composability}\nFine-tuning alone reduces DR to 1--2\\% but leaves residual violations (Table~\\ref{tab:composability}); adding S1 yields DR\\,$\\leq$\\,0.09\\% with R-F1 within $\\pm$0.6\\,pp (removed triples are 97.6--100\\% false positives).\nCF drops from $+$9.82\\,pp (zero-shot) to $+$1.18\\,pp (fine-tuned; Appendix~\\ref{app:cf-distribution}); beam ($k{=}4$) with LoRA eliminates all four violation types on SciERC (R-F1 43.60, 46.18; \\S\\ref{sec:beam-results}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lll rrrr r@{}}\n\\toprule\n\\textbf{Model} & \\textbf{Dataset} & \\textbf{Mode}\n  & \\textbf{DR\\,$\\downarrow$} & \\textbf{CF}\n  & \\textbf{R-F1\\,$\\uparrow$} & \\textbf{E-F1\\,$\\uparrow$}\n  & \\textbf{$\\Delta$DR} \\\\\n\\midrule\n\\multirow{4}{*}{Qwen3-8B}\n  & \\multirow{2}{*}{SciERC}\n    & Unconstr.\\ &  1.95 & 0    & 43.86 & 67.05 & --- \\\\\n  & & Full S1    & \\textbf{0} & 1.18 & 43.77 & 67.05 & $\\downarrow$100\\% \\\\\n\\cmidrule(l){2-8}\n  & \\multirow{2}{*}{DocRED}\n    & Unconstr.\\ &  0.56 & 0.08 & 40.89 & 82.35 & --- \\\\\n  & & Full S1    & \\textbf{0.00} & 0.22 & 40.79 & 81.87 & $\\downarrow$100\\% \\\\\n\\midrule\n\\multirow{4}{*}{\\shortstack[l]{Llama\\\\3.1-8B}}\n  & \\multirow{2}{*}{SciERC}\n    & Unconstr.\\ &  1.11 & 0    & 45.45 & 67.76 & --- \\\\\n  & & Full S1    &  0.09 & 0.46 & 45.47 & 67.76 & $\\downarrow$92\\% \\\\\n\\cmidrule(l){2-8}\n  & \\multirow{2}{*}{DocRED}\n    & Unconstr.\\ &  0.49 & 0.08 & 44.55 & 84.77 & --- \\\\\n  & & Full S1    &  0.00 & 0.26 & 44.70 & 84.71 & $\\downarrow$100\\% \\\\\n\\bottomrule\n\\end{tabular}}%\n\\caption{Fine-tuning composability: LoRA $\\times$ unconstrained vs.\\ S1 on SciERC (551 docs) and DocRED (998 dev docs).\nF1\\,$\\times$100.\nPaired bootstrap (B${=}$10{,}000, document-level): $\\Delta$R-F1 between constrained and unconstrained is not significant ($p{>}0.05$; largest $|\\Delta|{=}0.31$\\,pp, $p{=}0.056$), while DR reduction is significant in all settings ($p{<}0.001$).\nE-F1 includes parse-failure documents (Qwen PF: 7--8\\%; Llama PF: 2--3\\%).}\n\\label{tab:composability}\n\\end{table}\n\n% ──────────────────────────────────────────\n%  (f) Downstream impact of DR elimination\n%  exp_ids: task_e_lucky_violation_analysis\n% ──────────────────────────────────────────\n\\paragraph{Downstream impact.}\n\\label{sec:downstream-impact}\nAmong constraint-removed triples, only 0.49\\% match gold labels on average (``lucky violations''), confirming $<$0.5\\% recall cost; on Llama SciERC all five are recovered via legal type paths (zero churn; Appendix~\\ref{app:lucky-violations}).\n",
      "numLines": 50,
      "startLine": 103,
      "totalLines": 152
    }
  }
}
```

</details>

---

### Assistant

_source line 105_

<details><summary>Logged reasoning block</summary>

```text
Now I have a much clearer picture. Let me also look for the DocRED latency data. The paper claims "+2.43% on DocRED". The p8b_docred_latency experiment failed. Let me check if there's an artifact file with DocRED latency data, or if it was computed outside the registry.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "103ea2ba-f4ba-4490-958d-7211984f4ba6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LZkcTmr8LJCbL98a9x4x4B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1433,
      "cache_read_input_tokens": 52785,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1433
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

_source line 106_

<details open><summary>🔧 Tool call — Grep · `toolu_01BN8UX5gtAZqp13axHetzDv`</summary>

```json
{
  "pattern": "2\\.43",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts",
  "output_mode": "content",
  "head_limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "6a9499f0-6866-4ec2-b928-c34de0c85ebd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LZkcTmr8LJCbL98a9x4x4B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1433,
      "cache_read_input_tokens": 52785,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1433
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

_source line 107 · 2026-05-22T04:13:10.900Z_

<details><summary>↩ Tool result · `toolu_01BN8UX5gtAZqp13axHetzDv`</summary>

```text
artifacts/_project/report/case_study_kappa_dr_dddc01.md:74:| P170 | creator | 37 | 12 | 32.43 | 8 | 0.778 |
artifacts/_project/report/case_study_kappa_dr.md:74:| P170 | creator | 37 | 12 | 32.43 | 8 | 0.778 |
artifacts/dream_reports/dream_20260514T205155/logs/review_median.log:30:[Omitted long matching line]
artifacts/_project/paper/appendix_reproducibility.tex:18:Full S1 constrained decoding adds $+$13.1\% wall-clock overhead on SciERC and $+$2.43\% on DocRED (Qwen3-8B, zero-shot greedy); under LoRA fine-tuning, overhead is $+$10.0\% on SciERC.
artifacts/_project/paper/appendix_discussion.tex:383:On DocRED (same configuration), unconstrained inference averages 19.34\,s/doc and Full S1 averages 19.81\,s/doc ($+$2.43\% overhead).
artifacts/_project/paper/section5_runtime.tex:5:S1 overhead is $+$13.1\% on SciERC and $+$2.43\% on DocRED (amortized over longer sequences); under LoRA, $+$10.0\% with 37\% lower absolute latency.
artifacts/70b_docred_unconstrained_analysis.md:33:- Precision: **12.43%**
artifacts/dream_reports/dream_20260518T162745/logs/review_worst.log:71:[Omitted long matching line]
artifacts/dream_reports/dream_20260518T162745/logs/review_worst.log:95:[Omitted long matching line]
artifacts/dream_reports/dream_20260518T162745/logs/review_worst.log:121:[Omitted long matching line]
artifacts/dream_reports/dream_20260518T162745/logs/review_worst.log:182:[Omitted long matching line]
artifacts/dream_reports/dream_20260518T162745/logs/review_worst.log:185:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "00566ba7-e059-4b9d-b7c5-64cafe5e3fa4",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/_project/report/case_study_kappa_dr_dddc01.md:74:| P170 | creator | 37 | 12 | 32.43 | 8 | 0.778 |\nartifacts/_project/report/case_study_kappa_dr.md:74:| P170 | creator | 37 | 12 | 32.43 | 8 | 0.778 |\nartifacts/dream_reports/dream_20260514T205155/logs/review_median.log:30:[Omitted long matching line]\nartifacts/_project/paper/appendix_reproducibility.tex:18:Full S1 constrained decoding adds $+$13.1\\% wall-clock overhead on SciERC and $+$2.43\\% on DocRED (Qwen3-8B, zero-shot greedy); under LoRA fine-tuning, overhead is $+$10.0\\% on SciERC.\nartifacts/_project/paper/appendix_discussion.tex:383:On DocRED (same configuration), unconstrained inference averages 19.34\\,s/doc and Full S1 averages 19.81\\,s/doc ($+$2.43\\% overhead).\nartifacts/_project/paper/section5_runtime.tex:5:S1 overhead is $+$13.1\\% on SciERC and $+$2.43\\% on DocRED (amortized over longer sequences); under LoRA, $+$10.0\\% with 37\\% lower absolute latency.\nartifacts/70b_docred_unconstrained_analysis.md:33:- Precision: **12.43%**\nartifacts/dream_reports/dream_20260518T162745/logs/review_worst.log:71:[Omitted long matching line]\nartifacts/dream_reports/dream_20260518T162745/logs/review_worst.log:95:[Omitted long matching line]\nartifacts/dream_reports/dream_20260518T162745/logs/review_worst.log:121:[Omitted long matching line]\nartifacts/dream_reports/dream_20260518T162745/logs/review_worst.log:182:[Omitted long matching line]\nartifacts/dream_reports/dream_20260518T162745/logs/review_worst.log:185:[Omitted long matching line]",
    "numLines": 12
  }
}
```

</details>

---

### Tool call

_source line 108_

<details open><summary>🔧 Tool call — Bash · `toolu_01T7RrSskdpaPQ2mteq9AwYM`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/06688fc2-d26c-40b0-8ebe-68d505b40c0d/tool-results/mcp-agent-ml-research-read_registry-1779422951081.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n\n# Search for docred latency with actual overhead data\nfor k in exps:\n    if 'docred' in k.lower() and 'latency' in k.lower():\n        print(f'=== {k} ===')\n        print(json.dumps(exps[k], indent=2)[:600])\n        print()\n\n# Also look for any p8 related DocRED experiments\nfor k in exps:\n    if k.startswith('p8') and 'docred' in k.lower():\n        print(f'=== {k} ===')\n        print(json.dumps(exps[k], indent=2)[:600])\n        print()\n\n# Search all experiments for 'docred' and overhead in text\nfor k in exps:\n    if 'docred' in k.lower():\n        text = json.dumps(exps[k])\n        if 'overhead' in text.lower() and 'percent' in text.lower() or '2.43' in text:\n            print(f'MATCH: {k}')\n            print(json.dumps(exps[k].get('metrics',{}), indent=2)[:300])\n\"",
  "description": "Find DocRED 2.43% overhead source"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "2494419d-24d1-4b17-9abb-9bd4337e361f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LZkcTmr8LJCbL98a9x4x4B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1433,
      "cache_read_input_tokens": 52785,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1433
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

_source line 109 · 2026-05-22T04:13:20.351Z_

<details><summary>↩ Tool result · `toolu_01T7RrSskdpaPQ2mteq9AwYM`</summary>

```text
=== p8b_docred_latency ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-18T15:14:28.888Z",
  "updated_at": "2026-05-18T17:48:57.349Z",
  "hypothesis": "OntoCoDec constrained decoding overhead on Qwen3-8B DocRED (200-doc subset) measured on same GPU as P8 SciERC will confirm moderate overhead (<2x), providing consistent timing data for paper",
  "parent": "p8_latency_overhead",
  "spec": {
    "command": "run_constrained_extraction.py unconstrained+full_s1 then analyze_latency.py",
    "server": "westd-21461",
    "data_path": "/root/autodl-tmp/schema_outputs/docred_timing_subset_200.json",
    "dat

=== p8b_docred_latency ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-18T15:14:28.888Z",
  "updated_at": "2026-05-18T17:48:57.349Z",
  "hypothesis": "OntoCoDec constrained decoding overhead on Qwen3-8B DocRED (200-doc subset) measured on same GPU as P8 SciERC will confirm moderate overhead (<2x), providing consistent timing data for paper",
  "parent": "p8_latency_overhead",
  "spec": {
    "command": "run_constrained_extraction.py unconstrained+full_s1 then analyze_latency.py",
    "server": "westd-21461",
    "data_path": "/root/autodl-tmp/schema_outputs/docred_timing_subset_200.json",
    "dat

MATCH: 70b_docred_unconstrained
{
  "entity_f1": 69.03,
  "entity_precision": 75.03,
  "entity_recall": 63.92,
  "relation_f1": 13.03,
  "relation_precision": 12.43,
  "relation_recall": 13.69,
  "ET_violation": 0.02,
  "RV_violation": 7.8,
  "DR_violation": 15,
  "CF_violation": 0.07,
  "parse_failures": 0,
  "docs_processed": 99
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "7e0fc6ab-d45f-4fd7-9e8d-1e8a9883b864",
  "tool_use_result": {
    "stdout": "=== p8b_docred_latency ===\n{\n  \"status\": \"DONE\",\n  \"retry_count\": 0,\n  \"created_at\": \"2026-05-18T15:14:28.888Z\",\n  \"updated_at\": \"2026-05-18T17:48:57.349Z\",\n  \"hypothesis\": \"OntoCoDec constrained decoding overhead on Qwen3-8B DocRED (200-doc subset) measured on same GPU as P8 SciERC will confirm moderate overhead (<2x), providing consistent timing data for paper\",\n  \"parent\": \"p8_latency_overhead\",\n  \"spec\": {\n    \"command\": \"run_constrained_extraction.py unconstrained+full_s1 then analyze_latency.py\",\n    \"server\": \"westd-21461\",\n    \"data_path\": \"/root/autodl-tmp/schema_outputs/docred_timing_subset_200.json\",\n    \"dat\n\n=== p8b_docred_latency ===\n{\n  \"status\": \"DONE\",\n  \"retry_count\": 0,\n  \"created_at\": \"2026-05-18T15:14:28.888Z\",\n  \"updated_at\": \"2026-05-18T17:48:57.349Z\",\n  \"hypothesis\": \"OntoCoDec constrained decoding overhead on Qwen3-8B DocRED (200-doc subset) measured on same GPU as P8 SciERC will confirm moderate overhead (<2x), providing consistent timing data for paper\",\n  \"parent\": \"p8_latency_overhead\",\n  \"spec\": {\n    \"command\": \"run_constrained_extraction.py unconstrained+full_s1 then analyze_latency.py\",\n    \"server\": \"westd-21461\",\n    \"data_path\": \"/root/autodl-tmp/schema_outputs/docred_timing_subset_200.json\",\n    \"dat\n\nMATCH: 70b_docred_unconstrained\n{\n  \"entity_f1\": 69.03,\n  \"entity_precision\": 75.03,\n  \"entity_recall\": 63.92,\n  \"relation_f1\": 13.03,\n  \"relation_precision\": 12.43,\n  \"relation_recall\": 13.69,\n  \"ET_violation\": 0.02,\n  \"RV_violation\": 7.8,\n  \"DR_violation\": 15,\n  \"CF_violation\": 0.07,\n  \"parse_failures\": 0,\n  \"docs_processed\": 99",
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

_source line 110_

<details><summary>Logged reasoning block</summary>

```text
The 2.43% appears in appendix_discussion.tex line 383: "On DocRED (same configuration), unconstrained inference averages 19.34\,s/doc and Full S1 averages 19.81\,s/doc ($+$2.43\% overhead)."

But the p8b_docred_latency experiment failed and has no metrics. So the 2.43% number is stated in the paper but lacks registry backing.

Let me check the appendix_discussion.tex for the source of this number and if it references an exp_id.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "290a4398-0f2c-4210-8f22-7a27224af02d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TDigx6qLhyHRHzTdCSmY5i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1974,
      "cache_read_input_tokens": 54218,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1974
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

_source line 111_

<details open><summary>🔧 Tool call — Read · `toolu_017CamdYKCsfE6ybhkwC2KJv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex",
  "offset": 375,
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
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "5c548427-f8ff-4966-ba19-670c969a9eb8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TDigx6qLhyHRHzTdCSmY5i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1974,
      "cache_read_input_tokens": 54218,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1974
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

_source line 112 · 2026-05-22T04:13:26.990Z_

<details><summary>↩ Tool result · `toolu_017CamdYKCsfE6ybhkwC2KJv`</summary>

```text
375	Under fine-tuning, both strategies converge because few violations remain to filter or constrain ($\Delta \leq 0.55$\,pp across all four FT groups, with each strategy winning two).
376	
377	%%% Zero-Shot Runtime Profiling %%%
378	
379	\paragraph{Zero-Shot Runtime Profiling.}
380	\label{app:runtime}
381	
382	On SciERC (Qwen3-8B, zero-shot greedy, NVIDIA RTX PRO 6000 Blackwell Server Edition), unconstrained inference averages 4.163\,s/doc and Full S1 constrained decoding averages 4.710\,s/doc ($+$13.1\% overhead).
383	On DocRED (same configuration), unconstrained inference averages 19.34\,s/doc and Full S1 averages 19.81\,s/doc ($+$2.43\% overhead).
384	The lower relative overhead on DocRED reflects amortization: the fixed per-token constraint cost is spread over longer generation sequences.
385	XGrammar automaton compilation takes 0.044\,s; the full constraint pipeline (schema parsing, JSON Schema generation, grammar compilation) takes 0.33\,s on SciERC (Table~\ref{tab:scalability}), amortized to zero over the evaluation set.
386	
387	% exp_id: p8c_ft_scierc_latency — Reviewer Report #23 verified
388	\paragraph{Fine-Tuned Latency Profiling.}
389	\label{app:ft-latency}
390	Under LoRA fine-tuning (same hardware and dataset), unconstrained inference averages 2.612\,s/doc and Full S1 constrained decoding averages 2.873\,s/doc ($+$10.0\% overhead, $n{=}551$).
391	Fine-tuned models generate shorter, more structured outputs than zero-shot models (2.612\,s vs.\ 4.163\,s/doc unconstrained); absolute generation time drops by 37\%.
392	The relative overhead ($+$10.0\%) is slightly lower than zero-shot ($+$13.1\%), consistent with shorter sequences requiring fewer constraint checks per document.
393	
394	%%% Fuzzy Relation Matching %%%
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "da9b7ca4-2a91-40ed-a234-39b88bb54d9b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex",
      "content": "Under fine-tuning, both strategies converge because few violations remain to filter or constrain ($\\Delta \\leq 0.55$\\,pp across all four FT groups, with each strategy winning two).\n\n%%% Zero-Shot Runtime Profiling %%%\n\n\\paragraph{Zero-Shot Runtime Profiling.}\n\\label{app:runtime}\n\nOn SciERC (Qwen3-8B, zero-shot greedy, NVIDIA RTX PRO 6000 Blackwell Server Edition), unconstrained inference averages 4.163\\,s/doc and Full S1 constrained decoding averages 4.710\\,s/doc ($+$13.1\\% overhead).\nOn DocRED (same configuration), unconstrained inference averages 19.34\\,s/doc and Full S1 averages 19.81\\,s/doc ($+$2.43\\% overhead).\nThe lower relative overhead on DocRED reflects amortization: the fixed per-token constraint cost is spread over longer generation sequences.\nXGrammar automaton compilation takes 0.044\\,s; the full constraint pipeline (schema parsing, JSON Schema generation, grammar compilation) takes 0.33\\,s on SciERC (Table~\\ref{tab:scalability}), amortized to zero over the evaluation set.\n\n% exp_id: p8c_ft_scierc_latency — Reviewer Report #23 verified\n\\paragraph{Fine-Tuned Latency Profiling.}\n\\label{app:ft-latency}\nUnder LoRA fine-tuning (same hardware and dataset), unconstrained inference averages 2.612\\,s/doc and Full S1 constrained decoding averages 2.873\\,s/doc ($+$10.0\\% overhead, $n{=}551$).\nFine-tuned models generate shorter, more structured outputs than zero-shot models (2.612\\,s vs.\\ 4.163\\,s/doc unconstrained); absolute generation time drops by 37\\%.\nThe relative overhead ($+$10.0\\%) is slightly lower than zero-shot ($+$13.1\\%), consistent with shorter sequences requiring fewer constraint checks per document.\n\n%%% Fuzzy Relation Matching %%%",
      "numLines": 20,
      "startLine": 375,
      "totalLines": 533
    }
  }
}
```

</details>

---

### Assistant

_source line 113_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full picture. Let me verify the 37% claim from line 391:
- ZS unconstrained: 4.163 s/doc
- FT unconstrained: 2.612 s/doc
- (4.163 - 2.612) / 4.163 = 1.551 / 4.163 = 0.3726 = 37.3% → rounds to 37% ✓

And the 2.43% DocRED overhead:


- unconstrained: 19.34 s/doc
- constrained: 19.81 s/doc
- (19.81 - 19.34) / 19.34 = 0.47 / 19.34 = 0.0243 = 2.43% ✓

But this data has no registry backing—the p8b_docred_latency experiment failed, so these numbers only appear in the paper text. I should also cross-check the scalability claims about 2-3% overhead with 200 entity types and 1000 relations against the d062_ontology_scalability results, then compile my full audit.

Now I'm checking the trie comparison claims. Looking at the actual trie experiment results, the DR percentages range from 15.2% to 95.5% across different model and fine-tuning configurations. The paper states "DR rises to 15–96%", which rounds 15.2 down to 15 and 95.5 up to 96—that's a reasonable approximation of the actual range.

For the unconstrained baseline comparison, I need to find the corresponding DR values. I can see Qwen's zero-shot SciERC unconstrained result is 15.37%, but I still need to locate the Llama zero-shot unconstrained value to complete the comparison.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "363db3da-31fe-42c3-b440-8fc45a6adbe6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XtvEeZChJQsGwVEnbBuvKV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 963,
      "cache_read_input_tokens": 56192,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 963
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

_source line 114_

<details open><summary>🔧 Tool call — Bash · `toolu_01MULipPkLG7gifXG5EPXcvM`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained_ie/06688fc2-d26c-40b0-8ebe-68d505b40c0d/tool-results/mcp-agent-ml-research-read_registry-1779422951081.txt 2>/dev/null | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n\n# Find unconstrained DR for Llama ZS SciERC and Qwen FT SciERC, Llama FT SciERC\ntargets = {\n    'llama_scierc_unconstrained': 'Llama ZS SciERC unc',\n    'phase2_scierc_unconstrained': 'Qwen ZS SciERC unc (phase2)',\n    'w5_llama_lora_scierc_unconstrained_eval': 'Llama FT SciERC unc',\n    'w5_lora_scierc_unconstrained_eval': 'Qwen FT SciERC unc',\n}\n\nfor k, desc in targets.items():\n    if k in exps:\n        m = exps[k].get('metrics', {})\n        dr = m.get('DR_pct') or m.get('domain_range_violation_rate')\n        print(f'{desc} ({k}): DR={dr}')\n    else:\n        print(f'{desc} ({k}): NOT FOUND')\n\n# Also check the cross-model section for Llama ZS unconstrained DR\nprint()\nprint('=== Cross-model ZS unconstrained DR ===')\nfor k in exps:\n    if 'llama' in k.lower() and 'scierc' in k.lower() and 'unconstrained' in k.lower() and 'lora' not in k.lower() and 'ft' not in k.lower():\n        m = exps[k].get('metrics', {})\n        dr = m.get('DR_pct') or m.get('domain_range_violation_rate') or m.get('DR_violation')\n        print(f'{k}: DR={dr}')\n\n# Verify scalability data\nprint()\nprint('=== d062_ontology_scalability ===')\ne = exps.get('d062_ontology_scalability', {})\nprint(json.dumps(e.get('metrics', {}), indent=2))\n\" 2>&1 || cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/06688fc2-d26c-40b0-8ebe-68d505b40c0d/tool-results/mcp-agent-ml-research-read_registry-1779422951081.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\ntargets = {\n    'llama_scierc_unconstrained': 'Llama ZS SciERC unc',\n    'phase2_scierc_unconstrained': 'Qwen ZS SciERC unc (phase2)',\n    'w5_llama_lora_scierc_unconstrained_eval': 'Llama FT SciERC unc',\n    'w5_lora_scierc_unconstrained_eval': 'Qwen FT SciERC unc',\n}\nfor k, desc in targets.items():\n    if k in exps:\n        m = exps[k].get('metrics', {})\n        dr = m.get('DR_pct') or m.get('domain_range_violation_rate')\n        print(f'{desc} ({k}): DR={dr}')\nprint()\nfor k in exps:\n    if 'llama' in k.lower() and 'scierc' in k.lower() and 'unconstrained' in k.lower() and 'lora' not in k.lower():\n        m = exps[k].get('metrics', {})\n        dr = m.get('DR_pct') or m.get('domain_range_violation_rate') or m.get('DR_violation')\n        print(f'{k}: DR={dr}')\nprint()\nprint('=== d062_ontology_scalability ===')\ne = exps.get('d062_ontology_scalability', {})\nprint(json.dumps(e.get('metrics', {}), indent=2))\n\"",
  "description": "Get unconstrained DR for cross-model and scalability data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "70cbb951-1197-4f52-b976-ccaa016a917f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XtvEeZChJQsGwVEnbBuvKV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 963,
      "cache_read_input_tokens": 56192,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 963
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

_source line 115 · 2026-05-22T04:13:57.107Z_

<details><summary>↩ Tool result · `toolu_01MULipPkLG7gifXG5EPXcvM`</summary>

```text
Traceback (most recent call last):
  File "&lt;string>", line 3, in &lt;module>
    data = json.loads(json.loads(sys.stdin.read())['result'])
                      ~~~~~~~~~~^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.14/json/__init__.py", line 352, in loads
    return _default_decoder.decode(s)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^
  File "/usr/lib/python3.14/json/decoder.py", line 345, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
               ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.14/json/decoder.py", line 363, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
Llama ZS SciERC unc (llama_scierc_unconstrained): DR=0.1334
Qwen ZS SciERC unc (phase2) (phase2_scierc_unconstrained): DR=0.1537
Llama FT SciERC unc (w5_llama_lora_scierc_unconstrained_eval): DR=0.0111
Qwen FT SciERC unc (w5_lora_scierc_unconstrained_eval): DR=0.0195

llama_scierc_unconstrained: DR=0.1334

=== d062_ontology_scalability ===
{
  "compile_small_total_s": 0.334,
  "compile_medium_total_s": 0.322,
  "compile_large_total_s": 0.345,
  "compile_xlarge_total_s": 0.42,
  "grammar_small_s": 0.333,
  "grammar_xlarge_s": 0.365,
  "semantic_small_s": 0.0004,
  "semantic_xlarge_s": 0.017,
  "overhead_small": 1.02,
  "overhead_medium": 1.03,
  "overhead_large": 1.03,
  "overhead_xlarge": 1.03,
  "failures": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "cb86876b-cdf8-44c5-b33d-ae801ad4b163",
  "tool_use_result": {
    "stdout": "Traceback (most recent call last):\n  File \"&lt;string>\", line 3, in &lt;module>\n    data = json.loads(json.loads(sys.stdin.read())['result'])\n                      ~~~~~~~~~~^^^^^^^^^^^^^^^^^^\n  File \"/usr/lib/python3.14/json/__init__.py\", line 352, in loads\n    return _default_decoder.decode(s)\n           ~~~~~~~~~~~~~~~~~~~~~~~^^^\n  File \"/usr/lib/python3.14/json/decoder.py\", line 345, in decode\n    obj, end = self.raw_decode(s, idx=_w(s, 0).end())\n               ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/usr/lib/python3.14/json/decoder.py\", line 363, in raw_decode\n    raise JSONDecodeError(\"Expecting value\", s, err.value) from None\njson.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)\nLlama ZS SciERC unc (llama_scierc_unconstrained): DR=0.1334\nQwen ZS SciERC unc (phase2) (phase2_scierc_unconstrained): DR=0.1537\nLlama FT SciERC unc (w5_llama_lora_scierc_unconstrained_eval): DR=0.0111\nQwen FT SciERC unc (w5_lora_scierc_unconstrained_eval): DR=0.0195\n\nllama_scierc_unconstrained: DR=0.1334\n\n=== d062_ontology_scalability ===\n{\n  \"compile_small_total_s\": 0.334,\n  \"compile_medium_total_s\": 0.322,\n  \"compile_large_total_s\": 0.345,\n  \"compile_xlarge_total_s\": 0.42,\n  \"grammar_small_s\": 0.333,\n  \"grammar_xlarge_s\": 0.365,\n  \"semantic_small_s\": 0.0004,\n  \"semantic_xlarge_s\": 0.017,\n  \"overhead_small\": 1.02,\n  \"overhead_medium\": 1.03,\n  \"overhead_large\": 1.03,\n  \"overhead_xlarge\": 1.03,\n  \"failures\": 0\n}",
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

_source line 116_

<details><summary>Logged reasoning block</summary>

```text
Now let me also check: the paper says "1-15% unconstrained" for the trie comparison context. Let me verify this range.

From the cross-model data, the unconstrained DRs for SciERC ZS are:
- Qwen: DR=15.37% (from ablation table)
- Llama: DR=13.34% (from llama_scierc_unconstrained, stored as 0.1334 which is 13.34%)

Wait, the registry stores DR as 0.1334 for llama_scierc_unconstrained. 

I see now—the registry stores these values as fractions rather than percentages, so 0.1537 equals 15.37% and 0.1334 equals 13.34%. The paper's "1-15% unconstrained" baseline appears to refer to the trie experiments across Qwen and Llama models in both fine-tuned and zero-shot settings on SciERC. Looking at the trie-only results, the range spans from 15.2% to 95.5%, which aligns with the paper's "15-96%" claim. Now checking the beam latency numbers—the greedy beam overhead matches at 1.32x, but the constraint overhead shows 1.165x where the paper reports 1.17x, so there's a slight discrepancy I need to investigate. I'm checking the rounding discrepancy between the paper's reported 1.17× and the actual calculated value of 1.165×—the difference hinges on whether we're using standard rounding rules, where 1.165 would round to 1.16 under "round half to even" but to 1.17 under "round half up." which rounds to 1.16 at 2 decimal places. But the registry lists 1.165 directly, and using standard rounding rules, 1.165 rounds up to 1.17. So there's a discrepancy between what the paper states (1.17×) and the appendix (16.5% overhead, or 1.165×) — a minor inconsistency in how the values are presented across different sections.

Now I'm checking the beam search results on SciERC LoRA to verify the "R-F1 44-47" range. Looking at the experimental data across different beam widths and configurations, the F1 scores cluster around 44-46, which aligns with the paper's claimed range. Looking at the specific LoRA beam S1 experiments on SciERC, I'm seeing R-F1 values of 46.11, 44.23, and 46.18 across the different model runs, which does support the "44-47" range claim. But I'm puzzled about where the 43.60 value mentioned in the composability section comes from—it doesn't appear in these beam results. The Qwen beam4 result gives me 44.23, and Llama tops out at 46.18—so the actual range is 44-46 when rounded, not 44-47 as the paper states. The upper bound appears to be overstated.

Let me verify the zero-shot beam claim about achieving 0% DR on both datasets, and then I can finalize the audit.

Now I'm checking the ablation results to confirm the 24% DR reduction for the Semantic constraint. Looking at the numbers: unconstrained DR is 15.37%, and with just the Semantic constraint it drops to 11.65%, which works out to about a 24% relative reduction—that matches what the paper claims. The Grammar-only constraint shows a smaller 3% reduction, and the full approach gets down to under 1% DR.

But there's a discrepancy in the paper text—it mentions the grammar-only ablation achieving 24% DR reduction, when the table actually shows Grammar at 3% and Semantic at 24%. I need to reread the section more carefully to understand what's being referenced. Looking at the table values more carefully, Grammar (row 2) shows ↓3% DR reduction while Semantic (row 3) shows ↓24%. The paper text attributes 24% to the grammar-only ablation in row 2, but that's actually the Semantic row's value—this appears to be a mislabeling. However, I should consider whether "grammar-only" in the paper's comparison to GCD might refer to a different constraint level than what's labeled as "Grammar" in the ablation table itself. I'm noticing a discrepancy in the paper—the text claims Grammar achieves 24% DR reduction, but the table clearly shows it only achieves 3% DR reduction. The Semantic component is what actually achieves the 24% reduction. I should also verify the scalability claims about constant 2-3% overhead, which the data appears to support across different entity and relation scales.

Now I'm compiling all my findings to create a comprehensive audit of the paper's claims against the actual metrics. correctly from those raw numbers but has NO REGISTRY BACKING

**Line 5: "+10.0% with 37% lower absolute latency" (under LoRA)**
- Registry: p8c_ft_scierc_latency.overhead_mean_pct = 10 ✓
- 37% lower: (4.163 - 2.612) / 4.163 = 37.3% → rounds to 37% ✓
- Source: p8_latency_overhead (ZS) vs p8c_ft_scierc_latency (FT) unconstrained means

**Line 6: "<0.5s" constraint compilation**
- Registry: d062_ontology_scalability.compile_xlarge_total_s = 0.42 ✓ (max compilation time)

**Line 6: "constant overhead (2-3%) up to 200 entity types and 1,000 relations"**
- Registry: d062_ontology_scalability overheads = 1.02-1.03 → 2-3% ✓
- Sizes not in metrics; need to verify what "xlarge" maps to

**Line 11: "R-F1 44-47" for beam S1 LoRA on SciERC**
- Registry experiments: R-F1 ranges from 44.23 (Qwen) to 46.18 (Llama)
- Paper says "44-47" → upper bound 47 not supported by data (max is 46.18 → rounds to 46)
- **MISMATCH**: should be "44-46"

**Line 11: "DR=0% on both datasets"** - Now checking whether the zero dropout rate claim holds across the registry data for both datasets.

**Line 12: "1.54× (beam 1.32× + constraint 1.17×)"** - Verifying the latency multipliers by cross-referencing beam search and constraint overhead ratios against the registry values, where beam4 constrained divided by greedy unconstrained gives 1.537, beam-to-greedy ratio is 1.319, and constraint overhead is 1.165.

**Line 17: "6.41%→0% DR"** - Checking the DocRED result where the baseline DR drops from 6.41% to 0%.

**Line 17: "R-F1 11.24, +0.09 pp"** - Confirming the relation F1 score of 11.24 with a 0.09 percentage point improvement over the baseline of 11.15.

**Line 17: "CF 3.50% (from 0% unconstrained)"** - The constraint failure rate increases to 3.50% from the unconstrained baseline of 0%.

**Line 19: "XX.XX" placeholders** - The 70B LoRA evaluation is still pending; the training is complete but the eval experiments are currently running or preparing.

**Line 19: "8B pattern (9.90%→1.18%)"** - Looking at the ablation table to verify the constraint failure reduction in the full S1 configuration for SciERC zero-shot.

**Line 24: "only 24% DR reduction vs. Full S1's 94%"** - I'm checking the ablation table rows more carefully. The grammar-only ablation shows a 3% DR reduction, but the paper seems to be citing 24%, which actually corresponds to the semantic-only ablation in row 3. There's a mismatch between what the paper attributes to grammar-only and what the table actually shows. I'm checking the row numbering in the table—Grammar is row 2 with ΔDR = ↓3%, while Semantic is row 3 with ΔDR = ↓24%. The text claims grammar-only achieves "24% DR reduction," but that matches the Semantic row, not Grammar. This looks like they mixed up which ablation they were referencing—the Grammar row should show 3%, not 24%.

Now looking at the Trie experiments, the DR values range from 15.2% to 95.5% across different model configurations, which the paper rounds to "15-96%." For unconstrained decoding, the range spans 1.11% to 15.37%, matching the paper's stated "1-15%" range.

I'm also checking how the experiment IDs are formatted in the paper's comments versus the registry keys—some need the r16_ prefix added, and I need to verify which suffixes like _200 are actually part of the key names.

Now let me pull together the final report, and I should double-check that the beam LoRA experiments on SciERC truly eliminate all four violation types as claimed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "b1c30251-12d9-427d-b4d3-786cdb15e902",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015yxB5L1ayA3m8sojh48i3c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2446,
      "cache_read_input_tokens": 57155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2446
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

_source line 117_

<details open><summary>🔧 Tool call — Bash · `toolu_01TfFM8m9XTicgHdyJEqR6Um`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/06688fc2-d26c-40b0-8ebe-68d505b40c0d/tool-results/mcp-agent-ml-research-read_registry-1779422951081.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n\n# 1. w10_qwen_scierc_ft_beam_4 full metrics\nprint('=== w10_qwen_scierc_ft_beam_4 ===')\nprint(json.dumps(exps['w10_qwen_scierc_ft_beam_4'].get('metrics',{}), indent=2))\nprint()\n\n# 2. d062_ontology_scalability spec (to check what sizes map to)\nprint('=== d062_ontology_scalability spec ===')\nprint(json.dumps(exps['d062_ontology_scalability'].get('spec',{}), indent=2)[:600])\nprint()\nprint(json.dumps(exps['d062_ontology_scalability'].get('hypothesis',''), indent=2)[:300])\n\"",
  "description": "Check Qwen beam-4 violations and scalability spec"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "db3f677a-e53f-4cc4-8214-a46ae584d19a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015yxB5L1ayA3m8sojh48i3c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2446,
      "cache_read_input_tokens": 57155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2446
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

_source line 118 · 2026-05-22T04:16:13.275Z_

<details><summary>↩ Tool result · `toolu_01TfFM8m9XTicgHdyJEqR6Um`</summary>

```text
=== w10_qwen_scierc_ft_beam_4 ===
{
  "DR": 0,
  "CF": 0,
  "total_violation_rate": 0,
  "entity_type_violation_rate": 0,
  "relation_vocab_violation_rate": 0,
  "domain_range_violation_rate": 0,
  "cross_field_consistency_violation_rate": 0,
  "E_F1": 66.88,
  "E_P": 64.69,
  "E_R": 69.22,
  "R_F1": 44.23,
  "R_P": 39.41,
  "R_R": 50.41,
  "total_samples": 551,
  "json_parse_failures": 0,
  "total_entities": 1802,
  "total_relations": 1246,
  "vs_ft_greedy": {
    "baseline": "w5_lora_scierc_constrained_eval",
    "DR_delta": "0% \u2192 0% (same)",
    "CF_delta": "1.18% \u2192 0.0% (eliminated all violations)",
    "E_F1_delta": "67.05 \u2192 66.88 (-0.17, negligible)",
    "R_F1_delta": "43.77 \u2192 44.23 (+0.46, slight improvement)"
  },
  "vs_zs_beam_k4": {
    "DR_delta": "0% \u2192 0% (same)",
    "CF_delta": "0.53% \u2192 0.0% (eliminated)",
    "E_F1_delta": "32.00 \u2192 66.88 (+34.88)",
    "R_F1_delta": "8.56 \u2192 44.23 (+35.67)"
  }
}

=== d062_ontology_scalability spec ===
{
  "command": "python3 scripts/ontology_scalability_benchmark.py",
  "server": "westd-16980",
  "data_path": "/root/schema_semantic_constrained_ie/data/",
  "data_count": 40,
  "model_name": "Qwen3-8B",
  "seed": 42
}

"OntoCoDec's grammar compilation and per-token constraint overhead scale sub-linearly with ontology size (relations and entity types), because the prefix map grows linearly with entity type count but per-token masking only checks the active prefix path, not all types. Compile time may scale super-li
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "4cc54e97-4cc0-41c5-ae2a-fd74fa3f1396",
  "tool_use_result": {
    "stdout": "=== w10_qwen_scierc_ft_beam_4 ===\n{\n  \"DR\": 0,\n  \"CF\": 0,\n  \"total_violation_rate\": 0,\n  \"entity_type_violation_rate\": 0,\n  \"relation_vocab_violation_rate\": 0,\n  \"domain_range_violation_rate\": 0,\n  \"cross_field_consistency_violation_rate\": 0,\n  \"E_F1\": 66.88,\n  \"E_P\": 64.69,\n  \"E_R\": 69.22,\n  \"R_F1\": 44.23,\n  \"R_P\": 39.41,\n  \"R_R\": 50.41,\n  \"total_samples\": 551,\n  \"json_parse_failures\": 0,\n  \"total_entities\": 1802,\n  \"total_relations\": 1246,\n  \"vs_ft_greedy\": {\n    \"baseline\": \"w5_lora_scierc_constrained_eval\",\n    \"DR_delta\": \"0% \\u2192 0% (same)\",\n    \"CF_delta\": \"1.18% \\u2192 0.0% (eliminated all violations)\",\n    \"E_F1_delta\": \"67.05 \\u2192 66.88 (-0.17, negligible)\",\n    \"R_F1_delta\": \"43.77 \\u2192 44.23 (+0.46, slight improvement)\"\n  },\n  \"vs_zs_beam_k4\": {\n    \"DR_delta\": \"0% \\u2192 0% (same)\",\n    \"CF_delta\": \"0.53% \\u2192 0.0% (eliminated)\",\n    \"E_F1_delta\": \"32.00 \\u2192 66.88 (+34.88)\",\n    \"R_F1_delta\": \"8.56 \\u2192 44.23 (+35.67)\"\n  }\n}\n\n=== d062_ontology_scalability spec ===\n{\n  \"command\": \"python3 scripts/ontology_scalability_benchmark.py\",\n  \"server\": \"westd-16980\",\n  \"data_path\": \"/root/schema_semantic_constrained_ie/data/\",\n  \"data_count\": 40,\n  \"model_name\": \"Qwen3-8B\",\n  \"seed\": 42\n}\n\n\"OntoCoDec's grammar compilation and per-token constraint overhead scale sub-linearly with ontology size (relations and entity types), because the prefix map grows linearly with entity type count but per-token masking only checks the active prefix path, not all types. Compile time may scale super-li",
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

_source line 119_

<details><summary>Logged reasoning block</summary>

```text
Now I need to verify what "small", "medium", "large", "xlarge" map to in terms of entity types and relations. Let me check the scalability appendix.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "32bf56aa-250b-46a2-ba62-e649288811c6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013sc523ZPJ2cmzEvZKDyvgn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7827,
      "cache_read_input_tokens": 59601,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7827
      },
      "output_tokens": 10,
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

_source line 120_

<details open><summary>🔧 Tool call — Grep · `toolu_01BnTAbqXwpdF95pidy2Pqy5`</summary>

```json
{
  "pattern": "tab:scalability|app:scalability|200.*entity.*type|1.000.*relation|xlarge",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "head_limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "7f460327-0e95-4b59-859d-10d0da786c99",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013sc523ZPJ2cmzEvZKDyvgn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7827,
      "cache_read_input_tokens": 59601,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7827
      },
      "output_tokens": 10,
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

_source line 121 · 2026-05-22T04:16:25.480Z_

<details><summary>↩ Tool result · `toolu_01BnTAbqXwpdF95pidy2Pqy5`</summary>

```text
artifacts/_project/paper/main.tex:90:Scalability benchmarks up to 200 entity types and 1,000 relations show constant 2--3\% inference overhead and sub-second compilation ($<$0.5\,s; Appendix~\ref{app:scalability}); however, the first-token uniqueness requirement for continuation masking may become a tokenizer-dependent bottleneck beyond this scale.
artifacts/_project/paper/appendix_related_work.tex:40:\citet{roth_yih_2004} formulate joint entity and relation identification as an integer linear program (ILP) that enforces type constraints (e.g., \textsc{Emp-Org} only between \textsc{Per} and \textsc{Org} entities); this establishes the foundational principle that relational type compatibility should be a hard constraint, not a soft preference learned from data.
artifacts/_project/paper/appendix_discussion.tex:385:XGrammar automaton compilation takes 0.044\,s; the full constraint pipeline (schema parsing, JSON Schema generation, grammar compilation) takes 0.33\,s on SciERC (Table~\ref{tab:scalability}), amortized to zero over the evaluation set.
artifacts/_project/paper/section6_relwork_outline.tex:44:The idea of enforcing entity-type compatibility constraints for IE dates back to pre-neural methods: \citet{roth_yih_2004} formulate joint entity and relation identification as an integer linear program (ILP) that enforces type constraints---e.g., EMP-ORG only between PER and ORG entities---establishing the principle that relational type compatibility should be a hard constraint, not a soft preference.
artifacts/_project/paper/section5_runtime.tex:6:Constraint compilation is one-time $<$0.5\,s; scaling benchmarks confirm constant overhead (2--3\%) up to 200 entity types and 1{,}000 relations (Appendix~\ref{app:scalability}).
artifacts/_project/paper/appendix_scalability.tex:2:\label{app:scalability}
artifacts/_project/paper/appendix_scalability.tex:19:\label{tab:scalability}
artifacts/_project/paper/appendix_scalability.tex:22:Full constraint compilation (schema parsing + grammar build) scales sub-linearly (0.32\,s to 0.42\,s for 7$\to$1{,}000 relations; Table~\ref{tab:scalability}); within this, the XGrammar automaton accounts for $\sim$0.044\,s and semantic constraint compilation grows linearly but remains negligible (0.4\,ms to 17\,ms).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "dd87189d-b3cf-48e9-8682-73867648cb02",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/_project/paper/main.tex:90:Scalability benchmarks up to 200 entity types and 1,000 relations show constant 2--3\\% inference overhead and sub-second compilation ($<$0.5\\,s; Appendix~\\ref{app:scalability}); however, the first-token uniqueness requirement for continuation masking may become a tokenizer-dependent bottleneck beyond this scale.\nartifacts/_project/paper/appendix_related_work.tex:40:\\citet{roth_yih_2004} formulate joint entity and relation identification as an integer linear program (ILP) that enforces type constraints (e.g., \\textsc{Emp-Org} only between \\textsc{Per} and \\textsc{Org} entities); this establishes the foundational principle that relational type compatibility should be a hard constraint, not a soft preference learned from data.\nartifacts/_project/paper/appendix_discussion.tex:385:XGrammar automaton compilation takes 0.044\\,s; the full constraint pipeline (schema parsing, JSON Schema generation, grammar compilation) takes 0.33\\,s on SciERC (Table~\\ref{tab:scalability}), amortized to zero over the evaluation set.\nartifacts/_project/paper/section6_relwork_outline.tex:44:The idea of enforcing entity-type compatibility constraints for IE dates back to pre-neural methods: \\citet{roth_yih_2004} formulate joint entity and relation identification as an integer linear program (ILP) that enforces type constraints---e.g., EMP-ORG only between PER and ORG entities---establishing the principle that relational type compatibility should be a hard constraint, not a soft preference.\nartifacts/_project/paper/section5_runtime.tex:6:Constraint compilation is one-time $<$0.5\\,s; scaling benchmarks confirm constant overhead (2--3\\%) up to 200 entity types and 1{,}000 relations (Appendix~\\ref{app:scalability}).\nartifacts/_project/paper/appendix_scalability.tex:2:\\label{app:scalability}\nartifacts/_project/paper/appendix_scalability.tex:19:\\label{tab:scalability}\nartifacts/_project/paper/appendix_scalability.tex:22:Full constraint compilation (schema parsing + grammar build) scales sub-linearly (0.32\\,s to 0.42\\,s for 7$\\to$1{,}000 relations; Table~\\ref{tab:scalability}); within this, the XGrammar automaton accounts for $\\sim$0.044\\,s and semantic constraint compilation grows linearly but remains negligible (0.4\\,ms to 17\\,ms).",
    "numLines": 8
  }
}
```

</details>

---

### Tool call

_source line 122_

<details open><summary>🔧 Tool call — Read · `toolu_01EYBUu74A1nhVqajiR9Muac`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_scalability.tex",
  "limit": 40
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "e20a9df5-6fd8-4973-a60a-76d9ef1336d6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VBshyCZ4iK62TQRtrTFboD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 891,
      "cache_read_input_tokens": 67428,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 891
      },
      "output_tokens": 61,
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

_source line 123 · 2026-05-22T04:16:29.846Z_

<details><summary>↩ Tool result · `toolu_01EYBUu74A1nhVqajiR9Muac`</summary>

```text
1	\section{Ontology Scalability}
2	\label{app:scalability}
3	
4	\begin{table}[h]
5	\centering
6	\small
7	\resizebox{\columnwidth}{!}{%
8	\begin{tabular}{@{}lrrrr@{}}
9	\toprule
10	\textbf{Scale} & \textbf{Types} & \textbf{Rels} & \textbf{Compile (s)} & \textbf{Overhead} \\
11	\midrule
12	Small (SciERC) & 6 & 7 & 0.33 & 1.02$\times$ \\
13	Medium (DocRED) & 6 & 96 & 0.32 & 1.03$\times$ \\
14	Large (synth.) & 100 & 500 & 0.35 & 1.03$\times$ \\
15	XLarge (synth.) & 200 & 1{,}000 & 0.42 & 1.03$\times$ \\
16	\bottomrule
17	\end{tabular}}
18	\caption{Compilation time (one-time) and per-token inference overhead across ontology scales. Small and Medium use real ontologies; Large and XLarge use synthetic ontologies with random domain/range constraints. Overhead measured on Qwen3-8B, 10 documents per scale.}
19	\label{tab:scalability}
20	\end{table}
21	
22	Full constraint compilation (schema parsing + grammar build) scales sub-linearly (0.32\,s to 0.42\,s for 7$\to$1{,}000 relations; Table~\ref{tab:scalability}); within this, the XGrammar automaton accounts for $\sim$0.044\,s and semantic constraint compilation grows linearly but remains negligible (0.4\,ms to 17\,ms).
23	Inference overhead is constant at 2--3\% because XGrammar uses precompiled bitmasks ($O(1)$ per token) and the semantic layer checks only the active relation's domain/range set rather than the full ontology.
24	The practical limit is first-token uniqueness: when entity types exceed $\sim$200, prefix collisions in the tokenizer vocabulary may require fallback to multi-token disambiguation (\S\ref{sec:dynamic-masking}).
25	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "af7e9d0c-14eb-4f94-86fa-686146be74ac",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_scalability.tex",
      "content": "\\section{Ontology Scalability}\n\\label{app:scalability}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lrrrr@{}}\n\\toprule\n\\textbf{Scale} & \\textbf{Types} & \\textbf{Rels} & \\textbf{Compile (s)} & \\textbf{Overhead} \\\\\n\\midrule\nSmall (SciERC) & 6 & 7 & 0.33 & 1.02$\\times$ \\\\\nMedium (DocRED) & 6 & 96 & 0.32 & 1.03$\\times$ \\\\\nLarge (synth.) & 100 & 500 & 0.35 & 1.03$\\times$ \\\\\nXLarge (synth.) & 200 & 1{,}000 & 0.42 & 1.03$\\times$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Compilation time (one-time) and per-token inference overhead across ontology scales. Small and Medium use real ontologies; Large and XLarge use synthetic ontologies with random domain/range constraints. Overhead measured on Qwen3-8B, 10 documents per scale.}\n\\label{tab:scalability}\n\\end{table}\n\nFull constraint compilation (schema parsing + grammar build) scales sub-linearly (0.32\\,s to 0.42\\,s for 7$\\to$1{,}000 relations; Table~\\ref{tab:scalability}); within this, the XGrammar automaton accounts for $\\sim$0.044\\,s and semantic constraint compilation grows linearly but remains negligible (0.4\\,ms to 17\\,ms).\nInference overhead is constant at 2--3\\% because XGrammar uses precompiled bitmasks ($O(1)$ per token) and the semantic layer checks only the active relation's domain/range set rather than the full ontology.\nThe practical limit is first-token uniqueness: when entity types exceed $\\sim$200, prefix collisions in the tokenizer vocabulary may require fallback to multi-token disambiguation (\\S\\ref{sec:dynamic-masking}).\n",
      "numLines": 25,
      "startLine": 1,
      "totalLines": 25
    }
  }
}
```

</details>

---

### Assistant

_source line 124_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data. Let me verify the scalability numbers:
- XLarge: 200 types, 1000 rels, compile 0.42s, overhead 1.03×

Registry d062_ontology_scalability:
- compile_xlarge_total_s: 0.42 ✓
- overhead_xlarge: 1.03 ✓

Paper says "< 0.5s" for compilation: max is 0.42s ✓
Paper says "2-3%" overhead: range is 1.02×-1.03× = 2%-3% ✓


Paper says "up to 200 entity types and 1,000 relations": matches XLarge ✓

Now I'm checking the SciERC numbers - the table shows 6 entity types while the paper mentions 7 relations, and the compile time is 0.334s versus the paper's 0.33s, which is just rounding. I also need to verify the claim about CF response being model-dependent by looking at the DocRED beam zero-shot CF rates.

Looking at the data, the Qwen model shows 4.94% CF while Llama shows 1.0% CF on the same DocRED beam setup, so that confirms the model-dependent behavior. Now I'm compiling the final audit of all the numbers in section5_runtime.tex to check their verification status.

Going through the claims systematically: the SciERC latency overhead of 13.1% checks out, but the DocRED number is problematic since it only appears in the appendix text without corresponding registry metrics. The LoRA overhead of 10.0% and the 37% latency improvement both verify correctly. For the compilation overhead, the max time of 0.42 seconds and the constant 2-3% overhead range both match the scalability data. The entity and relation counts from the XLarge config are confirmed. Now checking the beam search R-F1 range of 44-47 against the actual values. The constraint overhead calculation checks out—the registry shows 1.165 which matches the appendix's 16.5% figure, though the paper rounds it to 1.17×. Moving on to the 70B zero-shot results, I'm verifying the SciERC metrics: the dropout rate drops from 6.41% to 0%, the relation F1 stays at 11.24 with a 0.09 percentage point gain, and the constraint failure rate is 3.5%.

For the 70B LoRA variant, the evaluation is still running so those placeholders are expected, but I'm catching a discrepancy in the constraint failure pattern—it shows 9.90% in the ablation table's full setup but 1.18% in the composability table. Looking at the Trie comparison section, there's a mismatch where the text claims grammar-only achieves 24% dropout reduction, but that figure actually belongs to the semantic row; the grammar row only shows 3% reduction. The full setup's 94% dropout reduction does match the ablation table though.

Checking the remaining validation points: the grammar row confirms RV and ET both hit zero, the trie-only experiments show dropout rates between 15-96% which aligns with the rounded values, and the unconstrained baselines fall in the 1-15% range as stated. I'm also noting some naming inconsistencies in the experiment IDs—several entries are missing the r16_ prefix that should be there for the 70B LoRA variants and the trie experiments.

Now I'm ready to put together the final report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "f5e42105-3cf1-42c3-bed9-b4f53d6f7322",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VZNZAetovRMvn7Zh5HhXkj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 736,
      "cache_read_input_tokens": 68319,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 736
      },
      "output_tokens": 10,
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

_source line 125_

All data collected. Here is the complete audit.

---

## Section5_runtime.tex Registry 一致性审计报告

### 审计覆盖范围
逐行检查了 section5_runtime.tex 中的 27 个定量声明，对照 registry 实验数据和论文内部表格。

---

### 对比表

| # | 论文声明 | 论文数值 | 对应 exp_id / 来源 | Registry 数值 | 匹配? |
|---|---------|---------|-------------------|--------------|-------|
| 1 | L5: SciERC overhead | +13.1% | `p8_latency_overhead` | overhead_pct=13.1 | ✅ |
| 2 | L5: DocRED overhead | +2.43% | `p8b_docred_latency` | **FAILED, 无 metrics** | ⚠️ 无 registry 支撑 |
| 3 | L5: LoRA overhead | +10.0% | `p8c_ft_scierc_latency` | overhead_mean_pct=10 | ✅ |
| 4 | L5: LoRA absolute latency reduction | 37% lower | `p8_latency_overhead` vs `p8c_ft_scierc_latency` | (4.163−2.612)/4.163=37.3% | ✅ |
| 5 | L6: compilation time | <0.5s | `d062_ontology_scalability` | compile_xlarge=0.42s | ✅ |
| 6 | L6: scaling overhead | 2–3% | `d062_ontology_scalability` | 1.02×–1.03× | ✅ |
| 7 | L6: scale range | 200 types, 1000 rels | `appendix_scalability.tex` XLarge row | 200 types, 1000 rels | ✅ |
| 8 | L11: beam LoRA R-F1 range | 44–47 | `w10_qwen_scierc_ft_beam_4`, `d066_sweep_llama_scierc_beam4_s1_551` | 44.23–46.18 | ❌ 上界应为 46 |
| 9 | L11: beam ZS DR=0% both datasets | 0% | `beam_search_scierc_full_551`, `r14_*_docred_beam4_998` | DR=0 | ✅ |
| 10 | L11: 998-doc DocRED | 998 | `r14_qwen_docred_beam4_998` | samples=998 | ✅ |
| 11 | L12: total latency | 1.54× | `d062_beam_latency` | 4.013/2.612=1.537 | ✅ |
| 12 | L12: beam overhead | 1.32× | `d062_beam_latency` | beam_greedy_ratio=1.319 | ✅ |
| 13 | L12: constraint overhead | 1.17× | `d062_beam_latency` | constraint_overhead_beam=1.165 | ⚠️ 论文1.17×, 实际1.165× (附录写16.5%) |
| 14 | L17: 70B ZS DR | 6.41%→0% | `r16_70b_scierc_zs_s1` | baseline_unc_DR=6.41, DR=0 | ✅ |
| 15 | L17: 70B ZS R-F1 | 11.24 | `r16_70b_scierc_zs_s1` | R_F1=11.24 | ✅ |
| 16 | L17: R-F1 delta | +0.09 pp | `r16_70b_scierc_zs_s1` | 11.24−11.15=0.09 | ✅ |
| 17 | L17: 70B ZS CF | 3.50% | `r16_70b_scierc_zs_s1` | CF_pct=3.5 | ✅ |
| 18 | L17: CF unconstrained baseline | 0% | `r16_70b_scierc_zs_s1` | baseline_unc_CF=0 | ✅ |
| 19 | L19: 70B LoRA数值 | XX.XX占位 | `r16_70b_lora_scierc_eval` / `eval_70b_lora_*` | PREPARING/RUNNING | ✅ 预期 |
| 20 | L19: 8B CF pattern | 9.90%→1.18% | `tab:scierc-ablation` + `tab:composability` | Full S1 CF=9.90%, Qwen FT CF=1.18% | ✅ |
| 21 | L24: grammar-only DR reduction | 24% | `tab:scierc-ablation` row 2 | Grammar ΔDR=**↓3%** (非24%) | ❌ **严重错误** |
| 22 | L24: Full S1 DR reduction | 94% | `tab:scierc-ablation` row 4 | ΔDR=↓94% | ✅ |
| 23 | L24: grammar-only RV/ET | →0% | `tab:scierc-ablation` row 2 | RV=0, ET=0 | ✅ |
| 24 | L25: trie-only DR range | 15–96% | `r16_trie_*` (4个实验) | 15.2–95.5% | ✅ (取整) |
| 25 | L25: unconstrained DR range | 1–15% | 各模型/设置 unconstrained | 1.11–15.37% | ✅ (取整) |

---

### 需要关注的问题

**❌ 严重：L24 grammar-only DR reduction 数值错误**

论文写道：
> "Our grammar-only ablation (Table 3, row 2)... achieving RV/ET→0% but **only 24% DR reduction** vs. Full S1's 94%."

但 `tab:scierc-ablation` row 2 (Grammar) 的 ΔDR = **↓3%**，不是 24%。24% 属于 row 3 (Semantic)。这是将 Semantic 层的效果错误归因到了 Grammar 层。

**修正建议**：将 "24%" 改为 "3%"，或改为引用正确的行。

---

**❌ R-F1 范围上界偏高：L11 "R-F1 44–47" 应为 "44–46"**

beam S1 LoRA SciERC 实验 R-F1：
- `w10_qwen_scierc_ft_beam_4`: 44.23
- `d066_sweep_llama_scierc_beam4_s1_551`: 46.18

最大值 46.18 → 取整后为 46，不是 47。

---

**⚠️ DocRED latency 2.43% 无 registry 支撑**

`p8b_docred_latency` 实验状态为 FAILED，无 metrics。2.43% 仅出现在论文文本中（appendix_discussion.tex L383：19.34→19.81 s/doc），原始数据未回写 registry。建议补登。

---

**⚠️ constraint overhead 1.17× vs registry 1.165×**

`d062_beam_latency.constraint_overhead_beam` = 1.165，论文写 1.17×。附录 beam_search 部分则写 "16.5%"（= 1.165×），与 registry 一致。主文 1.17× 与附录 16.5% 存在内部不一致（取整差异）。

---

**⚠️ exp_id 注释与 registry key 不完全对应**

L14 和 L21 的 `% exp_ids:` 注释使用了缩写名（如 `70b_lora_scierc`），registry 实际 key 为 `r16_70b_lora_scierc`（带 `r16_` 前缀）。不影响数据正确性，但会阻碍自动化追溯。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "uuid": "76da5634-f69e-48e0-8519-890d0e912afe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VZNZAetovRMvn7Zh5HhXkj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 736,
      "cache_read_input_tokens": 68319,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 736
      },
      "output_tokens": 10,
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

_source line 126_

All data collected. Here is the complete audit.

---

## Section5_runtime.tex Registry 一致性审计报告

### 审计覆盖范围
逐行检查了 section5_runtime.tex 中的 27 个定量声明，对照 registry 实验数据和论文内部表格。

---

### 对比表

| # | 论文声明 | 论文数值 | 对应 exp_id / 来源 | Registry 数值 | 匹配? |
|---|---------|---------|-------------------|--------------|-------|
| 1 | L5: SciERC overhead | +13.1% | `p8_latency_overhead` | overhead_pct=13.1 | ✅ |
| 2 | L5: DocRED overhead | +2.43% | `p8b_docred_latency` | **FAILED, 无 metrics** | ⚠️ 无 registry 支撑 |
| 3 | L5: LoRA overhead | +10.0% | `p8c_ft_scierc_latency` | overhead_mean_pct=10 | ✅ |
| 4 | L5: LoRA absolute latency reduction | 37% lower | `p8_latency_overhead` vs `p8c_ft_scierc_latency` | (4.163−2.612)/4.163=37.3% | ✅ |
| 5 | L6: compilation time | <0.5s | `d062_ontology_scalability` | compile_xlarge=0.42s | ✅ |
| 6 | L6: scaling overhead | 2–3% | `d062_ontology_scalability` | 1.02×–1.03× | ✅ |
| 7 | L6: scale range | 200 types, 1000 rels | `appendix_scalability.tex` XLarge row | 200 types, 1000 rels | ✅ |
| 8 | L11: beam LoRA R-F1 range | 44–47 | `w10_qwen_scierc_ft_beam_4`, `d066_sweep_llama_scierc_beam4_s1_551` | 44.23–46.18 | ❌ 上界应为 46 |
| 9 | L11: beam ZS DR=0% both datasets | 0% | `beam_search_scierc_full_551`, `r14_*_docred_beam4_998` | DR=0 | ✅ |
| 10 | L11: 998-doc DocRED | 998 | `r14_qwen_docred_beam4_998` | samples=998 | ✅ |
| 11 | L12: total latency | 1.54× | `d062_beam_latency` | 4.013/2.612=1.537 | ✅ |
| 12 | L12: beam overhead | 1.32× | `d062_beam_latency` | beam_greedy_ratio=1.319 | ✅ |
| 13 | L12: constraint overhead | 1.17× | `d062_beam_latency` | constraint_overhead_beam=1.165 | ⚠️ 论文1.17×, 实际1.165× (附录写16.5%) |
| 14 | L17: 70B ZS DR | 6.41%→0% | `r16_70b_scierc_zs_s1` | baseline_unc_DR=6.41, DR=0 | ✅ |
| 15 | L17: 70B ZS R-F1 | 11.24 | `r16_70b_scierc_zs_s1` | R_F1=11.24 | ✅ |
| 16 | L17: R-F1 delta | +0.09 pp | `r16_70b_scierc_zs_s1` | 11.24−11.15=0.09 | ✅ |
| 17 | L17: 70B ZS CF | 3.50% | `r16_70b_scierc_zs_s1` | CF_pct=3.5 | ✅ |
| 18 | L17: CF unconstrained baseline | 0% | `r16_70b_scierc_zs_s1` | baseline_unc_CF=0 | ✅ |
| 19 | L19: 70B LoRA数值 | XX.XX占位 | `r16_70b_lora_scierc_eval` / `eval_70b_lora_*` | PREPARING/RUNNING | ✅ 预期 |
| 20 | L19: 8B CF pattern | 9.90%→1.18% | `tab:scierc-ablation` + `tab:composability` | Full S1 CF=9.90%, Qwen FT CF=1.18% | ✅ |
| 21 | L24: grammar-only DR reduction | 24% | `tab:scierc-ablation` row 2 | Grammar ΔDR=**↓3%** (非24%) | ❌ **严重错误** |
| 22 | L24: Full S1 DR reduction | 94% | `tab:scierc-ablation` row 4 | ΔDR=↓94% | ✅ |
| 23 | L24: grammar-only RV/ET | →0% | `tab:scierc-ablation` row 2 | RV=0, ET=0 | ✅ |
| 24 | L25: trie-only DR range | 15–96% | `r16_trie_*` (4个实验) | 15.2–95.5% | ✅ (取整) |
| 25 | L25: unconstrained DR range | 1–15% | 各模型/设置 unconstrained | 1.11–15.37% | ✅ (取整) |

---

### 需要关注的问题

**❌ 严重：L24 grammar-only DR reduction 数值错误**

论文写道：
> "Our grammar-only ablation (Table 3, row 2)... achieving RV/ET→0% but **only 24% DR reduction** vs. Full S1's 94%."

但 `tab:scierc-ablation` row 2 (Grammar) 的 ΔDR = **↓3%**，不是 24%。24% 属于 row 3 (Semantic)。这是将 Semantic 层的效果错误归因到了 Grammar 层。

**修正建议**：将 "24%" 改为 "3%"，或改为引用正确的行。

---

**❌ R-F1 范围上界偏高：L11 "R-F1 44–47" 应为 "44–46"**

beam S1 LoRA SciERC 实验 R-F1：
- `w10_qwen_scierc_ft_beam_4`: 44.23
- `d066_sweep_llama_scierc_beam4_s1_551`: 46.18

最大值 46.18 → 取整后为 46，不是 47。

---

**⚠️ DocRED latency 2.43% 无 registry 支撑**

`p8b_docred_latency` 实验状态为 FAILED，无 metrics。2.43% 仅出现在论文文本中（appendix_discussion.tex L383：19.34→19.81 s/doc），原始数据未回写 registry。建议补登。

---

**⚠️ constraint overhead 1.17× vs registry 1.165×**

`d062_beam_latency.constraint_overhead_beam` = 1.165，论文写 1.17×。附录 beam_search 部分则写 "16.5%"（= 1.165×），与 registry 一致。主文 1.17× 与附录 16.5% 存在内部不一致（取整差异）。

---

**⚠️ exp_id 注释与 registry key 不完全对应**

L14 和 L21 的 `% exp_ids:` 注释使用了缩写名（如 `70b_lora_scierc`），registry 实际 key 为 `r16_70b_lora_scierc`（带 `r16_` 前缀）。不影响数据正确性，但会阻碍自动化追溯。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 526894,
  "duration_api_ms": 525854,
  "num_turns": 31,
  "stop_reason": "end_turn",
  "session_id": "06688fc2-d26c-40b0-8ebe-68d505b40c0d",
  "total_cost_usd": 1.49334825,
  "usage": {
    "input_tokens": 26,
    "cache_creation_input_tokens": 57214,
    "cache_read_input_tokens": 936471,
    "output_tokens": 24560,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 57214,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 3821,
        "cache_read_input_tokens": 68319,
        "cache_creation_input_tokens": 736,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 736
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1019,
      "outputTokens": 2111,
      "cacheReadInputTokens": 88125,
      "cacheCreationInputTokens": 26407,
      "webSearchRequests": 0,
      "costUSD": 0.05339525,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 26,
      "outputTokens": 24560,
      "cacheReadInputTokens": 936471,
      "cacheCreationInputTokens": 57214,
      "webSearchRequests": 0,
      "costUSD": 1.439953,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "aa966ff0-a91c-40f4-8797-19d3485f1150"
}
```

</details>

---
