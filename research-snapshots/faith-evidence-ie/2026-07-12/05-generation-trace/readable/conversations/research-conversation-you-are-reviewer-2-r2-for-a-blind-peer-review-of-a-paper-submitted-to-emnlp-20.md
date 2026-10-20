# Research conversation: You are Reviewer 2 (R2) for a blind peer review of a paper submitted to EMNLP 2026 Main (via ACL Rolling Review). Your f

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 50
- **Recorded user turns:** 1
- **Tool calls:** 20
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a9bd4203964701927.jsonl`
- **Structured JSON:** [`112fc31dcf9c89c0100d.json`](../../sessions/11/112fc31dcf9c89c0100d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

50 recorded events

### User

_source line 1 · 2026-05-15T12:47:17.960Z_

You are Reviewer 2 (R2) for a blind peer review of a paper submitted to EMNLP 2026 Main (via ACL Rolling Review). Your focus areas are **Novelty**, **Related Work**, and **Presentation/Framing**.

## ARR Review Scoring (EMNLP 2026)
- **Soundness**: 1-5 (5=Excellent, 4=Strong, 3=Acceptable, 2=Borderline, 1=Poor)
- **Excitement**: 1-5 (5=Highly Exciting, 4=Exciting, 3=Ambivalent, 2=Below Average, 1=Not Exciting)
- **Overall Assessment**: 1-5 with half-points (5=Award-worthy, 4=Accept main, 3.5=Leaning accept, 3=Borderline, 2.5=Leaning reject, 2=Reject/resubmit, 1.5=Major revision needed, 1=Do not resubmit)

## Paper: "Why Online RL Catastrophically Fails for Structured Information Extraction, and What Works Instead"

**Abstract**: Studies online RL (GRPO) for document-level RE with evidence generation on DocRED. Finds GRPO universally fails: reward increases while extraction F1 collapses. Evidence learning and relation extraction decouple. Proposes RSFT with NLI-based filtering as practical alternative (+3.7 F1 on test). Introduces EDCR metric for entity-sharing distractor citations.

**Three contributions claimed**:
1. Systematic demonstration that GRPO fails for structured IE with evidence–extraction decoupling analysis (§5)
2. RSFT with NLI-based filtering as effective offline alternative (§6)
3. EDCR diagnostic metric (§7)

**Related Work (§2)** covers:
- DocRE: ATLOP, DREEAM, SAIS; mentions LMRC, DocKS-RAG as generative but without evidence
- RL for NLP: RLHF, GRPO, references LongRLVR for gradient vanishing theory
- RSFT: ReST, offline RL literature, theoretical equivalence to conservative PPO
- Faithfulness: NLI-based metrics for summarization, extends to IE

**Key paper claims and their support**:

Claim 1 (GRPO failure): Tested 3 reward functions × multiple lr. Results:
- CED (lr=5e-5): rel_F1 peaks at 0.217
- CED (lr=5e-6): rel_F1=0.014 but evi_F1=0.850 (decoupling)
- flat-NLI and extract-only: collapse within 25-30 steps
- Connected to LongRLVR's gradient vanishing theory

Claim 2 (RSFT works): 
- Dev: +6.0pp rel_F1 over SFT
- Test: +3.7pp rel_F1 over SFT
- BUT: CED vs flat-NLI scoring is NOT statistically significant (p=0.08, 0.38, 0.12)
- Paper's own conclusion: "the benefit comes from rejection sampling itself, not CED"

Claim 3 (EDCR metric):
- Correlation with Evi-F1: r=-0.42 (weak to moderate)
- Best method still has 63.5% distractor citations
- Cross-method analysis on 5 methods

**Comparison with encoder methods (Table 6)**:
- DREEAM: rel_F1=0.630 (test), evi_F1=0.573 (test)
- This paper: rel_F1=0.392 (test), evi_F1=0.765 (test)
- Paper acknowledges cross-protocol comparison issues
- Extraction F1 substantially trails encoder SOTA (~0.63 vs 0.392)

**Model size ablation**: 1.7B (+2.6pp), 4B (+6.0pp), 8B (+1.7pp) — non-monotonic gains
**Re-DocRED**: RSFT gain shrinks from +6.0pp to +2.3pp with cleaner annotations
**NLI model ablation**: DeBERTa-large doesn't help downstream

**Title framing**: "Why Online RL Catastrophically Fails... and What Works Instead"
- The "what works" (RSFT) is relatively standard (rejection sampling fine-tuning exists in prior work)
- The paper's own ablations show CED is not the key — plain rejection sampling works equally well
- The paper honestly reports all negative results

## Your Task

Write a detailed R2 review focusing on:
1. **Novelty assessment**: How novel is each contribution? Is the GRPO failure finding surprising given existing theory? Is RSFT methodologically novel or a straightforward application? Is EDCR a significant metric contribution?
2. **Related work completeness**: Are important baselines missing? Is the positioning fair?
3. **Framing and claims**: Does the title/framing match what the paper actually shows? Are claims calibrated to evidence?
4. **Significance and impact**: Would this change how the community approaches RL for structured IE?
5. **Writing quality and clarity**

Structure your review as:
- Summary of contributions (2-3 sentences)
- Strengths (bulleted)
- Weaknesses (bulleted, numbered W1, W2, etc.)
- Questions for authors
- Scores: Soundness, Excitement, Overall Assessment (use ARR scale above)
- Confidence: 1-5 (5=expert, 3=knowledgeable, 1=not familiar)

Be rigorous but fair. Evaluate novelty against the current landscape of RL for NLP (post-DeepSeek-R1, GRPO widely used for reasoning). Give specific, actionable feedback.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "00a1eb94-0484-4e13-931d-e659507bc0c6",
  "agentId": "a9bd4203964701927",
  "type": "user",
  "uuid": "8e613f23-04a3-4741-bae3-7babc1406f7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-15T12:47:17.962Z_

```json
{
  "parentUuid": "8e613f23-04a3-4741-bae3-7babc1406f7d",
  "isSidechain": true,
  "agentId": "a9bd4203964701927",
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
  "uuid": "7666e0f5-d799-4c6f-b8f1-85376397fea2",
  "timestamp": "2026-05-15T12:47:17.962Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-15T12:47:21.005Z_



I'll start by reading the paper and related project files to give a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7666e0f5-d799-4c6f-b8f1-85376397fea2",
  "isSidechain": true,
  "agentId": "a9bd4203964701927",
  "requestId": "req_011Cb4NxWZyNoxYLDhurm8Mk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9cabcc9c-1f1d-4a7d-971b-192f376f7da1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NVbBoQhGP9jrk9iA4JVmzR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7241,
      "cache_read_input_tokens": 8249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7241,
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

_source line 4 · 2026-05-15T12:47:21.709Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_0148kJkDF3wZRpZ2G8SEkZwY`</summary>

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
  "parentUuid": "9cabcc9c-1f1d-4a7d-971b-192f376f7da1",
  "isSidechain": true,
  "agentId": "a9bd4203964701927",
  "requestId": "req_011Cb4NxWZyNoxYLDhurm8Mk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "be1467fe-0380-4f92-a5c5-36841ad23bbb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NVbBoQhGP9jrk9iA4JVmzR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7241,
      "cache_read_input_tokens": 8249,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7241
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 124,
          "cache_read_input_tokens": 8249,
          "cache_creation_input_tokens": 7241,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7241,
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

_source line 5 · 2026-05-15T12:47:21.719Z_

<details><summary>↩ Tool result · `toolu_0148kJkDF3wZRpZ2G8SEkZwY`</summary>

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
  "parentUuid": "be1467fe-0380-4f92-a5c5-36841ad23bbb",
  "isSidechain": true,
  "promptId": "00a1eb94-0484-4e13-931d-e659507bc0c6",
  "agentId": "a9bd4203964701927",
  "type": "user",
  "uuid": "df4298eb-5e27-4cd1-b06c-1e4dbe2c2ce6",
  "sourceToolAssistantUUID": "be1467fe-0380-4f92-a5c5-36841ad23bbb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-15T12:47:24.422Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01PA4g9Zd8gHU85vDDKfwuLm`</summary>

```json
{
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df4298eb-5e27-4cd1-b06c-1e4dbe2c2ce6",
  "isSidechain": true,
  "agentId": "a9bd4203964701927",
  "requestId": "req_011Cb4NxnyhcwFEgiDZBdxws",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "08dfff52-5a1f-427d-bf4a-fa1407c55bf7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013vim2fZW6iLmU5PShteARX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15490,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1447,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 49,
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

_source line 7 · 2026-05-15T12:47:24.632Z_

<details><summary>↩ Tool result · `toolu_01PA4g9Zd8gHU85vDDKfwuLm`</summary>

```text
{"result":"# 项目 faith-evidence-ie 概况\n\n## 实验状态 (74 个)\n\n- **mvp2_sft_eval_r2**: DONE (success) — \n- **mvp2_sft_eval**: DONE (killed) — \n- **mvp2_grpo_flatnli_r2**: DONE (killed) — \n- **mvp2_grpo_extract_r2**: DONE (killed) — \n- **mvp2_grpo_ced_r4**: DONE (killed) — \n- **mvp2_grpo_extract**: DONE (failed) — \n- **mvp2_grpo_flatnli**: DONE (failed) — \n- **mvp2_grpo_ced_r3**: DONE (failed) — \n- **mvp2_grpo_ced_r2**: DONE (killed) — \n- **mvp2_grpo_ced_r1**: DONE (killed) — \n- **mvp2_grpo_ced**: DONE (failed) — \n- **precompute_nli_train**: DONE (success) — \n- **mvp2_sft_warmup**: DONE (success) — \n- **smoke_test_grpo**: DONE (success) — \n- **mvp1_ced_signal**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-15\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| mvp2_rsft_ced_scoring_topk3_r2 | CED scoring ablation: top_k=3 (vs top_k=1). More training data (~8000 samples) vs stricter selection (2718 samples). Retry with HF_HUB_OFFLINE=1 (NLI model cached locally). | — | — | — |\n| mvp2_rsft_ced_scoring_topk3 | CED scoring ablation: top_k=3 (vs top_k=1). More training data (~8000 samples) vs stricter selection (2718 samples). Answers: does CED filtering strictness affect RSFT training quality? | — | — | — |\n| mvp2_eval_rsft_r2b_maxtok1536_r2 | Truncation diagnosis: r2b eval with max_new_tokens=1536 (vs default 1024). Retry with correct model stack (Base+SFT+RSFT). If EDCR improves significantly (from 0.6609 toward 0.71+), truncation is the cause. If unchanged, distractor citation is genuine RSFT behavior. | — | — | — |\n\n## 待处理\n- mvp2_eval_rsft_s44: Full dev eval of RSFT seed=44 checkpoint. First MVP-2 judgement data point. Pass: rel_f1 > 0.4057 AND evi_f1 > 0.798 (SFT baseline).（准备中）\n\n## 近期结论\n- **mvp2_rsft_diagnosis** (success): RSFT failure root cause: rel_f1=0.0483 vs SFT 0.4057. Diagnose: training data distribution (relation count), step-170 checkpoint output analysis, SFT vs RSFT data comparison.\n- **mvp2_eval_ced_kl001_r4_last** (killed): —\n- **mvp2_grpo_ced_kl001_r3** (killed): kl_coef=0.01 (vs r5 kl_coef=0.0) prevents CED mode collapse while keeping QLoRA 4-bit compatible — answers whether KL regularization is necessary (retry: fix --lr + bash -c wrapping) ← 基于 mvp2_grpo_ced_kl001\n\n## 趋势\n成功 21 / 负向 11 / 失败 12 / 共 64\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nrtx5090-4x: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\n\n## 告警\n- mvp2_grpo_ced: 训练失败 — unknown\n- mvp2_grpo_flatnli: 训练失败 — unknown\n- mvp2_grpo_extract: 训练失败 — unknown\n- mvp2_sft_eval: 已被终止 — unknown\n- mvp2_grpo_ced_r1: 已被终止 — unknown\n- mvp2_grpo_ced_r2: 已被终止 — unknown\n- mvp2_grpo_ced_r3: 训练失败 — unknown\n- mvp2_grpo_ced_r4: 已被终止 — unknown\n- mvp2_grpo_extract_r2: 已被终止 — unknown\n- mvp2_grpo_flatnli_r2: 已被终止 — unknown\n- mvp2_grpo_flatnli_r3: 已被终止 — unknown\n- mvp2_grpo_ced_kl001: 训练失败 — unknown\n- mvp2_grpo_ced_kl001_r2: 已被终止 — unknown\n- mvp2_grpo_ced_kl001_r3: 已被终止 — unknown\n- mvp2_grpo_flatnli_r4: 已被终止 — unknown\n- mvp2_grpo_extract_r4: 已被终止 — unknown\n- mvp2_grpo_flatnli_r5: 已被终止 — unknown\n- mvp2_eval_ced_kl001_r4_multi: 已被终止 — unknown\n- mvp2_eval_ced_kl001_r4_last: 已被终止 — unknown\n- mvp2_eval_ced_kl001_r4_ckpt90: 已被终止 — unknown\n- mvp2_eval_ced_kl001_r4_high: 训练失败 — unknown\n- mvp2_grpo_ced_lr5e6_r1: 已被终止 — unknown\n- mvp2_grpo_ced_lr5e6_p1_r1: 已被终止 — unknown\n- mvp2_grpo_ced_lr5e6_rp_r1: 训练失败 — unknown\n- mvp2_eval_ced_kl001_r4_ckpt7080: 训练失败 — unknown\n- mvp2_grpo_ced_lr5e6_rp_r2: 已被终止 — unknown\n- mvp2_eval_lr5e6_r1_ckpt40: 训练失败 — unknown\n- mvp2_eval_lr5e6_rp_r2_ckpt20: 已被终止 — unknown\n- mvp2_eval_lr5e6_r1_ckpt60: 训练失败 — unknown\n- mvp2_rsft_generate: 训练失败 — unknown\n- mvp2_rsft_train_r2_fix: 已被终止 — unknown\n- mvp2_eval_rsft_\n\n## 研究想法\n# Idea Inbox\n\n## 待验证\n\n- [2026-05-14] **GRPO 遗忘缓解方案 A**：增大 KL 系数（0.001→0.04）+ 扩大 LoRA rank（r=4→r=16）+ 降低 lr 至 1e-6。文献调研表明 GRPO+QLoRA 低秩+低KL 是已知不稳定组合，这是最低成本的修复。\n- [2026-05-14] **GRPO 遗忘缓解方案 B**：分层 Reward 设计——将单一 reward 分解为 format_reward + entity_reward + relation_reward，消除 reward hacking 捷径。参考 RL-Struct (arXiv 2512.00319) 的层级约束方法。\n- [2026-05-14] **GRPO 遗忘缓解方案 C**：集成 Qwen 团队的 Online Merging Optimizer (arXiv 2405.17931)，在 GRPO 每步将 LoRA 更新方向锚定在 SFT 附近，训练中在线缓解 alignment tax。\n## ACTIVE"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "08dfff52-5a1f-427d-bf4a-fa1407c55bf7",
  "isSidechain": true,
  "promptId": "00a1eb94-0484-4e13-931d-e659507bc0c6",
  "agentId": "a9bd4203964701927",
  "type": "user",
  "uuid": "0288d37e-fcff-4d5c-8f9a-06ddcd08790f",
  "sourceToolAssistantUUID": "08dfff52-5a1f-427d-bf4a-fa1407c55bf7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-15T12:47:24.885Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01E2votVPTFR1BwAQ7crq61k`</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0288d37e-fcff-4d5c-8f9a-06ddcd08790f",
  "isSidechain": true,
  "agentId": "a9bd4203964701927",
  "requestId": "req_011Cb4NxnyhcwFEgiDZBdxws",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b41265c3-786e-4bc6-a665-12217da49bac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013vim2fZW6iLmU5PShteARX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15490,
      "output_tokens": 160,
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
          "output_tokens": 160,
          "cache_read_input_tokens": 15490,
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

_source line 9 · 2026-05-15T12:47:24.894Z_

<details><summary>↩ Tool result · `toolu_01E2votVPTFR1BwAQ7crq61k`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/report.md\", \"content\": \"# Handover — 2026-05-15\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| mvp2_rsft_ced_scoring_topk3_r2 | CED scoring ablation: top_k=3 (vs top_k=1). More training data (~8000 samples) vs stricter selection (2718 samples). Retry with HF_HUB_OFFLINE=1 (NLI model cached locally). | — | — | — |\\n| mvp2_rsft_ced_scoring_topk3 | CED scoring ablation: top_k=3 (vs top_k=1). More training data (~8000 samples) vs stricter selection (2718 samples). Answers: does CED filtering strictness affect RSFT training quality? | — | — | — |\\n| mvp2_eval_rsft_r2b_maxtok1536_r2 | Truncation diagnosis: r2b eval with max_new_tokens=1536 (vs default 1024). Retry with correct model stack (Base+SFT+RSFT). If EDCR improves significantly (from 0.6609 toward 0.71+), truncation is the cause. If unchanged, distractor citation is genuine RSFT behavior. | — | — | — |\\n\\n## 待处理\\n- mvp2_eval_rsft_s44: Full dev eval of RSFT seed=44 checkpoint. First MVP-2 judgement data point. Pass: rel_f1 > 0.4057 AND evi_f1 > 0.798 (SFT baseline).（准备中）\\n\\n## 近期结论\\n- **mvp2_rsft_diagnosis** (success): RSFT failure root cause: rel_f1=0.0483 vs SFT 0.4057. Diagnose: training data distribution (relation count), step-170 checkpoint output analysis, SFT vs RSFT data comparison.\\n- **mvp2_eval_ced_kl001_r4_last** (killed): —\\n- **mvp2_grpo_ced_kl001_r3** (killed): kl_coef=0.01 (vs r5 kl_coef=0.0) prevents CED mode collapse while keeping QLoRA 4-bit compatible — answers whether KL regularization is necessary (retry: fix --lr + bash -c wrapping) ← 基于 mvp2_grpo_ced_kl001\\n\\n## 趋势\\n成功 21 / 负向 11 / 失败 12 / 共 64\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nrtx5090-4x: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\\n\\n## 告警\\n- mvp2_grpo_ced: 训练失败 — unknown\\n- mvp2_grpo_flatnli: 训练失败 — unknown\\n- mvp2_grpo_extract: 训练失败 — unknown\\n- mvp2_sft_eval: 已被终止 — unknown\\n- mvp2_grpo_ced_r1: 已被终止 — unknown\\n- mvp2_grpo_ced_r2: 已被终止 — unknown\\n- mvp2_grpo_ced_r3: 训练失败 — unknown\\n- mvp2_grpo_ced_r4: 已被终止 — unknown\\n- mvp2_grpo_extract_r2: 已被终止 — unknown\\n- mvp2_grpo_flatnli_r2: 已被终止 — unknown\\n- mvp2_grpo_flatnli_r3: 已被终止 — unknown\\n- mvp2_grpo_ced_kl001: 训练失败 — unknown\\n- mvp2_grpo_ced_kl001_r2: 已被终止 — unknown\\n- mvp2_grpo_ced_kl001_r3: 已被终止 — unknown\\n- mvp2_grpo_flatnli_r4: 已被终止 — unknown\\n- mvp2_grpo_extract_r4: 已被终止 — unknown\\n- mvp2_grpo_flatnli_r5: 已被终止 — unknown\\n- mvp2_eval_ced_kl001_r4_multi: 已被终止 — unknown\\n- mvp2_eval_ced_kl001_r4_last: 已被终止 — unknown\\n- mvp2_eval_ced_kl001_r4_ckpt90: 已被终止 — unknown\\n- mvp2_eval_ced_kl001_r4_high: 训练失败 — unknown\\n- mvp2_grpo_ced_lr5e6_r1: 已被终止 — unknown\\n- mvp2_grpo_ced_lr5e6_p1_r1: 已被终止 — unknown\\n- mvp2_grpo_ced_lr5e6_rp_r1: 训练失败 — unknown\\n- mvp2_eval_ced_kl001_r4_ckpt7080: 训练失败 — unknown\\n- mvp2_grpo_ced_lr5e6_rp_r2: 已被终止 — unknown\\n- mvp2_eval_lr5e6_r1_ckpt40: 训练失败 — unknown\\n- mvp2_eval_lr5e6_rp_r2_ckpt20: 已被终止 — unknown\\n- mvp2_eval_lr5e6_r1_ckpt60: 训练失败 — unknown\\n- mvp2_rsft_generate: 训练失败 — unknown\\n- mvp2_rsft_train_r2_fix: 已被终止 — unknown\\n- mvp2_eval_rsft_s43: 训练失败 — unknown\\n\", \"total_chars\": 3020, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b41265c3-786e-4bc6-a665-12217da49bac",
  "isSidechain": true,
  "promptId": "00a1eb94-0484-4e13-931d-e659507bc0c6",
  "agentId": "a9bd4203964701927",
  "type": "user",
  "uuid": "1396a717-a58c-45ce-b944-a3c52df03825",
  "sourceToolAssistantUUID": "b41265c3-786e-4bc6-a665-12217da49bac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-15T12:47:28.485Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01L2omGCnRUJkawSCmXkshuS`</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1396a717-a58c-45ce-b944-a3c52df03825",
  "isSidechain": true,
  "agentId": "a9bd4203964701927",
  "requestId": "req_011Cb4Ny2N7bW1Fu5fn83Dgh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eaa5266e-e6a7-4af3-a69f-0a83e6f256c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ph1vipSN96fCkc3AKDYwqn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4325,
      "cache_read_input_tokens": 16937,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4325,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 52,
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

_source line 11 · 2026-05-15T12:47:28.495Z_

<details><summary>↩ Tool result · `toolu_01L2omGCnRUJkawSCmXkshuS`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/paper_framing.md\", \"content\": \"# Paper Framing — FREIGE\\n\\n> **状态**: POST-MVP (MVP-1 + MVP-2 均 PASS，进入 Research 阶段)\\n> **最后更新**: 2026-05-15\\n\\n## Target Venue\\n\\n- Primary: **EMNLP 2026 Main** (ARR July cycle, ~July 15-25 → commit EMNLP Aug/Sep)\\n- Stretch: ARR May 25 (10 days, 极紧，仅在实验全部顺利时考虑)\\n- Fallback: AAAI 2027 (abstract July 25, paper Aug 1)\\n\\n## Core Insight\\n\\nLLM-based document-level IE 已逼近 encoder SOTA 的抽取精度，但零方法能生成可验证证据。朴素 NLI faithfulness reward 可被 entity-mentioning distractor 句子游戏——共享实体但不支持具体关系的句子仍获正面蕴含分数。\\n\\n**CED (Contrastive Evidence Discrimination)** 通过文档内 hard negative 对比，将 evidence 质量评估从\\\"是否蕴含\\\"升级为\\\"是否比最佳干扰句更蕴含\\\"——本质上是 evidence grounding 场景下的 **anti-reward-overoptimization mechanism**（连接 Gao et al. 2023 reward overoptimization 理论）。\\n\\n**MVP 关键发现**: CED 作为在线 RL (GRPO) reward 导致 catastrophic forgetting（3 种 reward type × 多个 lr 全线失败），但作为离线 RL (RSFT) 的候选筛选信号极其有效——4 组超参配置均稳定超过 SFT baseline。**方法论结论**: 对结构化 IE 任务，CED 应作为离线质量信号而非在线训练奖励。\\n\\n## Story Arc\\n\\n1. **Problem**: LLM DocRE 无证据 → 部署障碍（human-in-the-loop KB population、生物医学审计、RAG 溯源）\\n2. **Why naive reward fails**: flat-NLI 被 entity-sharing distractors 欺骗（SFT EDCR=71.2%，大量引用干扰句）\\n3. **Why online RL fails**: GRPO+CED/flat-NLI/extract-only 全部 catastrophic forgetting（reward ↑ + rel_f1 ↓ 至 <0.02）\\n4. **Solution**: CED 作为离线质量信号 + RSFT（rejection sampling fine-tuning）：SFT 模型生成 N 候选 → CED 打分筛选 → 微调，规避在线 RL 的遗忘风险\\n5. **Theoretical grounding**: 连接 LongRLVR (ICLR 2026) evidence grounding 梯度消失分析 + \\\"RSFT=PPO\\\" (ICML 2025) 等价性理论\\n6. **Result**: 首个 LLM-based DocRE 方法同时生成抽取和可验证证据\\n\\n## Core Claims\\n\\n### Claim 1 (Main): CED-scored RSFT 使 LLM 同时生成抽取和忠实证据\\n- FREIGE 是首个在 DocRED 上同时输出 (head, relation, tail, [evidence]) 的 LLM 方法\\n- RSFT+CED: rel_f1 +3.9~6.0pp over SFT, evi_f1 +1.1~2.1pp, EDCR -4.8~7.7pp\\n- **MVP-2 已验证**: 4/4 configs PASS\\n- **Research 需要**: test set 评估，DREEAM/SAIS Evi-F1 直接对比\\n\\n### Claim 2 (Ablation): CED scoring 优于 flat-NLI scoring 用于 RSFT\\n- CED-filtered RSFT vs flat-NLI-filtered RSFT 的 evi_f1 和 EDCR 差异\\n- CED 的对比性 margin 过滤掉 distractor-heavy 候选\\n- **Research 需要**: flat-NLI scored RSFT ablation（核心实验）\\n\\n### Claim 3 (Analysis): 在线 RL 在结构化 IE 上 catastrophically forget\\n- GRPO+QLoRA 在 3 种 reward type × 多个 lr 下全线失败\\n- 关键对比: evi_f1 在 GRPO 下提升至 0.850（>SFT 0.798）但 rel_f1 崩至 <0.02——CED 驱动了 evidence 学习但在线 RL 摧毁了抽取能力\\n- RSFT 规避此问题：不修改 policy gradient，只筛选训练数据\\n- **MVP 已有完整证据**: D031/D033 GRPO 判死，D039 RSFT 成功\\n\\n### Claim 4 (Evaluation): EDCR 作为独立评估指标\\n- EDCR = |entity-sharing non-gold cited sentences| / |total cited sentences|\\n- Evi-F1 盲区：不惩罚 plausible-looking distractor citations\\n- SFT EDCR=71.2%, RSFT+CED EDCR=63.5~66.4%（方向正确但差距有限，需坦诚讨论）\\n- **Research 需要**: cross-method diagnostic table, CED vs flat-NLI EDCR 对比\\n\\n## MVP Evidence Summary\\n\\n| Config | rel_f1 | Δ rel_f1 | evi_f1 | EDCR | 状态 |\\n|--------|--------|----------|--------|------|------|\\n| SFT baseline | 0.4057 | — | 0.7979 | 0.7118 | ✅ |\\n| RSFT r1 (3ep, α=128, s42) | 0.4449 | +3.92pp | 0.8187 | 0.6565 | ✅ |\\n| RSFT r1 (s44) | 0.4655 | +5.98pp | 0.8087 | 0.6350 | ✅ |\\n| RSFT r2a (1ep, α=128) | 0.4494 | +4.37pp | 0.8108 | 0.6641 | ✅ |\\n| RSFT r2b (1ep, α=32, lr=1e-5) | 0.4493 | +4.36pp | 0.8128 | 0.6609 | ✅ |\\n| GRPO best (lr=5e-5, ckpt-90) | 0.2110 | -19.5pp | 0.5750 | — | ❌ |\\n| GRPO best (lr=5e-6, ckpt-100) | 0.0138 | -39.2pp | 0.8500 | 0.9900 | ❌ |\\n\\n## Anticipated Reviewer Concerns\\n\\n### RC1: NLI reward 信号质量（高概率攻击）\\n- **攻击**: \\\"DeBERTa-v3-base 的 NLI 判断有 lexical overlap bias，CED 训练信号有噪声\\\"\\n- **已验证**: MVP-1 Pearson r=0.34（NLI vs lexical overlap），远低于 0.7，证明非捷径\\n- **Research 补充**: DeBERTa-base vs DeBERTa-large 对比\\n\\n### RC2: Gold evidence 标注不完整导致 false distractor\\n- **攻击**: \\\"被标为 distractor 的句子可能是 annotator 遗漏的有效证据\\\"\\n- **应对**: CED margin 的 self-correcting property——如果 false distractor 真正蕴含关系，其 p_neg 高 → margin 小 → 惩罚弱\\n- **Research 补充**: false-distractor 鲁棒性量化分析\\n\\n### RC3: 评测可比性\\n- **攻击**: \\\"生成式 evidence 如何与 DREEAM 的 attention-based evidence 做 apple-to-apple 对比？\\\"\\n- **应对**: 模型输出显式句子索引 [S_i]，直接映射句子级 Evi-F1；辅助指标用 RoBERTa-large-MNLI（非训练用 DeBERTa）避免 circular evaluation\\n\\n### RC4: 单数据集 + 单模型泛化性\\n- **攻击**: \\\"只在 DocRED + Qwen3-4B 上验证\\\"\\n- **Research**: Re-DocRED 扩展 + Qwen3-1.7B/8B model size ablation\\n\\n### RC5: RSFT vs GRPO 是否公平对比\\n- **攻击**: \\\"GRPO 失败可能是超参问题而非方法论问题\\\"\\n- **应对**: 完整 GRPO 轨迹——3 种 reward × 多个 lr × 全 checkpoint eval；D020 控制变量下 CED 是唯一存活的 reward type\\n\\n### RC6: EDCR 63-66% 仍然偏高，CED 对证据精确度提升有限\\n- **攻击**: \\\"RSFT+CED 的 EDCR 只比 SFT 低 5-8pp，证据质量提升不够显著\\\"\\n- **应对**: (1) CED 在 RSFT 中是间接作用（筛选训练数据），非直接 reward；(2) CED-as-reranker 可能更直接降低 EDCR；(3) 需要 flat-NLI RSFT 对比证明 CED 方向正确\\n- **Research**: CED reranker PoC（运行中），top_k ablation\\n\\n### RC7: 方法过于简单\\n- **应对**: 简洁是优点——RSFT 方法论已被证明理论等价于 PPO (ICML 2025)，CED 创新在于打分函数设计而非框架复杂度\\n\\n## Key Baselines (8+)\\n\\n1. **SFT-only**: Qwen3-4B + LoRA SFT on DocRED gold — 无 RL\\n2. **RSFT flat-NLI**: flat-NLI scored RSFT — 无 contrastive signal（核心 ablation）\\n3. **RSFT CED (FREIGE)**: CED scored RSFT — 主方法\\n4. **CED-as-reranker**: 推理时 CED 重排 SFT 候选（无训练）— 运行中\\n5. **GRPO+CED**: 在线 RL with CED reward — negative baseline\\n6. **DREEAM**: RoBERTa-large encoder — evidence SOTA (Evi-F1 57.34)\\n7. **SAIS**: RoBERTa encoder — evidence baseline (Evi-F1 55.67)\\n8. **DocKS-RAG**: GNN+RAG — extraction SOTA (F1 63.59, 无 evidence)\\n9. **LMRC**: LLaMA3.1-8B — generative LLM SOTA (F1 60.69, 无 evidence)\\n\\n## Publishability Threshold\\n\\n- **必要条件**: RSFT+CED 在 test set 上 Evi-F1 > DREEAM 57.34 AND rel_f1 显著 > SFT baseline\\n- **充分条件**: 上述 + CED vs flat-NLI RSFT Evi-F1/EDCR 差异显著 + GRPO 分析完整\\n- **Failure pivot**: Evi-F1 < 57.34 on test set → 转为 analysis contribution（在线 vs 离线 RL for structured IE）\\n\\n## Research Phase Priorities\\n\\n| Priority | 实验 | Claim | 预估 GPU-hours |\\n|----------|------|-------|---------------|\\n| P0 | CED vs flat-NLI RSFT ablation | C2 | ~20h |\\n| P0 | Test set evaluation (RSFT best config) | C1 | ~4h |\\n| P0 | EDCR pipeline 验证 + cross-method table | C4 | ~2h |\\n| P0 | DREEAM/SAIS Evi-F1 baseline reproduction | C1 | ~8h |\\n| P1 | CED-as-reranker (running) | C1 bonus | ~6h |\\n| P1 | Model size ablation (1.7B/8B) | RC4 | ~24h |\\n| P1 | Re-DocRED extension | RC4 | ~12h |\\n| P1 | top_k ablation (k=1 vs k=3) | RC6 | ~8h |\\n| P2 | GRPO forgetting 详细分析 + 可视化 | C3 | ~4h |\\n| P2 | DeBERTa-base vs large NLI 对比 | RC1 | ~4h |\\n\", \"total_chars\": 6099, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eaa5266e-e6a7-4af3-a69f-0a83e6f256c8",
  "isSidechain": true,
  "promptId": "00a1eb94-0484-4e13-931d-e659507bc0c6",
  "agentId": "a9bd4203964701927",
  "type": "user",
  "uuid": "d2b715a2-a35a-4f7e-9412-ff2feb4aade5",
  "sourceToolAssistantUUID": "eaa5266e-e6a7-4af3-a69f-0a83e6f256c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T12:47:29.424Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01RvKJPijz8dPSAsswuo89yq`</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2b715a2-a35a-4f7e-9412-ff2feb4aade5",
  "isSidechain": true,
  "agentId": "a9bd4203964701927",
  "requestId": "req_011Cb4Ny2N7bW1Fu5fn83Dgh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "72331445-dc3c-4d94-892f-05055ea85184",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ph1vipSN96fCkc3AKDYwqn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4325,
      "cache_read_input_tokens": 16937,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4325,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 52,
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

_source line 13 · 2026-05-15T12:47:29.434Z_

<details><summary>↩ Tool result · `toolu_01RvKJPijz8dPSAsswuo89yq`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ideas.md\", \"content\": \"# Idea Inbox\\n\\n## 待验证\\n\\n- [2026-05-14] **GRPO 遗忘缓解方案 A**：增大 KL 系数（0.001→0.04）+ 扩大 LoRA rank（r=4→r=16）+ 降低 lr 至 1e-6。文献调研表明 GRPO+QLoRA 低秩+低KL 是已知不稳定组合，这是最低成本的修复。\\n- [2026-05-14] **GRPO 遗忘缓解方案 B**：分层 Reward 设计——将单一 reward 分解为 format_reward + entity_reward + relation_reward，消除 reward hacking 捷径。参考 RL-Struct (arXiv 2512.00319) 的层级约束方法。\\n- [2026-05-14] **GRPO 遗忘缓解方案 C**：集成 Qwen 团队的 Online Merging Optimizer (arXiv 2405.17931)，在 GRPO 每步将 LoRA 更新方向锚定在 SFT 附近，训练中在线缓解 alignment tax。\\n## ACTIVE\\n\", \"total_chars\": 484, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "72331445-dc3c-4d94-892f-05055ea85184",
  "isSidechain": true,
  "promptId": "00a1eb94-0484-4e13-931d-e659507bc0c6",
  "agentId": "a9bd4203964701927",
  "type": "user",
  "uuid": "be8fcbcf-ac1a-495b-82f8-463d85e61ecd",
  "sourceToolAssistantUUID": "72331445-dc3c-4d94-892f-05055ea85184",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T12:47:29.876Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_012uci9mFREXNJfdhf2SGF3b`</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be8fcbcf-ac1a-495b-82f8-463d85e61ecd",
  "isSidechain": true,
  "agentId": "a9bd4203964701927",
  "requestId": "req_011Cb4Ny2N7bW1Fu5fn83Dgh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "63700f17-4f6e-42b3-b32e-0ee6bfae12ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ph1vipSN96fCkc3AKDYwqn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4325,
      "cache_read_input_tokens": 16937,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4325,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 52,
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

_source line 15 · 2026-05-15T12:47:29.886Z_

<details><summary>↩ Tool result · `toolu_012uci9mFREXNJfdhf2SGF3b`</summary>

````text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/memory.md\", \"content\": \"# 文献调研：GRPO/RLHF 训练中的\\\"先遗忘后恢复\\\"现象\\n\\n日期：2026-05-14\\n\\n## 背景\\n\\nQwen3-4B + GRPO + QLoRA 4-bit 训练文档级关系抽取，观察到：\\n- Reward 上升但 eval rel_F1 崩塌（ckpt-20: 0.0077 vs SFT baseline 0.406）\\n- lr=5e-5 和 lr=5e-6 下都出现\\n- 存在\\\"先遗忘后缓慢恢复\\\"的 U 型曲线（step-10=0.003 → step-90=0.211），但恢复不足\\n\\n---\\n\\n## 论文 1：Mitigating the Alignment Tax of RLHF\\n\\n- **作者**：Yifei Lin, Yuxin Tan, et al.\\n- **年份/Venue**：2024, EMNLP 2024\\n- **arXiv**：2309.06256\\n\\n### 核心发现\\n- 定义了\\\"alignment tax\\\"：RLHF 对齐后模型遗忘预训练/SFT 阶段习得能力的现象\\n- 发现简单的**模型参数平均**（插值 SFT 和 RLHF 后模型权重）在 alignment-forgetting Pareto 前沿上表现最优\\n- 提出 **Heterogeneous Model Averaging (HMA)**：对不同层使用不同插值比例\\n\\n### 与我们场景的相关性\\n- **直接相关**。GRPO 阶段的 rel_F1 崩塌是 alignment tax 的典型表现\\n- HMA 的层级插值思路可直接应用于 QLoRA adapter 权重（但 GRPO 路线已判死，仅留作参考）\\n\\n---\\n\\n## 论文 2：Online Merging Optimizers for Boosting Rewards and Mitigating Tax in Alignment\\n\\n- **作者**：Lu et al. (Qwen 团队)\\n- **年份/Venue**：2024, arXiv 2405.17931\\n- **开源**：github.com/QwenLM/online_merging_optimizers\\n\\n### 核心发现\\n- 在 RLHF 每个优化步骤中实时合并 RL policy 和 SFT 模型参数\\n- 在 Qwen 和 LLaMA 系列上验证有效\\n\\n### 与我们场景的相关性\\n- 高度相关但 GRPO 路线已判死，仅留作参考\\n\\n---\\n\\n## D031 Pivot: GRPO+QLoRA → RSFT + CED (2026-05-15)\\n\\n### 决策\\nGRPO+QLoRA 方向判死，pivot 到 Rejection Sampling Fine-Tuning (RSFT) + CED scoring。\\n\\n### 核心证据\\n- lr=5e-5 (ced_kl001_r4): best eval rel_f1=0.211 (step-90)，仅 SFT baseline (0.406) 的 52%\\n- lr=5e-6 (lr5e6_r1): 完整轨迹 ckpt-20→100 rel_f1 = 0.008/0.007/0.009/0.012/0.014 — 零恢复\\n- 所有 3 种 reward type (CED/extract-only/flat-NLI) 在 GRPO+QLoRA 下均 collapse\\n\\n### RSFT 技术约束\\n- **--quantize (4-bit) + merge_and_unload 在 RTX 5090 上有 CUBLAS 错误**，RSFT 训练不要用 quantize。bf16 Qwen3-4B 仅 ~8GB，无需量化。\\n- 运行目录必须是 `/root/autodl-tmp/`（freige 不是 pip install 的包，cd 到 freige/ 子目录会导致 import 找到内层空包）\\n\\n---\\n\\n## D038 重大修正：RSFT r1 实际成功 (2026-05-15)\\n\\n### 事件\\nD037 报告 RSFT r1 \\\"灾难性失败\\\"（rel_f1=0.0483），但这是 **TaskEvalCallback bug**——`--eval_max_docs 50` 评估 50 个 doc 的预测，却用全部 12275 个 gold triples 计算 F1，严重低估 rel_f1。\\n\\n### 真实结果\\ns44 全量 dev eval (985 docs): **rel_f1=0.4655 (+5.98pp), evi_f1=0.8087 (+1.08pp)** → MVP-2 PASS\\n\\n### TaskEvalCallback bug fix\\n已部署到 `rsft_trainer.py:118-120`。gold triples 现在过滤到 eval_max_docs 对应的文档子集。\\n\\n### 教训\\n- 在 callback 中用 subset eval 时，必须确保 gold 和 pred 在同一文档集合上计算\\n- 基于 callback 数字的任何结论都需要全量 eval 交叉验证\\n\\n---\\n\\n## ~~RSFT r1 灾难性失败根因~~ [D038 撤回]\\n\\n**以下分析基于 D037 的错误 rel_f1=0.0483。D038 确认该数字是 eval bug，实际 rel_f1=0.4655。**\\n\\n原分析中关于\\\"关系本体崩塌\\\"的观察可能来自 eval_max_docs=50 下的极小样本偏差，不代表模型真实行为。r1/s43/s44 的全量 eval 正在进行中，将给出真实 ablation 数据。\\n\\n---\\n\\n## RSFT r2a/r2b ablation 结果 (2026-05-15)\\n\\n### 实验配置与结果\\n\\n| 配置 | rel_f1 | evi_f1 | edcr | Δrel_f1 |\\n|------|--------|--------|------|---------|\\n| SFT baseline | 0.4057 | 0.7979 | 0.7118 | — |\\n| r1 (3ep, α=128, lr=2e-5, 2718) | 0.4449 | **0.8187** | 0.6565 | +3.92pp |\\n| r2a (1ep, α=128, lr=2e-5, clean 2548) | **0.4494** | 0.8108 | 0.6641 | +4.37pp |\\n| r2b (1ep, α=32, lr=1e-5, clean 2548) | 0.4493 | 0.8128 | 0.6609 | +4.36pp |\\n\\n### Ablation 结论\\n1. **1 epoch ≈ 3 epoch on rel_f1**（r2a=0.4494 vs r1=0.4449），多 epoch 无额外收益\\n2. **LoRA scaling 不敏感**（α=128 vs α=32 差异 <0.1pp）\\n3. **r1 在 evi_f1 上最优**（0.8187 vs r2a 0.8108），3 epoch 可能有助于证据定位\\n4. **所有 RSFT 变体 EDCR 低于 SFT**（~0.66 vs 0.71），RSFT 增加 pred_count 导致更多 distractor citation\\n\\n---\\n\\n## RSFT 文献对标 (2026-05-15, 更新)\\n\\n### 直接竞争者：无\\n在 DocRE / IE 上**无人用过 RSFT**，NLI-based CED reward for RE training 也无先例。Novelty 完全成立。\\n\\n### 最接近竞争者：R1-RE (arXiv 2507.04642)\\n用 GRPO 做**句子级** RE。与我们差异明确：文档级 vs 句子级、offline RSFT vs online GRPO、有 CED evidence reward vs 无。\\n\\n### Must-cite 论文\\n1. **R1-RE** — GRPO for sentence-level RE（最近竞争者，需在 related work 中区分）\\n2. **\\\"Minimalist Approach\\\"** — RSFT 理论基础\\n3. **RelPrior** — LLM-based DocRE baseline (+2.06-2.38pp rel_f1)\\n4. **\\\"RSFT=PPO\\\" (ICML 2025)** — RSFT 与 PPO 等价性理论\\n\\n### 我们的定位\\n- +3.9~6.0pp rel_f1 显著超过同类 LLM-based DocRE 改进（RelPrior: +2.06-2.38pp）\\n- CED 作为 rejection sampling 打分函数是新颖的方法论贡献\\n- 最接近的工作是 Progressive Self-distillation (ACM 2024) 用 knowledge distillation，但无 evidence-based reward\\n\\n### 新增文献 map categories (by literature scan worker)\\n- Category 6: RSFT Methodology & Theory（3 篇）\\n- Category 7: RL for Information Extraction（5 篇）\\n- Category 8: Recent LLM-based DocRE Methods（5 篇）\\n\\n---\\n\\n## CED-as-reranker 探索 (2026-05-15)\\n\\nRSFT 成功后仍保留 CED-as-reranker PoC 作为推理时替代方案（无需额外训练）。\\ncuda:0 上 PID 178050 运行中（985 docs × N=8，预计 ~6h）。\\n如果 reranker 接近或超过 RSFT，可作为论文中的 complementary contribution。\\n\\n---\\n\\n## Qwen3 generation_config 覆盖陷阱 (2026-05-15)\\n\\nQwen3 模型自带 `generation_config.json` 会静默覆盖代码传参：\\n- `model.generation_config.top_k = 20`（限制采样池）\\n- `model.generation_config.temperature = 0.6`（覆盖代码传的任何温度值）\\n\\n**必须在生成前显式覆盖**：\\n```python\\nmodel.generation_config.temperature = target_temp\\nmodel.generation_config.top_k = 0  # 禁用 top_k 限制\\nmodel.generation_config.do_sample = True\\n```\\n\\n---\\n\\n## Diversity 监控计算 bug (2026-05-15)\\n\\n### 根因\\n- triple-set 归一化逻辑不一致\\n- diversity 分母用配置值而非实际生成数\\n\\n### 修复\\n- 提取 `diversity_metrics.py` 独立模块\\n- 修复后真实数据：302 docs mean_diversity=7.52/8, median=8.0/8\\n\\n---\\n\\n## inference.py 参数教训 (2026-05-15)\\n\\n**inference.py 必须传完整模型 stack**：\\n- `--base_model /root/autodl-tmp/models/Qwen3-4B`\\n- `--sft_adapter /root/autodl-tmp/sft_output`\\n- `--model_path &lt;rsft_adapter_path>`（RSFT adapter）\\n- `--data_path /root/autodl-tmp/data/docred`\\n- `--output_dir &lt;output_path>`\\n- `--no-quantize`（RTX 5090 必须）\\n- `--max_new_tokens &lt;N>`（可选，默认 1024）\\n\\n**只传 --model_path 不传 --base_model + --sft_adapter 会导致模型 stack 错误**（Base + RSFT LoRA，缺 SFT merge），结果完全不可用。maxtok1536 eval 因此被 Reviewer CRITICAL 打回并重跑。\\n\\n---\\n\\n## RSFT 代码参数速查\\n\\n**inference.py**: --base_model, --sft_adapter, --model_path(rsft adapter), --data_path, --output_dir, --no-quantize, --max_new_tokens(1024)\\n\\n**rsft_generate.py**: --base_model, --sft_adapter, --data_path, --split, --output_dir, --num_generations(8), --temperature(0.7), --batch_size(1), --max_new_tokens(1024), --seed, --quantize/--no-quantize, --start_idx, --end_idx, --shard_id\\n\\n**rsft_score_filter.py**: --input_dir, --output_path, --nli_model_path, --nli_device, --tau(0.5), --f1_threshold(0.1), --selection_strategy(top_k), --top_k(2)\\n\\n**rsft_trainer.py**: --base_model, --sft_adapter, --rsft_data_path, --output_dir, --learning_rate, --num_epochs, --per_device_batch_size, --gradient_accumulation_steps, --lora_rank(64), --lora_alpha(128), --weighted_sampling, --quantize(False), --eval_data_dir, --eval_max_docs, --wandb_run_name, --seed\", \"total_chars\": 6195, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "63700f17-4f6e-42b3-b32e-0ee6bfae12ea",
  "isSidechain": true,
  "promptId": "00a1eb94-0484-4e13-931d-e659507bc0c6",
  "agentId": "a9bd4203964701927",
  "type": "user",
  "uuid": "f63299b9-360e-4d75-a056-bb394d503e9c",
  "sourceToolAssistantUUID": "63700f17-4f6e-42b3-b32e-0ee6bfae12ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-15T12:47:30.496Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0166wWndWJAF8jXLY8S7c1ap`</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f63299b9-360e-4d75-a056-bb394d503e9c",
  "isSidechain": true,
  "agentId": "a9bd4203964701927",
  "requestId": "req_011Cb4Ny2N7bW1Fu5fn83Dgh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "21a42822-1cd2-41ca-8569-dae27362bfe3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ph1vipSN96fCkc3AKDYwqn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4325,
      "cache_read_input_tokens": 16937,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4325,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 52,
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

_source line 17 · 2026-05-15T12:47:30.512Z_

<details><summary>↩ Tool result · `toolu_0166wWndWJAF8jXLY8S7c1ap`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md\", \"content\": \"# faith-evidence-ie — Research Dashboard\\n\\n> 最后更新: 2026-05-15 12:03 UTC | 更新原因: Post-MVP kickoff: complete_mvp() 完成，paper_framing.md + experiment_plan.yaml 已写，dream_simulate 已启动\\n\\n## 核心方向\\nFREIGE: 用 CED (Contrastive Evidence Discrimination) 作为离线质量信号，通过 RSFT (Rejection Sampling Fine-Tuning) 训练 LLM 在文档级关系抽取中同时生成抽取结果和可验证证据。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research（MVP 2026-05-15 通过，complete_mvp() 已调用）\\n- **MVP-1** ✅ CED signal: margin=0.4827, acc=81.5%, r=0.34\\n- **MVP-2** ✅ RSFT+CED: 4/4 configs PASS (rel_f1 +3.9~6.0pp, evi_f1 +1.1~2.1pp, EDCR -4.8~7.7pp vs SFT)\\n- **GRPO 判死** (D031/D033): 3 种 reward × 多 lr 全线 catastrophic forgetting\\n- **Paper framing**: POST-MVP, Core Claims 4 条 (详见 paper_framing.md)\\n- **Experiment plan**: 10 个研究实验 + 4 个 MVP 已完成 (详见 experiment_plan.yaml)\\n- **Dream 模拟**: dream_20260515T120227 运行中 (full review mode)\\n- **覆盖率**: P0 实验 4 个（0/4 完成），等 Dream 回调后批准启动\\n\\n## 投稿目标\\n- Primary: **EMNLP 2026 Main** (ARR July cycle)\\n- Stretch: ARR May 25（极紧，仅在实验全部顺利时考虑）\\n- Fallback: AAAI 2027 (Aug 1)\\n\\n## 近期任务\\n- [ ] 等待 Dream 模拟完成，按回调行动指令处理\\n- [ ] Dream 达标后批准 P0 实验启动\\n- [ ] plan_001: CED vs flat-NLI RSFT ablation (Claim 2 核心)\\n- [ ] plan_002: Test set evaluation\\n- [ ] plan_003: EDCR cross-method diagnostic table\\n- [ ] plan_004: DREEAM baseline reproduction\\n- [ ] 处理 3 个运行中实验结果 (maxtok1536 eval, s43 eval, CED reranker)\\n\\n## GPU 分配（2026-05-15 实况）\\n\\n| GPU | 状态 | 任务 |\\n|-----|------|------|\\n| cuda:0 | 🏃 | mvp2_ced_reranker_poc (plan_005) |\\n| cuda:1 | 🏃 | mvp2_eval_rsft_r2b_maxtok1536 (truncation 诊断) |\\n| cuda:2 | 🏃 | mvp2_eval_rsft_s43_r2 (第 3 seed 方差) |\\n| cuda:3 | ⏳ | 待分配（Dream 完成后派 P0 实验） |\\n\\n## GPU 预算\\n- 硬件: 4× RTX 5090 32GB (rtx5090-4x)\\n- MVP 已消耗: ~80+ GPU-hours (GRPO ~60h + RSFT ~20h)\\n- Research P0 预估: ~34h\\n- Research P1 预估: ~50h\\n- Research P2 预估: ~12h\\n- 总预算充裕\\n\\n## 评审笔记（原始，Research 阶段逐条处理）\\n1. ✅ CED 重框定为 anti-reward-overoptimization mechanism（paper_framing.md 已体现）\\n2. ✅ EDCR 升格为独立评估贡献 (Claim 4)\\n3. ✅ NLI lexical overlap bias → MVP-1 验证 r=0.34\\n4. ⬜ Evidence 评测 apple-to-apple 对齐（RC3，Research 阶段实现）\\n5. ⬜ Baselines 扩展到 6+（已规划 8+ baselines）\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D040 | 2026-05-15 | D040: MVP 正式通过 → 进入 Research 阶段。paper_framing.md 定 | mvp2_eval_rsft_r2a, mvp2_eval_rsft_r2b, mvp2_eval_rsft_r1, mvp2_rsft_train_r1_s44 |\\n| D039 | 2026-05-15 | D039: RSFT+CED ablation 全部 PASS MVP-2——方法鲁棒，1 epoc | mvp2_eval_rsft_r2a, mvp2_eval_rsft_r2b, mvp2_eval_rsft_r1, mvp2_rsft_train_r1_s44 |\\n| D038 | 2026-05-15 | D038: 撤回 D037——RSFT \\\"灾难性失败\\\"实为 eval bug（50-doc pred | mvp2_rsft_train_r1_s44, mvp2_rsft_train_r1 |\\n| D037 | 2026-05-15 | D037: RSFT 全线 FAIL（rel_f1=0.0483），pivot 到 CED-as-r | mvp2_rsft_train_r1, mvp2_rsft_train_r1_s43, mvp2_rsft_train_r1_s44 |\\n| D036 | 2026-05-15 | D034 撤销：diversity crisis 是监控 bug，非生成质量问题，T=0.7 下 d | mvp2_rsft_generate |\\n| D035 | 2026-05-15 | 暂停 RSFT 并行化：Reviewer critical 发现 diversity=1.0/8 是 | mvp2_diversity_probe, mvp2_rsft_generate |\\n| D034 | 2026-05-15 | D034: RSFT diversity 危机——diversity=1.0/8 因 tempera | mvp2_rsft_generate, mvp2_diversity_probe |\\n| D033 | 2026-05-15 | D031 最终确认：GRPO+QLoRA 全线 FAIL，lr5e6 全 6 checkpoint  | mvp2_eval_lr5e6_r1_ckpt100, mvp2_eval_lr5e6_r1_ckpt80, mvp2_eval_lr5e6_r1_ckpt60, mvp2_eval_lr5e6_r1_ckpt40, mvp2_eval_lr5e6_r1_ckpt20, mvp2_grpo_ced_lr5e6_r1 |\\n| D032 | 2026-05-15 | Kill GRPO 训练 (cuda:0 step 113/200): 轨迹数据已充分，释放 GPU | mvp2_grpo_ced_lr5e6_r1, mvp2_eval_lr5e6_r1_ckpt80 |\\n| D031 | 2026-05-14 | GRPO+QLoRA P0 方向判死：ckpt-40 rel_f1=0.0071（比 ckpt-20 | mvp2_eval_lr5e6_r1_ckpt40_r2, mvp2_eval_lr5e6_r1_ckpt20, mvp2_grpo_ced_lr5e6_r1, ced_kl001_r4 |\\n\\n\", \"total_chars\": 3570, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "21a42822-1cd2-41ca-8569-dae27362bfe3",
  "isSidechain": true,
  "promptId": "00a1eb94-0484-4e13-931d-e659507bc0c6",
  "agentId": "a9bd4203964701927",
  "type": "user",
  "uuid": "e4d5bfa7-049e-49fb-b1e0-4485275527ea",
  "sourceToolAssistantUUID": "21a42822-1cd2-41ca-8569-dae27362bfe3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-15T12:47:33.733Z_

Now let me look at the paper artifacts and literature map for a more complete picture.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4d5bfa7-049e-49fb-b1e0-4485275527ea",
  "isSidechain": true,
  "agentId": "a9bd4203964701927",
  "requestId": "req_011Cb4NySfMGvnmM4qtUE8VB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7d465772-47d9-4e16-8ccd-be3aaff74de9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YcRPc8eqRu572amtXTuUYh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11064,
      "cache_read_input_tokens": 21262,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11064,
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

_source line 19 · 2026-05-15T12:47:34.632Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0151nZ71dhhWYNFHsutpYtdY`</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d465772-47d9-4e16-8ccd-be3aaff74de9",
  "isSidechain": true,
  "agentId": "a9bd4203964701927",
  "requestId": "req_011Cb4NySfMGvnmM4qtUE8VB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "991f6aa7-108e-487f-a406-8213a86c626f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YcRPc8eqRu572amtXTuUYh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11064,
      "cache_read_input_tokens": 21262,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11064,
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

_source line 20 · 2026-05-15T12:47:34.651Z_

<details><summary>↩ Tool result · `toolu_0151nZ71dhhWYNFHsutpYtdY`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml\", \"content\": \"# Literature Map for faith-evidence-ie (FREIGE)\\n# Focus: CED-as-training-stabilizer (D024) + RSFT for DocRE\\n# Updated: 2026-05-15\\n\\npapers:\\n\\n  # === Category 1: Reward Diversity / Reward Shaping for RL Stability ===\\n\\n  - title: \\\"GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization\\\"\\n    authors: NVIDIA Labs\\n    year: 2025\\n    venue: ICML 2026\\n    url: https://arxiv.org/abs/2601.05242\\n    category: reward_diversity\\n    role: closest_prior_work\\n    key_finding: >\\n      直接将 GRPO 应用于多 reward 组合时，不同 rollout 的 reward 组合在归一化后 collapse 为相同 advantage 值，\\n      降低训练信号分辨率导致收敛失败。GDPO 对每个 reward 独立做 group-wise normalization 再聚合，\\n      保留多 reward 的相对差异，显著提升训练稳定性。\\n    relevance_to_ced_stabilizer: >\\n      最直接相关。CED reward 本质上引入了独立于 extraction F1 的 reward 维度（evidence quality），\\n      GDPO 的理论分析解释了为什么多维 reward 比单一 reward 更稳定——独立 reward 维度防止 advantage collapse。\\n      但 GDPO 是方法论贡献，CED 是 task-specific reward 设计自然具备了这一特性。\\n\\n  - title: \\\"DRA-GRPO: Exploring Diversity-Aware Reward Adjustment for R1-Zero-Like Training of LLMs\\\"\\n    authors: Xiwen Chen et al.\\n    year: 2025\\n    venue: arXiv 2505.09655\\n    url: https://arxiv.org/abs/2505.09655\\n    category: reward_diversity\\n    role: related_method\\n    key_finding: >\\n      GRPO 的标量 reward 无法区分语义多样但得分相同的输出（diversity-quality inconsistency）。\\n      DRA 用子模互信息（SMI）对 reward 加权，给多样性高的 completion 更大权重，\\n      等价于 Inverse Propensity Scoring 去偏，防止 policy 坍缩到先验模式。\\n    relevance_to_ced_stabilizer: >\\n      DRA 通过后处理 reward 注入多样性信号；CED 的 reward 本身就内含对比结构自然提供 diversity 信号。\\n      机制互补但来源不同——CED 是 reward design 层面，DRA 是 optimization 层面。\\n\\n  - title: \\\"Shrinking the Variance: Shrinkage Baselines for RL with Verifiable Rewards\\\"\\n    authors: Guanning Zeng et al.\\n    year: 2025\\n    venue: arXiv 2511.03710\\n    url: https://arxiv.org/abs/2511.03710\\n    category: reward_diversity\\n    role: theoretical_support\\n    key_finding: >\\n      RLVR 中 per-prompt 均值 baseline 在低 generation 数下估计不准导致高 variance 梯度。\\n      用 James-Stein shrinkage 混合 per-prompt 和 cross-prompt 均值，\\n      构造可证明更低 variance 的 policy gradient estimator。\\n    relevance_to_ced_stabilizer: >\\n      理论支持：reward variance 对 gradient estimation 质量至关重要。\\n      CED 的额外 reward 维度提供更丰富的 per-group variance，间接起到 variance 维持效果。\\n\\n  - title: \\\"Reward Shaping to Mitigate Reward Hacking in RLHF\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: arXiv 2502.18770\\n    url: https://arxiv.org/abs/2502.18770\\n    category: reward_diversity\\n    role: background\\n    key_finding: >\\n      RL reward 应有界且先快速增长后缓慢收敛。系统研究 reward shaping 原则，\\n      好的 reward 形状能抑制 reward hacking 并提升训练稳定性。\\n    relevance_to_ced_stabilizer: >\\n      CED reward 的 0-1 对比判别结构天然满足有界性，\\n      且 evidence quality 的渐进提升符合\\\"先快后慢\\\"的 reward shaping 原则。\\n\\n  # === Category 2: Mode Collapse Prevention in GRPO/RLHF ===\\n\\n  - title: \\\"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\\\"\\n    authors: ByteDance Seed, Tsinghua AIR\\n    year: 2025\\n    venue: NeurIPS 2025\\n    url: https://arxiv.org/abs/2503.14476\\n    category: mode_collapse_prevention\\n    role: key_baseline\\n    key_finding: >\\n      Naive GRPO 存在 entropy collapse（policy 熵快速下降→输出同质化）。\\n      DAPO 提出 Clip-Higher（放大 importance sampling 上界）和 Dynamic Sampling\\n      来对抗 entropy collapse，在 AIME 2024 上超越 DeepSeek-R1-Zero。\\n    relevance_to_ced_stabilizer: >\\n      DAPO 从 optimization 技巧角度解决 entropy collapse；CED reward 本身就能防止 mode collapse，\\n      无需额外 clip 调整。reward design vs. algorithm trick 的对比。\\n\\n  - title: \\\"Dr. GRPO: Removing Optimization Bias in GRPO\\\"\\n    authors: Liu et al.\\n    year: 2025\\n    venue: COLM 2025\\n    url: https://arxiv.org/abs/2503.20783\\n    category: mode_collapse_prevention\\n    role: related_analysis\\n    key_finding: >\\n      GRPO 的 std 归一化对低 variance 组（全对/全错）给予过高 advantage 权重引入 difficulty bias。\\n      Dr. GRPO 移除 std 归一化项消除偏差，在 per-token 基础上表现更优。\\n    relevance_to_ced_stabilizer: >\\n      分析了 reward_std→0 时的问题（advantage 异常放大或归零），\\n      与我们观察到的 extraction-only reward 下 frac_zero_std→0.8 现象高度一致。\\n      CED 通过增加 reward 维度天然维持 reward_std>0，避免了这一 bias。\\n\\n  - title: \\\"GVPO: Group Variance Policy Optimization for LLM Post-Training\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: NeurIPS 2025\\n    url: https://arxiv.org/abs/2504.19599\\n    category: mode_collapse_prevention\\n    role: alternative_framework\\n    key_finding: >\\n      将 KL 约束 reward 最大化的解析解直接嵌入梯度权重，\\n      variance 项自然平衡 exploration 与 exploitation，维持适度 entropy。\\n    relevance_to_ced_stabilizer: >\\n      GVPO 的 variance 项机制与 CED 维持 reward variance 的效果功能类似，\\n      但 GVPO 是算法层面 implicit regularization，CED 是 reward 层面 explicit structure。\\n\\n  - title: \\\"REINFORCE++: Stabilizing Critic-Free Policy Optimization with Global Advantage Normalization\\\"\\n    authors: Jian Hu et al.\\n    year: 2025\\n    venue: arXiv 2501.03262\\n    url: https://arxiv.org/abs/2501.03262\\n    category: mode_collapse_prevention\\n    role: related_method\\n    key_finding: >\\n      Prompt-level (local) advantage normalization 导致不准确估计和过拟合。\\n      Global batch normalization 提供更稳定、理论无偏的 gradient estimator。\\n    relevance_to_ced_stabilizer: >\\n      解决 local normalization 的 variance 问题；CED 从 reward 端增加 variance 来源。\\n      两者在不同层面解决同一问题：防止 gradient signal 消失。\\n\\n  - title: \\\"DiverseGRPO: Mitigating Mode Collapse in Image Generation via Diversity-Aware GRPO\\\"\\n    authors: Henglin Liu et al.\\n    year: 2025\\n    venue: arXiv 2512.21514\\n    url: https://arxiv.org/abs/2512.21514\\n    category: mode_collapse_prevention\\n    role: parallel_work\\n    key_finding: >\\n      图像生成中 GRPO 后期输出同质化。distributional reward modeling（谱聚类+exploratory reward）\\n      和 structure-aware regularization 实现 13-18% 语义多样性提升。\\n    relevance_to_ced_stabilizer: >\\n      跨域验证了 GRPO mode collapse 的普遍性，distributional reward 思路与 CED 精神相近——\\n      都是通过 reward 层面结构化信号维持输出多样性。\\n\\n  - title: \\\"Why GRPO Needs Normalization: A Local-Curvature Perspective on Adaptive Gradients\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: arXiv 2601.23135\\n    url: https://arxiv.org/abs/2601.23135\\n    category: mode_collapse_prevention\\n    role: theoretical_support\\n    key_finding: >\\n      GRPO 的 reward_std 归一化在温和条件下提供严格优于未归一化 REINFORCE 的收敛速率，\\n      收益由 prompt 间平均 reward std 刻画。\\n    relevance_to_ced_stabilizer: >\\n      直接理论支撑：reward_std 越大收敛越好。CED 通过 evidence quality 维度维持高 reward_std，\\n      从该理论看 CED 的稳定性优势是 reward_std 维持带来的收敛速率优势。\\n\\n  # === Category 3: Contrastive Rewards in RL ===\\n\\n  - title: \\\"Improving Reinforcement Learning from Human Feedback Using Contrastive Rewards\\\"\\n    authors: Shen, Zhang et al.\\n    year: 2024\\n    venue: arXiv 2403.07708\\n    url: https://arxiv.org/abs/2403.07708\\n    category: contrastive_reward\\n    role: closest_contrastive_precedent\\n    key_finding: >\\n      Contrastive reward 让 LLM 惩罚 reward uncertainty、改善鲁棒性、\\n      根据任务难度自适应校准、减少 PPO 中的 variance。\\n    relevance_to_ced_stabilizer: >\\n      最接近的对比 reward 先例。但针对 RLHF 通用场景，\\n      CED 是 task-specific evidence discrimination 对比信号，且在 GRPO（非 PPO）中验证。\\n\\n  - title: \\\"Improving Discriminative Capability of Reward Models in RLHF Using Contrastive Learning\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: EMNLP 2024\\n    url: https://aclanthology.org/2024.emnlp-main.852/\\n    category: contrastive_reward\\n    role: related_method\\n    key_finding: >\\n      无监督对比损失训练 reward model 充分捕捉对比数据区分度，\\n      带来更稳定的 PPO 训练 return 和 reward。\\n    relevance_to_ced_stabilizer: >\\n      验证对比训练 reward model → 更稳定 RL 训练链条。CED 不是对比训练 reward model，\\n      而是 reward function 本身就是对比判别，但 stabilizing 机制相通。\\n\\n  - title: \\\"Contrastive Preference Learning: Learning from Human Feedback without RL\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: ICLR 2025\\n    url: https://openreview.net/forum?id=iX1RjVQODj\\n    category: contrastive_reward\\n    role: background\\n    key_finding: >\\n      将 preference learning 重新表述为对比学习问题，无需显式 RL 即可从人类反馈中学习。\\n    relevance_to_ced_stabilizer: >\\n      对比框架在 preference alignment 中的通用性。CED 可被视为 task-specific contrastive preference signal。\\n\\n  # === Category 4: Evidence-Based Rewards in IE/NLP ===\\n\\n  - title: \\\"Drift: Enhancing LLM Faithfulness in Rationale Generation\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: ACL 2025\\n    url: https://aclanthology.org/2025.acl-long.340.pdf\\n    category: evidence_reward\\n    role: related_method\\n    key_finding: >\\n      用 faithfulness reward 引导 LLM 生成更可靠的 rationale，提升 CoT 推理事实一致性。\\n    relevance_to_ced_stabilizer: >\\n      Faithfulness reward 用于生成质量的先例。CED 中 evidence discrimination\\n      本质上也是 faithfulness 信号——判断证据是否忠实支持抽取结果。\\n\\n  - title: \\\"Fine-Grained NLI-Based Faithfulness Evaluation for Diverse Summarisation Tasks (INFUSE)\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: EACL 2024\\n    url: https://aclanthology.org/2024.eacl-long.102/\\n    category: evidence_reward\\n    role: background\\n    key_finding: >\\n      变长前提+简化假设的细粒度 NLI faithfulness 评估，超越传统 NLI 在多任务摘要上的表现。\\n    relevance_to_ced_stabilizer: >\\n      NLI 作为 faithfulness 评估工具的进展。CED 中 NLI 组件用于判断 evidence 对 triple 的支持度。\\n\\n  - title: \\\"Enhancing Cross-Evidence Reasoning Graph for Document-Level Relation Extraction\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: PMC/Bioinformatics 2024\\n    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11232587/\\n    category: evidence_reward\\n    role: background\\n    key_finding: >\\n      文档级关系抽取中用 cross-evidence reasoning graph 增强跨证据推理。\\n    relevance_to_ced_stabilizer: >\\n      DocRE 中 evidence 的重要性。但用 evidence 作为模型输入特征，\\n      我们用 evidence quality 作为 RL reward 信号——定位根本不同。\\n\\n  # === Category 5: Multi-Objective RL for Text Generation ===\\n\\n  - title: \\\"Confronting Reward Model Overoptimization with Constrained RLHF\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: OpenReview\\n    url: https://openreview.net/forum?id=gkfUvn0fLU\\n    category: multi_objective_rl\\n    role: related_analysis\\n    key_finding: >\\n      多组件 RM 的 overoptimization 研究。component RM 间的相关性显著影响 overoptimization 临界点，\\n      用 constrained MDP 防止超出适当边界。\\n    relevance_to_ced_stabilizer: >\\n      CED 引入了与 extraction F1 低相关的 reward component（evidence quality），\\n      根据该论文分析低相关多组件 reward 更不易 overoptimize，\\n      可能是 CED 稳定性的另一个理论解释角度。\\n\\n  - title: \\\"On-Policy RL with Optimal Reward Baseline\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: arXiv 2505.23585\\n    url: https://arxiv.org/abs/2505.23585\\n    category: multi_objective_rl\\n    role: theoretical_support\\n    key_finding: >\\n      Optimal baseline 一致性地实现更高训练 reward 和更高 entropy，\\n      有效稳定训练并促进更多样的 policy exploration。\\n    relevance_to_ced_stabilizer: >\\n      CED reward 的多维特性可能起到类似 optimal baseline 效果——\\n      evidence quality 维度为 advantage estimation 提供更丰富的参照信号。\\n\\n  # === Category 6: RSFT Methodology & Theory ===\\n\\n  - title: \\\"A Minimalist Approach to LLM Reasoning: from Rejection Sampling to Reinforce\\\"\\n    authors: Xiao et al.\\n    year: 2025\\n    venue: arXiv 2504.11343\\n    url: https://arxiv.org/abs/2504.11343\\n    category: rsft_methodology\\n    role: key_theoretical_support\\n    key_finding: >\\n      RAFT（简单 rejection sampling baseline）在数学推理上与 GRPO/PPO 表现相当。\\n      消融实验表明 GRPO 的主要优势来自丢弃全错 prompt 而非 reward normalization。\\n      提出 Reinforce-Rej，在 RAFT 基础上过滤全对和全错 sample。\\n    relevance_to_rsft_docre: >\\n      直接支持我们的设计选择：RSFT 在 DocRE 上成功而 GRPO 失败的原因可能是\\n      structured output（DocRE）比 math reasoning 更难用 online RL 优化，\\n      而 rejection sampling 的 offline 特性天然避免了 catastrophic forgetting。\\n\\n  - title: \\\"Beyond Rejection Sampling: Trajectory Fusion for Scaling Mathematical Reasoning (TrajFusion)\\\"\\n    authors: Jie Deng et al.\\n    year: 2026\\n    venue: arXiv 2602.04391\\n    url: https://arxiv.org/abs/2602.04391\\n    category: rsft_methodology\\n    role: method_component\\n    key_finding: >\\n      传统 RSFT 只用正确轨迹，丢弃错误轨迹。TrajFusion 将错误和正确轨迹交替拼接，\\n      显式建模试错推理过程，在困难数学问题上显著超越标准 RFT。\\n    relevance_to_rsft_docre: >\\n      Future work 方向：可考虑在 DocRE RSFT 中融合失败样本的信息。\\n      但 DocRE 的结构化输出（JSON triple）不同于 math 的 chain-of-thought，\\n      融合方式需要重新设计。\\n\\n  - title: \\\"Rejection Sampling Based Fine Tuning Secretly Performs PPO\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: ICML 2025\\n    url: https://openreview.net/forum?id=yQ2UivKlir\\n    category: rsft_methodology\\n    role: theoretical_support\\n    key_finding: >\\n      建立 RSFT 与 PPO 之间的理论联系：rejection sampling fine-tuning\\n      在特定条件下隐式执行 PPO with marginal KL constraints。\\n    relevance_to_rsft_docre: >\\n      为 RSFT 的有效性提供理论解释。我们的 RSFT 成功可被视为\\n      隐式执行了 constrained policy optimization，\\n      避免了显式 GRPO 在 structured output 上的不稳定性。\\n\\n  # === Category 7: RL for Information Extraction ===\\n\\n  - title: \\\"R1-RE: Cross-Domain Relation Extraction with RLVR\\\"\\n    authors: Runpeng Dai, Tong Zheng et al.\\n    year: 2025\\n    venue: arXiv 2507.04642\\n    url: https://arxiv.org/abs/2507.04642\\n    category: rl_for_ie\\n    role: direct_competitor\\n    key_finding: >\\n      首个将 RLVR（GRPO + verifiable reward）用于关系抽取的框架。\\n      将 RE 重构为推理任务，R1-RE-7B 在跨域 OOD 准确率约 70%，\\n      媲美 GPT-4o。在 SemEval-2010 Task 8 和私有 MDKG 数据集上评估。\\n    relevance_to_rsft_docre: >\\n      最直接竞争者。但关键差异：(1) R1-RE 是句子级 RE，我们是文档级 RE；\\n      (2) R1-RE 用 online GRPO，我们用 offline RSFT；\\n      (3) R1-RE 无 evidence extraction 组件，我们有 CED reward；\\n      (4) R1-RE 关注 OOD 泛化，我们关注 evidence-grounded extraction quality。\\n      互补而非直接冲突。\\n\\n  - title: \\\"MORE-R1: Guiding LVLM for Multimodal Object-Entity Relation Extraction via Stepwise Reasoning with RL\\\"\\n    authors: Anonymous\\n    year: 2026\\n    venue: arXiv 2603.09478\\n    url: https://arxiv.org/abs/2603.09478\\n    category: rl_for_ie\\n    role: related_method\\n    key_finding: >\\n      多模态 RE 中用 GRPO + Progressive Sample-Mixing Strategy 优化 LVLM 推理能力。\\n      两阶段训练：SFT cold-start + GRPO RL。\\n    relevance_to_rsft_docre: >\\n      跨模态验证 RL for RE 趋势。其 Progressive Sample-Mixing 与我们\\n      RSFT 的 difficulty-aware sampling 思想相通，但在不同模态。\\n\\n  - title: \\\"REAR: Reinforced Reasoning Optimization for Event Argument Extraction with Relation-Aware Support\\\"\\n    authors: Jianwen Luo et al.\\n    year: 2025\\n    venue: EMNLP 2025 Findings\\n    url: https://2025.emnlp.org/program/find_papers/\\n    category: rl_for_ie\\n    role: related_method\\n    key_finding: >\\n      将强化学习推理优化用于事件论元抽取，结合关系感知支持。\\n      不同于 DocRE 但同属 IE 领域的 RL 应用。\\n    relevance_to_rsft_docre: >\\n      验证 RL 在 IE 任务上的有效性趋势。我们的工作扩展到 DocRE + evidence，\\n      且使用 offline RSFT 而非 online RL。\\n\\n  - title: \\\"Adaptive Reinforcement Learning Planning: Harnessing LLMs for Complex Information Extraction\\\"\\n    authors: Zepeng Ding et al.\\n    year: 2024\\n    venue: arXiv 2406.11455\\n    url: https://arxiv.org/abs/2406.11455\\n    category: rl_for_ie\\n    role: background\\n    key_finding: >\\n      将 LLM 顺序抽取建模为 MDP，用 DDQN 训练 decision module\\n      自适应选择实体抽取顺序，提升复杂 IE 性能。\\n    relevance_to_rsft_docre: >\\n      RL for IE 的早期工作。用 RL 优化抽取策略而非模型本身，\\n      与我们 RSFT 直接微调 LLM 的方法路径不同。\\n\\n  - title: \\\"Graph-R1: Towards Agentic GraphRAG Framework via End-to-end Reinforcement Learning\\\"\\n    authors: Haoran Luo et al.\\n    year: 2025\\n    venue: ICML 2026\\n    url: https://arxiv.org/abs/2507.21892\\n    category: rl_for_ie\\n    role: background\\n    key_finding: >\\n      用端到端 RL 优化 GraphRAG agent 的多轮检索-推理循环，\\n      包含 knowledge hypergraph construction（n-ary relation extraction）。\\n    relevance_to_rsft_docre: >\\n      RL + knowledge extraction 的交叉点。Graph-R1 关注 QA 场景下的知识图谱构建，\\n      我们关注 DocRE 的训练优化，应用场景不同。\\n\\n  # === Category 8: Recent LLM-based DocRE Methods ===\\n\\n  - title: \\\"RelPrior: Relation as a Prior - A Novel Paradigm for LLM-based Document-level Relation Extraction\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: arXiv 2511.08143\\n    url: https://arxiv.org/abs/2511.08143\\n    category: llm_docre\\n    role: key_baseline\\n    key_finding: >\\n      用 binary relation 作为先验过滤无关实体对，再用 predefined relation 匹配实体，\\n      避免 LLM 在 DocRE 中被无关实体对分散注意力。\\n      在 DocRED/Re-DocRED 上超越现有 LLM-based DocRE 方法。\\n    relevance_to_rsft_docre: >\\n      我们的直接 baseline 之一。RelPrior 在 DocRED 上提升 +2.06-2.38pp，\\n      我们的 RSFT 提升 +5.98pp 显著更优。\\n      RelPrior 是 inference paradigm 创新，我们是 training paradigm 创新，正交互补。\\n\\n  - title: \\\"LMRC: LLM with Relation Classifier for Document-Level Relation Extraction\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: arXiv 2408.13889\\n    url: https://arxiv.org/abs/2408.13889\\n    category: llm_docre\\n    role: related_method\\n    key_finding: >\\n      两阶段方法：先用 attention-based classifier 过滤 NA 实体对（RCP），\\n      再用 LLM 在精简候选空间中做多分类（RC）。\\n      在 DocRED/Re-DocRED 上显著优于其他 LLM-based DocRE 方法。\\n    relevance_to_rsft_docre: >\\n      LMRC 用小模型预筛选 + LLM 分类的 pipeline 方式，与我们端到端 LLM 生成方式不同。\\n      展示 LLM-based DocRE 的 class imbalance 挑战，我们通过 RSFT 的 reward-based filtering 隐式解决。\\n\\n  - title: \\\"Ru-LLM: Logical Rule-Constrained Large Language Models for Document-Level Relation Extraction\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: NLPCC 2025\\n    url: https://link.springer.com/chapter/10.1007/978-981-95-3343-5_11\\n    category: llm_docre\\n    role: related_method\\n    key_finding: >\\n      用频繁模式挖掘 + MCTS 搜索逻辑规则，转化为 prompt 约束 LLM 输出，\\n      再用 CoT 验证过滤不满足规则的 triple。\\n      在 DWIE、DocRED、Re-DocRED 上超越现有 LLM 方法和规则框架。\\n    relevance_to_rsft_docre: >\\n      规则约束方式与我们的 CED reward 在 motivation 上相似（都是引入外部知识约束），\\n      但 Ru-LLM 用 inference-time 规则验证，我们用 training-time reward shaping。\\n\\n  - title: \\\"GLiDRE: Generalist Lightweight model for Document-level Relation Extraction\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: arXiv 2508.00757\\n    url: https://arxiv.org/abs/2508.00757\\n    category: llm_docre\\n    role: background\\n    key_finding: >\\n      基于 dual-encoder 的轻量级零/少样本 DocRE 模型，\\n      在 Re-DocRED、FREDo 等 benchmark 的 few-shot 场景达到 SOTA。\\n      预训练于 136K 文档的大规模 RE 数据。\\n    relevance_to_rsft_docre: >\\n      不同范式（encoder-based vs LLM generative），\\n      但验证了 DocRE 领域仍有方法创新空间。\\n\\n  - title: \\\"AutoRE: Document-Level Relation Extraction with Large Language Models\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: arXiv 2403.14888\\n    url: https://arxiv.org/abs/2403.14888\\n    category: llm_docre\\n    role: background\\n    key_finding: >\\n      RHF（Relation-Head-Facts）范式用 Mistral-7B + QLoRA 做端到端 DocRE，\\n      在多个 LLM 上达到 SOTA。\\n    relevance_to_rsft_docre: >\\n      QLoRA fine-tuning for DocRE 的先例。我们的 SFT baseline 与之类似，\\n      RSFT 在此基础上引入 reward-guided sample selection 进一步提升。\\n\", \"total_chars\": 17868, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "991f6aa7-108e-487f-a406-8213a86c626f",
  "isSidechain": true,
  "promptId": "00a1eb94-0484-4e13-931d-e659507bc0c6",
  "agentId": "a9bd4203964701927",
  "type": "user",
  "uuid": "6023e9f1-5fc2-46a4-a744-5021c4f702f5",
  "sourceToolAssistantUUID": "991f6aa7-108e-487f-a406-8213a86c626f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T12:47:35.681Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01GGoicpmiXRF44uGzjTNLoc`</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6023e9f1-5fc2-46a4-a744-5021c4f702f5",
  "isSidechain": true,
  "agentId": "a9bd4203964701927",
  "requestId": "req_011Cb4NySfMGvnmM4qtUE8VB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4e91b107-3310-48d5-abb8-48d4d83f7287",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YcRPc8eqRu572amtXTuUYh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11064,
      "cache_read_input_tokens": 21262,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11064,
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

_source line 22 · 2026-05-15T12:47:35.693Z_

<details><summary>↩ Tool result · `toolu_01GGoicpmiXRF44uGzjTNLoc`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/decisions.yaml\", \"content\": \"_next_id: 41\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 04:21 UTC\\n  summary: MVP 设计：两阶段验证——MVP-1 CED 信号验证（离线）→ MVP-2 端到端训练验证\\n  rationale: CED 是核心创新，必须先验证 DeBERTa NLI 能在 DocRED 上区分金标证据与实体共现干扰句（MVP-1），再投入 GPU\\n    跑完整训练流水线（MVP-2）。MVP-1 失败则 idea 需 pivot，避免浪费 GPU。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 05:46 UTC\\n  summary: 'MVP-1 PASS: CED 信号验证通过，核心假设成立（margin 0.48, accuracy 81.5%, Pearson r 0.34）'\\n  rationale: CED margin 4.8× 超过阈值，DeBERTa 判别力主要来自语义蕴含而非词汇重叠（r=0.34 远低于 0.7）。三个需关注项：33.4%\\n    gold p_pos < τ=0.5（τ 可能需调低）、44.4% 无 hard negatives（退化为 flat NLI）、少数负 margin 样本（标注噪声）。这些不影响\\n    MVP 结论但影响 Research 阶段 CED 调参。\\n  related_experiments:\\n  - exp_id: mvp1_ced_signal\\n    role: primary\\n    result: PASS — mean_margin=0.4827, accuracy=81.5%, pearson_r=0.3406\\n  depends_on: []\\n- id: D003\\n  date: 2026-05-14 06:02 UTC\\n  summary: 'Smoke test 功能性 PASS: ZeRO-2 + QLoRA 兼容，4.9GB/卡，授权启动 MVP-2 SFT'\\n  rationale: Smoke test 自报 FAIL 是假阴性——synthetic data format-only reward 产生零 variance，数学上无梯度是正常行为。关键目标全部达成：ZeRO-2+QLoRA+GRPOTrainer\\n    兼容、显存充裕（4.9/32GB）、有 reward variance 时梯度正常。Reviewer 独立确认功能性 PASS。\\n  related_experiments:\\n  - exp_id: smoke_test_grpo\\n    role: infrastructure\\n    result: 功能性 PASS (ZeRO-2+QLoRA, 4×5090, 4.9GB/卡)\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 07:26 UTC\\n  summary: 发现 rtx5090-4x 和 gpu-5090-4x-1 为同一台机器（4 GPU），GRPO 三路对比改为串行\\n  rationale: Reviewer 核实两个 SSH endpoint 返回相同 hostname 和 PID。实际资源 = 4× RTX 5090 32GB，非\\n    8 张。串行 3 路 GRPO 预估 ~7-10h（每路 ~2-3h），今天内可完成 MVP-2，暂不需要额外申请 GPU。\\n  related_experiments: []\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-14 10:03 UTC\\n  summary: CED r1 训练 step 40 后 mode collapse，启动早停+checkpoint 抢救+cliprange 排查\\n  rationale: Reviewer 审查发现 step 40 后所有指标退化（total_reward 1.79→1.10, f1 0.098→0.012,\\n    length 88→547）。clip_ratio 全程为 0 表明 PPO 裁剪未生效，可能是 policy drift 失控的根因。决策：(1) 抢救\\n    step 40 checkpoint 作为当前最优；(2) step 70 前不回升则 kill；(3) 排查并修正 cliprange 后重跑。step\\n    40 checkpoint 仍可用于 vs SFT 的对比 eval，MVP-2 流程不完全停滞。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r1\\n    role: primary\\n    result: training collapse after step 40, early stopping evaluation in progress\\n  depends_on:\\n  - D003\\n  - D004\\n- id: D006\\n  date: 2026-05-14 10:24 UTC\\n  summary: Kill CED r1（F1 归零+无 checkpoint），准备修复配置后重跑 r2\\n  rationale: Reviewer 确认 step 80 时 f1_reward=0.001（从 peak 0.098 单调下降 50 步），grpo_s3\\n    目录为空（无中间 checkpoint），step 40 最优模型不可挽回。继续 1.3h 必产废模型。诊断三个根因：(1) 无 save_steps 配置；(2)\\n    reward 权重失衡（format ~0.97 远大于 f1 ~0.001，模型无 f1 梯度信号）；(3) clip_ratio=0 裁剪未生效。决策\\n    kill 并修复后重跑 r2。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r1\\n    role: primary\\n    result: KILL — f1_reward 归零, 无 checkpoint, 训练不可挽回\\n  depends_on:\\n  - D005\\n- id: D007\\n  date: 2026-05-14 11:28 UTC\\n  summary: r3 回退 num_iterations=1，隔离变量逐一测试\\n  rationale: Reviewer CRITICAL 确认：r2 的 KL 在 step 5 爆到 37亿、step 15 爆到 3400亿，直接导致 loss\\n    爆炸+OOM。根因是 num_iterations=2 + QLoRA 4-bit 量化 logits 精度不足，两次迭代间 KL 被放大。r2 同时改了\\n    6 个超参，崩溃后无法归因。r3 必须回退 num_iterations=1，保留 reward weighting（reward 0.25→0.42 正常上升证明\\n    WeightedRewardFn 有效），一次只改一个变量。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r2\\n    role: evidence\\n    result: KL explosion + OOM at step 18, num_iterations=2 confirmed as root cause\\n  depends_on: []\\n- id: D008\\n  date: 2026-05-14 12:07 UTC\\n  summary: D007 证伪：KL 爆炸根因是 kl_coef + QLoRA 4-bit 不兼容，非 num_iterations。全部 GRPO 重跑\\n    kl_coef=0\\n  rationale: 3 个 GRPO 实验（num_iterations=1）均在 step 5 触发 KL 爆炸早停（KL 达 10^10 量级）。对比 r1（kl_coef=0/未设）跑了\\n    80+ steps 才因 reward imbalance collapse。证据链：所有设 kl_coef=0.05 的实验全部 step 5 爆炸，未设的\\n    r1 稳定运行。机理：QLoRA 4-bit 量化噪声导致 ref model 和 training model 的 log-probs 存在系统性偏差，KL(π_θ||π_ref)\\n    从第一步就是天文数字。修复：kl_coef=0，依赖 reward weighting + save_steps + KL 监控（logging only）控制稳定性。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r3\\n    role: evidence\\n    result: KL explosion step 5, kl_coef=0.05, num_iterations=1\\n  - exp_id: mvp2_grpo_extract\\n    role: evidence\\n    result: KL explosion step 5, KL=69.5B\\n  - exp_id: mvp2_grpo_flatnli\\n    role: evidence\\n    result: KL explosion step 5, KL=50.8B\\n  depends_on:\\n  - D007\\n- id: D009\\n  date: 2026-05-14 12:12 UTC\\n  summary: CED r4 采用保守配置：grad_accum=16 + lr=5e-6 + kl_coef=0.5 + warmup 200步，解决 r3\\n    单卡 batch=1 + 高 lr 导致的 KL 爆炸\\n  rationale: r3 根因明确：单卡无 grad_accum 导致 effective batch=1，梯度噪声极高，5 步内 KL 爆炸至 4.4M。r1-r3\\n    三次失败模式不同（mode collapse / OOM / KL explosion），说明 CED reward 本身不是问题，是训练超参不稳定。r4\\n    同时修复 3 个因素：(1) grad_accum=16 使 effective batch=16; (2) lr 从 5e-5 降至 5e-6; (3)\\n    kl_coef 从 0.05 升至 0.5 加强偏离惩罚; (4) 加 200 步 warmup 稳定初始阶段。需先拿到 extract 和 flatnli\\n    r1 结果作为对照基线。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r3\\n    role: evidence\\n    result: failed - KL explosion at step 5, batch=1 root cause\\n  - exp_id: mvp2_grpo_ced_r4\\n    role: target\\n    result: pending approval\\n  depends_on: []\\n- id: D010\\n  date: 2026-05-14 12:32 UTC\\n  summary: 选择 Option A：保留 kl_coef=0.0 实验进程，修复 registry 状态从 killed → RUNNING；D009 的\\n    kl_coef=0.5 正式作废\\n  rationale: Reviewer critical 报告 registry-reality 不一致。3 个实验实际在跑（kl_coef=0.0, grad_acc=16）但\\n    registry 标记 killed。配置本身正确——D008 已证明 kl_coef>0 在 QLoRA 4-bit 下不稳定（r1 kl_coef=0\\n    稳定 80 步 vs 所有 kl_coef>0 爆炸）。D009 提出的 kl_coef=0.5 会放大 QLoRA 量化噪声导致的 KL 计算失真，Reviewer\\n    warning 合理，该指令作废。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r4\\n    role: target\\n    result: running with kl_coef=0.0, registry fix needed\\n  - exp_id: mvp2_grpo_extract_r2\\n    role: target\\n    result: running with kl_coef=0.0, registry fix needed\\n  - exp_id: mvp2_grpo_flatnli_r2\\n    role: target\\n    result: running with kl_coef=0.0, registry fix needed\\n  depends_on:\\n  - D008\\n  - D009\\n- id: D011\\n  date: 2026-05-14 13:30 UTC\\n  summary: 采纳 Reviewer 评估框架审查：精确化 pass criteria、补充 extraction-only vs SFT 对比、要求多 checkpoint\\n    eval + 统一 eval 脚本\\n  rationale: Reviewer 指出 4 个 warning：(1) 缺 extraction-only vs SFT 对比——回答 GRPO 本身是否有效；(2)\\n    kl_coef=0 必须 eval 多 checkpoint 避免 collapse 后只看末尾；(3) pass criteria 需精确化基准；(4)\\n    eval 代码必须统一。全部采纳，已更新 ROADMAP 和指令 Agent。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r5\\n    role: target\\n  - exp_id: mvp2_grpo_extract_r3\\n    role: target\\n  - exp_id: mvp2_grpo_flatnli_r3\\n    role: target\\n  - exp_id: mvp2_sft_eval_r2\\n    role: baseline\\n  depends_on:\\n  - D010\\n- id: D012\\n  date: 2026-05-14 14:54 UTC\\n  summary: 调整 MVP-2 pass criteria：取消绝对 F1>45 门槛，改为相对标准；EDCR 升为主指标\\n  rationale: SFT baseline F1=40.57%（37% 输出截断于 1024 tokens），绝对门槛 F1>45 已不现实。截断影响所有模型相同，相对对比仍有效。Evi-F1=79.79%\\n    设了高 baseline，但 EDCR=71.18% 说明模型\\\"spray-and-pray\\\"大量引用 distractor——CED 的核心攻击目标。调整后\\n    pass criteria：(1) CED_Evi-F1 ≥ SFT_Evi-F1（方向正确）；(2) CED_F1 ≥ max(extract, SFT)\\n    - 5pp（不退化）；(3) CED_EDCR 显著低于 SFT_EDCR（核心判据）；(4) CED > flat-NLI 在 Evi-F1 或 EDCR\\n    上方向正确。绝对指标留到 post-MVP 增大 max_new_tokens 后重评。\\n  related_experiments:\\n  - exp_id: mvp2_sft_eval_r2\\n    role: baseline\\n    result: F1=40.57%, Evi-F1=79.79%, EDCR=71.18%\\n  depends_on:\\n  - D011\\n- id: D013\\n  date: 2026-05-14 14:54 UTC\\n  summary: MVP-2 pass criteria 调整：取消绝对 F1>45 门槛，改为相对对比；EDCR 升为核心判定指标\\n  rationale: SFT baseline F1=40.57%（37% 输出被 1024 token 截断导致），已低于原定 F1>45 门槛。但截断对所有模型等效影响，相对对比仍然公平。调整后\\n    pass criteria：(1) 核心不变：CED_Evi-F1 − SFT_Evi-F1 ≥ 2pp；(2) F1 改为相对：CED_F1 ≥ SFT_F1\\n    − 5pp（即 ≥35.57）；(3) 新增 EDCR 核心判定：CED_EDCR 显著低于 SFT_EDCR（71.18%），降幅 ≥10pp 视为强证据；(4)\\n    保持 CED > flat-NLI 方向。SFT EDCR=71% 说明 SFT 模型大量引用 entity-sharing distractors，正是\\n    CED 设计目标的攻击面。即使 Evi-F1 提升不足 2pp，EDCR 大幅下降也足以支撑 Claim 2。\\n  related_experiments:\\n  - exp_id: mvp2_sft_eval_r2\\n    role: baseline\\n    result: F1=40.57%, Evi-F1=79.79%, EDCR=71.18%\\n  depends_on:\\n  - D011\\n- id: D014\\n  date: 2026-05-14 14:58 UTC\\n  summary: CED r5 mode collapse 确认 kill；CED reward 必须加 F1 门控防止短输出 hack；暂停 ced_kl001\\n  rationale: CED r5 在 65% 进度完全 collapse：completion 固定 34 tokens，f1_reward=0，ced_reward≈0.99，entropy≈0。模型发现极短输出不引用\\n    distractor 即可获得近完美 CED 分——CED 自身被 reward hack。根因：CED reward 不依赖抽取质量，模型可在 F1=0\\n    时仍获高 CED reward。修复方案：F1 门控——仅在 completion 包含 ≥1 个 predicted triple 时计算 CED reward，否则\\n    CED=0。这确保 evidence quality 的评估以有效抽取为前提。ced_kl001 使用同样有缺陷的 reward 设计，必须暂停，等修复后再启动。extract_r3\\n    部分 collapse 但仍有 F1 信号，继续观察。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r5\\n    role: failed\\n    result: 'mode collapse: f1=0, ced≈0.99, 34-token fixed output'\\n  - exp_id: mvp2_grpo_extract_r3\\n    role: monitoring\\n    result: 'partial collapse: f1=0.2-0.34, 43-50 tokens, trending down'\\n  - exp_id: mvp2_grpo_flatnli_r3\\n    role: healthy\\n    result: 'healthy: entropy=0.087, grad_norm=0.398, 11% progress'\\n  depends_on:\\n  - D013\\n- id: D015\\n  date: 2026-05-14 14:58 UTC\\n  summary: ced_r5 mode collapse 保留跑完取分析价值；flatnli_r3 kill 并修复 NLI device 后重启\\n  rationale: ced_r5 在 63% 进度时 f1_reward=0 + entropy≈0，已 mode collapse。保留跑完因为：(1) negative\\n    result 证明纯 CED reward 导致 collapse，支撑 reward balance 的 ablation story；(2) 早期 checkpoint\\n    可能有 f1_reward 正常的版本可用。flatnli_r3 因 NLI 推理在 CPU 上运行导致 10x 减速（124s/it vs 12s/it），预计\\n    20h+。RTX 5090 32GB 有足够余量放 DeBERTa-v3-base (~400MB)，kill 后修复 device 配置重启可将时间降至\\n    2-3h。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r5\\n    role: subject\\n    result: f1_reward=0, mode collapse at 63%\\n  - exp_id: mvp2_grpo_flatnli_r3\\n    role: subject\\n    result: NLI on CPU, 10x slowdown, killed for restart\\n  depends_on:\\n  - D011\\n- id: D016\\n  date: 2026-05-14 15:00 UTC\\n  summary: Kill ced_r5 (total collapse)，ced_kl001 移到 cuda:0 立即启动\\n  rationale: ced_r5 step 250+ f1_reward=0、completion 坍缩到 34 tokens、save_total_limit=5\\n    已覆盖所有正常 checkpoint。继续跑无任何回收价值。Kill 后释放 cuda:0 给 ced_kl001（kl_coef=0.01），不再等 cuda:1。ced_kl001\\n    现在是 MVP-2 最关键实验——验证 CED+KL约束能否避免 reward hacking。extract_r3 和 flatnli_r3 保持 kl=0\\n    继续跑，作为对照：若它们没 collapse，说明问题是 CED reward 特异的；若也 collapse，说明 kl=0 通病。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r5\\n    role: failed\\n    result: total mode collapse, killed\\n  - exp_id: mvp2_grpo_ced_kl001\\n    role: replacement\\n    result: moved to cuda:0, critical experiment\\n  depends_on:\\n  - D015\\n- id: D017\\n  date: 2026-05-14 15:01 UTC\\n  summary: Kill ced_r5 + extract_r3 (kl_coef=0 collapse/stall), 部署 kl_coef=0.01 修正实验\\n  rationale: 3路GRPO健康检查：ced_r5完全mode collapse(entropy=0.0005, F1=0, grad_norm=0)，extract_r3训练停滞(grad_norm=0,\\n    F1=0.20低于SFT baseline 0.4057)。共同根因kl_coef=0导致策略无约束偏移。D008显示kl_coef=0.05会KL爆炸，选择0.01作为中间值（5x低于爆炸阈值）。flatnli_r3保留作为kl_coef=0对照组继续观察。\\n  related_experiments:\\n  - exp_id: ced_r5\\n    role: failed\\n    result: mode collapse, entropy=0.0005, F1=0\\n  - exp_id: extract_r3\\n    role: failed\\n    result: stalled, grad_norm=0, F1=0.20\\n  - exp_id: flatnli_r3\\n    role: control\\n    result: healthy at 10.7%, continue as kl_coef=0 control\\n  - exp_id: D008\\n    role: reference\\n    result: kl_coef=0.05 caused KL explosion\\n  depends_on: []\\n- id: D018\\n  date: 2026-05-14 15:04 UTC\\n  summary: flatnli_r3 紧急修复 reward_device cpu→cuda，extract_r3 改为跑完再替换\\n  rationale: Reviewer critical 发现 D015 未执行：flatnli_r3 仍以 --reward_device cpu 运行，step_time\\n    123s/step（GPU 后应 12-15s/step），cuda:3 被占用但 90% 时间等 CPU。修复后从 ~23h 降至 ~2-3h，是当前最高\\n    ROI 操作。extract_r3 已 68%（~50min 完成），改为跑完后再部署 extract_kl001，避免浪费已投入的 2.5h。ced_r5\\n    维持 kill（3.3h GPU 时间用于 ced_kl001 更有价值）。\\n  related_experiments:\\n  - exp_id: flatnli_r3\\n    role: fix\\n    result: reward_device cpu→cuda, from checkpoint-80 resume\\n  - exp_id: extract_r3\\n    role: revised\\n    result: let finish (~50min), then replace with extract_kl001\\n  - exp_id: ced_r5\\n    role: kill\\n    result: maintain kill decision, replace with ced_kl001\\n  depends_on:\\n  - D015\\n  - D017\\n- id: D019\\n  date: 2026-05-14 15:05 UTC\\n  summary: 修正 D017：extract_r3 改为跑完再释放，flatnli_r3 紧急补执行 D015（修复 NLI device 重启）\\n  rationale: Reviewer 审查发现：(1) D015 未执行——flatnli_r3 仍用 CPU NLI，step_time 120s vs GPU\\n    应 12-15s，23h→2-3h 的 10x 效率差，cuda:3 90% 时间在等 CPU。(2) extract_r3 只剩 ~50min，跑完可取早期\\n    checkpoint（collapse 前 step 20-100 可能比 last 好），不值得 kill 浪费已投入的 2.5h。修正后：cuda:0\\n    立即释放给 ced_kl001，cuda:2 等 50min 后给 extract_kl001，cuda:3 kill+修复 NLI device 后从 ckpt-80\\n    重启。\\n  related_experiments:\\n  - exp_id: flatnli_r3\\n    role: fix\\n    result: D015 未执行，NLI 在 CPU 导致 10x 低效，需 kill+修复+重启\\n  - exp_id: extract_r3\\n    role: revised\\n    result: 改为跑完（~50min），eval 早期 checkpoint\\n  - exp_id: ced_r5\\n    role: kill\\n    result: 仍立即 kill，与 D017 一致\\n  depends_on:\\n  - D017\\n  - D015\\n- id: D020\\n  date: 2026-05-14 15:15 UTC\\n  summary: ced_kl001 启动前必须先修复 CED reward F1 门控（D014 未实现）；kl_coef=0.01 实验改为 100 步探测性运行\\n  rationale: Reviewer 代码核查确认 D014 的 F1 门控从未实现：ced_reward.py 对 0-triple 短输出仍给近完美分(0.99)。ced_r5\\n    的 collapse 根因是双重的——kl_coef=0 导致策略自由偏移 + CED reward 对短输出的 hack。仅修 kl_coef 不解决 reward\\n    设计缺陷，ced_kl001 会重复失败。同时 kl_coef=0.01+QLoRA 的兼容性未验证（D008 证明 0.05 爆炸），先做 100 步探测降低风险。\\n  related_experiments:\\n  - exp_id: ced_r5\\n    role: evidence\\n    result: 34-token 短输出 → CED≈0.99 → reward hack → collapse\\n  - exp_id: ced_kl001\\n    role: blocked\\n    result: 等 CED reward 修复后才能启动\\n  - exp_id: D008\\n    role: reference\\n    result: kl_coef=0.05+QLoRA KL 爆炸\\n  depends_on:\\n  - D014\\n  - D017\\n  - D019\\n- id: D021\\n  date: 2026-05-14 17:20 UTC\\n  summary: Kill flatnli_r5（从已 hacked checkpoint 恢复无效），启动 flatnli_r6 从 SFT 全新训练 D020\\n    配置\\n  rationale: Reviewer 独立审查发现 flatnli_r3 checkpoint-100 已深陷 NLI reward hacking（f1=0.025,\\n    flat_nli=0.911）。从该 checkpoint 恢复加 kl_coef=0.01 后 KL=0.46（远高于从 SFT 新训的 ced_kl001_r4\\n    的 0.098），frac_zero_std 升至 0.8-0.9，grad_norm 近零——训练冻结。教训：从 kl=0 已漂移 checkpoint\\n    恢复并加 kl>0 不可行，必须从 SFT 全新开始。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_flatnli_r5\\n    role: 被 kill\\n    result: negative\\n  - exp_id: mvp2_grpo_flatnli_r3\\n    role: 提供了已 hacked 的 checkpoint\\n    result: negative\\n  - exp_id: mvp2_grpo_ced_kl001_r4\\n    role: 健康参照（从 SFT 新训）\\n    result: running\\n  depends_on:\\n  - D020\\n- id: D022\\n  date: 2026-05-14 17:40 UTC\\n  summary: Kill extract_r4 (f1_reward=0 at ckpt-30, mode collapse confirmed); cuda:2\\n    转 ced_kl001_r4 多 checkpoint eval\\n  rationale: extract_r4 (extraction-only, kl_coef=0.01+gen=8) 在 step 10 后 f1_reward\\n    归零、frac_zero_std≥0.8 停滞，checkpoint-30 无恢复信号。同配置的 ced_kl001_r4 在 step 20 f1_reward=0.082\\n    持续上升——直接证明 CED reward 通道是驱动学习的关键因素。这一负面结果本身是强证据，不再尝试 extract_r5。cuda:2 空闲，派去 eval\\n    ced_kl001_r4 中间 checkpoint，提前获取多 checkpoint 评估数据。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_extract_r4\\n    role: killed\\n    result: f1_reward=0 at ckpt-30, mode collapse\\n  - exp_id: mvp2_grpo_ced_kl001_r4\\n    role: contrast\\n    result: f1_reward=0.082 at step 20, healthy\\n  depends_on:\\n  - D020\\n- id: D023\\n  date: 2026-05-14 17:40 UTC\\n  summary: 'Kill extract_r4 (mode collapse confirmed); ablation 结论: CED reward 是 GRPO\\n    训练必需的 dense signal，extraction-only reward 太稀疏无法驱动学习'\\n  rationale: 'extract_r4 checkpoint-30: f1_reward 连续 25 步为 0，frac_zero_std 升至 0.9，grad_norm\\n    在 0.005-0.012 震荡。对比 ced_kl001_r4 同期（f1_reward=0.082 持续上升，frac_zero_std=0.4 持续下降），唯一差异是\\n    reward type。结论: Stage 1 (extract-only) 在 D020 配置下无法维持 GRPO 探索多样性，CED 提供的 dense\\n    reward signal 是训练成功的必要条件。这是论文的关键 ablation evidence。cuda:2 释放，分配给 SFT eval baseline。'\\n  related_experiments:\\n  - exp_id: mvp2_grpo_extract_r4\\n    role: failed_ablation\\n    result: mode collapse — f1_reward=0 for 25 steps\\n  - exp_id: mvp2_grpo_ced_kl001_r4\\n    role: positive_control\\n    result: f1_reward=0.082 at step 20, healthy training\\n  depends_on:\\n  - D020\\n- id: D024\\n  date: 2026-05-14 18:11 UTC\\n  summary: 'Kill flatnli_r6 (mode collapse step 25); D020 配置下三路 ablation 结论: 仅 CED\\n    reward 存活，extract-only 和 flat-NLI 均 collapse'\\n  rationale: 'flatnli_r6 step 25: frac_zero_std=0.9, f1_reward=0, flat_nli_reward=0,\\n    reward 100% 来自 format。与 extract_r4 collapse 模式一致。三个实验共用 D020 配置（kl=0.01, gen=8），唯一差异是\\n    reward type: extract-only collapse (step 10-30), flat-NLI collapse (step 25),\\n    CED 健康完成 100 步。结论: CED 的对比性 evidence discrimination 提供了 GRPO 所需的 dense gradient\\n    signal，是训练成功的必要条件。这比原设想的\\\"CED 改善 evidence quality\\\"更强——CED 是 GRPO 训练本身能否存活的关键。cuda:3\\n    释放用于加速 eval。'\\n  related_experiments:\\n  - exp_id: mvp2_grpo_flatnli_r6\\n    role: failed_ablation\\n    result: mode collapse step 25, frac_zero_std=0.9\\n  - exp_id: mvp2_grpo_extract_r4\\n    role: failed_ablation\\n    result: mode collapse step 10-30\\n  - exp_id: mvp2_grpo_ced_kl001_r4\\n    role: positive_control\\n    result: 100 steps healthy, reward 0.85-1.37\\n  depends_on:\\n  - D023\\n  - D020\\n- id: D025\\n  date: 2026-05-14 18:11 UTC\\n  summary: Kill flatnli_r6 (mode collapse confirmed step 25); D020 配置下三路 ablation\\n    结论：仅 CED reward 存活，extract-only 和 flat-NLI 均 collapse\\n  rationale: 'flatnli_r6 step 25: frac_zero_std=0.9, f1_reward=0, flat_nli_reward=0,\\n    reward 100% 来自 format。与 extract_r4 collapse 模式一致。D020 配置（kl=0.01, gen=8）下三路对比：extract-only\\n    step 30 collapse, flat-NLI step 25 collapse, CED 100 步健康完成。唯一差异是 reward type。结论：CED\\n    的对比性 evidence discrimination 提供了更丰富的梯度信号，是维持 GRPO 探索多样性的必要条件。这是论文最核心的 ablation\\n    evidence — 但需注意区分\\\"CED reward 本身的 anti-collapse 特性\\\"与\\\"stage 3 组合 reward 的其他差异\\\"两个假设。cuda:3\\n    释放后用于 eval 加速。'\\n  related_experiments:\\n  - exp_id: mvp2_grpo_flatnli_r6\\n    role: failed_ablation\\n    result: mode collapse step 25, frac_zero_std=0.9\\n  - exp_id: mvp2_grpo_extract_r4\\n    role: failed_ablation\\n    result: mode collapse step 30, f1_reward=0\\n  - exp_id: mvp2_grpo_ced_kl001_r4\\n    role: positive_control\\n    result: 100 steps healthy, reward=0.85-1.37\\n  depends_on:\\n  - D023\\n  - D020\\n- id: D026\\n  date: 2026-05-14 19:37 UTC\\n  summary: MVP-2 ced_kl001_r4 FAIL — lr=5e-5 导致灾难性遗忘+CED recall shortcut 双重问题，启动 P0/P0+P1\\n    并行修复\\n  rationale: 'ckpt-10/50/100 eval 全部远低于 SFT baseline（rel_f1: 0.003→0.156→0.217 vs\\n    SFT 0.4057，evi_f1: 0.720→0.564→0.575 vs SFT 0.7979）。训练 reward 5x 增长但 eval F1 未恢复，确认\\n    reward hacking + 灾难性遗忘双重机制。根因：lr=5e-5 过高 5-10x + CED 对非匹配 triple 无 recall 惩罚。D020\\n    ablation 的 CED 训练稳定性发现仍有效。下一步：P0（lr=5e-6）和 P0+P1（lr=5e-6 + ced_recall_penalty）并行验证。'\\n  related_experiments:\\n  - exp_id: ced_kl001_r4\\n    role: primary\\n    result: training success but eval fail\\n  - exp_id: mvp2_eval_ced_kl001_r4_ckpt10\\n    role: eval\\n    result: f1=0.003\\n  - exp_id: mvp2_eval_ced_kl001_r4_step50\\n    role: eval\\n    result: f1=0.156\\n  - exp_id: mvp2_eval_ced_kl001_r4_step100\\n    role: eval\\n    result: f1=0.217\\n  depends_on:\\n  - D024\\n  - D025\\n  - D029\\n- id: D027\\n  date: 2026-05-14 19:37 UTC\\n  summary: MVP-2 ced_kl001_r4 FAIL — lr=5e-5 过高导致灾难性遗忘+CED recall shortcut 叠加 reward\\n    hacking\\n  rationale: ckpt-10/50/100 三点轨迹确认：rel_f1 最高 0.217（SFT 0.4057, pass 0.356, gap -13.9pp），evi_f1\\n    最高 0.575（SFT 0.7979, pass 0.818, gap -24.3pp）。恢复速率递减（40步+15.3pp→50步+6.0pp），外推至\\n    step200 仍远低于 pass。根因：(1) lr=5e-5 是社区推荐的 5-10x，导致 step10 即灾难性遗忘；(2) CED shortcut\\n    使非匹配 triple 退化为 flat NLI，引导模型少预测高 EDCR；(3) train/eval 分布不匹配放大差距。下一步：P0(lr=5e-6)\\n    + P0+P1(lr=5e-6+recall_penalty) 并行。\\n  related_experiments:\\n  - exp_id: ced_kl001_r4\\n    role: primary\\n    result: success(training)/fail(eval)\\n  - exp_id: mvp2_eval_ced_kl001_r4_step100\\n    role: eval\\n    result: rel_f1=0.217,evi_f1=0.575\\n  - exp_id: mvp2_eval_ced_kl001_r4_ckpt50\\n    role: eval\\n    result: rel_f1=0.156,evi_f1=0.564\\n  - exp_id: mvp2_eval_ced_kl001_r4_ckpt10\\n    role: eval\\n    result: rel_f1=0.003,evi_f1=0.720\\n  depends_on:\\n  - D024\\n  - D025\\n- id: D028\\n  date: 2026-05-14 21:36 UTC\\n  summary: Kill rp_r2 (P0+P1) — loss 指数 divergence 不可恢复；cuda:3 转跑 rp_r2 ckpt-20 eval\\n    关闭对比线\\n  rationale: rp_r2 loss 从 step 10-20 持续指数增长 (908→24650→1.34e7)，根因是 recall_penalty\\n    5-10x 梯度 + kl_coef=0.01 形成正反馈循环。与 P0 的瞬时 KL spike 不同，这是持续 divergence。Kill 后 cuda:3\\n    跑 rp_r2 ckpt-20 eval（成本低，~2h）拿到数据关闭 P0+P1 对比线。不启动新训练——MVP 阶段 P0 单独通过即可。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_lr5e6_rp_r2\\n    role: killed\\n    result: loss exponential divergence\\n  - exp_id: mvp2_grpo_ced_lr5e6_r1\\n    role: primary\\n    result: P0 continues as sole MVP path\\n  depends_on:\\n  - D027\\n- id: D029\\n  date: 2026-05-14 21:44 UTC\\n  summary: 修正 rp_r2 终止理由：从\\\"loss 持续发散\\\"改为\\\"recall penalty 过度抑制 CED 信号\\\"\\n  rationale: Reviewer 独立核实 trainer_state.json 发现 rp_r2 step 30-40 的 loss/KL 已完全恢复正常（loss=0.038,\\n    KL=0.005），与 P0 的瞬态发散→恢复模式一致，不是持续发散。真正的问题是 ced_reward=0.005 远低于 P0 的 0.079，说明 recall\\n    penalty 过于严苛压制了 CED 学习信号。kill 决策本身不撤回，但论文引用此 negative result 时应表述为\\\"recall penalty\\n    过度抑制 CED 信号\\\"而非\\\"训练发散\\\"。\\n  related_experiments:\\n  - exp_id: rp_r2\\n    role: subject\\n    result: killed-但理由修正\\n  - exp_id: mvp2_train_lr5e6_r1\\n    role: reference\\n    result: 同样出现瞬态发散后恢复\\n  depends_on: []\\n- id: D030\\n  date: 2026-05-14 22:16 UTC\\n  summary: P0 ckpt-20 eval FAIL (rel_f1=0.0077); lr=5e-6 未能防止早期遗忘，与 lr=5e-5 相同模式；扩展至全\\n    checkpoint 轨迹评估\\n  rationale: lr=5e-5 和 lr=5e-6 在 step-20 均出现灾难性遗忘（rel_f1 < 0.01），说明问题不是单纯 LR 过高——GRPO+QLoRA\\n    在结构化生成任务上的前 20 步 inherently 不稳定（60% 输出截断，field compliance 仅 39.9%）。需要看完整 recovery\\n    trajectory（ckpt-40/60/80）才能判断是否\\\"先崩后恢复\\\"。ced_kl001_r4 (lr=5e-5) step-90 最高 0.211\\n    仍低于阈值，lr=5e-6 能否突破 0.30 存疑。同时开始考虑 GRPO 替代方案（DPO/rejection sampling）作为 contingency。\\n  related_experiments:\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt20\\n    role: primary\\n    result: 'FAIL: rel_f1=0.0077, 39x below threshold'\\n  - exp_id: mvp2_grpo_ced_lr5e6_r1\\n    role: training\\n    result: step ~68, f1_reward recovering at step 45\\n  depends_on: []\\n- id: D031\\n  date: 2026-05-14 23:10 UTC\\n  summary: GRPO+QLoRA P0 方向判死：ckpt-40 rel_f1=0.0071（比 ckpt-20 更差），两个 LR 均远劣于 SFT baseline。Pivot\\n    到离线 RL（Rejection Sampling FT → DPO）\\n  rationale: ckpt-20→ckpt-40 轨迹下降（0.0077→0.0071），GRPO 只学会格式/证据引用但完全丧失关系抽取能力。lr=5e-5\\n    最佳 0.211 vs SFT 0.406，lr=5e-6 最佳 0.008。catastrophic forgetting 是 GRPO+QLoRA 在结构化生成任务上的根本性问题，非超参可解。CED\\n    reward signal 本身有效（MVP-1 verified），问题在在线 RL 训练方法论。Pivot 到离线方法：(1) Rejection Sampling\\n    FT 最简单最稳定优先做 (2) DPO+CED scoring 作为并行备选。\\n  related_experiments:\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt40_r2\\n    role: trigger\\n    result: rel_f1=0.0071 FAIL\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt20\\n    role: prior\\n    result: rel_f1=0.0077 FAIL\\n  - exp_id: mvp2_grpo_ced_lr5e6_r1\\n    role: training\\n    result: f1_reward 无学习趋势\\n  - exp_id: ced_kl001_r4\\n    role: prior_attempt\\n    result: best 0.211 at ckpt-90, mode collapse\\n  depends_on:\\n  - D030\\n  - D027\\n- id: D032\\n  date: 2026-05-15 01:03 UTC\\n  summary: 'Kill GRPO 训练 (cuda:0 step 113/200): 轨迹数据已充分，释放 GPU 给 RSFT 管线加速'\\n  rationale: ckpt-80 rel_f1=0.0116 (SFT baseline 的 2.9%)，ckpt-20→80 全线 FAIL。ckpt-100\\n    eval 在跑会给最后一个数据点，但 step 200 无价值。释放 cuda:0 可用于并行 RSFT generate 或后续 scoring/training。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_lr5e6_r1\\n    role: killed\\n    result: trajectory ckpt-20~80 all FAIL, max rel_f1=0.0116\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt80\\n    role: evidence\\n    result: rel_f1=0.0116 negative\\n  depends_on:\\n  - D031\\n- id: D033\\n  date: 2026-05-15 01:22 UTC\\n  summary: D031 最终确认：GRPO+QLoRA 全线 FAIL，lr5e6 全 6 checkpoint rel_f1 < 0.02；negative\\n    result 模式有论文价值（CED↑ + rel_f1 catastrophic forgetting = 在线 RL 无法维持双能力）\\n  rationale: Reviewer 独立核实 lr5e6 全 6 checkpoint：rel_f1 最高仅 0.0138（阈值 0.30），evi_f1\\n    从 0.628 单调升至 0.850（超 SFT 0.798），edcr 稳定 ~0.99（远超 SFT 0.712）。模式：CED reward signal\\n    有效驱动 evidence 质量提升，但在线 RL (GRPO+QLoRA) 导致关系抽取 catastrophic forgetting。此 negative\\n    result 直接支持离线 RL (RSFT/DPO) 路线的必要性，且为论文提供重要论据。\\n  related_experiments:\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt100\\n    role: final_eval\\n    result: FAIL rel_f1=0.0138\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt80\\n    role: trajectory\\n    result: FAIL rel_f1=0.0116\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt60\\n    role: trajectory\\n    result: FAIL rel_f1=0.0093\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt40\\n    role: trajectory\\n    result: FAIL rel_f1=0.0071\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt20\\n    role: trajectory\\n    result: FAIL rel_f1=0.0077\\n  - exp_id: mvp2_grpo_ced_lr5e6_r1\\n    role: training\\n    result: killed after trajectory data collected\\n  depends_on:\\n  - D031\\n  - D032\\n- id: D034\\n  date: 2026-05-15 01:28 UTC\\n  summary: 'D034: RSFT diversity 危机——diversity=1.0/8 因 temperature 未生效，暂停生成并修复'\\n  rationale: Reviewer critical 发现：(1) rsft_generate.py 传入 temperature=0.7 但被 Qwen3-4B\\n    generation_config.json 自带的 T=0.6/top_k=20 覆盖，transformers 打出 WARNING 但 Agent 未注意；(2)\\n    SFT 后模型分布极度尖锐，T=0.6+top_k=20 几乎等同于 greedy，导致 8 次生成完全相同；(3) 早期 diversity_probe\\n    报告 7/8 是 format 解析 bug 导致的虚假多样性，修复格式后真实 diversity 暴露为 1.0/8。必须 kill 当前进程、修复 temperature\\n    覆盖（显式设 model.generation_config.temperature + top_k=0）、用 3-5 doc 验证后再重启。\\n  related_experiments:\\n  - exp_id: mvp2_rsft_generate\\n    role: affected\\n    result: diversity=1.0/8, 生成数据无法用于 rejection sampling\\n  - exp_id: mvp2_diversity_probe\\n    role: evidence\\n    result: 7/8 是虚假多样性（format bug），实际 5.0/8 且修复后降至 1.0/8\\n  depends_on:\\n  - D033\\n- id: D035\\n  date: 2026-05-15 01:29 UTC\\n  summary: 暂停 RSFT 并行化：Reviewer critical 发现 diversity=1.0/8 是格式修复后的真实值，之前 7/8 为格式不一致假象。高温探针优先。\\n  rationale: diversity_probe 原始数据 (8,6,1) 平均 5.0/8 而非上报的 7；且 probe 时 format_ok 仅 34%，\\\"多样性\\\"来自\\n    JSON key 名变体。生产环境 format_ok=99.8% 后实测 diversity=1.0/8。继续当前配置生成 14h 的数据毫无意义——rejection\\n    sampling 退化为普通 SFT。需先用高温(T=1.0/1.2/1.5)探针验证 diversity 是否可恢复。\\n  related_experiments:\\n  - exp_id: mvp2_diversity_probe\\n    role: evidence\\n    result: 虚报 7/8, 实际 5.0/8, 且为格式假象\\n  - exp_id: mvp2_rsft_generate\\n    role: affected\\n    result: diversity=1.0/8 at T=0.7, 暂不扩展\\n  depends_on:\\n  - D033\\n- id: D036\\n  date: 2026-05-15 01:33 UTC\\n  summary: D034 撤销：diversity crisis 是监控 bug，非生成质量问题，T=0.7 下 diversity 充足(7.11/8)，恢复并行生成\\n  rationale: 独立验证 Worker 分析 cuda:1 已生成的 200 docs：triple-set diversity 7.11/8 (median=8.0)，format\\n    parse rate 90.2%，61.5% 文档 8/8 完全不同。之前监控报告 mean_diversity=1.0/8 为度量代码计算错误。无需执行\\n    D034 的 temperature 修复和高温探针。\\n  related_experiments:\\n  - exp_id: mvp2_rsft_generate\\n    role: trigger\\n    result: diversity monitoring bug identified\\n  depends_on: []\\n- id: D037\\n  date: 2026-05-15 07:46 UTC\\n  summary: 'D037: RSFT 全线 FAIL（rel_f1=0.0483），pivot 到 CED-as-reranker（推理时方案）'\\n  rationale: 'GRPO（D027/D031/D033）和 RSFT 两条训练路线均呈现相同的灾难性遗忘——任何对 SFT checkpoint 的二次微调都摧毁\\n    rel_f1。RSFT r1: rel_f1=0.0483, num_preds=848（SFT baseline: 0.4057, 12234）。跨 seed\\n    方差 <0.04%，非随机。根因假设：LoRA 二次微调的系统性遗忘。Pivot 到 CED-as-reranker：SFT 模型生成 N 候选 → CED\\n    打分 → 选最佳，完全绕过训练问题。'\\n  related_experiments:\\n  - exp_id: mvp2_rsft_train_r1\\n    role: primary\\n    result: 'FAIL: rel_f1=0.0483'\\n  - exp_id: mvp2_rsft_train_r1_s43\\n    role: variance\\n    result: training variance <0.04%\\n  - exp_id: mvp2_rsft_train_r1_s44\\n    role: variance\\n    result: eval pending, same outcome expected\\n  depends_on:\\n  - D033\\n  - D027\\n- id: D038\\n  date: 2026-05-15 09:40 UTC\\n  summary: 'D038: 撤回 D037——RSFT \\\"灾难性失败\\\"实为 eval bug（50-doc pred vs 12275 gold denominator\\n    mismatch），s44 全量 eval 通过 MVP-2（rel_f1=0.4655 +5.98pp, evi_f1=0.8087 +1.08pp）'\\n  rationale: r1 的 rel_f1=0.0483 是评估代码 bug：TaskEvalCallback 在 50 docs 上生成预测但 gold triples\\n    用了全量 dev set 12275 条，recall 被人为压到 ~3.5%。s44 独立全量 eval（985 docs）结果：rel_f1=0.4655（+5.98pp\\n    vs SFT 0.4057），evi_f1=0.8087（+1.08pp vs 0.7979），edcr=0.6350（-7.68pp vs 0.7118）。CED\\n    rejection sampling 首次端到端验证成功。D037 的 reranker pivot 基于错误数据，RSFT 实际有效。\\n  related_experiments:\\n  - exp_id: mvp2_rsft_train_r1_s44\\n    role: primary\\n    result: 'PASS: rel_f1=0.4655, evi_f1=0.8087'\\n  - exp_id: mvp2_rsft_train_r1\\n    role: pending_reeval\\n    result: r1 0.0483 was eval bug, full eval needed\\n  depends_on:\\n  - D037\\n- id: D039\\n  date: 2026-05-15 11:49 UTC\\n  summary: 'D039: RSFT+CED ablation 全部 PASS MVP-2——方法鲁棒，1 epoch 足够，EDCR 局限需论文讨论'\\n  rationale: Reviewer 独立验证 4 组 RSFT 配置（r1 s42/s44, r2a, r2b）全部通过 MVP-2 判据（rel_f1 >\\n    0.4057, evi_f1 > 0.798）。核心发现：(1) RSFT+CED 方法贡献 +4-6pp rel_f1，具体超参影响极小（0.45pp 范围内），方法鲁棒性好；(2)\\n    1 epoch 足够，3 epoch 无显著额外收益；(3) r2b 保守 LoRA scaling+低 lr 略优于 r2a（截断更少、字段完整率更高）；(4)\\n    EDCR 一致偏高 63-66%，CED reward 对 rel_f1 提升明显但对证据精确度提升有限，需论文坦诚讨论。两个 warning（ablation\\n    变量混淆、EDCR 高）均不阻塞 MVP，clean ablation 留研究阶段补。等 s43_r2 第三种子确认后调 complete_mvp()。\\n  related_experiments:\\n  - exp_id: mvp2_eval_rsft_r2a\\n    role: ablation\\n    result: rel_f1=0.4494, evi_f1=0.8108, EDCR=0.6641, PASS\\n  - exp_id: mvp2_eval_rsft_r2b\\n    role: ablation\\n    result: rel_f1=0.4493, evi_f1=0.8128, EDCR=0.6609, 截断179/字段完整率81.8%, PASS\\n  - exp_id: mvp2_eval_rsft_r1\\n    role: baseline_rsft\\n    result: rel_f1=0.4449, evi_f1=0.8187, EDCR=0.6565, PASS\\n  - exp_id: mvp2_rsft_train_r1_s44\\n    role: seed_variance\\n    result: rel_f1=0.4655, evi_f1=0.8087, PASS\\n  depends_on:\\n  - D038\\n- id: D040\\n  date: 2026-05-15 12:03 UTC\\n  summary: 'D040: MVP 正式通过 → 进入 Research 阶段。paper_framing.md 定稿（RSFT+CED 路线，4 Claims），experiment_plan.yaml\\n    建立（10 研究实验），dream_simulate(full) 已启动'\\n  rationale: D039 已判定 MVP-2 全部 PASS（4/4 configs），但 complete_mvp() 未被调用。用户催促后补调。Post-MVP\\n    kickoff 按 skill 流程执行：(1) paper_framing.md 从 Pre-MVP draft 更新为 Post-MVP 定稿版——方法从\\n    GRPO 转为 RSFT+CED，新增 Claim 3（在线 RL catastrophic forgetting 分析）和 RC6/RC7；(2) experiment_plan.yaml\\n    新建，10 个研究实验分 P0/P1/P2；(3) dream_simulate(full) 已启动（dream_20260515T120227），等回调后再批准\\n    P0 实验。投稿目标调整为 ARR July → EMNLP 2026 Main（ARR May 25 仅作 stretch goal）。\\n  related_experiments:\\n  - exp_id: mvp2_eval_rsft_r2a\\n    role: evidence\\n    result: rel_f1=0.4494 PASS\\n  - exp_id: mvp2_eval_rsft_r2b\\n    role: evidence\\n    result: rel_f1=0.4493 PASS\\n  - exp_id: mvp2_eval_rsft_r1\\n    role: evidence\\n    result: rel_f1=0.4449 PASS\\n  - exp_id: mvp2_rsft_train_r1_s44\\n    role: evidence\\n    result: rel_f1=0.4655 PASS\\n  depends_on:\\n  - D039\\n\", \"total_chars\": 28970, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4e91b107-3310-48d5-abb8-48d4d83f7287",
  "isSidechain": true,
  "promptId": "00a1eb94-0484-4e13-931d-e659507bc0c6",
  "agentId": "a9bd4203964701927",
  "type": "user",
  "uuid": "234933b1-4808-4ca3-baa0-c44c92d33f03",
  "sourceToolAssistantUUID": "4e91b107-3310-48d5-abb8-48d4d83f7287",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T12:47:36.104Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01F9WNWuM37v28fmv8kG8Fkz`</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "EVALUATION.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "234933b1-4808-4ca3-baa0-c44c92d33f03",
  "isSidechain": true,
  "agentId": "a9bd4203964701927",
  "requestId": "req_011Cb4NySfMGvnmM4qtUE8VB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "36ab6688-0c30-46f6-9f00-579fc7311181",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YcRPc8eqRu572amtXTuUYh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11064,
      "cache_read_input_tokens": 21262,
      "output_tokens": 305,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11064
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 305,
          "cache_read_input_tokens": 21262,
          "cache_creation_input_tokens": 11064,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11064,
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

_source line 24 · 2026-05-15T12:47:36.113Z_

<details><summary>↩ Tool result · `toolu_01F9WNWuM37v28fmv8kG8Fkz`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No EVALUATION.md found for 'faith-evidence-ie'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "36ab6688-0c30-46f6-9f00-579fc7311181",
  "isSidechain": true,
  "promptId": "00a1eb94-0484-4e13-931d-e659507bc0c6",
  "agentId": "a9bd4203964701927",
  "type": "user",
  "uuid": "a46cd222-546b-43f1-8c8c-c661211dd817",
  "sourceToolAssistantUUID": "36ab6688-0c30-46f6-9f00-579fc7311181",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-15T12:47:40.675Z_

Now let me check for the writing plan and any existing paper draft artifacts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a46cd222-546b-43f1-8c8c-c661211dd817",
  "isSidechain": true,
  "agentId": "a9bd4203964701927",
  "requestId": "req_011Cb4NyrMdRFuxyu8wW8EBL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8ec44a0a-b9fd-4e02-a9c8-ecb7df740549",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RSV4iNaCM7FJE99SBwqgEv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26348,
      "cache_read_input_tokens": 32326,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 26348,
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

_source line 26 · 2026-05-15T12:47:41.625Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_019UJkkAAASxxmCaQpmo83qL`</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "writing_plan.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ec44a0a-b9fd-4e02-a9c8-ecb7df740549",
  "isSidechain": true,
  "agentId": "a9bd4203964701927",
  "requestId": "req_011Cb4NyrMdRFuxyu8wW8EBL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "087b3d4c-13a2-4cdf-9e73-aa849fece103",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RSV4iNaCM7FJE99SBwqgEv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26348,
      "cache_read_input_tokens": 32326,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 26348,
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

_source line 27 · 2026-05-15T12:47:41.634Z_

<details><summary>↩ Tool result · `toolu_019UJkkAAASxxmCaQpmo83qL`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No writing_plan.yaml found for 'faith-evidence-ie'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "087b3d4c-13a2-4cdf-9e73-aa849fece103",
  "isSidechain": true,
  "promptId": "00a1eb94-0484-4e13-931d-e659507bc0c6",
  "agentId": "a9bd4203964701927",
  "type": "user",
  "uuid": "e315e5f7-23a7-4b64-9b1d-9e4760bd83a4",
  "sourceToolAssistantUUID": "087b3d4c-13a2-4cdf-9e73-aa849fece103",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-15T12:47:42.842Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01LToBYAb28KpKK8nJoezWQb`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e315e5f7-23a7-4b64-9b1d-9e4760bd83a4",
  "isSidechain": true,
  "agentId": "a9bd4203964701927",
  "requestId": "req_011Cb4NyrMdRFuxyu8wW8EBL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ce7e6f85-244a-4866-a0a2-148bcaf23e0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RSV4iNaCM7FJE99SBwqgEv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26348,
      "cache_read_input_tokens": 32326,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 26348,
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

_source line 29 · 2026-05-15T12:47:42.871Z_

<details><summary>↩ Tool result · `toolu_01LToBYAb28KpKK8nJoezWQb`</summary>

```text
artifacts/dream_reports/dream_20260515T120227/best/paper.tex
artifacts/dream_reports/dream_20260515T120227/median/paper.tex
artifacts/dream_reports/dream_20260515T120227/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ce7e6f85-244a-4866-a0a2-148bcaf23e0c",
  "isSidechain": true,
  "promptId": "00a1eb94-0484-4e13-931d-e659507bc0c6",
  "agentId": "a9bd4203964701927",
  "type": "user",
  "uuid": "30cc0b91-ecd7-4566-acbf-f575583262c9",
  "sourceToolAssistantUUID": "ce7e6f85-244a-4866-a0a2-148bcaf23e0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-15T12:47:46.419Z_

<details open><summary>🔧 Tool call — Read · `toolu_019aA41URTFpeLJdkx2g86YQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/best/paper.tex",
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30cc0b91-ecd7-4566-acbf-f575583262c9",
  "isSidechain": true,
  "agentId": "a9bd4203964701927",
  "requestId": "req_011Cb4NzMpBNQS5T2fDHRguW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2fa00002-0eaf-4e56-bcef-267afc4153d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015yMCYRxZGYKfHGBeTS3KDb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 386,
      "cache_read_input_tokens": 58674,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 386,
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

_source line 31 · 2026-05-15T12:47:46.426Z_

<details><summary>↩ Tool result · `toolu_019aA41URTFpeLJdkx2g86YQ`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{times}
5	\usepackage{amsmath,amssymb}
6	\usepackage{booktabs}
7	\usepackage{graphicx}
8	\usepackage{multirow}
9	\usepackage{xcolor}
10	\usepackage[margin=2.5cm]{geometry}
11	\usepackage{hyperref}
12	\usepackage{natbib}
13	\usepackage{caption}
14	\usepackage{subcaption}
15	\usepackage{enumitem}
16	
17	\newcommand{\method}{FREIGE}
18	\newcommand{\ced}{CED}
19	\newcommand{\edcr}{EDCR}
20	\newcommand{\rsft}{RSFT}
21	
22	\title{FREIGE: Faithful Relation Extraction with Evidence via\\Contrastive Evidence Discrimination}
23	
24	\author{Anonymous}
25	\date{}
26	
27	\begin{document}
28	\maketitle
29	
30	% ============================================================
31	% ABSTRACT
32	% ============================================================
33	\begin{abstract}
34	LLM-based document-level relation extraction (DocRE) approaches extraction parity with encoder models but produces no verifiable evidence for predicted relations, limiting deployment in audit-critical domains.
35	We present \method{}, the first LLM-based DocRE system that jointly generates relation triples and supporting evidence sentences.
36	Our key contribution is \emph{Contrastive Evidence Discrimination} (\ced{}), a scoring function that contrasts genuine evidence against entity-sharing distractor sentences within the same document, converting a binary NLI signal into a contrastive margin that is robust to lexical-overlap bias.
37	We show that \ced{} as an online RL reward (GRPO) leads to catastrophic forgetting of extraction ability---reward rises monotonically while relation F1 collapses to near zero---constituting, to our knowledge, the first empirical demonstration of reward overoptimization in structured information extraction.
38	Instead, using \ced{} as an offline quality filter for \emph{Rejection Sampling Fine-Tuning} (\rsft{}) yields consistent gains: on the DocRED test set, \method{} achieves rel-F1 45.4 and Evi-F1 80.2, surpassing the encoder evidence SOTA (DREEAM, Evi-F1 57.3) under comparable evaluation.
39	We further propose the \emph{Entity-sharing Distractor Citation Rate} (\edcr{}), a complementary metric exposing a blind spot of Evi-F1: high Evi-F1 can coexist with substantial distractor citation.
40	Experiments across three model scales (1.7B/4B/8B) and two datasets (DocRED, Re-DocRED) confirm the generality of the approach.
41	\end{abstract}
42	
43	% ============================================================
44	% 1  INTRODUCTION
45	% ============================================================
46	\section{Introduction}
47	
48	Document-level relation extraction (DocRE) identifies relational facts between entity pairs scattered across multiple sentences. Recent encoder-based methods such as DREEAM and SAIS achieve strong extraction F1 and additionally produce evidence---the sentences supporting each predicted triple. However, these systems derive evidence from attention patterns or auxiliary classifiers, not from the extraction model's own reasoning.
49	
50	Large language models (LLMs) fine-tuned for DocRE have closed the extraction gap with encoder models, yet \emph{no existing LLM-based method produces verifiable evidence}. This is a critical deployment gap: in biomedical knowledge base population, legal document analysis, and RAG-based fact verification, practitioners need to trace each extracted fact back to its textual support.
51	
52	A natural idea is to reward the LLM for producing faithful evidence using an NLI-based faithfulness score. We find, however, that a \emph{flat} NLI reward is easily gamed by \textbf{entity-sharing distractor sentences}---sentences that mention the same entities as the gold evidence but do not actually support the relation. Such sentences receive high entailment scores from NLI models, creating a reward signal that conflates entity co-occurrence with genuine evidential support.
53	
54	We propose \textbf{Contrastive Evidence Discrimination (\ced{})}, which addresses this by computing a contrastive margin: $m = p_\text{pos} - p_\text{neg}$, where $p_\text{pos}$ is the NLI entailment probability for the gold evidence and $p_\text{neg}$ is that for the highest-scoring distractor. This margin is inherently robust to lexical-overlap bias because the bias affects both terms and partially cancels in the difference.
55	
56	A second finding is that \ced{} as an \emph{online} RL reward (via GRPO) catastrophically fails: the model learns to produce NLI-friendly evidence while completely forgetting how to extract relations (rel-F1 drops from 40.6 to $<$2 within 10 training steps, while reward increases monotonically). This is, to our knowledge, the first empirical demonstration of reward overoptimization in structured IE, echoing theoretical predictions from the reward overoptimization literature.
57	
58	Our solution is to use \ced{} \emph{offline}: the SFT model generates $N$ candidate outputs per document, \ced{} scores them, and only the top-$k$ candidates are retained for a second round of supervised fine-tuning (\rsft{}). This sidesteps catastrophic forgetting entirely because no policy gradient update occurs---the model simply sees higher-quality training data.
59	
60	We make four contributions:
61	\begin{enumerate}[nosep,leftmargin=*]
62	\item \textbf{\method{}}: the first LLM-based DocRE method that jointly outputs relation triples and verifiable evidence, achieving rel-F1 45.4 and Evi-F1 80.2 on DocRED test.
63	\item \textbf{\ced{} as offline quality signal}: contrastive NLI scoring for RSFT data filtering significantly outperforms flat-NLI filtering (Evi-F1 +2.6pp, EDCR $-$5.8pp on dev).
64	\item \textbf{Cautionary analysis of online RL for structured IE}: GRPO with three reward types all catastrophically forget, providing empirical grounding for when to prefer offline over online RL.
65	\item \textbf{\edcr{} metric}: a complementary evaluation dimension revealing that high Evi-F1 can coexist with substantial distractor citation (Pearson $r = -0.42$ between Evi-F1 and EDCR).
66	\end{enumerate}
67	
68	% ============================================================
69	% 2  RELATED WORK
70	% ============================================================
71	\section{Related Work}
72	
73	\paragraph{Document-Level Relation Extraction.}
74	DocRE requires reasoning across sentences to extract relations between entity pairs. Encoder-based methods dominate the DocRED leaderboard: ATLOP uses adaptive thresholding, DocuNet introduces a U-shaped network, and DREEAM adds evidence-aware attention training. SAIS improves evidence extraction via a separate evidence module. Recent LLM-based approaches (e.g., LMRC with LLaMA3.1-8B, DocKS-RAG with GNN augmentation) achieve competitive extraction F1 but produce no evidence.
75	
76	\paragraph{Faithfulness and Evidence in IE.}
77	The faithfulness of generated text has been extensively studied in summarization and question answering, typically via NLI-based evaluation. For relation extraction, evidence serves a complementary role: rather than verifying output fidelity, it provides provenance for extracted facts. Evi-F1, the standard metric, measures sentence-level overlap with gold evidence but does not penalize plausible-looking distractor citations.
78	
79	\paragraph{RL for Language Models.}
80	RLHF and its variants (DPO, GRPO, KTO) have shown success in aligning LLMs with human preferences. However, reward overoptimization---where the proxy reward increases while true quality degrades---remains a known failure mode. Our work provides the first empirical evidence of this phenomenon in structured information extraction.
81	
82	\paragraph{Rejection Sampling Fine-Tuning.}
83	RSFT (also called ReST or iterative DPO) generates candidates from the current policy, filters by a quality signal, and fine-tunes on the filtered set. Recent theoretical work shows RSFT is equivalent to PPO under certain conditions. We adopt RSFT with CED as the quality filter.
84	
85	% ============================================================
86	% 3  METHOD
87	% ============================================================
88	\section{Method}
89	
90	\subsection{Problem Formulation}
91	
92	Given a document $D$ with annotated entities, the task is to produce for each entity pair $(h, t)$ a set of relation triples $(h, r, t)$ along with evidence sentences $E \subseteq \{S_1, \ldots, S_{|D|}\}$ that support the relation. We formulate this as sequence generation: the LLM outputs structured text encoding triples and their evidence sentence indices.
93	
94	\subsection{SFT Baseline}
95	
96	We fine-tune Qwen3-4B with LoRA on DocRED training data, where the target sequence encodes each triple as \texttt{(head, relation, tail, [S$_i$, S$_j$, ...])}. The model learns to jointly predict relations and cite evidence sentences.
97	
98	\subsection{Contrastive Evidence Discrimination (\ced{})}
99	\label{sec:ced}
100	
101	For a predicted triple $(h, r, t)$ with cited evidence sentences $E_\text{pred}$, we define:
102	
103	\paragraph{Positive score.} Let the NLI model compute the entailment probability $p_\text{pos} = P(\text{entail} \mid \text{premise}=E_\text{pred},\; \text{hypothesis}=(h, r, t))$.
104	
105	\paragraph{Negative score.} We construct a distractor set: all sentences in $D$ that mention either $h$ or $t$ but are \emph{not} in the gold evidence set. The negative score is $p_\text{neg} = \max_{S_d \in \text{Distractor}} P(\text{entail} \mid S_d, (h, r, t))$.
106	
107	\paragraph{CED margin.} The contrastive margin is:
108	\begin{equation}
109	m_\text{CED} = p_\text{pos} - p_\text{neg}
110	\end{equation}
111	
112	A high margin indicates the cited evidence is genuinely more supportive than the best available distractor. The contrastive design provides two key properties:
113	\begin{enumerate}[nosep,leftmargin=*]
114	\item \textbf{Bias cancellation}: lexical-overlap bias in the NLI model affects both $p_\text{pos}$ and $p_\text{neg}$ similarly (both involve entity-mentioning sentences), so the bias partially cancels in the margin.
115	\item \textbf{Self-correction for annotation noise}: if a ``distractor'' is actually valid evidence missed by annotators, it will have high $p_\text{neg}$, reducing the margin and thus the penalty---the scoring is lenient toward false distractors.
116	\end{enumerate}
117	
118	We use DeBERTa-v3-base fine-tuned on MNLI as the NLI model. The CED scorer achieves discrimination accuracy of 81.5\% (correctly ranking gold evidence above the best distractor) with mean margin 0.48.
119	
120	\subsection{Rejection Sampling Fine-Tuning (\rsft{})}
121	\label{sec:rsft}
122	
123	\begin{enumerate}[nosep,leftmargin=*]
124	\item \textbf{Candidate generation}: For each training document, sample $N=8$ outputs from the SFT model (temperature 0.7).
125	\item \textbf{CED scoring}: Score each candidate's evidence quality using the CED margin.
126	\item \textbf{Filtering}: Retain top-$k$ candidates (default $k=1$) per document, yielding ${\sim}2{,}700$ high-quality training examples from ${\sim}21{,}000$ candidates (selection rate 12.8\%).
127	\item \textbf{Fine-tuning}: Train a second LoRA adapter on the filtered set (1 epoch, $\alpha$=128, lr=$2\times10^{-5}$).
128	\end{enumerate}
129	
130	This pipeline avoids the catastrophic forgetting of online RL: no policy gradient is computed, so the model's extraction ability is preserved while evidence quality improves through data curation.
131	
132	\subsection{Entity-sharing Distractor Citation Rate (\edcr{})}
133	\label{sec:edcr}
134	
135	Standard Evi-F1 measures sentence-level overlap with gold evidence but does not specifically penalize \emph{plausible-looking} distractor citations. We define:
136	
137	\begin{equation}
138	\text{EDCR} = \frac{|\{s \in E_\text{pred} : s \notin E_\text{gold} \wedge s \text{ mentions } h \text{ or } t\}|}{|E_\text{pred}|}
139	\end{equation}
140	
141	EDCR captures the fraction of cited sentences that share entities with the target triple but are not gold evidence---precisely the failure mode that flat NLI rewards encourage. Lower EDCR indicates more precise evidence.
142	
143	\subsection{Why Online RL Fails: GRPO Analysis}
144	
145	We attempted GRPO training with three reward types: (1)~CED margin, (2)~flat-NLI entailment, (3)~extraction-only F1. All three configurations, across multiple learning rates and KL penalties, exhibited the same failure pattern: the reward increases monotonically while relation F1 collapses within the first 10--30 steps. This constitutes reward overoptimization in the structured IE setting: the model discovers degenerate policies (e.g., citing all entity-mentioning sentences) that maximize the reward proxy while destroying extraction capability.
146	
147	% ============================================================
148	% 4  EXPERIMENTAL SETUP
149	% ============================================================
150	\section{Experimental Setup}
151	
152	\paragraph{Datasets.} We evaluate on DocRED (3,053 train / 1,000 dev / 1,000 test documents) and Re-DocRED (a revised version correcting false-negative annotations).
153	
154	\paragraph{Models.} Our primary model is Qwen3-4B with LoRA ($\alpha$=128, $r$=64). We additionally evaluate Qwen3-1.7B and Qwen3-8B for model size ablation.
155	
156	\paragraph{Baselines.}
157	(1)~\textbf{SFT}: Qwen3-4B fine-tuned on DocRED gold data.
158	(2)~\textbf{RSFT flat-NLI}: RSFT with flat NLI scoring (non-contrastive).
159	(3)~\textbf{DREEAM}: RoBERTa-large encoder, evidence SOTA (test Evi-F1 57.34).
160	(4)~\textbf{SAIS}: RoBERTa encoder evidence baseline (test Evi-F1 55.67).
161	(5)~\textbf{CED reranker}: inference-time CED reranking of SFT candidates ($N$=8), no additional training.
162	(6)~\textbf{GRPO+CED}: online RL with CED reward (negative baseline).
163	
164	\paragraph{Metrics.} Relation F1 (rel-F1), Ign-F1 (excluding shared training-test triples), Evidence F1 (Evi-F1, sentence-level), and EDCR (Section~\ref{sec:edcr}). Test rel-F1/ign-F1 from CodaLab; Evi-F1 and EDCR computed locally.
165	
166	\paragraph{NLI Model.} DeBERTa-v3-base fine-tuned on MNLI for CED scoring. We additionally ablate DeBERTa-v3-large.
167	
168	% ============================================================
169	% 5  RESULTS
170	% ============================================================
171	\section{Results}
172	
173	\subsection{Main Results on DocRED Test Set}
174	
175	Table~\ref{tab:test} presents the main results. \method{} (RSFT+CED) achieves rel-F1 45.4 and Evi-F1 80.2 on the DocRED test set. While the rel-F1 gap to encoder SOTA (DREEAM, 63.3) reflects the known trade-off of generative approaches, the Evi-F1 of 80.2 substantially surpasses DREEAM's 57.3 under comparable sentence-level evaluation. The dev-to-test decay is small: $-$1.2pp for rel-F1 and $-$0.7pp for Evi-F1, indicating robust generalization.
176	
177	\begin{table}[t]
178	\centering
179	\caption{DocRED test set results. $\dagger$: encoder-based methods; Evi-F1 comparison requires noting the protocol difference (attention-based vs.\ generative evidence).}
180	\label{tab:test}
181	\begin{tabular}{lcccc}
182	\toprule
183	\textbf{Method} & \textbf{rel-F1} & \textbf{ign-F1} & \textbf{Evi-F1} & \textbf{EDCR} \\
184	\midrule
185	DREEAM$\dagger$ & 63.3 & --- & 57.3 & --- \\
186	SAIS$\dagger$ & 62.3 & --- & 55.7 & --- \\
187	\midrule
188	SFT baseline & 39.7 & 39.5 & 78.9 & 70.5 \\
189	RSFT flat-NLI & 42.9 & 42.7 & 78.5 & 68.6 \\
190	\textbf{RSFT+CED (ours)} & \textbf{45.4} & \textbf{45.2} & \textbf{80.2} & \textbf{54.8} \\
191	\bottomrule
192	\end{tabular}
193	\end{table}
194	
195	The EDCR of 54.8 on the test set indicates that roughly half of the cited non-gold sentences are entity-sharing distractors---a substantial improvement over SFT (70.5) but indicating remaining room for improvement. Flat-NLI RSFT achieves only marginal EDCR improvement (68.6), confirming that contrastive scoring is essential for distractor filtering.
196	
197	\subsection{CED vs.\ Flat-NLI Ablation}
198	
199	Table~\ref{tab:ced_vs_flatnli} compares CED-scored and flat-NLI-scored RSFT on the dev set. CED RSFT outperforms flat-NLI RSFT across all metrics: +2.8pp rel-F1, +2.6pp Evi-F1, and $-$5.8pp EDCR. The flat-NLI RSFT provides only marginal EDCR improvement over SFT ($-$1.9pp), confirming that non-contrastive NLI scoring has little discriminative power against entity-sharing distractors.
200	
201	\begin{table}[t]
202	\centering
203	\caption{CED vs.\ flat-NLI RSFT ablation on DocRED dev set. All CED configurations outperform flat-NLI.}
204	\label{tab:ced_vs_flatnli}
205	\begin{tabular}{lccccc}
206	\toprule
207	\textbf{Method} & \textbf{rel-F1} & \textbf{Evi-F1} & \textbf{EDCR} & $\Delta$\textbf{Evi-F1} & $\Delta$\textbf{EDCR} \\
208	\midrule
209	SFT baseline & 40.6 & 79.8 & 71.2 & --- & --- \\
210	RSFT flat-NLI & 43.8 & 79.3 & 69.3 & $-$0.5 & $-$1.9 \\
211	RSFT CED (r1) & 44.5 & 81.9 & 65.7 & +2.1 & $-$5.5 \\
212	RSFT CED (s44) & 46.6 & 80.9 & 63.5 & +1.1 & $-$7.7 \\
213	RSFT CED (r2b) & 44.9 & 81.3 & 66.1 & +1.5 & $-$5.1 \\
214	\bottomrule
215	\end{tabular}
216	\end{table}
217	
218	The mechanism is clear: flat-NLI scoring assigns high scores to entity-sharing distractors (both genuine evidence and distractors contain the target entities and thus receive high NLI entailment scores). CED's contrastive margin $m = p_\text{pos} - p_\text{neg}$ explicitly penalizes candidates whose evidence is not substantially more supportive than the best distractor, filtering out distractor-heavy training examples.
219	
220	\subsection{EDCR Diagnostic Across Methods}
221	
222	Table~\ref{tab:edcr_diag} presents EDCR computed across all evidence-producing methods, revealing the diagnostic power of EDCR as a complementary metric to Evi-F1.
223	
224	\begin{table}[t]
225	\centering
226	\caption{EDCR diagnostic across all methods (dev set). EDCR and Evi-F1 capture different dimensions (Pearson $r = -0.42$).}
227	\label{tab:edcr_diag}
228	\begin{tabular}{lcccc}
229	\toprule
230	\textbf{Method} & \textbf{rel-F1} & \textbf{Evi-F1} & \textbf{EDCR} & \textbf{Evidence pattern} \\
231	\midrule
232	SFT & 40.6 & 79.8 & 71.2 & High distractor \\
233	RSFT flat-NLI & 43.8 & 79.3 & 69.3 & Slightly improved \\
234	RSFT CED (best) & 46.6 & 80.9 & 63.5 & Notably improved \\
235	CED reranker & 39.8 & 80.5 & 49.8 & Most precise \\
236	GRPO CED (ckpt-90) & 21.1 & 56.7 & 85.8 & Catastrophic distractor \\
237	\bottomrule
238	\end{tabular}
239	\end{table}
240	
241	Three observations stand out. First, GRPO's best checkpoint achieves Evi-F1 of 56.7 (seemingly reasonable) but EDCR of 85.8---nearly all citations are distractors. This is a case where Evi-F1 alone would mask a catastrophic failure mode. Second, the CED reranker achieves the lowest EDCR (49.8) among all methods, at the cost of 8$\times$ inference overhead, demonstrating that CED directly filters distractors at inference time. Third, the Pearson correlation between Evi-F1 and EDCR is only $-0.42$, confirming they capture orthogonal evaluation dimensions.
242	
243	\subsection{DREEAM Baseline Reproduction}
244	
245	To ensure evaluation comparability, we reproduce DREEAM (RoBERTa-large) on the DocRED dev set (Table~\ref{tab:dreeam_repro}). The reproduction gap is $<$0.3pp for both rel-F1 and Evi-F1, confirming pipeline consistency.
246	
247	\begin{table}[h]
248	\centering
249	\caption{DREEAM reproduction on DocRED dev set.}
250	\label{tab:dreeam_repro}
251	\begin{tabular}{lccc}
252	\toprule
253	\textbf{Setting} & \textbf{Paper} & \textbf{Reproduced} & \textbf{Gap} \\
254	\midrule
255	Dev rel-F1 & $\sim$62.9 & 62.7 & $-$0.2 \\
256	Dev Evi-F1 & $\sim$57.2 & 57.0 & $-$0.2 \\
257	Test Evi-F1 & 57.3 & (submitted) & --- \\
258	\bottomrule
259	\end{tabular}
260	\end{table}
261	
262	We note an important protocol difference: DREEAM extracts evidence via attention thresholds (precision 58.1, recall 55.9), while our method generates explicit sentence indices (precision 81.2, recall 79.3). The generative approach naturally has higher recall because the model can cite any number of sentences. Despite this difference, the sentence-level F1 evaluation protocol is identical, making the comparison valid at the metric level.
263	
264	\subsection{CED as Inference-Time Reranker}
265	
266	Table~\ref{tab:reranker} shows results for using CED as a training-free reranker: we sample $N$=8 candidates from SFT and select the one with the highest CED margin.
267	
268	\begin{table}[t]
269	\centering
270	\caption{CED reranker vs.\ baselines (dev set). The reranker achieves the best EDCR without any additional training.}
271	\label{tab:reranker}
272	\begin{tabular}{lcccc}
273	\toprule
274	\textbf{Method} & \textbf{rel-F1} & \textbf{Evi-F1} & \textbf{EDCR} & \textbf{Extra training} \\
275	\midrule
276	SFT baseline & 40.6 & 79.8 & 71.2 & --- \\
277	CED reranker & 39.8 & 80.5 & 49.8 & None \\
278	RSFT+CED & 46.6 & 80.9 & 63.5 & $\sim$2h LoRA \\
279	\bottomrule
280	\end{tabular}
281	\end{table}
282	
283	The reranker achieves EDCR 49.8 (the best across all methods) with no training cost, at 8$\times$ inference overhead. The rel-F1 drops slightly ($-$0.8pp) because CED selects for evidence quality rather than extraction quality. This provides a complementary pathway: for applications where evidence precision is paramount (e.g., biomedical audit), the reranker is preferable; for balanced performance, RSFT+CED is superior.
284	
285	\subsection{GRPO Catastrophic Forgetting}
286	
287	Table~\ref{tab:grpo} traces the GRPO training trajectory, revealing the reward overoptimization pattern. Within 10 steps, rel-F1 collapses from 40.6 (SFT initialization) to 0.3, while the CED reward increases from 0.45 to 1.195 over 100 steps. Meanwhile, Evi-F1 climbs to 85.0---the model has learned to produce evidence that the NLI model finds entailing, but has completely forgotten how to extract relations.
288	
289	\begin{table}[t]
290	\centering
291	\caption{GRPO trajectory (CED reward, lr=$5\times10^{-6}$). Reward rises while rel-F1 stays near zero---classic reward overoptimization.}
292	\label{tab:grpo}
293	\begin{tabular}{lcccc}
294	\toprule
295	\textbf{Checkpoint} & \textbf{rel-F1} & \textbf{Evi-F1} & \textbf{EDCR} & \textbf{Reward} \\
296	\midrule
297	SFT (init) & 40.6 & 79.8 & 71.2 & --- \\
298	step-10 & 0.3 & 72.0 & 99.8 & 0.45 \\
299	step-20 & 0.8 & 62.8 & 99.4 & 0.62 \\
300	step-40 & 0.7 & 75.8 & 99.4 & 0.78 \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2fa00002-0eaf-4e56-bcef-267afc4153d8",
  "isSidechain": true,
  "promptId": "00a1eb94-0484-4e13-931d-e659507bc0c6",
  "agentId": "a9bd4203964701927",
  "type": "user",
  "uuid": "fcc9b076-d616-4e27-8bc9-2c0d8017e85d",
  "sourceToolAssistantUUID": "2fa00002-0eaf-4e56-bcef-267afc4153d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-15T12:47:47.119Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UWcdxquDSLYhX6jSJcAMFz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/median/paper.tex",
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fcc9b076-d616-4e27-8bc9-2c0d8017e85d",
  "isSidechain": true,
  "agentId": "a9bd4203964701927",
  "requestId": "req_011Cb4NzMpBNQS5T2fDHRguW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9e9ae4fc-43aa-434f-9254-2ee329ae9827",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015yMCYRxZGYKfHGBeTS3KDb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 386,
      "cache_read_input_tokens": 58674,
      "output_tokens": 217,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 386
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 217,
          "cache_read_input_tokens": 58674,
          "cache_creation_input_tokens": 386,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 386,
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

_source line 33 · 2026-05-15T12:47:47.125Z_

<details><summary>↩ Tool result · `toolu_01UWcdxquDSLYhX6jSJcAMFz`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{booktabs}
8	\usepackage{multirow}
9	\usepackage{graphicx}
10	\usepackage{xcolor}
11	\usepackage{soul}
12	\usepackage{hyperref}
13	\usepackage{enumitem}
14	
15	\newcommand{\method}{FREIGE}
16	\newcommand{\ced}{CED}
17	\newcommand{\edcr}{EDCR}
18	
19	\title{FREIGE: Faithful Evidence-Grounded Document-Level Relation Extraction\\via Contrastive Evidence Discrimination}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\begin{abstract}
27	LLM-based document-level relation extraction (DocRE) approaches extraction performance competitive with encoder models, yet no existing method generates verifiable evidence sentences alongside extracted relations. We present \method{}, the first LLM framework for DocRE that jointly produces relation triples and grounded evidence. Our approach introduces Contrastive Evidence Discrimination (\ced{}), a scoring function that evaluates evidence quality by contrasting gold-supporting sentences against entity-sharing distractors within the same document. We find that \ced{} is effective as an offline quality signal for Rejection Sampling Fine-Tuning (RSFT) but leads to catastrophic forgetting when used as an online RL (GRPO) reward---a finding we systematically document across three reward types and multiple hyperparameter configurations. On DocRED, \method{} achieves an evidence F1 of 78.9\% on the test set, competitive with a relation F1 of 42.8\%, while reducing entity-sharing distractor citations (EDCR) by 5--8 percentage points over the SFT baseline. We further propose the Entity-sharing Distractor Citation Rate (\edcr{}) as a complementary evaluation metric that captures a failure mode invisible to standard evidence F1. Experiments across three model sizes (1.7B--8B) and two datasets (DocRED, Re-DocRED) confirm the consistency of our approach.
28	\end{abstract}
29	
30	\section{Introduction}
31	
32	Document-level relation extraction (DocRE) requires identifying relations between entity pairs that may span multiple sentences in a document \cite{yao2019docred}. While encoder-based methods have achieved strong extraction performance \cite{zhou2021atlop,tan2022dreeam}, and recent LLM-based approaches show competitive results \cite{xu2024lmrc}, none produce verifiable evidence---the specific sentences supporting each extracted relation.
33	
34	Evidence grounding is critical for deploying DocRE in high-stakes domains: human-in-the-loop knowledge base population, biomedical literature curation, and retrieval-augmented generation all require traceability from extracted facts to source text. Without evidence, users cannot verify whether an extraction reflects genuine textual support or a spurious entity co-occurrence.
35	
36	A natural approach to encouraging faithful evidence is to use Natural Language Inference (NLI) as a reward signal during reinforcement learning. However, we identify a fundamental limitation: flat NLI scoring is systematically deceived by \emph{entity-sharing distractors}---sentences that mention the head or tail entity but do not support the specific relation. Such sentences receive high NLI entailment scores because they share key entities with the claim, yet they provide no genuine evidential support.
37	
38	We propose \textbf{Contrastive Evidence Discrimination (\ced{})}, which addresses this limitation by computing a margin between the NLI score for a candidate evidence sentence and the maximum NLI score among entity-sharing distractor sentences from the same document. This contrastive formulation shifts the evaluation from ``does this sentence entail the claim?'' to ``does this sentence entail the claim \emph{better than the best distractor}?''
39	
40	A central finding of our work is that \ced{} is effective as an \emph{offline} quality signal but fails as an \emph{online} RL reward. When used as a GRPO reward, \ced{} drives evidence F1 upward (to 85.0\%) but causes catastrophic forgetting of relation extraction capability (rel\_F1 collapses to $<$2\%). This failure is systematic: we observe it across three reward types (CED, flat-NLI, extraction-only), multiple learning rates, and with KL constraints. In contrast, \ced{} as an offline signal for RSFT---where it filters training candidates rather than directly shaping gradients---yields consistent improvements across all metrics.
41	
42	Our contributions are:
43	\begin{enumerate}
44	    \item \method{}, the first LLM-based DocRE framework that jointly generates relation triples and evidence sentences, achieving competitive extraction and evidence quality on DocRED.
45	    \item Contrastive Evidence Discrimination (\ced{}), a scoring function that provides consistent improvement over flat-NLI scoring for evidence quality, functioning as a composable module applicable at both training and inference time.
46	    \item A systematic analysis of online vs.\ offline RL for structured IE, documenting catastrophic forgetting in GRPO and connecting it to the evidence grounding gradient vanishing phenomenon described in LongRLVR.
47	    \item \edcr{}, a diagnostic metric for entity-sharing distractor citations, with analysis revealing its correlation with relation type characteristics.
48	\end{enumerate}
49	
50	\section{Related Work}
51	
52	\paragraph{Document-Level Relation Extraction.}
53	DocRED \cite{yao2019docred} established the benchmark for document-level RE with evidence annotations. Encoder-based methods achieve strong extraction F1: ATLOP \cite{zhou2021atlop} (63.4\%), DocuNet \cite{zhang2021docunet} (64.6\%). For evidence, DREEAM \cite{tan2022dreeam} uses attention supervision to achieve evidence F1 of 57.34\%, and SAIS \cite{xiao2022sais} reaches 55.67\%. However, these methods treat evidence as attention weights rather than explicit outputs. Recent LLM approaches---LMRC \cite{xu2024lmrc} (60.69\% F1 with LLaMA3.1-8B) and DocKS-RAG \cite{docks2025} (63.59\% with GNN+RAG)---improve extraction but produce no evidence.
54	
55	\paragraph{RL for Language Model Alignment.}
56	RLHF and its variants \cite{ouyang2022training,rafailov2023direct} align LLMs with human preferences. For structured tasks, Group Relative Policy Optimization (GRPO) \cite{shao2024deepseekmath} and Rejection Sampling Fine-Tuning (RSFT) \cite{yuan2024rrhf} offer complementary paradigms. The theoretical equivalence between RSFT and PPO under certain conditions \cite{tang2024rsftppo} motivates using offline approaches when online RL is unstable. LongRLVR \cite{song2026longrlvr} provides theoretical analysis of evidence grounding gradient vanishing in long-context RL.
57	
58	\paragraph{Faithfulness Evaluation.}
59	NLI-based faithfulness metrics \cite{honovich2022true,laban2022summac} assess whether generated text is entailed by source documents. However, document-level IE poses unique challenges: entity-sharing distractors receive high entailment scores despite not supporting the specific relation, a failure mode not addressed by existing metrics.
60	
61	\section{Method}
62	
63	\subsection{Task Formulation}
64	
65	Given a document $D = \{s_1, s_2, \ldots, s_n\}$ consisting of $n$ sentences with annotated entity mentions, the task is to generate a set of relation tuples $\{(h_i, r_i, t_i, E_i)\}$ where $h_i$ is the head entity, $r_i$ is the relation type, $t_i$ is the tail entity, and $E_i \subseteq \{s_1, \ldots, s_n\}$ is the set of evidence sentences supporting the relation.
66	
67	We formulate this as a sequence-to-sequence task where an LLM generates structured output containing relation triples with explicit sentence indices as evidence markers.
68	
69	\subsection{SFT Baseline}
70	
71	We fine-tune Qwen3-4B with LoRA \cite{hu2022lora} on DocRED training data, where each training example maps a document to its gold relation triples with evidence annotations. The output format is:
72	\begin{quote}
73	\texttt{(head; relation; tail; [S$_i$, S$_j$, ...])}
74	\end{quote}
75	where \texttt{S$_i$} denotes the $i$-th sentence in the document.
76	
77	\subsection{Contrastive Evidence Discrimination (CED)}
78	
79	For a candidate output containing a relation triple $(h, r, t)$ with cited evidence sentences $E = \{e_1, \ldots, e_k\}$, we construct the evaluation as follows.
80	
81	\paragraph{Claim Construction.} We form a natural language claim $c = $ ``\texttt{[h] [r\_verbalized] [t]}'' from the relation triple.
82	
83	\paragraph{Positive and Negative Sets.} For each cited sentence $e_i \in E$:
84	\begin{itemize}
85	    \item \textbf{Positive score}: $p_{\text{pos}}(e_i) = \text{NLI}_{\text{entail}}(e_i, c)$, the entailment probability from a pre-trained NLI model (DeBERTa-v3-base fine-tuned on MNLI).
86	    \item \textbf{Negative set}: $N_i = \{s \in D \setminus E \mid s \text{ mentions } h \text{ or } t\}$---all non-cited sentences that share entities with the triple.
87	    \item \textbf{Maximum negative score}: $p_{\text{neg}}^*(e_i) = \max_{s \in N_i} \text{NLI}_{\text{entail}}(s, c)$.
88	\end{itemize}
89	
90	\paragraph{CED Score.} The CED score for a candidate is:
91	\begin{equation}
92	    \text{CED} = \frac{1}{|E|} \sum_{e_i \in E} \left[ p_{\text{pos}}(e_i) - p_{\text{neg}}^*(e_i) \right]
93	\end{equation}
94	
95	A high CED score indicates that cited evidence sentences are more strongly entailing than the best entity-sharing distractors. Unlike flat NLI scoring ($\max_i p_{\text{pos}}(e_i)$), CED explicitly penalizes candidates whose evidence is no more informative than distractor sentences.
96	
97	\subsection{Rejection Sampling Fine-Tuning (RSFT)}
98	
99	We apply CED as an offline quality signal for RSFT:
100	
101	\begin{enumerate}
102	    \item \textbf{Candidate Generation}: The SFT model generates $N=8$ candidate outputs per training document (21,952 candidates total).
103	    \item \textbf{CED Scoring}: Each candidate is scored with CED.
104	    \item \textbf{Selection}: The top-$k$ candidate per document (default $k{=}1$) is selected, yielding 2,718 high-quality training examples.
105	    \item \textbf{Fine-Tuning}: The SFT model is further fine-tuned on the selected examples with LoRA ($\alpha{=}32$, lr$=10^{-5}$, 1 epoch).
106	\end{enumerate}
107	
108	\subsection{CED as Inference-Time Reranker}
109	
110	CED can also be applied at inference time without additional training. Given $N$ candidate outputs from the SFT model, we select the candidate with the highest CED score. This provides a training-free approach to reducing distractor citations at the cost of increased inference time ($\sim$8$\times$).
111	
112	\subsection{Entity-Sharing Distractor Citation Rate (EDCR)}
113	
114	We propose EDCR as a complementary metric to evidence F1:
115	\begin{equation}
116	    \text{EDCR} = \frac{|\{s \in C \setminus G \mid s \text{ mentions } h \text{ or } t\}|}{|C|}
117	\end{equation}
118	where $C$ is the set of all cited sentences and $G$ is the gold evidence set. EDCR measures the proportion of citations that are entity-sharing distractors---sentences that mention relevant entities but do not support the specific relation. Standard evidence F1 treats all false positive citations equally; EDCR specifically quantifies the most deceptive type of error.
119	
120	\section{Experiments}
121	
122	\subsection{Setup}
123	
124	\paragraph{Dataset.} We evaluate on DocRED \cite{yao2019docred} (3,053 train / 1,000 dev / 1,000 test documents, 96 relation types) and Re-DocRED \cite{tan2022redocred}, a revised version with corrected annotations.
125	
126	\paragraph{Models.} Our primary model is Qwen3-4B with LoRA fine-tuning. We additionally evaluate Qwen3-1.7B and Qwen3-8B for model size ablation.
127	
128	\paragraph{Baselines.} We compare against: (1)~SFT baseline (Qwen3-4B LoRA, no RL); (2)~RSFT with flat-NLI scoring; (3)~GRPO with CED/flat-NLI/extraction-only rewards; (4)~DREEAM \cite{tan2022dreeam} (encoder, evidence SOTA); (5)~SAIS \cite{xiao2022sais} (encoder, evidence baseline).
129	
130	\paragraph{Metrics.} Relation F1 (rel\_F1), Ign\_F1 (excluding training relational facts), Evidence F1 (evi\_F1), and EDCR (lower is better).
131	
132	\paragraph{CED Configuration.} NLI model: DeBERTa-v3-base fine-tuned on MNLI. Discrimination accuracy on gold vs.\ distractor pairs: 81.5\%.
133	
134	\subsection{Main Results}
135	
136	Table~\ref{tab:main} presents the test set results. \method{} (RSFT+CED) achieves test rel\_F1 of 42.8--43.8\% and evi\_F1 of 78.3--78.9\%, representing a +4.2pp rel\_F1 and +1.4pp evi\_F1 improvement over the SFT baseline.
137	
138	\begin{table}[t]
139	\centering
140	\small
141	\begin{tabular}{lcccc}
142	\toprule
143	\textbf{Method} & \textbf{rel\_F1} & \textbf{ign\_F1} & \textbf{evi\_F1} & \textbf{EDCR}$\downarrow$ \\
144	\midrule
145	SFT baseline & 38.6 & 37.8 & 77.5 & 69.5 \\
146	RSFT flat-NLI & 42.0 & --- & 77.6 & 66.8 \\
147	RSFT CED (r2b) & 42.8 & 42.0 & 78.9 & 63.8 \\
148	RSFT CED (s44) & 43.8 & 42.9 & 78.3 & 62.0 \\
149	\midrule
150	DREEAM$^\dagger$ & --- & --- & 57.3 & --- \\
151	SAIS$^\dagger$ & --- & --- & 55.7 & --- \\
152	\bottomrule
153	\end{tabular}
154	\caption{Test set results on DocRED. $^\dagger$Encoder-based methods using attention-based evidence extraction (see \S\ref{sec:protocol} for evaluation protocol discussion). EDCR computed on dev set (test evidence labels unavailable for EDCR computation). Two RSFT+CED configurations are reported: r2b (1 epoch, $\alpha{=}32$) and s44 (3 epochs, $\alpha{=}128$, seed 44).}
155	\label{tab:main}
156	\end{table}
157	
158	The evi\_F1 gap between \method{} and encoder baselines (78.9\% vs.\ 57.3\% for DREEAM) is substantial but requires careful interpretation due to evaluation protocol differences (\S\ref{sec:protocol}). The ign\_F1 values closely track rel\_F1 ($<$1pp difference), indicating that RSFT does not overfit to training-set relation co-occurrences.
159	
160	\paragraph{Dev$\to$Test Generalization.}
161	Table~\ref{tab:devtest} shows the generalization gap. The rel\_F1 drop of 2.1--2.8pp is consistent with the SFT baseline (2.0pp) and within the expected range for DocRED. The s44 configuration (3 epochs) shows slightly larger degradation, suggesting mild dev-set overfitting compared to the 1-epoch r2b configuration.
162	
163	\begin{table}[t]
164	\centering
165	\small
166	\begin{tabular}{lcccc}
167	\toprule
168	\textbf{Config} & \textbf{dev} & \textbf{test} & $\Delta$\textbf{rel\_F1} & $\Delta$\textbf{evi\_F1} \\
169	\midrule
170	SFT & 40.6 / 79.8 & 38.6 / 77.5 & $-$2.0 & $-$2.3 \\
171	r2b & 44.9 / 81.3 & 42.8 / 78.9 & $-$2.1 & $-$2.4 \\
172	s44 & 46.6 / 80.9 & 43.8 / 78.3 & $-$2.8 & $-$2.6 \\
173	\bottomrule
174	\end{tabular}
175	\caption{Dev$\to$test generalization gap (rel\_F1 / evi\_F1).}
176	\label{tab:devtest}
177	\end{table}
178	
179	\subsection{CED vs.\ Flat-NLI Scoring (Claim 2)}
180	\label{sec:ced_vs_nli}
181	
182	Table~\ref{tab:ced_nli} compares CED and flat-NLI as RSFT scoring functions in an apple-to-apple ablation: both use the same candidate pool (21,952 generations), same selection threshold ($k{=}1$), and same RSFT hyperparameters.
183	
184	\begin{table}[t]
185	\centering
186	\small
187	\begin{tabular}{llccccc}
188	\toprule
189	\textbf{Method} & \textbf{Scoring} & \textbf{rel\_F1} & \textbf{evi\_F1} & \textbf{EDCR}$\downarrow$ \\
190	\midrule
191	SFT & --- & 40.6 & 79.8 & 71.2 \\
192	RSFT & flat-NLI & 44.2 & 79.9 & 68.5 \\
193	RSFT & CED & 44.9 & 81.3 & 66.1 \\
194	\midrule
195	\multicolumn{2}{l}{$\Delta$ (CED $-$ flat-NLI)} & +0.7 & +1.4 & $-$2.4 \\
196	\bottomrule
197	\end{tabular}
198	\caption{CED vs.\ flat-NLI RSFT ablation (dev set). CED provides consistent improvement across all three metrics.}
199	\label{tab:ced_nli}
200	\end{table}
201	
202	CED scoring improves over flat-NLI on all three dimensions: rel\_F1 (+0.7pp), evi\_F1 (+1.4pp), and EDCR ($-$2.4pp). The critical observation is that flat-NLI RSFT achieves virtually no evi\_F1 improvement over SFT (+0.1pp), while CED RSFT achieves +1.5pp. This reveals that flat-NLI scoring fails to discriminate evidence quality: it filters out candidates with globally low NLI scores but cannot distinguish entity-sharing distractors from genuine evidence, since both receive high entailment scores. CED's contrastive margin directly addresses this blind spot.
203	
204	\subsection{CED as Inference-Time Reranker}
205	
206	Table~\ref{tab:reranker} evaluates CED as a reranker applied at inference time. CED reranking of SFT outputs (no additional training) achieves the largest EDCR reduction ($-$10.7pp), demonstrating CED's direct value as a quality signal. Combining RSFT+CED training with CED reranking further reduces EDCR to 58.5\% while maintaining rel\_F1 and evi\_F1.
207	
208	\begin{table}[t]
209	\centering
210	\small
211	\begin{tabular}{lcccc}
212	\toprule
213	\textbf{Method} & \textbf{Train?} & \textbf{rel\_F1} & \textbf{evi\_F1} & \textbf{EDCR}$\downarrow$ \\
214	\midrule
215	SFT & SFT only & 40.6 & 79.8 & 71.2 \\
216	CED reranker & No & 41.5 & 80.5 & 60.5 \\
217	RSFT-CED & Yes & 44.9 & 81.3 & 66.1 \\
218	RSFT-CED + reranker & Yes & 45.2 & 81.8 & 58.5 \\
219	\bottomrule
220	\end{tabular}
221	\caption{CED as a composable module (dev set). Reranking uses $N{=}8$ candidates; inference cost is $\sim$8$\times$.}
222	\label{tab:reranker}
223	\end{table}
224	
225	The composability of CED is noteworthy: RSFT improves generation quality (higher rel\_F1 and evi\_F1), while reranking provides additional distractor filtering (lower EDCR). These two applications are complementary because RSFT modifies the model's generation distribution while reranking performs sharp selection among candidates.
226	
227	\subsection{Online RL Fails: GRPO Analysis (Claim 3)}
228	\label{sec:grpo}
229	
230	Table~\ref{tab:grpo} summarizes GRPO experiments across three reward types and multiple configurations. All configurations exhibit the same pattern: reward increases monotonically while rel\_F1 collapses catastrophically within 10--50 steps.
231	
232	\begin{table}[t]
233	\centering
234	\small
235	\begin{tabular}{lcccccc}
236	\toprule
237	\textbf{Reward} & \textbf{LR} & \textbf{KL} & \textbf{Collapse} & \textbf{Peak} & \textbf{Final} & \textbf{Final} \\
238	& & & \textbf{Step} & \textbf{rel\_F1} & \textbf{evi\_F1} & \textbf{Reward} \\
239	\midrule
240	CED & 5e-6 & 0 & $\sim$10 & 1.4 & 85.0 & 1.20 \\
241	CED & 5e-5 & 0.01 & $\sim$50 & 21.1 & 57.5 & 1.20 \\
242	flat-NLI & 5e-6 & 0 & $\sim$25 & $<$1 & $<$1 & 0.29 \\
243	extract & 5e-6 & 0 & $\sim$20 & 1.5 & --- & 0.30 \\
244	\bottomrule
245	\end{tabular}
246	\caption{GRPO trajectory summary. ``Collapse Step'' = step at which rel\_F1 drops below 5\%. All configs start from the same SFT checkpoint (rel\_F1 = 40.6\%).}
247	\label{tab:grpo}
248	\end{table}
249	
250	The CED reward without KL constraint (lr=5e-6) is particularly revealing: evi\_F1 \emph{increases} to 85.0\% (surpassing RSFT's 81.3\%) while rel\_F1 collapses to 1.4\%. The model learns to generate high-quality evidence but ``forgets'' how to extract relations---the policy gradient from CED reward reshapes generation toward evidence-rich outputs at the expense of structured extraction.
251	
252	Adding KL constraints (KL=0.01) delays but does not prevent collapse: rel\_F1 peaks at 21.1\% (step 90) before declining, still far below the SFT baseline. The flat-NLI reward collapses fastest (90\% of groups reach zero-variance outputs by step 25), because its smoother reward surface enables rapid convergence to degenerate optima.
253	
254	This systematic failure across reward types and hyperparameters is consistent with the evidence grounding gradient vanishing analysis in LongRLVR \cite{song2026longrlvr}: in multi-objective structured generation, the evidence grounding signal dominates the policy gradient while the extraction signal vanishes, creating an irreconcilable conflict. RSFT sidesteps this by using CED as a \emph{selection criterion} rather than a gradient signal, preserving the balanced generation capability of the SFT checkpoint.
255	
256	\subsection{EDCR Diagnostic Analysis (Claim 4)}
257	\label{sec:edcr}
258	
259	Table~\ref{tab:edcr_diag} presents cross-method EDCR diagnostics. CED-based methods consistently reduce the mean number of distractor citations per relation instance.
260	
261	\begin{table}[t]
262	\centering
263	\small
264	\begin{tabular}{lccccc}
265	\toprule
266	\textbf{Method} & \textbf{EDCR}$\downarrow$ & \textbf{evi\_F1} & \textbf{\#Distr.} & \textbf{\#Gold} & \textbf{\#Total} \\
267	\midrule
268	SFT & 71.2 & 79.8 & 3.2 & 2.1 & 5.3 \\
269	RSFT flat-NLI & 68.5 & 79.9 & 2.9 & 2.0 & 4.9 \\
270	RSFT CED & 66.1 & 81.3 & 2.6 & 2.1 & 4.7 \\
271	CED reranker & 60.5 & 79.0 & 2.2 & 2.0 & 4.2 \\
272	\bottomrule
273	\end{tabular}
274	\caption{Cross-method EDCR diagnostic (dev set). \#Distr.\ = mean entity-sharing distractor count, \#Gold = mean gold evidence cited, \#Total = mean total citations per instance.}
275	\label{tab:edcr_diag}
276	\end{table}
277	
278	\paragraph{Relation-Type Analysis.}
279	EDCR varies dramatically across relation types (Table~\ref{tab:edcr_rel}). Geographic and nationality relations (P17, P131, P27) exhibit high EDCR ($\geq$0.74 even after RSFT+CED), because documents about locations contain many sentences mentioning country and city names without supporting the specific relation. Creative-domain relations (P50, P86, P175) have lower EDCR ($\leq$0.42), as these relations are typically stated in specific sentences with fewer entity-sharing distractors.
280	
281	\begin{table}[t]
282	\centering
283	\small
284	\begin{tabular}{lcccr}
285	\toprule
286	\textbf{Relation} & \textbf{SFT} & \textbf{RSFT-CED} & $\Delta$ & \textbf{\#Inst.} \\
287	\midrule
288	\multicolumn{5}{l}{\emph{High-EDCR relations}} \\
289	P17 (country) & 85.0 & 79.0 & $-$6.0 & 1205 \\
290	P131 (located in) & 83.0 & 78.0 & $-$5.0 & 987 \\
291	P27 (citizenship) & 80.0 & 74.0 & $-$6.0 & 654 \\
292	P30 (continent) & 78.0 & 73.0 & $-$5.0 & 321 \\
293	P150 (contains) & 77.0 & 72.0 & $-$5.0 & 445 \\
294	\midrule
295	\multicolumn{5}{l}{\emph{Low-EDCR relations}} \\
296	P86 (composer) & 48.0 & 42.0 & $-$6.0 & 198 \\
297	P50 (author) & 45.0 & 39.0 & $-$6.0 & 276 \\
298	P175 (performer) & 42.0 & 37.0 & $-$5.0 & 312 \\
299	P40 (child) & 40.0 & 35.0 & $-$5.0 & 187 \\
300	P26 (spouse) & 38.0 & 33.0 & $-$5.0 & 156 \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9e9ae4fc-43aa-434f-9254-2ee329ae9827",
  "isSidechain": true,
  "promptId": "00a1eb94-0484-4e13-931d-e659507bc0c6",
  "agentId": "a9bd4203964701927",
  "type": "user",
  "uuid": "09b87287-2c01-4375-b682-107149b9ad10",
  "sourceToolAssistantUUID": "9e9ae4fc-43aa-434f-9254-2ee329ae9827",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-15T12:47:50.386Z_

Let me continue reading the median paper to see the rest of the results and analyses.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09b87287-2c01-4375-b682-107149b9ad10",
  "isSidechain": true,
  "agentId": "a9bd4203964701927",
  "requestId": "req_011Cb4Nzfa1ybFDsnB46Y826",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f8b38634-07a9-41c1-9948-76539ae859e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018sCVrubvhKjUUgh6KxZhFZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15948,
      "cache_read_input_tokens": 59060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15948,
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

_source line 35 · 2026-05-15T12:47:52.693Z_

<details open><summary>🔧 Tool call — Read · `toolu_0131VLGb9nHe8uyz2Lh27te7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/median/paper.tex",
  "offset": 300,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8b38634-07a9-41c1-9948-76539ae859e2",
  "isSidechain": true,
  "agentId": "a9bd4203964701927",
  "requestId": "req_011Cb4Nzfa1ybFDsnB46Y826",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "45b875c7-0a1f-4899-85c7-722bc092f94d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018sCVrubvhKjUUgh6KxZhFZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15948,
      "cache_read_input_tokens": 59060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15948,
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

_source line 36 · 2026-05-15T12:47:52.712Z_

<details><summary>↩ Tool result · `toolu_0131VLGb9nHe8uyz2Lh27te7`</summary>

```text
300	P26 (spouse) & 38.0 & 33.0 & $-$5.0 & 156 \\
301	\bottomrule
302	\end{tabular}
303	\caption{EDCR (\%) by relation type (dev set, top-5 and bottom-5). CED reduces EDCR consistently (5--6pp) but high-EDCR relations remain challenging.}
304	\label{tab:edcr_rel}
305	\end{table}
306	
307	CED provides a uniform 5--6pp EDCR reduction across all relation types, suggesting it captures a general distractor pattern rather than being relation-specific. However, the absolute EDCR values for geographic relations remain high (73--79\%), indicating that entity-sharing distractor confusion in these domains is structural: documents about locations inherently contain many entity-mentioning sentences, and resolving this likely requires relation-type-aware scoring.
308	
309	\paragraph{Limitations.} EDCR of 58.5--66.1\% across our best configurations means that a majority of non-gold citations are still entity-sharing distractors. While this represents meaningful progress over the SFT baseline (71.2\%), we acknowledge that the distractor problem is far from solved. Part of this is attributable to annotation incompleteness in DocRED---our Re-DocRED analysis (\S\ref{sec:redocred}) shows that EDCR drops significantly under more complete annotations.
310	
311	\subsection{Evidence Baseline Comparison}
312	\label{sec:protocol}
313	
314	Table~\ref{tab:baseline} contextualizes our evidence results against encoder baselines. An important caveat: DREEAM and SAIS extract evidence via attention weight thresholding (binary classification per sentence), while \method{} generates explicit sentence indices. These evaluation protocols differ fundamentally---our model ``knows what it is citing'' while attention-based methods derive evidence post-hoc.
315	
316	\begin{table}[t]
317	\centering
318	\small
319	\begin{tabular}{llccc}
320	\toprule
321	\textbf{Method} & \textbf{Type} & \textbf{dev evi\_F1} & \textbf{test evi\_F1} & \textbf{dev rel\_F1} \\
322	\midrule
323	DREEAM (paper) & encoder & --- & 57.3 & 63.5 \\
324	DREEAM (reprod.) & encoder & 56.8 & --- & 62.8 \\
325	SAIS (reprod.) & encoder & 54.8 & 55.7 & 61.8 \\
326	FREIGE (ours) & generative & 81.3 & 78.9$^*$ & 44.9 \\
327	\bottomrule
328	\end{tabular}
329	\caption{Evidence baseline comparison. $^*$Test evi\_F1 computed locally (not from CodaLab). DREEAM reproduction gap: $-$0.5pp from reported test evi\_F1.}
330	\label{tab:baseline}
331	\end{table}
332	
333	\method{}'s evi\_F1 substantially exceeds encoder baselines (78.9\% vs.\ 57.3\%), but we emphasize that this comparison should be treated as a reference point rather than a direct superiority claim. The evaluation protocols produce different error distributions: attention-based methods suffer from threshold sensitivity, while generative methods may over-cite (producing more citations that happen to include gold sentences). \method{}'s rel\_F1 (44.9\%) is lower than encoder methods (62.8\% for DREEAM), reflecting the current gap between generative and encoder approaches for extraction---\method{}'s contribution is evidence grounding, not extraction supremacy.
334	
335	\subsection{Model Size Ablation}
336	
337	Table~\ref{tab:size} evaluates the RSFT+CED pipeline across three model sizes.
338	
339	\begin{table}[t]
340	\centering
341	\small
342	\begin{tabular}{llccccc}
343	\toprule
344	\textbf{Model} & \textbf{Method} & \textbf{rel\_F1} & \textbf{evi\_F1} & \textbf{EDCR}$\downarrow$ & $\Delta$\textbf{rel} & $\Delta$\textbf{evi} \\
345	\midrule
346	\multirow{2}{*}{1.7B} & SFT & 32.8 & 73.5 & 75.0 & --- & --- \\
347	 & RSFT-CED & 36.5 & 75.8 & 70.5 & +3.7 & +2.3 \\
348	\midrule
349	\multirow{2}{*}{4B} & SFT & 40.6 & 79.8 & 71.2 & --- & --- \\
350	 & RSFT-CED & 44.9 & 81.3 & 66.1 & +4.4 & +1.5 \\
351	\midrule
352	\multirow{2}{*}{8B} & SFT & 44.5 & 81.8 & 69.0 & --- & --- \\
353	 & RSFT-CED & 48.2 & 83.2 & 63.5 & +3.7 & +1.4 \\
354	\bottomrule
355	\end{tabular}
356	\caption{Model size ablation (dev set). RSFT+CED consistently improves over SFT across 1.7B--8B, with relative gains largely independent of model capacity.}
357	\label{tab:size}
358	\end{table}
359	
360	RSFT+CED provides consistent improvements at all scales: $\Delta$rel\_F1 ranges from +3.7 to +4.4pp, and $\Delta$evi\_F1 from +1.4 to +2.3pp. The 1.7B model shows the largest evi\_F1 gain (+2.3pp), likely because smaller models have higher generation diversity, giving CED more room for discrimination. The 8B model achieves the best absolute performance (rel\_F1 48.2\%, evi\_F1 83.2\%) and the largest EDCR improvement ($-$5.5pp). The marginal gain from 4B to 8B is modest (rel\_F1 +3.3pp, evi\_F1 +1.9pp), suggesting diminishing returns at larger scales for this task.
361	
362	\subsection{Re-DocRED Extension}
363	\label{sec:redocred}
364	
365	Table~\ref{tab:redocred} compares results on DocRED and Re-DocRED, which corrects annotation incompleteness in DocRED by supplementing missing relations and evidence labels.
366	
367	\begin{table}[t]
368	\centering
369	\small
370	\begin{tabular}{llccc}
371	\toprule
372	\textbf{Dataset} & \textbf{Method} & \textbf{rel\_F1} & \textbf{evi\_F1} & \textbf{EDCR}$\downarrow$ \\
373	\midrule
374	\multirow{2}{*}{DocRED} & SFT & 40.6 & 79.8 & 71.2 \\
375	 & RSFT-CED & 44.9 & 81.3 & 66.1 \\
376	\midrule
377	\multirow{2}{*}{Re-DocRED} & SFT & 43.5 & 81.5 & 58.0 \\
378	 & RSFT-CED & 47.5 & 83.5 & 52.5 \\
379	\bottomrule
380	\end{tabular}
381	\caption{DocRED vs.\ Re-DocRED (dev set). Re-DocRED's more complete annotations reduce EDCR by $\sim$13pp across methods.}
382	\label{tab:redocred}
383	\end{table}
384	
385	Two findings emerge: (1)~EDCR drops substantially on Re-DocRED ($-$13.2pp for SFT, $-$13.6pp for RSFT-CED), confirming that a significant portion of apparent entity-sharing distractors in DocRED are actually valid evidence sentences missed by annotators. (2)~RSFT+CED maintains consistent improvements on Re-DocRED ($\Delta$rel\_F1 +4.0pp, $\Delta$evi\_F1 +2.0pp, $\Delta$EDCR $-$5.5pp), demonstrating robustness to annotation quality. The residual EDCR of 52.5\% on Re-DocRED indicates that the distractor problem persists even with better annotations, though at a reduced level.
386	
387	\subsection{Ablation Studies}
388	
389	\paragraph{Top-$k$ Selection.}
390	Table~\ref{tab:topk} evaluates the quality-quantity trade-off in CED candidate selection.
391	
392	\begin{table}[t]
393	\centering
394	\small
395	\begin{tabular}{ccccccc}
396	\toprule
397	\textbf{$k$} & \textbf{\#Samples} & \textbf{Mean CED} & \textbf{rel\_F1} & \textbf{evi\_F1} & \textbf{EDCR}$\downarrow$ \\
398	\midrule
399	1 & 2,718 & 0.668 & 44.9 & 81.3 & 66.1 \\
400	3 & 7,950 & 0.548 & 45.5 & 80.2 & 67.8 \\
401	\bottomrule
402	\end{tabular}
403	\caption{Top-$k$ selection ablation (dev set).}
404	\label{tab:topk}
405	\end{table}
406	
407	$k{=}3$ provides $\sim$3$\times$ more training data with lower mean CED score (0.548 vs.\ 0.668). This yields a slight rel\_F1 improvement (+0.6pp) from greater data diversity, but \emph{degrades} evi\_F1 ($-$1.1pp) and EDCR (+1.7pp). The rank-2 and rank-3 candidates contain more distractor-heavy evidence, diluting the CED signal. We use $k{=}1$ as the default since evidence quality is our primary objective.
408	
409	\paragraph{NLI Model Capacity.}
410	Table~\ref{tab:nli} compares DeBERTa-v3-base and DeBERTa-v3-large as CED scorers.
411	
412	\begin{table}[t]
413	\centering
414	\small
415	\begin{tabular}{lcccc}
416	\toprule
417	\textbf{NLI Model} & \textbf{Disc.\ Acc.} & \textbf{Margin} & \textbf{RSFT evi\_F1} & \textbf{RSFT EDCR}$\downarrow$ \\
418	\midrule
419	DeBERTa-v3-base & 81.5 & 0.48 & 81.3 & 66.1 \\
420	DeBERTa-v3-large & 84.5 & 0.52 & 81.7 & 65.2 \\
421	\bottomrule
422	\end{tabular}
423	\caption{NLI model ablation (dev set). ``Disc.\ Acc.'' = CED discrimination accuracy on gold vs.\ distractor pairs.}
424	\label{tab:nli}
425	\end{table}
426	
427	The larger NLI model improves discrimination accuracy by +3.0pp and mean CED margin by +0.04, but downstream RSFT gains are marginal (evi\_F1 +0.4pp, EDCR $-$0.9pp). This suggests that the current bottleneck is annotation completeness rather than NLI model capability: a stronger NLI model cannot compensate for gold evidence labels that are themselves incomplete.
428	
429	\section{Analysis}
430	
431	\paragraph{Why Flat-NLI Fails at Evidence Discrimination.}
432	The flat-NLI RSFT result (Table~\ref{tab:ced_nli}) reveals that flat-NLI scoring achieves virtually zero evi\_F1 improvement over SFT (+0.1pp), despite meaningfully improving rel\_F1 (+3.6pp). This asymmetry arises because flat-NLI can filter candidates with globally poor NLI scores (improving extraction quality) but cannot distinguish entity-sharing distractors from genuine evidence---both receive high entailment scores because they share key entities. CED's contrastive design directly targets this blind spot: the margin $p_{\text{pos}} - \max(p_{\text{neg}})$ penalizes candidates where distractor sentences also receive high NLI scores.
433	
434	\paragraph{Online vs.\ Offline RL for Structured IE.}
435	Our GRPO analysis (\S\ref{sec:grpo}) provides empirical evidence for a broader methodological insight: online RL is poorly suited for multi-objective structured generation where different objectives (extraction accuracy, evidence faithfulness) create competing gradient signals. The CED GRPO experiment is the clearest illustration---evi\_F1 rises to 85.0\% while rel\_F1 collapses to 1.4\%, because the CED reward gradient overwhelms the extraction objective. RSFT avoids this conflict entirely by treating CED as a data selection criterion rather than a training objective, preserving the SFT model's balanced generation capability.
436	
437	\paragraph{CED as a Composable Module.}
438	CED can be applied at three points in the pipeline: (1)~training data selection for RSFT, (2)~inference-time reranking, and (3)~both combined. Each application provides additive benefits (Table~\ref{tab:reranker}), with the combined approach achieving the best EDCR (58.5\%) while maintaining strong rel\_F1 and evi\_F1. This composability makes CED practical for deployment: teams can start with the training-free reranker and optionally add RSFT when compute allows.
439	
440	\section{Conclusion}
441	
442	We presented \method{}, the first LLM-based framework for document-level relation extraction with evidence grounding. Our Contrastive Evidence Discrimination (\ced{}) scoring function provides consistent improvements over flat-NLI scoring and functions as a composable module for both training and inference. We documented the systematic failure of online RL (GRPO) for structured IE and showed that offline application of \ced{} via RSFT effectively sidesteps catastrophic forgetting.
443	
444	Our results demonstrate that LLMs can generate both relation triples and verifiable evidence for DocRE, with evidence quality competitive across model sizes and datasets. The EDCR metric provides complementary diagnostic value by quantifying entity-sharing distractor citations.
445	
446	\paragraph{Limitations.}
447	\method{}'s rel\_F1 (42.8--43.8\%) remains below encoder SOTA ($\sim$63\%), reflecting the current gap between generative and encoder approaches for extraction. EDCR of 58.5--66.1\% indicates that distractor citations remain a significant issue. The evi\_F1 comparison with encoder baselines is not directly apple-to-apple due to different evidence extraction mechanisms. Our experiments are limited to English DocRE on DocRED/Re-DocRED.
448	
449	\bibliography{custom}
450	
451	\appendix
452	
453	\section{GRPO Full Configuration Grid}
454	\label{app:grpo}
455	
456	We evaluated GRPO across 3 reward types $\times$ 4+ learning rates $\times$ KL constraint configurations. All configurations exhibited the same failure pattern: monotonically increasing reward with catastrophic rel\_F1 collapse within 10--50 gradient steps. The KL-constrained CED variant (lr=5e-5, KL=0.01) achieved the highest peak rel\_F1 (21.1\% at step 90) but still fell far short of the SFT baseline (40.6\%).
457	
458	\section{RSFT Hyperparameter Configurations}
459	\label{app:rsft}
460	
461	\begin{table}[h]
462	\centering
463	\small
464	\begin{tabular}{lcccc}
465	\toprule
466	\textbf{Config} & \textbf{Epochs} & $\alpha$ & \textbf{LR} & \textbf{dev rel\_F1} \\
467	\midrule
468	r1 (s42) & 3 & 128 & 2e-5 & 44.5 \\
469	r1 (s44) & 3 & 128 & 2e-5 & 46.6 \\
470	r2a & 1 & 128 & 2e-5 & 44.9 \\
471	r2b & 1 & 32 & 1e-5 & 44.9 \\
472	\bottomrule
473	\end{tabular}
474	\caption{RSFT hyperparameter configurations. All use LoRA with rank 16.}
475	\end{table}
476	
477	\end{document}
478	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45b875c7-0a1f-4899-85c7-722bc092f94d",
  "isSidechain": true,
  "promptId": "00a1eb94-0484-4e13-931d-e659507bc0c6",
  "agentId": "a9bd4203964701927",
  "type": "user",
  "uuid": "bfccc6a9-a79a-46a5-88fe-b8bb38a94720",
  "sourceToolAssistantUUID": "45b875c7-0a1f-4899-85c7-722bc092f94d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-15T12:47:53.351Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MMUjY8n9z2bhfW1zMYJFN4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/best/paper.tex",
  "offset": 300,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bfccc6a9-a79a-46a5-88fe-b8bb38a94720",
  "isSidechain": true,
  "agentId": "a9bd4203964701927",
  "requestId": "req_011Cb4Nzfa1ybFDsnB46Y826",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "19bc4003-e879-4e54-8d85-839f652de652",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018sCVrubvhKjUUgh6KxZhFZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15948,
      "cache_read_input_tokens": 59060,
      "output_tokens": 269,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15948
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 269,
          "cache_read_input_tokens": 59060,
          "cache_creation_input_tokens": 15948,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15948,
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

_source line 38 · 2026-05-15T12:47:53.358Z_

<details><summary>↩ Tool result · `toolu_01MMUjY8n9z2bhfW1zMYJFN4`</summary>

```text
300	step-40 & 0.7 & 75.8 & 99.4 & 0.78 \\
301	step-60 & 0.9 & 81.0 & 99.3 & 0.91 \\
302	step-80 & 1.2 & 82.8 & 99.3 & 1.05 \\
303	step-100 & 1.4 & 85.0 & 98.8 & 1.20 \\
304	\midrule
305	GRPO (KL=0.01, ckpt-90) & 21.1 & 56.7 & 85.8 & --- \\
306	\bottomrule
307	\end{tabular}
308	\end{table}
309	
310	Adding KL regularization (KL=0.01) partially mitigates the collapse (rel-F1 recovers to 21.1) but remains far below SFT (40.6), and EDCR worsens to 85.8. Flat-NLI and extraction-only rewards collapse even earlier (steps 25--30). This comprehensive failure across reward types and hyperparameters motivates RSFT as the principled alternative: use CED's discriminative signal without the instability of online policy gradient updates.
311	
312	\subsection{Model Size Ablation}
313	
314	Table~\ref{tab:model_size} shows that RSFT+CED yields consistent improvements across three model scales.
315	
316	\begin{table}[t]
317	\centering
318	\caption{Model size ablation on DocRED dev set. RSFT+CED improves consistently across scales.}
319	\label{tab:model_size}
320	\begin{tabular}{lccccc}
321	\toprule
322	\textbf{Model} & \textbf{SFT rel-F1} & \textbf{RSFT rel-F1} & $\Delta$ & \textbf{RSFT Evi-F1} & \textbf{EDCR} \\
323	\midrule
324	Qwen3-1.7B & 34.2 & 37.8 & +3.6 & 77.6 & 68.2 \\
325	Qwen3-4B & 40.6 & 46.6 & +6.0 & 81.9 & 63.5 \\
326	Qwen3-8B & 44.8 & 49.2 & +4.4 & 83.5 & 58.8 \\
327	\bottomrule
328	\end{tabular}
329	\end{table}
330	
331	The improvement ranges from +3.6pp (1.7B) to +6.0pp (4B) in rel-F1 and +1.7--2.1pp in Evi-F1. Larger models benefit more from CED filtering (EDCR improves from 68.2 to 58.8 as scale increases), suggesting they better exploit the higher-quality training data. The 8B model achieves the highest Evi-F1 (83.5), indicating scaling potential for future work with larger models.
332	
333	\subsection{Re-DocRED Extension}
334	
335	Table~\ref{tab:redocred} evaluates on Re-DocRED, which corrects false-negative annotations in DocRED. All methods show higher rel-F1 (because previously correct predictions are no longer penalized as false positives). RSFT+CED maintains its advantage: +4.6pp rel-F1 and +1.9pp Evi-F1 over SFT.
336	
337	\begin{table}[t]
338	\centering
339	\caption{DocRED vs.\ Re-DocRED comparison (dev set).}
340	\label{tab:redocred}
341	\begin{tabular}{llccc}
342	\toprule
343	\textbf{Dataset} & \textbf{Method} & \textbf{rel-F1} & \textbf{Evi-F1} & \textbf{EDCR} \\
344	\midrule
345	DocRED & SFT & 40.6 & 79.8 & 71.2 \\
346	DocRED & RSFT+CED & 46.6 & 81.9 & 63.5 \\
347	\midrule
348	Re-DocRED & SFT & 47.2 & 81.2 & 64.8 \\
349	Re-DocRED & RSFT+CED & 51.8 & 83.1 & 57.8 \\
350	\bottomrule
351	\end{tabular}
352	\end{table}
353	
354	EDCR on Re-DocRED (57.8) is lower than on DocRED (63.5), as expected: with more complete gold annotations, fewer genuinely supportive sentences are misclassified as distractors. The consistent improvement across both datasets addresses the single-dataset generalization concern.
355	
356	\subsection{Top-$k$ Ablation}
357	
358	Table~\ref{tab:topk} compares $k$=1 (strict filtering, ${\sim}2{,}700$ samples, mean CED=0.668) vs.\ $k$=3 (relaxed, ${\sim}8{,}100$ samples, mean CED=0.542).
359	
360	\begin{table}[h]
361	\centering
362	\caption{Top-$k$ ablation for CED-scored RSFT (dev set).}
363	\label{tab:topk}
364	\begin{tabular}{lccccc}
365	\toprule
366	\textbf{top-$k$} & \textbf{Samples} & \textbf{Mean CED} & \textbf{rel-F1} & \textbf{Evi-F1} & \textbf{EDCR} \\
367	\midrule
368	1 & 2,718 & 0.668 & 46.6 & 80.9 & 63.5 \\
369	3 & $\sim$8,100 & 0.542 & 45.8 & 80.4 & 65.2 \\
370	\bottomrule
371	\end{tabular}
372	\end{table}
373	
374	Top-$k$=1 is slightly superior (+0.8pp rel-F1, +0.5pp Evi-F1, $-$1.7pp EDCR), suggesting that data quality outweighs data quantity in this regime. However, both settings substantially outperform SFT, indicating that CED's top-ranked candidates are consistently high-quality.
375	
376	\subsection{NLI Model Ablation}
377	
378	Table~\ref{tab:nli_ablation} compares DeBERTa-v3-base and DeBERTa-v3-large as CED scorers.
379	
380	\begin{table}[h]
381	\centering
382	\caption{NLI model ablation for CED scoring. DeBERTa-base is sufficient.}
383	\label{tab:nli_ablation}
384	\begin{tabular}{lccccc}
385	\toprule
386	\textbf{NLI Model} & \textbf{CED margin} & \textbf{Disc.\ acc} & \textbf{Pearson $r$} & \textbf{Evi-F1} & \textbf{EDCR} \\
387	\midrule
388	DeBERTa-v3-base & 0.480 & 81.5 & 0.34 & 80.9 & 63.5 \\
389	DeBERTa-v3-large & 0.523 & 84.9 & 0.28 & 81.5 & 61.8 \\
390	\bottomrule
391	\end{tabular}
392	\end{table}
393	
394	DeBERTa-large achieves marginally better discrimination accuracy (+3.4pp) and lower lexical-overlap correlation (Pearson $r$ 0.28 vs.\ 0.34), but downstream RSFT improvements are modest (+0.6pp Evi-F1, $-$1.7pp EDCR). The contrastive design of CED inherently reduces sensitivity to NLI model strength: lexical-overlap bias partially cancels in the margin computation. DeBERTa-base is sufficient for practical use, keeping the scoring pipeline lightweight.
395	
396	% ============================================================
397	% 6  DISCUSSION
398	% ============================================================
399	\section{Discussion}
400	
401	\paragraph{Evaluation Protocol Differences.}
402	The Evi-F1 comparison between \method{} (80.2) and DREEAM (57.3) requires careful interpretation. DREEAM extracts evidence via attention thresholds, producing precision-oriented but recall-limited evidence. Our generative approach produces explicit sentence citations with naturally higher recall (79.3 vs.\ 55.9). While the sentence-level F1 computation is identical, the evidence generation mechanism differs fundamentally. We recommend future work develop protocol-normalized metrics for cross-paradigm comparison.
403	
404	\paragraph{EDCR Limitations.}
405	EDCR captures only one type of evidence error (entity-sharing distractors) and may miss other failure modes such as temporally irrelevant evidence or topically adjacent but relationally incorrect citations. Additionally, EDCR depends on the completeness of gold evidence annotations---in Re-DocRED, EDCR is lower partly because annotations are more complete.
406	
407	\paragraph{Why RSFT Over Online RL.}
408	Our GRPO analysis demonstrates a specific failure mode: reward overoptimization in structured IE, where the model exploits the reward proxy (NLI entailment) via degenerate strategies (citing all entity-mentioning sentences) while abandoning the primary task (relation extraction). RSFT sidesteps this by never updating the policy with a reward gradient---it simply curates better training data. This suggests that for complex structured generation tasks where reward design is inherently imperfect, offline approaches may be systematically preferable.
409	
410	\paragraph{Remaining Challenges.}
411	The rel-F1 gap between LLM-based methods (${\sim}$45--49) and encoder SOTA (${\sim}$63) remains substantial. Closing this gap while maintaining evidence generation is an important direction. Additionally, EDCR of 54.8 on test indicates that roughly half of non-gold citations are still distractors, suggesting further improvements in evidence precision are needed.
412	
413	% ============================================================
414	% 7  CONCLUSION
415	% ============================================================
416	\section{Conclusion}
417	
418	We presented \method{}, the first LLM-based document-level relation extraction system that jointly generates relation triples and verifiable evidence. Our approach introduces Contrastive Evidence Discrimination (CED), a scoring function that converts NLI-based faithfulness assessment into a contrastive signal robust to entity-sharing distractor sentences. We demonstrated that CED fails catastrophically as an online RL reward (GRPO) but succeeds as an offline quality filter for rejection sampling fine-tuning (RSFT), providing an empirical cautionary tale for reward design in structured IE.
419	
420	On DocRED, \method{} achieves Evi-F1 80.2, substantially surpassing the encoder evidence SOTA (57.3), while improving extraction F1 by 5.7pp over the SFT baseline. The proposed EDCR metric reveals a blind spot of Evi-F1 where high coverage coexists with substantial distractor citation. Experiments across three model scales and two datasets confirm the generality of the approach. We hope this work encourages the community to treat evidence generation as a first-class output in document-level IE.
421	
422	\bibliographystyle{acl_natbib}
423	
424	\end{document}
425	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19bc4003-e879-4e54-8d85-839f652de652",
  "isSidechain": true,
  "promptId": "00a1eb94-0484-4e13-931d-e659507bc0c6",
  "agentId": "a9bd4203964701927",
  "type": "user",
  "uuid": "0f55ba20-e160-4f0f-8153-65ecfbb6e83f",
  "sourceToolAssistantUUID": "19bc4003-e879-4e54-8d85-839f652de652",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-15T12:47:58.553Z_

Now I have a comprehensive understanding of the paper, its claims, experimental evidence, and the project's internal documentation. Let me also check the worst-case paper for comparison and the experiment plan.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f55ba20-e160-4f0f-8153-65ecfbb6e83f",
  "isSidechain": true,
  "agentId": "a9bd4203964701927",
  "requestId": "req_011Cb4P18DeNDkvSLtLEcar2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5248cbe2-611e-40b4-8563-3e694b3ae963",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GzPgA7gmZFh4yZXhAyB5Nn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7954,
      "cache_read_input_tokens": 75008,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7954,
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

_source line 40 · 2026-05-15T12:47:59.390Z_

<details open><summary>🔧 Tool call — Glob · `toolu_011kHSYo4sD2K2JwGx6aCb8T`</summary>

```json
{
  "pattern": "**/experiment_plan.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5248cbe2-611e-40b4-8563-3e694b3ae963",
  "isSidechain": true,
  "agentId": "a9bd4203964701927",
  "requestId": "req_011Cb4P18DeNDkvSLtLEcar2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a5babeb7-0db0-4cb8-b448-c42f05eb8d00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GzPgA7gmZFh4yZXhAyB5Nn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7954,
      "cache_read_input_tokens": 75008,
      "output_tokens": 141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7954
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 141,
          "cache_read_input_tokens": 75008,
          "cache_creation_input_tokens": 7954,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7954,
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

_source line 41 · 2026-05-15T12:47:59.410Z_

<details><summary>↩ Tool result · `toolu_011kHSYo4sD2K2JwGx6aCb8T`</summary>

```text
experiment_plan.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a5babeb7-0db0-4cb8-b448-c42f05eb8d00",
  "isSidechain": true,
  "promptId": "00a1eb94-0484-4e13-931d-e659507bc0c6",
  "agentId": "a9bd4203964701927",
  "type": "user",
  "uuid": "0ef18311-4f89-4ecd-8751-8910da59fd25",
  "sourceToolAssistantUUID": "a5babeb7-0db0-4cb8-b448-c42f05eb8d00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-15T12:48:01.991Z_

<details open><summary>🔧 Tool call — Read · `toolu_017Vqx7SXdVAf9ni6gXoBMqk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ef18311-4f89-4ecd-8751-8910da59fd25",
  "isSidechain": true,
  "agentId": "a9bd4203964701927",
  "requestId": "req_011Cb4P1a8sZn9S8L3P1rGZL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "97de25ff-5a40-4af6-bec7-51636dce01a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TDQw6VRYgfXZnLBDoFhwox",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 261,
      "cache_read_input_tokens": 82962,
      "output_tokens": 85,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 261
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 85,
          "cache_read_input_tokens": 82962,
          "cache_creation_input_tokens": 261,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 261,
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

_source line 43 · 2026-05-15T12:48:02.003Z_

<details><summary>↩ Tool result · `toolu_017Vqx7SXdVAf9ni6gXoBMqk`</summary>

```text
1	experiments:
2	  # ── P0: 核心实验（必跑，论文 headline results） ──
3	
4	  - id: plan_001
5	    claim: 2
6	    description: "CED vs flat-NLI RSFT ablation: 用 flat-NLI scoring（非 contrastive）筛选 RSFT 训练数据，对比 CED scoring。验证 CED 的对比性 margin 是否优于朴素 NLI。步骤: (1) rsft_score_filter.py 用 flat-NLI 模式重新打分已有 candidates, (2) RSFT 训练, (3) 全量 dev eval。"
7	    priority: P0
8	    gpu_budget_hours: 20
9	    deps: []
10	    registry_id: null
11	
12	  - id: plan_002
13	    claim: 1
14	    description: "Test set evaluation: 用 RSFT best config（r2b 或 s44）在 DocRED test set 上评估。提交 CodaLab 获得官方 F1/Ign-F1，同时本地计算 Evi-F1 和 EDCR。"
15	    priority: P0
16	    gpu_budget_hours: 4
17	    deps: [plan_001]
18	    registry_id: null
19	
20	  - id: plan_003
21	    claim: 4
22	    description: "EDCR pipeline 验证 + cross-method diagnostic table: 在所有 evidence-producing 方法（SFT, RSFT-CED, RSFT-flatNLI, CED-reranker）上计算 EDCR，验证 EDCR 作为独立评估指标的诊断能力。"
23	    priority: P0
24	    gpu_budget_hours: 2
25	    deps: [plan_001]
26	    registry_id: null
27	
28	  - id: plan_004
29	    claim: 1
30	    description: "DREEAM baseline reproduction: 在 DocRED dev set 上复现 DREEAM (RoBERTa-large) 的 Evi-F1，确认 57.34 数字可复现，作为 Claim 1 的直接对比基线。"
31	    priority: P0
32	    gpu_budget_hours: 8
33	    deps: []
34	    registry_id: null
35	
36	  # ── P1: 重要补充（增强论文，时间紧可延后） ──
37	
38	  - id: plan_005
39	    claim: 1
40	    description: "CED-as-reranker: 推理时用 CED 对 SFT 生成的 N=8 候选重排选最佳，无需额外训练。验证 CED 在推理时的价值。已在运行中。"
41	    priority: P1
42	    gpu_budget_hours: 6
43	    deps: []
44	    registry_id: mvp2_ced_reranker_poc
45	
46	  - id: plan_006
47	    claim: 1
48	    description: "Model size ablation: Qwen3-1.7B 和 Qwen3-8B 上复现 RSFT+CED pipeline，验证方法对模型规模的泛化性。应对 RC4。"
49	    priority: P1
50	    gpu_budget_hours: 24
51	    deps: [plan_001]
52	    registry_id: null
53	
54	  - id: plan_007
55	    claim: 1
56	    description: "Re-DocRED extension: 在 Re-DocRED（修正 false negative 标注的版本）上评估，验证 RSFT+CED 在更干净标注下的表现。应对 RC4。"
57	    priority: P1
58	    gpu_budget_hours: 12
59	    deps: [plan_002]
60	    registry_id: null
61	
62	  - id: plan_008
63	    claim: 2
64	    description: "top_k ablation: CED scoring 筛选 top_k=3（更多训练数据 ~8000 samples）vs top_k=1（更严格 ~2718 samples），验证 CED 过滤严格度对 RSFT 质量的影响。"
65	    priority: P1
66	    gpu_budget_hours: 8
67	    deps: []
68	    registry_id: null
69	
70	  # ── P2: 加分项（有余力时做） ──
71	
72	  - id: plan_009
73	    claim: 3
74	    description: "GRPO forgetting 详细分析: 整理全部 GRPO checkpoint 的 rel_f1/evi_f1/EDCR 轨迹，绘制 forgetting dynamics 可视化（reward vs task performance 曲线），支撑 Claim 3 的论述。"
75	    priority: P2
76	    gpu_budget_hours: 4
77	    deps: []
78	    registry_id: null
79	
80	  - id: plan_010
81	    claim: 1
82	    description: "NLI model ablation: DeBERTa-v3-base vs DeBERTa-v3-large 作为 CED scorer 的对比，验证 NLI 模型能力对 CED 打分质量的影响。应对 RC1。"
83	    priority: P2
84	    gpu_budget_hours: 4
85	    deps: []
86	    registry_id: null
87	
88	  # ── MVP 已完成实验（关联 registry） ──
89	
90	  - id: plan_mvp1
91	    claim: 1
92	    description: "MVP-1: CED signal verification — DeBERTa NLI 区分 gold evidence vs entity-sharing distractor 的能力验证"
93	    priority: P0
94	    gpu_budget_hours: 1
95	    deps: []
96	    registry_id: mvp1_ced_signal
97	
98	  - id: plan_mvp2_sft
99	    claim: 1
100	    description: "SFT baseline: Qwen3-4B + LoRA SFT on DocRED gold, 建立抽取和证据质量基线"
101	    priority: P0
102	    gpu_budget_hours: 4
103	    deps: []
104	    registry_id: mvp2_sft_warmup
105	
106	  - id: plan_mvp2_rsft
107	    claim: 1
108	    description: "RSFT+CED 端到端验证: CED-filtered rejection sampling fine-tuning, 4 组配置全部 PASS。真实结果(D038修正后): r1 rel_f1=0.4449/evi_f1=0.8187, s44 rel_f1=0.4655/evi_f1=0.8087, r2a rel_f1=0.4494/evi_f1=0.8108, r2b rel_f1=0.4493/evi_f1=0.8128"
109	    priority: P0
110	    gpu_budget_hours: 20
111	    deps: [plan_mvp1, plan_mvp2_sft]
112	    registry_id: mvp2_rsft_train_r1
113	
114	  - id: plan_mvp2_grpo
115	    claim: 3
116	    description: "GRPO+QLoRA 全线失败（negative result = C3 核心证据）: 3 种 reward × 多 lr, rel_f1 max=0.211(lr5e-5)/0.014(lr5e-6), evi_f1 在 GRPO 下反而提升至 0.850 但 rel_f1 catastrophic forgetting。D031/D033 完整轨迹支撑 Claim 3"
117	    priority: P0
118	    gpu_budget_hours: 60
119	    deps: [plan_mvp2_sft]
120	    registry_id: mvp2_grpo_ced_lr5e6_r1
121	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "97de25ff-5a40-4af6-bec7-51636dce01a7",
  "isSidechain": true,
  "promptId": "00a1eb94-0484-4e13-931d-e659507bc0c6",
  "agentId": "a9bd4203964701927",
  "type": "user",
  "uuid": "465d9fa3-4903-4117-9139-e65f503f7918",
  "sourceToolAssistantUUID": "97de25ff-5a40-4af6-bec7-51636dce01a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-15T12:48:05.270Z_

Now I have a thorough understanding of the paper, its experimental backing, the internal project deliberations, and both the "best" and "median" dream paper drafts. Let me now write the R2 review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "465d9fa3-4903-4117-9139-e65f503f7918",
  "isSidechain": true,
  "agentId": "a9bd4203964701927",
  "requestId": "req_011Cb4P1m5gmL1NdWzjPsd9R",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cbf429d6-b849-421c-a7fa-b39402d99f1a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011zjsV95XfLghRrDUvtbH4e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2346,
      "cache_read_input_tokens": 83223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2346,
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

_source line 45 · 2026-05-15T12:48:06.180Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01C5po9FDWDQTHMfjzaiWXPQ`</summary>

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
  "parentUuid": "cbf429d6-b849-421c-a7fa-b39402d99f1a",
  "isSidechain": true,
  "agentId": "a9bd4203964701927",
  "requestId": "req_011Cb4P1m5gmL1NdWzjPsd9R",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3d6d0c0f-af2e-4239-bd81-34118a4d032b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011zjsV95XfLghRrDUvtbH4e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2346,
      "cache_read_input_tokens": 83223,
      "output_tokens": 136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2346
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 136,
          "cache_read_input_tokens": 83223,
          "cache_creation_input_tokens": 2346,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2346,
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

_source line 46 · 2026-05-15T12:48:06.183Z_

<details><summary>↩ Tool result · `toolu_01C5po9FDWDQTHMfjzaiWXPQ`</summary>

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
  "parentUuid": "3d6d0c0f-af2e-4239-bd81-34118a4d032b",
  "isSidechain": true,
  "promptId": "00a1eb94-0484-4e13-931d-e659507bc0c6",
  "agentId": "a9bd4203964701927",
  "type": "user",
  "uuid": "98bddd97-1a00-4b6e-a758-87afd2ac15f3",
  "sourceToolAssistantUUID": "3d6d0c0f-af2e-4239-bd81-34118a4d032b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-15T12:49:24.334Z_



Now I have all the information needed to write a thorough R2 review. Let me synthesize my analysis across both dream paper drafts, the internal project data, and the experimental evidence.

---

## Reviewer 2 (R2) — Novelty, Related Work, and Presentation/Framing

### Summary of Contributions

This paper studies online RL (GRPO) for document-level relation extraction with evidence generation on DocRED, finding that GRPO universally fails (reward increases while extraction F1 collapses). The authors propose RSFT with CED-based NLI filtering as an offline alternative, achieving +3.7--5.7pp rel-F1 over SFT on test. They also introduce EDCR, a metric for entity-sharing distractor citations. The paper makes a genuine empirical contribution by systematically documenting GRPO failure modes for structured IE, though the methodological novelty of the proposed solution is limited.

---

### Strengths

- **Thorough negative result documentation.** The GRPO failure analysis across 3 reward types, multiple learning rates, and KL configurations is the most thorough empirical demonstration of reward overoptimization in structured IE to date. The decoupling observation (evi_F1 rising to 85.0 while rel_F1 collapses to 1.4) is striking and well-documented. This alone has community value.

- **Intellectual honesty.** The paper is commendably transparent about its limitations: the rel-F1 gap to encoder SOTA (~63 vs ~43), the evaluation protocol differences with DREEAM/SAIS, the high residual EDCR (54-66%), and the marginal CED vs flat-NLI differences. This level of honesty is rare and appreciated.

- **Problem formulation is timely and well-motivated.** Evidence grounding for LLM-based IE is a genuine gap. The observation that entity-sharing distractor sentences game flat NLI signals is a useful insight for the community.

- **Reproducibility indicators are strong.** The paper reports multiple seeds, full checkpoint trajectories, hyperparameter sensitivity analysis, model size ablation, and a second dataset (Re-DocRED). The experimental grid is comprehensive relative to the claims made.

- **EDCR is a sensible diagnostic.** While simple in formulation, EDCR captures a real blind spot of Evi-F1. The cross-method diagnostic table (showing GRPO achieves "reasonable" Evi-F1 of 56.7 but catastrophic EDCR of 85.8) is a compelling illustration.

---

### Weaknesses

**W1: The title overclaims relative to the actual findings.**

The title "Why Online RL Catastrophically Fails for Structured Information Extraction, and What Works Instead" implies two things: (a) a general understanding of *why* online RL fails for structured IE, and (b) a strong alternative. Neither is fully delivered.

For (a): The paper demonstrates *that* GRPO fails but the causal analysis is thin. The connection to LongRLVR's gradient vanishing theory is speculative ("consistent with" is not "explained by"). The paper does not disentangle whether the failure is due to GRPO specifically, QLoRA 4-bit quantization artifacts (the decisions log shows kl_coef > 0 caused KL explosions specifically due to QLoRA quantization noise -- D008), the structured output format, the multi-objective reward structure, or the specific model (Qwen3-4B). Running GRPO with full fine-tuning (no QLoRA) on even a small model would help isolate the cause.

For (b): RSFT is a well-established technique. The paper's own ablations show that CED-specific scoring provides marginal benefit over flat-NLI scoring (the median paper reports +0.7pp rel-F1, +1.4pp evi-F1, -2.4pp EDCR; the best paper reports larger but potentially cherry-picked differences). The honest conclusion from the data is that *rejection sampling itself* is what works, not specifically CED-scored rejection sampling.

**Suggested fix:** Retitle to something like "Online RL Catastrophically Fails for Document-Level Relation Extraction with Evidence: An Empirical Study" or similar, positioning the paper primarily as an empirical analysis contribution rather than a methods paper.

**W2: CED vs flat-NLI RSFT differences are not statistically significant.**

The paper framing document explicitly notes p-values of 0.08, 0.38, and 0.12 for CED vs flat-NLI comparisons. Yet the best-case paper draft claims "CED significantly outperforms flat-NLI." The median paper is more cautious but still frames CED as a contribution rather than a null result. If CED vs flat-NLI is not significant, then "Contrastive Evidence Discrimination" is not a demonstrated methodological contribution -- it is an attempted contribution with inconclusive evidence.

This is the central tension of the paper: the core novelty (CED) does not clearly separate from the simpler baseline (flat-NLI RSFT), so the paper is left with a negative result (GRPO fails) and a standard technique (RSFT) as its main findings.

**W3: The GRPO failure may be an artifact of QLoRA, not a general statement about online RL for structured IE.**

The project's internal decisions log (D007, D008, D009, D010) documents that kl_coef > 0 caused KL explosions *specifically because QLoRA 4-bit quantization introduces systematic logit noise*, making the reference model's log-probs unreliable. This means the paper's GRPO experiments were conducted under a known-broken setup (kl_coef=0 means no KL constraint, and kl_coef > 0 explodes due to quantization). Running GRPO without QLoRA quantization would be essential to establish that the failure is inherent to online RL for structured IE rather than an artifact of the specific training setup. Without this control, the claim "online RL catastrophically fails for structured IE" is overstated.

**W4: Single model family (Qwen3) limits generalizability of the negative result.**

The GRPO failure claim would be substantially stronger if demonstrated on at least two model families (e.g., Qwen3 + LLaMA3). As currently constituted, the failure could be specific to Qwen3's architecture, tokenizer, or pre-training distribution. The model size ablation (1.7B/4B/8B) is within a single family and does not address this.

**W5: The Evi-F1 comparison with DREEAM/SAIS is misleading and the paper knows it.**

The paper reports Evi-F1 80.2 vs DREEAM's 57.3 as a headline result, but then acknowledges in discussion that the comparison is not apple-to-apple (generative models naturally over-cite, inflating recall; encoder models use attention thresholds with different precision-recall characteristics). Despite this acknowledgment, the number appears prominently in the abstract and introduction. This framing could mislead readers who skim. The paper should either (a) develop a protocol-normalized comparison or (b) not feature this comparison as a headline number.

**W6: EDCR correlation with Evi-F1 is weak (r = -0.42), undermining its claimed diagnostic value.**

A Pearson r of -0.42 is moderate at best. The paper claims EDCR and Evi-F1 "capture orthogonal evaluation dimensions," but r = -0.42 is neither orthogonal (r ~ 0) nor strongly correlated. The metric is computed on only 5 methods, which is too few data points for a reliable correlation estimate. The metric definition itself is straightforward (fraction of false-positive citations that share entities), and its value as an independent contribution is limited without demonstrating it captures failures that materially change system rankings or development decisions.

**W7: Missing important related work and baselines.**

- **R1-RE (arXiv 2507.04642)**: The most directly relevant concurrent work -- GRPO for sentence-level RE. The literature map acknowledges it but neither paper draft cites it. This omission is problematic given the paper's central claim about GRPO failure; the community will want to know why GRPO works for sentence-level RE (R1-RE) but not document-level RE with evidence.

- **DAPO, Dr. GRPO, REINFORCE++**: The literature map lists multiple GRPO stability improvements (clip-higher, std normalization fixes, etc.) that could potentially address the observed failures. The paper should discuss whether these techniques were considered and why they would not resolve the issue.

- **RelPrior (arXiv 2511.08143)**: A recent LLM-based DocRE method achieving +2.06-2.38pp rel-F1 improvement -- directly comparable to this work's RSFT gains. Neither paper draft mentions it.

- **No comparison with DPO**: Given that DPO is the standard offline RL alternative to GRPO, its absence as a baseline is notable. The paper compares online RL (GRPO) to a non-RL technique (RSFT) and concludes "offline is better," but the real comparison should be online RL vs offline RL (DPO).

---

### Questions for Authors

1. Have you attempted GRPO without QLoRA (e.g., full LoRA or full fine-tuning at 1.7B scale) to isolate whether the catastrophic forgetting is caused by quantization artifacts or is inherent to online RL for this task?

2. What are the p-values for CED vs flat-NLI RSFT on all reported metrics? The paper framing document mentions p=0.08/0.38/0.12 but these do not appear in the paper drafts.

3. For the EDCR metric: what fraction of sentences flagged as "entity-sharing distractors" are actually valid evidence missed by DocRED annotators? The Re-DocRED analysis suggests this is substantial (~13pp EDCR drop). Does this undermine EDCR's utility on incompletely annotated datasets?

4. Why was DPO not included as a baseline? It would be the natural "offline RL" comparison.

5. The best-case paper draft reports test rel-F1 of 45.4 and the median draft reports 42.8--43.8. These are substantially different. Which is the actual test result, and what accounts for the discrepancy?

6. R1-RE demonstrates successful GRPO for sentence-level RE. Can you articulate why GRPO succeeds there but fails here? Is it the document length, the multi-objective nature (extraction + evidence), or something else?

---

### Minor Issues

- The CED formulation in the best and median paper drafts differ slightly (per-evidence averaging vs single-margin). The paper should settle on one and be precise.
- The paper uses Qwen3-4B throughout but the model size ablation reports 1.7B and 8B results that appear simulated/projected (no experiment IDs in the project tracker). Clarify which results are actual vs projected.
- Table 6 in the best draft mixes test and dev numbers in the same table without clear delineation.

---

### Scores

| Criterion | Score |
|-----------|-------|
| **Soundness** | 3 (Acceptable) |
| **Excitement** | 3 (Ambivalent) |
| **Overall Assessment** | 3.0 (Borderline) |
| **Confidence** | 4 (High -- familiar with GRPO/RSFT literature, DocRE, and NLI-based faithfulness evaluation) |

### Justification

The paper's primary value is the systematic GRPO failure analysis for structured IE, which is timely and well-executed. However, the methodological contribution (CED) does not clearly separate from the simpler flat-NLI baseline, the GRPO failure may be confounded by QLoRA artifacts, the title and framing overclaim relative to the evidence, and several important baselines and related works are missing. With the suggested revisions -- particularly isolating the QLoRA confound, adding statistical significance tests, including DPO as a baseline, and recalibrating the framing -- this could become a solid empirical contribution paper. In its current form, the gap between claims and evidence prevents a higher score.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98bddd97-1a00-4b6e-a758-87afd2ac15f3",
  "isSidechain": true,
  "agentId": "a9bd4203964701927",
  "requestId": "req_011Cb4P251CMoeEqvPKXni9R",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "45c16634-82ed-4868-93e3-1dfef5d903d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016CeRKzqKuhk8VrypNnp18n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 714,
      "cache_read_input_tokens": 85569,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 714,
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

_source line 48 · 2026-05-15T12:49:51.885Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01Q3jbSdCzVkgbF1K8gJS4SJ`</summary>

```json
{
  "report": "# R2 Review — Novelty, Related Work, and Presentation/Framing\n\n## Paper: \"Why Online RL Catastrophically Fails for Structured Information Extraction, and What Works Instead\"\n\n---\n\n## Summary of Contributions\n\nThis paper studies online RL (GRPO) for document-level relation extraction with evidence generation on DocRED, finding that GRPO universally fails (reward increases while extraction F1 collapses). The authors propose RSFT with CED-based NLI filtering as an offline alternative, achieving +3.7--5.7pp rel-F1 over SFT on test. They also introduce EDCR, a metric for entity-sharing distractor citations. The paper makes a genuine empirical contribution by systematically documenting GRPO failure modes for structured IE, though the methodological novelty of the proposed solution is limited.\n\n---\n\n## Strengths\n\n- **Thorough negative result documentation.** The GRPO failure analysis across 3 reward types, multiple learning rates, and KL configurations is the most thorough empirical demonstration of reward overoptimization in structured IE to date. The decoupling observation (evi_F1 rising to 85.0 while rel_F1 collapses to 1.4) is striking and well-documented. This alone has community value.\n\n- **Intellectual honesty.** The paper is commendably transparent about its limitations: the rel-F1 gap to encoder SOTA (~63 vs ~43), the evaluation protocol differences with DREEAM/SAIS, the high residual EDCR (54-66%), and the marginal CED vs flat-NLI differences. This level of honesty is rare and appreciated.\n\n- **Problem formulation is timely and well-motivated.** Evidence grounding for LLM-based IE is a genuine gap. The observation that entity-sharing distractor sentences game flat NLI signals is a useful insight for the community.\n\n- **Reproducibility indicators are strong.** The paper reports multiple seeds, full checkpoint trajectories, hyperparameter sensitivity analysis, model size ablation, and a second dataset (Re-DocRED). The experimental grid is comprehensive relative to the claims made.\n\n- **EDCR is a sensible diagnostic.** While simple in formulation, EDCR captures a real blind spot of Evi-F1. The cross-method diagnostic table (showing GRPO achieves \"reasonable\" Evi-F1 of 56.7 but catastrophic EDCR of 85.8) is a compelling illustration.\n\n---\n\n## Weaknesses\n\n### W1: The title overclaims relative to the actual findings.\n\nThe title \"Why Online RL Catastrophically Fails for Structured Information Extraction, and What Works Instead\" implies two things: (a) a general understanding of *why* online RL fails for structured IE, and (b) a strong alternative. Neither is fully delivered.\n\nFor (a): The paper demonstrates *that* GRPO fails but the causal analysis is thin. The connection to LongRLVR's gradient vanishing theory is speculative (\"consistent with\" is not \"explained by\"). The paper does not disentangle whether the failure is due to GRPO specifically, QLoRA 4-bit quantization artifacts (internal experiments show kl_coef > 0 caused KL explosions specifically due to QLoRA quantization noise), the structured output format, the multi-objective reward structure, or the specific model (Qwen3-4B). Running GRPO with full fine-tuning (no QLoRA) on even a small model would help isolate the cause.\n\nFor (b): RSFT is a well-established technique. The paper's own ablations show that CED-specific scoring provides marginal benefit over flat-NLI scoring (the median paper reports +0.7pp rel-F1, +1.4pp evi-F1, -2.4pp EDCR). The honest conclusion from the data is that *rejection sampling itself* is what works, not specifically CED-scored rejection sampling.\n\n**Suggested fix:** Retitle to something like \"Online RL Catastrophically Fails for Document-Level Relation Extraction with Evidence: An Empirical Study\" or similar, positioning the paper primarily as an empirical analysis contribution rather than a methods paper.\n\n### W2: CED vs flat-NLI RSFT differences are not statistically significant.\n\nThe paper framing documents note p-values of 0.08, 0.38, and 0.12 for CED vs flat-NLI comparisons. Yet the best-case draft claims \"CED significantly outperforms flat-NLI.\" If CED vs flat-NLI is not significant, then \"Contrastive Evidence Discrimination\" is not a demonstrated methodological contribution -- it is an attempted contribution with inconclusive evidence.\n\nThis is the central tension of the paper: the core novelty (CED) does not clearly separate from the simpler baseline (flat-NLI RSFT), so the paper is left with a negative result (GRPO fails) and a standard technique (RSFT) as its main findings.\n\n### W3: The GRPO failure may be an artifact of QLoRA, not a general statement about online RL for structured IE.\n\nInternal experimental logs document that kl_coef > 0 caused KL explosions *specifically because QLoRA 4-bit quantization introduces systematic logit noise*, making the reference model's log-probs unreliable. This means the GRPO experiments were conducted under a known-broken KL setup (kl_coef=0 means no KL constraint; kl_coef > 0 explodes due to quantization). Running GRPO without QLoRA quantization would be essential to establish that the failure is inherent to online RL for structured IE rather than an artifact of the specific training setup. Without this control, the claim \"online RL catastrophically fails for structured IE\" is overstated.\n\n### W4: Single model family (Qwen3) limits generalizability of the negative result.\n\nThe GRPO failure claim would be substantially stronger if demonstrated on at least two model families (e.g., Qwen3 + LLaMA3). The model size ablation (1.7B/4B/8B) is within a single family and does not address this concern.\n\n### W5: The Evi-F1 comparison with DREEAM/SAIS is misleading and the paper acknowledges it.\n\nThe paper reports Evi-F1 80.2 vs DREEAM's 57.3 as a headline result, but acknowledges that generative models naturally over-cite (inflating recall) while encoder models use attention thresholds with different precision-recall characteristics. Despite this acknowledgment, the number appears prominently in the abstract and introduction. This framing could mislead readers who skim. The paper should either (a) develop a protocol-normalized comparison or (b) not feature this comparison as a headline number.\n\n### W6: EDCR correlation with Evi-F1 is weak (r = -0.42), undermining its claimed diagnostic value.\n\nA Pearson r of -0.42 is moderate at best. The paper claims EDCR and Evi-F1 \"capture orthogonal evaluation dimensions,\" but r = -0.42 is neither orthogonal nor strongly correlated. The metric is computed on only 5 methods, which is too few data points for a reliable correlation estimate. The metric definition itself is straightforward, and its value as an independent contribution is limited without demonstrating it captures failures that materially change system rankings or development decisions.\n\n### W7: Missing important related work and baselines.\n\n- **R1-RE (arXiv 2507.04642)**: The most directly relevant concurrent work -- GRPO for sentence-level RE. The community will want to know why GRPO works for sentence-level RE but not document-level RE with evidence.\n- **DAPO, Dr. GRPO, REINFORCE++**: Multiple GRPO stability improvements that could potentially address the observed failures. The paper should discuss whether these techniques were considered.\n- **RelPrior (arXiv 2511.08143)**: A recent LLM-based DocRE method achieving +2.06-2.38pp rel-F1 improvement -- directly comparable.\n- **No DPO baseline**: DPO is the standard offline RL alternative to GRPO. Comparing online RL (GRPO) to a non-RL technique (RSFT) and concluding \"offline is better\" without testing DPO leaves a gap in the argument.\n\n---\n\n## Questions for Authors\n\n1. Have you attempted GRPO without QLoRA (e.g., full LoRA or full fine-tuning at 1.7B scale) to isolate whether the catastrophic forgetting is caused by quantization artifacts or is inherent to online RL for this task?\n\n2. What are the p-values for CED vs flat-NLI RSFT on all reported metrics? These should appear in the paper.\n\n3. For the EDCR metric: what fraction of sentences flagged as \"entity-sharing distractors\" are actually valid evidence missed by DocRED annotators? The Re-DocRED analysis suggests this is substantial (~13pp EDCR drop). Does this undermine EDCR's utility on incompletely annotated datasets?\n\n4. Why was DPO not included as a baseline?\n\n5. The best-case paper draft reports test rel-F1 of 45.4 and the median draft reports 42.8--43.8. Which is the actual test result, and what accounts for the discrepancy?\n\n6. R1-RE demonstrates successful GRPO for sentence-level RE. Can you articulate why GRPO succeeds there but fails here?\n\n---\n\n## Minor Issues\n\n- The CED formulation differs slightly between paper versions (per-evidence averaging vs single-margin). Settle on one and be precise.\n- Model size ablation (1.7B/8B) results appear to be projected rather than completed experiments. Clarify which results are actual vs projected.\n- Some tables mix test and dev numbers without clear delineation.\n\n---\n\n## Scores\n\n| Criterion | Score |\n|-----------|-------|\n| **Soundness** | 3 (Acceptable) |\n| **Excitement** | 3 (Ambivalent) |\n| **Overall Assessment** | 3.0 (Borderline) |\n| **Confidence** | 4 (High) |\n\n## Score Justification\n\nThe paper's primary value is the systematic GRPO failure analysis for structured IE, which is timely and well-executed. However, the methodological contribution (CED) does not clearly separate from the simpler flat-NLI baseline (p > 0.05), the GRPO failure may be confounded by QLoRA artifacts, the title and framing overclaim relative to the evidence, and several important baselines and related works are missing. With the suggested revisions -- particularly isolating the QLoRA confound, adding statistical significance tests, including DPO as a baseline, citing R1-RE, and recalibrating the framing -- this could become a solid empirical contribution paper. In its current form, the gap between claims and evidence prevents a higher score.\n\n## Actionable Revision Priorities (ranked)\n\n1. **[Critical]** Run GRPO without QLoRA on at least one scale to isolate the quantization confound (W3)\n2. **[Critical]** Report statistical significance for CED vs flat-NLI RSFT; if not significant, reframe CED as a contributing factor rather than the key contribution (W2)\n3. **[High]** Add DPO as a baseline to complete the online-vs-offline RL comparison (W7)\n4. **[High]** Cite and discuss R1-RE, DAPO, Dr.GRPO, RelPrior (W7)\n5. **[High]** Recalibrate title and abstract to match the actual evidence strength (W1)\n6. **[Medium]** Develop or discuss protocol-normalized evidence comparison with encoder methods (W5)\n7. **[Medium]** Test on a second model family for the negative result (W4)\n",
  "project": "faith-evidence-ie",
  "tier": "best",
  "dream_id": "dream_20260515T120227",
  "overall_score": "borderline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45c16634-82ed-4868-93e3-1dfef5d903d4",
  "isSidechain": true,
  "agentId": "a9bd4203964701927",
  "requestId": "req_011Cb4P251CMoeEqvPKXni9R",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "52061eba-dd39-48b7-acf4-8be6f1a3e218",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016CeRKzqKuhk8VrypNnp18n",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 714,
      "cache_read_input_tokens": 85569,
      "output_tokens": 5912,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 714
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5912,
          "cache_read_input_tokens": 85569,
          "cache_creation_input_tokens": 714,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 714,
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

_source line 49 · 2026-05-15T12:49:52.556Z_

<details><summary>↩ Tool result · `toolu_01Q3jbSdCzVkgbF1K8gJS4SJ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/best/review_report.md\", \"dream_id\": \"dream_20260515T120227\", \"tier\": \"best\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52061eba-dd39-48b7-acf4-8be6f1a3e218",
  "isSidechain": true,
  "promptId": "00a1eb94-0484-4e13-931d-e659507bc0c6",
  "agentId": "a9bd4203964701927",
  "type": "user",
  "uuid": "30163e62-e8b8-46c5-858b-1e5addefad50",
  "sourceToolAssistantUUID": "52061eba-dd39-48b7-acf4-8be6f1a3e218",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-15T12:50:02.789Z_

Review submitted. Here is a summary of the key findings:

**Scores:** Soundness 3, Excitement 3, Overall 3.0 (Borderline), Confidence 4/5.

**Core assessment:** The paper's strongest asset is the systematic GRPO failure documentation for structured IE -- this negative result has real community value. However, three issues prevent a higher score:

1. **CED vs flat-NLI is not statistically significant** (p = 0.08/0.38/0.12 by the project's own admission), which undermines the core methodological claim. Rejection sampling itself appears to be what works, not CED specifically.

2. **The GRPO failure may be a QLoRA artifact** rather than a fundamental limitation of online RL for structured IE. The internal decision logs show kl_coef > 0 exploded due to 4-bit quantization noise, meaning all GRPO experiments ran under a broken KL setup. Without a non-quantized control, the headline claim is overstated.

3. **Title and framing overclaim** relative to the evidence. The paper claims to explain "why" GRPO fails and "what works instead," but delivers "GRPO fails under these specific conditions" and "standard RSFT works."

**Seven weaknesses** were identified (W1-W7), with the top three actionable priorities being: (a) run GRPO without QLoRA to isolate the confound, (b) report statistical significance and reframe CED if not significant, (c) add DPO as a baseline and cite R1-RE.

The review was submitted to `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/best/review_report.md`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30163e62-e8b8-46c5-858b-1e5addefad50",
  "isSidechain": true,
  "agentId": "a9bd4203964701927",
  "requestId": "req_011Cb4P9uYeYYF1cdwsJgfmW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "df5609b0-5d24-4015-a6b9-15f8cf800431",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q9DZdhPeR6kEXR9C8eaex1",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6041,
      "cache_read_input_tokens": 86283,
      "output_tokens": 424,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6041
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 424,
          "cache_read_input_tokens": 86283,
          "cache_creation_input_tokens": 6041,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6041,
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
