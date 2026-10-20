# Research conversation: [服务器重启后首条消息] 当前日期: 2026-05-15。服务器刚重启，项目状态可能已更新。不要依赖对话历史中的状态信息，以 registry 当前值为准。 **用户消息：** [系统提醒] 你刚才完成了 [Director 指令] 但没 — Part 30 of 41

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap (July export snapshot)** · Conversation logs

[← Part 29](part-029.md) · [Transcript overview](../research-conversation-2026-05-15-registry-director.md) · [Part 31 →](part-031.md) · [Structured JSON](../../../sessions/53/5325f58252a9e4d5e1fc.json)

## Round 346

### Assistant

_source line 6122 · 2026-05-15T17:52:08.066Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me also check:
1. The title location
2. nedellec2026 bib key
3. Qwen 2.5-7B references
4. Code and data section

Let me search for the title.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19337e17-6ba5-47cd-988b-f275ee619db2",
  "isSidechain": false,
  "requestId": "req_011Cb4nCQa8gJHVUyFvBGSqy",
  "type": "assistant",
  "uuid": "030dccd9-3750-4c75-bba6-7aea6b25fd29",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016dvgGkpYX12D26Yg3JSCjh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3156,
      "cache_read_input_tokens": 149401,
      "output_tokens": 515,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3156,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 515,
          "cache_read_input_tokens": 149401,
          "cache_creation_input_tokens": 3156,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3156
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


### Tool call

_source line 6123 · 2026-05-15T17:52:09.733Z_

<details open><summary>🔧 Tool call — Grep · `toolu_014r7ngZQRy8K6mb4rHKxCB5`</summary>

```json
{
  "pattern": "\\\\title",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "030dccd9-3750-4c75-bba6-7aea6b25fd29",
  "isSidechain": false,
  "requestId": "req_011Cb4nCQa8gJHVUyFvBGSqy",
  "type": "assistant",
  "uuid": "2a5520db-f5e8-494d-9b6f-dd071ea35b60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016dvgGkpYX12D26Yg3JSCjh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3156,
      "cache_read_input_tokens": 149401,
      "output_tokens": 515,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3156,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 515,
          "cache_read_input_tokens": 149401,
          "cache_creation_input_tokens": 3156,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3156
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

_source line 6124 · 2026-05-15T17:52:09.754Z_

<details><summary>↩ Tool result · `toolu_014r7ngZQRy8K6mb4rHKxCB5`</summary>

```text
21:\title{Strong Predictors, Weak Selectors:\\ Confidence Signals Predict but Struggle to Select in 8B-Scale Information Extraction}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a5520db-f5e8-494d-9b6f-dd071ea35b60",
  "isSidechain": false,
  "promptId": "4ab6fc0d-e7b3-4753-81c9-824338d4b6fc",
  "type": "user",
  "uuid": "524cb5c8-3edb-4375-8350-577ddc58aef6",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "21:\\title{Strong Predictors, Weak Selectors:\\\\ Confidence Signals Predict but Struggle to Select in 8B-Scale Information Extraction}",
    "numLines": 1
  },
  "sourceToolAssistantUUID": "2a5520db-f5e8-494d-9b6f-dd071ea35b60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite"
}
```

</details>

---


### Tool result

_source line 6125 · 2026-05-15T17:52:11.768Z_

<details><summary>↩ Tool result · `toolu_01YXHz37RJfYKHN6G3a5jGEK`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "29cdae1c-2689-45c3-816b-b6305bf9a516",
  "isSidechain": false,
  "promptId": "4ab6fc0d-e7b3-4753-81c9-824338d4b6fc",
  "type": "user",
  "uuid": "5265db3c-c1e6-41cc-a101-9a5888a1e175",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "29cdae1c-2689-45c3-816b-b6305bf9a516",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite"
}
```

</details>

---


### Tool call

_source line 6126 · 2026-05-15T17:52:10.496Z_

<details open><summary>🔧 Tool call — Grep · `toolu_014A2Ggzwh3sn8ehK4Ubx9UA`</summary>

```json
{
  "pattern": "nedellec|yao2026",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "output_mode": "content",
  "-n": true,
  "glob": "*.{tex,bib}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "524cb5c8-3edb-4375-8350-577ddc58aef6",
  "isSidechain": false,
  "requestId": "req_011Cb4nCQa8gJHVUyFvBGSqy",
  "type": "assistant",
  "uuid": "53b41f21-85b4-423a-add4-4ac2bfac9d1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016dvgGkpYX12D26Yg3JSCjh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3156,
      "cache_read_input_tokens": 149401,
      "output_tokens": 515,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3156,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 515,
          "cache_read_input_tokens": 149401,
          "cache_creation_input_tokens": 3156,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3156
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

_source line 6127 · 2026-05-15T17:52:10.525Z_

<details><summary>↩ Tool result · `toolu_014A2Ggzwh3sn8ehK4Ubx9UA`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex:13:\citet{yao2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, corroborating our quality-estimation findings.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex:16:The most relevant study, \citet{yao2026consistency}, examines consistency--accuracy correlations for LLM-based IE, finding results that our quality-estimation analysis corroborates.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib:280:@article{yao2026consistency,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "53b41f21-85b4-423a-add4-4ac2bfac9d1d",
  "isSidechain": false,
  "promptId": "4ab6fc0d-e7b3-4753-81c9-824338d4b6fc",
  "type": "user",
  "uuid": "8d71b1c8-881b-448c-9bf0-b84716ed8223",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex:13:\\citet{yao2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, corroborating our quality-estimation findings.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex:16:The most relevant study, \\citet{yao2026consistency}, examines consistency--accuracy correlations for LLM-based IE, finding results that our quality-estimation analysis corroborates.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib:280:@article{yao2026consistency,",
    "numLines": 3
  },
  "sourceToolAssistantUUID": "53b41f21-85b4-423a-add4-4ac2bfac9d1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite"
}
```

</details>

---


### Tool call

_source line 6128 · 2026-05-15T17:52:11.745Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01YXHz37RJfYKHN6G3a5jGEK`</summary>

```json
{
  "pattern": "Qwen.2\\.5|Qwen2",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "output_mode": "content",
  "-n": true,
  "glob": "*.{tex,bib}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d71b1c8-881b-448c-9bf0-b84716ed8223",
  "isSidechain": false,
  "requestId": "req_011Cb4nCQa8gJHVUyFvBGSqy",
  "type": "assistant",
  "uuid": "29cdae1c-2689-45c3-816b-b6305bf9a516",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016dvgGkpYX12D26Yg3JSCjh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3156,
      "cache_read_input_tokens": 149401,
      "output_tokens": 515,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3156,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 515,
          "cache_read_input_tokens": 149401,
          "cache_creation_input_tokens": 3156,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3156
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


### Runtime record

_source line 6129_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] [Patch] Round 8 高优先写作修复——不依赖正在跑的实验，立即处理。  按优先级排序：  ## 1. R8-N1 页数压缩至 ≤8 页（CRITICAL，desk-rejection 风险） 当前估计 10-11 页正文。压缩策略： - Discussion free-form ablation 详述移至 Appendix（~0.5 页） - Robustn…",
  "leafUuid": "5265db3c-c1e6-41cc-a101-9a5888a1e175",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6"
}
```

---


### Runtime record

_source line 6130_

```json
{
  "type": "ai-title",
  "aiTitle": "Set up agent communication with Director",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6"
}
```

---


### Assistant

_source line 6131 · 2026-05-15T17:54:02.279Z_

<details><summary>Logged reasoning block</summary>

```text
Good news:
1. **Title**: Already uses "Struggle to Select" — R8-N2 is already done!
2. **nedellec2026**: No such bib key exists. The reference is correctly yao2026consistency.
3. **Qwen 2.5-7B**: No occurrences in any .tex or .bib files. R7-W4 is clean.
4. **Eikema**: Already in Related Work (lines 25, 28). R7-W3/R5-M2 says to "前移到 Related Work MBR 段" — it's already there.


5. Several items are already complete, so I can focus on what still needs attention: the critical page compression task (R8-N1), the abstract rewrite following the problem-finding-implication structure (R4-W3), and R4-W1.

I also need to handle the gap reframing (R3-W2) that combines LP compression with MBR failure as the core issue, reword Contribution 1 (R7-W2), add the Code and Data statement (R8-W1), and position SJ as the primary structural signal (R5-W7). I've confirmed that R6-W1 about the VC majority threshold is already in place, and R8-M1 about the missing bib key is resolved.

The page compression is the most urgent priority right now, so let me start calculating the current main body length to see how much space I'm working with. I need to figure out the actual page limit rules for EMNLP 2026 Findings and what counts toward it. The Director mentioned the paper is currently around 10-11 pages, but the limit is 8 pages for the main body. References and appendices don't count, and Limitations typically sits outside the main page count, so I'm looking at needing to cut roughly 2-3 pages from the core content.

I'm identifying several compression strategies: moving the free-form ablation discussion to the appendix could save about half a page, compressing the robustness paragraph might save another third of a page, removing specific numbers from the introduction contribution bullets could trim a bit more, and condensing the seed variability paragraph in the experiments section. I should also look at tightening section 4.4 on robustness.

Beyond those targeted cuts, I can rewrite the abstract more concisely, rephrase the contributions section, and potentially reframe the gap discussion. Now I'm going to execute these edits aggressively, starting with the discussion's free-form ablation section — I'll move the detailed analysis to the appendix and keep just a 2-3 sentence summary in the main text. The ablation confirms that removing grammar constraints produces nearly identical likelihood distributions and negligible changes in selection performance, ruling out constrained decoding as the source of LP compression. Our consensus-proximity strategies implement MBR decoding, but they all fail because utility correlates with F1 across instances rather than within them.

Different signals optimize for different metrics—quality estimation, binary discrimination, and sample selection don't align—so relying on a single metric risks choosing the wrong signal for the task at hand. Log-probability scores are too compressed within instances to effectively discriminate among candidates, and consensus-proximity approaches that work across instances don't help with within-instance selection. Signal effectiveness varies by task complexity and type, with structural signals dominating on NER while log-probability leads on RE, though these patterns break down at the capability boundary. I'm seeing that instance-level confidence signals tell us which inputs the model struggles with, not which specific output among candidates is actually better. The real issue is that when variance within samples is small compared to overall task difficulty, even perfect quality estimation can't distinguish between nearly identical candidates—so closing this gap likely requires per-sample approaches like trained verifiers rather than relying on instance-level metrics alone. during training due to a configuration default, but this creates only a negligible distribution shift for SciERC (less than 0.3% of the training window) since the blocks remain empty and inference uses constrained decoding to enforce JSON output anyway—CoNLL-2003 and WNUT-17 aren't affected at all. For quality ranking, VC dominates on harder NER tasks while LP outperforms structural signals on RE, likely because RE's high zero-F1 rate makes generation confidence more discriminative than structural overlap. The rankings hold consistently across model families at 8B scale, and at larger scales VC and SJ converge on NER with reduced variance, though all signals lose significance when model capability is insufficient. I'm looking at how to tighten the introduction section on constrained decoding. The key insight is that schema compliance is essential for practical IE systems, and our ablation confirms fine-tuned models maintain format validity without explicit grammar constraints, so I can merge these ideas more efficiently while keeping the footnote about our validation results.

Now examining the central finding about the correlation-selection gap—consistency signals give us decent quality estimation metrics but surprisingly fail at actually selecting good samples, even though there's room for improvement. The issue is that most signals are inherently instance-level, and the two mechanisms that might bridge this gap both have problems: MBR utility doesn't transfer within instances, and log-probabilities get compressed in ways that hurt selection unless we specifically address that compression.

For the signal comparison, I'm looking at five different confidence signals across three categories—structural approaches like entity voting and Soft Jaccard, surface-level metrics like exact match and Fleiss' kappa, and the model's internal log-probability—tested on multiple NER and RE datasets. I see the Director's feedback on the abstract revision—removing signal names, dataset lists, and metrics to restructure it as a problem-finding-implication format, with signal abbreviations moved to the Introduction instead. The current abstract is already fairly streamlined, but I should tighten it further and reorganize around those three core elements.

Now I need to tackle the other revisions: checking all RE mentions to add "preliminary" where it's missing, and in section 4.3, reorganizing the gap analysis around LP compression and MBR failure patterns, with a horizontal rule in Table 3 to separate instances.

I'm also noting the contribution reframing—emphasizing that metrics decouple—and planning to add a code and data availability paragraph at the end. For the SJ signal, I need to verify where "primary structural signal" labeling is needed.

Given the scope, I'll work through these systematically, starting with the highest-impact changes: the Introduction compression and contribution rewording, then the Discussion section (moving ablation to appendix and tightening recommendations), followed by the Experiments section (compressing seed variability and the thinking tokens discussion), updating Table 3, revising the Abstract, checking the Conclusion for RE preliminary mentions, and finally updating the title in main.tex.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5265db3c-c1e6-41cc-a101-9a5888a1e175",
  "isSidechain": false,
  "requestId": "req_011Cb4nD2qx1ruqA8o3Q1Uz3",
  "type": "assistant",
  "uuid": "b3517e67-1938-4f14-a479-8f797926510c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NGW9rZU9gdzZtPiCUhCsra",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 856,
      "cache_read_input_tokens": 152557,
      "output_tokens": 5327,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 856,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5327,
          "cache_read_input_tokens": 152557,
          "cache_creation_input_tokens": 856,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 856
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


### Assistant

_source line 6132 · 2026-05-15T17:54:04.273Z_

已读取全部文件。多项已完成（标题已用 "Struggle to Select"、无 Qwen2.5-7B、Eikema 已在 Related Work、Table 3 caption 已有 VC threshold、无 nedellec2026 bib key）。

集中处理：(1) 页数压缩、(2) Abstract 重写、(3) RE preliminary 标注、(4) Gap reframing、(5) 次要修复。逐文件执行。

**Introduction 压缩 + Contribution 重写 + 信号列表精简：**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3517e67-1938-4f14-a479-8f797926510c",
  "isSidechain": false,
  "requestId": "req_011Cb4nD2qx1ruqA8o3Q1Uz3",
  "type": "assistant",
  "uuid": "ff73a7db-41bb-46dc-96ed-76f8874a8939",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NGW9rZU9gdzZtPiCUhCsra",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 856,
      "cache_read_input_tokens": 152557,
      "output_tokens": 5327,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 856,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5327,
          "cache_read_input_tokens": 152557,
          "cache_creation_input_tokens": 856,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 856
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


### Tool call

_source line 6133 · 2026-05-15T17:54:08.675Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01G64Rzrr92PDDywVNp7UitZ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex",
  "old_string": "Structured IE requires schema-compliant output, making constrained decoding \\cite{willard2023guided} the standard inference strategy---without it, a substantial fraction of outputs from general-purpose models are unparseable.\\footnote{Fine-tuned models may retain format compliance without grammar constraints: our free-form ablation achieves 99.95\\% valid JSON rate (\\S\\ref{sec:ablation}).}\nAll experiments use constrained decoding, the regime under which structured IE is practically deployed.\n\nOur central finding is the \\textbf{correlation-selection gap} (Figure~\\ref{fig:overview}): consistency-based signals achieve strong quality estimation ($\\rho$ up to 0.45, AUROC up to 0.82) but fail at sample selection despite substantial oracle headroom.\nFour of five signals are instance-level by construction---this is definitional, not empirical.\nBoth per-sample mechanisms that could bridge the gap fail: MBR utility correlates with F1 across instances but not within them (\\S\\ref{sec:discussion}), and log-probability scores are severely compressed within instances, though where compression is mitigated, selection recovers significant gains (\\S\\ref{sec:ablation}).",
  "new_string": "All experiments use constrained decoding \\cite{willard2023guided}, the standard for schema-compliant IE output.\\footnote{Our free-form ablation (\\S\\ref{sec:ablation}) confirms fine-tuned models produce 99.95\\% valid JSON without grammar constraints.}\n\nOur central finding is the \\textbf{correlation-selection gap} (Figure~\\ref{fig:overview}): consistency signals achieve strong quality estimation ($\\rho$ up to 0.45) but fail at sample selection despite substantial oracle headroom.\nFour of five signals are instance-level by construction; log-probability, the only per-sample signal, is too compressed to discriminate (\\S\\ref{sec:discussion}), though where compression is mitigated, selection recovers gains (\\S\\ref{sec:ablation})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff73a7db-41bb-46dc-96ed-76f8874a8939",
  "isSidechain": false,
  "requestId": "req_011Cb4nD2qx1ruqA8o3Q1Uz3",
  "type": "assistant",
  "uuid": "eaa3d911-a76c-42ad-856e-4eb9da711831",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NGW9rZU9gdzZtPiCUhCsra",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 856,
      "cache_read_input_tokens": 152557,
      "output_tokens": 5327,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 856,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5327,
          "cache_read_input_tokens": 152557,
          "cache_creation_input_tokens": 856,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 856
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

_source line 6134 · 2026-05-15T17:54:08.700Z_

<details><summary>↩ Tool result · `toolu_01G64Rzrr92PDDywVNp7UitZ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eaa3d911-a76c-42ad-856e-4eb9da711831",
  "isSidechain": false,
  "promptId": "4ab6fc0d-e7b3-4753-81c9-824338d4b6fc",
  "type": "user",
  "uuid": "a7d70760-5165-42c6-a47a-b27dc0d0ce2f",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex",
    "oldString": "Structured IE requires schema-compliant output, making constrained decoding \\cite{willard2023guided} the standard inference strategy---without it, a substantial fraction of outputs from general-purpose models are unparseable.\\footnote{Fine-tuned models may retain format compliance without grammar constraints: our free-form ablation achieves 99.95\\% valid JSON rate (\\S\\ref{sec:ablation}).}\nAll experiments use constrained decoding, the regime under which structured IE is practically deployed.\n\nOur central finding is the \\textbf{correlation-selection gap} (Figure~\\ref{fig:overview}): consistency-based signals achieve strong quality estimation ($\\rho$ up to 0.45, AUROC up to 0.82) but fail at sample selection despite substantial oracle headroom.\nFour of five signals are instance-level by construction---this is definitional, not empirical.\nBoth per-sample mechanisms that could bridge the gap fail: MBR utility correlates with F1 across instances but not within them (\\S\\ref{sec:discussion}), and log-probability scores are severely compressed within instances, though where compression is mitigated, selection recovers significant gains (\\S\\ref{sec:ablation}).",
    "newString": "All experiments use constrained decoding \\cite{willard2023guided}, the standard for schema-compliant IE output.\\footnote{Our free-form ablation (\\S\\ref{sec:ablation}) confirms fine-tuned models produce 99.95\\% valid JSON without grammar constraints.}\n\nOur central finding is the \\textbf{correlation-selection gap} (Figure~\\ref{fig:overview}): consistency signals achieve strong quality estimation ($\\rho$ up to 0.45) but fail at sample selection despite substantial oracle headroom.\nFour of five signals are instance-level by construction; log-probability, the only per-sample signal, is too compressed to discriminate (\\S\\ref{sec:discussion}), though where compression is mitigated, selection recovers gains (\\S\\ref{sec:ablation}).",
    "originalFile": "\\section{Introduction}\\label{sec:introduction}\n\nSelf-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.\nOn discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K (PaLM-540B; \\citealp{wang2023selfconsistency}).\nMore broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \\cite{snell2025scaling, brown2024monkeys}.\nThese results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.\nFor tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.\nBut information extraction (IE) poses a structurally different challenge.\nThe output is not a single token or number; it is a \\textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.\nThere is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.\nCan self-consistency still provide useful signal in this structured setting?\n\nPrior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \\textit{quality estimation} (which inputs does the model handle reliably?) and \\textit{sample selection} (which of $N$ outputs is best?).\nThese require different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.\nSelf-consistency methods for discrete answers \\cite{wang2023selfconsistency, chen2024usc} and weighted variants \\cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.\nThe most relevant study, \\citet{yao2026consistency}, examines consistency--accuracy correlations for LLM-based IE, finding results that our quality-estimation analysis corroborates.\nOur work complements theirs in three directions: (i)~structural matching beyond surface-level agreement, (ii)~testing whether quality estimation translates to best-of-$N$ selection (it does not), and (iii)~a difficulty gradient revealing non-obvious findings invisible on a single dataset.\n\nStructured IE requires schema-compliant output, making constrained decoding \\cite{willard2023guided} the standard inference strategy---without it, a substantial fraction of outputs from general-purpose models are unparseable.\\footnote{Fine-tuned models may retain format compliance without grammar constraints: our free-form ablation achieves 99.95\\% valid JSON rate (\\S\\ref{sec:ablation}).}\nAll experiments use constrained decoding, the regime under which structured IE is practically deployed.\n\nOur central finding is the \\textbf{correlation-selection gap} (Figure~\\ref{fig:overview}): consistency-based signals achieve strong quality estimation ($\\rho$ up to 0.45, AUROC up to 0.82) but fail at sample selection despite substantial oracle headroom.\nFour of five signals are instance-level by construction---this is definitional, not empirical.\nBoth per-sample mechanisms that could bridge the gap fail: MBR utility correlates with F1 across instances but not within them (\\S\\ref{sec:discussion}), and log-probability scores are severely compressed within instances, though where compression is mitigated, selection recovers significant gains (\\S\\ref{sec:ablation}).\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_overview}\n\\caption{The correlation-selection gap. \\textbf{Left}: high inter-sample agreement correlates with high F1 (quality estimation). \\textbf{Right}: instance-level signals assign identical scores to all candidates, precluding sample selection.}\n\\label{fig:overview}\n\\end{figure*}\n\nWe systematically compare five confidence signals from three families---structural (entity voting confidence [VC], Soft Jaccard [SJ]), surface (exact match [EM], Fleiss' $\\kappa$ [FK]), and model-internal (log-probability [LP])---across NER and RE on SciERC \\cite{luan2018scierc}, CoNLL-2003 \\cite{tjongkimsang2003conll}, and WNUT-17 \\cite{derczynski2017wnut}, using Qwen3-8B and LLaMA-3.1-8B.\nOur contributions are:\n\\begin{enumerate}\n    \\item \\textbf{Metric dissociation.}\n    We find that quality estimation ($\\rho$), binary discrimination (AUROC), and sample selection (best-of-$N$ F1) decouple: different signals lead on different metrics, so single-metric evaluation risks selecting the wrong signal for the intended use case.\n\n    \\item \\textbf{The correlation-selection gap.}\n    Despite strong quality estimation, no signal significantly improves sample selection despite substantial oracle headroom: log-probability scores are too compressed within instances to discriminate among candidates, and MBR-style consensus-proximity selection correlates with F1 across instances but not within them.\n\n    \\item \\textbf{Difficulty- and task-dependent signal rankings.}\n    Signal rankings shift with task complexity and task type---structural signals lead on NER while LP leads on RE---and collapse at the capability boundary (WNUT-17).\n    NER findings span three datasets; RE conclusions rest on SciERC alone (preliminary).\n\\end{enumerate}\n\n",
    "structuredPatch": [
      {
        "oldStart": 16,
        "oldLines": 12,
        "newStart": 16,
        "newLines": 10,
        "lines": [
          " The most relevant study, \\citet{yao2026consistency}, examines consistency--accuracy correlations for LLM-based IE, finding results that our quality-estimation analysis corroborates.",
          " Our work complements theirs in three directions: (i)~structural matching beyond surface-level agreement, (ii)~testing whether quality estimation translates to best-of-$N$ selection (it does not), and (iii)~a difficulty gradient revealing non-obvious findings invisible on a single dataset.",
          " ",
          "-Structured IE requires schema-compliant output, making constrained decoding \\cite{willard2023guided} the standard inference strategy---without it, a substantial fraction of outputs from general-purpose models are unparseable.\\footnote{Fine-tuned models may retain format compliance without grammar constraints: our free-form ablation achieves 99.95\\% valid JSON rate (\\S\\ref{sec:ablation}).}",
          "-All experiments use constrained decoding, the regime under which structured IE is practically deployed.",
          "+All experiments use constrained decoding \\cite{willard2023guided}, the standard for schema-compliant IE output.\\footnote{Our free-form ablation (\\S\\ref{sec:ablation}) confirms fine-tuned models produce 99.95\\% valid JSON without grammar constraints.}",
          " ",
          "-Our central finding is the \\textbf{correlation-selection gap} (Figure~\\ref{fig:overview}): consistency-based signals achieve strong quality estimation ($\\rho$ up to 0.45, AUROC up to 0.82) but fail at sample selection despite substantial oracle headroom.",
          "-Four of five signals are instance-level by construction---this is definitional, not empirical.",
          "-Both per-sample mechanisms that could bridge the gap fail: MBR utility correlates with F1 across instances but not within them (\\S\\ref{sec:discussion}), and log-probability scores are severely compressed within instances, though where compression is mitigated, selection recovers significant gains (\\S\\ref{sec:ablation}).",
          "+Our central finding is the \\textbf{correlation-selection gap} (Figure~\\ref{fig:overview}): consistency signals achieve strong quality estimation ($\\rho$ up to 0.45) but fail at sample selection despite substantial oracle headroom.",
          "+Four of five signals are instance-level by construction; log-probability, the only per-sample signal, is too compressed to discriminate (\\S\\ref{sec:discussion}), though where compression is mitigated, selection recovers gains (\\S\\ref{sec:ablation}).",
          " ",
          " \\begin{figure*}[t]",
          " \\centering"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "eaa3d911-a76c-42ad-856e-4eb9da711831",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite"
}
```

</details>

---


### Runtime record

_source line 6135_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] [Patch] Round 8 高优先写作修复——不依赖正在跑的实验，立即处理。  按优先级排序：  ## 1. R8-N1 页数压缩至 ≤8 页（CRITICAL，desk-rejection 风险） 当前估计 10-11 页正文。压缩策略： - Discussion free-form ablation 详述移至 Appendix（~0.5 页） - Robustn…",
  "leafUuid": "a7d70760-5165-42c6-a47a-b27dc0d0ce2f",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6"
}
```

---


### Runtime record

_source line 6136_

```json
{
  "type": "ai-title",
  "aiTitle": "Set up agent communication with Director",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6"
}
```

---


### Tool call

_source line 6137 · 2026-05-15T17:54:15.067Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01YQ7E8Ad1RKpqadHgwnK3aS`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex",
  "old_string": "    \\item \\textbf{Metric dissociation.}\n    We find that quality estimation ($\\rho$), binary discrimination (AUROC), and sample selection (best-of-$N$ F1) decouple: different signals lead on different metrics, so single-metric evaluation risks selecting the wrong signal for the intended use case.\n\n    \\item \\textbf{The correlation-selection gap.}\n    Despite strong quality estimation, no signal significantly improves sample selection despite substantial oracle headroom: log-probability scores are too compressed within instances to discriminate among candidates, and MBR-style consensus-proximity selection correlates with F1 across instances but not within them.\n\n    \\item \\textbf{Difficulty- and task-dependent signal rankings.}\n    Signal rankings shift with task complexity and task type---structural signals lead on NER while LP leads on RE---and collapse at the capability boundary (WNUT-17).\n    NER findings span three datasets; RE conclusions rest on SciERC alone (preliminary).",
  "new_string": "    \\item \\textbf{Metric dissociation.}\n    We find that quality estimation, binary discrimination, and sample selection decouple, so single-metric evaluation risks selecting the wrong signal.\n\n    \\item \\textbf{The correlation-selection gap.}\n    Despite strong quality estimation, no signal significantly improves sample selection: LP scores are too compressed within instances, and MBR-style selection correlates with F1 across but not within instances.\n\n    \\item \\textbf{Difficulty- and task-dependent signal rankings.}\n    Signal rankings shift with task complexity and type, and collapse at the capability boundary. RE conclusions rest on SciERC alone (preliminary)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7d70760-5165-42c6-a47a-b27dc0d0ce2f",
  "isSidechain": false,
  "requestId": "req_011Cb4nMeY2NkLyJwdhSvZaN",
  "type": "assistant",
  "uuid": "56360a1c-bc6b-4906-9517-ea70338f26c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019evSnf2EkCPWjc5ZFTyJGx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5377,
      "cache_read_input_tokens": 153413,
      "output_tokens": 526,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5377,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 526,
          "cache_read_input_tokens": 153413,
          "cache_creation_input_tokens": 5377,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5377
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

_source line 6138 · 2026-05-15T17:54:15.078Z_

<details><summary>↩ Tool result · `toolu_01YQ7E8Ad1RKpqadHgwnK3aS`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "56360a1c-bc6b-4906-9517-ea70338f26c2",
  "isSidechain": false,
  "promptId": "4ab6fc0d-e7b3-4753-81c9-824338d4b6fc",
  "type": "user",
  "uuid": "6e48a055-0088-4ebd-a3e5-e48a21f080f5",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex",
    "oldString": "    \\item \\textbf{Metric dissociation.}\n    We find that quality estimation ($\\rho$), binary discrimination (AUROC), and sample selection (best-of-$N$ F1) decouple: different signals lead on different metrics, so single-metric evaluation risks selecting the wrong signal for the intended use case.\n\n    \\item \\textbf{The correlation-selection gap.}\n    Despite strong quality estimation, no signal significantly improves sample selection despite substantial oracle headroom: log-probability scores are too compressed within instances to discriminate among candidates, and MBR-style consensus-proximity selection correlates with F1 across instances but not within them.\n\n    \\item \\textbf{Difficulty- and task-dependent signal rankings.}\n    Signal rankings shift with task complexity and task type---structural signals lead on NER while LP leads on RE---and collapse at the capability boundary (WNUT-17).\n    NER findings span three datasets; RE conclusions rest on SciERC alone (preliminary).",
    "newString": "    \\item \\textbf{Metric dissociation.}\n    We find that quality estimation, binary discrimination, and sample selection decouple, so single-metric evaluation risks selecting the wrong signal.\n\n    \\item \\textbf{The correlation-selection gap.}\n    Despite strong quality estimation, no signal significantly improves sample selection: LP scores are too compressed within instances, and MBR-style selection correlates with F1 across but not within instances.\n\n    \\item \\textbf{Difficulty- and task-dependent signal rankings.}\n    Signal rankings shift with task complexity and type, and collapse at the capability boundary. RE conclusions rest on SciERC alone (preliminary).",
    "originalFile": "\\section{Introduction}\\label{sec:introduction}\n\nSelf-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.\nOn discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K (PaLM-540B; \\citealp{wang2023selfconsistency}).\nMore broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \\cite{snell2025scaling, brown2024monkeys}.\nThese results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.\nFor tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.\nBut information extraction (IE) poses a structurally different challenge.\nThe output is not a single token or number; it is a \\textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.\nThere is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.\nCan self-consistency still provide useful signal in this structured setting?\n\nPrior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \\textit{quality estimation} (which inputs does the model handle reliably?) and \\textit{sample selection} (which of $N$ outputs is best?).\nThese require different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.\nSelf-consistency methods for discrete answers \\cite{wang2023selfconsistency, chen2024usc} and weighted variants \\cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.\nThe most relevant study, \\citet{yao2026consistency}, examines consistency--accuracy correlations for LLM-based IE, finding results that our quality-estimation analysis corroborates.\nOur work complements theirs in three directions: (i)~structural matching beyond surface-level agreement, (ii)~testing whether quality estimation translates to best-of-$N$ selection (it does not), and (iii)~a difficulty gradient revealing non-obvious findings invisible on a single dataset.\n\nAll experiments use constrained decoding \\cite{willard2023guided}, the standard for schema-compliant IE output.\\footnote{Our free-form ablation (\\S\\ref{sec:ablation}) confirms fine-tuned models produce 99.95\\% valid JSON without grammar constraints.}\n\nOur central finding is the \\textbf{correlation-selection gap} (Figure~\\ref{fig:overview}): consistency signals achieve strong quality estimation ($\\rho$ up to 0.45) but fail at sample selection despite substantial oracle headroom.\nFour of five signals are instance-level by construction; log-probability, the only per-sample signal, is too compressed to discriminate (\\S\\ref{sec:discussion}), though where compression is mitigated, selection recovers gains (\\S\\ref{sec:ablation}).\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_overview}\n\\caption{The correlation-selection gap. \\textbf{Left}: high inter-sample agreement correlates with high F1 (quality estimation). \\textbf{Right}: instance-level signals assign identical scores to all candidates, precluding sample selection.}\n\\label{fig:overview}\n\\end{figure*}\n\nWe systematically compare five confidence signals from three families---structural (entity voting confidence [VC], Soft Jaccard [SJ]), surface (exact match [EM], Fleiss' $\\kappa$ [FK]), and model-internal (log-probability [LP])---across NER and RE on SciERC \\cite{luan2018scierc}, CoNLL-2003 \\cite{tjongkimsang2003conll}, and WNUT-17 \\cite{derczynski2017wnut}, using Qwen3-8B and LLaMA-3.1-8B.\nOur contributions are:\n\\begin{enumerate}\n    \\item \\textbf{Metric dissociation.}\n    We find that quality estimation ($\\rho$), binary discrimination (AUROC), and sample selection (best-of-$N$ F1) decouple: different signals lead on different metrics, so single-metric evaluation risks selecting the wrong signal for the intended use case.\n\n    \\item \\textbf{The correlation-selection gap.}\n    Despite strong quality estimation, no signal significantly improves sample selection despite substantial oracle headroom: log-probability scores are too compressed within instances to discriminate among candidates, and MBR-style consensus-proximity selection correlates with F1 across instances but not within them.\n\n    \\item \\textbf{Difficulty- and task-dependent signal rankings.}\n    Signal rankings shift with task complexity and task type---structural signals lead on NER while LP leads on RE---and collapse at the capability boundary (WNUT-17).\n    NER findings span three datasets; RE conclusions rest on SciERC alone (preliminary).\n\\end{enumerate}\n\n",
    "structuredPatch": [
      {
        "oldStart": 32,
        "oldLines": 13,
        "newStart": 32,
        "newLines": 12,
        "lines": [
          " Our contributions are:",
          " \\begin{enumerate}",
          "     \\item \\textbf{Metric dissociation.}",
          "-    We find that quality estimation ($\\rho$), binary discrimination (AUROC), and sample selection (best-of-$N$ F1) decouple: different signals lead on different metrics, so single-metric evaluation risks selecting the wrong signal for the intended use case.",
          "+    We find that quality estimation, binary discrimination, and sample selection decouple, so single-metric evaluation risks selecting the wrong signal.",
          " ",
          "     \\item \\textbf{The correlation-selection gap.}",
          "-    Despite strong quality estimation, no signal significantly improves sample selection despite substantial oracle headroom: log-probability scores are too compressed within instances to discriminate among candidates, and MBR-style consensus-proximity selection correlates with F1 across instances but not within them.",
          "+    Despite strong quality estimation, no signal significantly improves sample selection: LP scores are too compressed within instances, and MBR-style selection correlates with F1 across but not within instances.",
          " ",
          "     \\item \\textbf{Difficulty- and task-dependent signal rankings.}",
          "-    Signal rankings shift with task complexity and task type---structural signals lead on NER while LP leads on RE---and collapse at the capability boundary (WNUT-17).",
          "-    NER findings span three datasets; RE conclusions rest on SciERC alone (preliminary).",
          "+    Signal rankings shift with task complexity and type, and collapse at the capability boundary. RE conclusions rest on SciERC alone (preliminary).",
          " \\end{enumerate}",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "56360a1c-bc6b-4906-9517-ea70338f26c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite"
}
```

</details>

---


### Assistant

_source line 6139 · 2026-05-15T17:54:18.179Z_

**Experiments 压缩 — thinking tokens + seed variability + QE≠selection：**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e48a055-0088-4ebd-a3e5-e48a21f080f5",
  "isSidechain": false,
  "requestId": "req_011Cb4nN7pqrn4EZTyiqjctu",
  "type": "assistant",
  "uuid": "8f230003-6119-48a4-90c2-357a85a11f0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ikPjsDyGHg9L7y9hoK7qw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 583,
      "cache_read_input_tokens": 158790,
      "output_tokens": 494,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 583,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 494,
          "cache_read_input_tokens": 158790,
          "cache_creation_input_tokens": 583,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 583
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


### Tool call

_source line 6140 · 2026-05-15T17:54:21.664Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01RKfDMiihGNaVv18zke3itW`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
  "old_string": "We note a training confound for SciERC: Qwen3-8B's SciERC checkpoint was trained with \\texttt{enable\\_thinking=True} (LLaMA Factory 0.9.4 default), which prepends empty \\texttt{&lt;think>\\textbackslash n&lt;/think>} blocks (4--5 tokens) to each training response and includes them in the loss computation; CoNLL-2003 and WNUT-17 checkpoints explicitly set \\texttt{enable\\_thinking=False}.\nNo reasoning content is present (the blocks are always empty), and constrained decoding at inference time enforces JSON-only output, so thinking tokens do not appear in generated samples.\nThis constitutes a minor train--test distribution mismatch for SciERC ($<$0.3\\% of the 2048-token training window); CoNLL-2003 and WNUT-17 are unaffected.\nWe discuss implications in the Limitations section.",
  "new_string": "Qwen3-8B's SciERC checkpoint has a minor train--test mismatch: empty \\texttt{&lt;think>&lt;/think>} blocks (4--5 tokens, no reasoning content) were included in training but are suppressed by constrained decoding at inference; CoNLL and WNUT-17 are unaffected.\nA quantitative analysis rules out this confound (Appendix~\\ref{app:thinking_token})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f230003-6119-48a4-90c2-357a85a11f0a",
  "isSidechain": false,
  "requestId": "req_011Cb4nN7pqrn4EZTyiqjctu",
  "type": "assistant",
  "uuid": "caf3edd3-f589-421c-bd31-48e595c70182",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ikPjsDyGHg9L7y9hoK7qw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 583,
      "cache_read_input_tokens": 158790,
      "output_tokens": 494,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 583,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 494,
          "cache_read_input_tokens": 158790,
          "cache_creation_input_tokens": 583,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 583
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

_source line 6141 · 2026-05-15T17:54:21.678Z_

<details><summary>↩ Tool result · `toolu_01RKfDMiihGNaVv18zke3itW`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "caf3edd3-f589-421c-bd31-48e595c70182",
  "isSidechain": false,
  "promptId": "4ab6fc0d-e7b3-4753-81c9-824338d4b6fc",
  "type": "user",
  "uuid": "54afc4b5-14ea-4bfc-ba28-1ad435aa29ba",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
    "oldString": "We note a training confound for SciERC: Qwen3-8B's SciERC checkpoint was trained with \\texttt{enable\\_thinking=True} (LLaMA Factory 0.9.4 default), which prepends empty \\texttt{&lt;think>\\textbackslash n&lt;/think>} blocks (4--5 tokens) to each training response and includes them in the loss computation; CoNLL-2003 and WNUT-17 checkpoints explicitly set \\texttt{enable\\_thinking=False}.\nNo reasoning content is present (the blocks are always empty), and constrained decoding at inference time enforces JSON-only output, so thinking tokens do not appear in generated samples.\nThis constitutes a minor train--test distribution mismatch for SciERC ($<$0.3\\% of the 2048-token training window); CoNLL-2003 and WNUT-17 are unaffected.\nWe discuss implications in the Limitations section.",
    "newString": "Qwen3-8B's SciERC checkpoint has a minor train--test mismatch: empty \\texttt{&lt;think>&lt;/think>} blocks (4--5 tokens, no reasoning content) were included in training but are suppressed by constrained decoding at inference; CoNLL and WNUT-17 are unaffected.\nA quantitative analysis rules out this confound (Appendix~\\ref{app:thinking_token}).",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 12,
        "oldLines": 10,
        "newStart": 12,
        "newLines": 8,
        "lines": [
          " ",
          " \\paragraph{Models and sampling.}",
          " Both \\textbf{Qwen3-8B} and \\textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\\alpha{=}64$) for 5 epochs using LLaMA Factory \\cite{zheng2024llamafactory} under identical training procedures, ensuring comparisons across the two model families (both at 8B scale) reflect model differences rather than training confounds.",
          "-We note a training confound for SciERC: Qwen3-8B's SciERC checkpoint was trained with \\texttt{enable\\_thinking=True} (LLaMA Factory 0.9.4 default), which prepends empty \\texttt{&lt;think>\\textbackslash n&lt;/think>} blocks (4--5 tokens) to each training response and includes them in the loss computation; CoNLL-2003 and WNUT-17 checkpoints explicitly set \\texttt{enable\\_thinking=False}.",
          "-No reasoning content is present (the blocks are always empty), and constrained decoding at inference time enforces JSON-only output, so thinking tokens do not appear in generated samples.",
          "-This constitutes a minor train--test distribution mismatch for SciERC ($<$0.3\\% of the 2048-token training window); CoNLL-2003 and WNUT-17 are unaffected.",
          "-We discuss implications in the Limitations section.",
          "+Qwen3-8B's SciERC checkpoint has a minor train--test mismatch: empty \\texttt{&lt;think>&lt;/think>} blocks (4--5 tokens, no reasoning content) were included in training but are suppressed by constrained decoding at inference; CoNLL and WNUT-17 are unaffected.",
          "+A quantitative analysis rules out this confound (Appendix~\\ref{app:thinking_token}).",
          " We draw $N{=}8$ samples at $T{=}1.0$ (primary; single seed, seed${=}42$), with $N{=}16$ for scaling experiments.\\footnote{$N{=}8$ establishes the primary baseline at minimal compute cost; $N{=}16$ with multiple seeds verifies scaling behavior. $N$-scaling analysis (Appendix~\\ref{app:n_scaling}) shows sublinear gains beyond $N{=}8$. $N{=}16$ results in Table~\\ref{tab:robustness} (Appendix~\\ref{app:robustness}); 3-seed stability ($\\sigma{\\leq}0.026$; Table~\\ref{tab:multiseed}, Appendix~\\ref{app:multiseed}) confirms identical signal rankings across seeds.}",
          " Quality estimation uses Spearman $\\rho$ and AUROC; downstream utility uses best-of-$N$ selection macro F1 (instance-averaged) with exact span matching (NER) and head-tail-label matching (RE).",
          " Inference uses vLLM with constrained decoding \\cite{willard2023guided}."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "caf3edd3-f589-421c-bd31-48e595c70182",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite"
}
```

</details>

---


### Runtime record

_source line 6142 · 2026-05-15T17:54:21.721Z_

```json
{
  "parentUuid": "54afc4b5-14ea-4bfc-ba28-1ad435aa29ba",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "62e815fb-3e27-4cd7-aaf8-0f75b00b565d",
  "timestamp": "2026-05-15T17:54:21.721Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite"
}
```

---


### Tool call

_source line 6143 · 2026-05-15T17:54:32.026Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01LKmEnr1FHEnHf1ZdHMpcji`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
  "old_string": "\\paragraph{Seed variability.}\nIndividual seeds exhibit notable variance---even the most favorable seed falls short of significance ($p{=}0.19$)---motivating our multi-seed design.\n\n\\paragraph{Quality estimation $\\neq$ output selection.}\nInstance-level confidence signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} among $N$ candidates is best.\nWhen per-sample variance is low relative to instance-level difficulty, even perfect quality estimation cannot discriminate among near-identical candidates.\nThis gap has direct consequences for test-time scaling in IE \\cite{brown2024monkeys, snell2025scaling}: closing it likely requires per-sample signals such as trained verifiers \\cite{cobbe2021verifiers}.",
  "new_string": "\\paragraph{Quality estimation $\\neq$ output selection.}\nInstance-level signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} is best; when per-sample variance is low, even perfect quality estimation fails to discriminate.\nIndividual seeds exhibit notable variance (even the best seed $p{=}0.19$), motivating multi-seed evaluation.\nClosing this gap likely requires per-sample signals such as trained verifiers \\cite{cobbe2021verifiers}."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62e815fb-3e27-4cd7-aaf8-0f75b00b565d",
  "isSidechain": false,
  "requestId": "req_011Cb4nNc6xJohnL9Si1vA4B",
  "type": "assistant",
  "uuid": "16c7afd9-680c-4f80-8afa-a932d30bc5d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YbHNExyZ1YXdXBaj2LnQQi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 655,
      "cache_read_input_tokens": 159373,
      "output_tokens": 435,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 655,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 435,
          "cache_read_input_tokens": 159373,
          "cache_creation_input_tokens": 655,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 655
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

_source line 6144 · 2026-05-15T17:54:32.037Z_

<details><summary>↩ Tool result · `toolu_01LKmEnr1FHEnHf1ZdHMpcji`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "16c7afd9-680c-4f80-8afa-a932d30bc5d6",
  "isSidechain": false,
  "promptId": "4ab6fc0d-e7b3-4753-81c9-824338d4b6fc",
  "type": "user",
  "uuid": "971a6906-e991-4f87-b2ed-ca36bf879f37",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
    "oldString": "\\paragraph{Seed variability.}\nIndividual seeds exhibit notable variance---even the most favorable seed falls short of significance ($p{=}0.19$)---motivating our multi-seed design.\n\n\\paragraph{Quality estimation $\\neq$ output selection.}\nInstance-level confidence signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} among $N$ candidates is best.\nWhen per-sample variance is low relative to instance-level difficulty, even perfect quality estimation cannot discriminate among near-identical candidates.\nThis gap has direct consequences for test-time scaling in IE \\cite{brown2024monkeys, snell2025scaling}: closing it likely requires per-sample signals such as trained verifiers \\cite{cobbe2021verifiers}.",
    "newString": "\\paragraph{Quality estimation $\\neq$ output selection.}\nInstance-level signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} is best; when per-sample variance is low, even perfect quality estimation fails to discriminate.\nIndividual seeds exhibit notable variance (even the best seed $p{=}0.19$), motivating multi-seed evaluation.\nClosing this gap likely requires per-sample signals such as trained verifiers \\cite{cobbe2021verifiers}.",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 106,
        "oldLines": 13,
        "newStart": 106,
        "newLines": 10,
        "lines": [
          " On RE, the best signal (LP, 0.395) falls below greedy (0.404, $-0.9$\\,pp; single seed, preliminary), while 18.1~pp of oracle headroom remains.",
          " VC, the best quality estimator ($\\rho{=}0.379$), selects to only 0.623 on NER ($\\Delta{=}{-}2.2$~pp, $p{=}0.26$); the direction is consistent with CoNLL and WNUT-17 (Table~\\ref{tab:cross_selection}), though CoNLL's limited oracle headroom (${\\leq}4.0$~pp at $N{=}8$) constrains selection comparison.",
          " ",
          "-\\paragraph{Seed variability.}",
          "-Individual seeds exhibit notable variance---even the most favorable seed falls short of significance ($p{=}0.19$)---motivating our multi-seed design.",
          "-",
          " \\paragraph{Quality estimation $\\neq$ output selection.}",
          "-Instance-level confidence signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} among $N$ candidates is best.",
          "-When per-sample variance is low relative to instance-level difficulty, even perfect quality estimation cannot discriminate among near-identical candidates.",
          "-This gap has direct consequences for test-time scaling in IE \\cite{brown2024monkeys, snell2025scaling}: closing it likely requires per-sample signals such as trained verifiers \\cite{cobbe2021verifiers}.",
          "+Instance-level signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} is best; when per-sample variance is low, even perfect quality estimation fails to discriminate.",
          "+Individual seeds exhibit notable variance (even the best seed $p{=}0.19$), motivating multi-seed evaluation.",
          "+Closing this gap likely requires per-sample signals such as trained verifiers \\cite{cobbe2021verifiers}.",
          " ",
          " %% ============================================================",
          " \\subsection{Robustness}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "16c7afd9-680c-4f80-8afa-a932d30bc5d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite"
}
```

</details>

---


### Assistant

_source line 6145 · 2026-05-15T17:54:35.625Z_

**Discussion 压缩 — ablation 移 Appendix + practical recommendations 精简：**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "971a6906-e991-4f87-b2ed-ca36bf879f37",
  "isSidechain": false,
  "requestId": "req_011Cb4nPNH2WyuNWpbTDrJej",
  "type": "assistant",
  "uuid": "f1aeb7a0-1de4-4470-a7c8-130930e94e1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LLn3zKfSzE8CFnBTFn24rd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 492,
      "cache_read_input_tokens": 160028,
      "output_tokens": 645,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 492,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 645,
          "cache_read_input_tokens": 160028,
          "cache_creation_input_tokens": 492,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 492
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


### Tool call

_source line 6146 · 2026-05-15T17:54:45.975Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01XsadimiMhUob3KFhX45JA6`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
  "old_string": "\\paragraph{Practical recommendations.}\nFor per-instance quality ranking, VC provides the strongest rank correlation ($\\rho{=}0.38$), though EM leads binary discrimination (AUROC${=}0.816$ on CoNLL); under conditional filtering, EM leads on both NER and RE ($\\rho{=}0.360$, $0.417$; RE: preliminary, single benchmark).\nSignal rankings depend on task difficulty and task type: EM dominates easy NER (CoNLL), VC and SJ dominate hard NER (SciERC); on RE, the hierarchy reverses---LP outperforms structural signals (3-seed; Table~\\ref{tab:multiseed}), likely because RE's high zero-F1 rate (40\\%) creates a binary-outcome regime where generation confidence is more discriminative than structural overlap.\nRankings are directionally consistent across two model families at 8B scale, though with model-dependent magnitude.\nAt $N{=}16$, SJ converges to VC on NER ($\\Delta{=}0.002$) with lower variance ($\\sigma{=}0.010$ vs.\\ $0.026$); when capability is insufficient (WNUT-17), all signals converge toward non-significance (Table~\\ref{tab:wnut}).",
  "new_string": "\\paragraph{Practical recommendations.}\nFor quality ranking, VC leads on hard NER ($\\rho{=}0.38$) while EM leads easy NER and binary discrimination (AUROC${=}0.816$, CoNLL); on RE (preliminary), LP outperforms structural signals (Table~\\ref{tab:multiseed}), likely because RE's 40\\% zero-F1 rate favors generation confidence.\nRankings are consistent across two 8B-scale model families; at $N{=}16$, SJ converges to VC (Appendix~\\ref{app:robustness}); at the capability boundary (WNUT-17), all signals collapse (Table~\\ref{tab:wnut})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1aeb7a0-1de4-4470-a7c8-130930e94e1c",
  "isSidechain": false,
  "requestId": "req_011Cb4nPNH2WyuNWpbTDrJej",
  "type": "assistant",
  "uuid": "c2c1549e-2957-4b2e-8391-5318eba1d7a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LLn3zKfSzE8CFnBTFn24rd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 492,
      "cache_read_input_tokens": 160028,
      "output_tokens": 645,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 492,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 645,
          "cache_read_input_tokens": 160028,
          "cache_creation_input_tokens": 492,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 492
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

_source line 6147 · 2026-05-15T17:54:45.989Z_

<details><summary>↩ Tool result · `toolu_01XsadimiMhUob3KFhX45JA6`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2c1549e-2957-4b2e-8391-5318eba1d7a4",
  "isSidechain": false,
  "promptId": "4ab6fc0d-e7b3-4753-81c9-824338d4b6fc",
  "type": "user",
  "uuid": "cfa8007e-2af5-47d0-b846-fe6d59a10167",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
    "oldString": "\\paragraph{Practical recommendations.}\nFor per-instance quality ranking, VC provides the strongest rank correlation ($\\rho{=}0.38$), though EM leads binary discrimination (AUROC${=}0.816$ on CoNLL); under conditional filtering, EM leads on both NER and RE ($\\rho{=}0.360$, $0.417$; RE: preliminary, single benchmark).\nSignal rankings depend on task difficulty and task type: EM dominates easy NER (CoNLL), VC and SJ dominate hard NER (SciERC); on RE, the hierarchy reverses---LP outperforms structural signals (3-seed; Table~\\ref{tab:multiseed}), likely because RE's high zero-F1 rate (40\\%) creates a binary-outcome regime where generation confidence is more discriminative than structural overlap.\nRankings are directionally consistent across two model families at 8B scale, though with model-dependent magnitude.\nAt $N{=}16$, SJ converges to VC on NER ($\\Delta{=}0.002$) with lower variance ($\\sigma{=}0.010$ vs.\\ $0.026$); when capability is insufficient (WNUT-17), all signals converge toward non-significance (Table~\\ref{tab:wnut}).",
    "newString": "\\paragraph{Practical recommendations.}\nFor quality ranking, VC leads on hard NER ($\\rho{=}0.38$) while EM leads easy NER and binary discrimination (AUROC${=}0.816$, CoNLL); on RE (preliminary), LP outperforms structural signals (Table~\\ref{tab:multiseed}), likely because RE's 40\\% zero-F1 rate favors generation confidence.\nRankings are consistent across two 8B-scale model families; at $N{=}16$, SJ converges to VC (Appendix~\\ref{app:robustness}); at the capability boundary (WNUT-17), all signals collapse (Table~\\ref{tab:wnut}).",
    "originalFile": "\\section{Discussion}\\label{sec:discussion}\n\n\\paragraph{Practical recommendations.}\nFor per-instance quality ranking, VC provides the strongest rank correlation ($\\rho{=}0.38$), though EM leads binary discrimination (AUROC${=}0.816$ on CoNLL); under conditional filtering, EM leads on both NER and RE ($\\rho{=}0.360$, $0.417$; RE: preliminary, single benchmark).\nSignal rankings depend on task difficulty and task type: EM dominates easy NER (CoNLL), VC and SJ dominate hard NER (SciERC); on RE, the hierarchy reverses---LP outperforms structural signals (3-seed; Table~\\ref{tab:multiseed}), likely because RE's high zero-F1 rate (40\\%) creates a binary-outcome regime where generation confidence is more discriminative than structural overlap.\nRankings are directionally consistent across two model families at 8B scale, though with model-dependent magnitude.\nAt $N{=}16$, SJ converges to VC on NER ($\\Delta{=}0.002$) with lower variance ($\\sigma{=}0.010$ vs.\\ $0.026$); when capability is insufficient (WNUT-17), all signals converge toward non-significance (Table~\\ref{tab:wnut}).\n\n\\paragraph{Why the gap exists: two layers.}\n\\textit{Layer 1 (definitional):} Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.\nConsensus-proximity selection (\\S\\ref{sec:evaluation}) does not recover per-sample discrimination (Table~\\ref{tab:selection}).\n\\textit{Layer 2 (score compression):} Log-probability, the only per-sample signal, also fails to exploit the oracle headroom.\nLP scores are severely compressed: the median within-instance LP range is only 0.041 nats, and the CDF rises smoothly with no bimodal split (Figure~\\ref{fig:lp_range_cdf}, Table~\\ref{tab:logprob_ties}).\nIn instances with above-median LP spread ($n{=}210$), LP \\textit{significantly} outperforms greedy ($+2.9$~pp, $p{=}0.004$; $\\varepsilon$ sensitivity in Table~\\ref{tab:epsilon_sweep}), confirming score compression as the primary bottleneck; a free-form ablation (\\S\\ref{sec:ablation}) shows this persists without constrained decoding.\nThe gap holds even among high-diversity instances (Appendix~\\ref{app:diversity}).\nNotably, LP compression's impact on quality estimation is task-dependent: despite identical compression levels, LP provides stronger QE on RE than on NER (Table~\\ref{tab:multiseed}), because RE's binary-outcome regime makes even compressed generation confidence more informative than structural overlap; this does not translate to selection gains on either task.\n\n\\paragraph{The gap widens with $N$.}\nDoubling from $N{=}8$ to $N{=}16$ expands oracle headroom by $+4.4$~pp, yet SJ---the strongest quality estimator at $N{=}16$ ($\\rho{=}0.411$)---selects to $-0.05$~pp below greedy, LP improves by only $+0.4$~pp, and VC deteriorates ($\\Delta$: $-2.2{\\to}{-}3.1$~pp); on RE at $N{=}16$ (preliminary), all consistency signals fall below greedy while LP is the sole positive signal ($\\Delta{=}{+}0.7$~pp, $p{=}0.058$; Table~\\ref{tab:re_n16_selection}).\nThe gap is not a small-$N$ artifact; detailed $N$-scaling analysis in Appendix~\\ref{app:n_scaling}.\n\n\\paragraph{Ablation: free-form decoding.}\\label{sec:ablation}\nA natural objection is that constrained decoding artificially suppresses LP score variation by restricting the output space.\nWe test this with a controlled ablation on SciERC (Qwen3-8B, $N{=}8$, $T{=}1.0$): grammar constraints are removed entirely and outputs are parsed post-hoc.\nThe fine-tuned model produces valid JSON at 99.95\\% rate (4{,}406/4{,}408 samples), confirming format compliance without grammar enforcement.\nLP score distributions are nearly identical across regimes: within-instance standard deviation ratio is $0.97{\\times}$, and the tied fraction decreases by only $2$~pp (from 59.7\\% to 57.7\\% at $\\varepsilon{=}0.05$; Table~\\ref{tab:freeform_ablation}, Panel~A).\nNER selection gains remain negligible under both regimes (Panel~B), confirming that LP compression is intrinsic to the model's probability assignments rather than an artifact of constrained decoding.\nThis rules out constrained decoding as the primary cause of the correlation-selection gap.\n\nOur consensus-proximity selection strategies instantiate MBR decoding \\cite{eikema2022sampling, freitag2022high}; all variants fail because utility functions correlate with F1 across instances but not within them (Appendix~\\ref{app:mbr_discussion}).\nPer-signal quality estimation changes and an RE-specific selection interaction under free-form decoding are detailed in Appendix~\\ref{app:freeform_ablation}.\n\n\\paragraph{Methodological implications.}\nThe decoupling of $\\rho$, AUROC, and selection F1 means single-metric evaluation risks selecting the wrong signal.\nEffective selection likely requires per-sample signals such as trained verifiers \\cite{cobbe2021verifiers, venktesh2025trust}; $N{=}8$ captures most quality estimation benefit (Appendix~\\ref{app:n_scaling}).\nStructural signals are robust to domain shift when the training schema subsumes the target (VC $\\rho{=}0.469$ OOD vs.\\ $0.379$ in-domain; Appendix~\\ref{app:ood}).\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 10,
        "newStart": 1,
        "newLines": 8,
        "lines": [
          " \\section{Discussion}\\label{sec:discussion}",
          " ",
          " \\paragraph{Practical recommendations.}",
          "-For per-instance quality ranking, VC provides the strongest rank correlation ($\\rho{=}0.38$), though EM leads binary discrimination (AUROC${=}0.816$ on CoNLL); under conditional filtering, EM leads on both NER and RE ($\\rho{=}0.360$, $0.417$; RE: preliminary, single benchmark).",
          "-Signal rankings depend on task difficulty and task type: EM dominates easy NER (CoNLL), VC and SJ dominate hard NER (SciERC); on RE, the hierarchy reverses---LP outperforms structural signals (3-seed; Table~\\ref{tab:multiseed}), likely because RE's high zero-F1 rate (40\\%) creates a binary-outcome regime where generation confidence is more discriminative than structural overlap.",
          "-Rankings are directionally consistent across two model families at 8B scale, though with model-dependent magnitude.",
          "-At $N{=}16$, SJ converges to VC on NER ($\\Delta{=}0.002$) with lower variance ($\\sigma{=}0.010$ vs.\\ $0.026$); when capability is insufficient (WNUT-17), all signals converge toward non-significance (Table~\\ref{tab:wnut}).",
          "+For quality ranking, VC leads on hard NER ($\\rho{=}0.38$) while EM leads easy NER and binary discrimination (AUROC${=}0.816$, CoNLL); on RE (preliminary), LP outperforms structural signals (Table~\\ref{tab:multiseed}), likely because RE's 40\\% zero-F1 rate favors generation confidence.",
          "+Rankings are consistent across two 8B-scale model families; at $N{=}16$, SJ converges to VC (Appendix~\\ref{app:robustness}); at the capability boundary (WNUT-17), all signals collapse (Table~\\ref{tab:wnut}).",
          " ",
          " \\paragraph{Why the gap exists: two layers.}",
          " \\textit{Layer 1 (definitional):} Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "c2c1549e-2957-4b2e-8391-5318eba1d7a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite"
}
```

</details>

---


### Runtime record

_source line 6148_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] [Patch] Round 8 高优先写作修复——不依赖正在跑的实验，立即处理。  按优先级排序：  ## 1. R8-N1 页数压缩至 ≤8 页（CRITICAL，desk-rejection 风险） 当前估计 10-11 页正文。压缩策略： - Discussion free-form ablation 详述移至 Appendix（~0.5 页） - Robustn…",
  "leafUuid": "cfa8007e-2af5-47d0-b846-fe6d59a10167",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6"
}
```

---


### Runtime record

_source line 6149_

```json
{
  "type": "ai-title",
  "aiTitle": "Set up agent communication with Director",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6"
}
```

---


### Tool call

_source line 6150 · 2026-05-15T17:55:02.157Z_

<details open><summary>🔧 Tool call — Edit · `toolu_019zgj3xUgmzfkRMUuy7rCJA`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
  "old_string": "\\paragraph{Ablation: free-form decoding.}\\label{sec:ablation}\nA natural objection is that constrained decoding artificially suppresses LP score variation by restricting the output space.\nWe test this with a controlled ablation on SciERC (Qwen3-8B, $N{=}8$, $T{=}1.0$): grammar constraints are removed entirely and outputs are parsed post-hoc.\nThe fine-tuned model produces valid JSON at 99.95\\% rate (4{,}406/4{,}408 samples), confirming format compliance without grammar enforcement.\nLP score distributions are nearly identical across regimes: within-instance standard deviation ratio is $0.97{\\times}$, and the tied fraction decreases by only $2$~pp (from 59.7\\% to 57.7\\% at $\\varepsilon{=}0.05$; Table~\\ref{tab:freeform_ablation}, Panel~A).\nNER selection gains remain negligible under both regimes (Panel~B), confirming that LP compression is intrinsic to the model's probability assignments rather than an artifact of constrained decoding.\nThis rules out constrained decoding as the primary cause of the correlation-selection gap.\n\nOur consensus-proximity selection strategies instantiate MBR decoding \\cite{eikema2022sampling, freitag2022high}; all variants fail because utility functions correlate with F1 across instances but not within them (Appendix~\\ref{app:mbr_discussion}).\nPer-signal quality estimation changes and an RE-specific selection interaction under free-form decoding are detailed in Appendix~\\ref{app:freeform_ablation}.",
  "new_string": "\\paragraph{Ablation: free-form decoding.}\\label{sec:ablation}\nRemoving grammar constraints entirely (SciERC, Qwen3-8B) yields nearly identical LP distributions (within-instance std ratio $0.97{\\times}$, tied fraction $-2$~pp) and negligible selection changes, ruling out constrained decoding as the cause (Appendix~\\ref{app:freeform_ablation}).\nOur consensus-proximity strategies instantiate MBR decoding \\cite{eikema2022sampling}; all fail because utility correlates with F1 across instances but not within them (Appendix~\\ref{app:mbr_discussion})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cfa8007e-2af5-47d0-b846-fe6d59a10167",
  "isSidechain": false,
  "requestId": "req_011Cb4nQQ8vQp6jMNbMXyRdC",
  "type": "assistant",
  "uuid": "26d2dfd7-9757-4d34-99ed-2e7566a685e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QxMJReM7T1hnoQrHDNC9m2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 702,
      "cache_read_input_tokens": 160520,
      "output_tokens": 697,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 702,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 697,
          "cache_read_input_tokens": 160520,
          "cache_creation_input_tokens": 702,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 702
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

_source line 6151 · 2026-05-15T17:55:02.171Z_

<details><summary>↩ Tool result · `toolu_019zgj3xUgmzfkRMUuy7rCJA`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "26d2dfd7-9757-4d34-99ed-2e7566a685e6",
  "isSidechain": false,
  "promptId": "4ab6fc0d-e7b3-4753-81c9-824338d4b6fc",
  "type": "user",
  "uuid": "976b530a-637a-479d-b1dc-3ca06cc1145c",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
    "oldString": "\\paragraph{Ablation: free-form decoding.}\\label{sec:ablation}\nA natural objection is that constrained decoding artificially suppresses LP score variation by restricting the output space.\nWe test this with a controlled ablation on SciERC (Qwen3-8B, $N{=}8$, $T{=}1.0$): grammar constraints are removed entirely and outputs are parsed post-hoc.\nThe fine-tuned model produces valid JSON at 99.95\\% rate (4{,}406/4{,}408 samples), confirming format compliance without grammar enforcement.\nLP score distributions are nearly identical across regimes: within-instance standard deviation ratio is $0.97{\\times}$, and the tied fraction decreases by only $2$~pp (from 59.7\\% to 57.7\\% at $\\varepsilon{=}0.05$; Table~\\ref{tab:freeform_ablation}, Panel~A).\nNER selection gains remain negligible under both regimes (Panel~B), confirming that LP compression is intrinsic to the model's probability assignments rather than an artifact of constrained decoding.\nThis rules out constrained decoding as the primary cause of the correlation-selection gap.\n\nOur consensus-proximity selection strategies instantiate MBR decoding \\cite{eikema2022sampling, freitag2022high}; all variants fail because utility functions correlate with F1 across instances but not within them (Appendix~\\ref{app:mbr_discussion}).\nPer-signal quality estimation changes and an RE-specific selection interaction under free-form decoding are detailed in Appendix~\\ref{app:freeform_ablation}.",
    "newString": "\\paragraph{Ablation: free-form decoding.}\\label{sec:ablation}\nRemoving grammar constraints entirely (SciERC, Qwen3-8B) yields nearly identical LP distributions (within-instance std ratio $0.97{\\times}$, tied fraction $-2$~pp) and negligible selection changes, ruling out constrained decoding as the cause (Appendix~\\ref{app:freeform_ablation}).\nOur consensus-proximity strategies instantiate MBR decoding \\cite{eikema2022sampling}; all fail because utility correlates with F1 across instances but not within them (Appendix~\\ref{app:mbr_discussion}).",
    "originalFile": "\\section{Discussion}\\label{sec:discussion}\n\n\\paragraph{Practical recommendations.}\nFor quality ranking, VC leads on hard NER ($\\rho{=}0.38$) while EM leads easy NER and binary discrimination (AUROC${=}0.816$, CoNLL); on RE (preliminary), LP outperforms structural signals (Table~\\ref{tab:multiseed}), likely because RE's 40\\% zero-F1 rate favors generation confidence.\nRankings are consistent across two 8B-scale model families; at $N{=}16$, SJ converges to VC (Appendix~\\ref{app:robustness}); at the capability boundary (WNUT-17), all signals collapse (Table~\\ref{tab:wnut}).\n\n\\paragraph{Why the gap exists: two layers.}\n\\textit{Layer 1 (definitional):} Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.\nConsensus-proximity selection (\\S\\ref{sec:evaluation}) does not recover per-sample discrimination (Table~\\ref{tab:selection}).\n\\textit{Layer 2 (score compression):} Log-probability, the only per-sample signal, also fails to exploit the oracle headroom.\nLP scores are severely compressed: the median within-instance LP range is only 0.041 nats, and the CDF rises smoothly with no bimodal split (Figure~\\ref{fig:lp_range_cdf}, Table~\\ref{tab:logprob_ties}).\nIn instances with above-median LP spread ($n{=}210$), LP \\textit{significantly} outperforms greedy ($+2.9$~pp, $p{=}0.004$; $\\varepsilon$ sensitivity in Table~\\ref{tab:epsilon_sweep}), confirming score compression as the primary bottleneck; a free-form ablation (\\S\\ref{sec:ablation}) shows this persists without constrained decoding.\nThe gap holds even among high-diversity instances (Appendix~\\ref{app:diversity}).\nNotably, LP compression's impact on quality estimation is task-dependent: despite identical compression levels, LP provides stronger QE on RE than on NER (Table~\\ref{tab:multiseed}), because RE's binary-outcome regime makes even compressed generation confidence more informative than structural overlap; this does not translate to selection gains on either task.\n\n\\paragraph{The gap widens with $N$.}\nDoubling from $N{=}8$ to $N{=}16$ expands oracle headroom by $+4.4$~pp, yet SJ---the strongest quality estimator at $N{=}16$ ($\\rho{=}0.411$)---selects to $-0.05$~pp below greedy, LP improves by only $+0.4$~pp, and VC deteriorates ($\\Delta$: $-2.2{\\to}{-}3.1$~pp); on RE at $N{=}16$ (preliminary), all consistency signals fall below greedy while LP is the sole positive signal ($\\Delta{=}{+}0.7$~pp, $p{=}0.058$; Table~\\ref{tab:re_n16_selection}).\nThe gap is not a small-$N$ artifact; detailed $N$-scaling analysis in Appendix~\\ref{app:n_scaling}.\n\n\\paragraph{Ablation: free-form decoding.}\\label{sec:ablation}\nA natural objection is that constrained decoding artificially suppresses LP score variation by restricting the output space.\nWe test this with a controlled ablation on SciERC (Qwen3-8B, $N{=}8$, $T{=}1.0$): grammar constraints are removed entirely and outputs are parsed post-hoc.\nThe fine-tuned model produces valid JSON at 99.95\\% rate (4{,}406/4{,}408 samples), confirming format compliance without grammar enforcement.\nLP score distributions are nearly identical across regimes: within-instance standard deviation ratio is $0.97{\\times}$, and the tied fraction decreases by only $2$~pp (from 59.7\\% to 57.7\\% at $\\varepsilon{=}0.05$; Table~\\ref{tab:freeform_ablation}, Panel~A).\nNER selection gains remain negligible under both regimes (Panel~B), confirming that LP compression is intrinsic to the model's probability assignments rather than an artifact of constrained decoding.\nThis rules out constrained decoding as the primary cause of the correlation-selection gap.\n\nOur consensus-proximity selection strategies instantiate MBR decoding \\cite{eikema2022sampling, freitag2022high}; all variants fail because utility functions correlate with F1 across instances but not within them (Appendix~\\ref{app:mbr_discussion}).\nPer-signal quality estimation changes and an RE-specific selection interaction under free-form decoding are detailed in Appendix~\\ref{app:freeform_ablation}.\n\n\\paragraph{Methodological implications.}\nThe decoupling of $\\rho$, AUROC, and selection F1 means single-metric evaluation risks selecting the wrong signal.\nEffective selection likely requires per-sample signals such as trained verifiers \\cite{cobbe2021verifiers, venktesh2025trust}; $N{=}8$ captures most quality estimation benefit (Appendix~\\ref{app:n_scaling}).\nStructural signals are robust to domain shift when the training schema subsumes the target (VC $\\rho{=}0.469$ OOD vs.\\ $0.379$ in-domain; Appendix~\\ref{app:ood}).\n",
    "structuredPatch": [
      {
        "oldStart": 18,
        "oldLines": 16,
        "newStart": 18,
        "newLines": 9,
        "lines": [
          " The gap is not a small-$N$ artifact; detailed $N$-scaling analysis in Appendix~\\ref{app:n_scaling}.",
          " ",
          " \\paragraph{Ablation: free-form decoding.}\\label{sec:ablation}",
          "-A natural objection is that constrained decoding artificially suppresses LP score variation by restricting the output space.",
          "-We test this with a controlled ablation on SciERC (Qwen3-8B, $N{=}8$, $T{=}1.0$): grammar constraints are removed entirely and outputs are parsed post-hoc.",
          "-The fine-tuned model produces valid JSON at 99.95\\% rate (4{,}406/4{,}408 samples), confirming format compliance without grammar enforcement.",
          "-LP score distributions are nearly identical across regimes: within-instance standard deviation ratio is $0.97{\\times}$, and the tied fraction decreases by only $2$~pp (from 59.7\\% to 57.7\\% at $\\varepsilon{=}0.05$; Table~\\ref{tab:freeform_ablation}, Panel~A).",
          "-NER selection gains remain negligible under both regimes (Panel~B), confirming that LP compression is intrinsic to the model's probability assignments rather than an artifact of constrained decoding.",
          "-This rules out constrained decoding as the primary cause of the correlation-selection gap.",
          "+Removing grammar constraints entirely (SciERC, Qwen3-8B) yields nearly identical LP distributions (within-instance std ratio $0.97{\\times}$, tied fraction $-2$~pp) and negligible selection changes, ruling out constrained decoding as the cause (Appendix~\\ref{app:freeform_ablation}).",
          "+Our consensus-proximity strategies instantiate MBR decoding \\cite{eikema2022sampling}; all fail because utility correlates with F1 across instances but not within them (Appendix~\\ref{app:mbr_discussion}).",
          " ",
          "-Our consensus-proximity selection strategies instantiate MBR decoding \\cite{eikema2022sampling, freitag2022high}; all variants fail because utility functions correlate with F1 across instances but not within them (Appendix~\\ref{app:mbr_discussion}).",
          "-Per-signal quality estimation changes and an RE-specific selection interaction under free-form decoding are detailed in Appendix~\\ref{app:freeform_ablation}.",
          "-",
          " \\paragraph{Methodological implications.}",
          " The decoupling of $\\rho$, AUROC, and selection F1 means single-metric evaluation risks selecting the wrong signal.",
          " Effective selection likely requires per-sample signals such as trained verifiers \\cite{cobbe2021verifiers, venktesh2025trust}; $N{=}8$ captures most quality estimation benefit (Appendix~\\ref{app:n_scaling})."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "26d2dfd7-9757-4d34-99ed-2e7566a685e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite"
}
```

</details>

---


### Assistant

_source line 6152 · 2026-05-15T17:55:06.208Z_

**Table 3 (tab:selection) — R3-W2 水平线分隔 instance-level vs per-sample：**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "976b530a-637a-479d-b1dc-3ca06cc1145c",
  "isSidechain": false,
  "requestId": "req_011Cb4nRb9jgyncDoiho1fEM",
  "type": "assistant",
  "uuid": "644f5a14-c74f-47ef-8748-45260ca7b2b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FYQXRF7GGZNU7p9qw2XrKe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 754,
      "cache_read_input_tokens": 161222,
      "output_tokens": 718,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 754,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 718,
          "cache_read_input_tokens": 161222,
          "cache_creation_input_tokens": 754,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 754
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


### Tool call

_source line 6153 · 2026-05-15T17:55:13.521Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01814snNx7pP6iCoNbFWDnnr`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
  "old_string": "Oracle & $0.778 \\pm 0.003$ & --- & 0.585 \\\\\n\\midrule\nLP           & $\\mathbf{0.647} \\pm 0.005$ & .29 & 0.395 \\\\\n\\midrule\nSJ           & $0.646 \\pm 0.002$ & .68 & 0.386 \\\\\nFK           & $0.646 \\pm 0.001$ & .79 & --- \\\\\nEM           & $0.637 \\pm 0.001$ & .45 & 0.372 \\\\\nVC           & $0.623 \\pm 0.004$ & .26 & 0.359 \\\\\n\\midrule\nGreedy$^\\dagger$ & $0.645 \\pm 0.001$ & --- & \\textbf{0.404} \\\\\nRandom           & $0.610 \\pm 0.003$ & --- & 0.354 \\\\",
  "new_string": "Oracle & $0.778 \\pm 0.003$ & --- & 0.585 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Per-sample signal}} \\\\\nLP           & $\\mathbf{0.647} \\pm 0.005$ & .29 & 0.395 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Instance-level signals (consensus-proximity selection)}} \\\\\nSJ           & $0.646 \\pm 0.002$ & .68 & 0.386 \\\\\nFK           & $0.646 \\pm 0.001$ & .79 & --- \\\\\nEM           & $0.637 \\pm 0.001$ & .45 & 0.372 \\\\\nVC           & $0.623 \\pm 0.004$ & .26 & 0.359 \\\\\n\\midrule\nGreedy$^\\dagger$ & $0.645 \\pm 0.001$ & --- & \\textbf{0.404} \\\\\nRandom           & $0.610 \\pm 0.003$ & --- & 0.354 \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "644f5a14-c74f-47ef-8748-45260ca7b2b5",
  "isSidechain": false,
  "requestId": "req_011Cb4nRb9jgyncDoiho1fEM",
  "type": "assistant",
  "uuid": "bd04cac4-3033-4f38-96f6-b810b9924f04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FYQXRF7GGZNU7p9qw2XrKe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 754,
      "cache_read_input_tokens": 161222,
      "output_tokens": 718,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 754,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 718,
          "cache_read_input_tokens": 161222,
          "cache_creation_input_tokens": 754,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 754
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

_source line 6154 · 2026-05-15T17:55:13.544Z_

<details><summary>↩ Tool result · `toolu_01814snNx7pP6iCoNbFWDnnr`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd04cac4-3033-4f38-96f6-b810b9924f04",
  "isSidechain": false,
  "promptId": "4ab6fc0d-e7b3-4753-81c9-824338d4b6fc",
  "type": "user",
  "uuid": "e1ff51af-0b9c-4290-8f5b-ececaa31c3ef",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
    "oldString": "Oracle & $0.778 \\pm 0.003$ & --- & 0.585 \\\\\n\\midrule\nLP           & $\\mathbf{0.647} \\pm 0.005$ & .29 & 0.395 \\\\\n\\midrule\nSJ           & $0.646 \\pm 0.002$ & .68 & 0.386 \\\\\nFK           & $0.646 \\pm 0.001$ & .79 & --- \\\\\nEM           & $0.637 \\pm 0.001$ & .45 & 0.372 \\\\\nVC           & $0.623 \\pm 0.004$ & .26 & 0.359 \\\\\n\\midrule\nGreedy$^\\dagger$ & $0.645 \\pm 0.001$ & --- & \\textbf{0.404} \\\\\nRandom           & $0.610 \\pm 0.003$ & --- & 0.354 \\\\",
    "newString": "Oracle & $0.778 \\pm 0.003$ & --- & 0.585 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Per-sample signal}} \\\\\nLP           & $\\mathbf{0.647} \\pm 0.005$ & .29 & 0.395 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Instance-level signals (consensus-proximity selection)}} \\\\\nSJ           & $0.646 \\pm 0.002$ & .68 & 0.386 \\\\\nFK           & $0.646 \\pm 0.001$ & .79 & --- \\\\\nEM           & $0.637 \\pm 0.001$ & .45 & 0.372 \\\\\nVC           & $0.623 \\pm 0.004$ & .26 & 0.359 \\\\\n\\midrule\nGreedy$^\\dagger$ & $0.645 \\pm 0.001$ & --- & \\textbf{0.404} \\\\\nRandom           & $0.610 \\pm 0.003$ & --- & 0.354 \\\\",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 81,
        "oldLines": 8,
        "newStart": 81,
        "newLines": 10,
        "lines": [
          " \\midrule",
          " Oracle & $0.778 \\pm 0.003$ & --- & 0.585 \\\\",
          " \\midrule",
          "+\\multicolumn{4}{l}{\\textit{Per-sample signal}} \\\\",
          " LP           & $\\mathbf{0.647} \\pm 0.005$ & .29 & 0.395 \\\\",
          " \\midrule",
          "+\\multicolumn{4}{l}{\\textit{Instance-level signals (consensus-proximity selection)}} \\\\",
          " SJ           & $0.646 \\pm 0.002$ & .68 & 0.386 \\\\",
          " FK           & $0.646 \\pm 0.001$ & .79 & --- \\\\",
          " EM           & $0.637 \\pm 0.001$ & .45 & 0.372 \\\\"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "bd04cac4-3033-4f38-96f6-b810b9924f04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite"
}
```

</details>

---


### Assistant

_source line 6155 · 2026-05-15T17:55:17.576Z_

**§4.3 Gap reframing — R3-W2, LP compression 为核心：**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1ff51af-0b9c-4290-8f5b-ececaa31c3ef",
  "isSidechain": false,
  "requestId": "req_011Cb4nSRijGkjcackRo83YT",
  "type": "assistant",
  "uuid": "18740d71-4623-4b5a-8226-1839f7e2f2d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fj1y8o1PkfnYsaWbRe9MWN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 775,
      "cache_read_input_tokens": 161976,
      "output_tokens": 448,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 775,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 448,
          "cache_read_input_tokens": 161976,
          "cache_creation_input_tokens": 775,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 775
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


### Tool call

_source line 6156 · 2026-05-15T17:55:23.970Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01HBNkUUBae8rhqZW9vUrYNF`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
  "old_string": "Despite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection (Table~\\ref{tab:selection}; see also Figure~\\ref{fig:selection_gap}).\nFour of five signals are instance-level aggregates that assign a single score per input regardless of which sample is evaluated; they cannot rank candidates by construction.\nThe non-trivial question is whether log-probability---the only per-sample signal---can exploit the oracle headroom.\nWe anchor this analysis on SciERC, where output diversity is substantial (39--43\\% unique outputs per instance, F1 std 0.11--0.14; Appendix~\\ref{app:diversity}).",
  "new_string": "Despite strong quality estimation, confidence signals yield limited gains for best-of-$N$ selection (Table~\\ref{tab:selection}; see also Figure~\\ref{fig:selection_gap}).\nFour of five signals are instance-level by construction (they assign identical scores to all candidates); the non-trivial question is whether LP---the only per-sample signal---can exploit the oracle headroom.\nWe anchor on SciERC, where output diversity is substantial (39--43\\% unique outputs; Appendix~\\ref{app:diversity})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18740d71-4623-4b5a-8226-1839f7e2f2d9",
  "isSidechain": false,
  "requestId": "req_011Cb4nSRijGkjcackRo83YT",
  "type": "assistant",
  "uuid": "ea5ab7a9-6ff9-4d97-8775-092eaffe85d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fj1y8o1PkfnYsaWbRe9MWN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 775,
      "cache_read_input_tokens": 161976,
      "output_tokens": 448,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 775,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 448,
          "cache_read_input_tokens": 161976,
          "cache_creation_input_tokens": 775,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 775
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

_source line 6157 · 2026-05-15T17:55:23.978Z_

<details><summary>↩ Tool result · `toolu_01HBNkUUBae8rhqZW9vUrYNF`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ea5ab7a9-6ff9-4d97-8775-092eaffe85d4",
  "isSidechain": false,
  "promptId": "4ab6fc0d-e7b3-4753-81c9-824338d4b6fc",
  "type": "user",
  "uuid": "c4c0fbb2-69cd-4de4-b2f6-85e87bf47916",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
    "oldString": "Despite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection (Table~\\ref{tab:selection}; see also Figure~\\ref{fig:selection_gap}).\nFour of five signals are instance-level aggregates that assign a single score per input regardless of which sample is evaluated; they cannot rank candidates by construction.\nThe non-trivial question is whether log-probability---the only per-sample signal---can exploit the oracle headroom.\nWe anchor this analysis on SciERC, where output diversity is substantial (39--43\\% unique outputs per instance, F1 std 0.11--0.14; Appendix~\\ref{app:diversity}).",
    "newString": "Despite strong quality estimation, confidence signals yield limited gains for best-of-$N$ selection (Table~\\ref{tab:selection}; see also Figure~\\ref{fig:selection_gap}).\nFour of five signals are instance-level by construction (they assign identical scores to all candidates); the non-trivial question is whether LP---the only per-sample signal---can exploit the oracle headroom.\nWe anchor on SciERC, where output diversity is substantial (39--43\\% unique outputs; Appendix~\\ref{app:diversity}).",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 96,
        "oldLines": 10,
        "newStart": 96,
        "newLines": 9,
        "lines": [
          " \\end{tabular}",
          " \\end{table}",
          " ",
          "-Despite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection (Table~\\ref{tab:selection}; see also Figure~\\ref{fig:selection_gap}).",
          "-Four of five signals are instance-level aggregates that assign a single score per input regardless of which sample is evaluated; they cannot rank candidates by construction.",
          "-The non-trivial question is whether log-probability---the only per-sample signal---can exploit the oracle headroom.",
          "-We anchor this analysis on SciERC, where output diversity is substantial (39--43\\% unique outputs per instance, F1 std 0.11--0.14; Appendix~\\ref{app:diversity}).",
          "+Despite strong quality estimation, confidence signals yield limited gains for best-of-$N$ selection (Table~\\ref{tab:selection}; see also Figure~\\ref{fig:selection_gap}).",
          "+Four of five signals are instance-level by construction (they assign identical scores to all candidates); the non-trivial question is whether LP---the only per-sample signal---can exploit the oracle headroom.",
          "+We anchor on SciERC, where output diversity is substantial (39--43\\% unique outputs; Appendix~\\ref{app:diversity}).",
          " ",
          " \\paragraph{No significant improvement over greedy.}",
          " We evaluate significance via 2-seed instance-level sign tests ($n{=}551$, Fisher combination)."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "ea5ab7a9-6ff9-4d97-8775-092eaffe85d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite"
}
```

</details>

---


### Assistant

_source line 6158 · 2026-05-15T17:55:27.738Z_

**Abstract 重写 — 问题-发现-意义 三段式 + RE preliminary：**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4c0fbb2-69cd-4de4-b2f6-85e87bf47916",
  "isSidechain": false,
  "requestId": "req_011Cb4nTCR4EvTRiujXD8jEq",
  "type": "assistant",
  "uuid": "cb6daad8-6886-4d9c-afa5-d258ef291376",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0175JibAefTgKHpo7GNU7VyS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 505,
      "cache_read_input_tokens": 162751,
      "output_tokens": 356,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 505,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 356,
          "cache_read_input_tokens": 162751,
          "cache_creation_input_tokens": 505,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 505
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


### Tool call

_source line 6159 · 2026-05-15T17:55:34.430Z_

<details open><summary>🔧 Tool call — Write · `toolu_01D6NfqPEkt3C2FZtgrvvPsm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex",
  "content": "\\begin{abstract}\nSelf-consistency---sampling multiple outputs and selecting via agreement---yields large gains on discrete-answer tasks, but information extraction (IE) produces \\textit{sets} of entities and relations with partial overlap, where no majority vote exists.\n\nWe evaluate five confidence signals for LLM-based IE across three NER benchmarks and one RE benchmark (preliminary) with two 8B-parameter models, revealing the \\textit{correlation-selection gap}: all signals achieve strong quality estimation yet none significantly improves sample selection despite substantial oracle headroom.\nThe gap has two layers: instance-level signals cannot rank candidates by construction, and log-probability---the only per-sample signal---is too compressed within instances to discriminate (median range 0.041 nats); where compression is mitigated, selection recovers significant gains.\nSignal rankings shift with task difficulty and type, and collapse at the capability boundary.\n\nClosing the gap likely requires learned per-sample scoring such as trained verifiers.\n\\end{abstract}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb6daad8-6886-4d9c-afa5-d258ef291376",
  "isSidechain": false,
  "requestId": "req_011Cb4nTCR4EvTRiujXD8jEq",
  "type": "assistant",
  "uuid": "cb7b7004-2d5f-4183-aea9-21ba2f4a7d12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0175JibAefTgKHpo7GNU7VyS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 505,
      "cache_read_input_tokens": 162751,
      "output_tokens": 356,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 505,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 356,
          "cache_read_input_tokens": 162751,
          "cache_creation_input_tokens": 505,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 505
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

_source line 6160 · 2026-05-15T17:55:34.445Z_

<details><summary>↩ Tool result · `toolu_01D6NfqPEkt3C2FZtgrvvPsm`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb7b7004-2d5f-4183-aea9-21ba2f4a7d12",
  "isSidechain": false,
  "promptId": "4ab6fc0d-e7b3-4753-81c9-824338d4b6fc",
  "type": "user",
  "uuid": "744f5882-1da6-4294-b0c3-7f5ceb28c31c",
  "toolUseResult": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex",
    "content": "\\begin{abstract}\nSelf-consistency---sampling multiple outputs and selecting via agreement---yields large gains on discrete-answer tasks, but information extraction (IE) produces \\textit{sets} of entities and relations with partial overlap, where no majority vote exists.\n\nWe evaluate five confidence signals for LLM-based IE across three NER benchmarks and one RE benchmark (preliminary) with two 8B-parameter models, revealing the \\textit{correlation-selection gap}: all signals achieve strong quality estimation yet none significantly improves sample selection despite substantial oracle headroom.\nThe gap has two layers: instance-level signals cannot rank candidates by construction, and log-probability---the only per-sample signal---is too compressed within instances to discriminate (median range 0.041 nats); where compression is mitigated, selection recovers significant gains.\nSignal rankings shift with task difficulty and type, and collapse at the capability boundary.\n\nClosing the gap likely requires learned per-sample scoring such as trained verifiers.\n\\end{abstract}\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 10,
        "newStart": 1,
        "newLines": 9,
        "lines": [
          " \\begin{abstract}",
          " Self-consistency---sampling multiple outputs and selecting via agreement---yields large gains on discrete-answer tasks, but information extraction (IE) produces \\textit{sets} of entities and relations with partial overlap, where no majority vote exists.",
          "-Can consistency signals nonetheless select the best among $N$ candidates?",
          " ",
          "-Across three NER benchmarks and one RE benchmark (preliminary, single dataset) with two 8B-parameter models, all signals achieve strong quality estimation yet none significantly improves sample selection despite substantial oracle headroom---the \\textit{correlation-selection gap}.",
          "-Instance-level signals cannot rank candidates by construction; log-probability, the only per-sample signal, is too compressed to discriminate among near-identical outputs; and consensus-proximity selection correlates with quality across instances but not within them.",
          "-Signal rankings shift with task difficulty and collapse at the capability boundary.",
          "+We evaluate five confidence signals for LLM-based IE across three NER benchmarks and one RE benchmark (preliminary) with two 8B-parameter models, revealing the \\textit{correlation-selection gap}: all signals achieve strong quality estimation yet none significantly improves sample selection despite substantial oracle headroom.",
          "+The gap has two layers: instance-level signals cannot rank candidates by construction, and log-probability---the only per-sample signal---is too compressed within instances to discriminate (median range 0.041 nats); where compression is mitigated, selection recovers significant gains.",
          "+Signal rankings shift with task difficulty and type, and collapse at the capability boundary.",
          " ",
          " Closing the gap likely requires learned per-sample scoring such as trained verifiers.",
          " \\end{abstract}"
        ]
      }
    ],
    "originalFile": "\\begin{abstract}\nSelf-consistency---sampling multiple outputs and selecting via agreement---yields large gains on discrete-answer tasks, but information extraction (IE) produces \\textit{sets} of entities and relations with partial overlap, where no majority vote exists.\nCan consistency signals nonetheless select the best among $N$ candidates?\n\nAcross three NER benchmarks and one RE benchmark (preliminary, single dataset) with two 8B-parameter models, all signals achieve strong quality estimation yet none significantly improves sample selection despite substantial oracle headroom---the \\textit{correlation-selection gap}.\nInstance-level signals cannot rank candidates by construction; log-probability, the only per-sample signal, is too compressed to discriminate among near-identical outputs; and consensus-proximity selection correlates with quality across instances but not within them.\nSignal rankings shift with task difficulty and collapse at the capability boundary.\n\nClosing the gap likely requires learned per-sample scoring such as trained verifiers.\n\\end{abstract}\n",
    "userModified": false
  },
  "sourceToolAssistantUUID": "cb7b7004-2d5f-4183-aea9-21ba2f4a7d12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite"
}
```

</details>

---


### Runtime record

_source line 6161 · 2026-05-15T17:55:34.470Z_

```json
{
  "parentUuid": "744f5882-1da6-4294-b0c3-7f5ceb28c31c",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "3eeb7bfb-5b44-4410-ade2-c4361d063b5c",
  "timestamp": "2026-05-15T17:55:34.470Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite"
}
```

---


### Runtime record

_source line 6162_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] [Patch] Round 8 高优先写作修复——不依赖正在跑的实验，立即处理。  按优先级排序：  ## 1. R8-N1 页数压缩至 ≤8 页（CRITICAL，desk-rejection 风险） 当前估计 10-11 页正文。压缩策略： - Discussion free-form ablation 详述移至 Appendix（~0.5 页） - Robustn…",
  "leafUuid": "3eeb7bfb-5b44-4410-ade2-c4361d063b5c",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6"
}
```

---


### Runtime record

_source line 6163_

```json
{
  "type": "ai-title",
  "aiTitle": "Set up agent communication with Director",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6"
}
```

---


### Assistant

_source line 6164 · 2026-05-15T17:55:37.565Z_

**次要修复 — R8-W1 Code and Data 承诺：**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3eeb7bfb-5b44-4410-ade2-c4361d063b5c",
  "isSidechain": false,
  "requestId": "req_011Cb4nTyA7qvhVEX4gP4PZN",
  "type": "assistant",
  "uuid": "8390ec7f-05cc-4a4a-b754-9e7a6a99f438",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WJPFEg7XsGQ4ikLPAKXeR3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 517,
      "cache_read_input_tokens": 163256,
      "output_tokens": 114,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 517,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 114,
          "cache_read_input_tokens": 163256,
          "cache_creation_input_tokens": 517,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 517
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


### Tool call

_source line 6165 · 2026-05-15T17:55:38.087Z_

<details open><summary>🔧 Tool call — Read · `toolu_017wxHxSGVM28DxzNjhofVhL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8390ec7f-05cc-4a4a-b754-9e7a6a99f438",
  "isSidechain": false,
  "requestId": "req_011Cb4nTyA7qvhVEX4gP4PZN",
  "type": "assistant",
  "uuid": "ed251dad-c3cd-4363-8dc0-2e74a7790eb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WJPFEg7XsGQ4ikLPAKXeR3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 517,
      "cache_read_input_tokens": 163256,
      "output_tokens": 114,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 517,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 114,
          "cache_read_input_tokens": 163256,
          "cache_creation_input_tokens": 517,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 517
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

_source line 6166 · 2026-05-15T17:55:38.093Z_

<details><summary>↩ Tool result · `toolu_017wxHxSGVM28DxzNjhofVhL`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	We systematically evaluate five confidence signals across quality estimation, binary discrimination, and sample selection for LLM-based structured IE, revealing that these metrics decouple---single-metric evaluation risks selecting the wrong signal for the intended use case.
4	All signals achieve strong quality estimation yet none significantly improves sample selection on SciERC despite substantial oracle headroom---the \textit{correlation-selection gap}.
5	The instance-level failure of four signals is definitional; LP scores are too compressed within instances to discriminate among candidates (median LP range 0.041 nats), though where compression is mitigated, LP becomes significant; a free-form ablation confirms compression persists without constrained decoding.
6	Signal rankings shift with difficulty and task type: EM leads on easy NER, structural signals on hard NER, while LP outperforms structural signals for RE quality estimation despite identical compression---consistent across two model families; at the capability boundary (WNUT-17), all signals collapse.
7	RE findings rest on SciERC alone (preliminary); trained verifiers, scaling to 70B+, and conformal prediction are promising directions.
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ed251dad-c3cd-4363-8dc0-2e74a7790eb5",
  "isSidechain": false,
  "promptId": "4ab6fc0d-e7b3-4753-81c9-824338d4b6fc",
  "type": "user",
  "uuid": "8b8e3b91-ecae-43ff-a287-96e7451400c6",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex",
      "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nWe systematically evaluate five confidence signals across quality estimation, binary discrimination, and sample selection for LLM-based structured IE, revealing that these metrics decouple---single-metric evaluation risks selecting the wrong signal for the intended use case.\nAll signals achieve strong quality estimation yet none significantly improves sample selection on SciERC despite substantial oracle headroom---the \\textit{correlation-selection gap}.\nThe instance-level failure of four signals is definitional; LP scores are too compressed within instances to discriminate among candidates (median LP range 0.041 nats), though where compression is mitigated, LP becomes significant; a free-form ablation confirms compression persists without constrained decoding.\nSignal rankings shift with difficulty and task type: EM leads on easy NER, structural signals on hard NER, while LP outperforms structural signals for RE quality estimation despite identical compression---consistent across two model families; at the capability boundary (WNUT-17), all signals collapse.\nRE findings rest on SciERC alone (preliminary); trained verifiers, scaling to 70B+, and conformal prediction are promising directions.\n",
      "numLines": 8,
      "startLine": 1,
      "totalLines": 8
    }
  },
  "sourceToolAssistantUUID": "ed251dad-c3cd-4363-8dc0-2e74a7790eb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite"
}
```

</details>

---


### Tool call

_source line 6167 · 2026-05-15T17:55:40.959Z_

<details open><summary>🔧 Tool call — Read · `toolu_01StM6KhyQXNSxppnEB9tF1m`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b8e3b91-ecae-43ff-a287-96e7451400c6",
  "isSidechain": false,
  "requestId": "req_011Cb4nUEuQp7sVe6SQ1n7D6",
  "type": "assistant",
  "uuid": "8130bda2-8217-4e43-bad0-465c1192163a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012dpkKeQb7c14ToWEpHkawy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 399,
      "cache_read_input_tokens": 163773,
      "output_tokens": 89,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 399,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 89,
          "cache_read_input_tokens": 163773,
          "cache_creation_input_tokens": 399,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 399
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

_source line 6168 · 2026-05-15T17:55:40.968Z_

<details><summary>↩ Tool result · `toolu_01StM6KhyQXNSxppnEB9tF1m`</summary>

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
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors:\\ Confidence Signals Predict but Struggle to Select in 8B-Scale Information Extraction}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\section*{Ethics Statement}
40	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, LLaMA-3.1-8B).
41	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
42	No new human data was collected or annotated for this study.
43	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
44	Code and data will be released upon acceptance at [anonymized URL].
45	
46	\bibliography{references}
47	
48	\appendix
49	\input{sections/appendix}
50	
51	\end{document}
52	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8130bda2-8217-4e43-bad0-465c1192163a",
  "isSidechain": false,
  "promptId": "4ab6fc0d-e7b3-4753-81c9-824338d4b6fc",
  "type": "user",
  "uuid": "45b361c3-0af3-4e8b-b8b7-dc09e7998667",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{inconsolata}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\n\\graphicspath{{figures/}}\n\n\\title{Strong Predictors, Weak Selectors:\\\\ Confidence Signals Predict but Struggle to Select in 8B-Scale Information Extraction}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{sections/abstract}\n\\input{sections/introduction}\n\\input{sections/related_work}\n\\input{sections/method}\n\\input{sections/experiments}\n\\input{sections/discussion}\n\\input{sections/conclusion}\n\n\\section*{Limitations}\n\\input{sections/limitations}\n\n\\section*{Ethics Statement}\nAll experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, LLaMA-3.1-8B).\nCoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.\nNo new human data was collected or annotated for this study.\nOur findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.\nCode and data will be released upon acceptance at [anonymized URL].\n\n\\bibliography{references}\n\n\\appendix\n\\input{sections/appendix}\n\n\\end{document}\n",
      "numLines": 52,
      "startLine": 1,
      "totalLines": 52
    }
  },
  "sourceToolAssistantUUID": "8130bda2-8217-4e43-bad0-465c1192163a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite"
}
```

</details>

---


### Assistant

_source line 6169 · 2026-05-15T17:55:53.248Z_

<details><summary>Logged reasoning block</summary>

```text
I see that Code and Data release is already in the Ethics Statement (line 44): "Code and data will be released upon acceptance at [anonymized URL]." 

R8-W1 asks for a "Code and Data 发布承诺段落". This is already there in the Ethics Statement. But some venues want a separate "Reproducibility" or "Code Availability" section. Let me check if this is sufficient.

For EMNLP, the Ethics Statement typically includes such commitments. The Director says "添加 Code and Data 发布承诺段落" - but it's already there. I'll note this.


Now I need to check the page count after my edits and see what else needs attention. Let me look at whether the Discussion section can be tightened further, particularly the paragraphs about LP compression being task-dependent and how the gap widens with N. I should also verify the current state of the Discussion to understand what compression is still possible.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45b361c3-0af3-4e8b-b8b7-dc09e7998667",
  "isSidechain": false,
  "requestId": "req_011Cb4nUTjatHvKJXxeXzp57",
  "type": "assistant",
  "uuid": "71dfcfee-88fc-4724-8c5c-0e4e05cc50ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ANAUYcwwiBB2mV5Rna467C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 687,
      "cache_read_input_tokens": 164172,
      "output_tokens": 438,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 687,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 438,
          "cache_read_input_tokens": 164172,
          "cache_creation_input_tokens": 687,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 687
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


### Assistant

_source line 6170 · 2026-05-15T17:55:53.250Z_

Code and Data 承诺已在 Ethics Statement (main.tex line 44)。编译检查页数改进。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71dfcfee-88fc-4724-8c5c-0e4e05cc50ab",
  "isSidechain": false,
  "requestId": "req_011Cb4nUTjatHvKJXxeXzp57",
  "type": "assistant",
  "uuid": "90faed6f-3e17-4994-9c16-c4d4959ffa8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ANAUYcwwiBB2mV5Rna467C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 687,
      "cache_read_input_tokens": 164172,
      "output_tokens": 438,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 687,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 438,
          "cache_read_input_tokens": 164172,
          "cache_creation_input_tokens": 687,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 687
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


### Tool call

_source line 6171 · 2026-05-15T17:55:53.258Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__paper_compile_and_check · `toolu_01BGHgPHsGu6imsJXtzykuUb`</summary>

```json
{
  "project": "struct_self_consist_ie",
  "max_pages": 8
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90faed6f-3e17-4994-9c16-c4d4959ffa8d",
  "isSidechain": false,
  "requestId": "req_011Cb4nUTjatHvKJXxeXzp57",
  "type": "assistant",
  "uuid": "b582b1ac-b18c-4670-9700-89cbf0e43038",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ANAUYcwwiBB2mV5Rna467C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 687,
      "cache_read_input_tokens": 164172,
      "output_tokens": 438,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 687,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 438,
          "cache_read_input_tokens": 164172,
          "cache_creation_input_tokens": 687,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 687
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

_source line 6172 · 2026-05-15T17:55:57.049Z_

<details><summary>↩ Tool result · `toolu_01BGHgPHsGu6imsJXtzykuUb`</summary>

```text
{"result":"{\"success\": true, \"passed\": false, \"compiled\": {\"success\": true, \"pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf\", \"paper_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper\", \"main_tex\": \"main.tex\", \"log_tail\": \"\\nOverfull \\\\hbox (47.2356pt too wide) in paragraph at lines 745--756\\n [][] \\n []\\n\\n\\nUnderfull \\\\hbox (badness 1655) in paragraph at lines 790--790\\n[]\\\\T1/ptm/m/n/10 (+20) Table 22: |Cross-dataset OOD qual-ity es-ti-ma-tion\\n []\\n\\n\\nUnderfull \\\\hbox (badness 1769) in paragraph at lines 790--790\\n\\\\T1/ptm/m/n/10 (+20) in-stances ($\\\\OML/cmm/m/it/10 n[]\\\\OT1/cmr/m/n/10 2756$\\\\T1/\\nptm/m/n/10 (+20) ). CoNLL$\\\\OMS/cmsy/m/n/10 !$\\\\T1/ptm/m/n/10 (+20) SciERC: CoNLL\\n-\\n []\\n\\n\\nOverfull \\\\hbox (46.87402pt too wide) in paragraph at lines 792--805\\n [][] \\n []\\n\\n[22])\\nUnderfull \\\\hbox (badness 5133) in paragraph at lines 818--50\\n []\\\\T1/ptm/b/n/10.95 (+20) Asymmetry in-ter-pre-ta-tion.[] \\\\T1/ptm/m/n/10.95 (+\\n20) The di-rec-tional\\n []\\n\\n\\nUnderfull \\\\hbox (badness 7081) in paragraph at lines 818--50\\n\\\\T1/ptm/m/n/10.95 (+20) asym-me-try is driven by schema cov-er-age:\\n []\\n\\n[23\\n\\n] (./main.aux)\\n ***********\\nLaTeX2e <2025-11-01>\\nL3 programming layer <2026-01-19>\\n ***********\\nPackage rerunfilecheck Info: File `main.out' has not changed.\\n(rerunfilecheck)             Checksum: 12754B12DD2F90E2AB798D6280AE20BA;4768.\\n ) \\nHere is how much of TeX's memory you used:\\n 16909 strings out of 469438\\n 267249 string characters out of 5468411\\n 748286 words of memory out of 5000000\\n 44542 multiletter control sequences out of 15000+600000\\n 722220 words of font info for 470 fonts, out of 8000000 for 9000\\n 59 hyphenation exceptions out of 8191\\n 84i,12n,93p,1001b,698s stack positions out of 10000i,1000n,20000p,200000b,200000s\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/inconsolata/Inconsolata-zi4\\nr.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx9.pfb><\\n/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/s\\nhare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/t\\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive\\n/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-\\ndist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fo\\nnts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\\ne1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\\nic/amsfonts/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf\\nonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/\\ncmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb\\n>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr\\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/\\ntexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive\\n/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-\\ndist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fo\\nnts/type1/public/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fon\\nts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-dist/font\\ns/type1/urw/helvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/\\ntimes/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pf\\nb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\\nOutput written on main.pdf (23 pages, 659460 bytes).\\nPDF statistics:\\n 1601 PDF objects out of 1728 (max. 8388607)\\n 1064 compressed objects within 11 object streams\\n 221 named destinations out of 1000 (max. 500000)\\n 85268 words of extra memory for PDF output out of 89155 (max. 10000000)\\n\", \"error\": \"\", \"pages\": 23, \"warnings\": [\"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\"]}, \"pages\": 23, \"page_status\": \"over_limit\", \"max_pages\": 8, \"min_pages\": null, \"critical_warnings\": [], \"minor_warnings\": [\"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"Underfull \\\\hbox (badness 3333) in paragraph at lines 19--20\", \"Underfull \\\\hbox (badness 1152) in paragraph at lines 37--39\", \"Underfull \\\\hbox (badness 2556) in paragraph at lines 13--19\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 1226) in paragraph at lines 71--74\", \"Underfull \\\\hbox (badness 3668) in paragraph at lines 14--20\", \"Underfull \\\\hbox (badness 1377) in paragraph at lines 14--20\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 111--114\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 111--114\", \"Underfull \\\\hbox (badness 5036) in paragraph at lines 119--1\", \"Underfull \\\\hbox (badness 1616) in paragraph at lines 119--1\", \"Underfull \\\\hbox (badness 1242) in paragraph at lines 8--15\", \"Underfull \\\\hbox (badness 1365) in paragraph at lines 147--152\", \"Underfull \\\\hbox (badness 1158) in paragraph at lines 183--191\", \"Underfull \\\\hbox (badness 1043) in paragraph at lines 205--211\", \"Underfull \\\\hbox (badness 1742) in paragraph at lines 205--211\", \"Underfull \\\\hbox (badness 1184) in paragraph at lines 214--219\", \"Underfull \\\\hbox (badness 1990) in paragraph at lines 229--233\", \"Underfull \\\\hbox (badness 1824) in paragraph at lines 303--307\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 311--319\", \"Underfull \\\\hbox (badness 1082) in paragraph at lines 311--319\", \"Underfull \\\\hbox (badness 4454) in paragraph at lines 311--319\", \"Underfull \\\\hbox (badness 1681) in paragraph at lines 382--388\", \"Underfull \\\\hbox (badness 8056) in paragraph at lines 90--93\", \"Underfull \\\\hbox (badness 5802) in paragraph at lines 90--93\", \"Underfull \\\\hbox (badness 1253) in paragraph at lines 90--93\", \"Underfull \\\\hbox (badness 1715) in paragraph at lines 90--93\", \"Underfull \\\\hbox (badness 2635) in paragraph at lines 90--93\", \"Underfull \\\\vbox (badness 6910) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 1990) in paragraph at lines 109--113\", \"Underfull \\\\hbox (badness 2753) in paragraph at lines 134--140\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 134--140\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 134--140\", \"Underfull \\\\hbox (badness 1082) in paragraph at lines 134--140\", \"Underfull \\\\hbox (badness 1072) in paragraph at lines 134--140\", \"Underfull \\\\hbox (badness 6691) in paragraph at lines 134--140\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 134--140\", \"Underfull \\\\hbox (badness 1019) in paragraph at lines 142--145\", \"Overfull \\\\hbox (0.91821pt too wide) in paragraph at lines 147--153\", \"Underfull \\\\hbox (badness 1033) in paragraph at lines 155--159\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Overfull \\\\hbox (19.10843pt too wide) in paragraph at lines 165--176\", \"Underfull \\\\hbox (badness 4060) in paragraph at lines 254--257\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Overfull \\\\hbox (18.97287pt too wide) in paragraph at lines 316--329\", \"Underfull \\\\hbox (badness 1210) in paragraph at lines 333--337\", \"Overfull \\\\hbox (75.87871pt too wide) in paragraph at lines 343--359\", \"Overfull \\\\hbox (0.76773pt too wide) in paragraph at lines 370--395\", \"Underfull \\\\hbox (badness 2460) in paragraph at lines 410--410\", \"Underfull \\\\hbox (badness 3514) in paragraph at lines 410--410\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 464--467\", \"Underfull \\\\hbox (badness 1810) in paragraph at lines 464--467\", \"Underfull \\\\hbox (badness 1845) in paragraph at lines 464--467\", \"Underfull \\\\hbox (badness 1442) in paragraph at lines 464--467\", \"Underfull \\\\hbox (badness 1845) in paragraph at lines 464--467\", \"Underfull \\\\hbox (badness 2277) in paragraph at lines 464--467\", \"Underfull \\\\hbox (badness 2626) in paragraph at lines 464--467\", \"Underfull \\\\hbox (badness 6268) in paragraph at lines 464--467\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 464--467\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 464--467\", \"Underfull \\\\hbox (badness 1552) in paragraph at lines 464--467\", \"Underfull \\\\hbox (badness 4266) in paragraph at lines 469--472\", \"Underfull \\\\hbox (badness 1418) in paragraph at lines 550--555\", \"Underfull \\\\hbox (badness 2894) in paragraph at lines 582--585\", \"Underfull \\\\hbox (badness 5008) in paragraph at lines 582--585\", \"Underfull \\\\hbox (badness 1859) in paragraph at lines 682--683\", \"Underfull \\\\hbox (badness 1838) in paragraph at lines 685--687\", \"Overfull \\\\hbox (27.00938pt too wide) in paragraph at lines 698--708\", \"Underfull \\\\vbox (badness 2781) has occurred while \\\\output is active []\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Overfull \\\\hbox (50.91055pt too wide) in paragraph at lines 723--738\", \"Overfull \\\\hbox (47.2356pt too wide) in paragraph at lines 745--756\", \"Underfull \\\\hbox (badness 1655) in paragraph at lines 790--790\", \"Underfull \\\\hbox (badness 1769) in paragraph at lines 790--790\", \"Overfull \\\\hbox (46.87402pt too wide) in paragraph at lines 792--805\", \"Underfull \\\\hbox (badness 5133) in paragraph at lines 818--50\", \"Underfull \\\\hbox (badness 7081) in paragraph at lines 818--50\"], \"issues\": [\"pages 23 > limit 8\"], \"summary\": \"FAIL: pages 23 > limit 8\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b582b1ac-b18c-4670-9700-89cbf0e43038",
  "isSidechain": false,
  "promptId": "4ab6fc0d-e7b3-4753-81c9-824338d4b6fc",
  "type": "user",
  "uuid": "16bea775-d30e-4f95-86f5-45b2f63a5c83",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"passed\\\": false, \\\"compiled\\\": {\\\"success\\\": true, \\\"pdf_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf\\\", \\\"paper_dir\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper\\\", \\\"main_tex\\\": \\\"main.tex\\\", \\\"log_tail\\\": \\\"\\\\nOverfull \\\\\\\\hbox (47.2356pt too wide) in paragraph at lines 745--756\\\\n [][] \\\\n []\\\\n\\\\n\\\\nUnderfull \\\\\\\\hbox (badness 1655) in paragraph at lines 790--790\\\\n[]\\\\\\\\T1/ptm/m/n/10 (+20) Table 22: |Cross-dataset OOD qual-ity es-ti-ma-tion\\\\n []\\\\n\\\\n\\\\nUnderfull \\\\\\\\hbox (badness 1769) in paragraph at lines 790--790\\\\n\\\\\\\\T1/ptm/m/n/10 (+20) in-stances ($\\\\\\\\OML/cmm/m/it/10 n[]\\\\\\\\OT1/cmr/m/n/10 2756$\\\\\\\\T1/\\\\nptm/m/n/10 (+20) ). CoNLL$\\\\\\\\OMS/cmsy/m/n/10 !$\\\\\\\\T1/ptm/m/n/10 (+20) SciERC: CoNLL\\\\n-\\\\n []\\\\n\\\\n\\\\nOverfull \\\\\\\\hbox (46.87402pt too wide) in paragraph at lines 792--805\\\\n [][] \\\\n []\\\\n\\\\n[22])\\\\nUnderfull \\\\\\\\hbox (badness 5133) in paragraph at lines 818--50\\\\n []\\\\\\\\T1/ptm/b/n/10.95 (+20) Asymmetry in-ter-pre-ta-tion.[] \\\\\\\\T1/ptm/m/n/10.95 (+\\\\n20) The di-rec-tional\\\\n []\\\\n\\\\n\\\\nUnderfull \\\\\\\\hbox (badness 7081) in paragraph at lines 818--50\\\\n\\\\\\\\T1/ptm/m/n/10.95 (+20) asym-me-try is driven by schema cov-er-age:\\\\n []\\\\n\\\\n[23\\\\n\\\\n] (./main.aux)\\\\n ***********\\\\nLaTeX2e <2025-11-01>\\\\nL3 programming layer <2026-01-19>\\\\n ***********\\\\nPackage rerunfilecheck Info: File `main.out' has not changed.\\\\n(rerunfilecheck)             Checksum: 12754B12DD2F90E2AB798D6280AE20BA;4768.\\\\n ) \\\\nHere is how much of TeX's memory you used:\\\\n 16909 strings out of 469438\\\\n 267249 string characters out of 5468411\\\\n 748286 words of memory out of 5000000\\\\n 44542 multiletter control sequences out of 15000+600000\\\\n 722220 words of font info for 470 fonts, out of 8000000 for 9000\\\\n 59 hyphenation exceptions out of 8191\\\\n 84i,12n,93p,1001b,698s stack positions out of 10000i,1000n,20000p,200000b,200000s\\\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/inconsolata/Inconsolata-zi4\\\\nr.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx9.pfb><\\\\n/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/s\\\\nhare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/t\\\\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive\\\\n/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-\\\\ndist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fo\\\\nnts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\\\\ne1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\\\\nic/amsfonts/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf\\\\nonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/\\\\ncmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb\\\\n>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr\\\\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/\\\\ntexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive\\\\n/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-\\\\ndist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fo\\\\nnts/type1/public/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fon\\\\nts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-dist/font\\\\ns/type1/urw/helvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/\\\\ntimes/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pf\\\\nb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\\\\nOutput written on main.pdf (23 pages, 659460 bytes).\\\\nPDF statistics:\\\\n 1601 PDF objects out of 1728 (max. 8388607)\\\\n 1064 compressed objects within 11 object streams\\\\n 221 named destinations out of 1000 (max. 500000)\\\\n 85268 words of extra memory for PDF output out of 89155 (max. 10000000)\\\\n\\\", \\\"error\\\": \\\"\\\", \\\"pages\\\": 23, \\\"warnings\\\": [\\\"Token not allowed in a PDF string (Unicode):\\\", \\\"Token not allowed in a PDF string (Unicode):\\\", \\\"Token not allowed in a PDF string (Unicode):\\\", \\\"Token not allowed in a PDF string (Unicode):\\\"]}, \\\"pages\\\": 23, \\\"page_status\\\": \\\"over_limit\\\", \\\"max_pages\\\": 8, \\\"min_pages\\\": null, \\\"critical_warnings\\\": [], \\\"minor_warnings\\\": [\\\"Token not allowed in a PDF string (Unicode):\\\", \\\"Token not allowed in a PDF string (Unicode):\\\", \\\"Token not allowed in a PDF string (Unicode):\\\", \\\"Token not allowed in a PDF string (Unicode):\\\", \\\"Underfull \\\\\\\\hbox (badness 3333) in paragraph at lines 19--20\\\", \\\"Underfull \\\\\\\\hbox (badness 1152) in paragraph at lines 37--39\\\", \\\"Underfull \\\\\\\\hbox (badness 2556) in paragraph at lines 13--19\\\", \\\"Underfull \\\\\\\\vbox (badness 10000) has occurred while \\\\\\\\output is active []\\\", \\\"Underfull \\\\\\\\hbox (badness 1226) in paragraph at lines 71--74\\\", \\\"Underfull \\\\\\\\hbox (badness 3668) in paragraph at lines 14--20\\\", \\\"Underfull \\\\\\\\hbox (badness 1377) in paragraph at lines 14--20\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 111--114\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 111--114\\\", \\\"Underfull \\\\\\\\hbox (badness 5036) in paragraph at lines 119--1\\\", \\\"Underfull \\\\\\\\hbox (badness 1616) in paragraph at lines 119--1\\\", \\\"Underfull \\\\\\\\hbox (badness 1242) in paragraph at lines 8--15\\\", \\\"Underfull \\\\\\\\hbox (badness 1365) in paragraph at lines 147--152\\\", \\\"Underfull \\\\\\\\hbox (badness 1158) in paragraph at lines 183--191\\\", \\\"Underfull \\\\\\\\hbox (badness 1043) in paragraph at lines 205--211\\\", \\\"Underfull \\\\\\\\hbox (badness 1742) in paragraph at lines 205--211\\\", \\\"Underfull \\\\\\\\hbox (badness 1184) in paragraph at lines 214--219\\\", \\\"Underfull \\\\\\\\hbox (badness 1990) in paragraph at lines 229--233\\\", \\\"Underfull \\\\\\\\hbox (badness 1824) in paragraph at lines 303--307\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 311--319\\\", \\\"Underfull \\\\\\\\hbox (badness 1082) in paragraph at lines 311--319\\\", \\\"Underfull \\\\\\\\hbox (badness 4454) in paragraph at lines 311--319\\\", \\\"Underfull \\\\\\\\hbox (badness 1681) in paragraph at lines 382--388\\\", \\\"Underfull \\\\\\\\hbox (badness 8056) in paragraph at lines 90--93\\\", \\\"Underfull \\\\\\\\hbox (badness 5802) in paragraph at lines 90--93\\\", \\\"Underfull \\\\\\\\hbox (badness 1253) in paragraph at lines 90--93\\\", \\\"Underfull \\\\\\\\hbox (badness 1715) in paragraph at lines 90--93\\\", \\\"Underfull \\\\\\\\hbox (badness 2635) in paragraph at lines 90--93\\\", \\\"Underfull \\\\\\\\vbox (badness 6910) has occurred while \\\\\\\\output is active []\\\", \\\"Underfull \\\\\\\\hbox (badness 1990) in paragraph at lines 109--113\\\", \\\"Underfull \\\\\\\\hbox (badness 2753) in paragraph at lines 134--140\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 134--140\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 134--140\\\", \\\"Underfull \\\\\\\\hbox (badness 1082) in paragraph at lines 134--140\\\", \\\"Underfull \\\\\\\\hbox (badness 1072) in paragraph at lines 134--140\\\", \\\"Underfull \\\\\\\\hbox (badness 6691) in paragraph at lines 134--140\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 134--140\\\", \\\"Underfull \\\\\\\\hbox (badness 1019) in paragraph at lines 142--145\\\", \\\"Overfull \\\\\\\\hbox (0.91821pt too wide) in paragraph at lines 147--153\\\", \\\"Underfull \\\\\\\\hbox (badness 1033) in paragraph at lines 155--159\\\", \\\"Underfull \\\\\\\\vbox (badness 10000) has occurred while \\\\\\\\output is active []\\\", \\\"Overfull \\\\\\\\hbox (19.10843pt too wide) in paragraph at lines 165--176\\\", \\\"Underfull \\\\\\\\hbox (badness 4060) in paragraph at lines 254--257\\\", \\\"Underfull \\\\\\\\vbox (badness 10000) has occurred while \\\\\\\\output is active []\\\", \\\"Overfull \\\\\\\\hbox (18.97287pt too wide) in paragraph at lines 316--329\\\", \\\"Underfull \\\\\\\\hbox (badness 1210) in paragraph at lines 333--337\\\", \\\"Overfull \\\\\\\\hbox (75.87871pt too wide) in paragraph at lines 343--359\\\", \\\"Overfull \\\\\\\\hbox (0.76773pt too wide) in paragraph at lines 370--395\\\", \\\"Underfull \\\\\\\\hbox (badness 2460) in paragraph at lines 410--410\\\", \\\"Underfull \\\\\\\\hbox (badness 3514) in paragraph at lines 410--410\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 464--467\\\", \\\"Underfull \\\\\\\\hbox (badness 1810) in paragraph at lines 464--467\\\", \\\"Underfull \\\\\\\\hbox (badness 1845) in paragraph at lines 464--467\\\", \\\"Underfull \\\\\\\\hbox (badness 1442) in paragraph at lines 464--467\\\", \\\"Underfull \\\\\\\\hbox (badness 1845) in paragraph at lines 464--467\\\", \\\"Underfull \\\\\\\\hbox (badness 2277) in paragraph at lines 464--467\\\", \\\"Underfull \\\\\\\\hbox (badness 2626) in paragraph at lines 464--467\\\", \\\"Underfull \\\\\\\\hbox (badness 6268) in paragraph at lines 464--467\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 464--467\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 464--467\\\", \\\"Underfull \\\\\\\\hbox (badness 1552) in paragraph at lines 464--467\\\", \\\"Underfull \\\\\\\\hbox (badness 4266) in paragraph at lines 469--472\\\", \\\"Underfull \\\\\\\\hbox (badness 1418) in paragraph at lines 550--555\\\", \\\"Underfull \\\\\\\\hbox (badness 2894) in paragraph at lines 582--585\\\", \\\"Underfull \\\\\\\\hbox (badness 5008) in paragraph at lines 582--585\\\", \\\"Underfull \\\\\\\\hbox (badness 1859) in paragraph at lines 682--683\\\", \\\"Underfull \\\\\\\\hbox (badness 1838) in paragraph at lines 685--687\\\", \\\"Overfull \\\\\\\\hbox (27.00938pt too wide) in paragraph at lines 698--708\\\", \\\"Underfull \\\\\\\\vbox (badness 2781) has occurred while \\\\\\\\output is active []\\\", \\\"Underfull \\\\\\\\vbox (badness 10000) has occurred while \\\\\\\\output is active []\\\", \\\"Overfull \\\\\\\\hbox (50.91055pt too wide) in paragraph at lines 723--738\\\", \\\"Overfull \\\\\\\\hbox (47.2356pt too wide) in paragraph at lines 745--756\\\", \\\"Underfull \\\\\\\\hbox (badness 1655) in paragraph at lines 790--790\\\", \\\"Underfull \\\\\\\\hbox (badness 1769) in paragraph at lines 790--790\\\", \\\"Overfull \\\\\\\\hbox (46.87402pt too wide) in paragraph at lines 792--805\\\", \\\"Underfull \\\\\\\\hbox (badness 5133) in paragraph at lines 818--50\\\", \\\"Underfull \\\\\\\\hbox (badness 7081) in paragraph at lines 818--50\\\"], \\\"issues\\\": [\\\"pages 23 > limit 8\\\"], \\\"summary\\\": \\\"FAIL: pages 23 > limit 8\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"passed\": false, \"compiled\": {\"success\": true, \"pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf\", \"paper_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper\", \"main_tex\": \"main.tex\", \"log_tail\": \"\\nOverfull \\\\hbox (47.2356pt too wide) in paragraph at lines 745--756\\n [][] \\n []\\n\\n\\nUnderfull \\\\hbox (badness 1655) in paragraph at lines 790--790\\n[]\\\\T1/ptm/m/n/10 (+20) Table 22: |Cross-dataset OOD qual-ity es-ti-ma-tion\\n []\\n\\n\\nUnderfull \\\\hbox (badness 1769) in paragraph at lines 790--790\\n\\\\T1/ptm/m/n/10 (+20) in-stances ($\\\\OML/cmm/m/it/10 n[]\\\\OT1/cmr/m/n/10 2756$\\\\T1/\\nptm/m/n/10 (+20) ). CoNLL$\\\\OMS/cmsy/m/n/10 !$\\\\T1/ptm/m/n/10 (+20) SciERC: CoNLL\\n-\\n []\\n\\n\\nOverfull \\\\hbox (46.87402pt too wide) in paragraph at lines 792--805\\n [][] \\n []\\n\\n[22])\\nUnderfull \\\\hbox (badness 5133) in paragraph at lines 818--50\\n []\\\\T1/ptm/b/n/10.95 (+20) Asymmetry in-ter-pre-ta-tion.[] \\\\T1/ptm/m/n/10.95 (+\\n20) The di-rec-tional\\n []\\n\\n\\nUnderfull \\\\hbox (badness 7081) in paragraph at lines 818--50\\n\\\\T1/ptm/m/n/10.95 (+20) asym-me-try is driven by schema cov-er-age:\\n []\\n\\n[23\\n\\n] (./main.aux)\\n ***********\\nLaTeX2e <2025-11-01>\\nL3 programming layer <2026-01-19>\\n ***********\\nPackage rerunfilecheck Info: File `main.out' has not changed.\\n(rerunfilecheck)             Checksum: 12754B12DD2F90E2AB798D6280AE20BA;4768.\\n ) \\nHere is how much of TeX's memory you used:\\n 16909 strings out of 469438\\n 267249 string characters out of 5468411\\n 748286 words of memory out of 5000000\\n 44542 multiletter control sequences out of 15000+600000\\n 722220 words of font info for 470 fonts, out of 8000000 for 9000\\n 59 hyphenation exceptions out of 8191\\n 84i,12n,93p,1001b,698s stack positions out of 10000i,1000n,20000p,200000b,200000s\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/inconsolata/Inconsolata-zi4\\nr.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx9.pfb><\\n/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/s\\nhare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/t\\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive\\n/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-\\ndist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fo\\nnts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\\ne1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\\nic/amsfonts/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf\\nonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/\\ncmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb\\n>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr\\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/\\ntexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive\\n/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-\\ndist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fo\\nnts/type1/public/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fon\\nts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-dist/font\\ns/type1/urw/helvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/\\ntimes/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pf\\nb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\\nOutput written on main.pdf (23 pages, 659460 bytes).\\nPDF statistics:\\n 1601 PDF objects out of 1728 (max. 8388607)\\n 1064 compressed objects within 11 object streams\\n 221 named destinations out of 1000 (max. 500000)\\n 85268 words of extra memory for PDF output out of 89155 (max. 10000000)\\n\", \"error\": \"\", \"pages\": 23, \"warnings\": [\"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\"]}, \"pages\": 23, \"page_status\": \"over_limit\", \"max_pages\": 8, \"min_pages\": null, \"critical_warnings\": [], \"minor_warnings\": [\"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"Underfull \\\\hbox (badness 3333) in paragraph at lines 19--20\", \"Underfull \\\\hbox (badness 1152) in paragraph at lines 37--39\", \"Underfull \\\\hbox (badness 2556) in paragraph at lines 13--19\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 1226) in paragraph at lines 71--74\", \"Underfull \\\\hbox (badness 3668) in paragraph at lines 14--20\", \"Underfull \\\\hbox (badness 1377) in paragraph at lines 14--20\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 111--114\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 111--114\", \"Underfull \\\\hbox (badness 5036) in paragraph at lines 119--1\", \"Underfull \\\\hbox (badness 1616) in paragraph at lines 119--1\", \"Underfull \\\\hbox (badness 1242) in paragraph at lines 8--15\", \"Underfull \\\\hbox (badness 1365) in paragraph at lines 147--152\", \"Underfull \\\\hbox (badness 1158) in paragraph at lines 183--191\", \"Underfull \\\\hbox (badness 1043) in paragraph at lines 205--211\", \"Underfull \\\\hbox (badness 1742) in paragraph at lines 205--211\", \"Underfull \\\\hbox (badness 1184) in paragraph at lines 214--219\", \"Underfull \\\\hbox (badness 1990) in paragraph at lines 229--233\", \"Underfull \\\\hbox (badness 1824) in paragraph at lines 303--307\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 311--319\", \"Underfull \\\\hbox (badness 1082) in paragraph at lines 311--319\", \"Underfull \\\\hbox (badness 4454) in paragraph at lines 311--319\", \"Underfull \\\\hbox (badness 1681) in paragraph at lines 382--388\", \"Underfull \\\\hbox (badness 8056) in paragraph at lines 90--93\", \"Underfull \\\\hbox (badness 5802) in paragraph at lines 90--93\", \"Underfull \\\\hbox (badness 1253) in paragraph at lines 90--93\", \"Underfull \\\\hbox (badness 1715) in paragraph at lines 90--93\", \"Underfull \\\\hbox (badness 2635) in paragraph at lines 90--93\", \"Underfull \\\\vbox (badness 6910) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 1990) in paragraph at lines 109--113\", \"Underfull \\\\hbox (badness 2753) in paragraph at lines 134--140\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 134--140\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 134--140\", \"Underfull \\\\hbox (badness 1082) in paragraph at lines 134--140\", \"Underfull \\\\hbox (badness 1072) in paragraph at lines 134--140\", \"Underfull \\\\hbox (badness 6691) in paragraph at lines 134--140\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 134--140\", \"Underfull \\\\hbox (badness 1019) in paragraph at lines 142--145\", \"Overfull \\\\hbox (0.91821pt too wide) in paragraph at lines 147--153\", \"Underfull \\\\hbox (badness 1033) in paragraph at lines 155--159\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Overfull \\\\hbox (19.10843pt too wide) in paragraph at lines 165--176\", \"Underfull \\\\hbox (badness 4060) in paragraph at lines 254--257\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Overfull \\\\hbox (18.97287pt too wide) in paragraph at lines 316--329\", \"Underfull \\\\hbox (badness 1210) in paragraph at lines 333--337\", \"Overfull \\\\hbox (75.87871pt too wide) in paragraph at lines 343--359\", \"Overfull \\\\hbox (0.76773pt too wide) in paragraph at lines 370--395\", \"Underfull \\\\hbox (badness 2460) in paragraph at lines 410--410\", \"Underfull \\\\hbox (badness 3514) in paragraph at lines 410--410\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 464--467\", \"Underfull \\\\hbox (badness 1810) in paragraph at lines 464--467\", \"Underfull \\\\hbox (badness 1845) in paragraph at lines 464--467\", \"Underfull \\\\hbox (badness 1442) in paragraph at lines 464--467\", \"Underfull \\\\hbox (badness 1845) in paragraph at lines 464--467\", \"Underfull \\\\hbox (badness 2277) in paragraph at lines 464--467\", \"Underfull \\\\hbox (badness 2626) in paragraph at lines 464--467\", \"Underfull \\\\hbox (badness 6268) in paragraph at lines 464--467\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 464--467\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 464--467\", \"Underfull \\\\hbox (badness 1552) in paragraph at lines 464--467\", \"Underfull \\\\hbox (badness 4266) in paragraph at lines 469--472\", \"Underfull \\\\hbox (badness 1418) in paragraph at lines 550--555\", \"Underfull \\\\hbox (badness 2894) in paragraph at lines 582--585\", \"Underfull \\\\hbox (badness 5008) in paragraph at lines 582--585\", \"Underfull \\\\hbox (badness 1859) in paragraph at lines 682--683\", \"Underfull \\\\hbox (badness 1838) in paragraph at lines 685--687\", \"Overfull \\\\hbox (27.00938pt too wide) in paragraph at lines 698--708\", \"Underfull \\\\vbox (badness 2781) has occurred while \\\\output is active []\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Overfull \\\\hbox (50.91055pt too wide) in paragraph at lines 723--738\", \"Overfull \\\\hbox (47.2356pt too wide) in paragraph at lines 745--756\", \"Underfull \\\\hbox (badness 1655) in paragraph at lines 790--790\", \"Underfull \\\\hbox (badness 1769) in paragraph at lines 790--790\", \"Overfull \\\\hbox (46.87402pt too wide) in paragraph at lines 792--805\", \"Underfull \\\\hbox (badness 5133) in paragraph at lines 818--50\", \"Underfull \\\\hbox (badness 7081) in paragraph at lines 818--50\"], \"issues\": [\"pages 23 > limit 8\"], \"summary\": \"FAIL: pages 23 > limit 8\"}"
    }
  },
  "sourceToolAssistantUUID": "b582b1ac-b18c-4670-9700-89cbf0e43038",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite"
}
```

</details>

---


### Runtime record

_source line 6173_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] [Patch] Round 8 高优先写作修复——不依赖正在跑的实验，立即处理。  按优先级排序：  ## 1. R8-N1 页数压缩至 ≤8 页（CRITICAL，desk-rejection 风险） 当前估计 10-11 页正文。压缩策略： - Discussion free-form ablation 详述移至 Appendix（~0.5 页） - Robustn…",
  "leafUuid": "16bea775-d30e-4f95-86f5-45b2f63a5c83",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6"
}
```

---


### Runtime record

_source line 6174_

```json
{
  "type": "ai-title",
  "aiTitle": "Set up agent communication with Director",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6"
}
```

---


### Runtime record

_source line 6175_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] [Patch] Round 8 高优先写作修复——不依赖正在跑的实验，立即处理。  按优先级排序：  ## 1. R8-N1 页数压缩至 ≤8 页（CRITICAL，desk-rejection 风险） 当前估计 10-11 页正文。压缩策略： - Discussion free-form ablation 详述移至 Appendix（~0.5 页） - Robustn…",
  "leafUuid": "16bea775-d30e-4f95-86f5-45b2f63a5c83",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6"
}
```

---


### Runtime record

_source line 6176_

```json
{
  "type": "ai-title",
  "aiTitle": "Set up agent communication with Director",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6"
}
```

---


### System

_source line 6177 · 2026-05-15T17:58:14.885Z_

```json
{
  "parentUuid": null,
  "logicalParentUuid": "16bea775-d30e-4f95-86f5-45b2f63a5c83",
  "isSidechain": false,
  "type": "system",
  "subtype": "compact_boundary",
  "content": "Conversation compacted",
  "isMeta": false,
  "timestamp": "2026-05-15T17:58:14.885Z",
  "uuid": "eb7bd92e-6fca-41d6-9f5c-b133bc007d22",
  "level": "info",
  "compactMetadata": {
    "trigger": "auto",
    "preTokens": 167900,
    "preCompactDiscoveredTools": [
      "RemoteTrigger",
      "TodoWrite",
      "WebSearch",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__paper_agent_post_to_director",
      "mcp__agent-ml-research__paper_agent_request_review",
      "mcp__agent-ml-research__paper_compile_and_check",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap"
    ],
    "postTokens": 10242,
    "durationMs": 137826
  },
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite"
}
```

---


## Round 347

## Round 347

77 recorded events


### User

_source line 6178 · 2026-05-15T17:58:14.886Z_

This session is being continued from a previous conversation that ran out of context. The summary below covers the earlier portion of the conversation.

Summary:
1. Primary Request and Intent:
   The user is the Director coordinating an EMNLP 2026 Findings paper (DDL 2026-05-25) for project "struct_self_consist_ie." I am the Paper Agent. This session covers multiple patch operations:
   
   a) **LP T=0.7 data integration** — Update robustness table, §4.4, temperature text, figure caption, and Limitations with new LP T=0.7 data (NER ρ=0.249).
   b) **ε sweep analysis** — Add ε robustness section to Appendix + §4.2 footnote, responding to R2 reviewer concern.
   c) **Framing corrections** — SJ N=16 as gap evidence, CoNLL headroom caveat.
   d) **Model name verification** — Confirm no "Qwen2.5-7B" in paper.
   e) **exp-001 N=16 subset check** — Verify paper uses full-set (529) not 200-instance subset data.
   f) **Round 8 CPU analyses** — Thinking token LP dilution (3-part argument), SJ normalizer sensitivity, seed 456 LP range.
   g) **Round 8 major patch** — Page compression to ≤8 pages (CRITICAL), Abstract rewrite, RE preliminary markers, Gap reframing, Table 3 restructuring, plus 6 minor fixes.

2. Key Technical Concepts:
   - Correlation-selection gap: instance-level signals predict quality but cannot select best sample
   - LP score compression: median within-instance LP range 0.041 nats
   - Binary-outcome regime: RE's 40% zero-F1 rate makes LP more informative than structural overlap
   - Task-dependent signal rankings: NER structural > LP; RE LP > structural
   - ε sensitivity: convenience threshold, Spearman ρ is ε-free continuous measure
   - Thinking token confound: 0.001 nats LP shift (2.68%), constant prefix cancellation, CoNLL control group contradicts hypothesis
   - MBR decoding: consensus-proximity selection correlates across but not within instances
   - Temperature sensitivity: LP has largest effect (Δρ=+0.044), signal hierarchy preserved
   - SJ normalizer robustness: max vs union Δρ=0.005, ΔAUROC=0.003

3. Files and Code Sections:

   - **`docs/paper/sections/appendix.tex`** (MODIFIED extensively):
     - Robustness table (tab:robustness): SJ T=0.7 NER 0.364, FK T=0.7 NER 0.289, added LP T=0.7/T=1.0 rows
     - Temperature sensitivity text: All values updated, LP analysis added, hierarchy updated to SJ>FK>LP
     - Figure caption: Updated LP temperature info
     - SJ normalizer: Added ΔAUROC=0.003
     - Seed 456 LP range: Already present (0.040 nats, 62.2%)
     - NEW section: Thinking Token Impact Analysis (app:thinking_token) with 3 paragraphs
     - CoNLL control group updated: Added T=1.0 tied fraction 86.8%
     - NEW paragraph: ε robustness of selection F1 (app:epsilon_robustness)
     - NEW table: tab:epsilon_robustness (5 signals × 4 configs, max F1 variation)

   - **`docs/paper/sections/experiments.tex`** (MODIFIED extensively):
     - §4.4: LP exclusion replaced with "LP exhibits largest temperature sensitivity on NER (Δρ=+0.044)"
     - §4.1 thinking tokens: Compressed from 4 lines to 2, references Appendix~ref{app:thinking_token}
     - §4.2: Added footnote about ε=0.05 being convenience threshold
     - §4.3 opening: Compressed, reframed around LP as non-trivial question
     - Table 3 (tab:selection): Added visual separators — "Per-sample signal" above LP, "Instance-level signals (consensus-proximity selection)" above SJ/FK/EM/VC
     - Seed variability: Merged into QE≠selection paragraph
     - QE≠selection paragraph: Compressed from 4 lines to 3
     - CoNLL caveat: Added "though CoNLL's limited oracle headroom (≤4.0 pp at N=8) constrains selection comparison"

   - **`docs/paper/sections/discussion.tex`** (MODIFIED extensively):
     - Practical recommendations: Compressed from 5 lines to 2 lines
     - Gap widens with N: Added SJ N=16 data "SJ---the strongest quality estimator at N=16 (ρ=0.411)---selects to −0.05 pp below greedy"
     - Free-form ablation: Compressed from 8 lines to 2 lines (details → Appendix refs)
     - Current full content after edits:
       ```latex
       \paragraph{Practical recommendations.}
       For quality ranking, VC leads on hard NER ($\rho{=}0.38$) while EM leads easy NER and binary discrimination (AUROC${=}0.816$, CoNLL); on RE (preliminary), LP outperforms structural signals (Table~\ref{tab:multiseed}), likely because RE's 40\% zero-F1 rate favors generation confidence.
       Rankings are consistent across two 8B-scale model families; at $N{=}16$, SJ converges to VC (Appendix~\ref{app:robustness}); at the capability boundary (WNUT-17), all signals collapse (Table~\ref{tab:wnut}).
       
       \paragraph{Why the gap exists: two layers.}
       [unchanged]
       
       \paragraph{The gap widens with $N$.}
       Doubling from $N{=}8$ to $N{=}16$ expands oracle headroom by $+4.4$~pp, yet SJ---the strongest quality estimator at $N{=}16$ ($\rho{=}0.411$)---selects to $-0.05$~pp below greedy, LP improves by only $+0.4$~pp, and VC deteriorates...
       
       \paragraph{Ablation: free-form decoding.}\label{sec:ablation}
       Removing grammar constraints entirely (SciERC, Qwen3-8B) yields nearly identical LP distributions (within-instance std ratio $0.97{\times}$, tied fraction $-2$~pp) and negligible selection changes, ruling out constrained decoding as the cause (Appendix~\ref{app:freeform_ablation}).
       Our consensus-proximity strategies instantiate MBR decoding \cite{eikema2022sampling}; all fail because utility correlates with F1 across instances but not within them (Appendix~\ref{app:mbr_discussion}).
       
       \paragraph{Methodological implications.}
       [unchanged]
       ```

   - **`docs/paper/sections/introduction.tex`** (MODIFIED):
     - Constrained decoding: 2 lines → 1 line
     - Central finding: 3 lines → 2 lines
     - Contribution bullets: All three compressed, specific numbers removed
     - R7-W2: Contribution 1 now says "We find that quality estimation, binary discrimination, and sample selection decouple"

   - **`docs/paper/sections/abstract.tex`** (REWRITTEN):
     ```latex
     \begin{abstract}
     Self-consistency---sampling multiple outputs and selecting via agreement---yields large gains on discrete-answer tasks, but information extraction (IE) produces \textit{sets} of entities and relations with partial overlap, where no majority vote exists.
     
     We evaluate five confidence signals for LLM-based IE across three NER benchmarks and one RE benchmark (preliminary) with two 8B-parameter models, revealing the \textit{correlation-selection gap}: all signals achieve strong quality estimation yet none significantly improves sample selection despite substantial oracle headroom.
     The gap has two layers: instance-level signals cannot rank candidates by construction, and log-probability---the only per-sample signal---is too compressed within instances to discriminate (median range 0.041 nats); where compression is mitigated, selection recovers significant gains.
     Signal rankings shift with task difficulty and type, and collapse at the capability boundary.
     
     Closing the gap likely requires learned per-sample scoring such as trained verifiers.
     \end{abstract}
     ```

   - **`docs/paper/sections/limitations.tex`** (MODIFIED):
     - LP T=0.7 exclusion: Replaced 3 paragraphs with concise 3 lines about LP temperature being limited to SciERC NER
     - Thinking token: Condensed from 4 lines to 2, references Appendix~ref{app:thinking_token}
     - Seed 456: Added LP range consistency sentence

   - **`docs/paper/sections/conclusion.tex`** — Read but not modified this session; already has RE preliminary and task-dependent findings.

   - **`docs/paper/main.tex`** — Title already "Struggle to Select"; Code/Data already in Ethics Statement (line 44).

   - **`docs/paper/sections/related_work.tex`** — Read; Eikema references already present in MBR context (lines 25, 28).

4. Errors and fixes:
   - **System reminder false positives**: Multiple "[系统提醒] 你刚才完成了 [Director 指令] 但没有调用 main_agent_post_to_director" appeared even when I had already reported or when no report was needed. I correctly responded "No response requested."
   - **Duplicate Director instructions**: The Round 8 CPU analysis was sent twice (R8-W2/W3/W4). I identified the duplicate and only added the missing data points (CoNLL T=1.0 86.8%, seed 456 LP range in Limitations).
   - **exp-001 subset concern**: Director warned about 200/529 subset, but registry showed full-set rerun already completed (ner_n=529). paper_framing.md warning was stale.
   - **Page count tool limitation**: paper_compile_and_check always reports "FAIL" because it counts all 23 pages (including appendix) against the 8-page limit. Must manually verify main body page count.

5. Problem Solving:
   - **LP T=0.7 integration**: Systematically updated 5 locations, verified no stale values with grep
   - **ε sweep**: Created compact 5×4 table + analytical paragraph addressing R2 reviewer concern
   - **Thinking token defense**: Built 3-part quantitative argument (shift magnitude, constant prefix, CoNLL control)
   - **Page compression**: Compressed Introduction (~3 lines saved), Experiments (~5 lines), Discussion (~8 lines). Free-form ablation moved to appendix reference. Total savings estimated ~1.5 pages.
   - **Gap reframing**: Table 3 visual separation between per-sample and instance-level signals

6. All user messages:
   - "Continue from where you left off." (initial, after context restoration)
   - "[系统提醒] 你刚才完成了 [Director 指令] 但没有调用 main_agent_post_to_director..." (multiple times — false positives)
   - "Continue from where you left off." (multiple times between actions)
   - "[Director 指令] ε sweep 分析结果 — 请加入论文（BLOCKING #2 修复）" — ε sweep data + write suggestions
   - "[Director 指令] ε sweep 分析完成 + 写作注意事项" — ε robustness + SJ/VC framing warnings + CoNLL caveat
   - "[Director 指令] 模型名修正提醒" — Qwen2.5-7B → Qwen3-8B check
   - "[Director 指令] Reviewer 审查 ROADMAP D095 时标记了两个 warning" — epsilon_sweep model name + exp-001 N=16 subset
   - "[Director 指令] [Patch] Round 8 审稿回应——三项 CPU 分析结果" — Thinking token, SJ normalizer, Seed 456 LP
   - "[Director 指令] [Patch] Round 8 reviewer concerns 新数据——3 项 CPU 分析结果已就绪" — Same 3 items (duplicate)
   - "[Director 指令] [Patch] Round 8 高优先写作修复——不依赖正在跑的实验" — 6-item major patch: page compression, title, abstract, RE preliminary, gap reframing, minor fixes

7. Pending Tasks:
   - **Verify actual main body page count** — Need to check if compressions brought main content ≤8 pages. The compile tool only reports total pages (23). Need pdf_to_images or pdftotext to verify page breakdown.
   - **Further page compression if needed** — Director estimated 10-11 pages; my compressions may have saved ~1-1.5 pages. May need additional cuts.
   - **R5-W7**: SJ as "primary structural signal" — Not yet addressed
   - **R4-W1**: RE preliminary markers throughout — Abstract done ("preliminary"), but need systematic check across all files
   - **Remaining minor fixes check**: R8-M1 bib key (already clean), R7-W3 Eikema (already in Related Work), others verified

8. Current Work:
   I was executing the Round 8 major patch (6 items). I completed:
   - Page compression in Introduction, Experiments (§4.1, §4.3), Discussion (recommendations, ablation)
   - Abstract rewrite (three-part structure with RE preliminary)
   - Table 3 restructuring (per-sample vs instance-level separators)
   - §4.3 gap reframing
   - Contribution bullet rewording (R7-W2)
   - Verified title, model names, Eikema, bib keys, Code/Data all already correct
   
   Compiled successfully (23 pages total, no critical warnings) but have NOT yet verified the actual main body page count to confirm the ≤8 page target is met.

9. Optional Next Step:
   Verify the main body page count using pdf_to_images or pdftotext to determine if the page compression was sufficient for the ≤8 page CRITICAL requirement. The Director's instruction stated: "R8-N1 页数压缩至 ≤8 页（CRITICAL，desk-rejection 风险）当前估计 10-11 页正文。" If still over 8 pages, apply additional compression to Experiments QE results paragraphs, Related Work, or Method sections. Then report to Director with full patch status covering all 6 items.

If you need specific details from before compaction (like exact code snippets, error messages, or content you generated), read the full transcript at: /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-paper-agent-4f1165b4/9fa88e93-92fc-446f-90c6-86ed7a5c1cb6.jsonl
Continue the conversation from where it left off without asking the user any further questions. Resume directly — do not acknowledge the summary, do not recap what was happening, do not preface with "I'll continue" or similar. Pick up the last task as if the break never happened.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eb7bd92e-6fca-41d6-9f5c-b133bc007d22",
  "isSidechain": false,
  "promptId": "4ab6fc0d-e7b3-4753-81c9-824338d4b6fc",
  "type": "user",
  "isVisibleInTranscriptOnly": true,
  "isCompactSummary": true,
  "uuid": "947c9223-32fc-4304-88a3-ab29e6a03a79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite"
}
```

</details>

---


### Runtime record

_source line 6179 · 2026-05-15T17:58:14.630Z_

```json
{
  "parentUuid": "947c9223-32fc-4304-88a3-ab29e6a03a79",
  "isSidechain": false,
  "attachment": {
    "type": "file",
    "filename": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex",
    "content": {
      "type": "text",
      "file": {
        "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex",
        "content": "\\begin{abstract}\nSelf-consistency---sampling multiple outputs and selecting via agreement---yields large gains on discrete-answer tasks, but information extraction (IE) produces \\textit{sets} of entities and relations with partial overlap, where no majority vote exists.\n\nWe evaluate five confidence signals for LLM-based IE across three NER benchmarks and one RE benchmark (preliminary) with two 8B-parameter models, revealing the \\textit{correlation-selection gap}: all signals achieve strong quality estimation yet none significantly improves sample selection despite substantial oracle headroom.\nThe gap has two layers: instance-level signals cannot rank candidates by construction, and log-probability---the only per-sample signal---is too compressed within instances to discriminate (median range 0.041 nats); where compression is mitigated, selection recovers significant gains.\nSignal rankings shift with task difficulty and type, and collapse at the capability boundary.\n\nClosing the gap likely requires learned per-sample scoring such as trained verifiers.\n\\end{abstract}\n",
        "numLines": 10,
        "startLine": 1,
        "totalLines": 10
      }
    },
    "displayPath": "../../../docs/paper/sections/abstract.tex"
  },
  "type": "attachment",
  "uuid": "4a219935-8fb6-4d87-8671-94a07ddaec3d",
  "timestamp": "2026-05-15T17:58:14.630Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite"
}
```

---


### Runtime record

_source line 6180 · 2026-05-15T17:58:14.882Z_

```json
{
  "parentUuid": "4a219935-8fb6-4d87-8671-94a07ddaec3d",
  "isSidechain": false,
  "attachment": {
    "type": "file",
    "filename": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
    "content": {
      "type": "text",
      "file": {
        "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
        "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe evaluate on three English IE benchmarks spanning a difficulty gradient.\n\\textbf{SciERC} \\cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).\n\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\\approx}$91\\% micro F1.\n\\textbf{WNUT-17} \\cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (52\\% zero F1).\n\n\\paragraph{Models and sampling.}\nBoth \\textbf{Qwen3-8B} and \\textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\\alpha{=}64$) for 5 epochs using LLaMA Factory \\cite{zheng2024llamafactory} under identical training procedures, ensuring comparisons across the two model families (both at 8B scale) reflect model differences rather than training confounds.\nQwen3-8B's SciERC checkpoint has a minor train--test mismatch: empty \\texttt{&lt;think>&lt;/think>} blocks (4--5 tokens, no reasoning content) were included in training but are suppressed by constrained decoding at inference; CoNLL and WNUT-17 are unaffected.\nA quantitative analysis rules out this confound (Appendix~\\ref{app:thinking_token}).\nWe draw $N{=}8$ samples at $T{=}1.0$ (primary; single seed, seed${=}42$), with $N{=}16$ for scaling experiments.\\footnote{$N{=}8$ establishes the primary baseline at minimal compute cost; $N{=}16$ with multiple seeds verifies scaling behavior. $N$-scaling analysis (Appendix~\\ref{app:n_scaling}) shows sublinear gains beyond $N{=}8$. $N{=}16$ results in Table~\\ref{tab:robustness} (Appendix~\\ref{app:robustness}); 3-seed stability ($\\sigma{\\leq}0.026$; Table~\\ref{tab:multiseed}, Appendix~\\ref{app:multiseed}) confirms identical signal rankings across seeds.}\nQuality estimation uses Spearman $\\rho$ and AUROC; downstream utility uses best-of-$N$ selection macro F1 (instance-averaged) with exact span matching (NER) and head-tail-label matching (RE).\nInference uses vLLM with constrained decoding \\cite{willard2023guided}.\n\n%% ============================================================\n\\subsection{Quality Estimation Results}\n\\label{sec:qe_results}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Quality estimation across tasks and models (Spearman $\\rho$ and AUROC; $N{=}8$, seed${=}42$). Best value per column in \\textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types, single benchmark---preliminary); CoNLL evaluates NER (4 types). $N{=}16$ results appear in Table~\\ref{tab:robustness} (Appendix~\\ref{app:robustness}).}\n\\label{tab:quality_estimation}\n\\begin{tabular}{ll cc cc cc cc}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{SciERC NER}} & \\multicolumn{2}{c}{\\textbf{SciERC RE}} & \\multicolumn{2}{c}{\\textbf{CoNLL (Qwen)}} & \\multicolumn{2}{c}{\\textbf{CoNLL (LLaMA)}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-8} \\cmidrule(lr){9-10}\nSignal & Family & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC \\\\\n\\midrule\nVC & Structural & \\textbf{.379} & \\textbf{.663} & \\textbf{.350} & .694 & .424 & .789 & .426 & .709 \\\\\nSJ  & Structural & .360 & .650 & .250 & .670 & .436 & .801 & \\textbf{.431} & .704 \\\\\nFK & Surface & .267 & .602 & .275 & .609 & .400 & .774 & .428 & .703 \\\\\nEM  & Surface    & .295 & .614 & .134 & \\textbf{.706} & \\textbf{.451} & \\textbf{.816} & \\textbf{.431} & .705 \\\\\n\\midrule\nLP     & Model      & .205 & .578 & .266 & .601 & .316 & .753 & .307 & \\textbf{.761} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_signal_heatmap}\n\\caption{Quality estimation heatmap (Spearman $\\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC NER while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\\rho{=}0.360$) and RE ($\\rho{=}0.417$), while LP RE collapses to near-zero ($\\rho{=}0.011$).}\n\\label{fig:signal_heatmap}\n\\end{figure*}\n\nTable~\\ref{tab:quality_estimation} presents rank correlation ($\\rho$) and AUROC for five confidence signals across tasks and models.\\footnote{$\\varepsilon{=}0.05$ is a convenience threshold used only in the selection analysis (\\S\\ref{sec:selection_gap}); quality estimation metrics ($\\rho$, AUROC) are continuous and $\\varepsilon$-free. Selection F1 is stable across $\\varepsilon \\in [0, 0.2]$ (Appendix~\\ref{app:epsilon_robustness}).}\n\n\\paragraph{Difficulty-dependent signal complementarity.}\nOn SciERC NER (6 types), structural signals lead: VC $\\rho{=}0.379$, SJ $\\rho{=}0.360$, both outperforming surface ($\\rho{\\leq}0.295$) and LP ($\\rho{=}0.205$); on RE, VC extends this advantage ($\\rho{=}0.350$; preliminary), but the remaining hierarchy reverses: multi-seed analysis shows LP rises above both SJ and FK (Table~\\ref{tab:multiseed}), likely because RE's 40\\% zero-F1 rate creates a binary-outcome regime where generation confidence outperforms structural overlap.\nThe best NER AUROC reaches 0.816 (EM, CoNLL Qwen), indicating strong binary discriminative power; pairwise bootstrap CIs confirm the SJ--LP gap ($\\Delta\\rho{=}{+}0.155$, CI excludes zero) but the SJ--EM gap is marginal (Appendix~\\ref{app:bootstrap_signal}).\n\n\\paragraph{$\\rho$--AUROC dissociation.}\nSignal choice depends on use case: on CoNLL, EM leads AUROC (0.816) despite a middling $\\rho$ (0.451), preferred for binary triage; this dissociation replicates across configurations (LP leads AUROC at 0.761 on CoNLL LLaMA yet trails in $\\rho$).\n\n\\paragraph{Signal rankings shift with task difficulty.}\nOn CoNLL (greedy F1${\\approx}$0.91), EM leads ($\\rho{=}0.451$, AUROC${=}0.816$); this crossover---EM${>}$SJ on easy tasks vs.\\ SJ${>}$EM on hard tasks---demonstrates difficulty-dependent complementarity, consistent across model families.\nOn WNUT-17 (52\\% zero F1), full-set VC achieves $\\rho{=}0.724$ but conditional $\\rho{=}0.038$ (n.s.; Table~\\ref{tab:wnut}); LP exhibits strong \\textit{negative} correlation ($\\rho{=}{-}0.410$); all conditional signals collapse, suggesting a capability boundary beyond which consistency captures binary success/failure but not quality gradation.\n\n\\paragraph{Conditional filtering.}\nRestricting to non-zero F1 instances reshuffles signal rankings (Figure~\\ref{fig:signal_heatmap}, right): EM emerges as the strongest conditional signal on both NER ($\\rho{=}0.360$) and RE ($\\rho{=}0.417$; preliminary), while structural signals drop substantially (VC NER: $0.379{\\to}0.300$) and LP RE collapses to $\\rho{=}0.011$ (Appendix~\\ref{app:additional}).\n\n%% ============================================================\n\\subsection{The Correlation-Selection Gap}\n\\label{sec:selection_gap}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). NER: 2-seed mean${\\pm}\\sigma$ ($n{=}551$), Fisher combined $p$ vs.\\ greedy; RE: single seed (preliminary). Best non-oracle in \\textbf{bold}. $^\\dagger$Greedy: a fixed $T{=}1.0$ sample (not $T{=}0$), serving as the no-selection reference. VC selection uses majority-threshold voting ($\\text{freq}{>}N/2$; see \\S\\ref{sec:signals}).}\n\\label{tab:selection}\n\\begin{tabular}{lccc}\n\\toprule\nMethod & NER F1 & $p$ & RE F1 \\\\\n\\midrule\nOracle & $0.778 \\pm 0.003$ & --- & 0.585 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Per-sample signal}} \\\\\nLP           & $\\mathbf{0.647} \\pm 0.005$ & .29 & 0.395 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Instance-level signals (consensus-proximity selection)}} \\\\\nSJ           & $0.646 \\pm 0.002$ & .68 & 0.386 \\\\\nFK           & $0.646 \\pm 0.001$ & .79 & --- \\\\\nEM           & $0.637 \\pm 0.001$ & .45 & 0.372 \\\\\nVC           & $0.623 \\pm 0.004$ & .26 & 0.359 \\\\\n\\midrule\nGreedy$^\\dagger$ & $0.645 \\pm 0.001$ & --- & \\textbf{0.404} \\\\\nRandom           & $0.610 \\pm 0.003$ & --- & 0.354 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDespite strong quality estimation, confidence signals yield limited gains for best-of-$N$ selection (Table~\\ref{tab:selection}; see also Figure~\\ref{fig:selection_gap}).\nFour of five signals are instance-level by construction (they assign identical scores to all candidates); the non-trivial question is whether LP---the only per-sample signal---can exploit the oracle headroom.\nWe anchor on SciERC, where output diversity is substantial (39--43\\% unique outputs; Appendix~\\ref{app:diversity}).\n\n\\paragraph{No significant improvement over greedy.}\nWe evaluate significance via 2-seed instance-level sign tests ($n{=}551$, Fisher combination).\nOn NER, the oracle (0.778) reveals 13.3~pp of headroom above greedy (0.645).\nLP achieves the highest mean selection F1 (0.647), indistinguishable from greedy ($\\Delta{=}{+}0.2$~pp, $p{=}0.29$); all other signals also fail to reach significance (all $p{>}0.05$; Table~\\ref{tab:selection}), with 75--80\\% of instances producing identical F1 under signal selection and greedy.\nOn RE, the best signal (LP, 0.395) falls below greedy (0.404, $-0.9$\\,pp; single seed, preliminary), while 18.1~pp of oracle headroom remains.\nVC, the best quality estimator ($\\rho{=}0.379$), selects to only 0.623 on NER ($\\Delta{=}{-}2.2$~pp, $p{=}0.26$); the direction is consistent with CoNLL and WNUT-17 (Table~\\ref{tab:cross_selection}), though CoNLL's limited oracle headroom (${\\leq}4.0$~pp at $N{=}8$) constrains selection comparison.\n\n\\paragraph{Quality estimation $\\neq$ output selection.}\nInstance-level signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} is best; when per-sample variance is low, even perfect quality estimation fails to discriminate.\nIndividual seeds exhibit notable variance (even the best seed $p{=}0.19$), motivating multi-seed evaluation.\nClosing this gap likely requires per-sample signals such as trained verifiers \\cite{cobbe2021verifiers}.\n\n%% ============================================================\n\\subsection{Robustness}\n\\label{sec:robustness_main}\n\nConsistency-based signals are robust across $T{\\in}\\{0.7, 1.0\\}$ and show sublinear gains from $N{=}8$ to $N{=}16$ (Table~\\ref{tab:robustness}, Appendix~\\ref{app:robustness}); LP exhibits the largest temperature sensitivity on NER ($\\Delta\\rho{=}{+}0.044$), with the signal hierarchy preserved across temperatures.\nNER signals are reasonably calibrated (ECE 0.069--0.096; Appendix~\\ref{app:calibration}); RE miscalibration (ECE up to 0.339, preliminary) imposes a ceiling at $\\rho{\\approx}0.28$ for $N{=}16$.\n",
        "numLines": 121,
        "startLine": 1,
        "totalLines": 121
      }
    },
    "displayPath": "../../../docs/paper/sections/experiments.tex"
  },
  "type": "attachment",
  "uuid": "e5903e0d-1780-427a-ba67-6df19ea95363",
  "timestamp": "2026-05-15T17:58:14.882Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite"
}
```

---


### Runtime record

_source line 6181 · 2026-05-15T17:58:14.634Z_

```json
{
  "parentUuid": "e5903e0d-1780-427a-ba67-6df19ea95363",
  "isSidechain": false,
  "attachment": {
    "type": "file",
    "filename": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
    "content": {
      "type": "text",
      "file": {
        "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
        "content": "\\section{Discussion}\\label{sec:discussion}\n\n\\paragraph{Practical recommendations.}\nFor quality ranking, VC leads on hard NER ($\\rho{=}0.38$) while EM leads easy NER and binary discrimination (AUROC${=}0.816$, CoNLL); on RE (preliminary), LP outperforms structural signals (Table~\\ref{tab:multiseed}), likely because RE's 40\\% zero-F1 rate favors generation confidence.\nRankings are consistent across two 8B-scale model families; at $N{=}16$, SJ converges to VC (Appendix~\\ref{app:robustness}); at the capability boundary (WNUT-17), all signals collapse (Table~\\ref{tab:wnut}).\n\n\\paragraph{Why the gap exists: two layers.}\n\\textit{Layer 1 (definitional):} Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.\nConsensus-proximity selection (\\S\\ref{sec:evaluation}) does not recover per-sample discrimination (Table~\\ref{tab:selection}).\n\\textit{Layer 2 (score compression):} Log-probability, the only per-sample signal, also fails to exploit the oracle headroom.\nLP scores are severely compressed: the median within-instance LP range is only 0.041 nats, and the CDF rises smoothly with no bimodal split (Figure~\\ref{fig:lp_range_cdf}, Table~\\ref{tab:logprob_ties}).\nIn instances with above-median LP spread ($n{=}210$), LP \\textit{significantly} outperforms greedy ($+2.9$~pp, $p{=}0.004$; $\\varepsilon$ sensitivity in Table~\\ref{tab:epsilon_sweep}), confirming score compression as the primary bottleneck; a free-form ablation (\\S\\ref{sec:ablation}) shows this persists without constrained decoding.\nThe gap holds even among high-diversity instances (Appendix~\\ref{app:diversity}).\nNotably, LP compression's impact on quality estimation is task-dependent: despite identical compression levels, LP provides stronger QE on RE than on NER (Table~\\ref{tab:multiseed}), because RE's binary-outcome regime makes even compressed generation confidence more informative than structural overlap; this does not translate to selection gains on either task.\n\n\\paragraph{The gap widens with $N$.}\nDoubling from $N{=}8$ to $N{=}16$ expands oracle headroom by $+4.4$~pp, yet SJ---the strongest quality estimator at $N{=}16$ ($\\rho{=}0.411$)---selects to $-0.05$~pp below greedy, LP improves by only $+0.4$~pp, and VC deteriorates ($\\Delta$: $-2.2{\\to}{-}3.1$~pp); on RE at $N{=}16$ (preliminary), all consistency signals fall below greedy while LP is the sole positive signal ($\\Delta{=}{+}0.7$~pp, $p{=}0.058$; Table~\\ref{tab:re_n16_selection}).\nThe gap is not a small-$N$ artifact; detailed $N$-scaling analysis in Appendix~\\ref{app:n_scaling}.\n\n\\paragraph{Ablation: free-form decoding.}\\label{sec:ablation}\nRemoving grammar constraints entirely (SciERC, Qwen3-8B) yields nearly identical LP distributions (within-instance std ratio $0.97{\\times}$, tied fraction $-2$~pp) and negligible selection changes, ruling out constrained decoding as the cause (Appendix~\\ref{app:freeform_ablation}).\nOur consensus-proximity strategies instantiate MBR decoding \\cite{eikema2022sampling}; all fail because utility correlates with F1 across instances but not within them (Appendix~\\ref{app:mbr_discussion}).\n\n\\paragraph{Methodological implications.}\nThe decoupling of $\\rho$, AUROC, and selection F1 means single-metric evaluation risks selecting the wrong signal.\nEffective selection likely requires per-sample signals such as trained verifiers \\cite{cobbe2021verifiers, venktesh2025trust}; $N{=}8$ captures most quality estimation benefit (Appendix~\\ref{app:n_scaling}).\nStructural signals are robust to domain shift when the training schema subsumes the target (VC $\\rho{=}0.469$ OOD vs.\\ $0.379$ in-domain; Appendix~\\ref{app:ood}).\n",
        "numLines": 28,
        "startLine": 1,
        "totalLines": 28
      }
    },
    "displayPath": "../../../docs/paper/sections/discussion.tex"
  },
  "type": "attachment",
  "uuid": "cbd9b6f6-3b25-4ca0-b931-5994b6c8ddfd",
  "timestamp": "2026-05-15T17:58:14.634Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite"
}
```

---


### Runtime record

_source line 6182 · 2026-05-15T17:58:14.635Z_

```json
{
  "parentUuid": "cbd9b6f6-3b25-4ca0-b931-5994b6c8ddfd",
  "isSidechain": false,
  "attachment": {
    "type": "file",
    "filename": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex",
    "content": {
      "type": "text",
      "file": {
        "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex",
        "content": "\\section{Introduction}\\label{sec:introduction}\n\nSelf-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.\nOn discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K (PaLM-540B; \\citealp{wang2023selfconsistency}).\nMore broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \\cite{snell2025scaling, brown2024monkeys}.\nThese results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.\nFor tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.\nBut information extraction (IE) poses a structurally different challenge.\nThe output is not a single token or number; it is a \\textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.\nThere is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.\nCan self-consistency still provide useful signal in this structured setting?\n\nPrior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \\textit{quality estimation} (which inputs does the model handle reliably?) and \\textit{sample selection} (which of $N$ outputs is best?).\nThese require different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.\nSelf-consistency methods for discrete answers \\cite{wang2023selfconsistency, chen2024usc} and weighted variants \\cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.\nThe most relevant study, \\citet{yao2026consistency}, examines consistency--accuracy correlations for LLM-based IE, finding results that our quality-estimation analysis corroborates.\nOur work complements theirs in three directions: (i)~structural matching beyond surface-level agreement, (ii)~testing whether quality estimation translates to best-of-$N$ selection (it does not), and (iii)~a difficulty gradient revealing non-obvious findings invisible on a single dataset.\n\nAll experiments use constrained decoding \\cite{willard2023guided}, the standard for schema-compliant IE output.\\footnote{Our free-form ablation (\\S\\ref{sec:ablation}) confirms fine-tuned models produce 99.95\\% valid JSON without grammar constraints.}\n\nOur central finding is the \\textbf{correlation-selection gap} (Figure~\\ref{fig:overview}): consistency signals achieve strong quality estimation ($\\rho$ up to 0.45) but fail at sample selection despite substantial oracle headroom.\nFour of five signals are instance-level by construction; log-probability, the only per-sample signal, is too compressed to discriminate (\\S\\ref{sec:discussion}), though where compression is mitigated, selection recovers gains (\\S\\ref{sec:ablation}).\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_overview}\n\\caption{The correlation-selection gap. \\textbf{Left}: high inter-sample agreement correlates with high F1 (quality estimation). \\textbf{Right}: instance-level signals assign identical scores to all candidates, precluding sample selection.}\n\\label{fig:overview}\n\\end{figure*}\n\nWe systematically compare five confidence signals from three families---structural (entity voting confidence [VC], Soft Jaccard [SJ]), surface (exact match [EM], Fleiss' $\\kappa$ [FK]), and model-internal (log-probability [LP])---across NER and RE on SciERC \\cite{luan2018scierc}, CoNLL-2003 \\cite{tjongkimsang2003conll}, and WNUT-17 \\cite{derczynski2017wnut}, using Qwen3-8B and LLaMA-3.1-8B.\nOur contributions are:\n\\begin{enumerate}\n    \\item \\textbf{Metric dissociation.}\n    We find that quality estimation, binary discrimination, and sample selection decouple, so single-metric evaluation risks selecting the wrong signal.\n\n    \\item \\textbf{The correlation-selection gap.}\n    Despite strong quality estimation, no signal significantly improves sample selection: LP scores are too compressed within instances, and MBR-style selection correlates with F1 across but not within instances.\n\n    \\item \\textbf{Difficulty- and task-dependent signal rankings.}\n    Signal rankings shift with task complexity and type, and collapse at the capability boundary. RE conclusions rest on SciERC alone (preliminary).\n\\end{enumerate}\n\n",
        "numLines": 44,
        "startLine": 1,
        "totalLines": 44
      }
    },
    "displayPath": "../../../docs/paper/sections/introduction.tex"
  },
  "type": "attachment",
  "uuid": "c8f0aa14-dcf0-486a-9acb-05c1ac55b0fb",
  "timestamp": "2026-05-15T17:58:14.635Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite"
}
```

---


### Runtime record

_source line 6183 · 2026-05-15T17:58:14.631Z_

```json
{
  "parentUuid": "c8f0aa14-dcf0-486a-9acb-05c1ac55b0fb",
  "isSidechain": false,
  "attachment": {
    "type": "file",
    "filename": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex",
    "content": {
      "type": "text",
      "file": {
        "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex",
        "content": "Our evaluation covers three datasets but only one RE benchmark (SciERC), where 40\\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.\nRE selection failure persists even when restricting to non-zero F1 instances (Appendix~\\ref{app:re_conditional_selection}), ruling out floor effects as the sole explanation, but generalization to other RE benchmarks remains unvalidated.\nWNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.\n\nWe evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.\nA 3-seed robustness analysis confirms that signal rankings are stable across seeds ($\\sigma{\\leq}0.026$; Table~\\ref{tab:multiseed}), but whether our findings---particularly the correlation-selection gap and the difficulty-dependent signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.\nLarger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.\n\nOur analysis of selection potential uses only unsupervised signals.\nWe do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.\n\nWe evaluate at $N{=}8$ (primary) and $N{=}16$; $N{=}8$ was chosen to balance signal quality against compute cost, as $N$-scaling analysis shows sublinear gains beyond this point (Appendix~\\ref{app:n_scaling}).\nThe behavior at larger sample sizes (e.g., $N{=}64$) is unknown, and $N$-scaling gains are setting-dependent.\n\nOn CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\\rho{=}0.431$ vs.\\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.\nOur free-form ablation (\\S\\ref{sec:ablation}) confirms that LP score compression persists without constrained decoding, but was conducted on a single dataset (SciERC) with one model (Qwen3-8B); whether the compression finding generalizes to other datasets, model families, or model scales remains untested.\n\nQwen3-8B's SciERC checkpoint was trained with \\texttt{enable\\_thinking} active, injecting empty \\texttt{&lt;think>&lt;/think>} blocks (4--5 tokens, no reasoning content) before each response; CoNLL and WNUT checkpoints disabled this feature.\nA three-part analysis (Appendix~\\ref{app:thinking_token}) rules out this confound: the LP shift is only 0.001 nats (2.68\\% of median LP range), the shift is near-constant across candidates within each instance (preserving rankings), and CoNLL---trained \\textit{without} thinking tokens---exhibits \\textit{higher} tied fractions (95.8\\%) than SciERC (60.3\\%), directly contradicting the hypothesis that thinking tokens cause LP compression.\n\nOne of three seeds (seed${=}456$) was run with \\texttt{--subtask joint} (joint NER+RE decoding) rather than \\texttt{--subtask ner} used by the other two seeds; the resulting NER F1 difference is ${<}0.3$~pp and falls within normal seed variance, so we retain this seed in 3-seed analyses without correction.\nLP compression is also unaffected: seed${=}456$ yields median LP range${=}0.040$ nats and tied fraction${=}62.2\\%$, consistent with seed${=}42$ ($0.041$ nats, $60.3\\%$; Appendix~\\ref{app:logprob_ties}).\n\nLog-probability temperature comparison is limited to SciERC NER ($\\rho{=}0.249$ at $T{=}0.7$ vs.\\ $0.205$ at $T{=}1.0$); RE $T{=}0.7$ LP data is unavailable.\nLP shows the largest temperature sensitivity among all signals ($\\Delta\\rho{=}{+}0.044$ on NER), with lower temperature improving quality estimation, but whether this translates to selection gains remains untested.\nOn CoNLL at $T{=}0.7$, LP tied fractions reach 95.8\\%, suggesting that compression worsens on easy datasets at lower temperature.\n",
        "numLines": 27,
        "startLine": 1,
        "totalLines": 27
      }
    },
    "displayPath": "../../../docs/paper/sections/limitations.tex"
  },
  "type": "attachment",
  "uuid": "e315745a-d09e-4261-9d08-e0ba302aeac3",
  "timestamp": "2026-05-15T17:58:14.631Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite"
}
```

---


### Runtime record

_source line 6184 · 2026-05-15T17:58:14.884Z_

```json
{
  "parentUuid": "e315745a-d09e-4261-9d08-e0ba302aeac3",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__bootstrap_provenance",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__list_artifacts",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__overleaf_init",
      "mcp__agent-ml-research__overleaf_pull",
      "mcp__agent-ml-research__overleaf_push",
      "mcp__agent-ml-research__overleaf_status",
      "mcp__agent-ml-research__overleaf_sync",
      "mcp__agent-ml-research__paper_agent_post_to_director",
      "mcp__agent-ml-research__paper_agent_request_review",
      "mcp__agent-ml-research__paper_compile_and_check",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__send_progress",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__verify_references",
      "mcp__agent-ml-research__write_paper_section"
    ],
    "addedLines": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__bootstrap_provenance",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__list_artifacts",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__overleaf_init",
      "mcp__agent-ml-research__overleaf_pull",
      "mcp__agent-ml-research__overleaf_push",
      "mcp__agent-ml-research__overleaf_status",
      "mcp__agent-ml-research__overleaf_sync",
      "mcp__agent-ml-research__paper_agent_post_to_director",
      "mcp__agent-ml-research__paper_agent_request_review",
      "mcp__agent-ml-research__paper_compile_and_check",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__send_progress",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__verify_references",
      "mcp__agent-ml-research__write_paper_section"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "46e5d77d-fd62-4fe0-a1a6-81373f74d3e9",
  "timestamp": "2026-05-15T17:58:14.884Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite"
}
```

---


### Runtime record

_source line 6185 · 2026-05-15T17:58:14.884Z_

```json
{
  "parentUuid": "46e5d77d-fd62-4fe0-a1a6-81373f74d3e9",
  "isSidechain": false,
  "attachment": {
    "type": "mcp_instructions_delta",
    "addedNames": [
      "agent-ml-research"
    ],
    "addedBlocks": [
      "## agent-ml-research\nML research experiment management tools"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "15d0afc4-e043-4935-9927-e06e79724d54",
  "timestamp": "2026-05-15T17:58:14.884Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite"
}
```

---


### Runtime record

_source line 6186_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] [Patch] Round 8 高优先写作修复——不依赖正在跑的实验，立即处理。  按优先级排序：  ## 1. R8-N1 页数压缩至 ≤8 页（CRITICAL，desk-rejection 风险） 当前估计 10-11 页正文。压缩策略： - Discussion free-form ablation 详述移至 Appendix（~0.5 页） - Robustn…",
  "leafUuid": "947c9223-32fc-4304-88a3-ab29e6a03a79",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6"
}
```

---


### Runtime record

_source line 6187_

```json
{
  "type": "ai-title",
  "aiTitle": "Set up agent communication with Director",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6"
}
```

---


### Assistant

_source line 6188 · 2026-05-15T17:58:19.107Z_

<details><summary>Logged reasoning block</summary>

```text
Let me check the current state of the paper by compiling it and checking the page count. The critical pending task is verifying if the main body is ≤8 pages after all the compressions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15d0afc4-e043-4935-9927-e06e79724d54",
  "isSidechain": false,
  "requestId": "req_011Cb4nforcEsEp6fe93sBDu",
  "type": "assistant",
  "uuid": "dd5b88af-ce18-4e72-93c2-6dc02f1edcf5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WTNPrmECoy4DqqQbcwbFWM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30850,
      "cache_read_input_tokens": 11701,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 30850,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 160,
          "cache_read_input_tokens": 11701,
          "cache_creation_input_tokens": 30850,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 30850
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


### Assistant

_source line 6189 · 2026-05-15T17:58:19.645Z_

Let me verify the actual main body page count after all compressions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd5b88af-ce18-4e72-93c2-6dc02f1edcf5",
  "isSidechain": false,
  "requestId": "req_011Cb4nforcEsEp6fe93sBDu",
  "type": "assistant",
  "uuid": "4c18a459-b86c-4035-a8e5-2cc179568c49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WTNPrmECoy4DqqQbcwbFWM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30850,
      "cache_read_input_tokens": 11701,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 30850,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 160,
          "cache_read_input_tokens": 11701,
          "cache_creation_input_tokens": 30850,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 30850
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


### Tool call

_source line 6190 · 2026-05-15T17:58:19.999Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01W93ZxjJpJvLxP9gC9ThPPn`</summary>

```json
{
  "query": "select:paper_compile_and_check,pdf_to_images",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c18a459-b86c-4035-a8e5-2cc179568c49",
  "isSidechain": false,
  "requestId": "req_011Cb4nforcEsEp6fe93sBDu",
  "type": "assistant",
  "uuid": "395ad5fc-e6f8-415b-be54-af6551c04bf2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WTNPrmECoy4DqqQbcwbFWM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30850,
      "cache_read_input_tokens": 11701,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 30850,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 160,
          "cache_read_input_tokens": 11701,
          "cache_creation_input_tokens": 30850,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 30850
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

_source line 6191 · 2026-05-15T17:58:20.005Z_

<details><summary>↩ Tool result · `toolu_01W93ZxjJpJvLxP9gC9ThPPn`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "395ad5fc-e6f8-415b-be54-af6551c04bf2",
  "isSidechain": false,
  "promptId": "4ab6fc0d-e7b3-4753-81c9-824338d4b6fc",
  "type": "user",
  "uuid": "5740cf44-76f4-4ce1-aa50-cb47bcdde810",
  "toolUseResult": {
    "matches": [],
    "query": "select:paper_compile_and_check,pdf_to_images",
    "total_deferred_tools": 50
  },
  "sourceToolAssistantUUID": "395ad5fc-e6f8-415b-be54-af6551c04bf2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite"
}
```

</details>

---


### Tool call

_source line 6192 · 2026-05-15T17:58:23.138Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_012GP7L7UXfhLb4srH72kLxh`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__paper_compile_and_check,mcp__agent-ml-research__pdf_to_images",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5740cf44-76f4-4ce1-aa50-cb47bcdde810",
  "isSidechain": false,
  "requestId": "req_011Cb4ngBCzUoPLTw8Lzh786",
  "type": "assistant",
  "uuid": "2932005e-05ef-45a5-ac1e-8d53ef9127de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ZaPpYUbdCiYK4ckyiEaC2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 179,
      "cache_read_input_tokens": 42551,
      "output_tokens": 104,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 179,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 104,
          "cache_read_input_tokens": 42551,
          "cache_creation_input_tokens": 179,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 179
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

_source line 6193 · 2026-05-15T17:58:23.141Z_

<details><summary>↩ Tool result · `toolu_012GP7L7UXfhLb4srH72kLxh`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__paper_compile_and_check"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__pdf_to_images"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2932005e-05ef-45a5-ac1e-8d53ef9127de",
  "isSidechain": false,
  "promptId": "4ab6fc0d-e7b3-4753-81c9-824338d4b6fc",
  "type": "user",
  "uuid": "9a9709b2-b9eb-4b38-9f53-0a2d0523fa0e",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__paper_compile_and_check",
      "mcp__agent-ml-research__pdf_to_images"
    ],
    "query": "select:mcp__agent-ml-research__paper_compile_and_check,mcp__agent-ml-research__pdf_to_images",
    "total_deferred_tools": 50
  },
  "sourceToolAssistantUUID": "2932005e-05ef-45a5-ac1e-8d53ef9127de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite"
}
```

</details>

---


### Tool call

_source line 6194 · 2026-05-15T17:58:25.887Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__paper_compile_and_check · `toolu_01H1RQtUDyxfUEQSdgPcGgH7`</summary>

```json
{
  "project": "struct_self_consist_ie",
  "max_pages": 8
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a9709b2-b9eb-4b38-9f53-0a2d0523fa0e",
  "isSidechain": false,
  "requestId": "req_011Cb4ngQYvUwu2CTn5AAvNu",
  "type": "assistant",
  "uuid": "58b84212-b649-4ec9-98e1-c701f3a98991",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0131jaTJK5UTj9vYz4BR2bws",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1194,
      "cache_read_input_tokens": 42730,
      "output_tokens": 92,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1194,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 92,
          "cache_read_input_tokens": 42730,
          "cache_creation_input_tokens": 1194,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1194
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

_source line 6195 · 2026-05-15T17:58:26.039Z_

<details><summary>↩ Tool result · `toolu_01H1RQtUDyxfUEQSdgPcGgH7`</summary>

```text
{"result":"{\"success\": true, \"passed\": false, \"compiled\": {\"success\": true, \"pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf\", \"paper_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper\", \"main_tex\": \"main.tex\", \"log_tail\": \"\\nOverfull \\\\hbox (47.2356pt too wide) in paragraph at lines 745--756\\n [][] \\n []\\n\\n\\nUnderfull \\\\hbox (badness 1655) in paragraph at lines 790--790\\n[]\\\\T1/ptm/m/n/10 (+20) Table 22: |Cross-dataset OOD qual-ity es-ti-ma-tion\\n []\\n\\n\\nUnderfull \\\\hbox (badness 1769) in paragraph at lines 790--790\\n\\\\T1/ptm/m/n/10 (+20) in-stances ($\\\\OML/cmm/m/it/10 n[]\\\\OT1/cmr/m/n/10 2756$\\\\T1/\\nptm/m/n/10 (+20) ). CoNLL$\\\\OMS/cmsy/m/n/10 !$\\\\T1/ptm/m/n/10 (+20) SciERC: CoNLL\\n-\\n []\\n\\n\\nOverfull \\\\hbox (46.87402pt too wide) in paragraph at lines 792--805\\n [][] \\n []\\n\\n[22])\\nUnderfull \\\\hbox (badness 5133) in paragraph at lines 818--50\\n []\\\\T1/ptm/b/n/10.95 (+20) Asymmetry in-ter-pre-ta-tion.[] \\\\T1/ptm/m/n/10.95 (+\\n20) The di-rec-tional\\n []\\n\\n\\nUnderfull \\\\hbox (badness 7081) in paragraph at lines 818--50\\n\\\\T1/ptm/m/n/10.95 (+20) asym-me-try is driven by schema cov-er-age:\\n []\\n\\n[23\\n\\n] (./main.aux)\\n ***********\\nLaTeX2e <2025-11-01>\\nL3 programming layer <2026-01-19>\\n ***********\\nPackage rerunfilecheck Info: File `main.out' has not changed.\\n(rerunfilecheck)             Checksum: 12754B12DD2F90E2AB798D6280AE20BA;4768.\\n ) \\nHere is how much of TeX's memory you used:\\n 16909 strings out of 469438\\n 267249 string characters out of 5468411\\n 748286 words of memory out of 5000000\\n 44542 multiletter control sequences out of 15000+600000\\n 722220 words of font info for 470 fonts, out of 8000000 for 9000\\n 59 hyphenation exceptions out of 8191\\n 84i,12n,93p,1001b,698s stack positions out of 10000i,1000n,20000p,200000b,200000s\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/inconsolata/Inconsolata-zi4\\nr.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx9.pfb><\\n/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/s\\nhare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/t\\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive\\n/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-\\ndist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fo\\nnts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\\ne1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\\nic/amsfonts/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf\\nonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/\\ncmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb\\n>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr\\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/\\ntexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive\\n/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-\\ndist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fo\\nnts/type1/public/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fon\\nts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-dist/font\\ns/type1/urw/helvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/\\ntimes/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pf\\nb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\\nOutput written on main.pdf (23 pages, 659460 bytes).\\nPDF statistics:\\n 1601 PDF objects out of 1728 (max. 8388607)\\n 1064 compressed objects within 11 object streams\\n 221 named destinations out of 1000 (max. 500000)\\n 85268 words of extra memory for PDF output out of 89155 (max. 10000000)\\n\", \"error\": \"\", \"pages\": 23, \"warnings\": [\"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\"]}, \"pages\": 23, \"page_status\": \"over_limit\", \"max_pages\": 8, \"min_pages\": null, \"critical_warnings\": [], \"minor_warnings\": [\"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"Underfull \\\\hbox (badness 3333) in paragraph at lines 19--20\", \"Underfull \\\\hbox (badness 1152) in paragraph at lines 37--39\", \"Underfull \\\\hbox (badness 2556) in paragraph at lines 13--19\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 1226) in paragraph at lines 71--74\", \"Underfull \\\\hbox (badness 3668) in paragraph at lines 14--20\", \"Underfull \\\\hbox (badness 1377) in paragraph at lines 14--20\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 111--114\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 111--114\", \"Underfull \\\\hbox (badness 5036) in paragraph at lines 119--1\", \"Underfull \\\\hbox (badness 1616) in paragraph at lines 119--1\", \"Underfull \\\\hbox (badness 1242) in paragraph at lines 8--15\", \"Underfull \\\\hbox (badness 1365) in paragraph at lines 147--152\", \"Underfull \\\\hbox (badness 1158) in paragraph at lines 183--191\", \"Underfull \\\\hbox (badness 1043) in paragraph at lines 205--211\", \"Underfull \\\\hbox (badness 1742) in paragraph at lines 205--211\", \"Underfull \\\\hbox (badness 1184) in paragraph at lines 214--219\", \"Underfull \\\\hbox (badness 1990) in paragraph at lines 229--233\", \"Underfull \\\\hbox (badness 1824) in paragraph at lines 303--307\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 311--319\", \"Underfull \\\\hbox (badness 1082) in paragraph at lines 311--319\", \"Underfull \\\\hbox (badness 4454) in paragraph at lines 311--319\", \"Underfull \\\\hbox (badness 1681) in paragraph at lines 382--388\", \"Underfull \\\\hbox (badness 8056) in paragraph at lines 90--93\", \"Underfull \\\\hbox (badness 5802) in paragraph at lines 90--93\", \"Underfull \\\\hbox (badness 1253) in paragraph at lines 90--93\", \"Underfull \\\\hbox (badness 1715) in paragraph at lines 90--93\", \"Underfull \\\\hbox (badness 2635) in paragraph at lines 90--93\", \"Underfull \\\\vbox (badness 6910) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 1990) in paragraph at lines 109--113\", \"Underfull \\\\hbox (badness 2753) in paragraph at lines 134--140\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 134--140\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 134--140\", \"Underfull \\\\hbox (badness 1082) in paragraph at lines 134--140\", \"Underfull \\\\hbox (badness 1072) in paragraph at lines 134--140\", \"Underfull \\\\hbox (badness 6691) in paragraph at lines 134--140\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 134--140\", \"Underfull \\\\hbox (badness 1019) in paragraph at lines 142--145\", \"Overfull \\\\hbox (0.91821pt too wide) in paragraph at lines 147--153\", \"Underfull \\\\hbox (badness 1033) in paragraph at lines 155--159\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Overfull \\\\hbox (19.10843pt too wide) in paragraph at lines 165--176\", \"Underfull \\\\hbox (badness 4060) in paragraph at lines 254--257\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Overfull \\\\hbox (18.97287pt too wide) in paragraph at lines 316--329\", \"Underfull \\\\hbox (badness 1210) in paragraph at lines 333--337\", \"Overfull \\\\hbox (75.87871pt too wide) in paragraph at lines 343--359\", \"Overfull \\\\hbox (0.76773pt too wide) in paragraph at lines 370--395\", \"Underfull \\\\hbox (badness 2460) in paragraph at lines 410--410\", \"Underfull \\\\hbox (badness 3514) in paragraph at lines 410--410\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 464--467\", \"Underfull \\\\hbox (badness 1810) in paragraph at lines 464--467\", \"Underfull \\\\hbox (badness 1845) in paragraph at lines 464--467\", \"Underfull \\\\hbox (badness 1442) in paragraph at lines 464--467\", \"Underfull \\\\hbox (badness 1845) in paragraph at lines 464--467\", \"Underfull \\\\hbox (badness 2277) in paragraph at lines 464--467\", \"Underfull \\\\hbox (badness 2626) in paragraph at lines 464--467\", \"Underfull \\\\hbox (badness 6268) in paragraph at lines 464--467\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 464--467\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 464--467\", \"Underfull \\\\hbox (badness 1552) in paragraph at lines 464--467\", \"Underfull \\\\hbox (badness 4266) in paragraph at lines 469--472\", \"Underfull \\\\hbox (badness 1418) in paragraph at lines 550--555\", \"Underfull \\\\hbox (badness 2894) in paragraph at lines 582--585\", \"Underfull \\\\hbox (badness 5008) in paragraph at lines 582--585\", \"Underfull \\\\hbox (badness 1859) in paragraph at lines 682--683\", \"Underfull \\\\hbox (badness 1838) in paragraph at lines 685--687\", \"Overfull \\\\hbox (27.00938pt too wide) in paragraph at lines 698--708\", \"Underfull \\\\vbox (badness 2781) has occurred while \\\\output is active []\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Overfull \\\\hbox (50.91055pt too wide) in paragraph at lines 723--738\", \"Overfull \\\\hbox (47.2356pt too wide) in paragraph at lines 745--756\", \"Underfull \\\\hbox (badness 1655) in paragraph at lines 790--790\", \"Underfull \\\\hbox (badness 1769) in paragraph at lines 790--790\", \"Overfull \\\\hbox (46.87402pt too wide) in paragraph at lines 792--805\", \"Underfull \\\\hbox (badness 5133) in paragraph at lines 818--50\", \"Underfull \\\\hbox (badness 7081) in paragraph at lines 818--50\"], \"issues\": [\"pages 23 > limit 8\"], \"summary\": \"FAIL: pages 23 > limit 8\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58b84212-b649-4ec9-98e1-c701f3a98991",
  "isSidechain": false,
  "promptId": "4ab6fc0d-e7b3-4753-81c9-824338d4b6fc",
  "type": "user",
  "uuid": "789f68bc-f140-491e-8f18-7f35ab471be5",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"passed\\\": false, \\\"compiled\\\": {\\\"success\\\": true, \\\"pdf_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf\\\", \\\"paper_dir\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper\\\", \\\"main_tex\\\": \\\"main.tex\\\", \\\"log_tail\\\": \\\"\\\\nOverfull \\\\\\\\hbox (47.2356pt too wide) in paragraph at lines 745--756\\\\n [][] \\\\n []\\\\n\\\\n\\\\nUnderfull \\\\\\\\hbox (badness 1655) in paragraph at lines 790--790\\\\n[]\\\\\\\\T1/ptm/m/n/10 (+20) Table 22: |Cross-dataset OOD qual-ity es-ti-ma-tion\\\\n []\\\\n\\\\n\\\\nUnderfull \\\\\\\\hbox (badness 1769) in paragraph at lines 790--790\\\\n\\\\\\\\T1/ptm/m/n/10 (+20) in-stances ($\\\\\\\\OML/cmm/m/it/10 n[]\\\\\\\\OT1/cmr/m/n/10 2756$\\\\\\\\T1/\\\\nptm/m/n/10 (+20) ). CoNLL$\\\\\\\\OMS/cmsy/m/n/10 !$\\\\\\\\T1/ptm/m/n/10 (+20) SciERC: CoNLL\\\\n-\\\\n []\\\\n\\\\n\\\\nOverfull \\\\\\\\hbox (46.87402pt too wide) in paragraph at lines 792--805\\\\n [][] \\\\n []\\\\n\\\\n[22])\\\\nUnderfull \\\\\\\\hbox (badness 5133) in paragraph at lines 818--50\\\\n []\\\\\\\\T1/ptm/b/n/10.95 (+20) Asymmetry in-ter-pre-ta-tion.[] \\\\\\\\T1/ptm/m/n/10.95 (+\\\\n20) The di-rec-tional\\\\n []\\\\n\\\\n\\\\nUnderfull \\\\\\\\hbox (badness 7081) in paragraph at lines 818--50\\\\n\\\\\\\\T1/ptm/m/n/10.95 (+20) asym-me-try is driven by schema cov-er-age:\\\\n []\\\\n\\\\n[23\\\\n\\\\n] (./main.aux)\\\\n ***********\\\\nLaTeX2e <2025-11-01>\\\\nL3 programming layer <2026-01-19>\\\\n ***********\\\\nPackage rerunfilecheck Info: File `main.out' has not changed.\\\\n(rerunfilecheck)             Checksum: 12754B12DD2F90E2AB798D6280AE20BA;4768.\\\\n ) \\\\nHere is how much of TeX's memory you used:\\\\n 16909 strings out of 469438\\\\n 267249 string characters out of 5468411\\\\n 748286 words of memory out of 5000000\\\\n 44542 multiletter control sequences out of 15000+600000\\\\n 722220 words of font info for 470 fonts, out of 8000000 for 9000\\\\n 59 hyphenation exceptions out of 8191\\\\n 84i,12n,93p,1001b,698s stack positions out of 10000i,1000n,20000p,200000b,200000s\\\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/inconsolata/Inconsolata-zi4\\\\nr.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx9.pfb><\\\\n/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/s\\\\nhare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/t\\\\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive\\\\n/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-\\\\ndist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fo\\\\nnts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\\\\ne1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\\\\nic/amsfonts/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf\\\\nonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/\\\\ncmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb\\\\n>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr\\\\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/\\\\ntexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive\\\\n/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-\\\\ndist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fo\\\\nnts/type1/public/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fon\\\\nts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-dist/font\\\\ns/type1/urw/helvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/\\\\ntimes/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pf\\\\nb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\\\\nOutput written on main.pdf (23 pages, 659460 bytes).\\\\nPDF statistics:\\\\n 1601 PDF objects out of 1728 (max. 8388607)\\\\n 1064 compressed objects within 11 object streams\\\\n 221 named destinations out of 1000 (max. 500000)\\\\n 85268 words of extra memory for PDF output out of 89155 (max. 10000000)\\\\n\\\", \\\"error\\\": \\\"\\\", \\\"pages\\\": 23, \\\"warnings\\\": [\\\"Token not allowed in a PDF string (Unicode):\\\", \\\"Token not allowed in a PDF string (Unicode):\\\", \\\"Token not allowed in a PDF string (Unicode):\\\", \\\"Token not allowed in a PDF string (Unicode):\\\"]}, \\\"pages\\\": 23, \\\"page_status\\\": \\\"over_limit\\\", \\\"max_pages\\\": 8, \\\"min_pages\\\": null, \\\"critical_warnings\\\": [], \\\"minor_warnings\\\": [\\\"Token not allowed in a PDF string (Unicode):\\\", \\\"Token not allowed in a PDF string (Unicode):\\\", \\\"Token not allowed in a PDF string (Unicode):\\\", \\\"Token not allowed in a PDF string (Unicode):\\\", \\\"Underfull \\\\\\\\hbox (badness 3333) in paragraph at lines 19--20\\\", \\\"Underfull \\\\\\\\hbox (badness 1152) in paragraph at lines 37--39\\\", \\\"Underfull \\\\\\\\hbox (badness 2556) in paragraph at lines 13--19\\\", \\\"Underfull \\\\\\\\vbox (badness 10000) has occurred while \\\\\\\\output is active []\\\", \\\"Underfull \\\\\\\\hbox (badness 1226) in paragraph at lines 71--74\\\", \\\"Underfull \\\\\\\\hbox (badness 3668) in paragraph at lines 14--20\\\", \\\"Underfull \\\\\\\\hbox (badness 1377) in paragraph at lines 14--20\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 111--114\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 111--114\\\", \\\"Underfull \\\\\\\\hbox (badness 5036) in paragraph at lines 119--1\\\", \\\"Underfull \\\\\\\\hbox (badness 1616) in paragraph at lines 119--1\\\", \\\"Underfull \\\\\\\\hbox (badness 1242) in paragraph at lines 8--15\\\", \\\"Underfull \\\\\\\\hbox (badness 1365) in paragraph at lines 147--152\\\", \\\"Underfull \\\\\\\\hbox (badness 1158) in paragraph at lines 183--191\\\", \\\"Underfull \\\\\\\\hbox (badness 1043) in paragraph at lines 205--211\\\", \\\"Underfull \\\\\\\\hbox (badness 1742) in paragraph at lines 205--211\\\", \\\"Underfull \\\\\\\\hbox (badness 1184) in paragraph at lines 214--219\\\", \\\"Underfull \\\\\\\\hbox (badness 1990) in paragraph at lines 229--233\\\", \\\"Underfull \\\\\\\\hbox (badness 1824) in paragraph at lines 303--307\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 311--319\\\", \\\"Underfull \\\\\\\\hbox (badness 1082) in paragraph at lines 311--319\\\", \\\"Underfull \\\\\\\\hbox (badness 4454) in paragraph at lines 311--319\\\", \\\"Underfull \\\\\\\\hbox (badness 1681) in paragraph at lines 382--388\\\", \\\"Underfull \\\\\\\\hbox (badness 8056) in paragraph at lines 90--93\\\", \\\"Underfull \\\\\\\\hbox (badness 5802) in paragraph at lines 90--93\\\", \\\"Underfull \\\\\\\\hbox (badness 1253) in paragraph at lines 90--93\\\", \\\"Underfull \\\\\\\\hbox (badness 1715) in paragraph at lines 90--93\\\", \\\"Underfull \\\\\\\\hbox (badness 2635) in paragraph at lines 90--93\\\", \\\"Underfull \\\\\\\\vbox (badness 6910) has occurred while \\\\\\\\output is active []\\\", \\\"Underfull \\\\\\\\hbox (badness 1990) in paragraph at lines 109--113\\\", \\\"Underfull \\\\\\\\hbox (badness 2753) in paragraph at lines 134--140\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 134--140\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 134--140\\\", \\\"Underfull \\\\\\\\hbox (badness 1082) in paragraph at lines 134--140\\\", \\\"Underfull \\\\\\\\hbox (badness 1072) in paragraph at lines 134--140\\\", \\\"Underfull \\\\\\\\hbox (badness 6691) in paragraph at lines 134--140\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 134--140\\\", \\\"Underfull \\\\\\\\hbox (badness 1019) in paragraph at lines 142--145\\\", \\\"Overfull \\\\\\\\hbox (0.91821pt too wide) in paragraph at lines 147--153\\\", \\\"Underfull \\\\\\\\hbox (badness 1033) in paragraph at lines 155--159\\\", \\\"Underfull \\\\\\\\vbox (badness 10000) has occurred while \\\\\\\\output is active []\\\", \\\"Overfull \\\\\\\\hbox (19.10843pt too wide) in paragraph at lines 165--176\\\", \\\"Underfull \\\\\\\\hbox (badness 4060) in paragraph at lines 254--257\\\", \\\"Underfull \\\\\\\\vbox (badness 10000) has occurred while \\\\\\\\output is active []\\\", \\\"Overfull \\\\\\\\hbox (18.97287pt too wide) in paragraph at lines 316--329\\\", \\\"Underfull \\\\\\\\hbox (badness 1210) in paragraph at lines 333--337\\\", \\\"Overfull \\\\\\\\hbox (75.87871pt too wide) in paragraph at lines 343--359\\\", \\\"Overfull \\\\\\\\hbox (0.76773pt too wide) in paragraph at lines 370--395\\\", \\\"Underfull \\\\\\\\hbox (badness 2460) in paragraph at lines 410--410\\\", \\\"Underfull \\\\\\\\hbox (badness 3514) in paragraph at lines 410--410\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 464--467\\\", \\\"Underfull \\\\\\\\hbox (badness 1810) in paragraph at lines 464--467\\\", \\\"Underfull \\\\\\\\hbox (badness 1845) in paragraph at lines 464--467\\\", \\\"Underfull \\\\\\\\hbox (badness 1442) in paragraph at lines 464--467\\\", \\\"Underfull \\\\\\\\hbox (badness 1845) in paragraph at lines 464--467\\\", \\\"Underfull \\\\\\\\hbox (badness 2277) in paragraph at lines 464--467\\\", \\\"Underfull \\\\\\\\hbox (badness 2626) in paragraph at lines 464--467\\\", \\\"Underfull \\\\\\\\hbox (badness 6268) in paragraph at lines 464--467\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 464--467\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 464--467\\\", \\\"Underfull \\\\\\\\hbox (badness 1552) in paragraph at lines 464--467\\\", \\\"Underfull \\\\\\\\hbox (badness 4266) in paragraph at lines 469--472\\\", \\\"Underfull \\\\\\\\hbox (badness 1418) in paragraph at lines 550--555\\\", \\\"Underfull \\\\\\\\hbox (badness 2894) in paragraph at lines 582--585\\\", \\\"Underfull \\\\\\\\hbox (badness 5008) in paragraph at lines 582--585\\\", \\\"Underfull \\\\\\\\hbox (badness 1859) in paragraph at lines 682--683\\\", \\\"Underfull \\\\\\\\hbox (badness 1838) in paragraph at lines 685--687\\\", \\\"Overfull \\\\\\\\hbox (27.00938pt too wide) in paragraph at lines 698--708\\\", \\\"Underfull \\\\\\\\vbox (badness 2781) has occurred while \\\\\\\\output is active []\\\", \\\"Underfull \\\\\\\\vbox (badness 10000) has occurred while \\\\\\\\output is active []\\\", \\\"Overfull \\\\\\\\hbox (50.91055pt too wide) in paragraph at lines 723--738\\\", \\\"Overfull \\\\\\\\hbox (47.2356pt too wide) in paragraph at lines 745--756\\\", \\\"Underfull \\\\\\\\hbox (badness 1655) in paragraph at lines 790--790\\\", \\\"Underfull \\\\\\\\hbox (badness 1769) in paragraph at lines 790--790\\\", \\\"Overfull \\\\\\\\hbox (46.87402pt too wide) in paragraph at lines 792--805\\\", \\\"Underfull \\\\\\\\hbox (badness 5133) in paragraph at lines 818--50\\\", \\\"Underfull \\\\\\\\hbox (badness 7081) in paragraph at lines 818--50\\\"], \\\"issues\\\": [\\\"pages 23 > limit 8\\\"], \\\"summary\\\": \\\"FAIL: pages 23 > limit 8\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"passed\": false, \"compiled\": {\"success\": true, \"pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf\", \"paper_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper\", \"main_tex\": \"main.tex\", \"log_tail\": \"\\nOverfull \\\\hbox (47.2356pt too wide) in paragraph at lines 745--756\\n [][] \\n []\\n\\n\\nUnderfull \\\\hbox (badness 1655) in paragraph at lines 790--790\\n[]\\\\T1/ptm/m/n/10 (+20) Table 22: |Cross-dataset OOD qual-ity es-ti-ma-tion\\n []\\n\\n\\nUnderfull \\\\hbox (badness 1769) in paragraph at lines 790--790\\n\\\\T1/ptm/m/n/10 (+20) in-stances ($\\\\OML/cmm/m/it/10 n[]\\\\OT1/cmr/m/n/10 2756$\\\\T1/\\nptm/m/n/10 (+20) ). CoNLL$\\\\OMS/cmsy/m/n/10 !$\\\\T1/ptm/m/n/10 (+20) SciERC: CoNLL\\n-\\n []\\n\\n\\nOverfull \\\\hbox (46.87402pt too wide) in paragraph at lines 792--805\\n [][] \\n []\\n\\n[22])\\nUnderfull \\\\hbox (badness 5133) in paragraph at lines 818--50\\n []\\\\T1/ptm/b/n/10.95 (+20) Asymmetry in-ter-pre-ta-tion.[] \\\\T1/ptm/m/n/10.95 (+\\n20) The di-rec-tional\\n []\\n\\n\\nUnderfull \\\\hbox (badness 7081) in paragraph at lines 818--50\\n\\\\T1/ptm/m/n/10.95 (+20) asym-me-try is driven by schema cov-er-age:\\n []\\n\\n[23\\n\\n] (./main.aux)\\n ***********\\nLaTeX2e <2025-11-01>\\nL3 programming layer <2026-01-19>\\n ***********\\nPackage rerunfilecheck Info: File `main.out' has not changed.\\n(rerunfilecheck)             Checksum: 12754B12DD2F90E2AB798D6280AE20BA;4768.\\n ) \\nHere is how much of TeX's memory you used:\\n 16909 strings out of 469438\\n 267249 string characters out of 5468411\\n 748286 words of memory out of 5000000\\n 44542 multiletter control sequences out of 15000+600000\\n 722220 words of font info for 470 fonts, out of 8000000 for 9000\\n 59 hyphenation exceptions out of 8191\\n 84i,12n,93p,1001b,698s stack positions out of 10000i,1000n,20000p,200000b,200000s\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/inconsolata/Inconsolata-zi4\\nr.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx9.pfb><\\n/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/s\\nhare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/t\\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive\\n/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-\\ndist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fo\\nnts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\\ne1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\\nic/amsfonts/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf\\nonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/\\ncmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb\\n>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr\\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/\\ntexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive\\n/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-\\ndist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fo\\nnts/type1/public/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fon\\nts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-dist/font\\ns/type1/urw/helvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/\\ntimes/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pf\\nb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\\nOutput written on main.pdf (23 pages, 659460 bytes).\\nPDF statistics:\\n 1601 PDF objects out of 1728 (max. 8388607)\\n 1064 compressed objects within 11 object streams\\n 221 named destinations out of 1000 (max. 500000)\\n 85268 words of extra memory for PDF output out of 89155 (max. 10000000)\\n\", \"error\": \"\", \"pages\": 23, \"warnings\": [\"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\"]}, \"pages\": 23, \"page_status\": \"over_limit\", \"max_pages\": 8, \"min_pages\": null, \"critical_warnings\": [], \"minor_warnings\": [\"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"Underfull \\\\hbox (badness 3333) in paragraph at lines 19--20\", \"Underfull \\\\hbox (badness 1152) in paragraph at lines 37--39\", \"Underfull \\\\hbox (badness 2556) in paragraph at lines 13--19\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 1226) in paragraph at lines 71--74\", \"Underfull \\\\hbox (badness 3668) in paragraph at lines 14--20\", \"Underfull \\\\hbox (badness 1377) in paragraph at lines 14--20\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 111--114\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 111--114\", \"Underfull \\\\hbox (badness 5036) in paragraph at lines 119--1\", \"Underfull \\\\hbox (badness 1616) in paragraph at lines 119--1\", \"Underfull \\\\hbox (badness 1242) in paragraph at lines 8--15\", \"Underfull \\\\hbox (badness 1365) in paragraph at lines 147--152\", \"Underfull \\\\hbox (badness 1158) in paragraph at lines 183--191\", \"Underfull \\\\hbox (badness 1043) in paragraph at lines 205--211\", \"Underfull \\\\hbox (badness 1742) in paragraph at lines 205--211\", \"Underfull \\\\hbox (badness 1184) in paragraph at lines 214--219\", \"Underfull \\\\hbox (badness 1990) in paragraph at lines 229--233\", \"Underfull \\\\hbox (badness 1824) in paragraph at lines 303--307\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 311--319\", \"Underfull \\\\hbox (badness 1082) in paragraph at lines 311--319\", \"Underfull \\\\hbox (badness 4454) in paragraph at lines 311--319\", \"Underfull \\\\hbox (badness 1681) in paragraph at lines 382--388\", \"Underfull \\\\hbox (badness 8056) in paragraph at lines 90--93\", \"Underfull \\\\hbox (badness 5802) in paragraph at lines 90--93\", \"Underfull \\\\hbox (badness 1253) in paragraph at lines 90--93\", \"Underfull \\\\hbox (badness 1715) in paragraph at lines 90--93\", \"Underfull \\\\hbox (badness 2635) in paragraph at lines 90--93\", \"Underfull \\\\vbox (badness 6910) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 1990) in paragraph at lines 109--113\", \"Underfull \\\\hbox (badness 2753) in paragraph at lines 134--140\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 134--140\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 134--140\", \"Underfull \\\\hbox (badness 1082) in paragraph at lines 134--140\", \"Underfull \\\\hbox (badness 1072) in paragraph at lines 134--140\", \"Underfull \\\\hbox (badness 6691) in paragraph at lines 134--140\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 134--140\", \"Underfull \\\\hbox (badness 1019) in paragraph at lines 142--145\", \"Overfull \\\\hbox (0.91821pt too wide) in paragraph at lines 147--153\", \"Underfull \\\\hbox (badness 1033) in paragraph at lines 155--159\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Overfull \\\\hbox (19.10843pt too wide) in paragraph at lines 165--176\", \"Underfull \\\\hbox (badness 4060) in paragraph at lines 254--257\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Overfull \\\\hbox (18.97287pt too wide) in paragraph at lines 316--329\", \"Underfull \\\\hbox (badness 1210) in paragraph at lines 333--337\", \"Overfull \\\\hbox (75.87871pt too wide) in paragraph at lines 343--359\", \"Overfull \\\\hbox (0.76773pt too wide) in paragraph at lines 370--395\", \"Underfull \\\\hbox (badness 2460) in paragraph at lines 410--410\", \"Underfull \\\\hbox (badness 3514) in paragraph at lines 410--410\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 464--467\", \"Underfull \\\\hbox (badness 1810) in paragraph at lines 464--467\", \"Underfull \\\\hbox (badness 1845) in paragraph at lines 464--467\", \"Underfull \\\\hbox (badness 1442) in paragraph at lines 464--467\", \"Underfull \\\\hbox (badness 1845) in paragraph at lines 464--467\", \"Underfull \\\\hbox (badness 2277) in paragraph at lines 464--467\", \"Underfull \\\\hbox (badness 2626) in paragraph at lines 464--467\", \"Underfull \\\\hbox (badness 6268) in paragraph at lines 464--467\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 464--467\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 464--467\", \"Underfull \\\\hbox (badness 1552) in paragraph at lines 464--467\", \"Underfull \\\\hbox (badness 4266) in paragraph at lines 469--472\", \"Underfull \\\\hbox (badness 1418) in paragraph at lines 550--555\", \"Underfull \\\\hbox (badness 2894) in paragraph at lines 582--585\", \"Underfull \\\\hbox (badness 5008) in paragraph at lines 582--585\", \"Underfull \\\\hbox (badness 1859) in paragraph at lines 682--683\", \"Underfull \\\\hbox (badness 1838) in paragraph at lines 685--687\", \"Overfull \\\\hbox (27.00938pt too wide) in paragraph at lines 698--708\", \"Underfull \\\\vbox (badness 2781) has occurred while \\\\output is active []\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Overfull \\\\hbox (50.91055pt too wide) in paragraph at lines 723--738\", \"Overfull \\\\hbox (47.2356pt too wide) in paragraph at lines 745--756\", \"Underfull \\\\hbox (badness 1655) in paragraph at lines 790--790\", \"Underfull \\\\hbox (badness 1769) in paragraph at lines 790--790\", \"Overfull \\\\hbox (46.87402pt too wide) in paragraph at lines 792--805\", \"Underfull \\\\hbox (badness 5133) in paragraph at lines 818--50\", \"Underfull \\\\hbox (badness 7081) in paragraph at lines 818--50\"], \"issues\": [\"pages 23 > limit 8\"], \"summary\": \"FAIL: pages 23 > limit 8\"}"
    }
  },
  "sourceToolAssistantUUID": "58b84212-b649-4ec9-98e1-c701f3a98991",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite"
}
```

</details>

---


### Runtime record

_source line 6196_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] [Patch] Round 8 高优先写作修复——不依赖正在跑的实验，立即处理。  按优先级排序：  ## 1. R8-N1 页数压缩至 ≤8 页（CRITICAL，desk-rejection 风险） 当前估计 10-11 页正文。压缩策略： - Discussion free-form ablation 详述移至 Appendix（~0.5 页） - Robustn…",
  "leafUuid": "789f68bc-f140-491e-8f18-7f35ab471be5",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6"
}
```

---


### Runtime record

_source line 6197_

```json
{
  "type": "ai-title",
  "aiTitle": "Set up agent communication with Director",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6"
}
```

---


### Assistant

_source line 6198 · 2026-05-15T17:58:30.236Z_

<details><summary>Logged reasoning block</summary>

```text
The compile tool reports 23 pages total (including appendix), which always fails against the 8-page limit. I need to visually inspect the PDF to determine where the main body ends and appendix begins. Let me render pages 7-11 to find the boundary.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "789f68bc-f140-491e-8f18-7f35ab471be5",
  "isSidechain": false,
  "requestId": "req_011Cb4ngceCW5v7HTHTxmPL7",
  "type": "assistant",
  "uuid": "b9fcce33-3490-48ef-9cb3-d23879407823",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MsBBim5MevX68U5Tt7FQrt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4313,
      "cache_read_input_tokens": 43924,
      "output_tokens": 248,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4313,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 248,
          "cache_read_input_tokens": 43924,
          "cache_creation_input_tokens": 4313,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4313
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


### Assistant

_source line 6199 · 2026-05-15T17:58:31.673Z_

编译成功，23 页总计（含附录）。需要视觉检查确定正文在第几页结束。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9fcce33-3490-48ef-9cb3-d23879407823",
  "isSidechain": false,
  "requestId": "req_011Cb4ngceCW5v7HTHTxmPL7",
  "type": "assistant",
  "uuid": "099fd6bb-e6af-4b77-b4ad-6c037cdfd6e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MsBBim5MevX68U5Tt7FQrt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4313,
      "cache_read_input_tokens": 43924,
      "output_tokens": 248,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4313,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 248,
          "cache_read_input_tokens": 43924,
          "cache_creation_input_tokens": 4313,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4313
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


### Tool call

_source line 6200 · 2026-05-15T17:58:33.314Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images · `toolu_01BVWh7erNvGSjACPiiaZn1f`</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
  "pages": "7-12",
  "dpi": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "099fd6bb-e6af-4b77-b4ad-6c037cdfd6e4",
  "isSidechain": false,
  "requestId": "req_011Cb4ngceCW5v7HTHTxmPL7",
  "type": "assistant",
  "uuid": "2358000d-f388-4c3a-827e-05c78540a507",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MsBBim5MevX68U5Tt7FQrt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4313,
      "cache_read_input_tokens": 43924,
      "output_tokens": 248,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4313,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 248,
          "cache_read_input_tokens": 43924,
          "cache_creation_input_tokens": 4313,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4313
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

_source line 6201 · 2026-05-15T17:58:35.634Z_

<details><summary>↩ Tool result · `toolu_01BVWh7erNvGSjACPiiaZn1f`</summary>

```text
Error: result (4,409,797 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-paper-agent-4f1165b4/9fa88e93-92fc-446f-90c6-86ed7a5c1cb6/tool-results/mcp-agent-ml-research-pdf_to_images-1778867915623.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-paper-agent-4f1165b4/9fa88e93-92fc-446f-90c6-86ed7a5c1cb6/tool-results/mcp-agent-ml-research-pdf_to_images-1778867915623.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2358000d-f388-4c3a-827e-05c78540a507",
  "isSidechain": false,
  "promptId": "4ab6fc0d-e7b3-4753-81c9-824338d4b6fc",
  "type": "user",
  "uuid": "a3733c91-c759-4340-bcca-dd9bdf6952c8",
  "toolUseResult": "Error: result (4,409,797 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-paper-agent-4f1165b4/9fa88e93-92fc-446f-90c6-86ed7a5c1cb6/tool-results/mcp-agent-ml-research-pdf_to_images-1778867915623.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-paper-agent-4f1165b4/9fa88e93-92fc-446f-90c6-86ed7a5c1cb6/tool-results/mcp-agent-ml-research-pdf_to_images-1778867915623.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
  "mcpMeta": {
    "storage": "sanitized-trace-archive",
    "source_line": 6201,
    "serialized_bytes": 4409834,
    "serialized_sha256": "0607d05ab664779ba5ed70c27f48452b1cefc0475fda9e751120d2a07fc92d2c",
    "note": "Complete sanitized source is retained in trace-files.tar.gz."
  },
  "sourceToolAssistantUUID": "2358000d-f388-4c3a-827e-05c78540a507",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite"
}
```

</details>

---


### Runtime record

_source line 6202_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] [Patch] Round 8 高优先写作修复——不依赖正在跑的实验，立即处理。  按优先级排序：  ## 1. R8-N1 页数压缩至 ≤8 页（CRITICAL，desk-rejection 风险） 当前估计 10-11 页正文。压缩策略： - Discussion free-form ablation 详述移至 Appendix（~0.5 页） - Robustn…",
  "leafUuid": "a3733c91-c759-4340-bcca-dd9bdf6952c8",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6"
}
```

---


### Runtime record

_source line 6203_

```json
{
  "type": "ai-title",
  "aiTitle": "Set up agent communication with Director",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6"
}
```

---


### Assistant

_source line 6204 · 2026-05-15T17:58:38.498Z_

<details><summary>Logged reasoning block</summary>

```text
The image output is too large. Let me try rendering fewer pages - just pages 8-10 to find where main body ends and appendix starts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3733c91-c759-4340-bcca-dd9bdf6952c8",
  "isSidechain": false,
  "requestId": "req_011Cb4nhKqgZdA21n1XZjv2p",
  "type": "assistant",
  "uuid": "fe934555-1d89-41b7-a869-033152626c02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qbe1grFUh4h3RgJeWyEcce",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 656,
      "cache_read_input_tokens": 48237,
      "output_tokens": 198,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 656,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 198,
          "cache_read_input_tokens": 48237,
          "cache_creation_input_tokens": 656,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 656
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


### Assistant

_source line 6205 · 2026-05-15T17:58:39.018Z_

图像太大，缩小范围。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe934555-1d89-41b7-a869-033152626c02",
  "isSidechain": false,
  "requestId": "req_011Cb4nhKqgZdA21n1XZjv2p",
  "type": "assistant",
  "uuid": "f1326e3f-ce24-45f3-baf7-0cfafbcbc7ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qbe1grFUh4h3RgJeWyEcce",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 656,
      "cache_read_input_tokens": 48237,
      "output_tokens": 198,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 656,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 198,
          "cache_read_input_tokens": 48237,
          "cache_creation_input_tokens": 656,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 656
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


### Tool call

_source line 6206 · 2026-05-15T17:58:39.698Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images · `toolu_01TZmstnKJvobNNwrnJBDv2n`</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf",
  "pages": "8-9",
  "dpi": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1326e3f-ce24-45f3-baf7-0cfafbcbc7ad",
  "isSidechain": false,
  "requestId": "req_011Cb4nhKqgZdA21n1XZjv2p",
  "type": "assistant",
  "uuid": "13180785-385a-4a8f-a66b-9cb8192e0281",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/paper_agent_4f1165b4",
  "sessionId": "9fa88e93-92fc-446f-90c6-86ed7a5c1cb6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "stateless-growing-kite",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qbe1grFUh4h3RgJeWyEcce",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 656,
      "cache_read_input_tokens": 48237,
      "output_tokens": 198,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 656,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 198,
          "cache_read_input_tokens": 48237,
          "cache_creation_input_tokens": 656,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 656
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


### Large event (continued)

````text
### Tool result

_source line 6207 · 2026-05-15T17:58:40.505Z_

&lt;details>&lt;summary>↩ Tool result · `toolu_01TZmstnKJvobNNwrnJBDv2n`&lt;/summary>

```text
Error: result (1,533,151 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-paper-agent-4f1165b4/9fa88e93-92fc-446f-90c6-86ed7a5c1cb6/tool-results/mcp-agent-ml-research-pdf_to_images-1778867920500.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-paper-agent-4f1165b4/9fa88e93-92fc-446f-90c6-86ed7a5c1cb6/tool-results/mcp-agent-ml-research-pdf_to_images-1778867920500.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***

```

&lt;/details>

&lt;details>&lt;summary>Recorded metadata&lt;/summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "13180785-385a-4a8f-a66b-9cb8192e0281",
  "isSidechain": false,
  "promptId": "4ab6fc0d-e7b3-4753-81c9-824338d4b6fc",
  "type": "user",
  "uuid": "12308f05-c9cc-40ab-98a5-612e6edb8445",
  "toolUseResult": "Error: result (1,533,151 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-paper-agent-4f1165b4/9fa88e93-92fc-446f-90c6-86ed7a5c1cb6/tool-results/mcp-agent-ml-research-pdf_to_images-1778867920500.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-paper-agent-4f1165b4/9fa88e93-92fc-446f-90c6-86ed7a5c1cb6/tool-results/mcp-agent-ml-research-pdf_to_images-1778867920500.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
  "mcpMeta": {
    "structuredContent": {

````

---

### Large event (continued)

```text
      "result": "{\"success\": true, \"data\": {\"images\": [{\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/_pdf_images/main_p8.png\", \"base64\": \"iVBORw0KGgoAAAANSUhEUgAABNkAAAbaCAIAAAB3QTY3AAAACXBIWXMAABcSAAAXEgFnn9JSAAii3ElEQVR4nOydCdhVUxv3TylKVIgyZEipvFG9RMZ6RaaEiJdQJCQR6TX7lEIIpWSoyJB4Q9GgZIhmoqiUUgmZ4s0QT6bz/a5zf61vtfc5+5znec6zn4b/7+rqes4+++y99lr3utf9X9NOJIUQQgghhBBCiHhJlHYChBBCCCGEEEJscUiLCiGEEEIIIYSIG2lRIYQQQgghhBBxIy0qhBBCCCGEECJupEWFEEIIIYQQQsSNtKgQQgghhBBCiLiRFhVCCCGEEEIIETfSokIIIYQQQggh4kZaVAghhBBCCCFE3EiLCiGEEEIIIYSIG2lRIYQQQgghhBBxIy0qhBBCCCGEECJupEWFEEIIIYQQQsSNtKgQQgghhBBCiLiRFhVCCCGEEEIIETfSokIIIYQQQggh4kZaVAghhBBCCCFE3EiLCiGEEEIIIYSIG2lRIYQQQgghhBBxIy0qhBBCCCGEECJupEWFEEIIIYQQQsSNtKgQQgghhBBCiLiRFhVCCCGEEEIIETfSokIIIYQQQggh4kZaVAghhBBCCCFE3EiLCiGEEEIIIYSIG2lRIYQQQgghhBBxIy0qhBBCCCGEECJupEWFEEIIIYQQQsSNtKgQQgghhBBCiLiRFhVCCCGEEEIIETfSokIIIYQQQggh4kZaVAghhBBCCCFE3EiLCiGEEEIIIYSIG2lRIYQQQgghhBBxIy0qhBBCCCGEECJupEWFEEIIIYQQQsSNtKgQQgghhBBCiLiRFhVCCCGEEEIIETfSokIIIYQQQggh4kZaVAghhBBCCCFE3EiLCiGEEEIIIYSIG2lRIYQQQgghhBBxIy0qhBBCCCGEECJupEWFEEIIIYQQQsSNtKgQQgghhBBCiLiRFhVCCCGEEEIIETfSokIIIYQQQggh4kZaVAghhBBCCCFE3EiLCiGEEEIIIYSIG2lRIYQQQgghhBBxIy0qhBBCCCGEECJupEWFEEIIIYQQQsSNtKgQQgghhBBCiLiRFhVCCCGEEEIIETfSokIIIYQQQggh4kZaVAghhBBCCCFE3EiLCiGEEEIIIYSIG2lRIYQQQgghhBBxIy0qhBBCCCGEECJupEWFEEIIIYQQQsSNtKgQQgghhBBCiLiRFhVCCCGEEEIIETfSokIIIYQQQggh4kZaVAghhBBCCCFE3EiLCiGEEEIIIYSIG2lRIYQQQgghhBBxIy0qhBBCCCGEECJupEWFEEIIIYQQQsSNtKgQQgghhBBCiLiRFhVCCCGEEEIIETfSokIIIYQQQggh4kZaVAghhBBCCCFE3EiLCiGEEEIIIYSIG2lRIYQQQgghhBBxIy0qhBBCCCGEECJupEWFEEIIIYQQQsSNtKgQQgghhBBCiLiRFhVCCCGEEEIIETfSokIIIYQQQggh4kZaVAghhBBCCCFE3EiLCiGEEEIIIYSIG2lRIYQQQgghhBBxIy0qhBBCCCGEECJupEWFEEIIIYQQQsSNtKgQQgghhBBCiLiRFhVCCCGEEEIIETfSokIIIYQQQggh4kZaVAghhBBCCCFE3EiLCiGEEEIIIYSIG2lRIYQQQgghhBBxIy0qhBBCCCGEECJupEWFEEIIIYQQQsSNtKgQQgghhBBCiLiRFhVCCCGEEEIIETfSokIIIYQQQggh4kZaVAghhBBCCCFE3EiLCiGEEEIIIYSIG2lRIYQQQgghhBBxIy0qhBBCCCGEECJupEWFEEIIIYQQQsSNtKgQQgghhBBCiLiRFhVCCCGEEEIIETfSokIIIYQQQggh4kZaVAghhBBCCCFE3EiLCiGEEEIIIYSIG2lRIYQQQgghhBBxIy0qhBBCCCGEECJupEWFEEIIIYQQQsSNtKgQQgghhBBCiLiRFhVCCCGEEEIIETfSokIIIYQQQggh4kZaVAghhBBCCCFE3EiLCiGEEEIIIYSIG2lRIYQQQgghhBBxIy0qhBBCCCGEECJupEWFEEIIIYQQQsSNtKgQQgghhBBCiLiRFhVCCCGEEEIIETfSokIIIYQQQggh4kZaVAghhBBCCCFE3EiLCiGEEEIIIYSIG2lRIYQQQgghhBBxIy0qhBBCCCGEECJupEWFEEIIIYQQQsSNtKgQQgghhBBCiLiRFhVCCCGEEEIIETfSokIIIYQQQggh4kZaVAghhBBCCCFE3EiLCiGEEEIIIYSIG2lRIYQQQgghhBBxIy0qhBBCCCGEECJupEWFEEIIIYQQQsSNtKgQQgghhBBCiLiRFhVCCCGEEEIIETfSokIIIYQQQggh4kZaVAghhBBCCCFE3EiLCiGEEEIIIYSIG2lRIYQQQgghhBBxIy0qhBBCCCGEECJupEWFEEIIIYQQQsSNtKgQQgghhBBCiLiRFhVCCCGEEEIIETfSokIIIYQQQggh4kZaVAghhBBCCCFE3EiLCiGEEEIIIYSIG2lRIYQQQgghhBBxIy0qhBBCCCGEECJupEWFEEIIIYQQQsSNtKgQQgghhBBCiLiRFhVCCCGEEEIIETfSokIIIYQQQggh4kZaVAghhBBCCCFE3EiLiiz8/fff77777oQJE9yRX3/99ZFHHvnkk09KMVVZKcVEzp49e/jw4eRb/LcW//3vf9944428XzaiTL/77rvx48f37dv3vvvumzt3bt5vXVh++OGHZ555hv+LcxHZcDx8/vnnQ4cO9Y9gQkOGDPn9999LK0klytdffz1o0KBvv/225G6xevXqxx9/fFPMQKrbrFmzJk+eXNgfYjN+Ax0mhmzPhdhs+9NPP8301cKFCzdF20imHDs+mcDGHRkzZgxNT3GuWVDwx88/r/P/cSTtralWRbvFL7/88nMOWFtD0bz22msbQzMqYkZaVGQEv3D77bfvuuuuiUTi3HPPdcefeuopjhx77LGlmLaslGIia9Wqxa2nTZsW/623cIjsyfmKFSvmPdrIVKYjR4485ZRTpk6dOm/evPr163MOR/J769x55513Tj311LJly5KMJUuWFOdSsuGSBgd1yCGHkMlbb721f/wf//gHB4kySythJUqXLl14um7dupXExamDLVu2LFOmDLcgui2JW5QcvXv3rlGjBim//PLLc/8VVlS7du1AAx2mRLM9d2KwbZRP165d0TOZTmjUqBGZVnIJKAk++OCDE0880Rz7d999Zwe//fZbPnKwON2OEycuPffcUYnE/+FfmTK31av34K673rv77v2OOmrYFVeMmzfvazuNXMUsi9bJa/URKlSosOOOO+Lu+Hurrbbi72233TaxnmXLlt1www2VK1fm78cee6zITyQ2UaRFRRYGDx4caOqI+E877bRRo0YFzvzzzz/jTVrU3TMlMoZbP/jgg//+979x3zHcupiUbpHlnb///rtjx4633npr3q+ctkwJqqpVq/b999/bxy+++OLAAw984okn8n73aPxC/OuvvyyiLaYW3YRseNNlxYoVYS1KHHbmmWe6iHMzY+rUqaeccsqsWbNK6PpYbLly5TZFLQq9evXKRYsGnPawYcOyatGSzvYcKbJt59hO/fTTTy1atHjvvfcynfD222+TVw0bNixsAkqddevWoeV8LQqYSl76Fw4++BG06LHHDrePP/5YcN9907feuhfqlD/sIC1Lhw4dooffwxQUFJDmLl26uGHViy66iCNHH320faTC3nvvvRz5+OOP+Xj++edLi26ZSIuKLLz22mtZm7rk+p6zeJKUlgsuuKBU7jt//vx77rmnVG5dfEor0zYPGjVqdNJJJ5VuGohEp0yZ4h85/PDDi69FRTyULVs2oEVFMdlll102US36+OOP56JFO3fu/OOPP7qPL730Ui4N9KbLb7/91rFjx6ynoVebN2/ev3//iHPatGljo3Cvv/56/hIYE3vuuWdAi+aLU04ZgRZt3XqEf3DgwFkcLFv2tg8//H+jo0j9vfbaa+HChblf+X//+1/t2rXRse5IQIsaJ5xwwgcffMAfV155pbTolkn+tSgx0JwN+eyzz+yrgoIC7HjatGkET7Nnz/7iiy/ceiT+WL58+cyZM/kKoyz1hQ3CkaMWPfvsswP+JU5s8Db++xIT1KlTpyQG4mKgtDJt8+D7778n9/7973+XYhpwlRUqVHjzzTf9g9KimxDSonln89aiTzzxBOcQ4rsjm70Wbd++/YEHHpj1tD59+tSvXz9iBJVAtGbNmpdccgnZVep9iEWg5LQoKjSsRVet+snm7t5991R38P777yeTieRzvDKpveOOO/wjabXo008/PW/evKS0aJ7A+80JsW7dup9++il83DAtxg/nzp37zjvvzJgxY9GiRX/8kWbxcAmR/0h0+vTpb26IDb7/9ddfSE07wqPaHy5gWrBgQeCrr7/+Ou9p21yhZRo/fvyDDz44adIk8pmPixcv5vhHH300I8XKlSuTqWkeM9bzxRdf+FfARkePHj1o0CCu47dzyQxalPMnTpxof3PHHj16cE6jRo3s4hj0DI/PP//czqSU7Uj0Cod33313yJAhNLFhtzt//nwa41deeYVrOgsZNWpU+fLlSYBd3KXfT6TBBW2SCc508uTJTz75pLsImTN16tRHH32UWwRuSvP2+uuvP/zww88//7zrWLFsP+aYY7gv7pX7ktvuK+p2ePuE5cuXv/DCCzwaDxhe0EgZmahYvXo1N3r22WdJf6Ysonz9HLaDCGP7+OGHH7ozeVJLPM/rb3uQKdMCmGEkU53TWNfQoUP9HHCQZrKau/AI4WTn+GgR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oBZXqVIFGea/DGkzY/z48SeccIK5rFNOOSXwLp9kanE+kmzXXXflBFoTmpJ33323VJIqxGaGtKgQQgghhBBCiLiRFhVCCCGEEEIIETfSokIIIYQQQggh4kZaVAghhBBCCCFE3EiLCiGEEEIIIYSIG2lRIYQQQgghhBBxIy0qhBBCCCGEECJupEWFEEIIIYQQQsSNtKjIJwUFBePGjVuwYEH8t166dOmIESNK7vozZsx4+umnS+76Jc26det4hLFjx3711Vd2ZPbs2bn/3H/8v/766+ds/Pbbb5z5xx9/BI7/8ssvud/0m2++mThx4nPPPTdp0qQvvviiCMmGWbNmvfnmm4X6SdHY2CyE3HvyySdLOxVRFDbH/v7775kzZ7722msll6Q4+fXXX0eNGvX1118X7efkBnXh7bffzm+qfJ599tl33nmn5K5fHDYzY4iZkmsuP/vss8GDB//0008lcfHcWbZsWekmIMzatWtvvfXWG1Pccsst3333XeCE3r1733777X379u3Tpw8nfPnll3m5L+01Tub333+PPm3lypXLly93H7GQHK9Pm/7www9vhBkuNiGkRUV+wBNdfvnlFSpUSCQSRDBx3nr48OGNGjXivvvtt1/J3WW33XbjFnPnzi25W5QcBKz77LNP3bp127dvf8QRR9SqVatt27Ycyf0K/uOjZm+++eZddtklkWLXXXfdfz1cc9ttt+Xgsccey5kff/zxlVdeWbFiRTtz9913r1OnTo0aNRo2bHjWWWeNGTMm0+0WLVrUsmXLsmXL1q9fnzS3adNmjz324OKnn356pUqVTOhmpX///tyR+15zzTW5P2mR2XgsZN68eS1atChTpkzlypVLOy1R5J5jBQUFPXv2rF69OudfcsklMaStRPn+++87dOiwzTbb8DgffPBBEa7wxBNP7LXXXvz8P//5T96TZyxZsoTrV61aFdVXQrcoGpuZMcRMSTeX5557Lhd/4IEHSuLiuYDouu6668aOHVtaCcgEmhDPPGHChK222oosog0NnDB//vxu3brht3v16kWT/ccffxTzjlyBrDjllFOoL1emIA2Z0nbooYcOHDjQHXn55Zd79Ojx559/Zr3LY489xuOceuqpxUyt2JKRFhX55LTTTotfiyZTwXfeG9eAF+7Xr1+7du3WrVuXx1vEw8qVKwkoaZDcE82aNYtAFqWXqWUKE378YcOGmcL88ccf/TM55/rrr2/WrJk7ctVVV3Ea2tWCWv4fP368RdIXXXRR+F40nOXLl0cwf/TRR+4gie/bt+/WW2/Nrwjlc0z2PffcE5sWTWshubTlJQFZxIMXR4uWRMqLWaf69++/OcmPAw44oMhaFAYMGFCiWpTCat++/Z133llC188lARHfbmbGECcl0Vw6Jk6c2Lp168WLF5fExbOC+jr99NPfeOONUrl7LkyePPmWW24pV64cDWLY9S1cuPCCCy7Iy42+++47WmFaQGt2Fy1a1KRJk0wzZXDFmMSDDz7oHyQbO3TokDVIWL58OUL0lVdeyUuyxZaJtKjIJwT9paJFf/755/w2rgSIpdizm1/uuusuMue5557zD86fP79ChQpuvm4RmDRpkmnRcPft77//fvzxx7uPd999d7h0pk2bZj9/6623/OO9e/fm4D777JNWcJoA/vzzz3NMJKYYmxZNC9F8ad162223LY4WzXvKi1+nCHc2J/lx0kknFUeLPvXUUyWqRUuXQYMGzZkzJ+KEzcwY4iTvzeXGw4UXXtijR4/STkUUN910E4Lz3//+N0UQXqEwZMgQxGpebtSqVStkuftofTf33ntv+MylS5faKEJAi8KVV17Zs2fPvKRHiAjyr0WXLFkyZ0M+++wz+6qgoIAIePr06VOmTJk9e3YgDubje++9x1f879aGiU2LzUOL/u9//0MLleKAQH6heSZzwi1Khw4doqO9aF577bVMWjSZWjXk/rbByUDp/PXXXzZ39/bbb3cHP/nkE5u/9Pjjj2e67+GHH557p3vpalGa/6233rpUbp0snhbNe8rzUqc2M/khLZoJwgPM79133404ZzMzhjjZXLXoSy+9tNNOOxVqS4L4OeOMM5Lru2IPOeSQwLcXXXTRr7/+Wvy7vPXWW4F+3rVr17744ovhzPn777+pRDNmzEirRb/55hsakalTpxY/SSI2qOBzQrhBeMrUpBbFumDBAn/FE+dwZFoKxFqOi6HyQv61KFLzzQ35+OOPk6mhEp6cj1QPcsG+couzEZ925O2337Y/VqxYkfe0bZaQdQTc//3vfxctWhSQ92vWrME7Dxo0aOLEiVin/xUOiIJYtWpVMiUAhg0bNmvWLLcuaOnSpU888cS4ceMCK4UoFMo3mZr2+eSTT3JC4LKZtCgXf+yxx15++eUffvgh+nHwlWPGjOHi1Jbw8BdJJQIbMWJEwDwyNa7ffvstOcCt0wZ8OP3XX3/9oYce4o6uASCFzZo142qdO3fGQS9cuNCdT4TkSyzj008/ff7559FO3CI8qYxwyuyf0hkyZEiOc4dI9vjx4x9++GGqA01I4Fue3TYs+frrr8kKij7aZdx22208DsIP/+Ifx9cE9huw3VAeffRRLhseMg08fiYtSgkGhjrTalGey2Rnv3793EHy3BagRkzPw7owg4jnpSgnT578yCOPzJs3L60W5QQST/aSzsAsKXIA50N14Ctctj/9OKvxJzfMopEjR5YrV658+fIzUvibeWQy47R8+OGHWBe3w1uSpGRK59s1nXFSWeyIv+GE06L8iurM7ay++6T1HplSTkGTb4MHD37hhRfCl4ow9ULVqQivlaP8wHiojGQaFZPqGfiWIqbWY37IYzwDRhJ9tZLDaVHqL1lKpqXd9Y3iI4jk28DCWl+LkofYJOUYdhfLly9/5plnqA5Yr5tux1PPWI/bsGTJkiV2xLXLlPjYsWMDrUC+speLT5o0KWxOH330ER7AOqRITKaO6bTGkOmaBtnLM5L+5557DgfrjmPhtE34PbIo7YxxPAaXxWMQugT2gKF0SGQyFf1TIpmEBNlCjXCOJbC1D3Vn6NChlKDVoMD1ubWlYcKECRSla0PJZL7ih3gk/yekkMzBqHgWbscJfo1LZm4uM1laWpzrWLx4cWD/Ldya38s5c+bMGSFwa/5PcIk8Pj4q3MJG3MiHHK5du/Y555yT9lvSQPmSLZhl1kejmpBvFDfZm8v5uUMhnnfeefZ348aNKYXAVnyZ0l9Yjj766K233jqX5Q9kC5E5NTqtFk2mFl4dfvjh0RfBaVPr/SOEAaNHj7ZALlMVDjdkVIRwQ4Y90/xRZSgXYhgSHLBnEYCm/M0QBQUFfIVXDEgtnJ75NJwnOe9rND7ar2Igz1oUL88DYHzfeVg8gbvkKzwCj81pODs+WscnFmYy1Vyq5SN5Ufyl25s9tLhNmjShkaNyEtkcdthh7iu8wG677YY7wNnxFQ2PeXls64YbbrBdQ2jbOnXq9I9//MMW73Xs2JHyOvHEEw888MC9997bb+lpJI444giOXH755b179yZONR2yzz77+M1nWItSpm3btr399tv79+/PjapVqxYxBYUGiXQSChPi3HjjjVzKNfwk+4orrrjyyisJUlu1aoWM8TVM2sYVkYnf53x+WLZs2XPPPdcPFF599VWyy9qbpk2bkjDbMZLY64QTTuBqxxxzzK233jp8+PDVq1f37NmzTp06lmPuCvjfdu3a8XQE6LTftWrVOvjgg52X5Hk5wk8IyMg0cnj77bfPOo5BXejbt+8hhxxCTEBEThpq1KjhVmKQZloFLnLBBRcQYdSsWdOCNtIfId6Q9LanFI0TmZbpTDK/RYsWCFceB0vg5AEDBnA80+Nn0qKc4w91JjNoUeyTg5SjvyjU7ND2PSoaeJJ999134MCB+FOshRIJaFEcy+mnn37//fdjxjvssEOjRo1cLI6NHXXUUTwsASsGj3q3KDCr8YezCIPkCNmO4d2awtW+CDMO06NHjzPPPBNvSctBpEXNTabWgnIRM1E77f3337dJX/5aI9OixHBW+rDNNtsQLrsT0nqPTCknWNlzzz3vvvtugkhStd1227ktTLOaeu51KpPXMnLRoihhqs/NN99MI3LXXXdRiFRSCyhpWW666SZKjYuQY/bHzjvvHHG1EsW0KOqCipxYD7bh11AsmfQ7J8bfzok5LcpPdtllF9umC3t2PpPonF9RBQjgkF7kNmGlfUtp2k0pEdflR/z3z3/+81//+hexI7Ktc+fOO+20U6CCh7MXHxvOXqRIdPaaOeEZMKdrr70Wg3GxLI9cr149fnvxxRdjLVTYtFcIG0Oma/LIuDKcpM2KtGwHU/5kDrejjmN1mDGGTWXnHEJeuyxPSr7hMXBreAyyyDzGmDFjTj311HLlypEGWwcBlFQ4qb5jIQFULtdTQ9Y1a9aMYkW0o1T5iipmX+HBqDW4CMpo4sSJNMrUVm5HCvHVVCJymLLAUe+4447WPffll1+6UqMG4TFsgT1QNC49aZvLCEsLM2rUKBJDzpCHxx9/PE+XTDVetKdHHnkkF6f5tjM5yEN169btnvXQ1HLCVVddZSegmbt06eJcIg943333Rd8oLVg4lyVbAscRxrhQF4FgkAHVFAC5iyeksAhUyH/SQ53CHsiWiF/lCNckLLG/bb3J+eef776lAvrFVGQoX8yG8qXmIi+7d+/O46edA0V4ZiUVoUUpDr4KdGQ7sMw2bdrQsvh61QK55557jkDuuuuu4+dp9z8LN2QkkoDKNWToTwyDSseRWbNmIbBxYuVSbIR7U208YEimp3whZh2R9loByoWP+CX7aJ0FNAROmmI5OBA7M54051mLYjqkPu2oBV6YcMr1djhpmkxZpGlxyyysFlXAERsEEBHg1l2TiTRyVZpQj+YEH2EfqeEWSbsftm7dmiNoD2KLZKqxxHeUKVOmZcuWNlaGLdLochHrI//xxx+vv/76RGorVHwoBf3tt9+ecsopHGnYsKFzNAEtSoHioVzPH4WOE6latWqm0dEzzjjD7xds3ry56z/Go9GMucvWr1/fn4ISblwJcGk/3EfCBU5AaNlHGn6S4bqTTVbRUNlHPDIf3XxCGkvCLB4zEDf/K4X7SJtHcRAHkPl2hAznJyTVGj+OEzKSA+HN3B00gSTM9cVSLqaC3FtJkBZ8RKASG5HthK200BwhkMp0zWRqbadtb2vlhQMKnPDLL78QhyFOXH7SumAP1MFMj++0KM3/UymeeOIJ2jzkcbQW5Zr33nsvQRKibvDgwe40HtYuWOR5dxQr16R1dEdsU0enRVetWkVxOKOyUVO3zRLRGELI/RZrefnll5M5GH+mLCJGDMx0jTbjAKh0vnXulNOuvvpq+9tqtKvvyfXFEdCi5EbHjh2tTerVqxcnUKZu0COT90ibckJhDtrfOAesdP/993ffZjX1XOpUVq+VVYvSlFAB/eno48aN4yd4kmRqHIkGyHRyp06daIAJs7p27ZrpaiWNiSJ8CMKYCvj888/brHWnZ0j8ySef7M5Hm/Et5WgfTYtikxZ/4wpM8Dv3+9JLL/nxJZWOjxy0j2hgu7ufJDLK+oaweZoGm7ngtGg4e4kInR2Gs7dfv36EkmmfPWxOHHHfYgNcpLBzdDNdk5yh4psj5XkJu8kEQl5snsekyp999tn2K+7IOXhCzrH4jOYPpeo8hp9pmKu1dzQcSFl+QuOVNs0Bx4LecKOy5A9XcP1xFDd57moNhsG3VapUQUdZD4XtWYovveOOO+wcIn7rwkimVDdFYFr0vPPOo6bzK5oG641yfZrh5jLa0sL4roPW3HoP8YQ4Rvut06IIWoSo+6FlICraDeD36NHDd4l169blBNcBkfZGaaEiWyeIf5ALNm3a1EUgn332GdmLtokY7UQP07y6xFtmvvHGGxYpFRNbLGp/4wPNzZJpdmTIkCFhnfzhhx8+mxtYAiadXO85Dz30UDJ2/vz5yZTARlG7fHZ07tzZZu1GaNGpU6fylXWDhsEn4H84wdeigUDuyCOPzNSvEW7IaA78hoyKTC3mCKGpTSPCNvh40EEHpb2gSKZshogx7Vt8pk2bxlduqja6jI/Wufbee++5v5PrpWk4Viwh8qxFsXhSj2PlqXhmXKHVjQD4R5ys09z2zDbRxTBF7r/sSITBn1InqfNOCj788MP2B+E+DtdtGm5tD8rT/daaQISNO3LZZZdxxN9mjcCXI67VfPHFFxMbbnyKf7EuKzdCEtCijzzySO3atf/wQN+m7bw0cDo0kG5iJL7VVOuCBQsIUgmp3XUsbR06dPAf0DWuGNgee+xBrObOHzNmDCfsvffeyVST2aBBgy5durj7cuT888+/9dZb7WMgbjbat2/vx80EjonQbGRTLC48Mg3m9/La4FWmV/bRUqIAA6E2ysp/NIuWEELuBDI5seGqy7TgdGjITewhSLp37+7vj0duOCluEP24UZTw4yc9LUp7dnkKTIhGiEdIq0VpdLkFMRl3Jxa55ZZbSJJ/GuLELshX0c+SCWQ5csg/Ys2k06LkP9rMWQXWRWI4wQbfqBREKm6eJC2fe95cjD+cRQFFl9WMA5iWoHzdEVfBP/7440ATjsNMq0X9+duEp5xz5plnJiO9RzjlydQyXUIK95GKTF65j1lNPZc6ldVrZdWiNsc7ML3cBsRcVTUBTAuV6SKxYVrUn8xM2G09TclUEIbOROQ4a0FU8O2+++5rJ5sWdd0TyfXW7mQArhsbcNlruXfXXXfZR5zkXnvthf27kWcaYn/76+T6eQpOi6bN3iZNmnAQf2gfc8xezMkf48Kc8BvuY9G0aPQ1bTfvwN4t1i74MbppIRe3IFO5hSsCIm/zGKZUrUR8FZeWgGMh7LEJF0BhoXacGrEG1Prok+srqa/S0cYcqVOnjjvCbzniP7jtz+yvcEG4cuToo4+2j4HmMqulBXCuwx3xXccTTzzhG+G6deuc0kZjm7RzXasoJevvdrdGuCZSU7Sy3igA0ouTA0Ej51OgfgRiM2MzvdaYcufbcC92xOvHCoUtFnWgw7l4nz597GPaxaJEQbTOl+cAatwGe2xbwZ133nncuHHuOhZI+N6GYM9NUovQotbWWHdeWmgoA1rUAjnXg4NpBTbbD1w8ulPV/CSSwR2pVq0aVXtje9fUxgMO5O233168ePH06dMRk1iFC/Y++eQT02jI0dWrV9uMVCspGwJ07h3HYmOE8eRznrXosmXLbArylClTeAb7O9AFZQOkHJ83b549JO6Dj/68eRPogVBVhLEeoxNOOCE8ku4memFwtpEpztp9G9ai//nPfzjiT+FDm3GEpsU+WmTsD1PApZdemvCW/AW06FlnnYVDPCnEsGHD0j6OpYrGI7CucvDgwbRY4eu4DtdA42oOzqZa+RA0FBQUkFd8O3To0Ey5mjZupp3w42bbECiw2MMcuntvpwXo999/vzvBGrZMu5/btFU3R8ugjlStWpXjNoprWrR169buhEJtz8MtkBkm+fw2Hunu1rGkJfD4ycxzdIcMGZJWixI/oWxNrleuXDm8/xAWazPKijZU9fXXX/NbJJB/MJA5u+yyS7169cKGZFGvWXiVKlWwt8BG9rkYfziLAoouqxkHWLVqVYUKFYh90RuBBWY5atHA3kXWw73nnnvaxwjvEdaiZIi5a4LLZ555xt4u6xaTZDX1XOpUMpvXyqpFqXoVK1YMHCRV/IoKax+tO6w4O0jni/DeRWvXrrWhUYTEwoUL+QP9H7CWVq1aWQ9ReO8iyx/M0h1x+Ul1s54IfxKgzSx1fXC9e/cOvPLBpl67Cp42e63oO3XqZB9zzN605uRSWzQtGn3NtHsZPPTQQxzs3r27O2K3dtWN9qt+/frhOmuRcY4LmF944QVO22GHHR555JHwGzJcCqnChxxyCGc6hRDWouEhzd9++80aTXfE6rU/+wblnEi9KjbtRbJaWhiTu7SngR0HkuvN0mlRH+uf8u2T/Eelh7PXlUjEjQLYnPDA4Efbtm0xg/D1M/WGW1b4Y27muPLywhJ/saiBisO977777lbFzj333OLfBV5//XXSvN122/lNM3cnq51ipIb6riNCi1ofcaCT1wdnFdCiNvOWn2Sa8uPIXYv6ftL8Upw762xC4GHcGlG3KNRNhsJDzpkzx19H6lbz2kfXL2bzVSGexZJ51qLENLQfKG+ygwcwSRmYNUH1sznKboOisBa1zJIWzQo1GRWRSK0Eu+222wItBxmIU+jZs6dVeH/Ttty16GOPPWYf04bj9loqt4t6oL3ff//9EYS5Pw5tZPPmzU3hnH322a5W2AzATO1iMtS42kTWTAtTbYxrxIgRma6WS9xsvbABzWyhg/OShdWitrIiPCposYVNPS2mFk2mRp+sbxhGjhyZTM198qPJtOSuRbl+IKL15+gSeNk2NgRP4b7SBg0aJDbsls4dyoLf+sPdyQ0zh+AsEIuHufbaa+2hCEf8jthcjD+rFs1qxmGIYk2f16hRw38rT9G0qBU0EYmF7BHeI6xFk6lBg169euE6cOwmOVw0kC8tmoz0WtGhP8FWIjXmHzBIK7umTZvax7BYwiHstyFZA9+8EI6xwKZtz5gxw5xYRDCXSYsG8od6gQ4fPHiw1QVfJFAjKGVswARSkyZNAsMyvhbNlL2WTjdmnrvUx1tSyr45uSsXTYtGXzOtFuU0DtarV88dOeyww9A/Ln8S3sqOHNOQFrs7HHzwwYESxyUOGzaMujB69GgbFXRTLXLXopSUOxLWomB9HLaZTdrmMqts8EGz2frksOvIpEUtr2rWrOl3q+ESy5YtG7HZQcSNAuAhOS1gwEQggaH+aAoKCnbaaSeS5AL0G264gToS3gerCPiLRR22WmrUqFFLly51U0KKiVl1WD1WqVKlQoUKVtm7du3qt78RWtSsBS+R6XZhLUoRWysfCOTCFF+Llpb33mghW/Cc2IBVNOIxU1s2x3DRokX8/c477yxevHjevHk2cIgl2K6N4PwG52/CWjSATdnlUcODvKY/cX+4IdtENzxHN7yjmghDc2UhnQUEzhcPGDBg7733tsVm5k1KQovapDI3jTDQ3uO/qlevXqghfuyBuLZSpUoWf1t/hPXoh/cYdAQa16FDh/LRX4voY3sGRExqzSVuxnsmNpzSbJQrVw6Pb38XVouSpIQ3gONo0aIFx61nq7BalAwM7FiYTA062c4ltjYP3x1oD8LkrkXDBNaL4hYsbmjVqlXANmiBEqmRySK4vxEjRvDbwCQoP3NsPPyss86Kvs64ceP23HNPzixfvjztnB3MxfizatGsZpwWzrftQBLeAE7RtCggRP0Jfpm8R1iLImnIFrfasIS0aLTXig793bh6YFtRGw0+9dRT/ZT7Ymn69OmXbEjEdp15JK0WtRiO6M2cmHO/YbJqUUqTHG7evLkFnfZtQCS0a9eOg9g80UmgHye5oRbNlL329ghX73LUomnNqZhaNPqamfZ479WrFwL7uuuu++WXX6ZNm7bLLru4TijzGBGjVYV6r8zYsWOdY3HL+1esWIH6vfbaa00hWCJLQovuvPPOTk6kbS4jLC0thKrOdRx11FHOFaTVoligSUp/MX9yvUuMHnXIdKMAyM6w4fHI3LdQzzV+/PjtttuONhcnQGhat27dTNO4Cou/WNRhzejRRx+d+zb7WTGzadiwYeC47RpF648qpvG9x8M6QXCS/O1aPcMG1V0HTZiwFk1uGMjtuuuu/r64PsXXoqXlvTchZs6caSN/BQUFJi9dfxAGaVN2k6mGkr9d7uFATL7Fk8g8a1Gbke/iS3sY25SIxpU2zG1a4zKFamPC3V5TYdj62o1hGtXGDKGGi2tnzZpl7Zyt27E2sn///vZtyWnRW265hYP2rotkqL3HwybSdbj6Izw+Lgj48ssvTex17tzZpSTcP038ZFsrBRpXi8vDHaIY5Ouvv26xaYMGDQJCCHdp7XcucbOtPgpEbzbu5JbuFFaL2iqdwLrNZGqeEhLXurQLq0Xnz5+fdr8HG6Nr2bJlMjWpY+sUgb3XqaSuASisFuW3bhlkeB9dHJxtixLoCXbbpYRFflZwuIkNV1IlN8wc0snFt99++8B8V8zAao0zPxo5W8npupZzMf6sWjSrGQdYvHix22Ng+PDhtgGJNRVF06Lff/+9U+MR3iOc8lWrVhGfnXbaae5ISWjRrF4ra+hvixVHjRrlH7R5EG66wcY8Rxfq1atn+9xYgfrLZQ1rLpM5aFHzxu6tKmm1qL1XkBiUsgi/fyUwR9ey1+1wZtiomtvnJpfszWROxdGiWa+ZSYvaZgH48yuuuOKBBx6gjrivzGNUqVIl/EY0azpz1KKuiJ1jofVxiaSuBTb/y7sWpe3gyIknnpj2IlktLQCuw23k41yHs4q0WtS8gd/NykVod8wl9u7dO3ALGggcXfSNAvB0iVBPn0Ug4ddjOkeXFlwQjhR7IGGF7TqMINBP6rBdo9FyaWU2CnannXbaMQeqV6/u1mnXrl0bBRi4FG2f7Wtto0Q+9uK3rl278neg85qPichF0WEt6gzeBXKZdiHWHN28Y5NS/bkGOFKKddmyZW4JqFspQAFxxDZJtvmqbp25vf3FhTclTZ61qC1+deOZ2JmbfGtDw/xtbte9AAd3g6N0ujS5fjNeCL8qTfjQ2PgbV9ieexbcd+zY0Y/qbMb/wQcf7E7OlxY9LIX7GGjvLVjfa6+9/Hbx5ZdfzvTKe39/899//x0XbFO/bPpl+fLl/Y3FlyxZ4s4PNK5r1qyx7Rz9nSoI62kM+Aq7wmsHmkBSSKaZcdpuQG4ZlRGIm+fOnVu2bNlq1ar5SszcqOtWLKwWJWHW3Pqvd/vxxx8rVqzollAWVotapOLGChymRZ0uatWqVSI1UOlGxvBll112meskCwst2wshkxYl95yp2LK0gEp0b0EIxBa21IQCyvRSMownbV8d5WubCfmJtI003ILMo446KpHa+clftYXlW0cYlcLf4ZnTKGLrAsjF+MNZZMO/7l5ZzTgA1dM28jVsb33baHHlypWJDTcXefrppxMbviEgrEXHjh3LE5l1RXiPcMrt4n6gT13jiHPRWU09lzqV1WtlDf0HDhyY8IZADcJissKN5m3MWpToH/OwDVpoDc2J+TtCYeRnnnmmdaZk1aKYh69FzVFcf/31gWQ0btwYxRXYUNcIaFHrUDj99NP9c6677rpKlSq5zpRcsjeTObnXIdrCQr97OkzgYbNeM5MW7dSpU1irOGxKAv7W77js0aOHhWg5alEci7+OEcdSrlw5mxHGz2nmXOBotcYNHuZLi9repG6P1sBFslpaAK7sr7A11+F2Vw5rURs5Rxr5mTBgwAAiY1vZuPXWW/sh7yeffGL9mNE3CmDbRLtNoQwcWiK1g4OfG2PGjHGbMhBmBEZlSb/bozgtgZ9QdtiP34WRFtrxTDsyWLWKeF1NEbAH958a35LIPC3IepTSztG1MgpsY+ET1qLt27d3f1sgl2nro3BDZhuw+Q2ZtGihsL1g0WLmVYjobO8eqhtGGJiIu2DBgjdTr+FMpvq++Zt8Nl9nM3jTvvK6JMizFjXByZMT7rgFshbO4u/sI07no48+slepco49tu1BTPbxlQnaXN62vIVju9I5J2ihm21cafuz7b///uQnroTmlhCHk8lV6/SysM/tS5RM7aTKEXulpGFr55ycs3D8gAMOcO0ToosoxF/oa5d1c1poe2ynnL333ptQAFmLiyHoyeRE/vGPf/gyg8bSbTFnvWvE1rRSXIe01atXz+25Yo16zZo13W9tvmuZMmVo+IlQETCc73bDGzJkiAkhEsMtaDjr1q3rugOt5ca3FhQUoJTsHS1EORz0R3RteacbECBiI5F+36dJcX8yMN8mvNGnMAQ3xIXHHXeci/8I3/G8rhU3PeP3I1r8bQPIadljjz0oJr+RXrZsWdWqVSkUd1k8jk3AI5d4LoQiMeXjjz/ufhJ+fJuhmli/paRj+fLlBBC+JrftNyk7f7UPFd9ei0La/H3DsQ1ioERqhvaTTz7ph4DEIjRLfsAUwNQaj4boouww/oMOOiiRGt4kBsU123bw0KRJEwIOso42EluynyM1/dcYEBe6IeVcjD+cRbYTybhx4zAhG6yLNuMAxAe+QuARqMI235Jssf4U5B9NCOrl7LPPTqRW4ZJLlmlVqlShTN2iIP5A17lILsJ7hFNu7+6rUKHC5MmTuT7uxRaacoIJhqymnkudyuq1wno7gL1Eihrkwm6ei4zyYyxbkBlbExsBmpmUvPrqq/aRUsN/Hn/88a4LwL2Gx3di7sV6gwYNSmy4zNvCOLcnme1wi64juB8xYoQNHHH9mTNn+u9Ls9eEhKdokh7r3HEvqaIGHXbYYegoN1y2atWqXXbZxV8Fl0v2+uZEDEAtsAmcZIWZk3WMIpvxBpm2mQkYQ9ZrmhcKvP/TZNLJJ59MVpPD3Gv06NH+S+nshERqfN48RrNmzZyet93UbWPqCHAsftXAsVAKyVS3e9myZU0EEjv169evUaNG1qaYVVi75utM26GNPHdHbLID1cQdMS3qppagKkm8e29NMl1zGW1pAXAd1apVc9125jqcmOzfv3/CmzFEKGx9In4PLEminpqbCrtETMi2w42+UQB+QsUP9HYRdoYjkBYtWrhN10znOBeEvW2zzTaUwg033MCDDB06lCImUvf7LgM/scYOpZ3pTXUGd7fNgcNgBttvv32Rd49PC1ZB1rl+vWRqm6htt90208K3wYMHJ0J9hYZNYs80yTaZEi2JDedzNWjQwO9IIpBz23cHyNSQYX5umpL1ILu2ye3mGJ3hWyzUOJNX1JT58+ebniJQsa3dbIyUE/jKNvQBWw5NhGCqdU4K+yrtm1BKgjxrUdoqwgg37s8D+2tL8IBuWyfA1Jwm4YcEHO4rMqJQO3xsmVg02bRpUzws4oqo2jW02Fbt2rWprsQNF1544c8//2xxD6EqUQLV3ipzw4YNcalkNW2hbbaOy7bXeT3wwAPmI2gIbctZC8dpiYlozzvvvLPOOosWzm3X/uWXX+KztttuO/MjpMTcN+266YFEatOUyy67LNPu3sCV8Wi4rZEjR3L9iy66yEky/DVBlbXcgFpzG7GSMPe2Etu1IplyWIQOtmFDItUHHNgiBR1umQDoLn+HLTLEmnMaSCIeHoF2giYqkZpbRVa7M1HdNEJt2rRB0LZq1Yo7Ou3ED3fbbTdr8vkJx2ngbZpl48aN3SysMESKaJ5DDz20d+/e7du3b9euncsx3Iq9JY9i5Y64CcJ6isxiEf/lHz7omXPPPZe8pdXv1q3bBRdcgIgK70yIk7KRhERqWNK2NbISDDw+FZnrWJyaSA308aR16tTZc889yTE7SEkRB2AeBF72WzMeXxVwgm1+SDFhGH4PBc9lcoikElITPRCgkM/hta8BsG17kyoJIODDmCll4nXXx4F8skE/U63+UB7xE2FT165dEYGEDmSXk9nRxp/JQshDewOEe1NuhBmHIRlIvtNPPx0VivEgA/yeGh7Echtj4O5chwS0bt36qaeeMiNELVPB99prL0yIQJw64g+PR3iPcMqpy9ZxkEgtKyUuwT8kUls1Tpo0KRdTz6VORXgtbHXAgAH2LXEbFS3trOZkanI4xkmtxPBuvvlmLMeF1IT7Nu6USG3PS/hVum8FwJhJHtZI3l511VXEuFR5P+oleVRz58Twq65HiQKyEJ/8xGGSvahNq78Uiu3tjCqz8S7OobyoX+bksSi/rq1duxYzC0xDJSixrcITqXFmd1+yl6T62ete+uVnL3aVabl+MtVlYBMxEqmVchSuDWqRWrMWLmXOGesNy1p+HjaGiGuOGTMGY7PKgkDluJvugcxGFCVC+K9Zwn6sKUyk9sJ18T3+1jIcB4h0Ccy19rniiisoLNomavTVV19NTXTWS9lZRcMTUl44f1ukYLM/rLMmkdpxbcWKFQSXNns5kZqjQTRJs2U9d4nUBEtT0VbRaD3xUfg0/CfJc3aVqbnMZGlhfNcBtC82ko8JYWY2tYeM6tu3L2rBZldx5dbrQVqgD91u3rgX5IdziTht1xeQ6UaZoNTce2scOEYbq0+kIhDyzR/stQ4avwPR2bAPfsy9DyLwE+v1TmSePNyjRw/yEzukLcPY0r6wEavI9Ka3IsONMCrMFSOh2d1///3Tjv8PHz78hBNOwIHbDN6WLVtSiP4JhBzunc9hcOamFROp7QystrpAjpaLtpL2N2J7Kr8hu+222xYuXEi7gM/hyrgpokqOJ1KNL86BimMvsE2kdkWKaD23ZKg4tvjT6Sk3340sxVP5Gs12kHU/NB1rY4pxzh4qkb2LaNu+/fZb3FBYT3KE43zr1kH5kE3kBV/pxUG5QC5Z9x71E/MK7CBHVhPruHzm5I8//jjCI2TFTVNEH+JxAlsjRMPJ8+bNy/S+Y4edgIXwOGknvWBac+fOzTofxsHz0mD7b1rzIU8IetLOBbW3ouXYIcL1I3oNi4YJubzsYOaCOeqdOZqIssOW8O/hFw+UCt988820adMmTJiAPaT1GGmh0HlkMxKy0U3S81m+fDlFH6gOZn78T84H+o+LbPxYV2Cvl2TOZkztxkS5I9ZFCx2uvFyHamU5w2MG5IRhlhxOcLT3SJtyDMPfFuLTTz/NvVCSudWpfHktDJgf+qN/Gy08I+Ub8TLtaCcWDWE3ee4yEINJ66kyCftM5CV7MSf/CiTMN6c1a9YUYale9DXDoEXRbJz27rvvTpw4ETlBaE4MXbduXX8ifTKDx8gRU/5pHUsyNdznz/mkihUzY90cXRw+lpO7M8/R0rBYc6qZXEcRMJcYGOkq7I1sV7zAixuMTBEI3tXvkyWvkI5E4ZTU5MmTR48ejSIaMGAA6t1N0Qr8xC6O4nJvhd14oEUYO3Zsv379sO1C+WoHmbbDDjuEm7BozOAjArkAfkNGq5S2IROFgrpM8GNSK6ynIjQaVYAfUmrxbJ/rKNl9dMXmRNolc0JsCcj4hdjMIOpt1KhReAVpMrUpt5vmvcmRdh/dLYTXXnstYpedrHTu3Dnt6t9Vq1ZFvHDliy++8BcqbzagYY466qhM471C5BFpUZErCsfFFouMX4jNjDFjxlCpBw4cGDi+Zs0aBMmmuzPKlqxFk6lZo+G3m+YC5Z5It/oXScYFMy2BXrFixdlnn7355TZP3a1bN3/PCCFKDmlRkSt4pUQOr2cUYvNDxi/EZsbnn39etWrVMmXKnHHGGQ888MDw4cPvv//+jh07tm3bNmLK9MaPrdh0b0PZAnnttdf8XRhzx7b7atq06Z133vnEE08MGjTo2muvPemkkyIGyX/77beNZElLfqFG5H0JqxCZkBYVOTFw4MD999+/cuXKO++88zXXXBN+ZagQmysyfiE2Sz799NPOnTvXr1+/WrVq6JAOHTpE7Nmz8bNgwYILL7ywcopmzZr17dtXe0AWip9//vn2228/6KCDcPX4/LZt2z766KMxL5wTYgtEWlQIIYQQQgghRNxIiwohhBBCCCGEiBtpUSGEEEIIIYQQcSMtKoQQQgghhBAibqRFhRBCCCGEEELEjbSoEEIIIYQQQoi4kRYVQgghhBBCCBE30qJbLn///feMGTOK/LLEpUuXvvTSS/lNUib++uuvKVOmvPvuu/HcbmOgoKDglVdeWbFiRWknpKT44osvJkyY8NBDD5V2QkqcLedJS47ffvvt52z8+uuvdnKcrqk4/PHHH2+++eb06dNLOyEbOzjDl19+edmyZVnPpKLduJ5Ro0YFvp06deqtt956xx139O3bt1evXk8//XTJpDcKmt2ZM2e+9tpr7sgvv/zy8MMP5/J0pQvRQqnk2KbCZ599Nnjw4J9++qlU7v79998PGzYM6yqVu+fCp59++sILL5R2KsRGirTolghN+2233bbzzjsnEolrrrmmsD+fNm3a4Ycfzm+PPvrokkhegD59+lhS77///hhuV+ogvHv06FGpUiUemVC1tJNTIrz66qunnXYaD3jMMccU81IYcJcuXfKSqpIgj0+aibVr15544omPP/54CV1/Y+Coo45KpNhmm2123HFH/ufv8uXL83eFChXsq/333z9m11RkkNaIpcqVK5PU22+/vbSTs/FCZN+5c2dzhr5+y8RXX3313nvvnX766VtttRW/WrNmjf/tjz/+iFjdfffdDzroIMJixEOJJTwN1uzusssuPMsll1zijj/22GMcOfXUU+NMTBHYbbfdSOfcuXNLOyEbKeeeey7588ADD8R8348//rhVq1Zly5bl7n/88UfMd8+F8ePHN2rUiOThnEs7LWIjRVp0y+Wee+4pmhaFDz74IM6Ar3v37pu9Fv3zzz/9j61bt96MtWgyNUbBA/bp06eY1yGgL1euHHosL6kqCfL1pJmwyrh5N/OIh5NPPnnlypX2kVCeR27Tpo19/Pbbby+44IK99947GbtrKg633HKLtGgutGzZMkctapxxxhldunTJJAzQDEuWLMlrAgsBrVhAiy5fvhwh+sorr5RWknKkX79+7dq1W7duXWknpHQINNDhIxMnTqTVXrx4cYyJ+n8gQbfddtuNVosmU4PqJdFIhQtFbKJIi265vPTSS0XWojSfcQZ81n5v3lq0Y8eO/kdi681bixKC84A0UYX61W+//bZ06VL/yPjx40ePHp3XpOWZoj1pBJ9//rk/4PP3338PHjx48x6vaNiw4erVq93HgBZNpgyjXr16ydhdU3Gg1KRFc+Giiy7KXYv++uuv55133qJFi/hJ7dq1w7MWzznnnBJI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zuOO3V25cmXAA8BPAy66Zs2apUuXHjhwoHXr1uaTxSFOA4RcNESIECFChAgRIkTaI2ShaQKF8+TJkwdKacJ5mjdv3qdPn4CR5PoOs+c+7VMCVFPHhoHq1auHJzucTgi5aIgQIUKECBEiRIgQJy8++uijFi1alCpVqmjRog0aNOjVq1fADcD79+/v27dvoUKFzjnnnIoVKz755JOp/3LBCcGAAQPOO++8Zs2aeZ6sG+LURchFQ4QIESJEiBAhQoQIESJERiPkoiFChAgRIkSIECFChAgRIqMRctEQIUKECBEiRIgQIUKECJHRCLloiBAhQoQIESJEiBAhQoTIaIRcNESIECFChAgRIkSIECFCZDRCLnoK448//vj9eBw5csQz5cGDBx0p//rrrwwubYgQJxD79u2bMGHCn3/+mYZ5rlmzZsyYMUePHvVP9t13302aNMknAcP21VdfXb9+fSrLk1b5hAgRIkSIECFCZAxCLnoK45lnnqlZs6a+tnTWWWfdd999H3/8sWfKUaNG1a1bVylz5MhRsWLFQoUKXXDBBVdfffWAAQN++OGHDC55iBAZhi+//PLaa68944wzEP6ff/45DXOuVKkSec6ZMydegs8++6xevXqkKVasmE8+M2fOJM3FF1+cyvKkVT4hQoQIESJEiBAZg5CLntrYt2+fGGbfvn39U/7+++9KOXDgQN3Zvn17165duZM7d+7Fixenf2FPc4RfXj5pceTIkezZs6c5F3311VdbtmzpztOWhG3btiXkoj/++OONN96Y+k+Qp1U+DpzSgn3yF/7vv//euHHjW2+99cknn/B/wKd++eWXjz76aPbs2fG+Exgk2507d86dO3fhwoW//vprygpPMVL8bLLAhCHhKXv28OHDK1eu9Pzp4MGDQarwxx9/pOzVGYN0apwDBw4cOnTI//G9e/c6wqz++eefb7/9NmWFOVHYv3//lClTcKhOdEFOE3z33Xdjx45Np8y3bt06derUdMo8xAlByEVPeeTIkQNn96WXXkqY8uyzzyblf//7X/vmTTfdxM0SJUpgkNKtjKc/vvnmm/79+5/oUoSIi/POOy/NuagnZsyYYa+U4uYm5KInMxzVObWAG92xY8cTXQo/bNq0qWbNmrfddtvMmTO7du1apkwZ3Cz/R3D0Bw0aRMrnn3/+1VdfrVix4uOPP55stnBIfo0c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TUwIzLBcuXI//vhjvFf++eefCy+8sGzZsjBShYwaNSp//vzxFgqgqboG2sdFt2/fPnDgwFatWuXJk4enOcJF//777yRjzp8//8orr8wSOur76HHHHZdL+NiIESPSxkWF3FN2Bx9eeumlq666Kub80UH2URtt2rRp3769LzCoJWJGO7iBup4wYcJPP/1kBy5atOitt95KOc29e/fS4mnT/OvWrRs+fHh6vhUTB7QbCI3FUP7tt9/mdEZyGFu3bp05cyZ9Ydq0aatXr07np5GcKVOm9O7dm09n+cx4kqDIo0ePfuaZZz7//PMcyUBG8e+//5LVjz76KKcz4pC9cFz0wMbtt98OGfjyyy9NCAM2IS1atIj3ypgxY4jQt29fO/CEE06oUKFC0L9348aN9evXr1u3brx1UXDiiSfmCBeFAnXv3j35+L169YKoZ/KjDCHQbzvk1FNPzSV87M0330wzF809ZXdwiIe77747N+8gyG58+umnzZs3z5cvH1117ty5hPz5559PPPFEuXLlCPnf//6XcsoTJ04khVq1amVdZmPj1VdfPeuss/jWf/7zn+z+Vkwc0G4gDNytW7c+/PDDyfzrr7+e09nJMUDDLrnkkmLFil1++eVdu3a95ZZbSpcuzRCGGKfh6wsXLmzcuPFXX30lm81eP0gbXn755TvvvHPBggVnnnlm0AjMhejRo8fRRx9NVu+///6czotD9iLruSiaesH+WLNmjR7t2bNn6dKlc+bM+fjjj+fPnw/PMW/98ccfCwLYu3dvlmfvYMKvv/5aoECBokWL+jgkxJIxe9OmTTHf0qBO9dqBt912W9C57t9//23atOmiRYv++9//hnBREZI0c9EdO3bUqFHj3nvvTf6VnTt3lilT5pVXXsnMdxnAKK8dknv4mOOiDg4+YH4hosYHJBcieeeOlIEmP/744w0XFVQzmeGiP//8MyyXdLIijwkAkchBLioc0G4gDRo0yCgXTYNkpu1bI0eOLFy4cJ06dey1UMzOO+64g2q5+eabs3WXO6ZvqVKlxP0oacuWLXv37p19n4sJTD6zboHtTcd///3305yHFPDQQw85LnooIOu5KFTzo/0htxC6+meffcbPWbNmwUX1aP369XqLvvFRACGH5ThE93GPiy66yBcOGyF80KBBwVe2bt2qEd1HX1966SXCr776ajsQ1dmvXz/+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NX788cfBgwdTM1mb7JgxYz7//PNg+J9//kn4iy++2KtXr6lTp/79999Z+93cgO3bt1O03r17T58+nfIeUl9PHuiE0aNHh0T4999/586dO2vWrMx8JZ4cOjg4ODg4OBwQcFzUIUVs3br1tttuK1iwYCQS+eqrrxLG37hx46OPPlqqVKmIhzPPPBN7GtoZjLls2bJ77rmnQIECilmlSpUyZcqUL1++QYMGDzzwwOrVq2Nm5pZbbtEr3377bRYU72DBNddcQ50MGzYsC9OkhkmzbNmyvvD169dfeOGFr776KgS4devWxGnRokUWfjc3YOXKlY0aNVqwYEGrVq0oIF3g0Pl6kli8ePF///tfsnf00UfHjLBnz57u3btLFdx///0pfyieHDo4ODg4ODgcKHBc9FBHJleuzjjjjCS5qPDiiy+KYf7yyy/hMW+99Vai1a5dWz+3bdv2+OOPE3L44YdPmzYt5ivVq1d3XNSH99577/LLL4ccZmGaf/31FyTTdxMggZUqVRoyZIh+/vvvv7fccssNN9yQhd9NiDQsw9asWfOhhx7St6iEl156Kbu/mHu+njw2b94cwkWFPn36ZJSLIlT//POP+RlTDg8srFu3bvjw4ZlMZPLkye+++26W5Cc1rFy50v65ZcsW1M4777wT4qKyY8feP/74///ef/+HXbv+3yL/999/n+3ZzRz27Nkzd+5cBrKePXu+8cYbSfrs5DgWLVpEo6ThQ3/++WeSDlB052BMAtOQSYccR45rLYdcBcdFD3W0atUqM69feumlGeKiU6ZMIX7+/PkTxnz44YeJWb9+fTuwY8eOBJYpU2b37t3BV/73v/85LppTePXVV6n8tWvX5mAeMinMCbFgwQLKmFMMMGe/nlH85z//Ceeib775Zka5KLRz2bJlmc5argD95ayzzqIGqKjMpCPanzdv3m3btmVV3pLHjh072rVrN2PGDBPy2muvNWnS5O233543b16DBg0mTJgQfGvOnLWRyP+x/zVs+IoewZdIMKZ6zw2AKp9//vljx45dvXp1+/btqfl69erldKYSAEmrXLkyWU3PzCBqihaUw5Tqp3fv3nv37g3GhHk+9thjFSpUUMySJUueeOKJpUqVqlGjxuWXXz506NBdu3alIcMO6UfOai2HXIis56Io6wX7Y82aNXq0Z8+epUuXzpkz5+OPP54/f/7G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wU41xG2I9GPw4MHFixfnLffee28abv/Pf/7TuXPnM844gye8+eabSS9eIsDoNW7c+LTTTqMMlEeJM2fO5LJatWpZUiSDjRs3XnfdddmyZaMw//u//5u1hQkRwoPkc9F///vf607E7t279dMvv/yyefPmFStWLF26dPXq1d9//73Sv/vuu3XREPKfkwF33XUXxos2yuqChAjhBWbk9NNPX7NmzclTgMzhNlle8WD897//LVu27LPPPpvVBYmPU42Lfvzxx02bNl21alXit2Th8vuLL77Ypk0b49Yb2EWaPHlyZnLRkzwYwY+kFDhWQyQXgwYNSjMXFerWrZuFXNRxV0Fz585tc9F9+/a1atXq5ZdfzqoiGfz00085cuRIChf9y/WCECc5ks9FoZofngjFS/z222+Mglx+9NFHcFH9JIazffv2D6PhZJ71P6lw4MCBOXPmjBs3Dtn++eefnl8R74wZM1566aXPPvvMb0FwatVA/J04cSJiNz/hUH766ae1a9fGeL3zzjufuqB9582bN2HChD179picvPT9998/evQotzBobdy4Uen79+9ftGgR/xw7duzdd999/fXXDx06pJ/IzE+TJk365ptvPEXatGkTpeWNe/fujRtLxpN59dixY+fOnWuiYgx4y/Lly1944YUFCxb4H0X+WbNmqfxUjcKYU1IQFJKhmuvXr/dL7Ouvv+aWDRs2UFm0+o8//rAzUGuexj80B56uXaqVK1fyzLfffhtBJVhrXvTBBx/gb/E0nmwfnHP48GHqnqoqc4vmthmW5s+fzwDJM51AcAuPclx9QM2mTp1qZpFsxKpaLN2gADztlVdeWbt2ra1LUesVNfPnn39eokQJlBO5IXCTHvBku1SfWnDcbmIuaWJl++qrr5Rigpp27dpl7FLUAtjcZvfu3RQDx4jqewqAgtEfuZG+yatNujodQJ5K2bZtm1KMKsaqeFQEGwd+pXHHjx+/bNkyfyGprA71wZ2i886cOfOXX37xiNGvnPTxq6++muJ1796d4m3ZskWZf/755/fee081QhPQc6UfP34cU0AJ6Ywm0cCvDHFL5bhdm2dSL3L6A9L4dcmSJagrkjzVuGhq8e9///uxxx7L6lKcALqMvUD31ltvZRoX9bz65MdJ2HwBwKClk4t27Ngxa7ko+Oc//2lz0ZMK//jHP9LPRbHkd955Z7KK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dphfjx49On78+K+//jozi/Tnn3+uWrVq0aJFmflS4ccff5w1axbNFCtDlggkQdCC77zzjv2NNT8Q7KuvvupP//333z/99NPhw4dPnTp13759GVTCWG+3kUgt4sLf06dPn7506VJ/zp9++mnhwoXPPPMML7U/SffVV19NmzZt8ODBEydO3L9/f3oK48cvv/xC8T7//PPkPjYjsGbNmvfffz+rSxEiRIgQIUKcigi56N8HeJk9evTIly9fJBJ58803M78AixcvvuSSS3j7eeedZxI7duxIytChQzO/PI7rr3ft2jVXrlzNmze/8cYby5UrV6dOndq1a48cOdLkeemllyjh9ddfnzlFwkcfOHBgsWLFeOkdd9yROS8Vtm/f3qlTpxw5cvDqDz/8MFa2TBZIgvjjjz8eeughqffbb78dkPOf//wnedauXWsnIvaWLVvOmzcPIooEChUqBEPLiHJGfbtB4rUIQNSevnPnTi7z58/PK+zM33zzTf369aFbffr0IcN1111H4vHjx3nCAw88sG3bNp5ABznrrLO+//77tJXHgx07dtx77725c+fmdXFpedZi9OjR55xzDuWkwFldlhAhQoQIEeJURMhF/25o1qxZVnFR8Nlnn3m46JIlSyhSVq3T4vdny5bt448/1iXUFP+bEpJu8uzevbtFixZz587NzII9//zzmc9FhauvvjqYi2aJQBJEq1at4rK4ESNG3HLLLT///LOd2Ldv38qVK+t/yHbr1q3F2X7//ffkljDq2z1vSaQWceHp6VTn9ttvHzx4sCdbrVq1unbtqv+7d+/+xBNP8M8999zTuHFjk2f27NkVKlSAzaanPB6ojh4umnRppx/Dhw8/1bjooUOHpkyZcuzYsawuyAn49ddf58+fn4URPUnBhg0bJk6cyECT9CcfOXJkxowZe/bsSeIz/x4yN9i+fbt9efTo0WXLlr377rsm6GP16tWJPw3hvPjiiyaygzb933hQnzp+/Lj/J88UYTC2bNkyb948bPtHH31Eb1Xip59+6rgRVRkasuSpdSygjVOnTjVlCxEinQi56N8NOFVZyEX/85//eLhoFgKrfeaZZ+Jke9JhgO3bt8+SIhkwQGYVF73xxhuDuejJDCSWBhaHJhQtWrRJkyae9I0bNw4bNix5pYuJjh072pdpq4UHifT0L774gjzPPvusnbh3796c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ly9fxEPZsmVPykDFihULFixIYrVq1bjzp59+evjhh+vUqaM7W7VqFfLaKVOm6La8efPeeuuty5YtC96DQfzQQw+VKVOG2y6++OLsKN0PP/zQuXPnY445hk+8+OKL2fGJwwO0bI0aNdRkw4cP9139+uuv+/TpU7JkSa6WK1euX79+GzdufPDBB0uXLq1HihUrZsSmSpUqxYsXV/r333/P42PHjj3vvPOUkjt3bsTp3//+N8+eeeaZnTp1iikbDj6kqrOcfPLJvOHll19OYd4cHBwcHBwcsgmOix4O+Ouvv1LynubNm2eNi6YqA9kH6ChFK1So0P79++10LODHHnusQoUKJmX79u0iFUcddVTIidJnnHGGbrvpppvCPz1x4sTs46JCw4YNHRdNiF9++aVSpUqii2+99Vbwhueee46rH3zwgUmZPXu2Wvmjjz7y3fzmm2/my5dv8+bN+rl37968efNyZ/fu3ZXy22+/jRkzRonZcWx9Ojtd2r514J3lmWeeadmy5Q8//JDCXB3q2Llz57PPPpvkzWhIugDineT9P//8c/AwzD/++GPJkiUzZ848CP011q9fP2fOnPfffz/cmcUHusCqVatQCDwoPxrhzz//9PlE/Prrr75RxoCGoLoOtABJ48cff6Td42UmC+BVS5cufe+991L1wuSR8rIcyUBER48e/fXXX6fnc/SR5cuX88VBgwa9/PLLB+60wmhLFzaDr8NhAMdFD3m88MILqVoEgFZljYt27doVQz8lecgmDB48mKIdd9xxMa/Wr1/f/pknTx5YK/fffPPNMe9/5513ypUrp0Wz/v37h3+akTu7uWj79u0dF00GtIIW/4sVKxYciT/77DMu2SMlI6i4aEx7mmq3ZytOOOEE7nzooYfse4YOHUoiH920aVMqS5LeTpe2b6WhsxxRWLNmzaWXXnqUh4Q3//7773379kVJ0gS33HJLMu9fvHhxt27dfNysT58+xx577Pnnn9+zZ0/eU6lSpcqVKy9cuDDrxUgRvv3228aNG0cyULFixZUrVybzILz6rLPOQtXPmjWrV69e5cuXf+WVV3Rp7dq1VNq///1v885TTz31xBNPZHQ477zzJkyYYFfO7t27GVM+/PDDbCmehS1btrRp04ZGJ0vhm02Sx8SJExn1eOH999+fkhcmiewoyxGOZ555hsq86qqr0vCt77//Hn2O8DDgakngiiuuyPLbdu3ahZkqR7AcmRNxyCaknotu2LDho3/im2++0SWGutWrV6PW//vf/2Lkfffdd+ap/fv3I6lLly7l0ieffLJjx46UZ+ywBPVZoECBl156KSVvyxoX1VJGOqd7s4DHHnsshIv6eMK//vUvrCj538oJ04dmzZoNGzZM9oePewThuOjBA1rh8ccfx1Cmuk455RTf3tFt27YVKlTITsFqDOGiyAY6zfzEAA3Kg/htyl3f09np0vktx0VTjr1796LQkuGiAh0kSS76xhtvtGzZ0l4z//LLL+vUqVOsWLHXXnvNJO7btw/2wjuxRHNwHy/1cO65506ePBlzduvWrV27diVLNWrUSPjg5s2bixYtOn36dJMyYsSI/Pnz25NZM2fOVDffvn27UqgK+Rk1aNDA3j1ODbRu3XrFihUpK1gc/P3339pKcID8zW7f4cOHp42L2t9NVVkchI0bN15++eV2J80m0Ih0sVGjRpmUm2++mU8f4GvpyI6LHmZIPReFar79T8iMQwUvXryYn++88w6EU5cYEvTUmjVrlIJ46Z+YHMDBBhUrOvToo49+8MEHGzZsMJewgCdNmvTMM88sW7Ys6Nby/vvvT5gwYcGCBVSyTfttLvrHH398YCGetyo0GEOHpxYtWsRtjMSMsuYpM+vMV5RiAiOhpHjkhx9+YJjB4ier5CroCogF/Oqrr44ePRrh8Y1DO3fu5OtJBomJx0V5Z1AjU6JvvvkGks8jvXr18l1dv349xhY05gC5aEjRoh4veuGFF5566ikMvj179gRf++2339JSzz33HHUe5KJwJF7+7LPP8nJaOWbAnuALX3755TFjxvBI8Iu8Qe8nq/TfsWPHJhnjivvfffddXks9B9fWFC6LsYpPGzPOALHho88//zyCRPaUmKSAxQStwOdef/11zbL7Joa/++47aKqdEsJF586d60uJyUXV+lnewbh27VqsZ+ScDmhUYrDTKf2rr75atWoV/8yfP3/q1KkUx1SUOMCWLVtMSrDjoDQmerALG/wWt+kNGDS6x7zTVkFRT89wP6KIlNrLYiGynTwXjafEVJBge6FqZs2ahZ4hn5lyzjwMgGQmz0Vp8WS4KB2tTJkyds2jvWvVqsWzNGvw/uuuu45LAwYMSD7bqQXKEOPE/GRY1NbihJaGyLl9GyyUFHSgSeHN6ub2lA1dTJsChgwZYr8QVVahQoU0uJFXrFjxAPkb5NPenqBdDGngort27br99tvtlAMvi0P6MX36dFqNgSm1r7322msdFz3MkGIuymgEjcRY/MGCok1u3ryZS0uXLsUq4jaMSH7KWQULVfwTBRT1NLVIKSwltdk7zIAFr7G/devWDz74oKgCtX3ppZc2adKEup09ezZ8qWXLlmY2GlXOVbQ8thoGKzbKoEGDzAttLkrl01j85P4333wzyBP0rX79+mmV6Z577iEPfBSiUqJECVIuueQSYxHSsr179+ZOuPHWrVtvvfVWeYJhtZx99tkydkGjRo3ssZyRj8yPGDGiT58+BQsWrFOnjr2Ayft5pGfPnsnUVTwuCu/yjXlRj4tStDvuuINHyLOPQXXp0uW+++7jnwPhouFF4/1Vq1bF+id7DRs2xGaCRZirdJ+77rrrnHPOoX0hnM2aNeNmm4tyc5UqVcaNG8cYAAnMnTu3bYQFAR+gRS666KJ58+ZBEho0aHD88ccb7gQduuaaa/Lly6cNtLVr1+ZzuT2QgfCyL1++/LLLLqPysecwJkqVKmXvQ4MblCxZEq4Fg+ratWvhwoXp+OYqNKNmzZpkCYbD1Tx58ig9oYCF5EdcNJohDz7jOHkuSo1RS76Xx+SiWn6haDt37gyvqyDIGxmmRJ988gnNTQNFY3U6yNXIkSPJDymUCxahPKMfzHKNnFCwp2lfxfGyS4TA0Ezdu3enzgcOHMjVdu3aaSNcsIMjqBdccEHE2ilNDq+88kopIlXjAw88IJmkQf/zn/8oD+vXr48mku1kuGg8Jfbjjz+SeREMOKf9yIwZM2rUqIFIU/zSpUsXKlQItcNLfCThcEXKuShNcMYZZ/hq78knn+TBevXqxXwEXZQrVy5kz0xhpBnB6YlWrVodffTRu3fvDn+wW7dumosxKe+++y4pKFiTQh8MclFw4403Bue8AH2tefPmWSlGZnCA/A0DAK1rexSnh4vu378fdUT3tBMdFz0UIfmPaT0eCBwXDQcD90cBmBlYrRhhRzEEr1mzxp6V5kGoGRWLQsPwS2d3SzEXRa1jfMjm8AGDEg1ultcMNY1mkE9jRGJqa+HUxZ9ICC2I2T66vXr1IgWbUj8xH/lpOMPEiROPOeYYI5QYZ1iN5lmbi/72228tWrQIRhwNQpTMHoNllMh0NoAqkJmot0KOOaLNlnBmTTrQAbQXpVOnTrofaTnrrLPMou7TTz8tfyfzQlho3rx5YTLJVJS4B1b1cxmgKrD1y5YtG4+LIqJYKjw1ePBgcwl7t2jRorLss8xFw4tG29nrsXQEubeZxzt37lytWjWjQeBFij5quGiHDh1g9eZ+7J6YoXoMsIpgfWZRmqYne7zw9ddfVwpMTzF4IKVaCcEyiyTycIN9QYmNK/7nn38uVkYdRj1dQT3zIVOK/Pnzn3LKKeZx5AFqof+pK2xfU2PhAhYCw0WjGQs1wKxwhnBRZEBig7wNHToUJlOrVi3fy31c9LPPPlOHKlKkyKuvvhqesSC09vL++++bvMG9zVW709FwXKVopED8Fi5cyEACLfz444+5evzxxxsuKijsljHNf//9d8piu1EhDNwAfwt+SxgzZkzkn1G7qFXDRWlKMq/JJnQIOn/q1KnY/bR4QtlOhovGU2L0CMh2/fr1fVyU4RZJM4runXfe4Qb0Dwzf7B/JKdAp1EzknFqCWpt5Q5ps+vTpkGd7w6FAi/PUhAkT6PLxApAw4D777LOzZs2iWoJcVAGKxo4dO2/ePE0BGyTDRcVJbFaJFGnO4pFHHon3VO3atbmBMSvqGQBmOX3Lli08brvhyHhFCeunHaQE6ULCR48ejRb1efxu2rRJ5ilVN2XKFEa9EJdgagDt1KNHj5BiCvJRP/nkk00XQGIZBaTHhHhcVEazimwD05B07ByTQitT8/F2Zau9DKKeD7D5aZYu6dRKkao0/A0ZYAiI58yybt061Brjvj0rhPqS6kCKeOG2bdui/+SiCN6kSZMQMHufghDSRsi5rD7y8/zzzwefRbY1C4yO5bvLly9XejJlCZHqeLWK2Yk2o+xBvhTey2gvmVW8RD4aZjaZTCob1KHvKcr+1Vdf8QjKBx21ZMkSn9tavPoJKRqXuJkMIE4+Hyh60Jw5c2hcJMQ4IQoIatAq4FleQsOhiIKTp3xXoye38Q+vDTHRf/rpJzKsiUjeJrGkouR7ZftTICEUindS4fRfyggLCr5QTlJ8lDI6LhoOFODbAUiW6Mj6Sd/UPwihOinSwuCoS/oHypo2OppiLoqUUAB6IGVA7CAYMTWCOjl3au2ePqxi6ypdS566tmZ0iIkgF8V8L1SoECaOfqJkucHY9Nq3g6jpJw1hOxoZLoqKady4cZLRJoKmKkORdneYbIBKlSrZS3/16tWL/DNmqdyccufOzaiADFSoUAEm/GcGEAYN9ra3cPK7j8RFYTu3ZKBLly4tW7YkJR4X5Z927drxFEOyGRKgrx07drQLnlkumrBoSD6mNsO87ketRLwVY/1kDMuVK9eIESPsT7Rp08bmoozi5NkMrozZttHjA0wsEjjmhMEj4p1/YzSRiJa9hgDFIich7o5QYqjInxYw/sx6AgIDXTGVCapWrQr51/+0rCrNZICx1rRCMgIWEzYX5W0aKU1/CeGiDH5Gcuh0J5xwQjwuSs1Xq1atWLFiWiOCuGZtTk1s35aup59+2vwf7HR9+/YlBTPO9x7ZcDYXVakNF+3Zs2eZMmVs93gYY8OGDc0NwW/JJLW56Ouvv264qKBDbnwnhYbLdjQ5LhquxGTI2lxU83G2T3X58uWzY7Y+U0CeTznlFLIxaNAgtFP16tU1BQBhw8y9+eab6Q5a423QoIFtsNIudevWpbmpTBR73rx5O3XqZI66jXqCjeK64oor6MWYs1RmwYIFbS5KN7nqqqtQZU8++SSyisTaVl0yXJQMIFd2iqYVAOQk3lO33nprJMM5haG/cuXK/GzatCliQH+nEeU5/+ijj0rYYB29evWiSxpRxHqmXGS7f//+hQsXPvPMM+W6T0k1oNx4441YushzqVKlfKLlA3V+5513JuN7Rd7OOecc3kaXX79+PV8vXbq0ZhAMYnJRKDSZJDEYlBihRe1QdpNyzz33cOd1110XMw8IAKpAn5AGo07UxU466STDRT/99FPKjvDYXBQlRhdGwPLkyYOCtTcLUMM0NF1m1KhRjPjc8NRTT+nSyJEj5dqAdNGDNCmmjn/ffffxFDUsjXfWWWfZ1RivjVAFl112GRngWS6pLOPHj/eVdPXq1bJDEA++a0yXhGUJl+ogIDxoOWr1jTfeoNrpR7bSCOlliO4NN9xAn8JOQB7OP/98+qwmYigjH6VFKDUp5FDzuTQ3r5LA0yWbNGlifMGoK002hdRPSNFoQYSTHG7YsAG9ymuND9S6deu4+YUXXsCuuPvuu41jEeqdcZk7zz33XLtCkCtyzhcx/OhH+fLl43MSJMZHjCUeoRV4PwVRc9AR4rm4Y3Ug0ornR8fnf/JAvWHgkSKWjjmB9VW0aFG1bP369bEQqAE+5OsyGDynnXbajBkz6OnUkmrScdF4oMWRW/SP7aCqTrps2TIxL34yUuineuiqVav4n780OkpPl9I2XZtiLrpx40ZRbWxfEWvgmynUAqkpc9TbyaM7tdSzc+dO/Uy5l/nhhyAXjVqb/qlhVBg33HvvvUpB7YqSobyCU5IaA9DOdHVNziWDoKkKNHBef/31+on+uvDCC+0b4EvcALOyEzX4oYZo+oi3yHNpADZ9TR7xfHTR1CFclHFRQ4JGKXgXo6/PRs8sF02maKYFt23bJkuasU0pchhbvHix/QnfftHevXuLSVK6hDWD4cLNvoU7OqZGCGpAKTI7bJNXxQ8hWlhF8MNgMQ1zMMWEW2Ka64tGLLXAhZz4zD4hoYDFhM1Fo171arBE4BHg5H100d1YKr6Xq4poL4qjJaBTTz01mZ26MfHjjz8qmDOU3maSQrDTqUKQc9+dCbkobWTbxEFkjYvKjzcYMjREtqPJcdFwJXbXXXf5uCgGUOSfu/sUVCbH/W4U3Fsey0rBRiSlTp06xszSCoDxXWdwLFasmDHQoxlRc7DPTEqrVq1gKYYerFy5MuKdUKWfpEMezMwvVkuuXLngFUZQE3JRJNP3xWjGUjnQjuWYkPs30Oqf1htpHXODPL3tDQWY1zSo/t+6dWuNGjWMCkJjiMrqJ9qPn3RnzFbU159//qkAJ7bbv/D1119LYdI1bM/bEFBk+nvEi2aHTRx06zVcdMqUKVQgfyFsOpQ4Xkg52ghz3wjws88+y8ttHxwfaDj1ZbNKDPOMBNxD4GlGsHU/8qAUWCI/zzjjDHMz9MAcN0WNVahQwe6zNLGvC6vjo9gpoB7RcWJGqYa0EaKrvlmzZk1IBRLYpk2bmHGMsQoi3uYgOzG8LAml2gdyWL58eUNlyRscyThsJ+xlsMfixYvzCYwHCbPagjGXIUlT5FBBUgzfg7PBWkXd0WA6IkiqVS4b8eonvGhIOx81+cTSM6udKJN27dqZS/Xq1ZO9jTCrXWwuqrkk44YTzZg5euKJJ/RTZ90dc8wxXbp0EXlGwjXexaxhQWONPfqoEszogwhpoxn8XIINE/bl7amnnipSpIhZp2V41VDruGg8II00aMylGpqYS6ZfQMf4qWV/LQGaKVqxuTQE/RZSzEWxs8n6+vXr6T8IGf2HwviO5tu0aZMIN9A6BjejyrVHFLvTkNi0HX906CImF416AzM6keFNSueee+4xlwYMGKBRk4Fn3rx59lPiooy1Ec+5LsmzvGJyUX4WLFgwT548mnHp2rXr1KlT7RticlEGLRK5c86cOZGUBoaNx0XpkyNHjvQlGi5qslSlShWkFOPJ3uSTNS6aZNGWL1/euXPnRx99VKYkOl3pGvt9Tiw+Lrp3715Z29Lp9uJhEKJ8QdZ6+umnRyxHzcxy0V27doVbtMKWLVt69OjRs2fPzz77TDMRxveY7q91VIbejh07ZlbAYsLHRaNePcv9+JJLLsGQSj52EU3jS7F9dL/55hut3GJeZ/lMvAULFiiAFiVFgO2ly1RxUWwvWXgh2UgtF43Gl+1o0rGLQpRYkIvCQm3SAiB71apVMz8xp6r+E+mJnCf6ZLgWGD9+PCl33nmnSZECHzp0qH5iCAY7ndZXFYNN3iW+jdwlS5Y0XPTpp5+m7La3AuQhYq1nJuSicpow00CC2YAdEgNfrvVAc+1YtHQ3rEzDx+AGXLUnB9FjRtchXYicybYW1YGMVHVVupt5Vscp+Tw++DSmPwqT73IV+hGuHg3oL1IUknyfnWe4aIcOHagZhI2xhnGE/MQ7qVXzDvacb0I3n0GDBkW8dWOTwmANiTJ1jq119dVXm6vq+7aP9/HHH08p9P/q1auRCpSeqVJJV7du3XRDPC5qx2jQHMTDDz+sn+FtpLEvYRjVEC4arywJpdoHxotTTz3VTnnkkUfIvGZwEvYycNJJJ/kGRO2UsecpYIl2YHbFDrADqosBco90e8z6CS8anQUZNn0EAmx8oOB49rzA5MmTTUeD0Pr4HndSIvu7cBLezABkpAsiWrRoUXMDtrqvxwUR5KLaS2KPpzQ0KdAnk0KFmA9RnyVKlLD3cUS96TbHRUOAVnn33XcRBoYD2BbNbaYmYWfyXcX0pVcqoCyVjJWirZGG82ObyV83PXnO3vNF5bJLCYPWGIamYuqqE1IvGCiioKtWraIq7Si7DvEQ5KJUWqNGjUiX86R8dG0uGvX2K8r7K5IxJyeIiz7//PO8IWJ59oYjJheNenOusrTknOmL2xmTi15zzTUkIgmTJk2KeN5ryVVDYoSf6eKDzUVNHNSZM2ei3O2emTUumrBoNByaFyNDBrGGc2OvaxzyTfYH4+jS4zDHRYcYsEP2KyoEVDCIi9LNwJZZLorNFwnM2fuA5c1rzY4gHxeNejOgMFXt2mVc901OhQtYTAS5KJgyZYqauF27dslz0SB8+0XfeOMN+Rz27t074bPxsGnTpmbNmikP9ErjEZ0qLrp582b+P/3000PykEIuGi7b0czE0Y2nxIJcFPFo27ZtxJvjR0joO3Aze4YUjXfTP5GeA2yCXDReinFsKV++fMGCBX3vUdOLwUqH+1yK7P2imHGowaC3gjGRE3JRjFpfJk0+g5+2QQ51j1EjMvrNRJiOPcT0lGc+xtD5559vHqfV0H7BnMt3Q10Vgmfu19vi6eeffvpJnrcMOvEybLBixQr4AJ+AB8rJEFG3rZqYPrpz586V62bMPCisS6bCa2/bto12NLv0sZ0UZGHYsGFKofVt6huM9yMGpVWRp556irIE61OR+aLxuagdu0jtbrbdhreRdpUnnKAM4aLxypJQqn0oXbq0bzLFRsJeFo3FReOlGAaoqHK+lQMxWPWamPUTXjQYacQ7LnvcuHE+M1suVCjJIGdTMALDRTVYB4NpSYeb3Q1wUT5krm7YsIGr3BO7Ej0kz0XtvbW2vpIF6/PldvtFQwDtNHtEzaZQ44CAkDD22ftIzQkFomBqGvu29ASRTTEX1bSN6RJyvoVwUpgdO3Zg9zAA6BL9M+jBi6GgqUGRdTs2gENMBLko4yu2u5k+9HFRY4ExjD355JMMRfR5MxFi7xdFWefKlSuZmCvxuCgDJ6QOnc4AFhx+YnLRBg0akHm0OQIQ8U6A9HUDRCtr5zQm5KJYq+ZbefLksUcU7URilLWN5mhWuWjCovXp0ydinYvgs9fFTMw6ieDjoqaVd+3axYgb8ZxF42VPJ6kGIz1qXdQ0a2a5KKWj9WnNoH/p9OnTKSw2k4+n2VwUPWAmShnz5CDn2wwZLmAxATcOctFoBq2NeNGt7PSEXHTQoEHGKTEYRxfLVY9nQWixTkzlL1y4UKGAzPbLVHFRGgILg55unLENjL9WCrlouGxHk+Oi4UosyEWj3shyySWXYDHDhIcPH36QHIacPBdVClo94i3l+VSHmqNx48ZRT//zvy9Mg23bYR+fd955IblKyEW1FGYYi7BmzRqJesjWdHEbWwnD8QzrQBRr1aqlLQMyf/v27WtC06FnSCcl3sszy0Wjnqc9qt5QOwi/vTbesGFDpW/cuBET3GzRf+utt7QL1GytjMaPXfTEE09EPM8Oe9lHuP322yPezG+87MWE/HTUrVCkaH5UluaSUM7oeZuQxONvUuM0MVIRPEfNIHkuKvlM2EbZwUVVloRSbQMrlAe7du0a82oyvSyaGS5qUmJyUfmsyi89Zv0kLJo0XsTb7GAzut27d8tNPeLtQ7bNaR8XlfY2Am+g6RKzDp8jXFRDhi/ugM1FZ8+e7fNqMeTqyASDHX0W1aol+u3bt4tqiXytXbtWLqjr1q3TBlE0tvzMTVgjHpenqpBlx65MIcVcVA7HZrcrAsdPrXuoCvhfBTOBnuj5VATaB+IuRUOfedud6ZIcOnXqFPGcWvVTO3ny5s1r1J/80zC19RNrzO6o6ufGerDj6GKJoo4ZdGNGRbahfeSKs+eDZuYKFCgQ3PIX5KJ0FRNJiPxr92D37t3tpyBOZjsE4pHMapUgVhCPi44fP94EKUUIfdpTnmMRb2nUfkrco1+/fuGf9pnXCYumECbGXqf+I94WMv0cMmQIPytVqmQHDbr66qsjlj9tmzZt7DdreiKezfH5559jkEHqzDxR1DtmiYHHDiyUhf2iEL+Itz3GXrGkMvv37x/NkA2bi2rrpg6c5EMmorJ+Ihv2IokQImAxUa9evZi0EFlq0qRJkIsuW7YshItif5s1HKBwKT550IbtfPny+VgZ1R5+FCp2iW2nirqblwc7XTwuKtcyswePkpYtWzZihX1SDumPtgBgZxvSHvwWw3/kn4ve48aNi/zT1zcmFw2X7WhyXDRciQW5KEMMjZvjIXODyCwXpQsr5IlP2cpptkOHDvwvt3afD79t25UpU6Z06dIhuUrIRZUl3w379u3TGmDQd91APh2+oLLQp9y5c3///ffz5s3jEi0Lc0MmKSzSYiZVtc0eGzTey7PARQHm+8knn6z/J06caK+NG7ItCmGPg6pwe4IvHhfVNsKItXRpQHtFLJ/PJCE3zltvvVWZ//LLLzt37ixTfsyYMcZXVgjnbwok7jsT2EZmuWjCNso+LppQqm1s3LgxRMkk08uiqeOi2k2jTXox6yeZos2dO1daHdvPlijKQn9kKI94u3xNbD8fF5XWRXX4XnvvvfeSTr/QzxzhohLv0aNH26+1uShDm8+rJQvHpx3ekJ8prW+WAI0nOWaAXHaj3mwgXUN7JBcvXqxL9hbibEWKuagIJ4WBWJoVXrljoaP1E9Gh5HJN5h6FbNJSMlW2evVq/W+HS3WIB+2batu2LXXIOAEXlRpFiTB2TpgwQd62F1544fLlyxnmGTNsCoTFCT0z+5g1Oppj03TGN5Rj3bp1IXng5dzGQAiLePbZZ+1LND3KMeainLiofbpjly5dKlSoYGbvNKMsZQcBGz58OJzKkOpoRvDYkCMEbGirhh0rQtiyZQvUCMVnQjiIftirZ4goVhRjoT05wgCjqrYJW0xgY3EbmTcp4UXTXCYNR7W/+uqrWtgsXrz4qlWrYFzwOkUBRaej0Gn3WbNmyRe3cePGitpXu3Zt2/ULhuAb133QNqQbb7zRpEAR+YppC2pAhqYZVKgKRdaxj1vwYcWKFXJSZUjGfBk7dixDSMOGDWVfKm4No6wm4W6//XZxOYpM96d6CxYsaCJp87njjz8+SLRCBCwImr5IkSI+30KDXbt2VatWzcdFX3jhBbWUb7UHrk53Y2Bu1qyZUsgwlD4oD6TLBIdpG3NWgTci1ixSEEgg7WhmEBgYsNHNwVfBTqfDnMxxKQaaruJ+3kAp6ONUFymIvVoTCxKeH/G8oGkFBBLzyI4oE/wWvA7+QH6mT5+OzkeAW7duHfF2b9KayrOOBTKHSwnhsh2N1VmCSEaJ2T7n0mMoyYEDB44aNWrSpEkY9Amn2NKAzHLRqMfcIgHHTjEEaTCZemZaSrBtOzWBL/hZ1BN1/ZOQizKUxKQc2g6K0MZ8SpYrMuPzhRkxYkTEc/RAM2hxniKgWmkmOw+QEESucOHCvmg0CJs2x2aNizZo0CDEV1NAr1J7vplxDHd7ZjMeFxWtigQW6qMZJCTojxAO6gE9ieZZtGhRy5YtzacZPqCmPieUcP4mDWwPwcLChQtVisxy0YRtlH1cNKFU25DPDsaAj22SbRnlCXtZNHVc9PTTTy9ZsqT+j1k/4UUzk7CMqrfddlvEmtozlzD8FHLZ2Bg+LkpzR7ylYB+L07qo8UPJES768MMPcxXj0H6t89ENgYL12GsPdGFsKnjmjh07jKeqLm3dutVHOLnEQI/Jp7M2feF+sg8p5qKUH5Eya7uYPrapStmM+zKQYa1LWL3yyxUwm9KzLnyog+qVBY89Jx7C0K4NLSVKlICLogflUESHR9X26NEDnY65zBDCUAQhVOwExPS+++4Tu6hevfrIkSP/+OOPKVOmYDpEvN0Id9xxR7zZJmxK7ehD8wYP1cDC8B1AIoiLYgeg92+99VZuu/LKK+2VmagXVl5Zingusr4gQ1oMTMhFGapRqeIJEW/iEP5TtWpVOLb4lfDpp58yMjGmyhkS0nLnnXeasQoT3PbI6tevn7xGAW/GcI+pFpFh8qxdbehWhnBjeYQUDb2gE0EYLMkDDEpLTJUqVZIBrS3BehYWgbHVvn17qCM8RAq9Xr16NOIDDzxAKzOwof0TxmLBVuANfAhe2q5dO15oTrqjTbVgHvECFSxZsoQUxSaNeKEFfcalDbSemDNg+EeKzITcDz/8oJpBxhBOCqWVvQIFCjAka/WYcZqaQQ6x27p16xbTUSKegPnQt29fWRg0BHQlZjRmqrdcuXL6n6ans9A0yjxPQYYVy57WEceOZERGGTZsmKiXkQc7PidsTW1NiTAXdFKc4qAYj68gqAQE9ZJLLpk8eTKVAD2jO5urdqdDqCidZAa5pRrtZTEKomhkEW+NmjJiryNLPXv2NAuzvMHco/i0ts0Xs4NTcCUipYMHD0bwKBHMnJ7Ca5E6qQ54OJVjXEZDZBt2Gq+z+BBPiX355ZcQ7IIFC0Y8Xg010qwHedNqoQ+Y8jnrepMFLkq1RwKxpuhWtLs8FDQ7Wb9+fXsAZSygOfS/lpGpQNtnD7vWxPhJyEUZ5RlT7KOeTbrWvX3RpATNOwTPHMIORnIYxUxwqenTp0sP+IKsyv34iiuuMEXjHzqU9E8WuChKBmkMWvk+dO/ePRLYB1urVi079AuCLaHycVGdtIROCM6t0xn5uikLtcdLklnS0ekvqCPDEtH2VFcwJlA4f5OrBWrZjp+E6WV87+kgPos/nItGE7VRklxU/t4+khNeloRS7YNcnakxY4Lu27evc+fOar6EvSyaIi66fft2ZMO4EsSsn/CiYTvZZ9Iy1qPAVfl2EF0d/2uGGx8XjWaEsLaNnKjHye1pwRzhoupZaHXbOJQvT8h2gCMZijlEtxUdZRDUUidEFFERwzJiTF97O+NATWwD+ql8jhAhnbt5qJ7pIsCqKTaiE4wLRwrpXA3G2kbL6FLIiYUOQaDpMNpso4o6tMk8zWH8cGScoZjQBRh/qTLFUKkx17FpboxCH8MUjI8u3WPVqlXBsxkESkE+7ThgBqSE+Bcd/AgpGr3DrhNuoEF9hw5Tb/BndRYf1VQrw/ow5jIVAAzJQZZCdhBlDdAhRpqYx5rzOdt6ozakGagcWQmIFjox3sHlIQKWNaQtdje9Epsb6yfeDVTX3x6gfzE7SLxOFwQvQdLMoBLPrZp0milmMM+Y36JRyJiaib+2ERaCZGQ7HJlVYjBz6pkRetmyZfPnz585c+akSZOw/+C9mYock3LoUBN7223wmBOFOjOL7XQZOAz2q2EImzdvLl68uHFIoRVgKRFvmo8iI2aQMc3E8Q/WBt1NewQqVKhw9913y1sBI9W0u75o5yEIHT8YHKkREmg/76eeTSJvVtQijOOYjaWQdcaylP+C7bktYFGJ75155pmPPPIItjiU2+xOlK+B7XjJPRFrX+vIkSOvvvpqw9/ICTWfTHg85BP73u6qSNTRRx9tx2idMWOG8mZ2j8MqtaSDVR0M1Y4MQwLtbQg6IeO4444LCUQsyLPd3rCgHSjB4A4lSpSI/HMbhfZBmDlWRWUvXLgwDQp1h1LSKYw3itzdyRi9W46ao0aN8pElbR42lRPeRnIzSRgsCsVCpSEDjGsrPCQsS0Kp9gFFp04BXezVqxdiAO8yi6gJexlQ1CibZSnFXn3RPKzZUCAuavd3BMB2RI9ZP+FF88lw+/btzcEz1atXN/MsjKdkzxzQohC4tj8R2YZnco850gNxgr6afc6oaBoFOmp09dKlSyPeGdoxa1iQT5DthCLDz57+aNCgQcQ6ap7Kl1OxUS+aOKhduzadi1JD5jWhSXdOmwfpIQTESW6nS5Yswb7Sxsnly5ej8RADrZFyA5d00AlQJ9IhLnRhGl23vfvuu/Es85Qje+PoOhzhmDx5sq15bcSMXeTgkCmECNhBDgYGTIrkNzw7ZA0weazYmFtz586dm8wBvNmE559/XovA2LiY7Bhe06dP10JKoUKFHnvssV9++QWGoxRsr8cff1y0H+Pg9ttvP/HEE7t27Xr//fdfeOGFZv+tgEkBExAl4EFsyjJlykAJoA2a94HAn3HGGboBTsXbNAGETA4bNqxSpUriJ3CJeP4UcE4M05jOIHyiZ8+efBcNf9ttt2FYY+DWrVuX0sWrCiweTH87pVu3br7ImcIrr7wiPyAVzXA8cqKzqSB4MEAIOZ8rXbo0KVQU7DqasZwY8U73gWWRt+QNWYhutWrVLr/88gkTJtA0tWrVMjtZMOkor/h/xDuAUa4TUKnTTz/9+uuvj3lmDFw9V65c9iVzKE4y0YzgkLb3O4yocuXKNs+HT2pbSsSLj4olilQoLpRS5DqBjLVu3dp4eVx66aX28i/Zk1MVLIj7qVLJBkUbPHgwn3vuuee0XMlt0NTwNkL8FJ0ub968vXv3DjmHNpqxS5DWpKWSLEs8qY4H6JB2wke8rSK+6DghvWzDhg0K+Cc6xHu+/vrrHj16GOnCiIfamajRV1xxhaiXuCiPID+89oILLqDyjaNQSP2EFK1Lly6Uonv37jNnzrzjjjsuuugi02dPO+00iC4tNW3atBYtWvBFSciUKVO0fB3xjucxTjRwZigueeDrfIL/qWdd4h/tfRCXhltSIr0kd+7c/fr1s8/aEbZu3aoV3YgXWYAehJT27dtX3jQ8S32i0Pr3768URJp6o63lQBHxNpZLGilsu3bt5O6XL18+XsLQSan5rsmhg40ffvjB9jP96KOPTANR51jdtu+q8XVCPNBm5hJK1V5yz244LuqQYiDrr732GvoaEWcMi7fX1HFRh6whSQE7yIGxtXDhwpzOxeEPbaMNHpKGCdipU6d46+0HP7SeHBI5bOfOndwg6zMYyzrq2SvYu0EjMklgaIYcLfjTTz/JsI54O3UTvs2XQzIfctgmBii9PgvuG9jQr7/+OoNOFkotNxz6LObagbtuwU/sUzoFSo3N/fY/z+uKieAcQczYgUliz549K1eujOld8vPPP/viYCWJLLeRsH///i+++CILpnBmpRryg1TE2xGWsJdlCsZH93//+5/xKEkeMYumn7Tgp59+aha07Us//vgjAp+86xC54lWKIHhQQWXUMl16zn8+pEHXo/PKBTUo3iG+q9y/fft2ul6at0k6LuqQYuiEcSEkvLucN+xtdQ4OySBJATvIcRAO9ocl0DC5c+fOnz9/+/btR4wYMWnSJOTnxhtvbNmy5SHt4Z/jwNY577zzfHGSbcBGtIwWSSLY+BGF+fPn169fP+j8BiFv1qyZi5RxuCJm7CIHB4eo46IOKcfXX3997rnnVqhQYcCAATGH1TVr1nTu3Llw4cLHHnvsGWecMXDgwJjT9g4OMZFQwBwcbCxduvTaa6+tUqVKiRIlzjrrLIioz6nVIWvYtWvX5ZdfHoxXZ7Bjx47WrVsrilWLFi0OZO3usAHDX9OmTYML8lu3bm3VqpUbCg9jOC7q4BAPjos6ODg4ODg4ZBq7d+++++67wxnUF1988dBDD11wwQVly5a96qqrevfu7QuQe+Tgq6++6tevX8xwICSmPGicw0EFnURidho7ODgYOC7q4ODg4ODgkA7s3bs3Z4/ScXBIM3755ZdevXodd9xxxx57bPXq1fv37x/iTeDgcATCcVEHBwcHBwcHBwcHBweHdMNxUQcHBwcHBwcHBwcHB4d0w3FRBwcHBwcHBwcHBwcHh3TDcVEHBwcHBwcHBwcHBweHdMNxUQcHBwcHBwcHBwcHB4d0w3HRIx0bNmx48cUXczoX/w+///77K6+8koYQc1988cW8efNiXvr111//52HPnj3Bq3v37v2fhX379vlSYmK/h2B6muNJ/vjjjxMmTAi5gSw9/fTT33zzjZ2YZQmhdMEix7yTdvfd9ueff2bhi4cEPvvsMyr5mWee+frrr3M6Lw7/16PROQh5TmfEwcHBwcHhSITjokcuJk2aVKtWrUgkcsYZZ+R0Xv6Pt/Ts2bNAgQLk5+23386+D7300ksnnXQSX7nsssti3jBgwICKFStyw1FHHfXGG2/4rs6aNeuKK67gaq5cuTp37rx8+fKZM2c2b9484uFf//pXjRo1TvJQrVq1UqVKKX3r1q3wqwcffLB06dJKKVq0KHcef/zx/L388ssnTpyYrYfLbdmypU2bNpSIT4fcBkfihrZt2+rnAUrId99917t375IlS6rIdevWHTx4cEyS+frrr1911VW6LW/evNTJcccdV7ly5aZNmz7xxBO7d+/OwtcPTvTp02fIkCFvvvkmAoC0OAqUg9i4cWOXLl3y5cuH1EFHczo7Dg4ODg4ORyIcFz2i8eGHHx4kXFSAH2Y3FwXz5s0L4aLg+++/L168OPeUKFFi8+bNvqvQZmjSNddcY1L2798Pq+R+mIbv5g8++KBgwYJmpXfGjBliXOa1y5Ytq127NimNGjXK1mVSXg7/CeeiX375JcR44cKFJuXAJUT8Fvzwww/hd1aoUIHb7r77bv2Ep1199dWkVKxYMbuXytNzyvycOXOOOuoorbcvWrSocePGP//8cxq+m3Kkp7rS85VLL700p7joH3/88cwzz3z22Wfp//ShhV9++eWFF1749ttvTcrKlSvHjRu3b9++HMxVzoIaeP3113Pq6z/99NOkSZN+++23nMrAYYyvvvpq2rRpyd8f7B0hoOHmzp07ePDg+fPn7927N6t5TICXX375tddes1Poqm+++SbmkElx2s/BhuOiRzQwhQ8qLtq+ffs0cNFPPvkknIuCk046KU+ePNz2n//8B6XpuwphGzJkiJ1y+umnc/PDDz8cfFXnzp3N8te7774rYmZ7q27duvXoo48mcfLkyVksUnL497//Hc5FgzhwCWHk4w1UZsI769Wrx50PPvigSYGNnHnmmSReccUVWc5AQlDGHj16ZN/7DZo1a3biiSem4UPZimXLlo0ZMyYNH+rYsWMavnL77bfnFBedOXMmnz7ttNPS/+lDBe+9916LFi1y585NRdmG7Mknn0wKJm8O5i2n8Nxzz1WuXJniX3vtten/OqNnkyZN5GKTcHrRIVOYPXu2HJEwP5K5P17viIePP/6YtqMFO3XqxCNNmzY94CzHwI4dO+RWBu/l56ZNm2677Ta5vNkGktN+DjZSz0Uxuz/6J3zbz8DatWt1yZ5X++6771asWPHf//6Xv0nO8TgcIBwXjQcGgxEjRmjE7dKli+/qDTfc4Nt4SR3G46Lbt2///fff9T+DR5CLRjNMK1hrVsqTNHKEi2Lly3s54Z1nn322j4uChx56iMT8+fPv378/y3kIAa+FIjKiZ8fLfShTpsyhzkV//PHHsmXL0jWy+0NDhgwpVqxYdn8lmqNc9Pvvv0fwJk6cmP5PH0Kgh8pjwra2n3nmmZYtW+YsF0rPun3MbzH65BQXjXorWvJsz1T952B1HULQbHWSXDQap3fEBEZIyZIlNYdO/Vx//fWDBw8+0OzGwS233NK9e3c7pUOHDj4DyWk/Bxup56JLlix5+5/44osv7BvQX+aSscghn0qhK+qfNASwOTywdOnSL7/8MurFRGGEpv59N+zbt2/+/PlPPfXUnDlzduzYYV+KyTQ2b978/PPPz5o1i9fCo8K/Tgu+8847o0ePXrBggabBfO9/9dVX+Wf37t18/bnnnsOWDXmb4aJ///33Rx99NHbsWOQheNuyZcvGjRs3ZcqU4HY7KmHjxo0UmSK89dZbJh3lq/UcXpgkF0VuUZ2ijr4VyxtvvPHZZ5+1U+JxUZ+nSjwuCksh8Y477gjJkg1GoA8yQLlIWb9+vUmhgLpt9erV/Fy+fLl+Gi7622+/vfHGG0jL2rVrfW+mEe16i8dFv/vuu5kzZ2IS8YnwrB4gFx01apQmWUOiGcUTQoRBFbJt27aoJ4Sminbt2hX1pII65/3nn38+iStWrDClpstEPepFMV944YWg1UUT0NeQKJrYt6OVSwsXLsRi4ylkGEFSQxQoUKBEiRLKgPqsQNH49Pjx4+l0wZk7GmvRokX8s2bNGsTe5IR3rly5kn8oHX2Be0wVbdmyBfmfPXu2z4mRfL700kt0QyRk69at8eoz6nl0IyG0LxKL0aBJQ+q2QYMGVNddd91FERA53cwNEkLyMG3aNJSMymgE7/PPP1dKUFp4lnzSdu+//75JnD59eu7cuY899lg99euvv5qG4/+oN16YFHuSIl73p7apItpC+bSRg1zUIUlccMEFSa78pA179+5Nz7q90LVr119++cX8pBfnIBeNZgwlyXPRdFZXmpsmtfj6668zxUWjSfeOqVOnchuSc2AZzCI0pxxzst7BIZpyLoptB5HArvrBgm12Y+LQZzA7bC5K4uLFi/mpTXSYufz/3//+9zCOpZkSPPnkk5oSw/CCxfG/HCGGDh1q7qEt4DnDhg379NNPb7nllmLFisFdzdUg08DsrlevHpXP/RjozZs3D8kAeq1GjRoYrHCAdu3aHXPMMTBeXcL6bNmyJQwErcrbKlasqKyWK1cuSFkNxEWx/s8888xKlSoVKlSIn/369TM3wA3q169/ww03rFq1Cvv16KOP5m/U49uU8T//+Q/3UwRp51y5ciFLUY9dn3766ffffz+MZeDAgeecc06SXJR/WrRowc358uXji+ZqklwUwW7YsKGdEpOL0iJKFP9JBtjfUu5AdBcrX1yOnJis0vpFihTp1auXfsqA+PDDDxGJ6tWrU3t58uQxu0P5+pVXXkmTUXvmQzG5KIJHS8ESO3fuzNWbb745pKseIBelqknkUrynQoQQWnLWWWfx+GOPPcbPPXv2wK8UmEpbrai0m266iZ/UBt999NFHaQtVAkWeM2cOb5P7NNVoL9fzZgRj0KBBTzzxROXKlUuXLq1uhbwhZuXLl+cRiKJCVfFyaD/v51W88EEPxiYgD7Vr1+7fvz/vR9RpEexO7Sn9+OOPO3XqVLhw4Vq1apFhOY136dKFwtasWZP/yTB54P0KxwVR5EEqgZRq1aqRcvnll5s8r127lnQ6F8QMBk7nilelGHNUOMK8YcMGvkW2yUnU22h98cUX89rGjRtThBkzZlBF9CNugNH16dNHAgnXnTRpEv9QWL0Q1nrffffJ4918BRkePHhwkyZNXvSQP39+8r9r1y66BvVAE9DpVFfiulBTSW/U8zXAtFLTkNuQ7k8fpMYQA8aduXPnli1b9rrrrrPpq+OiBz8OQi7aoUMHemV6vjVx4kSKb+8tP+S4aDqrK53fSjmyj4vefffdjoseIWAM/SgAs9dsx44dckFlMN20aZM9GnLPmjVr3veAZZJ9O4qDSDEX3b17NxaVmS8PAhuOG7AtbC4KweB/eIJit1A1mOykJFyUc5AljWEKmY966yHYfxhthhug1Ixb4K+//po3b16bHQWZRvHixc0aIM0UQtjgMD4NKNpg9pJt27aNnwULFrz11lvlpCqzT8QgJsRFMc3FpngDZcFI1WJI1PP94AazHAqrpLy//fbbX3/9xc0iHhdddBHdafr06VdffTVdC+sc6mUTWuho8lwUkZZZD4cx1kA8Ltq6devnMjB8+HBMdp6yb/NxUf5i6ytOkmGMSYIiQ+x5kGZSyvLly/kJlTL30KHgRab2ZEBQLVqdhsTy89xzz9VVEqFMpIRzUQx6e/dmq1atuMHQvyAOhIsuWrQod+7ckDGzwuZDQiGErflETl3GhP3QIrnx0UX5wq8ktwyfkBnaqHv37hEvkJVqUrtYzeIzwsZVSA5CjrDB9JBJUrp167Z161a4Yu/evXUn6ccdd5ydf0YFWK49QiM5PNumTRv+h5hpU80JJ5zAezBTyDwpXILFieWa1T+EjRS6gNgaWhSaR4oJDkEZb7jhBv3PVe6M1xAjRoyoUKGC+UnxjbcF3Jt3Gh/dnTt3amH5lFNOmT17NowR6fr8888RvAIFChguGvVYuo+Ljhw5sl69ekZTwRi5gTrXTzq+z0dXBVTphKpVq4qLhnR/WC6JCLYeEWG2vS1ylosiMD7XCWRMRyhRM5gLY8eOpTjBB6EBs2bNolwIf3BDewiWLl3KOxFyBouYN3zzzTfwefRSMKwIlbxgwYKoFy7l5ZdfnjRpklE+NlauXIl6nDFjRvATP/30EwM9/6Dhx40bZx5HIFXY559/Pmg/xLS2yZ7tcoWK+CAWbNcA+emMHj2a4TI4fbZ27VrGPox1unDMcgnINrqa/FSuXFmfsC22b7/9lppB//CJmKeCxQSqQ84+9G5sJPsS+UF58jmUId+SUWRzUXQIT9EWMT0dQtriq6++0jg7f/78qVOnhtudNBC2KTnk0+Q2yEXjtWBIdVE/9LtRo0ZRY0Fjj6/QWGSemqQ5zCgmxGzKkG9RS3Qr8kaFZG0LGB1H5aKeeQ/d1my9ITPz5s0jqzGbIKFI0H8x/SkLXSMeFw3plQm5KE3P1csvv1zTl5lqBTqsdCM6Futl/PjxiI0u0eJkBpEIHjdAQ7z55ptyPhJictGg9ot6eg/9LIcj2xdASLKTHuHQep4PEldEVD9FsoBxjqPmEQxxMfoy//DTCHl2I8VcVCQTAYV207vo9rY4whkoISXnH5uL0lVUbHMn4wop7vy9hJATqc0EoJqkmPEM469Ro0bmKtSodOnS5qePaaB3+GkM1qi3LSfmd1FDGII+jUk7HnXUUdjWptEZREuWLGlu0F6Idu3axSuOuKgdx1UHqBj9e8899/BCs7Iq4mHcHSG9/ESr2u9ECR599NG2b7A4W5JcNOodRgoz4ZFmzZppDikeF8UaviUDVGOlSpXicdGTTz4ZJknGMLjvu+8+rTtlFv379+dVw4YNMyk0Sr58+YwGZzy4+eabzVUZELZxRmPZFj99M5yLoq3gRQyKf2ZAc/Zws3iZzCwXhRsj1XfddZeGWOiWcZ31IRkhhDX5uKimM+Jx0WhG6AXfa9W+Tz/9dNRzG6b5/rSgNX+zrK3dv0EKEeSiiiHhW14QxUJVRj2yx/+lSpXy7YASxaI7mBTEgJQHHnjApIivmqkl6GLNmjWNSYcNEW8L7m233UZ7GYPy008/Nc4UPi4azQhB0bJlS99LkCubi1JGm4tu2rQpf/789hm/9GJa3Cw+B7moPBRsLqrVYGNUxez+c+fOJRuGsYvqU3ZzQ05xUQy4Nm3akDczV0jvu+aaa+i/CDC1Ubt2bSQhtwd4vv0s1KJGjRrYjvRE9HmhQoXoO5deeqkvoJoP9IhLLrkE+cfUQC1Q6ipVqsDweVBO7MgYEtW5c2cGlI4dO0pXyz0bnUzHzJUrF21E3ylfvrz8C9DGxjaNegYABAmFNnLkSEaiPHnyIDC6RG6vuuqqvHnz8rlp06ZpK76ikVNwStqzZ0/0PJ9GKz7++ON2zm1rG00+cOBAdTF7eCpQoABFQ+Yf86BgcrVq1TJEhaZHShHdPn36oM/r1Klj7wMaMGDAxRdfDCFEIZxzzjkXXXRRvGqkX0tm6Mtat1f/xbBGAnkQqaZdGjRocPzxxycTXYnmoDgUGeFHpdP12rZtqwFLPgLyCKBp+Jbk33DRoUOHFi1alHaMeL4bNlGJ1xbof1LkbE9FSR8CaGS8HKKFaAJGNPgw+gSLQlkyiiukBeNV16xZsxAe3gYf7tq1a+HChW3HE9Q4haKfIl3QErqAvfkoXlPG+9aCBQtQfbTLhg0b+FYygfQMIIp8RUMnue3du3e1atXklsI/qFO+QneoW7cuIu3rDsmIBEYyJR00aBAKn4Hv/PPP940+Ib1SSMhFMQPI5GmnnSZFnWQrYK01b96cuqJlP/roo3r16lHPancY6erVq/mJjsIeIMUE/8NYogl0rIC9hcrHRYPaT8A2wzBDLJEfNAwDH5k3V5PvpEc4GD7kZ2o7qP7tQRRU/UWbm/gpi1FEjI6GikBtioXZ8pytSDEX1bKnPGxVSGBWk7BpFi9eTDl9XBTOyf/20gfWJynu8L2EEBeViSzoWBSzaGOOCcFigz4V9mBuDq56aYyHAQbPMrGBgHJb0INXdMJYfgyrtvGdcKNmMHaR2Kam0gUZ5dqSh3kd8ZwhdUnjkM8LBY3GUGGnJL9f1PzEFtSAjRkUTdpHlx6OvrZTDBfF1Jg+fXrE2wmp3YBZALoD6xCrSz9///13nWjKUKGU1q1b20QuGLtIBqX5SY8L56JaA8QqvfSfCFIRg8xy0aZNm0KrYBQM3rZfdBDJCGEWuKhYU9AtOZIRxYrCMtZeGoARPMVCDJ7XEuSiZcqUCfrK3n///YZVqv6DLmdBLopARv65qqzTdAw/EVWjywS3lPsgelm8ePGJEyf6+GqQi8ospuv5XhLORbEyI965u/HykAUuGrP7R61AJthPegmtaa7mFBdFA6jqbGsMughbE0nT3n6UAz9hnuYe+iC9yUw6oBu5AUaKJAc3G9u47rrreLlZmTnvvPOk0HhQK6uYeuZEpainPezZDQx6ftIo9957r+azJKiYsLoBUcE6VICAqGfEly1blhtkTcJnEM6It2aFFGEq3HTTTZAKLmlB20zAo17gHvYSjW1t09ywrPr16/u4qL1FEL2Rx4NRIBjWfMUIs7oG3EA/tRhldix/9913kPaQmtT9vl6JIoKiGGHDyFG5wk9eQZ4ZAmbMmGFS5JfBs2bslt4O+uii7eEw+iKUlRSaWDeEtAX3U0A529MfGUapWNo63nwobU1HY2g2KRhyGsUMFw1vwWB17d69Gxk2rhnIZP78+VFN5oYOHTrYc+jdu3c3RkUyTelrmnLlymngVs2g2zMbCY+KjXgeW4by6bwx8sw4pRSFNrjzzjvNUwlFggGXgtu2xPDhw31cNLxXRpP20ZUpJZ8LIWEraITNly8fDFzs9/PPPxfVx0QUgSEd+aSvSRhI5CntrgrhojG1HyoCWq59VeZb2Kual8lsJz2SQQ/Fig4eefXrr7+KeRlXGnq9oVqiXWYJUNQ0GGEhm5BiLooUolvXr1+PGlVADgrz0UcfRT0543/NvybkojziuGgySMhFo163R3OhIhFQuAdGnrkU5KKYa5rTwo4cPHhwvBMvRTBs0iJce+21EWtpIlVc1E5BrsaOHYvl8dprr91www12YYPGKIYLbI0hxP5KFrho1FuSjXib0Bi8k49dZJYFBJ+PLmaczLssuwCgjiMZ68ZQ0E6dOjFyaGBmbLBdIqOp4KKMu/yUQ3iSOMD9ognfHC6EqeKiWHWRDP9niMGFF14YkrEkuSgywG1HH320zzCSp7To/YFzUSOTWAmy4MH1118ffrSpuhLgEWwCk54qLtqtWzd+hmwdTyEXjXqMjj4LAUZ1cI/dK3PQRxfm6bPGAD9JtKNhFSlSBLVjrAcxurlz55obtD85fEsLj2MvmnmraMYuRBMknL6PKELezGr/lClTxHLNDfy038DNEWsvNy8sUaKE7S+gZf+2bdvqBtHmU0891Zc3WFP16tXNAqa86O1YVkFrW57hhovSg2RmRD3upCUgjHhztUKFClj5JmOYWRJv+dSI8Bv/8KjXd0IqM0h4dHIVn7Bvmz9/fsTz3g/ZTk99Iuc+DaCDrMxCZTwuas8Abtq0yc5Swrbo27dvJLloeXK48LmGykgwXDS8BYPVRVnQhPb0QdWqVRE/8xOh4hNGpNesWSM/kYRNGfwW8kAK3Ntkb8KECZn1PFSns/WGekerVq1MCnZvxNrzkoxIwOhKlSpli8e6detsLpqwV0YPgIsmbAXAI7bFCCpVqkSiPShcc801PiONPh7ORaOxtF+HDh1Q8rbQasFfbiyZ7aRHMpYuXfruu+8iS0uWLIFM0jVkyVPncsE1Ike/JgVqEPWsU/43cwE7duzQzdl0hIEP2Xu+qFx2USIUBhuCf770sHbtWhNiFwtJQXSDPrrhs7wO0SS4KB0YxWec8hNy0ag3a8CIJf3epEmTmOMorRPxfFR86TIRtKUtmg1cdOPGjZizffr0Mb6y4Vx08+bNPsWdTDaisbgonblRo0YRb72IoTdJLuqDj4tiIMKTI94pW1k7N1xLWPKQwayhK2lgoKKGDBkycuRI++YD56LQXX76yh6O7OOiyQhhqrio3Ms1P12mTBlqMiRjSXJRjCRF3/Hte9HCyK233hpNKReNevM4GOg6jwECEx5Kd9asWeJF3G92BKWKi7Zr185HLH1IFRfds2cPWgVLVM7J8tE9SLioJiNiclE7tplvb54m4GyPyubNm0cSBZKRJjzhhBNMyscff0wK3UE/1bVR+L7V/qZNmyozUg52v/DtbbvuuuugzUF/gW7duukGaT9SgtmTqcRfOqYMWTuQW9DavuuuuyL/XBc1EMuqW7euWY/S8g6yF8yb8fvVSg7WsDHFQhAkPPJ5NuuQAoNU0aJFSY8XbJyOz1Wf70w0g/5dddVV+hmPi9qxiyRLZqRL2BbiBiGxGwxq1qyZJ08enz0a3C8a0oIx1ypN69BDIYeqKEMRe/fuLc5mVh2FhE0Z81uag2N8ydpemGgsLqpxrXXr1iZFW+LNeJRQJJA6/vFNa/r6VMJeGT0ALhpN1ArRWFxUpo5tHWnqYfr06b57wrloUPsxsEJ0gy0rXZfZTnrEgj5o9oiac0nkPIjJoZ+qQOxP7QvVRJ4umbM2FMcHpCeIbIq5qCYzjNrS8S0KSqRNsUFgD23fvl21Zt6jQLtO4BIinItStwUKFFAcFCGci6KP1q1bp/+xGzT3afvrG2gbm28fZjRjhsy8JOVcFM6GOWUELCEXRfDIw1FHHWUfZpM1LqpSawwO8rFwLjpw4EC9LRhHF9JYuHDhiDVjnSmgXEqWLElLMebJjUrThxhk1JWPDh04FxX9C/rGYCLE29UZzkWpB+Pjl1kumowQpoqLKiC+9l6ee+65/G/HoxaM2ZS8j65c4n1ESGt3Cr+UQi5qusk333yjqu7Tp080Fsyd8DdZVOecc45SUsVFZZqYXUYGxqJKFRdV3CmjkQ4DLirxsM+ph8wEZ2R8wOjUwVGmn2qp31iQmsEJIbQJuSgMJDz+ZwgXZeh5/PHHMWoXLFig6Ny2a2vyXBTRRSHkzZvX1t6a3PFZ4T7wXUWhL1iwIOoi/IDKIOER2/ERp6g3P0i67YJr44033oj80wFb0JJa9erV9TN5LmpkKWFbJMlFqQeIaKlSpXzpQS4a0oIx+WHUcwJEA2iXqYlDpkv8oxmWiLfSaFbhEjZlzG+RqBW2XLlydezYMdwlJCaS56ImQkRCkdD85tVXXx3Mv2m7hL0yemBcNBraCtHMcFH529v3ZIqLapnUTI3FRKY66RELmo9REj0v5xrRKyAvJLqSSNnHH39swhehNjGq9b8RNu4/hLmoymbWM5FX43xLjWzLwKZNm1RIDHFUGOxcP6UjFIwXJB+G7ohFOBeVO4fNRTGF6cbmp49poEzvvfdec1XEww6NY0NDhQlYKmASNW7c2PxMLRf99ttvpbwMF9XeCeOdFdMY1bYoO46uzlBp1qxZvGxEvbE25qIN39KGLh8XlVdYTC6KHQxX1LSxvNQi//TBe/nll5Xoc+jdvHlzPIJnQ2YZn5AbFZVTtmxZVLbZO2QX6gC5KD8VxsmOEIPOuuqqq4KbE+zSxeOijLVm8VaeafEIUkwkFEIdCq81RkHhBI2ngHbANmnSxNwQk4sih6VLl9YgrVislStXtm2aiRMnmm268bho/vz5fVx06NChvh4a9YZ2btNunBRy0Q4dOphL2hpkx0O20a1bN1s+sQWLFCmi/7Unyj4kPR4XRQix/IyX3cqVKyPeapV+Kn5Yvnz5GDLMI2+++aYRhhIlSpBD+4VaSjU+FwyQCkBtHApidn95lBkuqjqxQ+McclyUgstvBXWBQKIbS5YsaXRgCBYvXgy9r1mzJt38119/hc0i1ebq9ddfzztD9hIn5KLly5dH7YQE9Y3HRfkozaTTuaKBSNfRpLkoKkgRBHyhj3TC0KBBg+JlTMAsYVCQKm7UqFFIQYKER3slgrGjlC7/0iA0Etkjsp1+/vnn62cWuGjCtkiSiyqQ21FHHeWz+30yGd6CMfkh2pLcmp1ZQRbEQEb7qo8z5mqBMWFTxuO9aDwYl/xQUE2Z3RSTBS6aUCS04cX49Nr5N30qYa+MHhgXTdgKaeOisIaIFwU9vBTJd1IHA/TJ2xnxihg+5JervaCrVq3iH8VZ1MmaxktLS4nxdFfKkWIuKudbDG4sD+35tMtm4NsvGs3Ya8tYRTWJ0JqANA4h0Kl99oiiwzOlvHRoB0MdLQKz6t69Ozau1JY0l/q/mZdFmZYqVcpEYaUhcufOHYwhLqA0ixYtiuY1AxJqDlvHhN9ETfDyQoUKmU2n2Jrh6kZRc21rUinaHIV9rOiLGMSowkcffVTLSiNGjJAPoaZjoR/2O6kKjaaYuRRt69atouuUFP4QDBoe9Tohg5aP4RjI6Le5KOO0KpYatu9EzqkTLpljHrUsE/nndotohmlFbRuXHowAnSfpI6hBaIu/zaZEloJKRB44xqZhsKe9bGIshmD7jPkkJJrhAkdWaRoagjGGAcxmFD5oZRLYAdkwhaHZGpUNT1B0DUbf8PLaSCiECrMBlXrrrbdQKdSz5ia6du2qQw527dqFbMB8qHBUM/eIi9JrTDDqTz75hJ9mhhvuzQu5B/MLNjh27FgsEmrDmGuag/edzYAwyKiyZxn5n9qGqBtrQ+vkZiFFByNRM76Ca7OfzbHFEm+77TaTgkVOipldql69urFXqH86Zrz9NtgWdC7zE1vHmFyywC688EJ697Rp03iPVoyDwbG1jNmxY0faAgKJJUSfomjvv/++DAgF/0DIr7vuOiy2G264oWHDhmZGQ9YMigulpMiTEiSqC42EbPNFxFI9USIds/vDfiOeWxfZmDx5MjmPeOSfN8hrV9ZecPkiDcgaF416M9/0HWxrmnv48OHJr/NMnz6dduGp3r1721N+US9Eik+ihJ07dyqweUIuqro1kwUGtLjMoJhclHLRhevXr29SssxFpfcaNGhghzmgJrGxIl6YGV/4AxQgMhz13DpMHVJYKfM5c+YE6u8fBbcJT8+ePSOWV62BFsHiNRASKN3oc+LVuqjZzJkFLpqwLZL30ZVjpM+71ZbJhC0YrC5ZAuawq2iABZm5FfSzeqi2GSdsypj7RbUdLurJsBRCMhtlbWSBiyYUCcoY8bb82ITK16cS9sroAXDRhK0QTSMXlQsbY0TQHRKtRftmtpMesVCwHnvyCONfK38mRRFko16AmLczguVi//C/OfwJ2+NtL6xuerKdYi5K+Q3nFqWOGY41yEV5ECvQPEgvjbfM4mBA51dAbdQfZtbvv/+OxhRbO//885cuXYpQ6oxBzSEhZBqtsbxhHYxnGrEi3kY49DVagEsMKuPHjx89evTZZ59tDoSICRoXYlmtWjVe261bt6ZNmxo5Ru61yBnxwmN8+eWXjCI6jB5zfNCgQb51f34OHDgwf/78kYyzChmn+/Xrp0VI1LdC6fKg3om5zwtRSbly5aLICu+uUbNcuXJDhw61/TYZFFVR3MzLGenz5cvHKDJv3rygmwfv0YGixxxzzO233x5TgFG+hovSChoMBIYWmqNy5crUpGZhIx5bhvTCWxTnNuL5X/EhI+QUX26TcDyMckZ38i+iGNxNFMQ555xjM08qH5Zu30C7yNkSQIzhgYwTGpw0XqKMKIjciqglCAy2e1BCot6oT7toz6FMhHihjL799lvIuWhbxHOmZfxg7KFmTHWJZfEhLFSlQE46depk7xYLR4gQCg888IDejAzwWoZD/mF0N2vOiurBQKgjXsVFaUTM/WbNmtEcp512mo5VNGAk1kq4HqRyNH6vXbtWb4t4NrHhRRRQ67ERL+KIWUGNerzilltuKV26NFm67777qHCzW2HRokVGtMiGMT6ef/55zcKULFly5MiRCA9tJzMCoxDhR8FCVrXoTYXLpZZOVLNmTaxP2GPz5s2xxuLFJKDD0r8w9zFc4C1UryFCmE36NM1KocaMGYOoR7wVTurfNqkRMK1JRjymiqqnQ8E2IcAaBXkVH9KEiwpoW9vy6QCNGzfW/eg3Bf+MeL6+vJ8GokT9+/en2uN1fypNK/lkmNyahX0+h+QgyXL6wngNOdMim5A1LkptoNWzEEwBvRdigmvOjr5vTwWSjSuvvFKVmZCLSjmjAM0hW1EvoIsObonG4aKzZs2KeCGyTIp87O2NdslwUWwGlCetac95IRgoakqhaTjfXCFsQdFZ4RX0KZMuG912pfFh69atGoNMyueff44kowrscFzofGTejg0ThJa47UCpUW8MYuAz1agupriPQkIumrAtkueiaNRIYLJJ+3fk9ZCwBYPVpdBlNgvSAG1c4XyuIgxwDB8M1gmbMvgtHkEn2z8xM8yaM70J0yKhC14WuGhCkUDzayi0p890rJpxz07YK6NJc1HtM7cn3RK2QjSNXDTqRcCKeBGkbTL88ssvo+GjiTopoogdkp4oOwc5FP8WZSvjVhKujaAwAnjWJ598ohPvGIK1oVRLMuvWrTP+ulEvNJ1ZMk0DsiV2EaJMsemBmeWTiCAjLiTEiVSqQE2i3ezdkgxI8U61RlKRTh6BRSCy4YdfGyDrSG3WQu9kAQw29vjKT992wXjARhFLIasxl0OTB7WUhs3MdB+UiFlTDUHQ9cA2XLID8vQID36TToQLIfIPTZJqRi/51As/GVnN4rDx0SUdSQsx+nkt/DzJbhIO8obS37lz54G/Kh5UOXSWjz/+OHwlTXeiximdj9hHPU5I0yezh4R7qHZDomKWjrfRcLZLsAFcMXgq/UYPIS8Mgs5ONsxCCjbQQXJytWKfQqGNQPKPTvAz6oVsi2ObSTEtd8NhBg4cOGrUqEmTJs2ZM8c4AsQD7ylcuHDVqlWhPZjUsLhp06ahXmzSK4cRWFCrVq2efvpp3s/9ZuVBsY5IMfevWLGClAoVKugnA7ds2eOOO+7mm28eN27cnXfeWa1aNaOudSqMOUNC0E6QiLeIRxfgozq8ET5mFtYU4M2OXNChQ4eI5QBppkjspX4qE2tbJ2Zpn3PE24DAU8OHD4feGAaImcsnzLwkLALrP+QwAwRbx8ByJx1E6/aif7bbM1Z++fLlw4cndAjmOI1u/I9QqlSg7WasCcExY8bQJTUHKldV2xdGssR7JEsJ26JXr15c1exbOOg7mlS95557EEvNEUOxRAixXBO2YLC6RO1Kly794YcfQqJuv/12zdJCX7VcT3PY53AikGYKI7wpg99CwgsWLGj0GB0BIm1IuM5ZPeWUU8K9PTX3YQdx1ZFs9sEziqsE/zcpCUWCNtVEHg1KPhm1te2I6kWS1eXDe2U0Vu+ICbm22mfRJ2wF0UWyZ1vymqm3w1zrwBs7iEC5cuUi1tZ00KNHj8g/N+AEtR/3aynlpJNOuv/++8eOHXvttdc2bNhQ41FIJ2X40JQirDi8Eo4EUF2KSLRkyRI6r/xMly9frhFQh7iQyCVu4H/TTAyUYq0fedC6oFhrGpC9cXQdHBwOBAyxIe6vDtmBmPtFHRxSi6lTp2odIOK5ENPNMc60whDxTg/CUCBFqxkRb5u9ogBAWuQE7kPLli3jHcElwCVk6tkoVqyYcdbFiOnUqZNZqYZRmKOPMT3NEj3vIWOLFy+WHR/xlvU03fnNN98ospeA+WvWRrAsFWsq4nmSm+Mio94imNLhk9jE2EPKJ7YyJpHCt0S8xfDx48fDpvr376/F7bJlyz755JNkW66MPHVZBuBvWk82uyFGjhwpVh/JcCgwGcDMxSK/5JJLJk+eTDrcxufpHYR2x2ANX3755Sbu6OzZs2EaVBQkpF27du3bt09m0hNmcs0115QpU4Zq4bU87gu+yk+xQSqQmp8xY0b16tUjngsJ3EbbuowswXw0gxOvLTDc+/btK6ebIkWKwK/Wrl0bnkNE0YhciRIlYJiQjbp160ILNWkS0oIxq4s8a+6AFEgm9FvrZjAK7dyuV68eZXzggQdefPHFW2655eKLL7bnW0OaMvgtLaWefvrp3DZlypTmzZt369bN9BQxPRBv6gHuPWzYML4S8XwuYINwJ96jncm5c+emMiGNWP/GtefWW281q0kJRWLcuHEKXkiG6XH0C9qaxkI/aH0ypFcGe0fMIkA27r33Xr2BLjN48GC5OIW3AhrJNCt6CQ5D15PjMaCBKBp5e/jhhzV9hoRQlnfffbdLly66h340bdo0JAT+rNXs448//vHHH0fgg9pPWUVydEJVxCPklM5MU4Z0UtpI7iS+EANHLGhZbf40fqZmmp5/dEyJ8OGHH9oTDTwoHqu9lukMH+u4qIPDQYohQ4b49nQ5pAGOizoczIA5dO7cecuWLVjP8+fPnzlz5qRJk7R53l5K8gEDGgrHDYqjOHfuXMxE+CFWpm8XwB9//LFq1aoDsUJ27dpl3MCSxMaNG20HBL4e9PU4cFAJ69atM6ftGcBY/vYA06PsSR4+CbWzHY4MbC+M5CEngnhL/du3b7e9gZJHFtoiHrZt24bsaRUrKB4JW9BXXdQP5bUdNCigtnBHM1wz4CErV66M6X0TrymD3+JOua5QhxCqYFWQT4hctvr4hIsEOVy/fr0yQO+LuZB+4L0yJsJbIaeApH322We+bhjeSSkIjR4eO/qIAhVCsyJ4QT9TftIL6A4xXdOpYR5ECNMTPtfAcVEHh4MUKXH+dMgstC+uXLlyOZ0RBwc/sMNKlCgRcw8P9DIkAtPdd9/dsmXLmJeydpqUg8PhgRUrVthutA6HKJ544omJEyfmdC4csgjHRR0cHBz+H1577bULLrjgWA/XX399vIMBHRxyBNrmZ5/FLezevbtTp07xlr/27t2bK1euRo0aBVdmXnnlFZ+Lo4PDkYP33nuvY8eOSa6EOxy0GDVqVDKBuBwOWjgu6uDg4ODgcAhg0aJFuXPnzp8/f/v27UeMGDFp0qShQ4feeOONLVu2tKNWBqGtg6eeemrfvn0nTJgwZswY/mnSpInvKE4HhyMK7hD7wwOuHQ91OC7q4ODg4OBwaGDp0qXXXnttlSpVSpQocdZZZ0FEdbpyOPbu3fvYY49xf6lSpSpVqtS8efMBAwbYp004ODg4ODjkCBwXdXBwcHBwcHBwcHBwcEg3HBd1cHBwcHBwcHBwcHBwSDccF3VwcHBwcHBwcHBwcHBINxwXdXBwcHBwcHBwcHBwcEg3HBd1cHBwcHBwcHBwcHBwSDccFz1s8e233z711FM///xzmr+7adOmKVOmHOBL1q9fP2HChBEjRnz66acpyRX4/fff//dPhMQB37dv3/8SIccPJQtW9cyZM996662cyk+S+PDDDydOnLh///40f3fv3r1jxoxZt25dmr8LkJbp06fv3LkzDd/KjupNsuq2bt363HPPpfC7QaRcrfGqqVOnuoiyDg4ODg4OOQLHRQ9b3HjjjZFIZMCAAWn7ImZo7dq1+eiJJ554IO958sn/j70zj/ep2v//xzxLqLhRxkrGBldFgzRQyVgoXSSVJJV0U+nRpJIGhCtF5kQDkuKWTBlSpiRcXBSiFK6SVPv3fHxev7O+y96fz/58zjmfc45hvf44j7PXXp+913qv93qv92sN7z3gwQcfXLx4cZUqVXja+++/n5Li/fvf/77pppsiaahcuXLFihUp6vnnn9+hQ4e5c+famXHo77rrrvz58yszOc9OQ4UKFQoUKEBi+/btU1KwDCCmqL/99ltSChUqBJHOqYIlg0qVKlHOBQsWZPN7ERrvbdSoUXa+dMuWLW3btpUiffPNN9nwxqwQb0LR8boGDRqQ5+STT07he4NIoVmbP39+8+bNc+fOzQPDP87p4ODg4ODgkEVwXPSYxaeffnr99dd/9dVX2flSvO1MctE5c+bwhM2bN/P/mjVrcH9TuDQK6tWrx/MbN26sy0OHDk2YMOGEE04gsU+fPr7MnTp1Ih3y6Uvfv38/t9q0aZPCgqUXQVH/9ddfnTt3fvTRR305qWP2Fs0PXwEGDx6M6JBhNr8Xrg73mDx5cla/Nwjxw+zhovHEmxk1SEZ0mgpJORf1FTu1Zu3PP/8sU6aM46LJY9++fRjMPXv2JJn/p59+Gj9+fI4sO+fgq7MNS5YsGT16dPbvMTmqsWLFipkzZ+Z0KRwcHP4Pjos6pBI4jpnkojfddFPu3LlTWCQfWrRoQQl5i504btw4EnPlygX7tdNhp6SfffbZwefs2rXrhhtuyLpyJkTyov7HP/7xxx9/ZEORYmLkyJGffPJJjrw6Zytu45JLLsk2LhoT2dMKKeeiq1evfvbZZ1P4wCAuuugix0WTwaZNm7B4+fLlQ1z//e9/E+afP39+s2bNcmTZOQdfnc047bTTqONnn32W0wU5OjB8+PAKFSogMYaGnC6Lg4PD/yH1XBTT/+Xh2LJliy/P2rVrdevXX3/13dq5cyfp+/btS3nBHLIBmeei1apVy1Iu2rJlyyAX/f7777UX97XXXrPTH3vssXhc1Ituv8y6ciZEkqL+17/+RbacWhpdvnx5wYIF//3vf2f/q3O24j7kLBfNtlZILRfdu3dv1apVH3744VQ9MCYcF00ef/3116mnnpokF/VydNn5OFnxHjhwYNu2bbNhj0kmkcI5wUw+iiHecVEHhyMNqeeiCxcu/PRw+DywH374wdz63//+Z9/as2fPggULSD+299WkFjt27JgYxerVq7dv327f2rp16+LFi4P5J02aNHLkyGXLljFg++7u27fvvffe86KRfmbNmjVixAhtl7XBr2bPnj1s2LC33nrLx8diEqRff/31/fffHzVqFIXZtm1bPHrw9ddfL1q0qHTp0nDRRVHYO/F46apVq0aPHj1hwoSYPv26detIx1ui/O+++26wakJMLrp27Vpx0fHjx9vp8bjod999h/RiPt/Gzz//PGPGjFdeeWXmzJmUB/XmRV6UxKqCNJlyrlixQikIwX4CzTF16tQhQ4Z88MEHvngtMUVN4ocffnjgwAFdvv3221rHoFvxcLrV0qVLF6XBvOvbb79VSriLuXHjRoQ/ZsyYoHsXs4nXrFlTrlw53j5o0CAebivSl19+ydPMJa02f/58ZaAMtPLcuXONz8ED33zzzcmTJwdjTaHh3IJ2kt8+JRusuJFncHcWhcdqDR8+fNq0abzLd5e6fPTRR7t376aQSI9sX3zxRYiUDKjO2LFj6Zi0e0wu+uOPP/JGHvj555/7dtmFdBmqPG/ePP6hs9McaHvQWtriDWmFkAIEEVN0aDVElyeg5/wfk4sitNdff51y7tq1y3eLTqQ+TmmxSDzEFANtv/zyy3lghw4dKLa9UT+mWaOBkNjQoUOxWkFvlUK+8cYbvIKO5rvluGi68Pe//z15LurlqHhdyx4hgCrfddddqXpaJmkk46Pjog4ORxpSzEVxAmCS+Go/WLAJJ/4KjsVnn33m46J4aUuWLDEc1XHRJAFROffcc3G/IDk33nhj1apVvaiQX331Vbm/vjEAL79WrVqYYxjFCSecULJkyUsvvfSaa66BvOGz8oQCBQqQuHLlyurVq/O0XLlyFStWzOZd0KdKlSo98cQTOJFPP/10/vz5YaTmbpAgbdq0ieeMGzcOd7Nfv37c9RFmA3gv3K9w4cLkefTRR/mfWugW/gSOxQMPPIBuDBgw4MQTT6TMog0wEMie3A584rZt24pVxtuRGJOLPv744yTyah8VicdFIT+4tjGfbwCROOOMMxA43YEyn3XWWdDsl19+2Yv6zffddx9PxrEzUu3atSsptJp5AjTmlFNOmTRpEtSCpjn11FMNd/UCooZYduvW7aSTTiKRTudFY7fSTLY86WWzZ8+mfUlp1aqV8dIgCYzNlHbDhg0x63Lw4MEePXqgS/j6bdq04ecPPvigoQ3xmhgKjegU5Im3o3WQn6eeeurMM88kUYcPefLDDz8ssoQS3nPPPdWqVeNpXF555ZWQTwpGfj3nwgsvtKcYevbsWbNmzTlz5tDWderUQXR79+6NV3F4VOvWrQsWLOhrTfoObxw8eDCSQcHy5MnDX0VIhn1R61KlSvEc6F/jxo2rVKmisFVoWkjTo5N33HHHVVddNX36dCrFP1pNsrmodJX38jo6EQ83Ri+ePGGeF198sRypgQMH8ivtQoT+YVS9KLf0iTdmKyQsgA/xRPf999/T77p3747o6BE8wcdFv/32W/SWl9JD69atW7RoUZRZtyDGikxGRdCl8uXL06m5vPnmm5Xhgw8+oI+T0qBBA57A80PMGrVo2LAhEkPgPKpy5crr16/XLVQCRaLXQ0fHjx9fokSJe++91/6tYyzpguOiDukFRsAe1zIDBiDaNDNPcFzU4ZgHLtCXAeBr6S7+Hk7p3Llzly5dunnz5uA0NClQgGz+4kCKuSjeG2zB+AFB4GaRASfGx0WR1GdROC6aLpQpUwavTv8fOHCgfv36XlST0DbcNZ/TtmLFirx5877wwgu6VGxMXD28NC1ZwJHwxXFMO3ToILf+9ddfF28xDzn//PNxx81lhQoVoFhmISLIRaEuLVq0MJc8Ch0IqRG+rG9r5c8//0wixMOkLFmyhIrA7uhdvBpPHU9UdcEpl+u8devWmM/3cVHc/V69epGCo/zOO+/4MouLQiTGpgHC3Lt37+LFi4dz0WHDhsGFvvvuO5Mikiwu6kWpo81FAdze5qJ79uyhjtAYXWIyuGtL0idq2ot+p3it4qLx5Nm/f39SfIddKR5UJ151oItPPvmkuVTEVPM5mZAmxgshp9kdioru2LEDFbLJkpfWKGgvFtCLTmlBO0nBmzSLkO3atSPlo48+0iVchUtzmBDmr6W/eBWHp7355pu+mYUFCxaQAoExKTQQKbfeeqsuKQkkipRLL71Ua9rwSdoFnQ9ZSIT1nXfeeWadliqLGBsuikDsmLSPPPIIdzt37hwuT6wr1Jqc9Hq4GUaSrtGxY0dSypYteyCKmOL1tULCAvgQU3TQdcgkRNSkTJs2zeaiyAfmrCVcLxpIplixYvny5TMLtpqOgXUrUPb+/fvFos2Ei3ZZmz268cwaXZKCmeMekFsyNGvWTJcwbS7F1QGWjUupmZDjjAXxYrKwGAx8wcMpyHnGjBledL8AVDy4S0VAOIhaRg9toTtwaSZuvv32W3j422+/bXZMGCA3hl2eTCvEmyXkgWPGjHnrrbcoXkwuSpvyfMxjcDIrGfGaXQAY9m3btvmWtc2KN0rru8XlJ598gugmTZoUNPgxX4089RP++o4IIUP8M52s3rlzZ7gTgjVYs2YNEn733Xffe+892xpoI8CUKVNsO+xloo22bNlCB6TM5A/uKsJC2kOqtsZQeF6HPIcPHx7cwhMucAHbYnbQKIVW1iW/snPyfPVZWh/p8XYjDWqnDlinTh391p5MjCcoL7rpgypPnDiRgRKbpkSEg+1Vdwb2RqEQDfSi4w6dCyVHVo6LOhzzoMt8GoBm2Onvupw/f77+kWNjgDUghXRIWXaWOcVcVCQTr5o+zwgH+bED7mEBsfXUk39i7tHVsqrjokkC6WFVmzdvbuw7w5W5ix33OW0PPfQQKYhXlxjoQoUKlShRwn5myZIlc+fObcYSnA9+csYZZ5gMOOX42eYSskQGRm5dBrnoueeeC181DTpr1ix7c2YQQe7UrVs3UnwTHGIvzz33nC7/+c9/cvn444+HPNn+IbWuVq2a3lWrVi2eE9MPExc98cQT70rDHXfcce2118LYQ7gozpN+Yidq6dVwUZw5HxdVXFzDRfFQaYv777/fZIBnQr/NZcw9uvLmw7kobXrCCScwqBuqjCLxnKAPZApGfWm1Q2nQYt0VV1yhDCFNHGRBABn6yBLVJMUW6RNPPEGKTYDxckh55plnzFsgeDiCusQ14e6dd94ZUnGdCrYJVY0aNYKbnE855RSbvUhhDKcC+FWkGA/JBxw17o4ePdpOvOCCCwwXxcqVL1+e6hh5Ll68mLsFCxaUUxgiT/E9pGqeTN/XAiNeXTzx+lohYQGCCIru+eefJ8Xeon/w4EGbi7722munn376IQtNmjQhQ9++fZXhlVde8TXxvffeSwo+qC59XFTwmTU8+yJFisCUTAaUmReZg9/0Ozq7ISrPPvssP7e3cuQgF8XMvvjiizQ3VApu0LRpU4pqpniWL19+++23Y0lQURqoaNGilPOyyy7zPcTeWTB16lSsJZZNKnHdddchjXbt2pGC6Qj+HA7MLWge7Is+iE1gjDDT5150hb9Lly5XX331Bx98ABPA2usQpuGi2jHBS3nIDTfckCtXLl8c74TiRbcZXyZMmMA/9G4y23u5UZJGjRpBM5APcqhataohGytXrqSbPPXUU/gbmIsCBQr4JhODr1ZMo5deegk1oJtjLU2wOirSsGFDCs9AQ02LFy9u1vBtIJBBgwZppgyap54F9EkwbQRA5cjDKMlDdOAlw22EhtApGKF4/scff8w/FFJeEwMEfUcGX2+x93HgfdFYvIJRg0aBdiYpcAOGA/KodrKidCItS/JM5TG7G4YMGdKzZ8/TTjsNBeayU6dOygCT1OQRtx6LQtoVT1ACIjr//POxV/iKrVq1QjLe4btd9Cit2yTUQPpO5cqVGXmRYa9evRRI33FRh2MYGEn8fDqsvUH1zyhEQTWnSZ+aM2cOl1p5+vnnnxl0cHXEwo5uLqplT0C3VyWBmb5atWrVggULsOaOi6YK+DGR6Hf/gkcocUZ9XPSWW26xXT1Qs2ZNCI/9K3FROyVy+L67v6Lwol47YzbuJhmMfxAkSKIZDAZmc2A4ghSiUqVKDDC++WAcBbJdfvnlumSkjwQiD8WEqEWbNm14IH4J/1OF4LysEG+P7iOPPBLCRfFR+JU9/AN8pnRxUc8K0rBnzx4Ge9rl1FNPNXdjclHtxgznol7arAQDsy7Hjh1rszgfhg0bhvyvCQB1UoaQJo7JReWdhHNRrU8iNJMifcbtCMoHs6MdzmaHZ8yKIxa7NfUNkgYNGvjKrEeZV0thsOAmQ3ggIiTpW3nz/USHk3GUgyLVFvEQeeKRBx0pqdbdd9+ty6B4fa2QsABB+EQH8Jt901je4baCLla6dOngK/r3768M4qJ2E6u7QUF1GZOL+syaZijsvetBGD1ZuHChNlAY3u7lKBeFlkOkTW/FUYCOGqrMuKnFf+SMe/3dd9/h7g8cODDmo6SlF198sQ7WUmUtYJJiVPH6668nhXFZl6h0xNpo4KXtmLBNAR2qbt26phPRZbTzwnBRWsduQc252LqXULzoib1HA5tsJg5GjBjBCGXmyODtEWuTTp06dWAm5ocwPeilvT7pe/X3338PczPeCBXnbo0aNTSTi5VDdc3PBwwYYE9wGGgbDnRRpgOeQydt3bo1HUcbAYyhgCvSuDBkU50MtBGsjEvTZbRNSR1EmyDkABgixzPPOeccUtBzzd7yZN/AESLwILRz3raiyNxwUXDPPfdEorPV6KoX5cMVK1a0xR4c1xIKqkyZMhBL/Y+vaJtoWXW7hOEaiGWgtIjRZJB5dFzU4RgGFgYaFfzO/P79+8WwzITjsmXLuFRv3blzp3anio4e3Vx048aNS5cuxQhi37FfX3zxhakSFof/tfrkuGiqgKjFBvPmzYunYm86CnLRwYMHR6ztqQwJDN4MfvYDE3JRLzrePPPMMzx5wYIFWhc1A0+QIKH9V155paZXr7vuupBhT/BRCGoEESLFt3sNNYtENyvqMr1cVEKA4+HxR6I7MGNGVIrHRRngQ6i1hmdfhgxwUS/KsmBfUF96FmOqLdjMcFHcMsb+4sWLS6qNGzf+/PPP41VHg3cw5LVBSBOnnIv6VptxaDp37oyDrp1X9jHghFxUziium6868sjbtm2ry/RyUR3ptLdn+36iioToT4g8Y3JRLRUa/zIhF01YgCB8omOQy5MnD33Hl822FWS21TuIlHDR7t27cxm+7Z/BaOzYsZ06dZo0aZK6oW0ocoqL0qwFCxY0EzrCihUrKAxmWQTst99+47JQoUIhvU9QD6KaJkXbuZ9//nmTMmjQIFJeeuklXVavXr18+fL2Q2hWHTjXkK0VfrNOK2hTgLhocMcE7Jq7TZo0MfkTihc2ValSJUMRUUvN2WvF2z44sHfv3quvvnrkyJG6hKLAk81dRbqy92H5Xo1xoOOYoiJbLbLJ9CFABhoT2gp3JeRrujG34QQ3AqgXmybIQBthoyjklClTdKnpA3s+Dutnc1Evjc0uXLjQpGi51Ug4nsBjgvHFZ0UZNWwuKkNttqt4aZNxpkjBcS1cUNrt1apVKzMvYO/28nHRhBqoQ/52jUTvHRd1OIaxePFi+OS6deuwA5jxDRs2aMYN8wi9mjNnjunRX331FSl2aEAvGp/lqOeiPmjL7ty5cxWCkn82RKHtyAqxq9VhwXHRDAAB4pkpikmtWrXMGBP03XE1cKzJyXB+8ODBMWPGMCb5nOaEXJRGZCAxLkJCLupFfUGGWMYwzfGHq7iPQqASihbj+/Knzk/iGOkyY1zUi7JKPEJSunbtGswc/k2XeGjdujW/MoGXhAxw0SFDhuAsmjWfFHJRcPvtt8vp2bVrV+3atUOq0759+0hgoc+HeE2cdVwUZ50qXHjhhbIV2qObLi6qw6I437666OipiXCTXi6qwEu+WLv2T0aMGBGJxuyJ+XMhnjxjctEZM2aQ2Lt3b10m5KLJFMAHn+i2b9/OJVTBl822FeXKlStVqlS8cNZeirio9nqEfK4GSnPxxReTX6uj2qN7JHBRzC/vfeKJJ3zp0h8RpOQ/kRXkOZpSMUtqgP5FCjzKi4olEmvHb5cuXQwr0GZvX2Rv+7xovB0THTt2NPkTitfsArBXaL20FW/fWSYbZocO4xpagan0zQH5Xq1NucHSSnnUs4oVK0a/SPjVkJjDTbyNAIZYpreNBFMYGJeMtn2uWylBLmqOGHiBcFPxBB4TSXJR+yPADz74oG3Mg+NaQkGZ3V7B1vdx0XAN1MkChmP7Ce68qMOxDcZcc0bUbLjVLBumUpc6YQQLwJ8P0s5jgYtqaspMaOnzLbBwhc8NnqYF9q4wx0XThd9++80wtFWrVmn6Ew9PKTHXkfbv33/FFVc88MAD99xzD0Np8IhgOBfFuDNaX3311eZuQi5qAiegDM2bN+cuzn1IpYIUQjPxvi2v+Gr2iJJhLupFYwtHovCxRy8RF4X2d+vWLZiuwd7smRTSy0U1ZJoDsV6quej69esZxXHgKNKLL74Ys4KChGC7RwK6p+m0kCbOOi4qj8d82yMDXHTPnj1qd18gFp2ENIVJLxeld0QO3wXq+wn2jf8vuOAC3w9//fXXadOmeaHyjMlFtSd84sSJukzIRRMWIAif6LDwhQoVilib8wXbVqjKQX93ypQpCqKQEi6qZRBzPs1g6dKl2qFEFytatKhRgyOHi2ptzeyTN5BF1XnjrOCiOoKuTQH2uqIg+ciV1wo/Nt/OYBMbaVq8c+ZCQvFqSFJPhEcZMqkV7/B9NHv37kUBMMILFy7Uuui3334b89U//vhjTCNmQycXQM2aNe11xSBiDjf0jnr16oX8Kr1tZIBDeeuttw4aNGj69OkRK7KalyEuGk/gMZEVXDShoBibTjvttEh0txcdxFYwHxcN18DZs2dz94477rATHRd1OLZBd2D4++KLL7TrbefOnTarwm0TKcPNMOGLli9fbj/hWOCiqpsJaIEZ4lJTvEhkexo2b94sEWzatMn+ZqDjoukCXMgmPJrqvu2223QZ5KIMQo0bN44ZqMAgnItqNyAPMXc13pvoz0HnqX379uZ/XNjKlSv79sz4oE1i9uCneAl22E8vumYIlTK9JXkuqjOi7dq1sxM1ojPy2ZTDS9tDFY+LMsjZnrSBJF+qVCkcIJPYs2dPm4vSCpFo+FMz7f3xxx9HomeHzMO57Nevny5x36mv2ZPsJc1FFTDDtxle0NdZSpQoYUJPxQRmi2x58uShhCZxx44dECSteoU0sdZUFSjVICVcVEE7TERHiFbE2lgbs+LBQ4833HADKU8//bRdvNatW5966qnm8/Hp5aLy5mvXrm2vrihghpaY4MBa8LTXxCBOyEqb5ULkGZOLUuCKFSuaEyBB8fpaIWEBggiKTpTJtj/aUFq6dGldKlgX+mnPNn722Wf33Xef/k/IRbV+6/PLfWrAgMolJssOhow50ltQbO5SWSMcGQp71imnuKgmp3yGyIse0SRdn3LNOi6q3Z7YH99zdCIRVualrdD6vshqExvplf0V6CCSES9mZMCAAcWKFYtEA8XpjVrxNpH2gtAOHRP+IJyLbty4MZJoGtSLBnOqVKmSNCokIkDM4QaDEx5eOwNcVLs/qIg8IrVaJrmoF0fgMZEVXDShoLzoLAMjoI7n1KlTx2y99nHRcA1U7CUTUltwXNTheMPixYtNvCL6svblAtynlStX8o9v88uxwEW1+RbnFetGTVRh38Sq586LpghwUYiE4ZawetiUiSw6bNiwyOHRXPC5Me4dOnRg5IDgjRkzBvfUnnhmiCpYsCB5zASBppMZfnQ5a9YscbYZM2asWrUKqqaRe+TIkSIqym8HNcEpt5fF9EHCeDXCIVZsDFtnKBUjGaWynekzzjjDnuRWBE7D3EKg0A6+iDW4qvoSBkzY5hjyh2CAvl1bdN1OnTpFDj+WYxdYTKlWrVrTpk3DEPTt27dmzZo2FwU66ItLun79+tGjR+uBMFieiRx69+7NJSSErjRv3rw777wT1wEPCedbBCwoai8a9SFy+GqVHLK33noLofm+2qIYNr4DwzEh4lGkSBHUafjw4Y888ggFM9tQQ5pYTlvXrl0hKngn4q7iwPbKoYi3WdL3orpKiuEtXtrytVn5VCjL5s2bIz10XvuiETjyUdTZYMVVXzuMx/bt23FuaHRz4BCtLly4sL08qLNM9unK6tWrkxL8UoJA3xENxvGlIag4zAfRRaKb69R24quR6LmmgQMHvvDCC5TcEKQQeYqLQhKMhUQ3ChUqZLP9oHiDrRBegCCColu+fLnOBaDAMFVskY5JS8lpArxJPE79ivJTHvzm8847z5RcMTzxXM0zFTHbbNXT/AKeKOMFBkdTnEGzps+0YB9atWr1/PPP9+jRg76mPUgyiZFo8F4IKkZPakNDzJ49W8uzas3wLehZgSlTpqiD+9KlbwqskHVc1GwKsMmbl9YoInha4fdtSLGJjeYOsAa+wiBMY0UTclHTjxjIFLpJYaK14t2lSxdf/s8//xxrrB069qxoOBdFknny5KFr2wdKBUWKMsVgLOjTp4/Mfjy+FJOLaorKnrAT3nnnHXG5DHBR8Toz45YSLhpP4DGRFVw0XFD2bi/GPgb6iDU/5eOi4Rqo8OAVKlSw29FxUYdjGwrWY7usS5cu1cqfSVEEWS8a3Itbvm9bHAtclPobzq2TojH32DgumhLg/5144omQK/wzTD9OjFZ4kOqAAQMUzg4nmER5ZgxCSrSBDydTjqYqEIJcPYYB1FSriJFocEWGeWx6ixYtlFK3bl0y6COl+fLl45+pU6fKfZEPsWDBAi+6IoTrTBkY8hkAbrjhBnsl3AYDqhhFJPq9ECpl1qboOTBPnAMI2+OPP85dM6Lv27ePAUmh5BmonnvuOfs7EzamT5+uNS6Bd9mfduBXJUuWFLu7++67KTw+rhzZSDR8SPny5RkXcaz1cYVI9HBRvJNFmzdvhlEoG5wTv9O3Rxd88sknilJIE+BAo/N4S1QNSnDgwAFFfYxEFyRhF9xV65QtWxYaEBT1nDlzbrvtNqWgCSZyIAO8OAMeSTBccLVq1UxgjBCgUe3bt6ckej5Onm2nQpoYG6dvDFBsPANsHM2n7Z144YMHD6b50FXJgfpqa6IOykaizByJoQY4x1ryPeGEE+Ab8Bzqy//S8CeffBLjq68L1K9ff/fu3cGKjxs3TtEvI9FVNVP+nTt3otL0i169evXs2bNRo0YYbt2iFaiUJkeoI/pDK+hzeZHoQr3ZIewDRk/+ViT63VpoGJc1atRAOWUP6UfUQqFTItEPHtiqGCJPcVHkf8EFF7Rt2xZmTvc3a7ZB8coJ87VCwgL4EE90WphSOvQbkoAmIxZskXYHQcW1ICwlR4XMHBPPVBPTqTUHwV81aKVKlfQ5DToX3FUyhEbGM2s0PY2iU+WRKLu2V3dhtlIDvGosjGKAcQnv/eKLL8R+I9G4o2aTc/aANpX0bC3C0GHEDDfIOi7qpR1rt08BgObNm+O7y03RhMW5555rH/qVWZPvoh0TGEl79fK7775DY433n5CL2tGbeBEy0ZertOKNzbGngSAYmrwI7tAR47KNv+/Vl156KZeYTdto0ws0e3vffffZ5lGzkPE2jMTkotoIQEewv/ZEHzFzphloI9/uD/Eo+zhuBrhoPIHHhNbGjQzp13RkWtxkSMhFtSJt7wYPFxRejT1bjVsSsWI7a5rPhPIK10AGDo0sdhxdzQHZe0/27NkTvlHZweEoAo76p9HPh8rQ0Vn0TZNdu3bR33HscSA1JXfw4EEdKLWj9njHBhcVGGWpNn5bMKawQwqBtdXU/vbt2xm5Y+7DtPHVV1/he6GpDFSMapMnTx41ahR+PL5OSCS9INBU+2uc/Nb+6rQPGjb05aLwvaAJQX3Xr18f77MTRyCQjBnkglzUiwpn5cqVMgTUTiTKQLsp7ADCa9eutb/+lyRoLN+RSAF7pHiGST4HboYhC+7xDm9iyr9mzZrwHVkZAwq/atUqU34kg3zsF8WreBD8lkcF10wyAwSyevVqjQcxP0bKwIBkUBKfcELkafbo8lj88njfOA0iZivEK0C6gD0x6/Axy8NAgNqYeaV0gRGELiArlzAnLejrQQIE2A6CQnkSRvPOHsyYMQM3+pJLLjGdGkIOOTdGA8sg4h0SAkrQzgKzfOSlefwmopUXneKJWJFvMKQnnXTSKaecYow/+la4cGHD/RjHTz311Eg0RDOMglYYOnSo5i+6du2qbRFaxS1atCjO/fDhwyFpsBd7kVnLzr44jTYgt5988om5hDiZ3RDouWYxKACkEYpSq1Yt2R/t0MmXL99HH33E66imJinGjRtnnuZ7tWKViV0z6lGXJk2amDXGe+65p0+fPqYYEKpghG0DbcOx49960cbSRgD4ksIxdOnSpV69esbPy0AbaRm/ZcuW+uqpJoLPO+88hnutcmhCwV671leL7I0VihVvFhtDBB6EdoxTgHXr1qEYtIhUAudB9UKSkcMPdWvO1P4oC0pesGDBLVu2aN9cuKA0w27mBTDyuXPnNhtVNL/A27HVmjwK18CBAwdGorPG7777LuMXYtQs4WmnnTZ27FgejlaffPLJefLk8X3A3MHhKAU9ThGJFi5ciAeig5Off/65BhF9xIVEbpGB/31xFr1jiYs6HIHAX8TEx/z4wTPPPOMMcVYjJhfNWbz44ot4EjldCod0IOZ5UYejF0uXLoXzwC6wD3jkrVq1MnM90AntjRcbNIcvfNBysdZ/qlWrpmU3OK04A2wTdxwvfPTo0VrjKlmyJB1f8x2w9GbNmsHioF7aFODbeQ5/aNCggcqAQ89D4AyQmf79+4sw83boitkxYX8qE1fGLDtffvnl8RbeeeDZZ5/dt29fMtxyyy1t2rQxq16HDh26//77zYr3tddea5Y97R06PAGipfDX+fPnf/PNN+O9GuKqTadiL08//bRZI+3RowecjV/Bc5AGjCXmWq624WgBHxrfr18/e17DtxGgY8eO4lQZbiN79wciQiCi3BSPOkJlFQT+jDPOGDx4ME9Ai+DnpEBiZ8yYsXv3bnimytO4cWM5nSECDwKBU2DzhB07dsDwIfPPPvssygPz10Jl2bJlRT7NMVSKZDRWu/dhpDB/TXvFE5QX5aJUH4as3V5XXHGFvegKIdc2ByqoiacQDRQGDRqkIxL8ELmNHz+eS4gryoB3jtDgopTNxLxwcDjaQW9asGCB2aCKrTB9nH/gpeaWCfJnw3FRhyyE9haa/YcGuBS33357jhTpuMIRwkV19G7Tpk1r166tUKFCeCArhyMNjosek9i7d++qVasysOUhJdCmAN82LRs//fRT+Aq/dkwEjwAkA3sXQExzFLLivX79ers8mzdvTmZrA/wK7urbD6JiUBFqGv652oSgqBneCBBEcPcHrCkzGxkSCtwH2h1xmZ1QGWtlhpvg5qmYgrJ3e1HCoBi3bdsW3MYVroHaAKLKouc+7k1KMKaJg8NRDbotPQ6dpwf5zAWX2MmdO3fGOy6XI3Bc9HjBhx9+mDt37iJFinTu3Hnw4MGjRo3q379/u3btOnXqFHOYd0gtdJjT94GK7MeLL74YSYPZRuVwtEDHs6+55pqcLoiDg4ODg4ODQwrguOhxhM8++6xNmzaVK1c++eSTGzRocOedd2bzKvzxiUWLFnXr1q1UqVLFixevUqWK78uT2YyNGzfS9JUqVRowYEAOFsMhAxgyZEj16tXRopIlS/bo0SOZT9U7ODg4ODg4OBzJcFzUwcHBwcHBwcHBwcHBIbvhuKiDg4ODg4ODg4ODg4NDdsNxUQcHBwcHBwcHBwcHB4fshuOiDg4ODg4ODg4ODg4ODtkNx0UdHBwcHBwcHBwcHBwcshuOizo4ODg4ODg4ODg4ODhkNxwXdXBwcHBwcHBwcHBwcMhuOC7qcCxgxYoVr7/++u+//57TBTkS8f333w8ZMmTXrl05XRCHYxAHDx6cPn36N998k2R+Ouknn3yyaNGi5F+xfPnyoUOHDh8+/D//+U+Gyujg4ODg4OBwhMJxUYdjAdWrV49EIlOnTs3pghyJ6NatG8K59957c7ogDscUfvjhhy5duhQuXBjtmjx5csL8mzdv7t69e5EiRcj/7LPPJvOKP//8k1e8+uqrH3/8ccmSJXPnzr1kyZJMF9zBwcHBwcHhSIHjog7HAl577bXWrVvjHOd0QY5ELFiwoGnTpuly4v/444+UFyMrnnkk4zipb8OGDZPkokKHDh2S56Ivv/xysWLFYKT8P2fOnCuvvHLr1q0ZL6uDg4ODg4PDEQbHRR0cHA7Df/7zn8cffzy1zzxw4EDnzp1T+8wjHF27dt27d29OlyLL8Y9//CNdXPSpp55KnotWrVq1Vq1amSidg4ODg4ODwxGN1HNRHNkvD8eWLVt8edauXatbv/76q1L+/PPPTZs2LV68eM6cOYsWLeIhhw4dSnnZHBwcwrF///7q1avfc889qX1shw4djitSMWrUKBjXzz//nNMFyXJkHRdFFcl5XKlNJvHbb7999tlnb7/99rRp01atWvXXX3/ldIkOA+VZvXr1e++9t3DhwoMHD6brt9u2bZs1a9b777+/ceNGO/2XX3753+EgJfxR+/bt++CDD3766ad0VyAOdu3a9eGHH86bNw+NVcrnn3+e/M995/kPHDjwv0SQ9GhuX7opQDLAxaKc77zzDi2C68V7lc7/yT8kHn7//fd///vfK1asyPyj4gE3csKECVn3fAFRv/baa1999VVWv+gYQ7ZFqcAgvPnmm1n9FoesRuq5KMPMp4fDF9bihx9+MLewnkpcs2aNUhYsWKB/vvjiiyNtKD1isWfPno8++oiez1DN+OS7S8qSJUtef/11fBQIf/DnjD3r16/3ouP9+PHjZ8yYYR6CMz19+vQ33niDW/ZP/vjjD0YamvLPP/9cunQpxhofyLcpkdGI33pRq/Tqq6/ihZhbW7ZsmTRp0siRI2OaeB7FrZkzZ/JDny0LucWjggFUKP8nn3zyr3/9C/kEd/AycsuHZlSeO3fu8OHDv/7662B5UgJegW4PGzbsrbfe2rlzp+8uqs6rEf7o0aMZv7Up0cb27dupNf/s3bt36tSpZEMCvjyMzWPGjMGx2LBhg+/ujh07eLudQhPjkNGypJNZTgziuuqqqyAAN95446JFi7788kv7JxSM/JT/22+/9b0ax1eZv/vuu7Fjx+LfGBWiLg899BDPrFKlyqIojNMTD3iTaDL6TE2DsvJChRmidQk7QogAQ24FQbb8+fNTZfoI9aWENO6iNHD566+/LrJg9p3qcuXKleZRCRUjHqigWhwbi0Bw2nbv3q1beFfz589H22m14A/Du4xAKzP809DUJSYX5SFoFw1EGXyziklyUeRAsW21sQMX0dkRCGaHBvUNE9QO5REhQXQjRozA4TZ5EDXCpLQJGcvRBarTo0ePokWLNmzY8IEHHrjnnntq1KhRtmxZtD2ni/b/gbL9/e9/j6ShYsWKDBzJ/BDSeNNNN7Vs2RKVw/jXrVv3+uuvZ8jT3VGjRnXq1EnPzJUrV506dapXr16mTJnTTz/92muvpacHJ7W1q5wCZF4H6I///Oc/CxQogNls3749r65ZsybF49XJP8R3nv/dd9+94YYbTI2qVq16dhTVqlU77bTT8uXLR/odd9xBTszLLbfcYkRKleks1L1WrVo8ASWP50FhgZ944onixYufeOKJV155ZZcuXerXr8/lRRdddPnll1P+zMiEl/bu3ZunUSR6aGYeFQ8MQ2eddRbPP+OMM7Li+TZQIV6EXmX1i44xZEOUCnoKqs5b6B1Z9xaH7EGKuShsRDTyBwuGcHpR241XAaOwuSiWUZc43F507NGlO/6XDHC2Lr74YoZkfEd65sknn4yjae7OmTOHAfLFF19Enk8++SQu8s033yyvFKft0UcfZXijM+NnP/LII2eeeSYeDJf8Azl57LHHKlSowNifO3fuk046SRPSkFKsDG8h28cff8zoJbcbXHHFFVoIWr58+Z133lm6dOnChQvjDvIPd3GMvKiGPPjggwx+Q4cO7dy5M+mMpmZ5HL/hmmuuwZGCVVKdv/3tb88880z4LerSt29fxS7yjXz403gGuJ6wuI4dO1JOfiLCDLVo165dwYIFqRrs4rzzzmNUyxMFBi7lbYTCIyhaAS+/TZs2+C6DBg0ydzdv3ox7hFRnz55NmWkRZG5I1KxZsy655BKcEryEDz/8kBapVKkSlTUtIjz99NP4Q7jmCL9BgwZ4GF7ULcAZ5Yf8HH/OZIZM4uJwiydA2Kj1woULSYc/4IjwcLxGWr9///7KD/vi53gYgwcPpqj4Qy+//LJuwRgRHT+BY0AwypUrJ93gCfICUQBajRTSH4sivF/DY6kaCgkl69q16wknnIDqJiPMEK3zQjtCiAAT3goCmyY/j7ej6tQXn3vu3LmFChUi5dZbb+WldD3Eju6Rgi9ryO2kSZNIoUcnoxjxAElDn3nO7bffDgVlnOZXNDFigQ+g3pUrV65Xrx68hURos/3bkC4j8P/999+PEHgO2nLdddep9W0uCkdt3br1K6+8gnnhLeeffz4VMXeT4aIME8gNP4actKPURq9AvNiBJk2aIFXKgEx4lwJo//e//8WwoDD8CuXBHacuKKSMDOylVatW8umln8fMgV40ExKCqqMnJpG+j41FxxBXwtmTrAYGByWcOnUqzbd169bbbruNJihfvnwycyt0t8aNG5tLvAVoJI1r58HE8UDU0qQsXrwYxSMRg+ajo4a70iszWS+GHp4DXTEpdF6GlXRRl5jn+VFdnkz/8mVGjVF4qmBSLr30Upss0e4ME4iIxGbNmgXpKJaQQQTFoA/adzdt2iSWzjiefOHjQSQ5i7goWLZsWfZwUfpOy5Yt8a8y8Nuj1MKkpNgZiFKRAcybN89x0WMDKeai+/btw9XTIltMYO/IQPe2ueiPP/7I/5hI0we0uIpvkdriHXuYOHEizASx6xI/np551lln6RJ3jSHnrbfeMvmnTJlChgsuuMA4Ae3btycF59V8ZQH/nhTGQjxjpcA3SLnvvvu86LoTjXjqqaeSgkcI7+VRK1asOP3000nByfCiqyL//ve/ucSX7dWr144dOxizcWG9qFv/wAMPmPLceOONZOvTp48usfh4zGb7Fr5Lwlu4JqhT/fr1fSPfSy+9xNvt/eE9evQQPdAlgzo0hhRIqZZYVWZc1Qw3R0z85z//wT82i107d+4UCUEsXrTLIExIlMkPPyxZsiQ/0dQMgBiQn0R4i9zuhx9+mBSomjLQU7iEpOmSJ1999dVe1C+hakieuzYX7dChg+1w4PQbL/aNN94gs71Hl4fgDkI8dEkT4ESSByqoFC174t/AYbyohlx22WWkGP1R8ZLZbIk0aDX0U5e//PILFA5VTEaYIVqXsCPEE2D4rRBoisfeoyv1gwabFK1+2MGfafratWsbUSRUjHjAIRYPhxYqZdiwYaRUrVqV3qcqw2lJOeecc8yvEnYZANk788wzzco2DSSyZ7gozgFSNT4u5Ja7F198sXlC8nt0ITBBP0PKpj0CAI7KpZk/Qjk1U4MR0+r9r7/+Kr8cP9vsepDkp02blrAMRz5++OGHUqVK5cmTZ/ny5cG7zz33HDUNnz3JBtBM9mYKNJBmpWBr164N/yG+BNnMpJhw++23Y7rtL3iJ+cBI7WwYh2LFipEeXBzG8bjkkksy72CcfPLJRYsW9SWOGTPmpJNOyuSTGVu1PyV4i2IzaptLxq9g3UXVgG8XK5ZQga+NcbaBA4ZYLrrookwWHmj+Meu4KHY4e7hohoGEj8bA/kdXZAeNzo6LHgNIMRcVyfzqq6+++OILvDcoitlL40Xdgrlz5zL88I9vXRSPGUaqbPgxWjh1IRPDgUtavHjxV1991aQwluCEPfroo7rE0cR59c2M1qtXj947fPhwXcqZM8tcYNy4caTYE89yCBilTMqFF15Iiv2RwIULF5KCS6Q9k3gbuaKwl54gEnnz5oVIHEqD3oXPrQyiWLizpjqmnCG3vDSn2Yx8SIYRt0WLFnbFIQYFCxakhGvWrFHK3/72N35lmDwoUaIEZU7vWaZw1K1bt23btnZKv379mjVrprfA8CmDb7cknFMkWZfIzUcbkCEpxmkQB8PLNxngAOZ/8S6bi/LDMmXKmN2t+OhmiSDIRUeNGlW6dOlDFrSscfPNNysDYjdTFcLAgQNJocl0mTwXpY1w7+yxEG8DnTGX4cKMqXVeEh0hRIDhso2HIBddt26d2KBJ+eijj3wdDeYAadT/yShGPGA8tSJkUr777jutpdvZIKvISjOAyXQZ2A75X3nlFTsPzWG4KBKG+A0aNMioivgk2LBhg/Jnkov27dsXgmG68JtvvkkeEk0GzBQpNjHT/ouhQ4eaFBqdFExfwjIc+RAN860TGjC2ap+C5olyCsHTE5oO0HxcCDQNZ0yNcPXVV8NF7TVVbRT38TEvbTtux44dfelffvmlvbSYMdA7pNtBR6VGjRqZHESuueaaeFzUi+6YMP9j2GPWvVSpUpHo5giTgsS0p9FeQPaBfnruuedmpuTCcc5FV69eXaRIEd+uk6MCR1dkB8dFYwJi9WUAxiLBtiBouHxLly7Fkth+Ec4wQ+f8+fPxtJctW+bzo7IUKeaiWvYE1HPOnDn63zhk+FULFiz4/ffffVzUhy1btmiZNOG5suMcInJoVcy733//PXfPP/98X7p4QqtWrXQZ5KLvv/++bxSU3T/zzDNNCmTG5/B5UdpgL5flzp0b79bOoOWaJk2aXHM4rr32WmnCxx9/TIZChQrhXPoOvobcAlr6MyPfxIkTubQXYIXmzZuTPnjwYF2Ki9pKKAqRws3h4gAvvPBCvAxIlQy+k0uimjgTuhQXtV0EnwnGZGgFgIEk6N6pQW0u+sgjj0Sie+SCs+NBLtq+fXso+jUB3H333cogLqoVSPshd911l13aJEc4szkCmYwcOfLEE0/kt2rxhML0YmldMh0hRIDhso2HIBf10nbTmS30Y8aMiURXcWXx8RRr1qxpZkaSUYx4CHJRlDwS3SZtZ1OH1QbOZLoMLc7/voPH9nnRjRs3RqLbX4PaYuatMslFPUtDkAbNF4nuczZ3g1xUxsGeQRCD1aG7oxorVqwQHaL54uXRzFHZsmXxOfbu3WtOKeuA9/r16+2jy/JLkLwubV8k5Axweg/eo+pVqlRJRv70uHz58uXKlWvGjBlK+fHHHwsWLNitWzc7WzwuesEFF5BuLJWwcOFCXu0bRPDPqAKMHZFiZxIWzIvOvMgy1K9f355z96IHK4K+zVdffTUqiiAzD57nj8dFGQvMRIwQk4viZSGlyOEH9mg+aYsRZkyka44GVUFuaIV9Msg7nItSZmr99ttvxzygGxKGwIsfC8PHRbE8thorZzJRLbwkzuRTbJ/EwhWe9pX979evn++ge0xkOJrA9u3bGcGHDh2KdxSUbbpiHHihkR2QGwVDqmPHjkW3kyxAUKuTCXvhJYonAqeiPKgcHMFx0ZhA8p8GoE6xbds2XdJh9Y/ZnEILirWh0nBR3TVrhFmNFHNRLAJ9nuENtaaXQpOojMY8bcTV7rJ4XBSjQLcREc2GAFxHO+Rj+UYmA5G34I7TadOmRax9vMlz0UqVKpmUmFwUShmxNgUFWYFWL8OZ3tNPP63xsmLFigpCk8wtHxcV1zJbWA201mT2PYZwUYzg9ZkGLE7CtNdkbGBVtcXUp+0QEtVUS5cJuagXXUAoUqQIiUWLFu3fv7894ga5KGNM06ZN9Qp8d1uFgly0du3a4bY+tVzUi/o3PXv27NWrF60gvqRBMVyYQlDrkuwIIQIMuRUPMbmoKBCc1ovaOgQij00rjdTOLGIkqRjxkC4uKhcwmS6jVSbfvkqbi2oFPjymbua5KOAVHTt2RM3wVyKH7yJOnoveeuutusQGnnE4cvyAZZLQeUWwbNmyeHnUGZUHNdARDPqI3ET8YE2RlCtXjhRxUcjYFVdcUadOHeOIxDsDnLGD91hyND/JY2kvvPCCpmwgJKj9hRdeSMPZG3S9OFwUZ1ol8QVJCq5Y0sFr1KjBmIKlpQvAfpMpGEAakm3VqlVxWuJlQ5PpjNBCXqQmu+WWW3CQ4p3n9+JzUUTnW22LyUV18jwSjelgEunFSkx+Ti0E2GR6VosWLWho+iMaxQhlnizLhq1G38pGEYke/LEXGELCEAghsTB8XBRFRQ9LlCgxcODAVatWQWYSRrUQws/k89u2bdtSNVwFpSSj8Ciq1p9pPnPQPQQZiyaA3Hg1ZJtuSxWqV69uk/l0xTgQgpEdkEOfPn00TDCmmNhjOoUXrwAxtTrJsBfh8US86MwFfe2ZZ55BaAwiOg3kuKgPolFbt261A/f8GYUoqKw3w4HIpz4+98033/A/OoNpIieaw2WSEeYyj6z9vqi27KI0aKcCeGyIgv5sQuyaT/DB2mGtCqV7PHwLIfNQDIZ4p54WL14s7zlmOn1Ylynkojq4YsLZB1kB7iMZFCYnBPPmzVMsooh1lDT8lo+L6pRUMJih0p944gldhnBRrOrLmcawYcO09mXvX7VBh9cgFFzcLlCgAGOz1h+S4aJedFi97rrrzIhrXK4gF/WiAwbi0j4u3mWOgwa5KMMGTCxky1lquShjLe1itMjmouHCFIJal2RH8OILMPxWTMTkovyqdOnStDhGj0bBS9MmWMUdady4selQSSpGPGSAiybTZRT1xxdKyuaio0eP5n8TbywmMslFt23bhvx5qZpArDKTXHT8+PG3H46jZQDSaf/I4QcNfNA2V6AvH0Dn8MvRLsMK8EEjgUihPNlwnvAzwOk6eL9mzRo4bSTWfGIIUD9Vgc5ijkDbkBJCdd6LAlcY3kUd4RX2Mk48nH766WabN9XE0iYZwx/XWYOagI0N0jwcG0wf/MSkKEDgW2+9Fe88v5fGRevVqzc2DZhZclKpcC5KAfr370+LYAntkwVe2r4Mn3nMMOgmOAlGUNo0YeZ5xWqgDRpZsFfQIZtKJQxDEB4Lw8dFaWUU0pCxZKJaeEmcyYcZIm1+Yriol5zCSyGT36Ob3mgC6tQPPfSQLmXwu3fvrsuMxTjwAiP1L7/8QooofcuWLXHdJ0yYQMGQW0gB4ml1wrAXXqJ4IjhC6D/ehckwaNAgx0WDWLVqFS3im7Dzouv5Yl7GgVm2bBmXWrrX2qGZGqALaF0wez5okmIuqjNCpuj6fAuVUfjc4Kox0MdCkJG+5oJoUnta7xjG888/H4k1dYoyYX30dT7gC7yp5SBsny5TyEUZDPLmzWuoXZAVaGHTt73Ki05qymMwHxFhjB8wYECePHl4iObmQ255AS46Y8YMLk855RTf1LsWeaZMmaLLbNijC6eKRHfD+raEcSmagbcUsbYNC1r+MgNPQi5KixvvGUlq8DDVDHJRI0yGVflS5l1BLtqoUaPI4bEiBYY6za6lkIviiJDzkUceMSk2F00oTC+W1iXTEUIEGC7beIjJRQEDLemvvvpqgwYNtNvq5ptvJgVPy0RsEpJRjHjIABdNpsuIjb/00kt2BpuLYsNFCXz73BgRzCfgMslFkRtGxsyUp4SLHr1QixQrViwkjxolYm0o0BFfO6qNzk6b/RGIF74kTUjmDHCSB++/+uorujYKr62tZEjyU5aUAStEfqmobzuol6aEFAOaAYuGmBUtWpS38K6En/rEY+O3V111lZnfGTlyZPAYSAhglZKA2sLHlnv16lWuXDnfPouGDRuanbrB8/xeGhetUqXKXWmA+4nOxeSi1JeeohPgFSpUQM7BDVNarKM1k69aPMhcrFu3zqRs2bIFsWPHdCkuajNwfXLZjCzhYQgSxsKwuSjtBS0M7hFNGNUimTP5DJE+LuolofDp5aLpjSaAhWeYGz16tC0NE48wYzEOvDgjtaYwfENeeAG8WFqdMOxFwngizZs3p/vb87CSm+OiPmBX582bh3BQ+CVLlmCoNSKjzGJkRobYZFLUBXbv3r1r1y4zR6ndvCZES1YjxVxU678mEqPWfDUY0Pm3pwEXVkR006ZNWBBGGuTFJRJkDPg9DUdpROxsAwqk4dk+LIScYReaDpCb6zsDhjUvUKCAcSNSxUV/+umnQoUK2RwmyAo0ElBm20bjJbdo0UIHk3r27Gmf1dEOKIXVCbnlBbgoWsQoToqZdhVwZKtVq2ami7KBi1ISzc7CwI2DjiHAsdDM6+uvvx4JnGYUJcMQ6zIhF6XJ7Ngk+rlZ/g1yUV/4H/n36m48h8xdunQxd5955plI9Iyi0RkveszMjNYJuShGzTfQxoMm120uqs1d8jMSCtOLpXVeEh0hRIDhso0HqV8w4K2askyZMmYFEh2WK2lP93rJKUY8ZICLJtNltFuycuXKNsfQnk/FKOYtOt/r+6wc7rgJ1Jw8F926dWvk8NUGrEQkuoxv+qyiENkte1xxUfEQLGrI1LV6tD1M4ItErJU0nd60xYhzbw4NJnMGOL2G9Mcff0SvIsl9PoS+D+WGIaxYsUIr8/nz57e/XuPF2qOLNaPFMWsIZ+DAgeGvUBh2BrWQrc7hgJZ0795dw3Hk8DPt9Jfwz43G3LcSb49u165dY3LRyy67DEuojzrawb1s6BANPTTd1Qugc+fOwZ0mNoKxi1RNE4YqPAxBeCwMz+KiKCq/iqn/CaNaJHMmX5YzJhcNUfj0clEvndEEPOvYPKOMvLh69eopJWMxDrw4XFQfTAru1QwpgBdLqxO6MeHxRGT8GzVqFCyw46I2UBWz1GeOfWI8vei8my6lFYzjuB/mHKUN/AEtH9rzTVmKFHNRbb5lqKPm2nD7afQLLr5svvOi5oOiPsT8Hr2DDbxwDX5NmzZ97rnnGLAxr+bA965duzCaxYsXNymwAvzRF1980TxBjpo9haYoJraXIHfEjpgiK//000+blDvvvLNixYom1gWqLCfJF4BKn6/Em7zhhhvwFfr27cvYYKbcKIztxQ4dOpTS7t+/P/yWFw3+5vMAcFaw47Vr1zbm++OPP4alGFvP6KWPQBpjTR+WBU9tAGc5vuIV8B+qXKdOHTOhSDGuuuoq7prZdOxFw4YNbSIR/JYag3TEmuHG7p933nlmbMARQfLm016akLb9ITLbm39oCyy+/tcqCrwRuSErBmaELEKIwO+44w440n333YeaGWr60ksvRQ4P2CjSYiJV4iTpgA0Fg/mERLrXkAbhZOTDFOLQnHLKKSJI2hoaLsx4WpewI4QIMFy28aDF5FdffRVHx0cyNbSbDVRe1D064YQT7FMxXnKKEQ/yA2zXXAGcaAV7gk+fYzEySdhlkGqFChUi0UWkb775hvK888472ubduHHjDz/8kDwvv/yyGoi3owaDBg2CddhcsWfPntw16xshYASR1hlHk/bVuS8M3fr166FMmCk5KJ9//rnmqvB1bJcOoLSRw2Ptyulp2bJlwjIc4RCxByHhdswGV9vhkBeuEXby5Mnt2rWjoyFqzZfDPM0DkzkDnIFJPawuo4DhRfGO7GonZ926daUD2CLtXaS/2JsO4sUugh9GoutgId+Z86IeLRZPpgOWleEd2nRqfd6WN2qpQRsZ4kU5FtLFRXmFb1nY3qNLl9TQXKlSpWAMzF69ekkTMh8ek14W/t2aeFzUVDM8DEF4LAwvjYueEgU2Iebqd3hUiyTP5GcbF00+moABte7SpUu/fv0Uw4xua25lIMaBl04uGl6ADHDR8Hgi+pRomzZtggV2XNQGwzSNhYuocRw1Fp+CZ3lRB0YcDa/ShC/y9RF+KCLKkJFtK4Ip5qKUW2u+Apw7plvv46K4p46LZgzQJ7w6fTEMXHjhhb4NJ4w6+Bk4nYzKvXv3xqyYdQ/G9YEDBzKi8MPTTz8dZogFHDdunL6yzWj6+OOP03w0osbFSHQ9SvHiZOU7duzIiEIiLnKLFi2k6150i4g+jwb4raEKXrTpb7vttnz58ulujRo1yGzu4qcyiOIN4PrgnfAWs4kr3i0Y0ZNPPonBjUR3bw4YMMD49KjiBRdcUL169T59+lB9HGgTdmXz5s2GxlPyhQsXkmK+gY67H/NjfRkGLrs4VSQaI8QX1YNeQxVwBDHc0HsGy2effdas++F8aDCIRPciUk7o4sUXX6wUvHyGUuw+/O3qq68eM2bM4MGD8f5x000Ta9GDARs5qE+hJ2eddRaXCPOuu+5CMmbCCB3QKkGhQoXM6t+WLVu03CRcd911JjYgI6j4CW4l1I4Bfvz48SI5uGVmPye6J1evWbNmIfvfGId0HpicaA6MUd42wyp1DBdmiNZ5oR3Biw6cMQUYfisEPDxv3rwaJu0PMAAcFPqLnQJni3kINlwx4mHixImQZ15NAfAScNrowgqHC3CSINIbN27UwB+JzjqZACchXUbQcU39EA2hdXggCvDQQw8ZTouUNKcTiYamMNuM9cVXLZyWKVMGbYnnE1PHoUOHmlAZt9xyizlmhmeGaSKxdOnSNAQjiLx/WpwCUGz9BAlPnz4d/Ue2eiPuI7/FWYfba3kNo4E8szNsfcphPiNpfzvXB3EVBG6vHWn+SDMCMD0cFG1NnDp1Kuphz3ckcwY4YxtMLr30UhpR/8c7squdivbMBZ1CMbTsGGbxuKiJHGt/ACwmfvnlF4YY9VnGkWQ+PWr2o9rQOQLA6Omlre3b+xKDSBcXDcJ3XnT79u20dSRtpdTOiZKobDFLni7om70m2EcQCbloeBiC8FgYnrUuiqMIpcREB9c8wqNaJHkmP9u4aPLRBJQZ+8wt1VrSsKmgl/4YB156uGjCAmSAi4bHE1HoJvvLgsEnOMQErvKnafGK0GrD0TD1K1eu5B87CjRDvAIaffPNNwmdjRQiS2IXYdbxj2EmwbOzDlkBhufVq1eHxH5E/8iQwujMxspjN9HmdJ2u8aKGjF8Fd4+IRvI0usG6devsnhByKxz4o7zLt+iUI4AHwpxDdtORIWOfX0csCpKGuUmmOSSNffv2rVixQge2bchaBSW2Z88eWtz39YLkwVCUTHBsKbO9NIHQzAK4QUJhxkS8jhAiwPTK1mDnzp32rmYDyuzrqtQufCkmw4qRMSTsMvT6VatWybmJaXaoI53UHFNJLdAiuJNpeoabhF9NOIah74s2b9485l3UtUSJEpHAKV8YOA43HvzMmTP1UVkai2zNmjXjgVriFpI5A5wxLop/bLZjxMOQIUMigU3pEOaI9fliLz4X1Znw4BNs4KWYCVwUSee0TTyFELRv3x6qHExXaCKYrReVUuHChXPlyuU7rO5FJxn1Twa4KII1H6oJxtGlyUSqfV/NwbRqotkO2JYxaNYveArRVCohFw0PQxAeC8M7/LyoTpE0aNDA53AmjGqRzJn8bOOiXnqiCeiMkplD9FHBjMU48NLDRcML4GWIi4bHE9E2mVKlStmk2nHRIPQRE3s9k7bzre3py5pe9EO4n1rxitavX69V0+DxoqxG1sbRdThWEdPKOzg4ODhkJ3B/S5YsGW/fuHbL48gG54Xl5pYpU8asC0FRcNPPOusse4onmTPAGeCiv/zyC25lwlC6vMKsMRooNIt9ilvxhINcVGc3ChUqFLKHmWKbwKq6JH8ybO3JJ5+sVq1aMIKxVt3Nfg19ApcR0+wb8qJnTMxGj5hctHHjxiFc9JZbbnnuuef0vw5s+wqs+KJBoqWT5MBEwfEBv5+HJ5xx47GR6P55+wuQaKBpqYRcNDwMQcJYGDYXJUU7b02EAiFhVItkzuRnjIsqDpMdHiwZJB9NQPMdhgoiN7siGYtx4MWJ7BCTi4YXwMsQFw2PJ3LgwIHSpUuTwd6XtHbt2ogVXdnBS9tnOn/+fNFROKfWOXft2qVo0mZFAVavA6Xa4KDvngCs5e8WsqfYjos6ZASOizo4ODgcCVi0aNEpp5xStmxZO6IPDnr//v3z5csHEbVZkAHOSuTwuAC4zpFYYaXCzwAnc/C+W7duXbp0MYc2cZJuv/12O0RZPOAJUX5qZ2+l5lFVqlSxSaBOEJBoWPSmTZu6du1KYu7cuWN+BsYAZxdf33wOhMJDBhBdwrIpsAIysbcGvP322yReeeWVZhl548aN2gtavnx5WBACbNq0qTlL78U6z++lEVrfZn7AmKswyOb0r6LFUndfTvHzPHny+BbEYDVoBR4/ZbC3JuGzjhgx4u9//7tW5MJx6NAhHaYoXLgw/PDFF1+EfdWrV880ivZbPv/8875qUnddJgxDEB4LY/PmzRErwioaLjZINvPGhFEtkjmTrxehz0a1klF4LfHdfPPNOhQQ3NcTD0lGE5DC03nXrVv3wQcfSNoQe9pu2bJlGYtx4MWJ7EAH5OEzZ85MvgBeLK1OGPbCSxRP5NVXX41Eox6MHj2abrt9+3Z99CV//vxkTm2Yj6MXqIoiEsHtV69erUOh2pTupX3EhURukYH/zVykbgWRPcV2XNQhI9BIaR/1dHBwcHDIEeCW3X333SVKlKhfv3737t3hIZAT2MJLL70UEnyiVq1adsj+3377rVy5cjE30sc7A5zkwXud8IQXtWrV6v7776eECxYsSLJqMD3Y1+mnn96vXz8cXLzPa665xuzKHjp0qBYGhdKlS1eoUIGiUkioEaw1YWhcLfyec845VGrcuHEwHySZzN5y2CBu9E033cRoSKkg502aNMmbN2+PHj18Bylx++rUqaMSwkvxsHUWMeZ5/gkTJpgADWJBsCw88r/97W8mMAROP4xo+vTp+lirwNvtY7G4pLVr19ZCE6TI3uQP3/vHP/4BodIHYGDOyKpGjRqPPfZY8Mso8QD9a9mypQ5vR6KHurUqSNWeffZZsTUd0vaizETVhGY88cQTEm9IGAIvNBYGzWRiKNBYS5cu5VHmHDvKpkXp8KgWQviZfNpC39GJRKMK4cEnqfDwIgU1oKXsHe8JkWQ0AchqyZIlRcy4S8+VQCpXrrx+/fqMxTgQ7MgOMP+77rpLC9QoObpqTuiEFGDFihVBrU4m7IWXKJ6IF13KVoAASsXd2bNn0+PQHFoqedU95kFP1DcyBSyVmcvgH3ipuUXfMSufJpSR46IORwG+/vprBnjMAYPNueeey7CarqDhDg4ODg5ZAVwQfEG5cY0aNUoYAjFoukP2smbmDDC/xUPFKce7TW9wAUHeFcw5JCxCxkDZFHZ7586dENfkz8NTEcOd1q5dO2vWLJy8kBUwqkD1j5wgGpDGlStXzpw5c+7cuRmOEwkBoGXt3arpRXgYgoSxMEKQrqgWKT+Tj0woeXo7S/LRBHSq31SKF61Zs0ZzHBmOcSAkGdkhpACZRLx4IgIigm8rzgU5j+rgc1kHOg5qQzvSTL6wGlzS3TB3RxR7d1zUwcHBwcHhWAAutb6gGIl+VCklrqGDw9EId5LIweFogeOiDg4ODg4Oxwh++umnDh06aPNkvXr17OgyDg7HDxwXdXA4WuC4qIODg4ODwzGFzZs39+/fv2nTpqeddlqjRo169uw5efLknC6Ug0P2wUW1cHA4WuC4qIODg4ODw7GMgwcPuv26DscJXFQLB4ejC46LOjg4ODg4ODg4ODg4OGQ3HBd1cHBwcHBwcHBwcHBwyG44Lurg4ODg4ODg4ODg4OCQ3XBc1MHBwcHBwcHBwcHBwSG74bjo0Y2DBw++9tprvqj9e/funTRpkv3V8u+//37IkCHJfL/4aAF1nDBhwk8//ZTTBUklfvvtt/fff3/9+vUheWI2ZbDFV6xY8frrr2fRd9WTKWcOAq0YPXr0r7/+mtMF8Xbv3v3zzz//8ssv/7OggvH3f4fDbqz9+/ebdKR94MABc/nHH38EX+R71KFDh+wnmOeY/DzEd/evv/4K/iQmfB/OjolNmzahk75EKhjyTLBhw4YMCjpp0C+mTJlipwT7joODg4ODg0O2wXHRoxtvv/12JBKpU6eOLufPn9+yZUt9WW7RokUmW7du3Ui59957c6iYqcS2bdtuueWWvHnzUqP//Oc/OV2c1ADScuuttxYqVIhKQfNCcvqaMl6LV69enZSpU6fmVDlzBMuXL2/SpEnu3Lkp3g8//JCzhZk1a1b37t3hnC+//HLp0qUjUdSvX3/ixIncfffdd6+66iolFihQ4PHHH1+1apX5bb9+/cqVK8etCy+8cObMmZMnTzaZaW4fGzx48CD5a9Wqxd3ChQujG998882QIUOuvvpq/SRfvnx33HEH5TE/2bx5c69evYoVK8bdChUq9OnTh3LmypVL+QsWLFiyZMn8+fPzP6rF/zw2kob//ve/IbWGT3bs2JFfBT9r2a5du0gc7Ny5kwwvvPDCwIEDMy34GIAGP/XUUxIpklRivL7j4ODg4ODgkG1wXPToxvfff487NWrUKJOCn1qxYkWfd7VgwYKmTZsuWbIkJ8qYADHXeRJmO+20044lLipAPBJyvGBTxmzx1157rXXr1kE+lqS0M1/OnALEDCqV41x0woQJt9xyy59//qnLefPmiXSNGDHC5IEgnXHGGSKowSc8++yzKLm9mHnjjTfqIU8++WQw/9atW7nFr0zKoUOHSpQoQWKHDh1iFnL8+PHc3bRpkxdd6+b/bt26/fjjj7p76623knLJJZfocv/+/XBFUiC6MZ+2d+9eCHDnzp3FaX1clOaAclevXr1t27Y3WTjllFMuuugik23o0KHQ8pjPzzywkzYX9eL0HQcHBwcHB4dsg+OixyAuv/zyo8W7mjRpUjJrd3BOn4eqVaBjjIuKbGSA4yXZ4klKOyEyXM7sgeYpcpCLzpw5s0KFCv/73//sxMsuu4xSNW/e3E58/fXXtfaohUEb8LSnn37aToFn5suXT3Q0ZjuWLFnS92H3qlWrkrl3794xy7lmzZpixYrp/59//rlKlSqGPHsBLio0btx4+fLlMZ/me6mPiz7//PPwc1/OgwcPFi9efMCAAXYiXHH06NHhr8gY5s+f7+Oi3lFlLR0cHBwcHI49pJ6LQg++PBxbtmzx5Vm7dq1umTNd+EAbNmxYsmTJnDlzcAs2btyYkgWc4xNHi3e1evXqIkWKvPfee+HZ9u/fX7169XvuucdOdFzURjItnqS0k4HjoiH48ccfy5Qp8+abb/rSJ02aRKny5s1r004MoJYu+/XrZ2c+dOhQ2bJlv/32WzsRLtq1a9dzzjmH/EWLFv366699r4AELlu2zE7RuuvDDz8cs6g8/+STT9b/iOuZZ56x78bkouPGjVu5cmW8ugvqmz4uunjx4mBOGDU5fdWkCihqvNXXzOBo56IxowMEcbScpf/ll19o+uC5YhsHDhz41oK9TSA7wRjE2/ft25elb6F2vOXnn3/O0rccmUhSt7MBGQu1sHv37iFDhvhMWWpx5IjIwSHlSD0XXbhw4aeHw+dV4PSYW2bpYPny5UrBXdA/QU/LISYY0WfMmGGnxPSuduzYsWDBAt9vGfY++OCDYcOGcQv313f3s88+Gzly5MyZM7///ns7WA7eNpQGLyGZ4m3fvh0vfOjQoR9//DFFNelohTgDXjhFjccqKaFOysF/yPbll18q3XDRP/7444svvnj11Vd5fsyfh1QwHjD3o6IIOsR//fXX3Llzhw8fPn78+GDwnm3bts2ePduLKvnkyZMnTpyI2H15EAIsjnELR9y3GmY43p9//onY//Wvf9EEwUmZYFPGbHFqYcoflDZtusiC2ZkJE1BKiI+YZDmRFb0YQY0ePZoB3l5zo2x6izaIAlMSWxN4Js2KVPUTRmKJN/gimDYOBGqJPxfkouGthtc+Z84c/oFl8RAkg0aZ8lByZaMLKCXcNPXs2TN//vy2qgsU7IQTTqBgzz//vJ1+8cUXk1i5cmX7FOi0adOuvPJK3xPgovfff//WrVshkPqJz22FefoWLZPnokHE5KLJICYXjYmbbrrpwgsvDKbXrFnTt4CcPOIZHO/o56K+6ABBHF1n6enO8Vb4DejR9rli37J/tgETl/zs24ABAy644ILgFHxC4PbwlhdffDFL33JkIqFuZxsyFmrh0Ucf5Vft27fPolJ5R5KIHBxSjhRzUXxH7Cme3A8W7L1q+KOM+niuNhfdt28f/+MO8g8OGe6p7iZPHo5P4Gy1bdu2cOHCf/vb3+x027tCnrjXpOTKlQvPz842duzY1q1bv/LKK5jRokWLnn/++Zs3b9YtJH/NNdfcc889cJiPPvqI59trJoqJ0qtXr4Ql7N27N94wDgTcqWHDhlh5M3EIGZPPCrF57LHHYG4xnwCTvP7668n297//nWz9+/dXun6LktSuXbtq1aqKwnLbbbclWcF4oHi87t5774Vi9e3bl2fi2xk9XLt2LdWh4vjZOLv4fMZvePPNNy+99FKEzM+hXgUKFJBHWKhQIbtq77zzzkknnTRmzBhoT9euXSEnVMHcFceDV1Mp437BVURZQ5rSbvHdu3dTcg2oeHvxpA0Bu/POO/UKBjkz5b9q1aqyZcsiyf3798eTUng5BURNi3fr1g32iCcHP6xbty6M0dxVmW+//XalLFmypEWLFiqhFw0MC+9CVqSggSRWqlSpSJEiXJJuFwYWzaM6deqEmiHYK664onjx4jYXDWk1HI5WrVrRWGg7LaigR+3atYO4KtoQqm74/J49ex555BEeHnLuGvKDKlKGmHeRKs+kMCYFV1KqC2yajSiCO1rFRb3oJJE260Kr7CmAo4uLHjhwgF750ksvBW91796dJ6xZsya9rw4xON7Rz0WD0QGEo/QsvbhoOL38+eefl0ZB18sGLoqGTJ8+PZguLmrb6hBcdNFFZMbUp/ft4qK8K0vfcoTAp7TxdDv7ES/UQjgwvE2bNv3kk09SWJIjVkTZCbdB8jhBirmoWGXIxx7EM+lUNhfdtWvXvHnzzJKXHgJyakPO0QJYh6aNw7ko4sWFJcUmMAj8ggsuMEsxGmuhE7rE3kFxDx48qEtc9j59+pjf4tbjvuP3hxcPOsczH3roIV1qoMXLNBn+8Y9/kJJw1+gbb7xBtph7dC+77DIpG3XUYpH5LER4BWMCfeOx0DaTUqNGDX711ltv6ZIHcmnUEjfdnPRDaZ966inuwmGgOiSi2/KfoA1a/SNP/vz5eYh+Dm+BqdasWdO8ThzvnHPOQVZ46lAOCBgpjRs39uI3pXd4i/ND+lf9+vVtLhpT2lSkTJkyJC5cuNAkUkgYYPhutPBy6iGnnnoqXNf8ZOPGjSVLloR7b9++XSlQWZuLgvfff99wUS86b6Va1KtXT8aBep144okwRvOQ33///eyzz6Zq5iFwaVE740yEtBo8FmbO3SpVqrz88ss0E+UZO3asF112IN23OEmDkj9EMtL5++67L+ZdE8EIl1cpjz/+OD2CCpLYtm1bJVIqtCi478BwUTBy5Eg9qmfPnibD0cVFcaPJtnXr1uCtN998MxJYQE6IhAbnaOeiMYGedO7c2U45Ws4vJMNFM5Y5Y2C8i7e0lS4uikpPmTIlAz50urhoht9yJCCotA4+OBF5TgjHE1LMRUUy8UK++OILPNQVK1bs2bPH3P3111/nzp27du1a/vHt0TXQV+a4ZaipQwgQbzgXFRi0bAKj6JGDBg06lAa8Urm24nI4r/yP66z8DHjDhw+3X5HMaQoaEUJrwpDs2LGDZ9pLRpnnovZuyQ4dOpinJaxgTMCxy5UrZ4/ueLcNGzY0K2Mwk7POOsssk8JbeCB6rstZs2YFPV1+QuLdd9/tRef4cf1t2wpVyJs3r7kUx7NJ/rp161Rs05q+phSCLd6jR4+EXNSLRpQhsU2bNiaF9urUqVM8ESVZTsgY/9sfKQH//Oc/teqoSyifj4t++OGHNhf1ons4SZk2bZpJad68ue2SDhw4MEh7RLANFw1vtTlz5nBZu3ZtXx1/+eWXUqVK+VbnKleuHL60/uSTT/KTvn37xsugqK0iz2jpaaedhqmkc5GYP39+7ZRGb+GBwd/aXNRLWzwE48aNU8rRxUVvuOEGSHjMW7QvT2jatGm63pvQ4ByTXBS7h8DtFMdFMwa8F3suw0a6uGiGkS4uelQjqLQOPjgReU4IGQXE6ssAzNrSrl278DrgYkuXLsWfsQ8HQShwIeZHwT82fctqpJiLmu211BMnT/+bQ034pgsWLIDGxOOiO3fuJAPpeIrpPTt+fAIBJsNFteJkCMzGjRsj0V2v1wSgX3388ceR6P5SvOrMrE4bXrd9+3YtQNneZ+a5qO1vacHw9ddfT6aCMQHTuPbaa8MLo0OP/IU4aYfqRx99pFtyoK+//no7v1Z4GjRo4BMIVGfkyJEnnniivWQXMyZQo0aNSDSxRn1NKQRbXNJIyEX37dtXokSJ3LlzIzGlwNyC54p9SFjOM888k/99p/VWrlxJIgRPl8lzUftFqoXZ9lyjRo18+fL5vrcZPC8a0mriJyhGsJpa6O7YsaMuFy5cSB3DJdO1a9dwb7JPnz7qWXv37p01a9bZZ5/tRVtBH/B8+eWXuTznnHN0ftUHHxdFlyTzggULMrR4RxUX1aaAeEfjGCN5Qt26ddP76nCDc+RwUSTvOyBtH1E2W9m//vprpZiZFDs6APoMcYpEV/WVTWvpSZ6lTwi61fTp09HYe++9d8yYMb4jM+PGjdMXa1G5Xr16kcf0KRu4BFgh7j766KNTp061u6qhl5DAZ555plu3bkOHDo0XuSecizIOYk/oHb1797a/o5sk6G6MMv369YtEtye8EYV9YtBwUWz1iBEj7rzzzqefftp32h+v5g0LxvMzoBU0f4dyMrBiK6iUfYo+JhedPXv2xIkTzXn+hG9BeUjH3SQnTU9RsRvBQFbr1q3r2bNny5YtMQ7If8eOHRSpR48eyQst/BC+Fz3pw1AybNiwt956y8gqntJ6lm6jt3Ysg++++04ZeItS7FOy/D9p0iQG0xQG9bFDLQj4rlodoTBo2jvvvBP0i6hjcI9uePEyLCKD/fv3azTkUWqOmOEMGA0pM/rG04I6kwx4/rx589AoChCMJUE3l9tAT8RoTJgwYffu3brF6zC8FMw3N+1FXQJFwsNYobQ82TCCmELITByH4wp0508DkMZu27bNF5pn7dq1+pUCZ5BCQxseF1wvzCKkmIvi0eJGYDLQJHQX1TErnBhT/tfmunhclDz6CUBHfS6mQxAZ46JaW4t3RFNgrNWqS8WKFWMeoUkSn3/+eZcuXRjmsR3ih+ZWVnBRsa9kKugDfICf3HDDDeHZGAxwoGFQM2fOpF78BHqjWzG5KPpMYtWqVU0KbihOgI4viiqYkSYmx8ONi1iHJFPLRb3ovlPScYy8qAmrVq1auAQSlpOxRwcv7XhXXpqEgQbdzHNRXBaI6CmnnOIrXpCLhrRaCBfFLS5atCivkDOEiIJnOH2AuPI0PI94GTZs2CAh4H+gbGYbqlb1ET4D9qmnnhrT9Pm4qBcdPCpXrswPy5Urh0MZ5KJw3RAuunnz5vLly8crakwuCsE743DwXt8Pk+Gi+F7kiRd5BUeQu2eddVbIE+IhxOAcOVz0v//9r050n3feedqpAYPCjEeiR5SNc7Bs2bKyZcuiVIynwegA+F5YRX5y8sknPxaFdD6Zs/QJQbM2atQof/78lOfKK6+kF9SpU8dua0qCJOEhdPYKFSroLPfgwYPthwwYMKBAgQIUgFbQl34uvfRS4wqLXtIR0F6eoMhedF7jZdoI4aK0OINU6dKlmzdvXrduXZnHdDkPWBWqo+8SU+XCUZjDFF4aF2UcvPjiiwsVKqQjCfRTm+Nh1opHobPcQVKNkeHh9AuKetJJJ2G4yNa6dWuTIchFcf1z5cr1wAMPJP+W/v37k46hQ+bUQkVFPravBc2mXc455xwqjvBPPPFEDB2q2K5duyTlFnIIX/jss88uuugiEqFnbdq04XWDBg3y4iitT7fRdmw+slJTGpLGcE/71qtXT2desP8PPvggnZ0CdO7cORIN7mA+zZABxAu1oGH6qaeewgIjLp0GQrxmdgaihRmhI9i2JWHxMiMiNQHthdLyXmwIzUc580Tx7rvv2vXC2DKy0OiwYpSW/sh70cYXXnghScnQxXBsUC1Ki0ahuoZ1jx49mldrKGd8ZMShjSgDRWUsoySMUDQZCkai3A8k8+STT1IkfkUZGFjV1gA7oIEjphAyHMfheIP2lm7dutUO3PNnFKKg2t6FTRD51OQCnIv/V69ejRGAuCpntu2vydrvi2rLLgpE3eCo/LMhCnqRCCf6FJxiwbzq7pEflT7HkTEuivng0vcJhyDmzZsnuwzs86JJAp+je/fuxoPRlrns4aJJVtAG/TYSPQMZkmfhwoUYVpwnXWq3ZzgXXb9+PYlNmjTR5YgRI2gsLLsuk+Gizz33nDw2Xaaci2Kk8K4Y0qCOL7/8su/jIjERXk7sHQ/kfy3W2WC4xYXSEJ55LkqB+Z+ROGbsFsNFw1sthIsCvEARbMqMM50wdnTPnj3JHzMej4HOrzISIyVz8NUcJa1fv76PcBoEuaiX9o1Qfoh7gcfp46KNGzfmVrdu3WI+kMwhURljclG4x+2HI+gNJ8NFW7RoEbLsuXjxYtUo5AlBJDQ4Rw4X9dLmyxo2bGhS8FlJuffee+1sqK588ZjRAeC0pMTcoxtylj4ZtGrVil+Z9S74IVzRHGn2olwUQnXWWWfpM0I//vgj1gxWY++GgJrivJqlPxxTioEa61L0EhJrVjIx9SK99mqhnTnIRXHuy5cvD8U1jsSoUaMi0chqyVdWkAGnDMFb4qJly5aFXcgIqDy41MHM8qFjclHxdgUgwGrJkBrd83FRxi8ufR8ZTvgWcdEyZco8/PDDov20gi12fHeaslOnTqKd+/fvR2G0QSN5hBzC96KkkVeYjz+RrtlJRZUPKm1M3Zbt9R0YadSokYlugGRsli5hZsBRMYgXakELdDQc1s+LHlDSx6KhdspAF1OkQ9u2hBcvJSKiKRlSI9GTL5r5lQ7bE8qQOpieea/OpMBIMf5JBmGmazP2mS8CMOLwBApvVj7xatQ7FGoBMNpGolPwSEB9GYZj+1fU97rrrotEJxzffvttejHP12h15plnakCPadwyFsfheMOqVaswJsG9pXR2cSszIYj1NoQThw0/xDhOeoiZGM1qpJiL6myemVrT51vQfoXPDa4ag23btjGKwATsr1/gi3ALXUxt8Y49ZIyLLliwgMuaNWv6hnwaTt9FNId1MQp0foYZDKXZJpQkFOXcbA/LTi6asIJBcAvvKleuXGaDnIHOFqLMeFoMVCY9GS46e/bsSNoZpE8++YT/sZvmbjJcVCc/DX1NORf10k4eUrB69eoFP0ITRMJyanXCt0iidVFzMjMle3RFw3wf1bS5aMJWC+eicEUG8qJFi1Lau+66K6Fk5PaF+0PyayPRyV07XQtHMTm8gG8ak6YiH/RWv/VxUVhoJP7BS7hBy5Yt45Uz6/boogm4UCYmdhAffPBBxDpanCQSGpwjiotiWsuVK0fDmUi/8ixx6czcCuOgfZY7GB0ghIvGO0ufDLSbw8fK5G2bUSBoLaGdZAj//GyNGjWM/EXnfIv2d9xxB4m+jYhefC76wgsvkG4+DSVcccUV1atXT1hNH/TNjJiRadVn7bZgvChdunTMMx0hXDRy+LIn4ywpAwcO1KXhojxcBvyVV16JV9pwLmpbUQZBmIP5SBKyjRx+mF/MIRnLbxB+CB/7b09bgH79+jVr1kwecEylDeo25ZHtNSu69BQzgcXQnzdvXpTNhIQYN26cWFbytYiJYKgF6Z4dkU5xCmzVlcthdDth8VIiIqDNFHaswRIlStAxDdnQUQU75gKkOpK2OykZYD0YJg5Z0FCl81Bemt7ans93331HykknnWQ/B8tGwYxx6927tz1F4kW3L+lr2+qDMYWQsTgOxxsYOGCV69atW7hw4ZIlSzZs2CBPGBUSIzM9l2GalOD2aZxSnZc0Mw5ZjRRzUa3qmumWb775hku5p6j+9jSgNyKiDCHolgmrq2k2pKBLs2jgEA8Z46L8SicVfXPwvXr10oclevbsaQ5peGlO3ty5c3VJA/F/wg9/KwitcQ21Qnj++eebDPrERcJ9j+PHjydbly5d7MRwLpqwgjHRqlWrSHQ1xl6QHzp0qLiQwn7arAZfmRT8Zl3G5KL//Oc/CxUqJGHefffdPi6KdY5Y5ypjcjwkZjOlDHPREGlTPJzgIkWKJBktJmE5GaV8be2lUXETaEeLJPYEp35lb5NOyEXxBSPRvU/2ixS7SGNtwlYL56JeWqshHB/jjYm1a9eSmcE7JA/apS1JvmkRLSxXrFgx3g8ZvG3qbkNLKEEuSj+NRLcdxnQ00dWQb0JI1Oaoc/JIyEXlloVMNWppy8RLwzVHtxMOBwkNzhHFRb1oFOVIdO+fLhkNtTZilBPF/tSKlxO09iFcNN5Z+mSgKRX8V/vYnuKcmRDQcFHfYpq4nJnlsYHrs23bNrhEw4YNzYEFufi+/YTy6YPzFPG4KEYb/37R4YA0ovPpjTGr5Z2Y24DFRX0dtnbt2jEDq4RzUfvsAMSelAcffFCX8ukRvrb6hy/thnNR3/kUmLmZlNFb7CPEWA8UL/hJ5HDEO4QvHhKy/zOm0sb0ZGSCjByeeOIJM6KpsZo0aeKLB8GIkMkTbsGhU7pnzwNqftyenUTrbNsSXrwUikhc1K6yb1tQp06dbFsKGOV9ehiOcuXKQfaCoTfMM4NcVEX1BSPQzLvZ568AmQqRYKBJDRzOeELwMhTH4bgCXdIs9ZmTnzr48Pvvv+tS/sDBgwfxED4NRIrlUnt3s/PzxSnmotp8SzWoOfVRtYMHinznRRGQKDiCw4PR10cZ89w3XRICVk+3LFasmH3MQ9v37WP08u3sSVxMgJxXXDFs4qBBg3A6zZYSzK7N4uBjmBXzwUmNqZinkE9QetF9O5FoHMt169bhXWl8LVWq1MqVK+XW60jqzTffjAKMHTs23tPkneDBwH7RCs27a27PrBZ6aXP/ZntkeAVjYuPGjdpcWr58eUZ6foXVNnuEZHAj0a9xfv3113379pXvi92U+yUuimNkFP6bb76BEhtrqxlKMixdupShi1foyBDCkceJKHwu4+jRoxkJ7Dm/YFN6sVpc0rBHu3Bp67TnlClTQuRjkLCcaCOjMnnMph1eihtqD1eYuTx58uTKlWvixInYDRpIFBcyhnzkR2rUtF1AkU8Twnf16tX6jiv+HOaVSuGviOlRI4hZwlbTh0Dss2E+0JoQ9WCg3Xg499xzQ/ik0LJly+LFi/t2/FJ+BGIc0yAaN27Mw+Pdbdu2bZCLeml8vkqVKnZ8EZyhzp07I8zgZkgD9V86WrqO3pFZO0Ljre6C6667zjdP4QOdDpmbmXsFfCpatCiWJORXCQ3O9OnTg+w62HeyDbSCNm1Kwri2CkCtxWqIik/rMslFbfc6HJQkEgf0VuXReVH7V5oms1dfYdc9evSgO6DY5gn4yrorF58OaD9EAc91fN1GPC6qE9ExEXQ8wvHKK6/wq8WLFwdvxYyjC7uzvxVsEMJFMU12ihrUbPmRsSpdurROrhpvOybCuahvbgW7YZQEt6ps2bKYQZlrXHkGqWbNmoW8KybiHcKXGuAzxPth8kRL6/Pa2Ekf4Sdm2NLqZXq/ApoMUsJFw4uXQhEl5KIK0m47DNjeM888M74ADoMWY8P3BKWLi5ptIDG5qLY5aOEhHhfNQByH4wr4FXhQ9B0tFzGM2mce16xZI47GmGjCF/ncBsPCYKrZdlIyxVwUD1JrvgI1ifn5uGDsItTL3sTL/+6waELQA/XJkEh0KQbFgv/LCEaim9NGjBiB7R44cCCeaCS6PIJXZ7YzDR48WFscI9HdFPaOyp49e1aqVAlvdfLkyTCoiy66yB6hNVsZdCN8QJtLliwZ+X/svXm8TdX/x39MoTIrhMxFEUUhQxFJMlOGjFEJ4Wuq0CNjCBkLoa6hkCE+JVGSUIZkHooyh1CJkOr8nr/9/t31W/beZ599zz13cK3XH/dxzzr7rL2G93qv92ut9X4vK84nNhZToGxBQGLFLEY2hIxhL7qupguYhMSFA6II00CXyTQMKlasiH1JHSFaEjwDRayoi0cFQwFuU6ZMGfmJhBHWo0eKuQ/uvvtuRJTxLPsY4qsgXJRZH5uYqb19+/aoUeVSErTOi4r/LQQMu+TYsWOywkfJZesPG5o5Aw1Ot9JiTZo0adWqlbI2XLvS2eP79+8fNGgQyjpgkeqxY8dKvATv1l6zZg3vtYXKDAXvcgokPgHPwIXoHZ5//fXXbcwH/ilMEgkZOXIkqgMGAlFhpqeyw4YNE5uMZpw3bx7yQ4bCM2lGdegIW0qdbsWMo2oFChS4//77meRk8c+j15inlS3btWvXUHvmsGiPw3I2COHxPjIE53eNJUPdXSncnDlzZAEoYO0ki9uSDfQysufkonQE7SzHBPLmzUtdsEQZDlQ/VEBFpIg+VTY9BpYf12vGKT9Urc0omDx5sorPrIBxQyd63x2KgaWzETn8CbydmT0UDhLL8JfRR+9jBjHSnWMnbB2jDlltgQmfOnUKW+3vv/8uX748Zha6gsraDLVE46K9e/dGR8klyTaozcawXFRcTEuVKsUoY9yhlxCGxo0b27ioLTCerK46vb9CcVFGOra1s5wRbI6JmLnukCcmFy1YsCB9JwPQJgB+3hKWiwYtW1NCH0kkGKZXW5y5sPBwwp85c2Yg9B3LwbgQrWCsY+rGjRsxNnS/d1lp0m/GjhaiwkW9ixfFJgrLRZnTZe0YWZIjhyh//zcmHjp0KODwz7QhilxUmLPMDqG4aDDucRyuc4jPo9gktJjiaBs2bJB4Rc4QxOh5+crPcbCoIEFiF124cAHVBpmM070s2Kl//PEH8x9/PVbrDaIIzEesNHWaXEHYC8bcnj17eMDZHSdOnMDOc7pW2gCjQKDV/jb57N69Wyc86CwyCdvdMn4iCJEXqoLeQI/zOlfphf7p5xZgO2r1XZ3R5V0YE65shBFOfXUDgrI5N4ThjTRU1EeBR2szJXjsyIWCn3LSYh6nMWEmSIjMJfyN+HjV8ePH9+7dK/tLzvOoHr0WFogBlD5OS2PwMe+FZPJ0LYCapyMDchuqAWmZo0ePwsORUmQ7CRUs0g5h9uhoyEy+fPlsRvaZM2fgjWHXv8MqnOQG8YxFYPr16ydRNOWk+pgxY0qUKGGTukTjonL4Qrn/uSIsF61fv36uXLlsyu3hhx+2cVGbV6o0iNOrPxQXbdOmTYYMGaLSxXIy2XWHPDG5qDiU0m4lS5ZMnTp1qAXf+HDRIUOGlClTZtmyZZBJdEJcLyzwdsKHN8oyqO1cGx9loS1OXJQhH7AiGDVt2lS3N+SYjzMq2+nTpyO41EdHVLiod/Gi2ERhuWjQmlhr1arVs2fPrl27omRCXZvkClQoQps2bVrnrDp37lyRnChyUTkCIzLvwUXjGsfhuoJcYqJ7KGzatEk8IlWK3KwZtHZf+EqWjA9bUGa2+E5GoB8iQ8LG0TVIqcDCa9y4cVKXInnB1V/0mgDKq3jx4q5HGAxmzpwZykszFJiJS5cunWjB0FMSaLo777zTuZ8AF33sscciuxkvOYOhh+2YPn16DDUxAiAhN1to3bq17WGnMXrs2LHA1VdGBaPBRTH1KEC1atV0KwTjRr/6PCwXvduC/sCOHTuwIG1cVI9QxesqV67Mq50rNaG4qLx04MCBeiLWdlydRYOxtEfd5Cz5yD+Jz0WDls9IVguut3fGh4vCJEPd8+QH3k74EKq8efMKE1NrXhjHaFFx+XYV2lBcFKM5d+7cGTNmrF69up6OighYJ4z0M+Fk0rBhQ4m24tPJ3ImocFHv4kWxicJyUbRK7dq14+P4J4fvKlSooG8/LlmyRAWRjiIXLV++vAqj7doICnGK43BdgRYWJ0fRgQiAOH+eOnWKht26dev3338vmpz5VBxKJQi5bJ8qRxgJ9+O9IhlFGC5qEGds3ry5RYsWiXYH7rWCa46LYhqipOjHV1991Rb+5zoHk+6yZctkc7tQoULeboquwKSoU6cOs2lCFC+l4sKFC40aNXJuTJ08ebJp06YpNVKiHNQfOnSoShHvO+dhUWd0AOxXuWBw9+7dmCAYiEEfvvR+wMNiW8tNbFC+Bx98UKcfYblonz59ApZj9unTp48ePQrFypEjR5o0aWxcNE+ePO3bt0cRUXi5KkM/ic0YXGxBXFjhnPJR5xh169bF6Mc2/e6777CfYmJiMPQj4FrkSfGyZMmCfTxx4sSKFSsqreiHi8qtG0B82mfPns3/6hbEYNy5aNDyZqdzixcvrm6sCfsWP1y0SpUqAetSYuz+O++8k4o8/fTTmzZt8tlQYZ3wP/jgA3mgXLlyJPIAL6Jf5OeuQusa+UJApwe0oHcKTLWkp0+fHuVAo/EWukOFPPDpZO6EM9SCjAV9RVLcGvX7ZmxcNGzxotJE/JM5c+aAFgMZsiF+SWplWU6et2zZkldMmjSJV1AG19WNUMDeE6+Wu+66i2E1depUzL9q1aqpDTQZ+PpiwYkTJwKWr4S+JIS8BbSYdsJFH3vsMXUAbd68eWiVtWvXejSC/oo4xXG4fkC/SESi9evX79y5U5xCmQ6E4cslLiTyFQ/wv3ILUjFlSYGyyv9OL5sEguGiBnFGXAPuXSeYP39+IO6XIiYVJNC/TIc5c+aMq79QyoYYH4LXXnstskywGrt37x7XACrXLRDInj17ut6Befny5eR8zjaewI7MnTu3vuUIp3IGqXJGB5B0uRoBMla/fn1az6cvvR8sWrSocOHCkhsWYeXKlfVTXmG56KVLlySGpyB//vzQiSeffFLnokWLFj179iwkTS4lwvS07ZMIs3JC327ClsXOFo9oyaRt27aRTVJQUPFID1j7fmpPwA8XlSjNNuiOrxFw0aB11UfACvQtpmTYt4TlouTTsWNHehPNJkEKO3XqVKhQIcrm343QO3RC0No7lfAEAYv02qIl60KLnISSbQEDhByckSyxuTt06CCOrwA+rG+b+3Qy1+EaaoEhI4s7CBh5oovmzJkjtIoJVK3vOLmod/Hi30QwBzkaDRo2bAivIEWNOJiwxA6A+6l4CjqaNGni31OD/pVGCFixKrp166auUZg7d66Ef0ubNi1NTWdBhBo0aCAPt27desOGDfAZ5Zlfo0YNieEsXJRyIpnt27dv3LgxA8p2uYitEWylilMch+sKv/76q4SDFTCu1cIB/8BL1VebNm1SawH//fefRJ9V2LNnT6K58xguamAQBUyaNKlUqVKZM2dmfmJq97gqI/lg+PDhBQoUQKEn2nXG1wp+/vnnqlWrYp9hxyeOs4TB9QynL5Z+pVZY/Pjjjwm3lgRX3Lp1awS++gI4NuZO2BUZHuMtcQow4cSRI0d27dplO507derUF0PDeTMZZAN9mKxO/Zw5cyaKp9Ox7yGQtsUdNF6aNGn4yn8+fpzweQaC56pC4yS0HgdMaJlt27a53lnl08k8KhAuql/rGrZ4gmg1USggzB07dmRowAmXL1++YMGCmJgYSCMyYNtpDIvjx4/DbKN1vYU6o0uGZBsqIkOoRoggjsN1BdTgb7/9RtOdP3/eJl18RN+ePHnSdcHu4sWLpy0kckQow0UNDAwMDAwMUiC6dOlyT2hgciV1ARMbpUuXvv/++23m6fbt2wNX30KZApCYTubr1q2jAXv37p0I7/KPgwcP5syZ0xklFSxdulQP8p/4cPUX9Y8I4jgYJGcYLmpgYGBgYGBgkPIhDggVK1YcNWrU3Llz+du4ceNMmTJVqlQpJcUGSxwn8+PHjwurl2gRHlfTJQleeuklSrVmzRpb+rlz5zp06KD7BSQ+IuCi8Y/jYJBsYbiogYGBgYGBgcF1gRUrVrRo0aJcuXIFChQoVapUvXr13nvvvXgekE5uSAQn89WrV8OmWrVq9e+///br10+P7JVMAENOkyZNxowZW7duPWHChJiYmDFjxrRv375JkyZJHua9U6dOtF6cYoxFJY6DQfKE4aIGBgYGBgYGBgYGfnH27NmWLVvC52vUqNGjR4+IfaoTFN9++22LFi2KFSuWM2fOChUqQEQldFAS4o8//oCC5smTJ3PmzPnz53/55Zd9xnA2cRxSMAwXNTAwMDAwMDAwMDAwMEhsGC5qYGBgYGBgYGBgYGBgkNgwXNTAwMDAwMDAwMDAwMAgsWG4aIrF2rVr582bl8gv/fHHHz/88MNEfqng119/tQVguHjx4v/+978k99EPi//+++9PB0JdMUwFnQ/b4Cdmw+7du2fNmjVkyBD+/vHHH/GsAqX96quvdK+POXPmfPvtt/HM1gDZ2L59+5IlS/bv3y8pmzdv9v9zXQn4l5xLly7Z0v1fNUYO9PuCBQso85YtW+SyR8bmTz/9FIdqa3COawMDAwMDA4MUA8NFUyxuvfXWQCCQaEwsJibmnnvu4Y333Xdf4rxRARZUp06dVKlS8Xa5oxzD9/nnn8+QIQMp0NFELk9cQZlfffXVvHnzSoC4bNmylShRInfu3PytX78+hrh+ezt8j6qlTZtWHi5atOhdFng4f/780gjwQI/XXb58uX379rwRejN58mR+Urhw4fjY+kOHDr3lllv0+Ox79uzhIzWKOE+DoBWqoVKlSkjC008/XbNmzdtvv71Ro0bZs2f3HyRDVwL+Jeezzz5r2rSpPJY6deo77riDV+fLl4/CvPjiiz/88IPruxCh4cOHZ8mShRLWrl37mWeeKVeuXNasWWvVqlW8ePFp06bFtfrOcW1gYGBgYGCQwmC4aIrFyJEj27Rpo9OYhAbGbpJwUUA1M2fObLNZH3/88WuCiwrmzZsn1v/hw4clZcOGDWXLliWlRo0atm3SJ598kvTKlSvbMjl27Ng999wDffV4EVLRrFkz9fGtt966++674xkDsGfPnjoXvXLlCvRpzJgx8ckzWSExx5EAakfvFy5cWN0C99NPP4k8qD3SsHAqAf+SA0flyXbt2slHRtaIESNIyZAhA2TV9vPt27dDa/nWFuHw22+/LVasGOnjx4/3WWYdruPawMDAwMDAIMXAcFGDqOG3335LKi4KZFdWt1lffPHFa4iLrlmzRrioXgUYgmxkzZw5U3+4R48eJD766KPOfN5///133nkn1FsOHjyYOnVqW27xByw0rvdWX1t45plnEvmNa9eupUm7d++uJ/7666958uT5+uuvI87Wv+RUq1aNJ//v//5Pf0YuhStUqJCeePToUUpFuqvg/fLLL7feeis8NrICO8e1gYGBgYGBQYpB9Lnojz/++N3VOHTokO2ZvXv3ylfO3RiMb/nq5MmTUS+bQYLCcNH4AILh5KLg7rvvJrFjx456IgwhFKNgTMFYQr0lJiaGH3700UfRKrYgZXPRUaNGZc+ePZFfOmPGDJq0du3atnRIXXz8wP1LTvXq1Z1cdMGCBSKlx48fV4ktWrQg5a677grl5DxlypSIryY3XNQVV65cOXLkiMdIjwouXbrEW1DsCfqWUIjTYYRrukH++++/b7/99ssvv/R+bOvWrdFV3bTw+vXrV65cGcU89cwPHjzo+tVGC5Fle/HiRd2VHWNy586d8SimCxK0WQwMDJyIPhdlDH95Nfbs2aM/wGyhvrJZGCj6NWvWyFdo/KiXLUXi8OHDc+bMWbhw4f79+20E/ptvvtFNRsH333//zjvvMKVB+525MSPKCcAdO3bwGL1pe+Dvv/9evnz5W2+9RQ6nTp3Sv3Lloh7Fc+LChQtMAGT+ySefXL582fbtiRMnIJZTp06lVM5gKj65KMWYPXs2mWzYsMGWA+Wnavxz5swZbO758+c7LRusgXfffffTTz/95ZdfbN+Swq+gEJFNjaG4aL58+Ujs1q2bnhiKUaxbty5UICLmV+Thueee44eQq29isWzZMspMd+sPhxUDcP78+c8++4xvGeBOLkr32Vqe5qVb+efcuXMIz6xZs2hnZyFXrVo1efLkzz//nMecL/Vofx3YditWrKAMPENf6yrIo5t44+LFiykYY0SNjrlz56ZJkyZz5szSXB6HmbGGN2/ePH36dKTduQDnp/o6GAgiD5RfT6f8tvBFYsjC9yjq6dOnbfnYlIB/yXHlotROSqXMcTIXl06aNFRdeJhB7VFZBuO0adMYmE7/dlcuGv+mptGQahoN+XeVtGQOccm29U4ojB07tkKFCs6GCgsmYt4yevTouBcwvkBuCxUqtH37dp/PX7sNMmTIEPHrDlV45tzBgwfLROC6ihQBmEAHDBiQPXt28nz22WejkqeOAwcOtG3b1pWL/vTTT5kyZXrhhRciyBY9kC1btoCGrFmzMhPFu7z/HxK6WQwMDFwRZS6KKYmyxkr4VYNuRvz777/MMdg9rlx0165dX331ldBRw0X9AL5UsWJFGo05++GHH65bty6J2KMDBw4sUqQI+lQ/zkfvtG7dunnz5qtXrxZOUrx48dq1azdo0CBoTc/M/RK/hMf4/6abbuKj7vVHzzIjjhs3jtcxl6Cy9VipTi7qWrxQwHysVKkSJimEsFSpUrxIGSKUfNCgQWSFZQmRePDBBwsUKEC2+s/DclFk7/nnn8cEQQKXLl2aP3/+p59+WnzbqEXDhg1vuOEGCs8rbrzxRjkZyzynr1X36NGD1oOeffHFFxRPbxlaj0abNGlSx44d+SHN6yeYrQ5XLkrBJFFIskIoRtGiRYtQA4dZtk+fPvfffz8/rF+/Pv/37t27U6dOOXLkIAWCpyoSVgyClk2GgEEa+adDhw5lypRRXJRRTDtjMaROnVoe3r17d5MmTWjeu+66i14rXLiwvIJOPHv2rMoT+kfxRowYAY2sWrUqz5ctW/bxxx/HOJAHPNpfAar2yiuvFCxYkPwhrhIRCjlXtQvVTXv37uUxpAsSDvPHWgpapg9DiZJkyJDhVQuh1lNgtpQWKaVB+Em6dOlo2wsXLvivvg3IvHhsgi5duoTaGKTYkMahQ4fC3p988smMGTPC6IKhlYB/yXFyUQYL6oLE8uXLq0QkRwr53XffhaqLB2CJjPp27dpt27YNcWLc8Vd/wDmu49/UWMONGjUaNmwYElu0aFGEJNnGfJZ4184NZ6FeCKSfTFCYPAxvj+vbhXq9/fbbcf1h/IGOYgw6V9YQ5o8//tj5/DXdIC+99FJYIv3ee+9FkYsKUKEJQboYoQ899JDrWhv6limYl0bGRUePHn3nnXdWjQVvmTBhQthfxdXbP4GaxcDAIBSizEXPnTuHsg4VaDFoGQE8cOLECScXxVYg5dChQ8JUDRf1A4iE8v2jVevVqxe0WMfx48cllIhuhg4fPpwUtRgs8/H777+PFSgpKF9SSpYsuXbtWj7SBbCyzJkzK3udPG+77Tb5//z58+nTp69WrZrK38lFXYvniu+//56HIRLyUQL5YA3LR9gF3ypp4R8sVMxWfWsrLBf98MMPdZe2/v3783HNmjXSYlBQPt58882DBw+mGOTTvXt3UnLmzCnLrlCggBZYaMmSJdiy8j/MVvi8QGKQem8EOWHjovydMWOGEEUsFdvDwihg7LNiMWXKFLoP+uc9cOSH+r07vXr1IoUcVEpYMYB10Pj6WkCNGjUUF8V8hI4GrBCs6gEEUpq3c+fOly5dCsb2zhtvvKGeqVWrFhxS/keWeCnMasuWLQcOHAh6tr8OOAlkkt8KhYPf8li/fv2C4boJcqLi9EC6MJjUk9Td+4zuqVOnsmbN+vrrr6sU2pPMVYwoP9V3gorcfvvtIhVwb6psewAhocWWLVum3pIqVSrqzitCKQH/kmPjonSExD2C1+3bt0891qdPH9tOaZyASRrQwn1XrlyZ8uubz7ZxHf+mxjCFS6Nw5KPIav78+eXhJAStSpltiRSVrnc+HCfqxahBv0UQfyss9UK0Ro4cGUHkM5QJgrd48WLXb2kKJLl379629MuXL1Oep59+2vmTZNIgVCqCW83IMCwXlQkiulz0gw8+iDrpQuViJKAuXL9FFT/zzDORcVF6v0iRIspI8In58+c7Nac3EqJZDAwMPBBlLiokE6tx8+bNUMqtW7eqIJBByx8J+3Xv3r38Y+OiGH8bLPz777+Gi/oE7D2gBboEeuyQp556ymaGwi50k1rmP31axcKzkSiJX6LuBnzggQdgHerbwoUL6/d22Liod/F00Pt33313z549VQqWCtxg3LhxQWv9Il26dLapa86cOWSuM+GwXBQqgpm7atUq+SgmrLpqAhs3YPm86W+hLqqJFi1aFNBiCGHHyF4iRc2TJw8T3pVYyAK2vnfkB4qL0hSY+5A9Ouvll192ndSFUWBAvxCLjh07yuJCXLkoPN/GRcOKASzl3nvv1bPFHg1cfUY3V65cOhcFN9xwwy233KI+SqymVq1aycczZ87wkU5XDwjzUcdrQ7W/K8TJFpqhUsJ2E/SMAaKOeyEYKh5sWC7aoUMHsrKdGb7jjjtIVIzdu/qhwCAS000Af9bt/k6dOpUtW1Z/ftCgQXqeTiXgX3KEi1Lm4sWLy7m4WrVqzZgxw0Y8ZIc5TZo0oZxFvQGV5RVq07J9+/aBqwMF28Z1/Jt60qRJiMcVDbJ3ajt6kJiAGlFxxovawFe488479WURhThRr4gRlnrRthSbkcUzPu+FYlhh6xctWpScQ3k+I/N0otPBBAPDdW0umGwaZOjQoTzAqIyTOKUkLlqzZs1QGSItzZo1k4pEwEXRyWR+9OhR/z/ZuXPnTTfdFGrJIxQMFzW4psF0+Z0DyusNWxeCJhfCHzx4UI97L2BOhLvxE7VNlQiIMheVbU9APVevXi3/q/Xy7du3r127lhnLyUWZjNWThov6h9jcDRo0UPtFChJQRDdDMShTpUqlLAaZEvQdBiEh+kRbr149UtQegjI3L168CBPIYkE97NwX9SieDkzPQOhbMcVFzXYg89KlS9hAWMBqgPnxF1UL4UxR0B6+HTt2rKRg3QYczq58S+Lzzz8ftIKFpk+fnjdiCcmBQIHsq1StWvXxq9GkSROPKjuhuCisbO7cubKvGCp8QqiTlpDGaHHRUGJA/vzftm1bPVunv+htt93m5KK33nqr+khu/ERtlaMc+FipUiX1wODBg0n55ptv5GOo9neFCIO+Uxe2mzp37iwbhk7n2LBcNF++fHKmV4c0rDpg7F19b8iJaBEPeKPawcubNy/czOOHTiXgX3KEizKIaG05g02KcytJugn8/PPPfurihOQpLr60f8A6XK2+tY3r+Dc1PZ47d+7HHYirwRoVoHa6d+8u5HnUqFGK5+/du/ddC1mzZqXx342FUnc69fr000+7du3KuLCtW5HbuxqcHvioQdIxTXhyypQpKDrGvn6Y2ZV6rVq1SvdM3rdvX/PmzeWa4tmzZ3svSXzyySelS5cmTxo81KHuX375hQaxRa7GnKCocqsQfEZqpO93JZ8GQWnLMVS0jaunvRM6F6VZ+Lhs2TLbsfxQXBRtIO7WCxYsUMuFNjC00fmTJ0+2heC2kS5GioojoDcd0jhz5kwGCDP1iRMnPCry8ccfk+Hnn3/u/AptjHrnb2RcFLmSJSdQsGBB2srbqAhaIiHnShAbaqT7oqNtmBEwOWJiYtA2NqH12SyY7LBr8Tm3HSZHp9EIEnRAYi6oRXAFOo7hgLxhFdOqcfV6PX78uNytxasZCFTEtWuYN/mWQvKWsPNm0Fr9ZKzxDzwEodLzPHTo0Pz5853RJQQkUgZqijQ66Y23CHkX0mdNDRRQoV86IGYDMikfGYbyD11j+zkjRb6SY4OJgyhz0QMHDkC1f/jhB8a2hJegPjLloKn5X1Y6bVxUQhbt3r1bMjFc1D+YO7Gr0Js33njjyJEjdZXqNENr1apFytKlS+WjnFnVpS0sFw1a+1fYfD169IA8YHxgpquvnFzUo3g6Fi5cyDOLFi1y/VasZ0xeWzpsR9/78hm7CEOhffv2KNmpU6fq9MmVizJVkNiwYUP5iMGRLl06UpjhlM8S2pkUOc4aH9jO6MrlGVAgVxM/FKPAFrQFlHL9YXy4KLMC/+ub2MFocFF0QrZs2WheteWFsQLr0DvUtf1d4eSiYbuJeQ5TSboApq3/1puLUkJ+kjZtWtsEzKxMuuK68eGiQat9GjRoIMUbMmRIMPbcATa3x6/8c1Gn5OhndDEg6AvXrRsVWRcm6bMuNjBTMBjhHph07dq1sykcfVxHpalLlCjxyCOPRFbUKOLcuXMQp5tvvhnRGj58uM0SRUHdaCFg7TnfGAt1zkhRL3qEgVa0aFGahYrr+vzkyZOZLciocR6ifuONN0hnRD/wwANkjj4PWBf2qEHnpF7Yi9DOXr162bJCD9P+Aetsv2usVwom4wvZc8aN09G3b19eYbOQWrduTQkzZMhADlRTWkPfMU5uDQIfLleuHA/XqVMn7PaCcNFu3brB6gOxyJs3L9aUesaVi0Ib7r777tGjR1OwQYMGUd+WLVvqjpoXL16kQZjCmF5R+1SKOU4dc7WRroMHDxYrVowBwpPiGRG0QitJlzGOKleuXLNmTY+KMLJ4hZPkB60zGnJyITIuikHIq+XuKAHCgFb3+MmkSZNEezz55JMIhpr1qGa1atU6d+4MP6TlmU3uv/9+3d/HT7Ns3LgRlYLA0PjISa5cub744ougpaNo8FtuuSVgHbXg1XwrMRd05Ul1yJNhToaIEGPc57IFkHgKSB0qGjGDmYug8lJVvKDlrkIdaTTmShqqSpUqGGMex5X5qnHjxunTp3/88cdpAQYReSKQQYta9+nTp2PHjm+99Zac02nVqpVaOKPK/KR27dqIK2JGe6IK9FMSHiLkXUifNTWwgfkahXD48GE9cM+/FoSCSlAxOk62DPWVFGYiEoWFXcNc1AY5sosCwnRATPlnvwWmGeGizB+0grBw/pdvJXYRUmsWP/wAks/0I9oZdaCc+pxmKKOXwczMit2AwKEdbA45YbkoRC5//vzKPy0sF/Uong65viKU7xyzSMAKM2NLl/V1tRodloui9TBoqLWYfXJG15uLyuk+3c6AgUv4HyD+irJt63Fe1CdsXJTpvGzZsnwsU6aM0x3L42YOb8Sfi86cOZP/6VM92/hzUUBPMWc/8cQT9AUMHOlyLk84298VTi7qp5sQTmZNsXcZKSqUrjcXZdKVSFc2fSUeyMoDME5clLnfeRcRIiHWPLULWodQAtb+kkeN/HNRJ2z+orJgFLA8zPXH5FBDQDtiECdQC+z+/v37C72UM7qhuGhUmjpfvnxYSxEUNVqAHmC/5siRI2vWrIMHD/aI4otAUnK0lvMroV6Y5o899pis8O7YscPmwK8gmjAU9cL4QwkIf5g4cWJAOyxjo16MOLUU4gpIV/369QPW0Xe1EUT7U8iA5VIRds2O1siSJYvu161Dgku7juLk2SBLly6VMwUwMWeMaAXhohQeNcX0hIHEuBabW4mHk4tiU6Fj9XPOMhCg6GrZF0IFHVJrN126dAnEnvQJOkjX0KFD4Ri64zR6mAcwTOUjJLZWrVqhakHJGZ429w0BpOvll1/WKxJZ7KKgZVUOHz5cSCkUzttcZuzwmH7kgfaE5KsWCFp2EeodqVNnwsM2C1YHTFJR+t27d/M8OcgqAI0vippRIDsxlFmC+alXtGnTRnd36t69u3Pj1AOyIkyx+/btK6xP5vFOnTqpZ+rWrVuyZEl1kgUrQrbrIXWueVIpsbWKFi3KVI5mpgXEMEDCdStI3GfUORSJvCVbl8FYg03N3d4iFLaQfmpqYANmEprK6TTBCBXmpVaLtmzZwkddNZFCZ8lJ1WuYi4r7jVJ8cn0LJFvC5zp3jQEGH7OI61dRvzYqhQFypYKIoN9lB1IW54JuZijAFGCqZibu16+f7atgOBJCT0EVVIyQYDgu6l08HTI5lStXzpa+detWdJNsvDivLWU2Ik/1MSwXlVhEqkh+uChmdyDWR1H8nIPW8R4J+ImhQx3FOnHO0Mxwtrs3vOGMo8tkwPTmJH7BcIwCiy0mJsb1q/hzUSkn84eebVS4aNDyO23Xrh0GE0aebeEzVPu7VtPJRcN2k+I/hw4dEv9JCJKkhD2jK2fRbexRNt6nTJniv/o6ihcv7qzdpEmT+BXjLmjx1XTp0mXMmNEW2pdaKyfbuHJRXXKccXRlQPFG2z6PeKWWKlUqVF08gKXOQFZThjcXDUajqatWrcpHZ+Bc7z2WKKJx48YBaxNMD6bgCqzDgBWCy/mVUC8kQReSRo0aoaKdD3tTLyxLlcJMrVNBRb3oIJEcP2FLsb/lrDXUSM7eFyhQQA7+hcWoUaNce0cgc4Fr/Ntk2yA8SYHJBOIU6hoq4aJ6bAWMRRpNp8FOLgrrQy/ZzgjAfwKxF0EtW7ZMn/KClnJjXKsGVKQLZYJxP2LECFvBhPzrh5K8nYd5WKdYAgrw8MMPq2XoeHJRAUNDBnLlypU9HnNy0R49epBiuysInhOI3QMM+mgWmCSipfucQ00DWvgJUbzqDBqQUy3K6YYpButFqW65QsJ/9SEP5KbTfnRywPLgkI+8mo/jx4/Xf7V8+fKAFSwgVJB/BikPlC5d2vYuZlvyV5WdPXt2wNq3lwfg6pkyZVIHG6X1SJSPHiLkp5Bha2rgBPqTwci4W79+/YYNG/bv3y+LU8w4wsiUAOzYsYMUNRxk+5C/x48fv7a5qOz/qkitQjLlUmNG3fFYHDx4UNgm1jYzBw10XINkAhH1uPDAIGitMKFD1UeZJiXeT9DNDIXaKW3rCm8SIgpI56IYfDfffLP6aOOi3sXTcf78eTnTot/bdvjwYSyGoHWQQI7j6nPq0aNHU6VKNXz4cJUSlouKx53KRKZ/9UZXLopljMKVu0zRsHo4Cln8Qy1SaxqB/+EJ6ltEF4tTrUsh584LUW2QaQDo+yRLliyRRJ3mBWN5tSujYEBhr4fyxYo/F/3jjz/gZgEtVEwwNkSz3n0RcNH33nvPI65sqPZ3fdjJRcN2E+aFSqcNYVzKAM2ZMycfQxUsGHsHgD40gtaOBPVVp1/iykUfeOABZxxRDF9+xdCWj7J5glWkljkvXbr0zDPPqAOfTiXgX3IeeughnsR0Uw/QUJQqYG0a6+cAf/75Z2oXsPyyXOuyadMm16AyjGJ+hagoe1pW3HXptY3r+De1BNAuWrSoLh7I3vTp010LH3XMnTs3h4WJEyd63/x04MABisoIdX4l1MsWXgV+60qxvKmXLe4rMkAvy/+itCln27ZtdbbvAfS2HITBWETvMcTq1q0bsI6q2m4adwIBQ9/CMUI9IKcbXL3ok22DfPPNN7LVAy8KFavZNXbRkCFDAtb9W/LRxkUljJNzAZcZlnTUWtAKAaVP0E4IbaC/0CSug5dhLofzUY9hA9iKH4TO5INWn9Kh+sZLVLho0GoBaodm9nBRdnLRO++8kxTbMp/QG4akfAzbLPny5cOccPqcq7ugRfHqS2ZSEiVa/fr1E8YV2RKYMDTdXJHtRxV8US7tk2uWFVCzEoUu1DaPdI3trI0Mutq1a9sqy4hWalltbNKSstambD8PEfJTyLA1NbCB4aD28+SQKZAQDAxG+SgdgdmAFaf8KJmM1q1bJ2beNc9F5fAtVrVEYZJqO4/aOmMX6TD+oj6BPOXKlUtZYOiRNGnSKLdyuQlQH+eVKlXKkycPxijE5p133sEkWrt2rc6RXn755cDVZ2UrV65MingyyCIr2p/+xbgkH7mhW3z6g9aaKx9LlCjhp3g2TJ48WUhXzZo14UJY4egadVP2woULITbMymrWYSZDPel+KXKlpO7zJuaC0vVythOF+MMPP8ycOfORRx4Ro5bRiO0uXJTaqfAPjEk+qp8zP9GkKnO5fFxozGuvvRawzgvBXqA6fHXHHXcoAkAjB6yjtqF78v+F7NMCtb4oEPZI5npXSuCle++9V18Up3GoS/ny5VHloaZniXo6Y8YMlSJmGdaVSvEWg2As84ShffbZZ3QBwlC8ePGAdTZMXMV4u3jIqClfLmNgTlIF++KLL6S75SNPpkuXrmzZslje48ePp4QLFizQY9h4tL8Tskpti+Th3U1UQcVJQh4oqmLjEk4ZsUekXf1tUOIYhVAg1USyp62Oz4WtvhPiOTZ27FjVxb///jsFJhO1Y7x9+3bxfCtZsiTthvFaqlQp3QByKgH/kiOeOU2bNtVLxRgXQ6F69er60XGUg1B9TC5d4WOIwEIxXFxV/blz58Qrie6AS2D2ybYnlFuFP7GN6/g3Newoa9aspGBN9unTB/MR6xmRiOCGj4gBC+ratSuiiGWsb57YIPcY6StuCq5hY+V+HSdn8KZeSuwFSLscAg/GUi9Guhxct0Uss4EuRgh58rbbbpNLbhVQFNSU+qK3Q+0NBmPvqlU+IE7IWozrrmkybBCMZllbYerxvsDWlYvKQqSywm1clAGiz7YKstckAZn5rR5Q2gkhXSgNCT3luvpP34kyZ4DTPh7DJCYmJuCIDY5IdOjQQT/vhnoXjv2lFUAFIa8XDs4zXAI5keGMt6xg46IoB1E4Nt94FJFMvrJR6d0s6OGwXDosF8XukjWagBXjyjbph0VYhiaHhJ1EF80fCB2/2pWLyoKOx7AVUDWGA0NYXK4YeuqrUCLkp5Bha8qQv+NqXOfOfYgWJtnmzZtlVwORlnEnYoykCUfbsmWLCl8k/JOmJl1stmueiyJksucrwL5xjXVmuGhUwBTLpMh4nj59OlzuwQcflNOkcK3+/fvLTgVjWF2DAf+UGVRH/vz5JUoEXEh8MFC+/OTSpUsMclHcDz/8MFMptp2YtgHrHA4dJDsMlGHjxo2oe2F3AcvBEis5VPFCAaNQNtwCVjxV2yI6o4J5F1I0dOhQzPROnTopFs3AkysxA1bM3uXLlx87dmzgwIGi/jAjZLVyxYoVYi5jiU6ZMkVtlLVr1w65FS5K3WvVqvXEE0+QCHtULhBBa36irTDN4fDQGHiXCiyBWc/rVNuWLl1ad4sKy0Wh6yhueLv8HDOChlUsC+NbjoxiyVEqeAWTvfSLKPcCBQpAvXLnzq0KoN+MokD3jRs3Lnv27DyAvsZYJGeojiwoUHGJYxxWDKS+2McZM2aUUjVp0oSPGD1YeGhA1JnMu8Jk5PiDSnn++ef3799Pm8gOW/r06YcNGya7Q/rlJQrM02pfOlT760CY5doPUKVKFZ11e3cT8x+Mjpny/fffx0pgAlZsTU4EgMceeyzUVYoUEuskb968nTt3hswzFpQe91l9GwYMGIDdCeXDkCVnJBwJgYbZdryhZEIaA1ZIJ0U7nUoAvepTcjBnlZ1E/1J4/Wi9BPQKWARYj32NQqDloYUYcNA8Cl+2bFmqyfB3hlVUEI87QEloFgYpP6eQKCvnuI5WU6NbxIsvYAXCQV+FPbaQENi5c6cchK5WrZp+LFmBvg5cHepcITGpV8GCBTFTJDSR7YCGAN2CjkU+acyXXnrJNSIoCm306NGZMmVCyY8YMcK5Q4iQYF/aDv/bQA7OAguSVYOg0nv37k1r0CZY5x7yL3DloijbgOVoKh9tXFS+dW57Sjq6mv/lsiJbiFcd6jDqoEGDJHPXRcyDBw8yJ8p4Yep3DU0UjA2ii+rQE8nTqdUVEAb0xpvhoB+J0oGwMa7974vypExbTvcZ8kmXLp3oB+9mkTV37xhOYblo0BJ4tJxcIc7bbduD3gjL0CRQ5ahRo2w/lPRQ54Fduais6XuEVsLcQiqooAiGtJ7ORYMhRMhPIcPWlDno2asR2U3XKRjohC9j4xUh4YqjbdiwYdu2bfyza9cu9DOWG09K1B5JJ4X/Q4336CJBYhdBrE+dOgUL93nhmEFkQD8iJWi0o0ePbt26Naw5hT06adIk1DpChrmJzQ1FhNc53RFDgXdh6+tripi8od4b1+LJT3bv3u1xFuj06dMMm8huMgxaJgL2n/r5n3/+qaLUqjO6FJjhp86ZK0j5GclUGbvHWQYZ5CrgjQ5yC3U669oF9aUxxeeNfvE+bRgW//zzD6YY0w9KcOXKlVgPsGKocsWKFcUJJ2z7+y+2azcJyTxz5syWLVuck9nhw4f93GtHLZBPFU8rPmDmkBVKLHvsAEiaxx0GfMWcHdbkTQTI1WTwRkigz5sA6Qv9QlE+6geAQyH+TY0e2759e5KwUB0LFy4sUKAADLxNmzY2sWR8BTS/ZR2JSb3kgAByCFFMnTq1vkIXtNb4SBcSEja45cmTJyVUMnRu7ty5+lcY7oGrnQWckEhCrkEHkkmDIJZvvfVWzpw506ZN27NnTw8eqMOVi0ogopEjR8pHGxfl7WLZ285byr5ot27dgrHHIpweniqQjCJdqA6JL6W71QStU+KqlehoWbh0jZMcjBXXKlWq6Imo601XQ6LfNW3alP9dl2D8A9PFNVSSgvOMrhyP0s8BBWP3RZWfpHezMPXccMMN9K9TrhBpUcJhuahaUmQCFbJn89L0RliG1rt370DsUW0dsuUYiq25clE5K64iwymgeyV2euXKlWkNtUpr46IeIuSnkOaMblwhl5jo5xcYaLIloFLkZs2gNWb5ij7CQP0yBPxcBRR/JGwcXYPkAxREqCVn7ysKrxO4+osaJBqee+4511NPGCu6h6eBQcoDfFh27LNmzaqnHz9+PKB5DAatA8byT+JTr6BlVma1AMGQFDlHeuedd9oIqjc2btwoIXb08AFYtB5RVQQSTE6P2KwqlUwaRPyxITDOW/s84MpFe/XqlSdPHt3JJXC1p7f45dquk+nfv3/69OllcUeoO9a/7hqzYcOG1157Tf7XA8ZCLWj/wNVnJmFT+tkHOe6OrIaqSO7cuQsUKOBdWSzjQDT8RWHjuXLl8r7cS87I6KG/p02bFnD42Uq91MHysM1Ss2bNgOWToq9kMRYGDRok/4flojaPd6Fzij/s3r1bXVbnirAMjRzSpUsHZ9YPGCNLN954o+3mXh2uXHT9+vUkpkqVSqf0f/75Z8OGDc9YkH1ddchRIskpsfQQIT+FNFw0rjhy5IicfhdxgnPKxS2nTp2Cpm7duhWbSrYQLl++LA6ltDkP61F75CjvV199xf/x3GbwCcNFrxeUKVOmUKFCzhUOFIe3Nr9OYLhoEkI8cNRpNAWUYLdu3cxxfYPrAYcPH7b52gFMLjHsZsyYwQApWLCgbLz4oV6YiYst1KlTR0xt/td9H+JKvYKW61fq1KmLFy8uHGnZsmVjxoyJ4AAUtYiJiXnvvffko5wsdY1spwPDKE2aNFmyZHnzzTchWhUrVlQtlkwahByctzGFhRAk/YAS7BEOqU/NcgJWDxuLcXnbbbdlzpxZUc1jx47xKxVDDv0pDtgY923btiUdbla+fHkVHo/2199LL0h8crXzSV3Kli2rcyQ4icf1sBKl1uMERzBSLlqtWrXSpUsrQkjV2rVrZzsI6oTs6VFBRHTWrFnQVwRPjg2rHXi+InNbFD3vZtm8ebM4OzA8X3nlFYwoyCeZqL1B8XGA06o8ReSUmxKtqoceaNq0qWKAq1atkh1v2+1ZOrZs2RKwfG1UCkUKWHfhqhRxf2jfvr1K6devny3snA1ygYp+ba9AghfSApQT4R86dCivlta4dOmSeIL07dv3hx9+QE3VqFGDj4888sjGjRuPHj3qLUJhC+mnpgY6EEKJSLR+/fqdO3eKUyh9IUfJ5BIXEvmKB/jf9bqHa95f1CDZomfPngErXAeqc/r06VOmTBkwYEDt2rWVNXCdQ5bfwq7pGiQQ5F74SpUqDR8+HCN1woQJ3bt3f+KJJzzsHgODFA+sAbkNS8wvbFn/XFRdE6VD/0kE1AuMGDFCNk8iPifvRIMGDbJly+bqaGoDFFRsX1EX6rjpNd0gf/7557PPPps3b94HHnigS5cuEGymZhXPhh6n1sIqoUDM4OpcLiZ78+bN8+XL17Vr15dffrl69eo2t8OzZ882atQIAi+VJWcJQnPx4sWRI0cWLVo0YDltwi4gkChbspK3wMS+//57iASlqlWrFoJHGWDCuge+EydPnoT3ehsVkXFRoUPCxjt37kytQwU00kGlJBBDjhw51JWV8KJBgwZB2iGQkFVY4uuvvy5957NZglbcewmrFrB8zrt16yYMH24GvxIPfMRm3rx5pPA6EVo6UWKVVaxYsXjx4thgH374IU0BPVYRdxA/WF/A2l13rRQyL37mAeso7MGDB9euXVulShVJ6dWrl/KiWrRoEYXkYYpE17du3drj0DiMWla+AOKk33cKvenQoYPEyQtYkQL0WNZM1iJgOXPmRDwQZrmLjhHBiA4rQh6F9F9TAx2McRpKHbL97rvv1CoJ/8BL1VcMRteVRMNFDRIKzGeogIceeihPnjyFCxeuW7cuRr/HNevXFZYtW4bKy2yhbdu2oaLMGSQcEMWBAwfee++9zGelSpVq1qwZU1cUjV0Dg2sUqO4DBw7YbpFNWkCBohvQokePHq4hmlzBq/fu3esa+DCpEK0GgTpu27Ytrj7M4rrv4Tt94cKFrVu3RtBi8Kh/LUADKJifqAeTJ0+GqySE6t63b9/y5ct1w9oPqLUeJELHTz/9pAJGRAZM9h07dkQQDEKqwKxHvziDF9Bfc+fO7dixY3zKpgBhowXiHyccCUcGXMN58Irdu3ergAWUX93i41OEolVIAwEt+dtvv9GqchZA/4qPv//+OxNK4jiC+oThogYGBgYGBgYGBlFA69atY2JikroU1zBgbi1atAh7H6+BQYqB4aIGBgYGBgYGBgZRwJUrV1q2bBnq4hCDsOjYsaOEqDUwuE5guKiBgYGBgYGBgUF08M8//4wYMcLQ0ciQrA5PGhgkAgwXNTAwMDAwMDAwMDAwMEhsGC5qYGBgYGBgYGBgYGBgkNgwXNTAwMDAwMDAwMDAwMAgsWG4qIGBgYGBgYGBgYGBgUFiw3DRlIMDBw4k9Cv+/vvvL774Qr8K/PLly++8886OHTvin/nWrVunTZvmevFuIuPnn3++cuVKUpfiKpw4cWLSpEkJfbPzf//9t2HDhs8//zxB3+IB72ru3Llz1qxZgwcPnjFjhtzYnuJx5MiR6dOn6ynJZ5hEAIr9ZwjY7kA7c+bMl19++dFHHx09elRPv3Dhgu2HJs6HgYGBgYHBtQvDRVMIxowZM27cuITL/+DBg127dr3pppsCgYB+KfmCBQtIKVOmTPxfcffdd5PVkiVL4p9VPLF///42bdpQ5aQuyP+Pzp070zjdu3dPuFcMGTIkd+7cvOWFF15IuLd4I1Q1oRxNmjQZNmwYXRMTE5M2bdrs2bO7XrqdYgDrfuCBB2iNG264QU9PPsMkAjRv3jwQAidPnpRnIKV0dLFixVBo77zzzl133fXqq6+qHN5777127drJT1KlSoXmoUGQ2wIFCtSpUwd1lNxWkQwMDAwMDAw8YLhoSkCnTp2mTJmSCC+Codm46IkTJxo1aoSBGP/MsTvhG8lkv+v06dO1a9f++eef45/VP//8E/9M1q5dW7du3Q0bNsQ/Kw8MGjQoabloqGpWq1YNmqo+fvDBB0WLFk1WiwUJASro5KJJMkyiIsOUOX369FDHZs2atdCQK1euBx98UD02cODA1KlTf/vtt/Jx3759GTJk6N+/v55V9erVaZnKlSurFJ4vV64cifXq1TN01MDAwMDA4FqB4aLXPAYMGNCgQYPEedfgwYNtXDQF45tvvsFujucJwB9//PG1116LVpESGu+++27SclFXrFq1ilJ9+umnSV2QJACszMZFEx/z58+PyjbsyJEj33//fVvi5cuXM2fOPHbsWPl46NChNGnS1KlTR3+mffv2CABDSaW0atWKFBip/tjJkyczZcpE+rRp0+JfWgMDAwMDA4NEQPS5KBbDd1cD88L2zN69e+Wrv/76S1L+/PPP7xzATIl68VIY1qxZky5duiNHjiTO664rLgrq1avXrl27iH9+/vx52OyLL74YxSIlKJInF+3bty+lWrduXVIXJAmQ5Fx0586dN9100+LFi+Ofldrq1AHLpXOVBuvTpw8fR48erT8za9Ys28nt1q1bO7lo0No/J71t27ahyjBw4MDPPvss8jpEFVF0tr8Ooa9N+MR///2HEH755Zfxf/vBgwdnz5795ptvukr1tY6///575cqVW7duTeqCXC/AAF69evX8+fM/+eQTFMK///4btHzmf/jhBz8/1/3wXc1mLG3dx/7SpUsXL160Od4ra9wG/08mCQ4cOPDBBx8kdSkM4ovoc9H169d/eTX27NmjP/Drr7+qrxBrSfzll1++dIABE/XipTCUK1euUqVKtsR//vmHiYR2RqNt2rQJcwc73nbKDuX18ccfB61DtlOmTMHiVF/99ttvKMTJkyevXbvWdtrNlYteuHBh2bJlesrZs2f/97//SUm+/vrr6dOnq7hKWAOo2mnTprkGyOErXVr4OY8dO3ZMvqIiq1atcv7q+PHjKPG33nqLh53bmNT95MmTyBIW7YoVK6jvNxpOnz4tj23ZskVS/vjjD/XbRYsWUd/vv/9epaDosZ7JxFkMG2jGRx99lJ8/+eSTZPvdd9+FKpLPijBG6BFbxcWwpsyUKiYmxrVgmBSQzHnz5rmuWfBbuo+23b17tx8uSufqDXju3DlJ37x5s6RQcT+vRiS2bdvGP8uXL3///feZ8JzV/P3338lQmhGZUS/lJ1R2zZo1tjwPHTpEA86YMcNp34cS+FOnTn344Ydz5syhqLYwOXECfcp76Q7yd8ZeojzvWbApw6A1fBgskyZNogeVz6SCKxe1DROwfft2ETCqgFAtXLjQVXliN0+dOvWjjz7yuXrFW26//XYaf8SIETS7bv0zkHft2kW70RE0nRhPEaBFixYVK1ZUH++55x7nugPvJfGWW25RKaG4aIUKFUjv0qVLqNfRnv/3f/8XWVGjjig621+H+PTTT7t27ar0RlgMGTLk1ltvpcHjLwAM5Oeee44Rd//995PhqFGj4plh8gHj+uWXX86cOTP1YlJI6uKkfGDetGzZMm3atPnz52/UqFGbNm1Kly6dNWvWxx577K677nrzzTf9ZIKZ1759e5QbvVakSBHmaNsDs2fPrlu3rrjZo3KZp7BtmjZtqtz1mzdvzjOumft/MpFBwWS+oKGSuiwG8UWUuSjkAQ6JVfqrBkU4ASYLNg2mho2L7t+/n4+HDx/WfxixfXOdAJOdcTh06FCVgl7r3LmzzLjwmQcffBBDVjRIjRo1hCTArJ5//vmcOXPeeOONWJP8w7d58uSRHDBkmzRpMmHChP79+998881wXd0rz8ZFeUWzZs3I57bbbpMU6AEqL126dHfccQdTNVYmOcjEBiOFAPCxbNmyvI6Unj17yq/OnDlDLSQoi8x/CAYWA9YnKRAP6FzhwoUlcpLNkmDi5F1wb1qjWrVqZCJ2NpRmwIABfMVPEC0JAwPQ2lRf/scWVFQKa55SdejQ4fz58ypzCiZkUqUMHz6cFEyQsL0Dn69Xrx4P8+pXX331jTfeCFUkWfsMVRGMA2gYZneqVKmYRSRzGGzVqlVJIR2brGDBgrSP2Ot6OGV4ET8h54kTJ5In/WKb2yCBRYsWhURRnmeffZauCctFaR+sOin5mDFj1BLp119/jcA888wzQuZDvRpOSEqVKlX4OW3CuyQr+KGzmvv27evTp49UjUT+7927Nz9B3kjhoyoVmoePHTt2hMlTBr5t1aqVlM1D4JmSS5YsCUeF7XTq1IlChu1WJ65cufL444+/+OKLMDdklbINGzZMfUsnIgbdu3fnXQi5FEwt8UAa6bKZM2dCyylAlixZbJs2Ohd1DhMAiRWJYmwyMPPlyyfDH+nSF5Jg9bVq1aLpVq9ejRnNA8WKFcPcoeTHjx8PVTUyl8meIYAMQ9olHZ0gHryrVq16++234auMCH09yycgEsgMUiQf6S96n9ft3btXfwzTSoREjU1XLsrMksYCYzzUG5MVF42is30yRFR8jL3z3LhxY+PGjf3T0Zdeein+XJR5jUwwcoLWLPPoo48mn532aEHOwBsumtBgKsSqgXnaPFCYBQoVKmSz7sKCuU/0ZM2aNZ2jjxRmCsRVTyxVqhTPV6hQIWzm/p9MTGBwGi6aMhBlLoplzyjyOFfw008/8QBzsI2LwgT4eI1eVJBUkJl16dKlKoUGpIXz5s1Leu3ataEH8PmtW7cWKFCAFIhW0Nqvg/BITBQse2ZT9J1MzwxsdI26XAErk8egDSp/GxfFOF68eDEpiosGrf0uUjJkyNCvXz8hA7t37yYFE7lBgwZCVEjHfsX0lxAsGBOIRKVKlfT5j5JLSvny5WXPh2eyZcuGNamsZ4wAHqAd5CMixMeuXbsGre2mn3/+WexyDL79+/fDu5o2bYqIXrp0SQLGrl+/XhWbdFiBoqYKqO9MmTIps576UjWseT8dJNuM6oyuR5E8KkJ3nDp1ig4SPqYyl59kz569b9++MnBeeeUVUqA08gA/ZE6CEsvHy5cv58+fnwe++OILSeHtadOm1Te7GjZsGJaLCmRDABKlUmhViJCwBY9XMyOKASd8CVINhYDq0MWu1QTwJRIRZpUyatQoUqivSoEe9+rVS30kQx6A+Qc9BZ5xoSZ7ynzffffZbhbxA7gELFedjFqyZIm8V9oELgejUw9DfSnJvHnzgpbIUSQ1uyMeGTNmZMrXM9e5qOswCcbqgYIFC86ZMydoKYGHH36YlPnz56tnnn766fTp06vN9oceekgMHYi6tyuEsD79jC7FRsNA71UKQx45hEh70FpXQMXJ/PDhw/JRYjUBW4RkVIGko0n0UtFWiy1MmzaN8tB6iKV+0MCJZMVFUzCi5WOsw9X3ftiwYR5Hsm2QGS2eAtCxY0cy0U9/pDwwZxkumtAQ6njzzTdjCTi/PXbsGKaCPseFBTMpNpWoSlchx+qwZYiVyMMYIWEz9/9kYgKDynDRlIEoc1EhmTt27Ni8efO6detgQb///rv6Fgby1Vdf7d27l39sXPTbb7+FCO3btw96sGHDBgan2RQNC3GOcvrRVaxYkXT9FlBalZQ0adLIIUDaNpUFyKR6Biu8UKFC48ePvxKLI0eOiF5TutJ5Rpf+tXFRQErmzJn1lCJFiuimZDD2dgd9F6hbt262+Q9OYiPbsFlSoBbykZ9DA2JiYuQjJmzA2gFWz4vN/dFHH9maaOTIkaQ/9dRTKoVMXF1DH3zwQZ7csmWLSvG/YmLjoh5FClsRnreRNDm4eO+996qUbdu2kaJCksKRcubMeUVDhw4deKBly5ZBi/nAKJic9GJMmTLFJxeVNQg4j0qB2ar5z/vVAJuSj/S4LVtnNYNuXHTChAk6F6UpINVUX71u9uzZPEAF5QFXgacfeQZWrBYaZsyYEYFfgCwBqAPDkO2pU6fK/1Bf+Lm+RP3ZZ58xbOWELeYs1sYzzzyjvr3jjjuoiJ6584yuc5jwPyk9evRQKePGjdPbB7aJjaKLCh3EAzqfDAUnF+VFpGzfvl1/THx6GdRhM9SBZVO+fHn1cefOnbb9TwVGB+nqiL6UCrWDXEGzq1evjkmXKVMmBGzjxo0ebzRcNBEQRR9jhVC+9+ixPHny6ItiHogKF5VwzYaLGsQHR48ezZAhA41sixCug/koTre4YfLdd999cuwFzJo1y/ZAx44d1SEUgcyt+smvUPD/ZGLCcFFXeMffOXXqFAQNLrZp06aDBw/q6+9+wv0kEKLMRWXbE1DP1atXy/9Ka2O+rF27FhPQxkWxFJWPKCad/GP85sOiRIkSjEOnB5rQJ93LMWiZufqeGDYZ5p3+gOxnPvDAA487oGitk4vSg364KCrSVtRnn32WlLlz56oU2RNzclFxPRWIDarOCga1U1vHjx9/9dVXZR9VfSt3PzjP7J07dy5r1qw0gjrRWrNmTZs3pkBUsM0h1idcuWioInlXhEZw5aI0rEqx6WVsdOro7E3xppMtqSFDhjgL7IeLMmblEJE6Tkm91IEI71cHYwXpjTfesGXrrGbQBxedPn16wDoIYHtdnTp11GqXU+CB7DEyXvS1hrji888/J5OMGTMOHTrURmWLFCliCwlrg+p0TGosj2zZspGVnomTizqHiXBR3cK29ePhw4cD2jn8oOUd7bOjnVz0zjvvJMXmzyzrIDly5AiboYLsA+thitTil83hlslSzu7Kwcig2xldWhKmAZPnSXXT8sWLF1+9GgHrmJmeEl3KFFc4ne0hXaLfrly5wjQ6derUXbt2OX/466+/MoTpepRzBEH+PByYg5ahvGTJkilTpqASnY7r3m7qHj7G1Ij5nWypsu6WHwwXGsDD9x507do1d+7cfuKp6FyUTPhISXQfIgVXR3c6grfLEY+VK1c6S+LdbpHFaPCG9w+9AxAErRGHsPFzXbsGr+ai9CBysmDBAv8h5SOuaSivewaFjFN6mZZH4evr2nrmWDh06/Lly523XvkJP4HupXh0PcWjDLZFMY/Cnz59mhL6Py7eq1cvWjhdunT6bo0NSKZtivQWMOGiNH7VqlXJPH369DYzA6PL5qST+FyUlkdj0PgbNmywnULyqfpQd8gJvQDFMFzUFR7xd5B/+ciQl390j5iw4X4SDlHmolj2SD8mKaYq8oTpQGVEXzNW+V8Ocdm4KAOYX/GwnJA8efKkfOv0wDbQUbBgQcYh/N+W7spFsYlJVHcqOE1z2ZLSaZ4TUeei+tJdZFw0aHkNdezYEdMHA0LotPoqFPED/fr1C8SeaGXoQuxdqyynPeVQZVwRJy7qXZEIuGjp0qU9dLRcJYpCdxbYZxxdOSgr23EMfH0X1/vVwWhzUdkq9L5y05WL0mLFihXjtxCYZ555JuK9DuVACz8XIyxorXcEfBxqwhzs2bNn7969maRlwUg3aKLCRTHC8uXLp3M5LCrbSlAo2LgodoBEyLDRRakscIZfCgXGFM/ry65YUeLfbvPyoF8kc7Ejg6FjF0FLAtYBEMlB/dADZOWzwNGF09kem6B58+YZMmSghffv31+2bFnkQTxgFy1apP+WpkNfYZXCNPLmzZspUyZ0PsPETxAdbwdmDNzOnTvXrFkTMSbzKlWqQPPUaVs/buqhfIxRbryXIT969Gh+lStXLlkY9RMawOl7r9dIIszBQMLWXbgo6kJO5QhoQF0be/jYQ4F4e9asWfkVXEIviXe7xSdGgwe8fxgqAIEAJUPzNmzYkNajjygYU4k6Gy9cFBL71FNP5bEQsI7Eh+VaEdc0lNc9jAUVmjFjRiyKLVu20KoqBAY6UyczdC4lnDNnDoLdtm1bHiMHWezzGX6C9mE6mDZtGsIM32Pc6V483q1dq1YtKZKfjgPFixfneTrI5/PeAiYQLhq0FqrELQvZ1teJkpaL0gtkUrt2bYYbUnf77bfTnnLKzL/qwzSij+hZyCqGqHijGC5qQ6j4O0AoqIiuRG/mo6wMhg33k6BI2PtF5cguQoPKQP74Z78FJE9xbtv6qEACr6f4u+zjCYk049zSceWiMvuqA2xO0zwmJoYH9LArTiQ3LopljPVZpkwZUbhytNUnF2WYMcOh/rCqUdAwQNcqyxyjTgXHCf65aNiKRMBFsRSZbkPtmUDCeRhzyllgn1wUQ58GzJYtGwbKSy+9tGDBAvWV96uD0eaiWB6Bq71/nXDlokFrjocKpk2blhzy589PG3pk4oE1a9ZIVKFArJ+q7EbqJ2OdwLpl7KhRmUBcNGjFOcuePXvJkiURm/Pnz9epU6d9+/Z+6mXjokxmdLpOaxXSp0+P4e5/Vwc72BkDTPyQbfdkyJEN6LStVE4uKhwbqGPSNiSfM7quzva///47zRiwTjsL2xdXZ32lDBMfkVA+yRgTYnSi8MOep/J2YAZ169YlRW3X//XXXxKaWMVWCeumHnTbSz99+jQWpKI6EkEgS5YscmbeT2gAV10qEG2Jjetd92AsF4UaMe4YBdgholtUpICwPvZA6Ldt5cu73eIToyEUvH/oEYBAwPwLr1A/79KlS0A7tC9clC6TpmBQ0ywBKwChd6kirmkor3uUodwvjYqm/HQZhWGukWEiHvJgzJgxvFGXf1mgVPHt/MhYmzZt9BXV7t27q43TsN1EZSmSz7PiFEZW9BA/P88HfQzMoMZFg9YhRPFrqFixomrVpOWiEtdABfqSUyqKavpRfUxezD6oApUyfvx4w0WdCBV/B6UnzEuJBPSBj3J6JWy4nwRFlLmoOGupESvXtzBZSvhc564xOHbsmGyi6l5VWOp85dzxM9DRuHHjgOZDpeDKRdGbaHOPI4sSlbdUqVI2T116U13flNy4aP/+/QNWxGD5GCcuGozdRenXrx/zky1cioJ4B0U2Pv1z0bAViYCLPvLIIwErVrCtVOvWrTt48ODo0aP5lhnOWWD/94tKGA9+RTF0EuL96mC0uahsS3bu3NmWGxawimTjFHg0tXJ6pDGFBTldWMNCndNDg40dOzZNmjS8i1czcHhjqlSpnAFmxccbA1fET6UnHBcFc+fObdSoETLPG7/0fcWik1dIQ02cOFF/TPZFS5cu7TNbnsfycArAwIEDyYf+1RPRPyTqjrWhuOjSpUuFi4a6dSD5cNFgCGd7iRGtB1HLmjUrUqSsB7HhdC96OSDjZ0fa24FZWg/zTv/J8uXLZZlGBnhYN/Wgm8xg5SN7ugO5nEeYNm2aPBA2NIAHFyU3vsqUKVPY6guF0OMC0KqygySTWlhH96AbF/XTbhHHaHBF2B96ByBYtmwZH/ft26cyhMUxmhYuXCgfhYvqaxbiYe7nruzIaurhdS+O/ZAQXW6HDRtGIvQsaB1FprINGzbUiwErzpAhA9pYneYNK2PIcO7cudU42rVr11dffeWn8KqcYRtHlU1+7vP2cj8CFryaiwZj3XB0zZm0XHTo0KEMUtUdotX1QMFhVR/9lStXLt3SQIYNF3UiVPwdZhxhZKoNd+zYQYoYQt7hfhIaUeaisv+rVqeY4fgoq/6M8OOxwB4VIgrbvHDhAgNbji+Lrvnrr79k49h5TZ+BjsmTJzMOnVcCOLno2bNnUeX6ROI0zWGV4q5mc5fHfFF0N7lxUVnUVxQOxshH2KN63puLHj16FIP4pptuslEyHVgquqMd0xJj2+f1jHPmzOHtEDY90bVIYSsSAReV2TpHjhz6fEnOEmAGdcO3iIFOs0Wi/IS0EUiwmSxZsuiEKuyrg9HmohKai0lLN3+RTKwTZQ+5CrxEllYfGSMqGhMdzdTuJzBsz5499YtJZVlBjBhZLWI86u4Gb731loi07EXoTSdn4XRHoGhxUayZCGg2EFtcne0H8AebcAZjebX/e+ckuJRzF5qpIV26dNgceqIseejRkp5++mlXLgrnEbM11FWxHlyUGWrt2rURBFKOGK7KUwwy/WSUuF8q8oP9Grh641duDvQ+oy7wdmCWqCdqV1BAg8i8IEsqYdVO0I2LQoB5tdOBXNUirKr34KLB2NBWYV1GXWMXyUpW/fr1gz4c3YNuXNRPuwUjjdHgCj8/9AhAADm5+eabPfJ3xi4Szaxzcg9EUFMPr3tZa7BZFMKueREMcO7cuQHr1LStGEI11apZWBkTtx3YnR6B3E/hIwDtT542/hwKPgXMxkWDsTEC1bJCkvuLKpnctm2bTI59+/ZV33qrPrlg75FHHtEzNP6iTnjE32GwyEfZeoHkY6goP0rvcD8JjShzUTl8SzWoOdWTyugH1gU2f1GJr8tHbErGlRBaGKwJpesNjCd0t3NpTbioHpYGdlGoUCFll6PrxXa3uX+gp0RzYeSNGjVq/PjxlStX1lU8Znfg6shvcg1DpkyZlA0nBlaGDBn0ZUKJd6KH/BVrUt8AETtSd3kSG0vtygZjvV7VSRjx0a9Ro8a+ffvQ1HJWEwqEppOjy3KOxeP+N4h3wC3QrkCOWeoRSqFPUjs/0W5kq7lYsWLnzp1DqilVqCKFrYgsS+t2pISf0R1OhF7S0fLx/Pnzwm1uvfVWJjMoBBWhIxQ/bNasGd9CtlFYdBYDtnTp0qQULVoUquAzUgXkDUGyHQ4M+2o5rqOOkCk4qwkQwsDV4aOE6+pcS9zJ0qdP37RpUyxODBpaRnWrq8AjqBgEalkBbZM7d25FjwcMGBCwAu7ruweuwLTVl2+gmtRagl5gxMiJVuwbzDtkG5FWA1YMRHFXw4zggVy5conNIfuWZCLF1leCncNkzJgxpGBnqBRx5VUvompZsmShQRjLjHFMTMYUWtqPK4hY6tigSMisWbMoEiNdAsmohSS+qlatGl0QNjeFJ554wsZmFQYOHKjfEUr704a2BTIZLwiqUjvMo3LsHPPUGUBSIRQXZYSK/5jejAmNyLgo/M02RmhJBlfY14V1YJZDjDZDHNx7772B2HO8EXBR2f71Pm0RTy4qF2WF3Rl25aJLlixRNQrr6B5046J+2i0YaYwGV/j8YagABFT2lltu8fhhKC5qWyUMhchq6up1HwzBRYOxdA6mrYd+0CERv9XSalgZY3YQkwOgYdQOXsTd5AE5XWK7wSsUfAqYk4uiHoXypU2bFoWf5FwU0IyYNwznGTNmBK6+JNxb9clVovrdB0HDRd3gHX8HqRaOhgGpwhfJxpVHuJ9EQJS56D///CN7vopeq7vjdDjvdEHaMNzVD6m/n7B4BpDDggUL2hKFizLgmVk7d+6MmdiwYUO1M7Ny5Uq5KipguSuoYzyCiRMnQizlW6YrtaYojh+yDofJPnr0aJjt+++/L24kABP5awvCcMSqQ9yhH71795aUihUrLlq0iJ59/fXXmVqEp0FUeGbQoEEytWC1jx079rfffoNvSNDze+65B20LneAZiVtw9913y0kbyG327NmFHDLx8IzsOhYpUgSyh/Uj4TdLlCgxbtw41/MGKDjsmFBObph9vFHfBaW0kqeTRznBTCCzCMY0FjZWdagieVQEM4InMbsDlhMOHAmzm+flAdHmBw8eZPhUqVJFUqAccqYAiihWuwACoIe15C1dunSRG8mw/hESeBSkpX379p9//rnPlaCFCxfadrEEoV6NfnzttdekslmzZh08eLCEcYPkOKuJ1PEAZQtY5z9hUJRq/PjxMkXx85EjR8oiOkLVoUMHdbtayZIl1cmrUAIvBwGYzhFyuDdWCK2hai1nmANWOFDvFmAMYp4+88wzzLLQS0af7u64c+fOMmXKSFay6q+EDaUnLqaIBAU7duyYbBdDijCYMJFpNPlh8+bNV6xY4Rwm1Jo2kSOa1IUyX758ec6cORKpiK5UEfwREvFQ0kEvhD2siwIXhpwjRw7lm4SepyQMHMw7LEh4ESPa/9IhYk8X03ehHpg8eTLkigfoa+wMBEY1msRTUVXImTMn1UdloazKly+P5e29SBSKiyJ+YgnRRz5rEX9ExkVpipYtW5KCWYnZQQ9Sdz8WQ1gHZvGNdwZAknTZ6o+Ai6IK+MhM4VG2eHJR8TQLe0jSlYsyWpWNG9bRPejGRf20WzDSGA2uCPtD7wAEEgLdNVSHIOpc1GdNnV73wdBcNE+ePLyFSXb48OEBxwomkHRmXvnoJxQiuVFrdF3AWtmUrciIu8kDMGSppp/jDD4FzMlFg5Zmk1hiqEqeT0IuygRXo0YN2lzGl5zR9c9FoeIBa41Az9NwUT/Q4+8wmhRH27Bhw7Zt2/jHNV6xHu4nEQqZILGLLly4gCkM+fF/gD5o2TcwEH4oS+8JUbCUByx76JxtxU6d0WWyQdTiemUijQ9rulaueEVa9DpS5t27d/sPoIJq1rWhDgQSu02/c0KAYPfv39/mLxcKMvL9LKzEsyIewPRHGEId/Wdi2L59u9glVC2u90PQSs6DDz5fHXVQeNowlOuvDci5bJOePHkSAuMs5JkzZ7p166YfT3WFdC4dt2fPHgaO66hhNkUMnPqQ1oOs6sdgGHfO2zXjCWoKdYTcypro0qVLsQOmTp367LPPhtqc1IFxQCFd6/XTTz9FEO2JCiIV3ruySD78at26dR4Wc3RBX0C0EtOsiYyLBq2Vb8zKnj17wjeg6z6PUYV1YJZFw8aNG9u+le0XeUsEXBTJueGGG9KmTescmHPnzpW5Pj5cFHsjcPWVRaHgykVl10tWRsI6ugfduKifdgtGGqPBFWF/6B2AQNbmnJGH1cGlqHPRsAUO5XUfDMFFSeSBChUqBGPdX3PlyqU7lAZj90XV6ZiwMqbKwFwgR5PEAT7ibvLAoUOHZKldUWUP+BSw9evXO7lo0Dq8JgGNZQFL/8qbYaKo1eEa/0+GQuXKlVECyhaKKxeld2RJVDdRDBd1wk/8HblZM2itlfOVREH3CPeTCMVO2Di6BokAiIRcKqVSXGMXGTjBGCtevLjr1j1gRmzUqJFzWQTjuGbNmrqHvUGKBFz0sccei+DyxuSGXr16NWnSxPUrnw5g1wkw1Jzu9wmHyLgoNgRcIrIryL0dmHfv3p0uXTp4o/4t6g5eocKf+OGiTh9jOT4Dc9APyS9ZsmTQoEHyf1ie4Op7LxA/EeWL7gFXLsrogMfKkkdYR/dg7KaiHszCT7sFI43R4IqwP/QOQDBx4sSA5UCxY8cO9dsNGza89tpr8n/UuWjYAnt43btyUYncI+sdly5dkgM1No9KyE+JEiWUaRRWxpo1a2b7OdwJm95PNyHYlDZOVoH4aGTMmDHUoYYtW7bQLEHfArZixYpQl8RQNokVb+OiTHAeDLNr165qM9b/k64Qb8/06dMrzSa+BroLmLfqo4WFUc+YMUM9sHfvXlKw4jxefb3BI/4OFu/WrVvV9gC2jTiUivbzCPeTCDBcNCUARdOqVStlNBsu6g0mYHGWYzKg3Vyf+fjjj5966innRtZvv/2GWe960bZBSsLJkyebNm2aAq6VYgpPlSpVjRo1bJsGQcu+9Lm9fz1g0qRJzmBaCQqnsz3/iPOC2kLEehCnCbVkJqfHW7ZsOXToUMocExPz0Ucf+Qz07e3AHIwlY/p9P/369StYsKCKNRDWTT3o5mPMM3JEHMr6yiuvYIZCDKpVq6Y2ScKGBnD1vRfwTODq+KihIGG39PUX5gIomfJODOvoLq7XPGCbAsK2W8QxGkLB+4feAQhgd3IUFjLDV0hUhw4dypcvr6iUPK+fohdPfo8gfwqR1dTD6164aEALX8fcDa+WcFMCOCFUrXTp0qoK8HBqp0e8CytjZcuW1W/sRP+rO1fCdpNsGxYpUsT/qRbqJS7uN910E/KjNxe0gWHy6KOPqj3PsAIGRowYAWWVzWQnpkyZ4uSicHXZ/tX3viAq69atk6s71RkK/0+6AqkQB6u+ffuirOCTCGfAikUE2zl69Kgf1SdVyJAhA0oPGTh+/Lhc/07Ob7/9dqhNhesN3vF35BIXEvmKB760LhSVH/oM95NAMFw0hYA5VZbQgrFaI7IrMVM8lDERsDwoXGM103QYea4HxTHo43rm2eBaxOXLl6NyQDo5QAxTzIjXXnsNI4AZnX9q167tPH9+PcNnsK5owelsDzWV6OIBK8AmhgIpEjUX1KtXT5YXUfVyIYoNTZo08XOYysOBWbBo0SJsXGxuzN9WrVq1bt1aHZP26abu6mOMiSOOzWI7duvWTWgD6tRPaACb771e4ObNm/OYH78e7FdaOG/evA888ECXLl2oHaPAxio9fOwhKnJNd8CKfcAcoU8fHu0WWYyGsPD4oUcAAlm2OHv2bKNGjcQVH1Bg2X1CGFQ0h9tuu02CC0JEZeMxffr0NL6HmEVcUw+ve+GiEEsKibB17twZIvryyy/bisG4qFChApIwYMCArl27QuQkEkHQt4zRp8WLF+fnlOGFF14gB90Q9+4m2WINeAZKdAXmPqwsbdq00EhKwksZnpSENreJtIeAffPNN9BUCZeA+Rfq3O/zzz+vuCj6R/izgObNkycPPZ41a1aVKFc6+3/SG8iSyBt2F9MQg1EsMTJnDPpRfUFrOUl+lSpVqpIlS65atYqmY5BSyERW4MkZHvF3+Adeqr7atGmT2nHxGe4ngWC4aIrCrl27OnbsyFhlLrnvvvuwM3z6zl1XGD58eIECBapVq6bmKgODFIyLFy++8cYbGGowBIzRunXrDhkyRD/uZXANAa2Fkj9y5MiGDRuWL1++YMECLP4RI0ZgyOq7Ot4I5cCsAMuCtTr30n0ilI/x8ePHeW9ky3muvvdYS8x3NEWcskL4t23bZtu40xGxo3tk7RZxjAaPH/oJQID5vnXrVj/xtKOFUAX28LrXz+giPxg5Hq0ktY4s8qX86ty5c7TJsWPH/BdeAHGFKHpvD4YCL4UhLFu2DAbuHQ46PgOTlgx12VXigMIjhIpjI356MEWf4Oc//PCDdNDly5f1nWEDBY/4O3xEsyFmruw9snA/8YfhogYGBgYGBtcAJAyJa9jDpUuXOm99SPGoX7/+uHHjkroUBgmIUHF0kxtgWc7wQgYGBn5guKiBgYGBgcE1ALmYd82aNbb0c+fOdejQIdECVicT9O/f3+NmIIOUgWuCi27evLlFixaJucNsYJCSYLiogYGBgYHBNYCVK1emSZMmY8aMrVu3njBhQkxMzJgxY9q3b9+kSZMITrtd05g4caKJiXA94NSpU3DR1KlTe5ypTnIYZ0UDg/jAcFEDAwMDA4NrA99++22LFi2KFSuWM2fOChUqQETV1R0GBikMy5Yte+yxxzJbqFu37pgxY5K6RAYGBtGH4aIGBgYGBgYGBgYGBgYGiQ3DRQ0MDAwMDAwMDAwMDAwSG4aLGhgYGBgYGBgYGBgYGCQ2DBc1uAp//fXXggUL9CueEx9Xrlz5+uuvR48e/eGHHya3WxB//PFHSpW0Zfj333+/+uqrTZs2qZS1a9fOmzcvPnn+/PPPkydPNgEYooU49Uj8uy8C7Nmz5+OPP1Yfk0oA5syZoy61NzAwMDAwMLjeYLiowf+HM2fOtG/fPkOGDIFA4Pvvv0+qYkCG69atu3LlyrfffpuSFC5cOKlKYkNMTMw999xDke67774kLMbQoUNvueUWivHmm2+qxFtvvZWU+ATSfPLJJ8lh2rRp0SijQdx6JP7dFycsXrz4rrvu4o316tVTiUkiAPBhXpo3b97EfKmBgYGBgYFB8oHhogZXoWzZsknLRbt161ahQgX5f9SoUc8++2xSlcSJTZs2JTkXBT179rRx0ZEjR7Zp0+aff/7xn4nt4U8//bRBgwY///xztAp5nSNOPRJB98UTH3/8sY2LJo4A/Pfff//++6/6eOXKlaefftrExjQwMDAwMLhuYbiowVXAPE1CLoptmjVr1hYtWiTJ28Pit99+Sw5cFBZq46JxBRWB0EaxSAbXFhjgNi6aOIB27tq1K5FfamBgYGBgYJBsEX0u+uOPP353NQ4dOmR7Zu/evfLVX3/9pRLPnTu3ffv2r7/+ev369bt37/7777+jXjaDsEhaLnrgwAHebrioN+LJRf/7778nnniiUaNG0S2VwTWEJOGi33zzTdq0aXfs2JGYL02GYAD+eTWY7JyJ58+fVz+5fPmyns7z+m+dr7Bl9c8///ArWyJ5quf1DAHzsi0lFK5cuRJBC/DqTz/9dM+ePRH81g+OHz8+ffr0hD5ocPTo0bfeeotJIUHfEhbbtm2jMdXHKJYKMVi8ePHhw4c9njl79uycOXPiE9YBw++DDz6Iaw6bN2/+4osvPB7YuHFjTEwMwyrigoELFy6sWLFi5MiRS5YsoZzxySr5448//oj/uRgEb+bMmbphb2DgB9HnojDJL6+Gbcr59ddf1VdMZpLIMFizZg0p8hd8++23iXlo7doFRsPy5cuZfj766KNTp07Zvlq6dOnFixexGL766qt33nnH1Sft5MmT8+fPnzVrFj/3w0X37duHunn33Xd/+OEH21e8iEkCO2DhwoXONQiP8jBnYKqSLW9/9NFHv7GgVwdRWb169eTJkz/77DPnvHXixIkNGzbwz8qVK5nYxD77999/ma6oHf/v2rWLUql68Tps4mnTpiFv/tszLBflt0xa1I46fv755zSRs8F5708//cSTTOGrVq1S6b/88suCBQtmzJixc+dOZ86YklScFmM0uXJRmgsLTE+hjgyiKVOmzJ079/Tp05LImOrWrRs/f/jhh/kJnaWeP3DggLPf6WLak0l9+/btznmd/Pfv3y+VomyM/VAtI6DjEAzalsaxTVdkzqyPkYp+mDp1qq40+J8CUAvMLI/M6R06Lmh5PtOSiDRZ+XwF8vO///2PRKpA39ly5luxe+gFHps3bx76Sr76/fffSaF4tncF3Xpk69atiASGI31te972sM+RS3/xFYJ67Ngxj5YR0PWMEeQBmXflojYB8Ggub1nFgGMY0suffPKJIjxISO7cuXkpYk9lVXQ0HqABbTl4qxE6mpyDlhVL3VFc9LjtGY+mTnIgPF26dEmdOnXAwgsvvMDgQr8NGzZMXMHBgw8+OG7cOPWTr7/+un79+qRnz5590KBB9GObNm1SpUpFSpkyZZxD6Y033kBN8e3NN9/cs2dPenbChAnVq1eXzG+66SaUgChMAYZ7+/btJcOqVauihwcMGCAPU86sWbNmzpxZPmbLli1LlizyJKCR41R3yta3b99MmTLx24QIAofl8Mgjj0jZnAM5uqDFeMvQoUMT9C0eYP4qVKiQbfU2KqViQLVr106CRyB7rs+ITIoYR+brfvDgwSeffDJdunRxyoHxLrVm4Hg8VrhwYZ5Zt25dBAUToJBr1KjBHPfqq68mhzXohAZKo06dOhH/nDmoZcuWadKkoa2Sm8o1SP6IMhfF3GEywIz4VYMinEGLHmCIoCBsXHTLli183Lt3LzkwhfDM2rVrnRaGgQ00db58+bBasGZQzVgqEpQSK61r167YDUIsy5cvX6xYMdQEs4tNO0Np7r33XsyCZcuWoYlEy4fioljebdu27dixI0Yesx1PYlQpioJhWrZsWUwlunLgwIHMMZ06dZLInGHLg/WJxu/QoQMP3HXXXa9aUMVYvHhxiRIlsH3hY61atbrxxhuxdOUrjFFM6rRp07744ov9+/cXK2T27NkvvfRSnjx5+B/aw09KlSp122238ZFnoIKYehRVjOOxY8eGbU+BBxdFET///PM8zwPfffddgQIFbrjhBv7HaBPSCLsg2wceeIBEaJLYhXyLrcy3lKF169aTJk2ibUl/7rnn9A0H2rNIkSLwcP6hibA+FReFZNLUfGszGhhKvII+ovrM9xkzZqRNpI+effZZHi5evDgtPGLECIYkOdMgJA4ePFjlAG9s2rQpsws58EDevHmhr1gP8i0FFlGBWlBy/sfA5aOH7x/dR9t+/PHHjO5q1apRC6H6tMArr7xSsGBBfg6F4EVSvKC1ME+r9ujRg5bBLEifPr1rcB36qGHDhjQ4XYM8IB7IA5lgQ9Ni3q9A4SCxFStW5IfwK9qBvoP+Sc6rV6+uVasW9tbjjz8OZSpZsmS5cuX4CGcgz1GjRlFxUuhHMpclklA9Qi2aN28OJYPW0g7SUM6HfY5cik2zkyElRFqkOrVr127QoIFr4x8+fJhhTiPwPFJRuXJlxUWdAuDRXGFlFZZYqVIlumn58uUMOmrKUCJ94sSJd9xxB8/ToQgeRGjXrl38T01pT72oHmpk9+7dTZo0oaNREfQR5qYIIV2mr0+5NnVyAy0sykqtawCUsCTqIY4FonyEhAtGjhwpDzNInfmjkRBL7EuVcunSJUYQz/fq1cu1SHQH7Sn6vHfv3jSdEjnGrLxL9BUys2LFCkjp22+/HUHdJVBWAgUkp5pogETgoshn3bp1I9jnj+Ii+7vvvmvjohGXygk0hgcXDVpiIHNoxHHXEDYGb9gcbC0mcQ29ueiECROaNWumHy6IK6pWrYq1I//36dOHERFxVgrJdn+FrhSF79xg8IZeI3ozV65chosaRIAoc1EMKVShhzRDA3jgxIkTOhfF4uR/jCRzLjeuwCaDYsn/qF1MDax8+YiBKNEyn3jiCdk2gdHxEata/Xz8+PHQJ2XGYRXlyJHDg4s2btxY18iYp2qugldg+r/++uvq21mzZvEt84H/8khwICwV/aUYPSRiDKkUWfqdMmVK0LLmZaMPw3fRokXYuE899RQ2K1+RM+kY6AcOHAhawgmFwExhqhZdifjlzJnz1ltvVfrUoz2DnlwU0WU2pQV4gOJhT1NfeJosE1IqXnH8+PEKFSrwsWbNmhjic+fOpaiXL19eunSpTiFggDyjyDbMFmal2BGAlSkuir1FttKwymigXswr2LXykQewSqk4Vlow9nymOqPL/EHfwS50LkoijOLRRx9VL6VJYZuYqmoTRjgt9Gzt2rV8PHLkCK/InDmz67G9kydPUgZlM0ES+C18I2hto+3fv1/Mxy5duiAbw4YN69evX9AiFWp3iIaCFJGJ08yiEWCSsgtEFTCXaYHu3buTQv/Sjx6vgBIg82pRjH/uueceGlzt+G3cuFG2gzCAJO7O8OHDhZspYgylJwXrJ1SPUGY+qtNuS5YsoQChHvYzUqQMas9QmOT777+/bds2Z+NTfXgFvE6lyEKScFGnAHg0l7esIlo0ptAVMG/ePL6tXr26fJQzF6r70DaMgoC186YyDKtGaC7p6M6dO4s8v/jii6Qo0hWqqZMbzpw5I/tO8+fP19NlpQmeb3t+/fr1DGr9bMLKlStlT8m2oKaAZpO1GAVZngtFzqdOnYpulP+7du2KglJf2bioYNSoUZF5CojqSLjLsWTZMaG5aGRAHXmTqDgBGQgkmFeLDFgPLhqM1TzxiQHuJwe0k/7xgw8+CMtF44l9+/bZFmfjD+YUfW0oWQE9KQM8Tq3qFGZZcDRc1CCuiDIXFZKJNbB58+Z16/4f9t4E3qbqjf8/5qEoShIqUxINotGQeYi+qZQkmUJC0ddY+JsryTcZQpIpIUOZCSGZM4XMY2YyXUXo/N6//fyt37L3Ofuee++5l/R8Xvd1X2evvfbaa3jWWs9nr2c966e1a9eePHnS3EWLRaXevHmzkE/DReUp4qOdoPLyOJpEAg39/yV49NFHYSbmMnfu3PYBCXAJxgUhZkHn0xfUKGfOnHJJ00BEUfftBGFu4bgoOhM6ur3+MHXqVN4u2oksabrGIBmYDI/yz08wFBdFDEgE1dxOFtojlmMiXRMmTOCp6tWruzLMKEm4vZcGNZoQ2zJWyms0V//6jNVGt0CBAq5KeOedd+wSoUBzOWDAABMB4oGCSN1euIzhw4cT57HHHpMIqPKFCxe23yLrIbYWCKe1lYYmTZoUKVLEfgTWV7t2bfnt4qKCQYMG2VMvLNqrLEoTC4EEEAabhwB4OyE7d+701gwU4qabburevbtc0oKu9ZyCBQsSYju2YRxAPBgcTM3UrVuXOG3btvWmD4cJOCvqdqCYKZqlG+8ryCravGs2lbKbbxC0JpcIhokA3yOkRIkSJkT4ar169UyIq0UmTZrE5ciRI+Xy4sWLtnGjK3Iwgp5SqFAhOq+5lIWCcItUNCs91zYzkQzbNrouAQhZXf6ySlflEdsnFhEQM/M1wcVFBVmzZrW5aCTDSOrUqbNkyWLuLlq0iLtGvP2r+prCq6++SlYrVqxoBw4ePFjItmtJR0xF7BB4CIODrDEiHgsWLHClz3Aki9IGQtLCEUhUfDNSIQn2BrmQXHTr1q3xOwTo38xF6ewlS5aMVmr/Bi4qg5sdkgRcVL6jRZGLotzmy5fP1YWvHaD2iCly+vTpI99s7BVm5aLXAiBWP3tg9sugLEHQ5Iz63bt321SL3yhFhHOXOLLBLWkQZS4qy56AkjA1ym8j2cyLixcv/uuvv1xcFMXU9QiAx0Y3b9clzAEJzLuoXDc5MHdFo7U3emV0IL9lwWHEiBF2gj77RWEOefPmDZeTHDlyZMiQwRUodmgdO3aMJD/BUFxUvBmZr/UGMoEJq5RVo7feessVx8tFZfHHXisQTc5sm/Svz1i5qCxn2UbpiHHAsm+UNRwybCLI0hAD+tNXQqi1cDZjKSTw7hdFF7GVBvgzOn24TIbkop9//rk99YqWvHr1ajuO6D2GgwkXtfmP/2Zjs/jMACe70Z599llzV85utWdBGDtE8WkPDBm2IYzR1TSffPJJwDEKDfeKL774wrtMdO7cOdgRyr2M3V4uumvXLmkyEyLnZNqbbVwt8ttvv6VJk4Y027VrJ+amNlyRgxH0lEyZMiVLlswYkvAs8e3lRBu5c+e+++677RDvflGXAISsLn9Z3b59e8Cx2Q6Zh2AYLgptsLloJMMIXPS2224LVxb/qr6mMGvWrIBjqE83N4FSHDBs2DATiIpAI4p9h4FwUcp4//33BxwTAJebGYYjb21HyEVdCMlFY8Xx48enTp06cOBAsmrb8tlcFKGC0E6bNs1rvkhPnDdv3qBBg7zbywUMUDw7evRo16Zim4vu379/qQWTDsrZli1bTAaYFLxmWUT+6aefBg8eTClce78FVLi9iUOyJCYVNBYtOGPGDKPqMbm0bt064GzxlcyY6YZHhg8fzluQBLOVOhwoF7klV0yXIbmoN1dknsYdO3YshXUVRDZdM9iSVRcJMVxU/CDwRteMEAzPJMkbtcpMF5KWMISOHDlSNt77c9EJEybI4r/UmOTQ5qK07xgHXgZFE7u6TCT1TJZ4EaMHr0BQ5b32mgpp8jryL74SbCDDIrHjx4+3ZZK8ya6c+vXrkxq9kruSsjHAoeNLiPkEKUBKmQiQIipz0qRJRmZi7R2Rg/RR7XiFHOnXq1evWB8JJ8yGiyIz0ndcohh0bNnEloqnaA57k4K/2PjfVRgwSv/ggZgR0V/kkn4tPzZv3ixPIQCMDxJoHPdE4ooiKogyF6WXIi5bt25FLsX/BIVhRAg68sdvGQddXJRuKZf0Om4RRy6NwxWFD5jv0dJatmwJ1UdfsRVWf41WRlvXxiQfOlGoUCGUnpB5oB15KmXKlK7VbFFwzYplPLgo00bAMvMzEPVdFhgTzkVtA2Cf+owHF0VTDDgWnnLp5aJMWoTI0OzF7Nmzues6f8Wfi/7+++/8bt68ebhMRsJFZUXR9UUcdUFUXrmMKxcNOrtYaZQePXpIQ9tcyMt8mjRp4pWocAjJRadPn07gc889F+4Vsmrt/fgtuqwsCUbORW2TZi+9RBEUperOO+90dbp4cNGKFSsSYcqUKXKJWs+l1xFX0NFcYTuudfL4cVF/WZ04cSJ30ZZC3g1GwEUjHEb8uWjQt6qvKaC5ynY7u9rR8GTrNTq6CaRlixUr5npcuGjQ+QQsO9VpZXsx8Opy0X79+pUuXRqiSBPkyJEDZdfo7sJFR4wYUalSpbvuuks2hrg+OIprnD59+jDOZM2aFR3XdpRFkekC7du3pxLefvttRMh8qgheyUXRdFu1apU+ffoPPvhg3bp1BHbp0iV//vxEQK99+eWXZWN/wFnet9cBGHsLFCjAFIPGz0CBWLZt21a+T6HeoGQzAgSs1blPP/2UMsqsxIidM2dO2bJRp04dicB4IlMSYimr3JLau+++i/SiJlHJTLJe82wbaPZ58uShWhYuXEh+ZNOHcNGQuQo65pcMjHPmzGH4ffHFF/Ply2du0eJIIKMHb6fpaSa7kqXDwhZkQ7ugZs2atox5mSQ0j6Q6d+5MhSCQGTJkYGQwd6EotD7jG1LBWMEPaayQXJQBgcaSzQJSY/L5wHDRDh06IDyy0ZH/YvqB3kiHkia2194jrGeUWF4kG3yoTHmvZI/2QtiaNm06cOBA2Z5Ammawoq/lypWLV/OD/8iVMb9nJrITpJnIquwtMjMLT0m/kE5NRdGDpHqHDBkiikrg8vd3/94RV1CTH3/8cfDy9mNEN1b/2OGEWbgoLJQfNIFsQ5DEg44oMh0zOCOxdBMpkfRcf7Hxv6twgZEWLXfv3r22455LDoSCiuMPcQjKpXwOQHWURUHCkWo6AnN9ki0KJu75omJ8S9komCz7bnfAmChsE2WLWpB1UfvD5IoVK7h0fdNSeMFMzMBhdgbGiYvWq1dP5mM7QR86wYtQkkJmg4YTbzGub42yi4+xO5L8BENxUcSAEAY11xtlHJ8wYUIwqlzUvz7jwUWR/BQpUhQtWlQuvVxUlubCmRGKY2GXbxJ/LoqWFrhyb6ELkXBRUWjsDWNBx6ibwIIFC8plXLkoEyc6jVjwynqvPxeVtdkIvcyH5KJivWk8tXhfIVZJjRs3dqX24IMPEi7fwqLFRYOOYcgjjzwiE7C9iTEeXJSxEd0L1QedICYmhvjhXGswIZGUbWoejC8X9ZfVYcOGBax9m17EykUjHEZi5aLB8FV9rUF2NRuPQbDTbNmyQdIk50YA6tevL9vjbRguKr/Fo6lhPsGrykURFd5ulmtQRnn2hRdekEvRuRlJROYRYGEOZgkFASDE7AeRBWQSlLXTs2fPoukaM2zERqi4UcdtLoouhUJvvv1L4tK/ChcuzFCPDk1vkm265nuHGBrYcweCHXAWyoKXt1i/8cYbLtYnwztkT1xDMxEIOzXtKAOFPXSQMUKMKTU/XHsjbdDZEX77c4+8UbhouFzBNtHg5Tct8sQTT8hvujZzU6VKleQS9dQ1L0iHpfZoFx6EUIlPtTZt2pg4Li5KHkqUKGE+ijGEojOQZ+P0jlEdLmE0vQMHDghd8bHRpbMHQtno0spwQuk4Mll88MEHQefrG1Iqn1MNF41TPQcvGwa7TGphnrZVjnwIMLMk5aIs5i7j86233mqWMb0Jyl4Pe2aRoUw6tTiYkG0vxYoVowPOnj0b+ZQVXZ/eEVecPn2aGpbUzp07Jx+Gxo0bF+uDXmEOXuaiqB/i9J44DOnMXMJUkQdZAhFvC5s2bapdu/bcuXP9xSZWoVK4gHiHNPRgpBWqZex1xWus9D5ZFE2IvX1CEGUuKpuIzIciOb4F5i3uc72rxrIEzADKDyi4eVAqxWsCobBB1dEnjVePYBy5KHpnwPFNYqfpQyfEyMS7ziAKhOwucx3PMGTIkMBlJ0Ox5icYiosy7gScpRKXU+WaNWsSLl9Jo8VFY63PeHBRcbVidhJ6uaiQbdeesaBDNlatWiUqUaFChexb/lyUCSlVqlTp0qVz2fqTean5SLio7Gt955137Dhbt24NWF5k4sRFxTWCkYRIuKgQRVEvbCCBXtvLkFx0zJgxAWvroPcVstPY26DwARQ4O+UEclHZJB90ptVBgwYhz2nSpDGliAcXBQyY6JFI1Hvvvefv65JpG6JiH1AUPy4aiayazy4GkAEpeyQ2upEMI/5c1L+qrzX8/PPPwvFkuYOCFy9enB+yEiWfUSgOSq33ICubiwYdT0KSVP/+/SXkanHRvXv3MpCafhd09F1k1VgdCxe1zbnbtm1LCEIol/QIxmqzLdm4xpWBunnz5tSPvXgOe0csjSGl4aLz5s175plnvA75W7Zsab8u6HzCk4Nq5OMXcmhvzw46jFdO3GGSkpDRo0e7WJ+MzDZdYXq1GZFXfRfDH/v8Hh/XxJUrVzafLQRi+mHb6LpyJbYGjPbmKZM+cysc3h7k6VnmU2Pwcoc1xhcmtzAuMyy4uChVetddd12wUL58+cDl7QPLly8PeLYFMWLEj4va+1CEj9n10KBBA7vm41TPwVDUkbaDujPWmaKJBzgz7D/11FO2+YmM4ca4z5ug2BnZM4v4XbM7tfSLzp0723nz7x1xxaefflq/fn1z2aZNG5KCZsf6oA8XtQ07H3vsMbt9paWoK/spf7Hxv6vwAp0c6o56vGTJEjodTEq+iTBCCiMz696IHCHyjYan+P3bb79B8gnhcVuVTWxEmYvK+q8xlEdYuVyxYkXQ2SR24DIoqhBRJgC0BEZ5WSmWAY5qQs3iMk5bU/6FkFnH5k6M2jfeeKO59NdoFy5cyN2bbrrJttcX2z8xq3ZBPgznz5/fPuaR4Vg2W/bp08eVmaCjc5Alk36sGra4VHHpQygTtiYqIBvmg260uGis9RkPLjpq1ChUHPM51stFSZNXBK50aITe+cILL9AvqDo52c/2oys+VI3dS9BDZsQcCP3DfP1iumJuFm8osusPtcbOuYuK0KZkG5XOfNYNXtYAzIQXJy4qmoFpRJnGqlataiJ4mY/42kXvsQ9BJXHX1xNBSC7KFJs9e3ZjUeZ9BS0laqt81BAg3pTdcOCocFGqTs4+FQjNNj5v48FFIXg1a9b01kNIMPGTmu1Hl1nHVf+RcFF/WUW6RFm3JRNaYjpm9erVuSvTgYGLi0YyjPhzUf+qZsa51lzaiMMzsX2oVq0axJsf3bt3J5BiMhuOGTMm5FE9Li4avCxI0G+RpavFRWWF3Mdo0Ou7SCYX0+myZs3KCO/dKy4tC0s0S6whIcUkGwwIZgy0Icb5DM52oBiDfPfdd2JKUKpUKddTcoiR0YC9HnSEi9qdSLY6G9LrVd8PHTokRKJp06b+PmPQoIjmkgTvflFvrmSFsGzZsvbisMCspKGk0qnpiSj95q7XdxHTgZzwZAJdXLRGjRq33nqrt+HEXELWbF2+vmP1XRSOi9pllK/Y9mcyl4xFXs8CL3UcNGgQ84K3aMZr2t8Ogo4GO2HCBDmrxqzdxY+LuuRH4N874gTxDWlvA0Z7FwsL7z5PF3y4qL2fU7QRk1rIHc7+YuN/V+ECndQs9Zltn2JqyzQtlzKMMzaiWJp9lBLZPCKs1fsNNJEQZS4qxrcUgJJTPCmPd4+4a79o0DkxQnbTMoFB5fnN/2v2LKZrBHIYHdohFc5Y3KJFCxm1ZSs5EZ544omA9R0XyWOUSZMmjflEKsyT0ZBBEDEdN24c1DTgGHrZJ6EL0OFkYwZvYUDv3bs3jxvLQMbfokWLoibScBKC2kdqtrFHrPmBN8qsab8X1T9Tpky5c+c2AxwTTObMmc3RQbL8ZaYEA0oRuGzHKxBt2LZxQh0nRAbxWOuTYZpLdMdwLSJc1Mx/dGMi21s3RZuxvZKAzp07BxxPmOgZKASoMgzoZrIX5slYPHv2bGqMjMlROo8//vi3334rccQbsDl7EOor++UKFSrEZIZee//995u1JtQOqp0Ejxw5QivLICW+ee2DB8V60Pj1oc8WKVLE5oHt27cPXGmTKadWGgGwIX4OHnzwQZgwBRH78Lx580IkpB3z5csX8PjgFRJF60NlmY/ffvttUgjp200YI21nUiBlLu0DM0K+YuLEidTGs88+a1g3Ko6tworpmr1cIGTe3jstq1vG9bG3RVCebPJPE+fIkcOY0LgiByPoKcWKFcuWLRtthPpLzYwdO3bx4sXhWBYtEnCOTunfvz+Mbv/+/aJlotMY1xFeAQhZXf6yKs54A86pRajsNDo9wmhjQgBIAVmSRTPqXPZGmnXLWIcRqoL4GTJkMO0l3yx4Y6xVTRUFHGcbIWvpakFWV9KmTbt9+3YkVhb39u3bJ8t0kydPZpgN6XLWy0WpWLE1ZeD67bffvFz0zjvv9OGio0eP9o6igjhxUUY8r+TYCMdFheaJLYxtCGpD9sOHy6dAuKh8TLE//BmE5KLyvWzIkCGydPPII4+4npKvb6+++qpcRoWLBh2bEbFTZUz28fk8f/584pBJOzASLsoAK7woZcqUdEnXKEEzMa6+9957O3bsoN8hIeZWSD+6siTFW+TSxSQROZtcuVCiRAki29+yvSl4ETkXtb8GemUswnoWeKmjfNr2/5J1+vTpnj17EpOhRr4nmj0m0eKi/r0jrhCHFPdcCdkoAQP0fzZOXNTeBuXlov5i4393ypQprvyHXEr59wARpTusWrVKHKGjLwnbElYpVAsVd/Xq1cZ9kawfCC9FdE+cOBETEyMMzighiY0oc1HYo6z5Ciiby7OfwMtFUSxgoebBZcuW2Q7lFSFBpYkWC8qVK4f60qFDBxlqEbIuXbrI4ZZQOxoCjbBWrVoSGUYknhup/5o1a8pnsHTp0kF7mH6gOoynIRvObGAIOL6/0V/tdTP6AKNw9uzZYaoQFd5rTPzFY4RPfhiyUW3FIST5Ycq0P/KRGabA/PnzU0DoUJUqVYznycGDB8ueHKYZ7srHeMoFiRJejUoBZ6Nrffjhh6L4oqOguxMCSaPUwiIgoj71uWLFCnQaci53UdldhyUIhIuiLkAUqQrIm/nSjzyTGjo0EdAMyJ6xHINgUDkyTQphs93DcJdEJJ9UIHSayyxZsrz11lsMN+gZJCvuN2BQxi4OVR72LgmiXtg8J3j55AyeateuHXWFCoW+TgjJ9u7d2/RKpk/oCnMS2lWlSpXs41tQ4+SsQt7CS8+dO8csK4JUqlQp7ydV9A/JDy9FPJAHIa4QD7Iq+Qk4Tnptoo5e/sILL0iyAWdNIKRYBi9zUV6B4l61alW4Lko5E63c3bx5c7hXBJ3PgQUKFCA/sAK6Q5MmTYzCgaBCU+VB2ohSEEJVSEjbtm3Fc7gIBlM4RItJ19siKE85c+Z88cUXETwqE/GQId7bfLH2FJF8tBMjMAa8wrv0IZg5c6a0FwyHXsb8zeMvvfTStGnTqGSXADAJhasuf1kNOva0spIfcLY52Uu7zIJyS9zYMB2KnQKgZoy1gs8wQm2bR9544w0S4e2oKVxC1Bm1oLLhqjp4rXJR+dghlWkfTCVKP6Wj0kL6yfRy0aDzvYzxSh6knl1cVDqdvUJuo1+/fi1atAh5K05cFKJITLIXLoI/FxXf6cblmAuyH9527OSFcFHkjSmAIdfbKUJyUTHchfKJnBgrfYOhQ4cGrO810eKiQYeWyBaYwJU7fm3IJ1fbWXcwMi4adBw4MazJQIqYmYVB5lw6i1nBjoSLylhk+pSLSTKM3HLLLbZWYEM+b9l2Lt4UvIgWFw1GVs8CL3WULakh530BYzUzO80kl4nERf17R1yBODGtH7wS4heAOcj27+1FFLmov9j4312+fHmjK6Gb+1wQ41v5KMwUaTgaVbdu3Tp+iJtGoaZmjUf2ToJwNR9dJIrvorNnz1IMWLh376w/zp8/jxAzbiZN4a8DoBoy0do7wZCkuBqh0V6MsLIQFKtD+aBjqifrqCHvXrx4EclODB/IKGT0nAS6L/dHAuvT2OhSjWhCcTojV8aIcB60uYvGIGsm1G2sbu4EMDcmPG82CGEiifBzzy4HkcT0BwKGmJnmQ07IQyQ9PSYmZs2aNf6GVcZGl6IxFbnOeIgE1Cpym0gjj4gQrYY4RVhqf8Ba0SO3bNnCVAGxRAEaNGgQRNrl5soF9BhRL2gF2zI/rvCXVUqH8IckLTRiOLbsQryHEf+qRjDEtf01BaGIgSv35onCHfBYLBvMmTPHy0WDzrZe+ZYR8OzOFVMR19qaAWTMOLlxIU5cVFZ67eN2BStWrJCBy5+LEof8p0uXzmseNm7cOBo0TZo0KVOmdLk2JNx8AjP7ReWw2fz587vGupBc9MUXX0yWLNnhw4fFSRtwDSM9e/a0n4oKF2V8Nt/+JkyYIDbwrlYTiF091NEW6Vi5KNJuzghh9hQfUf369QtetkKyN+RHwkXLlSuXKlUqM4y7mKTYOXuNRSdPnozCIHZYLneJScNFI69ngZc6irW/93TrDQ6Y8TNkyGAbCScSF/XvHeGKExKMkJkyZfIqVLxCepD/6msUuai/2PjfjaCg/y7IISa2VSm9Q3ZEmhA5WTPoSO8Pl93EistYY7YALxAumjQGqonrR1eh+FfBu19UkTQIuV/0egWqmMudlYHPubKKaxaDBw8OOPYXtmoFlZJDQcKdXgDRCme61rdv35BcVDy4ZMmSxTtGxcTE5MqVKxzVFMdUgSu9koTD6tWrA455i22OsXnzZnM2lT8XDV42zof22GpQnz59xOReOFLZsmXtUrRu3doswtt+dMV7kGsdyctFqfmsWbOatTI5scPlHIVEoILGnjweXFQWtWzrX/Rpu33FhXLIQ3ppIHFja8efNm2a62uFK1cnTpywN1bIIryMEo0bN+b3hx9+KLdgrVDxHDlymMheLkqV3nLLLe3btzchLiYpNvzUv32K6eLFi2UxWYycH3zwQbtZ5UxLe8e+C2KyYVOmeHDRyOtZMHDgQBd1XLBggawWzps3zwRSzOrVq6P9jx07lrvGh4WpGfPFRBYbbW/n4tcwW7Zs5uOCGIeXLl3axAm5X9S/dwQdeyKXIXRIIAbm8G0XhHgz/vgoM15hDsaXi/qLjf9dhQtyLgndVsSDjiPueI4cOYKkrV27ds2aNbKqcf78edkdKh+m6cXGXjfojBVcxs8hVjygXFShiBqUi14t/Ku46EMPPQRt8PqGHTJkyLV8nKYiHCAMqVOn9jrlQlNMnz59OEuQjh07ZsiQIZyLYDFm9q78iGqIBmmbwBCtZMmS3oN2DdDahYvG6tHEfjvcBk29V69eb7311gMPPGB2esOdAs7OTBNf/IUakoOiKdtlCxcu3LVrV4hBlSpVSFNMPOCcadKkCTjG3vBb0i9evLjhVECslGVRHX1L2E7Dhg2N0i9ctGbNmiakR48esAJjlAjlvu2222CnZl1r3bp1tIXdv+SARLN9FJBV12qS8D37SJWUKVOmTZt2z549YtQARypWrJgxXUFT5y3hbCNJJ+Dsip8wYQJJoTsKLYGtjRw5UtZ+XblCtGAUxtIHaSED4jFBNvxTh6inCxcuJKukzF2UUfEW8cILLwSudLjAI4yxtkCK42tjuYpSK5VPlmh0SBScEGETqxbeLsSSlGEysN/PPvtMXAoRLdzONCF1sEoUaDlARb7d2M7bhMWZ42qCl31DwADlMk71bJrSZeosS53UEtWL9L733nv58uUT3X3OnDkBZ5vGjBkzEBU4JEN0wHEaPHfu3OBlDia1N336dHm11Aayt3Xr1uHDh0uvyZIlCwRAPkuJ1wZbtoOx9Q5qFdFNnjy5WQ8PCe7Cq3lpyLvi8ThwpVNoF7zCHHQOEOIpY+cZvOxHl/qRS/Gob5P2YGxi439X4QLtIjs/lyxZsmHDBrG8XbFihYx1coiL7ZrH2MzHxMQYV0Ziu2svkyY2lIsqFFGDfI/XY6+SHmLvZDuBvI6B/k1h8+TJg8aDsoVmBi2pXLlyOMVCce2jWrVqLg/DQcdoyt5BaoAyWqdOHTHERR81DsZs/Pnnn0WLFvVyUVRVdF8hAIhQqVKl4CrozeGEZ+PGjTA38ZAccI5CbdeuXaxG+xcuXOApYYwB57xBsXcl/P333xcLydy5c8tLP/74Y9E1xZmWpDB79mxx2QpuuOEGdGJ7FQhtSfwPBxzfZobWLlq0SOyQZS0UDRhGWqNGDQmB1Ygdo3BR6rZQoULotajy5cqVs1ddgo7PDxqF8rZu3ZoeV7ZsWeMT5cyZM5988ol48qMs3bt3h9iPHj1aqAXquBjB9u3b12yQNoxOTsZGia9Xrx7aIRwJDkwGYPu9e/cmh669/S70799fag+yAQOHm1E5tWrVmjlzJlTNmyv0deoHCjRo0KAvv/yyfPny5rhdOaZS1vpefvllYtavX19W6oRfoa3CvmgUmg9S9Mwzz1BvxqkbtSFHfwUcs1JjILp9+3ahH/IxAo5k73nZu3evmFxKJocNGwZFfOCBB6Bb4ZihuJcLOG4daE1eJPtOkWHKiAL97bff0gukIAyJSGznzp1lTzsx5YijyOsZ5fuDDz4Qw+AMGTJ06dLFrAzT7rBQYwBPzo0HWngg8ibh0CTyIGeDp0qVCsEIOpsO5JsIpaYt5CnkU2wfKCA1TEUhGNQ58nz06NFOnTqJzwsyQ5Zsi3Gf3kHHJz6Z9OGiEPucOXMGHK9FXk9mCJVsVhdBpcjh9jXYwkz2jDzQWcRraZs2bYQ2Uyf0TcolIkd5W7VqZa+5+YuN/12FCwiPnEUioKua70f8EFtcwcqVK21jHAYB49DoB+dYzThtNEsIlIsqFFEAc0/dunXl4A0GYteHTEWiYsaMGShDUvm0Qly3zfzjwPSADvfUU0+hXaHQoyOiqaizt380wn1+TshnaTQSOcbJC1gQfHLu3Lnz589PvMPN0XLWr1/vPd4zckBdUKnD7Qo7ePAgd+OxncnY6J49e3bdunU+liyyyz0hm6u92Lx5s9nsh5ZPd6YIO3bsgPtF4giAtvv1119FF6fX+5+dS+JCJGDaMEyXPMjGb3voIG+uU3BIYefOnXEVEgq4du3acOKHykthpeEi2YG8f//+BH7hjUc9hwNkj6KF5ELUkv1FgzybM2+DTnegtl28TrxgiIDRsnE6QiNc7yC1JDsQ0RbmhMNfbPzvKmwg6vQypJTqcvFJLhHLw4cPhxw6uIv8MHcksWMF5aIKhUKhUCj+LQjpu0ihUCgUVwXKRRUKhUKhUPxboFxUoVAorh0oF1UoFAqFQvFvgWyM9O6UUygUCkXSQ7moQqFQKBSK6x+nTp1q37797bffnjFjxjx58nTq1Mnf3ahCoVAoEhvKRRUKhUKhUCgUCoVCkdRQLqpQKBQKhUKhUCgUiqSGclGFQqFQKBQKhUKhUCQ1lIsqFAqFQqFQKBQKhSKpoVxUoVAoFAqFQqFQKBRJDeWiCoVCoVAoFAqFQqFIaigXVSgUCoVCoVAoFApFUkO5qEKhUCgUCoVCoVAokhrKRRUKhUKhUEQN58+fnzlz5vr166OS2h9//DFo0KBt27YlPKmzZ88eOnQo5K0TJ07s3r074a9IYpw6dWr06NGnT5+Wy4TX1blzF86cOe/6+/vvv3ft2nXp0qUo5Tosdu7cSXES+y1JDERr5MiR586d84kzfvz4H374IalyFE8gAMuWLfvkk09GjRp14MCBq5iT1atXz5kz5ypmQBFdKBdVKBQKhUIRBUDnmjZtmi5dukAg8OWXX0YlTdIhtYoVKyYwnTVr1jRs2BBiEPJut27dqlWrlsBXJCWgbdWrV0+ZMiWVs2/fPglMeF398MOuVq1mZ8zYMxD4//h78smhvXotPnXq3JYtW+rVq5d4DAR68/DDD5P5O++8M5FekfTYv3//K6+8kiJFCsoVTvAAPJ8IN9xww8WLF5Mye3HC+fPnX3jhhcmTJ0ObU6dOnSFDhuPHjyd9NgYPHnzXXXdRXfXr10/6tysSCcpFFQqFQqG4rnB1lVp01ihy0T179sASJ02alJBEfvrpp6effvrPP/8MeffChQvZs2dPliwZBC8hb0li/P3331mzZrW5aFTqCnTu/ANENHnyzmfOnDeBBw8erFy5criF5YRjw4YN1z4XjaRn2XFMG/lw0UuXLsHzu3TpEp0sJg7ee++9vHnzyu+vvvrq2Wef/euvv65KTj777DPlotcZlIsqFAqFQnH9YMiQIVCvq5iBNm3aRJGLJhxbt27Nli0bPC1chG+++SbgoEWLFkmZsYRD1hINF40WhgxZBRfNlOkDV/i0adOKFSuWSF86/vzzz2uci545c6Zp06ZxjXPPPff4c9FrH8KoK1SocLUz8n8xdepU5aLXGZSLKhQKhUJxneDnn39OkybNjz/+eBXzcE1xUYjTY4891rlzZ584JUuW7NSpE3nOkCGD2Xv5j0AicdHPP/8ZLpo5s5uLguLFi3fo0CG6rxNc+1y0evXqZcqUiWuc64CLHjx4kCIoF/1H4MyZMz97cP78/2/gcOTIkVWrVi1cuHDlypW7d+/++++/g863Bu8jgqQZD5WLKhQKhUJxFYBOsGXLlqBjnTh06NAFCxZ4zd727NkzZsyYQYMGLVq06MKFC/atc+fOzZo1ix87duwYMmTI3r17N27cmD17dhS1wYMHL126lJBwr4ahzZ0797PPPvvmm2+8TIaMkSV+bNu27Ysvvpg9e7Y3BZ+M2Vz07NmzSy389ttvEueXX36RkFOnTknIgQMHxo4dO27cuE2bNqH72gkSx+WqhGSnTJkyYsSIFStW7N+/38etDmmSGSlOSJCT++67jx8FCxYkZt++fUNGo4wzZsyIiYmhjRYvXkx7rVu3zhUnkgY9evTod999R3sR2XWLYk6ePDnouCCiZYcNGxaSZO7cuZOCU1EonV4uatcVuXVVPjHNpc/ypg8XJedp0qTx3zhKGWVlnv9k1X6pRNi+fbtc0nzmqXBc1KfG0KGpZCpq/vz5hw8fjpXvHTt2jIpFaHmK2jPhRhqlJulZJsNSUgSsVatWZK9o0aISLkq8jXBxDBeFD/z444/0TWiA61mRLkMY4lc0esTAgQPp197uEK7gAgYK8ZxEVY91gOSYbFAQhI0iPPbYY3YtCZBVWplCTZs2zbbfZnyQyAxKErJ69WoJ2bx5s/32SEYbZIMc8hbYkZeLUj+U/WrZDF9rYPD8wQNxncVQKZfIofyQtqCVvY8Ifv/99yTIs3JRhUKhUCiSDnCALl26iIYKY3nxxRdTp04tNqLFihVDHZRo6ActWrR48MEHFy5cCLsoVKhQ2bJlRUdcs2ZNo0aNMmXKhOKOIpg+fXqeLVeu3IABA6BV/K5bt26nTp2+//77kBmARN19993du3dHBe/YsWPatGmFAgGYWJ48eUiBpHg76d90001cNm7c2DzukzGBzUVRr9GPpXQffvihKR06UN68eV977TV5ELKBBk+Gf/311+eee+7++++XaCim1atXh/w88MADJn24N7UHE+ZHt27dSNlHYXriiSfuuOMOn+agJils8PI+NIrvUuVR4N58881bb72Vu2jS1LBpL8IvOoikQYOO55WaNWvyupYtW6ZMmfLZZ5+VZQfoN09RzNtuuw2V/d5776VyePzmm2/mlnkcbfv111+vXLny9OnTv/nmm/Lly9v7Rb11ReUT8/bbbydOlSpVyAla+5NPPkkEGs6HwPtwURqO1GjikA/SjtWqVUuVKhUt+8knn0gldO7cmcaS3/LZAqLSr18/LhFd82xILhquxqR0pUuX7tChw9atW8ePH3/jjTf6bJSlsL1794a6U2/wFmojc+bMkC65u2vXrhIlSvD2d999V+oZZf2RRx4h5KOPPiIEQkVbc0nH6eTA9f3FJ44IBpKDaOXPn5/uJv3LPNW0aVORLkM441S0oNNt6YNUMjwtW7ZsyI9xCu1fcAgq8sCrX3rppdGjR+fIkUM+ZiEhwl4oAgV544037HIZl788XqBAATrOvHnzGBNoIPIsnPD48eNvv/02T5G+RF6/fn29evUIefrpp022Yx1tgFQdkRlw/vvf/z766KMuLlqyZElC+vTp41NF/x5s376dBtq7d+9RC5ccCAUV2Thz5syCBQu4PHXqFEP60SvBOMwtat4r54kB5aIKhUKhUCQpDh06VKFCBfSnwoULz5w5E+0NpVPW5V599VWJg1pvVGEwaNAgLj///POgc0qELA6gVqL8/fbbb++88w7KPbfQKQn3t9F96KGHDAdAC0F5tdla8+bNSQEFesaMGUFnnQ0dlBDj18cnYwKvja4U1o5DkeFIhqfxG8oqv2GnEAP5fezYsa+++kqUY/NsjRo1YG7mEvU63DLdyZMnkyVL5mNbSAReLfSG92bMmJF3UUA7DlmF9MISucWr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69Sp88ADD0Q3TYVy0XjgzJkzP3tg/BEcOXJk1apVCxcuXLly5e7du//++2/7wbVr1/74449Lly7dvHnzhQsXkizPykUVCoVCobgKSCAX/eOPP4SLdurUKdyDO3bskD2ls2bNGjNmjHGWc/bs2alTpw4YMOC77747fPiw66n169ejvvDjt99+GzVq1MSJE0M6TFq2bNmQIUO+/fbbffv2hXw7FGv69OmDBg1avHhxSM3m/vvvr1atml/JrwTE9c4776TIH374IQrTtm3bgldyUTStCRMmjBgxYv/+/d7H9+zZM378+GHDhv3yyy+xvoukUIK/+uor9DPqwYTbXJQMQCZ5I/XpevzgwYOUWn5TP+T22WefNTkHtAU5T506NYHff/89Id6GMLh06dK8efNOnjxpB/7000+UZfbs2YcOHQrpJ8kAAiYKPa2AGkqrbdy40RvNv34OHDjA3YEDB86dO9dbXjJD/pETBGbOnDk+mRFQJ2QJ2UD39d5FcigvXQO5PXr0aDyKQ06QvS+//JJWoH54RJKtUKECFf7SSy9R4SLkkZTOp0fQNO3atSPNvHnzmpYNV2r/fgdoYopMBKK5Ot1ff/01bdq0oOMZa/DgwRs2bIiwugDUYuTIkcjb9u3beTzCWyGBbAx34P2KBLGR5qDXbN261XWXGkZWg84WA4pPJw35Omr466+/ppKpHy8XDdkRFDYYeX7wQGSJUVEu6XTyg9aXpyCiCxYsIGTRokXyA8qaZHRUuahCoVAoFFcBCeSiKNnCRdEbXPFRW/v371+iRAnufvTRR2+++abERE3kLpp0lixZUEChqU2aNLnppptMCijB99xzDzG7dev2/vvv58iR47bbbuPy0UcftfUSdMGKFSuSLFpL48aNiZAvX75KlSo9/fTTaJwSB22yevXq/fr169Chw4033li0aNHdu3e78tm8eXOe3bRpU4Q1RvYeeOAB4RIwcFFSDRft06dPpkyZyAmXN998s02oLl682KZNm4YNG0I2GjRoQITatWtD5sO9CKW5UKFCqP6wTaooVapU5pZwUdKpUaNGNgdcQqqFgaCODx06tEyZMsmSJTNLtWjP5Pahhx4iJnXSycGuXbu6dOkinpDIGyErV6705gSNnzfefvvtRBPuHXQ4GFVNOHehH3fccUfPnj1DFgRds2bNmmnTpk2ePDlko0iRIrRv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TGPJkiW62XD4TerZIwpr1qyhTf7888+pU6cuW7ZMT580adLSpUvp62Be6Skb3UEDPvnkk7rMKC76999/b9q0iUcvX77cca2PRCGWs2fP5ukqqLfjoYsWLaK56IVwNpJdvHiRupCfx3lyUcRM+mv69On79u0LWTvLNoOnhGPGjKFebkmguehQ7sawkkiGOjxr5/MsxunHH38MPzxw4IDPuNO5KJdzSHer6TScke4zHNxAYBihdNycOXMOHTrkOEu/0zISOIFqMpy/+uorRx6di+pyC9QNqbKkMEZStDBW4uXKwMDAwMDAICWQzFwUPQAaiT76swY9fpSQCpRFnYuiPsqh0Izz58+jR3IYfrizGxNoUcIzfTxGiDoO0JXPnDnz+uuv879EiRJyFl28b9++pNxyyy2SAvt64oknMmXK9Mgjj/zvf/+TUMXNmzf3vPmGDRsee+yxIUOGUIDbbrstX7584hfxp59+kvXY9OnTCwOx7F4WBZpf+ABdzyPq16+/cePGefPmoRbHxMTozmx1Lkp+hErim4tbVCgBz5IQ59xQXTV37ty8efOizcN5XnzxxRw5cihfo7BTYU0QgN69e8MfaJCBAweK7yJ0VnUTbt6hQ4c6deosXLgQIlGjRo38+fMrU0bYAg1y00030Thoz5UrV6Y909ugIj799ccff0AeGjduTDaenjlz5kqVKunOpahI+fLl6Sk4YZs2bTJmzPjWW2/Jinc4TerfI7169aKcZKZB7r77bpEKBABFnI54+eWXIScQ4IIFC/JQz/Kju3NzruJyGpCnSLq0KretUKHC7bffLtHt27VrF1KiqFrXrl3bt28PzWvbtq0EPdfDo0GYkYr333+/Z8+eWbNmrVKlir+DTagXBaD8sE1ozwMPPODgovQdjcAogKXw0MjISDV2gtWue/fuXPLll18y3B588EGkRWdK9FS5cuWQE7gc8pYhQwZ1yqd2wZ41YMAABB6itWXLlurVqyOBwWoq/f7KK6/QkoEEFCpUiNFk2VExQo5093AI9izkjVrTUHRxv379EMsWLVrwCMsOy4FIM+K4D8LDrZA6cVPkWLPVuSjDXAw6wBtvvAHVlzw0bL169e666y4fLposhUmsXBkYGBgYGBikEJKZi0IjURH01QYHDh06RIYTJ07oXBTVn/+oemplDI2KFEcIbAMHJkyYIPqcT+AT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
```

---
