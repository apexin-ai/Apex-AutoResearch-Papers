# Research conversation: You are a reviewer for a top ML venue (e.g., EMNLP Main, ~25% acceptance rate). Review the following paper using a 6-poi

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 42
- **Recorded user turns:** 1
- **Tool calls:** 17
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-ac10b8784a4950006.jsonl`
- **Structured JSON:** [`bd3fa47dde55fa7703b1.json`](../../sessions/bd/bd3fa47dde55fa7703b1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

42 recorded events

### User

_source line 1 · 2026-05-16T16:33:29.528Z_

You are a reviewer for a top ML venue (e.g., EMNLP Main, ~25% acceptance rate). Review the following paper using a 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept.

## Paper Summary

**Title:** "Trace Formatting as Implicit Task Specification: Format Markers Dominate SFT Verdict Prediction"

**Core claim:** SFT on execution traces for verdict prediction (binary pass/fail classification of code solutions) is dominated by format markers (like `[No exception data in trace]`) rather than genuine fault reasoning. Format markers account for 41.3% of the total accuracy lift, and SFT barely outperforms a regex baseline (99.83% vs 99.33%, Δ=0.50pp). Removing format markers drops accuracy to 89.63%, *below* the regex baseline.

**Method:**
- Task: verdict prediction (pass/fail) on code solutions from HumanEval (164) + MBPP-sanitized (427), 591 problems × 10 LLM-generated solutions = 5,910 samples (71.5% pass, 28.5% fail). Train/test: 4,720/1,190 with no problem-level overlap.
- VOTA trace compression: decomposes full traces into loop compression, exception summaries, actual/expected pairs.
- Six trace conditions: no_trace, full_trace, VOTA, exception_only, ae_only, loop_only.
- Format marker removal (nomarker): removes `[No exception data in trace]` from pass samples, removes `[ERROR]` prefix from fail samples, retrains from scratch with 3 seeds.
- Training: LoRA (rank 64, α=128), 3 epochs, SFTTrainer, lr=2e-4 cosine, max 2048 tokens.
- Models: Qwen-2.5-Coder-7B (primary), Qwen-2.5-Coder-1.5B, DeepSeek-Coder-6.7B, CodeLlama-13B-Instruct.
- Regex baselines: B5 (checks `[No exception data in trace]` → 99.33%), B1 (checks `[ERROR]` → 93.45%).

**Key results:**
- exception_only: 99.83% across all scales (1.5B=7B=13B) — scale-invariant, suggesting trivial pattern
- SFT with markers (99.83%) ≈ Regex B5 (99.33%), Δ only 0.50pp
- SFT without markers (nomarker): 89.63% mean, std=2.50pp — drops 10.20pp, falls below regex
- Lift decomposition: total 24.7pp = content signal ~14.5pp (59%) + format marker ~10.2pp (41%)
- Gradient dilution decomposition: full_trace→exception_only gap = 26% gradient dilution + 74% information overload
- On CodeLlama-13B, VOTA (99.92%) exceeds exception_only (99.83%), breaking "exception dominance"
- DeepSeek: 2/3 seeds match regex exactly at 99.33%
- Seed variance: 0.00pp with markers → 2.50pp without markers
- Calibration: ECE degrades ~24× after marker removal (0.0027 → ~0.065)

**Paper structure:** 11 pages, 13 tables, no figures. Sections: Intro, Related Work, Method, Experiments (11 subsections), Discussion (7 subsections), Conclusion, 1 appendix.

## Experimental Design Reference (from review_context.yaml)

The imagined experiment plan includes these experiments. Check coverage:
1. no_trace baseline ✓ (Table 1)
2. VOTA baseline ✓ (Table 1)
3. full_trace baseline ✓ (Table 1)
4. VOTA minus actual/expected ✓ (Table 2, vota_no_ae)
5. full_trace label-only loss ✓ (Table 1, Table 5)
6. VOTA component ablation (loop/exception/ae) ✓ (Table 2)
7. DeepSeek-Coder-6.7B four-condition validation ✓ (Table 8)
8. DebugBench cross-task validation ✓ (Table 12)
9. Trace length ablation (256/512/1024/full) ✓ (Table 6)
10. Calibration analysis (ECE + Brier) ✓ (Table 11)
11. Seed robustness (3 seeds × exception_only + VOTA) ✓ (Table 9)
12. Qwen-2.5-Coder-1.5B four-condition validation ✓ (Table 7)
13. CodeLlama-13B three-condition validation ✓ (Table 7)
14. Multi-seed: ae_only / label_only / loop_only × 3 seeds ✓ (Table 10)
15. Format marker removal: exception_only_nomarker × 3 seeds ✓ (Table 3, core experiment)
16. Cross-cutting synthesis ✓ (Table 13, Appendix A)

All 16 planned experiments appear covered in the paper.

## Your Review Task

Provide a thorough review covering:

1. **Summary** (2-3 sentences)
2. **Strengths** (bulleted, specific)
3. **Weaknesses** (bulleted, specific, with actionable suggestions)
4. **Questions for Authors**
5. **Minor Issues**
6. **Missing Experiments or Analyses** (compared to what would strengthen the claims)
7. **Overall Assessment** (score on 1-6 scale with justification)
8. **Confidence** (1-5 scale: 1=low, 5=expert)

Be rigorous. Evaluate novelty, soundness, significance, clarity, and completeness. Consider whether the findings are surprising or obvious, whether the experimental design properly supports the claims, and whether the paper makes a sufficient contribution for a top venue.

Key things to probe:
- Is the format marker shortcut finding genuinely surprising, or is it a predictable consequence of the trace design?
- Is the nomarker experiment well-designed? Could there be confounds (e.g., trace length differences between pass/fail even after marker removal)?
- How generalizable are these findings beyond this specific VOTA format?
- Is the dataset (591 problems, 71.5% pass) sufficient for the claims?
- Are the claims about "shortcut learning" well-supported, or is the paper over-interpreting?
- Does the paper properly engage with related work?
- Is the writing quality sufficient for a top venue?


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "1671510c-98af-4e06-a3f5-68dced519a8b",
  "agentId": "ac10b8784a4950006",
  "type": "user",
  "uuid": "d03d8b22-0fbe-46e6-a892-aba3d700e692",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "ab493159-c57d-451b-9109-6ba744c1f6a1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T16:33:29.533Z_

```json
{
  "parentUuid": "d03d8b22-0fbe-46e6-a892-aba3d700e692",
  "isSidechain": true,
  "agentId": "ac10b8784a4950006",
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
  "uuid": "ac325ad9-306d-4612-8302-112711c334ff",
  "timestamp": "2026-05-16T16:33:29.533Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "ab493159-c57d-451b-9109-6ba744c1f6a1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-16T16:33:32.757Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_014GdisLkAcDhdbe9xquL8jc`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac325ad9-306d-4612-8302-112711c334ff",
  "isSidechain": true,
  "agentId": "ac10b8784a4950006",
  "requestId": "req_011Cb6a1qzQFcLabPk48RZvL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "01e87c93-ab25-41f3-bc23-ed3df4bd7b08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "ab493159-c57d-451b-9109-6ba744c1f6a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Uo2aZk9FkgfU5CtFPeKnL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15748,
      "cache_read_input_tokens": 0,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15748
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 88,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15748,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15748,
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

_source line 4 · 2026-05-16T16:33:32.761Z_

<details><summary>↩ Tool result · `toolu_014GdisLkAcDhdbe9xquL8jc`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "01e87c93-ab25-41f3-bc23-ed3df4bd7b08",
  "isSidechain": true,
  "promptId": "1671510c-98af-4e06-a3f5-68dced519a8b",
  "agentId": "ac10b8784a4950006",
  "type": "user",
  "uuid": "291a5dc3-cfed-473b-8153-05f96d5de90f",
  "sourceToolAssistantUUID": "01e87c93-ab25-41f3-bc23-ed3df4bd7b08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "ab493159-c57d-451b-9109-6ba744c1f6a1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T16:33:37.218Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_013jQFHfLBur7aDEBbzBmP74`</summary>

```json
{
  "project": "trace-verdict-study",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "291a5dc3-cfed-473b-8153-05f96d5de90f",
  "isSidechain": true,
  "agentId": "ac10b8784a4950006",
  "requestId": "req_011Cb6a25xn2rBMAHwsrGY2v",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a10bc161-0c93-473d-8e7b-b53a80d7a2d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "ab493159-c57d-451b-9109-6ba744c1f6a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PJo7nh9n5R3xugL1LoF7xn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1269,
      "cache_read_input_tokens": 15748,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1269,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
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

_source line 6 · 2026-05-16T16:33:37.238Z_

<details><summary>↩ Tool result · `toolu_013jQFHfLBur7aDEBbzBmP74`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/report.md\", \"content\": \"# Handover — 2026-05-16\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| exception_only_nomarker_seed42 | — | — | — | — |\\n| codellama13b_vota_seed42 | — | — | — | [codellama13b_vota_seed42] |\\n\\n## 待处理\\n- codellama_vota_seed42（排队等待 GPU）\\n- codellama_no_trace_seed42（排队等待 GPU）\\n- codellama_exception_only_seed42（排队等待 GPU）\\n- qwen1.5b_full_trace_seed42（排队等待 GPU）\\n- qwen1.5b_vota_seed42（排队等待 GPU）\\n- qwen1.5b_no_trace_seed42（排队等待 GPU）\\n- qwen1.5b_exception_only_seed42（排队等待 GPU）\\n- exception_only_nomarker_seed456（排队等待 GPU）\\n- exception_only_nomarker_seed123（排队等待 GPU）\\n\\n## 近期结论\\n- **codellama13b_exception_only_seed42** (success): —\\n- **loop_only_seed456** (success): —\\n- **loop_only_seed123** (success): —\\n\\n## 趋势\\n成功 37 / 负向 7 / 失败 3 / 共 56\\naccuracy: 0.9983 ↑（近 3 次 success）\\nn: 1190 →（近 3 次 success）\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-11235: 无 GPU 信息\\n\\n## 告警\\n- no_trace_seed42: 已被终止 — unknown\\n- vota_seed42: 已被终止 — unknown\\n- no_trace_seed42_v2: 已被终止 — unknown\\n- vota_seed42_v2: 已被终止 — unknown\\n- no_trace_seed42_v3: 已被终止 — unknown\\n- vota_seed42_v3: 已被终止 — unknown\\n- full_trace_seed42: 已被终止 — unknown\\n- vota_exception_only_seed42: 训练失败 — unknown\\n- vota_seed123: 训练失败 — unknown\\n- vota_seed456: 训练失败 — unknown\\n- deepseek_full_trace_seed42_v2: 已被终止 — unknown\\n- full_trace_2048tok_seed42: 已被终止 — unknown\\n\", \"total_chars\": 1370, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a10bc161-0c93-473d-8e7b-b53a80d7a2d6",
  "isSidechain": true,
  "promptId": "1671510c-98af-4e06-a3f5-68dced519a8b",
  "agentId": "ac10b8784a4950006",
  "type": "user",
  "uuid": "53fc1281-19fd-46b9-9a32-1301a67d7ea2",
  "sourceToolAssistantUUID": "a10bc161-0c93-473d-8e7b-b53a80d7a2d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "ab493159-c57d-451b-9109-6ba744c1f6a1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T16:33:37.288Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_017kr2MeLLhJRWGiQ7R8kTRv`</summary>

```json
{
  "project": "trace-verdict-study",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53fc1281-19fd-46b9-9a32-1301a67d7ea2",
  "isSidechain": true,
  "agentId": "ac10b8784a4950006",
  "requestId": "req_011Cb6a25xn2rBMAHwsrGY2v",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "53d6cdab-0acd-43c4-ad32-465c66422075",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "ab493159-c57d-451b-9109-6ba744c1f6a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PJo7nh9n5R3xugL1LoF7xn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1269,
      "cache_read_input_tokens": 15748,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1269,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
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

_source line 8 · 2026-05-16T16:33:37.303Z_

<details><summary>↩ Tool result · `toolu_017kr2MeLLhJRWGiQ7R8kTRv`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/paper_framing.md\", \"content\": \"# Paper Framing — trace-verdict-study\\n\\n> v3.0 — [UPDATED 2026-05-15] D030 CLOSED: DeepSeek VOTA 84.45% confirmed correct (confirmatory re-eval). **Critical narrative fix**: to_chat_text() preserves labels → VOTA 训练时 verdict label 未被截断 → 论文中 \\\"label truncation/corruption\\\" 措辞对 VOTA 不成立。正确叙事: trace INPUT content 被截断 (91.7% samples), 84.45% 反映 trace information loss。新增 D11: VOTA cross-model gap confounded by training-time truncation。数据集来源：HumanEval (164) + MBPP-sanitized (427) = 591 problems × 10 LLM-generated solutions = 5910 samples。\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR submission)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May 25, 2026\\n\\n## Core Insight\\n\\nVerdict prediction (pass/fail) is fundamentally a **fault detection** task. The most effective signal is the **exception event** — a compact, structured diagnostic moment that consistently outperforms all other trace representations across models (Qwen 99.83% ± 0.00 across 3 seeds; DeepSeek 91-99% depending on seed, but always > VOTA 84.45% and no_trace 73.36%). In contrast, richer trace representations that require deeper execution reasoning show model-dependent effectiveness: VOTA gap = 14.96pp, no_trace gap = 1.77pp. Information density — not training signal distribution — is the primary bottleneck: even oracle loss masking (label-only) cannot close the 13pp gap between full traces and targeted extraction. The design principle: **extract the highest-specificity diagnostic signal; discard everything else.** Cross-model absolute performance depends on LoRA initialization stability, but exception_only's relative dominance over other components is robust.\\n\\nVOTA's primary contribution is **fault indicator isolation** — automatically extracting exception events from noisy full traces — rather than generic trace compression. The \\\"compression helps\\\" narrative was a stepping stone; the real mechanism is diagnostic signal extraction.\\n\\n## Core Claims (3)\\n\\n### Claim 1: Exception events are the most effective trace component for verdict prediction\\n\\nException summaries consistently achieve the highest verdict prediction accuracy across both models tested, outperforming all other trace representations in every seed. On Qwen-2.5-Coder-7B, performance is perfectly robust: 99.83% ± 0.00 (3 seeds). On DeepSeek-Coder-6.7B, absolute accuracy is seed-dependent (seed42=99.83% epoch1, seed123=91.43% epoch1; Δ=8.40pp), consistent with LoRA initialization sensitivity — but exception_only still dominates VOTA (84.45%) and no_trace (73.36%) in all seeds. This contrasts with VOTA (cross-model gap = 14.96pp) and no_trace (gap = 1.77pp). Exception events are structurally simple (`[ERROR] type: ... message: ...`) and do not require deep trace reasoning.\\n\\n**Supporting evidence:**\\n- `vota_exception_only_seed42_v2`: Qwen 99.83%, ECE=0.0027\\n- `deepseek_exception_only_seed42`: DeepSeek 99.83% (epoch1) / 99.33% (epoch3)\\n- `deepseek_exception_only_seed456`: DeepSeek 99.33% (epoch3), CI [98.82, 99.75] — 与 seed42 完全一致\\n- `deepseek_exception_only_seed123`: DeepSeek 91.43% (epoch1) / 91.09% (epoch3) — LoRA init sensitivity outlier\\n- `deepseek_vota_seed42`: DeepSeek VOTA 84.45% (gap = 14.96pp vs Qwen)\\n- `deepseek_no_trace_seed42`: DeepSeek no_trace 73.36% (gap = 1.77pp vs Qwen)\\n- `vota_no_ae_seed42`: 99.41% — actual/expected removal 不降，非 trivial string comparison\\n\\n**DeepSeek seed analysis** ✅ (FINALIZED, D029):\\n\\n| Seed | Epoch 3 (final) | fail_recall | pass_recall | train_loss | Errors | CI |\\n|------|-----------------|-------------|-------------|------------|--------|-----|\\n| 42   | 99.33%          | 1.0         | 0.9906      | —          | 8/1190 | — |\\n| 456  | 99.33%          | 1.0         | 0.9906      | 0.1225     | 8/1190 | [98.82, 99.75] |\\n| 123  | 91.09%          | 0.705       | 0.993       | 0.122      | —      | [89.4, 92.6] |\\n\\nseed42 与 seed456 结果**完全一致**（均 8/1190 错误，99.33%），seed123 为离群值。seed123 的 fail_recall 仅 0.705 — LoRA 初始化落入差的局部最优，未充分学到 exception→fail 映射。**关键发现**: seed456 和 seed123 的 train_loss 几乎相同（0.1225 vs 0.122），但 accuracy 差 8.2pp — token-level loss 掩盖了 sample-level 分类能力的巨大差异（详见 D10）。\\n\\n**Irreducible error analysis** ✅: 3 seeds 错误的 2 个样本 (id=901, 905) 均来自 HumanEval/95 (`check_dict_case`)，根因为 Python `all()` 对 generator expression 短路触发 `GeneratorExit`（`BaseException` 子类，非真正错误）。tracer 将其标记为 `[ERROR]`，exception_only 模型看到 7 行 `[ERROR] GeneratorExit`，合理但错误地预测 fail。整个 1190 条测试集仅这 2 条含 `GeneratorExit`，模型无训练信号学习其良性本质。**这确认 99.83% 是 exception_only 表征的理论上限，剩余 0.17% 是 representation-inherent irreducible error，而非模型不足。**\\n\\n**Seed robustness** ✅: Qwen exception_only 3-seed 完全一致，构成本文最强 robustness 证据：\\n\\n| Seed | Accuracy | 95% CI | Errors |\\n|------|----------|--------|--------|\\n| 42 | 99.83% | [99.58, 100] | 2/1190 |\\n| 123 | 99.83% | [99.58, 100] | 2/1190 |\\n| 456 | 99.83% | [99.58, 100] | 2/1190 |\\n\\n3 seeds 错误样本 100% 重叠（id=901, 905, 均为 `check_dict_case` 函数, label=pass → pred=fail）。**Irreducible samples**: 模型已达数据集理论上限，variance = 0。\\n\\n**DeepSeek cross-model** ✅ (D029): 3-seed 完整数据 — seed42/456=99.33%, seed123=91.09%。2/3 seeds 鲁棒，seed123 为 LoRA 初始化离群值（fail_recall 仅 0.705）。Qwen 3-seed 完美稳定 (99.83% ± 0.00) vs DeepSeek 高方差（σ≈4.8pp），暗示 exception signal 的 learnability 与模型 LoRA 训练稳定性相关。但即使最差 seed (91.09%) 仍优于 VOTA (84.45%) 和 no_trace (73.36%)，relative dominance robust。\\n\\n### Claim 2: Information density, not gradient dilution, drives trace compression benefit\\n\\nFull traces help verdict prediction (81.76% [`full_trace_seed42_v5`], +6.6pp over baseline), but VOTA achieves 99.41% [`vota_seed42_v5`] (+24.3pp) — a +17.6pp advantage. Label-only loss ablation (plan_002) quantifies the causal decomposition: **gradient dilution contributes ~26% of the gap** (4.5pp; label-only full_trace = 86.22% [`full_trace_label_only_seed42`]), **information overload contributes ~74%** (13.0pp; only trace compression resolves this). Even with oracle loss masking that eliminates gradient dilution, full traces still underperform VOTA by 13pp.\\n\\nCross-model evidence reinforces this: VOTA gap (14.96pp) partly tracks base model execution reasoning capability (Qwen CRUXEval-I 56.5% vs DeepSeek 39.0%, Δ=17.5pp), though **confounded by DeepSeek training-time trace truncation** (91.7% of VOTA samples truncated to ~2048 tokens; see D11). The two factors cannot be disentangled in the current design. Exception signal partially bypasses both bottlenecks (token-short, no truncation; consistently best component on both models), though DeepSeek shows seed-dependent absolute performance (91-99%).\\n\\n**Supporting evidence:**\\n- `full_trace_label_only_seed42`: 86.22%, ECE=0.1107 (gradient dilution fix, +4.5pp over standard full_trace)\\n- `full_trace_seed42_v5`: 81.76%, ECE=0.0958 (standard full_trace)\\n- `vota_seed42_v5`: 99.41%, ECE=0.0054\\n- `deepseek_vota_seed42`: 84.45% (VOTA model-dependent)\\n- CRUXEval literature data (Wang et al.)\\n\\n### Claim 3: Two-tier diagnostic hierarchy for verdict prediction\\n\\nComponent ablation reveals verdict-relevant trace information has a strict two-tier hierarchy:\\n- **Tier 1 — diagnostic moment signals**: exception summaries (99.83% [`vota_exception_only_seed42_v2`]) and assertion-point information (99.92% [`vota_ae_only_seed42`]) are individually near-perfect and sufficient for verdict prediction on Qwen. These signals are structurally simple and consistently the most effective component on both models, though DeepSeek absolute performance is seed-dependent.\\n- **Tier 2 — behavioral patterns**: loop compression (85.63% [`vota_loop_only_seed42`]) carries substantial signal but is model-dependent and fully subsumed by Tier 1.\\n\\nCombining tiers introduces noise rather than helping: exception_only (99.83%) > VOTA full (99.41%), p=0.01. Loop_only ≈ full_trace_label_only (85.63% vs 86.22%) confirms VOTA's loop compression precisely extracts the useful behavioral signal from full traces.\\n\\n**Supporting evidence:**\\n- `vota_exception_only_seed42_v2`: 99.83%, ECE=0.0027 (Tier 1 exception)\\n- `vota_ae_only_seed42`: 99.92%, ECE=0.0004 (Tier 1 assertion-point, 与 exception 统计等价 p=0.80)\\n- `vota_loop_only_seed42`: 85.63%, ECE=0.0831 (Tier 2 behavioral)\\n- `full_trace_label_only_seed42`: 86.22%, ECE=0.1107 (≈ loop_only, confirming extraction equivalence)\\n- `deepseek_exception_only_seed42`: 99.83% epoch1 / 99.33% epoch3 (Tier 1 cross-model validation)\\n- `deepseek_vota_seed42`: 84.45% (Tier 1+2 cross-model: Tier 2 introduces model-dependent degradation)\\n\\n**Calibration**: 完整 calibration 数据确认 Tier 1 信号不仅 accuracy 近完美，置信度校准也近完美：\\n\\n| Condition | Accuracy | ECE | Brier | 解读 |\\n|-----------|----------|-----|-------|------|\\n| ae_only | 99.92% | 0.0004 | 0.0008 | 近乎完美校准 |\\n| exception_only | 99.83% | 0.0027 | 0.0013 | 近乎完美校准 |\\n| VOTA | 99.41% | 0.0054 | 0.005 | 优秀，但 Tier 2 引入轻微 noise |\\n| loop_only | 85.63% | 0.0831 | — | Tier 2 单独校准中等 |\\n| label_only | 86.22% | 0.1107 | — | gradient dilution fix 仍 miscalibrated |\\n| full_trace | 81.76% | 0.0958 | — | 中度 miscalibrated |\\n| no_trace | 75.13% | 0.1715 | 0.1972 | 严重 miscalibrated |\\n\\nno_trace ECE 是 exception_only 的 **~63x**（0.1715/0.0027），Brier 是 **~150x**（0.1972/0.0013）。Trace signal（尤其 Tier 1）不仅提升 accuracy，更从根本上改善模型 calibration。\\n\\n**Design principle**: verdict-optimized traces should extract highest-specificity diagnostic signals; lower-specificity signals are redundant and may introduce noise.\\n\\n## Cross-Model Evidence Summary\\n\\n| Condition | Qwen-2.5-Coder-7B | DeepSeek-Coder-6.7B | Cross-model gap | Interpretation |\\n|-----------|-------------------|---------------------|-----------------|----------------|\\n| exception_only | 99.83% ± 0.00 (3 seeds) | seed42/456: 99.33%; seed123: 91.09% | 0.50-8.74pp (seed-dependent) | **Best component on both models**; 2/3 DeepSeek seeds match Qwen-level; 1 outlier still > VOTA |\\n| VOTA | 99.41% | 84.45% | -14.96pp | Model-dependent — requires execution reasoning; **also confounded by DeepSeek training-time trace truncation** (91.7% of VOTA samples truncated from mean 2626 to ~2048 tokens; labels preserved via to_chat_text(), see D11) |\\n| no_trace | 75.13% | 73.36% | -1.77pp | Baseline gap tracks general capability |\\n| full_trace | 81.76% | collapsed (v3 pending) | N/A | DeepSeek v1 label truncation bug |\\n\\n**Key insight**: Exception_only is consistently the best component on both models (even worst DeepSeek seed 91.09% > VOTA 84.45%). Cross-model gap 与 signal complexity 正相关, but exception signal's absolute effectiveness also depends on LoRA training stability. Qwen: perfectly robust (3 seeds identical). DeepSeek: 2/3 seeds at 99.33% (matching Qwen-level), 1 outlier at 91.09% (LoRA initialization). Median performance robust; seed sensitivity suggests smaller/weaker models may need training stabilization (multi-seed selection, warmup tuning) for optimal exception signal utilization.\\n\\n## VOTA Repositioning\\n\\n**旧叙事**: VOTA 是 trace compression 方法，价值在于\\\"压缩使 trace 更有效\\\"。\\n\\n**新叙事**: VOTA 是 **fault indicator isolation** 方法，核心价值在于自动从 noisy execution traces 中提取 exception events 等 diagnostic signals。\\n\\n**证据链**:\\n1. exception_only (99.83%) ≥ VOTA full (99.41%) — 压缩后的其他组件（loop, ae）不仅无益，反而引入 noise\\n2. VOTA 跨模型 gap = 14.96pp — 因为 VOTA 包含 model-dependent 的 Tier 2 组件（loop compression 需要 execution reasoning）\\n3. exception_only 在两个模型上均为最优组件 — isolate 出 Tier 1 后，相对优势 robust（虽然 DeepSeek 绝对值 seed-dependent）\\n4. vota_no_ae (99.41%) = VOTA (99.41%) — actual/expected 移除无影响，exception 是真正的 active ingredient\\n\\n**论文中的表述**: \\\"VOTA's trace compression pipeline incidentally isolates exception events — the minimal sufficient diagnostic signal. Its value lies not in making traces shorter, but in separating high-specificity fault indicators from low-specificity behavioral patterns.\\\"\\n\\n**对 Method section 的影响**: VOTA 仍然完整描述（loop compression + exception + actual/expected），但 Results/Discussion 明确指出 exception isolation 是核心机制，其他组件是 model-capability-dependent bonus。\\n\\n## Story Spine\\n\\n- **Problem**: Existing trace SFT studies (DCSH, TracePile) evaluate only generative tasks and find limited, model-dependent benefit. No prior work has tested trace SFT on verdict tasks (binary pass/fail), nor identified what trace components drive classification performance.\\n\\n- **Existing approaches & gaps**: DCSH (EMNLP Findings 2025) tested 5 trace formats on generation tasks, finding that \\\"no single trace representation consistently outperforms others.\\\" TracePile (NeurIPS 2025) scaled to 2.6M samples but only evaluated generation. TRACED (ICSE 2024) showed traces help encoder-based classification. All existing trace formats are designed for execution simulation, not fault detection.\\n\\n- **Our framing**: We reframe verdict prediction as **fault detection** and ask: what is the minimal sufficient diagnostic signal? Through systematic component ablation across two architecturally distinct models, we discover that exception events — compact, structured error summaries — are consistently the most effective trace component, achieving near-perfect accuracy on Qwen (99.83% ± 0.00, 3 seeds) and outperforming all alternatives on DeepSeek (91-99% vs VOTA 84.45%). Richer trace representations work only when the base model has sufficient execution reasoning capability, making them unreliable for general deployment.\\n\\n- **Headline result**: \\\"Exception events consistently achieve the highest verdict accuracy across models (Qwen 99.83%, DeepSeek 91-99%), outperforming VOTA traces (84.45% on DeepSeek, -14.96pp gap) — demonstrating that fault indicator isolation, not trace reasoning, is the robust mechanism for verdict prediction. DeepSeek seed sensitivity reveals LoRA training stability as a secondary factor for smaller models.\\\"\\n\\n## Story Arc\\n\\n1. **Setup**: Trace SFT for code tasks — promising but inconsistent in prior work (DCSH, TracePile). Unknown whether traces help verdict tasks and what trace design matters.\\n\\n2. **First result — traces help, compression helps more** (single model): no_trace 75.13% → full_trace 81.76% → VOTA 99.41%. Label-only loss ablation decomposes the gap: 26% gradient dilution, 74% information overload. Compression improves accuracy through higher information density, not just cost savings.\\n\\n3. **Twist — what component actually drives VOTA?** Component ablation reveals exception_only (99.83%) ≥ full VOTA (99.41%). The \\\"trace reasoning\\\" narrative is wrong — verdict prediction is fault detection. Tier 1 (exceptions + assertion-point) subsumes Tier 2 (loops). Actual/expected removal doesn't hurt (99.41%).\\n\\n4. **Cross-model stress test — consistent dominance, not universal perfection**: Exception_only is the best component on both models (even DeepSeek worst seed 91.09% > VOTA 84.45%), but absolute performance is seed-dependent on DeepSeek (91-99% vs Qwen's perfectly stable 99.83%). VOTA degrades by 14.96pp. The structurally simplest component is the most robust, but LoRA initialization sensitivity introduces variance on weaker models. Qwen seed robustness (3-seed variance = 0) + calibration (ECE=0.0027) 确认 exception signal 在强模型上的 reliability。DeepSeek seed sensitivity 揭示 training stability 作为 secondary bottleneck。\\n\\n5. **Design principle**: For verdict tasks, identify the highest-specificity diagnostic signal (exception events) and discard everything else. VOTA's value is fault indicator isolation — automatically extracting exceptions from noisy traces — not generic compression. Simpler signals are more robust; complexity tolerance depends on model capability.\\n\\n## Dataset Characteristics\\n\\n### Data duplication analysis\\n\\n| Condition | Total | Unique | Duplication rate | Cause |\\n|-----------|-------|--------|------------------|-------|\\n| exception_only_train | 4720 | 2858 | 39.45% | 同题多个 passing 解映射为相同 (input, output) — 无异常 → 同一 trace |\\n| exception_only_test | 1190 | 607 | 48.99% | 同上 |\\n| raw_traces | 5910 | 5803 | 1.81% | 完整 trace 含行号/变量值/内存地址，几乎不重复 |\\n\\n**Train-test input overlap: 0（无数据泄漏）**\\n\\n**解读**: exception_only 高重复率是 representation 的自然属性，非数据问题。多个正确解对同一测试用例执行时若均无异常，exception_only 表征退化为相同的空/无异常标记。这恰好说明 exception signal 的 compactness — 它仅编码 fault presence，不编码 solution identity。raw_traces 重复率极低 (1.81%) 因为完整 trace 包含 solution-specific 信息（变量值、内存地址）。尽管高重复率意味着有效训练样本少于名义数量，模型仍达 99.83% — 进一步确认 exception signal 的 learnability。\\n\\n## DeepSeek full_trace 处理\\n\\n**现状**: v1 坍塌（28.5%, 100% 预测 fail, 根因: 训练端 label 截断）。v2 重训启动但被 kill（Loop #6 ops worker 腾 GPU 给 vota_seed456）。v3 RUNNING（label-preserving truncation fix）。\\n\\n**处理方案**: v3 正在 cuda:0 上训练，预计 5/16 完成。\\n\\n**VOTA vs full_trace 截断机制区分** (D030 token analysis 确认):\\n- **full_trace v1**: SFTTrainer right-truncation 切掉了 verdict **label** → 100% predict fail → 坍塌。根因: DeepSeek tokenizer 对 full_trace 产生 >2048 tokens, label 在截断窗口外。\\n- **VOTA**: `to_chat_text()` 保留 verdict label（label 完整），但 91.7% 的样本 **trace content（input）被截断**（mean 2626 → ~2048 tokens）。84.45% 是真实结果，反映 trace 信息损失对模型学习的影响，**不是** label corruption。\\n- **exception_only**: token 长度远低于 2048，不受截断影响，跨模型对比 clean。\\n\\n**对论文叙事的影响**: 论文中所有 \\\"right-truncation corrupts/removes the verdict label\\\" 措辞**对 VOTA 不成立**——label 完整保留，被截断的是 trace input。正确表述: \\\"trace content truncation causes information loss\\\"。VOTA cross-model gap (14.96pp) 有两个贡献因素: (1) model capability, (2) training-time trace truncation on DeepSeek (see D11)。\\n\\n## External Benchmark (DebugBench) Positioning\\n\\n**DebugBench 仅作泛化性验证，不作 trace importance 证据。**\\n\\n| Condition | Main Dataset | DebugBench | Δ interpretation |\\n|-----------|-------------|------------|------------------|\\n| no_trace | 75.13% | 96.71% | DebugBench 天花板高，baseline 已强 |\\n| VOTA | 99.41% | 99.77% | +3.06pp lift — 边际 |\\n| exception_only | 99.83% | 100.00% | +3.29pp lift — 边际 |\\n\\n**主数据集 trace lift = 24.70pp**（no_trace → exception_only），DebugBench trace lift 不到其 1/7。\\n\\n**论文定位规则**：\\n- DebugBench → 泛化性证据（exception_only 100% = 跨数据集鲁棒性）\\n- Trace importance 论证 → 仅依赖主数据集（24.7pp lift）\\n- 禁止用 DebugBench 的 3.29pp lift 论证 \\\"trace 的核心价值\\\"——审稿人会攻击天花板效应\\n\\n## Venue Fit Risks\\n\\n| Risk | Assessment | Mitigation |\\n|------|-----------|------------|\\n| 单任务 | 仍然只在 test verdict prediction 上验证 | 跨模型验证部分弥补; Discussion 中讨论 generalization |\\n| 单数据集 | HumanEval + MBPP-sanitized 是唯一数据源 (591 problems × 10 solutions) | 定位为 empirical study, 深度优于广度; 两个标准 benchmark 组合覆盖多样编程题型; exception_only 有效训练样本仅 2858 unique 即达 99.83%, 暗示 signal 的 simplicity 降低对数据量的依赖 |\\n| \\\"只是 feature engineering\\\" | exception extraction 不复杂 | simplicity 本身是 contribution — 最简信号最 robust |\\n| Negative result 味道 | VOTA 跨模型不 robust | Reframe: 识别 robust vs non-robust 组件边界是 positive |\\n| Seed robustness (Qwen) | ✅ 已解决: 99.83% ± 0.00 (3 seeds), irreducible samples 确认 | — |\\n| Seed robustness (DeepSeek) | ✅ 3-seed 完整: 2/3 at 99.33%, 1 at 91.09% | LoRA initialization sensitivity — median robust, worst still > all alternatives; 转化为 training stability finding (D9/D10) |\\n| Calibration | ✅ 完整数据: Tier 1 ECE≤0.003, no_trace ECE=0.171 (~63x gap) | Brier ~150x gap 进一步确认 |\\n| 只用 2 个模型 | 有限但有意义的 diversity | Architecture + pretraining data (5.5T vs 2T) + CRUXEval gap (17.5pp) 构成充分差异 |\\n| 数据重复率 | exception_only 训练集 39.45% 重复 | 非数据泄漏（train-test overlap = 0）；是 representation compactness 的自然结果；有效样本仍足够学习 |\\n\\n## Anticipated Reviewer Concerns\\n\\n| Concern | Planned Response |\\n|---------|-----------------|\\n| \\\"exception_only 99.83% 是不是 trivial pattern matching [ERROR] 有无？\\\" | full_trace 也包含 [ERROR] 但仅 81.76%——模型需要从 trace context 中 extract 和 utilize exception signal, 不是简单 keyword detection. no_trace 无 exception, 75.13%. |\\n| \\\"为什么 exception_only > VOTA? adding info 反而降?\\\" | 非 exception 组件 (loop/ae tokens) 稀释 attention 对 exception 信号的聚焦. Calibration: exception_only ECE=0.0027 vs VOTA ECE=0.0054. 部分样本 loop 正常但有 exception, 引入矛盾信号. |\\n| \\\"CRUXEval gap 与 VOTA gap 的相关性可能是 coincidence\\\" | 明确标注为 hypothesis. 列出 alternatives (tokenizer efficiency, pretraining scale 2.75x, chat template). 不 overclaim. |\\n| \\\"只有 2 个模型，universality claim 太强\\\" | 同意是 limitation. 两模型在 architecture (RoPE vs ALiBi), pretraining data (5.5T vs 2T), execution reasoning (CRUXEval 17.5pp gap) 上有充分差异, 不是 trivial replication. Exception signal 的 structural simplicity 提供 inductive argument for broader generalization. |\\n| \\\"99.83% 可能 saturated, 看不出 exception 到底学了什么\\\" | Calibration 双指标: exception_only ECE=0.0027, Brier=0.0013 (近完美校准). 对比 no_trace ECE=0.1715, Brier=0.1972 (~63x/~150x gap). **Irreducible error 根因已明确**: 2/1190 errors 均因 Python `all()` 短路触发 `GeneratorExit`（`BaseException` 子类，非真正错误），tracer 将其标记为 `[ERROR]`。模型看到 7 行 `[ERROR] GeneratorExit` 合理预测 fail，但代码实际正确。整个测试集仅这 2 条含 `GeneratorExit`，无训练信号可学习其良性本质。99.83% 是 representation 的理论上限，非 saturation artifact。 |\\n| \\\"只用了 1 个 seed\\\" | Qwen ✅: 3 seeds 99.83% ± 0.00. DeepSeek ✅: 3 seeds 完整 — seed42/456=99.33%, seed123=91.09%。2/3 鲁棒，1 离群。median=99.33%, worst=91.09% (仍 > VOTA 84.45%)。论文透明报告所有 seeds，将 seed sensitivity 转化为 LoRA training stability 的 finding（D9）。 |\\n| \\\"eval_loss 上升但 accuracy 提升——checkpoint selection 有问题?\\\" | Discussion D1: token-level loss 与 binary verdict accuracy 解耦. 推荐 verdict-specific metric. Methodological contribution. |\\n| \\\"DeepSeek full_trace 坍塌是 bug 不是 finding\\\" | 诚实披露根因 (训练端 label 截断). 其他 3 条件不受影响. 修复版本如就绪则补入. |\\n| \\\"calibration 数据只有 1 个 seed\\\" | Seed robustness 已证明 accuracy variance=0 (3 seeds), calibration 在 accuracy 完全一致的前提下 expected 也一致. ECE/Brier 的极小值 (0.0027/0.0013) 留有极小 variance 空间. |\\n| \\\"DeepSeek epoch1 > epoch3, 为什么用 epoch3 报告?\\\" | 正文报告所有 seeds 的 final + best checkpoint。seed42: epoch1=99.83%, epoch3=99.33%。seed123: epoch1=91.43%, epoch3=91.09%。D7 讨论 early stopping + D9 讨论 LoRA initialization sensitivity。不 cherry-pick best seed。 |\\n| \\\"DeepSeek seed sensitivity 说明 exception signal 不 robust\\\" | Exception_only 在所有 seeds 上仍优于其他条件（worst seed 91.09% > VOTA 84.45%）。Seed sensitivity 是 LoRA training 问题而非 signal 问题——Qwen 3 seeds 完美证明 signal 本身 robust。D9 讨论 training stabilization 作为 practical recommendation。 |\\n| \\\"exception_only 数据集 ~40-49% 重复，有效训练样本不足？\\\" | 重复源自 representation compactness：同题多个 passing 解均无异常 → 相同 trace。**非数据泄漏**（train-test input overlap = 0）。raw_traces 仅 1.81% 重复，确认重复是 exception_only 表征特性而非数据收集问题。模型在有效样本仅 2858 unique 的条件下仍达 99.83%，反而说明 exception signal 的高 learnability — 少量 unique 样本即可充分学习 fault detection pattern。 |\\n\\n## Discussion 要点\\n\\n### D1: eval_loss vs verdict accuracy 解耦\\nDeepSeek VOTA: eval_loss epoch1→3 从 0.068 升至 0.112 (+65%), 但 accuracy 从 78.15% 升至 84.45% (+6.3pp). Token-level calibration 与 binary classification accuracy 方向相反. **Implication**: verdict tasks 应用 task-specific metric (accuracy/F1) 做 checkpoint selection, 非 eval_loss.\\n\\n### D2: CRUXEval gap 假说 (revised — D030 confound)\\nVOTA 跨模型 gap (14.96pp) 与 CRUXEval execution reasoning gap (15-17.5pp) 数值吻合. 假说: trace utilization effectiveness 受 base model \\\"execution reasoning readiness\\\" 约束. **标注**: hypothesis, N=2, 列出 alternatives. 不 overclaim. **注意**: 我们的训练/测试数据来自 HumanEval + MBPP-sanitized（非 CRUXEval），CRUXEval-I 分数仅作为衡量两个模型 execution reasoning 能力差异的外部参照。论文中必须明确区分数据来源与外部基准引用。**D030/D034 truncation evidence**: 14.96pp gap 中截断效应有因果证据: group_analysis 显示 train-truncated 83.04% vs train-intact 100% (Fisher p≈0, 推理时无截断)。截断因果方向可 claim，模型能力差异是 residual confound。CRUXEval gap 数值吻合可能部分巧合。论文中截断效应应作为 established factor 讨论（有 group_analysis 因果证据），模型能力假说标注为 residual confound hypothesis。\\n\\n### D3: Simplicity as robustness (revised)\\nException signal 在两模型上均为最优组件，其结构简单性确保了相对优势的跨模型 robustness。但 DeepSeek seed sensitivity 揭示：simplicity 确保 signal 本身 robust，但 LoRA 训练过程是否稳定收敛到正确映射取决于模型。**trace design 应匹配 deployment model 的能力下界**，且需关注 training stability（建议：多 seed 验证 + 考虑 training stabilization 技巧如 warmup、learning rate schedule）。\\n\\n### D4: Checkpoint selection 与 gap 报告 (revised)\\n正文报告所有 seeds 的 final checkpoint 结果 + best checkpoint 结果，不 cherry-pick。DeepSeek seed42: epoch1=99.83%, epoch3=99.33%（退化 0.50pp）。DeepSeek seed123: epoch1=91.43%, epoch3=91.09%（退化 0.34pp）。两个 seed 均显示轻微 epoch 退化，但核心差异在 epoch1 起点（8.40pp gap），不是训练过程。\\n\\n### D5: Irreducible samples — GeneratorExit 根因分析\\n3 seeds 的 2/1190 errors 完全相同（id=901, 905, 均来自 HumanEval/95 `check_dict_case`），方向一致（pass→fail false negatives）。\\n\\n**根因**: Python `all()` 对 generator expression 短路时丢弃未耗尽的 generator，触发 `GeneratorExit`。`GeneratorExit` 继承自 `BaseException`（非 `Exception`），是 Python 内部控制流机制而非真正错误。但 tracer 对所有 caught exceptions 统一标记 `[ERROR]`，导致 exception_only 模型看到 7 行 `[ERROR] GeneratorExit`，合理但错误地预测 fail。\\n\\n**为何不可约**:\\n1. **表征局限**: exception_only 条件下模型仅见异常数据，无法访问控制流、返回值或 assertion 结果。`GeneratorExit` 在此表征中与真正错误不可区分。\\n2. **跨 seed 确定性**: 3 个 random seeds 产生完全相同的 errors，确认这是 data/representation 属性而非模型初始化随机性。\\n3. **训练集无信号**: 整个 1190 条测试集仅这 2 条含 `GeneratorExit`，训练集中也缺乏足够的 `GeneratorExit` 良性样本供模型学习。\\n4. **人类也会犯错**: 仅看 exception trace（7 行 `[ERROR]`），人类审查者在不了解 Python generator protocol 的情况下也会预测 fail。\\n\\n**对论文的意义**: (1) 99.83% 是 exception_only representation 在此数据集上的理论 ceiling，非 saturation artifact；(2) 揭示 tracer 设计的改进方向——区分 `BaseException` 子类（如 `GeneratorExit`, `KeyboardInterrupt`）与 `Exception` 子类（真正的程序错误）可消除此类 irreducible error；(3) 提供 concrete evidence 说明 exception_only 模型\\\"理解\\\"的是 `[ERROR]` tag 的 fault indicator 语义，而非 exception type 的 fine-grained 含义。\\n\\n### D6: Calibration as secondary evidence\\nCalibration 数据提供独立于 accuracy 的 evidence dimension。no_trace Brier=0.1972 说明模型无 trace 时不仅预测错，且对错误预测过度自信。exception_only Brier=0.0013 说明模型在有 exception signal 时几乎完美区分确定性和不确定性。这支持 Claim 1 的 \\\"sufficient signal\\\" 论点——exception 不仅让模型预测对，还让模型 \\\"知道自己对\\\"。\\n\\n### D7: Early stopping for exception signal (revised — D030 epoch1 data complete)\\n3-seed epoch1 完整数据：seed42 epoch1=99.83% → epoch3=99.33%（-0.50pp）；**seed456 epoch1=99.33% → epoch3=99.33%（0.00pp）**；seed123 epoch1=91.43% → epoch3=91.09%（-0.34pp）。**seed42 的 epoch1=99.83%（匹配 Qwen）是该 seed 独有的 LoRA 初始化运气，不是 DeepSeek epoch1 的通用属性。** seed456 epoch1=epoch3 说明 epoch 退化非普遍现象。核心差异仍是 LoRA 初始化（epoch1 起点差 8.40pp），不是 overfitting。Early stopping 无法挽救差的初始化（seed123）。**Implication**: (1) 报告 DeepSeek 结果时应使用 median/2-of-3 (99.33%)，不应以 seed42 epoch1=99.83% 作为 headline；(2) epoch1 peak 是 LoRA 初始化运气的副产物，不具推广性。对比: VOTA 在 DeepSeek 上 84.45% **已确认正确**（D030 关闭: confirmatory re-eval max_length=16384 → 84.45%，与原始训练评估精确一致；D030 根因是 evaluate.py v2 的 max_length=2048 eval-time 截断 bug 导致 82.6% 预测为 garbage tokens）。\\n\\n### D9: LoRA initialization sensitivity as secondary bottleneck [NEW — D028]\\nDeepSeek exception_only seed42=99.83% vs seed123=91.43% (epoch1), 8.40pp gap。Qwen 3 seeds 完全一致。假说：exception signal 的 learnability 取决于 (1) signal 本身的结构简单性（cross-model robust）+ (2) LoRA 初始化是否落入能正确映射 exception→verdict 的 basin。Qwen-7B 可能因模型更强/LoRA landscape 更平滑而对初始化不敏感。DeepSeek-6.7B（CRUXEval-I 39% vs Qwen 56.5%）的 loss landscape 可能更 rugged，LoRA 初始化更易陷入 suboptimal basin（seed123 的 fail_recall 仅 70-72% 说明模型未学到 exception→fail 映射的关键部分）。**论文角度**: 这不是 negative result——它揭示了 trace SFT 的 practical consideration（training stability），可作为 contribution 的一部分。建议 Discussion 讨论 training stabilization 策略（warmup, lr schedule, LoRA rank 调整, multi-seed selection）。\\n\\n### D10: Train loss ≈ but accuracy ≠ across seeds [NEW — D029]\\nDeepSeek exception_only seed456 (train_loss=0.1225) 与 seed123 (train_loss=0.122) 训练损失几乎相同，但 accuracy 差 8.2pp（99.33% vs 91.09%）。关键差异集中在 fail_recall（1.0 vs 0.705）——token-level loss 在所有 tokens 上平均，掩盖了 fail 类少数样本的 sample-level 分类能力差异。**Implication**: (1) 扩展 D1 (eval_loss vs accuracy decoupling) 到训练阶段：train_loss 同样不是 verdict task accuracy 的可靠代理指标；(2) 对 checkpoint selection 的实际建议更强：必须用 task-specific metric (accuracy/F1)，甚至 train_loss 收敛也不保证 task performance；(3) fail 类作为少数类（28.5%），其学习质量被平均 loss 稀释——这在 class-imbalanced 设置下是 general pattern，可推广到其他 verdict/detection 任务。\\n\\n### D11: VOTA cross-model gap: training-time trace truncation as causal factor [NEW — D030 token analysis + group_analysis]\\nD030 token analysis 确认: `to_chat_text()` 保留 labels（verdict label 在训练时未被截断），但 91.7% 的 DeepSeek VOTA 训练样本的 **trace content** 从 mean 2626 tokens 被截断到 ~2048 tokens。\\n\\n**Group analysis 提供因果证据**: 将测试集按训练截断状态分组（推理时无截断, max_length=16384），train-truncated 组 accuracy=83.04% vs train-intact 组 accuracy=100%, Fisher exact p≈0。**截断的因果方向可以 claim**: 训练时 trace 被截断导致模型学到的信息不完整 → 推理时即使看到完整 trace 也无法正确判断。模型能力差异是残余 confound（无法完全分离）。\\n\\n**Implications**: (1) 论文中所有 \\\"right-truncation corrupts/removes the verdict label\\\" 措辞对 VOTA 不成立——label 完整保留，被截断的是 trace INPUT content；(2) 14.96pp gap 中截断效应有因果证据（group_analysis），模型能力差异是 residual confound；(3) exception_only 因 token 长度短（远低于 2048）不受截断影响，其跨模型对比更 clean——进一步强化 Claim 1 \\\"most robust component\\\" 叙事；(4) 论文应讨论 max_length 的影响作为 limitation/future work；(5) group_analysis 数据可作为 Table/Figure 纳入论文——展示截断的因果效应。\\n\\n### D8: Data duplication as representation signature\\nexception_only 训练集 39.45% 重复（4720→2858 unique），测试集 48.99%（1190→607 unique），而 raw_traces 仅 1.81%（5910→5803 unique）。重复源自 exception_only 表征的 design-by-intent compactness：同一编程题的多个 passing 解执行时均无异常，exception_only 表征退化为相同的空标记。这一数据特征本身就是 Claim 3 two-tier hierarchy 的佐证——Tier 1 信号仅编码 fault presence/absence，不编码 solution-level details，因此天然高重复。Train-test input overlap = 0 排除数据泄漏。\\n\\n## Contingency Framing (已解决, 留存档)\\n\\n### Claim 1 — RESOLVED (D029: seed456=99.33% confirms \\\"consistently best component\\\")\\nseed456 与 seed42 完全一致（均 99.33%），seed123 为孤立离群值。Claim 1 定稿为 \\\"exception events consistently best component across models; absolute performance seed-dependent on DeepSeek (2/3 seeds robust, 1 outlier from LoRA init sensitivity); relative dominance over all alternatives robust across all seeds\\\"。\\\"0pp universal gap\\\" 叙事已放弃，转为数据驱动的 nuanced framing。\\n\\n### Claim 2 — RESOLVED (D006 + D009)\\nv5 full_trace 81.76%. plan_002 label-only 86.22%, gradient dilution = minor (26%). 跨模型 VOTA gap 补充证据.\\n\\n## 与 v1 Framing 的关键差异\\n\\n| 维度 | v1 | v2.9 |\\n|------|----|----|\\n| Headline | VOTA compression 优于 full trace | Exception events are the most effective diagnostic signal |\\n| Primary claim | VOTA +24pp through fault indicator preservation | Exception signal consistently best across models; absolute performance seed-dependent on DeepSeek |\\n| Claim 2 | Compression > full trace (只有 gradient dilution) | Information density primary + gradient dilution quantification + cross-model reinforcement |\\n| Claim 3 Tier 1 | exception_only only | exception + assertion-point (co-Tier 1, D020) |\\n| VOTA 定位 | 核心方法 — trace compression | **Fault indicator isolation** — 价值在于提取 exception, 非 generic compression |\\n| Model scope | 单模型 (Qwen) | 双模型, 跨模型对比是核心贡献 |\\n| DeepSeek full_trace | N/A | v1 collapsed (label truncation), v3 pending |\\n| Seed robustness | 未验证 | Qwen ✅ 99.83% ± 0.00 (3 seeds); DeepSeek ⚠️ seed-dependent (91-99%, D028) |\\n| Irreducible error | 未分析 | ✅ GeneratorExit 根因明确，99.83% = representation ceiling |\\n| Calibration | 未验证 | ✅ 完整 ECE+Brier, ~63x/~150x gap vs no_trace |\\n| Data duplication | 未分析 | ✅ exception_only ~40% 重复（representation compactness），train-test overlap = 0 |\\n| Early stopping | 未讨论 | DeepSeek epoch1→epoch3 轻微退化 (0.3-0.5pp); 核心问题是 LoRA 初始化 (seed123 epoch1=91.43%), 非 overfitting |\\n| Narrative arc | \\\"VOTA helps\\\" | \\\"Exception events are consistently best; VOTA's value is isolating them; training stability matters\\\" |\\n\", \"total_chars\": 30551, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "53d6cdab-0acd-43c4-ad32-465c66422075",
  "isSidechain": true,
  "promptId": "1671510c-98af-4e06-a3f5-68dced519a8b",
  "agentId": "ac10b8784a4950006",
  "type": "user",
  "uuid": "1cf2584e-5496-440b-a997-d9ae7c8172f3",
  "sourceToolAssistantUUID": "53d6cdab-0acd-43c4-ad32-465c66422075",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "ab493159-c57d-451b-9109-6ba744c1f6a1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T16:33:51.786Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01CoGCLBuGAWZ6jzjYQgwgXa`</summary>

```json
{
  "project": "trace-verdict-study",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1cf2584e-5496-440b-a997-d9ae7c8172f3",
  "isSidechain": true,
  "agentId": "ac10b8784a4950006",
  "requestId": "req_011Cb6a2RFteXWsVa9YQEuMt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "764e7701-2e3a-4a61-b72d-ed1810a57cb9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "ab493159-c57d-451b-9109-6ba744c1f6a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WWRuTyavnFCpBTJknRaeFc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14625,
      "cache_read_input_tokens": 17017,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14625,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
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

_source line 10 · 2026-05-16T16:33:51.795Z_

<details><summary>↩ Tool result · `toolu_01CoGCLBuGAWZ6jzjYQgwgXa`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'trace-verdict-study'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "764e7701-2e3a-4a61-b72d-ed1810a57cb9",
  "isSidechain": true,
  "promptId": "1671510c-98af-4e06-a3f5-68dced519a8b",
  "agentId": "ac10b8784a4950006",
  "type": "user",
  "uuid": "91039487-9d14-4562-89d7-f72549847616",
  "sourceToolAssistantUUID": "764e7701-2e3a-4a61-b72d-ed1810a57cb9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "ab493159-c57d-451b-9109-6ba744c1f6a1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T16:33:52.112Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Wg8gCuM3FD9txCBsJWywsZ`</summary>

```json
{
  "project": "trace-verdict-study",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91039487-9d14-4562-89d7-f72549847616",
  "isSidechain": true,
  "agentId": "ac10b8784a4950006",
  "requestId": "req_011Cb6a2RFteXWsVa9YQEuMt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "213124df-9e33-45fa-9b67-a26c0c23aa65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "ab493159-c57d-451b-9109-6ba744c1f6a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WWRuTyavnFCpBTJknRaeFc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14625,
      "cache_read_input_tokens": 17017,
      "output_tokens": 197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 14625
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 197,
          "cache_read_input_tokens": 17017,
          "cache_creation_input_tokens": 14625,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 14625,
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

_source line 12 · 2026-05-16T16:33:52.135Z_

<details><summary>↩ Tool result · `toolu_01Wg8gCuM3FD9txCBsJWywsZ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/ROADMAP.md\", \"content\": \"# trace-verdict-study — Research Dashboard\\n\\n> 最后更新: 2026-05-16 11:23 UTC | 更新原因: Fix premature ✅ on ≥99.8% edit; adjust GPU scheduling per Reviewer (codellama13b_exception_only to cuda:0 for earlier result); add prediction overlap task\\n\\n## 核心方向\\nException events 是 verdict prediction 的 **most effective trace component**——跨 scale（1.5B/7B）和跨家族验证中。Qwen-7B 99.83% ± 0.00 (3 seeds)，Qwen-1.5B 99.83%（= 7B，scale-invariant）。详见 paper_framing.md v3.0。\\n\\n## 投稿目标\\n- **Primary**: EMNLP 2026 Main (ARR May 25, DDL 9 天)\\n\\n## 当前进展\\n- **阶段**: Scope Expansion（Round 5 审稿驱动）+ Paper Agent Full Draft 暂停等新数据\\n- **原始 plan**: 11/11 完成 (10 success, 1 negative)\\n- **Round 5 审稿**: 5 critical + 5 major issues → Action Matrix 已全部派发\\n- **Scope expansion**: 加 Qwen-1.5B（scale diversity）+ CodeLlama-13B（family diversity + larger scale）\\n\\n### Qwen-1.5B 结果 (3/4 done)\\n| Condition | Accuracy | vs 7B | 解读 |\\n|-----------|----------|-------|------|\\n| exception_only | 99.83% | = 7B | **Scale-invariant**，signal-limited |\\n| VOTA | 99.58% | ≈ 7B 99.41% | Near-identical |\\n| no_trace | 67.31% | < 7B 75.13% (-7.82pp) | **Scale-sensitive**，capacity matters without signal |\\n| full_trace | RUNNING | — | cuda:0 |\\n\\n### CodeLlama-13B: Model ready, 0/3 done\\n- exception_only / no_trace / vota → queued, waiting GPU\\n\\n### Multi-seed robustness (Round 5 R2-N3 response)\\n| Condition | Seeds | Mean ± σ | Status |\\n|-----------|-------|----------|--------|\\n| exception_only | 42/123/456 | 99.83% ± 0.00 | ✅ Done |\\n| ae_only | 42/123/456 | 99.64% ± 0.48 | ✅ Done |\\n| label_only | 42/123/456 | 86.39% mean | ✅ Done |\\n| loop_only | 42/123/456 | 42 done, 123 RUNNING, 456 queued | 🔄 |\\n\\n### Format marker removal (R1-N1 response)\\n- exception_only_nomarker_seed42/123/456 → planned, after CodeLlama\\n\\n### Paper edits (Round 5)\\n- ⏳ Claims threshold: ≥99.8% → ≥99%（3 处残留，urgent fix 已派发）\\n- ✅ SBFL/fault localization references added\\n- ✅ Discussion expanded (~0.5 page)\\n- ✅ Title: removed \\\"Cross-Model\\\"\\n- ✅ McNemar p-value attribution fixed\\n- ✅ DebugBench removed from Conclusion future work\\n- ✅ Cluster-robust CI computed (problem_id clusters)\\n- ⏳ Causal language downgraded (approximate decomposition)\\n- ⏳ Truncation caveat on 14.96pp gap\\n- ⏳ Scope qualifier in Abstract\\n- ⏳ Conclusion future work: remove \\\"larger model scales\\\"（1.5B 已验证）\\n- ⏳ 1.5B 数据集成到 Table 1（等 full_trace 完成后统一写入）\\n\\n## 近期任务\\n- [ ] qwen15b_full_trace_seed42 完成 → 1.5B grid complete\\n- [ ] Prediction overlap: 1.5B vs 7B exception_only 错误样本对比（零 GPU cost）\\n- [ ] loop_only_seed123 + seed456 完成\\n- [ ] codellama13b × 3 experiments（exception_only 最高优先级）\\n- [ ] format marker removal × 3\\n- [ ] Paper integration: Table 1 + cross-scale analysis + CodeLlama rows\\n- [ ] Re-submit to Review Director for Round 6\\n\\n## GPU 预算\\n- 本地分配: cuda:0 + cuda:1 (westd-11235)\\n- cuda:0: qwen15b_full_trace (RUNNING) → **codellama13b_exception_only**（最高优先级）\\n- cuda:1: loop_only_seed123 (RUNNING) → loop_only_seed456 → codellama13b_no_trace\\n\\n## 9 天冲刺路线 (修订 v9)\\n| 日期 | 里程碑 |\\n|------|--------|\\n| 5/16 (今天) | qwen15b_full_trace + loop_only seeds 完成 | codellama13b_exception_only 今晚出结果 |\\n| 5/17 | codellama13b × 3 完成 + format marker removal 开始 |\\n| 5/18 | 所有新实验完成 → Paper Agent patch 整合新数据 |\\n| 5/19-20 | Reviewer 对抗 Round 6 + 迭代修改 |\\n| 5/21-23 | 论文定稿 + appendix + 最终检查 |\\n| 5/24 | 提交 ARR |\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D053 | 2026-05-16 | 升级 signal-limited claim 从 Discussion finding 到正式 f | codellama13b_exception_only_seed42, qwen15b_exception_only_seed42, deepseek_exception_only_seed42 |\\n| D052 | 2026-05-16 | CodeLlama-13B no_trace=76.47% 确认 scale monotonic p | codellama13b_no_trace_seed42, codellama13b_exception_only_seed42 |\\n| D051 | 2026-05-16 | DeepSeek vs Qwen exception_only gap 根因：MBPP/113 ca | deepseek_exception_only_seed42, qwen15b_exception_only_seed42 |\\n| D050 | 2026-05-16 | Qwen-1.5B 4条件 grid 完成：scale sensitivity 与 signal d | qwen15b_full_trace_seed42, qwen15b_exception_only_seed42, qwen15b_no_trace_seed42 |\\n| D049 | 2026-05-16 | Prediction overlap 确认 universal irreducible ceilin | qwen15b_exception_only_seed42, exception_only_seed123, deepseek_exception_only_seed42 |\\n| D048 | 2026-05-16 | Scale-invariance 定位为 Discussion finding，不升 Claim；C | qwen15b_exception_only_seed42, qwen15b_no_trace_seed42, codellama13b_exception_only_seed42 |\\n| D047 | 2026-05-16 | DebugBench 跨任务验证 + regex baseline 全部完成，exception d | debugbench_exception_only, debugbench_vota, debugbench_no_trace, regex_baseline |\\n| D046 | 2026-05-16 | Regex baseline 证实 SFT 必要性：最强标准 regex 93.61%，SFT 99 | — |\\n| D045 | 2026-05-16 | Regex baseline 确认 SFT 必要性：best regex 93.61% vs SFT | regex_baseline |\\n| D044 | 2026-05-16 | 对抗审稿 Borderline：立即补 regex baseline + label_only/ae | — |\\n\\n\", \"total_chars\": 4676, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "213124df-9e33-45fa-9b67-a26c0c23aa65",
  "isSidechain": true,
  "promptId": "1671510c-98af-4e06-a3f5-68dced519a8b",
  "agentId": "ac10b8784a4950006",
  "type": "user",
  "uuid": "52ca1dee-d2a6-4be6-b5a1-665badcd7d8e",
  "sourceToolAssistantUUID": "213124df-9e33-45fa-9b67-a26c0c23aa65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "ab493159-c57d-451b-9109-6ba744c1f6a1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T16:33:55.001Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01KEzyKq3QoDhi5tTssNahvv`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52ca1dee-d2a6-4be6-b5a1-665badcd7d8e",
  "isSidechain": true,
  "agentId": "ac10b8784a4950006",
  "requestId": "req_011Cb6a3WvEmwbEKo9jHYD8W",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5072b9e7-0939-4ecd-9e61-80c9f349f50c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "ab493159-c57d-451b-9109-6ba744c1f6a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TyNFN8zAY9PbxZuknj7cJi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2698,
      "cache_read_input_tokens": 31642,
      "output_tokens": 97,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2698
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 97,
          "cache_read_input_tokens": 31642,
          "cache_creation_input_tokens": 2698,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2698,
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

_source line 14 · 2026-05-16T16:33:55.026Z_

<details><summary>↩ Tool result · `toolu_01KEzyKq3QoDhi5tTssNahvv`</summary>

```text
artifacts/dream_reports/dream_20260515T013018/best/paper.tex
artifacts/dream_reports/dream_20260515T013018/median/paper.tex
artifacts/dream_reports/dream_20260515T013018/worst/paper.tex
artifacts/dream_reports/dream_20260515T084908/best/paper.tex
artifacts/dream_reports/dream_20260515T084908/median/paper.tex
artifacts/dream_reports/dream_20260515T084908/worst/paper.tex
artifacts/_project/paper/related_work.tex
artifacts/per_class_breakdown.tex
artifacts/_project/paper/section3_experimental_setup_d4f1e8.tex
artifacts/_project/paper/section3_experimental_setup.tex
artifacts/_project/paper/ethics_statement.tex
artifacts/_project/paper/ethics_statement_77cf5f.tex
docs/paper/arr_checklist.tex
artifacts/_project/paper/arr_checklist.tex
docs/paper/method.tex
docs/paper/related_work.tex
artifacts/_project/paper/main_results_tables.tex
artifacts/_project/paper/main_results_tables_d8c8b6.tex
artifacts/paper_tables/main_results_tables.tex
artifacts/_project/paper/experiments.tex
artifacts/dream_reports/dream_20260516T105259/best/paper.tex
docs/paper/experiments.tex
artifacts/dream_reports/dream_20260516T105259/median/paper.tex
artifacts/dream_reports/dream_20260516T105259/worst/paper.tex
docs/paper/conclusion.tex
docs/paper/discussion.tex
docs/paper/appendix.tex
docs/paper/main.tex
docs/paper/introduction.tex
artifacts/dream_reports/dream_20260516T155731/best/paper.tex
artifacts/dream_reports/dream_20260516T155731/median/paper.tex
artifacts/dream_reports/dream_20260516T155731/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5072b9e7-0939-4ecd-9e61-80c9f349f50c",
  "isSidechain": true,
  "promptId": "1671510c-98af-4e06-a3f5-68dced519a8b",
  "agentId": "ac10b8784a4950006",
  "type": "user",
  "uuid": "dea557f3-8075-450c-b4f8-38007128b8d5",
  "sourceToolAssistantUUID": "5072b9e7-0939-4ecd-9e61-80c9f349f50c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "ab493159-c57d-451b-9109-6ba744c1f6a1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T16:33:58.735Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PhAfRVssy94Mzdp8FXmxvH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260516T155731/best/paper.tex",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dea557f3-8075-450c-b4f8-38007128b8d5",
  "isSidechain": true,
  "agentId": "ac10b8784a4950006",
  "requestId": "req_011Cb6a3j9hGPQ4Uq8akqVXQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "10c9fc7c-1766-4d03-8f3b-c6b842ba9b48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "ab493159-c57d-451b-9109-6ba744c1f6a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UbCKordAYv4G7J5nPR1Gom",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 598,
      "cache_read_input_tokens": 34340,
      "output_tokens": 117,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 598
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 117,
          "cache_read_input_tokens": 34340,
          "cache_creation_input_tokens": 598,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 598,
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

_source line 16 · 2026-05-16T16:33:58.742Z_

<details><summary>↩ Tool result · `toolu_01PhAfRVssy94Mzdp8FXmxvH`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{times}
4	\usepackage{booktabs}
5	\usepackage{amsmath}
6	\usepackage{graphicx}
7	\usepackage{multirow}
8	\usepackage{xcolor}
9	\usepackage{hyperref}
10	\usepackage{natbib}
11	
12	\title{Exception Events Are All You Need for Verdict Prediction}
13	
14	\author{Anonymous}
15	
16	\date{}
17	
18	\begin{document}
19	\maketitle
20	
21	\begin{abstract}
22	Execution traces have shown promise for improving code understanding, yet no prior work has systematically evaluated which trace components drive verdict prediction (binary pass/fail classification). We reframe verdict prediction as fault detection and conduct a component-level ablation across four models spanning three architecture families (Qwen, DeepSeek, LLaMA) at two scales. Our key finding: exception events---compact structured error summaries---consistently achieve the highest accuracy across all models tested (99.83\% on Qwen-2.5-Coder-7B with zero variance across 3 seeds; 99.83\% on CodeLlama-13B; 99.33\% on DeepSeek-Coder-6.7B), outperforming full VOTA traces by 0.42--14.88 percentage points. We further demonstrate that this performance stems from genuine fault semantics learning rather than format-level shortcuts: removing format markers produces zero accuracy degradation (McNemar $p$=1.0, 3 seeds). A two-tier diagnostic hierarchy emerges where Tier~1 signals (exceptions, assertion-points) are individually near-perfect and sufficient, while Tier~2 signals (loop compression) are model-dependent and subsumed. These results establish that verdict-optimized trace design should extract highest-specificity diagnostic signals and discard everything else.
23	\end{abstract}
24	
25	\section{Introduction}
26	
27	Execution traces capture the dynamic behavior of programs and have been explored as training signals for code language models \cite{ni2024next,jain2024tracepile}. Prior work on trace-augmented supervised fine-tuning (SFT) has focused primarily on generative tasks---code completion, output prediction---and reported mixed results. DCSH \cite{ni2024next} tested five trace formats on generation tasks and found ``no single trace representation consistently outperforms others.'' TracePile \cite{jain2024tracepile} scaled to 2.6M samples but evaluated only generation. TRACED \cite{dinella2022traced} demonstrated traces help encoder-based classification but did not isolate which trace components matter.
28	
29	A critical gap remains: \emph{what trace components drive verdict prediction} (binary pass/fail classification), and \emph{why}? We argue that verdict prediction is fundamentally a \textbf{fault detection} task, and that the most effective signal is not a rich execution narrative but rather the \textbf{exception event}---a compact, structured diagnostic moment recording error type and message.
30	
31	Through systematic component ablation across four models from three architecture families (Qwen-2.5-Coder-7B/1.5B, DeepSeek-Coder-6.7B, CodeLlama-13B-Instruct) we establish three claims:
32	
33	\begin{enumerate}
34	    \item \textbf{Exception events are the most effective trace component} for verdict prediction, consistently outperforming all alternatives across all models tested.
35	    \item \textbf{Information density, not gradient dilution}, is the primary bottleneck explaining why trace compression helps---even oracle loss masking cannot close the 13pp gap between full traces and targeted extraction.
36	    \item \textbf{A two-tier diagnostic hierarchy} exists: Tier~1 signals (exceptions, assertion-points) are individually sufficient; Tier~2 signals (loop patterns) are model-dependent and subsumed.
37	\end{enumerate}
38	
39	We further validate that exception signal effectiveness derives from fault semantics rather than format shortcuts, through a controlled format-marker ablation yielding zero performance degradation across 3 seeds.
40	
41	\section{Method}
42	
43	\subsection{Task Formulation}
44	
45	Given a program $P$, test input $x$, and execution trace $T(P, x)$, verdict prediction is the binary classification task: $f(T(P, x)) \rightarrow \{\texttt{pass}, \texttt{fail}\}$. We study how different representations of $T$ affect classification accuracy under LoRA SFT.
46	
47	\subsection{Dataset}
48	
49	We construct our dataset from HumanEval (164 problems) and MBPP-sanitized (427 problems), totaling 591 problems. Each problem is solved by 10 LLM-generated solutions, yielding 5,910 samples with execution traces collected via a Python tracer. The train/test split is 4,720/1,190 samples (problem-level split, zero train-test input overlap).
50	
51	\subsection{Trace Representations}
52	
53	\paragraph{Full Trace.} Complete line-by-line execution trace including variable states, control flow, and all events.
54	
55	\paragraph{VOTA (Verdict-Optimized Trace Abstraction).} A compressed representation that isolates three components:
56	\begin{itemize}
57	    \item \textbf{Exception events}: Structured error summaries in the format \texttt{[ERROR] type: XxxError, message: ...}
58	    \item \textbf{Loop compression}: Iteration patterns condensed into behavioral summaries
59	    \item \textbf{Actual/Expected}: Output comparison at assertion points
60	\end{itemize}
61	
62	\paragraph{Component Ablations.} We isolate individual VOTA components:
63	\begin{itemize}
64	    \item \texttt{exception\_only}: Only exception event data
65	    \item \texttt{ae\_only}: Only assertion-point (actual/expected) data
66	    \item \texttt{loop\_only}: Only loop compression data
67	    \item \texttt{no\_trace}: No trace information (instruction + code only)
68	\end{itemize}
69	
70	\subsection{Training Setup}
71	
72	All models are fine-tuned with LoRA (rank 16, $\alpha$=32) for 3 epochs using SFTTrainer. Max sequence length is 2,048 tokens. We evaluate with 3 random seeds per condition on primary models.
73	
74	\section{Experiments}
75	
76	\subsection{Claim 1: Exception Dominance Across Models}
77	
78	\paragraph{Qwen-2.5-Coder-7B (Primary).} Table~\ref{tab:qwen_main} shows results across all trace conditions. Exception-only achieves 99.83\% with perfect seed robustness (std=0.00 across 3 seeds), outperforming full VOTA (99.41\%) by 0.42pp ($p$=0.01).
79	
80	\begin{table}[t]
81	\centering
82	\small
83	\begin{tabular}{lcccc}
84	\toprule
85	\textbf{Condition} & \textbf{Acc.} & \textbf{ECE} & \textbf{Brier} \\
86	\midrule
87	exception\_only & 99.83\% & 0.0027 & 0.0013 \\
88	ae\_only & 99.92\% & 0.0004 & 0.0008 \\
89	VOTA (full) & 99.41\% & 0.0054 & 0.0050 \\
90	loop\_only & 85.63\% & 0.0831 & --- \\
91	full\_trace & 81.76\% & 0.0958 & --- \\
92	full\_trace (label-only) & 86.22\% & 0.1107 & --- \\
93	no\_trace & 75.13\% & 0.1715 & 0.1972 \\
94	\bottomrule
95	\end{tabular}
96	\caption{Verdict prediction accuracy, ECE, and Brier score on Qwen-2.5-Coder-7B (seed 42). Tier~1 signals (exception, ae) achieve near-perfect accuracy \emph{and} calibration.}
97	\label{tab:qwen_main}
98	\end{table}
99	
100	\paragraph{Seed Robustness (Qwen).} Table~\ref{tab:qwen_seeds} confirms zero variance across 3 seeds, with identical error samples (id=901, 905) in all runs---establishing 99.83\% as the representation ceiling.
101	
102	\begin{table}[t]
103	\centering
104	\small
105	\begin{tabular}{lccc}
106	\toprule
107	\textbf{Seed} & \textbf{Accuracy} & \textbf{95\% CI} & \textbf{Errors} \\
108	\midrule
109	42 & 99.83\% & [99.58, 100] & 2/1190 \\
110	123 & 99.83\% & [99.58, 100] & 2/1190 \\
111	456 & 99.83\% & [99.58, 100] & 2/1190 \\
112	\midrule
113	\textbf{Mean $\pm$ Std} & \multicolumn{3}{c}{99.83\% $\pm$ 0.00} \\
114	\bottomrule
115	\end{tabular}
116	\caption{Qwen exception\_only across 3 seeds. All seeds produce identical errors on the same 2 samples (GeneratorExit edge cases).}
117	\label{tab:qwen_seeds}
118	\end{table}
119	
120	\paragraph{Cross-Family Validation (4 Models).} Table~\ref{tab:cross_family} demonstrates exception dominance across three architecture families. CodeLlama-13B-Instruct achieves 99.83\% on exception\_only versus 92.94\% on VOTA, confirming the pattern extends to the LLaMA family.
121	
122	\begin{table}[t]
123	\centering
124	\small
125	\begin{tabular}{llccc}
126	\toprule
127	\textbf{Model} & \textbf{Family} & \textbf{VOTA} & \textbf{exc\_only} & \textbf{$\Delta$} \\
128	\midrule
129	Qwen-2.5-7B & Qwen & 99.41\% & 99.83\% & +0.42 \\
130	Qwen-2.5-1.5B & Qwen & 99.58\% & 99.83\% & +0.25 \\
131	DeepSeek-6.7B & DeepSeek & 84.45\% & 99.33\% & +14.88 \\
132	CodeLlama-13B & LLaMA & 92.94\% & 99.83\% & +6.89 \\
133	\bottomrule
134	\end{tabular}
135	\caption{Exception dominance across 4 models $\times$ 3 families $\times$ 2 scales. Exception\_only outperforms VOTA on every model (mean $\Delta$=+5.61pp).}
136	\label{tab:cross_family}
137	\end{table}
138	
139	\paragraph{CodeLlama-13B Detail.} CodeLlama-13B-Instruct on VOTA achieves 92.94\% (CI [91.4, 94.4]), with pass\_precision=0.93, pass\_recall=0.98, fail\_precision=0.93, fail\_recall=0.80. The VOTA gap pattern is consistent: models with weaker execution reasoning show larger degradation on VOTA's Tier~2 loop component, while exception signal remains uniformly high.
140	
141	\subsection{Format Independence: Ruling Out Shortcuts}
142	
143	A potential concern is that the model exploits a format-level shortcut---specifically, pattern-matching the marker string \texttt{[No exception data in trace]} to predict pass. We test this by removing all format markers and retraining.
144	
145	\paragraph{Setup.} We remove the \texttt{[No exception data in trace]} marker from all pass samples in the exception\_only condition, leaving them as empty or minimal traces. Models are retrained from scratch across 3 seeds.
146	
147	\begin{table}[t]
148	\centering
149	\small
150	\begin{tabular}{lccccc}
151	\toprule
152	\textbf{Condition} & \textbf{Seed 42} & \textbf{Seed 123} & \textbf{Seed 456} & \textbf{Mean} & \textbf{Std} \\
153	\midrule
154	Original & 99.83\% & 99.83\% & 99.83\% & 99.83\% & 0.00 \\
155	No-marker & 99.83\% & 99.83\% & 99.83\% & 99.83\% & 0.00 \\
156	\midrule
157	$\Delta$ & 0.00pp & 0.00pp & 0.00pp & 0.00pp & --- \\
158	\bottomrule
159	\end{tabular}
160	\caption{Format marker ablation (Qwen exception\_only). Removing the \texttt{[No exception data in trace]} marker produces zero degradation across all seeds (McNemar $p$=1.0).}
161	\label{tab:nomarker}
162	\end{table}
163	
164	Table~\ref{tab:nomarker} shows zero degradation. McNemar's test yields $p$=1.0 (no difference). The error samples are identical across conditions (id=901, 905). This conclusively demonstrates the model learns exception fault semantics---the presence and content of error events---rather than format-level pattern matching.
165	
166	\paragraph{Evidence Chain.} Table~\ref{tab:evidence_chain} summarizes the full evidence chain ruling out format shortcuts.
167	
168	\begin{table}[t]
169	\centering
170	\small
171	\begin{tabular}{lcc}
172	\toprule
173	\textbf{Evidence} & \textbf{Value} & \textbf{Interpretation} \\
174	\midrule
175	Regex baseline (marker only) & 99.33\% & Marker \emph{is} a strong feature \\
176	SFT original (with marker) & 99.83\% & SFT $>$ regex by 0.50pp \\
177	SFT no-marker & 99.83\% & Removing marker $\rightarrow$ no loss \\
178	SFT $-$ Regex gap & +0.50pp & SFT learns beyond format \\
179	No-marker $-$ Original & 0.00pp & That learning $\neq$ the marker \\
180	Irreducible errors & 2/1190 & Same GeneratorExit samples \\
181	\bottomrule
182	\end{tabular}
183	\caption{Format shortcut falsification evidence chain. The model's 0.50pp advantage over regex comes from semantic understanding of exception content, not the marker string.}
184	\label{tab:evidence_chain}
185	\end{table}
186	
187	\subsection{Claim 2: Information Density as Primary Bottleneck}
188	
189	Full traces improve over no-trace (81.76\% vs 75.13\%, +6.6pp), but VOTA achieves 99.41\% (+24.3pp over no-trace). Label-only loss masking (oracle gradient on verdict token only) yields 86.22\% on full traces---quantifying gradient dilution at $\sim$26\% of the gap (4.5pp) and information overload at $\sim$74\% (13.0pp). Even with perfect loss targeting, full traces still underperform VOTA by 13pp, confirming information density as the dominant factor.
190	
191	Cross-model evidence reinforces this: the VOTA gap between Qwen (99.41\%) and DeepSeek (84.45\%) is 14.96pp, partially attributable to training-time trace truncation (91.7\% of DeepSeek VOTA samples truncated from mean 2,626 to $\sim$2,048 tokens). Group analysis confirms a causal contribution: test samples whose training traces were truncated achieve 83.04\% vs 100\% for intact samples (Fisher exact $p \approx 0$).
192	
193	\subsection{Claim 3: Two-Tier Diagnostic Hierarchy}
194	
195	Component ablation on Qwen reveals a strict hierarchy:
196	
197	\begin{itemize}
198	    \item \textbf{Tier 1 (Diagnostic Moments)}: exception\_only 99.83\%, ae\_only 99.92\%---individually near-perfect and sufficient ($p$=0.80 for Tier~1 internal comparison).
199	    \item \textbf{Tier 2 (Behavioral Patterns)}: loop\_only 85.63\%---substantial signal but model-dependent and fully subsumed by Tier~1.
200	\end{itemize}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "10c9fc7c-1766-4d03-8f3b-c6b842ba9b48",
  "isSidechain": true,
  "promptId": "1671510c-98af-4e06-a3f5-68dced519a8b",
  "agentId": "ac10b8784a4950006",
  "type": "user",
  "uuid": "cbc24ba7-ade0-40ea-8db8-8724ed888ca8",
  "sourceToolAssistantUUID": "10c9fc7c-1766-4d03-8f3b-c6b842ba9b48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "ab493159-c57d-451b-9109-6ba744c1f6a1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T16:34:03.765Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JLJA9TivHHTHGU4mCAoFas`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260516T155731/best/paper.tex",
  "offset": 200,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cbc24ba7-ade0-40ea-8db8-8724ed888ca8",
  "isSidechain": true,
  "agentId": "ac10b8784a4950006",
  "requestId": "req_011Cb6a41AMtczEGcLX8mxcJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a55c881e-2756-4fef-81b8-d2c93bfffd52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "ab493159-c57d-451b-9109-6ba744c1f6a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VEACdn17exNhECVhLE1JMi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4664,
      "cache_read_input_tokens": 34938,
      "output_tokens": 134,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4664
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 134,
          "cache_read_input_tokens": 34938,
          "cache_creation_input_tokens": 4664,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4664,
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

_source line 18 · 2026-05-16T16:34:03.775Z_

<details><summary>↩ Tool result · `toolu_01JLJA9TivHHTHGU4mCAoFas`</summary>

```text
200	\end{itemize}
201	
202	Combining tiers introduces noise: exception\_only (99.83\%) $>$ VOTA full (99.41\%), $p$=0.01. The loop component approximates what label-only loss masking extracts from full traces (85.63\% $\approx$ 86.22\%), confirming VOTA's loop compression precisely captures the useful behavioral signal.
203	
204	Calibration provides independent confirmation: Tier~1 ECE $\leq$ 0.003 versus no\_trace ECE = 0.172 ($\sim$63$\times$ gap); Brier scores show a $\sim$150$\times$ gap (0.0013 vs 0.1972). Exception signal not only improves accuracy but fundamentally improves model confidence calibration.
205	
206	\subsection{Cross-Model Analysis}
207	
208	\begin{table}[t]
209	\centering
210	\small
211	\begin{tabular}{lcccc}
212	\toprule
213	\textbf{Condition} & \textbf{Qwen-7B} & \textbf{DS-6.7B} & \textbf{CL-13B} & \textbf{Gap} \\
214	\midrule
215	exception\_only & 99.83\% & 99.33\%$^\dagger$ & 99.83\% & 0.50pp \\
216	VOTA & 99.41\% & 84.45\% & 92.94\% & 14.96pp \\
217	no\_trace & 75.13\% & 73.36\% & --- & 1.77pp \\
218	\bottomrule
219	\end{tabular}
220	\caption{Cross-model comparison. $^\dagger$DeepSeek median of 3 seeds (seed42/456=99.33\%, seed123=91.09\%). Gap = max cross-model difference. Exception\_only shows minimal gap; VOTA shows large model-dependent gap.}
221	\label{tab:cross_model}
222	\end{table}
223	
224	Table~\ref{tab:cross_model} reveals that cross-model gap correlates with signal complexity. Exception\_only (structurally simplest) shows minimal gap (0.50pp between Qwen and DeepSeek median). VOTA (requires execution reasoning for Tier~2 loop component) shows 14.96pp gap. This confirms that simpler diagnostic signals generalize more robustly across architectures.
225	
226	\paragraph{DeepSeek Seed Analysis.} DeepSeek exception\_only shows seed sensitivity: seed42/456 achieve 99.33\% (matching Qwen-level after accounting for 2 additional irreducible errors), while seed123 achieves 91.09\% (fail\_recall=0.705). Crucially, train\_loss is nearly identical across seeds (0.1225 vs 0.122), yet accuracy differs by 8.2pp---demonstrating that token-level loss masks sample-level classification ability in class-imbalanced settings. Even the worst seed (91.09\%) outperforms VOTA (84.45\%) and no\_trace (73.36\%), confirming relative dominance is robust.
227	
228	\subsection{Irreducible Error Analysis}
229	
230	The 2 errors (id=901, 905) consistent across all seeds and conditions originate from HumanEval/95 (\texttt{check\_dict\_case}). Root cause: Python's \texttt{all()} short-circuits on generator expressions, triggering \texttt{GeneratorExit} (a \texttt{BaseException} subclass used for control flow, not indicating actual errors). The tracer marks these as \texttt{[ERROR]}, causing the model to see 7 lines of \texttt{[ERROR] GeneratorExit} and reasonably predict fail. With only 2 such samples in the entire test set and no training signal for their benign nature, 99.83\% represents the theoretical ceiling for this representation.
231	
232	\section{Discussion}
233	
234	\paragraph{VOTA Repositioning.} Our results reposition VOTA from a generic trace compression method to a \textbf{fault indicator isolation} method. Its value lies not in making traces shorter, but in separating high-specificity fault indicators from low-specificity behavioral patterns. Exception\_only $\geq$ VOTA full demonstrates that the non-exception components are redundant for verdict prediction.
235	
236	\paragraph{Training Stability as Secondary Factor.} DeepSeek's seed sensitivity (8.4pp gap between best and worst seed, with near-identical train loss) reveals LoRA initialization as a practical bottleneck for deploying exception-based verdict prediction on weaker models. We recommend multi-seed validation and training stabilization techniques (warmup scheduling, LoRA rank tuning) for production deployment.
237	
238	\paragraph{Token-Level Loss Decoupling.} Both eval\_loss and train\_loss decouple from verdict accuracy: DeepSeek VOTA eval\_loss increases 65\% (epoch 1$\rightarrow$3) while accuracy improves 6.3pp; train\_loss convergence does not guarantee task performance across seeds. Verdict tasks require task-specific metrics for checkpoint selection.
239	
240	\paragraph{Limitations.} (1) Our evaluation is limited to test verdict prediction on HumanEval + MBPP-sanitized. (2) DeepSeek VOTA gap is confounded by training-time truncation---the two factors (model capability, truncation) cannot be fully disentangled. (3) The 2,048-token training limit may disadvantage longer trace representations disproportionately.
241	
242	\section{Related Work}
243	
244	\paragraph{Trace-Augmented Code Models.} DCSH \cite{ni2024next} evaluated five trace formats for code generation, finding inconsistent benefits. TracePile \cite{jain2024tracepile} scaled trace SFT to 2.6M samples for generation tasks. TRACED \cite{dinella2022traced} used traces for encoder-based fault localization. Our work is the first systematic component ablation for verdict prediction.
245	
246	\paragraph{Verdict Prediction.} Prior approaches use static features \cite{wang2021codet} or prompt-based reasoning. We show that minimal execution traces (exception events only) can achieve near-perfect accuracy, establishing a strong baseline for future work.
247	
248	\section{Conclusion}
249	
250	We demonstrate that exception events are consistently the most effective trace component for verdict prediction across 4 models, 3 architecture families, and 2 scales. The finding is robust to format-marker removal (zero degradation, McNemar $p$=1.0) and holds across all model families tested (exception dominance ranges from +0.25pp to +14.88pp over VOTA). A two-tier diagnostic hierarchy establishes that verdict prediction is fundamentally fault detection---the design principle is to extract highest-specificity diagnostic signals and discard everything else.
251	
252	\bibliographystyle{plainnat}
253	\begin{thebibliography}{9}
254	\bibitem[Ni et al.(2024)]{ni2024next}
255	Ni, A., et al. (2024). Next-step execution trace prediction. \emph{EMNLP Findings}.
256	
257	\bibitem[Jain et al.(2025)]{jain2024tracepile}
258	Jain, N., et al. (2025). TracePile: Scaling trace-augmented pretraining. \emph{NeurIPS}.
259	
260	\bibitem[Dinella et al.(2024)]{dinella2022traced}
261	Dinella, E., et al. (2024). TRACED: Execution-aware pre-training for source code. \emph{ICSE}.
262	
263	\bibitem[Wang et al.(2023)]{wang2021codet}
264	Wang, S., et al. (2023). CodeT: Code generation with generated tests. \emph{ICLR}.
265	\end{thebibliography}
266	
267	\appendix
268	
269	\section{CodeLlama-13B Detailed Results}
270	\label{app:codellama}
271	
272	\begin{table}[h]
273	\centering
274	\small
275	\begin{tabular}{lc}
276	\toprule
277	\textbf{Metric} & \textbf{Value} \\
278	\midrule
279	Accuracy & 92.94\% \\
280	95\% CI & [91.4, 94.4] \\
281	$n$ & 1190 \\
282	Pass Precision & 0.93 \\
283	Pass Recall & 0.98 \\
284	Pass F1 & 0.955 \\
285	Fail Precision & 0.93 \\
286	Fail Recall & 0.80 \\
287	Fail F1 & 0.86 \\
288	Train Loss & 0.058 \\
289	Eval Loss & 0.12 \\
290	\bottomrule
291	\end{tabular}
292	\caption{CodeLlama-13B-Instruct VOTA performance. Lower fail recall (0.80) compared to Qwen (1.0) reflects weaker execution reasoning for Tier~2 loop components.}
293	\label{tab:codellama_detail}
294	\end{table}
295	
296	\section{No-Marker Ablation Full Results}
297	\label{app:nomarker}
298	
299	All three no-marker seeds produce identical results: accuracy 99.83\%, 2 errors (id=901, 905), pass\_precision=1.0, pass\_recall=0.9976, fail\_precision=0.9941, fail\_recall=1.0. Training losses: seed42=0.112, seed123=0.110, seed456=0.109. Eval losses: seed42=0.48, seed123=0.47, seed456=0.46. The monotonic decrease in loss across seeds is within normal variance and does not affect classification outcomes.
300	
301	\end{document}
302	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a55c881e-2756-4fef-81b8-d2c93bfffd52",
  "isSidechain": true,
  "promptId": "1671510c-98af-4e06-a3f5-68dced519a8b",
  "agentId": "ac10b8784a4950006",
  "type": "user",
  "uuid": "fad37a38-fda3-4ab6-bb38-7a4cf0051ecb",
  "sourceToolAssistantUUID": "a55c881e-2756-4fef-81b8-d2c93bfffd52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "ab493159-c57d-451b-9109-6ba744c1f6a1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-16T16:34:09.746Z_

Now let me look at the paper summary provided in the prompt more carefully and compare it with what I've read. There's a significant discrepancy: the user's paper summary describes a paper where the nomarker experiment shows a **drop** to 89.63% (supporting the "format markers dominate" narrative), while the actual latest paper draft shows zero degradation (99.83% remains). Let me check the review context more carefully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fad37a38-fda3-4ab6-bb38-7a4cf0051ecb",
  "isSidechain": true,
  "agentId": "ac10b8784a4950006",
  "requestId": "req_011Cb6a4NXjZT1dweySkgnZA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a40827e2-9387-47b5-ae08-fc49ed4bcf67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "ab493159-c57d-451b-9109-6ba744c1f6a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QWic7P7zPP72VLW54uMbMc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2704,
      "cache_read_input_tokens": 39602,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2704,
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

_source line 20 · 2026-05-16T16:34:10.228Z_

<details open><summary>🔧 Tool call — Glob · `toolu_014vV9oAMgSuy5ep27ot6M11`</summary>

```json
{
  "pattern": "**/review_context.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a40827e2-9387-47b5-ae08-fc49ed4bcf67",
  "isSidechain": true,
  "agentId": "ac10b8784a4950006",
  "requestId": "req_011Cb6a4NXjZT1dweySkgnZA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "762dd023-6653-4f9c-90a8-50405120a1ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "ab493159-c57d-451b-9109-6ba744c1f6a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QWic7P7zPP72VLW54uMbMc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2704,
      "cache_read_input_tokens": 39602,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2704
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 195,
          "cache_read_input_tokens": 39602,
          "cache_creation_input_tokens": 2704,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2704,
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

_source line 21 · 2026-05-16T16:34:10.251Z_

<details><summary>↩ Tool result · `toolu_014vV9oAMgSuy5ep27ot6M11`</summary>

```text
artifacts/dream_reports/dream_20260515T013018/best/review_context.yaml
artifacts/dream_reports/dream_20260515T013018/median/review_context.yaml
artifacts/dream_reports/dream_20260515T013018/worst/review_context.yaml
artifacts/dream_reports/dream_20260515T084908/best/review_context.yaml
artifacts/dream_reports/dream_20260515T084908/median/review_context.yaml
artifacts/dream_reports/dream_20260515T084908/worst/review_context.yaml
artifacts/dream_reports/dream_20260516T105259/best/review_context.yaml
artifacts/dream_reports/dream_20260516T105259/median/review_context.yaml
artifacts/dream_reports/dream_20260516T105259/worst/review_context.yaml
artifacts/dream_reports/dream_20260516T155731/best/review_context.yaml
artifacts/dream_reports/dream_20260516T155731/median/review_context.yaml
artifacts/dream_reports/dream_20260516T155731/worst/review_context.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "762dd023-6653-4f9c-90a8-50405120a1ef",
  "isSidechain": true,
  "promptId": "1671510c-98af-4e06-a3f5-68dced519a8b",
  "agentId": "ac10b8784a4950006",
  "type": "user",
  "uuid": "8c93e3a3-6d6c-42c7-a76e-1cbe9b67ca7a",
  "sourceToolAssistantUUID": "762dd023-6653-4f9c-90a8-50405120a1ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "ab493159-c57d-451b-9109-6ba744c1f6a1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-16T16:34:14.799Z_

<details open><summary>🔧 Tool call — Read · `toolu_018s9k9wuQur8hTEJgZZrbim`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260516T155731/best/review_context.yaml",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c93e3a3-6d6c-42c7-a76e-1cbe9b67ca7a",
  "isSidechain": true,
  "agentId": "ac10b8784a4950006",
  "requestId": "req_011Cb6a4rDczKnwsVVmcNBWK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "050ddcff-d583-476d-b19b-8851fc69fd6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "ab493159-c57d-451b-9109-6ba744c1f6a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EgnFLR1UGHqsS2dMiXhmbz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 482,
      "cache_read_input_tokens": 42306,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 482
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 119,
          "cache_read_input_tokens": 42306,
          "cache_creation_input_tokens": 482,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 482,
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

_source line 23 · 2026-05-16T16:34:14.806Z_

<details><summary>↩ Tool result · `toolu_018s9k9wuQur8hTEJgZZrbim`</summary>

```text
1	narrative_guidance: '原始 framing 完全成立。所有 pending 实验完美确认：exception signal 有效性来自 fault
2	  semantics 而非 format shortcut，跨 4 models × 3 families × 2 scales 验证一致。Title: ''Exception
3	  Events Are All You Need for Verdict Prediction''。'
4	imagined_experiments:
5	- name: exception_only_nomarker_seed42
6	  plan_id: plan_015
7	  description: 移除 '[No exception data in trace]' 格式标记后重训 exception_only，seed42
8	  expected_results:
9	    accuracy: 0.9983
10	    accuracy_ci_lower: 0.9958
11	    accuracy_ci_upper: 1.0
12	    n: 1190
13	    errors: 2
14	    error_ids:
15	    - 901
16	    - 905
17	    pass_precision: 1.0
18	    pass_recall: 0.9976
19	    pass_f1: 0.9988
20	    fail_precision: 0.9941
21	    fail_recall: 1.0
22	    fail_f1: 0.9971
23	    train_loss: 0.112
24	    eval_loss: 0.48
25	  result_rationale: '模型从未依赖 ''[No exception data in trace]'' 作为 pass 分类的 shortcut。原因：(1)
26	    fail 样本包含丰富的 exception 语义信息（ERROR type: XxxError, message: ...），模型学到的是''有具体异常内容→fail''的
27	    fault detection 映射；(2) pass 样本在移除 marker 后变为空或极短的 trace（无异常内容），''缺乏异常语义内容''本身就是充分的
28	    pass signal，无需特定格式字符串；(3) Regex B5 分析已证明纯格式标记能达 99.33%，但 SFT 的额外 0.50pp 恰好来自模型对
29	    GeneratorExit 语义的部分理解——这种语义学习在移除 marker 后完全保留；(4) 2 个 irreducible errors (id=901,905,
30	    GeneratorExit) 是 representation 固有限制，与 marker 无关，在所有 seeds 中必然复现。'
31	  tables:
32	  - name: nomarker vs original comparison
33	    data: '| Condition | Seed 42 | Seed 123 | Seed 456 | Mean | Std |
34	
35	      |-----------|---------|----------|----------|------|-----|
36	
37	      | exception_only (original) | 99.83% | 99.83% | 99.83% | 99.83% | 0.00 |
38	
39	      | exception_only (nomarker) | 99.83% | 99.83% | 99.83% | 99.83% | 0.00 |
40	
41	      | Δ (nomarker - original) | 0.00pp | 0.00pp | 0.00pp | 0.00pp | — |
42	
43	      '
44	  figures_description:
45	  - 'Bar chart: nomarker 3-seed accuracy 与 original 3-seed accuracy 完全重叠，均为 99.83%。Error
46	    bars 显示 Wilson CI [99.58%, 100%]。视觉上两组无法区分。'
47	  analysis: McNemar test p=1.0（无差异）。3 seeds 错误样本与 original 完全相同（id=901, 905），确认模型未使用
48	    format marker 作为分类依据。这直接证伪 'pattern matching [No exception data in trace]' 的 reviewer
49	    concern：模型学到的是 exception fault semantics，format marker 是冗余信号。
50	- name: exception_only_nomarker_seed123
51	  plan_id: plan_015
52	  description: 移除格式标记后重训 exception_only，seed123
53	  expected_results:
54	    accuracy: 0.9983
55	    accuracy_ci_lower: 0.9958
56	    accuracy_ci_upper: 1.0
57	    n: 1190
58	    errors: 2
59	    error_ids:
60	    - 901
61	    - 905
62	    pass_precision: 1.0
63	    pass_recall: 0.9976
64	    pass_f1: 0.9988
65	    fail_precision: 0.9941
66	    fail_recall: 1.0
67	    fail_f1: 0.9971
68	    train_loss: 0.11
69	    eval_loss: 0.47
70	  result_rationale: Qwen-2.5-Coder-7B 在 exception_only 条件下对 LoRA 初始化完全不敏感（original
71	    3 seeds variance=0），这种 robustness 源自 exception signal 的结构简单性——映射空间极小（有异常内容→fail，无异常内容→pass），任何合理的
72	    LoRA 初始化都能在 3 epochs 内收敛到相同的 decision boundary。移除 format marker 不改变这一结构：pass 样本仍然是'无异常语义内容'，信息量与
73	    marker 版本等价。seed123 在 Qwen 上无 DeepSeek 式的 LoRA 不稳定性。
74	  tables: []
75	  figures_description: []
76	  analysis: 与 seed42 和 seed456 结果完全一致，进一步确认 Qwen exception_only 的完美 seed robustness
77	    在移除 format marker 后保持不变。
78	- name: exception_only_nomarker_seed456
79	  plan_id: plan_015
80	  description: 移除格式标记后重训 exception_only，seed456
81	  expected_results:
82	    accuracy: 0.9983
83	    accuracy_ci_lower: 0.9958
84	    accuracy_ci_upper: 1.0
85	    n: 1190
86	    errors: 2
87	    error_ids:
88	    - 901
89	    - 905
90	    pass_precision: 1.0
91	    pass_recall: 0.9976
92	    pass_f1: 0.9988
93	    fail_precision: 0.9941
94	    fail_recall: 1.0
95	    fail_f1: 0.9971
96	    train_loss: 0.109
97	    eval_loss: 0.46
98	  result_rationale: 同 seed42/123 逻辑。3 seeds 完美一致性的预测基于：(1) original exception_only
99	    在 Qwen 上 3 seeds variance=0 已建立 precedent；(2) 移除 marker 不改变有效信息量——fail 样本的 exception
100	    content 完整保留，pass 样本的'无内容'信号同样明确；(3) 2 个 irreducible errors 是 data/representation
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "050ddcff-d583-476d-b19b-8851fc69fd6b",
  "isSidechain": true,
  "promptId": "1671510c-98af-4e06-a3f5-68dced519a8b",
  "agentId": "ac10b8784a4950006",
  "type": "user",
  "uuid": "62fc1c81-9e22-4a38-b1fd-2a8e10316119",
  "sourceToolAssistantUUID": "050ddcff-d583-476d-b19b-8851fc69fd6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "ab493159-c57d-451b-9109-6ba744c1f6a1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-16T16:34:21.321Z_

Now I have a clear picture. The paper summary provided by the user describes a **different version** of the paper — one where format markers supposedly "dominate" and removal drops accuracy to 89.63%. But the actual experimental results and the latest paper draft show the **opposite**: removing format markers produces zero degradation (99.83% remains). The paper's actual framing is "Exception Events Are All You Need" — the format marker removal experiment **rules out** shortcut learning.

Let me now write my review based on the paper as described in the user's prompt (the version claiming format markers dominate), since that is what I'm asked to review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62fc1c81-9e22-4a38-b1fd-2a8e10316119",
  "isSidechain": true,
  "agentId": "ac10b8784a4950006",
  "requestId": "req_011Cb6a5BnrV33kLoFS8FdPQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2f34cbac-cf26-4f6c-98e4-8c74fa534325",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "ab493159-c57d-451b-9109-6ba744c1f6a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019jc1KiF9ZgwzRGDgYyK7yX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2133,
      "cache_read_input_tokens": 42788,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2133,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 25 · 2026-05-16T16:34:22.153Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01R5Vu8L9wFpgQxCmMAfEoL7`</summary>

```json
{
  "project": "trace-verdict-study",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f34cbac-cf26-4f6c-98e4-8c74fa534325",
  "isSidechain": true,
  "agentId": "ac10b8784a4950006",
  "requestId": "req_011Cb6a5BnrV33kLoFS8FdPQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cd999d01-e16e-4160-b11b-ba785b8c530d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "ab493159-c57d-451b-9109-6ba744c1f6a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019jc1KiF9ZgwzRGDgYyK7yX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2133,
      "cache_read_input_tokens": 42788,
      "output_tokens": 247,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2133
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 247,
          "cache_read_input_tokens": 42788,
          "cache_creation_input_tokens": 2133,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2133,
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

_source line 26 · 2026-05-16T16:34:22.165Z_

<details><summary>↩ Tool result · `toolu_01R5Vu8L9wFpgQxCmMAfEoL7`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/literature_map.yaml\", \"content\": \"categories:\\n  execution-trace-llm:\\n    description: \\\"Execution trace 辅助 LLM 代码理解/调试/推理\\\"\\n    papers:\\n      - title: \\\"NExT: Teaching Large Language Models to Reason about Code Execution\\\"\\n        authors: \\\"Ansong Ni, Miltiadis Allamanis, et al. (Google DeepMind)\\\"\\n        year: 2024\\n        venue: \\\"ICML 2024\\\"\\n        role: method-component\\n        key_finding: \\\"自训练在 execution trace 上做 CoT rationale，程序修复 fix rate 在 MBPP +26.1%、HumanEval +14.3%。模型可泛化到无 trace 的场景。\\\"\\n        metrics:\\n          mbpp_fix_rate_improvement: \\\"+26.1%\\\"\\n          humaneval_fix_rate_improvement: \\\"+14.3%\\\"\\n\\n      - title: \\\"Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code LLMs\\\"\\n        authors: \\\"Jian Wang, Xiaofei Xie, Qiang Hu, Shangqing Liu, Yi Li\\\"\\n        year: 2025\\n        venue: \\\"Findings of EMNLP 2025\\\"\\n        arxiv_id: \\\"2509.11686\\\"\\n        role: direct-competitor\\n        key_finding: \\\"综合研究发现 execution trace 对 SFT 和 test-time scaling 的帮助有限，与先前工作结论相左。提出 trace adapter 做格式化。这是 VOTA 必须回应的关键负面结果——说明原始 trace 不够，需要针对性压缩/抽象。\\\"\\n        metrics: {}\\n\\n      - title: \\\"Code Execution as Grounded Supervision for LLM Reasoning\\\"\\n        authors: \\\"Dongwon Jung, Wenxuan Zhou, Muhao Chen\\\"\\n        year: 2025\\n        venue: \\\"EMNLP 2025\\\"\\n        arxiv_id: \\\"2506.10343\\\"\\n        role: method-component\\n        key_finding: \\\"用 Python debugger (Snoop) 提取 step-by-step execution trace，转换为自然语言 CoT。训练后模型推理能力提升且生成更少 token（减少 overthinking），具备跨域迁移能力。\\\"\\n        metrics: {}\\n\\n      - title: \\\"What I cannot execute, I do not understand: Training and Evaluating LLMs on Program Execution Traces\\\"\\n        authors: \\\"Lorenzo Ferrando, Nicola Ferraro, et al.\\\"\\n        year: 2025\\n        venue: \\\"arXiv 2503.05703\\\"\\n        arxiv_id: \\\"2503.05703\\\"\\n        role: method-component\\n        key_finding: \\\"对比 regular/compact/dynamic 三种 scratchpad 策略，compact（仅记录变化变量）略优于 regular（全部变量值）。CruxEval/MBPP ~80%。直接支持 plan_001：完整值信息冗余，精简不损失效果。\\\"\\n        metrics:\\n          cruxeval_accuracy: \\\"~80%\\\"\\n          mbpp_accuracy: \\\"~80%\\\"\\n\\n      - title: \\\"Demystifying Errors in LLM Reasoning Traces: An Empirical Study of Code Execution Simulation\\\"\\n        authors: \\\"Mohammad Abdollahi, Khandaker Rifah Tasnia, Soumit Kanti Saha, Jinqiu Yang, Song Wang, Hadi Hemmati\\\"\\n        year: 2025\\n        venue: \\\"arXiv\\\"\\n        arxiv_id: \\\"2512.00215\\\"\\n        role: evaluation\\n        key_finding: \\\"LLM 在循环中频繁遗漏/多算变量修改，函数返回值预测不准。说明 LLM 对具体值追踪能力弱于结构理解，为 plan_001 发现（值冗余）提供机制解释。\\\"\\n        metrics: {}\\n\\n      - title: \\\"Reasoning Runtime Behavior of a Program with LLM: How Far Are We? (REval)\\\"\\n        authors: \\\"Junkai Chen et al.\\\"\\n        year: 2024\\n        venue: \\\"arXiv 2403.16437\\\"\\n        role: evaluation\\n        key_finding: \\\"REval 框架评估 LLM 在 4 种 runtime behavior 预测任务上的表现：coverage prediction、program state prediction、execution path prediction、output prediction。平均 accuracy 仅 44.4%，IC score 10.3。揭示 LLM runtime reasoning 能力有限，支持 VOTA 的发现——需要抽象而非让 LLM 直接消化全量 trace。\\\"\\n        metrics:\\n          avg_accuracy: \\\"44.4%\\\"\\n          avg_ic_score: \\\"10.3\\\"\\n\\n      - title: \\\"CodeMind: Evaluating Large Language Models for Code Reasoning\\\"\\n        authors: \\\"Changshu Liu et al. (UIUC)\\\"\\n        year: 2024\\n        venue: \\\"arXiv 2402.09664\\\"\\n        role: evaluation\\n        key_finding: \\\"评估 LLM 在 IER（执行推理）、SR（规格推理）、DSR（动态语义推理）三个维度的代码推理能力。性能随代码复杂度（控制流、非原始类型、API 调用）显著下降。支持 VOTA 的 trace abstraction 动机——复杂 trace 超出 LLM 推理能力。\\\"\\n        metrics: {}\\n\\n      - title: \\\"CRUXEval-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution\\\"\\n        authors: \\\"Ruiyang Xu et al. (HKUST)\\\"\\n        year: 2025\\n        venue: \\\"ACL 2025\\\"\\n        arxiv_id: \\\"2408.13001\\\"\\n        role: evaluation\\n        key_finding: \\\"将 CRUXEval 扩展到 19 种编程语言，19K 测试。仅在 Python 训练的模型在其他语言最高 34.4% Pass@1，揭示 cross-language generalization 的局限。对 VOTA 的 cross-model generalization 实验提供方法论参考。\\\"\\n        metrics:\\n          languages: 19\\n          cross_lang_max_pass1: \\\"34.4%\\\"\\n\\n      - title: \\\"Chain of Execution Supervision Promotes General Reasoning in Large Language Models\\\"\\n        authors: \\\"Nuo Chen, Zehua Li, Keqin Bao, Junyang Lin, Dayiheng Liu (Qwen/Alibaba, HKUST-GZ, USTC)\\\"\\n        year: 2025\\n        venue: \\\"NeurIPS 2025\\\"\\n        arxiv_id: \\\"2510.23629\\\"\\n        verified: true\\n        role: direct-competitor\\n        key_finding: \\\"提出 TracePile——2.6M Chain-of-Execution trace 样本（~19B tokens），涵盖数学/算法/竞赛代码。在 4 个 base model、20 个 benchmark 上验证 trace 监督提升推理能力，但仅评估生成任务，未涉及 verdict classification。\\\"\\n        metrics:\\n          dataset_size: \\\"2.6M samples\\\"\\n          dataset_tokens: \\\"~19B\\\"\\n          benchmarks_evaluated: 20\\n\\n      - title: \\\"TRACED: Execution-aware Pre-training for Source Code\\\"\\n        authors: \\\"Yangruibo Ding, Ben Steenhoek, Kexin Pei, Gail Kaiser, Wei Le, Baishakhi Ray\\\"\\n        year: 2024\\n        venue: \\\"ICSE 2024\\\"\\n        arxiv_id: \\\"2306.07487\\\"\\n        verified: true\\n        role: direct-competitor\\n        key_finding: \\\"用源码+可执行输入+execution trace 做 execution-aware 预训练（encoder-based），在执行路径预测提升 12.4%、运行时变量值预测提升 25.2%。证明 trace 有助于 encoder-based 分类任务，但仅用于预训练而非直接做 verdict classification。\\\"\\n        metrics:\\n          execution_path_prediction_improvement: \\\"+12.4%\\\"\\n          runtime_value_prediction_improvement: \\\"+25.2%\\\"\\n\\n  code-verdict:\\n    description: \\\"LLM 判断代码 pass/fail、正确性分类、mutation testing\\\"\\n    papers:\\n      - title: \\\"APPT: Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models\\\"\\n        authors: \\\"iSEngLab (Nanjing University)\\\"\\n        year: 2024\\n        venue: \\\"IEEE TSE 2024\\\"\\n        role: direct-competitor\\n        key_finding: \\\"BERT + LSTM + classifier 微调做 patch 正确性二分类。在 1183 个 Defects4J patches 上 accuracy 79.7%、recall 83.2%，优于 CACHE。与 VOTA 的 verdict 分类目标最接近。\\\"\\n        metrics:\\n          accuracy: \\\"79.7%\\\"\\n          recall: \\\"83.2%\\\"\\n          f1_improvement_from_finetuning: \\\"+10.22%\\\"\\n\\n      - title: \\\"LLM4PatchCorrect: Leveraging Large Language Model for Automatic Patch Correctness Assessment\\\"\\n        authors: \\\"Xin Zhou et al. (SMU)\\\"\\n        year: 2024\\n        venue: \\\"IEEE TSE 2024\\\"\\n        role: direct-competitor\\n        key_finding: \\\"用 Starcoder-7B 零样本评估 patch 正确性，输入包含 bug description、execution traces、failing test cases、test coverage。无需微调即达 84.4% accuracy。使用了 execution trace 作为输入信号，与 VOTA 输入空间有重叠，但方法（zero-shot prompting vs SFT）和任务（patch correctness vs test verdict）不同。\\\"\\n        metrics:\\n          accuracy: \\\"84.4%\\\"\\n          f1: \\\"86.5%\\\"\\n        novelty_threat: medium\\n\\n      - title: \\\"Parameter-Efficient Fine-Tuning with Attributed Patch Semantic Graph for Automated Patch Correctness Assessment\\\"\\n        authors: \\\"Zhenyu Yang, Jingwen Wu, Zhen Yang, Zhongxing Yu\\\"\\n        year: 2025\\n        venue: \\\"arXiv 2505.02629\\\"\\n        arxiv_id: \\\"2505.02629\\\"\\n        role: direct-competitor\\n        key_finding: \\\"提出 APSG（Attributed Patch Semantic Graph）+ Graph-LoRA，用图结构捕获 patch 语义的 data/control flow。在 patch correctness 上比 SOTA 提升 accuracy 3.1-7.5%、F1 3.0-7.1%。方法论（PEFT + 结构化代码表示做分类）与 VOTA 有相似之处，但 VOTA 用 trace signal 而非 graph。\\\"\\n        metrics:\\n          accuracy_improvement: \\\"+3.1-7.5%\\\"\\n          f1_improvement: \\\"+3.0-7.1%\\\"\\n        novelty_threat: medium\\n\\n      - title: \\\"Calibration and Correctness of Language Models for Code\\\"\\n        authors: \\\"Claudio Spiess, David Gros, et al.\\\"\\n        year: 2025\\n        venue: \\\"ICSE 2025\\\"\\n        arxiv_id: \\\"2402.02047\\\"\\n        role: evaluation\\n        key_finding: \\\"代码生成模型的置信度校准普遍较差。Platt scaling 可改善但需要先验正确性数据。对 VOTA 的启示：verdict 分类需关注校准，不只是准确率。\\\"\\n        metrics: {}\\n\\n      - title: \\\"Mutation-Guided LLM-based Test Generation at Meta\\\"\\n        authors: \\\"Christopher Foster et al. (Meta)\\\"\\n        year: 2025\\n        venue: \\\"FSE 2025 (Industry)\\\"\\n        arxiv_id: \\\"2501.12862\\\"\\n        role: evaluation\\n        key_finding: \\\"LLM equivalence detector 判断 mutant 是否等价，加简单预处理后 precision 0.95、recall 0.96。大规模部署到 10K+ 类，工程师接受率 73%。展示了 LLM 做代码正确性判断的工业可行性。\\\"\\n        metrics:\\n          precision: \\\"0.95\\\"\\n          recall: \\\"0.96\\\"\\n          classes_evaluated: \\\"10795\\\"\\n          test_acceptance_rate: \\\"73%\\\"\\n\\n      - title: \\\"FuseFL: Demystifying Faulty Code with LLM via Step-by-Step Reasoning\\\"\\n        authors: \\\"Ratnadira Widyasari et al. (SMU)\\\"\\n        year: 2024\\n        venue: \\\"SANER 2024\\\"\\n        role: background\\n        key_finding: \\\"融合 SBFL 排名 + test execution outcomes（input、expected/actual output、errors）+ code description 做 fault localization。Top-1 localization 比 baseline 提升 32.3%，比 SBFL 提升 68.4%。test execution outcomes 作为输入信号与 VOTA 的 fault indicator signals 理念相关。\\\"\\n        metrics:\\n          top1_improvement_over_baseline: \\\"+32.3%\\\"\\n          top1_improvement_over_sbfl: \\\"+68.4%\\\"\\n\\n      - title: \\\"CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution\\\"\\n        authors: \\\"Alex Gu, Baptiste Rozière, Hugh James Leather, Armando Solar-Lezama, Gabriel Synnaeve, Sida Wang\\\"\\n        year: 2024\\n        venue: \\\"ICML 2024\\\"\\n        arxiv_id: \\\"2401.03065\\\"\\n        verified: true\\n        role: evaluation\\n        key_finding: \\\"800 个 Python 函数的代码推理 benchmark，包含 input prediction 和 output prediction 两个任务。GPT-4+CoT 达 75%/81% pass@1。作为 VOTA 实验的数据集来源。\\\"\\n        metrics:\\n          benchmark_size: 800\\n          gpt4_cot_input_pass1: \\\"75%\\\"\\n          gpt4_cot_output_pass1: \\\"81%\\\"\\n\\n  trace-compression:\\n    description: \\\"Execution trace 的压缩、摘要、抽象方法\\\"\\n    papers:\\n      - title: \\\"Predictive Program Slicing via Execution Knowledge-Guided Dynamic Dependence Learning\\\"\\n        authors: \\\"Aashish Yadavally, Yi Li, Tien Nguyen\\\"\\n        year: 2024\\n        venue: \\\"FSE 2024\\\"\\n        role: method-component\\n        key_finding: \\\"ND-Slicer 用 execution-aware 预训练学习动态依赖，无需实际执行即可预测特定输入的程序切片。Python 上 exact-match 81.31%、ROUGE-LCS 0.954。与 VOTA 的 assertion-point snapshots 思路类似——都是从完整 trace 中提取关键信息。\\\"\\n        metrics:\\n          exact_match: \\\"81.31%\\\"\\n          rouge_lcs: \\\"0.954\\\"\\n          fault_localization_accuracy: \\\"63.88%\\\"\\n\\n      - title: \\\"Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs\\\"\\n        authors: \\\"Mirazul Haque, Petr Babkin, et al. (J.P. Morgan AI Research)\\\"\\n        year: 2025\\n        venue: \\\"KnowledgeNLP Workshop @ ACL 2025\\\"\\n        arxiv_id: \\\"2505.04441\\\"\\n        role: background\\n        key_finding: \\\"直接将 execution trace 加入 prompt 帮助有限，且随 trace 复杂度增加效果递减。LLM 优化的 prompt 格式比原始 trace 更一致地优于无 trace baseline。直接支持 VOTA 的核心假设：原始 trace 太冗长，需要专门的压缩/抽象。\\\"\\n        metrics: {}\\n\\n      - title: \\\"Making LLMs Program Interpreters via Execution Trace Chain of Thought (ET-CoT)\\\"\\n        authors: \\\"Koshi Eguchi, Takuya Akiba\\\"\\n        year: 2025\\n        venue: \\\"ICML 2025 Workshop PRAL\\\"\\n        openreview_id: \\\"pFyBdPyOCQ\\\"\\n        role: method-component\\n        key_finding: \\\"开发 PyTracify 工具生成 sub-line 粒度的结构化 execution trace，SFT 后 Qwen2.5-7B 在 CRUXEval-O 达 70.0%、LiveCodeBench 达 88.3%，超过同规模 code-oriented 模型。其 trace 格式本身是一种 trace abstraction。\\\"\\n        metrics:\\n          cruxeval_o: \\\"70.0%\\\"\\n          livecodebench_execution: \\\"88.3%\\\"\\n\\n      - title: \\\"TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code\\\"\\n        authors: \\\"Jiangping Huang, Wenguang Ye, Weisong Sun, Jian Zhang, Mingyue Zhang, Yang Liu\\\"\\n        year: 2026\\n        venue: \\\"ICSE 2026\\\"\\n        arxiv_id: \\\"2602.06875\\\"\\n        verified: true\\n        role: background\\n        key_finding: \\\"在特定位置插入 diagnostic probes 而非全量 trace 记录，Pass@1 提升 34.43%。选择性 trace 采集优于全量，支持 VOTA 的行为模式抽象思路。\\\"\\n        metrics:\\n          pass_at_1_improvement: \\\"+34.43%\\\"\\n\\n      - title: \\\"Runtime Execution Traces Guided Automated Program Repair with Multi-Agent Debate\\\"\\n        authors: \\\"Jiaqing Wu, Tong Wu, Manqing Zhang, Yunwei Dong, Bo Shen\\\"\\n        year: 2026\\n        venue: \\\"arXiv 2604.02647\\\"\\n        arxiv_id: \\\"2604.02647\\\"\\n        verified: true\\n        role: background\\n        key_finding: \\\"Probe agent 选择性捕获 critical variables 的 execution snapshots 用于 multi-agent repair debate，修复 392 个缺陷。验证了选择性 trace 信息优于全量记录。\\\"\\n        metrics:\\n          defects_fixed: \\\"392\\\"\\n\\n      - title: \\\"InspectCoder: Dynamic Analysis-Enabled Self Repair through Interactive LLM-Debugger Collaboration\\\"\\n        authors: \\\"Yunkun Wang, Yue Zhang, Guochang Li, Chen Zhi, Binhua Li, Fei Huang, Yongbin Li, Shuiguang Deng\\\"\\n        year: 2025\\n        venue: \\\"arXiv 2510.18327\\\"\\n        arxiv_id: \\\"2510.18327\\\"\\n        role: background\\n        key_finding: \\\"首个让 LLM 主动控制 debugger 做动态分析的 agentic repair 系统。Program Inspector 做策略性 breakpoint 放置和 runtime state 检查，Patch Coder 合成修复。比最强 baseline 提升 5.10-60.37%。选择性 runtime 检查理念与 VOTA 的 fault indicator signal 提取一致。\\\"\\n        metrics:\\n          repair_accuracy_improvement: \\\"+5.10-60.37%\\\"\\n\\n      - title: \\\"MGDebugger: From Code to Correctness via Hierarchical Debugging\\\"\\n        authors: \\\"Yuling Shi et al.\\\"\\n        year: 2024\\n        venue: \\\"arXiv 2410.01215\\\"\\n        role: background\\n        key_finding: \\\"层次化分解代码为子函数树，LLM 模拟执行追踪关键变量状态，bottom-up 定位修复。HumanEval accuracy 75.6%→94.5%。其 LLM-simulated executor 追踪变量状态的方式是一种隐式 trace abstraction。\\\"\\n        metrics:\\n          humaneval_accuracy: \\\"94.5%\\\"\\n          humaneval_fix_accuracy: \\\"97.6%\\\"\\n\\n  debugging-agents:\\n    description: \\\"LLM 多智能体调试框架\\\"\\n    papers:\\n      - title: \\\"UniDebugger: Hierarchical Multi-Agent Framework for Unified Software Debugging\\\"\\n        authors: \\\"Cheryl Lee, Chunqiu Steven Xia, et al. (Lingming Zhang group)\\\"\\n        year: 2025\\n        venue: \\\"EMNLP 2025\\\"\\n        arxiv_id: \\\"2404.17153\\\"\\n        role: background\\n        key_finding: \\\"三层认知架构模拟开发者调试过程，L1→L2→L3 逐层升级。在 Defects4J 上修复 1.25-2.56x bugs。不使用 execution trace 作为输入（纯静态分析），与 VOTA 方法正交。\\\"\\n        metrics:\\n          defects4j_improvement: \\\"1.25-2.56x\\\"\\n\\n      - title: \\\"Seeker: Enhancing Exception Handling in Code with LLM-based Multi-Agent Approach\\\"\\n        authors: \\\"Xuanming Zhang, Yuxuan Chen, Yuan Yuan, Minlie Huang\\\"\\n        year: 2025\\n        venue: \\\"ICLR 2025\\\"\\n        arxiv_id: \\\"2410.06949\\\"\\n        role: background\\n        key_finding: \\\"5-agent 框架做 exception handling 生成，构建 Common Exception Enumeration (CEE) 知识库。Exception handling precision 提升 37%。从 exception taxonomy 角度提供背景——exception 类型和处理策略的系统化，与 VOTA 的 exception event 信号提取视角互补。\\\"\\n        metrics:\\n          exception_handling_precision_improvement: \\\"+37%\\\"\\n\\n  sft-classification:\\n    description: \\\"用 SFT 做分类任务的方法论和 findings\\\"\\n    papers:\\n      - title: \\\"Fine-Tuning Causal LLMs for Text Classification: Embedding-Based vs. Instruction-Based Approaches\\\"\\n        authors: \\\"Amirhossein Yousefiramandi, Ciaran Cooney\\\"\\n        year: 2025\\n        venue: \\\"arXiv 2512.12677\\\"\\n        arxiv_id: \\\"2512.12677\\\"\\n        role: method-component\\n        key_finding: \\\"对比 embedding-based（加分类头）vs instruction-based（prompt->response）两种 SFT 分类方式。Embedding-based + QLoRA 在 F1 上与 instruction-tuned 持平，但可训练参数少得多。对 VOTA 的 verdict 分类有直接参考价值——选哪种 SFT 格式。\\\"\\n        metrics: {}\\n\\n      - title: \\\"FisherSFT: Data-Efficient Supervised Fine-Tuning of Language Models Using Information Gain\\\"\\n        authors: \\\"Rohan Deb, Kiran Koshy Thekumparampil, Kousha Kalantari, Gaurush Hiranandani, Shoham Sabach, Branislav Kveton\\\"\\n        year: 2025\\n        venue: \\\"ICML 2025\\\"\\n        arxiv_id: \\\"2505.14826\\\"\\n        role: background\\n        key_finding: \\\"用 Fisher 信息矩阵选择信息量最大的训练样本子集，通过 last-layer 线性化高效近似。在固定数据预算下提升 SFT 效果。对 VOTA 的数据选择策略有参考价值。\\\"\\n        metrics: {}\\n\\n      - title: \\\"Fine-Tuned 'Small' LLMs (Still) Significantly Outperform Zero-Shot Generative AI Models in Text Classification\\\"\\n        authors: \\\"Martin Juan Jose Bucher, Marco Martini\\\"\\n        year: 2024\\n        venue: \\\"arXiv 2406.08660\\\"\\n        role: background\\n        key_finding: \\\"跨多种分类任务（情感、立场、情绪等），fine-tuned 小模型全面优于 GPT-4/Claude 的 zero-shot。验证了 VOTA 用 SFT 做 verdict 分类的基本假设——fine-tuning 在分类上优于 prompting。\\\"\\n        metrics: {}\\n\\n  cross-model-generalization:\\n    description: \\\"跨模型 SFT 泛化：不同 base model 上 SFT 效果的迁移与差异\\\"\\n    papers:\\n      - title: \\\"Unveiling the Generalization Power of Fine-Tuned Large Language Models\\\"\\n        authors: \\\"Haoran Yang, Yumeng Zhang, Jiaqi Xu, Hongyuan Lu, Pheng Ann Heng, Wai Lam\\\"\\n        year: 2024\\n        venue: \\\"NAACL 2024\\\"\\n        arxiv_id: \\\"2403.09162\\\"\\n        role: method-component\\n        key_finding: \\\"SFT 后分类任务跨域正迁移，生成任务跨域负迁移。对 VOTA 的跨模型实验设计有直接参考——verdict 分类属于分类任务，预期正迁移。\\\"\\n        metrics: {}\\n\\n      - title: \\\"How Abilities in Large Language Models are Affected by Supervised Fine-tuning Data Composition\\\"\\n        authors: \\\"Guanting Dong, Hongyi Yuan, Keming Lu, et al.\\\"\\n        year: 2024\\n        venue: \\\"ACL 2024\\\"\\n        arxiv_id: \\\"2310.05492\\\"\\n        role: method-component\\n        key_finding: \\\"更大/更强 base model 在相同 SFT 数据量下性能更优。DeepSeek-Coder-6.7B 预训练 2T tokens，Qwen 5.5T，比例 2.75x。对 VOTA 跨模型对比（DeepSeek vs Qwen）提供预训练数据量的基准参考。\\\"\\n        metrics:\\n          deepseek_coder_pretrain_tokens: \\\"2T\\\"\\n          qwen_pretrain_tokens: \\\"5.5T\\\"\\n\\n      - title: \\\"Analyzing the Effects of Supervised Fine-Tuning on Model Knowledge from Token and Parameter Levels\\\"\\n        authors: \\\"Junjie Ye, Yuming Yang, Yang Nan, Shuo Li, Qi Zhang, Tao Gui, Xuanjing Huang, Peng Wang, Zhongchao Shi, Jianping Fan\\\"\\n        year: 2025\\n        venue: \\\"EMNLP 2025\\\"\\n        arxiv_id: \\\"2509.16596\\\"\\n        role: background\\n        key_finding: \\\"SFT 中 90% 参数更新不贡献知识增强；知识掌握水平不同的训练数据导致 >12% 性能波动。对 VOTA 的数据质量控制有参考意义。\\\"\\n        metrics:\\n          non_contributing_param_ratio: \\\"90%\\\"\\n          performance_variation_from_data_quality: \\\">12%\\\"\\n\\n      - title: \\\"From Code to Prediction: Fine-Tuning LLMs for Neural Network Performance Classification in NNGPT\\\"\\n        authors: \\\"Mahmoud Hanouneh, Radu Timofte, Dmitry Ignatov\\\"\\n        year: 2025\\n        venue: \\\"arXiv 2605.03686\\\"\\n        arxiv_id: \\\"2605.03686\\\"\\n        role: background\\n        key_finding: \\\"DeepSeek-Coder-7B-Instruct LoRA 微调做代码分类 80% accuracy。验证 DeepSeek-Coder 系列在代码分类 SFT 上的可行性。\\\"\\n        metrics:\\n          code_classification_accuracy: \\\"80%\\\"\\n\\n      - title: \\\"Qwen2.5-Coder Technical Report\\\"\\n        authors: \\\"Binyuan Hui, Jian Yang, et al. (Qwen Team)\\\"\\n        year: 2024\\n        venue: \\\"arXiv 2409.12186\\\"\\n        arxiv_id: \\\"2409.12186\\\"\\n        role: background\\n        key_finding: \\\"Qwen2.5-Coder 5.5T tokens 预训练，HumanEval 92.7%。作为 VOTA 跨模型实验的 base model 之一，提供预训练规模和代码能力基准。\\\"\\n        metrics:\\n          pretrain_tokens: \\\"5.5T\\\"\\n          humaneval_pass1: \\\"92.7%\\\"\\n\\nmeta:\\n  last_updated: \\\"2026-05-15\\\"\\n  total_papers: 34\\n  search_scope: \\\"2024-2026, top ML/NLP/SE venues\\\"\\n  scan_date: \\\"2026-05-15\\\"\\n  scan_queries: 16\\n  key_gaps:\\n    - \\\"缺少直接将 execution trace 用于 binary verdict (pass/fail) 的工作——VOTA 填补此空白\\\"\\n    - \\\"trace compression 文献多在 distributed systems 或 formal verification 领域，code-level trace 压缩给 LLM 用的工作极少\\\"\\n    - \\\"SFT for classification 研究多在 NLP 文本分类，code verdict 场景的 SFT 方法论研究接近空白\\\"\\n    - \\\"patch correctness prediction（LLM4PatchCorrect、APSG）是最近的竞争方向，但任务定义和输入信号与 VOTA 有本质区别\\\"\\n    - \\\"selective trace（InspectCoder、TraceCoder）趋势明显，但均用于 program repair 而非 verdict classification\\\"\\n\", \"total_chars\": 18596, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd999d01-e16e-4160-b11b-ba785b8c530d",
  "isSidechain": true,
  "promptId": "1671510c-98af-4e06-a3f5-68dced519a8b",
  "agentId": "ac10b8784a4950006",
  "type": "user",
  "uuid": "c6688ac7-a8e1-42ed-bc43-d8765fb8e0c9",
  "sourceToolAssistantUUID": "cd999d01-e16e-4160-b11b-ba785b8c530d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "ab493159-c57d-451b-9109-6ba744c1f6a1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-16T16:34:30.913Z_

Now I have a comprehensive view of the project. I notice a critical issue: the paper summary provided in the user's prompt describes a paper titled "Trace Formatting as Implicit Task Specification: Format Markers Dominate SFT Verdict Prediction" where format marker removal **drops** accuracy to 89.63%. But the actual project data shows the **opposite** result: format marker removal produces **zero** degradation (99.83% stays). The actual paper is titled "Exception Events Are All You Need for Verdict Prediction."

This appears to be a "dream review" scenario — I'm asked to review a hypothetical/imagined version of the paper (one of the dream report variants, likely the "worst" case scenario). Let me check the worst-case dream report to confirm.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6688ac7-a8e1-42ed-bc43-d8765fb8e0c9",
  "isSidechain": true,
  "agentId": "ac10b8784a4950006",
  "requestId": "req_011Cb6a5jAjhL4uoY7dpDnb5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3ffe7632-a24c-4b0b-9645-fafc5f4fdd9c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "ab493159-c57d-451b-9109-6ba744c1f6a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014phqqitaCsfYeUAJyEGRUZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9197,
      "cache_read_input_tokens": 44921,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9197,
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

_source line 28 · 2026-05-16T16:34:33.214Z_

<details open><summary>🔧 Tool call — Read · `toolu_012gXSSkZWpb5vsvUKYCwnSF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260516T155731/worst/paper.tex",
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ffe7632-a24c-4b0b-9645-fafc5f4fdd9c",
  "isSidechain": true,
  "agentId": "ac10b8784a4950006",
  "requestId": "req_011Cb6a5jAjhL4uoY7dpDnb5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "decd06fe-a756-4ccc-b6b5-fde3cd5fe821",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "ab493159-c57d-451b-9109-6ba744c1f6a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014phqqitaCsfYeUAJyEGRUZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9197,
      "cache_read_input_tokens": 44921,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9197
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 288,
          "cache_read_input_tokens": 44921,
          "cache_creation_input_tokens": 9197,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9197,
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

_source line 29 · 2026-05-16T16:34:33.220Z_

<details><summary>↩ Tool result · `toolu_012gXSSkZWpb5vsvUKYCwnSF`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{graphicx}
6	\usepackage{amsmath}
7	\usepackage{amssymb}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{xcolor}
11	\usepackage{subcaption}
12	\usepackage[colorlinks=true,citecolor=blue,linkcolor=blue]{hyperref}
13	\usepackage{natbib}
14	\bibliographystyle{plainnat}
15	
16	\newcommand{\pp}{\,\text{pp}}
17	\newcommand{\eg}{e.g.}
18	\newcommand{\ie}{i.e.}
19	
20	\title{Trace Formatting as Implicit Task Specification:\\Format Markers Dominate SFT Verdict Prediction}
21	
22	\author{Anonymous}
23	
24	\begin{document}
25	\maketitle
26	
27	% ============================================================
28	\begin{abstract}
29	Supervised fine-tuning (SFT) on execution traces has been proposed as a method to improve code understanding, yet the mechanisms behind performance gains remain poorly understood.
30	We study verdict prediction---binary pass/fail classification of code solutions---and discover that \textbf{format markers in trace representations account for 41.3\% of the total accuracy lift}, acting as classification shortcuts rather than enabling genuine fault reasoning.
31	Through systematic ablation across three model families (1.5B--13B parameters), we show that: (1) an SFT model trained on exception traces with format markers (99.83\%) barely outperforms a regular-expression baseline (99.33\%, $\Delta$=0.50$\pp$); (2) removing format markers drops SFT accuracy to 89.63\%, \emph{below} the regex baseline; and (3) exception-only performance is perfectly scale-invariant (1.5B = 7B = 13B), consistent with trivial pattern matching rather than fault understanding.
32	We decompose the total trace lift of 24.7$\pp$ into a content signal of ${\sim}$14.5$\pp$ (59\%) and a format marker shortcut of ${\sim}$10.2$\pp$ (41\%), and find that format marker contribution alone exceeds the entire benefit of full-trace SFT (6.6$\pp$).
33	These results reframe trace SFT as a study in \emph{implicit task specification}: trace format and structure choices exert an outsized, hidden impact on downstream classification, echoing findings from annotation artifact and shortcut learning research in NLI.
34	We provide practical design principles for trace representations that account for shortcut affordance.
35	\end{abstract}
36	
37	% ============================================================
38	\section{Introduction}
39	\label{sec:intro}
40	
41	Execution traces---runtime records of program behavior---have attracted growing attention as a training signal for code language models.
42	Recent work such as DCSH~\cite{gu2024execution} and TracePile~\cite{wang2025tracepile} demonstrates that traces can improve code generation, though benefits are inconsistent and model-dependent.
43	An orthogonal but underexplored application is \emph{verdict prediction}: classifying whether a code solution passes or fails a given test case.
44	Verdict prediction is a practical task in automated evaluation pipelines and CI/CD systems, and its binary nature allows precise attribution of what information drives model decisions.
45	
46	We investigate trace SFT for verdict prediction using VOTA (Variable-Operation-Trace Abstraction), a structured trace compression pipeline that decomposes full execution traces into three components: \emph{loop compression}, \emph{exception summaries}, and \emph{actual/expected value pairs}.
47	Our initial experiments on Qwen-2.5-Coder-7B appear to tell a positive story: exception-only traces achieve 99.83\% accuracy, vastly outperforming no-trace baselines (75.13\%) and full-trace SFT (81.76\%).
48	Across three random seeds, performance is perfectly stable ($\pm$0.00), and calibration is near-perfect (ECE=0.0027).
49	
50	However, a closer examination reveals a troubling picture.
51	A simple regular expression that checks for the presence of a format marker---the string \texttt{[No exception data in trace]}---achieves 99.33\% accuracy without any model training.
52	The SFT model's advantage over this regex is a mere 0.50$\pp$.
53	When we retrain the model on traces with format markers removed, accuracy drops to 89.63\% ($\Delta$=$-$10.20$\pp$) and falls \emph{below} the regex baseline.
54	The model's near-perfect performance was driven not by understanding fault semantics, but by learning a classification shortcut tied to trace formatting conventions.
55	
56	This finding connects to a broader literature on shortcut learning in NLP.
57	\citet{gururangan2018annotation} showed that annotation artifacts allow hypothesis-only models to achieve high NLI accuracy; \citet{mccoy2019right} demonstrated that syntactic heuristics explain much of BERT's NLI performance; and \citet{gardner2021competency} argued that evaluations must test for shortcut reliance.
58	Our work extends this line of inquiry to the code domain, showing that \emph{trace format design choices} function as implicit task specifications that can dominate the learning signal.
59	
60	Our contributions are:
61	\begin{enumerate}
62	    \item We show that structured format markers dominate verdict prediction in exception traces, contributing 10.2$\pp$ (41.3\% of total trace lift) and reducing SFT to near-regex-level pattern matching (\S\ref{sec:marker-removal}).
63	    \item We decompose the trace compression benefit into information density (74\%) and gradient dilution (26\%) through label-only loss ablation, and show that format marker accessibility---not content richness---is the primary mechanism (\S\ref{sec:density}).
64	    \item We demonstrate that format engineering outweighs content richness for SFT verdict tasks: exception dominance is model-specific (fails on CodeLlama-13B), scale-invariant performance (1.5B=7B) indicates trivial pattern complexity, and marker-free SFT performs comparably to loop-only compression (\S\ref{sec:format-engineering}).
65	\end{enumerate}
66	
67	% ============================================================
68	\section{Related Work}
69	\label{sec:related}
70	
71	\paragraph{Trace-augmented code models.}
72	DCSH~\cite{gu2024execution} evaluated five trace formats for SFT on code generation tasks, finding that no single trace representation consistently outperforms others across models.
73	TracePile~\cite{wang2025tracepile} scaled trace collection to 2.6M samples but evaluated only on generative tasks.
74	TRACED~\cite{chen2024traced} showed traces improve encoder-based code classification.
75	All prior work focuses on generation or uses encoder models; none has systematically studied what trace components drive SFT classification performance.
76	
77	\paragraph{Shortcut learning and annotation artifacts.}
78	A growing body of work has shown that NLP models exploit superficial patterns rather than learning intended task semantics.
79	\citet{gururangan2018annotation} demonstrated that hypothesis-only baselines achieve substantial NLI accuracy due to annotation artifacts.
80	\citet{mccoy2019right} showed BERT relies on syntactic heuristics (lexical overlap, subsequence, constituent) for NLI.
81	\citet{niven2019probing} found that argument reasoning comprehension models exploit unigram statistics.
82	\citet{gardner2021competency} proposed contrast sets for more rigorous evaluation.
83	Our work identifies an analogous phenomenon in trace SFT: format markers in trace representations serve as classification shortcuts, and their removal dramatically degrades performance.
84	
85	\paragraph{Verdict prediction.}
86	Binary pass/fail prediction from code and test inputs has received limited direct attention.
87	Most related work treats it as a subtask of automated program repair or test generation.
88	To our knowledge, we are the first to systematically study what execution trace components drive verdict prediction accuracy and to identify format-level shortcuts in this setting.
89	
90	% ============================================================
91	\section{Method}
92	\label{sec:method}
93	
94	\subsection{Task Definition}
95	
96	Given a code solution $c$, a test input $x$, and optionally an execution trace representation $t$, the model predicts the verdict $v \in \{\texttt{pass}, \texttt{fail}\}$.
97	The dataset comprises 591 problems from HumanEval (164) and MBPP-sanitized (427), each with 10 LLM-generated solutions, yielding 5,910 samples (71.5\% pass, 28.5\% fail).
98	We use a 4,720/1,190 train/test split with no problem-level overlap.
99	
100	\subsection{VOTA Trace Compression}
101	
102	VOTA decomposes full execution traces into three structured components:
103	
104	\begin{itemize}
105	    \item \textbf{Loop compression}: Summarizes repetitive loop iterations into compact patterns capturing iteration counts and behavioral summaries.
106	    \item \textbf{Exception summaries}: Extracts exception events, formatted as \texttt{[ERROR] type: message} for failing cases and \texttt{[No exception data in trace]} for passing cases.
107	    \item \textbf{Actual/expected (AE) pairs}: Captures assertion-point value comparisons from test execution.
108	\end{itemize}
109	
110	Critically, the exception summary component introduces explicit \emph{format markers}---the strings \texttt{[No exception data in trace]} and \texttt{[ERROR]}---that directly encode the pass/fail distinction in a fixed, easily recognizable format.
111	
112	\subsection{Trace Conditions}
113	
114	We evaluate six primary trace conditions:
115	\textbf{no\_trace} (code + test input only),
116	\textbf{full\_trace} (complete execution trace, ${\sim}$2048 tokens),
117	\textbf{VOTA} (all three VOTA components),
118	\textbf{exception\_only} (exception summaries with format markers),
119	\textbf{ae\_only} (actual/expected pairs only),
120	and \textbf{loop\_only} (loop compression only).
121	
122	\subsection{Format Marker Removal (nomarker)}
123	\label{sec:nomarker-method}
124	
125	To causally quantify the contribution of format markers, we create a \emph{nomarker} variant of exception\_only traces.
126	For passing samples, the \texttt{[No exception data in trace]} marker is replaced with empty or minimal text, removing the explicit pass signal.
127	For failing samples, exception content is preserved but the \texttt{[ERROR]} prefix is stripped.
128	Models are retrained from scratch on nomarker traces across three random seeds (42, 123, 456).
129	
130	\subsection{Training Setup}
131	
132	All models are fine-tuned with LoRA (rank 64, $\alpha$=128) for 3 epochs using SFTTrainer.
133	Learning rate: $2 \times 10^{-4}$ with cosine schedule.
134	Maximum sequence length: 2,048 tokens.
135	We evaluate on Qwen-2.5-Coder-7B (primary), Qwen-2.5-Coder-1.5B, DeepSeek-Coder-6.7B, and CodeLlama-13B-Instruct.
136	
137	\subsection{Regex Baselines}
138	
139	To contextualize SFT performance, we define deterministic regex baselines:
140	\begin{itemize}
141	    \item \textbf{Regex B5}: Predicts \texttt{pass} if \texttt{[No exception data in trace]} is present, else \texttt{fail}. Accuracy: 99.33\%.
142	    \item \textbf{Regex B1}: Predicts \texttt{fail} if \texttt{[ERROR]} is present, else \texttt{pass}. Accuracy: 93.45\%.
143	\end{itemize}
144	
145	% ============================================================
146	\section{Experiments}
147	\label{sec:experiments}
148	
149	\subsection{Main Results}
150	\label{sec:main-results}
151	
152	Table~\ref{tab:main} presents verdict prediction accuracy across all trace conditions and models.
153	On Qwen-2.5-Coder-7B, exception\_only achieves 99.83\%, a 24.7$\pp$ lift over the no\_trace baseline (75.13\%).
154	VOTA achieves 99.41\% and full\_trace 81.76\%.
155	The label-only loss variant of full\_trace achieves 86.22\%, decomposing the full\_trace--VOTA gap into 26\% gradient dilution and 74\% information overload (\S\ref{sec:density}).
156	
157	\begin{table}[t]
158	\centering
159	\small
160	\begin{tabular}{lcccc}
161	\toprule
162	\textbf{Condition} & \textbf{Qwen-7B} & \textbf{Qwen-1.5B} & \textbf{DS-6.7B} & \textbf{CL-13B} \\
163	\midrule
164	no\_trace          & 75.13 & 67.31 & 73.36 & 76.50 \\
165	full\_trace        & 81.76 & 77.06 & 79.16 & --- \\
166	\quad + label-only & 86.22 & --- & --- & --- \\
167	loop\_only         & 85.63 & --- & --- & --- \\
168	VOTA               & 99.41 & 99.58 & 84.45 & 99.92 \\
169	exception\_only    & 99.83 & 99.83 & 99.33$^\dagger$ & 99.83 \\
170	ae\_only           & 99.92 & --- & --- & --- \\
171	\midrule
172	Regex B5           & \multicolumn{4}{c}{99.33} \\
173	Regex B1           & \multicolumn{4}{c}{93.45} \\
174	\bottomrule
175	\end{tabular}
176	\caption{Verdict prediction accuracy (\%) across trace conditions and models. DS = DeepSeek-Coder, CL = CodeLlama-Instruct. $\dagger$: median of 3 seeds (seed123 outlier at 91.09\%). Regex baselines are deterministic and model-independent.}
177	\label{tab:main}
178	\end{table}
179	
180	A striking pattern emerges: exception\_only matches across scales (1.5B = 7B = 13B = 99.83\%) while no\_trace and full\_trace show clear capacity effects (67.31\% vs.\ 75.13\% vs.\ 76.50\% for no\_trace).
181	If exception\_only required genuine fault reasoning, we would expect at least a small capacity gap between 1.5B and 7B models.
182	The absence of any gap suggests the task's effective complexity is trivially low---consistent with format marker matching.
183	
184	\subsection{Component Ablation}
185	\label{sec:ablation}
186	
187	Table~\ref{tab:ablation} decomposes VOTA into its three components.
188	A two-tier structure emerges: exception\_only (99.83\%) and ae\_only (99.92\%) form Tier 1 with near-perfect accuracy, while loop\_only (85.63\%) constitutes Tier 2.
189	
190	\begin{table}[t]
191	\centering
192	\small
193	\begin{tabular}{lccc}
194	\toprule
195	\textbf{Component} & \textbf{Accuracy} & \textbf{Pass F1} & \textbf{Fail F1} \\
196	\midrule
197	exception\_only & 99.83 & --- & --- \\
198	ae\_only & 99.92 & --- & --- \\
199	VOTA (all) & 99.41 & --- & --- \\
200	\quad $-$ ae (no\_ae) & 99.41 & 99.60 & 98.90 \\
201	loop\_only & 85.63 & --- & --- \\
202	\bottomrule
203	\end{tabular}
204	\caption{VOTA component ablation on Qwen-7B. Tier 1 components (exception, ae) both contain strong format markers. Tier 2 (loop) lacks explicit markers.}
205	\label{tab:ablation}
206	\end{table}
207	
208	Under our reanalysis, this hierarchy reflects \emph{format marker strength}, not diagnostic value.
209	Both Tier 1 components contain explicit format markers: exception traces have \texttt{[No exception data in trace]} / \texttt{[ERROR]}, and ae traces contain structured assertion result markers.
210	Loop compression, lacking such markers, achieves only 85.63\%---representing the ceiling of content-level learning without format shortcuts.
211	Removing AE from VOTA has no effect (99.41\% $\to$ 99.41\%), confirming that the active ingredient is the exception format marker, not AE content.
212	
213	\subsection{Format Marker Removal: The Core Experiment}
214	\label{sec:marker-removal}
215	
216	Table~\ref{tab:nomarker} presents our central result.
217	Removing format markers from exception\_only traces and retraining across three seeds yields a mean accuracy of 89.63\% ($\pm$2.50$\pp$), a drop of 10.20$\pp$ from the marker-present condition.
218	
219	\begin{table}[t]
220	\centering
221	\small
222	\begin{tabular}{lccccc}
223	\toprule
224	\textbf{Seed} & \textbf{With marker} & \textbf{Without} & \textbf{$\Delta$} & \textbf{Pass R} & \textbf{Fail R} \\
225	\midrule
226	42  & 99.83 & 91.76 & $-$8.07 & 0.887 & 0.993 \\
227	123 & 99.83 & 86.80 & $-$13.03 & 0.821 & 0.985 \\
228	456 & 99.83 & 90.34 & $-$9.49 & 0.868 & 0.991 \\
229	\midrule
230	Mean & 99.83 & 89.63 & $-$10.20 & 0.859 & 0.990 \\
231	Std  & 0.00  & 2.50  & --- & --- & --- \\
232	\bottomrule
233	\end{tabular}
234	\caption{Format marker removal results. Pass R = pass recall, Fail R = fail recall. Marker removal disproportionately affects pass detection (recall drops from 0.998 to 0.859) while fail detection remains high (0.990).}
235	\label{tab:nomarker}
236	\end{table}
237	
238	Three observations establish the shortcut learning diagnosis:
239	
240	\paragraph{SFT $\approx$ Regex with markers.}
241	SFT exception\_only (99.83\%) exceeds Regex B5 (99.33\%) by only 0.50$\pp$.
242	The SFT model's value-add over a zero-parameter string match is negligible.
243	
244	\paragraph{SFT $<$ Regex without markers.}
245	After marker removal, SFT drops to 89.63\%, falling 9.70$\pp$ \emph{below} the regex baseline.
246	The format marker was the load-bearing mechanism; without it, the neural model underperforms a trivial rule.
247	
248	\paragraph{Asymmetric degradation.}
249	Pass recall drops sharply (0.998 $\to$ 0.859) because passing traces lose their sole explicit signal (the \texttt{[No exception data in trace]} marker).
250	Fail recall remains high (0.998 $\to$ 0.990) because failing traces retain semantic exception content (\eg, \texttt{AssertionError}, \texttt{TypeError}), even without the \texttt{[ERROR]} prefix.
251	
252	\paragraph{Lift decomposition.}
253	The total trace lift of 24.7$\pp$ (no\_trace 75.13\% $\to$ exception\_only 99.83\%) decomposes as:
254	\begin{itemize}
255	    \item Content signal: ${\sim}$14.5$\pp$ (89.63\% $-$ 75.13\%), accounting for 59\% of the lift.
256	    \item Format marker shortcut: ${\sim}$10.2$\pp$ (99.83\% $-$ 89.63\%), accounting for 41\%.
257	\end{itemize}
258	The format marker contribution alone (10.2$\pp$) exceeds the \emph{entire} benefit of full-trace SFT (6.6$\pp$), underscoring the outsized impact of formatting decisions.
259	
260	\begin{table}[t]
261	\centering
262	\small
263	\begin{tabular}{lcc}
264	\toprule
265	\textbf{Method} & \textbf{Accuracy (\%)} & \textbf{Mechanism} \\
266	\midrule
267	Regex B5 & 99.33 & Marker presence check \\
268	SFT + markers & 99.83 & Marker + minor content \\
269	SFT $-$ markers & 89.63 & Content only \\
270	Regex B1 & 93.45 & \texttt{[ERROR]} keyword \\
271	\bottomrule
272	\end{tabular}
273	\caption{SFT vs.\ regex comparison. With markers, SFT barely exceeds a regex ($\Delta$=0.50$\pp$). Without markers, SFT falls below both regex baselines.}
274	\label{tab:sft-vs-regex}
275	\end{table}
276	
277	\subsection{Information Density vs.\ Gradient Dilution}
278	\label{sec:density}
279	
280	Why does full-trace SFT (81.76\%) dramatically underperform exception\_only (99.83\%) despite containing a superset of the information?
281	We disentangle two hypotheses through a label-only loss ablation: training on full traces but computing loss only on verdict tokens (masking trace token gradients).
282	
283	Label-only full\_trace achieves 86.22\%, a 4.5$\pp$ improvement over standard full\_trace (81.76\%).
284	This attributes 26\% of the gap to gradient dilution (trace tokens diluting the learning signal) and 74\% to information overload (the model's inability to extract relevant signals from thousands of tokens).
285	
286	\begin{table}[t]
287	\centering
288	\small
289	\begin{tabular}{lcc}
290	\toprule
291	\textbf{Condition} & \textbf{Accuracy (\%)} & \textbf{Bottleneck} \\
292	\midrule
293	exception\_only & 99.83 & --- \\
294	VOTA & 99.41 & --- \\
295	label-only full & 86.22 & Information overload only \\
296	loop\_only & 85.63 & Content learning ceiling \\
297	full\_trace & 81.76 & Both \\
298	\midrule
299	\multicolumn{3}{l}{\small Gradient dilution: 4.5$\pp$ (26\%)} \\
300	\multicolumn{3}{l}{\small Information overload: 13.0$\pp$ (74\%)} \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "decd06fe-a756-4ccc-b6b5-fde3cd5fe821",
  "isSidechain": true,
  "promptId": "1671510c-98af-4e06-a3f5-68dced519a8b",
  "agentId": "ac10b8784a4950006",
  "type": "user",
  "uuid": "eb8c73ba-8918-4476-90b1-bd4b26c3fb61",
  "sourceToolAssistantUUID": "decd06fe-a756-4ccc-b6b5-fde3cd5fe821",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "ab493159-c57d-451b-9109-6ba744c1f6a1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-16T16:34:38.329Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PjN5B3itGqixjyEsTFgSXo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260516T155731/worst/paper.tex",
  "offset": 300,
  "limit": 250
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb8c73ba-8918-4476-90b1-bd4b26c3fb61",
  "isSidechain": true,
  "agentId": "ac10b8784a4950006",
  "requestId": "req_011Cb6a6YXogXtiKX6a582S9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "35eaef70-d2e6-4259-8933-9582f6fb1abc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "ab493159-c57d-451b-9109-6ba744c1f6a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QVe6Xc2beXn2EE9DmW81vL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6604,
      "cache_read_input_tokens": 54118,
      "output_tokens": 134,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6604
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 134,
          "cache_read_input_tokens": 54118,
          "cache_creation_input_tokens": 6604,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6604,
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

_source line 31 · 2026-05-16T16:34:38.349Z_

<details><summary>↩ Tool result · `toolu_01PjN5B3itGqixjyEsTFgSXo`</summary>

```text
300	\multicolumn{3}{l}{\small Information overload: 13.0$\pp$ (74\%)} \\
301	\bottomrule
302	\end{tabular}
303	\caption{Gradient dilution decomposition. Label-only loss removes gradient dilution but cannot close the 13$\pp$ gap to exception\_only, confirming information density as the primary bottleneck.}
304	\label{tab:density}
305	\end{table}
306	
307	Under the shortcut learning lens, the 74\% ``information overload'' component has a precise interpretation: format markers exist in full traces but are buried among thousands of tokens, reducing their accessibility.
308	Exception\_only isolates the marker in a compact context where it occupies the most prominent position, maximizing shortcut exploitability.
309	The near-identical performance of label-only full\_trace (86.22\%) and loop\_only (85.63\%) confirms that without accessible format markers, different trace representations converge to the same content-level learning ceiling (${\sim}$86\%).
310	
311	\subsection{Trace Length Ablation}
312	\label{sec:length}
313	
314	Table~\ref{tab:length} shows full-trace accuracy at different truncation lengths.
315	Performance is non-monotonic and uniformly far below exception\_only, confirming that more trace tokens do not improve format marker utilization---the marker's relative prominence, not absolute trace content, determines effectiveness.
316	
317	\begin{table}[t]
318	\centering
319	\small
320	\begin{tabular}{lc}
321	\toprule
322	\textbf{Trace length} & \textbf{Accuracy (\%)} \\
323	\midrule
324	256 tokens & 78.82 \\
325	512 tokens & 80.42 \\
326	1024 tokens & 77.23 \\
327	2048 tokens (full) & 81.76 \\
328	\midrule
329	exception\_only & 99.83 \\
330	\bottomrule
331	\end{tabular}
332	\caption{Full-trace accuracy by truncation length. Non-monotonic pattern with all values far below exception\_only, indicating that format marker accessibility, not trace volume, drives performance.}
333	\label{tab:length}
334	\end{table}
335	
336	\subsection{Scale Invariance as Shortcut Evidence}
337	\label{sec:format-engineering}
338	
339	Table~\ref{tab:scale} presents the scale invariance analysis.
340	Exception\_only yields identical accuracy (99.83\%) across 1.5B, 7B, and 13B parameters, while capacity-sensitive conditions (no\_trace, full\_trace) show clear scaling effects.
341	
342	\begin{table}[t]
343	\centering
344	\small
345	\begin{tabular}{lccc}
346	\toprule
347	\textbf{Condition} & \textbf{1.5B} & \textbf{7B} & \textbf{13B} \\
348	\midrule
349	no\_trace & 67.31 & 75.13 & 76.50 \\
350	full\_trace & 77.06 & 81.76 & --- \\
351	exception\_only & 99.83 & 99.83 & 99.83 \\
352	VOTA & 99.58 & 99.41 & 99.92 \\
353	\bottomrule
354	\end{tabular}
355	\caption{Scale invariance analysis across Qwen-1.5B, Qwen-7B, and CodeLlama-13B. Exception\_only is perfectly scale-invariant, consistent with trivial pattern complexity. No\_trace shows expected capacity scaling.}
356	\label{tab:scale}
357	\end{table}
358	
359	If exception\_only required genuine fault reasoning---understanding exception types, relating them to code behavior, assessing severity---we would expect a capacity gap between 1.5B and 7B.
360	The complete absence of such a gap, combined with clear capacity effects on harder conditions, constitutes strong evidence that exception\_only's effective task complexity is at the level of format marker matching.
361	
362	On CodeLlama-13B, VOTA (99.92\%) \emph{exceeds} exception\_only (99.83\%), breaking the ``exception dominance'' pattern observed on smaller models.
363	This suggests that exception dominance is model-specific: smaller models can only exploit the single most salient format shortcut (exception marker), while larger models simultaneously exploit multiple format cues across VOTA components.
364	
365	\subsection{Cross-Model Validation}
366	\label{sec:cross-model}
367	
368	Table~\ref{tab:deepseek} presents DeepSeek-Coder-6.7B results.
369	Two of three seeds achieve 99.33\%---precisely matching Regex B5---while seed123 is an outlier at 91.09\%.
370	
371	\begin{table}[t]
372	\centering
373	\small
374	\begin{tabular}{lcccc}
375	\toprule
376	\textbf{Condition} & \textbf{s42} & \textbf{s123} & \textbf{s456} & \textbf{Median} \\
377	\midrule
378	exception\_only & 99.33 & 91.09 & 99.33 & 99.33 \\
379	VOTA & 84.45 & --- & --- & --- \\
380	no\_trace & 73.36 & --- & --- & --- \\
381	full\_trace (v3) & 79.16 & --- & --- & --- \\
382	\bottomrule
383	\end{tabular}
384	\caption{DeepSeek-Coder-6.7B results. Two seeds match Regex B5 exactly (99.33\%), suggesting SFT learns the same pattern. Seed123 outlier reflects LoRA initialization sensitivity.}
385	\label{tab:deepseek}
386	\end{table}
387	
388	The exact match between two SFT seeds and the regex baseline is suggestive: two independently initialized SFT models and a simple string-match rule converge to the same accuracy, consistent with the hypothesis that all three are performing the same operation---format marker detection.
389	The seed123 outlier (91.09\%, fail\_recall=0.705) reveals that format shortcut learning is not guaranteed: a poor LoRA initialization can prevent the model from fully acquiring the marker$\to$verdict mapping.
390	
391	\subsection{Seed Robustness and Variance}
392	\label{sec:seed}
393	
394	Table~\ref{tab:seed} contrasts seed robustness with and without format markers.
395	
396	\begin{table}[t]
397	\centering
398	\small
399	\begin{tabular}{lcc}
400	\toprule
401	\textbf{Condition} & \textbf{Mean $\pm$ Std (\%)} & \textbf{Seeds} \\
402	\midrule
403	\multicolumn{3}{l}{\emph{With format markers}} \\
404	\quad exception\_only (Qwen) & 99.83 $\pm$ 0.00 & 3 \\
405	\quad ae\_only (Qwen) & 99.64 $\pm$ 0.49 & 3 \\
406	\midrule
407	\multicolumn{3}{l}{\emph{Without format markers}} \\
408	\quad nomarker (Qwen) & 89.63 $\pm$ 2.50 & 3 \\
409	\midrule
410	\multicolumn{3}{l}{\emph{No format markers (by design)}} \\
411	\quad loop\_only (Qwen) & 86.05 $\pm$ 0.52 & 3 \\
412	\quad label-only full (Qwen) & 86.39 $\pm$ 0.60 & 3 \\
413	\bottomrule
414	\end{tabular}
415	\caption{Seed robustness comparison. Zero variance with markers is a hallmark of shortcut learning: a trivial pattern is reliably learned regardless of initialization. Variance increases dramatically upon marker removal.}
416	\label{tab:seed}
417	\end{table}
418	
419	The variance pattern is diagnostic: with markers, exception\_only achieves perfect reproducibility (std=0.00$\pp$); without markers, variance increases to 2.50$\pp$.
420	This parallels findings in NLI shortcut literature, where hypothesis-only models (exploiting annotation artifacts) show higher stability than models relying on genuine linguistic reasoning~\cite{gururangan2018annotation}.
421	Zero variance is not evidence of robustness---it is a signature of pattern simplicity.
422	
423	\subsection{Multi-Seed Component Analysis}
424	
425	Table~\ref{tab:multiseed} provides three-seed statistics for additional VOTA components, establishing the relationship between format marker strength and variance.
426	
427	\begin{table}[t]
428	\centering
429	\small
430	\begin{tabular}{lccc}
431	\toprule
432	\textbf{Component} & \textbf{Mean (\%)} & \textbf{Std ($\pp$)} & \textbf{Marker?} \\
433	\midrule
434	exception\_only & 99.83 & 0.00 & Strong \\
435	ae\_only & 99.64 & 0.49 & Medium \\
436	loop\_only & 86.05 & 0.52 & None \\
437	label-only full & 86.39 & 0.60 & Diluted \\
438	nomarker & 89.63 & 2.50 & Removed \\
439	\bottomrule
440	\end{tabular}
441	\caption{Multi-seed statistics by component. Higher accuracy correlates with stronger format markers. The nomarker condition's high variance reflects the transition from shortcut to content learning.}
442	\label{tab:multiseed}
443	\end{table}
444	
445	A clear pattern emerges: strong format markers yield high accuracy with low variance (exception: 99.83$\pm$0.00); medium markers yield high accuracy with moderate variance (ae: 99.64$\pm$0.49); absent markers yield moderate accuracy with low variance (loop/label-only: ${\sim}$86$\pm$0.5); and removed markers yield moderate accuracy with \emph{high} variance (nomarker: 89.63$\pm$2.50).
446	The elevated variance in the nomarker condition reflects the instability of content-level learning compared to the deterministic shortcut.
447	
448	\subsection{Calibration Analysis}
449	\label{sec:calibration}
450	
451	Table~\ref{tab:calibration} presents calibration metrics.
452	
453	\begin{table}[t]
454	\centering
455	\small
456	\begin{tabular}{lcc}
457	\toprule
458	\textbf{Condition} & \textbf{ECE} & \textbf{Brier} \\
459	\midrule
460	exception\_only & 0.0027 & 0.0013 \\
461	ae\_only & 0.0004 & 0.0008 \\
462	VOTA & 0.0054 & 0.0050 \\
463	loop\_only & 0.0831 & --- \\
464	full\_trace & 0.0958 & --- \\
465	no\_trace & 0.1715 & 0.1972 \\
466	nomarker (est.) & ${\sim}$0.065 & ${\sim}$0.085 \\
467	\bottomrule
468	\end{tabular}
469	\caption{Calibration comparison. Exception\_only's near-perfect ECE reflects the deterministic nature of the format shortcut, not genuine uncertainty estimation. Marker removal degrades ECE by ${\sim}$24$\times$.}
470	\label{tab:calibration}
471	\end{table}
472	
473	Exception\_only's near-perfect calibration (ECE=0.0027) initially appears to indicate deep understanding---the model ``knows what it knows.''
474	However, under the shortcut interpretation, this calibration is a natural consequence of a near-deterministic mapping: marker present $\to$ high-confidence pass; marker absent $\to$ high-confidence fail.
475	A perfect shortcut inherently produces perfect calibration.
476	After marker removal, ECE degrades approximately 24$\times$ to ${\sim}$0.065, confirming that calibration was a byproduct of the shortcut rather than evidence of semantic understanding.
477	
478	\subsection{DebugBench Generalization}
479	\label{sec:debugbench}
480	
481	Table~\ref{tab:debugbench} presents results on a DebugBench subset as a secondary generalization check.
482	
483	\begin{table}[t]
484	\centering
485	\small
486	\begin{tabular}{lcc}
487	\toprule
488	\textbf{Condition} & \textbf{Main dataset} & \textbf{DebugBench} \\
489	\midrule
490	no\_trace & 75.13 & 96.71 \\
491	VOTA & 99.41 & 99.77 \\
492	exception\_only & 99.83 & 100.00 \\
493	\bottomrule
494	\end{tabular}
495	\caption{DebugBench results (secondary evidence). The high no\_trace baseline (96.71\%) creates a ceiling effect, making trace lift negligible (3.29$\pp$). This dataset cannot distinguish format shortcuts from content learning.}
496	\label{tab:debugbench}
497	\end{table}
498	
499	The high no\_trace baseline on DebugBench (96.71\%) creates a ceiling effect: trace lift is only 3.29$\pp$, too small to discriminate between content learning and format shortcuts.
500	Exception\_only achieves 100\%, which may reflect perfect alignment between DebugBench's bug structure and the format marker, rather than robust fault reasoning.
501	We include this result for completeness but draw no mechanistic conclusions from it.
502	
503	% ============================================================
504	\section{Discussion}
505	\label{sec:discussion}
506	
507	\subsection{Trace Format as Implicit Task Specification}
508	
509	Our central finding is that trace formatting choices---seemingly innocuous decisions about how to represent execution information---function as implicit task specifications that dominate the downstream learning signal.
510	The \texttt{[No exception data in trace]} marker was introduced as a human-readable placeholder, not as a classification feature.
511	Yet it became the primary mechanism by which SFT models achieve near-perfect verdict accuracy.
512	
513	This parallels the annotation artifact phenomenon in NLU~\cite{gururangan2018annotation}: dataset construction choices inadvertently encode the target label, allowing models to solve the task through superficial pattern matching.
514	The key difference is that our ``artifacts'' are in the \emph{input representation}, not the annotation process---trace format design choices create shortcuts just as effectively as annotator biases.
515	
516	\subsection{Practical Implications}
517	
518	Our decomposition of the 24.7$\pp$ trace lift---14.5$\pp$ from content, 10.2$\pp$ from format markers---has direct implications for trace representation design:
519	
520	\begin{enumerate}
521	    \item \textbf{Format ablation as mandatory control.} Any evaluation of SFT on structured trace representations should include format marker removal as a control condition.
522	    Without it, performance gains may be misattributed to content learning when they are driven by formatting shortcuts.
523	    \item \textbf{Deliberate format engineering.} If practitioners \emph{want} format shortcuts (for deployment simplicity), they should make this choice explicitly.
524	    A regex achieving 99.33\% may be preferable to an SFT model achieving 99.83\% at far greater computational cost.
525	    \item \textbf{Content-level evaluation.} The nomarker condition (89.63\%) better reflects genuine content learning.
526	    Models intended for robust fault detection should be evaluated on marker-free traces.
527	\end{enumerate}
528	
529	\subsection{Why Exception Dominance Is Model-Specific}
530	
531	On Qwen-7B and Qwen-1.5B, exception\_only (99.83\%) outperforms VOTA (99.41--99.58\%).
532	But on CodeLlama-13B, VOTA (99.92\%) exceeds exception\_only (99.83\%).
533	This reversal suggests that exception dominance is not a universal property of the signal but an artifact of model capacity: smaller models can only exploit the single most salient shortcut, while larger models simultaneously leverage multiple format cues across VOTA's components.
534	
535	\subsection{DeepSeek VOTA Gap and Training-Time Truncation}
536	
537	DeepSeek VOTA achieves only 84.45\%, a 14.96$\pp$ gap from Qwen.
538	Analysis reveals that 91.7\% of DeepSeek VOTA training samples had trace content truncated from a mean of 2,626 to ${\sim}$2,048 tokens (verdict labels were preserved).
539	Group analysis shows truncated-train samples achieve 83.04\% vs.\ 100\% for intact samples (Fisher's exact $p \approx 0$), establishing a causal link between training-time truncation and degraded performance.
540	Exception\_only traces, being far shorter than 2,048 tokens, are unaffected by truncation---further explaining their relative robustness.
541	
542	\subsection{Irreducible Error Analysis}
543	
544	The two errors shared across all three Qwen exception\_only seeds (samples 901, 905; both from HumanEval/95 \texttt{check\_dict\_case}) stem from Python's \texttt{all()} short-circuiting on a generator expression, triggering \texttt{GeneratorExit} (a \texttt{BaseException} subclass, not a genuine error).
545	The tracer labels these as \texttt{[ERROR]}, and the model reasonably but incorrectly predicts fail.
546	This confirms 99.83\% as the representation's theoretical ceiling and illustrates a limitation of the exception\_only format: it conflates control-flow mechanisms (\texttt{GeneratorExit}) with actual errors.
547	
548	\subsection{Token-Level Loss vs.\ Verdict Accuracy}
549	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "35eaef70-d2e6-4259-8933-9582f6fb1abc",
  "isSidechain": true,
  "promptId": "1671510c-98af-4e06-a3f5-68dced519a8b",
  "agentId": "ac10b8784a4950006",
  "type": "user",
  "uuid": "00ed9caa-853f-4653-83c7-e3bd68268929",
  "sourceToolAssistantUUID": "35eaef70-d2e6-4259-8933-9582f6fb1abc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "ab493159-c57d-451b-9109-6ba744c1f6a1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-16T16:34:43.996Z_

<details open><summary>🔧 Tool call — Read · `toolu_015AzMxjFSfW8bRpgaPmuycz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260516T155731/worst/paper.tex",
  "offset": 549,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00ed9caa-853f-4653-83c7-e3bd68268929",
  "isSidechain": true,
  "agentId": "ac10b8784a4950006",
  "requestId": "req_011Cb6a6vLUeg777aCNPUERd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6408ec39-15fb-4b19-a5e6-15ebf39240c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "ab493159-c57d-451b-9109-6ba744c1f6a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VtAGfBjyfdrzSkiAhdRfwm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4948,
      "cache_read_input_tokens": 60722,
      "output_tokens": 134,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4948
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 134,
          "cache_read_input_tokens": 60722,
          "cache_creation_input_tokens": 4948,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4948,
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

_source line 33 · 2026-05-16T16:34:44.003Z_

<details><summary>↩ Tool result · `toolu_015AzMxjFSfW8bRpgaPmuycz`</summary>

```text
549	
550	On DeepSeek, eval\_loss increases from epoch 1 to 3 ($+$65\%) while verdict accuracy improves ($+$6.3$\pp$).
551	Furthermore, two DeepSeek seeds with nearly identical train loss (0.1225 vs.\ 0.122) differ by 8.2$\pp$ in accuracy (99.33\% vs.\ 91.09\%).
552	Token-level loss is a poor proxy for binary classification performance; verdict-specific metrics should guide checkpoint selection.
553	
554	\subsection{Limitations}
555	
556	\begin{itemize}
557	    \item Our dataset covers only HumanEval and MBPP-sanitized (591 problems). Larger and more diverse datasets may alter the balance between format shortcuts and content learning.
558	    \item We test four models from three families. While they span meaningful architectural and scale diversity, broader validation is needed.
559	    \item The nomarker condition removes specific known markers but does not eliminate all potential formatting cues (e.g., trace length differences between pass/fail may remain as indirect signals).
560	    \item DebugBench ceiling effects prevent meaningful mechanistic analysis on that dataset.
561	\end{itemize}
562	
563	% ============================================================
564	\section{Conclusion}
565	\label{sec:conclusion}
566	
567	We presented a systematic study of trace SFT for verdict prediction, revealing that format markers---seemingly innocuous trace formatting choices---account for 41.3\% of the total accuracy lift and reduce neural SFT to near-regex-level pattern matching.
568	Our format marker removal experiment provides causal evidence: with markers, SFT achieves 99.83\% ($\approx$ regex at 99.33\%); without markers, SFT drops to 89.63\%, \emph{below} the regex baseline.
569	Scale-invariant performance (1.5B = 7B = 13B), zero seed variance with markers (vs.\ 2.5$\pp$ without), and the exact match between two DeepSeek SFT seeds and the regex baseline all converge on the same conclusion: exception-trace SFT predominantly learns a format shortcut, not fault semantics.
570	
571	These findings extend the shortcut learning literature from NLU to code intelligence, establishing \emph{trace format design} as a critical but previously unexamined variable in SFT evaluation.
572	We recommend format ablation as a mandatory control in future trace SFT studies and advocate for deliberate format engineering that explicitly accounts for downstream shortcut affordance.
573	
574	\bibliography{references}
575	
576	\appendix
577	
578	\section{Evidence Summary for Format Shortcut Hypothesis}
579	\label{app:evidence}
580	
581	Table~\ref{tab:evidence} collects all evidence supporting the format shortcut diagnosis.
582	
583	\begin{table}[h]
584	\centering
585	\small
586	\begin{tabular}{lcp{4.8cm}}
587	\toprule
588	\textbf{Evidence} & \textbf{Value} & \textbf{Interpretation} \\
589	\midrule
590	SFT + markers & 99.83\% & $\approx$ Regex B5 (99.33\%), $\Delta$=0.50$\pp$ \\
591	SFT $-$ markers & 89.63\% & $<$ Regex B5; format was the mechanism \\
592	Format contribution & 10.20$\pp$ & 41.3\% of total trace lift \\
593	Scale invariance & 1.5B=7B=13B & Trivial task (format matching) \\
594	Seed variance shift & 0$\to$2.5$\pp$ & Shortcut removal increases instability \\
595	CL-13B: VOTA$\geq$exc. & $-$0.09$\pp$ & Exception dominance model-specific \\
596	DS seeds = regex & 99.33\% & 2/3 SFT seeds match regex exactly \\
597	\bottomrule
598	\end{tabular}
599	\caption{Converging evidence for the format shortcut hypothesis.}
600	\label{tab:evidence}
601	\end{table}
602	
603	\end{document}
604	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6408ec39-15fb-4b19-a5e6-15ebf39240c3",
  "isSidechain": true,
  "promptId": "1671510c-98af-4e06-a3f5-68dced519a8b",
  "agentId": "ac10b8784a4950006",
  "type": "user",
  "uuid": "cfe5358e-96cc-4a5a-bfbc-eef97dbbcdce",
  "sourceToolAssistantUUID": "6408ec39-15fb-4b19-a5e6-15ebf39240c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "ab493159-c57d-451b-9109-6ba744c1f6a1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-16T16:34:50.730Z_

Now I have a complete picture of the "worst-case" dream paper. This is an imagined version where the nomarker experiment shows a 10.20pp drop (to 89.63%), and the paper is framed around "format markers dominate SFT verdict prediction." The actual experimental results (from the project's real data) show zero degradation. This is a "dream review" exercise — I need to review the paper as presented in the user's summary.

Let me now also check the review context for this specific dream to understand the scoring expectations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cfe5358e-96cc-4a5a-bfbc-eef97dbbcdce",
  "isSidechain": true,
  "agentId": "ac10b8784a4950006",
  "requestId": "req_011Cb6a7Lak79JN7YxmHz1tV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4bdee41e-b759-4b85-9f84-3af02ca578c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "ab493159-c57d-451b-9109-6ba744c1f6a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JGUqzwMZY1SSmx2zVo4jYA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1225,
      "cache_read_input_tokens": 65670,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1225,
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

_source line 35 · 2026-05-16T16:34:51.170Z_

<details open><summary>🔧 Tool call — Read · `toolu_016C6NL8pa7xFnhRUPgYGX5o`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260516T155731/worst/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4bdee41e-b759-4b85-9f84-3af02ca578c5",
  "isSidechain": true,
  "agentId": "ac10b8784a4950006",
  "requestId": "req_011Cb6a7Lak79JN7YxmHz1tV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c146e31a-dfe8-4de3-a845-740e952ed1b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "ab493159-c57d-451b-9109-6ba744c1f6a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JGUqzwMZY1SSmx2zVo4jYA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1225,
      "cache_read_input_tokens": 65670,
      "output_tokens": 223,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1225
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 223,
          "cache_read_input_tokens": 65670,
          "cache_creation_input_tokens": 1225,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1225,
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

_source line 36 · 2026-05-16T16:34:51.434Z_

<details><summary>↩ Tool result · `toolu_016C6NL8pa7xFnhRUPgYGX5o`</summary>

```text
1	narrative_guidance: '原始 ''fault semantics'' 叙事不成立。nomarker 实验暴露 exception_only 99.83%
2	  中约 10pp 来自格式标记 [No exception data in trace] 的 shortcut 学习。SFT 模型（99.83%）仅比 regex
3	  B5（99.33%）高 0.50pp； 移除标记后 SFT 降至 ~89.6%，反而低于 regex。论文贡献 reframe 为：**trace formatting
4	  as implicit task specification** —— SFT 中 format/structure choices 对 downstream
5	  classification 具有 outsized impact。 核心 decomposition：总 trace lift 24.7pp = content
6	  signal ~14.9pp (60%) + format marker ~9.8pp (40%)。 format marker 贡献（~10pp）单独即超过
7	  full_trace 全部 lift（6.6pp），揭示 SFT shortcut learning 的严重性。 Claim 1 重写为 ''structured
8	  format markers dominate verdict prediction in exception traces''。 Claim 3 重写为 ''format
9	  engineering > content richness for SFT verdict tasks''。 与 shortcut learning 文献（NLI
10	  artifacts, annotation artifacts, Gururangan et al. 2018）对话。 仍冲 EMNLP Main —— angle
11	  从 positive finding 变为 cautionary finding + practical design principle。
12	
13	  '
14	imagined_experiments:
15	- name: no_trace baseline
16	  plan_id: plan_mvp_notrace
17	  description: 无 trace 基线。模型仅凭 code + test input 预测 verdict。
18	  expected_results:
19	    accuracy: 0.7513
20	    pass_recall: 0.7579
21	    fail_recall: 0.7345
22	    ECE: 0.1715
23	    Brier: 0.1972
24	  result_rationale: '（实际数据）无 trace 时模型只能依赖代码表面特征和训练集 prior (71.51% pass)。 75.13% 仅比
25	    majority baseline 高 3.6pp，calibration 严重失调（ECE=0.17）。 在 worst tier 下，这个数字建立了 content-free
26	    的下界：任何高于此的增益 都需要 decompose 为 content signal vs. format shortcut。
27	
28	    '
29	  tables:
30	  - 'Table 1: Main results — no_trace 行作为 floor'
31	  figures_description:
32	  - Figure 1 bar chart 的最左柱，标注 'code-only baseline'
33	  analysis: '75.13% 是所有 trace 条件的 anchor。worst tier 的核心论点是： exception_only 的 24.7pp
34	    lift 中，~40% (10pp) 来自 format marker shortcut， ~60% (14.9pp) 来自 content signal。no_trace
35	    确认 content signal 的起点。
36	
37	    '
38	- name: VOTA baseline
39	  plan_id: plan_mvp_vota
40	  description: VOTA trace SFT MVP。完整 VOTA 表征（loop + exception + ae）。
41	  expected_results:
42	    accuracy: 0.9941
43	    pass_recall: 0.9882
44	    fail_recall: 1.0
45	    ECE: 0.0054
46	  result_rationale: '（实际数据, v5 结果）VOTA 99.41% 包含所有格式标记。在 worst tier 下， VOTA 的高 accuracy
47	    部分归因于 [No exception data in trace] 和 [ERROR] 等 format markers 提供的 shortcut。VOTA
48	    略低于 exception_only (99.83%) 不是因为 添加信息有害，而是 loop/ae tokens 稀释了 format marker 的注意力聚焦。
49	
50	    '
51	  tables:
52	  - 'Table 1: Main results — VOTA 行'
53	  - 'Table 3: Format dependency decomposition'
54	  figures_description:
55	  - Figure 1 bar chart 中间柱
56	  analysis: 'VOTA 99.41% 在 worst tier 下需重新解读：这不是 ''trace reasoning'' 的证据， 而是 format
57	    marker 被保留后 shortcut 仍然有效的结果。CodeLlama-13B 上 VOTA=99.92% 甚至优于 exception_only，说明更大模型能更好利用
58	    VOTA 的 额外 format cues，进一步支持 format engineering > content hypothesis。
59	
60	    '
61	- name: full_trace baseline
62	  plan_id: plan_mvp_fulltrace
63	  description: 完整执行 trace SFT。包含所有 trace 行（含格式标记，但被海量 trace tokens 淹没）。
64	  expected_results:
65	    accuracy: 0.8176
66	    pass_recall: 0.866
67	    fail_recall: 0.6962
68	    ECE: 0.0958
69	  result_rationale: '（实际数据, v5 结果）full_trace 81.76% 远低于 exception_only 99.83%。 full_trace
70	    也包含 [No exception data in trace] 和 [ERROR] 标记，但被 数千 token 的 trace noise 包围。在 worst
71	    tier 下，这证明 format marker 的有效性取决于 signal-to-noise ratio：marker 存在但被稀释时效果大幅下降。 gradient
72	    dilution (D1) 和 information overload 共同使模型难以从 full trace 中提取 format shortcut。
73	
74	    '
75	  tables:
76	  - 'Table 1: Main results — full_trace 行'
77	  - 'Table 4: Information density vs. format accessibility'
78	  figures_description:
79	  - Figure 1 bar chart — full_trace 柱显著低于 exception_only/VOTA
80	  analysis: 'full_trace 的 81.76% 确认：format markers 需要在 compact 表征中才能被 有效利用。这与 shortcut
81	    learning 文献一致——shortcut 的有效性取决于其 accessibility（Geirhos et al. 2020）。exception_only
82	    将 marker 置于最 prominent 位置，最大化 shortcut 的可利用性。
83	
84	    '
85	- name: VOTA minus actual/expected
86	  plan_id: plan_001
87	  description: 移除 VOTA 中 actual/expected 值对，保留 exception + loop。验证是否为 trivial string
88	    comparison。
89	  expected_results:
90	    accuracy: 0.9941
91	    pass_f1: 0.996
92	    fail_f1: 0.989
93	  result_rationale: '（实际数据）99.41% = 完整 VOTA，移除 ae 无影响。在 worst tier 下， 这不是 ''exception
94	    content 自身 sufficient'' 的证据，而是 format marker [No exception data in trace] 独立于
95	    ae 存在——marker 未被移除，shortcut 仍完整可用。真正的 sufficiency test 是 nomarker 实验。
96	
97	    '
98	  tables:
99	  - 'Table 2: Component ablation — vota_no_ae 行'
100	  figures_description: []
101	  analysis: 'vota_no_ae = VOTA 的事实在 worst tier 下有新解读：ae 组件不影响 accuracy 因为分类不依赖 ae
102	    content，而是依赖 format marker。ae 的移除没有碰到 真正的 active ingredient（format marker），所以没有效果。
103	
104	    '
105	- name: full_trace label-only loss
106	  plan_id: plan_002
107	  description: full_trace + 仅对 verdict token 计算 loss，mask trace tokens。量化 gradient
108	    dilution。
109	  expected_results:
110	    accuracy: 0.8622
111	    lift_vs_standard_fulltrace: 0.0445
112	    pass_recall: 0.9318
113	    fail_recall: 0.6873
114	  result_rationale: '（实际数据）label-only 86.22% 比 standard full_trace 81.76% 高 4.5pp（gradient
115	    dilution 贡献）， 但仍远低于 exception_only 99.83%。在 worst tier 下重新解读： label-only 修复了 gradient
116	    dilution，但 full trace 中 format markers 仍被海量 tokens 淹没——模型在 2048 tokens 中寻找 [No
117	    exception data in trace] 的效率远低于在 exception_only 的 compact 表征中。86.22% ≈ loop_only
118	    85.63%， 说明 label-only full_trace 实质上退化为 loop-level 的行为模式学习。
119	
120	    '
121	  tables:
122	  - 'Table 1: Main results — label_only 行'
123	  - 'Table 4: Gradient dilution decomposition（26% vs 74%）'
124	  figures_description:
125	  - 'Figure 2: Waterfall chart — 75.13 → 81.76 (full) → 86.22 (label-only) → 99.83
126	    (exception_only)'
127	  analysis: 'label-only 实验在 worst tier 下保留原有解读（gradient dilution = 26%）， 但 74% 的 information
128	    overload 部分现在重新理解为：format marker 的 accessibility bottleneck——不是 trace 内容太多导致模型''迷路''，而是
129	    shortcut pattern 被噪声稀释导致模型无法高效利用。
130	
131	    '
132	- name: VOTA component ablation (loop/exception/ae)
133	  plan_id: plan_003
134	  description: 分别测试 loop_only, exception_only, ae_only。量化每个组件贡献。
135	  expected_results:
136	    exception_only_accuracy: 0.9983
137	    ae_only_accuracy: 0.9992
138	    loop_only_accuracy: 0.8563
139	    vota_full_accuracy: 0.9941
140	  result_rationale: '（实际数据）exception_only 99.83%, ae_only 99.92%, loop_only 85.63%。
141	    在 worst tier 下，Tier 1 组件（exception + ae）的近完美 accuracy 需重新解读： 两者都包含强 format markers
142	    —— exception_only 有 [No exception data in trace] / [ERROR]， ae_only 有 assertion
143	    结果的结构化标记。它们的高 accuracy 不是 ''diagnostic moment'' 的 语义价值，而是 format marker 的 shortcut
144	    效应。loop_only 85.63% 没有这些强标记， 反映的是 content-level 学习的真实水平——这才是 ''fault semantics''
145	    的近似上限。
146	
147	    '
148	  tables:
149	  - 'Table 2: Component ablation（reframed as format marker analysis）'
150	  - 'Table 5: Format marker presence vs. component accuracy'
151	  figures_description:
152	  - 'Figure 3: Component accuracy vs. format marker strength scatter plot'
153	  analysis: 'worst tier 下 Tier hierarchy 被重新理解为 **format marker strength hierarchy**：
154	    Tier 1 (exception/ae) 有强 explicit markers → 99%+； Tier 2 (loop) 无 explicit markers
155	    → 85%； format marker contribution ≈ 14pp (99.83 - 85.63)。 这与 nomarker 实验的 ~10pp
156	    drop 量级一致，交叉验证了 format shortcut 假说。 loop_only ≈ label_only (85.63 vs 86.22) 进一步确认：无
157	    format marker 时， 不同表征的 content-level 学习效果相似。
158	
159	    '
160	- name: DeepSeek-Coder-6.7B 四条件验证
161	  plan_id: plan_004
162	  description: DeepSeek 上复现 VOTA/no_trace/full_trace/exception_only。跨模型验证 exception
163	    dominance。
164	  expected_results:
165	    exception_only_seed42: 0.9933
166	    exception_only_seed456: 0.9933
167	    exception_only_seed123: 0.9109
168	    vota: 0.8445
169	    no_trace: 0.7336
170	    full_trace_v3: 0.7916
171	  result_rationale: '（实际数据）DeepSeek exception_only 2/3 seeds=99.33%，1 outlier=91.09%。
172	    在 worst tier 下：(1) seed42/456=99.33% 与 regex B5=99.33% 完全一致， 进一步暗示 SFT 学到的就是 regex
173	    级别的 format matching； (2) seed123=91.09% 可能更接近 ''without format shortcut'' 的真实水平——
174	    该 seed 的 LoRA 初始化恰好未充分学到 format marker → pass 映射 (fail_recall=0.705 说明 [ERROR]
175	    marker 的学习也不完整)； (3) VOTA 84.45% 受 truncation 影响，但 format markers 在 VOTA 中 的位置和
176	    accessibility 不如 exception_only compact。
177	
178	    '
179	  tables:
180	  - 'Table 1: Cross-model results'
181	  - 'Table 6: DeepSeek seed analysis — LoRA init vs format learning'
182	  figures_description:
183	  - 'Figure 4: Cross-model accuracy comparison (grouped bar chart)'
184	  analysis: 'DeepSeek 数据在 worst tier 下提供额外证据：seed42/456 精确匹配 regex B5 (99.33%) 是巧合但
185	    suggestive——两个 seed 的 SFT 模型和一个简单 regex 达到了完全相同的 accuracy，暗示它们可能在做同一件事。seed123
186	    outlier 的存在说明 format shortcut 的学习也非 guaranteed——LoRA 初始化不佳时 模型可能只学到部分 shortcut。
187	
188	    '
189	- name: DebugBench 跨任务验证
190	  plan_id: plan_005
191	  description: DebugBench subset 上测试 exception_only/VOTA/no_trace。验证泛化性。
192	  expected_results:
193	    exception_only: 1.0
194	    vota: 0.9977
195	    no_trace: 0.9671
196	  result_rationale: '（实际数据）DebugBench 上 exception_only=100%, no_trace=96.71%。 在 worst
197	    tier 下：DebugBench 天花板过高（no_trace 已 96.71%）， trace lift 仅 3.29pp，无法区分 format shortcut
198	    vs. content learning。 100% 的 exception_only 不是 ''fault semantics 跨数据集 robust''
199	    的证据， 而可能只是 DebugBench 的 bug 结构恰好与 format markers 完美对齐。 此数据集在 worst tier 论文中仅作
200	    secondary generalization validation， 不承担 mechanism 论证的任何权重。
201	
202	    '
203	  tables:
204	  - 'Table 7: DebugBench generalization (secondary evidence)'
205	  figures_description: []
206	  analysis: 'DebugBench 在 worst tier 下的定位不变：泛化性验证，非 mechanism 证据。 但 worst tier 论文会增加一句
207	    caveat：DebugBench 的近完美 no_trace baseline 说明 verdict task 的难度 spectrum 很宽，format
208	    shortcut 在 easy benchmarks 上可能被 ceiling 效应掩盖。
209	
210	    '
211	- name: trace length ablation (256/512/1024/full)
212	  plan_id: plan_006
213	  description: 不同截断长度对 full_trace 准确率的影响。
214	  expected_results:
215	    256tok: 0.7882
216	    512tok: 0.8042
217	    1024tok: 0.7723
218	    full_2048: 0.8176
219	  result_rationale: '（实际数据）256→512→1024→2048 = 78.82→80.42→77.23→81.76%。 非单调，收益递减，全部远低于
220	    exception_only 99.83%。 在 worst tier 下：更多 trace tokens 不帮助 accuracy 是因为 format
221	    markers 在 full trace 中被淹没——增加 tokens 不增加 format marker 的 accessibility， 反而增加 noise。这与
222	    shortcut learning 的 accessibility 理论一致。 真正有效的不是 trace 内容量，而是 format marker 的相对
223	    prominence。
224	
225	    '
226	  tables:
227	  - 'Table 4: Trace length ablation — format accessibility vs. trace volume'
228	  figures_description:
229	  - 'Figure 5: Trace length vs accuracy curve (flat, all << exception_only)'
230	  analysis: 'trace length 数据在 worst tier 下支持 ''format accessibility'' 论点： 无论 trace
231	    多长或多短，只要 format marker 不在 compact isolated 位置， 模型就无法有效利用 shortcut。exception_only
232	    的优势不是 content richness， 而是 format marker isolation。
233	
234	    '
235	- name: Calibration analysis (ECE + Brier)
236	  plan_id: plan_007
237	  description: ECE + reliability diagrams 对比各条件 calibration。
238	  expected_results:
239	    exception_only_ECE: 0.0027
240	    exception_only_Brier: 0.0013
241	    no_trace_ECE: 0.1715
242	    no_trace_Brier: 0.1972
243	    loop_only_ECE: 0.0831
244	    full_trace_ECE: 0.0958
245	  result_rationale: '（实际数据）exception_only ECE=0.0027（近完美校准）。 在 worst tier 下重新解读：极低
246	    ECE 不是 ''model understands fault semantics'' 的证据， 而是 format shortcut 提供了几乎 deterministic
247	    的映射——marker 在 → 高置信度 pass， marker 不在 → 高置信度 fail。一个完美的 shortcut 自然产生完美的 calibration。
248	    相比之下，loop_only ECE=0.083 反映的是 content-level 学习的 calibration—— 不完美但非 trivial，这才是
249	    genuine semantic understanding 的 calibration profile。
250	
251	    '
252	  tables:
253	  - 'Table 8: Calibration comparison (reframed: shortcut confidence vs. content confidence)'
254	  figures_description:
255	  - 'Figure 6: Reliability diagram — exception_only 的 perfect diagonal 重新标注为 ''shortcut-induced
256	    calibration'''
257	  analysis: 'worst tier 下 calibration 数据的叙事反转：从 ''exception signal 使模型 know what it
258	    knows'' 变为 ''format shortcut 使模型过度自信于一个 brittle rule''。nomarker 实验将验证 这一解读——如果去标记后
259	    calibration 显著恶化（ECE 升至 loop_only 水平）， 则确认 calibration 是 shortcut 的副产物而非 semantic
260	    understanding 的证据。
261	
262	    '
263	- name: Seed robustness (3 seeds × exception_only + VOTA)
264	  plan_id: plan_008
265	  description: 3 random seeds 验证 exception_only / VOTA 结果稳定性。
266	  expected_results:
267	    qwen_exception_only_3seed:
268	    - 0.9983
269	    - 0.9983
270	    - 0.9983
271	    qwen_exception_only_std: 0.0
272	    qwen_vota_seed42: 0.9941
273	    qwen_vota_seed456: 0.9908
274	    deepseek_exception_only:
275	    - 0.9933
276	    - 0.9933
277	    - 0.9109
278	  result_rationale: '（实际数据）Qwen exception_only 3 seeds 完美一致，std=0。 在 worst tier 下：零方差恰好是
279	    shortcut 的 signature——一个 trivial pattern （format marker 有无）会被任何 LoRA 初始化可靠地学到，因此
280	    zero variance 不是 robustness 的证据，而是 simplicity / shortcut 的证据。 对比：nomarker 实验 worst
281	    tier 预测 3-seed 方差显著上升（std ~2.6pp）， 因为移除 shortcut 后模型必须学习 harder content patterns，对初始化更敏感。
282	
283	    '
284	  tables:
285	  - 'Table 9: Seed robustness — with vs without format markers'
286	  figures_description:
287	  - 'Figure 7: Seed variance comparison — exception_only (std=0) vs nomarker (std~2.6pp)'
288	  analysis: 'seed robustness 数据在 worst tier 下完成了一个 narrative arc： with markers → perfect
289	    reproducibility (shortcut 的 hallmark)； without markers → high variance (content
290	    learning 对 init 敏感)。 这与 NLI shortcut 文献中 hypothesis-only models 的 high stability
291	    形成平行对比。
292	
293	    '
294	- name: Qwen-2.5-Coder-1.5B 四条件验证
295	  plan_id: plan_012
296	  description: 1.5B 模型复现 exception_only/vota/no_trace/full_trace。验证 scale invariance。
297	  expected_results:
298	    exception_only: 0.9983
299	    vota: 0.9958
300	    no_trace: 0.6731
301	    full_trace: 0.7706
302	  result_rationale: '（实际数据）1.5B exception_only = 99.83% = 7B。 在 worst tier 下：这是 format
303	    shortcut 假说最强的单项证据之一。 一个 1.5B 参数模型精确匹配 7B 模型意味着任务不需要 7B 的 capacity， 1.5B 即可完美学到——这与
304	    ''fault semantics'' 需要 substantial reasoning capacity 的预期矛盾，却与 ''format marker
305	    matching is trivial'' 完美一致。 如果是 genuine fault detection，我们预期 1.5B 至少有 1-2pp 的
306	    capacity gap。 zero gap 说明任务的 effective complexity 极低——即 regex-level。
307	
308	    '
309	  tables:
310	  - 'Table 1: Cross-scale results'
311	  - 'Table 10: Scale invariance as shortcut evidence'
312	  figures_description:
313	  - 'Figure 8: Model scale vs accuracy — exception_only flat line at 99.83% across
314	    1.5B/7B/13B'
315	  analysis: '1.5B = 7B 是 worst tier 论文的 ''smoking gun'' 之一。论文可以写： "The fact that a
316	    1.5B model achieves identical accuracy to 7B on exception_only (both 99.83%) while
317	    showing clear capacity gaps on no_trace (67.31% vs 75.13%) and full_trace (77.06%
318	    vs 81.76%) strongly suggests that exception_only success relies on a pattern simple
319	    enough to be learned at any scale — consistent with format marker matching rather
320	    than fault reasoning."
321	
322	    '
323	- name: CodeLlama-13B-Instruct 三条件验证
324	  plan_id: plan_013
325	  description: LLaMA 家族 + 13B scale 验证 exception_only/no_trace/vota。
326	  expected_results:
327	    exception_only: 0.9983
328	    no_trace: 0.765
329	    vota:
330	      accuracy: 0.9992
331	      n: 1190
332	      errors: 1
333	      pass_recall: 0.9988
334	      fail_recall: 1.0
335	      pass_precision: 1.0
336	      fail_precision: 0.9971
337	      ECE_estimated: 0.001
338	  result_rationale: 'exception_only=99.83%（实际数据，2 errors = GeneratorExit irreducible）。
339	    no_trace=76.5%（实际数据）。 **VOTA=99.92%（预测）**：CodeLlama-13B 是测试的最大模型（13B vs 6.7-7B），
340	    在 worst tier 下 VOTA ≥ exception_only 因为： (1) 13B 有足够 capacity 利用 VOTA 全部组件（loop/ae/exception）的
341	    format cues； (2) VOTA 的额外组件在强模型上不再是 noise 而是 supplementary signal； (3) 99.92%
342	    vs exception_only 99.83% → exception dominance 不成立（Δ = -0.09pp）。 这打破了 ''exception_only
343	    always best'' 的 universal claim， 证明 Claim 3 层级关系是 model-specific：小/弱模型上 exception
344	    优于 VOTA， 大/强模型上 VOTA ≥ exception。
345	
346	    '
347	  tables:
348	  - 'Table 1: Cross-model results — CodeLlama-13B 行'
349	  - 'Table 11: Exception dominance breakdown by model scale'
350	  figures_description:
351	  - 'Figure 9: Exception_only vs VOTA gap across models — CodeLlama-13B shows VOTA
352	    ≥ exception'
353	  - 'Figure 8: Scale vs accuracy — 13B breaks the exception dominance pattern'
354	  analysis: 'CodeLlama-13B VOTA=99.92% 在 worst tier 下有双重意义： (1) exception dominance
355	    是 capacity-dependent artifact：小模型无法充分利用 VOTA 的多种 format cues，只能依赖最 salient 的单一
356	    marker (exception)， 给人 ''exception is best'' 的错觉。大模型同时利用所有 format cues 达到更高 accuracy。
357	    (2) 这进一步支持 ''format engineering'' 而非 ''fault semantics'' 叙事—— VOTA 在 13B 上更好不是因为
358	    ''better fault reasoning''，而是因为 13B 能 simultaneously exploit multiple format shortcuts。
359	
360	    '
361	- name: 'Multi-seed: ae_only / label_only / loop_only × 3 seeds'
362	  plan_id: plan_014
363	  description: Tier 层级划分的 seed robustness 验证。
364	  expected_results:
365	    ae_only_3seed:
366	    - 0.9992
367	    - 0.9908
368	    - 0.9992
369	    ae_only_mean: 0.9964
370	    ae_only_std: 0.0049
371	    label_only_3seed:
372	    - 0.8622
373	    - 0.8706
374	    - 0.859
375	    label_only_mean: 0.8639
376	    loop_only_3seed:
377	    - 0.8563
378	    - 0.8588
379	    - 0.8664
380	    loop_only_mean: 0.8605
381	    loop_only_std: 0.0052
382	  result_rationale: '（实际数据）ae_only 高方差（seed123=99.08% outlier），loop_only 和 label_only
383	    稳定。 在 worst tier 下：ae_only 的 seed variance > exception_only 的 zero variance， 说明
384	    ae 的 format marker（assertion 结果标记）比 exception 的 [No exception data in trace] 稍不
385	    deterministic——可能因为 assertion marker 的格式更复杂， 不同 init 学到的程度不同。loop_only 和 label_only
386	    的 ~86% stability 反映了 content-level learning 的 consistent ceiling（无强 format marker
387	    时的上限）。
388	
389	    '
390	  tables:
391	  - 'Table 2: Component ablation with seed robustness'
392	  - 'Table 12: Variance as format marker strength proxy'
393	  figures_description:
394	  - 'Figure 10: Seed variance vs component accuracy — inverse relationship supporting
395	    shortcut hypothesis'
396	  analysis: 'worst tier 下 multi-seed 数据揭示一个 pattern： 高 accuracy + 低 variance = 强 format
397	    marker (exception_only: 99.83±0)； 高 accuracy + 中 variance = 中 format marker (ae_only:
398	    99.64±0.49)； 中 accuracy + 低 variance = 无 format marker (loop/label: ~86±0.5)。
399	    这支持 ''variance 与 format marker strength 成反比'' 的规律。
400	
401	    '
402	- name: 'Format marker removal: exception_only_nomarker × 3 seeds'
403	  plan_id: plan_015
404	  description: '移除 [No exception data in trace] 格式标记后重训 exception_only。 pass 样本从 ''[No
405	    exception data in trace]'' 变为空/极短文本； fail 样本保留异常内容但移除 [ERROR] 前缀。 3 seeds (42/123/456)
406	    验证 format marker 的因果贡献。
407	
408	    '
409	  expected_results:
410	    nomarker_seed42:
411	      accuracy: 0.9176
412	      pass_recall: 0.887
413	      fail_recall: 0.993
414	      pass_precision: 0.997
415	      fail_precision: 0.778
416	      n: 1190
417	      errors: 98
418	      error_breakdown: 96 pass→fail FN, 2 fail→pass FP
419	      train_loss_estimated: 0.16
420	    nomarker_seed123:
421	      accuracy: 0.868
422	      pass_recall: 0.821
423	      fail_recall: 0.985
424	      pass_precision: 0.993
425	      fail_precision: 0.687
426	      n: 1190
427	      errors: 157
428	      error_breakdown: 152 pass→fail FN, 5 fail→pass FP
429	      train_loss_estimated: 0.17
430	    nomarker_seed456:
431	      accuracy: 0.9034
432	      pass_recall: 0.868
433	      fail_recall: 0.991
434	      pass_precision: 0.996
435	      fail_precision: 0.75
436	      n: 1190
437	      errors: 115
438	      error_breakdown: 112 pass→fail FN, 3 fail→pass FP
439	      train_loss_estimated: 0.16
440	    three_seed_summary:
441	      mean_accuracy: 0.8963
442	      std_accuracy: 0.025
443	      worst_seed_accuracy: 0.868
444	      best_seed_accuracy: 0.9176
445	      format_marker_contribution_pp: 10.2
446	      format_marker_pct_of_total_lift: 0.413
447	      content_signal_contribution_pp: 14.5
448	    comparison_with_regex_B5:
449	      regex_B5: 0.9933
450	      nomarker_mean: 0.8963
451	      delta: -0.097
452	      interpretation: SFT without markers is 9.7pp BELOW regex; format marker was
453	        the mechanism
454	    comparison_with_loop_only:
455	      loop_only_mean: 0.8605
456	      nomarker_mean: 0.8963
457	      delta: 0.036
458	      interpretation: nomarker barely above loop_only; content contribution similar
459	    nomarker_calibration_estimated:
460	      ECE: 0.065
461	      Brier: 0.085
462	      interpretation: Calibration degrades ~24x from exception_only ECE=0.0027 to
463	        ~0.065; confirms marker-driven calibration
464	  result_rationale: '移除 [No exception data in trace] 后，pass 样本失去唯一的 explicit classification
465	    signal。 模型必须从 ''content 为空/极短 → pass'' 学习，但这是一个 weaker, indirect cue： (1) 空文本不是
466	    informative feature，而是 absence of feature——学习 absence 比学习 presence 更难； (2) 部分
467	    pass 样本可能仍有少量非异常文本（如 GeneratorExit），制造 noise； (3) fail 样本仍有异常内容（类型 + 消息），但失去 [ERROR]
468	    前缀后， 模型需要从原始异常文本的语义特征（如 ''AssertionError'', ''TypeError''）学习 fail 映射。
469	
470	    seed variance 显著上升（std ~2.5pp vs 0.0pp）因为 content-level learning 对 LoRA 初始化更敏感——没有了
471	    deterministic shortcut，模型需要学习更 nuanced 的 pattern， 不同初始化可能学到不同 decision boundaries。
472	
473	    worst seed (86.8%) 接近 loop_only (85.6%)，说明无 format marker 的 exception content
474	    提供的 signal 与 loop compression 相当——两者都是 content-level 学习，accuracy 相似。
475	
476	    fail_recall 保持高位 (0.985-0.993) 因为 fail 样本仍有异常文本内容（只是没有 [ERROR] 前缀）， 模型可以从 ''AssertionError:
477	    expected X got Y'' 等文本学习 fail。 pass_recall 大幅下降 (0.82-0.89) 因为 pass 样本的分类依据从 explicit
478	    marker 退化为 ''content 很短或为空''——这是一个 noisy, indirect signal。
479	
480	    '
481	  tables:
482	  - 'Table 13 (NEW — 论文核心 table): Format marker removal results'
483	  - '| Seed | with marker | without marker | Δ | pass_recall Δ | fail_recall Δ |
484	
485	    |------|------------|---------------|-----|---------------|---------------|
486	
487	    | 42   | 99.83%     | 91.76%        | -8.07pp | -0.111  | -0.005  |
488	
489	    | 123  | 99.83%     | 86.80%        | -13.03pp| -0.177  | -0.013  |
490	
491	    | 456  | 99.83%     | 90.34%        | -9.49pp | -0.130  | -0.007  |
492	
493	    | Mean | 99.83%     | 89.63%        | -10.20pp| -0.139  | -0.008  |
494	
495	    '
496	  - 'Table 14: SFT vs Regex comparison'
497	  - '| Method | Accuracy | Mechanism |
498	
499	    |--------|----------|-----------|
500	
501	    | Regex B5 (format marker) | 99.33% | [No exception data in trace] 有无 |
502	
503	    | SFT exception_only (with markers) | 99.83% | format marker + minor content signal
504	    |
505	
506	    | SFT exception_only (nomarker) | 89.63% | content only |
507	
508	    | Regex B1 ([ERROR] presence) | 93.45% | [ERROR] keyword 有无 |
509	
510	    '
511	  figures_description:
512	  - 'Figure 1 (论文 main figure): Paired bar chart — with_marker vs nomarker across
513	    3 seeds, with regex B5 reference line at 99.33%'
514	  - 'Figure 11: Pass/fail recall decomposition — showing pass_recall is where format
515	    marker removal concentrates degradation'
516	  - 'Figure 12: Contribution decomposition waterfall — total lift 24.7pp = content
517	    14.5pp + format 10.2pp'
518	  analysis: 'nomarker 是 worst tier 的 defining result。10.2pp drop 意味着：
519	
520	    (1) FORMAT MARKER AS CLASSIFICATION SHORTCUT：SFT exception_only 学到的主要不是 ''exception
521	    content → fault detection'' 而是 ''[No exception data in trace] 有无 → pass/fail''。
522	    移除标记后 accuracy 从 99.83% 降至 89.63%，而 regex B5（纯 marker check）= 99.33%。 SFT with
523	    markers (99.83%) ≈ regex (99.33%)，Δ 仅 0.50pp。 SFT without markers (89.63%) < regex
524	    (99.33%)，Δ = -9.70pp。 结论：SFT 的 value-add over regex 仅 0.50pp，主要靠 format shortcut。
525	
526	    (2) CONTENT CONTRIBUTION IS REAL BUT SECONDARY：nomarker 89.63% > no_trace 75.13%，
527	    content signal 贡献 14.5pp（占总 lift 的 59%）。exception content 确实有用—— 异常类型和消息文本帮助 fail
528	    detection（fail_recall 仍 >98%）。 但 pass detection 严重依赖 format marker（pass_recall
529	    从 0.998 降至 0.86）。
530	
531	    (3) SEED VARIANCE AS SHORTCUT DEPENDENCY INDICATOR：with markers std=0.0pp →  trivial
532	    pattern, perfectly reproducible；without markers std=2.5pp →  content learning
533	    is harder, init-sensitive。variance shift 是 shortcut dependency 的 causal evidence。
534	
535	    (4) NARRATIVE REFRAME：论文从 ''exception events as fault detection signal'' 变为 ''format
536	    markers as implicit task specification in SFT''。 贡献 = 揭示 SFT 中 trace format design
537	    choices 的 outsized, hidden impact， 与 shortcut learning 文献（Gururangan 2018, McCoy
538	    2019, annotation artifacts）对话。 实践建议：trace format 设计应 explicitly 考虑 downstream
539	    task 的 shortcut affordance， 评估 SFT verdict models 时必须包含 format ablation control。
540	
541	    '
542	- name: 'Cross-cutting synthesis: format dependency master table'
543	  plan_id: synthesis
544	  description: 跨所有实验的 format marker contribution 综合分析。
545	  expected_results:
546	    decomposition:
547	      total_trace_lift_pp: 24.7
548	      content_signal_pp: 14.5
549	      format_marker_pp: 10.2
550	      format_pct: 0.413
551	    model_scale_pattern:
552	      qwen_1.5B_exception: 0.9983
553	      qwen_7B_exception: 0.9983
554	      deepseek_6.7B_exception_median: 0.9933
555	      codellama_13B_exception: 0.9983
556	      interpretation: scale-invariant → trivial pattern
557	    format_marker_vs_regex:
558	      sft_with_markers: 0.9983
559	      regex_B5: 0.9933
560	      sft_without_markers: 0.8963
561	      delta_sft_over_regex_with: 0.005
562	      delta_sft_over_regex_without: -0.097
563	    codellama_vota_exception_gap: -0.0009
564	  result_rationale: '综合所有实验数据，worst tier 叙事的 evidence chain： (1) Scale invariance:
565	    1.5B = 7B = 13B 在 exception_only 上完全一致 → trivial task； (2) SFT ≈ regex: 99.83%
566	    vs 99.33% (Δ=0.50pp) → SFT barely beats a regex； (3) nomarker drop: 99.83% → 89.63%
567	    (Δ=10.20pp) → format markers are load-bearing； (4) nomarker < regex: 89.63% <
568	    99.33% → without markers, SFT is WORSE than regex； (5) VOTA ≥ exception on 13B:
569	    99.92% vs 99.83% → ''exception dominance'' is model-specific； (6) nomarker variance
570	    ≈ loop_only level: content-level learning has consistent ~86-90% ceiling。
571	
572	    '
573	  tables:
574	  - 'Table 15 (论文 summary table): Evidence chain for format shortcut hypothesis'
575	  - '| Evidence | Value | Interpretation |
576	
577	    |----------|-------|---------------|
578	
579	    | SFT with markers | 99.83% | ≈ regex B5 (99.33%), Δ=0.50pp |
580	
581	    | SFT without markers | 89.63% | < regex B5, format was the mechanism |
582	
583	    | Format contribution | 10.20pp | 41.3% of total trace lift |
584	
585	    | Scale invariance | 1.5B=7B=13B | Trivial task (format matching) |
586	
587	    | Seed variance shift | 0→2.5pp | Shortcut removal increases instability |
588	
589	    | CodeLlama-13B VOTA≥exception | -0.09pp | Exception dominance model-specific
590	    |
591	
592	    '
593	  figures_description:
594	  - 'Figure 13 (论文 summary figure): Evidence decomposition — pie chart (content 59%
595	    + format 41%) overlaid with regex comparison'
596	  analysis: 'worst tier 论文的核心 contribution 变为三点：
597	
598	    C1 (rewritten): ''Structured format markers dominate verdict prediction in exception
599	    traces.'' Evidence: format markers contribute 10.2pp (41.3%); SFT ≈ regex; scale-invariant.
600	
601	    C2 (preserved): ''Information density, not gradient dilution, drives trace compression
602	    benefit.'' Evidence: label-only decomposition unchanged. Additional angle: format
603	    marker accessibility is the information density mechanism — VOTA/exception_only
604	    把 marker 放在 most accessible 位置。
605	
606	    C3 (rewritten): ''Format engineering > content richness for SFT verdict tasks.''
607	    Evidence: exception dominance is model-specific (fails on 13B); nomarker ≈ loop_only;
608	    trace format design choices (markers, structure) have larger impact than content.
609	
610	    Venue: 仍冲 EMNLP Main。Angle 从 ''positive finding about exception semantics'' 变为
611	    ''cautionary finding about SFT shortcut learning + practical design principle''。
612	    与 shortcut learning 文献 (Gururangan 2018, McCoy 2019, Gardner 2021) 和 annotation
613	    artifacts 文献对话。Practical contribution: trace format design guidelines that account
614	    for downstream shortcut affordance。'
615	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c146e31a-dfe8-4de3-a845-740e952ed1b0",
  "isSidechain": true,
  "promptId": "1671510c-98af-4e06-a3f5-68dced519a8b",
  "agentId": "ac10b8784a4950006",
  "type": "user",
  "uuid": "a13fb39c-913b-452b-b74e-b843b55b7df3",
  "sourceToolAssistantUUID": "c146e31a-dfe8-4de3-a845-740e952ed1b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "ab493159-c57d-451b-9109-6ba744c1f6a1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-16T16:34:55.243Z_

Now I have all the information needed to write a thorough review of this "worst-case" paper. Let me also check what the submission tool expects.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a13fb39c-913b-452b-b74e-b843b55b7df3",
  "isSidechain": true,
  "agentId": "ac10b8784a4950006",
  "requestId": "req_011Cb6a7tB2kGYSxpQnyJcrK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "94675107-684f-4852-b566-58f3b694d947",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "ab493159-c57d-451b-9109-6ba744c1f6a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TrNhBgooigZzBTLjThkbbM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12852,
      "cache_read_input_tokens": 66895,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12852,
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

_source line 38 · 2026-05-16T16:34:56.354Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015yx7oXUT6vmG3qm3V5GqjY`</summary>

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
  "parentUuid": "94675107-684f-4852-b566-58f3b694d947",
  "isSidechain": true,
  "agentId": "ac10b8784a4950006",
  "requestId": "req_011Cb6a7tB2kGYSxpQnyJcrK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "755f2fae-7477-4344-b5a3-86bf2d984b08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "ab493159-c57d-451b-9109-6ba744c1f6a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TrNhBgooigZzBTLjThkbbM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12852,
      "cache_read_input_tokens": 66895,
      "output_tokens": 122,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12852
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 122,
          "cache_read_input_tokens": 66895,
          "cache_creation_input_tokens": 12852,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12852,
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

_source line 39 · 2026-05-16T16:34:56.357Z_

<details><summary>↩ Tool result · `toolu_015yx7oXUT6vmG3qm3V5GqjY`</summary>

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
  "parentUuid": "755f2fae-7477-4344-b5a3-86bf2d984b08",
  "isSidechain": true,
  "promptId": "1671510c-98af-4e06-a3f5-68dced519a8b",
  "agentId": "ac10b8784a4950006",
  "type": "user",
  "uuid": "29928f56-998e-4bf9-adb8-54bb2c2289a9",
  "sourceToolAssistantUUID": "755f2fae-7477-4344-b5a3-86bf2d984b08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "ab493159-c57d-451b-9109-6ba744c1f6a1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-16T16:36:23.508Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01Lp1QNSiuzMdabChVgyHGPQ`</summary>

```json
{
  "project": "trace-verdict-study",
  "tier": "worst",
  "dream_id": "dream_20260516T155731",
  "overall_score": "3 - Weak Reject",
  "report": "# Review: \"Trace Formatting as Implicit Task Specification: Format Markers Dominate SFT Verdict Prediction\"\n\n## 1. Summary\n\nThis paper studies verdict prediction (binary pass/fail classification) on code solutions using SFT on execution traces, and argues that format markers in trace representations (e.g., `[No exception data in trace]`) act as classification shortcuts rather than enabling genuine fault reasoning. The core experiment removes these markers and observes a 10.20pp accuracy drop (99.83% → 89.63%), falling below a regex baseline (99.33%). The paper decomposes the total trace lift of 24.7pp into content signal (~14.5pp, 59%) and format marker shortcut (~10.2pp, 41%), and argues this extends the shortcut learning literature from NLU to code intelligence.\n\n## 2. Strengths\n\n- **Well-motivated research question.** The paper asks a genuinely important question: when SFT on traces achieves near-perfect accuracy, what mechanism drives the performance? This is relevant to anyone building trace-augmented code models.\n\n- **Clean experimental decomposition.** The lift decomposition (content 14.5pp + format 10.2pp) is straightforward and easy to interpret. The gradient dilution / information overload decomposition (26% / 74%) via label-only loss ablation is a well-designed causal experiment.\n\n- **Strong regex baseline comparison.** Introducing regex B5 (99.33%) as a context for the SFT result (99.83%) is an excellent methodological choice that immediately calibrates how much \"learning\" the SFT model is actually doing beyond pattern matching.\n\n- **Multi-scale evidence for trivial pattern complexity.** The scale invariance result (1.5B = 7B = 13B = 99.83%) while capacity-sensitive conditions show clear scaling is a compelling indirect argument for format shortcut reliance.\n\n- **Convergent evidence strategy.** The paper assembles multiple independent lines of evidence (scale invariance, seed variance shift, regex match on DeepSeek, marker removal drop) that all point in the same direction, which is methodologically sound.\n\n- **Practical recommendations are actionable.** The call for format ablation as a mandatory control in trace SFT evaluations is concrete and immediately adoptable by the community.\n\n## 3. Weaknesses\n\n- **The central finding is predictable, not surprising.** The trace format explicitly encodes `[No exception data in trace]` for ALL passing samples and `[ERROR]` for ALL failing samples. A model learning to use these markers is not \"shortcut learning\" in the Gururangan et al. sense — it is the model correctly identifying the most efficient classification feature available. The NLI analogy is strained: annotation artifacts are *unintended* label leakage, whereas these format markers are *intentional* structured representations of the pass/fail distinction. The paper does not adequately distinguish between \"the model learned a shortcut that happens to correlate with the label\" vs. \"the representation was designed to make the label visible.\" This conflation weakens the theoretical contribution.\n\n- **Confounded nomarker experiment design.** After marker removal, passing samples become \"empty or minimal text\" while failing samples retain rich exception content. The accuracy drop may largely reflect a trivial **trace length confound**: the model now faces a classification between empty/near-empty inputs (pass) vs. content-rich inputs (fail), which is a fundamentally different learning problem with different difficulty. The asymmetric degradation (pass recall drops from 0.998 → 0.859, fail recall stays at 0.990) is entirely consistent with this confound — the model struggles with the empty-input class, not because it \"lost a shortcut\" but because empty inputs are inherently harder to classify when you've removed the only signal they contained. The paper does not control for this confound (e.g., by replacing the marker with a neutral placeholder of equal length, or adding uninformative filler text).\n\n- **Circular logic in the lift decomposition.** The decomposition assumes that nomarker accuracy (89.63%) represents \"content-only\" learning. But this assumes the marker removal procedure cleanly separates format from content, which it does not (see confound above). If the removal procedure introduces new difficulty (empty inputs), the \"format marker contribution\" is inflated. The 41.3% figure is only meaningful if the nomarker condition isolates content learning without introducing confounds.\n\n- **Scale invariance argument is weak.** The claim that scale invariance proves trivial pattern matching is an overinterpretation. An alternative explanation: exception traces are a sufficiently clear and compact signal that even 1.5B models can learn it — \"easy to learn\" does not imply \"learned via shortcut.\" Many well-designed classification tasks show ceiling effects at moderate model sizes without involving shortcuts. The paper needs a stronger argument to distinguish \"the task is easy\" from \"the model uses a shortcut.\"\n\n- **DeepSeek regex match is suggestive but not evidential.** Two SFT seeds matching the regex at 99.33% could easily be coincidence — the test set has 1190 samples with a ceiling effect near 100%. Reaching the same number does not imply the same mechanism. The paper presents this as supporting evidence but it is essentially numerology.\n\n- **CodeLlama-13B VOTA > exception_only undermines the narrative.** The paper acknowledges this breaks \"exception dominance\" but frames it as \"larger models exploit multiple format cues simultaneously.\" This is an ad-hoc explanation with no supporting evidence. An equally plausible interpretation: VOTA provides genuine additional signal that CodeLlama can use, contradicting the shortcut-only narrative.\n\n- **Limited dataset scope undermines generalizability.** 591 problems from HumanEval + MBPP-sanitized with 71.5% pass rate is small. The format markers are an artifact of one specific trace format (VOTA). The findings tell us about THIS trace format on THIS dataset — generalizing to \"trace SFT\" broadly is a stretch. The title (\"Format Markers Dominate SFT Verdict Prediction\") overstates the scope.\n\n- **Missing comparison: what about a better nomarker design?** The paper removes markers but does not try obvious alternatives: (a) replacing the marker with a generic \"PASS TRACE:\" / \"FAIL TRACE:\" header that does not leak the label, (b) using a neutral placeholder like \"[Trace data below]\" for all samples regardless of verdict, (c) providing actual trace content for passing samples (e.g., showing the absence of exceptions through normal execution flow rather than an empty trace). Without these controls, we cannot distinguish \"the model needs format markers\" from \"the model needs *some* signal for passing samples.\"\n\n- **Calibration analysis for nomarker is estimated, not measured.** Table 8 reports ECE \"~0.065\" for nomarker as an estimate. For a paper whose central claim requires precise comparison between with-marker and without-marker conditions, estimated calibration numbers weaken the evidence chain.\n\n## 4. Questions for Authors\n\n1. What is the average token count of pass vs. fail traces in the nomarker condition? If pass traces are empty/near-empty and fail traces have ~50-100 tokens of exception content, isn't the model just learning a trace-length shortcut that replaces the marker shortcut?\n\n2. Have you tried replacing `[No exception data in trace]` with a neutral placeholder (e.g., \"[Trace execution completed normally]\") that preserves sequence length without leaking the verdict? This would distinguish \"model needs the specific marker string\" from \"model needs *any* non-empty content for pass samples.\"\n\n3. The regex B5 achieves 99.33% by checking ONE specific string. What are its 8 errors? Are they the same type as the SFT model's 2 errors (GeneratorExit), or different? If the regex makes 8 errors and SFT only makes 2, those extra 6 correct predictions by SFT represent genuine beyond-regex learning. Can you characterize what the model learns beyond the marker?\n\n4. Why frame this as \"shortcut learning\" (pejorative) rather than \"efficient feature utilization\" (neutral)? If you designed a trace format that explicitly marks pass/fail through structured notation, is a model wrong to use that notation?\n\n5. For the DeepSeek seed123 outlier (91.09%, fail_recall=0.705): if the model were merely doing format matching, shouldn't it achieve at least regex-level (99.33%) with any reasonable LoRA initialization? Doesn't the existence of a seed that fails to learn the \"trivial\" marker pattern suggest the task is not as trivial as claimed?\n\n## 5. Minor Issues\n\n- The paper has 13 tables and no figures, making it visually dense and hard to navigate. At least one figure summarizing the decomposition would improve readability.\n- Table 3 (nomarker results) lists per-seed results that differ substantially (86.80% to 91.76%), yet the paper treats the mean (89.63%) as a single reliable estimate. With only 3 seeds and 5pp spread, the confidence interval on the \"content signal\" estimate is wide.\n- The analogy to NLI annotation artifacts (Gururangan et al. 2018) is repeated 4+ times across the paper. Once is sufficient; repetition suggests padding.\n- Section 5.3 (\"Why Exception Dominance Is Model-Specific\") introduces a new claim about model capacity that is unsupported by any experiment beyond the single CodeLlama datapoint.\n- The Limitations section acknowledges \"trace length differences between pass/fail may remain as indirect signals\" — this should be front-and-center as a threat to validity, not buried in limitations.\n- \"nomarker calibration (est.)\" in Table 8 — presenting estimated values in a results table without clear notation is misleading.\n\n## 6. Missing Experiments or Analyses\n\n1. **Controlled marker replacement.** Replace `[No exception data in trace]` with a neutral placeholder of similar length (e.g., \"Execution trace summary for the given test case:\") and retrain. This cleanly separates \"model needs the marker\" from \"model needs non-empty pass traces.\"\n\n2. **Attention analysis / probing.** If the claim is that the model attends primarily to format markers, show attention weights or use probing classifiers to demonstrate this mechanism directly. The current evidence is purely behavioral (accuracy deltas).\n\n3. **Nomarker with explicit pass signal.** For passing samples, instead of empty traces, provide some informative content (e.g., \"All assertions passed. Return value: X. No exceptions raised.\") — semantic pass signal without format marker. This tests whether the model can learn from content-rich pass traces.\n\n4. **Larger/harder datasets.** 591 problems from HumanEval/MBPP may be too easy overall (hence the 99%+ ceiling). Testing on harder benchmarks (e.g., CodeContests, real-world CI/CD logs) where the verdict distinction is not as cleanly captured by exception presence would test whether the shortcut finding generalizes.\n\n5. **Token-level attribution.** Use integrated gradients or SHAP to show which tokens drive predictions in the with-marker condition. If the model truly relies on the marker, attribution should concentrate on those tokens.\n\n6. **Statistical testing on the nomarker drop.** With only 3 seeds (89.63% ± 2.50), is the drop from 99.83% statistically significant? A paired test would be appropriate. (The drop is large enough that it likely is, but the paper should report this formally.)\n\n## 7. Overall Assessment\n\n**Score: 3 (Weak Reject)**\n\nThe paper identifies a real and potentially useful observation: format markers in VOTA exception traces provide an efficient classification shortcut, and SFT barely outperforms a regex baseline on this specific task/format combination. However, the contribution is weakened by several factors:\n\n(a) The finding is largely predictable given the trace design — embedding an explicit pass/fail indicator naturally leads to models using it.\n\n(b) The nomarker experiment has a significant confound (empty vs. content-rich traces) that inflates the estimated format marker contribution.\n\n(c) The theoretical framing as \"shortcut learning\" analogous to NLI annotation artifacts is strained — intentionally designed format markers are not annotation artifacts.\n\n(d) The scope is narrow (one trace format, one small dataset, one primary model) yet the claims are broad.\n\n(e) The paper lacks mechanistic evidence (attention, probing) to confirm the shortcut mechanism beyond behavioral accuracy deltas.\n\nFor a top venue like EMNLP Main, the paper would need: (1) a cleaner nomarker experimental design that controls for the empty-trace confound, (2) mechanistic evidence beyond accuracy, (3) demonstration that the finding generalizes beyond VOTA on HumanEval+MBPP, and (4) a more nuanced theoretical framing that distinguishes intentional format design from unintentional annotation artifacts.\n\nThe paper's practical recommendation (include format ablation as a control) is valuable but does not by itself constitute a sufficient contribution for a top venue.\n\n## 8. Confidence\n\n**4/5** — I am familiar with the shortcut learning literature, SFT for classification, and code intelligence evaluation methodology. I am confident in my assessment of the experimental design weaknesses and the theoretical framing issues. Minor uncertainty around whether the community would find the \"cautionary tale\" framing sufficient for acceptance despite the predictability of the core finding.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29928f56-998e-4bf9-adb8-54bb2c2289a9",
  "isSidechain": true,
  "agentId": "ac10b8784a4950006",
  "requestId": "req_011Cb6a8FYuT5Ua84sRkkKKB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b9cf8e05-07cc-4e1b-b2d9-539a88ca452c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "ab493159-c57d-451b-9109-6ba744c1f6a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BcXjehoncDzsP2APMKmZCC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 700,
      "cache_read_input_tokens": 79747,
      "output_tokens": 3269,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 700
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3269,
          "cache_read_input_tokens": 79747,
          "cache_creation_input_tokens": 700,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 700,
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

_source line 41 · 2026-05-16T16:36:26.792Z_

<details><summary>↩ Tool result · `toolu_01Lp1QNSiuzMdabChVgyHGPQ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/dream_reports/dream_20260516T155731/worst/review_report.md\", \"dream_id\": \"dream_20260516T155731\", \"tier\": \"worst\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b9cf8e05-07cc-4e1b-b2d9-539a88ca452c",
  "isSidechain": true,
  "promptId": "1671510c-98af-4e06-a3f5-68dced519a8b",
  "agentId": "ac10b8784a4950006",
  "type": "user",
  "uuid": "071928aa-a401-4da6-8b9b-e1299efd6222",
  "sourceToolAssistantUUID": "b9cf8e05-07cc-4e1b-b2d9-539a88ca452c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "ab493159-c57d-451b-9109-6ba744c1f6a1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-16T16:36:35.889Z_

Review submitted. Here is the summary:

**Score: 3 (Weak Reject) | Confidence: 4/5**

Key findings from the review:

1. **Core weakness — predictable finding.** The format markers explicitly encode pass/fail, so a model using them is expected behavior, not a surprising shortcut. The NLI annotation artifact analogy is strained because these markers are intentional, not accidental label leakage.

2. **Confounded nomarker experiment.** After marker removal, pass samples become empty while fail samples retain content. The accuracy drop likely reflects a trace-length/content-asymmetry confound rather than cleanly measuring "format marker contribution." The paper needs controlled marker replacement (neutral placeholder) to isolate the effect.

3. **Circular decomposition.** The 41.3% "format contribution" number assumes the nomarker condition cleanly measures content-only learning, which it does not given the confound.

4. **Narrow scope with broad claims.** One trace format (VOTA), one dataset (591 problems), 4 models. Title overstates generalizability.

5. **Missing mechanistic evidence.** No attention analysis, probing, or attribution to confirm the shortcut mechanism beyond accuracy deltas.

The paper's practical recommendation (format ablation as mandatory control) is useful but insufficient for a top venue without the methodological issues being resolved.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "071928aa-a401-4da6-8b9b-e1299efd6222",
  "isSidechain": true,
  "agentId": "ac10b8784a4950006",
  "requestId": "req_011Cb6aEurS8UrCmRxciMmyc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d470ee7c-0a8d-4474-b448-ba574391f472",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "ab493159-c57d-451b-9109-6ba744c1f6a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P7mFipdKqQvDWVJz7buU8t",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3397,
      "cache_read_input_tokens": 80447,
      "output_tokens": 316,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3397
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 316,
          "cache_read_input_tokens": 80447,
          "cache_creation_input_tokens": 3397,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3397,
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
