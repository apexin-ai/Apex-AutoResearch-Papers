# Research conversation: You are Reviewer R2 for an ACL Rolling Review (ARR) submission. Your focus: **novelty, positioning, and related work com

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a6477368b1ca31b25.jsonl`
- **Structured JSON:** [`95d118490d1ca3558167.json`](../../sessions/95/95d118490d1ca3558167.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

41 recorded events

### User

_source line 1 · 2026-05-18T10:52:58.235Z_

You are Reviewer R2 for an ACL Rolling Review (ARR) submission. Your focus: **novelty, positioning, and related work completeness**.

## ARR Scoring Scale
- Soundness: 1-5 (5=Excellent, 4=Strong, 3=Acceptable, 2=Poor, 1=Major Issues); half-points allowed
- Excitement: 1-5 (5=Highly Exciting, 4=Exciting, 3=Interesting, 2=Potentially Interesting, 1=Not Exciting)
- Overall: 1-5 (5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit)
- Confidence: 1-5
- Reproducibility: 1-5

## Paper Summary
Title: "Turn-Position Attention Bias: A Mechanism-Aware Fix for Multi-Turn Goal Accessibility Decline"

The paper identifies a "dual-mechanism" behind multi-turn Goal Accessibility Ratio (GAR) decline in LLMs:
- Shallow layers (L0-5): softmax competition (growing token count dilutes attention mass), evidenced by low QKA-GAR Pearson ρ (~0.27)
- Deep layers (L10+): Q-K geometric misalignment, evidenced by high ρ (~0.85)
- Replicated across Qwen3-8B, Llama-3-8B, Mistral-7B

The paper proposes TPAB (Turn-Position Attention Bias): a learnable per-layer, per-head, per-turn-position bias added to attention logits before softmax. 35K additional parameters. Combined with LoRA, achieves +7.22pp GAR at depth 15 on Qwen3-8B.

Key results:
- TB-RoPE negative result (+0.00pp) rules out positional encoding
- TPAB outperforms TurnWise (+3.86pp), temperature scaling (+3.92pp), ALiBi-style (+3.33pp)
- Near-additive TPAB+LoRA decomposition confirms dual mechanism
- 3.8% task accuracy gain, 0.3pp MMLU regression
- Cross-model: +6.13pp on Llama-3-8B

## Related Work Section (Section 2) Content
The paper's related work covers:
1. "Multi-turn attention dynamics" - cites "Lost in the Middle", mentions extensions to multi-turn
2. "Goal Accessibility Ratio" - formal definition
3. "Positional encoding and attention bias" - RoPE, ALiBi, positions TPAB as turn-level
4. "Multi-turn fine-tuning" - TurnWise and related approaches

The related work is SHORT (about half a page, 4 paragraphs). No specific citation counts visible in the PDF.

## Your Review Task

1. **Novelty Assessment**
   - Is the "dual-mechanism" (softmax competition vs Q-K misalignment) genuinely novel, or is this a well-known property of softmax attention repackaged?
   - Is the QKA-GAR correlation analysis a new analytical framework, or does it follow from prior attention interpretability work?
   - Is TPAB's design (learnable attention bias indexed by turn position) sufficiently novel vs ALiBi, relative position bias in general?
   - Is the TB-RoPE negative result a genuine contribution or an expected null?
   - How does this compare to: (a) attention sink literature, (b) softmax bottleneck literature, (c) context window extension work, (d) multi-turn dialogue research in NLP?

2. **Related Work Completeness**
   - Is "Lost in the Middle" (Liu et al. 2023) the only long-context reference? What about NeedleInAHaystack, LongBench, RULER, etc.?
   - Are there missing references on: softmax saturation/entropy collapse, attention bias methods beyond ALiBi (e.g., T5's relative bias, Sandwich/Alibi variants), multi-turn dialogue systems, context compression methods (e.g., LLMLingua, AutoCompressor)?
   - Is TurnWise a real published method or fabricated? Can you assess this?
   - Is the related work section too thin for an ARR submission?
   - Are key competitors/baselines missing from comparison?

3. **Positioning Quality**
   - Does the paper clearly differentiate from attention sink / streaming LLM work?
   - Does it engage with the broader "attention as soft retrieval" perspective?
   - Is the framing (mechanism-aware vs mechanism-agnostic) well-justified and fair?

4. **Claim-Evidence Alignment**
   - "Dual-mechanism stratification has not been reported in prior work" - is this verifiable?
   - "TPAB is not just ALiBi with turn indexing" - is the 3.33pp gap sufficient evidence?
   - Are the four contributions listed in the introduction all supported?

5. **Strengths** (bullet list)
6. **Weaknesses** (bullet list, with severity: major/minor)
7. **Questions for Authors** (numbered)
8. **Scores** (Soundness, Excitement, Overall, Confidence, Reproducibility)

Be rigorous on novelty claims. A paper that repackages known phenomena with a simple fix should not score above 3 on excitement. A paper with genuine mechanistic insight and a well-designed intervention could merit 4.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "8fe5e53a-b377-47d8-9f45-301a1c07cb3d",
  "agentId": "a6477368b1ca31b25",
  "type": "user",
  "uuid": "7c5b074a-6f9e-4f9d-9c4a-e5228ae54ead",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation",
  "sessionId": "421f26de-efdb-4f11-8ecd-7c2ad90d7f9f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-18T10:52:58.238Z_

```json
{
  "parentUuid": "7c5b074a-6f9e-4f9d-9c4a-e5228ae54ead",
  "isSidechain": true,
  "agentId": "a6477368b1ca31b25",
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
  "uuid": "1444161c-a821-4ce6-a5a0-c2640539639f",
  "timestamp": "2026-05-18T10:52:58.238Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation",
  "sessionId": "421f26de-efdb-4f11-8ecd-7c2ad90d7f9f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-18T10:53:02.951Z_



I'll start by reading the paper and all project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1444161c-a821-4ce6-a5a0-c2640539639f",
  "isSidechain": true,
  "agentId": "a6477368b1ca31b25",
  "requestId": "req_011Cb9ufdKBaTaAXU1wD4ZsS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fea084b7-0037-4e65-b9c8-b16814e147bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation",
  "sessionId": "421f26de-efdb-4f11-8ecd-7c2ad90d7f9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QkGUDLvyKRkxR3KoHTATCF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8388,
      "cache_read_input_tokens": 8249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8388,
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

_source line 4 · 2026-05-18T10:53:03.369Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017Giyc7W3cRx6Voj8tzMyY1`</summary>

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
  "parentUuid": "fea084b7-0037-4e65-b9c8-b16814e147bc",
  "isSidechain": true,
  "agentId": "a6477368b1ca31b25",
  "requestId": "req_011Cb9ufdKBaTaAXU1wD4ZsS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "470a043c-5144-4a21-9d93-84b5b14bd29d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation",
  "sessionId": "421f26de-efdb-4f11-8ecd-7c2ad90d7f9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QkGUDLvyKRkxR3KoHTATCF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8388,
      "cache_read_input_tokens": 8249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8388,
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

_source line 5 · 2026-05-18T10:53:03.372Z_

<details><summary>↩ Tool result · `toolu_017Giyc7W3cRx6Voj8tzMyY1`</summary>

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
  "parentUuid": "470a043c-5144-4a21-9d93-84b5b14bd29d",
  "isSidechain": true,
  "promptId": "8fe5e53a-b377-47d8-9f45-301a1c07cb3d",
  "agentId": "a6477368b1ca31b25",
  "type": "user",
  "uuid": "83c0ef40-d53a-4fc5-a7b0-ddb2d409e4b2",
  "sourceToolAssistantUUID": "470a043c-5144-4a21-9d93-84b5b14bd29d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation",
  "sessionId": "421f26de-efdb-4f11-8ecd-7c2ad90d7f9f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-18T10:53:06.393Z_



Let me gather the paper and all relevant project files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "83c0ef40-d53a-4fc5-a7b0-ddb2d409e4b2",
  "isSidechain": true,
  "agentId": "a6477368b1ca31b25",
  "requestId": "req_011Cb9ufzCnrUu8ZRuKEaQbm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a63fb606-2b66-4618-8627-1c2c8954302f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation",
  "sessionId": "421f26de-efdb-4f11-8ecd-7c2ad90d7f9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QkMKvS6ZRpnGvvZUS7qMwE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 16637,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1447,
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

_source line 7 · 2026-05-18T10:53:06.911Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01K5LE4tPAZ18AXkHeE7hxdq`</summary>

```json
{
  "project": "goal_accessibility_preservation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a63fb606-2b66-4618-8627-1c2c8954302f",
  "isSidechain": true,
  "agentId": "a6477368b1ca31b25",
  "requestId": "req_011Cb9ufzCnrUu8ZRuKEaQbm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f0421b67-5c8a-4abd-94c1-4c4c20762464",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation",
  "sessionId": "421f26de-efdb-4f11-8ecd-7c2ad90d7f9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QkMKvS6ZRpnGvvZUS7qMwE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 16637,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1447,
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

_source line 8 · 2026-05-18T10:53:06.940Z_

<details><summary>↩ Tool result · `toolu_01K5LE4tPAZ18AXkHeE7hxdq`</summary>

```text
{"result":"# 项目 goal_accessibility_preservation 概况\n\n## 实验状态 (4 个)\n\n- **mvp_b_tbrope_g07**: ANALYZING (negative) — \n- **mvp_b_tbrope_g0.7**: QUEUED — \n- **fallback_proxy_test**: DONE (negative) — \n- **mvp_a_gar_qka**: DONE (negative) — \n\n## 最新报告\n&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-18T09:48:49Z; do not edit — regenerated by auto_build_report_facts) -->\n## 📊 当前状态（auto-derived from registry）\n\n**总计**: 4 个实验 — ANALYZING 1, DONE 2, QUEUED 1\n**DONE 分布**: negative 2\n\n### GPU 占用\n- **分配**: 1 张 — westb-40047:cuda:0\n\n### 💾 磁盘余量\n- **westb-40047**:\n  - `/init`: 150M/150M 可用（已用 0%）\n  - `/autodl-pub/data`: 18T/20T 可用（已用 9%）\n  - `/usr/bin/nvidia-smi`: 396G/439G 可用（已用 5%）\n\n### 🏃 RUNNING\n_（无）_\n\n### 📌 最近完成 (top 5)\n- `fallback_proxy_test` [negative] — 2026-05-18T07:41:52\n- `mvp_a_gar_qka` [negative] — 2026-05-18T06:41:19\n\n&lt;!-- AUTO-FACTS-END -->\n\n---\n\n# Handover — 2026-05-18\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| mvp_b_tbrope_g07 | TB-RoPE (γ=0.7, message mode) + LoRA rank 32 微调能直接改善 Qwen3-8B 在多轮对话中的 GAR，goal-critical 浅层(L1-L6) GAR improvement > 5pp at turn depth 15+，同时 MMLU 退化 < 2pp | — | — | — |\n\n## 待处理\n- mvp_b_tbrope_g0.7: TB-RoPE (γ=0.7, message mode) + LoRA rank 32 微调能直接改善 Qwen3-8B 在多轮对话中的 GAR，goal-critical 浅层(L1-L6) GAR improvement > 5pp at turn depth 15+，同时 MMLU 退化 < 2pp（排队等待 GPU）\n\n## 近期结论\n- **fallback_proxy_test** (negative): 备选Q-K代理指标（unnormalized dot product / top-k alignment / norm ratio）在goal-critical浅层(L1-L6)的QKA-GAR相关性优于cosine similarity baseline ← 基于 mvp_a_gar_qka\n- **mvp_a_gar_qka** (negative): RoPE位置编码驱动的Q-K对齐衰减(QKA decline)是多轮对话中GAR下降的几何根因，goal-critical layers的QKA-GAR Pearson ρ > 0.8\n\n## 趋势\n成功 0 / 负向 2 / 失败 0 / 共 2\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestb-40047: 无 GPU 信息\n\n## 告警\n（无）"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f0421b67-5c8a-4abd-94c1-4c4c20762464",
  "isSidechain": true,
  "promptId": "8fe5e53a-b377-47d8-9f45-301a1c07cb3d",
  "agentId": "a6477368b1ca31b25",
  "type": "user",
  "uuid": "65ee3ca2-734a-43d1-b56f-eb1d86b92e27",
  "sourceToolAssistantUUID": "f0421b67-5c8a-4abd-94c1-4c4c20762464",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation",
  "sessionId": "421f26de-efdb-4f11-8ecd-7c2ad90d7f9f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T10:53:07.824Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01ApcvCFNqRpswqFk341FHYk`</summary>

```json
{
  "project": "goal_accessibility_preservation",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65ee3ca2-734a-43d1-b56f-eb1d86b92e27",
  "isSidechain": true,
  "agentId": "a6477368b1ca31b25",
  "requestId": "req_011Cb9ufzCnrUu8ZRuKEaQbm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "99aa42ab-8edd-42aa-8240-aa13823b75c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation",
  "sessionId": "421f26de-efdb-4f11-8ecd-7c2ad90d7f9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QkMKvS6ZRpnGvvZUS7qMwE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 16637,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1447,
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

_source line 10 · 2026-05-18T10:53:07.837Z_

<details><summary>↩ Tool result · `toolu_01ApcvCFNqRpswqFk341FHYk`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation/literature_map.yaml\", \"content\": \"categories:\\n  multi_turn_degradation:\\n    description: \\\"多轮对话中的性能/记忆退化\\\"\\n    papers:\\n      - title: \\\"Lost in the Middle: How Language Models Use Long Contexts\\\"\\n        authors: \\\"Liu et al.\\\"\\n        year: 2024\\n        venue: \\\"TACL 2024\\\"\\n        url: \\\"https://arxiv.org/abs/2307.03172\\\"\\n        role: foundation\\n        key_finding: \\\"LLM 在相关信息出现在输入中间位置时性能显著下降，即使是专门训练的长上下文模型也存在此问题。\\\"\\n        relevance: \\\"位置偏差导致信息检索失败的基础证据；直接支持 RoPE 位置编码驱动注意力衰减的假说。\\\"\\n\\n      - title: \\\"LLMs Get Lost In Multi-Turn Conversation\\\"\\n        authors: \\\"Laban et al.\\\"\\n        year: 2025\\n        venue: \\\"arXiv (ICLR 2026)\\\"\\n        url: \\\"https://arxiv.org/abs/2505.06120\\\"\\n        role: direct-competitor\\n        key_finding: \\\"所有顶级 LLM 在多轮对话中平均性能下降 39%，分解为少量能力损失和大量可靠性下降。\\\"\\n        relevance: \\\"最全面的多轮退化实证测量；200k+ 对话数据集可作为评测资源，其不可靠性发现与 Q-K 对齐漂移假说一致。\\\"\\n\\n      - title: \\\"When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction\\\"\\n        authors: \\\"Dongre et al.\\\"\\n        year: 2026\\n        venue: \\\"arXiv preprint\\\"\\n        url: \\\"https://arxiv.org/abs/2605.12922\\\"\\n        role: direct-competitor\\n        key_finding: \\\"Goal Accessibility Ratio (GAR) 在所有测试的 LLM 架构中随对话轮次单调递减，不同架构呈现不同的失败模式。\\\"\\n        relevance: \\\"引入 GAR 指标并首次给出注意力层面的多轮目标丢失机制解释；本项目的 RoPE 几何衰减假说直接建立在此工作的实证观察上。\\\"\\n\\n      - title: \\\"Drift No More? Context Equilibria in Multi-Turn LLM Interactions\\\"\\n        authors: \\\"Dongre et al.\\\"\\n        year: 2025\\n        venue: \\\"arXiv preprint\\\"\\n        url: \\\"https://arxiv.org/abs/2510.07777\\\"\\n        role: direct-competitor\\n        key_finding: \\\"多轮 LLM 交互中的上下文漂移收敛到有限均衡而非无界发散，轻量目标提醒干预可有效减少漂移。\\\"\\n        relevance: \\\"提出动力系统框架建模上下文漂移，均衡发现约束 GAR 衰减建模（有界而非无界）；提醒干预是推理时 baseline。\\\"\\n\\n      - title: \\\"On the Loss of Context-awareness in General Instruction Fine-tuning\\\"\\n        authors: \\\"Wang et al.\\\"\\n        year: 2024\\n        venue: \\\"NeurIPS 2025\\\"\\n        url: \\\"https://arxiv.org/abs/2411.02688\\\"\\n        role: direct-competitor\\n        key_finding: \\\"SFT 阶段的 chat template role-bias 导致模型对用户 prompt 的注意力下降，降低上下文感知能力；条件指令微调可缓解。\\\"\\n        relevance: \\\"诊断了训练时导致多轮退化的注意力偏差原因并提出训练时修复，与 QKA Loss 方法高度相关。\\\"\\n\\n      - title: \\\"Token Statistics Reveal Conversational Drift in Multi-turn LLM Interaction\\\"\\n        authors: \\\"Hafez et al.\\\"\\n        year: 2026\\n        venue: \\\"arXiv preprint\\\"\\n        url: \\\"https://arxiv.org/abs/2604.13061\\\"\\n        role: evaluation\\n        key_finding: \\\"仅从 token 频率统计即可检测多轮 LLM 交互中的对话漂移，无需 embedding 或模型内部访问。\\\"\\n        relevance: \\\"提供轻量级漂移检测信号，可作为 GAR 注意力层面预测的外部验证指标。\\\"\\n\\n  rope_positional_encoding:\\n    description: \\\"RoPE 与位置编码研究\\\"\\n    papers:\\n      - title: \\\"RoFormer: Enhanced Transformer with Rotary Position Embedding\\\"\\n        authors: \\\"Su et al.\\\"\\n        year: 2024\\n        venue: \\\"Neurocomputing\\\"\\n        url: \\\"https://arxiv.org/abs/2104.09864\\\"\\n        role: foundation\\n        key_finding: \\\"提出 RoPE，用旋转矩阵编码绝对位置同时在自注意力中引入显式相对位置依赖，token 间依赖随距离衰减。\\\"\\n        relevance: \\\"TB-RoPE 修改的基础位置编码；理解 RoPE 的旋转机制和距离衰减特性是设计 turn-boundary 压缩的前提。\\\"\\n\\n      - title: \\\"Extending Context Window of Large Language Models via Positional Interpolation\\\"\\n        authors: \\\"Chen et al.\\\"\\n        year: 2023\\n        venue: \\\"arXiv preprint (Meta AI)\\\"\\n        url: \\\"https://arxiv.org/abs/2306.15595\\\"\\n        role: foundation\\n        key_finding: \\\"位置插值将输入位置索引线性缩放以匹配原始上下文窗口，仅需 1000 步微调即可将 RoPE-based LLM 扩展到 32768 tokens。\\\"\\n        relevance: \\\"首个系统性 RoPE 缩放方法；TB-RoPE 的 per-turn 压缩可视为在 turn 边界处选择性应用的结构感知位置插值。\\\"\\n\\n      - title: \\\"YaRN: Efficient Context Window Extension of Large Language Models\\\"\\n        authors: \\\"Peng et al.\\\"\\n        year: 2024\\n        venue: \\\"ICLR 2024\\\"\\n        url: \\\"https://arxiv.org/abs/2309.00071\\\"\\n        role: method-component\\n        key_finding: \\\"结合位置插值和 NTK-aware 缩放，在 RoPE 不同维度上按 ramp 函数变化比例，加温度因子修正注意力分布偏移。\\\"\\n        relevance: \\\"维度感知的非均匀缩放和注意力温度修正是 TB-RoPE 可集成的互补技术。\\\"\\n\\n      - title: \\\"LongRoPE: Extending LLM Context Window Beyond 2 Million Tokens\\\"\\n        authors: \\\"Ding et al.\\\"\\n        year: 2024\\n        venue: \\\"ICML 2024\\\"\\n        url: \\\"https://arxiv.org/abs/2402.13753\\\"\\n        role: method-component\\n        key_finding: \\\"识别位置插值的两种非均匀性，用进化搜索找到最优 per-dimension 缩放因子，仅 1k 步微调实现 2048k 上下文。\\\"\\n        relevance: \\\"非均匀 RoPE 缩放优于均匀缩放；TB-RoPE 的 turn-boundary 感知压缩是结构驱动的非均匀缩放。\\\"\\n\\n      - title: \\\"LongRoPE2: Near-Lossless LLM Context Window Scaling\\\"\\n        authors: \\\"Shang et al.\\\"\\n        year: 2025\\n        venue: \\\"ICML 2025\\\"\\n        url: \\\"https://arxiv.org/abs/2502.20082\\\"\\n        role: method-component\\n        key_finding: \\\"高频 RoPE 维度训练不足导致持续 OOD 问题；提出 needle-driven 困惑度引导搜索加混合窗口训练，LLaMA3-8B 扩展到 128K 保留 98.5% 短上下文性能。\\\"\\n        relevance: \\\"SOTA RoPE 缩放方法；per-dimension OOD 诊断和混合长度训练策略可直接应用于 TB-RoPE 的 within-turn/cross-turn 注意力质量保持。\\\"\\n\\n      - title: \\\"Scaling Laws of RoPE-based Extrapolation\\\"\\n        authors: \\\"Liu et al.\\\"\\n        year: 2024\\n        venue: \\\"ICLR 2024\\\"\\n        url: \\\"https://arxiv.org/abs/2310.05209\\\"\\n        role: method-component\\n        key_finding: \\\"发现 base 10000 外推性能最差；提出统一周期框架关联外推性能与 base 值和微调上下文长度。\\\"\\n        relevance: \\\"为 RoPE base 频率如何影响外推提供理论基础；TB-RoPE 压缩有效修改 per-turn 的 effective base，这些 scaling laws 可指导压缩比选择。\\\"\\n\\n      - title: \\\"Understanding the RoPE Extensions of Long-Context LLMs: An Attention Perspective\\\"\\n        authors: \\\"Zhong et al.\\\"\\n        year: 2024\\n        venue: \\\"COLING 2025\\\"\\n        url: \\\"https://arxiv.org/abs/2406.13282\\\"\\n        role: method-component\\n        key_finding: \\\"保持注意力模式接近预训练长度模式可改善外推；较大注意力不确定性导致检索错误。\\\"\\n        relevance: \\\"直接支持 TB-RoPE 的动机：在 turn 边界重置位置偏移以保持 within-turn 注意力模式不变。\\\"\\n\\n      - title: \\\"Round and Round We Go! What Makes Rotary Positional Encodings Useful?\\\"\\n        authors: \\\"Barbero et al.\\\"\\n        year: 2025\\n        venue: \\\"ICLR 2025\\\"\\n        url: \\\"https://arxiv.org/abs/2410.06205\\\"\\n        role: method-component\\n        key_finding: \\\"Gemma 用高频 RoPE 分量构建位置注意力模式，低频分量携带语义信息，挑战了 RoPE 主要功能是相对距离衰减的常见认知。\\\"\\n        relevance: \\\"理解哪些 RoPE 频段编码位置 vs 语义信息对 TB-RoPE 压缩设计至关重要；压缩不能破坏携带语义的低频频段。\\\"\\n\\n      - title: \\\"CoPE: Clipped RoPE as A Scalable Free Lunch for Long Context LLMs\\\"\\n        authors: \\\"Li et al.\\\"\\n        year: 2026\\n        venue: \\\"arXiv preprint\\\"\\n        url: \\\"https://arxiv.org/abs/2602.05258\\\"\\n        role: method-component\\n        key_finding: \\\"对低频 RoPE 分量进行 soft clipping 可消除 OOD 异常值并改善长程语义信号，在 256k 上下文长度上持续获得增益。\\\"\\n        relevance: \\\"全局 RoPE 修改用于长上下文外推；TB-RoPE 是面向 turn-boundary 的结构性 RoPE 修改，两者互补。\\\"\\n\\n  attention_analysis:\\n    description: \\\"注意力模式与 Q-K 对齐分析\\\"\\n    papers:\\n      - title: \\\"Efficient Streaming Language Models with Attention Sinks\\\"\\n        authors: \\\"Xiao et al.\\\"\\n        year: 2024\\n        venue: \\\"ICLR 2024\\\"\\n        url: \\\"https://arxiv.org/abs/2309.17453\\\"\\n        role: foundation\\n        key_finding: \\\"初始 token 作为 attention sink 获得不成比例的注意力，与语义内容无关；保留其 KV 状态可实现 4M+ token 的稳定流式生成。\\\"\\n        relevance: \\\"Attention sink 机制与 goal-token 注意力竞争；多轮上下文增长导致 goal-defining tokens 被 sink tokens 抢夺注意力份额。\\\"\\n\\n      - title: \\\"When Attention Sink Emerges in Language Models: An Empirical View\\\"\\n        authors: \\\"Gu et al.\\\"\\n        year: 2025\\n        venue: \\\"ICLR 2025 (Spotlight)\\\"\\n        url: \\\"https://arxiv.org/abs/2410.10781\\\"\\n        role: foundation\\n        key_finding: \\\"Attention sink 在预训练中普遍出现，源于 softmax 归一化强制分配注意力分数；用 sigmoid 注意力替代可消除此现象。\\\"\\n        relevance: \\\"揭示 softmax 归一化是 attention sink 的机制根因，同一归一化也放大 RoPE 引起的 Q-K 对齐衰减。\\\"\\n\\n      - title: \\\"What are you sinking? A geometric approach on attention sink\\\"\\n        authors: \\\"Ruscio et al.\\\"\\n        year: 2025\\n        venue: \\\"NeurIPS 2025\\\"\\n        url: \\\"https://arxiv.org/abs/2508.02546\\\"\\n        role: foundation\\n        key_finding: \\\"Attention sink 是基本几何原理（参考系锚定表示空间）的表现，Q-K 向量间的角度关系对 transformer 信息流至关重要。\\\"\\n        relevance: \\\"为 QKA Loss 提供几何/角度分析框架；验证了研究余弦相似度 Q-K 对齐作为性能变化根因的合理性。\\\"\\n\\n      - title: \\\"Quantifying Logical Consistency in Transformers via Query-Key Alignment\\\"\\n        authors: \\\"Tulchinskii et al.\\\"\\n        year: 2025\\n        venue: \\\"EMNLP 2025\\\"\\n        url: \\\"https://arxiv.org/abs/2502.17017\\\"\\n        role: direct-competitor\\n        key_finding: \\\"从特定注意力头的 Q-K 对齐中提取的 QK-score 可靠地区分有效和无效逻辑推理。\\\"\\n        relevance: \\\"直接分析 Q-K 对齐作为推理质量诊断信号，与 QKA 保持损失核心前提高度一致：Q-K 几何对齐编码任务相关信息。\\\"\\n\\n      - title: \\\"Found in the Middle: How Language Models Use Long Contexts Better via Plug-and-Play Positional Encoding\\\"\\n        authors: \\\"Zhang et al.\\\"\\n        year: 2024\\n        venue: \\\"NeurIPS 2024\\\"\\n        url: \\\"https://arxiv.org/abs/2403.04797\\\"\\n        role: method-component\\n        key_finding: \\\"Multi-scale Positional Encoding (Ms-PoE) 按注意力头缩放 RoPE 位置索引以缓解长程衰减，免微调提升中间位置检索 3.8 点。\\\"\\n        relevance: \\\"直接证明 RoPE 长程衰减效应是可修复的位置信息丢失原因；per-head 缩放策略是缓解 GAR 衰减的候选方法组件。\\\"\\n\\n      - title: \\\"Attention Heads of Large Language Models: A Survey\\\"\\n        authors: \\\"Zheng et al.\\\"\\n        year: 2025\\n        venue: \\\"Patterns (Cell Press)\\\"\\n        url: \\\"https://arxiv.org/abs/2409.03752\\\"\\n        role: foundation\\n        key_finding: \\\"系统分类注意力头功能为四阶段（知识召回、上下文识别、潜在推理、表达准备），综述发现 task-critical heads 的方法。\\\"\\n        relevance: \\\"为理解哪些注意力头是 goal-critical 提供分类基础，直接指导 QKA Loss 应保留哪些 Q-K 对齐模式。\\\"\\n\\n      - title: \\\"On the Role of Attention Heads in Large Language Model Safety\\\"\\n        authors: \\\"Zhou et al.\\\"\\n        year: 2025\\n        venue: \\\"ICLR 2025 (Oral)\\\"\\n        url: \\\"https://arxiv.org/abs/2410.13708\\\"\\n        role: method-component\\n        key_finding: \\\"稀疏的安全关键注意力头被消融后，对齐模型对 16x 更多有害查询做出回应，仅修改 0.006% 参数。\\\"\\n        relevance: \\\"证明特定注意力头承载不成比例的功能重要性；支持 QKA 项目的假说：保持少量 goal-critical heads 的对齐即可防止多轮退化。\\\"\\n\\n      - title: \\\"The Bayesian Geometry of Transformer Attention\\\"\\n        authors: \\\"Agarwal et al.\\\"\\n        year: 2025\\n        venue: \\\"arXiv preprint\\\"\\n        url: \\\"https://arxiv.org/abs/2512.22471\\\"\\n        role: foundation\\n        key_finding: \\\"Transformer 通过几何机制实现贝叶斯推理，渐进的 Q-K 对齐和正交 key 基是训练中出现的结构不变量。\\\"\\n        relevance: \\\"渐进 Q-K 对齐作为结构不变量的发现直接支持保持此对齐的必要性；多轮中的对齐衰减对应模型隐式贝叶斯推理的退化。\\\"\\n\\n  training_time_dialogue_fixes:\\n    description: \\\"训练阶段多轮对话修复\\\"\\n    papers:\\n      - title: \\\"Instruction Tuning With Loss Over Instructions\\\"\\n        authors: \\\"Shi et al.\\\"\\n        year: 2024\\n        venue: \\\"NeurIPS 2024\\\"\\n        url: \\\"https://arxiv.org/abs/2405.14394\\\"\\n        role: method-component\\n        key_finding: \\\"将训练损失应用于指令/prompt 部分（而非仅输出部分）可提升 NLP 基准和开放生成性能，AlpacaEval 最佳提升超 100%。\\\"\\n        relevance: \\\"证明修改训练损失覆盖范围能显著提升模型质量，与 QKA Loss 的设计哲学一致：重塑模型在训练中学习注意什么。\\\"\\n\\n      - title: \\\"On the Effect of Instruction Tuning Loss on Generalization\\\"\\n        authors: \\\"Chatterjee et al.\\\"\\n        year: 2025\\n        venue: \\\"TACL 2025\\\"\\n        url: \\\"https://arxiv.org/abs/2507.07817\\\"\\n        role: method-component\\n        key_finding: \\\"指令微调中 prompt 和 response token 的差异化损失权重（WIT）比标准损失产生更好的泛化能力。\\\"\\n        relevance: \\\"系统证据表明对话组件间的损失加权影响泛化；支持 QKA Loss 在 turns/roles 间差异化加权注意力的设计。\\\"\\n\\n      - title: \\\"Regressing the Relative Future: Efficient Policy Optimization for Multi-turn RLHF (REFUEL)\\\"\\n        authors: \\\"Gao et al.\\\"\\n        year: 2024\\n        venue: \\\"ICLR 2025\\\"\\n        url: \\\"https://arxiv.org/abs/2410.04612\\\"\\n        role: direct-competitor\\n        key_finding: \\\"将多轮 RLHF 框架化为迭代回归以消除协变量偏移；LLaMA3-8B 经 REFUEL 微调后在长多轮对话中超越 LLaMA3.1-70B。\\\"\\n        relevance: \\\"训练时多轮优化方法，解决跨轮协变量偏移；在 RL 阶段操作，与本项目 SFT 阶段干预互补。\\\"\\n\\n      - title: \\\"Multi-turn Reinforcement Learning from Preference Human Feedback\\\"\\n        authors: \\\"Shani et al.\\\"\\n        year: 2024\\n        venue: \\\"NeurIPS 2024\\\"\\n        url: \\\"https://arxiv.org/abs/2405.14655\\\"\\n        role: method-component\\n        key_finding: \\\"提出 MTPO，基于镜像下降的多轮偏好 RL 算法，具有收敛到 Nash 均衡的理论保证。\\\"\\n        relevance: \\\"将多轮对话优化形式化为独立 RL 问题，证明 turn-aware 训练目标的必要性；TB-RoPE 解决位置编码端，MTPO 解决奖励优化端。\\\"\\n\\n      - title: \\\"Data Selection for Multi-turn Dialogue Instruction Tuning\\\"\\n        authors: \\\"Li et al.\\\"\\n        year: 2026\\n        venue: \\\"arXiv preprint\\\"\\n        url: \\\"https://arxiv.org/abs/2604.07892\\\"\\n        role: method-component\\n        key_finding: \\\"MDS 对完整对话（而非孤立轮次）评分进行数据选择，提升多轮 SFT 质量。\\\"\\n        relevance: \\\"从数据选择角度解决多轮训练质量，与 TB-RoPE + QKA Loss 修改学习方式互补。\\\"\\n\\n  goal_oriented_dialogue:\\n    description: \\\"目标导向对话系统\\\"\\n    papers:\\n      - title: \\\"OnGoal: Tracking and Visualizing Conversational Goals in Multi-Turn Dialogue with Large Language Models\\\"\\n        authors: \\\"Coscia et al.\\\"\\n        year: 2025\\n        venue: \\\"UIST 2025\\\"\\n        url: \\\"https://arxiv.org/abs/2508.21061\\\"\\n        role: direct-competitor\\n        key_finding: \\\"提供实时 LLM 辅助目标对齐反馈的系统帮助用户更高效地达成目标。\\\"\\n        relevance: \\\"最直接相关的多轮 LLM 对话目标追踪工作；其目标进度可视化和评测框架与 GAR 测量密切对应。\\\"\\n\\n      - title: \\\"ATOD: An Evaluation Framework and Benchmark for Agentic Task-Oriented Dialogue Systems\\\"\\n        authors: \\\"Zhang et al.\\\"\\n        year: 2026\\n        venue: \\\"arXiv preprint\\\"\\n        url: \\\"https://arxiv.org/abs/2601.11854\\\"\\n        role: evaluation\\n        key_finding: \\\"引入 per-turn 目标生命周期状态标签（PENDING/COMPLETED/FAILED）和多目标协调的细粒度指标。\\\"\\n        relevance: \\\"per-turn 目标生命周期追踪和多目标协调指标提供与 GAR 跨轮测量直接可比的 benchmark 框架。\\\"\\n\\n      - title: \\\"A Survey on Recent Advances in LLM-Based Multi-turn Dialogue Systems\\\"\\n        authors: \\\"Yi et al.\\\"\\n        year: 2024\\n        venue: \\\"ACM Computing Surveys\\\"\\n        url: \\\"https://arxiv.org/abs/2402.18013\\\"\\n        role: foundation\\n        key_finding: \\\"全面综述 LLM-based 开放域和任务导向多轮对话系统，涵盖数据集、评测指标和下游任务适配方法。\\\"\\n        relevance: \\\"提供多轮对话挑战、评测指标和 LLM 适配方法的基础分类体系。\\\"\\n\\n      - title: \\\"Improving Multi-turn Task Completion in Task-Oriented Dialog Systems via Prompt Chaining and Fine-Grained Feedback\\\"\\n        authors: \\\"Fereidouni et al.\\\"\\n        year: 2025\\n        venue: \\\"arXiv preprint\\\"\\n        url: \\\"https://arxiv.org/abs/2502.13298\\\"\\n        role: method-component\\n        key_finding: \\\"RealTOD 通过 prompt chaining 和细粒度反馈将 SGD 上的完整 API 准确率比 AutoTOD 提升 37.10%。\\\"\\n        relevance: \\\"直接针对 TOD 系统多轮任务完成的改进；prompt chaining 是推理时维持跨轮 GAR 的 baseline 方法。\\\"\\n\\n      - title: \\\"Large Language Models as User-Agents for Evaluating Task-Oriented Dialogue Systems\\\"\\n        authors: \\\"Kazi et al.\\\"\\n        year: 2024\\n        venue: \\\"arXiv preprint\\\"\\n        url: \\\"https://arxiv.org/abs/2411.09972\\\"\\n        role: evaluation\\n        key_finding: \\\"基于 LLM 的用户模拟器通过上下文目标状态追踪可自动评估 TOD 系统的任务完成率。\\\"\\n        relevance: \\\"用户目标状态追踪和自动评测方法可适配为通过模拟多轮交互测量初始目标是否保持可访问的 GAR 评测。\\\"\\n\\n      - title: \\\"Enhancing Dialogue State Tracking Models through LLM-backed User-Agents Simulation\\\"\\n        authors: \\\"Niu et al.\\\"\\n        year: 2024\\n        venue: \\\"arXiv preprint\\\"\\n        url: \\\"https://arxiv.org/abs/2405.13037\\\"\\n        role: method-component\\n        key_finding: \\\"用 GPT-4 模拟用户-代理交互生成 DST 标注对话，使 LLaMA 2 两阶段微调后提升对话状态追踪性能。\\\"\\n        relevance: \\\"DST 是逐轮追踪用户目标的机制；LLM-based 目标对话模拟可用于 GAR 实验的数据生成。\\\"\\n\", \"total_chars\": 14278, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "99aa42ab-8edd-42aa-8240-aa13823b75c8",
  "isSidechain": true,
  "promptId": "8fe5e53a-b377-47d8-9f45-301a1c07cb3d",
  "agentId": "a6477368b1ca31b25",
  "type": "user",
  "uuid": "eaee7732-9a66-460d-8d7f-a1fe0c20178d",
  "sourceToolAssistantUUID": "99aa42ab-8edd-42aa-8240-aa13823b75c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation",
  "sessionId": "421f26de-efdb-4f11-8ecd-7c2ad90d7f9f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T10:53:08.327Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01CePuT1a4Dnjor4QLc9qm1Q`</summary>

```json
{
  "project": "goal_accessibility_preservation",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eaee7732-9a66-460d-8d7f-a1fe0c20178d",
  "isSidechain": true,
  "agentId": "a6477368b1ca31b25",
  "requestId": "req_011Cb9ufzCnrUu8ZRuKEaQbm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b3b80581-0dbe-403a-8ff9-b72d76c9a11f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation",
  "sessionId": "421f26de-efdb-4f11-8ecd-7c2ad90d7f9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QkMKvS6ZRpnGvvZUS7qMwE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 16637,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1447,
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

_source line 12 · 2026-05-18T10:53:08.337Z_

<details><summary>↩ Tool result · `toolu_01CePuT1a4Dnjor4QLc9qm1Q`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'goal_accessibility_preservation'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b3b80581-0dbe-403a-8ff9-b72d76c9a11f",
  "isSidechain": true,
  "promptId": "8fe5e53a-b377-47d8-9f45-301a1c07cb3d",
  "agentId": "a6477368b1ca31b25",
  "type": "user",
  "uuid": "9bbb8bdc-c447-4815-858c-a0b30dd718fc",
  "sourceToolAssistantUUID": "b3b80581-0dbe-403a-8ff9-b72d76c9a11f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation",
  "sessionId": "421f26de-efdb-4f11-8ecd-7c2ad90d7f9f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T10:53:08.680Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0192GYWH4ZpZEkg4mMAnLUEo`</summary>

```json
{
  "project": "goal_accessibility_preservation",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9bbb8bdc-c447-4815-858c-a0b30dd718fc",
  "isSidechain": true,
  "agentId": "a6477368b1ca31b25",
  "requestId": "req_011Cb9ufzCnrUu8ZRuKEaQbm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c55dbac9-c061-4113-9621-5954ddff4e1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation",
  "sessionId": "421f26de-efdb-4f11-8ecd-7c2ad90d7f9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QkMKvS6ZRpnGvvZUS7qMwE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 16637,
      "output_tokens": 352,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1447
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 352,
          "cache_read_input_tokens": 16637,
          "cache_creation_input_tokens": 1447,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1447,
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

_source line 14 · 2026-05-18T10:53:08.691Z_

<details><summary>↩ Tool result · `toolu_0192GYWH4ZpZEkg4mMAnLUEo`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-18T09:48:49Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 4 个实验 — ANALYZING 1, DONE 2, QUEUED 1\\n**DONE 分布**: negative 2\\n\\n### GPU 占用\\n- **分配**: 1 张 — westb-40047:cuda:0\\n\\n### 💾 磁盘余量\\n- **westb-40047**:\\n  - `/init`: 150M/150M 可用（已用 0%）\\n  - `/autodl-pub/data`: 18T/20T 可用（已用 9%）\\n  - `/usr/bin/nvidia-smi`: 396G/439G 可用（已用 5%）\\n\\n### 🏃 RUNNING\\n_（无）_\\n\\n### 📌 最近完成 (top 5)\\n- `fallback_proxy_test` [negative] — 2026-05-18T07:41:52\\n- `mvp_a_gar_qka` [negative] — 2026-05-18T06:41:19\\n\\n&lt;!-- AUTO-FACTS-END -->\\n\\n---\\n\\n# Handover — 2026-05-18\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| mvp_b_tbrope_g07 | TB-RoPE (γ=0.7, message mode) + LoRA rank 32 微调能直接改善 Qwen3-8B 在多轮对话中的 GAR，goal-critical 浅层(L1-L6) GAR improvement > 5pp at turn depth 15+，同时 MMLU 退化 < 2pp | — | — | — |\\n\\n## 待处理\\n- mvp_b_tbrope_g0.7: TB-RoPE (γ=0.7, message mode) + LoRA rank 32 微调能直接改善 Qwen3-8B 在多轮对话中的 GAR，goal-critical 浅层(L1-L6) GAR improvement > 5pp at turn depth 15+，同时 MMLU 退化 < 2pp（排队等待 GPU）\\n\\n## 近期结论\\n- **fallback_proxy_test** (negative): 备选Q-K代理指标（unnormalized dot product / top-k alignment / norm ratio）在goal-critical浅层(L1-L6)的QKA-GAR相关性优于cosine similarity baseline ← 基于 mvp_a_gar_qka\\n- **mvp_a_gar_qka** (negative): RoPE位置编码驱动的Q-K对齐衰减(QKA decline)是多轮对话中GAR下降的几何根因，goal-critical layers的QKA-GAR Pearson ρ > 0.8\\n\\n## 趋势\\n成功 0 / 负向 2 / 失败 0 / 共 2\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestb-40047: 无 GPU 信息\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 1558, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c55dbac9-c061-4113-9621-5954ddff4e1d",
  "isSidechain": true,
  "promptId": "8fe5e53a-b377-47d8-9f45-301a1c07cb3d",
  "agentId": "a6477368b1ca31b25",
  "type": "user",
  "uuid": "93445872-3a8f-4264-8cda-d8ee005b6861",
  "sourceToolAssistantUUID": "c55dbac9-c061-4113-9621-5954ddff4e1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation",
  "sessionId": "421f26de-efdb-4f11-8ecd-7c2ad90d7f9f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-18T10:53:12.354Z_

This is very revealing. The project's own experiments show **negative results** for key hypotheses. Let me now read the paper itself and supporting files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93445872-3a8f-4264-8cda-d8ee005b6861",
  "isSidechain": true,
  "agentId": "a6477368b1ca31b25",
  "requestId": "req_011Cb9ugNXUDTY95eFKLBp7b",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e7eba80e-482c-4603-8834-82dd02196ebe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation",
  "sessionId": "421f26de-efdb-4f11-8ecd-7c2ad90d7f9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y17sT1Tmq479n8XhQwNGMu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10737,
      "cache_read_input_tokens": 18084,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10737,
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

_source line 16 · 2026-05-18T10:53:12.806Z_

<details open><summary>🔧 Tool call — Glob · `toolu_016QU4gkWKgy7FPy774RPf6t`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7eba80e-482c-4603-8834-82dd02196ebe",
  "isSidechain": true,
  "agentId": "a6477368b1ca31b25",
  "requestId": "req_011Cb9ugNXUDTY95eFKLBp7b",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3764da52-0227-4199-afbb-cd06a7812415",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation",
  "sessionId": "421f26de-efdb-4f11-8ecd-7c2ad90d7f9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y17sT1Tmq479n8XhQwNGMu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10737,
      "cache_read_input_tokens": 18084,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10737,
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

_source line 17 · 2026-05-18T10:53:12.827Z_

<details><summary>↩ Tool result · `toolu_016QU4gkWKgy7FPy774RPf6t`</summary>

```text
artifacts/dream_reports/dream_20260518T101930/best/paper.tex
artifacts/dream_reports/dream_20260518T101930/median/paper.tex
artifacts/dream_reports/dream_20260518T101930/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3764da52-0227-4199-afbb-cd06a7812415",
  "isSidechain": true,
  "promptId": "8fe5e53a-b377-47d8-9f45-301a1c07cb3d",
  "agentId": "a6477368b1ca31b25",
  "type": "user",
  "uuid": "5c4da8f1-9641-4385-9999-61faa1c9c801",
  "sourceToolAssistantUUID": "3764da52-0227-4199-afbb-cd06a7812415",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation",
  "sessionId": "421f26de-efdb-4f11-8ecd-7c2ad90d7f9f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-18T10:53:13.256Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01JXfDmxgbxmvmKbJ54KQwHa`</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c4da8f1-9641-4385-9999-61faa1c9c801",
  "isSidechain": true,
  "agentId": "a6477368b1ca31b25",
  "requestId": "req_011Cb9ugNXUDTY95eFKLBp7b",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9578708f-07b5-4397-9910-39f97fa140ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation",
  "sessionId": "421f26de-efdb-4f11-8ecd-7c2ad90d7f9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y17sT1Tmq479n8XhQwNGMu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10737,
      "cache_read_input_tokens": 18084,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10737,
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

_source line 19 · 2026-05-18T10:53:13.275Z_

<details><summary>↩ Tool result · `toolu_01JXfDmxgbxmvmKbJ54KQwHa`</summary>

```text
artifacts/dream_reports/dream_20260518T101930/best/paper.pdf
artifacts/dream_reports/dream_20260518T101930/median/paper.pdf
artifacts/dream_reports/dream_20260518T101930/worst/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9578708f-07b5-4397-9910-39f97fa140ca",
  "isSidechain": true,
  "promptId": "8fe5e53a-b377-47d8-9f45-301a1c07cb3d",
  "agentId": "a6477368b1ca31b25",
  "type": "user",
  "uuid": "cee8fa5a-b7ab-4e56-9d68-c86b4061fafb",
  "sourceToolAssistantUUID": "9578708f-07b5-4397-9910-39f97fa140ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation",
  "sessionId": "421f26de-efdb-4f11-8ecd-7c2ad90d7f9f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-18T10:53:14.230Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01EXhBZfBuKbbK1BeQddss1t`</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cee8fa5a-b7ab-4e56-9d68-c86b4061fafb",
  "isSidechain": true,
  "agentId": "a6477368b1ca31b25",
  "requestId": "req_011Cb9ugNXUDTY95eFKLBp7b",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e5946f86-6e08-4b93-9dd6-5efce4f3b82e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation",
  "sessionId": "421f26de-efdb-4f11-8ecd-7c2ad90d7f9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y17sT1Tmq479n8XhQwNGMu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10737,
      "cache_read_input_tokens": 18084,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10737,
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

_source line 21 · 2026-05-18T10:53:14.251Z_

<details><summary>↩ Tool result · `toolu_01EXhBZfBuKbbK1BeQddss1t`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e5946f86-6e08-4b93-9dd6-5efce4f3b82e",
  "isSidechain": true,
  "promptId": "8fe5e53a-b377-47d8-9f45-301a1c07cb3d",
  "agentId": "a6477368b1ca31b25",
  "type": "user",
  "uuid": "e9f20e68-38f8-4e0f-8c3d-33fbd7b74596",
  "sourceToolAssistantUUID": "e5946f86-6e08-4b93-9dd6-5efce4f3b82e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation",
  "sessionId": "421f26de-efdb-4f11-8ecd-7c2ad90d7f9f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-18T10:53:15.146Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01WfGKiohKmcsWfb86YD4QKJ`</summary>

```json
{
  "project": "goal_accessibility_preservation",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9f20e68-38f8-4e0f-8c3d-33fbd7b74596",
  "isSidechain": true,
  "agentId": "a6477368b1ca31b25",
  "requestId": "req_011Cb9ugNXUDTY95eFKLBp7b",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "978381db-a3db-4128-8aaf-2533a72d43f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation",
  "sessionId": "421f26de-efdb-4f11-8ecd-7c2ad90d7f9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y17sT1Tmq479n8XhQwNGMu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10737,
      "cache_read_input_tokens": 18084,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10737,
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

_source line 23 · 2026-05-18T10:53:15.158Z_

<details><summary>↩ Tool result · `toolu_01WfGKiohKmcsWfb86YD4QKJ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation/paper_framing.md\", \"content\": \"# Paper Framing — Goal Accessibility Preservation\\n\\n## Target Venue\\nARR October 2026 → NAACL 2027 (PRIMARY)\\n\\n## Title (Working)\\nTurn-Position Attention Bias: A Mechanism-Aware Fix for Multi-Turn Goal Accessibility Decline\\n\\n## Core Insight\\nMulti-turn GAR (Goal Accessibility Ratio) decline operates through two distinct mechanisms at different transformer layers:\\n- **Shallow layers (L0-5)**: softmax competition — as conversation grows, more tokens compete for attention mass, diluting goal-token attention regardless of Q-K alignment quality\\n- **Deep layers (L10+)**: Q-K geometric misalignment — query-key cosine similarity genuinely degrades with positional distance\\n\\nRoPE positional distance is NOT the driver of shallow-layer GAR decline (TB-RoPE compression yields +0.00pp, definitively falsified). The dominant mechanism is softmax dilution, which is orthogonal to positional encoding geometry.\\n\\n## Core Claims\\n\\n### Claim 1 (Analysis): Dual-Mechanism GAR Decline\\nMulti-turn GAR decline is driven by two distinct mechanisms stratified by layer depth. Shallow layers (L0-5) exhibit softmax-competition-driven decline where QKA barely changes (12%) while GAR drops 48-56%. Deep layers (L10+) show genuine Q-K geometric misalignment (QKA-GAR ρ > 0.8). This mechanistic stratification has not been reported in prior work.\\n\\n**Evidence needed**: Per-layer GAR + QKA analysis across multiple models (Qwen3-8B confirmed; need Llama-3-8B, Mistral-7B for generality). Fallback proxy analysis (4 Q/K metrics all fail at shallow layers).\\n\\n### Claim 2 (Negative Result): Position Distance is Not the Bottleneck\\nCompressing inter-turn RoPE positional distances (TB-RoPE) has zero measurable effect on GAR (+0.00pp with γ=0.7 compression). This falsifies the hypothesis that RoPE distance drives multi-turn attention decay, contradicting implications from \\\"When Attention Closes\\\" and \\\"Lost in the Middle at Birth\\\".\\n\\n**Evidence needed**: TB-RoPE-only (no training) showing +0.00pp across all layers and depths. TB-RoPE+LoRA showing no improvement. Multiple γ values if reviewers demand (but mechanism argument is stronger).\\n\\n### Claim 3 (Method): Turn-Position Attention Bias (TPAB)\\nA lightweight learnable bias in attention logits, indexed by turn position rather than token distance, directly counteracts softmax dilution at shallow layers. TPAB adds ~35K parameters (per-layer, per-head, per-turn-position bias), is FlashAttention-compatible, and improves both GAR and downstream task performance without single-turn regression.\\n\\n**Evidence needed**: GAR improvement > 5pp at depth 15+, task-level accuracy improvement, MMLU preservation, ablation (TPAB-only vs TPAB+LoRA vs LoRA-only).\\n\\n### Claim 4 (Generalization): Mechanism-Aware > Mechanism-Agnostic\\nTPAB (mechanism-aware, targeting softmax competition) outperforms mechanism-agnostic approaches: behavioral training (TurnWise, RLAAR), position modification (TB-RoPE), and general attention priors (temperature scaling). The advantage is because TPAB directly addresses the identified bottleneck.\\n\\n**Evidence needed**: Head-to-head comparison with baselines on both GAR and task metrics.\\n\\n## Anticipated Reviewer Concerns\\n\\n### C1: \\\"GAR improvement doesn't mean task performance improvement\\\"\\n**Response**: We include task-level evaluation (instruction following accuracy, extraction accuracy) alongside GAR. If GAR improves but tasks don't, we honestly report and discuss.\\n**Experiments**: Task accuracy evaluation on sharded simulation benchmark (6 task types).\\n\\n### C2: \\\"Only tested on one model (Qwen3-8B)\\\"\\n**Response**: Cross-model validation on Llama-3-8B and Mistral-7B for analysis claims. TPAB training on at least 2 model families.\\n**Experiments**: Multi-model GAR analysis + TPAB training.\\n\\n### C3: \\\"TPAB is just ALiBi/relative position bias with different indexing\\\"\\n**Response**: ALiBi is fixed linear decay by token distance; TPAB is learnable bias by turn structure. The motivation is fundamentally different (softmax competition at turn boundaries vs general recency bias). TPAB is mechanism-aware — designed from the dual-mechanism analysis, not a generic position bias.\\n**Experiments**: Ablation comparing TPAB vs ALiBi-style bias vs uniform bias.\\n\\n### C4: \\\"Training data is synthetic\\\"\\n**Response**: MVP uses synthetic data for controlled validation. Full experiments include real multi-turn data (ShareGPT, WildChat). HF benchmark (627 real conversations) used for evaluation.\\n**Experiments**: Train on real data, eval on both synthetic and real.\\n\\n### C5: \\\"How does this interact with longer context windows / different architectures?\\\"\\n**Response**: TPAB is architecture-agnostic (works on any transformer with softmax attention). Context length doesn't change the softmax competition mechanism — more tokens always dilute regardless of window size.\\n**Experiments**: Test at different context lengths if feasible.\\n\\n### C6: \\\"Why not just use attention-guided loss instead of bias?\\\"\\n**Response**: Attention-guided loss requires goal token labels and attention materialization (expensive, not FlashAttention-compatible). TPAB is label-free and kernel-compatible. We include attention-guided loss as an ablation to compare approaches.\\n\\n## Framing Risks (from Novelty Check)\\n\\n### Risk 1: GOAT Differentiation\\nGOAT (arXiv:2601.15380) uses learnable attention priors based on token position. Reviewers may view TPAB as \\\"GOAT at turn granularity\\\". Defense: TPAB's design is mechanistically motivated (softmax competition analysis), not a generic position bias. Related Work must explicitly compare: turn-level is not trivial coarsening of token-level because the mechanism (softmax dilution at turn boundaries) is structurally different from general recency bias.\\n\\n### Risk 2: \\\"When Attention Closes\\\" Priority\\nGAR definition and multi-turn attention decay diagnosis come from arXiv:2605.12922 (May 2026). We CANNOT claim \\\"discovering\\\" the problem. Our contribution is: (a) dual-mechanism analysis (softmax competition vs Q-K decay stratified by layer), (b) TB-RoPE falsification, (c) TPAB mechanism-aware intervention. Paper story is \\\"理解 → 解决\\\" not \\\"发现 → 理解 → 解决\\\".\\n\\n## Paper Structure Outline\\n1. Introduction: Multi-turn degradation problem → existing fixes treat symptoms → we identify root mechanism → propose mechanism-aware fix\\n2. Background: GAR definition, multi-turn attention decay, RoPE and softmax\\n3. Mechanism Analysis: Dual-mechanism discovery (shallow softmax competition + deep Q-K decay) + TB-RoPE negative result\\n4. Method: TPAB design motivated by mechanism analysis\\n5. Experiments: GAR evaluation + task-level evaluation + baselines + ablations\\n6. Analysis: Per-layer GAR visualization, bias parameter analysis, cross-model validation\\n7. Discussion & Limitations: Goal-stable scope, synthetic data, architecture specificity\\n\", \"total_chars\": 6796, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "978381db-a3db-4128-8aaf-2533a72d43f6",
  "isSidechain": true,
  "promptId": "8fe5e53a-b377-47d8-9f45-301a1c07cb3d",
  "agentId": "a6477368b1ca31b25",
  "type": "user",
  "uuid": "1f8c3741-028a-43f9-8acc-4ee02332800b",
  "sourceToolAssistantUUID": "978381db-a3db-4128-8aaf-2533a72d43f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation",
  "sessionId": "421f26de-efdb-4f11-8ecd-7c2ad90d7f9f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-18T10:53:15.732Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01RgujrV7d1cN67Z8bqQM1zb`</summary>

```json
{
  "project": "goal_accessibility_preservation",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f8c3741-028a-43f9-8acc-4ee02332800b",
  "isSidechain": true,
  "agentId": "a6477368b1ca31b25",
  "requestId": "req_011Cb9ugNXUDTY95eFKLBp7b",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3863b600-f33f-4aca-b462-726782907021",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation",
  "sessionId": "421f26de-efdb-4f11-8ecd-7c2ad90d7f9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y17sT1Tmq479n8XhQwNGMu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10737,
      "cache_read_input_tokens": 18084,
      "output_tokens": 473,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10737
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 473,
          "cache_read_input_tokens": 18084,
          "cache_creation_input_tokens": 10737,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10737,
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

_source line 25 · 2026-05-18T10:53:15.748Z_

<details><summary>↩ Tool result · `toolu_01RgujrV7d1cN67Z8bqQM1zb`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation/ROADMAP.md\", \"content\": \"# goal_accessibility_preservation — Research Dashboard\\n\\n> 最后更新: 2026-05-18 10:14 UTC | 更新原因: D003 pivot: TB-RoPE 证伪 → TPAB + Dual-Mechanism Analysis\\n\\n## 核心方向\\n**Pivot 后 (D003)**：Dual-Mechanism Analysis + Turn-Position Attention Bias (TPAB) 干预。\\n- 分析贡献：多轮 GAR 衰减的双重机制——浅层由 softmax 竞争驱动，深层由 Q-K 衰减驱动。RoPE 位置距离不是驱动因素（TB-RoPE +0.00pp 证伪）。\\n- 方法贡献：TPAB——在 attention logits 中加入 turn-position-indexed learnable bias，直接对抗 softmax 稀释。不需 goal token 标签，按 turn 结构索引。\\n- Paper story：发现 → 理解 → 解决。\\n\\n## 当前阶段\\n**MVP 验证（Pivot）** — TB-RoPE 假设被证伪，pivot 到 TPAB。需要新的 MVP 验证。\\n\\n## 历史实验总结\\n| ID | 结论 | 关键发现 |\\n|----|------|----------|\\n| mvp_a_gar_qka | GAR PASS, QKA FAIL | 浅层 softmax 竞争, 深层 Q-K 衰减 |\\n| fallback_proxy_test | NEGATIVE | 所有 Q/K 代理浅层 ρ<0.5 |\\n| mvp_b_tbrope_g07 | FAIL (+0.00pp) | RoPE 距离压缩对 GAR 零影响 |\\n\\n## 新 MVP: TPAB 概念验证\\n- 模型: Qwen3-8B\\n- 干预: per-layer per-head learnable bias，indexed by turn position (1-30)\\n- 训练: LoRA rank 32 + TPAB 参数，5K 合成多轮数据，next-token loss\\n- **Pass 标准**:\\n  - GAR improvement > 5pp at turn depth 15+（合成 + HF 双数据集）\\n  - **Task-level 验证**：multi-turn instruction following accuracy 提升（避免 GAR→performance 因果链缺口）\\n  - MMLU 退化 < 2pp\\n- **Fail**: pivot 到 attention-guided loss 或 analysis-only paper\\n- 预估: ~15-20 GPU-hours\\n\\n## 近期任务\\n- [ ] WebSearch 确认 TPAB novelty（\\\"learnable attention bias turn structure\\\"/\\\"GOAT attention priors\\\"）\\n- [ ] 实现 TPAB（per-layer per-head turn-position bias 参数）\\n- [ ] 设计 task-level evaluation（instruction following accuracy on multi-turn benchmark）\\n- [ ] 跑 TPAB MVP 训练 + 评估\\n- [ ] MMLU baseline 评估（正在运行中）\\n\\n## GPU 预算\\n- 项目分配: westb-40047 cuda:0 (RTX PRO 6000 96GB)\\n- 已用: MVP-A ~0.1h + MVP-B training ~2h + evals ~1h ≈ 3 GPU-hours\\n- Pivot MVP 预算: ~15-20 GPU-hours\\n- 全量预算: ~600 H100-hours\\n\\n## 目标会议\\n- PRIMARY: ARR October 2026 (DDL 2026-10-12)，21 周\\n- STRETCH: AAAI 2027 (DDL 2026-07-21/28)，9-10 周\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D003 | 2026-05-18 | Pivot 方向确定：Turn-Position Attention Bias (TPAB) + D | mvp_a_gar_qka, mvp_b_tbrope_g07, fallback_proxy_test |\\n| D002 | 2026-05-18 | MVP-B FAIL：TB-RoPE γ=0.7 对 GAR 零影响（+0.00pp TB-RoPE | mvp_b_tbrope_g07, mvp_a_gar_qka, fallback_proxy_test |\\n| D001 | 2026-05-18 | MVP-A 结果：GAR 衰减强复现 PASS，QKA 代理在 goal-critical laye | mvp_a_gar_qka |\\n\\n\\n\", \"total_chars\": 2232, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3863b600-f33f-4aca-b462-726782907021",
  "isSidechain": true,
  "promptId": "8fe5e53a-b377-47d8-9f45-301a1c07cb3d",
  "agentId": "a6477368b1ca31b25",
  "type": "user",
  "uuid": "faf85a0f-861e-4ad3-960b-fdedf1a9a376",
  "sourceToolAssistantUUID": "3863b600-f33f-4aca-b462-726782907021",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation",
  "sessionId": "421f26de-efdb-4f11-8ecd-7c2ad90d7f9f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-18T10:53:18.754Z_

Now let me read the actual paper tex file (the "best" version, which is the one under review).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "faf85a0f-861e-4ad3-960b-fdedf1a9a376",
  "isSidechain": true,
  "agentId": "a6477368b1ca31b25",
  "requestId": "req_011Cb9ugtk9wtMUEbT9UB8X3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0bee892d-f218-4ecc-b152-8fd3d756abfa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation",
  "sessionId": "421f26de-efdb-4f11-8ecd-7c2ad90d7f9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TQ8RcquSKGTMM2Nk8QhfRP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4192,
      "cache_read_input_tokens": 28821,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4192,
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

_source line 27 · 2026-05-18T10:53:19.408Z_

<details open><summary>🔧 Tool call — Read · `toolu_013wqBTe2pdRLxG3EtJcLzGY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation/artifacts/dream_reports/dream_20260518T101930/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0bee892d-f218-4ecc-b152-8fd3d756abfa",
  "isSidechain": true,
  "agentId": "a6477368b1ca31b25",
  "requestId": "req_011Cb9ugtk9wtMUEbT9UB8X3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "717e6267-6677-45cf-9ad2-c44abfc43a8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation",
  "sessionId": "421f26de-efdb-4f11-8ecd-7c2ad90d7f9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TQ8RcquSKGTMM2Nk8QhfRP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4192,
      "cache_read_input_tokens": 28821,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4192
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 124,
          "cache_read_input_tokens": 28821,
          "cache_creation_input_tokens": 4192,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4192,
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

_source line 28 · 2026-05-18T10:53:19.704Z_

<details><summary>↩ Tool result · `toolu_013wqBTe2pdRLxG3EtJcLzGY`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{times}
5	\usepackage{graphicx}
6	\usepackage{amsmath,amssymb}
7	\usepackage{booktabs}
8	\usepackage{multirow}
9	\usepackage{hyperref}
10	\usepackage[margin=2.5cm]{geometry}
11	\usepackage{xcolor}
12	\usepackage{caption}
13	\usepackage{subcaption}
14	
15	\newcommand{\tpab}{TPAB}
16	\newcommand{\gar}{GAR}
17	\newcommand{\pp}{pp}
18	
19	\title{Turn-Position Attention Bias: A Mechanism-Aware Fix\\for Multi-Turn Goal Accessibility Decline}
20	
21	\author{Anonymous}
22	\date{}
23	
24	\begin{document}
25	\maketitle
26	
27	% ============================================================
28	% ABSTRACT
29	% ============================================================
30	\begin{abstract}
31	Large Language Models (LLMs) progressively lose access to goal-relevant information as multi-turn conversations deepen, a phenomenon measured by Goal Accessibility Ratio (\gar{}).
32	We identify a dual-mechanism structure behind this decline: shallow transformer layers (L0--5) suffer from softmax competition, where growing token counts dilute attention mass regardless of query-key alignment quality, while deep layers (L10+) exhibit genuine query-key geometric misalignment (Pearson $\rho > 0.8$ between QKA and \gar{}).
33	This stratification replicates across Qwen3-8B, Llama-3-8B, and Mistral-7B, with shallow $\rho \in [0.26, 0.28]$ and deep $\rho \in [0.83, 0.87]$.
34	Motivated by this analysis, we propose Turn-Position Attention Bias (\tpab{}), a learnable per-layer, per-head, per-turn-position bias injected into attention logits before softmax.
35	\tpab{} adds only 35K parameters yet improves \gar{} by 7.22 percentage points (\pp{}) at depth 15 on Qwen3-8B and 6.13\pp{} on Llama-3-8B, translating to 3.8\% mean task accuracy improvement across six downstream tasks with only 0.3\pp{} MMLU regression.
36	\tpab{} outperforms mechanism-agnostic baselines including behavioral fine-tuning (+3.86\pp{} over TurnWise), temperature scaling (+3.92\pp{}), and ALiBi-style bias (+3.33\pp{}), while requiring 10$\times$ less training data.
37	A negative result on turn-boundary RoPE compression (+0.00\pp{}) rules out positional-encoding geometry as the bottleneck, strengthening the causal link between softmax dilution and the observed decline.
38	\end{abstract}
39	
40	% ============================================================
41	% 1. INTRODUCTION
42	% ============================================================
43	\section{Introduction}
44	
45	Multi-turn conversation is the dominant deployment mode for LLMs in assistants, customer service, and collaborative coding.
46	In these settings, the system prompt, user preferences, and task constraints are typically established in early turns and must remain accessible throughout the conversation.
47	Yet empirical evidence shows that LLMs progressively forget or ignore this goal-relevant information as conversation depth increases: a phenomenon we quantify through the Goal Accessibility Ratio (\gar{}), defined as the fraction of attention mass allocated to goal-turn tokens at generation time.
48	
49	The practical consequences are well documented: instruction drift, preference inconsistency, and constraint violations all worsen with conversation length.
50	Prior work has proposed mitigation strategies ranging from context compression to behavioral fine-tuning with turn-augmented data.
51	These approaches treat the symptom (degraded output quality) without diagnosing the mechanism (why attention to goal tokens declines in the first place).
52	Without mechanistic understanding, interventions are necessarily inefficient: they cannot target the specific architectural bottleneck responsible for the decline.
53	
54	We present a per-layer analysis of \gar{} decline across three model families (Qwen3-8B, Llama-3-8B, Mistral-7B) that reveals two distinct mechanisms stratified by layer depth.
55	At shallow layers (L0--5), \gar{} drops by 48--52\% from depth 5 to depth 25, yet query-key alignment (QKA) barely changes.
56	The cause is softmax competition: as token count grows, the softmax denominator increases, diluting per-token attention mass regardless of query-key similarity.
57	At deep layers (L10+), QKA and \gar{} are tightly correlated ($\rho > 0.83$), indicating genuine geometric misalignment between query and key representations for distant goal tokens.
58	This dual-mechanism stratification has not been reported in prior work on multi-turn attention dynamics.
59	
60	A critical negative result supports this diagnosis: compressing inter-turn RoPE positional distances (TB-RoPE) produces zero measurable \gar{} improvement (+0.00\pp{}).
61	This falsifies the hypothesis that positional-encoding geometry drives multi-turn attention decay, contradicting implications from recent position-bias analyses.
62	Since RoPE distance does not drive shallow-layer dilution, the bottleneck must lie in softmax normalization itself.
63	
64	We propose Turn-Position Attention Bias (\tpab{}), a lightweight intervention designed from this mechanistic understanding.
65	\tpab{} adds a learnable bias to attention logits, indexed by turn position rather than token distance, before softmax normalization.
66	With only 35K additional parameters (0.0004\% of model size), \tpab{} directly counteracts softmax dilution at shallow layers while remaining neutral for single-turn tasks (0.1\pp{} MMLU regression for \tpab{}-only).
67	Combined with LoRA for deep-layer correction, \tpab{}+LoRA achieves 7.22\pp{} \gar{} improvement at depth 15, translating to 3.8\% mean task accuracy gain across six task types.
68	
69	Our contributions are:
70	\begin{itemize}
71	    \item A dual-mechanism analysis of multi-turn \gar{} decline, identifying softmax competition (shallow layers) and Q-K misalignment (deep layers) as distinct bottlenecks, replicated across three model families (Section~\ref{sec:mechanism}).
72	    \item A negative result on TB-RoPE that rules out positional-encoding geometry as the driver of shallow-layer decline (Section~\ref{sec:mechanism}).
73	    \item \tpab{}, a mechanism-aware attention bias that improves \gar{} by 6--8\pp{} and task accuracy by 3--4\% with negligible single-turn regression (Section~\ref{sec:method},~\ref{sec:experiments}).
74	    \item Comprehensive ablations and baseline comparisons showing that mechanism-aware intervention (\tpab{}) outperforms mechanism-agnostic alternatives by 2--4\pp{} (Section~\ref{sec:ablations}).
75	\end{itemize}
76	
77	% ============================================================
78	% 2. BACKGROUND AND RELATED WORK
79	% ============================================================
80	\section{Background and Related Work}
81	
82	\paragraph{Multi-turn attention dynamics.}
83	Several studies have documented attention degradation in long conversations.
84	``Lost in the Middle'' showed that LLMs under-attend to information placed in the middle of long contexts, and subsequent work extended this finding to multi-turn settings where early-turn information becomes progressively less accessible.
85	Our work differs by decomposing this decline into layer-specific mechanisms rather than treating it as a monolithic phenomenon.
86	
87	\paragraph{Goal Accessibility Ratio.}
88	We define \gar{} as the mean attention weight assigned to goal-turn tokens (system prompt and initial user instruction) across all attention heads at the final generation position.
89	Formally, for a model with $L$ layers and $H$ heads per layer, and goal-turn token set $\mathcal{G}$:
90	\begin{equation}
91	\text{GAR} = \frac{1}{L \cdot H} \sum_{l=1}^{L} \sum_{h=1}^{H} \sum_{g \in \mathcal{G}} \alpha_{l,h}(t_{\text{gen}}, g)
92	\end{equation}
93	where $\alpha_{l,h}(t_{\text{gen}}, g)$ is the attention weight from the generation position to goal token $g$ at layer $l$, head $h$.
94	
95	\paragraph{Positional encoding and attention bias.}
96	RoPE encodes absolute position through rotation of query and key vectors, with relative distance determining the angle between them.
97	ALiBi adds a fixed linear penalty to attention logits proportional to token distance.
98	Both operate at the token level. \tpab{} differs by operating at the turn level with learned, layer-specific parameters.
99	
100	\paragraph{Multi-turn fine-tuning.}
101	TurnWise and related approaches use data augmentation (shuffled/inserted turns) to encourage robustness through behavioral training.
102	These methods do not modify the attention mechanism and require large augmented datasets (50K+ examples).
103	\tpab{} targets the architectural bottleneck directly, requiring only 5K training examples.
104	
105	% ============================================================
106	% 3. MECHANISM ANALYSIS
107	% ============================================================
108	\section{Mechanism Analysis}
109	\label{sec:mechanism}
110	
111	\subsection{Experimental Protocol}
112	
113	We measure per-layer \gar{} and query-key alignment (QKA, defined as mean cosine similarity between query vectors at generation position and key vectors at goal-token positions) across conversation depths 5, 15, and 25 on synthetic multi-turn benchmarks.
114	We compute the Pearson correlation $\rho$ between QKA and \gar{} across depth conditions for each layer group, partitioning layers into shallow (L0--5) and deep (L10+).
115	
116	\subsection{Dual-Mechanism Discovery}
117	
118	Table~\ref{tab:cross_model} presents the cross-model analysis.
119	All three model families exhibit a consistent stratification: shallow layers show low QKA-\gar{} correlation ($\rho \in [0.26, 0.28]$) while deep layers show high correlation ($\rho \in [0.83, 0.87]$).
120	The stratification boundary falls at approximately L6--L8 across all models.
121	
122	\begin{table}[t]
123	\centering
124	\caption{Dual-mechanism replication across three model families (extraction task). Shallow $\rho$ is mean Pearson correlation between QKA and \gar{} at layers L0--5; deep $\rho$ at L10+. Decline is \gar{} drop from depth 5 to 25.}
125	\label{tab:cross_model}
126	\small
127	\begin{tabular}{lcccccc}
128	\toprule
129	\textbf{Model} & \textbf{Params} & \textbf{Arch} & \textbf{Shallow $\rho$} & \textbf{Deep $\rho$} & \textbf{GAR\textsubscript{d5}} & \textbf{Decline} \\
130	\midrule
131	Qwen3-8B  & 8.2B & Dense RoPE   & 0.27 & 0.87 & 0.0499 & 48.5\% \\
132	Llama-3-8B & 8.0B & GQA RoPE     & 0.26 & 0.85 & 0.0465 & 50.3\% \\
133	Mistral-7B & 7.2B & GQA+SWA RoPE & 0.28 & 0.83 & 0.0512 & 51.6\% \\
134	\bottomrule
135	\end{tabular}
136	\end{table}
137	
138	\textbf{Shallow layers: softmax competition.}
139	At layers L0--5, \gar{} declines by 48--52\% from depth 5 to depth 25, yet QKA changes minimally.
140	The low $\rho$ ($\sim$0.27) indicates that the decline is not driven by query-key alignment degradation.
141	Instead, as conversation depth increases, the total number of tokens in the key set grows, and the softmax denominator increases proportionally.
142	This dilutes the attention mass allocated to any fixed set of goal tokens, regardless of how well their keys align with the query.
143	This is a mathematical property of softmax normalization: $\text{softmax}(z_i) = e^{z_i} / \sum_j e^{z_j}$ decreases for fixed $z_i$ as more terms enter the denominator.
144	
145	\textbf{Deep layers: Q-K geometric misalignment.}
146	At layers L10+, QKA and \gar{} are tightly coupled ($\rho > 0.83$).
147	Here the decline reflects genuine degradation of query-key similarity for distant goal tokens.
148	RoPE's rotation angle grows with positional distance, and deep-layer attention heads that have learned position-sensitive patterns cannot maintain alignment with tokens from early turns at large distances.
149	
150	\textbf{Mistral's sliding window attention} at layers L0--7 restricts the key set to a local window, partially mitigating dilution and producing marginally higher shallow $\rho$ (0.28 vs.\ 0.27 for Qwen3).
151	However, goal tokens from early turns fall outside the window at depths 15+, so \gar{} decline remains severe (51.6\%).
152	
153	\subsection{TB-RoPE Negative Result}
154	
155	To test whether RoPE positional distance drives the shallow-layer decline, we apply Turn-Boundary RoPE compression (TB-RoPE): compressing inter-turn positional distances by a factor $\gamma = 0.7$ while preserving intra-turn distances.
156	TB-RoPE produces +0.00\pp{} \gar{} change across all layers and depths on Qwen3-8B, with or without LoRA fine-tuning.
157	This definitively rules out positional-encoding geometry as the bottleneck.
158	The result is expected under the softmax-competition hypothesis: softmax dilution depends on the number of competing tokens, not their positional encoding.
159	
160	% ============================================================
161	% 4. METHOD
162	% ============================================================
163	\section{Method: Turn-Position Attention Bias}
164	\label{sec:method}
165	
166	\subsection{Design Motivation}
167	
168	The dual-mechanism analysis identifies softmax competition at shallow layers as the primary bottleneck.
169	A targeted fix must increase the pre-softmax logit for goal-turn tokens specifically at shallow layers, without disrupting the informative attention patterns at deep layers.
170	This motivates a learnable, layer-specific, turn-position-indexed bias.
171	
172	\subsection{Formulation}
173	
174	For layer $l$, head $h$, and a token belonging to turn $k$ (where $k=0$ is the goal turn), \tpab{} adds a bias $b_{l,h,k}$ to the attention logit before softmax:
175	\begin{equation}
176	\hat{\alpha}_{l,h}(i,j) = \frac{q_i^\top k_j}{\sqrt{d}} + b_{l,h,\tau(j)}
177	\end{equation}
178	where $\tau(j)$ returns the turn index of token $j$.
179	The bias tensor $\mathbf{B} \in \mathbb{R}^{L \times H \times K_{\max}}$ is initialized to zero and learned through standard next-token prediction loss.
180	For Qwen3-8B with $L=36$, $H=28$, and $K_{\max}=35$ turn positions, this adds $|B| = 36 \times 28 \times 35 = 35{,}280$ parameters.
181	
182	\subsection{Properties}
183	
184	\textbf{Single-turn neutrality.}
185	For single-turn inputs, all tokens share turn index $k=0$.
186	The bias reduces to a constant $b_{l,h,0}$ added to all logits, which cancels in softmax: $\text{softmax}(z + c) = \text{softmax}(z)$.
187	This guarantees zero interference with single-turn capability.
188	
189	\textbf{Complementarity with LoRA.}
190	\tpab{} targets shallow-layer softmax competition through additive bias, while LoRA modifies Q/K/V projections to improve deep-layer geometric alignment.
191	The two mechanisms address orthogonal bottlenecks and combine near-additively (Section~\ref{sec:component_ablation}).
192	
193	\textbf{FlashAttention compatibility.}
194	The bias is added to attention logits before the softmax kernel, requiring only a broadcasted addition to the score matrix.
195	This is compatible with FlashAttention's fused attention implementation, which already supports attention bias inputs.
196	
197	\subsection{Training}
198	
199	We train \tpab{}+LoRA (rank 32) jointly on 5K synthetic multi-turn conversations with standard next-token prediction loss.
200	The training objective does not require goal-token labels or attention materialization.
201	\tpab{} parameters receive gradients through the softmax path: $\partial \mathcal{L} / \partial b_{l,h,k}$ flows through the attention weights to the output.
202	
203	% ============================================================
204	% 5. EXPERIMENTS
205	% ============================================================
206	\section{Experiments}
207	\label{sec:experiments}
208	
209	\subsection{Setup}
210	
211	We evaluate on two benchmarks: (1)~a synthetic multi-turn benchmark with controlled conversation depths (5, 15, 25 turns) and two task types (extraction, reasoning), and (2)~417 real conversations from HuggingFace dialogue datasets.
212	All experiments use a single A100-80GB GPU.
213	Baselines include the unmodified base model, LoRA-only (rank 32), and TurnWise (LoRA on 50K turn-augmented data).
214	
215	\subsection{TPAB GAR Results}
216	
217	Table~\ref{tab:tpab_gar} presents \tpab{}+LoRA \gar{} improvement on Qwen3-8B.
218	At depth 5, improvement is minimal (+0.22\pp{} extraction) because softmax dilution is not yet severe.
219	At depths 15 and 25, \tpab{} achieves 7.22\pp{} and 8.50\pp{} improvement respectively for extraction, and 6.50\pp{} and 7.80\pp{} for reasoning.
220	On real conversations, improvement is 5.20\pp{}, smaller than synthetic due to variable turn lengths and mixed depths.
221	
222	\begin{table}[t]
223	\centering
224	\caption{\tpab{}+LoRA \gar{} improvement on Qwen3-8B (synthetic benchmark). $\Delta$ in percentage points.}
225	\label{tab:tpab_gar}
226	\small
227	\begin{tabular}{lcccr}
228	\toprule
229	\textbf{Task} & \textbf{Depth} & \textbf{Baseline} & \textbf{TPAB+LoRA} & \textbf{$\Delta$\pp{}} \\
230	\midrule
231	Extraction & 5  & 0.0499 & 0.0521 & +0.22 \\
232	Extraction & 15 & 0.0353 & 0.1075 & +7.22 \\
233	Extraction & 25 & 0.0257 & 0.1107 & +8.50 \\
234	\midrule
235	Reasoning  & 5  & 0.0374 & 0.0398 & +0.24 \\
236	Reasoning  & 15 & 0.0174 & 0.0824 & +6.50 \\
237	Reasoning  & 25 & 0.0163 & 0.0943 & +7.80 \\
238	\bottomrule
239	\end{tabular}
240	\end{table}
241	
242	\subsection{Cross-Model Generalization}
243	
244	Table~\ref{tab:cross_model_tpab} shows \tpab{} generalizes to Llama-3-8B.
245	Improvement on Llama-3 (6.13\pp{} at d15) is slightly smaller than Qwen3 (7.22\pp{}) due to Llama-3's grouped-query attention constraining per-head bias adaptation.
246	MMLU regression is identical (0.3\pp{}) across both models, consistent with the single-turn neutrality property.
247	
248	\begin{table}[t]
249	\centering
250	\caption{Cross-model \tpab{}+LoRA results. All metrics on extraction task.}
251	\label{tab:cross_model_tpab}
252	\small
253	\begin{tabular}{lcccccc}
254	\toprule
255	\textbf{Model} & \textbf{d15 Base} & \textbf{d15 TPAB} & \textbf{$\Delta$d15} & \textbf{$\Delta$d25} & \textbf{HF $\Delta$} & \textbf{MMLU $\Delta$} \\
256	\midrule
257	Qwen3-8B  & 0.0353 & 0.1075 & +7.22 & +8.50 & +5.20 & $-$0.3 \\
258	Llama-3-8B & 0.0328 & 0.0941 & +6.13 & +6.61 & +4.52 & $-$0.3 \\
259	\bottomrule
260	\end{tabular}
261	\end{table}
262	
263	\subsection{Task-Level Accuracy}
264	
265	Table~\ref{tab:task_acc} evaluates whether \gar{} improvement translates to downstream task performance.
266	Across six task types at depth 15, \tpab{}+LoRA achieves 3.7\% mean accuracy improvement.
267	Tasks that depend most directly on goal-token access (instruction recall: +4.6\%, constraint following: +4.4\%) benefit most.
268	Context grounding, which requires distributed multi-turn integration rather than goal-token access, shows the smallest gain (+2.6\%).
269	The Pearson correlation between per-task \gar{} improvement and accuracy improvement is $r = 0.84$.
270	
271	\begin{table}[t]
272	\centering
273	\caption{Task-level accuracy at depth 15: baseline vs.\ \tpab{}+LoRA on Qwen3-8B.}
274	\label{tab:task_acc}
275	\small
276	\begin{tabular}{lcccc}
277	\toprule
278	\textbf{Task} & \textbf{Base Acc} & \textbf{TPAB Acc} & \textbf{$\Delta$\%} & \textbf{GAR $\Delta$\pp{}} \\
279	\midrule
280	Instruction recall      & 71.2 & 75.8 & +4.6 & +8.1 \\
281	Entity extraction       & 64.8 & 68.3 & +3.5 & +7.2 \\
282	Multi-step reasoning    & 58.3 & 61.7 & +3.4 & +6.8 \\
283	Preference consistency  & 67.5 & 71.2 & +3.7 & +7.0 \\
284	Constraint following    & 69.1 & 73.5 & +4.4 & +7.5 \\
285	Context grounding       & 62.4 & 65.0 & +2.6 & +5.9 \\
286	\midrule
287	\textbf{Mean}           & 65.6 & 69.3 & +3.7 & +7.1 \\
288	\bottomrule
289	\end{tabular}
290	\end{table}
291	
292	\subsection{MMLU Preservation}
293	
294	Table~\ref{tab:mmlu} confirms that \tpab{} does not degrade single-turn capability.
295	\tpab{}-only regression is 0.1\pp{}, consistent with the theoretical prediction of single-turn neutrality.
296	The 0.3\pp{} total regression of \tpab{}+LoRA originates from the LoRA component and falls within standard evaluation noise ($\pm$0.2--0.4\pp{} across random seeds).
297	
298	\begin{table}[t]
299	\centering
300	\caption{MMLU 5-shot accuracy across configurations on Qwen3-8B.}
301	\label{tab:mmlu}
302	\small
303	\begin{tabular}{lcccccr}
304	\toprule
305	\textbf{Method} & \textbf{Overall} & \textbf{STEM} & \textbf{Human.} & \textbf{Soc.Sci} & \textbf{Other} & \textbf{$\Delta$} \\
306	\midrule
307	Qwen3-8B base & 72.1 & 68.4 & 74.3 & 76.8 & 69.1 & -- \\
308	TPAB-only     & 72.0 & 68.3 & 74.2 & 76.7 & 69.0 & $-$0.1 \\
309	LoRA-only     & 71.7 & 68.0 & 73.9 & 76.5 & 68.7 & $-$0.4 \\
310	TPAB+LoRA     & 71.8 & 68.2 & 74.0 & 76.5 & 68.9 & $-$0.3 \\
311	\bottomrule
312	\end{tabular}
313	\end{table}
314	
315	\subsection{Comparison with Mechanism-Agnostic Baselines}
316	
317	Table~\ref{tab:baselines} compares \tpab{} with TurnWise, a mechanism-agnostic baseline that uses LoRA fine-tuning on 50K turn-augmented examples.
318	TurnWise achieves 3.36\pp{} \gar{} improvement at depth 15, comparable to LoRA-only (3.58\pp{}), suggesting that turn augmentation provides minimal additional benefit beyond standard fine-tuning.
319	\tpab{}+LoRA outperforms TurnWise by 3.86\pp{} at d15 and 4.95\pp{} at d25, while using 10$\times$ less training data and 4$\times$ less compute.
320	
321	\begin{table}[t]
322	\centering
323	\caption{Comparison with mechanism-agnostic baselines on Qwen3-8B.}
324	\label{tab:baselines}
325	\small
326	\begin{tabular}{lcccccc}
327	\toprule
328	\textbf{Method} & \textbf{Data} & \textbf{Hours} & \textbf{d15 $\Delta$} & \textbf{d25 $\Delta$} & \textbf{Task $\Delta$} & \textbf{MMLU} \\
329	\midrule
330	TPAB+LoRA     & 5K synth  & 2.1 & +7.22 & +8.50 & +3.8\% & $-$0.3 \\
331	TurnWise+LoRA & 50K aug   & 8.5 & +3.36 & +3.55 & +1.8\% & $-$0.7 \\
332	LoRA-only     & 5K synth  & 1.9 & +3.58 & +3.97 & +1.5\% & $-$0.4 \\
333	\bottomrule
334	\end{tabular}
335	\end{table}
336	
337	% ============================================================
338	% 6. ABLATIONS
339	% ============================================================
340	\section{Ablation Studies}
341	\label{sec:ablations}
342	
343	\subsection{Component Ablation: TPAB vs.\ LoRA}
344	\label{sec:component_ablation}
345	
346	Table~\ref{tab:component} isolates the contributions of \tpab{} and LoRA.
347	\tpab{}-only (35K params) achieves 3.81\pp{} at d15, concentrated at shallow layers (4.82\pp{} shallow lift vs.\ 0.91\pp{} deep lift).
348	LoRA-only (30.67M params) achieves a similar aggregate (3.58\pp{}) but through deep-layer improvement (2.87\pp{} deep lift vs.\ 1.23\pp{} shallow lift).
349	The combined model achieves 7.22\pp{}, near the sum of individual contributions (3.81 + 3.58 = 7.39), confirming that the two components target orthogonal mechanisms.
350	\tpab{}-only matches LoRA-only's \gar{} improvement with 870$\times$ fewer parameters.
351	
352	\begin{table}[t]
353	\centering
354	\caption{Component ablation on Qwen3-8B. Shallow/deep lift measured at L0--5 and L10+ respectively.}
355	\label{tab:component}
356	\small
357	\begin{tabular}{lcccccr}
358	\toprule
359	\textbf{Method} & \textbf{Params} & \textbf{d15 $\Delta$} & \textbf{d25 $\Delta$} & \textbf{HF $\Delta$} & \textbf{Shallow} & \textbf{Deep} \\
360	\midrule
361	Baseline   & --     & --   & --   & --   & --   & -- \\
362	TPAB-only  & 35.3K  & +3.81 & +4.55 & +3.49 & +4.82 & +0.91 \\
363	LoRA-only  & 30.67M & +3.58 & +3.97 & +3.14 & +1.23 & +2.87 \\
364	TPAB+LoRA  & 30.70M & +7.22 & +8.50 & +5.20 & +6.10 & +3.41 \\
365	\bottomrule
366	\end{tabular}
367	\end{table}
368	
369	\subsection{Bias Design Ablation}
370	
371	Table~\ref{tab:bias_design} compares four bias designs at the same attention logit injection point.
372	Learned \tpab{} outperforms all fixed alternatives.
373	The 3.33\pp{} gap over ALiBi-style bias addresses the concern that \tpab{} is merely ALiBi with turn-level indexing: ALiBi applies a fixed linear penalty by token distance, while \tpab{} learns layer-specific, head-specific biases adapted to the dual-mechanism structure.
374	Analysis of the learned bias values reveals that shallow layers learn larger biases (mean 0.94) than deep layers (mean 0.31), with substantial per-head variance (std 0.28), confirming that a fixed schedule cannot capture this structure.
375	
376	\begin{table}[t]
377	\centering
378	\caption{Bias design comparison (all with LoRA rank 32 on Qwen3-8B). $\Delta$ in \pp{}.}
379	\label{tab:bias_design}
380	\small
381	\begin{tabular}{lccccr}
382	\toprule
383	\textbf{Bias Design} & \textbf{Learned} & \textbf{Params} & \textbf{d15 $\Delta$} & \textbf{d25 $\Delta$} & \textbf{HF $\Delta$} \\
384	\midrule
385	TPAB (learned)       & Yes & 35.3K & +7.22 & +8.50 & +5.20 \\
386	Fixed linear decay   & No  & 0     & +4.63 & +5.18 & +3.47 \\
387	ALiBi-style (turn)   & No  & 0     & +3.89 & +4.11 & +2.91 \\
388	Uniform (+const)     & No  & 0     & +4.21 & +4.67 & +3.12 \\
389	No bias (LoRA-only)  & --  & 0     & +3.58 & +3.97 & +3.14 \\
390	\bottomrule
391	\end{tabular}
392	\end{table}
393	
394	\subsection{Temperature Scaling}
395	
396	Temperature scaling at shallow layers provides an independent test of the softmax competition hypothesis: if softmax dilution causes the decline, sharper attention ($\tau < 1$) should partially recover \gar{}.
397	Table~\ref{tab:temperature} confirms this prediction.
398	However, temperature scaling is a blunt instrument.
399	At $\tau = 0.5$, shallow-layer \gar{} improves by 3.14\pp{}, but MMLU regresses by 1.8\pp{} and perplexity increases by 4.2\% because sharpening affects all tokens, not just goal tokens.
400	Learned temperature improves the trade-off (3.30\pp{} \gar{}, 1.2\pp{} MMLU regression) but remains 3.92\pp{} below \tpab{} at d15.
401	\tpab{} achieves a 2.7$\times$ better efficiency ratio (\gar{} gain per unit MMLU regression) because it selectively boosts goal-turn tokens rather than globally sharpening attention.
402	
403	\begin{table}[t]
404	\centering
405	\caption{Softmax temperature scaling vs.\ \tpab{} (all with LoRA rank 32 on Qwen3-8B).}
406	\label{tab:temperature}
407	\small
408	\begin{tabular}{lcccc}
409	\toprule
410	\textbf{Method} & \textbf{d15 $\Delta$\pp{}} & \textbf{Shallow $\Delta$} & \textbf{MMLU $\Delta$} & \textbf{PPL $\Delta$} \\
411	\midrule
412	$\tau$=0.8 (L0--5)     & +1.93 & +2.01 & $-$0.6\% & +1.8\% \\
413	$\tau$=0.5 (L0--5)     & +2.65 & +3.14 & $-$1.8\% & +4.2\% \\
414	$\tau$=learned (L0--5)  & +3.30 & +3.52 & $-$1.2\% & +2.9\% \\
415	TPAB (learned bias)     & +7.22 & +6.10 & $-$0.3\% & +0.4\% \\
416	\bottomrule
417	\end{tabular}
418	\end{table}
419	
420	\subsection{Training Data Ablation}
421	
422	Table~\ref{tab:train_data} compares synthetic and real training data for \tpab{}.
423	Real-data training (3K ShareGPT + 2K WildChat) improves HF real-conversation \gar{} by 1.12\pp{} over synthetic-trained \tpab{}, reaching 6.32\pp{} total improvement.
424	On the synthetic benchmark, real-trained performance is slightly lower ($-$0.37\pp{} at d15), reflecting expected distribution mismatch.
425	The result indicates that even synthetic training achieves strong gains, lowering the barrier to \tpab{} adoption.
426	
427	\begin{table}[t]
428	\centering
429	\caption{Training data ablation for \tpab{}+LoRA on Qwen3-8B.}
430	\label{tab:train_data}
431	\small
432	\begin{tabular}{lcccc}
433	\toprule
434	\textbf{Training Data} & \textbf{Synth d15} & \textbf{Synth d25} & \textbf{HF GAR} & \textbf{HF $\Delta$\pp{}} \\
435	\midrule
436	Synthetic 5K              & 0.1075 & 0.1107 & 0.0974 & +5.20 \\
437	Real 5K (ShareGPT+WildChat) & 0.1038 & 0.1052 & 0.1086 & +6.32 \\
438	Baseline (no training)    & 0.0353 & 0.0257 & 0.0454 & -- \\
439	\bottomrule
440	\end{tabular}
441	\end{table}
442	
443	% ============================================================
444	% 7. DISCUSSION AND CONCLUSION
445	% ============================================================
446	\section{Discussion}
447	
448	\paragraph{Why mechanism-aware intervention works.}
449	The component ablation (Table~\ref{tab:component}) provides the clearest evidence: \tpab{} and LoRA improve \gar{} through different layer groups, and their benefits combine near-additively.
450	This orthogonality is a direct consequence of the dual-mechanism structure.
451	Mechanism-agnostic approaches like TurnWise cannot exploit this structure because they apply uniform training signal across all layers, diluting the intervention where it matters most.
452	
453	\paragraph{Practical implications.}
454	\tpab{} requires only 35K additional parameters, trains in 2.1 GPU-hours on 5K examples, and causes negligible single-turn regression.
455	These properties make it practical for production deployment: the bias tensor can be stored alongside existing LoRA adapters, and the inference overhead is a single broadcasted addition per layer.
456	
457	\paragraph{Limitations.}
458	Our evaluation covers three 7--8B parameter models.
459	Whether the dual-mechanism pattern and \tpab{} benefits extend to larger models (70B+) or different architectures (Mamba, RWKV) remains open.
460	The synthetic benchmark, while controlled, may not capture all patterns of real multi-turn degradation.
461	\tpab{} targets goal-token accessibility specifically; it does not address other multi-turn challenges such as contradiction resolution or topic coherence.
462	
463	\section{Conclusion}
464	
465	We identified a dual-mechanism structure in multi-turn \gar{} decline: softmax competition at shallow layers and Q-K geometric misalignment at deep layers.
466	This finding, replicated across Qwen3-8B, Llama-3-8B, and Mistral-7B, provides the foundation for \tpab{}, a mechanism-aware attention bias that directly counteracts softmax dilution.
467	\tpab{}+LoRA achieves 7.22\pp{} \gar{} improvement and 3.8\% task accuracy gain on Qwen3-8B with 0.3\pp{} MMLU regression, outperforming all mechanism-agnostic baselines while requiring minimal additional parameters and compute.
468	The TB-RoPE negative result (+0.00\pp{}) strengthens the causal argument by ruling out positional-encoding geometry as the bottleneck.
469	These results demonstrate that mechanistic understanding of attention dynamics enables more efficient and targeted interventions for multi-turn LLM deployment.
470	
471	\bibliographystyle{plain}
472	
473	\end{document}
474	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "717e6267-6677-45cf-9ad2-c44abfc43a8d",
  "isSidechain": true,
  "promptId": "8fe5e53a-b377-47d8-9f45-301a1c07cb3d",
  "agentId": "a6477368b1ca31b25",
  "type": "user",
  "uuid": "4f6acb68-63dc-4670-bd43-181aea28f680",
  "sourceToolAssistantUUID": "717e6267-6677-45cf-9ad2-c44abfc43a8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation",
  "sessionId": "421f26de-efdb-4f11-8ecd-7c2ad90d7f9f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-18T10:53:23.756Z_

Now let me also look at the other paper versions (median and worst) for comparison, and check the decisions.yaml for context on how the paper was constructed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f6acb68-63dc-4670-bd43-181aea28f680",
  "isSidechain": true,
  "agentId": "a6477368b1ca31b25",
  "requestId": "req_011Cb9uhBTjr9YxHZ2MpmoYb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "94b9ab82-ef93-431a-a387-16a45abc093d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation",
  "sessionId": "421f26de-efdb-4f11-8ecd-7c2ad90d7f9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QgbZjiAg55kS7Lq8uBLLCP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10757,
      "cache_read_input_tokens": 33013,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10757,
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

_source line 30 · 2026-05-18T10:53:24.730Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_015GphJb2gpdcrUPpbvx6VX2`</summary>

```json
{
  "project": "goal_accessibility_preservation",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94b9ab82-ef93-431a-a387-16a45abc093d",
  "isSidechain": true,
  "agentId": "a6477368b1ca31b25",
  "requestId": "req_011Cb9uhBTjr9YxHZ2MpmoYb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6db8491f-34f5-4771-9ba3-089223bbfcbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation",
  "sessionId": "421f26de-efdb-4f11-8ecd-7c2ad90d7f9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QgbZjiAg55kS7Lq8uBLLCP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10757,
      "cache_read_input_tokens": 33013,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10757,
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

_source line 31 · 2026-05-18T10:53:24.746Z_

<details><summary>↩ Tool result · `toolu_015GphJb2gpdcrUPpbvx6VX2`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation/decisions.yaml\", \"content\": \"_next_id: 4\\ndecisions:\\n- id: D001\\n  date: 2026-05-18 06:40 UTC\\n  summary: MVP-A 结果：GAR 衰减强复现 PASS，QKA 代理在 goal-critical layers FAIL（结构性原因：softmax\\n    竞争而非 Q-K 失配）。调整策略：TB-RoPE 仍推进（直接 GAR 验证），QKA Loss 降级为上层辅助信号，fallback 代理快速测试但预期同样受限。\\n  rationale: MVP-A 数据：GAR decline 48.5%/56.4%（远超 20% 阈值）。QKA-GAR ρ at goal-critical\\n    layers (L1-L6) 仅 0.22-0.30，L4/L5 甚至为负。但上层 (L10+) ρ > 0.8。QKA 本身仅下降 12% 而 GAR 下降\\n    48-56%，说明早期层 GAR 衰减主要由 softmax token 竞争驱动，非 Q-K 几何问题。TB-RoPE 压缩位置距离同时影响 softmax\\n    竞争和 Q-K 对齐，无需 QKA 代理即可验证（直接测 GAR）。QKA Loss 在 goal-critical layers 从原理上无法捕捉 GAR\\n    改善，降级为上层 (L10+) 辅助 loss。这使方法更聚焦（TB-RoPE 为核心），论文 story 更清晰。\\n  related_experiments:\\n  - exp_id: mvp_a_gar_qka\\n    role: primary evidence\\n    result: GAR decline PASS, QKA proxy FAIL at goal-critical layers\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-18 10:08 UTC\\n  summary: MVP-B FAIL：TB-RoPE γ=0.7 对 GAR 零影响（+0.00pp TB-RoPE-only, -0.25pp +LoRA）。跳过\\n    γ=0.5/0.9（位置压缩本身无效，换 γ 无意义）。核心假设\\\"RoPE 距离驱动 GAR 衰减\\\"被证伪。启动方法 pivot。\\n  rationale: '三次实验收敛到同一结论：(1) MVP-A: QKA 代理在浅层失效→softmax 竞争而非 Q-K 失配；(2) Fallback:\\n    所有 Q/K 代理浅层 ρ<0.5；(3) MVP-B: TB-RoPE-only +0.00pp→位置距离根本不是 GAR 瓶颈。TB-RoPE-only\\n    在推理时零效果是决定性证据——不是训练不够，是机制不对。继续测 γ=0.5/0.9 是浪费 GPU。项目不终止：dual-mechanism 分析发现有论文价值（浅层\\n    softmax 竞争 + 深层 Q-K 衰减），需要 pivot 到直接攻击 softmax 竞争的干预方法。'\\n  related_experiments:\\n  - exp_id: mvp_b_tbrope_g07\\n    role: primary evidence\\n    result: GAR +0.00pp (TB-RoPE-only), -0.25pp (TB-RoPE+LoRA), FAIL\\n  - exp_id: mvp_a_gar_qka\\n    role: supporting evidence\\n    result: QKA proxy FAIL at goal-critical layers\\n  - exp_id: fallback_proxy_test\\n    role: supporting evidence\\n    result: All Q/K proxies FAIL at shallow layers\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-18 10:14 UTC\\n  summary: Pivot 方向确定：Turn-Position Attention Bias (TPAB) + Dual-Mechanism Analysis。Paper\\n    story = 机制分析（浅层 softmax 竞争 + 深层 Q-K 衰减）+ mechanism-aware 干预（turn-position bias\\n    对抗 softmax 稀释）。Temperature scaling 作 ablation，Wang et al. 作 baseline。\\n  rationale: Reviewer 评估 5 个方向后排序：TPAB+Analysis > Attention-guided loss > Analysis-only\\n    > Temperature > Wang et al.。TPAB 最优因为：(1) 直接对抗已识别机制（softmax 竞争）；(2) 不需 goal token\\n    标签（按 turn 位置索引）；(3) 实现极轻量（per-layer/head 小参数）；(4) 与 ALiBi/GOAT 有清晰区分（turn-level\\n    结构 vs token-level 距离）。论文合并 analysis+intervention 给出完整 story：\\\"发现 → 理解 → 解决\\\"。Attention-guided\\n    loss 作为补充备选，不先做（实践障碍多）。关键元风险：GAR→task performance 因果链未验证，pivot 实验必须包含 task-level\\n    评估。\\n  related_experiments:\\n  - exp_id: mvp_a_gar_qka\\n    role: mechanism evidence\\n    result: dual-mechanism discovery\\n  - exp_id: mvp_b_tbrope_g07\\n    role: falsification\\n    result: position compression zero effect\\n  - exp_id: fallback_proxy_test\\n    role: mechanism evidence\\n    result: all Q/K proxies fail at shallow layers\\n  depends_on:\\n  - D001\\n  - D002\\n\", \"total_chars\": 2787, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6db8491f-34f5-4771-9ba3-089223bbfcbc",
  "isSidechain": true,
  "promptId": "8fe5e53a-b377-47d8-9f45-301a1c07cb3d",
  "agentId": "a6477368b1ca31b25",
  "type": "user",
  "uuid": "33374bae-8b85-4bf4-b00b-0ab03da4ddb5",
  "sourceToolAssistantUUID": "6db8491f-34f5-4771-9ba3-089223bbfcbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation",
  "sessionId": "421f26de-efdb-4f11-8ecd-7c2ad90d7f9f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-18T10:53:26.251Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01KkjXsQzNeAYcjX4KjiDVFP`</summary>

```json
{
  "pattern": "**/dream_*/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation/artifacts/dream_reports"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33374bae-8b85-4bf4-b00b-0ab03da4ddb5",
  "isSidechain": true,
  "agentId": "a6477368b1ca31b25",
  "requestId": "req_011Cb9uhBTjr9YxHZ2MpmoYb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cbccd49e-475a-46ed-820f-c0c5298bcad8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation",
  "sessionId": "421f26de-efdb-4f11-8ecd-7c2ad90d7f9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QgbZjiAg55kS7Lq8uBLLCP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10757,
      "cache_read_input_tokens": 33013,
      "output_tokens": 229,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10757
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 229,
          "cache_read_input_tokens": 33013,
          "cache_creation_input_tokens": 10757,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10757,
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

_source line 33 · 2026-05-18T10:53:26.290Z_

<details><summary>↩ Tool result · `toolu_01KkjXsQzNeAYcjX4KjiDVFP`</summary>

```text
artifacts/dream_reports/dream_20260518T101930/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260518T101930/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260518T101930/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260518T101930/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260518T101930/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260518T101930/best/experiment_data.json
artifacts/dream_reports/dream_20260518T101930/best/paper_framing.md
artifacts/dream_reports/dream_20260518T101930/best/paper.tex
artifacts/dream_reports/dream_20260518T101930/best/paper.aux
artifacts/dream_reports/dream_20260518T101930/best/paper.out
artifacts/dream_reports/dream_20260518T101930/best/paper.pdf
artifacts/dream_reports/dream_20260518T101930/best/paper.log
artifacts/dream_reports/dream_20260518T101930/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260518T101930/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260518T101930/median/experiment_data.json
artifacts/dream_reports/dream_20260518T101930/median/paper_framing.md
artifacts/dream_reports/dream_20260518T101930/median/paper.tex
artifacts/dream_reports/dream_20260518T101930/median/paper.aux
artifacts/dream_reports/dream_20260518T101930/median/paper.out
artifacts/dream_reports/dream_20260518T101930/median/paper.pdf
artifacts/dream_reports/dream_20260518T101930/median/paper.log
artifacts/dream_reports/dream_20260518T101930/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260518T101930/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260518T101930/worst/experiment_data.json
artifacts/dream_reports/dream_20260518T101930/worst/paper_framing.md
artifacts/dream_reports/dream_20260518T101930/worst/paper.tex
artifacts/dream_reports/dream_20260518T101930/worst/paper.aux
artifacts/dream_reports/dream_20260518T101930/worst/paper.out
artifacts/dream_reports/dream_20260518T101930/worst/paper.pdf
artifacts/dream_reports/dream_20260518T101930/worst/paper.log
artifacts/dream_reports/dream_20260518T101930/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260518T101930/logs/orchestrator.log
artifacts/dream_reports/dream_20260518T101930/best/review_context.yaml
artifacts/dream_reports/dream_20260518T101930/logs/review_best.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cbccd49e-475a-46ed-820f-c0c5298bcad8",
  "isSidechain": true,
  "promptId": "8fe5e53a-b377-47d8-9f45-301a1c07cb3d",
  "agentId": "a6477368b1ca31b25",
  "type": "user",
  "uuid": "916d37f5-557e-443f-8fae-51e5a2c1ffc0",
  "sourceToolAssistantUUID": "cbccd49e-475a-46ed-820f-c0c5298bcad8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation",
  "sessionId": "421f26de-efdb-4f11-8ecd-7c2ad90d7f9f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-18T10:53:29.465Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CPnCfANhv1cvV24d8DjBLz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation/artifacts/dream_reports/dream_20260518T101930/best/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "916d37f5-557e-443f-8fae-51e5a2c1ffc0",
  "isSidechain": true,
  "agentId": "a6477368b1ca31b25",
  "requestId": "req_011Cb9uhfdPjEjrHbwcXeLpt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b40339ba-86ea-4748-839d-40ff5d27030f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation",
  "sessionId": "421f26de-efdb-4f11-8ecd-7c2ad90d7f9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NarU3ungDXV3tGnPV2aAMx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2799,
      "cache_read_input_tokens": 43770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2799,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 73,
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

_source line 35 · 2026-05-18T10:53:29.756Z_

<details><summary>↩ Tool result · `toolu_01CPnCfANhv1cvV24d8DjBLz`</summary>

```text
1	tier: best
2	narrative_guidance: 'Full four-claim story stands. TPAB mechanism hypothesis fully
3	  validated: learnable turn-position bias effectively counteracts shallow-layer softmax
4	  dilution, GAR gains causally translate to task performance, and dual-mechanism analysis
5	  generalizes across Qwen3-8B / Llama-3-8B / Mistral-7B. TB-RoPE negative result strengthens
6	  causal argument by ruling out position-encoding geometry as bottleneck. TPAB outperforms
7	  all mechanism-agnostic baselines on both GAR and task metrics with negligible MMLU
8	  regression. Paper title keeps ''mechanism-aware fix''; dual-mechanism stratification
9	  is novel contribution. Strong NAACL main conference paper with analysis depth +
10	  practical method + negative result as evidence.
11	
12	  '
13	imagined_experiments:
14	- name: Dual-mechanism analysis on Llama-3-8B
15	  plan_id: analysis_cross_model_llama
16	  description: 'Replicate per-layer GAR + QKA correlation analysis on Llama-3-8B (32
17	    layers, GQA, RoPE). Run extraction and reasoning tasks at depths 5/15/25 on synthetic
18	    data. Compute per-layer Pearson ρ(QKA, GAR) to verify shallow softmax-competition
19	    vs deep Q-K misalignment stratification.
20	
21	    '
22	  expected_results:
23	    extraction_gar_d5: 0.0465
24	    extraction_gar_d15: 0.0328
25	    extraction_gar_d25: 0.0231
26	    extraction_gar_decline_pct: 50.3
27	    reasoning_gar_d5: 0.0351
28	    reasoning_gar_d15: 0.0162
29	    reasoning_gar_d25: 0.0148
30	    reasoning_gar_decline_pct: 57.8
31	    shallow_qka_gar_rho_mean_L0_L5: 0.26
32	    deep_qka_gar_rho_mean_L10_plus: 0.85
33	    extraction_max_layer_rho: 0.88
34	    extraction_max_layer_rho_layer: L12_d25
35	    reasoning_max_layer_rho: 0.9
36	    reasoning_max_layer_rho_layer: L16_d5
37	    layers_with_rho_gt_0.8:
38	    - L12
39	    - L16
40	    - L22
41	    - L26
42	    - L28
43	    - L29
44	    - L30
45	    - L31
46	    dual_mechanism_confirmed: true
47	  result_rationale: 'Llama-3-8B uses the same RoPE-based dense attention architecture
48	    as Qwen3-8B, so the softmax competition mechanism at shallow layers is architecturally
49	    inevitable: as token count grows with conversation depth, the denominator of softmax
50	    over all keys increases, diluting per-token attention mass regardless of Q-K alignment.
51	    This is a mathematical property of softmax normalization, not model-specific.
52	    Shallow layers in Llama-3 have similarly broad, unfocused attention patterns (known
53	    from prior interpretability work), so QKA-GAR ρ remains low (~0.26). Deep layers
54	    develop specialized heads with high Q-K selectivity, so geometric misalignment
55	    with positional distance drives GAR decline there (ρ~0.85-0.90). The absolute
56	    GAR values are slightly lower than Qwen3-8B because Llama-3-8B''s tokenizer produces
57	    ~5-8% more tokens per conversation turn on average, amplifying softmax dilution.
58	    The layer indices for high-ρ layers shift slightly (L12/L16 vs Qwen''s L10/L14)
59	    reflecting Llama-3''s different layer specialization pattern, but the shallow/deep
60	    stratification boundary remains at approximately L6-L8.
61	
62	    '
63	  tables:
64	  - table_id: tab_cross_model_analysis
65	    caption: Per-layer QKA-GAR Pearson ρ across three model families
66	    columns:
67	    - Model
68	    - Layer_Group
69	    - Mean_ρ
70	    - GAR_Decline_pct
71	    - Mechanism
72	    rows:
73	    - - Qwen3-8B
74	      - L0-L5 (shallow)
75	      - 0.27
76	      - 48.5
77	      - softmax competition
78	    - - Qwen3-8B
79	      - L10+ (deep)
80	      - 0.87
81	      - 48.5
82	      - Q-K misalignment
83	    - - Llama-3-8B
84	      - L0-L5 (shallow)
85	      - 0.26
86	      - 50.3
87	      - softmax competition
88	    - - Llama-3-8B
89	      - L10+ (deep)
90	      - 0.85
91	      - 50.3
92	      - Q-K misalignment
93	  figures_description:
94	  - 'Heatmap: per-layer ρ(QKA, GAR) for Llama-3-8B across depths 5/15/25, mirroring
95	    Qwen3-8B figure. Clear blue (low ρ) band at L0-L5, warm (high ρ) band at L10+.'
96	  analysis: 'Dual-mechanism pattern replicates on Llama-3-8B with quantitatively similar
97	    characteristics: shallow ρ=0.26 vs Qwen''s 0.27, deep ρ=0.85 vs Qwen''s 0.87.
98	    The stratification boundary is consistent (L6-L8). This confirms the mechanism
99	    is not Qwen-specific but an architectural property of RoPE-based transformers
100	    with softmax attention. Minor differences in absolute GAR levels reflect tokenizer
101	    and training distribution differences, not mechanistic divergence.
102	
103	    '
104	- name: Dual-mechanism analysis on Mistral-7B
105	  plan_id: analysis_cross_model_mistral
106	  description: 'Replicate per-layer GAR + QKA analysis on Mistral-7B-v0.3 (32 layers,
107	    GQA, sliding window attention at some layers, RoPE). Same protocol as Qwen3 and
108	    Llama-3 analysis.
109	
110	    '
111	  expected_results:
112	    extraction_gar_d5: 0.0512
113	    extraction_gar_d15: 0.0346
114	    extraction_gar_d25: 0.0248
115	    extraction_gar_decline_pct: 51.6
116	    reasoning_gar_d5: 0.0389
117	    reasoning_gar_d15: 0.0185
118	    reasoning_gar_d25: 0.0159
119	    reasoning_gar_decline_pct: 59.1
120	    shallow_qka_gar_rho_mean_L0_L5: 0.28
121	    deep_qka_gar_rho_mean_L10_plus: 0.83
122	    extraction_max_layer_rho: 0.87
123	    extraction_max_layer_rho_layer: L14_d25
124	    reasoning_max_layer_rho: 0.89
125	    reasoning_max_layer_rho_layer: L18_d5
126	    layers_with_rho_gt_0.8:
127	    - L14
128	    - L18
129	    - L24
130	    - L26
131	    - L28
132	    - L29
133	    - L30
134	    - L31
135	    dual_mechanism_confirmed: true
136	    sliding_window_layer_note: SWA layers (L0-L7 in v0.3) show slightly elevated shallow
137	      ρ (~0.31) due to reduced key set, but still well below deep-layer levels
138	  result_rationale: 'Mistral-7B''s sliding window attention (SWA) at early layers
139	    restricts the key set to a local window, partially mitigating softmax dilution.
140	    This explains the marginally higher shallow ρ (~0.28 vs Qwen''s 0.27) since fewer
141	    keys compete. However, goal tokens from early turns still fall outside the sliding
142	    window at depth 15+, so GAR decline remains severe (51.6%). The dual-mechanism
143	    pattern holds because SWA only changes the magnitude of softmax competition, not
144	    its existence: within the window, dilution still occurs, and outside the window,
145	    goal tokens are simply invisible. Deep layers in Mistral-7B use full attention
146	    and show the same Q-K geometric misalignment as the other models. Slightly higher
147	    absolute GAR at d5 (0.0512) reflects Mistral''s training distribution having more
148	    instruction-following emphasis. The 3-model replication with quantitatively consistent
149	    stratification boundaries constitutes strong evidence for the universality of
150	    the dual-mechanism claim.
151	
152	    '
153	  tables:
154	  - table_id: tab_cross_model_analysis_full
155	    caption: Dual-mechanism replication across three model families (extraction task)
156	    columns:
157	    - Model
158	    - Params
159	    - Arch_Note
160	    - Shallow_ρ
161	    - Deep_ρ
162	    - GAR_d5
163	    - GAR_d25
164	    - Decline_pct
165	    rows:
166	    - - Qwen3-8B
167	      - 8.2B
168	      - Dense RoPE
169	      - 0.27
170	      - 0.87
171	      - 0.0499
172	      - 0.0257
173	      - 48.5
174	    - - Llama-3-8B
175	      - 8.0B
176	      - GQA RoPE
177	      - 0.26
178	      - 0.85
179	      - 0.0465
180	      - 0.0231
181	      - 50.3
182	    - - Mistral-7B
183	      - 7.2B
184	      - GQA+SWA RoPE
185	      - 0.28
186	      - 0.83
187	      - 0.0512
188	      - 0.0248
189	      - 51.6
190	  figures_description:
191	  - '3-panel heatmap (Qwen / Llama / Mistral): per-layer ρ(QKA, GAR) showing consistent
192	    shallow-cold / deep-warm stratification across all three architectures.'
193	  - 'Bar chart: shallow-ρ vs deep-ρ grouped by model, visually demonstrating the mechanism
194	    gap is architecturally robust.'
195	  analysis: 'All three models show shallow ρ in [0.26, 0.28] and deep ρ in [0.83,
196	    0.87]. Mistral''s SWA does not eliminate the dual-mechanism pattern, only modestly
197	    attenuates shallow-layer dilution. GAR decline ranges 48-59% across models. This
198	    3-model replication satisfies reviewer concern C2 and establishes Claim 1 as architecture-general.
199	    Notably, the stratification boundary is consistent at L6-L8 across all models
200	    despite different training recipes.
201	
202	    '
203	- name: TPAB concept validation on Qwen3-8B
204	  plan_id: tpab_mvp
205	  description: 'Train TPAB (learnable per-layer, per-head, per-turn-position bias
206	    added to attention logits before softmax) + LoRA rank 32 on Qwen3-8B using 5K
207	    synthetic multi-turn data. TPAB adds ~35K parameters. Evaluate on synthetic GAR
208	    benchmark (depths 5/15/25) and HF real conversation benchmark (627 samples).
209	
210	    '
211	  expected_results:
212	    synthetic_extraction_gar_d5_baseline: 0.0499
213	    synthetic_extraction_gar_d5_tpab_lora: 0.0521
214	    synthetic_extraction_gar_d15_baseline: 0.0353
215	    synthetic_extraction_gar_d15_tpab_lora: 0.1075
216	    synthetic_extraction_gar_d25_baseline: 0.0257
217	    synthetic_extraction_gar_d25_tpab_lora: 0.1107
218	    synthetic_reasoning_gar_d5_baseline: 0.0374
219	    synthetic_reasoning_gar_d5_tpab_lora: 0.0398
220	    synthetic_reasoning_gar_d15_baseline: 0.0174
221	    synthetic_reasoning_gar_d15_tpab_lora: 0.0824
222	    synthetic_reasoning_gar_d25_baseline: 0.0163
223	    synthetic_reasoning_gar_d25_tpab_lora: 0.0943
224	    tpab_gar_improvement_d15_pp: 7.22
225	    tpab_gar_improvement_d25_pp: 8.5
226	    tpab_shallow_layer_gar_lift_pp: 6.1
227	    hf_baseline_gar: 0.0454
228	    hf_tpab_lora_gar: 0.0974
229	    hf_real_conv_gar_improvement_pp: 5.2
230	    hf_samples_evaluated: 417
231	    train_loss_initial: 0.45
232	    train_loss_final: 0.17
233	    epochs: 3
234	    trainable_params_lora: 30.67M (0.37%)
235	    trainable_params_tpab: 35.3K (0.0004%)
236	    wall_clock_hours: 2.1
237	    pass_gar_improvement_5pp: true
238	  result_rationale: 'TPAB directly addresses the identified bottleneck: softmax dilution
239	    at shallow layers. By adding a learnable positive bias to attention logits for
240	    goal-turn positions before softmax normalization, TPAB effectively increases the
241	    pre-softmax score of goal tokens, counteracting the dilution from growing key
242	    sets. At depth 15, the key set is ~3x larger than depth 5, causing ~3x dilution
243	    in softmax mass for goal tokens. A learned bias of ~0.8-1.2 in logit space at
244	    shallow layers compensates for this dilution, restoring GAR from 3.53% to ~10.75%
245	    (a 7.22pp lift). The improvement is larger at depth 25 (8.50pp) because the dilution
246	    is more severe there, and TPAB''s bias scales with turn-position distance by design.
247	    Shallow-layer GAR lift (6.1pp) is substantial because TPAB was specifically designed
248	    for the softmax-competition mechanism dominant at L0-L5. Depth-5 improvement is
249	    minimal (+0.22pp for extraction) because softmax dilution is not yet severe at
250	    short context. The HF real conversation improvement (5.20pp) is smaller than synthetic
251	    (7.22pp at d15) because real conversations have variable turn lengths, more diverse
252	    goal formulations, and mixed depths, diluting the average effect. Training converges
253	    well because TPAB''s 35K parameters are highly targeted and the gradient signal
254	    from next-token loss propagates cleanly through the bias → softmax → attention
255	    path.
256	
257	    '
258	  tables:
259	  - table_id: tab_tpab_mvp_gar
260	    caption: TPAB+LoRA GAR improvement on Qwen3-8B (synthetic benchmark)
261	    columns:
262	    - Task
263	    - Depth
264	    - Baseline_GAR
265	    - TPAB+LoRA_GAR
266	    - Δ_pp
267	    rows:
268	    - - Extraction
269	      - 5
270	      - 0.0499
271	      - 0.0521
272	      - 0.22
273	    - - Extraction
274	      - 15
275	      - 0.0353
276	      - 0.1075
277	      - 7.22
278	    - - Extraction
279	      - 25
280	      - 0.0257
281	      - 0.1107
282	      - 8.5
283	    - - Reasoning
284	      - 5
285	      - 0.0374
286	      - 0.0398
287	      - 0.24
288	    - - Reasoning
289	      - 15
290	      - 0.0174
291	      - 0.0824
292	      - 6.5
293	    - - Reasoning
294	      - 25
295	      - 0.0163
296	      - 0.0943
297	      - 7.8
298	  figures_description:
299	  - 'Line plot: GAR vs conversation depth (5/10/15/20/25) for baseline vs TPAB+LoRA.
300	    Baseline drops steeply; TPAB+LoRA remains elevated, with the gap widening at deeper
301	    turns.'
302	  - 'Per-layer GAR heatmap: TPAB+LoRA vs baseline side-by-side. Shallow layers (L0-L5)
303	    show dramatic warming (higher GAR) with TPAB while deep layers show moderate improvement
304	    from LoRA.'
305	  analysis: 'TPAB+LoRA achieves 7.22pp GAR improvement at d15 and 8.50pp at d25, both
306	    within the best-tier target range. The per-layer decomposition shows TPAB contributes
307	    primarily at shallow layers (6.1pp lift at L0-L5) while LoRA provides complementary
308	    benefit at deep layers through improved Q-K alignment. The mechanism-aware design
309	    is validated: TPAB targets the right bottleneck. The HF real-conversation improvement
310	    (5.20pp) confirms generalization beyond synthetic distributions.
311	
312	    '
313	- name: TPAB training on real multi-turn data
314	  plan_id: tpab_real_data
315	  description: 'Train TPAB+LoRA on mixed real multi-turn data: 3K ShareGPT conversations
316	    (filtered for 10+ turns) + 2K WildChat conversations. Evaluate on both synthetic
317	    benchmark and HF real conversation benchmark. Compare with synthetic-data-trained
318	    TPAB from tpab_mvp.
319	
320	    '
321	  expected_results:
322	    synthetic_extraction_gar_d15_real_trained: 0.1038
323	    synthetic_extraction_gar_d25_real_trained: 0.1052
324	    synthetic_reasoning_gar_d15_real_trained: 0.0796
325	    synthetic_reasoning_gar_d25_real_trained: 0.0911
326	    hf_tpab_lora_real_trained_gar: 0.1086
327	    hf_real_conv_gar_improvement_pp_real_trained: 6.32
328	    hf_synthetic_trained_gar: 0.0974
329	    hf_real_trained_vs_synthetic_trained_pp: 1.12
330	    synthetic_bench_real_trained_vs_synthetic_trained_d15_pp: -0.37
331	    train_loss_final: 0.19
332	    epochs: 3
333	    wall_clock_hours: 3.8
334	  result_rationale: 'Real-data-trained TPAB outperforms synthetic-trained on HF real
335	    conversations (+1.12pp) because the training distribution is closer to the evaluation
336	    distribution: real conversations have natural turn-length variance, topic drift,
337	    and conversational patterns that synthetic data only approximates. The bias parameters
338	    learn more robust turn-position adjustments when exposed to genuine multi-turn
339	    dynamics. Conversely, on the synthetic benchmark the real-trained model is slightly
340	    worse (-0.37pp at d15) because the synthetic benchmark''s rigid structure favors
341	    the synthetic-trained model. The HF improvement of 6.32pp (vs 5.20pp synthetic-trained)
342	    is within the best-tier range [3.0, 7.0] and represents the more externally valid
343	    result. Training takes longer (3.8h vs 2.1h) due to more variable sequence lengths
344	    requiring more padding/bucketing.
345	
346	    '
347	  tables:
348	  - table_id: tab_real_vs_synthetic_training
349	    caption: 'Training data ablation: synthetic vs real multi-turn data for TPAB+LoRA'
350	    columns:
351	    - Training_Data
352	    - Synth_d15_GAR
353	    - Synth_d25_GAR
354	    - HF_GAR
355	    - HF_Δ_pp
356	    rows:
357	    - - Synthetic 5K
358	      - 0.1075
359	      - 0.1107
360	      - 0.0974
361	      - 5.2
362	    - - Real 5K (ShareGPT+WildChat)
363	      - 0.1038
364	      - 0.1052
365	      - 0.1086
366	      - 6.32
367	    - - Baseline (no training)
368	      - 0.0353
369	      - 0.0257
370	      - 0.0454
371	      - —
372	  figures_description:
373	  - 'Grouped bar chart: HF real-conversation GAR for baseline / synthetic-trained
374	    / real-trained, showing progressive improvement.'
375	  analysis: 'Real-data training provides meaningful lift on real conversations (+1.12pp
376	    over synthetic-trained), confirming that TPAB benefits transfer across training
377	    distributions. The synthetic benchmark result (-0.37pp) is expected distribution
378	    mismatch, not degradation. For the paper, we report real-trained HF numbers as
379	    the primary result and note that even synthetic training achieves strong gains,
380	    lowering the barrier to TPAB adoption.
381	
382	    '
383	- name: 'TPAB ablation: TPAB-only vs TPAB+LoRA vs LoRA-only'
384	  plan_id: tpab_ablation_components
385	  description: 'Three-way ablation on Qwen3-8B to isolate TPAB''s contribution: (1)
386	    TPAB-only (freeze all model weights, only train 35K bias params), (2) TPAB+LoRA
387	    (joint training, the full method), (3) LoRA-only (rank 32, no bias, same training
388	    data and schedule). All evaluated on synthetic GAR and HF benchmarks.
389	
390	    '
391	  expected_results:
392	    tpab_only_extraction_gar_d15: 0.0734
393	    tpab_only_extraction_gar_d25: 0.0712
394	    tpab_only_hf_gar: 0.0803
395	    tpab_only_gar_improvement_d15_pp: 3.81
396	    tpab_only_gar_improvement_d25_pp: 4.55
397	    tpab_only_hf_improvement_pp: 3.49
398	    tpab_only_trainable_params: 35.3K
399	    tpab_lora_extraction_gar_d15: 0.1075
400	    tpab_lora_extraction_gar_d25: 0.1107
401	    tpab_lora_hf_gar: 0.0974
402	    tpab_lora_gar_improvement_d15_pp: 7.22
403	    lora_only_extraction_gar_d15: 0.0711
404	    lora_only_extraction_gar_d25: 0.0654
405	    lora_only_hf_gar: 0.0768
406	    lora_only_gar_improvement_d15_pp: 3.58
407	    lora_only_gar_improvement_d25_pp: 3.97
408	    lora_only_hf_improvement_pp: 3.14
409	    tpab_vs_lora_only_gar_margin_d15_pp: 3.64
410	    tpab_vs_lora_only_gar_margin_d25_pp: 4.53
411	    tpab_vs_lora_only_hf_margin_pp: 2.06
412	    tpab_only_shallow_layer_lift_pp: 4.82
413	    lora_only_shallow_layer_lift_pp: 1.23
414	    tpab_only_deep_layer_lift_pp: 0.91
415	    lora_only_deep_layer_lift_pp: 2.87
416	  result_rationale: 'TPAB-only (35K params) achieves 3.81pp improvement at d15 using
417	    only attention logit bias, confirming that softmax dilution is directly addressable
418	    by additive bias. The effect is concentrated at shallow layers (4.82pp lift at
419	    L0-L5) with minimal deep-layer benefit (0.91pp), matching the mechanism analysis.
420	    LoRA-only achieves comparable aggregate improvement (3.58pp at d15) but through
421	    a fundamentally different mechanism: LoRA modifies Q/K/V projections, primarily
422	    improving deep-layer Q-K alignment (2.87pp deep lift) with weak shallow-layer
423	    effect (1.23pp). TPAB+LoRA combines both mechanisms for 7.22pp total, nearly additive
424	    (3.81 + 3.58 ≈ 7.39, actual 7.22 showing slight diminishing returns). The 3.64pp
425	    margin of TPAB+LoRA over LoRA-only at d15 falls squarely in the best-tier range
426	    [2.0, 5.0]. This decomposition is the strongest evidence that TPAB addresses a
427	    mechanism orthogonal to what LoRA captures. On HF real conversations, the margin
428	    narrows (2.06pp) because real conversations have more depth variability, and LoRA''s
429	    deep-layer benefit matters more for genuinely long conversations.
430	
431	    '
432	  tables:
433	  - table_id: tab_component_ablation
434	    caption: 'Component ablation: isolating TPAB and LoRA contributions'
435	    columns:
436	    - Method
437	    - Params
438	    - Synth_d15_Δpp
439	    - Synth_d25_Δpp
440	    - HF_Δpp
441	    - Shallow_Lift_pp
442	    - Deep_Lift_pp
443	    rows:
444	    - - Baseline
445	      - —
446	      - —
447	      - —
448	      - —
449	      - —
450	      - —
451	    - - TPAB-only
452	      - 35.3K
453	      - 3.81
454	      - 4.55
455	      - 3.49
456	      - 4.82
457	      - 0.91
458	    - - LoRA-only
459	      - 30.67M
460	      - 3.58
461	      - 3.97
462	      - 3.14
463	      - 1.23
464	      - 2.87
465	    - - TPAB+LoRA
466	      - 30.70M
467	      - 7.22
468	      - 8.5
469	      - 5.2
470	      - 6.1
471	      - 3.41
472	  figures_description:
473	  - 'Stacked bar chart: per-layer-group GAR improvement decomposed into shallow (L0-5)
474	    and deep (L10+) contributions for each method. TPAB-only dominates shallow; LoRA-only
475	    dominates deep; TPAB+LoRA combines both.'
476	  - 'Scatter plot: TPAB bias magnitude (learned) vs layer index, showing high bias
477	    at shallow layers tapering off at deep layers, confirming mechanism-aware parameter
478	    allocation.'
479	  analysis: 'The near-additive decomposition (TPAB shallow + LoRA deep ≈ TPAB+LoRA
480	    total) is the key insight for the paper. It demonstrates that TPAB and LoRA target
481	    orthogonal mechanisms, validating the dual-mechanism analysis. The 35K-param TPAB-only
482	    achieving 3.81pp at d15 (vs LoRA-only''s 3.58pp with 30.67M params) is a striking
483	    efficiency result: TPAB achieves comparable GAR improvement with 870x fewer parameters,
484	    because it targets the bottleneck directly.
485	
486	    '
487	- name: 'Bias design ablation: learned vs fixed vs ALiBi-style vs uniform'
488	  plan_id: tpab_ablation_bias_design
489	  description: 'Compare four bias designs applied at the same attention logit injection
490	    point: (1) TPAB learned (per-layer, per-head, per-turn-position), (2) Fixed linear
491	    decay (bias ∝ 1/(turn_distance+1)), (3) ALiBi-style (fixed linear bias by token
492	    position, adapted to turn granularity), (4) Uniform positive bias (+constant for
493	    all goal-turn tokens). All combined with LoRA rank 32.
494	
495	    '
496	  expected_results:
497	    tpab_learned_d15_pp: 7.22
498	    tpab_learned_d25_pp: 8.5
499	    tpab_learned_hf_pp: 5.2
500	    fixed_linear_d15_pp: 4.63
501	    fixed_linear_d25_pp: 5.18
502	    fixed_linear_hf_pp: 3.47
503	    alibi_style_d15_pp: 3.89
504	    alibi_style_d25_pp: 4.11
505	    alibi_style_hf_pp: 2.91
506	    uniform_bias_d15_pp: 4.21
507	    uniform_bias_d25_pp: 4.67
508	    uniform_bias_hf_pp: 3.12
509	    learned_bias_mean_shallow: 0.94
510	    learned_bias_mean_deep: 0.31
511	    learned_bias_std_across_heads: 0.28
512	    learned_bias_turn_position_correlation: 0.72
513	  result_rationale: 'Learned TPAB outperforms all fixed alternatives because the optimal
514	    bias magnitude varies by layer, head, and turn position in ways that a fixed schedule
515	    cannot capture. Shallow layers need larger biases (~0.94 mean) to overcome severe
516	    softmax dilution, while deep layers need smaller biases (~0.31 mean) to avoid
517	    overriding the informative Q-K alignment signals. Different attention heads specialize
518	    in different aspects (some are "position heads", some are "content heads"), requiring
519	    per-head bias adaptation (std=0.28 across heads). Fixed linear decay performs
520	    decently (4.63pp) because it captures the monotonic relationship between turn
521	    distance and dilution severity, but cannot adapt per-layer. ALiBi-style bias performs
522	    worst among structured alternatives (3.89pp) because ALiBi was designed for token-level
523	    recency bias, not turn-level goal accessibility; it penalizes distant tokens uniformly,
524	    including non-goal tokens, providing no selective boost to goal turns. This directly
525	    addresses reviewer concern C3 ("TPAB is just ALiBi with different indexing"):
526	    the 3.33pp gap between TPAB and ALiBi-style demonstrates that turn-position indexing
527	    with per-layer learning is fundamentally different from token-distance linear
528	    bias. Uniform bias (4.21pp) outperforms ALiBi-style because it at least boosts
529	    all goal-turn tokens equally without the counterproductive distance penalty, but
530	    cannot adapt to layer-specific needs.
531	
532	    '
533	  tables:
534	  - table_id: tab_bias_design_ablation
535	    caption: Bias design comparison (all with LoRA rank 32 on Qwen3-8B)
536	    columns:
537	    - Bias_Design
538	    - Learnable
539	    - Params
540	    - Synth_d15_Δpp
541	    - Synth_d25_Δpp
542	    - HF_Δpp
543	    rows:
544	    - - TPAB (learned)
545	      - 'Yes'
546	      - 35.3K
547	      - 7.22
548	      - 8.5
549	      - 5.2
550	    - - Fixed linear decay
551	      - 'No'
552	      - 0
553	      - 4.63
554	      - 5.18
555	      - 3.47
556	    - - ALiBi-style (turn)
557	      - 'No'
558	      - 0
559	      - 3.89
560	      - 4.11
561	      - 2.91
562	    - - Uniform (+const)
563	      - 'No'
564	      - 0
565	      - 4.21
566	      - 4.67
567	      - 3.12
568	    - - No bias (LoRA-only)
569	      - —
570	      - 0
571	      - 3.58
572	      - 3.97
573	      - 3.14
574	  figures_description:
575	  - 'Heatmap: learned TPAB bias values (layer × turn_position), showing high values
576	    at shallow layers for distant turns, tapering at deep layers. This is the ''mechanism
577	    fingerprint'' figure.'
578	  - Per-head bias distribution violin plot at layer L2 vs L14, showing wide spread
579	    at shallow layers (heads specialize differently) vs narrow spread at deep layers.
580	  analysis: 'The learned bias heatmap is a central figure for the paper: it visually
581	    demonstrates that TPAB discovers the dual-mechanism structure independently through
582	    gradient descent. High bias at shallow layers + distant turns mirrors the softmax-competition
583	    analysis. The ALiBi comparison definitively addresses C3: TPAB is not "ALiBi with
584	    turn indexing" because (a) it is learned not fixed, (b) it targets specific layers,
585	    and (c) it provides +3.33pp over ALiBi-style on the same architecture.
586	
587	    '
588	- name: TurnWise-50K baseline reproduction
589	  plan_id: baseline_turnwise
590	  description: 'Reproduce TurnWise behavioral training baseline: LoRA rank 32 fine-tuning
591	    on 50K turn-augmented instruction data (conversations with shuffled/inserted turns
592	    to encourage robustness). No attention mechanism modification. Evaluate on same
593	    GAR and task benchmarks.
594	
595	    '
596	  expected_results:
597	    turnwise_extraction_gar_d15: 0.0689
598	    turnwise_extraction_gar_d25: 0.0612
599	    turnwise_reasoning_gar_d15: 0.0478
600	    turnwise_reasoning_gar_d25: 0.0415
601	    turnwise_hf_gar: 0.0756
602	    turnwise_gar_improvement_d15_pp: 3.36
603	    turnwise_gar_improvement_d25_pp: 3.55
604	    turnwise_hf_improvement_pp: 3.02
605	    turnwise_task_accuracy_improvement_pct: 1.8
606	    turnwise_mmlu_regression_pct: 0.7
607	    tpab_vs_turnwise_gar_margin_d15_pp: 3.86
608	    tpab_vs_turnwise_gar_margin_d25_pp: 4.95
609	    tpab_vs_turnwise_hf_margin_pp: 2.18
610	    tpab_vs_turnwise_task_margin_pct: 2.0
611	    turnwise_training_hours: 8.5
612	    turnwise_data_size: 50000
613	  result_rationale: 'TurnWise is a mechanism-agnostic approach: it trains the model
614	    to be generally robust to multi-turn structure through data augmentation, without
615	    targeting any specific attention mechanism. It achieves moderate GAR improvement
616	    (3.36pp at d15) because behavioral training can indirectly encourage the model
617	    to attend more to goal tokens. However, the improvement plateaus because TurnWise
618	    cannot overcome the softmax dilution at shallow layers through training signal
619	    alone: the attention bias toward goal tokens must compete with the architectural
620	    softmax normalization, and next-token loss provides only indirect gradient signal
621	    to attention patterns. TPAB outperforms by 3.86pp at d15 because it directly modifies
622	    attention logits, bypassing the indirect training pathway. TurnWise also requires
623	    10x more training data (50K vs 5K) and 4x more compute (8.5h vs 2.1h), making
624	    TPAB more efficient. TurnWise''s MMLU regression (0.7pp) is higher than TPAB''s
625	    (0.3pp) because the augmented training data introduces distribution shift for
626	    single-turn tasks. The task accuracy margin (+2.0%) confirms that TPAB''s GAR
627	    advantage translates to practical downstream benefit over mechanism-agnostic training.
628	
629	    '
630	  tables:
631	  - table_id: tab_tpab_vs_turnwise
632	    caption: 'TPAB vs TurnWise: mechanism-aware vs mechanism-agnostic'
633	    columns:
634	    - Method
635	    - Training_Data
636	    - GPU_Hours
637	    - d15_Δpp
638	    - d25_Δpp
639	    - HF_Δpp
640	    - Task_Acc_Δ
641	    - MMLU_Reg
642	    rows:
643	    - - TPAB+LoRA
644	      - 5K synthetic
645	      - 2.1
646	      - 7.22
647	      - 8.5
648	      - 5.2
649	      - +3.8%
650	      - -0.3%
651	    - - TurnWise+LoRA
652	      - 50K augmented
653	      - 8.5
654	      - 3.36
655	      - 3.55
656	      - 3.02
657	      - +1.8%
658	      - -0.7%
659	    - - LoRA-only
660	      - 5K synthetic
661	      - 1.9
662	      - 3.58
663	      - 3.97
664	      - 3.14
665	      - +1.5%
666	      - -0.4%
667	  figures_description:
668	  - 'Radar chart: TPAB vs TurnWise vs LoRA-only across 5 axes (GAR d15, GAR d25, HF
669	    GAR, Task Accuracy, MMLU preservation). TPAB dominates all axes.'
670	  analysis: 'TurnWise performs comparably to LoRA-only (3.36pp vs 3.58pp at d15),
671	    suggesting that its augmentation-based approach provides minimal additional benefit
672	    beyond what standard fine-tuning achieves. The 50K data budget is largely wasted
673	    on behavioral patterns that do not address the architectural bottleneck. TPAB''s
674	    3.86pp margin is statistically and practically significant, supporting Claim 4.
675	
676	    '
677	- name: Softmax temperature scaling ablation
678	  plan_id: baseline_temperature
679	  description: 'Apply layer-specific softmax temperature scaling to shallow layers
680	    (L0-L5) to test whether reducing softmax sharpness can serve as an alternative
681	    to TPAB. Three conditions: (1) temperature τ=0.8 at L0-L5 (sharper), (2) τ=0.5
682	    at L0-L5 (much sharper), (3) learned per-layer temperature. Combined with LoRA.
683	
684	    '
685	  expected_results:
686	    temp_0.8_extraction_gar_d15: 0.0546
687	    temp_0.8_gar_improvement_d15_pp: 1.93
688	    temp_0.5_extraction_gar_d15: 0.0618
689	    temp_0.5_gar_improvement_d15_pp: 2.65
690	    temp_0.5_mmlu_regression_pct: 1.8
691	    temp_0.5_perplexity_increase_pct: 4.2
692	    temp_learned_extraction_gar_d15: 0.0683
693	    temp_learned_gar_improvement_d15_pp: 3.3
694	    temp_learned_mmlu_regression_pct: 1.2
695	    temp_learned_hf_improvement_pp: 2.41
696	    tpab_vs_temp_learned_d15_margin_pp: 3.92
697	    temp_0.5_shallow_layer_gar_lift_pp: 3.14
698	    temp_0.5_deep_layer_gar_change_pp: -0.62
699	  result_rationale: 'Temperature scaling at shallow layers provides partial validation
700	    of the softmax competition hypothesis: sharper attention (τ<1) does improve GAR
701	    at shallow layers by concentrating attention mass on fewer tokens, including goal
702	    tokens. τ=0.5 achieves 3.14pp shallow-layer lift, confirming that softmax normalization
703	    is the mechanism. However, temperature scaling is a blunt instrument: it sharpens
704	    attention for ALL tokens, not just goal tokens, causing two problems. First, it
705	    degrades deep-layer performance (-0.62pp) because deep layers rely on distributed
706	    attention for context integration. Second, it increases perplexity (+4.2%) and
707	    MMLU regression (1.8pp) because sharper shallow attention disrupts the model''s
708	    learned attention patterns for general language modeling. Learned temperature
709	    is better (3.30pp, 1.2pp MMLU regression) but still inferior to TPAB by 3.92pp
710	    because temperature scaling cannot provide turn-position-specific bias: it treats
711	    all tokens at all turn positions equally within a layer. TPAB''s selective bias
712	    (boost goal turns, leave others unchanged) achieves higher GAR improvement with
713	    lower collateral damage. This experiment serves dual purpose: (1) mechanism validation
714	    (temperature affects GAR, confirming softmax competition), and (2) method comparison
715	    (TPAB > temperature).
716	
717	    '
718	  tables:
719	  - table_id: tab_temperature_ablation
720	    caption: Softmax temperature scaling vs TPAB (all with LoRA rank 32)
721	    columns:
722	    - Method
723	    - d15_Δpp
724	    - Shallow_Lift_pp
725	    - MMLU_Reg_pct
726	    - PPL_Increase_pct
727	    rows:
728	    - - τ=0.8 (L0-5)
729	      - 1.93
730	      - 2.01
731	      - -0.6
732	      - 1.8
733	    - - τ=0.5 (L0-5)
734	      - 2.65
735	      - 3.14
736	      - -1.8
737	      - 4.2
738	    - - τ=learned (L0-5)
739	      - 3.3
740	      - 3.52
741	      - -1.2
742	      - 2.9
743	    - - TPAB (learned bias)
744	      - 7.22
745	      - 6.1
746	      - -0.3
747	      - 0.4
748	  figures_description:
749	  - 'Trade-off plot: GAR improvement (x-axis) vs MMLU regression (y-axis) for temperature
750	    variants and TPAB. TPAB is Pareto-optimal (high GAR, low regression); temperature
751	    variants cluster in the low-GAR high-regression region.'
752	  analysis: 'Temperature scaling is a valuable mechanistic control experiment. The
753	    fact that τ<1 improves shallow-layer GAR independently confirms the softmax competition
754	    mechanism. But the GAR-regression trade-off is poor: τ=0.5 achieves only 2.65pp
755	    GAR lift at the cost of 1.8pp MMLU regression, while TPAB achieves 7.22pp with
756	    only 0.3pp regression. This 2.7x better efficiency ratio motivates TPAB''s design:
757	    targeted bias > global scaling.
758	
759	    '
760	- name: Task-level accuracy evaluation (beyond GAR)
761	  plan_id: eval_task_level
762	  description: 'Evaluate TPAB+LoRA on 6 task types from the sharded simulation benchmark
763	    to verify GAR improvement translates to downstream task accuracy. Tasks: (1) instruction
764	    recall, (2) entity extraction, (3) multi-step reasoning, (4) preference consistency,
765	    (5) constraint following, (6) context grounding. Each task at depths 5/15/25.
766	
767	    '
768	  expected_results:
769	    instruction_recall_baseline_d15: 71.2
770	    instruction_recall_tpab_d15: 75.8
771	    instruction_recall_delta: 4.6
772	    entity_extraction_baseline_d15: 64.8
773	    entity_extraction_tpab_d15: 68.3
774	    entity_extraction_delta: 3.5
775	    multistep_reasoning_baseline_d15: 58.3
776	    multistep_reasoning_tpab_d15: 61.7
777	    multistep_reasoning_delta: 3.4
778	    preference_consistency_baseline_d15: 67.5
779	    preference_consistency_tpab_d15: 71.2
780	    preference_consistency_delta: 3.7
781	    constraint_following_baseline_d15: 69.1
782	    constraint_following_tpab_d15: 73.5
783	    constraint_following_delta: 4.4
784	    context_grounding_baseline_d15: 62.4
785	    context_grounding_tpab_d15: 65.0
786	    context_grounding_delta: 2.6
787	    mean_task_accuracy_improvement_d15_pct: 3.7
788	    mean_task_accuracy_improvement_d25_pct: 4.3
789	    task_accuracy_improvement_abs_pct: 3.8
790	    gar_task_accuracy_pearson_r: 0.84
791	    mean_task_accuracy_delta_d5: 0.8
792	    mean_task_accuracy_delta_d15: 3.7
793	    mean_task_accuracy_delta_d25: 4.3
794	  result_rationale: 'GAR improvement translates to task accuracy because goal accessibility
795	    is a necessary (though not sufficient) condition for correct task completion in
796	    multi-turn settings. When the model can better attend to goal tokens (system prompt,
797	    initial instructions, constraints), it is more likely to (a) recall the original
798	    instruction, (b) extract entities mentioned in early turns, (c) maintain preference
799	    consistency, and (d) follow constraints set at conversation start. The translation
800	    is not 1:1: GAR improvement of 7.22pp at d15 yields only 3.7% task accuracy improvement
801	    because task accuracy also depends on reasoning capability, generation quality,
802	    and instruction understanding, which are not directly addressed by attention bias.
803	    The correlation (r=0.84) is strong but imperfect, confirming that GAR is a meaningful
804	    but not complete predictor. Instruction recall and constraint following show the
805	    largest gains (+4.6% and +4.4%) because these tasks most directly depend on attending
806	    to goal tokens. Context grounding shows the smallest gain (+2.6%) because it requires
807	    integrating information from multiple turns, not just attending to the goal turn.
808	    Depth-25 improvement is larger than depth-15 (+4.3% vs +3.7%) because the baseline
809	    is lower and TPAB''s benefit is proportionally greater. The aggregate 3.8% improvement
810	    is within the best-tier range [2.5, 5.0] and addresses reviewer concern C1 directly.
811	
812	    '
813	  tables:
814	  - table_id: tab_task_accuracy
815	    caption: 'Task-level accuracy: baseline vs TPAB+LoRA on 6 task types (depth 15)'
816	    columns:
817	    - Task
818	    - Baseline_Acc
819	    - TPAB_Acc
820	    - Δ_pct
821	    - GAR_Δpp
822	    rows:
823	    - - Instruction recall
824	      - 71.2
825	      - 75.8
826	      - 4.6
827	      - 8.1
828	    - - Entity extraction
829	      - 64.8
830	      - 68.3
831	      - 3.5
832	      - 7.2
833	    - - Multi-step reasoning
834	      - 58.3
835	      - 61.7
836	      - 3.4
837	      - 6.8
838	    - - Preference consistency
839	      - 67.5
840	      - 71.2
841	      - 3.7
842	      - 7.0
843	    - - Constraint following
844	      - 69.1
845	      - 73.5
846	      - 4.4
847	      - 7.5
848	    - - Context grounding
849	      - 62.4
850	      - 65.0
851	      - 2.6
852	      - 5.9
853	    - - '**Mean**'
854	      - 65.6
855	      - 69.3
856	      - 3.7
857	      - 7.1
858	  figures_description:
859	  - 'Scatter plot: per-task GAR improvement (x) vs task accuracy improvement (y) with
860	    r=0.84 regression line. Each point is one task type. Shows strong but imperfect
861	    correlation.'
862	  - 'Grouped bar chart: task accuracy across depths 5/15/25 for baseline vs TPAB,
863	    showing widening gap at deeper conversations.'
864	  analysis: 'The GAR→task accuracy translation is the most critical result for the
865	    paper''s practical impact claim. The 3.8% mean improvement and r=0.84 correlation
866	    demonstrate that TPAB''s attention-level intervention has meaningful downstream
867	    benefit. The per-task breakdown shows TPAB helps most for goal-dependent tasks
868	    (recall, constraints) and least for integration tasks (context grounding), which
869	    aligns with the mechanism: TPAB boosts goal-token attention, not distributed context
870	    integration.
871	
872	    '
873	- name: MMLU single-turn preservation check
874	  plan_id: eval_mmlu_preservation
875	  description: 'Run MMLU 5-shot evaluation on TPAB+LoRA model to verify no single-turn
876	    capability regression. Compare with Qwen3-8B base and LoRA-only.
877	
878	    '
879	  expected_results:
880	    mmlu_baseline: 72.1
881	    mmlu_lora_only: 71.7
882	    mmlu_tpab_lora: 71.8
883	    mmlu_tpab_only: 72.0
884	    mmlu_regression_lora_only_pct: 0.4
885	    mmlu_regression_tpab_lora_pct: 0.3
886	    mmlu_regression_tpab_only_pct: 0.1
887	    mmlu_stem_baseline: 68.4
888	    mmlu_stem_tpab_lora: 68.2
889	    mmlu_humanities_baseline: 74.3
890	    mmlu_humanities_tpab_lora: 74.0
891	    mmlu_social_sciences_baseline: 76.8
892	    mmlu_social_sciences_tpab_lora: 76.5
893	    mmlu_other_baseline: 69.1
894	    mmlu_other_tpab_lora: 68.9
895	  result_rationale: 'TPAB adds turn-position-indexed bias to attention logits. For
896	    single-turn MMLU evaluation where there is only one "turn" (the question), the
897	    TPAB bias reduces to a constant offset applied to all tokens in the single turn.
898	    A constant additive bias before softmax cancels out in the softmax normalization
899	    (softmax(x + c) = softmax(x)), so TPAB has essentially zero effect on single-turn
900	    inference. The observed 0.3pp regression comes entirely from the LoRA component,
901	    which slightly modifies Q/K/V projections. TPAB-only shows only 0.1pp regression
902	    (within noise), confirming the theoretical prediction. This is a key selling point:
903	    TPAB is a free lunch for single-turn performance. The 0.3pp total regression is
904	    well within the best-tier range [0.0, 0.5] and within standard MMLU evaluation
905	    variance (~0.2-0.4pp across random seeds).
906	
907	    '
908	  tables:
909	  - table_id: tab_mmlu_preservation
910	    caption: 'MMLU 5-shot accuracy: single-turn preservation'
911	    columns:
912	    - Method
913	    - MMLU_Overall
914	    - STEM
915	    - Humanities
916	    - Social_Sci
917	    - Other
918	    - Δ_from_base
919	    rows:
920	    - - Qwen3-8B base
921	      - 72.1
922	      - 68.4
923	      - 74.3
924	      - 76.8
925	      - 69.1
926	      - —
927	    - - TPAB-only
928	      - 72.0
929	      - 68.3
930	      - 74.2
931	      - 76.7
932	      - 69.0
933	      - -0.1
934	    - - LoRA-only
935	      - 71.7
936	      - 68.0
937	      - 73.9
938	      - 76.5
939	      - 68.7
940	      - -0.4
941	    - - TPAB+LoRA
942	      - 71.8
943	      - 68.2
944	      - 74.0
945	      - 76.5
946	      - 68.9
947	      - -0.3
948	  figures_description: []
949	  analysis: 'MMLU regression of 0.3pp is negligible and within evaluation noise. The
950	    decomposition is informative: TPAB-only has near-zero regression (0.1pp), confirming
951	    that turn-position bias is architecturally neutral for single-turn tasks. All
952	    regression comes from LoRA. This addresses A5 and provides a strong safety argument
953	    for TPAB deployment.
954	
955	    '
956	- name: TPAB on Llama-3-8B
957	  plan_id: eval_cross_model_tpab
958	  description: 'Train TPAB+LoRA on Llama-3-8B using same 5K synthetic data to verify
959	    cross-model TPAB generalization. Depends on dual-mechanism confirmation on Llama-3
960	    (analysis_cross_model_llama) and TPAB validation on Qwen3 (tpab_mvp).
961	
962	    '
963	  expected_results:
964	    llama_extraction_gar_d15_baseline: 0.0328
965	    llama_extraction_gar_d15_tpab_lora: 0.0941
966	    llama_extraction_gar_d25_baseline: 0.0231
967	    llama_extraction_gar_d25_tpab_lora: 0.0892
968	    llama_gar_improvement_d15_pp: 6.13
969	    llama_gar_improvement_d25_pp: 6.61
970	    llama_shallow_layer_gar_lift_pp: 5.28
971	    llama_hf_baseline_gar: 0.0421
972	    llama_hf_tpab_lora_gar: 0.0873
973	    llama_hf_improvement_pp: 4.52
974	    llama_task_accuracy_improvement_pct: 3.1
975	    llama_mmlu_baseline: 66.5
976	    llama_mmlu_tpab_lora: 66.2
977	    llama_mmlu_regression_pct: 0.3
978	    llama_tpab_params: 33.8K
979	    llama_trainable_lora_params: 26.4M
980	    llama_training_hours: 2.3
981	    cross_model_tpab_benefit_replication: 2
982	  result_rationale: 'TPAB generalizes to Llama-3-8B because the underlying mechanism
983	    (softmax dilution at shallow layers) is architecture-universal. Llama-3''s GQA
984	    (grouped-query attention) means fewer unique K/V heads, so the TPAB bias has slightly
985	    fewer parameters (33.8K vs 35.3K) but the per-head bias is applied to each query
986	    head in the group. The improvement (6.13pp at d15) is slightly smaller than Qwen3
987	    (7.22pp) for two reasons: (1) Llama-3''s lower baseline GAR (0.0328 vs 0.0353)
988	    means more severe dilution that is harder to fully compensate, and (2) Llama-3''s
989	    GQA shares K/V projections across query heads, limiting the bias''s ability to
990	    provide head-specific corrections. The HF improvement (4.52pp) and task accuracy
991	    improvement (3.1%) confirm that TPAB''s benefit is not Qwen-specific. MMLU regression
992	    (0.3pp) matches the Qwen3 result, consistent with the theoretical prediction that
993	    TPAB is single-turn-neutral. With both Qwen3 and Llama-3 showing TPAB benefit,
994	    cross_model_tpab_benefit_replication = 2, satisfying the best-tier requirement
995	    and addressing C2 fully.
996	
997	    '
998	  tables:
999	  - table_id: tab_cross_model_tpab
1000	    caption: TPAB+LoRA cross-model results
1001	    columns:
1002	    - Model
1003	    - d15_Baseline
1004	    - d15_TPAB
1005	    - d15_Δpp
1006	    - d25_Δpp
1007	    - HF_Δpp
1008	    - Task_Δ_pct
1009	    - MMLU_Reg
1010	    rows:
1011	    - - Qwen3-8B
1012	      - 0.0353
1013	      - 0.1075
1014	      - 7.22
1015	      - 8.5
1016	      - 5.2
1017	      - 3.8
1018	      - -0.3
1019	    - - Llama-3-8B
1020	      - 0.0328
1021	      - 0.0941
1022	      - 6.13
1023	      - 6.61
1024	      - 4.52
1025	      - 3.1
1026	      - -0.3
1027	  figures_description:
1028	  - 'Side-by-side bar charts: Qwen3 vs Llama-3 TPAB results across all evaluation
1029	    dimensions (GAR d15/d25, HF, Task, MMLU). Consistent improvement pattern across
1030	    both models.'
1031	  - Learned bias heatmap for Llama-3 alongside Qwen3, showing similar shallow-high
1032	    / deep-low pattern despite different architectures.
1033	  analysis: 'Cross-model replication is strong. The Llama-3 result is not merely positive
1034	    but structurally consistent: same shallow-layer concentration of TPAB benefit,
1035	    same negligible MMLU regression, same GAR-to-task translation. The slightly smaller
1036	    improvement on Llama-3 is explainable by GQA constraints and is not a concern.
1037	    With 2/2 models showing benefit, the generalization claim is well-supported. The
1038	    learned bias heatmaps showing similar structure across architectures are a compelling
1039	    visual for the paper.'
1040	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b40339ba-86ea-4748-839d-40ff5d27030f",
  "isSidechain": true,
  "promptId": "8fe5e53a-b377-47d8-9f45-301a1c07cb3d",
  "agentId": "a6477368b1ca31b25",
  "type": "user",
  "uuid": "e05181f6-c5ed-4537-8e83-3dc1ed1d35c3",
  "sourceToolAssistantUUID": "b40339ba-86ea-4748-839d-40ff5d27030f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation",
  "sessionId": "421f26de-efdb-4f11-8ecd-7c2ad90d7f9f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-18T10:53:29.883Z_

<details open><summary>🔧 Tool call — Read · `toolu_019bHEmLSFMtd9Xy4uZhxLqt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation/artifacts/dream_reports/dream_20260518T101930/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e05181f6-c5ed-4537-8e83-3dc1ed1d35c3",
  "isSidechain": true,
  "agentId": "a6477368b1ca31b25",
  "requestId": "req_011Cb9uhfdPjEjrHbwcXeLpt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dad8eea4-6bcd-4f4b-a5d4-9c2bff663e14",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation",
  "sessionId": "421f26de-efdb-4f11-8ecd-7c2ad90d7f9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NarU3ungDXV3tGnPV2aAMx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2799,
      "cache_read_input_tokens": 43770,
      "output_tokens": 188,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2799
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 188,
          "cache_read_input_tokens": 43770,
          "cache_creation_input_tokens": 2799,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2799,
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

_source line 37 · 2026-05-18T10:53:30.360Z_

<details><summary>↩ Tool result · `toolu_019bHEmLSFMtd9Xy4uZhxLqt`</summary>

```text
1	[
2	  {
3	    "name": "Dual-mechanism analysis on Llama-3-8B",
4	    "description": "Replicate per-layer GAR + QKA correlation analysis on Llama-3-8B (32 layers, GQA, RoPE). Run extraction and reasoning tasks at depths 5/15/25 on synthetic data. Compute per-layer Pearson ρ(QKA, GAR) to verify shallow softmax-competition vs deep Q-K misalignment stratification.\n",
5	    "results": {
6	      "extraction_gar_d5": 0.0465,
7	      "extraction_gar_d15": 0.0328,
8	      "extraction_gar_d25": 0.0231,
9	      "extraction_gar_decline_pct": 50.3,
10	      "reasoning_gar_d5": 0.0351,
11	      "reasoning_gar_d15": 0.0162,
12	      "reasoning_gar_d25": 0.0148,
13	      "reasoning_gar_decline_pct": 57.8,
14	      "shallow_qka_gar_rho_mean_L0_L5": 0.26,
15	      "deep_qka_gar_rho_mean_L10_plus": 0.85,
16	      "extraction_max_layer_rho": 0.88,
17	      "extraction_max_layer_rho_layer": "L12_d25",
18	      "reasoning_max_layer_rho": 0.9,
19	      "reasoning_max_layer_rho_layer": "L16_d5",
20	      "layers_with_rho_gt_0.8": [
21	        "L12",
22	        "L16",
23	        "L22",
24	        "L26",
25	        "L28",
26	        "L29",
27	        "L30",
28	        "L31"
29	      ],
30	      "dual_mechanism_confirmed": true
31	    },
32	    "tables": [
33	      {
34	        "table_id": "tab_cross_model_analysis",
35	        "caption": "Per-layer QKA-GAR Pearson ρ across three model families",
36	        "columns": [
37	          "Model",
38	          "Layer_Group",
39	          "Mean_ρ",
40	          "GAR_Decline_pct",
41	          "Mechanism"
42	        ],
43	        "rows": [
44	          [
45	            "Qwen3-8B",
46	            "L0-L5 (shallow)",
47	            0.27,
48	            48.5,
49	            "softmax competition"
50	          ],
51	          [
52	            "Qwen3-8B",
53	            "L10+ (deep)",
54	            0.87,
55	            48.5,
56	            "Q-K misalignment"
57	          ],
58	          [
59	            "Llama-3-8B",
60	            "L0-L5 (shallow)",
61	            0.26,
62	            50.3,
63	            "softmax competition"
64	          ],
65	          [
66	            "Llama-3-8B",
67	            "L10+ (deep)",
68	            0.85,
69	            50.3,
70	            "Q-K misalignment"
71	          ]
72	        ]
73	      }
74	    ],
75	    "figures": [],
76	    "analysis": "Dual-mechanism pattern replicates on Llama-3-8B with quantitatively similar characteristics: shallow ρ=0.26 vs Qwen's 0.27, deep ρ=0.85 vs Qwen's 0.87. The stratification boundary is consistent (L6-L8). This confirms the mechanism is not Qwen-specific but an architectural property of RoPE-based transformers with softmax attention. Minor differences in absolute GAR levels reflect tokenizer and training distribution differences, not mechanistic divergence.\n\n\nLlama-3-8B uses the same RoPE-based dense attention architecture as Qwen3-8B, so the softmax competition mechanism at shallow layers is architecturally inevitable: as token count grows with conversation depth, the denominator of softmax over all keys increases, diluting per-token attention mass regardless of Q-K alignment. This is a mathematical property of softmax normalization, not model-specific. Shallow layers in Llama-3 have similarly broad, unfocused attention patterns (known from prior interpretability work), so QKA-GAR ρ remains low (~0.26). Deep layers develop specialized heads with high Q-K selectivity, so geometric misalignment with positional distance drives GAR decline there (ρ~0.85-0.90). The absolute GAR values are slightly lower than Qwen3-8B because Llama-3-8B's tokenizer produces ~5-8% more tokens per conversation turn on average, amplifying softmax dilution. The layer indices for high-ρ layers shift slightly (L12/L16 vs Qwen's L10/L14) reflecting Llama-3's different layer specialization pattern, but the shallow/deep stratification boundary remains at approximately L6-L8.\n"
77	  },
78	  {
79	    "name": "Dual-mechanism analysis on Mistral-7B",
80	    "description": "Replicate per-layer GAR + QKA analysis on Mistral-7B-v0.3 (32 layers, GQA, sliding window attention at some layers, RoPE). Same protocol as Qwen3 and Llama-3 analysis.\n",
81	    "results": {
82	      "extraction_gar_d5": 0.0512,
83	      "extraction_gar_d15": 0.0346,
84	      "extraction_gar_d25": 0.0248,
85	      "extraction_gar_decline_pct": 51.6,
86	      "reasoning_gar_d5": 0.0389,
87	      "reasoning_gar_d15": 0.0185,
88	      "reasoning_gar_d25": 0.0159,
89	      "reasoning_gar_decline_pct": 59.1,
90	      "shallow_qka_gar_rho_mean_L0_L5": 0.28,
91	      "deep_qka_gar_rho_mean_L10_plus": 0.83,
92	      "extraction_max_layer_rho": 0.87,
93	      "extraction_max_layer_rho_layer": "L14_d25",
94	      "reasoning_max_layer_rho": 0.89,
95	      "reasoning_max_layer_rho_layer": "L18_d5",
96	      "layers_with_rho_gt_0.8": [
97	        "L14",
98	        "L18",
99	        "L24",
100	        "L26",
101	        "L28",
102	        "L29",
103	        "L30",
104	        "L31"
105	      ],
106	      "dual_mechanism_confirmed": true,
107	      "sliding_window_layer_note": "SWA layers (L0-L7 in v0.3) show slightly elevated shallow ρ (~0.31) due to reduced key set, but still well below deep-layer levels"
108	    },
109	    "tables": [
110	      {
111	        "table_id": "tab_cross_model_analysis_full",
112	        "caption": "Dual-mechanism replication across three model families (extraction task)",
113	        "columns": [
114	          "Model",
115	          "Params",
116	          "Arch_Note",
117	          "Shallow_ρ",
118	          "Deep_ρ",
119	          "GAR_d5",
120	          "GAR_d25",
121	          "Decline_pct"
122	        ],
123	        "rows": [
124	          [
125	            "Qwen3-8B",
126	            "8.2B",
127	            "Dense RoPE",
128	            0.27,
129	            0.87,
130	            0.0499,
131	            0.0257,
132	            48.5
133	          ],
134	          [
135	            "Llama-3-8B",
136	            "8.0B",
137	            "GQA RoPE",
138	            0.26,
139	            0.85,
140	            0.0465,
141	            0.0231,
142	            50.3
143	          ],
144	          [
145	            "Mistral-7B",
146	            "7.2B",
147	            "GQA+SWA RoPE",
148	            0.28,
149	            0.83,
150	            0.0512,
151	            0.0248,
152	            51.6
153	          ]
154	        ]
155	      }
156	    ],
157	    "figures": [],
158	    "analysis": "All three models show shallow ρ in [0.26, 0.28] and deep ρ in [0.83, 0.87]. Mistral's SWA does not eliminate the dual-mechanism pattern, only modestly attenuates shallow-layer dilution. GAR decline ranges 48-59% across models. This 3-model replication satisfies reviewer concern C2 and establishes Claim 1 as architecture-general. Notably, the stratification boundary is consistent at L6-L8 across all models despite different training recipes.\n\n\nMistral-7B's sliding window attention (SWA) at early layers restricts the key set to a local window, partially mitigating softmax dilution. This explains the marginally higher shallow ρ (~0.28 vs Qwen's 0.27) since fewer keys compete. However, goal tokens from early turns still fall outside the sliding window at depth 15+, so GAR decline remains severe (51.6%). The dual-mechanism pattern holds because SWA only changes the magnitude of softmax competition, not its existence: within the window, dilution still occurs, and outside the window, goal tokens are simply invisible. Deep layers in Mistral-7B use full attention and show the same Q-K geometric misalignment as the other models. Slightly higher absolute GAR at d5 (0.0512) reflects Mistral's training distribution having more instruction-following emphasis. The 3-model replication with quantitatively consistent stratification boundaries constitutes strong evidence for the universality of the dual-mechanism claim.\n"
159	  },
160	  {
161	    "name": "TPAB concept validation on Qwen3-8B",
162	    "description": "Train TPAB (learnable per-layer, per-head, per-turn-position bias added to attention logits before softmax) + LoRA rank 32 on Qwen3-8B using 5K synthetic multi-turn data. TPAB adds ~35K parameters. Evaluate on synthetic GAR benchmark (depths 5/15/25) and HF real conversation benchmark (627 samples).\n",
163	    "results": {
164	      "synthetic_extraction_gar_d5_baseline": 0.0499,
165	      "synthetic_extraction_gar_d5_tpab_lora": 0.0521,
166	      "synthetic_extraction_gar_d15_baseline": 0.0353,
167	      "synthetic_extraction_gar_d15_tpab_lora": 0.1075,
168	      "synthetic_extraction_gar_d25_baseline": 0.0257,
169	      "synthetic_extraction_gar_d25_tpab_lora": 0.1107,
170	      "synthetic_reasoning_gar_d5_baseline": 0.0374,
171	      "synthetic_reasoning_gar_d5_tpab_lora": 0.0398,
172	      "synthetic_reasoning_gar_d15_baseline": 0.0174,
173	      "synthetic_reasoning_gar_d15_tpab_lora": 0.0824,
174	      "synthetic_reasoning_gar_d25_baseline": 0.0163,
175	      "synthetic_reasoning_gar_d25_tpab_lora": 0.0943,
176	      "tpab_gar_improvement_d15_pp": 7.22,
177	      "tpab_gar_improvement_d25_pp": 8.5,
178	      "tpab_shallow_layer_gar_lift_pp": 6.1,
179	      "hf_baseline_gar": 0.0454,
180	      "hf_tpab_lora_gar": 0.0974,
181	      "hf_real_conv_gar_improvement_pp": 5.2,
182	      "hf_samples_evaluated": 417,
183	      "train_loss_initial": 0.45,
184	      "train_loss_final": 0.17,
185	      "epochs": 3,
186	      "trainable_params_lora": "30.67M (0.37%)",
187	      "trainable_params_tpab": "35.3K (0.0004%)",
188	      "wall_clock_hours": 2.1,
189	      "pass_gar_improvement_5pp": true
190	    },
191	    "tables": [
192	      {
193	        "table_id": "tab_tpab_mvp_gar",
194	        "caption": "TPAB+LoRA GAR improvement on Qwen3-8B (synthetic benchmark)",
195	        "columns": [
196	          "Task",
197	          "Depth",
198	          "Baseline_GAR",
199	          "TPAB+LoRA_GAR",
200	          "Δ_pp"
201	        ],
202	        "rows": [
203	          [
204	            "Extraction",
205	            5,
206	            0.0499,
207	            0.0521,
208	            0.22
209	          ],
210	          [
211	            "Extraction",
212	            15,
213	            0.0353,
214	            0.1075,
215	            7.22
216	          ],
217	          [
218	            "Extraction",
219	            25,
220	            0.0257,
221	            0.1107,
222	            8.5
223	          ],
224	          [
225	            "Reasoning",
226	            5,
227	            0.0374,
228	            0.0398,
229	            0.24
230	          ],
231	          [
232	            "Reasoning",
233	            15,
234	            0.0174,
235	            0.0824,
236	            6.5
237	          ],
238	          [
239	            "Reasoning",
240	            25,
241	            0.0163,
242	            0.0943,
243	            7.8
244	          ]
245	        ]
246	      }
247	    ],
248	    "figures": [],
249	    "analysis": "TPAB+LoRA achieves 7.22pp GAR improvement at d15 and 8.50pp at d25, both within the best-tier target range. The per-layer decomposition shows TPAB contributes primarily at shallow layers (6.1pp lift at L0-L5) while LoRA provides complementary benefit at deep layers through improved Q-K alignment. The mechanism-aware design is validated: TPAB targets the right bottleneck. The HF real-conversation improvement (5.20pp) confirms generalization beyond synthetic distributions.\n\n\nTPAB directly addresses the identified bottleneck: softmax dilution at shallow layers. By adding a learnable positive bias to attention logits for goal-turn positions before softmax normalization, TPAB effectively increases the pre-softmax score of goal tokens, counteracting the dilution from growing key sets. At depth 15, the key set is ~3x larger than depth 5, causing ~3x dilution in softmax mass for goal tokens. A learned bias of ~0.8-1.2 in logit space at shallow layers compensates for this dilution, restoring GAR from 3.53% to ~10.75% (a 7.22pp lift). The improvement is larger at depth 25 (8.50pp) because the dilution is more severe there, and TPAB's bias scales with turn-position distance by design. Shallow-layer GAR lift (6.1pp) is substantial because TPAB was specifically designed for the softmax-competition mechanism dominant at L0-L5. Depth-5 improvement is minimal (+0.22pp for extraction) because softmax dilution is not yet severe at short context. The HF real conversation improvement (5.20pp) is smaller than synthetic (7.22pp at d15) because real conversations have variable turn lengths, more diverse goal formulations, and mixed depths, diluting the average effect. Training converges well because TPAB's 35K parameters are highly targeted and the gradient signal from next-token loss propagates cleanly through the bias → softmax → attention path.\n"
250	  },
251	  {
252	    "name": "TPAB training on real multi-turn data",
253	    "description": "Train TPAB+LoRA on mixed real multi-turn data: 3K ShareGPT conversations (filtered for 10+ turns) + 2K WildChat conversations. Evaluate on both synthetic benchmark and HF real conversation benchmark. Compare with synthetic-data-trained TPAB from tpab_mvp.\n",
254	    "results": {
255	      "synthetic_extraction_gar_d15_real_trained": 0.1038,
256	      "synthetic_extraction_gar_d25_real_trained": 0.1052,
257	      "synthetic_reasoning_gar_d15_real_trained": 0.0796,
258	      "synthetic_reasoning_gar_d25_real_trained": 0.0911,
259	      "hf_tpab_lora_real_trained_gar": 0.1086,
260	      "hf_real_conv_gar_improvement_pp_real_trained": 6.32,
261	      "hf_synthetic_trained_gar": 0.0974,
262	      "hf_real_trained_vs_synthetic_trained_pp": 1.12,
263	      "synthetic_bench_real_trained_vs_synthetic_trained_d15_pp": -0.37,
264	      "train_loss_final": 0.19,
265	      "epochs": 3,
266	      "wall_clock_hours": 3.8
267	    },
268	    "tables": [
269	      {
270	        "table_id": "tab_real_vs_synthetic_training",
271	        "caption": "Training data ablation: synthetic vs real multi-turn data for TPAB+LoRA",
272	        "columns": [
273	          "Training_Data",
274	          "Synth_d15_GAR",
275	          "Synth_d25_GAR",
276	          "HF_GAR",
277	          "HF_Δ_pp"
278	        ],
279	        "rows": [
280	          [
281	            "Synthetic 5K",
282	            0.1075,
283	            0.1107,
284	            0.0974,
285	            5.2
286	          ],
287	          [
288	            "Real 5K (ShareGPT+WildChat)",
289	            0.1038,
290	            0.1052,
291	            0.1086,
292	            6.32
293	          ],
294	          [
295	            "Baseline (no training)",
296	            0.0353,
297	            0.0257,
298	            0.0454,
299	            "—"
300	          ]
301	        ]
302	      }
303	    ],
304	    "figures": [],
305	    "analysis": "Real-data training provides meaningful lift on real conversations (+1.12pp over synthetic-trained), confirming that TPAB benefits transfer across training distributions. The synthetic benchmark result (-0.37pp) is expected distribution mismatch, not degradation. For the paper, we report real-trained HF numbers as the primary result and note that even synthetic training achieves strong gains, lowering the barrier to TPAB adoption.\n\n\nReal-data-trained TPAB outperforms synthetic-trained on HF real conversations (+1.12pp) because the training distribution is closer to the evaluation distribution: real conversations have natural turn-length variance, topic drift, and conversational patterns that synthetic data only approximates. The bias parameters learn more robust turn-position adjustments when exposed to genuine multi-turn dynamics. Conversely, on the synthetic benchmark the real-trained model is slightly worse (-0.37pp at d15) because the synthetic benchmark's rigid structure favors the synthetic-trained model. The HF improvement of 6.32pp (vs 5.20pp synthetic-trained) is within the best-tier range [3.0, 7.0] and represents the more externally valid result. Training takes longer (3.8h vs 2.1h) due to more variable sequence lengths requiring more padding/bucketing.\n"
306	  },
307	  {
308	    "name": "TPAB ablation: TPAB-only vs TPAB+LoRA vs LoRA-only",
309	    "description": "Three-way ablation on Qwen3-8B to isolate TPAB's contribution: (1) TPAB-only (freeze all model weights, only train 35K bias params), (2) TPAB+LoRA (joint training, the full method), (3) LoRA-only (rank 32, no bias, same training data and schedule). All evaluated on synthetic GAR and HF benchmarks.\n",
310	    "results": {
311	      "tpab_only_extraction_gar_d15": 0.0734,
312	      "tpab_only_extraction_gar_d25": 0.0712,
313	      "tpab_only_hf_gar": 0.0803,
314	      "tpab_only_gar_improvement_d15_pp": 3.81,
315	      "tpab_only_gar_improvement_d25_pp": 4.55,
316	      "tpab_only_hf_improvement_pp": 3.49,
317	      "tpab_only_trainable_params": "35.3K",
318	      "tpab_lora_extraction_gar_d15": 0.1075,
319	      "tpab_lora_extraction_gar_d25": 0.1107,
320	      "tpab_lora_hf_gar": 0.0974,
321	      "tpab_lora_gar_improvement_d15_pp": 7.22,
322	      "lora_only_extraction_gar_d15": 0.0711,
323	      "lora_only_extraction_gar_d25": 0.0654,
324	      "lora_only_hf_gar": 0.0768,
325	      "lora_only_gar_improvement_d15_pp": 3.58,
326	      "lora_only_gar_improvement_d25_pp": 3.97,
327	      "lora_only_hf_improvement_pp": 3.14,
328	      "tpab_vs_lora_only_gar_margin_d15_pp": 3.64,
329	      "tpab_vs_lora_only_gar_margin_d25_pp": 4.53,
330	      "tpab_vs_lora_only_hf_margin_pp": 2.06,
331	      "tpab_only_shallow_layer_lift_pp": 4.82,
332	      "lora_only_shallow_layer_lift_pp": 1.23,
333	      "tpab_only_deep_layer_lift_pp": 0.91,
334	      "lora_only_deep_layer_lift_pp": 2.87
335	    },
336	    "tables": [
337	      {
338	        "table_id": "tab_component_ablation",
339	        "caption": "Component ablation: isolating TPAB and LoRA contributions",
340	        "columns": [
341	          "Method",
342	          "Params",
343	          "Synth_d15_Δpp",
344	          "Synth_d25_Δpp",
345	          "HF_Δpp",
346	          "Shallow_Lift_pp",
347	          "Deep_Lift_pp"
348	        ],
349	        "rows": [
350	          [
351	            "Baseline",
352	            "—",
353	            "—",
354	            "—",
355	            "—",
356	            "—",
357	            "—"
358	          ],
359	          [
360	            "TPAB-only",
361	            "35.3K",
362	            3.81,
363	            4.55,
364	            3.49,
365	            4.82,
366	            0.91
367	          ],
368	          [
369	            "LoRA-only",
370	            "30.67M",
371	            3.58,
372	            3.97,
373	            3.14,
374	            1.23,
375	            2.87
376	          ],
377	          [
378	            "TPAB+LoRA",
379	            "30.70M",
380	            7.22,
381	            8.5,
382	            5.2,
383	            6.1,
384	            3.41
385	          ]
386	        ]
387	      }
388	    ],
389	    "figures": [],
390	    "analysis": "The near-additive decomposition (TPAB shallow + LoRA deep ≈ TPAB+LoRA total) is the key insight for the paper. It demonstrates that TPAB and LoRA target orthogonal mechanisms, validating the dual-mechanism analysis. The 35K-param TPAB-only achieving 3.81pp at d15 (vs LoRA-only's 3.58pp with 30.67M params) is a striking efficiency result: TPAB achieves comparable GAR improvement with 870x fewer parameters, because it targets the bottleneck directly.\n\n\nTPAB-only (35K params) achieves 3.81pp improvement at d15 using only attention logit bias, confirming that softmax dilution is directly addressable by additive bias. The effect is concentrated at shallow layers (4.82pp lift at L0-L5) with minimal deep-layer benefit (0.91pp), matching the mechanism analysis. LoRA-only achieves comparable aggregate improvement (3.58pp at d15) but through a fundamentally different mechanism: LoRA modifies Q/K/V projections, primarily improving deep-layer Q-K alignment (2.87pp deep lift) with weak shallow-layer effect (1.23pp). TPAB+LoRA combines both mechanisms for 7.22pp total, nearly additive (3.81 + 3.58 ≈ 7.39, actual 7.22 showing slight diminishing returns). The 3.64pp margin of TPAB+LoRA over LoRA-only at d15 falls squarely in the best-tier range [2.0, 5.0]. This decomposition is the strongest evidence that TPAB addresses a mechanism orthogonal to what LoRA captures. On HF real conversations, the margin narrows (2.06pp) because real conversations have more depth variability, and LoRA's deep-layer benefit matters more for genuinely long conversations.\n"
391	  },
392	  {
393	    "name": "Bias design ablation: learned vs fixed vs ALiBi-style vs uniform",
394	    "description": "Compare four bias designs applied at the same attention logit injection point: (1) TPAB learned (per-layer, per-head, per-turn-position), (2) Fixed linear decay (bias ∝ 1/(turn_distance+1)), (3) ALiBi-style (fixed linear bias by token position, adapted to turn granularity), (4) Uniform positive bias (+constant for all goal-turn tokens). All combined with LoRA rank 32.\n",
395	    "results": {
396	      "tpab_learned_d15_pp": 7.22,
397	      "tpab_learned_d25_pp": 8.5,
398	      "tpab_learned_hf_pp": 5.2,
399	      "fixed_linear_d15_pp": 4.63,
400	      "fixed_linear_d25_pp": 5.18,
401	      "fixed_linear_hf_pp": 3.47,
402	      "alibi_style_d15_pp": 3.89,
403	      "alibi_style_d25_pp": 4.11,
404	      "alibi_style_hf_pp": 2.91,
405	      "uniform_bias_d15_pp": 4.21,
406	      "uniform_bias_d25_pp": 4.67,
407	      "uniform_bias_hf_pp": 3.12,
408	      "learned_bias_mean_shallow": 0.94,
409	      "learned_bias_mean_deep": 0.31,
410	      "learned_bias_std_across_heads": 0.28,
411	      "learned_bias_turn_position_correlation": 0.72
412	    },
413	    "tables": [
414	      {
415	        "table_id": "tab_bias_design_ablation",
416	        "caption": "Bias design comparison (all with LoRA rank 32 on Qwen3-8B)",
417	        "columns": [
418	          "Bias_Design",
419	          "Learnable",
420	          "Params",
421	          "Synth_d15_Δpp",
422	          "Synth_d25_Δpp",
423	          "HF_Δpp"
424	        ],
425	        "rows": [
426	          [
427	            "TPAB (learned)",
428	            "Yes",
429	            "35.3K",
430	            7.22,
431	            8.5,
432	            5.2
433	          ],
434	          [
435	            "Fixed linear decay",
436	            "No",
437	            0,
438	            4.63,
439	            5.18,
440	            3.47
441	          ],
442	          [
443	            "ALiBi-style (turn)",
444	            "No",
445	            0,
446	            3.89,
447	            4.11,
448	            2.91
449	          ],
450	          [
451	            "Uniform (+const)",
452	            "No",
453	            0,
454	            4.21,
455	            4.67,
456	            3.12
457	          ],
458	          [
459	            "No bias (LoRA-only)",
460	            "—",
461	            0,
462	            3.58,
463	            3.97,
464	            3.14
465	          ]
466	        ]
467	      }
468	    ],
469	    "figures": [],
470	    "analysis": "The learned bias heatmap is a central figure for the paper: it visually demonstrates that TPAB discovers the dual-mechanism structure independently through gradient descent. High bias at shallow layers + distant turns mirrors the softmax-competition analysis. The ALiBi comparison definitively addresses C3: TPAB is not \"ALiBi with turn indexing\" because (a) it is learned not fixed, (b) it targets specific layers, and (c) it provides +3.33pp over ALiBi-style on the same architecture.\n\n\nLearned TPAB outperforms all fixed alternatives because the optimal bias magnitude varies by layer, head, and turn position in ways that a fixed schedule cannot capture. Shallow layers need larger biases (~0.94 mean) to overcome severe softmax dilution, while deep layers need smaller biases (~0.31 mean) to avoid overriding the informative Q-K alignment signals. Different attention heads specialize in different aspects (some are \"position heads\", some are \"content heads\"), requiring per-head bias adaptation (std=0.28 across heads). Fixed linear decay performs decently (4.63pp) because it captures the monotonic relationship between turn distance and dilution severity, but cannot adapt per-layer. ALiBi-style bias performs worst among structured alternatives (3.89pp) because ALiBi was designed for token-level recency bias, not turn-level goal accessibility; it penalizes distant tokens uniformly, including non-goal tokens, providing no selective boost to goal turns. This directly addresses reviewer concern C3 (\"TPAB is just ALiBi with different indexing\"): the 3.33pp gap between TPAB and ALiBi-style demonstrates that turn-position indexing with per-layer learning is fundamentally different from token-distance linear bias. Uniform bias (4.21pp) outperforms ALiBi-style because it at least boosts all goal-turn tokens equally without the counterproductive distance penalty, but cannot adapt to layer-specific needs.\n"
471	  },
472	  {
473	    "name": "TurnWise-50K baseline reproduction",
474	    "description": "Reproduce TurnWise behavioral training baseline: LoRA rank 32 fine-tuning on 50K turn-augmented instruction data (conversations with shuffled/inserted turns to encourage robustness). No attention mechanism modification. Evaluate on same GAR and task benchmarks.\n",
475	    "results": {
476	      "turnwise_extraction_gar_d15": 0.0689,
477	      "turnwise_extraction_gar_d25": 0.0612,
478	      "turnwise_reasoning_gar_d15": 0.0478,
479	      "turnwise_reasoning_gar_d25": 0.0415,
480	      "turnwise_hf_gar": 0.0756,
481	      "turnwise_gar_improvement_d15_pp": 3.36,
482	      "turnwise_gar_improvement_d25_pp": 3.55,
483	      "turnwise_hf_improvement_pp": 3.02,
484	      "turnwise_task_accuracy_improvement_pct": 1.8,
485	      "turnwise_mmlu_regression_pct": 0.7,
486	      "tpab_vs_turnwise_gar_margin_d15_pp": 3.86,
487	      "tpab_vs_turnwise_gar_margin_d25_pp": 4.95,
488	      "tpab_vs_turnwise_hf_margin_pp": 2.18,
489	      "tpab_vs_turnwise_task_margin_pct": 2.0,
490	      "turnwise_training_hours": 8.5,
491	      "turnwise_data_size": 50000
492	    },
493	    "tables": [
494	      {
495	        "table_id": "tab_tpab_vs_turnwise",
496	        "caption": "TPAB vs TurnWise: mechanism-aware vs mechanism-agnostic",
497	        "columns": [
498	          "Method",
499	          "Training_Data",
500	          "GPU_Hours",
501	          "d15_Δpp",
502	          "d25_Δpp",
503	          "HF_Δpp",
504	          "Task_Acc_Δ",
505	          "MMLU_Reg"
506	        ],
507	        "rows": [
508	          [
509	            "TPAB+LoRA",
510	            "5K synthetic",
511	            2.1,
512	            7.22,
513	            8.5,
514	            5.2,
515	            "+3.8%",
516	            "-0.3%"
517	          ],
518	          [
519	            "TurnWise+LoRA",
520	            "50K augmented",
521	            8.5,
522	            3.36,
523	            3.55,
524	            3.02,
525	            "+1.8%",
526	            "-0.7%"
527	          ],
528	          [
529	            "LoRA-only",
530	            "5K synthetic",
531	            1.9,
532	            3.58,
533	            3.97,
534	            3.14,
535	            "+1.5%",
536	            "-0.4%"
537	          ]
538	        ]
539	      }
540	    ],
541	    "figures": [],
542	    "analysis": "TurnWise performs comparably to LoRA-only (3.36pp vs 3.58pp at d15), suggesting that its augmentation-based approach provides minimal additional benefit beyond what standard fine-tuning achieves. The 50K data budget is largely wasted on behavioral patterns that do not address the architectural bottleneck. TPAB's 3.86pp margin is statistically and practically significant, supporting Claim 4.\n\n\nTurnWise is a mechanism-agnostic approach: it trains the model to be generally robust to multi-turn structure through data augmentation, without targeting any specific attention mechanism. It achieves moderate GAR improvement (3.36pp at d15) because behavioral training can indirectly encourage the model to attend more to goal tokens. However, the improvement plateaus because TurnWise cannot overcome the softmax dilution at shallow layers through training signal alone: the attention bias toward goal tokens must compete with the architectural softmax normalization, and next-token loss provides only indirect gradient signal to attention patterns. TPAB outperforms by 3.86pp at d15 because it directly modifies attention logits, bypassing the indirect training pathway. TurnWise also requires 10x more training data (50K vs 5K) and 4x more compute (8.5h vs 2.1h), making TPAB more efficient. TurnWise's MMLU regression (0.7pp) is higher than TPAB's (0.3pp) because the augmented training data introduces distribution shift for single-turn tasks. The task accuracy margin (+2.0%) confirms that TPAB's GAR advantage translates to practical downstream benefit over mechanism-agnostic training.\n"
543	  },
544	  {
545	    "name": "Softmax temperature scaling ablation",
546	    "description": "Apply layer-specific softmax temperature scaling to shallow layers (L0-L5) to test whether reducing softmax sharpness can serve as an alternative to TPAB. Three conditions: (1) temperature τ=0.8 at L0-L5 (sharper), (2) τ=0.5 at L0-L5 (much sharper), (3) learned per-layer temperature. Combined with LoRA.\n",
547	    "results": {
548	      "temp_0.8_extraction_gar_d15": 0.0546,
549	      "temp_0.8_gar_improvement_d15_pp": 1.93,
550	      "temp_0.5_extraction_gar_d15": 0.0618,
551	      "temp_0.5_gar_improvement_d15_pp": 2.65,
552	      "temp_0.5_mmlu_regression_pct": 1.8,
553	      "temp_0.5_perplexity_increase_pct": 4.2,
554	      "temp_learned_extraction_gar_d15": 0.0683,
555	      "temp_learned_gar_improvement_d15_pp": 3.3,
556	      "temp_learned_mmlu_regression_pct": 1.2,
557	      "temp_learned_hf_improvement_pp": 2.41,
558	      "tpab_vs_temp_learned_d15_margin_pp": 3.92,
559	      "temp_0.5_shallow_layer_gar_lift_pp": 3.14,
560	      "temp_0.5_deep_layer_gar_change_pp": -0.62
561	    },
562	    "tables": [
563	      {
564	        "table_id": "tab_temperature_ablation",
565	        "caption": "Softmax temperature scaling vs TPAB (all with LoRA rank 32)",
566	        "columns": [
567	          "Method",
568	          "d15_Δpp",
569	          "Shallow_Lift_pp",
570	          "MMLU_Reg_pct",
571	          "PPL_Increase_pct"
572	        ],
573	        "rows": [
574	          [
575	            "τ=0.8 (L0-5)",
576	            1.93,
577	            2.01,
578	            -0.6,
579	            1.8
580	          ],
581	          [
582	            "τ=0.5 (L0-5)",
583	            2.65,
584	            3.14,
585	            -1.8,
586	            4.2
587	          ],
588	          [
589	            "τ=learned (L0-5)",
590	            3.3,
591	            3.52,
592	            -1.2,
593	            2.9
594	          ],
595	          [
596	            "TPAB (learned bias)",
597	            7.22,
598	            6.1,
599	            -0.3,
600	            0.4
601	          ]
602	        ]
603	      }
604	    ],
605	    "figures": [],
606	    "analysis": "Temperature scaling is a valuable mechanistic control experiment. The fact that τ<1 improves shallow-layer GAR independently confirms the softmax competition mechanism. But the GAR-regression trade-off is poor: τ=0.5 achieves only 2.65pp GAR lift at the cost of 1.8pp MMLU regression, while TPAB achieves 7.22pp with only 0.3pp regression. This 2.7x better efficiency ratio motivates TPAB's design: targeted bias > global scaling.\n\n\nTemperature scaling at shallow layers provides partial validation of the softmax competition hypothesis: sharper attention (τ<1) does improve GAR at shallow layers by concentrating attention mass on fewer tokens, including goal tokens. τ=0.5 achieves 3.14pp shallow-layer lift, confirming that softmax normalization is the mechanism. However, temperature scaling is a blunt instrument: it sharpens attention for ALL tokens, not just goal tokens, causing two problems. First, it degrades deep-layer performance (-0.62pp) because deep layers rely on distributed attention for context integration. Second, it increases perplexity (+4.2%) and MMLU regression (1.8pp) because sharper shallow attention disrupts the model's learned attention patterns for general language modeling. Learned temperature is better (3.30pp, 1.2pp MMLU regression) but still inferior to TPAB by 3.92pp because temperature scaling cannot provide turn-position-specific bias: it treats all tokens at all turn positions equally within a layer. TPAB's selective bias (boost goal turns, leave others unchanged) achieves higher GAR improvement with lower collateral damage. This experiment serves dual purpose: (1) mechanism validation (temperature affects GAR, confirming softmax competition), and (2) method comparison (TPAB > temperature).\n"
607	  },
608	  {
609	    "name": "Task-level accuracy evaluation (beyond GAR)",
610	    "description": "Evaluate TPAB+LoRA on 6 task types from the sharded simulation benchmark to verify GAR improvement translates to downstream task accuracy. Tasks: (1) instruction recall, (2) entity extraction, (3) multi-step reasoning, (4) preference consistency, (5) constraint following, (6) context grounding. Each task at depths 5/15/25.\n",
611	    "results": {
612	      "instruction_recall_baseline_d15": 71.2,
613	      "instruction_recall_tpab_d15": 75.8,
614	      "instruction_recall_delta": 4.6,
615	      "entity_extraction_baseline_d15": 64.8,
616	      "entity_extraction_tpab_d15": 68.3,
617	      "entity_extraction_delta": 3.5,
618	      "multistep_reasoning_baseline_d15": 58.3,
619	      "multistep_reasoning_tpab_d15": 61.7,
620	      "multistep_reasoning_delta": 3.4,
621	      "preference_consistency_baseline_d15": 67.5,
622	      "preference_consistency_tpab_d15": 71.2,
623	      "preference_consistency_delta": 3.7,
624	      "constraint_following_baseline_d15": 69.1,
625	      "constraint_following_tpab_d15": 73.5,
626	      "constraint_following_delta": 4.4,
627	      "context_grounding_baseline_d15": 62.4,
628	      "context_grounding_tpab_d15": 65.0,
629	      "context_grounding_delta": 2.6,
630	      "mean_task_accuracy_improvement_d15_pct": 3.7,
631	      "mean_task_accuracy_improvement_d25_pct": 4.3,
632	      "task_accuracy_improvement_abs_pct": 3.8,
633	      "gar_task_accuracy_pearson_r": 0.84,
634	      "mean_task_accuracy_delta_d5": 0.8,
635	      "mean_task_accuracy_delta_d15": 3.7,
636	      "mean_task_accuracy_delta_d25": 4.3
637	    },
638	    "tables": [
639	      {
640	        "table_id": "tab_task_accuracy",
641	        "caption": "Task-level accuracy: baseline vs TPAB+LoRA on 6 task types (depth 15)",
642	        "columns": [
643	          "Task",
644	          "Baseline_Acc",
645	          "TPAB_Acc",
646	          "Δ_pct",
647	          "GAR_Δpp"
648	        ],
649	        "rows": [
650	          [
651	            "Instruction recall",
652	            71.2,
653	            75.8,
654	            4.6,
655	            8.1
656	          ],
657	          [
658	            "Entity extraction",
659	            64.8,
660	            68.3,
661	            3.5,
662	            7.2
663	          ],
664	          [
665	            "Multi-step reasoning",
666	            58.3,
667	            61.7,
668	            3.4,
669	            6.8
670	          ],
671	          [
672	            "Preference consistency",
673	            67.5,
674	            71.2,
675	            3.7,
676	            7.0
677	          ],
678	          [
679	            "Constraint following",
680	            69.1,
681	            73.5,
682	            4.4,
683	            7.5
684	          ],
685	          [
686	            "Context grounding",
687	            62.4,
688	            65.0,
689	            2.6,
690	            5.9
691	          ],
692	          [
693	            "**Mean**",
694	            65.6,
695	            69.3,
696	            3.7,
697	            7.1
698	          ]
699	        ]
700	      }
701	    ],
702	    "figures": [],
703	    "analysis": "The GAR→task accuracy translation is the most critical result for the paper's practical impact claim. The 3.8% mean improvement and r=0.84 correlation demonstrate that TPAB's attention-level intervention has meaningful downstream benefit. The per-task breakdown shows TPAB helps most for goal-dependent tasks (recall, constraints) and least for integration tasks (context grounding), which aligns with the mechanism: TPAB boosts goal-token attention, not distributed context integration.\n\n\nGAR improvement translates to task accuracy because goal accessibility is a necessary (though not sufficient) condition for correct task completion in multi-turn settings. When the model can better attend to goal tokens (system prompt, initial instructions, constraints), it is more likely to (a) recall the original instruction, (b) extract entities mentioned in early turns, (c) maintain preference consistency, and (d) follow constraints set at conversation start. The translation is not 1:1: GAR improvement of 7.22pp at d15 yields only 3.7% task accuracy improvement because task accuracy also depends on reasoning capability, generation quality, and instruction understanding, which are not directly addressed by attention bias. The correlation (r=0.84) is strong but imperfect, confirming that GAR is a meaningful but not complete predictor. Instruction recall and constraint following show the largest gains (+4.6% and +4.4%) because these tasks most directly depend on attending to goal tokens. Context grounding shows the smallest gain (+2.6%) because it requires integrating information from multiple turns, not just attending to the goal turn. Depth-25 improvement is larger than depth-15 (+4.3% vs +3.7%) because the baseline is lower and TPAB's benefit is proportionally greater. The aggregate 3.8% improvement is within the best-tier range [2.5, 5.0] and addresses reviewer concern C1 directly.\n"
704	  },
705	  {
706	    "name": "MMLU single-turn preservation check",
707	    "description": "Run MMLU 5-shot evaluation on TPAB+LoRA model to verify no single-turn capability regression. Compare with Qwen3-8B base and LoRA-only.\n",
708	    "results": {
709	      "mmlu_baseline": 72.1,
710	      "mmlu_lora_only": 71.7,
711	      "mmlu_tpab_lora": 71.8,
712	      "mmlu_tpab_only": 72.0,
713	      "mmlu_regression_lora_only_pct": 0.4,
714	      "mmlu_regression_tpab_lora_pct": 0.3,
715	      "mmlu_regression_tpab_only_pct": 0.1,
716	      "mmlu_stem_baseline": 68.4,
717	      "mmlu_stem_tpab_lora": 68.2,
718	      "mmlu_humanities_baseline": 74.3,
719	      "mmlu_humanities_tpab_lora": 74.0,
720	      "mmlu_social_sciences_baseline": 76.8,
721	      "mmlu_social_sciences_tpab_lora": 76.5,
722	      "mmlu_other_baseline": 69.1,
723	      "mmlu_other_tpab_lora": 68.9
724	    },
725	    "tables": [
726	      {
727	        "table_id": "tab_mmlu_preservation",
728	        "caption": "MMLU 5-shot accuracy: single-turn preservation",
729	        "columns": [
730	          "Method",
731	          "MMLU_Overall",
732	          "STEM",
733	          "Humanities",
734	          "Social_Sci",
735	          "Other",
736	          "Δ_from_base"
737	        ],
738	        "rows": [
739	          [
740	            "Qwen3-8B base",
741	            72.1,
742	            68.4,
743	            74.3,
744	            76.8,
745	            69.1,
746	            "—"
747	          ],
748	          [
749	            "TPAB-only",
750	            72.0,
751	            68.3,
752	            74.2,
753	            76.7,
754	            69.0,
755	            -0.1
756	          ],
757	          [
758	            "LoRA-only",
759	            71.7,
760	            68.0,
761	            73.9,
762	            76.5,
763	            68.7,
764	            -0.4
765	          ],
766	          [
767	            "TPAB+LoRA",
768	            71.8,
769	            68.2,
770	            74.0,
771	            76.5,
772	            68.9,
773	            -0.3
774	          ]
775	        ]
776	      }
777	    ],
778	    "figures": [],
779	    "analysis": "MMLU regression of 0.3pp is negligible and within evaluation noise. The decomposition is informative: TPAB-only has near-zero regression (0.1pp), confirming that turn-position bias is architecturally neutral for single-turn tasks. All regression comes from LoRA. This addresses A5 and provides a strong safety argument for TPAB deployment.\n\n\nTPAB adds turn-position-indexed bias to attention logits. For single-turn MMLU evaluation where there is only one \"turn\" (the question), the TPAB bias reduces to a constant offset applied to all tokens in the single turn. A constant additive bias before softmax cancels out in the softmax normalization (softmax(x + c) = softmax(x)), so TPAB has essentially zero effect on single-turn inference. The observed 0.3pp regression comes entirely from the LoRA component, which slightly modifies Q/K/V projections. TPAB-only shows only 0.1pp regression (within noise), confirming the theoretical prediction. This is a key selling point: TPAB is a free lunch for single-turn performance. The 0.3pp total regression is well within the best-tier range [0.0, 0.5] and within standard MMLU evaluation variance (~0.2-0.4pp across random seeds).\n"
780	  },
781	  {
782	    "name": "TPAB on Llama-3-8B",
783	    "description": "Train TPAB+LoRA on Llama-3-8B using same 5K synthetic data to verify cross-model TPAB generalization. Depends on dual-mechanism confirmation on Llama-3 (analysis_cross_model_llama) and TPAB validation on Qwen3 (tpab_mvp).\n",
784	    "results": {
785	      "llama_extraction_gar_d15_baseline": 0.0328,
786	      "llama_extraction_gar_d15_tpab_lora": 0.0941,
787	      "llama_extraction_gar_d25_baseline": 0.0231,
788	      "llama_extraction_gar_d25_tpab_lora": 0.0892,
789	      "llama_gar_improvement_d15_pp": 6.13,
790	      "llama_gar_improvement_d25_pp": 6.61,
791	      "llama_shallow_layer_gar_lift_pp": 5.28,
792	      "llama_hf_baseline_gar": 0.0421,
793	      "llama_hf_tpab_lora_gar": 0.0873,
794	      "llama_hf_improvement_pp": 4.52,
795	      "llama_task_accuracy_improvement_pct": 3.1,
796	      "llama_mmlu_baseline": 66.5,
797	      "llama_mmlu_tpab_lora": 66.2,
798	      "llama_mmlu_regression_pct": 0.3,
799	      "llama_tpab_params": "33.8K",
800	      "llama_trainable_lora_params": "26.4M",
801	      "llama_training_hours": 2.3,
802	      "cross_model_tpab_benefit_replication": 2
803	    },
804	    "tables": [
805	      {
806	        "table_id": "tab_cross_model_tpab",
807	        "caption": "TPAB+LoRA cross-model results",
808	        "columns": [
809	          "Model",
810	          "d15_Baseline",
811	          "d15_TPAB",
812	          "d15_Δpp",
813	          "d25_Δpp",
814	          "HF_Δpp",
815	          "Task_Δ_pct",
816	          "MMLU_Reg"
817	        ],
818	        "rows": [
819	          [
820	            "Qwen3-8B",
821	            0.0353,
822	            0.1075,
823	            7.22,
824	            8.5,
825	            5.2,
826	            3.8,
827	            -0.3
828	          ],
829	          [
830	            "Llama-3-8B",
831	            0.0328,
832	            0.0941,
833	            6.13,
834	            6.61,
835	            4.52,
836	            3.1,
837	            -0.3
838	          ]
839	        ]
840	      }
841	    ],
842	    "figures": [],
843	    "analysis": "Cross-model replication is strong. The Llama-3 result is not merely positive but structurally consistent: same shallow-layer concentration of TPAB benefit, same negligible MMLU regression, same GAR-to-task translation. The slightly smaller improvement on Llama-3 is explainable by GQA constraints and is not a concern. With 2/2 models showing benefit, the generalization claim is well-supported. The learned bias heatmaps showing similar structure across architectures are a compelling visual for the paper.\n\nTPAB generalizes to Llama-3-8B because the underlying mechanism (softmax dilution at shallow layers) is architecture-universal. Llama-3's GQA (grouped-query attention) means fewer unique K/V heads, so the TPAB bias has slightly fewer parameters (33.8K vs 35.3K) but the per-head bias is applied to each query head in the group. The improvement (6.13pp at d15) is slightly smaller than Qwen3 (7.22pp) for two reasons: (1) Llama-3's lower baseline GAR (0.0328 vs 0.0353) means more severe dilution that is harder to fully compensate, and (2) Llama-3's GQA shares K/V projections across query heads, limiting the bias's ability to provide head-specific corrections. The HF improvement (4.52pp) and task accuracy improvement (3.1%) confirm that TPAB's benefit is not Qwen-specific. MMLU regression (0.3pp) matches the Qwen3 result, consistent with the theoretical prediction that TPAB is single-turn-neutral. With both Qwen3 and Llama-3 showing TPAB benefit, cross_model_tpab_benefit_replication = 2, satisfying the best-tier requirement and addressing C2 fully.\n"
844	  }
845	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dad8eea4-6bcd-4f4b-a5d4-9c2bff663e14",
  "isSidechain": true,
  "promptId": "8fe5e53a-b377-47d8-9f45-301a1c07cb3d",
  "agentId": "a6477368b1ca31b25",
  "type": "user",
  "uuid": "178f8bde-7101-4dff-a927-2b8a8ae9d571",
  "sourceToolAssistantUUID": "dad8eea4-6bcd-4f4b-a5d4-9c2bff663e14",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation",
  "sessionId": "421f26de-efdb-4f11-8ecd-7c2ad90d7f9f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-18T10:53:33.873Z_

Now let me check the review context file that was already generated.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "178f8bde-7101-4dff-a927-2b8a8ae9d571",
  "isSidechain": true,
  "agentId": "a6477368b1ca31b25",
  "requestId": "req_011Cb9uhy5dJexEyjviUUULs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "27104b5a-f026-4ea8-a5d0-c62fcb6e7223",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation",
  "sessionId": "421f26de-efdb-4f11-8ecd-7c2ad90d7f9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ViZZ4QoaCdEU7Ve9pFvmRZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 32218,
      "cache_read_input_tokens": 46569,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 32218,
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

_source line 39 · 2026-05-18T10:53:35.918Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TexoWGgZQeNG3pXWrvFUDn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation/artifacts/dream_reports/dream_20260518T101930/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27104b5a-f026-4ea8-a5d0-c62fcb6e7223",
  "isSidechain": true,
  "agentId": "a6477368b1ca31b25",
  "requestId": "req_011Cb9uhy5dJexEyjviUUULs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f20dcb3a-f187-41ea-b481-b2cd880e4404",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation",
  "sessionId": "421f26de-efdb-4f11-8ecd-7c2ad90d7f9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ViZZ4QoaCdEU7Ve9pFvmRZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 32218,
      "cache_read_input_tokens": 46569,
      "output_tokens": 116,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 32218
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 116,
          "cache_read_input_tokens": 46569,
          "cache_creation_input_tokens": 32218,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 32218,
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

_source line 40 · 2026-05-18T10:53:36.193Z_

<details><summary>↩ Tool result · `toolu_01TexoWGgZQeNG3pXWrvFUDn`</summary>

```text
1	narrative_guidance: 'Full four-claim story stands. TPAB mechanism hypothesis fully
2	  validated: learnable turn-position bias effectively counteracts shallow-layer softmax
3	  dilution, GAR gains causally translate to task performance, and dual-mechanism analysis
4	  generalizes across Qwen3-8B / Llama-3-8B / Mistral-7B. TB-RoPE negative result strengthens
5	  causal argument by ruling out position-encoding geometry as bottleneck. TPAB outperforms
6	  all mechanism-agnostic baselines on both GAR and task metrics with negligible MMLU
7	  regression. Paper title keeps ''mechanism-aware fix''; dual-mechanism stratification
8	  is novel contribution. Strong NAACL main conference paper with analysis depth +
9	  practical method + negative result as evidence.
10	
11	  '
12	imagined_experiments:
13	- name: Dual-mechanism analysis on Llama-3-8B
14	  plan_id: analysis_cross_model_llama
15	  description: 'Replicate per-layer GAR + QKA correlation analysis on Llama-3-8B (32
16	    layers, GQA, RoPE). Run extraction and reasoning tasks at depths 5/15/25 on synthetic
17	    data. Compute per-layer Pearson ρ(QKA, GAR) to verify shallow softmax-competition
18	    vs deep Q-K misalignment stratification.
19	
20	    '
21	  expected_results:
22	    extraction_gar_d5: 0.0465
23	    extraction_gar_d15: 0.0328
24	    extraction_gar_d25: 0.0231
25	    extraction_gar_decline_pct: 50.3
26	    reasoning_gar_d5: 0.0351
27	    reasoning_gar_d15: 0.0162
28	    reasoning_gar_d25: 0.0148
29	    reasoning_gar_decline_pct: 57.8
30	    shallow_qka_gar_rho_mean_L0_L5: 0.26
31	    deep_qka_gar_rho_mean_L10_plus: 0.85
32	    extraction_max_layer_rho: 0.88
33	    extraction_max_layer_rho_layer: L12_d25
34	    reasoning_max_layer_rho: 0.9
35	    reasoning_max_layer_rho_layer: L16_d5
36	    layers_with_rho_gt_0.8:
37	    - L12
38	    - L16
39	    - L22
40	    - L26
41	    - L28
42	    - L29
43	    - L30
44	    - L31
45	    dual_mechanism_confirmed: true
46	  result_rationale: 'Llama-3-8B uses the same RoPE-based dense attention architecture
47	    as Qwen3-8B, so the softmax competition mechanism at shallow layers is architecturally
48	    inevitable: as token count grows with conversation depth, the denominator of softmax
49	    over all keys increases, diluting per-token attention mass regardless of Q-K alignment.
50	    This is a mathematical property of softmax normalization, not model-specific.
51	    Shallow layers in Llama-3 have similarly broad, unfocused attention patterns (known
52	    from prior interpretability work), so QKA-GAR ρ remains low (~0.26). Deep layers
53	    develop specialized heads with high Q-K selectivity, so geometric misalignment
54	    with positional distance drives GAR decline there (ρ~0.85-0.90). The absolute
55	    GAR values are slightly lower than Qwen3-8B because Llama-3-8B''s tokenizer produces
56	    ~5-8% more tokens per conversation turn on average, amplifying softmax dilution.
57	    The layer indices for high-ρ layers shift slightly (L12/L16 vs Qwen''s L10/L14)
58	    reflecting Llama-3''s different layer specialization pattern, but the shallow/deep
59	    stratification boundary remains at approximately L6-L8.
60	
61	    '
62	  tables:
63	  - table_id: tab_cross_model_analysis
64	    caption: Per-layer QKA-GAR Pearson ρ across three model families
65	    columns:
66	    - Model
67	    - Layer_Group
68	    - Mean_ρ
69	    - GAR_Decline_pct
70	    - Mechanism
71	    rows:
72	    - - Qwen3-8B
73	      - L0-L5 (shallow)
74	      - 0.27
75	      - 48.5
76	      - softmax competition
77	    - - Qwen3-8B
78	      - L10+ (deep)
79	      - 0.87
80	      - 48.5
81	      - Q-K misalignment
82	    - - Llama-3-8B
83	      - L0-L5 (shallow)
84	      - 0.26
85	      - 50.3
86	      - softmax competition
87	    - - Llama-3-8B
88	      - L10+ (deep)
89	      - 0.85
90	      - 50.3
91	      - Q-K misalignment
92	  figures_description:
93	  - 'Heatmap: per-layer ρ(QKA, GAR) for Llama-3-8B across depths 5/15/25, mirroring
94	    Qwen3-8B figure. Clear blue (low ρ) band at L0-L5, warm (high ρ) band at L10+.'
95	  analysis: 'Dual-mechanism pattern replicates on Llama-3-8B with quantitatively similar
96	    characteristics: shallow ρ=0.26 vs Qwen''s 0.27, deep ρ=0.85 vs Qwen''s 0.87.
97	    The stratification boundary is consistent (L6-L8). This confirms the mechanism
98	    is not Qwen-specific but an architectural property of RoPE-based transformers
99	    with softmax attention. Minor differences in absolute GAR levels reflect tokenizer
100	    and training distribution differences, not mechanistic divergence.
101	
102	    '
103	- name: Dual-mechanism analysis on Mistral-7B
104	  plan_id: analysis_cross_model_mistral
105	  description: 'Replicate per-layer GAR + QKA analysis on Mistral-7B-v0.3 (32 layers,
106	    GQA, sliding window attention at some layers, RoPE). Same protocol as Qwen3 and
107	    Llama-3 analysis.
108	
109	    '
110	  expected_results:
111	    extraction_gar_d5: 0.0512
112	    extraction_gar_d15: 0.0346
113	    extraction_gar_d25: 0.0248
114	    extraction_gar_decline_pct: 51.6
115	    reasoning_gar_d5: 0.0389
116	    reasoning_gar_d15: 0.0185
117	    reasoning_gar_d25: 0.0159
118	    reasoning_gar_decline_pct: 59.1
119	    shallow_qka_gar_rho_mean_L0_L5: 0.28
120	    deep_qka_gar_rho_mean_L10_plus: 0.83
121	    extraction_max_layer_rho: 0.87
122	    extraction_max_layer_rho_layer: L14_d25
123	    reasoning_max_layer_rho: 0.89
124	    reasoning_max_layer_rho_layer: L18_d5
125	    layers_with_rho_gt_0.8:
126	    - L14
127	    - L18
128	    - L24
129	    - L26
130	    - L28
131	    - L29
132	    - L30
133	    - L31
134	    dual_mechanism_confirmed: true
135	    sliding_window_layer_note: SWA layers (L0-L7 in v0.3) show slightly elevated shallow
136	      ρ (~0.31) due to reduced key set, but still well below deep-layer levels
137	  result_rationale: 'Mistral-7B''s sliding window attention (SWA) at early layers
138	    restricts the key set to a local window, partially mitigating softmax dilution.
139	    This explains the marginally higher shallow ρ (~0.28 vs Qwen''s 0.27) since fewer
140	    keys compete. However, goal tokens from early turns still fall outside the sliding
141	    window at depth 15+, so GAR decline remains severe (51.6%). The dual-mechanism
142	    pattern holds because SWA only changes the magnitude of softmax competition, not
143	    its existence: within the window, dilution still occurs, and outside the window,
144	    goal tokens are simply invisible. Deep layers in Mistral-7B use full attention
145	    and show the same Q-K geometric misalignment as the other models. Slightly higher
146	    absolute GAR at d5 (0.0512) reflects Mistral''s training distribution having more
147	    instruction-following emphasis. The 3-model replication with quantitatively consistent
148	    stratification boundaries constitutes strong evidence for the universality of
149	    the dual-mechanism claim.
150	
151	    '
152	  tables:
153	  - table_id: tab_cross_model_analysis_full
154	    caption: Dual-mechanism replication across three model families (extraction task)
155	    columns:
156	    - Model
157	    - Params
158	    - Arch_Note
159	    - Shallow_ρ
160	    - Deep_ρ
161	    - GAR_d5
162	    - GAR_d25
163	    - Decline_pct
164	    rows:
165	    - - Qwen3-8B
166	      - 8.2B
167	      - Dense RoPE
168	      - 0.27
169	      - 0.87
170	      - 0.0499
171	      - 0.0257
172	      - 48.5
173	    - - Llama-3-8B
174	      - 8.0B
175	      - GQA RoPE
176	      - 0.26
177	      - 0.85
178	      - 0.0465
179	      - 0.0231
180	      - 50.3
181	    - - Mistral-7B
182	      - 7.2B
183	      - GQA+SWA RoPE
184	      - 0.28
185	      - 0.83
186	      - 0.0512
187	      - 0.0248
188	      - 51.6
189	  figures_description:
190	  - '3-panel heatmap (Qwen / Llama / Mistral): per-layer ρ(QKA, GAR) showing consistent
191	    shallow-cold / deep-warm stratification across all three architectures.'
192	  - 'Bar chart: shallow-ρ vs deep-ρ grouped by model, visually demonstrating the mechanism
193	    gap is architecturally robust.'
194	  analysis: 'All three models show shallow ρ in [0.26, 0.28] and deep ρ in [0.83,
195	    0.87]. Mistral''s SWA does not eliminate the dual-mechanism pattern, only modestly
196	    attenuates shallow-layer dilution. GAR decline ranges 48-59% across models. This
197	    3-model replication satisfies reviewer concern C2 and establishes Claim 1 as architecture-general.
198	    Notably, the stratification boundary is consistent at L6-L8 across all models
199	    despite different training recipes.
200	
201	    '
202	- name: TPAB concept validation on Qwen3-8B
203	  plan_id: tpab_mvp
204	  description: 'Train TPAB (learnable per-layer, per-head, per-turn-position bias
205	    added to attention logits before softmax) + LoRA rank 32 on Qwen3-8B using 5K
206	    synthetic multi-turn data. TPAB adds ~35K parameters. Evaluate on synthetic GAR
207	    benchmark (depths 5/15/25) and HF real conversation benchmark (627 samples).
208	
209	    '
210	  expected_results:
211	    synthetic_extraction_gar_d5_baseline: 0.0499
212	    synthetic_extraction_gar_d5_tpab_lora: 0.0521
213	    synthetic_extraction_gar_d15_baseline: 0.0353
214	    synthetic_extraction_gar_d15_tpab_lora: 0.1075
215	    synthetic_extraction_gar_d25_baseline: 0.0257
216	    synthetic_extraction_gar_d25_tpab_lora: 0.1107
217	    synthetic_reasoning_gar_d5_baseline: 0.0374
218	    synthetic_reasoning_gar_d5_tpab_lora: 0.0398
219	    synthetic_reasoning_gar_d15_baseline: 0.0174
220	    synthetic_reasoning_gar_d15_tpab_lora: 0.0824
221	    synthetic_reasoning_gar_d25_baseline: 0.0163
222	    synthetic_reasoning_gar_d25_tpab_lora: 0.0943
223	    tpab_gar_improvement_d15_pp: 7.22
224	    tpab_gar_improvement_d25_pp: 8.5
225	    tpab_shallow_layer_gar_lift_pp: 6.1
226	    hf_baseline_gar: 0.0454
227	    hf_tpab_lora_gar: 0.0974
228	    hf_real_conv_gar_improvement_pp: 5.2
229	    hf_samples_evaluated: 417
230	    train_loss_initial: 0.45
231	    train_loss_final: 0.17
232	    epochs: 3
233	    trainable_params_lora: 30.67M (0.37%)
234	    trainable_params_tpab: 35.3K (0.0004%)
235	    wall_clock_hours: 2.1
236	    pass_gar_improvement_5pp: true
237	  result_rationale: 'TPAB directly addresses the identified bottleneck: softmax dilution
238	    at shallow layers. By adding a learnable positive bias to attention logits for
239	    goal-turn positions before softmax normalization, TPAB effectively increases the
240	    pre-softmax score of goal tokens, counteracting the dilution from growing key
241	    sets. At depth 15, the key set is ~3x larger than depth 5, causing ~3x dilution
242	    in softmax mass for goal tokens. A learned bias of ~0.8-1.2 in logit space at
243	    shallow layers compensates for this dilution, restoring GAR from 3.53% to ~10.75%
244	    (a 7.22pp lift). The improvement is larger at depth 25 (8.50pp) because the dilution
245	    is more severe there, and TPAB''s bias scales with turn-position distance by design.
246	    Shallow-layer GAR lift (6.1pp) is substantial because TPAB was specifically designed
247	    for the softmax-competition mechanism dominant at L0-L5. Depth-5 improvement is
248	    minimal (+0.22pp for extraction) because softmax dilution is not yet severe at
249	    short context. The HF real conversation improvement (5.20pp) is smaller than synthetic
250	    (7.22pp at d15) because real conversations have variable turn lengths, more diverse
251	    goal formulations, and mixed depths, diluting the average effect. Training converges
252	    well because TPAB''s 35K parameters are highly targeted and the gradient signal
253	    from next-token loss propagates cleanly through the bias → softmax → attention
254	    path.
255	
256	    '
257	  tables:
258	  - table_id: tab_tpab_mvp_gar
259	    caption: TPAB+LoRA GAR improvement on Qwen3-8B (synthetic benchmark)
260	    columns:
261	    - Task
262	    - Depth
263	    - Baseline_GAR
264	    - TPAB+LoRA_GAR
265	    - Δ_pp
266	    rows:
267	    - - Extraction
268	      - 5
269	      - 0.0499
270	      - 0.0521
271	      - 0.22
272	    - - Extraction
273	      - 15
274	      - 0.0353
275	      - 0.1075
276	      - 7.22
277	    - - Extraction
278	      - 25
279	      - 0.0257
280	      - 0.1107
281	      - 8.5
282	    - - Reasoning
283	      - 5
284	      - 0.0374
285	      - 0.0398
286	      - 0.24
287	    - - Reasoning
288	      - 15
289	      - 0.0174
290	      - 0.0824
291	      - 6.5
292	    - - Reasoning
293	      - 25
294	      - 0.0163
295	      - 0.0943
296	      - 7.8
297	  figures_description:
298	  - 'Line plot: GAR vs conversation depth (5/10/15/20/25) for baseline vs TPAB+LoRA.
299	    Baseline drops steeply; TPAB+LoRA remains elevated, with the gap widening at deeper
300	    turns.'
301	  - 'Per-layer GAR heatmap: TPAB+LoRA vs baseline side-by-side. Shallow layers (L0-L5)
302	    show dramatic warming (higher GAR) with TPAB while deep layers show moderate improvement
303	    from LoRA.'
304	  analysis: 'TPAB+LoRA achieves 7.22pp GAR improvement at d15 and 8.50pp at d25, both
305	    within the best-tier target range. The per-layer decomposition shows TPAB contributes
306	    primarily at shallow layers (6.1pp lift at L0-L5) while LoRA provides complementary
307	    benefit at deep layers through improved Q-K alignment. The mechanism-aware design
308	    is validated: TPAB targets the right bottleneck. The HF real-conversation improvement
309	    (5.20pp) confirms generalization beyond synthetic distributions.
310	
311	    '
312	- name: TPAB training on real multi-turn data
313	  plan_id: tpab_real_data
314	  description: 'Train TPAB+LoRA on mixed real multi-turn data: 3K ShareGPT conversations
315	    (filtered for 10+ turns) + 2K WildChat conversations. Evaluate on both synthetic
316	    benchmark and HF real conversation benchmark. Compare with synthetic-data-trained
317	    TPAB from tpab_mvp.
318	
319	    '
320	  expected_results:
321	    synthetic_extraction_gar_d15_real_trained: 0.1038
322	    synthetic_extraction_gar_d25_real_trained: 0.1052
323	    synthetic_reasoning_gar_d15_real_trained: 0.0796
324	    synthetic_reasoning_gar_d25_real_trained: 0.0911
325	    hf_tpab_lora_real_trained_gar: 0.1086
326	    hf_real_conv_gar_improvement_pp_real_trained: 6.32
327	    hf_synthetic_trained_gar: 0.0974
328	    hf_real_trained_vs_synthetic_trained_pp: 1.12
329	    synthetic_bench_real_trained_vs_synthetic_trained_d15_pp: -0.37
330	    train_loss_final: 0.19
331	    epochs: 3
332	    wall_clock_hours: 3.8
333	  result_rationale: 'Real-data-trained TPAB outperforms synthetic-trained on HF real
334	    conversations (+1.12pp) because the training distribution is closer to the evaluation
335	    distribution: real conversations have natural turn-length variance, topic drift,
336	    and conversational patterns that synthetic data only approximates. The bias parameters
337	    learn more robust turn-position adjustments when exposed to genuine multi-turn
338	    dynamics. Conversely, on the synthetic benchmark the real-trained model is slightly
339	    worse (-0.37pp at d15) because the synthetic benchmark''s rigid structure favors
340	    the synthetic-trained model. The HF improvement of 6.32pp (vs 5.20pp synthetic-trained)
341	    is within the best-tier range [3.0, 7.0] and represents the more externally valid
342	    result. Training takes longer (3.8h vs 2.1h) due to more variable sequence lengths
343	    requiring more padding/bucketing.
344	
345	    '
346	  tables:
347	  - table_id: tab_real_vs_synthetic_training
348	    caption: 'Training data ablation: synthetic vs real multi-turn data for TPAB+LoRA'
349	    columns:
350	    - Training_Data
351	    - Synth_d15_GAR
352	    - Synth_d25_GAR
353	    - HF_GAR
354	    - HF_Δ_pp
355	    rows:
356	    - - Synthetic 5K
357	      - 0.1075
358	      - 0.1107
359	      - 0.0974
360	      - 5.2
361	    - - Real 5K (ShareGPT+WildChat)
362	      - 0.1038
363	      - 0.1052
364	      - 0.1086
365	      - 6.32
366	    - - Baseline (no training)
367	      - 0.0353
368	      - 0.0257
369	      - 0.0454
370	      - —
371	  figures_description:
372	  - 'Grouped bar chart: HF real-conversation GAR for baseline / synthetic-trained
373	    / real-trained, showing progressive improvement.'
374	  analysis: 'Real-data training provides meaningful lift on real conversations (+1.12pp
375	    over synthetic-trained), confirming that TPAB benefits transfer across training
376	    distributions. The synthetic benchmark result (-0.37pp) is expected distribution
377	    mismatch, not degradation. For the paper, we report real-trained HF numbers as
378	    the primary result and note that even synthetic training achieves strong gains,
379	    lowering the barrier to TPAB adoption.
380	
381	    '
382	- name: 'TPAB ablation: TPAB-only vs TPAB+LoRA vs LoRA-only'
383	  plan_id: tpab_ablation_components
384	  description: 'Three-way ablation on Qwen3-8B to isolate TPAB''s contribution: (1)
385	    TPAB-only (freeze all model weights, only train 35K bias params), (2) TPAB+LoRA
386	    (joint training, the full method), (3) LoRA-only (rank 32, no bias, same training
387	    data and schedule). All evaluated on synthetic GAR and HF benchmarks.
388	
389	    '
390	  expected_results:
391	    tpab_only_extraction_gar_d15: 0.0734
392	    tpab_only_extraction_gar_d25: 0.0712
393	    tpab_only_hf_gar: 0.0803
394	    tpab_only_gar_improvement_d15_pp: 3.81
395	    tpab_only_gar_improvement_d25_pp: 4.55
396	    tpab_only_hf_improvement_pp: 3.49
397	    tpab_only_trainable_params: 35.3K
398	    tpab_lora_extraction_gar_d15: 0.1075
399	    tpab_lora_extraction_gar_d25: 0.1107
400	    tpab_lora_hf_gar: 0.0974
401	    tpab_lora_gar_improvement_d15_pp: 7.22
402	    lora_only_extraction_gar_d15: 0.0711
403	    lora_only_extraction_gar_d25: 0.0654
404	    lora_only_hf_gar: 0.0768
405	    lora_only_gar_improvement_d15_pp: 3.58
406	    lora_only_gar_improvement_d25_pp: 3.97
407	    lora_only_hf_improvement_pp: 3.14
408	    tpab_vs_lora_only_gar_margin_d15_pp: 3.64
409	    tpab_vs_lora_only_gar_margin_d25_pp: 4.53
410	    tpab_vs_lora_only_hf_margin_pp: 2.06
411	    tpab_only_shallow_layer_lift_pp: 4.82
412	    lora_only_shallow_layer_lift_pp: 1.23
413	    tpab_only_deep_layer_lift_pp: 0.91
414	    lora_only_deep_layer_lift_pp: 2.87
415	  result_rationale: 'TPAB-only (35K params) achieves 3.81pp improvement at d15 using
416	    only attention logit bias, confirming that softmax dilution is directly addressable
417	    by additive bias. The effect is concentrated at shallow layers (4.82pp lift at
418	    L0-L5) with minimal deep-layer benefit (0.91pp), matching the mechanism analysis.
419	    LoRA-only achieves comparable aggregate improvement (3.58pp at d15) but through
420	    a fundamentally different mechanism: LoRA modifies Q/K/V projections, primarily
421	    improving deep-layer Q-K alignment (2.87pp deep lift) with weak shallow-layer
422	    effect (1.23pp). TPAB+LoRA combines both mechanisms for 7.22pp total, nearly additive
423	    (3.81 + 3.58 ≈ 7.39, actual 7.22 showing slight diminishing returns). The 3.64pp
424	    margin of TPAB+LoRA over LoRA-only at d15 falls squarely in the best-tier range
425	    [2.0, 5.0]. This decomposition is the strongest evidence that TPAB addresses a
426	    mechanism orthogonal to what LoRA captures. On HF real conversations, the margin
427	    narrows (2.06pp) because real conversations have more depth variability, and LoRA''s
428	    deep-layer benefit matters more for genuinely long conversations.
429	
430	    '
431	  tables:
432	  - table_id: tab_component_ablation
433	    caption: 'Component ablation: isolating TPAB and LoRA contributions'
434	    columns:
435	    - Method
436	    - Params
437	    - Synth_d15_Δpp
438	    - Synth_d25_Δpp
439	    - HF_Δpp
440	    - Shallow_Lift_pp
441	    - Deep_Lift_pp
442	    rows:
443	    - - Baseline
444	      - —
445	      - —
446	      - —
447	      - —
448	      - —
449	      - —
450	    - - TPAB-only
451	      - 35.3K
452	      - 3.81
453	      - 4.55
454	      - 3.49
455	      - 4.82
456	      - 0.91
457	    - - LoRA-only
458	      - 30.67M
459	      - 3.58
460	      - 3.97
461	      - 3.14
462	      - 1.23
463	      - 2.87
464	    - - TPAB+LoRA
465	      - 30.70M
466	      - 7.22
467	      - 8.5
468	      - 5.2
469	      - 6.1
470	      - 3.41
471	  figures_description:
472	  - 'Stacked bar chart: per-layer-group GAR improvement decomposed into shallow (L0-5)
473	    and deep (L10+) contributions for each method. TPAB-only dominates shallow; LoRA-only
474	    dominates deep; TPAB+LoRA combines both.'
475	  - 'Scatter plot: TPAB bias magnitude (learned) vs layer index, showing high bias
476	    at shallow layers tapering off at deep layers, confirming mechanism-aware parameter
477	    allocation.'
478	  analysis: 'The near-additive decomposition (TPAB shallow + LoRA deep ≈ TPAB+LoRA
479	    total) is the key insight for the paper. It demonstrates that TPAB and LoRA target
480	    orthogonal mechanisms, validating the dual-mechanism analysis. The 35K-param TPAB-only
481	    achieving 3.81pp at d15 (vs LoRA-only''s 3.58pp with 30.67M params) is a striking
482	    efficiency result: TPAB achieves comparable GAR improvement with 870x fewer parameters,
483	    because it targets the bottleneck directly.
484	
485	    '
486	- name: 'Bias design ablation: learned vs fixed vs ALiBi-style vs uniform'
487	  plan_id: tpab_ablation_bias_design
488	  description: 'Compare four bias designs applied at the same attention logit injection
489	    point: (1) TPAB learned (per-layer, per-head, per-turn-position), (2) Fixed linear
490	    decay (bias ∝ 1/(turn_distance+1)), (3) ALiBi-style (fixed linear bias by token
491	    position, adapted to turn granularity), (4) Uniform positive bias (+constant for
492	    all goal-turn tokens). All combined with LoRA rank 32.
493	
494	    '
495	  expected_results:
496	    tpab_learned_d15_pp: 7.22
497	    tpab_learned_d25_pp: 8.5
498	    tpab_learned_hf_pp: 5.2
499	    fixed_linear_d15_pp: 4.63
500	    fixed_linear_d25_pp: 5.18
501	    fixed_linear_hf_pp: 3.47
502	    alibi_style_d15_pp: 3.89
503	    alibi_style_d25_pp: 4.11
504	    alibi_style_hf_pp: 2.91
505	    uniform_bias_d15_pp: 4.21
506	    uniform_bias_d25_pp: 4.67
507	    uniform_bias_hf_pp: 3.12
508	    learned_bias_mean_shallow: 0.94
509	    learned_bias_mean_deep: 0.31
510	    learned_bias_std_across_heads: 0.28
511	    learned_bias_turn_position_correlation: 0.72
512	  result_rationale: 'Learned TPAB outperforms all fixed alternatives because the optimal
513	    bias magnitude varies by layer, head, and turn position in ways that a fixed schedule
514	    cannot capture. Shallow layers need larger biases (~0.94 mean) to overcome severe
515	    softmax dilution, while deep layers need smaller biases (~0.31 mean) to avoid
516	    overriding the informative Q-K alignment signals. Different attention heads specialize
517	    in different aspects (some are "position heads", some are "content heads"), requiring
518	    per-head bias adaptation (std=0.28 across heads). Fixed linear decay performs
519	    decently (4.63pp) because it captures the monotonic relationship between turn
520	    distance and dilution severity, but cannot adapt per-layer. ALiBi-style bias performs
521	    worst among structured alternatives (3.89pp) because ALiBi was designed for token-level
522	    recency bias, not turn-level goal accessibility; it penalizes distant tokens uniformly,
523	    including non-goal tokens, providing no selective boost to goal turns. This directly
524	    addresses reviewer concern C3 ("TPAB is just ALiBi with different indexing"):
525	    the 3.33pp gap between TPAB and ALiBi-style demonstrates that turn-position indexing
526	    with per-layer learning is fundamentally different from token-distance linear
527	    bias. Uniform bias (4.21pp) outperforms ALiBi-style because it at least boosts
528	    all goal-turn tokens equally without the counterproductive distance penalty, but
529	    cannot adapt to layer-specific needs.
530	
531	    '
532	  tables:
533	  - table_id: tab_bias_design_ablation
534	    caption: Bias design comparison (all with LoRA rank 32 on Qwen3-8B)
535	    columns:
536	    - Bias_Design
537	    - Learnable
538	    - Params
539	    - Synth_d15_Δpp
540	    - Synth_d25_Δpp
541	    - HF_Δpp
542	    rows:
543	    - - TPAB (learned)
544	      - 'Yes'
545	      - 35.3K
546	      - 7.22
547	      - 8.5
548	      - 5.2
549	    - - Fixed linear decay
550	      - 'No'
551	      - 0
552	      - 4.63
553	      - 5.18
554	      - 3.47
555	    - - ALiBi-style (turn)
556	      - 'No'
557	      - 0
558	      - 3.89
559	      - 4.11
560	      - 2.91
561	    - - Uniform (+const)
562	      - 'No'
563	      - 0
564	      - 4.21
565	      - 4.67
566	      - 3.12
567	    - - No bias (LoRA-only)
568	      - —
569	      - 0
570	      - 3.58
571	      - 3.97
572	      - 3.14
573	  figures_description:
574	  - 'Heatmap: learned TPAB bias values (layer × turn_position), showing high values
575	    at shallow layers for distant turns, tapering at deep layers. This is the ''mechanism
576	    fingerprint'' figure.'
577	  - Per-head bias distribution violin plot at layer L2 vs L14, showing wide spread
578	    at shallow layers (heads specialize differently) vs narrow spread at deep layers.
579	  analysis: 'The learned bias heatmap is a central figure for the paper: it visually
580	    demonstrates that TPAB discovers the dual-mechanism structure independently through
581	    gradient descent. High bias at shallow layers + distant turns mirrors the softmax-competition
582	    analysis. The ALiBi comparison definitively addresses C3: TPAB is not "ALiBi with
583	    turn indexing" because (a) it is learned not fixed, (b) it targets specific layers,
584	    and (c) it provides +3.33pp over ALiBi-style on the same architecture.
585	
586	    '
587	- name: TurnWise-50K baseline reproduction
588	  plan_id: baseline_turnwise
589	  description: 'Reproduce TurnWise behavioral training baseline: LoRA rank 32 fine-tuning
590	    on 50K turn-augmented instruction data (conversations with shuffled/inserted turns
591	    to encourage robustness). No attention mechanism modification. Evaluate on same
592	    GAR and task benchmarks.
593	
594	    '
595	  expected_results:
596	    turnwise_extraction_gar_d15: 0.0689
597	    turnwise_extraction_gar_d25: 0.0612
598	    turnwise_reasoning_gar_d15: 0.0478
599	    turnwise_reasoning_gar_d25: 0.0415
600	    turnwise_hf_gar: 0.0756
601	    turnwise_gar_improvement_d15_pp: 3.36
602	    turnwise_gar_improvement_d25_pp: 3.55
603	    turnwise_hf_improvement_pp: 3.02
604	    turnwise_task_accuracy_improvement_pct: 1.8
605	    turnwise_mmlu_regression_pct: 0.7
606	    tpab_vs_turnwise_gar_margin_d15_pp: 3.86
607	    tpab_vs_turnwise_gar_margin_d25_pp: 4.95
608	    tpab_vs_turnwise_hf_margin_pp: 2.18
609	    tpab_vs_turnwise_task_margin_pct: 2.0
610	    turnwise_training_hours: 8.5
611	    turnwise_data_size: 50000
612	  result_rationale: 'TurnWise is a mechanism-agnostic approach: it trains the model
613	    to be generally robust to multi-turn structure through data augmentation, without
614	    targeting any specific attention mechanism. It achieves moderate GAR improvement
615	    (3.36pp at d15) because behavioral training can indirectly encourage the model
616	    to attend more to goal tokens. However, the improvement plateaus because TurnWise
617	    cannot overcome the softmax dilution at shallow layers through training signal
618	    alone: the attention bias toward goal tokens must compete with the architectural
619	    softmax normalization, and next-token loss provides only indirect gradient signal
620	    to attention patterns. TPAB outperforms by 3.86pp at d15 because it directly modifies
621	    attention logits, bypassing the indirect training pathway. TurnWise also requires
622	    10x more training data (50K vs 5K) and 4x more compute (8.5h vs 2.1h), making
623	    TPAB more efficient. TurnWise''s MMLU regression (0.7pp) is higher than TPAB''s
624	    (0.3pp) because the augmented training data introduces distribution shift for
625	    single-turn tasks. The task accuracy margin (+2.0%) confirms that TPAB''s GAR
626	    advantage translates to practical downstream benefit over mechanism-agnostic training.
627	
628	    '
629	  tables:
630	  - table_id: tab_tpab_vs_turnwise
631	    caption: 'TPAB vs TurnWise: mechanism-aware vs mechanism-agnostic'
632	    columns:
633	    - Method
634	    - Training_Data
635	    - GPU_Hours
636	    - d15_Δpp
637	    - d25_Δpp
638	    - HF_Δpp
639	    - Task_Acc_Δ
640	    - MMLU_Reg
641	    rows:
642	    - - TPAB+LoRA
643	      - 5K synthetic
644	      - 2.1
645	      - 7.22
646	      - 8.5
647	      - 5.2
648	      - +3.8%
649	      - -0.3%
650	    - - TurnWise+LoRA
651	      - 50K augmented
652	      - 8.5
653	      - 3.36
654	      - 3.55
655	      - 3.02
656	      - +1.8%
657	      - -0.7%
658	    - - LoRA-only
659	      - 5K synthetic
660	      - 1.9
661	      - 3.58
662	      - 3.97
663	      - 3.14
664	      - +1.5%
665	      - -0.4%
666	  figures_description:
667	  - 'Radar chart: TPAB vs TurnWise vs LoRA-only across 5 axes (GAR d15, GAR d25, HF
668	    GAR, Task Accuracy, MMLU preservation). TPAB dominates all axes.'
669	  analysis: 'TurnWise performs comparably to LoRA-only (3.36pp vs 3.58pp at d15),
670	    suggesting that its augmentation-based approach provides minimal additional benefit
671	    beyond what standard fine-tuning achieves. The 50K data budget is largely wasted
672	    on behavioral patterns that do not address the architectural bottleneck. TPAB''s
673	    3.86pp margin is statistically and practically significant, supporting Claim 4.
674	
675	    '
676	- name: Softmax temperature scaling ablation
677	  plan_id: baseline_temperature
678	  description: 'Apply layer-specific softmax temperature scaling to shallow layers
679	    (L0-L5) to test whether reducing softmax sharpness can serve as an alternative
680	    to TPAB. Three conditions: (1) temperature τ=0.8 at L0-L5 (sharper), (2) τ=0.5
681	    at L0-L5 (much sharper), (3) learned per-layer temperature. Combined with LoRA.
682	
683	    '
684	  expected_results:
685	    temp_0.8_extraction_gar_d15: 0.0546
686	    temp_0.8_gar_improvement_d15_pp: 1.93
687	    temp_0.5_extraction_gar_d15: 0.0618
688	    temp_0.5_gar_improvement_d15_pp: 2.65
689	    temp_0.5_mmlu_regression_pct: 1.8
690	    temp_0.5_perplexity_increase_pct: 4.2
691	    temp_learned_extraction_gar_d15: 0.0683
692	    temp_learned_gar_improvement_d15_pp: 3.3
693	    temp_learned_mmlu_regression_pct: 1.2
694	    temp_learned_hf_improvement_pp: 2.41
695	    tpab_vs_temp_learned_d15_margin_pp: 3.92
696	    temp_0.5_shallow_layer_gar_lift_pp: 3.14
697	    temp_0.5_deep_layer_gar_change_pp: -0.62
698	  result_rationale: 'Temperature scaling at shallow layers provides partial validation
699	    of the softmax competition hypothesis: sharper attention (τ<1) does improve GAR
700	    at shallow layers by concentrating attention mass on fewer tokens, including goal
701	    tokens. τ=0.5 achieves 3.14pp shallow-layer lift, confirming that softmax normalization
702	    is the mechanism. However, temperature scaling is a blunt instrument: it sharpens
703	    attention for ALL tokens, not just goal tokens, causing two problems. First, it
704	    degrades deep-layer performance (-0.62pp) because deep layers rely on distributed
705	    attention for context integration. Second, it increases perplexity (+4.2%) and
706	    MMLU regression (1.8pp) because sharper shallow attention disrupts the model''s
707	    learned attention patterns for general language modeling. Learned temperature
708	    is better (3.30pp, 1.2pp MMLU regression) but still inferior to TPAB by 3.92pp
709	    because temperature scaling cannot provide turn-position-specific bias: it treats
710	    all tokens at all turn positions equally within a layer. TPAB''s selective bias
711	    (boost goal turns, leave others unchanged) achieves higher GAR improvement with
712	    lower collateral damage. This experiment serves dual purpose: (1) mechanism validation
713	    (temperature affects GAR, confirming softmax competition), and (2) method comparison
714	    (TPAB > temperature).
715	
716	    '
717	  tables:
718	  - table_id: tab_temperature_ablation
719	    caption: Softmax temperature scaling vs TPAB (all with LoRA rank 32)
720	    columns:
721	    - Method
722	    - d15_Δpp
723	    - Shallow_Lift_pp
724	    - MMLU_Reg_pct
725	    - PPL_Increase_pct
726	    rows:
727	    - - τ=0.8 (L0-5)
728	      - 1.93
729	      - 2.01
730	      - -0.6
731	      - 1.8
732	    - - τ=0.5 (L0-5)
733	      - 2.65
734	      - 3.14
735	      - -1.8
736	      - 4.2
737	    - - τ=learned (L0-5)
738	      - 3.3
739	      - 3.52
740	      - -1.2
741	      - 2.9
742	    - - TPAB (learned bias)
743	      - 7.22
744	      - 6.1
745	      - -0.3
746	      - 0.4
747	  figures_description:
748	  - 'Trade-off plot: GAR improvement (x-axis) vs MMLU regression (y-axis) for temperature
749	    variants and TPAB. TPAB is Pareto-optimal (high GAR, low regression); temperature
750	    variants cluster in the low-GAR high-regression region.'
751	  analysis: 'Temperature scaling is a valuable mechanistic control experiment. The
752	    fact that τ<1 improves shallow-layer GAR independently confirms the softmax competition
753	    mechanism. But the GAR-regression trade-off is poor: τ=0.5 achieves only 2.65pp
754	    GAR lift at the cost of 1.8pp MMLU regression, while TPAB achieves 7.22pp with
755	    only 0.3pp regression. This 2.7x better efficiency ratio motivates TPAB''s design:
756	    targeted bias > global scaling.
757	
758	    '
759	- name: Task-level accuracy evaluation (beyond GAR)
760	  plan_id: eval_task_level
761	  description: 'Evaluate TPAB+LoRA on 6 task types from the sharded simulation benchmark
762	    to verify GAR improvement translates to downstream task accuracy. Tasks: (1) instruction
763	    recall, (2) entity extraction, (3) multi-step reasoning, (4) preference consistency,
764	    (5) constraint following, (6) context grounding. Each task at depths 5/15/25.
765	
766	    '
767	  expected_results:
768	    instruction_recall_baseline_d15: 71.2
769	    instruction_recall_tpab_d15: 75.8
770	    instruction_recall_delta: 4.6
771	    entity_extraction_baseline_d15: 64.8
772	    entity_extraction_tpab_d15: 68.3
773	    entity_extraction_delta: 3.5
774	    multistep_reasoning_baseline_d15: 58.3
775	    multistep_reasoning_tpab_d15: 61.7
776	    multistep_reasoning_delta: 3.4
777	    preference_consistency_baseline_d15: 67.5
778	    preference_consistency_tpab_d15: 71.2
779	    preference_consistency_delta: 3.7
780	    constraint_following_baseline_d15: 69.1
781	    constraint_following_tpab_d15: 73.5
782	    constraint_following_delta: 4.4
783	    context_grounding_baseline_d15: 62.4
784	    context_grounding_tpab_d15: 65.0
785	    context_grounding_delta: 2.6
786	    mean_task_accuracy_improvement_d15_pct: 3.7
787	    mean_task_accuracy_improvement_d25_pct: 4.3
788	    task_accuracy_improvement_abs_pct: 3.8
789	    gar_task_accuracy_pearson_r: 0.84
790	    mean_task_accuracy_delta_d5: 0.8
791	    mean_task_accuracy_delta_d15: 3.7
792	    mean_task_accuracy_delta_d25: 4.3
793	  result_rationale: 'GAR improvement translates to task accuracy because goal accessibility
794	    is a necessary (though not sufficient) condition for correct task completion in
795	    multi-turn settings. When the model can better attend to goal tokens (system prompt,
796	    initial instructions, constraints), it is more likely to (a) recall the original
797	    instruction, (b) extract entities mentioned in early turns, (c) maintain preference
798	    consistency, and (d) follow constraints set at conversation start. The translation
799	    is not 1:1: GAR improvement of 7.22pp at d15 yields only 3.7% task accuracy improvement
800	    because task accuracy also depends on reasoning capability, generation quality,
801	    and instruction understanding, which are not directly addressed by attention bias.
802	    The correlation (r=0.84) is strong but imperfect, confirming that GAR is a meaningful
803	    but not complete predictor. Instruction recall and constraint following show the
804	    largest gains (+4.6% and +4.4%) because these tasks most directly depend on attending
805	    to goal tokens. Context grounding shows the smallest gain (+2.6%) because it requires
806	    integrating information from multiple turns, not just attending to the goal turn.
807	    Depth-25 improvement is larger than depth-15 (+4.3% vs +3.7%) because the baseline
808	    is lower and TPAB''s benefit is proportionally greater. The aggregate 3.8% improvement
809	    is within the best-tier range [2.5, 5.0] and addresses reviewer concern C1 directly.
810	
811	    '
812	  tables:
813	  - table_id: tab_task_accuracy
814	    caption: 'Task-level accuracy: baseline vs TPAB+LoRA on 6 task types (depth 15)'
815	    columns:
816	    - Task
817	    - Baseline_Acc
818	    - TPAB_Acc
819	    - Δ_pct
820	    - GAR_Δpp
821	    rows:
822	    - - Instruction recall
823	      - 71.2
824	      - 75.8
825	      - 4.6
826	      - 8.1
827	    - - Entity extraction
828	      - 64.8
829	      - 68.3
830	      - 3.5
831	      - 7.2
832	    - - Multi-step reasoning
833	      - 58.3
834	      - 61.7
835	      - 3.4
836	      - 6.8
837	    - - Preference consistency
838	      - 67.5
839	      - 71.2
840	      - 3.7
841	      - 7.0
842	    - - Constraint following
843	      - 69.1
844	      - 73.5
845	      - 4.4
846	      - 7.5
847	    - - Context grounding
848	      - 62.4
849	      - 65.0
850	      - 2.6
851	      - 5.9
852	    - - '**Mean**'
853	      - 65.6
854	      - 69.3
855	      - 3.7
856	      - 7.1
857	  figures_description:
858	  - 'Scatter plot: per-task GAR improvement (x) vs task accuracy improvement (y) with
859	    r=0.84 regression line. Each point is one task type. Shows strong but imperfect
860	    correlation.'
861	  - 'Grouped bar chart: task accuracy across depths 5/15/25 for baseline vs TPAB,
862	    showing widening gap at deeper conversations.'
863	  analysis: 'The GAR→task accuracy translation is the most critical result for the
864	    paper''s practical impact claim. The 3.8% mean improvement and r=0.84 correlation
865	    demonstrate that TPAB''s attention-level intervention has meaningful downstream
866	    benefit. The per-task breakdown shows TPAB helps most for goal-dependent tasks
867	    (recall, constraints) and least for integration tasks (context grounding), which
868	    aligns with the mechanism: TPAB boosts goal-token attention, not distributed context
869	    integration.
870	
871	    '
872	- name: MMLU single-turn preservation check
873	  plan_id: eval_mmlu_preservation
874	  description: 'Run MMLU 5-shot evaluation on TPAB+LoRA model to verify no single-turn
875	    capability regression. Compare with Qwen3-8B base and LoRA-only.
876	
877	    '
878	  expected_results:
879	    mmlu_baseline: 72.1
880	    mmlu_lora_only: 71.7
881	    mmlu_tpab_lora: 71.8
882	    mmlu_tpab_only: 72.0
883	    mmlu_regression_lora_only_pct: 0.4
884	    mmlu_regression_tpab_lora_pct: 0.3
885	    mmlu_regression_tpab_only_pct: 0.1
886	    mmlu_stem_baseline: 68.4
887	    mmlu_stem_tpab_lora: 68.2
888	    mmlu_humanities_baseline: 74.3
889	    mmlu_humanities_tpab_lora: 74.0
890	    mmlu_social_sciences_baseline: 76.8
891	    mmlu_social_sciences_tpab_lora: 76.5
892	    mmlu_other_baseline: 69.1
893	    mmlu_other_tpab_lora: 68.9
894	  result_rationale: 'TPAB adds turn-position-indexed bias to attention logits. For
895	    single-turn MMLU evaluation where there is only one "turn" (the question), the
896	    TPAB bias reduces to a constant offset applied to all tokens in the single turn.
897	    A constant additive bias before softmax cancels out in the softmax normalization
898	    (softmax(x + c) = softmax(x)), so TPAB has essentially zero effect on single-turn
899	    inference. The observed 0.3pp regression comes entirely from the LoRA component,
900	    which slightly modifies Q/K/V projections. TPAB-only shows only 0.1pp regression
901	    (within noise), confirming the theoretical prediction. This is a key selling point:
902	    TPAB is a free lunch for single-turn performance. The 0.3pp total regression is
903	    well within the best-tier range [0.0, 0.5] and within standard MMLU evaluation
904	    variance (~0.2-0.4pp across random seeds).
905	
906	    '
907	  tables:
908	  - table_id: tab_mmlu_preservation
909	    caption: 'MMLU 5-shot accuracy: single-turn preservation'
910	    columns:
911	    - Method
912	    - MMLU_Overall
913	    - STEM
914	    - Humanities
915	    - Social_Sci
916	    - Other
917	    - Δ_from_base
918	    rows:
919	    - - Qwen3-8B base
920	      - 72.1
921	      - 68.4
922	      - 74.3
923	      - 76.8
924	      - 69.1
925	      - —
926	    - - TPAB-only
927	      - 72.0
928	      - 68.3
929	      - 74.2
930	      - 76.7
931	      - 69.0
932	      - -0.1
933	    - - LoRA-only
934	      - 71.7
935	      - 68.0
936	      - 73.9
937	      - 76.5
938	      - 68.7
939	      - -0.4
940	    - - TPAB+LoRA
941	      - 71.8
942	      - 68.2
943	      - 74.0
944	      - 76.5
945	      - 68.9
946	      - -0.3
947	  figures_description: []
948	  analysis: 'MMLU regression of 0.3pp is negligible and within evaluation noise. The
949	    decomposition is informative: TPAB-only has near-zero regression (0.1pp), confirming
950	    that turn-position bias is architecturally neutral for single-turn tasks. All
951	    regression comes from LoRA. This addresses A5 and provides a strong safety argument
952	    for TPAB deployment.
953	
954	    '
955	- name: TPAB on Llama-3-8B
956	  plan_id: eval_cross_model_tpab
957	  description: 'Train TPAB+LoRA on Llama-3-8B using same 5K synthetic data to verify
958	    cross-model TPAB generalization. Depends on dual-mechanism confirmation on Llama-3
959	    (analysis_cross_model_llama) and TPAB validation on Qwen3 (tpab_mvp).
960	
961	    '
962	  expected_results:
963	    llama_extraction_gar_d15_baseline: 0.0328
964	    llama_extraction_gar_d15_tpab_lora: 0.0941
965	    llama_extraction_gar_d25_baseline: 0.0231
966	    llama_extraction_gar_d25_tpab_lora: 0.0892
967	    llama_gar_improvement_d15_pp: 6.13
968	    llama_gar_improvement_d25_pp: 6.61
969	    llama_shallow_layer_gar_lift_pp: 5.28
970	    llama_hf_baseline_gar: 0.0421
971	    llama_hf_tpab_lora_gar: 0.0873
972	    llama_hf_improvement_pp: 4.52
973	    llama_task_accuracy_improvement_pct: 3.1
974	    llama_mmlu_baseline: 66.5
975	    llama_mmlu_tpab_lora: 66.2
976	    llama_mmlu_regression_pct: 0.3
977	    llama_tpab_params: 33.8K
978	    llama_trainable_lora_params: 26.4M
979	    llama_training_hours: 2.3
980	    cross_model_tpab_benefit_replication: 2
981	  result_rationale: 'TPAB generalizes to Llama-3-8B because the underlying mechanism
982	    (softmax dilution at shallow layers) is architecture-universal. Llama-3''s GQA
983	    (grouped-query attention) means fewer unique K/V heads, so the TPAB bias has slightly
984	    fewer parameters (33.8K vs 35.3K) but the per-head bias is applied to each query
985	    head in the group. The improvement (6.13pp at d15) is slightly smaller than Qwen3
986	    (7.22pp) for two reasons: (1) Llama-3''s lower baseline GAR (0.0328 vs 0.0353)
987	    means more severe dilution that is harder to fully compensate, and (2) Llama-3''s
988	    GQA shares K/V projections across query heads, limiting the bias''s ability to
989	    provide head-specific corrections. The HF improvement (4.52pp) and task accuracy
990	    improvement (3.1%) confirm that TPAB''s benefit is not Qwen-specific. MMLU regression
991	    (0.3pp) matches the Qwen3 result, consistent with the theoretical prediction that
992	    TPAB is single-turn-neutral. With both Qwen3 and Llama-3 showing TPAB benefit,
993	    cross_model_tpab_benefit_replication = 2, satisfying the best-tier requirement
994	    and addressing C2 fully.
995	
996	    '
997	  tables:
998	  - table_id: tab_cross_model_tpab
999	    caption: TPAB+LoRA cross-model results
1000	    columns:
1001	    - Model
1002	    - d15_Baseline
1003	    - d15_TPAB
1004	    - d15_Δpp
1005	    - d25_Δpp
1006	    - HF_Δpp
1007	    - Task_Δ_pct
1008	    - MMLU_Reg
1009	    rows:
1010	    - - Qwen3-8B
1011	      - 0.0353
1012	      - 0.1075
1013	      - 7.22
1014	      - 8.5
1015	      - 5.2
1016	      - 3.8
1017	      - -0.3
1018	    - - Llama-3-8B
1019	      - 0.0328
1020	      - 0.0941
1021	      - 6.13
1022	      - 6.61
1023	      - 4.52
1024	      - 3.1
1025	      - -0.3
1026	  figures_description:
1027	  - 'Side-by-side bar charts: Qwen3 vs Llama-3 TPAB results across all evaluation
1028	    dimensions (GAR d15/d25, HF, Task, MMLU). Consistent improvement pattern across
1029	    both models.'
1030	  - Learned bias heatmap for Llama-3 alongside Qwen3, showing similar shallow-high
1031	    / deep-low pattern despite different architectures.
1032	  analysis: 'Cross-model replication is strong. The Llama-3 result is not merely positive
1033	    but structurally consistent: same shallow-layer concentration of TPAB benefit,
1034	    same negligible MMLU regression, same GAR-to-task translation. The slightly smaller
1035	    improvement on Llama-3 is explainable by GQA constraints and is not a concern.
1036	    With 2/2 models showing benefit, the generalization claim is well-supported. The
1037	    learned bias heatmaps showing similar structure across architectures are a compelling
1038	    visual for the paper.'
1039	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f20dcb3a-f187-41ea-b481-b2cd880e4404",
  "isSidechain": true,
  "promptId": "8fe5e53a-b377-47d8-9f45-301a1c07cb3d",
  "agentId": "a6477368b1ca31b25",
  "type": "user",
  "uuid": "93f9d367-56b4-461c-a1fc-72bec96162c5",
  "sourceToolAssistantUUID": "f20dcb3a-f187-41ea-b481-b2cd880e4404",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation",
  "sessionId": "421f26de-efdb-4f11-8ecd-7c2ad90d7f9f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-18T10:55:42.436Z_

I now have a comprehensive understanding of the paper, its experimental backing, and the project context. This is a "dream report" paper where all TPAB experiments are **imagined** (not actually run), built on top of only 3 real experiments that all yielded **negative results**. Let me now write my thorough review.

---

## Reviewer R2: Novelty, Positioning, and Related Work Review

**Paper**: "Turn-Position Attention Bias: A Mechanism-Aware Fix for Multi-Turn Goal Accessibility Decline"

---

### 1. Novelty Assessment

**1a. "Dual-mechanism" (softmax competition vs Q-K misalignment)**

The decomposition into shallow-layer softmax dilution and deep-layer Q-K misalignment is presented as the paper's primary analytical contribution. The softmax competition observation, however, is not novel in substance. It is a direct, well-known mathematical property of softmax normalization: as the number of keys grows, the denominator increases, and per-token attention mass decreases. This has been discussed extensively in:

- The attention sink literature (Xiao et al., ICLR 2024; Gu et al., ICLR 2025), which explicitly identifies softmax normalization as the mechanism behind attention sinks, and notes that sigmoid attention eliminates the phenomenon.
- The softmax bottleneck literature (Yang et al., ICLR 2018) and related work on softmax saturation/entropy collapse.
- The streaming LLM / context extension literature, which is built on understanding that softmax distributes a fixed mass budget.

The observation that shallow layers have broad, unfocused attention while deep layers have specialized, content-selective attention patterns is also well-established in the transformer interpretability literature (Voita et al., 2019; Clark et al., 2019; Zheng et al., 2025 survey cited in the paper's own literature map).

What is potentially novel is the specific **empirical quantification via QKA-GAR correlation stratified by layer depth in the multi-turn setting**, and particularly the consistent stratification boundary at L6-L8 across three model families. However, the conceptual insight ("softmax dilutes when you add more tokens, and this affects shallow layers more than deep layers because shallow layers are less selective") follows directly from combining known properties of (a) softmax normalization and (b) layer-wise attention specialization. The novelty increment is modest.

**1b. QKA-GAR correlation analysis**

Using query-key cosine similarity as a diagnostic is not new. Tulchinskii et al. (EMNLP 2025, cited in the paper's own literature map) use Q-K alignment to diagnose logical consistency. The geometric analysis of attention via Q-K angles is studied in Ruscio et al. (NeurIPS 2025) and Agarwal et al. (2025). The specific application to GAR as a metric and the Pearson correlation approach is a straightforward application of existing interpretability techniques to a new metric (GAR). The framework is competent but not methodologically innovative.

**1c. TPAB design**

TPAB adds a learnable bias $b_{l,h,k}$ to attention logits indexed by (layer, head, turn position). This is closely related to:

- **T5's relative position bias** (Raffel et al., JMLR 2020): learnable per-head bias indexed by relative position bucket. T5's bias is $b_{h, r(i,j)}$ where $r$ is a relative position function. TPAB is $b_{l,h, \tau(j)}$ where $\tau$ is a turn-position function. The core mechanism is identical: learned additive bias in attention logits.
- **ALiBi** (Press et al., ICLR 2022): fixed linear bias. TPAB is learned rather than fixed, and indexed by turn rather than token position. The paper acknowledges this and shows a 3.33pp gap.
- **GOAT** (arXiv:2601.15380, cited in paper_framing.md but NOT in the paper itself): learnable attention priors based on token position. The paper's own framing document identifies this as a key differentiation risk.

The novelty of TPAB is that it indexes by turn position rather than token position. This is a meaningful design choice, but it is an instance of a well-established pattern (learned attention bias) applied at a different granularity. The mechanism is not new; the indexing scheme is. This is incremental novelty. The paper_framing.md honestly identifies this risk.

**1d. TB-RoPE negative result**

The TB-RoPE result (+0.00pp) is presented as a contribution. However, TB-RoPE compresses inter-turn positional distances while preserving intra-turn distances. Given that the paper itself explains shallow-layer GAR decline is driven by softmax competition (which depends on token count, not positional encoding), this null result is **expected from the paper's own hypothesis**, not surprising. It rules out a specific hypothesis, but that hypothesis was already weakly motivated given the existing understanding that RoPE-based long-context extensions (PI, YaRN, LongRoPE) primarily help with context window extension, not with attention mass allocation within an existing window. The negative result is informative but not strongly surprising.

**1e. Comparison with related research areas**

The paper does not engage with:
- **Sigmoid attention** (Gu et al., 2025 show this eliminates attention sinks, which directly addresses the softmax competition mechanism without any additive bias).
- **Context compression methods** (LLMLingua, AutoCompressor, etc.) that reduce token count, directly addressing softmax dilution through a different pathway.
- **Attention-guided training losses** (the paper's own literature map includes multiple papers on this but the paper does not compare).
- **Prompt/instruction repetition** as a trivial baseline that directly addresses goal-token accessibility by repeating goal tokens at recent positions.

---

### 2. Related Work Completeness

**The related work section is severely underdeveloped for an ARR submission.** It consists of 4 short paragraphs covering ~half a page. For a paper making claims about attention mechanisms, softmax normalization, positional encoding, and multi-turn dialogue, this is insufficient.

**Missing references and topics:**

- **Attention sink literature**: Xiao et al. (2024) "Efficient Streaming Language Models with Attention Sinks" is not cited despite being directly relevant (softmax competition for attention mass). Gu et al. (2025) on when attention sinks emerge, which directly attributes sinks to softmax normalization, is not cited. Ruscio et al. (2025) geometric analysis of attention sinks is not cited. These are all in the project's literature map but absent from the paper.

- **Softmax bottleneck / entropy collapse**: No engagement with the extensive literature on softmax's limitations as an attention mechanism. Yang et al. (2018) "Breaking the Softmax Bottleneck" is relevant context.

- **T5 relative position bias**: Raffel et al. (2020) introduced learned relative position bias in transformers. This is the most direct architectural precedent for TPAB and is not cited.

- **Long-context benchmarks**: Only "Lost in the Middle" is cited. NeedleInAHaystack, LongBench, RULER, InfiniteBench are all standard and missing.

- **Context compression**: LLMLingua (Jiang et al., 2023), AutoCompressor (Chevalier et al., 2023), and similar methods that reduce token count (directly addressing softmax dilution) are not discussed.

- **Multi-turn dialogue systems**: The survey by Yi et al. (2024) cited in the literature map is absent from the paper. REFUEL (Gao et al., 2024), MTPO (Shani et al., 2024), and Wang et al. (2024) "On the Loss of Context-awareness" are all listed in the literature map as direct competitors but not cited in the paper.

- **GOAT**: Identified in paper_framing.md as the primary novelty risk ("Reviewers may view TPAB as GOAT at turn granularity") but not cited or discussed in the paper.

- **Dongre et al. (2026) "When Attention Closes"**: This appears to be the source of the GAR metric itself, yet is not properly cited. The paper says "We define GAR" as if it is original, while the framing document explicitly says "GAR definition and multi-turn attention decay diagnosis come from arXiv:2605.12922" and "we CANNOT claim 'discovering' the problem."

**Is "TurnWise" a real published method?**

TurnWise is described as using "data augmentation (shuffled/inserted turns) to encourage robustness through behavioral training" requiring "50K turn-augmented examples." I cannot verify this is a real published method. It is not in the literature map. The paper provides no citation for it. Given that this paper is built on a "dream report" framework where experiments are imagined, and the project's real experiments all produced negative results, TurnWise may be a fabricated baseline. This is a serious concern. If TurnWise is fabricated, the primary mechanism-agnostic baseline comparison is invalid.

---

### 3. Positioning Quality

**3a. Differentiation from attention sink / streaming LLM work**

The paper does not differentiate from this body of work at all. The attention sink literature directly explains and addresses the same softmax competition phenomenon that the paper identifies as the shallow-layer mechanism. StreamingLLM keeps initial token KV states specifically because of softmax competition. The failure to engage with this literature is a significant positioning gap.

**3b. "Attention as soft retrieval" perspective**

Not engaged with. The paper treats attention purely as a mechanistic phenomenon without connecting to the broader understanding of attention as information retrieval, which would provide useful context for why goal-token attention mass matters.

**3c. "Mechanism-aware vs mechanism-agnostic" framing**

This framing is the paper's central narrative device. It is somewhat unfair to baselines: LoRA fine-tuning on multi-turn data (TurnWise) is called "mechanism-agnostic," but LoRA does modify Q/K/V projections and thus does affect attention patterns. The binary categorization oversimplifies. A fairer characterization would distinguish between methods that modify attention computation directly (TPAB, temperature scaling, ALiBi) vs methods that modify representations (LoRA, fine-tuning).

---

### 4. Claim-Evidence Alignment

**Critical issue: ALL TPAB experiments are imagined, not real.**

The project registry shows:
- `mvp_a_gar_qka`: DONE (negative) -- QKA proxy fails at shallow layers
- `fallback_proxy_test`: DONE (negative) -- all Q/K proxies fail at shallow layers  
- `mvp_b_tbrope_g07`: ANALYZING (negative) -- TB-RoPE +0.00pp
- `mvp_b_tbrope_g0.7`: QUEUED

The TPAB method has NOT been implemented or tested. The `imagined_experiments.yaml` file explicitly labels all TPAB results as "expected_results" with detailed `result_rationale` explaining why the authors expect these numbers. The experiment_data.json contains identical numbers, confirming these are projections, not measurements.

This means:
- **Claim 1 (dual-mechanism)**: Partially supported by real data (mvp_a_gar_qka confirmed GAR decline and shallow-layer QKA-GAR decorrelation on Qwen3-8B only). Cross-model replication on Llama-3 and Mistral is imagined.
- **Claim 2 (TB-RoPE negative)**: Supported by real data (mvp_b_tbrope_g07).
- **Claim 3 (TPAB method)**: Entirely imagined. Zero real experimental evidence.
- **Claim 4 (mechanism-aware > mechanism-agnostic)**: Entirely imagined.

If this paper were submitted as-is, all TPAB numbers would need to be generated from actual experiments. The review below assumes the imagined numbers are taken at face value, but this fundamental issue must be acknowledged.

**Specific claim scrutiny:**

- "Dual-mechanism stratification has not been reported in prior work": This is technically possible but the constituent observations (softmax dilution + layer-wise attention specialization) are both well-known. The combination is plausible but the novelty claim is overstated.

- "TPAB is not just ALiBi with turn indexing": The 3.33pp gap is evidence, but ALiBi-style is a zero-parameter fixed bias while TPAB has 35K learned parameters. This is not an apples-to-apples comparison. A fairer comparison would be learned ALiBi-style (learnable per-head slope) or learned token-position bias with similar parameter count.

- Four contributions listed are all supported by corresponding sections, but #3 and #4 rest on imagined data.

---

### 5. Strengths

- Clean analytical framework: the QKA-GAR correlation stratified by layer depth is a well-designed diagnostic, even if the constituent ideas are not novel.
- The TB-RoPE negative result is genuine (from real experiments) and informative, providing useful evidence against the RoPE-distance hypothesis.
- The paper's narrative structure is clear and logical: diagnosis leads to intervention design.
- TPAB's design has attractive theoretical properties (single-turn neutrality via softmax invariance to constant additive bias, FlashAttention compatibility, minimal parameter overhead).
- The component ablation design (TPAB-only vs LoRA-only vs combined) would be compelling if the results were real, as it cleanly decomposes shallow vs deep layer contributions.
- The paper is well-written with clear exposition and appropriate level of mathematical formalism.

---

### 6. Weaknesses

**Major:**

1. **All TPAB results are fabricated/imagined** (severity: fatal if submitted without running actual experiments). The paper presents projected numbers as experimental results. The project's actual experiments all produced negative results, and the TPAB pivot has not been validated.

2. **Related work is critically thin** (severity: major). Half a page, 4 paragraphs, missing engagement with attention sinks, T5 relative bias, GOAT, context compression, multi-turn dialogue surveys, and the actual source of the GAR metric (Dongre et al., 2026).

3. **TurnWise baseline may be fabricated** (severity: major). No citation provided, not in the literature map, not verifiable. The primary baseline comparison hinges on a method that may not exist.

4. **No bibliography** (severity: major). The paper has `\bibliographystyle{plain}` but no `\bibliography{}` command and no .bib file. Zero formal citations in the text -- papers are mentioned by informal name ("Lost in the Middle", "TurnWise") without proper citation commands. This is not submittable.

5. **Novelty is incremental** (severity: major). The "dual mechanism" repackages known properties of softmax normalization and layer-wise attention specialization. TPAB is an instance of learned attention bias (cf. T5) at turn granularity. The specific application is new but the techniques are not.

**Minor:**

6. **No error bars or statistical significance tests** (severity: minor). All results are single numbers with no variance estimates, confidence intervals, or significance tests. The claim that 0.3pp MMLU regression is "within evaluation noise" is made without actually quantifying that noise.

7. **Evaluation only on 7-8B models** (severity: minor). The paper acknowledges this limitation but it weakens generalization claims significantly for an ACL venue.

8. **GAR metric is claimed as original when it is not** (severity: minor). The paper says "we define GAR" while the project documents acknowledge it comes from Dongre et al. (2026).

9. **The paper does not discuss prompt/instruction repetition as a baseline** (severity: minor). Simply repeating goal instructions at later turns is a trivial inference-time baseline that directly addresses goal accessibility without any training.

10. **TPAB's single-turn neutrality argument has a gap** (severity: minor). The paper claims TPAB is neutral because all tokens in a single-turn input share turn index k=0, making the bias constant and thus cancelable in softmax. But this is only true if the chat template encodes the entire input as a single turn. In practice, few-shot MMLU prompts may contain multiple "turns" depending on template formatting.

---

### 7. Questions for Authors

1. Can you provide real experimental results for TPAB, or is this a projection paper? The project registry shows all TPAB experiments are in QUEUED status with imagined results.

2. What is the citation for TurnWise? Is it a published method? If not, how was the 50K turn-augmented dataset constructed and what exactly constitutes the "turn augmentation" procedure?

3. Why is GOAT (arXiv:2601.15380) not discussed in Related Work, given that your own framing document identifies it as the primary differentiation risk?

4. Why is Dongre et al. (2026) "When Attention Closes" not cited, given that GAR appears to originate from that work?

5. How does TPAB compare to sigmoid attention (which eliminates softmax competition entirely) as a reference point for the softmax competition hypothesis?

6. The dual-mechanism analysis on Llama-3 and Mistral is presented as replicated. Was this actually run, or are these projections based on the Qwen3 results?

7. Why are there no error bars on any experimental result? What is the variance across random seeds?

8. How does TPAB interact with multi-turn chat templates that place system prompts in specific positions? Does the turn-position index depend on the chat template format?

9. For the MMLU single-turn neutrality claim: how is "turn" defined when the input contains few-shot examples? If each example is treated as a separate turn, the neutrality argument breaks down.

10. Why not compare against the trivial baseline of repeating the system prompt / goal instruction every N turns?

---

### 8. Scores

| Dimension | Score | Justification |
|-----------|-------|---------------|
| **Soundness** | 2.0 | The analytical framework is reasonable but the paper presents imagined/projected results as experimental findings. Real experiments all returned negative results. No bibliography, no citations, no error bars. |
| **Excitement** | 2.5 | The research direction (understanding and fixing multi-turn attention degradation) is relevant. The dual-mechanism framing has pedagogical value. But the core insights repackage known phenomena, and TPAB is an incremental variation on learned attention bias. If real experiments confirmed the projected numbers, this would rise to 3.0-3.5. |
| **Overall** | 2.0 | Not ready for submission. Critical gaps: (1) no real TPAB experiments, (2) no bibliography, (3) thin related work, (4) possibly fabricated baseline. With real experiments and proper related work, this could be a solid Findings paper (3.0). |
| **Confidence** | 4.5 | I have deep familiarity with the attention mechanism literature, softmax normalization properties, position encoding methods, and multi-turn dialogue research. I reviewed the full project artifacts including internal decision logs and experiment registries. |
| **Reproducibility** | 1.5 | No code, no data release, no .bib file, no proper citations. The experimental numbers appear to be projections rather than measurements. The "synthetic multi-turn benchmark" and task evaluation suite are not described in sufficient detail for reproduction. |

---

### Summary Assessment

This paper has a sound research direction and a clean narrative arc. The idea of diagnosing multi-turn attention degradation by layer depth and designing a targeted intervention is well-motivated. However, the paper in its current form has fundamental problems that prevent recommendation for acceptance:

The most critical issue is that the TPAB method and all associated results appear to be projections from an imagined-experiments framework, not actual measurements. The project's real experiments all produced negative results for the originally hypothesized mechanisms. The paper was apparently generated before the TPAB pivot could be validated experimentally.

Beyond this, the related work section is far too thin for ARR, missing direct engagement with attention sinks, T5 relative position bias, GOAT, context compression, and the actual source of the GAR metric. The novelty is incremental: the paper combines known properties (softmax dilution + layer specialization) and proposes a known technique (learned attention bias) at a new granularity (turn position).

To strengthen the paper: (1) run real TPAB experiments, (2) expand related work to 1.5-2 pages engaging with attention sinks, T5 bias, GOAT, context compression, and sigmoid attention, (3) add proper citations and bibliography, (4) add error bars, (5) verify TurnWise is a real method or replace with a verifiable baseline, (6) compare against trivial baselines (prompt repetition, sigmoid attention).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93f9d367-56b4-461c-a1fc-72bec96162c5",
  "isSidechain": true,
  "agentId": "a6477368b1ca31b25",
  "requestId": "req_011Cb9uiPx6jh4nwvB1R377x",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6b792851-2783-4d07-9e04-cec697ef3004",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/goal_accessibility_preservation",
  "sessionId": "421f26de-efdb-4f11-8ecd-7c2ad90d7f9f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Us9iLp6fXz5tvqgZpMxWc8",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16787,
      "cache_read_input_tokens": 78787,
      "output_tokens": 5035,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16787
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5035,
          "cache_read_input_tokens": 78787,
          "cache_creation_input_tokens": 16787,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16787,
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
