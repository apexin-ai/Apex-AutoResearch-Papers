# Research conversation: You are Reviewer R2 for an academic paper review at a top ML venue (acceptance rate ~25%, 6-point scale: 1=Strong Reject

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 60
- **Recorded user turns:** 1
- **Tool calls:** 25
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-ade4d670d78b2afaf.jsonl`
- **Structured JSON:** [`60c97dfa6c32188cd568.json`](../../sessions/60/60c97dfa6c32188cd568.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

60 recorded events

### User

_source line 1 · 2026-05-16T10:42:36.291Z_

You are Reviewer R2 for an academic paper review at a top ML venue (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 6=Strong Accept). Your focus is **novelty and related work**.

## Paper Summary
Title: "Collapse Monitoring Is Harder Than It Looks: Configuration-Dependent Signal Behavior in Iterative Model Collapse"

The paper investigates whether training-time signals can reliably monitor model collapse severity during iterative fine-tuning on synthetic data. It tests 4 signal families (spectral, output, gradient, downstream) across 6 contamination levels, 3 model scales (0.5B, 1.5B, 3B), 2 text domains (WikiText, PubMed), 2 fine-tuning methods (QLoRA, Full FT), and 2 architectures (Qwen, LLaMA). The main finding is negative: no single signal reliably tracks collapse across all configurations.

## Key Claims
1. Signal-severity correlation is conditional on configuration
2. Within-generation early warning is scale-dependent
3. Signal behavior is architecture- and method-dependent

## Paper References (10 total)
[1] Shumailov et al. 2024 - Nature paper on model collapse
[2] Alemohammad et al. 2024 - Self-consuming generative models (ICLR)
[3] Dohmatob et al. 2024 - Model collapse as scaling law change (ICML)
[4] Gerstgrasser et al. 2024 - Is model collapse inevitable? (NeurIPS)
[5] Deng et al. 2025 - SIGMA spectral analysis for collapse detection
[6] Kalinowski et al. 2024 - TDA for collapse detection
[7] Kazdan et al. 2024 - Collapse or thrive?
[8] Briesch et al. 2023 - Self-consuming training loop
[9] Seddik et al. 2024 - Statistical analysis of language model collapse
[10] Hataya et al. 2023 - Large-scale generative models corrupt datasets (ICCV)

## Experimental Details
- Models: Qwen2.5-0.5B/1.5B/3B, LLaMA-3.2-1B
- Datasets: WikiText-2, PubMed abstracts
- Signals: stable rank, spectral entropy, perplexity, token entropy, training loss, gradient norm, HellaSwag, MMLU-mini, self-BLEU, distinct-1/2/3
- Fine-tuning: QLoRA (rank 64), Full FT
- Framing: Negative-result taxonomy paper

## Key Results
- No single signal reliably tracks collapse across configurations
- Stable rank AUC drops 0.984→0.71 from 0.5B to 1.5B
- Stable rank reverses direction in LLaMA at moderate contamination
- Collapse signal magnitude monotonically decreases with scale (SR: 6.6x→3.4x→2.4x)
- Signal rankings unstable across domains (4/7 match WikiText vs PubMed)
- Only 5/11 signals direction-consistent between Qwen and LLaMA
- PPL provides no within-gen early warning at 0.5B (AUC=0.534) but improves at 1.5B (0.66)
- Recovery domain-dependent (100% WikiText vs 60% PubMed)

## SIGMA Relationship
Paper mentions SIGMA [5] but did NOT complete empirical comparison (plan_009 was killed). Differentiation is purely methodological (reference-free vs reference-required). This is acknowledged in Section 4.3.

## Experimental Gaps (from review context)
- 1.5B validation: only 10/30 runs completed
- Full FT comparison: N=1 only (plan_012 for multi-seed never ran)
- SIGMA comparison: no data (plan_009 killed)
- LLaMA: f=100% incomplete
- All claims beyond 0.5B have very limited statistical power

## Your Task
Write a detailed R2 review focusing on:
1. **Novelty assessment** (is "signals don't generalize across configs" a novel finding? incremental? obvious?)
2. **Related work coverage** (missing references, inadequate positioning, related work that already shows similar results)
3. **Contribution significance** (does this advance the field? who benefits?)
4. **Framing quality** (is the negative-result framing effective? does the paper sell its contributions well?)
5. **Writing quality** (clarity, organization, presentation)
6. **Specific weaknesses** (numbered list)
7. **Specific strengths** (numbered list)
8. **Questions for authors**
9. **Overall score** (1-6) with justification
10. **Confidence** (1-5)

Be rigorous but fair. Negative-result papers CAN be valuable at top venues (e.g., EMNLP has a negative results track). Evaluate whether this paper meets that bar—is the negative result surprising enough, is the methodology strong enough to support the claims, and does the paper provide actionable insights?

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "80dd2a4d-c31a-43ae-8316-4a6135d9fed6",
  "agentId": "ade4d670d78b2afaf",
  "type": "user",
  "uuid": "ec3c5a97-64a7-4655-99b4-a8fbcd1c7eed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T10:42:36.300Z_

```json
{
  "parentUuid": "ec3c5a97-64a7-4655-99b4-a8fbcd1c7eed",
  "isSidechain": true,
  "agentId": "ade4d670d78b2afaf",
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
  "uuid": "f8d01c15-d5b4-444d-bcca-509545d71041",
  "timestamp": "2026-05-16T10:42:36.300Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-16T10:42:38.511Z_



I'll start by reading the paper's key files to understand the full content before writing my review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8d01c15-d5b4-444d-bcca-509545d71041",
  "isSidechain": true,
  "agentId": "ade4d670d78b2afaf",
  "requestId": "req_011Cb67FvQoFv5oSWuq838iB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dad1a806-10cb-4c9b-8442-d40c9066aff5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N3xoU1mfxV8dQ55qdi8TQJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7076,
      "cache_read_input_tokens": 8249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7076,
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

_source line 4 · 2026-05-16T10:42:39.367Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Nc3iGrbnnbaA99zQVsmFci`</summary>

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
  "parentUuid": "dad1a806-10cb-4c9b-8442-d40c9066aff5",
  "isSidechain": true,
  "agentId": "ade4d670d78b2afaf",
  "requestId": "req_011Cb67FvQoFv5oSWuq838iB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a21ad49a-3480-4fb3-a395-a776ac405bf0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N3xoU1mfxV8dQ55qdi8TQJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7076,
      "cache_read_input_tokens": 8249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7076,
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

_source line 5 · 2026-05-16T10:42:39.374Z_

<details><summary>↩ Tool result · `toolu_01Nc3iGrbnnbaA99zQVsmFci`</summary>

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
  "parentUuid": "a21ad49a-3480-4fb3-a395-a776ac405bf0",
  "isSidechain": true,
  "promptId": "80dd2a4d-c31a-43ae-8316-4a6135d9fed6",
  "agentId": "ade4d670d78b2afaf",
  "type": "user",
  "uuid": "48efb900-7e64-401e-8937-45bb56f120ea",
  "sourceToolAssistantUUID": "a21ad49a-3480-4fb3-a395-a776ac405bf0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-16T10:42:41.447Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01GsE1i58BfLs542KSMGT3E5`</summary>

```json
{
  "project": "collapse_severity_monitor"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48efb900-7e64-401e-8937-45bb56f120ea",
  "isSidechain": true,
  "agentId": "ade4d670d78b2afaf",
  "requestId": "req_011Cb67GA5L2rmHZoxtjkVgR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2a3a1965-1ceb-4550-8d6b-5ba7c1cd3028",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LWasMhVEwiAUJCg4omHVQq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1449,
      "cache_read_input_tokens": 15325,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1449,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 48,
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

_source line 7 · 2026-05-16T10:42:41.640Z_

<details><summary>↩ Tool result · `toolu_01GsE1i58BfLs542KSMGT3E5`</summary>

```text
{"result":"# 项目 collapse_severity_monitor 概况\n\n## 实验状态 (35 个)\n\n- **plan_002_pubmed_1.5B_3seeds**: DONE (killed) — \n- **per_layer_analysis_v5**: DONE (success) — \n- **mvp_frac50_100**: DONE (success) — \n- **plan001-wikitext-15B-5seeds-gpu1**: DONE (failed) — \n- **plan_001_wikitext_15B_5seeds**: PREPARING (killed) — \n- **plan_001_wikitext_1.5B_5seeds**: DONE (killed) — \n- **per_layer_analysis_active**: DONE (failed) — \n- **per_layer_analysis_v4**: DONE (failed) — \n- **per_layer_analysis_v3**: DONE (failed) — \n- **per_layer_analysis_v2**: DONE (killed) — \n- **per_layer_analysis**: DONE (failed) — \n- **mvp_frac0**: DONE (success) — \n- **mvp_collapse_003**: DONE (killed) — \n- **mvp_collapse_002**: DONE (killed) — \n- **mvp_collapse_001**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-16\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| plan010-3B-spotcheck | 3B model spot-check: collapse severity signals 在第三个 scale point (3B) 上保持一致，增强 cross-scale claims | — | — | — |\n| plan002-pubmed-cqa1 | Cross-domain validation: collapse severity signals 在 PubMed biomedical domain 上保持 ρ > 0.7 相关性，证明信号的 domain-agnostic 特性 | — | — | — |\n| plan001_v2_gpu0 | Scale validation (GPU 0 restart): fractions (0.0, 0.25, 0.1) × 5 seeds on 1.5B model. Restart after timeout, skip logic enabled, timeout=48h. | — | — | — |\n\n## 待处理\n- plan001-cqa1-seed46: Scale validation (cqa1 acceleration): seed46 × 6 fractions × 5 gens on 1.5B model, QLoRA, WikiText-2. Offloaded from autodl-5090 to cqa1 cuda:2 for parallel speedup.（已分配 ? GPU:?，等待提交）\n- plan001-cqa1-seed45: Scale validation (cqa1 acceleration): seed45 × 6 fractions × 5 gens on 1.5B model, QLoRA, WikiText-2. Offloaded from autodl-5090 to cqa1 cuda:1 for parallel speedup.（准备中）\n- plan001-cqa1-seed44: Scale validation (cqa1 acceleration): seed44 × 6 fractions × 5 gens on 1.5B model, QLoRA, WikiText-2. Offloaded from autodl-5090 to cqa1 cuda:0 for parallel speedup.（准备中）\n- plan_001_seed43_frac50（准备中）\n- plan_001_seed43_frac0（准备中）\n- plan_001_seed42_frac50（准备中）\n- plan_001_seed42_frac0（准备中）\n- plan_001_wikitext_15B_5seeds: Scale validation: training dynamic signals (spectral/output/downstream) 在 1.5B 模型上以 Spearman ρ > 0.7 跟踪 collapse severity，且 5 seeds 的 variance 足够小以支持统计显著性 claim（准备中）\n\n## 近期结论\n- **plan011-llama-download** (success): —\n- **plan008-self-recovery** (success): Self-recovery deep dive (Claim 3): analyze spike-then-recover pattern at 50% synthetic mixing, quantify recovery ratios by signal family, assess cross-seed consistency\n  [plan008-self-recovery-report](/api/workspace-files/projects/collapse_severity_monitor/artifacts/plan008-self-recovery/report/report.md) | [plan008-recovery-patterns-csv](/api/workspace-files/projects/collapse_severity_monitor/artifacts/plan008-self-recovery/data/recovery_patterns.csv)\n- **plan002-pubmed-gpu2-tail** (success): —\n\n## 趋势\n成功 9 / 负向 0 / 失败 8 / 共 24\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nautodl-5090: 空闲 cuda:0, cuda:1\ncqa1-37219: 无 GPU 信息\n\n## 告警\n- mvp_collapse_001: 训练失败 — unknown\n- mvp_collapse_002: 已被终止 — unknown\n- mvp_collapse_003: 已被终止 — unknown\n- per_layer_analysis: 训练失败 — unknown\n- per_layer_analysis_v2: 已被终止 — unknown\n- per_layer_analysis_v3: 训练失败 — unknown\n- per_layer_analysis_active: 训练失败 — unknown\n- per_layer_analysis_v4: 训练失败 — unknown\n- plan_001_wikitext_1.5B_5seeds: 已被终止 — unknown\n- plan_002_pubmed_1.5B_3seeds: 已被终止 — unknown\n- plan001-wikitext-15B-5seeds: 训练失败 — unknown\n- plan001-wikitext-15B-5seeds-gpu1: 训练失败 — unknown\n- plan001-gpu1: 已被终止 — unknown\n- plan009-sigma-headtohead: 已被终止 — unknown\n- plan002-pubmed-gpu2: 训练失败 — unknown\n\n## 研究想法\n# Idea Inbox\n\n## 待验证\n\n- [2026-05-15] **⚠️ PROVISIONAL — SIGMA 方向差异假设（C001 约束，N=2 未验证）。** 初步观察：data corruption collapse 下 effective_rank↑（表示弥散），而 SIGMA 论文的 recursive collapse 下 effective_rank↓（表示收缩）。方向相反。**此为 provisional 假设，需 plan_001 seed43-46 + plan_003 Full FT SIGMA 数据验证后才能定论。禁止在论文或分析中当已验证结论使用。**\n- [2026-05-15] **Gen1 phase-transition 模式（Reviewer 提出，n=2 初步确认）。** 处理组信号呈 gen0→gen1 剧变 + gen2-4 plateau 模式，非单调。暗示第一代 synthetic data corruption 冲击最大，后续代次模型\"适应\" corrupted distribution。若 plan_001 全数据确认，可作为 Claim C3（non-uniform behavior）的补充证据或独立发现。需要 cross-fraction 验证此模式是否随 contamination fraction 增大而加剧。\n\n## ACTIVE"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a3a1965-1ceb-4550-8d6b-5ba7c1cd3028",
  "isSidechain": true,
  "promptId": "80dd2a4d-c31a-43ae-8316-4a6135d9fed6",
  "agentId": "ade4d670d78b2afaf",
  "type": "user",
  "uuid": "14ccfc9d-0149-434a-88c9-2f94674b01ed",
  "sourceToolAssistantUUID": "2a3a1965-1ceb-4550-8d6b-5ba7c1cd3028",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-16T10:42:42.443Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01GZTF7gkAUg4oUgQgqUvKgz`</summary>

```json
{
  "project": "collapse_severity_monitor",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14ccfc9d-0149-434a-88c9-2f94674b01ed",
  "isSidechain": true,
  "agentId": "ade4d670d78b2afaf",
  "requestId": "req_011Cb67GA5L2rmHZoxtjkVgR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "743f2738-3f17-47fa-a9b3-16b25ee51174",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LWasMhVEwiAUJCg4omHVQq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1449,
      "cache_read_input_tokens": 15325,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1449,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 48,
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

_source line 9 · 2026-05-16T10:42:42.465Z_

<details><summary>↩ Tool result · `toolu_01GZTF7gkAUg4oUgQgqUvKgz`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/report.md\", \"content\": \"# Handover — 2026-05-16\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| plan010-3B-spotcheck | 3B model spot-check: collapse severity signals 在第三个 scale point (3B) 上保持一致，增强 cross-scale claims | — | — | — |\\n| plan002-pubmed-cqa1 | Cross-domain validation: collapse severity signals 在 PubMed biomedical domain 上保持 ρ > 0.7 相关性，证明信号的 domain-agnostic 特性 | — | — | — |\\n| plan001_v2_gpu0 | Scale validation (GPU 0 restart): fractions (0.0, 0.25, 0.1) × 5 seeds on 1.5B model. Restart after timeout, skip logic enabled, timeout=48h. | — | — | — |\\n\\n## 待处理\\n- plan001-cqa1-seed46: Scale validation (cqa1 acceleration): seed46 × 6 fractions × 5 gens on 1.5B model, QLoRA, WikiText-2. Offloaded from autodl-5090 to cqa1 cuda:2 for parallel speedup.（已分配 ? GPU:?，等待提交）\\n- plan001-cqa1-seed45: Scale validation (cqa1 acceleration): seed45 × 6 fractions × 5 gens on 1.5B model, QLoRA, WikiText-2. Offloaded from autodl-5090 to cqa1 cuda:1 for parallel speedup.（准备中）\\n- plan001-cqa1-seed44: Scale validation (cqa1 acceleration): seed44 × 6 fractions × 5 gens on 1.5B model, QLoRA, WikiText-2. Offloaded from autodl-5090 to cqa1 cuda:0 for parallel speedup.（准备中）\\n- plan_001_seed43_frac50（准备中）\\n- plan_001_seed43_frac0（准备中）\\n- plan_001_seed42_frac50（准备中）\\n- plan_001_seed42_frac0（准备中）\\n- plan_001_wikitext_15B_5seeds: Scale validation: training dynamic signals (spectral/output/downstream) 在 1.5B 模型上以 Spearman ρ > 0.7 跟踪 collapse severity，且 5 seeds 的 variance 足够小以支持统计显著性 claim（准备中）\\n\\n## 近期结论\\n- **plan011-llama-download** (success): —\\n- **plan008-self-recovery** (success): Self-recovery deep dive (Claim 3): analyze spike-then-recover pattern at 50% synthetic mixing, quantify recovery ratios by signal family, assess cross-seed consistency\\n  [plan008-self-recovery-report](/api/workspace-files/projects/collapse_severity_monitor/artifacts/plan008-self-recovery/report/report.md) | [plan008-recovery-patterns-csv](/api/workspace-files/projects/collapse_severity_monitor/artifacts/plan008-self-recovery/data/recovery_patterns.csv)\\n- **plan002-pubmed-gpu2-tail** (success): —\\n\\n## 趋势\\n成功 9 / 负向 0 / 失败 8 / 共 24\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nautodl-5090: 空闲 cuda:0, cuda:1\\ncqa1-37219: 无 GPU 信息\\n\\n## 告警\\n- mvp_collapse_001: 训练失败 — unknown\\n- mvp_collapse_002: 已被终止 — unknown\\n- mvp_collapse_003: 已被终止 — unknown\\n- per_layer_analysis: 训练失败 — unknown\\n- per_layer_analysis_v2: 已被终止 — unknown\\n- per_layer_analysis_v3: 训练失败 — unknown\\n- per_layer_analysis_active: 训练失败 — unknown\\n- per_layer_analysis_v4: 训练失败 — unknown\\n- plan_001_wikitext_1.5B_5seeds: 已被终止 — unknown\\n- plan_002_pubmed_1.5B_3seeds: 已被终止 — unknown\\n- plan001-wikitext-15B-5seeds: 训练失败 — unknown\\n- plan001-wikitext-15B-5seeds-gpu1: 训练失败 — unknown\\n- plan001-gpu1: 已被终止 — unknown\\n- plan009-sigma-headtohead: 已被终止 — unknown\\n- plan002-pubmed-gpu2: 训练失败 — unknown\\n\", \"total_chars\": 2867, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "743f2738-3f17-47fa-a9b3-16b25ee51174",
  "isSidechain": true,
  "promptId": "80dd2a4d-c31a-43ae-8316-4a6135d9fed6",
  "agentId": "ade4d670d78b2afaf",
  "type": "user",
  "uuid": "4b76ead3-c945-4894-bce4-dafbbb59ba81",
  "sourceToolAssistantUUID": "743f2738-3f17-47fa-a9b3-16b25ee51174",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-16T10:42:43.124Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_019qTszGKzQJPx78h779BTsB`</summary>

```json
{
  "project": "collapse_severity_monitor",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b76ead3-c945-4894-bce4-dafbbb59ba81",
  "isSidechain": true,
  "agentId": "ade4d670d78b2afaf",
  "requestId": "req_011Cb67GA5L2rmHZoxtjkVgR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1c07f244-cea3-4084-bbae-c2c80fc49574",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LWasMhVEwiAUJCg4omHVQq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1449,
      "cache_read_input_tokens": 15325,
      "output_tokens": 251,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1449
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 251,
          "cache_read_input_tokens": 15325,
          "cache_creation_input_tokens": 1449,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1449,
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

_source line 11 · 2026-05-16T10:42:43.149Z_

<details><summary>↩ Tool result · `toolu_019qTszGKzQJPx78h779BTsB`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/literature_map.yaml\", \"content\": \"# Literature Map — collapse_severity_monitor\\n# 最后更新: 2026-05-14 (expanded to 37 papers)\\n# 研究方向: 在线监控模型 collapse 严重度——用训练动态信号实时跟踪迭代合成数据训练中的质量退化\\n\\n# ============================================================\\n# 竞争关系分类说明:\\n#   direct_competitor  — 解决同一问题（在线监控 collapse）\\n#   related            — 解决相近问题或使用相关方法\\n#   complementary      — 互补（提供理论基础/工具/缓解策略）\\n#   foundation         — 领域基础工作\\n# ============================================================\\n\\npapers:\\n\\n  # ===================== DIRECT COMPETITORS =====================\\n\\n  - id: sigma_2026\\n    title: \\\"SIGMA: Scalable Spectral Insights for LLM Model Collapse\\\"\\n    authors: [Yi Gu, Lingyou Pang, Xiangkun Ye, Tianyu Wang, Jianyu Lin, Carey E. Priebe, Alexander Aue]\\n    year: 2026\\n    venue: arXiv (2601.03385)\\n    relation: direct_competitor\\n    core_method: >\\n      通过 embedding Gram 矩阵的谱分析来量化 model collapse 程度。\\n      推导 Gram 矩阵谱的确定性和随机性界，用谱收缩作为 collapse 指标。\\n    signals: [Gram matrix spectrum, rank deficiency, spectral bounds]\\n    scale: model-level (output embeddings)\\n    key_findings:\\n      - Gram 矩阵满秩是 LLM 正常运作的必要条件\\n      - 秩亏缺意味着语义级信息丢失，标志 collapse 开始\\n      - 随机公式使框架可扩展至大规模模型\\n    vs_ours: >\\n      SIGMA 用输出嵌入的 Gram 矩阵谱，是事后/黑盒方法，不需要模型权重。\\n      我们用训练动态信号（权重频谱熵、stable rank、token entropy），\\n      是训练中实时监控，更早期更细粒度（per-layer）。\\n      SIGMA 不做 per-layer 分析，不跟踪训练过程的动态变化。\\n    threat_level: medium\\n\\n  - id: kalinowski_2026\\n    title: \\\"Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index\\\"\\n    authors: [Alexander Kalinowski]\\n    year: 2026\\n    venue: arXiv (2604.26984)\\n    relation: direct_competitor\\n    core_method: >\\n      提出在线拓扑感知监控器，结合 Modular Morse Homology Maintenance (MMHM)\\n      和复合 Collapse Index (CI)，通过稀疏增量更新实现快速在线监控。\\n    signals: [persistent homology, Collapse Index (CI), topological features]\\n    scale: model-level (representation space topology)\\n    key_findings:\\n      - CI 在 LLM fine-tuning 和时序 KGE 训练中提供低延迟早期预警\\n      - 表征各向异性和多尺度结构丧失在性能指标反应之前就可检测\\n      - 增量更新避免每个 epoch 重建复形\\n    vs_ours: >\\n      Kalinowski 用拓扑信号（persistent homology），我们用频谱/熵信号。\\n      两者都是在线监控，但信号族完全不同。我们的信号更轻量、\\n      更可解释（stable rank/spectral entropy 有直接的线性代数含义）。\\n      Kalinowski 不研究迭代合成数据训练场景。\\n    threat_level: medium\\n\\n  # ===================== CLOSELY RELATED =====================\\n\\n  - id: spectral_lens_2026\\n    title: \\\"Spectral Lens: Activation and Gradient Spectra as Diagnostics of LLM Optimization\\\"\\n    authors: [Andy Zeyi Liu et al.]\\n    year: 2026\\n    venue: arXiv (2605.05683)\\n    relation: related\\n    core_method: >\\n      用 activation covariance 和 per-sample gradient 的 SVD 谱\\n      作为 LLM 训练优化的诊断工具。\\n    signals: [activation covariance spectrum, gradient SVD spectrum]\\n    scale: layer-level\\n    key_findings:\\n      - batch size 是表示几何的隐藏决定因素\\n      - 早期训练的 activation covariance 尾部可预测下游 token 效率\\n      - activation 谱头部运动 + gradient 谱可区分学习侧和执行侧改进\\n    vs_ours: >\\n      方法论高度相关——同样用频谱分析训练动态。\\n      但他们关注优化诊断，不研究 collapse/合成数据退化。\\n      可作为方法论参考。\\n    threat_level: low\\n\\n  - id: shi_neurips2025\\n    title: \\\"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\\\"\\n    authors: [Lianghe Shi, Meng Wu, Huijie Zhang, Zekai Zhang, Molei Tao, Qing Qu]\\n    year: 2025\\n    venue: NeurIPS 2025 (Spotlight)\\n    relation: related\\n    core_method: >\\n      揭示 model collapse 中从泛化到记忆的转变。\\n      发现训练数据熵与模型泛化能力的强线性相关。\\n      提出基于熵的子集选择方法来减缓 collapse。\\n    signals: [dataset entropy, generalization metrics]\\n    scale: model-level (data distribution)\\n    key_findings:\\n      - 迭代训练中数据分布熵急剧下降导致泛化能力下降\\n      - 强线性相关：训练数据集熵与模型泛化能力\\n      - 熵选择方法有效减缓泛化到记忆转变\\n    vs_ours: >\\n      他们用数据级别的熵，我们用模型内部的训练动态信号。\\n      互补：他们的数据熵可作为我们的外部验证指标。\\n      他们不做 per-layer 分析，不做在线监控。\\n    threat_level: low\\n\\n  - id: wyss_2024\\n    title: \\\"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI\\\"\\n    authors: [C. M. Wyss et al.]\\n    year: 2024\\n    venue: arXiv (2410.12341)\\n    relation: related\\n    core_method: >\\n      用语义网络和 next-token 概率来表征 LLM 中的 model collapse。\\n      引入 collapsed prediction 概念量化多样性损失。\\n      分析不同合成 token 比例 (25%/50%/75%) 对 collapse 的影响。\\n    signals: [next-token probability distribution, semantic network metrics, collapsed prediction ratio]\\n    scale: token-level (output)\\n    key_findings:\\n      - Next-token 概率分布可精确量化多样性损失\\n      - 合成 token 比例越高，collapse 越严重\\n      - 跨数据集迁移：在非微调数据集上 collapse 程度不同\\n    vs_ours: >\\n      他们用输出级指标（next-token prob），我们用训练动态内部信号。\\n      他们的 synthetic fraction 实验与我们的实验设计有重叠。\\n      不同之处：他们是事后分析，我们是训练中在线监控。\\n    threat_level: low\\n\\n  - id: xu_2026\\n    title: \\\"Predicting LLM Compression Degradation from Spectral Statistics\\\"\\n    authors: [Mingxue Xu]\\n    year: 2026\\n    venue: arXiv (2604.18085)\\n    relation: related\\n    core_method: >\\n      用 stable rank 和信息密度 (bits/param) 预测 LLM 压缩导致的退化。\\n      交互项 compression_ratio * stable_rank 是退化的强预测器。\\n    signals: [stable rank, information density, compression ratio]\\n    scale: layer-level (attention vs MLP 分开分析)\\n    key_findings:\\n      - stable rank 是压缩退化的主要预测因子（Pearson r=0.890 attention, 0.839 MLP）\\n      - 层类型比压缩方法更重要\\n      - layer-specific calibration 优于 method-specific tuning\\n    vs_ours: >\\n      直接验证 stable rank 作为退化预测信号的有效性。\\n      虽然场景不同（压缩 vs collapse），但支持我们选用 stable rank 的合理性。\\n      他们的 per-layer 分析方法可参考。\\n    threat_level: low\\n\\n  - id: layer_collapse_diffusion_2026\\n    title: \\\"Layer Collapse in Diffusion Language Models\\\"\\n    authors: [Alexander Conzelmann, Albert Catalan-Tatjer, Shiwei Liu]\\n    year: 2026\\n    venue: arXiv (2605.06366)\\n    relation: related\\n    core_method: >\\n      分析 diffusion language model (LLaDA-8B) 中的 per-layer activation 动态，\\n      发现少数早期层展现 collapsed activation patterns。\\n    signals: [activation patterns, super-outlier magnitude]\\n    scale: layer-level\\n    key_findings:\\n      - 几个早期层出现 channel-axis collapse（单一维度主导所有位置）\\n      - 尽管看似冗余，pruning outlier 导致退化为重复随机 token 循环\\n      - Diffusion LM 与 autoregressive LM 的 collapse 行为不同\\n    vs_ours: >\\n      做了 per-layer collapse 分析，但在 diffusion LM 上。\\n      方法论参考：per-layer activation 分析方法。\\n    threat_level: low\\n\\n  # ===================== FOUNDATION =====================\\n\\n  - id: alemohammad_iclr2024\\n    title: \\\"Self-Consuming Generative Models Go MAD\\\"\\n    authors: [Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard G. Baraniuk]\\n    year: 2024\\n    venue: ICLR 2024\\n    relation: foundation\\n    core_method: >\\n      定义三种 autophagous loop（fully synthetic / synthetic augmentation / fresh data），\\n      证明无足够真实数据时 precision 或 recall 必然下降（MAD 现象）。\\n    signals: [FID, precision, recall]\\n    scale: model-level (image generative models)\\n    key_findings:\\n      - 三种 loop 类型的 collapse 行为不同\\n      - 无 fresh data 时 quality 或 diversity 必然退化\\n      - 在 StyleGAN、DDPM、denoising diffusion 上验证\\n    vs_ours: >\\n      领域基础论文之一。他们的 loop 分类框架直接对应我们的实验设计。\\n      他们用 FID/precision/recall（事后指标），我们提供训练中在线信号。\\n\\n  - id: papyan_pnas2020\\n    title: \\\"Prevalence of Neural Collapse during the Terminal Phase of Deep Learning Training\\\"\\n    authors: [Vardan Papyan, X. Y. Han, David L. Donoho]\\n    year: 2020\\n    venue: PNAS 117(40), 24652-24663\\n    relation: foundation\\n    core_method: >\\n      发现分类网络训练末期的 Neural Collapse——类内表征收缩到 Simplex ETF。\\n    signals: [within-class variability, classifier-mean alignment]\\n    scale: model-level (last-layer representations)\\n    key_findings:\\n      - 训练末期出现四种 collapse 现象\\n      - 类均值收敛到 Simplex ETF 顶点\\n      - Collapse 与泛化能力相关\\n    vs_ours: >\\n      虽然 neural collapse 与 model collapse 是不同概念，\\n      但谱分析方法论可借鉴，且提供 \\\"collapse\\\" 概念的对比参考。\\n\\n  - id: hataya_iccv2023\\n    title: \\\"Will Large-scale Generative Models Corrupt Future Datasets?\\\"\\n    authors: [Ryuichiro Hataya, Han Bao, Hiromi Arai]\\n    year: 2023\\n    venue: ICCV 2023 (pp. 20555-20565)\\n    relation: foundation\\n    core_method: >\\n      用 SOTA 生成模型生成 ImageNet/COCO 规模数据集，\\n      评估\\\"被污染\\\"数据集在分类和生成任务上的下游性能退化。\\n    signals: [classification accuracy, FID, generation quality]\\n    scale: dataset-level (ImageNet/COCO scale)\\n    key_findings:\\n      - 生成图像对下游性能有负面影响\\n      - 影响程度取决于任务类型和生成图像比例\\n      - 首次在 ImageNet 规模验证数据集污染效应\\n    vs_ours: >\\n      早期数据集污染实证研究，在视觉领域验证了 collapse 前兆。\\n      他们关注下游任务性能，我们关注训练中的实时信号。\\n\\n  # ===================== COMPLEMENTARY (Theory/Mitigation) =====================\\n\\n  - id: shumailov_nature2024\\n    title: \\\"AI Models Collapse When Trained on Recursively Generated Data\\\"\\n    authors: [Ilia Shumailov et al.]\\n    year: 2024\\n    venue: Nature 631, 755-759\\n    relation: foundation\\n    core_method: >\\n      首次系统性证明迭代合成数据训练导致 model collapse。\\n      在 LLM、VAE、GMM 上验证。分布尾部消失是核心机制。\\n    signals: [test loss, distribution tail metrics]\\n    scale: model-level\\n    key_findings:\\n      - 迭代训练导致不可逆缺陷：分布尾部消失\\n      - 罕见事件最先遗忘\\n      - LLM、VAE、GMM 都有此现象\\n    vs_ours: >\\n      领域基石论文，建立了我们要解决的问题。\\n      他们用事后评估（test loss），我们提供在线监控手段。\\n\\n  - id: dohmatob_iclr2025\\n    title: \\\"Strong Model Collapse\\\"\\n    authors: [Elvis Dohmatob, Yunzhen Feng et al.]\\n    year: 2025\\n    venue: ICLR 2025 (Spotlight)\\n    relation: complementary\\n    core_method: >\\n      用算子值自由概率论证明即使极小比例的合成数据 (1/1000)\\n      也会导致 model collapse，且更大模型放大 collapse。\\n    signals: [test error on real data, bias-variance decomposition]\\n    scale: model-level\\n    key_findings:\\n      - 任何非零常数比例的合成数据都导致 collapse\\n      - 更大模型可放大 collapse\\n      - 神经缩放定律在合成数据下失效\\n    vs_ours: >\\n      理论基础——解释了为什么需要监控（即使少量合成数据也危险）。\\n      他们的 fraction 实验与我们的实验设计直接相关。\\n\\n  - id: gerstgrasser_2024\\n    title: \\\"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\\\"\\n    authors: [Matthias Gerstgrasser, Rylan Schaeffer et al.]\\n    year: 2024\\n    venue: arXiv (2404.01413)\\n    relation: complementary\\n    core_method: >\\n      证明数据累积（而非替换）可避免 model collapse。\\n      替换导致 test error 增长，累积则有有限上界。\\n    signals: [test error over iterations]\\n    scale: model-level\\n    key_findings:\\n      - 累积真实+合成数据则无 collapse（所有模型/模态）\\n      - 替换数据则 collapse\\n      - 关键因素是数据管理策略\\n    vs_ours: >\\n      互补——他们研究何时 collapse（数据管理策略），\\n      我们研究如何实时检测 collapse（训练动态信号）。\\n\\n  - id: kazdan_2024\\n    title: \\\"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World\\\"\\n    authors: [Joshua Kazdan et al.]\\n    year: 2024\\n    venue: arXiv (2410.16713)\\n    relation: complementary\\n    core_method: >\\n      系统比较三种训练工作流：replace（collapse）、\\n      accumulate（稳定）、fixed compute（介于两者之间）。\\n    signals: [test loss on real data]\\n    scale: model-level\\n    key_findings:\\n      - Replace 工作流一定 collapse\\n      - Accumulate 工作流保持稳定\\n      - Fixed compute 工作流 loss 升高但 plateau\\n    vs_ours: 互补——提供实验设计参考（不同工作流下 collapse 行为差异）。\\n\\n  - id: seddik_2024\\n    title: \\\"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\\\"\\n    authors: [Mohamed El Amine Seddik et al.]\\n    year: 2024\\n    venue: arXiv (2404.05090)\\n    relation: complementary\\n    core_method: >\\n      统计模型严格刻画不同递归训练场景下的 collapse 程度。\\n      给出混合真实/合成数据时避免 collapse 的最大合成数据比例估计。\\n    signals: [distribution tail, statistical divergence]\\n    scale: model-level\\n    key_findings:\\n      - 纯合成数据训练无法避免 collapse\\n      - 混合训练下存在可计算的合成数据上限\\n      - 分布尾部消失是 collapse 的统计特征\\n    vs_ours: 理论互补——给出合成数据比例的安全阈值。\\n\\n  - id: schaeffer_2025\\n    title: \\\"Position: Model Collapse Does Not Mean What You Think\\\"\\n    authors: [Rylan Schaeffer, Joshua Kazdan, Alvan Caleb Arulandu, Sanmi Koyejo]\\n    year: 2025\\n    venue: arXiv (2503.03150)\\n    relation: complementary\\n    core_method: >\\n      梳理 model collapse 文献中 8 种不同定义，\\n      分为三个家族：test loss 行为、分布形变、缩放行为。\\n    signals: N/A (position paper)\\n    scale: N/A\\n    key_findings:\\n      - Model collapse 有 8 种不完全一致的定义\\n      - 三个家族：test loss 行为、分布形变、缩放定律\\n      - 术语混乱阻碍了系统性理解\\n    vs_ours: >\\n      重要定位参考——论文中需明确使用哪种 collapse 定义。\\n      建议采用他们的分类框架。\\n\\n  - id: feng_iclr2025\\n    title: \\\"Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification\\\"\\n    authors: [Feng et al.]\\n    year: 2025\\n    venue: ICLR 2025\\n    relation: complementary\\n    core_method: >\\n      用高斯混合+线性分类器+线性验证器推导验证器有效的条件。\\n      证明不完美验证器也可有效筛选合成数据。\\n    signals: [verifier-based quality score]\\n    scale: model-level\\n    key_findings:\\n      - 验证器筛选合成数据可达到最优性能\\n      - 即使不完美验证器也有效\\n      - 给出可衡量的代理条件\\n    vs_ours: 互补——缓解策略。我们的监控信号可作为验证器的补充。\\n\\n  - id: yi_2025\\n    title: \\\"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence\\\"\\n    authors: [Bingji Yi, Qiyuan Liu, Yuwei Cheng, Haifeng Xu]\\n    year: 2025\\n    venue: arXiv (2510.16657)\\n    relation: complementary\\n    core_method: >\\n      证明外部验证器（人类或更强模型）可阻止 collapse。\\n      分析验证器引导下的短期改进和长期收敛行为。\\n    signals: [verifier quality score]\\n    scale: model-level\\n    key_findings:\\n      - 外部验证器注入信息则不会 collapse\\n      - 短期有改进，长期收敛到验证器的知识中心\\n    vs_ours: 互补——缓解策略方向，与监控方向正交。\\n\\n  - id: bakshi_2026\\n    title: \\\"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources\\\"\\n    authors: [Soham Bakshi et al.]\\n    year: 2026\\n    venue: arXiv (2602.10531)\\n    relation: complementary\\n    core_method: >\\n      分析在真实+合成混合数据上的迭代训练动态。\\n      next-token prediction 模型下的长期演化分析。\\n    signals: [mixture weight, sample size, test performance]\\n    scale: model-level\\n    key_findings:\\n      - 非零真实数据混合权重（即使递减）可避免 collapse\\n      - 混合权重和样本量共同控制长期性能\\n    vs_ours: 理论互补——刻画迭代训练的长期演化。\\n\\n  - id: briesch_2023\\n    title: \\\"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop\\\"\\n    authors: [Martin Briesch, Dominik Sobania, Franz Rothlauf]\\n    year: 2023\\n    venue: arXiv (2311.16822)\\n    relation: complementary\\n    core_method: >\\n      首次针对 LLM 研究 self-consuming training loop，\\n      用逻辑表达式构造可验证的生成内容，分析不同合成数据比例下输出多样性下降。\\n    signals: [output diversity, correctness rate]\\n    scale: model-level\\n    key_findings:\\n      - Self-consuming loop 产生正确输出，但多样性随合成数据比例下降\\n      - 首批 LLM self-consuming loop 实证研究之一\\n      - 提出基于逻辑表达式的内容验证方法\\n    vs_ours: >\\n      早期 LLM self-consuming loop 实证研究。\\n      他们用输出级多样性指标，我们用训练动态内部信号；互为补充。\\n\\n  - id: dohmatob_icml2024\\n    title: \\\"A Tale of Tails: Model Collapse as a Change of Scaling Laws\\\"\\n    authors: [Elvis Dohmatob, Yunzhen Feng, Pu Yang, Francois Charton, Julia Kempe]\\n    year: 2024\\n    venue: ICML 2024 (pp. 11165-11197)\\n    relation: complementary\\n    core_method: >\\n      从 scaling law 视角分析 collapse——理论框架揭示 collapse 导致 scaling law 改变。\\n    signals: [test loss scaling, skill metrics]\\n    scale: model-level\\n    key_findings:\\n      - Loss of scaling、shifted scaling with number of generations\\n      - Skill un-learning 现象\\n      - 混合人类/合成数据时的 grokking 效应\\n    vs_ours: >\\n      理论背景——从 scaling law 角度量化 collapse 严重度。\\n      我们用训练动态信号在训练中追踪，他们用事后 scaling 分析。\\n\\n  - id: fu_icml2024\\n    title: \\\"Towards Theoretical Understandings of Self-Consuming Generative Models\\\"\\n    authors: [Shi Fu, Sen Zhang, Yingjie Wang, Xinmei Tian, Dacheng Tao]\\n    year: 2024\\n    venue: ICML 2024\\n    relation: complementary\\n    core_method: >\\n      构建严格理论框架分析 self-consuming loop 中数据分布演化。\\n      分析参数和非参数模型中三种误差源的复合效应。\\n    signals: [distribution divergence, error accumulation]\\n    scale: model-level\\n    key_findings:\\n      - 统计/表达/近似三种误差在迭代中复合\\n      - 给出误差增长的理论界\\n    vs_ours: 理论互补——严格刻画 collapse 的误差复合机制。\\n\\n  - id: gillman_icml2024\\n    title: \\\"Self-Correcting Self-Consuming Loops for Generative Model Training\\\"\\n    authors: [Nate Gillman, Michael Freeman, Daksh Aggarwal, Chia-Hong Hsu, Calvin Luo, Yonglong Tian, Chen Sun]\\n    year: 2024\\n    venue: ICML 2024\\n    relation: complementary\\n    core_method: >\\n      引入 correction function 使 self-consuming loop 指数级更稳定。\\n      在人体运动合成任务上验证。\\n    signals: [corrector quality, loop stability]\\n    scale: model-level\\n    key_findings:\\n      - Correction function 使 loop 指数级稳定\\n      - 即使 synthetic:real = 100:1 也可避免 collapse\\n    vs_ours: 互补——缓解策略，correction function 概念与在线监控互补。\\n\\n  - id: pennington_nips2017\\n    title: \\\"Nonlinear Random Matrix Theory for Deep Learning\\\"\\n    authors: [Jeffrey Pennington, Pratik Worah]\\n    year: 2017\\n    venue: NeurIPS 2017\\n    relation: foundation\\n    core_method: >\\n      将神经网络中的逐点非线性纳入随机矩阵理论的矩方法框架，\\n      推导数据协方差矩阵在网络层间传播的渐近谱分布。\\n    signals: [eigenvalue distribution, spectral density]\\n    scale: layer-level (weight/covariance matrices)\\n    key_findings:\\n      - 非线性激活函数可纳入 RMT 矩方法\\n      - 推导单层随机特征方法在记忆任务上的渐近性能\\n      - 分析数据协方差矩阵在网络中传播时的特征值演化\\n    vs_ours: >\\n      RMT 在深度学习中的理论基础。我们的谱分析方法论（spectral entropy、\\n      stable rank）建立在此类随机矩阵理论之上。\\n\\n  # ===================== DATA CONTAMINATION DETECTION =====================\\n\\n  - id: kirchenbauer_icml2023\\n    title: \\\"A Watermark for Large Language Models\\\"\\n    authors: [John Kirchenbauer, Jonas Geiping, Yuxin Wen, Jonathan Katz, Ian Miers, Tom Goldstein]\\n    year: 2023\\n    venue: ICML 2023 (pp. 17061-17084)\\n    relation: complementary\\n    core_method: >\\n      LLM 文本水印框架——green/red token list + soft promotion + 统计检测。\\n    signals: [green token ratio, z-score]\\n    scale: token-level (output)\\n    key_findings:\\n      - 可嵌入统计可检测水印且不影响文本质量\\n      - 开源检测算法不需模型访问\\n    vs_ours: 合成数据溯源的基础方法，与 collapse 检测互补。\\n\\n  - id: dathathri_nature2024\\n    title: \\\"Scalable Watermarking for Identifying Large Language Model Outputs\\\"\\n    authors: [Sumanth Dathathri, Abigail See, Sumedh Ghaisas et al.]\\n    year: 2024\\n    venue: Nature 634, 818-823\\n    relation: complementary\\n    core_method: >\\n      SynthID-Text：产品级文本水印，与 speculative sampling 集成。\\n      在 Gemini ~20M 响应上验证。\\n    signals: [watermark detection score]\\n    scale: token-level (output)\\n    key_findings:\\n      - 产品级规模的水印部署\\n      - 不影响文本质量，最小延迟开销\\n    vs_ours: 大规模合成数据标记的工业实践，与监控方向互补。\\n\\n  - id: sander_neurips2024\\n    title: \\\"Watermarking Makes Language Models Radioactive\\\"\\n    authors: [Tom Sander, Pierre Fernandez, Alain Durmus, Matthijs Douze, Teddy Furon]\\n    year: 2024\\n    venue: NeurIPS 2024\\n    relation: related\\n    core_method: >\\n      证明在水印 LLM 输出上微调的模型保留水印残留（\\\"放射性\\\"）。\\n    signals: [watermark residual in fine-tuned model]\\n    scale: model-level\\n    key_findings:\\n      - 水印信号通过训练传播到下游模型\\n      - 可检测模型是否在合成数据上训练\\n    vs_ours: >\\n      直接相关——检测合成数据训练的替代方法。\\n      他们检测\\\"是否用了合成数据\\\"，我们监控\\\"合成数据造成多严重的 collapse\\\"。\\n\\n  - id: mitchell_icml2023\\n    title: \\\"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\\\"\\n    authors: [Eric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher D. Manning, Chelsea Finn]\\n    year: 2023\\n    venue: ICML 2023 (pp. 24950-24962)\\n    relation: complementary\\n    core_method: >\\n      LLM 生成文本占据 log-probability 负曲率区域，据此零样本检测。\\n    signals: [log probability curvature]\\n    scale: text-level\\n    key_findings:\\n      - 生成文本的概率曲率特征可区分人类/机器文本\\n      - 0.95 AUROC 检测 GPT-NeoX 20B 生成的假新闻\\n    vs_ours: 合成文本检测方法，可识别训练数据中的合成成分。\\n\\n  - id: shi_iclr2024\\n    title: \\\"Detecting Pretraining Data from Large Language Models\\\"\\n    authors: [Weijia Shi, Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra Blevins, Danqi Chen, Luke Zettlemoyer]\\n    year: 2024\\n    venue: ICLR 2024\\n    relation: related\\n    core_method: >\\n      Min-K% Prob：未见样本含低概率 outlier word，据此检测预训练数据成员。\\n    signals: [Min-K% probability score]\\n    scale: text-level\\n    key_findings:\\n      - 比 reference model 方法提升 7.4%\\n      - 适用于版权检测、污染检测、隐私审计\\n    vs_ours: 数据污染检测工具——可检测合成数据是否混入训练集，与 collapse 监控互补。\\n\\n  # ===================== METHODOLOGICAL FOUNDATIONS =====================\\n\\n  - id: martin_mahoney_2021\\n    title: \\\"Predicting Trends in the Quality of State-of-the-Art Neural Networks without Access to Training or Testing Data\\\"\\n    authors: [Charles H. Martin, Michael W. Mahoney]\\n    year: 2021\\n    venue: Nature Communications 12\\n    relation: complementary\\n    core_method: >\\n      WeightWatcher 工具——用 RMT 分析权重矩阵的谱性质，\\n      无需训练/测试数据即可预测模型质量。\\n    signals: [stable rank, power law exponent (alpha), spectral norm]\\n    scale: layer-level (per weight matrix)\\n    key_findings:\\n      - stable rank 追踪自正则化程度\\n      - 5+1 训练阶段对应不同的谱形态\\n      - heavy-tailed 分布特征区分好/差模型\\n    vs_ours: >\\n      方法论基础——WeightWatcher 的 stable rank 和谱分析方法\\n      直接启发我们的信号设计。\\n\\n  - id: yunis_2024\\n    title: \\\"Approaching Deep Learning through the Spectral Dynamics of Weights\\\"\\n    authors: [David Yunis, Kumar Kshitij Patel et al.]\\n    year: 2024\\n    venue: arXiv (2408.11804)\\n    relation: complementary\\n    core_method: >\\n      以权重奇异值/向量的动态演化为核心视角理解深度学习。\\n      证明谱动态可区分记忆网络和泛化网络。\\n    signals: [singular value dynamics, singular vector alignment]\\n    scale: layer-level (per weight matrix)\\n    key_findings:\\n      - 权重衰减增强低秩偏置\\n      - 谱动态区分记忆 vs 泛化\\n      - 与 lottery ticket 和 loss surface 结构相关\\n    vs_ours: 方法论基础——谱动态视角可用于理解 collapse 过程中的权重变化。\\n\\n  - id: chen_liu_2024\\n    title: \\\"Assessing Neural Network Representations During Training Using Noise-Resilient Diffusion Spectral Entropy\\\"\\n    authors: [Chen Liu et al.]\\n    year: 2024\\n    venue: IEEE CISS 2024\\n    relation: complementary\\n    core_method: >\\n      提出 Diffusion Spectral Entropy (DSE) 和 Diffusion Spectral Mutual Information (DSMI)，\\n      利用数据几何在高维中可靠计算信息论指标。\\n    signals: [DSE, DSMI]\\n    scale: layer-level (representations)\\n    key_findings:\\n      - DSE 在训练中增加\\n      - DSMI(class label) 在泛化学习中增加，过拟合时停滞\\n      - 可用于指导网络初始化和预测下游准确率\\n    vs_ours: >\\n      方法论工具——DSE 是我们 spectral entropy 信号的潜在替代实现。\\n\\n  - id: lu_neurips2024\\n    title: \\\"AlphaPruning: Using Heavy-Tailed Self Regularization Theory for Improved Layer-wise Pruning of Large Language Models\\\"\\n    authors: [Haiquan Lu, Yefan Zhou, Shiwei Liu, Zhangyang Wang, Michael W. Mahoney, Yaoqing Yang]\\n    year: 2024\\n    venue: NeurIPS 2024\\n    relation: complementary\\n    core_method: >\\n      用 HT-SR 理论的谱密度形态（alpha exponent）指导 LLM 层级剪枝。\\n    signals: [alpha exponent, ESD shape metrics]\\n    scale: layer-level\\n    key_findings:\\n      - Alpha exponent 有效指导 per-layer 剪枝比例\\n      - LLaMA-7B 可剪至 80% sparsity 保持合理 perplexity\\n    vs_ours: >\\n      验证 per-layer 谱分析对 LLM 质量评估的有效性。\\n      支持我们用类似方法监控 collapse。\\n\\n  - id: sanyal_iclr2020\\n    title: \\\"Stable Rank Normalization for Improved Generalization in Neural Networks and GANs\\\"\\n    authors: [Amartya Sanyal, Philip H. S. Torr, Puneet K. Dokania]\\n    year: 2020\\n    venue: ICLR 2020\\n    relation: complementary\\n    core_method: >\\n      提出 stable rank normalization——最小化线性算子的 stable rank。\\n      理论证明唯一最优解，实验验证改善泛化。\\n    signals: [stable rank, Lipschitz constant]\\n    scale: layer-level\\n    key_findings:\\n      - 控制 stable rank 改善泛化 gap 11.3%\\n      - Stable rank 与泛化能力直接关联\\n    vs_ours: >\\n      理论支持——建立 stable rank 与泛化的直接联系。\\n      支持我们选用 stable rank 作为 collapse（泛化退化）的监控信号。\\n\\n  - id: kalra_2026\\n    title: \\\"A Scalable Measure of Loss Landscape Curvature for Analyzing the Training Dynamics of LLMs\\\"\\n    authors: [Dayal Singh Kalra, Jean-Christophe Gagnon-Audet, Andrey Gromov, Ishita Mediratta, Kelvin Niu, Alexander H. Miller, Michael Shvartsman]\\n    year: 2026\\n    venue: arXiv (2601.16979)\\n    relation: related\\n    core_method: >\\n      Critical sharpness：<10 forward passes 高效度量 loss landscape 曲率。\\n      首次在 7B 规模验证 progressive sharpening 和 Edge of Stability。\\n    signals: [critical sharpness, relative critical sharpness]\\n    scale: model-level\\n    key_findings:\\n      - Progressive sharpening 在 7B 规模仍然存在\\n      - Critical sharpness 可指导 pre-train 到 fine-tune 的数据混合\\n    vs_ours: >\\n      训练动态监控方法论参考——高效的大规模 LLM 训练动态度量。\\n      Critical sharpness 可作为我们信号集的潜在补充。\\n\\n  # ===================== DATA QUALITY =====================\\n\\n  - id: penedo_2024\\n    title: \\\"The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale\\\"\\n    authors: [Guilherme Penedo, Hynek Kydlicek, Loubna Ben allal, Anton Lozhkov, Margaret Mitchell, Colin Raffel, Leandro Von Werra, Thomas Wolf]\\n    year: 2024\\n    venue: arXiv (2406.17557)\\n    relation: complementary\\n    core_method: >\\n      15T token 数据集的完整策略文档——去重、过滤、教育文本提取。\\n    signals: [data quality classifiers, deduplication metrics]\\n    scale: dataset-level\\n    key_findings:\\n      - 详细 ablation 各种去重和过滤策略\\n      - FineWeb-Edu 在知识密集任务上大幅提升性能\\n    vs_ours: 数据质量策略参考——理解高质量训练数据标准，为分析 collapse 的数据原因提供基线。\\n\\n  - id: zhang_2026\\n    title: \\\"The LLM Data Auditor: A Metric-oriented Survey on Quality and Trustworthiness in Evaluating Synthetic Data\\\"\\n    authors: [Kaituo Zhang, Mingzhi Hu, Hoang Anh Duy Le et al.]\\n    year: 2026\\n    venue: arXiv (2601.17717)\\n    relation: complementary\\n    core_method: >\\n      系统分类合成数据评估指标——quality (validity/fidelity/utility) +\\n      trustworthiness (safety/faithfulness)。\\n    signals: [quality metrics taxonomy, trustworthiness metrics]\\n    scale: dataset-level\\n    key_findings:\\n      - 从内在属性评估合成数据，而非仅看下游性能\\n      - 质量和可信度两个维度的完整分类体系\\n    vs_ours: 合成数据质量评估框架——为理解 collapse 的数据级原因提供指标体系。\\n\\n# ============================================================\\n# 关键发现总结\\n# ============================================================\\n\\nsummary:\\n  total_papers: 37\\n  direct_competitors: 2  # SIGMA, Kalinowski\\n  novelty_confirmation: >\\n    在 34 篇文献中，没有工作同时做到：(a) 训练中在线监控 (b) 用频谱/熵训练动态信号\\n    (c) per-layer 粒度 (d) 在迭代合成数据训练场景下验证。\\n    我们的核心新颖性空间依然存在。\\n\\n  coverage:\\n    model_collapse_theory: 16  # shumailov, dohmatob x2, alemohammad, fu, gerstgrasser, seddik, kazdan, schaeffer, bakshi, shi_neurips2025, feng, yi, gillman, briesch, hataya\\n    data_contamination: 5  # kirchenbauer, dathathri, sander, mitchell, shi_iclr2024\\n    spectral_methods: 9  # sigma, martin_mahoney, yunis, lu, sanyal, spectral_lens, xu, conzelmann, pennington\\n    training_dynamics: 4  # kalinowski, chen_liu, kalra, papyan\\n    data_quality: 3  # wyss, penedo, zhang\\n\\n  gap_analysis:\\n    sigma: >\\n      用输出嵌入 Gram 矩阵谱——事后/黑盒，不做 per-layer，不跟踪训练过程。\\n    kalinowski: >\\n      用拓扑信号——在线但信号族不同，不研究迭代合成数据场景。\\n    our_unique_position: >\\n      训练动态频谱/熵信号 + per-layer 粒度 + 迭代合成数据场景 = 独特定位。\\n\\n  per_layer_collapse_analysis:\\n    papers_with_per_layer:\\n      - layer_collapse_diffusion_2026  # diffusion LM per-layer activation collapse\\n      - xu_2026  # stable rank per-layer（compression 场景）\\n      - spectral_lens_2026  # per-layer activation/gradient 谱\\n      - lu_neurips2024  # alpha exponent per-layer for pruning\\n    gap: \\\"无论文在迭代合成数据训练中做 per-layer collapse 分析\\\"\\n\\n  stable_rank_as_collapse_signal:\\n    papers_using_stable_rank:\\n      - martin_mahoney_2021  # WeightWatcher 中作为模型质量指标\\n      - xu_2026  # 压缩退化预测器 (r=0.89)\\n      - yunis_2024  # 谱动态中的低秩偏置\\n      - sanyal_iclr2020  # stable rank 与泛化的直接联系\\n    gap: \\\"无论文直接用 stable rank 监控 iterative synthetic data collapse\\\"\\n\\n  spectral_entropy_as_collapse_signal:\\n    papers_using_spectral_entropy:\\n      - chen_liu_2024  # DSE 跟踪训练动态\\n      - sigma_2026  # 谱分析但在 Gram 矩阵上\\n    gap: \\\"无论文直接用 weight spectral entropy 监控 collapse\\\"\\n\\n  synthetic_fraction_effects:\\n    papers_studying_fraction:\\n      - dohmatob_iclr2025  # 理论：任何非零 fraction 都危险\\n      - dohmatob_icml2024  # scaling law 角度的 fraction 分析\\n      - alemohammad_iclr2024  # 三种 loop 类型的不同效果\\n      - wyss_2024  # 实证：25%/50%/75% 不同 collapse 程度\\n      - seddik_2024  # 统计：给出安全上限估计\\n    gap: \\\"大量理论/实证工作，但都用事后指标衡量 fraction 效果\\\"\\n\\n  data_contamination_detection:\\n    papers:\\n      - kirchenbauer_icml2023  # 基础水印方法\\n      - dathathri_nature2024  # 产品级水印 (SynthID)\\n      - sander_neurips2024  # 水印放射性传播\\n      - mitchell_icml2023  # DetectGPT 概率曲率检测\\n      - shi_iclr2024  # Min-K% 预训练数据检测\\n    relevance: >\\n      合成数据检测与 collapse 监控互补：他们回答\\\"是否有合成数据\\\"，\\n      我们回答\\\"合成数据造成了多严重的 collapse\\\"。\\n\", \"total_chars\": 26925, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c07f244-cea3-4084-bbae-c2c80fc49574",
  "isSidechain": true,
  "promptId": "80dd2a4d-c31a-43ae-8316-4a6135d9fed6",
  "agentId": "ade4d670d78b2afaf",
  "type": "user",
  "uuid": "415de543-4682-444c-9419-76f1404d7076",
  "sourceToolAssistantUUID": "1c07f244-cea3-4084-bbae-c2c80fc49574",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-16T10:42:46.263Z_

Now let me read the paper itself and the experimental artifacts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "415de543-4682-444c-9419-76f1404d7076",
  "isSidechain": true,
  "agentId": "ade4d670d78b2afaf",
  "requestId": "req_011Cb67GRntJdS1h3HKjPsGH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7a2588b8-9075-4f0c-8990-e4cbc1ef6650",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012kqUWH6P5XM7Zm4FHmUHTS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16993,
      "cache_read_input_tokens": 16774,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16993,
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

_source line 13 · 2026-05-16T10:42:47.271Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Dma1zqVnC4LuTGrfiXxU13`</summary>

```json
{
  "project": "collapse_severity_monitor",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a2588b8-9075-4f0c-8990-e4cbc1ef6650",
  "isSidechain": true,
  "agentId": "ade4d670d78b2afaf",
  "requestId": "req_011Cb67GRntJdS1h3HKjPsGH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ba55df25-a2d4-47a3-a8db-2b15ea78f95f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012kqUWH6P5XM7Zm4FHmUHTS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16993,
      "cache_read_input_tokens": 16774,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16993,
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

_source line 14 · 2026-05-16T10:42:47.286Z_

<details><summary>↩ Tool result · `toolu_01Dma1zqVnC4LuTGrfiXxU13`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper_framing.md\", \"content\": \"# Paper Framing — collapse_severity_monitor\\n\\n## Target Venue\\n- Primary: EMNLP 2026 via ACL Rolling Review (ARR)\\n- Deadline: ARR submission 2026-05-25\\n- Backup: ARR June cycle (2026-06-15) if 5/25 not feasible\\n\\n## Core Claims (3 条)\\n\\n1. **Signal-Severity Correlation**: Spectral signals (stable rank, spectral entropy) and output signals (token entropy, perplexity) reliably track model collapse severity across synthetic data contamination levels, maintaining monotonic ordering across tested fractions and generations. (MVP: ρ=1.0 with n=3; to be validated with n=6 fractions × 5 seeds in plan_001. Primary evidence: Spearman ρ with bootstrap CIs; effect sizes elevated as primary evidence, ρ as supporting.)\\n\\n2. **Early Warning Capability**: Collapse can be detected at moderate contamination (50%) within a single training run: stable rank achieves AUC=0.984 [0.978, 0.989] for within-gen collapse detection, reaching AUC=0.94 (sens=0.78, spec=1.00) at just 10% training progress. Training loss is the second-best within-gen detector (AUC=0.923). ROC analysis must use clustered bootstrap (one observation per fraction×seed) to avoid inflating AUC from serial generation dependence. **Featured sub-result: held-out evaluation perplexity — the metric practitioners most commonly check at eval checkpoints — provides no within-generation early warning (AUC=0.534 ≈ random).** This is because held-out PPL requires multi-generation accumulation before collapse manifests; in contrast, train-set loss (AUC=0.923) detects earlier because it directly measures learning dynamics on the contaminated distribution. Claim 2 Results 段落结构：(a) stable_rank early detection 正面证据, (b) 专门 1 段讨论 PPL within-gen 失效 + 原理解释 + AUC 对比, (c) ROC curves 图。Abstract 加半句：\\\"notably, held-out evaluation perplexity — the metric practitioners most commonly check — provides no within-generation early warning (AUC=0.53)\\\"。(Note: stable_rank is seed-sensitive but early-detecting; spectral_entropy is seed-robust but late-detecting (only at 100%). Practitioner recommendation: use stable_rank for within-gen early warning, perplexity for cross-gen severity comparison, spectral_entropy for severity discrimination. Cross-validation needed: plan001 5-seed + plan002 PubMed within-gen ROC, 如果多配置 PPL AUC 一致 ~0.5，camera-ready 可升级措辞。See writing notes 17, 18, 19.)\\n\\n3. **Non-Uniform Signal Behavior**: The same monitoring signal can be informative under one training method and misleading under another. Spectral signals saturate at extreme severity; gradient norm is non-monotonic under QLoRA but monotonic under Full FT; downstream metrics (HellaSwag) track collapse under Full FT but remain stable under QLoRA. Both methods show large gen1 PPL jumps (Full FT 15.3x, QLoRA 8.7x) but diverge in subsequent evolution: Full FT saturates (gen1→4: 1.11x), QLoRA decelerates but continues (gen1→4: 6.13x). Featured sub-result: PPL-downstream dissociation — QLoRA PPL=839 but hellaswag=0.430 vs Full FT PPL=326 but hellaswag=0.372, meaning PPL-based monitoring overestimates damage under QLoRA and practitioners must consider training method when selecting collapse signals. Terminal spectral convergence (SR ~154-156) noted as observation, not claimed as finding (N=1). Signal taxonomy table should include \\\"method-dependence\\\" column.\\n\\n## Story Spine\\n\\n- **Problem**: Model collapse from iterative training on synthetic data is a growing concern as LLM-generated text pervades training corpora. While the phenomenon is well-characterized theoretically (Shumailov et al. 2024, Alemohammad et al. 2024, Dohmatob et al. 2024), practitioners lack actionable tools to detect and quantify collapse severity during training. Current work focuses on post-hoc analysis or output-level detection, missing the rich signal available in training dynamics.\\n\\n- **Existing approaches & gaps**: SIGMA (2025) monitors output embedding spectral properties but requires access to a clean reference distribution (plan_009 adds head-to-head to clarify operational vs fundamental advantage). Kalinowski (2024) uses topological analysis but is computationally expensive. Data mixing strategies (Gerstgrasser et al. 2024, Kazdan et al. 2024) study prevention rather than detection. Neither provides a systematic comparison of which training-time signals best track collapse across severity levels, nor do they examine within-generation temporal dynamics for early warning.\\n\\n- **Our framing**: We conduct a systematic empirical analysis of training dynamic signals as collapse severity monitors. Across 4 signal families (spectral, output, gradient, downstream) × 6 contamination levels × 2 model scales × 2 domains × 2 fine-tuning methods, we characterize which signals track collapse, when they diverge, and where they fail. Key insight: stable rank provides the earliest within-gen warning (AUC=0.94 at 10% training progress) while perplexity provides the most reliable cross-generation severity tracking — but these roles are non-interchangeable. We document a partial self-recovery phenomenon at moderate contamination consistent with known data mixing effects (Gerstgrasser et al. 2024), and characterize where standard monitoring signals mislead practitioners.\\n\\n- **Headline result template**: \\\"Stable rank detects within-generation collapse with AUC=0.984, reaching actionable sensitivity (AUC=0.94) at 10% training progress. Across generations, spectral entropy provides the most robust severity discrimination (CV=0.0015) but is a late detector (only at 100% contamination). Held-out evaluation perplexity — often the go-to metric at eval checkpoints — is nearly ineffective for within-generation detection (AUC=0.534), while train-set loss detects data distribution shift (AUC=0.923) but not model quality degradation; evaluation perplexity remains the strongest cross-generation severity tracker. Different signals have complementary operating ranges; no single signal suffices across all detection contexts.\\\" (Note: ρ ≥ 0.94 是 plan001 验证目标，非当前实际数值，到手前用 effect size 表述。分层信号策略替代单一 headline signal。ROC 数据来自 plan005 within-gen 分析，N=1 seed。)\\n\\n## Anticipated Reviewer Concerns & Mitigation\\n\\n| Concern | Severity | Mitigation |\\n|---------|----------|------------|\\n| Statistical power (seeds) | CRITICAL | 5 seeds WikiText, 3 seeds PubMed; bootstrap CIs for all claims |\\n| n=3 fractions → trivial ρ=1.0 | HIGH | 6 fractions (0/10/25/50/75/100%) |\\n| Single model scale | HIGH | 0.5B + 1.5B (+ 3B spot-check if GPU permits) |\\n| Single dataset | HIGH | WikiText-2 + PubMed (3 seeds each) |\\n| QLoRA only | MEDIUM | Full FT comparison on 1 config (plan_003) |\\n| ROC pools non-independent observations | HIGH | Clustered bootstrap or one-gen-per-run restriction (plan_005) |\\n| Stable rank direction under collapse | MEDIUM | Clarify: ‖W‖_F² grows faster than σ₁² → SR increases = energy dispersal, not concentration. Fix text |\\n| No theoretical grounding | MEDIUM | Informal argument: 75% phase transition ↔ distributional shift theory; when spectral monitoring fails (capacity redundancy) |\\n| \\\"First\\\" claims overclaimed | MEDIUM | Qualify: \\\"first systematic multi-axis comparison in iterative fine-tuning setting.\\\" Self-recovery → cite Gerstgrasser et al. |\\n| SIGMA differentiation thin | MEDIUM | Head-to-head (plan_009): run SIGMA at training checkpoints |\\n| Related work too thin | HIGH | ≥20 refs: Briesch 2023, Hataya 2023, Gerstgrasser 2024, Seddik 2024, Dohmatob \\\"Tale of Tails\\\" 2024, Pennington & Worah 2017 |\\n| Missing synthetic data gen params | LOW | Document temperature, top-p/k, max length, prompt format in Methods |\\n| No code/data release | MEDIUM | Release monitoring toolkit + signal trajectories + generation scripts |\\n| \\\"Not a monitoring system\\\" | LOW | Frame as analysis paper; taxonomy + early warning = practical value |\\n| No intervention/mitigation | LOW | Explicit non-goal; future work |\\n\\n## Core Insight (一句话)\\n\\nTraining dynamic signals provide a free, model-agnostic early warning system for model collapse — but different signal families have distinct operating ranges, and practitioners need to know which signal to trust at which severity level.\\n\\n## Novelty Statement\\n\\nWe provide the first systematic multi-axis comparison of training-time signal families as collapse severity monitors, spanning contamination levels, model scales, text domains, and fine-tuning methods. The within-generation early warning capability (stable rank AUC=0.94 at 10% training progress), the signal operating-range taxonomy, and the documentation of where standard monitoring signals actively mislead practitioners are the primary empirical contributions. The self-recovery observation at moderate contamination is consistent with known data mixing effects and is positioned as a finding rather than a novel phenomenon.\\n\\n## Key Writing Notes (from Dream review, 2026-05-14)\\n\\n1. **Effect sizes > ρ**: Elevate effect size tables as primary evidence; ρ as supporting.\\n2. **Stable rank direction**: SR increases under collapse = energy dispersal (Frobenius norm grows faster than spectral norm), not concentration. Fix text.\\n3. **25% contamination**: \\\"mild degradation / near-stability\\\", NOT \\\"strong recovery\\\" (PPL monotonically increases).\\n4. **Figures required**: Severity curves, ROC curves, heatmaps, per-layer propagation. Analysis paper without figures is a major gap.\\n5. **Reproducibility**: Code release, signal trajectories, generation scripts for D&B track.\\n6. **Collapse protocol**: Explicitly state whether fine-tuning from M₀ or M_{g-1} and discuss implications.\\n7. **Per-layer 叙事修正 (D011, 2026-05-15)**: 废弃\\\"三区结构\\\"（boundary/middle-neutral/late-bifurcation），改为 sub-module-centric 分析。真实数据显示 v_proj 在几乎所有层 diffuse（ΔSR +1~+3），down_proj 在 L11-L12 局部 collapse，其余子模块温和。Practitioner takeaway: 优先监控 v_proj stable rank 作为最敏感的 within-run collapse indicator。（注：cross-seed 稳定性另论，参见写作笔记 16。within-run 灵敏度与 cross-seed 排名是不同维度。）\\n8. **SIGMA 方向 provisional (C001/D014, 2026-05-15)**: expected_direction=+1（effective_rank 在 collapse 时上升）是 N=2 观测，非已验证结论。禁止在论文中当发现写。验证条件：plan_001 seed43-46 全量数据 + plan_003 Full FT SIGMA 数据。如果 Full FT 方向一致(+1)可排除 QLoRA confound；如果不一致需重写分析。\\\"Within-gen corruption vs recursive collapse 方向差异\\\"作为 discussion 论点需要等验证后才能使用。\\n9. **Non-monotonic claim scope (plan008/plan003, 2026-05-15)**: \\\"Non-monotonic\\\" 仅适用于 frac=50% 的 plateau 行为（ppl 26.9→25.6→25.7→25.6，真正收敛）。frac=100% gen1→gen2 的 -1.9% 下降（294→288）是噪声级波动，N=1 无法区分，禁止称为 \\\"non-monotonic pattern\\\"。100% 的正确描述：\\\"catastrophic jump at gen1 followed by continued degradation\\\"。\\n10. **HellaSwag method-dependence + 归因修正 (plan003, 2026-05-15; 合并原 Note 10+13)**: HellaSwag 追踪 collapse 能力取决于训练方法（Full FT: 有效, -12.5%；QLoRA: 无效/稳定）。D015/D017 的\\\"0.5B 失效\\\"诊断错误——失效的是 QLoRA 的隐式正则化，非模型规模。论文归因必须是 method 而非 scale。反直觉：QLoRA gen4 PPL (839) > Full FT gen4 PPL (326)，但 QLoRA hellaswag (0.430) > Full FT hellaswag (0.372)——PPL 不是下游质量的唯一预测器。\\n11. **Collapse trajectory: 两种方法都 gen1 大跳，差异在后续 (plan003, 2026-05-15; D026 修正 D024)**: Full FT gen1=15.3x 后饱和（gen1→4: 1.11x）；QLoRA gen1=8.7x 后减速增长（gen1→4: 6.13x，gen4 PPL=839）。**禁止**使用 \\\"slow onset\\\" / \\\"snowball\\\" / \\\"exponential\\\" 描述 QLoRA——QLoRA gen1 也是大跳（8.7x），不是缓慢起步。正确叙事：两种方法初始冲击程度不同（Full FT 更剧烈），后续演化模式不同（饱和 vs 减速增长）。终态谱收敛（SR ~154 vs ~156）需用正确数据重新验证后方可使用。\\n12. **Diversity 指标对 collapse 不敏感 (plan003, 2026-05-15)**: distinct_1 在 Full FT frac=100% 仅 -3%（0.0925→0.0897），self_bleu 几乎不变，即使 PPL 暴涨 17x。原因：collapsed model 输出分布坍缩到少数 token（token_entropy -55%），但采样随机性维持了 lexical diversity 的表面指标。论文中需明确将 diversity 族排除在有效 collapse indicator 之外，或专门讨论 entropy vs diversity 解耦现象。\\n13. *[已合并到 Note 10]*\\n14. **Claim 3 措辞升级方向 (Reviewer 评估, 2026-05-15)**: 从 \\\"different signals respond differently\\\" 升级为 \\\"the same signal can be informative under one training method and misleading under another\\\"——直击 practitioner pain point。PPL-downstream dissociation 作为 Claim 3 featured sub-result（1 段专门讨论），不独立成 claim（N=1 seed, 1 downstream task, 无法排除 HellaSwag ceiling/floor effect）。Signal taxonomy table 加 \\\"method-dependence\\\" 列。Abstract 用一句：\\\"perplexity and downstream metrics can diverge under parameter-efficient FT, cautioning against single-signal monitoring\\\"。Terminal spectral convergence 降级为 observation（N=1 无法区分\\\"收敛\\\"和\\\"碰巧接近\\\"）。Limitations 必须标注 Full FT 对比的 N=1 限制。\\n15. **Self-recovery prevalence 对比禁令 (Reviewer, 2026-05-16)**: 3-seed 的 9/9=100% vs plan008 的 16/18=89% 不可比——前者仅用 3 个信号（PPL, stable_rank, spectral_entropy），后者用 6 个信号。选取的恰好是最一致的信号。论文中讨论 self-recovery 时必须标注信号覆盖范围，禁止跨不同信号集做 prevalence 对比。\\n16. **Signal ranking instability: stable_rank seed-sensitive (plan006/008 3-seed update, 2026-05-16)**: 3-seed 数据显示 stable_rank 的 Cohen's d 从 61.7 暴跌到 9.43（rank 1→4），原因是 seed44 引入 frac=50% 方差（CV=0.022）。spectral_entropy 最稳定（CV=0.0015，d=33.48，rank 2→1）。**禁止**在论文中将 stable_rank 定位为\\\"最敏感信号\\\"——正确叙事见写作笔记 17 分层策略。最终 taxonomy ranking 需等 plan001 5-seed 数据确认。\\n17. **分层信号策略（Signal Heatmap 发现, 2026-05-16; 修正 D029）**: spectral_entropy 虽 cross-seed 最稳定（d=33.48, CV=0.0015），但是 **late detector**——仅在 frac=100% 下显著（Δ+25.7%），frac=50% 下 effect size < 5%。stable_rank 和 perplexity 是 **early detectors**（50% 即可检出：SR +564.8%, PPL +5255%）。**禁止**推单一 headline signal。正确叙事：\\\"signals have complementary operating ranges\\\"——stable_rank + perplexity 用于 early warning（Claim 2），spectral_entropy 用于 severity discrimination（区分 50% vs 100%）。这个分层发现本身就是 Claim 3 taxonomy 的核心价值：no single signal suffices。6/7 信号方向跨 QLoRA/Full FT 一致，强化 Claim 1 泛化性。\\n18. **Within-gen ROC 证据精确化 Claim 2（plan005 ROC 分析, 2026-05-16; 修正写作笔记 17 的 perplexity 角色）**: ROC 分析揭示信号在 within-gen vs cross-gen 两个维度的能力完全不同。stable_rank 是 within-gen 最强检测器（AUC=0.984, 10% progress 即达 AUC=0.94）；training_loss 次之（AUC=0.923）；**perplexity within-gen 几乎无效（AUC=0.534）**——但 cross-gen 仍是最强 severity tracker。spectral_entropy within-gen 非单调（20% progress 时 AUC 降到 0.30，方向翻转），**不适合 threshold-based 早期检测**。这修正了写作笔记 17 将 perplexity 归入 \\\"early detectors\\\" 的表述——perplexity 是 cross-gen early detector（50% contamination 可检出），但 within-gen early detector 只有 stable_rank 和 training_loss。论文叙事三维分层：(1) within-gen early alarm → stable_rank; (2) cross-gen severity tracking → perplexity; (3) cross-seed robust severity discrimination → spectral_entropy。Perplexity within-gen 失效是个有力的 practitioner 论点：\\\"the most commonly used collapse indicator fails at the earliest detection window\\\"。**ROC 数据为 N=1 seed, 0.5B only，plan001 5-seed 后需验证。**\\n19. **信号定义精确化：三个 loss/PPL 信号的数据源（D035, 2026-05-15; 修正原 Note 19 错误归因）**: 代码中存在三个容易混淆的信号，必须在 Method 中精确定义：\\n    - **training_loss** = Trainer running avg CE on **训练集**（含 synthetic 混合数据），每 50 step 记录（`train.py:109-110`）。Within-gen AUC=0.923（有效）。原因：直接测量模型对被污染训练分布的学习动态。\\n    - **perplexity** = exp(mean NLL) on **固定 held-out 验证集**，model.eval() 模式，每 50 step 记录（`signals.py:92-108`）。Within-gen AUC=0.534（无效）。原因：QLoRA 早期微调对 held-out 分布影响微弱，collapse 效应需多代累积。Cross-gen d=20.82（有效）。\\n    - **token_entropy** = output token 分布的 Shannon entropy，within-gen AUC=0.478（无效）。\\n    **原 Note 19 的错误**：将 AUC=0.534 的信号标注为\\\"training perplexity\\\"（训练数据上的 PPL），实际该信号是 held-out eval PPL。training_loss（训练数据上的 CE）反而 AUC=0.923。\\n    **论文叙事修正**：Claim 2 featured sub-result 从\\\"training perplexity fails\\\"修正为\\\"**held-out evaluation perplexity** fails at within-gen detection (AUC=0.534), while train-set loss detects effectively (AUC=0.923)\\\"。Practitioners 通常在 eval checkpoints 看 held-out PPL，这个指标恰恰是 within-gen 最弱的。训练 loss 是间接的分布变化探测器，但 stable_rank (AUC=0.984) 仍最强因为它检测权重结构变化。\\n    **Abstract/Intro 措辞**：从 \\\"training perplexity provides no within-gen early warning\\\" 改为 \\\"held-out evaluation perplexity — the metric practitioners most commonly check — provides no within-generation early warning (AUC=0.534)\\\"。\\n    Method 必须加入 training_loss 作为正式信号（Output 家族），明确标注数据源。Fig 3 展示 training_loss 合理（within-gen 第二强），需与 Method 信号列表一致。Camera-ready 升级条件：plan001 + plan002 cross-validation ROC 中 held-out PPL within-gen AUC 跨配置一致 ~0.5。\\n\", \"total_chars\": 15691, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ba55df25-a2d4-47a3-a8db-2b15ea78f95f",
  "isSidechain": true,
  "promptId": "80dd2a4d-c31a-43ae-8316-4a6135d9fed6",
  "agentId": "ade4d670d78b2afaf",
  "type": "user",
  "uuid": "59220d01-cc10-48ca-8c17-36752163c1ab",
  "sourceToolAssistantUUID": "ba55df25-a2d4-47a3-a8db-2b15ea78f95f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T10:42:48.220Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Y2QNXyuwrse8JbSgrNmsZd`</summary>

```json
{
  "project": "collapse_severity_monitor",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59220d01-cc10-48ca-8c17-36752163c1ab",
  "isSidechain": true,
  "agentId": "ade4d670d78b2afaf",
  "requestId": "req_011Cb67GRntJdS1h3HKjPsGH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6a9320f4-6264-4ce5-8c66-babda20a9696",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012kqUWH6P5XM7Zm4FHmUHTS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16993,
      "cache_read_input_tokens": 16774,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16993,
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

_source line 16 · 2026-05-16T10:42:48.236Z_

<details><summary>↩ Tool result · `toolu_01Y2QNXyuwrse8JbSgrNmsZd`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/memory.md\", \"content\": \"# Project Memory\\n\\n## 2026-05-16: Recovery Ratio 论文措辞与代码不匹配（paper revision 时必修）\\n\\n- **问题**: experiments.tex L93-94 写 \\\"output signals recover approximately 52% of the **clean-to-collapsed gap**\\\"，暗示定义 A（50% 在 0%–100% 之间的位置）。但代码（plan008_self_recovery.py `compute_recovery_metrics()`）实际计算的是定义 B（同一 fraction 内跨 gen 的 spike-recovery）。\\n- **数字正确**: 0.5245 来自 `ppl_ratio` 真实计算，四舍五入为 52%。\\n- **修复**: 将 \\\"clean-to-collapsed gap\\\" 改为 \\\"of peak degradation\\\" 或 \\\"of the initial spike\\\"。\\n\\n## 2026-05-16: Recovery Ratio 命名歧义（低优先级，下次改代码时统一）\\n\\n- **问题**：codebase 中 \\\"recovery_ratio\\\" 被两个分析脚本用了不同定义，引发 Reviewer 误读\\n- **定义 A (temporal_recovery_ratio)**: plan008 使用。50% fraction run 内跨 generation 的信号恢复程度（spike→recovery pattern）。mean_ppl_recovery_ratio=0.51 是此定义。**数据正确。**\\n- **定义 B (fraction_position_ratio)**: `(val_50% - val_0%) / (val_100% - val_0%)`，量化 50% 在 0-100 之间的位置。结果极小（~0.2%），因为 50% contamination 几乎不引发 collapse。\\n- **行动**：下次改代码时统一命名为 `temporal_recovery_ratio` vs `fraction_position_ratio`，避免混淆。\\n\\n## 2026-05-16: Cross-domain Recovery 增量分析（seed42+43 PubMed N=2）\\n\\n- **3/4 信号确认 PubMed recovery 弱于 WikiText**（与 plan008 一致），stable_rank 例外但在噪声内（Δ=0.0008）\\n- **新发现**: 100% collapse 时 PPL WikiText 3.6x > PubMed，但 stable_rank/spectral_entropy 几乎相同 → **结构性 collapse 程度相近，PPL 差异反映 domain 特性而非 collapse 程度**\\n- **PubMed N=2 高度一致**: std 极小（PPL 0%: ±0.005, 50%: ±0.015, 100%: ±0.565）\\n- **限制**: WikiText recovery ratio 只有 N=1 (seed42)，需 seed43/44 100% 完成\\n\\n## 2026-05-16: Within-gen AUROC C2 Dry-run（seed42 preliminary）\\n\\n- training_loss AUROC=0.980 @ step 50（最强早期信号，比之前分析中的 stable_rank 更强）\\n- perplexity AUROC=0.893 @ step 50\\n- Spearman ρ @ step 50: training_loss=-0.780, perplexity=0.712, token_entropy=-0.594\\n- 待 plan001 5-seed 完成后正式运行\\n\\n## 2026-05-16: Figure 状态快照\\n\\n- 7/7 figures 有真实数据版 PDF\\n- Fig 2 已改设计：cross-generation pooled ROC → within-gen AUROC vs training progress %（对应论文 §4.2）\\n- Fig 3 per-layer: 仅 0.5B 数据，1.5B 需 plan007\\n- Fig 2 cross-scale: 原设计可改为补充材料，等 plan010 3B 完成\\n- data loader glob pattern 已修复（paper_style.py load_signals_to_df）\\n\\n## 2026-05-15: 三维信号分层图景（跨 3 项分析一致）\\n\\n- **Cross-gen severity discrimination**: spectral_entropy 最强 (Cohen's d=33.48, 但 50% 下 effect < 5% = late detector)\\n- **Within-gen early detection**: stable_rank 最强 (AUC=0.984, 10% progress 即 AUC=0.94)；spectral_entropy 非单调（20% 时 AUC 降到 0.30，方向翻转）不适合 threshold-based 早期检测\\n- **Cross-method sensitivity (50% threshold)**: stable_rank + perplexity 最强（两者在 50% corruption 即可检出）\\n- **论文叙事**: 不是\\\"一个最佳信号\\\"，而是\\\"信号的互补操作范围\\\" — stable_rank 做 early alarm, spectral_entropy 做 severity meter, perplexity 做 cross-method 锚点。这是 Claim 3 taxonomy 核心价值。\\n- **perplexity within-gen 几乎无效** (AUC=0.534) — 作为\\\"最常用 collapse 指标\\\"这是 strong counterpoint\\n- 数据来源: signal_heatmap (cross-method), early_warning_roc (within-gen), plan006 (cross-gen Cohen's d)\\n\\n## 2026-05-15: Cross-Method Signal Sensitivity 分层发现（影响论文叙事）\\n\\n- **spectral_entropy 是 late detector**: 50% corruption 下 effect size < 5%（QLoRA +25.7% vs Full FT +16.1% 仅在 100% 下显著）。Cohen's d 最高≠早期检测能力最强。\\n- **stable_rank + perplexity 是 early detector**: 50% corruption 即可检出（stable_rank +564.8% QLoRA / +310.5% FT; PPL +5255% / +1597%）\\n- **论文分层表述策略**: C2（早期预警）主推 stable_rank + perplexity; C3（taxonomy）中 spectral_entropy 作为 \\\"severity discriminator\\\"（区分中/高严重度）。不矛盾但需分层——\\\"不同信号在不同严重度区间有不同灵敏度\\\"反而强化 taxonomy 价值。\\n- **跨方法一致性**: 6/7 信号方向跨 QLoRA/Full FT 一致 → 强化 C1\\n- **HellaSwag 不敏感**: 100% 下仅 -1.15%，确认不适合做 collapse detector\\n- **待 Director 确认**: D029 (headline = spectral_entropy) 是否需要调整措辞，或采用分层策略\\n\\n## 2026-05-15: plan006 Signal Taxonomy 关键分析洞察\\n\\n- **排名方法**: 必须用 Cohen's d（不是 max_rel_change）排名信号灵敏度。max_rel_change 对小基数信号（self_bleu）严重膨胀。Director 明确指令。\\n- **⚠️ 3-seed 修正（重要）**: 2-seed 排名存在过拟合。stable_rank 从 rank 1 暴跌到 rank 4（d: 61.7→9.43），原因是 seed44 引入 frac=50% 方差（CV=0.022）。spectral_entropy 升至 rank 1（d=33.48, CV=0.0015 最低=最稳定）。最终排名需等 5-seed 确认。\\n- **3-seed Tier 1** (|d|≥5): spectral_entropy=33.48, perplexity=20.82, distinct_1=14.60, stable_rank=9.43, distinct_2=7.59, distinct_3=7.08\\n- **self_bleu 陷阱**: max_rel_change 39% 但 Cohen's d 仅 3.5（第 7 名），小基数放大（0.003→0.002），CV=0.055 最高（最不稳定）。论文中不要引用 self_bleu 作为 top signal。\\n- **信号冗余**: ppl/stable_rank/spectral_entropy 高度相关(ρ>0.95)。论文不应把它们当独立证据——Claim 3 应聚焦 operating range 差异而非信号独立性。\\n- **最小监控集**: spectral_entropy (spectral 代表, 最稳定) + token_entropy (互补 output 信号) + hellaswag (独立下游检测)\\n- **gradient_norm 是一次性探测器**: gen1 spike +33% 后回落至 baseline。对比 stable_rank 持续升高不回落——paper narrative 角度: \\\"trigger alert vs continuous monitor\\\"\\n- **SIGMA vs stable_rank 判别力差距**: stable_rank d 是 sigma_effective_rank 的 47x(gen1) → 320x(gen4)。差距随 collapse 累积指数增长。这是 SIGMA differentiation claim 的硬数据。⚠️ SIGMA \\\"d\\\" 实为 N=1 relative change，需 ≥3 seeds 重算。\\n- **统计检验力**: N=3 Wilcoxon 不可用（min p=0.25）。Bootstrap 95% CI 下界远离 0（Tier 1 稳健）。hellaswag 唯一 CI 跨 0 → 不适合做 claim。正式 testing 需 N≥5。\\n\\n## 2026-05-15: plan008 Self-Recovery 关键非数值发现\\n\\n- **3-seed 更新**: Recovery prevalence 89%→100% (9/9)。PPL RR 0.51→0.5245±0.027（高度一致）。Weight-space 信号恢复更慢（stable_rank/spectral_entropy RR~0.32）vs output 信号（PPL RR~0.52）。\\n- **100% 非单调矛盾已澄清**: 核心信号（ppl/stable_rank/token_entropy/spectral_entropy）在 100% 下严格单调崩溃。hellaswag gen3=0.41→gen4=0.43 的微弱反弹驱动了代码输出 `100pct_monotonic_collapse: false`。论文叙事应区分核心信号单调 vs downstream 噪声波动。\\n- **Output vs Spectral 恢复差异**: Output 信号 (token_entropy 62.4%, PPL 51.0%) 恢复远强于 spectral 信号 (stable_rank 33.9%, spectral_entropy 34.0%)。含义：spectral structure damage 更持久，output diversity 更易恢复。对 Claim 3 信号分类学直接相关。\\n- **gradient_norm 跨尺度不一致**: 1.5B 模型在 50% mixing 下 gradient_norm 完全恢复+overshoot (>100%)，0.5B 单调下降。此信号不可跨模型尺度泛化——论文中需标注。\\n- **Threshold 分析受阻**: seed42/43 在 autodl-5090 上只有 0%/50%/100% 三个 fraction（非预期 6 个），中间 fraction (10/25/75%) 数据需等 plan001 后续 seed。\\n\\n## 2026-05-15: 状态检查必须基于文件证据（D018 教训）\\n\\n- **问题**：从 Worker 报告的 log tail 推断 seed 进度，导致 plan002 metrics 三处事实性错误（GPU-frac 分配错、seed 进度高估、声称不存在的 seed 目录）\\n- **硬规则**：所有状态检查必须基于 `ls` 确认目录存在 + `wc -l` 确认 JSONL 行数，禁止从日志内容推断进度\\n- **Worker 指令模板**：要求 Worker 先 `ls -d outputs_*` 确认存在，再逐目录 `ls -la` + `wc -l`，最后才看日志\\n\\n## 2026-05-15: pipeline.py resume 逻辑 bug（D016, 已部署）\\n\\n- **根因**：`all_summaries = []` 在每个 fraction 循环开始，`is_gen_complete()` 返回 True 时 `continue` 跳过但不回填 summary → 覆写后数据丢失\\n- **症状**：plan_003 重启后 summary_0pct.json = []，summary_50pct.json 只有 gen3-4\\n- **修复**：skip 分支从 signals JSONL 最后一条记录重建 summary entry 并 append\\n- **signals JSONL 数据完好**，可用 `rebuild_summaries.py` 重建\\n\\n## 2026-05-15: Full FT vs QLoRA 信号差异（待 plan_003 完成后分析）\\n\\n- **初步观察**：plan_003 Full FT 0.5B frac=50% gen3 的 ppl=25.73、stable_rank=40.34，远高于 MVP QLoRA 同条件 ppl=16.95、stable_rank=24.79\\n- **含义**：Full FT 下 collapse severity signals 放大效应更强——可能支撑 \\\"collapse severity 与训练方法相关\\\" claim\\n- **行动**：plan_003 frac=1.0 完成后，系统对比 Full FT vs QLoRA 全 fraction 信号曲线\\n\\n## 2026-05-15: Cross-gen 非单调度量（Reviewer 方法论升级，待落地）\\n\\n- **问题**：Spearman ρ 对 onset-then-plateau 模式天然低估。v2 已有绝对值 delta/max-dev/AUC，但缺相对化度量和 plateau 检测\\n- **待加入 3 个度量**：\\n  1. **gen0→gen1 effect size** (onset magnitude): `(signal_gen1 - signal_gen0) / signal_gen0`\\n  2. **max deviation (relative)**: `max(|signal_genK - signal_gen0|) / signal_gen0`\\n  3. **plateau detection**: gen1-gen4 coefficient of variation，低 CV = 信号饱和\\n- **时机**：plan_001 下一批 seed 完成后增量分析时加入\\n\\n## 2026-05-15: Checkpoint 持久化修复（D016, 已部署）\\n\\n- **根因**：`train.py:211` `save_strategy=\\\"no\\\"` + pipeline.py 无 `save_pretrained`\\n- **修复**：pipeline.py L125-130 在 merge_adapter() **之前** `save_pretrained` + train.py `save_strategy=\\\"epoch\\\"`\\n- **autodl-5090 hotfix 已验证**（__pycache__ cleared, seed45+ 将正常保存）\\n- **plan_003 gen0-2 HellaSwag 缺失无法恢复**（checkpoint 从未存在）\\n\\n## 2026-05-15: SIGMA 方向（⚠️ PROVISIONAL, C001 约束）\\n\\n- **初步观察：expected_direction = +1**（effective_rank 在 collapse 时上升）\\n- data corruption → 表示弥散 vs SIGMA recursive collapse → 表示坍缩，方向相反\\n- **⚠️ N=2 未验证，禁止在论文/分析中当已验证结论**\\n\\n## 2026-05-15: Preliminary 1.5B 分析 v2（seed42+43, frac 0%/50%）\\n\\n- **AUC 排名**：stable_rank (10.73) > perplexity (3.91) > training_loss (2.33, baseline)\\n- **Spearman 失效确认**：stable_rank ρ=0.15 但 AUC 最强（spike+plateau）\\n- **MaxDev 全在 gen=1**：支持 early detection narrative\\n\\n## 2026-05-15: cqa1-37219 HellaSwag 离线崩溃\\n\\n- **教训**：新服务器 checklist 必须 (1) 下载 eval 数据集 (2) 在线 load_dataset 填充 modules cache (3) 验证离线 load\\n\\n## 2026-05-14: SIGMA H2H 代码准备完成 (plan_009)\\n\\n- `compute_all_spectral_metrics()` 零额外开销联合采集 SIGMA + SVD\\n- MVP 信号 vs PPL 相关性：stable_rank ρ=0.829, token_entropy ρ=-0.811, spectral_entropy ρ=0.804\\n\", \"total_chars\": 8235, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6a9320f4-6264-4ce5-8c66-babda20a9696",
  "isSidechain": true,
  "promptId": "80dd2a4d-c31a-43ae-8316-4a6135d9fed6",
  "agentId": "ade4d670d78b2afaf",
  "type": "user",
  "uuid": "0cbae219-7614-4751-8f8d-7ccdffb4fe26",
  "sourceToolAssistantUUID": "6a9320f4-6264-4ce5-8c66-babda20a9696",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T10:42:48.492Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01WfhNrPQg7znnfyYM5mVWSd`</summary>

```json
{
  "project": "collapse_severity_monitor",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0cbae219-7614-4751-8f8d-7ccdffb4fe26",
  "isSidechain": true,
  "agentId": "ade4d670d78b2afaf",
  "requestId": "req_011Cb67GRntJdS1h3HKjPsGH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2484963c-8c96-46bd-95ee-d3eb61788abf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012kqUWH6P5XM7Zm4FHmUHTS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16993,
      "cache_read_input_tokens": 16774,
      "output_tokens": 300,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16993
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 300,
          "cache_read_input_tokens": 16774,
          "cache_creation_input_tokens": 16993,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16993,
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

_source line 18 · 2026-05-16T10:42:48.503Z_

<details><summary>↩ Tool result · `toolu_01WfhNrPQg7znnfyYM5mVWSd`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/ideas.md\", \"content\": \"# Idea Inbox\\n\\n## 待验证\\n\\n- [2026-05-15] **⚠️ PROVISIONAL — SIGMA 方向差异假设（C001 约束，N=2 未验证）。** 初步观察：data corruption collapse 下 effective_rank↑（表示弥散），而 SIGMA 论文的 recursive collapse 下 effective_rank↓（表示收缩）。方向相反。**此为 provisional 假设，需 plan_001 seed43-46 + plan_003 Full FT SIGMA 数据验证后才能定论。禁止在论文或分析中当已验证结论使用。**\\n- [2026-05-15] **Gen1 phase-transition 模式（Reviewer 提出，n=2 初步确认）。** 处理组信号呈 gen0→gen1 剧变 + gen2-4 plateau 模式，非单调。暗示第一代 synthetic data corruption 冲击最大，后续代次模型\\\"适应\\\" corrupted distribution。若 plan_001 全数据确认，可作为 Claim C3（non-uniform behavior）的补充证据或独立发现。需要 cross-fraction 验证此模式是否随 contamination fraction 增大而加剧。\\n\\n## ACTIVE\\n\", \"total_chars\": 612, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2484963c-8c96-46bd-95ee-d3eb61788abf",
  "isSidechain": true,
  "promptId": "80dd2a4d-c31a-43ae-8316-4a6135d9fed6",
  "agentId": "ade4d670d78b2afaf",
  "type": "user",
  "uuid": "86850dd3-2743-4bc7-a572-18ca4c7e587d",
  "sourceToolAssistantUUID": "2484963c-8c96-46bd-95ee-d3eb61788abf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T10:42:51.166Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_011f1xvrPmVio1o8FMV9e9iz`</summary>

```json
{
  "project": "collapse_severity_monitor",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86850dd3-2743-4bc7-a572-18ca4c7e587d",
  "isSidechain": true,
  "agentId": "ade4d670d78b2afaf",
  "requestId": "req_011Cb67Gpj2KSZiXdzEmbTXJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ae1bc184-42c4-473d-8562-b4c8ba334102",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0171X1gLHaJBRMFCHStqEvaU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11879,
      "cache_read_input_tokens": 33767,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11879,
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

_source line 20 · 2026-05-16T10:42:51.189Z_

<details><summary>↩ Tool result · `toolu_011f1xvrPmVio1o8FMV9e9iz`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/decisions.yaml\", \"content\": \"_next_id: 42\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 04:21 UTC\\n  summary: MVP 设计：Qwen2.5-1.5B QLoRA × WikiText-2 × 3 fractions × 5 generations，验证信号-collapse\\n    相关性\\n  rationale: 核心假设是训练动态信号能跟踪 collapse 严重度。用最小配置（1 model × 1 dataset × 3 fractions ×\\n    1 seed × 5 gens）验证是否 ≥2 信号族 Spearman ρ > 0.7。EMNLP ARR DDL 5/25 仅剩 11 天，必须 2 天内完成\\n    MVP 判定。选 1.5B+QLoRA 因为这是 proposal 的主实验配置，且计算量适中（~15-20h 单卡）。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 04:24 UTC\\n  summary: 采纳 Reviewer 4 项 MVP 设计改进：AUROC 降级为辅助、5 代 collapse 不足 contingency、边界情况 0/1/≥2\\n    预定义规则\\n  rationale: Reviewer 指出单种子 AUROC 统计效力不足（warning）、5 vs 7 代假阴性风险、n=15 置信区间宽、缺边界处理规则。全部合理：(1)\\n    AUROC 改为辅助参考不作 gate；(2) 100% fraction 5 代 perplexity 退化 &lt;10% 则追加至 7 代；(3) 0\\n    信号=hard fail, 1 信号=conditional+追加 seed, ≥2=pass；(4) MVP pass 仅为 go/no-go 不代表论文结论。防止事后\\n    rationalization。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 06:28 UTC\\n  summary: MVP 模型从 Qwen2.5-1.5B 切换为 Qwen2.5-0.5B，解除下载阻塞\\n  rationale: 1.5B 模型下载连续 3 次失败（AutoDL 网络不稳定），累计浪费 1.5h，GPU 0% 利用率。0.5B 已下载就绪（954MB）。MVP\\n    核心假设（信号-collapse 相关性）与模型大小无关，0.5B 足以验证 go/no-go。1.5B 留作 Phase 2 全量实验的 main sweep\\n    模型。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n  - D002\\n- id: D004\\n  date: 2026-05-14 07:42 UTC\\n  summary: MVP 生成优化：subsample 1500 chunks + gen_batch_size 32，预计 80h → 12-15h\\n  rationale: Reviewer 发现 autoregressive generation 是瓶颈（4.25h/gen × 15 gens = 64h），原预估\\n    8-12h 完全遗漏生成开销。A+B 组合：(1) subsample 从 4916→1500 chunks（768K tokens 足够训练和多样性评估，oversample\\n    填满训练集），(2) gen_batch_size 8→32（GPU 显存余量充足）。DDL 5/25 不允许 80h 单卡跑。\\n  related_experiments: []\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-14 20:40 UTC\\n  summary: MVP PASS — 训练动态信号追踪 collapse 严重度假设成立，进入 research 阶段\\n  rationale: Gate check 2/3 signal families PASS (spectral ρ=1.0, output ρ=1.0)。三级剂量反应清晰：0pct\\n    稳定无退化、50pct 轻微退化后部分恢复、100pct 超线性 collapse (PPL 53×, stable_rank 6.6×)。Early warning\\n    在 3% 训练进度即可检测。Downstream (HellaSwag) FAIL 因 0.5B 模型太弱，非假设问题。研究阶段需解决：n=1 seed/model/dataset、cross-fraction\\n    n=3 统计效力弱、stable_rank gen2+ 饱和、50pct non-monotonic recovery 需要解释。\\n  related_experiments:\\n  - exp_id: mvp_frac0\\n    role: control baseline\\n    result: 5 代稳定无退化\\n  - exp_id: mvp_frac50_100\\n    role: dose-response gradient\\n    result: 50pct 轻微退化+恢复, 100pct 超线性 collapse (PPL 839, SR 155.6)\\n  - exp_id: within_gen_temporal\\n    role: early warning 验证\\n    result: step 50 (3%) SR 偏差 34.4%\\n  depends_on: []\\n- id: D006\\n  date: 2026-05-14 20:41 UTC\\n  summary: MVP PASS — 进入 research 阶段，叙事方向定为 analysis paper\\n  rationale: Gate check 2/3 families PASS（spectral ρ=1.0, output ρ=1.0）。核心假设\\\"训练动态信号追踪\\n    collapse 严重度\\\"得到强支撑。Early warning 在 3% 训练进度即可检测。叙事采用 analysis paper 定位（系统性分析哪些信号能追踪\\n    collapse、在什么条件下有效），Reviewer 评估认为比 method paper 更匹配当前数据且审稿标准更有利。\\n  related_experiments:\\n  - exp_id: mvp_frac0\\n    role: control baseline\\n    result: 5 代完全稳定，PPL 波动 <0.5%\\n  - exp_id: mvp_frac50_100\\n    role: 主实验\\n    result: 2/3 gate PASS, 100pct 超线性 collapse (PPL 53×), 50pct partial recovery\\n  - exp_id: within_gen_analysis\\n    role: 补充分析\\n    result: stable_rank 3% 进度即检测到 34.4% 偏差\\n  depends_on: []\\n- id: D007\\n  date: 2026-05-14 22:14 UTC\\n  summary: 采纳 Dream 审稿建议：plan_001 升至 5 seeds，plan_002 升至 3 seeds，per-layer 降级 P2\\n  rationale: Dream worst-case 3/6 Weak Reject。致命问题：(1) 3 seeds 不足以支撑 variance claim（bootstrap\\n    CI ±50%），5 seeds 是最低可辩护线；(2) PubMed 1 seed 与论文反对 single-seed 的 message 自相矛盾。per-layer\\n    连续 5 次失败，降级等 plan_001 数据后在 1.5B 上重做。GPU 预算从 ~105h 升至 ~200h，双卡 wall time ~100h（~4天），可接受。\\n  related_experiments:\\n  - exp_id: plan_001\\n    role: target\\n    result: seeds 3→5, budget 90h→150h\\n  - exp_id: plan_002\\n    role: target\\n    result: seeds 1→3, budget 15h→45h\\n  - exp_id: plan_007\\n    role: deprioritized\\n    result: P1→P2, 等 plan_001 数据\\n  depends_on: []\\n- id: D008\\n  date: 2026-05-14 22:14 UTC\\n  summary: 'Dream review processed: increase seeds (3→5 WikiText, 1→3 PubMed), fix\\n    ROC methodology, add SIGMA head-to-head, calibrate claims'\\n  rationale: 'Dream (full, 2 reviewers) returned Best=4/6 Weak Accept, Median=4/6\\n    Borderline Reject, Worst=3/6 Weak Reject. Median doesn''t pass — plan has low\\n    tolerance for bad outcomes. Cross-tier consensus: (1) 3 seeds insufficient for\\n    variance claims, #1 improvement; (2) PubMed single-seed contradicts paper''s own\\n    anti-single-seed argument; (3) ROC pools non-independent generations; (4) self-recovery\\n    overclaimed vs data mixing literature; (5) related work too thin; (6) no theoretical\\n    grounding. All addressable. Extra ~90 GPU-hours (~2 days) for seed increase, well\\n    within NeurIPS timeline. Updated experiment_plan.yaml and paper_framing.md accordingly.'\\n  related_experiments:\\n  - exp_id: plan_001\\n    role: modified\\n    result: seeds 3→5, GPU 90→150h\\n  - exp_id: plan_002\\n    role: modified\\n    result: seeds 1→3, GPU 15→45h\\n  - exp_id: plan_009\\n    role: added\\n    result: SIGMA head-to-head, P1\\n  - exp_id: plan_010\\n    role: added\\n    result: 3B spot-check, P2\\n  depends_on: []\\n- id: D009\\n  date: 2026-05-14 22:15 UTC\\n  summary: Dream 审稿完成：best 4/6 Weak Accept, median 4/6 Borderline Reject, worst 3/6\\n    Weak Reject。实验计划与 dream 反馈对齐，解除 P0 实验审批封锁。\\n  rationale: 三档审稿共性问题（seeds、ROC方法论、PubMed单seed、SIGMA区分度）均已在 experiment_plan 中预置解决方案。best\\n    case 已达 Weak Accept 说明方向正确，执行到位可达接收线。worst case 的 gen8+ 建议和 7B 需求暂不纳入主线（GPU 预算限制），但\\n    plan_010(3B) 可部分缓解 scale 担忧。论文写作层面需修复：stable rank 方向解释、合成数据参数文档化、25%分类修正、related\\n    work 大幅扩展。\\n  related_experiments:\\n  - exp_id: dream_20260514T204316\\n    role: dream_simulation\\n    result: best=4/6, median=4/6, worst=3/6\\n  depends_on: []\\n- id: D010\\n  date: 2026-05-14 23:53 UTC\\n  summary: SIGMA 集成选 Option A：立即修改 signals.py，plan_001 剩余 runs 实时采集\\n  rationale: Reviewer 发现 pipeline.py 不保存 checkpoint，plan_009 的\\\"复用 checkpoint\\\"假设不成立。Option\\n    A 立即改 signals.py，当前运行的 2 个 run（各 GPU 的 seed=42）不受影响（已加载旧模块），后续 28 个 run 新进程自动采集\\n    SIGMA。丢 2/30 run 的 SIGMA 数据可接受（4 seeds 完整），零额外 GPU 开销。\\n  related_experiments:\\n  - exp_id: plan_009\\n    role: target\\n    result: pending\\n  - exp_id: plan_001\\n    role: data_source\\n    result: running\\n  depends_on: []\\n- id: D011\\n  date: 2026-05-15 03:16 UTC\\n  summary: 废弃 per-layer 三区叙事，改为 sub-module-centric 分析\\n  rationale: Appendix 数据修复后发现：§4.4 的\\\"三区结构\\\"（boundary/middle-neutral/late-bifurcation）基于错误数据。真实\\n    per-layer 数据显示 v_proj 在几乎所有层都有强烈 diffusion（ΔSR +1~+3），middle layers 并非 neutral（L3\\n    v_proj +2.633）。down_proj L11-L12 collapse 仍成立。新叙事：sub-module type 比 layer position\\n    更能预测 collapse 响应——v_proj 全架构 diffuse，down_proj 局部 collapse，其余稳定。强化 Claim 3 的粒度。\\n  related_experiments:\\n  - exp_id: per_layer_analysis_v5\\n    role: source\\n    result: 三区叙事与真实数据矛盾，middle_sr_delta=0.01 为错误值\\n  depends_on: []\\n- id: D012\\n  date: 2026-05-15 09:22 UTC\\n  summary: 目标会议从 NeurIPS 2026 转为 EMNLP 2026，用户指令\\n  rationale: 用户决定转投 EMNLP 2026。EMNLP 作为 NLP A 类会议，与本项目研究内容（LLM 训练动态信号追踪 collapse severity）更对口。DDL\\n    预计 2026 年 6 月中旬（待确认），比 NeurIPS late May 多 ~2-3 周缓冲。用户承诺资源不够可以加。\\n  related_experiments:\\n  - exp_id: plan_001\\n    role: core\\n    result: running\\n  - exp_id: plan_002\\n    role: core\\n    result: planned\\n  depends_on: []\\n- id: D013\\n  date: 2026-05-15 09:28 UTC\\n  summary: 确认 EMNLP 2026 ARR DDL 5/25，10 天冲刺排期，用户授权加资源\\n  rationale: 用户确认目标为 5/25 ARR cycle 投 EMNLP 2026。时间线：plan_001 ETA 5/16，plan_002 ETA\\n    ~5/17，P1 实验 ~5/18，分析 ~5/19，论文 5/19-24，提交 5/25。紧但可行。用户授权加资源。计划：(1) 申请 2 张额外 4090\\n    并行跑 plan_003+plan_010，所有 GPU 实验 5/17 完成；(2) plan_001 数据一到位立即启动全部 CPU 分析；(3) 5/18\\n    启动 Paper Agent Full Draft。\\n  related_experiments:\\n  - exp_id: plan_001\\n    role: core\\n    result: running\\n  - exp_id: plan_002\\n    role: core\\n    result: starting\\n  - exp_id: plan_003\\n    role: supporting\\n    result: planned\\n  - exp_id: plan_010\\n    role: supporting\\n    result: planned\\n  depends_on:\\n  - D012\\n- id: D014\\n  date: 2026-05-15 13:34 UTC\\n  summary: SIGMA expected_direction=+1 标记为 provisional，禁止论文引用为结论\\n  rationale: Reviewer 审查 SIGMA direction verify worker 产出，发现 3 个问题：(1) N=2 (seed43,\\n    frac 0%/50%) 下方向判断无统计意义；(2) within-gen corruption vs recursive collapse 的理论区分过于简化——pipeline\\n    本身是跨代递归 (gen0→gen1→...→gen4)，高 fraction 在 gen3+ 实质训练多轮递归退化数据，与 SIGMA 场景非泾渭分明；(3)\\n    memory.md 中\\\"方向差异是 discussion 亮点\\\"属于 premature rationalization。决定：expected_direction=+1\\n    作为工作假设保留（与经验观测一致），但标注 provisional。验证条件：plan_001 seed43-46 全量数据 + plan_003 Full\\n    FT SIGMA 数据。如果 Full FT 方向也是 +1 则可排除 QLoRA confound，否则需重写分析。\\n  related_experiments:\\n  - exp_id: plan_009\\n    role: target\\n    result: SIGMA direction provisional +1\\n  - exp_id: plan_001\\n    role: verification_source\\n    result: pending seed43-46 full data\\n  - exp_id: plan_003\\n    role: verification_source\\n    result: pending Full FT SIGMA data\\n  depends_on:\\n  - D010\\n- id: D015\\n  date: 2026-05-15 14:17 UTC\\n  summary: plan_003 gen0-2 HellaSwag 缺失接受（A+C），checkpoint 空目录无法补跑；立即修复 plan_001/002\\n    checkpoint 持久化\\n  rationale: plan_003 frac=0.0 全部 checkpoint 目录为空，gen0-2 HellaSwag 无法补跑。选择接受(A)+论文标注(C)：(1)\\n    frac=0.0 是 clean baseline，gen3=0.426/gen4=0.430 几乎不变，gen0-2 可合理推断在同范围；(2) plan_003\\n    核心目的是验证 signal 行为在 Full FT 下一致，signals 数据完好不影响主 claim；(3) 重跑 2h 性价比低（DDL 5/25）。但发现跨实验系统性问题：所有实验\\n    ckpt 目录均空，plan_001/002 也面临同样风险——必须立即修复 pipeline checkpoint 保存逻辑，至少保留 LoRA adapters，否则未来任何\\n    post-hoc eval 都不可能。\\n  related_experiments:\\n  - exp_id: plan_003\\n    role: affected\\n    result: gen0-2 HellaSwag permanently lost, accept gap\\n  - exp_id: plan_001\\n    role: at_risk\\n    result: checkpoint persistence fix needed NOW\\n  - exp_id: plan_002\\n    role: at_risk\\n    result: checkpoint persistence fix needed NOW\\n  depends_on:\\n  - D013\\n- id: D016\\n  date: 2026-05-15 14:19 UTC\\n  summary: 修复 checkpoint 不保存 bug：LoRA 实验存 adapter-only，Full FT 存完整模型，立即热更新 running\\n    experiments\\n  rationale: train.py save_strategy=\\\"no\\\" 导致所有实验 checkpoint 目录全空，已完成的 gen 数据不可恢复。选择\\n    adapter-only 方案（~10MB/ckpt）而非 merged model（~1GB/ckpt），磁盘开销低 100 倍且可重建完整模型。Full\\n    FT 无 adapter 必须存完整模型（~1GB/ckpt, 15GB total 可接受）。立即 patch running experiments 以减少数据损失。\\n  related_experiments:\\n  - exp_id: plan_001\\n    role: affected\\n    result: seed44 gen1 running, gen0-1 ckpt lost\\n  - exp_id: plan_002\\n    role: affected\\n    result: seed42 gen2 running, gen0-2 ckpt lost\\n  - exp_id: plan_003\\n    role: affected\\n    result: gen0-2 ckpt lost, 维持 A+C 方案\\n  depends_on: []\\n- id: D017\\n  date: 2026-05-15 15:15 UTC\\n  summary: HellaSwag gen0-2 缺失不补跑：plan_001 承担 HellaSwag 主线叙事，plan_003 只报告 signals\\n    对比，Limitations 诚实标注\\n  rationale: Reviewer 评估 + 增量分析共同确认：(1) plan_003 是 0.5B，HellaSwag 本身在该 scale 失效（Claim\\n    3 的 failure case），gen3-4 两点足以佐证 (2) 增量分析 HellaSwag p=0.272 无区分力，补跑 3 个点边际收益极低\\n    (3) 5h cuda:2 机会成本高于收益 (4) plan_001 (5 seeds×6 fracs) 提供完整 HellaSwag story\\n  related_experiments:\\n  - exp_id: plan_003\\n    role: affected\\n    result: gen0-2 HellaSwag 永久丢失，接受\\n  - exp_id: plan_001\\n    role: primary\\n    result: 承担 HellaSwag 主线叙事（5 seeds 有统计效力）\\n  depends_on:\\n  - D015\\n  - D016\\n- id: D018\\n  date: 2026-05-15 16:26 UTC\\n  summary: pipeline.py resume bug 确认为 critical，启动三步修复：重建 summary → 修复代码 → 重跑缺失评估\\n  rationale: Reviewer critical 确认：run_pipeline() resume 时 all_summaries=[] 重置 + is_gen_complete\\n    skip 导致已完成 gen 的 summary 系统性丢失。plan003 frac=0% 全丢、frac=50% 丢 gen0-2。训练信号可从 JSONL\\n    重建，但 hellaswag/self_bleu/distinct_n 需重跑评估。同时 autodl-5090 checkpoint 空目录需排查 __pycache__\\n    问题。\\n  related_experiments:\\n  - exp_id: plan003-fullft-05B\\n    role: affected\\n    result: summary data partially lost due to resume bug\\n  depends_on: []\\n- id: D019\\n  date: 2026-05-15 16:27 UTC\\n  summary: pipeline.py resume bug 确认 + summary 重建方案批准 + plan002 metrics 纠错\\n  rationale: Reviewer 确认 pipeline.py resume 逻辑在重启后丢失已完成 gen 的 summary 数据（all_summaries=[]\\n    重置 + continue 跳过）。批准 rebuild_summaries.py 从 JSONL 信号文件重建。同时 Reviewer 核实 plan002\\n    registry metrics 三处事实错误（GPU 分配/seed 进度/不存在目录），要求 Agent 基于文件证据修正。\\n  related_experiments:\\n  - exp_id: plan003-fullft-05B\\n    role: affected\\n    result: summary data loss from resume bug\\n  - exp_id: plan002-pubmed-cqa1\\n    role: affected\\n    result: registry metrics factually incorrect, true progress ~11%\\n  depends_on: []\\n- id: D020\\n  date: 2026-05-15 16:39 UTC\\n  summary: Seed44 let finish naturally; accept hellaswag gap for seeds 42-44\\n  rationale: '__pycache__ stale bytecode caused all checkpoints to be empty for seed42/43/44.\\n    Core signals (ppl, stable_rank, spectral_entropy, token_entropy) collected in\\n    real-time are unaffected. Hellaswag requires checkpoints for eval, so plan_001\\n    will only have hellaswag for seeds 45+46 (2/5). Killing seed44 wastes ~40min training\\n    with no ckpt recovery for gen0-2. Mitigation: downstream signals presented as\\n    supporting evidence (n=2 seeds), spectral+output carry primary statistical claims\\n    (n=5 seeds). plan_002 PubMed runs with new code will have full hellaswag coverage.'\\n  related_experiments:\\n  - exp_id: plan_001\\n    role: affected\\n    result: seed42-44 ckpt empty, hellaswag unrecoverable\\n  - exp_id: plan_003\\n    role: affected\\n    result: frac=0%/50% hellaswag partially lost\\n  - exp_id: plan_002\\n    role: mitigation\\n    result: new code, full hellaswag expected\\n  depends_on: []\\n- id: D021\\n  date: 2026-05-15 17:09 UTC\\n  summary: Fraction 覆盖率缺陷确认：plan001/002 只跑 2 fractions（0%/50%），必须立即补 frac=1.0，目标 6\\n    fractions\\n  rationale: Reviewer 通过 /proc/cmdline 确认根因：bash 启动脚本只遍历 seeds 不遍历 fractions。2 fractions\\n    的 Spearman ρ 统计上 trivial（只有 +1/-1），无法支撑 severity correlation claim。paper_framing.md\\n    已将 n=3 fractions 列为 HIGH severity 审稿人攻击面。最低可行：补 frac=1.0 达到 3 fractions；目标：6 fractions\\n    完整 severity gradient。优先级：P0——比新 seed 更重要，直接影响论文核心 claim 可信度。\\n  related_experiments:\\n  - exp_id: plan_001_wikitext_15B_5seeds\\n    role: affected\\n    result: only 2/6 fractions running\\n  - exp_id: plan002-pubmed-cqa1\\n    role: affected\\n    result: only 2/6 fractions running\\n  depends_on:\\n  - D013\\n- id: D022\\n  date: 2026-05-15 17:17 UTC\\n  summary: D021 修正：bash 脚本确实遍历 6 fractions（fraction-outer/seed-inner），不需要手动补跑。撤回手动启动\\n    frac=1.0 指令\\n  rationale: Reviewer 通过 bash 源码 + /proc PPid 链证实 run_plan001.sh 的外层循环就是 fractions，当前只看到\\n    frac=0.0/0.5 是因为还没轮到下一个 fraction。D021 的诊断基于 Worker 只看了单个 Python 进程的 cmdline（只有一个\\n    fraction 值），未检查 bash 父进程。手动启动进程会导致 GPU 冲突和文件写入冲突。全部 6 fractions × 5 seeds 自动完成\\n    ETA ~5/20-21，DDL 前 4-5 天。仍待决策：是否在安全窗口改循环顺序为 seed-outer/fraction-inner 以提前获得 seed42\\n    完整 6-fraction 数据。\\n  related_experiments:\\n  - exp_id: plan_001_wikitext_15B_5seeds\\n    role: affected\\n    result: 6 fractions will auto-execute, no manual intervention needed\\n  - exp_id: plan002-pubmed-cqa1\\n    role: affected\\n    result: same — auto-execute\\n  depends_on:\\n  - D021\\n- id: D023\\n  date: 2026-05-15 17:19 UTC\\n  summary: 保持当前 fraction-outer/seed-inner 循环顺序不变，不改脚本。seed42 ~5/16 晚获得 4 fractions，~5/18\\n    获得 6 fractions，全部 ~5/20-21\\n  rationale: 改循环顺序让 seed42 提前 ~30h 获得 6 fractions（5/16 晚 vs 5/18），但需要 kill bash 脚本重启，风险/收益不对称：(1)\\n    已经历一次诊断错误（D021），不宜再动运行中的脚本；(2) 当前顺序下 seed42 ~5/16 晚自然获得 4 fractions（0.0/0.1/0.5/0.75），Paper\\n    Agent 5/17 启动时已有足够数据做 preliminary severity correlation；(3) 全部完成 ETA 不变（~5/20-21），DDL\\n    前 4-5 天；(4) Reviewer 建议如时间紧可减 seeds 而非改循环，保留此 fallback。\\n  related_experiments:\\n  - exp_id: plan_001_wikitext_15B_5seeds\\n    role: primary\\n    result: keep fraction-outer order\\n  - exp_id: plan002-pubmed-cqa1\\n    role: primary\\n    result: keep fraction-outer order\\n  depends_on:\\n  - D022\\n- id: D024\\n  date: 2026-05-15 17:38 UTC\\n  summary: Claim 3 升级：collapse trajectory duality (cliff+saturation vs snowball) +\\n    terminal spectral convergence + hellaswag method-dependence\\n  rationale: plan003 Full FT 完整数据揭示三个关键发现：(1) Full FT 和 QLoRA 呈现质性不同的崩塌路径——Full FT\\n    cliff+saturation (15.3x gen1, 1.11x gen1→4) vs QLoRA snowball (1.7x gen1, 31.8x\\n    gen1→4)；(2) 终态谱属性收敛 (SR ~154-156, SE ~0.884-0.889)，训练方式改变路径不改变终态；(3) hellaswag\\n    在 Full FT 下单调下降 (tracking indicator) 而 QLoRA 下稳定 (lagging indicator)，且 QLoRA PPL\\n    更高(839)但下游更好(0.430 vs 0.372)。这些发现将 Claim 3 从简单的 signal taxonomy 升级为包含训练方式维度的 signal×method\\n    交互分析。同时限定 non-monotonic claim 仅适用于 frac=50%。\\n  related_experiments:\\n  - exp_id: plan003-fullft-0.5B\\n    role: primary_evidence\\n    result: success\\n  - exp_id: plan008-nonmonotonic\\n    role: claim_refinement\\n    result: scope_limited\\n  depends_on: []\\n- id: D025\\n  date: 2026-05-15 17:39 UTC\\n  summary: Supersede D023：批准 plan001 v2 脚本切换（seed-outer/fraction-inner），GPU1 优先切换，GPU0\\n    当前 run 结束后切换\\n  rationale: D023 \\\"不动脚本\\\"是 D021 诊断错误后的风险规避。此后 Reviewer 独立评估 v2（seed-outer 循环），确认科学上更优——每完成一个\\n    seed 即获得完整 6-fraction ρ profile，更早产出可分析数据。v2 还重排 fraction 优先级（先跑 0.25/1.0 高信息量点）。风险已通过\\n    Reviewer 评估缓解：v2 只改循环顺序不改 pipeline 逻辑，resume 机制能跳过已完成组合。激活策略：GPU1 seed44 后处理完成后立即切\\n    v2；GPU0 让 v1 跑完当前 seed45 frac=0.0 后再切。\\n  related_experiments:\\n  - exp_id: plan001-wikitext-15B-5seeds\\n    role: target\\n    result: running\\n  depends_on:\\n  - D023\\n- id: D026\\n  date: 2026-05-15 17:41 UTC\\n  summary: D024 修正：Agent 分析中 QLoRA 100% gen1-3 PPL 数据错误，作废 \\\"snowball/exponential\\\"\\n    叙事，改为 \\\"两种方法都 gen1 大跳，差异在后续演化\\\"\\n  rationale: 'Reviewer critical 发现 comparison_data.json 中 QLoRA 100% gen1-3 数据严重失真（gen1:\\n    报告 26.38 vs 实际 136.90，5.19x 低估）。D024 基于错误数据得出的 \\\"cliff+saturation vs snowball\\\"\\n    二元叙事不成立。实际 QLoRA gen1=8.7x（也是大跳，非 1.7x），后续减速增长（gen1→4: 6.13x）。正确对比：两种方法都在 gen1\\n    大幅崩塌（Full FT 15.3x > QLoRA 8.7x），差异在后续——Full FT 饱和，QLoRA 减速但持续增长至更高 PPL（839 vs\\n    326）。已要求 Agent 用正确源数据重做分析。终态谱收敛 finding 需重新验证。'\\n  related_experiments:\\n  - exp_id: plan003-fullft-0.5B\\n    role: primary_evidence\\n    result: data_error_in_analysis\\n  depends_on:\\n  - D024\\n- id: D027\\n  date: 2026-05-15 17:42 UTC\\n  summary: 修正 D015/D017：HellaSwag 失效归因于 QLoRA 训练方式而非 0.5B 模型规模；diversity 指标（distinct_n,\\n    self_bleu）排除在有效 collapse indicator 之外\\n  rationale: plan003 Full FT 0.5B 数据显示 HellaSwag 单调下降 -12.5%（0.425→0.372），证明 0.5B\\n    规模下 HellaSwag 可以检测 collapse，D015/D017 的\\\"0.5B 失效\\\"诊断错误——失效的是 QLoRA 的隐式正则化保护了下游性能。同时\\n    diversity 指标（distinct_1 仅 -3%，self_bleu 几乎不变）在 17x PPL 增长下无反应，原因是 token_entropy\\n    坍缩（-55%）但采样随机性维持了 lexical diversity 表面指标。论文中 Claim 2/3 相关讨论需按此修正归因。\\n  related_experiments:\\n  - exp_id: plan003-fullft-0.5B\\n    role: primary_evidence\\n    result: success\\n  depends_on:\\n  - D024\\n  - D026\\n- id: D028\\n  date: 2026-05-15 19:00 UTC\\n  summary: Claim 3 措辞升级但不拆分：从 \\\"signals differ\\\" 到 \\\"same signal informative vs misleading\\n    across methods\\\"；PPL-downstream dissociation 为 featured sub-result；terminal convergence\\n    降为 observation\\n  rationale: Reviewer 评估 D026 修正后 claim 强度：(1) N=1 Full FT 对比不支持 terminal geometry\\n    convergence 独立 claim；(2) Claim 3 措辞可升级为更强的 practitioner-facing framing；(3) PPL-downstream\\n    dissociation (QLoRA PPL=839/hellaswag=0.430 vs Full FT PPL=326/hellaswag=0.372)\\n    值得 highlight 但 N=1+单任务不支持独立 claim。Claim 1/2 证据未变（待 plan001 6-frac×5-seed），不加强措辞。\\n  related_experiments:\\n  - exp_id: plan003-fullft-0.5B\\n    role: primary_evidence\\n    result: success\\n  depends_on:\\n  - D026\\n  - D027\\n- id: D029\\n  date: 2026-05-15 19:06 UTC\\n  summary: 'Headline signal 从 stable_rank 切换到 spectral_entropy（provisional）：3-seed\\n    数据显示 stable_rank seed-sensitive (d: 61.7→9.43)'\\n  rationale: plan006/008 3-seed 增量分析：stable_rank 的 Cohen's d 从 2-seed 的 61.7 暴跌到 3-seed\\n    的 9.43（rank 1→4），seed44 引入 frac=50% 方差（CV=0.022）。spectral_entropy CV=0.0015 最低，d=33.48\\n    升至 rank 1。2-seed 的 d=61.7 是过拟合。论文中 Claim 2 early warning 和 headline result 从 stable_rank\\n    deviation 改为 spectral entropy deviation。最终排名待 plan001 5-seed 确认。per-layer v_proj\\n    stable_rank 建议（写作笔记 7）仍成立——within-run 灵敏度与 cross-seed 稳定性是不同维度。\\n  related_experiments:\\n  - exp_id: plan006-effect-size\\n    role: primary_evidence\\n    result: ranking_shift\\n  - exp_id: plan008-nonmonotonic\\n    role: supporting\\n    result: updated\\n  - exp_id: plan001-wikitext-15B-5seeds\\n    role: pending_validation\\n    result: running\\n  depends_on:\\n  - D028\\n- id: D030\\n  date: 2026-05-15 19:44 UTC\\n  summary: Paper Agent 5/17 启动策略：先写 structure/methods/related work/intro，Results 用\\n    placeholder 等 plan001 ≥3 seeds × ≥4 fractions 数据\\n  rationale: Reviewer 评估：5/17 时 plan001 数据预计仅 3 seeds × 2 fractions + seed42 可能 4\\n    fractions，不满足矩阵式覆盖。Results 章节用 partial data 写的风险高（story 可能被后续数据推翻）。但 structure/methods/related\\n    work/intro 不依赖最终数据，可先启动。Paper Agent 必须接收 constraints.yaml (C001) 和全部 15 条写作笔记。ROC\\n    分析和 signal heatmap 作为 CPU 分析先行产出。ρ≥0.94 是验证目标非实际数值，headline 改用 effect size 表述。\\n  related_experiments:\\n  - exp_id: plan001-wikitext-15B-5seeds\\n    role: pending_validation\\n    result: running\\n  depends_on:\\n  - D028\\n  - D029\\n- id: D031\\n  date: 2026-05-15 19:55 UTC\\n  summary: 修正 D029：废弃单一 headline signal，改为分层信号策略——stable_rank+PPL 做 early warning，spectral_entropy\\n    做 severity discrimination\\n  rationale: Signal heatmap 分析揭示 spectral_entropy 是 late detector（50% 下 effect < 5%，仅\\n    100% 下显著 +25.7%），不适合做 early warning signal。stable_rank 和 perplexity 在 50% contamination\\n    即可检出（SR +564.8%, PPL +5255%）。分层策略：\\\"signals have complementary operating ranges\\\"——early\\n    warning 用 SR+PPL，severity discrimination 用 SE。这个分层发现本身强化了 Claim 3 的核心论点（no single\\n    signal suffices）。6/7 信号方向跨 QLoRA/Full FT 一致，强化 Claim 1 泛化性。\\n  related_experiments:\\n  - exp_id: plan006-effect-size\\n    role: supporting\\n    result: ranking_shift\\n  - exp_id: plan003-fullft-0.5B\\n    role: supporting\\n    result: success\\n  depends_on:\\n  - D029\\n- id: D032\\n  date: 2026-05-15 20:00 UTC\\n  summary: Claim 2 修正：within-gen early warning 去除 perplexity，仅保留 stable_rank；三维信号分层叙事确立\\n  rationale: ROC 分析（plan005）显示 perplexity within-gen AUC=0.534（近乎无效），而 stable_rank\\n    AUC=0.984（10% progress 即 AUC=0.94）。Perplexity 的强项在 cross-gen severity tracking，不在\\n    within-gen early detection。据此确立三维分层叙事：within-gen alarm (stable_rank) / cross-gen\\n    severity (perplexity) / robust discrimination (spectral_entropy)。这也使 \\\"practitioners'\\n    go-to metric fails at earliest window\\\" 成为有力论点。\\n  related_experiments:\\n  - exp_id: plan005_roc\\n    role: primary_evidence\\n    result: stable_rank AUC=0.984, perplexity AUC=0.534, spectral_entropy AUC=0.773\\n      (non-monotonic)\\n  depends_on: []\\n- id: D033\\n  date: 2026-05-15 20:07 UTC\\n  summary: Claim 2 early warning 从 \\\"3% progress\\\" 修正为 \\\"10% progress (AUC=0.94)\\\"；perplexity\\n    从 early warning 移除；training_loss 加入为 confirmation signal\\n  rationale: 两轮 Reviewer 审查（heatmap + ROC）一致表明：(1) 原 \\\"3% progress\\\" 基于 N=1 seed 小样本\\n    artifact，3-seed ROC 无法复制；(2) perplexity within-gen AUC=0.534 几乎无效，不能归入 early warning；(3)\\n    training_loss AUC=0.923 是 within-gen 第二强信号但未在 framing 讨论；(4) spectral_entropy\\n    20% progress 时 AUC=0.305 方向翻转，不适合 threshold-based 检测。三维信号分层叙事已确立：stable_rank (within-gen\\n    onset) / perplexity (cross-gen severity) / spectral_entropy (cross-seed reliability)。\\n  related_experiments:\\n  - exp_id: plan005_roc\\n    role: primary_evidence\\n    result: stable_rank AUC=0.984, training_loss AUC=0.923, spectral_entropy AUC=0.773\\n      (non-monotonic), perplexity AUC=0.534\\n  - exp_id: signal_heatmap\\n    role: supporting\\n    result: spectral_entropy frac=50% effect size <5%, confirming late-detector status\\n  depends_on: []\\n- id: D034\\n  date: 2026-05-15 20:54 UTC\\n  summary: cqa1 cuda:2 调度：方案 C——plan002-gpu2 跑完 seed42 frac=1.0 后切 plan001\\n  rationale: seed42 frac=1.0 是 PubMed 该 seed 唯一的 100% fraction 数据点，保全后 seed42 拥有 0/50/100%\\n    三档完整 cross-domain 证据。杀掉重跑成本 > 等 ~20h。plan001 关键路径不受严重影响：cuda:2 预计 ~5/16 17:00Z\\n    释放后加速 plan001 剩余 seeds，仍赶得上 5/18 整体完成。\\n  related_experiments:\\n  - exp_id: plan002-pubmed-gpu2\\n    role: 继续运行至 seed42 frac=1.0 完成\\n  - exp_id: plan001-wikitext-15B-5seeds\\n    role: cuda:2 释放后接入加速\\n  depends_on:\\n  - D016\\n- id: D035\\n  date: 2026-05-15 22:02 UTC\\n  summary: Clarify training_loss (train-set CE) vs perplexity (held-out eval PPL)\\n    as distinct signals with different data sources\\n  rationale: 'Reviewer found AUC gap (0.923 vs 0.534) between \\\"Training Loss\\\" and\\n    \\\"Perplexity\\\" inexplicable if they''re monotonic transforms. Agent code investigation\\n    confirmed: training_loss = Trainer running avg CE on training set (contains synthetic\\n    mix); perplexity = exp(NLL) on fixed held-out validation set. Different data sources\\n    → different AUCs is expected. This distinction strengthens the paper: train-set\\n    signals detect contamination effects earlier because they''re closest to the distribution\\n    shift source, while held-out signals require multi-generation accumulation. Paper\\n    must explicitly define both signals'' data sources in Method and explain the sensitivity\\n    difference in Results/Discussion.'\\n  related_experiments:\\n  - exp_id: within_gen_analysis\\n    role: source of AUC values\\n    result: training_loss AUC=0.923, perplexity AUC=0.534\\n  depends_on: []\\n- id: D036\\n  date: 2026-05-15 22:02 UTC\\n  summary: 修正 PPL 命名混淆：论文中\\\"training perplexity misleading (AUC=0.534)\\\"实际指 evaluation\\n    PPL，非 training PPL\\n  rationale: Agent 调查确认 training_loss = train-set CE (AUC=0.923)，perplexity = held-out\\n    validation PPL (AUC=0.534)。由于 training PPL = exp(training loss)，training PPL 的\\n    AUC 应 ≈0.923，不能称 misleading。paper_framing.md 写作笔记 18/19 中\\\"training perplexity\\n    provides no within-gen early warning\\\"是命名错误——失效的是 evaluation PPL。修正方向：(1) 论文中三个\\n    PPL 概念必须显式区分：train-set CE/PPL（有效检测器）、held-out eval PPL（within-gen 无效）、cross-gen\\n    eval PPL（有效 tracker）；(2) Method 正式引入 training loss 信号；(3) Claim 2 叙事从\\\"training\\n    PPL misleading\\\"改为\\\"held-out eval PPL within-gen 无效\\\"；(4) 补充讨论 training loss 为何有效（检测数据分布变化而非模型质量变化）但解读上仍需谨慎（loss\\n    下降 ≠ 模型变好）。\\n  related_experiments:\\n  - exp_id: within_gen_analysis\\n    role: evidence\\n    result: training_loss AUC=0.923, perplexity(eval) AUC=0.534\\n  - exp_id: plan006-signal-taxonomy\\n    role: evidence\\n    result: perplexity(eval) cross-gen d=20.82\\n  depends_on:\\n  - D029\\n- id: D037\\n  date: 2026-05-15 22:07 UTC\\n  summary: Results section 数据溯源失败：3 critical + 3 warning，派 Main Agent 验证数据 + 重生成图，派\\n    Paper Agent 修正文本\\n  rationale: Reviewer 发现 Results 中至少 5 个数值错误（token_entropy AUC 0.700→0.478、spectral_entropy\\n    AUC 0.750→0.773、C1/C2 配置混淆、distinct-1 矛盾）+ 2 个子结果缺失（training_loss、self-recovery）。根因是写作时硬编码数值而非从分析\\n    artifact 提取。修复策略：Main Agent 验证数据源 + 重生成 Fig 3/4；Paper Agent 全面修正文本。\\n  related_experiments:\\n  - exp_id: plan005\\n    role: within-gen ROC analysis\\n    result: correct AUC values differ from text\\n  - exp_id: plan006\\n    role: 3-seed taxonomy (C2/1.5B)\\n    result: misattributed as C1 in text\\n  - exp_id: plan008\\n    role: self-recovery analysis\\n    result: data exists but omitted from Results\\n  depends_on: []\\n- id: D038\\n  date: 2026-05-16 01:14 UTC\\n  summary: 'seed44 diversity: 保持 N=2 Cohen''s d=14.60，不使用 gen3 代理 gen4 的近似值'\\n  rationale: 'Reviewer warning: gen3≠gen4，用 gen3 代替 gen4 计算 N=3 的 d=15.18 是近似而非实际值。d=14.60\\n    (N=2) 已是极大效应量，+4% 不改变结论，但引入方法学瑕疵（用相邻 generation 值代替缺失值）会被审稿人质疑。同时 \\\"degenerate\\n    output\\\" 说法已证实错误（seed44 生成文本 distinct-1 与其他 seed 一致），需改为准确描述：summary reconstruction\\n    脚本 bug 导致 gen4 diversity 缺失。'\\n  related_experiments:\\n  - exp_id: seed44_frac50\\n    role: evidence\\n    result: diversity values normal, gen4 missing due to rebuild bug\\n  depends_on: []\\n- id: D039\\n  date: 2026-05-16 02:47 UTC\\n  summary: Paper Agent 提前至 5/16 启动 Full Draft + Agent 全面并行铺开 CPU 分析和代码预写\\n  rationale: 用户要求不浪费任何资源。GPU 全满无空闲，但 CPU 分析（plan003 对比/plan006+008 增量）和代码预写（plan004/005/007/figure\\n    脚本集）可立即并行。Paper Agent 从 5/17 提前到 5/16，先写不依赖全量数据的章节（Intro/Related Work/Methods），Results\\n    用 partial data 填框架后续 patch。\\n  related_experiments:\\n  - exp_id: plan003-fullft-05B\\n    role: input\\n    result: success\\n  - exp_id: plan006-signal-taxonomy\\n    role: input\\n    result: success\\n  - exp_id: plan008-self-recovery\\n    role: input\\n    result: success\\n  - exp_id: plan001-wikitext-15B-5seeds\\n    role: pending\\n    result: running\\n  depends_on:\\n  - D030\\n- id: D040\\n  date: 2026-05-16 02:47 UTC\\n  summary: cqa1 GPU0/GPU1 空闲后调度：GPU0→seed44 frac=1.0 加速 plan002，GPU1→PubMed frac=0.25\\n    补密 fraction；Paper Agent 提前到 5/16 启动\\n  rationale: 用户要求不浪费任何资源。GPU0 接瓶颈任务节省 ~3.5h；GPU1 启动 plan002 原计划缺失 fraction（0.25）增加\\n    PubMed severity 梯度密度。Paper Agent 用 MVP+plan003+plan006/008 preliminary 数据立即启动，先写\\n    structure/methods/related work 不依赖全量数据，比原计划 5/17 提前 1 天。\\n  related_experiments:\\n  - exp_id: plan002-pubmed-cqa1\\n    role: 加速+扩展\\n  - exp_id: plan001-wikitext-15B-5seeds\\n    role: 继续运行\\n  depends_on:\\n  - D034\\n- id: D041\\n  date: 2026-05-16 08:21 UTC\\n  summary: Claim 2 within-gen 信号排序可能 scale-dependent：准备两种叙事写法\\n  rationale: C2 (1.5B) seed42 dry-run 显示 training_loss AUROC=0.980 (best) vs stable_rank\\n    0.800，与 C1 (0.5B) 中 stable_rank=0.94 (best) 排序不同。N=1 无统计力度，需等 5-seed 确认。两种准备：(A)\\n    5-seed 确认 training_loss 在 1.5B 更强 → Claim 2 改为 scale-dependent 推荐；(B) seed42 是\\n    outlier → 保持 stable_rank 叙事。无论哪种，\\\"signal informativeness is scale-dependent\\\" 本身可强化\\n    Claim 3 taxonomy。\\n  related_experiments:\\n  - exp_id: plan_014\\n    role: pending_confirmation\\n    result: 'seed42 dry-run: training_loss>stable_rank at 1.5B'\\n  depends_on:\\n  - D033\\n\", \"total_chars\": 28583, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ae1bc184-42c4-473d-8562-b4c8ba334102",
  "isSidechain": true,
  "promptId": "80dd2a4d-c31a-43ae-8316-4a6135d9fed6",
  "agentId": "ade4d670d78b2afaf",
  "type": "user",
  "uuid": "5ddd224f-6697-4de1-b2e9-c9392787ed58",
  "sourceToolAssistantUUID": "ae1bc184-42c4-473d-8562-b4c8ba334102",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T10:42:51.588Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_013BwB99ZXuBTot5Hf779Reh`</summary>

```json
{
  "project": "collapse_severity_monitor",
  "file": "paper_checklist.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ddd224f-6697-4de1-b2e9-c9392787ed58",
  "isSidechain": true,
  "agentId": "ade4d670d78b2afaf",
  "requestId": "req_011Cb67Gpj2KSZiXdzEmbTXJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b1a75d7e-efcb-4649-85b8-e9f37868d63e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0171X1gLHaJBRMFCHStqEvaU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11879,
      "cache_read_input_tokens": 33767,
      "output_tokens": 198,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11879
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 198,
          "cache_read_input_tokens": 33767,
          "cache_creation_input_tokens": 11879,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11879,
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

_source line 22 · 2026-05-16T10:42:51.599Z_

<details><summary>↩ Tool result · `toolu_013BwB99ZXuBTot5Hf779Reh`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'collapse_severity_monitor'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b1a75d7e-efcb-4649-85b8-e9f37868d63e",
  "isSidechain": true,
  "promptId": "80dd2a4d-c31a-43ae-8316-4a6135d9fed6",
  "agentId": "ade4d670d78b2afaf",
  "type": "user",
  "uuid": "684be0b1-4cee-4a0a-9230-6e0d1cd0e302",
  "sourceToolAssistantUUID": "b1a75d7e-efcb-4649-85b8-e9f37868d63e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-16T10:42:53.920Z_

Now let me look at the actual paper draft and any related work section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "684be0b1-4cee-4a0a-9230-6e0d1cd0e302",
  "isSidechain": true,
  "agentId": "ade4d670d78b2afaf",
  "requestId": "req_011Cb67H41yVic1nFN9gkp6e",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a7e2a9e6-09f0-49e4-ae6b-f84053908fae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CiLfGh8Mw24WdciV8N3zbE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15261,
      "cache_read_input_tokens": 45646,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15261,
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

_source line 24 · 2026-05-16T10:42:58.460Z_

<details open><summary>🔧 Tool call — Glob · `toolu_011qtAiGvNVg5aE9HVDCoTJS`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7e2a9e6-09f0-49e4-ae6b-f84053908fae",
  "isSidechain": true,
  "agentId": "ade4d670d78b2afaf",
  "requestId": "req_011Cb67H41yVic1nFN9gkp6e",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cdf55299-7222-4972-b39d-4dc8fbaa1e64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CiLfGh8Mw24WdciV8N3zbE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15261,
      "cache_read_input_tokens": 45646,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15261,
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

_source line 25 · 2026-05-16T10:42:58.483Z_

<details><summary>↩ Tool result · `toolu_011qtAiGvNVg5aE9HVDCoTJS`</summary>

```text
artifacts/dream_reports/dream_20260514T204316/best/paper.tex
artifacts/dream_reports/dream_20260514T204316/median/paper.tex
artifacts/dream_reports/dream_20260514T204316/worst/paper.tex
artifacts/_project/paper/method.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/experiments.tex
docs/paper/method.tex
docs/paper/discussion.tex
docs/paper/results.tex
artifacts/_project/paper/introduction_ce5ca8.tex
docs/paper/conclusion.tex
docs/paper/limitations.tex
docs/paper/abstract.tex
docs/paper/related_work.tex
paper/main.tex
paper/tables/competitor_comparison.tex
paper/sections/appendix.tex
paper/sections/related_work.tex
paper/sections/method.tex
paper/sections/abstract.tex
docs/paper/introduction.tex
paper/sections/limitations.tex
paper/sections/conclusion.tex
paper/sections/discussion.tex
paper/sections/experiments.tex
paper/sections/introduction.tex
artifacts/dream_reports/dream_20260516T095632/best/paper.tex
artifacts/dream_reports/dream_20260516T095632/median/paper.tex
artifacts/dream_reports/dream_20260516T095632/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cdf55299-7222-4972-b39d-4dc8fbaa1e64",
  "isSidechain": true,
  "promptId": "80dd2a4d-c31a-43ae-8316-4a6135d9fed6",
  "agentId": "ade4d670d78b2afaf",
  "type": "user",
  "uuid": "5ecbb657-ceaa-4920-91cb-ceb6cd42fb48",
  "sourceToolAssistantUUID": "cdf55299-7222-4972-b39d-4dc8fbaa1e64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-16T10:42:58.693Z_

<details open><summary>🔧 Tool call — Glob · `toolu_0116K19ftq5wTUYipt3Xf3LH`</summary>

```json
{
  "pattern": "**/paper/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ecbb657-ceaa-4920-91cb-ceb6cd42fb48",
  "isSidechain": true,
  "agentId": "ade4d670d78b2afaf",
  "requestId": "req_011Cb67H41yVic1nFN9gkp6e",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "48714642-220c-42db-9dc8-6a9e9ff3d604",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CiLfGh8Mw24WdciV8N3zbE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15261,
      "cache_read_input_tokens": 45646,
      "output_tokens": 194,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15261
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 194,
          "cache_read_input_tokens": 45646,
          "cache_creation_input_tokens": 15261,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15261,
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

_source line 27 · 2026-05-16T10:42:58.714Z_

<details><summary>↩ Tool result · `toolu_0116K19ftq5wTUYipt3Xf3LH`</summary>

```text
artifacts/_project/paper/references.bib
artifacts/_project/paper/annotated_bibliography.md
artifacts/_project/paper/method.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/experiments.tex
paper/scripts/plot_signal_severity.py
paper/scripts/plot_early_warning.py
paper/figures/fig_signal_severity.pdf
paper/figures/fig_signal_severity.png
paper/figures/fig_early_warning.pdf
paper/figures/fig_early_warning.png
paper/scripts/plot_per_layer_heatmap.py
paper/figures/fig_per_layer_heatmap.pdf
paper/figures/fig_per_layer_heatmap.png
paper/acl.sty
paper/acl_natbib.bst
docs/paper/method.tex
figures/paper/roc_curves_data.json
figures/paper/comparison_data.json
figures/paper/gen_fig5.py
docs/paper/discussion.tex
docs/paper/results.tex
artifacts/_project/paper/introduction_ce5ca8.tex
figures/paper/fig5_method_comparison.pdf
figures/paper/fig5_method_comparison.png
docs/paper/conclusion.tex
docs/paper/limitations.tex
docs/paper/abstract.tex
paper/_pdf_images/main_p8.png
paper/_pdf_images/main_p9.png
paper/_pdf_images/main_p10.png
paper/references.bib
figures/paper/gen_fig3_roc_curves.py
figures/paper/fig3_roc_curves.pdf
figures/paper/fig3_roc_curves.png
figures/paper/gen_fig4_signal_heatmap.py
figures/paper/fig4_signal_heatmap.pdf
figures/paper/fig4_signal_heatmap.png
figures/paper/fig2_severity_curves.py
figures/paper/fig2_severity_curves.pdf
figures/paper/fig2_severity_curves.png
figures/paper/gen_fig1_framework.py
figures/paper/fig1_framework.pdf
figures/paper/fig1_framework.png
docs/paper/related_work.tex
paper/main.tex
paper/tables/competitor_comparison.tex
paper/sections/appendix.tex
paper/sections/related_work.tex
paper/sections/method.tex
paper/sections/abstract.tex
docs/paper/introduction.tex
paper/sections/limitations.tex
paper/main.fls
paper/main.fdb_latexmk
paper/main.blg
paper/main.bbl
paper/main.aux
paper/main.out
paper/main.log
paper/main.pdf
paper/sections/conclusion.tex
paper/sections/discussion.tex
paper/sections/experiments.tex
paper/sections/introduction.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "48714642-220c-42db-9dc8-6a9e9ff3d604",
  "isSidechain": true,
  "promptId": "80dd2a4d-c31a-43ae-8316-4a6135d9fed6",
  "agentId": "ade4d670d78b2afaf",
  "type": "user",
  "uuid": "c8e4a215-e44d-4923-b7a6-716a12e977a3",
  "sourceToolAssistantUUID": "48714642-220c-42db-9dc8-6a9e9ff3d604",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-16T10:43:01.779Z_

<details open><summary>🔧 Tool call — Read · `toolu_01F1PwXYMtxR7CrxXZViASGp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8e4a215-e44d-4923-b7a6-716a12e977a3",
  "isSidechain": true,
  "agentId": "ade4d670d78b2afaf",
  "requestId": "req_011Cb67HaRKogg2g2gRUuzH2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a071a2cd-248d-41a9-810f-8fdc0ba92356",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019qf27AuHYPYjbwu56XX9DF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1275,
      "cache_read_input_tokens": 60907,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1275,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 29 · 2026-05-16T10:43:01.786Z_

<details><summary>↩ Tool result · `toolu_01F1PwXYMtxR7CrxXZViASGp`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Model collapse in iterative training.}
5	Model collapse---progressive degradation when models train on their own outputs---has been established across generative families~\citep{Shumailov2024,Alemohammad2024}.
6	Theoretical analyses show that even trace synthetic contamination induces collapse~\citep{Dohmatob2025}, with errors compounding across iterations~\citep{Dohmatob2024_tails,Fu2024_icml}, altered scaling laws~\citep{Seddik2024}, and entropy-driven memorization transitions~\citep{Shi2025_neurips}.
7	\citet{Schaeffer2025} catalogued eight distinct collapse definitions, motivating precise operationalization.
8	Mitigation strategies include data accumulation~\citep{Gerstgrasser2024,Kazdan2024}, loss modification~\citep{Zibakhsh2025}, verification-based filtering~\citep{Feng2025,Yi2025}, and correction functions~\citep{Gillman2024,Bakshi2026}.
9	These works establish \emph{that} collapse occurs and \emph{how} to mitigate it, but rely on post-hoc evaluation; none provides real-time training-time monitoring.
10	
11	\paragraph{Spectral and training-dynamic diagnostics.}
12	Spectral properties of weight matrices predict model quality without test data~\citep{Martin2021}, with stable rank linked to generalization~\citep{Sanyal2020} and shown to be scale-dependent~\citep{Jha2025}.
13	Recent work has characterized spectral dynamics across training~\citep{Liu2026_lifecycle,Staats2024,Pennington2017}, used spectral signals for compression and pruning~\citep{Xu2026,AlphaPruning2024,Yunis2024}, and applied gradient-based diagnostics~\citep{Li2025_gradient,Elgaar2026}, diffusion spectral entropy~\citep{Chen2024_dse}, spectral alignment~\citep{Qiu2025}, and loss landscape curvature~\citep{Kalra2026} to training health monitoring.
14	
15	\paragraph{Closest concurrent work.}
16	SIGMA~\citep{Gu2026} analyzes the output embedding Gram matrix spectrum to quantify collapse but operates post-hoc, requires a clean reference distribution, and has not been validated in iterative settings.
17	\citet{Kalinowski2026} proposes an online topological monitor via persistent homology but uses a different signal family and incurs higher computational cost (Table~\ref{tab:competitor_comparison} in Appendix~\ref{app:competitor_comparison}).
18	Neither provides a cross-family comparison, documents where signals saturate or mislead, or establishes within-generation early warning thresholds.
19	
20	\paragraph{Data quality and contamination detection.}
21	Watermarking~\citep{Kirchenbauer2023,Dathathri2024,Sander2024} and statistical detection~\citep{Mitchell2023,Shi2024_mink} identify synthetic data presence, while dataset-level approaches address quality filtering~\citep{Penedo2024,Zhang2026} and diversity quantification~\citep{Gambetta2024,Wang2025_scaling}.
22	These methods answer whether synthetic data is \emph{present}; our work addresses how severely it has \emph{degraded} the model, operating in real time during training rather than post-hoc.
23	Across the literature, no prior work simultaneously achieves online monitoring, spectral/entropic training-dynamic signals, and validation in the iterative synthetic data setting.
24	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a071a2cd-248d-41a9-810f-8fdc0ba92356",
  "isSidechain": true,
  "promptId": "80dd2a4d-c31a-43ae-8316-4a6135d9fed6",
  "agentId": "ade4d670d78b2afaf",
  "type": "user",
  "uuid": "cf7de797-5060-4f55-8676-6b9cc9fbe783",
  "sourceToolAssistantUUID": "a071a2cd-248d-41a9-810f-8fdc0ba92356",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-16T10:43:02.265Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Xa8P5hHVGtQDEuTnGp4iuo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf7de797-5060-4f55-8676-6b9cc9fbe783",
  "isSidechain": true,
  "agentId": "ade4d670d78b2afaf",
  "requestId": "req_011Cb67HaRKogg2g2gRUuzH2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f460cc24-9d19-4902-b9f9-1a838c1d35e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019qf27AuHYPYjbwu56XX9DF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1275,
      "cache_read_input_tokens": 60907,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1275,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 31 · 2026-05-16T10:43:02.270Z_

<details><summary>↩ Tool result · `toolu_01Xa8P5hHVGtQDEuTnGp4iuo`</summary>

```text
1	% Abstract — collapse_severity_monitor
2	% Data sources: plan006 (3-seed Cohen's d), within_gen_analysis, plan003-fullft-05B
3	
4	\begin{abstract}
5	Iterative training on model-generated data causes model collapse---progressive loss of distribution tails, contraction of output diversity, and degradation of acquired knowledge---yet the metrics practitioners most commonly watch during training fail to detect it.
6	We systematically evaluate five families of training-time signals---spectral (stable rank, spectral entropy), output (train loss, evaluation perplexity, token entropy), diversity (distinct-$n$, self-BLEU), gradient (L2 norm), and downstream (HellaSwag accuracy)---as collapse severity monitors across three experimental configurations spanning two model scales (0.5B, 1.5B), two fine-tuning methods (QLoRA, full fine-tuning), and six contamination fractions ($\alpha \in \{0, 0.1, 0.25, 0.5, 0.75, 1.0\}$) on WikiText-2.
7	We find that different signal families have complementary operating ranges.
8	Spectral entropy achieves the largest cross-generation effect size (Cohen's $d = 33.48$, $\mathrm{CV} = 0.0015$ across seeds), while stable rank provides the strongest within-generation early warning ($\mathrm{AUROC} = 0.94$ at 10\% training progress, $0.984$ pooled, 34.4\% deviation at 3\% of training).
9	Held-out evaluation perplexity provides no within-generation early warning (pooled $\mathrm{AUROC} = 0.533$, indistinguishable from random), while train loss is an effective but interpretively ambiguous detector (pooled $\mathrm{AUROC} = 0.923$): its decrease reflects successful fitting of corrupted data, not improved model quality.
10	The same signal can be informative under one training method and misleading under another: gradient norm is non-monotonic under QLoRA but monotonic under full fine-tuning.
11	These findings yield a three-tier monitoring strategy---stable rank for within-generation alarms, evaluation perplexity for cross-generation tracking, spectral entropy for severity discrimination---and a signal taxonomy characterizing where each family succeeds, saturates, or misleads.
12	\end{abstract}
13	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f460cc24-9d19-4902-b9f9-1a838c1d35e7",
  "isSidechain": true,
  "promptId": "80dd2a4d-c31a-43ae-8316-4a6135d9fed6",
  "agentId": "ade4d670d78b2afaf",
  "type": "user",
  "uuid": "0090e10e-c019-4f7e-b110-6b7e6edca0bf",
  "sourceToolAssistantUUID": "f460cc24-9d19-4902-b9f9-1a838c1d35e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-16T10:43:02.688Z_

<details open><summary>🔧 Tool call — Read · `toolu_0172orh3sJvDJ6MvZkdfno7G`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0090e10e-c019-4f7e-b110-6b7e6edca0bf",
  "isSidechain": true,
  "agentId": "ade4d670d78b2afaf",
  "requestId": "req_011Cb67HaRKogg2g2gRUuzH2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b8196f84-1850-443b-a5ba-80342378e8a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019qf27AuHYPYjbwu56XX9DF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1275,
      "cache_read_input_tokens": 60907,
      "output_tokens": 229,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1275
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 229,
          "cache_read_input_tokens": 60907,
          "cache_creation_input_tokens": 1275,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1275,
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

_source line 33 · 2026-05-16T10:43:02.697Z_

<details><summary>↩ Tool result · `toolu_0172orh3sJvDJ6MvZkdfno7G`</summary>

```text
1	% Introduction — collapse_severity_monitor
2	% Data sources: plan006 (3-seed Cohen's d), within_gen_analysis, plan003-fullft-05B
3	
4	\section{Introduction}
5	\label{sec:introduction}
6	
7	As LLM-generated text pervades web-scraped training corpora, practitioners increasingly fine-tune models on data shaped by prior model generations.
8	This recursive dynamic creates self-consuming loops that cause \emph{model collapse}---progressive loss of distribution tails, contraction of output diversity, and degradation of acquired knowledge~\citep{Shumailov2024,Alemohammad2024}.
9	The problem compounds: even trace synthetic contamination induces collapse at sufficient depth~\citep{Dohmatob2025}, with errors accumulating across iterations at accelerating rates~\citep{Dohmatob2024_tails,Fu2024_icml}.
10	Yet the metric practitioners most commonly rely on for quality assessment---held-out evaluation perplexity---fails to detect this degradation within a run, achieving pooled $\mathrm{AUROC} = 0.533$ for within-generation collapse detection (indistinguishable from random chance).
11	Train loss does change under collapse (pooled $\mathrm{AUROC} = 0.923$), but its decrease is interpretively ambiguous: the model fits lower-entropy synthetic data more easily, which looks like healthy convergence.
12	A practitioner watching only perplexity or interpreting train loss at face value would have no reliable warning that collapse is underway.
13	
14	Existing work addresses model collapse from two directions.
15	On the theoretical side, \citet{Shumailov2024} established the phenomenon, \citet{Dohmatob2025} proved that any nonzero synthetic fraction eventually induces strong collapse, and \citet{Dohmatob2024_tails} showed that collapse alters neural scaling laws.
16	On the mitigation side, data accumulation~\citep{Gerstgrasser2024}, loss modification~\citep{Zibakhsh2025}, and verification-based filtering~\citep{Feng2025} each reduce collapse pressure under specific conditions.
17	Missing from this landscape is a systematic analysis of which \emph{training-time signals} best track collapse severity, when they provide early warning, and where they saturate or actively mislead.
18	\citet{Schaeffer2025} highlight that even the definition of collapse varies across studies, further motivating signal-level analysis grounded in controlled experiments.
19	The two closest concurrent works---SIGMA~\citep{Gu2026}, which monitors output embedding spectra, and the topological index of \citet{Kalinowski2026}---each address part of this gap but carry limitations: SIGMA requires a clean reference distribution and operates post-hoc; topological monitoring incurs higher computational cost.
20	Neither provides a cross-family comparison of signal operating ranges or quantitative within-generation early warning thresholds.
21	
22	We conduct a systematic empirical study of training-time signals as collapse severity monitors.
23	We evaluate five signal families---spectral (stable rank, spectral entropy), output (train loss, evaluation perplexity, token entropy), diversity (distinct-$n$, self-BLEU), gradient (L2 norm), and downstream (HellaSwag accuracy)---across three experimental configurations spanning two model scales (0.5B, 1.5B), two fine-tuning methods (QLoRA and full fine-tuning), and six contamination fractions ($\alpha \in \{0, 0.1, 0.25, 0.5, 0.75, 1.0\}$) on WikiText-2 (Figure~\ref{fig:framework}).
24	Our central finding is that different signal families have complementary operating ranges, and the same signal's utility can flip from informative to misleading depending on the training method.
25	
26	Our contributions:
27	
28	\begin{enumerate}
29	    \item \textbf{Signal--severity correlation.}
30	    Spectral and output signals track collapse across contamination levels.
31	    Spectral entropy achieves the largest effect size (Cohen's $d = 33.48$, coefficient of variation $\mathrm{CV} = 0.0015$ across seeds), followed by evaluation perplexity ($d = 20.82$) and stable rank ($d = 9.43$, $\mathrm{CV} = 0.022$).
32	    Validated across QLoRA and full fine-tuning, ten of eleven monitored signals maintain consistent direction of change.
33	    The exception---gradient norm, which is non-monotonic under QLoRA but monotonic under full fine-tuning---demonstrates that method-dependence is a first-order concern for monitoring pipeline design.
34	
35	    \item \textbf{Within-generation early warning and negative results.}
36	    Stable rank achieves $\mathrm{AUROC} = 0.94$ at 10\% training progress ($0.984$ pooled) for binary collapse detection at 0.5B, with 34.4\% deviation from baseline at 3\% of training.
37	    At 1.5B, training loss becomes the dominant within-generation signal ($\mathrm{AUROC} = \mathrm{[TBD]}$ pooled), with optimal signal selection depending on model scale.
38	    Train loss at 0.5B is interpretively ambiguous (pooled $\mathrm{AUROC} = 0.923$): its decrease reflects successful fitting of corrupted data rather than improved model quality, and its AUROC starts below chance.
39	    Held-out evaluation perplexity achieves pooled $\mathrm{AUROC} = 0.533$ for within-generation detection---the most commonly relied-upon quality metric fails at the most actionable task.
40	    Evaluation perplexity's failure has a structural explanation: it accumulates degradation through the iterative contamination loop, not within a single generation's training.
41	
42	    \item \textbf{Signal taxonomy with method-dependent operating ranges.}
43	    The same signal can be informative under one training method and misleading under another.
44	    Gradient norm is non-monotonic under QLoRA but monotonic under full fine-tuning.
45	    HellaSwag accuracy tracks collapse under full fine-tuning ($-12.5\%$) but remains stable under QLoRA ($<3\%$ relative change), attributable to the training method rather than model scale.
46	    Surface-level diversity metrics do not reliably indicate collapse: distinct-1 changes by only $3\%$ under full fine-tuning even as perplexity increases $17\times$.
47	    Both methods exhibit large generation-1 perplexity jumps ($15.3\times$ and $8.7\times$), but full fine-tuning saturates (terminal perplexity $326$) while QLoRA continues to degrade ($839$); despite higher perplexity, QLoRA retains better downstream accuracy, demonstrating that perplexity can overestimate collapse severity under parameter-efficient fine-tuning.
48	    These findings motivate a three-tier monitoring recommendation: stable rank for within-generation alarms, evaluation perplexity for cross-generation severity tracking, and spectral entropy for robust severity discrimination.
49	\end{enumerate}
50	
51	Section~\ref{sec:related_work} surveys collapse theory, spectral analysis of neural networks, and concurrent monitoring approaches.
52	Section~\ref{sec:method} details our iterative contamination protocol, signal definitions, and evaluation framework.
53	Section~\ref{sec:results} presents signal--severity correlations, within-generation early warning analysis, and the method-dependent signal taxonomy.
54	Section~\ref{sec:discussion} discusses practical monitoring recommendations and limitations.
55	Section~\ref{sec:conclusion} concludes.
56	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b8196f84-1850-443b-a5ba-80342378e8a8",
  "isSidechain": true,
  "promptId": "80dd2a4d-c31a-43ae-8316-4a6135d9fed6",
  "agentId": "ade4d670d78b2afaf",
  "type": "user",
  "uuid": "5d1286e2-1378-486f-945b-84bbfc90f1d8",
  "sourceToolAssistantUUID": "b8196f84-1850-443b-a5ba-80342378e8a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-16T10:43:06.435Z_

<details open><summary>🔧 Tool call — Read · `toolu_018nQQPsVak2XsHwwqRsfFdm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d1286e2-1378-486f-945b-84bbfc90f1d8",
  "isSidechain": true,
  "agentId": "ade4d670d78b2afaf",
  "requestId": "req_011Cb67Hsff3KRaMexa59w4B",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e109f0e4-c61f-4203-acfb-09ae4e0c52ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CPX5Gd8z5rExKLiYN4UYz3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3745,
      "cache_read_input_tokens": 62182,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3745,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 35 · 2026-05-16T10:43:06.441Z_

<details><summary>↩ Tool result · `toolu_018nQQPsVak2XsHwwqRsfFdm`</summary>

```text
1	% Results section — collapse_severity_monitor
2	% Data sources: plan006 (3-seed Cohen's d), within_gen_analysis, plan003-fullft-05B, heatmap_data.json
3	
4	\section{Results}
5	\label{sec:results}
6	
7	We organize results around three claims.
8	Section~\ref{sec:correlation} establishes that spectral and output signals track collapse severity across configurations.
9	Section~\ref{sec:early_warning_results} shows that certain signals detect collapse within a single training run before evaluation perplexity diverges.
10	Section~\ref{sec:taxonomy} reveals that signal informativeness depends on the fine-tuning method, motivating a taxonomy of method-dependent operating ranges.
11	
12	\subsection{Signal--Severity Correlation}
13	\label{sec:correlation}
14	
15	We quantify signal sensitivity using Cohen's $d$ between the clean baseline ($\alpha = 0$) and full contamination ($\alpha = 1.0$) at generation~4, computed across three seeds from the C2 configuration (Qwen2.5-1.5B, WikiText-2; interim 3 of 5 planned seeds; Table~\ref{tab:configs}).
16	Effect sizes, rather than rank correlations, serve as the primary evidence because they convey the magnitude of signal separation, not just its ordering.
17	
18	\paragraph{Effect sizes.}
19	Spectral entropy achieves the largest and most reproducible effect size ($d = 33.48$, coefficient of variation across seeds $\mathrm{CV} = 0.0015$), followed by evaluation perplexity ($d = 20.82$), distinct-1 ($d = 14.60$, effective $N=2$ seeds; one seed excluded due to missing diversity computation in summary reconstruction), and stable rank ($d = 9.43$, $\mathrm{CV} = 0.022$).
20	Distinct-1's large endpoint separation coexists with non-monotonic intermediate behavior at 0.5B (Section~\ref{sec:taxonomy}).
21	Distinct-2 ($d = 7.59$) and distinct-3 ($d = -7.08$; negative because collapse increases trigram repetition) provide moderate separation.
22	Token entropy, self-BLEU, gradient norm, and HellaSwag accuracy yield small effect sizes ($d < 5$), placing them in a second tier for cross-generation severity discrimination (Figure~\ref{fig:severity_curves}).
23	
24	Stable rank is seed-sensitive: adding a third seed changed $d$ from $61.7$ to $9.43$ (rank 1st $\to$ 4th); its $\mathrm{CV} = 0.022$ is an order of magnitude above spectral entropy's $0.0015$.
25	We rely on bootstrap confidence intervals, as $N = 3$ is insufficient for rank-based tests.
26	
27	
28	\paragraph{Cross-method consistency.}
29	Ten of eleven monitored signals maintain consistent direction of change under both QLoRA and full fine-tuning (Figure~\ref{fig:signal_heatmap}): the sole exception is gradient norm, which exhibits non-monotonic behavior under QLoRA but monotonic decrease under full fine-tuning (Section~\ref{sec:taxonomy}).
30	
31	
32	\subsection{Within-Generation Early Warning}
33	\label{sec:early_warning_results}
34	
35	Cross-generation tracking (Section~\ref{sec:correlation}) requires completing multiple generations to assess severity.
36	A more actionable capability is detecting collapse \emph{within} a single training run, enabling early stopping before degradation accumulates.
37	We evaluate this using the relative deviation $\Delta_s$ (Eq.~\ref{eq:deviation}) and AUROC for binary collapse detection at each checkpoint.
38	
39	\paragraph{Stable rank as early alarm.}
40	Stable rank achieves $\mathrm{AUROC} = 0.94$ at 10\% training progress for distinguishing $\alpha = 1.0$ from $\alpha = 0$, reaching $0.984$ over the full run (Figure~\ref{fig:roc_curves}; Table~\ref{tab:within_gen_roc}).
41	At step~50 (3\% of training), $\Delta_\mathrm{SR} = 34.4\%$---far exceeding the 5\% detection threshold defined in Section~\ref{sec:evaluation}.
42	Stable rank's within-generation sensitivity reflects the structural nature of spectral signals: contamination alters the covariance eigenspectrum before output-level metrics respond, because energy dispersal across representation dimensions (Eq.~\ref{eq:stable_rank}) is detectable even when the model's token-level predictions have not yet degraded.
43	
44	
45	\paragraph{Spectral and token entropy.}
46	Token entropy deviates 24.5\% at step~50 but achieves only $\mathrm{AUROC} = 0.478$ (pooled)---near random chance, indicating that despite its large initial deviation, token entropy provides no reliable within-generation discrimination.
47	Spectral entropy achieves pooled $\mathrm{AUROC} = 0.773$, providing moderate within-generation discrimination but still substantially below stable rank's pooled $0.984$.
48	
49	\paragraph{Train loss: effective but interpretively ambiguous.}
50	Train loss achieves $\mathrm{AUROC} = 0.923$ at training completion, the second-strongest within-generation signal after stable rank.
51	However, its AUROC trajectory reveals early-training direction reversal (Figure~\ref{fig:roc_curves}b): $\mathrm{AUROC} = 0.24$ at 10\% progress, rising to $0.48$ at 20\%, $0.85$ at 50\%, and $0.923$ at completion.
52	The low early AUROC (${<}\,0.5$) indicates that the collapsing run's training loss is initially \emph{lower} than the clean baseline---the model fits the lower-entropy synthetic distribution more easily, a direct manifestation of the collapse mechanism.
53	As training progresses, cumulative degradation raises loss in the collapsed run, gradually restoring discriminability.
54	Train loss is therefore unreliable as an early collapse alarm (AUROC below chance for the first ${\sim}20\%$ of training), but effective at completion.
55	Practitioners should cross-validate with spectral indicators such as stable rank, which achieves $\mathrm{AUROC} = 0.94$ from 10\% progress onward.
56	
57	\paragraph{Scale-dependent signal dominance.}
58	At 1.5B scale (C2, $N = \mathrm{[TBD]}$ seeds), training loss emerges as the strongest within-generation indicator ($\mathrm{AUROC} = \mathrm{[TBD]}$ at 10\% progress, $\mathrm{[TBD]}$ pooled), contrasting with the 0.5B result where stable rank dominates.
59	The direction reversal that undermines train loss at 0.5B (AUROC $< 0.5$ for the first ${\sim}20\%$) is attenuated at 1.5B: the larger model's slower convergence on contaminated data preserves discriminability from early training.
60	Stable rank remains effective at 1.5B ($\mathrm{AUROC} = \mathrm{[TBD]}$ pooled) but no longer holds the top rank.
61	This scale-dependent shift implies that the optimal within-generation alarm depends on model capacity, motivating scale-conditional monitoring recommendations (Section~\ref{sec:taxonomy}).
62	
63	\paragraph{Evaluation perplexity: no within-generation signal.}
64	Held-out evaluation perplexity achieves only $\mathrm{AUROC} = 0.533$---indistinguishable from random.
65	The failure is structural: within a single generation the model trains on a fixed corpus $\mathcal{D}_g$ and has not yet produced synthetic data for $\mathcal{D}_{g+1}$ (Eq.~\ref{eq:mixing}); perplexity accumulates degradation across the iterative loop, not within a single run.
66	This yields a three-level hierarchy (all pooled AUROC): stable rank ($0.984$) detects representation-space structural change, train loss ($0.923$) detects training distribution change, and evaluation perplexity ($0.533$) measures generalization quality that does not diverge within one generation.
67	
68	
69	
70	\subsection{Signal Taxonomy: Method-Dependent Operating Ranges}
71	\label{sec:taxonomy}
72	
73	The cross-method comparison (C1 vs C4; Table~\ref{tab:configs}) reveals that the same signal can be informative under one training method and misleading under another.
74	
75	\paragraph{Gradient norm: method-dependent.}
76	Under QLoRA, gradient norm changes non-monotonically with contamination: $+5.9\%$ at $\alpha = 0.5$ relative to baseline, then $-30.8\%$ at $\alpha = 1.0$.
77	Under full fine-tuning, gradient norm decreases monotonically ($-58.3\%$ at $\alpha = 1.0$), consistent with the model converging more easily to lower-entropy synthetic data.
78	The QLoRA non-monotonicity likely arises from the interaction between contaminated gradients and the rank-$r$ adapter subspace~\citep{hu2022lora}: at moderate contamination, gradients from mixed real/synthetic data create conflicting update directions within the low-rank projection, inflating the norm; at full contamination, the uniform synthetic signal reduces this conflict~\citep{dettmers2023qlora}.
79	This method-dependence means gradient norm cannot be used as a collapse indicator without knowing the training configuration (Figure~\ref{fig:signal_heatmap}).
80	
81	\paragraph{Downstream and diversity metrics: insensitive at 0.5B.}
82	HellaSwag accuracy is insensitive under QLoRA (relative change $-1.15\%$; $N=1$ seed at 0.5B, no effect size computable).
83	Under full fine-tuning, the $\alpha = 0$ baseline is unavailable, preventing direct effect size computation; the available data show accuracy of $0.397$ ($\alpha = 0.5$) and $0.372$ ($\alpha = 1.0$), a $-6.3\%$ relative change between these two conditions.
84	
85	Distinct-1 is non-monotonic under QLoRA: $+17.7\%$ at $\alpha = 0.5$ but $-12.5\%$ at $\alpha = 1.0$, reversing direction between moderate and full contamination.
86	Self-BLEU is insensitive to collapse even when evaluation perplexity increases $17\times$ (generation~4, $\alpha = 1.0$, C4).
87	This disconnect arises because nucleus sampling ($p = 0.95$) draws from the distribution tail, producing superficially diverse surface forms even as the model's probability mass concentrates on fewer modes.
88	Token entropy captures this concentration (Section~\ref{sec:correlation}), but $n$-gram diversity metrics do not.
89	Monitoring pipelines that rely solely on output diversity metrics risk missing collapse entirely.
90	
91	\paragraph{Full fine-tuning collapse dynamics.}
92	Full fine-tuning produces sharper onset but lower terminal severity than QLoRA (Figure~\ref{fig:method_comparison}).
93	The generation~0 to generation~1 evaluation perplexity ratio is $15.3\times$ under full FT versus $8.7\times$ under QLoRA.
94	Post-onset, the trajectory is non-monotonic: evaluation perplexity \emph{decreases} from $294.0$ at generation~1 to $288.5$ at generation~2 before rising through generations~3--4 to a terminal value of $326.19$.
95	This generation~2 dip echoes the partial recovery observed at moderate contamination (below), suggesting that full parameter access allows transient re-adaptation even under full synthetic pressure.
96	The overall generation~1 to generation~4 ratio remains $1.11\times$, compared to continued monotonic growth under QLoRA, and terminal severity is lower: $\mathrm{PPL}_\text{eval} = 326.19$ versus QLoRA's $839.2$ ($0.39\times$).
97	This pattern---fast onset, partial dip, then resumed rise at lower terminal severity---is consistent with full parameter access enabling rapid adaptation to synthetic data characteristics.
98	
99	\paragraph{Partial recovery at moderate contamination.}
100	At $\alpha = 0.5$, output signals recover approximately 52\% of the generation-1 severity spike relative to the $\alpha = 1.0$ trajectory, and representation-space signals approximately 33\%, consistent with data accumulation effects~\citep{Gerstgrasser2024}.
101	
102	\paragraph{Recommended operating ranges.}
103	Based on the evidence above, we propose signal-to-task assignments (Table~\ref{tab:signal_taxonomy}):
104	\begin{itemize}[nosep]
105	    \item \textbf{Within-generation alarm (scale-conditional):} stable rank at ${\leq}1$B ($\mathrm{AUROC} = 0.984$ pooled; train loss unreliable early); training loss at ${\geq}1.5$B ($\mathrm{AUROC} = \mathrm{[TBD]}$ pooled; no early reversal). Monitor both when scale is uncertain.
106	    \item \textbf{Cross-generation severity discrimination:} spectral entropy ($d = 33.48$, $\mathrm{CV} = 0.0015$).
107	    \item \textbf{Cross-generation tracking:} evaluation perplexity (large absolute effect, interpretable scale).
108	    \item \textbf{Method-dependent:} gradient norm (monotonic under full FT only).
109	    \item \textbf{Non-monotonic:} distinct-1 ($+17.7\%$ at $\alpha{=}0.5$, $-12.5\%$ at $\alpha{=}1.0$ under QLoRA).
110	    \item \textbf{Insensitive at 0.5B scale:} HellaSwag accuracy (relative change ${<}3\%$, $N{=}1$).
111	\end{itemize}
112	
113	\noindent
114	Effect sizes are from C2 (1.5B, $N{=}3$ seeds); AUROC from C1 (0.5B, $N{=}1$); method comparisons from C1 vs C4.
115	Preliminary 3B baselines (C5, $\alpha{=}0$) confirm signal stability ($<3\%$ variation); severity validation at 3B and additional domains is ongoing.
116	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e109f0e4-c61f-4203-acfb-09ae4e0c52ad",
  "isSidechain": true,
  "promptId": "80dd2a4d-c31a-43ae-8316-4a6135d9fed6",
  "agentId": "ade4d670d78b2afaf",
  "type": "user",
  "uuid": "92b6eb5b-e801-49f2-8b20-f705e5a36a70",
  "sourceToolAssistantUUID": "e109f0e4-c61f-4203-acfb-09ae4e0c52ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-16T10:43:06.991Z_

<details open><summary>🔧 Tool call — Read · `toolu_011R9seiVcnptJxgkdasSWkH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92b6eb5b-e801-49f2-8b20-f705e5a36a70",
  "isSidechain": true,
  "agentId": "ade4d670d78b2afaf",
  "requestId": "req_011Cb67Hsff3KRaMexa59w4B",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b026817f-834d-4c6e-bcf6-2c1b8e253f13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CPX5Gd8z5rExKLiYN4UYz3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3745,
      "cache_read_input_tokens": 62182,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3745,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 37 · 2026-05-16T10:43:07.012Z_

<details><summary>↩ Tool result · `toolu_011R9seiVcnptJxgkdasSWkH`</summary>

```text
1	% Method section — collapse_severity_monitor
2	
3	\section{Methodology}
4	\label{sec:method}
5	
6	We design a controlled framework to evaluate how training-time signals track model collapse severity under iterative synthetic data contamination.
7	Our protocol varies contamination level and generational depth while monitoring four families of signals across three primary experimental configurations (with two additional configurations for ongoing cross-domain and scale validation).
8	
9	\subsection{Iterative Training Protocol}
10	\label{sec:protocol}
11	
12	We simulate iterative model collapse through a multi-generation fine-tuning loop.
13	Let $M_0$ denote a pretrained base model and $\mathcal{D}_\text{real}$ a corpus of real text.
14	At each generation $g \in \{0, 1, \ldots, G{-}1\}$ (with $G=5$), we execute three steps:
15	
16	\begin{enumerate}
17	    \item \textbf{Fine-tune.} Initialize from $M_0$ and fine-tune on the current training corpus $\mathcal{D}_g$, yielding model $\tilde{M}_g$. During training, we collect monitoring signals every 50 optimizer steps via a callback on a held-out validation set (Section~\ref{sec:signals}).
18	    \item \textbf{Generate.} Sample synthetic text $\mathcal{S}_g$ from $\tilde{M}_g$ by prompting with the first 32 tokens of randomly subsampled chunks from $\mathcal{D}_\text{real}$ and generating up to 480 new tokens with nucleus sampling ($p=0.95$, temperature $\tau=1.0$). We subsample 1{,}500 chunks for generation.
19	    \item \textbf{Mix.} Construct the next-generation corpus by replacing fraction $\alpha$ of real chunks with synthetic chunks:
20	    \begin{equation}
21	        \mathcal{D}_{g+1} = (1 - \alpha)\,\mathcal{D}_\text{real} \cup \alpha\,\mathcal{S}_g.
22	        \label{eq:mixing}
23	    \end{equation}
24	    When the number of synthetic chunks is fewer than $|\mathcal{D}_\text{real}|$, we upsample with replacement to maintain a fixed training set size of $|\mathcal{D}_\text{real}|$ across all configurations.
25	\end{enumerate}
26	
27	\noindent
28	Each generation initializes from the \emph{same} pretrained weights $M_0$, isolating the effect of data contamination from cumulative weight drift.
29	Collapse pressure enters solely through the training corpus: at generation $g$, the synthetic component was produced by a model trained on data that itself contained synthetic text from generation $g{-}1$.
30	
31	All fine-tuning runs use AdamW with learning rate $2 \times 10^{-4}$, weight decay $0.01$, linear warmup over $5\%$ of steps, and gradient clipping at $\|\cdot\|_2 \leq 1.0$.
32	We train for 5 epochs with effective batch size 16 (per-device batch 4, gradient accumulation 4) in \texttt{bf16} mixed precision.
33	QLoRA configurations~\citep{dettmers2023qlora} use rank $r=16$ with adapters on all linear projections and 4-bit NF4 quantization (full details in Appendix~\ref{app:hyperparams}).
34	Full fine-tuning (C4; Table~\ref{tab:configs}) uses identical optimizer settings with all parameters trainable.
35	
36	\subsection{Contamination Fractions}
37	\label{sec:fractions}
38	
39	We test six contamination levels: $\alpha \in \{0, 0.1, 0.25, 0.5, 0.75, 1.0\}$, where $\alpha=0$ is the clean baseline and $\alpha=1.0$ replaces the entire training set with synthetic data.
40	
41	\subsection{Monitoring Signals}
42	\label{sec:signals}
43	
44	We monitor five families of training-time signals (eleven signals total), collected every 50 optimizer steps.
45	Spectral signals and evaluation perplexity are computed on a held-out validation set in evaluation mode; train loss is logged from the training set by the Trainer.
46	
47	\paragraph{Spectral signals.}
48	Given $n$ validation sequences, we collect last-layer hidden states into a matrix $\mathbf{H} \in \mathbb{R}^{T \times d}$ ($T$ total tokens, $d$ hidden dimension), center by subtracting the column mean, and compute the sample covariance $\mathbf{C} = \frac{1}{T-1}\mathbf{H}^\top\mathbf{H}$ with eigenvalues $\lambda_1 \geq \cdots \geq \lambda_d \geq 0$.
49	
50	\emph{Stable rank} measures the effective dimensionality of the representation:
51	\begin{equation}
52	    \mathrm{SR}(\mathbf{C}) = \frac{\left(\sum_{i=1}^{d} \lambda_i\right)^2}{\sum_{i=1}^{d} \lambda_i^2}.
53	    \label{eq:stable_rank}
54	\end{equation}
55	Under model collapse, $\mathrm{SR}$ \emph{increases}: the Frobenius norm $\|\mathbf{H}\|_F^2$ grows faster than the leading eigenvalue $\lambda_1$, dispersing energy across more dimensions rather than concentrating it.%
56	\footnote{This is the participation ratio of the covariance eigenspectrum, closely related to but distinct from the matrix stable rank $\|\mathbf{H}\|_F^2 / \|\mathbf{H}\|_2^2$; the two are monotonically related for centered data.}
57	
58	\emph{Spectral entropy} provides a complementary measure of spectral concentration:
59	\begin{equation}
60	    \mathrm{SE}(\mathbf{C}) = \frac{-\sum_{i=1}^{d} p_i \log p_i}{\log d}, \quad p_i = \frac{\lambda_i}{\sum_{j=1}^{d} \lambda_j}.
61	    \label{eq:spectral_entropy}
62	\end{equation}
63	$\mathrm{SE} \in [0,1]$, with $\mathrm{SE}=1$ for a uniform spectrum and $\mathrm{SE} \to 0$ for concentration on few components.
64	We use $n=64$ validation chunks for SVD computation.
65	
66	\paragraph{Output signals.}
67	We monitor three output-level signals computed on different data splits.
68	
69	\emph{Train loss} $\mathcal{L}_\text{train}$ is the per-batch cross-entropy on the current training corpus, logged every 50 optimizer steps by the HuggingFace Trainer.
70	Because contaminated data has lower entropy than real text, train loss \emph{decreases} under collapse---the model fits synthetic output easily.
71	This makes train loss an effective within-generation detector of data distribution change, though a decrease in train loss does not imply improved model quality.
72	
73	\emph{Evaluation perplexity} is computed on a held-out clean validation set:
74	\begin{equation}
75	    \mathrm{PPL}_\text{eval} = \exp\!\left(\frac{1}{N}\sum_{i=1}^{|\mathcal{V}|} \ell(\mathbf{x}_i)\right),
76	    \label{eq:perplexity}
77	\end{equation}
78	where $\ell(\mathbf{x}_i)$ is the cross-entropy loss on validation sequence $\mathbf{x}_i$ and $N$ is the total token count.
79	Evaluation perplexity tracks degradation in language modeling quality on real text across generations, but its within-generation utility is limited (Section~\ref{sec:early_warning_results}).
80	Note that training perplexity $\mathrm{PPL}_\text{train} = \exp(\mathcal{L}_\text{train})$ is a monotone transform of train loss; we report train loss directly since it is the quantity logged during training.
81	
82	\emph{Token entropy} measures the mean per-position entropy of the next-token distribution:
83	\begin{equation}
84	    \mathrm{TE}(\mathbf{x}) = \frac{1}{L-1}\sum_{t=1}^{L-1} H\!\left(P_\theta(\cdot \mid x_{\leq t})\right), \quad H(P) = -\sum_v P(v) \log P(v),
85	    \label{eq:token_entropy}
86	\end{equation}
87	averaged over 100 validation chunks.
88	Decreasing token entropy indicates the model is becoming more peaked in its predictions, a hallmark of mode collapse in generation.
89	
90	\paragraph{Gradient signal.}
91	We log the L2 gradient norm $\|\nabla_\theta \mathcal{L}\|_2$ before each optimizer step.
92	Under QLoRA, gradient norm exhibits non-monotonic behavior because gradients are confined to a rank-$r$ adapter subspace~\citep{hu2022lora} with NF4 quantization noise~\citep{dettmers2023qlora}; Section~\ref{sec:taxonomy} analyzes this method-dependence.
93	
94	\paragraph{Diversity and repetition signals.}
95	We compute distinct-$n$ (the ratio of unique $n$-grams to total $n$-grams in generated text, for $n \in \{1,2,3\}$) and self-BLEU (average pairwise BLEU between generated samples) on 100 generated continuations per checkpoint.
96	Distinct-$n$ captures lexical diversity; self-BLEU captures inter-sample repetition.
97	
98	\paragraph{Downstream signal.}
99	We evaluate HellaSwag~\citep{zellers2019hellaswag} accuracy (4-choice commonsense reasoning, 1{,}000 samples) at the end of each generation as a downstream task probe.
100	
101	\subsection{Experimental Configurations}
102	\label{sec:configs}
103	
104	Table~\ref{tab:configs} summarizes our experimental configurations.
105	C1 provides initial signal discovery on the smallest model.
106	C2 is the primary analysis configuration, with five independent seeds providing statistical power for bootstrap confidence intervals and effect size estimation.
107	C4 isolates method-dependence by comparing full fine-tuning against QLoRA under matched conditions.
108	All results reported in this paper are from C1, C2, and C4.
109	C3 (cross-domain, PubMed) and C5 (scale validation, 3B) are ongoing; we include them in the table for completeness.
110	
111	\begin{table}[t]
112	\centering
113	\small
114	\caption{Experimental configurations. Trainable\% indicates the fraction of parameters updated during fine-tuning.}
115	\label{tab:configs}
116	\begin{tabular}{llrllcll}
117	\toprule
118	ID & Model & Params & Dataset & Fractions ($\alpha$) & Seeds & Method & Train.\% \\
119	\midrule
120	C1 & Qwen2.5-0.5B & 494M & WikiText-2 & \{0, 0.5, 1.0\} & 1 & QLoRA $r{=}16$ & 0.8 \\
121	C2 & Qwen2.5-1.5B & 1.5B & WikiText-2 & \{0, 0.1, 0.25, 0.5, 0.75, 1.0\} & 5 & QLoRA $r{=}16$ & 0.5 \\
122	C3 & Qwen2.5-1.5B & 1.5B & PubMed & \{0, 0.5, 1.0\} & 3 & QLoRA $r{=}16$ & 0.5 \\
123	C4 & Qwen2.5-0.5B & 494M & WikiText-2 & \{0, 0.5, 1.0\} & 1 & Full FT & 100 \\
124	C5 & Qwen2.5-3B & 3B & WikiText-2 & \{0, 0.5, 1.0\} & 1 & QLoRA $r{=}16$ & 0.3 \\
125	\bottomrule
126	\end{tabular}
127	\end{table}
128	
129	WikiText-2~\citep{merity2017pointer} is tokenized and chunked into 512-token sequences (4{,}916 training chunks).
130	PubMed abstracts~\citep{pubmed2024} (C3) undergo identical preprocessing.
131	
132	\subsection{Evaluation Framework}
133	\label{sec:evaluation}
134	
135	\paragraph{Cross-generation severity.}
136	For each signal $s$ and generation $g$, we compute the Spearman rank correlation $\rho_g^{(s)}$ between contamination fraction $\alpha$ and the end-of-generation signal value across all tested fractions, with 95\% bootstrap confidence intervals.
137	We report Cohen's $d$ effect sizes between the clean baseline and each contamination level as the primary evidence for signal sensitivity, since rank correlations alone do not convey the magnitude of signal separation.
138	
139	\paragraph{Within-generation detection.}
140	We compute the area under the ROC curve (AUROC) for binary collapse detection at each signal checkpoint (every 50 steps), using \emph{clustered bootstrap} resampling with fraction$\times$seed as the cluster unit to account for causal dependence across generations (Appendix~\ref{app:bootstrap}).
141	We also compute the relative deviation at each checkpoint:
142	\begin{equation}
143	    \Delta_s(t, \alpha) = \frac{|s_\alpha(t) - s_0(t)|}{|s_0(t)|} \times 100\%,
144	    \label{eq:deviation}
145	\end{equation}
146	where $s_\alpha(t)$ and $s_0(t)$ are signal values at step $t$ for fraction $\alpha$ and the clean baseline.
147	A signal provides early warning if $\Delta_s(t, \alpha) > 5\%$ within the first 10\% of training steps.
148	
149	\paragraph{Method-dependence.}
150	We compare signal trajectories between QLoRA (C1) and full fine-tuning (C4) under matched conditions to isolate method-dependent effects.
151	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b026817f-834d-4c6e-bcf6-2c1b8e253f13",
  "isSidechain": true,
  "promptId": "80dd2a4d-c31a-43ae-8316-4a6135d9fed6",
  "agentId": "ade4d670d78b2afaf",
  "type": "user",
  "uuid": "84640c53-0469-464a-bd08-1bbeb906ce7f",
  "sourceToolAssistantUUID": "b026817f-834d-4c6e-bcf6-2c1b8e253f13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-16T10:43:10.484Z_

<details open><summary>🔧 Tool call — Read · `toolu_017WG3MSuHT4zuQeMojUc9ot`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84640c53-0469-464a-bd08-1bbeb906ce7f",
  "isSidechain": true,
  "agentId": "ade4d670d78b2afaf",
  "requestId": "req_011Cb67JBsXgAqyzuCn9aDWa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a5781cd6-3952-413d-9860-12d00f5d782e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013x4ExP5bMtBZ8heh95cvuY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7864,
      "cache_read_input_tokens": 65927,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7864,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 39 · 2026-05-16T10:43:10.489Z_

<details><summary>↩ Tool result · `toolu_017WG3MSuHT4zuQeMojUc9ot`</summary>

```text
1	% Discussion section — collapse_severity_monitor
2	% Data sources: plan006 (3-seed Cohen's d), within_gen_analysis, plan003-fullft-05B, heatmap_data.json
3	
4	\section{Discussion}
5	\label{sec:discussion}
6	
7	\subsection{Practical Three-Tier Monitoring Recommendation}
8	\label{sec:three_tier}
9	
10	No single signal suffices for collapse monitoring across all operating regimes.
11	Our results motivate a three-tier strategy:
12	(1)~\textbf{within-generation alarm} $\to$ stable rank (highest AUROC from 10\% training progress; Section~\ref{sec:early_warning_results});
13	(2)~\textbf{cross-generation severity tracking} $\to$ evaluation perplexity (large effect size, interpretable scale);
14	(3)~\textbf{severity discrimination} $\to$ spectral entropy (largest effect size, lowest seed-to-seed variability).
15	The signal that best detects collapse onset (stable rank) differs from the one that most reproducibly quantifies its severity (spectral entropy).
16	
17	\subsection{Partial Recovery at Moderate Contamination}
18	\label{sec:recovery}
19	
20	The partial recovery at moderate contamination documented in Section~\ref{sec:taxonomy} is consistent with data accumulation effects~\citep{Gerstgrasser2024}: the retained real data fraction attenuates collapse pressure.
21	The practical consequence is that monitoring thresholds should be calibrated to the expected contamination level rather than set as binary decisions.
22	
23	Preliminary cross-domain results ($N = 2$ seeds, PubMed abstracts at $\alpha = 0.5$) indicate that cross-generation recovery is systematically weaker in specialized domains (evaluation perplexity recovers $41\%$ of the generation-1 spike vs.\ $53\%$ for WikiText; spectral signals recover $15$--$18\%$ vs.\ $32\%$), consistent with narrower distributions being harder to recover through real data mixing.
24	
25	\subsection{Comparison with Concurrent Monitoring Approaches}
26	\label{sec:sigma_comparison}
27	
28	The signals evaluated here incur near-zero marginal cost: they are computed from quantities already available during standard training and require no clean reference distribution.
29	SIGMA~\citep{Gu2026} operates post-hoc on the output embedding Gram matrix and requires a clean reference; \citet{Kalinowski2026} uses persistent homology at higher computational cost.
30	Neither provides cross-family comparison of operating ranges or within-generation early warning.
31	These approaches are complementary: SIGMA and topological methods may capture aspects of collapse that covariance signals miss, while our signals offer online, reference-free monitoring.
32	
33	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a5781cd6-3952-413d-9860-12d00f5d782e",
  "isSidechain": true,
  "promptId": "80dd2a4d-c31a-43ae-8316-4a6135d9fed6",
  "agentId": "ade4d670d78b2afaf",
  "type": "user",
  "uuid": "e6f514f6-2520-43ae-92b4-99df220c6af1",
  "sourceToolAssistantUUID": "a5781cd6-3952-413d-9860-12d00f5d782e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-16T10:43:11.360Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GrzrvhUVNopb1hy52FBYvy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6f514f6-2520-43ae-92b4-99df220c6af1",
  "isSidechain": true,
  "agentId": "ade4d670d78b2afaf",
  "requestId": "req_011Cb67JBsXgAqyzuCn9aDWa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b6835ed9-1033-483d-bbd1-28c5be2fe0a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013x4ExP5bMtBZ8heh95cvuY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7864,
      "cache_read_input_tokens": 65927,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7864,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 41 · 2026-05-16T10:43:11.373Z_

<details><summary>↩ Tool result · `toolu_01GrzrvhUVNopb1hy52FBYvy`</summary>

```text
1	% Limitations section — collapse_severity_monitor
2	
3	Our study has several limitations that bound the scope of our conclusions.
4	
5	\paragraph{Scale.}
6	All reported results use Qwen2.5-0.5B and 1.5B models.
7	Preliminary 3B baseline results confirm signal stability ($<3\%$ variation across generations at $\alpha = 0$), but severity gradient validation at 3B and cross-domain validation on PubMed are ongoing.
8	Whether signal--severity relationships and operating ranges transfer to models at scales of practical deployment ($\geq$7B) remains unvalidated.
9	Stable rank baselines are known to be scale-dependent~\citep{Jha2025}, and threshold calibration may require per-scale adjustment.
10	
11	\paragraph{Seed count and statistical power.}
12	Cross-generation effect sizes are computed from $N = 3$ seeds (C2 configuration, interim 3 of 5 planned seeds); within-generation AUROC results use $N = 1$ seed at 0.5B (C1).
13	The full fine-tuning comparison (C4) uses $N = 1$ seed.
14	These sample sizes are insufficient for rank-based tests (minimum $p = 0.25$ for Wilcoxon with $N = 3$), and we rely on bootstrap confidence intervals.
15	Stable rank's coefficient of variation ($\mathrm{CV} = 0.022$) is an order of magnitude larger than spectral entropy's ($0.0015$), and its effect size dropped from $d = 61.7$ to $d = 9.43$ when a third seed was added---underscoring that our ranking of signals by sensitivity may shift with more seeds.
16	
17	\paragraph{Domain coverage.}
18	All reported results use WikiText-2; cross-domain validation on PubMed is ongoing.
19	Whether our signal taxonomy generalizes to biomedical text, code, dialogue, multilingual text, or instruction-following data is unknown.
20	
21	\paragraph{Repetition confound.}
22	At $\alpha = 1.0$, the 1{,}500 unique synthetic chunks are upsampled to 4{,}916, introducing repetition (${\sim}3.3\times$ per epoch) that may contribute to observed training dynamics through memorization rather than synthetic data quality degradation alone.
23	However, this confound is mitigated at moderate contamination: at $\alpha = 0.5$, the corpus contains 2{,}458 real and 1{,}500 synthetic chunks with minimal repetition, yet the dose-response trend and partial recovery conclusions (Section~\ref{sec:taxonomy}) remain intact.
24	The $\alpha = 0$ control undergoes the identical training procedure without collapse, ruling out the training process itself as a confound.
25	
26	\paragraph{Collapse source.}
27	Our iterative retraining protocol simulates a specific collapse mechanism---self-consuming loops with controlled contamination fractions.
28	Real-world collapse may involve mixed provenance (multiple model generations), distribution shift between generations, or partial synthetic contamination at unknown fractions.
29	Signal behavior under these conditions may differ from our controlled setting.
30	
31	\paragraph{Fine-tuning methods.}
32	We compare QLoRA and full fine-tuning.
33	Other parameter-efficient methods (LoRA without quantization, adapters, prefix tuning) may interact differently with spectral signals due to different parameterization constraints.
34	
35	\paragraph{Causal claims.}
36	We establish correlations between signals and collapse severity, not causal mechanisms.
37	The spectral entropy increase under collapse reflects a change in representation structure, but we do not prove that this change causes (rather than accompanies) output degradation.
38	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b6835ed9-1033-483d-bbd1-28c5be2fe0a3",
  "isSidechain": true,
  "promptId": "80dd2a4d-c31a-43ae-8316-4a6135d9fed6",
  "agentId": "ade4d670d78b2afaf",
  "type": "user",
  "uuid": "6a2ae237-8de3-4bae-a042-0adc1f30455b",
  "sourceToolAssistantUUID": "b6835ed9-1033-483d-bbd1-28c5be2fe0a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-16T10:43:11.501Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HUpZJVLuzEjteRCS5M5S13`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a2ae237-8de3-4bae-a042-0adc1f30455b",
  "isSidechain": true,
  "agentId": "ade4d670d78b2afaf",
  "requestId": "req_011Cb67JBsXgAqyzuCn9aDWa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "470fa8e6-e981-4c74-b151-8a120f7ab7a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013x4ExP5bMtBZ8heh95cvuY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7864,
      "cache_read_input_tokens": 65927,
      "output_tokens": 227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7864
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 227,
          "cache_read_input_tokens": 65927,
          "cache_creation_input_tokens": 7864,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7864,
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

_source line 43 · 2026-05-16T10:43:11.512Z_

<details><summary>↩ Tool result · `toolu_01HUpZJVLuzEjteRCS5M5S13`</summary>

```text
1	% Conclusion section — collapse_severity_monitor
2	% Data sources: plan006 (3-seed Cohen's d), within_gen_analysis, plan003-fullft-05B
3	
4	\section{Conclusion}
5	\label{sec:conclusion}
6	
7	We presented a systematic empirical study of training-time signals as model collapse severity monitors across two model scales, two fine-tuning methods, and six contamination fractions.
8	Three findings emerge.
9	First, spectral entropy ($d = 33.48$) and evaluation perplexity ($d = 20.82$) reliably track collapse severity; ten of eleven signals maintain consistent direction across methods.
10	Second, stable rank provides within-generation early warning ($\mathrm{AUROC} = 0.984$ pooled; $34.4\%$ deviation at 3\% of training), while evaluation perplexity---the most commonly checked metric---achieves only $\mathrm{AUROC} = 0.533$ for the same task.
11	Third, signal informativeness depends on the training method, motivating a three-tier monitoring strategy: stable rank for within-generation alarms, evaluation perplexity for cross-generation tracking, and spectral entropy for severity discrimination.
12	
13	\paragraph{Future directions.}
14	Validating these findings at larger scales ($\geq$7B) and across diverse domains and model families (cross-domain and 3B-scale experiments are ongoing) would establish generalizability.
15	Translating early warning signals into automated intervention triggers---adaptive learning rate reduction, selective data filtering, or training rollback when spectral deviation exceeds calibrated thresholds---would close the loop from detection to mitigation.
16	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "470fa8e6-e981-4c74-b151-8a120f7ab7a8",
  "isSidechain": true,
  "promptId": "80dd2a4d-c31a-43ae-8316-4a6135d9fed6",
  "agentId": "ade4d670d78b2afaf",
  "type": "user",
  "uuid": "f34778ab-1c88-4b31-86b7-600c739b4c0a",
  "sourceToolAssistantUUID": "470fa8e6-e981-4c74-b151-8a120f7ab7a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-16T10:43:13.641Z_

Now let me check the references and the dream review for additional context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f34778ab-1c88-4b31-86b7-600c739b4c0a",
  "isSidechain": true,
  "agentId": "ade4d670d78b2afaf",
  "requestId": "req_011Cb67JXAPiBUUTQ5NEcQw7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "87493932-94b6-4003-9d40-67cd3c455b0d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dk7ghMXutGiwCHHWa7cw4z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2347,
      "cache_read_input_tokens": 73791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2347,
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

_source line 45 · 2026-05-16T10:43:15.195Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DJFY8qipkkbqETrWpVMfuG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87493932-94b6-4003-9d40-67cd3c455b0d",
  "isSidechain": true,
  "agentId": "ade4d670d78b2afaf",
  "requestId": "req_011Cb67JXAPiBUUTQ5NEcQw7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0f737909-bc97-4bc2-9171-d6db8fad2d94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dk7ghMXutGiwCHHWa7cw4z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2347,
      "cache_read_input_tokens": 73791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2347,
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

_source line 46 · 2026-05-16T10:43:15.201Z_

<details><summary>↩ Tool result · `toolu_01DJFY8qipkkbqETrWpVMfuG`</summary>

```text
1	% references.bib — collapse_severity_monitor
2	% Auto-compiled from paper sections: abstract, introduction, related_work, method, competitor_comparison
3	% 44 citation keys, sorted alphabetically
4	% Generated: 2026-05-15
5	
6	@inproceedings{AlphaPruning2024,
7	  title     = {{AlphaPruning}: Using Heavy-Tailed Self Regularization Theory for Improved Layer-wise Pruning of Large Language Models},
8	  author    = {Haiquan Lu and Yefan Zhou and Shiwei Liu and Zhangyang Wang and Michael W. Mahoney and Yaoqing Yang},
9	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
10	  year      = {2024},
11	  eprint    = {2410.10912},
12	  archivePrefix = {arXiv},
13	  primaryClass  = {cs.LG}
14	}
15	
16	@inproceedings{Alemohammad2024,
17	  title     = {Self-Consuming Generative Models Go {MAD}},
18	  author    = {Sina Alemohammad and Josue Casco-Rodriguez and Lorenzo Luzi and Ahmed Imtiaz Humayun and Hossein Babaei and Daniel LeJeune and Ali Siahkoohi and Richard G. Baraniuk},
19	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
20	  year      = {2024},
21	  eprint    = {2307.01850},
22	  archivePrefix = {arXiv},
23	  primaryClass  = {cs.LG}
24	}
25	
26	@article{Bakshi2026,
27	  title   = {From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources},
28	  author  = {Soham Bakshi and Sunrit Chakraborty},
29	  year    = {2026},
30	  eprint  = {2602.10531},
31	  archivePrefix = {arXiv},
32	  primaryClass  = {cs.LG}
33	}
34	
35	@inproceedings{Chen2024_dse,
36	  title     = {Assessing Neural Network Representations During Training Using Noise-Resilient Diffusion Spectral Entropy},
37	  author    = {Danqi Liao and Chen Liu and Benjamin W. Christensen and Alexander Tong and Guillaume Huguet and Guy Wolf and Maximilian Nickel and Ian Adelstein and Smita Krishnaswamy},
38	  booktitle = {Proceedings of the 58th Annual Conference on Information Sciences and Systems (CISS)},
39	  year      = {2024},
40	  publisher = {IEEE},
41	  eprint    = {2312.04823},
42	  archivePrefix = {arXiv},
43	  primaryClass  = {cs.LG}
44	}
45	
46	@article{Dathathri2024,
47	  title   = {Scalable Watermarking for Identifying Large Language Model Outputs},
48	  author  = {Sumanth Dathathri and Abigail See and Sumedh Ghaisas and Po-Sen Huang and Rob McAdam and Johannes Welbl and Vandana Bachani and Alex Kaskasoli and Robert Stanforth and Tatiana Matejovicova and Jamie Hayes and Nidhi Vyas and Majd Al Merey and Jonah Brown-Cohen and Rudy Bunel and Borja Balle and Taylan Cemgil and Zahra Ahmed and Kitty Stacpoole and Ilia Shumailov and Ciprian Baetu and Sven Gowal and Demis Hassabis and Pushmeet Kohli},
49	  journal = {Nature},
50	  volume  = {634},
51	  pages   = {818--823},
52	  year    = {2024}
53	}
54	
55	@inproceedings{dettmers2023qlora,
56	  title     = {{QLoRA}: Efficient Finetuning of Quantized Large Language Models},
57	  author    = {Tim Dettmers and Artidoro Pagnoni and Ari Holtzman and Luke Zettlemoyer},
58	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
59	  year      = {2023},
60	  eprint    = {2305.14314},
61	  archivePrefix = {arXiv},
62	  primaryClass  = {cs.LG}
63	}
64	
65	@inproceedings{Dohmatob2024_tails,
66	  title     = {A Tale of Tails: Model Collapse as a Change of Scaling Laws},
67	  author    = {Elvis Dohmatob and Yunzhen Feng and Pu Yang and Francois Charton and Julia Kempe},
68	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
69	  pages     = {11165--11197},
70	  year      = {2024},
71	  eprint    = {2402.07043},
72	  archivePrefix = {arXiv},
73	  primaryClass  = {cs.LG}
74	}
75	
76	@inproceedings{Dohmatob2025,
77	  title     = {Strong Model Collapse},
78	  author    = {Elvis Dohmatob and Yunzhen Feng and Arjun Subramonian and Julia Kempe},
79	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
80	  year      = {2025},
81	  note      = {Spotlight},
82	  eprint    = {2410.04840},
83	  archivePrefix = {arXiv},
84	  primaryClass  = {cs.LG}
85	}
86	
87	@article{Elgaar2026,
88	  title   = {Curriculum Learning for {LLM} Pretraining: An Analysis of Learning Dynamics},
89	  author  = {Mohamed Elgaar and Hadi Amiri},
90	  year    = {2026},
91	  eprint  = {2601.21698},
92	  archivePrefix = {arXiv},
93	  primaryClass  = {cs.CL}
94	}
95	
96	@inproceedings{Feng2025,
97	  title     = {Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification},
98	  author    = {Yunzhen Feng and Elvis Dohmatob and Pu Yang and Francois Charton and Julia Kempe},
99	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
100	  year      = {2025},
101	  eprint    = {2406.07515},
102	  archivePrefix = {arXiv},
103	  primaryClass  = {cs.LG}
104	}
105	
106	@inproceedings{Fu2024_icml,
107	  title     = {Towards Theoretical Understandings of Self-Consuming Generative Models},
108	  author    = {Shi Fu and Sen Zhang and Yingjie Wang and Xinmei Tian and Dacheng Tao},
109	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
110	  year      = {2024},
111	  eprint    = {2402.11778},
112	  archivePrefix = {arXiv},
113	  primaryClass  = {cs.LG}
114	}
115	
116	@article{Gambetta2024,
117	  title   = {Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative {AI}},
118	  author  = {Daniele Gambetta and Gizem Gezici and Fosca Giannotti and Dino Pedreschi and Alistair Knott and Luca Pappalardo},
119	  year    = {2024},
120	  eprint  = {2410.12341},
121	  archivePrefix = {arXiv},
122	  primaryClass  = {cs.CL}
123	}
124	
125	@inproceedings{Gao2019,
126	  title     = {Representation Degeneration Problem in Training Natural Language Generation Models},
127	  author    = {Jun Gao and Di He and Xu Tan and Tao Qin and Liwei Wang and Tie-Yan Liu},
128	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
129	  year      = {2019},
130	  eprint    = {1907.12009},
131	  archivePrefix = {arXiv},
132	  primaryClass  = {cs.CL}
133	}
134	
135	@inproceedings{Gerstgrasser2024,
136	  title     = {Is Model Collapse Inevitable? {Breaking} the Curse of Recursion by Accumulating Real and Synthetic Data},
137	  author    = {Matthias Gerstgrasser and Rylan Schaeffer and Apratim Dey and Rafael Rafailov and Henry Sleight and John Hughes and Tomasz Korbak and Rajashree Agrawal and Dhruv Bhandarkar Pai and Andrey Gromov and Daniel A. Roberts and Diyi Yang and David L. Donoho and Sanmi Koyejo},
138	  booktitle = {Proceedings of the First Conference on Language Modeling (COLM)},
139	  year      = {2024},
140	  eprint    = {2404.01413},
141	  archivePrefix = {arXiv},
142	  primaryClass  = {cs.LG}
143	}
144	
145	@inproceedings{Gillman2024,
146	  title     = {Self-Correcting Self-Consuming Loops for Generative Model Training},
147	  author    = {Nate Gillman and Michael Freeman and Daksh Aggarwal and Chia-Hong Hsu and Calvin Luo and Yonglong Tian and Chen Sun},
148	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
149	  pages     = {15646--15677},
150	  year      = {2024},
151	  eprint    = {2402.07087},
152	  archivePrefix = {arXiv},
153	  primaryClass  = {cs.LG}
154	}
155	
156	@article{Gu2026,
157	  title   = {{SIGMA}: Scalable Spectral Insights for {LLM} Model Collapse},
158	  author  = {Yi Gu and Lingyou Pang and Xiangkun Ye and Tianyu Wang and Jianyu Lin and Carey E. Priebe and Alexander Aue},
159	  year    = {2026},
160	  eprint  = {2601.03385},
161	  archivePrefix = {arXiv},
162	  primaryClass  = {cs.LG}
163	}
164	
165	@inproceedings{hu2022lora,
166	  title     = {{LoRA}: Low-Rank Adaptation of Large Language Models},
167	  author    = {Edward J. Hu and Yelong Shen and Phillip Wallis and Zeyuan Allen-Zhu and Yuanzhi Li and Shean Wang and Lu Wang and Weizhu Chen},
168	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
169	  year      = {2022},
170	  eprint    = {2106.09685},
171	  archivePrefix = {arXiv},
172	  primaryClass  = {cs.CL}
173	}
174	
175	@article{Kalra2026,
176	  title   = {A Scalable Measure of Loss Landscape Curvature for Analyzing the Training Dynamics of {LLMs}},
177	  author  = {Dayal Singh Kalra and Jean-Christophe Gagnon-Audet and Andrey Gromov and Ishita Mediratta and Kelvin Niu and Alexander H. Miller and Michael Shvartsman},
178	  year    = {2026},
179	  eprint  = {2601.16979},
180	  archivePrefix = {arXiv},
181	  primaryClass  = {cs.LG}
182	}
183	
184	@article{Kalinowski2026,
185	  title   = {Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index},
186	  author  = {Alexander Kalinowski},
187	  year    = {2026},
188	  eprint  = {2604.26984},
189	  archivePrefix = {arXiv},
190	  primaryClass  = {cs.LG}
191	}
192	
193	@inproceedings{Kazdan2024,
194	  title     = {Collapse or Thrive? {Perils} and Promises of Synthetic Data in a Self-Generating World},
195	  author    = {Joshua Kazdan and Rylan Schaeffer and Apratim Dey and Matthias Gerstgrasser and Rafael Rafailov and David L. Donoho and Sanmi Koyejo},
196	  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},
197	  pages     = {29469--29494},
198	  year      = {2025},
199	  eprint    = {2410.16713},
200	  archivePrefix = {arXiv},
201	  primaryClass  = {cs.LG}
202	}
203	
204	@inproceedings{Kirchenbauer2023,
205	  title     = {A Watermark for Large Language Models},
206	  author    = {John Kirchenbauer and Jonas Geiping and Yuxin Wen and Jonathan Katz and Ian Miers and Tom Goldstein},
207	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
208	  pages     = {17061--17084},
209	  year      = {2023},
210	  eprint    = {2301.10226},
211	  archivePrefix = {arXiv},
212	  primaryClass  = {cs.CL}
213	}
214	
215	@article{Li2025_gradient,
216	  title   = {How Instruction and Reasoning Data shape Post-Training: Data Quality through the Lens of Layer-wise Gradients},
217	  author  = {Ming Li and Yanhong Li and Ziyue Li and Tianyi Zhou},
218	  year    = {2025},
219	  eprint  = {2504.10766},
220	  archivePrefix = {arXiv},
221	  primaryClass  = {cs.CL}
222	}
223	
224	@inproceedings{Jha2025,
225	  title     = {Spectral Scaling Laws in Language Models: How Effectively Do Feed-Forward Networks Use Their Latent Space?},
226	  author    = {Nandan Kumar Jha and Brandon Reagen},
227	  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},
228	  year      = {2025},
229	  eprint    = {2510.00537},
230	  archivePrefix = {arXiv},
231	  primaryClass  = {cs.CL}
232	}
233	
234	@article{Liu2026_lifecycle,
235	  title   = {The Spectral Lifecycle of Transformer Training: Transient Compression Waves, Persistent Spectral Gradients, and the {Q/K--V} Asymmetry},
236	  author  = {Yi Liu},
237	  year    = {2026},
238	  eprint  = {2604.22778},
239	  archivePrefix = {arXiv},
240	  primaryClass  = {cs.LG}
241	}
242	
243	@article{Martin2021,
244	  title   = {Predicting Trends in the Quality of State-of-the-Art Neural Networks without Access to Training or Testing Data},
245	  author  = {Charles H. Martin and Tongsu Serena Peng and Michael W. Mahoney},
246	  journal = {Nature Communications},
247	  volume  = {12},
248	  pages   = {4122},
249	  year    = {2021},
250	  eprint  = {2002.06716},
251	  archivePrefix = {arXiv},
252	  primaryClass  = {cs.LG}
253	}
254	
255	@inproceedings{merity2017pointer,
256	  title     = {Pointer Sentinel Mixture Models},
257	  author    = {Stephen Merity and Caiming Xiong and James Bradbury and Richard Socher},
258	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
259	  year      = {2017},
260	  eprint    = {1609.07843},
261	  archivePrefix = {arXiv},
262	  primaryClass  = {cs.CL}
263	}
264	
265	@inproceedings{Mitchell2023,
266	  title     = {{DetectGPT}: Zero-Shot Machine-Generated Text Detection using Probability Curvature},
267	  author    = {Eric Mitchell and Yoonho Lee and Alexander Khazatsky and Christopher D. Manning and Chelsea Finn},
268	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
269	  pages     = {24950--24962},
270	  year      = {2023},
271	  eprint    = {2301.11305},
272	  archivePrefix = {arXiv},
273	  primaryClass  = {cs.CL}
274	}
275	
276	@inproceedings{Penedo2024,
277	  title     = {The {FineWeb} Datasets: Decanting the Web for the Finest Text Data at Scale},
278	  author    = {Guilherme Penedo and Hynek Kydlicek and Loubna Ben Allal and Anton Lozhkov and Margaret Mitchell and Colin Raffel and Leandro von Werra and Thomas Wolf},
279	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS), Datasets and Benchmarks Track},
280	  year      = {2024},
281	  eprint    = {2406.17557},
282	  archivePrefix = {arXiv},
283	  primaryClass  = {cs.CL}
284	}
285	
286	@inproceedings{Pennington2017,
287	  title     = {Nonlinear Random Matrix Theory for Deep Learning},
288	  author    = {Jeffrey Pennington and Pratik Worah},
289	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
290	  pages     = {2637--2646},
291	  year      = {2017}
292	}
293	
294	@article{Qiu2025,
295	  title   = {Spectral Alignment as Predictor of Loss Explosion in Neural Network Training},
296	  author  = {Haiquan Qiu and You Wu and Yingjie Tan and Yaqing Wang and Quanming Yao},
297	  year    = {2025},
298	  eprint  = {2510.04202},
299	  archivePrefix = {arXiv},
300	  primaryClass  = {cs.LG}
301	}
302	
303	@inproceedings{Sander2024,
304	  title     = {Watermarking Makes Language Models Radioactive},
305	  author    = {Tom Sander and Pierre Fernandez and Alain Durmus and Matthijs Douze and Teddy Furon},
306	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
307	  year      = {2024},
308	  eprint    = {2402.14904},
309	  archivePrefix = {arXiv},
310	  primaryClass  = {cs.CL}
311	}
312	
313	@inproceedings{Sanyal2020,
314	  title     = {Stable Rank Normalization for Improved Generalization in Neural Networks and {GANs}},
315	  author    = {Amartya Sanyal and Philip H. S. Torr and Puneet K. Dokania},
316	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
317	  year      = {2020},
318	  eprint    = {1906.04659},
319	  archivePrefix = {arXiv},
320	  primaryClass  = {cs.LG}
321	}
322	
323	@article{Schaeffer2025,
324	  title   = {Position: Model Collapse Does Not Mean What You Think},
325	  author  = {Rylan Schaeffer and Joshua Kazdan and Alvan Caleb Arulandu and Sanmi Koyejo},
326	  year    = {2025},
327	  eprint  = {2503.03150},
328	  archivePrefix = {arXiv},
329	  primaryClass  = {cs.LG}
330	}
331	
332	@article{Seddik2024,
333	  title   = {How Bad is Training on Synthetic Data? {A} Statistical Analysis of Language Model Collapse},
334	  author  = {Mohamed El Amine Seddik and Suei-Wen Chen and Soufiane Hayou and Pierre Youssef and Merouane Debbah},
335	  year    = {2024},
336	  eprint  = {2404.05090},
337	  archivePrefix = {arXiv},
338	  primaryClass  = {cs.CL}
339	}
340	
341	@inproceedings{Shi2024_mink,
342	  title     = {Detecting Pretraining Data from Large Language Models},
343	  author    = {Weijia Shi and Anirudh Ajith and Mengzhou Xia and Yangsibo Huang and Daogao Liu and Terra Blevins and Danqi Chen and Luke Zettlemoyer},
344	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
345	  year      = {2024},
346	  eprint    = {2310.16789},
347	  archivePrefix = {arXiv},
348	  primaryClass  = {cs.CL}
349	}
350	
351	@inproceedings{Shi2025_neurips,
352	  title     = {A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective},
353	  author    = {Lianghe Shi and Meng Wu and Huijie Zhang and Zekai Zhang and Molei Tao and Qing Qu},
354	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
355	  year      = {2025},
356	  note      = {Spotlight},
357	  eprint    = {2509.16499},
358	  archivePrefix = {arXiv},
359	  primaryClass  = {cs.LG}
360	}
361	
362	@article{Shumailov2024,
363	  title   = {{AI} Models Collapse When Trained on Recursively Generated Data},
364	  author  = {Ilia Shumailov and Zakhar Shumaylov and Yiren Zhao and Nicolas Papernot and Ross Anderson and Yarin Gal},
365	  journal = {Nature},
366	  volume  = {631},
367	  pages   = {755--759},
368	  year    = {2024},
369	  eprint  = {2305.17493},
370	  archivePrefix = {arXiv},
371	  primaryClass  = {cs.LG}
372	}
373	
374	
375	@inproceedings{Staats2024,
376	  title     = {Small Singular Values Matter: A Random Matrix Analysis of Transformer Models},
377	  author    = {Max Staats and Matthias Thamm and Bernd Rosenow},
378	  booktitle = {Advances in Neural Information Processing Systems 38 (NeurIPS)},
379	  year      = {2025},
380	  eprint    = {2410.17770},
381	  archivePrefix = {arXiv},
382	  primaryClass  = {cs.LG}
383	}
384	
385	@article{Wang2025_scaling,
386	  title   = {Data Value in the Age of Scaling: Understanding {LLM} Scaling Dynamics Under Real-Synthetic Data Mixtures},
387	  author  = {Haohui Wang and Jingyuan Qi and Jianpeng Chen and Jun Wu and Lifu Huang and Lecheng Zheng and Kevin Choi and Balaji Veeramani and Edward Bowen and Alison Hu and Tyler Cody and Dawei Zhou},
388	  year    = {2025},
389	  eprint  = {2511.13640},
390	  archivePrefix = {arXiv},
391	  primaryClass  = {cs.CL}
392	}
393	
394	
395	@article{Xu2026,
396	  title   = {Predicting {LLM} Compression Degradation from Spectral Statistics},
397	  author  = {Mingxue Xu},
398	  year    = {2026},
399	  eprint  = {2604.18085},
400	  archivePrefix = {arXiv},
401	  primaryClass  = {cs.LG}
402	}
403	
404	@article{Yi2025,
405	  title   = {Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence},
406	  author  = {Bingji Yi and Qiyuan Liu and Yuwei Cheng and Haifeng Xu},
407	  year    = {2025},
408	  eprint  = {2510.16657},
409	  archivePrefix = {arXiv},
410	  primaryClass  = {cs.LG}
411	}
412	
413	@article{Yunis2024,
414	  title   = {Approaching Deep Learning through the Spectral Dynamics of Weights},
415	  author  = {David Yunis and Kumar Kshitij Patel and Samuel Wheeler and Pedro Savarese and Gal Vardi and Karen Livescu and Michael Maire and Matthew R. Walter},
416	  year    = {2024},
417	  eprint  = {2408.11804},
418	  archivePrefix = {arXiv},
419	  primaryClass  = {cs.LG}
420	}
421	
422	@inproceedings{zellers2019hellaswag,
423	  title     = {{HellaSwag}: Can a Machine Really Finish Your Sentence?},
424	  author    = {Rowan Zellers and Ari Holtzman and Yonatan Bisk and Ali Farhadi and Yejin Choi},
425	  booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics (ACL)},
426	  year      = {2019},
427	  eprint    = {1905.07830},
428	  archivePrefix = {arXiv},
429	  primaryClass  = {cs.CL}
430	}
431	
432	@article{Zhang2026,
433	  title   = {The {LLM} Data Auditor: A Metric-oriented Survey on Quality and Trustworthiness in Evaluating Synthetic Data},
434	  author  = {Kaituo Zhang and Mingzhi Hu and Hoang Anh Duy Le and Fariha Kabir Torsha and Zhimeng Jiang and Minh Khai Bui and Chia-Yuan Chang and Yu-Neng Chuang and Zhen Xiong and Ying Lin and Guanchu Wang and Na Zou},
435	  year    = {2026},
436	  eprint  = {2601.17717},
437	  archivePrefix = {arXiv},
438	  primaryClass  = {cs.CL}
439	}
440	
441	@article{pubmed2024,
442	  title   = {{PubMed} Central: A Full-Text Archive of Biomedical and Life Sciences Journal Literature},
443	  author  = {{National Library of Medicine}},
444	  journal = {National Center for Biotechnology Information},
445	  year    = {2024},
446	  url     = {https://www.ncbi.nlm.nih.gov/pmc/}
447	}
448	
449	@article{Zibakhsh2025,
450	  title   = {{ForTIFAI}: Fending Off Recursive Training Induced Failure for {AI} Model Collapse},
451	  author  = {Soheil Zibakhsh Shabgahi and Pedram Aghazadeh and Azalia Mirhoseini and Farinaz Koushanfar},
452	  year    = {2025},
453	  eprint  = {2509.08972},
454	  archivePrefix = {arXiv},
455	  primaryClass  = {cs.LG}
456	}
457	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0f737909-bc97-4bc2-9171-d6db8fad2d94",
  "isSidechain": true,
  "promptId": "80dd2a4d-c31a-43ae-8316-4a6135d9fed6",
  "agentId": "ade4d670d78b2afaf",
  "type": "user",
  "uuid": "7b5c93a4-de38-47c1-a991-595a36bd4d5a",
  "sourceToolAssistantUUID": "0f737909-bc97-4bc2-9171-d6db8fad2d94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-16T10:43:15.330Z_

<details open><summary>🔧 Tool call — Read · `toolu_01T9NNfQKdnvn5SAq87yyzvi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b5c93a4-de38-47c1-a991-595a36bd4d5a",
  "isSidechain": true,
  "agentId": "ade4d670d78b2afaf",
  "requestId": "req_011Cb67JXAPiBUUTQ5NEcQw7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eae4b8c3-97b1-40f4-a325-6cb317d41a91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dk7ghMXutGiwCHHWa7cw4z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2347,
      "cache_read_input_tokens": 73791,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2347
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 172,
          "cache_read_input_tokens": 73791,
          "cache_creation_input_tokens": 2347,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2347,
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

_source line 48 · 2026-05-16T10:43:15.362Z_

<details><summary>↩ Tool result · `toolu_01T9NNfQKdnvn5SAq87yyzvi`</summary>

```text
1	% Appendix — collapse_severity_monitor
2	% Verified data sources: mvp_frac50_100, within_gen_analysis, per_layer_analysis_v5
3	% Pending: plan_001 (1.5B 6-frac 5-seed), plan_002 (PubMed), plan_003 (Full FT),
4	%          plan_004 (1.5B within-gen), plan_005 (threshold calibration)
5	
6	\appendix
7	
8	\section{Experimental Details}
9	\label{app:exp_details}
10	
11	\subsection{Training Hyperparameters}
12	\label{app:hyperparams}
13	%% Source: mvp_frac50_100 — training config
14	
15	Table~\ref{tab:hyperparams} lists the complete training configuration used across all experiments.
16	
17	\begin{table}[h]
18	\centering
19	\caption{Complete training hyperparameters for all fine-tuning runs.}
20	\label{tab:hyperparams}
21	\small
22	\begin{tabular}{ll}
23	\toprule
24	\textbf{Parameter} & \textbf{Value} \\
25	\midrule
26	\multicolumn{2}{l}{\textit{QLoRA configuration}} \\
27	LoRA rank $r$ & 16 \\
28	LoRA scaling $\alpha_\text{LoRA}$ & 32 \\
29	LoRA dropout & 0.05 \\
30	Target modules & all linear (\texttt{q/k/v/o/up/down/gate\_proj}) \\
31	\midrule
32	\multicolumn{2}{l}{\textit{Base model quantization}} \\
33	Quantization type & NF4 (NormalFloat 4-bit) \\
34	Double quantization & enabled \\
35	Compute dtype & \texttt{bfloat16} \\
36	\midrule
37	\multicolumn{2}{l}{\textit{Optimizer}} \\
38	Algorithm & AdamW \\
39	Learning rate & $2 \times 10^{-4}$ \\
40	Weight decay & 0.01 \\
41	Warmup & 5\% of total steps (linear) \\
42	LR schedule & linear decay \\
43	Gradient clipping & $\|\nabla\|_2 \leq 1.0$ \\
44	\midrule
45	\multicolumn{2}{l}{\textit{Training}} \\
46	Per-device batch size & 4 \\
47	Gradient accumulation steps & 4 \\
48	Effective batch size & 16 \\
49	Epochs per generation & 5 \\
50	Steps per generation & ${\sim}1{,}540$ \\
51	Mixed precision & \texttt{bf16} \\
52	\midrule
53	\multicolumn{2}{l}{\textit{Signal collection}} \\
54	Collection interval & every 50 optimizer steps \\
55	Validation chunks for SVD & 64 \\
56	Validation chunks for entropy/PPL & 100 \\
57	\bottomrule
58	\end{tabular}
59	\end{table}
60	
61	\subsection{Synthetic Data Generation}
62	\label{app:data_gen}
63	%% Source: mvp_frac50_100 — generation config
64	
65	At each generation $g$, we sample synthetic text from the fine-tuned model $\tilde{M}_g$ using the following procedure:
66	
67	\begin{itemize}[nosep]
68	    \item \textbf{Prompting:} The first 32 tokens of each randomly subsampled real-text chunk serve as the prompt.
69	    \item \textbf{Decoding:} Nucleus sampling with temperature $\tau = 1.0$ and top-$p = 0.95$.
70	    \item \textbf{Max new tokens:} 480 (total sequence length $\leq 512$).
71	    \item \textbf{Subsample size:} 1{,}500 chunks per generation (from $|\mathcal{D}_\text{real}| = 4{,}916$).
72	\end{itemize}
73	
74	\noindent
75	The fixed prompt length ensures that synthetic and real chunks share distributional overlap at the beginning, isolating divergence to model-generated continuations.
76	
77	\subsection{Evaluation Details}
78	\label{app:eval_details}
79	%% Source: mvp_frac50_100 — evaluation config
80	
81	\paragraph{HellaSwag evaluation.}
82	We evaluate HellaSwag~\citep{zellers2019hellaswag} using 1{,}000 randomly sampled instances in 4-choice format.
83	For each instance, the model scores each candidate continuation by computing its per-token log-likelihood conditioned on the context, selecting the highest-scoring option.
84	Evaluation is performed at the end of each generation (not at intermediate checkpoints) due to computational cost.
85	
86	\paragraph{Perplexity and token entropy.}
87	Both are computed on the held-out WikiText-2 validation set using 100 validation chunks.
88	Perplexity uses the standard cross-entropy formulation (Eq.~\ref{eq:perplexity}); token entropy averages per-position next-token entropy (Eq.~\ref{eq:token_entropy}) over all positions in the validation set.
89	
90	\paragraph{Spectral signals.}
91	Stable rank and spectral entropy are computed from the last-layer hidden-state covariance matrix using 64 validation chunks.
92	We retain the top-5 singular values for trajectory logging; the full eigenspectrum is used for stable rank and spectral entropy computation.
93	
94	\subsection{Compute Resources}
95	\label{app:compute}
96	
97	All experiments were conducted on a server with $2 \times$ NVIDIA RTX~5090 (32\,GB VRAM each).
98	Table~\ref{tab:compute} summarizes the computational budget.
99	
100	\begin{table}[h]
101	\centering
102	\caption{Compute budget for P0 experiments.}
103	\label{tab:compute}
104	\small
105	\begin{tabular}{lcc}
106	\toprule
107	\textbf{Component} & \textbf{GPU-hours} & \textbf{Notes} \\
108	\midrule
109	MVP (0.5B, 3 fracs, 1 seed) & ${\sim}15$ & 15 runs $\times$ ${\sim}1$\,h each \\
110	Per-layer analysis & ${\sim}5$ & SVD on saved checkpoints \\
111	Within-gen analysis & ${\sim}5$ & Post-hoc signal recomputation \\
112	%% TODO: plan_001 — 1.5B 6-frac 5-seed budget estimate
113	Full design (est.) & ${\sim}170$ & 150 runs $\times$ ${\sim}1.1$\,h each \\
114	\midrule
115	\textbf{Total (P0)} & $\mathbf{{\sim}195}$ & \\
116	\bottomrule
117	\end{tabular}
118	\end{table}
119	
120	
121	\section{Full Signal Trajectories}
122	\label{app:signal_tables}
123	
124	\subsection{Cross-Fraction Signal Tables}
125	\label{app:cross_frac_tables}
126	%% Source: mvp_frac50_100 — end-of-generation signal values
127	
128	Table~\ref{tab:full_cross_frac} reports end-of-generation signal values for all generations and fractions in the MVP configuration.
129	
130	\begin{table}[h]
131	\centering
132	\caption{End-of-generation signal values across all generations and contamination fractions (0.5B, WikiText-2, seed~42). SR: stable rank, SE: spectral entropy, TE: token entropy, PPL: perplexity.}
133	\label{tab:full_cross_frac}
134	\small
135	\begin{tabular}{clcccc}
136	\toprule
137	\textbf{Gen} & $\boldsymbol{\alpha}$ & \textbf{SR} & \textbf{SE} & \textbf{TE} & \textbf{PPL} \\
138	\midrule
139	%% Source: signals_{0,50,100}pct_gen0.jsonl — step 1540 (is_generation_end)
140	0 & 0    & 22.89 & 0.702 & 2.260 & 15.74 \\
141	0 & 0.5  & 22.92 & 0.702 & 2.261 & 15.73 \\
142	0 & 1.0  & 23.42 & 0.704 & 2.258 & 15.67 \\
143	\midrule
144	%% TODO: plan_001 — fill gen 0 rows for fractions {0.1, 0.25, 0.75} with 5-seed mean ± std
145	%% TODO: plan_001 — fill gens 1–4 for all 6 fractions with 5-seed mean ± std
146	1 & 0    & 22.94 & 0.702 & 2.260 & 15.73 \\
147	1 & 0.5  & 26.17 & 0.724 & 2.151 & 17.95 \\
148	1 & 1.0  & 130.81 & 0.872 & 1.100 & 136.9 \\
149	\midrule
150	2 & 0    & 23.42 & 0.703 & 2.258 & 15.67 \\
151	2 & 0.5  & 25.09 & 0.719 & 2.208 & 17.21 \\
152	2 & 1.0  & 153.77 & 0.885 & 0.892 & 394.3 \\
153	\midrule
154	3 & 0    & 23.43 & 0.703 & 2.259 & 15.67 \\
155	3 & 0.5  & 25.40 & 0.720 & 2.203 & 17.15 \\
156	3 & 1.0  & 156.94 & 0.886 & 0.795 & 691.4 \\
157	\midrule
158	4 & 0    & 23.41 & 0.703 & 2.259 & 15.67 \\
159	4 & 0.5  & 24.79 & 0.716 & 2.215 & 16.95 \\
160	4 & 1.0  & 155.64 & 0.884 & 0.782 & 839.2 \\
161	\bottomrule
162	\end{tabular}
163	\end{table}
164	
165	%% TODO: plan_001 — expanded table with 6 fractions × 5 seeds (mean ± std), all 5 generations
166	%% TODO: plan_001 — separate table per signal with full numeric precision
167	
168	\subsection{Cross-Generation Trajectories}
169	\label{app:cross_gen_traj}
170	%% Source: mvp_frac50_100 — cross-gen tracking at α = 1.0
171	
172	Table~\ref{tab:crossgen_traj} reports the cross-generation perplexity trajectory at $\alpha = 1.0$, demonstrating super-linear growth.
173	
174	\begin{table}[h]
175	\centering
176	\caption{Perplexity trajectory across 5 generations at $\alpha = 1.0$ (0.5B, WikiText-2, seed~42).}
177	\label{tab:crossgen_traj}
178	\small
179	\begin{tabular}{ccccc}
180	\toprule
181	\textbf{Gen 0} & \textbf{Gen 1} & \textbf{Gen 2} & \textbf{Gen 3} & \textbf{Gen 4} \\
182	\midrule
183	%% Source: mvp_frac50_100
184	15.67 & 136.9 & 394.3 & 691.4 & 839.2 \\
185	\bottomrule
186	\end{tabular}
187	\end{table}
188	
189	%% TODO: plan_001 — full cross-gen trajectories for all signals with mean ± std across 5 seeds
190	%% TODO: plan_001 — cross-gen trajectory figure with error bands
191	
192	
193	\section{Per-Layer Analysis Details}
194	\label{app:per_layer}
195	
196	\subsection{Full Per-Layer Stable Rank Table}
197	\label{app:per_layer_sr}
198	%% Source: per_layer_analysis_v5 — 0.5B, WikiText-2, fractions {0, 0.5}, seed 42, gen 4
199	%% SVD of LoRA weight delta BA for each adapted module
200	
201	Table~\ref{tab:full_per_layer} reports the stable rank change $\Delta\mathrm{SR}$ (50\% contamination minus clean baseline) for all 24 transformer layers and 7 adapted sub-modules.
202	Positive values indicate rank diffusion; negative values indicate rank collapse.
203	
204	\begin{table}[h]
205	\centering
206	\caption{Full per-layer $\Delta\mathrm{SR}$ matrix: 50\% contamination vs.\ clean baseline (0.5B, gen~4, seed~42). Bold entries highlight $|\Delta\mathrm{SR}| > 1.0$.}
207	\label{tab:full_per_layer}
208	\footnotesize
209	\setlength{\tabcolsep}{3pt}
210	\begin{tabular}{lccccccc}
211	\toprule
212	\textbf{Layer} & \texttt{q\_proj} & \texttt{k\_proj} & \texttt{v\_proj} & \texttt{o\_proj} & \texttt{up\_proj} & \texttt{down\_proj} & \texttt{gate\_proj} \\
213	\midrule
214	%% Source: per_layer_results/per_layer_{0,50}pct_gen4.json — ΔSR = SR(50pct) - SR(0pct)
215	L0  & $\mathbf{+2.849}$ & $\mathbf{+2.055}$ & $\mathbf{+1.309}$ & $+0.47$ & $+0.24$ & $\mathbf{+1.361}$ & $+0.39$ \\
216	L1  & $+0.73$ & $+0.69$ & $-0.01$ & $+0.46$ & $+0.05$ & $+0.82$ & $+0.05$ \\
217	L2  & $+0.57$ & $\mathbf{+1.197}$ & $-0.27$ & $+0.03$ & $+0.02$ & $\mathbf{+1.515}$ & $+0.27$ \\
218	\midrule
219	L3  & $+0.95$ & $+0.77$ & $\mathbf{+2.633}$ & $-0.72$ & $+0.06$ & $\mathbf{+1.747}$ & $+0.27$ \\
220	L4  & $\mathbf{+1.129}$ & $\mathbf{+1.757}$ & $\mathbf{+1.824}$ & $+0.03$ & $+0.34$ & $+0.31$ & $+0.77$ \\
221	L5  & $+0.53$ & $\mathbf{+1.446}$ & $\mathbf{+2.441}$ & $-0.09$ & $+0.23$ & $+0.03$ & $+0.78$ \\
222	L6  & $+0.79$ & $+0.51$ & $\mathbf{+1.920}$ & $-0.83$ & $+0.23$ & $+0.54$ & $+0.10$ \\
223	L7  & $+0.24$ & $\mathbf{+1.158}$ & $\mathbf{+1.498}$ & $-0.16$ & $+0.09$ & $+0.56$ & $+0.31$ \\
224	L8  & $+0.99$ & $\mathbf{+1.786}$ & $\mathbf{+1.189}$ & $-0.07$ & $+0.17$ & $+0.55$ & $+0.65$ \\
225	L9  & $+0.76$ & $\mathbf{+1.029}$ & $\mathbf{+1.391}$ & $+0.37$ & $+0.24$ & $+0.45$ & $+0.02$ \\
226	L10 & $+0.72$ & $+0.66$ & $\mathbf{+1.773}$ & $+0.09$ & $-0.12$ & $+0.08$ & $+0.23$ \\
227	\midrule
228	L11 & $-0.10$ & $+0.73$ & $\mathbf{+1.492}$ & $-0.34$ & $+0.32$ & $\mathbf{-2.146}$ & $-0.28$ \\
229	L12 & $+0.35$ & $+0.53$ & $+0.40$ & $-0.74$ & $-0.51$ & $\mathbf{-3.218}$ & $-0.65$ \\
230	\midrule
231	L13 & $+0.92$ & $\mathbf{+1.221}$ & $+0.90$ & $-0.05$ & $-0.63$ & $+0.04$ & $\mathbf{-1.264}$ \\
232	L14 & $+0.21$ & $+0.34$ & $\mathbf{+1.210}$ & $+0.02$ & $-0.38$ & $+0.66$ & $+0.00$ \\
233	L15 & $+0.64$ & $+0.19$ & $+0.86$ & $-0.12$ & $-0.18$ & $\mathbf{+1.550}$ & $-0.21$ \\
234	L16 & $+0.12$ & $+0.12$ & $\mathbf{+3.060}$ & $+0.05$ & $+0.05$ & $\mathbf{+1.849}$ & $-0.39$ \\
235	L17 & $+0.27$ & $+0.08$ & $\mathbf{+1.394}$ & $-0.11$ & $+0.12$ & $\mathbf{+1.551}$ & $+0.08$ \\
236	L18 & $-0.50$ & $-0.08$ & $+0.75$ & $+0.16$ & $-0.18$ & $\mathbf{+1.124}$ & $-0.13$ \\
237	L19 & $+0.25$ & $\mathbf{+1.297}$ & $-0.51$ & $-0.35$ & $+0.12$ & $\mathbf{+1.397}$ & $+0.04$ \\
238	L20 & $+0.78$ & $+0.33$ & $\mathbf{+1.957}$ & $+0.83$ & $-0.07$ & $\mathbf{+2.181}$ & $-0.16$ \\
239	L21 & $+0.13$ & $-0.11$ & $\mathbf{+2.009}$ & $+0.23$ & $-0.06$ & $-0.35$ & $-0.46$ \\
240	L22 & $-0.55$ & $+0.11$ & $\mathbf{+2.401}$ & $-0.05$ & $-0.22$ & $\mathbf{+1.328}$ & $-0.56$ \\
241	L23 & $-0.45$ & $-0.50$ & $+0.45$ & $+0.38$ & $+0.19$ & $+0.89$ & $-0.17$ \\
242	\bottomrule
243	\end{tabular}
244	\end{table}
245	
246	\paragraph{Key observations.}
247	%% Source: per_layer_analysis_v5
248	The table reveals sub-module-specific sensitivity patterns across all layers:
249	\begin{itemize}[nosep]
250	    \item \texttt{v\_proj} exhibits the strongest aggregate diffusion, with $|\Delta\mathrm{SR}| > 1.0$ in 16 of 24 layers and a peak of $+3.060$ at L16.
251	    \item L0 \texttt{q\_proj} shows the largest boundary-layer change ($+2.849$); \texttt{k\_proj} and \texttt{down\_proj} also contribute substantially at L0 ($+2.055$, $+1.361$).
252	    \item L11--L12 \texttt{down\_proj} collapses ($-3.218$ at L12, $-2.146$ at L11), while \texttt{down\_proj} diffuses in other layers (e.g., $+2.181$ at L20, $+1.849$ at L16), indicating layer-specific rather than globally uniform behavior.
253	\end{itemize}
254	
255	\subsection{Weight Norm Analysis}
256	\label{app:weight_norm}
257	%% Source: per_layer_analysis_v5 — weight_norm_crossover_layer = 11
258	
259	Figure~\ref{fig:weight_norm} shows the per-layer Frobenius norm change of the LoRA weight delta $\mathbf{BA}$ between 50\% contamination and clean baseline conditions.
260	
261	\begin{figure}[h]
262	\centering
263	%% TODO: generate actual figure from per_layer_analysis_v5 data
264	\fbox{\parbox{0.9\linewidth}{\centering\vspace{2em}\textit{Placeholder: per-layer $\Delta\|\mathbf{BA}\|_F$ bar chart}\\\textit{(24 layers, contaminated vs.\ clean)}\vspace{2em}}}
265	\caption{Per-layer weight norm change $\Delta\|\mathbf{BA}\|_F$ under 50\% contamination (0.5B, gen~4, seed~42). A crossover occurs at layer~11: early layers (L0--L10) have smaller weight norms under contamination, while late layers (L11--L23) have larger norms. Dashed line marks the crossover boundary.}
266	\label{fig:weight_norm}
267	\end{figure}
268	
269	The crossover at layer~11 suggests that contamination redistributes learning effort from early representation-building layers toward later layers that handle output generation.
270	Early layers shrink (less adaptation needed when input distributions simplify under collapse), while late layers grow (increased effort to map simplified representations to the original vocabulary distribution).
271	
272	
273	\section{Statistical Analysis}
274	\label{app:stats}
275	
276	\subsection{Bootstrap Confidence Intervals}
277	\label{app:bootstrap}
278	
279	We employ clustered bootstrap resampling to compute 95\% confidence intervals for all reported correlations and effect sizes.
280	The cluster unit is the (fraction, seed) pair, yielding $6 \times 5 = 30$ independent clusters in the full experimental design.
281	Within each bootstrap iteration ($B = 10{,}000$ resamples), we resample clusters with replacement and recompute the statistic of interest.
282	This accounts for the within-run dependence across generations: generation $g+1$ trains on data produced by the model from generation $g$, so observations within a (fraction, seed) run are causally linked.
283	
284	Pooling individual generation observations as independent samples would inflate the effective sample size from 30 to 150, producing artificially narrow intervals.
285	Our clustered approach yields conservative but honest intervals that reflect the true experimental degrees of freedom.
286	
287	%% TODO: plan_001 — fill in bootstrap CI values for:
288	%% - Spearman ρ per signal per generation: ρ [95% CI]
289	%% - Effect size (ratio) at α=1.0 vs α=0 per signal: ratio [95% CI]
290	%% - Cross-generation accumulation rate per signal
291	
292	\subsection{Effect Size Summary}
293	\label{app:effect_sizes}
294	
295	%% TODO: plan_001 — complete table with 6-fraction × 5-seed data
296	
297	Table~\ref{tab:effect_sizes_full} reports effect sizes for all signal $\times$ fraction combinations.
298	
299	\begin{table}[h]
300	\centering
301	\caption{Effect sizes at generation~4 relative to clean baseline ($\alpha = 0$). MVP values (seed~42) shown; full design (mean $\pm$ std, Cohen's $d$) pending.}
302	\label{tab:effect_sizes_full}
303	\small
304	\begin{tabular}{lcccccc}
305	\toprule
306	& \multicolumn{6}{c}{\textbf{Contamination fraction} $\alpha$} \\
307	\cmidrule(lr){2-7}
308	\textbf{Signal} & 0 & 0.1 & 0.25 & 0.5 & 0.75 & 1.0 \\
309	\midrule
310	%% Source: mvp_frac50_100 (fractions 0, 0.5, 1.0 only)
311	SR (ratio) & 1.00$\times$ & --- & --- & 1.06$\times$ & --- & 6.6$\times$ \\
312	SE ($\Delta\%$) & 0 & --- & --- & $+1.8\%$ & --- & $+25.7\%$ \\
313	TE ($\Delta\%$) & 0 & --- & --- & $-1.9\%$ & --- & $-65.4\%$ \\
314	PPL (ratio) & 1.00$\times$ & --- & --- & 1.08$\times$ & --- & 53$\times$ \\
315	\midrule
316	%% TODO: plan_001 — Cohen's d rows
317	$d_\text{SR}$ & --- & --- & --- & --- & --- & --- \\
318	$d_\text{SE}$ & --- & --- & --- & --- & --- & --- \\
319	$d_\text{TE}$ & --- & --- & --- & --- & --- & --- \\
320	$d_\text{PPL}$ & --- & --- & --- & --- & --- & --- \\
321	\bottomrule
322	\end{tabular}
323	\end{table}
324	
325	%% TODO: plan_001 — fill all cells with mean ± std and Cohen's d from 5-seed data
326	
327	
328	\section{Within-Generation Temporal Analysis}
329	\label{app:within_gen}
330	
331	\subsection{Full Deviation Curves}
332	\label{app:deviation_curves}
333	%% Source: within_gen_analysis — 0.5B, WikiText-2, step-level temporal analysis
334	
335	Table~\ref{tab:deviation_step50} reports the relative deviation $\Delta_s$ (Eq.~\ref{eq:deviation}) at step~50 for all signals and available fractions.
336	
337	\begin{table}[h]
338	\centering
339	\caption{Relative deviation $\Delta_s$ at step~50 (${\sim}3\%$ training progress) for $\alpha = 1.0$ vs.\ $\alpha = 0$ (0.5B, WikiText-2, seed~42). Signals exceeding 5\% threshold marked with \checkmark.}
340	\label{tab:deviation_step50}
341	\small
342	\begin{tabular}{lccl}
343	\toprule
344	\textbf{Signal} & $\Delta_s$ at step 50 & ${>}\,5\%$? & \textbf{First step ${>}\,5\%$} \\
345	\midrule
346	%% Source: within_gen_analysis — signals_above_5pct_at_step50
347	Stable rank      & 34.4\% & \checkmark & step 50 (${\sim}3\%$) \\
348	Token entropy    & 24.5\% & \checkmark & step 50 (${\sim}3\%$) \\
349	Perplexity       & 17.7\% & \checkmark & step 50 (${\sim}3\%$) \\
350	Spectral entropy & 5.0\%  & borderline & step 100 (${\sim}6\%$) \\
351	Gradient norm    & 2.1\%  & ---        & step 100 (${\sim}6\%$) \\
352	\bottomrule
353	\end{tabular}
354	\end{table}
355	
356	%% TODO: plan_004 — 1.5B within-generation deviation curves
357	%% TODO: plan_004 — full deviation table: all signals × all fractions × all generations at steps {50, 100, 200, 500, 1000, 1540}
358	%% TODO: plan_004 — deviation trajectory figure: Δ_s(t) for each signal, multi-panel (one per generation)
359	
360	\subsection{Detection Threshold Sensitivity}
361	\label{app:threshold}
362	
363	%% TODO: plan_005 — AUROC vs. threshold sweep
364	%% TODO: plan_005 — threshold sensitivity analysis: how does detection performance vary as the deviation threshold varies from 1% to 20%?
365	%% TODO: plan_005 — ROC curves with proper clustered bootstrap CIs
366	
367	The detection threshold of 5\% used in Section~\ref{sec:early_warning_results} was chosen as a practically meaningful deviation from baseline.
368	We plan to evaluate sensitivity to this choice by sweeping the threshold from 1\% to 20\% and reporting AUROC at each level, using clustered bootstrap to account for non-independence of observations within a (fraction, seed) run.
369	
370	
371	\section{Competitor Comparison}
372	\label{app:competitor_comparison}
373	
374	\input{tables/competitor_comparison}
375	
376	
377	\section{Terminal Spectral Convergence}
378	\label{app:terminal_convergence}
379	
380	At generation~4, $\alpha = 1.0$, terminal stable rank values are $\mathrm{SR} = 153.87$ (full fine-tuning) versus $155.64$ (QLoRA)---a 1.2\% difference despite markedly different collapse dynamics (onset ratio $15.3\times$ vs $8.7\times$; terminal $\mathrm{PPL}_\text{eval}$ of $326.19$ vs $839.2$).
381	This observation rests on $N = 1$ seed per method and cannot be distinguished from coincidence.
382	If real, it would suggest that iterative synthetic contamination drives representations toward a method-independent attractor in spectral space---a convergence in representational structure despite divergent output-level severity.
383	Multi-seed validation is required before this can be treated as anything more than speculation.
384	
385	
386	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eae4b8c3-97b1-40f4-a325-6cb317d41a91",
  "isSidechain": true,
  "promptId": "80dd2a4d-c31a-43ae-8316-4a6135d9fed6",
  "agentId": "ade4d670d78b2afaf",
  "type": "user",
  "uuid": "af56072d-e9c7-4e0a-bfb2-4eec83ffaaa6",
  "sourceToolAssistantUUID": "eae4b8c3-97b1-40f4-a325-6cb317d41a91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-16T10:43:18.003Z_

Now let me read the dream review to understand what prior reviewers flagged.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af56072d-e9c7-4e0a-bfb2-4eec83ffaaa6",
  "isSidechain": true,
  "agentId": "ade4d670d78b2afaf",
  "requestId": "req_011Cb67JoWu8q1X5Trvauuv4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a5cb32a9-05a4-4a6d-b31e-0c699818bcdf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UFqpSUhenPzc1tkuncFUeQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16408,
      "cache_read_input_tokens": 76138,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16408,
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

_source line 50 · 2026-05-16T10:43:20.358Z_

<details open><summary>🔧 Tool call — Read · `toolu_017JURJx9C5mXR36AaCmuiqg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/median/paper.tex",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5cb32a9-05a4-4a6d-b31e-0c699818bcdf",
  "isSidechain": true,
  "agentId": "ade4d670d78b2afaf",
  "requestId": "req_011Cb67JoWu8q1X5Trvauuv4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d375afd3-6c8d-4f88-93b9-6212986699c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UFqpSUhenPzc1tkuncFUeQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16408,
      "cache_read_input_tokens": 76138,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16408,
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

_source line 51 · 2026-05-16T10:43:20.367Z_

<details><summary>↩ Tool result · `toolu_017JURJx9C5mXR36AaCmuiqg`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage{amsmath,amssymb}
4	\usepackage{booktabs}
5	\usepackage{graphicx}
6	\usepackage{hyperref}
7	\usepackage{xcolor}
8	\usepackage[margin=1in]{geometry}
9	\usepackage{multirow}
10	\usepackage{array}
11	
12	\title{Training Dynamic Signals as Model Collapse Severity Monitors:\\A Systematic Multi-Axis Empirical Analysis}
13	
14	\author{Anonymous}
15	
16	\date{}
17	
18	\begin{document}
19	
20	\maketitle
21	
22	\begin{abstract}
23	Model collapse from iterative training on synthetic data poses a growing risk as LLM-generated text pervades training corpora. We conduct a systematic empirical analysis of training dynamic signals as collapse severity monitors across 4 signal families (spectral, output, gradient, downstream), 6 contamination levels, 2 model scales (0.5B and 1.5B), 2 text domains, and 2 fine-tuning methods (QLoRA and Full FT). We find that signals exhibit generally monotonic correlation with collapse severity (Spearman $\rho \geq 0.87$) with occasional non-monotonicity at intermediate fractions, and bootstrap confidence interval lower bounds exceeding 0.8. For within-generation early warning, stable rank achieves AUC = 0.88 [0.80, 0.94] at 1.5B scale, with sensitivity amplitude decreasing at larger scales; notably, held-out evaluation perplexity---the metric practitioners most commonly check---provides no within-generation early warning (AUC = 0.55, CI crossing 0.5). We document that the same monitoring signal can be informative under one training method and misleading under another: perplexity and downstream metrics diverge under parameter-efficient fine-tuning, cautioning against single-signal monitoring. Cross-family validation on LLaMA-3.2-1B confirms directional consistency for 7/11 signals (preliminary, $N$=1). We release a signal operating-range taxonomy to guide practitioners in selecting appropriate collapse indicators.
24	\end{abstract}
25	
26	\section{Introduction}
27	
28	Model collapse---the progressive degradation of language models trained iteratively on their own outputs---has been characterized theoretically \cite{shumailov2024ai,alemohammad2024self,dohmatob2024tale} and empirically \cite{briesch2023large,hataya2023will}. As LLM-generated content becomes pervasive in web-scraped training corpora, practitioners face a practical question: \emph{how can collapse be detected and quantified during training, before catastrophic quality loss?}
29	
30	Existing approaches address parts of this problem. SIGMA \cite{anonymous2025sigma} monitors output embedding spectral properties but requires a clean reference distribution. Kalinowski et al.~\cite{kalinowski2024tda} employ topological data analysis but at prohibitive computational cost. Data mixing strategies \cite{gerstgrasser2024model,kazdan2024collapse} study prevention rather than detection. None provide a systematic comparison of which training-time signals best track collapse severity across contamination levels, nor examine within-generation temporal dynamics for early warning.
31	
32	We conduct the first systematic multi-axis comparison of training-time signal families as collapse severity monitors in iterative fine-tuning. Our contributions:
33	
34	\begin{enumerate}
35	    \item We demonstrate that spectral and output signals generally maintain monotonic correlation with collapse severity across contamination fractions and generations, with bootstrap CI lower bounds $> 0.8$ (Section~\ref{sec:correlation}).
36	    \item We show that stable rank provides within-generation early warning (AUC = 0.85--0.93 across scales) but with sensitivity amplitude decreasing at larger model scales; stable rank is the most sensitive but seed-variable signal, and practitioners should combine it with training loss for robustness. Held-out evaluation perplexity is ineffective for within-generation detection (Section~\ref{sec:early_warning}).
37	    \item We characterize non-uniform signal behavior across training methods and propose a signal operating-range taxonomy (Section~\ref{sec:taxonomy}).
38	\end{enumerate}
39	
40	\section{Method}
41	\label{sec:method}
42	
43	\subsection{Experimental Setup}
44	
45	\paragraph{Models.} Qwen2.5-0.5B and Qwen2.5-1.5B (QLoRA, rank=16, $\alpha$=32), with Full FT comparison on 0.5B. Cross-family validation on LLaMA-3.2-1B.
46	
47	\paragraph{Collapse Protocol.} We fine-tune model $M_g$ on a mixture of real data and synthetic data generated by $M_{g-1}$, iterating for $G=5$ generations. Contamination fractions: $f \in \{0\%, 10\%, 25\%, 50\%, 75\%, 100\%\}$. Each generation trains from $M_{g-1}$ (not from $M_0$). Seeds: 4 seeds for WikiText-2, 3 seeds for PubMed.
48	
49	\paragraph{Synthetic Data Generation.} Temperature 0.7, top-$p$ = 0.9, max length 512 tokens, prompted with real text prefixes from the training domain.
50	
51	\paragraph{Domains.} WikiText-2 (general) and PubMed abstracts (biomedical).
52	
53	\subsection{Signal Definitions}
54	
55	We monitor four signal families across training:
56	
57	\paragraph{Spectral Signals.}
58	\begin{itemize}
59	    \item \textbf{Stable rank} (SR): $\|W\|_F^2 / \|W\|_2^2$, computed on QLoRA adapter weight matrices. Under collapse, $\|W\|_F^2$ grows faster than $\sigma_1^2$, causing SR to \emph{increase} (energy dispersal, not concentration).
60	    \item \textbf{Spectral entropy} (SE): Shannon entropy of normalized singular values of adapter weights.
61	\end{itemize}
62	
63	\paragraph{Output Signals.}
64	\begin{itemize}
65	    \item \textbf{Held-out evaluation perplexity} (PPL): $\exp(\text{mean NLL})$ on a fixed held-out validation set, computed in \texttt{model.eval()} mode every 50 steps.
66	    \item \textbf{Training loss} (TL): Running average cross-entropy on the training set (containing synthetic mixtures), logged every 50 steps.
67	    \item \textbf{Token entropy} (TE): Shannon entropy of the output token distribution.
68	\end{itemize}
69	
70	\paragraph{Gradient Signals.}
71	\begin{itemize}
72	    \item \textbf{Gradient norm}: $L_2$ norm of gradients over trainable parameters.
73	\end{itemize}
74	
75	\paragraph{Downstream Signals.}
76	\begin{itemize}
77	    \item \textbf{HellaSwag}: 4-choice commonsense reasoning accuracy.
78	    \item \textbf{MMLU-mini}: 100-question knowledge evaluation across 4 subjects.
79	\end{itemize}
80	
81	\section{Signal--Severity Correlation}
82	\label{sec:correlation}
83	
84	\subsection{Cross-Generation Monotonicity}
85	
86	Table~\ref{tab:cross_config_auc} presents within-generation detection AUC across configurations and scales. Core spectral and output signals maintain directional consistency across all tested configurations. For the 4 core signals (stable rank, spectral entropy, perplexity, token entropy), Spearman $\rho = 1.0$ for cross-fraction ordering at 100\% contamination across both Qwen scales and LLaMA (Table~\ref{tab:llama_direction}).
87	
88	Bootstrap confidence intervals (clustered by seed, 2000 resamples) confirm that correlation lower bounds exceed 0.8 for stable rank and training loss across both WikiText and PubMed domains at 1.5B scale (Table~\ref{tab:cross_config_auc}).
89	
90	\begin{table}[t]
91	\centering
92	\caption{Within-generation detection AUC across configurations with 95\% bootstrap CIs (clustered by seed). Bold: statistically significant (CI lower $> 0.5$).}
93	\label{tab:cross_config_auc}
94	\small
95	\begin{tabular}{lcccc}
96	\toprule
97	Signal & WikiText 0.5B & WikiText 1.5B & PubMed 1.5B & Consistency \\
98	\midrule
99	Stable rank & 0.984 & \textbf{0.89 [0.81, 0.94]} & \textbf{0.86 [0.77, 0.93]} & Consistent (attenuated) \\
100	Training loss & 0.923 & \textbf{0.83 [0.74, 0.90]} & \textbf{0.80 [0.70, 0.88]} & Consistent (attenuated) \\
101	Perplexity & 0.534 & 0.56 [0.44, 0.66] & 0.52 [0.41, 0.63] & Near random \\
102	Spectral entropy & 0.58 & 0.62 [0.50, 0.72] & 0.59 [0.47, 0.70] & Weak \\
103	Token entropy & 0.478 & 0.51 [0.40, 0.62] & 0.49 [0.38, 0.60] & Near random \\
104	\bottomrule
105	\end{tabular}
106	\end{table}
107	
108	\subsection{Per-Layer Collapse Propagation}
109	
110	Analysis of 28 layers $\times$ 7 sub-modules in the 1.5B model (Table~\ref{tab:submodule}) reveals a sub-module-centric collapse pattern. The \texttt{v\_proj} sub-module is the most sensitive indicator (mean $\Delta$SR = +4.2, rank 1 in 2/3 seeds), consistent with 0.5B findings. Collapse propagates in a ``late $\to$ mid $\to$ early'' layer sequence: layers 22--27 show earliest divergence, followed by layers 12--18, then layers 0--5. The \texttt{down\_proj} sub-module exhibits localized rank \emph{collapse} (SR decrease of $-4.8$ at layers 22--25), consistent with FFN bottleneck vulnerability at $\sim$80\% network depth.
111	
112	\begin{table}[t]
113	\centering
114	\caption{Sub-module sensitivity ranking at 1.5B (100\% contamination, $N$=3 seeds).}
115	\label{tab:submodule}
116	\small
117	\begin{tabular}{lcccl}
118	\toprule
119	Sub-module & Mean $\Delta$SR & Std & Rank & 0.5B Consistent \\
120	\midrule
121	v\_proj & +4.2 & 1.1 & 1 & \checkmark \\
122	q\_proj & +1.4 & 0.6 & 2 & \checkmark \\
123	k\_proj & +1.1 & 0.8 & 3 & \checkmark \\
124	up\_proj & +0.8 & 0.4 & 4 & \checkmark \\
125	gate\_proj & +0.5 & 0.3 & 5 & \checkmark \\
126	o\_proj & +0.3 & 0.2 & 6 & \checkmark \\
127	down\_proj & $-3.2$ & 1.5 & -- (collapse) & \checkmark \\
128	\bottomrule
129	\end{tabular}
130	\end{table}
131	
132	Cross-seed consistency is imperfect: 1/3 seeds shows \texttt{k\_proj} co-dominant with \texttt{v\_proj}. We characterize \texttt{v\_proj} as the ``predominant'' rather than ``universal'' most-sensitive sub-module.
133	
134	\section{Within-Generation Early Warning}
135	\label{sec:early_warning}
136	
137	\subsection{Formal AUROC Statistics at 1.5B Scale}
138	
139	Table~\ref{tab:formal_auroc} presents within-generation binary AUROC with clustered bootstrap CIs ($N$=4 seeds, 2000 resamples). Stable rank achieves AUC = 0.88 [0.80, 0.94], statistically significant for within-generation detection (CI lower bound $> 0.5$). Training loss is the second significant detector (AUC = 0.82 [0.73, 0.89]).
140	
141	\begin{table}[t]
142	\centering
143	\caption{Formal within-generation AUROC at 1.5B with 95\% bootstrap CIs.}
144	\label{tab:formal_auroc}
145	\small
146	\begin{tabular}{lcccc}
147	\toprule
148	Signal & AUC Mean & CI Lower & CI Upper & Significant \\
149	\midrule
150	Stable rank & 0.88 & 0.80 & 0.94 & Yes \\
151	Training loss & 0.82 & 0.73 & 0.89 & Yes \\
152	Spectral entropy & 0.61 & 0.48 & 0.72 & No \\
153	Perplexity & 0.55 & 0.43 & 0.65 & No \\
154	Token entropy & 0.50 & 0.39 & 0.61 & No \\
155	\bottomrule
156	\end{tabular}
157	\end{table}
158	
159	\subsection{Scale Attenuation}
160	
161	Sensitivity amplitude systematically decreases with model scale. At 0.5B ($N$=1), stable rank achieves AUC = 0.984; at 1.5B ($N$=4), AUC = 0.88---a 10.6\% attenuation. The 0.5B point estimate falls outside the 1.5B 95\% CI, confirming that scale attenuation is a real effect rather than sampling noise. This is consistent with larger parameter spaces absorbing adapter perturbations: QLoRA modifies $\sim$2\% of parameters, and the same contamination-induced spectral disturbance is diluted by a larger frozen parameter space.
162	
163	\subsection{Temporal Divergence Profile}
164	
165	Table~\ref{tab:divergence} shows relative divergence from baseline at successive training steps (1.5B, WikiText). Stable rank diverges earliest (21\% at step 50) and most strongly (71\% at step 500). Training loss follows with moderate early divergence (15\% at step 50). Perplexity, spectral entropy, and token entropy show negligible early divergence ($\leq$4\% at step 50).
166	
167	\begin{table}[t]
168	\centering
169	\caption{Relative divergence (\%) from 0\%-contamination baseline by training step (1.5B, $N$=4 seeds). Seed CV in parentheses.}
170	\label{tab:divergence}
171	\small
172	\begin{tabular}{lccccc}
173	\toprule
174	Signal & Step 50 & Step 100 & Step 200 & Step 500 & AUC \\
175	\midrule
176	Stable rank & 21 (0.045) & 34 & 52 & 71 & 0.89 \\
177	Training loss & 15 (0.028) & 28 & 41 & 58 & 0.83 \\
178	Spectral entropy & 2 (0.022) & 5 & 9 & 18 & 0.62 \\
179	Perplexity & 4 (0.035) & 8 & 12 & 19 & 0.56 \\
180	Token entropy & 3 (0.041) & 6 & 11 & 15 & 0.51 \\
181	\bottomrule
182	\end{tabular}
183	\end{table}
184	
185	\subsection{Held-Out Perplexity Fails at Within-Generation Detection}
186	
187	A key practitioner-relevant finding: held-out evaluation perplexity---the metric most commonly checked at eval checkpoints---provides no within-generation early warning. Its AUC of 0.55 [0.43, 0.65] is statistically indistinguishable from random (CI crosses 0.5). This holds across both WikiText and PubMed domains (AUC = 0.56 and 0.52, respectively).
188	
189	The mechanism is straightforward: QLoRA fine-tuning modifies only $\sim$2\% of parameters, and within a single generation the adapter's influence on held-out distribution predictions is minimal. Collapse effects on held-out PPL require multi-generation accumulation. In contrast, training loss (AUC = 0.82) directly measures learning dynamics on the contaminated distribution and detects distribution shift within a single run.
190	
191	This creates a monitoring blind spot: practitioners who rely solely on held-out PPL at checkpoints will miss within-generation collapse signals entirely. Stable rank and training loss are the appropriate within-generation indicators.
192	
193	\subsection{Threshold Calibration}
194	
195	Table~\ref{tab:threshold} presents operating points for practical deployment. A combined threshold (stable rank $>$ 10\% deviation OR training loss $>$ 8\% deviation) achieves sensitivity 0.85 at specificity 0.90, detecting contamination fractions as low as 10\% by step 100. Individual thresholds offer higher specificity (0.95) but lower sensitivity (0.72) and require at least 25\% contamination for detection.
196	
197	\begin{table}[t]
198	\centering
199	\caption{Threshold operating points for within-generation collapse detection.}
200	\label{tab:threshold}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d375afd3-6c8d-4f88-93b9-6212986699c1",
  "isSidechain": true,
  "promptId": "80dd2a4d-c31a-43ae-8316-4a6135d9fed6",
  "agentId": "ade4d670d78b2afaf",
  "type": "user",
  "uuid": "9311bb1c-ae18-46ea-a62d-657093758541",
  "sourceToolAssistantUUID": "d375afd3-6c8d-4f88-93b9-6212986699c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-16T10:43:20.859Z_

<details open><summary>🔧 Tool call — Read · `toolu_011cMFrPSkQVUHFpnCDTtqHF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/tables/competitor_comparison.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9311bb1c-ae18-46ea-a62d-657093758541",
  "isSidechain": true,
  "agentId": "ade4d670d78b2afaf",
  "requestId": "req_011Cb67JoWu8q1X5Trvauuv4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "90d6c11b-96f2-4d9b-ab8c-c70cb701c53b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UFqpSUhenPzc1tkuncFUeQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16408,
      "cache_read_input_tokens": 76138,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16408
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 206,
          "cache_read_input_tokens": 76138,
          "cache_creation_input_tokens": 16408,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16408,
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

_source line 53 · 2026-05-16T10:43:20.872Z_

<details><summary>↩ Tool result · `toolu_011cMFrPSkQVUHFpnCDTtqHF`</summary>

```text
1	% Requires: \usepackage{booktabs, xcolor, amssymb, adjustbox}
2	% Define symbols if not already defined:
3	% \newcommand{\cmark}{\ding{51}}  % or use \checkmark
4	% \newcommand{\xmark}{\ding{55}}  % or use $\times$
5	\providecommand{\cmark}{\checkmark}
6	\providecommand{\xmark}{$\times$}
7	\providecommand{\pmark}{\textcolor{gray}{partial}}
8	
9	\begin{table*}[t]
10	\centering
11	\caption{
12	Comparison of collapse monitoring approaches.
13	\cmark\ = fully supported, \xmark\ = not supported, \pmark\ = partially addressed.
14	SIGMA operates on output embeddings post-hoc; Kalinowski monitors topology online but in a different setting.
15	Our work is the first to combine online spectral/entropic monitoring with per-layer granularity
16	and early warning in the iterative synthetic data setting.
17	}
18	\label{tab:competitor_comparison}
19	\begin{adjustbox}{max width=\textwidth}
20	\begin{tabular}{@{}lccc@{}}
21	\toprule
22	\textbf{Capability} & \textbf{SIGMA} & \textbf{Kalinowski} & \textbf{Ours} \\
23	 & \citep{Gu2026} & \citep{Kalinowski2026} & \\
24	\midrule
25	Signal type
26	  & Gram matrix spectrum
27	  & Persistent homology
28	  & \parbox{4cm}{Weight spectrum + output entropy/PPL + gradient norm} \\[4pt]
29	Online monitoring
30	  & \xmark\ (post-hoc)
31	  & \cmark
32	  & \cmark \\[2pt]
33	Clean reference needed
34	  & \cmark\ (required)
35	  & \xmark
36	  & \xmark \\[2pt]
37	Multi-signal comparison
38	  & \xmark\ (spectrum only)
39	  & \xmark\ (topology only)
40	  & \cmark\ (4 signal families) \\[2pt]
41	Cross-scale validation
42	  & \xmark
43	  & \xmark
44	  & \pmark\textsuperscript{a}\ (0.5B) \\[2pt]
45	Cross-domain validation
46	  & \xmark
47	  & \xmark
48	  & \pmark\textsuperscript{b}\ (WikiText) \\[2pt]
49	Per-layer analysis
50	  & \xmark
51	  & \xmark
52	  & \cmark \\[2pt]
53	Early warning
54	  & \xmark
55	  & \pmark\ (different setting)
56	  & \cmark\ (3\% training progress) \\[2pt]
57	Iterative collapse focus
58	  & \xmark
59	  & \xmark
60	  & \cmark\ (5 generations) \\[2pt]
61	Statistical rigor
62	  & N/A
63	  & N/A
64	  & \pmark\textsuperscript{c}\ (1 seed) \\
65	\bottomrule
66	\multicolumn{4}{@{}l}{\footnotesize
67	\textsuperscript{a}1.5B validation in progress.\quad
68	\textsuperscript{b}PubMed experiments planned.\quad
69	\textsuperscript{c}5-seed validation in progress; MVP uses 1 seed.}\\
70	\end{tabular}
71	\end{adjustbox}
72	\end{table*}
73	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "90d6c11b-96f2-4d9b-ab8c-c70cb701c53b",
  "isSidechain": true,
  "promptId": "80dd2a4d-c31a-43ae-8316-4a6135d9fed6",
  "agentId": "ade4d670d78b2afaf",
  "type": "user",
  "uuid": "40d612e4-f0d4-4fa0-8766-58827ceebbbe",
  "sourceToolAssistantUUID": "90d6c11b-96f2-4d9b-ab8c-c70cb701c53b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 54 · 2026-05-16T10:43:24.483Z_

Now I have enough information to write a thorough R2 review. Let me also quickly check the LLaMA-related claims and the cross-scale data since those are mentioned in the task description.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40d612e4-f0d4-4fa0-8766-58827ceebbbe",
  "isSidechain": true,
  "agentId": "ade4d670d78b2afaf",
  "requestId": "req_011Cb67KDBSSN5aX3AkCe1Lj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "81aa33e7-cd3f-4e71-b834-327cbb56733a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BLqRncyc88tz57h4NWvfdz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6055,
      "cache_read_input_tokens": 92546,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6055,
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

_source line 55 · 2026-05-16T10:43:25.190Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01BgxtrCGLve1NBwvRkmdrY7`</summary>

```json
{
  "project": "collapse_severity_monitor",
  "file": "writing_plan.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81aa33e7-cd3f-4e71-b834-327cbb56733a",
  "isSidechain": true,
  "agentId": "ade4d670d78b2afaf",
  "requestId": "req_011Cb67KDBSSN5aX3AkCe1Lj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "98f77a39-268f-4928-b07d-5530eecd4077",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BLqRncyc88tz57h4NWvfdz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6055,
      "cache_read_input_tokens": 92546,
      "output_tokens": 152,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6055
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 152,
          "cache_read_input_tokens": 92546,
          "cache_creation_input_tokens": 6055,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6055,
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

_source line 56 · 2026-05-16T10:43:25.203Z_

<details><summary>↩ Tool result · `toolu_01BgxtrCGLve1NBwvRkmdrY7`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/writing_plan.yaml\", \"content\": \"# Writing Plan — collapse_severity_monitor\\n# Generated: 2026-05-15T20:00:00Z by Paper Agent\\n# Status: PENDING DIRECTOR APPROVAL\\n\\nmeta:\\n  venue: \\\"EMNLP 2026 (via ACL Rolling Review)\\\"\\n  track: long paper\\n  template: templates/latex/acl2025/\\n  template_note: \\\"ARR 2026 uses ACL style files. Need to download/verify latest version from acl-org/acl-style-files.\\\"\\n  page_limit: 8  # + unlimited references + limitations/ethics appendix\\n  deadline: 2026-05-25\\n  core_claim: >\\n    Training dynamic signals provide complementary early warning for model collapse —\\n    stable rank detects within-generation collapse (AUC=0.984 at 10% training progress)\\n    while perplexity tracks cross-generation severity — but the same signal can be\\n    informative under one training method and misleading under another.\\n  created_at: 2026-05-15T20:00:00Z\\n  verify_refs: true\\n  data_strategy: >\\n    D030: write data-independent chapters first (method, related_work);\\n    Results uses available data (MVP + plan003 + plan006 + plan008 + within_gen_analysis);\\n    plan001/002/010 data patched in when complete (ETA 5/18-19).\\n\\npaper_outline:\\n  - section: abstract\\n    word_budget: 250\\n    core_bullets:\\n      - \\\"Problem: Model collapse from iterative synthetic data training is a growing concern, but practitioners lack actionable signals to detect and quantify collapse severity during training\\\"\\n      - \\\"Approach: Systematic empirical analysis of 4 signal families (spectral, output, gradient, downstream) × 6 contamination levels × 2 model scales × 2 domains × 2 fine-tuning methods\\\"\\n      - \\\"Result C1: Spectral and output signals reliably track collapse severity across configurations (effect sizes elevated as primary evidence)\\\"\\n      - \\\"Result C2: Stable rank detects within-generation collapse (AUC=0.984), reaching actionable sensitivity at 10% training progress; notably, training perplexity provides no within-generation early warning (AUC=0.534)\\\"\\n      - \\\"Result C3: The same signal can be informative under one training method and misleading under another; signal taxonomy showing complementary operating ranges\\\"\\n      - \\\"Takeaway: No single signal suffices across all detection contexts; we provide an empirical signal taxonomy to guide practitioner monitoring decisions\\\"\\n    dependencies: [results, method, introduction]\\n\\n  - section: introduction\\n    word_budget: 900\\n    core_bullets:\\n      - \\\"Hook: As LLM-generated text pervades training corpora, iterative training on synthetic data causes model collapse — but the most commonly monitored metric (training perplexity) is nearly blind to it within a training run (AUC=0.534 ≈ random)\\\"\\n      - \\\"Gap: Existing work characterizes collapse theoretically (Shumailov et al. 2024, Dohmatob et al. 2024) or proposes mitigation via data management (Gerstgrasser et al. 2024), but no systematic analysis exists of which training-time signals best track collapse severity, when they provide early warning, and where they mislead\\\"\\n      - \\\"Insight: Different signal families have complementary operating ranges — and the same signal's utility can flip from informative to misleading depending on training method\\\"\\n      - \\\"Contributions: [C1] Signal-severity correlation validated across contamination levels, model scales, text domains, and fine-tuning methods; [C2] Within-generation early warning capability — stable rank achieves AUC=0.94 at just 10% training progress; [C3] Signal taxonomy characterizing operating ranges, method-dependence, and failure modes\\\"\\n    dependencies: [results]\\n    citation_hints:\\n      - \\\"shumailov_nature2024: model collapse definition and Nature visibility\\\"\\n      - \\\"alemohammad_iclr2024: self-consuming generative models MAD\\\"\\n      - \\\"dohmatob_iclr2025: strong model collapse (any nonzero fraction)\\\"\\n      - \\\"gerstgrasser_2024: data accumulation avoids collapse\\\"\\n      - \\\"sigma_2026: spectral monitoring (differentiate)\\\"\\n      - \\\"schaeffer_2025: collapse definition taxonomy (adopt their framing)\\\"\\n    figures: [fig1_framework]\\n\\n  - section: related_work\\n    word_budget: 700\\n    core_bullets:\\n      - \\\"Cluster 1 — Model Collapse Theory & Empirics: Shumailov 2024, Dohmatob 2024/2025, Alemohammad 2024, Shi 2025, Seddik 2024, Fu 2024 → characterize when/why collapse happens; Gerstgrasser 2024, Kazdan 2024, Feng 2025 → mitigation via data management. Gap: post-hoc analysis, no online detection\\\"\\n      - \\\"Cluster 2 — Spectral & Topological Monitoring: SIGMA (Gu et al. 2026) monitors output embedding Gram matrix spectrum — post-hoc, requires clean reference, no per-layer. Kalinowski 2026 uses persistent homology — different signal family, not studied in iterative synthetic data setting. Martin & Mahoney 2021 (WeightWatcher) establishes stable rank as model quality predictor\\\"\\n      - \\\"Cluster 3 — Synthetic Data Detection: Watermarking (Kirchenbauer 2023, Dathathri 2024), DetectGPT (Mitchell 2023), Min-K% (Shi 2024) → detect presence of synthetic data, orthogonal to severity quantification\\\"\\n      - \\\"Cluster 4 — Training Dynamics: Spectral Lens (Liu et al. 2026), Kalra et al. 2026, Yunis et al. 2024 → spectral/dynamics methods for optimization diagnostics, not collapse monitoring\\\"\\n      - \\\"Our position: first systematic multi-axis comparison of training-time signal families as collapse severity monitors in iterative fine-tuning setting\\\"\\n    dependencies: [introduction]\\n\\n  - section: method\\n    word_budget: 1100\\n    core_bullets:\\n      - \\\"§3.1 Iterative Training Protocol: fine-tune M₀ (pretrained) → M₁ → ... → M_g using synthetic data from M_{g-1}. Each generation: QLoRA/Full FT on dataset mixed with synthetic at fraction α. Document: temperature, top-p, max_length, prompt format, gen_num_chunks\\\"\\n      - \\\"§3.2 Contamination Fractions: α ∈ {0%, 10%, 25%, 50%, 75%, 100%}. 0% = clean baseline (controls for training noise). 100% = full replacement (maximum collapse).\\\"\\n      - \\\"§3.3 Monitoring Signals — 4 families: (a) Spectral: stable_rank (SR = ‖W‖²_F/‖W‖², ↑ under collapse = energy dispersal, not concentration), spectral_entropy (H_s = −Σ p_i log p_i, p_i = σ²_i/Σσ²_j); (b) Output: perplexity (training PPL vs held-out evaluation PPL — explicitly distinguish), token_entropy; (c) Gradient: gradient_norm; (d) Downstream: HellaSwag accuracy\\\"\\n      - \\\"§3.4 Experimental Configurations: Table 4. Models: Qwen2.5-0.5B, 1.5B, (3B spot-check). Datasets: WikiText-2, PubMed. Methods: QLoRA (r=16, α=32), Full FT. Seeds: 5 (WikiText 1.5B), 3 (PubMed), 1 (Full FT, 3B)\\\"\\n      - \\\"§3.5 Evaluation Framework: (a) Cross-gen severity: Spearman ρ + bootstrap CI, Cohen's d effect sizes (primary evidence); (b) Within-gen detection: ROC with clustered bootstrap (one observation per fraction×seed to avoid inflating AUC from serial generation dependence); (c) Method-dependence: paired comparison across QLoRA/Full FT\\\"\\n    dependencies: []\\n    notation_table:\\n      M_g: \\\"model at generation g\\\"\\n      α: \\\"synthetic data contamination fraction\\\"\\n      SR: \\\"stable rank = ‖W‖²_F / ‖W‖²_op\\\"\\n      H_s: \\\"spectral entropy of singular value distribution\\\"\\n      PPL_train: \\\"training perplexity (on current batch)\\\"\\n      PPL_eval: \\\"evaluation perplexity (on held-out clean set)\\\"\\n    tables: [tab4_config]\\n    registry_refs: [mvp_frac50_100, plan001-wikitext-15B-5seeds, plan002-pubmed-cqa1, plan003-fullft-05B, plan010-3B-spotcheck]\\n\\n  - section: results\\n    word_budget: 1800\\n    core_bullets:\\n      - \\\"§4.1 Signal-Severity Correlation (C1): Effect size tables as primary evidence — spectral_entropy d=33.48 (most robust, CV=0.0015), perplexity d=20.82, stable_rank d=9.43 (seed-sensitive). Cross-gen Spearman ρ supporting. 6/7 signals direction-consistent across QLoRA/Full FT. [TODO plan001] 1.5B × 5 seeds for proper CI. [TODO plan002] PubMed cross-domain.\\\"\\n      - \\\"§4.2 Within-Generation Early Warning (C2): (a) stable_rank: AUC=0.984 [0.978,0.989], reaches AUC=0.94 (sens=0.78, spec=1.00) at 10% training progress. training_loss second-best (AUC=0.923). (b) DEDICATED PARAGRAPH: PPL within-gen failure (AUC=0.534 ≈ random) — mechanistic explanation: training PPL measures fit to potentially contaminated data, not representation structural change; model 'successfully' fits corrupted distribution. (c) spectral_entropy non-monotonic within-gen (AUC dips to 0.30 at 20%), unsuitable for threshold-based early detection. ROC data N=1 seed/0.5B — [TODO plan001] validation.\\\"\\n      - \\\"§4.3 Signal Taxonomy & Non-Uniform Behavior (C3): (a) Taxonomy table (tab1) with operating ranges + method-dependence column. Three-tier strategy: stable_rank→within-gen alarm, perplexity→cross-gen tracking, spectral_entropy→severity discrimination. (b) Full FT vs QLoRA trajectories: both gen1 large jump (FT 15.3x, QLoRA 8.7x), post-gen1 divergence (FT saturation gen1→4: 1.11x, QLoRA deceleration gen1→4: 6.13x). PROHIBIT 'slow onset' for QLoRA. (c) HellaSwag method-dependence: effective under Full FT (−12.5%), stable under QLoRA. Attribute to training method NOT model scale. (d) PPL-downstream dissociation: QLoRA PPL=839/hellaswag=0.430 vs FT PPL=326/hellaswag=0.372 — PPL overestimates QLoRA damage. (e) Self-recovery at frac=50%: observation (cite Gerstgrasser 2024), RR~0.52 output signals, ~0.33 weight-space. Prohibit cross-signal-set prevalence comparison (Writing Note 15).\\\"\\n      - \\\"§4.3 continued: diversity metrics (distinct_1, self_bleu) insensitive to collapse even at PPL 17x — token_entropy captures collapse but surface diversity maintained by sampling randomness. Exclude diversity from effective indicators.\\\"\\n      - \\\"PROHIBITIONS: (1) 'consistently outperforms'/'significantly improves' without stats. (2) SIGMA direction as verified finding (C001 provisional). (3) 100% gen1→gen2 −1.9% as 'non-monotonic' (noise, N=1). (4) stable_rank as 'most sensitive signal' (seed-sensitive, rank dropped 1→4 with 3 seeds).\\\"\\n    dependencies: [method]\\n    registry_refs: [mvp_frac50_100, mvp_frac0, plan003-fullft-05B, plan006-signal-taxonomy, plan008-self-recovery, within_gen_analysis, per_layer_analysis_v5, plan001-wikitext-15B-5seeds, plan002-pubmed-cqa1, plan010-3B-spotcheck]\\n    tables: [tab1_signal_taxonomy, tab2_within_gen_roc, tab3_cross_config]\\n    figures: [fig2_severity_curves, fig3_roc_curves, fig4_signal_heatmap, fig5_method_comparison]\\n\\n  - section: discussion\\n    word_budget: 600\\n    core_bullets:\\n      - \\\"Practical three-tier monitoring recommendation: (1) within-gen alarm → stable_rank, (2) cross-gen severity tracking → evaluation perplexity, (3) severity discrimination → spectral_entropy. No single signal suffices.\\\"\\n      - \\\"PPL within-gen failure mechanism: training PPL measures fit to (potentially contaminated) training distribution, not representation structural change. Spectral signals detect structural change independent of data quality.\\\"\\n      - \\\"Self-recovery at moderate contamination: consistent with data mixing effects (Gerstgrasser et al. 2024). Recovery ratio ~0.52 for output signals, ~0.33 for weight-space signals. Position as observation, not novel finding.\\\"\\n      - \\\"SIGMA comparison: our signals are free (computed during training), require no clean reference distribution, provide per-layer granularity. SIGMA operates post-hoc on output embeddings.\\\"\\n      - \\\"Terminal spectral convergence (SR ~154 vs ~156 for FT/QLoRA): noted as observation only (N=1, cannot distinguish convergence from coincidence).\\\"\\n    dependencies: [results]\\n    citation_hints:\\n      - \\\"gerstgrasser_2024 for self-recovery/data mixing\\\"\\n      - \\\"sigma_2026 for operational comparison\\\"\\n      - \\\"martin_mahoney_2021 for spectral analysis methodology\\\"\\n\\n  - section: conclusion\\n    word_budget: 250\\n    core_bullets:\\n      - \\\"Summary: systematic empirical analysis of training dynamic signals as collapse severity monitors across contamination levels, model scales, domains, and training methods\\\"\\n      - \\\"Key takeaway: signals have complementary operating ranges — stable_rank for within-gen early warning, perplexity for cross-gen severity, spectral_entropy for robust discrimination — and the same signal's utility depends on training method\\\"\\n      - \\\"Practical value: signal taxonomy enabling informed monitoring decisions; practitioners should not rely on single-signal monitoring\\\"\\n      - \\\"Future work: scaling to ≥7B models, integration with mitigation strategies, open-source monitoring toolkit release\\\"\\n    dependencies: [results, discussion]\\n\\n  - section: limitations\\n    word_budget: 300\\n    core_bullets:\\n      - \\\"Model scale: 0.5B and 1.5B with 3B spot-check — resource constraints prevent testing ≥7B where different dynamics may emerge\\\"\\n      - \\\"Full FT comparison: N=1 seed at single model scale (0.5B) — method-dependence claims are directional, not statistically robust\\\"\\n      - \\\"Domains: WikiText-2 (general) + PubMed (biomedical) — not tested on code, multilingual, or conversational data\\\"\\n      - \\\"Training method: QLoRA as primary with Full FT as comparison — not tested on other PEFT methods (LoRA full-rank, prefix-tuning, adapters)\\\"\\n      - \\\"Within-gen ROC: initial analysis on N=1 seed, 0.5B only (plan001 5-seed validation pending)\\\"\\n      - \\\"Self-recovery analysis: limited to 3 fractions (0/50/100%), 3 seeds — finer granularity needed for fraction threshold characterization\\\"\\n      - \\\"No intervention/mitigation: explicitly scoped as analysis paper; detection ≠ prevention\\\"\\n    dependencies: [results]\\n\\nvisualization_plan:\\n  - fig_id: fig1_framework\\n    type: conceptual\\n    tool: paperbanana\\n    description: >\\n      Iterative training loop + signal monitoring framework diagram.\\n      Shows: M₀→M₁→...→M_g pipeline with synthetic data generation step at each generation.\\n      Signal extraction points annotated at 4 locations: weight matrices (spectral),\\n      training loss stream (output), gradient computation (gradient), held-out evaluation (downstream).\\n      Highlight the early warning detection zone (within-gen) vs cross-gen tracking distinction.\\n    placement: introduction\\n    aspect_ratio: \\\"16:9\\\"\\n\\n  - fig_id: fig2_severity_curves\\n    type: statistical\\n    tool: matplotlib\\n    description: >\\n      Multi-panel line plots (2×2): 4 key signals (stable_rank, spectral_entropy,\\n      perplexity, token_entropy) across generations (x-axis, 0-4) with contamination\\n      fraction as color (0%=blue, 50%=orange, 100%=red). Shows monotonic ordering\\n      and cross-gen severity tracking for C1. Error bars/bands from available seeds.\\n      Use 0.5B MVP data; overlay 1.5B when available.\\n    data_source: \\\"registry: mvp_frac50_100, mvp_frac0, plan001-wikitext-15B-5seeds\\\"\\n    placement: results\\n    aspect_ratio: \\\"4:3\\\"\\n\\n  - fig_id: fig3_roc_curves\\n    type: statistical\\n    tool: matplotlib\\n    description: >\\n      Within-generation collapse detection ROC curves. Left panel: full ROC for\\n      stable_rank (AUC=0.984), training_loss (AUC=0.923), spectral_entropy,\\n      perplexity (AUC=0.534). Diagonal reference line. Right panel or inset:\\n      AUC vs training progress (10%, 25%, 50%, 100%) for each signal —\\n      shows stable_rank reaches AUC=0.94 at 10% while PPL stays ~0.5.\\n    data_source: \\\"registry: within_gen_analysis\\\"\\n    placement: results\\n    aspect_ratio: \\\"2:1\\\"\\n\\n  - fig_id: fig4_signal_heatmap\\n    type: statistical\\n    tool: matplotlib\\n    description: >\\n      Signal taxonomy heatmap. Rows: signals (stable_rank, spectral_entropy,\\n      perplexity, token_entropy, gradient_norm, hellaswag, distinct_1).\\n      Columns: key metrics (cross-gen effect size d, within-gen AUC,\\n      seed robustness 1/CV, QLoRA effective?, Full FT effective?).\\n      Color: green (effective) to red (ineffective/misleading).\\n      Annotated cells with numeric values. Operating range labels on right margin.\\n    data_source: \\\"registry: plan006-signal-taxonomy, within_gen_analysis, plan003-fullft-05B\\\"\\n    placement: results\\n    aspect_ratio: \\\"3:2\\\"\\n\\n  - fig_id: fig5_method_comparison\\n    type: statistical\\n    tool: matplotlib\\n    description: >\\n      Full FT vs QLoRA collapse trajectory comparison for frac=100%.\\n      Two panels: (a) PPL across generations — both show gen1 large jump\\n      (FT 15.3x, QLoRA 8.7x), then diverge (FT saturates, QLoRA decelerates but continues).\\n      (b) HellaSwag across generations — FT degrades (−12.5%), QLoRA stable.\\n      Annotate gen1 jump magnitudes. Show PPL-downstream dissociation clearly.\\n    data_source: \\\"registry: plan003-fullft-05B, mvp_frac50_100\\\"\\n    placement: results\\n    aspect_ratio: \\\"2:1\\\"\\n\\ntable_plan:\\n  - table_id: tab1_signal_taxonomy\\n    caption: \\\"Signal taxonomy: operating ranges, effect sizes, and method-dependence across collapse severity monitoring dimensions.\\\"\\n    placement: results\\n    type: comparison\\n    columns: [Signal, Family, \\\"Effect Size (d)\\\", \\\"Cross-gen ρ\\\", \\\"Within-gen AUC\\\", \\\"Seed CV\\\", \\\"Method-Dep.\\\", \\\"Operating Range\\\"]\\n    data_source: \\\"registry: plan006-signal-taxonomy, within_gen_analysis, plan003-fullft-05B\\\"\\n    notes: >\\n      Core table for Claim 3. Effect sizes: Cohen's d at gen4 (frac=0% vs 100%).\\n      Method-dep from QLoRA vs Full FT comparison. Bold best-per-column.\\n      Include footnote: stable_rank seed-sensitive (CV=0.022), spectral_entropy most robust (CV=0.0015).\\n\\n  - table_id: tab2_within_gen_roc\\n    caption: \\\"Within-generation collapse detection: ROC performance at different training progress checkpoints.\\\"\\n    placement: results\\n    type: comparison\\n    columns: [Signal, \\\"AUC (full)\\\", \\\"AUC @10%\\\", \\\"AUC @25%\\\", \\\"Sens @10%\\\", \\\"Spec @10%\\\"]\\n    data_source: \\\"registry: within_gen_analysis\\\"\\n    notes: >\\n      Clustered bootstrap CIs (one obs per fraction×seed). Highlight:\\n      stable_rank AUC=0.984 vs PPL AUC=0.534. Footnote: N=1 seed, 0.5B only.\\n\\n  - table_id: tab3_cross_config\\n    caption: \\\"Cross-configuration signal-severity correlation (Spearman ρ with 95% bootstrap CI).\\\"\\n    placement: results\\n    type: comparison\\n    columns: [Signal, \\\"0.5B WikiText (QLoRA)\\\", \\\"1.5B WikiText (QLoRA)\\\", \\\"1.5B PubMed (QLoRA)\\\", \\\"0.5B WikiText (Full FT)\\\"]\\n    data_source: \\\"registry: mvp_frac50_100, plan001-wikitext-15B-5seeds, plan002-pubmed-cqa1, plan003-fullft-05B\\\"\\n    notes: >\\n      [TODO] 1.5B WikiText and PubMed columns from plan001/002 when complete.\\n      Currently: 0.5B QLoRA (MVP, n=3 fractions) + 0.5B Full FT (plan003, n=3 fractions).\\n      May move to appendix if space tight — tab1 is higher priority.\\n\\n  - table_id: tab4_config\\n    caption: \\\"Experimental configurations for collapse severity monitoring analysis.\\\"\\n    placement: method\\n    type: configuration\\n    columns: [ID, Model, \\\"#Params\\\", Dataset, Domain, Fractions, Seeds, Method, \\\"Trainable %\\\"]\\n    data_source: \\\"manual\\\"\\n    notes: >\\n      C1: 0.5B QLoRA (MVP), Config A: 1.5B QLoRA WikiText 5-seed,\\n      Config B: 1.5B QLoRA PubMed 3-seed, Config C: 0.5B Full FT, Config D: 3B QLoRA spot-check.\\n\\nliterature_strategy:\\n  citation_budget: 42\\n  macro_context:\\n    - \\\"model collapse in iterative synthetic data training\\\"\\n    - \\\"spectral analysis of neural network weights and training dynamics\\\"\\n    - \\\"training-time monitoring and early warning systems\\\"\\n    - \\\"synthetic data detection, quality, and contamination\\\"\\n  micro_clusters:\\n    - cluster_name: \\\"Model Collapse Theory & Empirics\\\"\\n      search_queries:\\n        - \\\"model collapse iterative training synthetic data 2024 2025 2026\\\"\\n        - \\\"self-consuming generative models data distribution degradation\\\"\\n        - \\\"scaling laws synthetic data model collapse\\\"\\n      must_cite:\\n        - \\\"shumailov_nature2024\\\"\\n        - \\\"dohmatob_iclr2025\\\"\\n        - \\\"dohmatob_icml2024\\\"\\n        - \\\"alemohammad_iclr2024\\\"\\n        - \\\"gerstgrasser_2024\\\"\\n        - \\\"schaeffer_2025\\\"\\n        - \\\"shi_neurips2025\\\"\\n      target_count: 14\\n\\n    - cluster_name: \\\"Spectral & Topological Monitoring\\\"\\n      search_queries:\\n        - \\\"spectral analysis neural network collapse monitoring 2024 2025 2026\\\"\\n        - \\\"stable rank neural network generalization quality prediction\\\"\\n        - \\\"topological data analysis neural network training monitoring\\\"\\n      must_cite:\\n        - \\\"sigma_2026\\\"\\n        - \\\"kalinowski_2026\\\"\\n        - \\\"martin_mahoney_2021\\\"\\n        - \\\"sanyal_iclr2020\\\"\\n      target_count: 8\\n\\n    - cluster_name: \\\"Training Dynamics & Representation Analysis\\\"\\n      search_queries:\\n        - \\\"training dynamics spectral analysis deep learning 2024 2025 2026\\\"\\n        - \\\"weight matrix spectral properties during training\\\"\\n      must_cite:\\n        - \\\"spectral_lens_2026\\\"\\n        - \\\"yunis_2024\\\"\\n        - \\\"pennington_nips2017\\\"\\n      target_count: 6\\n\\n    - cluster_name: \\\"Synthetic Data Detection\\\"\\n      search_queries:\\n        - \\\"LLM generated text detection watermarking 2024 2025\\\"\\n        - \\\"synthetic data contamination detection\\\"\\n      must_cite:\\n        - \\\"kirchenbauer_icml2023\\\"\\n      target_count: 5\\n\\n    - cluster_name: \\\"Data Mixing & Mitigation\\\"\\n      search_queries:\\n        - \\\"synthetic data mixing collapse mitigation verification 2024 2025\\\"\\n      must_cite:\\n        - \\\"kazdan_2024\\\"\\n        - \\\"feng_iclr2025\\\"\\n      target_count: 5\\n\\n    - cluster_name: \\\"Collapse Definition & Taxonomy\\\"\\n      search_queries:\\n        - \\\"model collapse definition taxonomy survey 2025 2026\\\"\\n        - \\\"neural collapse representation learning\\\"\\n      must_cite:\\n        - \\\"schaeffer_2025\\\"\\n        - \\\"papyan_pnas2020\\\"\\n      target_count: 4\\n\\nwriting_order:\\n  - method          # data-independent: signal definitions, collapse protocol, evaluation metrics\\n  - related_work    # data-independent: literature clusters, positioning\\n  - results         # use available data (MVP/plan003/plan006/plan008/within_gen), TODO placeholders\\n  - discussion      # depends on results\\n  - introduction    # depends on results for hook/evidence\\n  - conclusion      # depends on results + discussion\\n  - limitations     # depends on results\\n  - abstract        # depends on everything\\n\\n# ============================================================\\n# Writing Constraints (from paper_framing.md, injected into all Worker prompts)\\n# ============================================================\\nwriting_constraints:\\n  evidence_hierarchy:\\n    - \\\"Effect sizes (Cohen's d) as PRIMARY evidence; Spearman ρ as SUPPORTING\\\"\\n    - \\\"Bootstrap CIs mandatory for all quantitative claims\\\"\\n    - \\\"ROC must use clustered bootstrap (one obs per fraction×seed)\\\"\\n\\n  prohibited_phrasings:\\n    - \\\"'consistently outperforms' / 'significantly improves' without statistical testing\\\"\\n    - \\\"'state-of-the-art' without comparison to latest SOTA\\\"\\n    - \\\"'significantly' without significance test\\\"\\n    - \\\"'XXX has achieved remarkable success in recent years'\\\"\\n    - \\\"'To the best of our knowledge, we are the first to...'\\\"\\n    - \\\"'Extensive experiments demonstrate that...'\\\"\\n    - \\\"'This demonstrates the effectiveness of our approach'\\\"\\n    - \\\"'slow onset' / 'snowball' / 'exponential' for QLoRA collapse trajectory\\\"\\n    - \\\"'most sensitive signal' for stable_rank (seed-sensitive, rank dropped 1→4)\\\"\\n    - \\\"'strong recovery' for 25% contamination (use 'mild degradation / near-stability')\\\"\\n\\n  mandatory_distinctions:\\n    - \\\"Training PPL (fit to current batch) vs evaluation PPL (held-out clean set) — different quantities, different AUCs\\\"\\n    - \\\"Within-gen detection (temporal, during training) vs cross-gen tracking (across generations)\\\"\\n    - \\\"stable_rank ↑ under collapse = energy dispersal (‖W‖²_F grows faster than σ₁²), NOT concentration\\\"\\n\\n  provisional_claims:\\n    - \\\"C001: SIGMA direction (effective_rank ↑ under collapse) — N=2, NOT verified. PROHIBIT as finding.\\\"\\n    - \\\"100% gen1→gen2 PPL −1.9% — noise (N=1). PROHIBIT as 'non-monotonic pattern'.\\\"\\n    - \\\"Terminal spectral convergence (SR ~154 vs ~156) — observation only, N=1.\\\"\\n\\n  attribution_rules:\\n    - \\\"HellaSwag method-dependence: attribute to training method (QLoRA implicit regularization), NOT model scale\\\"\\n    - \\\"Self-recovery: cite Gerstgrasser et al. 2024, position as observation not novel finding\\\"\\n    - \\\"Collapse trajectory: both methods gen1 large jump, difference is post-gen1 evolution (FT saturation vs QLoRA deceleration)\\\"\\n\\n  statistical_limitations:\\n    - \\\"Full FT comparison: N=1 seed — must note in Limitations\\\"\\n    - \\\"Within-gen ROC: N=1 seed, 0.5B — pending plan001 5-seed validation\\\"\\n    - \\\"Self-recovery: 3 fractions only (0/50/100%), recovery prevalence prohibit cross-signal-set comparison\\\"\\n    - \\\"N=3 seeds insufficient for Wilcoxon (min p=0.25); use bootstrap CI\\\"\\n    - \\\"3B spot-check: N=1 seed, 3 fractions — directional only\\\"\\n\", \"total_chars\": 24290, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "98f77a39-268f-4928-b07d-5530eecd4077",
  "isSidechain": true,
  "promptId": "80dd2a4d-c31a-43ae-8316-4a6135d9fed6",
  "agentId": "ade4d670d78b2afaf",
  "type": "user",
  "uuid": "5a509a5b-dcbf-4bfd-b732-5d71995f6d27",
  "sourceToolAssistantUUID": "98f77a39-268f-4928-b07d-5530eecd4077",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 57 · 2026-05-16T10:43:28.286Z_

I now have comprehensive understanding of the paper, its internal state, experimental gaps, and literature positioning. Let me write the R2 review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a509a5b-dcbf-4bfd-b732-5d71995f6d27",
  "isSidechain": true,
  "agentId": "ade4d670d78b2afaf",
  "requestId": "req_011Cb67KXeh2ixxzFddtRbKL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "624eb4bd-3679-41cb-b5f3-a00db54d92aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F4uEoRWyqn7o6FgHqcXfkN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8465,
      "cache_read_input_tokens": 98601,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8465,
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

_source line 58 · 2026-05-16T10:43:28.950Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_012XhNPVTKma6BsPmvzRNkVT`</summary>

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
  "parentUuid": "624eb4bd-3679-41cb-b5f3-a00db54d92aa",
  "isSidechain": true,
  "agentId": "ade4d670d78b2afaf",
  "requestId": "req_011Cb67KXeh2ixxzFddtRbKL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "653350af-8a54-4f68-8ba9-16d5ea2110bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F4uEoRWyqn7o6FgHqcXfkN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8465,
      "cache_read_input_tokens": 98601,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8465
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 119,
          "cache_read_input_tokens": 98601,
          "cache_creation_input_tokens": 8465,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8465,
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

_source line 59 · 2026-05-16T10:43:28.953Z_

<details><summary>↩ Tool result · `toolu_012XhNPVTKma6BsPmvzRNkVT`</summary>

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
  "parentUuid": "653350af-8a54-4f68-8ba9-16d5ea2110bb",
  "isSidechain": true,
  "promptId": "80dd2a4d-c31a-43ae-8316-4a6135d9fed6",
  "agentId": "ade4d670d78b2afaf",
  "type": "user",
  "uuid": "7bfd0881-f821-4f1d-a15c-f06395861ac7",
  "sourceToolAssistantUUID": "653350af-8a54-4f68-8ba9-16d5ea2110bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 60 · 2026-05-16T10:45:26.814Z_



Here is my R2 review.

---

## R2 Review: "Collapse Monitoring Is Harder Than It Looks: Configuration-Dependent Signal Behavior in Iterative Model Collapse"

**Focus: Novelty and Related Work**

---

### 1. Novelty Assessment

The paper's central claim is that no single training-time signal reliably tracks model collapse across all configurations (model scale, fine-tuning method, domain, contamination level). This is framed as a negative result. I have mixed views on the novelty.

**What is genuinely useful:** The systematic empirical decomposition -- testing 11 signals across multiple axes and documenting where each succeeds, saturates, or misleads -- has practical value. The specific finding that held-out evaluation perplexity provides no within-generation early warning (AUROC = 0.534) while stable rank achieves 0.984 is a concrete, actionable insight. The PPL-downstream dissociation (QLoRA PPL=839 with better HellaSwag than Full FT PPL=326) is a well-documented cautionary finding. The three-tier monitoring recommendation (stable rank for within-gen, perplexity for cross-gen, spectral entropy for severity discrimination) adds practical structure.

**What is less novel than presented:** The observation that "different metrics behave differently across configurations" is, at a high level, unsurprising. Anyone who has monitored training across different scales and methods knows that no single metric is universal. The paper's title ("Collapse Monitoring Is Harder Than It Looks") frames this as a revelation, but the specific finding that metric behavior is configuration-dependent is closer to an expected empirical regularity than a surprising negative result. Compare this to genuinely surprising negative results in the literature (e.g., "sharp minima can generalize" overturning the flat-minima hypothesis): those contradict strong prior beliefs. Here, there was no strong prior belief that a single signal would generalize universally.

The paper occupies an awkward middle ground: it is not purely a negative-result paper (it does find signals that work in specific contexts) nor a methods paper (it proposes no new signal or monitoring algorithm). The taxonomy/analysis-paper framing is reasonable but demands stronger empirical coverage than what is delivered.

**Novelty score: Moderate.** The contribution is primarily empirical systematization rather than conceptual novelty.

---

### 2. Related Work Coverage

The related work section (Section 2) is well-organized into four paragraphs covering collapse theory, spectral diagnostics, concurrent monitoring work, and data contamination detection. It cites 44 references total, which is thorough. However, I identify several gaps and positioning issues:

**Missing or underrepresented lines of work:**

(a) **Representation degeneration / anisotropy literature.** Gao et al. (2019, "Representation Degeneration Problem in Training NLG Models," cited in the bib but not discussed) is directly relevant -- it documents how token representations collapse into a narrow cone during standard LM training. The paper's stable rank increase under collapse (energy dispersal) is the opposite direction from representation degeneration (energy concentration). This tension deserves explicit discussion: why does iterative synthetic data contamination cause dispersal rather than the concentration seen in standard degeneration? The paper offers a one-line footnote but this is a substantive theoretical question.

(b) **Neural collapse (Papyan et al. 2020).** Listed in the literature map as a foundation paper but absent from the submitted paper. While neural collapse (in the classification sense) and model collapse (in the generative sense) are distinct phenomena, the shared terminology and shared spectral analysis tools warrant at least a clarifying sentence. Reviewers unfamiliar with the distinction will wonder about the connection.

(c) **Wyss et al. 2024 ("Learning by Surprise: Surplexity").** Listed in the literature map as related (next-token probability for collapse characterization at different synthetic fractions 25/50/75%) but absent from the paper. This is a close methodological relative that studies the same independent variable (synthetic fraction) with output-level signals. Its omission weakens the positioning.

(d) **Briesch et al. 2023.** Listed in the paper's own reference list in the task description as [8] but I do not see it cited in the submitted paper text. This is one of the earliest LLM self-consuming loop studies and should be cited.

(e) **Hataya et al. 2023 (ICCV).** Same situation -- listed as [10] in the task description references but not cited in the submitted related work section. The paper studies synthetic data corruption of datasets at ImageNet scale.

(f) **The broader "data quality for LLM training" literature** (e.g., data selection, curriculum learning, data mixing laws) is largely absent. Works like Xie et al. (2024, "DoReMi") or Ye et al. (2024, "Data Mixing Laws") study how data composition affects training dynamics -- directly relevant to understanding why different contamination fractions produce different signal behaviors.

**Positioning issues:**

(g) The differentiation from SIGMA is stated as "SIGMA requires a clean reference distribution and operates post-hoc" (Section 2, line 16). But the paper acknowledges internally (paper_framing.md) that the planned empirical comparison (plan_009) was killed and never completed. The differentiation is therefore purely methodological assertion without empirical backing. The competitor comparison table (Appendix) is one-sided: it lists capabilities the authors' method has and competitors lack, without acknowledging any advantages of SIGMA (e.g., theoretical grounding in random matrix theory, formal spectral bounds).

(h) The claim "no prior work simultaneously achieves online monitoring, spectral/entropic training-dynamic signals, and validation in the iterative synthetic data setting" (Section 2, line 23) is technically true but assembled from individually non-novel components. Online monitoring exists (Kalinowski). Spectral analysis of weights exists (Martin & Mahoney, WeightWatcher). Iterative synthetic data experiments exist (Shumailov, Alemohammad). The combination is new but the individual pieces are not, and the paper should acknowledge this more explicitly.

---

### 3. Contribution Significance

**Who benefits:** Practitioners fine-tuning models where synthetic data contamination is a concern. The three-tier monitoring recommendation is actionable if validated at scale. The finding that perplexity fails within-generation is practically important.

**Who does not benefit:** Researchers seeking theoretical understanding of collapse mechanisms. The paper provides no mechanistic explanation for why stable rank increases under collapse (the "energy dispersal" explanation is hand-waving), why the scale-dependence exists, or why the signal rankings shift between 0.5B and 1.5B.

**Significance concern:** The practical recommendations are undermined by the narrow experimental validation. The three-tier strategy is derived from one architecture family (Qwen) at small scales (0.5B-1.5B) on one domain (WikiText-2) with severe statistical limitations (N=1 for within-gen AUROC, N=1 for Full FT comparison). The paper's own title says monitoring is "harder than it looks" -- but the implication is that even these recommendations may not generalize, which undercuts the paper's own actionable contribution.

---

### 4. Framing Quality

The negative-result framing ("no single signal suffices") is partially effective but inconsistently applied. The paper oscillates between:

- A negative-result paper: "signals don't generalize across configs" (title, abstract)
- A positive-result paper: "stable rank achieves AUROC=0.984" (abstract, introduction, conclusion)
- A taxonomy paper: "we provide a signal operating-range taxonomy" (abstract, discussion)

These framings are not incompatible, but the paper does not commit cleanly to any of them. The negative-result framing is weakest because the result is not sufficiently surprising. The taxonomy framing is strongest but requires broader experimental coverage to be convincing.

The title is effective and memorable. The abstract is well-structured but overpacked with numbers -- it reads like a results summary rather than a story.

---

### 5. Writing Quality

**Strengths:**
- Clear signal definitions with explicit equations (Section 3.3)
- Good distinction between training loss and evaluation perplexity (after internal corrections)
- Honest limitations section that acknowledges seed count and scale limitations
- Appropriate use of [TBD] placeholders rather than fabricated numbers for incomplete experiments

**Weaknesses:**
- The Results section (Section 4) is dense and hard to follow. The three-claim structure is logical but the subsections are long and interleave positive findings with caveats in a way that loses the reader.
- Some numerical claims lack sufficient context. "Cohen's d = 33.48" is enormous but the paper does not discuss whether this magnitude is meaningful or an artifact of the measurement scale.
- The paper switches between configurations (C1, C2, C4) without always making clear which data is from which configuration, leading to apples-to-oranges comparisons. For example, effect sizes from C2 (1.5B, N=3) are presented alongside AUROC from C1 (0.5B, N=1) in the same recommendation table.
- Multiple TODO comments and placeholder values remain in the manuscript ([TBD] appears 6 times). This is a draft, not a submission-ready paper.

---

### 6. Specific Weaknesses

**W1. Severe statistical under-powering across claims.** The within-generation AUROC results (the paper's strongest contribution) rest on N=1 seed at 0.5B. The effect size rankings come from N=3 seeds where the ranking already shifted dramatically (stable rank d: 61.7 to 9.43 with the third seed). The Full FT comparison is N=1. The 1.5B validation has only 10/30 runs completed. At a top venue, claims about signal reliability demand robustness across seeds -- and the paper's own data shows this robustness is fragile.

**W2. Configuration coverage is too narrow for the claims.** The paper claims to study "two model scales, two fine-tuning methods, and six contamination fractions" but the actual coverage is highly uneven: 0.5B has 1 seed with 3 fractions; 1.5B has 3 seeds (of planned 5) with incomplete fraction coverage; Full FT has 1 seed; PubMed is not reported in the main paper; LLaMA is mentioned in the dream review abstract but absent from the submitted paper; 3B is baseline-only. The abstract lists these as achieved configurations but the paper cannot support cross-scale or cross-architecture claims with this data.

**W3. The SIGMA comparison is unfairly one-sided.** Plan_009 (head-to-head SIGMA comparison) was killed. The paper differentiates from SIGMA purely on methodological grounds ("requires clean reference," "post-hoc") without any empirical comparison. The competitor comparison table in the appendix is constructed to highlight the authors' advantages. This is a significant related-work weakness for a paper that positions itself relative to SIGMA as its closest competitor.

**W4. The negative-result contribution is not sufficiently surprising.** "Different signals work differently across configurations" is an expected empirical regularity. For a negative-result paper to be impactful, it should overturn a strong prior belief or demonstrate failure of a widely-adopted approach. The paper partially achieves the latter (perplexity fails within-gen), but this is one finding among many, not the central organizing principle.

**W5. No theoretical framework or mechanistic explanation.** The paper observes that stable rank increases under collapse and calls this "energy dispersal" but provides no explanation of why. Why does contamination with lower-entropy synthetic data cause the covariance eigenspectrum to flatten? Is this a QLoRA-specific artifact (adapter rank interactions)? The lack of even an informal theoretical argument makes it hard to predict whether findings will generalize.

**W6. Incomplete manuscript.** Six [TBD] placeholders in the results, TODO comments throughout the appendix, placeholder figures, and ongoing experiments (plan001, plan002, plan010) that are explicitly described as incomplete. This paper is not ready for review.

**W7. The repetition confound at alpha=1.0 is inadequately addressed.** At full contamination, 1500 synthetic chunks are upsampled 3.3x. The paper acknowledges this but dismisses it by pointing to moderate contamination results. However, many of the headline numbers (AUROC=0.984, d=33.48, PPL=839) come from the alpha=1.0 condition. The interaction between repetition-induced memorization and genuine collapse-induced degradation is not disentangled.

**W8. Cross-domain claims are unsupported.** The paper mentions PubMed in the experimental configuration table but reports no PubMed results in the main text. Cross-domain validation is listed as "ongoing." The paper cannot claim domain generality.

---

### 7. Specific Strengths

**S1. Well-designed experimental protocol.** The iterative training loop with controlled contamination fractions is clean. Initializing each generation from M_0 (rather than M_{g-1}) isolates the data contamination effect from cumulative weight drift -- a methodological choice that strengthens causal interpretation.

**S2. The within-gen vs. cross-gen distinction is valuable.** Decomposing monitoring into within-generation early warning and cross-generation severity tracking is a useful conceptual contribution. The finding that the best signal for each task differs (stable rank vs. perplexity) is well-supported at 0.5B.

**S3. Honest self-assessment.** The limitations section is thorough and the paper does not overclaim. The provisional nature of many findings is clearly marked. The internal writing constraints (prohibiting "most sensitive signal" for stable rank, requiring attribution corrections) show scientific discipline.

**S4. Practical three-tier monitoring recommendation.** Even if the specific thresholds may not generalize, the framework of decomposing monitoring into alarm/tracking/discrimination tiers is a useful contribution to practitioner methodology.

**S5. The PPL-downstream dissociation is a well-documented finding.** Showing that QLoRA achieves PPL=839 but hellaswag=0.430 while Full FT has PPL=326 but hellaswag=0.372 is counterintuitive and practically important, even at N=1.

**S6. The related work is broad and well-organized.** 44 references covering collapse theory, spectral methods, concurrent monitoring, and data contamination detection. The four-paragraph structure is clear.

---

### 8. Questions for Authors

Q1. The stable rank effect size dropped from d=61.7 to d=9.43 when a third seed was added. What is your estimate of where this will stabilize with 5 seeds? If it drops further, does stable rank remain in the recommended monitoring set?

Q2. You initialize each generation from M_0 rather than M_{g-1}. How does this choice affect your findings? Under cumulative weight initialization (the more common real-world scenario), collapse compounds through both data and parameters -- would your signal rankings change?

Q3. The scale-dependent signal ranking shift (stable rank dominant at 0.5B, training loss at 1.5B) is noted but unexplained. Can you provide even an informal argument for why this occurs? Without this, the three-tier recommendation is 0.5B-specific.

Q4. Why was the SIGMA head-to-head comparison (plan_009) killed? Given that SIGMA is your closest competitor and the differentiation is crucial to your novelty claim, this seems like a critical omission.

Q5. Your spectral signals are computed on last-layer hidden states (representation covariance), not on weight matrices. But the related work positioning cites WeightWatcher (which analyzes weight matrices). Which is it? The method section (Eq. 1-2) describes covariance of hidden states H, while some internal documents describe "weight spectral entropy." This inconsistency should be clarified.

Q6. At alpha=1.0, you upsample 1500 chunks to 4916 (3.3x repetition). Have you tested whether the observed signal behavior is driven by repetition rather than synthetic data quality? A control experiment with 3.3x repeated real data would disambiguate.

Q7. You claim "ten of eleven signals maintain consistent direction of change" across QLoRA and Full FT. But this is computed from N=1 seed per method. What is the probability that direction consistency is maintained at N=5?

Q8. The paper does not discuss the computational cost of signal collection. How much overhead does computing stable rank (SVD of the covariance matrix) add to training time? If it is non-negligible, the "free monitoring" framing is misleading.

---

### 9. Overall Score: 3/6 (Weak Reject)

**Justification:** The paper addresses a relevant practical question and contains some useful empirical findings (PPL within-gen failure, three-tier monitoring decomposition, PPL-downstream dissociation). However, it falls short of the acceptance bar for several reasons:

(a) The negative result ("signals don't generalize") is insufficiently surprising to carry the paper as a standalone contribution.

(b) The experimental coverage is too narrow and statistically underpowered for the breadth of the claims. Key results rest on N=1 seeds, rankings are unstable across seeds, and the manuscript contains [TBD] placeholders for major results.

(c) The SIGMA comparison -- critical for novelty positioning -- is purely methodological assertion without empirical validation.

(d) The paper is not submission-ready: incomplete experiments, placeholder values, and TODO comments throughout.

(e) The lack of any theoretical or mechanistic framework limits the paper's ability to predict generalization beyond the tested configurations, which is precisely the paper's own critique of existing work.

A revised version with completed experiments (5-seed 1.5B, PubMed, SIGMA comparison), the [TBD] values filled, and a more focused framing (either the taxonomy contribution or the PPL-failure finding as the headline) could reach borderline accept. The current version is premature.

---

### 10. Confidence: 4/5

I am confident in this assessment. I have read the paper carefully, including the methodology, results, appendix, and supplementary materials. My expertise covers spectral analysis of neural networks and training dynamics monitoring. My main uncertainty is whether the completed experiments (plan001 5-seed data) would substantially change the signal rankings and strengthen the statistical claims -- if they do, the paper's position improves. But the current manuscript must be evaluated as submitted, and it is not ready.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7bfd0881-f821-4f1d-a15c-f06395861ac7",
  "isSidechain": true,
  "agentId": "ade4d670d78b2afaf",
  "requestId": "req_011Cb67KovEa4W9QcBqUheQX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b17ae8f-f921-4e10-84d0-21c3feb6bce2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "570c097c-891d-480b-ba6e-6bc049e2208c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A84PrEFNieMbfxPUQw4wC2",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 697,
      "cache_read_input_tokens": 107066,
      "output_tokens": 4371,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 697
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4371,
          "cache_read_input_tokens": 107066,
          "cache_creation_input_tokens": 697,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 697,
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
