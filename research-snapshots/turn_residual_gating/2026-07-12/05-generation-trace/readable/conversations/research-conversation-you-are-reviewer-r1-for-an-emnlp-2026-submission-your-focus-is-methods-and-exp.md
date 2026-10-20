# Research conversation: You are Reviewer R1 for an EMNLP 2026 submission. Your focus is **Methods and Experiments**. Provide a blind, thorough r

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 57
- **Recorded user turns:** 1
- **Tool calls:** 25
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a32bc4203578b639f.jsonl`
- **Structured JSON:** [`6ddaf03dd3827de1d18d.json`](../../sessions/6d/6ddaf03dd3827de1d18d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

57 recorded events

### User

_source line 1 · 2026-05-16T15:50:01.305Z_

You are Reviewer R1 for an EMNLP 2026 submission. Your focus is **Methods and Experiments**. Provide a blind, thorough review.

## Venue: EMNLP 2026 (via ACL Rolling Review)
- Acceptance rate: ~22%
- Scoring: Soundness (1-5), Excitement (1-5), Overall (1-5)
- Soundness: 5=Excellent, 4=Strong, 3=Acceptable, 2=Poor, 1=Major Issues
- Excitement: 5=Highly Exciting, 4=Exciting, 3=Ambivalent, 2=Mediocre, 1=Not Exciting
- Overall: 5=Strong Accept, 4=Accept, 3=Borderline, 2=Reject, 1=Strong Reject

## Paper Summary

**Title**: "Phase-Dependent Compound Sparsity: Quantifying the Interaction Between Head Pruning and KV Cache Eviction Across Reasoning Phases"

**Core claim**: Compound sparsity (simultaneous head pruning + KV cache eviction) produces phase-dependent severity—later reasoning phases suffer more than earlier ones. Three findings:
1. **Phase gradient universality**: dz ≈ 1.0–1.2 across all models/architectures/sparsity levels (Bonferroni p < 10^-30)
2. **Dose-response monotonicity**: Severity increases monotonically with sparsity (Spearman ρ = 1.0)
3. **Strategy modulation with architecture-dependent magnitude**: Importance-based eviction 15-36× stronger than random on MATH-500/Qwen2, attenuates to 2-5× on simpler tasks and LLaMA

**Method (§3)**:
- Interaction Index (II): II_i = Δ_compound,i − (Δ_prune,i + Δ_evict,i)
- Phase segmentation via token position quantiles (upper/lower tertiles of attention density)
- Paired phase gradient: G_i = II_{i,low} − II_{i,high}
- Population summary: Ĝ = median(G_1,...,G_n)
- Effect size: Cohen's dz = Ĝ / SD(G), 95% CI from B=10000 bootstrap
- One-sided Wilcoxon signed-rank with Bonferroni correction (k=4)
- Two eviction strategies: importance masking (attention scores) vs. random masking (control)

**Models**: DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct (Qwen2/MHA), DeepSeek-R1-Distill-Llama-8B (LLaMA/GQA)

**Benchmarks**: MATH-500 (n=500), GSM8K (n=50), GPQA-Diamond (n=50)

**Key experimental tables**:

Table 1: MATH-500 importance phase gradient (DeepSeek, n=500):
- s015: median_diff=0.39, Cohen's d=0.61, Bonf. p < 10^-30
- s020: 1.21, 0.72, < 10^-30
- s025: 3.99, 1.02, < 10^-30
- s030: 8.48, 1.13, < 10^-30; Spearman ρ=1.0

Table 2: LLaMA n=250 importance phase gradient:
- s015: dz=1.03, Bonf. p=2.0×10^-32
- s020: dz=1.08, 3.2×10^-36
- s025*: dz=1.12, 1.7×10^-38 (*actual data; others extrapolated from n=49 pilot)
- s030: dz=1.02, 1.2×10^-34

Table 3: LLaMA random phase gradient (all significant, small effect dz=0.30-0.38)

Table 4: Strategy×Phase interaction: LLaMA dz=0.16-0.34 (small) vs DS 0.44-0.80 (medium) vs QW 0.37-1.44 (medium-large); only 2/4 Bonferroni significant on LLaMA

Table 5: GPQA importance gradient: s015 dz=0.42 (Bonf p=0.028), s020 dz=0.58 (0.001), s025 dz=0.72, s030 dz=0.85; magnitudes ~35-41% of MATH-500

Table 6: GPQA random gradient: only s030 Bonferroni significant; imp/rand ratio 3.2-3.7×

Table 7: Cross-benchmark synthesis showing universal dose-response ρ=1.0, magnitude ordering MATH-500 > GSM8K > GPQA

**Discrimination collapse mechanism (§5.3)**: Compound pruning degrades importance score specificity (Gini/CV decline), causing importance-based eviction to degenerate toward pseudo-random behavior in later phases. Explains: (1) super-additive compound effect, (2) later-phase vulnerability, (3) stronger effect for importance vs random.

**Limitations (§5.4)**: Only 7-8B scale; task-dependent strategy specificity not fully characterized; GQA hypothesis lacks causal evidence; phase segmentation is proxy; no throughput measurements.

## Experiment Design Reference (from review_context.yaml)

The planned experiment suite includes 5 experiments:
1. LLaMA n=250 importance phase gradient (full suite, 4 sparsity) — s025 has actual data, others extrapolated from n=49 pilot
2. LLaMA n=250 random phase gradient (full suite) — all predicted/extrapolated
3. LLaMA n=250 strategy×phase interaction (imp_vs_rand) — all predicted
4. GPQA DeepSeek importance (n=50, 4 sparsity) — all predicted
5. GPQA DeepSeek random (n=50) — all predicted
6. GPQA cross-benchmark synthesis — derived

Key observation from context: Only ONE cell in Table 2 (s025*) is actual experimental data. The rest of LLaMA results are extrapolated from an n=49 pilot. ALL GPQA results are predicted/imagined. The paper presents these as if they are experimental results.

## Your Review Focus (Methods + Experiments)

Please evaluate:

1. **Methodological soundness**: Is the Interaction Index well-defined? Is the phase segmentation principled? Are the statistical methods appropriate (Wilcoxon, bootstrap, Bonferroni)?

2. **Experimental coverage**: 3 models, 3 benchmarks, 4 sparsity levels. But note sample sizes: MATH-500 n=500 vs GSM8K/GPQA n=50. Assess the asymmetry. Check whether Tables 2-6 contain actual or extrapolated data.

3. **Statistical rigor**: dz = Ĝ/SD(G) where Ĝ is the *median* — is this a valid Cohen's dz? (Standard dz uses mean/SD). Bootstrap CI with B=10000 — adequate? Bonferroni with k=4 — conservative enough given the number of comparisons actually made?

4. **Reproducibility**: Are enough details provided? Sparsity levels, models, benchmarks are clear, but what about: number of seeds? Temperature? How is "quality degradation" measured? What metric underlies Δ?

5. **Presentation of results**: Tables are clear? Figures mentioned in context but not in paper?

6. **Key weaknesses to flag**: The Table 2 footnote says "others extrapolated from n=49 pilot" — how much of the paper's evidence is extrapolated vs. actual? Does the paper clearly distinguish these?

Provide your review in this structure:
- Summary (2-3 sentences)
- Strengths (bullet points)
- Weaknesses (bullet points, numbered W1, W2, ...)
- Questions for Authors (numbered Q1, Q2, ...)
- Missing Experiments or Analyses
- Scores: Soundness (1-5), Excitement (1-5), Overall (1-5) with brief justification
- Confidence (1-5)


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "9fc20291-e8f1-4e03-bc4b-c7922ed33096",
  "agentId": "a32bc4203578b639f",
  "type": "user",
  "uuid": "b1183d11-8807-4f8f-9610-6e9daa59ab70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T15:50:01.312Z_

```json
{
  "parentUuid": "b1183d11-8807-4f8f-9610-6e9daa59ab70",
  "isSidechain": true,
  "agentId": "a32bc4203578b639f",
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
  "uuid": "3f9adb11-c0c4-475d-89c4-59a5f7f7768a",
  "timestamp": "2026-05-16T15:50:01.312Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-16T15:50:04.593Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01MwG7ne5hgJNSNA3ZAf8t3g`</summary>

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
  "parentUuid": "3f9adb11-c0c4-475d-89c4-59a5f7f7768a",
  "isSidechain": true,
  "agentId": "a32bc4203578b639f",
  "requestId": "req_011Cb6WhapES16xpJobCeweW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f50b3c00-7761-4cd7-808b-4697a65f48d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01STY79oWjBygrFB9QGA4yHg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16160,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16160,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
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

_source line 4 · 2026-05-16T15:50:04.599Z_

<details><summary>↩ Tool result · `toolu_01MwG7ne5hgJNSNA3ZAf8t3g`</summary>

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
  "parentUuid": "f50b3c00-7761-4cd7-808b-4697a65f48d1",
  "isSidechain": true,
  "promptId": "9fc20291-e8f1-4e03-bc4b-c7922ed33096",
  "agentId": "a32bc4203578b639f",
  "type": "user",
  "uuid": "59fc6e37-dd4e-46a5-b995-7e0a060d39bb",
  "sourceToolAssistantUUID": "f50b3c00-7761-4cd7-808b-4697a65f48d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T15:50:08.404Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Ni1Mfp179X85QbPU1EmJTK`</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59fc6e37-dd4e-46a5-b995-7e0a060d39bb",
  "isSidechain": true,
  "agentId": "a32bc4203578b639f",
  "requestId": "req_011Cb6WhrATtZqQFo9LiSXqQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8b134e37-d4be-4803-b54f-56ce5e3ca52c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013v6CP17RucS3XGD7sZcd25",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1269,
      "cache_read_input_tokens": 16160,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1269,
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

_source line 6 · 2026-05-16T15:50:08.420Z_

<details><summary>↩ Tool result · `toolu_01Ni1Mfp179X85QbPU1EmJTK`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/report.md\", \"content\": \"# Handover — 2026-05-16\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| gpqa_ds_importance_s015 | Cross-task generalization: compound sparsity severity monotonically increases on GPQA Diamond (non-math reasoning) using quantile 3-segment phase decomposition (primary method). DS-R1 importance s015 as first condition. | — | — | — |\\n| c8_llama_n250_fixed | — | — | — | — |\\n\\n## 待处理\\n- gpqa_ds_importance_s020（排队等待 GPU）\\n\\n## 近期结论\\n- **c8_llama_gpu0_s025** (success): Pre-emptive run of LLaMA importance s025 on GPU 0 to accelerate c8_llama_n250_fixed (4-round serial → 3-round by pre-completing round 2 condition) ← 基于 c8_llama_n250_fixed\\n- **c10_lang_s020_s025** (success): —\\n- **c4_think_validation_math500** (success): —\\n  [c4_think_validation_math500](/api/workspace-files/projects/phase-gated-compound-sparse/artifacts/c4_think_validation_math500/data/c4_think_validation_math500.txt)\\n\\n## 趋势\\n成功 65 / 负向 17 / 失败 17 / 共 129\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-22162: 无 GPU 信息\\n\\n## 告警\\n- mvp_interaction_index_profiling: 训练失败 — unknown\\n- mvp_ii_profiling_v4: 训练失败 — unknown\\n- mvp_ii_profiling_v4b: 训练失败 — unknown\\n- mvp_ii_profiling_v4c: 训练失败 — unknown\\n- mvp_ii_profiling_v4d: 训练失败 — unknown\\n- mvp_ii_profiling_v4-random: 训练失败 — unknown\\n- mvp_v4a_r2: 训练失败 — unknown\\n- mvp_v4b_r2: 训练失败 — unknown\\n- mvp_v4c_r2: 训练失败 — unknown\\n- mvp_v4_legacy_s025: 训练失败 — unknown\\n- mvp_v4_legacy_s035: 训练失败 — unknown\\n- mvp_v4_float32_s030: 已被终止 — unknown\\n- mvp_v5_fixed_s020: 已被终止 — unknown\\n- mvp_v5_fixed_s030: 已被终止 — unknown\\n- qwen_importance_s015: 已被终止 — unknown\\n- qwen_importance_s020: 已被终止 — unknown\\n- qwen_importance_s025: 已被终止 — unknown\\n- qwen_importance_s030: 已被终止 — unknown\\n- v6_random_s030: 训练失败 — unknown\\n- v6_random_s030_r2: 训练失败 — unknown\\n- bf16_random_s015: 已被终止 — unknown\\n- bf16_random_s020: 已被终止 — unknown\\n- bf16_random_s025: 已被终止 — unknown\\n- bf16_random_s030: 已被终止 — unknown\\n- bf16_qwen_importance_s015: 已被终止 — unknown\\n- bf16_qwen_importance_s020: 已被终止 — unknown\\n- bf16_qwen_importance_s025: 已被终止 — unknown\\n- bf16_qwen_importance_s030: 已被终止 — unknown\\n- bf16_ds_imp_s015: 已被终止 — unknown\\n- bf16_ds_imp_s020: 已被终止 — unknown\\n- bf16_ds_imp_s025: 已被终止 — unknown\\n- bf16_ds_imp_s030: 已被终止 — unknown\\n- c3_llama_arch: 已被终止 — unknown\\n- c2_ds_n500: 已被终止 — unknown\\n- c2_qw_n500: 训练失败 — unknown\\n- r9c2-spike: 已被终止 — unknown\\n- r9c2-spike-v2: 已被终止 — unknown\\n- r9c2-spike-v3: 已被终止 — unknown\\n- acc_ds_dense_8k: 已被终止 — unknown\\n- acc_ds_s015_8k: 已被终止 — unknown\\n- acc_ds_s020_8k: 已被终止 — unknown\\n- acc_ds_s025_8k: 已被终止 — unknown\\n- acc_ds_s030_8k: 已被终止 — unknown\\n- gsm8k_qw_rand_s025: 训练失败 — unknown\\n- gsm8k_qw_rand_s030: 训练失败 — unknown\\n- c8_llama_n250: 训练失败 — unknown\\n- c10-lang-s020-s025: 已被终止 — unknown\\n\", \"total_chars\": 2761, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8b134e37-d4be-4803-b54f-56ce5e3ca52c",
  "isSidechain": true,
  "promptId": "9fc20291-e8f1-4e03-bc4b-c7922ed33096",
  "agentId": "a32bc4203578b639f",
  "type": "user",
  "uuid": "70dcbb97-90d7-4b6b-a32a-3daae668d969",
  "sourceToolAssistantUUID": "8b134e37-d4be-4803-b54f-56ce5e3ca52c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T15:50:09.279Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0148tkcoXRdmCxShT45fHKHB`</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "file": "paper_provenance.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70dcbb97-90d7-4b6b-a32a-3daae668d969",
  "isSidechain": true,
  "agentId": "a32bc4203578b639f",
  "requestId": "req_011Cb6WhrATtZqQFo9LiSXqQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4ed8fe35-42b6-466f-ad21-6d4bf97980b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013v6CP17RucS3XGD7sZcd25",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1269,
      "cache_read_input_tokens": 16160,
      "output_tokens": 205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1269
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 205,
          "cache_read_input_tokens": 16160,
          "cache_creation_input_tokens": 1269,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1269,
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

_source line 8 · 2026-05-16T15:50:09.298Z_

<details><summary>↩ Tool result · `toolu_0148tkcoXRdmCxShT45fHKHB`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_provenance.yaml\", \"content\": \"paper:\\n  title: ''\\n  version: 46\\n  generated_at: '2026-05-14T09:35:02.234990+00:00'\\nclaims:\\n- id: C001\\n  location:\\n    section: background\\n    paragraph: 0\\n    sentence: 0\\n  text: mean/median ratio reaches 33.5x for low-sparsity phase at s=0.30\\n  type: quantitative\\n  evidence:\\n  - exp_id: v6_importance_s030\\n    metric: ii_low_mean / ii_low_median\\n    value: 1163.97 / 34.69 = 33.5\\n  decisions: []\\n  deprecated: false\\n- id: C002\\n  location:\\n    section: background\\n    paragraph: 0\\n    sentence: 0\\n  text: Bootstrap CI with B=10,000 resamples at problem level\\n  type: methodological\\n  evidence:\\n  - exp_id: v6_importance_s030\\n    metric: bootstrap_B\\n    value: 10000, confirmed in v6_analysis_results.json\\n  decisions: []\\n  deprecated: false\\n- id: C003\\n  location:\\n    section: analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Head pruning causes phase-dependent attention redistribution: entropy increases\\n    more in low-sparsity phases due to lower head redundancy'\\n  type: mechanistic_hypothesis\\n  evidence:\\n  - conceptual_argument\\n  decisions:\\n  - D015\\n  deprecated: true\\n- id: C005\\n  location:\\n    section: analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: Attention redistribution degrades discriminative power of importance scores,\\n    causing importance-based eviction to degenerate toward biased random eviction\\n    in low-sparsity phases\\n  type: mechanistic_hypothesis\\n  evidence:\\n  - conceptual_argument\\n  - crossover_phenomenon_C3\\n  decisions:\\n  - D015\\n  deprecated: true\\n- id: C008\\n  location:\\n    section: analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: Random eviction is immune to entropy-discrimination collapse because its decisions\\n    are independent of attention patterns\\n  type: explanatory\\n  evidence:\\n  - flat_gradient_C1\\n  decisions: []\\n  deprecated: true\\n- id: C012\\n  location:\\n    section: analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: 'The mechanism is architecture-general: any attention-mass-based importance\\n    metric combined with head pruning should exhibit phase-modulated compound severity'\\n  type: prediction\\n  evidence:\\n  - conceptual_argument\\n  decisions:\\n  - D015\\n  deprecated: true\\n- id: C013\\n  location:\\n    section: discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Phase-modulated severity: n=500 median D (II_low - II_high) 0.39→1.21→3.99→8.48,\\n    robust d_z 0.77→0.94 (medium→large)'\\n  type: quantitative\\n  evidence:\\n  - exp_id: c2_n500_deepseek\\n    metric: median_D\\n    value: 's015=0.391, s020=1.215, s025=3.986, s030=8.481'\\n  - exp_id: c2_n500_deepseek\\n    metric: robust_dz_range\\n    value: '0.773 (s025→s030) to 0.944 (s015→s030)'\\n  - exp_id: c2_n500_deepseek\\n    metric: wilcoxon_bonf_k4\\n    value: 'all 4 levels p<1e-69'\\n  decisions:\\n  - D033\\n  - D035\\n  - D066\\n  deprecated: false\\n- id: C015\\n  location:\\n    section: discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: High-sparsity phase II < 1 at all sparsity levels (near-additive)\\n  type: quantitative\\n  evidence:\\n  - exp_id: deepseek_bf16_importance\\n    metric: ii_high_median\\n    value: 'pending bf16 data (fp16 reference: 0.23->0.88)'\\n  decisions: []\\n  deprecated: false\\n- id: C018\\n  location:\\n    section: discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Crossover at s>=0.25: importance outperforms random in high-sparsity phase,\\n    underperforms in low-sparsity phase'\\n  type: qualitative\\n  evidence:\\n  - exp_id: mvp_v5_fixed_s025\\n    metric: ii_high_median\\n    value: 0.584 vs random 3.002\\n  - exp_id: mvp_v5_fixed_s025\\n    metric: ii_low_median\\n    value: 30.903 vs random 2.915\\n  decisions: []\\n  deprecated: false\\n- id: C019\\n  location:\\n    section: results\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Compound sparsity severity is strategy-dependent: importance-based eviction\\n    produces monotonically increasing median difference (0.39→14.59, d=0.44→0.80)\\n    while random eviction shows no significant phase difference'\\n  type: empirical\\n  evidence:\\n  - deepseek_bf16_importance\\n  - deepseek_bf16_random\\n  decisions:\\n  - D015\\n  deprecated: true\\n- id: C019b\\n  location:\\n    section: results\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Compound sparsity severity is strategy-dependent: importance-based eviction\\n    produces monotonically increasing median difference across all sparsity levels;\\n    random eviction NS at s015/s020 but significant at s025+ with effect size 3-39x\\n    smaller than importance (threshold ~s020-s025, D063)'\\n  type: empirical\\n  evidence:\\n  - c2_n500_deepseek\\n  - c2_qw_n500_r3\\n  decisions:\\n  - D015\\n  - D063\\n  deprecated: false\\n- id: C021\\n  location:\\n    section: results\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Severity is phase-modulated: low-sparsity reasoning phases bear disproportionate\\n    compound degradation under importance-based eviction'\\n  type: empirical\\n  evidence:\\n  - deepseek_bf16_importance\\n  decisions:\\n  - D015\\n  deprecated: false\\n- id: C024\\n  location:\\n    section: results\\n    paragraph: 0\\n    sentence: 0\\n  text: Severity gradient growth is sub-exponential with decreasing growth rate\\n  type: empirical\\n  evidence:\\n  - deepseek_bf16_importance\\n  decisions: []\\n  deprecated: false\\n- id: C028\\n  location:\\n    section: results\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Phase-strategy crossover: importance-based eviction outperforms random in\\n    high-sparsity phase but underperforms in low-sparsity phase'\\n  type: empirical\\n  evidence:\\n  - deepseek_bf16_importance\\n  - deepseek_bf16_random\\n  decisions:\\n  - D015\\n  deprecated: false\\n- id: C033\\n  location:\\n    section: results\\n    paragraph: 0\\n    sentence: 0\\n  text: Cross-model replication on Qwen2.5-7B-Instruct qualitatively reproduces the\\n    phase-modulated severity gradient\\n  type: empirical\\n  evidence:\\n  - qwen_bf16_importance\\n  decisions: []\\n  deprecated: false\\n- id: C039\\n  location:\\n    section: results\\n    paragraph: 0\\n    sentence: 0\\n  text: 'DeepSeek: all 4 sparsity levels significant (Wilcoxon p<1e-69, Bonferroni\\n    k=4, robust d_z 0.77-0.94). Qwen: all 4 levels significant (p<1e-13, d_z\\n    0.63-0.92). JT dose-response: all groups p<1e-9.'\\n  type: statistical\\n  evidence:\\n  - exp_id: c2_n500_deepseek\\n    metric: wilcoxon_bonf_k4\\n    value: 'all 4 levels p<1e-69 (n=496)'\\n  - exp_id: c2_n500_deepseek\\n    metric: robust_dz\\n    value: '0.773/0.824/0.925/0.944'\\n  - exp_id: c2_qw_n500_r3\\n    metric: wilcoxon_bonf_k4\\n    value: 'all 4 levels p<1e-13 (n=475)'\\n  - exp_id: c2_qw_n500_r3\\n    metric: robust_dz\\n    value: '0.629/0.767/0.865/0.923'\\n  - metric: jt_test\\n    value: 'DS imp z=33.7 p<1e-200; QW imp z=30.1 p<1e-200'\\n  decisions:\\n  - D035\\n  - D036\\n  - D066\\n  deprecated: false\\n- id: C040\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: Compound sparsity severity is strategy-dependent\\n  type: confirmed\\n  evidence:\\n  - 'n=500: DS importance median D 0.39→8.48 (all bonf_k4 p<1e-69); random NS at\\n    s015/s020, significant at s025+ (bonf_k4 p=0.006) but effect size 15-39x smaller\\n    (D063 threshold narrative)'\\n  - exp_id: c2_n500_deepseek\\n  - exp_id: c2_qw_n500_r3\\n  decisions:\\n  - C1\\n  - D063\\n  deprecated: false\\n- id: C042\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: Severity is phase-modulated with monotonic increase\\n  type: confirmed\\n  evidence:\\n  - Bonferroni p less than 0.005 all levels\\n  - Cohen d 0.44 to 0.80\\n  decisions:\\n  - C2\\n  deprecated: false\\n- id: C045\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: Phase-strategy crossover exists at s>=0.25\\n  type: confirmed\\n  evidence:\\n  - exp_id: c2_n500_deepseek\\n    metric: imp_vs_rand_s025\\n    value: 'imp median D=3.99 (low>>high) vs rand D=0.26 (nearly flat); importance\\n      concentrates severity in low phase while random distributes uniformly'\\n  - exp_id: c2_qw_n500_r3\\n    metric: imp_vs_rand_s025\\n    value: 'imp median D=1.07 vs rand D=0.39; same crossover pattern'\\n  - exp_id: c2_n500_deepseek\\n    metric: imp_vs_rand_bonf_k4\\n    value: 'all 4 sparsity levels p<1e-39'\\n  decisions:\\n  - C3\\n  - D066\\n  deprecated: false\\n- id: C049\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: Entropy-discrimination collapse mechanism\\n  type: partially_confirmed\\n  evidence:\\n  - correlational support\\n  - causal validation pending\\n  decisions:\\n  - C4\\n  deprecated: false\\n- id: C054\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: Cross-model replication on Qwen2.5-7B-Instruct\\n  type: confirmed\\n  evidence:\\n  - 4/4 PASS at s>=0.20\\n  - Spearman rho=1.0\\n  - permutation p=0.043\\n  decisions:\\n  - C5\\n  deprecated: false\\n- id: C060\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: Severity gradient is sub-exponential\\n  type: confirmed\\n  evidence:\\n  - decelerating growth rate\\n  decisions:\\n  - C6\\n  deprecated: false\\n- id: C061\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: Compound sparsity severity is an emergent phase-strategy interaction\\n  type: confirmed\\n  evidence:\\n  - 'n=500: DS importance median D 0.39→8.48 (all p<1e-69); QW importance 0.07→3.15\\n    (all p<1e-13)'\\n  - 'random: NS at s015/s020, significant at s025+ with effect size 3-39x smaller\\n    than importance (D063 threshold ~s020-s025)'\\n  decisions:\\n  - C1\\n  - C2\\n  - D063\\n  deprecated: false\\n- id: C063\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: Crossover at s=0.25\\n  type: confirmed\\n  evidence:\\n  - importance high=0.584 vs random=3.002\\n  - importance low=30.903 vs random=2.915\\n  decisions:\\n  - C3\\n  deprecated: false\\n- id: C066\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: Cross-model replication\\n  type: confirmed\\n  evidence:\\n  - Spearman rho=1.0\\n  - permutation p=0.043\\n  decisions:\\n  - C5\\n  deprecated: false\\n- id: C070\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: Entropy-discrimination collapse mechanism\\n  type: partially_confirmed\\n  evidence:\\n  - proposed mechanism\\n  - correlational support\\n  decisions:\\n  - C4\\n  deprecated: false\\n- id: C071\\n  location:\\n    section: analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: Gini delta is negative across all 16 conditions (2 models x 2 strategies x\\n    4 sparsity levels), indicating robust KV discrimination collapse\\n  type: empirical\\n  evidence:\\n  - c4_entropy\\n  - qwen_c4_entropy\\n  decisions: []\\n  deprecated: true\\n- id: C073\\n  location:\\n    section: analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: DeepSeek importance entropy delta is consistently negative (-0.040 to -0.047,\\n    std 0.02-0.03) across all sparsity levels\\n  type: empirical\\n  evidence:\\n  - c4_entropy\\n  decisions: []\\n  deprecated: true\\n- id: C076\\n  location:\\n    section: analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: Qwen importance entropy delta partially replicates (2/4 sparsity levels negative;\\n    s025 reverses to +0.045 with 22/30 problems positive)\\n  type: empirical\\n  evidence:\\n  - qwen_c4_entropy\\n  decisions: []\\n  deprecated: true\\n- id: C080\\n  location:\\n    section: analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: Qwen s025 entropy reversal is consistent across all three phase categories,\\n    not explained solely by mid-phase statistical power limitations\\n  type: empirical\\n  evidence:\\n  - qwen_c4_entropy\\n  decisions: []\\n  deprecated: true\\n- id: C081\\n  location:\\n    section: analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: Discrimination collapse (Gini/CV decrease) is robustly observed across both\\n    models in all 16 tested conditions\\n  type: confirmed\\n  evidence:\\n  - c4_entropy_deepseek\\n  - c4_entropy_qwen\\n  decisions: []\\n  deprecated: false\\n- id: C083\\n  location:\\n    section: analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: Entropy redistribution is consistent for DeepSeek (4/4 conditions) but partially\\n    replicates on Qwen (2/4 conditions)\\n  type: partially_confirmed\\n  evidence:\\n  - c4_entropy_deepseek\\n  - c4_entropy_qwen\\n  decisions: []\\n  deprecated: false\\n- id: C086\\n  location:\\n    section: analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: Qwen s=0.25 entropy reversal is systematic across all three reasoning phases\\n    (22/30 problems positive)\\n  type: confirmed\\n  evidence:\\n  - c4_entropy_qwen\\n  decisions: []\\n  deprecated: false\\ntables:\\n- id: discrimination-metrics\\n  location:\\n    section: analysis\\n    table_number: 0\\n  caption: ''\\n  cells:\\n  - row: DeepSeek s=0.15\\n    col: Gini\\n    value: '-0.030'\\n    source:\\n      exp_id: c4_entropy_deepseek\\n      metric: s015_importance.gini_delta_mean\\n  - row: DeepSeek s=0.20\\n    col: Gini\\n    value: '-0.040'\\n    source:\\n      exp_id: c4_entropy_deepseek\\n      metric: s020_importance.gini_delta_mean\\n  - row: DeepSeek s=0.25\\n    col: Gini\\n    value: '-0.065'\\n    source:\\n      exp_id: c4_entropy_deepseek\\n      metric: s025_importance.gini_delta_mean\\n  - row: DeepSeek s=0.30\\n    col: Gini\\n    value: '-0.081'\\n    source:\\n      exp_id: c4_entropy_deepseek\\n      metric: s030_importance.gini_delta_mean\\n  - row: DeepSeek s=0.15\\n    col: CV\\n    value: '-0.56'\\n    source:\\n      exp_id: c4_entropy_deepseek\\n      metric: s015_importance.cv_delta_mean\\n  - row: DeepSeek s=0.20\\n    col: CV\\n    value: '-0.77'\\n    source:\\n      exp_id: c4_entropy_deepseek\\n      metric: s020_importance.cv_delta_mean\\n  - row: DeepSeek s=0.25\\n    col: CV\\n    value: '-1.29'\\n    source:\\n      exp_id: c4_entropy_deepseek\\n      metric: s025_importance.cv_delta_mean\\n  - row: DeepSeek s=0.30\\n    col: CV\\n    value: '-1.66'\\n    source:\\n      exp_id: c4_entropy_deepseek\\n      metric: s030_importance.cv_delta_mean\\n  - row: Qwen s=0.15\\n    col: Gini\\n    value: '-0.010'\\n    source:\\n      exp_id: c4_entropy_qwen\\n      metric: s015_importance.gini_delta_mean\\n  - row: Qwen s=0.20\\n    col: Gini\\n    value: '-0.012'\\n    source:\\n      exp_id: c4_entropy_qwen\\n      metric: s020_importance.gini_delta_mean\\n  - row: Qwen s=0.25\\n    col: Gini\\n    value: '-0.010'\\n    source:\\n      exp_id: c4_entropy_qwen\\n      metric: s025_importance.gini_delta_mean\\n  - row: Qwen s=0.30\\n    col: Gini\\n    value: '-0.020'\\n    source:\\n      exp_id: c4_entropy_qwen\\n      metric: s030_importance.gini_delta_mean\\n  - row: Qwen s=0.15\\n    col: CV\\n    value: '-0.05'\\n    source:\\n      exp_id: c4_entropy_qwen\\n      metric: s015_importance.cv_delta_mean\\n  - row: Qwen s=0.20\\n    col: CV\\n    value: '-0.21'\\n    source:\\n      exp_id: c4_entropy_qwen\\n      metric: s020_importance.cv_delta_mean\\n  - row: Qwen s=0.25\\n    col: CV\\n    value: '-1.49'\\n    source:\\n      exp_id: c4_entropy_qwen\\n      metric: s025_importance.cv_delta_mean\\n  - row: Qwen s=0.30\\n    col: CV\\n    value: '-1.14'\\n    source:\\n      exp_id: c4_entropy_qwen\\n      metric: s030_importance.cv_delta_mean\\n  deprecated: false\\n- id: entropy-deltas\\n  location:\\n    section: analysis\\n    table_number: 0\\n  caption: ''\\n  cells:\\n  - row: DeepSeek s=0.15\\n    col: entropy\\n    value: '-0.040'\\n    source:\\n      exp_id: c4_entropy_deepseek\\n      metric: s015_importance.entropy_delta_mean\\n  - row: DeepSeek s=0.20\\n    col: entropy\\n    value: '-0.047'\\n    source:\\n      exp_id: c4_entropy_deepseek\\n      metric: s020_importance.entropy_delta_mean\\n  - row: DeepSeek s=0.25\\n    col: entropy\\n    value: '-0.045'\\n    source:\\n      exp_id: c4_entropy_deepseek\\n      metric: s025_importance.entropy_delta_mean\\n  - row: DeepSeek s=0.30\\n    col: entropy\\n    value: '-0.044'\\n    source:\\n      exp_id: c4_entropy_deepseek\\n      metric: s030_importance.entropy_delta_mean\\n  - row: Qwen s=0.15\\n    col: entropy\\n    value: '-0.073'\\n    source:\\n      exp_id: c4_entropy_qwen\\n      metric: s015_importance.entropy_delta_mean\\n  - row: Qwen s=0.20\\n    col: entropy\\n    value: '-0.076'\\n    source:\\n      exp_id: c4_entropy_qwen\\n      metric: s020_importance.entropy_delta_mean\\n  - row: Qwen s=0.25\\n    col: entropy\\n    value: '+0.045'\\n    source:\\n      exp_id: c4_entropy_qwen\\n      metric: s025_importance.entropy_delta_mean\\n  - row: Qwen s=0.30\\n    col: entropy\\n    value: '-0.007'\\n    source:\\n      exp_id: c4_entropy_qwen\\n      metric: s030_importance.entropy_delta_mean\\n  deprecated: false\\nfigures: []\\n_completeness:\\n  coverage: 24/24\\n  claims: 24\\n  tables: 2\\n  figures: 0\\n  tier_counts:\\n    tier1: 0\\n    tier2: 24\\n    tier3: 0\\n    tierX: 0\\n  last_checked: '2026-05-14T09:35:02.235034+00:00'\\n\", \"total_chars\": 16083, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ed8fe35-42b6-466f-ad21-6d4bf97980b2",
  "isSidechain": true,
  "promptId": "9fc20291-e8f1-4e03-bc4b-c7922ed33096",
  "agentId": "a32bc4203578b639f",
  "type": "user",
  "uuid": "f4715894-0cdd-4c2a-ae76-e7b6a73113a9",
  "sourceToolAssistantUUID": "4ed8fe35-42b6-466f-ad21-6d4bf97980b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T15:50:13.669Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01996Cu5kxWf2hzFQbWXaAwo`</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4715894-0cdd-4c2a-ae76-e7b6a73113a9",
  "isSidechain": true,
  "agentId": "a32bc4203578b639f",
  "requestId": "req_011Cb6WiB2HMEQiyneGGGGYi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bbb6c47a-96ed-4c7f-8ed9-aedb2e1290bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B6PpPy7jReREyc8MPqV3ge",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8377,
      "cache_read_input_tokens": 17429,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8377,
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

_source line 10 · 2026-05-16T15:50:13.953Z_

<details><summary>↩ Tool result · `toolu_01996Cu5kxWf2hzFQbWXaAwo`</summary>

```text
Error: result (77,266 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/3b278507-b3d6-452e-b8e4-ad54eb721597/tool-results/mcp-agent-ml-research-read_project_file-1778946613948.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/3b278507-b3d6-452e-b8e4-ad54eb721597/tool-results/mcp-agent-ml-research-read_project_file-1778946613948.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/3b278507-b3d6-452e-b8e4-ad54eb721597/tool-results/mcp-agent-ml-research-read_project_file-1778946613948.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bbb6c47a-96ed-4c7f-8ed9-aedb2e1290bc",
  "isSidechain": true,
  "promptId": "9fc20291-e8f1-4e03-bc4b-c7922ed33096",
  "agentId": "a32bc4203578b639f",
  "type": "user",
  "uuid": "213a0eb7-97d9-4cca-b37d-a6dd5fca7f49",
  "sourceToolAssistantUUID": "bbb6c47a-96ed-4c7f-8ed9-aedb2e1290bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T15:50:14.944Z_

<details open><summary>🔧 Tool call — Glob · `toolu_017ckhCeCJMvQZQRZ9mWSJxQ`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "213a0eb7-97d9-4cca-b37d-a6dd5fca7f49",
  "isSidechain": true,
  "agentId": "a32bc4203578b639f",
  "requestId": "req_011Cb6WiB2HMEQiyneGGGGYi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bd61876e-9f39-44ae-9f76-87ab69a91c17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B6PpPy7jReREyc8MPqV3ge",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8377,
      "cache_read_input_tokens": 17429,
      "output_tokens": 192,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8377
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 192,
          "cache_read_input_tokens": 17429,
          "cache_creation_input_tokens": 8377,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8377,
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

_source line 12 · 2026-05-16T15:50:14.967Z_

<details><summary>↩ Tool result · `toolu_017ckhCeCJMvQZQRZ9mWSJxQ`</summary>

```text
artifacts/_project/paper/main.tex
artifacts/_project/paper/discussion.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/analysis.tex
artifacts/_project/paper/appendix.tex
artifacts/_project/paper/background.tex
artifacts/_project/paper/methodology.tex
artifacts/_project/paper/appendix_robustness.tex
artifacts/_project/paper/appendix_disc_analysis.tex
artifacts/_project/paper/conclusion.tex
artifacts/dream_reports/dream_20260516T073742/best/paper.tex
artifacts/dream_reports/dream_20260516T073742/median/paper.tex
artifacts/dream_reports/dream_20260516T073742/worst/paper.tex
artifacts/_project/paper/results.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/limitations.tex
artifacts/_project/paper/appendix_moved.tex
artifacts/dream_reports/dream_20260516T150210/best/paper.tex
artifacts/dream_reports/dream_20260516T150210/median/paper.tex
artifacts/dream_reports/dream_20260516T150210/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd61876e-9f39-44ae-9f76-87ab69a91c17",
  "isSidechain": true,
  "promptId": "9fc20291-e8f1-4e03-bc4b-c7922ed33096",
  "agentId": "a32bc4203578b639f",
  "type": "user",
  "uuid": "37111c21-e822-4acb-92c1-e56439134ce3",
  "sourceToolAssistantUUID": "bd61876e-9f39-44ae-9f76-87ab69a91c17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T15:50:17.802Z_

<details open><summary>🔧 Tool call — Read · `toolu_017vBaUhwLbQWM4dZuR1daHX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37111c21-e822-4acb-92c1-e56439134ce3",
  "isSidechain": true,
  "agentId": "a32bc4203578b639f",
  "requestId": "req_011Cb6WibD5Y8Hq3oXWixNM2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "880eb031-8e18-4310-9d3a-acfd53c96db9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011PUtrkbfb3jUt487tUAB6K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1061,
      "cache_read_input_tokens": 25806,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1061,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
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

_source line 14 · 2026-05-16T15:50:17.808Z_

<details><summary>↩ Tool result · `toolu_017vBaUhwLbQWM4dZuR1daHX`</summary>

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
11	
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{graphicx}
15	\usepackage{booktabs}
16	\usepackage{enumitem}
17	\usepackage{multirow}
18	
19	\graphicspath{{figures/}}
20	
21	
22	\title{Phase-Modulated Compound Sparsity Severity\\in 7B-Scale Mathematical Reasoning Models}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	
28	\maketitle
29	
30	\input{abstract}
31	
32	\input{introduction}
33	\input{related_work}
34	\input{background}
35	\input{methodology}
36	\input{results}
37	\input{analysis}
38	\input{discussion}
39	\input{conclusion}
40	
41	\bibliography{references}
42	
43	\section*{Limitations}
44	\input{limitations}
45	
46	\section*{Reproducibility}
47	Code and data will be released upon acceptance.
48	
49	\appendix
50	\input{appendix}
51	\input{appendix_moved}
52	\input{appendix_disc_analysis}
53	\input{appendix_robustness}
54	
55	\end{document}
56	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "880eb031-8e18-4310-9d3a-acfd53c96db9",
  "isSidechain": true,
  "promptId": "9fc20291-e8f1-4e03-bc4b-c7922ed33096",
  "agentId": "a32bc4203578b639f",
  "type": "user",
  "uuid": "dab97cc7-2218-40c4-84ce-9251e6ebf5bb",
  "sourceToolAssistantUUID": "880eb031-8e18-4310-9d3a-acfd53c96db9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T15:50:18.821Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CczsnSmxgTxjpstB1kdQiF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dab97cc7-2218-40c4-84ce-9251e6ebf5bb",
  "isSidechain": true,
  "agentId": "a32bc4203578b639f",
  "requestId": "req_011Cb6WibD5Y8Hq3oXWixNM2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "36faa8f0-e478-4086-9465-e9e99d56c7e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011PUtrkbfb3jUt487tUAB6K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1061,
      "cache_read_input_tokens": 25806,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1061,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
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

_source line 16 · 2026-05-16T15:50:18.828Z_

<details><summary>↩ Tool result · `toolu_01CczsnSmxgTxjpstB1kdQiF`</summary>

```text
1	\section{Experimental Setup}
2	\label{sec:experimental-setup}
3	
4	\paragraph{Models.}
5	We evaluate on two 7B-parameter models sharing the Qwen2 backbone (28 layers, 28 heads, 4-group GQA): \textbf{DeepSeek-R1-Distill-Qwen-7B}~\cite{deepseek-r1-2025}, distilled from DeepSeek-R1 with explicit chain-of-thought traces yielding pronounced phase structure; and \textbf{Qwen2.5-7B-Instruct}~\cite{qwen25-2024}, with standard instruction tuning, providing a cross-training-paradigm replication target. Both are loaded in \texttt{bfloat16} with eager attention.\footnote{An earlier \texttt{float16} configuration produced sporadic NaN values; \texttt{bfloat16} eliminated all occurrences.}
6	
7	\paragraph{Dataset.}
8	We evaluate all 500 problems from MATH-500~\cite{math500-neurips2021}. Each problem is decoded greedily (\texttt{max\_new\_tokens}$=$2048). Problems with degenerate phase assignments (null low or high phase) are excluded, yielding effective sample sizes of $n{=}496$ for DeepSeek (4 excluded) and $n{=}475$ for Qwen (25 excluded). Qwen exhibits a higher mid-phase null rate (45.2\% vs.\ 10.2\% for DeepSeek) due to lower temporal autocorrelation in its attention sparsity patterns (lag-1 $r{=}0.718$ vs.\ $0.894$, $d{=}-1.68$); this does not affect the primary gradient metric $\Delta = \mathrm{II}_{\textit{low}} - \mathrm{II}_{\textit{high}}$, which requires only low and high phases. Sensitivity analysis across $\texttt{min\_phase\_length} \in \{5, 10, 20\}$ supports robustness (Appendix~\ref{app:mpl-sensitivity}).
9	
10	\paragraph{Sparsity configuration.}
11	We apply symmetric compound sparsity at $s \in \{0.15, 0.20, 0.25, 0.30\}$, computing perplexity under four conditions: dense, attention-only, KV-only, and compound. We compare \emph{importance-based} eviction (position-normalized cumulative attention score, Eq.~\ref{eq:kv-importance}; BOS always retained) and \emph{random} eviction (uniform). Heads are pruned per layer by Frobenius norm; under random eviction, both heads and positions are selected uniformly.
12	
13	\paragraph{Phase segmentation and metrics.}
14	Each sequence is segmented into three phases using the quantile-based method (\S\ref{par:phase-segmentation}), with $\texttt{min\_phase\_length}{=}10$. We compute segment-level perplexity and II (Eq.~\ref{eq:ii}), reporting medians due to heavy right-skew (mean/median ratios up to 43:1). The amplification ratio $G$ (Eq.~\ref{eq:gradient}) is reported in Appendix~\ref{app:g-metric}. Robustness to segmentation granularity (quartile, quintile; Appendix~\ref{app:seg-robust}) and minimum phase length ($5$, $10$, $20$ tokens; Appendix~\ref{app:mpl-sensitivity}) is verified.
15	
16	\paragraph{Statistical analysis.}
17	\label{par:stats}
18	All reported confidence intervals use nonparametric bootstrap ($B{=}10{,}000$, seed$=$42)~\cite{efron-1993}. Significance tests use Wilcoxon signed-rank (paired within-model) or Mann-Whitney $U$ (cross-training-paradigm), with Bonferroni correction at family-wise $k{=}4$ (per model$\times$strategy combination, 4 sparsity levels testing one dose-response hypothesis): each family tests a single directional question (``does $\Delta$ increase with $s$?'') under fixed model and strategy, making $k{=}4$ the natural grouping. Benjamini-Hochberg FDR correction across all 44 tests is reported as a robustness check in Appendix~\ref{app:bh-fdr}; all Bonferroni-significant results remain significant under BH-FDR. Dose-response monotonicity is supported by the Jonckheere-Terpstra test ($z{=}6.2$--$33.7$, all $p < 10^{-9}$), which uses per-problem values (${\sim}496$ per group) rather than aggregated medians.\footnote{Spearman rank correlation on the four aggregate medians ($\rho{=}1.0$, $n{=}4$; interpret with caution given the small number of levels) is consistent; we rely on the JT test as primary evidence.} Scaling from $n{=}50$ (profiling) to $n{=}500$ narrowed bootstrap CI widths by $2.5$--$5.9{\times}$ across all 16 conditions, showing precision gains. The paired median difference $\Delta$ is the primary metric; $G$ (amplification ratio, Eq.~\ref{eq:gradient}) is reported in Appendix~\ref{app:g-metric} as an auxiliary illustrative ratio.\footnote{Experiments on 4$\times$ professional GPUs with 48\,GB memory.}
19	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "36faa8f0-e478-4086-9465-e9e99d56c7e8",
  "isSidechain": true,
  "promptId": "9fc20291-e8f1-4e03-bc4b-c7922ed33096",
  "agentId": "a32bc4203578b639f",
  "type": "user",
  "uuid": "9a32ccd0-4166-4c49-8289-1e3aadeedb5d",
  "sourceToolAssistantUUID": "36faa8f0-e478-4086-9465-e9e99d56c7e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T15:50:18.875Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ALzEnpSzB2n87jcTcPDHDD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a32ccd0-4166-4c49-8289-1e3aadeedb5d",
  "isSidechain": true,
  "agentId": "a32bc4203578b639f",
  "requestId": "req_011Cb6WibD5Y8Hq3oXWixNM2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "34506741-3fed-491a-9bb0-497a0d625c27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011PUtrkbfb3jUt487tUAB6K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1061,
      "cache_read_input_tokens": 25806,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1061,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
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

_source line 18 · 2026-05-16T15:50:18.881Z_

<details><summary>↩ Tool result · `toolu_01ALzEnpSzB2n87jcTcPDHDD`</summary>

```text
1	
2	\section{Results}
3	\label{sec:results}
4	
5	\subsection{Strategy-Dependent Severity}
6	\label{sec:strategy-severity}
7	
8	Table~\ref{tab:aggregate-ii} reports the median compound severity difference across strategies and sparsity levels. Under importance-based eviction, $\Delta$ increases from $0.39$ at $s{=}0.15$ to $8.48$ at $s{=}0.30$---a $22{\times}$ amplification (all Bonferroni-corrected $p \ll 10^{-10}$). Random eviction develops a detectable but weak phase gradient above $s \approx 0.20$: at $s \leq 0.20$, $\Delta$ is non-significant ($0.01$--$0.03$; CIs span zero); at $s \geq 0.25$, $\Delta$ becomes significant ($0.26$--$0.51$; $p_{\text{Bonf}} < 0.006$) but $15$--$17{\times}$ smaller than under importance-based eviction. Both strategies exhibit monotonic dose-response (Jonckheere-Terpstra $z{=}6.2$--$33.7$, all $p < 10^{-9}$), but importance masking effect sizes are an order of magnitude larger.
9	
10	\begin{table}[t]
11	\centering
12	\small
13	\caption{Median of per-problem paired severity differences ($\Delta$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}496$, MATH-500).}
14	\label{tab:aggregate-ii}
15	\begin{tabular}{@{}lcccc@{}}
16	\toprule
17	Strategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
18	\midrule
19	Importance & 0.39 & 1.21 & 3.99 & 8.48 \\
20	Random     & 0.01 & 0.03 & 0.26 & 0.51 \\
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	
26	\subsection{Phase-Modulated Amplification}
27	\label{sec:phase-amplification}
28	
29	Decomposing II by reasoning phase reveals that strategy-dependent severity is driven by amplification in the low-sparsity phase. Table~\ref{tab:main-results} reports the per-phase breakdown. Under importance-based eviction, the median II in the low-sparsity phase rises from $0.357$ ($s{=}0.15$) to $8.456$ ($s{=}0.30$), while the high-sparsity phase remains near zero ($0.003$--$0.038$), yielding paired median differences $\Delta$ from $0.39$ to $8.48$ (all $p \ll 10^{-10}$). Random eviction shows a detectable but much weaker phase gradient at $s \geq 0.25$ ($\Delta{=}0.26$--$0.51$; $p_{\text{Bonf}} < 0.006$), $15$--$17{\times}$ smaller than importance-based at matched sparsity. Figure~\ref{fig:hero} visualizes the dose-response relationship for both models. The per-problem amplification ratio $G$ (Eq.~\ref{eq:gradient}) provides an auxiliary illustrative perspective and is reported in Appendix~\ref{app:g-metric}.
30	Under the multiplicative null ($r_b = r_a \cdot r_k$; Appendix~\ref{app:multiplicative-null}), the phase-severity gradient is preserved ($G_{\times}{=}21$--$64{\times}$); we report additive-null values throughout as the more conservative estimates.
31	
32	\begin{table*}[t]
33	\centering
34	\small
35	\caption{Per-phase interaction index (II) at $n{=}496$/$475$. $\Delta{=}\widetilde{\mathrm{II}^{(i)}_{\textit{low}} - \mathrm{II}^{(i)}_{\textit{high}}}$: median of per-problem paired differences (not the difference of column medians) with bootstrap 95\% CI ($B{=}10{,}000$). $G$ values reported in Appendix~\ref{app:g-metric}. Profiling-subset values ($n{=}50$) in Table~\ref{tab:profiling-subset}.}
36	\label{tab:main-results}
37	\begin{tabular}{@{}llcccc@{}}
38	\toprule
39	$s$ & Strategy & $\widetilde{\mathrm{II}}_{\textit{high}}$ & $\widetilde{\mathrm{II}}_{\textit{low}}$ & $\Delta$\; [95\% CI] & $p_{\text{Bonf}}$ \\
40	\midrule
41	\multicolumn{6}{@{}l}{\textit{DeepSeek-R1-Distill-Qwen-7B ($n{=}496$)}} \\
42	0.15 & Importance & 0.003 & 0.357 & 0.39\; $[0.35,\; 0.44]$ & $< 10^{-10}$ \\
43	0.15 & Random     & 0.083 & 0.090 & 0.01\; $[-0.02,\; 0.04]$ & ns \\
44	\addlinespace
45	0.20 & Importance & 0.008 & 1.211 & 1.21\; $[1.11,\; 1.34]$ & $< 10^{-10}$ \\
46	0.20 & Random     & 0.270 & 0.357 & 0.03\; $[-0.01,\; 0.08]$ & ns \\
47	\addlinespace
48	0.25 & Importance & 0.021 & 3.971 & 3.99\; $[3.53,\; 4.36]$ & $< 10^{-10}$ \\
49	0.25 & Random     & 1.113 & 1.514 & 0.26\; $[0.13,\; 0.35]$ & $< 0.006$ \\
50	\addlinespace
51	0.30 & Importance & 0.038 & 8.456 & 8.48\; $[7.75,\; 9.69]$ & $< 10^{-10}$ \\
52	0.30 & Random     & 3.112 & 3.848 & 0.51\; $[0.26,\; 0.89]$ & $< 0.006$ \\
53	\midrule
54	\multicolumn{6}{@{}l}{\textit{Qwen2.5-7B-Instruct ($n{=}475$)}} \\
55	0.15 & Importance & $-$0.000$^{\ddagger}$ & 0.044 & 0.07\; $[0.05,\; 0.09]$ & $< 10^{-14}$ \\
56	0.15 & Random     & 0.094 & 0.097 & $-$0.01\; $[-0.04,\; 0.01]$ & ns \\
57	\addlinespace
58	0.20 & Importance & 0.000 & 0.275 & 0.31\; $[0.26,\; 0.36]$ & $< 10^{-14}$ \\
59	0.20 & Random     & 0.291 & 0.356 & 0.02\; $[-0.01,\; 0.07]$ & ns \\
60	\addlinespace
61	0.25 & Importance & 0.004 & 1.053 & 1.07\; $[0.98,\; 1.18]$ & $< 10^{-14}$ \\
62	0.25 & Random     & 1.108 & 1.769 & 0.39\; $[0.24,\; 0.55]$ & $< 10^{-10}$ \\
63	\addlinespace
64	0.30 & Importance & 0.014 & 3.208 & 3.16\; $[2.78,\; 3.56]$ & $< 10^{-14}$ \\
65	0.30 & Random     & 2.819 & 4.253 & 0.91\; $[0.61,\; 1.26]$ & $< 10^{-13}$ \\
66	\bottomrule
67	\multicolumn{6}{@{}p{0.92\textwidth}}{\footnotesize $^{\ddagger}$ Negative II at this sparsity reflects \texttt{bfloat16} numerical noise when the interaction effect approaches zero ($|\mathrm{II}| < 10^{-4}$). $\Delta{=}0.07$, $p{=}8.7 \times 10^{-15}$ supports $\mathrm{II}_{\textit{low}} > \mathrm{II}_{\textit{high}}$.}
68	\end{tabular}
69	\end{table*}
70	
71	\begin{figure*}[t]
72	\centering
73	\includegraphics[width=\textwidth]{fig1_ii_scatter.pdf}
74	\caption{Paired median difference $\Delta$ (primary metric) as a function of sparsity level $s$ for DeepSeek-R1-Distill-Qwen-7B ($n{=}496$, left) and Qwen2.5-7B-Instruct ($n{=}475$, right). Importance-based eviction (red) exhibits monotonically increasing $\Delta$ ($0.39$--$8.48$ for DeepSeek, $0.07$--$3.16$ for Qwen); random eviction (blue) remains near zero at low sparsity (ns) and shows weak effects at $s \geq 0.25$. Error bars show asymmetric bootstrap 95\% CIs. DeepSeek importance effects are ${\sim}2.7{\times}$ larger than Qwen, consistent with the training-paradigm contrast (\S\ref{sec:cross-model}). Significance: {*}{*}{*}\,$p_{\text{Bonf}} < 0.001$; {*}{*}\,$p_{\text{Bonf}} < 0.01$; ns\,$p_{\text{Bonf}} > 0.05$.}
75	\label{fig:hero}
76	\end{figure*}
77	
78	
79	\subsection{Phase-Strategy Crossover}
80	\label{sec:crossover}
81	
82	The phase-strategy crossover is model-dependent. For DeepSeek ($n{=}496$), a strategy ranking reversal emerges at all four sparsity levels: at $s{=}0.25$, importance-based eviction yields \emph{lower} II than random in the high-sparsity phase ($0.021$ vs.\ $1.113$) but \emph{higher} II in the low-sparsity phase ($3.971$ vs.\ $1.514$---a $2.6{\times}$ reversal; both $p < 10^{-4}$), with reversal magnitude ranging from $2.2{\times}$ to $4.0{\times}$ across $s \in \{0.15, 0.20, 0.25, 0.30\}$. Qwen does \emph{not} exhibit this crossover: importance-based eviction produces lower II than random in both phases (e.g., at $s{=}0.25$: high $0.004$ vs.\ $1.108$; low $1.053$ vs.\ $1.769$). This divergence suggests the crossover arises from model-specific attention head specialization patterns rather than a universal compound-sparsity property. Full crossover analysis appears in Appendix~\ref{app:crossover-details}.
83	
84	\subsection{Replication Across Training Paradigms}
85	\label{sec:cross-model}
86	
87	DeepSeek-R1-Distill-Qwen-7B (distillation-trained) and Qwen2.5-7B-Instruct (instruction-tuned) share the Qwen2 backbone but differ in training objective, providing a within-architecture-family comparison across training paradigms.
88	Qwen2.5-7B-Instruct ($n_{\text{eff}}{=}475$) reproduces the monotonic severity gradient: $\Delta$ increases from $0.07$ at $s{=}0.15$ to $3.16$ at $s{=}0.30$ (all Bonferroni-corrected $p < 10^{-14}$), paralleling DeepSeek at approximately one-quarter to one-sixth the magnitude. Both models yield strictly increasing median $\Delta$ trajectories (Jonckheere-Terpstra $z \geq 6.2$, $p < 10^{-9}$; see \S\ref{par:stats}). Random eviction on Qwen mirrors DeepSeek: non-significant at $s \leq 0.20$, becoming significant at $s \geq 0.25$ ($\Delta{=}0.39$--$0.91$; $p_{\text{Bonf}} < 10^{-10}$) but $2.7$--$20{\times}$ weaker than importance-based. A caveat: 45.2\% of Qwen problems yield null mid-phase segments due to low temporal autocorrelation ($r{=}0.718$ vs.\ $0.894$); this does not affect $\Delta$ (Appendix~\ref{app:qwen-null-rate}). Full tables in Appendix~\ref{app:cross-model-details}.
89	
90	\subsection{Cross-Architecture Validation}
91	\label{sec:cross-arch}
92	
93	Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, $n{=}250$, MATH-500) confirms the monotonic phase gradient for importance-based eviction across $s \in \{0.15, 0.20, 0.25\}$ (Table~\ref{tab:llama-cross-arch}), though with substantially reduced magnitude (approximately $25{\times}$ smaller interaction indices than Qwen2-architecture models). At $s{=}0.25$, the paired median difference $\Delta{=}0.38$ $[0.31,\; 0.40]$ ($p_{\text{Bonf}} < 10^{-37}$, $d_z{=}1.12$), indicating a large within-architecture effect despite the reduced absolute magnitude. The monotonic dose-response across $s{=}0.15$--$0.25$ parallels the Qwen2-family pattern, suggesting that phase-modulated severity generalizes across architecture families while quantitative characteristics remain architecture-specific. Random eviction conditions and $s{=}0.30$ are in progress; strategy${\times}$phase interaction analysis is deferred. Full per-sparsity breakdowns appear in Appendix~\ref{app:cross-arch}.
94	
95	\subsection{Scale Analysis: Qwen2.5-14B}
96	\label{sec:scale-14b}
97	
98	To assess whether phase-modulated severity persists at larger model scale within the same architecture family, we evaluate Qwen2.5-14B-Instruct on MATH-500 ($n{=}500$) at $s \in \{0.15, 0.20, 0.25, 0.30\}$.
99	
100	\begin{table}[t]
101	\centering
102	\small
103	\caption{Median of per-problem paired severity differences ($\Delta$) under importance-based eviction on Qwen2.5-14B-Instruct (MATH-500). \textit{Results pending.}}
104	\label{tab:scale-14b}
105	\begin{tabular}{@{}lcccc@{}}
106	\toprule
107	Strategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
108	\midrule
109	Importance & --- & --- & --- & --- \\
110	Random     & --- & --- & --- & --- \\
111	\bottomrule
112	\end{tabular}
113	\end{table}
114	
115	%% PLACEHOLDER: Fill Table~\ref{tab:scale-14b} when c12 experiment completes.
116	%% Expected analysis: (1) whether 14B amplifies or attenuates severity relative to 7B,
117	%% (2) whether strategy specificity ratio is scale-invariant,
118	%% (3) comparison of phase segmentation thresholds at larger scale.
119	
120	\subsection{Cross-Benchmark Validation: GSM8K}
121	\label{sec:cross-benchmark}
122	
123	To assess task generalization, we evaluate both models on GSM8K ($n{=}50$) at $s \in \{0.15, 0.20, 0.25, 0.30\}$. On DeepSeek (clean data, no output truncation), importance-based eviction replicates the MATH-500 phase gradient across all four sparsity levels with a strict dose-response: $\Delta{=}0.24$ at $s{=}0.15$ rising to $4.68$ at $s{=}0.30$ (all $p \leq 0.0003$, Wilcoxon). Strategy specificity on GSM8K manifests as a \emph{qualitative} gap: importance-based eviction produces significant phase gradients while random eviction is non-significant across all conditions (CIs spanning zero). We attribute this to \emph{task complexity}: GSM8K's simpler arithmetic is associated with more uniform attention distributions, yielding a flatter sparsity landscape; within MATH-500, longer traces exhibit higher strategy specificity (Spearman $\rho > 0$, $p < 0.02$), supporting cognitive load as the modulating variable. Qwen GSM8K results are inconclusive due to generation truncation (\texttt{max\_new\_tokens}${=}$2047): while directional consistency holds at $s \geq 0.25$ ($\Delta{=}1.14$--$4.62$; $p < 10^{-4}$), absolute values and phase assignments are unreliable because all outputs hit the token limit. Full tables in Appendix~\ref{app:gsm8k}.
124	
125	\paragraph{GSM8K accuracy under compound sparsity.}
126	A power analysis on GSM8K ($n{=}50$) reveals a strategy-dependent asymmetry in downstream accuracy. Under random head removal, all 8 conditions (2 models $\times$ 4 sparsity levels) are non-significant (max $|d|{=}0.164$). Post-hoc power analysis indicates $n{=}50$ can detect effects of $d \geq 0.40$ ($\alpha{=}0.05$, power${=}0.80$); all random conditions showed $|d| \leq 0.164$, meaning the null results may reflect insufficient power rather than true absence of effect. Under importance-based pruning, Qwen exhibits a medium-sized accuracy degradation at $s \geq 0.25$ ($d \approx 0.63$, power ${>}\,0.99$), consistent with the PPL-based severity gradient observed on MATH-500. DeepSeek importance conditions exhibit a qualitative downward trend in accuracy but are excluded from parametric inference due to heavy-tailed distributions that violate test assumptions.
127	
128	\subsection{Cross-Benchmark Validation: GPQA Diamond}
129	\label{sec:cross-benchmark-gpqa}
130	
131	To assess generalization beyond mathematical reasoning, we evaluate both models on GPQA Diamond~\cite{rein-gpqa-2024} ($n{=}198$), a graduate-level science QA benchmark requiring multi-step reasoning across physics, chemistry, and biology.
132	
133	\begin{table}[t]
134	\centering
135	\small
136	\caption{Median of per-problem paired severity differences ($\Delta$) under importance-based eviction on GPQA Diamond. \textit{Results pending.}}
137	\label{tab:gpqa-results}
138	\begin{tabular}{@{}lcccc@{}}
139	\toprule
140	Model & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
141	\midrule
142	DeepSeek-R1-Distill-Qwen-7B & --- & --- & --- & --- \\
143	Qwen2.5-7B-Instruct         & --- & --- & --- & --- \\
144	\bottomrule
145	\end{tabular}
146	\end{table}
147	
148	%% PLACEHOLDER: Fill Table~\ref{tab:gpqa-results} when c11 experiment completes.
149	%% Expected analysis: (1) phase gradient direction consistency with MATH-500/GSM8K,
150	%% (2) strategy specificity comparison across task types (math vs. science reasoning),
151	%% (3) whether cognitive load modulation hypothesis extends to non-mathematical domains.
152	
153	\subsection{Statistical Validation}
154	\label{sec:stat-validation}
155	
156	Table~\ref{tab:cohens-d} reports the paired median difference $\Delta$ under importance-based eviction for both models at $n{=}496$/$475$. All eight conditions yield CIs excluding zero; within-importance dose-response $d_z$ (s015 vs.\ s030) is $0.94$ (DeepSeek) and $0.92$ (Qwen), both large effects. Importance-based eviction produces significantly larger phase gradients than random at all four sparsity levels ($p_{\text{Bonf}} \ll 10^{-10}$, Wilcoxon; permutation tests in Appendix~\ref{app:permutation-details}).
157	
158	\begin{table}[t]
159	\centering
160	\small
161	\caption{Median of paired differences ($\Delta_i = \mathrm{II}^{(i)}_{\textit{low}} - \mathrm{II}^{(i)}_{\textit{high}}$) under importance-based eviction with bootstrap 95\% CIs ($B{=}10{,}000$).}
162	\label{tab:cohens-d}
163	\begin{tabular}{@{}lcc@{}}
164	\toprule
165	$s$ & DS ($n{=}496$): $\widetilde{\Delta}$\; [95\% CI] & QW ($n{=}475$): $\widetilde{\Delta}$\; [95\% CI] \\
166	\midrule
167	0.15 & $0.39$\; $[0.35,\; 0.44]$ & $0.07$\; $[0.05,\; 0.09]$ \\
168	0.20 & $1.21$\; $[1.11,\; 1.34]$ & $0.31$\; $[0.26,\; 0.36]$ \\
169	0.25 & $3.99$\; $[3.53,\; 4.36]$ & $1.07$\; $[0.98,\; 1.18]$ \\
170	0.30 & $8.48$\; $[7.75,\; 9.69]$ & $3.16$\; $[2.78,\; 3.56]$ \\
171	\bottomrule
172	\multicolumn{3}{@{}l}{\footnotesize All $p_{\text{Bonf}} < 10^{-13}$. Within-importance $d_z$ (s015 vs.\ s030): DS $0.94$, QW $0.92$.}
173	\end{tabular}
174	\end{table}
175	
176	\subsection{Answer-Region Analysis}
177	\label{sec:answer-region}
178	
179	Across both models, 93.2\% of answer tokens (\verb|\boxed{}| markers) fall within the high-sparsity phase, where compound interaction is minimal. This non-uniformity identifies \emph{where} severity concentrates: reasoning-trace tokens show $5.7$--$43.5{\times}$ PPL degradation vs.\ $1.3$--$5.3{\times}$ for answer tokens (Wilcoxon $p < 0.001$). However, reasoning-trace degradation may produce \emph{silent reasoning errors}---correct formatting with corrupted intermediate logic \cite{lanham-2023-faithfulness, turpin-2023-biased-cot}---a failure mode that PPL detects but answer-level accuracy may miss.
180	
181	\subsection{Downstream Accuracy Validation}
182	\label{sec:accuracy-validation}
183	
184	To validate that the PPL-based severity gradient translates to downstream task performance, we evaluate MATH-500 accuracy under compound sparsity (importance-based eviction, \texttt{max\_new\_tokens}${=}$8192; Table~\ref{tab:accuracy}). Qwen's minimal truncation ($\leq 4\%$) provides a clean PPL-accuracy bridge.
185	Qwen ($n{=}100$; truncation $\leq 4\%$) shows gradual decline from $46\%$ (dense) through $s{=}0.25$ ($\delta{=}-4$ to $-13$\,pp) with a sharp cliff at $s{=}0.30$ ($19\%$, $\delta{=}-27$\,pp). DeepSeek ($n{=}50$) degrades more steeply ($74\% \to 4\%$) with a dual-regime structure: at $s \leq 0.20$, degradation is primarily truncation-driven (non-truncated accuracy remains $68$--$71\%$ at $s{=}0.15$--$0.20$ vs.\ $88\%$ dense); at $s \geq 0.25$, both truncation and reasoning quality collapse simultaneously (Appendix~\ref{app:accuracy-details}).
186	The two models exhibit distinct failure modes reflecting training-paradigm dependence: DeepSeek failures are \emph{truncation-dominated} (truncation $16\% \to 76\%$), while Qwen failures are \emph{wrong-answer-dominated} (truncation $\leq 4\%$, reasoning quality degrades directly). Given minimal truncation, Qwen accuracy data provide a reliable PPL-accuracy bridge; DeepSeek accuracy results, confounded by truncation rates of $16\%$--$76\%$, should be interpreted as qualitative observations only.
187	
188	We provide a correlational mechanistic analysis in terms of importance discrimination collapse in \S\ref{sec:analysis}.
189	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "34506741-3fed-491a-9bb0-497a0d625c27",
  "isSidechain": true,
  "promptId": "9fc20291-e8f1-4e03-bc4b-c7922ed33096",
  "agentId": "a32bc4203578b639f",
  "type": "user",
  "uuid": "e8bb7df9-28d5-41c7-828d-b3e62b75c7a9",
  "sourceToolAssistantUUID": "34506741-3fed-491a-9bb0-497a0d625c27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T15:50:23.646Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LESRLqajFbKnC8SoCVKyLv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8bb7df9-28d5-41c7-828d-b3e62b75c7a9",
  "isSidechain": true,
  "agentId": "a32bc4203578b639f",
  "requestId": "req_011Cb6Wit8Jt2KLPHamAXiha",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "758bacd3-b275-4bdb-97c5-8bf0730fed1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VuciZaYcfhUYr6CjfwgiSy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9297,
      "cache_read_input_tokens": 26867,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9297,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
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

_source line 20 · 2026-05-16T15:50:23.652Z_

<details><summary>↩ Tool result · `toolu_01LESRLqajFbKnC8SoCVKyLv`</summary>

```text
1	\section{Importance Discrimination Collapse under Compound Sparsity}
2	\label{sec:analysis}
3	
4	The mechanisms discussed here are \emph{correlational diagnostics} that illuminate but do not fully explain the $15$--$17{\times}$ severity divergence between strategies. Both strategies exhibit near-identical Gini drops ($<10\%$ difference), yet severity diverges by $15$--$17{\times}$---an order-of-magnitude mismatch indicating that aggregate concentration collapse alone is insufficient. The critical differentiator is \emph{structural specificity} of importance-based pruning, which systematically removes high-attention-score heads (\S\ref{sec:discrimination-collapse-main}).
5	
6	\subsection{Importance Discrimination Collapse}
7	\label{sec:discrimination-collapse-main}
8	
9	Head pruning systematically reduces the discriminative power of cumulative importance scores, suggesting a mechanism for the phase-strategy interaction. The Gini coefficient decreases by $0.030$--$0.081$ (DeepSeek, $6$--$17\%$ relative to dense baseline) and $0.010$--$0.020$ (Qwen, $2$--$4\%$) after pruning, with consistent negative deltas in all 16 conditions (Appendix~\ref{app:analysis}, Table~\ref{tab:discrimination-metrics-full}). Random eviction shows near-identical Gini drops (e.g., DeepSeek $s{=}0.25$: $-0.065$ vs.\ $-0.060$), indicating that collapse is a consequence of head pruning \emph{per se}. Yet importance-based severity is $15$--$17{\times}$ larger---the amplification arises because importance-based eviction \emph{depends on} the very scores that pruning degrades.
10	
11	This pattern---\emph{importance discrimination collapse}---reflects eviction degenerating into noise-sensitive selection as score distributions approach uniformity. The effect is phase-dependent: per-phase Gini analysis on Qwen shows that the low-sparsity phase exhibits the largest Gini delta at every sparsity level, with monotonically increasing magnitude ($-0.017$ at $s{=}0.15$, $-0.020$ at $s{=}0.20$, $-0.029$ at $s{=}0.25$, $-0.035$ at $s{=}0.30$). Low-sparsity phases have broadly distributed attention where collapse has maximum impact; high-sparsity phases preserve concentration. \cite{hies-2025} report this collapse under single-axis pruning; we extend it to the compound setting.
12	
13	To provide quantitative evidence for structural specificity, we analyzed the attention Gini coefficients of importance-pruned versus retained heads. Importance pruning (Frobenius norm criterion) systematically removes heads with lower Gini coefficients---i.e., heads with more dispersed attention patterns (Mann-Whitney $U$, $p < 10^{-28}$; rank-biserial $r = 0.62$--$0.76$ across all 8 conditions). Random pruning, by contrast, samples heads with Gini indistinguishable from the population mean (200-trial verification). The Frobenius norm and Gini share sensitivity to attention magnitude; the large effect size ($r > 0.6$) nonetheless indicates strong structural separation.
14	
15	We note that this evidence is correlational; causal validation through controlled manipulation of importance-score entropy is an important direction for future work.
16	%% TODO: Add per-phase Gini results when available from Agent computation.
17	
18	\subsection{Entropy Redistribution: A Model-Dependent Secondary Effect}
19	\label{sec:entropy-redistribution-main}
20	
21	As a supplementary observation, head pruning also redistributes the attention entropy of surviving heads on DeepSeek ($\Delta\mathcal{H} \in [-0.047, -0.040]$; Appendix~\ref{app:analysis}, Table~\ref{tab:entropy-deltas}). However, entropy redistribution shows model-dependent behavior---the direction reverses on Qwen at $s{=}0.25$ ($\Delta\mathcal{H} = +0.045$)---replicating in only 2/4 Qwen conditions and thus only partially consistent. Importance discrimination collapse remains the more robust, model-independent correlate, though it partially accounts for rather than fully explains the severity divergence.
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "758bacd3-b275-4bdb-97c5-8bf0730fed1d",
  "isSidechain": true,
  "promptId": "9fc20291-e8f1-4e03-bc4b-c7922ed33096",
  "agentId": "a32bc4203578b639f",
  "type": "user",
  "uuid": "2fe1765c-2537-477c-82aa-56c4905a07a3",
  "sourceToolAssistantUUID": "758bacd3-b275-4bdb-97c5-8bf0730fed1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T15:50:24.195Z_

<details open><summary>🔧 Tool call — Read · `toolu_017Xpdycyg9kGwDxECj2kyjw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2fe1765c-2537-477c-82aa-56c4905a07a3",
  "isSidechain": true,
  "agentId": "a32bc4203578b639f",
  "requestId": "req_011Cb6Wit8Jt2KLPHamAXiha",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6f302fd0-0adf-46ba-82ab-27e68aef2c05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VuciZaYcfhUYr6CjfwgiSy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9297,
      "cache_read_input_tokens": 26867,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9297,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
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

_source line 22 · 2026-05-16T15:50:24.200Z_

<details><summary>↩ Tool result · `toolu_017Xpdycyg9kGwDxECj2kyjw`</summary>

```text
1	\begin{abstract}
2	Compound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.
3	We find that compound sparsity severity is not a fixed constant but an emergent property of the interaction among eviction strategy, reasoning phase, and sparsity level.
4	On DeepSeek-R1-Distill-Qwen-7B (MATH-500), importance-based eviction exhibits a monotonically increasing phase--severity gradient: the paired median difference $\Delta$ rises from $0.39$ at sparsity $s{=}0.15$ to $8.48$ at $s{=}0.30$ (Spearman $\rho{=}1.0$; all Bonferroni-corrected $p < 0.005$).
5	Random eviction develops a detectable gradient only above $s \approx 0.20$, at $2.7$--$17{\times}$ smaller magnitude.
6	The pattern replicates on Qwen2.5-7B-Instruct ($\Delta$: $0.07 \to 3.16$; $\rho{=}1.0$), shows consistent phase gradient direction on GSM8K for both models, and generalizes to LlamaForCausalLM ($n{=}250$; monotonic gradient confirmed, ${\sim}25{\times}$ smaller magnitude).
7	Per-phase Gini analysis identifies \emph{importance discrimination collapse}---the degeneration of head importance scores toward uniformity under compound stress---as a correlational diagnostic of this severity divergence.
8	These findings challenge the assumption of uniform compound interaction and establish phase-gated analysis---decomposing compound severity by reasoning phase and eviction strategy---as a principled framework for diagnosing where and why compound sparsity fails, with direct implications for phase-aware budget allocation in inference systems.
9	\end{abstract}
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f302fd0-0adf-46ba-82ab-27e68aef2c05",
  "isSidechain": true,
  "promptId": "9fc20291-e8f1-4e03-bc4b-c7922ed33096",
  "agentId": "a32bc4203578b639f",
  "type": "user",
  "uuid": "ef59e403-825b-42f2-b4f9-bfd0ad77fefe",
  "sourceToolAssistantUUID": "6f302fd0-0adf-46ba-82ab-27e68aef2c05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T15:50:24.496Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YLb82dRwLXZdTs1Dzzi9s4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef59e403-825b-42f2-b4f9-bfd0ad77fefe",
  "isSidechain": true,
  "agentId": "a32bc4203578b639f",
  "requestId": "req_011Cb6Wit8Jt2KLPHamAXiha",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a492876-f879-44aa-9e51-a01eefd6683b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VuciZaYcfhUYr6CjfwgiSy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9297,
      "cache_read_input_tokens": 26867,
      "output_tokens": 242,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9297
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 242,
          "cache_read_input_tokens": 26867,
          "cache_creation_input_tokens": 9297,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9297,
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

_source line 24 · 2026-05-16T15:50:24.506Z_

<details><summary>↩ Tool result · `toolu_01YLb82dRwLXZdTs1Dzzi9s4`</summary>

```text
1	\paragraph{Model scale and architecture.}
2	Our primary experiments span 7--14B parameters: DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct, and Qwen2.5-14B-Instruct (\S\ref{sec:scale-14b}). Whether the phase-modulated severity patterns persist, amplify, or attenuate at substantially larger scales (e.g., 70B) remains untested. Preliminary cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \S\ref{sec:cross-arch}, Appendix~\ref{app:cross-arch}) confirms that the monotonic phase gradient extends beyond the Qwen2 architecture ($n{=}250$, $d_z{=}1.12$ at $s{=}0.25$; all tested conditions $p_{\text{Bonf}} < 10^{-37}$) but with substantially reduced interaction magnitude (${\sim}25{\times}$ smaller than Qwen2-architecture models). The pattern has been tested on two architecture families (Qwen2ForCausalLM, LlamaForCausalLM) at two scale points (7B, 14B); comprehensive validation across more diverse architectures (e.g., Mistral, multi-latent attention) and larger scales is needed for full generalization claims.
3	
4	\paragraph{Task coverage.}
5	We evaluate on three benchmarks spanning mathematical and scientific reasoning: MATH-500 (primary), GSM8K (\S\ref{sec:cross-benchmark}), and GPQA Diamond (\S\ref{sec:cross-benchmark-gpqa}). Cross-benchmark validation on GSM8K supports the phase gradient direction under importance-based eviction but reveals that random eviction is non-significant (CIs spanning zero), precluding meaningful ratio computation. On MATH-500, strategy specificity is quantifiable ($15$--$17{\times}$); on GSM8K, it manifests as a qualitative gap (significant vs.\ non-significant). This suggests that the phase-strategy interaction is robust in direction but task-dependent in form---complex reasoning (MATH-500) produces quantitative strategy contrast while simpler arithmetic (GSM8K) produces qualitative separation. Qwen GSM8K outputs were truncated at \texttt{max\_new\_tokens}${=}$2047, so Qwen GSM8K absolute values carry this limitation; DeepSeek GSM8K data is untruncated. Our task-complexity explanation for specificity attenuation (lower cognitive load $\to$ more uniform attention $\to$ reduced strategy sensitivity) is supported by within-benchmark correlational evidence but requires validation across a broader range of task complexities; whether different reasoning tasks---code generation, multi-hop QA---produce yet different attenuation profiles remains open. Random eviction on GSM8K exhibits numerical instability (extreme outlier II values), likely a systematic interaction between reduced-precision arithmetic and score-independent eviction.
6	
7	\paragraph{Eviction strategy scope and H$_2$O confound.}
8	Our importance-based eviction uses cumulative attention scores (H$_2$O-style scoring~\cite{h2o-neurips2023}, Eq.~\ref{eq:kv-importance}), which creates an inherent confound: head pruning alters the attention distribution from which importance scores are computed, and eviction then operates on these degraded scores. The compound interaction patterns we report---including importance discrimination collapse and the phase-strategy crossover---may be partly attributable to this circular dependency rather than to compound sparsity \emph{per se}. Other attention-mass-based methods (SnapKV~\cite{snapkv-neurips2024}, PyramidKV~\cite{pyramidkv-colm2025}) share the same scoring basis and would likely exhibit a similar confound, whereas strategies that do not derive scores from the pruned attention distribution (e.g., learned eviction policies, recency-based heuristics) may exhibit qualitatively different compound interaction dynamics. Disentangling the contribution of score degradation from the intrinsic compound interaction requires testing eviction methods whose scoring is independent of head pruning; this is an important next step.
9	
10	\paragraph{Symmetric sparsity assumption.}
11	Our analysis applies symmetric sparsity levels: the same fraction $s$ is used for both head pruning and KV cache eviction. A preliminary spot check under asymmetric allocation (Appendix~\ref{app:asymmetric-robustness}) supports that the phase gradient is robust to head/KV budget ratios, but systematic characterization of the full asymmetric interaction surface remains future work.
12	
13	\paragraph{Phase segmentation validation.}
14	The \texttt{&lt;think>} token validation of sparsity-based phase segmentation (\S\ref{sec:background}, Appendix~\ref{app:think-validation}) is limited to a single model (DeepSeek-R1-Distill-Qwen-7B) on a single benchmark (GSM8K, $n{=}48$). Qwen2.5-7B-Instruct does not generate explicit reasoning markers, precluding the same validation. Whether the high agreement ($\kappa{=}0.88$) generalizes to other models with explicit CoT delimiters, or to non-mathematical reasoning tasks, remains open.
15	
16	\paragraph{Mechanism.}
17	The importance discrimination collapse mechanism is a correlational marker, not a complete causal explanation: both strategies exhibit near-identical Gini drops yet severity diverges by $15$--$17{\times}$, indicating that Gini collapse alone is insufficient. Causal validation through controlled entropy manipulation is needed. The entropy redistribution component replicates on only 2/4 Qwen conditions, suggesting model-specific factors.
18	
19	\paragraph{Perplexity vs.\ accuracy.}
20	Our primary severity metric is perplexity-based (II), chosen because its per-token granularity enables the phase-level decomposition central to our analysis; accuracy is binary per-problem and cannot be meaningfully decomposed by reasoning phase. Accuracy validation on MATH-500 (\S\ref{sec:accuracy-validation}, Appendix~\ref{app:accuracy-details}) shows gradual decline through $s{=}0.25$ ($\delta{=}-4$ to $-13$\,pp) followed by a sharp cliff at $s{=}0.30$ ($\delta{=}-27$\,pp) for Qwen ($n{=}100$, truncation $\leq 4\%$). DeepSeek accuracy deltas are confounded by rising truncation ($16\%$ to $76\%$); non-truncated analysis reveals a dual-regime structure but is limited by small surviving samples at high sparsity. Comprehensive accuracy evaluation across benchmarks remains an important next step.
21	
22	\paragraph{Sparsity range.}
23	Our experiments span $s \in \{0.15, 0.20, 0.25, 0.30\}$, sufficient to establish monotonicity at the tested levels (JT test $p \ll 10^{-10}$) but insufficient to characterize the functional form of the auxiliary ratio $G(s)$ or identify potential saturation thresholds. More extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics. We do not report inference throughput or latency measurements, which are necessary for a complete deployment analysis but orthogonal to our severity characterization. Extended limitations in Appendix~\ref{app:limitations}.
24	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0a492876-f879-44aa-9e51-a01eefd6683b",
  "isSidechain": true,
  "promptId": "9fc20291-e8f1-4e03-bc4b-c7922ed33096",
  "agentId": "a32bc4203578b639f",
  "type": "user",
  "uuid": "e87fafcf-5ae5-419a-af0d-be4ff3e6bb6c",
  "sourceToolAssistantUUID": "0a492876-f879-44aa-9e51-a01eefd6683b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T15:50:27.719Z_

<details open><summary>🔧 Tool call — Read · `toolu_01348mccjm9qAdvMkNMoSCEC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e87fafcf-5ae5-419a-af0d-be4ff3e6bb6c",
  "isSidechain": true,
  "agentId": "a32bc4203578b639f",
  "requestId": "req_011Cb6WjJ7CvCNsAyVv9dooR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fa3db684-cb1b-48cb-b0b5-b44b206b101b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MWw7V1ACvrSYUnYnoLztcK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3839,
      "cache_read_input_tokens": 36164,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3839,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 68,
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

_source line 26 · 2026-05-16T15:50:27.724Z_

<details><summary>↩ Tool result · `toolu_01348mccjm9qAdvMkNMoSCEC`</summary>

```text
1	% Section 3: Background and Problem Setup
2	% Note: eq:ii and eq:gradient are the canonical definitions.
3	% Full formulation details in Appendix (app:formulation-details).
4	
5	\section{Background and Problem Setup}
6	\label{sec:background}
7	
8	We formalize compound sparsity, define the Interaction Index, and introduce phase segmentation. Full mathematical details appear in Appendix~\ref{app:formulation-details}.
9	
10	\paragraph{Compound sparsity.}
11	Let $s \in (0,1)$ denote a unified sparsity budget. \emph{Attention head pruning} removes the bottom-$s$ fraction of heads per layer by Frobenius norm importance \cite{voita-acl2019, michel-neurips2019}. \emph{KV cache eviction} removes the bottom-$s$ fraction of token positions from the cache. We compare two strategies: \emph{importance-based}, which scores positions by position-normalized cumulative attention mass (Eq.~\ref{eq:kv-importance} in Appendix~\ref{app:formulation-details}), and \emph{random}, which evicts uniformly at random \cite{nacl-acl2024}. Applying both simultaneously yields \emph{compound sparsity}; the two axes interact because head pruning alters the importance ranking used for eviction \cite{spark-aaai2026}. Existing joint-pruning approaches such as GRASPrune \cite{graspune-acl2026} learn global budget-constrained gates but treat decisions as static across generation.
12	
13	\paragraph{Interaction Index.}
14	For a text segment, let $\text{PPL}_c$ denote perplexity under condition $c \in \{d, a, k, b\}$ (dense, attention-only, KV-only, compound). Normalizing by the dense baseline yields $r_c = \text{PPL}_c / \text{PPL}_d$, and:
15	\begin{equation}
16	    \mathrm{II} = r_b - r_a - r_k + 1.
17	    \label{eq:ii}
18	\end{equation}
19	$\mathrm{II} > 0$ indicates super-additive degradation; $\mathrm{II} = 0$ indicates additive independence. We adopt the additive null as primary: it assumes $r_b = r_a + r_k - 1$ (compound loss equals sum of individual losses), the most conservative independence assumption. Although the two axes are mechanistically linked (\S\ref{sec:analysis}), rejection ($\mathrm{II} > 0$) establishes super-additivity regardless of null specification. Appendix~\ref{app:multiplicative-null} reports parallel results under the multiplicative null ($r_b = r_a \cdot r_k$); the phase-severity gradient is preserved ($G_{\times}{=}21$--$64{\times}$), supporting null-choice invariance. The II distribution is heavily right-skewed; we report medians throughout.
20	
21	\paragraph{Severity gradient.}
22	To capture phase variation, the per-problem \emph{amplification ratio} is:
23	\begin{equation}
24	    G^{(i)} = \frac{\mathrm{II}^{(i)}_{\,\textit{low}}}{\mathrm{II}^{(i)}_{\,\textit{high}}},
25	    \label{eq:gradient}
26	\end{equation}
27	where $\mathrm{II}^{(i)}_{\,\textit{low/high}}$ is the interaction index in the low/high-sparsity phase for problem $i$. We report $G = \widetilde{G^{(i)}}$, the median across problems, with bootstrap CIs. We use the median of per-problem ratios (not the ratio of medians) to preserve per-problem pairing; see Appendix~\ref{app:profiling-subset} for comparison. $G$ serves as an auxiliary descriptive ratio that illustrates the degree of phase concentration; the primary statistical evidence for the severity gradient rests on $\Delta$ and paired Wilcoxon tests (\S\ref{sec:phase-amplification}).
28	
29	\paragraph{Phase segmentation.}
30	\label{par:phase-segmentation}
31	Inspired by ThinKV's phase-aware perspective on reasoning-time compression~\cite{thinkv-iclr2026}, each generated sequence is partitioned into three phases (low-, mid-, high-sparsity) by tercile boundaries of per-position attention sparsity, using a quantile-based segmentation rather than explicit reasoning delimiters (e.g., \texttt{&lt;think>} tokens). Low-sparsity phases correspond to broadly distributed attention (exploratory reasoning); high-sparsity phases to concentrated attention (structured computation). We note that this segmentation is an \emph{operationalization choice}: attention sparsity serves as a continuous proxy for reasoning phase rather than a theoretically grounded boundary. We validate robustness to segmentation granularity (tercile/quartile/quintile; Appendix~\ref{app:seg-robust}) and minimum phase length (Appendix~\ref{app:mpl-sensitivity}). Validation against DeepSeek's explicit \texttt{&lt;think>} markers using adaptive per-sequence quantile segmentation yields substantial agreement ($\kappa{=}0.88$, AUC-ROC${=}0.98$; $n{=}48$; Appendix~\ref{app:think-validation}). Details in Appendix~\ref{app:formulation-details}.
32	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa3db684-cb1b-48cb-b0b5-b44b206b101b",
  "isSidechain": true,
  "promptId": "9fc20291-e8f1-4e03-bc4b-c7922ed33096",
  "agentId": "a32bc4203578b639f",
  "type": "user",
  "uuid": "d84b4803-0822-4de8-9828-4ef984be08ce",
  "sourceToolAssistantUUID": "fa3db684-cb1b-48cb-b0b5-b44b206b101b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T15:50:28.213Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CQxjhpTYS1pFLpCK75M6JZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d84b4803-0822-4de8-9828-4ef984be08ce",
  "isSidechain": true,
  "agentId": "a32bc4203578b639f",
  "requestId": "req_011Cb6WjJ7CvCNsAyVv9dooR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fc17ef5f-cb40-403a-a136-e9a247100465",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MWw7V1ACvrSYUnYnoLztcK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3839,
      "cache_read_input_tokens": 36164,
      "output_tokens": 185,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3839
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 185,
          "cache_read_input_tokens": 36164,
          "cache_creation_input_tokens": 3839,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3839,
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

_source line 28 · 2026-05-16T15:50:28.230Z_

<details><summary>↩ Tool result · `toolu_01CQxjhpTYS1pFLpCK75M6JZ`</summary>

```text
1	\section{Compound Sparsity Formulation}
2	\label{app:formulation-details}
3	
4	\paragraph{Attention head pruning.}
5	Heads are ranked by Frobenius norm importance $w_j^{(\ell)} = \|\mathbf{A}_j^{(\ell)}\|_F$ \cite{voita-acl2019, michel-neurips2019}; a binary mask $m_j^{(\ell)} \in \{0,1\}$ retains the top-$(1{-}s)\cdot H$ heads:
6	\begin{equation}
7	    \tilde{\mathbf{o}}_j^{(\ell)} = m_j^{(\ell)} \cdot \mathbf{o}_j^{(\ell)}.
8	    \label{eq:head-mask}
9	\end{equation}
10	
11	\paragraph{KV cache eviction.}
12	A position mask $\mathbf{m}_k \in \{0,1\}^T$ retains the top-$(1{-}s)\cdot T$ positions (BOS always preserved):
13	\begin{equation}
14	    \tilde{a}_{ij} = a_{ij} \cdot m_{k,j}, \quad \forall\, i, j.
15	    \label{eq:kv-mask}
16	\end{equation}
17	Under importance-based eviction, each position $j$ is scored by its cumulative attention mass with position normalization:
18	\begin{equation}
19	    \mathrm{imp}(j) = \frac{\sum_{\ell, h, i} a_{ij}^{(\ell,h)}}{T - j},
20	    \label{eq:kv-importance}
21	\end{equation}
22	where the denominator compensates for causal bias---earlier positions are attended to by more queries \cite{thinkv-iclr2026, defensivekv-iclr2026}. Under random eviction, positions (excluding BOS) are evicted uniformly at random.
23	
24	\paragraph{Compound sparsity.}
25	Applying both mechanisms simultaneously yields compound sparsity. The two axes interact: head pruning redistributes attention mass, altering the importance ranking for KV eviction. Prior work \cite{spark-aaai2026} reports super-additive joint effects but treats interaction magnitude as a fixed property of $s$.
26	
27	\paragraph{Attention sparsity metric.}
28	For each query position $i$ and head $h$, we compute the fraction of key positions receiving negligible attention:
29	\begin{equation}
30	    \sigma_i^{(h)} = \frac{1}{T} \sum_{j=1}^{T} \mathbf{1}\!\left[a_{ij}^{(h)} < 0.01 \cdot \max_k a_{ik}^{(h)}\right].
31	    \label{eq:attn-sparsity}
32	\end{equation}
33	The per-position sparsity $\sigma_i = \frac{1}{H}\sum_h \sigma_i^{(h)}$ averages across all heads. Tokens are partitioned into high-, mid-, and low-sparsity phases by the tercile boundaries of $\{\sigma_i\}$; segments shorter than 10 tokens are merged into adjacent phases.
34	
35	\section{Multiplicative Null Verification}
36	\label{app:multiplicative-null}
37	
38	We verified that replacing the additive null $r_b = r_a + r_k - 1$ (Eq.~\ref{eq:ii}) with the multiplicative null $r_b = r_a \cdot r_k$ does not change qualitative conclusions. Under the multiplicative formulation, the interaction index becomes $\mathrm{II}_{\times} = r_b - r_a \cdot r_k$. Notably, $\mathrm{II}_{\times} < 0$ across all phases and sparsity levels: the compound interaction is \emph{sub-multiplicative} everywhere---actual compound degradation is less severe than the multiplicative prediction. $G_{\times}$ therefore quantifies the ratio of sub-multiplicative deviations between phases, not super-multiplicative amplification: a value of $G_{\times}{=}30$ means the low-sparsity phase deviates from the multiplicative null by $30{\times}$ more than the high-sparsity phase. Under importance-based eviction, $G_{\times}{=}21.1$--$36.2{\times}$ (DeepSeek) and $43.9$--$64.0{\times}$ (Qwen) across $s \in \{0.15, 0.20, 0.25, 0.30\}$, yielding a combined range of $21$--$64{\times}$. Although compound effects do not exceed the multiplicative prediction in any phase, the low-sparsity phase's deviation from the multiplicative null is $21$--$64{\times}$ larger than the high-sparsity phase's, indicating that the phase-gated severity gradient is preserved under the multiplicative null. These $n{=}500$ exact values are more conservative than the preliminary $n{=}50$ calibrated estimates ($\approx$51--183${\times}$), reflecting reduced variance at full sample size. Values are computed using aggregate per-phase PPL ratios; per-problem exact computation is left for future work. Random eviction remains flat ($G_{\times} \approx 1$). The crossover at $s{=}0.25$ is preserved. We adopt the additive formulation in the main text as the more conservative baseline: it assumes zero interaction (compound loss equals the sum of individual losses), so rejection ($\mathrm{II} > 0$) establishes super-additivity regardless of null specification. The qualitative conclusions---phase-modulated severity, strategy asymmetry, and crossover---are preserved under the multiplicative null.
39	
40	% Bootstrap and permutation details moved to main text \S\ref{sec:stat-validation}
41	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fc17ef5f-cb40-403a-a136-e9a247100465",
  "isSidechain": true,
  "promptId": "9fc20291-e8f1-4e03-bc4b-c7922ed33096",
  "agentId": "a32bc4203578b639f",
  "type": "user",
  "uuid": "0a4fb65e-89f7-4d6b-b7f6-5bbb347e923e",
  "sourceToolAssistantUUID": "fc17ef5f-cb40-403a-a136-e9a247100465",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T15:50:31.236Z_

<details open><summary>🔧 Tool call — Read · `toolu_019LcHyJc2MKtVi3zxjwRHDp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex",
  "offset": 41
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a4fb65e-89f7-4d6b-b7f6-5bbb347e923e",
  "isSidechain": true,
  "agentId": "a32bc4203578b639f",
  "requestId": "req_011Cb6Wja3uG7PWLwBzyttCH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "520840b7-0489-4cc5-9bc8-da3eb4e3666e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PsnkmRzPXnTS8FsYtR7MbY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3172,
      "cache_read_input_tokens": 40003,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3172,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 69,
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

_source line 30 · 2026-05-16T15:50:31.254Z_

<details><summary>↩ Tool result · `toolu_019LcHyJc2MKtVi3zxjwRHDp`</summary>

```text
&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (41). The file has 41 lines.&lt;/system-reminder>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "520840b7-0489-4cc5-9bc8-da3eb4e3666e",
  "isSidechain": true,
  "promptId": "9fc20291-e8f1-4e03-bc4b-c7922ed33096",
  "agentId": "a32bc4203578b639f",
  "type": "user",
  "uuid": "a1403786-8b4d-43d5-b298-9f348deed1ca",
  "sourceToolAssistantUUID": "520840b7-0489-4cc5-9bc8-da3eb4e3666e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T15:50:31.814Z_

<details open><summary>🔧 Tool call — Read · `toolu_016cqXmodPZ4r2eTxJRgmkYb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1403786-8b4d-43d5-b298-9f348deed1ca",
  "isSidechain": true,
  "agentId": "a32bc4203578b639f",
  "requestId": "req_011Cb6Wja3uG7PWLwBzyttCH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "98b8e0b5-0cfc-4189-9906-d3e9aaeb1f21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PsnkmRzPXnTS8FsYtR7MbY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3172,
      "cache_read_input_tokens": 40003,
      "output_tokens": 188,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3172
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 188,
          "cache_read_input_tokens": 40003,
          "cache_creation_input_tokens": 3172,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3172,
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

_source line 32 · 2026-05-16T15:50:31.829Z_

<details><summary>↩ Tool result · `toolu_016cqXmodPZ4r2eTxJRgmkYb`</summary>

```text
1	
2	\section{Phase-Strategy Crossover Details}
3	\label{app:crossover-details}
4	
5	On DeepSeek ($n{=}496$), a strategy ranking reversal emerges at $s{=}0.25$ (Figure~\ref{fig:crossover}): importance-based eviction yields \emph{lower} II than random in the high-sparsity phase ($0.021$ vs.\ $1.113$) but \emph{higher} II in the low-sparsity phase ($3.971$ vs.\ $1.514$---a $2.6{\times}$ reversal; both $p < 10^{-4}$). This crossover is observed at all four sparsity levels, with reversal magnitude of $4.0{\times}$ at $s{=}0.15$, $3.4{\times}$ at $s{=}0.20$, $2.6{\times}$ at $s{=}0.25$, and $2.2{\times}$ at $s{=}0.30$ (decreasing as random eviction severity rises). The reversal arises because head pruning redistributes attention mass, altering importance rankings in a way that couples the two sparsity mechanisms in low-sparsity phases (\S\ref{sec:discrimination-collapse-main}). Qwen does not exhibit a crossover: importance-based eviction produces lower II than random in both phases across all sparsity levels (e.g., at $s{=}0.25$: high $0.004$ vs.\ $1.108$; low $1.053$ vs.\ $1.769$).
6	
7	\begin{figure}[t]
8	\centering
9	\includegraphics[width=\columnwidth]{fig3_crossover.pdf}
10	\caption{Strategy-dependent crossover at $s{=}0.25$ on DeepSeek ($n{=}496$). Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces $2.6{\times}$ higher II in the low-sparsity phase, reversing the strategy ranking.}
11	\label{fig:crossover}
12	\end{figure}
13	
14	
15	\section{Profiling Subset Per-Phase Breakdown}
16	\label{app:profiling-subset}
17	
18	\begin{table*}[t]
19	\centering
20	\small
21	\caption{Per-phase interaction index (II) from the $n{=}50$ profiling subset (DeepSeek-R1-Distill-Qwen-7B). This preliminary table does not include per-condition bootstrap CIs; full-scale values with bootstrap 95\% CIs ($B{=}10{,}000$) at $n{=}496$ appear in Table~\ref{tab:main-results}, and strategy-contrast CIs for this subset appear in the permutation test (Table~\ref{tab:permutation}). $G$ values use the ratio-of-medians definition ($\widetilde{\mathrm{II}}_{\textit{low}} / \widetilde{\mathrm{II}}_{\textit{high}}$) and serve as an auxiliary illustration of phase concentration; the primary evidence is $\Delta$ (see Appendix~\ref{app:g-metric}). At low sparsity ($s{=}0.15$), the ratio-of-medians and per-problem definitions diverge ($7.5{\times}$ vs.\ $69{\times}$) because per-problem ratios are sensitive to near-zero $\mathrm{II}_{\textit{high}}$ values.}
22	\label{tab:profiling-subset}
23	\begin{tabular}{@{}llccccr@{}}
24	\toprule
25	$s$ & Strategy & $\widetilde{\mathrm{II}}_{\textit{high}}$ & $\widetilde{\mathrm{II}}_{\textit{mid}}$ & $\widetilde{\mathrm{II}}_{\textit{low}}$ & $\Delta$ & $G$ \\
26	\midrule
27	0.15 & Importance & 0.006 & 0.081 & 0.398 & 0.39 & $\mathbf{69}$ \\
28	0.15 & Random     & 0.093 & 0.097 & 0.103 & 0.01 & 1.1 \\
29	\addlinespace
30	0.20 & Importance & 0.015 & 0.203 & 1.496 & 1.48 & $\mathbf{103}$ \\
31	0.20 & Random     & 0.292 & 0.350 & 0.276 & $-$0.02 & 0.9 \\
32	\addlinespace
33	0.25 & Importance & 0.032 & 1.118 & 7.196 & 7.16 & $\mathbf{222}$ \\
34	0.25 & Random     & 0.818 & 0.932 & 1.363 & 0.54 & 1.7 \\
35	\addlinespace
36	0.30 & Importance & 0.053 & 2.283 & 14.639 & 14.59 & $\mathbf{274}$ \\
37	0.30 & Random     & 2.503 & 2.592 & 4.041 & 1.54 & 1.6 \\
38	\bottomrule
39	\end{tabular}
40	\end{table*}
41	
42	The $n{=}50$ profiling subset served as a preliminary calibration; all importance-based $\Delta$ values were subsequently replicated at $n{=}496$ with bootstrap 95\% CIs excluding zero (Table~\ref{tab:main-results}: $\Delta{=}0.39$\;$[0.35,\;0.44]$ to $8.48$\;$[7.75,\;9.69]$). The paired permutation test on this subset ($n{=}49$; Table~\ref{tab:permutation}) provides bootstrap 95\% CIs for the strategy contrast ($\widetilde{\Delta}_{\text{imp}} - \widetilde{\Delta}_{\text{rand}}$), all excluding zero after Bonferroni correction.
43	
44	
45	\section{Cross-Training-Paradigm Replication Details}
46	\label{app:cross-model-details}
47	
48	Both models share the Qwen2ForCausalLM backbone (28 layers, 28 heads, 4-group GQA) but differ in training: DeepSeek uses reasoning distillation from DeepSeek-R1, while Qwen2.5 uses standard instruction tuning without explicit reasoning delimiters. This within-architecture-family comparison enables assessment of training methodology effects on the compound sparsity interaction, though causal attribution is limited by the observational design.
49	
50	Despite lacking explicit \texttt{&lt;think>} delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity to permit phase segmentation via the same quantile-based method (\S\ref{par:phase-segmentation}). Twenty-five of the 500 problems are excluded due to degenerate phase assignments, yielding $n{=}475$ valid problems for Qwen (vs.\ $n{=}496$ for DeepSeek).
51	
52	\paragraph{Per-phase effective sample size.}
53	\label{app:qwen-null-rate}
54	Table~\ref{tab:qwen-effective-n} reports the per-phase effective sample size for Qwen2.5-7B-Instruct, defined as the number of problems with non-null phase segments (segment length $\geq$ \texttt{min\_phase\_length}). The mid-phase null rate (45.2\%) reflects problems where mid-sparsity tokens do not form contiguous runs above the merging threshold; this does not affect the low--high contrast ($\Delta$) used in the primary analysis.
55	
56	\begin{table}[t]
57	\centering
58	\small
59	\caption{Per-phase effective sample size for Qwen2.5-7B-Instruct ($n_{\text{eff}} = 475$). Phase segmentation is performed once on dense-model attention patterns and is independent of sparsity level.}
60	\label{tab:qwen-effective-n}
61	\begin{tabular}{@{}lcccc@{}}
62	\toprule
63	Phase & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
64	\midrule
65	High & 475 & 475 & 475 & 475 \\
66	Mid  & 274 & 274 & 274 & 274 \\
67	Low  & 475 & 475 & 475 & 475 \\
68	\bottomrule
69	\end{tabular}
70	\end{table}
71	
72	Table~\ref{tab:cross-model} reports the cross-training-paradigm comparison. Qwen reproduces the monotonic severity gradient at ${\sim}1/5$ of DeepSeek's magnitude. Figure~\ref{fig:cross-model} visualizes this comparison.
73	
74	\begin{table}[t]
75	\centering
76	\small
77	\caption{Cross-training-paradigm comparison of median compound severity difference ($\Delta$) under importance-based eviction.}
78	\label{tab:cross-model}
79	\begin{tabular}{@{}lcccc@{}}
80	\toprule
81	Model & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
82	\midrule
83	DeepSeek-R1-Distill-Qwen-7B ($n{=}496$) & 0.39 & 1.21 & 3.99 & 8.48 \\
84	Qwen2.5-7B-Instruct ($n{=}475$)         & 0.07 & 0.31 & 1.07 & 3.16 \\
85	\bottomrule
86	\end{tabular}
87	\end{table}
88	
89	\begin{figure}[t]
90	\centering
91	\includegraphics[width=\columnwidth]{fig5_crossmodel.pdf}
92	\caption{Cross-training-paradigm comparison of the median severity difference under importance-based eviction ($n{=}496$/$475$). Both DeepSeek (solid) and Qwen (dashed) exhibit monotonically increasing $\Delta$ with sparsity; Qwen's magnitude is approximately one-quarter to one-sixth of DeepSeek's.}
93	\label{fig:cross-model}
94	\end{figure}
95	
96	\paragraph{Per-problem concordance.}
97	The per-problem concordance across models is not significant (mean $\rho = -0.107$, $p = 0.926$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking.
98	
99	\paragraph{Random eviction control.}
100	As a control, random eviction on Qwen mirrors DeepSeek: non-significant at $s \leq 0.20$ ($\Delta$: $-0.01$, $0.02$; CIs span zero) but significant at $s \geq 0.25$ ($\Delta{=}0.39$, $p_{\text{Bonf}} < 10^{-10}$; $\Delta{=}0.91$, $p_{\text{Bonf}} < 10^{-13}$). Where significant, the random phase gradient is $2.7$--$3.5{\times}$ weaker than importance-based ($0.39$ vs.\ $1.07$ at $s{=}0.25$; $0.91$ vs.\ $3.16$ at $s{=}0.30$), supporting strategy-specific amplification.
101	
102	
103	\section{Permutation Test Details}
104	\label{app:permutation-details}
105	
106	For each problem $i$ and sparsity level $s$, we compute the compound severity difference $\Delta_i^{(\text{strat})} = \mathrm{II}_{\textit{low},i} - \mathrm{II}_{\textit{high},i}$ under each eviction strategy. The test statistic is the median of the paired difference $\widetilde{\Delta} = \text{median}_i\!\bigl(\Delta_i^{(\text{imp})} - \Delta_i^{(\text{rand})}\bigr)$, measuring whether importance-based eviction produces systematically larger phase-dependent severity than random eviction. We permute strategy labels $10{,}000$ times to construct the null distribution and apply Bonferroni correction for 4 sparsity-level comparisons.
107	
108	Per-problem distributions of the paired severity difference $\Delta_i = \mathrm{II}_{\textit{low},i} - \mathrm{II}_{\textit{high},i}$ under importance-based eviction are right-skewed at all sparsity levels, with mean/median ratios ranging from $1.2{\times}$ ($s{=}0.15$) to $1.6{\times}$ ($s{=}0.30$) for DeepSeek and $1.1{\times}$ to $1.4{\times}$ for Qwen.
109	
110	The permutation null distributions are approximately symmetric around zero at all sparsity levels. At $s{=}0.15$, the observed statistic falls at the $99.92$th percentile of the null ($p_{\text{Bonf}} = 0.0032$); at $s \geq 0.20$, no permutation exceeds the observed statistic.
111	
112	Table~\ref{tab:permutation} reports the results. All four sparsity levels reject $H_0$ after Bonferroni correction ($p_{\text{Bonf}} < 0.005$), with observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$. The monotonic growth of both the point estimate and the CI lower bound ($0.19 \to 0.69 \to 1.66 \to 6.70$) supports that compound severity amplification strengthens with sparsity---not merely in central tendency but also in worst-case lower bounds. Figure~\ref{fig:permtest-forest} presents these results as a forest plot.
113	
114	\begin{table}[t]
115	\centering
116	\small
117	\caption{Paired permutation test for compound severity: importance vs.\ random eviction on DeepSeek-R1-Distill-Qwen-7B ($n{=}49$ profiling subset, $10{,}000$ permutations, Bonferroni-corrected). The monotonic $\Delta$ pattern is supported at $n{=}496$ (Table~\ref{tab:aggregate-ii}).}
118	\label{tab:permutation}
119	\begin{tabular}{@{}rrcl@{}}
120	\toprule
121	$s$ & Observed $\widetilde{\Delta}$ & 95\% CI & $p_{\text{Bonf}}$ \\
122	\midrule
123	0.15 & 0.37 & $[0.19,\; 0.62]$ & 0.0032 \\
124	0.20 & 0.97 & $[0.69,\; 1.49]$ & ${<}\,0.001$ \\
125	0.25 & 3.34 & $[1.66,\; 6.64]$ & ${<}\,0.001$ \\
126	0.30 & 9.85 & $[6.70,\; 16.29]$ & ${<}\,0.001$ \\
127	\bottomrule
128	\end{tabular}
129	\end{table}
130	
131	\begin{figure}[t]
132	\centering
133	\includegraphics[width=\columnwidth]{fig4_bootstrap.pdf}
134	\caption{Forest plot of permutation test results. Horizontal bars show 95\% permutation CIs; diamonds mark observed median differences $\widetilde{\Delta}$. All CIs lie entirely above zero, supporting significant strategy-dependent severity at every sparsity level.}
135	\label{fig:permtest-forest}
136	\end{figure}
137	
138	
139	\section{Cross-Architecture Analysis}
140	\label{app:cross-arch}
141	
142	To test whether the phase-modulated severity pattern extends beyond the Qwen2 architecture, we replicate the experiment on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, 8B parameters; $n{=}250$, MATH-500) under importance-based eviction at $s \in \{0.15, 0.20, 0.25\}$. Table~\ref{tab:llama-cross-arch} reports per-phase interaction indices and the paired median difference $\Delta$.
143	
144	The monotonic phase gradient is confirmed across all three tested sparsity levels, with non-overlapping bootstrap CIs and all Bonferroni-corrected $p < 10^{-37}$. At $s{=}0.25$, $\Delta{=}0.38$ $[0.31,\; 0.40]$ with $d_z{=}1.12$, indicating a large within-architecture effect. The absolute magnitude is architecture-dependent: LLaMA interaction indices are approximately $25{\times}$ smaller than those on Qwen2-architecture models (DeepSeek, Qwen), suggesting that vulnerability to phase-modulated compound severity is substantially architecture-specific while the qualitative pattern---monotonic severity concentration in low-sparsity reasoning phases---generalizes.
145	
146	\begin{table}[t]
147	\centering
148	\small
149	\caption{Cross-architecture validation: per-phase II under importance-based eviction on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, $n{=}250$). $\Delta$: median of per-problem paired differences ($\mathrm{II}_{\textit{low}} - \mathrm{II}_{\textit{high}}$) with bootstrap 95\% CI ($B{=}1{,}000$).}
150	\label{tab:llama-cross-arch}
151	\begin{tabular}{@{}lccccc@{}}
152	\toprule
153	$s$ & $\widetilde{\mathrm{II}}_{\textit{high}}$ & $\widetilde{\mathrm{II}}_{\textit{low}}$ & $\Delta$\; [95\% CI] & $p_{\text{Bonf}}$ & $d_z$ \\
154	\midrule
155	0.25 & $0.017$ & $0.388$ & $0.38$\; $[0.31,\; 0.40]$ & $< 10^{-37}$ & $1.12$ \\
156	\bottomrule
157	\multicolumn{6}{@{}l}{\footnotesize $s{=}0.15$ and $s{=}0.20$ results confirm monotonic gradient; full table upon completion of all conditions.}
158	\end{tabular}
159	\end{table}
160	
161	\paragraph{Scope and pending conditions.}
162	Random eviction conditions and $s{=}0.30$ are in progress. Strategy${\times}$phase interaction analysis---which requires both importance and random data at matched sparsity levels---is deferred until all conditions complete. The within-importance results reported here are sufficient to confirm that the phase gradient generalizes to LlamaForCausalLM; whether the strategy specificity ($15$--$17{\times}$ on DeepSeek, $2.7$--$3.5{\times}$ on Qwen) also extends to this architecture remains an open question.
163	
164	
165	\section{Analysis: Importance Discrimination Collapse}
166	\label{app:analysis}
167	
168	\subsection{Importance Discrimination Collapse}
169	\label{sec:discrimination-collapse}
170	
171	Head pruning reduces the number of heads contributing to cumulative importance scores, collapsing the score distribution. Table~\ref{tab:discrimination-metrics-full} quantifies this effect: the Gini coefficient decreases by $0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen) after pruning, with consistent negative deltas across all 16 conditions (both models $\times$ 4 sparsity levels $\times$ 2 strategies). The CV delta is likewise negative in all 8 importance-based conditions. The same pattern holds under random eviction, indicating that importance discrimination collapse is a consequence of head pruning \emph{per se}, not of the eviction strategy.
172	
173	\begin{table}[t]
174	\centering
175	\caption{Importance discrimination collapse under importance-based eviction. $\Delta\mathrm{Gini}$ and $\Delta\mathrm{CV}$ are post-pruning minus baseline; negative values indicate reduced discriminative power.}
176	\label{tab:discrimination-metrics-full}
177	\small
178	\begin{tabular}{llrr}
179	\toprule
180	Model & $s$ & $\Delta\mathrm{Gini}$ & $\Delta\mathrm{CV}$ \\
181	\midrule
182	DeepSeek & $0.15$ & $-0.030$ & $-0.56$ \\
183	DeepSeek & $0.20$ & $-0.040$ & $-0.77$ \\
184	DeepSeek & $0.25$ & $-0.065$ & $-1.29$ \\
185	DeepSeek & $0.30$ & $-0.081$ & $-1.66$ \\
186	\midrule
187	Qwen & $0.15$ & $-0.010$ & $-0.05$ \\
188	Qwen & $0.20$ & $-0.012$ & $-0.21$ \\
189	Qwen & $0.25$ & $-0.010$ & $-1.49$ \\
190	Qwen & $0.30$ & $-0.020$ & $-1.14$ \\
191	\bottomrule
192	\end{tabular}
193	\end{table}
194	
195	When importance scores lose discriminability, thresholding degenerates into noise-sensitive selection---functionally approaching biased random eviction. This is phase-dependent: in low-sparsity phases, attention is already broadly distributed, so pruning-induced collapse has maximum impact; in high-sparsity phases, concentration is preserved. Random eviction is immune because its decisions are independent of score quality, consistent with $G \approx 1$.
196	
197	\subsection{Entropy Redistribution}
198	\label{sec:entropy-redistribution}
199	
200	Beyond importance discrimination collapse, we examine whether head pruning also redistributes the attention entropy of surviving heads. We measure the mean attention entropy per head:
201	\begin{equation}
202	    \mathcal{H}_i^{(h)} = -\sum_{j=1}^{T} a_{ij}^{(h)} \log a_{ij}^{(h)}
203	    \label{eq:attn-entropy}
204	\end{equation}
205	and compute $\Delta\mathcal{H}$ as the change from baseline (no pruning) to the pruned condition.
206	
207	For DeepSeek under importance-based eviction, the entropy delta is consistently negative across all four sparsity levels ($\Delta\mathcal{H} \in [-0.047, -0.040]$; Table~\ref{tab:entropy-deltas}), indicating that importance-based pruning systematically selects heads whose removal concentrates attention in the surviving heads, reinforcing importance discrimination collapse.
208	
209	For Qwen, the entropy pattern only partially replicates. The delta is negative at $s{=}0.15$ ($\Delta\mathcal{H} = -0.073$) and $s{=}0.20$ ($-0.076$), consistent with DeepSeek. However, at $s{=}0.25$, the delta reverses to $+0.045$, with 22 of 30 problems showing positive entropy change. At $s{=}0.30$, the delta is near zero ($-0.007$). The $s{=}0.25$ reversal is systematic rather than a statistical artifact: it is consistent across all three reasoning phases (low: $+0.042$, mid: $+0.034$, high: $+0.017$). We interpret this as a genuine model-specific difference, possibly arising from distinct head specialization patterns: Qwen's instruction tuning (vs.\ DeepSeek's distillation-based training) may produce head configurations where removing 25\% of heads triggers compensatory broadening rather than concentration.
210	
211	We characterize importance discrimination collapse as the robust, model-independent driver of the phase-strategy interaction, with entropy redistribution as a secondary amplifier that is consistent in DeepSeek but model-dependent in Qwen.
212	
213	\begin{table}[t]
214	\centering
215	\caption{Attention entropy deltas ($\Delta\mathcal{H}$) under importance-based eviction. DeepSeek shows consistent entropy compression; Qwen partially replicates with a reversal at $s{=}0.25$.}
216	\label{tab:entropy-deltas}
217	\small
218	\begin{tabular}{llr}
219	\toprule
220	Model & $s$ & $\Delta\mathcal{H}$ \\
221	\midrule
222	DeepSeek & $0.15$ & $-0.040$ \\
223	DeepSeek & $0.20$ & $-0.047$ \\
224	DeepSeek & $0.25$ & $-0.045$ \\
225	DeepSeek & $0.30$ & $-0.044$ \\
226	\midrule
227	Qwen & $0.15$ & $-0.073$ \\
228	Qwen & $0.20$ & $-0.076$ \\
229	Qwen & $0.25$ & $+0.045$ \\
230	Qwen & $0.30$ & $-0.007$ \\
231	\bottomrule
232	\end{tabular}
233	\end{table}
234	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "98b8e0b5-0cfc-4189-9906-d3e9aaeb1f21",
  "isSidechain": true,
  "promptId": "9fc20291-e8f1-4e03-bc4b-c7922ed33096",
  "agentId": "a32bc4203578b639f",
  "type": "user",
  "uuid": "12d19387-c78b-4ce2-86d0-167c23bd5729",
  "sourceToolAssistantUUID": "98b8e0b5-0cfc-4189-9906-d3e9aaeb1f21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-16T15:50:36.638Z_

<details open><summary>🔧 Tool call — Read · `toolu_013V59Hcgce8YNZLQicPMox6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_robustness.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12d19387-c78b-4ce2-86d0-167c23bd5729",
  "isSidechain": true,
  "agentId": "a32bc4203578b639f",
  "requestId": "req_011Cb6WjqNPziZbNLBvwm3fT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6f675722-5711-453f-b706-326da2926dda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FmvQLHjTohPSFjst75W3sM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7192,
      "cache_read_input_tokens": 43175,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7192,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
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

_source line 34 · 2026-05-16T15:50:36.645Z_

<details><summary>↩ Tool result · `toolu_013V59Hcgce8YNZLQicPMox6`</summary>

```text
1	\section{Benjamini-Hochberg FDR Correction}
2	\label{app:bh-fdr}
3	
4	Table~\ref{tab:bh-fdr} compares Bonferroni ($k{=}4$, per model$\times$strategy family) and Benjamini-Hochberg FDR correction across all 44 statistical tests. BH-FDR recovers 5 additional significant results beyond Bonferroni, all in low-effect-size conditions (random eviction or cross-training-paradigm random comparisons). All 32 Bonferroni-significant results remain significant under BH-FDR.
5	
6	\begin{table}[t]
7	\centering
8	\small
9	\caption{Bonferroni vs.\ BH-FDR correction summary ($\alpha{=}0.05$, 44 tests). ``BH only'' denotes tests significant under BH-FDR but not Bonferroni.}
10	\label{tab:bh-fdr}
11	\begin{tabular}{@{}lcc@{}}
12	\toprule
13	Category & Bonf.\ sig. & BH-only sig. \\
14	\midrule
15	Per-condition Wilcoxon ($k{=}16$) & 10 & 2 \\
16	Imp vs.\ rand ($k{=}8$) & 8 & 0 \\
17	Adjacent sparsity ($k{=}12$) & 10 & 1 \\
18	Cross-paradigm Mann-Whitney ($k{=}8$) & 4 & 2 \\
19	\midrule
20	Total ($k{=}44$) & 32 & 5 \\
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	The 5 BH-only results are: DeepSeek random $s{=}0.25$ and $s{=}0.30$ per-condition Wilcoxon ($p_{\text{Bonf}}{=}0.064$/$0.065$, BH $q{=}0.002$), DeepSeek random $s{=}0.25 \to 0.30$ adjacent-sparsity step ($p_{\text{Bonf}}{=}0.078$, BH $q{=}0.002$), and cross-training-paradigm random $s{=}0.25$/$s{=}0.30$ Mann-Whitney ($p_{\text{Bonf}}{=}0.66$/$0.17$, BH $q{=}0.018$/$0.005$). All involve random eviction---the weakest effects---indicating that Bonferroni is conservative but does not miss any importance-based findings.
26	
27	
28	\section{Minimum Phase Length Sensitivity}
29	\label{app:mpl-sensitivity}
30	
31	Table~\ref{tab:mpl-sensitivity} reports the paired median difference $\Delta$ under three \texttt{min\_phase\_length} (mpl) settings across all 16 conditions (2 models $\times$ 2 strategies $\times$ 4 sparsity levels). Conclusions are robust: all importance-based conditions remain significant at $p_{\text{Bonf}} < 10^{-10}$ across mpl $\in \{5, 10, 20\}$; random conditions maintain the same significance pattern (non-significant at $s \leq 0.20$, significant at $s \geq 0.25$). Median $\Delta$ values vary by $<5\%$ between mpl settings for DeepSeek importance, supporting that the severity gradient is not an artifact of the merging threshold.
32	
33	\begin{table*}[t]
34	\centering
35	\small
36	\caption{Sensitivity of median $\Delta$ to \texttt{min\_phase\_length} (mpl). $n_{\text{eff}}$: effective sample size after exclusions. All importance-based $p_{\text{Bonf}} < 10^{-10}$; ``ns'' denotes $p_{\text{Bonf}} > 0.05$.}
37	\label{tab:mpl-sensitivity}
38	\begin{tabular}{@{}llrrrrrr@{}}
39	\toprule
40	Model & Strategy & $s$ & \multicolumn{1}{c}{mpl$=$5} & \multicolumn{1}{c}{mpl$=$10} & \multicolumn{1}{c}{mpl$=$20} & $n_{\text{eff}}$(10) & $n_{\text{eff}}$(20) \\
41	\midrule
42	DS & Imp & 0.15 & 0.391 & 0.391 & 0.393 & 496 & 433 \\
43	DS & Imp & 0.20 & 1.215 & 1.215 & 1.235 & 496 & 433 \\
44	DS & Imp & 0.25 & 3.986 & 3.986 & 4.017 & 496 & 433 \\
45	DS & Imp & 0.30 & 8.481 & 8.481 & 8.420 & 496 & 433 \\
46	\addlinespace
47	DS & Rand & 0.15 & 0.014 & 0.014\textsuperscript{ns} & 0.012\textsuperscript{ns} & 496 & 433 \\
48	DS & Rand & 0.20 & 0.031\textsuperscript{ns} & 0.031\textsuperscript{ns} & 0.023\textsuperscript{ns} & 496 & 433 \\
49	DS & Rand & 0.25 & 0.257 & 0.257 & 0.190 & 496 & 433 \\
50	DS & Rand & 0.30 & 0.510 & 0.510 & 0.410 & 496 & 433 \\
51	\addlinespace
52	QW & Imp & 0.15 & 0.066 & 0.066 & 0.066 & 475 & 289 \\
53	QW & Imp & 0.20 & 0.307 & 0.307 & 0.325 & 475 & 289 \\
54	QW & Imp & 0.25 & 1.074 & 1.074 & 1.106 & 475 & 289 \\
55	QW & Imp & 0.30 & 3.155 & 3.155 & 3.581 & 475 & 289 \\
56	\addlinespace
57	QW & Rand & 0.15 & $-$0.011\textsuperscript{ns} & $-$0.011\textsuperscript{ns} & $-$0.011\textsuperscript{ns} & 475 & 289 \\
58	QW & Rand & 0.20 & 0.015\textsuperscript{ns} & 0.015\textsuperscript{ns} & 0.015\textsuperscript{ns} & 475 & 289 \\
59	QW & Rand & 0.25 & 0.393 & 0.393 & 0.266 & 475 & 289 \\
60	QW & Rand & 0.30 & 0.913 & 0.913 & 0.788 & 475 & 289 \\
61	\bottomrule
62	\end{tabular}
63	\end{table*}
64	
65	The main effect of increasing mpl is reduced $n_{\text{eff}}$: at mpl$=$20, DeepSeek retains 433/500 problems and Qwen retains 289/500 (mid-null rate rises to 71.2\% and 84.6\%, respectively). Despite this sample reduction, all significance conclusions hold.
66	
67	
68	\section{Segmentation Robustness}
69	\label{app:seg-robust}
70	
71	Table~\ref{tab:seg-robust} reports the paired median difference $\Delta$ under tercile, quartile, and quintile segmentation for both models under importance-based eviction. Phase gradient direction and statistical significance are preserved under quartile and quintile segmentation ($n{=}50$ spot check), indicating that the tercile-based findings are not an artifact of the segmentation choice.
72	
73	\begin{table*}[t]
74	\centering
75	\small
76	\caption{Segmentation robustness: median $\Delta$ under tercile ($n{=}496$/$475$), quartile ($n{=}50$ spot check), and quintile ($n{=}50$ spot check) segmentation. Importance-based eviction; all $p_{\text{Bonf}} < 10^{-7}$.}
77	\label{tab:seg-robust}
78	\begin{tabular}{@{}llccc@{}}
79	\toprule
80	Model & $s$ & Tercile & Quartile\; [95\% CI] & Quintile\; [95\% CI] \\
81	\midrule
82	\multirow{4}{*}{DeepSeek} & 0.15 & 0.391 & 0.491\; $[0.44,\; 0.70]$ & 0.505\; $[0.33,\; 0.71]$ \\
83	& 0.20 & 1.215 & 1.388\; $[1.05,\; 1.79]$ & 1.197\; $[1.02,\; 1.76]$ \\
84	& 0.25 & 3.986 & 4.322\; $[3.62,\; 8.06]$ & 4.960\; $[3.80,\; 9.02]$ \\
85	& 0.30 & 8.481 & 12.930\; $[9.83,\; 19.10]$ & 11.548\; $[10.06,\; 18.51]$ \\
86	\addlinespace
87	\multirow{4}{*}{Qwen} & 0.15 & 0.066 & 0.226\; $[0.14,\; 0.27]$ & 0.203\; $[0.13,\; 0.26]$ \\
88	& 0.20 & 0.307 & 0.561\; $[0.35,\; 0.77]$ & 0.517\; $[0.29,\; 0.75]$ \\
89	& 0.25 & 1.074 & 1.870\; $[1.05,\; 2.44]$ & 1.801\; $[1.13,\; 2.38]$ \\
90	& 0.30 & 3.155 & 4.097\; $[2.91,\; 4.94]$ & 4.009\; $[3.28,\; 5.34]$ \\
91	\bottomrule
92	\end{tabular}
93	\end{table*}
94	
95	The quartile and quintile $\Delta$ values are comparable to or slightly larger than tercile values because finer-grained segmentation isolates more extreme phases (the ``lowest'' quintile captures a more concentrated low-sparsity segment than the lowest tercile). The monotonic dose-response ($\Delta$ increasing with $s$) is preserved across all three segmentation schemes for both models, supporting that the severity gradient is not an artifact of the tercile segmentation choice.
96	
97	
98	\section{Robustness to Asymmetric Sparsity Allocation}
99	\label{app:asymmetric-robustness}
100	
101	Our main experiments use symmetric sparsity ($s_{\text{head}} = s_{\text{KV}} = s$). To verify that the phase-gated severity gradient does not depend on this symmetric assumption, we evaluate two asymmetric configurations at a fixed total sparsity budget equivalent to $s{=}0.25$, using importance-based eviction on DeepSeek-R1-Distill-Qwen-7B.
102	
103	\begin{table}[h]
104	\centering
105	\small
106	\caption{Asymmetric sparsity robustness: per-phase II under two head/KV allocations (DeepSeek, importance-based eviction, $n{=}50$ spot check).}
107	\label{tab:asymmetric-robust}
108	\begin{tabular}{@{}lcccccc@{}}
109	\toprule
110	Config & $s_{\text{head}}$ & $s_{\text{KV}}$ & $\widetilde{\mathrm{II}}_{\textit{low}}$ & $\widetilde{\mathrm{II}}_{\textit{mid}}$ & $\widetilde{\mathrm{II}}_{\textit{high}}$ & $\Delta$ \\
111	\midrule
112	A (KV-heavy) & 0.20 & 0.30 & 19.51 & 6.05 & 0.38 & $+$19.13 \\
113	B (head-heavy) & 0.30 & 0.20 & 18.77 & 3.97 & 0.52 & $+$18.25 \\
114	\addlinespace
115	Symmetric & 0.25 & 0.25 & 3.97 & --- & 0.02 & $+$3.99 \\
116	\bottomrule
117	\end{tabular}
118	\end{table}
119	
120	Both asymmetric configurations produce large positive $\Delta$ ($+19.13$ and $+18.25$), supporting that the phase-gated severity gradient is robust to the head/KV allocation ratio. The KV-heavy configuration (A) exhibits higher mid-phase II ($6.05$ vs.\ $3.97$), suggesting that the KV eviction axis has a stronger impact on intermediate reasoning phases. Both asymmetric $\Delta$ values exceed the symmetric baseline ($3.99$), consistent with one axis operating at $s{=}0.30$---above the symmetric maximum tested---which amplifies overall severity. A systematic investigation of the full asymmetric interaction surface is left for future work.
121	
122	
123	\section{Outlier Robustness Analysis}
124	\label{app:outlier-robustness}
125	
126	The extreme mean/median ratio (up to $97{,}640{:}1$ in individual conditions) reflects heavy-tailed II distributions driven by near-zero denominators in specific problems. We verify robustness via symmetric winsorization at $5\%$ and $10\%$ levels. All median-based statistics---paired median difference $\Delta$, Wilcoxon signed-rank $p$-values, and amplification ratio $G$---are strictly invariant under winsorization, as expected for rank-based estimators. The five core claims---compound exceeds individual, importance exceeds random, monotonic dose-response, $G \gg 1$ for importance (auxiliary illustration of phase concentration), $G \approx 1$ for random---are fully robust. The extreme outlier severity further validates our choice of median-based inference over mean-based alternatives. $G$ values in this robustness analysis follow the ratio-of-medians convention (Table~\ref{tab:profiling-subset}); the primary $G$ definition (Eq.~\ref{eq:gradient}) is similarly invariant as a median of per-problem ratios.
127	
128	
129	\section{\texttt{&lt;think>} Token Phase Validation}
130	\label{app:think-validation}
131	
132	DeepSeek-R1-Distill-Qwen-7B generates explicit \texttt{&lt;think>}...\texttt{&lt;/think>} delimiters that demarcate chain-of-thought reasoning from final answers, providing a model-generated ground truth for reasoning phase boundaries. We evaluate whether our attention-sparsity-based phase segmentation (\S\ref{par:phase-segmentation}) recovers these boundaries on GSM8K ($n{=}48$ problems with valid phase assignments), using adaptive per-sequence quantile segmentation rather than a fixed global threshold.
133	
134	\paragraph{Naming convention.}
135	A note on terminology: DeepSeek's \texttt{&lt;think>} phase (active reasoning) exhibits \emph{low} attention sparsity---attention is broadly distributed across many positions during exploratory computation. Conversely, the answer phase exhibits \emph{high} attention sparsity---attention concentrates on a few positions during structured output. Thus PACS ``low-sparsity phase'' corresponds to the model's thinking phase, and ``high-sparsity phase'' to the answer phase. The physical phenomenon is consistent: broadly distributed attention characterizes reasoning in both frameworks.
136	
137	\paragraph{Token-level agreement.}
138	We binarize each token as ``thinking'' (inside \texttt{&lt;think>}) or ``answer'' (outside) and compare against the sparsity-based phase assignment. The adaptive segmentation achieves substantial agreement: $\kappa{=}0.88$ (per-problem mean $0.85$, median $0.88$), with token-level accuracy of $94.2\%$. Per-problem AUC-ROC is $0.98$ (median $0.99$), indicating near-perfect discriminability between thinking and answer phases based on attention sparsity alone. Of problems, $75\%$ achieve $\kappa \geq 0.80$ and $100\%$ achieve $\kappa \geq 0.60$. The \texttt{&lt;think>} phase exhibits significantly lower attention sparsity than the answer phase ($0.656$ vs.\ $0.763$; Cohen's $d{=}-0.80$), indicating that attention distribution breadth reliably distinguishes reasoning from structured computation.
139	
140	\paragraph{Boundary proximity.}
141	The median distance between the sparsity-based phase boundary and the nearest \texttt{&lt;think>}/\texttt{&lt;/think>} delimiter is 1 token, with $81.2\%$ of boundaries falling within 10 tokens. This tight alignment indicates that the attention sparsity transition closely tracks the model's self-identified shift from exploratory reasoning to structured answer generation.
142	
143	\paragraph{Phase composition and II correlation.}
144	We examine whether the fraction of thinking tokens within each phase correlates with compound severity (II). At the mid-phase level, the thinking-token fraction correlates with II (Spearman $\rho{=}0.49$, $p < 0.001$), consistent with mid-phase segments that contain more reasoning content being more vulnerable to compound sparsity. Low- and high-phase correlations are non-significant, as expected: these phases are compositionally dominated by thinking or answer tokens, respectively, leaving insufficient variance for correlation.
145	
146	\paragraph{MATH-500 indirect validation.}
147	Direct $\kappa$ validation requires explicit \texttt{&lt;think>} delimiters, available only on GSM8K. On MATH-500 ($n{=}500$), we instead assess \emph{temporal ordering consistency}: the fraction of problems where the low-sparsity phase precedes the high-sparsity phase, consistent with a thinking-then-answering generation structure. DeepSeek achieves a temporal ordering score of $0.576$ with $100\%$ of problems exhibiting the expected direction (low-sparsity before high-sparsity). Qwen, which lacks \texttt{&lt;think>} delimiters, shows weaker but directionally consistent temporal ordering ($0.479$). This indirect evidence supports the validity of sparsity-based phase segmentation on MATH-500 but does not constitute direct $\kappa$ validation.
148	
149	\paragraph{Scope.}
150	The direct $\kappa$ validation ($\kappa{=}0.88$, $n{=}48$) is limited to DeepSeek-R1-Distill-Qwen-7B on GSM8K; MATH-500 has only indirect (temporal ordering) validation. Qwen2.5-7B-Instruct does not produce explicit reasoning delimiters, precluding direct $\kappa$ validation on either benchmark. Phase segmentation is computed on the dense model's attention patterns and is independent of sparsity level, so the agreement statistics are reported once rather than per-$s$.
151	
152	
153	\subsection{Non-Think Token Quality Under Compound Sparsity}
154	\label{app:nt-samples}
155	
156	Tokens generated outside \texttt{&lt;think>}...\texttt{&lt;/think>} delimiters---i.e., the final answer tokens---fall predominantly in the high-sparsity attention phase, where compound interaction is minimal (\S\ref{sec:answer-region}: 93.2\% of \verb|\boxed{}| markers reside in the high-sparsity phase). We illustrate the differential impact of compound sparsity on non-think (answer) versus think (reasoning) tokens with two representative examples from the GSM8K validation set (DeepSeek-R1-Distill-Qwen-7B, $s{=}0.25$, importance-based eviction).
157	
158	\paragraph{Example 1: Preserved answer, degraded reasoning.}
159	Under compound sparsity, the non-think answer tokens (\texttt{The answer is 42}) are generated with near-baseline perplexity (PPL ratio $1.2{\times}$), while the preceding think-phase tokens exhibit $4.8{\times}$ PPL inflation. The final answer remains correct despite substantial reasoning-trace degradation---a ``silent reasoning error'' scenario where intermediate logic is corrupted but the output format masks the damage.
160	
161	\paragraph{Example 2: Cascading failure at high sparsity.}
162	At $s{=}0.30$, reasoning-phase PPL inflation ($11.3{\times}$) propagates into the answer phase: the model produces a syntactically valid but numerically incorrect \verb|\boxed{}| output (PPL ratio $3.1{\times}$ on answer tokens vs.\ $1.1{\times}$ at $s{=}0.15$). This illustrates the sparsity threshold beyond which compound severity breaches the phase boundary, consistent with the accuracy cliff observed for Qwen at $s{=}0.30$ ($\delta{=}-27$\,pp; Table~\ref{tab:accuracy}).
163	
164	\paragraph{Implication.}
165	These examples illustrate that pruning-induced compound severity is phase-selective: non-think tokens are relatively protected at moderate sparsity ($s \leq 0.25$) because they coincide with the high-sparsity attention phase where importance scores retain discriminative power. At higher sparsity ($s{=}0.30$), discrimination collapse (\S\ref{sec:discrimination-collapse-main}) erodes this protection, and compound severity spills into the answer phase.
166	
167	
168	\section{Amplification Ratio ($G$) Details}
169	\label{app:g-metric}
170	
171	The per-problem amplification ratio $G^{(i)} = \mathrm{II}^{(i)}_{\textit{low}} / \mathrm{II}^{(i)}_{\textit{high}}$ (Eq.~\ref{eq:gradient}) provides an auxiliary illustrative perspective on the primary metric $\Delta$. Table~\ref{tab:g-metric} reports $G$ with bootstrap 95\% CIs for all conditions. $G$ serves as a visualization aid; primary statistical evidence for the phase-modulated severity gradient is provided by $\Delta$ and the associated Wilcoxon tests (\S\ref{sec:phase-amplification}).
172	
173	\begin{table*}[t]
174	\centering
175	\small
176	\caption{Per-problem amplification ratio $G$ (median of $G^{(i)}$) with bootstrap 95\% CIs ($B{=}10{,}000$). $G$ serves as an auxiliary visualization of phase concentration; primary statistical evidence for the severity gradient is provided by the Interaction Index $\Delta$ (\S\ref{sec:phase-amplification}). $G \gg 1$ suggests phase-concentrated severity; $G \approx 1$ suggests uniform severity across phases.}
177	\label{tab:g-metric}
178	\begin{tabular}{@{}llcc@{}}
179	\toprule
180	$s$ & Strategy & $G$\; [95\% CI] (DeepSeek) & $G$\; [95\% CI] (Qwen) \\
181	\midrule
182	0.15 & Importance & $\mathbf{7.5}$\; $[4.1,\; 11.4]$ & n.d.$^{\dagger}$ \\
183	0.15 & Random     & 0.5\; $[0.4,\; 0.6]$ & 0.7\; $[0.4,\; 0.8]$ \\
184	\addlinespace
185	0.20 & Importance & $\mathbf{17.9}$\; $[12.7,\; 26.3]$ & $\mathbf{2.6}$\; $[0.5,\; 5.1]$ \\
186	0.20 & Random     & 0.8\; $[0.6,\; 0.9]$ & 0.9\; $[0.7,\; 1.0]$ \\
187	\addlinespace
188	0.25 & Importance & $\mathbf{49.1}$\; $[40.1,\; 57.8]$ & $\mathbf{9.5}$\; $[5.2,\; 14.8]$ \\
189	0.25 & Random     & 1.1\; $[1.0,\; 1.2]$ & 1.3\; $[1.2,\; 1.4]$ \\
190	\addlinespace
191	0.30 & Importance & $\mathbf{79.8}$\; $[63.3,\; 96.5]$ & $\mathbf{36.9}$\; $[25.3,\; 49.1]$ \\
192	0.30 & Random     & 1.1\; $[1.0,\; 1.3]$ & 1.3\; $[1.2,\; 1.4]$ \\
193	\bottomrule
194	\multicolumn{4}{@{}p{0.85\textwidth}}{\footnotesize $^{\dagger}$ $\widetilde{\mathrm{II}}_{\textit{high}} \approx 0$; ratio undefined ($G$ CI: $[-0.2, 0.9]$). $\Delta{=}0.07$, $p{=}8.7 \times 10^{-15}$ supports $\mathrm{II}_{\textit{low}} > \mathrm{II}_{\textit{high}}$.}
195	\end{tabular}
196	\end{table*}
197	
198	The $G$ values illustrate that phase-concentrated severity is associated with importance-based eviction ($G{=}7.5$--$79.8{\times}$ for DeepSeek, $2.6$--$36.9{\times}$ for Qwen), while random eviction suggests weak modulation at $s \geq 0.25$ ($G \approx 1.1$--$1.3$; CIs exclude 1) and near-uniform severity at $s \leq 0.20$ (CIs span or touch 1). The monotonic increase in $G$ with sparsity is consistent with the $\Delta$ dose-response in Table~\ref{tab:main-results}, but $G$ should be interpreted as a descriptive ratio rather than an independent statistical test---the formal evidence rests on the paired $\Delta$ and associated Wilcoxon tests.
199	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f675722-5711-453f-b706-326da2926dda",
  "isSidechain": true,
  "promptId": "9fc20291-e8f1-4e03-bc4b-c7922ed33096",
  "agentId": "a32bc4203578b639f",
  "type": "user",
  "uuid": "c57bae32-6f89-4e06-aea8-fccc60925006",
  "sourceToolAssistantUUID": "6f675722-5711-453f-b706-326da2926dda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-16T15:50:36.903Z_

<details open><summary>🔧 Tool call — Read · `toolu_013FRgUXAH1FdU7gADw1gtBn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c57bae32-6f89-4e06-aea8-fccc60925006",
  "isSidechain": true,
  "agentId": "a32bc4203578b639f",
  "requestId": "req_011Cb6WjqNPziZbNLBvwm3fT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dd3f714a-e995-42e1-9a70-1d499b8bcdf3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FmvQLHjTohPSFjst75W3sM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7192,
      "cache_read_input_tokens": 43175,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7192
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 172,
          "cache_read_input_tokens": 43175,
          "cache_creation_input_tokens": 7192,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7192,
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

_source line 36 · 2026-05-16T15:50:36.911Z_

<details><summary>↩ Tool result · `toolu_013FRgUXAH1FdU7gADw1gtBn`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Long-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length \cite{kwon-sosp2023, pope-mlsys2023}.
5	Two complementary responses---\emph{attention head pruning} \cite{voita-acl2019, michel-neurips2019} and \emph{KV cache eviction} \cite{snapkv-neurips2024, adakv-neurips2025}---are increasingly deployed simultaneously as \emph{compound sparsity}, but the resulting quality degradation is often super-additive \cite{spark-aaai2026, slim-icml2025}. Recent evaluations show that reasoning capabilities degrade disproportionately under compound compression \cite{unicomp-2026}, and that per-dimension safe zones intersect to form a smaller joint safe region \cite{phase-transition-compression-2026}.
6	
7	Prior work treats compound interaction magnitude as roughly constant across generation \cite{spark-aaai2026, unicomp-2026}, despite evidence that pruning sensitivity depends on representational phase \cite{decision-repr-transition-2026} and that no single sparse attention strategy dominates across generation stages \cite{sparse-frontier-2025}.
8	This assumption is problematic for reasoning models, whose chain-of-thought generations \cite{wei-neurips2022-cot} alternate between broadly distributed attention (exploratory reasoning) and sharply concentrated attention (structured computation) \cite{thinkv-iclr2026}.
9	Phase-aware methods like ThinKV \cite{thinkv-iclr2026} apply different KV strategies per phase but without considering compound interaction, while importance-based eviction itself faces challenges from score collapse \cite{hies-2025}, greedy bias \cite{greedy-bias-kvcache-2026}, and temporal dynamics \cite{lethe-aaai2026}. These methods each optimize a single pruning axis; we characterize the interaction when multiple axes are composed.
10	If compound severity varies across these phases, a uniform sparsity budget may be safe in one phase yet destructive in another.
11	
12	We find that compound sparsity severity is an emergent property of the three-way interaction among eviction strategy, reasoning phase, and sparsity level.
13	Under importance-based KV cache eviction, the Interaction Index---a measure of super-additive degradation---concentrates in low-sparsity reasoning phases and is largely absent in high-sparsity phases.
14	On DeepSeek-R1-Distill-Qwen-7B (MATH-500), the paired median difference rises from $0.39$ at $s{=}0.15$ to $8.48$ at $s{=}0.30$ (Spearman $\rho{=}1.0$; all Bonferroni-corrected $p < 0.005$).
15	The pattern replicates on Qwen2.5-7B-Instruct ($\Delta$: $0.07 \to 3.16$; all $p < 0.005$), with cross-architecture confirmation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, $n{=}250$), where the monotonic phase gradient is validated with ${\sim}25{\times}$ smaller magnitude than Qwen2-architecture models.
16	Random eviction develops a detectable phase gradient only above $s \approx 0.20$, at $2.7$--$17{\times}$ smaller magnitude than importance-based (where both strategies reach significance at $s \geq 0.25$), supporting that the dominant gradient is strategy-specific.
17	Cross-benchmark validation on GSM8K reveals consistent phase gradient direction: DeepSeek replicates the monotonic dose-response ($\Delta$: $0.24 \to 4.68$; all $p \leq 0.0003$), while Qwen shows directional consistency at $s \geq 0.25$ but is inconclusive due to generation truncation (\S\ref{sec:cross-benchmark}). Strategy specificity attenuates on GSM8K relative to MATH-500, indicating that phase modulation generalizes but its magnitude is task-dependent.
18	
19	Per-phase Gini analysis identifies \emph{importance discrimination collapse}---the degeneration of head importance scores toward uniformity under compound stress---as a correlational diagnostic of this phase--strategy divergence. Both strategies exhibit consistent Gini drops across all tested conditions, yet severity diverges by $2.7$--$17{\times}$, implicating the structural specificity of importance-based pruning as the key differentiator.
20	
21	Beyond individual findings, we contribute a \emph{phase-gated analysis framework} that decomposes compound severity by reasoning phase and eviction strategy, transforming a scalar interaction metric into a structured diagnostic. This framework---combining the Interaction Index with attention-sparsity-based phase segmentation---reveals structure in compound degradation that aggregate metrics miss, and provides practitioners with a principled basis for phase-aware sparsity allocation.
22	
23	Our contributions:
24	\begin{enumerate}[nosep,leftmargin=*]
25	    \item We characterize a \textbf{phase-modulated compound severity gradient}: importance-based eviction exhibits a monotonic dose-response ($\rho{=}1.0$; $\Delta$: $0.39 \to 8.48$) with a phase gradient $2.7$--$17{\times}$ larger than random eviction where both strategies are significant ($s \geq 0.25$) on MATH-500; the gradient direction is consistent on GSM8K, while strategy specificity attenuates (\S\ref{sec:cross-benchmark}).
26	    \item We replicate the pattern \textbf{across models and architectures}: Qwen2.5-7B-Instruct ($\Delta$: $0.07 \to 3.16$; $\rho{=}1.0$) and DeepSeek-R1-Distill-Llama-8B ($n{=}250$; monotonic gradient confirmed, ${\sim}25{\times}$ reduced magnitude; \S\ref{sec:cross-arch}).
27	    \item We identify \textbf{importance discrimination collapse} via per-phase Gini analysis as a correlational diagnostic: consistent collapse across models and strategies, with the structural specificity of importance-based pruning corresponding to the severity divergence (\S\ref{sec:analysis}).
28	    \item We validate the phase gradient on \textbf{GSM8K} for both models, finding that phase modulation is benchmark-robust while strategy specificity is task-dependent (\S\ref{sec:cross-benchmark}).
29	\end{enumerate}
30	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dd3f714a-e995-42e1-9a70-1d499b8bcdf3",
  "isSidechain": true,
  "promptId": "9fc20291-e8f1-4e03-bc4b-c7922ed33096",
  "agentId": "a32bc4203578b639f",
  "type": "user",
  "uuid": "0c886982-268c-4538-b20f-fee0974add1d",
  "sourceToolAssistantUUID": "dd3f714a-e995-42e1-9a70-1d499b8bcdf3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-16T15:50:40.372Z_

Now let me check the discussion section and also look at what actual vs. predicted data exists.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c886982-268c-4538-b20f-fee0974add1d",
  "isSidechain": true,
  "agentId": "a32bc4203578b639f",
  "requestId": "req_011Cb6WkCzeihokw2pacqijS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "acfb8a13-908f-42d8-a1cd-070943a2937a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GGzTAaaNAgBtSkGwRLsWGX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9054,
      "cache_read_input_tokens": 50367,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9054,
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

_source line 38 · 2026-05-16T15:50:42.704Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PEmS54UbTt9BF4ygxKjx85`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "acfb8a13-908f-42d8-a1cd-070943a2937a",
  "isSidechain": true,
  "agentId": "a32bc4203578b639f",
  "requestId": "req_011Cb6WkCzeihokw2pacqijS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6b86cfff-534c-4b13-86e3-8302a27c6eba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GGzTAaaNAgBtSkGwRLsWGX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9054,
      "cache_read_input_tokens": 50367,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9054,
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

_source line 39 · 2026-05-16T15:50:42.712Z_

<details><summary>↩ Tool result · `toolu_01PEmS54UbTt9BF4ygxKjx85`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Implications for deployment.}
5	A uniform compression budget implicitly accepts order-of-magnitude severity penalties during low-sparsity reasoning phases. Pilot evaluation ($n{=}30$, $s{=}0.25$; Appendix~\ref{app:pilot-mitigation}) achieved 18\% oracle recovery (95\% CI: $[-39\%, 45.8\%]$), falling below the pre-registered 30\% gate; the CI spans zero, indicating no statistically distinguishable improvement. Effective phase-aware allocation likely requires finer phase boundary estimation than current proxies provide. Additional mechanisms (e.g., strategy switching, adaptive thresholding) warrant investigation. We hypothesize that phase-modulated severity may extend to alternative attention-mass-based scoring methods (H$_2$O \cite{h2o-neurips2023}, SnapKV \cite{snapkv-neurips2024}, PyramidKV \cite{pyramidkv-colm2025}), which remains an open question for future work. Extended discussion in Appendix~\ref{app:extended-discussion}.
6	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b86cfff-534c-4b13-86e3-8302a27c6eba",
  "isSidechain": true,
  "promptId": "9fc20291-e8f1-4e03-bc4b-c7922ed33096",
  "agentId": "a32bc4203578b639f",
  "type": "user",
  "uuid": "24d4b293-fd99-48de-a25e-7a2b53485782",
  "sourceToolAssistantUUID": "6b86cfff-534c-4b13-86e3-8302a27c6eba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-16T15:50:42.807Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LrVP7hdP8vrMVLwpAAvikf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24d4b293-fd99-48de-a25e-7a2b53485782",
  "isSidechain": true,
  "agentId": "a32bc4203578b639f",
  "requestId": "req_011Cb6WkCzeihokw2pacqijS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a3dc99aa-81e2-437c-ae65-5d952ba49b9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GGzTAaaNAgBtSkGwRLsWGX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9054,
      "cache_read_input_tokens": 50367,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9054
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 187,
          "cache_read_input_tokens": 50367,
          "cache_creation_input_tokens": 9054,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9054,
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

_source line 41 · 2026-05-16T15:50:42.812Z_

<details><summary>↩ Tool result · `toolu_01LrVP7hdP8vrMVLwpAAvikf`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We showed that compound sparsity severity is not phase-invariant but exhibits an emergent phase-strategy interaction. Under importance-based eviction, the paired median difference $\Delta$ increases from $0.39$ to $8.48$ (DeepSeek, $n{=}500$; Spearman $\rho{=}1.0$) and $0.07$ to $3.16$ (Qwen, $n{=}475$), all $p < 10^{-13}$. Random eviction is $2.7$--$17{\times}$ weaker where both strategies are significant ($s \geq 0.25$; DeepSeek $15$--$17{\times}$, Qwen $2.7$--$3.5{\times}$). A model-dependent crossover on DeepSeek demonstrates that no single strategy dominates uniformly. Per-phase Gini analysis reveals importance discrimination collapse as a correlational diagnostic: despite near-identical aggregate Gini drops, severity diverges by $2.7$--$17{\times}$, implicating the structural specificity of importance-based pruning.
5	Beyond the empirical findings, the phase-gated analysis framework itself---decomposing compound severity by reasoning phase and eviction strategy---transforms a scalar interaction metric into a structured diagnostic that reveals where compound sparsity fails and why. This framework provides practitioners with a principled basis for phase-aware sparsity allocation: applying aggressive compression during high-sparsity (structured computation) phases while preserving budget during low-sparsity (exploratory reasoning) phases. Future work could explore generalization to other reasoning domains, causal validation of importance discrimination collapse, and systematic characterization of asymmetric compound interactions.
6	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a3dc99aa-81e2-437c-ae65-5d952ba49b9b",
  "isSidechain": true,
  "promptId": "9fc20291-e8f1-4e03-bc4b-c7922ed33096",
  "agentId": "a32bc4203578b639f",
  "type": "user",
  "uuid": "69008e77-ccbb-4896-92ad-f97ad8be9185",
  "sourceToolAssistantUUID": "a3dc99aa-81e2-437c-ae65-5d952ba49b9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-16T15:50:46.036Z_

Now let me check the review context yaml for the provenance of actual vs. extrapolated data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69008e77-ccbb-4896-92ad-f97ad8be9185",
  "isSidechain": true,
  "agentId": "a32bc4203578b639f",
  "requestId": "req_011Cb6Wkeb2j2jYfxq8q8tDN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e9ee3e5f-181a-461e-9153-3f299b58eaad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U8Wgf5JPYeTXLYrAYSx16y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 956,
      "cache_read_input_tokens": 59421,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 956,
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

_source line 43 · 2026-05-16T15:50:47.016Z_

<details open><summary>🔧 Tool call — Glob · `toolu_015cMv8az5NKmJYJBR5DxVh1`</summary>

```json
{
  "pattern": "**/review_context*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9ee3e5f-181a-461e-9153-3f299b58eaad",
  "isSidechain": true,
  "agentId": "a32bc4203578b639f",
  "requestId": "req_011Cb6Wkeb2j2jYfxq8q8tDN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c5eedd79-daa1-429b-91e3-b4e85d60de38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U8Wgf5JPYeTXLYrAYSx16y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 956,
      "cache_read_input_tokens": 59421,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 956,
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

_source line 44 · 2026-05-16T15:50:47.037Z_

<details><summary>↩ Tool result · `toolu_015cMv8az5NKmJYJBR5DxVh1`</summary>

```text
artifacts/dream_reports/dream_20260516T073742/best/review_context.yaml
artifacts/dream_reports/dream_20260516T073742/median/review_context.yaml
artifacts/dream_reports/dream_20260516T073742/worst/review_context.yaml
artifacts/dream_reports/dream_20260516T150210/best/review_context.yaml
artifacts/dream_reports/dream_20260516T150210/median/review_context.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c5eedd79-daa1-429b-91e3-b4e85d60de38",
  "isSidechain": true,
  "promptId": "9fc20291-e8f1-4e03-bc4b-c7922ed33096",
  "agentId": "a32bc4203578b639f",
  "type": "user",
  "uuid": "eeab4357-1ea3-4a8b-8170-e7fcb5e67059",
  "sourceToolAssistantUUID": "c5eedd79-daa1-429b-91e3-b4e85d60de38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-16T15:50:47.574Z_

<details open><summary>🔧 Tool call — Glob · `toolu_013TmdktHQ59uMt7SzEWxThf`</summary>

```json
{
  "pattern": "**/dream_reports/**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eeab4357-1ea3-4a8b-8170-e7fcb5e67059",
  "isSidechain": true,
  "agentId": "a32bc4203578b639f",
  "requestId": "req_011Cb6Wkeb2j2jYfxq8q8tDN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9c624a5d-cd55-440a-86c1-7087c3c4e97b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U8Wgf5JPYeTXLYrAYSx16y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 956,
      "cache_read_input_tokens": 59421,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 956
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 212,
          "cache_read_input_tokens": 59421,
          "cache_creation_input_tokens": 956,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 956,
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

_source line 46 · 2026-05-16T15:50:47.599Z_

<details><summary>↩ Tool result · `toolu_013TmdktHQ59uMt7SzEWxThf`</summary>

```text
artifacts/dream_reports/dream_20260514T054026/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260514T054026/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260514T054026/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260514T054026/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260514T054026/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T054026/best/experiment_data.json
artifacts/dream_reports/dream_20260514T054026/best/paper_framing.md
artifacts/dream_reports/dream_20260514T054026/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T054026/median/experiment_data.json
artifacts/dream_reports/dream_20260514T054026/median/paper_framing.md
artifacts/dream_reports/dream_20260514T054026/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T054026/worst/experiment_data.json
artifacts/dream_reports/dream_20260514T054026/worst/paper_framing.md
artifacts/dream_reports/dream_20260514T054026/logs/orchestrator.log
artifacts/dream_reports/dream_20260514T054026/best/review_report.md
artifacts/dream_reports/dream_20260514T054026/median/review_report.md
artifacts/dream_reports/dream_20260514T054026/worst/review_report.md
artifacts/dream_reports/dream_20260514T054026/meta.yaml
artifacts/dream_reports/dream_20260514T143543/logs/orchestrator.log
artifacts/dream_reports/dream_20260514T143543/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260514T143543/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260514T143543/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260514T143543/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260514T143543/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T143543/best/experiment_data.json
artifacts/dream_reports/dream_20260514T143543/best/paper_framing.md
artifacts/dream_reports/dream_20260514T143543/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260514T143543/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T143543/median/experiment_data.json
artifacts/dream_reports/dream_20260514T143543/median/paper_framing.md
artifacts/dream_reports/dream_20260514T143543/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260514T143543/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T143543/worst/experiment_data.json
artifacts/dream_reports/dream_20260514T143543/worst/paper_framing.md
artifacts/dream_reports/dream_20260514T143543/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260514T143543/best/review_report.md
artifacts/dream_reports/dream_20260514T143543/median/review_report.md
artifacts/dream_reports/dream_20260514T143543/worst/review_report.md
artifacts/dream_reports/dream_20260514T143543/meta.yaml
artifacts/dream_reports/dream_20260516T073742/logs/orchestrator.log
artifacts/dream_reports/dream_20260516T073742/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260516T073742/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260516T073742/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260516T073742/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260516T073742/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260516T073742/best/experiment_data.json
artifacts/dream_reports/dream_20260516T073742/best/paper_framing.md
artifacts/dream_reports/dream_20260516T073742/best/paper.tex
artifacts/dream_reports/dream_20260516T073742/best/paper.aux
artifacts/dream_reports/dream_20260516T073742/best/paper.out
artifacts/dream_reports/dream_20260516T073742/best/paper.pdf
artifacts/dream_reports/dream_20260516T073742/best/paper.log
artifacts/dream_reports/dream_20260516T073742/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260516T073742/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260516T073742/median/experiment_data.json
artifacts/dream_reports/dream_20260516T073742/median/paper_framing.md
artifacts/dream_reports/dream_20260516T073742/median/paper.tex
artifacts/dream_reports/dream_20260516T073742/median/paper.aux
artifacts/dream_reports/dream_20260516T073742/median/paper.out
artifacts/dream_reports/dream_20260516T073742/median/paper.pdf
artifacts/dream_reports/dream_20260516T073742/median/paper.log
artifacts/dream_reports/dream_20260516T073742/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260516T073742/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260516T073742/worst/experiment_data.json
artifacts/dream_reports/dream_20260516T073742/worst/paper_framing.md
artifacts/dream_reports/dream_20260516T073742/worst/paper.tex
artifacts/dream_reports/dream_20260516T073742/worst/paper.aux
artifacts/dream_reports/dream_20260516T073742/worst/paper.out
artifacts/dream_reports/dream_20260516T073742/worst/paper.pdf
artifacts/dream_reports/dream_20260516T073742/worst/paper.log
artifacts/dream_reports/dream_20260516T073742/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260516T073742/best/review_context.yaml
artifacts/dream_reports/dream_20260516T073742/best/review_report.md
artifacts/dream_reports/dream_20260516T073742/logs/review_best.log
artifacts/dream_reports/dream_20260516T073742/median/review_context.yaml
artifacts/dream_reports/dream_20260516T073742/median/review_report.md
artifacts/dream_reports/dream_20260516T073742/logs/review_median.log
artifacts/dream_reports/dream_20260516T073742/worst/review_context.yaml
artifacts/dream_reports/dream_20260516T073742/worst/review_report.md
artifacts/dream_reports/dream_20260516T073742/logs/review_worst.log
artifacts/dream_reports/dream_20260516T073742/meta.yaml
artifacts/dream_reports/dream_20260516T150210/logs/orchestrator.log
artifacts/dream_reports/dream_20260516T150210/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260516T150210/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260516T150210/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260516T150210/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260516T150210/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260516T150210/best/experiment_data.json
artifacts/dream_reports/dream_20260516T150210/best/paper_framing.md
artifacts/dream_reports/dream_20260516T150210/best/paper.tex
artifacts/dream_reports/dream_20260516T150210/best/paper.aux
artifacts/dream_reports/dream_20260516T150210/best/paper.out
artifacts/dream_reports/dream_20260516T150210/best/paper.pdf
artifacts/dream_reports/dream_20260516T150210/best/paper.log
artifacts/dream_reports/dream_20260516T150210/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260516T150210/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260516T150210/median/experiment_data.json
artifacts/dream_reports/dream_20260516T150210/median/paper_framing.md
artifacts/dream_reports/dream_20260516T150210/median/paper.tex
artifacts/dream_reports/dream_20260516T150210/median/paper.aux
(Results are truncated. Consider using a more specific path or pattern.)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9c624a5d-cd55-440a-86c1-7087c3c4e97b",
  "isSidechain": true,
  "promptId": "9fc20291-e8f1-4e03-bc4b-c7922ed33096",
  "agentId": "a32bc4203578b639f",
  "type": "user",
  "uuid": "5ceab45d-de5b-4b72-8707-d457a8dbfe7b",
  "sourceToolAssistantUUID": "9c624a5d-cd55-440a-86c1-7087c3c4e97b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-16T15:50:51.525Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BHrYsQz7m3TVaesDypb3HM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/dream_reports/dream_20260516T150210/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ceab45d-de5b-4b72-8707-d457a8dbfe7b",
  "isSidechain": true,
  "agentId": "a32bc4203578b639f",
  "requestId": "req_011Cb6Wm1wRQUKTBgYTa7pun",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "df2f78f7-83e0-428e-b1fa-1f726b777379",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JMEJmnX4fbScAptux7Z3NS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2837,
      "cache_read_input_tokens": 60377,
      "output_tokens": 105,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2837
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 105,
          "cache_read_input_tokens": 60377,
          "cache_creation_input_tokens": 2837,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2837,
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

_source line 48 · 2026-05-16T15:50:51.531Z_

<details><summary>↩ Tool result · `toolu_01BHrYsQz7m3TVaesDypb3HM`</summary>

```text
1	narrative_guidance: "原始 framing \"phase-gated compound sparsity\" 完全成立。Strategy ×\
2	  \ phase × compound 三维交互\n在三模型（DS/QW/LLaMA）、两架构（Qwen2/Llama）、三 benchmark（MATH-500/GSM8K/GPQA）上一致复现。\n\
3	  LLaMA n=250 高功效下 imp_vs_rand d_z 达中等效应量（~0.52 at s030），random phase gradient 收缩至\n\
4	  不显著（d_z~0.18），消除 n=50 的 architecture-dependent 限定。GPQA 提供跨推理领域（科学→数学）泛化，\nstrategy\
5	  \ specificity ratio ≥5× 确认 importance 的 phase-dependent compound interaction \n\
6	  不是 metric artifact 而是 genuine phenomenon。C8 升级为 confirmed，论文 claims 无需调整。\nTitle/framing\
7	  \ 保持 \"phase-gated\"，EMNLP main 正会强竞争力——novelty 同时具备现象发现（三维交互）\n和机制解释（discrimination\
8	  \ collapse），泛化证据覆盖模型/架构/任务三个维度。\n"
9	imagined_experiments:
10	- name: LLaMA n=250 Cross-Architecture Full Validation
11	  plan_id: c8_llama_n250_fixed
12	  description: 'DeepSeek-R1-Distill-Llama-8B 上 n=250 problems，8 条件（importance/random
13	    × s015/s020/s025/s030）。
14	
15	    关键验证：(1) imp_vs_rand d_z 达 medium effect；(2) 3+ sparsity Bonferroni 显著；
16	
17	    (3) random phase gradient 在 n=250 下衰减至 negligible。
18	
19	    '
20	  expected_results:
21	    model: DeepSeek-R1-Distill-Llama-8B
22	    n_problems: 250
23	    n_valid: 244
24	    n_skipped: 6
25	    conditions_completed: 8/8
26	    n_bootstrap: 10000
27	    bonferroni_k: 4
28	    imp_vs_rand_dz:
29	      s015: 0.25
30	      s020: 0.34
31	      s025: 0.44
32	      s030: 0.52
33	    imp_vs_rand_dz_ci:
34	      s015:
35	      - 0.08
36	      - 0.42
37	      s020:
38	      - 0.17
39	      - 0.51
40	      s025:
41	      - 0.27
42	      - 0.61
43	      s030:
44	      - 0.35
45	      - 0.69
46	    imp_vs_rand_dz_interpretation:
47	      s015: small
48	      s020: small_to_medium
49	      s025: medium
50	      s030: medium
51	    imp_vs_rand_dz_monotonic: true
52	    phase_gradient_importance_dz:
53	      s015: 0.95
54	      s020: 1.04
55	      s025: 1.12
56	      s030: 0.98
57	    phase_gradient_importance_dz_ci:
58	      s015:
59	      - 0.75
60	      - 1.15
61	      s020:
62	      - 0.86
63	      - 1.22
64	      s025:
65	      - 0.94
66	      - 1.3
67	      s030:
68	      - 0.82
69	      - 1.14
70	    phase_gradient_importance_interpretation: all_large
71	    phase_gradient_random_dz:
72	      s015: 0.14
73	      s020: 0.17
74	      s025: 0.2
75	      s030: 0.22
76	    phase_gradient_random_dz_ci:
77	      s015:
78	      - -0.03
79	      - 0.31
80	      s020:
81	      - 0.0
82	      - 0.34
83	      s025:
84	      - 0.03
85	      - 0.37
86	      s030:
87	      - 0.05
88	      - 0.39
89	    phase_gradient_random_interpretation: negligible_to_small
90	    phase_gradient_random_bonferroni_significant:
91	      s015: false
92	      s020: false
93	      s025: false
94	      s030: false
95	    median_diff:
96	      s015: 0.024
97	      s020: 0.055
98	      s025: 0.152
99	      s030: 0.42
100	    median_diff_ci:
101	      s015:
102	      - 0.007
103	      - 0.044
104	      s020:
105	      - 0.015
106	      - 0.112
107	      s025:
108	      - 0.058
109	      - 0.285
110	      s030:
111	      - 0.19
112	      - 0.63
113	    wilcoxon_p:
114	      s015: 0.015
115	      s020: 0.003
116	      s025: 0.00028
117	      s030: 1.5e-05
118	    wilcoxon_p_bonferroni:
119	      s015: 0.06
120	      s020: 0.012
121	      s025: 0.0011
122	      s030: 6.0e-05
123	    significant_bonferroni:
124	      s015: false
125	      s020: true
126	      s025: true
127	      s030: true
128	    bonferroni_significant_count: 3
129	    cross_arch_comparison:
130	      deepseek_qwen2_imp_vs_rand_dz_s030: 0.8
131	      llama_imp_vs_rand_dz_s030: 0.52
132	      delta: 0.28
133	      note: LLaMA effect weaker in magnitude but unambiguously medium (CI excludes
134	        zero). Architecture modulates strength but not direction.
135	  result_rationale: "n=50 时 imp_vs_rand d_z=0.19→0.34，CI 极宽（s030: [0.06, 0.66]），仅\
136	    \ s030 Bonferroni \n显著（p=0.029）。n=250 使 SE 缩小 √5≈2.24 倍，效应量估计趋于真值。三个关键机制：\n\n\
137	    (1) Random phase gradient 衰减：n=50 时 random d_z=0.35-0.44 可能被采样变异性膨胀。\nRandom masking\
138	    \ 是无差别噪声注入，不应产生与 importance 同等的 strategy-dependent phase 调制。\n在 n=250 下采样噪声被平滑，random\
139	    \ d_z 回落至 ~0.14-0.22，无一 Bonferroni 显著——\n与 DS/QW 在 n=500 下 random s015/s020 NS\
140	    \ 的模式一致。n=50 时 LLaMA random 显著\n很可能是 Type I error（多重比较 + 小样本变异性）。\n\n(2) Importance\
141	    \ gradient 稳定：c8_llama_gpu0_s025 已验证 n=250 importance s025 \nd_z=1.1174（与 n=50\
142	    \ 的 1.12 一致），确认 importance phase gradient 是 robust signal \n而非偶然。全 4 水平 d_z 维持在\
143	    \ 0.95-1.12（large effect）。\n\n(3) imp_vs_rand 提升：当 random gradient 从 ~0.44 缩至\
144	    \ ~0.22 而 importance 保持 ~1.0+，\n两者差距扩大→imp_vs_rand d_z 从 0.34 提升至 0.52。s020/s025/s030\
145	    \ 三水平获得\nBonferroni 显著性（n=250 给出 >90% power 检测 d_z≥0.35 的效应）。\n"
146	  tables:
147	  - name: LLaMA n=250 vs n=50 Effect Size Comparison
148	    columns:
149	    - sparsity
150	    - n50_imp_rand_dz
151	    - n250_imp_rand_dz
152	    - n250_bonf_p
153	    - significant
154	    rows:
155	    - - s015
156	      - 0.19
157	      - 0.25
158	      - 0.06
159	      - NS
160	    - - s020
161	      - 0.26
162	      - 0.34
163	      - 0.012
164	      - ✓
165	    - - s025
166	      - 0.29
167	      - 0.44
168	      - 0.0011
169	      - ✓
170	    - - s030
171	      - 0.34
172	      - 0.52
173	      - 6.0e-05
174	      - ✓
175	  - name: Random Phase Gradient Attenuation n=50 → n=250
176	    columns:
177	    - sparsity
178	    - n50_random_dz
179	    - n250_random_dz
180	    - n250_CI_contains_zero
181	    - bonf_significant
182	    rows:
183	    - - s015
184	      - 0.35
185	      - 0.14
186	      - 'yes'
187	      - 'no'
188	    - - s020
189	      - 0.37
190	      - 0.17
191	      - borderline
192	      - 'no'
193	    - - s025
194	      - 0.45
195	      - 0.2
196	      - 'no'
197	      - 'no'
198	    - - s030
199	      - 0.44
200	      - 0.22
201	      - 'no'
202	      - 'no'
203	  figures_description:
204	  - 'fig_c8_n250_forest.pdf: Forest plot 三架构 (DS-Qwen2/QW/LLaMA) × 4 sparsity 的 imp_vs_rand
205	    d_z 及 95% CI。LLaMA n=250 点位从 n=50 虚线位置移至 medium zone。'
206	  - 'fig_c8_random_attenuation.pdf: 左=importance dz (稳定 ~1.0)，右=random dz (从 0.35-0.44
207	    衰减至 0.14-0.22)，双 panel 对比 n=50 vs n=250。'
208	  analysis: "LLaMA n=250 解除 C8 的 architecture-dependent 限定。三个关键变化：\n(1) imp_vs_rand\
209	    \ d_z s030=0.52（medium），s020/s025/s030 Bonferroni 显著（3/4）；\n(2) random phase gradient\
210	    \ 全部无 Bonferroni 显著——与 DS/QW 模式一致；\n(3) importance gradient 稳定（d_z=0.95-1.12），与\
211	    \ c8_llama_gpu0_s025 已验证的 1.1174 吻合。\n论文可改为 \"Cross-architecture validation confirms\
212	    \ strategy×phase interaction \n(d_z=0.52, Bonferroni p<0.001 at s=0.30)\" 而非 \"\
213	    suggests/provides partial support\"。\nC8 从 partially_confirmed 升级为 confirmed。\n"
214	- name: GPQA DeepSeek Importance Phase Gradient Profiling
215	  plan_id: gpqa_ds_importance_s015
216	  description: 'DeepSeek-R1-Distill-Qwen-7B 对 GPQA-Diamond (n=50) 运行 importance masking，
217	
218	    4 sparsity levels (s015/s020/s025/s030)。验证 phase gradient 单调递增跨 benchmark。
219	
220	    '
221	  expected_results:
222	    model: DeepSeek-R1-Distill-Qwen-7B
223	    benchmark: GPQA-Diamond
224	    n_problems: 50
225	    method: median + Wilcoxon + bootstrap_median(B=10000)
226	    importance:
227	      s015:
228	        median_gradient: 0.19
229	        ci_low: 0.065
230	        ci_high: 0.39
231	        wilcoxon_p: 0.0006
232	        bonferroni_p: 0.0024
233	      s020:
234	        median_gradient: 0.58
235	        ci_low: 0.24
236	        ci_high: 0.95
237	        wilcoxon_p: 0.0002
238	        bonferroni_p: 0.0008
239	      s025:
240	        median_gradient: 1.72
241	        ci_low: 0.82
242	        ci_high: 2.55
243	        wilcoxon_p: 0.0001
244	        bonferroni_p: 0.0004
245	      s030:
246	        median_gradient: 4.15
247	        ci_low: 1.9
248	        ci_high: 8.9
249	        wilcoxon_p: 0.0001
250	        bonferroni_p: 0.0004
251	    dose_response_monotonic: true
252	    spearman_rho: 1.0
253	    bonferroni_sig_count: 4
254	    all_bonferroni_significant: true
255	  result_rationale: "GPQA-Diamond 是 graduate-level 科学推理，推理链结构介于 MATH-500（长复杂链）和 \n\
256	    GSM8K（短规律链）之间。预测 phase gradient 单调递增：\n\n(1) 物理机制不依赖 task 类型——head pruning → discrimination\
257	    \ collapse → compound interaction \n在 low-sparsity phase 最严重，此机制跨 benchmark 通用。MATH-500\
258	    \ 和 GSM8K 已 100% 单调。\n\n(2) Gradient magnitude 预计介于 MATH-500 (0.39→8.48) 和 GSM8K\
259	    \ (0.24→4.68) 之间：\nGPQA 多选题 format 使 reasoning chain 比 MATH-500 短（平均 token 更少），但科学推理\n\
260	    的知识检索步骤比 GSM8K 算术多，compound sensitivity 居中。预测 s030 ≈ 4.15。\n\n(3) 全 4 水平 Bonferroni\
261	    \ 显著——DS 在 MATH-500 n=50 时 s015 就显著 (d=0.61)，\nGPQA 虽然绝对 magnitude 略小但效应仍在 detectable\
262	    \ 范围，n=50 配合 DS 的强 signal 足够。\n"
263	  tables:
264	  - name: Cross-Benchmark Phase Gradient (DeepSeek Importance)
265	    columns:
266	    - sparsity
267	    - MATH-500_n500
268	    - GSM8K_n50
269	    - GPQA_n50
270	    rows:
271	    - - s015
272	      - 0.39
273	      - 0.241
274	      - 0.19
275	    - - s020
276	      - 1.21
277	      - 0.74
278	      - 0.58
279	    - - s025
280	      - 3.99
281	      - 1.992
282	      - 1.72
283	    - - s030
284	      - 8.48
285	      - 4.682
286	      - 4.15
287	  figures_description:
288	  - 'fig_cross_benchmark_ds.pdf: 三条 dose-response 曲线 (MATH/GSM/GPQA) 均单调递增，GPQA 居中。'
289	  analysis: 'DS GPQA gradient 0.19→4.15 单调递增（ρ=1.0），全 4 水平 Bonferroni 显著。
290	
291	    三 benchmark 全部单调复现，phase modulation 是跨推理领域的 robust finding。
292	
293	    Magnitude ordering MATH > GPQA > GSM 反映推理链复杂度对 compound sensitivity 的调制。
294	
295	    '
296	- name: GPQA Qwen Importance Phase Gradient Cross-Model
297	  plan_id: gpqa_profiling_qw
298	  description: 'Qwen2.5-7B-Instruct 对 GPQA-Diamond (n=50) importance masking，验证 cross-model
299	    复现。
300	
301	    '
302	  expected_results:
303	    model: Qwen2.5-7B-Instruct
304	    benchmark: GPQA-Diamond
305	    n_problems: 50
306	    importance:
307	      s015:
308	        median_gradient: 0.038
309	        ci_low: 0.005
310	        ci_high: 0.088
311	        wilcoxon_p: 0.018
312	        bonferroni_p: 0.072
313	      s020:
314	        median_gradient: 0.19
315	        ci_low: 0.075
316	        ci_high: 0.35
317	        wilcoxon_p: 0.0004
318	        bonferroni_p: 0.0016
319	      s025:
320	        median_gradient: 0.85
321	        ci_low: 0.42
322	        ci_high: 1.3
323	        wilcoxon_p: 0.0001
324	        bonferroni_p: 0.0004
325	      s030:
326	        median_gradient: 2.28
327	        ci_low: 1.22
328	        ci_high: 3.55
329	        wilcoxon_p: 0.0001
330	        bonferroni_p: 0.0004
331	    dose_response_monotonic: true
332	    spearman_rho: 1.0
333	    bonferroni_sig_count: 3
334	    qw_ds_ratio_s030: 0.55
335	    note: QW magnitude ~55% of DS, consistent with MATH-500 pattern (QW ~37%). GPQA
336	      ratio slightly higher because QW's science reasoning less disadvantaged than
337	      math.
338	  result_rationale: 'QW 在 MATH-500 上 gradient 为 0.066→3.155（DS 的 ~37%），在 GSM8K 上为
339	    0.039→2.092。
340	
341	    GPQA 预测 QW gradient 0.038→2.28，DS/QW 比值约 1.8×。
342	
343	
344	    QW magnitude 一贯小于 DS（Qwen2.5-7B-Instruct 的 attention head utilization 更均匀，
345	
346	    pruning 影响较分散），但方向和单调性完全一致。s015 Bonferroni 边缘不显著（p=0.072），
347	
348	    与 MATH-500 上 QW s015 CI 含零的 onset threshold 模式一致——QW 在最低 sparsity 效应弱，
349	
350	    但 s020+ 稳定显著。
351	
352	    '
353	  tables:
354	  - name: Cross-Benchmark Phase Gradient (Qwen Importance)
355	    columns:
356	    - sparsity
357	    - MATH-500_n500
358	    - GSM8K_n50
359	    - GPQA_n50
360	    rows:
361	    - - s015
362	      - 0.066
363	      - 0.039
364	      - 0.038
365	    - - s020
366	      - 0.307
367	      - 0.158
368	      - 0.19
369	    - - s025
370	      - 1.075
371	      - 1.1
372	      - 0.85
373	    - - s030
374	      - 3.155
375	      - 2.092
376	      - 2.28
377	  figures_description:
378	  - 'fig_cross_benchmark_qw.pdf: QW 三 benchmark gradient 曲线，标注 onset threshold ~s020。'
379	  analysis: 'QW GPQA 单调递增复现（ρ=1.0），3/4 Bonferroni 显著。结合 DS，两模型×三 benchmark
380	
381	    共 6 条 dose-response 曲线全部单调。QW-GPQA s030=2.28 与 QW-GSM8K s030=2.09 接近，
382	
383	    暗示 QW 跨 task 的 compound sensitivity 较稳定。
384	
385	    '
386	- name: GPQA Random Baselines and Strategy Specificity
387	  plan_id: gpqa_random_baselines
388	  description: 'DS 和 QW 对 GPQA-Diamond (n=50) 运行 random masking，计算 imp/rand ratio。
389	
390	    验证 strategy specificity ≥5×。
391	
392	    '
393	  expected_results:
394	    ds_random:
395	      s015:
396	        median_gradient: 0.024
397	        wilcoxon_p: 0.12
398	      s020:
399	        median_gradient: 0.072
400	        wilcoxon_p: 0.045
401	      s025:
402	        median_gradient: 0.24
403	        wilcoxon_p: 0.008
404	      s030:
405	        median_gradient: 0.55
406	        wilcoxon_p: 0.003
407	    qw_random:
408	      s015:
409	        median_gradient: 0.005
410	        wilcoxon_p: 0.38
411	      s020:
412	        median_gradient: 0.025
413	        wilcoxon_p: 0.15
414	      s025:
415	        median_gradient: 0.12
416	        wilcoxon_p: 0.022
417	      s030:
418	        median_gradient: 0.36
419	        wilcoxon_p: 0.006
420	    strategy_specificity_ratio_ds:
421	      s015: 7.9
422	      s020: 8.1
423	      s025: 7.2
424	      s030: 7.5
425	    strategy_specificity_ratio_qw:
426	      s015: 7.6
427	      s020: 7.6
428	      s025: 7.1
429	      s030: 6.3
430	    strategy_specificity_ratio_range: 6.3-8.1×
431	    all_ratios_above_5x: true
432	    cross_benchmark_specificity:
433	      MATH-500: 15-36×
434	      GPQA: 6.3-8.1×
435	      GSM8K: 2.3-3.8×
436	  result_rationale: "Strategy specificity ratio 的 task-dependence 与 reasoning chain\
437	    \ 结构相关：\n\n(1) MATH-500 推理链最长最复杂（竞赛数学），importance score 的 phase-dependent \ndiscrimination\
438	    \ collapse 最剧烈 → ratio 最高（15-36×）；\n\n(2) GSM8K 推理链最短最规律（小学数学），importance 和 random\
439	    \ 的差异被压缩 → \nratio 最低（2.3-3.8×）；\n\n(3) GPQA 居中——graduate-level QA 涉及多步科学推理但为多选题\
440	    \ format（答案段短），\nreasoning 部分复杂度介于两者之间。ratio 6.3-8.1× 满足 ≥5× 的 best 阈值。\n\n物理解释：GPQA\
441	    \ 的 scientific reasoning 涉及领域知识检索和逻辑链推理，importance \nscore 对这些 pattern 的编码比 random\
442	    \ 有明显优势（score collapse 使 importance 退化\n但仍保留部分 phase-dependent 判别力），但不如 MATH-500\
443	    \ 中长推理链的累积优势大。\n\nRandom baseline 在 GPQA s025+ 产生可测 compound effect（p<0.05），但\
444	    \ magnitude \n远小于 importance——与 DS/QW 在 MATH-500 n=500 上 random s025 显著但 ratio\
445	    \ 15-38× \n的模式定性一致。\n"
446	  tables:
447	  - name: Strategy Specificity Ratio Across Benchmarks
448	    columns:
449	    - benchmark
450	    - ratio_range
451	    - interpretation
452	    - reasoning_chain_complexity
453	    rows:
454	    - - MATH-500
455	      - 15-36×
456	      - very_high
457	      - 长复杂链（竞赛数学）
458	    - - GPQA
459	      - 6.3-8.1×
460	      - high
461	      - 中等链（科学推理多选）
462	    - - GSM8K
463	      - 2.3-3.8×
464	      - moderate
465	      - 短规律链（小学算术）
466	  - name: GPQA imp/rand Ratio by Sparsity
467	    columns:
468	    - sparsity
469	    - DS_imp
470	    - DS_rand
471	    - DS_ratio
472	    - QW_imp
473	    - QW_rand
474	    - QW_ratio
475	    rows:
476	    - - s015
477	      - 0.19
478	      - 0.024
479	      - 7.9
480	      - 0.038
481	      - 0.005
482	      - 7.6
483	    - - s020
484	      - 0.58
485	      - 0.072
486	      - 8.1
487	      - 0.19
488	      - 0.025
489	      - 7.6
490	    - - s025
491	      - 1.72
492	      - 0.24
493	      - 7.2
494	      - 0.85
495	      - 0.12
496	      - 7.1
497	    - - s030
498	      - 4.15
499	      - 0.55
500	      - 7.5
501	      - 2.28
502	      - 0.36
503	      - 6.3
504	  figures_description:
505	  - 'fig_gpqa_specificity.pdf: 双线图 DS/QW importance vs random gradient on GPQA，阴影面积标注
506	    imp/rand ratio ≥5× zone。'
507	  - 'fig_specificity_by_task.pdf: Bar chart 三 benchmark 的 mean ratio（MATH=25×, GPQA=7.4×,
508	    GSM=3.0×），ordered by chain complexity。'
509	  analysis: "GPQA strategy specificity 6.3-8.1× 全部超过 5× 阈值，填补了 MATH (15-36×) 和 \n\
510	    GSM (2.3-3.8×) 之间的 gap。三 benchmark 形成 interpretable gradient：推理链复杂度↑ \n→ specificity\
511	    \ ratio↑。这支持 \"discrimination collapse 是 mechanism\" 的 framing——\n如果是 importance\
512	    \ metric 本身有缺陷，ratio 不应随 task difficulty 系统性变化。\nGPQA 数据使论文可以声明 \"strategy specificity\
513	    \ is a robust phenomenon (≥5×) across \ndiverse reasoning tasks\"。\n"
514	- name: Discrimination Collapse Quantitative Prediction
515	  plan_id: mechanism_gini_correlation
516	  description: "利用已完成的 c5_per_phase_gini 和 c2_n500 数据，计算 per-phase Gini_delta \n与\
517	    \ II severity 的跨模型定量相关。验证 Spearman ρ=1.0, Pearson r≥0.85。\n"
518	  expected_results:
519	    analysis_type: correlation of per-phase Gini collapse with II severity
520	    data_source: c5_per_phase_gini (n=30/model) + c2_n500 (n=500/model)
521	    ds_within_model:
522	      gini_delta_low:
523	      - -0.0163
524	      - -0.0209
525	      - -0.0313
526	      - -0.0373
527	      ii_median:
528	      - 0.3907
529	      - 1.2149
530	      - 3.9857
531	      - 8.4813
532	      spearman_rho: -1.0
533	      pearson_r: -0.94
534	      pearson_p: 0.031
535	    qw_within_model:
536	      gini_delta_low:
537	      - -0.0165
538	      - -0.02
539	      - -0.0286
540	      - -0.035
541	      ii_median:
542	      - 0.0659
543	      - 0.3073
544	      - 1.0745
545	      - 3.155
546	      spearman_rho: -1.0
547	      pearson_r: -0.96
548	      pearson_p: 0.022
549	    cross_model_pooled:
550	      n_datapoints: 8
551	      spearman_rho: -0.9
552	      pearson_r: -0.86
553	      pearson_p: 0.003
554	    cv_correlation:
555	      ds_cv_vs_ii_spearman: -1.0
556	      qw_cv_vs_ii_spearman: -1.0
557	      cross_model_cv_pearson: -0.88
558	  result_rationale: "Gini delta 和 II 的相关性有坚实的因果机制：head pruning → 剩余 head 的 importance\
559	    \ \nscore 分布更均匀（Gini 下降）→ importance-based eviction 丧失判别力 → eviction 近似\n随机 →\
560	    \ compound interaction 增大。因此 |Gini 下降| 应与 II severity 正相关。\n\n(1) DS low-phase\
561	    \ Gini delta [-0.016→-0.037] 与 II [0.39→8.48] 完美单调共变\n（Spearman ρ=-1.0 因为 Gini\
562	    \ 是负值——更负=更大 collapse=更大 II）。\nPearson r=-0.94 因两者均近似幂律增长但指数不同。\n\n(2) QW 同样单调（Gini\
563	    \ [-0.017→-0.035]，II [0.066→3.155]），Pearson r 略高(-0.96)\n因为 QW 的 II 增长在 log-scale\
564	    \ 更接近线性。\n\n(3) 跨模型 pooling (8 points) r=-0.86——DS 和 QW 共享正趋势但斜率不同（DS 单位 \nGini\
565	    \ 下降对应更大 II 增加），反映 Gini→II 传递函数是 architecture-dependent 的，\n但方向和 monotonicity\
566	    \ 是 universal 的。\n\n数据已存在（c5_per_phase_gini + c2_n500），仅需分析脚本。\n"
567	  tables:
568	  - name: Gini-II Correlation Summary
569	    columns:
570	    - scope
571	    - Spearman_ρ
572	    - Pearson_r
573	    - p_value
574	    rows:
575	    - - DS within-model
576	      - -1.0
577	      - -0.94
578	      - 0.031
579	    - - QW within-model
580	      - -1.0
581	      - -0.96
582	      - 0.022
583	    - - Cross-model pooled (n=8)
584	      - -0.9
585	      - -0.86
586	      - 0.003
587	  figures_description:
588	  - 'fig_gini_ii_scatter.pdf: |Gini_delta| vs II_median (log y-axis)，DS 圆/QW 方，按 sparsity
589	    着色。回归线及 r² 标注。'
590	  analysis: "Within-model Spearman ρ=1.0（完美单调）排除了 \"Gini 下降但 II 不增加\" 的反例。\nCross-model\
591	    \ r=-0.86 (p=0.003) 远超 r≥0.7 阈值。论文 §5 可声明 \"Gini decline \nquantitatively predicts\
592	    \ interaction severity (cross-model r=0.86, p=0.003)\"，\n将 discrimination collapse\
593	    \ 从 qualitative hypothesis 提升至 quantitative predictor。\n"
594	- name: 'C8 Status Upgrade: confirmed'
595	  plan_id: c8_upgrade
596	  description: '基于 c8_llama_n250_fixed 结果，将 C8 从 partially_confirmed 升级为 confirmed。
597	
598	    更新论文措辞和 claim table。
599	
600	    '
601	  expected_results:
602	    c8_old_status: partially_confirmed
603	    c8_new_status: confirmed
604	    language_changes:
605	      remove:
606	      - suggests
607	      - provides partial support
608	      - architecture-dependent caveat
609	      add:
610	      - confirms strategy×phase interaction across architectures
611	      - medium effect size (d_z=0.52)
612	    limitation_retained: magnitude differs across architectures (LLaMA d_z=0.52 vs
613	      Qwen2 d_z=0.80)
614	    paper_abstract_update: can claim 'generalizes across architectures' without hedging
615	  result_rationale: "C8 升级的三个充分条件在 best tier 下全部满足：\n(1) imp_vs_rand d_z ≥ 0.4 at\
616	    \ s030 → ✓ (0.52, medium effect)\n(2) ≥2 sparsity Bonferroni significant → ✓ (3/4\
617	    \ 显著)\n(3) random phase gradient 不再 Bonferroni significant → ✓ (0/4 显著)\n\nn=50\
618	    \ 时的 \"architecture-dependent\" caveat 源于两个 anomaly：(a) imp_vs_rand 弱\n(仅 s030\
619	    \ p=0.029)；(b) random 也显示 phase gradient (d_z=0.35-0.44)。\nn=250 同时解决了两者——(a)\
620	    \ 3 水平显著，(b) random 衰减至 negligible。\n这说明 n=50 的 anomaly 是统计功效不足 + 小样本变异性的产物，不是\
621	    \ architecture \n本身的差异。Strategy×phase interaction 是跨架构的 general phenomenon。\n"
622	  tables: []
623	  figures_description: []
624	  analysis: "C8 confirmed 使论文 claim table 全部为 confirmed（除 C5b future_work 和 C4 \n\
625	    partially_confirmed）。核心贡献 \"strategy×phase interaction generalizes across \narchitectures\"\
626	    \ 无需 hedging，EMNLP reviewer 不能以 \"only works on one architecture\" \ndismiss。\n"
627	- name: C9 Related Work Gap Analysis
628	  plan_id: c9_related_work
629	  description: '§2 Related Work 写作——定位与 Lethe/SparK/ThinKV/Physics of KV/HIES/R-KV
630	    的区分。
631	
632	    纯分析写作任务，无计算。
633	
634	    '
635	  expected_results:
636	    output_type: manuscript_section
637	    positioning: "唯一同时分析 pruning × eviction compound interaction 如何随 reasoning phase\
638	      \ \n和 eviction strategy 变化的工作。三维 (compound × phase × strategy) 交互分析\n是 unique\
639	      \ contribution。\n"
640	    gap_matrix:
641	      Lethe: adaptive method; no compound×phase analysis
642	      SparK: compound but uniform; no phase modulation
643	      ThinKV: single-axis phase-aware; no compound interaction
644	      Physics_of_KV: compression-rate phase transition (different 'phase' semantics)
645	      HIES: single-axis score collapse; no compound amplification
646	      R-KV: task-specific optimization; not mechanistic analysis
647	  result_rationale: "C9 是 writing task。在 best tier 下 positioning 清晰无争议——没有 prior work\
648	    \ 同时\n分析三个维度。关键区分：our \"phase\" = reasoning phase（temporal），Physics of KV \n\"\
649	    phase\" = compression-rate critical point（parametric）——语义正交。\nHIES 的 score collapse\
650	    \ 发现反而是 supporting evidence，不是 prior art。\n"
651	  tables: []
652	  figures_description: []
653	  analysis: §2 通过 6 篇工作的精确区分完成 novelty positioning。无需额外实验。
654	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df2f78f7-83e0-428e-b1fa-1f726b777379",
  "isSidechain": true,
  "promptId": "9fc20291-e8f1-4e03-bc4b-c7922ed33096",
  "agentId": "a32bc4203578b639f",
  "type": "user",
  "uuid": "7029fe03-ad8d-47da-bde5-0deec070bd69",
  "sourceToolAssistantUUID": "df2f78f7-83e0-428e-b1fa-1f726b777379",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-16T15:50:55.851Z_

Now I have a comprehensive understanding of the paper. Let me also check what actual experiment data exists vs. what's in the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7029fe03-ad8d-47da-bde5-0deec070bd69",
  "isSidechain": true,
  "agentId": "a32bc4203578b639f",
  "requestId": "req_011Cb6WmHyKn2BkTrfxZeGqK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2c23ce20-f6e2-47b5-819a-f3bd0b8d5bdc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013DvFswFZmKJDzmYshQUbGH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11031,
      "cache_read_input_tokens": 63214,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11031,
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

_source line 50 · 2026-05-16T15:50:57.805Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01JsfB135XoMMWKBkRw24ihy`</summary>

```json
{
  "pattern": "**/c8_llama*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c23ce20-f6e2-47b5-819a-f3bd0b8d5bdc",
  "isSidechain": true,
  "agentId": "a32bc4203578b639f",
  "requestId": "req_011Cb6WmHyKn2BkTrfxZeGqK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f72255cb-eff3-43e3-a54f-775e359fbb9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013DvFswFZmKJDzmYshQUbGH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11031,
      "cache_read_input_tokens": 63214,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11031,
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

_source line 51 · 2026-05-16T15:50:57.825Z_

<details><summary>↩ Tool result · `toolu_01JsfB135XoMMWKBkRw24ihy`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f72255cb-eff3-43e3-a54f-775e359fbb9e",
  "isSidechain": true,
  "promptId": "9fc20291-e8f1-4e03-bc4b-c7922ed33096",
  "agentId": "a32bc4203578b639f",
  "type": "user",
  "uuid": "a75e12dc-187c-4019-af48-86b38e2c2ac8",
  "sourceToolAssistantUUID": "f72255cb-eff3-43e3-a54f-775e359fbb9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-16T15:50:59.260Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01XcwDY8UieuFdpN9sZPgJMn`</summary>

```json
{
  "pattern": "extrapolat|predicted|pilot|imagined|pending",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a75e12dc-187c-4019-af48-86b38e2c2ac8",
  "isSidechain": true,
  "agentId": "a32bc4203578b639f",
  "requestId": "req_011Cb6WmHyKn2BkTrfxZeGqK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c01e93a2-40a7-4d47-afa1-15e03eb11008",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013DvFswFZmKJDzmYshQUbGH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11031,
      "cache_read_input_tokens": 63214,
      "output_tokens": 252,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11031
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 252,
          "cache_read_input_tokens": 63214,
          "cache_creation_input_tokens": 11031,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11031,
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

_source line 53 · 2026-05-16T15:50:59.280Z_

<details><summary>↩ Tool result · `toolu_01XcwDY8UieuFdpN9sZPgJMn`</summary>

```text
artifacts/_project/paper/discussion.tex:5:[Omitted long matching line]
artifacts/_project/paper/appendix_moved.tex:161:\paragraph{Scope and pending conditions.}
artifacts/_project/paper/appendix_disc_analysis.tex:21:\label{app:pilot-mitigation}
artifacts/_project/paper/appendix_disc_analysis.tex:56:Our primary analysis spans $s \in \{0.15, 0.20, 0.25, 0.30\}$; pilot data at $s{=}0.10$ and $s{=}0.35$ exist (6 total sparsity levels) but are not included in the main analysis due to limited sample size at these boundary conditions. Monotonicity is established at the tested sparsity levels (JT test $p \ll 10^{-10}$); the functional form of $G(s)$ between and beyond these levels is not characterized.
artifacts/_project/paper/results.tex:103:\caption{Median of per-problem paired severity differences ($\Delta$) under importance-based eviction on Qwen2.5-14B-Instruct (MATH-500). \textit{Results pending.}}
artifacts/_project/paper/results.tex:136:\caption{Median of per-problem paired severity differences ($\Delta$) under importance-based eviction on GPQA Diamond. \textit{Results pending.}}
artifacts/_project/paper/main.aux:596:\@writefile{lot}{\contentsline {table}{\numberline {3}{\ignorespaces Median of per-problem paired severity differences ($\Delta $) under importance-based eviction on Qwen2.5-14B-Instruct (MATH-500). \textit  {Results pending.}}}{6}{table.caption.16}\protected@file@percent }
artifacts/_project/paper/main.aux:597:\newlabel{tab:scale-14b}{{3}{6}{Median of per-problem paired severity differences ($\Delta $) under importance-based eviction on Qwen2.5-14B-Instruct (MATH-500). \textit {Results pending.}}{table.caption.16}{}}
artifacts/_project/paper/main.aux:651:\@writefile{lot}{\contentsline {table}{\numberline {4}{\ignorespaces Median of per-problem paired severity differences ($\Delta $) under importance-based eviction on GPQA Diamond. \textit  {Results pending.}}}{7}{table.caption.18}\protected@file@percent }
artifacts/_project/paper/main.aux:652:\newlabel{tab:gpqa-results}{{4}{7}{Median of per-problem paired severity differences ($\Delta $) under importance-based eviction on GPQA Diamond. \textit {Results pending.}}{table.caption.18}{}}
artifacts/_project/paper/main.aux:1547:\@writefile{toc}{\contentsline {paragraph}{Scope and pending conditions.}{16}{section*.47}\protected@file@percent }
artifacts/_project/paper/main.aux:1684:\newlabel{app:pilot-mitigation}{{K}{18}{Pilot Mitigation Experiment}{appendix.K}{}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c01e93a2-40a7-4d47-afa1-15e03eb11008",
  "isSidechain": true,
  "promptId": "9fc20291-e8f1-4e03-bc4b-c7922ed33096",
  "agentId": "a32bc4203578b639f",
  "type": "user",
  "uuid": "1316cc40-c5f0-4780-b48e-553e89d5ff00",
  "sourceToolAssistantUUID": "c01e93a2-40a7-4d47-afa1-15e03eb11008",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 54 · 2026-05-16T15:51:02.650Z_

Now I have enough information to write a thorough review. Let me check one more thing -- the LLaMA table in the paper vs the review context claim about what's actual data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1316cc40-c5f0-4780-b48e-553e89d5ff00",
  "isSidechain": true,
  "agentId": "a32bc4203578b639f",
  "requestId": "req_011Cb6WmriKM5E7pDnsq4DLn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d4427a7f-e717-40ff-8e74-ab1098ecfa7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MKKBWo3Br3LMMGxSnwce5U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1081,
      "cache_read_input_tokens": 74245,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1081,
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

_source line 55 · 2026-05-16T15:51:04.300Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Dyxzw1PZRivgZGjbgnFV91`</summary>

```json
{
  "pattern": "s015|s020|0\\\\.15.*0\\\\.20",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex",
  "output_mode": "content",
  "-C": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4427a7f-e717-40ff-8e74-ab1098ecfa7e",
  "isSidechain": true,
  "agentId": "a32bc4203578b639f",
  "requestId": "req_011Cb6WmriKM5E7pDnsq4DLn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8ee308e0-6020-4471-b7b9-1ac7bdcc6caa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MKKBWo3Br3LMMGxSnwce5U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1081,
      "cache_read_input_tokens": 74245,
      "output_tokens": 202,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1081
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 202,
          "cache_read_input_tokens": 74245,
          "cache_creation_input_tokens": 1081,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1081,
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

_source line 56 · 2026-05-16T15:51:04.321Z_

<details><summary>↩ Tool result · `toolu_01Dyxzw1PZRivgZGjbgnFV91`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8ee308e0-6020-4471-b7b9-1ac7bdcc6caa",
  "isSidechain": true,
  "promptId": "9fc20291-e8f1-4e03-bc4b-c7922ed33096",
  "agentId": "a32bc4203578b639f",
  "type": "user",
  "uuid": "2cd53edf-86e4-4e76-8178-2104b36bb5bc",
  "sourceToolAssistantUUID": "8ee308e0-6020-4471-b7b9-1ac7bdcc6caa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 57 · 2026-05-16T15:52:10.934Z_

Based on my comprehensive reading of the paper, the review context, and the provenance documentation, I can now provide my review.

---

## Review: "Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models"

### Summary

This paper introduces a phase-gated analysis framework to characterize how compound sparsity (simultaneous head pruning + KV cache eviction) interacts with reasoning phase structure in 7-8B parameter LLMs. The core finding is that severity concentrates in low-sparsity (exploratory reasoning) phases under importance-based eviction, with monotonic dose-response across sparsity levels. The paper provides a correlational mechanistic account via "importance discrimination collapse." The experimental breadth is notable (2-3 models, 3 benchmarks, 4 sparsity levels), though depth is uneven across conditions.

### Strengths

- **Well-formulated metric**: The Interaction Index (Eq. 1) is clean, interpretable, and grounded in the additivity assumption. The authors appropriately validate under both additive and multiplicative nulls.

- **Principled statistical methodology**: The use of Wilcoxon signed-rank tests (respecting non-normality of II distributions), bootstrap CIs at problem-level, and multiple testing correction is appropriate for this heavily right-skewed data. The choice of median over mean is well-justified (mean/median ratio up to 97,640:1).

- **Thorough robustness analysis**: Phase segmentation is validated against think-tokens (kappa=0.88), robustness to segmentation granularity (tercile/quartile/quintile), minimum phase length, and asymmetric sparsity allocation. The BH-FDR secondary analysis is a good practice.

- **Honest limitations**: The authors acknowledge the H2O confound (circular dependency between pruning and scoring), partial entropy replication on Qwen (2/4), the correlational nature of the mechanism, and truncation confounds on DeepSeek accuracy. This reflexivity strengthens the paper.

- **Strong primary results**: The MATH-500 n=496/475 results are compelling -- monotonic dose-response with all Bonferroni p < 10^{-10}, large effect sizes, cross-model replication within the same architecture family.

### Weaknesses

**W1. Incomplete experiments presented as sections.** Tables 3 and 4 (Qwen2.5-14B, GPQA Diamond) contain only "---" placeholders with "Results pending." These empty tables should not appear in a submission. The paper's framing (abstract, introduction) implies cross-benchmark validation on GPQA that does not yet exist in the manuscript. The LLaMA cross-architecture table (Table in Appendix F) reports only s=0.25 with a footnote stating other conditions "confirm monotonic gradient" without data. This creates an asymmetry between claims and evidence.

**W2. Cohen's d_z computation is non-standard.** The paper reports d_z = G-hat / SD(G) where G-hat is the *median*. Standard Cohen's d_z uses mean/SD of differences. While using the median is defensible given skewness, calling it "Cohen's d_z" without qualification is misleading. The reported d_z values (1.0-1.2 from the review context summary) may not be directly comparable to standard benchmarks for interpreting effect size magnitudes. The paper should either use the standard definition on appropriately transformed data or clearly state this is a "robust d_z" analogue.

**W3. Narrow architecture and scale coverage relative to claims.** The primary results come from two models sharing the identical Qwen2 backbone (28 layers, 28 heads, 4-group GQA). Qwen2.5-7B-Instruct and DeepSeek-R1-Distill-Qwen-7B differ only in training objective. The LLaMA results (single sparsity level fully reported) show 25x smaller magnitude, raising the question of whether the phenomenon is practically meaningful on non-Qwen2 architectures. The "cross-architecture" claim rests on incomplete data.

**W4. The "universality" framing is overstated for the evidence base.** The abstract claims the pattern "generalizes" to LlamaForCausalLM but with 25x reduced magnitude -- this is arguably a different regime. The 14B scale analysis is entirely missing. GPQA is missing. The GSM8K Qwen results are "inconclusive due to generation truncation." The paper's strongest evidence comes from a single architecture family on a single benchmark.

**W5. Perplexity-only primary metric.** The Interaction Index is perplexity-based. The accuracy validation (Section 4.8) reveals that the PPL signal does not straightforwardly translate: Qwen shows gradual decline through s=0.25 then a cliff at s=0.30, while DeepSeek accuracy is confounded by truncation. This non-linear mapping between the continuous PPL metric and discrete accuracy suggests the practical implications may be less clear than the phase-gradient story implies.

**W6. No throughput measurements.** For a paper motivated by efficient inference deployment, the absence of any latency/throughput measurements (acknowledged in Limitations) is a gap. The practical value of phase-aware allocation cannot be assessed without knowing the cost.

**W7. The discrimination collapse mechanism is weakly supported.** Both strategies show near-identical Gini drops (e.g., DeepSeek s=0.25: -0.065 vs -0.060), yet severity diverges 15-17x. The paper acknowledges this mismatch but still positions Gini collapse as the explanatory mechanism. The structural specificity argument (Mann-Whitney on pruned vs. retained head Gini) is interesting but does not close the explanatory gap. The paper is forthright about this being correlational, but the framing still implies more explanatory power than warranted.

**W8. Phase segmentation circularity concern.** Phases are defined by attention sparsity of the *dense* model. Under compound sparsity, attention patterns change. The paper does not address whether the dense-model phase assignments remain valid proxies for the pruned model's computational structure. The think-token validation (kappa=0.88) is performed only on GSM8K (n=48), not on the primary MATH-500 benchmark.

### Questions for Authors

**Q1.** The LLaMA table reports only s=0.25 with a footnote about other conditions. What are the actual s=0.15 and s=0.20 numerical values? Are random eviction experiments complete for LLaMA?

**Q2.** The paper uses d_z = median / SD. Can you report standard Cohen's d_z (mean/SD) alongside, or provide justification for why the standard definition is inappropriate here? At minimum, could you report the effect on a rank-transformed scale?

**Q3.** What fraction of the GSM8K/GPQA results mentioned in the abstract and introduction are from completed experiments vs. pending/planned? The review context suggests significant portions may be extrapolated from pilots.

**Q4.** The 25x magnitude reduction on LLaMA -- does this mean compound sparsity severity is practically negligible on this architecture? What does a Delta=0.38 correspond to in absolute PPL terms?

**Q5.** Can you provide the downstream accuracy under compound sparsity for a condition where phase-aware allocation (backed by your framework) is used, compared to uniform allocation? Even a pilot result would strengthen the practical motivation.

**Q6.** The pilot mitigation experiment (Appendix K) failed its pre-registered 30% gate (CI spans zero). Does this undermine the practical utility claim?

### Missing Experiments or Analyses

1. **Complete the GPQA and 14B experiments** -- these are currently empty placeholders that weaken the submission.
2. **LLaMA random eviction + remaining sparsity levels** -- needed to complete the cross-architecture claim.
3. **Phase-aware vs. uniform allocation downstream accuracy comparison** -- at least a proof-of-concept showing the framework yields actionable improvements.
4. **Throughput measurements** -- even basic tokens/sec under the tested sparsity configurations.
5. **Effect of generation length on the phase gradient** -- the paper hints that longer traces have stronger effects (Spearman rho > 0 for length vs. specificity) but does not systematically characterize this.
6. **A second non-Qwen2 architecture at full coverage** (e.g., Mistral, Gemma) to validate "cross-architecture generalization."

### Scores

**Soundness: 3 (Acceptable)**
The core MATH-500 methodology is sound -- appropriate non-parametric tests, bootstrap CIs, Bonferroni correction, robustness checks. However, incomplete experiments (GPQA, 14B, LLaMA full suite), the non-standard d_z usage, and placeholder tables in a submitted manuscript reduce confidence. The mechanism (Gini collapse) is acknowledged as correlational but framing sometimes implies more.

**Excitement: 3 (Ambivalent)**
The observation that compound sparsity severity is phase-dependent is genuinely interesting and practically relevant. The phase-gated analysis framework is a useful conceptual contribution. However, the phenomenon appears architecture-specific in magnitude (25x variation), the practical implications are unvalidated (pilot mitigation failed), and the paper covers well-trodden ground (building on H2O, SparK, ThinKV) with an analytical rather than methodological contribution.

**Overall: 3 (Borderline)**
The paper has a solid empirical core (MATH-500, two Qwen2-family models) with appropriate statistics and honest limitations. However, the submitted manuscript contains empty result tables, incomplete cross-architecture validation, a failed pilot mitigation, and overclaims relative to its actual evidence base. The gap between the abstract's scope (3 models, 3 benchmarks, cross-architecture generalization) and the completed experiments (primarily 2 Qwen2-family models on MATH-500) is the main concern. With completed experiments and moderated claims, this could be a solid EMNLP contribution.

**Confidence: 4 (High)**
I am familiar with the compound sparsity / KV cache compression literature, non-parametric statistical methodology, and the models/benchmarks used. My assessment of the statistical methods and experimental completeness is well-grounded.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2cd53edf-86e4-4e76-8178-2104b36bb5bc",
  "isSidechain": true,
  "agentId": "a32bc4203578b639f",
  "requestId": "req_011Cb6WnEUkwzfHy1GHi648c",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ec9a08b1-f0f0-491a-8e5e-cc9f4ff8dc42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016TEUPVK1MAwN5SDTvM6jFN",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 217,
      "cache_read_input_tokens": 75326,
      "output_tokens": 2446,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 217
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2446,
          "cache_read_input_tokens": 75326,
          "cache_creation_input_tokens": 217,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 217,
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
